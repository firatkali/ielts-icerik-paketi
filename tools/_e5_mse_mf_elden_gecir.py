# -*- coding: utf-8 -*-
"""E5 / 3. calistirma - cumle sonu eslestirme + ozellik eslestirme.

Kapsam: content/reading altinda question_type "matching_sentence_endings" ve
"matching_features" tasiyan dosyalardaki 28 isaretli soru.

Kural: answer / evidence / evidence_locator / numara / secenek harfleri
degismez. Yalniz soru metni (prompt), secenek METINLERI ve ic denetim notlari
yeniden yazilir. Betik idempotenttir: iki kez kosturulunca ayni sonucu verir.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

TARIH = "2026-08-08"

MSE = "content/reading/practice/matching-sentence-endings.json"
MF_P = "content/reading/practice/matching-features.json"
MF_1 = "content/reading/tests/AC1/matching-features.json"
MF_2 = "content/reading/tests/AC2/matching-features.json"
MF_3 = "content/reading/tests/AC3/matching-features.json"
MF_4 = "content/reading/tests/AC4/matching-features.json"

# --------------------------------------------------------------------------
# 1) Cumle sonu eslestirme - yeni son listeleri (harf -> metin)
# --------------------------------------------------------------------------

YENI_SONLAR = {
    "P-MSE-01": {
        "A": "curiosity about an object never seen before could not otherwise "
             "have been ruled out",
        "B": "the animal had no way of bringing that patch of skin into view "
             "by itself",
        "C": "she had been attending to the mark rather than to the reflection "
             "as such",
        "D": "animals of a species that can pass the test still vary widely in "
             "how they respond",
        "E": "little more than two hours of exposure had been enough to bring "
             "them out",
        "F": "the whales had built up some twenty-seven hours in front of it "
             "across the study",
        "G": "the glass held more attention than anything else in the pool",
        "H": "her reaction to being handled had to be told apart from her "
             "reaction to a visible mark",
    },
    "P-MSE-02": {
        "A": "it can widen a person's contacts and show future employers that "
             "they are reliable",
        "B": "some of the respondents had not given full details of what they "
             "earned",
        "C": "it was about the same size as the gap between two people five "
             "years apart in age",
        "D": "in Germany, the Netherlands and Norway more than four in ten "
             "took part regularly",
        "E": "unpaid work often has people on their feet rather than sitting "
             "still",
        "F": "volunteering goes together with being better educated and better "
             "off to begin with",
        "G": "the same result held up in every version of the analysis they ran",
        "H": "helping others may act on the hormones the body uses to handle "
             "stress",
    },
}

ORTAK_MSE = ("Sekiz sonun sekizi de ozne ve cekimli fiil tasiyan tam bir yan "
             "cumle; baslangictaki baglactan sonra hepsi dilbilgisi olarak "
             "isliyor, yani bicimden eleme yolu yine kapali. Degisen sey, "
             "artik her baslangic icin ayni cerceveye oturan en az bir rakip "
             "sonun bulunmasi: secim yalniz pasajdaki ayrintiyla yapilabiliyor.")

# --------------------------------------------------------------------------
# 2) Duzeltilen sorular: (dosya, numara) -> yeni alanlar
# --------------------------------------------------------------------------

DUZELTME = {

    # ---------------- cumle sonu eslestirme - A07 -------------------------
    (MSE, 1): dict(
        prompt="On some days a clear acrylic panel of the same size was "
               "lowered into the pool instead of the mirror, because",
        explanation="Paragraph B says the transparent panel of identical size "
                    "was used as a control, so that curiosity about a novel "
                    "object could be separated from a specific response to a "
                    "reflection.",
        grammar_check="Rakip son H: o da bir kontrol kosulunun gerekcesi "
                      "(sahte islem, D paragrafi) ve 'because' sonrasinda "
                      "kusursuz oturuyor. Cozucu artik iki kontrol gerekcesi "
                      "arasindan seffaf panelin hangisine hizmet ettigini "
                      "secmek zorunda; eskiden bu cerceveye uyan tek son A "
                      "idi. " + ORTAK_MSE,
        ne_degisti="Sonlar listesi yeniden yazildi. Eskiden her baslangica "
                   "yalniz tek bir son konu olarak uyuyordu; artik 1. "
                   "baslangicin karsisinda iki kontrol-kosulu gerekcesi var "
                   "(A: yeni nesneye merak, H: elle dokunmaya tepki). A'nin "
                   "metni de kanit cumlesinin sozcuklerinden uzaklastirildi "
                   "('novel object' -> 'an object never seen before').",
    ),
    (MSE, 2): dict(
        prompt="The full cluster of unusual actions had appeared in the very "
               "first mirror session for Natasha and Maris, which showed that",
        explanation="Paragraph C says these actions appeared within the very "
                    "first mirror session for two of the four animals, after "
                    "little more than two hours of exposure.",
        grammar_check="Rakip sonlar F ve G: F ayni pasajdan gelen toplam sure "
                      "(yaklasik yirmi yedi saat), G ise sureden cikarilabilecek "
                      "ama metnin desteklemedigi bir sonuc. Ucu de sure/ilgi "
                      "ekseninde oldugu icin cozucu 'toplam sure' ile 'ortaya "
                      "cikma suresi' arasindaki farki pasajdan okumak zorunda. "
                      + ORTAK_MSE,
        ne_degisti="Baslangic da son da tumden degisti. Eski ifade "
                   "('self-directed olarak sayildi cunku ... kendi bedenine "
                   "yonelikti') terimin tanimini sonun icine koyuyordu; sizinti "
                   "dogrudan sozluk esitligiydi. Yeni soru ayni kanit "
                   "cumlesinin oteki yarisini, davranislarin ne kadar cabuk "
                   "ortaya ciktigini hedefliyor ve karsisinda iki sure rakibi "
                   "var.",
    ),
    (MSE, 3): dict(
        prompt="The cosmetic mark was placed just behind an eye or an ear "
               "because",
        explanation="Paragraph D says the mark was applied to a part of the "
                    "body the whale could not see without a mirror, most often "
                    "just behind an eye or an ear.",
        grammar_check="Rakip son H: isaretle ilgili oteki gerekce, yani "
                      "dokunmaya verilen tepkiyi goruntuye verilen tepkiden "
                      "ayirma. Isaretin nereye konuldugu sorusuna da makul "
                      "duruyor, cunku sahte islem de ayni bolgeye uygulaniyor; "
                      "ayrim yalniz D paragrafindan cikiyor. " + ORTAK_MSE,
        ne_degisti="Sonun metni 'that patch of skin' anahtar sozcugunden "
                   "kurtarilmadi ama artik yalniz basina degil: isaret "
                   "cercevesinde ikinci bir son (H) var. Eskiden sekiz son "
                   "icinde isaretin konumundan soz eden tek secenek B idi.",
    ),
    (MSE, 4): dict(
        prompt="Natasha kept the marked patch of skin turned towards the "
               "mirror far longer than she did when the mark was invisible, "
               "which suggested that",
        explanation="Paragraph E treats the difference in duration between the "
                    "real mark and the sham mark as evidence that she was "
                    "inspecting the mark itself rather than simply enjoying "
                    "the mirror.",
        grammar_check="Rakip son G, pasajin acikca reddettigi karsit yorum: "
                      "'merely enjoying the mirror'. Iki son da sure farkindan "
                      "cikarilabilecek bir sonuc oneriyor, dolayisiyla secim "
                      "sahte isaret mantigini okumayi gerektiriyor; eskiden "
                      "sure ekseninde tek son C idi ve dilbilgisi olarak uyan "
                      "H anlamca tumden alakasizdi. " + ORTAK_MSE,
        ne_degisti="Baslangica sahte isaret karsilastirmasi acikca yazildi ve "
                   "sonlar listesine kanit cumlesinin kendisinin curuttugu "
                   "rakip yorum (G) eklendi. C'nin metni de kanittan "
                   "uzaklastirildi ('examining the mark itself and not merely "
                   "the glass' -> 'attending to the mark rather than to the "
                   "reflection as such').",
    ),
    (MSE, 5): dict(
        prompt="Maris never turned towards her own mark, and yet the team "
               "declined to treat this as a failure, taking it instead as a "
               "reminder that",
        explanation="Paragraph F says the researchers treated this not as a "
                    "failure but as a reminder that, even among species that "
                    "can pass the test, individual animals vary greatly in how "
                    "they respond.",
        grammar_check="Rakip son F: hayvanlarin aynanin onunde gecirdigi "
                      "toplam sure, Maris'in sonucunu hafifletici bir gerekce "
                      "olarak okunabilir ('yeterince firsati olmustu' degil, "
                      "'yeterince firsati vardi'). Metnin verdigi gerekce ise "
                      "bireysel degiskenlik; ayrim F/2'deki 'so much as' "
                      "kurulusundan okunuyor. " + ORTAK_MSE,
        ne_degisti="Baslangica Maris'in ne yapmadigi eklendi, boylece soru "
                   "'basarisizlik sayilmama' gerekcesini tek basina cagristiran "
                   "bir kalip olmaktan cikti; sonlar listesine ayni cerceveye "
                   "oturan bir rakip (F) kondu.",
    ),

    # ---------------- cumle sonu eslestirme - G06 -------------------------
    (MSE, 6): dict(
        prompt="Not everyone the survey reached ended up in the final sample "
               "of 42,926, because",
        explanation="Paragraph B says that after respondents with incomplete "
                    "income information had been excluded, the analysis covered "
                    "42,926 individuals.",
        grammar_check="Bu baslangicin cerceveye tam oturan tek rakibi yok; "
                      "sekiz son icinde orneklemden cikarilmayi anlatan tek "
                      "son B. Sayi baslangica tasindigi icin en azindan 'eksik "
                      "veri' kalibi tek basina yetmiyor, ama bu soru bu "
                      "calistirmada kismi duzeltilmis sayilir. " + ORTAK_MSE,
        ne_degisti="Baslangica orneklemin son buyuklugu (42.926) tasindi ve "
                   "sonun metni sadelestirildi. Kismi duzeltme: sekiz son "
                   "arasinda dislanmayi anlatan hala tek son var, bu yuzden "
                   "eleme yolu tamamen kapanmadi (E7 notu).",
    ),
    (MSE, 7): dict(
        prompt="The health gap was small on any single measure, but the "
               "authors were able to show that",
        explanation="Paragraph C says the size of the gap was similar to the "
                    "difference in reported health between men and women, or "
                    "between people five years apart in age.",
        grammar_check="Rakip son G: 'her cozumleme surumunde ayni sonuc "
                      "cikti' de yazarlarin gosterebildigi bir sey ve "
                      "baslangica kusursuz oturuyor. Ikisi arasindaki fark "
                      "buyukluk ile tutarlilik; secim C/2 ile G paragrafini "
                      "ayirt etmeyi gerektiriyor. " + ORTAK_MSE,
        ne_degisti="Baslangictaki 'somutlastirma' cagrisimi ('daha kolay "
                   "canlandirilabiliyor') kaldirildi; artik yalnizca "
                   "'gosterebildiler' deniyor, dolayisiyla buyukluk sonu ile "
                   "tutarlilik sonu ayni derecede cazip.",
    ),
    (MSE, 8): dict(
        prompt="Regular unpaid work was rare in Bulgaria, Hungary and "
               "Lithuania, whereas",
        explanation="Paragraph D says that more than four in ten respondents "
                    "in Germany, the Netherlands and Norway volunteered "
                    "regularly, compared with fewer than one in ten in the "
                    "three countries named.",
        grammar_check="Rakip son F: gonullulerle gonullu olmayanlar arasindaki "
                      "bir baska karsitlik (egitim ve gelir), ayni 'whereas' "
                      "kalibina oturuyor ve ayni paragrafin son cumlesinden "
                      "geliyor. Ulke ekseninin dogru olani D, ama artik "
                      "karsitlik yapisi tek basina D'yi isaret etmiyor. "
                      + ORTAK_MSE,
        ne_degisti="Baslangic korundu, son listesine ayni karsitlik kalibina "
                   "oturan ikinci bir aday (F) eklendi ve D'nin metnindeki "
                   "ulke listesi pasajin verdigi ucluye tamamlandi.",
    ),
    (MSE, 9): dict(
        prompt="Giving time freely might raise what a household earns, because",
        explanation="Paragraph E says volunteering can widen a person's "
                    "professional network, build skills and demonstrate "
                    "reliability to future employers, all of which might raise "
                    "household income.",
        grammar_check="Rakip son F, ters nedensellik: gonullulerin zaten daha "
                      "egitimli ve daha varlikli olmasi. Bu, geliri "
                      "aciklayabilecek ikinci bir yol olarak baslangica "
                      "kusursuz oturuyor ve pasajda gercekten yaziyor; yanlis "
                      "olmasinin nedeni yazarlarin kurdugu zincirin bu "
                      "olmamasi. " + ORTAK_MSE,
        ne_degisti="Sonlar listesine ters nedensellik rakibi (F) eklendi. "
                   "Eskiden sekiz son icinde gelirle iliskilendirilebilecek "
                   "tek son A idi, yani soru 'hangi son ekonomiden soz "
                   "ediyor' sorusuna iniyordu.",
    ),
    (MSE, 10): dict(
        prompt="Of the three possible explanations the authors offer, the "
               "middle one is that",
        explanation="Paragraph H lists three candidate explanations in order: "
                    "a sense of purpose and social connection, physical "
                    "activity, and an effect on stress-regulating hormones.",
        grammar_check="Rakip son H, ayni cumlenin ucuncu adayi (stres "
                      "hormonlari). Iki son da 'olasi aciklama' cercevesinde "
                      "ve ikisi de pasajda geciyor; ayrim yalniz siradan, yani "
                      "H/2'yi gercekten okumaktan cikiyor. Eskiden saglikla "
                      "iliskilendirilebilecek tek son E idi. " + ORTAK_MSE,
        ne_degisti="Baslangic 'saglik neden iyilessin' sorusundan "
                   "'yazarlarin siraladigi uc aciklamadan ortadaki hangisi' "
                   "sorusuna cevrildi ve listeye ucuncu aday (H) kondu; "
                   "boylece hareketin sagliga iyi geldigi genel bilgisi tek "
                   "basina cevabi vermiyor.",
    ),

    # ---------------- ozellik eslestirme - G05 ----------------------------
    (MF_P, 9): dict(
        prompt="The record kept for this group covered fewer days than the "
               "method used for the others.",
        explanation="Paragraph B says solid food waste was collected and "
                    "weighed over eight consecutive days, while discarded "
                    "drinks were recorded in a seven-day diary.",
        feature_check="Eski ifade olcum turunu ('tartilmak yerine yazili "
                      "gunluk') soruyordu; bes kategori icinde tek sivi olan E "
                      "bu turu pasaja bakmadan da ustune cekiyordu. Yeni ifade "
                      "olcumun SURESINI soruyor: kati atik sekiz gun boyunca "
                      "toplanip tartiliyor, icecek gunlugu yedi gun tutuluyor. "
                      "Kategorinin sivi olmasi bu farki vermiyor; A, B, C ve D "
                      "ancak B/1'deki sekiz gun okunarak elenebiliyor.",
        ne_degisti="Ifade, olcum yonteminden (gunluk / tarti) olcum suresine "
                   "(yedi gune karsi sekiz gun) tasindi. Boylece 'bes secenek "
                   "icinde tek icecek hangisiyse odur' kestirmesi kapandi; "
                   "cevap artik B paragrafindaki iki sayiyi karsilastirmayi "
                   "gerektiriyor.",
    ),
    (MF_P, 10): dict(
        prompt="The commonest reason for getting rid of this was that more "
               "had been prepared than anyone wanted to finish.",
        explanation="Paragraph F says coffee and tea were most often poured "
                    "away because a pot or cup had been made larger than "
                    "anyone actually wanted to finish.",
        feature_check="Karistirilabilecek oge A: G paragrafi 'bir ailenin "
                      "yiyebileceginden cok pirinc ya da yan yemek pisirmeyi' "
                      "de yaygin nedenler arasinda sayiyor, dolayisiyla asiri "
                      "hazirlama ifadesi artik pirince de uyuyor. Ayrim "
                      "'commonest' sozcugunde: G/2 pirincin kayiplarinin "
                      "cogunu bozulma ve kuflenmeye baglar, F/1 ise kahve ve "
                      "cay icin en sik nedenin fazla demlenmis olmasi "
                      "oldugunu soyler. B, C ve D icin verilen nedenler "
                      "bozulma, raf omru ve doku degisimi.",
        ne_degisti="Ifadeden 'icmek' fiili cikarildi. Eski metin ('anyone "
                   "wanted to drink') kategoriyi dogrudan soyluyordu; yeni "
                   "metin yalniz 'gereginden fazla hazirlama' diyor, bu da "
                   "pasajda hem pirinc hem icecekler icin geciyor. Cevap "
                   "artik hangi kategoride bu nedenin EN SIK oldugunu "
                   "okumayi gerektiriyor.",
    ),

    # ---------------- ozellik eslestirme - A02 (AC1) ----------------------
    (MF_1, 23): dict(
        prompt="Meetings in this group began more slowly, with the two "
               "animals often keeping their distance instead of touching.",
        explanation="Paragraph F says octopuses reunited with a familiar "
                    "partner took noticeably longer to make first contact and "
                    "were more likely to keep a cautious distance without "
                    "touching.",
        feature_check="Karistirilabilecek iki oge var. C: D paragrafi fiziksel "
                      "temasin uc gun boyunca seyreklestigini soyluyor, yani "
                      "'temas etmeden mesafe koruma' tarifi o doneme de "
                      "oturuyor. E: sezgi yabancilarin daha temkinli olacagini "
                      "soyler, oysa F/3 tam tersini veriyor - yabancilar daha "
                      "erken temas ediyor, daha cok dokunuyor. Dogru cevap D, "
                      "yalnizca F/2 okunarak bulunuyor.",
        ne_degisti="Ifadedeki ustunluk kalibi ('otekilerden daha uzun bekledi') "
                   "kaldirildi; bu kalip yedinci gun karsilastirmasini "
                   "isaret edip C'yi kendiliginden eliyordu. Yeni ifade "
                   "kanit cumlesinin iki yarisini (gec temas + mesafe koruma) "
                   "birlikte veriyor ve sezginin yanlis yone, E'ye, cektigi "
                   "bir soru haline geliyor.",
    ),
    (MF_1, 26): dict(
        prompt="Differences did turn up in this group, but they were weaker "
               "than the ones recorded later in the study.",
        explanation="Paragraph H says that vision alone, without touch or "
                    "water-borne chemical cues, produced weaker measurable "
                    "differences at the earlier stage, which is why the team "
                    "concludes that sight and physical contact together most "
                    "likely underlie recognition.",
        feature_check="Karistirilabilecek ogeler B ve C. B: hicbir duyuya izin "
                      "verilmeyen grup, sezgisel olarak 'en zayif fark' "
                      "beklenen yer - oysa pasaj zayif ama olculebilir farki "
                      "gorme izni olan gruba bagliyor. C: uc gunluk "
                      "birliktelikte de degisimler kaydediliyor, ama H/3'un "
                      "sozunu ettigi asama alistirma asamasi. Cevap ancak "
                      "H/3 okunarak A'ya gidiyor.",
        ne_degisti="Ifadeden 'gormek' sozcugu tumden cikarildi. Eski metin "
                   "('being able to see ... on its own') seffaf bolme "
                   "seceneginin adiyla birebir esleseyip cevabi sozcuk "
                   "duzeyinde veriyordu. Yeni ifade sonucun buyuklugunu "
                   "soruyor; yuzeydeki sezgi B'ye, dogru cevap A'ya gidiyor.",
    ),

    # ---------------- ozellik eslestirme - A05 (AC2) ----------------------
    (MF_2, 23): dict(
        prompt="Wheat found at this place had come through the centuries in "
               "better condition than grain of the same age recovered "
               "elsewhere.",
        explanation="Paragraph B says that the charred wheat grains recovered "
                    "from the site were unusually well preserved compared with "
                    "plant remains from other ancient sites of similar age.",
        feature_check="Karistirilabilecek oge C: en eski bugday bulgulariyla "
                      "anilan bolge oldugu icin 'iyi korunmus tane' ifadesi "
                      "sezgisel olarak oraya cekiyor. Ama pasaj C'yi yalniz "
                      "ehlilestirmenin izlendigi bolge olarak aniyor, oradan "
                      "cikan tanelerden hic soz etmiyor; korunma "
                      "karsilastirmasi B/1'de yalniz kazi yerine bagli. B ve "
                      "E de elenir: B ekimin baslangic yeri, E yalnizca "
                      "cozumlemenin yapildigi ulke.",
        ne_degisti="Ifadeden 'ekibin uzerinde calistigi tohumlar' kaydi "
                   "cikarildi; bu kayit dogrudan calismanin kazi yerini "
                   "isaret ediyordu. Yeni ifade yalniz korunma "
                   "karsilastirmasini soruyor, boylece sezgi Bereketli "
                   "Hilal'e (C) kayiyor ve dogru cevap ancak B/1'den "
                   "cikiyor.",
    ),

    # ---------------- ozellik eslestirme - A08 (AC3) ----------------------
    (MF_3, 23): dict(
        prompt="Within seconds of the first shaking, rock and ice broken loose "
               "by the quake were already coming down onto it.",
        explanation="Paragraph A says that within seconds the shaking tore "
                    "loose rock and ice from slopes above one of the region's "
                    "largest ice bodies.",
        feature_check="Karistirilabilecek ogeler E ve C. E: ayni cumle "
                      "heyelan ve ciglerin 'daglarin genis bir kusagi boyunca' "
                      "tetiklendigini soyluyor, dolayisiyla malzemenin "
                      "siradaginin uzerine dustugu dusunulebilir. C: F "
                      "paragrafi King George yakinlarindaki bir kol buzulunun "
                      "yeni enkazi tasidigini anlatiyor. Cumlenin adlandirdigi "
                      "hedef ise D; ayrim A/3'u okumayi gerektiriyor.",
        ne_degisti="Ifadeden 'ustunde duran yamaclar' kaydi cikarildi. Bu "
                   "kayit, secenekler icinde 'ustunde yamac bulunabilecek' tek "
                   "ogeyi kendiliginden isaret ediyordu (bir siradaginin "
                   "ustunde yamac olmaz). Yeni ifade yalniz malzemenin nereye "
                   "indigini soruyor; ayni cumledeki 'genis bir kusak boyunca' "
                   "kaydi E'yi gercek bir rakip yapiyor.",
    ),
    (MF_3, 24): dict(
        prompt="A single wide fall of debris down its side was the most "
               "conspicuous thing the earthquake produced anywhere in the "
               "range.",
        explanation="Paragraph D says the most conspicuous single event showed "
                    "up as a wide cascade of debris pouring down the flank of "
                    "this mountain.",
        feature_check="Karistirilabilecek oge B: ayni cumlede aniliyor, "
                      "ulkenin en yuksek tepesi oldugu icin 'en carpici olay' "
                      "sezgisini ustune cekiyor ve cevredeki heyelan izleriyle "
                      "birlikte veriliyor. Cumlenin ilk yarisi tek bir genis "
                      "enkaz akisini acikca C'ye bagliyor; ikinci yarisi B'ye "
                      "bagladigi sey tek bir akis degil, dagilmis izler.",
        ne_degisti="Ifade 25 numarayla kurdugu tamamlayicilik iliskisinden "
                   "kurtarildi ve pasajin kendi olcegine ('en carpici tek "
                   "olay') capalandi. Sezgi B'ye (Kanada'nin en yuksek "
                   "tepesi) gidiyor, dogru cevap D/1'i okumayi gerektiriyor.",
    ),
    (MF_3, 25): dict(
        prompt="Fresh scars left by slipping ground could be picked out in the "
               "country around it.",
        explanation="Paragraph D says that further landslide scars were "
                    "visible around this mountain.",
        feature_check="Karistirilabilecek ogeler C ve E. C: enkaz akisi da "
                      "yeni bir kopma izi birakiyor, dolayisiyla 'yeni izler' "
                      "ifadesi ona da uyuyor; ayrim izlerin dagin CEVRESINDE "
                      "gorulmesinde. E: izler bir siradaginin geneline degil, "
                      "adi verilen bir zirvenin cevresine baglanmis.",
        ne_degisti="Ifadeden 'ama en buyuk tek akis orada degildi' kaydi "
                   "cikarildi. Bu kayit 24 ile 25'i birbirinin tersi haline "
                   "getiriyordu: birini bilen otekini pasaja bakmadan "
                   "cikarabiliyordu. Iki soru artik birbirinden bagimsiz iki "
                   "ayrintiya capalanmis durumda.",
    ),
    (MF_3, 26): dict(
        prompt="The epicentre is placed at a distance of about ninety "
               "kilometres from it.",
        explanation="Paragraph A says the epicentre lay in remote terrain "
                    "roughly 90 kilometres north of this coastal town.",
        feature_check="Karistirilabilecek oge E: acilis cumlesi depremin "
                      "St Elias Daglari'nda oldugunu soyledigi icin uzakligin "
                      "siradagdan olculdugu dusunulebilir. D de rakip, cunku "
                      "ayni paragrafta merkez ussuyle birlikte aniliyor. "
                      "Mesafenin olculdugu nokta yalniz A/2 okunarak "
                      "bulunuyor.",
        ne_degisti="Ifadeden 'kiyidaki bu yerlesim' tanimi cikarildi. Bu "
                   "tanim, bes secenek icinde tek yerlesim olan ogeyi tur "
                   "uyusmasiyla dogrudan veriyordu; geri kalanlar dag, buzul "
                   "ya da siradag adi. Yeni ifade yalniz mesafeyi soruyor.",
    ),

    # ---------------- ozellik eslestirme - A11 (AC4) ----------------------
    (MF_4, 25): dict(
        prompt="Of the falls recorded after the campus session, this was the "
               "only one whose size was actually given.",
        explanation="Paragraph G says that after the building condition, "
                    "restorativeness scores dropped by roughly half compared "
                    "with their level beforehand; the other declines are "
                    "reported without a figure.",
        feature_check="Karistirilabilecek ogeler D ve B: ayni cumlede ikisinin "
                      "de dustugu soyleniyor (oznel canlilik geriledi, olumlu "
                      "duygular azaldi), ama ikisi icin de bir buyukluk "
                      "verilmiyor. 'Yaklasik yariya inme' olcusu yalniz "
                      "dinlendiricilik puanlarina bagli. Olcegin adi bu kez "
                      "yardim etmiyor, cunku soru dususun kendisini degil "
                      "sayilastirilmis olmasini soruyor.",
        ne_degisti="Ifade 'bina kosulundan sonra yariya indi' bicimindeki "
                   "dogrudan bulgudan, 'dususlerden hangisi sayiyla verildi' "
                   "sorusuna cevrildi. Boylece 'dinlendiricilik olcegi bina "
                   "gorunce en cok duser' bicimindeki ad-sezgisi devre disi "
                   "kaliyor; cozucu G/2'yi okumak zorunda.",
    ),
    (MF_4, 26): dict(
        prompt="It runs to twenty items, more than two of the other three but "
               "far fewer than the longest.",
        explanation="Paragraph E says this is a shorter, 20-item scale; the "
                    "Profile of Mood States has 65 items, the Restorative "
                    "Outcome Scale six and the Subjective Vitality Scale four.",
        feature_check="Karistirilabilecek oge A: 'en uzun degil ama kisa da "
                      "sayilmaz' tarifi, madde sayilari bilinmeden hicbir "
                      "olcege baglanamiyor. C (alti madde) ve D (dort madde) "
                      "yirmiden kisa, A (altmis bes madde) acik ara en uzun; "
                      "dolayisiyla tarif yalniz B'ye oturuyor ama bu ancak "
                      "E paragrafindaki dort sayi okunarak gorulebiliyor.",
        ne_degisti="Ifade olcegin ne olctugunden ('duygu yelpazesinin iki "
                   "ucu') madde sayisina tasindi. Eski metin, seceneklerden "
                   "birinin ADININ ('Positive and Negative Affect Schedule') "
                   "birebir cevirisiydi; yeni metin adin tasimadigi bir "
                   "ayrintiya, uzunluk siralamasina capalaniyor.",
    ),
}

# --------------------------------------------------------------------------
# 3) Elenen sorular: (dosya, numara) -> reject_reason
# --------------------------------------------------------------------------

ELENEN = {
    (MF_P, 1): "Sorunun ekseni ofis kulturu genel bilgisi: acik plan ofisin "
               "oteki duzenlerden daha gurultulu oldugu yaygin bir kani, soru "
               "da dort duzenden en gurultulusunu soruyor. Ifade nasil "
               "yazilirsa yazilsin cevap pasajdan degil bu kanidan cikiyor; "
               "kanit cumlesi (F/2) zaten yalniz 'hangisi en gurultuluydu' "
               "sorusunu destekliyor, baska bir eksene capalanamiyor.",
    (MF_P, 5): "Sorunun ekseni yine acik plan ofis hakkindaki yaygin kani: "
               "calisanlarin en az geri donmek istedigi duzenin sade acik ofis "
               "olmasi beklenen sonuc. Kanit cumlesi (H/1) uc bulguyu birlikte "
               "veren bir ozet cumlesi ve ucu de ayni duzeni gosteriyor, yani "
               "ifadeyi baska bir ayrintiya tasimak da mumkun degil.",
    (MF_2, 24): "Sorunun ekseni dunya tarihi genel bilgisi: basit bugdaylarin "
                "yaklasik on iki bin yil once Bereketli Hilal'de "
                "ehlilestirildigi, okul duzeyinde bilinen en yaygin tarih "
                "onermelerinden biri. Kanit cumlesi (G/2) yalniz bu onermeyi "
                "tasiyor; kapsam sozcuklerini ('genis alan') temizlemek "
                "ekseni degistirmiyor, cevap yine bes secenek icinden genel "
                "bilgiyle secilebiliyor.",
    (MF_2, 25): "Sorunun ekseni arkeoloji genel bilgisi: Karacadag'in "
                "einkorn ekiminin dogdugu yer olarak anilmasi, ayni kanit "
                "cumlesinde duran ve alanin disindan da bilinen spesifik bir "
                "bilgi. Kanit cumlesi degismeden ifadenin dayanabilecegi "
                "baska bir ayrinti yok.",
    (MF_2, 26): "Sorunun ekseni tarimin Bereketli Hilal'den Avrupa'ya "
                "yayildigi anlatisi; bu anlati ders kitabi duzeyinde "
                "bilindigi icin 'yayilmanin gittigi yon' sorusunun cevabi "
                "secenekler arasinda pasaja bakmadan bulunabiliyor. Kanit "
                "cumlesi (A/3) yolun ucundaki yeri adlandirmaktan baska bir "
                "sey soylemiyor.",
    (MF_4, 24): "Sorunun ekseni psikolojik olcme araclari genel bilgisi: "
                "Profile of Mood States'in alti ayri duygu boyutu olctugu "
                "yaygin bilinen bir bilgi ve ifadedeki 'olculen hos olmayan "
                "durumlarin cogu' kaydi altidan bese dogal olarak oturuyor. "
                "Kanit cumlesi (F/1) 'alti olumsuz duygu durumundan besi' "
                "kalibini tasidigi icin, ifade nasil yazilirsa yazilsin ayni "
                "arac bilgisine geri donuyor.",
}

# --------------------------------------------------------------------------
# 4) Dokunulmayan sorular
# --------------------------------------------------------------------------

DOKUNULMAYAN = {
    (MF_1, 25): "Sizinti ifadenin kipinde degil, SECENEK LISTESININ kendisinde: "
                "kanit cumlesi (C/3) yalniz bolmenin isik gecirip gecirmedigini "
                "soyluyor, secenek metinleri de gruplari tam olarak bu "
                "ozellikle adlandiriyor ('see-through screen' / 'solid "
                "screen'). Ilk asamayla ilgili her ifade bu yuzden sozcuk "
                "duzeyinde cozuluyor. Duzeltmek icin ya kanit cumlesini ya da "
                "secenek listesini degistirmek gerekir; talimat ikisini de bu "
                "adimin disinda biraktigi icin soru oldugu gibi kaldi. E6'nin "
                "yeniden uretim kapsamina alinmasi ve gruplarin bolme turuyle "
                "degil asama/sira ile adlandirilmasi yerinde olur.",
}


def uygula():
    sayac = dict(duzeltildi=0, elendi=0, dokunulmadi=0)
    dosyalar = [MSE, MF_P, MF_1, MF_2, MF_3, MF_4]

    for yol in dosyalar:
        d = ortak.oku(yol)

        # cumle sonu eslestirmede once secenek metinleri
        for g in (d.get("groups") or []):
            yeni = YENI_SONLAR.get(g.get("group_id"))
            if not yeni:
                continue
            eski = {o["key"]: o["text"] for o in g["option_list"]["options"]}
            if eski != yeni:
                g.setdefault("revision", {})
                g["revision"] = {
                    "tarih": TARIH,
                    "mekanizma": "konumsal_duzen",
                    "onceki_sonlar": eski,
                    "ne_degisti": "Sekiz sonun metni yeniden yazildi. Harfler "
                                  "ve harf-cevap eslesmesi korundu; degisen "
                                  "sey, her baslangica artik ayni cerceveden "
                                  "en az bir rakip sonun eslik etmesi.",
                }
            for o in g["option_list"]["options"]:
                o["text"] = yeni[o["key"]]

        for g, it in ortak.kumeli_sorular(d):
            anahtar = (yol, it.get("number"))

            if anahtar in DUZELTME:
                y = DUZELTME[anahtar]
                if it.get("status") != "verified":
                    it["revision"] = {
                        "tarih": TARIH,
                        "mekanizma": it.get("flag_mechanism"),
                        "onceki_prompt": it["prompt"],
                        "ne_degisti": y["ne_degisti"],
                    }
                it["prompt"] = y["prompt"]
                it["explanation"] = y["explanation"]
                if "feature_check" in y:
                    it["feature_check"] = y["feature_check"]
                if "grammar_check" in y:
                    it["grammar_check"] = y["grammar_check"]
                it["status"] = "verified"
                it["blind_solvable"] = None
                sayac["duzeltildi"] += 1

            elif anahtar in ELENEN:
                it["status"] = "rejected"
                it["reject_reason"] = ELENEN[anahtar]
                sayac["elendi"] += 1

            elif anahtar in DOKUNULMAYAN:
                it["review_note"] = DOKUNULMAYAN[anahtar]
                sayac["dokunulmadi"] += 1

        ortak.yaz(yol, d)

    print("duzeltildi %d - elendi %d - dokunulmadi %d"
          % (sayac["duzeltildi"], sayac["elendi"], sayac["dokunulmadi"]))
    print("toplam %d" % sum(sayac.values()))


if __name__ == "__main__":
    uygula()
