"""E8 4. calistirma: tamamlama ailesi B icin uc tur senaryosuz cevabi yazar.

Kardesi: `_e8_tamamlama_turlar.py` (3. calistirma, aile A). Ayni bicim, ayni
dayanak sinifi. Cevaplar modelin `dogrulama/sessiz/` kopyalarindan (senaryo ve
cevap anahtari gorulmeden) uretildi; burada yalniz kayda geciriliyor ki tur
dosyalari elle yazilmis 12 buyuk JSON yerine tek ve okunabilir bir tabloda dursun.

Kullanim: python tools/_e8_tamamlama_b_turlar.py
Yazar:    kalibrasyon/sessiz/{sentence-completion,summary-completion,
          flow-chart-completion,short-answer}-tur{1,2,3}.json

Dayanak sinifi (`_e8_dayanak_capraz.py` ile ayni):

  ANLAMSAL     frame_wording      — cercevenin/akis semasinin kendi sozu tek bir
                                    doldurmayi birakiyor
               general_knowledge  — cevap alan/dunya bilgisiyle biliniyor
               cross_question     — cevabi BASKA bir sorunun govdesi veriyor;
                                    bu ailede cogu zaman baska bir DOSYA
               logic              — cerceve cevabin turunu/yonunu zorluyor
               grammar_cue        — dilbilgisi zorlamasi ("an (27)" -> unlu)

  SANSA ACIK   number_guess / name_guess / guess

Uc turda ayni cevabin yazilmasi, o kalemde kararin belirli (deterministik) bir
gerekceye dayandigi anlamina gelir; turlarin ayrilmasi gercek kararsizliktir.
Ne senaryo (content/listening/scripts/) ne cevap anahtari acildi.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

# (id, dayanak, tur1, tur2, tur3)

SENTENCE = [
    # alistirma — dort blok
    ("practice-sentence-completion-1", "number_guess", "three", "two", "four"),
    ("practice-sentence-completion-2", "frame_wording", "kit", "test kit", "kit"),
    ("practice-sentence-completion-3", "guess", "bridge", "mill", "car park"),
    ("practice-sentence-completion-4", "frame_wording", "file", "file", "PDF"),
    ("practice-sentence-completion-5", "number_guess", "1500", "2000", "1200"),
    ("practice-sentence-completion-6", "grammar_cue", "appendix", "appendix", "appendix"),
    ("practice-sentence-completion-7", "frame_wording", "portal", "portal", "online portal"),
    ("practice-sentence-completion-8", "guess", "department", "placement office", "office"),
    ("practice-sentence-completion-9", "number_guess", "two years", "18 months", "six months"),
    ("practice-sentence-completion-10", "general_knowledge", "24", "24", "20"),
    ("practice-sentence-completion-11", "general_knowledge", "A0", "larger", "A0"),
    ("practice-sentence-completion-12", "frame_wording", "eye level", "eye level", "eye level"),
    ("practice-sentence-completion-13", "number_guess", "30", "50", "40"),
    ("practice-sentence-completion-14", "general_knowledge", "voucher", "book token", "voucher"),
    ("practice-sentence-completion-15", "guess", "app", "library website", "online system"),
    # L1
    ("L1-sentence-completion-27", "guess", "library website", "module page", "library website"),
    ("L1-sentence-completion-28", "guess", "booking system", "reception", "porters"),
    ("L1-sentence-completion-29", "number_guess", "Monday", "Tuesday", "Friday"),
    ("L1-sentence-completion-30", "frame_wording", "definition", "definition", "definition"),
    # L2
    ("L2-sentence-completion-27", "grammar_cue", "appendix", "appendix", "appendix"),
    ("L2-sentence-completion-28", "number_guess", "2000", "2500", "3000"),
    ("L2-sentence-completion-29", "number_guess", "12th", "20th", "15th"),
    ("L2-sentence-completion-30", "general_knowledge", "risk assessment", "declaration",
     "risk assessment"),
    # L3
    ("L3-sentence-completion-27", "frame_wording", "timeline", "timeline", "timeline"),
    ("L3-sentence-completion-28", "logic", "word", "word", "word"),
    ("L3-sentence-completion-29", "number_guess", "10", "15", "12"),
    ("L3-sentence-completion-30", "number_guess", "Friday", "the 30th", "Monday"),
    # L4
    ("L4-sentence-completion-27", "number_guess", "three", "five", "two"),
    ("L4-sentence-completion-28", "general_knowledge", "white space", "white space",
     "white space"),
    ("L4-sentence-completion-29", "guess", "atrium", "foyer", "atrium"),
    ("L4-sentence-completion-30", "general_knowledge", "frozen", "wet", "frozen"),
    # L5
    ("L5-sentence-completion-27", "number_guess", "five", "ten", "six"),
    ("L5-sentence-completion-28", "frame_wording", "appendix", "appendices", "appendix"),
    ("L5-sentence-completion-29", "guess", "computer room", "resource room", "study room"),
    ("L5-sentence-completion-30", "logic", "questionnaire", "questionnaire", "questionnaire"),
    # L6
    ("L6-sentence-completion-27", "number_guess", "50", "30", "40"),
    ("L6-sentence-completion-28", "frame_wording", "template", "spreadsheet", "form"),
    ("L6-sentence-completion-29", "general_knowledge", "folder", "group", "folder"),
    ("L6-sentence-completion-30", "number_guess", "500 records", "200 records", "50 records"),
]

SUMMARY = [
    # L3 — tohum bankasi
    ("L3-summary-completion-31", "general_knowledge", "1920s", "1920s", "1920s"),
    ("L3-summary-completion-32", "general_knowledge", "50", "50", "50"),
    ("L3-summary-completion-33", "general_knowledge", "crust", "crust", "hard crust"),
    ("L3-summary-completion-34", "cross_question", "seal", "seal", "seal"),
    ("L3-summary-completion-35", "general_knowledge", "75", "75", "75"),
    ("L3-summary-completion-36", "general_knowledge", "10", "10", "10"),
    # L5 — denizdeki plastik
    ("L5-summary-completion-36", "general_knowledge", "biofouling", "biofouling", "biofouling"),
    ("L5-summary-completion-37", "general_knowledge", "mesh", "mesh", "mesh"),
    ("L5-summary-completion-38", "general_knowledge", "1950s", "1950s", "1950s"),
    ("L5-summary-completion-39", "general_knowledge", "pellets", "nurdles", "pellets"),
    ("L5-summary-completion-40", "frame_wording", "standardising", "standardising",
     "standardising"),
    # L6 — durtme (nudge)
    ("L6-summary-completion-37", "number_guess", "5", "2", "3"),
    ("L6-summary-completion-38", "general_knowledge", "half", "half", "half"),
    ("L6-summary-completion-39", "general_knowledge", "interests", "welfare", "interests"),
    ("L6-summary-completion-40", "frame_wording", "preregistering", "preregistering",
     "preregistering"),
]

FLOW = [
    # alistirma — dort akis semasi
    ("practice-flow-chart-completion-1", "logic", "separate", "separate", "separate"),
    ("practice-flow-chart-completion-2", "general_knowledge", "20", "20", "20"),
    ("practice-flow-chart-completion-3", "general_knowledge", "regeneration", "regeneration",
     "regeneration"),
    ("practice-flow-chart-completion-4", "guess", "second bank", "partner bank", "backup store"),
    ("practice-flow-chart-completion-5", "general_knowledge", "1", "1", "1"),
    ("practice-flow-chart-completion-6", "cross_question", "brittle", "brittle", "brittle"),
    ("practice-flow-chart-completion-7", "general_knowledge", "a tenth", "a tenth", "a tenth"),
    ("practice-flow-chart-completion-8", "logic", "recycling", "recycling", "recycling"),
    ("practice-flow-chart-completion-9", "guess", "type", "absorption", "cover"),
    ("practice-flow-chart-completion-10", "general_knowledge", "tyres", "tyres", "tyres"),
    ("practice-flow-chart-completion-11", "number_guess", "two", "three", "two"),
    ("practice-flow-chart-completion-12", "cross_question", "window", "window", "window"),
    ("practice-flow-chart-completion-13", "general_knowledge", "friction", "friction", "friction"),
    ("practice-flow-chart-completion-14", "cross_question", "pilot", "pilot", "pilot"),
    ("practice-flow-chart-completion-15", "frame_wording", "hundreds", "hundreds", "hundreds"),
    # L2 — yeraltı kanalı
    ("L2-flow-chart-completion-31", "general_knowledge", "gravel", "alluvial fan", "gravel"),
    ("L2-flow-chart-completion-32", "general_knowledge", "thousand", "thousand", "thousand"),
    ("L2-flow-chart-completion-33", "logic", "maintenance", "maintenance", "maintenance"),
    ("L2-flow-chart-completion-34", "number_guess", "5", "10", "2"),
    ("L2-flow-chart-completion-35", "general_knowledge", "reservoir", "storage pond",
     "reservoir"),
    # L4 — yol gurultusu
    ("L4-flow-chart-completion-36", "frame_wording", "receiver", "receiver", "receiver"),
    ("L4-flow-chart-completion-37", "general_knowledge", "pores", "voids", "pores"),
    ("L4-flow-chart-completion-38", "frame_wording", "landscaping", "landscaping",
     "landscaping"),
    ("L4-flow-chart-completion-39", "number_guess", "30", "100", "30"),
    ("L4-flow-chart-completion-40", "logic", "bedrooms", "bedrooms", "bedrooms"),
]

SHORT = [
    # alistirma
    ("practice-short-answer-1", "number_guess", "50 years", "60 years", "40 years"),
    ("practice-short-answer-2", "frame_wording", "rooftop farms", "rooftop farms",
     "rooftop farms"),
    ("practice-short-answer-3", "number_guess", "40", "100", "12"),
    ("practice-short-answer-4", "general_knowledge", "raised beds", "raised beds",
     "raised beds"),
    ("practice-short-answer-5", "general_knowledge", "silt", "silt", "sediment"),
    ("practice-short-answer-6", "number_guess", "a third", "half", "40 per cent"),
    ("practice-short-answer-7", "general_knowledge", "rainfall", "the water table", "rainfall"),
    ("practice-short-answer-8", "number_guess", "5 degrees", "6 degrees", "10 degrees"),
    ("practice-short-answer-9", "general_knowledge", "logarithmic", "logarithmic",
     "logarithmic"),
    ("practice-short-answer-10", "general_knowledge", "railways", "railways", "railways"),
    ("practice-short-answer-11", "frame_wording", "line of sight", "line of sight",
     "line of sight"),
    ("practice-short-answer-12", "number_guess", "15 minutes", "10 minutes", "five minutes"),
    ("practice-short-answer-13", "general_knowledge", "1 micrometre", "1 micrometre",
     "one micron"),
    ("practice-short-answer-14", "general_knowledge", "ghost gear", "ghost gear", "ghost gear"),
    ("practice-short-answer-15", "cross_question", "every 15 years", "every 15 years",
     "every 15 years"),
    # L1
    ("L1-short-answer-37", "general_knowledge", "lead", "lead", "lead"),
    ("L1-short-answer-38", "general_knowledge", "lettuce", "lettuce", "lettuce"),
    ("L1-short-answer-39", "number_guess", "a third", "10 per cent", "20 per cent"),
    ("L1-short-answer-40", "guess", "ones that fail", "small projects", "failed projects"),
    # L3
    ("L3-short-answer-37", "general_knowledge", "wild relatives", "wild relatives",
     "wild relatives"),
    ("L3-short-answer-38", "general_knowledge", "the freezer", "the freezer", "the freezer"),
    ("L3-short-answer-39", "general_knowledge", "orthodox", "orthodox", "orthodox"),
    ("L3-short-answer-40", "general_knowledge", "minus 196", "minus 196", "minus 196"),
    # L4
    ("L4-short-answer-31", "general_knowledge", "unwanted sound", "unwanted sound",
     "unwanted sound"),
    ("L4-short-answer-32", "general_knowledge", "3", "3", "3"),
    ("L4-short-answer-33", "general_knowledge", "low frequencies", "low frequencies",
     "low frequencies"),
    ("L4-short-answer-34", "general_knowledge", "every five years", "every five years",
     "every five years"),
    ("L4-short-answer-35", "number_guess", "80 per cent", "70 per cent", "two thirds"),
]

PAKETLER = [
    ("sentence-completion", SENTENCE),
    ("summary-completion", SUMMARY),
    ("flow-chart-completion", FLOW),
    ("short-answer", SHORT),
]


def main():
    toplam = 0
    for paket, tablo in PAKETLER:
        kimlikler = [s[0] for s in tablo]
        if len(set(kimlikler)) != len(kimlikler):
            print("HATA: %s icinde tekrar eden kimlik var." % paket)
            return 1
        for tur in (1, 2, 3):
            ortak.yaz("kalibrasyon/sessiz/%s-tur%d.json" % (paket, tur), {
                "paket": paket,
                "tur": tur,
                "answers": [{"id": sid, "answer": satir[1 + tur], "basis": satir[1]}
                            for satir in tablo for sid in [satir[0]]],
            })
        print("%-24s %3d kalem x 3 tur" % (paket, len(tablo)))
        toplam += len(tablo)
    print("toplam %d kalem" % toplam)
    print("Sirada: python tools/_e8_anlam_esle.py <paket>  (K3 bayragini script yazar)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
