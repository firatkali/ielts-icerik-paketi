# İşaret Gerekçeleri — Mekanizmaya Göre Yeniden Yazım

Tarih: 2026-08-08 · Kaynak talimat: `prompts/SONNET5-E1-isaret-gerekceleri.md`

## Ne yapıldı

Denetim raporunun (`denetim/DENETIM-RAPORU.md` §5, madde A2) bulduğu kusur: işaretli
(`status: "flagged"`) 180 okuma sorusunun hepsinde birebir aynı `flag_reason` cümlesi
yazıyordu — "Parça gösterilmeden 3/3 turda doğru bilindi; genel kültürle çözülebiliyor."
Bu cümle 108 soruda gerçek mekanizmayla çelişiyordu.

Bu çalıştırmada `content/` altındaki bütün işaretli okuma soruları yeniden tarandı
(`grep -rl '"status": "flagged"'` ile 51 dosya bulundu, recursive JSON taramasıyla 180
işaretli soru sayıldı — denetim raporundaki 180 sayısı doğrulandı). Her sorunun
`blind_basis` alanına ve kendi `feature_check`/`heading_check`/`grammar_check`/
`distractor_analysis`/`not_given_justification`/`scan_note`/`uniqueness_check`/
`explanation` alanlarına bakılarak **kendine özgü** bir `flag_reason` yazıldı ve yeni
`flag_mechanism` alanı eklendi. Soru metni, `answer`, `evidence`, `status` ve
`blind_solvable` alanlarına dokunulmadı.

## Mekanizma × soru tipi dağılımı

| Soru tipi | genel_kultur | kip_imzasi | esdizim_kilidi | tanım_sızıntısı | konumsal_düzen | belirsiz | Toplam |
|---|---|---|---|---|---|---|---|
| flow_chart_completion | 2 | 0 | 1 | 0 | 0 | 1 | 4 |
| matching_features | 6 | 4 | 0 | 0 | 8 | 0 | 18 |
| matching_headings | 0 | 0 | 0 | 0 | 8 | 0 | 8 |
| matching_information | 0 | 0 | 0 | 0 | 2 | 1 | 3 |
| matching_sentence_endings | 0 | 0 | 0 | 0 | 10 | 0 | 10 |
| multiple_choice | 14 | 4 | 0 | 0 | 12 | 0 | 30 |
| note_completion | 4 | 0 | 4 | 0 | 0 | 1 | 9 |
| sentence_completion | 9 | 0 | 4 | 0 | 0 | 0 | 13 |
| short_answer | 2 | 0 | 0 | 0 | 0 | 0 | 2 |
| summary_completion | 6 | 0 | 10 | 2 | 5 | 3 | 26 |
| table_completion | 1 | 0 | 2 | 0 | 0 | 1 | 4 |
| true_false_not_given | 18 | 2 | 0 | 0 | 7 | 3 | 30 |
| yes_no_not_given | 9 | 2 | 0 | 0 | 12 | 0 | 23 |
| **Toplam** | **71** | **12** | **21** | **2** | **64** | **10** | **180** |

