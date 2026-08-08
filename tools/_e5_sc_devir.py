# -*- coding: utf-8 -*-
"""E5 / 7. calistirma - E6 devir dosyasina elenen yuvalari ekler.

`content/DOGRULAMA/yeniden-uretim-listesi.json` uzerine yazmaz, ekler.
Ayni (dosya, numara) ikilisi zaten varsa atlanir; betik idempotenttir.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402
import _e5_sc_elden_gecir as EG  # noqa: E402

LISTE = "content/DOGRULAMA/yeniden-uretim-listesi.json"


def main():
    liste = ortak.oku(LISTE)
    var = {(k["dosya"], k["numara"]) for k in liste["elenen"]}
    eklenen = 0

    for (yol, numara) in sorted(EG.ELE, key=lambda k: (k[0], k[1])):
        if (yol, numara) in var:
            continue
        veri = ortak.oku(yol)
        tip = veri.get("question_type")
        kayit = None
        for g, it in ortak.kumeli_sorular(veri):
            if it["number"] != numara:
                continue
            kayit = {
                "dosya": yol,
                "numara": numara,
                "tip": tip,
                "pasaj": it.get("passage_id") or g.get("passage_id")
                         or veri.get("passage_id")
                         or EG.ELE[(yol, numara)]["pasaj"],
                "kacinilacak": {
                    "kanit_cumlesi": it.get("evidence"),
                    "ifade": it.get("prompt"),
                },
                "neden_elendi": EG.ELE[(yol, numara)]["reject_reason"],
            }
        if kayit is None:
            raise SystemExit("soru bulunamadi: %s #%s" % (yol, numara))
        liste["elenen"].append(kayit)
        eklenen += 1

    ortak.yaz(LISTE, liste)
    print("eklenen kayit %d - toplam %d" % (eklenen, len(liste["elenen"])))


if __name__ == "__main__":
    main()
