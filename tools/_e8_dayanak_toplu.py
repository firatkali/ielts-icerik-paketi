# -*- coding: utf-8 -*-
"""E8 5. adim yardimcisi: dort turun dayanak dagilimini tek tabloda toplar.

Kullanim: python tools/_e8_dayanak_toplu.py

Her kalemin baskin dayanagi (uc turun cogunlugu) x 3/3 bilinip bilinmedigi.
Cevap anahtarina ve senaryoya bakmaz.
"""

import collections
import importlib
import io
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
import ortak  # noqa: E402

toplu = importlib.import_module("_e8_toplu")


def main():
    bilinen, dayanak = set(), {}
    disi = set()
    for p in toplu.paketler():
        d = ortak.oku("content/DOGRULAMA/SESSIZ-%s.json" % p)
        bilinen |= set(d["uc_turda_bilinen_k3"])
        disi |= set(d.get("olcum_disi") or [])
        dayanak.update(toplu.baskin_dayanak(p))

    c = collections.defaultdict(collections.Counter)
    for kid, b in dayanak.items():
        if kid in disi:
            continue
        c[b]["3/3" if kid in bilinen else "yok"] += 1

    print("%-20s %6s %8s %10s" % ("dayanak", "kalem", "3/3", "sinif"))
    t = collections.Counter()
    for b in sorted(c, key=lambda x: -sum(c[x].values())):
        sinif = "sansa acik" if b in toplu.SANSA_ACIK else "anlamsal"
        n = sum(c[b].values())
        print("%-20s %6d %8d %10s" % (b, n, c[b]["3/3"], sinif))
        t[sinif + "-kalem"] += n
        t[sinif + "-3/3"] += c[b]["3/3"]
    print("\nanlamsal   : %d kalem, %d tanesi 3/3"
          % (t["anlamsal-kalem"], t["anlamsal-3/3"]))
    print("sansa acik : %d kalem, %d tanesi 3/3"
          % (t["sansa acik-kalem"], t["sansa acik-3/3"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
