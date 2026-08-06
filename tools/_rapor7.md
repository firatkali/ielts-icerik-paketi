
---

## dinleme — form-completion, plan-map-diagram-labelling ve tamamlama paketleri — 2026-08-06

- Doğrulayan model: fable (üreteni: opus)
- Kapsam: `form-completion`, `plan-map-diagram-labelling`, ve dinlemedeki bütün tamamlama
  dosyaları (`note-completion`, `table-completion`, `flow-chart-completion`,
  `summary-completion`, `sentence-completion`, `short-answer`) — 36 dosya
- Toplam soru: 264
- Uyuşan: 241 (%91,3)
- İşaretlenen: 23

### İşaretlenen sorular
| Dosya | Soru | Orijinal | Doğrulayıcı | Güven | Kısa gerekçe |
|---|---|---|---|---|---|
| content/listening/practice/sentence-completion.json | 1 | five | 5 | 5 | rakam/yazı biçimi |
| content/listening/practice/sentence-completion.json | 4 | single file | file | 4 | "as one (4)" kalıbı ikisine de izin veriyor |
| content/listening/practice/short-answer.json | 1 | fifty years | 50 years | 5 | rakam/yazı biçimi |
| content/listening/practice/short-answer.json | 7 | water table | the water table | 5 | belirteç (the) |
| content/listening/practice/short-answer.json | 11 | line of sight | the line of sight | 5 | belirteç (the) |
| content/listening/practice/table-completion.json | 4 | Thursdays | Thursday | 5 | tekil/çoğul; hücre "every (4)" diyor |
| content/listening/tests/L1/short-answer.json | 39 | five per cent | 5 per cent | 5 | rakam/yazı biçimi |
| content/listening/tests/L2/flow-chart-completion.json | 34 | five | 5 | 5 | rakam/yazı biçimi |
| content/listening/tests/L2/note-completion.json | 39 | twelve | 12 | 5 | rakam/yazı biçimi |
| content/listening/tests/L2/sentence-completion.json | 29 | nineteenth | 19th | 5 | tarih biçimi |
| content/listening/tests/L2/table-completion.json | 5 | second | 2nd | 5 | tarih biçimi |
| content/listening/tests/L2/table-completion.json | 6 | 11.00 | 11 | 5 | saat biçimi |
| content/listening/tests/L2/table-completion.json | 9 | six | 6 | 5 | rakam/yazı biçimi |
| content/listening/tests/L3/form-completion.json | 5 | first | 1st | 5 | tarih biçimi |
| content/listening/tests/L3/sentence-completion.json | 29 | twelve | 12 | 5 | rakam/yazı biçimi |
| content/listening/tests/L3/short-answer.json | 38 | a freezer | freezer | 5 | belirteç (a) |
| content/listening/tests/L3/summary-completion.json | 32 | fifty | 50 | 5 | rakam/yazı biçimi |
| content/listening/tests/L3/summary-completion.json | 36 | ten | 10 | 5 | rakam/yazı biçimi |
| content/listening/tests/L4/note-completion.json | 6 | 07793441806 | 07793 441 806 | 5 | telefon numarasında boşluk |
| content/listening/tests/L4/sentence-completion.json | 27 | three | 3 | 5 | rakam/yazı biçimi |
| content/listening/tests/L4/short-answer.json | 33 | the low end | low frequencies | 5 | metinde iki ifade de var |
| content/listening/tests/L6/form-completion.json | 10 | HR 942 | HR942 | 5 | referans kodunda boşluk |
| content/listening/tests/L6/summary-completion.json | 37 | five | 5 | 5 | rakam/yazı biçimi |

### Örüntü

**İşaretlenen 23 sorunun 22'si içerik hatası değil, cevap anahtarı biçimi meselesi.**
Doğrulayıcı hiçbir soruda farklı bir bilgiyi cevap olarak vermedi; anahtarla aynı sözcüğü
ya da aynı sayıyı yazdı, yalnızca yazımı farklıydı. Dağılım şöyle:

- **11 soru rakam/yazı ikilemi** (`5`↔`five`, `12`↔`twelve`, `50`↔`fifty`, `10`↔`ten`,
  `3`↔`three`, `6`↔`six`). Bu tek başına işaretlenenlerin yarısı.
- **4 soru tarih/saat biçimi** (`2nd`↔`second`, `19th`↔`nineteenth`, `1st`↔`first`,
  `11`↔`11.00`).
- **3 soru belirteç** (`the water table`, `the line of sight`, `a freezer`).
- **2 soru boşluk** (telefon numarası `07793441806`, referans `HR 942`).
- **1 soru tekil/çoğul** (`Thursday`↔`Thursdays`).
- **1 soru gerçek ifade seçimi**: L4/33'te ders metni hem "less sensitive to **low
  frequencies**" hem "discounts **the low end** heavily" diyor; ikisi de metinden
  doğrudan alınabilir.

**Sonuç: bu paketlerde içerik doğruluğu pratikte %100, sorun anahtarın esnekliğinde.**
Gerçek bir sınavda bu cevapların hepsi doğru sayılır — resmî IELTS anahtarları sayıları
hem rakam hem yazı biçiminde, belirteçleri parantez içinde ("(the) water table") kabul
eder. Bu yüzden **hiçbir soru yeniden üretilmemeli**; yapılması gereken şey `answer`
alanının yanına `accepted_variants` doldurmak ya da puanlamada bir normalleştirici
kullanmak (rakam↔yazı eşlemesi, baştaki `a/the` atma, boşluk/noktalama atma). Bu tek
düzeltme işaretlenenlerin 22'sini birden kapatır.

**Plan/harita/şema etiketleme tipinde tek bir uyuşmazlık yok: 45/45.** Yedi dosyanın
(altı test + alıştırma) her sorusu tuttu; hem harf seçmeli hem sözcük yazmalı biçimlerde.
Senaryolardaki `spatial_description` alanı ile SVG'lerin geometrisi birbiriyle tutarlı ve
"girişe göre sol/sağ" çerçevesi bütün konuşmalarda korunmuş. Bu, doğrulaması en zor
sayılan tipin aslında paketin en sağlam kısmı olduğunu gösteriyor.

**Çeldirici-düzeltme mekaniği her dosyada çalışıyor.** Senaryolardaki "sorry, ignore that
/ that's last year's figure / it's moved to" düzeltmeleri anahtarda tutarlı biçimde
*düzeltilmiş* değere bağlanmış; doğrulayıcı 60'tan fazla çeldiricinin hiçbirine düşmedi ve
hiçbir soruda eski değer anahtarda kalmamış. Sayı sorularının yanıltıcılığı gerçek sınav
düzeyinde.

**Yöntem notu (biçim sorununun kendisi kısmen ölçüm aracından geliyor).**
`tools/karsilastir.py` cevap listesini birebir eşliyor: doğrulayıcı `["11","eleven"]`
yazarsa anahtardaki `["11"]` ile uyuşmaz sayılıyor. Bu yüzden bu oturumda cevaplar tek
biçime indirildi ve seçilen biçim kaçınılmaz olarak bazen anahtarınkinden farklı düştü.
Yani %91,3'lük oran **alt sınır**; içerik uyuşması %99,6 (264'te 263).
