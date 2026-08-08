"""E8 3. calistirma: K3 (anlam duzeyi) bayragini turlara SCRIPT yazar.

Neden script: K3 "kelime kelime tutturma degil, anlamca bilme" demek
(`OPUS5-E10` tanimi). 1. ve 2. calistirmada cevap harf oldugu icin K1 = K3'tu ve
soru cikmadi. Tamamlama ailesinde cikiyor: "luggage rack" / "overhead locker",
"charity" / "charity shop", "9" / "nine", "10 per cent" / "10%" ayni seyi
soyleyebilir. Bu karari olcumu yapan modelin vermesi icin CEVAP ANAHTARINI
gormesi gerekirdi — o da olcumu bitirirdi. Bu yuzden karari script veriyor:
anahtari yalniz o okuyor, disari SAYI basiyor, cevap degeri basmiyor.

Kural (bilerek dar tutuldu; genis eslesme sizintiyi oldugundan buyuk gosterir):
  - kucuk harf, noktalama/para birimi/bosluk sadelestirmesi
  - bas taki (a / an / the) atilir
  - yirmiye kadar sayi sozcugu <-> rakam, "half"->0.5, "per cent"->%
  - cogul -s atilir
  - biri digerinin SOZCUK duzeyinde alt dizisi ise anlamca ayni sayilir
    ("charity" ⊂ "charity shop"), ama tek harfli/bos artiklardan sonra en az
    bir anlamli sozcuk kalmalidir

Kullanim: python tools/_e8_anlam_esle.py <paket> [<paket> ...]
Yazar:    kalibrasyon/sessiz/<paket>-tur{1,2,3}.json dosyalarina "anlam" alani
"""

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

SAYI = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10",
    "eleven": "11", "twelve": "12", "thirteen": "13", "fourteen": "14",
    "fifteen": "15", "sixteen": "16", "seventeen": "17", "eighteen": "18",
    "nineteen": "19", "twenty": "20", "half": "0.5",
}
TAKI = {"a", "an", "the"}


def sozcukler(s):
    s = str(s).strip().lower()
    s = s.replace("per cent", "%").replace("percent", "%")
    s = s.replace("£", "").replace("$", "").replace(",", "")
    s = re.sub(r"[^\w%.'-]+", " ", s)
    out = []
    for w in s.split():
        w = w.strip(".'-")
        if not w or w in TAKI:
            continue
        w = SAYI.get(w, w)
        if len(w) > 3 and w.endswith("s") and not w.endswith("ss"):
            w = w[:-1]
        out.append(w)
    return out


def alt_dizi(kucuk, buyuk):
    n = len(kucuk)
    return any(buyuk[i:i + n] == kucuk for i in range(len(buyuk) - n + 1))


def anlamca_ayni(verilen, kayit):
    adaylar = [kayit.get("answer")] + list(kayit.get("accepted") or [])
    v = sozcukler(verilen if not isinstance(verilen, list) else " ".join(map(str, verilen)))
    if not v:
        return False
    for a in adaylar:
        if a is None:
            continue
        k = sozcukler(a if not isinstance(a, list) else " ".join(map(str, a)))
        if not k:
            continue
        if v == k or alt_dizi(v, k) or alt_dizi(k, v):
            return True
    return False


def anahtar_yukle():
    tablo = {}
    for p in ortak.soru_dosyalari():
        d = ortak.oku(p)
        if d.get("skill") != "listening":
            continue
        set_id = d.get("set_id", os.path.basename(p))
        for it in ortak.sorular(d):
            tablo["%s-%s" % (set_id, it.get("number"))] = {
                "answer": it.get("answer"),
                "accepted": it.get("accepted_variants") or [],
            }
    return tablo


def main():
    paketler = sys.argv[1:]
    if not paketler:
        print("Kullanim: python tools/_e8_anlam_esle.py <paket> [...]")
        return 2
    anahtar = anahtar_yukle()
    for paket in paketler:
        ek = 0
        for tur in (1, 2, 3):
            gy = "kalibrasyon/sessiz/%s-tur%d.json" % (paket, tur)
            d = ortak.oku(gy)
            for a in d.get("answers", []):
                k = anahtar.get(a.get("id"))
                if k is None:
                    continue
                a["anlam"] = anlamca_ayni(a.get("answer"), k)
                ek += 1 if a["anlam"] else 0
            ortak.yaz(gy, d)
        print("%s: uc turda toplam %d anlam-esleme" % (paket, ek))
    return 0


if __name__ == "__main__":
    sys.exit(main())
