# -*- coding: utf-8 -*-
"""OPUS5-E6 6. calistirma: bir soru dosyasinin ozeti (numara / kanit / cevap).

Kullanim: python tools/_e6_comp_ozet.py content/reading/tests/AC4/note-completion.json ...
"""
import io
import json
import os
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    for rel in sys.argv[1:]:
        d = json.load(open(os.path.join(KOK, rel.replace("/", os.sep)), encoding="utf-8"))
        print("\n===== %s  (%s, %s, %s)" % (rel, d.get("question_type"),
                                            d.get("word_limit"), d.get("passage_id")))
        if d.get("stem_block"):
            print("STEM:\n%s\n" % d["stem_block"])
        for g in (d["groups"] if "groups" in d else [d]):
            for it in g.get("items", []):
                loc = it.get("evidence_locator") or {}
                print("#%s [%s] %s/%s  cevap=%s  kabul=%s" % (
                    it["number"], it.get("status"), loc.get("paragraph"),
                    loc.get("sentence"), it.get("answer"),
                    it.get("accepted_variants")))
                print("   P: %s" % it.get("prompt"))


main()
