# -*- coding: utf-8 -*-
"""OPUS5-E6 6. calistirma: tamamlama ailesinin elenen yuvalarini yeniden doldurur.

Kapsam: sentence / summary / note / table / flow-chart completion (34 yuva).
Her yuva ayni dosyaya ayni numarayla yazilir; hicbir soru silinmez.

Kullanim: python tools/_e6_comp_uret.py
"""
import io
import json
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARIH = "2026-08-08"
KAYNAK = "prompts/OPUS5-E6-yeniden-uretim.md (6/7)"
GRUP = "Tamamlama ailesi yuvalari"

TEMIZLENEN = ("flag_reason", "flag_mechanism", "reject_reason", "review_note",
              "revision", "blind_solvable_kelime_duzeyi")


def y(prompt, answer, kabul, kanit, par, cum, aciklama, zorluk, ne_degisti):
    return {"prompt": prompt, "answer": answer, "accepted_variants": kabul,
            "evidence": kanit, "paragraph": par, "sentence": cum,
            "explanation": aciklama, "difficulty": zorluk,
            "ne_degisti": ne_degisti}


YENI = {}

# --------------------------------------------------------------- A01 (practice)
YENI[("content/reading/practice/sentence-completion.json", 1)] = y(
    "Questions 1-3 refer to Passage A01. Each animal was tested by itself in an "
    "enclosure where a heavy (1) ........ had already been placed.",
    ["concrete cube"], ["concrete cube"],
    "Each was tested alone in an enclosure that already contained a heavy concrete cube.",
    "B", 2,
    "Paragraph B says each elephant was tested alone in an enclosure that already "
    "contained a heavy concrete cube; so the answer is 'concrete cube'.",
    "easy",
    "Eski soru A/2'deki laboratuvar ornekleri cumlesine capaliydi ve cevap ('swat "
    "flies') hayvan davranisi kulturunun en cok tekrarlanan ayrintisiydi. Yeni yuva "
    "A paragrafina hic degmiyor: kanit B/2'ye, duzenegin fiziksel kurulumuna tasindi. "
    "Enclosure'da onceden duran nesnenin ne oldugu yalniz metinden okunur; disaridan "
    "kutu, kova, sandik gibi bircok aday esit derecede akla gelir.")

YENI[("content/reading/practice/sentence-completion.json", 3)] = y(
    "After a spell of apparently unrelated activity, Kandula rolled the block "
    "(3) ........ across the enclosure until it stood beneath the branch he could not reach.",
    ["several metres"], ["several metres", "several meters"],
    "After a period of apparently unrelated activity, he walked over to the concrete "
    "cube, rolled it several metres across the enclosure until it sat beneath the "
    "dangling branch, climbed onto it with his front feet and used his trunk to take the food.",
    "C", 3,
    "Paragraph C says Kandula rolled the cube several metres across the enclosure "
    "until it sat beneath the dangling branch; so the answer is 'several metres'.",
    "medium",
    "Eski soru H/2'ye capaliydi ve cevap tek sozcuktu ('anatomy'); model parcasiz uc "
    "turun ikisinde birebir, birinde tam es anlamlisiyla ('morphology') verdi, cunku "
    "'cihaz turun X'ine uymuyordu' cercevesi kavrami zorunlu kiliyordu. Yeni yuva H "
    "paragrafina hic degmiyor: kanit C/3'e, cozumun fiziksel ayrintisina tasindi. "
    "Blogun kac metre itildigi olculebilir ve keyfi bir ayrinti; disaridan bilinemez. "
    "Cerceve 'cube' sozcugunu anmiyor, boylece 1. sorunun cevabini da sizdirmiyor.")

# --------------------------------------------------------------- A02 (AC1)
YENI[("content/reading/tests/AC1/sentence-completion.json", 22)] = y(
    "Each reunion on the seventh day again ran for (22) ........ , and the same "
    "behaviours were recorded as in the earlier phase.",
    ["fifteen minutes"], ["fifteen minutes", "15 minutes"],
    "Each reunion again lasted fifteen minutes, and the same behaviours were recorded "
    "as in the earlier cohabitation phase.",
    "E", 4,
    "Paragraph E says each reunion again lasted fifteen minutes, with the same "
    "behaviours recorded as in the cohabitation phase; so the answer is 'fifteen minutes'.",
    "easy",
    "Eski soru H/2'ye capaliydi ve cevap yerlesik bir literatur terimiydi ('dear "
    "enemy' etkisi); cumle terimin tanimini verdigi icin ifade nasil yazilirsa "
    "yazilsin ayni unlu adi cagiriyordu. Yeni yuva H paragrafina hic degmiyor: kanit "
    "E/4'e, yedinci gun yapilan bulusmalarin suresine tasindi. Sure calismanin kendi "
    "tasarim ayrintisi; pasaj disindan bilinemez.")

# --------------------------------------------------------------- A03 (AC1 ozet)
YENI[("content/reading/tests/AC1/summary-completion.json", 36)] = y(
    "Magma still lies beneath the seafloor and, along the (36) ........ of the caldera, "
    "drives shallow vents that release carbon dioxide straight into the water beside a "
    "living reef, a combination found almost nowhere else on Earth.",
    ["inner shoreline"], ["inner shoreline", "inner shore"],
    "Magma still sits beneath the seafloor, and along the inner shoreline of the "
    "caldera it drives shallow vents that continuously release carbon dioxide gas "
    "directly into the water beside a living coral reef, a combination that is "
    "extremely rare anywhere on Earth.",
    "B", 3,
    "Paragraph B says magma beneath the seafloor drives shallow vents along the inner "
    "shoreline of the caldera; so the answer is 'inner shoreline'.",
    "medium",
    "Eski soru B/2'ye capaliydi ve cevap yerlesik bir jeoloji terimiydi ('caldera'); "
    "ozet cumlesi terimin tanimini veriyordu. Yeni yuva B/2'ye hic degmiyor: kanit "
    "B/3'e, bacalarin kaldera icinde tam olarak nerede siralandigi ayrintisina "
    "tasindi. Konum bilgisi yalniz metinden okunur, terim bilgisinden cikmaz.")

