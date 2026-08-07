# Parçasız çözüm ölçümü — toplu rapor

Her okuma sorusu, **okuma parçası ve cevap anahtarı hiç görülmeden** üç ayrı turda
cevaplandı. Üç turun üçünde de doğru bilinen soru "parçasız çözülebilir" sayıldı.

🔴 Bu ölçüm **bozuk soruyu** bulur, **zorluk seviyesini ölçmez.**

Karşılaştırma tabanı: aynı ölçüm resmî sınav sorularına uygulandığında **%57'si**
parçasız bilinebiliyordu. Bu yüzden mutlak eşik yok; her tip kendi resmî tabanıyla
karşılaştırılır. Resmî taban küçük örnekleme dayanır (tip başına 3-6 soru), kesin
eşik değil yön verir.

---

## 1 — true-false-not-given (2026-08-07)

- Ölçülen soru: **57** (7 dosya)
- Üç turun üçünde de parçasız bilinen: **30** — **%52.6**
- Üç turda aynı cevabın verildiği soru: 50/57 (%88) — turlar kararlı, sonuç şansa
  dayanmıyor.

### Tip bazında

| Soru tipi | Bizde | Oran | Resmî taban | Sapma |
|---|---|---|---|---|
| true_false_not_given | 30/57 | %53 | 3/3 (%100) | tabanın **altında** |

Bu pakette tek soru tipi var. Oranımız (%53) resmî tabanın (%100) belirgin
**altında**; ölçümün "belirgin üstünde" uyarısı bu tipte tetiklenmedi. Resmî taban
yalnız 3 soruya dayandığı için %100 rakamı gerçekçi bir tavan değil — asıl okunacak
sonuç, TFNG sorularımızın parçasız bilinme oranının genel resmî ortalamanın (%57)
biraz altında kalmasıdır.

### Set bazında dağılım

| Set | Soru | 3/3 bilinen | Oran |
|---|---|---|---|
| practice | 15 | 8 | %53 |
| AC1 | 7 | 6 | **%86** |
| AC2 | 7 | 4 | %57 |
| AC3 | 7 | 1 | %14 |
| AC4 | 7 | 2 | %29 |
| GT1 | 7 | 4 | %57 |
| GT2 | 7 | 5 | %71 |

🔴 **AC1 (6/7) ve GT2 (5/7)** bu paketin zayıf halkaları. AC1'de konu genel kültürde
çok bilinen bir vaka; parçaya bakmadan doğru bilinen 6 sorunun 5'i `general_knowledge`
ile geldi. GT2'de ise ifadeler günlük hayatın varsayılan kuralıyla örtüşüyor (ilan
metinlerinde beklenen: erken bilet daha ucuz, yazılı uyarı verilir), yani soru
parçadan değil hayat bilgisinden çözülebiliyor.

AC3 (%14) ve AC4 (%29) tersi yönde iyi örnek: ifadeler parçanın kendi ayrıntısına
bağlı, dışarıdan bilinemiyor.

### Cevap anahtarına göre dağılım

| Anahtar | Toplam | 3/3 bilinen | Oran |
|---|---|---|---|
| TRUE | 24 | 15 | %63 |
| FALSE | 17 | 8 | %47 |
| NOT GIVEN | 16 | 7 | %44 |

TRUE cevaplı sorular en kolay tahmin edilenler — beklenen bir sonuç, çünkü doğru
ifade genellikle dünyaya dair makul olanla örtüşür. Uçurum büyük değil; NOT GIVEN
ve FALSE ayrımı parçasız yapılamıyor, bu iyi işaret.

### `basis` dağılımı

Üç turun tamamı (171 cevap):

| Dayanak | Tüm cevaplar | Yalnız işaretli sorularda (90 cevap) |
|---|---|---|
| general_knowledge | 78 (%46) | 54 (%60) |
| logic | 47 (%27) | 21 (%23) |
| guess | 37 (%22) | 9 (%10) |
| option_wording | 9 (%5) | 6 (%7) |

