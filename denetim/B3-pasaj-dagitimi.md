# B3 — 157 alistirma kaleminin 8 yeni pasaja dagitimi (FAZ 1.3 + 1.4)

Tarih: 2026-08-17. Arac: `tools/b3-dagitim.py` (salt okunur; yalniz `denetim/` altina yazar).

Girdi: `content/reading/practice/*.json` — **157 kalem / 160 soru numarasi / 12 paket** (`denetim/B3-ALISTIRMA-SAYIM.md` ile birebir).

Cikti: 7 akademik (`A13`-`A19`) + 1 General Training (`G07`) metnin **sartnamesi**. Metinler henuz yazilmadi; bu tablo yazimin girdisidir (`denetim/B3-pasaj-dagitimi.json`).

⚠️ `denetim/` altinda iCloud kopyasi var (okunmadi/yazilmadi): DENETIM-RAPORU 2.md, capraz-ozet 2.md, envanter 2.md


## 1. Metin x paket x kalem (capraz tablo)

| metin | SC | NC | SUM | SA | DL | MI | TFNG | YNNG | MC | MH | MF | MSE | kalem | numara | paket |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A13 | 6 |  |  | 2 |  |  | 4 |  | 3 |  | 5 |  | **20** | 21 | 5 |
| A14 | 3 |  |  | 1 |  |  |  | 8 | 3 | 5 |  |  | **20** | 21 | 5 |
| A15 |  | 3 | 4 | 1 |  | 4 |  | 7 |  |  |  |  | **19** | 19 | 5 |
| A16 |  | 3 |  | 1 |  |  | 8 |  | 3 | 5 |  |  | **20** | 21 | 5 |
| A17 | 3 |  |  | 1 |  | 8 | 3 |  | 3 |  |  |  | **18** | 18 | 5 |
| A18 | 3 | 6 |  | 2 |  | 3 |  |  |  | 5 |  |  | **19** | 19 | 5 |
| A19 |  | 3 | 4 | 2 | 10 |  |  |  |  |  |  |  | **19** | 19 | 4 |
| G07 |  |  | 7 |  |  |  |  |  |  |  | 5 | 10 | **22** | 22 | 3 |
| **toplam** | **15** | **15** | **15** | **10** | **10** | **15** | **15** | **15** | **12** | **15** | **10** | **10** | **157** | **160** |  |

Kisaltmalar: **SC** cumle tamamlama · **NC** not tamamlama · **SUM** ozet tamamlama · **SA** kisa cevap · **DL** diyagram etiketleme · **MI** bilgi eslestirme · **TFNG** TRUE/FALSE/NOT GIVEN · **YNNG** YES/NO/NOT GIVEN · **MC** coktan secmeli · **MH** baslik eslestirme · **MF** ozellik eslestirme · **MSE** cumle sonu eslestirme


## 2. Kume kume tasima haritasi

Grup butunlugu korunur: bir kume (paket + eski pasaj) tek bir yeni pasaja gider, bolunmez. Numaralar degismez (`number` sabit) — asagidaki araliklar yeni metinde de ayni.

| yeni metin | tip | paket | eski pasaj | eski group_id | kalem | numara |
|---|---|---|---|---|---|---|
| A13 | SC | sentence-completion.json | A01 | — | 3 | 1-3 |
| A13 | SC | sentence-completion.json | A02 | — | 3 | 4-6 |
| A13 | SA | short-answer.json | A01 | — | 1 | 1 |
| A13 | SA | short-answer.json | A02 | — | 1 | 2 |
| A13 | TFNG | true-false-not-given.json | A02 | — | 4 | 1-4 |
| A13 | MC | multiple-choice.json | A02 | — | 3 | 1-4 |
| A13 | MF | matching-features.json | A10 | P-MF-01 | 5 | 1-5 |
| A14 | SC | sentence-completion.json | A03 | — | 3 | 7-9 |
| A14 | SA | short-answer.json | A03 | — | 1 | 3 |
| A14 | YNNG | yes-no-not-given.json | A06 | — | 4 | 1-4 |
| A14 | YNNG | yes-no-not-given.json | A10 | — | 4 | 5-8 |
| A14 | MC | multiple-choice.json | A05 | — | 3 | 5-8 |
| A14 | MH | matching-headings.json | A01 | P-MH-01 | 5 | 1-5 |
| A15 | NC | note-completion.json | A06 | — | 3 | 1-3 |
| A15 | SUM | summary-completion.json | A10 | — | 4 | 1-4 |
| A15 | SA | short-answer.json | A04 | — | 1 | 4 |
| A15 | MI | matching-information.json | A01 | — | 4 | 1-4 |
| A15 | YNNG | yes-no-not-given.json | A11 | — | 4 | 9-12 |
| A15 | YNNG | yes-no-not-given.json | A12 | — | 3 | 13-15 |
| A16 | NC | note-completion.json | A07 | — | 3 | 4-6 |
| A16 | SA | short-answer.json | A05 | — | 1 | 5 |
| A16 | TFNG | true-false-not-given.json | A05 | — | 4 | 5-8 |
| A16 | TFNG | true-false-not-given.json | A08 | — | 4 | 9-12 |
| A16 | MC | multiple-choice.json | A08 | — | 3 | 9-12 |
| A16 | MH | matching-headings.json | A09 | P-MH-02 | 5 | 6-10 |
| A17 | SC | sentence-completion.json | A04 | — | 3 | 10-12 |
| A17 | SA | short-answer.json | A06 | — | 1 | 6 |
| A17 | MI | matching-information.json | A04 | — | 4 | 5-8 |
| A17 | MI | matching-information.json | A07 | — | 4 | 9-12 |
| A17 | TFNG | true-false-not-given.json | A09 | — | 3 | 13-15 |
| A17 | MC | multiple-choice.json | A11 | — | 3 | 13-15 |
| A18 | SC | sentence-completion.json | A05 | — | 3 | 13-15 |
| A18 | NC | note-completion.json | A08 | — | 3 | 7-9 |
| A18 | NC | note-completion.json | A09 | — | 3 | 10-12 |
| A18 | SA | short-answer.json | A07 | — | 1 | 7 |
| A18 | SA | short-answer.json | A08 | — | 1 | 8 |
| A18 | MI | matching-information.json | A11 | — | 3 | 13-15 |
| A18 | MH | matching-headings.json | A12 | P-MH-03 | 5 | 11-15 |
| A19 | NC | note-completion.json | A12 | — | 3 | 13-15 |
| A19 | SUM | summary-completion.json | A11 | — | 4 | 5-8 |
| A19 | SA | short-answer.json | A09 | — | 1 | 9 |
| A19 | SA | short-answer.json | A12 | — | 1 | 10 |
| A19 | DL | diagram-labelling.json | G01 | — | 3 | 1-3 |
| A19 | DL | diagram-labelling.json | G02 | — | 2 | 4-5 |
| A19 | DL | diagram-labelling.json | G03 | — | 3 | 6-8 |
| A19 | DL | diagram-labelling.json | G04 | — | 2 | 9-10 |
| G07 | SUM | summary-completion.json | G05 | — | 4 | 9-12 |
| G07 | SUM | summary-completion.json | G06 | — | 3 | 13-15 |
| G07 | MF | matching-features.json | G05 | P-MF-02 | 5 | 6-10 |
| G07 | MSE | matching-sentence-endings.json | A07 | P-MSE-01 | 5 | 1-5 |
| G07 | MSE | matching-sentence-endings.json | G06 | P-MSE-02 | 5 | 6-10 |

