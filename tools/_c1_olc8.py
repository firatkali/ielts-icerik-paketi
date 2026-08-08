# -*- coding: utf-8 -*-
"""8. grup uretim yardimcisi: metinlerin kelime sayisi ve suresini olcer.

Uretim script'i (`_c1_uret8.py`) sureyi 90-120 saniye penceresine zorluyor; bu
yardimci hangi metnin pencereye girmedigini ve hedef kelime araligini gosteriyor.
Ciktisi KONTROL.md'ye yazilan olcum tablosunun kaynagi.
"""
import re
import os

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HIZ = {"5": 80, "65": 105, "8": 127}

src = open(os.path.join(KOK, "tools", "_c1_uret8.py"), encoding="utf-8").read()
for ad in re.findall(r"^(C\d\d_\d+) = ", src, re.M):
    govde = re.search(ad + r' = """(.*?)"""', src, re.S).group(1)
    n = len(govde.split())
    wpm = HIZ[ad.split("_")[1]]
    sn = int(round(n / float(wpm) * 60 / 5.0) * 5)
    alt = int(90 * wpm / 60.0) + 1
    ust = int(120 * wpm / 60.0)
    durum = "OK" if 90 <= sn <= 120 else "DISARIDA"
    print("%-8s %4d kelime  %4d sn  hedef %d-%d kelime  %s" % (ad, n, sn, alt, ust, durum))
