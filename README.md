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
İki kez giriş isteyecek: tarayıcı açılınca hesabınla gir ve **"Authorize"** de.

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
