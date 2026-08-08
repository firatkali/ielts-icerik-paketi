"""OPUS5-E9: GT 'example responses' belgesindeki 2 cevabin zaten dokulmus
GT ornekleriyle ayni script olup olmadigini dogrular (yineleme kontrolu).

Metin ekrana yazdirilmaz; yalnizca ortusme orani basilir.

Kullanim: python tools/_e9_yinelenen_kontrol.py
"""
import json
import pathlib
import re

import fitz

PDF = pathlib.Path(
    "referans/ielts-general-training-writing-example-responses-to-parts-1-and-2-"
    "with-band-scores-and-examiner-comments.pdf"
)


def sadelestir(s):
    return re.sub(r"[^a-z0-9 ]", "", s.lower())


def kirp(sayfa_metni):
    """Aday cevabini 'Examiner comment' oncesinde keser, basligi atar."""
    govde = sayfa_metni.split("Examiner comment")[0]
    satir = [s for s in govde.splitlines() if s.strip()]
    return " ".join(satir[2:])  # ilk iki satir: gorev basligi + 'Sample Script A'


d = fitz.open(PDF)
adaylar = {"GT-T1-1A-A": kirp(d[1].get_text()), "GT-T2-2A-A": kirp(d[2].get_text())}

for kod, pdf_metin in adaylar.items():
    yol = pathlib.Path(f"kalibrasyon/ornekler/yazma/{kod}.json")
    dosya = json.loads(yol.read_text(encoding="utf-8"))
    a = set(sadelestir(pdf_metin).split())
    b = set(sadelestir(dosya["response_text"]).split())
    ortak = len(a & b) / max(len(a | b), 1)
    print(f"{kod}: band dosya={dosya['band']} | kelime kumesi ortusmesi = {ortak:.0%}"
          f" | pdf {len(a)} farkli kelime, dosya {len(b)}")
