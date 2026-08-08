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
