# Değerlendirme talimatı — düzeltme kaydı

Her satır: **hangi örüntü → hangi değişiklik → beklenen etki**. Bir sonraki ölçüm turu bu
beklentileri sınar. Değişiklik gerekçesi ölçümden gelmiyorsa buraya yazılmaz.

---

## 1. düzeltme — 2026-08-07

| | |
|---|---|
| Ölçüm | `kalibrasyon/olcum/RAPOR-tur1.md` (tur 1, her örnek 3 tekrar) |
| Görülen kümeler | **S1 + S2** (14 örnek × 3 puanlama) |
| SAKLI küme | **S3** — bu oturumda o kümenin hiçbir örneğine, gerçek bandına, sapma satırına bakılmadı |
| Değişen dosyalar | `ORTAK-KURALLAR.md`, `yazma-task1-academic.md`, `yazma-task1-general.md`, `yazma-task2.md`, `konusma.md` |

### 🔴 Ölçümün eksikliği (bu düzeltmenin dayanağı hakkında)

Tur 1 **tamamlanmadan** bu adıma gelindi: 23 örnekten **21'i** puanlandı (63/69 puanlama).
Eksik olan iki örnek `GT-T2-2B-B` ve `GT-T2-2B-C`; ikisi de görünür kümelerde (S1 ve S2), yani
saklı küme bu eksikten etkilenmiyor. `tools/puanlama-raporu.py 1` bu 21 örnek üzerinden
çalıştırıldı ve RAPOR-tur1.md eksik veriyle üretildi. Puanlamayı bu oturum **yapamaz**: ölçüm
Sonnet ile yapılır (bkz. `prompts/SONNET5-A3-puanlama-olcumu.md` başlığı), bu oturum Opus.
Eksik iki örnek 2. ölçüm turunda kapanacak. Aşağıdaki örüntüler 14 görünür örneğin 42 puanlamasına
dayanıyor ve hepsi tek tek örneğe değil, **band aralığı × ölçüt** kırılımına dayanıyor.

Ayrıca: kök `NOTLAR.md`, ölçüm turunun her grubu için **tahmin edilen** bandları listeliyor
(gerçek bandları veya sapmaları değil). Bu oturum saklı kümenin gerçek bandına ve sapmasına
bakmadı; saklı küme karşılaştırması hâlâ geçerli.

### Ölçüm ne dedi

Tek seferlik puan üzerinden, görünür kümeler (S1+S2, n=14): ortalama mutlak fark **0,93 band**,
eğilim **−0,57 band** (cimri), en büyük tek sapma **2,0 band**, aynı cevaptaki yayılım **0,33**.
Dört başarı ölçütünden yalnız tutarlılık geçti.

Örüntü, tek yönlü bir cimrilik değil — **ölçeğin ortaya doğru büzülmesi**:

| Gerçek band | Ölçüt sapmaları (ölçüt bandı − gerçek genel band) |
|---|---|
| ≥ 7 | görev −1,80 · tutarlılık −1,73 · kelime −1,23 · dilbilgisi −1,73 |
| 5 – 6,5 | görev −0,26 · tutarlılık −0,21 · kelime −0,36 · **dilbilgisi −0,95** |
| ≤ 4,5 | görev **+1,33** · tutarlılık +0,92 · kelime +0,58 · dilbilgisi +0,33 |

Gerçek bandlar 3,0–8,5 arasında yayılırken verilen tek seferlik puanların **tamamı 4,0–6,5**
aralığına düştü. Yani: üst bandlar sıkışıyor **ve** alt bandlar şişiyor. Alt band şişmesi
tehlikeli olan taraf: hazır olmayan kullanıcı hazır sanır.

İki ek örüntü:

1. **Cimriliğin en büyük tek kaynağı tavanlar (caps).** Puanlama gerekçelerinde tavan koşulu
   tetiklendiğinde model tavan değerini **puan olarak** yazıyor. Aynı mekanizma iki yönde birden
   hata üretiyor: güçlü cevapta tek bir tavan koşulu bandı 5'e çekiyor, zayıf cevapta ise tavan
   bir **taban** gibi çalışıp cevabı 5'e yükseltiyor. Tavan koşullarının kendisi de tartışmayla
   tetikleniyordu (ör. "genel bir bakış yok", "açık bir tutum yok" kararları, gerçek sınav
   görevlisinin aynı cevapta görmediği yerlerde veriliyordu).
2. **Dilbilgisi ölçütü ayrıca ve toplamalı olarak sert.** Diğer üç ölçütün doğru olduğu orta
   bandda bile −0,95. Hata payı tablosunun eşikleri, "içinde en az bir hata olan cümle" sayımıyla
   birlikte, temiz ama küçük kusurlu metni bir band aşağı itiyor.

### Yapılan değişiklikler

