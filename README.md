# Ne yapacaksın

İki şey. Hepsi bu.

---

## 1) Bir kereye mahsus kurulum

**a)** E-postandaki GitHub davetini kabul et (yeşil **"Accept invitation"** düğmesi).
Gelmediyse: [buradan kabul et](https://github.com/firatkali/ielts-icerik-paketi/invitations)

**b)** Başlat menüsüne `PowerShell` yaz, aç. Aşağıdaki satırı kopyalayıp yapıştır, Enter:

```
irm https://raw.githubusercontent.com/firatkali/ielts-icerik-paketi/main/kurulum.ps1 | iex
```

Gerisini kendi halleder. 5-15 dakika sürer. Ortada bir yerde GitHub girişi isteyecek:
sorulara Enter'a basıp geç, tarayıcı açılınca **"Authorize"** de.

Bitince masaüstünde **IELTS CALISTIR** diye bir kısayol olacak.

---

## 2) Çalıştır

Masaüstündeki **IELTS CALISTIR** kısayoluna **çift tıkla.**

- Sana ne yapacağını söyler, Enter'a basmanı ister.
- Claude açılır ve kendi kendine çalışır. **Sen hiçbir şey yazmayacaksın**, sadece
  bekleyeceksin (10-20 dakika).
- Bitince sana tek bir soru sorar: ekranda *"... tamam"* yazdı mı?
  **E** (evet) / **H** (hayır) / **L** (limit doldu) — birini yaz, Enter.
- Sonra kapat. Bir dahaki sefere yine çift tıkla, kaldığı yerden devam eder.

**Toplam 19 iş var.** Her iş birden çok kez çalışabilir — program kendi takip ediyor,
sen sadece çift tıklamaya devam et.

---

## Bilmen gereken 3 şey

**"Limit doldu" yazacak.** Bu normal, bozulmadı. Claude'un söylediği saati bekle, sonra
tekrar çift tıkla. Yapılan iş kaydedildi, hiçbir şey kaybolmuyor.

**İş birkaç haftaya yayılacak.** Bir günde bitmez. Acelesi yok.

**Bilgisayarı istediğin zaman kapatabilirsin.** Her iş bitince sonuç kaydediliyor.

---

## Takılırsan

| Ne görüyorsun | Ne yap |
|---|---|
| "Python bulunamadı" | Kurulumu tekrar çalıştır (1-b adımı) |
| "winget bulunamadı" | Microsoft Store → "App Installer" ara → güncelle → kurulumu tekrar çalıştır |
| Kısayol yok | `C:\ielts-paketi` klasörünü aç, içindeki **CALISTIR** dosyasına çift tıkla |
| Claude izin istiyor | "Yes" seç |
| Başka bir şey | Bana yaz, ekran görüntüsü at |
