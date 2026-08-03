# ⚠️ MODEL: DOSYAYA GÖRE DEĞİŞİR — AŞAĞIDAKİ TABLOYA BAK

Bu doğrulamanın tek mantığı şu: **soruyu üreten model, soruyu doğrulayamaz.** Aynı model
aynı hatayı iki kez yapar. Bu yüzden her paketi **karşıt model** çözer.

Bu dosya **7 kez** çalıştırılır (her seferinde ayrı oturum):

| # | Çalıştırmadan önce yaz | Doğrulanacak paket | Üreteni |
|---|---|---|---|
| 1 | `/model opus` | Okuma — doğru/yanlış/verilmemiş + evet/hayır/verilmemiş | Fable |
| 2 | `/model opus` | Okuma — çoktan seçmeli | Fable |
| 3 | `/model opus` | Okuma — eşleştirme tipleri | Fable |
| 4 | `/model opus` | Dinleme — riskli sorular | Fable |
| 5 | `/model fable` | Okuma — tamamlama tipleri | Opus |
| 6 | `/model fable` | Okuma — bilgi eşleştirme | Opus |
| 7 | `/model fable` | Dinleme — güvenli sorular | Opus |

Oturum başında `content/DOGRULAMA/` klasörüne bak, hangi paketlerin bittiğini gör,
**sıradaki bitmemişi** yap. Yedisi de bittiyse "CAPRAZ-90 tamam" de ve çık.

---

## 🔴 EN ÖNEMLİ KURAL

**Bu oturumda cevap anahtarını GÖRMEYECEKSİN.**

Soru dosyalarını **Read aracıyla açma.** Onlara sadece aşağıdaki scriptler dokunur.
Cevapları görürsen doğrulama tamamen değersizleşir — üretenle aynı cevabı onaylarsın ve
hatalı sorular süzgeçten geçer.

Adımlar sırayla uygulanır, atlanmaz, sıra değiştirilmez.

---

## Adım 1 — Kör kopya üret (sen okumadan)

Aşağıdaki komutu çalıştır. Paket adlarını bu oturumun tablosundan al (birden çok paket
adını aynı komutta arka arkaya yazabilirsin).

```
python tools/kor-kopya.py true-false-not-given yes-no-not-given
```

Script `dogrulama/kor/` klasörüne cevapsız kopyaları yazar. Bu klasör `.gitignore`'da,
depoya gitmez.

Hiç dosya bulunmadıysa o paket henüz üretilmemiştir — `NOTLAR.md`'ye yaz ve çık.

**Paket adları** (komutun sonuna yazılacak):

| Oturum | Paket adları |
|---|---|
| 1 | `true-false-not-given`, `yes-no-not-given` |
| 2 | `multiple-choice` (okuma), `multiple-choice-multi` |
| 3 | `matching-headings`, `matching-features`, `matching-sentence-endings` |
| 4 | `multiple-choice` (dinleme), `matching` |
| 5 | `note-completion`, `table-completion`, `flow-chart-completion`, `summary-completion`, `sentence-completion`, `short-answer`, `diagram-labelling` |
| 6 | `matching-information` |
| 7 | `form-completion`, `plan-map-diagram-labelling` + dinlemedeki tamamlama dosyaları |

⚠️ 2. ve 4. oturumda dosya adı aynı (`multiple-choice`) — script hepsini bulur. Okuma ve
dinleme dosyalarını `skill` alanından ayırt et; **sadece kendi becerine ait olanları**
çöz, diğerlerini atla.

## Adım 2 — Kör dosyaları çöz

Şimdi `dogrulama/kor/` altındaki dosyaları Read ile aç. Her soru için:

1. İlgili kaynağı oku:
   - Okuma sorusu → `passages/academic/<id>.json` veya `passages/general/<id>.json`
   - Dinleme sorusu → `content/listening/scripts/<script_id>.json`
2. Soruyu **gerçek bir aday gibi** çöz. Yönergeye ve kelime sınırına uy.
3. Kararından ne kadar emin olduğunu 1–5 arası puanla (`confidence`).
4. Emin olamadığın sorularda **tahmin et ama düşük güven ver** — boş bırakma.

