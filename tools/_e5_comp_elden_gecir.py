# -*- coding: utf-8 -*-
"""E5 / 4. calistirma - tamamlama ailesinde esdizim kilidi.

Kapsam: content/reading altinda tamamlama ailesindeki (note / sentence /
summary / table / flow_chart completion) `flag_mechanism: "esdizim_kilidi"`
tasiyan isaretli sorular; E10'un cumle tamamlama + kisa cevap (7. calistirma)
ve ozet ailesi (8. calistirma) isaretleri disinda.

Kural: answer / evidence / evidence_locator / accepted_variants / numara
degismez. Yalniz soru metni (prompt), ozet-not-akis govdesi (stem_block),
kelime bankasindaki CELDIRICI metinleri ve ic denetim notlari yeniden yazilir.
Betik idempotenttir.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

TARIH = "2026-08-08"
MEK = "esdizim_kilidi"

P_SC = "content/reading/practice/sentence-completion.json"
P_SUM = "content/reading/practice/summary-completion.json"
P_NC = "content/reading/practice/note-completion.json"
AC1_NC = "content/reading/tests/AC1/note-completion.json"
AC2_FC = "content/reading/tests/AC2/flow-chart-completion.json"
AC3_SC = "content/reading/tests/AC3/sentence-completion.json"
AC3_TC = "content/reading/tests/AC3/table-completion.json"
AC4_NC = "content/reading/tests/AC4/note-completion.json"
AC4_SC = "content/reading/tests/AC4/sentence-completion.json"
AC4_SUM = "content/reading/tests/AC4/summary-completion.json"
GT1_NC = "content/reading/tests/GT1/note-completion.json"
GT1_SUM = "content/reading/tests/GT1/summary-completion.json"
GT2_SUM = "content/reading/tests/GT2/summary-completion.json"
GT2_TC = "content/reading/tests/GT2/table-completion.json"

DOSYALAR = [P_SC, P_SUM, P_NC, AC1_NC, AC2_FC, AC3_SC, AC3_TC, AC4_NC,
            AC4_SC, AC4_SUM, GT1_NC, GT1_SUM, GT2_SUM, GT2_TC]

# --------------------------------------------------------------------------
# 1) Duzeltilen sorular
# --------------------------------------------------------------------------

DUZELTME = {

    (P_SC, 8): {
        "prompt": "Its reef has already spent years in water the rest of the "
                  "ocean will not reach for decades, which is why the authors "
                  "describe the site as a (8) ........ .",
        "explanation": "Paragraph C says that the reef at Maug has already "
                       "been living for years in conditions the wider ocean is "
                       "not expected to reach for decades, so that the site "
                       "effectively offers a preview of the future; the gap "
                       "asks what the authors call the site, so the answer is "
                       "'preview'.",
        "ne_degisti": "Kaliplasmis 'a ___ of what is coming' cercevesi "
                      "kaldirildi; bu cerceve bosluga tek bir dogal tamamlama "
                      "birakiyordu. Yeni cumlede bosluk cumle sonunda ve "
                      "cerceveden okunamiyor (warning, benchmark, window "
                      "adaylari da uyuyor), dogru sozcuk ancak C paragrafindaki "
                      "cumleden bulunuyor. 7. sorunun cevabi olan 'laboratory "
                      "tank' ifadesi bilincli olarak yeni metne alinmadi.",
    },

    (P_SUM, 10): {
        "prompt": "Drinks were handled separately: instead of being weighed by "
                  "the team, everything poured away was entered by the "
                  "household itself in a seven-day (10) ........ , type and "
                  "quantity alike.",
        "explanation": "Paragraph B says that discarded drinks were tracked "
                       "separately, with each household keeping a seven-day "
                       "diary noting the type and amount of any beverage "
                       "poured away; the gap asks what that seven-day record "
                       "was, so the answer is 'diary'.",
        "ne_degisti": "'keeping a week-long ___' kalibi kaldirildi: 'keep a "
                      "diary' esdizimi boslugu tek basina dolduruyordu. Yeni "
                      "cercevede ('entered in a seven-day ___') log, record, "
                      "journal ve diary esit derecede uyuyor; secim yalniz B "
                      "paragrafina bakilarak yapilabiliyor.",
    },

    (AC1_NC, 5): {
        "prompt": "He recalled where the cube lay after it had been moved out "
                  "of sight, past a (5) ........ and into a walled passage",
        "explanation": "Paragraph E says the researchers hid the cube around a "
                       "corner, in a walled passage invisible from the point "
                       "where Kandula entered the enclosure; the gap asks what "
                       "the cube was moved past, so the answer is 'corner'.",
        "ne_degisti": "'hidden round a ___' esdizimi kaldirildi. Yeni cerceve "
                      "boslugu 'duvarli gecide girmeden once gecilen sey' "
                      "olarak kuruyor; door, wall, screen, gate adaylari da "
                      "uyuyor, secim yalniz E paragrafina bagli.",
    },

    (AC2_FC, 1): {
        "prompt": "The Near-Infrared Camera records a run of long exposures, "
                  "each of (1) ........ , as a faint speck is followed against "
                  "the background of stars.",
        "explanation": "Paragraph B says Webb's Near-Infrared Camera captured "
                       "a series of long-exposure images, each lasting forty "
                       "minutes; the gap asks how long a single exposure ran, "
                       "so the answer is 'forty minutes'.",
        "ne_degisti": "Kutu hem poz sayisini ('ten') hem toplam sureyi "
                      "('roughly six hours') veriyordu; 6 saat / 10 = 36 ~ 40 "
                      "dakika islemi cevabi pasaja hic bakmadan veriyordu. "
                      "Sizinti burada esdizim degil aritmetikti; iki sayi da "
                      "kutudan cikarildi ve akis semasinin baska bir yerinde "
                      "tekrar edilmedi.",
    },

    (AC3_SC, 20): {
        "prompt": "On the radar pictures, freshly shattered rock and snow show "
                  "up ........ , because a rough surface throws far more of "
                  "the signal back to the satellite than a smooth one.",
        "explanation": "Paragraph C says rough, broken debris scatters radar "
                       "energy strongly and appears bright in the resulting "
                       "images, while smooth, undisturbed ice appears dark; "
                       "the gap asks how the fresh debris shows up, so the "
                       "answer is 'bright'.",
        "ne_degisti": "'whereas ... looks dark' zitligi kaldirildi; bosluk "
                      "artik 'dark'in sozluk karsitini isteyen bir yer degil. "
                      "Yeni cercevede white, clearly, strongly adaylari da "
                      "uyuyor, secim C paragrafina bagli.",
    },

    (AC4_SUM, 37): {
        "prompt": "In the earlier study, one group met 80 pairs late in the "
                  "evening and was tested twelve hours afterwards, while the "
                  "other met them at the start of the day and remained "
                  "(37) ........ until an evening test.",
        "explanation": "Paragraph C says the wake group learned the material "
                       "at nine in the morning, was tested twelve hours later "
                       "at nine that evening, and had remained awake "
                       "throughout; so the correct option is B.",
        "ne_degisti": "'stayed ___' kalibi ('stay awake' esdizimi) 'remained "
                      "___' ile degistirildi ve kelime bankasindaki H secenegi "
                      "('the length of the nap' -> 'in the laboratory') ayni "
                      "cerceveye oturan gercek bir rakip yapildi. Artik iki "
                      "secenek de dilbilgisi ve anlam bakimindan uyuyor; secim "
                      "C paragrafina bagli.",
    },

    (AC4_SUM, 39): {
        "prompt": "Where no such link existed, however, the picture changed: "
                  "the two turned out to offer (39) ........ .",
        "explanation": "Paragraph E says that for unrelated word pairs "
                       "nocturnal sleep and napping produced very similar "
                       "benefits, with effect sizes of 0.71 and 0.68; so the "
                       "correct option is F.",
        "ne_degisti": "'produced almost ___' kalibindaki 'almost' kaldirildi: "
                      "'almost' yakinlik bildirdigi icin bankadaki tek yakinlik "
                      "ifadesini (F) isaret ediyor, G'yi ise dilbilgisiyle "
                      "eliyordu. Yeni cercevede G ('much weaker results') de "
                      "dilbilgisi ve anlam bakimindan uyuyor.",
    },

    (AC4_SUM, 40): {
        "prompt": "Neither how long a rest ran nor which stages it contained "
                  "predicted the size of the gain; what counted, the authors "
                  "argue, was (40) ........ rather than anything about the "
                  "internal shape of the sleep.",
        "explanation": "Paragraph F says that neither the length of a nap nor "
                       "the sleep stages it contained showed a significant "
                       "relationship with the memory gain, and that simply "
                       "having the opportunity to sleep mattered more than the "
                       "nap's internal structure; so the correct option is A.",
        "ne_degisti": "'simply getting ___' kalibi ('get a chance to ...' "
                      "yerlesik esdizimi) kaldirildi ve kelime bankasindaki E "
                      "secenegi ('deeper sleep' -> 'an unbroken night') bu "
                      "cerceveye oturan gercek bir rakip yapildi; 'deeper "
                      "sleep' zaten uykunun IC YAPISI oldugu icin cumlenin "
                      "kendisiyle celisiyor, yani rakip sayilmiyordu.",
    },

    (GT1_NC, 15): {
        "prompt": "Shift pattern: The pattern changes every four weeks; the "
                  "new one appears on the staff (15) ........ by the Friday "
                  "before at the latest",
        "explanation": "Paragraph A of Text A says that the shift pattern, "
                       "which rotates every four weeks, is published on the "
                       "staff noticeboard no later than the preceding Friday; "
                       "so the answer is 'noticeboard'.",
        "ne_degisti": "'put up on the staff ___' esdizimi kaldirildi. Ayni "
                      "belge kumesi cevrimici bir personel portalini da "
                      "anlatiyor; 'appears on the staff ___' cercevesinde "
                      "noticeboard, portal ve intranet esit derecede uyuyor, "
                      "secim yalniz A metnine bakilarak yapilabiliyor.",
    },

    (GT1_NC, 16): {
        "prompt": "Breaks: Within a team, breaks are (16) ........ ; the rule "
                  "exists to protect the production lines",
        "explanation": "Paragraph B of Text A says that breaks must be "
                       "staggered within each team so that production lines "
                       "are never left unattended; so the answer is "
                       "'staggered'.",
        "ne_degisti": "Boslugun onundeki 'colleagues do not stop at the same "
                      "moment' aciklamasi kaldirildi: bu aciklama 'staggered' "
                      "sozcugunun tanimini veriyordu. Yeni cercevede "
                      "scheduled, rotated, limited, coordinated adaylari da "
                      "uyuyor.",
    },

    (GT1_SUM, 40): {
        "prompt": "For the authors, the lesson is that policy has so far dealt "
                  "with collecting and disposing of waste; real (40) ........ ,"
                  " they argue, will depend on campaigns that name the "
                  "particular foods concerned.",
        "explanation": "Paragraph I says that food waste policy has focused on "
                       "collection and disposal rather than prevention, and "
                       "that meaningful reductions depend on tackling the "
                       "specific items identified in the study; so the answer "
                       "is 'prevention'.",
        "ne_degisti": "'collecting and disposing ... rather than its ___' "
                      "karsitligi kaldirildi; atik politikasi soyleminde bu "
                      "karsitligin oteki ucu her zaman 'prevention' oldugu icin "
                      "bosluk tek basina doluyordu. Yeni cercevede reduction, "
                      "progress, change adaylari da uyuyor.",
    },

    (GT2_SUM, 37): {
        "prompt": "Once the strength of the earnings route was measured, "
                  "though, it emerged that income carried (37) ........ of the "
                  "overall link, with the remainder running through something "
                  "the income figures could not reach.",
        "explanation": "Paragraph F says that income differences accounted for "
                       "well under a fifth of the total association between "
                       "volunteering and self-rated health, so the earnings "
                       "route carries only a small part of the link; the "
                       "correct option is B.",
        "ne_degisti": "'it turned out to carry only (37)___' ifadesindeki "
                      "'only' kaldirildi: 'only' kucukluk bildirdigi icin "
                      "bankadaki tek kucukluk ifadesini isaret ediyordu. Yeni "
                      "cercevede F ('roughly half') ve H ('the main driver') de "
                      "dilbilgisi ve anlam bakimindan uyuyor.",
    },

    (GT2_SUM, 38): {
        "prompt": "The team then repeated the analysis with narrower samples, "
                  "with different thresholds for how often someone had to help "
                  "out before they were classed as a volunteer, and with extra "
                  "background variables added; across those versions the "
                  "picture was (38) ........ .",
        "explanation": "Paragraph G says that in every version of the analysis "
                       "the same basic pattern held; since the outcome did not "
                       "change, the correct option is G.",
        "ne_degisti": "'the outcome stayed ___ throughout' kalibi kaldirildi: "
                      "'stay stable' esdizimi boslugu tek basina dolduruyor, "
                      "'stayed contradictory' ise uymuyordu. Yeni cercevede "
                      "('across those versions the picture was ___') C "
                      "('contradictory') ve D ('easily explained') de uyuyor.",
    },

    (GT2_SUM, 39): {
        "prompt": "For the greater share of the effect that money cannot "
                  "account for, the authors offer (39) ........ : a stronger "
                  "sense of purpose and belonging, the walking and standing "
                  "that helping often involves, or an influence on the "
                  "hormones that govern stress.",
        "explanation": "Paragraph H says the authors put forward several "
                       "candidate explanations for the unexplained majority of "
                       "the effect while stressing that their data cannot "
                       "confirm any of them directly; so the correct option is "
                       "I.",
        "ne_degisti": "'___ rather than firm answers' karsitligi ve listedeki "
                      "'possible' niteleyicisi kaldirildi; ikisi de boslugun "
                      "kesinlikten uzak bir sey oldugunu soyluyordu. Yeni "
                      "cercevede E ('proof of a cause') de uyuyor ve secim H "
                      "paragrafina bagli.",
    },

    (GT2_SUM, 40): {
        "prompt": "Turning to the finding as a whole, the authors describe "
                  "what they have shown as (40) ........ .",
        "explanation": "Paragraph I says the authors are careful to describe "
                       "their results as an association rather than proof that "
                       "volunteering causes better health; so the correct "
                       "option is A.",
        "ne_degisti": "Bosluktan hemen onceki 'karistirici etkenler' cumlesi "
                      "ile hemen sonraki 'rastgele atamali bir deneme gerekir' "
                      "kaydi ozetten cikarildi; ikisi birlikte cevabi (yalnizca "
                      "bir iliski) pasaja bakmadan soyluyordu. Yeni cumlede D "
                      "('easily explained') ve E ('proof of a cause') de "
                      "uyuyor.",
    },
}

# --------------------------------------------------------------------------
# 2) Elenen sorular
# --------------------------------------------------------------------------

ELEME = {

    (P_SUM, 1):
        "Sizinti cercevede degil, boslugun hedefinde. Ozet cumlesi kanit "
        "cumlesinin (D/3) tasidigi 'moda olmasina ragmen kotu sonuc verdi' "
        "karsitligini aktarmak zorunda; bu karsitligi tasiyan her cumlede "
        "boslugun tek dogal sozcugu 'popularity' oluyor. Cerceveyi degistirmek "
        "boslugu acmiyor, boslugu baska bir yere tasimak ise cevabi degistirmek "
        "demek. E6 bu yuvayi ayni cumledeki sayisal ayrintiya (yuzde 14'luk "
        "dusus) capalamali.",

    (AC2_FC, 3):
        "Bosluk 'it ___ light' kalibinin ortasinda ve bir gok cisminin "
        "parlakligindan cap tahmin etme varsayimi Ingilizcede yalniz 'reflect' "
        "fiiliyle kuruluyor. Fiili baska bir cerceveye tasimak ya cumleyi "
        "bozuyor ya da cevabi sifat bicimine ('reflective') ceviriyor, yani "
        "korunan alani degistiriyor. E6 bu adimi cap tahmininin sayisina ya da "
        "'too faint to measure directly' gerekcesine capalamali.",

    (AC4_NC, 4):
        "'put on' fiili cikarilsa bile not, gurultu uzerine bir ofis "
        "calismasinda gozlemcilerin saydigi gunluk aliskanligi istiyor; bu "
        "cercevede 'headphones' pasajdan bagimsiz olarak akla gelen ilk ve "
        "neredeyse tek nesne. Kanit cumlesindeki oteki iki ornek (quiet "
        "corners, impromptu conversations) da ayni olcude tahmin edilebilir, "
        "yani hedefi cumle icinde kaydirmak da ise yaramiyor. E6 bu yuvayi ayni "
        "paragrafin olcum aracina (kod commit sayimi) tasimali.",

    (AC4_SC, 20):
        "Bosluk yuzde olarak verilen bir hava olcumunu istiyor; pasajin "
        "siraladigi dort degerden (sicaklik, kar derinligi, nem, ruzgar) yalniz "
        "biri yuzdeyle ifade edilir, dolayisiyla sayinin birimi tek basina "
        "cevabi veriyor. Birimi gizlemek sayiyi da gizlemeyi gerektiriyor, o "
        "zaman da soru olculebilir bir ayrintiya dayanmaktan cikiyor. E6 bu "
        "yuvayi ruzgar hizina (1.13 m/s) ya da kar derinligine capalamali.",

    (AC4_SC, 21):
        "'the passage of time' Ingilizcede tam kaliplasmis bir ifade; bosluk bu "
        "kalibin icinde durdugu surece hangi cerceveye konursa konsun tek "
        "tamamlamasi var, 'of time' kaldirildiginda ise cumle anlamini "
        "yitiriyor. E6 bu yuvayi ayni cumlenin olculebilir ayrintisina "
        "(anketlerin kagit uzerinde, on bes dakikanin hemen oncesinde ve hemen "
        "sonrasinda uygulanmasi) tasimali.",

    (GT2_TC, 16):
        "Is basvurusu baglaminda 'guncel bir ___ yukleyin' satirinin tek yaygin "
        "tamamlamasi CV; sozcuk basvuru surecinin kendisinden cikiyor, "
        "pasajdan degil. Satiri yeniden yazmak bunu degistirmiyor. E6 bu yuvayi "
        "ayni paragrafin baska bir kosuluna (300 kelimelik gerekce metni ya da "
        "28 Subat son basvuru tarihi) capalamali.",

    (GT2_TC, 20):
        "Kanit cumlesinin butun icerigi ('kendi biriminden biriyle "
        "eslestirilir, on hafta boyunca haftada bir gorusur') Ingiliz is "
        "dunyasinda dogrudan 'mentor' rolunu tanimliyor; satirdan hangi ayrinti "
        "cikarilirsa cikarilsin kalan cerceve ayni sozcugu veriyor. E6 bu "
        "yuvayi staj suresinin baska bir ayrintisina (aylik ucret ya da on "
        "haftalik sure) tasimali.",
}

# --------------------------------------------------------------------------
# 3) Dokunulmayan sorular - gerekce notu
# --------------------------------------------------------------------------

ORTAK_NOT = (
    "E10 anlam duzeyi olcumunden gelen isaret: model parcasiz uc turda da "
    "dogru KAVRAMI verdi, tutmayan sey sozcugun kendisiydi. Bu bicimde sizinti "
    "cercevede degil boslugun hedefinde durur; kapatmak icin boslugu baska bir "
    "ayrintiya tasimak, yani `answer` alanini degistirmek gerekir. Talimatin "
    "korunan alan kurali buna izin vermedigi ve soru kelime duzeyinde hala "
    "calistigi icin soru oldugu gibi birakildi. ")

DOKUNMA = {
    (P_NC, 3): ORTAK_NOT + "Model uc turda 'individual performance' verdi. "
               "Not, ucretin yalniz kisinin kendi isine bagli oldugunu "
               "soylemek zorunda ve bu kavramin Ingilizce karsiligi zaten "
               "'individual output/performance'. E6 onerisi: ayni paragrafin "
               "'social comparison / peer pressure' ayrintisina capalanmis yeni "
               "bir yuva.",

    (P_NC, 4): ORTAK_NOT + "Model uc turda 'magpie' verdi; tutmayan tek sey "
               "niteleyici ('Eurasian'). Niteleyiciyi zorunlu kilmanin tek "
               "yolu pasajda ikinci bir saksagan turunun bulunmasi, oyle bir "
               "sey yok. E6 onerisi: listenin kendisi yerine A paragrafindaki "
               "temizlikci balik ornegine capalanmis yuva.",

    (P_NC, 6): ORTAK_NOT + "Model 'small group / small sample' verdi. Uyarinin "
               "kendisi ('tek hayvan ya da az sayida hayvanla calisirsa "
               "yetenek gozden kacar') kavrami zaten tasiyor. E6 onerisi: dort "
               "belugadan ikisinin guclu tepki vermesi sayisina capalanmis "
               "yuva.",

    (P_NC, 11): ORTAK_NOT + "Model uc turda 'bed' verdi. 'Uyur halde bulunmus "
                "bir kurban' cercevesinde yatak kacinilmaz; ayirt edici olan "
                "yalniz malzeme niteleyicisi. E6 onerisi: kurbanin bulundugu "
                "yapinin adina (Collegium Augustalium) capalanmis yuva.",

    (P_NC, 12): ORTAK_NOT + "Model uc turda 'bones' verdi; 'skeletal remains' "
                "ile tam es anlamli. Antik donemden hucre duzeyi ayrinti "
                "iddiasinin karsit terimi kacinilmaz bicimde kemikler oluyor. "
                "E6 onerisi: H paragrafi yerine camlasma sicakligi ya da "
                "sogumanin hizina capalanmis yuva.",

    (AC4_NC, 1): ORTAK_NOT + "Model 'rearrange / reconfigure' verdi. Acik plan "
                 "ofisin ucuzluk disindaki ikinci gerekcesi kacinilmaz bicimde "
                 "'kolay yeniden duzenlenmesi'. E6 onerisi: ayni paragrafin "
                 "kalici odali ofisle yapilan maliyet karsilastirmasina "
                 "capalanmis yuva.",

    (GT1_NC, 17): ORTAK_NOT + "Model 'time clock / card reader / clocking-in "
                  "machine' verdi. Personel girisindeki giris-cikis kayit "
                  "cihazi kavrami cerceveden dogrudan cikiyor. E6 onerisi: "
                  "cihaz yerine ogle molasinin da kaydedilmesi kuralina "
                  "capalanmis yuva.",

    (GT1_NC, 18): ORTAK_NOT + "Model 'shift swap / shift change form' verdi. "
                  "Vardiya degisimi icin doldurulan belgeyi soran her cerceve "
                  "ayni bilesigi uretiyor. E6 onerisi: belge yerine 48 saatlik "
                  "onceden bildirim suresine capalanmis yuva.",

    (GT1_NC, 20): ORTAK_NOT + "Model 'booking system / staff portal' verdi. "
                  "'Cevrimici ___ uzerinden izin talebi' cercevesi kavrami "
                  "veriyor. 15. sorunun duzeltilmesiyle bu iki bosluk artik "
                  "birbirini kismen kisitliyor (noticeboard - portal), ama "
                  "sozcuk duzeyi sizintisi kapanmiyor. E6 onerisi: iki "
                  "haftalik asgari sureye capalanmis yuva.",

    (AC3_TC, 3): ORTAK_NOT + "Model uc turda 'dye' verdi. Ayna testinde deriye "
                 "uygulanan zararsiz isareti soran her cerceve boya kavramini "
                 "veriyor. E6 onerisi: isaretin turu yerine konuldugu yere "
                 "(goz ya da kulak arkasi) capalanmis yuva.",

    (GT2_TC, 15): ORTAK_NOT + "Model 'a visa / sponsorship' verdi. On hafta "
                  "boyunca calisma hakki kosulunu soran her cerceve ayni "
                  "kavrami veriyor. E6 onerisi: calisma hakki yerine uygun "
                  "lisans programi kosuluna (ekonomi, muhasebe, isletme) "
                  "capalanmis yuva.",
}

# --------------------------------------------------------------------------
# 4) stem_block / kelime bankasi degisiklikleri
# --------------------------------------------------------------------------

STEM = {
    P_SUM: [(
        "Drinks were handled separately, every household keeping a week-long "
        "(10) ........ of what was poured away and how much of it.",
        "Drinks were handled separately: instead of being weighed by the team, "
        "everything poured away was entered by the household itself in a "
        "seven-day (10) ........ , type and quantity alike.",
    )],
    AC1_NC: [(
        "- He recalled where the cube lay after it had been hidden round a "
        "(5) ........",
        "- He recalled where the cube lay after it had been moved out of "
        "sight, past a (5) ........ and into a walled passage",
    )],
    AC2_FC: [(
        "The Near-Infrared Camera records ten long exposures, each of "
        "(1) ........ , while a faint speck is followed against the star "
        "background for roughly six hours.",
        "The Near-Infrared Camera records a run of long exposures, each of "
        "(1) ........ , as a faint speck is followed against the background of "
        "stars.",
    )],
    AC4_SUM: [
        ("while the other met them at the start of the day and stayed "
         "(37) ........ until an evening test.",
         "while the other met them at the start of the day and remained "
         "(37) ........ until an evening test."),
        ("Where no such link existed, the two produced almost (39) ........ .",
         "Where no such link existed, however, the picture changed: the two "
         "turned out to offer (39) ........ ."),
        ("Neither how long a rest ran nor which stages it contained predicted "
         "the size of the gain, which suggests that simply getting "
         "(40) ........ counted for more than the internal shape of that "
         "sleep.",
         "Neither how long a rest ran nor which stages it contained predicted "
         "the size of the gain; what counted, the authors argue, was "
         "(40) ........ rather than anything about the internal shape of the "
         "sleep."),
    ],
    GT1_NC: [
        ("- The pattern changes every four weeks; the new one is put up on the "
         "staff (15) ........ by the Friday before at the latest",
         "- The pattern changes every four weeks; the new one appears on the "
         "staff (15) ........ by the Friday before at the latest"),
        ("- Colleagues in one team do not stop at the same moment - their "
         "breaks are (16) ........ so that no line is left with nobody on it",
         "- Within a team, breaks are (16) ........ ; the rule exists to "
         "protect the production lines"),
    ],
    GT1_SUM: [(
        "For the authors, the lesson is that policy has so far dealt with "
        "collecting and disposing of waste rather than its (40) ........ , and "
        "that campaigns need to name the particular foods concerned.",
        "For the authors, the lesson is that policy has so far dealt with "
        "collecting and disposing of waste; real (40) ........ , they argue, "
        "will depend on campaigns that name the particular foods concerned.",
    )],
    GT2_SUM: [
        ("Once the strength of the earnings route was measured, though, it "
         "turned out to carry only (37) ........ of the overall link, and the "
         "rest ran through something the income figures could not reach.",
         "Once the strength of the earnings route was measured, though, it "
         "emerged that income carried (37) ........ of the overall link, with "
         "the remainder running through something the income figures could not "
         "reach."),
        ("The team then repeated the analysis with narrower samples, with "
         "different thresholds for how often someone had to help out before "
         "they were classed as a volunteer, and with extra background "
         "variables added, and the outcome stayed (38) ........ throughout.",
         "The team then repeated the analysis with narrower samples, with "
         "different thresholds for how often someone had to help out before "
         "they were classed as a volunteer, and with extra background "
         "variables added; across those versions the picture was "
         "(38) ........ ."),
        ("For the greater share of the effect that money cannot account for, "
         "the authors have (39) ........ rather than firm answers: a stronger "
         "sense of purpose and belonging, the walking and standing that "
         "helping often involves, or a possible influence on the hormones that "
         "govern stress.",
         "For the greater share of the effect that money cannot account for, "
         "the authors offer (39) ........ : a stronger sense of purpose and "
         "belonging, the walking and standing that helping often involves, or "
         "an influence on the hormones that govern stress."),
        ("They are equally cautious about the finding as a whole, noting that "
         "people who choose to give their time may already be unlike those who "
         "do not in their spare hours, their starting health or their "
         "sociability; what the study demonstrates is therefore (40) ........ ,"
         " and settling the matter would require a trial in which the chance "
         "to volunteer was handed out at random.",
         "Turning to the finding as a whole, the authors describe what they "
         "have shown as (40) ........ ."),
    ],
}

# kelime bankasinda YALNIZ celdirici metinleri degisir; hicbir dogru
# secenegin harfi ya da metni degismez.
BANKA = {
    AC4_SUM: {
        "E": ("deeper sleep", "an unbroken night"),
        "H": ("the length of the nap", "in the laboratory"),
    },
}


def stem_uygula(veri, yol):
    n = 0
    for eski, yeni in STEM.get(yol, []):
        blok = veri.get("stem_block") or ""
        if yeni in blok:
            continue
        if eski not in blok:
            # tire karakteri farkli olabilir; en-dash denemesi
            alt = eski.replace(" - ", " — ")
            if alt in blok:
                eski = alt
            else:
                raise SystemExit("stem_block parcasi bulunamadi: %s\n  %r"
                                 % (yol, eski[:60]))
        veri["stem_block"] = blok.replace(eski, yeni)
        n += 1
    return n


def banka_uygula(veri, yol):
    n = 0
    for harf, (eski, yeni) in BANKA.get(yol, {}).items():
        for o in veri.get("word_bank") or []:
            if o.get("letter") != harf:
                continue
            if o["text"] == yeni:
                continue
            if o["text"] != eski:
                raise SystemExit("banka metni beklenenden farkli: %s %s"
                                 % (yol, harf))
            o["text"] = yeni
            n += 1
    return n


def main():
    d_say = e_say = n_say = s_say = b_say = 0

    for yol in DOSYALAR:
        veri = ortak.oku(yol)
        s_say += stem_uygula(veri, yol)
        b_say += banka_uygula(veri, yol)

        for it in ortak.sorular(veri):
            anahtar = (yol, it["number"])

            if anahtar in DUZELTME:
                y = DUZELTME[anahtar]
                onceki = it.get("revision", {}).get("onceki_prompt") \
                    or it["prompt"]
                it["prompt"] = y["prompt"]
                it["explanation"] = y["explanation"]
                it["status"] = "verified"
                it["blind_solvable"] = None
                it["revision"] = {
                    "tarih": TARIH,
                    "mekanizma": MEK,
                    "onceki_prompt": onceki,
                    "ne_degisti": y["ne_degisti"],
                }
                d_say += 1

            elif anahtar in ELEME:
                it["status"] = "rejected"
                it["reject_reason"] = ELEME[anahtar]
                e_say += 1

            elif anahtar in DOKUNMA:
                it["review_note"] = DOKUNMA[anahtar]
                n_say += 1

        ortak.yaz(yol, veri)

    print("duzeltildi %d - elendi %d - dokunulmadi %d" % (d_say, e_say, n_say))
    print("stem_block parcasi guncellendi: %d" % s_say)
    print("kelime bankasi celdiricisi guncellendi: %d" % b_say)
    bekleniyor = (len(DUZELTME), len(ELEME), len(DOKUNMA))
    if (d_say, e_say, n_say) != bekleniyor:
        raise SystemExit("BEKLENEN SAYI TUTMADI: %s" % (bekleniyor,))


if __name__ == "__main__":
    main()