| # | Örüntü | Değişiklik | Beklenen etki |
|---|---|---|---|
| 1 | Tavan değeri puan olarak kullanılıyor; alt bandlar 5'e şişiyor | ADIM 2'ye tavan tanımı eklendi: tavan **yalnızca üst sınır**, "max 5" = "5 veya altı"; tablodan okunan band ile tavanın **düşüğü** alınır; tavan hiçbir zaman bandı yükseltmez. Aynı ölçütte iki tavan birden tetiklendiyse band tablodan okunur | Alt bandlarda görev ölçütünün +1,33'lük şişmesi kapanır; gerçek band 3–4 olan cevaplar 4,5–5 yerine 3–4 alır |
| 2 | Tavanlar tartışmayla, zorlanarak tetikleniyor | Aynı kurala tetikleme eşiği eklendi: tavan ancak koşul bu cevapta **açıkça doğruysa** ve kanıtı gösterilebiliyorsa işler; savunmak gerekiyorsa işlemez | Üst bandlarda görev ölçütünün −1,80'lik çöküşü azalır |
| 3 | Ölçütler arası eşik davranışı hep aşağı yuvarlıyordu ("iki band arasındaysa düşüğünü al") | Kural değişti: iki band arasındaysa **aradaki yarım band** verilir; alt tam banda ancak üst bandın çekirdek koşulu hiç karşılanmadığında inilir | Sistematik cimriliğin ~0,25 bandlık kısmı kalkar; ölçüt düzeyinde çözünürlük artar |
| 4 | Puanlar 4,0–6,5'e büzülüyor, ölçeğin uçları hiç kullanılmıyor | ADIM 2'ye ölçek kullanımı kuralı eklendi: 3–9 arasındaki her band olağan bir sonuçtur; belirsizlik ortaya kaçmak için gerekçe değildir; 5 ve 6 varsayılan iniş yeri değildir | Hem üst hem alt uçta büzülme azalır; dağılım gerçek dağılıma yaklaşır |
| 5 | Dilbilgisi ölçütü her bandda ~1 band sert | Hata payı tablosunun eşikleri yaklaşık 10 puan yukarı kaydırıldı (8–9: ≤%20, 7: %20–40, 6: %40–60, 5: %60–80, 4: >%80) ve tabloya yorum eklendi: hata taşıyan cümle başarısız cümle değildir, 5 ve altı için anlamın gerçekten bozulması gerekir | Dilbilgisinin −1,05'lik sapması ~0 civarına iner; orta bandın genel puanı yaklaşık +0,25 yükselir |
| 6 | "Okuyucuyu tahmine zorlayan hata **ikiden fazla** → max 5" mutlak sayımı uzun ve iyi metni cezalandırıyor | Oransal hâle getirildi: cümlelerin **beşte birinden fazlası** yeniden okunmak zorundaysa; sayılacak olan hatalı cümle değil, yeniden okunması gereken cümle | 250+ kelimelik güçlü metinlerde dilbilgisinin 5'e çakılması biter |
| 7 | Kelime ölçütünde 7 kapısı yalnız aşağı çalışıyordu ("dört tane sayamıyorsan 6 veya altı") | Kural çift yönlü yapıldı: dördü sayabiliyorsan 7 **açıktır** ve genel izlenimle geri çekilemez; sekiz veya daha fazlası doğru kullanılmışsa 8'i destekler | Üst bandda kelime ölçütünün 6–7'ye çakılması azalır |
| 8 | Görev ölçütünün tavan koşulları, sınav görevlisinin görmediği yerde tetikleniyor | Koşulların tanımı netleştirildi (örneğe özel kural değil, tanım): genel bakış her yerde ve *Overall* etiketi olmadan da olabilir · tutum, taraf tutmayan gerekçeli bir sonuç da olabilir · bir madde "işlenmiş" sayılmak için ayrı paragraf gerektirmez, dolaylı karşılık da sayılır | Üst bandda görev ölçütünün tek başına 5'e düşmesi biter |
| 9 | Talimattaki örnek JSON çıktısı somut band değerleri içeriyordu (ör. 5/5/5/4); ölçümde puan vektörü zaman zaman bu örneğe birebir eşitti | Örnek çıktıdaki bütün band değerleri `<band>` yer tutucusuna çevrildi; "örnek yalnız **biçim** gösterir" notu eklendi. `ORTAK-KURALLAR.md` BLOK J'ye bir daha somut sayı konulmaması kuralı yazıldı | Çıktı örneğinin çapa etkisi kalkar; benzer cevaplara verilen aynı vektör azalır |
| 10 | Rol metni tek yönlü sertlik telkin ediyordu ("You are strict… şişirilmiş tahmin en kötü sonuç") | Rol metni simetrik hâle getirildi: amaç doğru bandı bulmak; şişirme de düşürme de kullanıcıya zarar verir, ikisi de "güvenli taraf" değildir | Sistematik −0,57'lik eğilimin bir kısmı kapanır |

