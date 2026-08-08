# -*- coding: utf-8 -*-
"""E5 / 5. calistirma - E6 devir dosyasina elenen yuvalari ekler.

`content/DOGRULAMA/yeniden-uretim-listesi.json` uzerine yazmaz, ekler.
Ayni (dosya, numara) ikilisi zaten varsa atlanir; betik idempotenttir.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

LISTE = "content/DOGRULAMA/yeniden-uretim-listesi.json"
AC4 = "content/reading/tests/AC4/summary-completion.json"

ELENEN = [AC4]
NUMARALAR = {AC4: [36, 38]}


def main():
    liste = ortak.oku(LISTE)
    var = {(k["dosya"], k["numara"]) for k in liste["elenen"]}
    eklenen = 0

    for yol in ELENEN:
        veri = ortak.oku(yol)
        for it in ortak.sorular(veri):
            if it["number"] not in NUMARALAR[yol]:
                continue
            if it.get("status") != "rejected":
                raise SystemExit("beklenen rejected degil: %s %s"
                                 % (yol, it["number"]))
            if (yol, it["number"]) in var:
                continue
            liste["elenen"].append({
                "dosya": yol,
                "numara": it["number"],
                "tip": veri["question_type"],
                "pasaj": veri["passage_id"],
                "kacinilacak": {
                    "kanit_cumlesi": it["evidence"],
                    "ifade": it["prompt"],
                },
                "neden_elendi": it["reject_reason"],
            })
            eklenen += 1

    ortak.yaz(LISTE, liste)
    print("eklenen kayit %d - toplam %d" % (eklenen, len(liste["elenen"])))


if __name__ == "__main__":
    main()
