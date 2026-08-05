# ⚠️ MODEL: SONNET

🔴 **Model burada bilerek Sonnet.** Uygulamada kullanıcının cevabını puanlayacak olan model bu.
Ölçümü daha güçlü bir modelle yaparsak ürünün gerçek davranışını değil, başka bir şeyi ölçmüş
oluruz. Bu adımda **asla model değiştirme.**

---

## Ne yapıyoruz ve neden

Elimizde, gerçek sınav görevlilerinin puanladığı örnek cevaplar var (`kalibrasyon/ornekler/`).
Doğru cevabı biliyoruz. Bu adım, **bizim değerlendirme talimatımızı** o örneklere uygulayıp
verdiği puanın gerçek puanla ne kadar tuttuğunu ölçüyor.

Ürünün tek satış vaadi "yazını okuyup band veriyorum". Bu ölçüm o vaadi doğrulayan tek iş.

---

## Tur yapısı

Bu dosya birden çok kez, **üç ayrı turda** çalıştırılır. Hangi turda olduğun sana ek talimatta
söylenir. Tur bilgisi gelmemişse `kalibrasyon/olcum/` klasörüne bak, hangi tur bitmiş gör,
sıradakini yap.

| Tur | Tekrar | Kullanılan talimat | Amaç |
|---|---|---|---|
| 1 | 3 | `degerlendirme/` ilk sürüm | Başlangıç sapması + modelin kendi tutarsızlığı |
| 2 | 1 | 1. düzeltmeden sonraki sürüm | Düzeltme işe yaradı mı |
| 3 (son) | 3 | 2. düzeltmeden sonraki sürüm | Son durum + saklı örnek kontrolü |

**Tekrar** = aynı cevabın aynı talimatla kaç kez puanlanacağı. Aynı cevaba farklı puan vermek
modelin kendi tutarsızlığıdır ve ayrıca ölçülür — kullanıcı üründe **tek** puan alıyor.

## Örnek kümeleri (dönüşümlü saklama)

Örnekler üç kümeye ayrılır: `S1`, `S2`, `S3`. Bölme **bir kez** yapılır ve
`kalibrasyon/olcum/kumeler.json` dosyasına yazılır; sonraki turlarda aynı bölme kullanılır.

Bölme kuralı: bandlar kümelere **dengeli** dağıtılsın (her kümede hem düşük hem yüksek band olsun),
konuşma ve yazma her kümede bulunsun. Yoksa küme karşılaştırması anlamsız olur.

Ölçümde **her turda bütün örnekler** puanlanır. Kümeler düzeltme adımında işe yarar: düzeltmeyi
yapan oturum bir kümeyi hiç görmez, o küme o turun **saklı** kümesidir.

---

## Adım 1 — Örnekleri oku

`kalibrasyon/ornekler/yazma/*.json` ve `kalibrasyon/ornekler/konusma/*.json`.

⚠️ `transcription_suspect: true` işaretli dosyaları **atla** ve raporda belirt — dökümü şüpheli
bir cevaptan çıkan sapma ölçüm değil gürültüdür.

## Adım 2 — Puanla

Her örnek için, **o beceriye ait değerlendirme talimatını** (`degerlendirme/` altındaki dosya)
aynen uygula. Talimatı bu oturumda **değiştirme, iyileştirme, tamamlama.** Ölçtüğümüz şey o
talimatın kendisi.

🔴 **Gerçek puanı görmeden puanla.** Örnek dosyasındaki `band` ve `examiner_comment` alanlarını
puanı verdikten sonra oku. Puanlarken göz ucuyla bile bakma — sınavın cevabını görüp sınava
girmiş olursun, ölçüm değersizleşir.

Konuşma örneklerinde `speech_rate_wpm` değerini talimatın istediği gibi hesaplayıp gir
(aday kelime sayısı ÷ konuşma süresi; süre yoksa dosyadaki değeri kullan, yoksa alanı boş bırak
ve raporda belirt).

Her puanlamayı şuraya yaz: `kalibrasyon/olcum/tur<N>/<örnek-kodu>-<tekrar-no>.json`

```json
{
  "sample": "AC-T1-1A-A",
  "round": 1,
  "repeat": 2,
  "predicted_band": 5.5,
  "criteria": [{ "name": "task_response", "band": 5.0 }],
  "output": { "<talimatın ürettiği tam çıktı>": "" }
}
```

## Adım 3 — Hesabı SCRIPT yapsın

Elle ortalama alma, elle sapma hesaplama.

```
python tools/puanlama-raporu.py 1
```

(sondaki sayı tur numarası). Script şunları basar ve `kalibrasyon/olcum/RAPOR-tur<N>.md`
dosyasına yazar:

- **ortalama mutlak fark** (bizim puan ↔ gerçek puan)
- **eğilim** — sürekli cömert mi cimri mi (işaretli ortalama fark)
- **en büyük sapma** ve hangi örnekte
- **tutarsızlık** — aynı cevaba verilen puanların yayılımı
- **tek seferlik dağılım** — ürünün gerçek davranışı bu; ortalama sadece tanı içindir
- beceri (yazma/konuşma), band aralığı ve küme bazında kırılım

## Başarı ölçütü

| Ölçü | Hedef |
|---|---|
| Ortalama mutlak fark | **< 0,5 band** |
| Tek bir örnekte sapma | **hiçbirinde ≥ 1,5 band olmayacak** |
| Eğilim (cömertlik/cimrilik) | **±0,25 band içinde** |
| Aynı cevaba verilen puanların yayılımı | ≤ 0,5 band |

## Adım 4 — Bitirince

`NOTLAR.md`'ye tek satır: tur numarası, kaç örnek puanlandı, ortalama mutlak fark, eğilim.
**Yorum yapma, talimatı düzeltme** — düzeltme ayrı bir adımın işi (sıra bozulursa ölçüm ile
düzeltme birbirine karışır).

```
git add -A
git commit -m "puanlama olcumu tur 1 (35 ornek x 3 tekrar)"
git pull --rebase
git push
```

**Kullanıcıya soru sorma.**
