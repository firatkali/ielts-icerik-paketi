# SORU DAĞILIM PLANI

> Bu dosya `00-KURULUM.md` tarafından `content/PLAN-soru-dagilimi.md` olarak yazılır.
> Bütün üretim promptları bunu okur. **Elle değiştirilmez.**

## Toplam hedef: 1.310 soru

| Beceri | Tam test | Tip alıştırması | Toplam |
|---|---|---|---|
| Okuma | 240 (6 test) | 160 | 400 |
| Dinleme | 240 (6 test) | 120 | 360 |
| Konuşma | — | 440 | 440 |
| Yazma | — | 110 | 110 |
| **TOPLAM** | | | **1.310** |

## Test kimlikleri

| Kimlik | Ne |
|---|---|
| `AC1` `AC2` `AC3` `AC4` | Academic okuma tam testi (her biri 3 pasaj, 40 soru) |
| `GT1` `GT2` | General Training okuma tam testi (3 bölüm, 40 soru) |
| `L1` … `L6` | Dinleme tam testi (4 bölüm, 40 soru) |

## Pasaj kimlikleri

| Kimlik | Ne | Kaynak |
|---|---|---|
| `A01`–`A12` | Academic okuma pasajı, 700–900 kelime | CC BY / kamu malı |
| `G01`–`G02` | GT 1. bölüm metin seti (4–5 kısa günlük metin, toplam ~400 kelime) | **Orijinal yazılır** |
| `G03`–`G04` | GT 2. bölüm metin seti (2 iş/eğitim metni, toplam ~500 kelime) | **Orijinal yazılır** |
| `G05`–`G06` | GT 3. bölüm uzun metin, 750–900 kelime | CC BY / kamu malı |

Pasaj → test eşlemesi:

| Test | Pasaj 1 | Pasaj 2 | Pasaj 3 |
|---|---|---|---|
| AC1 | A01 | A02 | A03 |
| AC2 | A04 | A05 | A06 |
| AC3 | A07 | A08 | A09 |
| AC4 | A10 | A11 | A12 |
| GT1 | G01 | G03 | G05 |
| GT2 | G02 | G04 | G06 |

---

## A. Academic okuma testi — soru yerleşimi (AC1, AC2, AC3, AC4 — dördü de aynı)

| Soru no | Pasaj | Soru tipi | Üreten prompt |
|---|---|---|---|
| 1–6 | 1 | Not / tablo / akış şeması tamamlama | `OPUS5-10` |
| 7–13 | 1 | TRUE / FALSE / NOT GIVEN | `FABLE5-40` |
| 14–18 | 2 | Başlık eşleştirme (matching headings) | `FABLE5-42` |
| 19–22 | 2 | Cümle tamamlama | `OPUS5-10` |
| 23–26 | 2 | Özellik eşleştirme (matching features) | `FABLE5-42` |
| 27–31 | 3 | Bilgi eşleştirme — hangi paragrafta | `OPUS5-11` |
| 32–35 | 3 | Çoktan seçmeli | `FABLE5-41` |
| 36–40 | 3 | Özet tamamlama (summary completion) | `OPUS5-10` |

Test başına: OPUS5-10 → 15 · OPUS5-11 → 5 · FABLE5-40 → 7 · FABLE5-41 → 4 · FABLE5-42 → 9 = **40**

## B. General Training okuma testi — soru yerleşimi (GT1, GT2 — ikisi de aynı)

| Soru no | Bölüm | Soru tipi | Üreten prompt |
|---|---|---|---|
| 1–7 | 1 | Bilgi eşleştirme — hangi metinde (A–E) | `OPUS5-11` |
| 8–14 | 1 | TRUE / FALSE / NOT GIVEN | `FABLE5-40` |
| 15–20 | 2 | Not / tablo tamamlama | `OPUS5-10` |
| 21–24 | 2 | Çoktan seçmeli | `FABLE5-41` |
| 25–27 | 2 | Cümle tamamlama | `OPUS5-10` |
| 28–32 | 3 | Başlık eşleştirme | `FABLE5-42` |
| 33–36 | 3 | YES / NO / NOT GIVEN | `FABLE5-40` |
| 37–40 | 3 | Özet tamamlama | `OPUS5-10` |

Test başına: OPUS5-10 → 13 · OPUS5-11 → 7 · FABLE5-40 → 11 · FABLE5-41 → 4 · FABLE5-42 → 5 = **40**

