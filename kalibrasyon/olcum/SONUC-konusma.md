# Puanlama kalibrasyonu — KONUŞMA (2026-08-09)

`prompts/OPUS5-A4-puanlama-duzeltmesi.md` son rapor çalıştırmasının konuşma bölümü.
Genel sonuç ve yazma tarafı: **`SONUC.md`**. Bu dosyada da **hiçbir düzeltme yapılmadı**.

Bütün sayılar `tools/_a4_sonuc_son.py` tarafından ham puanlama dosyalarından hesaplandı.
Aksi belirtilmedikçe puan = ürünün kullanıcıya gösterdiği **tek seferlik (ilk) puan**.

---

## Konuşma ne kadar ölçüldü

| Tur | Kapsam | Ne sınadı |
|---|---|---|
| 4 | 12 örnek × **6 tekrar** = 72 puanlama | Projenin **ilk konuşma ölçümü** (temel) |
| 6 | 12 örnek × 1 = 12 puanlama | 3. düzeltmenin konuşmaya etkisi (saklı küme S2) |

Konuşma, yazmadan **iki tur geç** ölçüldü: 1. ve 2. düzeltme konuşma verisi olmadan
yazıldı ve `konusma.md`'ye yalnız ortak bloklar üzerinden yansıdı. 3. düzeltme konuşmayı
gördü ama **konuşmaya özgü hiçbir kural yazmadı** — `konusma.md` yalnız 19–22 numaralı
ortak bloklardan değişti. Bu, aşağıdaki bulguyu okurken akılda tutulması gereken tek şey.

**Örneklerin kapsamı (ölçümün sınırı burada):**

| Part | Kaç örnek | Band aralığı |
|---|---|---|
| Part 1 | **0** | — |
| Part 2 | 2 | 5,0 · 6,5 |
| Part 3 | 10 | 5,0 – 9,0 |

Gerçek bandı **5'in altında hiç örnek yok**. Konuşmanın alt ucu ölçülmemiştir; bu yüzden
3. düzeltmenin 23 numaralı alt sınır notları bilerek yalnız yazma dosyalarına yazıldı.

---

## 1. İki turun ölçüleri

| Ölçü | tur 4 (6 tekrar) | **tur 6 (1 puanlama)** |
|---|---|---|
| Ortalama mutlak fark | 0,583 | **0,458** |
| Eğilim (+ cömert / − cimri) | −0,250 | **−0,375** |
| En büyük tek sapma | 2,00 | **1,50** |
| Yayılım (tutarsızlık) | **0,79** | — ¹ |
| Verilen puan aralığı | 4,5 – 8,5 | 5,0 – 8,5 |
| Tam isabet | 3/12 (%25) | **5/12 (%42)** |
| 0,5 band içinde | 9/12 (%75) | **10/12 (%83)** |
| ≥1,5 band sapan örnek | 1/12 | 2/12 |

¹ Tur 6'da her örnek bir kez puanlandı; yayılım tanım gereği 0,00 çıkar.
`RAPOR-tur6.md`'nin "yayılım ✅ geçti" satırı **konuşma için ölçüm değildir**.

**Okunuşu:** genel doğruluk iyileşti (0,583 → 0,458), ama eğilim **daha da cimri** oldu
(−0,250 → −0,375) ve ≥1,5 sapan örnek sayısı 1'den 2'ye çıktı. Yani ortalama iyi giderken
**uçlar kötüleşti** — kullanıcı tek puan gördüğü için önemli olan ikincisidir.

### Band aralığı × ölçüt (ölçüt bandı − gerçek genel band, tek seferlik)

| Tur | Band | n | akıcılık | kelime | dilbilgisi | **genel** |
|---|---|---|---|---|---|---|
| 4 | ≥ 7 | 7 | −0,36 | −0,50 | −1,00 | **−0,57** |
| 4 | 5–6,5 | 5 | +0,20 | **+0,70** | −0,30 | **+0,20** |
| **6** | ≥ 7 | 7 | **−1,00** | −0,21 | −0,86 | **−0,71** |
| **6** | 5–6,5 | 5 | 0,00 | **+0,60** | −0,20 | **+0,10** |

### Ölçüt bazında, bütün örneklerde

| Ölçüt | tur 4 (6 tekrarın ort.) | tur 4 (tek) | **tur 6 (tek)** |
|---|---|---|---|
| Akıcılık ve tutarlılık | −0,13 | −0,12 | **−0,58** |
| Kelime dağarcığı | +0,06 | 0,00 | **+0,12** |
| Dilbilgisi | −0,55 | −0,71 | **−0,58** |

**İki örüntü:**

- **Dilbilgisi ölçütü baştan beri en cimri ölçüt** (−0,55 / −0,71 / −0,58) ve üst bandda
  −0,86 ile duruyor. Bu değişmedi, hiç düzeltilmedi.