**Bu adımda karşılaştırma yapma.** Orijinal dosyaya bakma, "acaba doğru muyum" diye kontrol etme.

Cevaplarını şu biçimde `dogrulama/cevap/<kör-dosya-adıyla-aynı-ad>` olarak kaydet:

```json
{
  "_source": "content/reading/tests/AC1/true-false-not-given.json",
  "answers": [
    { "number": 7, "answer": ["FALSE"], "confidence": 5,
      "reasoning": "Paragraf C engebeli zeminde de adım saymaya devam ettiklerini söylüyor." },
    { "number": 8, "answer": ["NOT GIVEN"], "confidence": 3,
      "reasoning": "Kıta bilgisi hiç geçmiyor ama G paragrafındaki dağılım cümlesi ima ediyor olabilir." }
  ]
}
```

Alıştırma dosyalarında `groups` yapısı var — bütün kümelerdeki soruları düz bir liste
hâlinde `answers` içine yaz, `number` değerleri zaten benzersiz olmalı; değilse
`"group_id"` alanını da ekle.

## Adım 3 — Karşılaştırmayı SCRIPT yapsın

Elle karşılaştırma yapma. Bu komutu çalıştır (sondaki isim rapor dosyasının adı olur):

```
python tools/karsilastir.py true-false-not-given
```

Script şunu basar: kaç soru uyuştu, kaç tanesi sorunlu, uyuşma oranı, ve **hangi soruların
işaretlenmesi gerektiği**. Raporu `content/DOGRULAMA/<ad>.json` olarak kaydeder.

## Adım 4 — Sorunlu soruları işaretle

Uyuşmayan veya düşük güvenli her soruyu, **orijinal dosyasında** işaretle. **Silme.**
Silme kararını proje sahibi verecek (ikinci bir doğrulama daha yapılacak).

İlgili soru nesnesine iki alan ekle:

```json
"status": "flagged",
"flag_reason": "Çapraz doğrulamada NOT GIVEN yerine FALSE cevaplandı; G paragrafındaki dağılım cümlesi ifadeyi kısmen çürütüyor olabilir."
```

Sorunsuz sorulara `"status": "verified"` ekle.

Bu adımda artık orijinal dosyaları açman serbest (cevapların zaten kaydedildi).

## Adım 5 — Özet rapor yaz

`content/DOGRULAMA/RAPOR.md` dosyasına bu paketin bölümünü **ekle** (varsa üzerine yazma):

```markdown
## <paket adı> — <tarih>

- Doğrulayan model: opus (üreteni: fable)
- Toplam soru: 80
- Uyuşan: 71 (%88,8)
- İşaretlenen: 9

### İşaretlenen sorular
| Dosya | Soru | Orijinal | Doğrulayıcı | Güven | Kısa gerekçe |
|---|---|---|---|---|---|
| content/reading/tests/AC1/true-false-not-given.json | 8 | NOT GIVEN | FALSE | 4 | ... |

### Örüntü
<Bir soru tipinde sistematik hata var mı? Ör. "NOT GIVEN sorularının yarısı işaretlendi,
üretim promptundaki üç şartlı test yeterince uygulanmamış." Bu satır proje sahibi için
en değerli kısım — dürüst yaz.>
```

---

## Yorumlama ölçütü

| Uyuşma oranı | Ne demek |
|---|---|
| %95+ | İyi. İşaretlenenler tek tek bakılır |
| %85–95 | Kabul edilebilir. İşaretlenenlerin çoğu gerçekten belirsizdir |
| %85 altı | 🔴 Sistematik sorun var. Örüntüyü mutlaka yaz — o soru tipi yeniden üretilmeli |

Uyuşma oranı %85'in altındaysa `RAPOR.md`'de **büyük harfle** uyar.

---

## Bitirince

`NOTLAR.md` sonuna: hangi paket doğrulandı, hangi modelle, oran, işaretlenen sayısı.

```
git add -A
git commit -m "dogrulama: dogru-yanlis-verilmemis (80 soru, 9 isaretli)"
git pull --rebase
git push
```

**Kullanıcıya soru sorma. Hiçbir soruyu silme — sadece işaretle.**
