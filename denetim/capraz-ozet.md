# Çapraz Kontrol Özeti — 2. tur (Denetim, 2. çalıştırma)

- **Tarih:** 2026-08-09
- **Kaynaklar:** `content/DOGRULAMA/` altındaki bütün raporlar ve JSON'lar — `RAPOR.md`
  (ilk çapraz doğrulama), `RAPOR-2.md` (E7 cevap anahtarı yeniden ölçümü),
  `METINSIZ-RAPOR.md` + `METINSIZ-RAPOR-2.md` (okuma parçasız çözüm, ilk + yeniden),
  `ANLAM-DUZEYI-RAPOR.md` (K3 ölçütü), `SESSIZ-RAPOR.md` (dinleme sızıntı, 5 çalıştırma),
  `ISARET-GEREKCELERI.md`, `ELDEN-GECIRME.md` — ve `content/` altındaki 237 işaretli
  sorunun `flag_reason` / `flag_mechanism` / `blind_basis` alanları (bu denetimde
  dosyalardan yeniden sayıldı).
- **1. tur karşılaştırması:** `denetim/tur1/capraz-ozet.md`.
- **Kural gereği bu rapor sadece durum tespiti yapar; hiçbir içerik dosyası değiştirilmemiştir.**

1. turdan bu yana kontrol mekanizması ikiden dörde çıktı:

1. **Cevap anahtarı (kör çapraz çözüm):** ilk tur 743 soru + E7 yeniden ölçümü 188 soru.
2. **Okuma parçasız çözüm:** ilk ölçüm 381 soru; E5/E6 düzeltmelerinden sonra değişen
   189 soru E7'de yeniden ölçüldü (K3 anlam düzeyi dahil).
3. **Anlam düzeyi ölçütü (E10):** eski kelime-düzeyi ölçümünün kaçırdığı sızıntıyı aynı
   tur dökümlerinden yeniden değerlendirdi.
4. **Dinleme sızıntı ölçümü (E8, YENİ):** 1. turun en büyük ölçüm boşluğu kapandı —
   304 dinleme kalemi senaryo gösterilmeden 3'er turda çözüldü.

---

## 1. Toplam sayılar

### 1a. Cevap anahtarı doğrulaması (kör çapraz çözüm, üretmeyen model)

| Ölçüm | Soru | Uyuşan | İçerik düzeyinde | Kalıcı işaret |
|---|---:|---:|---:|---:|
| İlk tur (CAPRAZ-90, 7 oturum) | 743 | 718 (%96,6) | pratikte %100 (24 biçim eksiği kapatıldı, 1 yanlış alarm) | 0 |
| E7 yeniden ölçümü (E5/E6 sonrası değişen 188 soru) | 188 | 184 (%97,9) | 186 (%98,9; 2 uyuşmazlık birim/varyant yanlış alarmı) | **2** |

