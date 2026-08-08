# -*- coding: utf-8 -*-
"""OPUS5-E6 3. calistirma: coktan secmeli - tam testler.

E5'in eledigi dokuz yuvayi (AC1 32 / 34-35, AC3 32 / 34-35, AC4 33 / 34-35,
GT1 22 / 23-24, GT2 23-24) ayni dosyaya ayni numarayla yeniden doldurur.
Soru sayisi degismez, hicbir soru silinmez, select_count korunur.

Kullanim: python tools/_e6_mc_testler.py
"""
import collections
import io
import json
import os
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Alan sirasi mevcut yuvalarla ayni kalsin.
SIRA = ["number", "select_count", "prompt", "options", "answer", "evidence",
        "evidence_locator", "distractor_analysis", "explanation", "difficulty",
        "status", "blind_solvable", "blind_basis", "generated_by", "yeniden_uretim"]


def sec(*ciftler):
    return [{"letter": h, "text": t} for h, t in ciftler]


YENI = {
    "content/reading/tests/AC1/multiple-choice.json": {
        32: {
            "select_count": 1,
            "prompt": "Which of these statements about the island of Maug is correct?",
            "options": sec(
                ("A", "Scientists are stationed on the island all year round"),
                ("B", "Its coral reef is mainly found in deep water offshore"),
                ("C", "The island is a single peak rising from the seabed"),
                ("D", "It lies roughly 450 miles to the north of Guam"),
            ),
            "answer": ["D"],
            "evidence": ("Maug is an uninhabited volcanic island in the Commonwealth of the "
                         "Northern Mariana Islands, roughly 450 miles north of Guam in the "
                         "western Pacific."),
            "evidence_locator": {"paragraph": "A", "sentence": 1},
            "distractor_analysis": {
                "A": ("Cazip ama yok -- A/1 adayi 'uninhabited' (insansiz) diye tanitiyor; "
                      "arastirmacilar disaridan gelip olcum yapiyor, adada yil boyu kalan "
                      "kimseden soz edilmiyor."),
                "B": ("Yer degistirme -- resif A/2'de adanin cevresindeki SIG sulara "
                      "yerlestiriliyor ve gaz cikisi kalderanin ic kiyisinda; secenek hem "
                      "derinligi hem yonu tersine ceviriyor."),
                "C": ("Kapsam kaydirma -- B/2 Maug'u cokmus bir yanardagdan geriye kalan, "
                      "kabaca daire bicimindeki uc kucuk ada olarak anlatiyor; tek zirve "
                      "degil."),
            },
            "explanation": ("Paragraph A places Maug in the Commonwealth of the Northern "
                            "Mariana Islands, roughly 450 miles north of Guam in the western "
                            "Pacific."),
            "difficulty": "easy",
            "ne_degisti": (
                "Yuva bosaltilip ayni pasajdan yeni bir soruyla dolduruldu. Eski soru B/3'e "
                "dayaniyordu: yazarin jeolojiyi neden anlattigi. Volkanik adalarda magmanin "
                "deniz tabani bacalarindan gaz salmasi ders kitabi duzeyinde bir olgu oldugu "
                "icin 'suyun kimyasini aciklamak icin' cevabi pasajsiz da cikiyordu. Yeni soru "
                "B paragrafina hic degmiyor: kanit A/1'e, adanin konumuna tasindi. Guam'in "
                "kac mil kuzeyinde oldugu keyfi bir olcu; disaridan bilinemez, cunku 200 ya da "
                "700 mil de esit olculude makuldu. Uc celdirici de pasajin kendi ayrintilarini "
                "tersine ceviriyor (insansizlik, sig su, uc adaci), yani 'akla yatkin olani "
                "sec' stratejisi calismiyor. Kip dengesi icin dogru secenek olculu ('roughly'), "
                "iki celdirici mutlak ('all year round', 'a single peak') yazildi."),
        },
        "34-35": {
            "select_count": 2,
            "prompt": "Which TWO things does the writer say the research team did at Maug?",
            "options": sec(
                ("A", "Left instruments running the whole time to record how the water moved"),
                ("B", "Filmed the reef from cameras fixed to the seabed"),
                ("C", "Counted the fish likely to be sheltering in the reef"),
                ("D", "Compared Maug with reefs elsewhere in the Pacific"),
                ("E", "Gathered bubbles rising from the seabed vents to study on land"),
                ("F", "Cleared weedy algae from part of the seafloor"),
                ("G", "Measured the rate at which the vents usually release gas"),
            ),
            "answer": ["A", "E"],
            "evidence": ("The team deployed instruments to continuously record temperature, "
                         "light, the partial pressure of carbon dioxide, seawater pH and water "
                         "currents, while divers collected coral cores, applied dye to mark new "
                         "growth, and used funnels to capture bubbles of gas escaping from the "
                         "vents for laboratory analysis."),
            "evidence_locator": {"paragraph": "D", "sentence": 2},
            "distractor_analysis": {
                "B": ("Cazip ama yok -- surekli kayit alan cihazlar var, ama kaydettikleri "
                      "sicaklik, isik, karbondioksit basinci, pH ve akinti; deniz tabanina "
                      "sabitlenmis kameradan hic soz edilmiyor."),
                "C": ("Yakin ama eksik -- resif iskeletinin cok sayida baska deniz turune "
                      "barinak sagladigi G/3'te geciyor, ama bu turlerin sayildigi soylenmiyor."),
                "D": ("Yer degistirme -- H/1 Maug'daki degisimleri dunya genelindeki resiflerin "
                      "yuzyil sonunda yasayacagi seyle karsilastiriyor; bu bir projeksiyon, "
                      "ekibin baska Pasifik resiflerinde olcum yaptigi anlamina gelmiyor."),
                "F": ("Yer degistirme -- otsu alglerin bacalarin cevresinde deniz tabanina "
                      "egemen olmasi bir BULGU (F/2); ekibin onlari temizledigi degil, "
                      "gozledigi anlatiliyor."),
                "G": ("Yakin ama eksik -- bacalardan kacan kabarciklar hunilerle toplaniyor, "
                      "ama salim hizinin olculdugune dair tek bir ifade yok."),
            },
            "explanation": ("Paragraph D says the team deployed instruments to record water "
                            "currents, among other things, continuously, and that divers used "
                            "funnels to capture bubbles of gas escaping from the vents for "
                            "laboratory analysis."),
            "difficulty": "medium",
            "ne_degisti": (
                "Yuva bosaltilip ayni pasajdan yeni bir soruyla dolduruldu. Eski soru F/1 ve "
                "G/1'e dayaniyordu: calismalarin biri deniz tabani toplulugunu, digeri iskelet "
                "ic yapisini incelemesi. Asitlenme arastirmalarinin bu iki eksene ayrilmasi "
                "bilim haberciliginin yerlesik kalibi oldugu icin C+F ikilisi pasajsiz "
                "seciliyordu. Yeni soru F ve G paragraflarina hic degmiyor: kanit D/2'ye, "
                "sahada yapilan islere tasindi. Hangi buyuklugun surekli kaydedildigi ve "
                "kacan gazin ne yapildigi sahaya ozgu yontem kararlari; kamera, alg temizligi "
                "ya da baska resiflerle karsilastirma da esit olculude makul oldugu icin "
                "disaridan secilemez. Konumsal duzen icin dogru harfler A ve E: bu tipteki "
                "ayakta kalan uc yuvanin ucu de C+F oldugu icin (E5 2. calistirma olcumu) "
                "A harfi bilerek dogru yapildi ve C+F ikilisi kullanilmadi."),
        },
    },

    "content/reading/tests/AC3/multiple-choice.json": {
        32: {
            "select_count": 1,
            "prompt": "What does the writer suggest about the excavation of the Collegium Augustalium?",
            "options": sec(
                ("A", "Digging there began only after the glassy material was noticed"),
                ("B", "More than one body was recovered from the building"),
                ("C", "The building had probably been in use as a private home"),
                ("D", "The remains found there were excavated fairly recently"),
            ),
            "answer": ["B"],
            "evidence": ("Among the victims uncovered during excavations of the Collegium "
                         "Augustalium, a public building in the town centre, was a young man of "
                         "around 20 years old, found lying face down on a wooden bed where he "
                         "had apparently been sleeping when the flows arrived."),
            "evidence_locator": {"paragraph": "B", "sentence": 1},
            "distractor_analysis": {
                "A": ("Ters sira -- B/2 kalintilarin arkeologlarca 1960'lardan beri bilindigini, "
                      "camsi maddenin ise cok daha sonraki bir incelemede fark edildigini "
                      "soyluyor; secenek iki olayin sirasini tersine ceviriyor."),
                "C": ("Yer degistirme -- Collegium Augustalium B/1'de kent merkezinde bir KAMU "
                      "binasi olarak tanitiliyor; ozel konut oldugu hicbir yerde soylenmiyor."),
                "D": ("Kapsam kaydirma -- yakin tarihli olan sey kazi degil inceleme; kalintilar "
                      "B/2'ye gore altmis yildir biliniyor."),
            },
            "explanation": ("Paragraph B introduces the young man as one 'among the victims "
                            "uncovered during excavations' of the Collegium Augustalium, which "
                            "implies that other bodies were found there as well."),
            "difficulty": "medium",
            "ne_degisti": (
                "Yuva bosaltilip ayni pasajdan yeni bir soruyla dolduruldu. Eski soru A/3'e "
                "dayaniyordu: ahsap kirislerin, yiyecegin ve kumasin neden anildigi. "
                "Herculaneum'un organik malzemeyi olaganustu iyi korumasi arkeolojinin en cok "
                "anlatilan olgularindan biri oldugu icin 'kirilgan seyler alisilmadik bicimde "
                "dayandi' cevabi pasajsiz da cikiyordu. Yeni soru A paragrafina hic degmiyor: "
                "kanit B/1'e tasindi ve cevap tek bir sozcugun tasidigi cikarima baglandi "
                "('Among the victims uncovered' -> binada baska kurbanlar da vardi). Bu, vaka "
                "hakkinda okunmus her seyin disinda kalan bir metin ayrintisi; en cok "
                "anlatilan ayrintilar (yatak, uyku, yas) bilerek soru ekseni yapilmadi. Uc "
                "celdirici de metnin verdigi sirayi ya da tanimi tersine ceviriyor. Kip "
                "dengesi icin iki celdirici olculu yazildi ('probably', 'fairly recently')."),
        },
        "34-35": {
            "select_count": 2,
            "prompt": "Which TWO findings about the structures inside the tissue does the writer report?",
            "options": sec(
                ("A", "Individual cell bodies were all much the same width"),
                ("B", "Cell bodies ranged from under 3 to over 14 micrometres across"),
                ("C", "The axons were probably wider than those of a living brain"),
                ("D", "The sheaths had lost the layered form they once had"),
                ("E", "Axons from the spinal cord were usually thicker than those in the brain"),
                ("F", "The sheaths kept exactly the repeating pattern of ordinary nerve tissue"),
                ("G", "The measurements were probably only approximate"),
            ),
            "answer": ["B", "F"],
            "evidence": ("Individual cell bodies ranged from 2.7 to 14.2 micrometres across, and "
                         "the myelin sheaths retained their characteristic multilayered "
                         "structure, complete with the regular repeating pattern seen under a "
                         "microscope in ordinary, unfossilised nervous tissue."),
            "evidence_locator": {"paragraph": "E", "sentence": 3},
            "distractor_analysis": {
                "A": ("Kapsam kaydirma -- E/3 hucre govdelerini 2,7 ile 14,2 mikrometre arasinda "
                      "veriyor; bes kattan fazla fark eden bir araligi 'hemen hemen ayni' diye "
                      "ozetlemek olcuyu siliyor."),
                "C": ("Yer degistirme -- E/2 camlasmis dokudaki aksonlarin ortalama 717,7 "
                      "nanometre oldugunu ve bunun canli beyindeki ak madde araligina YAKIN "
                      "dustugunu soyluyor; daha genis olduklari soylenmiyor."),
                "D": ("Ters yon -- ayni cumle miyelin kiliflarinin cok katmanli yapiyi "
                      "KORUDUGUNU soyluyor."),
                "E": ("Sayi kaydirma -- omurilikten gelen aksonlar yaklasik 672, beyindekiler "
                      "717,7 nanometre; siralama secenektekinin tersi."),
                "G": ("Ters yon -- E/1 yapisal olcumlerin 'remarkably precise' (dikkate deger "
                      "olcude kesin) oldugunu soyluyor."),
            },
            "explanation": ("Paragraph E reports that individual cell bodies ranged from 2.7 to "
                            "14.2 micrometres across, and that the myelin sheaths kept the "
                            "regular repeating pattern seen in ordinary, unfossilised nervous "
                            "tissue."),
            "difficulty": "hard",
            "ne_degisti": (
                "Yuva bosaltilip ayni pasajdan yeni bir soruyla dolduruldu. Eski soru F/2 ve "
                "G/1'e dayaniyordu: karbon-oksijen agirligi ve noronlar arasi iletisim proteini. "
                "Organik dokunun karbon temelli olmasi da beyin dokusunda sinyal proteini "
                "bulunmasi da beklenen bulgular oldugu icin B+F ikilisi pasajsiz seciliyordu. "
                "Yeni soru F ve G paragraflarina hic degmiyor: kanit E/3'e, olculen "
                "buyukluklere tasindi. Hucre govdesi araliginin genis mi dar mi oldugu ve "
                "kiliflarin desenini koruyup korumadigi ancak olcum sonucundan bilinir; "
                "celdiriciler de ayni paragrafin gercek sayilarini ters cevirerek kuruldu "
                "(omurilik/beyin siralamasi, akson genisligi, olcum kesinligi), yani alan "
                "bilgisi hicbir secenegi elemiyor. Konumsal duzen icin harf cifti B+F secildi; "
                "C+F ikilisi bu calistirmada hicbir yuvada kullanilmadi."),
        },
    },

    "content/reading/tests/AC4/multiple-choice.json": {
        33: {
            "select_count": 1,
            "prompt": "What does the writer say about the first experiment?",
            "options": sec(
                ("A", "Its volunteers were chosen because they usually napped in the day"),
                ("B", "Its volunteers were on average older than those in the second study"),
                ("C", "It included more men than women"),
                ("D", "Sixty people took part in it altogether"),
            ),
            "answer": ["D"],
            "evidence": ("In the first experiment, 60 young adults, with an average age of 21.9 "
                         "and a standard deviation of 4.2 years, 17 of them male, were divided "
                         "into the two groups."),
            "evidence_locator": {"paragraph": "C", "sentence": 1},
            "distractor_analysis": {
                "A": ("Yer degistirme -- haftada en az bir kez sekerleme yapma sarti IKINCI "
                      "deneyin katilimcilarina ait (D/1); birinci deneyde boyle bir olcut "
                      "verilmiyor."),
                "B": ("Cazip ama yok -- iki deneyin de ortalama yasi 21,9; fark yalniz standart "
                      "sapmada (4,2'ye karsi 2,8), yas ortalamasinda degil."),
                "C": ("Ters oran -- altmis katilimcinin 17'si erkek, yani erkekler acik bir "
                      "azinlik."),
            },
            "explanation": ("Paragraph C says that 60 young adults took part in the first "
                            "experiment and were divided into the two groups."),
            "difficulty": "easy",
            "ne_degisti": (
                "Yuva bosaltilip ayni pasajdan yeni bir soruyla dolduruldu. Eski soru C/2-C/3'e "
                "dayaniyordu: iki grubun ogrenme ile sinav arasinda esit sure beklemesi. Uyku "
                "ile uyanikligi karsilastiran adil bir kiyaslamada surenin esitlenmesi yontem "
                "mantiginin kendisinden cikan bir kural oldugu icin cevap pasajsiz "
                "veriliyordu. Yeni soru o iki cumleye hic degmiyor: kanit C/1'e, orneklemin "
                "kendisine tasindi. Kac kisinin katildigi tamamen keyfi bir tasarim ayrintisi. "
                "Celdiriciler ayni sayfadaki gercek sayilarla kuruldu (yas ortalamalarinin "
                "esitligi, erkek katilimci orani) ve biri ikinci deneyin olcutunu birinciye "
                "tasiyor; hicbiri alan bilgisiyle elenemiyor. Kip dengesi icin dogru secenek "
                "mutlak ('altogether'), bir celdirici olculu ('usually') yazildi."),
        },
        "34-35": {
            "select_count": 2,
            "prompt": "Which TWO things does the writer say about the people in the second experiment?",
            "options": sec(
                ("A", "Every one of them was already in the habit of napping"),
                ("B", "They were all tested on the same afternoon"),
                ("C", "They were on average several years older than the first group"),
                ("D", "About a third of them were male"),
                ("E", "They had taken part in the first experiment as well"),
                ("F", "There were more of them than in the first experiment"),
                ("G", "Most of them usually slept badly at night"),
            ),
            "answer": ["A", "D"],
            "evidence": ("The second experiment recruited 34 participants who napped at least "
                         "once a week, with an average age of 21.9 and a standard deviation of "
                         "2.8 years, 11 of them male."),
            "evidence_locator": {"paragraph": "D", "sentence": 1},
            "distractor_analysis": {
                "B": ("Cazip ama yok -- ogrenmenin ogleden sonra bir bucukta yapildigi soyleniyor "
                      "(D/2), ama herkesin ayni ogleden sonra sinandigi soylenmiyor; tasarim "
                      "geregi ayni kisiler iki kosulu FARKLI gunlerde yasiyor (B/2)."),
                "C": ("Cazip ama yok -- iki grubun ortalama yasi da 21,9; degisen yalniz standart "
                      "sapma."),
                "E": ("Yer degistirme -- ayni kisilerin iki kosuldan da gecmesi ikinci deneyin "
                      "IC tasarimi (B/2); birinci deneyin katilimcilariyla ayni olduklari "
                      "soylenmiyor."),
                "F": ("Ters oran -- ikinci deneyde 34, birincide 60 kisi var."),
                "G": ("Cazip ama yok -- katilimcilarin gece uykusunun kotu oldugu hic "
                      "soylenmiyor; tek olcut haftada en az bir kez sekerleme yapmak."),
            },
            "explanation": ("Paragraph D says the second experiment recruited 34 people who "
                            "napped at least once a week, 11 of them male."),
            "difficulty": "medium",
            "ne_degisti": (
                "Yuva bosaltilip ayni pasajdan yeni bir soruyla dolduruldu. Eski soru D/2 ve "
                "F/1'e dayaniyordu: sekerlemelerde beyin etkinliginin polisomnografiyle "
                "kaydedilmesi ve agirlikla hafif 2. evre uykudan olusmasi. Ikisi de uyku "
                "arastirmalarinin standart bilgisi oldugu icin C+E ikilisi pasajsiz "
                "seciliyordu. Yeni soru o iki cumleye hic degmiyor: kanit D/1'e, ikinci deneyin "
                "orneklemine tasindi. Katilimcilarin sekerleme aliskanligi olan kisiler "
                "arasindan secilmesi ve erkek orani keyfi tasarim ayrintilari; ustelik "
                "celdiriciler ayni sayfanin gercek sayilarini ters cevirdigi icin 'akla yatkin "
                "olani sec' stratejisi yanlis harfe goturuyor (F: daha kalabalik ornek). "
                "Konumsal duzen icin harf cifti A+D; E5'in istedigi gibi A harfi dogru "
                "cevaplarin arasina alindi. Kip dengesi icin dogru seceneklerden biri mutlak "
                "('Every one of them'), digeri olculu ('About a third') yazildi."),
        },
    },

    "content/reading/tests/GT1/multiple-choice.json": {
        22: {
            "select_count": 1,
            "prompt": "When is lateness recorded as a formal attendance concern?",
            "options": sec(
                ("A", "After a single delay of about half an hour"),
                ("B", "After being more than ten minutes late three times in a rolling month"),
                ("C", "After ten minutes' lateness on two shifts in the same week"),
                ("D", "After any lateness that leaves a production line unattended"),
            ),
            "answer": ["B"],
            "evidence": ("Persistent lateness of more than ten minutes on three occasions within "
                         "a rolling month will be recorded as a formal attendance concern."),
            "evidence_locator": {"text": "A", "paragraph": "C", "sentence": 3},
            "distractor_analysis": {
                "A": ("Cazip ama yok -- tek seferlik uzun bir gecikme icin ayri bir kural "
                      "verilmiyor; olcut gecikmenin uzunlugu degil tekrar sayisi."),
                "C": ("Sayi kaydirma -- esik bir hafta icinde iki degil, bir aylik donem icinde "
                      "UC kez on dakikadan fazla gecikme."),
                "D": ("Yer degistirme -- uretim hattinin bos kalmamasi molalarin donusumlu "
                      "kullanilmasiyla ilgili bir kural (B/2); devamsizlik kaydinin olcutu "
                      "degil."),
            },
            "explanation": ("Paragraph C of Text A says that lateness of more than ten minutes "
                            "on three occasions within a rolling month will be recorded as a "
                            "formal attendance concern."),
            "difficulty": "medium",
            "ne_degisti": (
                "Yuva bosaltilip ayni metinden yeni bir soruyla dolduruldu. Eski soru D/2'ye "
                "dayaniyordu: iki vardiya arasinda on bir saat dinlenme birakmayan takasin "
                "reddedilmesi. On bir saatlik dinlenme araligi calisma mevzuatinin yaygin "
                "bilinen bir maddesi oldugu icin cevap metne bakilmadan veriliyordu. Yeni soru "
                "D paragrafina hic degmiyor: kanit C/3'e tasindi ve cevap tek bir sayida degil, "
                "UC sayinin birlikte tuttugu bir esikte (on dakika + uc kez + bir aylik "
                "donem). Celdiriciler de ayni bicimde sayili yazildi, boylece 'somut olani sec' "
                "sezgisi ayirt edici olmaktan cikti; hicbir is yeri bu ucluyu disaridan "
                "bilinebilecek bir standart olarak tasimiyor. Kip dengesi icin bir celdirici "
                "olculu ('about half an hour'), bir digeri mutlak ('any lateness') yazildi."),
        },
        "23-24": {
            "select_count": 2,
            "prompt": "Which TWO statements about annual leave are correct?",
            "options": sec(
                ("A", "Part-time staff receive the same 28 days as full-time staff"),
                ("B", "Unused leave is always lost at the end of December"),
                ("C", "Up to five unused days may be carried into the next leave year"),
                ("D", "Public holidays are counted separately from the 28-day entitlement"),
                ("E", "Leave requests usually need at least four weeks' notice"),
                ("F", "A manager may refuse a request without giving a reason"),
                ("G", "The leave year always begins on the first day of April"),
            ),
            "answer": ["C", "G"],
            "evidence": ("Leave entitlement is calculated on a pro-rata basis for part-time staff "
                         "and for anyone joining partway through the leave year, which runs from "
                         "1 April to 31 March. Up to five days of unused annual leave may be "
                         "carried forward into the following leave year with written approval "
                         "from a manager, but any leave not taken or approved for carry-over by "
                         "31 March is forfeited."),
            "evidence_locator": {"text": "B", "paragraph": "A", "sentence": 2},
            "distractor_analysis": {
                "A": ("Ters yon -- A/2 yarim zamanli calisanlarin hakkinin orantili (pro-rata) "
                      "hesaplandigini soyluyor; 28 gun tam zamanlilar icin."),
                "B": ("Yer degistirme -- aralik ayinin son iki haftasi yalniz onay makamini "
                      "degistiriyor (B/5); kullanilmayan izin 31 Mart'ta yaniyor."),
                "D": ("Ters yon -- A/1 28 gunun resmi tatilleri de KAPSADIGINI acikca "
                      "soyluyor."),
                "E": ("Kapsam kaydirma -- dort haftalik bildirim yalniz bes gunden uzun "
                      "kesintisiz izinler icin; olagan istek iki hafta once veriliyor (B/2, "
                      "B/3)."),
                "F": ("Cazip ama yok -- yoneticinin gerekcesiz ret yetkisinden hic soz "
                      "edilmiyor; metin yalniz kimin onaylayacagini ve hangi bildirim "
                      "surelerinin gerektigini duzenliyor."),
            },
            "explanation": ("Paragraph A of Text B says the leave year runs from 1 April to 31 "
                            "March, and paragraph D says up to five days of unused leave may be "
                            "carried forward into the following year with written approval."),
            "difficulty": "hard",
            "ne_degisti": (
                "Yuva bosaltilip ayni metinden yeni bir soruyla dolduruldu. Eski soru C/2 ve "
                "C/3'e dayaniyordu: fazla mesainin onceden onaylanmasi ve fazlaliginin izne "
                "cevrilebilmesi. Ikisi de sayisiz is yerinde ayni bicimde gecen standart "
                "maddeler oldugu icin B+E ikilisi metne bakilmadan seciliyordu. Yeni soru C "
                "paragrafina hic degmiyor: kanit A/2 ile D/1'e tasindi. Asil savunma harf "
                "seciminde degil kurgudadir - is hayatinda EN yaygin uc madde (resmi tatillerin "
                "izinden ayri sayilmasi, dort haftalik bildirim, yoneticinin gerekcesiz reddi) "
                "bilerek CELDIRICI yapildi, dogru iki secenek ise yalniz bu sirkete ozgu iki "
                "keyfi sayiya baglandi (bes gun devir, 1 Nisan). Boylece 'standart politikayi "
                "sec' stratejisi sistematik olarak yanlis harfe goturuyor. Konumsal duzen icin "
                "harf cifti C+G; E5'in istedigi gibi G harfi dogru cevaplarin arasina alindi."),
        },
    },

    "content/reading/tests/GT2/multiple-choice.json": {
        "23-24": {
            "select_count": 2,
            "prompt": "Which TWO statements about the remote working policy are correct?",
            "options": sec(
                ("A", "Staff may work remotely as soon as they join the company"),
                ("B", "Remote working arrangements are all reviewed every six months"),
                ("C", "The company pays for the internet connection used at home"),
                ("D", "Employees may work from abroad if their manager agrees"),
                ("E", "Home-office claims usually go through the line manager"),
                ("F", "Everyone must spend at least one day a week in the office"),
                ("G", "Any change to someone's remote days needs a week's notice"),
            ),
            "answer": ["B", "G"],
            "evidence": ("Remote working arrangements are reviewed every six months and may be "
                         "withdrawn if performance or availability standards are not met. "
                         "Requests to change remote working days must be submitted at least one "
                         "week in advance."),
            "evidence_locator": {"text": "B", "paragraph": "C", "sentence": 2},
            "distractor_analysis": {
                "A": ("Kapsam kaydirma -- uzaktan calisma basvurusu deneme suresini tamamlamis "
                      "calisanlara acik (A/1); ise baslar baslamaz degil."),
                "C": ("Ters yon -- en az 10 Mbps'lik baglantiyi calisanin kendisi saglamak "
                      "zorunda (B/2); sirketin verdigi sey dizustu bilgisayar."),
                "D": ("Kapsam kaydirma -- yurt disindan calismak icin hem IK'dan hem ilgili "
                      "ulke ofisinden ayri yazili onay gerekiyor (D/2); amir onayi tek basina "
                      "yetmiyor."),
                "E": ("Yer degistirme -- onayli ev ofisi ekipmani icin geri odeme masraf "
                      "sistemi uzerinden isteniyor (B/5), amir uzerinden degil."),
                "F": ("Cazip ama yok -- haftada bir gun ofiste bulunma zorunlulugu metinde yok; "
                      "yalniz musteriyle calisan rollerin daha sik cagrilabilecegi soyleniyor "
                      "(A/2)."),
            },
            "explanation": ("Paragraph C of Text B says remote working arrangements are reviewed "
                            "every six months, and that requests to change remote working days "
                            "must be submitted at least one week in advance."),
            "difficulty": "hard",
            "ne_degisti": (
                "Yuva bosaltilip ayni metinden yeni bir soruyla dolduruldu. Eski soru B "
                "paragrafinin ucuncu maddesi ile D/1'e dayaniyordu: cekirdek saatlerde "
                "ulasilabilir olmak ve kalici konum degisikligini IK'ya bildirmek. Uzaktan "
                "calisma politikalarinin neredeyse hepsinde bulunan iki madde oldugu icin B+D "
                "ikilisi metne bakilmadan seciliyordu. Yeni soru o iki cumleye hic degmiyor: "
                "kanit C/2 ve C/3'e tasindi. Kurgu GT1'deki ile ayni: en tanidik uc madde "
                "(deneme suresi olmadan uzaktan calisma, internetin sirketce odenmesi, amir "
                "onayiyla yurt disi) celdirici yapildi; dogru iki secenek sirkete ozgu iki "
                "keyfi sureye baglandi (alti aylik gozden gecirme, bir haftalik bildirim). "
                "Konumsal duzen icin harf cifti B+G; boylece bu calistirmadaki bes iki-harfli "
                "yuvada A, B, C, D, E, F, G harflerinin hepsi en az bir kez dogru oluyor ve "
                "hicbir cift tekrarlanmiyor."),
        },
    },
}


def main():
    toplam = 0
    for rel, yuvalar in YENI.items():
        yol = os.path.join(KOK, rel.replace("/", os.sep))
        d = json.load(open(yol, encoding="utf-8"))
        for i, it in enumerate(d["items"]):
            no = it.get("number")
            if no not in yuvalar:
                continue
            yeni = dict(yuvalar[no])
            if it.get("select_count") != yeni["select_count"]:
                raise SystemExit("%s #%s: select_count degisiyor" % (rel, no))
            if len(it["options"]) != len(yeni["options"]):
                raise SystemExit("%s #%s: secenek sayisi degisiyor" % (rel, no))
            eski = {
                "tarih": "2026-08-08",
                "kaynak_prompt": "prompts/OPUS5-E6-yeniden-uretim.md (3/7)",
                "uretilen_grup": "Coktan secmeli - tam testler",
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
            toplam += 1
            print("yazildi: %-46s #%-6s -> %s" % (rel.split("/")[-2], no, yeni["answer"]))
        with open(yol, "w", encoding="utf-8", newline="\n") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print("  %s: %d soru" % (rel, len(d["items"])))
    print("yeniden doldurulan yuva:", toplam)


if __name__ == "__main__":
    main()
