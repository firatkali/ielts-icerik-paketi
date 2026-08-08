# -*- coding: utf-8 -*-
"""E8 5. adim: dinleme sizinti olcumunun sonucunu orijinal soru dosyalarina isler.

Kullanim: python tools/_e8_isaretle.py [--kuru]

`tools/_b1_isaretle.py`nin dinleme surumudur; ONUN YERINI ALMAZ ve okuma
dosyalarina dokunmaz (`skill != "listening"` olan dosya atlanir).

Yazdiklari (yalniz olculen 10 pakette):
  3/3 bilinen + dayanagi anlamsal  -> blind_solvable, blind_basis, status=flagged,
                                      flag_reason (SORUYA OZEL), flag_mechanism
  3/3 bilinen + dayanagi sansa acik -> blind_solvable=true + blind_note, status ayni
  geri kalan                        -> blind_solvable=false
  olcum disi birakilan 3 kalem      -> yalniz blind_note

HICBIR SORU SILINMEZ, hicbir sorunun metni/cevabi degistirilmez.
`plan-map-diagram-labelling` hic islenmez: gorsel gerektirir, metin tabanli
olcum orada kordur (okuma tarafindaki diyagram etiketleme kararinin aynisi).
"""

import collections
import importlib
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
import ortak  # noqa: E402

toplu = importlib.import_module("_e8_toplu")
tablo = importlib.import_module("_e8_isaret_tablosu")

# Olculen paketler -> dosya adlari. `multiple-choice` iki olcume birden girdi
# (tek + cok cevapli), bu yuzden dayanak tablosu iki paketten birlestirilir.
DOSYA_PAKET = {
    "multiple-choice": ("multiple-choice-tek", "multiple-choice-cok"),
    "multiple-choice-multi": ("multiple-choice-cok",),
    "matching": ("matching",),
    "form-completion": ("form-completion",),
    "note-completion": ("note-completion",),
    "table-completion": ("table-completion",),
    "sentence-completion": ("sentence-completion",),
    "summary-completion": ("summary-completion",),
    "flow-chart-completion": ("flow-chart-completion",),
    "short-answer": ("short-answer",),
}

ONEK = "Senaryo gösterilmeden 3/3 turda doğru bilindi: "


def main():
    kuru = "--kuru" in sys.argv

    dayanak = {}
    for p in {x for grup in DOSYA_PAKET.values() for x in grup}:
        dayanak.update(toplu.baskin_dayanak(p))

    say = collections.Counter()
    mekanizma = collections.Counter()
    eksik = []
    islenen_id = set()

    for dosya_adi in sorted(DOSYA_PAKET):
        for p in ortak.bul("content/**/%s.json" % dosya_adi):
            if "/DOGRULAMA/" in p or "/scripts/" in p:
                continue
            d = ortak.oku(p)
            if d.get("skill") != "listening":
                continue
            set_id = d.get("set_id", os.path.basename(p))
            degisti = False
            for it in ortak.sorular(d):
                kid = "%s-%s" % (set_id, it.get("number"))
                islenen_id.add(kid)
                if kid in tablo.OLCUM_DISI:
                    it["blind_note"] = tablo.OLCUM_DISI_NOT
                    say["olcum_disi"] += 1
                elif kid in tablo.TABLO:
                    mek, sebep = tablo.TABLO[kid]
                    it["blind_solvable"] = True
                    it["blind_basis"] = dayanak.get(kid, "bilinmiyor")
                    it["status"] = "flagged"
                    it["flag_reason"] = ONEK + sebep + "."
                    it["flag_mechanism"] = mek
                    mekanizma[mek] += 1
                    say["isaretli"] += 1
                elif kid in tablo.SANSLI:
                    it["blind_solvable"] = True
                    it["blind_basis"] = dayanak.get(kid, "bilinmiyor")
                    it["blind_note"] = tablo.SANSLI_NOT
                    say["sansli"] += 1
                else:
                    it["blind_solvable"] = False
                    say["duz"] += 1
                degisti = True
            if degisti and not kuru:
                ortak.yaz(p, d)
            print("  %s: %s" % ("okundu" if kuru else "islendi", p))

    for kid in sorted(set(tablo.TABLO) | tablo.SANSLI | tablo.OLCUM_DISI):
        if kid not in islenen_id:
            eksik.append(kid)

    print("\nisaretli (flagged) : %d" % say["isaretli"])
    print("sansa acik, isaretlenmedi : %d" % say["sansli"])
    print("olcum disi (yalniz not) : %d" % say["olcum_disi"])
    print("blind_solvable=false : %d" % say["duz"])
    print("toplam islenen kalem : %d" % sum(say.values()))
    print("\nmekanizma dagilimi:")
    for m, n in mekanizma.most_common():
        print("  %-16s %d" % (m, n))
    if eksik:
        print("\nUYARI: tabloda olup dosyada bulunamayan kimlik: %s" % eksik)
        return 1
    if kuru:
        print("\n(--kuru: hicbir dosya yazilmadi)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