YENI[("content/reading/tests/AC1/summary-completion.json", 38)] = y(
    "Reef scientists' wider worry is that corals may lose the contest for space, and "
    "that complex reef habitat will gradually give way to simpler (38) ........ .",
    ["algal turf"], ["algal turf"],
    "This pattern matches a broader concern among reef scientists: that as oceans "
    "acidify, algae may increasingly outcompete corals for space, gradually replacing "
    "complex reef habitat with simpler algal turf.",
    "F", 3,
    "Paragraph F says reef scientists fear that algae will outcompete corals for space, "
    "gradually replacing complex reef habitat with simpler algal turf; so the answer "
    "is 'algal turf'.",
    "hard",
    "Eski soru F/2'ye capaliydi; cevap ('weedy algae') hem iklim habercileri "
    "tarafindan surekli tekrarlanan bir oruntuydu hem de kabul listesi 'algae' "
    "sozcugunu tek basina kabul ediyordu. Yeni yuva F/2'ye hic degmiyor: kanit F/3'e, "
    "arastirmacilarin genel kaygisini anlatan cumleye tasindi ve cerceveden 'algae' "
    "sozcugu bilerek cikarildi, boylece bosluk artik yakin bir es anlamliyi "
    "cagirmiyor. Kabul listesi tek bicime indirilmedi, bastan tek bicimli yazildi.")

YENI[("content/reading/tests/AC1/summary-completion.json", 39)] = y(
    "A second piece of research, published in the journal (39) ........ , looked at what "
    "happens inside the coral skeletons rather than on the seafloor surface.",
    ["PLOS ONE"], ["PLOS ONE", "PLoS ONE", "PLOS One"],
    "A related study of the Maug reef, published separately in the journal PLOS ONE, "
    "focused on what happens inside coral skeletons rather than on the seafloor surface.",
    "G", 1,
    "Paragraph G says a related study of the Maug reef was published in the journal "
    "PLOS ONE and looked inside coral skeletons rather than at the seafloor surface; "
    "so the answer is 'PLOS ONE'.",
    "medium",
    "Eski soru G/2'ye capaliydi ve cevap yerlesik bir deniz biyolojisi terimiydi "
    "('bioerosion'); ozet cumlesi terimin sozluk tanimini veriyordu. Yeni yuva G/2'ye "
    "hic degmiyor: kanit G/1'e, ikinci calismanin yayimlandigi derginin adina tasindi. "
    "Dergi adi keyfi bir kunye bilgisi; tanimdan turetilemez.")

# --------------------------------------------------------------- A04 (practice)
YENI[("content/reading/practice/sentence-completion.json", 10)] = y(
    "Questions 10-12 refer to Passage A04. A faint point of light was tracked against "
    "the background stars over a stretch of roughly (10) ........",
    ["six hours"], ["six hours", "6 hours"],
    "On 2 February 2025, Webb's Near-Infrared Camera captured a series of ten "
    "long-exposure images, each lasting forty minutes, over a period of roughly six "
    "hours, tracking a faint point of light moving against the background of stars in "
    "a pattern consistent with an object orbiting Uranus itself.",
    "B", 2,
    "Paragraph B says the faint point of light was tracked against the background of "
    "stars over a period of roughly six hours; so the answer is 'six hours'.",
    "easy",
    "Eski soru A/1'e capaliydi ve cevap ('seventh') temel astronomi bilgisiydi; soru "
    "kokunun kendisi de dunya bilgisini cagiriyordu. Yeni yuva A paragrafina hic "
    "degmiyor: kanit B/2'ye, gozlem penceresinin uzunluguna tasindi. Bu sure yalniz "
    "gozlem kaydindan okunur. Pozlarin sayisi (on) ve tek poz suresi (kirk dakika) "
    "bilerek cerceveye alinmadi, boylece aritmetikle turetilemiyor.")

YENI[("content/reading/practice/sentence-completion.json", 11)] = y(
    "No permanent name has been agreed yet, so the moon is listed under the "
    "provisional label (11) ........",
    ["S/2025 U1"], ["S/2025 U1"],
    "The newly found body has been given the provisional designation S/2025 U1.",
    "C", 1,
    "Paragraph C says the newly found body has been given the provisional designation "
    "S/2025 U1; so the answer is 'S/2025 U1'.",
    "medium",
    "Eski soru F/3'e capaliydi ve sizinti aritmetikti: cumle 1986 ucusunu veriyordu, "
    "gunumuz tarihi disaridan biliniyordu, fark dogrudan 'forty years' ediyordu. Yeni "
    "yuva F paragrafina hic degmiyor: kanit C/1'e tasindi. Bu yuvada istenen sey "
    "adlandirma gelenegi degil (E5 AC2-2'yi tam da onun icin elemisti) kodun "
    "kendisidir; S/2025 U1 dizisi pasaj disindan hicbir bicimde turetilemez.")

YENI[("content/reading/practice/sentence-completion.json", 12)] = y(
    "Its orbit lies about (12) ........ from the centre of Uranus, in a gap between two "
    "moons that were already known.",
    ["56,000 kilometres"],
    ["56,000 kilometres", "56,000 kilometers", "56,000 km", "35,000 miles"],
    "Its orbit lies roughly 35,000 miles, or 56,000 kilometres, from the centre of "
    "Uranus, in the gap between two previously known moons, Ophelia and Bianca.",
    "D", 1,
    "Paragraph D says the orbit lies roughly 35,000 miles, or 56,000 kilometres, from "
    "the centre of Uranus, in the gap between two previously known moons; so the "
    "answer is '56,000 kilometres' (or the same distance in miles).",
    "medium",
    "Eski soru H/1'e capaliydi; model parcasiz uc turda da 'preliminary' vererek "
    "cevabin ('ongoing research') butun icerigini karsiladi, cunku 'hakem "
    "degerlendirmesinden gecmemis bulgu' kavraminin hazir bir Ingilizce karsiligi "
    "var. Yeni yuva H paragrafina hic degmiyor: kanit D/1'e, yorungenin gezegen "
    "merkezine uzakligina tasindi. Sayi olculmus bir buyukluk; kavramdan turetilemez.")

# --------------------------------------------------------------- A04 (AC2 akis semasi)
YENI[("content/reading/tests/AC2/flow-chart-completion.json", 2)] = y(
    "The speck is accepted as a body circling Uranus, a moon that no earlier mission "
    "had recorded, and the addition to the planet's family is announced in (2) ........ .",
    ["February 2025"], ["February 2025", "in February 2025"],
    "In February 2025, astronomers added one more member to that family: a small moon "
    "so faint that no previous mission had ever recorded it, spotted only because a "
    "modern space telescope was powerful enough to catch its dim reflected light.",
    "A", 2,
    "Paragraph A says that in February 2025 astronomers added one more member to "
    "Uranus's family of moons; so the answer is 'February 2025'.",
    "easy",
    "Eski kutu C/1'e capaliydi ve cevap ('designation') adlandirma gelenegini bilmekten "
    "cikiyordu. Yeni kutu C/1'e hic degmiyor: kanit A/2'ye, duyurunun tarihine tasindi. "
    "Kutudan S/2025 U1 kodu da kaldirildi, cunku kod yilin kendisini tasiyordu; tarih "
    "artik yalniz A/2'den okunuyor.")

