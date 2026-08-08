# -*- coding: utf-8 -*-
"""OPUS5-E6 5. calistirma kontrolu: ozellik esleystirme yuvalari.

Denetledigi seyler:
  1. Yeniden doldurulan her yuva: status/generated_by/blind_solvable alanlari,
     yeniden_uretim kaydi, bos alan yok.
  2. Kanit cumlesi pasajda BIREBIR var mi ve evidence_locator dogru mu.
  3. Yeni kanit, E5'in "kacinilacak" dedigi cumleye degiyor mu; yeni ifade eski
     ifadenin tekrari mi.
  4. Cevap harfleri secenek listesinde var mi; allow_repeat=false olan dosyada
     harf tekrari var mi.
  5. Harf dagilimi (konumsal duzen yasagi) ve son paragrafa demirlenme.
  6. Kip sayimi (kip imzasi yasagi): ifadelerde mutlak / olculu dil.

Kullanim: python tools/_e6_mf_eslestirme_kontrol.py
"""
import collections
import io
import json
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LISTE = os.path.join(KOK, "content", "DOGRULAMA", "yeniden-uretim-listesi.json")

DOSYALAR = [
    "content/reading/practice/matching-features.json",
    "content/reading/tests/AC1/matching-features.json",
    "content/reading/tests/AC2/matching-features.json",
    "content/reading/tests/AC4/matching-features.json",
]

MUTLAK = ["only", "every", "all ", "no ", "never", "fewest", "alone", "both",
          "any ", "most ", "the first"]
OLCULU = ["about", "roughly", "may ", "might", "some ", "as though", "appeared",
          "seemed", "cautiously", "suggest", "likely", "rather than"]

hatalar = []


def pasaj_paragraflari(pid):
    for kok in ("academic", "general"):
        p = os.path.join(KOK, "passages", kok, pid + ".json")
        if os.path.exists(p):
            d = json.load(open(p, encoding="utf-8"))
            return {x["label"]: x["text"] for x in d["paragraphs"]}
    raise SystemExit("pasaj yok: " + pid)


def cumleler(metin):
    return re.split(r"(?<=[.!?])\s+", metin.strip())


def yuvalar(d):
    """(group, item) ciftleri - hem gruplu hem duz dosyalar icin."""
    for g in (d["groups"] if "groups" in d else [d]):
        for it in g["items"]:
            yield g, it


def main():
    e5 = {(x["dosya"], x["numara"]): x for x in
          json.load(open(LISTE, encoding="utf-8"))["elenen"]}
    yeni_ifadeler = []
    toplam = 0

    for rel in DOSYALAR:
        p = os.path.join(KOK, rel.replace("/", os.sep))
        d = json.load(open(p, encoding="utf-8"))
        print("\n== %s" % rel)
        for g, it in yuvalar(d):
            no = it["number"]
            anahtar = "%s#%s" % (rel, no)
            secenekler = [o["key"] for o in g["option_list"]["options"]]

            for h in it["answer"]:
                if h not in secenekler:
                    hatalar.append("%s: cevap harfi listede yok (%s)" % (anahtar, h))
            if it.get("status") == "rejected":
                hatalar.append("%s: hala rejected" % anahtar)

            if not it.get("yeniden_uretim"):
                continue
            toplam += 1
            yeni_ifadeler.append((anahtar, it["prompt"]))

            if it.get("status") != "verified":
                hatalar.append("%s: status verified degil" % anahtar)
            if it.get("generated_by") != "opus":
                hatalar.append("%s: generated_by opus degil" % anahtar)
            if it.get("blind_solvable") is not None:
                hatalar.append("%s: blind_solvable null olmali" % anahtar)
            for alan in ("prompt", "evidence", "explanation", "feature_check"):
                if not it.get(alan):
                    hatalar.append("%s: %s bos" % (anahtar, alan))

            # kanit pasajda birebir mi
            pid = g.get("passage_id") or d.get("passage_id")
            pars = pasaj_paragraflari(pid)
            loc = it["evidence_locator"]
            cs = cumleler(pars[loc["paragraph"]])
            if it["evidence"] != cs[loc["sentence"] - 1]:
                hatalar.append("%s: kanit cumlesi pasajla birebir eslesmiyor" % anahtar)
            if loc["paragraph"] == sorted(pars)[-1]:
                hatalar.append("%s: kanit son paragrafa demirlenmis" % anahtar)

            # E5'in yasakladigi cumle / ifade
            kayit = e5.get((rel, no))
            if kayit:
                kac = kayit["kacinilacak"]
                if kac["kanit_cumlesi"].strip() == it["evidence"].strip():
                    hatalar.append("%s: E5'in yasakladigi kanit cumlesi kullanilmis" % anahtar)
                if kac["ifade"].strip() == it["prompt"].strip():
                    hatalar.append("%s: eski ifade aynen tekrarlanmis" % anahtar)
            print("   %-4s %-4s %s/%s  %s" % (no, ",".join(it["answer"]),
                                              loc["paragraph"], loc["sentence"],
                                              it["prompt"][:64]))

        for g in (d["groups"] if "groups" in d else [d]):
            harfler = [h for it in g["items"] for h in it["answer"]]
            sayim = collections.Counter(harfler)
            if not g.get("allow_repeat") and max(sayim.values()) > 1:
                hatalar.append("%s (%s): allow_repeat false ama harf tekrari var"
                               % (rel, g.get("group_id", "-")))
            print("   harf dagilimi %s: %s"
                  % (g.get("group_id", "-"), dict(sorted(sayim.items()))))

    print("\n=== KIP SAYIMI (yeni ifadeler) ===")
    m = o = 0
    for anahtar, ifade in yeni_ifadeler:
        alt = ifade.lower()
        mv = [k for k in MUTLAK if k in alt]
        ov = [k for k in OLCULU if k in alt]
        m += 1 if mv else 0
        o += 1 if ov else 0
        print("   %-52s mutlak=%-22s olculu=%s" % (anahtar, ",".join(mv) or "-",
                                                   ",".join(ov) or "-"))
    n = len(yeni_ifadeler)
    print("   mutlak tasiyan: %d/%d (%.0f%%) | olculu tasiyan: %d/%d (%.0f%%) | esik %%33"
          % (m, n, 100.0 * m / n, o, n, 100.0 * o / n))
    if m * 3 < n:
        hatalar.append("kip imzasi: mutlak ifade orani ucte birin altinda")
    if o * 3 < n:
        hatalar.append("kip imzasi: olculu ifade orani ucte birin altinda")

    print("\n=== HATA: %d ===" % len(hatalar))
    for h in hatalar:
        print("  -", h)
    print("yeniden doldurulan yuva:", toplam)


if __name__ == "__main__":
    main()
