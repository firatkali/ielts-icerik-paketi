# -*- coding: utf-8 -*-
"""E5 - 1. calistirma: YES/NO/NOT GIVEN, kip imzasi.

`prompts/OPUS5-E5-isaretli-elden-gecirme.md` 1. grubu uygular.

Kural: `answer` ve `evidence` alanlarina DOKUNULMAZ. Yalniz `prompt` (ifade metni)
yeniden yazilir; ona bagli ic denetim alanlari (contradiction_point,
not_given_justification, scan_note) ve kullaniciya gorunen `explanation` guncellenir.
`explanation` Ingilizce yazilir (2026-08-08 sonrasi depo kurali).

Uc sonuc:
  duzeltildi  -> status "verified", blind_solvable None, revision blogu
  elendi      -> status "rejected", reject_reason; soru dosyada kalir
  dokunulmadi -> status degismez, neden explanation/NOTLAR'a yazilir
"""
import json
import os

TARIH = "2026-08-08"
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PRACTICE = "content/reading/practice/yes-no-not-given.json"
GT1 = "content/reading/tests/GT1/yes-no-not-given.json"
GT2 = "content/reading/tests/GT2/yes-no-not-given.json"


# --------------------------------------------------------------------------
# 1) DUZELTILEN SORULAR
# --------------------------------------------------------------------------
# Her kayit: yeni prompt + ona bagli alanlar. answer/evidence yok - dokunulmuyor.

