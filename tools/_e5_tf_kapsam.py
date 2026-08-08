# -*- coding: utf-8 -*-
"""E5 / 6. calistirma - kapsam sayimi (salt okur, hicbir sey yazmaz).

Kapsam iki kumenin birlesimi:
  a) true_false_not_given tipindeki butun isaretli sorular
  b) "kalan tekiller" - hicbir calistirma maddesinin talep etmedigi,
     dagilmis tek tuk isaretli sorular: matching_headings,
     matching_information, matching_features ve yes_no_not_given
     artiklariyla tamamlama ailesindeki `belirsiz` mekanizmali tekler.

7. ve 8. calistirmalarin kapsami (E10 kokenli cumle tamamlama / kisa cevap
ve ozet ailesi) ile 4. calistirmadan bilincli olarak flagged birakilan
E10 not/tablo/akis sorulari kapsam disidir; betik onlari ayrica sayar.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

TEKIL_TIP = ("matching_headings", "matching_information",
             "matching_features", "yes_no_not_given")


def main():
    tfng = []
    tekil = []
    disarida = []

    for p in ortak.soru_dosyalari():
        d = ortak.oku(p)
        tip = d.get("question_type")
        for it in ortak.sorular(d):
            if it.get("status") != "flagged":
                continue
            e10 = "blind_solvable_kelime_duzeyi" in it
            kayit = (p, it["number"], tip, it.get("flag_mechanism"),
                     "E10" if e10 else "E1")
            if tip == "true_false_not_given":
                tfng.append(kayit)
            elif tip in TEKIL_TIP:
                tekil.append(kayit)
            elif not e10 and it.get("flag_mechanism") == "belirsiz":
                tekil.append(kayit)
            else:
                disarida.append(kayit)

    print("== a) true_false_not_given")
    for k in tfng:
        print("   %-52s %2s  %-16s %s" % (k[0].split("content/")[-1], k[1], k[3], k[4]))
    print("   ara toplam: %d" % len(tfng))

    print("== b) kalan tekiller")
    for k in sorted(tekil):
        print("   %-52s %2s  %-22s %-16s %s"
              % (k[0].split("content/")[-1], k[1], k[2], k[3], k[4]))
    print("   ara toplam: %d" % len(tekil))

    print("== 6. calistirmanin kapsami: %d soru" % (len(tfng) + len(tekil)))

    print("== kapsam disi (7. / 8. calistirma ve 4.'nun bilincli birakilanlari): %d"
          % len(disarida))
    sayim = {}
    for k in disarida:
        sayim[(k[2], k[4])] = sayim.get((k[2], k[4]), 0) + 1
    for k in sorted(sayim):
        print("   %-28s %-4s %3d" % (k[0], k[1], sayim[k]))


if __name__ == "__main__":
    main()
