# -*- coding: utf-8 -*-
"""E5 / 2. calistirma -- coktan secmeli sorularin elden gecirilmesi.

Kapsam: content/reading altindaki butun `question_type: multiple_choice`
dosyalarindaki `status: "flagged"` sorular (30 yuva).

Mekanizmalar:
  kip_imzasi      (4 yuva)  -> dogru secenegin olculu, celdiricinin mutlak
                              yazilmis olmasi. Duzeltme: kip iki yone birden
                              dagitilir (olculu celdirici + kesin dogru secenek).
  konumsal_duzen (12 yuva)  -> celdiricilerin soru kokunun cercevesi disinda
                              kalmasi ya da uydurma olmasi; parcaya bakmadan
                              elenebiliyorlar. Duzeltme: her celdirici pasajin
                              gercek bir ayrintisina capalanir ve soru kokunun
                              istedigi cerceveye tasinir.
  genel_kultur   (14 yuva)  -> sorunun ekseninin kendisi dunya bilgisi;
                              mekanik duzeltmeye uygun degil, elenir.

Korunan alanlar: answer, evidence, evidence_locator, number, select_count.
"""
import io
import json
import os

TARIH = "2026-08-08"

P = "content/reading/practice/multiple-choice.json"
A1 = "content/reading/tests/AC1/multiple-choice.json"
A2 = "content/reading/tests/AC2/multiple-choice.json"
A3 = "content/reading/tests/AC3/multiple-choice.json"
A4 = "content/reading/tests/AC4/multiple-choice.json"
G1 = "content/reading/tests/GT1/multiple-choice.json"
G2 = "content/reading/tests/GT2/multiple-choice.json"

DOSYALAR = [P, A1, A2, A3, A4, G1, G2]


