# ⚠️ BU DOSYAYI ÇALIŞTIRMADAN ÖNCE: `/model opus`

Bu dosya **10 kez** çalıştırılır (her seferinde ayrı oturum):

| # | İş paketi | Üretilecek |
|---|---|---|
| 1 | `AC1` tam testi | 15 soru |
| 2 | `AC2` tam testi | 15 soru |
| 3 | `AC3` tam testi | 15 soru |
| 4 | `AC4` tam testi | 15 soru |
| 5 | `GT1` tam testi | 13 soru |
| 6 | `GT2` tam testi | 13 soru |
| 7 | Alıştırma: cümle tamamlama + not/tablo tamamlama | 30 soru |
| 8 | Alıştırma: özet tamamlama | 15 soru |
| 9 | Alıştırma: kısa cevap | 10 soru |
| 10 | Alıştırma: diyagram / plan etiketleme | 10 soru |

**Toplam 86 + 65 = 151 soru.**

Her oturumun başında `content/reading/tests/` ve `content/reading/practice/` klasörlerine
bak, hangi paketin bittiğini gör, **sıradaki bitmemiş paketi** yap. Hepsi bittiyse
"OPUS5-10 tamam" de ve çık.

---

## Önce oku

1. `content/PLAN-soru-dagilimi.md` — özellikle A ve B bölümleri (soru yerleşimi),
   D bölümü (alıştırma), telif ve kalite kuralları
