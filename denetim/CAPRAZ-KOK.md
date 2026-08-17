# Capraz-kok taramasi (FAZ 0.2)

Tarih: 2026-08-18. Arac: `tools/capraz-kok.py` (temel: `tools/_e6_comp_capraz.py`).

Kapsam: okuma 60 paket / 391 kalem, dinleme 51 paket / 352 kalem (`content/reading/` + `content/listening/`, alistirma+test).

Esik (2. tur, kok cakismasi): aday dizgi en az **4 karakter** ve normalize edilmis metin uzerinde **kelime siniri** eslesmesi. Bu esik kisa/yaygin kelimelerde yanlis pozitif uretebilir; asagidaki sayilar HAM tarama sonucudur, elle goz gezdirme gerekir.

⚠️ `denetim/` altinda iCloud kopyasi bulundu (okunmadi/yazilmadi, sadece bilgi amacli listeleniyor): DENETIM-RAPORU 2.md, capraz-ozet 2.md, envanter 2.md


## Ozet sayilar

| tur | okuma | dinleme | toplam |
|---|---|---|---|
| 1. kanit cakismasi (paylasilan kanit sayisi) | 12 | 0 | 12 |
| 2. kok cakismasi (prompt<-cevap ciftleri) | 5 | 94 | 99 |
| 3. pasaj/senaryo paylasimi (paylasilan id sayisi) | 0 | 22 | 22 |

### Asil kanal: alistirma sorusu -> test cevabi

Kac alistirma sorusunun (kalem) gercekten bir test sorusunun cevabini prompt'unda tasidigi (yon: alistirma_cevabi -> test_prompt DEGIL, test_cevabi -> alistirma_prompt; yani alistirma prompt'u test cevabini sizdiriyor):

| okuma | dinleme | toplam |
|---|---|---|
| 0 | 14 | 14 |

### Kok cakismasi yon dagilimi

| yon (cevap_sahibi -> prompt_sahibi) | okuma | dinleme |
|---|---|---|
| alistirma_cevabi -> alistirma_prompt | 0 | 10 |
| alistirma_cevabi -> test_prompt | 2 | 18 |
| test_cevabi -> alistirma_prompt | 0 | 22 |
| test_cevabi -> test_prompt | 3 | 44 |

## En agir 10 cift (kok cakismasi, eslesme uzunluguna gore)

| skill | prompt (sizdiran) | havuz | cevap sahibi | havuz | sizan dizgi | uzunluk |
|---|---|---|---|---|---|---|
| reading | content/reading/tests/AC1/sentence-completion.json#20 | test | content/reading/practice/note-completion.json#3 | practice | `three days` | 10 |
| reading | content/reading/tests/GT1/note-completion.json#15 | test | content/reading/tests/GT2/sentence-completion.json#27 | test | `four weeks` | 10 |
| reading | content/reading/tests/AC2/sentence-completion.json#22 | test | content/reading/practice/sentence-completion.json#7 | practice | `seventeen` | 9 |
| reading | content/reading/tests/AC1/sentence-completion.json#22 | test | content/reading/tests/AC1/note-completion.json#3 | test | `seventh` | 7 |
| reading | content/reading/tests/AC1/true-false-not-given.json#13 | test | content/reading/tests/AC1/note-completion.json#2 | test | `bamboo` | 6 |
| listening | content/listening/practice/table-completion.json#10 | practice | content/listening/tests/L1/note-completion.json#32 | test | `community gardens` | 17 |
| listening | content/listening/tests/L4/matching.json#13 | test | content/listening/tests/L4/plan-map-diagram-labelling.json#20 | test | `electrical store` | 16 |
| listening | content/listening/tests/L6/matching.json#12 | test | content/listening/tests/L6/plan-map-diagram-labelling.json#16 | test | `flower stall` | 12 |
| listening | content/listening/tests/L6/sentence-completion.json#28 | test | content/listening/practice/sentence-completion.json#7 | practice | `module page` | 11 |
| listening | content/listening/tests/L3/multiple-choice.json#22 | test | content/listening/practice/sentence-completion.json#9 | practice | `eight weeks` | 11 |

## Kok cakismasi detay — Okuma (ilk 30, tumu JSON'da)

