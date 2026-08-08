"""E8 hazirlik: dinleme soru dosyalarinin ALAN ADLARINI listeler.

Deger basmaz - bu oturumda senaryo/cevap gorunmemeli (E8 "en onemli kural").
Amac: sessiz-kopya.py'nin hangi alanlari silecegini alan adlarindan cikarmak.
"""

import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402


def main():
    ust = collections.Counter()
    grup = collections.Counter()
    soru = collections.Counter()
    tipler = collections.Counter()
    dosya = 0
    for p in ortak.soru_dosyalari():
        if not p.startswith("content/listening/"):
            continue
        d = ortak.oku(p)
        dosya += 1
        ust.update(d.keys())
        tipler[(d.get("skill"), d.get("question_type"), os.path.basename(p))] += 1
        for g in (d.get("groups") or []):
            grup.update(g.keys())
        for it in ortak.sorular(d):
            if isinstance(it, dict):
                soru.update(it.keys())

    print("dinleme soru dosyasi:", dosya)
    for ad, sayac in (("UST", ust), ("GRUP", grup), ("SORU", soru)):
        print("\n%s ALANLARI:" % ad)
        for k, v in sayac.most_common():
            print("  %-28s %d" % (k, v))
    print("\nSKILL / TIP / DOSYA:")
    for k, v in sorted(tipler.items(), key=lambda x: str(x[0])):
        print("  %s" % (k,), v)
    return 0


if __name__ == "__main__":
    sys.exit(main())
