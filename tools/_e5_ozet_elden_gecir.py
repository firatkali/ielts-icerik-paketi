# -*- coding: utf-8 -*-
"""E5 8. calistirma - elden gecirme.

Kapsam: E10'un ozet ailesinde isaretledigi 14 soru + depoda ayakta kalan 23
genel_kultur sorusu (toplam 37).

Kural (talimat): answer / accepted_variants / evidence / evidence_locator
KORUNUR. Duzeltme yalniz soru metnine ve ozet/not/tablo govdesine yapilir.
"""
import json, io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

TARIH = "2026-08-08"

# ---------------------------------------------------------------- DUZELTMELER
# dosya -> numara -> (yeni_prompt, yeni_explanation, mekanizma, ne_degisti)
DUZELT = {
 "content/reading/practice/summary-completion.json": {
  4: (
   "What the teams actually produced barely moved, which the authors read as a "
   "sign that seasoned (4) ........ using familiar tools are neither slowed nor "
   "hurried by a change of room, however differently that room makes them feel.",
   "Paragraph G attributes the unchanged output to experienced software engineers "
   "accustomed to their tools not being noticeably affected by the change of "
   "layout; so the answer is 'software engineers'.",
   "esdizim_kilidi",
   "Ozet govdesindeki 'The volume of code a team produced' ibaresi kaldirildi. "
   "'Code' sozcugu boslugun istedigi meslegi tek basina adlandiriyordu: model "
   "parcasiz uc turda da developers / programmers / developers verdi, yani "
   "kavrami ciktiyi olcen sozcukten okuyordu. Yeni cercevede ('what the teams "
   "actually produced') meslek adi yalnizca G/3'ten bulunabiliyor."),
  6: (
   "To find out, a small group of Finnish students each spent quiet time both "
   "among snow-covered trees and beside campus buildings, in an order-balanced "
   "(6) ........ design.",
   "Paragraph B calls this design, in which every participant experienced both "
   "conditions in a different order, a 'crossover' experiment; so the answer is "
   "'crossover'.",
   "tanim_sizintisi",
   "Bosluktan hemen sonra gelen ac tanim ('that let every volunteer serve as "
   "their own comparison') kaldirildi - bu, crossover duzeninin ders kitabi "
   "tanimiydi ve modele 2/3 turda dogru kavrami veriyordu. Yeni cerceveye "
   "crossover, within-subject, repeated-measures ve counterbalanced adaylarinin "
   "hepsi uyuyor; secim yalniz B/2'den yapilabiliyor."),
  12: (
   "The sharpest contrast was between town and country: city households threw "
   "out almost (12) ........ the weight recorded in the rural sub-district, and "
   "a larger share of what they discarded was still fit to eat, a difference the "
   "researchers tied partly to the gap in what the two groups earned and spent.",
   "Paragraph D says the 79.4 kilograms of waste per person in the city was "
   "almost double the 45.8 kilograms recorded in the rural area; so the answer "
   "is 'double'.",
   "esdizim_kilidi",
   "Ayni cumlenin sonundaki 'roughly twofold gap' ibaresi kaldirildi. Bosluk bir "
   "kat sayisi istiyordu ve cumlenin kendisi o kat sayisini ('twofold') on iki "
   "sozcuk sonra yaziyla veriyordu; model 3 turun 2'sinde double/twice verdi. "
   "Artik oran yalniz D/2'deki 79,4 ve 45,8 kilogramdan cikarilabiliyor."),
 },
 "content/reading/tests/AC1/summary-completion.json": {
  40: (
   "Because these changes resemble what reefs elsewhere may meet before this "
   "century ends, the island is now studied as a (40) ........ for the rest of "
   "the ocean.",
   "Paragraph H says that scientists regard the island as an early warning "
   "system, showing in the present what a warmer, more acidic ocean could look "
   "like elsewhere; the answer is therefore 'warning system'.",
   "esdizim_kilidi",
   "'an early ___' kalibi kaldirildi: 'early warning system' kaliplasmis bir "
   "obek oldugu icin 'early' sozcugu boslugun bas adini tek basina veriyordu "
   "(model uc turda da 'warning' yazdi). Yeni cerceveye warning system, test "
   "case, preview, model gibi birden cok aday uyuyor; secim H/2'den yapiliyor. "
   "Kanit cumlesinin 'less as a curiosity than as' kalibi bilincli olarak "
   "yankilanmadi."),
 },
 "content/reading/tests/AC3/summary-completion.json": {
  40: (
   "The authors conclude that only a very narrow band of (40) ........ could "
   "have left the tissue both scorched and structurally intact.",
   "Paragraph G says only a very narrow set of thermal conditions could explain "
   "both the extreme heat exposure and the preservation of the structure; so the "
   "answer is 'thermal conditions'.",
   "tanim_sizintisi",
   "Boslugun hemen ardindaki cizgi arasi ac tanim ('heat applied in an instant, "
   "then cooling almost at once') kaldirildi - bu, 'thermal' niteleyicisinin "
   "ozetteki tek kaynagiydi ve model uc turda da bas adi ('conditions') "
   "veriyordu. Niteleyici artik yalniz G/2'den okunabiliyor."),
 },
 "content/reading/tests/GT1/summary-completion.json": {
  37: (
   "The biggest inedible category by some way was (37) ........ from fruit and "
   "vegetables, above all from bananas and mangoes.",
   "Paragraph E says that among inedible waste, fruit and vegetable peelings, "
   "led by banana and mango skins, made up the largest share; so the answer is "
   "'peelings'.",
   "tanim_sizintisi",
   "Ozetteki 'chiefly the skins of bananas and mangoes' ibaresindeki 'skins' "
   "sozcugu kaldirildi; bu sozcuk boslugun karsiligini es anlamlisiyla "
   "yaziyordu ve model uc turda da 'peel' verdi. Meyve adlari korundu, cunku "
   "onlar E/3'un ayirt edici ayrintisi; kaldirilan tek sey cevabin sozluk "
   "karsiligi."),
 },
 "content/reading/tests/AC1/note-completion.json": {
  4: (
   "A large (4) ........ pushed into place served the same purpose once the cube "
   "was taken away",
   "Paragraph D describes how, once the cube was removed, Kandula pushed a large "
   "tractor tyre into use as a substitute platform; so the answer is 'tyre'.",
   "genel_kultur",
   "Nottaki 'tractor' sozcugu kaldirildi. Sizinti sorunun ekseninde degil, "
   "'tractor ___' esdiziminde ve fil + traktor lastigi eslesmesinin yaygin "
   "bilinmesindeydi; model uc turda da 'tyre' yazdi. Yeni cerceveye ('a large "
   "___ pushed into place') tyre, log, barrel, crate gibi adaylar esit derecede "
   "uyuyor, secim yalniz D/4'ten yapilabiliyor. Cevabin kendisi bir dunya "
   "bilgisi degil, pasajin siradan bir ayrintisi oldugu icin bu yuva elenmedi."),
 },
 "content/reading/tests/AC3/table-completion.json": {
  6: (
   "Both responsive animals — What they saw: Each of them studied the reflection "
   "with the (6) ........ .",
   "Paragraph F says that both whales preferred to view the mirror with their "
   "right eye; the answer is therefore 'right eye'.",
   "genel_kultur",
   "Hucrenin sonundaki 'hinting that one side of the brain deals with this task' "
   "ibaresi kaldirildi. Yanallasma (lateralisation) cagrisimi, hayvan "
   "davranisinda sikca bildirilen sag goz tercihini dogrudan hatirlatiyordu. "
   "Ibare gidince hucreye 'the same eye' de en az 'right eye' kadar uyuyor - "
   "ustelik 'Both / Each of them' vurgusu sezgiyi oraya cekiyor. KISMI duzeltme: "
   "geriye sag/sol ikilisinde zayif bir sag onyargisi kaliyor, E7 ayrica "
   "olcmeli."),
 },
}

