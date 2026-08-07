# Puanlama kalibrasyonu — SONUÇ (2026-08-07)

Bu dosya `prompts/OPUS5-A4-puanlama-duzeltmesi.md`'nin **3. (son rapor) çalıştırmasıdır**.
Bu çalıştırmada **hiçbir düzeltme yapılmadı**: `degerlendirme/` altındaki hiçbir dosyaya
dokunulmadı. Yalnızca üç ölçüm turu yan yana konuldu.

Bu aşamada saklı küme yok (son raporda hepsi görünür). Aşağıdaki her sayı
`tools/_a4_sonuc.py` tarafından hesaplandı; elle ortalama alınmadı.

---

## 🔴 Önce dürüst not: tur 3 tamamlanmadı

Tur 3, dört çalıştırmalık bir işti; **üçü bitti**. Son grup — `GT-T2` (5 örnek × 3 tekrar =
15 puanlama) — hiç puanlanmadı. Sebebi teknik: 105 numaralı adım (`gunluk/20260807-053340-adim105.log`)
oturum limitine takılıp çıkış kodu 1 ile düştü, iş listesi bir sonraki adıma geçti.

Yani **tur 3 = 23 örnekten 18'i (54/69 puanlama)**. Bu oturum eksiği kapatamaz: ölçüm bilerek
Sonnet ile yapılır (`prompts/SONNET5-A3-puanlama-olcumu.md` başlığı), bu oturum Opus'tur; buradan
puanlamak ürünün davranışını değil başka bir modelin davranışını ölçmüş olurdu.

Eksik 5 örneğin önceki turlardaki sapması:

| Örnek | Küme | Gerçek | tur 1 | tur 2 |
|---|---|---|---|---|
| GT-T2-2A-A | S3 | 5,0 | −0,5 | 0,0 |
| GT-T2-2A-B | S2 | 8,0 | **−2,0** | **−2,0** |
| GT-T2-2B-A | S3 | 4,0 | +0,5 | +0,5 |
| GT-T2-2B-B | S1 | 6,0 | — | −1,0 |
| GT-T2-2B-C | S2 | 8,5 | — | **−2,0** |

Bu grup, önceki iki turda **ortalamanın üstünde sapan** gruptu (tur 2'de ortalama mutlak fark
1,10; ölçülen 18 örnekte 0,86). Dolayısıyla **tur 3'ün başlık sayısı iyimser taraflıdır.**
Bu 5 örnek tur 2'deki gibi davransaydı tur 3'ün ortalama mutlak farkı 0,694 değil **0,78**
olurdu (üst sınır tahmini, ölçüm değil). Gerçek değer bu ikisinin arasında bir yerdedir ve
**bilinmiyor**.

Bu yüzden aşağıdaki tabloların hepsinde, tur karşılaştırması **üç turda da puanlanan aynı 18
örnek** üzerinden verilmiştir (eşleşik). Her turun kendi kümesi üzerinden okunan sayılar ayrıca
gösterildi ki fark görünsün.

---

## 1. Üç turun ölçüleri yan yana

**Eşleşik (üç turda da puanlanan aynı 18 örnek) — karşılaştırılabilir olan budur:**

| Ölçü | tur 1 | tur 2 | tur 3 |
|---|---|---|---|
| Ortalama mutlak fark | 0,944 | 0,861 | **0,694** |
| Eğilim (+ cömert / − cimri) | −0,667 | −0,639 | **−0,139** |
| En büyük tek sapma | 2,00 | 2,00 | **1,50** |
| Tutarsızlık (aynı cevaptaki yayılım) | 0,33 | — ¹ | **0,19** |
| ≥ 1,5 band sapan örnek | 7 / 18 | 7 / 18 | **1 / 18** |
| Verilen puanların aralığı | 4,5 – 7,0 | 3,5 – 7,0 | 4,5 – 7,5 |

¹ Tur 2'de her örnek **1 kez** puanlandı; yayılım tanım gereği 0,00 çıkar. `RAPOR-tur2.md`'deki
"✅ geçti" o satırda **anlamsızdır** — tutarlılık tur 2'de sınanmadı.

**Her turun kendi örnek kümesi üzerinden (RAPOR-tur\*.md ile birebir aynı):**

