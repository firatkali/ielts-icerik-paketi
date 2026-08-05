# ⚠️ MODEL: OPUS

Bu dosya **10 kez** çalıştırılır: 6 yazma + 4 konuşma.

🔴 **BAĞIMLILIK — bu adım, puanlama düzeltmesi bitmeden başlamaz.** Sebep: "band 8 böyle yazar"
diyen örnekler üretiyoruz, ama modelin band 8'i doğru bildiğinden emin olmadan üretirsek yanlış
etiketli örnek kütüphanesi kurmuş oluruz. Çalıştırıcı sırayı koruyor; sıra elle değiştirilirse
bu iş sessizce bozulur.

`degerlendirme/DEGISIKLIK-KAYDI.md` ve `kalibrasyon/olcum/SONUC.md` yoksa **çık** ve
`NOTLAR.md`'ye "puanlama ayarı bitmemiş" yaz.

---

## Ne yapıyoruz ve neden

Kullanıcı band 6 alıyor ve 7 istiyor. En işe yarar şey, aynı göreve verilmiş **band 7 cevabı**
görmek. Şu an içerikte yalnızca birkaç ifade ipucu var, tam cevap yok.

Her görev için üç seviyede tam örnek cevap üretiyoruz: **band 5 · 6,5 · 8**, her birinin altında
"neden bu band" açıklaması.

---

## Kapsam

| # | Ne | Kaç |
|---|---|---|
| 1-6 | Yazma görevleri | **30 görev × 3 seviye** = 90 cevap |
| 7-10 | Konuşma kartları | **20 kart × 3 seviye** = 60 cevap |

Görev seçimi: Academic Task 1 · Academic Task 2 · General Task 1 (mektup) · General Task 2
dengeli dağılsın. Konuşmada Part 2 kartları öncelikli.

Hepsine değil, örnekleme üretiliyor — talep görürse sonra genişletilir. Oturum başında
`content/ornek-cevaplar/` klasörüne bak, üretilmemiş ilk grubu yap.

---

## 🔴 Seviyeleri gerçekten ayır

En sık yapılan hata: üç cevabın da düzgün İngilizce olması, sadece uzunluğun değişmesi.
Band 5 cevabı **gerçekten band 5 olmalı** — hata içermeli.

| Band | Nasıl görünür |
|---|---|
| **5** | Sınırlı sözcük, tekrar; belirgin dilbilgisi hataları (tanımlık, zaman, çoğul) anlamı zorlaştırıyor; görevin bir kısmı eksik; bağlaçlar mekanik ("Firstly… Secondly…"); kelime sayısı sınırın ucunda |
| **6,5** | Görev karşılanıyor ama bazı noktalar yüzeysel; sözcük yeterli, ara ara yanlış eş anlamlı; hata var ama anlaşılmayı engellemiyor; bağlantı düzgün, akış biraz mekanik |
| **8** | Görev tam ve ayrıntılı; esnek ve doğal sözcük; cümle yapıları çeşitli, hata seyrek; fikirler kendiliğinden akıyor; **kusursuz değil** — band 9 değil |

Yazarken şu ölçütlere göre karar ver: görev yanıtı · tutarlılık · sözcük · dilbilgisi.
`degerlendirme/` altındaki **düzeltilmiş talimatı oku ve ona göre yaz** — böylece üretilen
örneklerle uygulamanın puanlaması aynı dili konuşur.

Konuşma cevapları **konuşma dilinde** olmalı: yarım cümleler, kendini düzeltme, doğal doldurma
sözcükleri. Yazılı cümleler dizisi konuşma örneği değildir.

## Çıktı

`content/ornek-cevaplar/writing/<gorev-kodu>.json`:

```json
{
  "exam": "ielts",
  "schema_version": "1.0",
  "kind": "model_answer_set",
  "skill": "writing",
  "task_ref": "AT01",
  "answers": [
    {
      "band": 5.0,
      "text": "<tam cevap>",
      "word_count": 156,
      "why_this_band": {
        "task_response": "≤2 cümle",
        "coherence_cohesion": "≤2 cümle",
        "lexical_resource": "≤2 cümle",
        "grammatical_range_accuracy": "≤2 cümle"
      },
      "what_would_lift_it": "≤2 cümle: bir üst banda çıkmak için ilk yapılacak şey"
    }
  ]
}
```

Konuşmada `criteria` üçlü olur (akıcılık · sözcük · dilbilgisi) ve `text` yerine `transcript`,
ayrıca `approx_duration_seconds` ve `word_count` yazılır — akıcılık hesabı konuşma hızından geliyor.

Kelime sayısı kurallara uymalı: Task 1 en az 150, Task 2 en az 250. **Band 5 örneği bile sınırın
altına düşmemeli**, yoksa düşüklüğün sebebi ölçüt değil eksik kelime olur.

## Kendi kendini denetle

Grubu bitirince, ürettiğin cevapları **band etiketlerini görmeden** kendin puanla (kısa bir
tabloya yaz). Verdiğin puan hedeflenen bandın 0,5'i içinde değilse o cevabı **yeniden yaz.**
Özellikle band 5 örneklerinde sık olur: farkında olmadan çok düzgün yazılır.

Sonucu `content/ornek-cevaplar/KONTROL.md`'ye ekle: görev · hedef band · kendi puanın · yeniden
yazıldı mı.

## Bitirince

```
git add -A
git commit -m "ornek cevaplar: academic task 1 (5 gorev x 3 seviye)"
git pull --rebase
git push
```

**Kullanıcıya soru sorma.**
