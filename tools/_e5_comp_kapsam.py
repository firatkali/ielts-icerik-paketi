# -*- coding: utf-8 -*-
"""E5 4. calistirma - kapsam sayimi: tamamlama ailesinde esdizim kilidi."""
import json, glob, collections, os

COMP = {"note_completion", "sentence_completion", "summary_completion",
        "table_completion", "flow_chart_completion"}


def sorular(d, path=()):
    if isinstance(d, dict):
        if "status" in d and "number" in d:
            yield d
        for k, v in d.items():
            yield from sorular(v, path + (k,))
    elif isinstance(d, list):
        for v in d:
            yield from sorular(v, path)


def main():
    mek = collections.Counter()
    tip_mek = collections.Counter()
    dosya = collections.Counter()
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
        skill = d.get("skill")
        for q in sorular(d):
            if q.get("status") != "flagged":
                continue
            m = q.get("flag_mechanism")
            mek[m] += 1
            tip_mek[(qt, m)] += 1
            if qt in COMP and m == "esdizim_kilidi" and skill == "reading":
                dosya[pn] += 1
                kayit.append((pn, qt, q.get("number"),
                              q.get("blind_solvable_kelime_duzeyi") is not None))
    print("== butun isaretlilerde mekanizma ==")
    for k, v in mek.most_common():
        print("  %-18s %d" % (k, v))
    print("toplam isaretli:", sum(mek.values()))
    print()
    print("== tamamlama ailesi x mekanizma ==")
    for (qt, m), v in sorted(tip_mek.items(), key=lambda x: str(x[0])):
        if qt in COMP:
            print("  %-24s %-18s %d" % (qt, m, v))
    print()
    print("== esdizim_kilidi, tamamlama ailesi, okuma ==")
    for k, v in sorted(dosya.items()):
        print("  %2d  %s" % (v, k))
    print("toplam:", sum(dosya.values()))
    e1 = [k for k in kayit if not k[3]]
    e10 = [k for k in kayit if k[3]]
    print("  E1 kokenli (kelime_duzeyi alani yok):", len(e1))
    print("  E10 kokenli (kelime_duzeyi alani var):", len(e10))
    print()
    print("== E1 kokenli liste ==")
    for k in e1:
        print("   ", k[0], k[1], k[2])
    print("== E10 kokenli liste ==")
    for k in e10:
        print("   ", k[0], k[1], k[2])


if __name__ == "__main__":
    main()
