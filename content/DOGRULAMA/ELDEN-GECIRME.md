# İşaretli soruları elden geçirme — mekanizma bazında düzeltme

Kaynak talimat: `prompts/OPUS5-E5-isaretli-elden-gecirme.md` (8 çalıştırma).
Bu dosya her çalıştırmada bir bölüm kazanır.

Girdi raporları: `ISARET-GEREKCELERI.md` (E1 — mekanizma etiketleri),
`ANLAM-DUZEYI-RAPOR.md` (E10 — anlam düzeyinde ek işaretliler),
`kalibrasyon/desen/*` (E4), `denetim/capraz-ozet.md` §4.

---

## 1. çalıştırma — YES/NO/NOT GIVEN, kip imzası · 2026-08-08

### Kapsam ve kendi sayımım

Talimatın 1. kuralı gereği sayıya güvenmeyip yeniden saydım. `content/` altında
`question_type: "yes_no_not_given"` taşıyan üç dosya var ve içlerindeki
`status: "flagged"` soru sayısı **23**:

| Dosya | Soru | İşaretli |
|---|---|---|
| `content/reading/practice/yes-no-not-given.json` | 15 | 15 |
| `content/reading/tests/GT1/yes-no-not-given.json` | 4 | 4 |
| `content/reading/tests/GT2/yes-no-not-given.json` | 4 | 4 |
| **toplam** | **23** | **23** |

E1'in dağılım tablosundaki 23 sayısıyla birebir aynı. E10 bu tipe hiç dokunmadı
(üç çalıştırması da tamamlama ailesindeydi), dolayısıyla bu tipte ek işaretli yok.

Tipin tamamı işaretli, çünkü `OPUS5-B1` ölçümünde **23/23 (%100)** parçasız bilindi —
ürünün en yüksek sızıntı oranı bu tipte (`UYARILAR.txt`, 07.08.2026 kaydı).

### Önce: kip imzası gerçekten var mı?

23 ifadeyi cevaplarına göre değil, **yazılış kipine** göre sınıflandırdım:

| Kip | YES (10) | NO (7) | NOT GIVEN (6) |
|---|---|---|---|
| mutlak / eşdeğerlik / üstünlük / normatif | 0 | **7** | 0 |
| ölçülü (can, may, tend to, plausible…) | 5 | 0 | 0 |
| yalın | 5 | 0 | 0 |
| eksen dışı boyut ekliyor | 0 | 0 | **6** |

Üç satırlık bir kural çıkıyor:

> mutlak yazılmışsa → NO · pasajın eksenine yeni bir boyut ekliyorsa → NOT GIVEN ·
> geri kalan → YES

Bu kural 23 sorunun **23'ünü** doğru bilir. B1'in ölçtüğü %100 tam olarak bu.
İki alt imza ayrı ayrı da kusursuz ayırıyordu:

- **Yedi NO'nun yedisi** bir mutlaklık taşıyordu: `clearly`, `failed to produce`,
  `made no difference`, `in much the same way`, `as well as`, `should be counted`,
  `most`. Hiçbir YES ifadesinde mutlaklık yoktu.
- **Altı NOT GIVEN'ın altısı** pasajın hiç ele almadığı bir *boyut* ekliyordu:
  cinsiyet kırılımı (10), yaş kırılımı (13), incelenmemiş bir şirket kategorisi (1),
  deneyden sonra ne olduğu (8), listede geçmeyen bir neden (GT1-36), yazarın hiç
  dile getirmediği bir politika yargısı (GT2-33). Soruyu okumak yetiyordu; pasaja
  bakmaya gerek yoktu.

### Sonuç dağılımı

| Sonuç | Soru | Numaralar |
|---|---|---|
| **Düzeltildi** | 13 | practice 1, 3, 6, 7, 8, 10, 13, 14 · GT1 35, 36 · GT2 33, 35, 36 |
| **Elendi** | 9 | practice 2, 4, 5, 9, 12, 15 · GT1 33, 34 · GT2 34 |
| **Dokunulmadı** | 1 | practice 11 |
| **toplam** | **23** | |

Elenen 9 sorunun tamamı E1'in `genel_kultur` etiketlediği sorular; elenen ile
`genel_kultur` kümesi bu tipte birebir örtüşüyor.

### Düzeltmenin iki yönü

Kip imzasını kırmak için tek yön yetmiyor. İfadeleri yalnız yumuşatsaydım
"ölçülü = YES" imzası yerine "ölçülü = NO" imzası kurardım — aynı sızıntının
tersi. Bu yüzden iki yönde birden çalıştım:

**a) Mutlak yazılmış NO'lar ölçülü kipe çekildi** (4 soru)

| Soru | Eski | Yeni |
|---|---|---|
| practice-3 | "star performers **clearly** improved…" | "…**tended to** produce **a little** more than they otherwise would" |
| practice-14 | "made **no difference** to how well it was recalled" | "**seems to have mattered little** to how well they were later recalled" |
| GT2-36 | "explain **most** of the health advantage" | "**appear to** account for **a little over half** of the health advantage" |
| practice-6 | "**failed to produce** a clear ordering" | "were able to rank **only two of the four** designs against each other" |

Dördü de hâlâ NO, çünkü kanıt cümleleri aynı kaldı ve ölçülü iddiayı da aynı
netlikte çürütüyor: practice-3'ün kanıtı faydanın "burada hiç görülmediğini"
söylüyor, dolayısıyla küçük bir artışı da dışlıyor.

**b) Bir YES mutlak kipe çekildi** (1 soru)

| Soru | Eski | Yeni |
|---|---|---|
| practice-7 | "came more easily … than the remaining designs" | "outscored **every other design in the trial**" |

Kanıt cümlesi (E/2) iki yarı kapalı düzenin hem tamamen açık hem de sabit masasız
düzenden üstün olduğunu söylüyor; denenen dört düzenden geri kalan ikisi zaten
tam olarak bunlar, dolayısıyla kapsayıcı ifade doğru. Artık sette **mutlak yazılmış
bir YES** var, yani "mutlak = NO" kuralı yanlış cevap veriyor.

**c) Kanıttan sözcük kaldıran düzeltmeler** (2 soru)

| Soru | Eski | Yeni |
|---|---|---|
| GT1-35 | "**may** understate the true extent of food loss" | "Food that households composted or gave to animals **was left out of** the study's main waste totals" |
| GT2-35 | "The idea … **is a plausible one**" | "Volunteering **may** improve health **indirectly, by raising** household income" |

GT2-35 iki yönden sızdırıyordu: `plausible` sözcüğü kanıt cümlesinden birebir
alınmıştı ve "bu fikir akla yatkın mı?" biçimindeki sorular neredeyse her zaman
YES çıkar. Yeni ifade yazarın kurduğu dolaylı yolun kendisini soruyor.

### NOT GIVEN'ların yeniden çapalanması (6 soru)

NOT GIVEN'da korunacak kanıt cümlesi yok — `evidence` zaten `null` ve öyle kaldı;
korunan şey **yokluğun kendisi**, yani cevabın NOT GIVEN olması. Sızıntı ifadenin
*ekseninde*ydi: hepsi pasajın hiç konuşmadığı bir boyut ekliyordu ve bu biçim tek
başına cevabı ele veriyordu. Altısını da pasajın bol bol konuştuğu bir eksene
taşıdım; artık metnin gerçekten karara bağlamadığı bir ayrıntıyı soruyorlar.

| Soru | Eski eksen dışı boyut | Yeni çapa |
|---|---|---|
| practice-1 | incelenmemiş bir şirket kategorisiyle kıyas (ofisli şirketler) | deneyimlilerin rehberlik için kendi çıktısından ödün verip vermediği — F/G/H konuyu işliyor, maliyeti hiç ölçmüyor |
| practice-8 | deneyden sonra hangi düzenin kurulduğu | etkinlik tabanlı ile takım ofisinin gürültüsü — F/1 yalnız açık planı alternatiflerle karşılaştırıyor, alternatifleri kendi aralarında hiç sıralamıyor |
| practice-10 | cinsiyet kırılımı | tazeleyici etkinin 15 dakika içinde nasıl seyrettiği — E, anketlerin yalnız hemen önce ve hemen sonra uygulandığını söylüyor |
| practice-13 | yaş kırılımı (yaşlı yetişkinler) | günün saatinin sınanıp sınanmadığı — C ve D saatleri ayrıntısıyla veriyor, F sınanan değişkenleri sayıyor ve saat yok |
| GT1-36 | neden listesinde geçmeyen bir neden (tarih etiketi) | 215 hanenin nasıl seçildiği — B yöntemi tek tek anlatıyor, seçim yöntemine hiç girmiyor |
| GT2-33 | yazarın hiç dile getirmediği politika yargısı | sağlık avantajının gönüllülük oranı yüksek ülkelerde daha büyük olup olmadığı — D ülke farklarını, C avantajı veriyor, ikisi hiç çaprazlanmıyor |

Altısında da `answer` NOT GIVEN ve `evidence` `null` olarak korundu; yeniden
yazılan alanlar `prompt`, `not_given_justification`, `scan_note`, `explanation`.

### Elenen 9 soru

Hepsinin ortak yanı, sorunun **ekseninin kendisinin** genel kültür olması: ifade
nasıl yazılırsa yazılsın cevap pasajdan değil dünya bilgisinden çıkıyor. Kip
dengelemesi bunu kapatmaz, o yüzden mekanik düzeltmeye uygun değiller.

| Soru | Cevap | Eksen |
|---|---|---|
| practice-2 | YES | rastgele/sıra usulü atama nedensellik çıkarımını güçlendirir (metodoloji kuralı) |
| practice-4 | YES | deneyimli çalışan yeni gelene rehberlik eder (işyeri mentorluğu) |
| practice-5 | YES | açık plan ofis tartışmalı bir konudur (popüler iş yaşamı söylemi) |
| practice-9 | YES | doğa stresi azaltır görüşü yaygın kabul görür |
| practice-12 | YES | doğanın etkisi kışın da sürer + pilot çalışma haberleri olumlu sonuçla çıkar |
| practice-15 | NO | şekerleme gece uykusunun yerini tutmaz (popüler uyku bilimi) |
| GT1-33 | YES | öz-bildirim doğrudan ölçümden güvenilmezdir (metodoloji kuralı) |
| GT1-34 | NO | kabuk/kemik "önlenemez" kategoride sayılır (gıda israfı sınıflandırması) |
| GT2-34 | YES | öz-bildirimli sağlık ölümü öngörür (çok atıf yapılan literatür bulgusu) |

Dokuzu da `status: "rejected"` + `reject_reason` aldı, dosyalarında **numaralarıyla
duruyor** ve `content/DOGRULAMA/yeniden-uretim-listesi.json` dosyasına eklendi.
Her kayıt, o pasajda zaten soru sorulmuş kanıt cümlesini `kacinilacak` altında
taşıyor, böylece E6 aynı cümleye ikinci soru yazmaz.

### Dokunulmayan 1 soru

**practice-11** (NO, A11). Sızıntı ifadenin kipinde değil, **kanıt cümlesinin
kendisinde**: G/1 "The pattern after the building condition was essentially the
reverse" diyor. Bu kanıta dayanan her NO ifadesi, "kontrol koşulu tedavi koşuluyla
aynı sonucu vermez" deney mantığıyla parçasız çözülebiliyor — ifadeyi ölçülü
yazmak yetmiyor, farklı bir kanıt cümlesi gerekiyor. Talimata göre kanıt cümlesini
değiştirmek yarım düzeltme sayıldığı için soru olduğu gibi bırakıldı; gerekçe
`review_note` alanına yazıldı. `status` hâlâ `flagged`.

### Kip imzası kırıldı mı?

Düzeltilen 13 sorunun yeni kip dağılımı:

| Kip | YES (3) | NO (4) | NOT GIVEN (6) |
|---|---|---|---|
| mutlak | **1** (practice-7) | 0 | 0 |
| ölçülü | 1 (GT2-35) | **3** (practice-3, 14, GT2-36) | 0 |
| yalın | 1 (GT1-35) | 1 (practice-6) | 6 |
| eksen dışı boyut ekliyor | 0 | 0 | **0** |

Eski üç kuralın üçü de artık çalışmıyor: "mutlak → NO" kalan tek mutlak ifadede
(practice-7) yanlış cevap veriyor; "ölçülü → YES" dört ölçülü ifadenin yalnız
birinde tutuyor; "eksen dışı → NOT GIVEN" hiçbir soruda uygulanamıyor.

### 🔴 E6 ve E7'ye devir notları

1. **Kip dengesi set düzeyinde bir iştir ve yarısı E6'da.** Elenen 9 yuva
   dolduruluncaya kadar sette yalnız 3 YES + 4 NO var. E6, 9 yerine soru yazarken
   **en az bir mutlak yazılmış NO ve en az bir mutlak yazılmış YES** koymalı;
   koymazsa bu sette "mutlak = YES" biçiminde **ters** bir imza oluşur (şu anda
   tek mutlak ifade bir YES). Aynı şekilde ölçülü ifadeler de iki cevaba
   dağıtılmalı.
2. **Yeniden çapalanan 6 NOT GIVEN ölçülmemiş sorudur.** Cevap ve `evidence`
   korundu ama yokluk gerekçesi baştan yazıldı; hepsinde `blind_solvable: null`
   duruyor. E7 bunları yeniden ölçmeli.
3. **practice-6 kısmi düzeltme.** Blanket olumsuzlama kaldırıldı ve yerine sayısal
   bir iddia kondu, ama "karşılaştırmalı bir çalışma bir sonuç bildirmiştir"
   sezgisiyle akıl yürüten bir çözücü hâlâ NO'ya varabilir. E7 ölçümünde bu soruya
   ayrıca bakılmalı.
4. **practice-11 açık kalıyor.** Kanıt cümlesi değişmeden düzeltilemez; E6'nın
   yeniden üretim kapsamına alınması yerinde olur.

### Doğrulama

```
python tools/_e5_ynng_elden_gecir.py     # duzeltildi 13 · elendi 9 · dokunulmadi 1
python tools/_e5_dogrula_degisim.py      # KORUNAN ALAN HATASI: 0
python tools/dogrula.py
```

- `answer`, `evidence`, `evidence_locator` üç dosyada da **hiç değişmedi**
  (HEAD ile alan alan karşılaştırıldı, 0 fark).
- Soru sayısı ve numaralar değişmedi: 15 + 4 + 4 = 23 soru girdi, 23 çıktı.
  GT1 ve GT2 tam testleri 40/40; on iki tam testin hepsi 40/40 kaldı.
- `isaretli (flagged)` 221 → **199** (13 verified + 9 rejected; practice-11 flagged
  kaldı).
- Şema hatası **0**.

#### Rebase notu — dil çevirisiyle çakışma

Bu çalıştırma sırasında depoya paralel iki commit girdi (`28ecd89`, `34236cf`:
"Kullaniciya gosterilen tum alanlar Ingilizceye cevrildi"), ve bu üç YNNG dosyasına
da dokundu: 2026-08-08 kuralı gereği bütün `explanation` alanları İngilizceye
çevrildi. Çakışma, üç dosyanın **yukarı akış sürümü esas alınıp E5 betiği onun
üzerine yeniden koşturularak** çözüldü. Sonuç:

