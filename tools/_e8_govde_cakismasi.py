"""E8 3. calistirma tanisi: sessiz kopyada cevap dizgisi HANGI ALANDA gecti.

`_e8_sizinti_kontrol.py` "govdede birebir gecen cevap dizgisi: N" uyarisi
veriyor ama nerede oldugunu soylemiyor. Uyari iki cok farkli seyi ayni torbaya
koyuyor:

  (a) kopya kusuru  — senaryo/cevap izi silinmemis, alan kopyaya sizmis;
  (b) icerik gercegi — cevap sozcugu sorunun kendi govdesinde (tablo basligi,
      not iskeleti, baska bir maddenin metni) zaten geciyor. Bu durumda kagida
      bakan adayin da gordugu bir sey; olcumden cikarilmaz, ama isaretlenir.

🔴 3. calistirmanin acik dersi: ALAN YOLUNU BASMAK BILE FAZLA. "soru 34 ->
.blocks[0].stem_block" cikti, cevabin o 726 karakterlik iskelette birebir gectigi
anlamina geliyor; iskeletteki sozcuk sayisi az oldugu icin bu, cevabi olcumu
yapan model icin fiilen daralttiu. Uc kalem (L1 not 34-35, L2 tablo 5) bu yuzden
`haric: true` ile olcum disi birakildi.

Bu yuzden ayrinti artik STDOUT'a degil `dogrulama/sessiz-tani.txt` dosyasina
yazilir (gitignore'da). Ekrana yalniz SAYI gelir. Olcumu yapan model o dosyayi
ACMAMALI; dosya, olcum bittikten sonra bakacak insan/sonraki adim icindir.

Kullanim: python tools/_e8_govde_cakismasi.py
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402


def yollar(o, yol=""):
    """(yol, dizgi) ciftleri uretir."""
    if isinstance(o, dict):
        for k, v in o.items():
            yield from yollar(v, "%s.%s" % (yol, k))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from yollar(v, "%s[%d]" % (yol, i))
    elif isinstance(o, str):
        yield yol, o


def main():
    kok = ortak.yol("dogrulama", "sessiz")
    if not os.path.isdir(kok):
        print("dogrulama/sessiz yok.")
        return 1

    tani = ortak.yol("dogrulama", "sessiz-tani.txt")
    satirlar = []
    toplam = 0
    for ad in sorted(os.listdir(kok)):
        with open(os.path.join(kok, ad), encoding="utf-8") as f:
            k = json.load(f)
        kaynak = ortak.oku(k["_source"])
        # cevap -> hangi soru numarasina ait (numara basilabilir, deger degil)
        cevaplar = []
        for it in ortak.sorular(kaynak):
            a = it.get("answer")
            for c in (a if isinstance(a, list) else [a]):
                if isinstance(c, str) and len(c) > 3:
                    cevaplar.append((it.get("number"), c.strip().lower()))
        if not cevaplar:
            continue
        for yol, dizgi in yollar(k):
            d = dizgi.lower()
            for numara, c in cevaplar:
                if c in d:
                    satirlar.append("%s soru %s -> alan %s (alan uzunlugu %d karakter)"
                                    % (ad, numara, yol, len(dizgi)))
                    toplam += 1

    with open(tani, "w", encoding="utf-8") as f:
        f.write("\n".join(satirlar) + "\n")
    print("toplam cakisma: %d — ayrinti dogrulama/sessiz-tani.txt (olcumu yapan "
          "model bu dosyayi acmamali)" % toplam)
    return 0


if __name__ == "__main__":
    sys.exit(main())