| Ölçü | tur 1 (n=21) | tur 2 (n=23) | tur 3 (n=18) |
|---|---|---|---|
| Ortalama mutlak fark | 0,952 | 0,913 | 0,694 |
| Eğilim | −0,667 | −0,696 | −0,139 |
| En büyük tek sapma | 2,00 | 2,00 | 1,50 |
| Yayılım | 0,33 | 0,00 ¹ | 0,19 |

**Ne oldu:** İlerlemenin neredeyse tamamı **2. düzeltmede** geldi. 1. düzeltme (tur 1 → tur 2)
eğilimi hiç oynatmadı (−0,67 → −0,64); yalnız dilbilgisi ölçütünü ve orta bandı düzeltti.
2. düzeltme (tur 2 → tur 3) eğilimi −0,64'ten −0,14'e indirdi. Aradaki fark, 2. düzeltmenin
öğüt değil **yordam** değiştirmesi: ölçüt tablosunun 9'dan aşağı okunması (değişiklik 11) ve
"7/8 satırı zaten hata içerir" kuralı (değişiklik 12).

**Band aralığı × ölçüt (eşleşik 18 örnek, ölçüt bandı − gerçek genel band):**

| Gerçek band | n | tur | görev | tutarlılık | kelime | dilbilgisi | **genel** |
|---|---|---|---|---|---|---|---|
| ≥ 7 | 7 | 1 | −1,64 | −1,93 | −1,21 | −1,64 | **−1,50** |
| | | 2 | −1,29 | −1,93 | −1,07 | −1,29 | **−1,36** |
| | | 3 | −1,07 | −0,93 | −0,64 | −0,93 | **−0,79** |
| 5 – 6,5 | 9 | 1 | −0,22 | −0,22 | −0,44 | −0,89 | **−0,39** |
| | | 2 | −0,17 | −0,28 | −0,44 | −0,61 | **−0,33** |
| | | 3 | +0,00 | +0,33 | +0,17 | −0,56 | **+0,06** |
| ≤ 4,5 | 2 | 1 | +1,50 | +1,00 | +0,50 | +0,50 | **+1,00** |
| | | 2 | +1,00 | +0,00 | +0,00 | +0,00 | **+0,50** |
| | | 3 | +1,50 | +1,50 | +0,50 | +0,50 | **+1,25** |

🔴 **Alt band geri gitti.** ≤4,5 aralığı tur 2'de +0,50 idi, tur 3'te **+1,25**. 2. düzeltmenin
18 numaralı değişikliği (5-4 ayrımı) tam bu şişmeyi durdurmak içindi ve **tutmadı**: aynı
düzeltmedeki altı yukarı yönlü değişiklik (11–17) alt bandı da yukarı itti. Bu, raporun en
kötü bulgusudur ve düzeltmenin **yan hasarıdır**, tur 3'ün eksik olmasıyla ilgisi yoktur.
Somut hâli: gerçek bandı **3,0** olan cevaba ürün **4,5** veriyor (tur 2'de 3,5 vermişti).

Ne kadarına dayandığı da yazılmalı: bu aralıkta tur 3'te **yalnız 2 örnek** var (gerçek band
3,0 ve 4,0). Yön nettir, büyüklüğü değildir.

---

## 2. Saklı küme ile açık küme karşılaştırması

Kümelerin düzeltme oturumlarında ne olduğu:

| Küme | 1. düzeltme | 2. düzeltme |
|---|---|---|
| S1 | görünür | **SAKLI** |
| S2 | görünür | görünür |
| S3 | **SAKLI** | görünür |

**Sınav 1 — 1. düzeltmenin saklı kümesi (S3), tur 2'de:** S3 **0,857** · o turda görünür olan
S2 **1,000**. Saklı küme, görünür kümeden **daha kötü değil**.

**Sınav 2 — 2. düzeltmenin saklı kümesi (S1), tur 3'te:**

| | n | Ortalama mutlak fark | Eğilim |
|---|---|---|---|
| S1 (son ayarın **görmediği** küme) | 7 | **0,714** | +0,000 |
| S2 + S3 (son ayarın gördüğü kümeler) | 11 | **0,682** | −0,227 |
| **Fark** | | **0,032 band** | |

