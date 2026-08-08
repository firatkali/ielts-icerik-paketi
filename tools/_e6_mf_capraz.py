# -*- coding: utf-8 -*-
"""OPUS5-E6 5. calistirma: yeni kanit cumleleri baska sorularda kullaniliyor mu?

Yeniden uretimde secilen kanit cumlelerinin depoda baska bir soruya capa olup
olmadigini kontrol eder (ayni cumleden iki soru cikmasin).
Kullanim: python tools/_e6_mf_capraz.py
"""
import glob
import io
import os
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PARCA = [
    ("A10 D/3", "despite its popularity in contemporary office trends"),
    ("A10 B/1", "sound-absorbing panels"),
    ("A02 D/2", "seventy-six per cent"),
    ("A05 E/1", "originally been classified"),
    ("A05 F/2", "spelt-like wheat"),
    ("A05 B/2", "under the microscope"),
    ("A05 G/3", "may have emerged sooner"),
    ("A11 E/4", "four-item Subjective Vitality"),
]


def main():
    desen = os.path.join(KOK, "content", "reading", "**", "*.json")
    for f in sorted(glob.glob(desen, recursive=True)):
        s = open(f, encoding="utf-8").read()
        bulunan = [ad for ad, p in PARCA if p in s]
        if bulunan:
            print(os.path.relpath(f, KOK), bulunan)


if __name__ == "__main__":
    main()
