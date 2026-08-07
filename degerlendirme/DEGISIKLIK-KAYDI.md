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
