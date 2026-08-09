# Envanter Uyuşması Denetimi — 2. tur

- **Tarih:** 2026-08-09
- **Kaynak:** `python tools/manifest.py` (bu denetimde yeniden koşuldu, `content/MANIFEST.json`
  güncellendi) ↔ `content/PLAN-soru-dagilimi.md`. Bütün sayılar dosyalardan bu denetimde
  yeniden sayıldı; önceki rapordan kopyalanmadı. Kontrol: `python tools/dogrula.py`
  (12 tam test 40/40, şema hatası 0, toplam 1310).
- **1. tur karşılaştırması:** `denetim/tur1/envanter.md` (2026-08-07).
- **Kural gereği bu rapor sadece durum tespiti yapar; hiçbir içerik dosyası değiştirilmemiştir.**

Sayım notu: çift cevaplı çoktan seçmeli kalemler soru **numarası** bazında 2 sayılır
(manifest ile aynı kural). Bu yüzden iki işaretli sayısı vardır: **237 kalem**
(manifest'in saydığı) = **250 soru numarası**. Aşağıdaki tablolar numara bazındadır.

---

## 1. Beceri bazında hedef / üretilen / fark

| Beceri | Hedef | Üretilen | Fark | İşaretli (flagged) | Kullanılabilir | Kullanılabilir hedefi tutuyor mu? | 1. turda |
|---|---:|---:|---:|---:|---:|---|---|
| Okuma | 400 | 400 | 0 | **122** | **278** | **HAYIR — 122 eksik** | işaretli 180, kullanılabilir 220 |
| Dinleme | 360 | 360 | 0 | **128** | **232** | **HAYIR — 128 eksik** | işaretli 0 (ölçülmemişti) |
| Konuşma | 440 | 440 | 0 | 0 | 440 | Evet (sızıntı ölçümü kapsam dışı) | aynı |
| Yazma | 110 | 110 | 0 | 0 | 110 | Evet (sızıntı ölçümü kapsam dışı) | aynı |
| **TOPLAM** | **1.310** | **1.310** | **0** | **250** | **1.060** | — | işaretli 180, kullanılabilir 1.130 |

**1. tura göre ne değişti:** Okuma işaretlisi 180 → 122'ye indi (E5 elden geçirme + E6
yeniden üretim + E7 yeniden ölçüm sonucu; işaretlerin bileşimi tamamen yenilendi, aşağıda).
Dinleme 0 → 128'e çıktı — ama bu bozulma değil, 1. turun "dinleme hiç ölçülmedi" açığının
kapanması: beş çalıştırmalık sızıntı ölçümü (`SESSIZ-RAPOR.md`) yapıldı ve 121 kalem
(128 numara) işaretlendi. **Toplam kullanılabilir sayı 1.130'dan 1.060'a düştü; bu,
havuz kötüleştiği için değil, karanlık bölge ölçüldüğü için oldu.**

Destek malzemesi (soru sayılmaz ama plan hedefi var):

| Malzeme | Hedef | Üretilen | Fark |
|---|---:|---:|---:|
| Okuma pasajı (A01–A12) | 12 | 12 | 0 |
| GT metin seti (G01–G06) | 6 | 6 | 0 |
| Dinleme senaryosu (6 test × 4 bölüm) | 24 | 24 | 0 |

Test bazında yerleşim tutuyor: 6 okuma + 6 dinleme testinin her biri tam 40 soru
(`dogrula.py` 12/12 TAM). Konuşma kırılımı planla birebir (200 + 60 + 180), yazma da
(30 + 20 + 60).

---

## 2. Soru tipi bazında — Okuma

### 2a. Okuma tam testleri (AC1–AC4 + GT1–GT2, hedef 240)

Plandaki not/tablo/akış ailesi tek hedef (36); üç tip ayrı satırda.

