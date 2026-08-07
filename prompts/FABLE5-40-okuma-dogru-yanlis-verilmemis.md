# ⚠️ BU DOSYAYI ÇALIŞTIRMADAN ÖNCE: `/model fable`

Yanlış modelde çalıştırırsan soru kalitesi düşer. `/model` yazıp `fable` seçtiğinden emin ol.

Bu dosya **8 kez** çalıştırılır (her seferinde ayrı oturum):

| # | İş paketi | Üretilecek |
|---|---|---|
| 1–4 | `AC1` … `AC4` tam testleri | her biri 7 soru (TRUE/FALSE/NOT GIVEN) |
| 5–6 | `GT1`, `GT2` tam testleri | her biri 11 soru (7 TFNG + 4 YES/NO/NOT GIVEN) |
| 7 | Alıştırma: TRUE / FALSE / NOT GIVEN | 15 soru |
| 8 | Alıştırma: YES / NO / NOT GIVEN | 15 soru |

**Toplam 50 + 30 = 80 soru.**

Oturum başında hangi paketin bittiğine bak, sıradaki bitmemişi yap. Hepsi bittiyse
"FABLE5-40 tamam" de ve çık.

---

## Neden bu dosya ayrı ve neden en güçlü model

Bu, bütün sınavın **en zor üretilen** soru tipi. Dil modelleri burada sistematik olarak
hata yapıyor: "FALSE" ile "NOT GIVEN" ayrımını karıştırıyorlar. Bu dosyanın tamamı o tek
hatayı önlemek için yazıldı. **Aşağıdaki üç adımlı testi her soru için uygula, atlama.**

## Önce oku

1. `content/PLAN-soru-dagilimi.md` — A, B, D bölümleri, telif ve kalite kuralları
2. İlgili pasajlar: `passages/academic/*.json` / `passages/general/*.json`
3. Format referansı — `referans/text/` (yoksa `.pdf` Read ile):
   - `ielts-academic-reading-computer-delivered-identifying-information-true-flase-not-given-answer-key.txt`
   - `ielts-general-training-reading-computer-delivered-identifying-information-true-false-not-given-answer-key.txt`
   - `ielts-academic-reading-sample-tasks-2023.txt` (yönerge kalıbı)

---

## İki ayrı soru tipi — karıştırma

| | `true_false_not_given` | `yes_no_not_given` |
|---|---|---|
| Neyi sorar | Metindeki **olgusal bilgiyi** | **Yazarın görüşünü / iddiasını** |
| Seçenekler | TRUE / FALSE / NOT GIVEN | YES / NO / NOT GIVEN |
| Kullanılabileceği pasaj | Her pasaj | Yazarın açık bir görüş belirttiği pasaj |
| Yönerge | `Do the following statements agree with the information given in the passage?` | `Do the following statements agree with the claims of the writer in the passage?` |

**YES/NO/NOT GIVEN için pasajda gerçekten yazar görüşü olmalı** — "araştırmacılar X buldu"
görüş değil, olgudur. "Bu bulgu, mevcut politikaların yetersiz olduğunu göstermektedir"
görüştür. Uygun pasaj yoksa o pasajı bu tip için kullanma.

## Yönerge kalıpları

```
Do the following statements agree with the information given in the passage?

In boxes 7-13 on your answer sheet, write

TRUE           if the statement agrees with the information
FALSE          if the statement contradicts the information
NOT GIVEN      if there is no information on this
```

```
Do the following statements agree with the claims of the writer in the passage?

In boxes 33-36 on your answer sheet, write

YES            if the statement agrees with the claims of the writer
NO             if the statement contradicts the claims of the writer
NOT GIVEN      if it is impossible to say what the writer thinks about this
```

Kutu numaralarını gerçek aralıkla yaz.

---

## 🔴 Üç adımlı test — HER soru için, istisnasız

Bir soru yazdıktan sonra kendi kendine şu üçünü sırayla uygula. Biri bile takılırsa
soruyu **at, düzeltmeye çalışma**.

### Adım 1 — Cevabı sen unut, pasajı yeniden oku

Soruyu bir aday gibi oku. Pasajda **sadece** ilgili yeri değil, **konuyla ilgili bütün
paragrafları** tara. Sonra üç şıktan hangisi olduğunu yeniden karar ver. İlk kararınla
aynı çıkmadıysa soru belirsizdir → at.

### Adım 2 — Şık gerekçesini yaz (zorunlu alan)

