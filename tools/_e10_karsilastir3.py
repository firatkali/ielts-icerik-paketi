# -*- coding: utf-8 -*-
"""E10 3. calistirma yardimcisi: not/tablo/akis tamamlama paketlerinde uc turun
metinsiz cevaplarini gercek cevapla yan yana dizer. Karar insanda; bu betik
yalniz karsilastirma tablosunu basar.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

PAKETLER = ["note-completion", "table-completion", "flow-chart-completion"]


def main():
    for pak in PAKETLER:
        turlar = []
        for n in (1, 2, 3):
            d = json.load(open("kalibrasyon/metinsiz/%s-tur%d.json" % (pak, n),
                               encoding="utf-8"))
            turlar.append({a["id"]: a for a in d["answers"]})

        print("=" * 78)
        print("%s  (tur boyutlari: %s)" % (pak, [len(t) for t in turlar]))
        print("=" * 78)

        yollar = [p for p in ortak.bul("content/**/%s.json" % pak)
                  if "/DOGRULAMA/" not in p]
        gorulen = set()
        for p in yollar:
            d = ortak.oku(p)
            sid = d.get("set_id", os.path.basename(p))
            print("\n--- %s | skill=%s | %s" % (sid, d.get("skill"), p))
            for it in ortak.sorular(d):
                num = it.get("number")
                kid = "%s-%s" % (sid, num)
                gorulen.add(kid)
                cev = it.get("answer")
                var = it.get("accepted_variants") or []
                t = []
                for tr in turlar:
                    a = tr.get(kid)
                    t.append("/".join(a["answer"]) if a else "YOK")
                print("  %-4s | dogru=%-28s var=%-30s | %s || %s || %s | bs=%s st=%s"
                      % (num,
                         cev if isinstance(cev, str) else "/".join(cev or []),
                         ",".join(var)[:30],
                         t[0], t[1], t[2],
                         it.get("blind_solvable"), it.get("status")))
        fazla = set(turlar[0]) - gorulen
        if fazla:
            print("\n!! dokumde olup dosyada bulunmayan kimlikler: %s"
                  % sorted(fazla))
    return 0


if __name__ == "__main__":
    sys.exit(main())
