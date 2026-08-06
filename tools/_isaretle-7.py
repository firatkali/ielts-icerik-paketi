"""7. calistirma (dinleme form/plan/tamamlama) icin isaretleme adimi.

content/DOGRULAMA/dinleme-form-plan-tamamlama.json raporunu okur, uyusmayan
sorulara status=flagged + flag_reason, digerlerine status=verified ekler.
Hicbir soru silinmez.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

RAPOR = "content/DOGRULAMA/dinleme-form-plan-tamamlama.json"

# "<dosya>|<numara>" -> gerekce
GEREKCE = {
    "content/listening/practice/sentence-completion.json|1":
        "Bicim farki: capraz dogrulamada '5' yazildi, anahtarda 'five'. Icerik ayni "
        "(alti yerine bes noktada veri toplandi); rakam bicimi kabul edilen varyant olarak eklenmeli.",
    "content/listening/practice/sentence-completion.json|4":
        "Capraz dogrulamada 'file' yazildi, anahtarda 'single file'. Cumlede 'as one (4)' "
        "dendigi icin 'one single file' gereksiz tekrar olur; iki kelime siniri ikisine de izin veriyor.",
    "content/listening/practice/short-answer.json|1":
        "Bicim farki: '50 years' / 'fifty years'. Icerik ayni (zirveden sonra elli yil dustu).",
    "content/listening/practice/short-answer.json|7":
        "Yalnizca belirteclik farki: 'the water table' / 'water table'. Icerik ayni.",
    "content/listening/practice/short-answer.json|11":
        "Yalnizca belirteclik farki: 'the line of sight' / 'line of sight'. Icerik ayni.",
    "content/listening/practice/table-completion.json|4":
        "Tekil/cogul farki: 'Thursday' / 'Thursdays'. Tablo hucresi 'every (4)' dedigi icin "
        "tekil bicim de dogru okunur; ikisi de kabul edilmeli.",
    "content/listening/tests/L1/short-answer.json|39":
        "Bicim farki: '5 per cent' / 'five per cent'. Icerik ayni (ucte bir degil, yaklasik yuzde bes).",
    "content/listening/tests/L2/flow-chart-completion.json|34":
        "Bicim farki: '5' / 'five'. Icerik ayni (yeralti kanalinda kayip yuzde besin altinda).",
    "content/listening/tests/L2/note-completion.json|39":
        "Bicim farki: '12' / 'twelve'. Icerik ayni (on gun degil on iki gunde bir).",
    "content/listening/tests/L2/sentence-completion.json|29":
        "Bicim farki: '19th' / 'nineteenth'. Icerik ayni (12'si eski taslak tarihi).",
    "content/listening/tests/L2/table-completion.json|5":
        "Bicim farki: '2nd' / 'second'. Icerik ayni (3 Ekim Cumartesi degil, 2 Ekim Cuma).",
    "content/listening/tests/L2/table-completion.json|6":
        "Bicim farki: '11' / '11.00'. Icerik ayni (10.30 doldu, bir sonraki slot Sali saat 11).",
    "content/listening/tests/L2/table-completion.json|9":
        "Bicim farki: '6' / 'six'. Icerik ayni (bes saat degil, merdiven yuzunden alti saat).",
    "content/listening/tests/L3/form-completion.json|5":
        "Bicim farki: '1st' / 'first'. Icerik ayni (ayin 15'i degil, ayin biri).",
    "content/listening/tests/L3/sentence-completion.json|29":
        "Bicim farki: '12' / 'twelve'. Icerik ayni (15 dakika gecen yila ait).",
    "content/listening/tests/L3/short-answer.json|38":
        "Yalnizca belirteclik farki: 'freezer' / 'a freezer'. Icerik ayni.",
    "content/listening/tests/L3/summary-completion.json|32":
        "Bicim farki: '50' / 'fifty'. Icerik ayni (otuz bitki eski kilavuzlarda).",
    "content/listening/tests/L3/summary-completion.json|36":
        "Bicim farki: '10' / 'ten'. Icerik ayni (bes yil eski uygulama).",
    "content/listening/tests/L4/note-completion.json|6":
        "Bosluk farki: '07793 441 806' / '07793441806'. Rakamlar ayni; telefon numarasi "
        "bosluklu ve bosluksuz iki bicimde de kabul edilmeli.",
    "content/listening/tests/L4/sentence-completion.json|27":
        "Bicim farki: '3' / 'three'. Icerik ayni (plotter iki degil uc is gunu aliyor).",
    "content/listening/tests/L4/short-answer.json|33":
        "Ifade farki: 'low frequencies' / 'the low end'. Ders metni ikisini de kullaniyor "
        "('the ear is far less sensitive to low frequencies... discounts the low end heavily'); "
        "iki cevap da metinden dogrudan alinabilir, ikisi de kabul edilmeli.",
    "content/listening/tests/L6/form-completion.json|10":
        "Bosluk farki: 'HR942' / 'HR 942'. Icerik ayni.",
    "content/listening/tests/L6/summary-completion.json|37":
        "Bicim farki: '5' / 'five'. Icerik ayni (gazetelerdeki on bes puan tek pilottan).",
}


def main():
    rapor = ortak.oku(RAPOR)
    isaretli = dogrulanan = 0

    for sonuc in rapor["sonuclar"]:
        yol = sonuc.get("file")
        if not yol or "detay" not in sonuc:
            continue
        sorunlu = {str(d["number"]) for d in sonuc["detay"]}
        d = ortak.oku(yol)
        for it in ortak.sorular(d):
            n = str(it.get("number"))
            if n in sorunlu:
                anahtar = "%s|%s" % (yol, n)
                if anahtar not in GEREKCE:
                    raise SystemExit("Gerekce eksik: " + anahtar)
                it["status"] = "flagged"
                it["flag_reason"] = GEREKCE[anahtar]
                isaretli += 1
            else:
                it["status"] = "verified"
                it.pop("flag_reason", None)
                dogrulanan += 1
        ortak.yaz(yol, d)
        print("  guncellendi:", yol)

    print("\nflagged: %d | verified: %d" % (isaretli, dogrulanan))


if __name__ == "__main__":
    main()