| Cevap | Yazman gereken |
|---|---|
| TRUE / YES | Pasajdaki **birebir cümle**. O cümle ifadeyi tek başına doğrulamalı — iki cümleyi birleştirip çıkarım yapman gerekiyorsa soru zayıftır, at |
| FALSE / NO | Pasajdaki **birebir cümle** + o cümlenin ifadeyle **hangi noktada çeliştiği**. Çelişki tek ve net bir noktada olmalı: sayı farkı, yön farkı (arttı/azaldı), olumsuzlama, özne farkı |
| NOT GIVEN | ⚠️ Aşağıdaki NOT GIVEN kontrolü |

### Adım 3 — NOT GIVEN kontrolü (en kritik)

NOT GIVEN yazacaksan üç şartın **üçünü birden** sağlamalısın:

1. **Konu pasajda geçiyor.** Tamamen alakasız bir ifade NOT GIVEN değil, kötü sorudur.
   İfade pasajın konusuyla ilgili olmalı, sadece o **belirli ayrıntı** bulunmamalı.
2. **Pasajda ifadeyi çürüten hiçbir cümle yok.** Varsa cevap FALSE'tur. Pasajın
   tamamını tarayarak doğrula, sadece ilgili paragrafa bakma.
3. **Pasajda ifadeyi doğrulayan hiçbir cümle yok** — dolaylı olarak bile.
   "Yazar bunu ima ediyor" diyebiliyorsan NOT GIVEN değildir.

Bu üçünü `not_given_justification` alanında **açıkça** yaz: konunun nerede geçtiği,
neyin söylenmediği, ve neden çelişki sayılmadığı.

### En sık yapılan iki hata — bunlara düşme

**Hata A: "Pasaj söylemiyorsa FALSE" sanmak.**
> Pasaj: "The survey covered 400 households in the city."
> İfade: "The survey covered rural households as well."
> ❌ FALSE değil. Pasaj kırsal hane olmadığını söylemiyor, sadece şehri söylüyor.
> ✅ NOT GIVEN.

**Hata B: Kıyas/derece ifadelerini NOT GIVEN sanmak.**
> Pasaj: "Method A took eleven days, while Method B was completed in four."
> İfade: "Method B was faster than Method A."
> ❌ NOT GIVEN değil. Sayılar doğrudan karşılaştırmayı veriyor.
> ✅ TRUE.

