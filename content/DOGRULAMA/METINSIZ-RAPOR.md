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

---

## 4 — matching-features + matching-sentence-endings (2026-08-07)

### Özet

| Paket | Soru | 3/3 bilinen | Oran | Resmî taban | Sapma |
|---|---|---|---|---|---|
| matching-features | 26 | 18 | %69 | 3/4 (%75) | tabanın **altında** |
| matching-sentence-endings | 10 | 10 | **%100** | 3/3 (%100) | tabana **eşit** |
| **Toplam** | **36** | **28** | **%78** | — | — |

Bu çalıştırmada script hiçbir tipe 🔴 (tabandan belirgin sapma) koymadı: her iki tip
de resmî tabanın altında ya da tam üzerinde. Ama bu iki tipin resmî tabanı zaten çok
yüksek (%75 ve %100) — yani bunlar **doğaları gereği** parçasız bilinebilen tiplerdir.
Aşağıdaki bulgular "kural ihlali" değil, "tabanın niye bu kadar yüksek olduğunun"
bizim havuzumuzdaki karşılığıdır.

Turlar kararlı: matching-features'ta 26 sorunun 24'ünde (%92), sentence-endings'te
10/10'unda üç turda da aynı harf verildi. Sonuç şansa dayanmıyor.

---

### 4.1 — matching-features: 18/26 (%69)

#### Set bazında dağılım — asıl bulgu burada

| Set | Soru | 3/3 bilinen | Oran |
|---|---|---|---|
| practice | 10 | 4 | %40 |
| AC1 | 4 | 3 | %75 |
| AC2 | 4 | **4** | **%100** |
| AC3 | 4 | **4** | **%100** |
| AC4 | 4 | 3 | %75 |
| **sınav setleri (AC1-AC4)** | **16** | **14** | **%88** |

🔴 Uçurum paketin içinde: **practice %40, sınav setleri %88.** Aynı soru tipi, aynı
depo, iki katı fark. Yani bu tipin "doğası gereği bilinebilir" olması bir bahane
değil — kendi practice dosyamız aynı tipte %40 tutturuyor, demek ki daha iyisi
mümkün ve elimizde zaten örneği var.

#### Kusur 1 — ifade, seçeneğin **tanımını** yeniden söylüyor

Sınav setlerinde parçasız bilinen soruların çoğunda ifade bir **bulgu** değil,
seçeneğin kendi tanımının başka sözcüklerle yazılışı:

| Soru | İfade | Seçenek | Neden parçasız çıkıyor |
|---|---|---|---|
| AC1-25 | "no way at all of sensing the other animal" | B: *solid screen* | Opak bölme = hiçbir şey algılanamaz. Tanım. |
| AC1-26 | "being able to see… was on its own not enough" | A: *see-through screen* | "See" sözcüğü tek adayı gösteriyor. |
| AC2-24 | "this **wide area**" | C: *the Fertile Crescent* | Listede tek "geniş alan" o. |
| AC3-26 | "this **settlement on the shore**" | A: *Yakutat* | Listede tek yerleşim o. |
| AC3-23 | "the slopes standing **over it**" | D: *Hubbard Glacier* | Yamacın altında kalan tek şey buzul. |

Ortak mekanizma: **seçenek listesi tür bakımından karışık** (bir yerleşim, iki dağ,
bir buzul, bir sıradağ / şeffaf bölme, opak bölme, buluşma günleri, iki 7. gün
grubu). İfadedeki tek bir sözcük ("area", "settlement", "over it", "see") seçeneğin
**türünü** seçiyor, içeriğini değil. Aday parçayı okumadan eleyebiliyor.

#### Kusur 2 — genel kültürle bilinen özel adlar

AC2'nin 4 sorusunun 4'ü bilindi. Karacadağ–einkorn bağı (25) ve tarımın Avrupa'ya
yayılması (26) ders kitabı bilgisi; `general_knowledge` etiketiyle geldi. AC4'te
POMS'un olumsuz duygu durumlarını, PANAS'ın hem olumlu hem olumsuzu ölçtüğü ve
POMS'tan kısa olduğu (24, 26) yayımlanmış ölçek tanımıdır — parçaya gerek yok.

Seçenekler gerçek ve tanınmış adlarsa (yer, ölçek, kişi), soru parçanın ne dediğini
değil adayın o adı tanıyıp tanımadığını ölçer.

#### Direnen 8 soru ne yapıyor — kopyalanacak olan bu

