# ⚠️ BU DOSYAYI ÇALIŞTIRMADAN ÖNCE: `/model fable`

Bu dosya **4 kez** çalıştırılır (her seferinde ayrı oturum):

| # | İş paketi | Üretilecek |
|---|---|---|
| 1 | `AC1` + `AC2` tam testleri | 2 × 4 = 8 soru |
| 2 | `AC3` + `AC4` tam testleri | 2 × 4 = 8 soru |
| 3 | `GT1` + `GT2` tam testleri | 2 × 4 = 8 soru |
| 4 | Alıştırma | 15 soru |

**Toplam 24 + 15 = 39 soru.**

Oturum başında hangi paketin bittiğine bak, sıradaki bitmemişi yap. Hepsi bittiyse
"FABLE5-41 tamam" de ve çık.

---

## Neden güçlü model

Çoktan seçmelinin zorluğu doğru cevapta değil, **çeldiricilerde**. Kötü çeldirici iki
şekilde olur: (a) bakar bakmaz elenen aptal seçenek → soru bedava, (b) doğru cevap kadar
savunulabilir seçenek → soru haksız. Bu dosyanın tamamı bu ikisini önlemek için yazıldı.

## Önce oku

1. `content/PLAN-soru-dagilimi.md` — A, B, D bölümleri, telif ve kalite kuralları
2. İlgili pasajlar: `passages/academic/*.json` / `passages/general/*.json`
3. Format referansı — `referans/text/`:
   - `ielts-academic-reading-computer-delivered-multiple-choice-one-answer-answer-key.txt`
   - `ielts-academic-reading-computer-delivered-multiple-choice-more-than-one-answer-answer-key.txt`
   - `ielts-general-training-reading-computer-delivered-multiple-choice-answer-key.txt`

---

## İki alt tip

| Alt tip | `question_type` | Seçenek | Cevap |
|---|---|---|---|
| Tek cevap | `multiple_choice` | A, B, C, D | 1 harf |
| Birden fazla cevap | `multiple_choice_multi` | A–G (7 seçenek) | 2 harf |

Her tam testte **4 sorunun 3'ü tek cevaplı, 1'i çift cevaplı** olsun. Çift cevaplı soru
2 puan sayılır ve iki numarayı birden kaplar — bu yüzden **çift cevaplı soru
kullanacaksan** grubu şöyle kur: 32, 33 tek cevaplı + 34–35 çift cevaplı (tek soru,
iki numara). Alıştırmada 15 sorunun 3'ü çift cevaplı olsun.

## Yönerge kalıpları

```
Choose the correct letter, A, B, C or D.
Write the correct letter in boxes 32-35 on your answer sheet.
```

```
Choose TWO letters, A-G.
Write the correct letters in boxes 34 and 35 on your answer sheet.

Which TWO benefits of the new system does the writer mention?
```

---

## 🔴 Çeldirici tasarımı — dört kural

Her yanlış seçenek, **belirli bir yanlış okuma biçiminden** doğmalı. Rastgele yanlış
cümle yazmak yasak. Kullanılacak dört çeldirici türü:

| Tür | Ne yapar | Örnek |
|---|---|---|
| **Kapsam kaydırma** | Pasajda geçen doğru bilgiyi abartır veya daraltır | Pasaj "çoğu bölgede" der, seçenek "her bölgede" der |
| **Yer değiştirme** | Doğru bilgiyi yanlış özneye/dönemi/yere bağlar | Pasajda A yöntemi için söylenen şeyi B yöntemine yükler |
| **Yakın ama eksik** | Pasajda geçen bir şeyi söyler ama sorulan soruyu cevaplamaz | Soru "sebep" sorar, seçenek "sonuç" verir |
| **Cazip ama yok** | Konuyla ilgili, mantıklı, ama pasajda geçmez | Genel bilgiyle doğru görünen ama metinde olmayan iddia |

Her soruda **en az üç farklı** çeldirici türü kullan.

### Yasaklar

- Hiçbir seçenek diğerinin daha uzun/detaylı hâli olmayacak (uzun seçenek = doğru
  ipucu verir). **Seçenek uzunlukları birbirine yakın olsun** — en uzun, en kısanın iki
  katını geçmesin
- Hiçbir seçenek pasajdaki cümlenin birebir kopyası olmayacak — doğru cevap da dahil
- `All of the above` / `None of the above` yasak
- İki seçenek aynı anlama gelmeyecek (ikisi de yanlış olmalıysa bile birbirinden farklı
  yanlışlar olmalı)
- Doğru cevap harfi grup içinde dengeli dağılsın; iki soru üst üste aynı harf olmasın

---

## Soru kökü kuralları

1. **Soru kökü tek bir şeyi sorsun.** "Yazar aşağıdakilerden hangisini söylüyor?" gibi
   belirsiz kök yasak. İyi kökler: `What does the writer suggest about …?` ·
   `Why did the researchers change their approach?` · `The writer mentions X in order to …`
2. Soruların **hepsi aynı beceriyi ölçmesin**: biri ana fikir, biri ayrıntı, biri yazarın
   amacı/tutumu, biri bir terimin metindeki anlamı.
3. **Sıra kuralı geçerli** — sorular pasajdaki geçiş sırasına göre dizilir.
4. Kök + seçenekler birlikte 60 kelimeyi geçmesin.

---

## Doğrulama — her soru için

1. **Doğru cevabın kanıtını yaz.** Pasajdan birebir cümle. İki cümleyi birleştirmen
   gerekiyorsa ikisini de yaz.
2. **Her çeldirici için eleme gerekçesi yaz** (`distractor_analysis`). Gerekçe
   "pasajda geçmiyor" ise o çeldirici zayıftır — en fazla bir tanesi böyle olabilir,
   kalanların pasajda **kısmen dayanağı** olmalı.
