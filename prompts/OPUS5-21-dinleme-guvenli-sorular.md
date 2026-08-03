# ⚠️ BU DOSYAYI ÇALIŞTIRMADAN ÖNCE: `/model opus`

Bu dosya **12 kez** çalıştırılır (her seferinde ayrı oturum):

| # | İş paketi | Üretilecek |
|---|---|---|
| 1–6 | `L1` … `L6` tam testleri (her biri) | 29 soru |
| 7 | Alıştırma: form / not tamamlama | 15 soru |
| 8 | Alıştırma: tablo tamamlama | 15 soru |
| 9 | Alıştırma: cümle tamamlama | 15 soru |
| 10 | Alıştırma: akış şeması tamamlama | 15 soru |
| 11 | Alıştırma: kısa cevap | 15 soru |
| 12 | Alıştırma: plan / harita / diyagram etiketleme | 15 soru |

**Toplam 174 + 90 = 264 soru.**

⚠️ **Ön koşul:** `content/listening/scripts/` altında ilgili testin 4 bölümü yazılmış
olmalı. Yoksa "önce `OPUS5-20` çalıştırılmalı" de ve çık.

Oturum başında hangi paketin bittiğine bak, sıradaki bitmemişi yap. Hepsi bittiyse
"OPUS5-21 tamam" de ve çık.

---

## Önce oku

1. `content/PLAN-soru-dagilimi.md` — E ve F bölümleri, telif ve kalite kuralları
2. Yapacağın testin senaryoları: `content/listening/scripts/L1-S1.json` … `L1-S4.json`
   (özellikle `turns` ve `answer_points`)
3. Format referansı — `referans/text/` altındaki cevap anahtarları (yoksa `.pdf` Read ile):
   - `ielts-listening-computer-delivered-note-completion-answer-key.txt`
   - `ielts-listening-computer-delivered-table-completion-answer-key.txt`
   - `ielts-listening-computer-delivered-sentence-completion-answer-key.txt`
   - `ielts-listening-computer-delivered-flow-chart-completion-answer-key.txt`
   - `ielts-listening-computer-delivered-short-answer-answer-key.txt`
   - `ielts-listening-computer-delivered-plan-map-diagram-labelling-answer-key.txt`
   - `ielts-listening-sample-tasks-2023.txt` (yönerge kalıpları)

---

## Bu prompt hangi soru tiplerini üretir

Cevabın seste **birebir söylendiği** tipler:

| Tip | `question_type` | Nerede kullanılır |
|---|---|---|
| Form tamamlama | `form_completion` | 1. bölüm |
| Not tamamlama | `note_completion` | 1. ve 4. bölüm |
| Tablo tamamlama | `table_completion` | 1. ve 4. bölüm |
| Cümle tamamlama | `sentence_completion` | 3. bölüm |
| Akış şeması tamamlama | `flow_chart_completion` | 4. bölüm |
| Özet tamamlama | `summary_completion` | 4. bölüm |
| Kısa cevap | `short_answer` | 4. bölüm |
| Plan / harita / diyagram etiketleme | `plan_map_diagram_labelling` | 2. bölüm |

## Tam testte yerleşim (`content/PLAN-soru-dagilimi.md` E bölümü)

| Soru no | Bölüm | Ne üreteceksin | Dosya |
|---|---|---|---|
| 1–10 | S1 | Form / not / tablo tamamlama | `content/listening/tests/L1/form-completion.json` |
| 16–20 | S2 | Plan / harita / diyagram etiketleme | `content/listening/tests/L1/plan-map-diagram-labelling.json` |
| 27–30 | S3 | Cümle tamamlama | `content/listening/tests/L1/sentence-completion.json` |
| 31–40 | S4 | Not / özet / akış şeması tamamlama + kısa cevap | `content/listening/tests/L1/note-completion.json` (+ gerekiyorsa ikinci dosya) |

1–10 için tip seçimi: senaryo bir kayıt/rezervasyon ise **form**, karşılaştırma içeriyorsa
**tablo**, geri kalanında **not**. 31–40 blokunu **ikiye böl**: 31–36 tamamlama +
37–40 kısa cevap (veya 31–35 akış şeması + 36–40 not). Altı testte hepsi aynı olmasın,
seçimini `NOTLAR.md`'ye yaz.

Soru numaraları 11–15 ve 21–26 **sana ait değil** — onları `FABLE5-43` üretecek. O
aralıkları boş bırak, numaraları kaydırma.

---

## Altın kurallar

