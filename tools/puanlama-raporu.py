"""Puanlama olcumunun raporu: sapma, egilim, tutarsizlik.

Kullanim:  python tools/puanlama-raporu.py <tur-no>

Okur:  kalibrasyon/olcum/tur<N>/*.json   (her dosya bir puanlama)
       kalibrasyon/ornekler/**/*.json    (gercek band puanlari)
       kalibrasyon/olcum/kumeler.json    (varsa: S1/S2/S3 bolmesi)
Yazar: kalibrasyon/olcum/RAPOR-tur<N>.md

Hesaplari model degil bu script yapar. Sebep: ayni isin daha once elle
yapilan bir surumunde puanlama hatasi cikti ve ham ciktiya bakip karar
vermek yanlis sonuc verdi.
"""

import datetime
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402


def gercek_bandlar():
    tablo = {}
    for p in ortak.bul("kalibrasyon/ornekler/**/*.json"):
        d = ortak.oku(p)
        if d.get("kind") != "official_scored_sample":
            continue
        kod = os.path.basename(p)[:-5]
        tablo[kod] = {
            "band": d.get("band"),
            "skill": d.get("skill"),
            "suspect": bool(d.get("transcription_suspect")),
        }
    return tablo


def kumeler():
    p = ortak.yol("kalibrasyon", "olcum", "kumeler.json")
    if not os.path.exists(p):
        return {}
    with open(p, encoding="utf-8") as f:
        d = json.load(f)
    tablo = {}
    for kume, kodlar in d.items():
        for k in kodlar:
            tablo[k] = kume
    return tablo


def yarim_banda(x):
    return round(x * 2) / 2


def ozetle(farklar):
    """farklar: isaretli fark listesi (tahmin - gercek)."""
    if not farklar:
        return None
    mutlak = [abs(f) for f in farklar]
    return {
        "n": len(farklar),
        "ortalama_mutlak_fark": round(sum(mutlak) / len(mutlak), 3),
        "egilim": round(sum(farklar) / len(farklar), 3),
        "en_buyuk_sapma": round(max(mutlak), 2),
    }


