"""E10 1. calistirma: cumle tamamlama + kisa cevap paketlerini ANLAM duzeyinde
yeniden degerlendirir ve bulgulari orijinal soru dosyalarina isler.

Kullanim: python tools/_e10_anlam_isaretle.py

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
# Karar kurali: modelin cevabi gercek cevapla AYNI SEYE isaret ediyorsa anlamca
# dogru. Niteleyici dusup ana ad kaliyorsa ayni sey; gonderge daralip/degisiyorsa
# ya da sayi/isim tutmuyorsa degil.
BULGULAR = {
    ("practice-sentence-completion", 2):
        "3 turda da 'contact' verdi, gerçek cevap 'sensory contact'",
    ("practice-sentence-completion", 3):
        "'anatomy / morphology / anatomy' verdi, 'morphology' anatomy'nin eş "
        "anlamlısı",
    ("practice-sentence-completion", 4):
        "3 turda da 'seawater' verdi, gerçek cevap 'running seawater'",
    ("practice-sentence-completion", 6):
        "3 turda da 'individual' verdi, gerçek cevap 'unique individual'",
    ("practice-sentence-completion", 7):
        "3 turda da 'laboratory' verdi, gerçek cevap 'laboratory tank'",
    ("practice-sentence-completion", 12):
        "3 turda da 'preliminary' verdi, gerçek cevap 'ongoing research' — aynı "
        "kavramın başka sözcüğü",
    ("AC1-sentence-completion", 19):
        "3 turda da 'transparent barrier' verdi, gerçek cevap 'transparent "
        "divider' — barrier/divider eş anlamlı",
    ("AC1-sentence-completion", 20):
        "3 turda da 'hierarchy' verdi, gerçek cevap 'dominance hierarchy'",
    ("AC2-sentence-completion", 20):
        "3 turda da 'laboratories' verdi, gerçek cevap 'separate laboratories'",
    ("AC3-sentence-completion", 22):
        "3 turda da 'climbers' verdi, gerçek cevap 'mountaineers' — eş anlamlı",
    ("AC4-sentence-completion", 22):
        "'vegetation / foliage / vegetation' verdi, 'foliage' aynı göndergeyi "
        "karşılıyor",
    ("GT1-sentence-completion", 27):
        "3 turda da 'final pay' verdi, gerçek cevap 'final salary' — pay/salary "
        "eş anlamlı",
    ("GT2-sentence-completion", 25):
        "3 turda da 'probation period' verdi, gerçek cevap 'probationary "
        "period' — aynı kelimenin başka çekimi",
    ("GT2-sentence-completion", 26):
        "3 turda da 'office equipment' verdi, gerçek cevap 'home-office "
        "equipment'",
    ("practice-short-answer", 6):
        "3 turda da 'transactive memory' verdi, gerçek cevap 'transactive "
        "memory system'",
}


def main():
    yollar = [p for p in (ortak.bul("content/**/sentence-completion.json")
                          + ortak.bul("content/**/short-answer.json"))
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