**Sonuç: ezber işareti yok.** İki küme arasındaki fark 0,032 band — ölçüm çözünürlüğünün
(0,5 band) çok altında. Aynı kontrol her iki düzeltme için de ayrı ayrı yapıldı ve ikisi de
temiz çıktı. Ölçeğin **iki uçtaki hatası** (üst bandda cimrilik, alt bandda şişme) saklı
kümede de görünür kümede de **aynen duruyor** — ezberde beklenen şey bunun tersidir.

Küme bazında eğilimlerdeki fark (S3 −0,600, S1 +0,000, S2 +0,083) **bileşim etkisidir, ezber
değil**: tur 3'te puanlanamayan 5 örnekten ikisi S3'ün tek düşük bandlı örnekleriydi
(GT-T2-2B-A 4,0 · GT-T2-2A-A 5,0). Geriye kalan S3, gerçek bandı 5,5–8,5 olan 5 örnekten
oluşuyor — yani modelin hâlâ cimri olduğu aralığın tamamı. S1'de ise en düşük bandlı örnek
(GT-T1-1B-A, 3,0) duruyor ve tek başına +1,5 sapıyor. Ortalama **mutlak** fark bu bileşim
farkından etkilenmez ve ikisinde de aynıdır.

### Bu kontrolün kendi zayıflıkları (sonuç temiz çıksa bile yazılmalı)

- **Küme başına 5–7 örnek.** 0,3 bandın altındaki bir ezber etkisini bu n ile ayırt edemeyiz.
- **Tur 3'ün eksiği kümelere eşit dağılmadı:** S1 −1 örnek, S2 −2, S3 −2. Karşılaştırma bu
  yüzden tam simetrik değil.