YENI[("content/reading/tests/AC2/flow-chart-completion.json", 3)] = y(
    "Too faint to be measured directly, the object has its width put at about "
    "(3) ........ , which makes it one of the smallest moons known anywhere.",
    ["ten kilometres"],
    ["ten kilometres", "ten kilometers", "10 kilometres", "10 km", "six miles"],
    "Because it has not been imaged in enough detail to measure directly, its size has "
    "to be estimated: assuming it reflects light in a similar way to Uranus's other "
    "small moons, astronomers calculate a diameter of about six miles, or ten "
    "kilometres, making it one of the smallest moons known anywhere in the solar system.",
    "C", 2,
    "Paragraph C says astronomers calculate a diameter of about six miles, or ten "
    "kilometres, making it one of the smallest moons known; so the answer is 'ten "
    "kilometres' (or the same figure in miles).",
    "medium",
    "Eski kutu ayni cumleye capaliydi ama bosluk 'it ___ light' kalibinin ortasindaydi "
    "ve parlakliktan cap tahmini Ingilizcede yalniz 'reflect' fiiliyle kuruluyordu. "
    "E5'in kendi onerisi uyarinca bosluk ayni cumlenin OLCULEN degerine tasindi: "
    "varsayimin fiili artik sorulmuyor, sorulan sey hesaplanan capin kendisi. Sizdiran "
    "oge (fiil kalibi) cerceveden tumuyle kalkti; yeni hedefin disaridan turetilebilir "
    "bir karsiligi yok.")

YENI[("content/reading/tests/AC2/flow-chart-completion.json", 6)] = y(
    "The team lead's comment: an object that slipped past even a (6) ........ shows how "
    "much of a well-studied planetary system may still lie hidden.",
    ["dedicated flyby mission"], ["dedicated flyby mission"],
    "As El Moutamid noted, the moon is small, but finding something that even a "
    "dedicated flyby mission missed underlines how much of even a well-studied "
    "planetary system can still remain hidden from view.",
    "H", 2,
    "Paragraph H quotes the team lead as saying that finding something even a "
    "dedicated flyby mission missed shows how much of a well-studied planetary system "
    "can remain hidden; so the answer is 'dedicated flyby mission'.",
    "hard",
    "Eski kutu E/2'ye capaliydi ve cevap bir ozel ad ve dunya bilgisiydi (gok cismi "
    "adlarini onaylayan kurum). Ayni cumlenin oteki yarisi (Shakespeare ve Pope "
    "gelenegi) da ayni olcude taniniyor, o yuzden E/2 tumuyle birakildi ve akis "
    "semasinin son adimi adlandirmadan cikarildi; sema basligi da buna gore "
    "degistirildi. Kanit H/2'ye, ekip liderinin degerlendirmesine tasindi.")

# --------------------------------------------------------------- A06 (practice not)
YENI[("content/reading/practice/note-completion.json", 1)] = y(
    "Sample: (1) ........ employee-month records in all, from a single department, "
    "April 2022 to March 2023",
    ["977"], ["977"],
    "A team of researchers analysed 977 employee-month records from one of the "
    "company's departments, covering April 2022 through March 2023.",
    "B", 1,
    "Paragraph B says the researchers analysed 977 employee-month records from one "
    "department, covering April 2022 through March 2023; so the answer is '977'.",
    "easy",
    "Eski not satiri A/2'ye capaliydi ve cevap ('47') cografya ders kitabi duzeyinde "
    "bir dunya bilgisiydi; 'prefecture' sozcugu tek basina Japonya'yi adlandirdigi "
    "icin cerceve duzeltmesi de yetmiyordu. Yeni satir A paragrafina hic degmiyor: "
    "kanit B/1'e, orneklem buyukluguna tasindi. 977 keyfi bir kayit sayisi, disaridan "
    "bilinemez.")

# --------------------------------------------------------------- A09 (practice not)
YENI[("content/reading/practice/note-completion.json", 10)] = y(
    "Vitrified tissue: axons averaging (10) ........ nanometres across, roughly the "
    "range found in living white matter",
    ["717.7"], ["717.7"],
    "Axons in the vitrified brain tissue measured on average 717.7 nanometres in "
    "diameter, close to the typical range for white matter in a living brain, while "
    "axons from the preserved spinal cord measured around 672 nanometres.",
    "E", 2,
    "Paragraph E says axons in the vitrified brain tissue measured on average 717.7 "
    "nanometres in diameter, close to the typical range for white matter in a living "
    "brain; so the answer is '717.7'.",
    "medium",
    "Eski not satiri A/2'ye capaliydi ve cevap ('500') volkanoloji anlatilarinin "
    "standart rakamiydi; satirin kendisi zaten o genel gercegin ifadesiydi. Yeni satir "
    "A paragrafina hic degmiyor: kanit E/2'ye, olculen akson capina tasindi. Ondalikli "
    "olcum degeri pasaj disindan turetilemez. Ayni A paragrafinin oteki adaylari da "
    "(AD 79, yaklasik 20 metrelik gomulme) bilinen rakamlar oldugu icin bilerek "
    "kullanilmadi.")

# --------------------------------------------------------------- A10 (practice ozet)
YENI[("content/reading/practice/summary-completion.json", 1)] = y(
    "Both the zoned open-plan room and the team office beat the plain open-plan "
    "baseline on how content the staff felt and on how productive they believed "
    "themselves to be, while the activity-based arrangement finished below the "
    "baseline on both counts, with scores about (1) ........ per cent lower.",
    ["14"], ["14"],
    "The activity-based design, despite its popularity in contemporary office trends, "
    "performed worse than the open-plan baseline on both measures, with satisfaction "
    "and productivity scores roughly 14 per cent lower.",
    "D", 3,
    "Paragraph D says the activity-based design scored roughly 14 per cent lower than "
    "the open-plan baseline on both satisfaction and productivity; so the answer is "
    "'14 per cent'.",
    "medium",
    "Eski bosluk ayni cumleye capaliydi ama hedefi 'moda olmasina ragmen kotu sonuc "
    "verdi' karsitligiydi ve o karsitligi tasiyan her cumlede boslugun tek dogal "
    "sozcugu 'popularity' oluyordu. E5'in kendi onerisi uyarinca bosluk ayni cumlenin "
    "OLCULEN degerine tasindi ve karsitlik ibaresi ('for all its ... in current office "
    "fashion') cerceveden tumuyle cikarildi. Yuzde 14'luk dusus calismanin kendi "
    "sayisi; disaridan tahmin edilemez.")

