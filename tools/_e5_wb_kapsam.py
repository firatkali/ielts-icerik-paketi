# -*- coding: utf-8 -*-
"""E5 / 5. calistirma — kapsam sayimi.

Kapsam: kelime bankali ozet alt tipi (AC2, AC4, GT2) + `tanim_sizintisi`
mekanizmali sorular (AC3-38, AC4-36). Bu betik yalniz sayar, hicbir sey yazmaz.
"""
import glob
import json
import os

KOK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def yukle(yol):
    with open(yol, encoding="utf-8") as f:
        return json.load(f)


def main():
    bankali = []
    kelimeli = []
    tanim = []

    for yol in sorted(glob.glob(os.path.join(KOK, "content", "reading", "**", "summary-completion.json"), recursive=True)):
        d = yukle(yol)
        ad = os.path.relpath(yol, KOK).replace("\\", "/")
        hedef = bankali if d.get("word_bank") else kelimeli
        for it in d["items"]:
            hedef.append((ad, it["number"], it.get("status"), it.get("flag_mechanism")))

    for yol in sorted(glob.glob(os.path.join(KOK, "content", "**", "*.json"), recursive=True)):
        try:
            d = yukle(yol)
        except Exception:
            continue
        if not isinstance(d, dict) or "items" not in d:
            continue
        ad = os.path.relpath(yol, KOK).replace("\\", "/")
        for it in d["items"]:
            if isinstance(it, dict) and it.get("flag_mechanism") == "tanim_sizintisi":
                tanim.append((ad, it["number"], it.get("status")))

    print("== kelime bankali ozet (AC2 / AC4 / GT2)")
    isaretli = [r for r in bankali if r[2] == "flagged"]
    for r in bankali:
        print("   %-52s %2d  %-9s %s" % (r[0], r[1], r[2], r[3]))
    print("   toplam %d soru, isaretli %d" % (len(bankali), len(isaretli)))

    print("== parcadan kelime ozet (kapsam disi, 8. calistirma)")
    print("   toplam %d soru, isaretli %d"
          % (len(kelimeli), len([r for r in kelimeli if r[2] == "flagged"])))

    print("== tanim_sizintisi mekanizmasi (depo geneli)")
    for r in tanim:
        print("   %-52s %2d  %s" % r)

    kapsam = set()
    for r in isaretli:
        kapsam.add((r[0], r[1]))
    for r in tanim:
        if r[2] == "flagged":
            kapsam.add((r[0], r[1]))
    print("== 5. calistirmanin kapsami: %d soru" % len(kapsam))
    for k in sorted(kapsam):
        print("   %-52s %2d" % k)


if __name__ == "__main__":
    main()
