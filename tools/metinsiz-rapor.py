"""B1 3. adim: parcasiz verilen cevaplari anahtarla karsilastirir.

Kullanim:  python tools/metinsiz-rapor.py <paket-adi>

Okur:  kalibrasyon/metinsiz/<paket>-tur1.json, -tur2.json, -tur3.json
Yazar: content/DOGRULAMA/METINSIZ-<paket>.md  (+ .json ham veri)

Bir soru UC TURUN UCUNDE de dogru bilinmisse "parcasiz cozulebilir" sayilir.
Tek turda tutturmak sanstir; uc turda tutturmak degildir.

Cikan oran TEK BASINA yorumlanmaz: resmi sorularin da %57'si parcasiz
bilinebiliyordu. Karsilastirma her zaman SORU TIPI bazinda ve asagidaki
resmi taban ile yapilir.
"""

import datetime
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

# Resmi ornek sorularda olculen parcasiz bilinme (dogru/toplam).
# Kucuk orneklem - kesin esik degil, yon verir.
RESMI_TABAN = {
    "note_completion": (6, 6),
    "summary_completion": (4, 4),          # listeden secmeli
    "matching_headings": (4, 4),
    "true_false_not_given": (3, 3),
    "matching_sentence_endings": (3, 3),
    "matching_features": (3, 4),
    "sentence_completion": (1, 5),
    "table_completion": (0, 5),
    "diagram_labelling": (0, 5),
}


def normal(a):
    if a is None:
        return []
    if not isinstance(a, list):
        a = [a]
    return sorted(str(x).strip().lower() for x in a)


def anahtar_yukle():
    """Tum okuma sorularini id -> (cevap, tip, dosya) olarak toplar."""
    tablo = {}
    for p in ortak.soru_dosyalari():
        d = ortak.oku(p)
        if d.get("skill") != "reading":
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
    if len(sys.argv) < 2:
        print("Kullanim: python tools/metinsiz-rapor.py <paket-adi>")
        return 2
    paket = sys.argv[1]

    turlar = []
    for n in (1, 2, 3):
        p = ortak.yol("kalibrasyon", "metinsiz", "%s-tur%d.json" % (paket, n))
        if not os.path.exists(p):
            print("HATA: eksik tur dosyasi: kalibrasyon/metinsiz/%s-tur%d.json" % (paket, n))
            print("Uc turun ucu de yazilmadan rapor uretilmez.")
            return 1
        with open(p, encoding="utf-8") as f:
            turlar.append(json.load(f))

    anahtar = anahtar_yukle()

    # id -> kac turda dogru
    sayac, bazlar, bilinmeyen = {}, {}, []
    for t in turlar:
        for a in t.get("answers", []):
            sid = a.get("id")
            kayit = anahtar.get(sid)
            if kayit is None:
                bilinmeyen.append(sid)
                continue
            if dogru_mu(a.get("answer"), kayit):
                sayac[sid] = sayac.get(sid, 0) + 1
            else:
                sayac.setdefault(sid, 0)
            if a.get("basis"):
                bazlar[a["basis"]] = bazlar.get(a["basis"], 0) + 1

    # tip bazinda topla
    tipler = {}
    cozulebilir = []
    for sid, kac in sayac.items():
        tip = anahtar[sid]["type"] or "bilinmiyor"
        d = tipler.setdefault(tip, {"toplam": 0, "uc_turda": 0})
        d["toplam"] += 1
        if kac >= 3:
            d["uc_turda"] += 1
            cozulebilir.append(sid)

    toplam = sum(v["toplam"] for v in tipler.values())
    uc = sum(v["uc_turda"] for v in tipler.values())

    satir = []
    satir.append("## %s — %s" % (paket, datetime.date.today().isoformat()))
    satir.append("")
    satir.append("- Ölçülen soru: **%d**" % toplam)
    satir.append("- Üç turun üçünde de parçasız bilinen: **%d** (%%%.1f)"
                 % (uc, (uc / toplam * 100) if toplam else 0))
    if bilinmeyen:
        satir.append("- ⚠️ Anahtarda bulunamayan cevap kimliği: %d" % len(bilinmeyen))
    satir.append("")
    satir.append("| Soru tipi | Bizde | Oran | Resmî taban |")
    satir.append("|---|---|---|---|")
    for tip in sorted(tipler):
        v = tipler[tip]
        oran = v["uc_turda"] / v["toplam"] * 100 if v["toplam"] else 0
        rt = RESMI_TABAN.get(tip)
        rts = "%d/%d (%%%.0f)" % (rt[0], rt[1], rt[0] / rt[1] * 100) if rt else "ölçülmedi"
        isaret = ""
        if rt and rt[1]:
            if oran - (rt[0] / rt[1] * 100) > 25:
                isaret = " 🔴"
        satir.append("| %s | %d/%d | %%%.0f%s | %s |"
                     % (tip, v["uc_turda"], v["toplam"], oran, isaret, rts))
    satir.append("")
    if bazlar:
        satir.append("**Kararın dayanağı dağılımı:** " +
                     " · ".join("%s %d" % (k, v) for k, v in sorted(bazlar.items())))
        satir.append("")
    satir.append("🔴 Bu ölçüm **bozuk soruyu** bulur, zorluk seviyesini ölçmez.")
    satir.append("")

    md = ortak.yol("content", "DOGRULAMA", "METINSIZ-%s.md" % paket)
    os.makedirs(os.path.dirname(md), exist_ok=True)
    with open(md, "a", encoding="utf-8") as f:
        f.write("\n".join(satir) + "\n")

    ortak.yaz("content/DOGRULAMA/METINSIZ-%s.json" % paket, {
        "tarih": datetime.date.today().isoformat(),
        "paket": paket,
        "toplam": toplam,
        "uc_turda_bilinen": cozulebilir,
        "tip_bazinda": tipler,
        "dayanak_dagilimi": bazlar,
    })

    print("Toplam %d soru | 3/3 bilinen %d (%%%.1f)"
          % (toplam, uc, (uc / toplam * 100) if toplam else 0))
    print("Rapor: content/DOGRULAMA/METINSIZ-%s.md" % paket)
    print("\nIsaretlenecek sorular (blind_solvable=true):")
    for sid in cozulebilir:
        k = anahtar[sid]
        print("  %s  soru %s  (%s)" % (k["file"], k["number"], k["type"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
