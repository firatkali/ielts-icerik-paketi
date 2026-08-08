"""E8: sessiz kopyada yasakli alan kalmis mi + cevap dizgisi sizmis mi.

Kopyayi model okuyacak; once bu kontrol gecmeli. Cikti yalniz SAYI ve alan adi,
cevap degeri basilmaz.

🔴 "govdede birebir gecen cevap dizgisi: N" uyarisi bir ARASTIRMA isaretidir,
agir hata degil: cevap sozcugu sorunun kendi govdesinde de geciyor olabilir
(tablo basligi, not iskeletinin baska bir satiri) — kagida bakan aday da ayni
seyi gorur. Uyarinin NEREDE oldugunu `tools/_e8_govde_cakismasi.py` soyler ve
ayrintiyi bilerek dosyaya yazar: 3. calistirmada alan yolunu ekrana basmak,
cevabi olcumu yapan model icin daraltti ve uc kalem olcum disi kalmak zorunda
kaldi. Olcum turlarini yapan model bu ayrintiyi gormemeli.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

sessiz = __import__("sessiz-kopya".replace("-", "_")) if False else None
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util  # noqa: E402
spec = importlib.util.spec_from_file_location(
    "sessiz_kopya", os.path.join(os.path.dirname(os.path.abspath(__file__)), "sessiz-kopya.py"))
sk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sk)


def alanlar(o, out):
    if isinstance(o, dict):
        for k, v in o.items():
            out.add(k)
            alanlar(v, out)
    elif isinstance(o, list):
        for v in o:
            alanlar(v, out)


def dizgiler(o, out):
    if isinstance(o, dict):
        for v in o.values():
            dizgiler(v, out)
    elif isinstance(o, list):
        for v in o:
            dizgiler(v, out)
    elif isinstance(o, str):
        out.append(o)


def main():
    kok = ortak.yol("dogrulama", "sessiz")
    if not os.path.isdir(kok):
        print("dogrulama/sessiz yok."); return 1

    # 1) yasakli alan kalmis mi
    hata = 0
    for ad in sorted(os.listdir(kok)):
        with open(os.path.join(kok, ad), encoding="utf-8") as f:
            k = json.load(f)
        bulunan = set()
        alanlar(k, bulunan)
        kacak = sorted(bulunan & sk.SIL)
        if kacak:
            print("SIZINTI ALANI %s: %s" % (ad, kacak)); hata += 1

        # 2) kopyadaki dizgilerde gercek cevap birebir geciyor mu
        kaynak = ortak.oku(k["_source"])
        cevaplar = []
        for it in ortak.sorular(kaynak):
            for c in ([it.get("answer")] if not isinstance(it.get("answer"), list)
                      else it["answer"]):
                if isinstance(c, str) and len(c) > 3:
                    cevaplar.append(c.strip().lower())
        metin = []
        dizgiler(k, metin)
        govde = " \n ".join(metin).lower()
        # Coktan secmelide cevap zaten seceneklerin biri; oradaki gecis normal.
        if k.get("_question_type") not in ("multiple_choice", "multiple_choice_multi",
                                           "matching", "matching_features",
                                           "matching_information"):
            gecen = sum(1 for c in set(cevaplar) if c in govde)
            if gecen:
                print("UYARI %s: govdede birebir gecen cevap dizgisi: %d" % (ad, gecen))

    # 3) senaryo metninden herhangi bir cumle kopyaya girmis mi
    for ad in sorted(os.listdir(kok)):
        with open(os.path.join(kok, ad), encoding="utf-8") as f:
            k = json.load(f)
        kaynak = ortak.oku(k["_source"])
        sid = kaynak.get("script_id") or ""
        metin = []
        dizgiler(k, metin)
        if sid and any(sid in m for m in metin):
            print("SIZINTI script_id %s" % ad); hata += 1

    print("kontrol bitti, %d dosya, %d agir hata" % (len(os.listdir(kok)), hata))
    return 1 if hata else 0


if __name__ == "__main__":
    sys.exit(main())
