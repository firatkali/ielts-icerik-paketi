# Parçasız çözüm ölçümü — toplu rapor

Her okuma sorusu, **okuma parçası ve cevap anahtarı hiç görülmeden** üç ayrı turda
cevaplandı. Üç turun üçünde de doğru bilinen soru "parçasız çözülebilir" sayıldı.

🔴 Bu ölçüm **bozuk soruyu** bulur, **zorluk seviyesini ölçmez.**

Karşılaştırma tabanı: aynı ölçüm resmî sınav sorularına uygulandığında **%57'si**
parçasız bilinebiliyordu. Bu yüzden mutlak eşik yok; her tip kendi resmî tabanıyla
karşılaştırılır. Resmî taban küçük örnekleme dayanır (tip başına 3-6 soru), kesin
eşik değil yön verir.

---

## 1 — true-false-not-given (2026-08-07)

- Ölçülen soru: **57** (7 dosya)
- Üç turun üçünde de parçasız bilinen: **30** — **%52.6**
- Üç turda aynı cevabın verildiği soru: 50/57 (%88) — turlar kararlı, sonuç şansa
  dayanmıyor.

### Tip bazında

| Soru tipi | Bizde | Oran | Resmî taban | Sapma |
|---|---|---|---|---|
| true_false_not_given | 30/57 | %53 | 3/3 (%100) | tabanın **altında** |

Bu pakette tek soru tipi var. Oranımız (%53) resmî tabanın (%100) belirgin
**altında**; ölçümün "belirgin üstünde" uyarısı bu tipte tetiklenmedi. Resmî taban
yalnız 3 soruya dayandığı için %100 rakamı gerçekçi bir tavan değil — asıl okunacak
sonuç, TFNG sorularımızın parçasız bilinme oranının genel resmî ortalamanın (%57)
biraz altında kalmasıdır.

### Set bazında dağılım

| Set | Soru | 3/3 bilinen | Oran |
|---|---|---|---|
| practice | 15 | 8 | %53 |
| AC1 | 7 | 6 | **%86** |
| AC2 | 7 | 4 | %57 |
| AC3 | 7 | 1 | %14 |
| AC4 | 7 | 2 | %29 |
| GT1 | 7 | 4 | %57 |
| GT2 | 7 | 5 | %71 |

🔴 **AC1 (6/7) ve GT2 (5/7)** bu paketin zayıf halkaları. AC1'de konu genel kültürde
çok bilinen bir vaka; parçaya bakmadan doğru bilinen 6 sorunun 5'i `general_knowledge`
ile geldi. GT2'de ise ifadeler günlük hayatın varsayılan kuralıyla örtüşüyor (ilan
metinlerinde beklenen: erken bilet daha ucuz, yazılı uyarı verilir), yani soru
parçadan değil hayat bilgisinden çözülebiliyor.

AC3 (%14) ve AC4 (%29) tersi yönde iyi örnek: ifadeler parçanın kendi ayrıntısına
bağlı, dışarıdan bilinemiyor.

### Cevap anahtarına göre dağılım

| Anahtar | Toplam | 3/3 bilinen | Oran |
|---|---|---|---|
| TRUE | 24 | 15 | %63 |
| FALSE | 17 | 8 | %47 |
| NOT GIVEN | 16 | 7 | %44 |

TRUE cevaplı sorular en kolay tahmin edilenler — beklenen bir sonuç, çünkü doğru
ifade genellikle dünyaya dair makul olanla örtüşür. Uçurum büyük değil; NOT GIVEN
ve FALSE ayrımı parçasız yapılamıyor, bu iyi işaret.

### `basis` dağılımı

Üç turun tamamı (171 cevap):

| Dayanak | Tüm cevaplar | Yalnız işaretli sorularda (90 cevap) |
|---|---|---|
| general_knowledge | 78 (%46) | 54 (%60) |
| logic | 47 (%27) | 21 (%23) |
| guess | 37 (%22) | 9 (%10) |
| option_wording | 9 (%5) | 6 (%7) |

`option_wording` düşük (%5–7). Yani sorular **çeldirici yazımından** ele vermiyor;
ifadeler "fazla mutlak / fazla ayrıntılı" gibi biçimsel ipucu taşımıyor. Bu, düzeltmesi
en zor kusurun bu havuzda küçük olduğu anlamına gelir.

İşaretli soruların baskın dayanağı `general_knowledge` (%60). Bu düzeltilebilir bir
kusur değil, **konu seçimiyle** ilgili: ünlü vakalar (AC1) ve gündelik hizmet
ilanları (GT2) doğal olarak dışarıdan bilinir. Düzeltme yolu, ifadeyi parçanın
kendine özgü sayısal/koşullu ayrıntısına bağlamaktır.

### Ölçülmeyenler

Diyagram etiketleme bu pakette yok. Görsel gerektiren tiplerde metin tabanlı bu ölçüm
kördür ve o tipler geldiğinde **"ölçülmedi"** olarak geçilecektir.

### Yapılan işaretleme

30 soruya orijinal dosyasında `blind_solvable: true`, `blind_basis`, `status: "flagged"`
ve `flag_reason` yazıldı. Kalan 27 soruya `blind_solvable: false`. **Hiçbir soru
silinmedi**, soru sayısı 57'de sabit.

---

🔴 Son söz: **bu ölçüm bozuk soruyu bulur, zorluk seviyesini ölçmez.** "Bu soru gerçek
sınav zorluğunda" demek ancak binlerce gerçek adayın verisiyle mümkündür.