## 3. Metin metin sartname


### A13 — malzeme muhendisligi / kendi kendini onaran beton

- **Modul:** academic · **kelime:** 800-900 · **paragraf:** en az 8, onerilen 9 (ust sinir 10)
- **Yuk:** 20 kalem / 21 numara, 5 farkli paket (sinir 5) — paragraf basina 2.57 soru (sinir 3)
- **Tasidigi tipler:** cumle tamamlama (SC) 6 kalem, kisa cevap (SA) 2 kalem, TRUE/FALSE/NOT GIVEN (TFNG) 4 kalem, coktan secmeli (MC) 3 kalem, ozellik eslestirme (MF) 5 kalem
- **Konu:** Bakteri tasiyan kapsullerle catlagini kendi kapatan beton karisimlarinin farkli laboratuvarlarda denenmesi; hangi ekip hangi kosulda ne olctu.
- **Kaynak:** PLOS ONE (biyo-beton / self-healing concrete calismalari) · yedek: OpenStax Chemistry (baglayici malzeme bolumu)
- **Konu cakismasi:** en yakin mevcut metin: yok — mevcut 18 metinde muhendislik/malzeme konusu hic yok. Mevcut konularin hicbirine degmiyor (hayvan davranisi, iklim/jeoloji, uzay, tarih/arkeoloji, toplum/is, saglik/davranis disinda yeni bir alan).

**Metnin saglamasi gereken on kosullar:**

- 7-10 harflendirilmis paragraf (en az 8, onerilen 9)  _(prompts/01-pasaj-secimi.md + butce)_
- birbirinden ayri en az 20 kanit cumlesi (her kalem kendi cumlesini alacak)  _(butce (kanit cumlesi basina en cok 1 soru))_
- en az 8 ayri somut sayi/olcu/ad, en az 4 ayri paragrafa dagilmis — hepsi metnin kendi calismasina ozgu (kamuya acik/ezberlenebilir deger yasak)  _(plan 1.2 tablosu (tamamlama ailesi))_
- 3-4 adi gecen arastirmaci/kurum ve toplam 5 ayirt edici iddia (her iddia tek bir ada baglanacak)  _(plan 1.2 tablosu (ozellik eslestirme))_
- en az 4 dogrulanabilir OLGU cumlesi (yazar gorusu degil); NOT GIVEN kalemleri icin metnin sessiz kaldigi komsu noktalar birakilacak  _(turetilmis (butce))_
- 3 ayri odak noktasi; her birinde 4 secenegi ayirt edecek kadar ayrinti (genel kultur yanlis secenege capalanacak)  _(turetilmis (butce))_
- 2 paragraf BASKA hicbir sorunun dokunmadigi hale birakilacak; her birinde 3 kelime veya bir sayiyla cevaplanabilen, calismanin kendi sectigi bir deger  _(plan 1.4)_

**Yeni grup yapisi** (yonerge satiri yeni pasaj kimligini soyleyecek; `passage_id` kalem veya grup duzeyinde yazilacak — `PLAN-EK-kurallar.md` 6):

| onerilen group_id | paket | question_type | kalem | numara | yonerge ilk satiri |
|---|---|---|---|---|---|
| P-SC-A13 | sentence-completion.json | sentence_completion | 6 | 1-6 | `Questions 1-6 refer to Passage A13` |
| P-SA-A13 | short-answer.json | short_answer | 2 | 1-2 | `Questions 1-2 refer to Passage A13` |
| P-TF-A13 | true-false-not-given.json | true_false_not_given | 4 | 1-4 | `Questions 1-4 refer to Passage A13` |
| P-MC-A13 | multiple-choice.json | multiple_choice | 3 | 1-4 | `Questions 1-4 refer to Passage A13` |
| P-MF-A13 | matching-features.json | matching_features | 5 | 1-5 | `Questions 1-5 refer to Passage A13` |