# ------------------------------------------------------------------ ELEMELER
# dosya -> numara -> neden_elendi
ELE = {
 "content/reading/practice/note-completion.json": {
  1: "Cevabin kendisi bir dunya bilgisi: Japonya'nin 47 ile bolunmus olmasi "
     "cografya ders kitabi duzeyinde bilinir ve model parcasiz uc turda da '47' "
     "yazdi (3/3 PUAN alirdi). Nottan 'Japan's' kaldirilsa bile 'prefecture' "
     "sozcugu tek basina Japonya'yi adlandiriyor, yani cerceve duzeltmesi yariya "
     "kaliyor. E6 onerisi: ayni cumledeki calisan sayisi (yaklasik 900) ya da "
     "'23 other countries' yerine Mart 2025 tarihi.",
  10: "Cevabin kendisi bir dunya bilgisi: piroklastik akintilarin yaklasik 500 "
      "santigrat dereceye ulastigi volkanoloji anlatilarinin standart rakami; "
      "model uc turda da '500' yazdi (3/3 PUAN). Not satirinin kendisi zaten bu "
      "genel gercegin ifadesi, dolayisiyla yeniden yazmak sizintiyi kapatmiyor. "
      "E6 onerisi: A paragrafinin Herculaneum'a olan uzakligi ya da Pompeii ile "
      "Herculaneum'un farkli gomulme bicimi.",
 },
 "content/reading/practice/sentence-completion.json": {
  1: "Cevabin kendisi bir dunya bilgisi: fillerin dallari sinek kovmak icin "
     "kullandigi hayvan davranisi kulturunun en cok tekrarlanan ayrintilarindan "
     "biri; model uc turda da 'swat flies' yazdi (3/3 PUAN). Kanit cumlesi (A/2) "
     "uc ornek sayiyor ve ucu de ayni olcude taniniyor (ayna testi, yer bellegi, "
     "sinek kovma), dolayisiyla cerceveyi baska ornege tasimak da sizdirir. E6 "
     "onerisi: A paragrafinin laboratuvar ile arazi arasinda kurdugu karsitlik.",
  10: "Cevabin kendisi bir dunya bilgisi: Uranus'un Gunes'ten yedinci gezegen "
      "olmasi temel astronomi; model uc turda da 'seventh' yazdi (3/3 PUAN). "
      "Soru kokunun kendisi ('in order of distance outwards from the Sun') zaten "
      "dunya bilgisini cagiriyor. E6 onerisi: A/1'in oteki yarisi - uydu "
      "ailesinin kalabalikligi ya da halka sisteminin egikligi.",
  11: "Sizinti aritmetik ve kapatilamiyor: cumle 1986 ucusunu veriyor, gunumuz "
      "tarihi de disaridan biliniyor, ikisinin farki dogrudan 'forty years' "
      "ediyor; model uc turda da '40 years' yazdi (kabul listesinde var, 3/3 "
      "PUAN). Cumleden 1986'yi kaldirmak yariya kalir, cunku Voyager 2'nin "
      "Uranus'e 1986'da ugradigi ayrica dunya bilgisidir - ayni depodaki "
      "practice/short-answer 4 bunun kaniti: model o tarihi gun gun bilerek "
      "yazdi. E6 onerisi: F/3'un cozunurluk esigi gerekcesi ya da uydunun "
      "yaklasik on kilometrelik capi.",
 },
 "content/reading/practice/short-answer.json": {
  4: "Cevabin kendisi bir dunya bilgisi: Voyager 2'nin Uranus'e en yakin gecis "
     "tarihi (24 Ocak 1986) halka acik NASA kayitlarindan bilinen unlu bir "
     "tarih; model uc turda da gun/ay/yil dogru yazdi (3/3 PUAN). Soru kokunun "
     "tamami zaten 'o tarih neydi' sorusudur, yani eksen dunya bilgisinin "
     "kendisi. E6 onerisi: F/2'nin ikinci yarisi - Voyager'in cektigi yakin "
     "goruntulerin bugun hala tek ornek olmasi, ya da bu uydunun o gecise hic "
     "yakalanmamis olmasi.",
  8: "Cevabin kendisi bir dunya bilgisi ve soru kokunun tamami onu soruyor: "
     "'Kanada'nin en yuksek zirvesi' sorusunun cevabi Mount Logan'dir ve model "
     "uc turda da yazdi (3/3 PUAN). Kokten 'highest in Canada' ibaresini "
     "cikarmak soruyu duzeltmez, baska bir soru yazmak olur - talimatin yarim "
     "duzeltme saydigi sey budur. E6 onerisi: D/1'in oteki yarisi - Mount King "
     "George'un yamacindaki genis enkaz akmasi ya da uydu goruntusuyle yer "
     "arastirmasinin ortusmesi.",
 },
 "content/reading/practice/summary-completion.json": {
  2: "Cevabin kendisi, ozetin verdigi tanimin standart sozcugu: 'flow' "
     "kavraminin psikolojideki ders kitabi tanimi zaten 'bir ise tamamen dalmis "
     "(absorbed) olma hali'dir; model uc turda da 'absorbed' yazdi (3/3 PUAN). "
     "Tanimi ozetten cikarmak boslugu kapatmiyor, bosalttiyor: geriye kalan 'a "
     "person is completely ___' cercevesine absorbed, immersed, engrossed, "
     "focused esit derecede uyar ve soru cok cevapli hale gelir. E6 onerisi: "
     "E paragrafinin flow icin verdigi sayisal fark ya da kismi bolmenin rolu.",
  9: "🔴 Sizinti kabul listesinin kendisinde ve o korunan bir alan: "
     "accepted_variants 'scales' tek basina kabul ediyor, model de uc turda "
     "'scales' yazdi (3/3 PUAN). Cerceveden 'precise to within two grams' "
     "ibaresini kaldirmak 'digital' niteleyicisinin kaynagini kapatir ama "
     "cop tartilan seyin terazi olmasi zaten kacinilmaz oldugu icin 'scales' "
     "yine puan alir. Kabul listesini daraltmak talimatin korunan alan kuralina "
     "takiliyor, dolayisiyla mekanik duzeltme yolu yok. E6 onerisi: B/1'in "
     "ayirt edici ayrintisi - sekiz ardisik gun ya da atigin ayrica tasnif "
     "edilmesi.",
 },
 "content/reading/tests/AC1/sentence-completion.json": {
  22: "Cevabin kendisi yerlesik bir literatur terimi: 'dear enemy effect' hayvan "
      "davranisi yazininin adiyla anilan bir kavramidir ve model uc turda da "
      "yazdi (3/3 PUAN). Cumleden tanimi ('reacting with less hostility to an "
      "animal that is already known') cikarmak mumkun degil, cunku hangi etkinin "
      "sorulduğunu belirleyen tek sey odur; kalan her cerceve ayni unlu terimi "
      "cagiriyor. E6 onerisi: H/2'nin gerekce yarisi - tekrarlanan kavgalarin "
      "enerji harcamasi ve yaralanma riski.",
 },
 "content/reading/tests/AC1/summary-completion.json": {
  36: "Cevabin kendisi yerlesik bir jeoloji terimi: cokmus bir yanardagin "
      "halka bicimli cukuru 'caldera' diye anilir ve ozetin kendisi bu tanimi "
      "('a volcano that fell in on itself ... three small islands in a ring') "
      "veriyor; model uc turda da yazdi (3/3 PUAN). Tanimi cikarmak boslugu "
      "yanitlanamaz yapar, birakmak terimi verir. E6 onerisi: B/2'nin oteki "
      "ayrintisi - uc adanin sayisi ya da adalarin dizilisi yerine yanardagin "
      "cokme zamani.",
  38: "Cevap iki yonden sizdiriyor: asitlenen suda saglikli mercanin yerini "
      "yosunun almasi iklim habercilerinin en cok tekrarladigi oruntudur ve "
      "kabul listesi 'algae' sozcugunu tek basina kabul ediyor; model uc turda "
      "da 'algae' yazdi (3/3 PUAN). Niteleyiciyi ('weedy') zorunlu kilmak icin "
      "kabul listesini daraltmak gerekir, o da korunan bir alan. E6 onerisi: "
      "F/2'nin karsilastirma yarisi - bacalardan biraz uzaktaki mercanin gorunur "
      "bicimde saglikli kalmasi.",
  39: "Cevabin kendisi yerlesik bir deniz biyolojisi terimi ve ozet onun tanimini "
      "veriyor: 'minute organisms bore into the skeletons ... weakening the reef "
      "from the inside' zaten bioerosion'un sozluk karsiligidir; model uc turda "
      "da yazdi (3/3 PUAN). Tanimi cikarinca bosluk yanitlanamaz hale geliyor. "
      "E6 onerisi: G/2'nin nicel yarisi - oyucu canlilarin bu suda ne kadar daha "
      "yogun yerlestigi.",
 },
 "content/reading/tests/AC2/flow-chart-completion.json": {
  2: "Cevabin kendisi yerlesik bir astronomi terimi: yeni bulunan gok "
     "cisimlerine kalici ad verilmeden once 'provisional designation' atanmasi "
     "adlandirma geleneginin kendisidir ve S/2025 U1 bicimindeki kod bu terimin "
     "isaretidir; model uc turda da 'designation' yazdi (3/3 PUAN). Kutudan "
     "'provisional' sozcugunu kaldirmak yetmiyor, cunku sizdiran sey sifat degil "
     "adlandirma gelenegini bilmek. E6 onerisi: C paragrafinin gozlem ayrintisi "
     "- cismin kac pozda izlendigi ya da hangi tarihte kaydedildigi.",
  6: "Cevabin kendisi bir ozel ad ve dunya bilgisi: gok cismi adlarini onaylayan "
     "kurumun Uluslararasi Astronomi Birligi olmasi astronominin en cok bilinen "
     "kurumsal gercegi; model uc turda da adin tamamini yazdi (3/3 PUAN). "
     "Kutunun kalan icerigi (Shakespeare ve Pope gelenegi) degistirilse bile "
     "'onaylayan kurum' sorusunun tek cevabi ayni kalir. E6 onerisi: E/2'nin "
     "gelenek yarisi - adlarin mitolojiden degil oyun ve siirden secilmesi.",
 },
 "content/reading/tests/AC2/sentence-completion.json": {
  21: "Cevabin kendisi yerlesik bir bugday genetigi terimi ve cumle onun tanimini "
      "veriyor: 'alti kromozomlu bugdaya ozgu genetik bolge' zaten D genome'un "
      "tanimidir; model uc turda da yazdi (3/3 PUAN). Tanim cikarilirsa hangi "
      "dizinin soruldugu belirsizlesir. Ayrica 3. calistirma ayni pasajda "
      "hexaploid terimini tasiyan practice-6'yi da ayni gerekceyle elemisti. "
      "E6 onerisi: E/3'un sayisal yarisi - toplam otuz iki DNA dizisi.",
  22: "Cevabin kendisi bir ozel ad ve arkeoloji ders kitabi bilgisi: einkorn "
      "ekiminin dogdugu yer olarak Karacadag anilir; model uc turda da yazdi "
      "(3/3 PUAN). 3. calistirma ayni pasajda ayni ekseni tasiyan AC2-24 ve "
      "AC2-25'i zaten elemisti, dolayisiyla bu yuva o kararin devami. 🔴 E6 "
      "dikkat: G/2 artik bu testte ucuncu kez elenen bir yuvanin kanit cumlesi; "
      "bu cumleye yeni soru yazilmamali. E6 onerisi: G paragrafinin yayilma "
      "anlatisi yerine E/3'teki korunma karsilastirmasi.",
 },
 "content/reading/tests/AC3/sentence-completion.json": {
  19: "Cevabin kendisi yerlesik bir sismoloji terimi ve cumle onun tanimini "
      "veriyor: 'tracks the ___ of the ground before and after a quake' zaten "
      "ground displacement'in tanimidir; model uc turda da yazdi (3/3 PUAN). "
      "ONE WORD ONLY sinirinda bu tanimi tasimayan bir cerceve kurulamiyor. "
      "E6 onerisi: B/2'nin gerekce yarisi - yontemin buzul altindaki ana kayayi "
      "gorebilmeyi gerektirmesi.",
  21: "Cevabin kendisi yerlesik bir buzulbilim terimi ve cumle onun tanimini "
      "veriyor: gunde 50 fit ilerleyen bir buzulun 'rapid ___ phase'i surge "
      "disinda adlandirilmiyor; model uc turda da yazdi (3/3 PUAN). Hizi "
      "cikarmak boslugu belirsizlestiriyor, birakmak terimi veriyor. E6 "
      "onerisi: F/1'in tarih yarisi - depremden haftalar once, kasim ayinda "
      "baslamis olmasi.",
 },
 "content/reading/tests/GT1/note-completion.json": {
  19: "Cevabin kendisi hukukla sabitlenmis bir sayi: Birlesik Krallik'ta tam "
      "zamanli calisanin yasal asgari yillik izni resmi tatiller dahil 28 "
      "gundur ve not satiri bu kosulun ikisini de ('full time', 'public "
      "holidays counted inside that total') veriyor; model uc turda da '28 "
      "days' yazdi (3/3 PUAN). Kosullari cikarmak sayiyi bulunamaz yapar. E6 "
      "onerisi: B metni A/1 yerine izin talebinin iki hafta onceden yapilmasi "
      "kurali - ama o yuva 20'de dolu oldugu icin baska bir paragraf secilmeli.",
 },
 "content/reading/tests/GT1/sentence-completion.json": {
  26: "Cevabin kendisi Ingilizce is dunyasinin yerlesik terimi: resmi tatil "
      "calismasinin karsiligi 'double time'dir ve cumle bir bucuk kat karsitligini "
      "vererek terimi dogrudan cagiriyor; model uc turda da yazdi (3/3 PUAN). "
      "Karsitligi kaldirmak cumleyi anlamsiz birakir. E6 onerisi: B metni C/1'in "
      "oteki yarisi - haftalik 37,5 saatlik esik.",
 },
}