# ---------------------------------------------------------------- duzeltmeler
DUZELT = {
    # ---------------------------------------------------------------- A02
    (P, 2): {
        "mekanizma": "konumsal_duzen",
        "prompt": "In the three days before the octopuses met, the researchers were trying to find out",
        "options": {
            "A": "whether seeing a partner, with no other contact, would matter later on.",
            "B": "whether one steady water temperature removed differences between tanks.",
            "C": "which animal in each pair would win most of its encounters.",
            "D": "whether water-borne chemical cues on their own would be enough.",
        },
        "distractor_analysis": {
            "B": "Yer degistirme -- suyun sabit 24 derecede tutulmasi gercek bir tasarim kararidir ve amaci B paragrafinda veriliyor: davranis degisikligi cevre farkina degil hayvanlarin birbirini yasamasina baglanabilsin diye. Ama bu, barindirma duzeninin amaci; uc gunluk evrenin degil.",
            "C": "Yer degistirme -- ustunluk siralamasi gercekten olculuyor (D/1, guclu hayvan etkilesimlerin ortalama yuzde 76'sini kazaniyor), ama bu birlikte yasama evresinde, hayvanlar bulustuktan sonra.",
            "D": "Yakin ama eksik -- kimyasal ipuclarinin tek basina ne yaptigi tam olarak sinanmayan sey: su hatlari bilerek tamamen ayri tutuluyor, yani bu evrede koku disarida birakiliyor. Secenek sinanan duyunun yerine sinanmayani koyuyor.",
        },
        "explanation": "Paragraph C says the animals spent three days either side of a transparent divider, able to see but not touch or smell one another, and that this stage let the researchers ask whether visual exposure alone was enough to influence later behaviour.",
        "ne_degisti": "Celdiriciler soru kokunun cercevesine tasindi: dorttu de artik pasajda gercekten anlatilan bir arastirma amaci (sabit sicaklik, ustunluk siralamasi, kimyasal ipuclari) ve ucu de baska bir evreye ait. Eskiden yalniz A bir 'duyuyu yalitma' amaciydi; simdi A ve D ayni bicimde kuruldugu icin 'tek duyu yalitan secenek dogrudur' elemesi calismiyor. Dogru secenek kanit cumlesinin sozcuklerinden ('visual exposure alone... influence later behaviour') uzaklastirildi.",
    },
    (P, "3-4"): {
        "mekanizma": "kip_imzasi",
        "options": {
            "A": "Sound carried through water may also play a part.",
            "B": "Sight on its own appears to leave behaviour unchanged.",
            "C": "Sight and touch probably work together.",
            "D": "Smell on its own probably gives the clearest signal.",
            "E": "The early stage tested touch, not sight.",
            "F": "The senses of smell and taste remain too poorly understood.",
            "G": "Taste is better understood than smell.",
        },
        "distractor_analysis": {
            "A": "Cazip ama yok -- su icinde tasinan sesten hic soz edilmiyor; secenek artik olculu yazildigi icin kipine bakarak elenemiyor, yalniz pasajda karsiligi olmadigi icin yanlis.",
            "B": "Kapsam kaydirma -- H/3 gormenin tek basina 'daha zayif ama olculebilir' farklar urettigini soyluyor; secenek bunu hicbir degisiklik olmadigina cekiyor.",
            "D": "Yer degistirme -- 'tek basina' denemesi gorme icin yapiliyor; kokunun tek basina ne yaptigi hic olculmuyor, ustelik ayni cumle koku ve tat duyusunun yeterince bilinmedigini soyluyor.",
            "E": "Yer degistirme -- ilk evrede seffaf bolme yalnizca gormeye izin veriyor, dokunma ve koku disarida birakiliyor; secenek iki duyunun yerini degistiriyor.",
            "G": "Yakin ama eksik -- pasaj tat ile kokuyu birlikte, ikisi de yeterince bilinmeyen duyular olarak aniyor; aralarinda bir siralama yapmiyor.",
        },
        "explanation": "Paragraph H says that sight and physical contact together, rather than either sense alone, most likely underlie this recognition, and that octopuses' sense of smell and taste remains too poorly understood for a contribution from chemical signals to be ruled out.",
        "ne_degisti": "Kip iki yone birden dagitildi. Dogru seceneklerden F mutlak/kesin kipe cekildi ('cannot yet be excluded' -> 'remain too poorly understood'), boylece kesin yazilmis bir dogru secenek olustu. Buna karsilik uc celdirici olculu kipe cekildi (A 'may also', B 'appears to', D 'probably'). Yeni dagilim: olculu 4 secenegin 1'i dogru, kesin 3 secenegin 1'i dogru -- 'olculu = dogru' kurali da 'mutlak = yanlis' kurali da artik calismiyor.",
    },
    # ---------------------------------------------------------------- A05
    (P, 5): {
        "mekanizma": "konumsal_duzen",
        "prompt": "What does the writer say set the site apart from others of its time?",
        "options": {
            "A": "The unusual length of time people went on living there.",
            "B": "Its size, when most communities were still small and mobile.",
            "C": "The far better state of its grain than at sites of the same age.",
            "D": "Its place on a route already used for trading grain.",
        },
        "distractor_analysis": {
            "A": "Yakin ama eksik -- yerlesimin kabaca MO 7400-6000 arasinda iskan edildigi A/2'de veriliyor, ama bu surenin cagdaslarina gore olagandisi oldugu soylenmiyor; siti ayiran ozellik olarak olcek gosteriliyor.",
            "C": "Yer degistirme -- tahillarin benzer yastaki baska sitlerden belirgin bicimde iyi korunmus olmasi B/1'de, buluntular icin soyleniyor; yerlesimin kendisini cagdaslarindan ayiran ozellik olarak degil.",
            "D": "Kapsam kaydirma -- A/3 sitin, tarim uygulamalarini *sonradan* Avrupa'ya tasiyacak yollar uzerinde bulundugunu soyluyor; secenek bunu o donemde zaten isleyen bir tahil ticareti yoluna cekiyor.",
        },
        "explanation": "Paragraph A says that what set the site apart was its scale: at a time when most human communities were still small and mobile, Catalhoyuk had grown into a dense, town-like settlement.",
        "ne_degisti": "Eskiden yalniz B siti kendi cagiyla karsilastiran bir cerceve tasiyordu, oteki ucu ise sure/buluntu/ticaret gibi baska eksenlere kayiyordu; bu yuzden 'ayirt eden ozellik' sorusuna uyan tek secenek B kaliyordu. Simdi A ve C de acikca cag-ici karsilastirma kuruyor ('cagdaslarina gore uzun iskan', 'ayni yastaki sitlerden iyi korunmus tahil') ve ikisi de pasajin gercek ayrintilarina capalandi; secenek bicimi artik dogruyu ele vermiyor.",
    },
    (P, "7-8"): {
        "mekanizma": "kip_imzasi",
        "options": {
            "A": "Einkorn farming began outside Turkey.",
            "B": "Bread wheat was unknown in Europe.",
            "C": "Hexaploid wheat may have appeared earlier than assumed.",
            "D": "The Fertile Crescent account may have to be abandoned.",
            "E": "Modern spelt probably descends from this very wheat.",
            "F": "This is the first genetic sign of a spelt-like wheat in the region.",
            "G": "The team examined a protein gene.",
        },
        "distractor_analysis": {
            "A": "Yer degistirme -- G/2 einkorn tariminin dogdugu yer olarak guney Turkiye'deki Karacadag bolgesini gosteriyor; secenek bu bilgiyi ulke disina tasiyor.",
            "B": "Cazip ama yok -- ekmeklik bugday modern karsilastirma turleri arasinda, Avrupa da yayilma yonu olarak aniliyor, ama Avrupa'da bilinip bilinmedigine dair hicbir ifade yok.",
            "D": "Kapsam kaydirma -- G/1 bulgunun standart anlatiyi 'karmasiklastirdigini' soyluyor; secenek artik olculu yazilmis olsa da anlatinin buutunuyle birakilmasini one suruyor, bu da metnin soylediginden fazlasi.",
            "E": "Kapsam kaydirma -- F/1 eski dizilerin speltayi da iceren modern hexaploid bicimlere *benzedigini* soyluyor; benzerlik, olculu yazilsa bile dogrudan soy bagi iddiasina genisletilemez.",
            "G": "Yakin ama eksik -- ekibin onemli bir bugday proteininden sorumlu gen uzerinde calistigi D/2'de veriliyor, ama bu bir yontem ayrintisi; dizilerden cikarilan bir sonuc degil.",
        },
        "explanation": "Paragraph F says this is the first genetic evidence hinting at a spelt-like wheat in the Neolithic Near East, and paragraph G says the six-chromosome form of wheat may have emerged sooner than researchers had assumed.",
        "ne_degisti": "Dogru seceneklerden F kesin kipe cekildi ('may have been present' -> 'is the first genetic sign'), celdiricilerden D ve E ise olculu kipe cekildi ('is disproved' -> 'may have to be abandoned', 'descends directly' -> 'probably descends'). Yeni dagilim: olculu 3 secenegin 1'i dogru, kesin 4 secenegin 1'i dogru. 'Temkinli yazilan ikili dogrudur' imzasi kirildi.",
    },
    # ---------------------------------------------------------------- A08
    (P, 12): {
        "mekanizma": "konumsal_duzen",
        "prompt": "Why does the writer quote a researcher's reaction to the images?",
        "options": {
            "A": "To explain why the region's ice has been watched for years.",
            "B": "To stress how little of the range can be checked from the ground.",
            "C": "To show how unusual a disturbance on this scale is.",
            "D": "To confirm that the ground survey matched the satellite images.",
        },
        "distractor_analysis": {
            "A": "Yakin ama eksik -- arastirmacinin bolgenin buzunu yillardir izledigi tam da bu cumlede (E/2) soyleniyor, ama bu, sozun aktarilma amaci degil, konusani tanitan bir ayrinti.",
            "B": "Yakin ama eksik -- daglik alanin buyuk olcude ulasilmaz oldugu hem E/3'te hem H/1'de geciyor; yine de alintinin islevi erisim sorununu anlatmak degil, olayin buyuklugunu vurgulamak.",
            "D": "Yer degistirme -- yer arastirmasinin uydu goruntulerini dogrulamasi D/2'de, ayri bir cumlede anlatiliyor; arastirmacinin sozu bir dogrulama degil bir sasirma ifadesi.",
        },
        "explanation": "Paragraph E reports a researcher saying that the number and magnitude of the avalanches and landslides was astounding and that nothing comparable had been documented there before; the writer adds that this reflects how unusual such an event is.",
        "ne_degisti": "Eski A ('hasar beklenmisti') ve D ('uydu goruntulerine kusku dusurmek') alintinin icerigiyle acikca celisiyor, B ise cerceve disinda kaliyordu; ucu de pasaja bakmadan elenebiliyordu. Dort secenek de artik pasajin gercek ayrintilarina capalanmis, kendi icinde tutarli yazarlik amaclari: yillardir suren izleme (E/2), yerden denetlenemezlik (H/1), olcegin sira disiligi (E/3), yer arastirmasinin dogrulamasi (D/2).",
    },
    # ---------------------------------------------------------------- A11
    (P, 14): {
        "mekanizma": "konumsal_duzen",
        "prompt": "What reason does the writer give for the choice of the campus spot?",
        "options": {
            "A": "Reaching it involved a walk, as the forest did.",
            "B": "Its noise was measured alongside the forest's.",
            "C": "It was calm rather than obviously stressful.",
            "D": "Participants already knew the place from daily use.",
        },
        "distractor_analysis": {
            "A": "Yakin ama eksik -- iki kosulda da yurunuyor (ormana bes, kampus noktasina iki dakika, C/1-2), ama yurumek yerin secilme gerekcesi olarak verilmiyor.",
            "B": "Yer degistirme -- olculen cevre degiskenleri D paragrafinda sayiliyor (sicaklik, kar kalinligi, nem, ruzgar) ve bunlar yalniz orman oturumlari icin; gurultu hic olculmuyor.",
            "D": "Cazip ama yok -- katilimcilar bir uygulamali bilimler universitesinin ogrencileri (B/1), ama noktayi gunluk olarak kullandiklarina dair bir ifade yok.",
        },
        "explanation": "Paragraph C says the researchers deliberately chose a comparison environment that was calm and free of traffic rather than obviously stressful.",
        "ne_degisti": "Eskiden B ortami tam tersine ceviriyordu ('kent caddesi gibi gurultulu'), A ve D ise pasajla hic baglanti kurmayan ayrintilardi; kontrol kosulu mantigini bilen bir cozucu C'yi elemeyle buluyordu. Yeni celdiricilerin ucu de pasajin gercek ayrintilarina dayaniyor (yurume suresi C/1-2, olculen cevre degiskenleri D, katilimcilarin universite ogrencisi olmasi B/1) ve hicbiri ortamin niteligini tersine cevirmiyor.",
    },
    (P, 15): {
        "mekanizma": "konumsal_duzen",
        "prompt": "What do the researchers recommend that future studies test?",
        "options": {
            "A": "Busier streets, measured noise levels and heart-rate readings.",
            "B": "Repeat visits, longer gaps between them and follow-up surveys.",
            "C": "Older participants, other tree species and evening rather than daytime visits.",
            "D": "Longer visits, other seasons and other cultural backgrounds.",
        },
        "distractor_analysis": {
            "A": "Yer degistirme -- karsilastirma ortami bilerek trafiksiz seciliyor (C/2) ve olculen degiskenler arasinda gurultu ya da nabiz yok; secenek onerilmemis bir olcum setini siraliyor.",
            "B": "Cazip ama yok -- sakinlestirici etkinin ne kadar surdugu ilgi cekici bir devam adimi gibi gorunuyor, ama H/2'deki oneri listesinde tekrar ziyaret ya da takip anketi gecmiyor.",
            "C": "Cazip ama yok -- agac turleri (yuzde 80 ladin, yuzde 20 hus) ve oturum zamani C ve D'de veriliyor, ama bunlarin sinanmasi onerilmiyor; oneri yas degil kultur ekseninde.",
        },
        "explanation": "Paragraph H says the researchers recommend that future work test longer exposure times, other seasons, and participants from different cultural backgrounds.",
        "ne_degisti": "Eskiden yalniz D uc ogeli bir liste bicimindeydi, yani bilimsel makalelerin 'gelecek calisma onerisi' kalibini tasiyan tek secenekti; C ise oneriyi tersine cevirdigi icin (yalniz kisa daraltma) parcasiz elenebiliyordu. Dort secenek de artik uc ogeli, akla yatkin birer oneri listesi ve hicbiri kendi icinde tutarsiz degil; ayirt etme yalniz H/2'yi okumakla mumkun.",
    },
    # ---------------------------------------------------------------- A03 / AC1
    (A1, 33): {
        "mekanizma": "konumsal_duzen",
        "prompt": "What does the writer say about the survey that began in May 2014?",
        "options": {
            "A": "A second visit was planned for later the same year",
            "B": "It was the first time instruments were left recording there",
            "C": "The material the divers collected was analysed on site",
            "D": "It was run by a team based in the Northern Marianas",
        },
        "distractor_analysis": {
            "B": "Cazip ama yok -- ekibin surekli kayit alan cihazlar yerlestirdigi D/2'de soyleniyor, ama bunun ilk kez yapildigina dair bir ifade yok; ustelik A/1 sahanin dunyanin en yakindan incelenen resif alanlarindan biri oldugunu soyluyor.",
            "C": "Yer degistirme -- dalgiclarin hunilerle topladigi gaz kabarciklari acikca 'laboratuvar analizi icin' toplaniyor (D/2); olcumlerin bir kismi sahada surse de toplanan malzeme sahada incelenmiyor.",
            "D": "Yer degistirme -- ekibi yoneten Ian Enochs, NOAA'nin Miami Universitesi'ndeki enstitusune bagli (D/1); Kuzey Mariana Adalari calismanin yeri, ekibin merkezi degil.",
        },
        "explanation": "Paragraph D says the detailed survey at Maug began in May 2014, with a follow-up visit planned for that August.",
        "ne_degisti": "Eski celdiriciler bicimlerinden taniniyordu: B 'ilk kez yapilan calisma' seklinde bir kapsam abartmasi, D var olmayan basarisiz bir denemeye gonderme, C ise gorunurde ilgisiz bir yer degisikligiydi; olculu ve somut yazilmis tek secenek A kaliyordu. Simdi dort secenek de ayni somutlukta, pasajin gercek ayrintilarina capalanmis olgu iddialari (cihaz yerlestirme D/2, laboratuvar analizi D/2, ekibin bagli oldugu kurum D/1).",
    },
    # ---------------------------------------------------------------- A06 / AC2
    (A2, 32): {
        "mekanizma": "konumsal_duzen",
        "prompt": "Why did the researchers combine three separate sets of records?",
        "options": {
            "A": "To follow employees as they moved between departments",
            "B": "To set an individual's output beside the teammates around them",
            "C": "To check the company's own figures against what staff reported",
            "D": "To stretch the study over more months than one source covered",
        },
        "distractor_analysis": {
            "A": "Kapsam kaydirma -- kayitlar sirketin tek bir departmanindan aliniyor (B/1), dolayisiyla departmanlar arasi hareketi izlemek soz konusu degil; kaynaklardan birinin insan kaynaklari kayitlari olmasi bunu akla yatkin kiliyor.",
            "C": "Yakin ama eksik -- calisanin kendi beyanina dayanan olculer D/1'de aniliyor, ama karsilastirma malzemesi olarak degil, kacinilan bir belirsizlik kaynagi olarak.",
            "D": "Cazip ama yok -- inceleme donemi Nisan 2022 - Mart 2023 ile sinirli ve bu sure kaynak sayisina bagli degil; birlestirmenin sagladigi sey daha uzun sure degil, daha genis bilgi.",
        },
        "explanation": "Paragraph B says that combining the three sources let the researchers see not only how much each employee produced, but also who they were working alongside and how often they exchanged messages with teammates.",
        "ne_degisti": "Dogru secenek kanit cumlesinin sozcuklerinden uzaklastirildi ('see... how much each employee produced, but who they were working alongside' -> 'set an individual's output beside the teammates around them'). Soru koku de 'neden birlestirildi' bicimine cekilip dort secenek ayni amac kalibina ('To ...') getirildi; boylece dogru secenegi kanit cumlesinin yankisi olmasindan taniyan kestirme kapandi.",
    },
    (A2, 33): {
        "mekanizma": "konumsal_duzen",
        "prompt": "What did the finding on internal messaging call into question?",
        "options": {
            "A": "The finding that newcomers gain most from experienced teammates",
            "B": "The claim that team membership was decided at random",
            "C": "The measure chosen to judge how much work each person did",
            "D": "The assumption that longer-serving teams keep in touch more often",
        },
        "distractor_analysis": {
            "A": "Yakin ama eksik -- ilk yilindaki calisanlarin yaklasik yuzde 26.2 kazandigi bulgusu F/2'de veriliyor ve mesajlasma bulgusu bunu sarsmiyor, tersine aciklamaya calisiyor.",
            "B": "Yer degistirme -- katilma sirasina gore takim kurma C/1'de anlatiliyor ve calismanin gucu olarak sunuluyor; mesajlasma bulgusu bu duzeni degil, deneyimle iletisim arasinda varsayilan bagi sorguluyor.",
            "C": "Yakin ama eksik -- hizmet verilen musteri sayisinin cikti olcusu olarak secilmesi D/1-2'de savunuluyor; mesajlasma bulgusu bu olcunun gecerliligine dokunmuyor.",
        },
        "explanation": "Paragraph G says a further finding complicated the obvious explanation that experienced teams simply talk to one another more: the teams with the highest average tenure in fact communicated internally less.",
        "ne_degisti": "Eski A ('mesajlasmanin olculebilirligi') anlamca sacma oldugu icin parcasiz eleniyordu ve geri kalan iki celdirici de pasajin acikca dogruladigi seyleri hedef gosteriyordu. Dort secenek de artik metnin gercekten kurdugu birer iddia (F/2 yeni calisanlarin kazanci, C/1 rastgele takim kurulusu, D/1-2 cikti olcusu, G/1 deneyim-iletisim bagi) ve hepsi 'sorgulanabilir' cercevede; ayirt etme G/1'i okumaya bagli. Dogru secenek de kanit cumlesinin sozcuklerinden uzaklastirildi.",
    },
    (A2, "34-35"): {
        "mekanizma": "konumsal_duzen",
        "options": {
            "A": "Star performers were spread too thinly across the teams",
            "B": "Employees' first six months were left out of the figures",
            "C": "Employees are paid only for what they produce themselves",
            "D": "Each client contract fixes the hours a worker gives",
            "E": "Highly productive staff sent fewer messages than others",
            "F": "Colleagues never see one another face to face",
            "G": "Teams were formed by joining order rather than by choice",
        },
        "distractor_analysis": {
            "A": "Yer degistirme -- en iyi calisanlari takimlara dagitmak H/4'te yazarin *onermedigi* bir yonetim aliskanligi olarak geciyor; sirkette uygulanan bir duzen degil, dolayisiyla etkinin yoklugunu aciklayamaz.",
            "B": "Kapsam kaydirma -- disarida birakilan sey calisanlarin ilk alti ayi (B/1) ve amaci ornegin yerlesik personelden olusmasi; yeni personelin kendisi analizde var, ustelik en buyuk kazanc onlarda (F/2).",
            "D": "Yakin ama eksik -- her musteri sozlesmesinin sabit otuz saat ayirdigi D/1'de veriliyor, ama bu bilgi ciktinin nasil olculdugune ait; akran etkisinin yokluguyla ilgili degil.",
            "E": "Yer degistirme -- G/1 deneyimli ya da zaten verimli calisanlarin *dusuk iletisimli ortamlarda* daha iyi is cikardigini soyluyor; bu kisilerin daha az mesaj yazdigi iddia edilmiyor.",
            "G": "Yakin ama eksik -- katilma sirasina gore takim kurulusu C/1'de calismanin nicin guvenilir sayildigini acikliyor; etkinin neden gorunmedigini degil.",
        },
        "explanation": "Paragraph H says that Caster pays employees according to individual output alone, which removes much of the incentive to match a team's overall performance, and that without face-to-face contact to reinforce peer pressure it appears to have little effect at all.",
        "ne_degisti": "Eskiden yalniz C ve F 'etkinin neden gorunmedigi' cercevesinde yaziliyor, oteki bes secenek baska bir bulguyu ya da yontem ayrintisini anlatiyordu; bu yuzden cerceve tek basina dogru ikiliyi veriyordu. Yedi secenek de yeniden yazilarak ayni cerceveye tasindi -- her biri simdi akran etkisinin yoklugu icin one surulebilecek makul bir aciklama bicimindedir (dagitim, orneklem disi birakma, sabit saat, dusuk mesajlasma, atama duzeni) ve yanlisliklari ancak pasajda nereye ait olduklari gorulunce anlasiliyor.",
    },
    # ---------------------------------------------------------------- A09 / AC3
    (A3, 33): {
        "mekanizma": "konumsal_duzen",
        "prompt": "What was the team's purpose-built image-processing method used for?",
        "options": {
            "A": "Working out which elements the glassy material contained",
            "B": "Checking that the sheaths still had all their layers",
            "C": "Picking out real nerve tissue among the glass around it",
            "D": "Matching the proteins found against brain reference databases",
        },
        "distractor_analysis": {
            "A": "Yer degistirme -- kimyasal bilesimi olcen is, ayni paragrafta sayilan enerji dagilimli X isini yontemine ait (D/2); goruntu isleme rutininin islevi bu degil.",
            "B": "Kapsam kaydirma -- kiliflarin cok katmanli yapisini korudugu E/2'de bir olcum sonucu olarak veriliyor; yontem katmanlarin eksiksizligini dogrulamak icin degil, miyeline ozgu tekrarlayan deseni yakalamak icin gelistirildi.",
            "D": "Yer degistirme -- proteinlerin referans veri tabanlariyla karsilastirilmasi D/4'te ayri ve son basamak olarak sayiliyor; goruntu isleme rutini protein degil desen ariyor.",
        },
        "explanation": "Paragraph D says the custom image-processing method, developed to detect the repeating pattern typical of myelin, helped distinguish genuine neural structures from random glassy debris.",
        "ne_degisti": "Eski D ('cok daha buyuk bir ornek kumesi') uydurmaydi ve buluntunun tek bir bireye ait olmasiyla acikca celisiyordu; B ise dogrulanamayan bir mutlaklik ('her katman') tasiyordu. Dort secenek de artik D ve E paragraflarinda gercekten anlatilan islerden biri (X isini olcumu, katmanli yapinin olculmesi, desen ayikliyici rutin, veri tabani karsilastirmasi); hangi isin hangi yontemin oldugunu bilmek icin paragrafi okumak gerekiyor. Dogru secenek kanit cumlesinin sozcuklerinden de uzaklastirildi.",
    },
    # ---------------------------------------------------------------- A12 / AC4
    (A4, 32): {
        "mekanizma": "konumsal_duzen",
        "prompt": "Why does the writer say the nap question has practical importance?",
        "options": {
            "A": "Employers now offer rest breaks and shorter working days",
            "B": "Students rely on naps to revise and to make up lost sleep",
            "C": "In some cultures napping is ordinary; in others a full night is hard to get",
            "D": "Researchers disagree about what consolidation is and when it happens",
        },
        "distractor_analysis": {
            "A": "Cazip ama yok -- isverenlerden, dinlenme molasindan ya da kisa is gununden hic soz edilmiyor; gunduz uykusunun yayginligi anlatildigi icin akla yatkin gorunuyor.",
            "B": "Yakin ama eksik -- ders calismak ya da kaybedilen uykuyu telafi etmek icin sekerlemeye guvenenler H/1-2'de geciyor; ama bu, bulgularin uygulamadaki karsiligi, sorunun A paragrafinda verilen gerekcesi degil.",
            "D": "Yer degistirme -- pekistirme A/1'de tanimlaniyor ve yerlesik bir surec olarak sunuluyor; belirsiz olan sey pekistirmenin ne oldugu degil, kisa bir sekerlemenin gece uykusuyla ayni yarari saglayip saglamadigi.",
        },
        "explanation": "Paragraph A ties the practical importance of the question to two situations: cultures where daytime napping is common, and societies where a full night's sleep is often in short supply.",
        "ne_degisti": "Eskiden yalniz C iki parcali karsitlik bicimindeydi ve pasajin kendi ikili cercevesini birebir yansitiyordu; ustelik en uzun secenekti. Dort secenek de artik iki ogeli yazildi ve ucu pasajin gercek ayrintilarina capalandi (H/1-2 ogrencilerin sekerlemeye guvenmesi, A/1 pekistirmenin tanimi); dogru secenegin dis bicimi artik ayirt edici degil.",
    },
    # ---------------------------------------------------------------- G03 / GT1
    (G1, 21): {
        "mekanizma": "konumsal_duzen",
        "prompt": "What must an employee who forgets their clock-in card do?",
        "options": {
            "A": "Report to their supervisor before that shift ends",
            "B": "Collect a form for it from the staff office",
            "C": "Have the day's hours checked by hand instead",
            "D": "Have the day recorded as a formal attendance concern",
        },
        "distractor_analysis": {
            "B": "Yer degistirme -- personel ofisinden alinan form, C paragrafinda degil D paragrafinda geciyor ve vardiya takasi icin kullaniliyor; kartini unutan calisan icin bir form ongorulmuyor.",
            "C": "Kapsam kaydirma -- saatlerin elle dogrulanmasi tek seferlik unutmanin degil, tekrar tekrar dogru giris yapmamanin sonucu olarak veriliyor (C/2).",
            "D": "Yer degistirme -- resmi devamsizlik kaydi, bir aylik donem icinde uc kez on dakikadan fazla gec kalmanin sonucu (C/3); kart unutmanin degil.",
        },
        "explanation": "Paragraph C of Text A says that employees who forget their card should report to their supervisor within the same shift.",
        "ne_degisti": "Eski C ('personel girisinden yedek kart almak') pasajda hic gecmeyen uydurma bir islemdi ve parcasiz elenebiliyordu; B ve D ise cerceve disinda kaliyordu. Dort secenek de artik el kitabinin C ve D paragraflarinda gercekten bulunan islemler (amire bildirme, personel ofisi formu, saatlerin elle dogrulanmasi, resmi devamsizlik kaydi); hangisinin kart unutmaya ait oldugunu bulmak icin C/2'yi okumak gerekiyor.",
    },
    # ---------------------------------------------------------------- G04 / GT2
    (G2, 21): {
        "mekanizma": "kip_imzasi",
        "prompt": "What does the writer say about the graduate programme?",
        "options": {
            "A": "Interns may apply for it once their placement ends",
            "B": "Fifteen places on it are shared out across the departments",
            "C": "Invitations to apply are tied to what the business needs",
            "D": "It is likely to start within weeks of the internship finishing",
        },
        "distractor_analysis": {
            "A": "Kapsam kaydirma -- basvuru daveti yalniz guclu performans gosteren stajyerlere taniniyor ve ertesi yil icin geciyor (A metni D/2); secenek olculu yazilmis olsa da hakki butun stajyerlere ve stajin bitisine tasiyor.",
            "B": "Yer degistirme -- on bes kisilik kontenjan staj programina ait (A metni C/2); secenek bu sayiyi mezun programina yukluyor.",
            "D": "Yakin ama eksik -- metin davetin ertesi yil icin oldugunu soyluyor; stajin bitisinden birkac hafta sonra baslayan bir programdan soz edilmiyor.",
        },
        "explanation": "Paragraph D of Text A says that strong performers may be invited to apply for the graduate programme the following year, though this is not guaranteed and depends on business need.",
        "ne_degisti": "Kip ters yone cevrildi: dogru secenek C'nin olculu ifadesi ('depends partly on') kesin bicime getirildi ('are tied to what the business needs'), buna karsilik A ve D olculu kipe cekildi ('any intern can' -> 'interns may', 'begins soon after' -> 'is likely to start'). Artik olculu yazilan iki secenek de yanlis, kesin yazilan iki secenegin biri dogru; 'olculu = dogru' imzasi kalkti.",
    },
    (G2, 22): {
        "mekanizma": "kip_imzasi",
        "prompt": "What does the writer say about staff who deal directly with clients?",
        "options": {
            "A": "They can be asked to come in on more days than others",
            "B": "They are not allowed to work remotely at all",
            "C": "They might also need written approval from the HR team",
            "D": "They receive a larger equipment allowance than other staff",
        },
        "distractor_analysis": {
            "B": "Kapsam kaydirma -- metin bu rollerin ofise daha sik cagrilabilecegini soyluyor (B metni A/2); secenek bunu tam bir uzaktan calisma yasagina buyutuyor.",
            "C": "Yer degistirme -- hem IK'dan hem ilgili ulke ofisinden yazili onay sarti yurt disindan calismak icin gecerli (B metni D/2); musteriyle calisan roller icin degil.",
            "D": "Yakin ama eksik -- ev ofisi ekipmani icin yillik 150 sterlinlik geri odeme butun uzaktan calisanlar icin ayni (B metni B/4); bu gruba ek bir odenek taninmiyor.",
        },
        "explanation": "Paragraph A of Text B says that staff in client-facing roles may be required to attend the office more frequently, regardless of the general policy on remote days.",
        "ne_degisti": "Dogru secenek A metnin kendi 'may be required' kalibini birebir yankilamayacak bicimde yeniden yazildi ('may need to spend' -> 'can be asked to come in'), celdiricilerden C olculu kipe cekildi ('need approval' -> 'might also need'), D ise kesin bicimde birakildi. Yeni dagilim: olculu 2 secenegin 1'i dogru, kesin 2 secenegin 0'i dogru. GT2 setinin tamami icinde (21 ve 22 birlikte) olculu 4 secenegin 1'i, kesin 4 secenegin 1'i dogru -- set duzeyinde kip dengelenmis oldu.",
    },
}