2. Yapacağın paketin pasajları: `passages/academic/*.json` veya `passages/general/*.json`
3. Format referansı — ilgili dosyaları `referans/text/` altından oku (yoksa `.pdf`'i Read ile aç):
   - `ielts-academic-reading-computer-delivered-note-completion-answer-key.txt`
   - `ielts-academic-reading-computer-delivered-table-completion-answer-key.txt`
   - `ielts-academic-reading-computer-delivered-sentence-completion-answer-key.txt`
   - `ielts-academic-reading-computer-delivered-summary-completion-selecting-words-from-text-answer-key.txt`
   - `ielts-academic-reading-computer-delivered-summary-completion-selecting-from-list-of-words-or-phrases-answer-key.txt`
   - `ielts-academic-reading-sample-tasks-2023.txt` (yönerge cümlelerinin kalıbı için)

Referanslardan **sadece yönerge kalıbını ve düzeni** alırsın. İçerik kopyalamak yasaktır.

---

## Bu prompt hangi soru tiplerini üretir

Hepsinin ortak özelliği: **cevap pasajda birebir yazılıdır.** Yorum, çıkarım, yargı gerekmez.

| Tip | `question_type` | Ne |
|---|---|---|
| Not tamamlama | `note_completion` | Madde işaretli notlarda boşluk |
| Tablo tamamlama | `table_completion` | Tabloda boş hücre |
| Akış şeması tamamlama | `flow_chart_completion` | Sıralı adımlarda boşluk |
| Özet tamamlama | `summary_completion` | Paragraf özetinde boşluk |
| Cümle tamamlama | `sentence_completion` | Tek cümlede boşluk |
| Kısa cevap | `short_answer` | Soru cümlesi, kısa yanıt |
| Diyagram / plan etiketleme | `diagram_labelling` | Görselde numaralı etiket |

---

## Altın kurallar

1. **Cevap pasajda birebir geçen kelime(ler) olmalı.** Eş anlamlısını yazma, kendi
   kelimeni koyma, çoğul/tekil değiştirme.
2. **Boşluğun etrafındaki metni sen yazarsın, pasajdan kopyalamazsın.** Yani soru kökü
   pasajdaki cümlenin eş anlamlı yeniden ifadesi olur; cevap kelimesi ise birebir aynı kalır.
   Bu tipin bütün zorluğu buradadır — bunu yapmazsan soru "kelime avı"na döner.
3. **Kelime sınırını yönergede belirt ve kendin uy.** Kullanılacak kalıplar:
   - `Choose ONE WORD ONLY from the passage for each answer.`
   - `Choose NO MORE THAN TWO WORDS from the passage for each answer.`
   - `Choose NO MORE THAN THREE WORDS AND/OR A NUMBER from the passage for each answer.`
   Sayılar rakamla yazılır ve tek kelime sayılır (`25`, `1997`). Tireli kelime
   (`well-known`) tek kelime sayılır.
4. **Sıra kuralı:** bu tiplerde sorular pasajda geçiş sırasına göre dizilir. Soru 19'un
   cevabı, soru 20'nin cevabından önce geçmeli.
5. **Cevap benzersiz olmalı.** Aynı kelime pasajda birden çok yerde geçiyorsa ve ikisi de
   boşluğa uyuyorsa, o soruyu değiştir.
6. **Özet tamamlamada iki alt tip var:**
   - *Metinden kelime seçme* → `word_bank: null`
   - *Listeden kelime seçme* → `word_bank` dolu (8–10 seçenek, A-J harfli; en az 3 çeldirici
     fazla olacak). Bu alt tipte cevap pasajda birebir geçmek zorunda değildir ama listedeki
     kelime pasajın anlamını **kesin** karşılamalıdır.
7. **Diyagram etiketlemede görsel gerekir.** `visual` alanına kendi çizdiğin SVG'yi koy
   (aşağıda anlatıldı). Pasaj somut bir nesne/süreç/mekân tarif etmiyorsa o pasajı bu tip
   için kullanma, başka pasaj seç.

---

## Diyagram / plan etiketleme için görsel

`visual` alanına harici dosyaya bağlı olmayan, tek parça SVG koy:

```json
"visual": {
  "kind": "diagram",
  "svg": "<svg viewBox=\"0 0 400 300\" xmlns=\"http://www.w3.org/2000/svg\">...</svg>",
  "alt": "Bir su arıtma tesisinin dört aşamalı şeması; 1, 2 ve 3 numaralı kutular boş."
}
```

Kurallar:
- Sadece `rect`, `circle`, `line`, `path`, `polygon`, `text` kullan
- Renk: siyah çizgi (`#000`), beyaz dolgu. Uygulama koyu tema uygulayacak, sabit renk verme
- `viewBox` mutlaka olsun, sabit `width`/`height` verme
- Boşluklar SVG içinde `1`, `2`, `3` diye numaralanmış kutular olsun
- Yazı boyutu `font-size="12"`, `font-family="sans-serif"`

---

## Çıktı JSON şeması

Bir dosya = bir soru grubu (aynı yönergeyi paylaşan sorular).

```json
{
  "schema_version": "1.0",
  "set_id": "AC1-note-completion",
  "skill": "reading",
  "module": "academic",
  "test_id": "AC1",
  "practice": false,
  "passage_id": "A01",
  "question_type": "note_completion",
  "generated_by": "opus",
  "instructions": "Complete the notes below. Choose ONE WORD ONLY from the passage for each answer.",
  "word_limit": "ONE WORD ONLY",
  "word_bank": null,
  "visual": null,
  "stem_block": "Desert ant navigation\n- Distance measured by counting (1) ........\n- Direction taken from patterns of (2) ........",
  "items": [
    {
      "number": 1,
      "prompt": "Distance measured by counting (1) ........",
      "answer": ["steps"],
      "accepted_variants": ["steps"],
      "evidence": "The ants keep track of how far they have walked by counting their steps.",
      "evidence_locator": { "paragraph": "C", "sentence": 2 },
      "explanation": "Paragraf C, karıncanın mesafeyi adımlarını sayarak ölçtüğünü söylüyor; boşluk 'counting' fiilinden sonra geldiği için cevap 'steps'.",
      "difficulty": "easy"
    }
  ]
}
```

Alan açıklamaları:

| Alan | Kural |
|---|---|
| `set_id` | `<TEST>-<tip>` veya alıştırmada `practice-<tip>` |
| `practice` | Alıştırma dosyalarında `true`, tam testlerde `false` |
| `test_id` | Alıştırmada `null` |
| `stem_block` | Not/tablo/akış şeması/özet gövdesi, boşluklar `(n) ........` biçiminde. Cümle tamamlama, kısa cevap ve diyagramda `null` |
| `answer` | Dizi. Tek cevaplıysa tek elemanlı |
| `accepted_variants` | Kabul edilecek yazımlar (büyük/küçük harf farkı hariç). Ör. `["car park","carpark"]`. Yoksa `answer` ile aynı |
| `evidence` | Pasajdan **birebir** cümle. Boş bırakılamaz |
| `evidence_locator` | Paragraf harfi + kaçıncı cümle |
| `explanation` | **Türkçe**, 1–2 cümle. Uygulama yanlış cevap açıklaması olarak gösterecek |
| `difficulty` | `easy` / `medium` / `hard` — grup içinde karışık olsun |

Tablo tamamlamada `stem_block` yerine `table` kullan:

```json
"table": {
  "headers": ["Method", "Advantage", "Limitation"],
  "rows": [
    ["Satellite imaging", "(1) ........", "expensive"],
    ["Ground survey", "accurate", "(2) ........"]
  ]
}
```

---

## Dosya adları

Tam test paketleri (`AC1`–`AC4`, `GT1`, `GT2`) — `content/PLAN-soru-dagilimi.md`'deki
yerleşime birebir uy:

**Academic testte senin ürettiklerin:**
| Soru no | Tip | Dosya |
|---|---|---|
| 1–6 | not / tablo / akış şeması tamamlama | `content/reading/tests/AC1/note-completion.json` (veya `table-completion` / `flow-chart-completion`) |
| 19–22 | cümle tamamlama | `content/reading/tests/AC1/sentence-completion.json` |
| 36–40 | özet tamamlama | `content/reading/tests/AC1/summary-completion.json` |

1–6 için hangi tipi seçeceğine pasaja bakarak karar ver: adım adım bir süreç anlatıyorsa
akış şeması, karşılaştırma varsa tablo, geri kalanında not tamamlama. **Dört Academic
testte hepsi aynı tip olmasın** — çeşitlendir ve kararını `NOTLAR.md`'ye yaz.

**GT testte senin ürettiklerin:**
| Soru no | Tip | Dosya |
|---|---|---|
| 15–20 | not / tablo tamamlama | `content/reading/tests/GT1/note-completion.json` |
| 25–27 | cümle tamamlama | `content/reading/tests/GT1/sentence-completion.json` |
| 37–40 | özet tamamlama | `content/reading/tests/GT1/summary-completion.json` |

**Alıştırma paketleri:**
| Paket | Dosya(lar) |
|---|---|
| 7 | `content/reading/practice/sentence-completion.json` (15) + `content/reading/practice/note-completion.json` (15) |
| 8 | `content/reading/practice/summary-completion.json` (15) |
| 9 | `content/reading/practice/short-answer.json` (10) |
| 10 | `content/reading/practice/diagram-labelling.json` (10) |

Alıştırmalarda soru numaraları **1'den başlar** ve dosya içinde devam eder. Pasajları
havuzdan serbestçe seç ama:
- Aynı pasajdan en fazla 4 alıştırma sorusu çıkar
- **Tam testteki soruyla aynı bilgiyi hedefleme** — o testin dosyasını açıp bak, farklı
  cümlelerden sor
- Her sorunun `passage_id` alanı dolu olsun (alıştırmada sorular farklı pasajlardan
  gelebileceği için `passage_id`'yi grup değil **item** düzeyinde de yaz)

---

## Teslim öncesi kendi kontrol listen

Her dosya için tek tek doğrula, eksik varsa düzelt:

- [ ] Soru sayısı hedefle **birebir** aynı
- [ ] Soru numaraları plandaki aralıkla birebir aynı (ör. 19,20,21,22)
- [ ] Her `evidence` pasaj metninde **gerçekten** geçiyor (kopyala-ara ile doğrula)
- [ ] Her cevap kelimesi pasajda birebir geçiyor (listeden seçme özeti hariç)
- [ ] Hiçbir cevap `word_limit` sınırını aşmıyor
- [ ] Cevapların pasajdaki geçiş sırası, soru sırasıyla aynı
- [ ] Hiçbir soru kökü pasajdaki cümlenin birebir kopyası değil
- [ ] Aynı cevap iki soruda tekrar etmiyor
- [ ] `explanation` alanları Türkçe ve dolu
- [ ] JSON geçerli: `python3 -c "import json;json.load(open('DOSYA'))"` hatasız çalışıyor
- [ ] Soru metinlerinde "IELTS" geçmiyor

Şüpheli bir soru varsa **sil ve yerine yenisini üret** — eksik teslim etme.

---

## Bitirince

`NOTLAR.md` sonuna ekle: hangi paket yapıldı, kaç soru, hangi pasajlar, seçilen alt tipler,
elenen soru varsa sebebi.

```bash
cd ~/Desktop/ielts-paketi
git add -A
git commit -m "okuma AC1: tamamlama tipleri (15 soru)"
git pull --rebase
git push
```

Commit mesajını yaptığın pakete göre yaz. **Kullanıcıya soru sorma.**
</content>
