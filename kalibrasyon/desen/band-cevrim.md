# Band çevrim tablosu — 2. çalıştırma

Tarih: 2026-08-08 · Kaynak prompt: `prompts/OPUS5-E4-cambridge-desen.md` (2/3)

Kaynak: arkadaşın diskindeki kendi (satın alınmış) gerçek sınav kitapları,
Cambridge IELTS 1–8. İnternetten **aranmadı, indirilmedi**;
`content/PLAN-soru-dagilimi.md` telif kuralı 3'ün dar istisnası uygulandı.
Bu dosyaya **yalnız sayı** girdi: tek bir pasaj/soru/seçenek/başlık/senaryo
cümlesi (parafrazı dahil) yok, çizelgeleri çevreleyen açıklama metni de yok.

---

## 🔴 Ana bulgu: bu kaynakta "kaç doğru = hangi band" tablosu YOK

8 kitabın tamamı bu soru için tarandı. Sonuç:

- **Cambridge IELTS 1:** puanlama çizelgesi hiç yok. (Metin katmanı olan tek
  kitap; tam metni programla arandı, çizelge deseni hiç geçmiyor.)
- **Cambridge IELTS 2–8:** her testin **her modülünün** cevap anahtarının
  sonunda, 40 soruyu **üç aralığa** bölen bir hazırlık çizelgesi var. Bu bir
  band (1–9) çevrim tablosu **değil**; üç kademeli bir "sınava hazır mısın"
  ölçütü: alt aralık = hazır değil, orta aralık = sınırda, üst aralık = hazır.

Yani prompt'un istediği anlamda bir band çevrim tablosu bu kaynaktan
**aktarılamaz — çünkü kaynakta yok.** Aktarılabilen tek sayısal çevrim ölçütü
bu üç aralığın **eşik noktalarıdır**; aşağıda tamamı verilmiştir.

🔴 **E6 (yeniden üretim) buradan band eşiği ALMAZ.** Depodaki band eşikleri
(`content/*/tests/*/_test.json` → `band_thresholds`, kaynak
`official_average_2023`) bu çalıştırmadan **etkilenmez**; aşağıdaki sayılar
yalnız karşılaştırma çapasıdır.

---

## Ne ölçüldü

Toplam **70 çizelge** okundu: 7 kitap (2–8) × (4 test × 2 modül + 2 GT okuma).
Her çizelgeden iki sayı alındı:

- **A** = orta aralığın başladığı doğru sayısı (alt aralık `0 … A-1`)
- **B** = üst aralığın başladığı doğru sayısı (orta aralık `A … B-1`,
  üst aralık `B … 40`)

Her sayı **iki kez, bağımsız olarak** okundu: önce sayfa görüntüsünden, sonra
yalnız çizelgenin sayı satırı kırpılıp kitap başına tek şeride dizilerek. 70
çizelgenin 70'i iki okumada da aynı çıktı; uyuşmazlık yok.

---

## Dinleme — eşikler (kitap × test)

Hücre biçimi: `alt aralık / orta aralık / üst aralık`

| Kitap | Test 1 | Test 2 | Test 3 | Test 4 |
|---|---|---|---|---|
| 2 | 0–18 / 19–25 / 26–40 | 0–16 / 17–25 / 26–40 | 0–17 / 18–25 / 26–40 | 0–18 / 19–26 / 27–40 |
| 3 | 0–17 / 18–27 / 28–40 | 0–17 / 18–27 / 28–40 | 0–14 / 15–25 / 26–40 | 0–15 / 16–26 / 27–40 |
| 4 | 0–14 / 15–30 / 31–40 | 0–13 / 14–28 / 29–40 | 0–12 / 13–27 / 28–40 | 0–12 / 13–27 / 28–40 |
| 5 | 0–13 / 14–28 / 29–40 | 0–12 / 13–27 / 28–40 | 0–13 / 14–28 / 29–40 | 0–12 / 13–27 / 28–40 |
| 6 | 0–12 / 13–26 / 27–40 | 0–13 / 14–28 / 29–40 | 0–12 / 13–27 / 28–40 | 0–12 / 13–27 / 28–40 |
| 7 | 0–11 / 12–27 / 28–40 | 0–11 / 12–27 / 28–40 | 0–11 / 12–27 / 28–40 | 0–11 / 12–27 / 28–40 |
| 8 | 0–14 / 15–29 / 30–40 | 0–13 / 14–27 / 28–40 | 0–13 / 14–28 / 29–40 | 0–11 / 12–27 / 28–40 |

