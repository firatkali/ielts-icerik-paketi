# DENETİM RAPORU — 2. tur

- **Tarih:** 2026-08-09
- **Denetleyen:** Fable (Claude ailesi) — 2. denetim turu, 3. ve son çalıştırma
- **Kaynaklar:** `denetim/envanter.md` · `denetim/capraz-ozet.md` (bu turun ilk iki
  çalıştırması) · `kalibrasyon/olcum/SONUC.md` + `SONUC-konusma.md` ·
  `content/DOGRULAMA/RAPOR.md` + `RAPOR-2.md` + `METINSIZ-RAPOR-2.md` + `SESSIZ-RAPOR.md`
  + `ANLAM-DUZEYI-RAPOR.md` + `ISARET-GEREKCELERI.md` · sayısal ölçü raporu
  `content/DOGRULAMA/OLCU-reading.md` (ham: `kalibrasyon/olcu/*.json`) ·
  1. tur arşivi `denetim/tur1/`
- **Kural:** Bu rapor durum tespiti yapar, karar vermez. Hiçbir içerik dosyası
  değiştirilmedi; bütün eleme/kabul kararları proje sahibinindir. Sayılar önceki
  raporlardan kopyalanmadı, dosyalardan yeniden ölçüldü.

---

## 0. KARARLAR — 2026-08-11 (proje sahibi)

Raporun §5'inde açık bırakılan maddelerin üçü karara bağlandı. Bu bölüm rapora sonradan
eklendi: §5 durum tespitidir ve olduğu gibi duruyor, burası ne yapılacağını söyler.

**Yürütme değişti:** içerik işi artık dışarıya verilmiyor, proje sahibi + asistan
yapıyor. Yani aşağıdaki üç madde "birinden beklenen" değil, sıradaki iş.

| # | Karar | Seçilen yol |
|---|---|---|
| **B3** | Aynı pasaj/senaryo birden çok pakette — alıştırma, testin cevabını düz metin veriyor | **(a) "bir olgu, bir paket" taraması.** Kanıt-çakışması aracı paket arası köke genişletilecek; en acil çiftler §5-B3'te listeli. Gerçek kullanıcıyı da etkileyen tek sızıntı kanalı olduğu için **önce bu**. |
| **B1** | 121 işaretli dinleme sorusu | **(b) mekanizma bazında elden geçirme.** Tip tip gidilecek: `secenek_sozu`+`cerceve_sozu` (49 kalem) yazım işi, `genel_kultur` (43) senaryo/konu değişikliği, `capraz_sizinti` (10) B3'e bağlı — B3 bitmeden başlanmaz. Atma seçeneği elendi: altı testin altısı da 40 sorunun altına düşerdi. |
| **B2** | Reçetesi tükenen iki okuma tipi (cümle tamamlama, cümle sonu eşleştirme) | **(b) yeniden üretim.** Üçüncü elden geçirme turu elendi — iki ölçüm de düzelmediğini gösterdi. **Havuzdan çıkarma da elendi:** iki tip de gerçek sınavda çıkıyor, çıkarmak adayı hazırlıksız bırakır; sorun tipin kendisinde değil, sorunun yazımında. Cümle sonu eşleştirmede E7'nin reçetesi bağlayıcı: yanlış sonlardan en az ikisi aynı köke anlamca oturacak. |

**Üçüne birden geçerli kabul şartı:** yeniden üretilen ya da elden geçirilen her soru,
onu işaretleyen ölçümün aynısından geçecek. Ölçümsüz düzeltme "düzeltildi" sayılmaz —
E5/E6 turunda tam olarak bu yüzden iki tip elde patladı.

**Açık kalanlar (karar verilmedi):** B4 (gerçek olaya dayalı pasajlar) · B5 (konuşma
puanlamasının üç eksiği) · B6 (ezber şüphesi) · B7 (dil kalıntıları) · B8 (boş
`flag_mechanism`) · B9 (iki çift-cevap sorusu) · B10 (görsel tipler hiç ölçülmedi) ·
B11 (ertelenmiş puanlama küçükleri).

---

## 1. Genel durum