`option_wording` düşük (%5–7). Yani sorular **çeldirici yazımından** ele vermiyor;
ifadeler "fazla mutlak / fazla ayrıntılı" gibi biçimsel ipucu taşımıyor. Bu, düzeltmesi
en zor kusurun bu havuzda küçük olduğu anlamına gelir.

İşaretli soruların baskın dayanağı `general_knowledge` (%60). Bu düzeltilebilir bir
kusur değil, **konu seçimiyle** ilgili: ünlü vakalar (AC1) ve gündelik hizmet
ilanları (GT2) doğal olarak dışarıdan bilinir. Düzeltme yolu, ifadeyi parçanın
kendine özgü sayısal/koşullu ayrıntısına bağlamaktır.

### Ölçülmeyenler

Diyagram etiketleme bu pakette yok. Görsel gerektiren tiplerde metin tabanlı bu ölçüm
kördür ve o tipler geldiğinde **"ölçülmedi"** olarak geçilecektir.

### Yapılan işaretleme

30 soruya orijinal dosyasında `blind_solvable: true`, `blind_basis`, `status: "flagged"`
ve `flag_reason` yazıldı. Kalan 27 soruya `blind_solvable: false`. **Hiçbir soru
silinmedi**, soru sayısı 57'de sabit.

---

## 2 — yes-no-not-given + matching-headings (2026-08-07)

Bu çalıştırmada iki paket birlikte ölçüldü. Sonuçlar birbirinin tam zıddı çıktı, o yüzden
ayrı ayrı okunmalı.

### Özet

| Paket | Soru | 3/3 bilinen | Oran | Resmî taban |
|---|---|---|---|---|
| yes_no_not_given | 23 | **23** | **%100** | ayrı ölçülmedi (en yakını TFNG 3/3) |
| matching_headings | 45 | 8 | %18 | 4/4 (%100) — tabanın **çok altında** |

---

### 2.1 — yes-no-not-given: 23/23 🔴🔴

**Bu paketin tamamı parçaya bakmadan bilindi.** Üç turun üçünde de aynı cevap verildi
(23/23 kararlılık) ve üçünde de doğruydu.

| Set | Soru | 3/3 bilinen | Oran |
|---|---|---|---|
| practice | 15 | 15 | %100 |
| GT1 | 4 | 4 | %100 |
| GT2 | 4 | 4 | %100 |

| Anahtar | Toplam | 3/3 bilinen | Oran |
|---|---|---|---|
| YES | 10 | 10 | %100 |
| NO | 7 | 7 | %100 |
| NOT GIVEN | 6 | 6 | %100 |

Sonucun şans olmadığı ayrıca sınandı: aynı cevaplar bir kademe kaydırılarak
(YES→NO→NOT GIVEN) puanlandığında **0/23** çıkıyor, yani puanlayıcı ayırt ediyor;
anahtar da dengeli (10 YES / 7 NO / 6 NOT GIVEN), tek cevaba yığılmış değil.

#### Kusurun tam yeri: cevap ifadenin **kipinde** kodlanmış

Üç cevabın her biri, içerikten bağımsız bir yazım imzası taşıyor:

- **NOT GIVEN olanların hepsi**, çalışmanın ekseni dışında bir boyut açıyor: çalışmada
  olmayan bir karşılaştırma grubu (tamamen uzaktan çalışan şirketler; kadın-erkek; yaşlı-genç),
  çalışma sonrası bir eylem (tasarımın kampüse yayılması), ölçülmemiş bir neden (tarih
  etiketleri) ya da bir politika önerisi ("Governments **should**…"). Dördü de klasik
  "eksen dışı" NG kalıbı.
- **NO olanların hepsi** bir mutlaklık/eşitleme sözcüğü taşıyor: "**clearly** improved",
  "**failed** to produce a clear ordering", "in **much the same way**", "made **no
  difference**", "serves **as well as**", "**should** be counted as genuine", "explain
  **most** of".
- **YES olanların hepsi** ölçülü, değerlendirici ve akademik varsayılan duruşla uyumlu:
  "widely shared view", "**may** understate", "a **plausible** one", "unusual scientific
  strength".

