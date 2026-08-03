# Ne yapacaksın

`prompts` klasöründe **13 dosya** var. Her dosyayı Claude'a yapıştırıp çalıştıracaksın.

**Bir oturuma sadece bir dosya yapıştır.**

## 🔴 Önemli: çoğu dosya birden çok kez çalıştırılır

Bir dosyayı yapıştırdığında Claude **o dosyanın sadece bir parçasını** yapar, kaydeder ve
biter. Aynı dosyayı tekrar yapıştırdığında **kaldığı yerden devam eder** — nerede
kaldığını kendisi bulur.

Ne zaman duracaksın? Claude *"… tamam"* dediğinde (ör. "OPUS5-10 tamam"). O dosyayla işin
bitmiştir, sıradakine geçersin.

Her dosyanın en üstünde kaç kez çalıştırılacağı yazıyor. Toplamda **yaklaşık 90 oturum**
olacak. Sıkıcı ama her oturum kısa.

---

# Bir kereye mahsus kurulum (Windows)

Dört program kuracaksın. Hepsi ücretsiz. Sırayla git.

### 1) Git for Windows

[git-scm.com/downloads/win](https://git-scm.com/downloads/win) → indir → kur.
Kurulumda **hiçbir şeyi değiştirme**, hep "Next" de.

> Bu şart. Olmadan Claude komut çalıştıramıyor.

### 2) Python

[python.org/downloads](https://www.python.org/downloads/) → sarı **"Download Python"**
düğmesi → indir → çalıştır.

> ⚠️ Kurulum penceresinin **en altındaki "Add python.exe to PATH"** kutusunu **işaretle**,
> sonra "Install Now" de. Bu kutuyu atlarsan sonra hiçbir şey çalışmaz.

### 3) Claude Code

Başlat menüsüne `PowerShell` yaz, aç. Şunu yapıştır, Enter:

```
irm https://claude.ai/install.ps1 | iex
```

Bitince PowerShell'i **kapat, yeniden aç**. Kontrol et:

```
claude --version
```

Bir numara yazıyorsa tamam.

### 4) GitHub CLI

[cli.github.com](https://cli.github.com/) → "Download for Windows" → kur.

---

### 5) Daveti kabul et

E-postana GitHub'dan bir davet geldi (konu: *"firatkali has invited you to collaborate"*).
İçindeki yeşil **"Accept invitation"** düğmesine bas.
Gelmediyse: [github.com/firatkali/ielts-icerik-paketi/invitations](https://github.com/firatkali/ielts-icerik-paketi/invitations)

### 6) Projeyi indir

PowerShell'i aç, şunu yapıştır, Enter:

```
git clone https://github.com/firatkali/ielts-icerik-paketi.git C:\ielts-paketi
```

`C:\` sürücüsünde `ielts-paketi` klasörü oluşacak.

> Masaüstüne değil `C:\` altına koyuyoruz — Masaüstü OneDrive'a bağlıysa dosyalar
> senkronda takılıyor.

### 7) GitHub'a bağlan

```
gh auth login
```

Sorular soracak — hepsinde Enter'a basıp geç, sonunda tarayıcı açılır, hesabınla giriş
yapıp **"Authorize"** de.

**Kurulum bitti. Bir daha yapmayacaksın.**

---

# Her dosya için 5 adım

**1.** PowerShell'i aç, şunu yapıştır, Enter — Claude açılır:

```
cd C:\ielts-paketi ; claude
```

**2.** Dosya adının başına bak, modeli seç. Yaz ve Enter'a bas:

| Dosya adı şununla başlıyorsa | Yazacağın |
|---|---|
| `00-` | `/model sonnet` |
| `01-` | `/model opus` |
| `OPUS5-` | `/model opus` |
| `FABLE5-` | `/model fable` |
| `CAPRAZ-` | dosyanın içindeki tabloya bak (bazısı opus, bazısı fable) |
| `99-` | `/model sonnet` |

Dosyanın en üstünde de büyük harfle yazıyor — oradan teyit edebilirsin.

**3.** Prompt dosyasını aç ve kopyala:
- `C:\ielts-paketi\prompts` klasörüne gir
- Sıradaki dosyaya **sağ tık → Birlikte aç → Not Defteri** (çift tıklama ile açma)
- `Ctrl+A` (hepsini seç) → `Ctrl+C` (kopyala)
- Claude'a `Ctrl+V` ile yapıştır, Enter

**4.** Bitmesini bekle. Claude sonucu kendisi kaydedip GitHub'a yükler.

**5.** `/exit` yaz, çık.
- Claude *"… tamam"* **demediyse**: aynı dosyayı yeni bir oturumda tekrar yapıştır (1. adımdan).
- *"… tamam"* **dediyse**: sonraki dosyaya geç.

---

# Sıra

Tam dosya adlarıyla, yukarıdan aşağı:

```
 1.  00-KURULUM.md
 2.  01-pasaj-secimi.md
 3.  OPUS5-10-okuma-tamamlama-tipleri.md
 4.  OPUS5-11-okuma-bilgi-eslestirme.md
 5.  OPUS5-20-dinleme-senaryolar.md
 6.  OPUS5-21-dinleme-guvenli-sorular.md
 7.  OPUS5-30-konusma-ve-yazma-gorevleri.md
 8.  FABLE5-40-okuma-dogru-yanlis-verilmemis.md
 9.  FABLE5-41-okuma-coktan-secmeli.md
10.  FABLE5-42-okuma-eslestirme-tipleri.md
11.  FABLE5-43-dinleme-riskli-sorular.md
12.  CAPRAZ-90-dogrulama.md
13.  99-teslim-formati.md
```

⚠️ Sırayı bozma. Örneğin dinleme sorularını (6) yazabilmek için önce dinleme
senaryolarının (5) yazılmış olması gerekiyor.

---

# Fırat yeni dosya eklerse

PowerShell'e yapıştır, Enter — yeni dosyalar iner:

```
cd C:\ielts-paketi ; git pull
```

---

# Takılırsan

- **Uzun sürüyor:** normal, bazıları 10-15 dakika. Bekle.
- **Claude izin isterse:** "Yes" seç. (Normalde sormaz, ayarlar hazır.)
- **`prompts` klasörü boş görünüyor:** `git pull` çalıştır (yukarıda).
- **`claude`, `git`, `gh` veya `python` "tanınmıyor" diyor:** o programın kurulumu
  eksik ya da PowerShell'i kurulumdan sonra yeniden açmadın. Kapat, aç, tekrar dene.
- **Python kurdum ama "python tanınmıyor" diyor:** kurulumda "Add python.exe to PATH"
  kutusunu işaretlememişsin. Python'u kaldırıp kutuyu işaretleyerek tekrar kur.
- **Ters gitti:** `/exit` yaz, PowerShell'i kapat, baştan aç.
- **Anlamadığın bir şey:** bana yaz.
