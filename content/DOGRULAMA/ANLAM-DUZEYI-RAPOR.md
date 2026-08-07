# Anlam düzeyi ölçüt — parçasız cevabın *anlamca* tutup tutmadığı

Bu rapor yeni bir ölçüm turu koşturmuyor. Mevcut `kalibrasyon/metinsiz/<paket>-tur1/2/3.json`
dökümlerini — modelin parçayı görmeden verdiği cevapları — yeniden değerlendiriyor. Eski
`OPUS5-B1` ölçümü "cevap 3/3 turda **kelimesi kelimesine** tuttu mu?" diye soruyordu; bu ölçüm
"cevap 3/3 turda **anlamca** tuttu mu?" diye soruyor.

## Karar kuralı (üç çalıştırmada aynı)

Modelin cevabı, gerçek cevapla **aynı şeye işaret ediyorsa** anlamca doğru sayıldı:

- eş anlamlı kelime (`mountaineers` ↔ `climbers`, `salary` ↔ `pay`)
- aynı kelimenin farklı çekimi/biçimi (`probationary period` ↔ `probation period`)
- niteleyici düşmüş ama ana ad duruyor, gönderge aynı (`separate laboratories` → `laboratories`)
- aynı kavramın başka sözcüğü (`ongoing research` → `preliminary`)

Anlamca **yanlış** sayılanlar: gönderge daralıyor ya da değişiyor (`weeks or months` → `weeks`,
`plant DNA` → `ancient DNA`), sayı/isim tutmuyor (`8,400 years` → `8,000 years`), yanlış kavram.
🔴 Üç turun **üçünde de** anlamca doğru olması şart — tek turda tutturmak hâlâ şans olabilir.

---

## 1. çalıştırma — cümle tamamlama + kısa cevap · 2026-08-08

| Paket | Soru | Kelime düzeyi (eski) | Anlam düzeyi (yeni) | Fark | Yeni işaretlenen |
|---|---|---|---|---|---|
| sentence-completion | 37 | 13 (%35.1) | 27 (%73.0) | +37.9 puan | 14 |
| short-answer | 10 | 2 (%20.0) | 3 (%30.0) | +10.0 puan | 1 |
| **toplam** | **47** | **15 (%31.9)** | **30 (%63.8)** | **+31.9 puan** | **15** |

Kendi sayımım **15 yeni soru.** Plandaki "cümle tamamlamada ~19" rakamına ulaşmadım: cümle
tamamlamada 14 yeni soru buldum, anlam düzeyi oranı %73.0 çıktı. Denetim raporunun andığı %81
ile arasındaki fark, sınırda kalan sekiz soruyu (aşağıda) saymamış olmamdan geliyor — gönderge
daralan ya da sayısı tutmayan cevabı "biliniyor" saymadım.

### Yeni işaretlenen sorular

`sentence-completion` (14): practice 2, 3, 4, 6, 7, 12 · AC1 19, 20 · AC2 20 · AC3 22 ·
AC4 22 · GT1 27 · GT2 25, 26
`short-answer` (1): practice 6

### Somut örnekler — gerçek cevap → modelin anlamca doğru ama kelimece farklı cevabı

| Soru | Gerçek cevap | Modelin üç turdaki cevabı | Neden anlamca doğru |
|---|---|---|---|
| AC3-22 | `mountaineers` | climbers · climbers · climbers | Tam eş anlamlı; "dağcılar" göndergesi birebir aynı, yalnız sözcük farklı. |
| AC1-19 | `transparent divider` | transparent barrier ×3 | Tankı bölen saydam engel; `divider`/`barrier` aynı nesneyi adlandırıyor. |
| GT2-25 | `probationary period` | probation period ×3 | Aynı kelimenin sıfat/ad çekimi; kavram deneme süresi, birebir aynı. |
| practice-12 | `ongoing research` | preliminary ×3 | "Hakem değerlendirmesinden geçmemiş, bitmemiş bulgu" kavramı; farklı sözcük, aynı iddia. |
| practice-3 | `anatomy` | anatomy · **morphology** · anatomy | Kelime düzeyinde 2/3 tuttuğu için "bilinmiyor" sayılmıştı; `morphology` biyolojide `anatomy`nin eş anlamlısı, anlamca 3/3. |