Yani aday parçayı değil, **cümlenin kipini** okuyarak cevaplıyor: ölçülü→YES,
mutlak→NO, eksen dışı→NOT GIVEN. Bu, konu seçiminden gelen bir kusur değil, **üretim
promptunun cümle yazımından** gelen bir kusur — ve tam da bu yüzden düzeltilebilir.

#### 1. çalıştırmayla karşıtlık, bulguyu doğruluyor

Aynı aileden olan true-false-not-given'da oran %53'tü. Fark tesadüf değil: TFNG ifadeleri
parçanın **kendi olgusuna** (sayı, tarih, koşul) bağlanıyor; YNNG ifadeleri ise "yazar ne
düşünüyor"u sorduğu için doğal olarak retorik kiple yazılıyor ve kip ele veriyor.

#### Düzeltme yönü (bu rapor uygulamıyor, işaret ediyor)

1. YES cevaplı ifadeleri de zaman zaman mutlak, NO cevaplı ifadeleri de zaman zaman ölçülü
   yaz — kip ile cevap arasındaki bağı kopar.
2. NOT GIVEN'ı "eksen dışı boyut" ile üretmeyi bırak; parçanın **gerçekten değindiği** bir
   konuda, ama yazarın tavrını belirtmediği bir noktada üret.
3. NO'yu tek bir niteleyici sözcükle değil, parçadaki somut bir ifadeyle çelişerek kur.

### 2.2 — matching-headings: 8/45 (%18)

| Set | Soru | 3/3 bilinen | Oran |
|---|---|---|---|
| AC1 | 5 | 0 | %0 |
| AC2 | 5 | 1 | %20 |
| AC3 | 5 | 1 | %20 |
| AC4 | 5 | 2 | %40 |
| GT1 | 5 | 1 | %20 |
| GT2 | 5 | 0 | %0 |
| practice | 15 | 3 | %20 |

Resmî tabanda başlık eşleştirme parçasız bilinmenin **en yüksek** olduğu tiplerden biriydi
(4/4). Bizde %18. Ölçümün "tabanın belirgin üstünde" uyarısı tetiklenmedi; tersine, bu tip
bu havuzda tabanın çok altında.

Tur kararlılığı da bunu destekliyor: 45 sorunun yalnız **27'sinde** üç tur aynı cevabı
verdi (%60). YNNG'de bu oran %100'dü. Başlık listeleri parçasız **çözülemiyor**; verilen
cevaplar turdan tura kayıyor.

