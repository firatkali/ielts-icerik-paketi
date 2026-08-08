"""E8 hazirlik 2: stem_block / table / box / visual / context_line ISKELETI.

Yine deger basmaz: yalniz alan adi + tip + (dizgilerde) uzunluk. Boylece
sessiz-kopya.py bu yapilari dogru gezebilir, ama senaryo/cevap gorunmez.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

ILGI = ("stem_block", "table", "box", "visual", "context_line", "options")


def iskelet(o, derinlik=0):
    if isinstance(o, dict):
        return {k: iskelet(v, derinlik + 1) for k, v in o.items()}
    if isinstance(o, list):
        return [iskelet(o[0], derinlik + 1), "...x%d" % len(o)] if o else []
    if isinstance(o, str):
        return "str(%d)" % len(o)
    return type(o).__name__


def main():
    gorulen = {}
    for p in ortak.soru_dosyalari():
        if not p.startswith("content/listening/"):
            continue
        d = ortak.oku(p)
        tip = d.get("question_type")
        for kap in [d] + list(d.get("groups") or []):
            for alan in ILGI:
                if alan in kap:
                    anahtar = (tip, alan)
                    if anahtar not in gorulen:
                        gorulen[anahtar] = iskelet(kap[alan])
    import json
    for k in sorted(gorulen, key=str):
        print("%s / %s:" % k)
        print("   ", json.dumps(gorulen[k], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
