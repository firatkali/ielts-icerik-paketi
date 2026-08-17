# Capraz-kok taramasi (FAZ 0.2)

Tarih: 2026-08-18. Arac: `tools/capraz-kok.py` (temel: `tools/_e6_comp_capraz.py`).

Kapsam: okuma 60 paket / 391 kalem, dinleme 51 paket / 352 kalem (`content/reading/` + `content/listening/`, alistirma+test).

Esik (2. tur, kok cakismasi): aday dizgi en az **4 karakter** ve normalize edilmis metin uzerinde **kelime siniri** eslesmesi. Bu esik kisa/yaygin kelimelerde yanlis pozitif uretebilir; asagidaki sayilar HAM tarama sonucudur, elle goz gezdirme gerekir.

⚠️ `denetim/` altinda iCloud kopyasi bulundu (okunmadi/yazilmadi, sadece bilgi amacli listeleniyor): DENETIM-RAPORU 2.md, capraz-ozet 2.md, envanter 2.md


## Ozet sayilar

| tur | okuma | dinleme | toplam |
|---|---|---|---|
| 1. kanit cakismasi (paylasilan kanit sayisi) | 61 | 0 | 61 |
| 2. kok cakismasi (prompt<-cevap ciftleri) | 15 | 94 | 109 |
| 3. pasaj/senaryo paylasimi (paylasilan id sayisi) | 17 | 22 | 39 |

### Asil kanal: alistirma sorusu -> test cevabi

Kac alistirma sorusunun (kalem) gercekten bir test sorusunun cevabini prompt'unda tasidigi (yon: alistirma_cevabi -> test_prompt DEGIL, test_cevabi -> alistirma_prompt; yani alistirma prompt'u test cevabini sizdiriyor):

| okuma | dinleme | toplam |
|---|---|---|
| 7 | 14 | 21 |

### Kok cakismasi yon dagilimi

| yon (cevap_sahibi -> prompt_sahibi) | okuma | dinleme |
|---|---|---|
| alistirma_cevabi -> alistirma_prompt | 4 | 10 |
| alistirma_cevabi -> test_prompt | 1 | 18 |
| test_cevabi -> alistirma_prompt | 7 | 22 |
| test_cevabi -> test_prompt | 3 | 44 |

## En agir 10 cift (kok cakismasi, eslesme uzunluguna gore)

| skill | prompt (sizdiran) | havuz | cevap sahibi | havuz | sizan dizgi | uzunluk |
|---|---|---|---|---|---|---|
| reading | content/reading/practice/sentence-completion.json#7 | practice | content/reading/practice/short-answer.json#3 | practice | `six-month period` | 16 |
| reading | content/reading/practice/summary-completion.json#7 | practice | content/reading/tests/AC1/sentence-completion.json#22 | test | `fifteen minutes` | 15 |
| reading | content/reading/practice/yes-no-not-given.json#10 | practice | content/reading/tests/AC1/sentence-completion.json#22 | test | `fifteen minutes` | 15 |
| reading | content/reading/tests/AC3/true-false-not-given.json#13 | test | content/reading/practice/note-completion.json#5 | practice | `Monodontidae` | 12 |
| reading | content/reading/practice/true-false-not-given.json#10 | practice | content/reading/practice/note-completion.json#8 | practice | `12 December` | 11 |
| reading | content/reading/practice/true-false-not-given.json#9 | practice | content/reading/tests/AC3/sentence-completion.json#19 | test | `north-west` | 10 |
| reading | content/reading/tests/GT1/note-completion.json#15 | test | content/reading/tests/GT2/sentence-completion.json#27 | test | `four weeks` | 10 |
| reading | content/reading/practice/matching-sentence-endings.json#3 | practice | content/reading/tests/AC3/table-completion.json#3 | test | `cosmetic` | 8 |
| reading | content/reading/practice/summary-completion.json#11 | practice | content/reading/practice/sentence-completion.json#9 | practice | `a third` | 7 |
| reading | content/reading/practice/short-answer.json#1 | practice | content/reading/practice/summary-completion.json#7 | practice | `sharply` | 7 |

## Kok cakismasi detay — Okuma (ilk 30, tumu JSON'da)

