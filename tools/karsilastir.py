"""Capraz dogrulama 3. adim: kor cevaplari orijinal anahtarla karsilastirir.

Kullanim:  python tools/karsilastir.py <rapor-adi>
Ornek:     python tools/karsilastir.py true-false-not-given

Okur:  dogrulama/cevap/*.json
Yazar: content/DOGRULAMA/<rapor-adi>.json
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

import datetime
import glob
import json


def normal(a):
    if a is None:
        return []
    if not isinstance(a, list):
        a = [a]
    return sorted(str(x).strip().lower() for x in a)


def main():
    if len(sys.argv) < 2:
        print("Kullanim: python tools/karsilastir.py <rapor-adi>")
        return 2
    rapor_adi = sys.argv[1]

    cevap_dizin = ortak.yol("dogrulama", "cevap")
    cevaplar = sorted(glob.glob(os.path.join(cevap_dizin, "*.json")))
    if not cevaplar:
        print("HATA: dogrulama/cevap/ bos. Once kor dosyalari cozup buraya yaz.")
        return 1

    sonuclar = []
    for cev_yol in cevaplar:
        with open(cev_yol, encoding="utf-8") as f:
            c = json.load(f)
        src = c.get("_source")
        if not src or not os.path.exists(ortak.yol(src)):
            sonuclar.append({"file": src, "hata": "kaynak dosya bulunamadi"})
            continue
        orig = ortak.oku(src)
        anahtar = {str(it.get("number")): it for it in ortak.sorular(orig)}

        uyusan, uyusmayan, detay = 0, 0, []
        for a in c.get("answers", []):
            n = str(a.get("number"))
            it = anahtar.get(n)
            if it is None:
                uyusmayan += 1
                detay.append({"number": n, "durum": "orijinalde yok"})
                continue
            ayni = normal(a.get("answer")) == normal(it.get("answer"))
            guven = a.get("confidence", 5)
            if ayni and guven >= 3:
                uyusan += 1
            else:
                uyusmayan += 1
                detay.append({
                    "number": n,
                    "dogrulayici": a.get("answer"),
                    "orijinal": it.get("answer"),
                    "confidence": guven,
                    "gerekce": a.get("reasoning", ""),
                    "durum": "uyusmadi" if not ayni else "dusuk_guven",
                })
        sonuclar.append({"file": src, "toplam": uyusan + uyusmayan,
                         "uyusan": uyusan, "uyusmayan": uyusmayan, "detay": detay})

    cikti = "content/DOGRULAMA/%s.json" % rapor_adi
    ortak.yaz(cikti, {"tarih": datetime.date.today().isoformat(),
                      "rapor": rapor_adi, "sonuclar": sonuclar})

    t = sum(r.get("toplam", 0) for r in sonuclar)
    u = sum(r.get("uyusmayan", 0) for r in sonuclar)
    oran = (t - u) / t * 100 if t else 0
    print("Toplam %d soru | uyusan %d | sorunlu %d | uyusma orani %.1f%%"
          % (t, t - u, u, oran))
    if oran < 85 and t:
        print("!!! UYARI: uyusma orani %85'in altinda - sistematik sorun olabilir.")
    print("Rapor:", cikti)

    print("\nIsaretlenmesi gereken sorular:")
    for r in sonuclar:
        for d in r.get("detay", []):
            print("  %s  soru %s  orijinal=%s  dogrulayici=%s  (%s)"
                  % (r["file"], d.get("number"), d.get("orijinal"),
                     d.get("dogrulayici"), d.get("durum")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
