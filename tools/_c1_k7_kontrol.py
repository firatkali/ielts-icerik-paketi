# -*- coding: utf-8 -*-
"""7. grup uretiminin bicim kontrolu (tek seferlik, dosya degistirmez)."""
import glob
import json
import os
import re

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OLCUT = set(["fluency_coherence", "lexical_resource", "grammatical_range_accuracy"])


def cumle_say(metin):
    return len([p for p in re.split(r"(?<=[.?!])\s+", metin.strip()) if p])


def main():
    sorun = []
    yol = os.path.join(KOK, "content", "ornek-cevaplar", "speaking", "*.json")
    dosyalar = sorted(glob.glob(yol))
    if len(dosyalar) != 5:
        sorun.append("5 dosya bekleniyordu, %d bulundu" % len(dosyalar))
    for f in dosyalar:
        kod = os.path.basename(f)[:-5]
        with open(f, encoding="utf-8") as fh:
            d = json.load(fh)
        if d.get("task_ref") != kod:
            sorun.append("%s: task_ref dosya adiyla uyusmuyor" % kod)
        for alan in ("exam", "schema_version", "kind", "skill", "part"):
            if alan not in d:
                sorun.append("%s: %s alani yok" % (kod, alan))
        kart = os.path.join(KOK, "content", "speaking", "part2-3", kod + ".json")
        if not os.path.isfile(kart):
            sorun.append("%s: kart dosyasi havuzda yok" % kod)
        if [a["band"] for a in d["answers"]] != [5.0, 6.5, 8.0]:
            sorun.append("%s: band uclusu 5,0/6,5/8,0 degil" % kod)
        for a in d["answers"]:
            etiket = "%s / %s" % (kod, a["band"])
            if len(a["transcript"].split()) != a["word_count"]:
                sorun.append("%s: word_count gercek sayimla tutmuyor" % etiket)
            if a["word_count"] < 80:
                sorun.append("%s: 80 kelime alt sinirinin altinda" % etiket)
            if not 90 <= a["approx_duration_seconds"] <= 120:
                sorun.append("%s: sure 90-120 penceresi disinda" % etiket)
            if set(a["why_this_band"]) != OLCUT:
                sorun.append("%s: why_this_band uc olcut degil" % etiket)
            metinler = list(a["why_this_band"].items())
            metinler.append(("what_would_lift_it", a["what_would_lift_it"]))
            for ad, v in metinler:
                if not v.strip():
                    sorun.append("%s: %s bos" % (etiket, ad))
                elif cumle_say(v) > 2:
                    sorun.append("%s: %s %d cumle (sinir 2)" % (etiket, ad, cumle_say(v)))

    if sorun:
        for s in sorun:
            print("BULGU: %s" % s)
        raise SystemExit(1)
    print("5 dosya / 15 cevap - bulgu yok")


if __name__ == "__main__":
    main()