Birinci turun on iki açık maddesinden onu kapatılmış ya da ciddi ilerletilmiş durumda:
cevap anahtarları ikinci kör ölçümde de içerik düzeyinde pratikte %100 çıktı, okumanın
işaretli stoku 180'den 116'ya indi, dinlemenin hiç yapılmamış sızıntı ölçümü beş
çalıştırmayla yapıldı, puanlama üç düzeltme sonunda yazmada ilk kez ölçütleri tutuyor ve
kullanıcıya görünen alanlar İngilizceye çevrildi. Buna karşılık teslim önünde iki büyük
karar yükü duruyor: dinleme ölçümü 121 yeni işaret getirdi (kullanılabilir dinleme
232/360'a indi; altı dinleme testinin hiçbiri işaretsiz değil) ve iki okuma tipinde
(cümle tamamlama, cümle sonu eşleştirme) elden geçirme reçetesinin işlemediği ölçümle
sabit. Konuşma puanlaması ortalamada iyi ama uçlarda riskli (iki örnekte −1,5 band,
tutarlılık son düzeltmeden sonra hiç ölçülmedi) — içerik, işaretliler ve konuşma
tutarlılığı hakkında karar verilmeden "teslim edilebilir" denemez.

---

## 2. Sayılar

Kaynak: `denetim/envanter.md` (ayrıntılı tablolar orada; hepsi bu turda yeniden sayıldı).

| Beceri | Hedef | Üretilen | İşaretli | Kullanılabilir | 1. turda kullanılabilir |
|---|---:|---:|---:|---:|---:|
| Okuma | 400 | 400 | 122 | **278** | 220 (▲ +58) |
| Dinleme | 360 | 360 | **128** | **232** | 360 görünüyordu (ölçülmemişti) |
| Konuşma | 440 | 440 | 0 | 440 | 440 (ölçüm kapsamı dışında) |
| Yazma | 110 | 110 | 0 | 110 | 110 (ölçüm kapsamı dışında) |
| **Toplam** | **1.310** | **1.310** | **250** | **1.060** | 1.130 |

(İşaretli sayısı kalem bazında 237, soru numarası bazında 250 — çift cevaplı çoktan
seçmeliler 2 numara sayılır.)

Destek malzemesi tam (12+6 pasaj, 24 senaryo), 12 tam test 40/40, şema hatası 0, boş
cevap anahtarı/açıklama yok, askıda (`review`) soru kalmadı (1. turda 2 vardı).
Kanıt alanı boş 23 NOT GIVEN sorusunun tamamına negatif gerekçe yazılmış (1. tur A6
kapalı).

Kullanılabilir stokun en dar yerleri:

| Soru tipi (test + alıştırma) | Üretilen | Kullanılabilir | 1. turda |
|---|---:|---:|---:|
| Okuma: cümle sonu eşleştirme | 10 | **1** | 0 |
| Okuma: akış şeması | 6 | **2** | 2 |
| Dinleme: eşleştirme | 43 | **14** | ölçülmemişti |
| Dinleme: çoktan seçmeli (tek+çok) | 63 | **18** | ölçülmemişti |
| Dinleme: özet tamamlama | 15 | 6 | ölçülmemişti |
| Dinleme: kısa cevap | 28 | 13 | ölçülmemişti |
| Okuma: özet tamamlama | 43 | 16 | 17 |
| Okuma: çoktan seçmeli | 39 | 15 | 9 |

1. turda sıfıra inen üç okuma tipinden ikisi toparladı (YNNG 0→14, MC 9→15), biri
toparlamadı (MSE 0→1; E7 raporu: "rakip-ekleme bu tipte yetmedi").

---

## 3. Kalite

Ayrıntı `denetim/capraz-ozet.md`; burada birleşik özet.

**Cevap anahtarları iki turda da sağlam.** İlk çapraz doğrulama 743 soruda içerik
düzeyinde pratikte %100; E5/E6 sonrası değişen 188 sorunun E7 kör ölçümü %98,9 (E6'nın
72 yeni sorusunun 72'si uyuştu). Ayakta kalan tek şey 2 çift-cevap vakası (practice
MH-15, GT1 özet-40) — ikisi de işaretli, karar bekliyor. 1. turun tek açık anahtar
eksiği (`40 minutes` varyantı) kapatılmış, dosyada doğrulandı.

**Sızıntı cephesinde tablo iki yönlü değişti:**

- **Okuma düzeldi ama seçici biçimde.** Elden geçirme + yeniden üretim sonrası: MC
  %100→%62, YNNG %100→%39, TFNG %53→%12, MF %69→%31, MH %18→%4. Buna karşılık iki tip
  düzelmedi: `sentence_completion` E7'nin kendi kabul ölçütünde kaldı (%43 > resmî taban
  %20; ana mekanizma eşdizim kilidi), `matching_sentence_endings` yerinde saydı (9/10
  hâlâ parçasız çözülüyor). Ölçüt de sıkılaştı: 1. turun kelime-düzeyi sayıları yerine
  artık anlam düzeyi (K3) sayılıyor — tamamlama ailesindeki oran artışları kötüleşme
  değil, ölçütün körlüğünün kalkması.