Not: `denetim/DENETIM-RAPORU.md` §3'teki iki desen bu dağılımda net görünüyor —
seçenek metinli tipler (`matching_features/headings/sentence_endings`, `multiple_choice`,
`true_false_not_given`, `yes_no_not_given`) ağırlıkla `konumsal_düzen` (elemeyle çözülme)
ve `kip_imzasi` (kesinlik/kalıp farkı) taşıyor; tamamlama ailesi
(`note/sentence/summary/table_completion`, `flow_chart_completion`) ağırlıkla
`eşdizim_kilidi` (kalıbın tahmin edilebilir ucu) taşıyor. `tanım_sızıntısı` yalnız
2 soruda kullanıldı — bu iki soruda boşluğun hemen ardından gelen açıklayıcı yan cümle
terimin tanımını doğrudan veriyordu (`AC3/summary-completion.json` #38 "microtubules",
`AC4/summary-completion.json` #36 "within-subject").

`blind_basis` → `flag_mechanism` eşlemesi, görev talimatındaki tabloya uyuyor
(iki `tanım_sızıntısı` durumu, tanım sızıntısı çok belirgin olduğu için bilinçli olarak
tablonun `general_knowledge`/`logic` varsayılan seçeneklerinin dışına çıkıldı):

| `blind_basis` | Kullanılan mekanizma(lar) | Soru sayısı |
|---|---|---|
| `general_knowledge` | genel_kultur (71) · tanım_sızıntısı (1) | 72 |
| `option_wording` | kip_imzasi (12) · konumsal_düzen (8) | 20 |
| `logic` | konumsal_düzen (56) · eşdizim_kilidi (21) · tanım_sızıntısı (1) | 78 |
| `guess` | belirsiz (10) | 10 |

## Örnekler

### genel_kultur (71 soru)
- `content/reading/practice/matching-features.json` #1 — "Cevap A (sade açık ofis)
  parçaya bakmadan da tahmin edilebiliyor: açık ofislerin öteki düzenlere göre daha
  gürültülü olduğu yaygın bir genel bilgi; soru dört düzenden en gürültülüsünü sorduğu
  için bu bilgiyle doğrudan A'ya varılabiliyor."
- `content/reading/practice/multiple-choice.json` #1 — "Cevap B, bilimsel deneylerde
  denekleri eşleştirirken en yaygın kullanılan ölçütün ağırlık olması genel bilgisiyle
  tahmin edilebiliyor; cinsiyet (A), toplanma mevsimi (C) ve komşuluk (D) daha az tipik
  eşleştirme ölçütleri, parçaya bakmadan da B en olası seçenek."
- `content/reading/tests/GT1/note-completion.json` #19 — "Cevap '28 days', Birleşik
  Krallık'ta tam zamanlı çalışanlar için yasal asgari yıllık izin hakkının (resmî
  tatiller dâhil) 28 gün olması bilinen bir iş hukuku gerçeği; bu genel bilgiyle boşluk
  parçaya bakmadan da doldurulabiliyor."

### kip_imzasi (12 soru)
- `content/reading/practice/multiple-choice.json` #3-4 — "Doğru seçenekler C ve F,
  'probably' ve 'cannot yet be excluded' gibi ölçülü/temkinli ifadeler taşıyor;
  çeldiriciler ise 'essential', 'nothing at all', 'sharpest results' gibi mutlak
  ifadeler kullanıyor — bu kesinlik derecesi farkı parçaya bakmadan da doğru ikiliyi
  ayırt ettiriyor."
- `content/reading/practice/yes-no-not-given.json` #3 — "İfadedeki 'clearly' (açıkça)
  mutlak zarfı, araştırma bulgularını aktaran ifadelerde sık sık abartı sinyali;
  'yıldız çalışan etkisi' araştırmalarında genelde beklenenin aksine sınırlı ya da sıfır
  etki bulunması bilgisiyle birlikte, ifadenin YANLIŞ olacağı parçaya bakmadan da
  tahmin edilebiliyor."
- `content/reading/tests/GT2/true-false-not-given.json` #13 — "İfadedeki 'most popular'
  (en popüler) üstünlük ifadesi, metnin çömlekçiliği yalnız elli dersten biri olarak
  andığı, hiçbir rağbet sıralaması vermediği bir yerde kurulmuş; bu tür mutlak
  dereceleme ifadeleri genelde NOT GIVEN'a işaret eder."

### eşdizim_kilidi (21 soru)
- `content/reading/practice/sentence-completion.json` #8 — "Boşluk 'a ___ of what is
  coming' kalıbının ucunda; bu kalıbın en doğal tamamlaması 'preview' olduğu için
  parçaya bakılmadan da tahmin edilebiliyor."
- `content/reading/tests/GT2/table-completion.json` #16 — "Boşluk 'an up-to-date ___'
  kalıbının ucunda; iş başvurularında bu kalıbın en doğal ve tek yaygın tamamlaması
  'CV' (özgeçmiş) olduğu için parçaya bakmadan da tahmin edilebiliyor."
- `content/reading/tests/AC4/summary-completion.json` #39 — "Boşluk '(39)___ rather
  than firm answers' karşıtlığına dayanıyor; 'rather than firm' ifadesi boşluğun kesin
  olmayan bir şey olduğunu işaret ediyor, kelime bankasındaki 'unproven suggestions' bu
  karşıtlığa tam oturuyor."