# ------------------------------------------------------------------ elenenler
ELE = {
    (P, 1): "Sorunun ekseni deney tasarimi genel bilgisi: hayvan deneylerinde deneklerin agirliga gore eslestirilmesi pasajdan bagimsiz bilinen standart bir uygulama. Cinsiyet, toplanma mevsimi ve komsuluk daha az tipik olcutler oldugu icin secenekler nasil yazilirsa yazilsin agirlik en olasi cevap kalir; kip dengelemesi ya da celdirici capalamasi bunu kapatmaz.",
    (P, 6): "Sorunun ekseni terimin kendisi: soru kokundeki 'hexaploid' sozcugunun 'hexa-' oneki dogrudan alti kromozom takimini soyluyor, yani sizinti secenek diziliminde degil kokte. Terimi soru kokunden cikarmak kanit cumlesini de degistirmeyi gerektirir; bu, gorev kuralina gore yarim duzeltme sayilir.",
    (P, "9-10"): "Sorunun ekseni cografya genel bilgisi: buyuk buzullu siradaglarin bir ulke siniri boyunca uzanmasi ve kalin buzla ortulu olmasi pasaja bakmadan bilinebiliyor. Iki dogru secenek de bolgenin ansiklopedik tanimini tekrarliyor; secenekleri yeniden yazmak bu ekseni degistirmez.",
    (P, 11): "Sorunun ekseni uzaktan algilama genel bilgisi: uydu goruntusuyle hasar tespitinin oncesi-sonrasi karsilastirmasiyla yapilmasi standart afet izleme yontemi. Kanit cumlesinin kendisi bu standardin anlatimi oldugu icin celdiricileri guclendirmek yetmiyor.",
    (P, 13): "Sorunun ekseni arastirma yontemi kurali: kosul sirasinin rastgelestirilmesinin amaci tekrar test etme (sira/alistirma) etkisini kontrol altina almaktir ve bu, pasajdan bagimsiz olarak ogretilen bir kural. Seceneklerin kipi ya da capasi degistirilse de cevap yontem bilgisinden cikar.",
    (A1, 32): "Sorunun ekseni jeoloji genel bilgisi: volkanik adalarda magmanin deniz tabani bacalarindan surekli gaz salmasi bilinen bir olgu, dolayisiyla yazarin jeolojiyi neden anlattigi parcaya bakmadan cikarilabiliyor. Celdiricileri metne capalamak sorunun eksenini degistirmiyor.",
    (A1, "34-35"): "Sorunun ekseni alan bilgisi: okyanus asitlenmesi calismalarinin biri deniz tabani toplulugu, digeri iskeletin ic yapisi olmak uzere iki eksende yurutuldugu genel olarak biliniyor. Yedi secenek arasindan hangilerinin 'calisilmis' oldugunu secmek pasaji degil bu yerlesik kalibi olcuyor.",
    (A3, 32): "Sorunun ekseni arkeoloji genel bilgisi: Herculaneum'un organik malzemeyi -- ahsap, yiyecek, kumas -- olaganustu iyi korumasiyla taninmasi yaygin bir bilgi. Sayilan nesnelerin neden anildigi bu bilgiyle dogrudan biliniyor; secenek dengelemesi bunu kapatmaz.",
    (A3, "34-35"): "Sorunun ekseni temel kimya/biyoloji bilgisi: organik dokunun buyuk kismini karbon ve oksijenin olusturmasi (B) ve beyin dokusunda noronlar arasi iletisimle ilgili bir proteinin bulunmasi (F) beklenen bulgular. Iki dogru secenek de pasaji degil alan bilgisini siniyor.",
    (A4, 33): "Sorunun ekseni deney tasarimi kurali: uyku ile uyanikligi karsilastiran adil bir kiyaslamada ogrenme ile sinav arasindaki surenin esit tutulmasi gerektigi pasajdan bagimsiz biliniyor. Secenekler nasil dizilirse dizilsin 'esit sure' cevabi yontem mantigindan cikar.",
    (A4, "34-35"): "Sorunun ekseni uyku bilimi genel bilgisi: beyin etkinliginin polisomnografiyle kaydedilmesi (C) ve kisa sekerlemelerin agirlikla hafif 2. evre uykudan olusmasi (E) alan bilgisi olarak biliniyor. Yedi secenek arasindan bu ikisini secmek pasaji okumayi gerektirmiyor.",
    (G1, 22): "Sorunun ekseni calisma mevzuati genel bilgisi: iki vardiya arasinda en az on bir saat dinlenme birakilmasi yaygin bilinen bir duzenleme. Secenekler yeniden yazilsa da 'yeterli dinlenme yok' cevabi mevzuat bilgisinden cikar.",
    (G1, "23-24"): "Sorunun ekseni is yeri politikalarinin standart maddeleri: fazla mesainin onceden amir onayi gerektirmesi (B) ve on saati asan kismin izne cevrilebilmesi (E) cok sayida is yerinde gecerli. Yedi secenek arasindan bu ikisini secmek metni degil is hayati bilgisini olcuyor.",
    (G2, "23-24"): "Sorunun ekseni uzaktan calisma politikalarinin standart maddeleri: cekirdek saatlerde ulasilabilir olmak (B) ve kalici konum degisikligini IK'ya bildirmek (D) bu tur politikalarda neredeyse her zaman bulunur. Secenek dengelemesi bu ekseni degistirmez.",
}