## C. Okuma — tam test toplamları (6 test = 240 soru)

| Prompt | AC (×4) | GT (×2) | Toplam |
|---|---|---|---|
| `OPUS5-10` | 60 | 26 | 86 |
| `OPUS5-11` | 20 | 14 | 34 |
| `FABLE5-40` | 28 | 22 | 50 |
| `FABLE5-41` | 16 | 8 | 24 |
| `FABLE5-42` | 36 | 10 | 46 |
| | | | **240** |

## D. Okuma — soru tipi alıştırması (160 soru, aynı pasaj havuzundan)

| Soru tipi | Adet | Üreten prompt |
|---|---|---|
| Cümle tamamlama | 15 | `OPUS5-10` |
| Not / tablo tamamlama | 15 | `OPUS5-10` |
| Özet tamamlama | 15 | `OPUS5-10` |
| Kısa cevap | 10 | `OPUS5-10` |
| Diyagram / plan etiketleme | 10 | `OPUS5-10` |
| Bilgi eşleştirme (hangi paragrafta) | 15 | `OPUS5-11` |
| TRUE / FALSE / NOT GIVEN | 15 | `FABLE5-40` |
| YES / NO / NOT GIVEN | 15 | `FABLE5-40` |
| Çoktan seçmeli | 15 | `FABLE5-41` |
| Başlık eşleştirme | 15 | `FABLE5-42` |
| Özellik eşleştirme | 10 | `FABLE5-42` |
| Cümle sonu eşleştirme | 10 | `FABLE5-42` |
| **TOPLAM** | **160** | |

⚠️ Alıştırma soruları **tam testlerdeki sorularla aynı olamaz**. Aynı pasajı kullanır ama
farklı bilgiyi hedefler.

## E. Dinleme testi — soru yerleşimi (L1…L6 — altısı da aynı)

| Soru no | Bölüm | İçerik | Soru tipi | Üreten prompt |
|---|---|---|---|---|
| 1–10 | 1 | Günlük durumda 2 kişilik konuşma | Form / not / tablo tamamlama | `OPUS5-21` |
| 11–15 | 2 | Günlük konuda tek kişilik anlatım | Çoktan seçmeli veya eşleştirme | `FABLE5-43` |
| 16–20 | 2 | (aynı bölüm) | Plan / harita / diyagram etiketleme | `OPUS5-21` |
| 21–26 | 3 | Eğitim ortamında 2–4 kişilik tartışma | Çoktan seçmeli + eşleştirme | `FABLE5-43` |
| 27–30 | 3 | (aynı bölüm) | Cümle tamamlama | `OPUS5-21` |
| 31–40 | 4 | Akademik ders (tek kişi) | Not / özet / akış şeması tamamlama + kısa cevap | `OPUS5-21` |

Test başına: OPUS5-21 → 29 · FABLE5-43 → 11 = **40**
6 test: OPUS5-21 → 174 · FABLE5-43 → 66 = **240**

Senaryo metinlerini (24 bölüm = 6 test × 4 bölüm) `OPUS5-20` üretir.

## F. Dinleme — soru tipi alıştırması (120 soru, aynı senaryolardan)

| Soru tipi | Adet | Üreten prompt |
|---|---|---|
| Form / not tamamlama | 15 | `OPUS5-21` |
| Tablo tamamlama | 15 | `OPUS5-21` |
| Cümle tamamlama | 15 | `OPUS5-21` |
| Akış şeması tamamlama | 15 | `OPUS5-21` |
| Kısa cevap | 15 | `OPUS5-21` |
| Plan / harita / diyagram etiketleme | 15 | `OPUS5-21` |
| Çoktan seçmeli (tek cevap) | 10 | `FABLE5-43` |
| Çoktan seçmeli (birden fazla cevap) | 10 | `FABLE5-43` |
| Eşleştirme | 10 | `FABLE5-43` |
| **TOPLAM** | **120** | |

## G. Konuşma + Yazma (550 birim) — hepsi `OPUS5-30`

| İçerik | Adet |
|---|---|
| Konuşma 1. bölüm: 20 konu × 10 soru | 200 |
| Konuşma 2. bölüm: konuşma kartı | 60 |
| Konuşma 3. bölüm: her kart için 3 tartışma sorusu | 180 |
| Yazma Academic 1. görev (grafik/tablo/süreç/harita) | 30 |
| Yazma General 1. görev (mektup) | 20 |
| Yazma 2. görev (deneme yazısı, Academic + General ortak) | 60 |
| **TOPLAM** | **550** |