### Anlamca da saymadığım sınır durumlar (şeffaflık için)

| Soru | Gerçek cevap | Modelin cevabı | Neden sayılmadı |
|---|---|---|---|
| practice-sc-5 | `first contact` | contact · **approach** · contact | Parça mesafe korumayı temastan ayırıyor; `approach` ≠ `contact`. |
| practice-sc-9 | `hypothetical future` | simulation · prediction · prediction | Modelleme kavramı var, "gelecek" ögesi yok. |
| practice-sc-14 | `transitional stage` | beginning · stage · start | Ayırt edici öge (`transitional`) iki turda düşmüş. |
| AC2-sc-19 | `plant DNA` | ancient DNA ×3 | Sorulan ayrıntı (`plant`) tutmuyor; `ancient` başka bir şey söylüyor. |
| GT2-sc-27 | `four weeks` | four weeks · **one month** · four weeks | Birim çevrimi sayı değişikliği sayıldı; sayıda kesinlik kuralı gevşetilmedi. |
| practice-sa-3 | `weeks or months` | weeks ×3 | Gönderge daralıyor: `weeks` aralığın yalnız alt ucunu veriyor. |
| practice-sa-5 | `8,400 years` | 8,000 years ×3 | Yanlış sayı. |
| practice-sa-9 | `scanning electron microscopy` | electron microscopy · **transmission** electron microscopy · electron microscopy | 2. tur başka bir tekniği (TEM) adlandırıyor. |

### İşaretlemenin şekli

Anlamca bilinen her soruya orijinal dosyasında şu alanlar yazıldı:

```json
"blind_solvable": true,
"blind_solvable_kelime_duzeyi": false,
"blind_basis": "logic",
"status": "flagged",
"flag_reason": "Parça gösterilmeden anlamca 3/3 turda doğru bilindi: ...",
"flag_mechanism": "esdizim_kilidi"
```

Eski kelime-düzeyi bulgusu silinmedi: `blind_solvable: false` değeri
`blind_solvable_kelime_duzeyi` alanına taşındı, çünkü iki ölçüm farklı şeyi ölçüyor — biri
kavrayışı, öteki kelime tutturmayı. Hiçbir soru silinmedi; 47 sorunun 47'si yerinde
(`sentence-completion` 37, `short-answer` 10), tam testlerde soru sayısı değişmedi.

Uygulayan betik: `tools/_e10_anlam_isaretle.py`.

---

## 2. çalıştırma — özet ailesi · 2026-08-08

`summary-completion`, iki alt tipiyle birlikte. Alt tipleri ayrı satırda veriyorum, çünkü
bulgunun kendisi bu ayrımda saklı.

| Alt tip | Set | Soru | Kelime düzeyi (eski) | Anlam düzeyi (yeni) | Fark | Yeni işaretlenen |
|---|---|---|---|---|---|---|
| parçadan kelime | practice, AC1, AC3, GT1 | 29 | 12 (%41.4) | 26 (%89.7) | +48.3 puan | 14 |
| kelime bankalı | AC2, AC4, GT2 | 14 | 14 (%100) | 14 (%100) | 0 puan | 0 |
| **toplam** | | **43** | **26 (%60.5)** | **40 (%93.0)** | **+32.6 puan** | **14** |

Kendi sayımım **14 yeni soru.** Plandaki "özet ailesinde ~15" rakamına bir soru kaldım.

