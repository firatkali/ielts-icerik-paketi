# -*- coding: utf-8 -*-
"""OPUS5-E6 3. calistirma: coktan secmeli tam test paketlerinin kontrolu.

Sinananlar (bes dosyanin hepsi, yalniz yeniden uretilenler degil):
  - soru sayisi ve numaralar degismemis, select_count korunmus
  - cevap harfleri secenek listesinde var ve sayisi select_count kadar
  - her kanit cumlesi ilgili pasajda birebir geciyor ve locator dogru
  - kanit sirasi soru sirasiyla artan (IELTS sira kurali)
  - hicbir secenek metni pasajla 6 kelimelik birebir ortusme tasimiyor
  - dogru harf dagilimi ve iki-harfli yuvalarda harf ciftleri
  - kip imzasi sayimi (dogru secenek / celdirici, mutlak / olculu)

Kullanim: python tools/_e6_mc_testler_kontrol.py
"""
import collections
import io
import json
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DOSYALAR = ["content/reading/tests/AC1/multiple-choice.json",
            "content/reading/tests/AC2/multiple-choice.json",
            "content/reading/tests/AC3/multiple-choice.json",
            "content/reading/tests/AC4/multiple-choice.json",
            "content/reading/tests/GT1/multiple-choice.json",
            "content/reading/tests/GT2/multiple-choice.json"]

BEKLENEN = {"AC1": ["32", "33", "34-35"], "AC2": ["32", "33", "34-35"],
            "AC3": ["32", "33", "34-35"], "AC4": ["32", "33", "34-35"],
            "GT1": ["21", "22", "23-24"], "GT2": ["21", "22", "23-24"]}

MUTLAK = ["all ", " all", "every", "always", "never", "only", "any ", "no ",
          "must ", "the whole time", "exactly", "altogether", "everyone",
          "single", "each ", "entirely", "whole"]
OLCULU = ["may ", "might", "probably", "likely", "roughly", "about ", "usually",
          "mainly", "seems", "appear", "tends", "on average", "fairly",
          "some ", "generally", "often", "suggest"]


def cumleler(metin):
    return re.split(r'(?<=[.!?])\s+(?=[A-Z"“])', metin.strip())


def pasaj_yukle(pid, modul):
    p = json.load(open(os.path.join(KOK, "passages", modul, pid + ".json"),
                       encoding="utf-8"))
    par = {}
    if p.get("paragraphs"):
        for x in p["paragraphs"]:
            par[(None, x["label"])] = x["text"]
    for t in (p.get("texts") or []):
        for blok in t["text"].split("\n\n"):
            satir = blok.split("\n")
            par[(t["label"], satir[0].strip())] = " ".join(satir[1:]).strip()
    return par


def kip(s):
    d = " " + s.lower() + " "
    m = [w for w in MUTLAK if w in d]
    o = [w for w in OLCULU if w in d]
    if m and not o:
        return "mutlak"
    if o and not m:
        return "olculu"
    if o and m:
        return "karma"
    return "notr"


