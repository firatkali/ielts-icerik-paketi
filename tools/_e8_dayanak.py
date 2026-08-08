"""E8: 3/3 bilinen sorularin dayanak (basis) dagilimi + tutmayanlar.

Rapora yazacak sayilari uretir. Cevap degeri basmaz, yalniz kimlik + dayanak.
"""

import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402


def main():
    paket = sys.argv[1]
    ozet = ortak.oku("content/DOGRULAMA/SESSIZ-%s.json" % paket)
    bilinen = set(ozet["uc_turda_bilinen_k3"])
    kac = ozet["tur_basina_dogru"]

    dayanak = {}
    with open(ortak.yol("kalibrasyon", "sessiz", "%s-tur1.json" % paket), encoding="utf-8") as f:
        for a in json.load(f)["answers"]:
            dayanak[a["id"]] = a.get("basis")

    bilinen_d = collections.Counter()
    kalan_d = collections.Counter()
    for sid, n in sorted(kac.items()):
        (bilinen_d if sid in bilinen else kalan_d)[dayanak.get(sid)] += 1

    print("3/3 BILINEN (%d) dayanak:" % len(bilinen))
    for k, v in bilinen_d.most_common():
        print("  %-20s %d" % (k, v))
    print("\nBILINMEYEN (%d) dayanak:" % (len(kac) - len(bilinen)))
    for k, v in kalan_d.most_common():
        print("  %-20s %d" % (k, v))
    print("\nSoru bazinda kac turda dogru:")
    for sid, n in sorted(kac.items()):
        print("  %-32s %d/3  %s" % (sid, n, dayanak.get(sid)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