YENI[("content/reading/practice/summary-completion.json", 2)] = y(
    "The same two layouts also came top for flow, the zoned room scoring (2) ........ "
    "per cent above the plain baseline and the team office 12 per cent above it, which "
    "suggests that partial enclosure aids lasting concentration.",
    ["15"], ["15"],
    "Employees in team offices reported flow scores 12 per cent higher than those in "
    "the open-plan condition, and employees in the zoned open-plan design reported "
    "flow scores 15 per cent higher, suggesting that both partly enclosed layouts "
    "allowed for more sustained concentration than either the fully open or the fully "
    "unassigned arrangement.",
    "E", 2,
    "Paragraph E says flow scores were 12 per cent higher in team offices and 15 per "
    "cent higher in the zoned open-plan design; since the gap concerns the zoned room, "
    "the answer is '15'.",
    "medium",
    "Eski bosluk E/1'e capaliydi ve cevap ('absorbed') ozetin verdigi tanimin standart "
    "sozcuguydu; tanimi cikarmak da boslugu cok cevapli yapiyordu. Yeni bosluk E/1'e "
    "hic degmiyor: kanit E/2'ye, iki duzenin flow farkina tasindi ve 'flow' teriminin "
    "tanimi ozetten tumuyle kaldirildi. Iki yuzdeden biri cerceve icinde verildigi "
    "icin soru olculebilir kaliyor, ama istenen sayi disaridan turetilemiyor.")

# --------------------------------------------------------------- A10 (AC4 not)
YENI[("content/reading/tests/AC4/note-completion.json", 4)] = y(
    "How the layouts were judged: Repeated staff surveys covering satisfaction, "
    "engagement, (4) ........ , energy, flow and how productive people felt",
    ["enjoyment"], ["enjoyment"],
    "Employees completed regular questionnaires measuring satisfaction, engagement, "
    "enjoyment, sense of energy, flow, and perceived productivity.",
    "C", 2,
    "Paragraph C lists the things the regular questionnaires measured: satisfaction, "
    "engagement, enjoyment, sense of energy, flow and perceived productivity; the "
    "missing item is 'enjoyment'.",
    "medium",
    "Eski satir C/4'e capaliydi ve cevap ('headphones') gurultu uzerine bir ofis "
    "calismasinda akla gelen ilk nesneydi; ayni cumledeki oteki ornekler de (sessiz "
    "koseler, ayakustu sohbetler) ayni olcude tahmin edilebilirdi, yani hedefi cumle "
    "icinde kaydirmak ise yaramiyordu. Yeni satir C/4'e hic degmiyor: kanit C/2'ye, "
    "anketin olctugu alt boyutlarin listesine tasindi. ONE WORD ONLY sinirinda kalan "
    "tek pasaja ozgu aday buydu; kod commit sayimi da C/4 icinde oldugu icin "
    "kullanilamadi.")

# --------------------------------------------------------------- A11 (AC4 cumle)
YENI[("content/reading/tests/AC4/sentence-completion.json", 20)] = y(
    "Reaching the campus viewpoint took the volunteers only ........ , against the "
    "five-minute walk out to the trees.",
    ["two minutes"], ["two minutes", "2 minutes"],
    "In the comparison condition, participants instead walked two minutes to a spot on "
    "campus where they spent 15 minutes viewing nearby buildings, an environment the "
    "researchers deliberately chose to be calm and free of traffic rather than "
    "obviously stressful.",
    "C", 2,
    "Paragraph C says participants walked two minutes to the campus spot, against the "
    "five-minute walk to the forest stand; so the answer is 'two minutes'.",
    "easy",
    "Eski soru D/1'e capaliydi; bosluk yuzde olarak verilen bir hava olcumunu "
    "istiyordu ve pasajin dort degerinden yalnizca biri yuzdeyle ifade edildigi icin "
    "birimin kendisi cevabi veriyordu. Yeni soru D/1'e hic degmiyor: kanit C/2'ye, "
    "karsilastirma kosuluna yurume suresine tasindi. Sure keyfi bir tasarim ayrintisi; "
    "birim ipucu tasimiyor cunku iki sure de dakika cinsinden ve biri cercevede veriliyor.")

YENI[("content/reading/tests/AC4/sentence-completion.json", 21)] = y(
    "The Profile of Mood States, a ........ scale, covered six mood dimensions, among "
    "them fatigue and vigour.",
    ["65-item"], ["65-item", "65 item"],
    "The Profile of Mood States, a 65-item scale, measured six mood dimensions "
    "including tension, anger, depression, fatigue, confusion and vigour.",
    "E", 2,
    "Paragraph E says the Profile of Mood States is a 65-item scale measuring six mood "
    "dimensions; so the answer is '65-item'.",
    "medium",
    "Eski soru E/5'e capaliydi ve bosluk 'the passage of time' kaliplasmis obeginin "
    "icinde duruyordu; kalip yerinde kaldigi surece tek tamamlamasi vardi. Yeni soru "
    "E/5'e hic degmiyor: kanit E/2'ye, olcegin madde sayisina tasindi. Madde sayisi "
    "arac kunyesine ait bir sayi ve cerceve hicbir kalibin icinde degil.")

YENI[("content/reading/tests/AC4/sentence-completion.json", 22)] = y(
    "The 22 students who volunteered, all of them healthy and half of them women, had "
    "an average age of ........ .",
    ["22.5"], ["22.5"],
    "To investigate, researchers recruited 22 healthy university students, 11 women "
    "and 11 men, with an average age of 22.5, from a university of applied sciences in "
    "southern Finland.",
    "B", 1,
    "Paragraph B says the 22 students recruited, 11 women and 11 men, had an average "
    "age of 22.5; so the answer is '22.5'.",
    "easy",
    "Eski soru H/1'e capaliydi; model parcasiz uc turun ikisinde birebir 'vegetation', "
    "birinde tam es anlamlisi 'foliage' verdi, cunku 'kalin kar neyi gizler' sorusunun "
    "Ingilizcede birden cok es adi var. Yeni soru H paragrafina hic degmiyor: kanit "
    "B/1'e, orneklemin ortalama yasina tasindi. Ondalikli ortalama disaridan "
    "turetilemez ve es anlamli bir karsiligi yok.")

