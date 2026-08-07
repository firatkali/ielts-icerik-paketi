# Envanter Uyuşması Denetimi

- **Tarih:** 2026-08-07
- **Kaynak:** `python tools/manifest.py` çıktısı (`content/MANIFEST.json`) ↔ `content/PLAN-soru-dagilimi.md`
- **Kural gereği bu rapor sadece durum tespiti yapar; hiçbir içerik dosyası değiştirilmemiştir.**

---

## 1. Beceri bazında hedef / üretilen / fark

| Beceri | Hedef | Üretilen | Fark | İşaretli (flagged) | Kullanılabilir (üretilen − işaretli) | Kullanılabilir hedefi tutuyor mu? |
|---|---:|---:|---:|---:|---:|---|
| Okuma | 400 | 400 | 0 | **180** | **220** | **HAYIR — 180 eksik** |
| Dinleme | 360 | 360 | 0 | 0 | 360 | Evet |
| Konuşma | 440 | 440 | 0 | 0 | 440 | Evet |
| Yazma | 110 | 110 | 0 | 0 | 110 | Evet |
| **TOPLAM** | **1.310** | **1.310** | **0** | **180** | **1.130** | — |

Destek malzemesi (soru sayılmaz ama plan hedefi var):

| Malzeme | Hedef | Üretilen | Fark |
|---|---:|---:|---:|
| Okuma pasajı (A01–A12) | 12 | 12 | 0 |
| GT metin seti (G01–G06) | 6 | 6 | 0 |
| Dinleme senaryosu (6 test × 4 bölüm) | 24 | 24 | 0 |

Ayrıca test bazında yerleşim tutuyor: 6 okuma testi ve 6 dinleme testinin **her biri tam 40 soru**
(AC1–AC4, GT1–GT2, L1–L6). Konuşma kırılımı planla birebir: 1. bölüm 20 konu × 10 = 200,
kart 60, 3. bölüm 180. Yazma kırılımı da birebir: Academic 1. görev 30, General mektup 20,
2. görev 60.

**İşaretlilerin tamamı okuma becerisinde.** Dinleme, konuşma ve yazmada hiç işaret yok
(dinlemede çapraz kontrolün hiç sorun bulamamış olması dikkat çekicidir; bu envanterin değil
2. çalıştırmanın — çapraz kontrol özetinin — konusudur, orada irdelenmeli).

---

## 2. Soru tipi bazında — Okuma

### 2a. Okuma tam testleri (AC1–AC4 + GT1–GT2, hedef 240)

Plandaki AC 1–6 yuvası "not / tablo / akış şeması tamamlama" ailesi olarak tek hedef verir
(AC 24 + GT 12 = 36); tabloda üç tip ayrı satırda, aile toplamı dipnotta.

| Soru tipi | Hedef | Üretilen | Fark | İşaretli | Kullanılabilir |
|---|---:|---:|---:|---:|---:|
| Not tamamlama | (aile*) | 18 | — | 7 | 11 |
| Tablo tamamlama | (aile*) | 12 | — | 4 | 8 |
| Akış şeması tamamlama | (aile*) | 6 | — | 4 | 2 |
| TRUE / FALSE / NOT GIVEN | 42 | 42 | 0 | 22 | 20 |
| YES / NO / NOT GIVEN | 8 | 8 | 0 | **8** | **0** |
| Başlık eşleştirme | 30 | 30 | 0 | 5 | 25 |
| Cümle tamamlama | 22 | 22 | 0 | 9 | 13 |
| Özellik eşleştirme | 16 | 16 | 0 | **14** | **2** |
| Bilgi eşleştirme | 34 | 34 | 0 | 2 | 32 |
| Çoktan seçmeli | 24 | 24 | 0 | **18** | **6** |
| Özet tamamlama | 28 | 28 | 0 | **19** | **9** |
| **TOPLAM** | **240** | **240** | **0** | **112** | **128** |

\* Not+tablo+akış ailesi: hedef 36, üretilen 36, fark 0, işaretli 15, kullanılabilir 21.

### 2b. Okuma alıştırmaları (hedef 160)

| Soru tipi | Hedef | Üretilen | Fark | İşaretli | Kullanılabilir |
|---|---:|---:|---:|---:|---:|
| Cümle tamamlama | 15 | 15 | 0 | 4 | 11 |
| Not / tablo tamamlama | 15 | 15 | 0 | 2 | 13 |
| Özet tamamlama | 15 | 15 | 0 | 7 | 8 |
| Kısa cevap | 10 | 10 | 0 | 2 | 8 |
| Diyagram / plan etiketleme | 10 | 10 | 0 | 0 | 10 |
| Bilgi eşleştirme | 15 | 15 | 0 | 1 | 14 |
| TRUE / FALSE / NOT GIVEN | 15 | 15 | 0 | 8 | 7 |
| YES / NO / NOT GIVEN | 15 | 15 | 0 | **15** | **0** |
| Çoktan seçmeli | 15 | 15 | 0 | **12** | **3** |
| Başlık eşleştirme | 15 | 15 | 0 | 3 | 12 |
| Özellik eşleştirme | 10 | 10 | 0 | 4 | 6 |
| Cümle sonu eşleştirme | 10 | 10 | 0 | **10** | **0** |
| **TOPLAM** | **160** | **160** | **0** | **68** | **92** |

---

## 3. Soru tipi bazında — Dinleme

### 3a. Dinleme tam testleri (L1–L6, hedef 240)

