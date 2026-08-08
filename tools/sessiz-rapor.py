"""E8 2. adim: senaryosuz verilen dinleme cevaplarini anahtarla karsilastirir.

Kullanim:  python tools/sessiz-rapor.py <paket-adi> [--secim=tek|cok|hepsi]

Okur:  kalibrasyon/sessiz/<paket>-tur1.json, -tur2.json, -tur3.json
Yazar: content/DOGRULAMA/SESSIZ-<paket>.md  (+ .json ham veri)

`metinsiz-rapor.py`nin dinleme surumudur; ONUN dosyalarina dokunmaz
(dogrulama/metinsiz, kalibrasyon/metinsiz, content/DOGRULAMA/METINSIZ-* okunmaz
ve yazilmaz). Anahtar yalniz skill == "listening" dosyalarindan kurulur, boylece
ayni adli okuma paketi (multiple-choice.json her iki bacakta var) karismaz.

Bir soru UC TURUN UCUNDE de dogru bilinmisse "senaryosuz cozulebilir" sayilir.
Tek turda tutturmak sanstir; uc turda tutturmak degildir.

Iki olcut ayri raporlanir:
  K1 kelime duzeyi — cevap birebir (ya da accepted_variants'tan biri) tuttu mu.
  K3 anlam duzeyi — cevap ayni seye isaret ediyor mu (OPUS5-E10 tanimi). Bunu
     script kendi basina karar veremez; tur dosyasindaki cevap kaydinda
     "anlam": true/false varsa o kullanilir, yoksa K1 sonucuna dusulur.
     Coktan secmeli/eslestirmede cevap harf oldugundan K1 == K3.

🔴 Resmi dinleme sizinti tabani YOK: okuma tarafindaki RESMI_TABAN resmi okuma
ornek sorularindan olculmustu, dinlemede boyle bir olcum hic yapilmadi
(denetim/DENETIM-RAPORU.md §5 A3). Bu yuzden tabanla karsilastirma yapilmaz,
uydurulmus sayi da yazilmaz. Onun yerine tip "yapisal olarak tahmin edilemez"
mi diye isaretlenir: form/not/tablo tamamlamada cevap cogu zaman ozel ad, sayi
ya da saattir; oralarda dusuk oran BEKLENIR ve basari sayilmaz.
"""

import datetime
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

# Cevabi yapisal olarak tahmin edilemeyen tipler: ozel ad, sayi, saat, adres.
# Bu tiplerde dusuk parcasiz-bilinme orani beklenir, basari sayilmaz.
TAHMIN_EDILEMEZ = {
    "form_completion", "note_completion", "table_completion",
}
# Olcumun asil ilgilendigi tipler: cevap secenek havuzundan gelir, sizinti
# secenegin sozunden okunabilir.
ODAK = {
    "multiple_choice", "multiple_choice_multi", "matching",
    "matching_features", "matching_information",
}
# Metin tabanli olcumun kor oldugu tip (gorsel gerekir) — olculmez.
OLCULMEZ = {"plan_map_diagram_labelling", "diagram_labelling"}


def normal(a):
    if a is None:
        return []
    if not isinstance(a, list):
        a = [a]
    return sorted(str(x).strip().lower() for x in a)


def anahtar_yukle():
    """Tum DINLEME sorularini id -> (cevap, tip, dosya) olarak toplar."""
    tablo = {}
    for p in ortak.soru_dosyalari():
        d = ortak.oku(p)
        if d.get("skill") != "listening":
            continue
        set_id = d.get("set_id", os.path.basename(p))
        for it in ortak.sorular(d):
            sid = "%s-%s" % (set_id, it.get("number"))
            tablo[sid] = {
                "answer": it.get("answer"),
                "accepted": it.get("accepted_variants") or [],
                "type": d.get("question_type"),
                "file": p,
                "number": it.get("number"),
                "numara_sayisi": len(ortak.numaralar(it)) or 1,
            }
    return tablo


def dogru_mu(verilen, kayit):
    v = normal(verilen)
    if v == normal(kayit["answer"]):
        return True
    for alt in kayit["accepted"]:
        if v == normal(alt):
            return True
    return False


