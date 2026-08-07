# -*- coding: utf-8 -*-
"""E10 3. calistirma: not/tablo/akis tamamlama paketlerini (note-completion,
table-completion, flow-chart-completion) ANLAM duzeyinde yeniden degerlendirir
ve bulgulari orijinal soru dosyalarina isler.

Kullanim: python tools/_e10_anlam_isaretle3.py

B1 olcumu "cevap 3/3 turda KELIMESI KELIMESINE tuttu mu" diye bakiyordu. Bu adim
ayni uc tur dokumune anlam duzeyinde bakiyor: es anlamli kelime, farkli cekim ya
da ayni seyi gosteren farkli yuzey ifadesi de "biliniyor" sayiliyor.

HICBIR SORU SILINMEZ. Eski kelime-duzeyi bulgusu da silinmez: uzerine yazmak
yerine blind_solvable_kelime_duzeyi alaninda saklanir (ikisi farkli sey olcuyor).

Dokumler yalniz OKUMA sorularini iceriyor; dinleme setleri bu turda atlanir
(practice set_id'leri iki beceride de ayni, bu yuzden skill filtresi sart).
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

SEBEP = ("Parça gösterilmeden anlamca 3/3 turda doğru bilindi: farklı kelimeyle "
         "ama doğru kavramla cevaplandı (%s).")

# paket -> {(set_id, soru no): gerekcedeki somut karsilastirma}
# Karar kurali 1. ve 2. calistirmadaki ile ayni: modelin cevabi gercek cevapla
# AYNI SEYE isaret ediyorsa anlamca dogru. Niteleyici dusup gonderge ayni
# kaliyorsa ayni sey; gonderge daralip/degisiyorsa ya da sayi/isim tutmuyorsa
# degil.
BULGULAR = {
    "note-completion": {
        ("practice-note-completion", 3):
            "3 turda da 'individual performance' verdi, gerçek cevap "
            "'individual output' — ücretin yalnız kişinin kendi işine bağlı "
            "olduğu aynı iddia",
        ("practice-note-completion", 4):
            "3 turda da 'magpie' verdi, gerçek cevap 'Eurasian magpie' — "
            "niteleyici düştü, aynanın önünde testi geçen kuş aynı",
        ("practice-note-completion", 6):
            "'small sample / small group / small sample' verdi; küçük grup ile "
            "küçük örneklem burada aynı uyarıyı kuruyor",
        ("practice-note-completion", 11):
            "3 turda da 'bed' verdi, gerçek cevap 'wooden bed' — kurbanın "
            "üzerinde bulunduğu nesne aynı, yalnız malzeme niteleyicisi düştü",
        ("practice-note-completion", 12):
            "3 turda da 'bones' verdi, gerçek cevap 'skeletal remains' — eş "
            "anlamlı: tek başına kemiklerin veremediği hücre düzeyi ayrıntı",
        ("AC4-note-completion", 1):
            "'rearrange / reconfigure / rearrange' verdi; rearrange ile "
            "reconfigure aynı iddiayı (ihtiyaç değişince kolay yeniden "
            "düzenlenmesi) veriyor",
        ("GT1-note-completion", 17):
            "'time clock / card reader / clocking-in machine' verdi; üçü de "
            "personel girişindeki aynı cihazı adlandırıyor",
        ("GT1-note-completion", 18):
            "'shift swap form / shift change form / shift swap form' verdi; "
            "vardiya değişimi için doldurulan aynı belge",
        ("GT1-note-completion", 20):
            "'booking system / staff portal / booking system' verdi; izin "
            "taleplerinin girildiği aynı çevrimiçi sistem",
    },
    "table-completion": {
        ("AC3-table-completion", 3):
            "3 turda da 'dye' verdi, gerçek cevap 'cosmetic' — ayna testinde "
            "deriye uygulanan aynı zararsız boyalı işaret",
        ("GT2-table-completion", 15):
            "'sponsorship / a visa / sponsorship' verdi; 'vize gerektirmeden "
            "çalışma hakkı' ile 'sponsorluk gerektirmemesi' aynı koşul",
    },
    "flow-chart-completion": {
        ("AC2-flow-chart-completion", 1):
            "3 turda da '40 minutes' verdi, gerçek cevap 'forty minutes' — "
            "aynı sayının rakamla yazılışı",
    },
}


def main():
    isaretli = []
    for pak, bulgular in BULGULAR.items():
        yollar = [p for p in ortak.bul("content/**/%s.json" % pak)
                  if "/DOGRULAMA/" not in p]
        for p in yollar:
            d = ortak.oku(p)
            if d.get("skill") != "reading":
                continue
            set_id = d.get("set_id", os.path.basename(p))
            degisti = False
            for it in ortak.sorular(d):
                anahtar = (set_id, it.get("number"))
                if anahtar not in bulgular:
                    continue
                if it.get("blind_solvable") is True:
                    print("  zaten isaretli, atlandi: %s-%s" % anahtar)
                    continue
                # Eski kelime-duzeyi bulgusu silinmiyor, sadece tasiniyor.
                it["blind_solvable_kelime_duzeyi"] = it.get("blind_solvable", False)
                it["blind_solvable"] = True
                it["blind_basis"] = "logic"
                it["status"] = "flagged"
                it["flag_reason"] = SEBEP % bulgular[anahtar]
                it["flag_mechanism"] = "esdizim_kilidi"
                isaretli.append("%s-%s" % anahtar)
                degisti = True
            if degisti:
                ortak.yaz(p, d)
                print("  islendi: %s" % p)

    print("\n%d soru anlam duzeyinde isaretlendi." % len(isaretli))
    tum = [k for b in BULGULAR.values() for k in b]
    eksik = [k for k in tum if "%s-%s" % k not in isaretli]
    if eksik:
        print("🔴 bulunamadi/atlandi: %s" % eksik)
    print(json.dumps(isaretli, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