practice'te kaçırdığım 6 soru (2, 3, 4, 6, 7, 8) hep **sonuç sorularıydı**: hangi
düzen en çok algılanan verimlilik artışı getirdi, hangi grup ağırlıkça en çok atıldı.
Bunlar ancak parçadaki sayıyla bilinir. Üstelik iki practice setinde de bir seçenek
**iki kez** doğru, bir seçenek **hiç** doğru değil (set 1: A×2, B×2, C hiç; set 2:
E×2, B hiç). Üç turda da "her harf bir kez" varsayıp eledim ve altısını birden
kaçırdım. Sınav setlerinde (AC1-AC3) ise her harf tam bir kez doğru — eleme çalışıyor.

Direnen diğer iki soru aynı kalıpta: AC1-24 (önce geri çekilen hayvanın sonradan
üstün gelmesi) ve AC4-23 (deneyin en çarpıcı sonucu) — ikisi de bulgu sorusu.

#### Dürüst bir kayıt

AC3-24 ve AC3-25, iki dağ arasında (King George / Logan) %50'lik bir elemeyle geldi;
3. turda `guess` yazıldı ve yine tuttu. Script kuralı gereği ikisi de işaretlendi,
ama bu iki işaret diğerlerinden **daha zayıf** kanıta dayanıyor. Raporun bu satırı
sonradan bakan için burada duruyor.

---

### 4.2 — matching-sentence-endings: 10/10 (%100)

Tek dosya (practice), 10 soru, hepsi üç turun üçünde de bilindi. Resmî taban da 3/3
(%100) olduğu için script sapma işareti koymadı — ama ölçüm yine de bir şey söylüyor:
**`general_knowledge` bir kez bile kullanılmadı.** Dayanak dağılımı `logic` 21,
`option_wording` 9. Yani sorular konuyu bilmekle değil, **cümlenin kendi dilbilgisi
ve anlam örgüsüyle** çözüldü.

Mekanizma: her kökün içinde, yalnız tek bir sonu seçen bir **anahtar sözcük** var.

| Kök | Anahtar | Son |
|---|---|---|
| "counted as **self**-directed because" | self | E: *aimed at the whale's **own body*** |
| "mark applied just behind an **eye or an ear** because" | görülemeyen bölge | B: *no way of seeing that patch **unaided*** |
| "a **clear panel** was lowered **instead of** the mirror because" | kontrol koşulu | A: *reacting simply to an **unfamiliar object*** |
| "rare in Bulgaria… **whereas**" | karşıtlık + ülke | D: *Germany and Norway* |
| "had to be **left out** of the analysis because" | eksik veri | B: *had not supplied full details* |

Kullanılmayan çeldiriciler (F, G, H) her iki sette de gerçek birer parça bilgisi gibi
yazılmış — ama **hiçbir kökün** anlamına ya da dilbilgisine oturmuyorlar. Çeldirici,
yanlış olduğu için değil, **hiçbir yere takılamadığı** için eleniyor. Gerçek sınavda
çeldirici en az iki köke makul biçimde takılır; ayrım parçadadır.

Bu tipte resmî taban da %100 olduğu için "bozuk" demek fazla iddialı olur; doğru
ifade şu: **bu tipin bilinen zaafı bizim setimizde de aynen mevcut** ve
`option_wording` payının %30 olması bunun **düzeltilebilir** kısmını gösteriyor.

---

### `basis` dağılımı

matching-features (78 cevap):

| Dayanak | Sayı | Oran |
|---|---|---|
| general_knowledge | 30 | %38 |
| logic | 30 | %38 |
| option_wording | 14 | %18 |
| guess | 4 | %5 |

matching-sentence-endings (30 cevap):

| Dayanak | Sayı | Oran |
|---|---|---|
| logic | 21 | %70 |
| option_wording | 9 | %30 |
| general_knowledge | 0 | %0 |
| guess | 0 | %0 |

İki tip birbirinin tersi: matching-features'ta ağırlık **konu bilgisinde** (özel adlar,
tanınmış ölçekler), sentence-endings'te tamamen **yazımda**. İkincisi prompt düzeyinde
kapatılabilir bir kusurdur, birincisi konu/seçenek seçimini gerektirir.

`guess` oranı %5 — 3. çalıştırmanın %0'ından sonra ilk kez sıfırın üstünde. Küçük ama
gerçek bir işaret: bu pakette gerçekten bilinemeyen sorular var.

---

### Düzeltme yönü (bu rapor uygulamıyor, işaret ediyor)

1. **Seçenek listesini tür bakımından türdeş yap.** Hepsi yerleşim, ya da hepsi dağ
   olsun; "bir kasaba + iki dağ + bir buzul + bir sıradağ" karışımı, ifadedeki tek
   sözcüğün cevabı vermesine yol açıyor (AC2, AC3).