Kural: **Aritmetik ve doğrudan karşılaştırma çıkarım sayılmaz** (TRUE/FALSE olabilir).
**Sebep, niyet, genelleme, gelecek tahmini çıkarımdır** (yoksa NOT GIVEN'dır).

---

## Soru yazma kuralları

1. **Sıra kuralı mutlak.** Sorular pasajdaki geçiş sırasına göre dizilir. NOT GIVEN
   soruları için "geçiş yeri" = konunun ele alındığı yer.
2. **Cevap dağılımı.** Bir grupta üç şık da bulunsun, hiçbiri grubun yarısını geçmesin.
   7 soruluk grup için ideal: 3 TRUE, 2 FALSE, 2 NOT GIVEN (sıralaması karışık).
   **Ardışık üç soru aynı cevabı almasın.**
3. **İfade tek bir şeyi test etsin.** İki iddiayı birleştiren ifade ("X arttı ve Y azaldı")
   yasak — biri doğru biri yanlış olabilir.
4. **Birebir kopya yasak.** İfade pasajdaki cümlenin aynısı olamaz; eş anlamlı yeniden
   ifade şart. Ama **anlamı kaydırmadan** — abartı sıfat ekleme ("all", "never", "the most")
   ifadeyi teknik olarak yanlışlar, bu ucuz bir FALSE üretir; en fazla iki soruda kullan.
5. **İfadeler kısa olsun** — tek cümle, 20 kelimeyi geçmesin.
6. Cevaplar pasajın tamamına yayılsın.

---

## Çıktı JSON şeması

```json
{
  "schema_version": "1.0",
  "set_id": "AC1-true-false-not-given",
  "skill": "reading",
  "module": "academic",
  "test_id": "AC1",
  "practice": false,
  "passage_id": "A01",
  "question_type": "true_false_not_given",
  "generated_by": "fable",
  "instructions": "Do the following statements agree with the information given in the passage?\n\nIn boxes 7-13 on your answer sheet, write\n\nTRUE if the statement agrees with the information\nFALSE if the statement contradicts the information\nNOT GIVEN if there is no information on this",
  "options": ["TRUE", "FALSE", "NOT GIVEN"],
  "items": [
    {
      "number": 7,
      "prompt": "The ants rely on landmarks rather than counting when the ground is uneven.",
      "answer": ["FALSE"],
      "evidence": "Even across broken, rocky ground the ants continued to rely on step counting, ignoring nearby landmarks.",
      "evidence_locator": { "paragraph": "C", "sentence": 4 },
      "contradiction_point": "Pasaj engebeli zeminde de adım saymaya devam ettiklerini söylüyor; ifade tersini iddia ediyor.",
      "not_given_justification": null,
      "scan_note": "Yer işareti konusu B ve C paragraflarında geçiyor; ikisi de ifadeyi desteklemiyor.",
      "explanation": "Paragraf C, zemin engebeliyken bile karıncaların yer işaretlerini değil adım saymayı kullandığını söylüyor — ifade bunun tersi.",
      "difficulty": "medium"
    },
    {
      "number": 8,
      "prompt": "The species is found on more than one continent.",
      "answer": ["NOT GIVEN"],
      "evidence": null,
      "evidence_locator": null,
      "contradiction_point": null,
      "not_given_justification": "Pasaj türün yaşadığı ortamı (A ve B paragrafları, çöl) anlatıyor, yani konu geçiyor; ancak hangi kıtalarda bulunduğuna dair tek bir cümle yok. Dağılımı çürüten bir ifade de yok, dolayısıyla FALSE değil.",
      "scan_note": "Coğrafya A, B ve G paragraflarında geçiyor; hiçbirinde kıta bilgisi yok.",
      "explanation": "Pasaj türün çölde yaşadığını söylüyor ama kaç kıtada bulunduğundan hiç söz etmiyor.",
      "difficulty": "medium"
    }
  ]
}
```

| Alan | Kural |
|---|---|
| `evidence` | TRUE/FALSE'ta **zorunlu** ve birebir. NOT GIVEN'da `null` |
| `contradiction_point` | Sadece FALSE/NO'da dolu, çelişkinin tam noktasını Türkçe yaz |
| `not_given_justification` | Sadece NOT GIVEN'da dolu; üç şartı da açıklamalı. **Boş bırakılamaz** |
| `scan_note` | **Her soruda zorunlu.** Konunun pasajda geçtiği bütün paragrafları listele — Adım 1 taramasının kanıtı |
| `explanation` | **İngilizce**, 1–2 cümle, uygulamada gösterilecek |

`yes_no_not_given` için aynı şema; `options` `["YES","NO","NOT GIVEN"]`, `question_type`
`yes_no_not_given`, ve `evidence` **yazarın görüş cümlesi** olmalı.

---

## Dosya adları

| Paket | Dosya |
|---|---|
| AC1–AC4 (soru 7–13) | `content/reading/tests/AC1/true-false-not-given.json` |
| GT1–GT2 (soru 8–14) | `content/reading/tests/GT1/true-false-not-given.json` |
| GT1–GT2 (soru 33–36) | `content/reading/tests/GT1/yes-no-not-given.json` |
| Alıştırma TFNG (15) | `content/reading/practice/true-false-not-given.json` |
| Alıştırma YNNG (15) | `content/reading/practice/yes-no-not-given.json` |

Alıştırmalarda numaralar 1'den başlar, `test_id` `null`, `practice` `true`, her item'a
`passage_id` yaz. Bir pasajdan en fazla 4 alıştırma sorusu; tam testte kullanılan
cümleleri tekrar kullanma.

---

## Teslim öncesi kendi kontrol listen

- [ ] Soru sayısı ve numaraları planla birebir aynı
- [ ] Her soruda `scan_note` dolu
- [ ] Her NOT GIVEN sorusunda `not_given_justification` üç şartı da açıklıyor
- [ ] Her TRUE/FALSE sorusunda `evidence` pasajda birebir geçiyor (ara ve doğrula)
- [ ] Her FALSE sorusunda `contradiction_point` tek ve net bir noktayı gösteriyor
- [ ] Üç şık da grupta var, hiçbiri yarıyı geçmiyor, ardışık üç soru aynı cevap değil
- [ ] Hiçbir ifade iki iddiayı birleştirmiyor
- [ ] Hiçbir ifade pasaj cümlesinin birebir kopyası değil
- [ ] Aşırı genelleme ("all", "never") en fazla 2 soruda
- [ ] Cevapların pasajdaki sırası, soru sırasıyla aynı
- [ ] YES/NO/NOT GIVEN sorularında kanıt gerçekten **yazar görüşü** cümlesi
- [ ] JSON geçerli
- [ ] "IELTS" geçmiyor

**Son kontrol:** grubu baştan sona bir aday gibi çöz, kendi cevap anahtarına bakmadan.
Uyuşmayan soruyu sil ve yerine yenisini üret. Kaç soru elediğini `NOTLAR.md`'ye yaz.

---

## Bitirince

```
git add -A
git commit -m "okuma AC1: dogru-yanlis-verilmemis (7 soru)"
git pull --rebase
git push
```

**Kullanıcıya soru sorma.**