Bilinen 8 sorunun büyük kısmı, paragrafın **makale iskelesindeki yerinden** çıkarılabilen
başlıklar: B paragrafı için "Why the usual approach did not work" (AC3), "Finds whose
identity was still an open question" (AC2); son paragraflar için sonuç cümlesi biçimindeki
başlıklar (AC4 "Calmer but not more energetic", practice "What the length of the rest did
not explain"). Yani giriş→yöntem→sonuç dizilişi tahmin edilebiliyor. 8/45'te kaldığı için
bu bir paket kusuru değil, izlenecek bir eğilim: **sonuç bildiren başlıkları** listenin
sonuna denk getirmemek bu payı daha da düşürür.

### `basis` dağılımı ve dürüst bir sınır

| Dayanak | yes-no-not-given (69 cevap) | matching-headings (135 cevap) |
|---|---|---|
| logic | 35 (%51) | 135 (%100) |
| general_knowledge | 29 (%42) | 0 |
| option_wording | 5 (%7) | 0 |
| guess | 0 | 0 |

⚠️ **Bu tablo YNNG'de kusuru olduğundan küçük gösteriyor.** Yukarıda anlatılan kip imzası
biçimsel bir ipucudur, yani gerçekte `option_wording` sayılmalıydı; turlarda çoğu kez
`logic` olarak etiketlendi. Etiketleme kararı ölçümden önce verildiği için sonradan
düzeltilmedi — ama raporun okunuşu şudur: **YNNG'deki asıl mekanizma çeldirici/ifade
yazımıdır**, %7'lik `option_wording` rakamı değil.

### Araçta düzeltilen bir eksik

`tools/metinsiz-kopya.py` parçasız kopyaya **başlık listesini taşımıyordu**; başlıklar
`option_list` alanında duruyor, script ise yalnız `instructions`/`options`/`items`
kopyalıyordu. Bu haliyle başlık eşleştirme "hiç seçenek verilmeden" ölçülürdü ve çıkan
düşük oran sorunun değil kopyanın eksiğinin sonucu olurdu. Script, seçenek listelerini
(cevap ve parça izi temizlenmiş olarak) kopyaya yazacak biçimde düzeltildi ve ölçüm
düzeltilmiş kopyayla yapıldı.

Etkisi: 1. çalıştırma (true-false-not-given) **etkilenmedi** — o tipte `option_list` yok,
seçenekler sabit TRUE/FALSE/NOT GIVEN. Düzeltme asıl 4. çalıştırmayı (matching-features,
matching-sentence-endings) da kurtarır; `option_list` taşıyan dosyalar bunlar.

### Ölçülmeyenler

Diyagram etiketleme bu iki pakette yok. Görsel gerektiren tiplerde bu ölçüm kördür,
geldiğinde **"ölçülmedi"** olarak geçilecek.

### Yapılan işaretleme

- yes-no-not-given: **23** soruya `blind_solvable: true` + `status: "flagged"` +
  `flag_reason`. `blind_solvable: false` yazılan soru yok.
- matching-headings: **8** soru işaretlendi, **37** soruya `blind_solvable: false`.

**Hiçbir soru silinmedi**; soru sayıları 23 ve 45'te sabit.

---

## 3 — multiple-choice (+ multiple-choice-multi) (2026-08-07)

### Özet

| Paket | Soru | 3/3 bilinen | Oran | Resmî taban |
|---|---|---|---|---|
| multiple_choice | 30 | **30** | **%100** | resmî listede yok — ayrı ölçülmedi |
| multiple-choice-multi | 0 | — | — | **ölçülmedi**: okuma tarafında dosya yok |

`multiple-choice-multi` yalnız `content/listening/practice/` altında var; dinleme bu
adımın kapsamı dışında olduğu için bu paket ölçülmedi. Okuma tarafındaki çoktan seçmeli
sorular — tek cevaplı da, iki cevaplı da — `multiple-choice.json` dosyalarında duruyor
ve hepsi aşağıdaki 30 sorunun içinde.

### 3.1 — multiple-choice: 30/30 🔴🔴🔴

**Paketin tamamı parçaya bakmadan bilindi.** 7 dosya, 30 soru, üç turun üçünde de aynı
cevap, üçünde de doğru.

| Set | Soru | 3/3 bilinen | Oran |
|---|---|---|---|
| practice | 12 | 12 | %100 |
| AC1 | 3 | 3 | %100 |
| AC2 | 3 | 3 | %100 |
| AC3 | 3 | 3 | %100 |
| AC4 | 3 | 3 | %100 |
| GT1 | 3 | 3 | %100 |
| GT2 | 3 | 3 | %100 |

#### Bu sonuç şansla açıklanamaz

30 sorunun 21'i tek cevaplı (A–D, şans 1/4), 9'u iki cevaplı (A–G içinden İKİ harf, şans
1/21; iki harfin ikisi de doğru olmadan soru doğru sayılmıyor). Tek bir turun tamamını
tutturma olasılığı:

    (1/4)^21 × (1/21)^9 ≈ 3 × 10⁻²⁵

Yani üç tur olmasa, tek tur bile tek başına belirleyiciydi.

⚠️ **Yöntem üstüne dürüst bir not:** üç tur kuralının işi, tek turda tutturulan şans
cevabını elemektir. Bu pakette üç tur da **birebir aynı** cevapları verdi (30/30
kararlılık), dolayısıyla 3/3 süzgeci burada ayırt edici çalışmadı — sonucu taşıyan şey
turların sayısı değil, yukarıdaki tek tur olasılığıdır. Kararlılığın kendisi de ayrı bir
bulgu: ipucu belirsiz bir sezgi değil, **her turda aynı yere götüren kuralcı bir işaret**.
(Karşılaştırma: matching-headings'te tur kararlılığı %60'tı, orada ipucu yoktu.)

Cevap anahtarı dengeli, yani sonuç "hep aynı harfi işaretledim" ucuzluğundan da gelmiyor:

| Harf | Tek cevaplı 21 soruda |
|---|---|
| A | 5 |
| B | 6 |
| C | 6 |
| D | 4 |

#### Kusur 1 — iki cevaplı sorularda A ve G **hiçbir zaman** doğru değil

9 iki-cevaplı sorunun 18 doğru harfinin dağılımı:

| Harf | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| Kaç kez doğru | **0** | 3 | 5 | 1 | 3 | 5 | **0** |

Listenin ilk ve son maddesi 9 soruda 9 kez de çeldirici. Dahası doğru **çift** de
tekrarlıyor: {C, F} 9 sorunun 4'ünde doğru cevap (practice 3-4, practice 7-8, AC1 34-35,
AC2 34-35), {B, E} 2'sinde. Aday üç soru gördükten sonra kalanları listeye bakmadan
işaretleyebilir. Bu, içerikten tamamen bağımsız, **konumsal** bir sızıntı.