- **Dinleme ilk kez ölçüldü ve okumadaki desen aynen çıktı.** 304 kalem, 3'er tur,
  senaryo gösterilmeden: seçenekli tipler %67-88 sızdırıyor (eşleştirmede seçenek sözü
  mekanizması %89), tamamlamada alan-terimi boşlukları %52-60, sayı/ad soran kalemlerde
  sızıntı 0/117. 121 kalem işaretlendi; işaretler soru-özel gerekçeli (1. turun tek-tip
  gerekçe kusuru burada baştan önlenmiş).

**Yeni yapısal bulgu — paket mimarisi sızdırıyor.** Aynı pasaj/senaryonun hem alıştırma
hem tam test paketlerinde kullanılması yüzünden birinin boşluğu diğerinin düz metni:
okumada E7 "3/3 bilinenlerin en az 20'si bu kanaldan", dinlemede `cross_question`
dayanaklı kalemlerin %91'i bilindi. Bu, tek tek soruların değil **havuz tasarımının**
kusuru; soru elden geçirmeyle kapanmaz.

**Ölçülmeyen yerler:** okuma diyagram etiketleme (10) + dinleme plan/harita (45) görsel
gerektirdiği için hiçbir sızıntı ölçümüne girmedi; konuşma/yazma içeriği (görevlerin
kendisi) hâlâ hiçbir doğruluk/sızıntı ölçümünden geçmedi. Oralarda "işaret 0" temizlik
değil, ölçüsüzlük.

**Dil tutarlılığı (önceki turdan açık madde):** kullanıcıya görünen alanlar İngilizceye
çevrilmiş — örnek cevaplardaki band gerekçeleri (`why_this_band`, `what_would_lift_it`,
42 dosya) ve yazma grafiklerindeki Türkçe birim adları dahil; bu denetimin taraması
kullanıcıya dönük alanlarda Türkçe kalıntı bulmadı (Çatalhöyük gibi özel adlar hariç).
Üç belirsiz kalıntı §5'te (B7).

---

## 4. Puanlama

Kaynak: `kalibrasyon/olcum/SONUC.md` + `SONUC-konusma.md`. 1. turdan bu yana: tur 3'ün
eksik GT-T2 grubu tamamlandı, konuşma ilk kez ölçüldü (tur 4), alt band turu (5) ve
3. düzeltme sonrası doğrulama turu (6) yapıldı.

**1. tur "4 ölçütten 2'si karşılanmıyor" diyordu. Bugün, doğrulama turunda (36 örnek):**

| Ölçüt | Hedef | 1. tur durumu | Bugün — yazma (24) | Bugün — konuşma (12) |
|---|---|---|---|---|
| Ortalama mutlak fark | < 0,5 | 🔴 0,694 | ✅ **0,354** | ✅ 0,458 |
| En büyük tek sapma | < 1,5 | 🔴 1,50 (sınırda) | ✅ en büyük 1,00 | 🔴 **2 örnek −1,5** |
| Eğilim | ±0,25 | ✅ −0,139 | ✅ −0,021 | 🔴 **−0,375** |
| Yayılım (tutarlılık) | ≤ 0,5 | ✅ 0,19 (o gün öyle görünüyordu) | ⚪ tur 6'da ölçülmedi; son gerçek ölçüm 0,28 ✅ (3. düzeltme ÖNCESİ) | ⚪ ölçülmedi; son gerçek ölçüm **0,79 🔴** (tur 4) |