### A14 — bilim pratigi / arastirma verisinin paylasilmamasi

- **Modul:** academic · **kelime:** 800-900 · **paragraf:** en az 8, onerilen 9 (ust sinir 10)
- **Yuk:** 20 kalem / 21 numara, 5 farkli paket (sinir 5) — paragraf basina 2.38 soru (sinir 3)
- **Tasidigi tipler:** cumle tamamlama (SC) 3 kalem, kisa cevap (SA) 1 kalem, YES/NO/NOT GIVEN (YNNG) 8 kalem, coktan secmeli (MC) 3 kalem, baslik eslestirme (MH) 5 kalem
- **Konu:** Arastirmacilarin ham verisini neden paylasmadigi uzerine meta-arastirma; yazarin degerlendirme ve itiraz cumleleri bol.
- **Kaynak:** PLOS ONE (meta-research / data sharing calismalari) · yedek: OpenStax Sociology (arastirma yontemleri bolumu)
- **Konu cakismasi:** en yakin mevcut metin: A06/A10 (toplum-is) — ofis duzeni ve uzaktan calisma. Konu is yeri duzeni degil, bilimsel calismanin kendi pratigi; ofis/uzaktan calisma alt konularina hic girmiyor.

**Metnin saglamasi gereken on kosullar:**

- 7-10 harflendirilmis paragraf (en az 8, onerilen 9)  _(prompts/01-pasaj-secimi.md + butce)_
- birbirinden ayri en az 20 kanit cumlesi (her kalem kendi cumlesini alacak)  _(butce (kanit cumlesi basina en cok 1 soru))_
- 8-10 paragraf ve HER paragrafin ayirt edilebilir tek ana fikri; 5 paragraf baslik sorusuna acik olacak  _(plan 1.2 tablosu (baslik eslestirme))_
- en az 8 yazar gorusu/degerlendirme cumlesi (tablo tabani 4; kalem sayisi 8 oldugu icin cumle basina 1 kural bunu yukseltiyor)  _(plan 1.2 tablosu (YES/NO/NOT GIVEN))_
- en az 4 ayri somut sayi/olcu/ad, en az 4 ayri paragrafa dagilmis — hepsi metnin kendi calismasina ozgu (kamuya acik/ezberlenebilir deger yasak)  _(plan 1.2 tablosu (tamamlama ailesi))_
- 3 ayri odak noktasi; her birinde 4 secenegi ayirt edecek kadar ayrinti (genel kultur yanlis secenege capalanacak)  _(turetilmis (butce))_
- 1 paragraf BASKA hicbir sorunun dokunmadigi hale birakilacak; her birinde 3 kelime veya bir sayiyla cevaplanabilen, calismanin kendi sectigi bir deger  _(plan 1.4)_

**Yeni grup yapisi** (yonerge satiri yeni pasaj kimligini soyleyecek; `passage_id` kalem veya grup duzeyinde yazilacak — `PLAN-EK-kurallar.md` 6):

| onerilen group_id | paket | question_type | kalem | numara | yonerge ilk satiri |
|---|---|---|---|---|---|
| P-SC-A14 | sentence-completion.json | sentence_completion | 3 | 7-9 | `Questions 7-9 refer to Passage A14` |
| P-SA-A14 | short-answer.json | short_answer | 1 | 3 | `Question 3 refers to Passage A14` |
| P-YN-A14 | yes-no-not-given.json | yes_no_not_given | 8 | 1-8 | `Questions 1-8 refer to Passage A14` |
| P-MC-A14 | multiple-choice.json | multiple_choice | 3 | 5-8 | `Questions 5-8 refer to Passage A14` |
| P-MH-A14 | matching-headings.json | matching_headings | 5 | 1-5 | `Questions 1-5 refer to Passage A14` |

### A15 — bitki biyolojisi / bitkilerin kimyasal savunmasi

- **Modul:** academic · **kelime:** 700-900 · **paragraf:** en az 8, onerilen 9 (ust sinir 10)
- **Yuk:** 19 kalem / 19 numara, 5 farkli paket (sinir 5) — paragraf basina 2.25 soru (sinir 3)
- **Tasidigi tipler:** not tamamlama (NC) 3 kalem, ozet tamamlama (SUM) 4 kalem, kisa cevap (SA) 1 kalem, bilgi eslestirme (MI) 4 kalem, YES/NO/NOT GIVEN (YNNG) 7 kalem
- **Konu:** Yaprak zedelendiginde salinan kimyasallarin komsu bitkilerde tepki baslatmasi; olculen degerler ve arastirmacinin yorum cumleleri.
- **Kaynak:** PLOS Biology / PLOS ONE (bitki savunma kimyasi) · yedek: OpenStax Biology (bitki tepkileri bolumu)
- **Konu cakismasi:** en yakin mevcut metin: A01/A02/A07 (doga) — ama ucu de HAYVAN davranisi. Hayvan yok; konu bitki fizyolojisi/kimyasi. Mevcut doga metinlerinin alt konusu (fil, ahtapot, balina davranisi) ile ortusmuyor.

**Metnin saglamasi gereken on kosullar:**

