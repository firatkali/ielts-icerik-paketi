# -*- coding: utf-8 -*-
"""E5 8. calistirma - kapsam sayimi.

Kapsam iki kumenin birlesimi:
  (a) E10'un ozet ailesinde (summary_completion) isaretledigi sorular
  (b) depo genelinde ayakta kalan flag_mechanism == "genel_kultur" sorulari
"""
import json, glob, collections


def sorular(d):
    if isinstance(d, dict):
        if "status" in d and "number" in d:
            yield d
        for v in d.values():
            yield from sorular(v)
    elif isinstance(d, list):
        for v in d:
            yield from sorular(v)


def tara():
    kayit = []
    for p in sorted(glob.glob("content/**/*.json", recursive=True)):
        pn = p.replace("\\", "/")
        if "/DOGRULAMA/" in pn:
            continue
        try:
            d = json.load(open(p, encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        qt = d.get("question_type")
        sk = d.get("skill")
        for q in sorular(d):
            kayit.append({
                "dosya": pn, "tip": qt, "skill": sk, "numara": q.get("number"),
                "durum": q.get("status"), "mek": q.get("flag_mechanism"),
                "e10": q.get("blind_solvable_kelime_duzeyi") is not None,
                "cevap": q.get("answer"), "banka": bool(d.get("word_bank")),
            })
    return kayit


def main():
    kayit = tara()
    isaretli = [k for k in kayit if k["durum"] == "flagged"]
    print("== depodaki butun isaretliler: %d ==" % len(isaretli))
    for k, v in collections.Counter(x["tip"] for x in isaretli).most_common():
        print("  %-28s %d" % (k, v))
    print()
    print("== mekanizmaya gore ==")
    for k, v in collections.Counter(x["mek"] for x in isaretli).most_common():
        print("  %-20s %d" % (k, v))
    print()

    a = [k for k in isaretli
         if k["tip"] == "summary_completion" and k["skill"] == "reading" and k["e10"]]
    b = [k for k in isaretli if k["mek"] == "genel_kultur"]
    kapsam = a + [k for k in b if k not in a]

    print("== (a) E10 kokenli ozet ailesi: %d ==" % len(a))
    for k in a:
        print("  %-56s %2s  %-16s banka=%s  %s"
              % (k["dosya"], k["numara"], k["mek"], k["banka"], k["cevap"]))
    print()
    print("== (b) ayakta kalan genel_kultur: %d ==" % len(b))
    for k in b:
        print("  %-56s %-24s %2s  %s"
              % (k["dosya"], k["tip"], k["numara"], k["cevap"]))
    print()
    print("== KAPSAM TOPLAM: %d ==" % len(kapsam))
    print()
    print("== ozet ailesi bilanco (tum summary_completion, reading) ==")
    sc = [k for k in kayit if k["tip"] == "summary_completion" and k["skill"] == "reading"]
    print("  toplam soru:", len(sc))
    for k, v in collections.Counter(x["durum"] for x in sc).most_common():
        print("    %-12s %d" % (k, v))
    print("  banka'li:", sum(1 for x in sc if x["banka"]),
          " parcadan kelime:", sum(1 for x in sc if not x["banka"]))


if __name__ == "__main__":
    main()
