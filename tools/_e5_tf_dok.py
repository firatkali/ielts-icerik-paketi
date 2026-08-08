# -*- coding: utf-8 -*-
"""E5 / 6. calistirma - kapsamdaki sorulari dokmek icin yardimci (salt okur)."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402


def dok(yol, nums=None, hepsi=False):
    d = ortak.oku(yol)
    print("=====", yol, "pid=", d.get("passage_id"))
    gruplar = d.get("groups") or [None]
    for g in gruplar:
        kap = g if g else d
        its = kap.get("items") or []
        if not its:
            continue
        ilgili = [i for i in its if nums is None or i["number"] in nums]
        if not ilgili and not hepsi:
            continue
        if g:
            print("  GROUP", g.get("group_id"), "pid=", g.get("passage_id"))
        ol = kap.get("option_list") or d.get("option_list")
        if ol:
            for o in ol.get("options") or []:
                print("    OPT", o.get("key"), "|", o.get("text"))
        if kap.get("stem_block"):
            print("    STEM:", kap["stem_block"][:1500])
        for it in its:
            se = nums is None or it["number"] in nums
            if not (se or hepsi):
                continue
            print("   %s #%s %s %s ans=%s" % ("***" if se else "   ", it["number"],
                                              it.get("status"), it.get("flag_mechanism"),
                                              it.get("answer")))
            for alan in ("prompt", "target_paragraph", "evidence", "evidence_locator",
                         "flag_reason", "explanation", "not_given_justification"):
                v = it.get(alan)
                if v:
                    if isinstance(v, dict):
                        v = json.dumps(v, ensure_ascii=False)
                    print("      %s: %s" % (alan.upper(), str(v)[:600]))


if __name__ == "__main__":
    yol = sys.argv[1]
    nums = [int(x) for x in sys.argv[2:]] or None
    dok(yol, nums, hepsi=True)
