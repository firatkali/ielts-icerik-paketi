# -*- coding: utf-8 -*-
"""OPUS5-E6 1. calistirma: YES/NO/NOT GIVEN - tam testler.

E5'in eledigi uc yuvayi (GT1/33, GT1/34, GT2/34) ayni dosyaya ayni numarayla
yeniden doldurur. Soru sayisi degismez, hicbir soru silinmez.

Kullanim: python tools/_e6_ynng_uret.py
"""
import collections
import io
import json
import os
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Alan sirasi mevcut yuvalarla ayni kalsin.
SIRA = ["number", "prompt", "answer", "evidence", "evidence_locator",
        "contradiction_point", "not_given_justification", "scan_note",
        "explanation", "difficulty", "status", "blind_solvable", "blind_basis",
        "generated_by", "yeniden_uretim"]

YENI = {
    ("content/reading/tests/GT1/yes-no-not-given.json", 33): {
        "prompt": "Edible food made up a clearly larger part of urban waste than of rural waste.",
        "answer": ["YES"],
        "evidence": ("City dwellers in Cibinong generated 79.4 kilograms of food waste per person a year, "
                     "almost double the 45.8 kilograms recorded in rural Sukajaya, and a significantly higher "
                     "proportion of the urban total, 38.2%, was edible food compared with 23.4% in rural areas."),
        "evidence_locator": {"paragraph": "D", "sentence": 2},
        "contradiction_point": None,
        "not_given_justification": None,
        "scan_note": ("Kentsel-kirsal karsilastirma D paragrafinda: D/1 farkin varligini duyuruyor, D/2 hem "
                      "kisi basi agirliklari (79,4'e 45,8) hem yenilebilir payi (%38,2'ye %23,4) veriyor, D/3 "
                      "geliri neden olarak aniyor. Miktar ile pay ayni cumlede yan yana durdugu icin sorunun "
                      "ekseni hangisinin sorulduguna dikkat etmek. H/1-2 kirsalin daha az attigini yineliyor "
                      "ama yenilebilir payi hakkinda ayri bir sayi vermiyor."),
        "explanation": ("The writer reports that 38.2% of the urban total was edible food, against 23.4% in "
                        "rural areas, so edible food formed a larger share of city waste."),
        "difficulty": "medium",
        "ne_degisti": ("Yuva bosaltilip ayni pasajdan yeni bir ifadeyle dolduruldu. Eski soru B/1'deki "
                       "'oz-bildirime dayali tahminler guvenilmez' yargisini soruyordu; bu, pasajdan bagimsiz "
                       "bilinen bir yontem kuraliydi. Yeni ifade B paragrafina hic degmiyor: kanit D/2'ye, "
                       "kentsel ve kirsal atigin yenilebilir paylarina tasindi. Pay yalnizca calismanin kendi "
                       "sayilarindan (%38,2'ye %23,4) okunabiliyor ve ayni cumlede duran kisi basi agirlik "
                       "farkiyla karistirilmamasi gerekiyor, yani miktar-oran ayrimini yapmak sart. Kip "
                       "dengesi icin ifade mutlak yazildi ('clearly larger') ve cevabi YES: olculu kipin "
                       "dogru, mutlak kipin yanlis tarafa ayrilmasi kirildi."),
    },
    ("content/reading/tests/GT1/yes-no-not-given.json", 34): {
        "prompt": ("Roughly half of the food discarded by the households studied is likely to have gone into "
                   "the rubbish bin."),
        "answer": ["NO"],
        "evidence": ("The researchers also noted an important boundary of their method: they measured only "
                     "what ended up in household rubbish bins, which accounted for 82.8% of all discarded "
                     "food in the sample."),
        "evidence_locator": {"paragraph": "F", "sentence": 2},
        "contradiction_point": ("Yazar cop kutusuna gidenin butun atilan gidanin %82,8'i oldugunu kesin bir "
                                "sayiyla veriyor; ifade bu payi yari dolayina indiriyor. Celiski tek noktada: "
                                "kutuya giden payin buyuklugu. Ifadedeki 'roughly / is likely to' olculu kipi "
                                "araligi genisletmiyor, cunku %82,8 yariya yakin sayilamaz."),
        "not_given_justification": None,
        "scan_note": ("Yontemin kapsam payi F/2'de tek bir sayiyla veriliyor (%82,8); F/3 kutu disinda kalanin "
                      "ana toplamlara girmedigini soyluyor, H/2 kirsalda kompostun yayginligini aniyor. "
                      "Hicbir paragraf kutuya giden pay icin ikinci bir oran vermiyor."),
        "explanation": ("The writer gives a definite figure for this: rubbish bins accounted for 82.8% of all "
                        "the food discarded in the sample, far more than about half."),
        "difficulty": "medium",
        "ne_degisti": ("Yuva bosaltilip ayni pasajdan yeni bir ifadeyle dolduruldu. Eski soru C/2'deki "
                       "yenilebilir-yenilemez ayrimini soruyordu; kabuk, kemik ve yumurta kabugunun "
                       "'onlenemez' sayilmasi gida israfi tartismasinda yerlesik bir siniflandirma oldugu "
                       "icin cevap pasajsiz da cikiyordu. Yeni ifade C paragrafina hic degmiyor: kanit "
                       "F/2'ye, yontemin kapsam payina (%82,8) tasindi. Bu oran keyfi bir arastirma "
                       "ayrintisi; disaridan bilinemez, yalniz metinden okunur. Kip dengesi icin ifade "
                       "olculu yazildi ('roughly ... is likely to') ve cevabi NO: olculu kipin otomatik "
                       "olarak dogru cevaba isaret etmesi kirildi."),
    },
    ("content/reading/tests/GT2/yes-no-not-given.json", 34): {
        "prompt": ("Anyone volunteering less often than twice a year fell outside the study's definition of a "
                   "volunteer."),
        "answer": ["YES"],
        "evidence": ("Volunteering was recorded as a simple yes-or-no measure, based on whether a person had "
                     "taken part in unpaid work for an organisation at least once every six months, while "
                     "health was self-reported on a five-point scale running from \"very bad\" to \"very good\"."),
        "evidence_locator": {"paragraph": "B", "sentence": 3},
        "contradiction_point": None,
        "not_given_justification": None,
        "scan_note": ("Gonulluluk olcusunun tanimi B/3'te: kurulusta ucretsiz calismaya alti ayda en az bir kez "
                      "katilmis olmak. Sikliga iliskin ikinci bir esik yalnizca G/1'de geciyor (dayaniklilik "
                      "sinamasinda farkli tanimlar denenmis) ama orada asil tanim degistirilmiyor; D siklik "
                      "degil ulke oranlarini veriyor."),
        "explanation": ("Volunteering was defined as taking part in unpaid work for an organisation at least "
                        "once every six months, so anyone taking part less than twice a year would not have "
                        "met that threshold."),
        "difficulty": "medium",
        "ne_degisti": ("Yuva bosaltilip ayni pasajdan yeni bir ifadeyle dolduruldu. Eski soru C/3'teki "
                       "'oz-bildirimli saglik gelecekteki hastaligi ongorur' bulgusunu soruyordu; bu, saglik "
                       "yazininda genel kulturlesmis bir bulgu oldugu icin pasaj kapaliyken de "
                       "bilinebiliyordu. Yeni ifade C paragrafina hic degmiyor: kanit B/3'e, gonulluluk "
                       "olcusunun esigine tasindi. Esigin alti ayda bir mi yilda bir mi oldugu disaridan "
                       "kestirilemeyen keyfi bir tasarim ayrintisi; ustelik 'alti ayda en az bir kez' "
                       "esigini 'yilda iki kez'e cevirip sinir durumu hakkinda hukum vermek gerekiyor. Kip "
                       "dengesi icin ifade mutlak yazildi ('Anyone ... fell outside') ve cevabi YES."),
    },
}


def main():
    for (rel, no), yeni in YENI.items():
        yol = os.path.join(KOK, rel.replace("/", os.sep))
        d = json.load(open(yol, encoding="utf-8"))
        for i, it in enumerate(d["items"]):
            if it.get("number") != no:
                continue
            eski = {
                "tarih": "2026-08-08",
                "kaynak_prompt": "prompts/OPUS5-E6-yeniden-uretim.md (1/7)",
                "uretilen_grup": "YES/NO/NOT GIVEN - tam testler",
                "eski_prompt": it["prompt"],
                "eski_cevap": it["answer"],
                "eski_kanit_cumlesi": it.get("evidence"),
                "neden_elendi": it.get("reject_reason"),
                "ne_degisti": yeni.pop("ne_degisti"),
            }
            yeni_item = {
                "number": no,
                "status": "verified",
                "blind_solvable": None,
                "blind_basis": None,
                "generated_by": "opus",
                "yeniden_uretim": eski,
            }
            yeni_item.update(yeni)
            d["items"][i] = collections.OrderedDict(
                (k, yeni_item[k]) for k in SIRA if k in yeni_item)
        with open(yol, "w", encoding="utf-8", newline="\n") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print("yazildi:", rel, no)


if __name__ == "__main__":
    main()