def main():
    hata = 0
    dogru_harf = collections.Counter()
    ciftler = collections.Counter()
    say = {"dogru_mutlak": [], "dogru_toplam": 0,
           "celd_olculu": [], "celd_toplam": 0}

    for rel in DOSYALAR:
        d = json.load(open(os.path.join(KOK, rel.replace("/", os.sep)), encoding="utf-8"))
        test = d["test_id"]
        modul = "academic" if d["module"] == "academic" else "general"
        par = pasaj_yukle(d["passage_id"], modul)
        nums = [str(it["number"]) for it in d["items"]]
        if nums != BEKLENEN[test]:
            hata += 1
            print("!! %s: soru numaralari bozuk %s" % (test, nums))

        onceki = None
        print("\n== %s (%s)" % (test, d["passage_id"]))
        for it in d["items"]:
            no, sc = str(it["number"]), it.get("select_count")
            harfler = [o["letter"] for o in it["options"]]
            if len(it["answer"]) != sc:
                hata += 1
                print("!! %s #%s: cevap sayisi select_count ile uyusmuyor" % (test, no))
            for a in it["answer"]:
                if a not in harfler:
                    hata += 1
                    print("!! %s #%s: cevap harfi secenekte yok: %s" % (test, no, a))

            loc, ev = it["evidence_locator"], " ".join(it["evidence"].split())
            metin = par.get((loc.get("text"), loc["paragraph"]))
            if metin is None:
                hata += 1
                print("!! %s #%s: paragraf bulunamadi %s" % (test, no, loc))
                continue
            cs = cumleler(metin)
            idx = loc["sentence"] - 1
            # Kanit birden cok cumle olabilir; ilki locator'in gosterdigi cumle olmali.
            ilk = cumleler(it["evidence"])[0]
            if " ".join(ilk.split()) not in " ".join(metin.split()):
                hata += 1
                print("!! %s #%s: KANIT %s paragrafinda birebir gecmiyor" % (test, no, loc))
            elif not (0 <= idx < len(cs)) or " ".join(cs[idx].split()) != " ".join(ilk.split()):
                hata += 1
                print("!! %s #%s: locator cumle no yanlis (%s/%s, paragrafta %d cumle)"
                      % (test, no, loc["paragraph"], loc["sentence"], len(cs)))
            anahtar = (loc.get("text") or "", loc["paragraph"], loc["sentence"])
            if onceki and anahtar <= onceki:
                hata += 1
                print("!! %s #%s: sira kurali bozuk (%s <= onceki %s)" % (test, no, anahtar, onceki))
            onceki = anahtar

            # Birebir ortusme yalniz bu calistirmanin yazdigi yuvalarda hata sayilir;
            # onceki uretimlerin seceneklerinde bulunursa not olarak basilir.
            tam = " ".join(" ".join(t.split()) for t in par.values()).lower()
            for o in it["options"]:
                kel = re.findall(r"[a-z0-9']+", o["text"].lower())
                for i in range(len(kel) - 5):
                    oc = " ".join(kel[i:i + 6])
                    if oc not in tam:
                        continue
                    if it.get("generated_by") == "opus":
                        hata += 1
                        print("!! %s #%s %s: 6 kelimelik birebir ortusme -> %s"
                              % (test, no, o["letter"], oc))
                    else:
                        print("   (not) %s #%s %s eski uretim, birebir ortusme -> %s"
                              % (test, no, o["letter"], oc))

            if sc == 2:
                ciftler["+".join(sorted(it["answer"]))] += 1
            for a in it["answer"]:
                dogru_harf[a] += 1

            if it.get("generated_by") == "opus":
                for o in it["options"]:
                    t = kip(o["text"])
                    if o["letter"] in it["answer"]:
                        say["dogru_toplam"] += 1
                        if t in ("mutlak", "karma"):
                            say["dogru_mutlak"].append("%s#%s%s" % (test, no, o["letter"]))
                    else:
                        say["celd_toplam"] += 1
                        if t in ("olculu", "karma"):
                            say["celd_olculu"].append("%s#%s%s" % (test, no, o["letter"]))

            print("  #%-6s sc=%d cevap %-6s kanit %s%s/%s  %s"
                  % (no, sc, ",".join(it["answer"]), loc.get("text") or "",
                     loc["paragraph"], loc["sentence"], it["status"]))

    print("\ndogru harf dagilimi:", dict(sorted(dogru_harf.items())))
    print("iki-harfli yuvalarda ciftler:", dict(sorted(ciftler.items())))
    for c, n in ciftler.items():
        if n > 2:
            hata += 1
            print("!! ayni harf cifti ikiden fazla: %s (%d)" % (c, n))

    dm, dt = len(say["dogru_mutlak"]), say["dogru_toplam"]
    co, ct = len(say["celd_olculu"]), say["celd_toplam"]
    print("\nyeniden uretilen yuvalarin kip sayimi (yalniz generated_by=opus):")
    print("  dogru secenek %d - mutlak ifade tasiyan %d (%%%.0f, esik %%33) %s"
          % (dt, dm, 100.0 * dm / dt, say["dogru_mutlak"]))
    print("  celdirici %d - olculu ifade tasiyan %d (%%%.0f, esik %%33)"
          % (ct, co, 100.0 * co / ct))
    if dm * 3 < dt:
        hata += 1
        print("!! kip imzasi: dogru seceneklerde mutlak oran ucte birin altinda")
    if co * 3 < ct:
        hata += 1
        print("!! kip imzasi: celdiricilerde olculu oran ucte birin altinda")

    print("\nHATA:", hata)
    return 1 if hata else 0


if __name__ == "__main__":
    sys.exit(main())