## Academic okuma — eşikler (kitap × test)

| Kitap | Test 1 | Test 2 | Test 3 | Test 4 |
|---|---|---|---|---|
| 2 | 0–13 / 14–22 / 23–40 | 0–14 / 15–22 / 23–40 | 0–15 / 16–24 / 25–40 | 0–14 / 15–23 / 24–40 |
| 3 | 0–13 / 14–25 / 26–40 | 0–15 / 16–26 / 27–40 | 0–14 / 15–26 / 27–40 | 0–15 / 16–27 / 28–40 |
| 4 | 0–12 / 13–26 / 27–40 | 0–13 / 14–27 / 28–40 | 0–12 / 13–27 / 28–40 | 0–12 / 13–28 / 29–40 |
| 5 | 0–11 / 12–29 / 30–40 | 0–12 / 13–29 / 30–40 | 0–11 / 12–28 / 29–40 | 0–12 / 13–28 / 29–40 |
| 6 | 0–12 / 13–30 / 31–40 | 0–12 / 13–29 / 30–40 | 0–11 / 12–28 / 29–40 | 0–12 / 13–29 / 30–40 |
| 7 | 0–11 / 12–27 / 28–40 | 0–13 / 14–29 / 30–40 | 0–13 / 14–30 / 31–40 | 0–11 / 12–27 / 28–40 |
| 8 | 0–12 / 13–29 / 30–40 | 0–11 / 12–28 / 29–40 | 0–11 / 12–28 / 29–40 | 0–11 / 12–28 / 29–40 |

## General Training okuma — eşikler (kitap × GT testi)

| Kitap | GT Test A | GT Test B |
|---|---|---|
| 2 | 0–19 / 20–27 / 28–40 | 0–18 / 19–26 / 27–40 |
| 3 | 0–13 / 14–30 / 31–40 | 0–15 / 16–30 / 31–40 |
| 4 | 0–16 / 17–30 / 31–40 | 0–14 / 15–30 / 31–40 |
| 5 | 0–16 / 17–28 / 29–40 | 0–17 / 18–29 / 30–40 |
| 6 | 0–17 / 18–29 / 30–40 | 0–16 / 17–28 / 29–40 |
| 7 | 0–15 / 16–27 / 28–40 | 0–17 / 18–29 / 30–40 |
| 8 | 0–15 / 16–30 / 31–40 | 0–15 / 16–30 / 31–40 |

---

## Özet sayılar

| Modül | n | A ort. | A en az | A en çok | B ort. | B en az | B en çok |
|---|---|---|---|---|---|---|---|
| Dinleme | 28 | 14,46 | 12 | 19 | 27,96 | 26 | 31 |
| Academic okuma | 28 | 13,43 | 12 | 16 | 28,11 | 23 | 31 |
| GT okuma | 14 | 16,93 | 14 | 20 | 29,79 | 27 | 31 |

40 soruya oran olarak:

| Modül | A (%) | B (%) |
|---|---|---|
| Dinleme | %36,1 | %69,9 |
| Academic okuma | %33,6 | %70,3 |
| GT okuma | %42,3 | %74,5 |

### Kuşak farkı — sayı olarak var, dikkat

Kitap 2–3 ile kitap 4–8 arasında eşikler belirgin biçimde kayıyor:

| Modül | Kuşak | n | A ort. | B ort. |
|---|---|---|---|---|
| Dinleme | kitap 2–3 | 8 | 17,50 | 26,75 |
| Dinleme | kitap 4–8 | 20 | 13,25 | 28,45 |
| Academic okuma | kitap 2–3 | 8 | 15,12 | 25,38 |
| Academic okuma | kitap 4–8 | 20 | 12,75 | 29,20 |
| GT okuma | kitap 2–3 | 4 | 17,25 | 29,25 |
| GT okuma | kitap 4–8 | 10 | 16,80 | 30,00 |

