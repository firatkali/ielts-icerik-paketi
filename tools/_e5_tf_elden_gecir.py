# -*- coding: utf-8 -*-
"""E5 / 6. calistirma - TRUE/FALSE/NOT GIVEN + kalan tekiller.

Kural: answer / evidence / evidence_locator / numara / secenek harfleri
degismez. Yalniz ifade (prompt), baslik listesindeki KULLANILMAYAN harflerin
metinleri ve ic denetim notlari (explanation, scan_note, contradiction_point,
not_given_justification, revision, reject_reason, review_note) yeniden yazilir.
Betik idempotenttir.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

TARIH = "2026-08-08"

P_TF = "content/reading/practice/true-false-not-given.json"
P_MH = "content/reading/practice/matching-headings.json"
P_MI = "content/reading/practice/matching-information.json"
P_YN = "content/reading/practice/yes-no-not-given.json"
P_SUM = "content/reading/practice/summary-completion.json"
AC1_TF = "content/reading/tests/AC1/true-false-not-given.json"
AC1_MF = "content/reading/tests/AC1/matching-features.json"
AC2_TF = "content/reading/tests/AC2/true-false-not-given.json"
AC2_MH = "content/reading/tests/AC2/matching-headings.json"
AC2_FC = "content/reading/tests/AC2/flow-chart-completion.json"
AC3_TF = "content/reading/tests/AC3/true-false-not-given.json"
AC3_MH = "content/reading/tests/AC3/matching-headings.json"
AC3_MI = "content/reading/tests/AC3/matching-information.json"
AC3_TC = "content/reading/tests/AC3/table-completion.json"
AC4_TF = "content/reading/tests/AC4/true-false-not-given.json"
AC4_MH = "content/reading/tests/AC4/matching-headings.json"
AC4_NC = "content/reading/tests/AC4/note-completion.json"
GT1_TF = "content/reading/tests/GT1/true-false-not-given.json"
GT1_MH = "content/reading/tests/GT1/matching-headings.json"
GT2_TF = "content/reading/tests/GT2/true-false-not-given.json"

DOSYALAR = [P_TF, P_MH, P_MI, P_YN, P_SUM, AC1_TF, AC1_MF, AC2_TF, AC2_MH,
            AC2_FC, AC3_TF, AC3_MH, AC3_MI, AC3_TC, AC4_TF, AC4_MH, AC4_NC,
            GT1_TF, GT1_MH, GT2_TF]

# ---------------------------------------------------------------------------
# 1) Duzeltilen sorular
# ---------------------------------------------------------------------------

DUZELTME = {

    # --- practice / TFNG ---------------------------------------------------
    (P_TF, 3): {
        "mekanizma": "eksen_disi_ayrinti",
        "prompt": "In each pair, the animal that came to dominate was the "
                  "heavier of the two.",
        "explanation": "Paragraph B says the two animals in a pair were "
                       "matched to differ in weight by no more than fifteen "
                       "per cent, and paragraph D says a dominance hierarchy "
                       "emerged in every pair, but the passage never says "
                       "whether the dominant animal was the heavier one.",
        "not_given_justification": "(1) Konu pasajda var: B paragrafi "
            "esleme olcutunu ve tek tek agirliklari, D paragrafi her ciftte "
            "bir baskinlik siralamasi olustugunu veriyor. (2) Ifadeyi curuten "
            "cumle yok: baskin hayvanin hafif olan oldugu hicbir yerde "
            "soylenmiyor. (3) Dogrulayan cumle de yok: metin agirligi ve "
            "baskinligi ayri ayri veriyor, ikisini hicbir yerde "
            "caprazlamiyor.",
        "scan_note": "Agirlik B paragrafinin 1. ve 2. cumlelerinde, "
                     "baskinlik D paragrafinin 2. cumlesinde ve F "
                     "paragrafinda (baskinligin tersine donmesi) geciyor; "
                     "hicbiri iki olcuyu birbirine baglamiyor.",
        "ne_degisti": "Eski ifade oturumlarin gunun ayni saatinde yapilip "
                      "yapilmadigini soruyordu; pasajin hic konusmadigi bir "
                      "boyut (gunun saati) ekleyen bu kalip tek basina NOT "
                      "GIVEN'i veriyordu. Yeni ifade metnin bol bol "
                      "konustugu iki ekseni (agirlik eslemesi ve baskinlik "
                      "siralamasi) kesistiriyor; ikisi de ayrintisiyla "
                      "veriliyor ama hic caprazlanmiyor.",
    },

    (P_TF, 7): {
        "mekanizma": "eksen_disi_ayrinti",
        "prompt": "Each of the two laboratories analysed the same samples "
                  "independently of the other.",
        "explanation": "Paragraph D says the extraction and analysis were "
                       "carried out in two physically separate laboratories "
                       "so that the ancient samples would not be "
                       "contaminated, but it never says whether the two "
                       "laboratories duplicated each other's work or divided "
                       "it between them.",
        "not_given_justification": "(1) Konu pasajda var: D paragrafinin 1. "
            "cumlesi iki laboratuvari ve neden ayri tutulduklarini "
            "anlatiyor. (2) Ifadeyi curuten cumle yok: isin bolusuldugu "
            "hicbir yerde soylenmiyor. (3) Dogrulayan cumle de yok: ayni "
            "orneklerin iki kez, bagimsiz olarak incelendigi de "
            "soylenmiyor.",
        "scan_note": "Iki laboratuvar yalniz D paragrafinin 1. cumlesinde "
                     "geciyor; D'nin geri kalani isaretleyici uzunluklarini "
                     "ve dizilemeyi anlatiyor, E paragrafi sonuclari veriyor.",
        "ne_degisti": "Eski ifade dizilemenin kac ay surdugunu soruyordu; "
                      "pasajin hic vermedigi bir sure ayrintisi ekleyen bu "
                      "kalip tek basina NOT GIVEN'i veriyordu. Yeni ifade "
                      "metnin ayrintisiyla anlattigi iki laboratuvarli "
                      "duzenegi hedefliyor; is bolusumunun bicimi metinde "
                      "karara baglanmiyor.",
    },

    (P_TF, 8): {
        "mekanizma": "genel_kultur",
        "prompt": "Catalhoyuk is described as the place where the spread of "
                  "hexaploid wheat came to an end.",
        "explanation": "Paragraph G describes Catalhoyuk as a possible "
                       "staging point on the spread of hexaploid wheat "
                       "towards Europe, that is, a place along the route "
                       "rather than the point at which that spread stopped.",
        "contradiction_point": "Pasaj Catalhoyuk'u yayilmanin Avrupa'ya "
            "dogru surdugu yol ustundeki bir durak sayiyor; ifade ise "
            "yayilmanin orada bittigini soyluyor. Celiski tek noktada: ara "
            "durak / son nokta.",
        "scan_note": "Catalhoyuk'un yayilmadaki rolu G paragrafinin 3. "
                     "cumlesinde; A paragrafi da yerlesimin ilerideki tarim "
                     "yollari uzerinde bulundugunu soyluyor, H paragrafi ayni "
                     "yonu yineliyor.",
        "ne_degisti": "Eski ifade bugday evcillestirmesinin Bereketli Hilal "
                      "merkezli klasik anlatisini soruyordu; bu ders kitabi "
                      "bilgisi oldugu icin cevap pasaja bakilmadan "
                      "cikiyordu. Yeni ifade ayni kanit cumlesinin oteki "
                      "yarisini, Catalhoyuk'a bicilen rolu hedefliyor; 'ara "
                      "durak mi son nokta mi' ayrimi yalniz G/3'ten "
                      "yapilabiliyor.",
    },

    (P_TF, 10): {
        "mekanizma": "eksen_disi_ayrinti",
        "prompt": "The ground survey of 12 December covered the slopes of "
                  "Mount Logan as well as those of Mount King George.",
        "explanation": "Paragraph D names both Mount King George and Mount "
                       "Logan and reports that a ground survey on 12 December "
                       "confirmed what the satellite images had shown, but it "
                       "never says which slopes that survey actually visited.",
        "not_given_justification": "(1) Konu pasajda var: D paragrafinin 1. "
            "cumlesi iki dagi adiyla aniyor, 2. cumlesi 12 Aralik'taki yer "
            "arastirmasini anlatiyor. (2) Ifadeyi curuten cumle yok. (3) "
            "Dogrulayan cumle de yok: arastirmanin kapsami hicbir yerde "
            "verilmiyor.",
        "scan_note": "Iki dagin adi D paragrafinin 1. cumlesinde, yer "
                     "arastirmasi 2. cumlesinde geciyor; B ve C paragraflari "
                     "uydu verisini anlatiyor, arastirmanin hangi yamaclari "
                     "kapsadigina hicbiri deginmiyor.",
        "ne_degisti": "Eski ifade arastirmacilarin araziye yuruyerek gidip "
                      "gitmedigini soruyordu; pasajda hic karsiligi olmayan "
                      "bir ulasim ayrintisi ekleyen bu kalip tek basina NOT "
                      "GIVEN'i veriyordu. Yeni ifade metnin ayrintisiyla "
                      "verdigi iki dagi ve yer arastirmasini birlikte "
                      "hedefliyor; kapsam metinde karara baglanmiyor.",
    },

    (P_TF, 11): {
        "mekanizma": "kalip_beklentisi",
        "prompt": "The debris shaken loose by the earthquake is being carried "
                  "inland, away from the coast.",
        "explanation": "Paragraph F says the surging glacier is carrying the "
                       "newly generated avalanche and landslide debris "
                       "steadily downhill towards the sea, that is, towards "
                       "the coast rather than away from it.",
        "contradiction_point": "Pasaj enkazin denize dogru tasindigini "
            "soyluyor; ifade ic kesimlere, kiyidan uzaga tasindigini iddia "
            "ediyor. Celiski tek noktada: tasimanin yonu.",
        "scan_note": "Enkazin tasinmasi F paragrafinin 2. cumlesinde; A ve D "
                     "paragraflari enkazin nerede olustugunu anlatiyor, "
                     "yonunden soz etmiyor.",
        "ne_degisti": "Eski ifade depremin buzulun hizli ilerleyisini "
                      "durdurdugunu soyluyordu; 'buyuk bir sarsinti surmekte "
                      "olan bir sureci durdurur mu' kalibi doga "
                      "pasajlarinda neredeyse her zaman FALSE cikar. Yeni "
                      "ifade ayni kanit cumlesindeki tasima yonunu "
                      "hedefliyor; deniz mi ic kesim mi sorusu hicbir genel "
                      "kaliptan cikarilamiyor.",
    },

    (P_TF, 13): {
        "mekanizma": "genel_kultur",
        "prompt": "The volcanic material that sealed the town built up over "
                  "more than a single day.",
        "explanation": "Paragraph A says the town was sealed beneath roughly "
                       "20 metres of volcanic deposits over the following "
                       "days, so the covering accumulated over more than one "
                       "day, even though the flows themselves killed "
                       "residents almost instantly.",
        "scan_note": "Gomulmenin suresi A paragrafinin 3. cumlesinde geciyor "
                     "('over the following days'); ayni cumle olumlerin "
                     "'neredeyse aninda' gerceklestigini de soyluyor, iki "
                     "ayri zaman olcegi bilincli olarak yan yana duruyor.",
        "ne_degisti": "Eski ifade kumasin baska Roma sitelerinde ender "
                      "gorulen bir durumda korunmasini soruyordu; "
                      "Herculaneum'un organik malzemeyi esssiz bicimde "
                      "korumasi arkeolojinin en cok bilinen olgularindan "
                      "biri. Yeni ifade ayni cumlenin oteki yarisini, ortu "
                      "tabakasinin ne kadar surede olustugunu hedefliyor; "
                      "yaygin sezgi 'kasaba bir anda gomuldu' dedigi icin "
                      "sezgi artik YANLIS yone gidiyor, dogru cevap yalniz "
                      "A/3'teki 'over the following days' ibaresinden "
                      "cikiyor.",
    },

    (P_TF, 15): {
        "mekanizma": "genel_kultur",
        "prompt": "The brain tissue is thought to have melted into a liquid "
                  "before hardening into glass.",
        "explanation": "Paragraph C says the tissue was converted directly "
                       "into a glass-like solid; no intermediate liquid stage "
                       "is described anywhere in the passage, so the "
                       "statement contradicts it.",
        "contradiction_point": "Pasaj dokunun DOGRUDAN cam benzeri bir kati "
            "hale gectigini soyluyor; ifade once sivilasip sonra "
            "katilastigini iddia ediyor. Celiski tek noktada: 'dogrudan' "
            "gecis / ara sivi asamasi.",
        "scan_note": "Donusumun bicimi C paragrafinin 1. cumlesinde, gereken "
                     "kosullar 2. cumlesinde, isil kosullarin dar araligi G "
                     "paragrafinda anlatiliyor; hicbirinde sivi bir ara "
                     "asamadan soz edilmiyor.",
        "ne_degisti": "Eski ifade kafatasindaki koyu maddenin mineral "
                      "cokelti olup olmadigini soruyordu; camlasmis beyin "
                      "dokusu bulgusu bilim haberciliginde genis yer buldugu "
                      "icin cevap pasajsiz cikiyordu. Yeni ifade ayni "
                      "cumledeki 'directly' sozcugunu hedefliyor; "
                      "camlasmanin malzeme biliminde bir sivinin hizla "
                      "sogutulmasi demek olmasi, bilgili bir cozucuyu TRUE'ya "
                      "iterek sezgiyi ters yone ceviriyor.",
    },

    # --- AC1 / TFNG --------------------------------------------------------
    (AC1_TF, 7): {
        "mekanizma": "genel_kultur",
        "prompt": "The puzzles at which elephants had failed required an "
                  "animal to raise itself up in order to reach food.",
        "explanation": "Paragraph A describes the insight puzzles as ones in "
                       "which an animal suddenly stacks boxes to reach food "
                       "hung out of reach, so the task required the animal to "
                       "lift itself towards the food.",
        "scan_note": "Bulmacanin bicimi A paragrafinin 3. cumlesinde "
                     "geciyor; B paragrafi ayni duzenegi (asili meyve, agir "
                     "kup, bambu sopa) kuruyor ama 'icgoru bulmacasi' "
                     "tanimini vermiyor.",
        "ne_degisti": "Eski ifade fillerin icgoru testlerindeki tarihsel "
                      "basarisizligini soruyordu; bu, hayvan bilisi "
                      "literaturunun bilinen bir tartismasi oldugu icin cevap "
                      "pasajsiz cikiyordu. Yeni ifade ayni cumlenin oteki "
                      "yarisini, bulmacanin fiziksel bicimini hedefliyor: "
                      "'kutu ustune cikip yukselme' ayrintisi metne "
                      "bakilmadan bilinemez.",
    },

    (AC1_TF, 9): {
        "mekanizma": "genel_kultur",
        "prompt": "Kandula broke off partway through his first successful "
                  "attempt and came back to it later.",
        "explanation": "Paragraph C says the behaviour appeared abruptly, in "
                       "a single uninterrupted sequence, so it was not broken "
                       "off and resumed later.",
        "contradiction_point": "Pasaj davranisin tek ve kesintisiz bir dizi "
            "halinde ortaya ciktigini soyluyor; ifade girisimin yarida "
            "birakilip sonra surduruldugunu iddia ediyor. Celiski tek "
            "noktada: kesintisizlik.",
        "scan_note": "Cozumun ortaya cikis bicimi C paragrafinin 3. ve 4. "
                     "cumlelerinde, ayrica H paragrafinda ('the sudden, "
                     "error-free appearance') geciyor; ikisi de kesintiye yer "
                     "birakmiyor.",
        "ne_degisti": "Eski ifade davranisin deneme-yanilmayla kademeli "
                      "gelisip gelismedigini soruyordu; 'icgoru' kavraminin "
                      "tanimi geregi ani olmasi genel psikoloji bilgisi. "
                      "Yeni ifade ayni cumledeki 'single uninterrupted "
                      "sequence' ibaresini hedefliyor; girisimin yarida "
                      "kesilip kesilmedigi metne bakilmadan bilinemez.",
    },

    (AC1_TF, 12): {
        "mekanizma": "genel_kultur",
        "prompt": "According to the authors, the earlier experiments failed "
                  "because the elephants were offered no tool at all.",
        "explanation": "Paragraph F says the authors blame the tools that "
                       "previous experiments had offered, which means tools "
                       "were offered; the problem was that a stick did not "
                       "suit the animal's trunk.",
        "contradiction_point": "Pasaj yazarlarin sucu 'onceki deneylerin "
            "SUNDUGU araclara' attigini soyluyor, yani arac sunulmustu; ifade "
            "hic arac sunulmadigini iddia ediyor. Celiski tek noktada: aracin "
            "sunulmus olmasi.",
        "scan_note": "Yazarlarin aciklamasi F paragrafinin 2. cumlesinde; B "
                     "paragrafi deneyde bambu bir sopanin sunuldugunu ayrica "
                     "soyluyor, F/3-4 sopanin neden ise yaramadigini "
                     "anlatiyor.",
        "ne_degisti": "Eski ifade yazarlarin basarisizligi hayvanin zekasina "
                      "baglayip baglamadigini soruyordu; beklenmedik bir "
                      "hayvan basarisini anlatan metinlerin gecmis "
                      "basarisizligi 'arac yanlisti' diye aciklamasi cok "
                      "yaygin bir anlati kalibi. Yeni ifade ayni cumleyi "
                      "tersten, 'arac sunulmus muydu' ekseninden soruyor; bu "
                      "ayrinti yalniz F/2 ile B paragrafindan cikiyor.",
    },

    (AC1_TF, 13): {
        "mekanizma": "eksen_disi_ayrinti",
        "prompt": "The bamboo stick was taken out of the enclosure once "
                  "Kandula began using the cube.",
        "explanation": "The passage says a bamboo stick was offered at the "
                       "start and later explains why sticks suit elephants "
                       "poorly, but it never says whether the stick was "
                       "removed once the animal began using the cube.",
        "not_given_justification": "(1) Konu pasajda var: B paragrafi bambu "
            "sopanin sunuldugunu, F paragrafi sopanin neden ise yaramadigini "
            "anlatiyor. (2) Ifadeyi curuten cumle yok: sopanin ortamda kaldigi "
            "hicbir yerde soylenmiyor. (3) Dogrulayan cumle de yok: D "
            "paragrafinda kaldirilan nesne kupun kendisi, sopa degil.",
        "scan_note": "Bambu sopa B paragrafinin 4.-5. cumlelerinde ve F "
                     "paragrafinin 3.-4. cumlelerinde geciyor; D "
                     "paragrafinda kaldirilan nesne kup. Sopanin ne zaman "
                     "ortadan kalktigi hicbir paragrafta yok.",
        "ne_degisti": "Eski ifade kupun ustundeyken yiyecegi daha iyi gorup "
                      "gormedigini soruyordu; pasajin hic ele almadigi bir "
                      "duyu kanali (gorme) ekleyen bu kalip tek basina NOT "
                      "GIVEN'i veriyordu. Yeni ifade metnin bol bol "
                      "konustugu bir nesneyi, bambu sopayi hedefliyor; "
                      "sopanin ne zaman kaldirildigi karara baglanmiyor.",
    },

    # --- AC2 / TFNG --------------------------------------------------------
    (AC2_TF, 10): {
        "mekanizma": "genel_kultur",
        "prompt": "The orbits of the small inner moons are affected by the "
                  "planet's rings as well as by one another.",
        "explanation": "Paragraph E says the orbits of these small, closely "
                       "spaced bodies interact with one another and with the "
                       "planet's faint rings, so both influences are stated.",
        "scan_note": "Ic uydularin yorunge etkilesimi E paragrafinin 3. "
                     "cumlesinde; G paragrafinin 2. cumlesi ayni etkilesimi "
                     "'karmasik kutlecekim iliskileri' olarak yineliyor.",
        "ne_degisti": "Eski ifade 'bu kadar cok ve birbirine yakin cismi "
                      "izlemek uzmanlar icin bile zordur' diyordu; cok-cisim "
                      "probleminin zorlugu genel fizik bilgisi oldugu icin "
                      "cevap pasajsiz cikiyordu. Yeni ifade ayni cumlenin "
                      "oteki yarisini, etkilesimin halkalari da kapsayip "
                      "kapsamadigini hedefliyor; halkalarin isin icinde "
                      "olmasi pasaja ozgu bir ayrinti.",
    },

    (AC2_TF, 11): {
        "mekanizma": "genel_kultur",
        "prompt": "What kept the moon out of sight was its size rather than "
                  "its distance from Earth.",
        "explanation": "Paragraph F says it was the moon's size that placed "
                       "it below the threshold Voyager's instruments and "
                       "Earth-based telescopes could resolve, so size rather "
                       "than distance is given as the reason it went unseen.",
        "scan_note": "Gorunmezligin nedeni F paragrafinin 3. cumlesinde; C "
                     "paragrafi da cismin dogrudan olculemeyecek kadar kucuk "
                     "oldugunu soyluyor. Uzaklik hicbir yerde neden olarak "
                     "gosterilmiyor.",
        "ne_degisti": "Eski ifade ucus sonrasinda yer teleskoplarinin da "
                      "goremedigini soyluyordu; yer teleskoplarinin uzay "
                      "araclarindan daha sinirli oldugu yaygin bilgisiyle "
                      "cevap pasajsiz cikiyordu. Yeni ifade ayni cumlenin "
                      "NEDEN kismini hedefliyor: boyut mu uzaklik mi sorusu "
                      "iki secenek de makul oldugu icin ancak F/3 okunarak "
                      "yanitlanabiliyor.",
    },

    (AC2_TF, 12): {
        "mekanizma": "genel_kultur",
        "prompt": "Tiscareno maintains that the difference between a ring and "
                  "a moon has always been clear-cut.",
        "explanation": "Paragraph G reports Tiscareno as saying the line "
                       "between ring and moon may not always have been as "
                       "clear as it is today, which contradicts the claim "
                       "that the distinction has always been clear-cut.",
        "contradiction_point": "Pasaj halka ile uydu arasindaki cizginin "
            "gecmiste bugunku kadar net olmayabilecegini soyluyor; ifade "
            "ayrimin her zaman net oldugunu iddia ediyor. Celiski tek "
            "noktada: ayrimin gecmisteki netligi.",
        "scan_note": "Tiscareno'nun sozleri G paragrafinin 2. cumlesinde; A "
                     "ve E paragraflari halka-uydu sistemini tanitiyor ama "
                     "ayrimin netligine deginmiyor.",
        "ne_degisti": "Eski ifade 'baska bir gezegen daha fazla kucuk ic "
                      "uyduya sahiptir' diyordu; kesif haberlerinin konu "
                      "gezegeni benzersiz gosterme kalibi yuzunden cevap "
                      "pasajsiz cikiyordu. Yeni ifade ayni cumlenin ikinci "
                      "yarisini, halka ile uydu arasindaki sinirin tarihsel "
                      "netligini hedefliyor.",
    },

    (AC2_TF, 13): {
        "mekanizma": "eksen_disi_ayrinti",
        "prompt": "A name taken from Shakespeare has already been put forward "
                  "for the new moon.",
        "explanation": "Paragraph E explains the naming tradition and says "
                       "the newcomer's eventual name will need formal "
                       "approval, but it never says whether any particular "
                       "name has yet been proposed.",
        "not_given_justification": "(1) Konu pasajda var: E paragrafinin 2. "
            "cumlesi adlandirma gelenegini ve onay surecini ayrintisiyla "
            "anlatiyor. (2) Ifadeyi curuten cumle yok. (3) Dogrulayan cumle de "
            "yok: metin yalniz 'eventual name' diyor, herhangi bir adin "
            "onerildigini soylemiyor.",
        "scan_note": "Adlandirma E paragrafinin 2. cumlesinde; C paragrafi "
                     "gecici tanimlamayi (S/2025 U1) veriyor, o da bir ad "
                     "onerisi degil.",
        "ne_degisti": "Eski ifade ekibin bulguyu bir yil icinde yayina "
                      "gonderme niyetini soruyordu; pasajda hic gecmeyen bir "
                      "takvim ayrintisi ekleyen bu kalip tek basina NOT "
                      "GIVEN'i veriyordu. Yeni ifade metnin ayrintisiyla "
                      "anlattigi adlandirma surecini hedefliyor; bir ad "
                      "onerilip onerilmedigi karara baglanmiyor.",
    },

    # --- AC4 / TFNG --------------------------------------------------------
    (AC4_TF, 7): {
        "mekanizma": "genel_kultur",
        "prompt": "The company where the study was carried out has more than "
                  "five thousand staff at its main site.",
        "explanation": "Paragraph A says the technology company that ran the "
                       "study has 5,580 employees at its main campus, which "
                       "is more than five thousand.",
        "scan_note": "Calisan sayisi A paragrafinin 4. cumlesinde; B "
                     "paragrafi deneye katilan 288 kisiyi ve 22 takimi "
                     "veriyor, bunlar kampusun toplami degil orneklem.",
        "ne_degisti": "Eski ifade calismanin kontrollu kanit eksikligi "
                      "yuzunden yapildigini soyluyordu; bir tartismayi "
                      "'kisisel izlenime dayaniyor' diye cerceveleyip "
                      "arastirmanin gerekcesi yapmak akademik girislerin "
                      "standart kalibi. Yeni ifade ayni cumledeki sayiyi "
                      "(5.580) hedefliyor; bes bin esigi ancak A/4 okunarak "
                      "dogrulanabiliyor.",
    },

    (AC4_TF, 13): {
        "mekanizma": "kalip_beklentisi",
        "prompt": "How energetic employees said they felt did not differ "
                  "significantly between the four layouts.",
        "explanation": "Paragraph G says that neither the number of software "
                       "code commits nor employees' self-reported energy "
                       "levels showed a statistically significant difference "
                       "between the four layouts.",
        "scan_note": "Enerji olcumu G paragrafinin 2. cumlesinde kod commit "
                     "sayisiyla birlikte veriliyor; C paragrafi enerjinin "
                     "anketle olculdugunu, D ve E paragraflari degisen "
                     "olcumleri (memnuniyet, uretkenlik, akis) ayri ayri "
                     "veriyor.",
        "ne_degisti": "Eski ifade kod uretiminin duzenden etkilenmedigini "
                      "soyluyordu; ofis calismalarinda OZNEL olcumlerin "
                      "degisip NESNEL ciktinin degismemesi bilinen bir "
                      "arastirma orgusu oldugu icin cevap pasajsiz cikiyordu. "
                      "Yeni ifade ayni cumlenin oteki yarisini, oznel bir "
                      "olcumun (kendi bildirdikleri enerji) degismedigini "
                      "hedefliyor; ayni orgu bu kez YANLIS yone isaret "
                      "ediyor, dogru cevap yalniz G/2'den cikiyor.",
    },

    # --- GT1 / TFNG --------------------------------------------------------
    (GT1_TF, 8): {
        "mekanizma": "genel_kultur",
        "prompt": "A book returned fifty days late costs no more in charges "
                  "than one returned thirty days late.",
        "explanation": "Text A says overdue items are charged at 20 pence a "
                       "day up to a maximum of five pounds per item; the "
                       "maximum is reached after 25 days, so an item returned "
                       "thirty days late and one returned fifty days late "
                       "both incur the same five-pound charge.",
        "scan_note": "Gecikme ucreti A metninin 4. cumlesinde; ayni metnin 3. "
                     "cumlesi odunc suresini (uc hafta) veriyor, ucretle "
                     "ilgili baska bir kayit yok.",
        "ne_degisti": "Eski ifade gecikme ucretinde bir ust sinir bulunup "
                      "bulunmadigini soruyordu; kutuphane cezalarinin eser "
                      "basina sinirli olmasi cok yaygin bir uygulama. Yeni "
                      "ifade ayni cumledeki iki sayiyi (gunluk 20 peni, ust "
                      "sinir 5 sterlin) birlikte kullanmayi gerektiriyor: ust "
                      "sinira 25. gunde ulasildigi ancak hesapla goruluyor.",
    },

    (GT1_TF, 9): {
        "mekanizma": "genel_kultur",
        "prompt": "The library is open for eight hours on a Saturday.",
        "explanation": "Text A says the library opens on Saturday from 10 "
                       "a.m. to 4 p.m., which is six hours, not eight.",
        "contradiction_point": "Metin cumartesi saatlerini 10.00-16.00 "
            "veriyor, yani alti saat; ifade sekiz saat diyor. Celiski tek "
            "noktada: acik kalinan saat sayisi.",
        "scan_note": "Acilis saatleri A metninin 5. cumlesinde: hafta ici "
                     "9.00-19.00, cumartesi 10.00-16.00, pazar ve resmi "
                     "tatillerde kapali.",
        "ne_degisti": "Eski ifade cumartesi saatlerinin hafta iciyle ayni "
                      "olup olmadigini soruyordu; kamu hizmetlerinde "
                      "cumartesinin daha kisa olmasi cok yaygin oldugu icin "
                      "cevap metne bakilmadan cikiyordu. Yeni ifade ayni "
                      "cumleden bir sure hesabi istiyor (10.00-16.00 = alti "
                      "saat); sekiz saat esigi hicbir genel kuraldan "
                      "cikarilamaz.",
    },

    (GT1_TF, 10): {
        "mekanizma": "belirsiz",
        "prompt": "Both of the weekly beginner swimming sessions start at the "
                  "same time of day.",
        "explanation": "Text B says beginner swimming is held on Tuesdays and "
                       "Thursdays at 6 p.m., so both sessions start at the "
                       "same time.",
        "scan_note": "Yeni baslayanlar yuzme dersi B metninin 2. cumlesinde; "
                     "ayni metnin 3. cumlesi yogayi sabah 9.30'a, 4. cumlesi "
                     "badmintonu cumartesi 10.00'a koyuyor.",
        "ne_degisti": "Eski ifade dersin haftada kac kez yapildigini "
                      "soruyordu; E1 bunu 'net mekanizma yok, dogruluk "
                      "buyuk olcude sansa dayaniyor' diye isaretlemisti, "
                      "cunku 'sali ve persembe' ile 'haftada iki kez' "
                      "arasindaki eslesme tek adimlik bir cikarim ve gunluk "
                      "hayatta yeni baslayan kurslari cogunlukla haftada iki "
                      "gundur. Yeni ifade ayni cumledeki saat bilgisini "
                      "hedefliyor: iki oturumun ayni saatte olup olmadigi "
                      "metinden baska hicbir yerden bilinemez.",
    },

    (GT1_TF, 12): {
        "mekanizma": "genel_kultur",
        "prompt": "Credit can only be added to the travel card at a station "
                  "machine.",
        "explanation": "Text C says the card can be loaded with credit at any "
                       "station machine or through the free mobile app, so a "
                       "machine is not the only way.",
        "contradiction_point": "Metin krediyi hem istasyon makinesinden hem de "
            "ucretsiz mobil uygulamadan yuklenebilecegini soyluyor; ifade tek "
            "yolun makine oldugunu iddia ediyor. Celiski tek noktada: "
            "uygulama uzerinden yukleme secenegi.",
        "scan_note": "Kredi yukleme C metninin 1. cumlesinde; ayni metnin "
                     "geri kalani ucretleri, cocuk indirimini, gecis kuralini "
                     "ve kart degisimini anlatiyor.",
        "ne_degisti": "Eski ifade uygulamanin indirilmesinin ucretli olup "
                      "olmadigini soruyordu; resmi ulasim uygulamalarinin "
                      "ucretsiz olmasi neredeyse evrensel bir bilgi. Yeni "
                      "ifade ayni cumledeki 'or' baglacini hedefliyor: kac "
                      "yukleme kanali oldugu ancak C/1 okunarak bilinir.",
    },

    # --- GT2 / TFNG --------------------------------------------------------
    (GT2_TF, 9): {
        "mekanizma": "kip_imzasi",
        "prompt": "Visitors may bring their own food into the festival.",
        "explanation": "Text B says the food stalls accept card payment only "
                       "and that camping is not permitted, but it says "
                       "nothing about whether visitors may bring food of "
                       "their own.",
        "not_given_justification": "(1) Konu metinde var: B metninin son "
            "cumlesi hem yiyecek standlarini hem de bir yasagi (kamp) "
            "duzenliyor. (2) Ifadeyi curuten kayit yok: disaridan yiyecek "
            "getirmenin yasak oldugu hicbir yerde yazmiyor. (3) Dogrulayan "
            "kayit da yok: izin verildigi de soylenmiyor.",
        "scan_note": "Yiyecek standlari ve yasaklar B metninin son "
                     "cumlesinde; ayni metnin oteki cumleleri saatleri, "
                     "biletleri ve cocuk girisini anlatiyor. Baska hicbir "
                     "metin festivalden soz etmiyor.",
        "ne_degisti": "Eski ifade festivalin 'her yil' Castle Park'ta "
                      "yapildigini soyluyordu; metnin yalniz 'bu yilki "
                      "festival' demesine karsi kurulan bu kapsam genislemesi "
                      "tek basina NOT GIVEN'i veriyordu. Yeni ifadede hicbir "
                      "kapsam ya da siklik sozcugu yok; metnin gercekten "
                      "duzenledigi bir alanda (yiyecek ve yasaklar) karara "
                      "baglanmamis bir ayrinti soruluyor.",
    },

    (GT2_TF, 10): {
        "mekanizma": "genel_kultur",
        "prompt": "Tickets valid for a single day are not sold for every day "
                  "of the festival.",
        "explanation": "Text B says the festival runs from Friday to Sunday "
                       "but that day tickets are available only for Friday "
                       "and Saturday, so single-day tickets are not sold for "
                       "every day.",
        "scan_note": "Bilet turleri B metninin 3. cumlesinde; ayni metnin 1. "
                     "cumlesi festivalin cuma-pazar surdugunu soyluyor, iki "
                     "cumle birlikte okunmadan cevap cikmiyor.",
        "ne_degisti": "Eski ifade onceden alinan biletin kapida alinandan "
                      "ucuz olup olmadigini soruyordu; erken bilet indirimi "
                      "evrensel bir fiyatlandirma kurali. Yeni ifade ayni "
                      "cumledeki 'only for Friday and Saturday' kaydini "
                      "festival takvimiyle birlikte okumayi gerektiriyor.",
    },

    (GT2_TF, 11): {
        "mekanizma": "genel_kultur",
        "prompt": "A plot holder may leave up to a quarter of the plot "
                  "uncultivated without breaking the rules.",
        "explanation": "Text C says plot holders must keep at least 75 per "
                       "cent of the plot cultivated, which leaves up to a "
                       "quarter that may be left uncultivated.",
        "scan_note": "Ekim orani ve yeniden tahsis C metninin 3. cumlesinde; "
                     "C/1 bekleme listesini, C/2 kirayi, C/4 yapi iznini "
                     "anlatiyor.",
        "ne_degisti": "Eski ifade parselin baskasina verilmesinden once yazili "
                      "uyari yapilip yapilmadigini soruyordu; bir hakkin geri "
                      "alinmasindan once yazili uyari verilmesi yaygin bir "
                      "idari adillik kurali. Yeni ifade ayni cumledeki %75 "
                      "esigini yuzde hesabiyla hedefliyor.",
    },

    (GT2_TF, 13): {
        "mekanizma": "kip_imzasi",
        "prompt": "Classes that are cancelled are offered again later in the "
                  "year.",
        "explanation": "Text E says classes with fewer than six enrolled "
                       "students by the Friday before term begins are "
                       "cancelled, but it never says whether such classes are "
                       "offered again later.",
        "not_given_justification": "(1) Konu metinde var: E metninin son "
            "cumlesi iptal kuralini ayrintisiyla veriyor (alti kisiden az, "
            "terim oncesi cuma). (2) Ifadeyi curuten kayit yok. (3) "
            "Dogrulayan kayit da yok: iptal edilen dersin sonradan yeniden "
            "acilip acilmadigi hic soylenmiyor.",
        "scan_note": "Iptal kurali E metninin son cumlesinde; ayni metin "
                     "kayit takvimini, ucretleri ve indirimi veriyor, telafi "
                     "ya da yeniden acilma konusuna hic girmiyor.",
        "ne_degisti": "Eski ifade comlekciligin 'en populer' ders olup "
                      "olmadigini soruyordu; hicbir ragbet siralamasi "
                      "verilmeyen bir metinde kurulan bu ustunluk kalibi tek "
                      "basina NOT GIVEN'i veriyordu. Yeni ifadede ustunluk ya "
                      "da kapsam sozcugu yok; metnin acikca duzenledigi iptal "
                      "kuralinin karara baglanmamis bir yani soruluyor.",
    },

    (GT2_TF, 14): {
        "mekanizma": "belirsiz",
        "prompt": "Job seekers are entitled to the same reduction as "
                  "students.",
        "explanation": "Text E says concessions of 50 per cent are available "
                       "to job seekers and to students with valid "
                       "identification, so both groups receive the same "
                       "reduction.",
        "scan_note": "Indirim E metninin 3. cumlesinde geciyor; ayni cumle "
                     "ucret araligini (60-110 sterlin) de veriyor, "
                     "indirimden yararlanan baska bir grup sayilmiyor.",
        "ne_degisti": "Eski ifade gecerli kimlikli ogrencilerin standart "
                      "ucretin yarisini odeyip odemedigini soruyordu; %50 "
                      "ogrenci indirimi yaygin bir uygulama oldugu icin '50' "
                      "ile 'yari' eslesmesi metne bakilmadan kurulabiliyordu. "
                      "Yeni ifade indirimin ogrencilere OZGU olup olmadigini "
                      "soruyor; is arayanlarin da ayni indirimi almasi yalniz "
                      "E/3'ten cikiyor.",
    },

    # --- matching_information ---------------------------------------------
    (P_MI, 6): {
        "mekanizma": "konumsal_duzen",
        "prompt": "a general pattern in the field that this particular find "
                  "is said to illustrate",
        "explanation": "Paragraph H says the discovery illustrates a broader "
                       "pattern in planetary astronomy: each generation of "
                       "instruments reveals objects that the previous "
                       "generation's technology could not see.",
        "ne_degisti": "Eski soru kokunde 'hakem degerlendirmesinden gecmemis "
                      "olma itirafi' vardi; 'peer-reviewed' kavraminin "
                      "pasajda tek bir karsiligi oldugu icin dogru paragraf "
                      "metne bakilmadan bulunabiliyordu. Yeni kok ayni "
                      "cumlenin ikinci yarisini, gezegen astronomisi icin "
                      "cikarilan genel oruntuyu hedefliyor; F paragrafi "
                      "(Voyager'in goremeyisi) ve C paragrafi (boyutun "
                      "tahminle bulunmasi) artik gercek rakip, cunku ikisi de "
                      "ayni fikrin tekil ornekleri.",
    },

    (AC3_MI, 28): {
        "mekanizma": "konumsal_duzen",
        "prompt": "a reference to a second town where the same kind of "
                  "preservation cannot be taken for granted",
        "explanation": "Paragraph H says the finding cannot be assumed to "
                       "apply broadly across other victims at Herculaneum or "
                       "Pompeii, naming a second town where the same "
                       "preservation cannot be taken for granted.",
        "ne_degisti": "Eski kok ('baska kurbanlar icin ayni seyin "
                      "varsayilmamasi uyarisi') pasajda tek bir cumleye "
                      "birebir oturuyordu; G'deki dar isil kosul sinirlamasi "
                      "ve C'deki 'ender bulunma' kaydi kolayca eleniyordu. "
                      "Yeni kok ayni cumlede gecen ikinci kasaba adini "
                      "hedefliyor; A paragrafi da Pompeii'yi anip iki "
                      "kasabanin gomulme bicimini karsilastirdigi icin artik "
                      "gercek bir rakip, ayrim ancak paragraflar okunarak "
                      "yapilabiliyor.",
    },

    # --- matching_headings (baslik listesi grup duzeyinde duzeltiliyor) ----
    (P_MH, 11): {
        "mekanizma": "konumsal_duzen",
        "ne_degisti": "Baslik listesindeki iki olu harf yeniden yazildi (vi, "
                      "viii). B paragrafinin rakibi artik iv ('An everyday "
                      "habit, and an open question'), yani A paragrafinin "
                      "gercek konusu; anlati sirasindan 'B = tasarim' diye "
                      "okunmasi engellendi.",
    },
    (P_MH, 14): {
        "mekanizma": "konumsal_duzen",
        "ne_degisti": "Eski celdirici viii ('Why some pairs were harder to "
                      "learn') pasajda hic karsiligi olmadigi icin okumadan "
                      "eleniyordu; yerine G paragrafinin gercek savini tasiyan "
                      "'Why some memories need a whole night' kondu. E "
                      "paragrafinin sonucunu aciklayan bu baslik artik gercek "
                      "bir rakip.",
    },
    (P_MH, 15): {
        "mekanizma": "konumsal_duzen",
        "ne_degisti": "Eski celdirici ii ('The stages that make up a night's "
                      "sleep') paragrafin tanitmadigi bir konuyu adlandirdigi "
                      "icin eleniyordu; yerine F paragrafinin ilk cumlesinin "
                      "gercek icerigi ('The internal make-up of the daytime "
                      "naps') kondu. Artik F'nin ilk cumlesi ile ana fikri iki "
                      "ayri basliga karsilik geliyor, secim ancak paragrafin "
                      "tamami okunarak yapilabiliyor.",
    },
    (AC2_MH, 14): {
        "mekanizma": "konumsal_duzen",
        "ne_degisti": "Eski celdirici ix ('Storage methods that kept the "
                      "harvest edible') pasajda hic karsiligi olmadigi icin "
                      "okumadan eleniyordu; yerine B paragrafinin ilk "
                      "cumlesinin gercek icerigi ('Remains better preserved "
                      "than at comparable sites') kondu. Ayrica olu vi basligi "
                      "C ve H paragraflarindaki 'tane bicimi yaniltir' savina "
                      "capalandi. B artik iki basligin arasinda.",
    },
    (AC3_MH, 14): {
        "mekanizma": "konumsal_duzen",
        "ne_degisti": "Baslik listesindeki tek olu harf (x, 'A glacier stopped "
                      "in its tracks') pasajin acikca curuttugu bir iddiaydi "
                      "ve okumadan eleniyordu; yerine G paragrafinin gercek "
                      "icerigi ('New dangers for climbers and expeditions') "
                      "kondu. B paragrafinin rakibi olan vii ('A tally of the "
                      "slopes that failed') zaten B/1'e capalanmis durumda, "
                      "yani secim artik yalniz paragrafin ana fikrini tartarak "
                      "yapilabiliyor.",
    },
    (AC4_MH, 17): {
        "mekanizma": "konumsal_duzen",
        "ne_degisti": "Eski celdirici x ('How long each questionnaire took to "
                      "complete') pasajda hic verilmeyen bir olcuyu "
                      "adlandirdigi icin okumadan eleniyordu; yerine E "
                      "paragrafinin gercekten verdigi madde sayilari ('The "
                      "number of items in each scale') kondu. E artik iki "
                      "basligin arasinda ve secim ana fikri tartmayi "
                      "gerektiriyor.",
    },
    (AC4_MH, 18): {
        "mekanizma": "konumsal_duzen",
        "ne_degisti": "Eski celdirici i ('A surprising rise in participants' "
                      "energy') pasajin acikca curuttugu bir iddiaydi; yerine "
                      "G paragrafinin gercek bulgusu ('The reverse pattern at "
                      "the second site') kondu, olu iv basligi da H "
                      "paragrafinin karin acikladigi savina capalandi. F "
                      "paragrafinin karsisinda artik ayni cerceveden iki rakip "
                      "var.",
    },
    (GT1_MH, 31): {
        "mekanizma": "konumsal_duzen",
        "ne_degisti": "Iki olu baslik yeniden yazildi: v ('How the amounts "
                      "changed across the seasons') metnin acikca "
                      "olcmedigini soyledigi bir seyi adlandiriyordu, yerine G "
                      "metninin gercek icerigi ('The reasons householders "
                      "themselves gave') kondu; x ('Why one district earns "
                      "more than another') pasajda aciklanmayan bir nedeni "
                      "adlandiriyordu, yerine H metninin gercek icerigi ('What "
                      "rural families did with their scraps') kondu. E "
                      "paragrafinin rakibi vii zaten E/3'e capalanmis "
                      "durumda.",
    },
}

# ---------------------------------------------------------------------------
# 2) Baslik listelerinde yeniden yazilan KULLANILMAYAN harfler
#    (dogru cevap olan hicbir harfe dokunulmuyor)
# ---------------------------------------------------------------------------

BASLIK = {
    P_MH: {
        "P-MH-03": {
            "ii": ("The stages that make up a night's sleep",
                   "The internal make-up of the daytime naps"),
            "vi": ("How the puzzle game changed the scores",
                   "Practical advice for people who rely on naps"),
            "viii": ("Why some pairs were harder to learn",
                     "Why some memories need a whole night"),
        },
    },
    AC2_MH: {
        None: {
            "vi": ("The difficulty of dating buried seeds",
                   "Why the shape of a grain can mislead"),
            "ix": ("Storage methods that kept the harvest edible",
                   "Remains better preserved than at comparable sites"),
        },
    },
    AC3_MH: {
        None: {
            "x": ("A glacier stopped in its tracks",
                  "New dangers for climbers and expeditions"),
        },
    },
    AC4_MH: {
        None: {
            "i": ("A surprising rise in participants' energy",
                  "The reverse pattern at the second site"),
            "iv": ("The health risks of standing in severe cold",
                   "Why the snow may have hidden one effect"),
            "vii": ("An urban view chosen to create stress",
                    "A calm city scene used for comparison"),
            "x": ("How long each questionnaire took to complete",
                  "The number of items in each scale"),
        },
    },
    GT1_MH: {
        None: {
            "v": ("How the amounts changed across the seasons",
                  "The reasons householders themselves gave"),
            "x": ("Why one district earns more than another",
                  "What rural families did with their scraps"),
        },
    },
}

# ---------------------------------------------------------------------------
# 3) Elenen sorular
# ---------------------------------------------------------------------------

ELEME = {

    (P_TF, 4): (
        "Kanit cumlesi (F/3) tek bir yon soyluyor: yabanci ciftler daha erken "
        "etkilesime giriyor, daha sik dokunuyor ve birlikte daha uzun vakit "
        "geciriyor. Cumleden cikarilabilecek her dogru ifade 'yabancilar "
        "tanidiklardan daha cok etkilesime girer' bicimini aliyor; yenilik "
        "arayisi davranis biyolojisinin en yaygin genellemelerinden biri "
        "oldugu icin cevap ifade nasil yazilirsa yazilsin pasaja bakilmadan "
        "cikiyor. Cumlede pasaja ozgu tek bir sayi ya da ad da yok. E6 bu "
        "yuvayi F paragrafinin sayisal ayrintilarina capalamali (baskinligin "
        "tersine dondugu on iki yabanci ciftin sekizi, ya da son sinamada hic "
        "murekkep birakilmamasi)."
    ),

    (AC1_TF, 10): (
        "Kanit cumlesi (D/3) yalniz 'yiyecek yeri degistiginde Kandula kupu "
        "yeni noktaya yuvarladi' diyor; bu cumleden cikarilabilecek her dogru "
        "ifade 'akilli hayvan yeni duruma uyum sagladi' bicimini aliyor. Uyum "
        "saglama, akilli hayvan calismalarinin standart kanit yapisi olarak "
        "beklendigi icin cevap eksen degistirilmeden kapanmiyor; ekseni "
        "degistirmek ise kanit cumlesini degistirmek demek, talimat bunu "
        "yarim duzeltme sayiyor. E6 bu yuvayi D paragrafinin sayisal ya da "
        "nesnel ayrintilarina capalamali (ayni oturumda dokuz kez tekrarlamasi, "
        "kup kaldirilinca traktor lastigine gecmesi, kucuk nesneleri ust uste "
        "koyma denemesinin basarisiz olmasi)."
    ),

    (AC3_TF, 7): (
        "Kanit cumlesi (A/3) ayna testinin gercekte neyi olctugu tartismasini "
        "ozetliyor: 'gercek oz farkindalik mi yoksa daha dar bir sey mi'. Bu "
        "tartisma hayvan bilisinin en cok aktarilan tartismalarindan biri ve "
        "cumlenin iki yarisi da (tartismanin varligi, testin yine de en net "
        "davranissal isaret sayilmasi) alan bilgisinden dogrudan cikiyor. "
        "Cumlede pasaja ozgu tek bir sayi, ad ya da olcu yok, dolayisiyla "
        "ifade nasil yazilirsa yazilsin eksen genel kultur kaliyor. E6 bu "
        "yuvayi B paragrafinin sayisal ayrintilarina capalamali (98 oturum, "
        "aynanin onunde 27 saate karsi seffaf panelin onunde 23 saat)."
    ),

    (AC1_MF, 25): (
        "3. calistirma bu soruyu dokunulmadan birakmis ve gerekcesini "
        "review_note alanina yazmisti: sizinti ifadenin kipinde degil, kanit "
        "cumlesi ile secenek listesinin arasinda. Kanit cumlesi (C/3) yalniz "
        "bolmenin isik gecirip gecirmedigini soyluyor, secenek metinleri de iki "
        "grubu tam olarak bu ozellikle adlandiriyor (see-through screen / solid "
        "screen); ilk asamayla ilgili nasil yazilirsa yazilsin her ifade bu iki "
        "etiketten birine sozcuk duzeyinde baglaniyor. Duzeltmek icin ya kanit "
        "cumlesini ya secenek listesini degistirmek gerekiyor, talimat ikisini "
        "de yarim duzeltme saydigi icin yuva bu calistirmada elenenlere "
        "alindi. E6 icin en temiz cozum secenek listesini bolme turuyle degil "
        "asama/sira ile adlandirmak (ornegin 'ilk uc gunu ayri geciren birinci "
        "yari'); bu, AC1-26'yi da guclendirir."
    ),

    (P_YN, 11): (
        "1. calistirma bu soruyu dokunulmadan birakmis ve gerekcesini "
        "review_note alanina yazmisti: sizinti ifadenin kipinde degil, kanit "
        "cumlesinin kendisinde. G/1 'The pattern after the building condition "
        "was essentially the reverse' diyor; bu kanita dayanan her NO ifadesi "
        "'kontrol kosulu tedavi kosuluyla ayni sonucu vermez' deney mantigiyla "
        "parcasiz cozulebiliyor. Ifadeyi olculu yazmak yetmiyor, farkli bir "
        "kanit cumlesi gerekiyor; talimat kanit degisimini yarim duzeltme "
        "saydigi icin yuva bu calistirmada elenenlere alindi. E6 bu yuvayi "
        "G paragrafinin sayisal ayrintisina capalamali (dinlendiricilik "
        "puanlarinin yaklasik yariya dusmesi) ya da H paragrafindaki karin "
        "canlilik uzerindeki etkisi savina tasimali."
    ),
}

# ---------------------------------------------------------------------------
# 4) Dokunulmayan sorular - gerekce review_note alanina yaziliyor
# ---------------------------------------------------------------------------

DOKUNULMADI = {
    (AC1_TF, 11): (
        "E5 / 6. calistirma: dokunulmadi. E1 bu soruyu 'belirsiz' mekanizmayla "
        "isaretlemis ve blind_basis alanina 'guess' yazmisti; olcumde model "
        "dogru cevabi bir mekanizmayla degil, uc secenekli bir kumede sansla "
        "tutturmus. Ifade E/4'un icerigini duz bicimde paraphrase ediyor, "
        "kanit cumlesi disinda hicbir imza tasimiyor. Yine de AC1-10 ile ayni "
        "ekseni (etkileyici yetenek iddiasi -> TRUE) paylastigi icin E7 "
        "olcumunde tekrarli olarak yeniden olculmesi gerekiyor; AC1-10 bu "
        "calistirmada elendigi icin eksen zaten zayifladi."
    ),
    (AC3_MI, 29): (
        "E5 / 6. calistirma: dokunulmadi. E1 mekanizmayi 'belirsiz' bulmus ve "
        "blind_basis alanina 'guess' yazmisti. Soru kokunun istedigi olcum "
        "(sinir liflerinin kalinligi) pasajda yalniz E paragrafinda var, "
        "dolayisiyla cevap paragraf okunarak bulunuyor; sekiz paragrafli bir "
        "kumede dogru harfin bir kez tutturulmasi bir imza degil. Duzeltme "
        "yapilmadi, E7 tekrarli olarak yeniden olcmeli."
    ),
    (P_SUM, 5): (
        "E5 / 6. calistirma: dokunulmadi. E1'in kendi gerekcesi sizintiyi degil "
        "sizintinin YOKLUGUNU anlatiyor: 'green and ___' cercevesine 'lush', "
        "'dense', 'mature' gibi bircok aday uyuyor, yani bosluk zaten cok "
        "adayli. blind_basis 'guess'; olcumde dogru sozcuk sansla tutmus. "
        "Cerceveyi daha da gevsetmek boslugu yanitlanamaz hale getirirdi, o "
        "yuzden soru oldugu gibi birakildi; E7 tekrarli olarak yeniden "
        "olcmeli."
    ),
    (P_SUM, 7): (
        "E5 / 6. calistirma: dokunulmadi. E1'in gerekcesi boslugun birden cok "
        "zarfa acik oldugunu ('sharply', 'significantly', 'rapidly') soyluyor, "
        "yani cerceve zaten kilitli degil; blind_basis 'guess'. Bu tur "
        "boslugun tek gercek kusuru olcum zorlugu, sizinti degil; duzeltme "
        "yapilmadi. E6 bu yuvayi yeniden uretirse zarf yerine sayi ya da "
        "olcek adi isteyen bir bosluk daha dayanikli olur."
    ),
    (P_SUM, 13): (
        "E5 / 6. calistirma: dokunulmadi. E1'in gerekcesi 'bes, yedi, on "
        "noktali olcekler esit derecede olasi' diyor, yani bosluk kapali bir "
        "listeden sayi istiyor ve cerceve tek adaya kilitlenmiyor; blind_basis "
        "'guess'. Kapali liste isteyen bosluklar E10'un toplu raporunda da "
        "dayanikli sayiliyor. Duzeltme yapilmadi, E7 yeniden olcmeli."
    ),
    (AC2_FC, 5): (
        "E5 / 6. calistirma: dokunulmadi. E1'in gerekcesi boslugun istedigi "
        "sira numarasinin 'parcaya bakmadan tahmin edilemeyecek kadar spesifik' "
        "oldugunu soyluyor - yani gerekce sizintiyi degil sizintinin yoklugunu "
        "anlatiyor; blind_basis 'guess'. 4. calistirma ayni akis semasinin 1. "
        "kutusundaki hesaplanabilir bosluk sorununu zaten kapatmisti. Duzeltme "
        "yapilmadi, E7 yeniden olcmeli."
    ),
    (AC3_TC, 1): (
        "E5 / 6. calistirma: dokunulmadi. E1'in gerekcesi 'plastic', 'glass', "
        "'plexiglass' gibi alternatiflerin ayni cerceveye uydugunu soyluyor, "
        "yani bosluk tek adaya kilitli degil; blind_basis 'guess'. Malzeme adi "
        "isteyen bu bosluk ancak B/3 okunarak dogru yazilabiliyor. Duzeltme "
        "yapilmadi, E7 yeniden olcmeli."
    ),
    (AC4_NC, 5): (
        "E5 / 6. calistirma: dokunulmadi, ama mekanizma etiketi tartismali. "
        "E1 'belirsiz' demis ve blind_basis alanina 'guess' yazmis; oysa "
        "'merely a ___ effect' cercevesi 4. calistirmanin tanimladigi ESDIZIM "
        "KILIDI bicimine yakin duruyor ('novelty effect' yerlesik bir esdizim). "
        "Kilidi acmanin tek yolu boslugu baska bir ayrintiya tasimak, o da "
        "answer'i degistirmek demek - yani bu bir duzeltme degil eleme "
        "olurdu. Yuvayi elemek yerine kayda gecirmeyi sectim: AC4 dosyasinda "
        "bu calistirmadan once zaten iki elenen yuva var (36 ve 38, 5. "
        "calistirma) ve ucuncu bir yuva ayni pasaji yeniden uretime iyice "
        "bagimli kilardi. E6 isterse bu yuvayi da kapsama alabilir; onerilen "
        "yeni capa F paragrafindaki %4'luk masa doluluk artisi."
    ),
}


# ---------------------------------------------------------------------------

def baslik_uygula(veri, yol):
    n = 0
    for grup_id, harfler in BASLIK.get(yol, {}).items():
        kaplar = []
        for g in (veri.get("groups") or [veri]):
            if grup_id is None or g.get("group_id") == grup_id:
                kaplar.append(g)
        if not kaplar:
            raise SystemExit("baslik grubu bulunamadi: %s %s" % (yol, grup_id))
        for kap in kaplar:
            ol = kap.get("option_list") or veri.get("option_list")
            if not ol:
                raise SystemExit("option_list yok: %s" % yol)
            for o in ol.get("options") or []:
                eski_yeni = harfler.get(o.get("key"))
                if not eski_yeni:
                    continue
                eski, yeni = eski_yeni
                if o["text"] == yeni:
                    continue
                if o["text"] != eski:
                    raise SystemExit("baslik metni beklenenden farkli: %s %s"
                                     % (yol, o.get("key")))
                o["text"] = yeni
                n += 1
    return n


def main():
    d_say = e_say = k_say = b_say = 0

    for yol in DOSYALAR:
        veri = ortak.oku(yol)
        b_say += baslik_uygula(veri, yol)

        for it in ortak.sorular(veri):
            anahtar = (yol, it["number"])

            if anahtar in DUZELTME:
                y = DUZELTME[anahtar]
                onceki = (it.get("revision") or {}).get("onceki_prompt") \
                    or it["prompt"]
                if "prompt" in y:
                    it["prompt"] = y["prompt"]
                for alan in ("explanation", "contradiction_point",
                             "not_given_justification", "scan_note"):
                    if alan in y:
                        it[alan] = y[alan]
                it["status"] = "verified"
                it["blind_solvable"] = None
                it["revision"] = {
                    "tarih": TARIH,
                    "mekanizma": y["mekanizma"],
                    "onceki_prompt": onceki,
                    "ne_degisti": y["ne_degisti"],
                }
                d_say += 1

            elif anahtar in ELEME:
                it["status"] = "rejected"
                it["reject_reason"] = ELEME[anahtar]
                e_say += 1

            elif anahtar in DOKUNULMADI:
                it["review_note"] = DOKUNULMADI[anahtar]
                k_say += 1

        ortak.yaz(yol, veri)

    print("duzeltildi %d - elendi %d - dokunulmadi %d" % (d_say, e_say, k_say))
    print("yeniden yazilan baslik: %d" % b_say)
    bekleniyor = (len(DUZELTME), len(ELEME), len(DOKUNULMADI))
    if (d_say, e_say, k_say) != bekleniyor:
        raise SystemExit("BEKLENEN SAYI TUTMADI: %s" % (bekleniyor,))


if __name__ == "__main__":
    main()
