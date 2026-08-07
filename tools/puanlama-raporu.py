"""Puanlama olcumunun raporu: sapma, egilim, tutarsizlik.

Kullanim:  python tools/puanlama-raporu.py <tur-no>

Okur:  kalibrasyon/olcum/tur<N>/*.json   (her dosya bir puanlama)
       kalibrasyon/ornekler/**/*.json    (gercek band puanlari)
       kalibrasyon/olcum/kumeler.json    (varsa: S1/S2/S3 bolmesi)
Yazar: kalibrasyon/olcum/RAPOR-tur<N>.md          (tam rapor, degismedi)
       kalibrasyon/olcum/RAPOR-tur<N>-GENEL.md    (ornek tablosu/kume sapmasi YOK)
       kalibrasyon/olcum/RAPOR-tur<N>-<KUME>.md   (sadece o kumenin tablosu)

Hesaplari model degil bu script yapar. Sebep: ayni isin daha once elle
yapilan bir surumunde puanlama hatasi cikti ve ham ciktiya bakip karar
vermek yanlis sonuc verdi.

Dosyalarin bolunme sebebi: duzeltme oturumu saklı kume kore olmak zorunda
(bkz. prompts/OPUS5-A4-puanlama-duzeltmesi.md). Hepsi tek dosyada olunca
"o bolumu okuma" bir insan disiplinine dayaniyordu, kirilgandi. Artik
saklı kumenin verisi baska dosyada hic yer almiyor.
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

    def baslik_govde():
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
        return m

    def beceri_govde():
        m = []
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
        return m

    def kume_govde(sadece_kume=None):
        m = []
        satirlik = sorted(kume_farklari.items())
        if sadece_kume is not None:
            satirlik = [(k, f) for k, f in satirlik if k == sadece_kume]
        if satirlik:
            m.append("## Kume bazinda (sakli kume kontrolu)")
            m.append("")
            m.append("| Kume | n | Ortalama mutlak fark | Egilim |")
            m.append("|---|---|---|---|")
            for k, f in satirlik:
                o = ozetle(f)
                m.append("| %s | %d | %.3f | %+.3f |"
                         % (k, o["n"], o["ortalama_mutlak_fark"], o["egilim"]))
            m.append("")
            m.append("🔴 Sakli kume ile acik kumeler arasinda belirgin fark varsa ayar "
                     "orneklere ezberlenmis olabilir.")
            m.append("")
        return m

    def ornek_ornek_govde(satirlar_alt):
        m = []
        m.append("## Ornek ornek")
        m.append("")
        m.append("| Kod | Beceri | Kume | Gercek | Tek seferlik | Ortalama | Tekrar | Yayilim |")
        m.append("|---|---|---|---|---|---|---|---|")
        for s in sorted(satirlar_alt, key=lambda x: -abs(x[4] - x[3])):
            m.append("| %s | %s | %s | %.1f | %.1f | %.2f | %d | %.2f |" % s)
        m.append("")
        return m

    def dosyaya_yaz(cikti, icerik):
        tam = ortak.yol(cikti)
        os.makedirs(os.path.dirname(tam), exist_ok=True)
        with open(tam, "w", encoding="utf-8") as f:
            f.write("\n".join(icerik) + "\n")

    # 1) Tam rapor — degismedi, her seyi tek dosyada icerir (son rapor adimi bunu okur).
    tam_icerik = (baslik_govde() + beceri_govde() + kume_govde()
                  + ornek_ornek_govde(satirlar))
    dosyaya_yaz("kalibrasyon/olcum/RAPOR-tur%s.md" % tur, tam_icerik)

    # 2) Genel rapor — ornek tablosu ve kume sapmasi YOK; duzeltme oturumu her zaman acabilir.
    genel_icerik = baslik_govde() + beceri_govde()
    dosyaya_yaz("kalibrasyon/olcum/RAPOR-tur%s-GENEL.md" % tur, genel_icerik)

    # 3) Kume bazli rapor — sadece o kumenin sapma satiri ve ornek tablosu.
    for k in sorted(kume_farklari):
        satirlar_k = [s for s in satirlar if s[2] == k]
        kume_icerik = ["# Puanlama olcumu — tur %s — kume %s (%s)"
                       % (tur, k, datetime.date.today().isoformat()), ""]
        kume_icerik += kume_govde(sadece_kume=k) + ornek_ornek_govde(satirlar_k)
        dosyaya_yaz("kalibrasyon/olcum/RAPOR-tur%s-%s.md" % (tur, k), kume_icerik)

    print("Ornek: %d | puanlama: %d" % (len(puanlar), sum(len(v) for v in puanlar.values())))
    print("Ortalama mutlak fark (tek seferlik): %.3f" % tek_ozet["ortalama_mutlak_fark"])
    print("Egilim: %+.3f | en buyuk sapma: %.2f | yayilim: %.2f"
          % (tek_ozet["egilim"], en_buyuk, yayilim_ort))
    for ad, gecti in olcut:
        print("  %s %s" % ("[OK]  " if gecti else "[KALDI]", ad))
    print("Rapor: kalibrasyon/olcum/RAPOR-tur%s.md (+ -GENEL ve kume dosyalari)" % tur)
    return 0


if __name__ == "__main__":
    sys.exit(main())