3. **Kendi kendine test:** cevabı unut, soruyu bir aday gibi çöz. Farklı bir şık
   seçtiysen soruyu at.
4. **Savunulabilirlik testi:** her çeldirici için sor — "bu şıkkı savunan bir aday haklı
   olabilir mi?" Cevap "evet" ise o çeldiriciyi değiştir.

---

## Çıktı JSON şeması

```json
{
  "schema_version": "1.0",
  "set_id": "AC1-multiple-choice",
  "skill": "reading",
  "module": "academic",
  "test_id": "AC1",
  "practice": false,
  "passage_id": "A03",
  "question_type": "multiple_choice",
  "generated_by": "fable",
  "instructions": "Choose the correct letter, A, B, C or D.\nWrite the correct letter in boxes 32-33 on your answer sheet.",
  "items": [
    {
      "number": 32,
      "select_count": 1,
      "prompt": "Why did the research team change the location of the second trial?",
      "options": [
        { "letter": "A", "text": "The original site became unavailable." },
        { "letter": "B", "text": "The soil at the first site was too variable." },
        { "letter": "C", "text": "Local residents objected to the equipment." },
        { "letter": "D", "text": "A second site allowed a larger sample." }
      ],
      "answer": ["B"],
      "evidence": "Readings from the first site varied so widely between plots that the team moved the second trial to more uniform ground.",
      "evidence_locator": { "paragraph": "E", "sentence": 2 },
      "distractor_analysis": {
        "A": "Yakın ama eksik — pasaj sahanın kapandığını değil, verilerin tutarsız olduğunu söylüyor.",
        "C": "Cazip ama yok — yerel halktan hiç söz edilmiyor; makul göründüğü için seçiliyor.",
        "D": "Kapsam kaydırma — ikinci sahanın daha büyük olduğu söyleniyor ama taşınma sebebi olarak verilmiyor."
      },
      "explanation": "Paragraf E, ilk sahadaki ölçümlerin parseller arasında çok değişken çıktığını ve ekibin bu yüzden daha türdeş bir alana geçtiğini söylüyor.",
      "difficulty": "medium"
    },
    {
      "number": "34-35",
      "select_count": 2,
      "prompt": "Which TWO advantages of the new method does the writer mention?",
      "options": [
        { "letter": "A", "text": "..." },
        { "letter": "B", "text": "..." },
        { "letter": "C", "text": "..." },
        { "letter": "D", "text": "..." },
        { "letter": "E", "text": "..." },
        { "letter": "F", "text": "..." },
        { "letter": "G", "text": "..." }
      ],
      "answer": ["C", "F"],
      "evidence": "... (iki avantajın geçtiği cümleler)",
      "evidence_locator": { "paragraph": "G", "sentence": 3 },
      "distractor_analysis": { "A": "...", "B": "...", "D": "...", "E": "...", "G": "..." },
      "explanation": "...",
      "difficulty": "hard"
    }
  ]
}
```

| Alan | Kural |
|---|---|
| `number` | Tek cevaplıda sayı; çift cevaplıda `"34-35"` biçiminde metin |
| `select_count` | 1 veya 2 |
| `answer` | Harf dizisi; çift cevaplıda **alfabetik sırada** iki harf |
| `distractor_analysis` | Doğru şık **hariç** her harf için gerekçe. Eksik bırakılamaz |
| `explanation` | Türkçe, 1–2 cümle |

---

## Dosya adları

| Paket | Dosya |
|---|---|
| AC1–AC4 (soru 32–35) | `content/reading/tests/AC1/multiple-choice.json` |
| GT1–GT2 (soru 21–24) | `content/reading/tests/GT1/multiple-choice.json` |
| Alıştırma (15) | `content/reading/practice/multiple-choice.json` |

Alıştırmada numaralar 1'den başlar, `test_id` `null`, `practice` `true`, her item'a
`passage_id`. Bir pasajdan en fazla 4 alıştırma sorusu; tam testte kullanılan yeri
tekrar kullanma.

---

## Teslim öncesi kendi kontrol listen

- [ ] Soru sayısı ve numaraları planla birebir aynı
- [ ] Her testte 3 tek cevaplı + 1 çift cevaplı soru (alıştırmada 12 + 3)
- [ ] Her sorunun `evidence` alanı pasajda birebir geçiyor
- [ ] Her çeldirici için `distractor_analysis` dolu
- [ ] "Pasajda geçmiyor" gerekçesi soru başına en fazla 1 kez
- [ ] Her soruda en az 3 farklı çeldirici türü kullanılmış
- [ ] Seçenek uzunlukları dengeli (en uzun ≤ 2 × en kısa)
- [ ] Hiçbir seçenek pasajdaki cümlenin birebir kopyası değil
- [ ] Doğru cevap harfleri dengeli dağılmış, üst üste aynı harf yok
- [ ] Sorular farklı becerileri ölçüyor (ana fikir / ayrıntı / amaç / anlam)
- [ ] Cevapların pasajdaki sırası, soru sırasıyla aynı
- [ ] JSON geçerli
- [ ] "IELTS" geçmiyor

**Son kontrol:** grubu cevap anahtarına bakmadan kendin çöz. Uyuşmayan soruyu sil,
yenisini üret. Eleme sayısını `NOTLAR.md`'ye yaz.

---

## Bitirince

```bash
cd ~/Desktop/ielts-paketi
git add -A
git commit -m "okuma AC1-AC2: coktan secmeli (8 soru)"
git pull --rebase
git push
```

**Kullanıcıya soru sorma.**
</content>