- 🔴 **Akıcılık ölçütü doğrulama turunda çöktü: −0,12 → −0,58**, üst bandda **−1,00**.
  Tur 4'te üç ölçütün en doğrusuydu; tur 6'da en kötüsü oldu. Sebebi bölüm 3'te.
- **Kelime ölçütü orta bandda hâlâ +0,60/+0,70** ile en yüksek sapma. 3. düzeltme bunu
  **bilerek** düzeltmedi (aynı turda iki yöne birden itmemek için); duruyor.

---

## 2. Örnek örnek

| Örnek | Gerçek | tur 4 (6 puanlama) | tur 4 tek | **tur 6** | tur 6 sapma |
|---|---|---|---|---|---|
| SP-band5-1 | 5,0 | 6,0 · 5,0 · 5,0 · 5,0 · 4,5 · 5,0 | 6,0 | **5,0** | 0,0 |
| SP-band5-2 | 5,0 | 4,5 · 5,0 · 4,5 · 4,0 · 4,5 · 5,0 | 4,5 | **5,0** | 0,0 |
| SP-band6-1 | 6,0 | 6,5 · 6,5 · 6,0 · 6,5 · 6,5 · 6,5 | 6,5 | **6,0** | 0,0 |
| SP-band6-2 | 6,0 | 5,5 · 6,5 · 6,5 · 6,0 · 6,0 · 6,0 | 5,5 | **6,0** | 0,0 |
| SP-band6_5-1 | 6,5 | 7,0 · 6,0 · 7,0 · 6,0 · 6,5 · 6,5 | 7,0 | **7,0** | +0,5 |
| SP-band7-1 | 7,0 | 7,0 · 7,0 · 7,5 · 7,5 · 7,0 · 7,5 | 7,0 | **7,0** | 0,0 |
| SP-band7-2 | 7,0 | 7,0 · 7,5 · 7,0 · 7,5 · 7,5 · 7,0 | 7,0 | **6,5** | −0,5 |
| SP-band7_5-1 | 7,5 | 6,5 · 6,0 · 6,5 · 7,0 · 7,0 · 7,0 | 6,5 | **6,0** | 🔴 **−1,5** |
| SP-band8-1 | 8,0 | 8,0 × 6 | 8,0 | **7,5** | −0,5 |
| SP-band8-2 | 8,0 | 6,0 · 7,0 · 6,5 · 7,0 · 7,5 · 6,5 | 6,0 | **6,5** | 🔴 **−1,5** |
| SP-band8_5-1 | 8,5 | 8,0 · 8,0 · 8,5 · 8,0 · 8,5 · 8,5 | 8,0 | **8,0** | −0,5 |
| SP-band9-1 | 9,0 | 8,5 · 8,5 · 9,0 · 8,5 · 9,0 · 9,0 | 8,5 | **8,5** | −0,5 |

**Kazanılan:** gerçek bandı 5,0 · 5,0 · 6,0 · 6,0 olan **dört örneğin dördü de** tur 6'da
tam isabet etti; tur 4'te dördü de kaçmıştı (+1,0 · −0,5 · +0,5 · −0,5). 3. düzeltmenin
alt band okuma kuralı, doğru satıra oturmuş bir cevapta işini yaptı.

**Kaybedilen:** üst banddaki (≥7) yedi örneğin **altısı** tur 6'da gerçek bandın altında,
biri tam isabet. Tur 4'te üçü tam isabetti. Ölçeğin üst ucu konuşmada bir miktar kapandı.

---

## 3. 🔴 İki büyük sapmanın mekanizması

Tur 6'nın ≥1,5 band sapan iki örneği de konuşmadır ve ikisinin de **akıcılık ölçütü**
çökmüştür:

| Örnek | Gerçek | Akıcılık tur 4 | **Akıcılık tur 6** | Genel tur 6 |
|---|---|---|---|---|
| SP-band7_5-1 | 7,5 | 6,5 | **5,0** | 6,0 |
| SP-band8-2 | 8,0 | 6,0 | **5,0** | 6,5 |

Gerekçe metinleri mekanizmayı açıkça gösteriyor. Tur 4, tur 6'daki gerekçelerle yan yana:

- **tur 4** (SP-band7_5-1): *"…eventually landing on a clear point… The repeated restarts
  needed to get there… show hesitation over language breaking the flow more than
  occasionally."* → **6,5**: başarı adlandırılıyor, sonra kusur bandı kırpıyor.
- **tur 6** (aynı örnek): *"…reformulates the same phrase repeatedly within a single
  response… this happens in most of the candidate's turns."* → **5,0**: yalnız kusurun
  yaygınlığı sayılıyor.