- 7-10 harflendirilmis paragraf (en az 8, onerilen 9)  _(prompts/01-pasaj-secimi.md + butce)_
- birbirinden ayri en az 19 kanit cumlesi (her kalem kendi cumlesini alacak)  _(butce (kanit cumlesi basina en cok 1 soru))_
- en az 7 yazar gorusu/degerlendirme cumlesi (tablo tabani 4; kalem sayisi 7 oldugu icin cumle basina 1 kural bunu yukseltiyor)  _(plan 1.2 tablosu (YES/NO/NOT GIVEN))_
- en az 8 ayri somut sayi/olcu/ad, en az 4 ayri paragrafa dagilmis — hepsi metnin kendi calismasina ozgu (kamuya acik/ezberlenebilir deger yasak)  _(plan 1.2 tablosu (tamamlama ailesi))_
- en az 8 harflendirilmis paragraf ve 4 ayri paragrafta bulunabilir olgu (ayni paragraf iki bilgi sorusuna kaynak olmayacak)  _(turetilmis (butce + bugunku yonerge))_
- 1 paragraf BASKA hicbir sorunun dokunmadigi hale birakilacak; her birinde 3 kelime veya bir sayiyla cevaplanabilen, calismanin kendi sectigi bir deger  _(plan 1.4)_

**Yeni grup yapisi** (yonerge satiri yeni pasaj kimligini soyleyecek; `passage_id` kalem veya grup duzeyinde yazilacak — `PLAN-EK-kurallar.md` 6):

| onerilen group_id | paket | question_type | kalem | numara | yonerge ilk satiri |
|---|---|---|---|---|---|
| P-NC-A15 | note-completion.json | note_completion | 3 | 1-3 | `Questions 1-3 refer to Passage A15` |
| P-SUM-A15 | summary-completion.json | summary_completion | 4 | 1-4 | `Questions 1-4 refer to Passage A15` |
| P-SA-A15 | short-answer.json | short_answer | 1 | 4 | `Question 4 refers to Passage A15` |
| P-MI-A15 | matching-information.json | matching_information | 4 | 1-4 | `Questions 1-4 refer to Passage A15` |
| P-YN-A15 | yes-no-not-given.json | yes_no_not_given | 7 | 9-15 | `Questions 9-15 refer to Passage A15` |

### A16 — spor bilimi / kosu biyomekanigi ve zemin degisimi

- **Modul:** academic · **kelime:** 800-900 · **paragraf:** en az 8, onerilen 9 (ust sinir 10)
- **Yuk:** 20 kalem / 21 numara, 5 farkli paket (sinir 5) — paragraf basina 2.38 soru (sinir 3)
- **Tasidigi tipler:** not tamamlama (NC) 3 kalem, kisa cevap (SA) 1 kalem, TRUE/FALSE/NOT GIVEN (TFNG) 8 kalem, coktan secmeli (MC) 3 kalem, baslik eslestirme (MH) 5 kalem
- **Konu:** Kosucularin zemin sertligi degistiginde adim uzunlugu ve temas suresini nasil degistirdigi; olcum agirlikli olgusal anlatim.
- **Kaynak:** PLOS ONE (kosu biyomekanigi calismalari) · yedek: OpenStax Anatomy & Physiology (hareket sistemi bolumu)
- **Konu cakismasi:** en yakin mevcut metin: A11/A12 (saglik-davranis) — ruh hali ve bellek. Konu ruh hali/bellek degil, olculen hareket mekanigi; psikolojik sonuc iddiasi tasimayacak.

**Metnin saglamasi gereken on kosullar:**

- 7-10 harflendirilmis paragraf (en az 8, onerilen 9)  _(prompts/01-pasaj-secimi.md + butce)_
- birbirinden ayri en az 20 kanit cumlesi (her kalem kendi cumlesini alacak)  _(butce (kanit cumlesi basina en cok 1 soru))_
- 8-10 paragraf ve HER paragrafin ayirt edilebilir tek ana fikri; 5 paragraf baslik sorusuna acik olacak  _(plan 1.2 tablosu (baslik eslestirme))_
- en az 4 ayri somut sayi/olcu/ad, en az 4 ayri paragrafa dagilmis — hepsi metnin kendi calismasina ozgu (kamuya acik/ezberlenebilir deger yasak)  _(plan 1.2 tablosu (tamamlama ailesi))_
- en az 8 dogrulanabilir OLGU cumlesi (yazar gorusu degil); NOT GIVEN kalemleri icin metnin sessiz kaldigi komsu noktalar birakilacak  _(turetilmis (butce))_
- 3 ayri odak noktasi; her birinde 4 secenegi ayirt edecek kadar ayrinti (genel kultur yanlis secenege capalanacak)  _(turetilmis (butce))_
- 1 paragraf BASKA hicbir sorunun dokunmadigi hale birakilacak; her birinde 3 kelime veya bir sayiyla cevaplanabilen, calismanin kendi sectigi bir deger  _(plan 1.4)_

**Yeni grup yapisi** (yonerge satiri yeni pasaj kimligini soyleyecek; `passage_id` kalem veya grup duzeyinde yazilacak — `PLAN-EK-kurallar.md` 6):

| onerilen group_id | paket | question_type | kalem | numara | yonerge ilk satiri |
|---|---|---|---|---|---|
| P-NC-A16 | note-completion.json | note_completion | 3 | 4-6 | `Questions 4-6 refer to Passage A16` |
| P-SA-A16 | short-answer.json | short_answer | 1 | 5 | `Question 5 refers to Passage A16` |
| P-TF-A16 | true-false-not-given.json | true_false_not_given | 8 | 5-12 | `Questions 5-12 refer to Passage A16` |
| P-MC-A16 | multiple-choice.json | multiple_choice | 3 | 9-12 | `Questions 9-12 refer to Passage A16` |
| P-MH-A16 | matching-headings.json | matching_headings | 5 | 6-10 | `Questions 6-10 refer to Passage A16` |

### A17 — mikrobiyoloji / biyofilmlerin yuzeyleri kolonilestirmesi

