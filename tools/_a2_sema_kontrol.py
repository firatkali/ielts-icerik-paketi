"""degerlendirme/cikti-semasi.json dosyasinin kendi kendini sinamasi.

Kullanim:  python tools/_a2_sema_kontrol.py

Sema gecerli mi, semadaki ornekler semaya uyuyor mu ve semanin reddetmesi
gereken ciktilari gercekten reddediyor mu diye bakar. Elle goz kararina
guvenilmedi: sema ic ice if/then kullaniyor, bir yazim hatasi sessizce
kurali etkisiz birakabiliyor.
"""

import copy
import json
import os
import sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEMA = os.path.join(KOK, "degerlendirme", "cikti-semasi.json")


def main():
    with open(SEMA, encoding="utf-8") as f:
        sema = json.load(f)
    print("JSON okundu:", os.path.relpath(SEMA, KOK))

    try:
        from jsonschema import Draft202012Validator as V
    except ImportError:
        print("jsonschema kurulu degil - sadece JSON gecerliligi kontrol edildi.")
        return 0

    V.check_schema(sema)
    print("Sema gecerli (draft 2020-12).")
    dogrulayici = V(sema)

    hata = 0
    for i, ornek in enumerate(sema["examples"]):
        hatalar = [e.message for e in dogrulayici.iter_errors(ornek)]
        print("  ornek %d: %s" % (i, hatalar or "gecti"))
        hata += len(hatalar)

    # Semanin REDDETMESI gereken durumlar
    def reddetmeli(ad, cikti):
        nonlocal hata
        hatalar = list(dogrulayici.iter_errors(cikti))
        if hatalar:
            print("  reddedildi (dogru): %s" % ad)
        else:
            print("  🔴 KABUL ETTI (yanlis): %s" % ad)
            hata += 1

    yazma = sema["examples"][0]
    yetersiz = sema["examples"][1]

    d = copy.deepcopy(yazma)
    d["criteria"] = d["criteria"][:3]
    reddetmeli("yazma, 4 yerine 3 olcut", d)

    d = copy.deepcopy(yazma)
    d["skill"] = "speaking"
    reddetmeli("konusma, 3 yerine 4 olcut", d)

    d = copy.deepcopy(yazma)
    d["overall_band"] = 6.25
    reddetmeli("ceyrek band", d)

    d = copy.deepcopy(yazma)
    d["estimated"] = False
    reddetmeli("estimated: false", d)

    d = copy.deepcopy(yazma)
    d["criteria"][0]["name"] = "pronunciation"
    reddetmeli("telaffuz olcutu", d)

    d = copy.deepcopy(yazma)
    del d["criteria"][0]["quote"]
    reddetmeli("alintisiz gerekce", d)

    d = copy.deepcopy(yazma)
    d["rewrites"] = d["rewrites"] * 4
    reddetmeli("4 duzeltme ornegi (en fazla 3)", d)

    d = copy.deepcopy(yazma)
    d["comment"] = "serbest metin"
    reddetmeli("semada olmayan alan", d)

    d = copy.deepcopy(yetersiz)
    d["overall_band"] = 5.0
    reddetmeli("insufficient ama band verilmis", d)

    d = copy.deepcopy(yetersiz)
    del d["insufficient_reason"]
    reddetmeli("insufficient ama sebep yok", d)

    # Konusma ciktisi (3 olcut) kabul edilmeli
    konusma = copy.deepcopy(yazma)
    konusma["skill"] = "speaking"
    konusma["criteria"] = konusma["criteria"][:3]
    konusma["criteria"][0]["name"] = "fluency_coherence"
    konusma["lowest_criterion"] = "fluency_coherence"
    hatalar = [e.message for e in dogrulayici.iter_errors(konusma)]
    print("  konusma, 3 olcut: %s" % (hatalar or "gecti"))
    hata += len(hatalar)

    print("Sonuc:", "TAMAM" if hata == 0 else "%d SORUN" % hata)
    return 0 if hata == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
