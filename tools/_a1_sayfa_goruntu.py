"""PDF sayfalarini PNG'ye cevirir (el yazisi dokumu icin).
Cikti gitignore'daki dogrulama/ klasorune yazilir, depoya girmez.

Kullanim: python tools/_a1_sayfa_goruntu.py <pdf> <ilk> <son> <dpi> <onek>
"""
import sys, pathlib
import pymupdf

pdf, ilk, son, dpi, onek = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
hedef = pathlib.Path("dogrulama")
hedef.mkdir(exist_ok=True)
belge = pymupdf.open(pdf)
for no in range(ilk, son + 1):
    sayfa = belge[no - 1]
    pix = sayfa.get_pixmap(dpi=dpi)
    yol = hedef / f"{onek}-s{no:02d}.png"
    pix.save(yol)
    print(yol, pix.width, "x", pix.height)
