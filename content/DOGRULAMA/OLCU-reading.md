# Sayısal ölçüler — okuma — 2026-08-07

⚠️ Bu ölçüler makul göstergedir, **kanıtlanmış zorluk ölçütü değildir**. B2 (sözcüksel örtüşme),
B3 (kanıt dağınıklığı), B4 (çeldirici yakınlığı) — `tools/olcu.py` ile hesaplandı, model kullanılmadı.

## Kapsam

- Ölçülen soru: **391** (14 tip), atlanan: **0**
- Çapa: resmî IELTS örnek görevlerinden (`referans/ielts-academic-reading-sample-tasks-2023.pdf`,
  `referans/ielts-general-reading-sample-tasks-2023.pdf`) elle çıkarılmış **116 soru-kanıt çifti**,
  13 tipte (`kalibrasyon/resmi-cift/`, 27 dosya — gitignore'lu, depoya girmedi).
- `yes_no_not_given` için resmî örnek belgede ayrı bir görev bulunamadı (belgeler yalnız
  "True/False/Not Given" örneği veriyor). Yapısal olarak aynı ölçüt ailesine ait olduğu için
  (`true_false_not_given` ile aynı `YARGI_TIPLERI` davranışı) o tipin çapası **yaklaşık değer**
  olarak `true_false_not_given` çapasıyla karşılaştırıldı, ayrı bir sapma kararına konu edilmedi.

## Tip bazında dağılım (sözcüksel örtüşme — soru cümlesi vs kaynak metin)

| Tip | Bizde (n) | Bizde ort. | Resmî çapa (n) | Resmî ort. | Fark |
|---|---|---|---|---|---|
| diagram_labelling | 10 | 0.504 | 5 | 0.467 | 0.037 |
| flow_chart_completion | 6 | 0.671 | 11 | 0.620 | 0.051 |
| matching_features | 26 | 0.498 | 11 | 0.568 | 0.070 |
| matching_headings | 45 | 0.022 | 11 | 0.409 | 🔴 0.387 |
| matching_information | 49 | 0.327 | 8 | 0.375 | 0.048 |
| matching_sentence_endings | 10 | 0.715 | 3 | 0.528 | 🔴 0.187 |
| multiple_choice | 30 | 0.601 | 6 | 0.444 | 🔴 0.157 |
| note_completion | 33 | 0.554 | 12 | 0.503 | 0.051 |
| sentence_completion | 37 | 0.472 | 8 | 0.626 | 🔴 0.154 |
| short_answer | 10 | 0.427 | 5 | 0.723 | 🔴 0.296 |
| summary_completion | 43 | 0.498 | 14 | 0.427 | 0.071 |
| table_completion | 12 | 0.488 | 5 | 0.670 | 🔴 0.182 |
| true_false_not_given | 57 | 0.631 | 17 | 0.574 | 0.057 |
| yes_no_not_given | 23 | 0.587 | (≈ tfng: 0.574) | — | bilgi amaçlı |

Eşik: ±0.10 (yüzde puanı). Kanıt dağınıklığı (kaç cümle) tiplerin çoğunda hem bizde hem
çapada 1.0 civarında — tamamlama tipleri (note/sentence/table/short-answer/flow-chart/
diagram) yapısal olarak tek cümleye dayanır, bu normal.

## 🔴 Çapadan ±%10 dışına çıkan tipler (gözden geçirilecek, silinmeyecek)

1. **matching_headings** — bizim havuzda başlık adaylarının kaynak metinle örtüşmesi
   neredeyse sıfır (%2.2) iken resmî örnekte %40.9. Ancak resmî çapa yalnız **tek pasajdan,
   11 soru** ile kurulu (küçük örneklem, muhtemelen o pasaja özgü sözcük tekrarı) — bu farkı
   tek başına "bizim başlıklarımız fazla zor" diye okumak yanıltıcı olur. Gözden geçirmede
   öncelik: daha geniş bir resmî örneklemle tekrar ölçmek.
2. **matching_sentence_endings** — bizde örtüşme (%71.5) resmîden (%52.8) belirgin yüksek;
   cümle sonu adayları kaynağa fazla yakın yazılmış olabilir (sahte-kolay risk).
3. **multiple_choice** — bizde (%60.1) resmîden (%44.4) yüksek; MC gövdeleri ortalamada
   biraz fazla metne yakın kurulmuş.
4. **sentence_completion** — bizde (%47.2) resmîden (%62.6) düşük; cümleler resmî örneklere
   göre daha fazla yeniden ifade edilmiş (bu, "zor" yönünde bir sapma — kötü değil ama
   resmî normdan uzak).
5. **short_answer** — bizde (%42.7) resmîden (%72.3) belirgin düşük; aynı yönde, sorular
   resmî örneklerden daha az birebir.
6. **table_completion** — bizde (%48.8) resmîden (%67.0) düşük; aynı yönde.

Not: (3) ve (4)-(5)-(6) zıt yönlerde sapıyor — MC/matching-sentence-endings havuzumuzda
resmîden daha "kolay" (fazla örtüşen), completion aile üyelerinin bir kısmı resmîden daha
"zor" (az örtüşen). Tek yönlü bir sistematik hata değil, tip bazlı incelenmeli.

## 🔴 Ölçüm sınırlaması: çeldirici yakınlığı (B4) harf/yargı tipli sorularda güvenilir değil

`distractor_distance` ölçüsü yanlış seçenek **metnini** kaynakla karşılaştırır. Ama
`matching_information`, `matching_headings`, `matching_features` gibi tiplerde "seçenek"
çoğu zaman düz bir paragraf harfidir (`"B"`, `"C"` …) — gerçek bir metin değil. Böyle tek
harfli "seçenekler" kaynak metinde paragraf etiketi olarak zaten geçtiği için (örn. "B Once
the finished newspaper…") ölçü yapay olarak 0.0 ya da 1.0'a doygunlaşıyor; içerik kalitesini
yansıtmıyor. Aynı durum `true_false_not_given` / `yes_no_not_given` için de geçerli — "TRUE",
"FALSE", "NOT GIVEN" birer yargı sözcüğü, metin parçası değil, o yüzden çeldirici ölçüsü
buralarda anlamsız (hem bizim havuzumuzda hem resmî çapada aynı yapay davranış var, ikisi de
etkilendiği için karşılaştırma taraflı değil ama tek başına yorumlanamaz).

Bu yüzden **çeldirici bazlı "uç örnek" listesi yalnız `multiple_choice` için** verildi
(orada seçenekler gerçek metin, ölçü güvenilir).

## Uç örnekler

**Örtüşmesi en yüksek 10 soru** (cevabın kelimeleri kaynakta neredeyse birebir geçiyor —
olası "kolay/sızıntılı" adaylar; sadece harf/yargı-dışı, gerçek anlam gerektiren tiplerden
seçildi):

| # | Dosya | Set | No | Tip | Cevap örtüşmesi | Durum |
|---|---|---|---|---|---|---|
| 1 | reading/practice/matching-headings.json | practice-matching-headings | 9 | matching_headings | 1.0 | 🔴 review işaretlendi |
| 2 | reading/tests/AC2/matching-features.json | AC2-matching-features | 26 | matching_features | 1.0 | zaten `flagged` (dokunulmadı) |
| 3 | reading/tests/GT1/matching-information.json | GT1-matching-information | 3 | matching_information | 1.0 | 🔴 review işaretlendi |
| 4 | reading/practice/multiple-choice.json | practice-multiple-choice | 7-8 | multiple_choice | 0.9 | zaten `flagged` |
| 5 | reading/practice/multiple-choice.json | practice-multiple-choice | 2 | multiple_choice | 0.875 | zaten `flagged` |
| 6 | reading/tests/AC1/multiple-choice.json | AC1-multiple-choice | 34-35 | multiple_choice | 0.833 | zaten `flagged` |
| 7 | reading/practice/multiple-choice.json | practice-multiple-choice | 14 | multiple_choice | 0.8 | zaten `flagged` |
| 8 | reading/tests/AC2/multiple-choice.json | AC2-multiple-choice | 32 | multiple_choice | 0.8 | zaten `flagged` |
| 9 | reading/tests/AC4/multiple-choice.json | AC4-multiple-choice | 34-35 | multiple_choice | 0.8 | zaten `flagged` |
| 10 | reading/tests/GT2/multiple-choice.json | GT2-multiple-choice | 22 | multiple_choice | 0.8 | zaten `flagged` |

**8/10'u önceki metinsiz-çözüm (kör-çözülebilirlik) turunda zaten `status: flagged` olarak
işaretlenmişti** — iki bağımsız yöntem (kör çözüm testi ve sözcüksel örtüşme ölçümü) aynı
soruları birbirinden habersiz şekilde işaret etti. Bu, ölçümün geçerliliği için iyi bir
çapraz doğrulama. O 8 soruya "status zaten flagged, üzerine yazma" kuralı gereği
dokunulmadı. Yalnız kalan **2 soruya** (`matching-headings.json` #9,
`GT1/matching-information.json` #3 — ikisi de `status: verified` idi) `difficulty_flags`
eklendi ve `status: review` yapıldı.

**Çeldiricisi metne hiç değmeyen sorular (`multiple_choice`, güvenilir ölçüm):** yok.
En düşük çeldirici mesafesi 0.283 (`practice-multiple-choice` #15) — resmî çapanın
minimumuna (0.10) yakın ama sıfıra hiç inmiyor. MC çeldiricileri genel olarak metinden tümüyle
kopuk değil.

## Atlanan soru sayısı ve sebebi

**0 soru atlandı.** `content/reading/**` altındaki 391 sorunun tamamı (kaynak metin + ölçülebilir
alan) bulundu; script hiçbirini "kaynak metin yok" ya da "ölçülebilir alan yok" diye elemedi.

## Kayıt

- `kalibrasyon/olcu/reading.json` — ham ölçüm (391 soru, 14 tip)
- `kalibrasyon/olcu/resmi.json` — resmî çapa ölçümü (116 soru, 13 tip)
- `kalibrasyon/resmi-cift/*.json` — çapa girdisi (27 dosya, **gitignore'lu, telifli metin
  içeriyor, depoya girmedi**)
- 2 soruya `difficulty_flags` + `status: review` eklendi (yukarıda listelendi)