Dürüst okunuşu:

- **Yazma hedefe geldi.** MAE 0,952 → 0,389 (eşleşik 21 örnekte 0,333); ≥1,5 band sapan
  yazma örneği kalmadı (1. ölçümde 7/21 idi); yazmada kullanıcıların %100'ü 1,0 band
  içinde puan alıyor. 1. turun en tehlikeli bulgusu — alt band şişmesi (gerçek 3,0'a
  4,5) — ölçüldü (tur 5: +1,25), düzeltildi, doğrulandı (tur 6: +0,38; gerçek 3,0 artık
  3,5 alıyor).
- **Konuşma ortalamada iyi, uçlarda kötü.** MAE 0,458 geçiyor ama 4 ölçütün yalnız 1'i
  temiz: band 7,5 ve 8,0 konuşmacılar 6,0/6,5 görüyor (üniversite eşiğinin iki yanı),
  eğilim cimrileşti, akıcılık ölçütü doğrulama turunda −0,12'den −0,58'e kaydı
  (mekanizması raporda teşhisli: iniş kuralı, yanlış yerleşimin üstüne biniyor).
  Konuşmanın tutarlılığı (0,79, iki örnekte 1,5 band savrulma) 3. düzeltmeden sonra
  **hiç ölçülmedi** — bugünkü değeri bilinmiyor.
- **Ezber şüphesi açık risk olarak duruyor.** Saklı küme farkı ilk iki düzeltmede 0,08
  iken 3. düzeltmede 0,292'ye çıktı ve yön ters döndü. Raporun kendi analizi küme
  zorluğunu daha olası buluyor ama ezberi eleyemiyor; tek ayıraç hiç kullanılmamış yeni
  örneklerle ölçüm.
- **Kapsam sınırları:** konuşmada Part 1 örneği 0, band 5 altı örnek 0; yazmada band 3,0
  altı örnek 0; alt band toplam 4 örnek. Okuma/dinlemenin "kaç doğru = hangi band" eşiği
  bu ölçümle doğrulanmaz; "tahmini band" ibaresi üründen kalkamaz (SONUC.md'nin kendi
  kapanışı).

---

## 5. Açık sorunlar — proje sahibinin karar vereceği maddeler

Önce 1. turun maddelerinin akıbeti, tek satırda: A2 (gerekçeler) ✅ · A3 (dinleme
ölçümü) ✅ · A4 (varyant) ✅ · A5 (askıdaki 2 soru) ✅ · A6 (boş kanıt) ✅ · A7 (anlam
ölçütü) ✅ · A8 (GT-T2) ✅ · A9 (alt band) ✅ · A12 (araç borçları) ✅ · A1 (işaretli
okuma) kısmen — 180'den 116'ya · A10 (konuşma ölçümü) kısmen — ölçüldü, tutarlılık
kaldı · A11 (kabul ölçütleri) kısmen — yazmada tuttu, konuşmada kalmaya devam.

Bugünün maddeleri (hiçbiri "yapıldı" değildir; seçenekler yazılı, karar proje sahibinin):

**B1 — 121 işaretli dinleme sorusu (bu turun en büyük yeni maddesi).** Kullanılabilir
dinleme 232/360; altı testin altısında işaret var (10-18/40), işaretliler atılırsa
hiçbir dinleme testi tam kalmaz. Seçenekler: (a) at ve testleri yeniden dengele;
(b) mekanizma bazında elden geçir — `secenek_sozu`+`cerceve_sozu` 49 kalem yazım işi,
`genel_kultur` 43 kalem senaryo/konu değişikliği ister, `capraz_sizinti` 10 kalem B3'e
bağlı; (c) seçenekli tiplerde (MC + eşleştirme, 96 soru) düzeltilmiş promptla yeniden
üretim. Okumanın E5/E6 deneyimi emsal: orada elden geçirme çoğu tipte işledi ama iki
tipte işlemedi — dinlemede de tip tip karar verilmeli.

