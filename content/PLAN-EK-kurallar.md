# PLAN — EK KURALLAR

Bu dosya `PLAN-soru-dagilimi.md`'ye eklenen istisnaları taşır (o dosya elle değiştirilmez).

## Kalite kuralı 2 istisnası

Cevabı NOT GIVEN olan sorularda `evidence` boş kalır; gerekçe `not_given_justification`
alanına yazılır. `tools/dogrula.py` zaten NOT GIVEN'ı `evidence` zorunluluğundan muaf
tutuyor — bu kural yazısı aracın davranışına uydurulmuş oluyor, tersi değil.

## FAZ 1 — B3 okuma: yeni pasajlar ve yeni ölçüm kuralları (2026-08-17)

### 1. Yeni pasaj kimlikleri

`A13`–`A19` (akademik, 7 pasaj) + `G07` (General Training, 1 pasaj). Hepsi
`passages/INDEX.json`'da `pool: "practice"`, `assigned_test: null` ile işaretlenir.

**Kural: alıştırma havuzu ile test havuzu ayrıdır.** Bir pasaj ikisinde birden
kullanılamaz — `A01`–`A12`/`G01`–`G06` test tarafına, `A13`–`A19`/`G07` alıştırma
tarafına aittir; karışmaz.

### 2. Pasaj başına soru bütçesi

- Paragraf başına **en çok 3 soru**.
- Kanıt cümlesi (`evidence`) başına **en çok 1 soru**.

### 3. Boşluk açma kuralı

Boşluk, kalıbın/eşdizim öbeğinin ucuna değil, **kaynağın kendi seçtiği değere** açılır.
(Örn. "Each animal was tested... where a heavy (1) ........ had already been placed"
gibi kalıbın son kelimesine değil, kaynağın kendi çalışmasında rapor ettiği somut
değere.)

### 4. Gerçek olay yasağı

Ünlü, gerçek olay + kamuya açık sayı kullanılmaz (B4 dersi — JWST/Uranus, Kandula,
PANAS/POMS, Britanya mevzuatı gibi sayıları haberden bilinen olgular). Sayısal
cevaplar metnin kendi çalışmasının seçtiği değerler olur — dışarıdan doğrulanabilir/
ezbere bilinebilir olmaz.

### 5. Cümle sonu eşleştirme reçetesi (bağlayıcı — `matching_sentence_endings`)

Yanlış sonlardan **en az ikisi** her kök için dilbilgisi ve anlam olarak oturacak;
ayrım yalnız pasaj ayrıntısıyla yapılabilecek. Hangi iki rakip sonun oturduğu
`grammar_check` alanında **tek tek yazılacak** (tek rakiple yetinmek yetersiz ölçüldü).

### 6. Yeni pasaj kimliği yazım yeri

Yeni üretilecek alıştırma sorularında `passage_id`, dosya düzeyinde değil **kalem
(item) veya grup (group) düzeyinde** yazılacak — uygulama bu zinciri (kalem → grup →
dosya) okuyor, dosya düzeyi alıştırma paketlerinde `null` kalmalı.

### 7. Ölçüm eşikleri

- Cümle sonu eşleştirme: **≤ %20** (10 soruda en çok 2) + yukarıdaki reçete denetimi.
- Dinleme seçenekli tipler (çoktan seçmeli, eşleştirme): **≤ %30**.
- Dinleme tamamlama ailesi (form/not/tablo/akış şeması/kısa cevap): **≤ %20**.
