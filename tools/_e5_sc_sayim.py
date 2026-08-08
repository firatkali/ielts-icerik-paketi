# -*- coding: utf-8 -*-
"""E5 / 7. calistirma - olcum.

1. bolum: her sorunun parcasiz cevabi, dogru cevabin AYIRT EDICI ogesini
   tasiyor mu? (kapsamin siniflandirmasi ve sonucla capraz tablosu)
2. bolum: soru metni, cevabin AYIRT EDICI ogesini tanimlayan bir ibare
   tasiyor mu? (HEAD ile karsilastirmali). Bu, sizintinin CERCEVEDE mi yoksa
   CEVABIN KENDISINDE mi durdugunu ayiran olcu: cerceveden geliyorsa ibare
   kaldirilabilir, cevaptan geliyorsa soru metninde boyle bir ibare zaten
   yoktur ve yine de model dogru kavrami verir.
"""
import collections
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

SC = "content/reading/practice/sentence-completion.json"
SA = "content/reading/practice/short-answer.json"
AC1 = "content/reading/tests/AC1/sentence-completion.json"
AC2 = "content/reading/tests/AC2/sentence-completion.json"
AC3 = "content/reading/tests/AC3/sentence-completion.json"
AC4 = "content/reading/tests/AC4/sentence-completion.json"
GT1 = "content/reading/tests/GT1/sentence-completion.json"
GT2 = "content/reading/tests/GT2/sentence-completion.json"

# (dosya, numara): (cevap, modelin parcasiz cevabi,
#                   ayirt edici oge modelde var mi, bas ad zorunlu mu)
KAPSAM = {
    (SC, 2):  ("sensory contact",           "contact",            False, True),
    (SC, 3):  ("anatomy",                   "anatomy/morphology", True,  True),
    (SC, 4):  ("running seawater",          "seawater",           False, True),
    (SC, 6):  ("unique individual",         "individual",         False, True),
    (SC, 7):  ("laboratory tank",           "laboratory",         False, True),
    (SC, 12): ("ongoing research",          "preliminary",        True,  True),
    (SA, 6):  ("transactive memory system", "transactive memory", True,  True),
    (AC1, 19): ("transparent divider",      "transparent barrier", True, False),
    (AC1, 20): ("dominance hierarchy",      "hierarchy",          False, False),
    (AC2, 20): ("separate laboratories",    "laboratories",       False, True),
    (AC3, 22): ("mountaineers",             "climbers",           True,  True),
    (AC4, 22): ("vegetation",               "vegetation/foliage", True,  True),
    (GT1, 27): ("final salary",             "final pay",          True,  True),
    (GT2, 25): ("probationary period",      "probation period",   True,  True),
    (GT2, 26): ("home-office equipment",    "office equipment",   False, True),
}

# Her cevabin AYIRT EDICI ogesini soru metninde ele verebilecek sozcukler.
# (bas adi degil, yalniz ayirt edici ogeyi: 'transparent', 'dominance',
#  'sensory', 'running', 'unique', 'tank', 'home', 'separate', ...)
TANIM_ALANI = {
    (SC, 2):  ["sensory", "sense", "feel", "feeling", "touch", "touching"],
    (SC, 3):  ["anatomy", "anatomical", "body", "bodily", "morphology",
               "physique", "build"],
    (SC, 4):  ["running", "flowing", "flow", "flowed", "circulating",
               "circulated", "pumped"],
    (SC, 6):  ["unique", "particular", "specific", "individually", "name",
               "named"],
    (SC, 7):  ["tank", "aquarium", "vessel", "enclosure"],
    (SC, 12): ["ongoing", "continuing", "unfinished", "preliminary",
               "provisional", "incomplete"],
    (SA, 6):  ["transactive", "shared", "implicit", "who", "knows"],
    (AC1, 19): ["transparent", "clear", "watch", "watched", "see", "seen",
                "seeing", "sight", "visual", "visible", "look", "looking"],
    (AC1, 20): ["dominance", "dominant", "win", "won", "winning", "wins",
                "stronger", "strongest", "beat", "retreated", "subordinate"],
    (AC2, 20): ["separate", "separately", "apart", "different", "split",
                "divided", "two"],
    (AC3, 22): ["mountaineers", "mountaineering", "climbers", "climbing",
                "climb", "mountains", "peaks"],
    (AC4, 22): ["vegetation", "greenery", "foliage", "plants", "leaves",
                "leafy", "green"],
    (GT1, 27): ["final", "last", "leaving", "leaves", "leave", "resign",
                "resigns", "resigning", "departure"],
    (GT2, 25): ["probationary", "probation", "trial", "initial", "first",
                "completed", "complete"],
    (GT2, 26): ["home", "domestic", "household", "remote", "remotely"],
}


