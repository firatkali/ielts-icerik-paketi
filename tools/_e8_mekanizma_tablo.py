# -*- coding: utf-8 -*-
"""E8 5. adim yardimcisi: mekanizma x soru tipi tablosunu markdown olarak basar.

Kullanim: python tools/_e8_mekanizma_tablo.py

Isaretli kalemleri orijinal dosyalardan degil `_e8_isaret_tablosu.TABLO`dan alir;
soru tipini dosyanin `question_type` alanindan okur. Cevap anahtarina bakmaz.
"""

import collections
import glob
import importlib
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
import ortak  # noqa: E402

tablo = importlib.import_module("_e8_isaret_tablosu")


def tipler():
    out = {}
    for f in glob.glob(ortak.yol("content", "listening", "**", "*.json"),
                       recursive=True):
        if "scripts" in f.replace(os.sep, "/").split("/"):
            continue
        with open(f, encoding="utf-8") as fh:
            try:
                d = json.load(fh)
            except ValueError:
                continue
        if d.get("skill") != "listening":
            continue
        for kap in (d.get("groups") or [d]):
            for it in (kap.get("items") or []):
                out["%s-%s" % (d.get("set_id"), it.get("number"))] = \
                    d.get("question_type")
    return out


def main():
    tip = tipler()
    c = collections.defaultdict(collections.Counter)
    for kid, (mek, _) in tablo.TABLO.items():
        c[tip.get(kid, "?")][mek] += 1
    mekler = sorted({m for v in c.values() for m in v})
    print("| Soru tipi | " + " | ".join(mekler) + " | Toplam |")
    print("|" + "---|" * (len(mekler) + 2))
    toplam = collections.Counter()
    for qt in sorted(c):
        satir = " | ".join(str(c[qt][m]) for m in mekler)
        print("| `%s` | %s | **%d** |" % (qt, satir, sum(c[qt].values())))
        toplam.update(c[qt])
    print("| **Toplam** | "
          + " | ".join("**%d**" % toplam[m] for m in mekler)
          + " | **%d** |" % sum(toplam.values()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
