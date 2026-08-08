# -*- coding: utf-8 -*-
"""OPUS5-E6 6. calistirma: bir pasajin hangi cumleleri hangi soruda kullanilmis.

Kullanim: python tools/_e6_comp_capraz.py A01 [A02 ...]
Cikti: pasajin her paragraf/cumlesi + o cumleye capalanmis sorular.
"""
import io
import json
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def pasaj(pid):
    for kok in ("academic", "general"):
        p = os.path.join(KOK, "passages", kok, pid + ".json")
        if os.path.exists(p):
            return json.load(open(p, encoding="utf-8"))
    raise SystemExit("pasaj yok: " + pid)


def cumleler(metin):
    return re.split(r"(?<=[.!?])\s+", metin.strip())


def soru_dosyalari():
    for kok, _, adlar in os.walk(os.path.join(KOK, "content", "reading")):
        if "DOGRULAMA" in kok:
            continue
        for a in adlar:
            if a.endswith(".json"):
                yield os.path.join(kok, a)


def yuvalar(d):
    for g in (d["groups"] if "groups" in d else [d]):
        for it in g.get("items", []):
            yield g, it


def main():
    hedefler = sys.argv[1:]
    kullanim = {}  # (pasaj, paragraf, cumle) -> [etiket]
    for yol in soru_dosyalari():
        try:
            d = json.load(open(yol, encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(d, dict) or d.get("skill") != "reading":
            continue
        rel = os.path.relpath(yol, KOK).replace(os.sep, "/")
        for g, it in yuvalar(d):
            pid = g.get("passage_id") or d.get("passage_id") or it.get("passage_id")
            loc = it.get("evidence_locator") or {}
            if not pid or not loc:
                continue
            k = (pid, loc.get("paragraph"), loc.get("sentence"))
            kullanim.setdefault(k, []).append(
                "%s#%s(%s)" % (rel.split("/")[-2] + "/" + rel.split("/")[-1],
                               it["number"], d.get("question_type", "?")))

    for pid in hedefler:
        d = pasaj(pid)
        print("\n===== %s  %s" % (pid, d.get("title")))
        for p in (d["paragraphs"] or []):
            for i, c in enumerate(cumleler(p["text"]), 1):
                etik = kullanim.get((pid, p["label"], i), [])
                print("%s/%d %s| %s" % (p["label"], i, ("<<" + ",".join(etik) + ">> ") if etik else "", c))
        for t in d.get("texts", []) or []:
            print("-- metin %s: %s" % (t.get("label"), t.get("title")))
            for p in t["paragraphs"]:
                for i, c in enumerate(cumleler(p["text"]), 1):
                    etik = kullanim.get((pid, p["label"], i), [])
                    print("%s/%d %s| %s" % (p["label"], i, ("<<" + ",".join(etik) + ">> ") if etik else "", c))


main()