| prompt (sizdiran) | havuz | cevap sahibi | havuz | sizan dizgi |
|---|---|---|---|---|
| content/reading/tests/AC1/sentence-completion.json#20 | test | content/reading/practice/note-completion.json#3 | practice | `three days` |
| content/reading/tests/GT1/note-completion.json#15 | test | content/reading/tests/GT2/sentence-completion.json#27 | test | `four weeks` |
| content/reading/tests/AC2/sentence-completion.json#22 | test | content/reading/practice/sentence-completion.json#7 | practice | `seventeen` |
| content/reading/tests/AC1/sentence-completion.json#22 | test | content/reading/tests/AC1/note-completion.json#3 | test | `seventh` |
| content/reading/tests/AC1/true-false-not-given.json#13 | test | content/reading/tests/AC1/note-completion.json#2 | test | `bamboo` |

## Kok cakismasi detay — Dinleme (ilk 30, tumu JSON'da)

| prompt (sizdiran) | havuz | cevap sahibi | havuz | sizan dizgi |
|---|---|---|---|---|
| content/listening/practice/table-completion.json#10 | practice | content/listening/tests/L1/note-completion.json#32 | test | `community gardens` |
| content/listening/tests/L4/matching.json#13 | test | content/listening/tests/L4/plan-map-diagram-labelling.json#20 | test | `electrical store` |
| content/listening/tests/L6/matching.json#12 | test | content/listening/tests/L6/plan-map-diagram-labelling.json#16 | test | `flower stall` |
| content/listening/tests/L6/sentence-completion.json#28 | test | content/listening/practice/sentence-completion.json#7 | practice | `module page` |
| content/listening/tests/L3/multiple-choice.json#22 | test | content/listening/practice/sentence-completion.json#9 | practice | `eight weeks` |
| content/listening/tests/L6/sentence-completion.json#28 | test | content/listening/tests/L1/sentence-completion.json#27 | test | `module page` |
| content/listening/tests/L5/plan-map-diagram-labelling.json#20 | test | content/listening/tests/L6/plan-map-diagram-labelling.json#20 | test | `cycle racks` |
| content/listening/practice/flow-chart-completion.json#5 | practice | content/listening/tests/L1/short-answer.json#39 | test | `5 per cent` |
| content/listening/practice/sentence-completion.json#15 | practice | content/listening/tests/L5/sentence-completion.json#29 | test | `study pods` |
| content/listening/tests/L4/note-completion.json#6 | test | content/listening/tests/L3/form-completion.json#9 | test | `telephone` |
| content/listening/practice/sentence-completion.json#4 | practice | content/listening/practice/flow-chart-completion.json#1 | practice | `separate` |
| content/listening/practice/flow-chart-completion.json#10 | practice | content/listening/practice/short-answer.json#12 | practice | `an hour` |
| content/listening/tests/L2/note-completion.json#39 | test | content/listening/practice/short-answer.json#12 | practice | `an hour` |
| content/listening/practice/flow-chart-completion.json#1 | practice | content/listening/practice/table-completion.json#13 | practice | `a fifth` |
| content/listening/tests/L2/table-completion.json#4 | test | content/listening/tests/L4/flow-chart-completion.json#40 | test | `bedroom` |
| content/listening/practice/flow-chart-completion.json#1 | practice | content/listening/tests/L5/table-completion.json#32 | test | `a fifth` |
| content/listening/tests/L4/flow-chart-completion.json#40 | test | content/listening/practice/flow-chart-completion.json#12 | practice | `window` |
| content/listening/tests/L6/summary-completion.json#37 | test | content/listening/practice/sentence-completion.json#11 | practice | `larger` |
| content/listening/tests/L2/table-completion.json#5 | test | content/listening/practice/table-completion.json#14 | practice | `Friday` |
| content/listening/tests/L2/table-completion.json#5 | test | content/listening/tests/L1/sentence-completion.json#29 | test | `Friday` |
| content/listening/tests/L1/matching.json#26 | test | content/listening/tests/L2/table-completion.json#5 | test | `second` |
| content/listening/tests/L2/multiple-choice.json#22 | test | content/listening/tests/L2/table-completion.json#5 | test | `second` |
| content/listening/tests/L5/sentence-completion.json#29 | test | content/listening/tests/L2/table-completion.json#5 | test | `second` |
| content/listening/tests/L6/matching.json#11 | test | content/listening/tests/L2/table-completion.json#5 | test | `second` |
| content/listening/tests/L6/form-completion.json#8 | test | content/listening/tests/L4/plan-map-diagram-labelling.json#16 | test | `office` |
| content/listening/tests/L6/form-completion.json#10 | test | content/listening/tests/L4/plan-map-diagram-labelling.json#16 | test | `office` |
| content/listening/tests/L2/table-completion.json#10 | test | content/listening/tests/L4/sentence-completion.json#30 | test | `frozen` |
| content/listening/tests/L3/short-answer.json#39 | test | content/listening/tests/L4/sentence-completion.json#30 | test | `frozen` |
| content/listening/tests/L3/short-answer.json#40 | test | content/listening/tests/L4/sentence-completion.json#30 | test | `frozen` |
| content/listening/practice/sentence-completion.json#9 | practice | content/listening/practice/flow-chart-completion.json#11 | practice | `three` |