# ----------------------------------------------------- STEM_BLOCK YAMALARI
# Soru metni ile ozet govdesindeki cumle her zaman birebir ayni degil (bas harf,
# kirpilmis yan cumle). Bu yuzden govde parca duzeyinde yamaniyor.
STEM = {
 "content/reading/practice/summary-completion.json": [
  ("The volume of code a team produced barely moved, which the authors read as a "
   "sign that seasoned (4)",
   "What the teams actually produced barely moved, which the authors read as a "
   "sign that seasoned (4)"),
  ("an order-balanced (6) ........ design that let every volunteer serve as "
   "their own comparison.",
   "in an order-balanced (6) ........ design."),
  ("tied partly to the roughly twofold gap in what the two groups earned and "
   "spent.",
   "tied partly to the gap in what the two groups earned and spent."),
 ],
 "content/reading/tests/AC1/summary-completion.json": [
  ("the island is now treated as an early (40) ........ .",
   "the island is now studied as a (40) ........ for the rest of the ocean."),
 ],
 "content/reading/tests/AC3/summary-completion.json": [
  ("only a very narrow band of (40) ........ — heat applied in an instant, then "
   "cooling almost at once — could have left the tissue",
   "only a very narrow band of (40) ........ could have left the tissue"),
 ],
 "content/reading/tests/GT1/summary-completion.json": [
  ("was (37) ........ from fruit and vegetables, chiefly the skins of bananas "
   "and mangoes.",
   "was (37) ........ from fruit and vegetables, above all from bananas and "
   "mangoes."),
 ],
 "content/reading/tests/AC1/note-completion.json": [
  ("- A tractor (4) ........ served the same purpose once the cube was taken away",
   "- A large (4) ........ pushed into place served the same purpose once the "
   "cube was taken away"),
 ],
}