#### Kusur 2 — doğru cevap ölçülü, çeldirici mutlak (2. çalıştırmadaki kusurun aynısı)

İki cevaplı 9 sorunun **hepsinde** doğru çift, ihtiyatlı/koşullu yazılmış iki maddeydi;
çeldiriciler mutlaklık taşıyordu. Örnekler:

| Soru | Doğru (ölçülü) | Çeldirici (mutlak) |
|---|---|---|
| practice 3-4 | "**probably** work together" · "**cannot yet** be excluded" | "is **essential**" · "changed **nothing at all**" · "gave the **sharpest** results" |
| practice 7-8 | "**may** have appeared earlier" · "**may** have been present" | "is **disproved**" · "was **unknown**" · "descends **directly**" |
| AC3 34-35 | "Carbon and oxygen dominate" · "A protein … was present" | "**Only one** protein" · "Chemistry **alone proved**" |

Bu, 2. çalıştırmada yes-no-not-given'da bulunan kusurun ta kendisi: **cevap, cümlenin
kipinde kodlanmış.** Orada ölçülü→YES / mutlak→NO idi; burada ölçülü→doğru şık /
mutlak→çeldirici. İki farklı soru tipinde aynı imzanın çıkması, bunun tek tek soruların
değil **üretim promptu ailesinin ortak alışkanlığı** olduğunu gösteriyor.

#### Kusur 3 — "Why does the writer…" soruları yazı geleneğiyle çözülüyor