Bu tam olarak **19 numaralı değişikliğin** yaptığı iştir: "bir satırda durduğunda altındaki
satırı da oku, alt satır açıkça fazla sert olana kadar inmeye devam et". Kural açıkça
"6 ve altı satırlar" diye sınırlandırılmıştı ve o sınır **teknik olarak tutuyor** — ihlal
yok. Ama sınır, modelin **zaten yanlış satıra oturduğu** durumda korumuyor: konuşmanın
akıcılık ölçütünde model bu iki örneği tur 4'te de 6,0/6,5'e koymuştu, yani zaten
"6 ve altı" bölgesindeydi; yeni kural oradan bir satır **daha** aşağı indirdi. Hata
düzeltilmedi, **bileşikleştirildi**.

Aynı kural doğru yerleşmiş cevaplarda tam beklendiği gibi çalıştı: gerçek bandı 5,0 olan
iki örnek tur 4'te 6,0 ve 4,5 alırken tur 6'da ikisi de **5,0** aldı.

**Sonuç:** 19 numaralı değişikliğin **kendisi** yanlış değil; konuşmada **yanlış yerleşimi
büyütüyor**. Bunu yazmadan ayıran şey, yazmada ilk yerleşimin doğru olması. Konuşmada
akıcılık ölçütünün ilk yerleşimi üst bandda hatalı; kural onun üstüne biniyor.

**Öneri (bu çalıştırmada uygulanmadı — düzeltme yasak):** sıradaki düzeltmede
`konusma.md`'de 19 numaralı iniş kuralına, üst bandda kullanılan 12 numaralı kuralın
karşılığı yazılmalı — *kusurun yaygın olması, cevabın başardığı şeyi geçersiz kılmaz;
inmeden önce üstteki satırın cevabı anlatıp anlatmadığı bir kez daha sorulmalı.* Bu bir
alt band gevşetmesi değil, **iniş kuralının duruş koşuludur** ve yazmayı etkilemez.

---

## 4. Tutarlılık — konuşmanın en zayıf yanı

Tur 4, konuşmanın **tekrarlı ölçüldüğü tek tur**: 12 örnek × 6 puanlama.

| Ölçüt | Ortalama yayılım (6 tekrar) |
|---|---|
| Akıcılık ve tutarlılık | 0,54 |
| Kelime dağarcığı | 0,88 |
| **Dilbilgisi** | **0,96** |
| **Genel band** | **0,79** 🔴 |

- 12 örneğin **11'i** tekrarlar arasında oynadı; yalnız SP-band8-1 altı puanlamada altı kez
  aynı puanı verdi.
- İki örnekte yayılım **1,5 band**: SP-band5-1 (4,5–6,0) ve SP-band8-2 (6,0–7,5).
  Aynı cevap, aynı talimat, iki farklı kullanıcıya **1,5 band** fark.
- Yayılımın en büyük kaynağı **dilbilgisi** (0,96), kelime (0,88) hemen arkasında.
  3. düzeltme kaydındaki "yayılımın çoğu kelime ölçütünden geliyor" notu **yarım
  doğrudur**: kelime büyük bir kaynak ama en büyüğü değil.

Yazmayla karşılaştırma: tur 3'te yazmanın yayılımı **0,28**, tur 5'te 0,25. Konuşma
yazmanın **üç katı** savruluyor.

🔴 **Bu ölçüm 3. düzeltmeden ÖNCEdir ve sonra tekrarlanmadı.** Tur 6 tek puanlamalıdır.
Konuşmanın bugünkü tutarlılığı **bilinmiyor**.

---

## 5. Başarı ölçütleri — konuşma (tur 6)

