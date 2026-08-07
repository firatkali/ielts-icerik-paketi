"""Depodaki toplam flagged soru sayisi (UYARILAR.txt satiri icin)."""

import glob
import json
import os

n = 0


def walk(o):
    global n
    if isinstance(o, dict):
        if o.get("status") == "flagged":
            n += 1
        for v in o.values():
            walk(v)
    elif isinstance(o, list):
        for v in o:
            walk(v)


for p in glob.glob("content/**/*.json", recursive=True):
    if "DOGRULAMA" in p.replace(os.sep, "/"):
        continue
    try:
        with open(p, encoding="utf-8") as f:
            walk(json.load(f))
    except (json.JSONDecodeError, OSError):
        continue

print("flagged:", n)
