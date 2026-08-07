# ⚠️ MODEL: OPUS

Bu dosya **7 kez** çalıştırılır, elenen yuva sayısına göre bölünmüş:

| # | Kapsam |
|---|---|
| 1 | YES/NO/NOT GIVEN — tam testler |
| 2 | YES/NO/NOT GIVEN — alıştırma |
| 3 | Çoktan seçmeli — tam testler |
| 4 | Çoktan seçmeli — alıştırma |
| 5 | Cümle sonu eşleştirme + özellik eşleştirme |
| 6 | Tamamlama ailesi yuvaları |
| 7 | Kalanlar + tam test bütünlüğü kontrolü |

Hangi çalıştırma olduğun sana ek talimatta söylenir; söylenmiyorsa `content/DOGRULAMA/
yeniden-uretim-listesi.json`'daki henüz doldurulmamış ilk grubu yap.

---

## 🔴 Model bilerek Opus, Fable değil

Kusurlu desenin kaynağı `FABLE5-40` / `FABLE5-41` / `FABLE5-42` yuvalarıdır (kip imzası +
konumsal düzen). Aynı aileye tekrar yazdırmak aynı imzayı üretir — bu yüzden yeniden üretim
bilerek başka bir modelle yapılıyor.

---

## Ne yapıyoruz ve neden

`OPUS5-E5` bazı işaretli soruları elemeye karar verdi (konusu genel kültür olanlar) ve her
elenen yuva için `content/DOGRULAMA/yeniden-uretim-listesi.json` dosyasına ne aradığını,
neden elendiğini ve kaçınılması gereken kanıt cümlesini yazdı. Bu adım o yuvaları **aynı
sayıda, aynı numarayla** yeniden dolduruyor — ama bu sefer önceki üretimin somut kusurları
açıkça yasaklanmış bir talimatla.

Girdi:
- `content/DOGRULAMA/yeniden-uretim-listesi.json` (E5)
- `kalibrasyon/desen/test-yerlesimi.md` (E4 — oran/ölçüt, konu/cümle değil)
- İlgili pasajlar (`passages/`) — yeni soru aynı pasajdan, E5'in "kaçınılacak kanıt
  cümlesi/paragraf" listesine değmeyen bir yerden yazılır.

---

## 🔴 Zorunlu kurallar (her çalıştırmada)

1. **Sayıya güvenme, yeniden say.** `content/DOGRULAMA/yeniden-uretim-listesi.json`'daki
   `elenen` listesini kendi say; plandaki tahmini sayılar yön verir, hedef değildir.
2. **Hiçbir soru silinmez.** Bu adım zaten dolduruyor, silmiyor.
3. **Tam testlerde soru sayısı değişmez.** Her elenen yuva **aynı dosyaya, aynı numarayla**
   yazılır; test toplamı 40 kalır. Her çalıştırma bitiminde `python tools/dogrula.py`
   çalıştırıp "TAM TEST BÜTÜNLÜĞÜ" bölümünde ilgili testin hâlâ 40/40 olduğunu doğrula.
4. **Saklı küme koruması** — geçerli değil (puanlama dosyası açılmıyor).
5. **Token tasarrufu — hedefli okuma.** Yalnız kendi kapsamındaki elenen yuvaların pasajlarını
   aç; ilgisiz pasaj/dosyaları tarama.
6. 🔴 **Her çalıştırma depoda İZLENEN bir dosyayı değiştirip commit etmek zorunda.**

---

## 🔴 Yeni promptun açıkça yasakladığı, eski promptta olmayan iki kural

**Kip imzası yasağı.** Doğru cevap ile çeldiricinin kesinlik derecesi **eşleşecek.** Ölçülü
ifade (`may`, `probably`, `plausible`) yalnız doğru cevaba, mutlaklık (`clearly`, `only`,
`essential`, `no difference`) yalnız çeldiriciye ayrılamaz — ikisi de her iki tarafta da
görünebilmeli. Set bitince kip sayımı yap ve `NOTLAR.md`'ye yaz: doğru cevapların **en az
üçte biri** mutlak ifade taşımalı, çeldiricilerin **en az üçte biri** ölçülü ifade taşımalı.

**Konumsal düzen yasağı.** A ve G şıkları da doğru olabilecek (yalnız orta şıklar doğru
olmayacak diye bir kural yok); aynı harf çifti (ör. {C,F}) bir sette **ikiden fazla**
tekrarlanmayacak; "sınırlılık beyanı / hakem değerlendirmesi" tipi kapanış kalıbı **son
paragrafa demirlenmeyecek** (doğru cevap bazen ilk/orta paragraftan da gelmeli). Set bitince
harf dağılımını say, `NOTLAR.md`'ye yaz.

## Kendi kendini sınama (üretim bitmeden — zorunlu)

Her yeni soruyu, **pasajı kapatıp** yalnız soru + seçeneklerle kendin çöz. Bilebiliyorsan
soru daha depoya girmeden yeniden yazılır — depoya giren soru bu sınamayı geçmiş olmalı.

**Anlamca bilme de "bilinen" sayılır** (K3 ölçütü, `OPUS5-E10`'daki gibi) — kelime kelime
tutturmak şart değil, doğru kavramı anlamca çıkarabiliyorsan yine bilinen sayılır ve soru
yeniden yazılır. (E7 bunu bağımsız bir turda tekrar ölçecek; bu kendi kendini sınama ön
elemedir, E7'nin yerini tutmaz.)

## Yerleşim

Yeni soru elenen yuvanın **aynı dosyasına, aynı numarasıyla** yazılır (`number` alanı
değişmez). `answer`, `evidence`, `explanation`, `difficulty` alanları normal şemaya uygun
doldurulur. `status: "verified"`, `blind_solvable: null` (henüz ölçülmedi — E7 ölçecek).
`generated_by` alanına bu üretimi yapan modeli yaz (opus).

## Bitirince (her çalıştırmada)

```
git add -A
git commit -m "tukenen tiplerde yeniden uretim: YNNG tam testler (1/7)"
git pull --rebase
git push
```

**Kullanıcıya soru sorma. Hiçbir soruyu silme.**