TIP_ETIKET = "multiple_choice"


def yukle(p):
    with io.open(p, encoding="utf-8") as f:
        return json.load(f)


def yaz(p, d):
    with io.open(p, "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")


def main():
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    duzeltildi = elendi = dokunulmadi = 0
    yeni_elenen = []

    for p in DOSYALAR:
        d = yukle(p)
        pasaj_zarf = d.get("passage_id")
        for it in d["items"]:
            if it.get("status") != "flagged":
                continue
            anahtar = (p, it["number"])

            if anahtar in DUZELT:
                r = DUZELT[anahtar]
                onceki_prompt = it["prompt"]
                onceki_secenekler = {o["letter"]: o["text"] for o in it["options"]}

                if "prompt" in r:
                    it["prompt"] = r["prompt"]
                for o in it["options"]:
                    if o["letter"] in r["options"]:
                        o["text"] = r["options"][o["letter"]]

                # celdirici cozumlemesi yalniz dogru olmayan harfleri kapsar
                dogru = set(it["answer"])
                bekl = set(o["letter"] for o in it["options"]) - dogru
                if set(r["distractor_analysis"]) != bekl:
                    raise SystemExit(
                        "celdirici harfleri uyusmuyor: %s %s -- beklenen %s, verilen %s"
                        % (p, it["number"], sorted(bekl),
                           sorted(r["distractor_analysis"])))
                it["distractor_analysis"] = dict(r["distractor_analysis"])
                it["explanation"] = r["explanation"]

                it["status"] = "verified"
                it["blind_solvable"] = None
                it["revision"] = {
                    "tarih": TARIH,
                    "mekanizma": r["mekanizma"],
                    "onceki_prompt": onceki_prompt,
                    "onceki_secenekler": onceki_secenekler,
                    "ne_degisti": r["ne_degisti"],
                }
                duzeltildi += 1

            elif anahtar in ELE:
                it["status"] = "rejected"
                it["reject_reason"] = ELE[anahtar]
                yeni_elenen.append({
                    "dosya": p.replace("\\", "/"),
                    "numara": it["number"],
                    "tip": TIP_ETIKET,
                    "pasaj": it.get("passage_id") or pasaj_zarf,
                    "kacinilacak": {
                        "kanit_cumlesi": it.get("evidence"),
                        "soru_koku": it["prompt"],
                    },
                    "neden_elendi": ELE[anahtar],
                })
                elendi += 1
            else:
                dokunulmadi += 1

        yaz(p, d)

    # E6 devir dosyasi -- uzerine yazilmaz, eklenir
    yol = "content/DOGRULAMA/yeniden-uretim-listesi.json"
    liste = yukle(yol)
    var = set((e["dosya"], str(e["numara"]), e["tip"]) for e in liste["elenen"])
    for e in yeni_elenen:
        if (e["dosya"], str(e["numara"]), e["tip"]) not in var:
            liste["elenen"].append(e)
    yaz(yol, liste)

    print("duzeltildi %d - elendi %d - dokunulmadi %d"
          % (duzeltildi, elendi, dokunulmadi))
    print("yeniden-uretim-listesi.json toplam elenen: %d" % len(liste["elenen"]))


if __name__ == "__main__":
    main()
