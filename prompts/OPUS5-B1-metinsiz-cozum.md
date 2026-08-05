# ⚠️ MODEL: OPUS

Bu dosya **8 kez** çalıştırılır. Her çalıştırmada okuma sorularının bir bölümü işlenir.

---

## Ne yapıyoruz ve neden

Bir okuma sorusu, **okuma parçasına bakmadan** cevaplanabiliyorsa o soru bozuktur: ya çeldiricileri
zayıftır ya da cevap genel kültürle bilinebilir. Gerçek sınavda böyle soru bulunmaz, çünkü sınav
metni anlamayı ölçer, aday ne biliyor onu değil.

Bu adım her soruyu **parçayı hiç göstermeden** çözdürüyor. Bilinen sorular işaretleniyor.

⚠️ Bu ölçü, soruların **bozuk** olanını bulur. "Bu soru gerçek sınav zorluğunda" demeyi
sağlamaz — öyle bir şey ancak binlerce gerçek adayın verisiyle söylenebilir. Rapor dilinde de
bu ayrım korunacak.

---

## 🔴 ÇAPA — mutlak eşik KOYMA

Aynı ölçüm resmî sınav sorularına da uygulandı. Sonuç: **resmî soruların %57'si de parçaya
bakmadan bilinebiliyor.** Yani "bilinen soru = kötü soru" kuralı toptan uygulanırsa kendi
havuzumuzun yarısını boşuna eleriz.

Karşılaştırma **soru tipi bazında** yapılır. Resmî tabandaki oranlar:

| Soru tipi | Resmî soruda parçasız bilinme |
|---|---|
| Not tamamlama | 6/6 |
| Özet tamamlama (listeden seçmeli) | 4/4 |
| Başlık eşleştirme | 4/4 |
| Doğru/Yanlış/Verilmemiş | 3/3 |
| Cümle sonu eşleştirme | 3/3 |
| Özellik eşleştirme | 3/4 |
| Cümle tamamlama | 1/5 |
| Özet tamamlama (metinden kelime) | 1/5 |
| Tablo tamamlama | 0/5 |
| Diyagram etiketleme | 0/5 |

⚠️ Bu taban **küçük bir örnekleme** dayanıyor (tip başına 3-6 soru). Kesin eşik değil, yön verir.
Bizim oranımız kendi tipinin tabanına **yakınsa** normal; **belirgin üstündeyse** o tip gözden
geçirilir.

---

## 🔴 EN ÖNEMLİ KURAL

**Bu oturumda ne okuma parçasını ne cevap anahtarını göreceksin.**

`passages/` klasörünü açma. Soru dosyalarını Read ile açma. Onlara sadece aşağıdaki script dokunur.
Parçayı bir kez okursan bu ölçüm tamamen değersizleşir ve bunu sonradan kimse fark edemez.

---

## Adım 1 — Parçasız kopya üret

```
python tools/metinsiz-kopya.py <paket-adi> [<paket-adi> ...]
```

Script `dogrulama/metinsiz/` klasörüne, parça ve cevap **olmadan** soru kopyaları yazar
(gitignore'da, depoya gitmez).

Çalıştırma listesi — sıradaki bitmemişi yap (`kalibrasyon/metinsiz/` klasörüne bak):

| # | Paketler |
|---|---|
| 1 | `true-false-not-given` |
| 2 | `yes-no-not-given`, `matching-headings` |
| 3 | `multiple-choice`, `multiple-choice-multi` (yalnız okuma) |
| 4 | `matching-features`, `matching-sentence-endings` |
| 5 | `matching-information` |
| 6 | `note-completion`, `table-completion` |
| 7 | `summary-completion`, `flow-chart-completion` |
| 8 | `sentence-completion`, `short-answer`, `diagram-labelling` |

## Adım 2 — Çöz (3 tur)

Her soruyu **üç kez ayrı ayrı** cevapla. Sebep: tek turda tutturulan cevap şans olabilir;
üçünde de tutturulmuşsa soru gerçekten parçasız bilinebiliyordur.

Her tur için: soruyu oku, elindeki genel bilgiyle en olası cevabı ver, **boş bırakma**, ve
kararının kaynağını söyle:

- `general_knowledge` — konuyu zaten biliyorum
- `option_wording` — seçeneklerin dili ele veriyor (biri fazla mutlak, biri fazla ayrıntılı…)
- `logic` — seçenekler birbirini dışlıyor, elemeyle çıkıyor
- `guess` — gerçekten tahmin

Çıktı: `kalibrasyon/metinsiz/<paket>-tur<N>.json`

```json
{ "answers": [ { "id": "AC1-tfng-7", "answer": ["TRUE"], "basis": "general_knowledge" } ] }
```

🔴 Turlar birbirinden bağımsız olmalı: 2. turu yaparken 1. turun cevaplarına bakma.

## Adım 3 — Karşılaştırmayı script yapsın

```
python tools/metinsiz-rapor.py <paket-adi>
```

Script cevapları anahtarla karşılaştırır, **3/3 turda bilinen** soruları çıkarır, tip bazında
oranı hesaplar ve resmî tabanla yan yana koyar. Raporu `content/DOGRULAMA/METINSIZ-<paket>.md`
olarak yazar.

## Adım 4 — İşaretle (silme)

3/3 turda bilinen her soruya, **orijinal dosyasında**:

```json
"blind_solvable": true,
"blind_basis": "general_knowledge",
"status": "flagged",
"flag_reason": "Parça gösterilmeden 3/3 turda doğru bilindi; genel kültürle çözülebiliyor."
```

Diğerlerine `"blind_solvable": false`.

🔴 **Hiçbir soruyu silme.** Bu adımda artık orijinal dosyaları açabilirsin (cevapların kaydedildi).

⚠️ **Diyagram etiketleme sorularını atla.** Onlar görsel gerektiriyor, metin tabanlı her ölçüm
orada kör; sonuç zorluğu değil görselin yokluğunu ölçer. Raporda "ölçülmedi" yaz.

## Adım 5 — Rapor

`content/DOGRULAMA/METINSIZ-RAPOR.md`'ye bu paketin bölümünü **ekle**:

- soru sayısı · 3/3 bilinen sayısı · oran
- **tip bazında** oran ve resmî taban
- 🔴 tabandan **belirgin sapan** tipler (ör. tablo tamamlamada resmî 0/5 iken bizde %60 →
  o tipin üretim promptu cevabı fazla açık ediyor demektir)
- `basis` dağılımı — `option_wording` yüksekse çeldirici yazımı zayıf, bu düzeltilebilir bir kusur

Son satır her zaman: **bu ölçüm bozuk soruyu bulur, zorluk seviyesini ölçmez.**

## Bitirince

```
git add -A
git commit -m "metinsiz cozum: true-false-not-given (80 soru, 11 isaretli)"
git pull --rebase
git push
```

⏭️ Dinleme soruları bu adımın **dışında** — aynı ölçü onlara da uygulanabilir ama okuma önce
gelir, kapsam bilerek dar tutuldu.

**Kullanıcıya soru sorma. Hiçbir soruyu silme.**