def main():
    if len(sys.argv) < 2:
        print("Kullanim: python tools/puanlama-raporu.py <tur-no>")
        return 2
    tur = sys.argv[1]

    dizin = ortak.yol("kalibrasyon", "olcum", "tur%s" % tur)
    dosyalar = sorted(glob.glob(os.path.join(dizin, "*.json")))
    if not dosyalar:
        print("HATA: %s bos. Once puanlamalari yaz." % dizin)
        return 1

    gercek = gercek_bandlar()
    kume = kumeler()
    if not gercek:
        print("HATA: kalibrasyon/ornekler/ altinda puanli ornek yok.")
        return 1

    # ornek kodu -> verilen puanlar
    puanlar, eksik, suspect_atlanan = {}, [], []
    for p in dosyalar:
        with open(p, encoding="utf-8") as f:
            d = json.load(f)
        kod = d.get("sample")
        if kod not in gercek:
            eksik.append(kod)
            continue
        if gercek[kod]["suspect"]:
            suspect_atlanan.append(kod)
            continue
        b = d.get("predicted_band")
        if b is None:
            continue
        puanlar.setdefault(kod, []).append(float(b))

    if not puanlar:
        print("HATA: eslesen puanlama bulunamadi.")
        return 1

    # Urun davranisi TEK SEFERLIK: her orneğin ILK puani ayri raporlanir.
    tek_farklar, ort_farklar, satirlar = [], [], []
    beceri_farklari, kume_farklari, yayilimlar = {}, {}, []
    for kod, liste in sorted(puanlar.items()):
        g = float(gercek[kod]["band"])
        tek = liste[0]
        ort = sum(liste) / len(liste)
        tek_farklar.append(tek - g)
        ort_farklar.append(ort - g)
        yayilim = max(liste) - min(liste)
        yayilimlar.append(yayilim)
        beceri_farklari.setdefault(gercek[kod]["skill"], []).append(tek - g)
        if kod in kume:
            kume_farklari.setdefault(kume[kod], []).append(tek - g)
        satirlar.append((kod, gercek[kod]["skill"], kume.get(kod, "-"), g,
                         tek, round(ort, 2), len(liste), round(yayilim, 2)))

    tek_ozet = ozetle(tek_farklar)
    ort_ozet = ozetle(ort_farklar)
    en_buyuk = max(abs(s[4] - s[3]) for s in satirlar)
    yayilim_ort = sum(yayilimlar) / len(yayilimlar) if yayilimlar else 0

    olcut = [
        ("Ortalama mutlak fark < 0,5 band", tek_ozet["ortalama_mutlak_fark"] < 0.5),
        ("Hicbir ornekte >= 1,5 band sapma yok", en_buyuk < 1.5),
        ("Egilim +-0,25 band icinde", abs(tek_ozet["egilim"]) <= 0.25),
        ("Ayni cevaba verilen puanlarin yayilimi <= 0,5", yayilim_ort <= 0.5),
    ]

    m = []
    m.append("# Puanlama olcumu — tur %s (%s)" % (tur, datetime.date.today().isoformat()))
    m.append("")
    m.append("Olculen ornek: **%d** | toplam puanlama: **%d**"
             % (len(puanlar), sum(len(v) for v in puanlar.values())))
    if suspect_atlanan:
        m.append("")
        m.append("⚠️ Dokumu supheli oldugu icin atlanan ornek: %s"
                 % ", ".join(sorted(set(suspect_atlanan))))
    if eksik:
        m.append("")
        m.append("⚠️ Ornek dosyasi bulunamayan puanlama: %s" % ", ".join(sorted(set(eksik))))
    m.append("")
    m.append("## Urunun gercek davranisi (tek seferlik puan)")
    m.append("")
    m.append("| Olcu | Deger |")
    m.append("|---|---|")
    m.append("| Ortalama mutlak fark | **%.3f band** | " % tek_ozet["ortalama_mutlak_fark"])
    m.append("| Egilim (+ comert / − cimri) | **%+.3f band** |" % tek_ozet["egilim"])
    m.append("| En buyuk tek sapma | **%.2f band** |" % en_buyuk)
    m.append("| Ayni cevaptaki yayilim (ort.) | **%.2f band** |" % yayilim_ort)
    m.append("")
    m.append("## Tani amacli (tekrarlarin ortalamasi)")
    m.append("")
    m.append("Ortalama mutlak fark %.3f · egilim %+.3f — bu satir SADECE tani icindir; "
             "kullanici uzerinde tek puan gorur." % (ort_ozet["ortalama_mutlak_fark"],
                                                    ort_ozet["egilim"]))
    m.append("")
    m.append("## Basari olcutleri")
    m.append("")
    m.append("| Olcut | Sonuc |")
    m.append("|---|---|")
    for ad, gecti in olcut:
        m.append("| %s | %s |" % (ad, "✅ gecti" if gecti else "🔴 KALDI"))
    m.append("")
    if beceri_farklari:
        m.append("## Beceri bazinda")
        m.append("")
        m.append("| Beceri | n | Ortalama mutlak fark | Egilim |")
        m.append("|---|---|---|---|")
        for b, f in sorted(beceri_farklari.items()):
            o = ozetle(f)
            m.append("| %s | %d | %.3f | %+.3f |"
                     % (b, o["n"], o["ortalama_mutlak_fark"], o["egilim"]))
        m.append("")
    if kume_farklari:
        m.append("## Kume bazinda (sakli kume kontrolu)")
        m.append("")
        m.append("| Kume | n | Ortalama mutlak fark | Egilim |")
        m.append("|---|---|---|---|")
        for k, f in sorted(kume_farklari.items()):
            o = ozetle(f)
            m.append("| %s | %d | %.3f | %+.3f |"
                     % (k, o["n"], o["ortalama_mutlak_fark"], o["egilim"]))
        m.append("")
        m.append("🔴 Sakli kume ile acik kumeler arasinda belirgin fark varsa ayar "
                 "orneklere ezberlenmis olabilir.")
        m.append("")
    m.append("## Ornek ornek")
    m.append("")
    m.append("| Kod | Beceri | Kume | Gercek | Tek seferlik | Ortalama | Tekrar | Yayilim |")
    m.append("|---|---|---|---|---|---|---|---|")
    for s in sorted(satirlar, key=lambda x: -abs(x[4] - x[3])):
        m.append("| %s | %s | %s | %.1f | %.1f | %.2f | %d | %.2f |" % s)
    m.append("")

    cikti = "kalibrasyon/olcum/RAPOR-tur%s.md" % tur
    tam = ortak.yol(cikti)
    os.makedirs(os.path.dirname(tam), exist_ok=True)
    with open(tam, "w", encoding="utf-8") as f:
        f.write("\n".join(m) + "\n")

    print("Ornek: %d | puanlama: %d" % (len(puanlar), sum(len(v) for v in puanlar.values())))
    print("Ortalama mutlak fark (tek seferlik): %.3f" % tek_ozet["ortalama_mutlak_fark"])
    print("Egilim: %+.3f | en buyuk sapma: %.2f | yayilim: %.2f"
          % (tek_ozet["egilim"], en_buyuk, yayilim_ort))
    for ad, gecti in olcut:
        print("  %s %s" % ("[OK]  " if gecti else "[KALDI]", ad))
    print("Rapor:", cikti)
    return 0


if __name__ == "__main__":
    sys.exit(main())