# --------------------------------------------------------------- DOKUNULMAYAN
DOKUN = {
 "content/reading/practice/summary-completion.json": {
  3: "E5 / 8. calistirma: dokunulmadi. Model parcasiz uc turda threshold / limit "
     "/ threshold verdi; ayirt edici oge ('safe') hicbir turda gelmedi ve kabul "
     "listesi yalniz 'safe limits' kabul ettigi icin bu cevap 3 turun 0'inda "
     "puan alirdi. Bas ad ise cumlenin anlamsal rolunce zorunlu: 'gurultu "
     "onerilen ___ asti' cercevesinde ne yazilirsa yazilsin limit/esik okunur. "
     "Duzeltme yarim kalirdi. E6 bu yuvayi yeniden uretirse F/2'deki yuzde "
     "20-30 araligina capalamali.",
  8: "E5 / 8. calistirma: dokunulmadi. Model stressful / draining / stressful "
     "verdi, yani 3 turun 1'inde puan alirdi - 3/3 olcutunu karsilamiyor. "
     "Cumlenin bosluktan onceki yarisi (kotu ruh halinde artis, canlilikta "
     "dusus, tazelenmede yariya inme) G/2'nin gercek icerigi; onu kaldirmak "
     "kanit iliskisini koparirdi. Bosluga draining, depleting, tiring, wearing "
     "esit derecede uyuyor, yani cerceve zaten kilitli degil.",
  11: "E5 / 8. calistirma: dokunulmadi. Model uc turda da 'shells' verdi; kabul "
      "listesi 'eggshells' ve 'egg shells' kabul ettigi icin bu cevap 3 turun "
      "0'inda puan alirdi. Sizinti listenin kendisinde: 'skins, bones and ___' "
      "uclusunun kanonik tamamlamasi eggshells. Listeyi kisaltmak boslugu "
      "kapatmiyor, cok cevapli yapiyor - C/2 uc ogeyi de sayiyor, dolayisiyla "
      "'skins' ve 'bones' da gecerli cevap olurdu. E6 onerisi: C/2'nin sayisal "
      "yarisi (48 kilogramlik yenilemez pay).",
  14: "E5 / 8. calistirma: dokunulmadi. Model mortality / death / mortality "
      "verdi, yani 3 turun 2'sinde puan alirdi - sinirda ama 3/3 degil. Sizinti "
      "'illness and mortality' ikilisinin tip yazininda kaliplasmis olmasinda; "
      "ancak 'illness' sozcugunu ozetten kaldirmak boslugu cok cevapli yapar, "
      "cunku o zaman C/3'un kendi sozcugu 'illness' de gecerli bir cevap olur. "
      "🔴 E7 bu soruyu ayrica olcmeli: 2/3 puan orani kapsamin en yuksegi.",
 },
 "content/reading/tests/AC1/summary-completion.json": {
  37: "E5 / 8. calistirma: dokunulmadi. Model dye / stains / dye verdi, yani 3 "
      "turun 2'sinde puan alirdi. Bas ad cumlenin anlamsal rolunce zorunlu: "
      "'yeni buyumeyi ___ ile isaretlediler' cercevesinde bir isaretleme "
      "maddesi okunur ve D/2'de o maddenin adi zaten tek. Cerceveyi gevsetmek "
      "boslugu tags/markers gibi pasajda bulunmayan adaylara acar, yani soruyu "
      "yanitlanamaz yapar. 🔴 E7 ayrica olcmeli.",
 },
 "content/reading/tests/AC3/summary-completion.json": {
  36: "E5 / 8. calistirma: dokunulmadi. Model uc turda da 'decay' verdi; kabul "
      "listesi yalniz 'decomposition' kabul ettigi icin 3 turun 0'inda puan "
      "alirdi. Bas ad zorunlu: 'dokunun cok cabuk isitilmasi yuzunden siradan "
      "___ hic baslamadi' cercevesinde curume disinda bir kavram okunamaz. "
      "Sorunun gercek kusuru cerceve degil, kabul listesinin darligi - o da "
      "korunan bir alan.",
  37: "E5 / 8. calistirma: dokunulmadi. Model uc turda da 'databases' verdi; "
      "ayirt edici oge ('reference') hic gelmedi ve kabul listesi yalniz "
      "'reference database(s)' kabul ettigi icin 3 turun 0'inda puan alirdi. "
      "Bas ad zorunlu: 'beyin proteinlerinin ___ ile karsilastirilmasi' "
      "cercevesinde veri tabani disinda bir sey okunamaz. Duzeltme yarim "
      "kalirdi.",
 },
 "content/reading/tests/GT1/summary-completion.json": {
  38: "E5 / 8. calistirma: dokunulmadi. Model uc turda da 'fridge' verdi; kabul "
      "listesi yalniz 'refrigerator' kabul ettigi icin 3 turun 0'inda puan "
      "alirdi. Sorunun gercek kusuru sizinti degil kabul listesinin darligi: "
      "ONE WORD ONLY sinirinda 'fridge' pasajin dunyasinda dogru bir cevaptir "
      "ama anahtar reddediyor. Kabul listesi korunan alan oldugu icin bu "
      "calistirmada duzeltilemiyor. 🔴 E6/E7 bu yuvada anahtarin 'fridge'i de "
      "kabul etmesi gerekip gerekmedigine karar vermeli.",
 },
}