| Soru tipi | Hedef | Üretilen | Fark | İşaretli | Kullanılabilir | 1. turda kullanılabilir |
|---|---:|---:|---:|---:|---:|---:|
| Not tamamlama | (aile*) | 18 | — | 7 | 11 | 11 |
| Tablo tamamlama | (aile*) | 12 | — | 3 | 9 | 8 |
| Akış şeması tamamlama | (aile*) | 6 | — | 4 | 2 | 2 |
| TRUE / FALSE / NOT GIVEN | 42 | 42 | 0 | 6 | 36 | 20 |
| YES / NO / NOT GIVEN | 8 | 8 | 0 | 4 | 4 | **0** |
| Başlık eşleştirme | 30 | 30 | 0 | 1 | 29 | 25 |
| Cümle tamamlama | 22 | 22 | 0 | 7 | 15 | 13 |
| Özellik eşleştirme | 16 | 16 | 0 | 6 | 10 | **2** |
| Bilgi eşleştirme | 34 | 34 | 0 | 1 | 33 | 32 |
| Çoktan seçmeli | 24 | 24 | 0 | 13 | 11 | **6** |
| Özet tamamlama | 28 | 28 | 0 | 17 | 11 | 9 |
| **TOPLAM** | **240** | **240** | **0** | **69** | **171** | **128** |

\* Not+tablo+akış ailesi: hedef 36, üretilen 36, fark 0, işaretli 14, kullanılabilir 22.

### 2b. Okuma alıştırmaları (hedef 160)

| Soru tipi | Hedef | Üretilen | Fark | İşaretli | Kullanılabilir | 1. turda kullanılabilir |
|---|---:|---:|---:|---:|---:|---:|
| Cümle tamamlama | 15 | 15 | 0 | 8 | 7 | 11 |
| Not / tablo tamamlama | 15 | 15 | 0 | 5 | 10 | 13 |
| Özet tamamlama | 15 | 15 | 0 | 10 | 5 | 8 |
| Kısa cevap | 10 | 10 | 0 | 1 | 9 | 8 |
| Diyagram / plan etiketleme | 10 | 10 | 0 | 0 | 10 (ölçülemedi — görsel) | 10 |
| Bilgi eşleştirme | 15 | 15 | 0 | 0 | 15 | 14 |
| TRUE / FALSE / NOT GIVEN | 15 | 15 | 0 | 1 | 14 | 7 |
| YES / NO / NOT GIVEN | 15 | 15 | 0 | 5 | 10 | **0** |
| Çoktan seçmeli | 15 | 15 | 0 | 11 | 4 | **3** |
| Başlık eşleştirme | 15 | 15 | 0 | 1 | 14 | 12 |
| Özellik eşleştirme | 10 | 10 | 0 | 2 | 8 | 6 |
| Cümle sonu eşleştirme | 10 | 10 | 0 | **9** | **1** | **0** |
| **TOPLAM** | **160** | **160** | **0** | **53** | **107** | **92** |

Okuma genelinde tip düzeyinde durum:

- **Belirgin düzelenler:** TFNG 27 → 50 kullanılabilir, YNNG 0 → 14, çoktan seçmeli 9 → 15,
  özellik eşleştirme 8 → 18, başlık eşleştirme 37 → 43.