2. **İfade, seçeneğin tanımını tekrarlamasın.** "Hiçbir şey algılayamayan grup" = opak
   bölme, tanımdır. Bunun yerine o grubun parçada yazan **sonucunu** sor (AC1-25,
   AC1-26).
3. **Sonuç sorusu yaz, tanım sorusu değil.** Direnen 8 sorunun 8'i de sonuç sorusuydu;
   kalıp elimizde, sınav setlerine taşınması yeterli.
4. **Tekrarı ve kullanılmayan seçeneği sınav setlerine de taşı.** practice'te bir
   harfin iki kez doğru olması eleme stratejisini kırdı ve altı soruyu birden korudu;
   AC1-AC3'te her harf tam bir kez doğru ve eleme çalışıyor. `NB You may use any letter
   more than once` notu AC4'te zaten var, diğerlerine de eklenebilir.
5. **Tanınmış özel adları soru eksenine koyma.** Karacadağ–einkorn, POMS/PANAS
   tanımları gibi ders kitabı bilgileri cevabı parçasız veriyor; soru o adın parçadaki
   **özel ayrıntısına** bağlansın.
6. **Sentence-endings'te çeldirici en az iki köke takılabilsin.** Şu anda F, G, H
   hiçbir köke oturmadığı için dilbilgisiyle eleniyor; ayrım parçaya taşınmalı.
7. **Kökteki anahtar sözcüğü sonda tekrarlama.** "self-directed → own body",
   "eye or ear → seeing that patch unaided" eşleşmeleri sözcük düzeyinde; eşanlamlıyı
   sondan kaldırıp ayrımı parçaya bırak.

### Ölçülmeyenler

- `matching-features` yalnız okuma tarafında ölçüldü; dinleme bu adımın kapsamı dışında
  (prompt gereği).
- `matching-sentence-endings` sınav setlerinde (AC1-AC4, GT1-GT2) **yok**; yalnız
  practice dosyası var, ölçüm 10 soruyla sınırlı kaldı.
- Diyagram etiketleme bu pakette yok; görsel gerektiren tiplerde bu ölçüm kördür.

### Yapılan işaretleme

- matching-features: 26 sorunun **18'ine** `blind_solvable: true`, `blind_basis`,
  `status: "flagged"`, `flag_reason`; **8'ine** `blind_solvable: false`.
- matching-sentence-endings: 10 sorunun **10'una** `blind_solvable: true` + flag.
- Toplam 36 soru işlendi, **28 işaretlendi**. **Hiçbir soru silinmedi**; soru sayıları
  değişmedi.

---

## 5 — matching-information (2026-08-07)

### Özet

| Paket | Soru | 3/3 bilinen | Oran | Resmî taban |
|---|---|---|---|---|
| matching_information | 49 | **3** | **%6** | resmî listede yok — ayrı ölçülmedi |

**Bu, ölçümün beş çalıştırmasındaki en düşük oran.** Karşılaştırma için: yes-no-not-given
%100, multiple-choice %100, matching-sentence-endings %100, matching-features %69,
true-false-not-given %53, matching-headings %18, matching-information **%6**. Genel resmî
ortalama %57 idi; bu paket onun çok altında.

Resmî tabanda bu tip yok, o yüzden script sapma işareti koyamadı. Ama tabana gerek de
kalmıyor: %6, bu ölçüm için zaten şans seviyesine yakın bir sonuç.

### Sonucun şans seviyesiyle karşılaştırması

7 dosyanın 5'inde seçenekler A–H (8 seçenek, 35 soru), GT1 ve GT2'de A–E (5 seçenek,
14 soru). Rastgele işaretlemenin tur başına beklenen isabeti:

    35 × 1/8 + 14 × 1/5 = 7.2 / 49 → **%14.6**

Gerçekte tur başına isabet **40/147 (%27.2)** çıktı — şansın 1.9 katı. Yani parçasız
çözümde sıfır bilgi yok, ama bilgi **soruyu tutturmaya yetmiyor**: üç turun üçünde
birden tutan yalnız 3 soru kaldı.

| Kaç turda doğru | Soru |
|---|---|
| 0 | 24 |
| 1 | 13 |
| 2 | 9 |
| 3 | **3** |

### Tur kararlılığı: %16 — ölçümün gördüğü en düşük değer

49 sorunun yalnız **8'inde** üç tur aynı harfi verdi.

| Paket | Tur kararlılığı |
|---|---|
| yes-no-not-given | %100 |
| multiple-choice | %100 |
| matching-sentence-endings | %100 |
| matching-features | %92 |
| true-false-not-given | %88 |
| matching-headings | %60 |
| **matching-information** | **%16** |

Bu rakam tek başına paketin durumunu özetliyor. Yüksek kararlılık, "her turda aynı yere
götüren kuralcı bir işaret" demekti (3. çalıştırmanın notu). %16 bunun tersi: **cevaplar
turdan tura savruluyor, çünkü tutunacak bir işaret yok.** İfade, hangi paragrafta
olduğunu ele veren biçimsel bir imza taşımıyor.

### Set bazında dağılım

| Set | Soru | 3/3 bilinen | Oran |
|---|---|---|---|
| practice | 15 | 1 | %7 |
| AC1 | 5 | 0 | %0 |
| AC2 | 5 | 0 | %0 |
| AC3 | 5 | 2 | %40 |
| AC4 | 5 | 0 | %0 |
| GT1 | 7 | 0 | %0 |
| GT2 | 7 | 0 | %0 |

🟢 GT1 ve GT2'de **0/14**. Bu, önceki dört çalıştırmanın en ısrarlı bulgusunun tersine
dönmesi demek: TFNG'de GT2 %71, çoktan seçmelide GT setleri %100 idi ve sebep hep aynıydı
— "gündelik hayatın varsayılan kuralı parçayı gereksiz kılıyor". Burada ilan metinlerine
sorulan şey kural değil, **hangi ilanda geçtiği**; hayat bilgisi hangi ilan olduğunu
söylemiyor. Aynı GT malzemesiyle sağlam soru yazmanın mümkün olduğunun kanıtı.

### İşaretlenen 3 soru ve tek gerçek sızıntı

| Soru | Anahtar | İfade | Dayanak |
|---|---|---|---|
| practice 6 | H | "an admission that the work has not yet been examined by other specialists" | logic |
| AC3 28 | H | "a warning against assuming that the same thing happened to other victims" | logic |
| AC3 29 | E | "measurements showing that preserved nerve fibres were close in width to those of a living person" | guess |

İlk ikisi aynı mekanizma: **sınırlılık beyanı son paragrafta durur.** "Henüz hakem
değerlendirmesinden geçmedi", "bu bulgu başkalarına genellenemez" — bilimsel bir yazının
bu iki hamlesi hemen her zaman kapanış paragrafındadır. Parçayı okumaya gerek yok, yazı
türünün iskeleti yetiyor. İkisinde de üç turda da H yazıldı, üçünde de tuttu.

⚠️ Üçüncüsü (AC3-29) **daha zayıf kanıta dayanıyor**: üç turda da `guess` etiketiyle E
verildi, "ölçüm sonucu → bulgular bölümü → orta-geç paragraf" akıl yürütmesiyle. Script
kuralı gereği işaretlendi, ama bu bir sızıntıdan çok 1/8'lik bir isabetin üst üste
gelmesi. Bu satır sonradan bakan için burada duruyor.

### Aynı sızıntının hafif hâli: 2/3'te kalan sorular

Dokuz soru üç turun ikisinde tutturuldu. Yedisi aynı kalıpta — **yazının sonuna doğru
duran retorik hamleler**:

| Soru | Anahtar | Hamle |
|---|---|---|
| practice 5 | G | ihtiyatlı bir tarihsel tahmin ("may once have been harder to tell apart") |
| practice 10 | G | genelleyici çıkarım (yakınsak evrim savı) |
| AC1 30 | G | daha geniş sonuç ("mercandan başka canlılar da bağlı") |
| AC2 27 | F | bulgu rakamı |
| AC3 27 | B | arka plan / keşif tarihi |
| AC4 27 | D | yöntem ayrıntısı |
| GT1 3 | C | — (ilan, kalıp yok) |

Yani giriş→arka plan→yöntem→bulgu→yorum→sınırlılık dizilişi **kısmen** tahmin
edilebiliyor. Ama kısmen: aynı akıl yürütme 24 soruda üç turun üçünde de ıskaladı. Bu,
düzeltilmesi gereken bir kusur değil, tipin doğal alt sınırı — gerçek sınavda da böyle
paragraf konumu tahmini bir miktar işe yarar.

### `basis` dağılımı

Üç turun tamamı (147 cevap):

| Dayanak | Sayı | Oran |
|---|---|---|
| guess | 89 | %61 |
| logic | 58 | %39 |
| general_knowledge | 0 | **%0** |
| option_wording | 0 | **%0** |

Bu tablo ölçümün en temiz sonucu. Önceki dört çalıştırmada rapora ayrı ayrı not düşülen
iki kusur burada **hiç görünmüyor**:

- **`option_wording` = 0.** Seçenekler harf (A–H / A–E); yazılabilecek bir çeldirici
  metni yok, dolayısıyla "doğru şık ölçülü, çeldirici mutlak" imzası bu tipte
  yapısal olarak imkânsız. YNNG ve çoktan seçmelide paketi tek başına çökerten kusur
  buydu.
- **`general_knowledge` = 0.** Hiçbir soruda konu bilgisi işe yaramadı. İfadeler
  parçanın **ne söylediğini** değil **nerede söylediğini** sorduğu için, dışarıdan
  bilinen hiçbir şey cevabı vermiyor. matching-features'ta %38 olan bu pay burada sıfır.

`guess` %61 ile ölçümün gördüğü en yüksek değer (önceki en yüksek: matching-features %5,
çoktan seçmelide %0). Cevapların çoğu gerçekten tahmindi.

### Zorluk etiketiyle ilişki

| Etiket | Soru | 3/3 bilinen |
|---|---|---|
| easy | 12 | 0 |
| medium | 30 | 3 |
| hard | 7 | 0 |

İşaretlenen üç sorunun üçü de `medium`. `easy` etiketli 12 sorunun hiçbiri parçasız
bilinemedi — yani "kolay" etiketi burada "bulunması kolay" demek, "bilinmesi kolay"
değil. Bu doğru kullanım.

### İzlenecek küçük bir eğilim (kusur değil)

Dört akademik setin (AC1–AC4) **dördünde de** beş cevap arasında hem A hem H tam bir kez
bulunuyor, ve hiçbir harf tekrar etmiyor. Rastgele dağılımda dört setin dördünde birden
A+H çıkma olasılığı ≈ %1.6. Aday bunu bilerek kullanamaz (istatistiği görmesi gerekir),
o yüzden bu ölçümde bir sızıntı üretmedi — ama üretim promptu ilk ve son paragrafa
sistematik olarak birer soru bağlıyor gibi görünüyor. GT setlerinde böyle bir düzen yok
(harfler tekrar ediyor, `NB You may use any letter more than once` notu da orada).

### Düzeltme yönü (bu rapor uygulamıyor, işaret ediyor)

Bu paket için ağır bir düzeltme listesi çıkmıyor; iki küçük madde var:

1. **Sınırlılık/kapsam uyarısı sorusunu son paragrafa bağlama.** "Henüz hakem
   incelemesinden geçmedi", "başkalarına genellenemez" gibi ifadeler her metinde
   kapanışa denk geldiği için parçasız bilinebiliyor (practice 6, AC3 28 — işaretlenen
   üç sorunun ikisi). Bu hamleyi taşıyan paragraf yazının ortasına da konabilir, ya da
   soru o uyarının **içeriğine** (hangi koşul, hangi grup) bağlanabilir.
2. **A ve H'yi her akademik sette birer kez doğru yapma alışkanlığını kır.** Şu an 4/4;
   dağılımı serbest bırakmak yeter.

### Kopyalanacak olan

Bu paket, önceki dört çalıştırmanın düzeltme listelerinin **zaten uygulanmış hâli** gibi
duruyor ve sebebi tipin kendisinde:

- Soru, parçanın bir **iddiasını** değil bir **konumunu** soruyor. Genel kültür konum
  bilgisi vermiyor.
- Seçenekler metin değil harf. Çeldirici yazımı diye bir yüzey yok, dolayısıyla kip
  imzası sızdıramıyor.
- İfadeler parçanın kendi ayrıntısına bağlanmış: "717,7 nanometre", "ilk aylarda
  üretilenin hesap dışı bırakılması", "iki panel önünde geçirilen toplam süre". 1. ve
  4. çalıştırmanın "ifadeyi parçanın kendine özgü sayısal/koşullu ayrıntısına bağla"
  önerisinin uygulanmış hâli budur.

GT1/GT2'nin 0/14'ü ayrıca şunu gösteriyor: GT malzemesi (ilanlar, el kitapları) doğası
gereği bozuk soru üretmiyor — 1. ve 3. çalıştırmadaki GT sorunu **soru kurgusundan**
geliyordu, malzemeden değil.

### Ölçülmeyenler

- Dinleme tarafı bu adımın kapsamı dışında (prompt gereği).
- Diyagram etiketleme bu pakette yok; görsel gerektiren tiplerde bu ölçüm kördür ve o
  tip geldiğinde **"ölçülmedi"** olarak geçilecek.

### Araç notu

4. adım (işaretleme) mevcut `tools/_b1_isaretle.py` ile yapıldı; bu çalıştırmada araca
bir şey eklenmedi. Script rapor JSON'undaki 3/3 bilinen kimlikleri okuyup orijinal
dosyalara `blind_solvable` / `blind_basis` / `status` / `flag_reason` yazıyor,
`blind_basis` olarak üç turdaki en sık dayanağı seçiyor ve hiçbir soruyu silmiyor.

### Yapılan işaretleme

49 sorunun **3'üne** orijinal dosyasında `blind_solvable: true`, `blind_basis`,
`status: "flagged"` ve `flag_reason` yazıldı; **46'sına** `blind_solvable: false`.
**Hiçbir soru silinmedi**; soru sayısı 49'da sabit.

---

## 6 — note-completion + table-completion (2026-08-07)

- Ölçülen soru: **45** (6 dosya — note-completion 33, table-completion 12)
- Üç turun üçünde de parçasız bilinen: **13** — **%28.9**
- Üç turda aynı cevabın verildiği soru: 25/45 (%56) — önceki beş çalıştırmanın en
  düşüğü. Beklenen bir sonuç: burada şık yok, aday boşluğa **kelime** yazıyor; aynı
  anlamı farklı kelimeyle vermek mümkün olduğu için turlar doğal olarak ayrışıyor.

### Tip bazında

| Soru tipi | Bizde | Oran | Resmî taban | Sapma |
|---|---|---|---|---|
| note_completion | 9/33 | %27 | 6/6 (%100) | tabanın **altında** |
| table_completion | 4/12 | %33 | 0/5 (%0) | 🔴 tabanın **üstünde** |

🔴 **table_completion tek uyarı veren tip.** Resmî örneklemde tablo tamamlama 0/5 ile
diyagram etiketlemeyle birlikte en sızıntısız tipti; bizde %33. Sebebi aşağıda ayrı
başlıkta — kısaca: **bizim tablo hücrelerimiz veri değil cümle.**

⚠️ İki taban da küçük: resmî taraf tip başına 5-6 soru, bizim table_completion
örneklemimiz 12 soru. %33 ile %0 arasındaki fark 4 soruya dayanıyor; yön güvenilir,
büyüklük değil.

note_completion tersi yönde: %27 ile hem kendi resmî tabanının (6/6) hem genel resmî
ortalamanın (%57) belirgin altında. Resmî 6/6 rakamı altı soruya dayandığı için
gerçekçi bir tavan değil, ama yön açık: not tamamlama bu pakette sağlam çalışıyor.

### Set bazında dağılım

| Set | Tip | Soru | 3/3 bilinen | Oran |
|---|---|---|---|---|
| practice | note | 15 | 2 | %13 |
| AC1 | note | 6 | 2 | %33 |
| AC4 | note | 6 | 2 | %33 |
| GT1 | note | 6 | 3 | **%50** |
| AC3 | table | 6 | 2 | %33 |
| GT2 | table | 6 | 2 | %33 |

practice (%13) en sağlamı; 15 sorunun 13'ü parçasız bilinemedi. GT1 (%50) yine zayıf
halka — 1. ve 3. çalıştırmadaki GT bulgusunun tekrarı. Ama 5. çalıştırmada GT setleri
0/14 ile en temiz sonuçtu; yani sorun GT **malzemesinde** değil, GT malzemesine
sorulanın çoğu zaman "kural" olmasında. Kural, hayat bilgisiyle biliniyor.

### İşaretlenen 13 soru

| Soru | Anahtar | Zorluk | Dayanak |
|---|---|---|---|
| practice 1 | `47` | easy | general_knowledge |
| practice 10 | `500` | easy | general_knowledge |
| AC1 4 | `tyre` | medium | general_knowledge |
| AC1 5 | `corner` | medium | logic |
| AC4 4 | `headphones` | easy | logic |
| AC4 5 | `novelty` | hard | guess |
| GT1 15 | `noticeboard` | easy | logic |
| GT1 16 | `staggered` | medium | logic |
| GT1 19 | `28 days` | easy | general_knowledge |
| AC3 1 | `acrylic` | easy | guess |
| AC3 6 | `right eye` | hard | general_knowledge |
| GT2 16 | `CV` | easy | logic |
| GT2 20 | `mentor` | hard | logic |

Onuüçünün de üç turda **aynı kelime** yazıldı — hiçbirinde üçte bir isabetin üst üste
gelmesi gibi bir şans açıklaması yok. Bu tipte tahmin uzayı sınırsız olduğu için
(şık yok, kelime yazılıyor) 3/3 tutturmak çoktan seçmelideki 3/3'ten çok daha güçlü
bir kanıt.

### İki sızıntı mekanizması

Onuüç sorunun tamamı iki kalıptan birine giriyor.

**1. Eşdizim kilidi (8/13) — boşluk kalıp bir İngilizce öbek dizisinin içinde duruyor,
cümle iskeleti kelimeyi zaten söylüyor.**

| Boşluklu çerçeve | Kilitlenen kelime |
|---|---|
| "hidden round a …" | corner |
| "put on …" (ofiste) | headphones |
| "a … effect" | novelty |
| "put up on the staff …" | noticeboard |
| "breaks are … so that no line is left uncovered" | staggered |
| "a clear … screen" | acrylic |
| "an up-to-date …" (başvuru) | CV |
| "a … from the intern's own department sees them once a week" | mentor |

Bunların hiçbirinde parçayı okumak gerekmiyor; boşluğun **iki yanındaki kelimeler**
cevabı tek bir seçeneğe indiriyor. Bu, düzeltilebilir bir kusur — aynı bilgi için
boşluk öbeğin öbür ucuna taşınabilir ("hidden round a corner" → `corner` yerine
`hidden`; "breaks are staggered" → `staggered` yerine bu düzenin **sebebi**).

**2. Dünya bilgisi (5/13) — boşluktaki değer parçaya değil dünyaya ait bir sabit.**

- `47` — Japonya'nın il sayısı.
- `500` — piroklastik akış sıcaklığı olarak her kaynakta geçen değer.
- `28 days` — Birleşik Krallık'ta tam zamanlı yıllık izin, resmî tatiller dâhil.
- `tyre` — fil araç kullanımı deneyinin yayımlanmış ayrıntısı.
- `right eye` — dişli balinalarda bilinen yanallık.

Bunlar da düzeltilebilir: aynı cümlede parçaya özgü olan başka bir değer var
(kaç ülke, kaç dakika, hangi ölçüm); boşluk oraya taşınırsa soru parçasız
çözülemez hale gelir.

### Neden table_completion tabanın üstünde — hücre cümleye dönünce

İşaretlenen dört tablo sorusunun ikisi (GT2 16 `CV`, GT2 20 `mentor`) tam cümle
hücrelerinde: "Form filled in online, an up-to-date (16) …, and 300 words on why you
want the placement." Bu bir tablo hücresinden çok bir not satırı. Cümle olunca
eşdizim kilidi devreye giriyor.

Aynı dosyada **sayısal** boşluklar hiç bilinemedi: AC3 4 (`kaç ziyaret`), AC3 5
(`ne kadar süre`), GT2 18 (`kabul için kaç gün`) — üçü de 0/3. Resmî tablo
tamamlamanın 0/5 olmasının sebebi tam da bu: resmî tabloda hücreler **veri**
(sayı, birim, ad, tarih), cümle değil. Bizim dört işaretimizin dördü de veri
olmayan hücrelerden geldi.

Yani sapma tipin kendisinden değil, tipin **yazılışından** geliyor — ve bu, bu
raporun çıkardığı en somut düzeltme.

### 2/3'te kalan sorular: yanlış değil, eşanlamlı

Sekiz soruda turların biri ya da ikisi tuttu. Hepsinde kaçırılan tur **anlamca doğru
ama kelimece yanlış** bir cevap verdi:

| Soru | Anahtar | Kaçıran turun cevabı |
|---|---|---|
| practice 6 | small sample | small group |
| AC1 2 | bamboo | wood |
| AC4 1 | reconfigure | rearrange |
| GT1 17 | card reader | time clock / clocking-in machine |
| GT1 18 | shift-swap form | shift change form |
| GT1 20 | staff portal | booking system |
| GT2 15 | sponsorship | a visa |
| GT2 17 | video interview | telephone interview |

Bu tablo tipin **savunma mekanizmasını** gösteriyor. Anlam yuvası parçasız
kestirilebiliyor, ama "parçadan kelime al" kuralı kestirmeyi cevaba çevirmiyor.
Yani `NO MORE THAN TWO WORDS **from the passage**` kısıtı boş bir biçimsellik değil,
ölçünün taşıyıcı kolonu. Bu bir kusur değil, korunacak özellik.

### `basis` dağılımı

Üç turun tamamı (135 cevap):

| Dayanak | Sayı | Oran |
|---|---|---|
| guess | 64 | %47 |
| logic | 44 | %33 |
| general_knowledge | 27 | %20 |
| option_wording | 0 | **%0** |

**`option_wording` = %0, yapısal olarak.** Bu tipte şık yok; yazılmış bir çeldirici
metni olmadığı için "doğru şık ölçülü, çeldirici mutlak" imzası imkânsız. 2. ve 3.
çalıştırmada (YNNG, çoktan seçmeli) paketi tek başına çökerten kusur buydu; tamamlama
tiplerinde hiç doğmuyor.

Yalnız işaretlenen 13 sorunun 39 cevabına bakılırsa dağılım tersine dönüyor:

| Dayanak | Sayı | Oran |
|---|---|---|
| logic | 18 | %46 |
| general_knowledge | 15 | %38 |
| guess | 6 | %15 |

Yani sızıntının ana kanalı `logic` — ve bu tipte `logic` demek "şıkları eledim"
değil, **"cümle çerçevesi kelimeyi zaten söylüyor"** demek. Eşdizim kilidi
bulgusunun sayısal karşılığı bu satır.

### Zorluk etiketiyle ilişki

| Etiket | Soru | 3/3 bilinen | Oran |
|---|---|---|---|
| easy | 15 | 7 | %47 |
| medium | 20 | 3 | %15 |
| hard | 10 | 3 | **%30** |

`easy` → `medium` düşüşü beklenen yönde. Ama `hard` etiketli 10 sorunun 3'ü
parçasız bilindi (AC4 5 `novelty`, AC3 6 `right eye`, GT2 20 `mentor`) — `medium`'un
iki katı. Bu üçü de eşdizim ya da dünya bilgisi kilidi taşıyor; yani "hard"
etiketi burada **kelimenin parçada bulunmasının zorluğunu** ölçmüş, kelimenin
bilinmesinin zorluğunu değil. Önceki çalıştırmalarda etiket temizdi; burada
üç satırlık bir tutarsızlık var.

### Düzeltme yönü (bu rapor uygulamıyor, işaret ediyor)

1. **Tablo hücresini cümle yazmayı bırak.** table_completion'da boşluk sayı/birim/ad/
   tarih hücresine gelsin. İşaretlenen 4 tablo sorusunun 4'ü de cümle hücresinden,
   sayısal hücrelerin 0'ı sızdırdı. Tek başına bu değişiklik tipi tabanın altına
   indirir.
2. **Boşluğu eşdizimin tahmin edilen ucuna koyma.** "hidden round a …", "put on …",
   "a … effect", "an up-to-date …" gibi çerçevelerde boşluk öbeğin öbür ucuna ya da
   cümlenin parçaya özgü kısmına taşınsın.
3. **Dünya sabitini boşluk yapma.** 47 (il sayısı), 500 (°C), 28 days (yasal izin) —
   üçü de parçadan bağımsız doğrular. Aynı cümledeki parçaya özgü değer boşluk
   yapılsın (practice 1'de "23 further countries" gibi).
4. **Üç `hard` etiketini gözden geçir.** AC4 5, AC3 6, GT2 20 parçasız çözüldüğü için
   `hard` sıfatını hak etmiyor.

### Korunacak olan

- **`from the passage` kısıtı.** 2/3 tablosu bunun tek başına sekiz soruyu kurtardığını
  gösteriyor.
- **Sayısal boşluklar.** AC3 4-5, GT2 18, practice 7-8 — hepsi 0/3. Parçaya özgü ölçüm
  ve tarih dışarıdan bilinemiyor.
- **practice dosyasının kurgusu (%13).** On beş sorunun on üçü dayandı.

### Ölçülmeyenler

- Dinleme tarafı bu adımın kapsamı dışında (prompt gereği). `note-completion` ve
  `table-completion` dinleme dosyaları script tarafından "okuma değil" diye atlandı.
- **Diyagram etiketleme: ölçülmedi.** Bu pakette bulunmuyor; görsel gerektiren tiplerde
  metin tabanlı bu ölçüm kördür ve 8. çalıştırmada da "ölçülmedi" olarak geçilecek.

### Araç notu

4. adım (işaretleme) bu çalıştırmada mevcut `tools/_b1_isaretle.py` yerine aynı mantığı
uygulayan tek seferlik bir betikle yapıldı: rapor JSON'undaki 3/3 bilinen kimlikler
orijinal dosyalara `blind_solvable` / `blind_basis` / `status` / `flag_reason` olarak
yazıldı, `blind_basis` olarak üç turun en sık dayanağı seçildi, hiçbir soru silinmedi. Yazım
sonrası tüm dosyalarda soru sayısı ve `answer` alanları git'teki önceki hâliyle
karşılaştırılarak doğrulandı (6/6 dosya değişmemiş). Özet istatistikler
`tools/_b1_metinsiz6_ozet.py` ile üretildi.

### Yapılan işaretleme

45 sorunun **13'üne** orijinal dosyasında `blind_solvable: true`, `blind_basis`,
`status: "flagged"` ve `flag_reason` yazıldı; **32'sine** `blind_solvable: false`.
**Hiçbir soru silinmedi**; soru sayısı 45'te sabit.

---

🔴 Son söz: **bu ölçüm bozuk soruyu bulur, zorluk seviyesini ölçmez.** "Bu soru gerçek
sınav zorluğunda" demek ancak binlerce gerçek adayın verisiyle mümkündür.