def sorular(d):
    if isinstance(d, dict):
        if "status" in d and "number" in d:
            yield d
        for v in d.values():
            yield from sorular(v)
    elif isinstance(d, list):
        for v in d:
            yield from sorular(v)


def main():
    dosyalar = sorted(set(list(DUZELT) + list(ELE) + list(DOKUN)))
    duzeltildi = elendi = dokunulmadi = 0
    devir = []
    for f in dosyalar:
        d = json.load(open(f, encoding="utf-8"))
        sb = d.get("stem_block")
        for q in sorular(d):
            n = q.get("number")

            if n in DUZELT.get(f, {}):
                yeni, aciklama, mek, ne = DUZELT[f][n]
                eski = q["prompt"]
                q["revision"] = {"tarih": TARIH, "mekanizma": mek,
                                 "onceki_prompt": eski, "ne_degisti": ne}
                q["prompt"] = yeni
                q["explanation"] = aciklama
                q["status"] = "verified"
                q["blind_solvable"] = None
                duzeltildi += 1

            elif n in ELE.get(f, {}):
                q["status"] = "rejected"
                q["reject_reason"] = ELE[f][n]
                devir.append({
                    "dosya": f, "numara": n,
                    "tip": d.get("question_type"),
                    "pasaj": q.get("passage_id") or d.get("passage_id"),
                    "kacinilacak": {
                        "kanit_cumlesi": q.get("evidence"),
                        "soru_metni": q.get("prompt"),
                    },
                    "neden_elendi": ELE[f][n],
                })
                elendi += 1

            elif n in DOKUN.get(f, {}):
                q["review_note"] = DOKUN[f][n]
                dokunulmadi += 1

        for eski_p, yeni_p in STEM.get(f, []):
            if eski_p not in sb:
                raise SystemExit("stem_block yamasi tutmadi: %s\n  %r" % (f, eski_p))
            sb = sb.replace(eski_p, yeni_p, 1)
        if sb is not None:
            d["stem_block"] = sb
        json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        open(f, "a", encoding="utf-8").write("\n")

    print("duzeltildi %d - elendi %d - dokunulmadi %d"
          % (duzeltildi, elendi, dokunulmadi))
    json.dump({"elenen": devir}, open("tools/_e5_ozet_devir_ara.json", "w",
                                      encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("devir icin hazirlanan kayit:", len(devir))


if __name__ == "__main__":
    main()
