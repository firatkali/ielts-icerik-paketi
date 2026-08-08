# -*- coding: utf-8 -*-
"""OPUS5-E6: yeniden uretilen yuvalari E5 listesinde isaretler.

Sonraki calistirmalar (2/7 ... 7/7) hangi grubun bitmis oldugunu buradan gorur.
Kullanim: python tools/_e6_liste_isaretle.py <calistirma-etiketi> <dosya:numara> ...
Argumansiz calistirilirsa 1. calistirmanin uc yuvasi isaretlenir.
"""
import io
import json
import os
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YOL = os.path.join(KOK, "content", "DOGRULAMA", "yeniden-uretim-listesi.json")

ETIKET = "OPUS5-E6 1/7 - YES/NO/NOT GIVEN tam testler"
HEDEF = [("content/reading/tests/GT1/yes-no-not-given.json", 33),
         ("content/reading/tests/GT1/yes-no-not-given.json", 34),
         ("content/reading/tests/GT2/yes-no-not-given.json", 34)]


def main():
    d = json.load(open(YOL, encoding="utf-8"))
    ifadeler = {}
    for rel in sorted(set(r for r, _ in HEDEF)):
        q = json.load(open(os.path.join(KOK, rel.replace("/", os.sep)), encoding="utf-8"))
        for it in q["items"]:
            ifadeler[(rel, it["number"])] = it["prompt"]

    n = 0
    for x in d["elenen"]:
        anahtar = (x["dosya"], x["numara"])
        if anahtar not in HEDEF:
            continue
        x["yeniden_uretildi"] = {
            "tarih": "2026-08-08",
            "calistirma": ETIKET,
            "model": "opus",
            "yeni_ifade": ifadeler[anahtar],
        }
        n += 1
    print("isaretlenen yuva:", n)
    print("kalan yuva:", sum(1 for x in d["elenen"] if "yeniden_uretildi" not in x))
    with open(YOL, "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")


if __name__ == "__main__":
    main()
