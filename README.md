# Ne yapacaksın

`prompts` klasöründe **13 dosya** var. Her dosyayı **ayrı bir Claude oturumunda** çalıştıracaksın.

**13 dosya = 13 ayrı oturum.** Bir oturuma sadece bir dosya yapıştır.

---

## Bir kereye mahsus kurulum

**1) Daveti kabul et.**
E-postana GitHub'dan bir davet geldi (konu: *"firatkali has invited you to collaborate"*). İçindeki yeşil **"Accept invitation"** düğmesine bas.
Gelmediyse: [github.com/firatkali/ielts-icerik-paketi/invitations](https://github.com/firatkali/ielts-icerik-paketi/invitations) adresine gir, oradan kabul et.

**2) Projeyi bilgisayarına indir.** Terminale yapıştır, Enter:
```
git clone https://github.com/firatkali/ielts-icerik-paketi.git ~/Desktop/ielts-paketi
```
Masaüstünde `ielts-paketi` diye bir klasör oluşacak.

**3) GitHub'a bağlan.** Terminale yapıştır, Enter:
```
gh auth login
```
Sorular soracak — hepsinde Enter'a basıp geç, sonunda tarayıcı açılır, hesabınla giriş yapıp **"Authorize"** de.

Kurulum bitti. Bir daha yapmayacaksın.

---

## Her dosya için 5 adım

**1.** Terminale bunu yapıştır, Enter — Claude açılır:
```
cd ~/Desktop/ielts-paketi && claude
```

**2.** Dosya adının başına bak, modeli seç:

| Dosya adı | Yaz ve Enter'a bas |
|---|---|
| `OPUS5-` ile başlıyorsa | `/model opus` |
| `FABLE5-` ile başlıyorsa | `/model fable` |
| `CAPRAZ-` ile başlıyorsa | dosyanın içinde yazıyor |

**3.** Prompt dosyasını aç: Masaüstündeki `ielts-paketi` klasörüne gir, `prompts` klasörünü aç, sıradaki dosyaya çift tıkla. Açılan yazının **hepsini** seç (`Cmd+A`), kopyala (`Cmd+C`), Claude'a yapıştır, Enter.

**4.** Bitmesini bekle. Claude sonucu kendisi kaydedip GitHub'a yükler.

**5.** `/exit` yaz, çık. Sonraki dosyaya geç → 1. adımdan tekrar.

---

## Sıra

Numara sırasına göre git:

```
00 → 01 → OPUS5-10 → OPUS5-11 → OPUS5-20 → OPUS5-21 → OPUS5-30
   → FABLE5-40 → FABLE5-41 → FABLE5-42 → FABLE5-43 → CAPRAZ-90 → 99
```

---

## Fırat yeni dosya eklerse

Terminale yapıştır, Enter — yeni dosyalar iner:
```
cd ~/Desktop/ielts-paketi && git pull
```

---

## Takılırsan

- **Uzun sürüyor:** normal, bazıları 10-15 dakika. Bekle.
- **Claude izin isterse:** "Yes" seç. (Normalde sormaz, ayarlar hazır — ama beklenmedik bir şey çıkarsa sorabilir.)
- **`prompts` klasörü boş görünüyor:** `git pull` komutunu çalıştır (yukarıda).
- **Ters gitti:** `/exit` yaz, terminali kapat, baştan aç.
- **`git` veya `gh` komutu bulunamadı diyor:** bana yaz, kurulum lazım.
- **Anlamadığın bir şey:** bana yaz.