Plan dinleme testinde tipleri yuva (bölüm) düzeyinde belirler; tip karışımı testten teste
değişebilir. Yuva toplamları planla tutuyor: FABLE5-43 yuvaları (çoktan seçmeli + eşleştirme)
hedef 66 → üretilen 33 + 33 = 66; OPUS5-21 yuvaları hedef 174 → üretilen 174.

| Soru tipi | Üretilen | İşaretli | Kullanılabilir |
|---|---:|---:|---:|
| Form tamamlama | 40 | 0 | 40 |
| Not tamamlama | 27 | 0 | 27 |
| Tablo tamamlama | 15 | 0 | 15 |
| Akış şeması tamamlama | 10 | 0 | 10 |
| Özet tamamlama | 15 | 0 | 15 |
| Cümle tamamlama | 24 | 0 | 24 |
| Kısa cevap | 13 | 0 | 13 |
| Plan / harita / diyagram | 30 | 0 | 30 |
| Çoktan seçmeli | 33 | 0 | 33 |
| Eşleştirme | 33 | 0 | 33 |
| **TOPLAM** | **240** | **0** | **240** |

### 3b. Dinleme alıştırmaları (hedef 120)

| Soru tipi | Hedef | Üretilen | Fark | İşaretli | Kullanılabilir |
|---|---:|---:|---:|---:|---:|
| Form / not tamamlama | 15 | 15 | 0 | 0 | 15 |
| Tablo tamamlama | 15 | 15 | 0 | 0 | 15 |
| Cümle tamamlama | 15 | 15 | 0 | 0 | 15 |
| Akış şeması tamamlama | 15 | 15 | 0 | 0 | 15 |
| Kısa cevap | 15 | 15 | 0 | 0 | 15 |
| Plan / harita / diyagram | 15 | 15 | 0 | 0 | 15 |
| Çoktan seçmeli (tek) | 10 | 10 | 0 | 0 | 10 |
| Çoktan seçmeli (çoklu) | 10 | 10 | 0 | 0 | 10 |
| Eşleştirme | 10 | 10 | 0 | 0 | 10 |
| **TOPLAM** | **120** | **120** | **0** | **0** | **120** |

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

---

## 5. Boş alan denetimi (cevap anahtarı / explanation / evidence)

- **Cevap anahtarı (`answer`) boş olan soru: YOK.** (okuma + dinleme, 760 soru tarandı)
- **Açıklama (`explanation`) boş olan soru: YOK.**
- **Konuşma / yazma birimlerinde** eksik zorunlu alan (prompt, kart başlığı/maddeleri,
  key_points) **YOK.** (Bu birimlerde cevap anahtarı / kanıt alanı şema gereği bulunmaz.)
- **Kanıt (`evidence`) boş olan soru: 22 adet.** Tamamının cevabı **NOT GIVEN** — bu cevapta
  kanıt cümlesi doğası gereği yoktur (bilgi pasajda yok), yani yapısal olarak beklenen bir
  boşluk. Yine de kalite kuralı 2 "kanıt zorunlu" dediği için liste aşağıda; 22'nin 12'si
  zaten `flagged`. Karar proje sahibinin.

| Dosya | Soru no | Durum |
|---|---|---|
| `content/reading/practice/true-false-not-given.json` | 3, 7, 10 | flagged |
| `content/reading/practice/true-false-not-given.json` | 14 | verified |
| `content/reading/practice/yes-no-not-given.json` | 1, 8, 10, 13 | flagged |
| `content/reading/tests/AC1/true-false-not-given.json` | 8 | verified |
| `content/reading/tests/AC1/true-false-not-given.json` | 13 | flagged |
| `content/reading/tests/AC2/true-false-not-given.json` | 9 | verified |
| `content/reading/tests/AC2/true-false-not-given.json` | 13 | flagged |
| `content/reading/tests/AC3/true-false-not-given.json` | 10, 13 | verified |
| `content/reading/tests/AC4/true-false-not-given.json` | 9, 12 | verified |
| `content/reading/tests/GT1/true-false-not-given.json` | 11, 14 | verified |
| `content/reading/tests/GT1/yes-no-not-given.json` | 36 | flagged |
| `content/reading/tests/GT2/true-false-not-given.json` | 9, 13 | flagged |
| `content/reading/tests/GT2/yes-no-not-given.json` | 33 | flagged |

**Ek tespit — arada kalmış durum:** 2 soru ne `verified` ne `flagged`; `status: "review"`
olarak kalmış ve bu yüzden 180'lik işaretli sayımına girmiyor:

| Dosya | Soru no | Cevap |
|---|---|---|
| `content/reading/practice/matching-headings.json` | 9 | x |
| `content/reading/tests/GT1/matching-information.json` | 3 | C |

Seçenekler: bu ikisi ya elden geçirilip `verified`/`flagged` yapılır ya da işaretli sayılır;
karar proje sahibinin.

---

## 6. Özet

Üretim envanteri hedefle birebir tutuyor (1.310/1.310 soru, 18/18 pasaj, 24/24 senaryo,
boş cevap anahtarı/açıklama yok); ancak işaretliler düşülünce okuma 220/400'e iniyor ve
en büyük eksik, kullanılabilir sorusu neredeyse hiç kalmayan okuma tiplerinde (YES/NO/NOT
GIVEN 0, cümle sonu eşleştirme 0, özellik eşleştirme 2, çoktan seçmeli 6+3).