Bu fark **testlerin zorluk farkı olarak okunamaz** — çizelge yayıncının
tavsiye eşiği; eski kitaplarda alt aralık geniş, üst aralık erken başlıyor,
yeni kitaplarda tam tersi. Yön bilgisi olarak kullanılabilir, büyüklük olarak
kullanılamaz. Daha güncel kuşak (4–8) daha temsili sayılmalı.

---

## Depodaki mevcut band eşikleriyle karşılaştırma (yalnız gözlem)

Depoda `content/*/tests/*/_test.json` içindeki `band_thresholds`
(`band_thresholds_source: "official_average_2023"`) ile kitapların **B** eşiği
(üst aralığın başlangıcı) yan yana konursa:

| Modül | Kitap B ort. | Depodaki eşikte hangi banda denk düşer |
|---|---|---|
| Dinleme | 27,96 | band 6,5 (26) ile band 7,0 (30) arası |
| Academic okuma | 28,11 | band 6,5 (27) ile band 7,0 (30) arası |
| GT okuma | 29,79 | band 6,0 (30) civarı |

**A** eşiği (alt aralığın bittiği yer) için: dinlemede 14,46 → depodaki band
4,5 (13) ile 5,0 (16) arası; Academic okumada 13,43 → band 4,5 (13) civarı;
GT okumada 16,93 → depodaki band 4,5 (19) eşiğinin altı.

Tek dikkat çeken sapma: kitaplarda GT ile Academic arasındaki ham fark **üst
eşikte yalnız +1,68 doğru** (29,79 − 28,11), depodaki tabloda ise aynı bantta
fark çok daha büyük (band 6,0'da GT 30 / AC 23 = +7 doğru; band 6,5'te 32 / 27
= +5). Yani kitapların ölçütü, GT okumanın Academic'e göre **daha küçük** bir
kaydırma gerektirdiğini söylüyor. Bu **bir karar değil, bir işaret**: örneklem
farklı (yayıncı tavsiyesi vs. resmî ortalama tablo) ve GT için n yalnız 14.
Depodaki eşikler bu dosya yüzünden değiştirilmedi.

---

## Okunan sayfalar (5. zorunlu kural)

Kitap hiçbir zaman baştan sona okunmadı. Önce giriş bölümünün "cevap anahtarı
kaç. sayfada" satırı, sonra yalnız cevap anahtarı sayfaları açıldı; çizelgenin
bulunduğu şerit çoğu sayfada programla kırpılıp yalnız o şerit okundu.

| Kitap | Okunan PDF sayfaları | Adet |
|---|---|---|
| 1 | (görüntü okunmadı; metin katmanı programla arandı) | 0 |
| 2 | 5, 6, 146–155, 159, 161 | 14 |
| 3 | 5, 6, 149–158 | 12 |
| 4 | 6, 148–157 | 11 |
| 5 | 6, 146–148, 150–159 | 14 |
| 6 | 149–158 | 10 |
| 7 | 153–162 | 10 |
| 8 | 3–5, 7, 8, 150–161 | 17 |
| **Toplam** | | **88** |

(Kitap 2/5'teki fazladan sayfalar, çizelge arama programının yanlış işaret
ettiği ve çizelge içermediği görülen sayfalardır.)

Depoya kitaptan hiçbir metin, hiçbir cevap anahtarı içeriği kopyalanmadı;
sayfa görüntüleri `.gitignore`'lu geçici klasörde üretildi ve iş bitince
silindi.

---

## Bir sonraki çalıştırmaya not

Kitaplar **erişilebilir durumda**: `C:\Users\enhar\Desktop\kitaplar\` altında
`Cambridge IELTS Book 1..8.pdf`. 1. çalıştırma (`test-yerlesimi.md`) "kaynak
bulunamadı" diye atlanmıştı; o karar artık geçersiz, 1. çalıştırma
tekrarlanabilir. Kitap 1 dışındakiler taranmış görüntüdür (metin katmanı yok),
sayfaları PNG'ye dökülerek okunmalıdır.

---

Bu sayılar hedef değil, karşılaştırma çapasıdır; örneklem küçükse büyüklüğü
değil yönü kullanılır.
