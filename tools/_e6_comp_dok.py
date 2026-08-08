# -*- coding: utf-8 -*-
"""OPUS5-E6 6. calistirma: tamamlama ailesinin elenen yuvalarini dokur.

Kullanim: python tools/_e6_comp_dok.py [pasaj_id ...]
"""
import io
import json
import os
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LISTE = os.path.join(KOK, "content", "DOGRULAMA", "yeniden-uretim-listesi.json")

TAM = {"flow_chart_completion", "note_completion", "sentence_completion",
       "summary_completion", "table_completion"}


def main():
    sec = set(sys.argv[1:])
    d = json.load(open(LISTE, encoding="utf-8"))
    todo = [x for x in d["elenen"]
            if "yeniden_uretildi" not in x and x["tip"] in TAM
            and (not sec or x["pasaj"] in sec)]
    for x in sorted(todo, key=lambda y: (y["pasaj"], y["dosya"], str(y["numara"]))):
        print("### %s %s #%s (%s)" % (x["pasaj"], x["dosya"], x["numara"], x["tip"]))
        for k, v in x["kacinilacak"].items():
            print("  KACIN[%s]: %s" % (k, v))
        print("  NEDEN: %s" % x["neden_elendi"])
        print()
    print("toplam %d" % len(todo))


main()
