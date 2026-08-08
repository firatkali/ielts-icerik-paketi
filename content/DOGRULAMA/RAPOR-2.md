# CAPRAZ-90/2 — Yeniden Ölçüm: Cevap Anahtarı Raporu

Kaynak talimat: `prompts/FABLE5-E7-yeniden-olcum.md` (1. çalıştırma).
`OPUS5-E5`'in düzelttiği ve `OPUS5-E6`'nın yeniden ürettiği sorular, üretmeyen model
tarafından kör olarak (cevap anahtarını görmeden) yeniden çözüldü; karşılaştırmayı
`tools/karsilastir.py` yaptı (`yeniden-olcum-cevap-anahtari.json`).

---

## E5/E6 sonrası değişen sorular — cevap anahtarı — 2026-08-08

- Doğrulayan model: **fable** (düzelten/yeniden üreten: opus — E5 ve E6'nın ikisi de Opus)
- Kapsam: `blind_solvable: null` bırakılmış **188 soru** (E5 düzeltmesi 116 + E6 yeni üretimi 72), 52 dosya
- Uyuşan: **184 (%97,9)** — içerik düzeyinde **186 (%98,9)**, iki uyuşmazlık birim/varyant yanlış alarmı
- İşaretlenen: **2** (`status: "flagged"` + `flag_reason` yazıldı; hiçbir soru silinmedi)

### Kapsam nasıl belirlendi

Talimatın 1. kuralı gereği sayıya güvenilmedi: E5'in sekiz ve E6'nın yedi commit'inin
dokunduğu dosyalar git'ten yeniden çıkarıldı, ölçüm hedefi ise dosya listesinden değil
alan durumundan alındı — E5/E6 elden geçirdiği her soruda `blind_solvable` alanını
`null` bırakmıştı (`tools/_e7_hedef_listesi.py`). Bu ölçüt 52 dosyada 188 soru verdi;
E5/E6'nın hiç dokunmadığı dosyaların (26 dinleme + 7 okuma) kör kopyaları açılmadan
silindi. Tip kırılımı:

| Soru tipi | E5 | E6 | Toplam |
|---|---|---|---|
| multiple_choice (yuva) | 16 | 14 | 30 |
| true_false_not_given | 26 | 3 | 29 |
| summary_completion | 21 | 8 | 29 |
| yes_no_not_given | 13 | 10 | 23 |
| sentence_completion | 4 | 17 | 21 |
| matching_features | 10 | 8 | 18 |
| matching_sentence_endings | 10 | 0 | 10 |
| matching_headings | 8 | 0 | 8 |
| note_completion | 4 | 4 | 8 |
| flow_chart_completion | 1 | 3 | 4 |
| short_answer | 0 | 3 | 3 |
| table_completion | 1 | 2 | 3 |
| matching_information | 2 | 0 | 2 |
| **toplam** | **116** | **72** | **188** |

Ölçümden önce `python tools/dogrula.py` koşuldu: on iki tam testin hepsi 40/40, şema
hatası 0 — E6'nın boş bıraktığı yuva yok, NOTLAR.md'ye devredilecek eksik çıkmadı.

### Kapsanan dosyalar

| Test | Dosyalar | Soru |
|---|---|---|
| AC1 | matching-features, multiple-choice, note-completion, sentence-completion, summary-completion, true-false-not-given | 17 |
| AC2 | flow-chart, matching-features, matching-headings, multiple-choice, sentence-completion, summary-completion, true-false-not-given | 23 |
| AC3 | matching-features, matching-headings, matching-information, multiple-choice, sentence-completion, summary-completion, table-completion, true-false-not-given | 17 |
| AC4 | matching-features, matching-headings, multiple-choice, note-completion, sentence-completion, summary-completion, true-false-not-given | 19 |
| GT1 | matching-headings, multiple-choice, note-completion, sentence-completion, summary-completion, true-false-not-given, yes-no-not-given | 19 |
| GT2 | multiple-choice, sentence-completion, summary-completion, table-completion, true-false-not-given, yes-no-not-given | 20 |
| alıştırma | on bir dosya (MC, TFNG, YNNG, MSE, MF, MH, MI, note, sentence, summary, short-answer) | 73 |
| **toplam** | **52 dosya** | **188** |

### İşaretlenen sorular

| Dosya | Soru | Orijinal | Doğrulayıcı | Güven | Gerekçe |
|---|---|---|---|---|---|
| content/reading/practice/matching-headings.json | 15 | v | ii | 3 | A12 F paragrafı için ii ("The internal make-up of the daytime naps") ve v ("What the length of the rest did not explain") **yalnız bu paragrafa** demirleniyor ve her biri paragrafın bir yarısını kapsıyor (bileşim / sonuçsuzluk). İlk turun raporundaki AC3/14 örüntüsünün aynısı: çeldirici başka paragrafa bağlanmıyor. ii'yi başka paragrafa demirlenebilir bir başlıkla değiştirmek soruyu tartışmasız yapar. |
| content/reading/tests/GT1/summary-completion.json | 40 | prevention | reductions | 4 | Kanıt cümlesi iki adayı birden taşıyor: "has focused on collection and disposal rather than **prevention**, and that meaningful **reductions** will depend on tackling the specific items". Özet kalıbı ("real ___ will depend on campaigns") pasajın "reductions will depend on" öbeğini neredeyse birebir yankılıyor; iki cevap da savunulabilir. En ucuz düzeltme `accepted_variants`'a "reductions" eklemek ya da boşluğu tek adaylı kalıba taşımak. |

İkisi de E5'in düzelttiği sorular; `status: "flagged"` yapıldı, silinmedi
(`tools/_e7_isaretle.py`). İşaretli sayısı 33 → **35**.

### Yanlış alarmlar (işaretlenmedi)

| Dosya | Soru | Orijinal | Doğrulayıcı | Durum |
|---|---|---|---|---|
| content/reading/practice/sentence-completion.json | 12 | 56,000 kilometres | 35,000 miles | `accepted_variants` "35,000 miles"ı **zaten içeriyor**; script yalnız `answer` alanına bakıyor. Düzeltme gerekmez. |
| content/reading/tests/AC2/flow-chart-completion.json | 3 | ten kilometres | six miles | `accepted_variants` "six miles"ı **zaten içeriyor**. Aynı script sınırlaması. |

E6'nın yeni sorularında varyant listeleri bu iki örnekte görevini yapmış; önceki
oturumların "rakam/yazı, mil/kilometre" dersinin uygulandığı görülüyor.

### Örüntü

- **E6'nın 72 yeni sorusunun 72'si de anahtarla uyuştu** (iki birim yanlış alarmı
  içerik düzeyinde uyuşma). Yeniden üretimde cevap anahtarı tutarlılığı sorunu
  görünmüyor; tek gerçek uyuşmazlık iki E5 düzeltmesinde çıktı ve ikisi de "yanlış
  cevap" değil, "**iki savunulabilir cevap**" türünden.
- **E5'in yeniden çapaladığı NOT GIVEN'lar gerçekten NOT GIVEN.** YNNG'de yeniden
  yazılan yokluk soruları (örn. GT1-36 hane seçimi, GT2-33 ülke×avantaj çaprazı,
  alıştırma 1/8/10/13) kör çözümde de pasajın karara bağlamadığı eksenlere düştü ve
  hepsi anahtarla uyuştu.
- **Kip dengelemesi cevabı bozmamış.** E5'in ölçülü/mutlak kip taşıdığı ifadelerde
  (alıştırma YNNG 3, 6, 7, 14; GT2-35, GT2-36) kanıt cümleleri yeni ifadeleri aynı
  netlikte doğruluyor ya da çürütüyor; hiçbirinde cevap kayması yok.
- **İki harfli çoktan seçmeli yuvaların altısı da uyuştu** ve cevap harfleri artık
  gerçekten dağılmış: A+E, C+F, B+F, A+D, C+G, B+G. E5 2. çalıştırmanın bıraktığı
  "C+F yığılması" E6 üretiminde kırılmış görünüyor (ölçümü 2. çalıştırmanın sızıntı
  turu ayrıca yapacak).
- **Sınıra en yakın uyuşan cevaplar** (ikinci turda bakılmaya aday): AC1 özet 40
  ("warning system" — üç kelimelik "early warning system"in İKİ KELİME sınırına
  sıkışması, güven 4), AC2 başlık 14 (iv/ix ikilemi, güven 4), AC3 başlık 14
  (ii/vii ikilemi ilk rapordan beri sürüyor, güven 4), alıştırma cümle tamamlama 8
  ("preview"/"warning system", güven 4), alıştırma YNNG 4 ("kabaca iki kat" ifadesinin
  26,2/8,6 ≈ 3 katı dışlaması NO'yu gerektiriyor, güven 4).

### 🔴 Yöntem notları

1. **`tools/kor-kopya.py`'de sızıntı bulundu ve kapatıldı.** E5/E6'nın eklediği
   `revision`, `yeniden_uretim`, `review_note`, `flag_mechanism`, `blind_basis` alanları
   silme listesinde olmadığı için kör kopyalara aynen geçiyordu ve yer yer **cevabı
   açık ediyordu** (örn. AC1 MF-26 revizyon notu "doğru cevap A'ya gidiyor", AC1 MC
   34-35 üretim notu "doğru harfler A ve E"). Alanlar `SIL` kümesine eklendi, kör
   kopyalar temiz sürümden yeniden üretildi. **Bu düzeltmeden önce yalnız AC1'in üç
   kör dosyası açılmıştı**; o dosyalardaki üç yuva (MF-26, MC-32, MC-34-35) için kör
   çözüm notlarına sözleşme gereği şerh düşüldü. 2. çalıştırma (sızıntı ölçümü) temiz
   kopyalarla çalışacak.
2. **ELDEN-GECIRME.md okuması kısmi kirlenme yarattı.** Talimat, kapsamı E5 raporundan
   çıkarmayı istiyor; raporun 1-3. bölümleri ise düzelttiği soruların cevaplarını
   tablolar hâlinde içeriyor. Bu yüzden YNNG düzeltmeleri, MSE'nin 10 sorusu ve iki
   harfli MC yuvalarının bir kısmı için doğrulayıcı, anahtar bilgisine ölçümden önce
   maruz kaldı; ilgili cevap dosyalarına tek tek şerh düşüldü ve çözümler yalnız pasaj
   kanıtıyla gerekçelendirildi. Kirlenen sorularda uyuşma zaten %100 çıktığı için oran
   yorumunu değiştirmiyor, ama **bu soruların cevap anahtarı doğrulaması "tam kör"
   sayılmamalı**. Sonraki E7 benzeri adımlar için öneri: kapsam, rapor gövdesinden
   değil commit dosya listelerinden + alan durumundan çıkarılmalı (bu çalıştırmada
   `_e7_hedef_listesi.py` tam da bunu yapıyor; rapor okuması yalnız teyit içindi).
3. Önceki oturum cevapları `kor-kopya.py`'nin yeni arşivleme davranışıyla
   `dogrulama/cevap-arsiv/20260808-101011/` altına kalktı; karşılaştırma temiz
   klasörle çalıştı (1-6. oturumların kronik karışıklığı bu kez yaşanmadı).

### Sonraki adım

2. çalıştırma (sızıntı): aynı 188 soru `tools/metinsiz-kopya.py` ile pasajsız çözülüp
3 bağımsız turla ölçülecek, `blind_solvable`/`blind_basis` alanları o ölçümün sonucuna
göre doldurulacak ve rapor `METINSIZ-RAPOR-2.md`'ye yazılacak. Bu çalıştırmada
`blind_solvable` alanlarına bilerek dokunulmadı.

Ek devir: **AC1 TFNG #11** bu kapsamın dışında kaldı (metni E5/E6'da değişmedi,
`blind_solvable` dolu) ama NOTLAR.md'deki E6 notu "guess gerekçesi duruyor, E7 yine de
ölçsün" diyor — 2. çalıştırmanın sızıntı turu bu soruyu kapsama almalı.