- **Hâlâ kritik:** cümle sonu eşleştirme **1/10** (E7 ölçümünün kendi tespiti: "rakip-ekleme
  bu tipte yetmedi, yeniden üretim sonraki halkaya devredildi"), akış şeması 2/6,
  okuma çoktan seçmelisi toplamda 15/39, özet tamamlama 16/43.
- **Geriye gidenler:** alıştırma cümle tamamlama 11 → 7, alıştırma özet 8 → 5 — E7'nin anlam
  düzeyi (K3) ölçütü ve çapraz-pasaj bulgusu bu tiplerde 1. turun görmediği sızıntıyı
  yakaladı; `sentence_completion` E7 raporunda "düzelmedi" (%43 > resmî taban %20) diye
  açıkça işaretli.

---

## 3. Soru tipi bazında — Dinleme

Dinleme 1. turda hiç sızıntı ölçümüne girmemişti; bu turdaki bütün işaretler yeni
(`SESSIZ-RAPOR.md`, 5 çalıştırma; kaynak: senaryo gösterilmeden 3/3 turda bilinme, K3
anlam düzeyi, yalnız dayanağı anlamsal olanlar işaretli).

### 3a. Dinleme tam testleri (L1–L6, hedef 240)

Yuva toplamları planla tutuyor: FABLE5-43 yuvaları 66 (çoktan seçmeli 33 + eşleştirme 33),
OPUS5-21 yuvaları 174.

| Soru tipi | Üretilen | İşaretli | Kullanılabilir |
|---|---:|---:|---:|
| Form tamamlama | 40 | 5 | 35 |
| Not tamamlama | 27 | 8 | 19 |
| Tablo tamamlama | 15 | 2 | 13 |
| Akış şeması tamamlama | 10 | 4 | 6 |
| Özet tamamlama | 15 | 9 | 6 |
| Cümle tamamlama | 24 | 5 | 19 |
| Kısa cevap | 13 | 8 | 5 |
| Plan / harita / diyagram | 30 | 0 (ölçülemedi — görsel) | 30 |
| Çoktan seçmeli | 33 | 20 | 13 |
| Eşleştirme | 33 | 22 | 11 |
| **TOPLAM** | **240** | **83** | **157** |

Test bazında işaret: L1 13 · L2 10 · L3 18 · L4 16 · L5 16 · L6 10. **Altı dinleme
testinin hiçbiri işaretsiz değil**; işaretliler atılırsa hiçbir dinleme testi 40 soruyla
oynatılamaz.

### 3b. Dinleme alıştırmaları (hedef 120)

| Soru tipi | Hedef | Üretilen | Fark | İşaretli | Kullanılabilir |
|---|---:|---:|---:|---:|---:|
| Form / not tamamlama | 15 | 15 | 0 | 2 | 13 |
| Tablo tamamlama | 15 | 15 | 0 | 2 | 13 |
| Cümle tamamlama | 15 | 15 | 0 | 3 | 12 |
| Akış şeması tamamlama | 15 | 15 | 0 | 9 | 6 |
| Kısa cevap | 15 | 15 | 0 | 7 | 8 |
| Plan / harita / diyagram | 15 | 15 | 0 | 0 (ölçülemedi) | 15 |
| Çoktan seçmeli (tek) | 10 | 10 | 0 | 7 | 3 |
| Çoktan seçmeli (çoklu) | 10 | 10 | 0 | 8 | 2 |
| Eşleştirme | 10 | 10 | 0 | 7 | 3 |
| **TOPLAM** | **120** | **120** | **0** | **45** | **75** |

Dinlemede en kritik tipler: eşleştirme toplam **14/43** kullanılabilir, çoktan seçmeli
(tek+çoklu) **18/63**, kısa cevap 13/28, özet 6/15, akış 12/25. Ölçülemeyen 45 plan/harita
sorusu "temiz" değil, "ölçüm dışı" (görsel gerektirir).

---

## 4. Konuşma + Yazma (hedef 550)

| İçerik | Hedef | Üretilen | Fark | İşaretli |
|---|---:|---:|---:|---:|
| Konuşma 1. bölüm (20 konu × 10) | 200 | 200 | 0 | 0 |
| Konuşma 2. bölüm kartı | 60 | 60 | 0 | 0 |
| Konuşma 3. bölüm sorusu | 180 | 180 | 0 | 0 |
| Yazma Academic 1. görev | 30 | 30 | 0 | 0 |
| Yazma General 1. görev (mektup) | 20 | 20 | 0 | 0 |
| Yazma 2. görev | 60 | 60 | 0 | 0 |
| **TOPLAM** | **550** | **550** | **0** | **0** |

1. turdan farksız. Bu iki beceriye sızıntı/doğruluk ölçümü uygulanmadı (kapsam dışı);
"işaret 0" temizlik kanıtı değildir. Örnek cevap kütüphanesi bu envanterin dışında ama
mevcut: 110 yazma görevinin ve 60 konuşma kartının 3'er seviyeli örnekleri üretilmiş
(ayrıntı hedefleriyle karşılaştırma bu raporun kapsamında değil).

---

## 5. Boş alan denetimi (cevap anahtarı / explanation / evidence)

Okuma + dinleme 760 soru kalemi tarandı:

- **Cevap anahtarı (`answer`) boş: YOK.**
- **Açıklama (`explanation`) boş: YOK.**
- **Konuşma / yazma birimlerinde** eksik zorunlu alan YOK (bu şemalarda cevap
  anahtarı/kanıt alanı bulunmaz).
- **Kanıt (`evidence`) boş: 23 soru** — tamamının cevabı NOT GIVEN, tamamı
  `status: "verified"`, ve **23'ünün 23'ünde `not_given_justification` alanı dolu**
  (negatif gerekçe yazılmış). 1. turdaki A6 açık maddesi bu yolla kapatılmış: kanıt
  cümlesi doğası gereği olmayan cevaba, "bilgi pasajda yok" gerekçesi alanına yazılmış.
  Yapısal olarak beklenen boşluk; ek iş gerektirmiyor. Liste:

| Dosya | Soru no |
|---|---|
| `content/reading/practice/true-false-not-given.json` | 3, 7, 10, 14 |
| `content/reading/practice/yes-no-not-given.json` | 1, 8, 10, 13, 15 |
| `content/reading/tests/AC1/true-false-not-given.json` | 8, 13 |
| `content/reading/tests/AC2/true-false-not-given.json` | 9, 13 |
| `content/reading/tests/AC3/true-false-not-given.json` | 10, 13 |
| `content/reading/tests/AC4/true-false-not-given.json` | 9, 12 |
| `content/reading/tests/GT1/true-false-not-given.json` | 11, 14 |
| `content/reading/tests/GT1/yes-no-not-given.json` | 36 |
| `content/reading/tests/GT2/true-false-not-given.json` | 9, 13 |
| `content/reading/tests/GT2/yes-no-not-given.json` | 33 |

(1. turda 22 idi; +1 fark E6'nın yeniden ürettiği `practice/yes-no-not-given` 15 —
o da NOT GIVEN cevaplı ve gerekçeli.)

**1. turun iki askıdaki sorusu kapanmış:** `practice/matching-headings` 9 ve
`GT1/matching-information` 3 artık `verified`; depo genelinde `status` değeri
`verified`/`flagged` dışında olan soru **kalmadı** (1. turda 2 vardı).

**Küçük tutarsızlık (yeni):** işaretli 116 okuma kaleminin **26'sında `flag_mechanism`
alanı boş** (E7'nin işaretledikleri arasında; gerekçe metninde dayanak var ama mekanizma
alanı doldurulmamış). Dinlemede 121/121 dolu. İşaretliler elden geçirilecekse bu 26'nın
mekanizması önce doldurulmalı (1. tur A2 maddesinin küçük kalıntısı).

---

## 6. Özet

Üretim envanteri hedefle birebir tutuyor (1.310/1.310 soru, 18/18 pasaj, 24/24 senaryo,
12 tam test 40/40, boş cevap anahtarı/açıklama yok, askıda soru yok); ancak işaretliler
düşülünce kullanılabilir stok okumada 278/400, dinlemede 232/360 — okuma 1. tura göre
58 soru düzeldi, dinlemenin 128'lik açığı ise yeni yapılmış sızıntı ölçümünün ilk kez
görünür kıldığı gerçek durum; en dar yerler cümle sonu eşleştirme (1/10), dinleme
eşleştirme (14/43) ve dinleme çoktan seçmeli (18/63).
