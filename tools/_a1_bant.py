"""Bir PDF sayfasini ust uste binen yatay bantlara bolup PNG yapar.
El yazisi dokumunde satirlari yakindan okumak icin kullanilir.

Kullanim: python tools/_a1_bant.py <pdf> <sayfa> <y0> <y1> <bant> <dpi> <onek> [x0 x1]
  y0/y1 : sayfa yuksekliginin yuzdesi (0-1) olarak el yazisi bolgesi
  bant  : kac parcaya bolunecek (parcalar biraz ust uste biner)
  x0/x1 : istege bagli yatay sinir (varsayilan 0.08-0.92)
Cikti gitignore'daki dogrulama/ klasorune yazilir, depoya girmez.
"""
import sys, pathlib, string
import pymupdf

pdf, sayfa_no = sys.argv[1], int(sys.argv[2])
y0, y1 = float(sys.argv[3]), float(sys.argv[4])
bant, dpi, onek = int(sys.argv[5]), int(sys.argv[6]), sys.argv[7]
x0 = float(sys.argv[8]) if len(sys.argv) > 8 else 0.08
x1 = float(sys.argv[9]) if len(sys.argv) > 9 else 0.92

belge = pymupdf.open(pdf)
sayfa = belge[sayfa_no - 1]
r = sayfa.rect
yukseklik = (y1 - y0) / bant
bindirme = yukseklik * 0.06
for i in range(bant):
    ust = y0 + i * yukseklik - (bindirme if i else 0)
    alt = y0 + (i + 1) * yukseklik + (bindirme if i < bant - 1 else 0)
    kutu = pymupdf.Rect(r.x0 + x0 * r.width, r.y0 + ust * r.height,
                        r.x0 + x1 * r.width, r.y0 + alt * r.height)
    pix = sayfa.get_pixmap(dpi=dpi, clip=kutu)
    yol = pathlib.Path("dogrulama") / f"{onek}{string.ascii_lowercase[i]}.png"
    pix.save(yol)
    print(yol, pix.width, "x", pix.height)