- **Modul:** academic · **kelime:** 700-900 · **paragraf:** en az 9, onerilen 10 (ust sinir 10)
- **Yuk:** 18 kalem / 18 numara, 5 farkli paket (sinir 5) — paragraf basina 1.89 soru (sinir 3)
- **Tasidigi tipler:** cumle tamamlama (SC) 3 kalem, kisa cevap (SA) 1 kalem, bilgi eslestirme (MI) 8 kalem, TRUE/FALSE/NOT GIVEN (TFNG) 3 kalem, coktan secmeli (MC) 3 kalem
- **Konu:** Yeni bir yuzeyde mikroorganizma tabakasinin asama asama olusmasi; her paragrafta ayri bir bulunabilir olgu.
- **Kaynak:** PLOS ONE (biyofilm olusumu calismalari) · yedek: OpenStax Microbiology
- **Konu cakismasi:** en yakin mevcut metin: yok — mevcut 18 metinde mikrobiyoloji hic yok. Saglik/tedavi iddiasina girmeden mikrobiyal ekoloji anlatiliyor.

**Metnin saglamasi gereken on kosullar:**

- 7-10 harflendirilmis paragraf (en az 9, onerilen 10)  _(prompts/01-pasaj-secimi.md + butce)_
- birbirinden ayri en az 18 kanit cumlesi (her kalem kendi cumlesini alacak)  _(butce (kanit cumlesi basina en cok 1 soru))_
- en az 4 ayri somut sayi/olcu/ad, en az 4 ayri paragrafa dagilmis — hepsi metnin kendi calismasina ozgu (kamuya acik/ezberlenebilir deger yasak)  _(plan 1.2 tablosu (tamamlama ailesi))_
- en az 3 dogrulanabilir OLGU cumlesi (yazar gorusu degil); NOT GIVEN kalemleri icin metnin sessiz kaldigi komsu noktalar birakilacak  _(turetilmis (butce))_
- en az 8 harflendirilmis paragraf ve 8 ayri paragrafta bulunabilir olgu (ayni paragraf iki bilgi sorusuna kaynak olmayacak)  _(turetilmis (butce + bugunku yonerge))_
- 3 ayri odak noktasi; her birinde 4 secenegi ayirt edecek kadar ayrinti (genel kultur yanlis secenege capalanacak)  _(turetilmis (butce))_
- 1 paragraf BASKA hicbir sorunun dokunmadigi hale birakilacak; her birinde 3 kelime veya bir sayiyla cevaplanabilen, calismanin kendi sectigi bir deger  _(plan 1.4)_

**Yeni grup yapisi** (yonerge satiri yeni pasaj kimligini soyleyecek; `passage_id` kalem veya grup duzeyinde yazilacak — `PLAN-EK-kurallar.md` 6):

| onerilen group_id | paket | question_type | kalem | numara | yonerge ilk satiri |
|---|---|---|---|---|---|
| P-SC-A17 | sentence-completion.json | sentence_completion | 3 | 10-12 | `Questions 10-12 refer to Passage A17` |
| P-SA-A17 | short-answer.json | short_answer | 1 | 6 | `Question 6 refers to Passage A17` |
| P-MI-A17 | matching-information.json | matching_information | 8 | 5-12 | `Questions 5-12 refer to Passage A17` |
| P-TF-A17 | true-false-not-given.json | true_false_not_given | 3 | 13-15 | `Questions 13-15 refer to Passage A17` |
| P-MC-A17 | multiple-choice.json | multiple_choice | 3 | 13-15 | `Questions 13-15 refer to Passage A17` |

### A18 — genetik yontem / DNA barkodlamayla tur tanimlama

- **Modul:** academic · **kelime:** 700-900 · **paragraf:** en az 8, onerilen 9 (ust sinir 10)
- **Yuk:** 19 kalem / 19 numara, 5 farkli paket (sinir 5) — paragraf basina 2.43 soru (sinir 3)
- **Tasidigi tipler:** cumle tamamlama (SC) 3 kalem, not tamamlama (NC) 6 kalem, kisa cevap (SA) 2 kalem, bilgi eslestirme (MI) 3 kalem, baslik eslestirme (MH) 5 kalem
- **Konu:** Kucuk bir gen parcasindan tur tanimlama yonteminin nasil kuruldugu ve nerede yaniltici oldugu; somut deger ve ad yogun.
- **Kaynak:** PLOS ONE (DNA barcoding calismalari) · yedek: OpenStax Biology (biyoteknoloji bolumu)
- **Konu cakismasi:** en yakin mevcut metin: A01/A02/A07 (doga) — hayvan davranisi. Davranis anlatmiyor; laboratuvar yontemi ve yontemin sinirlari anlatiliyor.

**Metnin saglamasi gereken on kosullar:**

- 7-10 harflendirilmis paragraf (en az 8, onerilen 9)  _(prompts/01-pasaj-secimi.md + butce)_
- birbirinden ayri en az 19 kanit cumlesi (her kalem kendi cumlesini alacak)  _(butce (kanit cumlesi basina en cok 1 soru))_
- 8-10 paragraf ve HER paragrafin ayirt edilebilir tek ana fikri; 5 paragraf baslik sorusuna acik olacak  _(plan 1.2 tablosu (baslik eslestirme))_
- en az 11 ayri somut sayi/olcu/ad, en az 4 ayri paragrafa dagilmis — hepsi metnin kendi calismasina ozgu (kamuya acik/ezberlenebilir deger yasak)  _(plan 1.2 tablosu (tamamlama ailesi))_
- en az 8 harflendirilmis paragraf ve 3 ayri paragrafta bulunabilir olgu (ayni paragraf iki bilgi sorusuna kaynak olmayacak)  _(turetilmis (butce + bugunku yonerge))_
- 2 paragraf BASKA hicbir sorunun dokunmadigi hale birakilacak; her birinde 3 kelime veya bir sayiyla cevaplanabilen, calismanin kendi sectigi bir deger  _(plan 1.4)_

