# ⚠️ MODEL: OPUS

Bu dosya **3 kez** çalıştırılır: 1) test yerleşimi deseni · 2) band çevrim tablosu ·
3) puanlı örnek envanteri. Hangi çalıştırma olduğun sana ek talimatta söylenir; söylenmiyorsa
`kalibrasyon/desen/` klasörüne bak, hangisi eksikse onu yap.

---

## 🔴🔴🔴 TELİF SINIRI — bu dosyanın en hassas kuralı, önce bunu oku

`content/PLAN-soru-dagilimi.md`'nin telif kuralı 3'ü Cambridge IELTS kitaplarını "aranmaz,
indirilmez, kullanılmaz" diye yasaklıyor. **Bu adım o kuralın dar bir istisnasıdır** ve
istisna şudur:

- Kitaplar **arkadaşın diskindeki kendi kopyasıdır** (satın alınmış, yasal). Bu depo onlara
  internetten erişmiyor, indirmiyor, aramıyor.
- Bu çalıştırmalarda kitaplardan çıkarılan **tek şey sayısal desen ve ölçüttür**: bir testte
  kaç soru hangi tipten, cevap dağılımı ne, kaç doğru hangi banda denk geliyor, puanlı örnek
  var mı.

**Depoya giren dosyalarda şunlardan TEK BİRİ bile bulunamaz:** bir pasaj cümlesi, bir soru
metni, bir seçenek metni, bir başlık listesi, bir senaryo replası — bunların **parafrazı da
dahil.** İhlal projeyi bitirir; depo public.

🔴 **Kitaptan gelen desen soru üretiminde içerik kaynağı değildir.** E6 (yeniden üretim) bu
çalıştırmanın çıktısından yalnız **oran/ölçüt** alır, konu/cümle/senaryo almaz.

Kitaplar diskte yoksa: ilgili çıktı dosyasına "kaynak bulunamadı, bu çalıştırma atlandı" yaz,
sebebi `NOTLAR.md`'ye de yaz, commit et, çık (aşağıdaki 6. zorunlu kural).

---

## Ne yapıyoruz ve neden

Bugüne kadarki bütün desen bilgisi (soru tipi dağılımı, "kaç doğru = hangi band") resmî IELTS
web sitesindeki küçük örneklem belgelerinden geliyor (`referans/`). Bu, E5/E6/E9'daki
düzeltme ve yeniden üretim kararlarını **küçük bir örneklemle** almak zorunda bırakıyor.
Gerçek sınav kitapları çok daha büyük bir örneklem sunuyor. Bu adım o örneklemden **yalnız
sayıları** çıkarıp bir karşılaştırma çapası kuruyor — kitap içeriğinin kendisi asla depoya
girmez.

**Bu adım karar vermez, ölçüt yazar.** Sonuç dosyalarının sonunda her zaman şu cümle bulunur:
bu sayılar hedef değil, karşılaştırma çapasıdır; örneklem küçükse büyüklüğü değil yönü
kullanılır.

---

## 🔴 Zorunlu kurallar (her çalıştırmada)

1. **Sayıya güvenme, yeniden say.** Bu çalıştırma kitaptan sayı çıkarıyor; kendi saydığın
   sayıları iki kez kontrol et, tahmin etme.
2. **Hiçbir soru silinmez.** Bu adım soru üretmiyor/silmiyor.
3. **Tam testlerde soru sayısı değişmez.** Etkilenmez.
4. **Saklı küme koruması** — geçerli değil (puanlama dosyası açılmıyor), ama 3. çalıştırmada
   üretilecek konuşma/yazma örnekleri **puanlama kalibrasyonu için ayrılıyor** — bkz. aşağıda.
5. **Token tasarrufu — hedefli okuma.** Önce kitabın içindekiler/dizin sayfası, sonra yalnız
   cevap anahtarı sayfaları ve gerekli görev sayfaları. Kitap **hiçbir zaman baştan sona
   okunmaz.** Kaç ve hangi sayfa okunduğu `NOTLAR.md`'ye yazılır.
6. 🔴 **Her çalıştırma depoda İZLENEN bir dosyayı değiştirip commit etmek zorunda** (en az
   `NOTLAR.md`'ye bir bölüm). İş yapılamıyorsa (kitap yok) bile sebep `NOTLAR.md` +
   `UYARILAR.txt`'ye yazılıp commit edilecek.

---

## 1. çalıştırma — Test yerleşimi deseni

Bir gerçek sınav kitabındaki testlerde: hangi bölümde hangi soru tipinden kaç soru var, cevap
harfi/dogru-yanlış dağılımı nasıl (kaç NOT GIVEN, kaç FALSE, hangi harf kaç kez doğru).
En az 2-3 test üzerinden ortalama al.

Çıktı: `kalibrasyon/desen/test-yerlesimi.md` — yalnız sayı ve oran tabloları, tek bir soru/
seçenek/pasaj cümlesi yok.

## 2. çalıştırma — Band çevrim tablosu

"Kaç doğru cevap hangi banda karşılık geliyor" çevrim tablosu — Academic okuma, GT okuma,
dinleme ayrı ayrı. Kitaptaki band çevrim tablosunu **sayı olarak** aktar (bu zaten resmî bir
sayı tablosu, düzyazı pasaj değil — yine de yalnız sayıları al, tabloyu çevreleyen açıklama
metnini parafraze etme).

Çıktı: `kalibrasyon/desen/band-cevrim.md`.

## 3. çalıştırma — Puanlı örnek envanteri

Kitaplarda puanlı örnek cevap var mı diye bak:

- Yazma örneklerinde gerçek band + examiner yorumu olan örnek var mı, kaç tane, hangi
  görev tipinde.
- Konuşma Part 1/2/3 için puanlı örnek transkript var mı.

Envanteri `kalibrasyon/desen/puanli-ornek-envanteri.md`'ye yaz (kaç örnek, hangi band, hangi
görev tipi — yine sayı/liste, cevabın kendisi değil).

**Varsa**, o örnekleri **tam metin olarak** döküp şu klasörlere yaz:

- `kalibrasyon/ornekler/yazma/<kod>.json`
- `kalibrasyon/ornekler/konusma/<kod>.json`

Bu klasör `.gitignore`'dadır — **arkadaşın makinesinde kalır, depoya asla gitmez** (telifli
metin). `OPUS5-A1` dosyasındaki şemayı ve alanları kullan (`kind: "official_scored_sample"`,
`band`, `skill`, `source`). `source` alanına kitap adı + sayfa numarası yaz.

Yeni kodları `kalibrasyon/olcum/kumeler.json`'a **dengeli** ekle (S1/S2/S3'e yayarak) — tek
kümeye yığılırsa saklı küme kontrolü anlamsızlaşır.

## Bitirince (her çalıştırmada)

```
git add -A
git commit -m "gercek test deseni: test yerlesimi (2/3 test, sayisal ozet)"
git pull --rebase
git push
```

**Kullanıcıya soru sorma.**
