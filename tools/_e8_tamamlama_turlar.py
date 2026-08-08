"""E8 3. calistirma: tamamlama ailesi A icin uc tur senaryosuz cevabi yazar.

Cevaplar modelin `dogrulama/sessiz/` kopyalarindan (senaryo ve cevap anahtari
gorulmeden) uretildi; burada yalniz kayda geciriliyor ki tur dosyalari elle
yazilmis 9 buyuk JSON yerine tek ve okunabilir bir tabloda dursun.

Kullanim: python tools/_e8_tamamlama_turlar.py
Yazar:    kalibrasyon/sessiz/{form,note,table}-completion-tur{1,2,3}.json

Dayanak sinifi (2. calistirmadaki ayrimin tamamlama ailesine cevrilmis hali):

  ANLAMSAL     frame_wording  — form/not iskeletinin kendi sozu tek bir doldurmayi
                                birakiyor (coktan secmelideki `option_wording`in
                                karsiligi: orada secenegin sozu, burada cercevenin sozu)
               general_knowledge — cevap alan/dunya bilgisiyle biliniyor
               cross_question    — cevabi BASKA bir sorunun govdesi veriyor
                                   (bu ailede cogu zaman baska bir DOSYA: alistirma
                                   paketleri tam testlerle ayni senaryolari kullaniyor)
               logic             — cerceve cevabin turunu/yonunu zorluyor
               grammar_cue       — dilbilgisi zorlamasi (ornek: "an (40)" -> unlu ile baslar)

  SANSA ACIK   number_guess / name_guess / guess

  HARIC        arac_kirlenmesi — cevap bilgisi ols;um araciyla modele sizdi, olcume
                                 girmez (asagidaki nota bak)

🔴 `arac_kirlenmesi`: `_e8_sizinti_kontrol.py` "govdede birebir gecen cevap
dizgisi: N" uyarisi veriyor, `_e8_govde_cakismasi.py` ise hangi alanda oldugunu
soyluyor. Bu iki cikti birlikte uc kalemde cevabi model icin daralttiu (kopyada
zaten gecen bir sozcuk oldugu ortaya cikti). O uc kalem `haric: true` ile
isaretlendi ve orana katilmadi — kirlenmis olcum, olcum degildir.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

# (id, dayanak, tur1, tur2, tur3)
FORM = [
    # L1 - WILLOWBANK ACTIVITY CAMPS
    ("L1-form-completion-1", "name_guess", "Wheeler", "Bradshaw", "Hendrick"),
    ("L1-form-completion-2", "guess", "junior", "8-10", "middle"),
    ("L1-form-completion-3", "number_guess", "6 July", "13 July", "10 July"),
    ("L1-form-completion-4", "number_guess", "9 a.m.", "8.45", "9.30"),
    ("L1-form-completion-5", "number_guess", "120", "135", "110"),
    ("L1-form-completion-6", "number_guess", "50", "30", "60"),
    ("L1-form-completion-7", "general_knowledge", "debit card", "debit card", "credit card"),
    ("L1-form-completion-8", "number_guess", "07700 900412", "01632 960255", "07866 341290"),
    ("L1-form-completion-9", "guess", "sailing", "climbing", "canoeing"),
    ("L1-form-completion-10", "frame_wording", "waterproof jacket", "waterproof coat",
     "waterproof jacket"),
    # L3 - QUARRY FIELDS LEISURE CENTRE
    ("L3-form-completion-1", "name_guess", "Dawson", "Ellison", "Marsden"),
    ("L3-form-completion-2", "number_guess", "12", "7", "4"),
    ("L3-form-completion-3", "number_guess", "38", "42", "35"),
    ("L3-form-completion-4", "general_knowledge", "5", "5", "4"),
    ("L3-form-completion-5", "number_guess", "1st", "15th", "5th"),
    ("L3-form-completion-6", "frame_wording", "writing", "writing", "writing"),
    ("L3-form-completion-7", "number_guess", "45", "30", "40"),
    ("L3-form-completion-8", "frame_wording", "shoes", "trainers", "shoes"),
    ("L3-form-completion-9", "frame_wording", "phone", "telephone", "phone"),
    ("L3-form-completion-10", "guess", "March", "April", "February"),
    # L5 - HOLLOWFIELD CYCLE TOURS
    ("L5-form-completion-1", "number_guess", "16", "9", "23"),
    ("L5-form-completion-2", "number_guess", "9.30", "9", "10"),
    ("L5-form-completion-3", "name_guess", "Reynolds", "Carmichael", "Bexley"),
    ("L5-form-completion-4", "number_guess", "27", "14", "62"),
    ("L5-form-completion-5", "number_guess", "35", "28", "42"),
    ("L5-form-completion-6", "number_guess", "40", "32", "50"),
    ("L5-form-completion-7", "general_knowledge", "pub", "cafe", "pub"),
    ("L5-form-completion-8", "cross_question", "water bottle", "water bottle", "water bottle"),
    ("L5-form-completion-9", "guess", "town hall", "library", "clock tower"),
    ("L5-form-completion-10", "number_guess", "GR4472", "HC2810", "GW1195"),
    # L6 - ARDLEIGH COLLEGE
    ("L6-form-completion-1", "name_guess", "Halloran", "Pritchard", "Nkemdi"),
    ("L6-form-completion-2", "guess", "Geography", "Engineering", "History"),
    ("L6-form-completion-3", "name_guess", "14 Sandbach Road", "8 Priory Close", "23 Elm Grove"),
    ("L6-form-completion-4", "frame_wording", "refurbished", "renovated", "rewired"),
    ("L6-form-completion-5", "general_knowledge", "en-suite", "en-suite", "en-suite"),
    ("L6-form-completion-6", "logic", "132", "145", "128"),
    ("L6-form-completion-7", "frame_wording", "boxes", "suitcases", "belongings"),
    ("L6-form-completion-8", "number_guess", "30", "15", "28"),
    ("L6-form-completion-9", "frame_wording", "porters' lodge", "reception", "porters' lodge"),
    ("L6-form-completion-10", "number_guess", "AC7318", "HR2094", "ARD556"),
]

NOTE = [
    # alistirma - dort ayri senaryo (hepsi tam testlerle ORTAK)
    ("practice-note-completion-1", "number_guess", "9", "8", "10"),
    ("practice-note-completion-2", "number_guess", "4 p.m.", "3.30", "5 p.m."),
    ("practice-note-completion-3", "frame_wording", "sweets", "nuts", "sweets"),
    ("practice-note-completion-4", "number_guess", "1 June", "30 May", "15 June"),
    ("practice-note-completion-5", "number_guess", "15", "12", "20"),
    ("practice-note-completion-6", "guess", "repair kit", "gloves", "sun cream"),
    ("practice-note-completion-7", "number_guess", "a week", "48 hours", "two weeks"),
    ("practice-note-completion-8", "general_knowledge", "bad weather", "high winds", "ice"),
    ("practice-note-completion-9", "general_knowledge", "2,500", "3,000", "2,700"),
    ("practice-note-completion-10", "frame_wording", "maintenance", "labour", "maintenance"),
    ("practice-note-completion-11", "number_guess", "30 metres", "20 metres", "seven storeys"),
    ("practice-note-completion-12", "frame_wording", "time", "time", "time"),
    ("practice-note-completion-13", "general_knowledge", "framing", "framing", "framing"),
    ("practice-note-completion-14", "general_knowledge", "13.6", "13.6", "11"),
    ("practice-note-completion-15", "guess", "a week", "three days", "ten days"),
    # L1 - GROWING FOOD IN CITIES
    ("L1-note-completion-31", "cross_question", "allotments", "allotments", "allotments"),
    ("L1-note-completion-32", "cross_question", "community garden", "community gardens",
     "community garden"),
    ("L1-note-completion-33", "number_guess", "500", "250", "300"),
    ("L1-note-completion-34", "arac_kirlenmesi", "three", "three", "three"),
    ("L1-note-completion-35", "arac_kirlenmesi", "half", "half", "half"),
    ("L1-note-completion-36", "frame_wording", "contact", "contact", "contact"),
    # L2 - STORING AND SHARING THE WATER
    ("L2-note-completion-36", "general_knowledge", "pottery", "pottery", "brick"),
    ("L2-note-completion-37", "frame_wording", "settling tank", "filter tank", "settling tank"),
    ("L2-note-completion-38", "frame_wording", "silt", "silt", "silt"),
    ("L2-note-completion-39", "number_guess", "10", "12", "14"),
    ("L2-note-completion-40", "grammar_cue", "obligation", "obligation", "obligation"),
    # L4 - MARCHWOOD COACHES LOST PROPERTY
    ("L4-note-completion-1", "guess", "501", "X17", "Airline"),
    ("L4-note-completion-2", "guess", "Tuesday", "Thursday", "Monday"),
    ("L4-note-completion-3", "frame_wording", "luggage rack", "overhead locker", "luggage rack"),
    ("L4-note-completion-4", "guess", "navy blue", "dark green", "black"),
    ("L4-note-completion-5", "name_guess", "Cavendish", "Oduya", "Trelawney"),
    ("L4-note-completion-6", "number_guess", "07700 900318", "01632 960774", "07892 441003"),
    ("L4-note-completion-7", "general_knowledge", "charity shop", "charity", "charity shop"),
    ("L4-note-completion-8", "guess", "ticket office", "car park", "cafe"),
    ("L4-note-completion-9", "frame_wording", "passport", "passport", "passport"),
    ("L4-note-completion-10", "number_guess", "5", "10", "8"),
    # L6 - BEHAVIOURAL ECONOMICS
    ("L6-note-completion-31", "general_knowledge", "unlimited", "unlimited", "limitless"),
    ("L6-note-completion-32", "general_knowledge", "1.5", "1.5", "1.5"),
    ("L6-note-completion-33", "frame_wording", "complaints", "complaints", "complaints"),
    ("L6-note-completion-34", "general_knowledge", "nine in ten", "90 per cent", "nine in ten"),
    ("L6-note-completion-35", "general_knowledge", "procrastination", "procrastination",
     "procrastination"),
    ("L6-note-completion-36", "general_knowledge", "next pay rise", "pay rise", "next pay rise"),
]

TABLE = [
    # alistirma - dort senaryo (yine tam testlerle ORTAK)
    ("practice-table-completion-1", "number_guess", "250", "300", "200"),
    ("practice-table-completion-2", "guess", "passport", "proof of identity", "photograph"),
    ("practice-table-completion-3", "number_guess", "21", "14", "28"),
    ("practice-table-completion-4", "logic", "Tuesday", "Thursday", "Wednesday"),
    ("practice-table-completion-5", "number_guess", "4.30", "5.15", "3.45"),
    ("practice-table-completion-6", "guess", "keyring", "leather fob", "blue keyring"),
    ("practice-table-completion-7", "cross_question", "reference number", "reference number",
     "reference number"),
    ("practice-table-completion-8", "number_guess", "12", "8", "15"),
    ("practice-table-completion-9", "general_knowledge", "1940s", "1940s", "1940s"),
    ("practice-table-completion-10", "cross_question", "vertical", "vertical", "vertical"),
    ("practice-table-completion-11", "logic", "saving money", "saving money", "fresh food"),
    ("practice-table-completion-12", "number_guess", "25", "22", "30"),
    ("practice-table-completion-13", "number_guess", "10 per cent", "5", "20 per cent"),
    ("practice-table-completion-14", "guess", "Thursday", "Monday", "Wednesday"),
    ("practice-table-completion-15", "general_knowledge", "padlock", "padlock", "padlock"),
    # L2 - removals
    ("L2-table-completion-1", "name_guess", "Vaughan", "Kaminski", "Braithwaite"),
    ("L2-table-completion-2", "number_guess", "07700 900266", "01632 960118", "07845 220719"),
    ("L2-table-completion-3", "name_guess", "Alder Road", "Hillside Avenue", "Beech Street"),
    ("L2-table-completion-4", "name_guess", "Netherfield", "Kirkby", "Ashford"),
    ("L2-table-completion-5", "arac_kirlenmesi", "second", "second", "second"),
    ("L2-table-completion-6", "number_guess", "10.30", "2.15", "11 a.m."),
    ("L2-table-completion-7", "number_guess", "420", "395", "450"),
    ("L2-table-completion-8", "frame_wording", "crate", "wooden crate", "crate"),
    ("L2-table-completion-9", "number_guess", "7", "6", "8"),
    ("L2-table-completion-10", "general_knowledge", "aerosols", "gas bottles", "plants"),
    # L5 - microplastics
    ("L5-table-completion-31", "general_knowledge", "5", "5", "5"),
    ("L5-table-completion-32", "logic", "a fifth", "a fifth", "half"),
    ("L5-table-completion-33", "frame_wording", "flood", "flood", "wet"),
    ("L5-table-completion-34", "general_knowledge", "8", "8", "10"),
    ("L5-table-completion-35", "frame_wording", "nets", "nets", "instruments"),
]

PAKETLER = {
    "form-completion": FORM,
    "note-completion": NOTE,
    "table-completion": TABLE,
}


def main():
    for paket, satirlar in PAKETLER.items():
        for tur in (1, 2, 3):
            cevaplar = []
            for sid, dayanak, *uc in satirlar:
                kayit = {"id": sid, "answer": uc[tur - 1], "basis": dayanak}
                if dayanak == "arac_kirlenmesi":
                    kayit["haric"] = True
                cevaplar.append(kayit)
            ortak.yaz("kalibrasyon/sessiz/%s-tur%d.json" % (paket, tur),
                      {"paket": paket, "tur": tur, "answers": cevaplar})
        print("%s: %d kalem x 3 tur" % (paket, len(satirlar)))
    print("toplam %d kalem" % sum(len(v) for v in PAKETLER.values()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