1. **Cevap seste birebir söylenmeli.** `answer` alanı, konuşmacının ağzından çıkan
   kelimenin aynısı olmalı. Eş anlamlısını yazma.
2. **Soru kökü sesteki cümlenin aynısı olamaz** — eş anlamlı yeniden ifade şart.
   Ama boşluğa gelen kelime birebir kalır.
3. **Sıra kuralı mutlak.** Dinlemede geri dönüş yok: soru 3'ün cevabı, soru 4'ün
   cevabından **önce** duyulmalı. `answer_points` içindeki `turn_index` değerlerini
   kullanarak bunu doğrula.
4. **Cevaplar arasında nefes payı bırak.** İki cevap arka arkaya aynı replikte olmasın —
   aralarında en az bir replik geçsin. Aksi hâlde soru insanlık dışı zorlaşır.
5. **Kelime sınırı:** yönergede belirt, kendin uy.
   - `Write ONE WORD AND/OR A NUMBER for each answer.`
   - `Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each answer.`
   - `Write NO MORE THAN THREE WORDS AND/OR A NUMBER for each answer.`
6. **Yazım kabulü.** Dinlemede yanlış yazım yanlış cevaptır, o yüzden:
   - Zor yazılan isimler ancak **seste harf harf söylendiyse** sorulabilir
   - Sayılar için hem rakam hem yazı kabul et: `accepted_variants: ["25", "twenty-five"]`
   - Para/ölçü için sembollü ve sembolsüz: `["£25", "25 pounds", "25"]`
   - İngiliz/Amerikan yazım farkı varsa ikisini de kabul et: `["colour", "color"]`
7. **Çeldiriciyi kullan.** Senaryoda `distractor` alanı dolu olan noktaları tercihen soru
   yap — sınavın ayırt ediciliği oradan gelir. Ama cevap **düzeltilmiş** değer olmalı.
8. Bir bölümde **aynı türden** (hep sayı, hep isim) cevap yığılmasın.

---

## Plan / harita / diyagram etiketleme (16–20)

Senaryonun 2. bölümündeki `spatial_description` alanını kullan.

`visual` alanına kendi çizdiğin SVG'yi koy:

```json
"visual": {
  "kind": "plan",
  "svg": "<svg viewBox=\"0 0 480 360\" xmlns=\"http://www.w3.org/2000/svg\">...</svg>",
  "alt": "Ziyaretçi merkezinin zemin kat planı; 16-20 numaralı beş oda etiketsiz.",
  "labels": ["A", "B", "C", "D", "E", "F", "G", "H"]
}
```

SVG kuralları:
- Sadece `rect`, `circle`, `line`, `path`, `polygon`, `text`
- Siyah çizgi (`#000`), dolgu yok veya beyaz — sabit renk paleti kullanma
- `viewBox` zorunlu, sabit `width`/`height` yasak
- Boşluk yerleri **numara** ile (`16`, `17`…), seçenek yerleri **harf** ile gösterilir
- `font-size="12"`, `font-family="sans-serif"`
- Kuzey oku, giriş kapısı ve en az bir sabit referans noktası (etiketi verilmiş) olsun —
  aday nereden başlayacağını bilmeli

İki alt tip var, ikisini de kullan (testler arasında dönüşümlü):
- **Harf seçme:** planda A–H harfli konumlar var, aday numaraya karşılık harfi yazar →
  `options` dolu
- **Kelime yazma:** planda numaralı boşluklar var, aday sesten duyduğu adı yazar →
  `options` null, `word_limit` dolu

---

## Çıktı JSON şeması

```json
{
  "schema_version": "1.0",
  "set_id": "L1-form-completion",
  "skill": "listening",
  "test_id": "L1",
  "section": 1,
  "practice": false,
  "script_id": "L1-S1",
  "question_type": "form_completion",
  "generated_by": "opus",
  "instructions": "Complete the form below. Write ONE WORD AND/OR A NUMBER for each answer.",
  "word_limit": "ONE WORD AND/OR A NUMBER",
  "options": null,
  "visual": null,
  "stem_block": "CAR HIRE BOOKING\nSurname: (1) ........\nCollection date: (2) ........\nDaily rate: £(3) ........",
  "table": null,
  "items": [
    {
      "number": 1,
      "prompt": "Surname: (1) ........",
      "answer": ["Kowalczyk"],
      "accepted_variants": ["Kowalczyk"],
      "evidence": "That's Kowalczyk — K-O-W-A-L-C-Z-Y-K.",
      "answer_point_id": "L1-S1-01",
      "turn_index": 6,
      "distractor_used": null,
      "explanation": "Soyadı seste harf harf söyleniyor: K-O-W-A-L-C-Z-Y-K.",
      "difficulty": "easy"
    },
    {
      "number": 2,
      "prompt": "Collection date: (2) ........",
      "answer": ["8 March"],
      "accepted_variants": ["8 March", "8th March", "March 8", "the 8th of March"],
      "evidence": "It was the fifteenth, but we've moved it forward — it's now the eighth of March.",
      "answer_point_id": "L1-S1-07",
      "turn_index": 22,
      "distractor_used": "15 March",
      "explanation": "Konuşmacı önce 15'ini söylüyor ama sonra düzeltiyor: tarih 8 Mart'a alınmış.",
      "difficulty": "medium"
    }
  ]
}
```