E7'nin işaretlediği iki soru "yanlış cevap" değil "iki savunulabilir cevap" türünden:
`practice/matching-headings` 15 (v↔ii) ve `GT1/summary-completion` 40
(prevention↔reductions). İkisi de hâlâ `flagged` duruyor; karar bekliyor.
E6'nın 72 yeni sorusunun 72'si de anahtarla uyuştu. 1. turun açık bıraktığı tek anahtar
eksiği (`AC2/flow-chart` 1'e `40 minutes` varyantı) **kapatılmış** — dosyada doğrulandı.

**Cevap anahtarı cephesinin net sonucu 1. turla aynı: içerik düzeyinde pratikte %100.**
Toplamda 931 kör çözümden ayakta kalan gerçek uyuşmazlık 2 (ikisi de çift-cevap
belirsizliği).

### 1b. Sızıntı ölçümleri (işaretlerin kaynağı)

| Ölçüm | Kapsam | 3/3 bilinen | İşaret |
|---|---:|---:|---:|
| Okuma ilk ölçüm (B1, kelime düzeyi) | 381 | 180 (%47) | 180 → E5/E6 elden geçirme/yeniden üretimle bileşim değişti |
| Okuma E10 (anlam düzeyi, aynı dökümler) | aynı | cümle tam. %73, özet %93 (anlamca) | +~29 (bugün 25'i duruyor) |
| Okuma E7 yeniden ölçümü (E5/E6 sonrası 189 soru) | 189 | 82 (%43,4 K3) | 81 yeni + 1 eski |
| **Dinleme (E8, YENİ)** | 304 (352 kalemin ölçülebilenleri) | 125 K3 (%41,1) | **121** (dayanağı anlamsal olanlar) |

Bugünkü işaretli stok (dosyalardan sayıldı): **okuma 116 kalem** (122 numara) +
**dinleme 121 kalem** (128 numara) = **237 kalem / 250 numara.**

Okuma işaretlerinin kaynağı (gerekçe metninden sınıflandı):

| Kaynak | Kalem |
|---|---:|
| E7 parçasız yeniden ölçüm (K3, 3/3) | 81 |
| E10 anlam düzeyi ölçütü | 25 |
| E7 cevap anahtarı (çift-cevap) | 2 |
| "Belirsiz — net mekanizma yok" (E1'in sınıfladığı, E5'in elden çıkarmadığı) | 8 |
| **Toplam** | **116** |

---

## 2. Soru tipi bazında işaretlenme oranı

### Okuma (bugünkü durum, test + alıştırma birlikte)

| Soru tipi | Üretilen | İşaretli | Oran | 1. turda oran |
|---|---:|---:|---:|---:|
| Cümle sonu eşleştirme | 10 | 9 | **%90** | %100 |
| Özet tamamlama | 43 | 27 | **%63** | %60 |
| Akış şeması tamamlama | 6 | 4 | %67 | %67 |
| Çoktan seçmeli | 39 | 24 | **%62** | %100 |
| Cümle tamamlama | 37 | 15 | %41 | %35 |
| YES / NO / NOT GIVEN | 23 | 9 | %39 | %100 |
| Not tamamlama | 33 | 12 | %36 | %27 |
| Özellik eşleştirme | 26 | 8 | %31 | %69 |
| Tablo tamamlama | 27 | 5 | %19 | %33 |
| TRUE / FALSE / NOT GIVEN | 57 | 7 | %12 | %53 |
| Kısa cevap | 10 | 1 | %10 | %20 |
| Başlık eşleştirme | 45 | 2 | %4 | %18 |
| Bilgi eşleştirme | 49 | 1 | %2 | %6 |
| Diyagram etiketleme | 10 | — | ölçülemedi (görsel) | — |

Cümle tamamlama, not tamamlama ve özet oranlarının 1. turdan **yüksek** görünmesi
kötüleşme değil: E10/E7'nin anlam-düzeyi (K3) ölçütü, 1. turun kelime-düzeyi ölçütünün
göremediği sızıntıyı sayıyor (1. tur raporunun kendisi bu iyimserliği not etmişti).
E7'nin kendi kabul ölçütüne göre bir tip açıkça **düzelmedi**: `sentence_completion`
(%43 > resmî taban %20); `matching_sentence_endings` fiilen yerinde saydı (9/10).

### Dinleme (E8, K3; işaretlenme = 3/3 bilinen ∧ dayanak anlamsal)

| Soru tipi | Ölçülen kalem | İşaretli | Oran |
|---|---:|---:|---:|
| Çoktan seçmeli (çok cevaplı) | 8 | 4 kalem (8 numaranın 8'i değil — çift sayım numarada) | **%87,5 (3/3 bilinme)** |
| Çoktan seçmeli (tek) | 37 | 24* | %67,6 (3/3), işaretli %64,9 |
| Eşleştirme | 43 | 29 | **%67,4** |
| Özet tamamlama | 15 | 9 | %60,0 |
| Kısa cevap | 28 | 15 | %53,6 |
| Akış şeması | 25 | 13 | %52,0 |
| Not tamamlama | 40 | 10 | %25,0 |
| Cümle tamamlama | 39 | 8 | %20,5 |
| Tablo tamamlama | 29 | 4 | %13,8 |
| Form tamamlama | 40 | 5 | %12,5 |
| Plan / harita / diyagram | 45 | — | ölçülmedi (görsel) |

\* 3/3 bilinen 25'in 4'ü `number_guess` (şans oranında tutturma) — bilerek işaretlenmedi,
dosyada `blind_note` ile duruyor.

**Evet, işaretler iki beceride de aynı yerlerde yoğunlaşıyor:** yazılı seçenek/ifade
metni taşıyan tipler (çoktan seçmeli, eşleştirme, özet) en üstte; cevabı özel ad / sayı /
saat olan tipler (form, tablo) en altta — dinlemede bu düşüklük "iyi tasarım" değil,
o tiplerin yapısal tahmin edilemezliği (raporun kendi tespiti).

---

## 3. Üreten model bazında kırılım

Önemli şerh: `generated_by` alanı artık **son üreteni** gösteriyor. E6'nın yeniden
ürettiği ~41 okuma sorusu Fable yuvalarında olduğu hâlde `opus` imzalı; bu yüzden
1. turdaki "yuva = model" eşlemesi artık geçerli değil ve aşağıdaki tablo 1. turla
birebir kıyaslanamaz.

| Beceri, model (son üreten) | Soru | İşaretli | Oran |
|---|---:|---:|---:|
| Dinleme, fable (`FABLE5-43`: MC + eşleştirme) | 96 | 64 | **%66,7** |
| Dinleme, opus (`OPUS5-21`: form/tamamlama/plan) | 264 | 64 | %24,2 |
| Okuma, opus | 241 | 82 | %34,0 |
| Okuma, fable | 159 | 40 | %25,2 |

İki okuma net değişti: 1. turda Fable %62 / Opus %32 idi; E5/E6 sonrası %25 / %34.
Bu, Fable'ın ilk üretimdeki iki sistematik kusurunun (kip imzası, konumsal düzen)
elden geçirmeyle büyük ölçüde kapandığını, kalan yükün ağırlıkla Opus'un tamamlama/özet
ailesine (eşdizim kilidi + genel kültür + çapraz-pasaj) kaydığını gösteriyor.

Dinlemede ise 1. turun öngörüsü aynen doğrulandı: okumada %100 sızdıran prompt ailesinin
dinleme akrabası (`FABLE5-43`) ölçülür ölçülmez %66,7 ile en yüksek işaret oranını verdi.
**Aynı ailenin aynı hastalığı iki beceride bağımsız çıktı — bu artık desen, tesadüf değil.**

---

## 4. `flag_reason` temaları

1. turun bulgusu ("180 işaretin hepsinde birebir aynı cümle") **kapanmış**: E1 gerekçeleri
mekanizmaya göre yeniden yazdı, E7/E8/E10 işaretleri de baştan soru-özel gerekçeyle geldi.
Bugün 237 işaretin gerekçeleri soruya özgü; tema analizi artık `flag_mechanism` alanından
doğrudan yapılabiliyor (küçük istisna: 26 okuma işaretinde mekanizma alanı boş — gerekçe
metninde dayanak yazıyor ama alan doldurulmamış; envanter raporu §5).

Mekanizma dağılımı (dosyalardan sayıldı, kalem bazında):

| Mekanizma | Okuma | Dinleme | Toplam | Ne demek |
|---|---:|---:|---:|---|
| `genel_kultur` | 5 | 43 | 48 | cevap dünya bilgisi/ders kitabı terimi; ses/parça süs |
| `esdizim_kilidi` | 43 | 5 | 48 | boşluk kalıp öbeğin tahmin edilen ucunda |
| `konumsal_duzen` | 29 | 11 | 40 | elemeyle/yapısal düzenden çözülüyor |
| `secenek_sozu` | — | 34 | 34 | seçeneğin sözü ait olduğu kökü kendisi adlandırıyor |
| `cerceve_sozu` | — | 15 | 15 | form/not çerçevesinin sözü tek doldurmayı bırakıyor |
| `capraz_sizinti` | — | 10 | 10 | başka soru/paket aynı bilgiyi düz metin yazıyor |
| `kip_imzasi` | 5 | 3 | 8 | ölçülü=doğru / mutlak=çeldirici imzası |
| `belirsiz` | 8 | — | 8 | net mekanizma yok (şans) |
| (mekanizma alanı boş) | 26 | — | 26 | E7 işaretleri; gerekçede dayanak var |
| **Toplam** | **116** | **121** | **237** | |

En sık temalar, her birine bir örnek:

**Tema 1 — Genel kültür / alanın ders kitabı terimi (≈48 + okuma "boş" grubunun bir
kısmı; iki becerinin ortak en büyük teması).** *Örnek (dinleme):* "tohum bankalarının
depolama sıcaklığı −20" — literatür sabiti, senaryoyu dinlemeye gerek yok. *Örnek
(okuma):* PANAS/POMS madde sayıları, JWST/Uranus keşif sayıları — E5'in düzeltmesi
işlemedi çünkü sayının kendisi kamuoyu bilgisi. **Soru yazımıyla kapanmaz; pasaj/konu
seçimi kararı ister.**

**Tema 2 — Seçenek/çerçeve sözü (dinleme 49; okumadaki karşılığı kip imzası+tanım
sızıntısının devamı).** *Örnek:* eşleştirmede "yeri kokusu için seçildi" → yalnız
*çiçek tezgâhı* kökü mümkün; formda "internetten ya da uygulamadan — (9) ile değil" →
*telefon*. Eşleştirmede `option_wording` dayanaklı kalemlerin %89'u senaryosuz bilindi.
**Prompt/yazım düzeyinde düzeltilebilir** (seçeneğin sözünü kökten koparmak).

**Tema 3 — Eşdizim kilidi (okuma 43).** *Örnek:* "an up-to-date ___" → *CV*;
"a ___ of what is coming" → *preview*. E5 sonrası bile okumadaki en büyük tek mekanizma;
`sentence_completion`ın "düzelmedi" çıkmasının ana nedeni. Düzeltmesi mekanik (boşluğu
öbeğin öbür ucuna/parçaya özgü değere taşımak) ama bu tipte **ikinci denemede de
tutmadı** — E7 raporu yeniden üretimi öneriyor.

**Tema 4 — Çapraz sızıntı: pasaj/senaryo paylaşımı (dinleme 10 + okumada E7'nin "3/3
bilinenlerin en az 20'si bu kanaldan" tespiti).** Aynı pasaj/senaryo hem alıştırma hem
tam test paketlerinde kullanılıyor; birinin boşluğu diğerinin **düz metni**. *Örnek:*
alıştırma akış şemasının "SEALING AND FREEZING" adımı, L3 özetinin 34. boşluğunu
kelimesi kelimesine yazıyor; practice MC-11'in cevabını practice TFNG-10'un kökü veriyor.
**1. turda hiç görünmeyen, bu turun en önemli yeni teması: soru kusuru değil, paket
mimarisi kusuru.** Soru elden geçirmeyle kapanmaz; "bir olgu, bir paket" kuralı ya da
alıştırma pasajlarının ayrılması gerekir.

**Tema 5 — Konumsal/yapısal düzen (40).** *Örnek:* başlık eşleştirmede iki başlığın da
aynı paragrafa demirlenmesi (practice MH-15, E7'nin çift-cevap işareti); "sınırlılık
beyanı hep son paragrafta" kalıbı. Büyük ölçüde elden geçirmeyle azaldı (TFNG %53→%12,
MF %69→%31); kalanı MSE'de yoğun.

Tema olmayan ama kayda değer iki bulgu: (a) **NOT GIVEN/FALSE karışıklığı bu turda da
çıkmadı** — E7, E5'in yeniden çapaladığı NOT GIVEN'ların kör çözümde de NOT GIVEN'a
düştüğünü ayrıca doğruladı. (b) **Kip imzası kusuru fiilen kapandı** (180'de ~53 →
bugün 8): E7'nin tespitiyle eski "mutlak→NO / ölçülü→YES" kuralı artık çalışmıyor.

---

## 5. Desen yorumu: sistematik mi, dağınık mı?

**Sistematik — ve 1. turdan daha net, çünkü aynı desenler ikinci beceride bağımsız olarak
tekrar etti:**

1. **Seçenek metni taşıyan tipler sızdırır** (üretim ailesi fark etmeksizin): okumada MC /
   YNNG / MSE (%100'lerden geldiler), dinlemede MC + eşleştirme (%67-88). Dinleme bu
   desenin **bağımsız doğrulamasıdır** — ölçülmeden önce 1. tur "orası da risk altında,
   veri yok" demişti; veri geldi ve tam öngörülen yerde çıktı.
2. **Tamamlama ailesinin sızıntısı boşluğun nereye açıldığında**: alan terimi/eşdizim ucu
   sızdırıyor (okuma özet/cümle, dinleme özet/kısa cevap/akış %52-63), konuşmanın/parçanın
   seçtiği değer sızdırmıyor (form/tablo %12-19, sayı-ad soran 117 dinleme kaleminde
   sızıntı 0). İki beceride aynı ayrım.
3. **Yeni ve yapısal: çapraz-pasaj/senaryo sızıntısı.** 12 pasaj + 24 senaryonun hem
   alıştırma hem test paketlerince paylaşılması, tek tek soruları değil **paket mimarisini**
   sızdırır hâle getirmiş. `cross_question` dayanaklı kalemlerin %91'i 3/3 bilindi —
   ölçümdeki en isabetli dayanak.
4. **Elden geçirme çalışıyor ama tipe göre:** TFNG, YNNG, MF, MH, tablo belirgin düzeldi;
   `sentence_completion` düzelmedi (%43 > %20 taban), `matching_sentence_endings` yerinde
   saydı (9/10). Yani "elden geçir" reçetesi evrensel değil — iki tip için E7 raporu
   açıkça yeniden üretim/tasarım değişikliği öneriyor.

Dağınık-tekil kısım da net: bilgi eşleştirme (%2), başlık eşleştirme (%4), kısa cevap
(%10), dinleme form/tablo (%12-14) fiilen temiz; kişi-görüş eşleştirmeleri ve birbirini
dışlayan çift tasarımı ölçümün karşı kutbunda "sağlam tasarımın çalışan örneği" olarak
kayıtlı.

**Sonuç cümlesi:** Cevap anahtarları iki ölçüm turunda da içerik düzeyinde pratikte %100
doğrulandı (ayakta kalan yalnız 2 çift-cevap vakası); sızıntı cephesinde ise okuma
işaretleri 180'den 116'ya inerken dinlemenin ilk ölçümü 121 yeni işaret ekledi — desen
iki beceride aynı: seçenek sözü + alan terimi + paylaşılan pasaj/senaryo. Asıl karar
yükü artık okumada değil, **dinlemenin seçenekli tipleri ile paket mimarisinde** (aynı
senaryonun/pasajın çok pakette kullanılması).

### Bu rapordan çıkan, karar bekleyen maddeler (karar proje sahibinin)

1. **121 işaretli dinleme sorusu** — seçenekler: işaretlileri at (6 dinleme testinin
   hiçbiri 40/40 kalmaz) / mekanizma bazında elden geçir (`secenek_sozu`+`cerceve_sozu`
   49 kalem yazımla düzelir; `genel_kultur` 43 kalem senaryo/konu değişikliği ister) /
   seçenekli tiplerde yeniden üretim.
2. **116 işaretli okuma sorusu** — E5/E6'nın ikinci turundan sağ çıkanlar; özellikle
   `sentence_completion` (E7: "düzelmedi") ve MSE (9/10) için elden geçirme reçetesi
   tükendi, seçenekler yeniden üretim ya da tipin havuzdan çıkarılması.
3. **Çapraz-pasaj/senaryo kuralı** — "bir olgu, bir paket" taraması ya da alıştırma
   içeriğinin ayrı pasaj/senaryolara taşınması; soru düzeyinde düzeltme bu kanalı kapatmaz.
4. **Gerçek olaya dayalı pasajlar** (A04/JWST, A01/Kandula, Britanya mevzuatı, A05
   verimlilik çalışmaları) — sayısal cevapları haberlerden biliniyor; pasaj/olgu seçimi
   kararı.
5. **İki çift-cevap işareti** (practice MH-15, GT1 özet-40) — varyant ekle / boşluğu
   taşı / başlığı değiştir; tek satırlık işler ama karar ister.
6. **26 okuma işaretinde `flag_mechanism` boş** — elden geçirme yapılacaksa önce
   doldurulmalı (E1 dersinin kalıntısı).
7. **Görsel tipler ölçüsüz:** okuma diyagram etiketleme 10 + dinleme plan/harita 45 —
   metin tabanlı ölçüm kör; ya görselli bir ölçüm tasarlanır ya risk belgelenip kabul edilir.