# --------------------------------------------------------------- A12 (AC4 ozet)
YENI[("content/reading/tests/AC4/summary-completion.json", 36)] = y(
    "In the earlier one, different volunteers were placed in a sleeping group and a "
    "waking group, while in the later one the same volunteers met both conditions on "
    "different days, each spending half an hour on (36) ........ before the final test "
    "so that grogginess would not distort it.",
    ["J"], ["J", "a puzzle game", "puzzle game"],
    "To reduce the grogginess that can follow a nap and distort test performance, all "
    "participants completed a 30-minute puzzle game before their final recall test.",
    "D", 3,
    "Paragraph D says all participants completed a 30-minute puzzle game before the "
    "final recall test, to reduce grogginess; so the correct option is J.",
    "medium",
    "Eski bosluk B/2'ye capaliydi ve 'within-subject' terimini hedefliyordu; cumlenin "
    "kendisi terimin tek tanimini veriyor, bankadaki karsit terim de elemeyle "
    "cikiyordu. Yeni bosluk B/2'ye hic degmiyor: kanit D/3'e, sersemligi azaltmak icin "
    "uygulanan otuz dakikalik etkinlige tasindi (E5'in onerisi). Iki desen adi da "
    "bankadan cikarildi ve ikinci deneyin tasarimi artik BOSLUKSUZ metinde anlatiliyor, "
    "yani tanim sizintisi kaynagindan kaldirildi. Bankaya iki gercek rakip eklendi "
    "('a quiet walk', ayrica 'in the laboratory' de bu cerceveye oturuyor).")

YENI[("content/reading/tests/AC4/summary-completion.json", 38)] = y(
    "The naps themselves ran to an average of (38) ........ and were made up for the "
    "most part of a lighter stage of sleep.",
    ["D"], ["D", "64.1 minutes"],
    "Naps in the second experiment lasted an average of 64.1 minutes and consisted "
    "mainly of Stage 2 sleep, a lighter stage than the deep sleep typically associated "
    "with the middle of a full night.",
    "F", 1,
    "Paragraph F says naps in the second experiment lasted an average of 64.1 minutes "
    "and consisted mainly of Stage 2 sleep; so the correct option is D.",
    "medium",
    "Eski bosluk E/2'ye capaliydi ve secim, uykunun anlamca iliskili malzemeyi daha "
    "cok kayirdigi yolundaki bilissel bilim bilgisine iniyordu; banka da bu ekseni "
    "hazir bir zit cift olarak tasiyordu. Yeni bosluk E/2'ye hic degmiyor: kanit "
    "F/1'e, sekerlemelerin gercekte ne kadar surdugune tasindi. Iki kutuplu anlam "
    "cifti bankadan cikarildi; yerine olculebilir bir sure ve ona gercek bir rakip "
    "kondu ('an hour and a half'), cunku planlanan sure ile gerceklesen ortalama "
    "birbirinden farkli ve ozet planlanan sureyi artik anmiyor.")

# --------------------------------------------------------------- G03 (GT1)
YENI[("content/reading/tests/GT1/note-completion.json", 19)] = y(
    "Exchanging a shift: Both workers still have to meet their weekly hours, and a "
    "swap leaving under (19) ........ of rest between shifts is always refused",
    ["eleven hours"], ["eleven hours", "11 hours"],
    "Both employees remain responsible for meeting their required weekly hours, and "
    "swaps that would leave fewer than eleven hours' rest between shifts will not be "
    "approved.",
    "D", 2,
    "Text A, paragraph D says swaps that would leave fewer than eleven hours' rest "
    "between shifts will not be approved; so the answer is 'eleven hours'.",
    "medium",
    "Eski satir B metni A/1'e capaliydi ve cevap ('28 days') hukukla sabitlenmis bir "
    "sayiydi; satir kosullarin ikisini birden verdigi icin sayi disaridan cikiyordu. "
    "Yeni satir o cumleye hic degmiyor: kanit A metni D/2'ye, vardiya degisimi "
    "kuralinin ikinci kosuluna tasindi ve satir 18. yuvanin dayandigi D/1'i tekrar "
    "etmiyor. Not bloguna yeni bir bosluk eklenmedi, var olan bolum bir satir "
    "genisletildi; bosluk sirasi 15-20 olarak korundu.")

YENI[("content/reading/tests/GT1/sentence-completion.json", 26)] = y(
    "Hours worked beyond the (26) ........ week are always paid at one and a half times "
    "the standard hourly rate.",
    ["37.5-hour"], ["37.5-hour", "37.5 hour"],
    "Overtime is paid at 1.5 times the standard hourly rate for hours worked beyond "
    "the 37.5-hour week, and at double time for work on public holidays.",
    "C", 1,
    "Text B, paragraph C says overtime is paid at 1.5 times the standard rate for "
    "hours worked beyond the 37.5-hour week; so the answer is '37.5-hour'.",
    "medium",
    "Eski bosluk ayni cumleye capaliydi ama hedefi 'double time' idi: resmi tatil "
    "calismasinin karsiligi Ingiliz is dunyasinin yerlesik terimi ve cumle bir bucuk "
    "kat karsitligini vererek terimi dogrudan cagiriyordu. E5'in kendi onerisi "
    "uyarinca bosluk ayni cumlenin ESIK degerine tasindi; resmi tatil / cift ucret "
    "karsitligi cerceveden tumuyle cikarildi, yani sizdiran oge kaldirildi. Haftalik "
    "esik sirkete ozgu bir sayi.")

YENI[("content/reading/tests/GT1/sentence-completion.json", 27)] = y(
    "Anyone who builds up more than (27) ........ of overtime in a single month may take "
    "the excess as time off instead of pay.",
    ["ten hours"], ["ten hours", "10 hours"],
    "Staff who accumulate more than ten hours of overtime in a single month may choose "
    "to take the excess as time off in lieu instead of payment.",
    "C", 3,
    "Text B, paragraph C says staff who accumulate more than ten hours of overtime in "
    "a single month may take the excess as time off in lieu; so the answer is 'ten hours'.",
    "medium",
    "Eski soru B metni D/2'ye capaliydi; model parcasiz uc turda da 'final pay' vererek "
    "cevabin ayirt edici sozcugunu tutturdu, cunku isten ayrilista odenen seyin son "
    "maas olmasi calisma hayatinin standart uygulamasi. Yeni soru D paragrafina hic "
    "degmiyor: kanit C/3'e, fazla mesainin izne cevrilme esigine tasindi. Esik "
    "sirkete ozgu; ayrica cevabin 'time off in lieu' olmamasi icin o ifade cerceve "
    "icinde veriliyor.")