| prompt (sizdiran) | havuz | cevap sahibi | havuz | sizan dizgi |
|---|---|---|---|---|
| content/reading/practice/sentence-completion.json#7 | practice | content/reading/practice/short-answer.json#3 | practice | `six-month period` |
| content/reading/practice/summary-completion.json#7 | practice | content/reading/tests/AC1/sentence-completion.json#22 | test | `fifteen minutes` |
| content/reading/practice/yes-no-not-given.json#10 | practice | content/reading/tests/AC1/sentence-completion.json#22 | test | `fifteen minutes` |
| content/reading/tests/AC3/true-false-not-given.json#13 | test | content/reading/practice/note-completion.json#5 | practice | `Monodontidae` |
| content/reading/practice/true-false-not-given.json#10 | practice | content/reading/practice/note-completion.json#8 | practice | `12 December` |
| content/reading/practice/true-false-not-given.json#9 | practice | content/reading/tests/AC3/sentence-completion.json#19 | test | `north-west` |
| content/reading/tests/GT1/note-completion.json#15 | test | content/reading/tests/GT2/sentence-completion.json#27 | test | `four weeks` |
| content/reading/practice/matching-sentence-endings.json#3 | practice | content/reading/tests/AC3/table-completion.json#3 | test | `cosmetic` |
| content/reading/practice/summary-completion.json#11 | practice | content/reading/practice/sentence-completion.json#9 | practice | `a third` |
| content/reading/practice/short-answer.json#1 | practice | content/reading/practice/summary-completion.json#7 | practice | `sharply` |
| content/reading/practice/true-false-not-given.json#4 | practice | content/reading/tests/AC1/note-completion.json#3 | test | `seventh` |
| content/reading/tests/AC1/sentence-completion.json#22 | test | content/reading/tests/AC1/note-completion.json#3 | test | `seventh` |
| content/reading/practice/matching-sentence-endings.json#1 | practice | content/reading/tests/AC3/table-completion.json#1 | test | `acrylic` |
| content/reading/tests/AC1/true-false-not-given.json#13 | test | content/reading/tests/AC1/note-completion.json#2 | test | `bamboo` |
| content/reading/practice/summary-completion.json#10 | practice | content/reading/tests/AC3/summary-completion.json#39 | test | `seven` |

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
| 3 | `Using a Latin square design, in which every team eventually experienced every condition bu` | matching-features.json#5(p), yes-no-not-given.json#5(p), note-completion.json#2(t), note-completion.json#3(t) |
| 4 | `The clearest effect of the entire study appeared on the Restorative Outcome Scale, which i` | summary-completion.json#7(p), yes-no-not-given.json#11(p), matching-features.json#23(t), matching-headings.json#18(t) |
| 3 | `The activity-based design, despite its popularity in contemporary office trends, performed` | matching-features.json#1(p), summary-completion.json#1(p), true-false-not-given.json#11(t) |
| 3 | `Employees in team offices reported flow scores 12 per cent higher than those in the open-p` | matching-features.json#4(p), summary-completion.json#2(p), yes-no-not-given.json#7(p) |
| 3 | `His success was not limited to the cube itself: when it was removed, he pushed a large tra` | matching-headings.json#3(p), note-completion.json#4(t), true-false-not-given.json#10(t) |
| 3 | `To reduce the grogginess that can follow a nap and distort test performance, all participa` | matching-headings.json#13(p), matching-information.json#27(t), summary-completion.json#36(t) |
| 3 | `These actions, described by the researchers as self-directed rather than social, appeared ` | matching-information.json#12(p), matching-sentence-endings.json#2(p), true-false-not-given.json#9(t) |
| 3 | `One plausible explanation is that volunteering pays off financially: it can widen a person` | matching-sentence-endings.json#9(p), matching-headings.json#30(t), yes-no-not-given.json#35(t) |
| 3 | `A ground survey carried out on 12 December confirmed what the satellite images had suggest` | multiple-choice.json#11(p), note-completion.json#8(p), matching-headings.json#16(t) |
| 3 | `In the forest condition, participants walked for five minutes to reach a stand of Norway s` | multiple-choice.json#13(p), matching-headings.json#15(t), sentence-completion.json#19(t) |
| 3 | `In the comparison condition, participants instead walked two minutes to a spot on campus w` | multiple-choice.json#14(p), yes-no-not-given.json#9(p), sentence-completion.json#20(t) |
| 3 | `Reversals of dominance, in which the previously subordinate animal became the stronger one` | true-false-not-given.json#4(p), matching-features.json#24(t), sentence-completion.json#21(t) |
| 3 | `Across these encounters a dominance hierarchy consistently emerged, with the stronger anim` | matching-features.json#25(t), matching-headings.json#16(t), sentence-completion.json#20(t) |
| 2 | `Recycling, including paper, glass and plastic bottles, is collected on alternate Thursdays` | diagram-labelling.json#2(p), matching-information.json#5(t) |
| 2 | `Helmets are not provided and riders are responsible for their own safety equipment.` | diagram-labelling.json#5(p), true-false-not-given.json#8(t) |
| 2 | `Provide their own reliable internet connection of at least 10 Mbps.` | diagram-labelling.json#9(p), sentence-completion.json#25(t) |
| 2 | `Rice and other cereals accounted for the single largest share of edible waste, at nearly 1` | matching-features.json#6(p), matching-headings.json#31(t) |
| 2 | `Discarded drinks were tracked separately: participants kept a seven-day diary noting the t` | matching-features.json#9(p), summary-completion.json#10(p) |
| 2 | `Beverages made up a smaller but still measurable part of the total: households poured away` | matching-features.json#10(p), matching-headings.json#32(t) |
| 2 | `There had been no earlier attempts to push, climb or stack anything nearby; the behaviour ` | matching-headings.json#2(p), true-false-not-given.json#9(t) |

