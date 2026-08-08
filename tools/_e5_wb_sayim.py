# -*- coding: utf-8 -*-
"""E5 / 5. calistirma - kelime bankali ozette tasarim olcumu.

Iki seyi olcer:

1) CELDIRICI ORTU: kelime bankasindaki her bos harf (dogru cevap olmayan
   harf) bir boslugun gercek rakibi mi, yoksa hicbir boslukla ilgisi olmayan
   dolgu mu. Once/sonra karsilastirmasi HEAD ile degil, asagidaki elle
   kurulmus eslemeyle yapilir; eslemenin kendisi rapora giriyor.

2) TANIM KALINTISI: duzeltilen bosluklarin tasiyici cumlesinde, cevabin
   tanimini veren eski ibarelerden biri hala duruyor mu.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

AC2 = "content/reading/tests/AC2/summary-completion.json"
AC3 = "content/reading/tests/AC3/summary-completion.json"
AC4 = "content/reading/tests/AC4/summary-completion.json"

# harf -> (once hangi boslugun rakibiydi, sonra hangi boslugun rakibi)
AC2_RAKIP = {
    "D": (37, 36),
    "E": (None, 37),
    "F": (None, 38),
    "G": (None, 39),
    "J": (None, 40),
}

# duzeltilen bosluk -> ozetten cikarilmasi gereken tanim ibareleri
TANIM_KALINTISI = {
    (AC2, 36): ["cause rather than mere association"],
    (AC2, 37): ["standard hours and fixed contracts turn into"],
    (AC2, 38): ["even in the most productive quarter"],
    (AC2, 39): ["stayed longest"],
    (AC2, 40): ["shared, unspoken sense of who knows what"],
    (AC3, 38): ["minute rods that support a cell from within",
                "23 nanometres"],
}


def main():
    veri = ortak.oku(AC2)
    dogru = {c for it in ortak.sorular(veri) for c in (it.get("answer") or [])}
    metin = {o["letter"]: o["text"] for o in veri["word_bank"]}

    print("== AC2 kelime bankasi: celdirici ortusu")
    once = sonra = 0
    for harf in sorted(AC2_RAKIP):
        if harf in dogru:
            raise SystemExit("rakip sayilan harf aslinda dogru cevap: %s" % harf)
        o, s = AC2_RAKIP[harf]
        once += 1 if o else 0
        sonra += 1 if s else 0
        print("   %s  %-22s  once: %-6s sonra: %s"
              % (harf, metin[harf], o or "-", s or "-"))
    print("   bir boslugun gercek rakibi olan celdirici: %d -> %d (5 uzerinden)"
          % (once, sonra))
    if sonra != 5:
        raise SystemExit("her celdirici bir boslukla eslesmeli")

    print("== tanim kalintisi taramasi")
    kalinti = 0
    for (yol, n), ibareler in sorted(TANIM_KALINTISI.items()):
        d = ortak.oku(yol)
        govde = d.get("stem_block") or ""
        for ib in ibareler:
            if ib in govde:
                print("   KALINTI: %s #%s -> %r" % (yol, n, ib))
                kalinti += 1
    print("   ozet govdesinde kalan tanim ibaresi: %d" % kalinti)
    if kalinti:
        raise SystemExit(1)

    print("== elenen yuvalar")
    d = ortak.oku(AC4)
    for it in ortak.sorular(d):
        if it.get("status") == "rejected":
            print("   %s #%s (%s)" % (AC4, it["number"], it["answer"]))


if __name__ == "__main__":
    main()
