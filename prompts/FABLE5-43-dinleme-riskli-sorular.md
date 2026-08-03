# ⚠️ BU DOSYAYI ÇALIŞTIRMADAN ÖNCE: `/model fable`

Bu dosya **9 kez** çalıştırılır (her seferinde ayrı oturum):

| # | İş paketi | Üretilecek |
|---|---|---|
| 1–6 | `L1` … `L6` tam testleri | her biri 11 soru (5 → 2. bölüm, 6 → 3. bölüm) |
| 7 | Alıştırma: çoktan seçmeli (tek cevap) | 10 soru |
| 8 | Alıştırma: çoktan seçmeli (birden fazla cevap) | 10 soru |
| 9 | Alıştırma: eşleştirme | 10 soru |

**Toplam 66 + 30 = 96 soru.**

⚠️ **Ön koşul:** `content/listening/scripts/` altında ilgili testin 4 bölümü olmalı.
Yoksa "önce `OPUS5-20` çalıştırılmalı" de ve çık.

Oturum başında hangi paketin bittiğine bak, sıradaki bitmemişi yap. Hepsi bittiyse
"FABLE5-43 tamam" de ve çık.

---

## Önce oku

1. `content/PLAN-soru-dagilimi.md` — E ve F bölümleri, telif ve kalite kuralları
2. Yapacağın testin senaryoları: `content/listening/scripts/L1-S2.json` ve `L1-S3.json`
   (özellikle `turns`, `answer_points` ve `distractor` alanları)
3. Format referansı — `referans/text/`:
   - `ielts-listening-computer-delivered-multiple-choice-one-answer-answer-key.txt`
   - `ielts-listening-computer-delivered-multiple-choice-one-answer-transcript.txt`
   - `ielts-listening-computer-delivered-multiple-choice-more-than-one-answer-answer-key.txt`
   - `ielts-listening-sample-tasks-2023.txt`

---

## Dinleme çoktan seçmelisi okumadakinden FARKLI

Aday sesi **bir kez** duyar ve geri dönemez. Bu üç şeyi zorunlu kılar:

1. **Seçenekler kısa olmalı** — her biri en fazla 10 kelime. Aday soruyu ses gelmeden
   okuyabilmeli. Uzun seçenek = okurken sesi kaçırma = haksız soru.
2. **Cevaplar seste yeterince aralıklı olmalı** — iki sorunun cevabı arka arkaya iki
   replikte olamaz. En az 3 replik ara bırak.
3. **Çeldirici seste geçmeli.** Okumadan farklı olarak, dinlemede iyi çeldirici
   **konuşmacının ağzından çıkan ama doğru olmayan** şeydir.

## Dinlemeye özgü üç çeldirici türü — hepsini kullan

| Tür | Ne yapar |
|---|---|
| **Söylendi sonra düzeltildi** | Konuşmacı önce A der, sonra "aslında hayır, B" der. A çeldirici, B cevap. Senaryodaki `distractor` alanı dolu olan noktalar bunlar |
| **Başkası söyledi** | 3. bölümde bir konuşmacının önerisi, diğerinin görüşü olarak sunulur |
| **Söylendi ama sorulan bu değil** | Sesle geçen doğru bir bilgi ama soru başka bir şeyi soruyor (sebep sorulur, sonuç verilir) |

Her soruda **en az iki farklı** tür kullan. Sesle hiç geçmeyen çeldiriciyi soru başına
en fazla bir tane koy.

---

## Yerleşim (`content/PLAN-soru-dagilimi.md` E bölümü)

| Soru no | Bölüm | Ne üreteceksin |
|---|---|---|
| 11–15 | S2 (tek kişilik anlatım) | 5 soru: 3 tek cevaplı çoktan seçmeli + 1 çift cevaplı (2 numara kaplar) **veya** 5 soruluk bir eşleştirme kümesi |
| 21–26 | S3 (tartışma) | 6 soru: 3 tek cevaplı çoktan seçmeli + 3 soruluk bir eşleştirme kümesi |

Altı test boyunca 11–15 blokunu çeşitlendir: 3 testte çoktan seçmeli, 3 testte
eşleştirme. Seçimini `NOTLAR.md`'ye yaz.

Soru numaraları 1–10, 16–20, 27–40 **sana ait değil** (`OPUS5-21` üretecek). O aralıkları
boş bırak, numaraları kaydırma.

---

## Yönerge kalıpları

```
Choose the correct letter, A, B or C.
```
(Dinlemede genellikle **3 seçenek** olur, okumadaki gibi 4 değil.)

```
Choose TWO letters, A-E.

Which TWO facilities are currently closed?
```

```
What does the speaker say about each of the following activities?

Choose FIVE answers from the box and write the correct letter, A-G, next to questions 11-15.

A   it is fully booked
B   it has been moved to a new site
C   it is free for members
...
```

Eşleştirmede kutu (`box`) seçenekleri soru sayısından **en az 2 fazla** olsun.

---

## Kurallar

1. **3. bölümde kim ne dedi net olsun.** Görüş sorularında konuşmacı adını soruda kullan:
   `What does Marta think about the sample size?`
2. **Sıra kuralı mutlak** — soruların cevapları seste artan sırada duyulmalı.
   `turn_index` ile doğrula. (Eşleştirme kümesi içinde de sıra korunur.)
3. Soru kökü + seçenekler birlikte **50 kelimeyi geçmesin**.
4. Seçenek uzunlukları dengeli olsun.
5. Doğru cevap harfleri dengeli dağılsın; üst üste aynı harf olmasın.
6. Çift cevaplı soruda `number` `"14-15"` biçiminde yazılır ve iki numara kaplar.
7. Cevabın dayandığı repliği **birebir** `evidence` alanına yaz. Boş bırakılamaz.

