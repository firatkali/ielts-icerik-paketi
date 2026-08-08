"""E8 5. adim yardimcisi: dinleme sizinti olcumunun toplu tablosunu cikarir.

Kullanim: python tools/_e8_toplu.py [--liste]

`content/DOGRULAMA/SESSIZ-*.json` + `kalibrasyon/sessiz/<paket>-tur<N>.json`
dosyalarindan paket bazinda ve toplu orani hesaplar. Cevap anahtarina ve senaryo
metnine bakmaz; yalniz onceki dort caistirmanin kendi ciktilarini okur.

Dayanaklar iki sinifa ayrilir (2. calistirmada tanimlandi):
  anlamsal   -> option_wording, frame_wording, general_knowledge, logic,
                cross_question, grammar_cue
  sansa acik -> guess, number_guess, name_guess, coin_flip

`--liste` isaretlemeye girecek kalemleri "<id> <dayanak>" olarak basar.
"""

import collections
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

SANSA_ACIK = {"guess", "number_guess", "name_guess", "coin_flip"}

# Rapordaki gruplama (1-4. calistirma).
GRUP = {
    "multiple-choice-tek": "1. calistirma",
    "multiple-choice-cok": "2. calistirma",
    "matching": "2. calistirma",
    "form-completion": "3. calistirma",
    "note-completion": "3. calistirma",
    "table-completion": "3. calistirma",
    "sentence-completion": "4. calistirma",
    "summary-completion": "4. calistirma",
    "flow-chart-completion": "4. calistirma",
    "short-answer": "4. calistirma",
}


def paketler():
    out = []
    for f in sorted(glob.glob(ortak.yol("content", "DOGRULAMA", "SESSIZ-*.json"))):
        out.append(os.path.basename(f)[len("SESSIZ-"):-len(".json")])
    return out


def baskin_dayanak(paket):
    """Her kalemin uc turdaki cogunluk dayanagi."""
    say = collections.defaultdict(collections.Counter)
    for n in (1, 2, 3):
        yol = ortak.yol("kalibrasyon", "sessiz", "%s-tur%d.json" % (paket, n))
        with open(yol, encoding="utf-8") as f:
            for a in json.load(f)["answers"]:
                if a.get("basis"):
                    say[a["id"]][a["basis"]] += 1
    return {i: c.most_common(1)[0][0] for i, c in say.items()}


def topla():
    satir, isaret = [], []
    for p in paketler():
        d = ortak.oku("content/DOGRULAMA/SESSIZ-%s.json" % p)
        dayanak = baskin_dayanak(p)
        k3 = d["uc_turda_bilinen_k3"]
        anlamsal = [i for i in k3 if dayanak.get(i) not in SANSA_ACIK]
        sansli = [i for i in k3 if dayanak.get(i) in SANSA_ACIK]
        satir.append({
            "paket": p, "grup": GRUP.get(p, "?"),
            "kalem": d["toplam_kalem"], "numara": d["toplam_numara"],
            "olcum_disi": len(d.get("olcum_disi") or []),
            "k1": len(d["uc_turda_bilinen_k1"]), "k3": len(k3),
            "anlamsal": len(anlamsal), "sansli": sansli,
        })
        isaret += [(i, dayanak[i], p) for i in anlamsal]
    return satir, isaret


def json_yaz(satir, isaret):
    """Toplu tabloyu content/DOGRULAMA/SESSIZ-TOPLU.json olarak yazar."""
    t = collections.Counter()
    for s in satir:
        for k in ("kalem", "numara", "olcum_disi", "k1", "k3", "anlamsal"):
            t[k] += s[k]
        t["sansli"] += len(s["sansli"])
    veri = {
        "tarih": "2026-08-08",
        "kaynak": "prompts/OPUS5-E8-dinleme-sessiz-olcum.md (5. calistirma)",
        "olculen_kalem": t["kalem"],
        "olcum_disi_kalem": t["olcum_disi"],
        "olculen_numara": t["numara"],
        "olculmeyen_tip": {"plan-map-diagram-labelling": "gorsel gerektirir"},
        "k1": t["k1"], "k3": t["k3"],
        "anlamsal_dayanakli": t["anlamsal"],
        "sansa_acik_3_3": t["sansli"],
        "paket_bazinda": [
            {k: s[k] for k in ("paket", "grup", "kalem", "numara", "olcum_disi",
                               "k1", "k3", "anlamsal")}
            for s in satir],
        "isaretlenen": sorted(i for i, _, _ in isaret),
    }
    ortak.yaz("content/DOGRULAMA/SESSIZ-TOPLU.json", veri)
    print("yazildi: content/DOGRULAMA/SESSIZ-TOPLU.json (%d isaretli kalem)"
          % len(isaret))


def main():
    satir, isaret = topla()
    if "--json" in sys.argv:
        json_yaz(satir, isaret)
        return 0
    if "--liste" in sys.argv:
        for i, b, p in isaret:
            print("%s\t%s\t%s" % (i, b, p))
        return 0

    print("%-24s %-13s %6s %6s %5s %5s %5s %5s"
          % ("paket", "grup", "kalem", "numara", "disi", "K1", "K3", "anlam"))
    t = collections.Counter()
    for s in satir:
        print("%-24s %-13s %6d %6d %5d %5d %5d %5d"
              % (s["paket"], s["grup"], s["kalem"], s["numara"],
                 s["olcum_disi"], s["k1"], s["k3"], s["anlamsal"]))
        for k in ("kalem", "numara", "olcum_disi", "k1", "k3", "anlamsal"):
            t[k] += s[k]
        for i in s["sansli"]:
            t["sansli"] += 1
    # SESSIZ-*.json'daki `toplam_kalem` zaten olcum disi birakilanlari icermez.
    olculen = t["kalem"]
    print("%-24s %-13s %6d %6d %5d %5d %5d %5d"
          % ("TOPLAM", "", t["kalem"], t["numara"], t["olcum_disi"],
             t["k1"], t["k3"], t["anlamsal"]))
    print("\nOlculen kalem: %d (+ olcum disi %d = %d kalem)"
          % (olculen, t["olcum_disi"], olculen + t["olcum_disi"]))
    print("K1 orani: %.1f%%  K3 orani: %.1f%%  anlamsal dayanakli: %.1f%%"
          % (100.0 * t["k1"] / olculen, 100.0 * t["k3"] / olculen,
             100.0 * t["anlamsal"] / olculen))
    print("3/3 tuttugu halde dayanagi sansa acik (isaretlenmeyecek): %d"
          % t["sansli"])
    print("Isaretlenecek kalem: %d" % len(isaret))
    return 0


if __name__ == "__main__":
    sys.exit(main())