DUZELTME = {
    (PRACTICE, 3): {
        "prompt": "Employees placed alongside star performers tended to produce a "
                  "little more than they otherwise would.",
        "difficulty": "medium",
        "explanation": "The writer states that whatever benefit workers usually gain "
                       "from star performers did not appear in this study at all, so "
                       "even a small rise is ruled out.",
        "contradiction_point": "E/3, yildiz calisanlardan genelde elde edilen faydanin "
                               "'burada gorulmedigini' soyluyor; ifade kucuk de olsa bir "
                               "artis oldugunu one suruyor. Celiski tek noktada: artisin "
                               "var olup olmadigi.",
        "scan_note": "Yildiz calisanlarin etkisi E paragrafinda (E/2 olculebilir iyilesme "
                     "yok, E/3 faydanin burada gorulmedigi) ve H/2'de ele aliniyor; hicbir "
                     "cumle olculu de olsa bir artistan soz etmiyor.",
        "ne_degisti": "Ifadedeki 'clearly' mutlak zarfi kaldirildi; iddia 'tended to "
                      "produce a little more' bicimine, yani olculu kipe cekildi. Boylece "
                      "'mutlak ifade = NO' imzasi kirildi: artik olculu yazilmis bir NO "
                      "var. Kanit cumlesi (E/3) faydanin hic gorulmedigini soyledigi icin "
                      "olculu iddiayi da ayni netlikte curutuyor.",
    },
    (PRACTICE, 6): {
        "prompt": "The researchers were able to rank only two of the four office "
                  "designs against each other.",
        "difficulty": "medium",
        "explanation": "The writer reports a clear ranking covering all four designs, "
                       "not just two of them.",
        "contradiction_point": "D/1 sonuclarin dort tasarim arasinda net bir siralama "
                               "gosterdigini soyluyor; ifade siralamanin yalnizca ikisini "
                               "kapsadigini iddia ediyor. Celiski tek noktada: siralamanin "
                               "kac tasarimi kapsadigi.",
        "scan_note": "Siralama D paragrafinda veriliyor: D/1 dort tasarimi kapsayan net "
                     "siralama yargisi, D/2-D/3 dort tasarimin da sayilari. E akis "
                     "puanlarini ekliyor; hicbir cumle siralamayi iki tasarimla "
                     "sinirlamiyor.",
        "ne_degisti": "Blanket olumsuzlama ('failed to produce a clear ordering') yerine "
                      "belirli sayisal bir iddia kondu. Eski bicim, 'arastirma pasajlari "
                      "sonuc bildirir' sezgisiyle mutlak olumsuzlamanin yanlis cikacagi "
                      "tahmininden coziluyordu; yeni bicim pasajdaki siralamanin kapsamini "
                      "bilmeyi gerektiriyor. Kanit cumlesi (D/1) degismedi.",
    },
    (PRACTICE, 7): {
        "prompt": "On sustained concentration, both partly enclosed layouts outscored "
                  "every other design in the trial.",
        "difficulty": "medium",
        "explanation": "The writer reports higher flow scores for both the team-office "
                       "and the zoned design than for either the fully open or the fully "
                       "unassigned arrangement, which are the only other layouts tested.",
        "scan_note": "Odaklanma ve akis E paragrafinda: E/2 iki yari kapali duzenin hem "
                     "tamamen acik hem de sabit masasiz duzenden daha surekli konsantrasyon "
                     "sagladigini soyluyor. Denenen dort duzenden geri kalan ikisi tam olarak "
                     "bunlar; F gurultu verisiyle destekliyor, celisen cumle yok.",
        "ne_degisti": "Olculu karsilastirma ('came more easily ... than the remaining "
                      "designs') yerine kapsayici/mutlak bir ifade kondu ('outscored every "
                      "other design in the trial'). Kip imzasini kirmanin ikinci yonu: "
                      "artik mutlak yazilmis bir YES var, yani 'mutlak = NO' kurali bu "
                      "sette yanlis cevap veriyor. Kanit cumlesi (E/2) iddiayi aynen "
                      "karsiliyor: geri kalan iki duzen zaten tam acik ve sabit masasiz "
                      "duzenler.",
    },
    (PRACTICE, 14): {
        "prompt": "Whether the word pairs were related or unrelated seems to have "
                  "mattered little to how well they were later recalled.",
        "difficulty": "medium",
        "explanation": "The writer reports a clear difference in recall depending on the "
                       "type of material, so the distinction mattered a great deal.",
        "contradiction_point": "E/1 sonuclarin 'hatirlanan malzemenin turune bagli net bir "
                               "fark' ortaya koydugunu soyluyor; ifade bu farkin onemsiz "
                               "oldugunu one suruyor. Celiski tek noktada: turun yarattigi "
                               "farkin buyuklugu.",
        "scan_note": "Malzeme turunun etkisi E paragrafinda (E/1 net fark yargisi, E/2 "
                     "iliskili ve iliskisiz ciftler icin ayri etki buyuklukleri) ve G'de "
                     "isleniyor; ikisi de farkin belirgin oldugunu soyluyor.",
        "ne_degisti": "Mutlak olumsuzlama ('made no difference') yerine olculu bir kucumseme "
                      "('seems to have mattered little') kondu. Eski bicim, arastirma "
                      "pasajlarinda mutlak olumsuzlamanin neredeyse her zaman yanlis cikmasi "
                      "kaliyla parcasiz coziluyordu. Kanit cumlesi (E/1) 'net bir fark' "
                      "dedigi icin olculu iddiayi da curutuyor.",
    },
    (GT1, 35): {
        "prompt": "Food that households composted or gave to animals was left out of the "
                  "study's main waste totals.",
        "difficulty": "medium",
        "explanation": "The writer states that food composted, fed to animals or disposed "
                       "of outside the regular bin was not captured in the main waste "
                       "totals.",
        "scan_note": "Yontemin kapsam siniri F paragrafinda: F/2 olcumun yalnizca cop "
                     "kutusuna gideni kapsadigini (%82,8), F/3 kompost ve hayvan yemine "
                     "gidenin ana toplamlara girmedigini soyluyor. H/2 kirsalda kompostun "
                     "yayginligini yineliyor; celisen cumle yok.",
        "ne_degisti": "Olculu kip belirteci ('may understate') tasiyan yargi cumlesi yerine, "
                      "ayni kanit cumlesinin duz bildirimsel ilk yarisi soruldu. Eski bicimde "
                      "'may' zaten YES'e isaret ediyordu; yeni bicimde kip belirteci yok, "
                      "dolayisiyla ifadenin kipinden cevap okunamiyor. Kanit cumlesi (F/3) "
                      "degismedi, iddiayi birebir karsiliyor.",
    },
    (GT2, 35): {
        "prompt": "Volunteering may improve a person's health indirectly, by raising the "
                  "income of their household.",
        "difficulty": "hard",
        "explanation": "The writer sets out this indirect route from volunteering through "
                       "household income to health as a plausible explanation, and the "
                       "survey data support the first step of the chain.",
        "scan_note": "Mali aciklama E paragrafinda kuruluyor: E/1 zinciri (gonulluluk -> ag, "
                     "beceri, guvenilirlik -> hane geliri -> saglik), E/2 verinin zincirin "
                     "ilk yarisini destekledigini soyluyor. F payin bestebirin altinda "
                     "kaldigini gosteriyor ama yolun varligini reddetmiyor; G/3 ayni bulguyu "
                     "yineliyor.",
        "ne_degisti": "Soru artik bir fikrin 'akla yatkin olup olmadigini' sormuyor. Eski "
                      "bicim ('is a plausible one') iki yonden siziyordu: 'plausible' sozcugu "
                      "kanit cumlesinden birebir aliniyordu ve akla yatkinlik sorulari "
                      "neredeyse her zaman YES cikar. Yeni bicim, yazarin one surdugu "
                      "dolayli yolun kendisini (gelir uzerinden) soruyor; bunu bilmek icin "
                      "E paragrafini okumak gerekiyor. Kanit cumlesi (E/1) degismedi.",
    },
    (GT2, 36): {
        "prompt": "Income differences appear to account for a little over half of the "
                  "health advantage linked to volunteering.",
        "difficulty": "medium",
        "explanation": "The writer states that the remaining four-fifths of the "
                       "association ran through some other mechanism, leaving income with "
                       "far less than half.",
        "contradiction_point": "F/3, gelirle aciklanamayan kalan bestedortluk payin 'acik "
                               "farkla hikayenin daha buyuk kismi' oldugunu soyluyor; buna "
                               "gore gelirin payi bestebir dolayinda. Ifade bu payi yarinin "
                               "biraz uzerine cikariyor. Celiski tek noktada: gelir payinin "
                               "buyuklugu.",
        "scan_note": "Gelir mekanizmasinin payi E (bagin kurulmasi), F/2 (bestebirin epey "
                     "altinda), F/3 (kalan bestedortlugun baska mekanizmada oldugu) ve G/3'te "
                     "(her analizde payin mutevazi kaldigi) isleniyor.",
        "ne_degisti": "Mutlak oran ifadesi ('explain most of') yerine olculu ve sayisal bir "
                      "iddia ('appear to account for a little over half') kondu. Eski bicim, "
                      "'beklenen aciklama sanildigi kadar guclu cikmadi' anlati kalibiyla "
                      "parcasiz coziluyordu; yeni bicim gercek orani bilmeyi gerektiriyor. "
                      "Kanit cumlesi (F/3) bestedortluk payi verdigi icin yari uzerindeki "
                      "iddiayi da curutuyor.",
    },
}