(+64 kayit daha, `denetim/CAPRAZ-KOK.json` -> kok_cakismasi.dinleme)

## Kanit cakismasi detay — Okuma (ilk 20, tumu JSON'da)

| paket sayisi | kanit (ornek) | kalemler |
|---|---|---|
| 3 | `Across these encounters a dominance hierarchy consistently emerged, with the stronger anim` | matching-features.json#25(t), matching-headings.json#16(t), sentence-completion.json#20(t) |
| 2 | `Reversals of dominance, in which the previously subordinate animal became the stronger one` | matching-features.json#24(t), sentence-completion.json#21(t) |
| 2 | `The team deployed instruments to continuously record temperature, light, the partial press` | multiple-choice.json#34-35(t), summary-completion.json#37(t) |
| 2 | `His success was not limited to the cube itself: when it was removed, he pushed a large tra` | note-completion.json#4(t), true-false-not-given.json#10(t) |
| 2 | `To avoid contaminating the ancient samples with modern DNA, the extraction and analysis we` | matching-headings.json#16(t), sentence-completion.json#20(t) |
| 2 | `By comparing an image captured on 8 December, only two days after the earthquake, with a b` | matching-headings.json#15(t), sentence-completion.json#21(t) |
| 2 | `The clearest effect of the entire study appeared on the Restorative Outcome Scale, which i` | matching-features.json#23(t), matching-headings.json#18(t) |
| 2 | `In the forest condition, participants walked for five minutes to reach a stand of Norway s` | matching-headings.json#15(t), sentence-completion.json#19(t) |
| 2 | `To reduce the grogginess that can follow a nap and distort test performance, all participa` | matching-information.json#27(t), summary-completion.json#36(t) |
| 2 | `One plausible explanation is that volunteering pays off financially: it can widen a person` | matching-headings.json#30(t), yes-no-not-given.json#35(t) |
| 2 | `Income differences accounted for well under a fifth of the total association between volun` | matching-headings.json#31(t), summary-completion.json#37(t) |
| 2 | `Interns complete a short performance review at the five-week mark and a final review befor` | multiple-choice.json#21(t), table-completion.json#20(t) |

## Kanit cakismasi detay — Dinleme (ilk 20, tumu JSON'da)

(yok)

## Pasaj/senaryo paylasimi detay — Okuma

(yok)

## Pasaj/senaryo paylasimi detay — Dinleme

