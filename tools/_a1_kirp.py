"""Bir PDF sayfasinin belirli bir dikdortgenini yuksek cozunurlukte PNG yapar.
Kirpma orani sayfa boyutunun yuzdesi olarak verilir (0-1 arasi).

Kullanim: python tools/_a1_kirp.py <pdf> <sayfa> <x0> <y0> <x1> <y1> <dpi> <ad>
"""
import sys, pathlib
import pymupdf

pdf, sayfa_no = sys.argv[1], int(sys.argv[2])
x0, y0, x1, y1 = (float(v) for v in sys.argv[3:7])
dpi, ad = int(sys.argv[7]), sys.argv[8]

belge = pymupdf.open(pdf)
sayfa = belge[sayfa_no - 1]
r = sayfa.rect
kutu = pymupdf.Rect(r.x0 + x0 * r.width, r.y0 + y0 * r.height,
                    r.x0 + x1 * r.width, r.y0 + y1 * r.height)
pix = sayfa.get_pixmap(dpi=dpi, clip=kutu)
yol = pathlib.Path("dogrulama") / (ad + ".png")
pix.save(yol)
print(yol, pix.width, "x", pix.height)
