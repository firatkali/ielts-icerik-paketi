"""E8 hazirlik 3: dinleme soru sayimi (rule 1 - "sayiya guvenme, yeniden say").

Deger basmaz; yalniz sayilar. Aralikli numaralar (ornek "34-35") acilir.
"""

import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402


def main():
    tip_kalem = collections.Counter()
    tip_numara = collections.Counter()
    yer_numara = collections.Counter()
    for p in ortak.soru_dosyalari():
        if not p.startswith("content/listening/"):
            continue
        d = ortak.oku(p)
        tip = d.get("question_type")
        for it in ortak.sorular(d):
            tip_kalem[tip] += 1
            n = len(ortak.numaralar(it)) or 1
            tip_numara[tip] += n
            yer_numara["alistirma" if d.get("practice") else "tam test"] += n

    print("%-32s %6s %6s" % ("tip", "kalem", "numara"))
    for tip in sorted(tip_kalem):
        print("%-32s %6d %6d" % (tip, tip_kalem[tip], tip_numara[tip]))
    print("%-32s %6d %6d" % ("TOPLAM", sum(tip_kalem.values()), sum(tip_numara.values())))
    print()
    for k, v in sorted(yer_numara.items()):
        print("  %s: %d numara" % (k, v))
    return 0


if __name__ == "__main__":
    sys.exit(main())
