# -*- coding: utf-8 -*-
"""OPUS5-E6 6. calistirma: yeni cerceve metinlerinin kip dokumu (tek tek)."""
import io
import json
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MUT = ["only", "every", "all", "no", "never", "always", "must", "cannot",
       "each", "entirely", "whole"]
OLC = ["about", "roughly", "may", "might", "some", "appears", "seemed",
       "suggests", "likely", "rather than", "almost", "partly", "around"]


def main():
    e5 = json.load(open(os.path.join(KOK, "content", "DOGRULAMA",
                                     "yeniden-uretim-listesi.json"), encoding="utf-8"))["elenen"]
    keys = set((x["dosya"], x["numara"]) for x in e5)
    for rel in sorted(set(k[0] for k in keys)):
        d = json.load(open(os.path.join(KOK, rel.replace("/", os.sep)), encoding="utf-8"))
        for g in (d["groups"] if "groups" in d else [d]):
            for it in g.get("items", []):
                if (rel, it["number"]) not in keys:
                    continue
                yu = it.get("yeniden_uretim")
                if not yu or yu.get("uretilen_grup") != "Tamamlama ailesi yuvalari":
                    continue
                p = it["prompt"].lower()
                m = [k for k in MUT if re.search(r"\b" + k + r"\b", p)]
                o = [k for k in OLC if re.search(r"\b" + k + r"\b", p)]
                print("%s%s %-28s %s | M=%s O=%s" % (
                    "M" if m else "-", "O" if o else "-",
                    rel.split("/")[-2] + "#" + str(it["number"]),
                    it["prompt"][:80], ",".join(m), ",".join(o)))


main()
