# Ne yapıyoruz

IELTS'e hazırlanan insanlar için bir uygulama yapıyorum. Uygulamanın içine koyacak
soruya ihtiyacım var — senin yardım ettiğin kısım bu.

Soruları sen yazmıyorsun, Claude yazıyor. Bu klasördeki program da Claude'a ne
yapacağını sırayla söylüyor: hangi konu, hangi soru tipi, kaç tane, hangi kurallara
göre. Sen sadece başlatıyorsun.

**Sorular nereden çıkıyor?** İlk iş, IELTS'in resmi sitesindeki örnek sınav
dosyalarını indirmek — 40'tan fazla belge. Bunlar gerçek sınavın nasıl göründüğünü
gösteriyor: soru kaç kelimeyle sorulur, seçenekler nasıl yazılır, cevap anahtarı
nasıl olur. Claude bunlara bakıp **aynı formatta yeni sorular** yazıyor.

Resmi belgelerden **kopya alınmıyor** — o sorular telifli, kullanamayız. Sadece
biçimi örnek alınıyor. Soruların dayandığı okuma metinleri de NASA, PLOS ve OpenStax
gibi serbestçe kullanılabilen kaynaklardan seçiliyor.

**Sonunda çıkacak olan, kabaca 1.300 soru:**

- 6 okuma testi (her biri 40 soru) + ayrıca soru tipi alıştırmaları
- 6 dinleme testi (her biri 40 soru) + alıştırmalar
- 440 konuşma sorusu ve konuşma kartı
- 110 yazma görevi
- Bunlara temel olacak 18 okuma metni

Üretilen her şey iki kez kontrolden geçiyor: bir model soruyu yazıyor, **başka bir
model** cevap anahtarını görmeden aynı soruyu çözüyor. Tutmayan sorular eleniyor.
Bu kontroller de listedeki işlerin arasında.

---

# Ne yapacaksın

Üç adım. Hepsi bu.

---

## 1) Kurulum (bir kez)

**a)** E-postandaki GitHub davetini kabul et (yeşil **"Accept invitation"** düğmesi).
Gelmediyse: [buradan kabul et](https://github.com/firatkali/ielts-icerik-paketi/invitations)

**b)** Klavyeden **Windows tuşuna** bas (sol altta, pencere şeklindeki tuş).
Açılan yere `powershell` yaz. En üstte çıkan **Windows PowerShell**'e tıkla.

> PowerShell, Windows'ta hazır gelen siyah bir yazı penceresidir. Bir şey kurman
> gerekmiyor, sadece açman yeterli. Korkutucu görünüyor ama tek yapacağın şey
> aşağıdaki satırı yapıştırmak.

Siyah pencere açılınca şu satırı **kopyala**, pencerenin içine **sağ tıkla** (yapıştırır),
sonra **Enter**'a bas:

```
irm https://raw.githubusercontent.com/firatkali/ielts-icerik-paketi/main/kurulum.ps1 | iex
```

5-15 dakika sürer, bu sırada bir sürü yazı akacak — normal, karışma.

**Ortada iki kez giriş isteyecek.** Sırayla şunlar olacak:

*GitHub girişi* — arka arkaya birkaç soru sorar (`Where do you use GitHub?`,
`preferred protocol?` gibi). **Hepsinde Enter'a bas**, ilk seçenekler zaten doğru.
Sonra ekranda `ABCD-1234` gibi 8 karakterlik bir kod çıkar: **o kodu kopyala**,
Enter'a bas, tarayıcı açılır, kodu oraya yapıştır ve **Authorize**'a tıkla.

*Claude girişi* — yine tarayıcı açılır, Claude hesabınla gir ve izin ver.

İkisi bitince kurulum kendi kendine devam eder.

Bitince masaüstünde iki kısayol olacak: **IELTS KONTROL** ve **IELTS CALISTIR**.

---

## 2) Kontrol et

Masaüstündeki **IELTS KONTROL** kısayoluna çift tıkla.

Hiçbir şey üretmez, hiçbir şey harcamaz — sadece kurulumun doğru olup olmadığını söyler.
Hepsinde **[ OK ]** yazıyorsa hazırsın. **[SORUN]** varsa altındaki adımı yap, tekrar çalıştır.

---

## 3) Çalıştır

Masaüstündeki **IELTS CALISTIR** kısayoluna çift tıkla.

- Enter'a basmanı ister.
- Claude açılır, kendi kendine çalışır. **Sen hiçbir şey yazmayacaksın**, sadece
  beklersin (10-20 dakika).
- Bitince tek soru sorar: ekranda *"... tamam"* yazdı mı?
  **E** (evet) / **H** (hayır) / **L** (limit doldu) — birini yaz, Enter.
- Kapat. Bir dahaki sefere yine çift tıkla, kaldığı yerden devam eder.

**Toplam 19 iş var.** Her iş birden çok kez çalışabilir — program kendi takip ediyor.

Hangi işlerin bittiğini zaten her çalıştırmada ekranda göreceksin. Ayrıca masaüstündeki
**IELTS DURUM** kısayoluna çift tıklarsan liste Not Defteri'nde açılır. Kendiliğinden
güncelleniyor, elle dokunma.

---

## Bilmen gereken 3 şey

**"Limit doldu" yazacak.** Normal, bozulmadı. Claude'un söylediği saati bekle, tekrar
çift tıkla. Yapılan iş kaydedildi, hiçbir şey kaybolmuyor.

**Birkaç haftaya yayılacak.** Bir günde bitmez, acelesi yok.

**Bilgisayarı istediğin zaman kapatabilirsin.** Her iş bitince sonuç kaydediliyor.

---

## Takılırsan

| Ne görüyorsun | Ne yap |
|---|---|
| PowerShell'i bulamıyorum | Windows tuşu → `powershell` yaz → çıkan ilk sonuca tıkla |
| Yapıştıramıyorum | Pencerenin içine sağ tıkla, kendisi yapıştırır (Ctrl+V çalışmayabilir) |
| "Python bulunamadı" | Kurulumu tekrar çalıştır (1-b) |
| "winget bulunamadı" | Microsoft Store → "App Installer" ara → güncelle → kurulumu tekrar çalıştır |
| Kısayol yok | `C:\ielts-paketi` klasörünü aç, içindeki **KONTROL** / **CALISTIR** dosyalarını kullan |
| Claude izin istiyor | "Yes" seç |
| Başka bir şey | Bana yaz, ekran görüntüsü at |