def alan_isabet(metin, alan):
    kel = set(re.findall(r"[a-z]+", (metin or "").lower()))
    return sorted(w for w in alan if w in kel)


def head_surumu(yol):
    ham = subprocess.run(["git", "show", "HEAD:%s" % yol],
                         cwd=ortak.KOK, stdout=subprocess.PIPE, check=True)
    return json.loads(ham.stdout.decode("utf-8"))


def main():
    durum = {}
    for yol in sorted({k[0] for k in KAPSAM}):
        for it in ortak.sorular(ortak.oku(yol)):
            if (yol, it["number"]) in KAPSAM:
                durum[(yol, it["number"])] = it

    print("== 1. bolum: ayirt edici oge modelin parcasiz cevabinda var mi ==")
    print("%-52s %-3s %-26s %-22s %-6s %-8s %s"
          % ("dosya", "no", "cevap", "modelin cevabi", "ayirt", "bas ad",
             "sonuc"))
    capraz = collections.Counter()
    for (yol, num), (cev, blind, ayirt, zorunlu) in sorted(KAPSAM.items()):
        it = durum[(yol, num)]
        sonuc = {"verified": "duzeltildi", "rejected": "elendi"}.get(
            it.get("status"), "dokunulmadi")
        print("%-52s %-3s %-26s %-22s %-6s %-8s %s"
              % (yol.split("/")[-2] + "/" + yol.split("/")[-1], num, cev,
                 blind, "VAR" if ayirt else "yok",
                 "zorunlu" if zorunlu else "acik", sonuc))
        capraz[(ayirt, zorunlu, sonuc)] += 1

    print()
    print("== capraz tablo ==")
    for (ayirt, zorunlu, sonuc), n in sorted(capraz.items()):
        print("  ayirt edici oge %-4s | bas ad %-8s -> %-12s %d"
              % ("VAR" if ayirt else "yok",
                 "zorunlu" if zorunlu else "acik", sonuc, n))
    print()
    print("  ayirt edici oge modelde VAR: %d / %d"
          % (sum(1 for v in KAPSAM.values() if v[2]), len(KAPSAM)))
    print("  bas ad cumlenin anlamsal rolunden zorunlu: %d / %d"
          % (sum(1 for v in KAPSAM.values() if v[3]), len(KAPSAM)))

    print()
    print("== 2. bolum: soru metni ayirt edici ogeyi tanimliyor mu ==")
    onceki = sonraki = 0
    for yol in sorted({k[0] for k in KAPSAM}):
        eski = {it["number"]: it for it in ortak.sorular(head_surumu(yol))}
        for it in ortak.sorular(ortak.oku(yol)):
            n = it["number"]
            if (yol, n) not in KAPSAM:
                continue
            alan = TANIM_ALANI[(yol, n)]
            e = alan_isabet(eski[n].get("prompt"), alan)
            y = alan_isabet(it.get("prompt"), alan)
            onceki += bool(e)
            sonraki += bool(y)
            if e or y:
                print("  %-46s #%-3s once=%s  sonra=%s"
                      % (yol.split("/")[-2] + "/" + yol.split("/")[-1], n,
                         e or "-", y or "-"))
    print("  tanim sizdiran soru metni: %d -> %d (15 sorudan)"
          % (onceki, sonraki))


if __name__ == "__main__":
    main()