- Elenen 9 ve dokunulmayan 1 sorunun `explanation` alanı yukarı akışın İngilizce
  çevirisiyle duruyor (E5 bu alanlara dokunmuyor).
- Düzeltilen 13 sorunun `explanation` alanı zaten E5 tarafından İngilizce yazıldı.
- Yani 23 sorunun 23'ünde `explanation` İngilizce; şema hatası sayısı çakışma
  öncesindeki 743'ten **0**'a indi. Bu düşüşün tamamı yukarı akış çevirisinin
  eseri, E5'in değil.
- `answer` / `evidence` / `evidence_locator` karşılaştırması çözümden **sonra**
  yukarı akış sürümüne karşı yeniden koşuldu: yine 0 fark.

---

## 2. çalıştırma — çoktan seçmeli, kip imzası + konumsal düzen · 2026-08-08

### Kapsam ve kendi sayımım

Talimatın 1. kuralı gereği yeniden saydım. `content/reading` altında
`question_type: "multiple_choice"` taşıyan yedi dosya var; içlerindeki
`status: "flagged"` **yuva sayısı 30**, ama bu 30 yuva **39 soruya** karşılık
geliyor: dokuz yuva `select_count: 2` (iki harf seçilen "TWO letters" tipi) ve
cevap kâğıdında iki kutu tutuyor.

| Dosya | Yuva | Soru | İşaretli yuva |
|---|---|---|---|
| `content/reading/practice/multiple-choice.json` | 12 | 15 | 12 |
| `content/reading/tests/AC1/multiple-choice.json` | 3 | 4 | 3 |
| `content/reading/tests/AC2/multiple-choice.json` | 3 | 4 | 3 |
| `content/reading/tests/AC3/multiple-choice.json` | 3 | 4 | 3 |
| `content/reading/tests/AC4/multiple-choice.json` | 3 | 4 | 3 |
| `content/reading/tests/GT1/multiple-choice.json` | 3 | 4 | 3 |
| `content/reading/tests/GT2/multiple-choice.json` | 3 | 4 | 3 |
| **toplam** | **30** | **39** | **30** |

Tipin tamamı işaretli. E1'in dağılım tablosundaki 30 sayısı **yuva** sayımı;
soru sayımı 39. E10 bu tipe hiç dokunmadı (üç çalıştırması da tamamlama
ailesindeydi), dolayısıyla ek işaretli yok.

Mekanizma dağılımı da E1'inkiyle birebir tuttu: `konumsal_duzen` 12,
`genel_kultur` 14, `kip_imzasi` 4.

### Sonuç dağılımı

| Sonuç | Yuva | Soru | Nerede |
|---|---|---|---|
| **Düzeltildi** | 16 | 19 | konumsal_düzen 12 + kip_imzası 4 |
| **Elendi** | 14 | 20 | genel_kültür 14 |
| **Dokunulmadı** | 0 | 0 | — |
| **toplam** | **30** | **39** | |

1. çalıştırmadaki gibi elenen küme ile `genel_kultur` kümesi bu tipte de birebir
örtüşüyor. Bu çalıştırmanın başlığındaki iki mekanizmanın (kip imzası + konumsal
düzen) **16 yuvasının 16'sı düzeltildi**; dokunulmadan bırakılan yuva yok.

### a) Kip imzası — 4 yuva

Dört yuvada da imza aynıydı ve kusursuz çalışıyordu: **ölçülü yazılmış her
seçenek doğru, kesin yazılmış hiçbir seçenek doğru değildi.**

| | Ölçülü seçenek | bunlardan doğru | Kesin seçenek | bunlardan doğru |
|---|---|---|---|---|
| **önce** | 6 | **6 (%100)** | 16 | **0 (%0)** |
| **sonra** | 11 | 3 (%27) | 11 | 3 (%27) |

Düzeltme tek yönlü olamazdı: yalnız çeldiricileri yumuşatsaydım "ölçülü = yanlış"
biçiminde ters bir imza kurardım. Bu yüzden her yuvada iki yön birden çalıştı —
bir doğru seçenek kesin kipe çekildi, bir ya da iki çeldirici ölçülü kipe.

| Yuva | Doğru seçenek kesinleşti | Çeldirici ölçülüleşti |
|---|---|---|
| practice-3-4 | F: "cannot yet be excluded" → "**remain too poorly understood**" | A "may also", B "appears to", D "probably" |
| practice-7-8 | F: "may have been present" → "**is the first genetic sign**" | D "may have to be abandoned", E "probably descends" |
| GT2-21 | C: "depends **partly on**" → "**are tied to** what the business needs" | A "may apply", D "is likely to start" |
| GT2-22 | — (A ölçülü kaldı) | C "might also need" |

