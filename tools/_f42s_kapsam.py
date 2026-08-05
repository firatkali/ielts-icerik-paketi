"""Gecici: pasaj basina kac soru sorulmus sayar; ayrica verilen pasajlarin
soru koklerini listeler.  Kullanim:
    python tools/_f42s_kapsam.py            -> sayim
    python tools/_f42s_kapsam.py A06 A07    -> ayrinti
"""

import collections
import glob
import json
import os
import sys

hedef = set(sys.argv[1:])
sayim = collections.Counter()

for yol in sorted(glob.glob("content/reading/**/*.json", recursive=True)):
    with open(yol, encoding="utf-8") as f:
        d = json.load(f)
    ust = d.get("passage_id")
    for g in (d.get("groups") or [d]):
        varsayilan = g.get("passage_id") or ust
        for it in g.get("items", []):
            pid = it.get("passage_id") or varsayilan
            sayim[pid] += 1
            if pid in hedef:
                print("%-46s %s %-5s | %s | %s" % (
                    os.path.relpath(yol), pid, it.get("number"),
                    str(it.get("prompt"))[:100].replace("\n", " "), it.get("answer")))

if not hedef:
    for pid, n in sorted(sayim.items(), key=lambda x: x[1]):
        print("%-6s %d" % (pid, n))
