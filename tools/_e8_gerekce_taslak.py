"""E8 5. adim yardimcisi: isaretlenecek kalemlerin SESSIZ kopyadaki govdesini basar.

Kullanim: python tools/_e8_gerekce_taslak.py <paket-adi> [<paket-adi> ...]

5. calistirmada her isaretli soruya "bu soruya ozel somut sebep" yazilmasi
gerekiyor (E1'in dersi: tek tip cumle yazma). Sebebi yazabilmek icin sorunun
kendisi lazim -- ama SENARYO VE CEVAP ANAHTARI DEGIL. Bu script yalnizca
`dogrulama/sessiz/` altindaki kor kopyayi okur; orada senaryo izi ve cevap
zaten silinmistir (`tools/sessiz-kopya.py`). Orijinal soru dosyalarina,
`content/listening/scripts/` altina ve cevap anahtarina dokunmaz.

Onceki turlarin kaydettigi `basis` + (varsa) `gerekce` alanini da yanina yazar.
"""

import collections
import glob
import io
import json
import os
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402
import importlib

toplu = importlib.import_module("_e8_toplu")


def kopya_kalemleri():
    """id -> (soru sozlugu, dosyanin blok govdesi)."""
    out = {}
    for f in sorted(glob.glob(ortak.yol("dogrulama", "sessiz", "*.json"))):
        with open(f, encoding="utf-8") as fh:
            d = json.load(fh)
        for it in d["items"]:
            out[it["id"]] = (it["question"], d.get("blocks"), d["_source"])
    return out


def turda_verilen(paket):
    """Kalemin 1. turda VERILEN cevabi.

    Isaretlenen kalemler 3/3 dogru bilinenlerdir; dolayisiyla turda verilen cevap
    zaten dogru cevaptir. Cevap anahtari dosyasi acilmaz.
    """
    yol = ortak.yol("kalibrasyon", "sessiz", "%s-tur1.json" % paket)
    with open(yol, encoding="utf-8") as f:
        return {a["id"]: a.get("answer") for a in json.load(f)["answers"]}


def gerekceler(paket):
    out = collections.defaultdict(list)
    for n in (1, 2, 3):
        yol = ortak.yol("kalibrasyon", "sessiz", "%s-tur%d.json" % (paket, n))
        if not os.path.exists(yol):
            continue
        with open(yol, encoding="utf-8") as f:
            for a in json.load(f)["answers"]:
                if a.get("gerekce"):
                    out[a["id"]].append(a["gerekce"])
    return out


def main():
    istenen = set(sys.argv[1:])
    kopya = kopya_kalemleri()
    _, isaret = toplu.topla()
    ger, verilen = {}, {}
    for p in {p for _, _, p in isaret}:
        ger[p] = gerekceler(p)
        verilen[p] = turda_verilen(p)

    n = 0
    for kid, basis, paket in isaret:
        if istenen and paket not in istenen:
            continue
        n += 1
        soru, bloklar, kaynak = kopya.get(kid, ({}, None, "?"))
        print("=" * 70)
        print("%s  [%s]  %s" % (kid, basis, kaynak))
        print("  3/3 verilen cevap: %s"
              % json.dumps(verilen[paket].get(kid), ensure_ascii=False))
        for g in ger.get(paket, {}).get(kid, [])[:1]:
            print("  onceki gerekce: %s" % g)
        print("  soru: %s" % json.dumps(soru, ensure_ascii=False))
    print("=" * 70)
    print("%d kalem" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