def main():
    paketler = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(paketler) != 1:
        print("Kullanim: python tools/sessiz-rapor.py <paket-adi>")
        return 2
    paket = paketler[0]
    baslik_eki = ""
    for a in sys.argv[1:]:
        if a.startswith("--baslik="):
            baslik_eki = " — " + a.split("=", 1)[1]

    turlar = []
    for n in (1, 2, 3):
        p = ortak.yol("kalibrasyon", "sessiz", "%s-tur%d.json" % (paket, n))
        if not os.path.exists(p):
            print("HATA: eksik tur dosyasi: kalibrasyon/sessiz/%s-tur%d.json" % (paket, n))
            print("Uc turun ucu de yazilmadan rapor uretilmez.")
            return 1
        with open(p, encoding="utf-8") as f:
            turlar.append(json.load(f))

    anahtar = anahtar_yukle()

    # id -> kac turda dogru (kelime duzeyi K1 / anlam duzeyi K3)
    k1, k3, bazlar, bilinmeyen = {}, {}, {}, []
    for t in turlar:
        for a in t.get("answers", []):
            sid = a.get("id")
            kayit = anahtar.get(sid)
            if kayit is None:
                bilinmeyen.append(sid)
                continue
            dogru = dogru_mu(a.get("answer"), kayit)
            k1[sid] = k1.get(sid, 0) + (1 if dogru else 0)
            anlam = a.get("anlam")
            if anlam is None:
                anlam = dogru
            k3[sid] = k3.get(sid, 0) + (1 if anlam else 0)
            if a.get("basis"):
                bazlar[a["basis"]] = bazlar.get(a["basis"], 0) + 1

    tipler = {}
    cozulebilir_k1, cozulebilir_k3 = [], []
    for sid in k1:
        tip = anahtar[sid]["type"] or "bilinmiyor"
        v = tipler.setdefault(tip, {"toplam": 0, "numara": 0, "k1": 0, "k3": 0})
        v["toplam"] += 1
        v["numara"] += anahtar[sid]["numara_sayisi"]
        if k1[sid] >= 3:
            v["k1"] += 1
            cozulebilir_k1.append(sid)
        if k3[sid] >= 3:
            v["k3"] += 1
            cozulebilir_k3.append(sid)

    toplam = sum(v["toplam"] for v in tipler.values())
    numara = sum(v["numara"] for v in tipler.values())
    u1 = sum(v["k1"] for v in tipler.values())
    u3 = sum(v["k3"] for v in tipler.values())

    s = []
    s.append("## %s%s — %s" % (paket, baslik_eki, datetime.date.today().isoformat()))
    s.append("")
    s.append("- Ölçülen soru: **%d kalem / %d numara**" % (toplam, numara))
    s.append("- Üç turun üçünde de senaryosuz bilinen — K1 kelime düzeyi: **%d** (%%%.1f)"
             % (u1, (u1 / toplam * 100) if toplam else 0))
    s.append("- Üç turun üçünde de senaryosuz bilinen — K3 anlam düzeyi: **%d** (%%%.1f)"
             % (u3, (u3 / toplam * 100) if toplam else 0))
    if bilinmeyen:
        s.append("- ⚠️ Anahtarda bulunamayan cevap kimliği: %d" % len(bilinmeyen))
    s.append("")
    s.append("| Soru tipi | K1 | Oran | K3 | Oran | Yorum |")
    s.append("|---|---|---|---|---|---|")
    for tip in sorted(tipler):
        v = tipler[tip]
        o1 = v["k1"] / v["toplam"] * 100 if v["toplam"] else 0
        o3 = v["k3"] / v["toplam"] * 100 if v["toplam"] else 0
        if tip in OLCULMEZ:
            yorum = "ölçülmedi (görsel gerekir)"
        elif tip in TAHMIN_EDILEMEZ:
            yorum = "yapısal olarak tahmin edilemez — düşük oran beklenir, başarı sayılmaz"
        elif tip in ODAK:
            yorum = "ölçümün odağı 🔴" if o3 >= 50 else "ölçümün odağı"
        else:
            yorum = "—"
        s.append("| %s | %d/%d | %%%.0f | %d/%d | %%%.0f | %s |"
                 % (tip, v["k1"], v["toplam"], o1, v["k3"], v["toplam"], o3, yorum))
    s.append("")
    if bazlar:
        s.append("**Kararın dayanağı dağılımı:** " +
                 " · ".join("%s %d" % (k, v) for k, v in sorted(bazlar.items())))
        s.append("")
    s.append("🔴 Resmî dinleme sızıntı tabanı yok (okumadaki `RESMI_TABAN`ın dinleme karşılığı "
             "hiç ölçülmedi), bu yüzden tabanla karşılaştırma yapılmadı.")
    s.append("")
    s.append("🔴 Bu ölçüm **bozuk soruyu** bulur, zorluk ölçmez.")
    s.append("")

    md = ortak.yol("content", "DOGRULAMA", "SESSIZ-%s.md" % paket)
    os.makedirs(os.path.dirname(md), exist_ok=True)
    with open(md, "a", encoding="utf-8") as f:
        f.write("\n".join(s) + "\n")

    ortak.yaz("content/DOGRULAMA/SESSIZ-%s.json" % paket, {
        "tarih": datetime.date.today().isoformat(),
        "paket": paket,
        "toplam_kalem": toplam,
        "toplam_numara": numara,
        "uc_turda_bilinen_k1": sorted(cozulebilir_k1),
        "uc_turda_bilinen_k3": sorted(cozulebilir_k3),
        "tip_bazinda": tipler,
        "dayanak_dagilimi": bazlar,
        "tur_basina_dogru": {sid: k1[sid] for sid in sorted(k1)},
    })

    print("Toplam %d kalem / %d numara" % (toplam, numara))
    print("K1 3/3 bilinen %d (%%%.1f) | K3 3/3 bilinen %d (%%%.1f)"
          % (u1, (u1 / toplam * 100) if toplam else 0,
             u3, (u3 / toplam * 100) if toplam else 0))
    print("Rapor: content/DOGRULAMA/SESSIZ-%s.md" % paket)
    print("\nIsaretlenecek sorular (blind_solvable=true, K3):")
    for sid in sorted(cozulebilir_k3):
        k = anahtar[sid]
        print("  %s  soru %s  (%s)" % (k["file"], k["number"], k["type"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