# --------------------------------------------------------------- G04 (GT2)
YENI[("content/reading/tests/GT2/sentence-completion.json", 25)] = y(
    "Every member of staff working remotely must supply their own reliable internet "
    "connection, running at (25) ........ or better.",
    ["10 Mbps"], ["10 Mbps", "10Mbps"],
    "Provide their own reliable internet connection of at least 10 Mbps.",
    "B", 2,
    "Text B, paragraph B says remote workers must provide their own reliable internet "
    "connection of at least 10 Mbps; so the answer is '10 Mbps'.",
    "easy",
    "Eski soru B metni A/1'e capaliydi; model parcasiz uc turda da 'probation period' "
    "vererek cevabin ayirt edici ogesini tutturdu, cunku uzaktan calisma basvurusunun "
    "on kosulu ise alma dunyasinin en yerlesik kurali. Yeni soru A paragrafina hic "
    "degmiyor: kanit B/2'ye, baglanti hizi kosuluna tasindi. Sayi sirket "
    "yonergesine ozgu.")

YENI[("content/reading/tests/GT2/table-completion.json", 16)] = y(
    "Written stage: Form filled in online and an up-to-date CV uploaded by 28 "
    "February, plus a (16) ........ statement explaining your interest",
    ["300-word"], ["300-word", "300 word"],
    "Submit a 300-word statement explaining your interest in the placement.",
    "B", 3,
    "Text A, paragraph B says applicants must submit a 300-word statement explaining "
    "their interest in the placement; so the answer is '300-word'.",
    "easy",
    "Eski satir B/2'ye capaliydi ve cevap ('CV') basvuru surecinin kendisinden "
    "cikiyordu, pasajdan degil. Yeni satir B/2'ye hic degmiyor: kanit B/3'e, "
    "gerekce metninin uzunluguna tasindi; CV ve son basvuru tarihi artik VERILEN "
    "bilgi olarak satirda duruyor, sorulmuyor. Istenen uzunluk ilana ozgu bir sayi.")

YENI[("content/reading/tests/GT2/table-completion.json", 20)] = y(
    "During the placement: Every intern has a short performance review at the "
    "(20) ........ mark, and a final one before leaving",
    ["five-week"], ["five-week", "five week", "5-week"],
    "Interns complete a short performance review at the five-week mark and a final "
    "review before departure; strong performers may be invited to apply for the "
    "graduate programme the following year, though this is not guaranteed and depends "
    "on business need.",
    "D", 2,
    "Text A, paragraph D says interns complete a short performance review at the "
    "five-week mark and a final review before departure; so the answer is 'five-week'.",
    "medium",
    "Eski satir D/1'e capaliydi ve cumlenin butun icerigi ('kendi biriminden biriyle "
    "eslestirilir, on hafta boyunca haftada bir gorusur') dogrudan 'mentor' rolunu "
    "tanimliyordu. Yeni satir D/1'e hic degmiyor: kanit D/2'ye, ara degerlendirmenin "
    "zamanina tasindi. Bu tarih programa ozgu; on haftalik surenin ortasi olmasi da "
    "zorunlu degil, dolayisiyla hesapla turetilemez.")

# --------------------------------------------------------------- G05 (practice ozet)
YENI[("content/reading/practice/summary-completion.json", 9)] = y(
    "Because families are poor judges of their own rubbish, the team followed 215 "
    "households for a year, (9) ........ of them in the urban sub-district of Cibinong, "
    "and weighed what each home actually put in the bin.",
    ["150"], ["150"],
    "Over the course of a year, researchers followed 215 households, 150 in the urban "
    "sub-district of Cibinong and 65 in the rural sub-district of Sukajaya, to find "
    "out not just how much food they discarded but what kind, and why.",
    "A", 3,
    "Paragraph A says the researchers followed 215 households, 150 of them in the "
    "urban sub-district of Cibinong; so the answer is '150'.",
    "easy",
    "Eski bosluk B/1'e capaliydi ve sizinti kabul listesinin kendisindeydi: "
    "'scales' tek basina kabul ediliyordu ve cop tartilan seyin terazi olmasi "
    "kacinilmazdi. Yeni bosluk B/1'e hic degmiyor: kanit A/3'e, orneklemin kentsel "
    "ayagina tasindi. Toplam (215) cercevede verildigi icin soru olculebilir, ama "
    "kentsel pay disaridan turetilemez; kirsal sayi (65) bilerek anilmadi ki cikarma "
    "islemiyle bulunmasin.")

# --------------------------------------------------------------- A05 (AC2 cumle)
YENI[("content/reading/tests/AC2/sentence-completion.json", 21)] = y(
    "The markers designed for the work ran from about 106 to (21) ........ base pairs in "
    "length, short enough to pick up badly degraded fragments.",
    ["243"], ["243"],
    "The team focused on a gene responsible for a key wheat protein, designing several "
    "sets of short genetic markers, ranging from around 106 to 243 base pairs in "
    "length, specifically built to capture the small, degraded fragments of DNA that "
    "survive in seeds this old.",
    "D", 2,
    "Paragraph D says the genetic markers ranged from around 106 to 243 base pairs in "
    "length; so the answer is '243'.",
    "medium",
    "Eski soru E/3'e capaliydi ve cevap yerlesik bir bugday genetigi terimiydi ('D "
    "genome'); cumle terimin tanimini veriyordu. Yeni soru E/3'e hic degmiyor: kanit "
    "D/2'ye, tasarlanan isaretcilerin uzunluk araligina tasindi. Ust sinir yalniz "
    "yontem bolumunden okunur.")

YENI[("content/reading/tests/AC2/sentence-completion.json", 22)] = y(
    "Of the seventeen distinct variants found at the first marker length, (22) ........ "
    "had never been recorded in any genetic database.",
    ["thirteen"], ["thirteen", "13"],
    "Of the sequences obtained at one marker length, twenty-two in all, seventeen "
    "distinct genetic variants emerged, thirteen of which had never before been "
    "recorded in any genetic database; a further ten sequences at a second marker "
    "length revealed five variants, two of them likewise entirely new.",
    "E", 4,
    "Paragraph E says seventeen distinct variants emerged at the first marker length, "
    "thirteen of which had never before been recorded in any genetic database; so the "
    "answer is 'thirteen'.",
    "medium",
    "Eski soru G/2'ye capaliydi ve cevap bir ozel ad ve arkeoloji ders kitabi "
    "bilgisiydi (Karacadag). E5 ayrica G/2'ye yeni soru yazilmamasini ozellikle "
    "istemisti. Yeni soru G paragrafina hic degmiyor: kanit E/4'e, veri tabaninda hic "
    "kayitli olmayan varyant sayisina tasindi. Sayim calismanin kendi sonucu.")

