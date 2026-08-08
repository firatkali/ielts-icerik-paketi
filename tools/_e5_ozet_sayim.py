# -*- coding: utf-8 -*-
"""E5 8. calistirma - olcum: parcasiz uc turun cevaplari, kapsamdaki her soru icin.

Iki olcut (7. calistirmadan devralindi, ozet ailesine uyarlandi):
  1) modelin parcasiz cevabi dogru cevabin AYIRT EDICI ogesini tasiyor mu
  2) boslugun bas adi ozet cumlesinin anlamsal rolu tarafindan zorunlu kilinmis mi
Bu betik yalniz (1)'i mekanik olarak olcer; (2) elle karara baglanir.
"""
import json, glob, re, collections

DUMP = "kalibrasyon/metinsiz/%s-tur%d.json"
PAKET = ["summary-completion", "sentence-completion", "short-answer",
         "note-completion", "table-completion", "flow-chart-completion"]


def sorular(d):
    if isinstance(d, dict):
        if "status" in d and "number" in d:
            yield d
        for v in d.values():
            yield from sorular(v)
    elif isinstance(d, list):
        for v in d:
            yield from sorular(v)


def dokum():
    out = collections.defaultdict(lambda: [None, None, None])
    for p in PAKET:
        for t in (1, 2, 3):
            try:
                d = json.load(open(DUMP % (p, t), encoding="utf-8"))
            except Exception:
                continue
            for a in d["answers"]:
                out[a["id"]][t - 1] = a.get("answer")
    return out


def norm(s):
    return re.sub(r"[^a-z0-9 ]", " ", str(s).lower()).split()


def main():
    dok = dokum()
    satir = []
    for p in sorted(glob.glob("content/reading/**/*.json", recursive=True)):
        pn = p.replace("\\", "/")
        d = json.load(open(p, encoding="utf-8"))
        if not isinstance(d, dict) or d.get("skill") != "reading":
            continue
        qt = d.get("question_type")
        if qt not in {x.replace("-", "_") for x in PAKET}:
            continue
        sid = d.get("set_id")
        for q in sorular(d):
            if q.get("status") != "flagged":
                continue
            e10 = "blind_solvable_kelime_duzeyi" in q
            mek = q.get("flag_mechanism")
            if not (e10 and qt == "summary_completion") and mek != "genel_kultur":
                continue
            kid = "%s-%s" % (sid, q.get("number"))
            turlar = dok.get(kid, [None, None, None])
            dogru = norm(" ".join(q.get("answer") or []))
            bas = dogru[-1] if dogru else ""
            nitel = dogru[:-1]
            # ayirt edici oge: cok sozcuklu cevapta niteleyici, tek sozcukluda sozcugun kendisi
            ayirt = nitel if nitel else [bas]
            # kabul listesi: cevap + accepted_variants, normalize edilmis
            kabul = set()
            for v in (q.get("accepted_variants") or []) + (q.get("answer") or []):
                kabul.add(" ".join(norm(v)))
            tasiyor = 0
            puanlar = 0
            for t in turlar:
                if not t:
                    continue
                m = norm(" ".join(t if isinstance(t, list) else [t]))
                if all(any(a in w or w in a for w in m) for a in ayirt):
                    tasiyor += 1
                if " ".join(m) in kabul:
                    puanlar += 1
            satir.append({
                "dosya": pn, "tip": qt, "no": q.get("number"), "mek": mek,
                "kaynak": "E10" if e10 else "E1", "cevap": " ".join(dogru),
                "tur": [" ".join(norm(" ".join(t))) if t else "-" for t in turlar],
                "ayirt_tasiyor": tasiyor, "puanlar": puanlar,
            })

    print("== kapsam: %d soru ==" % len(satir))
    print()
    hdr = "%-42s %3s %-14s %-4s %-20s %-38s %5s %5s"
    print(hdr % ("dosya", "no", "mekanizma", "kyn", "dogru cevap",
                 "3 turun cevabi", "ayirt", "PUAN"))
    for s in satir:
        print(hdr % (s["dosya"][15:], s["no"], s["mek"], s["kaynak"],
                     s["cevap"][:20], " | ".join(s["tur"])[:38],
                     s["ayirt_tasiyor"], s["puanlar"]))
    print()
    c = collections.Counter(s["ayirt_tasiyor"] for s in satir)
    print("== ayirt edici ogeyi kac turda tutturdu ==")
    for k in sorted(c):
        print("  %d tur: %d soru" % (k, c[k]))
    print()
    p = collections.Counter(s["puanlar"] for s in satir)
    print("== parcasiz cevap kabul listesine gore KAC TURDA PUAN ALIRDI ==")
    for k in sorted(p):
        print("  %d tur: %d soru" % (k, p[k]))
    print("  3/3 puan alan: %d soru" % p[3])
    print()
    print("== alt kume kirilimi (3/3 puan alan) ==")
    for kaynak in ("E10", "E1"):
        alt = [s for s in satir if s["kaynak"] == kaynak]
        print("  %-4s %2d soruda %2d tanesi 3/3 puan alir"
              % (kaynak, len(alt), sum(1 for s in alt if s["puanlar"] == 3)))


if __name__ == "__main__":
    main()