Değişiklik 1–4 ve 9–10 **her beş dosyada** aynı; 5–7 dört puanlama talimatında aynı (hata payı
tablosu `ORTAK-KURALLAR.md`'ye **BLOK K** olarak alındı, dört dosyada aynen tekrarlanıyor);
8 her görev türünde kendi ölçütünün diline göre yazıldı.

### Bilerek yapılmayanlar

- **Örneğe özel hiçbir kural yazılmadı.** Hiçbir örnek kodu, cevabı, gerçek bandı veya konusu
  talimata girmedi. Bütün değişiklikler band aralığı × ölçüt kırılımına dayanıyor.
- Ölçüt sayısı ve ağırlığı değişmedi (yazma 4, konuşma 3).
- Telaffuz geri getirilmedi; konuşmada yine üç ölçüt var.
- Çıktı uzunluğu sınırları değişmedi.
- `cikti-semasi.json` değişmedi: makine sözleşmesi aynı, üretilen alanlar aynı. Şemadaki
  örnek dolu bir puanlamadır ama şema dosyası puanlayan modele **gönderilmiyor** (talimat
  dosyaları standalone), o yüzden çapa etkisi yok.

### 🔴 Konuşma tarafı ölçülmedi

`kalibrasyon/ornekler/` altında **konuşma klasörü hiç yok** (yalnız `yazma/` var): bu turda
puanlanan 21 örneğin hepsi yazma.
`konusma.md`'ye yapılan değişiklikler ortak blokların senkron tutulması kuralından geliyor
(`ORTAK-KURALLAR.md` bakım kuralı) ve yazma verisinden **genellenmiş** durumda — konuşmada
ölçülmüş bir örüntüye dayanmıyor. Konuşma puanlamasının sapması bu projede **hâlâ ölçülmemiştir**;
son raporda kalan risk olarak yazılmalı.

### Sınanacak beklenti (tur 2)

1. Eğilim −0,57'den **0'a doğru** hareket etmeli (hedef ±0,25 içi).
2. En büyük tek sapma 2,0'ın **altına** inmeli.
3. Tek seferlik puanlar 4,0–6,5 aralığından çıkmalı; gerçek band ≥7 olan örneklerde en az bir
   7 veya üstü, gerçek band ≤4 olan örneklerde en az bir 4 veya altı görülmeli.
4. Orta bandın (5–6,5) şu anda tutan doğruluğu **bozulmamalı** — asıl risk bu: 5 ve 10 numaralı
   değişiklikler orta bandı cömertliğe kaydırırsa düzeltme yanlış yöne gitmiştir.
5. Saklı küme (S3) ile görünür kümeler arasındaki fark **açılmamalı**. Açılırsa ayar örneklere
   ezberlenmiştir.

---

## 2. düzeltme — 2026-08-07

| | |
|---|---|
| Ölçüm | `kalibrasyon/olcum/RAPOR-tur2.md` (tur 2, 23 örnek × 1 puanlama — tur tam) |
| Görülen kümeler | **S2 + S3** (15 örnek) |
| SAKLI küme | **S1** — o kümenin hiçbir örneğine, cevabına, sınav görevlisi yorumuna, ölçüt puanına bakılmadı |
| Değişen dosyalar | `ORTAK-KURALLAR.md`, `yazma-task1-academic.md`, `yazma-task1-general.md`, `yazma-task2.md`, `konusma.md`, `NOTLAR.md` |
| Tanı scriptleri | `tools/_a4_analiz.py`, `tools/_a4_ust.py` — ikisi de `kumeler.json`'daki S2+S3'e kilitli |

### 🔴 Saklı küme hakkında dürüst not

`RAPOR-tur2.md`'nin "Örnek örnek" tablosu bütün kümeleri **tek tablo hâlinde** listeliyor; dosya
açıldığında S1 satırları da ekrana geldi. Bu satırlar bu oturumun **hiçbir analizine girmedi**:
bütün örüntüler, ortalamalar ve gerekçeler yalnız S2+S3'ün 15 örneği üzerinden, kümeye kilitli iki
script ile hesaplandı; S1 örneklerinin cevap metinleri, sınav görevlisi yorumları ve ölçüt
puanları hiç açılmadı. Yine de kayda geçiyor: saklı küme koruması **rapor biçimi yüzünden** ideal
değil. `tools/puanlama-raporu.py` sonraki turdan önce kümeye göre bölünmüş rapor üretecek şekilde
düzeltilmeli; son raporda bu bir risk olarak yazılmalı.

### 1. düzeltmenin beklentileri tuttu mu

| Beklenti | Sonuç |
|---|---|
| 1. Eğilim −0,57'den 0'a doğru hareket etmeli | 🔴 **KALDI** — görünür kümelerde −0,67; genel eğilim −0,67 → −0,70 |
| 2. En büyük tek sapma 2,0'ın altına inmeli | 🔴 **KALDI** — hâlâ 2,0 |
| 3. Puanlar 4,0–6,5 aralığından çıkmalı; ≥7 örneklerde en az bir 7+ | 🔴 **KALDI** — tek seferlik puanların tamamı 3,5–7,0'da; ≥7 olan 6 örneğin en yükseği 7,0, hiçbiri 7'yi geçmedi |
| 4. Orta bandın (5–6,5) doğruluğu bozulmamalı | ✅ **GEÇTİ** — orta band −0,40 → **−0,29**; asıl kazanç dilbilgisinde: −0,90 → **−0,64** |
| 5. Saklı küme (o turda S3) ile görünür kümeler arasındaki fark açılmamalı | ✅ **GEÇTİ** — 1. düzeltmede S3 saklıydı; tur 2'de S3 **0,86**, o turda görünür olan S2 **1,00**. Bir turda saklı olan küme sonraki turda görünür olandan **kötü değil** → ezber işareti yok |
| — | Tutarlılık ölçütü **sınanmadı**: tur 2'de her örnek 1 kez puanlandı, yayılım tanım gereği 0,00 çıkar. RAPOR-tur2'deki ✅ bu satırda **anlamsızdır** |

⚠️ Karşılaştırma uyarısı: 1. düzeltmenin tablosu o oturumun görünür kümeleri (S1+S2) üzerinden,
buradaki tablo bu oturumun görünür kümeleri (S2+S3) üzerinden hesaplandı. Ortak olan yalnız S2.
Aynı **band aralığı × ölçüt** kırılımı iki turda da aynı 15 örnekten (S2+S3) yeniden hesaplandığı
için aşağıdaki tur1↔tur2 sayıları eşleşiktir; yukarıdaki satırlar ise küme bileşimi farkını taşır.

Yani 1. düzeltmenin **dilbilgisi ve orta band** kısmı çalıştı, **üst band** kısmı hiç çalışmadı.
Değişiklik 3, 4, 7 ve 10 (yarım band, ölçek kullanımı, kelime 7 kapısı, simetrik rol metni) üst
bandı hareket ettirmedi. Sebebi aşağıda: hepsi **öğüt**tü, hiçbiri modelin puanı bulma **yordamını**
değiştirmedi.

### Ölçüm ne dedi (yalnız S2+S3, n=15)

Band aralığı × ölçüt kırılımı (ölçüt bandı − gerçek genel band):

| Gerçek band | n | görev | tutarlılık | kelime | dilbilgisi | genel |
|---|---|---|---|---|---|---|
| ≥ 7 | 6 | −1,42 | **−2,17** | −1,33 | −1,33 | **−1,50** |
| 5 – 6,5 | 7 | −0,21 | −0,29 | −0,21 | −0,64 | −0,29 |
| ≤ 4,5 | 2 | **+1,00** | +0,50 | 0,00 | 0,00 | +0,50 |

Sapmanın **neredeyse tamamı tek bir yerde**: gerçek bandı 7 ve üstü olan cevaplar. Orta band artık
neredeyse yerinde. Alt band hâlâ şişiyor ama görünür kümede yalnız 2 örnek var.

Üst bandda **tutarlılık** en kötü ölçüt (−2,17) ve 1. tura göre **kötüleşti** (−1,53 → −2,17).

#### Örüntü A — model kusurun **varlığını** cezalandırıyor, **bedelini** değil

Tur 2'nin gerekçeleri, aynı cevabın resmî sınav görevlisi yorumuyla yan yana konduğunda, kusurları
**aynı yerde** buluyor. Fark, o kusurun ne kadar sayıldığında. Sınav görevlisi yorumlarında tekrar
tekrar geçen ifade şu türden: hata var, "ancak okuyucuya etkisi az", "iletişimi engellemiyor",
"küçük bir sapma sayılır", "en yüksek bandların verilmesini engelliyor" — ve band yine 7–8,5.
Model tam olarak aynı kusuru adlandırıp 1,5–2 band düşüyor.

Bunun yapısal sebebi talimatın kendisinde: 7, 8 ve 9 satırları zaten hata **içeriyor**
("occasional errors", "occasional inaccuracy", "rare slips"). Talimatta bunu söyleyen bir cümle
yoktu, dolayısıyla adlandırılabilir her kusur diskalifiye gibi işledi.

#### Örüntü B — kanıt kuralının kendisi aşağı çekiyor

Tur 2'nin bütün üst band gerekçeleri aynı biçimde: "X iyi, **ama** y kusuru" — ve verilen band
kusuru izliyor. BLOK G "belirli kelimeyi/cümleyi/yapıyı adlandır" diyor; bir metinde adlandırması
en kolay şey **hatadır**. Yani kanıt kuralı, hiç öyle tasarlanmadığı hâlde, sistematik bir aşağı
baskı üretiyor.

#### Örüntü C — tavanların **değeri** yanlış, mekanizması değil

1. düzeltme tavanı "puan değil, tavan" hâline getirdi; bu doğruydu ama yetmedi, çünkü tavan
değerlerinin kendisi iki band fazla sert. Talimattaki tavanların neredeyse **hepsi "max 5"** —
tek bir biçimsel eksik, cevabı ölçeğin ortasına çakıyor. Üst bandda tutarlılığın çökmesinin
doğrudan sebebi bu: paragrafsızlık ve cümle sınırı tavanları, "max 5" oldukları için, iyi
sıralanmış bir metni 4,5–5'e indiriyor. Sınav görevlisi aynı eksik için "en yüksek bandları
engeller" diyor — yani 8/9'u kapatır, 5'e indirmez.

Aynı "max 5" yığılması alt bandda ters yönde çalışıyor: zayıf bir cevap üç tavanı birden tetikleyip
tam 5'e oturuyor, tavan **taban** gibi davranıyor. 1. düzeltmenin "iki tavan birden tetiklendiyse
tablodan oku" kuralı bu davranışı durdurmadı.

#### Örüntü D — hata oranı gözle tahmin ediliyor ve yüksek çıkıyor

Dilbilgisi orta bandda hâlâ en kötü ölçüt (−0,64). Gerekçelerde oran "kabaca yarısı", "kabaca beşte
ikisi" gibi **izlenimle** veriliyor; sınav görevlisi aynı metinler için "ara sıra hata" diyor.
Sorun 1. düzeltmede kaydırılan eşiklerde değil (o kaydırma işe yaradı: −0,90 → −0,64), **sayımda**.

#### Örüntü E — modelin tablo okuma yönü

Verilen puanların tamamı 3,5–7,0 arasında, gerçek bandlar 3,0–8,5'e yayılırken. "Bütün ölçeği
kullan" öğüdü iki turdur yazılı ve iki turdur işlemiyor. Öğüt yordamı değiştirmiyor: model tabloya
ortadan giriyor ve kanıt biriktikçe aşağı iniyor, yukarı çıkmıyor.

### Yapılan değişiklikler

| # | Örüntü | Değişiklik | Beklenen etki |
|---|---|---|---|
| 11 | E — ortadan başlayıp aşağı inme | **Puanlama yordamı tersine çevrildi.** Ölçüt tablosu artık **9'dan aşağı** okunuyor: satır satır in, **doğru olan ilk satırda dur**; band, "en güvenli" satır değil **hâlâ doğru olan en yüksek** satır. "Tabloya ortadan girme" açıkça yasaklandı | Ölçeğin üst ucu açılır; tek seferlik puanlar 7'nin üstüne çıkabilir. Ölçek kullanımı öğütten **yordama** dönüştüğü için ilk kez bağlayıcı |
| 12 | A — kusurun varlığı vs bedeli | STEP 2'ye **üst band kuralı** eklendi: 7, 8, 9 satırları zaten hata içerir; üst bandda soru "kusur bulabiliyor muyum" değil "bu kusur okuyucuya neye mal oluyor". 7 veya 8 satırının **zaten izin verdiği** bir kusur gerekçe gösterilerek 7'nin altı verilemez; "güçlü, ama X var" 7 veya 8 gerekçesidir, 5–6 gerekçesi değil | Üst bandın −1,50'lik çöküşünün ana kısmı kapanır — bu turun en büyük tek kalemi |
| 13 | C — tavan değerleri iki band fazla sert | Tutarlılık tavanları **yeniden derecelendirildi**: paragrafsızlık `max 5` → **`max 6`** (5'e ancak eksik paragraf **fikir sırasını** takip edilemez kıldığında inilir); cümle sınırı çöküşü `max 5` → **`max 6`**, tetikleme eşiği "okuyucu tekrar okumak zorunda" yerine **"cümlelerin beşte birinden fazlası"** + gerçekten iki kez okunanları say; `max 5` yalnız metnin tamamına yayıldığında ve bağ koptuğunda | Üst bandda tutarlılığın −2,17'si daralır; biçimsel bir eksik artık cevabı ölçeğin ortasına çakmaz |
| 14 | C — tavan tetiklendiğinde bandın kendisi oluyor | Tavan kuralı sertleştirildi: tavan **en son** uygulanır · tetiklenen tavan **hiçbir zaman tek başına bandın gerekçesi değildir** · **kaç tavan tetiklendiği kanıt değildir** · tavan değerine eşit bir band yazmadan önce cevabın tabloda o satıra gerçekten uyduğu doğrulanır, alt satıra uyuyorsa **alt band verilir** | Hem üstte tek tavanın bandı çakması, hem altta 5'in taban gibi davranması azalır |
| 15 | B — kanıt kuralı aşağı baskı üretiyor | Kanıt kuralı yönlendirildi: `why`'ın **birinci cümlesi** cevabın verilen bandı **ne ile hak ettiğini** söyler ve `quote` **onun** kanıtıdır; ikinci cümle bir üst banda ne engel olduğunu ekleyebilir. Yalnız kusur adlandıran `why` eksiktir ve yalnız kusura dayanan band genellikle bir band düşüktür. **Çıktı uzamıyor** — `why` yine en fazla 2 cümle | Gerekçe üretimindeki sistematik aşağı baskı kalkar; band, bulunan kusuru değil cevabın tamamını izler |
| 16 | D — hata oranı izlenimle tahmin ediliyor | BLOK K'ye **sayım disiplini** eklendi: izlenimle tahmin etme, say · bir cümle ancak hatasını **dilbilgisel bir adla** adlandırabiliyorsan sayılır · adlandıramıyorsan veya emin değilsen **sayılmaz** · yazım, farklı koyacağın bir virgül ve alışılmadık ama mümkün bir yapı burada hata değil · sayım iki satırın sınırına düşerse **üst band** alınır | Dilbilgisinin kalan −0,64'ü kapanır. Eşikler **kaydırılmadı** (1. düzeltmedeki kaydırma tuttu, ikinci kez kaydırmak orta bandı cömertliğe geçirirdi) |
| 17 | Üst bandda görev ölçütü (−1,42) | Üç yazma dosyasında görev ölçütü tablosunun **altına 6-7 ayrımı** yazıldı (örneğe özel değil, tanım): Görev 2'de bir fikir, okuyucu **niçin** öyle düşünüldüğünü görebiliyorsa gelişmiştir — örnek bir yol, gerekçe zinciri başka bir yol; ayrıca birden çok açıyı işleyip gerekçeli bir sonuca varmak **açık bir tutumdur**, iki taraftan birini seçmemek tutumsuzluk değildir. Görev 1 Academic'te genel bakış "daha dolgun olabilirdi" ise **var** sayılır (7'nin genel bakışıdır, eksik değil). Görev 1 General'de bir madde, okuyucunun üzerine hareket edebileceği içerik verildiğinde **kapsanmıştır**; satır sayısı ölçü değildir | Üst bandda görev ölçütünün −1,42'si daralır |
| 18 | Alt bandda görev ölçütü +1,00, 5 taban gibi çalışıyor | Dört yazma dosyasına **5-4 ayrımı** yazıldı: 5'te görev **kötü yapılmıştır**, 4'te **yapılmamıştır** (okuyucu istediği şeyi bulamaz) — ve "bir `max 5` tavanını tetiklemek 5'i **hak etmek değildir**; 4 ve 3 satırlarını da oku" | Alt bandın +0,50'lik şişmesi azalır. ⚠️ Görünür kümede alt bandda yalnız **2 örnek** var; bu değişikliğin dayanağı diğerlerinden **zayıf** ve tur 3'te ayrıca izlenmeli |

Değişiklik 11, 12, 14, 15, 16 **beş dosyada da** aynı (ortak bloklar, `ORTAK-KURALLAR.md` bakım
kuralı). 13 üç yazma dosyasında (konuşmada tutarlılık ölçütü ayrı değil). 17 ve 18 her görev
türünde kendi ölçütünün diline göre yazıldı.

### Bilerek yapılmayanlar

- **Örneğe özel hiçbir kural yazılmadı.** Hiçbir örnek kodu, konusu, cevabı, gerçek bandı veya
  sınav görevlisi yorumundan bir cümle talimata girmedi. Bütün değişiklikler band aralığı × ölçüt
  kırılımına ya da gerekçe **biçimine** dayanıyor.
- **Hata payı tablosunun eşikleri ikinci kez kaydırılmadı.** Ölçüm 1. kaydırmanın tuttuğunu
  gösterdi (orta band dilbilgisi −0,90 → −0,64); tekrar kaydırmak tek işleyen düzeltmeyi
  bozardı. Sayım kuralı düzeltildi, eşik değil.
- Ölçüt sayısı ve ağırlığı değişmedi (yazma 4, konuşma 3).
- Telaffuz geri getirilmedi.
- Çıktı uzunluğu sınırları değişmedi; 15 numaralı değişiklik `why`'ın **sırasını** belirliyor,
  uzunluğunu değil.
- `cikti-semasi.json` değişmedi.
- **Konuşmaya özgü hiçbir yeni kural yazılmadı.** `konusma.md` yalnız ortak blokların
  senkronundan değişti; konuşmanın kendi tavan değerlerine (hepsi `max 5`) dokunulmadı, çünkü
  onları ayarlayacak **hiçbir ölçüm yok**.

### 🔴 Konuşma tarafı hâlâ ölçülmedi

`kalibrasyon/ornekler/` altında yalnız `yazma/` var. Tur 2'de puanlanan 23 örneğin hepsi yazma.
`konusma.md`'ye giren 11, 12, 14, 15, 16 numaralı değişiklikler **yazma verisinden genellenmiş**
durumda. Konuşma puanlamasının sapması bu projede ölçülmemiştir; son raporda kalan risk.

### Sınanacak beklenti (tur 3)

1. **Üst band.** Gerçek bandı ≥7 olan örneklerde genel sapma −1,50'den **−0,75'in içine** girmeli
   ve en az bir örnek **7,5 veya üstü** almalı. Bu turun asıl sınavı budur.
2. **Tutarlılık.** ≥7 aralığında −2,17'den **−1,00'in içine** girmeli.
3. En büyük tek sapma **2,0'ın altına** inmeli.
4. Eğilim −0,70'ten **−0,35'in içine** girmeli.
5. **Orta band bozulmamalı.** 5–6,5 aralığı şu an −0,29; **+0,25'i geçmemeli**. Asıl risk bu:
   11, 12, 13, 14, 15, 16 numaralı değişikliklerin hepsi yukarı yönlü. Hepsi birden aşırı iterse
   orta band cimrilikten cömertliğe geçer ve düzeltme hedefi ıskalar.
6. **Alt band.** ≤4,5 aralığı +0,50'den yukarı **çıkmamalı**. 18 numaralı değişiklik aşağı yönlü,
   diğer altısı yukarı yönlü; alt bandda net etkinin ne olacağı bu düzeltmenin en belirsiz yeri.
7. Saklı küme (S1) ile görünür kümeler arasındaki fark **açılmamalı** (tur 2'de 0,14 band).

---

## 3. düzeltme — 2026-08-09

| | |
|---|---|
| Ölçüm | `RAPOR-tur3.md` (23 örnek × 3 puanlama, yazma) · `RAPOR-tur5.md` (gerçek bandı ≤4,5 olan 4 yazma örneği × 3 puanlama, alt banda nişan alan ek tur). Bağlam için `RAPOR-tur4-GENEL.md` (12 konuşma örneği × 6 puanlama — projenin **ilk konuşma ölçümü**) |
| Görülen kümeler | **S1 + S3** |
| SAKLI küme | **S2** — o kümenin hiçbir örneğine, cevabına, gerçek bandına, ölçüt puanına veya sapma satırına bakılmadı; `RAPOR-tur<N>-S2.md` dosyaları ve `olcum/tur<N>/AC-T2-2A-A-*.json` puanlamaları hiç açılmadı |
| Değişen dosyalar | `ORTAK-KURALLAR.md`, `yazma-task1-academic.md`, `yazma-task1-general.md`, `yazma-task2.md`, `konusma.md` |
| Tanı scripti | `tools/_a4_alt.py` — `kumeler.json`'daki **S1+S3'e kilitli**; gerçek bandları yalnız izinli kümelerin rapor dosyalarından okur |

Bu tur saklı küme koruması bakımından öncekilerden temiz: `puanlama-raporu.py` artık kümeye
bölünmüş rapor üretiyor, dolayısıyla 2. düzeltmedeki "tek tabloda hepsi göründü" sorunu tekrarlamadı.
Birleşik `RAPOR-tur3.md` / `RAPOR-tur5.md` dosyalarının yalnız **özet bölümü** (satır 1–32) okundu;
"Örnek örnek" tablosuna hiç inilmedi, örnek düzeyindeki her şey S1 ve S3 dosyalarından alındı.

### 2. düzeltmenin beklentileri tuttu mu

Aşağıdaki sayılar tur 3'ün **S1+S3** örneklerinden (n=15) hesaplandı; 2. düzeltmenin tablosu o
oturumun görünürleri olan S2+S3'ten (n=15) hesaplanmıştı. Ortak olan yalnız S3, yani karşılaştırma
küme bileşimi farkı taşıyor — yön güvenilir, ondalık değil.

| Beklenti | Sonuç |
|---|---|
| 1. ≥7 aralığında genel sapma −1,50 → −0,75 içi, en az bir 7,5+ | 🟡 **KIL PAYI KALDI** — −0,86. Ama hareket büyük ve doğru yönde; 7,5 iki kez verildi, konuşmada 8,0 ve 8,75 çıktı. Ölçeğin üst ucu ilk kez gerçekten açıldı |
| 2. ≥7 aralığında tutarlılık ölçütü −2,17 → −1,00 içi | 🟡 **KIL PAYI KALDI** — −1,14. En büyük tek kazanç bu |
| 3. En büyük tek sapma 2,0'ın altına | 🔴 **KALDI** — 2,50 (`RAPOR-tur3-GENEL.md`) |
| 4. Eğilim −0,70 → −0,35 içi | ✅ **GEÇTİ** — −0,326 |
| 5. Orta band (5–6,5) +0,25'i geçmemeli | ✅ **GEÇTİ** — −0,07. Orta band artık pratik olarak yerinde |
| 6. Alt band (≤4,5) +0,50'den yukarı çıkmamalı | 🔴 **KALDI, hem de tek yönlü** — tur 3'te **+0,92**, alt banda nişan alan tur 5'te **+1,28**. 18 numaralı değişiklik (5-4 ayrımı) tek başına diğer altı yukarı yönlü değişikliği tutamadı |
| 7. Saklı kümeyle (S1) fark açılmamalı | 🟡 tur 2'de 0,14 → tur 3'te **0,25** (S1 0,750 · S3 0,500), tur 4'te **0,625** (S1 0,875 · S3 0,250). Tur 4'ün farkı tek bir örnekten geliyor (n=4'lük kümelerde bir örnek 0,3 band oynatıyor), ama eğilim yanlış yönde ve **son raporda risk olarak yazılmalı** |
| — | Tur 4 tutarlılığı 🔴 **KALDI** (yayılım 0,79). Yazmada iki turdur ≤0,28 olan yayılım, konuşmada altı tekrarla ilk kez ölçüldü ve sınırı aştı |

Özet: 1. ve 2. düzeltme **üst bandı ve orta bandı** düzeltti — bu iki iş büyük ölçüde bitti.
Aynı değişikliklerin **hiçbiri alt bandda sınırlı değildi** ve alt band bunun bedelini ödedi.

### Ölçüm ne dedi (yalnız S1+S3)

Band aralığı × ölçüt (ölçüt bandı − gerçek genel band):

| Tur | Gerçek band | n | görev | tutarlılık | kelime | dilbilgisi | genel |
|---|---|---|---|---|---|---|---|
| 3 | ≤ 4,5 | 2 | **+1,17** | **+1,33** | +0,17 | +0,33 | **+0,92** |
| 3 | 5 – 6,5 | 7 | −0,10 | +0,14 | −0,17 | −0,71 | −0,07 |
| 3 | ≥ 7 | 6 | −1,11 | −1,14 | −0,67 | −0,89 | −0,86 |
| 5 | ≤ 4,5 | 3 | **+1,56** | **+1,89** | +0,78 | +0,56 | **+1,28** |

Sapma artık **iki uçta**, ve alt uç daha büyük. Alt bandda şişme **tek tip değil**: kelime ve
dilbilgisi ölçütleri neredeyse yerinde (+0,6/+0,8), **görev ve tutarlılık** ölçütleri 1,5–1,9 band
yukarıda. Gerçek bandı 3,0 olan bir cevap ürün üzerinde **4,5** görünüyor; gerçek bandı 4,0 olan
iki cevap **5,0** ve **5,5** görünüyor. Kullanıcı tarafında bunun anlamı: hazır olmayan aday
"orta seviyeye yaklaşmışım" sonucunu alıyor.

#### Örüntü F — tablo satırları simetrik değil, ama okuma yordamı simetrik

Bu turun asıl bulgusu. Üst bandın satırları **başarı** tarif eder (bir cevap ya genel bakışı
vermiştir ya vermemiştir), alt bandın satırları ise **eksiklik** tarif eder — ve eksiklikler
iç içe geçer: band 4'e uyan bir cevap band 5 satırını da "doğru" okutur, band 3'e uyan bir cevap
4 ve 5 satırlarını da doğru okutur.

11 numaralı değişiklik ("tabloyu 9'dan aşağı oku, **hâlâ doğru olan ilk satırda dur**") üst bandda
tam olarak istendiği gibi çalıştı — ölçeğin tavanı açıldı. Alt bandda ise aynı kural yapısal olarak
yanlış: iç içe geçmiş eksiklik satırlarında "hâlâ doğru olan ilk satır" **her zaman fazla yüksektir**.
Model 5'te duruyor, çünkü 5 satırı doğru; 4 satırının **daha** doğru olduğuna hiç bakmıyor.

#### Örüntü G — özellik bulunuyor, başarı sanılıyor

Tur 5'in gerekçelerinde tekrar eden biçim: cevabın becerdiği tek bir şey adlandırılıyor ve band o
şeyi izliyor. Bir yan cümle "yapısal iddia" sayılıyor, iki satır boşluğu "paragraflama" sayılıyor,
üç maddeden ikisine değinmek "kapsama" sayılıyor, çözülebilen bir öbek "iletişim" sayılıyor.
12 numaralı değişiklik üst band için "kusur bulmak diskalifiye değildir" diyor; **alt band için
karşılığı yazılmamıştı**: özelliğin *bulunması* onun *başarılması* değildir.

#### Örüntü H — gerekçe kuralı bu sefer yukarı bastırıyor

15 numaralı değişiklik `why`'ın ilk cümlesini "bandı ne hak ettiriyor" cümlesi yaptı; üst bandda
işe yaradı (tutarlılık −2,17 → −1,14). Alt bandda ters çalışıyor: model önce bir güçlü yan bulmak
zorunda, bulduğu tek güçlü yanı yazıyor, sonra **bandı o cümleye göre** veriyor. Gerekçe biçimi
puanın çapası hâline geldi.

#### Örüntü I — tavan hâlâ taban gibi çalışıyor, ama artık ölçülebilir biçimde

Üç örnekte de verilen ölçüt bandı, tetiklenen tavanın değerine **birebir eşit**. 1. düzeltme
"tavan puan değildir" dedi, 2. düzeltme "tavana eşit yazmadan önce satırı doğrula" dedi; ikisi de
**yasak** biçiminde yazıldığı için model yasağı çiğnemeden tavana oturabiliyor — satırı "doğruladı",
çünkü o satır (iç içe geçme yüzünden) gerçekten doğru. Kural pozitif bir yükümlülüğe çevrilmeli.

#### Örüntü J — konuşma (tur 4, ilk ölçüm) — kayda geçiyor, bu turda dokunulmuyor

Konuşma genel olarak projenin en iyi tarafı (MAE 0,583 · eğilim −0,250 · üst uçta 8,0 ve 8,75).
İki ölçülmüş örüntü var: (a) **kelime ölçütü orta bandda sistematik +0,5/+0,75**, üç ölçüt içinde
en yükseği; (b) **yayılım 0,79** ile tutarlılık ölçütü ilk kez kaldı, ve yayılımın çoğu kelime
ölçütünün tekrarlar arası 6,5/7/7,5 salınımından geliyor. İkisine de bu turda dokunulmadı;
gerekçe aşağıda.

### Yapılan değişiklikler

Hepsinin ortak mantığı: **2. düzeltmenin üst band kuralları neyse, alt bandda aynası yazıldı.**
Hiçbiri ölçeğin üstüne dokunmuyor — her biri açıkça "6 ve altı satırlar" / "ölçeğin alt ucu"
diye sınırlandı, çünkü üst band ve orta band şu an çalışıyor ve bozulmamalı.

| # | Örüntü | Değişiklik | Beklenen etki |
|---|---|---|---|
| 19 | F — "hâlâ doğru olan ilk satır" alt bandda hep fazla yüksek | STEP 2'ye **alt band okuma kuralı** eklendi (12 numaralı üst band kuralının aynası): 6 ve altı satırlar eksiklik tarif eder ve **üst üste binerler**; bir satırda durduğunda **altındaki satırı da oku**, ikisinden hangisi cevabı daha iyi anlatıyorsa o; alt satır açıkça fazla sert olana kadar inmeye devam et. "Çelişmediğin en yüksek satır" değil, "cevabı **anlatan** satır". STEP 2 rule 3'e de "bu durma testi yalnız 7 ve üstü için tamdır" notu düşüldü | Alt bandda görev (+1,56) ve tutarlılık (+1,89) şişmesinin ana kısmı kapanır; 3 ve 4 satırları ilk kez erişilebilir olur |
| 20 | G — özelliğin varlığı başarısı sanılıyor | STEP 2'ye **"özelliğin bulunması onun başarılması değildir"** kuralı eklendi: alt bandda soru "cevabın becerdiği bir şey bulabiliyor muyum" değil "okuyucu aradığını alıyor mu"; bir yan cümle range değildir, iki satır boşluğu paragraflama değildir, bir maddeye değinmek kapsama değildir, çözülebilen bir öbek iletişim değildir. Cevabın becerdiği bir şey **3 yerine 4** vermenin gerekçesidir, 5–6'nın değil | Tur 5 gerekçelerindeki "şu var, demek ki 5" adımı kırılır |
| 21 | I — tavan hâlâ taban | Tavan kuralı **yasaktan yükümlülüğe** çevrildi: tavan değerine eşit bir band **iki kez hak edilmelidir** — tavan izin vermeli **ve** tablo satırı cevabı kendi başına anlatmalı. Tavan bir şeyler yanlış olduğu için tetiklenir, dolayısıyla tablodan okunan band genellikle tavanın **altındadır**, eşiti değil; tam tavana oturmak, tavanın puan olarak kullanıldığının işaretidir. Aynı ölçütte iki tavan tetiklendiyse **en düşük tavanın altındaki satırlar okunur** | Üç örnekte de görülen "verilen band = tavan değeri" örtüşmesi kırılır |
| 22 | H — gerekçe biçimi puanın çapası | BLOK G / STEP 5'e bir madde eklendi: ilk cümlede güçlü yanı adlandırmak **biçim** gereğidir, **bandın kanıtı değildir**; ölçeğin alt ucunda o çoğu kez oradaki tek güçlü yandır ve cevabı ait olduğu satırdan yukarı taşımaz. "Adlandırdığın güçlü yan bandın yükselme sebebiyse, cevabı değil kendi yazdığın cümleyi puanlamışsındır." **Çıktı uzamıyor** — `why` yine en fazla 2 cümle, 15 numaralı kural aynen duruyor | Alt bandda gerekçe kaynaklı yukarı baskı kalkar, üst banddaki kazanç korunur |
| 23 | Alt bandda tutarlılık en kötü ölçüt (+1,33 → +1,89) ve **hiçbir ölçütte alt sınır notu yoktu** | 18 numaralı değişiklikte yalnız görev ölçütüne yazılan **"5'e karşı 4"** notu, üç yazma dosyasında **tutarlılık, kelime ve dilbilgisi** ölçütlerine de yazıldı ve **"4'e karşı 3"** ile uzatıldı (tanım netleştirmesi, örneğe özel kural değil): · **tutarlılık** — 5'te okuyucu takip eder ama işin bir kısmını kendi yapar, 4'te sırayı okuyucu kurar, 3'te ilişkiler hiç kurtarılamaz; sayfadaki boşluk her blok bir fikir tutmuyorsa paragraf değildir, ve **cümle sınırları çökmüşse konuların makul sırada gelmesi 6'ya yetmez** · **kelime** — 5'te okuyucu anlar ve zorlanmayı fark eder, 4'te yer yer bağlamdan çıkarır, 3'te kelime hiç kurtarılamaz; **yazım burada tam sayılır**, harf harf çözülen bir içerik kelimesi 4–3'tür, kararlı bir okuyucunun sonunda anlaması onu 5 yapmaz · **dilbilgisi** — BLOK K'nin sayım disiplini **tek yönlüdür**, sayım gerçekten "neredeyse her cümle" diyorsa band 4 veya 3'tür ve bu satırlar olağan sonuçlardır; range için verilen yarım band payı tek başına satır sınırını aşırtmaz | Alt bandda tutarlılığın +1,89'u ve kelimenin +0,78'i daralır. Üst banda dokunmaz: notların hepsi 5-4-3 sınırını tanımlıyor |

19, 20, 21, 22 **beş dosyada da** aynı (ortak bloklar; `ORTAK-KURALLAR.md` bakım kuralı).
23 yalnız üç yazma dosyasında ve her ölçütün kendi dilinde — gerekçesi aşağıda.

### Bilerek yapılmayanlar

- **Örneğe özel hiçbir kural yazılmadı.** Hiçbir örnek kodu, konusu, cevabı, gerçek bandı,
  görev türüne özgü içeriği veya sınav görevlisi yorumundan bir cümle talimata girmedi. Bütün
  değişiklikler band aralığı × ölçüt kırılımına ya da yordamın yapısına dayanıyor.
- **Üst bandın ve orta bandın hiçbir kuralı gevşetilmedi/sertleştirilmedi.** 12, 13, 15, 16, 17
  numaralı değişiklikler olduğu gibi duruyor. Bu turun bütün değişiklikleri "6 ve altı" / "ölçeğin
  alt ucu" diye açıkça sınırlandı. 1. ve 2. düzeltmenin dersi buydu: sınırlandırılmamış bir kural,
  hedeflemediği uçta ters yönde çalışıyor.
- **Tavan değerleri (max 5 / max 6) ikinci kez derecelendirilmedi.** 13 numaralı değişiklik üst
  bandda tuttu (tutarlılık −2,17 → −1,14). Alt banddaki sorun tavanın **değeri** değil, tavana
  **oturulması**; düzeltilen o (21).
- **Hata payı tablosunun eşikleri üçüncü kez kaydırılmadı.** Alt bandda dilbilgisi zaten en az
  sapan ölçütlerden (+0,56); eşiği oynatmak orta bandı bozardı.
- **Yuvarlama kuralı değiştirilmedi.** 5+5+3+4 = 4,25 → 4,5 yuvarlaması alt bandda yukarı itiyor
  ama `,25 yukarı` **gerçek IELTS kuralıdır**; ürünü gerçekten uzaklaştırırdı. Alt band ölçüt
  düzeyinde düzeltilir, aritmetikle değil.
- Ölçüt sayısı ve ağırlığı değişmedi (yazma 4, konuşma 3). Telaffuz geri getirilmedi.
  Çıktı uzunluğu sınırları değişmedi. `cikti-semasi.json` değişmedi.
- **Konuşmaya özgü hiçbir yeni kural yazılmadı** — `konusma.md` yalnız 19–22 ortak bloklarından
  değişti, 23 numaralı alt sınır notları yazma dosyalarına yazıldı. Sebep: konuşmada gerçek bandı
  **5'in altında tek bir örnek yok**; en düşük konuşma örneği band 5 ve o doğru puanlanıyor
  (+0,08). Konuşmanın alt ucu **ölçülmemiştir**, 23'ü oraya genellemek ölçüme dayanmayan bir
  değişiklik olurdu.
- **Konuşmada kelime ölçütünün +0,5/+0,75'i ve yayılım 0,79 bu turda düzeltilmedi.** İkisi de
  gerçek ve ölçülmüş (Örüntü J), ama: tek turluk konuşma verisi var; kelime ölçütünün 7 kapısı
  ("dördü sayabiliyorsan 7 açıktır") üst bandı açan şeyin ta kendisi ve konuşmanın üst ucu şu an
  projenin en iyi çalışan parçası; aynı turda hem alt bandı hem konuşma kelimesini itmek, 2.
  düzeltmenin yaptığı hatanın tekrarı olurdu (aynı yöne bakan çok sayıda değişiklik → hedefi
  aşma). Tur 6'da alt band düzelirse **4. sırada bu ele alınmalı**; düzelmezse yine beklemeli.

### 🔴 Ölçümün kapsamı hakkında

- Alt band ölçümü hâlâ **çok az örneğe** dayanıyor: tur 5'te görünür kümede **3 örnek**
  (gerçek band 3,0 · 4,0 · 4,0). Yön çok net (üç örnekte de aynı iki ölçüt, aynı büyüklükte) ama
  **band bazlı ince ayar bu veriyle yapılamaz**. Gerçek bandı 3'ün altında **hiç örnek yok**.
- Konuşmada **Part 1 örneği yok**; konuşmanın alt ucu (band 5'in altı) yok.
- Puanlayan, talimatı yazan ve örnekleri seçen aynı model ailesi — ortak kör noktalar bu ölçümde
  görünmez.

### Sınanacak beklenti (tur 6)

1. **Alt band.** ≤4,5 aralığında genel sapma **+1,28'den +0,50'nin içine** inmeli. Bu turun asıl
   sınavı budur.
2. **Alt bandda tutarlılık ölçütü** +1,89'dan **+0,75'in içine**, **görev ölçütü** +1,56'dan
   **+0,75'in içine** inmeli.
3. Gerçek bandı 3,0–4,0 olan örneklerin en az birinde **4,0 veya altı** bir tek seferlik puan
   görülmeli. Ürün iki turdur alt uçta 4,5'in altına hiç inmedi.
4. **Üst band bozulmamalı** — asıl risk bu. ≥7 aralığı şu an −0,86; **−1,10'un altına
   düşmemeli**. 19, 20, 21, 22, 23 numaralı değişikliklerin hepsi aşağı yönlü; hepsi "6 ve altı"
   diye sınırlandı ama sınırın tutup tutmadığını yalnız ölçüm söyler. Üst band −1,10'un altına
   düşerse **sınır tutmamıştır ve bu düzeltme geri alınmalıdır**.
5. **Orta band bozulmamalı.** 5–6,5 şu an −0,07; **−0,35'in dışına çıkmamalı**.
6. Eğilim: yazmada −0,326'dan sıfıra doğru gitmeli, **−0,25 ile +0,10 arasında** kalmalı.
7. Saklı küme (bu turda S2) ile görünür kümeler arasındaki fark **açılmamalı**. Tur 3'te 0,25,
   tur 4'te 0,625 idi; büyürse ayar örneklere ezberlenmiş demektir.
8. Konuşma **dokunulmadığı için sabit kalmalı**: MAE 0,583 ± 0,15. Konuşma bozulursa, bozan şey
   ortak bloklardır (19–22) ve o zaman ortak blokların konuşmaya taşınması sorgulanmalı.