(+41 kayit daha, `denetim/CAPRAZ-KOK.json` -> kanit_cakismasi.okuma)

## Kanit cakismasi detay — Dinleme (ilk 20, tumu JSON'da)

(yok)

## Pasaj/senaryo paylasimi detay — Okuma

| passage_id | alistirma kalem (paketler) | test kalem (paketler) |
|---|---|---|
| A11 | 14 (content/reading/practice/matching-information.json, content/reading/practice/multiple-choice.json, content/reading/practice/summary-completion.json, content/reading/practice/yes-no-not-given.json) | 13 (content/reading/tests/AC4/matching-features.json, content/reading/tests/AC4/matching-headings.json, content/reading/tests/AC4/sentence-completion.json) |
| A10 | 13 (content/reading/practice/matching-features.json, content/reading/practice/summary-completion.json, content/reading/practice/yes-no-not-given.json) | 13 (content/reading/tests/AC4/note-completion.json, content/reading/tests/AC4/true-false-not-given.json) |
| A07 | 12 (content/reading/practice/matching-information.json, content/reading/practice/matching-sentence-endings.json, content/reading/practice/note-completion.json) | 13 (content/reading/tests/AC3/table-completion.json, content/reading/tests/AC3/true-false-not-given.json) |
| A09 | 11 (content/reading/practice/matching-headings.json, content/reading/practice/note-completion.json, content/reading/practice/true-false-not-given.json) | 13 (content/reading/tests/AC3/matching-information.json, content/reading/tests/AC3/multiple-choice.json, content/reading/tests/AC3/summary-completion.json) |
| A12 | 11 (content/reading/practice/matching-headings.json, content/reading/practice/note-completion.json, content/reading/practice/yes-no-not-given.json) | 13 (content/reading/tests/AC4/matching-information.json, content/reading/tests/AC4/multiple-choice.json, content/reading/tests/AC4/summary-completion.json) |
| A08 | 10 (content/reading/practice/multiple-choice.json, content/reading/practice/note-completion.json, content/reading/practice/true-false-not-given.json) | 13 (content/reading/tests/AC3/matching-features.json, content/reading/tests/AC3/matching-headings.json, content/reading/tests/AC3/sentence-completion.json) |
| G05 | 9 (content/reading/practice/matching-features.json, content/reading/practice/summary-completion.json) | 13 (content/reading/tests/GT1/matching-headings.json, content/reading/tests/GT1/summary-completion.json, content/reading/tests/GT1/yes-no-not-given.json) |
| A01 | 9 (content/reading/practice/matching-headings.json, content/reading/practice/matching-information.json) | 13 (content/reading/tests/AC1/note-completion.json, content/reading/tests/AC1/true-false-not-given.json) |
| G06 | 8 (content/reading/practice/matching-sentence-endings.json, content/reading/practice/summary-completion.json) | 13 (content/reading/tests/GT2/matching-headings.json, content/reading/tests/GT2/summary-completion.json, content/reading/tests/GT2/yes-no-not-given.json) |
| A02 | 7 (content/reading/practice/multiple-choice.json, content/reading/practice/true-false-not-given.json) | 13 (content/reading/tests/AC1/matching-features.json, content/reading/tests/AC1/matching-headings.json, content/reading/tests/AC1/sentence-completion.json) |
| A05 | 7 (content/reading/practice/multiple-choice.json, content/reading/practice/true-false-not-given.json) | 13 (content/reading/tests/AC2/matching-features.json, content/reading/tests/AC2/matching-headings.json, content/reading/tests/AC2/sentence-completion.json) |
| A06 | 7 (content/reading/practice/note-completion.json, content/reading/practice/yes-no-not-given.json) | 13 (content/reading/tests/AC2/matching-information.json, content/reading/tests/AC2/multiple-choice.json, content/reading/tests/AC2/summary-completion.json) |
| G01 | 3 (content/reading/practice/diagram-labelling.json) | 14 (content/reading/tests/GT1/matching-information.json, content/reading/tests/GT1/true-false-not-given.json) |
| A04 | 4 (content/reading/practice/matching-information.json) | 13 (content/reading/tests/AC2/flow-chart-completion.json, content/reading/tests/AC2/true-false-not-given.json) |
| G02 | 2 (content/reading/practice/diagram-labelling.json) | 14 (content/reading/tests/GT2/matching-information.json, content/reading/tests/GT2/true-false-not-given.json) |
| G03 | 3 (content/reading/practice/diagram-labelling.json) | 12 (content/reading/tests/GT1/multiple-choice.json, content/reading/tests/GT1/note-completion.json, content/reading/tests/GT1/sentence-completion.json) |
| G04 | 2 (content/reading/practice/diagram-labelling.json) | 12 (content/reading/tests/GT2/multiple-choice.json, content/reading/tests/GT2/sentence-completion.json, content/reading/tests/GT2/table-completion.json) |

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
