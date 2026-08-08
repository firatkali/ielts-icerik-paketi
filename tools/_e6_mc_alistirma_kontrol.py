# -*- coding: utf-8 -*-
"""OPUS5-E6 4. calistirma: coktan secmeli alistirma paketinin kontrolu.

Sinananlar (dosyanin tamami, yalniz yeniden uretilenler degil):
  - soru sayisi ve numaralar degismemis, select_count ve passage_id korunmus
  - cevap harfleri secenek listesinde var ve sayisi select_count kadar
  - her kanit cumlesi ilgili pasajda birebir geciyor ve locator dogru
  - kanit sirasi soru sirasiyla artan (her pasaj blogu kendi icinde)
  - hicbir secenek metni pasajla 6 kelimelik birebir ortusme tasimiyor
  - dogru harf dagilimi ve iki-harfli yuvalarda harf ciftleri
  - kip imzasi sayimi (dogru secenek / celdirici, mutlak / olculu)

Kullanim: python tools/_e6_mc_alistirma_kontrol.py
"""
import collections
import io
import json
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOSYA = "content/reading/practice/multiple-choice.json"

BEKLENEN = ["1", "2", "3-4", "5", "6", "7-8", "9-10", "11", "12", "13", "14", "15"]

MUTLAK = ["all ", " all", "every", "always", "never", "only", "any ", "no ",
          "must ", "the whole time", "exactly", "altogether", "everyone",
          "single", "each ", "entirely", "whole"]
OLCULU = ["may ", "might", "probably", "likely", "roughly", "about ", "usually",
          "mainly", "seems", "appear", "tends", "on average", "fairly",
          "some ", "generally", "often", "suggest"]


def cumleler(metin):
    return re.split(r'(?<=[.!?])\s+(?=[A-Z"“])', metin.strip())


def pasaj_yukle(pid):
    p = json.load(open(os.path.join(KOK, "passages", "academic", pid + ".json"),
                       encoding="utf-8"))
    return {x["label"]: x["text"] for x in p["paragraphs"]}


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

    d = json.load(open(os.path.join(KOK, DOSYA.replace("/", os.sep)), encoding="utf-8"))
    nums = [str(it["number"]) for it in d["items"]]
    if nums != BEKLENEN:
        hata += 1
        print("!! soru numaralari bozuk %s" % nums)

    pasajlar, onceki, onceki_pid = {}, None, None
    for it in d["items"]:
        no, sc, pid = str(it["number"]), it.get("select_count"), it["passage_id"]
        if pid not in pasajlar:
            pasajlar[pid] = pasaj_yukle(pid)
        par = pasajlar[pid]
        harfler = [o["letter"] for o in it["options"]]
        if len(it["answer"]) != sc:
            hata += 1
            print("!! #%s: cevap sayisi select_count ile uyusmuyor" % no)
        for a in it["answer"]:
            if a not in harfler:
                hata += 1
                print("!! #%s: cevap harfi secenekte yok: %s" % (no, a))

        loc = it["evidence_locator"]
        metin = par.get(loc["paragraph"])
        if metin is None:
            hata += 1
            print("!! #%s: paragraf bulunamadi %s" % (no, loc))
            continue
        cs = cumleler(metin)
        idx = loc["sentence"] - 1
        # Kanit birden cok cumle olabilir; ilki locator'in gosterdigi cumle olmali.
        ilk = cumleler(it["evidence"])[0]
        if " ".join(ilk.split()) not in " ".join(metin.split()):
            hata += 1
            print("!! #%s: KANIT %s paragrafinda birebir gecmiyor" % (no, loc))
        elif not (0 <= idx < len(cs)) or " ".join(cs[idx].split()) != " ".join(ilk.split()):
            hata += 1
            print("!! #%s: locator cumle no yanlis (%s/%s, paragrafta %d cumle)"
                  % (no, loc["paragraph"], loc["sentence"], len(cs)))
        # Kanit birden cok cumleyse hepsi ayni pasajda gecmeli.
        for c in cumleler(it["evidence"])[1:]:
            if not any(" ".join(c.split()) in " ".join(t.split()) for t in par.values()):
                hata += 1
                print("!! #%s: ek kanit cumlesi pasajda yok: %s" % (no, c[:60]))

        anahtar = (loc["paragraph"], loc["sentence"])
        if pid == onceki_pid and onceki and anahtar <= onceki:
            hata += 1
            print("!! #%s: sira kurali bozuk (%s <= onceki %s)" % (no, anahtar, onceki))
        onceki, onceki_pid = anahtar, pid

        # Birebir ortusme yalniz bu calistirmanin yazdigi yuvalarda hata sayilir.
        tam = " ".join(" ".join(t.split()) for t in par.values()).lower()
        for o in it["options"]:
            kel = re.findall(r"[a-z0-9']+", o["text"].lower())
            for i in range(len(kel) - 5):
                oc = " ".join(kel[i:i + 6])
                if oc not in tam:
                    continue
                if it.get("generated_by") == "opus":
                    hata += 1
                    print("!! #%s %s: 6 kelimelik birebir ortusme -> %s" % (no, o["letter"], oc))
                else:
                    print("   (not) #%s %s eski uretim, birebir ortusme -> %s"
                          % (no, o["letter"], oc))

        # distractor_analysis butun celdiricileri kapsamali
        if it.get("generated_by") == "opus":
            bekl = sorted(h for h in harfler if h not in it["answer"])
            varsa = sorted(it.get("distractor_analysis") or {})
            if bekl != varsa:
                hata += 1
                print("!! #%s: distractor_analysis eksik/fazla %s != %s" % (no, varsa, bekl))
            for k in ("status", "blind_solvable", "blind_basis"):
                pass
            if it.get("status") != "verified" or it.get("blind_solvable") is not None:
                hata += 1
                print("!! #%s: status/blind_solvable beklenen degerde degil" % no)
            for eski_alan in ("flag_reason", "flag_mechanism", "reject_reason"):
                if eski_alan in it:
                    hata += 1
                    print("!! #%s: eskiyen alan silinmemis: %s" % (no, eski_alan))

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
                        say["dogru_mutlak"].append("#%s%s" % (no, o["letter"]))
                else:
                    say["celd_toplam"] += 1
                    if t in ("olculu", "karma"):
                        say["celd_olculu"].append("#%s%s" % (no, o["letter"]))

        print("  #%-6s sc=%d %s cevap %-6s kanit %s/%s  %s%s"
              % (no, sc, pid, ",".join(it["answer"]), loc["paragraph"], loc["sentence"],
                 it["status"], "  [YENI]" if it.get("generated_by") == "opus" else ""))

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
