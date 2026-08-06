"""Yazma ornek gorevleri PDF'inin metin katmanini duz metin olarak cikarir.

Not: `pdftotext` bu belgede gomulu font yuzunden bozuk cikti veriyor
(harfler kayiyor, bosluklar dusuyor). PyMuPDF ayni sayfalari dogru
cozuyor; gorev metni, sinav gorevlisi yorumu ve band puani buradan alinir.
El yazisi cevaplar metin katmaninda yok, onlar sayfa goruntusunden okunur.

Kullanim: python tools/_a1_metin_coz.py <pdf> <ilk> <son> [cikti]
Cikti verilmezse ekrana yazar. Telifli metin depoya yazilmaz.
"""
import sys
import pymupdf


def main():
    pdf, ilk, son = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    belge = pymupdf.open(pdf)
    parcalar = []
    for no in range(ilk, son + 1):
        parcalar.append(f"===== SAYFA {no} =====")
        parcalar.append(belge[no - 1].get_text("text"))
    cikti = "\n".join(parcalar)
    if len(sys.argv) > 4:
        with open(sys.argv[4], "w", encoding="utf-8") as f:
            f.write(cikti)
        print(sys.argv[4], len(cikti))
    else:
        print(cikti)


if __name__ == "__main__":
    main()
