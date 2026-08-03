# ⚠️ BU DOSYAYI ÇALIŞTIRMADAN ÖNCE: `/model opus`

Bu dosya **3 kez** çalıştırılır (her seferinde ayrı oturum):

| # | İş paketi | Üretilecek |
|---|---|---|
| 1 | `AC1` + `AC2` + `AC3` + `AC4` tam testleri | 4 × 5 = 20 soru |
| 2 | `GT1` + `GT2` tam testleri | 2 × 7 = 14 soru |
| 3 | Alıştırma | 15 soru |

**Toplam 49 soru.**

Her oturumun başında hangi paketin bittiğine bak, sıradaki bitmemişi yap. Hepsi bittiyse
"OPUS5-11 tamam" de ve çık.

---

## Önce oku

1. `content/PLAN-soru-dagilimi.md` (A, B, D bölümleri + telif ve kalite kuralları)
2. İlgili pasajlar: `passages/academic/*.json`, `passages/general/*.json`
3. Format referansı (klasör boşsa aynı adlı `.pdf`'i Read ile aç): `referans/text/ielts-general-training-reading-computer-delivered-matching-information-answer-key.txt`
   ve `referans/text/ielts-academic-reading-sample-tasks-2023.txt` (yönerge kalıbı için)

---

## Bu prompt tek bir soru tipi üretir: **bilgi eşleştirme**

`question_type`: `matching_information`

Aday, verilen bilginin **hangi paragrafta** (Academic) veya **hangi metinde** (General
Training 1. bölüm) geçtiğini bulur.

Bu tip "güvenli" sayılır çünkü yargı değil **konum tespiti** ister. Ama iki tuzağı var,
ikisine de düşme:

**Tuzak 1 — birden fazla paragrafa uyan ifade.** "Araştırmanın maliyetinden söz eden
paragraf" diyorsun ama maliyet üç paragrafta geçiyor. Soru geçersiz olur.
→ Her soruyu yazdıktan sonra **bütün paragrafları tek tek tara** ve o bilginin başka
paragrafta da olmadığını doğrula. Varsa soruyu daha spesifik yaz veya at.

**Tuzak 2 — kelime eşleşmesiyle bulunabilen soru.** Soruda pasajdaki nadir bir kelimeyi
aynen kullanırsan aday pasajı okumadan bulur.
→ Soru ifadesi **eş anlamlı yeniden ifade** olmalı.

---

## Yönerge kalıpları

**Academic (hangi paragrafta):**
```
The passage has NINE paragraphs, A-I.
Which paragraph contains the following information?
Write the correct letter, A-I, in boxes 27-31 on your answer sheet.
NB You may use any letter more than once.
```

**General Training 1. bölüm (hangi metinde):**
```
Look at the five notices, A-E.
For which notice are the following statements true?
Write the correct letter, A-E, in boxes 1-7 on your answer sheet.
NB You may use any letter more than once.
```

- Paragraf/metin sayısını gerçek sayıya göre yaz
- `NB You may use any letter more than once.` satırını **sadece** gerçekten bir harfi
  birden çok kez kullandıysan koy
- Bu tipte **sıra kuralı yoktur** — cevaplar pasajdaki sırayla olmak zorunda değil, hatta
  olmaması daha iyi

---

## Soru dağılımı kuralı

- Bir grupta **aynı harf en fazla 2 kez** cevap olabilir
- Pasajın **ilk ve son paragrafından da** en az birer soru gelsin (adaylar ortadan sorulmaya alışık)
- Sorulacak bilgi türlerini çeşitlendir: bir örnek · bir karşılaştırma · bir tanım ·
  bir sebep açıklaması · bir tarihsel gelişme · bir uygulama alanı · bir kısıtlama

---

## Çıktı JSON şeması

```json
{
  "schema_version": "1.0",
  "set_id": "AC1-matching-information",
  "skill": "reading",
  "module": "academic",
  "test_id": "AC1",
  "practice": false,
  "passage_id": "A03",
  "question_type": "matching_information",
  "generated_by": "opus",
  "instructions": "The passage has NINE paragraphs, A-I. Which paragraph contains the following information? Write the correct letter, A-I, in boxes 27-31 on your answer sheet. NB You may use any letter more than once.",
  "options": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
  "items": [
    {
      "number": 27,
      "prompt": "a comparison between two methods of measuring distance",
      "answer": ["D"],
      "accepted_variants": ["D"],
      "evidence": "Unlike odometry, which depends on counting steps, optic flow uses the movement of the visual scene across the eye.",
      "evidence_locator": { "paragraph": "D", "sentence": 3 },
      "uniqueness_check": "Ölçüm yöntemi karşılaştırması yalnızca D paragrafında var; B'de tek yöntem anlatılıyor, F'de sonuçlar tartışılıyor.",
      "explanation": "D paragrafı iki mesafe ölçüm yöntemini karşılaştırıyor; diğer paragraflar tek yöntemi anlatıyor.",
      "difficulty": "medium"
    }
  ]
}
```

Ek alanlar:

| Alan | Kural |
|---|---|
| `options` | Paragraf/metin harfleri |
| `uniqueness_check` | **Zorunlu.** Bu bilginin neden sadece o paragrafta olduğunu, karışabilecek diğer paragrafları isim vererek açıkla. Bu alanı dolduramıyorsan soru geçersizdir |
| `evidence` | Doğru paragraftan birebir cümle |
| `explanation` | Türkçe, 1–2 cümle |

---

## Dosya adları

| Paket | Dosya |
|---|---|
| AC1–AC4 (soru 27–31) | `content/reading/tests/AC1/matching-information.json` (her test için ayrı) |
| GT1–GT2 (soru 1–7) | `content/reading/tests/GT1/matching-information.json` |
| Alıştırma (15) | `content/reading/practice/matching-information.json` |

Alıştırmada soru numaraları 1'den başlar, `test_id` `null`, `practice` `true`, her item'a
`passage_id` yaz. Aynı pasajdan en fazla 4 alıştırma sorusu çıkar ve tam testteki
sorularla aynı bilgiyi sorma.

---

## Teslim öncesi kendi kontrol listen

- [ ] Soru sayısı ve numaraları planla birebir aynı
- [ ] Her sorunun `uniqueness_check` alanı dolu ve gerçekten diğer paragrafları elemiş
- [ ] Her `evidence` pasajda birebir geçiyor
- [ ] Hiçbir soru ifadesi pasajdaki nadir kelimeyi aynen kullanmıyor
- [ ] Aynı harf en fazla 2 kez cevap
- [ ] `NB You may use any letter more than once.` satırı doğru kullanılmış
- [ ] Yönergedeki paragraf sayısı ve kutu numaraları gerçek değerlerle uyuşuyor
- [ ] JSON geçerli
- [ ] "IELTS" kelimesi geçmiyor

Şüpheli soruyu sil ve yenisini üret.

---

## Bitirince

`NOTLAR.md` sonuna paketi ve elenen soruları yaz, sonra:

```
git add -A
git commit -m "okuma: bilgi eslestirme AC1-AC4 (20 soru)"
git pull --rebase
git push
```

**Kullanıcıya soru sorma.**
