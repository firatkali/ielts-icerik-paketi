# -*- coding: utf-8 -*-
"""E5 7. calistirma - kapsam sayimi: E10'dan gelen cumle tamamlama + kisa cevap."""
import json, glob, collections

TIP = {"sentence_completion", "short_answer"}


def sorular(d):
    if isinstance(d, dict):
        if "status" in d and "number" in d:
            yield d
        for v in d.values():
            yield from sorular(v)
    elif isinstance(d, list):
        for v in d:
            yield from sorular(v)


def main():
    toplam = collections.Counter()
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
        for q in sorular(d):
            st = q.get("status")
            if st == "flagged":
                toplam[qt] += 1
            if qt in TIP and st == "flagged" and d.get("skill") == "reading":
                kayit.append({
                    "dosya": pn, "tip": qt, "numara": q.get("number"),
                    "mek": q.get("flag_mechanism"),
                    "e10": q.get("blind_solvable_kelime_duzeyi") is not None,
                    "basis": q.get("blind_basis"),
                    "cevap": q.get("answer"),
                })
    print("== butun isaretliler, tipe gore ==")
    for k, v in toplam.most_common():
        print("  %-28s %d" % (k, v))
    print("toplam isaretli:", sum(toplam.values()))
    print()
    e10 = [k for k in kayit if k["e10"]]
    e1 = [k for k in kayit if not k["e10"]]
    print("== cumle tamamlama + kisa cevap, isaretli %d ==" % len(kayit))
    print("  E10 kokenli:", len(e10), " E1 kokenli:", len(e1))
    print()
    print("== E10 kokenli (BU CALISTIRMANIN KAPSAMI) ==")
    for k in e10:
        print("  %-52s %-20s %2s  %-16s %-8s %s"
              % (k["dosya"], k["tip"], k["numara"], k["mek"], k["basis"], k["cevap"]))
    print()
    print("== E1 kokenli (kapsam disi) ==")
    for k in e1:
        print("  %-52s %-20s %2s  %-16s %-8s %s"
              % (k["dosya"], k["tip"], k["numara"], k["mek"], k["basis"], k["cevap"]))


if __name__ == "__main__":
    main()