GT2-22'de doğru seçeneği kesinleştirmedim, çünkü GT2-21 zaten kesin bir doğru
seçenek kazanmıştı; ikisini birden kesinleştirseydim set düzeyinde "kesin =
doğru" imzası doğardı. Onun yerine A'nın metnin kendi `may be required`
kalıbını **birebir yankılaması** kırıldı ("may need to spend" → "can be asked to
come in"). GT2 setinin iki yuvası birlikte: ölçülü 4 seçeneğin 1'i, kesin 4
seçeneğin 1'i doğru.

`practice-7-8`'de F'nin kesinleştirilmesi kanıtı zorlamıyor: F paragrafı
"this is the **first** genetic evidence hinting at the presence of a spelt-like
wheat … at all" diyor, yani *ilklik* iddiası metinde zaten düz kipte duruyor;
temkinli olan şey bulgunun kendisi değil, ondan çıkarılan olasılık.

### b) Konumsal düzen — 12 yuva

E1'in bu etiketle anlattığı şey "elemeyle çözülme". 12 yuvayı okuyunca
eleminin nereden geldiği üç başlıkta toplandı:

1. **Çerçeve dışı çeldirici** — çeldirici, soru kökünün sorduğundan başka bir
   şeyi cevaplıyor. (practice-5: yalnız B siti kendi çağıyla karşılaştırıyordu;
   AC2-34-35: yalnız C ve F "etki neden görünmedi" çerçevesindeydi.)
2. **Uydurma çeldirici** — pasajda hiç geçmeyen bir işlem/nesne. (GT1-21'de
   "personel girişinden yedek kart", AC3-33'te "çok daha büyük bir örnek kümesi",
   AC1-33'te "başarısız olmuş önceki bir deneme".)
3. **Kendi içinde tutarsız çeldirici** — alıntının/pasajın içeriğiyle açıkça
   çelişiyor, okumadan da elenir. (practice-12'de "hasar beklenmişti" ve "uydu
   görüntülerine kuşku düşürmek"; practice-15'te öneriyi tersine çeviren "yalnız
   kışa daraltmak"; AC2-33'te "mesajlaşma ölçülebilir mi" seçeneği.)

Üçü için de tek bir düzeltme kuralı uyguladım:

> **Her çeldirici pasajın gerçek bir ayrıntısına çapalanır ve soru kökünün
> istediği çerçeveye taşınır.** Çeldirici artık "dünyada makul değil" diye değil,
> yalnız "pasaj başka yerde/başka şey söylüyor" diye yanlış olur.

Böylece IELTS'in kendi çeldirici taksonomisine (`yakın ama eksik` /
`yer değiştirme` / `kapsam kaydırma`) dönülmüş oluyor; elenen tür, dosyaların
`distractor_analysis` alanında `cazip ama yok` diye etiketlenen, yani pasajda
karşılığı hiç olmayan uydurma çeldirici. Düzeltilen 12 konumsal düzen yuvasının
38 çeldiricisinde bu etiket **10'dan 6'ya** indi
(`python tools/_e5_mc_sayim.py`); kalan altısı, pasajda karşılığı olmaması
sorunun *tek* çözüm anahtarı olmayan yerlerde bilinçli bırakıldı.

Örnekler:

| Yuva | Eski çeldirici | Yeni çeldirici | Nereye çapalandı |
|---|---|---|---|
| practice-2 | "To let the animals recover from being caught" (pasajda yok) | "whether one steady water temperature removed differences between tanks" | B/1, sabit 24 °C'nin gerçek gerekçesi |
| practice-12 | "To cast doubt on the satellite pictures" (alıntıyla çelişiyor) | "To confirm that the ground survey matched the satellite images" | D/2, 12 Aralık'taki yer araştırması |
| AC1-33 | "It replaced an earlier attempt that had failed" (yok) | "The material the divers collected was analysed on site" | D/2, huniyle toplanan gazın laboratuvara gitmesi |
| AC3-33 | "Examining a much larger set of samples" (yok) | "Matching the proteins found against brain reference databases" | D/4, dördüncü yöntem basamağı |
| GT1-21 | "Collect a spare card from the staff entrance" (yok) | "Have the day recorded as a formal attendance concern" | Metin A, C/3, geç kalma kuralı |

İki yuvada bir de **biçim imzası** vardı, o ayrıca kırıldı:

- **practice-15**: doğru seçenek tek başına üç öğeli bir listeydi ("longer
  visits, other seasons, other cultures") — bilimsel makalelerin "gelecek çalışma
  önerisi" kalıbı. Dört seçeneğin dördü de artık üç öğeli, kendi içinde tutarlı
  birer öneri listesi.
- **AC4-32**: doğru seçenek tek başına iki parçalı karşıtlık taşıyordu ve en uzun
  seçenekti. Dört seçenek de iki öğeli yazıldı.

Ayrıca dört yuvada (practice-2, AC2-32, AC2-33, AC3-33) doğru seçenek kanıt
cümlesinin **birebir yankısı**ydı; bunlarda seçenek metni kanıt cümlesinin
sözcüklerinden uzaklaştırıldı. Örnek: AC2-32'de "see … how much each employee
produced, but who they were working alongside" → "set an individual's output
beside the teammates around them".

### Elenen 14 yuva (20 soru)

Ortak yanı 1. çalıştırmadakiyle aynı: sorunun **ekseninin kendisi** dünya
bilgisi. Seçenekler nasıl yazılırsa yazılsın cevap pasajdan değil alan
bilgisinden çıkıyor.

| Yuva | Cevap | Eksen |
|---|---|---|
| practice-1 | B | deneklerin ağırlığa göre eşleştirilmesi (deney tasarımı âdeti) |
| practice-6 | D | `hexaploid` teriminin `hexa-` öneki cevabı söylüyor |
| practice-9-10 | B, E | buzullu sıradağların sınır boyunca uzanması + kalın buz (coğrafya) |
| practice-11 | D | uyduyla öncesi–sonrası karşılaştırması (standart afet izleme) |
| practice-13 | A | sıra rastgeleleştirmenin amacı tekrar-test etkisi (yöntem kuralı) |
| AC1-32 | B | volkanik adada magmanın bacalardan gaz salması (jeoloji) |
| AC1-34-35 | C, F | asitlenme çalışmalarının "topluluk + iskelet içi" ikili ekseni |
| AC3-32 | B | Herculaneum'un organik malzemeyi iyi koruması (arkeoloji) |
| AC3-34-35 | B, F | organik dokunun karbon+oksijen ağırlıklı olması (temel kimya) |
| AC4-33 | B | adil kıyaslama için öğrenme–sınav aralığının eşitlenmesi |
| AC4-34-35 | C, E | polisomnografi + şekerlemenin ağırlıkla 2. evre olması |
| GT1-22 | C | vardiyalar arası on bir saat dinlenme (çalışma mevzuatı) |
| GT1-23-24 | B, E | mesainin ön onayı + izne çevrilmesi (standart iş yeri politikası) |
| GT2-23-24 | B, D | çekirdek saatte ulaşılabilirlik + konum değişikliğini İK'ya bildirme |

`practice-6` özel bir durum ve gerekçesi kayda değer: sızıntı seçeneklerde
değil, **soru kökündeki terimde**. Terimi kökten çıkarmak kanıt cümlesini de
değiştirmeyi gerektirirdi; talimat bunu "yarım düzeltme" saydığı için yuva
elenenlere yazıldı, düzeltilmedi.

On dördü de `status: "rejected"` + `reject_reason` aldı, dosyalarında
**numaralarıyla duruyor** ve `content/DOGRULAMA/yeniden-uretim-listesi.json`
dosyasına eklendi (liste 9 → **23** kayıt). Her kayıt, o pasajda zaten soru
sorulmuş kanıt cümlesini ve soru kökünü `kacinilacak` altında taşıyor.

### 🔴 Ölçemediğim, ama bulduğum imza: iki harfli yuvalarda C+F yığılması

Bu tipte kip ve konumdan bağımsız, üçüncü bir sızıntı var ve bu çalıştırmanın
yetkisiyle **kapatılamıyor**. Dokuz `select_count: 2` yuvasının cevap harfleri:

| Yuva | Cevap | Bu çalıştırmadaki sonuç |
|---|---|---|
| practice-3-4 | **C, F** | düzeltildi |
| practice-7-8 | **C, F** | düzeltildi |
| AC2-34-35 | **C, F** | düzeltildi |
| AC1-34-35 | **C, F** | elendi |
| practice-9-10 | B, E | elendi |
| AC3-34-35 | B, F | elendi |
| AC4-34-35 | C, E | elendi |
| GT1-23-24 | B, E | elendi |
| GT2-23-24 | B, D | elendi |

Dokuz yuvanın **dördü** C+F; hiçbirinde A ya da G doğru değil, D yalnız bir kez
doğru. Bir çözücü yedi seçenekli yuvalarda pasaja hiç bakmadan C+F yazsa
**4/9** tutturur (şans oranı 1/21). Düzeltme yetkim seçenek *metinleriyle*
sınırlı: harf sırasını değiştirmek `answer` alanını değiştirmek demek, o da
talimatın 🔴 korunan alan kuralına ve "cevap harflerini toptan karıştırma"
yasağına takılıyor. Bu yüzden imzayı kırmadım, **ölçüp E6'ya devrettim** —
aşağıdaki 1. madde.

### 🔴 E6 ve E7'ye devir notları

1. **Harf dağılımı E6'nın işi ve zorunlu.** Bu çalıştırmadan sonra ayakta kalan
   üç `select_count: 2` yuvasının **üçü de C+F** (%100). E6, elenen altı iki
   harfli yuvayı doldururken **hiçbirine C+F vermemeli** ve doğru harfleri A–G
   aralığına yaymalı; özellikle şu ana kadar hiç kullanılmamış **A ve G**
   harflerini kullanmalı. Aksi hâlde bu tipte "C+F yaz" kestirmesi kalıcı olur.
2. **Tek harfli elenen sekiz yuvanın mevcut cevapları B ağırlıklı** (B×4, D×2,
   A×1, C×1). E6 bu yuvaları doldururken harfleri yeniden seçebilir; B'yi
   tekrarlamamasında yarar var.
3. **Düzeltilen 16 yuva ölçülmemiş sorudur.** `answer` ve `evidence` korundu ama
   soru kökü ve/veya seçenek metinleri baştan yazıldı; hepsinde
   `blind_solvable: null` duruyor. E7 bunları yeniden ölçmeli.
4. **practice-6 yeniden üretim kapsamında.** Kanıt cümlesi (`B/2`) `hexaploid`
   terimini tanımıyla birlikte veriyor; E6 bu pasaja yeni soru yazarken
   kromozom sayısını soran bir kök kurmamalı, kanıt cümlesi listede
   `kacinilacak` altında duruyor.
5. **AC2 dosyasının tamamı artık `verified`** (üç yuvanın üçü). E7 ölçümünde bu
   dosya, konumsal düzen düzeltmesinin tek başına yeterli olup olmadığını
   gösteren en temiz örnek olacak; ayrı raporlanması yerinde olur.

### Doğrulama

```
python tools/_e5_mc_elden_gecir.py        # duzeltildi 16 - elendi 14 - dokunulmadi 0
python tools/_e5_mc_dogrula_degisim.py    # KORUNAN ALAN HATASI: 0
python tools/dogrula.py
```

- `answer`, `evidence`, `evidence_locator`, `select_count` yedi dosyanın
  hepsinde **hiç değişmedi** (HEAD ile alan alan karşılaştırıldı, 0 fark).
  Seçenek harflerinin kümesi ve sırası da korundu.
- Yuva ve numara değişmedi: 30 yuva girdi, 30 çıktı; `select_count` ağırlıklı
  soru sayısı **39 → 39**. On iki tam testin hepsi 40/40 kaldı.
- `isaretli (flagged)` 199 → **169** (16 verified + 14 rejected).
- Şema hatası **0**; `explanation` alanlarının hepsi İngilizce yazıldı,
  `distractor_analysis` ve `revision` gibi iç denetim notları Türkçe kaldı.

---

## 3. çalıştırma — cümle sonu eşleştirme + özellik eşleştirme · 2026-08-08

### Kapsam ve kendi sayımım

Talimatın 1. kuralı gereği yeniden saydım. Bu iki tipte `content/reading` altında
altı dosya var; içlerindeki `status: "flagged"` soru sayısı **28**:

| Dosya | Soru | İşaretli |
|---|---|---|
| `content/reading/practice/matching-sentence-endings.json` | 10 | 10 |
| `content/reading/practice/matching-features.json` | 10 | 4 |
| `content/reading/tests/AC1/matching-features.json` | 4 | 3 |
| `content/reading/tests/AC2/matching-features.json` | 4 | 4 |
| `content/reading/tests/AC3/matching-features.json` | 4 | 4 |
| `content/reading/tests/AC4/matching-features.json` | 4 | 3 |
| **toplam** | **36** | **28** |

E1'in dağılım tablosuyla birebir aynı (`matching_features` 18, `matching_sentence_endings`
10) ve mekanizma kırılımı da tuttu: cümle sonu eşleştirmede `konumsal_duzen` 10;
özellik eşleştirmede `konumsal_duzen` 8, `genel_kultur` 6, `kip_imzasi` 4. E10 bu iki
tipe hiç dokunmadı (üç çalıştırması da tamamlama ailesindeydi), ek işaretli yok.

Cümle sonu eşleştirmenin **tamamı** işaretli; özellik eşleştirmede işaretsiz kalan
sekiz sorunun altısı `practice` dosyasının sayısal karşılaştırma soruları.

### Sonuç dağılımı

| Sonuç | Soru | Nerede |
|---|---|---|
| **Düzeltildi** | 21 | cümle sonu 10 · özellik eşleştirme 11 |
| **Elendi** | 6 | özellik eşleştirme 6 |
| **Dokunulmadı** | 1 | AC1-25 |
| **toplam** | **28** | |

🔴 **Bu çalıştırmada elenen küme ile `genel_kultur` kümesi ilk kez örtüşmüyor.**
1. ve 2. çalıştırmada ikisi birebir aynıydı; burada iki soru yer değiştirdi:

- **AC4-26 `genel_kultur` etiketli ama düzeltildi.** Sızıntı sorunun ekseninde
  değil, **seçeneğin kendi adında**ydı: "Positive and Negative Affect Schedule"
  adı, ifadenin sorduğu şeyi ("duygu yelpazesinin iki ucunu birden kaydeder")
  birebir söylüyordu. Adın taşımadığı bir ayrıntı — madde sayısı — kanıt
  cümlesinin içinde duruyordu, o yüzden mekanik düzeltmeye uygun.
- **AC2-24 `kip_imzasi` etiketli ama elendi.** Kapsam sözcüklerini ("geniş alan",
  "özellikle") temizlemek imzayı kırıyor, ama geriye kalan soru "basit buğdaylar
  yaklaşık on iki bin yıl önce nerede ehlileştirildi" oluyor; bu, ders kitabı
  düzeyinde bilinen bir önerme. Eksen genel kültür, etiket ne derse desin.

### a) Cümle sonu eşleştirme — 10 soru, tek bir mekanizma

E1 onunu da `konumsal_duzen` saymıştı ve haklıydı, ama mekanizmanın tam adı şu:
**her başlangıcın karşısında konu olarak yalnız tek bir son vardı.** Sekiz son
dilbilgisi bakımından kusursuz biçimde birbirinin yerine geçiyordu (E1'in
`grammar_check` notları bunu tek tek doğruluyor), dolayısıyla eleme biçimden
değil konudan geliyordu — ve konu eşleşmesi birebir olduğu için pasaja bakmaya
gerek kalmıyordu:

| Başlangıç | Konusu | Bu konudaki son sayısı (eski) |
|---|---|---|
| 1 — şeffaf panel neden kullanıldı | kontrol koşulu gerekçesi | 1 (A) |
| 2 — davranışlar neden ayrı sayıldı | "kendine yönelik" tanımı | 1 (E) |
| 3 — işaret neden göz/kulak arkasına | işaretin konumu | 1 (B) |
| 4 — gerçek/sahte işaret süre farkı | süreden çıkarılan sonuç | 1 (C) |
| 5 — Maris neden başarısızlık sayılmadı | bireysel değişkenlik | 1 (D) |
| 6 — kimler örneklemden çıkarıldı | eksik veri | 1 (B) |
| 7 — farkın büyüklüğü | büyüklük kıyası | 1 (C) |
| 8 — ülkeler arası karşıtlık | ülke oranları | 1 (D) |
| 9 — gönüllülük geliri neden artırsın | gelir yolu | 1 (A) |
| 10 — sağlık neden iyileşsin | bedensel hareket | 1 (E) |

Onunda da aynı: **1**. Bu yüzden düzeltme tek tek ifadelerde değil, **son
listesinin kendisinde** yapıldı. Kural:

> Her başlangıcın karşısına, aynı çerçeveye oturan ama pasajın onaylamadığı en az
> bir rakip son konur; rakip mümkün olduğunca pasajın kendi cümlelerinden
> devşirilir, uydurulmaz.

İki gruptaki üçer boş harf (F, G, H) bu iş için yeniden yazıldı; beş doğru sonun
metni de kanıt cümlesinin sözcüklerinden uzaklaştırıldı. Yeni durum:

| Başlangıç | Doğru son | Yeni rakip(ler) | Rakip nereden geliyor |
|---|---|---|---|
| 1 | A | H | sahte işlem de bir kontrol koşulu (D paragrafı) |
| 2 | E | F, G | toplam 27 saatlik maruziyet (B/4) + reddedilen yorum |
| 3 | B | H | sahte işlem aynı bölgeye uygulanıyor (D) |
| 4 | C | G | pasajın açıkça çürüttüğü "sadece aynadan hoşlanma" (E/3) |
| 5 | D | F | "yeterince fırsatı vardı" biçiminde hafifletici gerekçe |
| 6 | B | — | *kısmi* — dışlanmayı anlatan hâlâ tek son |
| 7 | C | G | "her sürümde aynı sonuç" (G paragrafı) |
| 8 | D | F | gönüllü/gönüllü olmayan karşıtlığının başka ekseni (D/3) |
| 9 | A | F | ters nedensellik: zaten daha eğitimli ve varlıklı (D/3 + E/2) |
| 10 | E | H | aynı cümlenin üçüncü adayı: stres hormonları (H/2) |

Üç düzeltme ayrıca **soruyu kanıt cümlesinin başka bir yarısına taşıdı**, çünkü
eski hâlde son, kanıtın kendi sözlüğünü tekrarlıyordu:

- **2. soru**: eski son "self-directed" teriminin sözlük karşılığıydı
  (`self-directed` ↔ "own body rather than at another animal"). Yeni soru aynı
  kanıt cümlesinin (C/3) öteki yarısını, davranışların ne kadar çabuk ortaya
  çıktığını hedefliyor; karşısında iki süre rakibi var.
- **7. soru**: "somutlaştırma" çağrışımı kaldırıldı, yalnız "gösterebildiler"
  kaldı — böylece büyüklük sonu ile tutarlılık sonu eşit derecede cazip.
- **10. soru**: "sağlık neden iyileşsin" sorusu, "yazarların sıraladığı üç
  açıklamadan ortadaki hangisi" sorusuna çevrildi. Hareketin sağlığa iyi geldiği
  genel bilgisi artık tek başına cevabı vermiyor; sıra ancak H/2 okunarak
  bulunuyor.

**6. soru kısmi düzeltme.** Örneklemin son büyüklüğü (42.926) başlangıca taşındı
ve son sadeleştirildi, ama sekiz son arasında "örneklemden çıkarılma"yı anlatan
hâlâ tek son var. Rakip yazmak için elimdeki tek gerçek malzeme, gelirini
bildirmeyen %11'lik kesim (G/2) idi; o da dışlama ölçütüyle neredeyse aynı şeyi
söylediği için **iki doğru cevaplı** bir soru üretirdi. Belirsizlik yaratmaktansa
sızıntının bir kısmını bıraktım; E7 ölçümünde bu soruya ayrıca bakılmalı.

### b) Özellik eşleştirme — 11 düzeltme, tek bir sızıntı biçimi

Bu tipte `konumsal_duzen` ve `kip_imzasi` etiketlerinin altında aynı şey yatıyor:
**ifade, seçeneklerden yalnız birinin TÜRÜNÜN taşıyabileceği bir özelliği
adlandırıyor.** Cevap, pasajdan değil seçenek listesinin biçiminden çıkıyor —
listeler tür bakımından karışık olduğu için (bir kazı yeri + bir dağ bölgesi +
bir makro bölge + bir kıta + bir ülke) bu çok kolay oluyor.

Kendi sınıflandırmamla, işaretli 18 özellik eşleştirme sorusunun **8'inde**
sızıntı doğrudan bu biçimdeydi:

| Soru | İfadenin adlandırdığı özellik | Yalnız hangi tür taşıyabilir |
|---|---|---|
| practice-9 | "tartılmak yerine yazılı günlük" | tek sıvı kategori (E) |
| practice-10 | "kimsenin *içmek* istemediği kadar" | içecek (E) |
| AC1-25 | "hiçbir şekilde algılayamama" | ışık geçirmez bölme (B) |
| AC1-26 | "yalnızca görebilme" | şeffaf bölme (A) |
| AC2-23 | "ekibin üzerinde çalıştığı tohumlar" | tek kazı yeri (A) |
| AC3-23 | "üstünde duran yamaçlar" | siradağın üstünde yamaç olmaz (D) |
| AC3-26 | "kıyıdaki bu yerleşim" | tek yerleşim (A) |
| AC4-26 | "duygu yelpazesinin iki ucu" | ölçeğin adının çevirisi (B) |

Sekizinin **yedisi** düzeltildi, biri (AC1-25) düzeltilemedi — aşağıda. Uygulanan
kural:

> İfade, seçenek listesinin biçiminden okunabilen özellikten alınıp pasajın
> gerçekten karara bağladığı bir ayrıntıya çapalanır; mümkünse yüzeydeki sezgi
> **yanlış** seçeneği gösterecek biçimde kurulur.

| Soru | Eski çapa | Yeni çapa | Sezgi artık nereye gidiyor |
|---|---|---|---|
| practice-9 | ölçüm *türü* (günlük / tartı) | ölçüm *süresi*: yedi güne karşı sekiz gün (B/1–B/2) | hiçbir yere — süre kategoriden okunamıyor |
| practice-10 | "içmek" fiili | "en sık neden" — pirinç için de fazla pişirme sayılıyor (G/3), ama pirincin baş nedeni bozulma (G/2) | A (pirinç) |
| AC1-23 | "ötekilerden daha uzun bekledi" (üstünlük, C'yi eliyordu) | geç temas + mesafe koruma birlikte (F/2) | E (yabancılar daha temkinli sanılır) |
| AC1-26 | "görebilmek" | farkın *büyüklüğü*: zayıf ama ölçülebilir (H/3) | B (hiç duyusu olmayan grup) |
| AC2-23 | "ekibin çalıştığı tohumlar" | korunma karşılaştırmasının kendisi (B/1) | C (Bereketli Hilal) |
| AC3-23 | "üstünde duran yamaçlar" | malzemenin nereye indiği (A/3) | E (aynı cümledeki "geniş kuşak") |
| AC3-24 | 25 ile kurduğu tamamlayıcılık | "en çarpıcı tek olay" ölçüsü (D/1) | B (Kanada'nın en yüksek tepesi) |
| AC3-25 | "ama en büyüğü orada değildi" | çevredeki izler (D/1) | C |
| AC3-26 | "kıyıdaki bu yerleşim" | yalnız mesafe (A/2) | E (deprem siradağda oldu) |
| AC4-25 | "yarıya indi" | dört düşüşten hangisi **sayıyla** verildi (G/2) | D (canlılık) |
| AC4-26 | ölçeğin ne ölçtüğü | madde sayısı: 20 · 65 · 6 · 4 (E paragrafı) | A (en uzun sanılır) |

**AC3-24 ve AC3-25 bir de birbirini ele veriyordu.** İkisi de aynı cümleye
(D/1) dayanıyor, ikisinin cevabı da o cümlede geçen iki dağ, ve 25 "ama en büyük
tek akış orada değildi" diyerek 24'ün cevabını dışarıda bırakıyordu: birini bilen
ötekini pasaja hiç bakmadan çıkarabiliyordu. O kayıt kaldırıldı; iki soru artık
cümlenin iki ayrı yarısına bağımsız olarak çapalanmış durumda. `allow_repeat`
`false` olduğu için bu tür tamamlayıcılık bu tipte tek başına bir eleme yolu.

### Elenen 6 soru

| Soru | Cevap | Eksen |
|---|---|---|
| practice-1 | A | açık plan ofis en gürültülü düzendir (yaygın kanı) |
| practice-5 | A | açık plan ofise en az geri dönülür (aynı kanı) |
| AC2-24 | C | buğday ~12.000 yıl önce Bereketli Hilal'de ehlileştirildi |
| AC2-25 | B | Karacadağ einkorn ekiminin doğduğu yerdir (arkeoloji) |
| AC2-26 | D | tarım Bereketli Hilal'den Avrupa'ya yayıldı (ders kitabı anlatısı) |
| AC4-24 | A | POMS altı olumsuz duygu boyutu ölçer (ölçme aracı bilgisi) |

Altısı da `status: "rejected"` + `reject_reason` aldı, dosyalarında
**numaralarıyla duruyor** ve `content/DOGRULAMA/yeniden-uretim-listesi.json`
dosyasına eklendi (liste 23 → **29** kayıt). Her kayıt kanıt cümlesini ve
ifadeyi `kacinilacak` altında taşıyor.

🔴 **AC2-24 ile AC2-25 aynı kanıt cümlesini paylaşıyor** (G/2). E6 o cümleye
tek bir soru yazmalı, ikisini birden değil; ikinci yuvayı başka bir paragraftan
doldurmalı.

### Dokunulmayan 1 soru

**AC1-25** (B, A02). Sızıntı ifadenin kipinde değil, **seçenek listesinin
kendisinde**: kanıt cümlesi (C/3) yalnız bölmenin ışık geçirip geçirmediğini
söylüyor, seçenek metinleri de iki grubu tam olarak bu özellikle adlandırıyor
(`see-through screen` / `solid screen`). İlk aşamayla ilgili nasıl yazılırsa
yazılsın her ifade bu iki etiketten birine sözcük düzeyinde bağlanıyor.
Düzeltmek için ya kanıt cümlesini ya seçenek listesini değiştirmek gerekiyordu;
talimat ikisini de bu adımın dışında bıraktığı için soru olduğu gibi kaldı,
gerekçe `review_note` alanına yazıldı, `status` hâlâ `flagged`.

Kardeşi AC1-26 düzeltildiği için elemeyle çözülme yolu yine de daraldı: 26'nın
yeni ifadesi "görmek" sözcüğünü hiç kullanmıyor ve `allow_repeat: false`
altındaki harf elemesini de kesmek için üç aday (A, B, C) açık bırakıyor.

### 🔴 E6 ve E7'ye devir notları

1. **AC2 dosyasının dördünden üçü elendi.** Yeniden üretilecek üç yuvanın
   ikisi (24, 25) aynı kanıt cümlesine bakıyordu; E6 bu cümleye tek soru
   yazmalı. Ayakta kalan tek soru (23) A cevaplı ve `allow_repeat: false`,
   yani yeni üç sorunun cevapları B, C, D, E arasından seçilmeli.
2. **AC1-25 açık kalıyor.** Kanıt cümlesi ya da seçenek listesi değişmeden
   düzeltilemez. En temiz çözüm seçenek listesini bölme türüyle değil
   **aşama/sıra** ile adlandırmak (ör. "ilk üç günü ayrı geçiren birinci
   yarı"); bu, AC1-26'yı da güçlendirir.
3. **Cümle sonu eşleştirmenin 6. sorusu kısmi düzeltme.** Sekiz son arasında dışlanmayı
   anlatan hâlâ tek son var; ikinci bir aday yazmak iki doğru cevaplı soru
   üretme riski taşıdığı için yapılmadı. E7 ölçümünde ayrıca bakılmalı.
4. **Düzeltilen 21 soru ölçülmemiş sorudur.** `answer` ve `evidence` korundu
   ama ifadeler ve cümle sonu listelerinin tamamı baştan yazıldı; hepsinde
   `blind_solvable: null` duruyor. E7 bunları yeniden ölçmeli.
5. **Cümle sonu eşleştirmede son listesi set düzeyinde bir denge işi.** Bu
   çalıştırma iki gruptaki altı boş harfi (F, G, H) rakip son yapmak için
   kullandı; E6 bu tipte yeni soru yazarsa aynı kuralı sürdürmeli — her
   başlangıcın karşısında aynı çerçeveden en az bir rakip son bulunmalı.

### Doğrulama

```
python tools/_e5_mse_mf_elden_gecir.py       # duzeltildi 21 - elendi 6 - dokunulmadi 1
python tools/_e5_mse_mf_devir.py             # eklenen kayit 6 - toplam 29
python tools/_e5_mse_mf_dogrula_degisim.py   # KORUNAN ALAN HATASI: 0
python tools/dogrula.py
```

- `answer`, `evidence`, `evidence_locator`, `allow_repeat` altı dosyanın
  hepsinde **hiç değişmedi** (HEAD ile alan alan karşılaştırıldı, 0 fark).
  Seçenek harflerinin kümesi ve sırası da korundu; `allow_repeat: false` olan
  gruplarda harf tekrarı yok.
- Soru sayısı ve numaralar değişmedi: 36 soru girdi, 36 çıktı. On iki tam
  testin hepsi 40/40 kaldı.
- `isaretli (flagged)` 169 → **142** (21 verified + 6 rejected; AC1-25 flagged
  kaldı).
- Şema hatası **0**; `explanation` alanlarının hepsi İngilizce yazıldı,
  `feature_check`, `grammar_check`, `revision` ve `reject_reason` gibi iç
  denetim notları Türkçe kaldı.

---

## 4. çalıştırma — tamamlama ailesinde eşdizim kilidi · 2026-08-08

### Kapsam ve kendi sayımım

Talimatın 1. kuralı gereği yeniden saydım. Bu çalıştırma tipe değil **mekanizmaya**
bakıyor: `content/reading` altında tamamlama ailesinde (`note` / `sentence` /
`summary` / `table` / `flow_chart_completion`) `flag_mechanism: "esdizim_kilidi"`
taşıyan **61** işaretli soru var (62'nci eşdizim kilidi sorusu tamamlama ailesinde
değil, `practice/short-answer` #6).

Bu 61 soru iki ayrı kaynaktan geliyor ve bunu tek tek doğruladım
(`python tools/_e5_comp_kapsam.py`): E10'un eklediği sorularda
`blind_solvable_kelime_duzeyi` alanı var, E1'inkilerde yok.

| Kaynak | Soru | Bu çalıştırmanın kapsamında mı |
|---|---|---|
| E1 (kelime düzeyi işaret) | 21 | evet |
| E10 — not/tablo/akış tamamlama | 12 | evet |
| E10 — cümle tamamlama | 14 | hayır → 7. çalıştırma |
| E10 — özet ailesi | 14 | hayır → 8. çalıştırma |
| **bu çalıştırma** | **33** | |

Kapsam sınırını böyle çizdim, çünkü çalıştırma listesinin 7. ve 8. maddeleri
E10'un cümle tamamlama ve özet ailesi işaretlerini açıkça kendilerine ayırıyor;
geriye kalan E10 grubunu (not/tablo/akış, 12 soru) hiçbir madde talep etmiyor ve
mekanizması bu maddenin başlığıyla birebir aynı. E1'in dağılım tablosundaki
eşdizim kilidi sayısı (21) kendi sayımımla birebir tuttu.

### Sonuç dağılımı

| Sonuç | Soru | Nerede |
|---|---|---|
| **Düzeltildi** | 15 | E1 kökenli 14 · E10 kökenli 1 |
| **Elendi** | 7 | E1 kökenli 7 |
| **Dokunulmadı** | 11 | E10 kökenli 11 |
| **toplam** | **33** | |

🔴 **Elenen küme ile `genel_kultur` kümesi bu çalıştırmada hiç kesişmiyor.**
Elenen yedi sorunun yedisi de `esdizim_kilidi` etiketli; hiçbiri genel kültür
sorusu değil. Eleme gerekçesi ilk üç çalıştırmadakinden farklı ve aşağıda ayrıca
anlatılıyor.

### Bu mekanizma öncekilerden yapıca farklı

1., 2. ve 3. çalıştırmada sızıntı **çerçevedeydi**: ifadenin kipi, seçeneklerin
biçimi, son listesinin konusu. Çerçeve düzeltilebilir bir şey, çünkü `answer` ve
`evidence` ona dokunmadan yeniden yazılabiliyor. Eşdizim kilidinde durum
tersine dönüyor — sızıntı çoğu zaman **cevabın kendisinde**. 33 soruyu okuyunca
üç alt biçim çıktı:

| Alt biçim | Ne oluyor | Düzeltilebilir mi |
|---|---|---|
| **a) Çerçeve kilidi** | Boşluğun çevresinde, tek bir tamamlaması olan bir kalıp var (`keep a ___`, `put up on the staff ___`, `stay ___`, `the mere ___ of time`). Kalıbı kaldırınca boşluğa birden çok aday uyar hale geliyor. | **Evet** — 14 soru |
| **b) Hesaplanabilir boşluk** | Sızıntı eşdizim değil aritmetik: gövde hem çarpanı hem çarpımı veriyor. | **Evet** — 1 soru |
| **c) Hedef kilidi** | Boşluğun *hedeflediği kavramın* İngilizcede tek karşılığı var (`popularity`, `humidity`, `CV`, `mentor`, `reflects light`). Çerçeve ne yapılırsa yapılsın aynı sözcüğü veriyor; açmak için boşluğu başka bir ayrıntıya taşımak, yani `answer`'ı değiştirmek gerekiyor. | **Hayır** — 7 soru elendi, 11 soru dokunulmadan bırakıldı |

Yani bu mekanizmada "düzeltmek" ile "yeniden üretmek" arasındaki sınır, öteki
mekanizmalardakinden çok daha erken geliyor. Bu çalıştırmanın asıl bulgusu bu.

### a) Çerçeve kilidi — 14 düzeltme

Uygulanan tek kural:

> Boşluğun çevresindeki kilitleyici sözcük (fiil, edat ya da sıfat) kaldırılır ve
> geriye, **pasajın kendi dünyasından en az iki adayın** uyduğu bir yuva bırakılır.
> Cevap artık kalıptan değil yalnız kanıt cümlesinden bulunuyor.

Serbest cevaplı (parçadan kelime) yedi soru:

| Soru | Kaldırılan kilit | Yeni çerçevede uyan adaylar |
|---|---|---|
| practice-sc-8 | `a ___ of what is coming` | preview · warning · benchmark · window |
| practice-sum-10 | `keeping a week-long ___` | diary · log · record · journal |
| AC1-nc-5 | `hidden round a ___` | corner · door · wall · screen |
| AC3-sc-20 | `appear ___ , whereas … looks dark` | bright · white · clearly · strongly |
| GT1-nc-15 | `put up on the staff ___` | noticeboard · portal · intranet |
| GT1-nc-16 | boşluğun önündeki "aynı anda durmuyorlar" tanımı | staggered · scheduled · rotated · coordinated |
| GT1-sum-40 | `collecting and disposing … rather than its ___` | prevention · reduction · progress · change |

GT1-nc-15 örnek olarak anlamlı: aynı belge kümesi hem bir personel ilan panosunu
hem de çevrimiçi bir personel portalını anlatıyor. Eski çerçeve (`put up on`)
portalı dilbilgisiyle eliyordu; yeni çerçeve (`appears on the staff ___`) ikisini
de açık bırakıyor, dolayısıyla 15 ile 20 artık birbirini kısıtlıyor ve ikisi de
metne bakmayı gerektiriyor.

Kelime bankalı özette (7 soru) aynı kural iki yönde birden çalıştı — çünkü orada
kilit yalnız cümlede değil, **bankada uygun rakip bulunmamasında**:

| Soru | Kaldırılan kilit | Artık uyan rakip seçenek(ler) |
|---|---|---|
| AC4-37 | `stayed ___` ("stay awake") | H, metni `the length of the nap` → **`in the laboratory`** yapıldı |
| AC4-39 | `produced almost ___` ("almost" yakınlık istiyor) | G `much weaker results` (artık dilbilgisi olarak uyuyor) |
| AC4-40 | `simply getting ___` ("get a chance to…") | E, metni `deeper sleep` → **`an unbroken night`** yapıldı |
| GT2-37 | `carry only ___` ("only" küçüklük istiyor) | F `roughly half` · H `the main driver` |
| GT2-38 | `the outcome stayed ___ throughout` ("stay stable") | C `contradictory` · D `easily explained` |
| GT2-39 | `___ rather than firm answers` + listedeki "possible" | E `proof of a cause` |
| GT2-40 | boşluğu çevreleyen "karıştırıcı etkenler" ve "rastgele atamalı deneme gerekir" kayıtları | D `easily explained` · E `proof of a cause` |

🔴 Kelime bankasında **yalnız çeldirici metinleri** değişti (AC4'te E ve H). Harf
kümesi, harflerin sırası ve **doğru seçeneklerin metinleri** iki bankada da
korundu; doğrulama betiği bunu ayrıca sınıyor. AC4'te `deeper sleep` çeldirici
sayılmıyordu, çünkü "uykunun iç yapısı"nın kendisiydi ve 40. sorunun cümlesiyle
çelişiyordu; `an unbroken night` aynı yere gerçek bir rakip olarak oturuyor.

GT2-40'ta düzeltme cümlenin kendisiyle sınırlı kalamadı: cevabı asıl sızdıran
şey, boşluğun **önünde** duran "gönüllü olmayı seçenler zaten farklı olabilir"
cümlesi ile **arkasında** duran "rastgele atamalı bir deneme gerekirdi" kaydıydı.
İkisi birlikte "yalnızca bir ilişki" cevabını çerçeveden okutuyordu; ikisi de
özetten çıkarıldı. Kanıt cümlesi (I/1) ve cevap harfi aynı kaldı.

### b) Hesaplanabilir boşluk — 1 düzeltme

**AC2-fc-1** (`forty minutes`) bu çalıştırmanın en net bulgusu ve E10'un
işaretlediği tek not/tablo/akış sorusunun düzeltilebileni. E10 raporu bu soruyu
"ölçüm anahtardan bile katıydı" diye anmıştı, çünkü modelin verdiği `40 minutes`
zaten `accepted_variants` içinde. Asıl mesele başkaydı: akış şemasının ilk kutusu
hem poz **sayısını** ("ten") hem toplam **süreyi** ("roughly six hours")
veriyordu. 6 saat ÷ 10 ≈ 36 dakika; en yakın yuvarlak değer kırk dakika. Yani
cevap pasaja hiç bakılmadan **hesaplanabiliyordu** — sızıntı eşdizim değil
aritmetikti. İki sayı da kutudan çıkarıldı ve şemanın başka bir kutusunda
tekrarlanmadı.

### Elenen 7 soru — hedef kilidi

Bu yedisinde sorun soru metninde değil, **boşluğun neyi hedeflediğinde**. Boşluk,
İngilizcede tek karşılığı olan bir kavramı istiyor; çerçeve nasıl yazılırsa
yazılsın o sözcük çıkıyor. Açmanın tek yolu boşluğu cümlenin başka bir ayrıntısına
taşımak, o da `answer`'ı değiştirmek demek — talimat bunu "yarım düzeltme"
saydığı için düzeltme değil eleme.

| Soru | Cevap | Neden hedef kilitli | E6'ya önerilen yeni çapa |
|---|---|---|---|
| practice-sum-1 | `popularity` | Özet "moda olmasına rağmen kötü sonuç verdi" karşıtlığını taşımak zorunda; bu karşıtlıkta boşluğun tek sözcüğü budur | aynı cümledeki %14'lük düşüş |
| AC2-fc-3 | `reflects` | Parlaklıktan çap tahmini varsayımı İngilizcede yalnız `reflect` fiiliyle kurulur | çap tahmininin sayısı ya da "ölçülemeyecek kadar sönük" gerekçesi |
| AC4-nc-4 | `headphones` | Gürültü çalışmasında gözlemcinin saydığı gündelik alışkanlık = kulaklık; kanıttaki öteki iki örnek de aynı ölçüde tahmin edilebilir | kod commit sayımı |
| AC4-sc-20 | `humidity` | Dört hava değerinden yalnız biri yüzdeyle verilir; birim tek başına cevabı söyler | rüzgâr hızı (1.13 m/s) ya da kar derinliği |
| AC4-sc-21 | `passage` | `the passage of time` tam kalıplaşmış; `of time` kaldırılınca cümle anlamsızlaşıyor | anketlerin on beş dakikanın hemen öncesi/sonrasında uygulanması |
| GT2-tc-16 | `CV` | "Güncel bir ___ yükleyin" satırının başvuru dünyasında tek tamamlaması | 300 kelimelik gerekçe metni ya da 28 Şubat son tarihi |
| GT2-tc-20 | `mentor` | Kanıt cümlesinin bütün içeriği ("kendi biriminden biri, on hafta, haftada bir görüşme") doğrudan bu rolü tanımlıyor | aylık ücret ya da on haftalık süre |

Yedisi de `status: "rejected"` + `reject_reason` aldı, dosyalarında
**numaralarıyla duruyor** ve `content/DOGRULAMA/yeniden-uretim-listesi.json`
dosyasına eklendi (liste 29 → **36** kayıt). Her kayıt kanıt cümlesini ve soru
metnini `kacinilacak` altında, önerilen yeni çapayı da `neden_elendi` içinde
taşıyor.

### Dokunulmayan 11 soru — E10'un anlam düzeyi işaretleri

E10'un not/tablo/akış grubundan gelen 12 sorunun 11'i (12'ncisi yukarıdaki
AC2-fc-1) aynı biçimde: model parçasız üç turda da doğru **kavramı** verdi,
tutmayan şey sözcüğün kendisiydi.

| Soru | Cevap | Modelin verdiği |
|---|---|---|
| practice-nc-3 | individual output | individual performance ×3 |
| practice-nc-4 | Eurasian magpie | magpie ×3 |
| practice-nc-6 | small sample | small group / small sample |
| practice-nc-11 | wooden bed | bed ×3 |
| practice-nc-12 | skeletal remains | bones ×3 |
| AC4-nc-1 | reconfigure | rearrange / reconfigure |
| GT1-nc-17 | card reader | time clock / card reader / clocking-in machine |
| GT1-nc-18 | shift-swap form | shift swap form / shift change form |
| GT1-nc-20 | staff portal | booking system / staff portal |
| AC3-tc-3 | cosmetic | dye ×3 |
| GT2-tc-15 | sponsorship | sponsorship / a visa |

Bunlar hedef kilidinin daha yumuşak bir hâli: kavram çerçeveden çıkıyor ama
sözcük çıkmıyor, dolayısıyla **kelime düzeyinde soru hâlâ çalışıyor** — bir aday
`bones` yazsa yanlış sayılır. Yedi sorunun elenmesi zaten dört tam testte yedi
yuva açtı; bu on biri de elemek aynı dosyaları yeniden üretime bağımlı hale
getirirdi. Bu yüzden bilinçli bir editoryal karar olarak `status` değiştirilmedi
(`flagged` kaldı), her birine `review_note` alanında gerekçe ve E6 için somut bir
yeni çapa önerisi yazıldı. Karar tartışmaya açık; E6 isterse bu on biri de
yeniden üretim kapsamına alabilir, gerekli bilgi dosyaların içinde duruyor.

### 🔴 E6 ve E7'ye devir notları

1. **Eşdizim kilidi, elden geçirmeyle kapanan bir kusur değil.** Bu çalıştırmanın
   kapsamındaki 33 sorunun yalnız 15'i mekanik olarak düzeltilebildi; 18'inde
   sızıntı boşluğun hedefinde. Tamamlama ailesinde yeni soru yazılırken kural şu
   olmalı: **boşluk, İngilizcede tek karşılığı olan bir kavramı hedeflemesin.**
   Sayı, tarih, özel ad ve kapalı liste isteyen boşluklar dayanıklı (E10'un toplu
   raporu da bunu söylüyor); serbest kavram isteyen boşluklar değil.
2. **Elenen yedi yuvanın her birine somut bir yeni çapa önerisi yazıldı** ve
   `neden_elendi` alanında duruyor. AC4-sc-20 ile AC4-sc-21 aynı pasajdan (A11),
   GT2-tc-16 ile GT2-tc-20 aynı metinden (G04) geliyor; ikişerini **ayrı
   paragraflara** çapalamak gerekiyor, kanıt cümleleri listede `kacinilacak`
   altında.
3. **AC4 kelime bankası artık iki yeni çeldirici taşıyor** (E `an unbroken night`,
   H `in the laboratory`). E6 bu bankaya dokunursa bu iki metnin 37 ve 40'ın
   rakipleri olduğunu bilmeli; kaldırılırsa eşdizim kilidi geri gelir.
4. **5. çalıştırmanın kapsamı bu çalıştırmadan etkilenmedi.** Kelime bankalı
   özetteki iki `tanim_sizintisi` sorusu (AC3-38, AC4-36) ile bunların bankadaki
   karşıt seçenekleri (AC4'te C `between-subjects`, I `unrelated in meaning`)
   bilinçli olarak hiç ellenmedi.
5. **Düzeltilen 15 soru ölçülmemiş sorudur.** `answer`, `accepted_variants` ve
   `evidence` korundu ama soru metinleri ve özet/not/akış gövdeleri baştan
   yazıldı; hepsinde `blind_solvable: null` duruyor. E7 bunları yeniden ölçmeli.
   Özellikle GT2 özetinin dördü birden değiştiği için o dosya, kelime bankalı
   özette çeldirici tazelemesinin tek başına yeterli olup olmadığını gösteren en
   temiz örnek olacak.
6. **AC4-sum-39'da küçük bir kesinlik kaybı var.** Eski cümle "produced almost
   equal benefits" diyordu; "almost" kaldırılınca F seçeneği (`equal benefits`)
   pasajın 0.71/0.68 rakamlarına göre bir tık fazla kesin duruyor. Kanıt cümlesi
   "very similar benefits" dediği için seçim hâlâ tek doğru, ama E7 ölçümünde bu
   soruya ayrıca bakılmalı.

### Doğrulama

```
python tools/_e5_comp_kapsam.py            # kapsam: 61 esdizim kilidi, 33'u bu calistirmada
python tools/_e5_comp_elden_gecir.py       # duzeltildi 15 - elendi 7 - dokunulmadi 11
python tools/_e5_comp_devir.py             # eklenen kayit 7 - toplam 36
python tools/_e5_comp_dogrula_degisim.py   # KORUNAN ALAN HATASI: 0
python tools/dogrula.py
```

- `answer`, `accepted_variants`, `evidence`, `evidence_locator` ve `word_limit`
  on dört dosyanın hepsinde **hiç değişmedi** (HEAD ile alan alan karşılaştırıldı,
  102 soruda 0 fark). Kelime bankalarında harf kümesi ve sırası korundu, doğru
  seçeneklerin metinleri korundu; değişen tek şey AC4'teki iki çeldirici metni.
- Her boşluk numarasının özet/not/akış gövdesinde ya da tablo hücresinde hâlâ
  durduğu ayrıca sınandı.
- Soru sayısı ve numaralar değişmedi: 14 dosyada 102 soru girdi, 102 çıktı. On
  iki tam testin hepsi 40/40 kaldı.
- `isaretli (flagged)` 142 → **120** (15 verified + 7 rejected; dokunulmayan 11
  soru flagged kaldı). `esdizim_kilidi` işaretli soru 62 → **40**; kalan 40'ın
  11'i bu çalıştırmanın bilinçli olarak bıraktıkları, 29'u 7. ve 8.
  çalıştırmaların kapsamında.
- Şema hatası **0**; `explanation` alanlarının hepsi İngilizce yazıldı,
  `revision`, `reject_reason` ve `review_note` gibi iç denetim notları Türkçe
  kaldı.

---

## 5. çalıştırma — kelime bankalı özet, tanım sızıntısı · 2026-08-08

### Kapsam ve kendi sayımım

Talimatın 1. kuralı gereği yeniden saydım (`python tools/_e5_wb_kapsam.py`). Bu
çalıştırmanın kapsamı iki kümenin birleşimi: **kelime bankalı özet** alt tipindeki
işaretli sorular ve depo genelinde `flag_mechanism: "tanim_sizintisi"` taşıyan
sorular.

| Küme | Nerede | Soru | Bu çalıştırmada işaretli |
|---|---|---|---|
| kelime bankalı özet | AC2 36–40 · AC4 36–40 · GT2 37–40 | 14 | **7** |
| `tanim_sizintisi` | AC3-38 · AC4-36 | 2 | **1** (AC4-36 zaten üstteki 7'nin içinde) |
| **kapsam** | | | **8** |

Kelime bankalı özet üç dosyada 14 soru; bunların yedisi (GT2'nin dördü, AC4'ün
37/39/40'ı) 4. çalıştırmada eşdizim kilidi kapsamında zaten `verified` olmuştu, o
yüzden bu çalıştırmaya **AC2'nin beşi + AC4'ün 36 ve 38'i** kaldı. `tanim_sizintisi`
mekanizması depo genelinde yalnız iki soruda var; biri AC4-36, öteki AC3-38.
AC3-38 kelime bankalı değil (parçadan kelime), ama mekanizma bu maddenin başlığıyla
birebir aynı olduğu için kapsama alındı — aksi hâlde depodaki iki tanım sızıntısı
sorusundan biri hiçbir çalıştırmaya düşmüyordu.

Parçadan kelime özet (29 soru, 22 işaretli) kapsam dışı; 8. çalıştırmanın maddesi
E10'un özet ailesi işaretlerini açıkça kendine ayırıyor.

### Sonuç dağılımı

| Sonuç | Soru | Nerede |
|---|---|---|
| **Düzeltildi** | 6 | AC2 36, 37, 38, 39, 40 · AC3 38 |
| **Elendi** | 2 | AC4 36, 38 |
| **Dokunulmadı** | 0 | — |
| **toplam** | **8** | |

### Bu tipte sızıntının iki katmanı var

Kelime bankalı özet, öteki tamamlama tiplerinden bir yönüyle ayrılıyor: cevap
adayları **listelenmiş** durumda. Bu, sızıntıyı iki katmana bölüyor ve ikisini
birden kapatmadan soru düzelmiyor:

1. **Özet gövdesi katmanı** — boşluğun hemen yanında, cevabın *tanımını* veren bir
   ibare duruyor. AC2'nin beşinde de vardı: `and the authors could argue for cause
   rather than mere association` (= kontrollü deneyin tanımı), `standard hours and
   fixed contracts turn into ___` (= ölçümün neden güvenilir olduğu),
   `even in the most productive quarter of teams` ("bile" = boşluk olumsuz),
   `teams whose members had stayed longest` (= `length of service`'in birebir
   karşılığı), `rely on a shared, unspoken sense of who knows what` (= temasın
   neden gereksiz olduğu).
2. **Banka katmanı** — bankada o boşluğa dilbilgisi ve çerçeve bakımından uyan
   ikinci bir aday yok. Tanım kaldırılsa bile boşluğa yalnız tek seçenek
   oturuyorsa soru yine parçasız çözülüyor.

AC2'nin bankası bu ikinci katmanın en net örneğiydi. On harften beşi doğru cevap
(A, B, C, H, I), kalan beşi (D, E, F, G, J) hiçbir boşluğun gerçek rakibi
değildi: `extra pay`, `face-to-face contact`, `a training period`, `a rough
guide`, `social comparison`. Beş boşluğun beşinde çeldiriciler ya dilbilgisiyle
ya çerçeveyle eleniyordu, yani banka fiilen beş seçenekli değil **bire bir
eşleşen bir liste**ydi.

### Düzeltme kuralı

> Boşluğun yanındaki tanım ibaresi özet gövdesinden çıkarılır ve gerekçe pasaja
> bırakılır; aynı anda bankadaki boş duran harf, o boşluğa dilbilgisiyle uyan ve
> **yüzeydeki sezginin gideceği** gerçek bir rakip yapılır.

İkinci yarı olmadan birincisi yetmiyor, çünkü tanımı silmek adayı tekleştirmeyi
kaldırmıyor. AC2'de beş çeldiricinin beşi birden yeniden yazıldı:

| Boşluk | Doğru | Kaldırılan tanım ibaresi | Yeni rakip | Sezgi artık nereye gidiyor |
|---|---|---|---|---|
| 36 | A `a controlled experiment` | "the authors could argue for cause rather than mere association" | D `a rough guide` → **`a natural experiment`** | D — şirket politikasından doğan rastgelelik yüzeyde "doğal deney"e benziyor |
| 37 | C `a reliable measure` | "standard hours and fixed contracts turn into ___" | E `a training period` → **`a rough indicator`** | E — çıplak müşteri sayısı yüzeyde kaba bir gösterge |
| 38 | I `no measurable benefit` | "even in the most productive quarter of teams" | F `extra pay` → **`a modest gain`** | F — yıldız çalışanın çevresini yükseltmesi yaygın beklenti |
| 39 | H `length of service` | "teams whose members had stayed longest" | G `face-to-face contact` → **`time spent training`** | G — aynı cümlede takıma ait ikinci bir nitelik |
| 40 | B `a distraction` | "rely on a shared, unspoken sense of who knows what" | J `social comparison` → **`a source of pressure`** | J — "is largely ___" çerçevesine uyan ikinci olumsuz seçenek |

`python tools/_e5_wb_sayim.py` ölçümü: bir boşluğun gerçek rakibi olan çeldirici
sayısı **1 → 5** (beş üzerinden); özet gövdesinde kalan tanım ibaresi **0**.

38 ve 39'da düzeltme yalnız silmekle kalmadı, yerine pasajın kendi rakamını koydu:
39'daki tanım cümlesi "people in the top quarter of teams by that measure produced
roughly 12.2 per cent more" ile değiştirildi — bu, hangi niteliğin ölçüldüğünü
söylemiyor, dolayısıyla H ile G arasındaki seçim ancak F/2 okunarak yapılıyor.

🔴 Bankada **yalnız çeldirici metinleri** değişti. Harf kümesi, harflerin sırası ve
**doğru seçeneklerin metinleri** (A, B, C, H, I) korundu; doğrulama betiği bunu
ayrıca sınıyor.

### AC3-38 — tanım sızıntısının saf hâli

**AC3-38** (`microtubules`) kelime bankalı değil, parçadan kelime. Sızıntı burada
bankada değil, boşluğun hemen ardındaki **açık tanımdaydı**: `the (38) ........ ,
the minute rods that support a cell from within`. Bu, terimin sözlük karşılığıdır;
terimi bilen bir çözücü pasaja hiç bakmadan yazıyordu. Tanımla birlikte çalışan
23 nanometrelik ölçü de çıkarıldı (mikrotübül çapı ~25 nm olarak bilinir; ölçü tek
başına da terimi çağırıyordu). Yerine hiçbir şey tanımlamayan bir sıra bilgisi
kondu ("the smallest structures the team reports"); yeni çerçeveye pasajın kendi
dünyasından birden çok aday uyuyor (`cell bodies`, `myelin sheaths`,
`microtubules`) ve seçim yalnız E/4'ten yapılabiliyor.

### Elenen 2 soru — AC4

İkisi de AC4 özetinde ve ikisinde de sorun çerçevede değil, **boşluğun
hedefinde**; 4. çalıştırmanın "hedef kilidi" başlığıyla aynı yapı.

| Soru | Cevap | Neden mekanik düzeltmeye uygun değil |
|---|---|---|
| AC4-36 | J `within-subject` | Terimin İngilizcedeki tek tanımı "aynı katılımcılar her iki koşuldan da geçer"; ikinci deneyi dürüstçe anlatan her özet bu tanımı vermek zorunda. Üstelik 37. cümle ilk deneyin iki gruplu olduğunu söyleyince bankadaki karşıt terim C (`between-subjects`) ilk deneye bağlanıp eleniyor, J elemeyle çıkıyor. |
| AC4-38 | D `connected in meaning` | Eksen, uykunun hangi tür malzemeyi kayırdığı — bilişsel bilimin en çok aktarılan bulgularından biri — ve banka bu ekseni hazır bir zıt çift olarak taşıyor (D / I `unrelated in meaning`). 39. cümle "Where no such link existed" diyerek 38'in "bağlantılı" taraf olduğunu ayrıca söylüyor. |

AC4-36'da denenip bırakılan iki yol kayda değer: tanımı özetten silmek kalan
çerçeveyi anlamsız bırakıyor, bankadaki C'yi değiştirmek ise J'yi bankadaki **tek**
araştırma-deseni terimi hâline getirip sızıntıyı büyütüyor. Tek çıkış boşluğu başka
bir ayrıntıya taşımak, o da `answer`'ı değiştirmek demek — talimat bunu yarım
düzeltme sayıyor.

İkisi de `status: "rejected"` + `reject_reason` aldı, dosyada **numaralarıyla
duruyor** ve `content/DOGRULAMA/yeniden-uretim-listesi.json` dosyasına eklendi
(liste 36 → **38** kayıt). Her kayıt kanıt cümlesini ve cümlenin kendisini
`kacinilacak` altında, önerilen yeni çapayı `neden_elendi` içinde taşıyor.

### 🔴 E6 ve E7'ye devir notları

1. **AC2 bankasındaki beş yeni çeldirici beş boşluğun tek rakipleri.** E6 bu
   bankaya dokunursa bunu bilmeli; biri kaldırılırsa o boşlukta tanım sızıntısı
   geri gelir.
2. **Elenen iki yuva da A12 pasajından** (AC4 36 ve 38). İkisi de kelime bankalı
   özetin aynı gövdesinde; **ayrı paragraflara** çapalanmalı. Önerilen çapalar
   `neden_elendi` içinde: 36 için B ya da D paragrafı (haftada en az bir kez
   şekerleme yapan 34 katılımcı, ya da sersemliği azaltmak için uygulanan 30
   dakikalık bulmaca), 38 için E paragrafı (0.58'e karşı 0.15 etki büyüklüğü, ya
   da 40 ilişkili + 40 ilişkisiz çift bölüşümü).
3. **Banka harfleri boşalmadı.** İki yuva elendi ama J ve D bankada duruyor; E6 bu
   iki yuvayı doldururken ya aynı harfleri yeni bir çapayla kullanmalı ya da banka
   metinlerini birlikte yenilemeli — 37/39/40'ın cevap harfleri (B, F, A) ve 4.
   çalıştırmanın koyduğu iki çeldirici (E `an unbroken night`, H `in the
   laboratory`) bozulmamalı.
4. **Düzeltilen 6 soru ölçülmemiş sorudur.** `answer`, `accepted_variants` ve
   `evidence` korundu ama özet gövdeleri ve soru metinleri baştan yazıldı;
   hepsinde `blind_solvable: null` duruyor. E7 bunları yeniden ölçmeli. AC2'nin
   beşi birden değiştiği için o dosya, kelime bankalı özette "banka tazelemesi"
   yönteminin tek başına yeterli olup olmadığını gösteren en temiz örnek olacak.

### Doğrulama

```
python tools/_e5_wb_kapsam.py            # kapsam: 8 soru (AC2 36-40, AC4 36/38, AC3 38)
python tools/_e5_wb_elden_gecir.py       # duzeltildi 6 - elendi 2 - dokunulmadi 0
python tools/_e5_wb_devir.py             # eklenen kayit 2 - toplam 38
python tools/_e5_wb_sayim.py             # gercek rakip celdirici 1 -> 5, kalan tanim ibaresi 0
python tools/_e5_wb_dogrula_degisim.py   # sinanan alan 133 - KORUNAN ALAN HATASI: 0
python tools/dogrula.py
```

- `answer`, `accepted_variants`, `evidence`, `evidence_locator` ve `word_limit`
  üç dosyanın hepsinde **hiç değişmedi** (HEAD ile alan alan karşılaştırıldı, 133
  sınamada 0 fark). Kelime bankalarında harf kümesi, harf sırası ve doğru
  seçeneklerin metinleri korundu; değişen tek şey AC2'deki beş çeldirici metni.
- Her boşluk numarasının özet gövdesinde hâlâ durduğu ayrıca sınandı.
- Soru sayısı ve numaralar değişmedi: 15 soru girdi, 15 çıktı. On iki tam testin
  hepsi 40/40 kaldı.
- `isaretli (flagged)` 120 → **112** (6 verified + 2 rejected).
- Şema hatası **0**; `explanation` alanlarının hepsi İngilizce yazıldı, `revision`
  ve `reject_reason` gibi iç denetim notları Türkçe kaldı.

---

## 6. çalıştırma — TRUE/FALSE/NOT GIVEN + kalan tekiller · 2026-08-08

### Kapsam ve kendi sayımım

Talimatın 1. kuralı gereği yeniden saydım (`python tools/_e5_tf_kapsam.py`).
Çalıştırma listesinin bu maddesi iki kümeyi birleştiriyor:

| Küme | Nerede | İşaretli |
|---|---|---|
| **a) `true_false_not_given`** | practice + AC1–AC4 + GT1–GT2 (57 sorunun) | **30** |
| **b) kalan tekiller** | `matching_headings` 8 · `matching_information` 3 · `matching_features` 1 · `yes_no_not_given` 1 · tamamlama ailesinde E1 kökenli `belirsiz` mekanizmalı 6 tek | **19** |
| **kapsam** | | **49** |

"Kalan tekiller"i şöyle tanımladım: **hiçbir çalıştırma maddesinin talep
etmediği, tek tük kalmış işaretli sorular.** Sekiz maddelik listede
`matching_headings` ve `matching_information` hiç geçmiyor; `matching_features`
ile `yes_no_not_given` 3. ve 1. çalıştırmadan birer soruyla artmış durumda;
tamamlama ailesindeki altı `belirsiz` soru ise 4. çalıştırmanın eşdizim
kapsamına, 7. ve 8. çalıştırmanın E10 kapsamına girmiyor. Bunları buraya
almasaydım hiçbir çalıştırmaya düşmeyeceklerdi.

Kapsam dışında kalan 63 işaretli sorunun tamamı bir sonraki iki maddeye ait:
E10 kökenli 40 soru (7. ve 8. çalıştırma ile 4. çalıştırmanın bilinçli olarak
`flagged` bıraktığı 11 not/tablo sorusu) ve E1 kökenli 23 `genel_kultur` sorusu
(8. çalıştırmanın "genel-kültür temalıların elenme kararı" maddesi).

### Sonuç dağılımı

| Sonuç | Soru | Nerede |
|---|---|---|
| **Düzeltildi** | 36 | TFNG 26 · başlık eşleştirme 8 · bilgi eşleştirme 2 |
| **Elendi** | 5 | TFNG 3 · özellik eşleştirme 1 · YES/NO/NOT GIVEN 1 |
| **Dokunulmadı** | 8 | `belirsiz` + `blind_basis: "guess"` olanların tamamı |
| **toplam** | **49** | |

### 🔴 Bulgu 1: TFNG'de sızıntı kipte değil, eksende

1. çalıştırmada YES/NO/NOT GIVEN'ın imzası **kipti**: mutlak yazılmış her ifade
NO, ölçülü yazılmış her ifade YES çıkıyordu. Aynı ölçüyü bu tipte de aldım
(`python tools/_e5_tf_sayim.py`, 2. bölüm) ve sonuç negatif:

| Kapsam/mutlaklık sözcüğü taşıyan ifade | önce | sonra |
|---|---|---|
| TRUE (24 soru) | 1 | 2 |
| FALSE (17 soru) | 0 | 3 |
| NOT GIVEN (16 soru) | **4** | 2 |

Elli yedi ifadenin yalnız beşinde böyle bir sözcük vardı, dolayısıyla "mutlak
yaz" kuralı bu tipte hiç kurulmamış. Kurulan tek yön NOT GIVEN'daydı ve o da
bir kip meselesi değil, eksen meselesinin bir yan ürünü. İşaretli 30 soruyu
okuyunca iki ayrı imza çıktı:

**(a) NOT GIVEN — eksen dışı ayrıntı (7 soru).** Yedisi de pasajın hiç
konuşmadığı bir *boyut* ekliyordu; soruyu okumak yetiyordu, pasaja bakmaya
gerek yoktu:

| Soru | Eklenen eksen dışı boyut |
|---|---|
| practice-3 | oturumların günün hangi saatinde yapıldığı |
| practice-7 | dizilemenin kaç ay sürdüğü |
| practice-10 | araştırmacıların araziye nasıl gittiği (yürüyerek) |
| AC1-13 | hiç ele alınmayan bir duyu kanalı (görme) |
| AC2-13 | verilmeyen bir yayın takvimi ("bir yıl içinde") |
| GT2-9 | tekil bir olaya "her yıl" kapsamı eklemek |
| GT2-13 | hiçbir rağbet sıralaması olmayan yerde "en popüler" |

**(b) TRUE/FALSE — genel kültür ekseni (18 soru) ve kalıp beklentisi (2 soru).**
Burada ifade, alan bilgisinden ya da bilim haberciliğinin anlatı kalıplarından
doğrudan çıkan bir önermeyi soruyordu: Herculaneum'un organik malzemeyi eşsiz
biçimde koruması, içgörünün tanımı gereği ani olması, erken bilet indiriminin
ucuz olması, kütüphane cezasının üst sınırı bulunması…

Kalan 3 soru `belirsiz` etiketliydi ve aşağıda ayrıca ele alınıyor.

### Düzeltme kuralı — aynı kanıt cümlesinin öteki yarısı

🔴 Talimatın kuralı gereği `answer` ve `evidence` korunuyor, dolayısıyla
düzeltme için tek bir hareket alanı var:

> İfade, **aynı kanıt cümlesinin** dünya bilgisinden okunamayan yarısına
> taşınır. Mümkünse yüzeydeki sezgi **yanlış** cevabı gösterecek biçimde
> kurulur.

On dokuz TRUE/FALSE düzeltmesinin sekizi artık metnin kendi sayısına dayanıyor
(sayısal çapa taşıyan ifade **3 → 8**); geri kalanı yön, rol ya da neden gibi
yapısal çapalar kullanıyor. Örnekler:

| Soru | Cevap | Eski eksen (genel kültür) | Yeni çapa (aynı kanıt cümlesi) |
|---|---|---|---|
| practice-8 | FALSE | buğday Bereketli Hilal'de evcilleşti | Çatalhöyük'e biçilen rol: ara durak mı, son nokta mı (G/3) |
| practice-13 | TRUE | Herculaneum organik malzemeyi eşsiz korur | örtü tabakasının "over the following days" birikmesi (A/3) |
| practice-15 | FALSE | camlaşmış beyin dokusu bulgusu ünlüdür | "converted **directly** into a glass-like solid" (C/1) |
| AC1-7 | TRUE | filler içgörü testlerinde başarısızdı | bulmacanın fiziksel biçimi: kutuya çıkıp yükselmek (A/3) |
| AC1-12 | FALSE | "araç yanlıştı" anlatı kalıbı | araç **sunulmuş muydu** (F/2 + B) |
| AC2-11 | TRUE | yer teleskopları uzay araçlarından zayıftır | görünmezliğin nedeni: boyut mu uzaklık mı (F/3) |
| AC4-7 | TRUE | akademik girişlerin "kontrollü kanıt yok" kalıbı | ana kampüsteki 5.580 çalışan (A/4) |
| GT1-8 | TRUE | kütüphane cezaları üst sınırlıdır | 20 peni/gün ile 5 sterlin üst sınırının kesişimi: 25. gün (A/4) |
| GT1-9 | FALSE | cumartesi saatleri daha kısadır | 10.00–16.00 = altı saat, sekiz değil (A/5) |
| GT2-11 | TRUE | geri almadan önce yazılı uyarı verilir | "en az %75 ekili" → en çok çeyrek boş (C/3) |

**İki düzeltmede sezgi bilerek yanlış yöne çevrildi.** `practice-13`'te yaygın
sezgi "kasaba bir anda gömüldü" der ve FALSE'a gider; doğru cevap yalnız
"over the following days" ibaresinden çıkıyor. `AC4-13`'te ofis çalışmalarının
bilinen örgüsü "öznel ölçümler değişir, nesnel çıktı değişmez" der; yeni ifade
tam da **öznel** bir ölçümün (kendi bildirilen enerji) değişmediğini soruyor,
yani örgü bu kez yanlış cevabı gösteriyor.

**Yedi NOT GIVEN yeniden çapalandı.** Bu tipte de korunacak kanıt cümlesi yok
(`evidence` zaten `null`); korunan şey yokluğun kendisi. Yedisi de artık metnin
ayrıntısıyla düzenlediği bir alanda karara bağlanmamış bir ayrıntı soruyor:

| Soru | Yeni çapa | Neden hâlâ NOT GIVEN |
|---|---|---|
| practice-3 | baskın hayvanın ağır olan olup olmadığı | B ağırlıkları, D baskınlığı veriyor; ikisi hiç çaprazlanmıyor |
| practice-7 | iki laboratuvarın iş bölüşümü | D/1 iki laboratuvarı ve gerekçesini veriyor, bölüşüme girmiyor |
| practice-10 | 12 Aralık'taki yer araştırmasının kapsamı | D iki dağı da anıyor, araştırmanın hangi yamaçları gezdiğini söylemiyor |
| AC1-13 | bambu sopanın ne zaman kaldırıldığı | B sopayı sunuyor, F neden işe yaramadığını anlatıyor; D'de kaldırılan nesne kup |
| AC2-13 | bir ad önerilip önerilmediği | E adlandırma geleneğini ve onay sürecini veriyor, öneri konusuna girmiyor |
| GT2-9 | dışarıdan yiyecek getirilip getirilemeyeceği | B hem yiyecek standını hem bir yasağı (kamp) düzenliyor, bunu düzenlemiyor |
| GT2-13 | iptal edilen dersin yeniden açılıp açılmadığı | E iptal kuralını ayrıntısıyla veriyor, telafiye hiç değinmiyor |

Sözcük örtüşmesine dayanan kaba bir ölçü (`_e5_tf_sayim.py`, 3. bölüm) yedisinden
beşinde eksen oranının korunduğunu ya da yükseldiğini gösteriyor; AC2-13'te
0.38 → 0.75 ile en büyük sıçrama var. Ölçü paraphrase'i göremediği için
GT2-9'da düşük görünüyor (0.83 → 0.50) — o ifade metnin sözcükleriyle değil,
metnin *düzenlediği alanla* çapalandı. Asıl denetim yukarıdaki tabloda, elle.

### 🔴 Bulgu 2: başlık eşleştirmede sızıntı sorularda değil, listede

Sekiz işaretli `matching_headings` sorusunun hiçbirinde ifade yok — soru
yalnızca "Paragraph B" diyor. Dolayısıyla parçasız çözülebilme başlıkların
kendisinden geliyor ve iki kaynağı var:

1. **Ölü başlık.** Pasajda hiç karşılığı olmayan ya da pasajın açıkça
   çürüttüğü bir şeyi adlandıran başlık, okumadan elenir. (AC4'te "A surprising
   rise in participants' energy" — pasaj canlılığın **yükselmediğini** söylüyor;
   GT1'de "How the amounts changed across the seasons" — metin mevsimleri
   ölçmediğini açıkça yazıyor.)
2. **Anlatı sırası.** Ölü başlıklar elenince kalan başlıklar akademik bir
   pasajın alışılmış sırasına (tasarım → yöntem → koşullar → ölçüm → sonuç)
   birebir oturuyor ve B–F paragrafları da o sırada geliyor.

Uygulanan kural:

> Ölü başlıklar, **sorulmayan paragrafların** (A, G, H) gerçek içeriğiyle
> yeniden yazılır. Böylece hiçbir başlık "pasajda karşılığı yok" ya da
> "pasajla çelişiyor" diye elenemez; her sorulan paragrafın karşısında aynı
> çerçeveden en az bir rakip kalır.

On iki başlık yeniden yazıldı; **doğru cevap olan hiçbir harfin metnine
dokunulmadı** (doğrulama betiği bunu harf harf sınıyor):

| Dosya | Harf | Eski (ölü) | Yeni | Nereye çapalandı |
|---|---|---|---|---|
| practice P-MH-03 | ii | The stages that make up a night's sleep | The internal make-up of the daytime naps | F/1 (64,1 dakika, ağırlıklı 2. evre) |
| practice P-MH-03 | vi | How the puzzle game changed the scores | Practical advice for people who rely on naps | H |
| practice P-MH-03 | viii | Why some pairs were harder to learn | Why some memories need a whole night | G/2 |
| AC2 | vi | The difficulty of dating buried seeds | Why the shape of a grain can mislead | C/2 + H |
| AC2 | ix | Storage methods that kept the harvest edible | Remains better preserved than at comparable sites | B/1 |
| AC3 | x | A glacier stopped in its tracks | New dangers for climbers and expeditions | G |
| AC4 | i | A surprising rise in participants' energy | The reverse pattern at the second site | G |
| AC4 | iv | The health risks of standing in severe cold | Why the snow may have hidden one effect | H/1 |
| AC4 | vii | An urban view chosen to create stress | A calm city scene used for comparison | C/2 |
| AC4 | x | How long each questionnaire took to complete | The number of items in each scale | E (65 · 20 · 6 · 4) |
| GT1 | v | How the amounts changed across the seasons | The reasons householders themselves gave | G |
| GT1 | x | Why one district earns more than another | What rural families did with their scraps | H |

Üç yerde rakip bilinçli olarak **paragrafın ilk cümlesine** çapalandı, yani
klasik IELTS tuzağı kuruldu: başlık paragrafın bir yarısını doğru anlatıyor ama
ana fikrini vermiyor. `practice-15`'te F paragrafının ilk cümlesi (naps'in iç
yapısı) artık ii'ye, ana fikri (o yapının bellek kazancını açıklamaması) v'ye
karşılık geliyor; aynı kurgu AC2-14 (B/1 korunmuşluk ↔ B'nin ana fikri kimliğin
doğrulanmamışlığı) ve AC4-17'de (E'nin madde sayıları ↔ ölçümün öncesi/sonrası)
tekrarlanıyor. Seçim artık paragrafın tamamını okumayı gerektiriyor.

### Bilgi eşleştirmede iki düzeltme

`matching_information`'da mekanizma "soru kökünün adlandırdığı kavramın pasajda
tek karşılığı olması". İkisinde de kök, aynı kanıt cümlesinin başka bir yarısına
taşındı ve böylece gerçek bir rakip paragraf doğdu:

| Soru | Eski kök | Yeni kök | Yeni rakip |
|---|---|---|---|
| practice-6 (H) | "hakem değerlendirmesinden geçmemiş olma itirafı" | "bu bulgunun örneklediği söylenen genel örüntü" | F (Voyager'ın görememesi) ve C (boyutun tahminle bulunması) aynı fikrin tekil örnekleri |
| AC3-28 (H) | "başka kurbanlar için aynı şeyin varsayılmaması uyarısı" | "aynı korunmanın verili sayılamayacağı ikinci bir kasabaya gönderme" | A da Pompeii'yi anıyor ve iki kasabanın gömülme biçimini karşılaştırıyor |

### Elenen 5 yuva

| Soru | Cevap | Eksen / neden düzeltilemedi |
|---|---|---|
| practice TFNG-4 | TRUE | Kanıt cümlesi (F/3) tek yön söylüyor: yabancılar daha çok etkileşime giriyor. Cümleden çıkan her doğru ifade bu biçimi alıyor ve yenilik arayışı davranış biyolojisinin en yaygın genellemelerinden biri. |
| AC1 TFNG-10 | TRUE | Kanıt cümlesi (D/3) yalnız "yiyecek yeri değişince kübü yeni noktaya yuvarladı" diyor; her doğru ifade "akıllı hayvan uyum sağladı" oluyor. |
| AC3 TFNG-7 | TRUE | Kanıt cümlesi (A/3) ayna testi tartışmasını özetliyor; cümlede pasaja özgü tek bir sayı, ad ya da ölçü yok. |
| AC1 matching-features-25 | B | 3. çalıştırma "kanıt cümlesi ya da seçenek listesi değişmeden düzeltilemez" diye dokunulmadan bırakmıştı. |
| practice YNNG-11 | NO | 1. çalıştırma "kanıt cümlesi değişmeden düzeltilemez" diye dokunulmadan bırakmıştı. |

🔴 **Son iki satır bu çalıştırmanın bilinçli bir kararı.** 1. ve 3. çalıştırma bu
iki soruyu "dokunulmadı" kutusuna koymuş, ama ikisinin de devir notunda "E6'nın
yeniden üretim kapsamına alınması yerinde olur" yazıyordu. Talimat, kanıt
cümlesinin değişmesi gereken durumu açıkça **elenme** sayıyor; ikisi de tam
olarak o durumda. Kutuda bırakmak yerine `rejected` yapıp devir dosyasına
yazdım, böylece E6 onları listede görüyor. Dosyalarında numaralarıyla
duruyorlar.

Beşi de `content/DOGRULAMA/yeniden-uretim-listesi.json` dosyasına eklendi
(liste 38 → **43** kayıt); her kayıt kanıt cümlesini ve ifadeyi `kacinilacak`
altında, önerilen yeni çapayı `neden_elendi` içinde taşıyor.

### Dokunulmayan 8 soru — ölçüm gürültüsü

Bu sekizinin ortak bir imzası var ve imza sızıntıda değil, **ölçümde**:
`blind_basis` alanı sekizinde de `"guess"`. E1'in kendi gerekçeleri de sızıntıyı
değil sızıntının yokluğunu anlatıyor — "birden çok seçenek eşit derecede olası",
"doğru sözcüğün tutturulması büyük ölçüde şansa dayanıyor". Yani bunlar tek
turluk bir ölçümde şansla tutmuş sorular.

| Soru | Cevap | E1'in kendi gerekçesi |
|---|---|---|
| AC1 TFNG-11 | TRUE | üç seçenekli kümede şans |
| AC3 matching-info-29 | E | sekiz paragraflı kümede şans |
| practice summary-5 | leafy | "lush / dense / mature" da uyuyor |
| practice summary-7 | sharply | "significantly / rapidly" da uyuyor |
| practice summary-13 | five-point | beş/yedi/on noktalı ölçekler eşit olası |
| AC2 flow-chart-5 | fourteenth | "parçaya bakmadan tahmin edilemeyecek kadar spesifik" |
| AC3 table-1 | acrylic | "plastic / glass / plexiglass" da uyuyor |
| AC4 note-5 | novelty | "temporary / short-term / placebo" da uyuyor |

Talimatın 3. sonucu ("mekanizma net değilse soru olduğu gibi kalır, gerekçesi
yazılır") tam olarak bu durum için; sekizine de `review_note` yazıldı, `status`
`flagged` kaldı.

🔴 **Bir istisnayı kayda geçiriyorum: AC4 note-5.** E1 "belirsiz" demiş, ama
`merely a ___ effect` çerçevesi 4. çalıştırmanın tanımladığı **eşdizim kilidi**
biçimine yakın duruyor (`novelty effect` yerleşik bir eşdizim). Kilidi açmanın
tek yolu boşluğu başka bir ayrıntıya taşımak, o da `answer`'ı değiştirmek
demek — yani bu bir düzeltme değil eleme olurdu. AC4 dosyasında 5. çalıştırmadan
gelen iki elenen yuva (36 ve 38) zaten var; üçüncü bir yuva aynı pasajı yeniden
üretime iyice bağımlı kılardı. Bu yüzden elemedim ama kararı gizlemiyorum: E6
isterse kapsama alabilir, önerilen yeni çapa F/3'teki %4'lük masa doluluk
artışı.

### 🔴 E6 ve E7'ye devir notları

1. **AC1 TFNG dosyası en çok yıpranan dosya.** Yedi sorunun biri elendi (10),
   biri `flagged` kaldı (11) ve ikisi de aynı ekseni paylaşıyordu ("etkileyici
   yetenek iddiası → TRUE"). E6 elenen yuvayı doldururken bu eksene dönmemeli;
   D paragrafının nesnel ayrıntıları (aynı oturumda dokuz tekrar, traktör
   lastiği, küçük nesneleri üst üste koyma denemesinin başarısızlığı) listede
   `kacinilacak` altında değil, `neden_elendi` içinde öneri olarak duruyor.
2. **Elenen üç TFNG yuvasının cevapları TRUE.** Elemeden sonra tipin cevap
   dağılımı TRUE 21 · FALSE 17 · NOT GIVEN 16 oldu (elenen yuvalar sayılmadan).
   E6 üç yuvayı doldururken en az birini FALSE ya da NOT GIVEN yapmalı, aksi
   hâlde TRUE ağırlığı geri gelir.
3. **Başlık listeleri artık set düzeyinde dengede; bozulmasın.** On iki yeni
   başlığın her biri belirli bir paragrafın rakibi. E6 bu gruplara dokunursa
   yeni başlıkları da aynı kuralla yazmalı: sorulmayan paragrafların gerçek
   içeriğinden devşir, uydurma ya da pasajı çürüten başlık koyma.
4. **Düzeltilen 36 soru ölçülmemiş sorudur.** `answer` ve `evidence` korundu ama
   ifadeler ve başlık listeleri baştan yazıldı; hepsinde `blind_solvable: null`
   duruyor. E7 hepsini yeniden ölçmeli.
5. **E7 için özel istek: `blind_basis` alanı tek turluk ölçümde güvenilmez.**
   Bu çalıştırmanın dokunulmadan bıraktığı sekiz sorunun sekizi de o alanda
   `guess` taşıyordu, yani bir mekanizma değil şans kaydedilmişti. E7 ölçümü
   tekrarlı yapmalı; aksi hâlde bu sekiz soru bir sonraki turda da işaretli
   görünür.
6. **AC4-17'de kabul edilmiş bir belirsizlik payı var.** Yeni rakip başlık
   ("The number of items in each scale") E paragrafının gerçekten verdiği bir
   şeyi adlandırıyor; doğru başlık hâlâ vi, çünkü paragrafın ana fikri ölçümün
   deneyimden önce ve sonra yapılması. Aynı kurgu AC4-15'te (vii "A calm city
   scene used for comparison") de var. E7 ölçümünde bu iki soruya ayrıca
   bakılmalı.

### Doğrulama

```
python tools/_e5_tf_kapsam.py            # kapsam: 30 TFNG + 19 tekil = 49
python tools/_e5_tf_elden_gecir.py       # duzeltildi 36 - elendi 5 - dokunulmadi 8
python tools/_e5_tf_devir.py             # eklenen kayit 5 - toplam 43
python tools/_e5_tf_sayim.py             # sayisal capa 3 -> 8; kapsam sozcugu dagilimi
python tools/_e5_tf_dogrula_degisim.py   # sinanan alan 867 - KORUNAN ALAN HATASI: 0
python tools/dogrula.py
```

- `answer`, `evidence`, `evidence_locator` ve `difficulty` yirmi dosyanın
  hepsinde **hiç değişmedi** (HEAD ile alan alan karşılaştırıldı, 867 sınamada
  0 fark). Başlık ve seçenek listelerinde harf kümesi, harflerin sırası ve
  **doğru cevap olan harflerin metinleri** korundu; değişen tek şey on iki ölü
  başlık.
- Soru sayısı ve numaralar değişmedi: 49 soru girdi, 49 çıktı. On iki tam
  testin hepsi 40/40 kaldı.
- `isaretli (flagged)` 112 → **71** (36 verified + 5 rejected; dokunulmayan 8
  soru `flagged` kaldı).
- Şema hatası **0**; `explanation` alanlarının hepsi İngilizce yazıldı,
  `revision`, `reject_reason`, `review_note`, `scan_note`,
  `contradiction_point` ve `not_given_justification` gibi iç denetim notları
  Türkçe kaldı.

---

## 7. çalıştırma — E10'dan gelen cümle tamamlama + kısa cevap işaretleri · 2026-08-08

### Kapsam ve kendi sayımım

Talimatın 1. kuralı gereği yeniden saydım (`python tools/_e5_sc_kapsam.py`).
`content/reading` altında `sentence_completion` ve `short_answer` tiplerinde
**26** işaretli soru var; bunların kaynağını tek tek ayırdım — E10'un eklediği
sorularda `blind_solvable_kelime_duzeyi` alanı duruyor, E1'inkilerde durmuyor:

| Kaynak | Soru | Bu çalıştırmanın kapsamında mı |
|---|---|---|
| **E10 — cümle tamamlama** | 14 | evet |
| **E10 — kısa cevap** | 1 | evet |
| E1 — `genel_kultur` | 11 | hayır → 8. çalıştırma |
| **bu çalıştırma** | **15** | |

E10 raporunun 1. çalıştırma tablosuyla birebir aynı (cümle tamamlama 14, kısa
cevap 1). Dosya dağılımı: practice cümle tamamlama 6 · practice kısa cevap 1 ·
AC1 2 · AC2 1 · AC3 1 · AC4 1 · GT1 1 · GT2 2.

Kapsam sınırını böyle çizdim, çünkü 8. çalıştırma maddesi E1 kökenli genel-kültür
sorularının elenme kararını açıkça kendine ayırıyor; 4. çalıştırma da bu 15 soruyu
"7. çalıştırmaya" diye kapsamı dışında bırakmıştı.

### Sonuç dağılımı

| Sonuç | Soru | Nerede |
|---|---|---|
| **Düzeltildi** | 2 | AC1 19, 20 |
| **Elendi** | 7 | practice sc-3, sc-12, sa-6 · AC3 22 · AC4 22 · GT1 27 · GT2 25 |
| **Dokunulmadı** | 6 | practice sc-2, sc-4, sc-6, sc-7 · AC2 20 · GT2 26 |
| **toplam** | **15** | |

🔴 **Bu, sekiz çalıştırmanın en az düzeltme yapanı ve bu bir başarısızlık değil,
bulgunun kendisi.** Aşağıda ölçtüm: kapsamın 15 sorusunun **13'ünde** boşluğun baş
adı cümlenin anlamsal rolünden zorunlu olarak çıkıyor, yani soru metni ne yapılırsa
yapılsın aynı kavram okunuyor. Yeniden yazmak sızıntıyı kapatmadan ölçülmemiş yeni
bir soru üretirdi — talimatın "yarım düzeltme" saydığı şey tam olarak bu.

### Mekanizma: bu sızıntı ötekilerden yapıca farklı

E10 bu 15 sorunun hepsine `esdizim_kilidi` etiketi vermiş, ama 15'ini okuyunca
mekanizmanın adı başka: **model parçasız üç turda da doğru KAVRAMI verdi, tutmayan
şey sözcüğün kendisiydi.** Cevapların on üçü *niteleyici + baş ad* biçiminde bir
öbek ve modelin verdiği cevap çoğu seferinde öbeğin yalnız bir parçası:

| Doğru cevap | Modelin parçasız cevabı | Eksik kalan ayırt edici öge |
|---|---|---|
| sensory **contact** | contact ×3 | `sensory` |
| running **seawater** | seawater ×3 | `running` |
| unique **individual** | individual ×3 | `unique` |
| laboratory **tank** | laboratory ×3 | `tank` |
| dominance **hierarchy** | hierarchy ×3 | `dominance` |
| separate **laboratories** | laboratories ×3 | `separate` |
| home-office **equipment** | office equipment ×3 | `home-` |
| **transactive memory** system | transactive memory ×3 | — (yalnız `system` düştü) |
| **transparent** divider | transparent barrier ×3 | — |
| **final** salary | final pay ×3 | — |
| **probationary** period | probation period ×3 | — |
| anatomy | anatomy · morphology · anatomy | — |
| vegetation | vegetation · foliage · vegetation | — |
| mountaineers | climbers ×3 | — |
| ongoing research | preliminary ×3 | — |

Tablo iki kümeye ayrılıyor ve ayrım kararı belirliyor.

### 🔴 Ayırma ölçütü

> **Modelin parçasız cevabı, doğru cevabın AYIRT EDİCİ ögesini de taşıyor mu?**

- **Taşımıyorsa** (yalnız baş adı verdi, niteleyici düştü) → soru **kelime
  düzeyinde hâlâ ayırt ediyor**: `seawater` yazan aday puan almaz. Elemek için
  yeterli gerekçe yok.
- **Taşıyorsa** (ayırt edici ögeyi birebir ya da tam eş anlamlısıyla verdi) → soru
  artık yalnızca kopyalama sınıyor. Bu durumda ikinci soru geliyor: ayırt edici öge
  **nereden** okunuyor? Sorunun kendi açıklayıcı yan cümlesinden okunuyorsa yan
  cümle kaldırılır (**düzeltildi**); cevabın kendisinden okunuyorsa `answer`'a
  dokunmadan erişilemez (**elendi**).

İkinci bir ölçüt de düzeltilebilirliği belirliyor: **boşluğun baş adı cümlenin
anlamsal rolü tarafından zorunlu kılınıyor mu?** Bir ahtapot tankına ne verildiği
sorulduğunda baş ad zorunlu olarak `seawater`, eski DNA'nın nerede çözümlendiği
sorulduğunda zorunlu olarak `laboratories` olur.

İki ölçüt sonucu **tam olarak** belirliyor (`python tools/_e5_sc_sayim.py`):

| ayırt edici öge modelde | baş ad | sonuç | soru |
|---|---|---|---|
| yok | açık | **düzeltildi** | 1 |
| VAR | açık | **düzeltildi** | 1 |
| VAR | zorunlu | **elendi** | 7 |
| yok | zorunlu | **dokunulmadı** | 6 |

Ölçüm: ayırt edici öge 15 sorunun **8'inde** modelin cevabında duruyordu; baş ad
**13'ünde** zorunluydu.

### Düzeltilen 2 soru — sızıntı çerçevede

İkisi de AC1 cümle tamamlamadan ve ikisinde de sızıntının kaynağı sorunun kendi
açıklayıcı yan cümlesiydi: soru, cevabın tanımını okuyucuya veriyordu.

| Soru | Kaldırılan tanım | Yeni çapa | Sezgi artık nereye gidiyor |
|---|---|---|---|
| **19** (`transparent divider`) | "so each animal could **watch** its neighbour without ever touching or smelling it" — şeffaflığın tanımı | C/2'nin başka ayrıntısı: komşu tanklar + su beslemelerinin tamamen ayrı tutulması | ayrı su beslemesi koku engelini çağrıştırdığı için okumadan tahmin eden çözücü **opak/masif** bir bölme düşünür — yanlış cevap |
| **20** (`dominance hierarchy`) | "one of each pair came to **win** most encounters" — baskınlık sıralamasının tanımı | D/3'ün ikinci yarısı (temas ve mürekkep püskürtmenin seyrelmesi) + D/2'nin süre ayrıntısı | "ilişkiler yumuşadı" okuması *mutual tolerance* / *familiarity* gibi adaylara götürür — yanlış cevap |

19'da model üç turda da `transparent barrier` vermişti, yani ayırt edici sözcüğü
(`transparent`) birebir tutturuyordu; o sözcüğün tek kaynağı sorunun kendisiydi.
20'de model yalnız `hierarchy` veriyordu, yani kelime düzeyinde soru zaten
çalışıyordu — ama baş adı zorunlu kılan yan cümle kaldırılabildiği için düzeltmek
sızıntıyı büsbütün kapatıyor, dolayısıyla yarım düzeltme sayılmıyor.

Cevap benzersizliği ikisinde de korunuyor: C/3'teki opak bölme grubu için ne
"komşu tank" ne "ayrı su beslemesi" deniyor, D/3 de üç gün boyunca ortaya çıkan
tek şeyi adlandırıyor. 20'de %76'lık oran sorudan çıkarıldı, çünkü D/3'ün tek
sayısal ayrıntısıydı.

**Ölçü** (`_e5_sc_sayim.py`, 2. bölüm): sorunun ayırt edici ögeyi tanımlayan bir
ibare taşıyıp taşımadığını kaba bir sözcük alanıyla saydım — **6 → 4**. Düşen iki
soru tam olarak düzeltilen ikisi. Kalan dördünde (practice sa-6 `knows`, AC2-20
`split`/`two`, AC4-22 `green`, GT1-27 `leave`) ibare **kaldırılamıyor**, çünkü
kanıt cümlesinin kendi içeriği onu taşıyor: GT1-27'nin kanıtı zaten "işten ayrılan
çalışanın izin karşılığı" cümlesidir. Ölçü kaba, çünkü alan sözcüğünün bulunması
sızıntının kanıtı değil — AC2-20'de soru `split between two` diyor ama model yine
de `separate` vermedi.

### Elenen 7 soru — sızıntı cevabın kendisinde

| Soru | Cevap | Modelin verdiği | Neden düzeltilemez | E6'ya önerilen yeni çapa |
|---|---|---|---|---|
| practice sc-3 | `anatomy` | anatomy · morphology · anatomy | Tek sözcüklü cevap ve o sözcük sızıntı noktası; "bir türün beden yapısı" İngilizcede birden çok eş adla anılıyor | H/1'in içgörü ölçütünü sayan yarısı (hatasız ve ani çözüm, yeni nesnelere uyarlama, aletin yeri) |
| practice sc-12 | `ongoing research` | preliminary ×3 | Cevabın **bütün** içeriği başka bir sözcükle karşılandı; "bitmiş sonuç değil" karşıtlığı kanıt cümlesinin kendisi | H/1'in ikinci yarısı: her kuşak aracın öncekinin göremediğini bulması |
| practice sa-6 | `transactive memory system` | transactive memory ×3 | Eksen bir **kuramı adıyla** sormak; transaktif bellek örgüt psikolojisinin en çok atıf yapılan kavramlarından | H'nin ölçüsel iddiaları: yalnız bireysel çıktıya göre ödeme, ya da faydanın **daha az** kesintiyle artması |
| AC3 sc-22 | `mountaineers` | climbers ×3 | ONE WORD ONLY + tam eş anlamlı; kavramın birbirinin yerine geçen birden çok adı var | Yakutat'ın çıkış noktası olması, ya da yamaçların gevşek enkazla maskelenmesi |
| AC4 sc-22 | `vegetation` | vegetation · foliage · vegetation | Kelime düzeyinde bile 2/3 sızdırıyor; "karın örttüğü yeşillik" çok adlı | H/1'in son yarısı (yalnız sakinleştirici etkinin ayakta kalması) ya da H/2'deki örneklem sınırları |
| GT1 sc-27 | `final salary` | final pay ×3 | Ayırt edici sözcük (`final`) birebir tutturuldu; ayrılışta ödenen şeyin son maaş olması çalışma hayatının standardı | D/1: en çok beş günün yazılı onayla devri ve 31 Mart'ta yanması |
| GT2 sc-25 | `probationary period` | probation period ×3 | Aynı kelimenin başka çekimi, yani cevap tam tutturuldu; "başvurudan önce ne tamamlanmalı" işe alma dünyasının yerleşik kuralı | Haftada en çok üç gün sınırı, ya da müşteriyle çalışan roller istisnası |

Yedisi de `status: "rejected"` + `reject_reason` aldı, dosyalarında **numaralarıyla
duruyor** ve `content/DOGRULAMA/yeniden-uretim-listesi.json` dosyasına eklendi
(liste 43 → **50** kayıt). Her kayıt kanıt cümlesini ve soru metnini `kacinilacak`
altında, önerilen yeni çapayı `neden_elendi` içinde taşıyor.

### Dokunulmayan 6 soru — kelime düzeyinde çalışan sorular

Altısında da model yalnız baş adı verdi; ayırt edici niteleyici hiç gelmedi,
yani bu cevabı yazan aday puan alamaz. Baş ad ise zorunlu, dolayısıyla düzeltme
yarım kalırdı.

| Soru | Cevap | Modelin verdiği | Baş adı zorunlu kılan rol |
|---|---|---|---|
| practice sc-2 | `sensory contact` | contact | açık hortum ucunun nesneyle ilişkisi → `contact` |
| practice sc-4 | `running seawater` | seawater | ahtapot tankına ne verildiği → `seawater` |
| practice sc-6 | `unique individual` | individual | "birini tek tek ayırt etmek zorunda değil" → `individual` |
| practice sc-7 | `laboratory tank` | laboratory | "hiçbir X bunu tam taklit edemez" (bilim metni) → laboratuvar |
| AC2 sc-20 | `separate laboratories` | laboratories | eski DNA'nın çıkarıldığı yer → `laboratories` |
| GT2 sc-26 | `home-office equipment` | office equipment | uzaktan çalışmada masrafı geri alınan şey → `equipment` |

Altısına da `review_note` yazıldı (bulgu + baş adı zorunlu kılan rol + E6 için
somut yeni çapa önerisi), `status` `flagged` kaldı. Bu, 4. çalıştırmanın 11 soru
için verdiği kararın aynısı ve aynı gerekçeye dayanıyor.

### 🔴 E6 ve E7'ye devir notları

1. **Tamamlama ailesinde üretim kuralı artık iki maddeli.** 4. çalıştırma
   "boşluk, İngilizcede tek karşılığı olan bir kavramı hedeflemesin" demişti. Bu
   çalıştırma ikincisini ekliyor: **boşluğun ayırt edici ögesi tek başına bir
   niteleyici olmasın.** `running seawater`, `separate laboratories`,
   `home-office equipment` gibi öbeklerde baş ad çerçeveden okunuyor ve soru
   yalnız niteleyiciyi sınıyor; sayı, tarih, özel ad ve kapalı liste isteyen
   boşluklar bu kusuru taşımıyor.
2. **🔴 AC4 cümle tamamlama artık dört yuvanın üçü elenmiş durumda** (20 ve 21
   4. çalıştırmadan, 22 buradan); ayakta kalan tek soru 19. E6 A11 pasajından üç
   yeni soru yazarken üçünü de **ayrı paragraflara** çapalamalı; 20 ile 21'in
   kanıt cümleleri (hava değerleri ve "the passage of time") listede
   `kacinilacak` altında, 22'ninki H/1.
3. **Elenen yedi yuvanın yedisine de somut yeni çapa önerisi yazıldı** ve
   `neden_elendi` alanında duruyor. practice cümle tamamlamada iki yuva birden
   elendi (3 ve 12) ama iki ayrı pasajdan (A01, A04), çakışma yok.
4. **Düzeltilen 2 soru ölçülmemiş sorudur.** `answer`, `accepted_variants` ve
   `evidence` korundu ama soru metinleri baştan yazıldı; ikisinde de
   `blind_solvable: null` duruyor. E7 ikisini de yeniden ölçmeli.
5. **AC1-20 için set düzeyinde bir kalıntı risk var.** Aynı dosyadaki 21. soru
   ("A change in which animal held the **stronger position** …") baskınlık
   sözlüğünü sette tutuyor; 20'nin metninden kazanma/üstünlük dilini kaldırmak
   bu ipucunu kaldırmıyor. 21 `verified` ve `blind_solvable: false` olduğu için
   ona dokunmadım, ama E7 ölçümünde ikisi birlikte bakılmalı.
6. **AC1-19'un `difficulty` etiketi `easy` kaldı.** Düzeltme soruyu kesinlikle
   zorlaştırdı, ama zorluk etiketini ölçüm olmadan yeniden vermek tahmin olurdu;
   korunan alan olarak bıraktım. E7 ölçümünden sonra yeniden verilmeli.
7. **Dokunulmayan 6 soru bir sonraki turda da işaretli görünecek.** 4.
   çalıştırmanın 11'i ile birlikte tamamlama ailesinde 17 soru bu durumda. Karar
   tartışmaya açık; gerekli bilgi (bulgu, zorunluluk gerekçesi, önerilen çapa)
   her birinin `review_note` alanında duruyor, E6 isterse kapsama alabilir.

### Doğrulama

```
python tools/_e5_sc_kapsam.py            # kapsam: 26 isaretli, 15'i E10 kokenli
python tools/_e5_sc_elden_gecir.py       # duzeltildi 2 - elendi 7 - dokunulmadi 6
python tools/_e5_sc_devir.py             # eklenen kayit 7 - toplam 50
python tools/_e5_sc_sayim.py             # ayirt edici oge 8/15, zorunlu bas ad 13/15
python tools/_e5_sc_dogrula_degisim.py   # sinanan alan 433 - KORUNAN ALAN HATASI: 0
python tools/dogrula.py
```

- `answer`, `accepted_variants`, `evidence`, `evidence_locator`, `difficulty` ve
  `passage_id` sekiz dosyanın hepsinde **hiç değişmedi** (HEAD ile alan alan
  karşılaştırıldı, 433 sınamada 0 fark). Üst düzeyde `instructions`,
  `word_limit`, `question_type` ve `stem_block` de korundu.
- Düzeltilmeyen 45 sorunun soru metni **harfi harfine aynı** kaldı; bu ayrıca
  sınanıyor. Düzeltilen 2 sorunun eski metni `revision.onceki_prompt` içinde
  saklandı.
- Soru sayısı ve numaralar değişmedi: 8 dosyada 47 soru girdi, 47 çıktı. On iki
  tam testin hepsi 40/40 kaldı.
- `isaretli (flagged)` 71 → **62** (2 verified + 7 rejected; dokunulmayan 6 soru
  `flagged` kaldı).
- Şema hatası **0**; iki düzeltilen sorunun `explanation` alanı İngilizce yazıldı,
  `revision`, `reject_reason` ve `review_note` gibi iç denetim notları Türkçe
  kaldı.
