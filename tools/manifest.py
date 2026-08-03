"""content/MANIFEST.json uretir - uygulamanin icerigi yuklemek icin okuyacagi tek dosya.

Kullanim:  python tools/manifest.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

import collections
import datetime

HEDEF = {"reading": 400, "listening": 360, "speaking": 440, "writing": 110}


def main():
    kayit = []

    for p in ortak.bul("content/listening/scripts/*.json"):
        d = ortak.oku(p)
        kayit.append({
            "path": p, "kind": "listening_script",
            "script_id": d.get("script_id"), "test_id": d.get("test_id"),
            "section": d.get("section"), "word_count": d.get("word_count"),
            "answer_points": len(d.get("answer_points") or []),
        })

    for p in ortak.soru_dosyalari():
        d = ortak.oku(p)
        its = ortak.sorular(d)
        kayit.append({
            "path": p, "kind": "question_set", "set_id": d.get("set_id"),
            "skill": d.get("skill"), "module": d.get("module"),
            "test_id": d.get("test_id"), "practice": bool(d.get("practice")),
            "section": d.get("section"),
            "question_type": d.get("question_type"),
            "generated_by": d.get("generated_by"),
            "passage_id": d.get("passage_id"), "script_id": d.get("script_id"),
            "count": sum(2 if i.get("select_count") == 2 else 1 for i in its),
            "flagged": sum(1 for i in its if i.get("status") == "flagged"),
        })

    for p in ortak.bul("passages/**/*.json"):
        if p.endswith("INDEX.json"):
            continue
        d = ortak.oku(p)
        kayit.append({
            "path": p, "kind": "passage", "passage_id": d.get("passage_id"),
            "module": d.get("module"), "section": d.get("section"),
            "word_count": d.get("word_count"),
            "license": (d.get("source") or {}).get("license"),
            "source_url": (d.get("source") or {}).get("url"),
        })

    toplam = collections.Counter()
    for k in kayit:
        if k["kind"] == "question_set":
            toplam[k["skill"] or "?"] += k["count"]

    man = {
        "generated_at": datetime.date.today().isoformat(),
        "schema_version": "1.0",
        "targets": HEDEF,
        "totals": dict(toplam),
        "total_questions": sum(toplam.values()),
        "total_flagged": sum(k.get("flagged", 0) for k in kayit
                             if k["kind"] == "question_set"),
        "entries": kayit,
    }
    ortak.yaz("content/MANIFEST.json", man)

    print("MANIFEST.json yazildi.\n")
    print("%-12s %8s %8s %8s" % ("beceri", "hedef", "uretilen", "fark"))
    for b in ["reading", "listening", "speaking", "writing"]:
        u = toplam.get(b, 0)
        print("%-12s %8d %8d %8d" % (b, HEDEF[b], u, u - HEDEF[b]))
    th = sum(HEDEF.values())
    tu = sum(toplam.values())
    print("%-12s %8d %8d %8d" % ("TOPLAM", th, tu, tu - th))
    print("\nIsaretli (flagged) soru: %d" % man["total_flagged"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