| Alan | Kural |
|---|---|
| `stem_block` | Form/not/akış şeması gövdesi, boşluklar `(n) ........`. Cümle tamamlama, kısa cevap ve etiketlemede `null` |
| `table` | Tablo tamamlamada `{ "headers": [...], "rows": [[...]] }`, diğerlerinde `null` |
| `evidence` | Senaryodan **birebir** replik. Boş bırakılamaz |
| `answer_point_id` | Senaryodaki `answer_points` kimliği. Yeni bilgi noktası kullandıysan `null` yazma — senaryo dosyasını güncelleyip yeni id ekle |
| `turn_index` | Sıra kuralı doğrulaması için zorunlu |
| `distractor_used` | Çeldirici varsa yanlış değer, yoksa `null` |
| `explanation` | **Türkçe**, 1–2 cümle |

---

## Alıştırma paketleri (7–12)

Dosyalar: `content/listening/practice/<tip>.json` (tip adları `content/PLAN-soru-dagilimi.md`
sonundaki listede).

Kurallar:
- Soru numaraları 1'den başlar, `test_id` `null`, `practice` `true`
- 24 senaryonun tamamından serbestçe yararlan; her item'a `script_id` yaz
- Bir senaryodan en fazla 4 alıştırma sorusu çıkar
- **Tam testteki soruyla aynı bilgi noktasını kullanma** — o testin dosyalarını açıp
  kullanılmış `answer_point_id` değerlerini gör, farklılarını seç
- Alıştırma soruları **3'erli-5'erli kümeler** hâlinde grupla (`groups` alanı): her küme
  tek bir senaryodan gelsin ve kendi `stem_block`/`instructions` değerine sahip olsun

Alıştırma dosyasında birden çok küme olduğu için şema şöyle sarmalanır:

```json
{
  "schema_version": "1.0",
  "set_id": "practice-table-completion",
  "skill": "listening",
  "test_id": null,
  "practice": true,
  "question_type": "table_completion",
  "generated_by": "opus",
  "groups": [
    { "group_id": "P-TC-01", "script_id": "L2-S1", "instructions": "...",
      "word_limit": "...", "table": {...}, "items": [ ... ] }
  ]
}
```

---

## Teslim öncesi kendi kontrol listen

- [ ] Soru sayısı ve numaraları planla birebir aynı; 11–15 ve 21–26 aralıkları boş
- [ ] Her `evidence` senaryo metninde birebir geçiyor (ara ve doğrula)
- [ ] Her cevap seste birebir söyleniyor
- [ ] `turn_index` değerleri **artan** sırada (sıra kuralı)
- [ ] İki cevap aynı replikte değil
- [ ] Hiçbir cevap `word_limit` sınırını aşmıyor
- [ ] `accepted_variants` sayı/para/tarih için yeterince geniş
- [ ] Harf harf söylenmeyen zor yazımlı isim sorulmamış
- [ ] Etiketleme sorusunda SVG geçerli (tek satır string, kaçış karakterleri doğru) ve
      en az bir sabit referans noktası etiketli
- [ ] `explanation` alanları Türkçe ve dolu
- [ ] JSON geçerli: `python3 -c "import json;json.load(open('DOSYA'))"`
- [ ] "IELTS" kelimesi geçmiyor

Şüpheli soruyu sil, yenisini üret.

---

## Bitirince

`NOTLAR.md` sonuna: hangi paket, kaç soru, seçilen tipler, kullanılan `answer_point_id`'ler.

```bash
cd ~/Desktop/ielts-paketi
git add -A
git commit -m "dinleme L1: guvenli sorular (29 soru)"
git pull --rebase
git push
```

**Kullanıcıya soru sorma.**
</content>
