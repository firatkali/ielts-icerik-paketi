# -*- coding: utf-8 -*-
"""E5 8. calistirma - kapsamdaki sorulari okunur bicimde dokumler."""
import json, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def sorular(d):
    if isinstance(d, dict):
        if "status" in d and "number" in d:
            yield d
        for v in d.values():
            yield from sorular(v)
    elif isinstance(d, list):
        for v in d:
            yield from sorular(v)


ALAN = ("passage_id", "prompt", "answer", "accepted_variants", "evidence",
        "evidence_locator", "explanation", "difficulty", "flag_reason",
        "flag_mechanism", "blind_basis")


def main():
    f = sys.argv[1]
    nums = set(int(x) for x in sys.argv[2:]) if len(sys.argv) > 2 else None
    d = json.load(open(f, encoding="utf-8"))
    print("#" * 90)
    print(f, "| word_limit:", d.get("word_limit"), "| passage:", d.get("passage_id"))
    if d.get("stem_block"):
        print("--- stem_block ---")
        print(d["stem_block"])
    if d.get("word_bank"):
        print("--- word_bank ---")
        print(json.dumps(d["word_bank"], ensure_ascii=False, indent=1))
    for q in sorular(d):
        if nums and q.get("number") not in nums:
            continue
        print("--- SORU %s [%s] ---" % (q.get("number"), q.get("status")))
        for k in ALAN:
            if k in q:
                print("  %-18s %s" % (k, json.dumps(q[k], ensure_ascii=False)))


if __name__ == "__main__":
    main()
