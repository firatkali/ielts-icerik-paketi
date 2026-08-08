# Puanlama kalibrasyonu — SONUÇ (2026-08-09)

Bu dosya `prompts/OPUS5-A4-puanlama-duzeltmesi.md`'nin **son rapor çalıştırmasıdır**.
Bu çalıştırmada **hiçbir düzeltme yapılmadı**: `degerlendirme/` altındaki hiçbir dosyaya
dokunulmadı, `DEGISIKLIK-KAYDI.md`'ye yeni madde yazılmadı.

Bu aşamada **saklı küme yok** (A4 tablosu: son raporda hepsi görünür). Aşağıdaki her sayı
`tools/_a4_sonuc_son.py` tarafından ham puanlama dosyalarından hesaplandı; elle ortalama
alınmadı. Puanlar ürünün gerçek davranışıdır: her örneğin **tek seferlik (ilk) puanı**.
Tekrar ortalaması yalnız tutarlılık bölümünde kullanıldı ve orada ayrıca işaretlendi.

Konuşma tarafının ayrıntısı ayrı dosyada: **`SONUC-konusma.md`**.

---

## Ölçülen turlar

| Tur | Ne | Kapsam | Sınadığı |
|---|---|---|---|
| 1 | yazma, temel ölçüm | 21 örnek × 3 | talimatın ilk hâli |
| 2 | yazma | 23 örnek × 1 | 1. düzeltme (saklı küme S3) |
| 3 | yazma, **tamamlandı** | 23 örnek × 3 | 2. düzeltme (saklı küme S1) |
| 4 | **konuşma**, ilk ölçüm | 12 örnek × 6 | — (temel ölçüm) |
| 5 | **alt band turu** | gerçek bandı ≤4,5 olan 4 yazma örneği × 3 | 2. düzeltmenin alt banda etkisi |
| 6 | **doğrulama turu** | 24 yazma + 12 konuşma = 36 örnek × 1 | 3. düzeltme (saklı küme S2) |

Tur 3 önceki son rapor yazıldığında 23 örneğin 18'iyle duruyordu (`GT-T2` grubu oturum
limitine takılmıştı). O eksik **kapatıldı**: tur 3 artık 23 örnek × 3 = 69 puanlamadır ve
aşağıdaki bütün tur-3 sayıları tam kümedendir. Bu yüzden bu dosya bir öncekinin
güncellemesi değil, **yerine geçen sürümdür**.

---

## 1. Turların ölçüleri yan yana

**Her turun kendi örnek kümesi üzerinden** (`RAPOR-tur*.md` ile birebir aynı):

| Ölçü | tur 1 | tur 2 | tur 3 | tur 4 (konuşma) | tur 5 (alt band) | **tur 6 (doğrulama)** |
|---|---|---|---|---|---|---|
| n örnek | 21 | 23 | 23 | 12 | 4 | **36** |
| tekrar | 3 | 1 | 3 | 6 | 3 | 1 |
| Ortalama mutlak fark | 0,952 | 0,913 | 0,804 | 0,583 | 1,250 | **0,389** |
| Eğilim (+ cömert / − cimri) | −0,667 | −0,696 | −0,326 | −0,250 | **+1,250** | **−0,139** |
| En büyük tek sapma | 2,00 | 2,00 | 2,50 | 2,00 | 1,50 | **1,50** |
| Yayılım (tutarsızlık) | 0,33 | — ¹ | 0,28 | **0,79** | 0,25 | — ¹ |
| Verilen puanların aralığı | 4,5–7,0 | 3,5–7,0 | 4,5–7,5 | 4,5–8,5 | 4,5–5,5 | **3,5–8,5** |

¹ Tur 2 ve tur 6'da her örnek **1 kez** puanlandı; yayılım tanım gereği 0,00 çıkar.
`RAPOR-tur2.md` ve `RAPOR-tur6.md`'deki "✅ geçti" o satırda **anlamsızdır** — tutarlılık
o turlarda sınanmadı. Bkz. bölüm 3, ölçüt 4.

**Eşleşik karşılaştırma** — tur 1/2/3/6'nın **hepsinde** puanlanan aynı 21 yazma örneği.
Küme bileşimi farkını dışarıda bırakan, karşılaştırılabilir olan tablo budur:

