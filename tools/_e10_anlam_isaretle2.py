"""E10 2. calistirma: ozet ailesini (summary-completion, hem kelime bankali hem
metinden-kelime alt tipi) ANLAM duzeyinde yeniden degerlendirir ve bulgulari
orijinal soru dosyalarina isler.

Kullanim: python tools/_e10_anlam_isaretle2.py

B1 olcumu "cevap 3/3 turda KELIMESI KELIMESINE tuttu mu" diye bakiyordu. Bu adim
ayni uc tur dokumune anlam duzeyinde bakiyor: es anlamli kelime, farkli cekim ya
da ayni seyi gosteren farkli yuzey ifadesi de "biliniyor" sayiliyor.

HICBIR SORU SILINMEZ. Eski kelime-duzeyi bulgusu da silinmez: uzerine yazmak
yerine blind_solvable_kelime_duzeyi alaninda saklanir (ikisi farkli sey olcuyor).
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

SEBEP = ("Parça gösterilmeden anlamca 3/3 turda doğru bilindi: farklı kelimeyle "
         "ama doğru kavramla cevaplandı (%s).")

# (set_id, soru no) -> gerekcedeki somut karsilastirma
# Karar kurali 1. calistirmadaki ile ayni: modelin cevabi gercek cevapla AYNI
# SEYE isaret ediyorsa anlamca dogru. Niteleyici dusup gonderge ayni kaliyorsa
# ayni sey; gonderge daralip/degisiyorsa ya da sayi/isim tutmuyorsa degil.
BULGULAR = {
    ("practice-summary-completion", 3):
        "'threshold / limit / threshold' verdi, gerçek cevap 'safe limits' — "
        "aşılan eşik ile önerilen güvenli sınır aynı gönderge",
    ("practice-summary-completion", 4):
        "'developers / programmers / developers' verdi, gerçek cevap 'software "
        "engineers' — kod yazan aynı meslek grubu",
    ("practice-summary-completion", 6):
        "'crossover / within-subject / crossover' verdi; within-subject, her "
        "gönüllünün kendi karşılaştırması olduğu crossover düzeninin adı",
    ("practice-summary-completion", 8):
        "'stressful / draining / stressful' verdi, gerçek cevap 'draining' — "
        "kampüs koşulunun hafifçe yıpratıcı olduğu aynı iddia",
    ("practice-summary-completion", 11):
        "3 turda da 'shells' verdi, gerçek cevap 'eggshells' — mutfak artığı "
        "listesinde aynı gönderge",
    ("practice-summary-completion", 12):
        "'double / twice / double' verdi; twice, double'ın eş anlamlısı",
    ("practice-summary-completion", 14):
        "'mortality / death / mortality' verdi; death, mortality'nin eş "
        "anlamlısı",
    ("AC1-summary-completion", 37):
        "'dye / stains / dye' verdi; boyama maddesi olarak stain ile dye aynı "
        "şeyi adlandırıyor",
    ("AC1-summary-completion", 40):
        "3 turda da 'warning' verdi, gerçek cevap 'warning system' — 'early "
        "warning' aynı göndergenin yerleşik kalıbı",
    ("AC3-summary-completion", 36):
        "3 turda da 'decay' verdi, gerçek cevap 'decomposition' — eş anlamlı",
    ("AC3-summary-completion", 37):
        "3 turda da 'databases' verdi, gerçek cevap 'reference databases'",
    ("AC3-summary-completion", 40):
        "3 turda da 'conditions' verdi, gerçek cevap 'thermal conditions'; "
        "cümlenin kendi açıklaması ('ani ısı, hemen ardından soğuma') aynı "
        "göndergeyi veriyor",
    ("GT1-summary-completion", 37):
        "3 turda da 'peel' verdi, gerçek cevap 'peelings' — aynı kelimenin "
        "başka biçimi",
    ("GT1-summary-completion", 38):
        "3 turda da 'fridge' verdi, gerçek cevap 'refrigerator' — aynı nesnenin "
        "günlük dildeki adı",
}


def main():
    yollar = [p for p in ortak.bul("content/**/summary-completion.json")
              if "/DOGRULAMA/" not in p]

    isaretli = []
    for p in yollar:
        d = ortak.oku(p)
        if d.get("skill") != "reading":
            continue
        set_id = d.get("set_id", os.path.basename(p))
        degisti = False
        for it in ortak.sorular(d):
            anahtar = (set_id, it.get("number"))
            if anahtar not in BULGULAR:
                continue
            if it.get("blind_solvable") is True:
                print("  zaten isaretli, atlandi: %s-%s" % anahtar)
                continue
            # Eski kelime-duzeyi bulgusu silinmiyor, sadece tasiniyor.
            it["blind_solvable_kelime_duzeyi"] = it.get("blind_solvable", False)
            it["blind_solvable"] = True
            it["blind_basis"] = "logic"
            it["status"] = "flagged"
            it["flag_reason"] = SEBEP % BULGULAR[anahtar]
            it["flag_mechanism"] = "esdizim_kilidi"
            isaretli.append("%s-%s" % anahtar)
            degisti = True
        if degisti:
            ortak.yaz(p, d)
            print("  islendi: %s" % p)

    print("\n%d soru anlam duzeyinde isaretlendi." % len(isaretli))
    eksik = [k for k in BULGULAR if "%s-%s" % k not in isaretli]
    if eksik:
        print("🔴 bulunamadi/atlandi: %s" % eksik)
    print(json.dumps(isaretli, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