| Ölçüt | Sonuç |
|---|---|
| Ortalama mutlak fark < 0,5 band | ✅ **geçti** — 0,458 |
| Hiçbir örnekte ≥1,5 band sapma yok | 🔴 **KALDI** — SP-band7_5-1 ve SP-band8-2 |
| Eğilim ±0,25 band içinde | 🔴 **KALDI** — −0,375 (tur 4'te −0,250 ile sınırdaydı) |
| Aynı cevaba verilen puanların yayılımı ≤ 0,5 | ⚪ **ÖLÇÜLMEDİ** (tur 6 tek puanlamalı). Son gerçek ölçüm tur 4: **0,79 → KALDI** |

Dört ölçütten **yalnız biri** temiz geçiyor. Yazmada dördün üçü geçti, biri ölçülmedi
(bkz. `SONUC.md` bölüm 3).

### Saklı küme (S2) — konuşma tarafı

| Küme | n | Ort. mutlak fark | Eğilim |
|---|---|---|---|
| S2 (3. düzeltmede **saklı**) | 4 | 0,625 | −0,375 |
| S1 + S3 (görünür) | 8 | 0,375 | −0,375 |

Fark 0,250 band. Eğilim iki tarafta **birebir aynı**; ayrılan yalnız büyüklük ve onun da
tamamı tek bir örnekten geliyor (SP-band7_5-1, −1,5; S2'nin toplam 2,5 bandlık sapmasının
1,5'i). Dört örneklik bir kümede bu **ezber kanıtı sayılamaz**; genel ezber tartışması
`SONUC.md` bölüm 2'de.

---

## 6. Ürünün gerçek davranışı — konuşmada tek puan

| Fark | Kaç örnek (12) |
|---|---|
| −1,5 | 2 |
| −0,5 | 4 |
| **0,0** | **5** |
| +0,5 | 1 |

- 12 kullanıcıdan 10'u **yarım band içinde** doğru puan alıyor.
- Kalan ikisi **1,5 band düşük** alıyor: band 7,5 konuşmacı 6,0, band 8,0 konuşmacı 6,5
  görüyor. IELTS başvurularında 6,5 ile 7,5 arasındaki fark çoğu üniversite eşiğinin iki
  yanıdır; bu sapma pratikte "başvurabilirsin / başvuramazsın" farkı demektir.
- Sapmaların **6'sı cimri, 1'i cömert**. Ürün konuşmada sistematik olarak **düşük**
  puanlıyor. Yönü tercih edilebilir olandır (kullanıcı hazır olmadığını sanır, tersi
  değil) ama ölçüt olarak kaldı.
- Alt/orta bandda (5,0–6,5) ürün artık **hatasız**: beş örneğin dördü tam isabet, biri
  +0,5.

---

## 7. Kalan riskler — konuşma

1. 🔴 **Part 1 örneği yok.** Tanışma sorularında (kısa cevap, kişisel konu, düşük bilişsel
   yük) ürünün davranışı **hiç ölçülmedi**. Kullanıcının ilk karşılaşacağı bölüm orası ve
   akıcılık ölçütü orada Part 3'tekinden yapısal olarak farklı okunur. Ölçümün en büyük
   kör noktası budur.
2. 🔴 **Tutarlılık 3. düzeltmeden sonra ölçülmedi.** Son gerçek değer 0,79 (kaldı), iki
   örnekte 1,5 band. **Tekrarlı bir konuşma turu sıradaki iştir.**
3. 🔴 **Akıcılık ölçütü doğrulama turunda −0,12'den −0,58'e kaydı**, üst bandda −1,00.
   Mekanizma bölüm 3'te ve düzeltilebilir; ama tek turluk, tek puanlamalı veriyle
   ölçüldüğü için **gürültü olma ihtimali elenemedi**. Tekrarlı turdan önce düzeltme
   yapılırsa gürültüye ayar çekilmiş olabilir.
4. 🔴 **Konuşmanın alt ucu (band 5'in altı) yok.** Yazmada alt band şişmesi ölçüldü ve
   düzeltildi; konuşmada aynı sorunun **var olup olmadığı bile bilinmiyor**. 23 numaralı
   alt sınır notları bu yüzden `konusma.md`'ye yazılmadı — ölçüme dayanmayan bir değişiklik
   olurdu.
5. **Örnek sayısı az: 12 örnek, 8 farklı band değeri.** Band başına 1–2 örnek; band bazlı
   ince ayar yapılamaz. On örnek aynı iki konuda (hobiler · ünlü kişiler); **konu
   çeşitliliği yok**.
6. **Dilbilgisi ölçütü üç ölçümde de en cimri ölçüt** (üst bandda −0,86 … −1,00) ve
   tekrarlar arası en savruk ölçüt (yayılım 0,96). Hiç düzeltilmedi.
7. **Kelime ölçütü orta bandda +0,60/+0,70** ile duruyor; bilerek ertelendi.
8. **Puanlayan da, talimatı yazan da, örnekleri seçen de aynı model ailesi.** Konuşmada
   bu risk yazmadakinden büyüktür: değerlendirme **ses değil metin dökümü** üzerinden
   yapılıyor, telaffuz ölçütü bu yüzden zaten kaldırıldı, ve akıcılık ölçütü döküme
   yansıyan duraklama/yeniden başlama işaretlerine bağlı. Farklı aileden ikinci bir
   puanlayıcıyla çapraz kontrol **proje sahibinde bekliyor**.

---

## 8. 🔴 Kapanış

Konuşma puanlaması, ürünün ortalamada **en doğru** (MAE 0,458) ama uçlarda **en riskli**
tarafıdır: iki başarı ölçütü kaldı, biri hiç ölçülmedi, ve en son gerçekten ölçülen
tutarlılık değeri (0,79) sınırın epey üstündeydi.

Bu ölçüm **yazma ve konuşma puanlamasının** güvenilirliğini ölçer; okuma ve dinlemede
"kaç doğru = hangi band" eşiğini **doğrulamaz**. Üründe **"tahmini band"** ibaresi kalkmaz.