| Ölçü | tur 1 | tur 2 | tur 3 | **tur 6** |
|---|---|---|---|---|
| Ortalama mutlak fark | 0,952 | 0,857 | 0,714 | **0,333** |
| Eğilim | −0,667 | −0,619 | −0,190 | **0,000** |
| En büyük tek sapma | 2,00 | 2,00 | 2,00 | **1,00** |

Dört turun hepsinde olmayan üç yazma örneğinin geçmişi (eşleşik tabloya girmedi):

| Örnek | Gerçek | tur 1 | tur 2 | tur 3 | tur 5 | tur 6 |
|---|---|---|---|---|---|---|
| AC-ER-T1-B | 4,0 | — | — | — | **+1,5** | **+0,5** |
| GT-T2-2B-B | 6,0 | — | −1,0 | −1,0 | — | **0,0** |
| GT-T2-2B-C | 8,5 | — | −2,0 | **−2,5** | — | **−1,0** |

**Alt band turu (5) → doğrulama turu (6), aynı 4 örnek:**

| Örnek | Gerçek | tur 5 verilen | tur 6 verilen |
|---|---|---|---|
| GT-T1-1B-A | 3,0 | 4,5 (+1,5) | **3,5 (+0,5)** |
| AC-ER-T1-B | 4,0 | 5,5 (+1,5) | **4,5 (+0,5)** |
| AC-T2-2A-A | 4,0 | 5,0 (+1,0) | **4,0 (0,0)** |
| GT-T2-2B-A | 4,0 | 5,0 (+1,0) | **4,5 (+0,5)** |
| **ortalama** | | **+1,25** | **+0,38** |

### Ne oldu — turdan tura

- **1. düzeltme (tur 1 → tur 2)** eğilimi hiç oynatmadı (−0,667 → −0,619 eşleşik).
  Yalnız dilbilgisi ölçütünü ve orta bandı düzeltti.
- **2. düzeltme (tur 2 → tur 3)** ölçeğin **tavanını açtı**: üst bandda (≥7) ortalama sapma
  −1,50'den −1,11'e, tutarlılık ölçütü −2,11'den −1,22'ye indi. Eğilim −0,619 → −0,190.
  Ama aynı değişikliklerin hiçbiri alt bandla sınırlı değildi ve **alt band bunun bedelini
  ödedi**: ≤4,5 aralığı +0,50'den +1,00'a çıktı, alt banda nişan alan tur 5'te **+1,25**.
  Gerçek bandı 3,0 olan cevap üründe 4,5 görünüyordu.
- **3. düzeltme (tur 3+5 → tur 6)** alt bandı, üst bandı bozmadan kapattı. Bu turun asıl
  sınavı buydu ve geçti.

### Band aralığı × ölçüt — yazma (tek seferlik puan; ölçüt bandı − gerçek genel band)

| Tur | Band | n | görev | tutarlılık | kelime | dilbilgisi | **genel** |
|---|---|---|---|---|---|---|---|
| 1 | ≥ 7 | 8 | −1,81 | −1,88 | −1,31 | −1,69 | **−1,56** |
| 1 | 5–6,5 | 10 | −0,20 | −0,20 | −0,50 | −0,90 | **−0,40** |
| 1 | ≤ 4,5 | 3 | +1,33 | +1,00 | +0,33 | +0,33 | **+0,83** |
| 3 | ≥ 7 | 9 | −1,44 | −1,22 | −1,00 | −1,22 | **−1,11** |
| 3 | 5–6,5 | 11 | −0,09 | +0,18 | −0,05 | −0,73 | **−0,05** |
| 3 | ≤ 4,5 | 3 | +1,33 | +1,33 | +0,33 | +0,33 | **+1,00** |
| 5 | ≤ 4,5 | 4 | +1,50 | +1,75 | +0,75 | +0,25 | **+1,25** |
| **6** | ≥ 7 | 9 | −0,56 | −0,56 | 0,00 | −0,89 | **−0,44** |
| **6** | 5–6,5 | 11 | 0,00 | +0,36 | +0,36 | −0,23 | **+0,18** |
| **6** | ≤ 4,5 | 4 | +0,50 | +0,75 | 0,00 | 0,00 | **+0,38** |