# --------------------------------------------------------------------------
# 1b) YENIDEN CAPALANAN NOT GIVEN SORULARI
# --------------------------------------------------------------------------
# NOT GIVEN'da kanit cumlesi zaten null; korunan sey yoklugun kendisi (answer ve
# evidence degismiyor). Sizinti ifadenin *ekseninde*: eski ifadeler pasajin hic
# ele almadigi bir boyutu (cinsiyet, yas, politika, deney sonrasi) ekliyordu ve
# bu bicim tek basina NOT GIVEN'i ele veriyordu. Yeni ifadeler pasajin bol bol
# konustugu bir eksende duruyor ama metnin gercekten karara baglamadigi bir
# ayrintiyi soruyor.

DUZELTME.update({
    (PRACTICE, 1): {
        "prompt": "Experienced employees paid a price in their own output for the "
                  "guidance they gave to newcomers.",
        "difficulty": "hard",
        "explanation": "The passage measures what newcomers gained from experienced "
                       "teammates but never reports whether the experienced employees' own "
                       "output suffered as a result.",
        "not_given_justification": "(1) Konu pasajda geciyor: F deneyimli takimlarin yaninda "
                                   "calisanlarin kazancini kidem gruplarina gore veriyor, H/3 "
                                   "deneyimlilerin yeni gelenlere hedefli rehberlik verdigini "
                                   "soyluyor. (2) Pasajda ifadeyi curuten hicbir cumle yok: "
                                   "deneyimli calisanlarin uretkenliginin rehberlikten "
                                   "etkilenmedigini soyleyen bir ifade bulunmuyor, dolayisiyla "
                                   "NO denemez. (3) Pasajda ifadeyi dogrulayan hicbir cumle yok "
                                   "- dolayli olarak bile: G deneyimli calisanlarin dusuk "
                                   "iletisimli ortamlarda daha iyi calistigini soyluyor ama bunu "
                                   "yeni gelenlere rehberlik etmenin bedeliyle hic "
                                   "iliskilendirmiyor; H/4 deneyimli personele daha az kontrol "
                                   "toplantisi onerirken de bir uretkenlik kaybindan soz "
                                   "etmiyor.",
        "scan_note": "Deneyimlilerin rolu F (yeni gelenlerdeki kazanc), G (dusuk iletisimli "
                     "ortamda daha iyi performans) ve H/3-H/4'te (hedefli rehberlik, yonetici "
                     "onerisi) geciyor; hicbir paragraf rehberligin deneyimlinin kendi ciktisina "
                     "maliyetini olcmuyor ya da anmiyor.",
        "ne_degisti": "Ifade artik pasajin hic incelemedigi bir kategoriyle (ofis tabanli "
                      "sirketler) kiyaslama kurmuyor. Eski bicim, tek bir sirketi inceleyen bir "
                      "pasaja disaridan ikinci bir kategori ekledigi icin okunur okunmaz NOT "
                      "GIVEN'a isaret ediyordu. Yeni ifade pasajin merkezindeki eksende "
                      "(deneyimli-yeni calisan dinamigi) duruyor ve metnin gercekten sessiz "
                      "kaldigi bir noktayi soruyor; elemek icin F, G ve H'yi okumak gerekiyor. "
                      "Cevap NOT GIVEN ve evidence null olarak korundu.",
    },
    (PRACTICE, 8): {
        "prompt": "Noise levels in the activity-based design were lower than those in the "
                  "team-office design.",
        "difficulty": "hard",
        "explanation": "The passage compares noise in the open-plan office with the "
                       "alternative designs as a group, but never compares the alternative "
                       "designs with one another.",
        "not_given_justification": "(1) Konu pasajda geciyor: F/1 gurultu olcumlerini veriyor, "
                                   "B dort duzeni tanitirken ses yalitimli kapilari ve ses emici "
                                   "panelleri anlatiyor. (2) Pasajda ifadeyi curuten hicbir cumle "
                                   "yok: etkinlik tabanli duzenin takim ofisinden gurultulu "
                                   "oldugunu soyleyen bir ifade bulunmuyor, dolayisiyla NO "
                                   "denemez. (3) Pasajda ifadeyi dogrulayan hicbir cumle yok - "
                                   "dolayli olarak bile: F/1 yalnizca acik plan ofisi 'alternatif "
                                   "tasarimlarin herhangi biriyle' karsilastiriyor, alternatifleri "
                                   "kendi aralarinda hic siralamiyor; D ve E'deki siralamalar "
                                   "memnuniyet, algilanan verim ve akisa ait, gurultuye degil.",
        "scan_note": "Gurultu verisi yalniz F/1'de (acik planin guvenli siniri asma sikligi, "
                     "alternatiflere gore %20-30 fazla) ve C'de (sensorlerin ses duzeyini "
                     "kaydettigi) geciyor; hicbir paragraf iki alternatif tasarimin gurultusunu "
                     "birbiriyle karsilastirmiyor.",
        "ne_degisti": "Ifade artik 'deneyden sonra ne oldu' turunden bir uygulama ayrintisi "
                      "sormuyor. Eski bicim, sonuclari ve onerileri sunan bir pasaja deney "
                      "sonrasi bir karar ekledigi icin kalip olarak NOT GIVEN'a isaret "
                      "ediyordu. Yeni ifade pasajin olctugu bir degiskenin (gurultu) icinde "
                      "kaliyor; elemek icin F/1'in tam olarak neyi neyle karsilastirdigini "
                      "gormek gerekiyor. Cevap NOT GIVEN ve evidence null olarak korundu.",
    },
    (PRACTICE, 10): {
        "prompt": "The forest's restorative effect built up gradually over the fifteen "
                  "minutes participants spent there.",
        "difficulty": "hard",
        "explanation": "The questionnaires were given only immediately before and "
                       "immediately after each fifteen-minute period, so the passage never "
                       "reports how the effect developed during the stay.",
        "not_given_justification": "(1) Konu pasajda geciyor: F, Restorative Outcome Scale'in "
                                   "calismanin en belirgin etkisi oldugunu ve orman sonrasi "
                                   "keskin bicimde yukseldigini soyluyor. (2) Pasajda ifadeyi "
                                   "curuten hicbir cumle yok: etkinin ani ya da hemen doygunluga "
                                   "ulasan bir etki oldugunu soyleyen bir ifade bulunmuyor, "
                                   "dolayisiyla NO denemez. (3) Pasajda ifadeyi dogrulayan "
                                   "hicbir cumle yok - dolayli olarak bile: E, dort olcegin de "
                                   "yalnizca 15 dakikalik surenin hemen oncesinde ve hemen "
                                   "sonrasinda uygulandigini soyluyor; sure icinde ara olcum "
                                   "alinmadigi icin etkinin nasil bir seyir izledigi hic "
                                   "raporlanmiyor.",
        "scan_note": "Olcum takvimi E'de veriliyor (yalniz oncesi ve sonrasi, kagit anket); "
                     "sonuc F'de (tazeleyicilik puaninda keskin artis) ve G'de (bina kosulunda "
                     "dusme) toplam degisim olarak raporlaniyor. Hicbir paragraf 15 dakika "
                     "icindeki seyri anlatmiyor.",
        "ne_degisti": "Ifade artik pasajin toplulastirilmis olarak verdigi sonuclari cinsiyete "
                      "gore ayristirmiyor. Eski bicim, alt-grup kiyasi ekleyen her ifade gibi "
                      "kalip olarak NOT GIVEN'a isaret ediyordu. Yeni ifade calismanin en "
                      "belirgin bulgusunun (tazeleyicilik) icinde kaliyor ve olcum tasariminin "
                      "ayrintisini (E'deki once/sonra sinirlamasi) bilmeyi gerektiriyor. Cevap "
                      "NOT GIVEN ve evidence null olarak korundu.",
    },
    (PRACTICE, 13): {
        "prompt": "The researchers checked whether the time of day at which the word "
                  "pairs were learned affected recall.",
        "difficulty": "hard",
        "explanation": "The passage gives the exact times of learning and testing in both "
                       "experiments but never says that time of day was itself examined as "
                       "a possible influence on recall.",
        "not_given_justification": "(1) Konu pasajda geciyor: C, birinci deneyde ogrenme ve "
                                   "sinama saatlerini tek tek veriyor (aksam dokuz / sabah "
                                   "dokuz ve tersi), D ikinci deneyde ogrenmenin bir bucukta "
                                   "oldugunu soyluyor. (2) Pasajda ifadeyi curuten hicbir cumle "
                                   "yok: gunun saatinin denetlenmedigini ya da goz ardi "
                                   "edildigini soyleyen bir ifade bulunmuyor, dolayisiyla NO "
                                   "denemez. (3) Pasajda ifadeyi dogrulayan hicbir cumle yok - "
                                   "dolayli olarak bile: F yalnizca sekerleme suresinin ve uyku "
                                   "evrelerinin bellek gelisimiyle iliskisinin sinandigini "
                                   "soyluyor, gunun saatini anmiyor; saatler yalnizca tasarimi "
                                   "anlatmak icin veriliyor, sinanan bir degisken olarak degil.",
        "scan_note": "Saatler C/2-C/3 ve D/2'de tasarim ayrintisi olarak geciyor; sinanan "
                     "degiskenler E (malzeme turu) ve F'de (sekerleme suresi, uyku evreleri) "
                     "sayiliyor. Hicbir paragraf gunun saatini bir analiz degiskeni olarak "
                     "anmiyor.",
        "ne_degisti": "Ifade artik pasajin hic sinamadigi bir yas grubunu (yasli yetiskinler) "
                      "eklemiyor. Eski bicim, tek yas grubuyla calisan bir pasaja capraz-yas "
                      "kiyasi ekledigi icin kalip olarak NOT GIVEN'a isaret ediyordu. Yeni "
                      "ifade pasajin ayrintisiyla verdigi bir tasarim ogesinin (ogrenme ve "
                      "sinama saatleri) uzerine kuruluyor; elemek icin F'deki sinanan degisken "
                      "listesini gormek gerekiyor. Cevap NOT GIVEN ve evidence null olarak "
                      "korundu.",
    },
    (GT1, 36): {
        "prompt": "The 215 households were chosen at random from the two sub-districts.",
        "difficulty": "hard",
        "explanation": "The passage says how many households took part and where they "
                       "were, but never explains how they were selected.",
        "not_given_justification": "(1) Konu pasajda geciyor: A, 215 hanenin 150'sinin "
                                   "Cibinong'da 65'inin Sukajaya'da oldugunu ve bir yil boyunca "
                                   "izlendigini soyluyor. (2) Pasajda ifadeyi curuten hicbir "
                                   "cumle yok: hanelerin gonullulukten, kota ya da baska bir "
                                   "olcutten secildigini soyleyen bir ifade bulunmuyor, "
                                   "dolayisiyla NO denemez. (3) Pasajda ifadeyi dogrulayan "
                                   "hicbir cumle yok - dolayli olarak bile: B yontem "
                                   "ayrintilarini (tartma, icecek gunlugu, gorusmeler) tek tek "
                                   "sayiyor ama orneklemin nasil secildigine hic girmiyor; I/3 "
                                   "yontemin sinirlarini sayarken de sekiz gunluk anlik goruntu "
                                   "ve mevsim sorununu aniyor, secim yontemini degil.",
        "scan_note": "Orneklem bilgisi A/2-A/3'te (215 hane, iki alt bolge, bir yil) ve D'de "
                     "(kentsel-kirsal karsilastirma) geciyor; yontem B'de ve sinirlar I/3'te "
                     "anlatiliyor. Hicbir paragraf hanelerin nasil secildigini soylemiyor.",
        "ne_degisti": "Ifade artik pasajin ayrintili neden listesinde bulunmayan bir neden "
                      "(tarih etiketi karisikligi) one surmuyor. Eski bicim, 'listede olmayan "
                      "neden' kalibi oldugu icin G paragrafini okumadan da NOT GIVEN olarak "
                      "tahmin edilebiliyordu. Yeni ifade pasajin uzun uzun anlattigi yontem "
                      "ekseninde duruyor ve B ile I/3'u okuyup orada olmayan tek seyi fark "
                      "etmeyi gerektiriyor. Cevap NOT GIVEN ve evidence null olarak korundu.",
    },
    (GT2, 33): {
        "prompt": "The health advantage enjoyed by volunteers was largest in the countries "
                  "where volunteering was most common.",
        "difficulty": "hard",
        "explanation": "The passage reports how much volunteering rates varied between "
                       "countries and reports the health advantage for the sample as a "
                       "whole, but never brings the two together.",
        "not_given_justification": "(1) Konu pasajda geciyor: D, gonulluluk oranlarinin ulkeden "
                                   "ulkeye ne kadar degistigini veriyor (Almanya, Hollanda ve "
                                   "Norvec'te onda dorttten fazla; Bulgaristan, Macaristan ve "
                                   "Litvanya'da onda birden az), C ise saglik farkini "
                                   "bildiriyor. (2) Pasajda ifadeyi curuten hicbir cumle yok: "
                                   "saglik avantajinin ulkeler arasinda esit oldugunu ya da ters "
                                   "yonde degistigini soyleyen bir ifade bulunmuyor, dolayisiyla "
                                   "NO denemez. (3) Pasajda ifadeyi dogrulayan hicbir cumle yok "
                                   "- dolayli olarak bile: saglik avantaji butun ornek icin tek "
                                   "bir sayi olarak veriliyor; G'de sayilan dayaniklilik "
                                   "sinamalari (yalniz isgucundekiler, farkli gonulluluk "
                                   "tanimlari, ek kontrol degiskenleri, gelirini bildirmeyenler) "
                                   "arasinda ulkeye gore ayristirma yok.",
        "scan_note": "Ulke farklari D'de, saglik avantaji C'de, dayaniklilik sinamalari G'de "
                     "veriliyor; hicbir paragraf saglik avantajini ulkelerin gonulluluk oranina "
                     "gore ayristirmiyor.",
        "ne_degisti": "Ifade artik yazarin hic dile getirmedigi bir politika yargisi ('daha "
                      "fazla yapilmali') sormuyor. Eski bicim, metin salt durum tespiti "
                      "yaparken 'yazar ne onerir' turunden bir iddia ekledigi icin kalip olarak "
                      "NOT GIVEN'a isaret ediyordu. Yeni ifade pasajin acikca verdigi iki "
                      "bulguyu (ulke farklari ve saglik avantaji) caprazliyor; elemek icin "
                      "C, D ve G'yi okuyup bu caprazlamanin hic yapilmadigini gormek "
                      "gerekiyor. Cevap NOT GIVEN ve evidence null olarak korundu.",
    },
})


