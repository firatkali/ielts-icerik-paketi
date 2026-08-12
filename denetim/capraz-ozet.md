# Çapraz Kontrol Özeti — 2. tur (Denetim, 2. çalıştırma)

- **Tarih:** 2026-08-12 (bu turun 2. çalıştırmasının yeniden koşumu; önceki koşum 2026-08-09).
  `git log 5f24bde..HEAD -- content/` boş: içerik 9 Ağustos koşumundan bu yana **hiç değişmedi**.
  Aşağıdaki bütün sayılar bu çalıştırmada dosyalardan yeniden sayıldı; önceki koşumun
  sayılarıyla **birebir uyuştu** (işaretli 237/250, mekanizma dağılımı, model kırılımı).
- **Kaynaklar:** `content/DOGRULAMA/` altındaki bütün JSON raporları ve `RAPOR.md`
  (ilk çapraz doğrulama, 7 oturum), `RAPOR-2.md` (E7 cevap anahtarı yeniden ölçümü),
  `METINSIZ-RAPOR-2.md` + `METINSIZ-yeniden-olcum.md` (okuma parçasız çözüm),
  `SESSIZ-RAPOR.md` + `SESSIZ-TOPLU.json` (dinleme sızıntı ölçümü, 5 çalıştırma),
  `ISARET-GEREKCELERI.md` — ve `content/` altındaki **237 işaretli sorunun**
  `flag_reason` / `flag_mechanism` alanları (383 JSON dosyası bu denetimde tarandı).
- **1. tur karşılaştırması:** `denetim/tur1/capraz-ozet.md` (2026-08-07).
- **Kural gereği bu rapor sadece durum tespiti yapar; hiçbir içerik dosyası değiştirilmemiştir.**

---

## 1. Toplam sayılar: kaç soru doğrulandı, kaçı işaretli, uyuşma ne

### 1a. Cevap anahtarı doğrulaması (kör çapraz çözüm — üretmeyen model çözer)

| Ölçüm | Soru | Uyuşan | İçerik düzeyinde | Kalıcı işaret |
|---|---:|---:|---:|---:|
| İlk tur (CAPRAZ-90, 7 oturum, 2026-08-06) | 743 | 718 (%96,6) | pratikte %100 — 25 uyuşmazlığın 23'ü rakam/yazı-belirteç-boşluk biçimi, 1'i varyant yanlış alarmı, 1'i eksik varyant | 0 |
| E7 yeniden ölçümü (E5/E6 sonrası değişen 188 soru, 2026-08-08) | 188 | 184 (%97,9) | 186 (%98,9) — 2 uyuşmazlık birim/varyant yanlış alarmı | **2** |

Toplam **931 kör çözümden ayakta kalan gerçek uyuşmazlık 2** — ikisi de "yanlış cevap"
değil, "**iki savunulabilir cevap**" vakası: `practice/matching-headings` 15 (v↔ii,
iki başlık da aynı paragrafa demirli) ve `GT1/summary-completion` 40
(prevention↔reductions, kanıt cümlesi iki adayı birden taşıyor). İkisi de bugün
`flagged` duruyor, dosyada doğrulandı. E6'nın yeniden ürettiği 72 sorunun 72'si
anahtarla uyuştu. **Cevap anahtarı cephesi temiz; işaret yükünün kaynağı burası değil.**

### 1b. Sızıntı ölçümleri (işaretlerin asıl kaynağı)

"Sızıntı" = soru, pasaj/senaryo hiç gösterilmeden 3 bağımsız turun üçünde de doğru
biliniyor (K3 = anlam düzeyinde).