- **Saklı küme koruması rapor biçimi yüzünden ideal değildi.** `RAPOR-tur2.md`'nin "Örnek örnek"
  tablosu bütün kümeleri tek tabloda listeliyor; 2. düzeltme oturumu dosyayı açtığında S1
  satırları da ekrana geldi (bkz. `degerlendirme/DEGISIKLIK-KAYDI.md`, "Saklı küme hakkında
  dürüst not"). O oturum bütün analizini kümeye kilitli iki script ile S2+S3 üzerinden yaptı ve
  S1'in cevap metinlerini, sınav görevlisi yorumlarını, ölçüt puanlarını hiç açmadı — ama band
  ve sapma satırları göz ucuyla görüldü. **Kalan iş:** `tools/puanlama-raporu.py` kümeye göre
  bölünmüş rapor üretecek şekilde düzeltilmeli.
- Hiçbir küme **hiç görülmemiş** değil; her küme en az bir düzeltmede görünürdü. Tam anlamıyla
  el değmemiş bir test kümesi bu projede **yok**.

---

## 3. Başarı ölçütleri — tek tek

Ölçüt `prompts/SONNET5-A3-puanlama-olcumu.md`'den; sonuç tur 3'ün ölçülen 18 örneğinden.

| # | Ölçüt | Hedef | tur 1 | tur 2 | tur 3 | Sonuç |
|---|---|---|---|---|---|---|
| 1 | Ortalama mutlak fark | < 0,5 band | 0,952 | 0,913 | **0,694** | 🔴 **KALDI** |
| 2 | Tek örnekte sapma | hiçbirinde ≥ 1,5 olmayacak | 2,00 | 2,00 | **1,50** | 🔴 **KALDI** |
| 3 | Eğilim | ±0,25 band içinde | −0,667 | −0,696 | **−0,139** | ✅ **GEÇTİ** |
| 4 | Aynı cevaptaki yayılım | ≤ 0,5 band | 0,33 | — ¹ | **0,19** | ✅ **GEÇTİ** |

**4 ölçütten 2'si geçti.** Üçü de tur 1'de kalmıştı; ikisi düzeltmelerle geçti, ikisi kaldı.

Ölçüt 2 hakkında: kalan tek sapma **tam 1,50** (GT-T1-1B-A: gerçek 3,0 → verilen 4,5). Eşiğe
sıfır pay ile takılıyor ve yönü **yukarı** — yani ölçüt 2'yi düşüren hata ile bölüm 1'deki alt
band şişmesi **aynı hatadır**. Tur 2'de ≥1,5 sapan 7 örnek vardı; bunların 5'i tur 3'te
ölçüldü ve **beşi de** 1,0'ın altına indi. Kalan 2'si (GT-T2-2A-B, GT-T2-2B-C — ikisi de
−2,0) tur 3'te **hiç ölçülmedi**. Ölçüt 2'nin gerçek durumu bu iki örnek puanlanmadan
bilinemez.

Ölçüt 1 hakkında: 0,952 → 0,694 gerçek bir iyileşme ama hedefin (0,5) **%39 üstünde**, üstelik
iyimser taraflı bir sayı. Hedefe bu talimatla ulaşılacağına dair veri yok.

---

## 4. Ürünün gerçek davranışı — tek seferlik puanların dağılımı

Kullanıcı ortalama görmez, **tek bir puan** görür. Tur 3'te 18 örneğin her birinin **ilk**
puanlaması (ortalama değil):

| Verilen − gerçek | Kaç örnek | Örnekler |
|---|---|---|
| −1,0 | 5 | AC-T1-1B-A · AC-T1-1B-B · AC-T1-1C-C · AC-T2-2A-C · GT-T1-1B-D |
| −0,5 | 5 | AC-T1-1A-B · AC-T1-1C-B · AC-T2-2A-B · AC-T2-2B-B · GT-T1-1A-B |
| **0,0** | **2** | GT-T1-1B-B · GT-T1-1B-C |
| +0,5 | 3 | AC-T1-1A-A · AC-T2-2B-A · GT-T1-1A-A |
| +1,0 | 2 | AC-T1-1C-A · AC-T2-2A-A |
| +1,5 | 1 | GT-T1-1B-A |

| | tur 1 (n=21) | tur 2 (n=23) | tur 3 (n=18) |
|---|---|---|---|
| Tam isabet | %14 | %17 | **%11** |
| ±0,5 band içinde | %43 | %43 | **%56** |
| ±1,0 band içinde | %67 | %70 | **%94** |
| ≥1,5 band sapma | 7 örnek | 7 örnek | **1 örnek** |

**Bunun kullanıcı için anlamı, düz cümlelerle:**

- Kullanıcının aldığı puanın **doğru band olma ihtimali yaklaşık %11**. Tam isabet üç turda da
  düşük ve tur 3'te **artmadı**; iyileşen şey isabet değil, **hatanın büyüklüğü**.
- Puanların **%94'ü gerçek banddan en fazla 1 band uzakta**. Ürünün dürüst tarifi budur:
  "yaklaşık ±1 band."
- **Yön hâlâ simetrik değil.** Üst bandda (gerçek ≥7) ortalama −0,79; alt bandda (≤4,5)
  ortalama +1,25. Yani ürün **iyi yazana hak ettiğinden az, kötü yazana hak ettiğinden çok**
  veriyor. Genel eğilimin −0,139'a inmesi bu iki hatanın **birbirini ortalamada götürmesidir**,
  ikisinin de düzelmesi değil. Ölçütlerden biri geçti diye ürün ortalanmış sayılmaz.
- **Ölçek hâlâ dar:** gerçek bandlar 3,0–8,5'e yayılırken verilen puanlar **4,5–7,5**.
  Ürün pratikte 9 ve 8,5 vermiyor; 3 ve 4 de vermiyor.
- **Tutarsızlık:** 18 örneğin 7'sinde üç puanlama aynı çıkmadı (yayılım 0,5); 11'inde üçü de
  aynı. Ortalama yayılım 0,19. Aynı cevabı iki kez gönderen kullanıcı, **10 kişiden ~4'ünde**
  yarım band farklı bir sonuç görür. Ölçüt geçti ama kullanıcının gördüğü şey budur.

---

## 5. 2. düzeltmenin beklentileri tuttu mu

`DEGISIKLIK-KAYDI.md`'nin "Sınanacak beklenti (tur 3)" listesi, tur 3'ün ölçülen 18 örneğiyle:

| # | Beklenti | Sonuç |
|---|---|---|
| 1 | Üst band (≥7) sapması −1,50'den **−0,75 içine** girsin, en az bir örnek 7,5+ alsın | ⚠️ **KIL PAYI KALDI** — −0,79 (hedefe 0,04 uzak). 7,5 şartı ✅ tuttu (AC-T2-2A-C 7,5, AC-T1-1C-C 7,5). n=7 |
| 2 | Üst bandda tutarlılık ölçütü −2,17'den **−1,00 içine** | ✅ **GEÇTİ** — −0,93. Tavanların `max 5` → `max 6` derecelendirmesi (değişiklik 13) turun en net çalışan kalemi |
| 3 | En büyük tek sapma **2,0'ın altına** | ✅ **GEÇTİ** — 1,50 |
| 4 | Eğilim −0,70'ten **−0,35 içine** | ✅ **GEÇTİ** — −0,139 |
| 5 | Orta band (5–6,5) **+0,25'i geçmesin** | ✅ **GEÇTİ** — +0,06. Cimrilikten çıktı, cömertliğe geçmedi |
| 6 | Alt band (≤4,5) **+0,50'nin üstüne çıkmasın** | 🔴 **KALDI** — +1,25. Tam ters yöne gitti |
| 7 | Saklı küme (S1) farkı **açılmasın** | ✅ **GEÇTİ** — 0,032 band |

Yedi beklentiden **beşi tuttu**, biri kıl payı kaçtı, biri **ters yöne gitti**. 2. düzeltmenin
kendi kaydında "bu düzeltmenin en belirsiz yeri" diye işaretlediği madde (alt band) **doğru
tahmin edilmiş korku çıktı**.

---

## 6. Kalan riskler

### 🔴 R1 — Konuşma puanlaması **hiç ölçülmedi**

`kalibrasyon/ornekler/` altında **konuşma klasörü yok**; yalnız `yazma/` var. Üç turda
puanlanan örneklerin **tamamı yazma**. Bu, prompt'un uyardığı "Part 1 örneği yok" durumundan
daha geniştir: Part 1 de, Part 2 de, Part 3 de ölçülmedi.

`degerlendirme/konusma.md`'ye giren bütün değişiklikler (11, 12, 14, 15, 16 ve 1. düzeltmenin
1–4, 9–10'u) **yazma verisinden genellenmiştir** ve konuşmada sınanmamıştır. Konuşmanın kendi
tavan değerlerine (hepsi hâlâ `max 5` — yazmada bunların iki band fazla sert olduğu ölçüldü ve
`max 6`'ya çekildi) **hiç dokunulmadı**, çünkü onları ayarlayacak veri yok. Yazmada bulunan üst
band çöküşünün konuşmada **daha büyük** olması beklenir.

**Sonuç: bu raporun sayılarının hiçbiri konuşma için geçerli değildir.**

### 🔴 R2 — Örnek sayısı az; band bazlı ince ayar yapılamaz

Toplam 23 örnek, gerçek band başına dağılımı:

| Band | 3,0 | 4,0 | 5,0 | 5,5 | 6,0 | 6,5 | 7,0 | 7,5 | 8,0 | 8,5 |
|---|---|---|---|---|---|---|---|---|---|---|
| Örnek | 1 | 2 | 3 | 3 | 4 | 1 | 4 | 1 | 1 | 3 |
| tur 3'te ölçülen | 1 | 1 | 2 | 3 | 3 | 1 | 4 | 1 | **0** | 2 |

Band başına 1–4 örnek. Bu yüzden:

- Tek bir bandın davranışı hakkında **ayar yapılamaz**; bütün düzeltmeler band **aralığı**
  (≥7 / 5–6,5 / ≤4,5) üzerinden yapıldı ve öyle yapılmalı.
- Alt band grubunda tur 3'te **2 örnek** var. Bölüm 1'deki +1,25'lik şişmenin **yönü** güvenilir,
  **büyüklüğü** değil.
- **Band 8,0 tur 3'te hiç ölçülmedi.**
- Bütün örnekler yazma; modül dağılımı: Academic Task 1 = 7, Academic Task 2 = 5,
  General Training Task 1 = 6, General Training Task 2 = 5. Görev türü başına 5–7 örnek — bu da
  görev türüne özel bir sapma tespiti için yetersizdir.

### 🔴 R3 — Tur 3 eksik ölçüldü (23 örnekten 18)

Bölüm 0'da anlatıldı. Etkisi: son turun başlık sayıları **iyimser taraflı**; eksik grup önceki
turlarda ortalamanın üstünde sapıyordu ve en büyük iki sapma (−2,0 ve −2,0, gerçek band 8,0 ve
8,5) o grupta. **Ölçüt 2'nin (≥1,5 sapma yok) gerçek durumu bilinmiyor.**
**Kalan iş:** `python tools/puanlama-raporu.py 3`, GT-T2 grubu Sonnet ile puanlandıktan sonra
tekrar çalıştırılmalı.

### 🔴 R4 — Puanlayan da, talimatı yazan da, örnekleri döken de aynı model ailesi

Örnek cevapları el yazısından metne döken, değerlendirme talimatını yazan, talimatı düzelten ve
o talimatla puanlayan — hepsi Claude ailesinden modeller. **Ortak kör noktalar bu kurulumda
görünmez.** Bir kusuru hem yazan hem ölçen aynı aile ise, o kusur ölçümde hata olarak
belirmez. Farklı bir aileden ikinci bir puanlayıcıyla kontrol yapılmadı ve
**proje sahibinde bekliyor.**

Aynı sebep, dökümlerin kendisi için de geçerli: gerçek bandlar resmî kaynaktan, ama
**metne dökme** işi model tarafından yapıldı.

### R5 — Alt bandda ürün yanlış yönde hata yapıyor (en tehlikeli tek bulgu)

Gerçek bandı 3,0 olan cevap **4,5** alıyor; 4,0 olan **5,0** alıyor. Kullanıcı açısından bu,
"ortalama ±1 band" ifadesinden daha kötüdür: **hazır olmadığı hâlde hazır sanır** ve sınava
erken girer. Ürün, ters yöndeki hatasını (iyi yazana az verme) kullanıcının canını yakmadan
telafi eder; bu yöndekini etmez.

**Kalan iş:** bu, bir sonraki düzeltme turunun **birinci maddesi** olmalıdır. Bu raporda
düzeltme yapılmadı çünkü bu adım rapor adımıdır; ayrıca ≤4,5 aralığında yalnız 3 örnek
(2 tanesi tur 3'te ölçüldü) var — düzeltmeden önce **alt band örneği çoğaltılmalı.**

### R6 — Ölçüm sırası ve saklı küme koruması kusurluydu

Bölüm 2'nin sonunda sayıldı: `RAPOR-tur2.md`'nin tek tablolu biçimi 2. düzeltme oturumunda
saklı küme satırlarını ekrana getirdi; hiçbir küme "hiç görülmemiş" değil; tur 2'de tekrar
sayısı 1 olduğu için tutarlılık o turda sınanmadı.

### R7 — 4 başarı ölçütünden 2'si hâlâ tutmuyor

Ortalama mutlak fark 0,694 (hedef < 0,5) ve en büyük sapma 1,50 (hedef < 1,5). Ürün, kendi
kabul ölçütlerini **karşılamıyor.** Eğilimin ±0,25'e girmesi bunu değiştirmez (bölüm 4: iki
zıt yönlü hatanın ortalamada birbirini götürmesi).

---

## 7. Kapanış

Üç turda ölçülen ve düzeltilen şey **yazma puanlamasıdır** (konuşma için R1'e bakınız: hiç
ölçülmedi). Sapma 0,95 banddan 0,69 banda indi, sistematik cimrilik büyük ölçüde kapandı,
model tutarlı; buna karşılık kabul ölçütlerinin yarısı hâlâ tutmuyor ve alt bandda ürün yanlış
yönde hata yapıyor.

🔴 **Bu iş yalnızca yazma ve konuşma puanlamasının güvenilirliğini ölçer.
Okuma/dinlemede "kaç doğru = hangi band" eşiğini DOĞRULAMAZ** — o eşik yalnız canlı kullanım
verisiyle ayarlanabilir ve bu projede hiç sınanmadı. **Bu yüzden üründe "tahmini band" ibaresi
kalkmaz.**