| script_id | alistirma kalem (paketler) | test kalem (paketler) |
|---|---|---|
| L4-S4 | 8 (content/listening/practice/flow-chart-completion.json, content/listening/practice/short-answer.json) | 10 (content/listening/tests/L4/flow-chart-completion.json, content/listening/tests/L4/short-answer.json) |
| L6-S2 | 8 (content/listening/practice/multiple-choice.json, content/listening/practice/plan-map-diagram-labelling.json) | 10 (content/listening/tests/L6/matching.json, content/listening/tests/L6/plan-map-diagram-labelling.json) |
| L2-S4 | 8 (content/listening/practice/note-completion.json, content/listening/practice/short-answer.json) | 10 (content/listening/tests/L2/flow-chart-completion.json, content/listening/tests/L2/note-completion.json) |
| L5-S4 | 7 (content/listening/practice/flow-chart-completion.json, content/listening/practice/short-answer.json) | 10 (content/listening/tests/L5/summary-completion.json, content/listening/tests/L5/table-completion.json) |
| L4-S3 | 7 (content/listening/practice/matching.json, content/listening/practice/sentence-completion.json) | 10 (content/listening/tests/L4/matching.json, content/listening/tests/L4/multiple-choice.json, content/listening/tests/L4/sentence-completion.json) |
| L5-S3 | 7 (content/listening/practice/matching.json, content/listening/practice/sentence-completion.json) | 10 (content/listening/tests/L5/matching.json, content/listening/tests/L5/multiple-choice.json, content/listening/tests/L5/sentence-completion.json) |
| L1-S4 | 7 (content/listening/practice/short-answer.json, content/listening/practice/table-completion.json) | 10 (content/listening/tests/L1/note-completion.json, content/listening/tests/L1/short-answer.json) |
| L6-S4 | 6 (content/listening/practice/flow-chart-completion.json, content/listening/practice/note-completion.json) | 10 (content/listening/tests/L6/note-completion.json, content/listening/tests/L6/summary-completion.json) |
| L4-S2 | 6 (content/listening/practice/multiple-choice-multi.json, content/listening/practice/plan-map-diagram-labelling.json) | 10 (content/listening/tests/L4/matching.json, content/listening/tests/L4/plan-map-diagram-labelling.json) |
| L3-S2 | 6 (content/listening/practice/multiple-choice.json, content/listening/practice/plan-map-diagram-labelling.json) | 10 (content/listening/tests/L3/matching.json, content/listening/tests/L3/plan-map-diagram-labelling.json) |
| L3-S4 | 4 (content/listening/practice/flow-chart-completion.json) | 10 (content/listening/tests/L3/short-answer.json, content/listening/tests/L3/summary-completion.json) |
| L1-S2 | 5 (content/listening/practice/multiple-choice-multi.json, content/listening/practice/plan-map-diagram-labelling.json) | 9 (content/listening/tests/L1/multiple-choice.json, content/listening/tests/L1/plan-map-diagram-labelling.json) |
| L1-S1 | 4 (content/listening/practice/note-completion.json) | 10 (content/listening/tests/L1/form-completion.json) |
| L5-S1 | 4 (content/listening/practice/note-completion.json) | 10 (content/listening/tests/L5/form-completion.json) |
| L2-S3 | 4 (content/listening/practice/sentence-completion.json) | 10 (content/listening/tests/L2/matching.json, content/listening/tests/L2/multiple-choice.json, content/listening/tests/L2/sentence-completion.json) |
| L3-S3 | 4 (content/listening/practice/sentence-completion.json) | 10 (content/listening/tests/L3/matching.json, content/listening/tests/L3/multiple-choice.json, content/listening/tests/L3/sentence-completion.json) |
| L6-S1 | 4 (content/listening/practice/table-completion.json) | 10 (content/listening/tests/L6/form-completion.json) |
| L4-S1 | 4 (content/listening/practice/table-completion.json) | 10 (content/listening/tests/L4/note-completion.json) |
| L3-S1 | 4 (content/listening/practice/table-completion.json) | 10 (content/listening/tests/L3/form-completion.json) |
| L1-S3 | 3 (content/listening/practice/matching.json) | 10 (content/listening/tests/L1/matching.json, content/listening/tests/L1/multiple-choice.json, content/listening/tests/L1/sentence-completion.json) |
| L5-S2 | 4 (content/listening/practice/multiple-choice.json) | 9 (content/listening/tests/L5/multiple-choice.json, content/listening/tests/L5/plan-map-diagram-labelling.json) |
| L6-S3 | 1 (content/listening/practice/multiple-choice-multi.json) | 10 (content/listening/tests/L6/matching.json, content/listening/tests/L6/multiple-choice.json, content/listening/tests/L6/sentence-completion.json) |

## Yontem notu

- Paket = tek bir icerik dosyasi (`content/reading/**/*.json`, `content/listening/**/*.json`); `ortak.soru_dosyalari()` scripts/, DOGRULAMA/, `_test.json` gibi soru-disi dosyalari zaten disliyor.
- `passage_id`/`script_id` item -> group -> set zinciriyle cozuluyor.
- Kanit cakismasi: `evidence` kucuk harf + noktalama sadelestirilip karsilastirildi.
- Kok cakismasi: `answer` + `accepted_variants` dizgileri (>=4 karakter, tekilleştirilmis) diger paketlerin `prompt` metninde kelime siniriyla araniyor; ayni pakette esleşme sayilmiyor.
- Bu arac hicbir icerik dosyasini degistirmedi; salt-okunur tarama.