# --------------------------------------------------------------------------
# 2) ELENEN SORULAR (konusu genel kultur)
# --------------------------------------------------------------------------

ELEME = {
    (PRACTICE, 2): "Sorunun ekseni genel arastirma yontemi bilgisi: yeni calisanlarin sira "
                   "ya da rastgele usulle takimlara dagitilmasinin nedensellik cikarimini "
                   "guclendirdigi, pasajdan bagimsiz olarak bilinen bir metodoloji kurali. "
                   "Kip dengelemesi ya da konum degisikligi bunu kapatmaz; ifade nasil "
                   "yazilirsa yazilsin cevap yontem bilgisinden cikar.",
    (PRACTICE, 4): "Sorunun ekseni genel is yasami bilgisi: deneyimli calisanlarin yeni "
                   "gelenlere ihtiyac aninda hedefli rehberlik verebildigi, isyeri "
                   "mentorlugu uzerine yaygin kabul goren bir onerme. Ifadenin kipi olculu "
                   "ya da kesin yazilsa da cevap pasaja bakilmadan cikarilabiliyor.",
    (PRACTICE, 5): "Sorunun ekseni genel kultur: acik plan ofislerin yararli mi zararli mi "
                   "oldugunun tartismali olmasi, populer is yasami soyleminin bilinen bir "
                   "gercegi. Tartismanin varligini soran her ifade, kipi ne olursa olsun, "
                   "parcaya bakilmadan dogrulanabilir.",
    (PRACTICE, 9): "Sorunun ekseni genel kultur: dogada vakit gecirmenin stresi azalttigi "
                   "gorusunun yaygin kabul gordugu, pasajdan once bilinen bir sey. Ifade "
                   "zaten 'yaygin kabul' iddiasinin kendisini sordugu icin dogrulanmasi "
                   "pasaja hic bagli degil.",
    (PRACTICE, 12): "Sorunun ekseni cift katmanli genel bilgi: hem 'doganin sakinlestirici "
                    "etkisi kisin da surer' sonucu sezgisel, hem de pilot calisma "
                    "haberlerinin olagan olumlu sonuc kalibi ayni yone isaret ediyor. Kip "
                    "dengelemesi bu iki katmanin ikisini de kapatmiyor.",
    (PRACTICE, 15): "Sorunun ekseni genel uyku bilimi bilgisi: kisa bir sekerlemenin tam bir "
                    "gece uykusunun yerini tutamayacagi populerlesmis bir bulgu. Ifadeyi "
                    "olculu yazmak cevabi degistirmez; okur ifadenin kipinden bagimsiz olarak "
                    "zaten NO bekler.",
    (GT1, 33): "Sorunun ekseni genel arastirma yontemi bilgisi: oz-bildirime dayali "
               "tahminlerin dogrudan olcumden daha guvenilmez oldugu, pasajdan bagimsiz "
               "bilinen bir kural. Ifadedeki 'tend to' kipi kaldirilsa bile cevap ayni "
               "yerden cikar.",
    (GT1, 34): "Sorunun ekseni genel kultur: gida israfi tartismasinda kabuk, kemik ve "
               "yumurta kabugunun 'yenmeyen / onlenemez' kategoride sayilmasi yerlesik bir "
               "siniflandirma. Ifade normatif bicimden ('should be counted') cikarilsa bile "
               "cevap bu yerlesik ayrimdan okunuyor.",
    (GT2, 34): "Sorunun ekseni genel saglik arastirmasi bilgisi: oz-bildirimli sagligin "
               "gelecekteki hastalik ve olumu ongordugu, literaturde cok atif yapilan ve "
               "genel kulturlesmis bir bulgu. Soru ekseni bu bilginin kendisi oldugu icin "
               "mekanik duzeltmeye uygun degil.",
}


