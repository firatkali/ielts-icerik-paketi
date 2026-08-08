"""Ayiklanan konusma dokumlerinin sayfa metniyle birebir ayni oldugunu dogrular.

Kullanim:  python tools/_konusma_dogrula.py

Her transkript satiri ve her yorum paragrafi ham sayfa metninde AYNEN var mi
diye bakar. Amac: ayiklama sirasinda aday hatalarinin sessizce duzeltilmedigini
gostermek. Tek satir bile eslesmezse hata verir.
"""

import glob
import json
import os
import re
import sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GIRDI = os.path.join(KOK, "referans", "konusma-band-ornekleri.txt")
DOSYALAR = os.path.join(KOK, "kalibrasyon", "ornekler", "konusma", "*.json")


def main():
    with open(GIRDI, encoding="utf-8") as f:
        ham = "\n".join(s.strip() for s in f.read().splitlines() if s.strip())

    hatali, satir_sayisi, dosya_sayisi = [], 0, 0
    for yol in sorted(glob.glob(DOSYALAR)):
        ad = os.path.basename(yol)
        dosya_sayisi += 1
        with open(yol, encoding="utf-8") as f:
            kayit = json.load(f)

        for satir in kayit["transcript"].split("\n"):
            icerik = re.sub(r"^(EXAMINER|CANDIDATE): ?", "", satir)
            if not icerik:
                continue
            satir_sayisi += 1
            if (": " + icerik) not in ham and ("\n" + icerik) not in ham:
                hatali.append((ad, icerik[:70]))

        for paragraf in kayit["examiner_comment"].split("\n\n"):
            if paragraf not in ham:
                hatali.append((ad, "YORUM: " + paragraf[:70]))

    print("Dosya: %d | denetlenen transkript satiri: %d" % (dosya_sayisi, satir_sayisi))
    print("Kaynakta birebir bulunamayan: %d" % len(hatali))
    for h in hatali[:20]:
        print("  -", h[0], "|", h[1])
    return 1 if hatali else 0


if __name__ == "__main__":
    sys.exit(main())