# --------------------------------------------------------------- A08 (AC3 cumle)
YENI[("content/reading/tests/AC3/sentence-completion.json", 19)] = y(
    "Most of the 700-plus slides later identified lay to the ........ of the epicentre, "
    "along the line of the fault rupture.",
    ["northwest"], ["northwest", "north-west"],
    "The United States Geological Survey later identified more than 700 potential "
    "landslides and snow avalanches associated with the earthquake, most of them "
    "concentrated to the northwest of the epicentre along the line of the fault rupture.",
    "B", 1,
    "Paragraph B says most of the 700-plus landslides and avalanches were concentrated "
    "to the northwest of the epicentre, along the fault rupture; so the answer is "
    "'northwest'.",
    "easy",
    "Eski soru B/2'ye capaliydi ve cevap yerlesik bir sismoloji terimiydi "
    "('displacement'); cumle terimin tanimini veriyordu ve ONE WORD ONLY sinirinda "
    "tanimi tasimayan bir cerceve kurulamiyordu. Yeni soru B/2'ye hic degmiyor: kanit "
    "B/1'e, kaymalarin cografi dagilimina tasindi. Yon bilgisi olcumden gelir.")

YENI[("content/reading/tests/AC3/sentence-completion.json", 21)] = y(
    "The radar picture the analysts worked from was taken on 8 December, only ........ "
    "days after the shaking.",
    ["two"], ["two", "2"],
    "By comparing an image captured on 8 December, only two days after the earthquake, "
    "with a baseline image from 26 November, before the quake, analysts could see "
    "large new patches of brightness spreading across slopes that had previously "
    "appeared smooth and dark, a direct signature of freshly broken rock and snow.",
    "C", 3,
    "Paragraph C says the image used was captured on 8 December, only two days after "
    "the earthquake; so the answer is 'two'.",
    "easy",
    "Eski soru F/1'e capaliydi ve cevap yerlesik bir buzulbilim terimiydi ('surge'); "
    "gunde 50 fit ilerleyen bir buzulun evresi baska turlu adlandirilmiyordu. Yeni "
    "soru F paragrafina hic degmiyor: kanit C/3'e, goruntunun depremden kac gun sonra "
    "cekildigine tasindi. Cerceve deprem tarihini vermiyor, dolayisiyla fark yalniz "
    "metinden okunur.")

YENI[("content/reading/tests/AC3/sentence-completion.json", 22)] = y(
    "The scale of the disturbance startled even the experienced ........ who were "
    "studying the imagery.",
    ["glaciologists"], ["glaciologists"],
    "The scale of the disturbance startled even experienced glaciologists studying the "
    "imagery.",
    "E", 1,
    "Paragraph E says the scale of the disturbance startled even experienced "
    "glaciologists studying the imagery; so the answer is 'glaciologists'.",
    "medium",
    "Eski soru G/2'ye capaliydi ve cevap tek sozcuktu ('mountaineers'); model parcasiz "
    "uc turda da tam es anlamlisini ('climbers') verdi, cunku 'daga cikan insanlar' "
    "kavraminin Ingilizcede birden cok adi var. Yeni soru G paragrafina hic degmiyor: "
    "kanit E/1'e tasindi. ONE WORD ONLY sinirinda A08'in kalan malzemesi dardi; bu "
    "yuva yine de en az es anlamli karsiligi olan adaylardan biri, ama kalan risk "
    "E7'ye not edildi.")

for k, v in list(YENI.items()):
    v["dosya"], v["numara"] = k


# --------------------------------------------------------------------------
# stem_block / word_bank degisiklikleri: (dosya, eski parca, yeni parca)
# Eski parca dosyada birebir bulunmazsa betik durur.
# --------------------------------------------------------------------------
BLOK = [
    ("content/reading/practice/note-completion.json",
     "- Staff based in every one of Japan's (1) ........ prefectures, plus 23 further countries",
     "- Sample: (1) ........ employee-month records in all, from a single department, April 2022 to March 2023"),
    ("content/reading/practice/note-completion.json",
     "- Pyroclastic flows, racing currents of hot gas and debris, can reach about (10) ........ degrees Celsius",
     "- Vitrified tissue: axons averaging (10) ........ nanometres across, roughly the range found in living white matter"),

    ("content/reading/practice/summary-completion.json",
     "Both the zoned open-plan room and the team office beat the plain open-plan baseline "
     "on how content the staff felt and on how productive they believed themselves to be, "
     "while the activity-based arrangement, for all its (1) ........ in current office "
     "fashion, finished below the baseline on both counts. The same two layouts also came "
     "top for flow, the mental state in which a person is completely (2) ........ in the "
     "task at hand, which points to partial enclosure as an aid to lasting concentration.",
     "Both the zoned open-plan room and the team office beat the plain open-plan baseline "
     "on how content the staff felt and on how productive they believed themselves to be, "
     "while the activity-based arrangement finished below the baseline on both counts, "
     "with scores about (1) ........ per cent lower. The same two layouts also came top for flow, "
     "the zoned room scoring (2) ........ per cent above the plain baseline and the team "
     "office 12 per cent above it, which suggests that partial enclosure aids lasting "
     "concentration."),
    ("content/reading/practice/summary-completion.json",
     "Because families are poor judges of their own rubbish, the team gathered what each "
     "home actually binned on eight days in a row and put it on (9) ........ precise to "
     "within two grams.",
     "Because families are poor judges of their own rubbish, the team followed 215 "
     "households for a year, (9) ........ of them in the urban sub-district of Cibinong, "
     "and weighed what each home actually put in the bin."),

    ("content/reading/tests/AC1/summary-completion.json",
     "Maug is what is left of a volcano that fell in on itself, so that three small "
     "islands now sit in a ring around a drowned (36) ........ . Molten rock below the "
     "seabed feeds openings that pour carbon dioxide straight into the water beside a "
     "living reef.",
     "Maug's unusual chemistry comes from its geology. Magma still lies beneath the "
     "seafloor and, along the (36) ........ of the caldera, drives shallow vents that "
     "release carbon dioxide straight into the water beside a living reef."),
    ("content/reading/tests/AC1/summary-completion.json",
     "Their readings show that the water closest to the openings is slightly more acidic "
     "than the rest of the reef, and that the seabed there is taken over by (38) ........ "
     "instead of healthy coral. A second piece of research found that minute organisms "
     "bore into the skeletons far more heavily in this water, speeding up (39) ........ "
     "and weakening the reef from the inside.",
     "Reef scientists' wider worry is that corals will lose the contest for space, and "
     "that complex reef habitat will gradually give way to simpler (38) ........ . A "
     "second piece of research, published in the journal (39) ........ , looked at what "
     "happens inside the coral skeletons rather than on the seafloor surface."),

    ("content/reading/tests/AC2/flow-chart-completion.json",
     "From first sighting to an official name",
     "From the first images to what the find shows"),
    ("content/reading/tests/AC2/flow-chart-completion.json",
     "The speck is accepted as a body circling Uranus and is entered in the records under "
     "the provisional (2) ........ S/2025 U1.",
     "The speck is accepted as a body circling Uranus, and the addition to the planet's "
     "moon family is announced in (2) ........ ."),
    ("content/reading/tests/AC2/flow-chart-completion.json",
     "As the object is too faint to measure directly, its width is put at some ten "
     "kilometres, on the assumption that it (3) ........ light much as Uranus's other "
     "small moons do.",
     "Too faint to be measured directly, the object has its width put at about "
     "(3) ........ , which makes it one of the smallest moons known anywhere."),
    ("content/reading/tests/AC2/flow-chart-completion.json",
     "A lasting name, drawn from plays and poetry rather than from myth, still has to be "
     "approved by the (6) ........ .",
     "The team lead's comment: an object that slipped past even a (6) ........ shows how "
     "much of a well-studied planetary system can still lie hidden."),

    ("content/reading/tests/AC4/note-completion.json",
     "- Repeated staff surveys, sensors reading the air and the room, a count of technical output\n"
     "- Watchers logged everyday habits, for example how often people put on (4) ........",
     "- Repeated staff surveys covering satisfaction, engagement, (4) ........ , energy, "
     "flow and how productive people felt\n"
     "- Sensors reading noise, temperature, light and air; a count of technical output; "
     "watchers logging everyday habits at people's desks"),

    ("content/reading/tests/AC4/summary-completion.json",
     "In the earlier one, different volunteers were placed in a sleeping group and a "
     "waking group; the later one instead used a (36) ........ design, so that the very "
     "same volunteers went through both a rest and a matching stretch of time without one.",
     "In the earlier one, different volunteers were placed in a sleeping group and a "
     "waking group, while in the later one the same volunteers met both conditions on "
     "different days, each spending half an hour on (36) ........ before the final test "
     "so that grogginess would not distort it."),
    ("content/reading/tests/AC4/summary-completion.json",
     "Where the two halves of a pair were already (38) ........ , a whole night of sleep "
     "improved recall far more than a rest of an hour and a half did. Where no such link "
     "existed, however, the picture changed: the two turned out to offer (39) ........ .",
     "The naps themselves ran to an average of (38) ........ and were made up largely of "
     "a lighter stage of sleep. Where the two halves of a pair were already close in "
     "meaning, a whole night of sleep improved recall far more than the daytime rest did. "
     "Where no such link existed, however, the picture changed: the two turned out to "
     "offer (39) ........ ."),

    ("content/reading/tests/GT1/note-completion.json",
     "- Ask the supervisor in writing two days beforehand, on a (18) ........ picked up at the staff office\n"
     "\nAnnual leave\n"
     "- Someone working full time receives (19) ........ of paid leave a year, with public holidays counted inside that total\n"
     "- Time off is booked on the online (20) ........ , a fortnight ahead as a minimum",
     "- Ask the supervisor in writing two days beforehand, on a (18) ........ picked up at the staff office\n"
     "- Both workers still have to meet their weekly hours, and a swap leaving under (19) ........ of rest between shifts is refused\n"
     "\nAnnual leave\n"
     "- Time off is booked on the online (20) ........ , a fortnight ahead as a minimum"),
]