---

## Çıktı JSON şeması

```json
{
  "schema_version": "1.0",
  "set_id": "L1-multiple-choice",
  "skill": "listening",
  "test_id": "L1",
  "section": 3,
  "practice": false,
  "script_id": "L1-S3",
  "question_type": "multiple_choice",
  "generated_by": "fable",
  "instructions": "Choose the correct letter, A, B or C.",
  "box": null,
  "items": [
    {
      "number": 21,
      "select_count": 1,
      "prompt": "Why does Marta want to change the focus of the project?",
      "options": [
        { "letter": "A", "text": "The original data set was incomplete." },
        { "letter": "B", "text": "Her tutor suggested a different angle." },
        { "letter": "C", "text": "She found the first topic too broad." }
      ],
      "answer": ["C"],
      "evidence": "I started with transport in general, but honestly it was far too wide — I couldn't say anything useful about any of it.",
      "answer_point_id": "L1-S3-04",
      "turn_index": 9,
      "distractor_analysis": {
        "A": "Söylendi ama sorulan bu değil — eksik veriden söz ediliyor, ama bu değişiklik sebebi olarak verilmiyor.",
        "B": "Başkası söyledi — danışman önerisini diğer öğrenci anlatıyor, Marta'nın sebebi değil."
      },
      "explanation": "Marta konuyu değiştirme sebebini kendisi söylüyor: ulaşım konusu çok genişti ve hiçbir şey hakkında anlamlı bir şey söyleyemiyordu.",
      "difficulty": "medium"
    }
  ]
}
```

Eşleştirme kümesi için `question_type` `matching`, `box` dolu, `options` item düzeyinde
yok:

```json
{
  "question_type": "matching",
  "instructions": "What does the speaker say about each of the following activities?\n\nChoose FIVE answers from the box and write the correct letter, A-G, next to questions 11-15.",
  "box": {
    "label": null,
    "options": [
      { "letter": "A", "text": "it is fully booked" },
      { "letter": "B", "text": "it has been moved to a new site" }
    ]
  },
  "allow_repeat": false,
  "items": [
    { "number": 11, "select_count": 1, "prompt": "Pottery workshop",
      "options": null, "answer": ["B"], "evidence": "...", "answer_point_id": "...",
      "turn_index": 12, "distractor_analysis": { "A": "...", "C": "..." },
      "explanation": "...", "difficulty": "medium" }
  ]
}
```

| Alan | Kural |
|---|---|
| `number` | Tek cevaplıda sayı; çift cevaplıda `"14-15"` |
| `select_count` | 1 veya 2 |
| `evidence` | Senaryodan birebir replik, zorunlu |
| `answer_point_id` | Senaryodaki bilgi noktası kimliği. Yeni nokta kullandıysan senaryo dosyasına ekle |
| `turn_index` | Sıra kuralı doğrulaması için zorunlu |
| `distractor_analysis` | Doğru şık hariç her harf için gerekçe (hangi türden çeldirici olduğu dahil) |
| `explanation` | Türkçe, 1–2 cümle |

---

## Dosya adları

| Paket | Dosya |
|---|---|
| L1–L6, 2. bölüm (11–15) | `content/listening/tests/L1/multiple-choice.json` veya `.../matching.json` |
| L1–L6, 3. bölüm (21–26) | `content/listening/tests/L1/multiple-choice.json` + `.../matching.json` |
| Alıştırma tek cevaplı (10) | `content/listening/practice/multiple-choice.json` |
| Alıştırma çift cevaplı (10) | `content/listening/practice/multiple-choice-multi.json` |
| Alıştırma eşleştirme (10) | `content/listening/practice/matching.json` |

Aynı testte hem 2. hem 3. bölümden çoktan seçmeli çıkarsa **tek dosyada** birleştir ve
`section` alanını item düzeyinde de yaz.

Alıştırmada numaralar 1'den başlar, `test_id` `null`, `practice` `true`, `groups`
sarmalayıcısı kullanılır (her küme tek bir senaryodan). Bir senaryodan en fazla 4 soru;
tam testte kullanılan bilgi noktalarını tekrar kullanma.

---

## Teslim öncesi kendi kontrol listen

- [ ] Soru sayısı ve numaraları planla birebir aynı; 1–10, 16–20, 27–40 aralıkları boş
- [ ] Her `evidence` senaryo metninde birebir geçiyor
- [ ] `turn_index` değerleri artan sırada, iki cevap arasında en az 3 replik var
- [ ] Her seçenek en fazla 10 kelime
- [ ] Her soruda en az 2 farklı dinleme çeldirici türü kullanılmış
- [ ] Sesle hiç geçmeyen çeldirici soru başına en fazla 1
- [ ] `distractor_analysis` eksiksiz
- [ ] Eşleştirmede kutu seçenekleri soru sayısından en az 2 fazla
- [ ] Doğru cevap harfleri dengeli, üst üste aynı harf yok
- [ ] 3. bölüm görüş sorularında konuşmacı adı soruda geçiyor
- [ ] JSON geçerli
- [ ] "IELTS" geçmiyor

**Son kontrol:** senaryoyu baştan sona okuyup soruları cevap anahtarına bakmadan çöz.
Uyuşmayan soruyu sil, yenisini üret. Eleme sayısını `NOTLAR.md`'ye yaz.

---

## Bitirince

```bash
cd ~/Desktop/ielts-paketi
git add -A
git commit -m "dinleme L1: riskli sorular (11 soru)"
git pull --rebase
git push
```

**Kullanıcıya soru sorma.**
</content>