# --------------------------------------------------------------------------
# 3) DOKUNULMAYAN SORULAR
# --------------------------------------------------------------------------

DOKUNULMADI = {
    (PRACTICE, 11): "E5/1: Duzeltilemedi, dokunulmadi. Sizinti kanit cumlesinin kendisinde: "
                    "G/1 ('The pattern after the building condition was essentially the "
                    "reverse') kontrol kosulunun tedavi kosulunun tersi sonuc verdigini "
                    "soyluyor. Bu kanita dayanan her NO ifadesi, 'kontrol kosulu tedavi "
                    "kosuluyla ayni sonucu vermez' deney mantigiyla parcasiz cozulebiliyor. "
                    "Ifadeyi olculu yazmak yetmiyor, farkli bir kanit cumlesi gerekiyor - bu "
                    "da gorev kuralina gore yarim duzeltme sayilir. Yuva olduğu gibi birakildi.",
}


def uygula():
    dosyalar = {}
    for yol in (PRACTICE, GT1, GT2):
        tam = os.path.join(KOK, yol)
        dosyalar[yol] = (tam, json.load(open(tam, encoding='utf-8')))

    sayac = {"duzeltildi": 0, "elendi": 0, "dokunulmadi": 0}
    elenen_kayitlari = []

    for yol, (tam, veri) in dosyalar.items():
        for it in veri["items"]:
            anahtar = (yol, it["number"])

            if anahtar in DUZELTME:
                y = DUZELTME[anahtar]
                onceki = it["prompt"]
                it["prompt"] = y["prompt"]
                it["explanation"] = y["explanation"]
                it["difficulty"] = y["difficulty"]
                for alan in ("contradiction_point", "not_given_justification", "scan_note"):
                    if alan in y:
                        it[alan] = y[alan]
                it["status"] = "verified"
                it["blind_solvable"] = None
                it["revision"] = {
                    "tarih": TARIH,
                    "mekanizma": it.get("flag_mechanism"),
                    "onceki_prompt": onceki,
                    "ne_degisti": y["ne_degisti"],
                }
                sayac["duzeltildi"] += 1

            elif anahtar in ELEME:
                it["status"] = "rejected"
                it["reject_reason"] = ELEME[anahtar]
                sayac["elendi"] += 1
                elenen_kayitlari.append({
                    "dosya": yol,
                    "numara": it["number"],
                    "tip": veri["question_type"],
                    "pasaj": it.get("passage_id") or veri.get("passage_id"),
                    "kacinilacak": {
                        "kanit_cumlesi": it.get("evidence"),
                        "ifade": it["prompt"],
                    },
                    "neden_elendi": ELEME[anahtar],
                })

            elif anahtar in DOKUNULMADI:
                it["explanation"] = it["explanation"].rstrip()
                it["review_note"] = DOKUNULMADI[anahtar]
                sayac["dokunulmadi"] += 1

        with open(tam, "w", encoding="utf-8", newline="\n") as f:
            json.dump(veri, f, ensure_ascii=False, indent=2)
            f.write("\n")

    return sayac, elenen_kayitlari


def devir_dosyasi(elenen_kayitlari):
    yol = os.path.join(KOK, "content/DOGRULAMA/yeniden-uretim-listesi.json")
    if os.path.exists(yol):
        veri = json.load(open(yol, encoding='utf-8'))
    else:
        veri = {"elenen": []}

    mevcut = {(e["dosya"], e["numara"]) for e in veri["elenen"]}
    eklenen = 0
    for k in elenen_kayitlari:
        if (k["dosya"], k["numara"]) not in mevcut:
            veri["elenen"].append(k)
            eklenen += 1

    with open(yol, "w", encoding="utf-8", newline="\n") as f:
        json.dump(veri, f, ensure_ascii=False, indent=2)
        f.write("\n")
    return eklenen, len(veri["elenen"])


if __name__ == "__main__":
    sayac, elenenler = uygula()
    eklenen, toplam = devir_dosyasi(elenenler)
    print("duzeltildi  :", sayac["duzeltildi"])
    print("elendi      :", sayac["elendi"])
    print("dokunulmadi :", sayac["dokunulmadi"])
    print("devir dosyasina eklenen:", eklenen, "/ toplam:", toplam)