practice 12, practice 15, AC2 32, AC2 33, AC3 32, AC3 33'te doğru şık, o hamlenin bir
bilim yazısındaki **olağan işlevini** söylüyor; çeldiriciler ise hiçbir yazarın
yapmayacağı işlevler öneriyor ("uydu fotoğraflarını şüpheye düşürmek", "kasabanın zengin
olduğunu ima etmek"). Parçayı okumaya gerek kalmıyor, tür bilgisi yetiyor. Aynı ailede
practice 15'te doğru şık listenin **en uzun ve en ayrıntılı** maddesi ("longer visits,
other seasons, other cultures") — klasik sınav-kurnazlığı ipucu; AC4 32 de öyle.

#### Kusur 4 — yöntem/tanım bilgisiyle çıkan sorular

- practice 6: "hexaploid" kelimesinin **tanımı** zaten "daha çok kromozom takımı" demek.
- practice 11: yörüngeden yeni hasarı görmenin yolu iki tarihli görüntüyü karşılaştırmaktır.
- practice 13: iki koşulun sırasını rastgelelemenin amacı sıra/alıştırma etkisini elemektir.
- AC4 33: nap–uyanık karşılaştırmasında iki grubun eşitlendiği şey bekleme süresidir.
- AC1 32: mercanın yanına gaz ulaşmasını açıklayan şey volkanik jeolojidir.

Bunlar çeldirici yazımı kusuru değil, **soru seçimi** kusuru: parçanın kendine özgü
bilgisini değil, alanın genel bilgisini soruyorlar.

#### Kusur 5 — GT setlerinde iş hayatının varsayılan kuralı

GT1 ve GT2'nin 6 sorusunun 6'sı da sıradan çalışan kurallarını yeniden söylüyor: kartını
unutan amirine söyler, vardiya değişimi iki vardiya arası dinlenmeyi kısaltıyorsa
reddedilir, fazla mesai önceden onay ister ve izne çevrilebilir, uzaktan çalışan belirli
saatlerde ulaşılabilir olur ve kalıcı adres değişikliğini bildirir, müşteriyle çalışan
ofiste daha çok bulunur. Hiçbir el kitabı bunun tersini yazmayacağı için parça gereksiz.
Bu, 1. çalıştırmada GT2 için (%71) not düşülen kusurun **daha ağır** hâli.

### `basis` dağılımı

Üç turun tamamı (90 cevap):

| Dayanak | Sayı | Oran |
|---|---|---|
| general_knowledge | 43 | %48 |
| logic | 24 | %27 |
| option_wording | 23 | %26 |
| guess | 0 | %0 |

`guess` **sıfır** — 90 cevabın hiçbirinde gerçekten tahmin edilmedi. Bu tek başına
paketin durumunu özetliyor.

`option_wording` %26 ile bu ölçümün şimdiye kadarki en yüksek değeri (TFNG %5,
YNNG %7). Bu iyi haber sayılır: `option_wording` **düzeltilebilir** bir kusurdur —
çeldiricilerin yazımıyla ilgilidir, konu seçimiyle değil. Kusur 1 ve 2 doğrudan bu
başlığa girer ve prompt düzeyinde kapatılabilir.

⚠️ 2. çalıştırmadaki uyarının aynısı burada da geçerli: `general_knowledge` etiketi bir
miktar şişkin. Özellikle GT sorularında "genel kültür" dediğim şey aslında seçeneklerin
hangisinin makul yazıldığı bilgisiydi; sınırı ölçüm sırasında çizmek zor oldu. Raporun
okunuşu: **bu paketteki asıl mekanizma seçenek yazımıdır.**

### Düzeltme yönü (bu rapor uygulamıyor, işaret ediyor)

1. İki cevaplı sorularda doğru harfleri listeye **rastgele** dağıt; A ve G'yi de doğru
   yap. Şu anda 18 doğru harfin 0'ı A/G.
2. {C, F} gibi tekrar eden doğru çiftleri kır.
3. Kip ile doğruluk arasındaki bağı kopar: doğru şıkkı da zaman zaman kesin ifadeyle,
   çeldiriciyi de zaman zaman ölçülü ifadeyle yaz. (YNNG için yazılan 1 numaralı öneriyle
   aynı; iki tipte tek düzeltme.)
4. "Why does the writer…" sorularında çeldiriciler de **yazının gerçekten yapabileceği**
   işlevler olsun; saçma işlev çeldirici değildir.
5. Doğru şıkkı en uzun madde yapma; şık uzunluklarını dengele.
6. Tanımdan/yöntem bilgisinden çıkan soruları (practice 6, 11, 13) parçanın kendi
   sayısal/koşullu ayrıntısına bağla.
7. GT setlerinde soruyu "kural ne olmalı"dan "**bu** el kitabında hangi eşik/süre/istisna
   yazıyor"a çevir.

### Ölçülmeyenler

- `multiple-choice-multi`: okuma tarafında dosya yok, **ölçülmedi**.
- Diyagram etiketleme bu pakette yok; görsel gerektiren tiplerde bu ölçüm kördür.

### Yapılan işaretleme

30 sorunun **30'una** orijinal dosyasında `blind_solvable: true`, `blind_basis`,
`status: "flagged"` ve `flag_reason` yazıldı. `blind_solvable: false` yazılan soru yok.
**Hiçbir soru silinmedi**; soru sayısı 30'da sabit.

---

🔴 Son söz: **bu ölçüm bozuk soruyu bulur, zorluk seviyesini ölçmez.** "Bu soru gerçek
sınav zorluğunda" demek ancak binlerce gerçek adayın verisiyle mümkündür.
