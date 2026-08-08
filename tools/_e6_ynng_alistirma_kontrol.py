# -*- coding: utf-8 -*-
"""OPUS5-E6 2. calistirma: alistirma YNNG paketinin kontrolu.

Sinananlar:
  - soru sayisi 15, numaralar 1..15 (hicbir soru silinmemis/kaymamis)
  - her kanit cumlesi ilgili pasajda birebir geciyor ve locator dogru
  - kanit paragraf/cumle sirasi soru sirasiyla artan (IELTS sira kurali)
  - ifade ile pasaj arasinda 6 kelimelik birebir ortusme yok
  - cevap dagilimi ve ust uste ayni cevap sayisi
  - kip imzasi sayimi (dogru taraf = YES, celdirici taraf = NO/NOT GIVEN)

Kullanim: python tools/_e6_ynng_alistirma_kontrol.py
"""
import io
import json
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOSYA = os.path.join(KOK, "content", "reading", "practice", "yes-no-not-given.json")

MUTLAK = ["clearly", "only", "essential", "no difference", "every", "all four",
          "always", "never", "nothing", "one and the same", "both fixed",
          "entirely", "any other", "every other", "no ", "must "]
OLCULU = ["may ", "might", "probably", "plausible", "seems", "seem ", "seem to",
          "appear", "roughly", "about the same", "tended", "tends", "a little",
          "is said to", "suggest", "likely", "somewhat", "mainly"]

hata = 0


def cumleler(metin):
    return re.split(r'(?<=[.!?])\s+(?=[A-Z"“])', metin.strip())


def kip(s):
    d = s.lower()
    m = [w for w in MUTLAK if w in d]
    o = [w for w in OLCULU if w in d]
    if m and not o:
        return "mutlak", m
    if o and not m:
        return "olculu", o
    if o and m:
        return "karma", m + o
    return "notr", []


def main():
    global hata
    d = json.load(open(DOSYA, encoding="utf-8"))
    items = d["items"]
    if len(items) != 15 or [i["number"] for i in items] != list(range(1, 16)):
        hata += 1
        print("!! soru sayisi/numaralari bozuk:", [i["number"] for i in items])

    pasajlar = {}
    for it in items:
        pid = it["passage_id"]
        if pid not in pasajlar:
            p = json.load(open(os.path.join(KOK, "passages", "academic", pid + ".json"),
                               encoding="utf-8"))
            pasajlar[pid] = {x["label"]: x["text"] for x in p["paragraphs"]}

    onceki = {}
    for it in items:
        pid, no = it["passage_id"], it["number"]
        ev, loc = it.get("evidence"), it.get("evidence_locator")
        etiket = "#%-2d %s %-11s" % (no, pid, it["answer"][0])

        if bool(ev) != bool(loc):
            hata += 1
            print("!! #%d: evidence ile locator uyusmuyor" % no)
        if ev:
            par = pasajlar[pid].get(loc["paragraph"])
            if par is None or " ".join(ev.split()) not in " ".join(par.split()):
                hata += 1
                print("!! #%d: KANIT %s paragrafinda birebir gecmiyor" % (no, loc["paragraph"]))
            else:
                cs = cumleler(par)
                idx = loc["sentence"] - 1
                if not (0 <= idx < len(cs)) or " ".join(cs[idx].split()) != " ".join(ev.split()):
                    hata += 1
                    print("!! #%d: locator cumle no yanlis (%s/%d, paragrafta %d cumle)"
                          % (no, loc["paragraph"], loc["sentence"], len(cs)))
            anahtar = (loc["paragraph"], loc["sentence"])
            if pid in onceki and anahtar <= onceki[pid]:
                hata += 1
                print("!! #%d: sira kurali bozuk (%s%d <= onceki %s%d)"
                      % (no, anahtar[0], anahtar[1], onceki[pid][0], onceki[pid][1]))
            onceki[pid] = anahtar
        else:
            if it.get("not_given_justification") is None:
                hata += 1
                print("!! #%d: NOT GIVEN gerekcesi yok" % no)

        tam = " ".join(" ".join(t.split()) for t in pasajlar[pid].values()).lower()
        kel = re.findall(r"[a-z0-9']+", it["prompt"].lower())
        for i in range(len(kel) - 5):
            oc = " ".join(kel[i:i + 6])
            if oc in tam:
                hata += 1
                print("!! #%d: 6 kelimelik birebir ortusme -> %s" % (no, oc))
        t, kelimeler = kip(it["prompt"])
        print("%s kanit %-6s kip %-7s %s" % (
            etiket, (loc["paragraph"] + str(loc["sentence"])) if loc else "-", t,
            ",".join(kelimeler[:3])))

    print()
    dag = {}
    for it in items:
        dag[it["answer"][0]] = dag.get(it["answer"][0], 0) + 1
    print("cevap dagilimi:", dag)
    seri = [it["answer"][0] for it in items]
    for i in range(len(seri) - 2):
        if seri[i] == seri[i + 1] == seri[i + 2]:
            hata += 1
            print("!! ardisik uc ayni cevap: soru %d-%d" % (i + 1, i + 3))

    dogru = [it for it in items if it["answer"] == ["YES"]]
    celd = [it for it in items if it["answer"] != ["YES"]]
    dm = [it["number"] for it in dogru if kip(it["prompt"])[0] in ("mutlak", "karma")]
    co = [it["number"] for it in celd if kip(it["prompt"])[0] in ("olculu", "karma")]
    print("dogru taraf (YES) %d soru - mutlak ifade tasiyan: %s -> %.0f%% (esik %%33)"
          % (len(dogru), dm, 100.0 * len(dm) / len(dogru)))
    print("celdirici taraf (NO/NG) %d soru - olculu ifade tasiyan: %s -> %.0f%% (esik %%33)"
          % (len(celd), co, 100.0 * len(co) / len(celd)))
    if len(dm) * 3 < len(dogru):
        hata += 1
        print("!! kip imzasi: dogru cevaplarda mutlak ifade orani ucte birin altinda")
    if len(co) * 3 < len(celd):
        hata += 1
        print("!! kip imzasi: celdiricilerde olculu ifade orani ucte birin altinda")

    print("\nHATA:", hata)
    return 1 if hata else 0


if __name__ == "__main__":
    sys.exit(main())