---

## Çıktı dosya yolları (değişmez)

```
passages/academic/A01.json … A12.json
passages/general/G01.json … G06.json

content/reading/tests/<TEST>/<tip>.json          örn. content/reading/tests/AC1/note-completion.json
content/reading/practice/<tip>.json              örn. content/reading/practice/true-false-not-given.json

content/listening/scripts/<TEST>-S<n>.json       örn. content/listening/scripts/L1-S3.json
content/listening/tests/<TEST>/<tip>.json
content/listening/practice/<tip>.json

content/speaking/part1/<konu-kodu>.json          örn. content/speaking/part1/T01-hometown.json
content/speaking/part2-3/<kart-kodu>.json        örn. content/speaking/part2-3/C01.json
content/writing/academic-task1/<kod>.json        örn. content/writing/academic-task1/AT01.json
content/writing/general-task1/<kod>.json
content/writing/task2/<kod>.json
```

Soru tipi dosya adları (kebab-case, sabit):
`note-completion` · `table-completion` · `flow-chart-completion` · `summary-completion` ·
`sentence-completion` · `short-answer` · `diagram-labelling` · `matching-information` ·
`matching-headings` · `matching-features` · `matching-sentence-endings` ·
`true-false-not-given` · `yes-no-not-given` · `multiple-choice` ·
`multiple-choice-multi` · `matching` · `form-completion` · `plan-map-diagram-labelling`

---

## Telif kuralları (HER oturumda geçerli, istisnasız)

1. **Resmi IELTS belgeleri (`referans/`) sadece FORMAT referansıdır.** Yönerge cümlelerinin
   kalıbına, soru düzenine, cevap anahtarı biçimine bakarsın. **Tek bir pasaj cümlesi,
   soru metni veya senaryo replası kopyalanmaz, çevrilmez, yeniden yazılmaz.**
2. **Okuma pasajları yalnızca `passages/` havuzundan gelir.** Kendi kafandan pasaj
   uydurma, internetten yeni pasaj çekme.
3. **Yasak kaynaklar:** Cambridge IELTS kitapları ve bunların internetteki kopyaları,
   British Council / IDP materyalleri, Wikipedia (CC BY-SA — bulaşıcı lisans),
   The Conversation (CC BY-ND — türev yasak). **Aranmaz, indirilmez, kullanılmaz.**
4. **İzinli kaynaklar:** PLOS dergileri (CC BY), NASA / NOAA / USGS (kamu malı),
   OpenStax (CC BY). Her pasajda kaynak + lisans + adres bilgisi zorunlu.
5. Soru ve pasaj metinlerinde **"IELTS" kelimesi geçmez** (tescilli marka). Dosya adı ve
   JSON alanlarında geçebilir, kullanıcıya gösterilecek metinde geçmez.
6. Kişi isimleri, kurum isimleri, marka isimleri uydurma olmalı — gerçek şirket/kişi
   kullanma.

## Kalite kuralları (HER soru için geçerli)

1. **Tek ve tartışmasız cevap.** İki cevabın da savunulabildiği soru üretilmez.
2. **Kanıt zorunlu.** Her sorunun `evidence` alanında, cevabın dayandığı cümle pasajdan/
   senaryodan **birebir** alıntılanır. Alıntı bulunamıyorsa soru silinir.
3. **Kelime sınırına uy.** "ONE WORD ONLY" dediysen cevap tek kelime olmalı; "NO MORE THAN
   TWO WORDS" dediysen cevap en fazla iki kelime olmalı. Kendi kuralını ihlal etme.
4. **Sıra kuralı.** Tamamlama ve doğru/yanlış tipi sorular pasajda **geçiş sırasına göre**
   dizilir. Eşleştirme ve çoktan seçmeli için bu kural yoktur.
5. **Birebir kopya cümle yasak.** Soru kökü pasajdaki cümlenin aynısı olamaz — eş anlamlı
   kelime ve yapı değişikliği (paraphrase) şart. Aksi hâlde soru "kelime arama"ya dönüşür.
6. **Cevaplar pasajın tamamına yayılsın**, tek paragrafta yığılmasın.