Üç aralık da ilk kez aynı anda ±0,5 bandın içinde. Ölçek artık iki uçtan da açık:
verilen puanlar 3,5 ile 8,5 arasında (tur 1'de 4,5–7,0 idi).

### 3. düzeltmenin tur 6'ya yazdığı beklentiler

| # | Beklenti | Sonuç |
|---|---|---|
| 1 | Alt band (≤4,5) +1,28 → **+0,50 içine** | ✅ **GEÇTİ** — +0,38 |
| 2 | Alt bandda tutarlılık +1,89 → **+0,75 içine**, görev +1,56 → **+0,75 içine** | ✅ **GEÇTİ** — tutarlılık +0,75 (tam sınırda), görev +0,50 |
| 3 | Gerçek bandı 3,0–4,0 olan örneklerin en az birinde **≤4,0** puan | ✅ **GEÇTİ** — iki örnekte: GT-T1-1B-A → 3,5 · AC-T2-2A-A → 4,0 |
| 4 | Üst band (≥7) **−1,10'un altına düşmemeli** (asıl risk) | ✅ **GEÇTİ, hem de iyileşti** — −1,11 → −0,44 |
| 5 | Orta band (5–6,5) **−0,35'in dışına çıkmamalı** | ✅ **GEÇTİ** — −0,05 → +0,18 |
| 6 | Yazma eğilimi **−0,25 ile +0,10 arasında** | ✅ **GEÇTİ** — −0,021 |
| 7 | Saklı küme farkı **açılmamalı** (tur 3'te 0,25) | 🔴 **KALDI** — 0,292. Bölüm 2 |
| 8 | Konuşma dokunulmadığı için sabit kalmalı: MAE 0,583 ± 0,15 | ✅ toplamda geçti (0,458) ama **ölçüt düzeyinde kaydı** — bkz. `SONUC-konusma.md` |

Sekiz beklentinin altısı temiz geçti, biri sınırda, biri kaldı. Kalan (7) ezber şüphesidir
ve bir sonraki bölümün konusudur.

---

## 2. Saklı küme ile açık küme karşılaştırması

Kurulum: her düzeltme örneklerin üçte birini **hiç görmedi**; sonraki tur o kümeyi sınadı.
Açık kümede iyi + saklı kümede kötü = düzeltme örneklere ezberlenmiş demektir.

| Düzeltme | SAKLI küme | Sınayan tur | Saklı (n, ort. mutlak) | Açık (n, ort. mutlak) | **Fark** |
|---|---|---|---|---|---|
| 1. | S3 | tur 2 | 7 · 0,857 | 16 · 0,938 | **0,080** |
| 2. | S1 | tur 3 | 8 · 0,750 | 15 · 0,833 | **0,083** |
| 3. | **S2** | **tur 6** | 12 · **0,583** | 24 · **0,292** | **0,292** |

İlk iki düzeltmede saklı küme **açık kümeden iyi** çıktı; orada ezber yok. Üçüncüsünde
yön tersine döndü ve fark üç katına çıktı.

### 🔴 3. DÜZELTMENİN AYARI ÖRNEKLERE EZBERLENMİŞ OLABİLİR.

Saklı küme S2, doğrulama turunda açık kümelerin **iki katı** sapıyor (0,583 / 0,292).
Bu, önceki iki turda görülmeyen bir örüntüdür ve raporun **büyük harfle yazılması gereken**
tek bulgusudur. Beceriye ayırınca fark iki tarafta da duruyor, yani tek bir beceriden
gelmiyor:

| Beceri | S2 (saklı) | S1+S3 (açık) | Fark |
|---|---|---|---|
| yazma | 8 · 0,562 | 16 · 0,250 | 0,312 |
| konuşma | 4 · 0,625 | 8 · 0,375 | 0,250 |

**Karşı kanıt — kaydedilmesi gereken, ama şüpheyi kaldırmayan:**

1. **S2 zaten en zor kümedir ve görünürken de en kötüydü.** Küme bazında ortalama mutlak fark:

   | Tur | S1 | S2 | S3 | S2 o turda görünür müydü? |
   |---|---|---|---|---|
   | 1 | 1,000 | 0,857 | 1,000 | (düzeltme öncesi) |
   | 2 | 0,875 | **1,000** | 0,857 | **görünürdü** (1. düzeltme S1+S2 gördü) |
   | 3 | 0,750 | **1,125** | 0,500 | **görünürdü** (2. düzeltme S2+S3 gördü) |
   | 4 | 0,875 | 0,625 | 0,250 | görünürdü |
   | 6 | 0,333 | **0,583** | 0,250 | **saklıydı** |

   S2, kendisini **gören** iki düzeltmenin ardından da üç kümenin en kötüsüydü (tur 2 ve
   tur 3). Ezber varsayımı bunu açıklamaz: ezberlenmiş bir küme görünürken **iyi** çıkardı.

2. **Farkın kaynağı içerik olarak belli.** S2, ölçekteki en zor iki yazma örneğini
   (GT-T2-2B-C 8,5 · GT-T2-2A-B 8,0), projenin baştan beri kapanmayan tek yazma sapmasını
   (AC-T1-1C-A) ve konuşmadaki iki büyük sapmadan birini (SP-band7_5-1) taşıyor. S2'nin
   toplam 7,0 bandlık mutlak sapmasının **4,0'ı bu dört örnekten** geliyor; onlar
   çıkarılınca kalan sekiz örneğin ortalaması 0,375'e iniyor.

3. **Kümeler tek seferlik puanla, 12 örnekle ölçülüyor.** Bir örneğin 0,5 band oynaması
   küme ortalamasını 0,042 oynatır; 0,292'lik fark, S2'nin **yedi örneğinin yarımşar band
   düzelmesine** eşittir. Bu büyüklükte bir farkı gürültüden ayırmak 12 örnekle mümkün değil.

**Karar:** bu veri ezberi ne kanıtlıyor ne de eliyor. Fark yönü yanlış, büyüklüğü şüphe
uyandırmaya yeter, ama alternatif açıklama (küme zorluğu) daha iyi destekleniyor. Doğru
davranış bunu **açık bir risk olarak taşımaktır** — bkz. bölüm 5, risk 1. Ayırt etmenin tek
yolu **yeni, hiç görülmemiş örneklerle** ölçüm yapmaktır; mevcut 36 örnek bunu yapamaz.

---

## 3. Başarı ölçütleri — tek tek

Doğrulama turu (tur 6), 36 örnek, tek seferlik puan:

| Ölçüt | Hepsi (n=36) | Yazma (n=24) | Konuşma (n=12) |
|---|---|---|---|
| Ortalama mutlak fark < 0,5 band | ✅ **0,389** | ✅ 0,354 | ✅ 0,458 |
| Hiçbir örnekte ≥ 1,5 band sapma yok | 🔴 **KALDI** — 2 örnek | ✅ en büyük 1,00 | 🔴 **KALDI** — 2 örnek |
| Eğilim ±0,25 band içinde | ✅ **−0,139** | ✅ −0,021 | 🔴 **KALDI** — −0,375 |
| Aynı cevaba verilen puanların yayılımı ≤ 0,5 | ⚪ **ÖLÇÜLMEDİ** | ⚪ ÖLÇÜLMEDİ | ⚪ ÖLÇÜLMEDİ |

**Ölçüt 1 — geçti.** Ortalama mutlak fark 0,952'den 0,389'a indi; eşleşik 21 yazma örneğinde
0,952 → 0,333.

**Ölçüt 2 — kaldı, ve kalan iki örnek de konuşmadır.** SP-band7_5-1 (7,5 → 6,0) ve
SP-band8-2 (8,0 → 6,5). Yazmada ≥1,5 sapan örnek **kalmadı** (tur 1'de 7/21 idi). Ayrıntı
`SONUC-konusma.md`.

**Ölçüt 3 — toplamda geçti, konuşmada kaldı.** Yazmanın eğilimi pratik olarak sıfır
(−0,021). Konuşma −0,375 ile cimri tarafta ve tur 4'e göre (−0,250) **kötüleşti**.

**Ölçüt 4 — 🔴 bu turda ölçülmedi, "geçti" sayılamaz.** Tur 6'da her örnek **bir kez**
puanlandı; yayılım tanım gereği 0,00 çıkar. `RAPOR-tur6.md`'nin o satırdaki "✅ geçti"si
bir ölçüm değil, aritmetik bir zorunluluktur. Tutarlılığın **gerçekten** ölçüldüğü son
turlar:

| Tur | Ne | Tekrar | Yayılım | Sonuç |
|---|---|---|---|---|
| 3 | yazma | 3 | 0,28 (11/23 örnek oynadı, en fazla 1,0) | ✅ geçti |
| 5 | yazma, alt band | 3 | 0,25 (2/4 örnek oynadı) | ✅ geçti |
| 4 | **konuşma** | 6 | **0,79 (11/12 örnek oynadı, ikisi 1,5)** | 🔴 **KALDI** |

Yani: **yazmanın tutarlılığı 3. düzeltmeden önce ölçüldü ve geçiyordu; konuşmanınki
ölçüldü ve kaldı; 3. düzeltmeden sonra ikisi de yeniden ölçülmedi.** Tekrarlı bir konuşma
turu bu projenin en öncelikli eksiğidir.

---

## 4. Ürünün gerçek davranışı — tek seferlik puanların dağılımı

Kullanıcı ortalama görmez; **tek bir puan** görür. Doğrulama turunda o tek puanın gerçek
banda göre dağılımı:

| Fark | Kaç örnek (36) | Yazma (24) | Konuşma (12) |
|---|---|---|---|
| −1,5 | 2 | 0 | 2 |
| −1,0 | 1 | 1 | 0 |
| −0,5 | 11 | 7 | 4 |
| **0,0** | **14** | 9 | 5 |
| +0,5 | 7 | 6 | 1 |
| +1,0 | 1 | 1 | 0 |

| | Hepsi | Yazma | Konuşma | (karşılaştırma: tur 3 yazma) |
|---|---|---|---|---|
| Tam isabet | 14/36 (%39) | 9/24 (%38) | 5/12 (%42) | 3/23 (%13) |
| 0,5 band içinde | **32/36 (%89)** | 22/24 (%92) | 10/12 (%83) | 12/23 (%52) |
| 1,0 band içinde | 34/36 (%94) | **24/24 (%100)** | 10/12 (%83) | 20/23 (%87) |
| ≥1,5 band sapma | 2/36 | **0/24** | 2/12 | 3/23 |
| Cömert / tam / cimri | 8 / 14 / 14 | 7 / 9 / 8 | 1 / 5 / 6 | 7 / 3 / 13 |

**Kullanıcı tarafından okunuşu:**

- Tipik kullanıcı **doğru bandı ya da yarım band komşusunu** alıyor (%89).
- Yazmada, on kullanıcıdan onu **1,0 bandın içinde** puan alıyor; 1,5 band veya daha fazla
  sapma yazmada artık **hiç görülmüyor**.
- Kalan iki büyük sapmanın ikisi de konuşmadadır ve ikisi de **cimri** yöndedir (7,5 →
  6,0 · 8,0 → 6,5). Ürün yüksek seviyeli bir konuşmacıya "ortanın biraz üstü" diyebiliyor.
  Yönü doğru olan yanlış budur: kullanıcı hazır olmadığını sanır, hazır olmadığı hâlde
  hazır sanmaz.
- Alt bandda şişme kapandı: gerçek bandı 3,0 olan cevap artık **3,5**, 4,0 olan üç cevap
  **4,0 / 4,5 / 4,5** görünüyor. Tur 5'te bunlar 4,5 / 5,0 / 5,0 / 5,5 idi.
- Ürünün verdiği puan aralığı **3,5–8,5**. Tur 1'de 4,5–7,0 idi: ölçek her iki uçtan da
  gerçekten açıldı, dar bir orta banda sıkışma yok.

**Ayakta kalan tek yazma kusuru:** AC-T1-1C-A (gerçek band 5,0) dört turda ölçüldü ve
üçünde **+1,0**, birinde +0,5 sapma verdi; hiçbir düzeltmede kıpırdamadı — tur 6'da bile
6,0 aldı ve turun **tek** +1,0'lık yazma sapması odur. Tek örnek olduğu için kural
yazılmadı (örneğe özel kural yasak); örüntü doğrulanana kadar da yazılmamalı.

---

## 5. Kalan riskler

Sonuç iyi çıktığı hâlde aşağıdakiler **duruyor**. Hiçbiri bu ölçümle kapanmaz.

1. 🔴 **Saklı küme farkı yanlış yöne döndü (0,08 → 0,08 → 0,292).** Bölüm 2'de yazıldı:
   ezber ne kanıtlandı ne elendi. Ayırt etmenin tek yolu **hiç kullanılmamış yeni
   örneklerle** bir ölçüm turudur. Bu yapılmadan "kalibrasyon bitti" denemez.

2. 🔴 **Tutarlılık 3. düzeltmeden sonra hiç ölçülmedi.** Tur 6 tek puanlamalıdır. Son
   gerçek ölçümler: yazma 0,28 (geçti), **konuşma 0,79 (kaldı)**. Konuşmada aynı cevaba
   altı puanlamada 1,5 band fark verilen iki örnek vardı. Ürün tek puan gösterdiği için
   bu doğrudan kullanıcıya yansır. **Tekrarlı bir konuşma turu, sıradaki iş budur.**

3. 🔴 **Konuşmada Part 1 örneği yok.** On iki konuşma örneğinin hepsi Part 2/3.
   Tanışma sorularında (kısa, kişisel, düşük yüklü konuşma) ürünün davranışı
   **hiç ölçülmedi**. Kullanıcının ilk karşılaşacağı bölüm tam olarak orasıdır.

4. 🔴 **Örnek sayısı az — band başına 1-2.** 36 örnek, dokuz band değeri, iki beceri,
   üç yazma görev türü. Bu veriyle **band bazlı ince ayar yapılamaz**; yalnız üç geniş
   aralık (≤4,5 · 5–6,5 · ≥7) okunabilir. Alt bandın tamamı **4 örneğe** dayanıyor ve
   gerçek bandı **3,0'ın altında hiç örnek yok**. Konuşmada band 5'in altı yok.

5. 🔴 **Puanlayan da, talimatı yazan da, örnekleri döken de aynı model ailesi.** Ortak kör
   noktalar bu ölçüm düzeneğinde **yapısal olarak görünmez**: talimatı yazan model kendi
   anladığı ölçütü yazıyor, puanlayan model aynı ölçütü aynı biçimde anlıyor, sapma
   raporda çıkmıyor. Farklı aileden ikinci bir puanlayıcıyla çapraz kontrol
   **proje sahibinde bekliyor**; bu ölçüm serisi onun yerine geçmez.

6. **Konuşmanın akıcılık ölçütü doğrulama turunda aşağı kaydı** (−0,12 → −0,58) ve
   konuşmanın eğilimi −0,250'den −0,375'e gitti. 3. düzeltme `konusma.md`'ye yalnız ortak
   bloklardan (19–22) dokunmuştu; beklenti tam olarak "bozulursa bozan ortak bloklardır"
   diyordu. Tek turluk, tek puanlamalı veriyle bu **gürültü de olabilir**, ortak blokların
   konuşmaya sızması da. Ayrıntı ve karar önerisi `SONUC-konusma.md`'de.

7. **Konuşmada kelime ölçütü orta bandda hâlâ yüksek** (tur 4 +0,70 · tur 6 +0,60), üç
   ölçüt içinde en yükseği. Bilerek düzeltilmedi (aynı turda iki yöne birden itmemek
   için). Ölçülmüş, açık, kapanmamış bir sapmadır.

8. **AC-T1-1C-A** dört ölçümün üçünde +1,0 sapıyor ve hiçbir düzeltmeden etkilenmedi;
   tek örnek olduğu için sebebi bilinmiyor. Aynı görev türünden (Academic Task 1, band 5)
   ikinci bir örnek gerekiyor: örüntüyse düzeltilir, değilse gürültüdür.

---

## 6. 🔴 Kapanış

Bu iş **yazma ve konuşma puanlamasının** güvenilirliğini ölçer.

Okuma ve dinlemede "kaç doğru = hangi band" eşiğini **doğrulamaz**. O eşik ancak canlı
kullanım verisiyle ayarlanabilir; elimizdeki kaynaklarda (Cambridge IELTS 1–8) band çevrim
tablosu **yok**, yalnız hazırlık amaçlı üç aralıklı çizelgeler var, ve depodaki
`band_thresholds` değerleri hedef değil **çapa**dır.

Bu yüzden üründe **"tahmini band"** ibaresi **kalkmaz**.