**B2 — 116 işaretli okuma sorusu + reçetesi tükenen iki tip.** `sentence_completion`
ikinci ölçümde de tabana inmedi (%43 > %20), `matching_sentence_endings` 9/10 işaretli
ve E7 "rakip-ekleme yetmiyor" diyor. Seçenekler: bu iki tipte üçüncü bir elden geçirme
turu (veri, başarısını desteklemiyor) / yeniden üretim (MSE için E7'nin önerisi:
sonların en az ikisi aynı köke anlamca oturacak şekilde) / tipi havuzdan çıkarıp
yerine sağlam tiplerden üretim. Kalan işaretlilerde mekanizma kırılımı çapraz özetin
4. bölümünde.

**B3 — Paket mimarisi: aynı pasaj/senaryo birden çok pakette.** Çapraz sızıntı kanalı
soru düzeltmeyle kapanmıyor; alıştırma paketleri tam testlerin cevabını düz metin
veriyor. Seçenekler: "bir olgu, bir paket" taraması (E6'nın kanıt-çakışması aracının
paket-arası köke genişletilmesi) / alıştırmalar için ayrı pasaj-senaryo havuzu /
uygulamada alıştırma-test içerik ayrımıyla riski hafifletip belgeleme. En acil çiftler
raporlarda listeli (A08, A04/JWST, A05, G03, G06 + 8 dinleme senaryosu).

**B4 — Gerçek olaya dayalı pasaj/senaryolar.** JWST (A04), Kandula (A01), Britanya
mevzuatı (GT), PANAS/POMS (AC4), tohum bankası/plastik senaryoları: sayısal cevaplar
kamu bilgisi, soru yazımıyla düzelmez. Seçenekler: bu pasaj/bölümleri kurgusal ya da
az bilinen olaylarla değiştir / sorularını pasaja-özgü değerlere kaydır / riski kabul
edip belgele (gerçek adayın telefonu kapalı — sızıntının gerçek kullanıcıya etkisi
modele etkisinden küçük olabilir; ama alıştırma↔test sızıntısı gerçek kullanıcıyı da
etkiler).

**B5 — Konuşma puanlamasının üç eksiği:** (a) tutarlılık 3. düzeltmeden sonra ölçülmedi
(son değer 0,79 — sınırın %58 üstü); (b) akıcılık ölçütü doğrulama turunda kaydı,
teşhis konmuş düzeltme önerisi SONUC-konusma.md §3'te bekliyor; (c) Part 1 ve band<5
örneği hiç yok. Seçenekler: tekrarlı bir konuşma ölçüm turu (öncelik — düzeltmeden önce,
yoksa gürültüye ayar çekilir) / Part 1 + alt band örnek seti kurulması / mevcut hâliyle
yayınlayıp konuşma puanına "yazmadan daha az güvenilir" ibaresi.