| Ölçüm | Kapsam | 3/3 bilinen | Bugün ayakta kalan işaret |
|---|---:|---:|---:|
| Okuma ilk ölçüm (B1, kelime düzeyi) + E10 (anlam düzeyi) | 381 | 180 (%47) + E10 ekleri | E5/E6 elden geçirme/yeniden üretim sonrası bileşim tümüyle yenilendi |
| Okuma E7 yeniden ölçümü (E5/E6 sonrası 189 soru) | 189 | 82 (%43,4 K3) | 81 yeni + 1 eski işaret |
| Dinleme E8 (bu turda yeni; 1. turda hiç ölçülmemişti) | 304 kalem (352'nin ölçülebilenleri; 45 plan/harita görsel gerektirdiği için ölçüm dışı) | 125 K3 (%41,1) | **121** (yalnız dayanağı anlamsal olanlar; şans oranında tutturan 4 `number_guess` bilerek işaretlenmedi) |

**Bugünkü işaretli stok (bu çalıştırmada dosyalardan sayıldı): 237 kalem / 250 numara**
= okuma 116 kalem (122 numara) + dinleme 121 kalem (128 numara). Toplam 1.310 sorunun
%19'u. 1. turda 180 (yalnız okuma) idi; okuma 180 → 116'ya indi (düzelme), dinleme
0 → 121 (bozulma değil — 1. turun "dinleme hiç ölçülmedi" karanlık bölgesi ilk kez
ölçüldü).

---

## 2. Soru tipi bazında işaretlenme oranı — işaretler tipte yoğunlaşıyor mu?

Evet, çok belirgin biçimde. İki beceride de aynı uçlar.

### Okuma (test + alıştırma birlikte, numara bazında)

| Soru tipi | Üretilen | İşaretli | Oran | 1. turda |
|---|---:|---:|---:|---:|
| Cümle sonu eşleştirme | 10 | 9 | **%90** | %100 |
| Akış şeması tamamlama | 6 | 4 | %67 | %67 |
| Özet tamamlama | 43 | 27 | **%63** | %60 |
| Çoktan seçmeli | 39 | 24 | **%62** | %100 |
| Cümle tamamlama | 37 | 15 | %41 | %35 |
| YES / NO / NOT GIVEN | 23 | 9 | %39 | %100 |
| Not/tablo ailesi (not 33 + tablo 12) | 45 | 15 | %33 | ~%29 |
| Özellik eşleştirme | 26 | 8 | %31 | %69 |
| TRUE / FALSE / NOT GIVEN | 57 | 7 | %12 | %53 |
| Kısa cevap | 10 | 1 | %10 | %20 |
| Başlık eşleştirme | 45 | 2 | %4 | %18 |
| Bilgi eşleştirme | 49 | 1 | %2 | %6 |
| Diyagram etiketleme | 10 | — | ölçülemedi (görsel) | — |

Cümle tamamlama ve özetin 1. turdan yüksek görünmesi kötüleşme değil: E7/E10'un anlam
düzeyi (K3) ölçütü, 1. turun kelime düzeyi ölçütünün göremediği sızıntıyı sayıyor.
E7'nin kendi kabul ölçütüne göre bir tip açıkça **düzelmedi**: `sentence_completion`
(%43 > resmî taban %20). `matching_sentence_endings` fiilen yerinde saydı (9/10 hâlâ
parçasız çözülüyor; E7 raporu bu iki tip için elden geçirme yerine yeniden üretim öneriyor).

### Dinleme (E8 ölçümü, kalem bazında; işaret = 3/3 bilinen ∧ dayanak anlamsal)

| Soru tipi | Ölçülen | İşaretli | Oran |
|---|---:|---:|---:|
| Çoktan seçmeli (çok cevaplı) | 8 | 4 | 3/3 bilinme **%87,5** (7/8) |
| Eşleştirme | 43 | 29 | **%67,4** |
| Çoktan seçmeli (tek) | 37 | 24 | %64,9 (3/3 bilinme %67,6) |
| Özet tamamlama | 15 | 9 | %60 |
| Kısa cevap | 28 | 15 | %54 |
| Akış şeması tamamlama | 25 | 13 | %52 |
| Not tamamlama | 40 | 10 | %25 |
| Cümle tamamlama | 39 | 8 | %21 |
| Tablo tamamlama | 29 | 4 | %14 |
| Form tamamlama | 40 | 5 | %13 |
| Plan / harita / diyagram | 45 | — | ölçülmedi (görsel) |

Desen iki beceride aynı: **yazılı seçenek/ifade metni taşıyan tipler üstte** (çoktan
seçmeli, eşleştirme, özet, MSE), **cevabı özel ad / sayı / saat olan tipler altta**
(form, tablo). Alttakilerin düşüklüğü "iyi tasarım" kanıtı değil; o tiplerin cevabı
yapısal olarak tahmin edilemez (SESSIZ raporunun kendi tespiti).

---

## 3. Üreten model bazında kırılım

Kim neyi üretmişti: okumada TFNG/YNNG, çoktan seçmeli ve başlık/özellik/cümle-sonu
eşleştirme paketleri **Fable**, tamamlama ailesi + bilgi eşleştirme + kısa cevap +
diyagram **Opus**; dinlemede çoktan seçmeli + eşleştirme (`FABLE5-43`) **Fable**,
form/tamamlama/plan-harita (`OPUS5-21`) **Opus**. Şerh: `generated_by` alanı **son
üreteni** gösteriyor — E6'nın yeniden ürettiği ~41 okuma sorusu Fable yuvalarında
olsa da artık `opus` imzalı; bu yüzden okuma satırları 1. turla birebir kıyaslanamaz.

| Beceri, model (son üreten) | Soru (numara) | İşaretli | Oran |
|---|---:|---:|---:|
| Dinleme, fable (MC + eşleştirme) | 96 | 64 | **%66,7** |
| Dinleme, opus (form/tamamlama) | 264 | 64 | %24,2 |
| Okuma, opus | 241 | 82 | %34,0 |
| Okuma, fable | 159 | 40 | %25,2 |

(Bu çalıştırmada `generated_by` alanından numara bazında yeniden sayıldı; dört hücre de
önceki koşumla aynı çıktı.)

İki okuma: 1. turda Fable %62 / Opus %32 idi; E5/E6 elden geçirmesi sonrası %25 / %34.
Fable'ın ilk üretimdeki iki sistematik kusuru (kip imzası, konumsal düzen) büyük ölçüde
kapanmış; kalan yük Opus'un tamamlama/özet ailesinde (eşdizim + genel kültür + çapraz-pasaj).

Dinlemede ise 1. turun öngörüsü aynen çıktı: okumada en çok sızdıran prompt ailesinin
dinleme akrabası `FABLE5-43`, ölçülür ölçülmez %66,7 ile en yüksek işaret oranını verdi
ve altı dinleme testinin altısına da işaret düştü (L1 13 · L2 10 · L3 18 · L4 16 ·
L5 16 · L6 10). **Aynı ailenin aynı hastalığı iki beceride bağımsız olarak çıktı —
bu bir üretim deseni, tesadüf değil.**

---

## 4. `flag_reason` temaları

1. turun kusuru ("180 işaretin hepsinde birebir aynı gerekçe cümlesi") kapanmış durumda:
bugünkü 237 gerekçe soruya özgü ve 211'inde `flag_mechanism` alanı dolu (26 okuma
işaretinde alan boş; gerekçe metninde dayanak yazıyor ama mekanizma seçilmemiş —
envanter raporu §5'in tespiti, hâlâ geçerli).

Mekanizma dağılımı (bu çalıştırmada dosyalardan sayıldı, kalem bazında):

| Mekanizma | Okuma | Dinleme | Toplam |
|---|---:|---:|---:|
| `genel_kultur` | 5 | 43 | 48 |
| `esdizim_kilidi` | 43 | 5 | 48 |
| `konumsal_duzen` | 29 | 11 | 40 |
| `secenek_sozu` | — | 34 | 34 |
| (alan boş — E7 işaretleri; gerekçedeki dayanak: genel kültür 11, mantık 11, seçenek sözü 4) | 26 | — | 26 |
| `cerceve_sozu` | — | 15 | 15 |
| `capraz_sizinti` | — | 10 | 10 |
| `kip_imzasi` | 5 | 3 | 8 |
| `belirsiz` | 8 | — | 8 |
| **Toplam** | **116** | **121** | **237** |

En sık temalar, her birine bir örnek:

**Tema 1 — Genel kültür / gerçek olay bilgisi (48 + boş gruptan 11 ≈ 59; iki becerinin
ortak en büyük teması).** *Dinleme:* "anlaşılan sıcaklık yıllardır eksi (2) derece" —
tohum bankalarının standart depolama sıcaklığı, senaryonun seçtiği bir değer değil.
*Okuma:* GT1 not-19 "28 days" (Birleşik Krallık yasal yıllık izin), JWST/Uranus keşif
sayıları, PANAS/POMS ölçek madde sayıları — E5'in düzeltmesi burada işlemedi, çünkü
sayının kendisi kamuoyu bilgisi. **Soru yazımıyla kapanmaz; pasaj/konu (gerçek olay
yerine kurgusal/az bilinen olgu) kararı ister.**

**Tema 2 — Seçenek/çerçeve sözü (dinlemede 34+15=49).** Seçeneğin ya da form/not
çerçevesinin kendi sözü cevabı adlandırıyor. *Örnek:* eşleştirmede "üzerinde çok fazla
metin olması puan götürür" yalnız *slayt* için söylenebilir; notta "bir hanenin payı
(12) ile ölçülürdü, hacimle asla" karşıtlığı hacmin karşısına konabilecek tek ölçüyü
bırakıyor. Dinleme işaretlerinin %40'ı bu kanaldan. **Yazım düzeyinde düzeltilebilir**
(seçeneğin sözünü kökten koparmak, çerçeve karşıtlığını sese taşımak).

**Tema 3 — Eşdizim kilidi (48; 43'ü okumada).** Boşluk, kalıp öbeğin tahmin edilebilir
ucunda. *Örnek:* "an up-to-date ___" → *CV*; "a ___ of what is coming" → *preview*;
dinlemede "artık bir **an** (6) olarak veriliyor" — ünlüyle başlama zorunluluğu tek aday
bırakıyor. E5 sonrası bile okumadaki en büyük tek mekanizma ve `sentence_completion`ın
"düzelmedi" çıkmasının ana nedeni; bu tipte elden geçirme reçetesi **ikinci denemede de
tutmadı**.

**Tema 4 — Konumsal/yapısal düzen — elemeyle çözülme (40).** *Örnek:* practice MH-15'te
iki başlık da aynı paragrafa demirli (E7'nin çift-cevap işaretiyle aynı soru); L3
eşleştirmede kutudaki tek yasak-biçimli cümle köklerdeki tek yasak-biçimli kökle
eşleşiyor. Elden geçirmeyle en çok gerileyen tema (TFNG %53→%12, MF %69→%31); kalanı
MSE'de yoğun.

**Tema 5 — Çapraz sızıntı: pasaj/senaryo paylaşımı (dinleme 10 + E7'nin okuma tespiti:
3/3 bilinenlerin en az 20'si bu kanaldan).** Aynı pasaj/senaryo hem alıştırma hem tam
test paketlerinde kullanılıyor ve birinin soru kökü diğerinin cevabını **düz metin**
yazıyor. *Örnek:* practice MC-11'in cevabını practice TFNG-10'un kökü veriyor ("The
ground survey of 12 December…"); alıştırma akış şemasının boşluğunu L5 özet paketi
kelimesi kelimesine yazıyor. **1. turda hiç görünmeyen, bu turun en önemli yeni teması:
soru kusuru değil paket mimarisi kusuru** — tek tek soru düzeltmek bu kanalı kapatmaz,
"bir olgu, bir paket" kuralı ya da alıştırma içeriğinin ayrı pasaj/senaryolara taşınması
gerekir.

Kayda değer iki "olmayan" tema: (a) **NOT GIVEN/FALSE ayrım karışıklığı bu turda da
çıkmadı** — E7, E5'in yeniden çapaladığı NOT GIVEN'ların kör çözümde de NOT GIVEN'a
düştüğünü doğruladı. (b) **Kip imzası fiilen kapandı** (1. turda ~53 işaretin gerekçesi,
bugün 8): eski "mutlak→NO / ölçülü→YES" kestirmesi artık çalışmıyor.

---

## 5. Desen yorumu: sistematik mi, dağınık tekil mi?

**Sistematik — ve 1. turdan daha net, çünkü aynı desenler ikinci beceride bağımsız
olarak tekrar etti:**

1. **Seçenek metni taşıyan tipler sızdırır**, üretim ailesi fark etmeksizin: okumada
   MC/YNNG/MSE (1. turda %100'lerdeydi), dinlemede MC + eşleştirme (%65-88). Dinleme
   ölçümü bu desenin bağımsız doğrulaması: 1. tur "orası da risk altında, veri yok"
   demişti; veri geldi ve tam öngörülen yerde çıktı. **Risk altındaki tipler:** dinleme
   MC (tek+çoklu) ve eşleştirme, okuma MSE ve çoktan seçmeli.
2. **Tamamlama ailesinde sızıntı, boşluğun nereye açıldığına bağlı:** alan terimi /
   eşdizim ucu / genel kültür değeri sızdırıyor (okuma özet %63, dinleme özet %60,
   kısa cevap %54); konuşmanın/pasajın kendi seçtiği ad-sayı-saat sızdırmıyor (form %13,
   tablo %14-19). İki beceride aynı ayrım — bu, üretim şartnamesine çevrilebilir somut
   bir kural ("boşluğu kalıbın ucuna değil, kaynağın seçtiği değere aç").
3. **Yapısal ve yeni: çapraz-pasaj/senaryo sızıntısı.** 12 pasaj + 24 senaryonun
   alıştırma ve test paketlerince paylaşılması, sızıntıyı tek soru düzeyinden **paket
   mimarisi** düzeyine taşımış. Soru elden geçirme bu kanalı yapısal olarak kapatamaz.
4. **Elden geçirme reçetesi tipe göre çalışıyor:** TFNG, YNNG, MF, MH, tablo belirgin
   düzeldi; `sentence_completion` düzelmedi (%43 > %20 taban), `matching_sentence_endings`
   yerinde saydı (9/10). İki tip için E7 raporunun kendisi yeniden üretim/tasarım
   değişikliği öneriyor.

Dağınık-tekil kutup da net: bilgi eşleştirme (%2), başlık eşleştirme (%4), kısa cevap
okuma (%10), dinleme form/tablo (%13-14) fiilen temiz; cevap anahtarı cephesinde ayakta
kalan yalnız 2 çift-cevap vakası var. Yani sorun "her yerde biraz" değil — **belirli
tiplerde ve belirli mimari kararlarda yoğunlaşmış, tekrarlayan bir üretim deseni.**

**Sonuç cümlesi:** Cevap anahtarları 931 kör çözümde içerik düzeyinde pratikte %100
doğrulandı; işaret yükü tümüyle sızıntı cephesinde — okuma 180'den 116'ya indi, dinlemenin
ilk ölçümü 121 işaret ekledi ve desen iki beceride aynı: seçenek/çerçeve sözü + genel
kültür/eşdizim + paylaşılan pasaj-senaryo. Karar yükü artık okumada değil, **dinlemenin
seçenekli tipleri ile paket mimarisinde.**

### Karar bekleyen maddeler (karar proje sahibinin; burada yalnız seçenekler listelenir)

1. **121 işaretli dinleme sorusu** — seçenekler: işaretlileri at (hiçbir dinleme testi
   40/40 kalmaz) / mekanizma bazında elden geçir (`secenek_sozu`+`cerceve_sozu` 49 kalem
   yazımla düzelebilir; `genel_kultur` 43 kalem senaryo/konu değişikliği ister) /
   seçenekli tiplerde yeniden üretim.
2. **116 işaretli okuma sorusu** — özellikle `sentence_completion` (E7: "düzelmedi") ve
   MSE (9/10) için elden geçirme reçetesi tükendi; seçenekler yeniden üretim ya da tipin
   havuzdan çıkarılması.
3. **Çapraz-pasaj/senaryo kuralı** — "bir olgu, bir paket" taraması ya da alıştırma
   içeriğinin ayrı pasaj/senaryolara ayrılması.
4. **Gerçek olaya dayalı pasajlar** (A04/JWST, A01/Kandula, Britanya mevzuatı,
   PANAS/POMS) — sayısal cevapları haberlerden/literatürden biliniyor; pasaj/olgu seçimi
   kararı.
5. **İki çift-cevap işareti** (practice MH-15, GT1 özet-40) — varyant ekle / boşluğu
   taşı / başlığı değiştir; tek satırlık işler ama karar ister.
6. **26 okuma işaretinde `flag_mechanism` boş** — elden geçirme yapılacaksa önce
   doldurulmalı.
7. **Görsel tipler ölçüsüz** (okuma diyagram 10 + dinleme plan/harita 45) — metin
   tabanlı sızıntı ölçümü bu tiplerde kör; ya görselli ölçüm tasarlanır ya risk
   belgelenip kabul edilir.
