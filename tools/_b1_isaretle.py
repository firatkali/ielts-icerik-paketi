"""B1 4. adim: parcasiz olcumun sonucunu orijinal soru dosyalarina isler.

Kullanim: python tools/_b1_isaretle.py <paket-adi>

3/3 turda parcasiz bilinen soruya blind_solvable=true + status=flagged,
digerlerine blind_solvable=false yazar. HICBIR SORU SILINMEZ.
Diyagram etiketleme tipi atlanir (gorsel gerektirir, metin olcumu orada kor).
"""

import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

ATLA_TIP = {"diagram_labelling", "plan_map_diagram_labelling"}
SEBEP = ("Parça gösterilmeden 3/3 turda doğru bilindi; "
         "genel kültürle çözülebiliyor.")


def main():
    if len(sys.argv) < 2:
        print("Kullanim: python tools/_b1_isaretle.py <paket-adi>")
        return 2
    paket = sys.argv[1]

    rapor = ortak.oku("content/DOGRULAMA/METINSIZ-%s.json" % paket)
    bilinen = set(rapor["uc_turda_bilinen"])

    # Her sorunun baskin dayanagi (uc turun cogunlugu).
    dayanak = collections.defaultdict(collections.Counter)
    for n in (1, 2, 3):
        with open(ortak.yol("kalibrasyon", "metinsiz",
                            "%s-tur%d.json" % (paket, n)), encoding="utf-8") as f:
            for a in json.load(f)["answers"]:
                if a.get("basis"):
                    dayanak[a["id"]][a["basis"]] += 1

    yollar = [p for p in ortak.bul("content/**/%s.json" % paket)
              if "/DOGRULAMA/" not in p]
    isaretli = duz = atlanan = 0
    for p in yollar:
        d = ortak.oku(p)
        if d.get("skill") != "reading":
            continue
        if d.get("question_type") in ATLA_TIP:
            print("  atlandi (gorsel gerektirir): %s" % p)
            atlanan += 1
            continue
        set_id = d.get("set_id", os.path.basename(p))
        for it in ortak.sorular(d):
            sid = "%s-%s" % (set_id, it.get("number"))
            if sid in bilinen:
                it["blind_solvable"] = True
                it["blind_basis"] = dayanak[sid].most_common(1)[0][0]
                it["status"] = "flagged"
                it["flag_reason"] = SEBEP
                isaretli += 1
            else:
                it["blind_solvable"] = False
                duz += 1
        ortak.yaz(p, d)
        print("  islendi: %s" % p)

    print("\n%d soru isaretlendi (flagged), %d soru blind_solvable=false, "
          "%d dosya atlandi." % (isaretli, duz, atlanan))
    return 0


if __name__ == "__main__":
    sys.exit(main())