BANKA = {
    "content/reading/tests/AC4/summary-completion.json": [
        {"letter": "A", "text": "a chance to sleep"},
        {"letter": "B", "text": "awake"},
        {"letter": "C", "text": "an hour and a half"},
        {"letter": "D", "text": "64.1 minutes"},
        {"letter": "E", "text": "an unbroken night"},
        {"letter": "F", "text": "equal benefits"},
        {"letter": "G", "text": "much weaker results"},
        {"letter": "H", "text": "in the laboratory"},
        {"letter": "I", "text": "a quiet walk"},
        {"letter": "J", "text": "a puzzle game"},
    ],
}


def yuvalar(d):
    for g in (d["groups"] if "groups" in d else [d]):
        for it in g.get("items", []):
            yield it


def main():
    liste = json.load(open(os.path.join(KOK, "content", "DOGRULAMA",
                                        "yeniden-uretim-listesi.json"), encoding="utf-8"))
    e5 = {(x["dosya"], x["numara"]): x for x in liste["elenen"]}

    dosyalar = sorted(set(k[0] for k in YENI) | set(b[0] for b in BLOK))
    toplam = 0
    for rel in dosyalar:
        yol = os.path.join(KOK, rel.replace("/", os.sep))
        d = json.load(open(yol, encoding="utf-8"))
        for it in yuvalar(d):
            v = YENI.get((rel, it["number"]))
            if not v:
                continue
            kayit = e5[(rel, it["number"])]
            eski_prompt, eski_cevap = it["prompt"], it["answer"]
            eski_kanit = it.get("evidence")

            for alan in TEMIZLENEN:
                it.pop(alan, None)
            it["prompt"] = v["prompt"]
            it["answer"] = v["answer"]
            it["accepted_variants"] = v["accepted_variants"]
            it["evidence"] = v["evidence"]
            it["evidence_locator"] = {"paragraph": v["paragraph"], "sentence": v["sentence"]}
            it["explanation"] = v["explanation"]
            it["difficulty"] = v["difficulty"]
            it["status"] = "verified"
            it["blind_solvable"] = None
            it["blind_basis"] = None
            it["generated_by"] = "opus"
            it["yeniden_uretim"] = {
                "tarih": TARIH,
                "kaynak_prompt": KAYNAK,
                "uretilen_grup": GRUP,
                "eski_prompt": eski_prompt,
                "eski_cevap": eski_cevap,
                "eski_kanit_cumlesi": eski_kanit,
                "neden_elendi": kayit["neden_elendi"],
                "ne_degisti": v["ne_degisti"],
            }
            toplam += 1
            print("  %s #%s -> %s/%s" % (rel, it["number"], v["paragraph"], v["sentence"]))

        for f, eski, yeni in BLOK:
            if f != rel:
                continue
            if eski not in (d.get("stem_block") or ""):
                raise SystemExit("stem_block parcasi bulunamadi (%s): %r" % (rel, eski[:60]))
            d["stem_block"] = d["stem_block"].replace(eski, yeni)
            print("  %s stem_block guncellendi" % rel)
        if rel in BANKA:
            d["word_bank"] = BANKA[rel]
            print("  %s word_bank guncellendi" % rel)

        json.dump(d, open(yol, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        open(yol, "a", encoding="utf-8").write("\n")
    print("yeniden dolduruldu: %d yuva" % toplam)
    if toplam != len(YENI):
        raise SystemExit("EKSIK: %d yuva bulunamadi" % (len(YENI) - toplam))


main()