🔴 **Asıl bulgu, iki alt tipin farkı.** Kelime bankalı özette anlam düzeyi ölçümü tek bir yeni
soru bile bulmuyor — bulamaz da: cevap kapalı bir listeden seçilen harf olduğu için yüzey
sapması imkânsız, kelime düzeyi ölçümü orada zaten anlam düzeyi ölçümüdür (ve o 14 sorunun
14'ünü de "biliniyor" saymıştı). Bütün fark parçadan-kelime alt tipinden geliyor: %41.4 → %89.7.
Yani `OPUS5-B1`'in özet ailesinde kaçırdığı sızıntının tamamı "parçadan kelime kopyala"
kuralının olduğu yerde. Denetim raporunun andığı %93'lük parçadan-kelime rakamına %89.7 ile
yaklaştım; aradaki fark aşağıdaki üç soruyu saymamamdan geliyor.

### Yeni işaretlenen sorular

`summary-completion` (14): practice 3, 4, 6, 8, 11, 12, 14 · AC1 37, 40 · AC3 36, 37, 40 ·
GT1 37, 38

### Somut örnekler — gerçek cevap → modelin anlamca doğru ama kelimece farklı cevabı

| Soru | Gerçek cevap | Modelin üç turdaki cevabı | Neden anlamca doğru |
|---|---|---|---|
| AC3-36 | `decomposition` | decay ×3 | Tam eş anlamlı; "ısıtılan dokuda başlamayan çürüme" göndergesi birebir aynı. |
| GT1-38 | `refrigerator` | fridge ×3 | Aynı nesnenin günlük dildeki adı; buzdolabının arkasında unutulan süt ürünleri. |
| practice-4 | `software engineers` | developers · programmers · developers | Kod çıktısı ölçülen aynı meslek grubu; üç sözcük de aynı katılımcıları adlandırıyor. |
| practice-6 | `crossover` | crossover · **within-subject** · crossover | Kelime düzeyinde 2/3 tuttuğu için "bilinmiyor" sayılmıştı; within-subject, "her gönüllü kendi karşılaştırması" düzeninin öteki adı — anlamca 3/3. |
| AC1-40 | `warning system` | warning ×3 | "erken uyarı" ile "erken uyarı sistemi" aynı göndergeyi kuruyor; adanın rolü değişmiyor. |

### Anlamca da saymadığım sorular (şeffaflık için)

| Soru | Gerçek cevap | Modelin cevabı | Neden sayılmadı |
|---|---|---|---|
| practice-sum-15 | `elderly` | unemployed ×3 | Yanlış kavram: yaşlılık ile işsizlik başka gruplar. |
| AC3-sum-39 | `seven` | nine · several · nine | Yanlış sayı; ayrıca 2. tur sayı vermiyor. |
| GT1-sum-39 | `convenience` | **supermarkets** · convenience · convenience | 1. tur bir yeri adlandırıyor, cevap ise bir eğilim; 3/3 şartı düşüyor. |

### Bu çalıştırmada atlanan paket

Dinleme tarafındaki `summary-completion` setleri (L3 6, L5 5, L6 4 = 15 soru) değerlendirmeye
girmedi: `kalibrasyon/metinsiz/summary-completion-tur1/2/3.json` dökümlerinin üçü de yalnız
okuma sorularını içeriyor (43 kimliğin 43'ü okuma). Yöntemin 1. maddesi gereği üç tur dökümü
olmayan paket bu turda atlanır; dinleme sızıntı ölçümü ayrı bir adımın işi.

### İşaretlemenin şekli

1. çalıştırmadaki şemanın aynısı; eski kelime-düzeyi bulgusu yine silinmedi,
`blind_solvable_kelime_duzeyi` alanına taşındı. Hiçbir soru silinmedi: 43 soru girdi, 43 soru
çıktı (practice 15, AC1 5, AC2 5, AC3 5, AC4 5, GT1 4, GT2 4), tam testlerde soru sayısı
değişmedi. Uygulayan betik: `tools/_e10_anlam_isaretle2.py`.

---

## 3. çalıştırma — not/tablo/akış tamamlama · 2026-08-08

`note-completion`, `table-completion`, `flow-chart-completion` (okuma tarafı).

| Paket | Soru | Kelime düzeyi (eski) | Anlam düzeyi (yeni) | Fark | Yeni işaretlenen |
|---|---|---|---|---|---|
| note-completion | 33 | 9 (%27.3) | 18 (%54.5) | +27.3 puan | 9 |
| table-completion | 12 | 4 (%33.3) | 6 (%50.0) | +16.7 puan | 2 |
| flow-chart-completion | 6 | 4 (%66.7) | 5 (%83.3) | +16.7 puan | 1 |
| **toplam** | **51** | **17 (%33.3)** | **29 (%56.9)** | **+23.5 puan** | **12** |

Kendi sayımım **12 yeni soru.** Bu üç paket için planda yön verici bir rakam yoktu; bulduğum
oran, ilk iki çalıştırmanın parçadan-kelime kanadıyla aynı yönde ama daha ılımlı: not
tamamlamada boşlukların çoğu sayı, tarih ve özel ad istiyor (`90 kilometres`, `12 December`,
`Eurasian magpie`), orada yanlış sayı yanlış sayıdır — anlam düzeyine geçmek onları
kurtarmıyor. Sızıntı, boşluğun soyut bir kavram istediği yerde toplanıyor.

### Yeni işaretlenen sorular

`note-completion` (9): practice 3, 4, 6, 11, 12 · AC4 1 · GT1 17, 18, 20
`table-completion` (2): AC3 3 · GT2 15
`flow-chart-completion` (1): AC2 1

### Somut örnekler — gerçek cevap → modelin anlamca doğru ama kelimece farklı cevabı

| Soru | Gerçek cevap | Modelin üç turdaki cevabı | Neden anlamca doğru |
|---|---|---|---|
| practice-nc-12 | `skeletal remains` | bones ×3 | Tam eş anlamlı; "tek başına kemiklerin veremediği hücre düzeyi ayrıntı" iddiası birebir aynı. |
| AC2-fc-1 | `forty minutes` | 40 minutes ×3 | Aynı sayının rakamla yazılışı. Kelime düzeyi ölçümü bunu "bilinmiyor" saymıştı, oysa `40 minutes` cevap anahtarının kendi `accepted_variants` listesinde zaten var — ölçüm burada anahtardan bile katıydı. |
| AC4-nc-1 | `reconfigure` | rearrange · **reconfigure** · rearrange | Kelime düzeyinde 1/3 tuttuğu için "bilinmiyor" sayılmıştı; rearrange, "ihtiyaç değişince kolay yeniden düzenlenir" iddiasının aynısı. |
| GT1-nc-17 | `card reader` | time clock · **card reader** · clocking-in machine | Üç ad da personel girişindeki aynı cihazı gösteriyor; gönderge tek. |
| practice-nc-4 | `Eurasian magpie` | magpie ×3 | Niteleyici düşmüş, ana ad duruyor: ayna testini geçen kuş aynı. |

### Anlamca da saymadığım sorular (şeffaflık için)

| Soru | Gerçek cevap | Modelin cevabı | Neden sayılmadı |
|---|---|---|---|
| practice-nc-5 | `Monodontidae` | beluga · belugas · beluga | Boşluk "başka bir dişli balina **soyu**" istiyor; model türü adlandırıyor, soyu değil. |
| practice-nc-13 | `polysomnography` | EEG ×3 | EEG polisomnografinin tek kanalı; adlandırılan yöntem başka. 1. çalıştırmadaki SEM/TEM kararıyla aynı çizgi. |
| AC1-nc-2 | `bamboo` | bamboo · **wood** · bamboo | Sorulan ayrıntı çubuğun malzemesi; `wood` bambuyu adlandırmıyor. |
| AC1-nc-6 | `fingertip` | hand ×3 | Gönderge genişliyor: el, parmak ucu değil. |
| GT2-tc-19 | `travel allowance` | relocation allowance ×3 | Yol parası ile taşınma parası yerleşik olarak ayrı iki ödeme; üstelik "taşınan herkes" ögesini soru kökü zaten veriyor. |
| GT2-tc-18 | `ten working days` | two weeks · **seven days** · two weeks | 2. tur başka bir süre veriyor, 3/3 şartı düşüyor. |
| AC3-tc-2 | `barrel rolls` | head movements · head bobs · head turns | Baş hareketi ile gövde taklası ayrı davranışlar. |

### Bu çalıştırmada atlanan paketler

Üç paketin de **dinleme** setleri değerlendirmeye girmedi: `note-completion` 42 soru
(practice 15, L1 6, L2 5, L4 10, L6 6), `table-completion` 30 soru (practice 15, L2 10, L5 5),
`flow-chart-completion` 25 soru (practice 15, L2 5, L4 5) — toplam **97 soru.** Sebep 2.
çalıştırmadakiyle aynı: üç tur dökümünün üçü de yalnız okuma sorularını içeriyor (33/12/6
kimliğin tamamı okuma), bu sorular için parçasız cevap hiç üretilmemiş. Yöntemin 1. maddesi
gereği atlandı; dinleme sızıntısı ayrı bir adımın işi.

🔴 Dikkat: `practice-note-completion` set kimliği hem dinlemede hem okumada kullanılıyor, yani
döküm kimlikleri iki beceride çakışıyor. İşaretleme betiği bu yüzden `skill == "reading"`
süzgeciyle çalışıyor; süzgeç olmasa dinleme soruları okuma dökümüyle karşılaştırılırdı.

### İşaretlemenin şekli

1. ve 2. çalıştırmadaki şemanın aynısı, alan adı da aynı: eski kelime-düzeyi bulgusu silinmedi,
`blind_solvable_kelime_duzeyi` alanına taşındı. Hiçbir soru silinmedi: 51 okuma sorusu girdi,
51 çıktı (note 33, table 12, flow-chart 6); 12 tam testin hepsi 40/40 kaldı, şema hatası 0.
Uygulayan betikler: `tools/_e10_karsilastir3.py` (karşılaştırma tablosu),
`tools/_e10_anlam_isaretle3.py` (işaretleme).

---

## Toplu rapor — üç çalıştırmanın birlikte söylediği

| Çalıştırma | Paketler | Soru | Kelime düzeyi | Anlam düzeyi | Fark | Yeni |
|---|---|---|---|---|---|---|
| 1 | sentence-completion, short-answer | 47 | 15 (%31.9) | 30 (%63.8) | +31.9 puan | 15 |
| 2 | summary-completion | 43 | 26 (%60.5) | 40 (%93.0) | +32.6 puan | 14 |
| 3 | note / table / flow-chart-completion | 51 | 17 (%33.3) | 29 (%56.9) | +23.5 puan | 12 |
| **toplam** | **tamamlama ailesi** | **141** | **58 (%41.1)** | **99 (%70.2)** | **+29.1 puan** | **41** |

**Toplam 41 yeni soru işaretlendi.** Plandaki "cümle tamamlamada ~19, özet ailesinde ~15"
rakamları yön vericiydi; kendi sayımım o iki pakette 15 ve 14, üçüncü grupta 12.

Üç çalıştırmanın ortak bulgusu tek cümleyle: **`OPUS5-B1`'in tamamlama ailesinde ölçtüğü şey
kavrayış değil, kelime tutturmaydı.** Ailenin tamamına bakıldığında parçasız da bilinen soru
oranı %41.1 değil %70.2 — yani B1 sızıntının yaklaşık **beşte ikisini** görmüyordu.

Farkın nerede olduğu da netleşti:

- **Cevap kapalı bir listeden seçiliyorsa fark sıfır.** Kelime bankalı özet (14 soru) kelime
  düzeyinde de anlam düzeyinde de 14/14. Yüzey sapması imkânsız olduğu için orada kelime
  düzeyi ölçümü zaten anlam düzeyi ölçümüdür.
- **Cevap "parçadan kelime kopyala" ise fark en büyük.** Parçadan-kelime özet %41.4 → %89.7
  (+48.3 puan), cümle tamamlama %35.1 → %73.0 (+37.9 puan). Sızıntının tamamı burada.
- **Boşluk sayı/tarih/özel ad istiyorsa fark küçük.** Not ve tablo tamamlamada boşlukların
  önemli kısmı `90 kilometres`, `12 December`, `fourteen`, `twenty-three seconds` gibi kesin
  değerler istiyor; yanlış sayı anlam düzeyinde de yanlıştır, o yüzden bu iki pakette artış
  +27.3 ve +16.7 puanda kalıyor.

Pratik sonucu: bir tamamlama sorusunun sızıntıya dayanıklılığı, cevabın **biçimine** bağlı.
Kapalı liste ya da kesin değer isteyen boşluk dayanıklı; parçadan serbest kelime isteyen boşluk
değil — orada soru çoğunlukla kavrayışı değil, doğru eşdizimi bulmayı ölçüyor. İşaretlenen 41
sorunun hepsi `flag_mechanism: "esdizim_kilidi"` ile duruyor, hiçbiri silinmedi.

Kapsam sınırı: bu üç çalıştırma yalnız **okuma** sorularını değerlendirdi (141 soru). Tamamlama
ailesinin dinleme kanadı (özet 15 + not/tablo/akış 97 = 112 soru) hiç değerlendirilemedi, çünkü
`kalibrasyon/metinsiz/` dökümlerinde parçasız cevapları yok. Dinleme sızıntısı açık bir soru
olarak duruyor.

Bu ölçüm anlam düzeyinde bilinen soruyu bulur, kelime tutturma başarısını değil.