**Yeni grup yapisi** (yonerge satiri yeni pasaj kimligini soyleyecek; `passage_id` kalem veya grup duzeyinde yazilacak — `PLAN-EK-kurallar.md` 6):

| onerilen group_id | paket | question_type | kalem | numara | yonerge ilk satiri |
|---|---|---|---|---|---|
| P-SC-A18 | sentence-completion.json | sentence_completion | 3 | 13-15 | `Questions 13-15 refer to Passage A18` |
| P-NC-A18 | note-completion.json | note_completion | 6 | 7-12 | `Questions 7-12 refer to Passage A18` |
| P-SA-A18 | short-answer.json | short_answer | 2 | 7-8 | `Questions 7-8 refer to Passage A18` |
| P-MI-A18 | matching-information.json | matching_information | 3 | 13-15 | `Questions 13-15 refer to Passage A18` |
| P-MH-A18 | matching-headings.json | matching_headings | 5 | 11-15 | `Questions 11-15 refer to Passage A18` |

### A19 — su teknolojisi / gunes enerjili damitma duzenegi (SUREC METNI)

- **Modul:** academic · **kelime:** 700-900 · **paragraf:** en az 8, onerilen 9 (ust sinir 10)
- **Yuk:** 19 kalem / 19 numara, 4 farkli paket (sinir 5) — paragraf basina 2.43 soru (sinir 3)
- **Tasidigi tipler:** not tamamlama (NC) 3 kalem, ozet tamamlama (SUM) 4 kalem, kisa cevap (SA) 2 kalem, diyagram etiketleme (DL) 10 kalem
- **Konu:** Tuzlu suyun gunesle buharlastirilip yogusturuldugu duzenegin asamalari; cizilebilir duzenek — diyagram etiketlemenin 10 kalemi buraya.
- **Kaynak:** PLOS ONE (gunes damitma / solar still calismalari) · yedek: OpenStax Chemistry (faz degisimi bolumu) · USGS su bilimi sayfalari
- **Konu cakismasi:** en yakin mevcut metin: A03/A08 (iklim-jeoloji-okyanus). Iklim/jeoloji olgusu degil, insan yapimi bir duzenegin isleyisi; deniz/okyanus surec anlatimina girmeyecek.

**Metnin saglamasi gereken on kosullar:**

- 7-10 harflendirilmis paragraf (en az 8, onerilen 9)  _(prompts/01-pasaj-secimi.md + butce)_
- birbirinden ayri en az 19 kanit cumlesi (her kalem kendi cumlesini alacak)  _(butce (kanit cumlesi basina en cok 1 soru))_
- en az 19 ayri somut sayi/olcu/ad, en az 7 ayri paragrafa dagilmis — hepsi metnin kendi calismasina ozgu (kamuya acik/ezberlenebilir deger yasak)  _(plan 1.2 tablosu (tamamlama ailesi))_
- cizilebilir tek bir surec/duzenek anlatimi; en az 10 etiketlenebilir bilesen/asama, sirasi metinden izlenebilir  _(plan 1.2 tablosu (diyagram etiketleme))_
- 2 paragraf BASKA hicbir sorunun dokunmadigi hale birakilacak; her birinde 3 kelime veya bir sayiyla cevaplanabilen, calismanin kendi sectigi bir deger  _(plan 1.4)_

**Yeni grup yapisi** (yonerge satiri yeni pasaj kimligini soyleyecek; `passage_id` kalem veya grup duzeyinde yazilacak — `PLAN-EK-kurallar.md` 6):

| onerilen group_id | paket | question_type | kalem | numara | yonerge ilk satiri |
|---|---|---|---|---|---|
| P-NC-A19 | note-completion.json | note_completion | 3 | 13-15 | `Questions 13-15 refer to Passage A19` |
| P-SUM-A19 | summary-completion.json | summary_completion | 4 | 5-8 | `Questions 5-8 refer to Passage A19` |
| P-SA-A19 | short-answer.json | short_answer | 2 | 9-10 | `Questions 9-10 refer to Passage A19` |
| P-DL-A19 | diagram-labelling.json | diagram_labelling | 10 | 1-10 | `Questions 1-10 refer to Passage A19` |

### G07 — ev bitkileri ve ic hava kalitesi (GT 3. bolum, uzun genel ilgi metni)