### tanım_sızıntısı (2 soru)
- `content/reading/tests/AC3/summary-completion.json` #38 — "Cevap 'microtubules',
  cümlenin kendisi boşluktan hemen sonra terimin tanımını veriyor ('the minute rods
  that support a cell from within'); bu tanım, terimi bilenler için doğrudan
  çağrıştırdığından parçaya bakmadan da tahmin edilebiliyor."
- `content/reading/tests/AC4/summary-completion.json` #36 — "Cevap J ('within-subject'),
  cümlenin kendisi boşluktan hemen sonra terimin tanımını veriyor ('the very same
  volunteers went through both...'); kelime bankasındaki karşıt terim C
  ('between-subjects') farklı katılımcıları gerektirdiği için bu tanımla çelişiyor."

### konumsal_düzen (64 soru)
- `content/reading/practice/matching-features.json` #9 — "Cevap E (kahve ve çay), beş
  seçenek arasında sıvı/içecek olan tek kategori; 'tartılmak yerine yazılı günlükle
  kaydedilme' ölçüm farkı sıvıları katı yiyeceklerden elemeyle ayırıyor — parçaya
  bakmadan da yalnız E bu ölçüm türüne uyuyor."
- `content/reading/practice/matching-headings.json` #11 — "Başlık 'i', seçenekler
  arasında elemeyle bulunuyor: en yakın çeldirici 'vii' konuca yakın duruyor ama
  paragraf saat ya da sınama ayrıntısı vermiyor — bu yüzden yalnız 'i' ana fikri tam
  karşılıyor."
- `content/reading/tests/AC2/multiple-choice.json` #33 — "Cevap D, mesajlaşma
  bulgusunun sorguladığı şeyi doğrudan veriyor: deneyimli takımların daha çok konuştuğu
  varsayımı; A, B, C metnin verdiği somut faydayla çelişip elenir."

### belirsiz (10 soru)
- `content/reading/practice/summary-completion.json` #5 — "Net bir mekanizma yok:
  boşluk 'green and ___' ikilisinin ikinci sıfatını istiyor, 'leafy' dışında 'lush',
  'dense', 'mature' gibi birçok seçenek de eşit derecede olası; doğru sözcüğün
  tutturulması büyük ölçüde şansa dayanıyor."
- `content/reading/tests/AC2/flow-chart-completion.json` #5 — "Net bir mekanizma yok:
  boşluk küçük iç uydular grubundaki sıra numarasını istiyor, bu sayı parçaya bakmadan
  tahmin edilemeyecek kadar spesifik; doğru sayının tutturulması şansa dayanıyor."
- `content/reading/tests/GT2/true-false-not-given.json` #14 — "Net bir mekanizma yok:
  geçerli kimlikli öğrencilere uygulanan indirim oranının ('%50') tam olarak
  ifadedeki 'half' ile eşleşmesi, parçaya bakmadan tahmin edilemeyecek somut bir sayı;
  doğruluğu büyük ölçüde şansa dayanıyor."

## Toplam sayı ve `belirsiz` oranı

- Yeniden sayılan işaretli soru: **180** (denetim raporundaki sayıyla aynı;
  `tools/dogrula.py` çıktısı da 180 gösteriyor).
- `belirsiz` sayılan soru: **10 / 180 (%5.6)** — eşiğin (%20) çok altında, bu adımda
  ek bir işlem gerekmiyor. Bu 10 soru gerçekten net bir dilbilgisel/anlamsal ipucu
  taşımıyor (çoğu tek sözcüklük boşluk doldurma ya da tek bir sayısal ayrıntı); E5'e
  devredilecek not: bu 10 soru için "elden geçirme" yerine muhtemelen **yeniden
  üretim** daha uygun olur, çünkü düzeltilecek belirgin bir kalıp yok.

## Doğrulama

```
python tools/dogrula.py
```
çıktısı: şema hatası 0, `isaretli (flagged) 180`, bütün tam testler (AC1-4, GT1-2,
L1-6) 40/40 tam. Soru metni/cevap/evidence hiçbir dosyada değişmedi.
