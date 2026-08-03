# Ne yapacaksın

`prompts` klasöründe **13 dosya** var. Her dosyayı **ayrı bir Claude oturumunda** çalıştıracaksın.

**13 dosya = 13 ayrı oturum.** Bir oturuma sadece bir dosya yapıştır.

---

## Bir kereye mahsus kurulum

Terminale sırayla yapıştır, her birinden sonra Enter:

**1)** Projeyi indir:
```
git clone https://github.com/firatkali/ielts-icerik-paketi.git ~/Desktop/ielts-paketi
```

**2)** GitHub'a bağlan — tarayıcı açılır, hesabınla giriş yap, "Authorize" de:
```
gh auth login
```

**3)** Klasöre gir:
```
cd ~/Desktop/ielts-paketi
```

Bu kadar. Bir daha yapmayacaksın.

---

## Her dosya için 6 adım

**1.** Terminalde `claude` yaz, Enter.

**2.** **3 kere Shift+Tab** bas — oto moda geçer.

**3.** Dosya adının başına bak, modeli seç:

| Dosya adı | Yaz ve Enter'a bas |
|---|---|
| `OPUS5-` ile başlıyorsa | `/model opus` |
| `FABLE5-` ile başlıyorsa | `/model fable` |
| `CAPRAZ-` ile başlıyorsa | dosyanın içinde yazıyor |

**4.** Dosyayı aç, **içindekilerin hepsini** kopyala, yapıştır, Enter.

**5.** Bitmesini bekle. Claude sonucu kendisi kaydedip GitHub'a yükler.

**6.** `/exit` yaz, çık. Sonraki dosyaya geç → 1. adımdan tekrar.

---

## Sıra

Numara sırasına göre git:

```
00 → 01 → OPUS5-10 → OPUS5-11 → OPUS5-20 → OPUS5-21 → OPUS5-30
   → FABLE5-40 → FABLE5-41 → FABLE5-42 → FABLE5-43 → CAPRAZ-90 → 99
```

---

## Takılırsan

- **Uzun sürüyor:** normal, bazıları 10-15 dakika. Bekle.
- **Ters gitti:** `/exit` yaz, terminali kapat, baştan aç.
- **`gh auth login` çalışmadı** veya **anlamadığın bir şey:** bana yaz.