- **Modul:** general (bolum 3) · **kelime:** 850-900 · **paragraf:** en az 8, onerilen 10 (ust sinir 10)
- **Yuk:** 22 kalem / 22 numara, 3 farkli paket (sinir 5) — paragraf basina 2.20 soru (sinir 3)
- **Tasidigi tipler:** ozet tamamlama (SUM) 7 kalem, ozellik eslestirme (MF) 5 kalem, cumle sonu eslestirme (MSE) 10 kalem
- **Konu:** Evlerdeki bitkilerin ic hava olcumlerine etkisi uzerine birbiriyle cekisen ekipler; neden-sonuc ve karsitlik cumlesi yogun anlati.
- **Kaynak:** PLOS ONE (ic mekan bitkileri / hava kalitesi calismalari) · yedek: OpenStax Biology (bitki fizyolojisi) — anlatim sadelestirilerek
- **Konu cakismasi:** en yakin mevcut metin: G05 (gida israfi), G06 (gonulluluk) — ikisi de GT 3. bolum. Tuketim davranisi ve gonullu calisma alt konularina girmiyor; olcum agirlikli ev ici hava konusu. (prompts/01-pasaj-secimi.md'nin GT 3. bolum ornek listesinde zaten geciyor.)

**Metnin saglamasi gereken on kosullar:**

- 7-10 harflendirilmis paragraf (en az 8, onerilen 10)  _(prompts/01-pasaj-secimi.md + butce)_
- birbirinden ayri en az 22 kanit cumlesi (her kalem kendi cumlesini alacak)  _(butce (kanit cumlesi basina en cok 1 soru))_
- en az 7 ayri somut sayi/olcu/ad, en az 4 ayri paragrafa dagilmis — hepsi metnin kendi calismasina ozgu (kamuya acik/ezberlenebilir deger yasak)  _(plan 1.2 tablosu (tamamlama ailesi))_
- 3-4 adi gecen arastirmaci/kurum ve toplam 5 ayirt edici iddia (her iddia tek bir ada baglanacak)  _(plan 1.2 tablosu (ozellik eslestirme))_
- en az 10 neden-sonuc/karsitlik cumlesi (tablo tabani 5; iki grup tasindigi icin kalem sayisi belirleyici) — E7 recetesi burada uygulanacak  _(plan 1.2 tablosu (cumle sonu eslestirme))_

**Yeni grup yapisi** (yonerge satiri yeni pasaj kimligini soyleyecek; `passage_id` kalem veya grup duzeyinde yazilacak — `PLAN-EK-kurallar.md` 6):

| onerilen group_id | paket | question_type | kalem | numara | yonerge ilk satiri |
|---|---|---|---|---|---|
| P-SUM-G07 | summary-completion.json | summary_completion | 7 | 9-15 | `Questions 9-15 refer to Passage G07` |
| P-MF-G07 | matching-features.json | matching_features | 5 | 6-10 | `Questions 6-10 refer to Passage G07` |
| P-MSE-G07 | matching-sentence-endings.json | matching_sentence_endings | 10 | 1-10 | `Questions 1-10 refer to Passage G07` |

## 4. Butce dogrulamasi

Kurallar: metin basina en cok **5 farkli paket** (sert), hedef **~20 kalem** (yumusak), **paragraf basina en cok 3 soru**, **kanit cumlesi basina en cok 1 soru**, kisa cevabin her kalemi **dokunulmamis** bir paragraf tuketir.

| metin | kalem | kalem <= 20 | paket | paket <= 5 | paragraf en az/onerilen | paragraf basi soru | yogunluk | kisa cevap (serbest paragraf) | gereken ayri kanit cumlesi |
|---|---|---|---|---|---|---|---|---|---|
| A13 | 20 | OK | 5 | OK | 8/9 | 2.57 | OK | 2 | 20 |
| A14 | 20 | OK | 5 | OK | 8/9 | 2.38 | OK | 1 | 20 |
| A15 | 19 | OK | 5 | OK | 8/9 | 2.25 | OK | 1 | 19 |
| A16 | 20 | OK | 5 | OK | 8/9 | 2.38 | OK | 1 | 20 |
| A17 | 18 | OK | 5 | OK | 9/10 | 1.89 | OK | 1 | 18 |
| A18 | 19 | OK | 5 | OK | 8/9 | 2.43 | OK | 2 | 19 |
| A19 | 19 | OK | 4 | OK | 8/9 | 2.43 | OK | 2 | 19 |
| G07 | 22 | ⚠️ 22 | 3 | OK | 8/10 | 2.20 | OK | 0 | 22 |

### Korunum

| olcu | kaynak | hedef | durum |
|---|---|---|---|
| kalem | 157 | 157 | OK |
| soru numarasi | 160 | 160 | OK |

| paket | kaynak kalem | hedef kalem | durum |
|---|---|---|---|
| cumle tamamlama (SC) | 15 | 15 | OK |
| not tamamlama (NC) | 15 | 15 | OK |
| ozet tamamlama (SUM) | 15 | 15 | OK |
| kisa cevap (SA) | 10 | 10 | OK |
| diyagram etiketleme (DL) | 10 | 10 | OK |
| bilgi eslestirme (MI) | 15 | 15 | OK |
| TRUE/FALSE/NOT GIVEN (TFNG) | 15 | 15 | OK |
| YES/NO/NOT GIVEN (YNNG) | 15 | 15 | OK |
| coktan secmeli (MC) | 12 | 12 | OK |
| baslik eslestirme (MH) | 15 | 15 | OK |
| ozellik eslestirme (MF) | 10 | 10 | OK |
| cumle sonu eslestirme (MSE) | 10 | 10 | OK |

### Hatalar / uyarilar

- Sert kural ihlali **yok** (kume ortusmesi, sayim korunumu, paket cesidi, paragraf butcesi, kisa cevap duzeni, bagli kararlar).

- ⚠️ A13: 21 soru numarasi (kalem 20) — cift cevapli coktan secmeli kalem numarayi kalemden fazla gosteriyor; cevap kagidinda 21 satir
- ⚠️ A14: 21 soru numarasi (kalem 20) — cift cevapli coktan secmeli kalem numarayi kalemden fazla gosteriyor; cevap kagidinda 21 satir
- ⚠️ A16: 21 soru numarasi (kalem 20) — cift cevapli coktan secmeli kalem numarayi kalemden fazla gosteriyor; cevap kagidinda 21 satir
- ⚠️ G07: 22 kalem — metin basina hedef ~20 asildi (paragraf butcesi hala tutuyor: 10 paragrafta paragraf basina 2.20 soru)

### Sikisan noktalar (kural ihlali degil, yazimda pay yok)

| metin | sikisiklik |
|---|---|
| A13 | paragraf basina 2.57 soru — 3'luk tavana yakin |
| A17 | paragraf sayisi ust sinirda (10) — metin kisaltilirsa butce bozulur |
| A17 | ayri paragraf isteyen kalemler (baslik/bilgi eslestirme + kisa cevap) 9 paragraf tutuyor, metinde 10 paragraf var — yedek paragraf yok |
| G07 | 22 kalem — metin basina hedef ~20 asiliyor; yuk ancak 10 paragrafla tasiniyor |
| G07 | paragraf sayisi ust sinirda (10) — metin kisaltilirsa butce bozulur |

## 5. Konu onerileri ve izinli kaynak

Mevcut 18 metnin konulari (plan 1.2/1 yasak listesi): hayvan davranisi x3, iklim/jeoloji/okyanus x2, uzay x1, tarih/arkeoloji x2, toplum/is x2, saglik/davranis x2; GT: sehir hizmetleri, bos zaman, personel el kitabi, staj, gida israfi, gonulluluk. Asagidaki onerilerin hicbiri bu alt konulara degmiyor.

| metin | onerilen alan | izinli kaynak | yedek kaynak | en yakin mevcut metin | ayrim |
|---|---|---|---|---|---|
| A13 | malzeme muhendisligi / kendi kendini onaran beton | PLOS ONE (biyo-beton / self-healing concrete calismalari) | OpenStax Chemistry (baglayici malzeme bolumu) | yok — mevcut 18 metinde muhendislik/malzeme konusu hic yok | Mevcut konularin hicbirine degmiyor (hayvan davranisi, iklim/jeoloji, uzay, tarih/arkeoloji, toplum/is, saglik/davranis disinda yeni bir alan). |
| A14 | bilim pratigi / arastirma verisinin paylasilmamasi | PLOS ONE (meta-research / data sharing calismalari) | OpenStax Sociology (arastirma yontemleri bolumu) | A06/A10 (toplum-is) — ofis duzeni ve uzaktan calisma | Konu is yeri duzeni degil, bilimsel calismanin kendi pratigi; ofis/uzaktan calisma alt konularina hic girmiyor. |
| A15 | bitki biyolojisi / bitkilerin kimyasal savunmasi | PLOS Biology / PLOS ONE (bitki savunma kimyasi) | OpenStax Biology (bitki tepkileri bolumu) | A01/A02/A07 (doga) — ama ucu de HAYVAN davranisi | Hayvan yok; konu bitki fizyolojisi/kimyasi. Mevcut doga metinlerinin alt konusu (fil, ahtapot, balina davranisi) ile ortusmuyor. |
| A16 | spor bilimi / kosu biyomekanigi ve zemin degisimi | PLOS ONE (kosu biyomekanigi calismalari) | OpenStax Anatomy & Physiology (hareket sistemi bolumu) | A11/A12 (saglik-davranis) — ruh hali ve bellek | Konu ruh hali/bellek degil, olculen hareket mekanigi; psikolojik sonuc iddiasi tasimayacak. |
| A17 | mikrobiyoloji / biyofilmlerin yuzeyleri kolonilestirmesi | PLOS ONE (biyofilm olusumu calismalari) | OpenStax Microbiology | yok — mevcut 18 metinde mikrobiyoloji hic yok | Saglik/tedavi iddiasina girmeden mikrobiyal ekoloji anlatiliyor. |
| A18 | genetik yontem / DNA barkodlamayla tur tanimlama | PLOS ONE (DNA barcoding calismalari) | OpenStax Biology (biyoteknoloji bolumu) | A01/A02/A07 (doga) — hayvan davranisi | Davranis anlatmiyor; laboratuvar yontemi ve yontemin sinirlari anlatiliyor. |
| A19 | su teknolojisi / gunes enerjili damitma duzenegi (SUREC METNI) | PLOS ONE (gunes damitma / solar still calismalari) | OpenStax Chemistry (faz degisimi bolumu) · USGS su bilimi sayfalari | A03/A08 (iklim-jeoloji-okyanus) | Iklim/jeoloji olgusu degil, insan yapimi bir duzenegin isleyisi; deniz/okyanus surec anlatimina girmeyecek. |
| G07 | ev bitkileri ve ic hava kalitesi (GT 3. bolum, uzun genel ilgi metni) | PLOS ONE (ic mekan bitkileri / hava kalitesi calismalari) | OpenStax Biology (bitki fizyolojisi) — anlatim sadelestirilerek | G05 (gida israfi), G06 (gonulluluk) — ikisi de GT 3. bolum | Tuketim davranisi ve gonullu calisma alt konularina girmiyor; olcum agirlikli ev ici hava konusu. (prompts/01-pasaj-secimi.md'nin GT 3. bolum ornek listesinde zaten geciyor.) |

Kaynak kurali (`prompts/01-pasaj-secimi.md`): yalniz **PLOS · NASA/NOAA/USGS · OpenStax**; CC BY / kamu mali; Wikipedia ve The Conversation yasak. Somut sayilar metnin kendi calismasinin sectigi degerler olacak (`PLAN-EK-kurallar.md` 4).


## 6. Yontem ve sinirlar

- "Kume" = (paket dosyasi, eski `passage_id`). Duz `items` tasiyan 9 pakette grup alani yok; kume, ayni pasaja capali kalemlerin olusturdugu ortuk gruptur.
- Paragraf sayilari **tahmin degil turetim**: yogunluk (paragraf basina en cok 3 soru) + kisa cevabin tukettigi dokunulmamis paragraflar + baslik/bilgi eslestirmenin ayri paragraf ihtiyaci + 7-10 paragraf tabani.
- Kanit cumlesi sayisi kalem sayisina esit alindi (cumle basina en cok 1 soru); 700-900 kelimelik bir metinde ~40-50 cumle olur, en agir metin bunun ~49%'ini kullanir.
- Numaralar (`number`) degismiyor; bu yuzden bir metne dusen kumelerin numaralari bitisik olacak sekilde secildi — paket dosyasi icinde kalem sirasi bozulmuyor.
- Arac hicbir icerik dosyasini degistirmedi; `content/` altina yazmiyor.