**B6 — Ezber şüphesi (saklı küme farkı 0,292).** Tek ayıraç: hiç kullanılmamış
örneklerle bir ölçüm turu. Seçenekler: yeni örnek toplayıp tur 7 / riski belgeleyip
canlı kullanıcı verisiyle sınamayı bekle. "Kalibrasyon bitti" cümlesi bu yapılmadan
kurulamaz (SONUC.md'nin kendi ifadesi).

**B7 — Küçük dil kalıntıları (kullanıcıya görünürlüğü belirsiz):** konuşma kartlarındaki
`card_type` değerleri Türkçe (`kişi`/`nesne`/`olay`/`yer`/`soyut`, 60 dosya) ve 69
kartta `topic_tr` alanı var (adı gereği bilinçli Türkçe olabilir); bir dinleme
senaryosunda tek `pace` değeri Türkçe ("olcülü"). Uygulama bu alanları ekrana
basıyorsa çevrilmeli; basmıyorsa dokunulmasın. Karar, alanların üründe kullanımına
bağlı — bu depodan görünmüyor.

**B8 — 26 okuma işaretinde `flag_mechanism` boş.** E7'nin işaretlediklerinin bir kısmı;
gerekçe metninde dayanak var ama alan doldurulmamış. B2'de elden geçirme seçilirse önce
doldurulmalı (E1 dersi: yanlış/eksik gerekçe yanlış düzeltmeye yönlendirir). Mekanik,
küçük iş.

**B9 — İki çift-cevap sorusu** (practice MH-15 "v↔ii", GT1 özet-40
"prevention↔reductions"). Seçenekler: varyant ekle / boşluğu-başlığı tek adaylı hâle
getir. Tek satırlık işler; E7 bilerek karara bırakmış.

**B10 — Görsel tipler hiçbir ölçümden geçmedi** (okuma diyagram 10 + dinleme
plan/harita 55 kalem). Seçenekler: görsel destekli ayrı bir ölçüm turu tasarla / bu
tiplerin payını küçült / riski belgeleyip kabul et.

**B11 — Puanlamanın bilinen, bilinçli ertelenen küçükleri:** konuşmada kelime ölçütü
orta bandda +0,60, dilbilgisi ölçütü her ölçümde en cimri (üst bandda −0,86…−1,00),
AC-T1-1C-A örneği dört ölçümün üçünde +1,0 (ikinci örnek gelmeden kural yazılmamalı —
raporun kendi kısıtı doğru). Bir sonraki düzeltme turunun gündem listesi; şimdi
yapılacak iş yok, unutulmasın diye kayıtta.

---

## 6. Denetimin sınırları

1. **Denetçi, üreticilerle aynı model ailesinden.** Soruları Fable/Opus üretti, elden
   geçirmeyi Opus yaptı, ölçümleri Fable/Opus koştu, bu raporu Fable yazdı. Ailenin
   ortak kör noktası — iki modelin de doğru sandığı yanlış, ikisinin de doğal bulduğu
   kusur — bu kurulumun hiçbir katmanında görünmez. Cevap doğruluğunun ve puanlamanın
   son sözü, farklı aileden bir modelle yapılacak ikinci süzgeçte; o süzgeç hâlâ
   yapılmadı ve bu turda da yerine geçen bir şey yok.
2. **Bu denetim raporları ve alan durumlarını denetledi, soruları yeniden çözmedi.**
   Sayımlar ve tek tek doğrulamalar (varyant eklemeleri, statü değişimleri) dosyalardan
   yapıldı; ama 1.310 sorunun içeriği bu turda da yeniden çözülmüş değil. Ölçüm
   raporlarının kendilerinin kaçırdığı şey burada da kaçar. Ayrıca E7/E8 raporlarının
   dürüstlük kayıtlarındaki kirlenme şerhleri (MSE ve E5-YNNG ölçümleri "tam kör"
   değil) bu raporun sayılarına aynen taşınır.
3. **Üç rapor tek oturumda, tek denetçi tarafından yazıldı** (envanter → çapraz özet →
   bu rapor). İlk iki raporun hataları üçüncüye taşınabilir; bağımsız üç göz değil,
   aynı gözün üç bakışıdır. Kayıt düşülür: bu turun 1. çalıştırması olarak sayaçta
   görünen iş yalnız 1. tur raporlarının arşive taşınmasıydı; üç raporun üçü de bu
   oturumda üretildi.
4. **Ölçülmeyen yerler hakkında bu rapor sessizdir:** görsel tipler (§5 B10), konuşma
   Part 1 ve band<5 (§5 B5), konuşma/yazma görev içeriklerinin kalitesi, okuma/dinleme
   band eşikleri (yalnız canlı veriyle sınanır), ve dinleme sızıntısının resmî
   karşılaştırma tabanı (hiç ölçülmedi; %41,1'in "yüksek mi normal mi" olduğu
   bilinmiyor — SESSIZ raporunun kendi sınırı).
5. **Karşılaştırma tabanları küçük:** puanlamada band başına 1-4 örnek, alt band 4
   örnek, konuşma 12 örnek/2 konu; okuma resmî sızıntı tabanı tip başına 3-6 soru.
   Yönler güvenilir, büyüklükler değil.
6. **"Gerçek sınav zorluğunda" iddiası bu projede hiçbir yöntemle doğrulanamadı** —
   sızıntı ölçümü bozuk soruyu bulur, zorluk ölçmez; zorluk ancak gerçek aday verisiyle
   ölçülür. Ürün metinlerinde bu iddiadan kaçınılmalı.
