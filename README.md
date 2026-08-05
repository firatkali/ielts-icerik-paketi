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

> 🚫 **Cambridge IELTS kitaplarını (Book 1-19) kullanma.** İnternette dolaşan
> kopyaları korsan; oradan tek bir soru bile içeri girerse uygulama şikâyet üzerine
> mağazadan kaldırılır. O dosyaları açma, Claude'a gösterme, bu klasöre koyma.
> İhtiyacımız olan resmi örnekleri program kendi indirdi.

**Sonunda çıkacak olan, kabaca 1.300 soru:**

- 6 okuma testi (her biri 40 soru) + ayrıca soru tipi alıştırmaları
- 6 dinleme testi (her biri 40 soru) + alıştırmalar
- 440 konuşma sorusu ve konuşma kartı
- 110 yazma görevi
- Bunlara temel olacak 18 okuma metni

Üretilen her şey iki kez kontrolden geçiyor: bir model soruyu yazıyor, **başka bir
model** cevap anahtarını görmeden aynı soruyu çözüyor. Tutmayan sorular eleniyor.
Bu kontroller de listedeki işlerin arasında.

**Sorular bittikten sonra devam eden ikinci bölüm var.** Uygulamanın asıl vaadi
"yazını okuyup puan veriyorum" — o puanın doğru olup olmadığı da ölçülmeli. Listenin
sonundaki işler bunu yapıyor: gerçek sınav görevlilerinin puanladığı örnek cevaplar
modele puanlatılıyor, verdiği puan gerçeğiyle karşılaştırılıyor, sapma varsa düzeltilip
yeniden ölçülüyor. Yanında iki iş daha: okuma parçasına bakmadan cevaplanabilen (yani
bozuk) soruların ayıklanması, ve her göreve farklı seviyelerde örnek cevap yazılması.
Listede her işin ne işe yaradığı yazıyor — **IELTS DURUM** kısayolundan okuyabilirsin.

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

Masaüstündeki **IELTS CALISTIR** kısayoluna çift tıkla. **Hepsi bu.**

Program buradan sonrasını kendi yapar: Claude'u açar, işin bitmesini bekler, sonucu
kaydedip yükler, sıradaki işe geçer. **Toplam 127 iş var**, hepsini sırayla yürütür.

- **Sen hiçbir şey yazmayacaksın.** Enter'a basmak, `/exit` yazmak, E/H demek yok.
- Ekranda tek satır durum göreceksin: kaçıncı işte olduğu ve o işin ne kadar sürdüğü.
- **Kota dolarsa durmaz.** "Kota bekleniyor" yazıp geri sayıma geçer, saati gelince
  kaldığı yerden devam eder. Bu sırada hiçbir şey harcanmaz. **Program kendi kendine
  kapanmaz** — takılsa bile aralıkları açıp denemeye devam eder, senin yeniden
  başlatman gerekmez.
- **Pencereyi kapatma.** Kapanırsa üretim durur (yapılan işler kaybolmaz).
- Bilgisayarın uyuması program tarafından engellenir. Ekran kilitlenebilir, sorun değil.
- Durdurmak istersen pencerede **Ctrl + C**. Kaldığı yer kaydedilir; tekrar çift
  tıklarsan oradan devam eder.

⚠️ **İlk çalıştırmada bir kerelik bir adım isteyebilir:** "bu klasöre güveniyor musun"
sorusunu bir kez senin onaylaman gerekir. Program ne yapacağını ekranda yazar, 1 dakika sürer.

Hangi işlerin bittiğini masaüstündeki **IELTS DURUM** kısayolundan görebilirsin.
Kendiliğinden güncelleniyor, elle dokunma.

---

## Bilmen gereken 3 şey

**"Kota doldu" yazacak.** Normal, bozulmadı. Program bekleyip kendi devam eder,
senin bir şey yapmana gerek yok.

**Birkaç güne/haftaya yayılacak.** Bir oturumda bitmez, acelesi yok.

**Bilgisayarı istediğin zaman kapatabilirsin.** Her iş bitince sonuç kaydediliyor;
tekrar çift tıkladığında kaldığı yerden devam eder.

---

## Takılırsan

| Ne görüyorsun | Ne yap |
|---|---|
| PowerShell'i bulamıyorum | Windows tuşu → `powershell` yaz → çıkan ilk sonuca tıkla |
| Yapıştıramıyorum | Pencerenin içine sağ tıkla, kendisi yapıştırır (Ctrl+V çalışmayabilir) |
| "Python bulunamadı" | Kurulumu tekrar çalıştır (1-b) |
| "winget bulunamadı" | Microsoft Store → "App Installer" ara → güncelle → kurulumu tekrar çalıştır |
| Kısayol yok | `C:\ielts-paketi` klasörünü aç, içindeki **KONTROL** / **CALISTIR** dosyalarını kullan |
| "Bu klasöre güveniyor musun" | Bir kez `claude` yaz → güvendiğini söyleyen seçeneği seç → `/exit` → tekrar çift tıkla |
| Uzun süredir aynı işte duruyor | Bırak dursun, kendi deneyecek. Yarım günden uzun sürerse bana yaz |
| Pencere kapanmış | Tekrar çift tıkla, kaldığı yerden devam eder |
| Başka bir şey | Bana yaz, ekran görüntüsü at |

💡 **İstersen bilgisayar her açıldığında kendiliğinden başlasın:** klasördeki
**ACILISTA-BASLAT** dosyasına çift tıkla, `1` yaz, Enter. Böylece bilgisayar
yeniden başlasa bile üretim kaldığı yerden sürer. Kapatmak için aynı dosya, `2`.
