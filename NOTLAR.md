# Üretim notları

Bu dosyaya her oturumda alınan kararlar, atlanan işler ve karşılaşılan sorunlar yazılır.

## Ortam
- İşletim sistemi: Windows
- Çalışan Python komutu: `python` (veya `py` / `python3` — hangisi çalıştıysa)
- Referanslar: `referans/*.pdf` — **önce doğrudan `Read` dene.** Metin katmanı olan PDF'ler (dinleme transkriptleri, cevap anahtarları) `Read` ile sorunsuz açılıyor. Yalnız taranmış/görüntü tabanlı olanlar (ör. `*-sample-tasks-2023.pdf`) render gerektiriyor ve **`pdftoppm` bu makinede kurulu olmadığı için** "poppler" hatası veriyor. O durumda `pdftotext` (Git for Windows / poppler ile gelen) kurulu; `pdftotext -layout referans/<dosya>.pdf -` ile terminale bas ve öyle oku — ama bu komut oturuma göre izin isteyebiliyor. `referans/text/` klasörü boş; gerekirse `pdftotext -layout kaynak.pdf referans/text/kaynak.txt` ile çıktısı orada tutulabilir.

## 00-KURULUM
- Tarih: 2026-08-03
- İnen referans PDF sayısı: 43

## 01-pasaj-secimi (1. çalıştırma: A01–A06)
- Tarih: 2026-08-03
- Üretilen: `passages/academic/A01.json` … `A06.json`, `passages/INDEX.json` (6 kayıt).
- Kaynaklar (hepsi CC BY 4.0 veya ABD kamu malı, WebSearch+WebFetch ile bulundu):
  - A01 — PLOS ONE, Foerder ve ark. (2011), "Insightful Problem Solving in an Asian
    Elephant" — doğa/hayvan davranışı.
  - A02 — PLOS ONE, Tricarico ve ark. (2011), "I Know My Neighbour: Individual
    Recognition in Octopus vulgaris" — doğa/hayvan davranışı.
  - A03 — NOAA/AOML, "Volcanic Island of Maug Provides Natural Lab for Ocean
    Acidification" — iklim/jeoloji/okyanus, kamu malı.
  - A04 — NASA Science (Webb Mission Team blog), "New Moon Discovered Orbiting
    Uranus Using NASA's Webb Telescope" (2025) — uzay/gezegen bilimi, kamu malı.
  - A05 — PLOS ONE, "Ancient DNA from 8400 Year-Old Çatalhöyük Wheat" (2016) —
    tarih/arkeoloji.
  - A06 — PLOS ONE, "Experienced teammates increase productivity in remote work:
    Evidence from a full remote work company in Japan" — toplum/iş dünyası.
- Her pasaj ham kaynaktan **yeniden yazıldı** (özetlenip parafraze edildi), atıf
  numaraları/istatistik tabloları temizlendi, 7–9 harflendirilmiş paragrafa (A–H)
  bölündü. Kelime sayıları gerçekten sayıldı (Python `len(text.split())`), hepsi
  700–900 aralığında: A01=756, A02=730, A03=721, A04=765, A05=706, A06=746.
- **12 pasajlık konu dağılımı kararı:** Plandaki hedef (Doğa 3 · İklim/jeoloji/okyanus 2
  · Uzay 1 · Tarih/arkeoloji 2 · Toplum 2 · Sağlık 2) tek turda bitmiyor, iki turda
  (A01–A06 / A07–A12) tamamlanacak şekilde bölündü. Bu turda: Doğa 2, İklim/jeoloji/
  okyanus 1, Uzay 1, Tarih/arkeoloji 1, Toplum 1 üretildi. **A07–A12 turunda kalan:**
  Doğa 1, İklim/jeoloji/okyanus 1, Tarih/arkeoloji 1, Toplum 1, Sağlık ve insan
  davranışı 2 — bu dağılıma uyulmalı.
- `passages/INDEX.json`'daki `assigned_test`/`position`, PLAN dosyasındaki eşlemeye
  göre dolduruldu: AC1←A01(1),A02(2),A03(3); AC2←A04(1),A05(2),A06(3).
- Atlanan/sorun: yok — kaynak arama ve indirme sorunsuz tamamlandı.

## OPUS5-10 (1. çalıştırma: AC1 tam testi)
- Tarih: 2026-08-03
- `content/reading/tests/` ve `content/reading/practice/` boştu → sıradaki bitmemiş paket
  **1. paket (AC1)** idi, o yapıldı. **15 soru** üretildi, hedefle birebir aynı.
- Üretilen dosyalar:
  - `content/reading/tests/AC1/note-completion.json` — soru 1–6, pasaj **A01**
  - `content/reading/tests/AC1/sentence-completion.json` — soru 19–22, pasaj **A02**
  - `content/reading/tests/AC1/summary-completion.json` — soru 36–40, pasaj **A03**
- **Seçilen alt tipler ve gerekçe:**
  - 1–6 için **not tamamlama** seçildi. A01 bir araştırma anlatısı: karşılaştırılacak
    iki-üç değişken yok (tablo olmaz), adım adım süreç yalnız C paragrafında sıkışık
    (akış şeması yapılsaydı cevaplar tek paragrafa yığılırdı, "cevaplar pasaja yayılsın"
    kuralına aykırı olurdu). Not tamamlamada cevaplar B–B–C–D–E–F'ye yayıldı.
  - 36–40 için özet tamamlamanın **metinden kelime seçme** alt tipi kullanıldı
    (`word_bank: null`).
  - ⚠️ **AC2–AC4 için not:** 1–6 aralığında not tamamlama tekrar edilmemeli — AC2'de
    tablo, AC3'te akış şeması, AC4'te not/tablo gibi bir dağılım hedeflensin. Özet
    tamamlamada da **listeden kelime seçme** (`word_bank` dolu) alt tipi en az bir
    Academic testte kullanılsın.
- Kelime sınırları: 1–6 `ONE WORD ONLY`; 19–22 ve 36–40 `NO MORE THAN TWO WORDS`.
  Bütün cevaplar sınıra uyuyor.
- Elenen soru: yok. Ele alınıp **vazgeçilen** cevap adayları: A01'de `stick` (pasajda 4
  kez geçiyor, benzersiz değil), A03'te `vents` (5 kez) ve tek başına `algae` (3 kez).
  Bunların yerine tek geçişli `bamboo`, `dye`, `weedy algae` seçildi.
  `caldera` ve `bioerosion` pasajda 2'şer kez geçiyor ama ikisi de aynı sözcük ve aynı
  göndergeye ait olduğu için cevapta belirsizlik yaratmıyor — bırakıldı.
- Doğrulama: geçici bir kontrol scriptiyle her dosya için JSON geçerliliği, soru numara
  aralığı, `evidence`in pasajda birebir geçişi, `evidence_locator` (paragraf + kaçıncı
  cümle) doğruluğu, cevabın pasajda geçiş sayısı ve **konum sırası**, kelime sınırı,
  cevap tekrarı, soru kökünün birebir kopya olmaması ve "IELTS" geçmemesi tek tek
  denetlendi — hepsi temiz. Ardından `python tools/dogrula.py`: **şema hatası 0**.
- **`tools/dogrula.py`'de bir hata düzeltildi:** telif taraması döngüsü
  `passages/INDEX.json`'ı da açıyordu; bu dosyanın kökü sözlük değil **liste** olduğu
  için `d.get(...)` çağrısı `AttributeError` veriyor ve script çöküyordu. Lisans kontrolü
  döngüsündeki mevcut `INDEX.json` atlamasının aynısı telif döngüsüne de eklendi. Hata
  content/ altında ilk soru dosyası oluşana kadar görünmüyordu.
- AC1 şu an 15/40; kalan 25 soru OPUS5-11, FABLE5-40/41/42 promptlarından gelecek.
- **OPUS5-10 bitmedi:** 10 paketten 1'i tamam. Kalan 9 paket (AC2, AC3, AC4, GT1, GT2 ve
  5 alıştırma paketi) sonraki çalıştırmalarda yapılacak. AC3/AC4 için `A07–A12`,
  GT1/GT2 için `G01–G06` pasajları **henüz üretilmedi** — o paketler ancak pasajlar
  geldikten sonra yapılabilir; sırası gelince önce pasaj havuzuna bakılmalı.

## 01-pasaj-secimi (2. çalıştırma: A07–A12)
- Tarih: 2026-08-03
- ⚠️ **Oturum numarası notu:** Bu oturumu başlatan kullanıcı bunu "3. çalıştırma" olarak
  tanımlamıştı (promptun kendi tanımına göre 3. çalıştırma `G01–G06` üretir). Ancak depo
  durumu kontrol edildiğinde `passages/academic/`'ta sadece A01–A06 vardı, `passages/general/`
  tamamen boştu — yani bu, pasaj promptu için gerçekte **2. çalıştırmaydı**. Kullanıcıya
  bu çelişki soruldu, A07–A12 üretilmesi (promptun kendi "sıradaki grubu üret" kuralına
  uygun olan seçenek) onaylandı. **G01–G06 (GT metinleri, 3. tur) hâlâ üretilmedi** —
  sıradaki çalıştırma bunu yapmalı.
- Üretilen: `passages/academic/A07.json` … `A12.json`, `passages/INDEX.json` güncellendi
  (12 kayıt, AC3←A07/A08/A09, AC4←A10/A11/A12).
- Kaynaklar (hepsi CC BY 4.0 veya ABD kamu malı, WebSearch+WebFetch ile bulundu):
  - A07 — PLOS ONE, Mildener ve ark., "Evidence for mirror self-recognition in beluga
    whales (Delphinapterus leucas)" — doğa/hayvan davranışı.
  - A08 — NASA Earth Observatory, "Landslide and Avalanche Debris Litter Hubbard Glacier"
    (Aralık 2025 depremi sonrası) — iklim/jeoloji/okyanus, kamu malı.
  - A09 — PLOS ONE, Petrone ve ark. (2020), "Preservation of neurons in an AD 79 vitrified
    human brain" (Herculaneum) — tarih/arkeoloji.
  - A10 — PLOS ONE, Pitchforth ve ark. (2020), "The work environment pilot: An experiment
    to determine the optimal office design for a technology company" — toplum/iş dünyası.
  - A11 — PLOS ONE, Bielinis ve ark. (2021), "The effects of viewing a winter forest
    landscape... on the psychological relaxation of young Finnish adults" — sağlık/insan
    davranışı.
  - A12 — PLOS ONE, Lo, Dijk & Groeger (2014), "Comparing the Effects of Nocturnal Sleep
    and Daytime Napping on Declarative Memory Consolidation" — sağlık/insan davranışı.
- **12 pasajlık konu dağılımı tamamlandı:** Bu turda NOTLAR.md'deki 1. tur notunda
  belirtilen kalan pay uygulandı: Doğa 1 (A07), İklim/jeoloji/okyanus 1 (A08),
  Tarih/arkeoloji 1 (A09), Toplum 1 (A10), Sağlık ve insan davranışı 2 (A11, A12).
  A01–A12 toplamda plandaki hedef dağılıma (Doğa 3, İklim/jeoloji/okyanus 2, Uzay 1,
  Tarih/arkeoloji 2, Toplum 2, Sağlık 2) tam uyuyor.
- Her pasaj ham kaynaktan yeniden yazıldı (özetlenip parafraze edildi), doğrudan alıntılar
  dolaylı anlatıma çevrildi, istatistiksel yöntem detayları (p değerleri, eta-kare gibi)
  ve şirket/kurum özel adları (Booking.com, Häme University of Applied Sciences) genel
  ifadelerle anıldı, 8 harflendirilmiş paragrafa (A–H) bölündü. Kelime sayıları gerçekten
  sayıldı (Python `len(text.split())`), hepsi 700–900 aralığında: A07=887, A08=714,
  A09=753, A10=760, A11=796, A12=731. A10 ve A11 ilk taslakta 700'ün altında kalmıştı,
  kaynaktaki ek doğru bilgilerle (ör. A10'da git-commit ölçümünün yorumu, A11'de anket
  zamanlaması ve pilot çalışma uyarısı) genişletilip aralığa çekildi.
- `passages/INDEX.json`'daki `assigned_test`/`position`, PLAN dosyasındaki eşlemeye göre
  dolduruldu: AC3←A07(1),A08(2),A09(3); AC4←A10(1),A11(2),A12(3).
- Atlanan/sorun: yok — kaynak arama ve indirme sorunsuz tamamlandı. `python tools/dogrula.py`
  ile pasaj lisans/telif taraması temiz çıktı.

## 01-pasaj-secimi (3. çalıştırma: G01–G06)
- Tarih: 2026-08-04
- Depo durumu kontrol edildi: `passages/academic/`'ta A01–A12 tamdı, `passages/general/`
  tamamen boştu. Bu, hem promptun kendi "3. çalıştırma → G01–G06" tanımıyla hem de mevcut
  durumla uyumluydu, çelişki yoktu — doğrudan G01–G06 üretildi.
- `referans/ielts-general-reading-sample-tasks-2023.pdf` `Read` aracıyla açılamadı
  (`pdftoppm` eksik); `pdftotext -layout ... -` ile terminale basılıp öyle okundu — sadece
  format referansı olarak kullanıldı, hiçbir cümle kopyalanmadı. Bu bilgi dosyanın başındaki
  "Ortam" notuna da eklendi ki sonraki oturumlar tekrar takılmasın.
- Üretilen dosyalar ve kaynaklar:
  - **G01** (Bölüm 1, orijinal) — "Cloverfield Public Services": kurgusal bir kasabadaki
    beş günlük hizmet duyurusu (kütüphane üyeliği, spor merkezi kurs takvimi, ulaşım kartı
    kuralları, apartman geri dönüşüm rehberi, dil kursu kaydı). 433 kelime, 5 metin (A–E),
    her biri 82–94 kelime.
  - **G02** (Bölüm 1, orijinal) — "Leisure in Millbrook": farklı bir kurgusal kasabadaki
    beş boş-zaman hizmeti (bisiklet kiralama, festival programı, bahçe parseli kuralları,
    yüzme havuzu seansları, akşam kursu kaydı) — G01 ile aynı temayı tekrar etmemek için
    bilinçli olarak "kamu hizmetleri" değil "boş zaman" kümesi seçildi. 414 kelime, 5 metin,
    78–87 kelime aralığında.
  - **G03** (Bölüm 2, orijinal) — "Fernbridge Manufacturing — Staff Handbook Extracts":
    kurgusal bir üretim şirketinin çalışma saatleri/molalar el kitabı bölümü + izin/mesai
    politikası, iki metin, her biri kendi içinde A–D harfli paragraflara ve madde
    listelerine bölündü. 510 kelime.
  - **G04** (Bölüm 2, orijinal) — "Cedarline Financial Services — Internships and Remote
    Working": kurgusal bir finans şirketinin staj başvuru rehberi + uzaktan çalışma
    politikası, aynı yapıda (A–D harfli iç paragraflar, madde listeleri). 460 kelime.
  - **G05** (Bölüm 3, CC BY) — "What Ends Up in the Rubbish: A Household Food Waste Study",
    PLOS ONE, Martianto D, et al. (2024) "The quantity and composition of household food
    waste: Implications for policy", PLoS ONE 19(6): e0305087, CC BY 4.0 —
    https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0305087. Bogor
    Regency (Endonezya) kentsel/kırsal 215 hanede yapılan gıda israfı çalışması. 823
    kelime, 9 harflendirilmiş paragraf (A–I).
  - **G06** (Bölüm 3, CC BY) — "Why Volunteers Tend to Report Better Health", PLOS ONE,
    Detollenaere J, Willems S, Baert S (2017) "Volunteering, income and health", PLoS ONE
    12(3): e0173139, CC BY 4.0 —
    https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0173139. Avrupa
    Sosyal Araştırması (29 ülke, ~43.000 kişi) verisiyle gönüllülük–gelir–sağlık ilişkisini
    inceleyen çalışma. 795 kelime, 9 harflendirilmiş paragraf (A–I).
- **Bölüm 2 şema kararı:** `texts[].text` alanı tek bir string olduğu için, iç paragraf
  harflendirmesi (A, B, C…) doğrudan metin gövdesine gömüldü (satır başında harf, ardından
  paragraf). Üst düzey `texts[].label` alanı ise setteki iki metni birbirinden ayırt etmek
  için `A`/`B` olarak kullanıldı — yani aynı harf iki farklı anlamda (dış metin kimliği ve
  iç paragraf) kullanılıyor olabilir, bu kasıtlı bir tasarım kararı. Soru üretimi bu
  pasajları kullanırken buna dikkat etmeli.
- Kelime sayıları gerçekten sayıldı (Python `len(text.split())`): G01–G02 için her kısa
  metin 60–100 aralığında, G03–G04 toplamı ~500'e yakın (510, 460), G05–G06 750–900
  aralığında (823, 795). İlk taslaklarda G01–G06 hepsi hedefin altında/üstündeydi
  (G01=479→433, G02=490→414 kısaltıldı; G03=392→510, G04=334→460, G05=693→823,
  G06=639→795 yeni paragraf/cümlelerle genişletildi, kaynak makalelerdeki gerçek ek
  bilgilerle: G05'e içecek israfı + çöp kutusu ölçüm sınırlaması paragrafı, G06'ya
  duyarlılık analizleri paragrafı ve öz-bildirimli sağlığın geçerliliğine dair bir cümle).
- `passages/INDEX.json`'a 6 kayıt eklendi: GT1←G01(1),G03(2),G05(3); GT2←G02(1),G04(2),
  G06(3), PLAN dosyasındaki pasaj→test eşlemesine göre.
- Kalite kontrolü: her metinde somut ayrıntı (saat/ücret/tarih/telefon/koşul) var; G05/G06
  en az 3 paragrafta sayı/tarih/isim ve en az 2 yerde yazar değerlendirme cümlesi
  içeriyor; "IELTS" kelimesi hiçbir dosyada geçmiyor; G01–G04'te tüm yer/kurum/şirket
  adları uydurma (Cloverfield, Millbrook, Fernbridge Manufacturing, Cedarline Financial
  Services vb.). `python tools/dogrula.py`: şema hatası 0, lisans eksik 0, yasak
  kaynak/IELTS taraması temiz.
- **Pasaj havuzu artık tamam:** A01–A12 + G01–G06 = 18 pasaj, PLAN'daki tüm kimlikler
  üretildi. Sonraki `01-pasaj-secimi` çalıştırması gerekmiyor; sıradaki işler
  `content/reading/tests/` ve `content/reading/practice/` altındaki soru üretim
  promptlarıdır (OPUS5-10/11, FABLE5-40/41/42) — AC2, AC3, AC4, GT1, GT2 ve 5 alıştırma
  paketi hâlâ bekliyor.
- Atlanan/sorun: yok.

## OPUS5-10 (2. çalıştırma: AC2 tam testi)
- Tarih: 2026-08-04
- Depo kontrolü: `content/reading/tests/` altında yalnız `AC1/` vardı (15 soru, tam),
  `content/reading/practice/` klasörü hiç yoktu → çalıştırma listesindeki **2. paket (AC2)**
  sıradaki bitmemiş işti, o yapıldı. **15 soru** üretildi, hedefle birebir aynı.
- Üretilen dosyalar:
  - `content/reading/tests/AC2/flow-chart-completion.json` — soru 1–6, pasaj **A04**
  - `content/reading/tests/AC2/sentence-completion.json` — soru 19–22, pasaj **A05**
  - `content/reading/tests/AC2/summary-completion.json` — soru 36–40, pasaj **A06**
- **Seçilen alt tipler ve gerekçe:**
  - 1–6 için **akış şeması tamamlama** seçildi (AC1'de not tamamlama kullanılmıştı, tekrar
    edilmedi). A04 yeni bir Uranüs uydusunun bulunmasını sırayla anlatıyor: gözlem →
    geçici kod → çap tahmini → yörüngenin ölçülmesi → katalogda sıra → kalıcı ad onayı.
    Bu zincir pasajda B→C→D→E sırasıyla ilerlediği için akış şeması hem doğal hem de sıra
    kuralına uygun. **Tablo denendi ve vazgeçildi:** A04'teki tek gerçek karşılaştırma
    Voyager 2 (paragraf F) ile Webb (paragraf B) arasında; tablo satırları bu ikisini
    yan yana koyduğunda cevapların pasajdaki geçiş sırası bozuluyordu.
  - 19–22 **cümle tamamlama**, `NO MORE THAN TWO WORDS` (A05).
  - 36–40 için özet tamamlamanın **listeden kelime seçme** alt tipi kullanıldı
    (`word_bank` dolu: A–J, 10 seçenek, 5 doğru + 5 çeldirici). AC1'de metinden kelime
    seçme (`word_bank: null`) kullanılmıştı; NOTLAR'daki "en az bir Academic testte
    listeden seçme olsun" notu böylece karşılandı.
  - ⚠️ **AC3–AC4 için not:** 1–6 aralığında tablo tamamlama hâlâ hiç kullanılmadı; A07–A12
    içinde karşılaştırmalı yapısı olan bir pasaj varsa oraya tablo konsun. Özet
    tamamlamada AC3/AC4'ten en az birinde yine metinden kelime seçme kullanılabilir.
- **Şema kararı (listeden seçme alt tipi):** `word_bank` alanı `[{"letter": "A", "text":
  "..."}, ...]` biçiminde nesne listesi olarak yazıldı. Bu alt tipte `answer` **harf**
  tutuyor (`["A"]`), `accepted_variants` ise harfi *ve* seçeneğin metnini birlikte kabul
  ediyor (`["A", "a controlled experiment", "controlled experiment"]`) — uygulama hangisiyle
  karşılaştırırsa çalışsın diye. `word_limit` bu alt tipte anlamsız olduğu için `null`.
  Sonraki listeden-seçme dosyaları da bu düzeni izlemeli.
- Kelime sınırları: 1–6 `NO MORE THAN THREE WORDS AND/OR A NUMBER` (soru 6'nın cevabı
  `International Astronomical Union` üç kelime); 19–22 `NO MORE THAN TWO WORDS`;
  36–40 sınırsız (listeden seçme). Bütün cevaplar sınıra uyuyor.
- Elenen soru: yok. **Vazgeçilen cevap adayları:** A04'te `ten kilometres` (pasaj çapı
  "about six miles, or ten kilometres" diye veriyor — iki cevap da savunulabilirdi,
  benzersiz değil), `hexaploid` (A05'te 4 kez geçiyor), `spelt` (A05'te 2 kez).
  Yerlerine tek geçişli `reflects`, `fourteenth`, `plant DNA`, `D genome` seçildi.
  A06'nın çeldirici listesine bilinçli olarak **rastgeleleştirme** çağrıştıran bir seçenek
  konmadı: pasaj hem "effectively randomised" hem "as if ... a controlled experiment"
  diyor, ikisi de listede olsaydı 36. sorunun iki savunulabilir cevabı olurdu.
- Doğrulama: geçici bir denetim scriptiyle her dosya için JSON geçerliliği, soru numara
  aralığı (1–6 / 19–22 / 36–40), `evidence`in pasajda **birebir** geçişi,
  `evidence_locator` (paragraf + kaçıncı cümle) doğruluğu, cevabın pasajdaki geçiş sayısı
  (hepsi 1), `evidence` konumuna göre **sıra kuralı**, kelime sınırı, cevap tekrarı,
  soru kökü ile pasaj arasında 6+ kelimelik birebir örtüşme olmaması (hepsi 0),
  `explanation` alanlarının Türkçe olması, `stem_block` boşluk numaralarının soru
  numaralarıyla eşleşmesi ve "IELTS" geçmemesi tek tek denetlendi — **hata 0**.
  Ardından `python tools/dogrula.py`: **şema hatası 0**, okuma sorusu 30 (AC1 15 + AC2 15),
  görünür metinde IELTS 0, yasak kaynak 0. Geçici script silindi.
- Referans PDF'leri: `referans/text/` klasörü bu oturumda da yoktu. Cevap anahtarı
  PDF'lerinden ikisi (`sentence-completion`, `summary-completion-selecting-from-list`)
  `Read` ile açıldı — bunlar yalnız cevap listesi içeriyor, yönerge cümlesi yok.
  `ielts-academic-reading-sample-tasks-2023.pdf` render edilemedi (`pdftoppm` yok) ve
  `pdftotext` bu oturumda izin verilmediği için çalıştırılamadı; yönerge kalıpları
  prompt dosyasında verilen üç kalıptan ve AC1'in yerleşik biçiminden alındı.
- Atlanan/sorun: yok.

## OPUS5-10 (3. çalıştırma: AC3 tam testi)
- Tarih: 2026-08-04
- Depo kontrolü: `content/reading/tests/` altında `AC1/` ve `AC2/` vardı (15'er soru, tam),
  `content/reading/practice/` boştu → çalıştırma listesindeki **3. paket (AC3)** sıradaki
  bitmemiş işti, o yapıldı. **15 soru** üretildi, hedefle birebir aynı.
  (Kullanıcı bu oturumu "2. çalıştırma" diye tanımlamıştı; depo durumu AC2'nin bittiğini
  gösterdiği için promptun kendi "sıradaki bitmemiş paketi yap" kuralı uygulandı.)
- Üretilen dosyalar:
  - `content/reading/tests/AC3/table-completion.json` — soru 1–6, pasaj **A07**
  - `content/reading/tests/AC3/sentence-completion.json` — soru 19–22, pasaj **A08**
  - `content/reading/tests/AC3/summary-completion.json` — soru 36–40, pasaj **A09**
- **Seçilen alt tipler ve gerekçe:**
  - 1–6 için **tablo tamamlama** seçildi. AC1'de not, AC2'de akış şeması kullanılmıştı;
    NOTLAR'daki "tablo hâlâ hiç kullanılmadı" notu böylece karşılandı. A07 (beyaz
    balinalarda ayna testi) tablo için uygun, çünkü pasaj boyunca ikili karşılaştırmalar
    var: ayna ↔ kontrol levhası, gerçek işaret ↔ görünmez sahte işaret. Tablo
    "Odak / Araştırmacılar ne yaptı / Ne gördüler" sütunlarıyla kuruldu; satırlar pasaj
    sırasını (B → C → D → E → F) izlediği için **sıra kuralı** hücre okuma yönüyle
    (soldan sağa, yukarıdan aşağı) birebir uyuşuyor.
  - 19–22 **cümle tamamlama**, bu kez `ONE WORD ONLY` (A08). AC1 ve AC2'de bu aralıkta
    `NO MORE THAN TWO WORDS` kullanılmıştı; A08 tek kelimelik, tek geçişli teknik terimler
    (displacement, bright, surge, mountaineers) barındırdığı için daha dar sınır seçildi.
  - 36–40 için özet tamamlamanın **metinden kelime seçme** alt tipi kullanıldı
    (`word_bank: null`), NOTLAR'daki "AC3/AC4'ten en az birinde metinden seçme olsun"
    notuna uygun olarak. Özet A09'un C–G paragraflarını (camlaşmanın koşulları, kullanılan
    yöntemler, ölçümler, protein kanıtı, ısıl koşullar) kapsıyor.
  - ⚠️ **AC4 için not:** 1–6 aralığında not / tablo / akış şeması üçünün de kullanılmış
    olması gerekiyordu; AC4'te bunlardan biri tekrar edilecek — A10'un yapısına bakılıp
    en uygun olan seçilsin (üç tip de bir kez kullanıldığı için tekrar serbest). Özet
    tamamlamada AC4'te **listeden kelime seçme** kullanılırsa iki alt tip 2–2 dengelenir.
- Kelime sınırları: 1–6 `NO MORE THAN TWO WORDS` (en uzun cevap `twenty-three seconds`;
  tireli kelime tek kelime sayılıyor); 19–22 `ONE WORD ONLY`; 36–40 `NO MORE THAN TWO
  WORDS`. Bütün cevaplar sınıra uyuyor.
- Elenen soru: yok. **Vazgeçilen cevap adayları:** A07'de `panel` (pasajda 3 kez geçiyor),
  `sham` (2 kez) ve `two hours` (27/23 saatlik sürelerle karışma riski); A08'de
  `cryosphere` — "the cryosphere is effectively covering up the geosphere" cümlesinden
  soru kurulsaydı `ice` de savunulabilir bir cevap olurdu, tek cevap kuralı gereği
  bırakıldı; ayrıca `debris` (pasajda çok kez geçiyor). A09'da `myelin` elendi: soru
  kökünde tanımını vermeden sorulamıyordu, tanım verilince cevap kendiliğinden
  söylenmiş oluyordu. Yerlerine tek geçişli `acrylic`, `barrel rolls`, `cosmetic`,
  `displacement`, `surge`, `reference databases`, `microtubules` seçildi.
- Doğrulama: geçici bir denetim scriptiyle (`tools/_ac3_kontrol.py`, sonra silindi) her
  dosya için JSON geçerliliği, soru numara aralığı (1–6 / 19–22 / 36–40), `evidence`in
  pasajda **birebir** geçişi, `evidence_locator` doğruluğu, cevabın pasajdaki geçiş sayısı
  (**hepsi tam 1**), `evidence` konumuna göre sıra kuralı, kelime sınırı, cevap tekrarı,
  soru kökü ile pasaj arasında 6+ kelimelik birebir örtüşme olmaması, `explanation`
  alanlarının Türkçe olması, tablo/özet gövdesindeki boşluk numaralarının soru
  numaralarıyla eşleşmesi ve "IELTS" geçmemesi denetlendi. **İlk turda 2 hata çıktı ve
  düzeltildi:** (1) tablo 1. sorusunun kökü A07'den "a large two-way mirror was lowered
  into" ifadesini birebir taşıyordu → yeniden yazıldı; (2) 38. sorunun
  `evidence_locator`'ı E/3 girilmişti, doğrusu **E/4** (paragraf E "The structural
  measurements were remarkably precise." cümlesiyle başlıyor, elle sayarken atlanmış).
  Düzeltmeden sonra script **hata 0**. Ardından `python tools/dogrula.py`: **şema hatası 0**,
  okuma sorusu 45 (AC1 15 + AC2 15 + AC3 15), görünür metinde IELTS 0, yasak kaynak 0.
- Referans PDF'leri: `referans/text/` yine yoktu ve `pdftotext` bu oturumda da izin
  alamadı. `table-completion` cevap anahtarı PDF'i `Read` ile açıldı — sadece cevap listesi
  içeriyor, ama sayısal cevaplarda kullanılan `two/2`, `five/5` biçimindeki çift kabul
  yazımını doğruladı; `accepted_variants` alanları buna göre yazıldı (`fourteen`/`14`,
  `twenty-three seconds`/`23 seconds`, `seven`/`7`).
  `ielts-academic-reading-sample-tasks-2023.pdf` yine render edilemedi (`pdftoppm` yok);
  yönerge kalıpları prompt dosyasındaki üç kalıptan alındı.
- Atlanan/sorun: yok. **OPUS5-10'da 10 paketten 3'ü tamam;** kalan 7 paket AC4, GT1, GT2 ve
  5 alıştırma paketi. Alıştırma paketleri için `content/reading/practice/` hâlâ boş.

## OPUS5-10 (4. çalıştırma: AC4 tam testi)
- Tarih: 2026-08-04
- Depo kontrolü: `content/reading/tests/` altında `AC1/`, `AC2/`, `AC3/` vardı (15'er soru,
  tam), `content/reading/practice/` boştu → çalıştırma listesindeki **4. paket (AC4)**
  sıradaki bitmemiş işti, o yapıldı. **15 soru** üretildi, hedefle birebir aynı.
  (Kullanıcı bu oturumu "3. çalıştırma" diye tanımlamıştı; depo durumu AC3'ün bittiğini
  gösterdiği için promptun kendi "sıradaki bitmemiş paketi yap" kuralı uygulandı — aynı
  kayma AC3 oturumunda da vardı.)
- Üretilen dosyalar:
  - `content/reading/tests/AC4/note-completion.json` — soru 1–6, pasaj **A10**
  - `content/reading/tests/AC4/sentence-completion.json` — soru 19–22, pasaj **A11**
  - `content/reading/tests/AC4/summary-completion.json` — soru 36–40, pasaj **A12**
- **Seçilen alt tipler ve gerekçe:**
  - 1–6 için **not tamamlama** seçildi. AC1 not, AC2 akış şeması, AC3 tablo kullanmıştı;
    üç tip de birer kez kullanıldığı için AC4'te tekrar serbestti (AC3 notundaki karar).
    A10 (dört ofis düzeninin karşılaştırıldığı deney) ilk bakışta tabloya uygun görünüyor
    ama **tablo denendi ve vazgeçildi:** dört düzenin *tanımları* B paragrafında,
    *sonuçları* D ve E'de veriliyor; satırları düzenlere ayıran bir tablo, hücreler
    soldan sağa okunduğunda B↔D arasında ileri geri zıplıyor ve **sıra kuralını**
    bozuyordu. Not tamamlamada cevaplar A–B–B–C–F–H'ye yayıldı, sıra korundu.
    Akış şeması da elendi: A10 sıralı bir süreç değil, paralel bir karşılaştırma anlatıyor.
  - 19–22 **cümle tamamlama**, `NO MORE THAN TWO WORDS` (A11).
  - 36–40 için özet tamamlamanın **listeden kelime seçme** alt tipi kullanıldı
    (`word_bank` dolu: A–J, 10 seçenek, 5 doğru + 5 çeldirici), AC3 notundaki "AC4'te
    listeden seçme kullanılırsa iki alt tip 2–2 dengelenir" önerisine uygun olarak.
    **Academic özet tamamlama dengesi artık 2–2:** AC1 ve AC3 metinden seçme, AC2 ve AC4
    listeden seçme. Şema, AC2'de kararlaştırılan düzeni izliyor (`answer` harf tutuyor,
    `accepted_variants` harfi ve seçenek metnini birlikte kabul ediyor, `word_limit: null`).
  - ⚠️ **GT1/GT2 için not:** GT'de 15–20 aralığı yalnız not/tablo tamamlama olabiliyor
    (akış şeması plana göre yok). GT1'de biri, GT2'de öteki kullanılırsa iki tip de
    görülmüş olur. Özet tamamlamada (37–40) GT tarafında henüz hiçbir alt tip
    kullanılmadı; ikisinden birinde listeden seçme yapılabilir.
- **Alt tip dağılımı özeti (Academic, 1–6):** AC1 not · AC2 akış şeması · AC3 tablo ·
  AC4 not. Üç tip de en az bir kez kullanıldı, plandaki "dört Academic testte hepsi aynı
  tip olmasın" şartı karşılandı.
- Kelime sınırları: 1–6 `ONE WORD ONLY` (bütün cevaplar tek kelime; `sound-absorbing`
  tireli olduğu için tek kelime sayılıyor); 19–22 `NO MORE THAN TWO WORDS` (en uzunu
  `silver birch`); 36–40 sınırsız (listeden seçme, `word_limit: null`). Bütün cevaplar
  sınıra uyuyor.
- Elenen soru: yok. **Vazgeçilen cevap adayları:** A10'da `noise` (pasajda 4 kez geçiyor:
  A, C, F, H), `code commits` (2 kez: C ve G), `unassigned` (2 kez: B ve E), `energy`
  (2 kez), `default` (2 kez), `ranking` (2 kez) — hepsi benzersizlik kuralına takıldı.
  A11'de `snow` (9 kez) ve `vitality` (2 kez) elendi; ayrıca E paragrafındaki `flow`
  tanımı soru kökünde verilmeden sorulamadığı, verilince de cevabı ele verdiği için
  bırakıldı. Yerlerine tek geçişli `reconfigure`, `soundproof`, `sound-absorbing`,
  `headphones`, `novelty`, `workflows`, `silver birch`, `humidity`, `passage`,
  `vegetation` seçildi. A12'nin çeldirici listesine bilinçli olarak `between-subjects`,
  `unrelated in meaning` ve `the length of the nap` kondu — üçü de pasajda geçen ama
  ilgili boşlukta **yanlış** olan ifadeler, yani gerçek çeldirici; `deeper sleep` ve
  `much weaker results` ise pasajın söylemediği yönde çeldirici.
- Doğrulama: geçici bir denetim scriptiyle (`tools/_ac4_kontrol.py`, sonra silindi) her
  dosya için JSON geçerliliği, soru numara aralığı (1–6 / 19–22 / 36–40), `evidence`in
  pasajda **birebir** geçişi, `evidence_locator` doğruluğu, cevabın pasajdaki geçiş sayısı
  (**hepsi tam 1**), sıra kuralı, kelime sınırı, cevap tekrarı, soru kökü ile pasaj
  arasında 6+ kelimelik birebir örtüşme olmaması, `explanation` alanlarının Türkçe olması,
  gövdedeki boşluk numaralarının soru numaralarıyla eşleşmesi, `word_bank` seçenek/
  çeldirici sayısı ve "IELTS" geçmemesi denetlendi. **İlk turda 2 hata çıktı ve
  düzeltildi:** (1) 21. sorunun kökü A11'den "so that any change could be" ifadesini
  birebir taşıyordu → cümle yeniden yazıldı; (2) sıra kuralı denetiminin kendisi hatalıydı
  — 2. ve 3. sorular B paragrafının **aynı uzun cümlesini** kanıt olarak paylaştığı için
  kanıt cümlesinin konumuna bakan kontrol eşitlik görüp hata veriyordu; metinden seçme
  tiplerinde **cevabın kendi konumuna** bakacak şekilde düzeltildi (`soundproof` cümle
  içinde `sound-absorbing`den önce geçiyor, sıra gerçekte doğruydu). Düzeltmeden sonra
  script **hata 0**. Ardından `python tools/dogrula.py`: **şema hatası 0**, okuma sorusu 60
  (AC1–AC4 × 15), pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0.
- Referans PDF'leri: `referans/text/` klasörü bu oturumda da yoktu ve `pdftotext` yine
  çalıştırılamadı. Yönerge kalıpları prompt dosyasındaki üç kalıptan ve AC1–AC3'ün
  yerleşik biçiminden alındı; listeden seçme yönergesi AC2'deki kalıbın aynısı.
- Atlanan/sorun: yok. **OPUS5-10'da 10 paketten 4'ü tamam;** kalan 6 paket GT1, GT2 ve
  4 alıştırma paketi (7, 8, 9, 10 — bunlardan 7. paket iki dosya). Dört Academic testin de
  OPUS5-10 payı (60 soru) bitti; `content/reading/practice/` hâlâ boş.

## OPUS5-10 (5. çalıştırma: GT1 tam testi)
- Tarih: 2026-08-04
- Depo kontrolü: `content/reading/tests/` altında `AC1/`–`AC4/` vardı (15'er soru, tam),
  `GT1/`, `GT2/` ve `content/reading/practice/` yoktu/boştu → çalıştırma listesindeki
  **5. paket (GT1)** sıradaki bitmemiş işti, o yapıldı. **13 soru** üretildi, plandaki
  GT payıyla (15–20, 25–27, 37–40) birebir aynı. (Kullanıcı bu oturumu "4. çalıştırma"
  diye tanımlamıştı; AC3/AC4 oturumlarındaki aynı kayma sürüyor, promptun "sıradaki
  bitmemiş paketi yap" kuralı uygulandı.)
- Üretilen dosyalar:
  - `content/reading/tests/GT1/note-completion.json` — soru 15–20, pasaj **G03** (2. bölüm)
  - `content/reading/tests/GT1/sentence-completion.json` — soru 25–27, pasaj **G03**
  - `content/reading/tests/GT1/summary-completion.json` — soru 37–40, pasaj **G05** (3. bölüm)
- **Seçilen alt tipler ve gerekçe:**
  - 15–20 için **not tamamlama**. AC4 notundaki öneriye uyuldu (GT'de bu aralıkta yalnız
    not/tablo olabiliyor; **GT2'de tablo tamamlama kullanılırsa iki tip de görülmüş olur**).
    G03 bir personel el kitabı: vardiya, mola, giriş çıkış, izin, mesai başlıkları
    *paralel karşılaştırma* değil *ayrı ayrı kurallar* olduğu için tablo zorlamaydı;
    başlıklı madde listesi metnin kendi düzenine oturuyor. Cevaplar A metninin A–B–C–D
    paragraflarına ve B metninin A–B paragraflarına yayıldı, sıra korundu.
  - 25–27 **cümle tamamlama**, `NO MORE THAN TWO WORDS`, yine G03 (plan 2. bölümü şart
    koşuyor). Çakışmayı önlemek için **iş bölümü yapıldı:** notlar A metninin tamamını +
    B metninin izin hakkı/talebi kısmını, cümleler B metninin aralık onayı, mesai ücreti
    ve ayrılışta ödeme kısımlarını hedefliyor. Aynı cümleden iki soru çıkarılmadı.
  - 37–40 için özet tamamlamanın **metinden kelime seçme** alt tipi (`word_bank: null`),
    `ONE WORD ONLY`. GT tarafında henüz alt tip kullanılmamıştı; **GT2'de listeden seçme
    yapılırsa GT dengesi de 1–1 olur** (Academic zaten 2–2). Özet G05'in E–I paragraflarını
    kapsıyor, yani FABLE5-42'nin başlık eşleştirmesi ve FABLE5-40'ın YES/NO/NG'si için
    A–D paragrafları serbest kalıyor.
- Kelime sınırları: 15–20 `NO MORE THAN THREE WORDS AND/OR A NUMBER` (`28 days` sayı
  içerdiği için bu kalıp seçildi; en uzun cevap iki kelime), 25–27 `NO MORE THAN TWO WORDS`
  (hepsi tam iki kelime), 37–40 `ONE WORD ONLY` (hepsi tek kelime). Bütün cevaplar sınıra
  uyuyor. `shift-swap form` tireli olduğu için iki kelime sayılıyor.
- Elenen soru: yok. **Vazgeçilen cevap adayları:** G03'te `four weeks` (hem vardiya
  döngüsünde hem uzun izin ihbarında geçiyor — benzersizlik kuralı), `eleven hours`
  (metinde `eleven hours' rest` biçiminde, kesme işareti yüzünden cevap sınırı tartışmalı
  olurdu), `time off in lieu` (dört kelime, sınırı aşıyor), `staff office` (soru kökünde
  ipucu olarak zaten verildi). G05'te `rice` (çok geçiyor), `income` (D'de iki kez),
  `inedible` (C ve E), `compost/composted` (F ve H'de üç geçiş) elendi; yerlerine tek
  geçişli `peelings`, `refrigerator`, `convenience`, `prevention` seçildi.
- Doğrulama: geçici denetim scriptiyle (`tools/_gt1_kontrol.py`, sonra silindi) üç dosya
  için JSON geçerliliği, numara aralığı (15–20 / 25–27 / 37–40), `evidence`in pasajda
  **birebir** geçişi, cevabın pasajdaki geçiş sayısı (**hepsi tam 1**), sıra kuralı
  (cevabın kendi konumuna göre), kelime sınırı, cevap tekrarı, soru kökü ile pasaj
  arasında 6+ kelimelik birebir örtüşme olmaması, `explanation`ların Türkçe olması,
  `stem_block` boşluk numaralarının soru numaralarıyla eşleşmesi, zorluk çeşitliliği,
  zarf alanlarının tamlığı ve "IELTS" geçmemesi denetlendi. **İlk turda hata 0.**
  Ardından `python tools/dogrula.py`: **şema hatası 0**, okuma sorusu 73 (60 + GT1'in 13'ü),
  pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0.
- G03'ün iç yapısı yüzünden `evidence_locator`a **`text` alanı eklendi** — yani
  text: A, paragraph: C, sentence: 1 biçiminde: G03 iki ayrı el kitabı metninden oluşuyor
  ve her metnin kendi içinde A–D paragrafları var, tek başına paragraf harfi belirsiz
  kalıyordu. **GT2'de G04 için de aynı düzen kullanılmalı.** G05 tek parça olduğu için
  orada eski biçim (`paragraph` + `sentence`) korundu.
- Referans PDF'leri: `referans/text/` klasörü bu oturumda da yoktu. Yönerge kalıpları
  prompt dosyasındaki üç kalıptan ve AC1–AC4'ün yerleşik biçiminden alındı.
- Atlanan/sorun: yok. **OPUS5-10'da 10 paketten 5'i tamam;** kalan 5 paket GT2 ve 4
  alıştırma paketi (7, 8, 9, 10 — 7. paket iki dosya). `content/reading/practice/` hâlâ boş.

## OPUS5-10 (6. çalıştırma: GT2 tam testi)
- Tarih: 2026-08-04
- Depo kontrolü: `AC1`–`AC4` (15'er soru) ve `GT1` (13 soru) tamdı,
  `content/reading/practice/` boştu → çalıştırma listesindeki **6. paket (GT2)** sıradaki
  bitmemiş işti. `content/reading/tests/GT2/` altında **yalnızca `table-completion.json`**
  duruyordu (commit'lenmemiş, `UYARILAR.txt`'deki üç başarısız denemeden kalma):
  15–20 aralığı eksiksiz ve denetimden hatasız geçti, **yeniden üretilmedi, olduğu gibi
  korundu**; eksik olan 25–27 ile 37–40 bu oturumda üretildi. Toplam **13 soru**, plandaki
  GT payıyla (15–20, 25–27, 37–40) birebir aynı.
- Üretilen/korunan dosyalar:
  - `content/reading/tests/GT2/table-completion.json` — soru 15–20, pasaj **G04** (2. bölüm) *(önceki denemeden korundu)*
  - `content/reading/tests/GT2/sentence-completion.json` — soru 25–27, pasaj **G04** *(yeni)*
  - `content/reading/tests/GT2/summary-completion.json` — soru 37–40, pasaj **G06** (3. bölüm) *(yeni)*
- **Seçilen alt tipler ve gerekçe:**
  - 15–20 **tablo tamamlama**. GT1 notundaki öneri uygulandı: GT1 not tamamlama kullandığı
    için GT2'de tablo seçildi, böylece iki GT testinde her iki alt tip de görülüyor.
    G04'ün A metni (staj başvuru rehberi) zaten *aşama → tarih → içerik* biçiminde
    ilerlediği için tablo düzeni metnin kendi yapısına oturuyor.
  - 25–27 **cümle tamamlama**, `NO MORE THAN TWO WORDS`, yine G04 (plan 2. bölümü şart
    koşuyor). Çakışmayı önlemek için **metin bazlı iş bölümü:** tablo soruları yalnızca
    **A metnini** (staj rehberi), cümle soruları yalnızca **B metnini** (uzaktan çalışma
    politikası) hedefliyor. Aynı cümleden iki soru çıkarılmadı.
  - 37–40 için özet tamamlamanın **listeden kelime seçme** alt tipi (`word_bank` dolu,
    9 seçenek A–I, 4 cevap + **5 çeldirici**), `word_limit: null`. GT1 metinden seçme
    kullanmıştı; böylece **GT dengesi 1–1** oldu (Academic zaten 2–2: AC1/AC3 metinden,
    AC2/AC4 listeden). Özet G06'nın **E–I** paragraflarını kapsıyor, yani başlık
    eşleştirmesi (28–32) ve YES/NO/NG (33–36) için A–D paragrafları serbest kalıyor.
- Kelime sınırları: 15–20 `NO MORE THAN THREE WORDS AND/OR A NUMBER` (en uzun cevap
  `ten working days`, üç kelime), 25–27 `NO MORE THAN TWO WORDS` (`home-office equipment`
  tireli olduğu için iki kelime sayılıyor), 37–40 sınırsız (liste tipinde `word_limit`
  uygulanmaz). Bütün cevaplar sınıra uyuyor.
- Elenen soru: yok. **Vazgeçilen cevap adayları:** G04'te `ten weeks` (A metninde dört
  kez geçiyor — benzersizlik kuralı), `core hours` (B metninde üç kez), `line manager`
  ve `client-facing` (21–24 çoktan seçmeliye bırakıldı, FABLE5-41'in malzemesi kalsın
  diye), `instant messaging` (aynı cümlede core hours ile birlikte, 26 ile aynı maddeye
  yakın düşüyordu). G06'da özet çeldiricileri `roughly half` ve `the main driver`
  bilerek 37. boşluğa **dilbilgisel olarak** uyacak biçimde yazıldı (yalnız anlam eler);
  `contradictory` / `easily explained` 38 ve 40 için, `proof of a cause` 39 ve 40 için
  aynı işi görüyor.
- Doğrulama: geçici denetim scriptiyle (`tools/_gt2_kontrol.py`, sonra silindi) üç dosya
  için JSON geçerliliği, numara aralığı (15–20 / 25–27 / 37–40), `evidence`in pasajda
  **birebir** geçişi, cevabın pasajdaki geçiş sayısı (metinden seçme tiplerinde **hepsi
  tam 1**), sıra kuralı, kelime sınırı, cevap tekrarı, `word_bank` bütünlüğü (harf sırası,
  alfabetik dizim, çeldirici sayısı, cevabın bankada bulunması), gövde boşluk numaralarının
  soru numaralarıyla eşleşmesi, soru kökü ile pasaj arasında 6+ kelimelik birebir örtüşme
  olmaması, `explanation`ların Türkçe olması, zorluk çeşitliliği, zorunlu alanların
  tamlığı ve "IELTS" geçmemesi denetlendi. **İlk turda hata 0.** Ardından
  `python tools/dogrula.py`: **şema hatası 0**, okuma sorusu 86 (60 + GT1 13 + GT2 13),
  pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0.
- `evidence_locator`da GT1'deki düzen sürdürüldü: G04 iki ayrı metinden oluştuğu ve her
  metnin kendi içinde A–D paragrafları bulunduğu için `text` + `paragraph` + `sentence`;
  G06 tek parça olduğu için `paragraph` + `sentence`.
- Referans PDF'leri: `referans/text/` klasörü bu oturumda da yoktu. Yönerge kalıpları
  prompt dosyasındaki üç kalıptan ve AC1–AC4 + GT1'in yerleşik biçiminden alındı.
- Atlanan/sorun: yok. **OPUS5-10'da 10 paketten 6'sı tamam — bütün tam testler bitti
  (86 soru: AC×4 = 60, GT×2 = 26).** Kalan 4 paket yalnızca alıştırma (7, 8, 9, 10 —
  7. paket iki dosya, toplam 65 soru). `content/reading/practice/` hâlâ boş.
  **Sıradaki oturum için not:** 7. pakette (cümle + not/tablo tamamlama, 15+15) tam
  testlerde kullanılan cümlelerden kaçınmak için AC1–AC4 ve GT1–GT2'nin
  `sentence-completion` / `note-completion` / `table-completion` / `flow-chart-completion`
  dosyalarındaki `evidence` alanları önce topluca okunmalı.

## OPUS5-10 (7. çalıştırma: alıştırma — cümle tamamlama + not tamamlama)

- Tarih: 2026-08-04
- Depo kontrolü: `content/reading/tests/` altındaki altı tam test (AC1–AC4 15'er, GT1–GT2
  13'er = 86 soru) tamdı, `content/reading/practice/` **boştu** → çalıştırma listesindeki
  **7. paket** sıradaki bitmemiş işti. Bu paket iki dosya üretir, toplam **30 soru**.
- Üretilen dosyalar:
  - `content/reading/practice/sentence-completion.json` — soru **1–15**, pasajlar
    **A01, A02, A03, A04, A05** (her birinden 3 soru)
  - `content/reading/practice/note-completion.json` — soru **1–15**, pasajlar
    **A06, A07, A08, A09, A12** (her birinden 3 soru)
- **Alt tip kararı:** plan D bölümü bu satırı "not / tablo tamamlama" diye tanımlıyor;
  **not tamamlama** seçildi. Gerekçe: tam testlerde tablo tamamlama zaten iki kez
  (AC3/A07, GT2/G04) ve akış şeması bir kez (AC2/A04) kullanıldı, not tamamlama ise
  yalnızca AC1, AC4 ve GT1'de geçiyordu; ayrıca bu alıştırma dosyası **beş ayrı pasajı**
  kapsadığı için madde işaretli not blokları tek bir tabloya göre çok daha doğal duruyor.
  `stem_block` içinde her pasaj için ayrı başlıklı bir not bloğu var
  (`Passage A06 — <başlık>` biçiminde), boşluk numaraları dosya boyunca 1'den 15'e
  kesintisiz ilerliyor.
- **Pasaj seçimi ve çakışma önleme:** iki dosya **hiçbir pasajı paylaşmıyor**
  (cümle tamamlama A01–A05, not tamamlama A06–A09 + A12). Pasaj başına 3 soru — kuraldaki
  "en fazla 4" sınırının altında; böylece 8, 9 ve 10. paketlere yer kaldı. Tam testteki
  soruyla aynı bilgiyi hedeflememek için her pasajda **tam testin dokunmadığı paragraflar**
  seçildi:
  - A01: AC1 B–F kullanmıştı → alıştırma A, G, H
  - A02: AC1 C, D, F(4. cümle), H kullanmıştı → alıştırma B, F(2. cümle), G
  - A03: AC1 B, D, F, G, H kullanmıştı → alıştırma A, C, E
  - A04: AC2 B, C, D, E kullanmıştı → alıştırma A, F, H
  - A05: AC2 C, D, E, G kullanmıştı → alıştırma A, F, H
  - A06: AC2 C, D, E, F, G kullanmıştı → alıştırma A, B, H
  - A07: AC3 B, C, D, E, F kullanmıştı → alıştırma A, G, H
  - A08: AC3 B, C, F, G kullanmıştı → alıştırma A, D, H
  - A09: AC3 C, D, E, F, G kullanmıştı → alıştırma A, B, H
  - A12: AC4 B, C, E, F kullanmıştı → alıştırma D, G, H
- **Sıra kuralı** her pasaj bloğu içinde ayrı ayrı uygulandı (aynı pasajın üç sorusu
  metindeki geçiş sırasına göre); dosya düzeyinde pasajlar da kimlik sırasında.
- Kelime sınırı: **her iki dosyada da `NO MORE THAN TWO WORDS`**. Rakamla yazılan sayılar
  ve tireli kelimeler tek kelime sayıldı: `47`, `500`, `1952`, `90 kilometres`,
  `12 December`, `forty years`, `brand-new associations`. En uzun cevap iki kelime.
- **Alıştırma dosyalarının şeması:** `test_id: null`, `practice: true`, grup düzeyinde
  `passage_id: null` (dosya birden çok pasajı kapsadığı için) ve **item düzeyinde
  `passage_id`** dolu. Cümle tamamlamada `stem_block: null`, ilk sorularda hangi pasajın
  okunacağını belirten `Questions 1-3 refer to Passage A01.` biçiminde bir başlangıç var.
- **Elenen/değiştirilen sorular:** iki aday denetimde düştü ve yenisiyle değiştirildi.
  (1) A04 için `Voyager 2` cevabı — ifade pasajda iki kez geçiyor (F ve H paragrafları),
  benzersizlik kuralına takıldı; yerine aynı paragrafın 3. cümlesinden `forty years` üretildi.
  (2) A01 `concrete cube`, A12 `consolidation`, A07 `narwhals`, A05 `spelt`, A03 `450 miles`
  adayları da aynı sebeple (pasajda birden çok geçiş) hiç yazılmadan elendi. Ayrıca A05'te
  `James Mellaart` cevabı, telif kuralındaki "gerçek kişi adı kullanma" ilkesine yaklaştığı
  için bilerek terk edildi, yerine `1952` alındı.
- **Soru kökü ↔ pasaj örtüşmesi** otomatik denetlendi (6+ kelimelik birebir örtüşme yasağı);
  iki not maddesi bu yüzden yeniden yazıldı: A07'nin tür listesi sırası değiştirildi
  (`orcas, bottlenose dolphins, Asian elephants, a few great apes...`) ve A08'in deprem
  merkezi maddesi `north of Yakutat on the coast` biçimine çevrildi.
- Doğrulama: geçici denetim scriptiyle (`tools/_p7_kontrol.py`, sonra silindi) iki dosya
  için JSON geçerliliği, soru sayısı (15+15), numara aralığı (1–15), `evidence`in pasajda
  **birebir** geçişi, `evidence_locator`ın (paragraf + kaçıncı cümle) o cümleye **birebir**
  denk gelmesi, cevabın pasajdaki geçiş sayısı (**hepsi tam 1**), cevabın kendi
  `evidence`ı içinde bulunması, kelime sınırı, `accepted_variants` bütünlüğü, pasaj içi
  sıra kuralı, cevap tekrarı, pasaj başına soru sayısı (≤4), tam testlerdeki `evidence`
  cümleleriyle çakışma, soru kökü–pasaj örtüşmesi, `explanation`ların Türkçe ve dolu olması,
  zorluk çeşitliliği, zorunlu alanların tamlığı, `stem_block` boşluk numaralarının soru
  numaralarıyla eşleşmesi, her `prompt`un `stem_block` içinde geçmesi ve "IELTS" geçmemesi
  denetlendi. Son turda **hata 0**. Ardından `python tools/dogrula.py`: **şema hatası 0**,
  okuma sorusu 116 (tam test 86 + alıştırma 30), pasaj lisansı eksik 0, görünür metinde
  IELTS 0, yasak kaynak 0.
- Atlanan/sorun: yok. **OPUS5-10'da 10 paketten 7'si tamam** (86 tam test + 30 alıştırma =
  116 soru). Kalan 3 paket: **8** (özet tamamlama, 15), **9** (kısa cevap, 10),
  **10** (diyagram/plan etiketleme, 10) — toplam 35 soru.
  **Sıradaki oturumlar için not:**
  - 8. paket (özet tamamlama, 15): tam testlerde AC1/A03 ve GT1/G05 *metinden seçme*,
    AC2/A06, AC4/A12, GT2/G06 *listeden seçme* kullandı. Alıştırmada iki alt tipin ikisini
    de göstermek iyi olur (ör. 8 + 7 bölüşümü). Henüz **hiç dokunulmamış pasajlar: A10, A11
    ve bütün GT metinleri G01, G02** — özet tamamlama için A10/A11 ve G05/G06 uygun uzunlukta.
  - 10. paket (diyagram etiketleme): pasajın somut bir nesne/süreç/mekân anlatması şart.
    Havuzda buna en uygun olanlar **A03** (Maug kalderası + vent'ler), **A04** (Uranüs iç uydu
    yörüngeleri), **A08** (buzul üzerindeki heyelan/uydu görüntüleme düzeni) ve **A09**
    (Herculaneum'un piroklastik akıntı altında gömülmesi). SVG'ler prompt kurallarına göre
    tek parça, sabit renksiz ve `viewBox`'lı olmalı.

## OPUS5-10 (8. çalıştırma: alıştırma — özet tamamlama)

- Tarih: 2026-08-04
- Depo kontrolü: altı tam test (AC1–AC4 15'er, GT1–GT2 13'er = 86 soru) ve
  `content/reading/practice/` altındaki iki dosya (`sentence-completion.json`,
  `note-completion.json` — 15'er soru) tamdı → çalıştırma listesindeki **8. paket
  (alıştırma: özet tamamlama, 15 soru)** sıradaki bitmemiş işti, o yapıldı.
- Üretilen dosya: `content/reading/practice/summary-completion.json` — soru **1–15**,
  pasajlar **A10 (1–4), A11 (5–8), G05 (9–12), G06 (13–15)**.
- **Pasaj seçimi zorunluluktan geldi:** "aynı pasajdan en fazla 4 alıştırma sorusu" kuralı
  gereği A01–A09 ve A12'de yalnızca 1'er kontenjan kalmıştı (7. pakette her birinden 3 soru
  çıkmıştı). Özet tamamlama bir pasajdan **bitişik 3–4 boşluk** ister, tek boşlukla özet
  kurulamaz; bu yüzden alıştırmada hiç kullanılmamış olan **A10, A11, G05, G06** seçildi.
  A10 ve A11 4'er soruyla kontenjanını doldurdu, G05 4, G06 3 soru aldı (G06'da 1 kontenjan
  kaldı). **9. ve 10. paketler için kalan kontenjan:** A01–A09 + A12'de 1'er, G06'da 1,
  G01–G04'te 4'er soru.
- **Alt tip kararı — hepsi metinden kelime seçme (`word_bank: null`):** prompt şeması
  "bir dosya = bir soru grubu (aynı yönergeyi paylaşan sorular)" diyor ve `instructions`,
  `word_limit`, `word_bank` alanlarının üçü de **grup düzeyinde**; tek dosyada iki alt tipi
  karıştırmak bu şemayı bozardı (7. çalıştırma notundaki "8+7 bölüşümü" önerisi bu yüzden
  uygulanmadı). Metinden seçme tercih edildi çünkü (a) tam testlerde listeden seçme 3
  (AC2, AC4, GT2), metinden seçme 2 (AC1, GT1) kez kullanılmıştı — bu dosyayla denge 3–3
  oldu; (b) alıştırmanın asıl öğrettiği beceri cevabın pasajda **birebir** bulunması,
  öteki iki alıştırma dosyasıyla da tutarlı.
- **Tam testle çakışma önleme** (her pasajda testin dokunmadığı paragraflar seçildi):
  - A10: AC4 not tamamlama A, B, C, F, H kullanmıştı → alıştırma **D, E, F(2. cümle), G**
  - A11: AC4 cümle tamamlama C, D, E, H kullanmıştı → alıştırma **A, B, F, G**
  - G05: GT1 özeti E–I kullanmıştı → alıştırma **B, C, D**
  - G06: GT2 özeti F–I kullanmıştı → alıştırma **B, C, D**
  Denetim, `evidence` cümlelerinin altı tam testteki hiçbir `evidence` ile birebir
  çakışmadığını da doğruladı.
- **Şema kararı — `module: "both"`:** dosya hem Academic (A10, A11) hem General (G05, G06)
  pasajı kapsıyor; `99-teslim-formati.md` bu alan için `academic · general · both`
  değerlerine izin verdiğinden `both` yazıldı. Öteki alıştırma alanları 7. paketteki
  düzeni izliyor: `test_id: null`, `practice: true`, grup düzeyinde `passage_id: null`,
  **item düzeyinde `passage_id`** dolu. `stem_block` dört ayrı özet paragrafından oluşuyor,
  her biri `Passage <kimlik> — <başlık>` başlığı taşıyor, boşluk numaraları 1'den 15'e
  kesintisiz ilerliyor.
- Kelime sınırı: **`NO MORE THAN TWO WORDS`** (öteki iki alıştırma dosyasıyla aynı).
  Sayısal cevap bilinçli olarak kullanılmadı, böylece "AND/OR A NUMBER" kalıbına gerek
  kalmadı. Tireli kelimeler tek kelime sayıldı (`five-point`). En uzun cevaplar iki kelime:
  `safe limits`, `software engineers`, `digital scales`.
- **Sıra kuralı** her pasaj bloğu içinde ayrı ayrı uygulandı: A10 D3→E1→F2→G3,
  A11 A2→B2→F3→G2, G05 B1→B2→C2→D2, G06 B3→C3→D3.
- Elenen soru: yok. **Vazgeçilen cevap adayları** (hepsi benzersizlik kuralına takıldı,
  yani pasajda birden çok kez geçiyor): A10'da `ranking` (D ve H), `concentration`
  (C'deki "carbon dioxide concentration" ile çakışıyor), `flow` (C ve E), `code commits`
  (C ve G), `energy` (C ve G); A11'de `vigour` (E, F, H), `vitality` (E ve G), `half`
  (A ve G), `Finland` (A ve B); G05'te `regency` (A ve C), `Cibinong` / `Sukajaya`
  (A ve D), `income` (D'de iki kez), `eight` ("eight consecutive days" ve I'deki
  "eight-day snapshot"); G06'da `income` (çok geçiyor), `religious` (C ve D).
  Ayrıca G05'te `peels` adayı, GT1 testinde `peelings` cevabı kullanıldığı için
  karışıklık yaratmasın diye bırakıldı, yerine `eggshells` alındı.
- Doğrulama: geçici denetim scriptiyle (`tools/_p8_kontrol.py`, sonra silindi) JSON
  geçerliliği, soru sayısı (15), numara aralığı (1–15), her `prompt`un `stem_block` içinde
  geçmesi ve boşluk numarasının eşleşmesi, `evidence`in pasajda **birebir** geçişi,
  `evidence_locator`ın (paragraf + kaçıncı cümle) o cümleye birebir denk gelmesi, cevabın
  pasajdaki geçiş sayısı (**hepsi tam 1**), cevabın kendi `evidence`ı içinde bulunması,
  kelime sınırı, `accepted_variants` bütünlüğü, pasaj içi sıra kuralı, cevap tekrarı,
  **alıştırma genelinde pasaj başına soru sayısı (≤4)**, tam testlerdeki `evidence`
  cümleleriyle çakışma, soru kökü ile pasaj arasında 6+ kelimelik birebir örtüşme
  olmaması, `explanation`ların Türkçe ve dolu olması, zorluk çeşitliliği (easy 5,
  medium 7, hard 3) ve "IELTS" geçmemesi denetlendi. **İlk turda hata 0.** Ardından
  `python tools/dogrula.py`: **şema hatası 0**, okuma sorusu 131 (tam test 86 + alıştırma
  45), pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0.
- Referans PDF'leri: `referans/text/` klasörü bu oturumda da yoktu; yönerge kalıpları
  prompt dosyasındaki üç kalıptan ve AC1–GT2'nin yerleşik biçiminden alındı
  (özet için "Complete the summaries below." çoğul yazıldı, çünkü dosyada dört ayrı özet var).
- Atlanan/sorun: yok. **OPUS5-10'da 10 paketten 8'i tamam** (86 tam test + 45 alıştırma =
  131 soru). Kalan 2 paket: **9** (kısa cevap, 10) ve **10** (diyagram/plan etiketleme, 10).
  **Sıradaki oturumlar için not:** kısa cevapta pasaj başına kalan kontenjan dar
  (A01–A09 + A12'de 1'er, G06'da 1); rahat çalışma alanı **G01–G04** (her birinde 4
  kontenjan, alıştırmada hiç kullanılmadılar). 10. paketin diyagram adayları için
  7. çalıştırma notundaki liste (A03, A04, A08, A09) geçerliliğini koruyor, ancak
  bu pasajların her birinde yalnız 1 alıştırma kontenjanı kaldığı için **10 diyagram
  sorusu tek pasajdan çıkarılamaz**; G01–G04'ün somut mekân/plan anlatan metinleri
  (ör. spor merkezi, geri dönüşüm düzeni, fabrika vardiya akışı) plan etiketleme için
  değerlendirilmeli.

## OPUS5-10 (9. çalıştırma: alıştırma — kısa cevap)

- Tarih: 2026-08-04
- Depo kontrolü: altı tam test (AC1–AC4 15'er, GT1–GT2 13'er = 86 soru) ve
  `content/reading/practice/` altındaki üç dosya (`sentence-completion`, `note-completion`,
  `summary-completion` — 15'er soru) tamdı → çalıştırma listesindeki **9. paket
  (alıştırma: kısa cevap, 10 soru)** sıradaki bitmemiş işti, o yapıldı.
- Üretilen dosya: `content/reading/practice/short-answer.json` — soru **1–10**,
  pasajlar **A01, A02, A03, A04, A05, A06, A07, A08, A09, A12** (her birinden **1 soru**).
- **Pasaj seçimi — kasıtlı bir denge kararı:** "aynı pasajdan en fazla 4 alıştırma sorusu"
  kuralı gereği elde kalan kontenjan şuydu: A01–A09 + A12'de 1'er (7. paket her birinden
  3 soru almıştı), G06'da 1, G01–G04'te 4'er. Kısa cevap tipi her soruyu **bağımsız**
  sorduğu için 1'er kontenjanla çalışmaya en uygun tip odur; buna karşılık **10. paket
  (diyagram/plan etiketleme)** tek bir görsel altında 2–4 numaralı etiket ister, yani
  aynı pasajdan birkaç soru çıkarabilmek zorundadır. Bu yüzden akademik pasajların kalan
  1'er kontenjanı bu pakete verildi ve **G01–G04'ün 16 kontenjanı bütünüyle 10. pakete
  bırakıldı**. Sonuç: alıştırmada A01–A12 ve G05 4/4 dolu, G06'da 1, G01–G04'te 4'er
  kontenjan kaldı — 10 diyagram sorusu için fazlasıyla yeterli.
- **Tam testle ve öteki alıştırmalarla çakışma önleme:** her soru, o pasajda ne tam testin
  ne de 7./8. paketin dokunduğu bir **cümleden** üretildi (A01 D2, A02 B1, A03 C2,
  A04 F2, A05 C1, A06 H1, A07 B2, A08 D1, A09 D2, A12 D3). Denetim, hiçbir `evidence`
  cümlesinin altı tam testteki ya da öteki üç alıştırma dosyasındaki bir `evidence` ile
  birebir çakışmadığını doğruladı.
- **Alt tip / yönerge kararı:** kısa cevabın tek yönergesi var; `NO MORE THAN THREE WORDS
  AND/OR A NUMBER` seçildi, çünkü dosyada tarih (`24 January 1986`), yaş (`8,400 years`)
  ve üç kelimelik terimler (`transactive memory system`, `scanning electron microscopy`)
  birlikte bulunuyor. Öteki alıştırma dosyaları `NO MORE THAN TWO WORDS` kullanıyordu;
  böylece alıştırma seti üç kelime sınırının ikisini de gösteriyor. Tireli kelimeler
  (`30-minute`) tek kelime sayıldı.
- **Şema:** 7. ve 8. paketteki düzen sürdürüldü — `test_id: null`, `practice: true`,
  grup düzeyinde `passage_id: null`, **item düzeyinde `passage_id`** dolu,
  `stem_block: null` (kısa cevapta zorunlu), `word_bank: null`, `visual: null`.
  Her `prompt`, hangi pasajın okunacağını belirten `Question n refers to Passage Axx.`
  cümlesiyle başlıyor (7. paketteki `Questions 1-3 refer to ...` kalıbının tekil hâli).
  `module: "academic"` — dosyadaki on pasajın hepsi akademik.
- **Sıra kuralı** bu dosyada kendiliğinden sağlanıyor: her pasajdan tek soru var, sorular
  da pasaj kimliği sırasında diziliyor.
- Elenen soru: yok. **Vazgeçilen cevap adayları:** A01'de `concrete cube` ve `seven`
  (birden çok geçiş / 7. paketteki `seventh` ile karışma), A03'te `450 miles` ve
  `Fertile Crescent` (pasajda iki kez), A04'te `Voyager 2` (iki kez) ve SETI Institute
  (gerçek kişi adına bağlı olduğu için), A05'te `hexaploid`, `spelt`, `charred` (çok
  geçiş) ve `James Mellaart` (gerçek kişi adı kuralı), A06'da `977` (sayısal cevap
  fazlalaşmasın diye) ve F paragrafındaki yüzdeler (AC2'nin 39. sorusuyla aynı bilgiye
  fazla yakın), A08'de `7.0` ve `700` (700 pasajda üç kez), A12'de `Stage 2 sleep`
  (AC4'ün 40. sorusunun kanıt cümlesine bitişik olduğu için).
- Doğrulama: geçici denetim scriptiyle (`tools/_p9_kontrol.py`, sonra silindi) JSON
  geçerliliği, zarf alanlarının tamlığı, `stem_block`ın null olması, soru sayısı (10),
  numara aralığı (1–10), `evidence`in pasajda **birebir** geçişi, `evidence_locator`ın
  (paragraf + kaçıncı cümle) o cümleye birebir denk gelmesi, cevabın kendi `evidence`ı
  içinde bulunması, cevabın pasajdaki geçiş sayısı (**hepsi tam 1**), kelime sınırı
  (≤3 kelime), `accepted_variants` bütünlüğü, cevap tekrarı, sıra kuralı, **alıştırma
  genelinde pasaj başına soru sayısı (≤4)**, tam test ve öteki alıştırma dosyalarındaki
  `evidence` cümleleriyle çakışma, soru kökü ile pasaj arasında 6+ kelimelik birebir
  örtüşme olmaması, `explanation`ların Türkçe ve dolu olması, zorluk çeşitliliği
  (easy 4, medium 4, hard 2) ve "IELTS" geçmemesi denetlendi. **İlk turda hata 0.**
  Ardından `python tools/dogrula.py`: **şema hatası 0**, okuma sorusu 141 (tam test 86 +
  alıştırma 55), pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0.
- Referans PDF'leri: `referans/text/` klasörü bu oturumda da yoktu; kısa cevap yönergesi
  prompt dosyasındaki üç kalıptan (`NO MORE THAN THREE WORDS AND/OR A NUMBER`) ve
  AC1–GT2'nin yerleşik biçiminden alındı.
- Atlanan/sorun: yok. **OPUS5-10'da 10 paketten 9'u tamam** (86 tam test + 55 alıştırma =
  141 soru). Kalan tek paket: **10** (diyagram / plan etiketleme, 10 soru).
  **Sıradaki oturum için not:** kontenjan yalnızca **G01–G04'te 4'er** ve **G06'da 1**;
  akademik pasajların hepsi doldu. Yani 10 diyagram sorusu G01–G04'ten çıkarılmalı
  (ör. dört ayrı görsel, her birinde 2–3 numaralı etiket). Bu metinler somut mekân ve
  düzen anlatıyor: G01 kütüphane/spor merkezi/geri dönüşüm düzeni, G02 bisiklet kiralama
  noktaları, festival alanı, bahçe parselleri ve havuz seansları, G03 fabrika vardiya ve
  giriş-çıkış akışı, G04 staj başvuru aşamaları ve uzaktan çalışma düzeni — plan/akış
  etiketlemesi için uygun. SVG'ler prompt kurallarına göre tek parça, sabit renksiz,
  `viewBox`'lı ve numaralı kutulu olmalı; `question_type` alanı `diagram_labelling`,
  ek zorunlu alan `visual`.

## OPUS5-10 (10. çalıştırma: alıştırma — diyagram / plan etiketleme)

- Tarih: 2026-08-04
- Depo kontrolü: altı tam test (AC1–AC4 15'er, GT1–GT2 13'er = 86 soru) ve
  `content/reading/practice/` altındaki dört dosya (`sentence-completion`,
  `note-completion`, `summary-completion` 15'er, `short-answer` 10) tamdı →
  çalıştırma listesindeki **10. paket (alıştırma: diyagram / plan etiketleme, 10 soru)**
  tek kalan işti, o yapıldı. **OPUS5-10 böylece bitti: 86 + 65 = 151 soru.**
- Üretilen dosya: `content/reading/practice/diagram-labelling.json` — soru **1–10**,
  pasajlar **G01 (1–3), G02 (4–5), G03 (6–8), G04 (9–10)**.
- **Pasaj seçimi:** 9. çalıştırmanın bilinçli kararı gereği akademik pasajların
  kontenjanı dolmuştu; elde yalnız G01–G04 (4'er) ve G06 (1) vardı. Dördü de bu pakete
  girdi, G06'ya dokunulmadı (özet tamamlamada bitişik boşluk gerektiren tek pasaj payı
  olarak bırakmanın anlamı kalmadı, ama tek soruluk bir beşinci diyagram gereksizdi).
  Alıştırma genelinde pasaj başına soru sayısı: A01–A12 ve G05 4/4, G01 3, G02 2, G03 3,
  G04 2, G06 3 — **hiçbiri 4'ü aşmıyor**.
- **Tam testle çakışma önleme:** G01 ve G02'ye OPUS5-10'un tam test payı hiç dokunmamıştı
  (GT1/GT2'nin 15–20, 25–27, 37–40 soruları G03/G04/G05/G06'dan geliyor), bu yüzden bu
  ikisinde serbest seçim yapıldı. G03'te GT1'in kullandığı cümleler (A metni A/3, B/5,
  C/1, D/1; B metni A/1, B/2, B/5, C/1, D/2) dışarıda bırakıldı; diyagram A metninin
  **A/1, A/2 ve B/4** cümlelerinden kuruldu. G04'te GT2'nin kullandığı A metni tümüyle
  ve B metninin A/1, B/5, D/2 cümleleri dışarıda bırakıldı; diyagram B metninin
  **B/2 ve B/4** cümlelerinden kuruldu. Denetim, hiçbir `evidence` cümlesinin öteki
  dokuz soru dosyasındaki bir `evidence` ile birebir çakışmadığını doğruladı.
- **Dört ayrı görsel, tek `visual` alanı:** prompt şeması `visual`ı grup düzeyinde
  tanımlıyor, ama 10 soru dört ayrı pasajdan geliyor. Şemayı bozmamak için **tek bir SVG
  tuvali** üretildi; içinde yatay çizgilerle ayrılmış dört bölüm var (Diagram A/B/C/D),
  her bölümün başlığında hangi pasaja ait olduğu yazıyor. Boşluk numaraları tuval boyunca
  1'den 10'a kesintisiz ilerliyor ve her numara hem SVG'de hem ilgili `prompt`ta geçiyor.
- **Seçilen görseller ve gerekçe** (pasaj somut bir nesne/süreç/mekân anlatmalı kuralı):
  - **A — Elm Court atık akışı (G01):** binadan çıkan üç atık akımının şeması; boşluklar
    çöp alanının arkasındaki blok, takvimin asıldığı yer, büyük eşya toplamasının
    ayarlandığı birim.
  - **B — Millbrook bisiklet kiralama (G02):** yerleştirme istasyonu direkleri, bisiklet
    ve kasklı sürücü çizimi; boşluklar istasyonun adı ve sürücünün kendi getirmesi
    gereken parça.
  - **C — Fernbridge iş günü (G03):** 6.00–22.00 zaman çizgisi; vardiya çubukları, çekirdek
    saat kuşağı ve mola kutuları. En "gerçek diyagram" duran bölüm bu.
  - **D — Cedarline evden çalışma düzeni (G04):** masa, dizüstü, yönlendirici, telefon;
    boşluklar izin verilen en düşük bağlantı hızı ve çekirdek saatlerde yanıt verilecek
    kanal.
  - Yalnızca `rect`, `circle`, `line`, `path`, `polygon`, `text` kullanıldı; `viewBox`
    var, sabit `width`/`height` yok, renkler yalnız `#000`/`#fff`/`none`, yazı
    `font-size="12"`, `font-family="sans-serif"`. `alt` alanı Türkçe ve her boşluğun ne
    sorduğunu anlatıyor.
- Kelime sınırı: **`NO MORE THAN THREE WORDS AND/OR A NUMBER`** — tek sayısal cevap
  (`10 Mbps`) yüzünden sayı içeren kalıp seçildi. En uzun cevap iki kelime; `15-minute`
  tireli olduğu için tek kelime sayılıyor.
- **Sıra kuralı** her pasaj bloğu içinde ayrı ayrı uygulandı: G01 D1→D2→D4,
  G02 A1→A3, G03 A/A1→A/A2→A/B4, G04 B/B2→B/B4; bölümler de pasaj kimliği sırasında.
- Elenen soru: yok. **Vazgeçilen cevap adayları:** G01'de `Monday` / `Tuesdays and Fridays`
  (gün adları A ve E metinlerinde de geçiyor, benzersizlik kuralı); G02'de `£350` ve `£90`
  (bir tuvalde sayısal cevap yığılmasın diye) ve `lane swimming` (`lane sessions` ile aynı
  boşluğa savunulabilir ikinci bir cevap üretiyordu); G03'te `late` (pasajda 5 kez:
  `late shift`, `lateness`, `no later than`), `10-minute` ve `30-minute` (üç mola süresinden
  ikisi aynı anda sorulunca çeldirici değil kafa karışıklığı oluyordu — ikisi de şemada
  **verili** bırakıldı, yalnız `15-minute` soruldu), `four weeks` (iki yerde); G04'te
  `laptops` (üçüncü bir masaüstü etiketi şemayı kalabalıklaştırıyordu), `core hours`
  (6. sorunun cevabı olduğu için aynı cevabın iki kez çıkmaması adına), `client-facing`
  ve `ten weeks` (FABLE5-41'in 21–24 çoktan seçmeli malzemesi kalsın diye).
- Doğrulama: geçici denetim scriptleriyle (`tools/_p10_uret.py`, `tools/_p10_kontrol.py`,
  `tools/_p10_ortusme.py` — üçü de silindi) JSON geçerliliği, zarf alanlarının tamlığı,
  `stem_block`/`word_bank`ın null olması, soru sayısı (10), numara aralığı (1–10), her
  boşluk numarasının hem `prompt`ta hem SVG'de bulunması, `evidence`in pasajda **birebir**
  geçişi, `evidence_locator`ın (metin + paragraf + kaçıncı cümle) o cümleye birebir denk
  gelmesi, cevabın kendi `evidence`ı içinde bulunması, cevabın pasajdaki geçiş sayısı
  (**hepsi tam 1**), kelime sınırı, `accepted_variants` bütünlüğü, cevap tekrarı, pasaj içi
  sıra kuralı, alıştırma genelinde pasaj başına soru sayısı (≤4), öteki dokuz soru
  dosyasındaki `evidence` cümleleriyle çakışma, soru kökü–pasaj örtüşmesi,
  `explanation`ların Türkçe ve dolu olması, zorluk çeşitliliği (easy 4, medium 4, hard 2),
  "IELTS" geçmemesi; ayrıca **SVG'ye özel**: XML olarak ayrıştırılabilirlik, izinli eleman
  listesi, `viewBox` varlığı, sabit `width`/`height` olmaması, izinli renkler, metinlerin
  tuval ve kutu sınırlarını taşmaması, kutuların üst üste binmemesi. İlk turda çıkan
  hatalar düzeltildi: (1) açıklamalar Türkçe karakter içermiyordu, hepsi yeniden yazıldı;
  (2) B ve D bölümlerinde etiket metinleri kutularını taşıyordu, düzen yeniden
  yerleştirildi (etiket kutuları çizimin sağına/altına alındı, kılavuz çizgiler çizimin
  üstünden geçmeyecek şekilde yönlendirildi); (3) 4. sorunun kökü ile pasaj arasında
  5 kelimelik (`from any of the twelve`) örtüşme vardı, cümle yeniden yazıldı; (4) SVG'de
  `the colour-coded calendar in the` ifadesi birebir kopyaydı, `posted in` ile kırıldı.
  Kalan tek 5 kelimelik örtüşme saat ifadeleri (`10 a.m. to 4 p.m.`, `2 p.m. to 10 p.m.`)
  — bunlar veri, parafraze edilemez, bilerek bırakıldı. Son turda **hata 0**.
  Ardından `python tools/dogrula.py`: **şema hatası 0**, okuma sorusu **151**
  (tam test 86 + alıştırma 65), pasaj lisansı eksik 0, görünür metinde IELTS 0,
  yasak kaynak 0.
- Denetim scriptindeki cümle bölücü hakkında not: pasajlarda `a.m.` / `p.m.` ve ondalık
  sayılar (`37.5`, `1.30`) var; naif `.`-bölücü `evidence_locator` doğrulamasını yanlış
  yere düşürüyor. Bölme yalnız noktalama **büyük harfle** devam ediyorsa yapılmalı,
  ondalık sayılar korunmalı. **Sonraki oturumlar GT metinleriyle çalışırken bunu
  hatırlasın.**
- Atlanan/sorun: yok. **OPUS5-10 TAMAM — 10 paketin 10'u da bitti: 151 soru**
  (AC1–AC4 15'er, GT1–GT2 13'er, alıştırma 15+15+15+10+10). Okuma tarafında kalan işler
  başka promptlarda: OPUS5-11 (bilgi eşleştirme), FABLE5-40/41/42. `ilerleme.txt` 14'e
  çekildi, `DURUM.txt` yeniden üretildi (88 çalıştırmanın 14'ü).

## OPUS5-11 (1. çalıştırma: AC1–AC4 bilgi eşleştirme)
- Tarih: 2026-08-04
- Depoda hiçbir `matching-information.json` yoktu → prompt dosyasındaki üç paketten
  bitmemiş ilki **1. paket (AC1 + AC2 + AC3 + AC4)** idi, o yapıldı.
  **20 soru** (4 test × 5) üretildi, plandaki 27–31 aralığıyla birebir aynı.
- Üretilen dosyalar:
  - `content/reading/tests/AC1/matching-information.json` — soru 27–31, pasaj **A03**
  - `content/reading/tests/AC2/matching-information.json` — soru 27–31, pasaj **A06**
  - `content/reading/tests/AC3/matching-information.json` — soru 27–31, pasaj **A09**
  - `content/reading/tests/AC4/matching-information.json` — soru 27–31, pasaj **A12**
- **Yönerge:** dört pasajın da tam **8 paragrafı** (A–H) olduğu için hepsinde aynı kalıp:
  `The passage has EIGHT paragraphs, A-H. ... Write the correct letter, A-H, in boxes
  27-31 on your answer sheet.` Dört sette de beş cevabın hepsi **farklı harf** olduğundan
  `NB You may use any letter more than once.` satırı **hiçbirine konmadı** (prompt bu
  satırı yalnız gerçek tekrar varsa istiyor).
- **Cevap dağılımı** (hepsi tekrarsız, ilk paragraf A ve son paragraf H her sette var,
  sıra pasaj sırasına göre değil — prompt bunu tercih ediyor):
  - AC1 → C · H · A · G · E
  - AC2 → F · A · H · B · D
  - AC3 → B · H · E · A · F
  - AC4 → D · A · H · G · C
- **Sorulan bilgi türleri bilerek çeşitlendirildi:** karşılaştırma (AC1/29 ekosistem–tek
  canlı, AC3/30 iki kentin yok oluşu), tanım/açıklama (AC1/27 asitlenmenin kimyası,
  AC2/31 verimlilik ölçüsü, AC4/28 uykunun etkin rolü), sayısal bulgu (AC1/31 pH farkı,
  AC2/27 kıdeme göre azalan kazanç, AC3/29 akson kalınlığı), yöntem ayrıntısı (AC2/30
  ilk altı ayın dışarıda bırakılması, AC3/31 moleküllerle eleme, AC4/27 sersemliğe karşı
  önlem, AC4/31 ipuçlu hatırlama), sonuç/yorum (AC1/30 iskelete bağımlı türler, AC4/30
  unutulmaya açık anılar), öngörü ve uygulama (AC1/28 yüzyıl sonu, AC2/29 yönetici
  tavsiyesi), sınırlama (AC3/28 tek bireye genellenemezlik).
- **Elenen / değiştirilen sorular (Tuzak 1 — birden çok paragrafa uyan ifade):**
  - **A03, "laboratuvarın sınırı" sorusu atıldı.** C paragrafı deneylerin yalnız hafta-ay
    sürdüğünü, A paragrafı ise laboratuvar tankının gerçeği taklit edemediğini söylüyor;
    "laboratuvarın yetersizliği" diye sorulsa iki paragraf da savunulabilirdi. Yerine A
    için **ekosistem–tek canlı ayrımı**, C için **asitlenmenin kimyası** soruldu; ikisi
    de tek paragrafta.
  - **A09, "camlaşmanın neden çok ender olduğu" sorusu atıldı.** Hızlı ısınma + hızlı
    soğuma koşulu hem C hem G paragrafında geçiyor (C nedeni, G ise dar ısıl aralığı
    anlatıyor) — cevap tartışmalı olurdu. C ve G'nin ikisi de bu sette kullanılmadı.
  - **A06, "beklentiye ters çıkan sonuç" sorusu (G) atıldı.** E paragrafı "ilk sonuç
    yaygın bir varsayıma ters düştü", G paragrafı "bu bulgu apaçık açıklamayı
    karmaşıklaştırdı" diyor; ikisi de aynı ifadeye uyuyordu. G bu sette hiç kullanılmadı.
  - **A06/31 ilk hâli değiştirildi:** kökü "çalışanın kendi beyanına güvenilmemesi" idi ve
    kanıtı D paragrafının 2. cümlesiydi; bu cümle **aynı testin** `summary-completion`
    36–40 setinde (37. soru) zaten kullanılmıştı. Aynı adayın aynı cümleyi iki kez
    çözmemesi için soru D'nin 1. cümlesine (verimlilik ölçüsünün tanımı) çevrildi.
  - **A06/30'un kökünde `records` kelimesi vardı**, pasajda bu kelime yalnız B
    paragrafında geçiyordu — kelime eşleşmesiyle bulunma riski (Tuzak 2). Kök
    "the choice to ignore what employees produced during their opening months" olarak
    yeniden yazıldı.
- **Aynı testteki öteki setlerle örtüşme:** dört pasajın `summary-completion` setleri
  aynı pasajları kullandığı için her soru, o testteki öteki dosyaların `evidence`
  cümleleriyle tek tek karşılaştırıldı; tek çakışma (AC2/31) yukarıda anlatıldığı gibi
  giderildi. Bilgi düzeyinde de tekrar edilen olgu yok: örneğin A03'te özet tamamlama
  `bioerosion` terimini soruyor, bilgi eşleştirme aynı paragrafın **başka türlere barınak
  olma** cümlesini hedefliyor.
- Doğrulama: geçici denetim scriptiyle (`tools/_p11_kontrol.py` — silindi) JSON
  geçerliliği, zarf alanlarının tamlığı, `options` listesinin gerçek paragraf harfleriyle
  aynı olması, yönergedeki **paragraf sayısı ve kutu numaralarının** gerçek değerlere
  uyması, soru sayısı (5) ve numara aralığı (27–31), `answer`/`accepted_variants`
  tutarlılığı, `evidence`in pasajda **birebir** geçişi, `evidence_locator`ın (paragraf +
  kaçıncı cümle) o cümleye birebir denk gelmesi, kanıt paragrafının cevap harfiyle aynı
  olması, `uniqueness_check`in **dolu olması ve en az bir başka paragrafı adıyla elemesi**,
  aynı harfin en fazla 2 kez cevap olması, ilk ve son paragraftan soru gelmesi, `NB`
  satırının tekrar durumuyla tutarlılığı, cevapların pasaj sırasında dizilmemesi,
  açıklamaların Türkçe olması, görünür metinde "IELTS" geçmemesi ve **soru kökü ile pasaj
  arasında 4 kelimelik birebir örtüşme bulunmaması**. İki turda çıkan iki hata
  (yukarıdaki AC2/31 cümle çakışması ve AC2/30 kelime eşleşmesi) düzeltildi, son turda
  **hata 0**. Ardından `python tools/dogrula.py`: **şema hatası 0**, okuma sorusu **171**
  (tam test 106 + alıştırma 65), pasaj lisansı eksik 0, görünür metinde IELTS 0,
  yasak kaynak 0.
- Sonraki çalıştırmalara not: 2. paket **GT1 + GT2** (soru 1–7, G01/G02 metin setleri) —
  orada yönerge Academic kalıbı değil, *"Look at the five notices, A-E. For which notice
  are the following statements true?"* kalıbı olacak ve 7 soru 4–5 metne dağıtılacağı için
  **bir harfin iki kez cevap olması kaçınılmaz**; o zaman `NB` satırı **konmalı**.
- Atlanan/sorun: yok. **1. paket bitti: 20 soru.** Kalan: 2. paket (GT1+GT2, 14 soru),
  3. paket (alıştırma, 15 soru).

## OPUS5-11 (2. çalıştırma: GT1 + GT2 bilgi eşleştirme)
- Tarih: 2026-08-04
- Depo kontrolü: `matching-information.json` yalnız `AC1`–`AC4` altında vardı (5'er soru,
  tam) → prompt dosyasındaki üç paketten bitmemiş ilki **2. paket (GT1 + GT2)** idi, o
  yapıldı. **14 soru** (2 test × 7) üretildi, plandaki 1–7 aralığıyla birebir aynı.
- Üretilen dosyalar:
  - `content/reading/tests/GT1/matching-information.json` — soru 1–7, pasaj **G01**
  - `content/reading/tests/GT2/matching-information.json` — soru 1–7, pasaj **G02**
- **Yönerge:** her iki metin setinde de tam **beş kısa metin** (A–E) olduğu için ikisinde
  de aynı kalıp: `Look at the five notices, A-E. For which notice are the following
  statements true? Write the correct letter, A-E, in boxes 1-7 on your answer sheet.
  NB You may use any letter more than once.` Academic paketinin tersine `NB` satırı
  **iki dosyaya da kondu**, çünkü 7 soru 5 metne dağıldığı için tekrar kaçınılmaz
  (1. çalıştırmanın sonundaki not böyle öngörmüştü).
- **Cevap dağılımı** (aynı harf en fazla 2 kez, ilk metin A ve son metin E her sette var,
  sıra metin sırasına göre değil):
  - GT1 → E · A · C · B · D · A · B  (A×2, B×2, C, D, E)
  - GT2 → C · A · E · B · A · D · E  (A×2, E×2, B, C, D)
  İki test bilerek farklı dağılım kullanıyor (GT1'de A ve B ikişer, GT2'de A ve E ikişer),
  aday iki testte aynı örüntüyü öğrenmesin diye.
- **Sorulan bilgi türleri bilerek çeşitlendirildi:** ön koşul/işlem (GT1/1 düzey belirleme,
  GT1/2 adres belgesi), ceza ve ek ücret (GT1/3 çıkışta okutmama, GT2/5 24 saati aşan
  iade), izin/onay (GT1/4 veli onayı, GT2/1 yapı yüksekliği sınırı), bilginin nereden
  bulunacağı (GT1/5 girişteki çizelge), kısıtlama (GT1/6 ayırtılmış eserin süresi
  uzatılamaz), takvim istisnası (GT1/7 yarıyıl haftası, GT2/4 pazar erken bitiş),
  para tutulması ve iadesi (GT2/2), alternatif erişim yolu (GT2/3 telefonla kayıt),
  kural karşılaştırması (GT2/6 bir seansta zorunlu ötekinde isteğe bağlı), asgari
  katılımcı şartı (GT2/7).
- **Elenen / değiştirilen sorular:**
  - **G01, "ödünç alınabilecek en fazla eşya sayısı" sorusu atıldı** (Tuzak yok ama
    çakışma vardı): kanıtı A metninin 3. cümlesiydi, aynı cümle 6. sorunun (ayırtılmış
    eserin uzatılamaması) kanıtı olarak daha iyi iş görüyordu. Aynı cümleden iki soru
    çıkarmamak için 2. soru A'nın 2. cümlesine (adres belgesi) çevrildi.
  - **G02, "yaş sınırının altındakilerin ücretsiz girişi" sorusu (B) atıldı.** B metni on
    iki yaş altını yetişkinle birlikte ücretsiz alıyor, D metni ise üç yaş altını
    ücretsiz alıyor; "belirli bir yaşın altında giriş ücretsiz" ifadesi iki metne birden
    uyduğu için soru geçersiz olurdu (Tuzak 1). Yerine B için **pazar günü erken bitiş**
    soruldu, tek metne ait.
  - **G02, "kullanıcının kendi güvenlik donanımını getirmesi" sorusu (A) atıldı.** A
    kaskın verilmediğini söylüyor, D bone takmanın kulvar seanslarında zorunlu olduğunu
    söylüyor; "kişinin kendi ekipmanını getirmesi" ikisine de çekilebilirdi. A için
    bunun yerine 90 sterlinlik geçici blokaj ve 350 sterlinlik kayıp bedeli soruldu.
- **Tuzak 2 için ek denetim:** denetim scriptine, soru kökündeki her içerik kelimesinin
  (5+ harf) pasajın **yalnızca doğru metninde** geçip geçmediğine bakan bir kontrol
  eklendi — böyle bir kelime varsa aday pasajı okumadan eşleştirme yapabilir. İlk turda
  üç kök takıldı ve yeniden yazıldı: GT1/1'de `completed`+`first` (ikisi de yalnız E'de),
  GT1/5'te `every` (yalnız D'de), GT2/3'te `start` (yalnız E'de). Ayrıca GT1/5'teki
  "exact dates" ve GT2/6'daki "session" gibi birebir yankılar da temizlendi. Son hâlde
  hiçbir kökte tek metne özgü kelime kalmadı; buna karşılık **yanlış yöne çeken** ortak
  kelimeler bilerek bırakıldı (ör. GT2/3'teki "reserve" kelimesi pasajda yalnız D'de
  "pool is reserved for school lessons" biçiminde geçiyor — cevap E, yani kelime
  eşleştirmesi yapan adayı cezalandırıyor).
- Doğrulama: geçici denetim scriptiyle (`tools/_p11b_kontrol.py` — silindi) JSON
  geçerliliği, zarf alanlarının tamlığı, `passage_id`nin pasajla uyuşması, `options`
  listesinin gerçek metin harfleriyle aynı olması, yönergedeki **metin sayısı, harf
  aralığı ve kutu numaralarının** gerçek değerlere uyması, soru sayısı (7) ve numara
  aralığı (1–7), `answer`/`accepted_variants` tutarlılığı, `evidence`in doğru metinde
  **birebir** geçişi ve **başka metinde geçmemesi**, `evidence_locator`ın (metin + kaçıncı
  cümle) o cümleye birebir denk gelmesi, `uniqueness_check`in dolu olması ve en az bir
  başka metni **adıyla** elemesi, aynı harfin en fazla 2 kez cevap olması, ilk ve son
  metinden soru gelmesi, `NB` satırının tekrar durumuyla tutarlılığı, cevapların metin
  sırasında dizilmemesi, iki sorunun **aynı cümleyi** kullanmaması, zorluk çeşitliliği,
  açıklamaların Türkçe olması, görünür metinde "IELTS" geçmemesi ve soru kökü ile pasaj
  arasında 3–4 kelimelik birebir örtüşme bulunmaması denetlendi. Yapısal denetim ilk
  turda **hata 0** verdi; yalnız yukarıdaki Tuzak 2 kontrolü üç kök yakaladı, düzeltmeden
  sonra **hata 0**. Ardından `python tools/dogrula.py`: **şema hatası 0**, okuma sorusu
  **185** (tam test 120 + alıştırma 65), pasaj lisansı eksik 0, görünür metinde IELTS 0,
  yasak kaynak 0. GT1 ve GT2 artık 20/40.
- `evidence_locator` biçimi: G01/G02 beş ayrı kısa metinden oluşuyor ve metinlerin iç
  paragraf harflendirmesi yok, bu yüzden `{ "text": "A", "sentence": n }` kullanıldı
  (G03/G04'te olduğu gibi ayrıca `paragraph` alanı yok; Academic dosyalarındaki
  `paragraph` alanının karşılığı burada `text`).
- Aynı testteki öteki setlerle örtüşme yok: GT1/GT2'nin şu ana kadar üretilmiş öteki
  dosyaları 2. ve 3. bölüm pasajlarını (G03/G05, G04/G06) kullanıyor, **G01 ve G02'ye ilk
  kez bu sette dokunuldu**. 1. bölümün öteki soru grubu olan 8–14 (TRUE/FALSE/NOT GIVEN,
  FABLE5-40) aynı metin setinden gelecek — o oturum bu dosyadaki `evidence` cümlelerini
  önce okumalı; şu an kullanılan cümleler: G01 A/2, A/3, B/1, B/4, C/4, D/2, E/1 ve
  G02 A/2, A/4, B/2, C/4, D/4, E/2, E/4.
- Referans PDF'leri: `referans/text/` klasörü bu oturumda da yoktu (yalnız `referans/*.pdf`
  var). Yönerge kalıbı prompt dosyasında verilen General Training kalıbından alındı.
- Atlanan/sorun: yok. **2. paket bitti: 14 soru. OPUS5-11'de 3 paketten 2'si tamam
  (34 soru).** Kalan: 3. paket (alıştırma, 15 soru) — orada `test_id` `null`, `practice`
  `true`, numaralar 1'den başlıyor, her item'a `passage_id` yazılıyor, aynı pasajdan en
  fazla 4 soru çıkıyor ve **tam testlerdeki bilgiler tekrar sorulmuyor** (AC1–AC4 ve
  GT1–GT2 `matching-information.json` dosyalarının `evidence` alanları önce topluca
  okunmalı).

## OPUS5-11 (3. çalıştırma: alıştırma — bilgi eşleştirme)

- Paket: **alıştırma, 15 soru**. Dosya: `content/reading/practice/matching-information.json`.
  `test_id` `null`, `practice` `true`, numaralar 1–15, her item'da `passage_id` var.
  Bununla OPUS5-11'in üç paketi de bitti: 20 (AC1–AC4) + 14 (GT1–GT2) + 15 = **49 soru**.
- Pasaj seçimi: **A01, A04, A07, A11**. Tam testlerin bilgi eşleştirme setleri A03, A06,
  A09, A12, G01 ve G02'yi kullanmıştı; alıştırmada bu altı pasaja hiç dokunulmadı, böylece
  "aynı bilgiyi sorma" kuralı en baştan güvenceye alındı. Dört pasajın da paragraf
  harflendirmesi A–H olduğu için tek bir `options` listesi ve tek bir yönerge yetti.
  Pasaj başına 4 + 4 + 4 + 3 soru; sınır olan "aynı pasajdan en fazla 4" aşılmadı.
- Aynı pasajın tam testteki öteki setleriyle çakışma denetlendi: A01 → AC1
  `note-completion` (B/3, B/4, C/1, D/4, E/2, F/3), A04 → AC2 `flow-chart-completion`
  (B/2, C/1, C/2, D/1, E/1, E/2), A07 → AC3 `table-completion` (B/3, C/2, D/2, E/2, E/3,
  F/3), A11 → AC4 `sentence-completion` (C/1, D/1, E/5, H/1). Bu setteki 15 sorunun hiçbiri
  bu cümlelerden birini kullanmıyor; aynı paragrafa denk gelenlerde (A01 D ve F, A04 B ve
  E, A07 B, C, D ve E, A11 C ve E) bilinçli olarak **başka bir cümle** hedeflendi.
- Harf dağılımı: A2 B2 C2 D2 E1 F2 G2 H2 = 15. **Aynı harf en fazla 2 kez** kuralı sağlandı;
  sekiz harfin hepsi kullanıldı, yani ilk (A) ve son (H) paragraftan da soru geldi.
  Cevaplar pasaj sırasında dizilmiyor: A01 → F A H D, A04 → G H B F, A07 → D G B C,
  A11 → E A C. `NB You may use any letter more than once.` satırı korundu, çünkü set
  genelinde yedi harf ikişer kez cevap.
- Yönerge tek pasaja değil dörde birden baktığı için "The passage has..." kalıbı
  "Each of the passages below has EIGHT paragraphs, A-H." biçiminde kuruldu; hangi sorunun
  hangi pasaja ait olduğu `stem_block` alanındaki dört satırla veriliyor (alıştırma
  dosyalarında `summary-completion.json`'daki gruplama biçimiyle aynı mantık). Kutu
  numarası ("in boxes 27-31 on your answer sheet") alıştırmada anlamsız olduğu için
  "next to each question" ile değiştirildi.
- Bilgi türü çeşitliliği: tanım/özet (A01 A, A11 E), sebep açıklaması (A01 F, A07 D),
  örnek (A01 D), yargı/sonuç (A01 H, A07 G, A04 G), sayısal karşılaştırma (A07 B),
  zaman bilgisi (A04 F, A07 C), kısıtlama (A04 H, A04 B), pratik gerekçe (A11 A),
  yöntem kuralı (A11 C). Zorluk: 3 easy, 8 medium, 4 hard.
- Tuzak 1 (birden çok paragrafa uyan ifade) için her sorunun ardından o pasajın sekiz
  paragrafı tek tek tarandı ve `uniqueness_check` alanına karışabilecek paragraflar
  **adıyla** yazıldı. Bu denetimde **iki soru elendi**:
  - A07 (beluga) A paragrafı için düşünülen "ayna testinin nasıl yapıldığının genel
    tanımı" sorusu **atıldı**: D paragrafı aynı işlemin bu çalışmadaki uygulamasını
    anlatıyor ve "tanım" ile "uygulama" ayrımı adaydan haksız bir yorum istiyordu. A07'nin
    A paragrafı yerine B paragrafı kullanıldı, ikinci A cevabı A11'den alındı.
  - A01 (fil) H paragrafı için ilk yazılan "dar tasarlanmış tek bir testten hüküm vermeye
    karşı uyarı" sorusu **atıldı**: F paragrafı da "sorun hayvanların zekâsında değil,
    sunulan araçlardaydı" diyor ve iki cevap da savunulabilir hâle geliyordu. Yerine H'nin
    ilk cümlesindeki **üç özelliğin bir arada** değerlendirilmesi soruldu; C, D ve E bu
    özellikleri ayrı ayrı anlatıyor ama hiçbiri üçünü birleştirmiyor.
- Tuzak 2 (kelime eşleşmesiyle bulunabilen soru) için soru kökündeki içerik kelimeleri
  pasajın paragraflarına karşı tarandı; yalnızca bir ya da iki paragrafta geçen kelimeler
  işaretlendi. Bu tarama **sekiz soru kökünde** ayırt edici kelime yakaladı ve hepsi
  yeniden yazıldı: `incapable`/`species`/`simply` (soru 3), `platform`/`stood` (4), `today`
  (5), `procedure`/`without` (9), `capacity` (10), `spent`/`front` (11), `bodies` (12),
  `evidence` (14). Düzeltme sonrası geriye yalnızca pasajın geneline yayılmış sıradan
  kelimeler kaldı (`animal's`, `authors`, `learning`, `hung`, `place`).
- Yapısal denetim (yazılan kontrol betiğiyle): 15 `evidence` alanının hepsi kendi
  paragrafında **birebir** geçiyor ve aynı pasajın başka hiçbir paragrafında geçmiyor;
  `evidence_locator`ın paragraf harfi cevapla aynı ve verilen cümle numarası o cümleye
  denk düşüyor; `uniqueness_check`, `explanation`, `accepted_variants` ve `difficulty`
  alanlarının hiçbiri boş değil; numaralar 1–15 kesintisiz; görünür metinde "IELTS" yok.
  Ardından `python tools/dogrula.py`: **şema hatası 0**, okuma sorusu **200** (tam test 120
  + alıştırma 80), pasaj lisansı eksik 0, IELTS 0, yasak kaynak 0.
- Atlanan/sorun: yok. **OPUS5-11 tamamen bitti (3/3 paket, 49 soru).**

## OPUS5-20 (1. çalıştırma: L1 — dört bölümün senaryo metni)

- Tarih: 2026-08-04
- Depo kontrolü: `content/listening/scripts/` **tamamen boştu** ve NOTLAR.md'de hiç dinleme
  kaydı yoktu → çalıştırma listesindeki ilk üretilmemiş grup **L1** idi, o yapıldı.
  Bu oturumda **soru üretilmedi** (promptun kuralı); 40 soru sonradan `OPUS5-21` ve
  `FABLE5-43` tarafından bu metinlerden çıkarılacak.
- Üretilen dosyalar: `content/listening/scripts/L1-S1.json` … `L1-S4.json`.

### L1 — konu, aksan, kelime sayısı (sonraki testlerde TEKRAR EDİLMEYECEK)

| Bölüm | Konu (havuzdaki karşılığı) | Ortam | Aksanlar | Kelime | Bilgi noktası | Çeldirici |
|---|---|---|---|---|---|---|
| 1 | **yaz kampı kaydı** — telefonla kayıt | 2 kişi | F1 `en-GB` + M1 `en-AU` | 840 | 23 | 8 |
| 2 | **yeni bir müze** — Weavers' Yard tanıtımı | 1 kişi | F1 `en-GB` | 870 | 31 | 4 |
| 3 | **grup sunumu planlama** — topluluk enerjisi | 3 kişi | F1 `en-GB` + M1 `en-CA` + F2 `en-AU` | 942 | 27 | 6 |
| 4 | **kentsel tarım** — akademik ders | 1 kişi | M1 `en-GB` | 949 | 27 | 5 |

  ⚠️ **L2–L6 için:** yukarıdaki dört konu bir daha kullanılmayacak. 4. bölüm aksanı
  tablodaki döngüye göre ilerlemeli: L2 `en-AU`, L3 `en-CA`, L4 `en-GB`, L5 `en-AU`,
  L6 `en-CA`. Kelime aralıkları gerçekten sayıldı (`len(text.split())`, bütün repliklerin
  toplamı) ve hepsi hedefin içinde: 750–850 / 800–900 / 850–950 / 850–950.
- **Şemaya eklenen iki alan** (sonraki bölümler de aynısını kullanmalı, soru üreten
  promptlar buna dayanacak):
  - `turn_index_base: 0` — prompt şemasındaki `turn_index` alanının 0 mı 1 mi tabanlı
    olduğu belirsizdi; **0 tabanlı** (yani `turns` dizisinin indeksi) seçildi ve bu alanla
    açıkça belgelendi. Her `answer_points` kaydına ayrıca **`speaker`** alanı da kondu, ki
    3. bölümde "kim ne dedi" sorusu için turns'e geri dönmek gerekmesin.
  - `speakers[].voice` — prompt "aksanı `voice` alanına yaz" diyor, şema örneği ise
    `accent` kullanıyor. İkisi de yazıldı, değerleri birebir aynı (seslendirme aracı
    hangisini okursa okusun çalışsın diye).
- **Çeldirici (distractor) düzeltmeleri** — bölüm başına en az 3 şartı fazlasıyla karşılandı:
  - S1 (8): yaş (on → on bir), tarih (13 → 20 Temmuz), açılış saati (dokuz → dokuzu çeyrek
    geçe), ücret (210 → 185 pound), ödeme (kart → banka havalesi), etkinlik (kano →
    okçuluk), buluşma yeri (ana kapı → spor salonu), yaş grubu adı (Otters → Kingfisher).
  - S2 (4): kapalı gün (Pazartesi → Salı), tur saatleri (11.30/14.30 → 11.00/14.00),
    yıllık kart (25 → 22 pound), dokunma seansı (Pazar → Cumartesi).
  - S3 (6): hafta (10 → 9), oda (seminer odası B → medya odası), süre (15 → 12 dakika),
    veri kaynağı (ulusal anket → belediye açık veri portalı), kayıt biçimi (video → ses),
    kaynakça kılavuzu (geçen yılın el kitabı → ders sayfası).
  - S4 (5): zirve yılı (1950'ler → 1940'lar), bahçe alanı (5.000 → 2.000 m²), verim
    (on beş kat → yaklaşık üç kat), en çok bildirilen fayda (egzersiz → insanlarla temas),
    şehrin kendi sebzesini üretme oranı (üçte bir → yaklaşık yüzde beş).
- **S2 `spatial_description`:** 12 öğeli zemin kat + merdiven başı planı (main entrance,
  ticket desk, café, shop, cloakroom, workshop room, weaving gallery, lecture theatre,
  lift, courtyard garden, reading room, temporary exhibition gallery), tarif 6–9.
  repliklerde, `on your left` · `opposite` · `next to` · `at the far end` · `between … and …` ·
  `straight ahead` · `at the top of the stairs` · `at the back of` yön belirteçleriyle.
- **S3 görüş ayrımı:** Nadia (F1) rüzgâr kooperatifini savunuyor (on iki yıllık kayıt var)
  ve röportajların **filmini** çekmek istiyor; Callum (M1) okul çatısı güneş projesini
  savunuyor (kimse çalışmamış) ve klip yerine **alıntıyı slayta** koymak istiyor; danışman
  (F2) okulları destekliyor ama uzlaşma olarak **ses kaydı + slaytta metin** öneriyor.
  Üç ayrı görüş sahibi de `answer_points` içinde `kind: opinion` ile işaretli.
- **Doğrulama:** iki geçici betik yazıldı ve iş bitince silindi.
  - `tools/_l1_uret.py` (üretici): `turn_index` değerlerini **elle yazmak yerine** her
    `quote`u repliklerde arayarak hesapladı ve alıntı birden çok replikte (ya da hiç)
    geçiyorsa üretimi durdurdu — bu sayede alıntı/indeks uyuşmazlığı baştan imkânsız oldu.
    Kelime sayısı ve `estimated_minutes` (kelime/150) da burada hesaplandı.
  - `tools/_l1_kontrol.py` (denetleyici): JSON geçerliliği, zorunlu alanlar, kimlik
    tutarlılığı, gerçek kelime sayısının aralıkta olması, `word_count` alanının sayımla
    uyuşması, konuşmacı kodlarının tanımlı olması, **aksan dağılımının tablodaki gibi
    olması**, `answer_points` sayısı (≥15), `distractor` sayısı (≥3), her alıntının kendi
    repliğinde **birebir** ve metnin tamamında **tek** geçmesi, `speaker` alanının replikle
    uyuşması, `kind` değerlerinin izinli listede olması, bilgi noktalarının **metne
    yayılması** (her çeyrekte en az 2), S2'de plan öğesi sayısı + yön belirteçleri + her
    etiketin metinde geçmesi, S3'te en az iki konuşmacıdan ayrı görüş, "IELTS" geçmemesi,
    Amerikan yazımı taraması ve metinde rakam bulunmaması. **İlk turda hata 0.**
  - Ardından `python tools/dogrula.py`: **şema hatası 0**, pasaj lisansı eksik 0,
    görünür metinde IELTS 0, yasak kaynak 0. (Senaryolar soru dosyası olmadığı için
    "L1 0/40 EKSIK" satırı beklenen durumdur; 40 soru OPUS5-21 + FABLE5-43'ten gelecek.)
- **Yazım/telif kararları:** İngiliz İngilizcesi (`centre`, `programme`, `theatre`,
  `travelled`, `metres`) — betik Amerikan biçimlerini ayrıca taradı. Metinde **hiç rakam
  yok**, sayılar konuşulduğu gibi yazıldı (`eighteen forty-two`, `a hundred and
  eighty-five`, `oh seven nine four one, double two six, three one five`); tek istisna
  kâğıt boyu `A4`. 1. bölümde harf harf söyleme bir kez var (`Ferreira — F-E-R-R-E-I-R-A`).
  Bütün kişi/kurum/yer adları uydurma (Willowbank, Weavers' Yard, Larkspur Road,
  Netherfield, Foundry Lane, Bridge Street, Kingfisher/Otters grupları). Din, siyaset,
  savaş, hastalık, kişisel dram konusu yok — 4. bölümde bahçeciliğin tarihi anlatılırken
  savaş dönemi kampanyalarına **bilinçli olarak girilmedi**, yerine 19. yüzyıl
  düzenlemeleri ve arsa satışı kullanıldı.
- **Referans PDF'leri:** `referans/text/` klasörü yine yoktu ve `pdftotext` bu oturumda da
  izin alamadı. Ancak beş dinleme transkripti (`note-completion`, `table-completion`,
  `plan-map-diagram-labelling`, `multiple-choice-one-answer`, `short-answer`) **`Read`
  aracıyla doğrudan açılabildi** — bunlar metin tabanlı PDF'ler. Yalnız
  `ielts-listening-sample-tasks-2023.pdf` render gerektirdiği için açılamadı (`pdftoppm`
  yok). ⚠️ **Ortam notunun düzeltmesi:** "Read PDF'i açamıyor" tamamen doğru değil —
  metin katmanı olan PDF'ler `Read` ile açılıyor, yalnız taranmış/görüntü tabanlı olanlar
  açılmıyor. Sonraki oturumlar önce `Read` denemeli.
  Transkriptlerden yalnız konuşma ritmi, duraksama ve bilgi verme hızı alındı; **tek bir
  replik kopyalanmadı**, sahne/isim/senaryo taklit edilmedi (referanslardaki mobilya
  ilanı, quilt shop turu, öğrenci sebatı anketi, tez görüşmesi ve moda şirketi sunumu
  konularının hiçbiri kullanılmadı).
- Atlanan/sorun: yok. **OPUS5-20'de 6 testten 1'i tamam;** kalan L2, L3, L4, L5, L6.

## OPUS5-20 (2. çalıştırma: L2 — dört bölümün senaryo metni)

- Tarih: 2026-08-04
- Depo kontrolü: `content/listening/scripts/` altında yalnız `L1-S1…S4` vardı → çalıştırma
  listesindeki ilk üretilmemiş grup **L2** idi, o yapıldı. Bu oturumda da **soru
  üretilmedi** (promptun kuralı); 40 soru sonradan `OPUS5-21` ve `FABLE5-43` tarafından bu
  metinlerden çıkarılacak.
- Üretilen dosyalar: `content/listening/scripts/L2-S1.json` … `L2-S4.json`.

### L2 — konu, aksan, kelime sayısı (sonraki testlerde TEKRAR EDİLMEYECEK)

| Bölüm | Konu (havuzdaki karşılığı) | Ortam | Aksanlar | Kelime | Bilgi noktası | Çeldirici |
|---|---|---|---|---|---|---|
| 1 | **taşınma şirketi** — telefonla fiyat alma ve tarih ayırtma | 2 kişi | M1 `en-GB` + F1 `en-AU` | 841 | 25 | 7 |
| 2 | **kütüphane yenilemesi** — Marlbrook kütüphanesi yeniden açılış konuşması | 1 kişi | F1 `en-GB` | 865 | 25 | 7 |
| 3 | **saha araştırması raporu** — dere üzerinde su kalitesi/omurgasız sayımı | 3 kişi | M1 `en-GB` + F1 `en-CA` + M2 `en-AU` | 946 | 23 | 7 |
| 4 | **antik su sistemleri** — akademik ders | 1 kişi | M1 `en-AU` | 943 | 26 | 5 |

  ⚠️ **L3–L6 için:** L1'in konuları (yaz kampı kaydı · yeni bir müze · grup sunumu
  planlama · kentsel tarım) ve yukarıdaki dört konu bir daha kullanılmayacak. Havuzda kalan:
  1. bölüm — araç kiralama, spor salonu üyeliği, konaklama başvurusu, kayıp eşya bildirimi,
  sağlık merkezi randevusu, bisiklet turu rezervasyonu; 2. bölüm — toplum bahçesi projesi,
  gönüllü programı, yerel çiftlik pazarı, doğa yürüyüşü rotaları, geri dönüşüm merkezi,
  festival programı; 3. bölüm — staj değerlendirmesi, tez konusu seçimi, laboratuvar deneyi
  sonucu, anket tasarımı, kaynak taraması, poster hazırlığı; 4. bölüm — uyku ve hafıza,
  deniz plastikleri, davranışsal ekonomi, gürültü kirliliği, tohum bankaları, yapay ışık ve
  doğa. 4. bölüm aksanı döngüsü: L3 `en-CA`, L4 `en-GB`, L5 `en-AU`, L6 `en-CA`.
- **Şema:** L1'de kararlaştırılan düzen aynen sürdürüldü — `turn_index_base: 0`, her
  `answer_points` kaydında ek `speaker` alanı, `speakers[]` içinde hem `accent` hem `voice`
  (değerleri birebir aynı). 1. bölümde konuşmacı rolleri L1'e göre ters çevrildi (bu kez
  görevli `en-GB` erkek, müşteri `en-AU` kadın), 3. bölümde de aksan–cinsiyet eşlemesi
  değiştirildi (öğrenciler M1 `en-GB` / F1 `en-CA`, danışman M2 `en-AU`) — seslendirmede
  altı testin hep aynı ses dizilimiyle çıkmaması için.
- **Çeldirici (distractor) düzeltmeleri** — bölüm başına en az 3 şartı fazlasıyla karşılandı:
  - S1 (7): adres (Selby Lane → Weir Street), ev tipi (daire → üç yatak odalı ev), tarih
    (3 Ekim Cumartesi → 2 Ekim Cuma), keşif randevusu (Salı 10.30 → Salı 11.00), ambalaj
    (battaniye → ahşap sandık), süre (beş saat → altı saat), ödeme (telefonda kart →
    e-postayla ödeme bağlantısı).
  - S2 (7): kapalı kalma süresi (bir yıl → on sekiz ay), ısıtma (gaz kazanı → ısı pompası),
    geç açılış günü (Çarşamba → Perşembe), kimlik (iki belge → adres yazan tek belge),
    ödünç sınırı (on iki → on beş), kahve köşesinin yeri (çalışma odasının yanı → tam
    karşısı), okuma grubu (ayın ilk Salısı → ikinci Salısı).
  - S3 (7): alan sayısı (altı → beş), ikinci ziyaret (dört hafta sonra → temmuz ortası),
    tayin düzeyi (tür → familya), oksijen ölçümü (metre → kimyasal test kiti), en temiz
    nokta (ormandaki üst nokta → bostanların arkası), kelime sınırı (üç bin → iki bin beş
    yüz), teslim tarihi (on iki → on dokuz).
  - S4 (5): eğim (yüzde bir → binde bir), yaş (beş bin → üç bin yıl), açık kanal kaybı
    (yarısı → yaklaşık üçte bir), sıva (saf kireç → kireç + öğütülmüş çömlek), su sırası
    döngüsü (on gün → on iki gün).
- **S2 `spatial_description`:** 12 öğeli zemin kat + birinci kat planı (main entrance,
  returns machine, enquiry desk, newspaper and magazine area, children's library, meeting
  room, lift, computer suite, quiet study room, local history room, coffee point, garden),
  tarif 5–8. repliklerde, `on your left` · `straight ahead` · `opposite` · `between … and …` ·
  `at the far end` · `behind` · `at the top of the stairs` · `next to` yön belirteçleriyle.
  Kahve köşesinin yeri bilinçli olarak önce yanlış söylenip düzeltiliyor (plan sorusu için
  hazır çeldirici).
- **S3 görüş ayrımı:** Rhys (M1) raporun **alan alan** düzenlenmesini istiyor ve çalışmanın
  zayıflığını **örneklem sayısına** bağlıyor; Marisol (F1) **değişken değişken** düzenlemeyi
  savunuyor ve zayıflığı **hep yağmurdan sonra örnekleme yapılmış olmasına** bağlıyor;
  danışman (M2) değişken düzenini seçiyor ama başa alanları tanıtan bir sayfa koyduruyor ve
  iki sınırlamayı da yazdırıyor (Marisol'ünki önce). Ek ayrılık: ham verinin tamamı eke
  konsun (Marisol) ↔ metinde özet tablo yeter (Rhys); danışman eki seçiyor. Üç görüş sahibi
  de `answer_points` içinde `kind: opinion` ile işaretli (toplam 6 görüş kaydı).
- **Doğrulama:** L1'deki iki betikli düzen tekrarlandı, ikisi de iş bitince silindi.
  - `tools/_l2_uret.py` (üretici): `turn_index` değerlerini elle yazmak yerine her `quote`u
    repliklerde arayarak hesapladı; alıntı hiç geçmiyorsa ya da birden çok replikte
    geçiyorsa üretimi durdurdu. Kelime sayısı ve `estimated_minutes` (kelime/150) burada
    hesaplandı.
  - `tools/_l2_kontrol.py` (denetleyici): JSON geçerliliği, zorunlu alanlar, kimlik
    tutarlılığı, gerçek kelime sayısının aralıkta olması ve `word_count` ile uyuşması,
    konuşmacı kodlarının tanımlı **ve hepsinin kullanılmış** olması, `accent`/`voice`
    eşitliği, aksan dağılımının tablodaki gibi olması, `answer_points` sayısı (≥15),
    `distractor` sayısı (≥3), id tekrarı, her alıntının kendi repliğinde birebir ve metnin
    tamamında **tek** geçmesi, `speaker` alanının replikle uyuşması, `kind` değerlerinin
    izinli listede olması, bilgi noktalarının metne yayılması (her çeyrekte en az 2), S2'de
    plan öğesi sayısı + yön belirteçleri + her etiketin metinde geçmesi, S3'te en az iki
    konuşmacıdan ayrı görüş, S1'de harf harf söyleme, "IELTS" geçmemesi, Amerikan yazımı
    taraması ve metinde rakam bulunmaması. **İlk turda tek uyarı çıktı ve o da yanlış
    alarmdı:** Amerikan yazımı taraması `liter` dizisini "older li*ter*ature" içinde
    yakalıyordu; tarama kelime sınırlı düzenli ifadeye çevrildi, ardından **hata 0**.
  - İlk taslakta dört bölümün de kelime sayısı hedefin üstündeydi (869 / 967 / 1012 / 1334);
    bilgi noktası taşımayan süs cümleleri budanarak aralığa çekildi (841 / 865 / 946 / 943).
    En büyük budama 4. bölümdeydi: ders üç teknolojiyi (yeraltı kanalı, sarnıç, basamaklı
    kuyu) koruyarak yaklaşık üçte bir oranında sıkıştırıldı, hiçbir `answer_point` elenmedi.
  - Ardından `python tools/dogrula.py`: **şema hatası 0**, pasaj lisansı eksik 0, görünür
    metinde IELTS 0, yasak kaynak 0. ("L2 0/40 EKSIK" satırı beklenen durumdur.)
- **Yazım/telif kararları:** İngiliz İngilizcesi — metinde geçen ayırt edici biçimler
  `metres`, `kilometres`, `storeys`, `neighbour`, `enquiry`, `organise`, `café`; denetim
  betiği ayrıca Amerikan karşılıklarını (`center`, `program`, `analyze`, `liters`, `toward`,
  `license` vb.) kelime sınırlı düzenli ifadeyle taradı, hiçbiri geçmiyor. Metinde **hiç rakam yok**;
  sayılar konuşulduğu gibi yazıldı (`nineteen oh six`, `oh seven six three three, double
  four one, nine oh two`, `two thousand five hundred`, `one in a thousand`). 1. bölümde harf
  harf söyleme bir kez var (`Haugland — H-A-U-G-L-A-N-D`). Bütün kişi/kurum/yer adları
  uydurma (Hartfield Removals, Petra Haugland, Selby Court, Weir Street, Ashcombe, Marlbrook,
  Grange Road, Rhys, Marisol). 4. bölümde **hiçbir gerçek yer, halk ya da arkeolojik alan
  adı anılmadı** — teknolojiler jenerik olarak ("yamacın eteği", "kurak bir ova") anlatıldı;
  din, siyaset, savaş, hastalık, kişisel dram yok.
- **Referans PDF'leri:** beş dinleme transkripti (`note-completion`, `table-completion`,
  `plan-map-diagram-labelling`, `multiple-choice-one-answer`, `short-answer`) bu oturumda da
  `Read` ile doğrudan açıldı (L1 notundaki düzeltme doğrulandı); `ielts-listening-sample-
  tasks-2023.pdf` yine render gerektirdiği için açılamadı. Transkriptlerden yalnız konuşma
  ritmi, duraksama ve bilgi verme hızı alındı; **tek bir replik kopyalanmadı**, sahne/isim/
  senaryo taklit edilmedi (referanslardaki ikinci el mobilya ilanı, quilt shop turu, öğrenci
  sebatı anketi, tez görüşmesi ve moda şirketi sunumu konularının hiçbiri kullanılmadı).
- Atlanan/sorun: yok. **OPUS5-20'de 6 testten 2'si tamam;** kalan L3, L4, L5, L6.

## OPUS5-20 (3. çalıştırma: L3 — dört bölümün senaryo metni)

- Tarih: 2026-08-04
- Depo kontrolü: `content/listening/scripts/` altında `L1-S1…S4` ve `L2-S1…S4` vardı →
  çalıştırma listesindeki ilk üretilmemiş grup **L3** idi, o yapıldı. Bu oturumda da **soru
  üretilmedi** (promptun kuralı); 40 soru sonradan `OPUS5-21` ve `FABLE5-43` tarafından bu
  metinlerden çıkarılacak.
- Üretilen dosyalar: `content/listening/scripts/L3-S1.json` … `L3-S4.json`.

### L3 — konu, aksan, kelime sayısı (sonraki testlerde TEKRAR EDİLMEYECEK)

| Bölüm | Konu (havuzdaki karşılığı) | Ortam | Aksanlar | Kelime | Bilgi noktası | Çeldirici |
|---|---|---|---|---|---|---|
| 1 | **spor salonu üyeliği** — spor merkezi kayıt masasında yüz yüze üyelik | 2 kişi | F1 `en-AU` + M1 `en-GB` | 773 | 25 | 6 |
| 2 | **doğa yürüyüşü rotaları** — Stonecrop kır parkında üç yeni rota + park haritası | 1 kişi | M1 `en-GB` | 876 | 34 | 4 |
| 3 | **staj değerlendirmesi** — iki öğrenci + danışman, staj sonrası teslimler | 3 kişi | F1 `en-AU` + M1 `en-CA` + F2 `en-GB` | 945 | 30 | 4 |
| 4 | **tohum bankaları** — akademik ders | 1 kişi | F1 `en-CA` | 949 | 26 | 4 |

  ⚠️ **L4–L6 için:** L1 (yaz kampı kaydı · yeni bir müze · grup sunumu planlama · kentsel
  tarım), L2 (taşınma şirketi · kütüphane yenilemesi · saha araştırması raporu · antik su
  sistemleri) ve yukarıdaki dört konu bir daha kullanılmayacak. **Havuzda kalan:**
  1. bölüm — araç kiralama, konaklama başvurusu, kayıp eşya bildirimi, sağlık merkezi
  randevusu, bisiklet turu rezervasyonu; 2. bölüm — toplum bahçesi projesi, gönüllü programı,
  yerel çiftlik pazarı, geri dönüşüm merkezi, festival programı; 3. bölüm — tez konusu seçimi,
  laboratuvar deneyi sonucu, anket tasarımı, kaynak taraması, poster hazırlığı; 4. bölüm —
  uyku ve hafıza, deniz plastikleri, davranışsal ekonomi, gürültü kirliliği, yapay ışık ve
  doğa. Havuzda **tam beşer konu kaldı, üç test kaldı** — sıkışıklık yok.
  4. bölüm aksanı döngüsü: **L4 `en-GB`, L5 `en-AU`, L6 `en-CA`.**
  ⚠️ 3. bölüm için ayrıca: **"tez konusu seçimi" seçilirse dikkat** — referans
  `multiple-choice-one-answer` transkripti tam olarak bir tez görüşmesi sahnesi; o konuyu
  yaparken sahne, disiplin ve akış belirgin biçimde farklı kurulmalı.
- **Şema:** L1'de kararlaştırılan düzen aynen sürdürüldü — `turn_index_base: 0`, her
  `answer_points` kaydında ek `speaker` alanı, `speakers[]` içinde hem `accent` hem `voice`
  (değerleri birebir aynı). Aksan–cinsiyet eşlemesi yine değiştirildi (1. bölümde bu kez
  görevli `en-AU` kadın / müşteri `en-GB` erkek; 3. bölümde öğrenciler `en-AU` kadın +
  `en-CA` erkek, danışman `en-GB` kadın; 4. bölümde ilk kez kadın anlatıcı) — altı testin
  seslendirmede hep aynı ses dizilimiyle çıkmaması için.
- **3. bölüm bu kez üç konuşmacılı ama iki öğrenci + bir danışman kurgusuyla**, L1/L2'deki
  "iki öğrenci aynı işi planlıyor" düzeninden farklı olarak **iki ayrı stajın**
  karşılaştırılması üzerine kuruldu; böylece görüş ayrımı doğal olarak çıkıyor.
- **Çeldirici (distractor) düzeltmeleri** — bölüm başına en az 3 şartı karşılandı:
  - S1 (6): adres (flat two → flat nine), off-peak saati (beş → dört), ödeme günü (ayın on
    beşi → ayın biri), induction süresi (bir saat → kırk dakika), induction günü (Perşembe
    dolu → Cuma), buluşma yeri (spor salonu girişi → kayıt masası).
  - S2 (4): mavi rota uzunluğu (beş mil → dört buçuk mil), tahta yolun açılışı (mayıs sonu →
    haziran ortası), rehberli yürüyüş günü (ayın ilk Cumartesi → ilk Pazar), çalılık temizleme
    günü (Perşembe → Salı).
  - S3 (4): rapor kelime sınırı (dört bin → üç bin beş yüz), sunum süresi (on beş → on iki
    dakika), teslim tarihi (on üç → yirmi Kasım), günlüğün teslim biçimi (ayrı belge → rapora
    ek).
  - S4 (4): örnekleme (otuz bitki → elli bitki), depolama sıcaklığı (eksi on sekiz → eksi
    yirmi), çimlenme eşiği (yüzde yetmiş beş → yüzde seksen beş), yeniden test aralığı (beş
    yıl → on yıl).
- **S2 `spatial_description`:** bu kez `kind: "map"` (L1 ve L2'de `plan` idi — bina değil,
  açık alan tarif ediliyor). 12 öğe: main entrance, visitor centre, car park, toilets,
  information hut, picnic area, bird hide, pond-dipping platform, lime kiln, wildflower
  meadow, viewpoint, boardwalk. Tarif 5–9. repliklerde; `immediately on your left` ·
  `opposite` · `at the back of` · `straight ahead of you` · `between … and …` · `next to` ·
  `beyond` · `at the far end` · `above` yön belirteçleriyle.
- **S3 görüş ayrımı (üç kişi, üç eksende ayrışıyor):**
  - *Stajın en değerli yanı:* Tamsin (F1) sakinler toplantılarına oturmak; Corin (M1) kendi
    başına verilen sayım verisi işi (toplantıları "slayt okuma" diye eliyor).
  - *Günlük sıklığı:* Tamsin iki haftada bir; Corin haftalık; danışman (F2) haftalık ama
    yüz kelimelik kısa girdiler.
  - *Rapor yapısı:* Tamsin kronolojik; Corin beceri temelli; danışman Corin'in yapısını
    seçiyor, Tamsin'e uzlaşma olarak başa bir sayfalık zaman çizelgesi koyduruyor.
  Her üç konuşmacının görüşü de `answer_points` içinde `kind: opinion` ile işaretli
  (toplam 9 görüş kaydı) — eşleştirme ve çoktan seçmeli için fazlasıyla malzeme var.
- **Doğrulama:** L1/L2'deki iki betikli düzen tekrarlandı, ikisi de iş bitince silindi.
  - `tools/_l3_uret.py` (üretici): `turn_index` değerlerini elle yazmak yerine her `quote`u
    repliklerde arayarak hesapladı; alıntı hiç geçmiyorsa ya da birden çok replikte geçiyorsa
    üretimi durdurdu. Kelime sayısı ve `estimated_minutes` (kelime/150) burada hesaplandı.
  - `tools/_l3_kontrol.py` (denetleyici): L2'deki denetim listesinin aynısı — JSON
    geçerliliği, zorunlu alanlar, kimlik tutarlılığı, gerçek kelime sayısının aralıkta olması
    ve `word_count` ile uyuşması, `estimated_minutes` doğruluğu, konuşmacı kodlarının tanımlı
    ve hepsinin kullanılmış olması, `accent`/`voice` eşitliği, aksan dağılımının tablodaki
    gibi olması, `answer_points` sayısı (≥15), `distractor` sayısı (≥3), id tekrarı, her
    alıntının kendi repliğinde birebir ve metnin tamamında **tek** geçmesi, `speaker`
    alanının replikle uyuşması, `kind` değerlerinin izinli listede olması, bilgi noktalarının
    metne yayılması (her çeyrekte en az 2), S2'de plan öğesi sayısı + yön belirteçleri + her
    etiketin metinde geçmesi, S1/S3/S4'te `spatial_description`ın boş olması, S3'te en az iki
    konuşmacıdan ayrı görüş, S1'de harf harf söyleme, "IELTS" geçmemesi, kelime sınırlı
    Amerikan yazımı taraması ve metinde rakam bulunmaması. **İlk turda hata 0.**
  - İlk taslakta S2 (968), S3 (958) ve S4 (1061) hedefin üstündeydi; bilgi noktası taşımayan
    süs cümleleri budanarak aralığa çekildi (876 / 945 / 949). **Hiçbir `answer_point`
    elenmedi** — budama yalnız cevap taşımayan betimleyici cümlelerde yapıldı (en büyük
    budama S4'te: giriş, örnekleme ve yeniden üretim paragrafları sıkıştırıldı, dersin
    "solan fotoğraf" benzetmesi korundu).
  - Ardından `python tools/dogrula.py`: **şema hatası 0**, pasaj lisansı eksik 0, görünür
    metinde IELTS 0, yasak kaynak 0. ("L3 0/40 EKSIK" satırı beklenen durumdur.)
- **Yazım/telif kararları:** İngiliz İngilizcesi — metinde geçen ayırt edici biçimler
  `centre`, `programme`, `colour-coded`, `modelling`, `towards`, `neighbouring`. Amerikan
  karşılıkları (`center`, `program`, `color`, `analyze`, `meter`, `toward`, `behavior` vb.
  46 kelimelik liste) kelime sınırlı düzenli ifadeyle tarandı, hiçbiri geçmiyor. Metinde **hiç rakam yok**;
  sayılar konuşulduğu gibi yazıldı (`nineteen sixty-eight`, `oh seven eight two, double one
  four, six oh nine`, `minus a hundred and ninety-six`, `a mile and a half`). 1. bölümde harf
  harf söyleme bir kez var (`Kirkegaard — K-I-R-K-E-G-A-A-R-D`). Bütün kişi/kurum/yer adları
  uydurma (Quarry Fields, Adam Kirkegaard, Pennyfield Court/Road, Stonecrop Country Park,
  Cranmore Road, Redgate Housing Trust, Pelham Analytics, Tamsin, Corin). 4. bölümde
  **hiçbir gerçek tohum bankası, kurum ya da ülke adı anılmadı**; din, siyaset, savaş,
  hastalık, kişisel dram yok.
- ℹ️ **Bilinçli kabul edilen küçük yankı:** L2-S2'de kütüphanenin "seed library" tohum
  değişim hizmeti geçiyor, L3-S4 ise bilimsel tohum bankalarını anlatıyor. Farklı testler,
  farklı bölümler ve tamamen farklı içerik olduğu için konu tekrarı sayılmadı; yine de
  L4–L6'da tohum/bahçe temasına bir daha girilmemesi iyi olur.
- **Referans PDF'leri:** dört dinleme transkripti (`note-completion`,
  `plan-map-diagram-labelling`, `multiple-choice-one-answer`, `short-answer`) bu oturumda da
  `Read` ile doğrudan açıldı; `ielts-listening-sample-tasks-2023.pdf` yine render
  gerektirdiği için açılamadı (`referans/text/` klasörü hâlâ yok). Transkriptlerden yalnız
  konuşma ritmi, duraksama ve bilgi verme hızı alındı; **tek bir replik kopyalanmadı**,
  sahne/isim/senaryo taklit edilmedi (ikinci el mobilya ilanı, quilt shop turu, tez
  görüşmesi ve moda şirketi sunumu sahnelerinin hiçbiri kullanılmadı).
- Atlanan/sorun: yok. **OPUS5-20'de 6 testten 3'ü tamam;** kalan L4, L5, L6.

## OPUS5-20 (4. çalıştırma: L4 — dört bölümün senaryo metni)

- Tarih: 2026-08-04
- Depo kontrolü: `content/listening/scripts/` altında `L1-S1…S4`, `L2-S1…S4` ve `L3-S1…S4`
  vardı → çalıştırma listesindeki ilk üretilmemiş grup **L4** idi, o yapıldı. Bu oturumda da
  **soru üretilmedi** (promptun kuralı); 40 soru sonradan `OPUS5-21` ve `FABLE5-43` tarafından
  bu metinlerden çıkarılacak.
- Üretilen dosyalar: `content/listening/scripts/L4-S1.json` … `L4-S4.json`.

### L4 — konu, aksan, kelime sayısı (sonraki testlerde TEKRAR EDİLMEYECEK)

| Bölüm | Konu (havuzdaki karşılığı) | Ortam | Aksanlar | Kelime | Bilgi noktası | Çeldirici |
|---|---|---|---|---|---|---|
| 1 | **kayıp eşya bildirimi** — otobüs şirketinin kayıp eşya bürosuna telefon | 2 kişi | M1 `en-AU` + F1 `en-GB` | 842 | 28 | 7 |
| 2 | **geri dönüşüm merkezi** — yeniden açılan Halstock merkezinin tanıtımı + saha planı | 1 kişi | F1 `en-GB` | 890 | 36 | 6 |
| 3 | **poster hazırlığı** — iki öğrenci + danışman, araştırma günü posteri | 3 kişi | M1 `en-GB` + F1 `en-AU` + F2 `en-CA` | 946 | 33 | 7 |
| 4 | **gürültü kirliliği** — akademik ders | 1 kişi | F1 `en-GB` | 949 | 34 | 5 |

  ⚠️ **L5–L6 için:** L1 (yaz kampı kaydı · yeni bir müze · grup sunumu planlama · kentsel
  tarım), L2 (taşınma şirketi · kütüphane yenilemesi · saha araştırması raporu · antik su
  sistemleri), L3 (spor salonu üyeliği · doğa yürüyüşü rotaları · staj değerlendirmesi ·
  tohum bankaları) ve yukarıdaki dört konu bir daha kullanılmayacak. **Havuzda kalan (her
  bölümde tam dörder konu, iki test kaldı):** 1. bölüm — araç kiralama, konaklama başvurusu,
  sağlık merkezi randevusu, bisiklet turu rezervasyonu; 2. bölüm — toplum bahçesi projesi,
  gönüllü programı, yerel çiftlik pazarı, festival programı; 3. bölüm — tez konusu seçimi,
  laboratuvar deneyi sonucu, anket tasarımı, kaynak taraması; 4. bölüm — uyku ve hafıza,
  deniz plastikleri, davranışsal ekonomi, yapay ışık ve doğa.
  4. bölüm aksanı döngüsü: **L5 `en-AU`, L6 `en-CA`.**
  ⚠️ 3. bölüm için L3'te yazılan uyarı geçerliliğini koruyor: **"tez konusu seçimi" seçilirse**
  referans `multiple-choice-one-answer` transkripti tam olarak bir tez görüşmesi sahnesi;
  sahne, disiplin ve akış belirgin biçimde farklı kurulmalı.
- **Şema:** L1'de kararlaştırılan düzen aynen sürdürüldü — `turn_index_base: 0`, her
  `answer_points` kaydında ek `speaker` alanı, `speakers[]` içinde hem `accent` hem `voice`
  (değerleri birebir aynı). Aksan–cinsiyet eşlemesi yine değiştirildi: 1. bölümde bu kez
  **görevli `en-AU` erkek / müşteri `en-GB` kadın** (L1'de GB kadın + AU erkek, L2'de GB erkek
  + AU kadın, L3'te AU kadın + GB erkek olmuştu — dördü de farklı); 3. bölümde öğrenciler
  `en-GB` erkek + `en-AU` kadın, danışman `en-CA` kadın; 4. bölümde `en-GB` kadın anlatıcı
  (L1-S4 `en-GB` erkekti).
- **1. bölüm bu kez bir bildirim/şikâyet sahnesi** (L1 kayıt, L2 fiyat teklifi, L3 üyelik
  olmuştu): kaybedilen eşyanın tarifi form tamamlama için doğal olarak renk, malzeme, içerik,
  koltuk yeri, referans numarası gibi çok sayıda somut veri taşıyor.
- **Çeldirici (distractor) düzeltmeleri** — bölüm başına en az 3 şartı fazlasıyla karşılandı:
  - S1 (7): sefer numarası (dört yüz seksen altı → dört yüz seksen iki), tarih (Salı dokuz →
    Çarşamba on), çanta rengi (lacivert → koyu yeşil), saklama süresi (iki hafta → üç ay),
    teslim yeri (otogar → Canal Road deposu), açılış saati (internet sitesindeki sekiz →
    sekiz buçuk), teslim ücreti (beş pound → üç pound).
  - S2 (6): yeniden inşa süresi (bir yıl → on dört ay), bahçe atığı bölmesi (broşürdeki üç →
    dört), cam/kutu/pet kumbaralarının yeri (ofisin yanı → çıkış bariyeri), van izni (kapıda
    form imzalama → üç iş günü önce çevrimiçi başvuru), kapalı gün (Çarşamba → Salı), dükkân
    günleri (yalnız Cumartesi → Cuma-Pazar).
  - S3 (7): gövde puntosu (yirmi dört → en az otuz), plotter süresi (iki gün → üç iş günü),
    pano boyu (küçük panolar → geçen yıldan beri büyük), özet teslim tarihi (on bir → on sekiz;
    on bir başlık kaydı tarihiydi), özet kelime sınırı (üç yüz → iki yüz elli), mekân (seminer
    bloğu → kütüphane atriyumu), jüriye konuşma süresi (beş dakika → iki dakika).
  - S4 (5): trafiğin iki katına çıkması (on desibel → üç desibel), gürültü haritası yenileme
    aralığı (üç yıl → beş yıl), karayolunun payı (üçte iki → yaklaşık beşte dört), gözenekli
    asfaltın kazancı (beş desibel → uygulamada üç-dört), ağaç şeridi derinliği (on metre →
    otuz metre).
- **S2 `spatial_description`:** `kind: "plan"`, on üç öğeli saha planı (entrance barrier,
  site office, toilets and water point, car park, reuse shop, textiles bank, garden waste
  bays, ramp, wood/rubble/scrap metal skips, containers for general waste, glass/cans/plastic
  banks, electrical store, paint and chemicals store). Tarif 3–7. repliklerde;
  `immediately on your left` · `opposite` · `next to` · `at the far end` · `between … and …` ·
  `straight ahead` · `behind` · `beyond` yön belirteçleriyle. Cam kumbaralarının yeri bilinçli
  olarak önce eski yeriyle anılıp düzeltiliyor (plan sorusu için hazır çeldirici).
- **S3 görüş ayrımı (üç kişi, üç eksende ayrışıyor):**
  - *Yerleşim:* Idris (M1) yöntemin sol üste gelmesini istiyor; Anneke (F1) bulgunun en üste
    gelmesini savunuyor; danışman (F2) soruyu en üste, sonuçları ortaya, yöntemi alt şeride
    koyduruyor.
  - *Şekil sayısı:* Idris üç ayrı grafik; Anneke tek birleşik grafik + bir fotoğraf; danışman
    Anneke'nin düzenini seçip üstüne yağış olayı sayılarını gösteren küçük bir tablo ekletiyor.
  - *Baskı:* Idris bölümün ücretsiz plotter'ı; Anneke gecikmemek için paralı kopya dükkânı;
    danışman plotter'ı seçiyor ama şimdi rezerve ettiriyor (üç iş günü).
  Üçünün de görüşü `answer_points` içinde `kind: opinion` ile işaretli (M1 3, F1 3, F2 2 —
  toplam 8 görüş kaydı), yani eşleştirme ve çoktan seçmeli için fazlasıyla malzeme var.
- **Doğrulama:** L1–L3'teki iki betikli düzen tekrarlandı; her ikisi de iş bitince silindi.
  - `tools/_l4_uret.py` (üretici): `turn_index` değerlerini elle yazmak yerine her `quote`u
    repliklerde arayarak hesapladı; alıntı hiç geçmiyorsa ya da birden çok replikte geçiyorsa
    üretimi durdurdu. Kelime sayısı ve `estimated_minutes` (kelime/150) burada hesaplandı.
  - `tools/_l4_kontrol.py` (denetleyici): JSON geçerliliği, zorunlu alanlar, kimlik
    tutarlılığı, gerçek kelime sayısının aralıkta olması ve `word_count` ile uyuşması,
    `estimated_minutes` doğruluğu, konuşmacı kodlarının tanımlı ve hepsinin kullanılmış
    olması, `accent`/`voice` eşitliği, aksan dağılımının tablodaki gibi olması,
    `answer_points` sayısı (≥15), `distractor` sayısı (≥3), id tekrarı, her alıntının kendi
    repliğinde birebir ve metnin tamamında **tek** geçmesi, `speaker` alanının replikle
    uyuşması, `kind` değerlerinin izinli listede olması, bilgi noktalarının metne yayılması
    (her çeyrekte en az 2), S2'de plan öğesi sayısı + yön belirteçleri + her etiketin metinde
    geçmesi, S1/S3/S4'te `spatial_description`ın boş olması, S3'te en az iki konuşmacıdan ayrı
    görüş, S1'de harf harf söyleme, "IELTS" geçmemesi, kelime sınırlı Amerikan yazımı taraması
    ve metinde rakam bulunmaması denetlendi. **İlk turda iki uyarı çıktı, ikisi de düzeltildi:**
    (1) plan öğesi `general waste containers` metinde birebir geçmiyordu — S2 metnindeki cümle
    "the two large containers for general waste" olarak yazılıp etiket `containers for general
    waste` yapıldı; (2) Amerikan yazımı taraması `check` kelimesini yakalıyordu — bu **yanlış
    alarmdı**, İngiliz İngilizcesinde de "check" fiili doğrudur (Amerikan/İngiliz farkı para
    anlamındaki `check`/`cheque` çiftidir), tarama listesi düzeltildi. Düzeltmeden sonra
    **hata 0**.
  - İlk taslakta üç bölümün kelime sayısı hedefin üstündeydi (1135 / 1099 / 1316); bilgi
    noktası taşımayan süs cümleleri budanarak aralığa çekildi (890 / 946 / 949; S1 zaten
    842 idi). **Hiçbir `answer_point` elenmedi** — en büyük budama 4. bölümdeydi (dersin
    düzenlemeye dair ara yorum paragrafı kaldırıldı, kalan paragraflar sıkıştırıldı), 2.
    bölümde tanıtım konuşmasının tekrar eden nezaket cümleleri atıldı.
  - Ardından `python tools/dogrula.py`: **şema hatası 0**, pasaj lisansı eksik 0, görünür
    metinde IELTS 0, yasak kaynak 0. ("L4 0/40 EKSIK" satırı beklenen durumdur.)
- **Yazım/telif kararları:** İngiliz İngilizcesi — metinde geçen ayırt edici biçimler `centre`,
  `licence` (isim), `single-storey`, `colour`, `metres`, `tyre`, `kilometres`. Amerikan
  karşılıkları (`center`, `color`, `program`, `analyze`, `toward`, `behavior`, `gray`, `curb`,
  `elevator` vb.) kelime sınırlı düzenli ifadeyle tarandı, hiçbiri geçmiyor.
  ⚠️ **Bilinçli istisna:** 4. bölümde `meter` iki kez geçiyor ama **ölçüm aleti** anlamında
  (sound level meter); uzunluk birimi her yerde `metre`/`metres`. İngiliz İngilizcesinde bu
  ayrım doğrudur, bu yüzden `meter` tarama listesinden çıkarıldı — sonraki oturumlar bunu
  bilerek kullansın. Metinde **hiç rakam yok**; sayılar konuşulduğu gibi yazıldı (`nineteen
  eighty-four`, `oh seven nine three, double four one, eight oh six`, `two hundred and fifty`,
  `four eighty-two`). 1. bölümde harf harf söyleme bir kez var (`Thurlbeck —
  T-H-U-R-L-B-E-C-K`). Bütün kişi/kurum/yer adları uydurma (Marchwood Coaches, Ruth Thurlbeck,
  Canal Road, Halstock, Ferry Lane, Fenwick Street, Idris, Anneke). 4. bölümde **hiçbir gerçek
  ülke, şehir ya da kurum adı anılmadı** ("in many countries" gibi genel ifadeler kullanıldı);
  din, siyaset, savaş, hastalık, kişisel dram yok — gürültünün sağlık etkileri yerine
  rahatsızlık algısı, ölçüm ve planlama üzerinde duruldu.
- ℹ️ **Konu çakışması kontrolü:** L3 notunda "L4–L6'da tohum/bahçe temasına bir daha
  girilmemesi iyi olur" deniyordu; L4-S2'de `garden waste bays` geçiyor ama bu bahçecilik
  değil **atık ayrıştırması** bağlamındadır, konu tekrarı sayılmadı. L4-S4 (gürültü) bilinçli
  olarak **deniz gürültüsü** ve **gece ışığı / yaban hayat** açılımlarından uzak tutuldu, ki
  L5–L6'da "deniz plastikleri" ve "yapay ışık ve doğa" konuları serbest kalsın.
- **Referans PDF'leri:** `note-completion` ve `plan-map-diagram-labelling` dinleme
  transkriptleri bu oturumda `Read` ile doğrudan açıldı (metin katmanlı PDF'ler);
  `ielts-listening-sample-tasks-2023.pdf` yine render gerektirdiği için açılamadı
  (`referans/text/` klasörü hâlâ yok). Transkriptlerden yalnız konuşma ritmi, duraksama ve
  bilgi verme hızı alındı; **tek bir replik kopyalanmadı**, sahne/isim/senaryo taklit edilmedi
  (ikinci el mobilya ilanı ve quilt shop turu sahnelerinin hiçbiri kullanılmadı).
- Atlanan/sorun: yok. **OPUS5-20'de 6 testten 4'ü tamam;** kalan L5, L6.

## OPUS5-21 (1. çalıştırma: L1 — güvenli sorular, 29 soru)

- Tarih: 2026-08-04
- Depo kontrolü: `content/listening/tests/` ve `content/listening/practice/` **tamamen
  boştu**, NOTLAR.md'de OPUS5-21 kaydı yoktu → çalıştırma listesindeki ilk üretilmemiş
  paket **L1** idi, o yapıldı. Ön koşul sağlandı: `L1-S1` … `L1-S4` senaryoları yerinde.
- 11–15 ve 21–26 aralıkları **boş bırakıldı** (FABLE5-43'ün işi); `tools/dogrula.py`
  "L1 29/40 EKSIK eksik=[11–15, 21–26]" diyor, beklenen durum budur.

### Seçilen tipler ve dosyalar

| Soru | Bölüm | Tip | Dosya | Kelime sınırı |
|---|---|---|---|---|
| 1–10 | S1 | `form_completion` | `content/listening/tests/L1/form-completion.json` | TWO WORDS |
| 16–20 | S2 | `plan_map_diagram_labelling` (**harf seçme**, A–H) | `…/plan-map-diagram-labelling.json` | — |
| 27–30 | S3 | `sentence_completion` | `…/sentence-completion.json` | TWO WORDS |
| 31–36 | S4 | `note_completion` | `…/note-completion.json` | TWO WORDS |
| 37–40 | S4 | `short_answer` | `…/short-answer.json` | THREE WORDS |

- **1–10 için tip seçimi:** senaryo telefonla **kayıt/rezervasyon** olduğu için kural
  gereği **form**.
- **31–40 bölünmesi:** 31–36 tamamlama + 37–40 kısa cevap. ⚠️ **L2–L6 için:** altı
  testte hepsi aynı olmayacak → en az iki testte `31–35 akış şeması + 36–40 not`
  düzeni, en az birinde de 1–10 bloğunda **tablo** (karşılaştırma içeren senaryoda)
  kullanılsın.
- **Etiketleme alt tipi:** L1'de **harf seçme** (A–H). ⚠️ **L2'de kelime yazma** alt
  tipi (`options: null`, `word_limit` dolu) kullanılacak, sonra dönüşümlü devam.

### Kullanılan `answer_point_id` değerleri

| Set | Kimlikler |
|---|---|
| `L1-form-completion` | `L1-S1-01`, `L1-S1-03`, `L1-S1-04`, `L1-S1-06`, `L1-S1-08`, `L1-S1-10`, `L1-S1-12`, `L1-S1-14`, `L1-S1-15`, `L1-S1-17` |
| `L1-note-completion` | `L1-S4-01`, `L1-S4-05`, `L1-S4-09`, `L1-S4-13`, `L1-S4-16`, `L1-S4-19` |
| `L1-plan-map-diagram-labelling` | `L1-S2-15`, `L1-S2-17`, `L1-S2-18`, `L1-S2-19`, `L1-S2-20` |
| `L1-sentence-completion` | `L1-S3-22`, `L1-S3-23`, `L1-S3-25`, `L1-S3-28` |
| `L1-short-answer` | `L1-S4-21`, `L1-S4-28`, `L1-S4-26`, `L1-S4-29` |

- Çeldiricili bilgi noktasından çıkan sorular (cevap her zaman **düzeltilmiş** değer):
  `L1-S1-03` (Otters→Kingfisher), `L1-S1-04` (13→20 Temmuz), `L1-S1-06` (9.00→9.15),
  `L1-S1-08` (210→185 pound), `L1-S1-12` (kart→banka havalesi), `L1-S1-15`
  (kano→okçuluk), `L1-S3-22` (geçen yılın el kitabı→ders sayfası), `L1-S4-09`
  (5.000→2.000 m²), `L1-S4-13` (15 kat→∼3 kat), `L1-S4-19` (egzersiz→temas),
  `L1-S4-26` (üçte bir→yüzde beş). Toplam **11 soru**.

### Senaryo dosyalarına eklenen üç yeni bilgi noktası

Prompt "yeni bilgi noktası kullandıysan senaryo dosyasını güncelleyip yeni id ekle"
dediği için `answer_point_id` **hiçbir yerde null bırakılmadı**; üç soru için senaryoya
yeni kayıt açıldı. **Replik metinlerine dokunulmadı**, sadece `answer_points` dizisi
büyüdü ve `turn_index` sıralaması korundu:

- `L1-S3-28` — "Don't open with a definition of community energy" (replik 33) → soru 30
- `L1-S4-28` — "…a kilogram of lettuce is substantial" (replik 9) → soru 38
- `L1-S4-29` — "The failures are usually more instructive." (replik 12) → soru 40

ℹ️ Bu üçü ilk turda `L1-S3-27` / `L1-S4-23` / `L1-S4-27` kimlikleriyle yazılmıştı;
denetleyici, bilgi noktasının `quote`/`value` alanında cevabın geçmediğini yakaladı.
**Sonraki oturumlar dikkat etsin:** aynı replikte birden çok bilgi noktası varsa
`turn_index` tutar ama kimlik yanlış olabilir — kimliği `turn_index` değil **içerik**
üzerinden doğrulayın.

### Doğrulama

L1–L4 senaryo oturumlarındaki iki betikli düzen tekrarlandı; ikisi de iş bitince silindi.

- `tools/_o21_uret.py` (üretici): `turn_index` elle yazılmadı — her `evidence` senaryo
  repliklerinde arandı, **birden çok replikte geçiyorsa ya da hiç geçmiyorsa üretim
  durdu**. 2. bölümün SVG planı da koddan üretildi (elle kaçış karakteri yazılmadı).
- `tools/_o21_kontrol.py` (denetleyici; üreticiden bağımsız, her şeyi diskten okur):
  zarf/item alanları, kimlik tutarlılığı, `evidence`in senaryoda **birebir ve tek**
  geçmesi, `turn_index` doğruluğu, `answer_point`in gerçekten o bilgiyi taşıması,
  kimlik tekrarı, cevabın kanıtta birebir geçmesi (rakamlı cevaplarda esnek),
  `accepted_variants` dahil kelime sınırı, yönergede sınırın yazılı olması,
  açıklamaların Türkçe olması, `difficulty`, prompt–`stem_block` eşleşmesi, tipe göre
  `stem_block`/`table`/`visual` null kuralları, bölüm içi **sıra kuralı**, soru
  numaralarının planla birebir aynı olması, 11–15 / 21–26 aralıklarının boş kalması ve
  "IELTS" taraması. **İlk turda 39 uyarı çıktı, hepsi düzeltildi**; en önemli ikisi:
  (1) açıklamalar ASCII Türkçe yazılmıştı — `tools/dogrula.py` diyakritik arıyor,
  hepsi gerçek Türkçe karakterlerle yeniden yazıldı; (2) bazı `accepted_variants`
  değerleri kendi kelime sınırını aşıyordu ("quarter past nine", "a hundred and
  eighty-five", "the department office"…) — bunlar atıldı, çünkü aday böyle yazsa
  gerçek sınavda yanlış sayılırdı.
- SVG **geometrik olarak** da sınandı (depoda SVG → PNG çevirici yok): bütün
  koordinatların `viewBox` içinde kalması, her harf dairesinin **tam olarak bir**
  odanın içine düşmesi, her yazının kendi dikdörtgenine sığması. **Bir gerçek hata
  bulundu:** `STAIRS` etiketi merdiven dikdörtgeninin **altına**, yani vestiyerin
  (soru 17'nin cevabı olan C odasının) içine düşüyordu; etiket yukarı alındı, tarama
  çizgileri seyreltildi. ⚠️ **Sonraki etiketleme oturumları bu kontrolü mutlaka
  yapsın** — JSON geçerli olduğu için hiçbir şema denetimi bunu yakalamıyor.
- Ardından `python tools/dogrula.py`: **şema hatası 0**, görünür metinde IELTS 0,
  yasak kaynak 0.

### Bilinçli sapmalar

1. **"İki cevap aynı replikte olmasın" kuralı 2. bölümde uygulanamadı.** Plan tarifi
   tek kişilik anlatımın 6–9. repliklerinde (paragraflarında) geçiyor; 5 soru için
   4 paragraf var, matematiksel olarak imkânsız. Kural **cümle düzeyinde** uygulandı:
   16–17 aynı paragrafta ama **ayrı cümlelerde**, 18–19 keza. Denetleyici bunu `UYARI`
   sayar; aynı **cümlede** iki cevap olsaydı `HATA` verirdi.
2. Aynı gerekçeyle 4. bölümde (12 paragraflık ders, 10 soru) her paragrafta **en fazla
   bir** cevap kuralı uygulandı; paragraflar 70–100 kelime olduğu için nefes payı
   fazlasıyla var. 1. ve 3. bölümde (gerçek diyalog) kural **tam** uygulandı: iki cevap
   arasında her zaman en az bir replik geçiyor.
3. Etiketleme setinde bütün cevaplar doğal olarak `place` türünde; "aynı tür yığılmasın"
   kuralı bu tipe uygulanamaz. Diğer setlerde tür dağılımı geniş (1. bölüm: isim, grup
   adı, tarih, saat, iki fiyat, telefon, ödeme yöntemi, iki nesne).

### Plan çizimi (2. bölüm)

- `viewBox="0 0 480 360"`, sabit `width`/`height` yok, sadece `rect`/`circle`/`line`/
  `polygon`/`text`, hep `#000` çizgi, dolgu yok, tek satır string.
- **Sabit referanslar (etiketi verilmiş):** `MAIN ENTRANCE` (+ içeri bakan ok),
  `TICKET DESK`, `SHOP`, `STAIRS`, `corridor` ve kuzey oku `N`. Aday nereden
  başlayacağını biliyor.
- **Harf yerleşimi bilerek karıştırıldı** (cevaplar F, C, H, A, E). Odalar saat yönünde
  harflenseydi cevaplar A, B, C, D, E çıkacaktı ve tahmin edilebilir olurdu.
- Kullanılmayan çeldirici konumlar: B = asansör, D = avlu bahçesi, G = adlandırılmamış
  oda. B ve D metinde geçen gerçek mekânlar, yani "duydum ama yeri bu değil" tuzağı.

### Telif / yazım

- İngiliz İngilizcesi (`theatre`, `metres`, `fortnight`, `commonest`); Amerikan yazım
  tarandı, yok. Görünür metinde "IELTS" yok.
- Referans PDF'lerinden bu oturumda `note-completion` ve `plan-map-diagram-labelling`
  **cevap anahtarları** açıldı (`referans/text/` klasörü hâlâ yok, PDF'ler doğrudan
  `Read` ile okundu). İkisi de yalnızca numara + cevap listesi; **tek bir soru metni,
  senaryo ya da plan kopyalanmadı** — sadece cevap anahtarı biçimi (harf yazımı,
  "12 years" gibi sayı+birim gösterimi) doğrulandı. Yönerge kalıpları ("Complete the
  form below…", "Label the plan below. Write the correct letter, A–H…") format
  referansıdır, telif kapsamında değildir.
- Bütün kişi/kurum/yer adları senaryolardan geliyor, hepsi uydurma.
- Atlanan/sorun: yok. **OPUS5-21'de 12 paketten 1'i tamam;** sıradaki **L2**.

## OPUS5-21 (2. çalıştırma: L2 — güvenli sorular, 29 soru)

- Tarih: 2026-08-04
- Depo kontrolü: `content/listening/tests/` altında **yalnızca `L1/`** vardı,
  `content/listening/practice/` boştu → çalıştırma listesindeki ilk üretilmemiş paket
  **L2** idi, o yapıldı. Ön koşul sağlandı: `L2-S1` … `L2-S4` senaryoları yerinde.
- 11–15 ve 21–26 aralıkları **boş bırakıldı** (FABLE5-43'ün işi); `tools/dogrula.py`
  "L2 29/40 EKSIK eksik=[11–15, 21–26]" diyor, beklenen durum budur.

### Seçilen tipler ve dosyalar

| Soru | Bölüm | Tip | Dosya | Kelime sınırı |
|---|---|---|---|---|
| 1–10 | S1 | `table_completion` | `content/listening/tests/L2/table-completion.json` | TWO WORDS |
| 16–20 | S2 | `plan_map_diagram_labelling` (**kelime yazma**) | `…/plan-map-diagram-labelling.json` | TWO WORDS |
| 27–30 | S3 | `sentence_completion` | `…/sentence-completion.json` | TWO WORDS |
| 31–35 | S4 | `flow_chart_completion` | `…/flow-chart-completion.json` | TWO WORDS |
| 36–40 | S4 | `note_completion` | `…/note-completion.json` | TWO WORDS |

Üç seçim de L1'in bıraktığı nota uyuyor (L1 kaydındaki ⚠️ maddeleri):

- **1–10 için tip:** senaryo yine bir rezervasyon, ama içinde gerçek bir **karşılaştırma**
  var (paketlemesiz 340 £ / paketlemeli 410 £, cumartesi / cuma) → kural gereği **tablo**.
  Altı testte hepsi `form` olmasın diye bilinçli seçim; L1 = form, L2 = tablo.
  ⚠️ **L3–L6:** en az bir testte de `note_completion` denensin.
- **31–40 bölünmesi:** L1 = 31–36 not + 37–40 kısa cevap; L2 = **31–35 akış şeması +
  36–40 not**. ⚠️ **L3–L6:** en az bir testte daha akış şeması, en az birinde de
  `summary_completion` + kısa cevap düzeni kullanılsın.
- **Etiketleme alt tipi:** L1 harf seçme (A–H) idi, L2 **kelime yazma**
  (`options: null`, `word_limit` dolu). ⚠️ **L3 harf seçme**, sonra dönüşümlü devam.

### Kullanılan `answer_point_id` değerleri

| Set | Kimlikler |
|---|---|
| `L2-table-completion` | `L2-S1-01`, `L2-S1-02`, `L2-S1-03`, `L2-S1-06`, `L2-S1-08`, `L2-S1-10`, `L2-S1-12`, `L2-S1-14`, `L2-S1-15`, `L2-S1-21` |
| `L2-plan-map-diagram-labelling` | `L2-S2-15`, `L2-S2-26`, `L2-S2-27`, `L2-S2-28`, `L2-S2-20` |
| `L2-sentence-completion` | `L2-S3-17`, `L2-S3-19`, `L2-S3-20`, `L2-S3-22` |
| `L2-flow-chart-completion` | `L2-S4-27`, `L2-S4-01`, `L2-S4-05`, `L2-S4-10`, `L2-S4-12` |
| `L2-note-completion` | `L2-S4-14`, `L2-S4-16`, `L2-S4-21`, `L2-S4-23`, `L2-S4-25` |

- Çeldiricili bilgi noktasından çıkan sorular (cevap her zaman **düzeltilmiş** değer):
  `L2-S1-03` (Selby Lane→Weir Street), `L2-S1-08` (3 Ekim cumartesi→2 Ekim cuma),
  `L2-S1-10` (salı 10.30→salı 11.00), `L2-S1-14` (battaniye→ahşap sandık),
  `L2-S1-15` (5→6 saat), `L2-S2-20` (pencerenin yanı→tam karşısı), `L2-S3-19`
  (3.000→2.500 kelime), `L2-S3-20` (ayın 12'si→19'u), `L2-S4-01` (yüzde bir→binde bir),
  `L2-S4-14` (saf kireç→kireç + ezilmiş çömlek), `L2-S4-23` (10→12 gün).
  Toplam **11 soru**.

### Senaryo dosyalarına eklenen dört yeni bilgi noktası

`answer_point_id` hiçbir yerde null bırakılmadı; karşılığı olmayan dört bilgi için
senaryoya yeni kayıt açıldı (`tools/_o21b_nokta_ekle.py`, iş bitince silindi).
**Replik metinlerine dokunulmadı**, sadece `answer_points` dizisi büyüdü ve dizi
`turn_index` sırasında kalacak şekilde araya eklendi (bu yüzden kimlik numaraları
artık sıralı değil, ama `turn_index` sıralı — betik bunu doğruluyor):

- `L2-S2-26` — "Opposite that, on the far side of the room, is the children's library"
  (replik 6) → soru 17
- `L2-S2-27` — "Between the children's library and the lift there's a small room we're
  calling the meeting room." (replik 7) → soru 18
- `L2-S2-28` — "behind the fiction shelves, you'll find the computer suite"
  (replik 7) → soru 19
- `L2-S4-27` — "rain that fell on high ground sits in gravel below the surface"
  (replik 1) → soru 31

ℹ️ L2-S2'de plan tarifi için hazır bilgi noktası yalnızca dört taneydi (15, 16, 17, 20)
ve 15 ile 16 **aynı cümlede** geçiyor; beş soruluk bir etiketleme seti için yeni nokta
açmak zorunluydu. L1'in uyarısına uyularak kimlikler `turn_index` üzerinden değil
**içerik** üzerinden eşleştirildi; denetleyici de cevabın bilgi noktasının
`quote`/`value` alanında geçmesini şart koşuyor.

### Doğrulama

L1 oturumundaki iki betikli düzen tekrarlandı, üstüne bir de ASCII izdüşüm betiği
yazıldı; üçü de iş bitince silindi.

- `tools/_o21b_uret.py` (üretici): `turn_index` elle yazılmadı — her `evidence` senaryo
  repliklerinde arandı, **birden çok replikte geçiyorsa ya da hiç geçmiyorsa üretim
  durdu**; ayrıca bulunan replik ile bilgi noktasının `turn_index` değeri karşılaştırıldı.
  Plan SVG'si koddan üretildi (elle kaçış karakteri yazılmadı).
- `tools/_o21b_kontrol.py` (denetleyici; üreticiden bağımsız, her şeyi diskten okur):
  zarf/item alanları, `evidence`in senaryoda **birebir ve tek** geçmesi, `turn_index`
  doğruluğu, bilgi noktasının gerçekten o bilgiyi taşıması, kimlik tekrarı, cevabın
  kanıtta birebir geçmesi (rakamlı cevaplarda esnek), cevabın `accepted_variants`
  içinde olması, **`accepted_variants` dahil** kelime sınırı, yönergede sınırın yazılı
  olması, açıklamaların gerçek Türkçe karakter içermesi, `difficulty`, prompt ile
  `stem_block`/tablo eşleşmesi, gövdedeki boşluk numaralarının item numaralarıyla birebir
  aynı olması, tipe göre `stem_block`/`table`/`visual` null kuralları, bölüm içi **sıra
  kuralı**, soru numaralarının planla birebir aynı olması, 11–15 / 21–26 aralıklarının
  boş kalması ve "IELTS" taraması. **Sonuç: 0 hata, 1 uyarı** (aşağıdaki bilinçli sapma).
- SVG yine **geometrik olarak** sınandı (depoda SVG → PNG çevirici yok; `cairosvg`,
  `svglib`, `Pillow`, `matplotlib` — hiçbiri kurulu değil): bütün koordinatların
  `viewBox` içinde kalması, izinli öge/renk listesi, sabit `width`/`height` olmaması,
  **hiçbir yazının bir dikdörtgenin kenarını kesmemesi** (L1'deki `STAIRS` hatasının
  tekrarını önleyen kontrol), oda dikdörtgenlerinin çakışmaması, her boşluk numarasının
  **tam olarak bir** odanın içinde olması ve o odada başka yazı bulunmaması, kuzey oku
  ile giriş etiketinin varlığı.
- `tools/_o21b_ascii.py` planı kaba bir ASCII izdüşüme çevirdi ve yerleşim **gözle**
  okundu: 19 sol üst, roman raflarının üstünde; 17 sağ üst (bahçe kapılı), 18 ile
  asansör onun altında; 16 girişin solunda; gazete/dergi sağ ön cephede; birinci katta
  20 merdiven başının solunda, sessiz çalışma odasının karşısında. Tarifle birebir uyuyor.
- Ardından `python tools/dogrula.py`: **şema hatası 0**, görünür metinde IELTS 0,
  yasak kaynak 0, L2 29/40.

### Bilinçli sapmalar

1. **"İki cevap aynı replikte olmasın" kuralı 2. bölümde yine tam uygulanamadı.**
   Plan tarifi tek kişilik anlatımın 5–8. repliklerinde (paragraflarında) geçiyor; 5 soru
   için 4 paragraf var. **18 ile 19 aynı paragrafta ama ayrı cümlelerde** (aralarında
   toplantı odası kiralama ücreti cümlesi var). Denetleyici bunu `UYARI` sayar; aynı
   **cümlede** olsalardı `HATA` verirdi. Bu yüzden 15 (iade makinesi) ile 16 (danışma
   masası) bilgi noktalarından yalnızca biri soruya çevrildi — ikisi tek cümlede geçiyor,
   diğeri planda **sabit referans** olarak verildi.
2. 4. bölümde (14 paragraflık ders, 10 soru) her paragrafta **en fazla bir** cevap
   kuralı uygulandı; sorular 1., 2., 3., 4., 5., 6., 7., 10., 11. ve 12. repliklere
   dağıldı. 1. ve 3. bölümde kural **tam** uygulandı: iki cevap arasında her zaman en az
   bir replik var (1. bölümde en az iki replik).
3. Etiketleme setinde bütün cevaplar doğal olarak yer adı; "aynı tür yığılmasın" kuralı
   bu tipe uygulanamaz. Diğer setlerde tür dağılımı geniş — 1. bölüm 5 kelime / 5 sayı
   dengesinde (soyadı, sokak adı, yerleşim adı, eşya, madde ↔ telefon, gün, saat, fiyat,
   süre); 4. bölümde 10 sorunun yalnızca 2'si sayı.

### Plan çizimi (2. bölüm) — kelime yazma alt tipi

- `viewBox="0 0 500 620"`, sabit `width`/`height` yok, sadece `rect`/`line`/`polygon`/
  `text`, hep `#000` çizgi, dolgu yok, tek satır string. **İki katlı**: üstte
  `GROUND FLOOR`, altta `FIRST FLOOR` — kahve köşesi (20) yalnızca birinci katta
  anlatıldığı için ikinci kat çizmek zorunluydu.
- Boşluklar `16 .........` biçiminde **numara + noktalı çizgi** (harf seçme alt tipinde
  daireli harfler kullanılmıştı).
- **Sabit referanslar (etiketi verilmiş):** `MAIN ENTRANCE (Grange Road)` (+ içeri bakan
  ok), `ENQUIRY DESK`, `NEWSPAPERS AND MAGAZINES`, `FICTION SHELVES`, `LIFT`, `GARDEN`,
  `STAIRS`, `QUIET STUDY ROOM`, `LOCAL HISTORY ROOM`, `landing` ve kuzey oku `N`.
- Her boşluğun **bağımsız** bir çıpası var, aday zincire mecbur kalmasın diye:
  16 → girişin solu; 17 → bahçeye açılan kapı; 18 → çocuk kütüphanesi ile asansör arası;
  19 → roman raflarının arkası; 20 → çalışma odasının karşısı + merdiven başı.
- ⚠️ Bilinen küçük kusur: 17 numaralı odanın bahçe kapısı, odanın kendi dikdörtgen kenarı
  (x=398) ile dış duvardaki boşluk (x=400) üst üste geldiği için "kesik duvar" yerine
  bahçeye giden **iki paralel çizgi** olarak okunuyor. Belirsizlik yaratmıyor (17'nin
  yerini ayrıca "gazete alanının karşısı, salonun öbür ucu" tarifi de veriyor), ama
  sonraki etiketleme oturumları kapı boşluğu istiyorsa odayı `rect` yerine **dört ayrı
  `line`** ile çizsin.

### Telif / yazım

- İngiliz İngilizcesi (`metres`, `fortnight`, `per cent`, `£`); Amerikan yazım tarandı,
  yok. Görünür metinde "IELTS" yok.
- Referans PDF'lerinden bu oturumda `table-completion`, `flow-chart-completion` ve
  `sentence-completion` **cevap anahtarları** açıldı (`referans/text/` klasörü hâlâ yok,
  PDF'ler doğrudan `Read` ile okundu). Üçü de yalnızca numara + cevap listesi; **tek bir
  soru metni, senaryo ya da plan kopyalanmadı** — sadece cevap anahtarı biçimi
  (`tutor(s)`, `time(-)management` gibi esneklik gösterimi) doğrulandı. Yönerge kalıpları
  ("Complete the table below…", "Complete the flow-chart below…", "Label the plan
  below…") format referansıdır, telif kapsamında değildir.
- Bütün kişi/kurum/yer adları senaryolardan geliyor, hepsi uydurma.
- Atlanan/sorun: yok. **OPUS5-21'de 12 paketten 2'si tamam;** sıradaki **L3**.

---

## OPUS5-21 (3. çalıştırma: L3 — güvenli sorular, 29 soru)

- Tarih: 2026-08-04
- Depo kontrolü: `content/listening/tests/` altında **`L1/` ve `L2/`** vardı,
  `content/listening/practice/` boştu → çalıştırma listesindeki ilk üretilmemiş paket
  **L3** idi, o yapıldı. Ön koşul sağlandı: `L3-S1` … `L3-S4` senaryoları yerinde.
- 11–15 ve 21–26 aralıkları **boş bırakıldı** (FABLE5-43'ün işi); `tools/dogrula.py`
  "L3 29/40 EKSIK eksik=[11–15, 21–26]" diyor, beklenen durum budur.

### Seçilen tipler ve dosyalar

| Soru | Bölüm | Tip | Dosya | Kelime sınırı |
|---|---|---|---|---|
| 1–10 | S1 | `form_completion` | `content/listening/tests/L3/form-completion.json` | **ONE WORD** |
| 16–20 | S2 | `plan_map_diagram_labelling` (**harf seçme, A–H**) | `…/plan-map-diagram-labelling.json` | — (harf) |
| 27–30 | S3 | `sentence_completion` | `…/sentence-completion.json` | TWO WORDS |
| 31–36 | S4 | `summary_completion` | `…/summary-completion.json` | TWO WORDS |
| 37–40 | S4 | `short_answer` | `…/short-answer.json` | THREE WORDS |

L2'nin bıraktığı uyarılardan ikisi bu oturumda kapatıldı:

- **Etiketleme alt tipi:** L1 harf seçme, L2 kelime yazma, **L3 yine harf seçme** —
  dönüşüm sürüyor. ⚠️ **L4 kelime yazma** olsun.
- **31–40 bölünmesi:** L1 = not + kısa cevap, L2 = akış şeması + not,
  **L3 = özet (31–36) + kısa cevap (37–40)** — L2'nin istediği `summary_completion`
  düzeni kullanıldı. ⚠️ **L4–L6:** en az birinde akış şeması tekrar denensin, altı
  testin hepsi aynı olmasın.
- **1–10 için tip:** L3-S1 bir spor merkezine **üyelik kaydı** (ad, adres, telefon,
  ödeme talimatı) → kural gereği **form**. L2'nin "en az bir testte `note_completion`
  denensin" uyarısı bu senaryoya uymuyordu. ⚠️ **L4 buna en uygun aday:** L4-S1 bir
  **kayıp eşya bildirimi** (kayıt/rezervasyon değil, karşılaştırma da yok) → orada
  `note_completion` kullanılsın.
- **Kelime sınırında yenilik:** 1. bölümün on cevabı da tek kelime ya da tek sayı olacak
  şekilde seçildi, böylece ilk kez `ONE WORD AND/OR A NUMBER` yönergesi kullanılabildi
  (L1 ve L2'de bütün setler TWO WORDS'tü; sınır çeşitliliği artsın diye).

### Kullanılan `answer_point_id` değerleri

| Set | Kimlikler |
|---|---|
| `L3-form-completion` | `L3-S1-01`, `L3-S1-02`, `L3-S1-05`, `L3-S1-07`, `L3-S1-10`, `L3-S1-11`, `L3-S1-13`, `L3-S1-16`, `L3-S1-21`, `L3-S1-22` |
| `L3-plan-map-diagram-labelling` | `L3-S2-15`, `L3-S2-18`, `L3-S2-20`, `L3-S2-22`, `L3-S2-35` |
| `L3-sentence-completion` | `L3-S3-21`, `L3-S3-23`, `L3-S3-24`, `L3-S3-26` |
| `L3-summary-completion` | `L3-S4-01`, `L3-S4-05`, `L3-S4-08`, `L3-S4-10`, `L3-S4-14`, `L3-S4-15` |
| `L3-short-answer` | `L3-S4-27`, `L3-S4-20`, `L3-S4-21`, `L3-S4-25` |

- Çeldiricili bilgi noktasından çıkan sorular (cevap her zaman **düzeltilmiş** değer):
  `L3-S1-02` (flat 2 → flat 9), `L3-S1-07` (saat 5 → saat 4), `L3-S1-10` (ayın 15'i →
  ayın 1'i), `L3-S1-13` (bir saat → 40 dakika), `L3-S3-24` (15 → 12 dakika),
  `L3-S3-26` (13 Kasım → 20 Kasım), `L3-S4-05` (30 → 50 bitki), `L3-S4-14` (%75 → %85),
  `L3-S4-15` (5 yıl → 10 yıl). Toplam **9 soru**.
- Kullanılmayan iki büyük çeldirici bilinçli bırakıldı: `L3-S1-15` (Perşembe → Cuma)
  — doğru gün ancak bir **sonraki** replikte kesinleşiyor, komşu replikte zaten 8. soru
  vardı; `L3-S2-08` (5 mil → 4,5 mil) — rota uzunlukları `FABLE5-43`'ün çoktan seçmeli
  alanına daha uygun.

### Senaryo dosyalarına eklenen iki yeni bilgi noktası

`answer_point_id` hiçbir yerde null bırakılmadı; karşılığı olmayan iki bilgi için
senaryoya yeni kayıt açıldı. **Replik metinlerine dokunulmadı**, sadece `answer_points`
dizisine `turn_index` sırası bozulmayacak yere eklendi (kimlik numarası sıralı değil,
`turn_index` sıralı):

- `L3-S2-35` — "the boardwalk across the marsh, between the lake and the meadow"
  (replik 9) → soru 20. Mevcut `L3-S2-25` aynı repliği kullanıyor ama yalnızca **yeniden
  açılış tarihini** taşıyor; haritada gereken şey **konum** bilgisiydi.
- `L3-S4-27` — "a few cross with the neighbouring row" (replik 8) → soru 37. 8. replikteki
  hazır nokta (`L3-S4-18`) soyut bir sonuç cümlesiydi ("artık toplanan popülasyon değil");
  kısa cevap için somut ve tek karşılığı olan bu ifade gerekti.

### Doğrulama

- Bu oturumda **üretim betiği yazılmadı** — beş dosya doğrudan yazıldı, ardından
  bağımsız bir denetleyici (`tools/_l3_kontrol.py`) ve bir ASCII izdüşüm betiği
  (`tools/_l3_ascii.py`) her şeyi **diskten okuyarak** sınadı; ikisi de iş bitince silindi.
- Denetlenenler: her `evidence`in senaryo repliğinde **birebir** geçmesi ve doğru
  `turn_index`te olması, `turn_index`in bilgi noktasıyla uyuşması, set içi **artan sıra**,
  aynı bilgi noktasının iki kez kullanılmaması, **`accepted_variants` dahil** kelime
  sınırı, açıklamaların gerçek Türkçe karakter içermesi, soru numaralarının planla birebir
  aynı olması (29 soru; boş: 11–15, 21–26) ve görünür metinde "IELTS" taraması.
  **Sonuç: 0 hata**, geri kalan yalnızca aşağıdaki 1 numaralı bilinçli sapmanın uyarıları.
- İlk turda çıkan **2 gerçek hata düzeltildi**: soru 4'te `"4 p.m."`, soru 8'de
  `"trainers (indoor)"` varyantları ONE WORD sınırını aşıyordu; ikisi de silindi.
- SVG yine **geometrik olarak** sınandı (depoda SVG → PNG çevirici hâlâ yok): izinli öge
  listesi (`svg rect circle line path polygon text` — dışında öge yok), tek renk `#000`,
  `fill="none"`, sabit `width`/`height` yok, bütün koordinatlar `viewBox` içinde.
- ASCII izdüşüm **gözle** okundu: giriş altta ortada (ok içeri bakıyor), yol yukarı
  çıkıyor, solunda ziyaretçi merkezi — sağında C (otopark) tam karşısında; tuvaletler
  merkezin arkasında; yolun bittiği yerde bilgi kulübesi; A (piknik) kulübe ile göl
  arasında; adacık gölün içinde, G (kuş gözlem) adacıkla **aynı hizada** doğu kıyısında,
  H onun altında; D (kireç ocağı) G'nin ötesinde, gölün en uzak ucunda; E (tahta yol)
  gölün kuzeyindeki sazlık işaretlerinin arasında, göl ile B (çayır) arasında; F
  (seyir noktası) en tepede. Tarifle birebir uyuyor.
- Ardından `python tools/dogrula.py`: **şema hatası 0**, görünür metinde IELTS 0,
  yasak kaynak 0, L3 29/40.

### Bilinçli sapmalar

1. **"İki cevap aynı replikte olmasın" kuralı 1. ve 3. bölümde tam, 2. ve 4. bölümde
   kısmen uygulandı.** 1. bölümde iki cevap arasında her zaman **en az bir replik** var
   (replikler: 5, 7, 10, 12, 16, 18, 20, 26, 30, 32); 3. bölümde de öyle (19, 23, 25, 27).
   2. ve 4. bölüm **tek kişilik anlatım** olduğu için "replik" = paragraf; oralarda
   **her paragrafta en fazla bir cevap** kuralı uygulandı — 2. bölümde 5 soru 5 ayrı
   paragrafa (5, 6, 7, 8, 9), 4. bölümde 10 soru 10 ayrı paragrafa (1, 2, 4, 5, 6, 7, 8,
   9, 10, 11) dağıldı. L1 ve L2'de 2. bölümde aynı paragrafta iki cevap kalmıştı;
   **bu oturumda o da giderildi**, çünkü tahta yolun konumu (replik 9) soruya çevrilerek
   beşinci paragraf kazanıldı.
2. **Harita çeldiricisi:** D (kireç ocağı) ile E (tahta yol) coğrafi olarak yakın —
   ikisi de gölün kuzeyinde. Ayrım iki şeyle kuruluyor: E **sazlık işaretlerinin**
   üstünde ("across the marsh"), D ise **gölün ucunda, gözlem kulübesinin ötesinde**.
   Ayrıca 20 sorulduğunda D zaten 19'un cevabı olarak harcanmış oluyor. Bilerek bırakılan
   zorluk; 20 numaralı soru bu yüzden `hard` işaretlendi.
3. Etiketleme setinde harfler **soru sırasına göre artmıyor** (C, A, G, D, E) — aday
   sırayı tahmin edemesin diye harfler konumlara karışık dağıtıldı. B, F, H hiç doğru
   cevap değil (çayır, seyir noktası, gölet inceleme platformu).
4. Cevap türü dağılımı: 1. bölüm **5 kelime / 5 sayı** (soyadı, yazılı bildirim, spor
   ayakkabısı, telefon, ay adı ↔ daire no, aidat, saat, ödeme günü, dakika); 4. bölümün
   10 sorusunda 4 sayı, 6 kelime/terim; 3. bölümde 2 kelime + 1 sayı + 1 tarih.

### Plan çizimi (2. bölüm) — harf seçme alt tipi

- `viewBox="0 0 540 650"`, sabit `width`/`height` yok, yalnızca `rect`/`circle`/`line`/
  `path`/`polygon`/`text`, hep `#000` çizgi, dolgu yok, tek satır string.
- Bu sefer **bina planı değil, açık alan haritası** (`"kind": "map"`): göl bir `polygon`,
  adacık `circle`, patikalar `path`, bataklık **sazlık tutamları** (üçer kısa `line`)
  ile gösterildi.
- Seçenekler L1'deki gibi **daire içinde harf** (`circle r="11"` + ortalanmış `text`);
  her harf tam olarak bir alanın içinde ve o alanda başka yazı yok.
- **Sabit referanslar (etiketi verilmiş):** `MAIN ENTRANCE (Cranmore Road)` (+ içeri bakan
  ok), `drive`, `VISITOR CENTRE`, `TOILETS`, `INFORMATION HUT`, `LAKE`, `island` ve
  kuzey oku `N`. Aday ister girişten ister gölden başlayabiliyor.
- Her boşluğun **bağımsız** bir çıpası var: C → ziyaretçi merkezinin karşısı, yolun öbür
  yanı; A → bilgi kulübesi ile göl arası; G → adacığın karşısı; D → gölün uzak ucu,
  kulübenin ötesi; E → sazlığın üstü, göl ile çayır arası.

### Telif / yazım

- İngiliz İngilizcesi (`neighbouring`, `per cent`, `£`, `trainers`); Amerikan yazım
  tarandı, yok — yalnızca `accepted_variants` içinde hoşgörü olarak `neighboring`
  kabul ediliyor. Görünür metinde "IELTS" yok.
- ⚠️ **Referans PDF'leri bu oturumda açılamadı:** ortamda `pdftoppm` (poppler) yok,
  `pypdf`/`PyPDF2`/`fitz` de kurulu değil; `referans/text/` klasörü hâlâ yok. Bu yüzden
  yönerge kalıpları ve cevap anahtarı biçimi, aynı PDF'lerden çıkarılmış olan **L1 ve L2
  setlerinden** devralındı ("Complete the form below…", "Label the map below. Write the
  correct letter, A–H, next to Questions 16–20.", "Complete the summary below…",
  "Answer the questions below…"). Yeni bir biçim icat edilmedi; referanstan **tek bir
  cümle, soru ya da senaryo kopyalanmadı**.
- Bütün kişi/kurum/yer adları senaryolardan geliyor, hepsi uydurma.
- Atlanan/sorun: yok. **OPUS5-21'de 12 paketten 3'ü tamam;** sıradaki **L4**.

## OPUS5-21 (4. çalıştırma: L4 — güvenli sorular, 29 soru)

- Tarih: 2026-08-04
- Depo kontrolü: `content/listening/tests/` altında **`L1/`, `L2/` ve `L3/`** vardı,
  `content/listening/practice/` boştu → çalıştırma listesindeki ilk üretilmemiş paket
  **L4** idi, o yapıldı. Ön koşul sağlandı: `L4-S1` … `L4-S4` senaryoları yerinde.
- 11–15 ve 21–26 aralıkları **boş bırakıldı** (FABLE5-43'ün işi); `tools/dogrula.py`
  "L4 29/40 EKSIK eksik=[11–15, 21–26]" diyor, beklenen durum budur.

### Seçilen tipler ve dosyalar

| Soru | Bölüm | Tip | Dosya | Kelime sınırı |
|---|---|---|---|---|
| 1–10 | S1 | `note_completion` | `content/listening/tests/L4/note-completion.json` | TWO WORDS |
| 16–20 | S2 | `plan_map_diagram_labelling` (**kelime yazma**) | `…/plan-map-diagram-labelling.json` | TWO WORDS |
| 27–30 | S3 | `sentence_completion` | `…/sentence-completion.json` | TWO WORDS |
| 31–35 | S4 | `short_answer` | `…/short-answer.json` | THREE WORDS |
| 36–40 | S4 | `flow_chart_completion` | `…/flow-chart-completion.json` | **ONE WORD** |

L3'ün bıraktığı üç uyarının **üçü de** bu oturumda kapatıldı:

- **1–10 için tip:** L3, "L4-S1 bir kayıp eşya bildirimi, `note_completion` için en uygun
  aday" demişti — öyle yapıldı. Dört testin dağılımı artık **form / tablo / form / not**.
- **Etiketleme alt tipi:** L1 harf, L2 kelime, L3 harf, **L4 kelime yazma** — dönüşüm
  sürüyor. ⚠️ **L5 harf seçme (A–H)** olsun.
- **31–40 bölünmesi:** L1 = not + kısa cevap, L2 = akış şeması + not, L3 = özet + kısa
  cevap, **L4 = kısa cevap (31–35) + akış şeması (36–40)**. Akış şeması L3'ün istediği
  gibi tekrar denendi. ⚠️ **L5–L6:** dört testte de kullanılmamış bir düzen kalsın diye
  en az birinde `table_completion` 4. bölümde denensin.
- **Sıralama yeniliği:** ilk kez kısa cevap bloğu **önce**, tamamlama bloğu **sonra**
  geldi. Nedeni teknik: L4-S4 dersinde denetim hiyerarşisi (kaynak → yol → alıcı)
  7–11. paragraflarda anlatılıyor; akış şeması oraya oturunca kısa cevaplar zorunlu
  olarak 1–5. paragraflara düştü. Böylece 4. bölümün on cevabı **on ayrı paragrafa**
  dağıldı (1, 2, 3, 4, 5, 7, 8, 9, 10, 11).
- **Kelime sınırı çeşitliliği:** akış şemasının beş cevabı da tek kelime/sayı seçilerek
  `ONE WORD AND/OR A NUMBER` ikinci kez kullanıldı (L3'te 1. bölümdeydi).

### Kullanılan `answer_point_id` değerleri

| Set | Kimlikler |
|---|---|
| `L4-note-completion` | `L4-S1-01`, `L4-S1-02`, `L4-S1-06`, `L4-S1-08`, `L4-S1-10`, `L4-S1-11`, `L4-S1-17`, `L4-S1-19`, `L4-S1-22`, `L4-S1-25` |
| `L4-plan-map-diagram-labelling` | `L4-S2-07`, `L4-S2-11`, **`L4-S2-37` (yeni)**, `L4-S2-13`, `L4-S2-16` |
| `L4-sentence-completion` | `L4-S3-20`, `L4-S3-22`, `L4-S3-25`, `L4-S3-30` |
| `L4-short-answer` | `L4-S4-01`, `L4-S4-05`, `L4-S4-07`, `L4-S4-09`, `L4-S4-12` |
| `L4-flow-chart-completion` | `L4-S4-18`, `L4-S4-20`, `L4-S4-24`, `L4-S4-25`, `L4-S4-29` |

- **Senaryoya eklenen tek yeni bilgi noktası:** `L4-S2-37` — "the left-hand side takes you
  up the ramp" (5. replik, rampanın konumu). 18 numaralı soru buna dayanıyor; şema
  gereği `answer_point_id` boş bırakılmadı, `content/listening/scripts/L4-S2.json`
  güncellendi. Başka hiçbir senaryo dosyasına dokunulmadı.
- Çeldiricili bilgi noktasından çıkan sorular (cevap her zaman **düzeltilmiş** değer):
  `L4-S1-01` (486 → 482), `L4-S1-02` (Salı → Çarşamba), `L4-S1-08` (lacivert → koyu
  yeşil), `L4-S1-25` (5 £ → 3 £), `L4-S3-20` (2 gün → 3 iş günü), `L4-S3-25` (seminer
  bloğu → kütüphane atriyumu), `L4-S4-05` (10 dB → 3 dB), `L4-S4-09` (3 yıl → 5 yıl),
  `L4-S4-12` (üçte iki → beşte dört), `L4-S4-25` (10 m → 30 m). Toplam **10 soru** —
  şimdiye kadarki en yüksek oran (29 sorunun 10'u).
- Bilinçli kullanılmayan çeldiriciler: `L4-S1-16` (iki hafta → üç ay) — üç ay değeri
  7. sorunun kökünde veri olarak zaten yazılı, iki kez sorulmadı; `L4-S2-12`
  (3 → 4 bahçe atığı bölmesi) ve `L4-S2-25` (Çarşamba → Salı) — ikisi de `FABLE5-43`'ün
  çoktan seçmeli alanına daha uygun, ona bırakıldı; `L4-S3-23` (11 → 18) ve `L4-S3-27`
  (5 → 2 dakika) — 27–30 aralığında yalnızca dört soru var, 3. bölümün geri kalanı
  `FABLE5-43`'e ait.

### Doğrulama

- Üç geçici betik yazıldı (`tools/_l4_plan.py` çizim + üretim, `tools/_l4_ascii.py`
  ASCII izdüşüm, `tools/_l4_kontrol.py` denetleyici); üçü de **diskten okuyarak** sınadı
  ve iş bitince silindi.
- Denetlenenler: her `evidence`in senaryo repliğinde **birebir** geçmesi ve doğru
  `turn_index`te olması, `turn_index`in bilgi noktasıyla uyuşması, set içi **artan sıra**,
  aynı bilgi noktasının iki kez kullanılmaması, **`accepted_variants` dahil** kelime
  sınırı, açıklamaların gerçek Türkçe karakter içermesi, `answer`ın `accepted_variants`
  içinde olması, `stem_block` boşluk numaralarının item numaralarıyla birebir aynı olması,
  soru numaralarının planla birebir aynı olması (29 soru; boş: 11–15, 21–26) ve görünür
  metinde "IELTS" taraması. **Sonuç: 0 hata**, kalan 12 uyarı yalnızca aşağıdaki 1
  numaralı bilinçli sapmanın uyarıları.
- İlk turda çıkan **5 gerçek hata düzeltildi**, hepsi kelime sınırı: 1. soruda
  `"four eighty two"`, 6. soruda boşluklu iki telefon yazımı, 16. soruda
  `"the site office"`, 19. soruda `"scrap metal skip"` iki kelimeyi aşıyordu. Telefon
  numarasının asıl cevabı bu yüzden bitişik yazıma (`07793441806`) çevrildi.
- SVG yine **geometrik olarak** sınandı (depoda SVG → PNG çevirici hâlâ yok): izinli öge
  listesi (`svg rect line path polygon text` — dışında öge yok), tek renk `#000`,
  `fill="none"`, sabit `width`/`height` yok, bütün koordinatlar `viewBox` içinde, tek
  satır string. Ayrıca **kutu-kutu ve yazı-yazı çakışma taraması** yapıldı: ilk turda iki
  çakışma çıktı (elektrikli eşya deposu ile ilk bahçe atığı bölmesi üst üste biniyordu;
  rampaya giden yol deponun içinden geçiyordu). Bölmeler ve rampa kuzeye kaydırılıp
  yol 382. satıra alındı → **0 çakışma**.
- ASCII izdüşüm **gözle** okundu: giriş altta ortada (ok içeri bakıyor), bariyer yolun
  üstünde, yol kuzeye çıkıyor; solunda 16, onun arkasında tuvaletler/su noktası; sağında
  tam karşısında otopark, otoparkın kuzeyinde uzun bina (yakın uçta 17, ötesinde REUSE
  SHOP), yolun batısında REUSE SHOP'un tam karşısında 20; tam ileride dört bahçe atığı
  bölmesi; ötesinde yol ikiye ayrılıyor, sol kol 18 (yukarı okları var), sağındaki
  konteynerler aşağıdan yukarı WOOD → RUBBLE → 19; ahşabın yanında boya/kimyasal deposu;
  rampanın ucunda iki genel atık konteyneri; oradan çıkışa giden yol üzerinde cam-kutu-
  plastik kumbaraları, sonra çıkış bariyeri. Tarifle birebir uyuyor.
- Ardından `python tools/dogrula.py`: **şema hatası 0**, görünür metinde IELTS 0,
  yasak kaynak 0, L4 29/40.

### Bilinçli sapmalar

1. **"İki cevap aynı replikte olmasın" kuralı 1. ve 3. bölümde tam, 2. ve 4. bölümde
   paragraf düzeyinde uygulandı.** 1. bölümde iki cevap arasında her zaman **en az bir
   replik** var (replikler: 4, 7, 11, 13, 19, 21, 28, 32, 38, 42 — en dar aralık iki
   replik); 3. bölümde de öyle (21, 23, 27, 32). 2. ve 4. bölüm **tek kişilik anlatım**
   olduğu için "replik" = paragraf; oralarda **her paragrafta tam olarak bir cevap**
   kuralı uygulandı — 2. bölümde 5 soru 5 ayrı paragrafa (3, 4, 5, 6, 7), 4. bölümde
   10 soru 10 ayrı paragrafa (1, 2, 3, 4, 5, 7, 8, 9, 10, 11) dağıldı. L1–L3'teki
   uygulamanın aynısı.
2. **4. bölümün son üç paragrafı (ekoloji ve uygulama ödevi) soru dışı bırakıldı.**
   Sebep: paragraf başına bir cevap kuralı korunacaksa 12–14. paragraflar dörtten fazla
   soru taşıyamıyordu ve akış şeması bütün olarak 7–11. paragraflara oturuyordu. L3'te de
   aynı tercih yapılmıştı (orada da son paragraflar boş kalmıştı).
3. **Kelime yazma alt tipinde belirsizlik riski olan iki nokta bilerek soru yapılmadı:**
   tuvaletler (seste "tuvaletler **ve** içme suyu noktası" birlikte geçiyor, iki savunulabilir
   cevap doğardı) ve bahçe atığı bölmeleri (`garden waste bays` üç kelime, TWO WORDS
   sınırını aşardı). İkisi de planda **etiketi verilmiş sabit referans** olarak kullanıldı.
4. **Cevap türü dağılımı:** 1. bölüm **6 kelime / 4 sayı** (Çarşamba, raf, koyu yeşil,
   soyadı, hayır kurumu, yakıt pompaları, banka kartı ↔ 482, telefon, 3 £); 2. bölümün
   beşi de yer adı (kelime yazma alt tipinin doğası); 3. bölümde 3 kelime + 1 sayı;
   4. bölümde 4 sayı/oran (3 dB, beş yıl, beşte dört, 30 m) + 6 kelime.
5. **18 numaralı soru zincirli değil:** rampa, "bahçe atığı bölmelerinin ötesinde yolun
   sol kolu" tarifiyle bulunuyor; bölmeler planda etiketli olduğu için aday 16 ve 17'yi
   bilmeden de 18'i çözebiliyor. Aynı şekilde 19 (ahşap ve moloz yazılı) ve 20 (REUSE
   SHOP yazılı) kendi bağımsız çıpalarına dayanıyor.

### Plan çizimi (2. bölüm) — kelime yazma alt tipi

- `viewBox="0 0 600 800"`, sabit `width`/`height` yok, yalnızca `rect`/`line`/`path`/
  `polygon`/`text`, hep `#000` çizgi, dolgu yok, tek satır string, 70 öge.
- `"kind": "plan"` — bina değil, **saha planı**: yol iki paralel çizgi, rampa yukarı
  yönü iki `path` çevron (ok) ile, giriş/çıkış bariyerleri kalın (`stroke-width="3"`)
  çizgiyle gösterildi.
- Boşluklar **numara + altına kısa çizgi** olarak çizildi (`16`…`20`), harf yok,
  `options` `null`, `word_limit` dolu — kelime yazma alt tipi.
- **Sabit referanslar (etiketi verilmiş):** `MAIN ENTRANCE (Ferry Lane)` (+ içeri bakan
  ok), `entrance barrier`, `drive`, `TOILETS AND WATER POINT`, `CAR PARK`, `REUSE SHOP`,
  `GARDEN WASTE BAYS`, `WOOD`, `RUBBLE`, `PAINT AND CHEMICALS`, `GENERAL WASTE`,
  `GLASS, CANS AND PLASTIC BANKS`, `exit barrier` ve kuzey oku `N`.

### Telif / yazım

- İngiliz İngilizcesi (`tyre`, `licence`, `metre`, `£`, `rucksack`, `modelled`);
  `accepted_variants` içinde hoşgörü olarak yalnızca `judgment` (Amerikan) kabul ediliyor.
  Görünür metinde "IELTS" yok.
- ⚠️ **Referans PDF'leri bu oturumda da açılamadı:** `Read` aracı `pdftoppm` (poppler)
  istiyor, ortamda yok; `referans/text/` klasörü hâlâ üretilmemiş. Yönerge kalıpları
  L1–L3 setlerinden devralındı ("Complete the notes below…", "Label the plan below.
  Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each answer.", "Complete the
  flow-chart below…", "Answer the questions below…"). Yeni biçim icat edilmedi;
  referanstan **tek bir cümle, soru ya da senaryo kopyalanmadı**.
- Bütün kişi/kurum/yer adları senaryolardan geliyor, hepsi uydurma.
- Atlanan/sorun: yok. **OPUS5-21'de 12 paketten 4'ü tamam;** sıradaki **L5**.

## OPUS5-21 (5. çalıştırma: L5 — güvenli sorular, 29 soru)

- Tarih: 2026-08-04
- Depo kontrolü: `content/listening/tests/` altında **`L1/` … `L4/`** vardı,
  `content/listening/practice/` hâlâ boştu → çalıştırma listesindeki ilk üretilmemiş paket
  **L5** idi, o yapıldı. Ön koşul sağlandı: `L5-S1` … `L5-S4` senaryoları yerinde.
- 11–15 ve 21–26 aralıkları **boş bırakıldı** (FABLE5-43'ün işi); `tools/dogrula.py`
  "L5 29/40 EKSIK eksik=[11–15, 21–26]" diyor, beklenen durum budur.

### Seçilen tipler ve dosyalar

| Soru | Bölüm | Tip | Dosya | Kelime sınırı |
|---|---|---|---|---|
| 1–10 | S1 | `form_completion` | `content/listening/tests/L5/form-completion.json` | TWO WORDS |
| 16–20 | S2 | `plan_map_diagram_labelling` (**harf seçme A–H**) | `…/plan-map-diagram-labelling.json` | — (harf) |
| 27–30 | S3 | `sentence_completion` | `…/sentence-completion.json` | TWO WORDS |
| 31–35 | S4 | `table_completion` | `…/table-completion.json` | TWO WORDS |
| 36–40 | S4 | `summary_completion` | `…/summary-completion.json` | **ONE WORD** |

L4'ün bıraktığı iki uyarının **ikisi de** karşılandı:

- **Etiketleme alt tipi:** L1 harf, L2 kelime, L3 harf, L4 kelime, **L5 harf seçme (A–H)** —
  dönüşüm sürüyor. ⚠️ **L6 kelime yazma** olsun.
- **4. bölümde `table_completion`:** L4, "L5–L6'dan en az birinde 4. bölümde tablo
  denensin" demişti; 31–35 tablo olarak yazıldı. Tablonun satırları dersin ilk beş
  paragrafından (boyut sınıfları → kaynak → nehirler → miktar → varış yerleri) geliyor,
  yani tablo tek bir paragrafa sıkışmıyor.
- **1–10 için tip:** L5-S1 telefonla **rezervasyon**, promptun kuralı gereği `form`.
  Beş testin dağılımı artık **form / tablo / form / not / form**.
- **31–40 bölünmesi:** L1 = not + kısa cevap, L2 = akış şeması + not, L3 = özet + kısa
  cevap, L4 = kısa cevap + akış şeması, **L5 = tablo (31–35) + özet (36–40)**.
  ⚠️ **L6:** beş testin beşi de 5+5 böldü; prompt 31–36 + 37–40 bölünmesini de öneriyor,
  **L6'da 6+4 denensin** ve `short_answer` yeniden kullanılsın.
- **Kelime sınırı çeşitliliği:** özetin beş cevabı da tek kelime/sayı seçilerek
  `ONE WORD AND/OR A NUMBER` üçüncü kez kullanıldı (L3'te 1., L4'te 4. bölümdeydi).

### Kullanılan `answer_point_id` değerleri

| Set | Kimlikler |
|---|---|
| `L5-form-completion` | `L5-S1-01`, `L5-S1-03`, `L5-S1-04`, `L5-S1-07`, `L5-S1-09`, `L5-S1-12`, `L5-S1-15`, `L5-S1-18`, `L5-S1-22`, `L5-S1-25` |
| `L5-plan-map-diagram-labelling` | `L5-S2-10`, `L5-S2-11`, `L5-S2-13`, `L5-S2-15`, `L5-S2-17` |
| `L5-sentence-completion` | `L5-S3-16`, `L5-S3-22`, `L5-S3-24`, `L5-S3-30` |
| `L5-table-completion` | `L5-S4-01`, `L5-S4-04`, `L5-S4-07`, `L5-S4-08`, `L5-S4-11` |
| `L5-summary-completion` | `L5-S4-13`, `L5-S4-18`, `L5-S4-19`, `L5-S4-23`, `L5-S4-28` |

- **Senaryo dosyalarına hiç dokunulmadı** — 29 sorunun 29'u da senaryolarda hazır olan
  bilgi noktalarına oturdu, yeni `answer_point` eklemek gerekmedi (L4'te bir tane
  gerekmişti).
- Çeldiricili bilgi noktasından çıkan sorular (cevap her zaman **düzeltilmiş** değer):
  1 (22 → 29 Ağustos), 2 (9.45 → 9.15), 4 (14 → 14A), 6 (38 → 42 km), 9 (istasyon
  otoparkı → Waterside Depot), 27 (10 → 20 kişi), 29 (seminer odası → çalışma kabinleri),
  31 (2 mm → 5 mm), 32 (onda bir → beşte bir), 34 (8 → 11 milyon ton). Toplam **10 soru**,
  L4'le aynı oran.
- Bilinçli kullanılmayan çeldiriciler: `L5-S1-11` (saat başı → bisiklet/gün başı) —
  ücret zaten 5. soruda soruldu, ikinci kez ücrete girilmedi; `L5-S2-02` (broşürdeki
  11.00 → 10.30), `L5-S2-04` (15 → 18 £), `L5-S2-19` (afişteki 20 → 15 dk),
  `L5-S2-24` (yalnız Cumartesi → iki gün) — dördü de 2. bölümün 11–15 aralığına, yani
  `FABLE5-43`'ün çoktan seçmeli alanına bırakıldı; `L5-S3-04` (100 → 120),
  `L5-S3-18` (12 → 5), `L5-S3-21` (2.000 → 2.500 kelime), `L5-S3-23` (15 → 10+5 dk) —
  3. bölümde bana yalnızca dört soru düşüyor, gerisi 21–26 aralığında `FABLE5-43`'ün;
  `L5-S4-17` (üçte bir → onda bir ağ gözü) — 37. soru aynı paragraftan zaten çıkıyor,
  paragraf başına bir cevap kuralı gereği ikincisi alınmadı; `L5-S4-30` (6. hafta →
  7. hafta) — ödev paragrafı (12) soru dışı kaldı.

### Doğrulama

- Üç geçici betik yazıldı (`tools/_l5q_plan.py` çizim + üretim, `tools/_l5q_ascii.py`
  ASCII izdüşüm, `tools/_l5q_kontrol.py` denetleyici); üçü de **diskten okuyarak** sınadı
  ve iş bitince silindi. (Adları `_l5q_` ile başlıyor: `tools/_l5_kontrol.py` ve
  `tools/_l5_uret.py` OPUS5-20'den kalma, onlara dokunulmadı.)
- Denetlenenler: her `evidence`in senaryo repliğinde **birebir** ve **tek** geçmesi,
  `turn_index`in bilgi noktasıyla uyuşması, set içi artan sıra, aynı bilgi noktasının iki
  kez kullanılmaması, **`accepted_variants` dahil** kelime sınırı (harf içeren jeton =
  kelime, salt sayı jetonu ayrı sayıldı), açıklamaların gerçek Türkçe karakter içermesi,
  `answer`ın `accepted_variants` içinde olması, `stem_block`/`table` boşluk numaralarının
  item numaralarıyla birebir aynı olması ve her `prompt`un gövdede birebir bulunması,
  soru numaralarının planla birebir aynı olması (29 soru; boş: 11–15, 21–26), 6+ kelimelik
  soru kökü parçalarının senaryodan **birebir kopya olmaması** ve görünür metinde "IELTS"
  taraması. **Sonuç: 0 hata**, tek uyarı aşağıdaki 2 numaralı bilinçli sapmanın uyarısı.
- İlk turda **1 gerçek hata** çıktı ve düzeltildi: özetin gövdesinde 36, 38 ve 39
  numaralı boşluklardan sonra fazladan boşluk vardı (`(39) ........ , which`), bu yüzden
  39. sorunun `prompt`u gövdede birebir bulunamıyordu; noktalama gövdede düzeltildi.
  Kelime sınırı, sıra ve kanıt denetimlerinde ilk turda hata çıkmadı.
- Denetleyicinin ilk sürümü 2. ve 4. bölümde de "iki cevap arasında en az bir replik"
  kuralını arıyordu ve yanlış alarm veriyordu; kural L1–L4'teki uygulamaya göre
  düzeltildi (tek kişilik anlatımda replik = paragraf, paragraf başına bir cevap).
- SVG yine **geometrik olarak** sınandı (depoda SVG → PNG çevirici hâlâ yok): izinli öge
  listesi (`svg rect circle line polygon text` — dışında öge yok), tek renk `#000`,
  `fill="none"`, sabit `width`/`height` yok, bütün koordinatlar `viewBox` içinde, tek
  satır string, A–H harflerinin sekizi de tam bir kez var. **Kutu-kutu ve yazı-yazı
  çakışma taraması: 0 çakışma** (63 öge).
- ASCII izdüşüm **gözle** okundu: kuzey yukarıda, nehir en üstte, nehir kıyısı yolu
  sahnenin arkasından geçiyor; ana kapı altta ortada (ok içeri bakıyor), kapının hemen
  solunda BOX OFFICE, sağında 16 (F), onun sağında LOST PROPERTY; tam karşıda kuzey uçta
  17 (C); sağ tarafta danışma ile sahne arasında 18 (H), onun kuzeyinde FOOD STALLS,
  onun doğusunda toilets ve water point; sol tarafta WORKSHOP TENT, onun kuzeyinde
  19 (B); kapının dışında giriş yolunun solunda 20 (E), sağında çeldirici A; çayırın
  ortasında çeldirici D, güneybatı köşesinde çeldirici G. Tarifle birebir uyuyor.
- Ardından `python tools/dogrula.py`: **şema hatası 0**, görünür metinde IELTS 0,
  yasak kaynak 0, L5 29/40.

### Bilinçli sapmalar

1. **"İki cevap aynı replikte olmasın" kuralı 1. ve 3. bölümde tam uygulandı.**
   1. bölümde cevaplar 6, 8, 11, 15, 20, 26, 30, 32, 36, 44 numaralı repliklerde — en dar
   aralık iki replik; 3. bölümde 24, 30, 34, 40. 2. ve 4. bölüm **tek kişilik anlatım**
   olduğu için "replik" = paragraf; 4. bölümde 10 cevap **10 ayrı paragrafa** (1–9 ve 11)
   dağıldı. L1–L4'teki uygulamanın aynısı.
2. **2. bölümde 19 ve 20 numaralı sorular aynı paragraftan (6. replik) çıkıyor —
   L1–L5'te bunun ilk örneği.** Sebep yapısal: L5-S2'de sahayı tarif eden yalnızca
   **dört** paragraf var (3–6), beş soru gerekiyor. İki cevabın arasında üç cümle var
   (atölye çadırı → **aile alanı** → nehir kıyısı yolu → **bisiklet park yeri**), yani
   adayın nefes payı iki repliklik diyalog aralığından dar değil. Alternatif — park-and-
   ride paragrafını (7) haritaya katmak — saha planına ait olmadığı için elendi.
3. **4. bölümün 0, 10 ve 12. paragrafları soru dışı bırakıldı.** Giriş paragrafı (0)
   yalnızca dersin planını veriyor; 10. paragrafın (dört müdahale) içeriği özetin
   **verilen** metninde bağlam olarak duruyor, boşluk 11. paragrafa konuldu; 12. paragraf
   ödev duyurusu.
4. **Özette ONE WORD sınırı 38. sorunun kabulünü daraltıyor:** seste "nineteen fifties"
   deniyor ama iki kelime olduğu için `accepted_variants` yalnızca `1950s` / `1950's`.
   Rakamlı yazım bu sınırın standart karşılığı olduğu için sapma bilinçli.
5. **Cevap türü dağılımı:** 1. bölüm **4 kelime / 6 sayı-kod** (Ferrandez, farm café,
   water bottle, Waterside Depot ↔ 29, 9.15, 14A, 35, 42, GW941) — rezervasyon formunun
   doğası gereği sayılar başta toplanıyor; 2. bölümün beşi de harf; 3. bölümde 3 kelime +
   1 sayı; 4. bölümde 7 kelime + 3 sayı.
6. **16–20 zincirli değil:** 16 (bilet gişesinin karşısı) ve 20 (kapının solu) etiketli
   sabitlere, 18 (yemek tezgâhlarının hemen güneyi) ve 19 (atölye çadırının kuzeyi)
   kendi bağımsız çıpalarına dayanıyor; 17 kapıdan bakınca tam karşıda. Aday 16'yı
   bilmeden de 18'i çözebiliyor.

### Plan çizimi (2. bölüm) — harf seçme alt tipi

- `viewBox="0 0 620 720"`, sabit `width`/`height` yok, yalnızca `rect`/`circle`/`line`/
  `polygon`/`text`, hep `#000` çizgi, dolgu yok, tek satır string, 63 öge.
- `"kind": "plan"` — çayır üzerindeki festival sahası: çit dört çizgiyle, kapı boşluğu
  alt çizgideki kesikle, nehir ve nehir kıyısı yolu paralel çizgi çiftleriyle gösterildi.
- Seçenekler **daire içinde harf** (`A`…`H`), `options` dolu, `word_limit` `null` —
  harf seçme alt tipi. Beş cevap: 16=F, 17=C, 18=H, 19=B, 20=E; üç çeldirici harf
  (A kapının dışında sağda, D çayırın ortasında, G güneybatı köşede) hiçbir sorunun
  cevabı değil.
- **Sabit referanslar (etiketi verilmiş):** `MAIN GATE` (+ içeri bakan ok), `BRIDGE ROAD`,
  `BOX OFFICE`, `LOST PROPERTY`, `WORKSHOP TENT`, `FOOD STALLS`, `toilets`,
  `water point`, `riverside path`, `RIVER`, `hedge` ve kuzey oku `N`.

### Telif / yazım

- İngiliz İngilizcesi (`kilometres`, `£`, `marquee`, `standardising`, `metres`);
  `accepted_variants` içinde hoşgörü olarak `standardizing` (Amerikan) ve `farm cafe`
  (aksansız) kabul ediliyor. Görünür metinde "IELTS" yok.
- ⚠️ **Referans PDF'leri bu oturumda da açılamadı:** `Read` aracı `pdftoppm` (poppler)
  istiyor, ortamda yok; `referans/text/` klasörü hâlâ üretilmemiş. Yönerge kalıpları
  L1–L4 setlerinden devralındı ("Complete the form below…", "Label the plan below. Write
  the correct letter, A–H, next to Questions 16–20.", "Complete the sentences below…",
  "Complete the table below…", "Complete the summary below…"). Yeni biçim icat edilmedi;
  referanstan **tek bir cümle, soru ya da senaryo kopyalanmadı**.
- Bütün kişi/kurum/yer adları senaryolardan geliyor, hepsi uydurma.
- Atlanan/sorun: yok. **OPUS5-21'de 12 paketten 5'i tamam;** sıradaki **L6**.

---

## OPUS5-21 (6. çalıştırma: L6 — güvenli sorular, 29 soru)

- Tarih: 2026-08-04
- Depo kontrolü: `content/listening/tests/` altında **`L1/` … `L5/`** vardı,
  `content/listening/practice/` hâlâ boştu → çalıştırma listesindeki ilk üretilmemiş paket
  **L6** idi, o yapıldı. Ön koşul sağlandı: `L6-S1` … `L6-S4` senaryoları yerinde.
- Bununla **altı tam testin tamamlama/etiketleme yarısı bitti** (6 × 29 = 174 soru).
- 11–15 ve 21–26 aralıkları **boş bırakıldı** (FABLE5-43'ün işi); `tools/dogrula.py`
  "L6 29/40 EKSIK eksik=[11–15, 21–26]" diyor, beklenen durum budur.

### Seçilen tipler ve dosyalar

| Soru | Bölüm | Tip | Dosya | Kelime sınırı |
|---|---|---|---|---|
| 1–10 | S1 | `form_completion` | `content/listening/tests/L6/form-completion.json` | TWO WORDS |
| 16–20 | S2 | `plan_map_diagram_labelling` (**kelime yazma**) | `…/plan-map-diagram-labelling.json` | TWO WORDS |
| 27–30 | S3 | `sentence_completion` | `…/sentence-completion.json` | TWO WORDS |
| 31–36 | S4 | `note_completion` | `…/note-completion.json` | **THREE WORDS** |
| 37–40 | S4 | `summary_completion` | `…/summary-completion.json` | **ONE WORD** |

L5'in bıraktığı iki uyarı:

- **Etiketleme alt tipi:** L5 "L6 kelime yazma olsun" demişti, öyle yapıldı. Altı testin
  dizisi: L1 harf, L2 kelime, L3 harf, L4 kelime, L5 harf, **L6 kelime** — dönüşüm tamam,
  üç harf seçme + üç kelime yazma.
- **31–40 bölünmesi:** L5 "6+4 denensin **ve `short_answer` yeniden kullanılsın**"
  demişti. **6+4 uygulandı** (31–36 not + 37–40 özet) ama `short_answer` bilinçli olarak
  alınmadı; gerekçe aşağıda "Bilinçli sapmalar" 1. maddede.
- **1–10 için tip:** L6-S1 telefonla **yurt başvurusu** (kayıt), promptun kuralı gereği
  `form`. Altı testin dağılımı: **form / tablo / form / not / form / form**.
- **Kelime sınırı çeşitliliği:** tek testte üç ayrı sınır kullanıldı — 4. bölümün notunda
  `THREE WORDS` (L1–L5'te 4. bölümde hiç kullanılmamıştı; "two to one", "nine in ten",
  "next pay rise" cevapları için gerekiyordu), özette `ONE WORD`, gerisinde `TWO WORDS`.

### Kullanılan `answer_point_id` değerleri

| Set | Kimlikler |
|---|---|
| `L6-form-completion` | `L6-S1-01`, `L6-S1-02`, `L6-S1-05`, `L6-S1-06`, `L6-S1-09`, `L6-S1-12`, `L6-S1-14`, `L6-S1-17`, `L6-S1-22`, `L6-S1-31` |
| `L6-plan-map-diagram-labelling` | `L6-S2-12`, `L6-S2-16`, `L6-S2-19`, `L6-S2-21`, `L6-S2-23` |
| `L6-sentence-completion` | `L6-S3-22`, `L6-S3-26`, `L6-S3-29`, `L6-S3-32` |
| `L6-note-completion` | `L6-S4-01`, `L6-S4-05`, `L6-S4-08`, `L6-S4-10`, `L6-S4-14`, `L6-S4-16` |
| `L6-summary-completion` | `L6-S4-21`, `L6-S4-24`, `L6-S4-29`, `L6-S4-33` |

- **Senaryo dosyalarına hiç dokunulmadı** — 29 sorunun 29'u da senaryolarda hazır olan
  bilgi noktalarına oturdu, yeni `answer_point` eklemek gerekmedi (L5'te de öyleydi).
- Çeldiricili bilgi noktasından çıkan sorular (cevap her zaman **düzeltilmiş** değer):
  4 (arkadaşın önerdiği Thornbury → çatısı yenilendiği için kapalı), 6 (132 → 145 £),
  8 (23 → 30 Haziran), 9 (ana resepsiyon → kapıcılık odası), 17 (girişin yanı → sol
  koridorun ucu), 20 (arkadaki yükleme avlusu → kapının dışı), 27 (86 sonuç → 30 çalışma),
  32 (üçe bir → ikiye bir), 34 ("kimse çıkmadı" → onda dokuz), 37 (15 → 5 puan).
  Toplam **10 soru**, L4–L5'le aynı oran.
- Bilinçli kullanılmayan çeldiriciler: `L6-S1-03` (dört yıllık → üç yıllık program) —
  bölüm adı 2. soruda zaten soruldu, süre formda verilmiş bilgi olarak duruyor;
  `L6-S1-13` (40 → 38 hafta) ve `L6-S1-20` (12 → 14 Eylül) — form on soruyu doldurduğu
  için sözleşme süresi gövdeye verilmiş bilgi, taşınma günü ise dışarıda kaldı;
  `L6-S1-28` (Çarşamba → Perşembe temizlik) — 1. bölümde iki tarih/gün cevabı yığılmasın
  diye alınmadı; `L6-S2-03` (9.00 → 8.30), `L6-S2-05` (Perşembe → Çarşamba),
  `L6-S2-07` (19 → 32 tezgâh), `L6-S2-24` (11.00 → 12.30), `L6-S2-28` (12 → 18 numaralı
  otobüs), `L6-S2-29` (2 → 3 saat), `L6-S2-30` (5 £ → ücretsiz), `L6-S2-34` (15 → 18 £) —
  hepsi 2. bölümün 11–15 aralığına, yani `FABLE5-43`'ün çoktan seçmeli alanına bırakıldı;
  `L6-S3-01` (3.000 → 2.500 kelime), `L6-S3-10` (5 → 2 veri tabanı), `L6-S3-16`
  (20 → 10 yıl), `L6-S3-19` (tam metin süzgeci), `L6-S3-31` (Room B → 2. kattaki eğitim
  odası), `L6-S3-35` (Cuma → Perşembe) — 3. bölümde bana yalnızca dört soru düşüyor,
  gerisi 21–26 aralığında `FABLE5-43`'ün; `L6-S4-23` (iki hafta → iki gün önce
  hatırlatma) — 37. soru aynı paragraftan çıkıyor, paragraf başına bir cevap kuralı gereği
  ikincisi alınmadı; `L6-S4-31` (60 öğrencilik laboratuvar → on binlerce kişilik alan
  denemesi) ve `L6-S4-35`/`L6-S4-36` (8. hafta → 9. hafta, 3. bölüm → 4. bölüm) —
  özet 10. replikte bittiği için 11. paragraf (duyurular) soru dışı kaldı.

### Doğrulama

- Üretim ve denetim tek geçici betikte toplandı (`tools/_l6_sorular.py`); dosyaları
  yazdıktan sonra **diskten geri okuyup** sınıyor, depoda duruyor (L5'in `_l5q_*`
  betikleri silinmişti; bu betik yeniden üretilebilirlik için bırakıldı, `tools/_l6_uret.py`
  OPUS5-20'den kalma, ona dokunulmadı).
- Denetlenenler: her `evidence`in senaryo repliğinde **birebir** geçmesi, `turn_index`in
  bilgi noktasıyla uyuşması, set içi sıranın geri gitmemesi, **`accepted_variants` dahil**
  kelime sınırı (harf içeren jeton = kelime), `prompt`un `stem_block` içinde birebir
  bulunması, her soru numarası için gövdede boşluk olması, 29 numaranın planla birebir
  aynı dizide olması, açıklamaların dolu olması, "IELTS" taraması.
- Plan SVG'si ayrıca ölçüldü: yalnızca `rect`/`line`/`circle`/`polygon`/`text` (60 öge),
  tek renk `#000`, `fill="none"`, sabit `width`/`height` yok, bütün koordinatlar
  `viewBox="0 0 620 740"` içinde, tek satır string, **kutu-kutu ve yazı-yazı çakışması 0**.
- ASCII izdüşüm **gözle** okundu: kuzey yukarıda, ana giriş güneyde (Peveril Street),
  girişin solunda DANIŞMA MASASI, sağında 16; batı duvarında uzun tezgâh (güneyde EKMEK VE
  PASTA, kuzeyde PEYNİR), sol koridorun en ucunda 17; ortada iki SEBZE SIRASI, doğuda BAL
  VE REÇEL ile yan kapı; kuzey uçta saatin altında 18, hemen güneyinde OTURMA ALANI;
  kuzeydoğu köşede 19, ondan geçilen ek odada tuvaletler; kapının dışında 20, salonun
  arkasında YÜKLEME AVLUSU. Tarifle birebir uyuyor.
- Ardından `python tools/dogrula.py`: **şema hatası 0**, görünür metinde IELTS 0,
  yasak kaynak 0, L6 29/40.

### Bilinçli sapmalar

1. **L5'in `short_answer` önerisi uygulanmadı, yerine `summary_completion` seçildi.**
   L5'in asıl istediği 5+5 dışına çıkmaktı; **6+4 uygulandı**. `short_answer` alınsaydı
   31–36 not + 37–40 kısa cevap çıkacaktı ki bu **L1'in bölünmesinin birebir aynısı**
   olurdu. Altı testin 4. bölüm eşleşmeleri şimdi altısı da farklı: L1 not+kısa,
   L2 akış+not, L3 özet+kısa, L4 kısa+akış, L5 tablo+özet, **L6 not+özet**. Tip başına
   düşen kullanım da dengelendi (not 3, kısa cevap 3, özet 3, akış 2, tablo 1) ve
   `short_answer` zaten 11. alıştırma paketinde 15 soruyla ayrıca üretilecek.
2. **"İki cevap aynı replikte olmasın" kuralı 1. ve 3. bölümde tam uygulandı.**
   1. bölümde cevaplar 5, 7, 13, 16, 20, 24, 28, 32, 40, 52 numaralı repliklerde — en dar
   aralık iki replik; 3. bölümde 27, 31, 35, 39. 2. ve 4. bölüm **tek kişilik anlatım**
   olduğu için "replik" = paragraf; 4. bölümde 10 cevap **10 ayrı paragrafa** (0–5 ve
   7–10) dağıldı. L1–L5'teki uygulamanın aynısı.
3. **2. bölümde 19 ve 20 aynı paragraftan (8. replik) çıkıyor — L5'ten sonra ikinci kez.**
   Sebep yine yapısal: L6-S2'de salonu tarif eden yalnızca **beş** paragraf var (4–8) ve
   4. paragrafta soru yapılabilecek tek yer (danışma masası) sabit referans olarak
   planda verilmek zorundaydı. İki cevabın arasında tam bir cümle var (dolum dükkânı →
   **tuvaletler** → bisiklet park yeri), yani nefes payı iki repliklik diyalog aralığından
   dar değil.
4. **4. bölümün 6. ve 9. paragrafları soru dışı bırakıldı.** 6. paragraftaki reçel
   deneyinin bütün sayıları ("onda altısı", "otuzda bir") üç kelimeyi aşıyor, tek
   kelimelik/üç kelimelik bir boşluğa oturmuyor; 9. paragrafın içeriği (varsayılanı kim
   seçiyor) özetin **verilen** metninde bağlam olarak duruyor, boşluk aynı paragrafın
   sonuna (kişinin kendi hedefleri) konuldu.
5. **Notta `THREE WORDS` sınırı bilinçli:** 32 ("two to one") ve 34 ("nine in ten") seste
   böyle geçiyor; eş anlamlı kısaltma yazmak 1. altın kuralı çiğneyeceği için sınır
   genişletildi. `accepted_variants` rakamlı yazımları da kabul ediyor (`2:1`, `9 in 10`).
6. **Cevap türü dağılımı:** 1. bölüm 6 kelime / 4 sayı-kod (Brathwaite, Environmental
   Engineering, re-roofed, en-suite, one box, porter's lodge ↔ 22 Hartlow Road, 145,
   30 June, HR 942); 2. bölümün beşi de iki kelimelik ad; 3. bölümde 3 kelime + 1 sayı;
   4. bölümde 7 kelime + 3 sayı. Hiçbir bölümde arka arkaya iki aynı türden cevap yok.
7. **16–20 zincirli değil:** 16 etiketli danışma masasına, 17 sol koridora ve tarif edilen
   köşeye, 18 saate, 19 etiketli oturma alanına, 20 bahçe kapısına dayanıyor. Aday 16'yı
   bilmeden de 19'u çözebiliyor.

### Plan çizimi (2. bölüm) — kelime yazma alt tipi

- `viewBox="0 0 620 740"`, sabit `width`/`height` yok, yalnızca `rect`/`line`/`circle`/
  `polygon`/`text`, hep `#000` çizgi, dolgu yok, tek satır string, 60 öge.
- `"kind": "plan"` — Peveril Street'teki kapalı hal: duvarlar çizgilerle, ana giriş güney
  duvarındaki boşlukla, yan kapı ve tuvalet kapısı doğu duvarındaki iki boşlukla, giriş
  yolu bahçe kapısından caddeye inen iki paralel çizgiyle gösterildi.
- Boşluklar **numaralı kutu** (16–20), `options` `null`, `word_limit` `TWO WORDS` —
  kelime yazma alt tipi. Cevaplar: 16 flower stall, 17 fish counter,
  18 demonstration kitchen, 19 refill shop, 20 cycle racks.
- **Sabit referanslar (etiketi verilmiş):** `MAIN ENTRANCE` (+ içeri bakan ok),
  `INFORMATION DESK`, `BREAD & CAKE STALL`, `CHEESE COUNTER`, `VEGETABLE STALLS` (iki
  sıra), `HONEY & PRESERVES`, `SEATING AREA (24 chairs)`, `clock`, `toilets`, `side door`,
  `GATE`, `LOADING YARD`, `PEVERIL STREET` ve kuzey oku `N`.

### Telif / yazım

- İngiliz İngilizcesi (`£`, `en-suite`, `porter's lodge`, `behavioural`, `neighbours`);
  `accepted_variants` içinde hoşgörü olarak `ensuite`/`en suite`, `reroofed`, `2:1`,
  `9 in 10` kabul ediliyor. Görünür metinde "IELTS" yok.
- ⚠️ **Referans PDF'leri bu oturumda da açılamadı:** `referans/` altında yalnızca `.pdf`
  var, `referans/text/` hâlâ üretilmemiş ve `Read` aracı PDF için `pdftoppm` (poppler)
  istiyor, ortamda yok. Yönerge kalıpları L1–L5 setlerinden devralındı ("Complete the form
  below…", "Label the plan below. Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each
  answer.", "Complete the sentences below…", "Complete the notes below…", "Complete the
  summary below…"). Yeni biçim icat edilmedi; referanstan **tek bir cümle, soru ya da
  senaryo kopyalanmadı**.
- Bütün kişi/kurum/yer adları senaryolardan geliyor, hepsi uydurma; 4. bölümdeki deneyler
  gerçek kişi/kurum adı verilmeden tarif edildi.
- Atlanan/sorun: yok. **OPUS5-21'de 12 paketten 6'sı tamam;** tam testler bitti, sıradaki
  paket **7 — alıştırma: form / not tamamlama (15 soru)**, dosyası
  `content/listening/practice/note-completion.json`.

## OPUS5-21 (7. çalıştırma: alıştırma — form / not tamamlama, 15 soru)

- Tarih: 2026-08-04
- Depo kontrolü: `content/listening/tests/` altında **`L1/` … `L6/`** tamamdı (6 × 29 = 174),
  `content/listening/practice/` **boştu** → çalıştırma listesindeki ilk üretilmemiş paket
  **7 — alıştırma: form / not tamamlama** idi, o yapıldı. 24 senaryonun hepsi yerinde.
- Çıktı: `content/listening/practice/note-completion.json` — **15 soru, 4 küme**,
  `test_id: null`, `practice: true`, numaralar 1'den 15'e.
- Senaryo dosyalarına **dokunulmadı**; 15 sorunun 15'i de hazır bilgi noktalarına oturdu.

### Kümeler, senaryolar ve seçilen tipler

| Küme | Senaryo | Tip | Sorular | Kelime sınırı | Konu |
|---|---|---|---|---|---|
| `P-FN-01` | `L1-S1` | `form_completion` | 1–4 | TWO WORDS | yaz kampına telefonla kayıt |
| `P-FN-02` | `L5-S1` | `note_completion` | 5–8 | TWO WORDS | rehberli bisiklet turu rezervasyonu |
| `P-FN-03` | `L2-S4` | `note_completion` | 9–12 | TWO WORDS | pompa öncesi su taşıma/depolama dersi |
| `P-FN-04` | `L6-S4` | `note_completion` | 13–15 | TWO WORDS | davranışsal ekonomi dersi |

- Kümeler **4 + 4 + 4 + 3**, yani hepsi promptun istediği 3–5 aralığında ve hiçbir
  senaryodan 4'ten fazla soru çıkmadı.
- Denge bilinçli: iki **1. bölüm** (karşılıklı konuşma → biri form, biri not) + iki
  **4. bölüm** (tek kişilik ders → not). Dört ayrı testten (L1, L2, L5, L6) alındı ki
  aynı testi baştan sona çalışan aday alıştırmada da aynı sesi dinlemesin.
- **Gövdelerde tam test cevabı sızdırılmadı:** `stem_block` içindeki verilmiş bilgiler
  (ör. "the July fortnight", "helmets are handed out") kasten tam testte soru olmayan
  ayrıntılardan seçildi.

### Kullanılan `answer_point_id` değerleri

| Küme | Kimlikler |
|---|---|
| `P-FN-01` (L1-S1) | `L1-S1-02`, `L1-S1-07`, `L1-S1-19`, `L1-S1-22` |
| `P-FN-02` (L5-S1) | `L5-S1-10`, `L5-S1-19`, `L5-S1-24`, `L5-S1-26` |
| `P-FN-03` (L2-S4) | `L2-S4-07`, `L2-S4-08`, `L2-S4-19`, `L2-S4-22` |
| `P-FN-04` (L6-S4) | `L6-S4-07`, `L6-S4-17`, `L6-S4-23` |

Hiçbiri tam testlerde kullanılmadı — 174 sorunun `answer_point_id` listesi betikle
çıkarılıp kesişim **boş** olduğu doğrulandı ("Tam testteki soruyla aynı bilgi noktasını
kullanma" kuralı).

Cevaplar: 1 `11` · 2 `3.30` · 3 `mobile phones` · 4 `5 July` · 5 `12` ·
6 `waterproof jacket` · 7 `72 hours` · 8 `high wind` · 9 `3,000` · 10 `labour` ·
11 `five storeys` · 12 `time` · 13 `framing` · 14 `11` · 15 `two days`.

Çeldiricili bilgi noktasından çıkan sorular (cevap her zaman **düzeltilmiş** değer):
1 (10 → 11 yaş), 8 (yağmur → şiddetli rüzgâr), 9 (5.000 → 3.000 yıl),
15 (iki hafta → iki gün). Toplam **4 soru**, 15'te dörtte birden fazla.

### Doğrulama

- Denetim betiği depoda: `tools/_p07_kontrol.py`. Dosyayı **diskten geri okuyup** sınıyor.
- Denetlenenler: zarf alanları (`practice`, `test_id`, `question_type`), küme boyu 3–5,
  senaryo başına en fazla 4 soru, her `answer_point_id`nin senaryoda **var olması** ve
  tam testlerde **kullanılmamış** olması, `turn_index`in bilgi noktasıyla birebir uyuşması,
  küme içi sıranın geri gitmemesi, nefes payı, her `evidence`in ilgili replikte **birebir**
  geçmesi, **`accepted_variants` dahil** kelime sınırı (harf içeren jeton = kelime),
  `prompt`un `stem_block` içinde bulunması, her numara için gövdede boşluk olması,
  numaraların 1–15 dizisi olması, açıklamaların Türkçe ve dolu olması, "IELTS" taraması.
  **Hata 0.**
- Betiğin bıraktığı iki uyarı **elle incelendi ve kabul edildi** (ikisi de altın kural 6'nın
  "sayı/tarih rakamla da yazılabilir" maddesi): soru 2 seste "half past three" olarak
  geçiyor, cevap `3.30`; soru 4 seste "the fifth of July", cevap `5 July`. İkisinin de
  `accepted_variants` listesi yazılı biçimleri kapsıyor (`3:30`, `3.30 pm`, `15.30`;
  `5th July`, `July 5`, `July 5th`).
- Ardından `python tools/dogrula.py`: **şema hatası 0**, görünür metinde IELTS 0,
  yasak kaynak 0, `listening/practice` sayacı **15**.

### Bilinçli sapmalar

1. **Dört kümenin dördünde de `TWO WORDS AND/OR A NUMBER` sınırı var.** Tam testlerde
   sınır çeşitlendirilmişti; burada `ONE WORD` bilinçli olarak kullanılmadı, çünkü
   seçilen bilgi noktalarının yarısı iki kelimelik ("mobile phones", "waterproof jacket",
   "five storeys", "two days") ve eş anlamlı kısaltma yazmak 1. altın kuralı çiğnerdi.
   Yüzdelik ve tarih sorularında boşluk **birimin dışına** alındı (`(14) ........ per cent`,
   `about (9) ........ years`) — böylece cevap tek jeton kaldı, sınır zorlanmadı.
2. **Nefes payı kuralı bölüm tipine göre uygulandı.** Karşılıklı konuşmalarda
   (`L1-S1`: 7, 16, 36, 42 · `L5-S1`: 20, 32, 42, 46) iki cevap arasında en az iki replik
   var. Tek kişilik derslerde "replik" = paragraf sayıldığı için ayrı paragraf yeterli
   görüldü (`L2-S4`: 3, 4, 9, 11 · `L6-S4`: 2, 5, 7) — L1–L6'nın 4. bölüm setlerinde de
   uygulama aynıydı (ör. `L6-note-completion` 0,1,2,3,4,5). Denetim betiği bu ayrımı
   senaryonun `speakers` sayısına bakarak yapıyor.
3. **Cevap türü dağılımı:** her küme içinde ardışık iki cevap farklı türden —
   sayı/saat/nesne/tarih (P-FN-01), fiyat/nesne/süre/olay (P-FN-02),
   sayı/kavram/sayı/kavram (P-FN-03), terim/sayı/süre (P-FN-04). Toplamda 7 sayı-tarih,
   8 kelime.

### Telif / yazım

- İngiliz İngilizcesi (`£`, `labour`, `storeys`, `behavioural`); `accepted_variants`
  hoşgörü olarak `labor`, `stories`, `2 days`, `high winds` biçimlerini de kabul ediyor.
  Görünür metinde "IELTS" yok, gerçek kişi/kurum adı yok — bütün adlar senaryolardan.
- ⚠️ **Referans PDF'leri bu oturumda da açılamadı:** `referans/` altında yalnızca `.pdf`
  var, `referans/text/` hâlâ üretilmemiş ve `Read` aracı PDF için poppler istiyor, ortamda
  yok. Yönerge kalıpları L1–L6 setlerinden devralındı ("Complete the form below…",
  "Complete the notes below. Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each
  answer."). Yeni biçim icat edilmedi; referanstan **tek bir cümle, soru ya da senaryo
  kopyalanmadı**.
- Atlanan/sorun: yok. **OPUS5-21'de 12 paketten 7'si tamam;** sıradaki paket
  **8 — alıştırma: tablo tamamlama (15 soru)**, dosyası
  `content/listening/practice/table-completion.json`. Sonraki oturuma not: form/not
  paketinde `L1-S1`, `L5-S1`, `L2-S4`, `L6-S4` senaryolarından dörder/üçer soru çıktı;
  tabloda **başka senaryolara** yönelmek (ör. `L3-S1`, `L4-S1`, `L6-S1`, `L1-S4`) hem
  senaryo başına 4 soru sınırını rahatlatır hem alıştırma havuzunu yayar.

## OPUS5-21 (8. çalıştırma: alıştırma — tablo tamamlama, 15 soru)

- Tarih: 2026-08-04
- Depo kontrolü: `content/listening/tests/` altında **`L1/` … `L6/`** tam (6 × 29 = 174),
  `content/listening/practice/` altında yalnızca **`note-completion.json`** vardı →
  çalıştırma listesindeki ilk üretilmemiş paket **8 — alıştırma: tablo tamamlama** idi,
  o yapıldı. 24 senaryonun hepsi yerinde, hiçbirine dokunulmadı.
- Çıktı: `content/listening/practice/table-completion.json` — **15 soru, 4 küme**,
  `test_id: null`, `practice: true`, numaralar 1'den 15'e. `stem_block` her düzeyde
  `null`, gövde `table` içinde (`headers` + `rows`).
- 15 sorunun 15'i de hazır bilgi noktalarına oturdu; senaryo dosyalarına yeni id eklenmedi.

### Kümeler, senaryolar ve seçilen tablolar

| Küme | Senaryo | Bölüm | Sorular | Tablo | Kelime sınırı |
|---|---|---|---|---|---|
| `P-TC-01` | `L6-S1` | 1 | 1–4 | teklif sonrası aşamalar (depozito / form / giriş günü / temizlik) | TWO WORDS |
| `P-TC-02` | `L4-S1` | 1 | 5–8 | kayıp eşya kaydı (yolculuk / çanta / referans / posta) | TWO WORDS |
| `P-TC-03` | `L1-S4` | 4 | 9–11 | dersin bölümleri (tarihçe / bugünkü biçimler / katılım nedenleri) | TWO WORDS |
| `P-TC-04` | `L3-S1` | 1 | 12–15 | üyelik bilgileri (ücret / indirim / oryantasyon / dolaplar) | TWO WORDS |

- Kümeler **4 + 4 + 3 + 4**, hepsi 3–5 aralığında; hiçbir senaryodan 4'ten fazla soru yok.
- **Senaryolar bilinçli olarak 7. paketten farklı seçildi:** form/not paketi `L1-S1`,
  `L5-S1`, `L2-S4`, `L6-S4` kullanmıştı; burada `L6-S1`, `L4-S1`, `L1-S4`, `L3-S1` var.
  Böylece hiçbir senaryo iki alıştırma dosyasında birden 4 soru sınırını zorlamıyor ve
  alıştırma havuzu altı testin tamamına yayılıyor.
- Üç kümesi 1. bölüm (tablo tamamlamanın en tipik yeri), biri 4. bölüm dersi.
- **Tam testteki cevaplar gövdede sızdırılmadı:** her tablonun verilmiş hücreleri, ilgili
  testin `stem_block`'u açılıp tek tek karşılaştırılarak seçildi. Örnekler: `L6-S1`
  tablosunda en-suite ve £145 (L6 tam test cevapları) hiç anılmıyor; `L4-S1` tablosunda
  çantanın rengi ("dark green", L4 cevabı) yerine içindekiler kullanıldı; `L1-S4`
  tablosunda "half a century" ve "contact" (L1 cevapları) yerine zirve on yılı ve listenin
  en altındaki madde soruldu; `L3-S1` tablosunda off-peak'in bitiş saati (L3 cevabı)
  yazılmayıp yalnızca "weekdays only" denildi.

### Kullanılan `answer_point_id` değerleri

| Küme | Kimlikler |
|---|---|
| `P-TC-01` (L6-S1) | `L6-S1-15`, `L6-S1-19`, `L6-S1-20`, `L6-S1-28` |
| `P-TC-02` (L4-S1) | `L4-S1-03`, `L4-S1-14`, `L4-S1-24`, `L4-S1-26` |
| `P-TC-03` (L1-S4) | `L1-S4-02`, `L1-S4-07`, `L1-S4-20` |
| `P-TC-04` (L3-S1) | `L3-S1-06`, `L3-S1-09`, `L3-S1-15`, `L3-S1-24` |

Hiçbiri tam testlerde **ve** 7. paketteki form/not alıştırmasında kullanılmadı; kesişim
betikle çıkarıldı ve **boş**.

Cevaplar: 1 `250` · 2 `photo identification` · 3 `14` · 4 `Thursdays` · 5 `4.20` ·
6 `wooden fob` · 7 `M2074` · 8 `12` · 9 `1940s` · 10 `vertical` · 11 `saving money` ·
12 `26` · 13 `a fifth` · 14 `Friday` · 15 `code`.

Çeldiricili bilgi noktasından çıkan sorular (cevap her zaman **düzeltilmiş** değer):
3 (12 Eylül → 14 Eylül), 4 (Çarşamba → Perşembe), 9 (1950'ler → 1940'lar),
14 (Perşembe akşamı → Cuma). Toplam **4 soru**, 15'te dörtte birden fazla.

### Doğrulama

- Denetim betiği depoda: `tools/_p08_kontrol.py` (7. paketinkinin tablo sürümü). Dosyayı
  **diskten geri okuyup** sınıyor.
- Denetlenenler: zarf alanları (`practice`, `test_id`, `question_type`, `stem_block`,
  `options`, `visual`), küme boyu 3–5, senaryo başına en fazla 4 soru, **tablo yapısı**
  (her satırın hücre sayısı = başlık sayısı), her `answer_point_id`nin senaryoda var olması
  ve **hem tam testlerde hem öteki alıştırma dosyalarında** kullanılmamış olması,
  `turn_index`in bilgi noktasıyla birebir uyuşması, küme içi sıranın geri gitmemesi, nefes
  payı, her `evidence`in ilgili replikte **birebir** geçmesi, **`accepted_variants` dahil**
  kelime sınırı, `prompt`un tablo hücrelerinde bulunması, her numara için tabloda boşluk,
  numaraların 1–15 dizisi olması, açıklamaların Türkçe ve dolu olması, "IELTS" taraması.
  **Hata 0.**
- Betiğin bıraktığı üç uyarı **elle incelendi ve kabul edildi** (üçü de altın kural 6'nın
  "sayı rakamla da yazılabilir" maddesi; ses harfi harfine söylüyor, yazım rakama
  çevriliyor): soru 1 "two hundred and fifty pounds" → `250`; soru 5 "Twenty past four" →
  `4.20`; soru 7 "M for Marchwood, then two, oh, seven, four" → `M2074` (referans bir
  replik sonra arayan tarafından "M, two oh seven four" diye tekrarlanıyor, yani iki kez
  duyuluyor). Üçünün de `accepted_variants` listesi makul yazımları kapsıyor.
- Kelime sınırını aşan üç varyant (`two hundred and fifty`, `twenty past four`,
  `a wooden fob`) betik uyarınca **silindi** — kendi koyduğumuz sınırı geçen bir cevap
  kabul listesinde duramaz.
- Ardından `python tools/dogrula.py`: **şema hatası 0**, görünür metinde IELTS 0,
  yasak kaynak 0, `listening/practice` sayacı **30** (15 + 15).

### Bilinçli sapmalar

1. **Dört kümede de `TWO WORDS AND/OR A NUMBER` sınırı var.** `ONE WORD` yine
   kullanılmadı: seçilen noktaların bir kısmı iki kelimelik ("photo identification",
   "wooden fob", "saving money", "a fifth") ve tek kelimeye indirmek eş anlamlı yazmak
   demek olurdu — 1. altın kural buna izin vermiyor. Para ve birim işaretleri boşluğun
   **dışında** bırakıldı (`£(1) ........`, `£(12) ........ a month`), böylece cevap tek
   jeton kalıyor.
2. **Nefes payı bölüm tipine göre uygulandı** (7. paketteki ölçütün aynısı): karşılıklı
   konuşmalarda iki cevap arasında en az iki replik var (`L6-S1`: 28, 34, 36, 48 ·
   `L4-S1`: 9, 23, 40, 44 · `L3-S1`: 10, 16, 24, 34), tek kişilik derste ayrı paragraf
   yeterli sayıldı (`L1-S4`: 1, 2, 7).
3. **Cevap türü dağılımı:** her küme içinde ardışık iki cevap farklı türden —
   para/nesne/tarih/gün (P-TC-01), saat/nesne/kod/para (P-TC-02),
   on yıl/terim/kavram (P-TC-03), para/kesir/gün/nesne (P-TC-04). Toplamda 7 sayı-tarih,
   8 kelime.
4. **Tabloların üçü üç sütunlu** ("Details" + "Notes"), böylece verilmiş bilgi cevabı ele
   vermeden bağlam kuruyor; not sütunları kasten çeldiriciyi **açıklamıyor**, yalnızca
   sorunun nereye oturduğunu gösteriyor.

### Telif / yazım

- İngiliz İngilizcesi (`£`, `off-peak`, `rucksack`, `noticeboards`); bütün kişi, kurum ve
  yer adları senaryolardan geliyor, hepsi uydurma. Görünür metinde "IELTS" yok.
- ⚠️ **Referans PDF'leri bu oturumda da açılamadı:** `referans/` altında yalnızca `.pdf`
  var, `referans/text/` hâlâ üretilmemiş ve `Read` aracı PDF için poppler istiyor, ortamda
  yok. Yönerge kalıbı L2/L5 tam testlerinden ve 7. paketten devralındı ("Complete the table
  below. Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each answer."). Yeni biçim icat
  edilmedi; referanstan **tek bir cümle, soru ya da senaryo kopyalanmadı**.
- Atlanan/sorun: yok. **OPUS5-21'de 12 paketten 8'i tamam;** sıradaki paket
  **9 — alıştırma: cümle tamamlama (15 soru)**, dosyası
  `content/listening/practice/sentence-completion.json`. Sonraki oturuma not: cümle
  tamamlama 3. bölümde geçiyor, alıştırmada da **3. bölüm senaryolarına** yönelmek en
  doğalı (`L1-S3` … `L6-S3`); tam testlerde her 3. bölümden yalnızca 4'er nokta
  kullanıldığı için o senaryolarda bol boş bilgi noktası var, ayrıca 7. ve 8. paketlerin
  kullandığı 1./4. bölüm senaryolarıyla hiç çakışmaz.

## OPUS5-21 (9. çalıştırma: alıştırma — cümle tamamlama, 15 soru)

- Tarih: 2026-08-04
- Depo kontrolü: `content/listening/tests/` altında **`L1/` … `L6/`** tam (6 × 29 = 174),
  `content/listening/practice/` altında **`note-completion.json`** (7. paket) ve
  **`table-completion.json`** (8. paket) vardı → çalıştırma listesindeki ilk üretilmemiş
  paket **9 — alıştırma: cümle tamamlama** idi, o yapıldı. 24 senaryonun hepsi yerinde,
  hiçbirine dokunulmadı, yeni bilgi noktası eklenmedi.
- Çıktı: `content/listening/practice/sentence-completion.json` — **15 soru, 4 küme**,
  `test_id: null`, `practice: true`, numaralar 1'den 15'e. Cümle tamamlamada gövde
  olmadığı için `stem_block` **ve** `table` her düzeyde `null`; boşluk doğrudan
  `prompt` içinde (`(n) ........`).
- 15 sorunun 15'i de hazır `answer_points` kayıtlarına oturdu.

### Kümeler, senaryolar ve seçilen bilgi noktaları

| Küme | Senaryo | Bölüm | Sorular | Konu | Kelime sınırı |
|---|---|---|---|---|---|
| `P-SC-01` | `L2-S3` | 3 | 1–4 | dere üzerindeki saha araştırması raporu | TWO WORDS |
| `P-SC-02` | `L3-S3` | 3 | 5–8 | staj sonrası teslim edilecek işler | TWO WORDS |
| `P-SC-03` | `L4-S3` | 3 | 9–12 | konferans posteri tasarımı | TWO WORDS |
| `P-SC-04` | `L5-S3` | 3 | 13–15 | anket tasarımı | TWO WORDS |

- Kümeler **4 + 4 + 4 + 3**; hiçbir senaryodan 4'ten fazla soru yok.
- **Dört kümenin dördü de 3. bölüm** senaryosundan: cümle tamamlama tam testte 27–30
  aralığında, yani 3. bölümde geçiyor; alıştırmanın da aynı ses tipinde (2–4 kişilik
  akademik tartışma) olması gerçek sınav deneyimine en yakın olanı. 8. paketin sonunda
  bırakılan not da bunu öneriyordu.
- Senaryolar 7. ve 8. paketlerle **hiç çakışmıyor** (onlar 1. ve 4. bölümleri kullandı),
  dolayısıyla senaryo başına 4 soru sınırı hiçbir yerde zorlanmadı. `L1-S3` ve `L6-S3`
  bilerek boş bırakıldı — sonraki paketlerde (kısa cevap, akış şeması) elde yedek
  3. bölüm senaryosu kalsın diye.
- Tam testler her 3. bölüm senaryosundan yalnızca 4 nokta kullandığı için havuz genişti;
  seçilen 15 noktanın hiçbiri tam testlerde ya da öteki iki alıştırma dosyasında yok
  (kesişim betikle çıkarıldı, **boş**).

### Kullanılan `answer_point_id` değerleri

| Küme | Kimlikler |
|---|---|
| `P-SC-01` (L2-S3) | `L2-S3-01`, `L2-S3-11`, `L2-S3-13`, `L2-S3-21` |
| `P-SC-02` (L3-S3) | `L3-S3-09`, `L3-S3-13`, `L3-S3-27`, `L3-S3-30` |
| `P-SC-03` (L4-S3) | `L4-S3-02`, `L4-S3-14`, `L4-S3-21`, `L4-S3-33` |
| `P-SC-04` (L5-S3) | `L5-S3-04`, `L5-S3-15`, `L5-S3-25` |

Cevaplar: 1 `five` · 2 `test kit` · 3 `allotments` · 4 `single file` · 5 `3,500` ·
6 `appendix` · 7 `module page` · 8 `department` · 9 `eight weeks` · 10 `30` ·
11 `larger` · 12 `eye height` · 13 `120` · 14 `voucher` · 15 `library system`.

Çeldiricili bilgi noktasından çıkan sorular (cevap her zaman **düzeltilmiş** değer):
1 (altı alan → beş), 2 (ölçer → kimyasal test kiti), 3 (ormandaki üst nokta →
bostanların arkası), 5 (4.000 → 3.500 kelime), 6 (ayrı teslim → ek), 7 (e-posta →
ders sayfası), 10 (24 punto → 30 punto), 11 (küçük panolar → büyük panolar),
13 (100 → 120 yanıt). Toplam **9 soru**, 15'in yarısından fazlası.

### Doğrulama

- Denetim betiği depoda: `tools/_p09_kontrol.py` (7. ve 8. paketinkinin cümle tamamlama
  sürümü). Dosyayı **diskten geri okuyup** sınıyor.
- Denetlenenler: zarf alanları (`practice`, `test_id`, `question_type`, `stem_block`,
  `table`, `options`, `visual`), küme boyu 3–5, küme başına `context_line`, senaryo
  başına en fazla 4 soru, her `answer_point_id`nin senaryoda var olması ve **hem tam
  testlerde hem öteki alıştırma dosyalarında** kullanılmamış olması, `turn_index`in
  bilgi noktasıyla birebir uyuşması, küme içi sıranın geri gitmemesi, nefes payı, her
  `evidence`in ilgili replikte **birebir** geçmesi, **`accepted_variants` dahil** kelime
  sınırı, promptta doğru numaralı boşluğun bulunması, **2. altın kural** (soru kökü
  sesteki cümlenin sadeleştirilmiş kopyası mı), numaraların 1–15 dizisi olması,
  açıklamaların Türkçe ve dolu olması, "IELTS" taraması. **Hata 0.**
- Betiğin bıraktığı iki uyarı **elle incelendi ve kabul edildi** (ikisi de altın kural
  6'nın "sayı rakamla yazılabilir" maddesi; ses sayıyı kelimeyle söylüyor):
  soru 5 "three thousand five hundred words" → `3,500`; soru 13 "a minimum of a hundred
  and twenty completed responses" → `120`.
- Kelime sınırını aşan altı varyant (`chemical test kit`, `three thousand five hundred`,
  `the module page`, `a hundred and twenty`, `one hundred and twenty`,
  `the library system`) betik uyarınca **silindi** — 8. paketteki kararın aynısı: kendi
  koyduğumuz sınırı geçen bir yazım kabul listesinde duramaz.
- Ardından `python tools/dogrula.py`: **şema hatası 0**, görünür metinde IELTS 0,
  yasak kaynak 0, `listening/practice` sayacı **45** (15 + 15 + 15).

### Bilinçli sapmalar

1. **Dört kümede de `TWO WORDS AND/OR A NUMBER` sınırı var.** `ONE WORD` yine
   kullanılmadı: seçilen noktaların yarısı iki kelimelik ("test kit", "single file",
   "module page", "eight weeks", "eye height", "library system") ve tek kelimeye indirmek
   eş anlamlı/kısaltılmış yazmak demek olurdu — 1. altın kural buna izin vermiyor.
   Birim ve ölçü sözcükleri boşluğun **dışında** bırakıldı (`(5) ........ words`,
   `(10) ........ point`), böylece cevap tek jeton kalıyor.
2. **Nefes payı 3. bölüm için sıkı uygulandı.** Hepsi karşılıklı konuşma olduğu için
   iki cevap arasında en az iki replik var; gerçek aralıklar çok daha geniş
   (`L2-S3`: 1, 19, 25, 38 · `L3-S3`: 9, 13, 27, 31 · `L4-S3`: 3, 17, 23, 38 ·
   `L5-S3`: 7, 21, 34). Tartışmalarda görüş ayrılıkları uzun sürdüğü için cevapların
   seyrek olması ayrıca gerekiyordu: aralardaki repliklerin çoğu `FABLE5-43`'ün
   eşleştirme/çoktan seçmeli sorularına ait görüş noktaları.
3. **Cevap türü dağılımı:** her küme içinde ardışık iki cevap farklı türden —
   sayı/nesne/yer/kural (P-SC-01), sayı/nesne/yer/kurum (P-SC-02),
   süre/sayı/sıfat/yer (P-SC-03), sayı/nesne/sistem (P-SC-04). Toplamda 4 sayı,
   11 kelime; hiçbir kümede iki sayı yan yana değil.
4. **Soru kökleri baştan sona yeniden ifade edildi** (2. altın kural). Örnek: ses
   "Nothing under thirty for the body" diyor, soru kökü "the tutor sets a lower limit of
   (10) ........ point"; ses "put it at eye height rather than down in a corner" diyor,
   soru kökü "should be placed at (12) ........ rather than in a corner" — boşluğa gelen
   kelime birebir, çevresi değil. Betik bu kuralı sadeleştirilmiş metin karşılaştırmasıyla
   ayrıca sınıyor.

### Telif / yazım

- İngiliz İngilizcesi (`allotments`, `metre`, `programme` bağlamı, `£`); bütün kişi,
  kurum ve yer adları senaryolardan geliyor, hepsi uydurma. Görünür metinde "IELTS" yok.
- ⚠️ **Referans PDF'leri bu oturumda da açılamadı:** `referans/` altında yalnızca `.pdf`
  var, `referans/text/` hâlâ üretilmemiş ve `Read` aracı PDF için poppler istiyor, ortamda
  yok (`ielts-listening-computer-delivered-sentence-completion-answer-key.pdf` denendi,
  aynı hata). Yönerge kalıbı L1–L6 tam testlerinin cümle tamamlama setlerinden devralındı
  ("Complete the sentences below. Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each
  answer."). Yeni biçim icat edilmedi; referanstan **tek bir cümle, soru ya da senaryo
  kopyalanmadı**.
- Atlanan/sorun: yok. **OPUS5-21'de 12 paketten 9'u tamam;** sıradaki paket
  **10 — alıştırma: akış şeması tamamlama (15 soru)**, dosyası
  `content/listening/practice/flow-chart-completion.json`. Sonraki oturuma not: akış
  şeması 4. bölümde (ders) geçiyor, yani **`L*-S4` senaryolarına** yönelmek doğal olur;
  7. paket `L2-S4` ve `L6-S4`'ten soru çıkarmıştı, 8. paket `L1-S4`'ten üç soru aldı, o
  yüzden `L3-S4`, `L4-S4`, `L5-S4` en rahat üçlü. Akış şemasında adımların **sıra**
  bildirmesi şart: gövdeyi `stem_block` içinde ok (`↓`) ile kur, `table` null kalsın.

## OPUS5-21 (11. çalıştırma: alıştırma — kısa cevap, 15 soru)

- Tarih: 2026-08-05
- Depo kontrolü: `content/listening/tests/` altında **`L1/` … `L6/`** tam (6 × 29 = 174);
  `content/listening/practice/` altında `note-completion.json` (7), `table-completion.json`
  (8), `sentence-completion.json` (9) **ve** `flow-chart-completion.json` (10) vardı.
  Çalıştırma listesindeki ilk üretilmemiş paket bu yüzden **11 — alıştırma: kısa cevap**;
  o yapıldı. 24 senaryonun hepsi yerinde, hiçbirine dokunulmadı, yeni bilgi noktası
  eklenmedi.
- ⚠️ **10. paket diskteydi ama commit edilmemişti.** `UYARILAR.txt`e göre bir önceki iş
  ("Dinleme - kolay sorular (11/12)") üç denemede sonuç vermemiş; dosya üretilmiş, ama
  `NOTLAR.md` girdisi ve commit yapılamamış. Dosya bu oturumda **yeniden üretilmedi**:
  aynı denetim betiğinden geçirildi (**hata 0**) ve bu paketle birlikte commit edildi.
  10. paketin künyesi: `practice-flow-chart-completion`, 15 soru, 4 küme —
  `P-FC-01` `L3-S4` (1–4), `P-FC-02` `L5-S4` (5–8), `P-FC-03` `L4-S4` (9–12),
  `P-FC-04` `L6-S4` (13–15).
- Çıktı: `content/listening/practice/short-answer.json` — **15 soru, 4 küme**,
  `test_id: null`, `practice: true`, numaralar 1'den 15'e. Kısa cevapta gövde olmadığı
  için `stem_block` **ve** `table` her düzeyde `null`; `prompt` doğrudan bir sorudur,
  boşluk işareti (`........`) hiçbir yerde geçmez.
- 15 sorunun 15'i de hazır `answer_points` kayıtlarına oturdu.

### Kümeler, senaryolar ve seçilen bilgi noktaları

| Küme | Senaryo | Bölüm | Sorular | Konu | Kelime sınırı |
|---|---|---|---|---|---|
| `P-SA-01` | `L1-S4` | 4 | 1–4 | şehirde gıda üretimi | THREE WORDS |
| `P-SA-02` | `L2-S4` | 4 | 5–8 | pompa öncesi su taşıma ve depolama | TWO WORDS |
| `P-SA-03` | `L4-S4` | 4 | 9–12 | gürültü kirliliği | THREE WORDS |
| `P-SA-04` | `L5-S4` | 4 | 13–15 | denizdeki plastikler | THREE WORDS |

- Kümeler **4 + 4 + 4 + 3**; hiçbir senaryodan 4'ten fazla soru yok.
- **Dört kümenin dördü de 4. bölüm** senaryosundan: promptun tip tablosunda kısa cevap
  yalnızca 4. bölüme yazılmış (tam testte 37–40 aralığı), alıştırmanın da aynı ses
  tipinde — tek kişilik akademik ders — olması gerçek sınav deneyimine en yakın olanı.
- Senaryo seçimi **yük dengesine göre** yapıldı: 10. paket `L3-S4`, `L5-S4`, `L4-S4`,
  `L6-S4`'ü kullanmıştı; `L6-S4` alıştırmalarda zaten en çok yüklenen senaryo (7. + 10.
  paket = 6 soru) olduğu için bu pakette bilerek atlandı, yerine `L1-S4` ve `L2-S4`
  alındı. Alıştırma toplamı senaryo başına şöyle dengelendi: `L1-S4` 7, `L2-S4` 8,
  `L3-S4` 4, `L4-S4` 8, `L5-S4` 7, `L6-S4` 6.
- Seçilen 15 noktanın hiçbiri tam testlerde ya da öteki dört alıştırma dosyasında yok
  (kesişim betikle çıkarıldı, **boş**). İlk taslakta `L2-S4-27` (*gravel*) ve `L2-S4-16`
  (*settling basin*) seçilmişti; betik ikisinin de `L2` tam testinde kullanıldığını
  yakaladı, sorular `L2-S4-03` (*silt*) ve `L2-S4-13` (*water table*) ile değiştirildi.

### Kullanılan `answer_point_id` değerleri

| Küme | Kimlikler |
|---|---|
| `P-SA-01` (L1-S4) | `L1-S4-03`, `L1-S4-06`, `L1-S4-08`, `L1-S4-22` |
| `P-SA-02` (L2-S4) | `L2-S4-03`, `L2-S4-09`, `L2-S4-13`, `L2-S4-20` |
| `P-SA-03` (L4-S4) | `L4-S4-03`, `L4-S4-13`, `L4-S4-22`, `L4-S4-34` |
| `P-SA-04` (L5-S4) | `L5-S4-02`, `L5-S4-05`, `L5-S4-20` |

Cevaplar: 1 `fifty years` · 2 `rooftop farm` · 3 `41` · 4 `raised beds` · 5 `silt` ·
6 `a third` · 7 `water table` · 8 `ten degrees` · 9 `logarithmic` · 10 `railways` ·
11 `line of sight` · 12 `an hour` · 13 `one micrometre` · 14 `gear` ·
15 `every fifteen years`.

Çeldiricili bilgi noktasından çıkan soru **yalnızca 6** (açık kanaldan buharlaşma kaybı:
yarısı → üçte biri; cevap düzeltilmiş değer). Sebebi aşağıda, "Bilinçli sapmalar" 1.
maddede.

### Doğrulama

- Denetim betiği depoda: `tools/_p11_kontrol.py` (9. paketinkinin kısa cevaba uyarlanmış
  hâli; argümanla başka bir alıştırma dosyası da denetlenebiliyor). Sınadığı maddeler:
  zarf alanları, küme boyu (3–5), `context_line` ve `instructions` doluluğu, yönergede
  kelime sınırının yazılı olması, bilgi noktalarının **hem tam testlerde hem öteki
  alıştırma dosyalarında** kullanılmamış olması, `turn_index`in bilgi noktasıyla birebir
  uyuşması, küme içi sıranın geri gitmemesi, nefes payı, her `evidence`in ilgili replikte
  **birebir** geçmesi, cevabın replik metninde harfi harfine bulunması,
  **`accepted_variants` dahil** kelime sınırı, `prompt`un soru işaretiyle bitmesi ve
  boşluk işareti içermemesi, **2. altın kural** (soru kökü sesteki cümlenin
  sadeleştirilmiş kopyası mı), numaraların 1–15 dizisi olması, açıklamaların Türkçe ve
  dolu olması, "IELTS" taraması. **Hata 0, uyarı 0.**
- Aynı betik 10. paketin dosyasına da uygulandı: `python tools/_p11_kontrol.py
  content/listening/practice/flow-chart-completion.json` → **hata 0, uyarı 0**.
- Ardından `python tools/dogrula.py`: **şema hatası 0**, görünür metinde IELTS 0,
  yasak kaynak 0, `listening/practice` sayacı **75** (15 × 5).

### Bilinçli sapmalar

1. **Çeldirici oranı bu pakette düşük (15'te 1).** Sebep yapısal: altı 4. bölüm
   senaryosunun her birinde beşer çeldirici var ve **hepsi tam testlerde kullanılmış**
   (`L1-S4`, `L4-S4`, `L5-S4` için istisnasız; `L2-S4`'te yalnızca kanal kaybı boşta
   kalmıştı, o da bu pakete alındı). 7. altın kural "tercihen" diyor, aynı bilgi
   noktasını tekrar kullanma yasağı ise mutlak — ikisi çatışınca yasak öne alındı.
   Ayırt edicilik bunun yerine **replik içi konumdan** sağlandı: cevapların yarısı
   paragrafın ortasında, örnek ya da yan cümle içinde geçiyor (`silt`, `line of sight`,
   `gear`).
2. **Üç kümede THREE WORDS, birinde TWO WORDS.** `P-SA-02`nin dört cevabı da iki kelimeye
   sığdığı için sınır bilerek daraltıldı; kalan üç kümede `line of sight`,
   `commercial rooftop farm` ve `every fifteen years` üç kelime tuttuğu için gevşetildi.
   Zarf düzeyindeki `word_limit` en geniş olanı (THREE WORDS) gösteriyor, kümeler kendi
   sınırlarını yazıyor; hiçbir cevap kendi kümesinin sınırını aşmıyor.
3. **Cevap türü dağılımı** (8. altın kural): her kümede ardışık iki cevap farklı türden —
   süre/nesne/sayı/nesne (P-SA-01), madde/kesir/kavram/ölçü (P-SA-02),
   sıfat/kaynak/kavram/süre (P-SA-03), ölçü/sözcük/süre (P-SA-04). Toplamda 4 sayı-ölçü,
   11 sözcük; hiçbir kümede iki sayı yan yana değil.
4. **Nefes payı 4. bölüm ölçüsüyle uygulandı.** Tek kişilik anlatımda "replik" = paragraf
   olduğu için ayrı paragraf yeterli sayıldı (betik tek konuşmacıda asgari aralığı 1,
   karşılıklı konuşmada 2 tutuyor). Gerçek aralıklar: `L1-S4` 1·2·3·8, `L2-S4` 2·4·5·9,
   `L4-S4` 2·5·9·14, `L5-S4` 1·2·8 — dört kümede de cevaplar dersin tamamına yayıldı,
   son soru her zaman dersin son üçte birinden.
5. **Soru kökleri baştan sona yeniden ifade edildi** (2. altın kural). Örnek: ses
   "silt settles instead of travelling, and the channel blocks" diyor, soru kökü
   "If the tunnel is given too little fall, what collects in it and stops the flow?";
   ses "a barrier works by breaking the line of sight between the source and the ear"
   diyor, soru kökü "What has a wall got to interrupt between the traffic and the
   listener…" — cevap sözcüğü birebir, çevresi değil. Betik bu kuralı sadeleştirilmiş
   metin karşılaştırmasıyla ayrıca sınıyor.
6. **Zor yazımlı hiçbir terim sorulmadı** (6. altın kural). `manta trawl` ve `biofouling`
   gibi seste harf harf söylenmeyen teknik adlar aday listesindeydi, elendi; kalan
   cevapların hepsi günlük yazımı belli sözcükler. Amerikan yazımı olabilecek tek cevapta
   (`micrometre`) her iki biçim de kabul listesinde.

### Telif / yazım

- İngiliz İngilizcesi (`metre`, `kilometres`, `micrometre`, `railways`); bütün kişi, kurum
  ve yer adları senaryolardan geliyor, hepsi uydurma. Görünür metinde "IELTS" yok.
- ⚠️ **Referans PDF'leri bu oturumda da açılamadı:** `referans/` altında yalnızca `.pdf`
  var, `referans/text/` hâlâ üretilmemiş ve `Read` aracı PDF için poppler istiyor, ortamda
  yok. Kısa cevap yönerge kalıbı L1–L6 tam testlerinin `short-answer.json` setlerinden
  devralındı ("Answer the questions below. Write NO MORE THAN THREE WORDS AND/OR A NUMBER
  for each answer."). Yeni biçim icat edilmedi; referanstan **tek bir cümle, soru ya da
  senaryo kopyalanmadı**.
- Atlanan/sorun: yok. **OPUS5-21'de 12 paketten 11'i tamam;** geriye tek paket kaldı:
  **12 — alıştırma: plan / harita / diyagram etiketleme (15 soru)**, dosyası
  `content/listening/practice/plan-map-diagram-labelling.json`. Sonraki oturuma not:
  bu tip **2. bölümde** geçiyor, yani `L*-S2` senaryolarına ve onların
  `spatial_description` alanlarına bakılmalı; alıştırmalarda 2. bölüm senaryolarının
  **hiçbiri henüz kullanılmadı**, dolayısıyla altı senaryo da (`L1-S2` … `L6-S2`) boşta.
  Tam testler her `L*-S2`den 5 nokta kullanmış, geri kalanlar serbest. SVG kuralları
  promptun "Plan / harita / diyagram etiketleme" bölümünde; harf seçme ve kelime yazma
  alt tiplerinin **ikisi de** kullanılmalı (tam testlerde L1–L3 harf seçme, L4–L6 kelime
  yazma dizilişi vardı).

## OPUS5-21 (12. çalıştırma: alıştırma — plan / harita / diyagram etiketleme, 15 soru)

- Tarih: 2026-08-05
- Depo kontrolü: `content/listening/tests/` altında **`L1/` … `L6/`** tam (6 × 29 = 174);
  `content/listening/practice/` altında `note-completion.json` (7), `table-completion.json`
  (8), `sentence-completion.json` (9), `flow-chart-completion.json` (10) **ve**
  `short-answer.json` (11) vardı. Çalıştırma listesinde geriye tek paket kalmıştı:
  **12 — alıştırma: plan / harita / diyagram etiketleme**; o yapıldı. 24 senaryonun hepsi
  yerinde, hiçbirine dokunulmadı, yeni bilgi noktası eklenmedi.
- Çıktı: `content/listening/practice/plan-map-diagram-labelling.json` — **15 soru,
  4 küme**, `test_id: null`, `practice: true`, numaralar 1'den 15'e. Etiketlemede gövde
  çizimin içinde olduğu için `stem_block` **ve** `table` her düzeyde `null`; boşluk
  işareti (`........`) hiçbir promptta geçmez, boşluklar SVG'nin içinde numaralı.
- **Bu paketle OPUS5-21 tamam:** 174 tam test + 90 alıştırma = **264 soru**.

### Kümeler, senaryolar ve seçilen alt tipler

| Küme | Senaryo | Bölüm | Sorular | Çizim | Alt tip | Kelime sınırı |
|---|---|---|---|---|---|---|
| `P-PM-01` | `L3-S2` | 2 | 1–4 | kır parkı haritası | kelime yazma | THREE WORDS |
| `P-PM-02` | `L4-S2` | 2 | 5–8 | geri dönüşüm merkezi planı | harf seçme (A–H) | — |
| `P-PM-03` | `L6-S2` | 2 | 9–12 | kapalı çiftçi pazarı planı | kelime yazma | TWO WORDS |
| `P-PM-04` | `L1-S2` | 2 | 13–15 | müze zemin + üst kat planı | harf seçme (A–H) | — |

- Kümeler **4 + 4 + 4 + 3**; hiçbir senaryodan 4'ten fazla soru yok.
- **Dört kümenin dördü de 2. bölüm** senaryosundan: promptun tip tablosunda bu tip
  yalnızca 2. bölüme yazılı (tam testte 16–20 aralığı) ve `spatial_description` alanı
  yalnızca `L*-S2` dosyalarında var. Alıştırmalarda 2. bölüm senaryoları **ilk kez**
  kullanıldı; senaryo başına alıştırma yükü artık `L1-S2` 3, `L3-S2` 4, `L4-S2` 4,
  `L6-S2` 4.
- **İki alt tip de kullanıldı** ve tam testlerin tersine çevrildi: tam testlerde `L1`/`L3`
  harf seçme, `L4`/`L6` kelime yazmaydı; alıştırmada `L1`/`L4` harf seçme, `L3`/`L6`
  kelime yazma. Aynı senaryoyu iki farklı görevle çalışan aday, planı ezberlemek yerine
  sesi takip etmek zorunda kalıyor.

### Kullanılan `answer_point_id` değerleri

| Küme | Kimlikler |
|---|---|
| `P-PM-01` (L3-S2) | `L3-S2-14`, `L3-S2-17`, `L3-S2-21`, `L3-S2-24` |
| `P-PM-02` (L4-S2) | `L4-S2-08`, `L4-S2-09`, `L4-S2-15`, `L4-S2-17` |
| `P-PM-03` (L6-S2) | `L6-S2-11`, `L6-S2-15`, `L6-S2-20`, `L6-S2-22` |
| `P-PM-04` (L1-S2) | `L1-S2-16`, `L1-S2-21`, `L1-S2-23` |

Cevaplar: 1 `visitor centre` · 2 `information hut` · 3 `pond-dipping platform` ·
4 `viewpoint` · 5 `C` (tuvaletler ve su noktası) · 6 `A` (otopark) · 7 `E` (cam, kutu ve
plastik kumbaraları) · 8 `G` (boya ve kimyasal deposu) · 9 `information desk` ·
10 `cheese counter` · 11 `seating area` · 12 `toilets` · 13 `A` (mağaza) ·
14 `C` (asansör) · 15 `G` (okuma odası).

Seçilen 15 noktanın hiçbiri tam testlerde ya da öteki beş alıştırma dosyasında yok
(kesişim betikle çıkarıldı, **boş**). Tam testlerin `L*-S2` planlarında kullandığı beş
mekân bu pakette **çizimde adıyla yazılı sabit referans** olarak kullanıldı — böylece
aynı bilgi noktası soru olmadan aday için çapa görevi görüyor (`WEAVING GALLERY`,
`BIRD HIDE`, `SITE OFFICE`, `RAMP`, `FLOWER STALL` gibi).

### Çizimler

Dört SVG elle çizildi, üretici betikte duruyor (`tools/_p12_uret.py`). Promptun SVG
kurallarına uyuldu: sadece `rect`, `circle`, `line`, `path`, `polygon`, `text`; tek renk
`#000`, dolgu yok; `viewBox` var, sabit `width`/`height` yok; `font-size="12"`,
`font-family="sans-serif"`; her çizimde **kuzey oku**, **giriş oku** ve en az bir adıyla
yazılı sabit referans noktası var. Harf seçme planlarında sekiz konumun hepsi (A–H)
daire içinde harfle, kelime yazma planlarında boşluklar numara + alt çizgi ile gösterildi.
`P-PM-04` iki panelli: solda zemin kat (A–E), sağda üst kat (F–H); merdivenin çıkış yönü
okla verildi ki "merdivenin başında sağda" ifadesi tek anlama gelsin.

### Doğrulama

- Üretici: `tools/_p12_uret.py`. Denetim betiği: `tools/_p12_kontrol.py`
  (11. paketinkinin etiketlemeye uyarlanmış hâli). Sınadığı maddeler: zarf alanları,
  küme boyu (3–5), `context_line`/`instructions` doluluğu, kelime yazma kümelerinde
  yönergede sınırın yazılı olması, bilgi noktalarının **hem tam testlerde hem öteki
  alıştırma dosyalarında** kullanılmamış olması, `turn_index`in bilgi noktasıyla birebir
  uyuşması, sıra kuralı, nefes payı, her `evidence`in ilgili replikte **birebir** geçmesi,
  kelime cevaplarının replik metninde harfi harfine bulunması, harf cevaplarında soru
  kökündeki yer adının `evidence` içinde geçmesi, **`accepted_variants` dahil** kelime
  sınırı, promptta boşluk işareti bulunmaması, seçenek/boşluk etiketinin çizimde gerçekten
  yer alması, `visual.labels` ile seçenek/numara listesinin örtüşmesi, SVG kuralları
  (tek satır, `viewBox`, sabit `width`/`height` yok, izinsiz etiket yok, siyah dışı renk
  yok, XML olarak çözülebilmesi, kuzey oku + giriş + sabit referans), iki alt tipin de
  kullanılmış olması, numaraların 1–15 dizisi olması, açıklamaların Türkçe ve dolu olması,
  "IELTS" taraması. **Hata 0, uyarı 0.**
- Ek geometri kontrolü (tek seferlik, çizimler için): dört SVG'de de `viewBox` dışına
  taşan nokta **yok**, üst üste binen dikdörtgen **yok**, çakışan metin kutusu **yok**,
  A–H daireleri ve 1–12 boşluk numaralarının her biri **tam olarak bir** dikdörtgenin
  içinde. (İki durumda iki etiket aynı dış dikdörtgende: `P-PM-02`de uzun tek katlı bina,
  `P-PM-03`te uzun tezgâh — ikisi de içinden bölme çizgisiyle ayrılmış, kasıtlı.)
- Ardından `python tools/dogrula.py`: **şema hatası 0**, görünür metinde IELTS 0,
  yasak kaynak 0, `listening/practice` sayacı **90** (15 × 6 — alıştırma tarafı tamam).

### Bilinçli sapmalar

1. **`L2-S2` ve `L5-S2` kullanılmadı.** Tam testler bu iki senaryodan beşer mekân noktası
   almış; geriye `L2-S2`de 2 (`-16` danışma masası, `-17` gazete alanı), `L5-S2`de 2
   (`-09` bilet gişesi, `-14` su noktası) mekân noktası kalıyor. Küme en az 3 soru olmalı
   ve **bir küme tek senaryodan** geleceği için bu ikisinden küme kurulamadı. Kalan dört
   senaryonun kapasitesi tam tamına 4 + 4 + 4 + 3 = **15**; yani paket ancak bu dağılımla
   çıkıyordu.
2. **`L1-S2`den 3 soru.** Kullanılmamış noktalar t6 (mağaza), t8 (asansör **ve** avlu
   bahçesi) ve t9 (okuma odası). 4. altın kural iki cevabın aynı replikte olmasını
   yasakladığı için t8'den yalnız biri alınabildi → küme 3 soru; dosyadaki en küçük küme
   bilerek bu oldu.
3. **`P-PM-01`de THREE WORDS, `P-PM-03`te TWO WORDS.** `pond-dipping platform` tireli
   yazılınca iki, tiresiz üç kelime; iki yazımın da kabul edilebilmesi için o kümede sınır
   gevşetildi (`accepted_variants`ta ikisi de var). `P-PM-03`te dört cevabın dördü de iki
   kelimeye sığdığı için sınır daraltıldı. Zarf düzeyindeki `word_limit` en geniş olanı
   gösteriyor, kümeler kendi sınırlarını yazıyor; hiçbir cevap kendi kümesinin sınırını
   aşmıyor.
4. **Çeldirici 15'te 1** (7. soru: kumbaraların yeri — "ofisin yanındaydı" → çıkış
   bariyerinin dibi; cevap düzeltilmiş konum). Yapısal sebep: `L*-S2` senaryolarındaki
   çeldiricilerin büyük çoğunluğu **mekân dışı** (saat, ücret, gün, sayı) ve mekânla
   ilgili olanlar (`L5-S2` sahnenin yönü, `L6-S2` balık tezgâhının yeri) tam testlerde
   kullanılmış. Ayırt edicilik bunun yerine **plandaki boş konumlardan** geliyor: harf
   seçme planlarında sekiz konum var, `P-PM-02`de dördü, `P-PM-04`te beşi sorulmuyor;
   yani yanlış harfi seçmek çok kolay.
5. **Cevap türü dağılımı** (8. altın kural). Etiketlemede cevapların tamamı yer adı olmak
   zorunda; kural bu tipte ancak biçim çeşitliliğiyle uygulanabildi: kelime yazma
   kümelerinde tek kelime / iki kelime / tireli birleşik dönüşümlü
   (`viewpoint` – `information hut` – `pond-dipping platform` – `toilets`), harf seçme
   kümelerinde cevap harfleri planın dört bir yanına dağıtıldı (C·A·E·G ve A·C·G).
   Hiçbir kümede iki cevap yan yana konumda değil.
6. **Sıra ve nefes payı.** Dört senaryo da tek konuşmacılı olduğu için "replik" = paragraf
   sayıldı (betik tek konuşmacıda asgari aralığı 1 tutuyor). Gerçek diziler: `L3-S2`
   5·6·7·8, `L4-S2` 3·4·6·7, `L6-S2` 4·5·7·8, `L1-S2` 6·8·9 — hepsi artan, hiçbir iki
   cevap aynı replikte değil ve her kümede cevaplar mekân tarifinin başından sonuna
   yayıldı.
7. **Zor yazımlı isim sorulmadı** (6. altın kural). Seste harf harf söylenen ad yok, o
   yüzden bütün kelime cevapları günlük yazımı belli sözcüklerden seçildi. Amerikan
   yazımı olabilecek tek cevapta (`visitor centre`) `visitor center` de kabul listesinde;
   `viewpoint` için ayrık yazım (`view point`) da kabul ediliyor.

### Telif / yazım

- İngiliz İngilizcesi (`centre`, `theatre`, `car park`, `cloakroom`); bütün yer, kurum ve
  sokak adları senaryolardan geliyor, hepsi uydurma. Görünür metinde "IELTS" yok.
  Çizimlerdeki bütün etiketler senaryoların `spatial_description` alanından.
- ⚠️ **Referans PDF'leri bu oturumda da açılamadı:** `referans/` altında yalnızca `.pdf`
  var, `referans/text/` hâlâ üretilmemiş ve `Read` aracı PDF için poppler istiyor, ortamda
  yok. Etiketleme yönerge kalıpları L1–L6 tam testlerinin
  `plan-map-diagram-labelling.json` setlerinden devralındı ("Label the plan below. Write
  the correct letter, A–H, next to Questions …" ve "Label the plan below. Write NO MORE
  THAN TWO WORDS AND/OR A NUMBER for each answer."). Yeni biçim icat edilmedi;
  referanstan **tek bir cümle, soru ya da senaryo kopyalanmadı**.
- Atlanan/sorun: yok. **OPUS5-21'in 12 paketinin hepsi tamam** (174 tam test sorusu +
  90 alıştırma sorusu = 264). Dinleme tarafında geriye yalnızca `FABLE5-43` kaldı:
  her testte boş bırakılan **11–15 ve 21–26** aralıkları ile üç alıştırma dosyası
  (çoktan seçmeli tek cevaplı, çoktan seçmeli çok cevaplı, eşleştirme).

## OPUS5-30 (1. çalıştırma: konuşma 1. bölüm — oturum 1, 5 konu × 10 soru)

- Tarih: 2026-08-05
- Depo kontrolü: `content/speaking/`, `content/writing/` ve bütün alt klasörleri
  (`part1`, `part2-3`, `academic-task1`, `general-task1`, `task2`) **tamamen boştu**;
  `NOTLAR.md` içinde "OPUS5-30" ya da "konuşma" geçen tek bir kayıt yoktu. Yani bu, bu
  promptun gerçekten **1. çalıştırmasıydı** ve çalıştırma listesindeki ilk paket
  (**Konuşma 1. bölüm, oturum 1**) yapıldı. **50 soru** üretildi, hedefle birebir aynı.
- Üretilen dosyalar (prompt A bölümündeki oturum-1 konu dağılımına birebir uyuldu):
  - `content/speaking/part1/T01-hometown.json` — memleket
  - `content/speaking/part1/T02-accommodation.json` — ev / daire
  - `content/speaking/part1/T03-work-or-study.json` — iş veya çalışma
  - `content/speaking/part1/T04-free-time.json` — boş zaman
  - `content/speaking/part1/T05-food.json` — yemek
- **KULLANILAN KONULAR (sonraki oturumlar tekrar etmesin):** Hometown · Home and
  accommodation · Work or study · Free time · Food.
  **Oturum 2'ye kalan:** hava durumu ve mevsimler · müzik · ulaşım · alışveriş · arkadaşlar.
  **Oturum 3:** spor ve egzersiz · fotoğraf · kitap ve okuma · teknoloji · uyku.
  **Oturum 4:** seyahat · sanat ve el işi · hayvanlar · zaman yönetimi · komşuluk.
- **Soru kurgusu kararı — "evet/hayır" kuralı ile "ilk 3 soru `Do you…?` olsun" tavsiyesi
  çatışıyor.** Prompt hem `Do you…?` kalıbını örnek veriyor hem de "evet/hayırla kapanan
  soru yazma" diyor. Çözüm: ilk üç soru da **wh- / how often** kalıbında yazıldı
  (`Where is your hometown?`, `How often do you go into the centre…?`), yardımcı fiille
  başlayan tek soru **seçenekli** kuruldu (`Do you work, or are you a student?` — resmî
  örnekteki açılışın işlevsel karşılığı, kopya değil). Böylece hiçbir soru tek kelimeyle
  kapanmıyor. **Sonraki oturumlar bu düzeni sürdürsün.**
- Her sette 10 sorunun **odak (`focus`) alanları** promptun listesini dolaşıyor: temel bilgi
  / tanımlama · alışkanlık · tercih · sebep · geçmiş · değişim · başkaları açısı ·
  varsayım · gelecek · karşılaştırma. Set başına en az 7 farklı `focus` var, hiçbir soru
  metni beş dosya boyunca tekrar etmiyor.
- **Zorluk düzeni:** her sette 1–3 `easy`, 4–7 çoğunlukla `medium`, 8–10 `hard` (soyutlaşan
  ve gerekçe isteyen sorular sona konuldu). 4. sorudan sonra hiç `easy` yok.
- `useful_language`: soru başına 4 ifade, band 7 seviyesinde, İngiliz İngilizcesi
  (`flat`, `centre`, `outskirts`, `washing-up`, `have a go at`). Kültürel tarafsızlık için
  aday hakkında hiçbir varsayım yok: T02'de "kendi eviniz mi" sorulmuyor, T03 hem çalışan
  hem öğrenci için işliyor, T05'te alkol/din/bayram geçmiyor, T01'de "ülkeniz" değil
  "memleketiniz" ekseni kullanılıyor.
- Doğrulama: geçici denetim scriptiyle (`tools/_sp1_kontrol.py`, sonra silindi) beş dosya
  için JSON geçerliliği, zarf alanlarının tamlığı, `set_id` ↔ dosya adı eşleşmesi,
  soru sayısı (tam 10), numaraların 1–10 sırası, her sorunun **tek cümle** olması (tek `?`,
  ≤95 karakter), evet/hayırla kapanabilecek kalıpların yakalanması, `useful_language`
  sayısı (3–5) ve içinde tekrar olmaması, zorluk düzeni, `focus` çeşitliliği ve "IELTS"
  geçmemesi denetlendi — **ilk turda hata 0.**
- ⚠️ **`tools/dogrula.py` genişletildi.** Script yalnız okuma/dinleme soru setleri için
  yazılmıştı: her dosyada `test_id` · `practice` · `question_type` · `instructions` zarf
  alanlarını ve her soruda `answer` · `explanation` · `evidence` arıyordu. Konuşma/yazma
  birimlerinde **cevap anahtarı yok** (promptun kendi ifadesi), dolayısıyla beş yeni dosya
  script'e 200'ü aşkın sahte hata bastırıyor ve çıkış kodunu 1 yapıp gerçek hataları
  görünmez kılıyordu. Eklenen `konusma_yazma_denetle()` fonksiyonu `skill` alanı
  `speaking`/`writing` olan dosyaları kendi şemasına göre denetliyor
  (part1 → `items` + alanlar; part2-3 → tam 3 madde, `and explain…` ile başlayan `closing`,
  3 tartışma sorusu; writing → `module`/`task`/`prompt`/`key_points`, academic 1. görevde
  `visual` ya da `visuals` zorunlu) ve sayımı `speaking/part1`, `speaking/part2-3`,
  `writing/task1|2` başlıklarıyla ayrı raporluyor. Telif taramasındaki `gorunur` sözlüğüne
  de yazma `prompt`u ile `part2`/`part3` eklendi ki "IELTS" araması bu dosyaları da kapsasın.
  Sonuç: `python tools/dogrula.py` → **şema hatası 0**, konuşma sorusu 50, görünür metinde
  IELTS 0, yasak kaynak 0. **Sonraki OPUS5-30 oturumları bu denetimden geçmeli.**
- ℹ️ **DURUM.txt sayacı için not:** `tools/calistir.py` içindeki `_soru_say()` yalnızca
  üst düzey `items` / `groups` listesini sayıyor. Part 1 dosyaları doğru sayılıyor (50),
  ama **part2-3 dosyalarında sorular `part2`/`part3` altında** olduğu için o paketler
  geldiğinde DURUM.txt'deki "Konusma sorusu" satırı olduğundan az gösterecek. Sayaç
  bilgilendirme amaçlı, üretimi engellemiyor; düzeltilecekse `_soru_say()`e part2-3 dalı
  eklenmeli.
- Referans: `referans/ielts-speaking-sample-tasks-2023.pdf` bu oturumda **`Read` aracıyla
  sorunsuz açıldı** (önceki oturumlardaki poppler sorunu bu dosyada çıkmadı) ve yalnız
  format referansı olarak kullanıldı: 1. bölümde görevlinin konu geçiş cümlesi + numaralı
  kısa sorular düzeni, 2. bölümde `Describe …` + `You should say:` + üç madde + `and
  explain …` kalıbı, 3. bölümde konudan soyutlanmış genel sorular. **Tek bir soru, cümle
  ya da replik kopyalanmadı**; örnekteki konular (home town/accommodation) bizim oturum-1
  listemizle örtüşüyor ama sorular baştan yazıldı.
- Atlanan/sorun: yok. **OPUS5-30'da 16 paketten 1'i tamam (50/550 birim).** Sıradaki iş
  **oturum 2** (hava durumu ve mevsimler · müzik · ulaşım · alışveriş · arkadaşlar),
  yine `content/speaking/part1/` altına `T06`–`T10` kimlikleriyle.

## OPUS5-30 (2. çalıştırma: konuşma 1. bölüm — oturum 2, 5 konu × 10 soru)

- Tarih: 2026-08-05
- Depo kontrolü: `content/speaking/part1/` altında **T01–T05 tamdı** (50 soru),
  `content/speaking/part2-3/`, `content/writing/academic-task1/`, `general-task1/` ve
  `task2/` klasörlerinde **hiç dosya yoktu**. Yani çalıştırma listesindeki sıradaki
  bitmemiş paket **Konuşma 1. bölüm, oturum 2** idi, o yapıldı. Kullanıcının tanımı
  ("2. çalıştırma") depo durumuyla **birebir uyuştu**, önceki oturumlardaki numara kayması
  burada yok. **50 soru** üretildi, hedefle birebir aynı.
- Üretilen dosyalar (prompt A bölümündeki oturum-2 konu dağılımına birebir uyuldu):
  - `content/speaking/part1/T06-weather-and-seasons.json` — hava durumu ve mevsimler
  - `content/speaking/part1/T07-music.json` — müzik
  - `content/speaking/part1/T08-transport.json` — ulaşım
  - `content/speaking/part1/T09-shopping.json` — alışveriş
  - `content/speaking/part1/T10-friends.json` — arkadaşlar
- **KULLANILAN KONULAR (sonraki oturumlar tekrar etmesin):** Hometown · Home and
  accommodation · Work or study · Free time · Food · **Weather and seasons · Music ·
  Transport · Shopping · Friends**.
  **Oturum 3'e kalan:** spor ve egzersiz · fotoğraf · kitap ve okuma · teknoloji · uyku.
  **Oturum 4:** seyahat · sanat ve el işi · hayvanlar · zaman yönetimi · komşuluk.
- 1. oturumda alınan **soru kurgusu kararı sürdürüldü:** yardımcı fiille başlayan
  (`Do you…?`, `Would you…?`) soru yalnızca **seçenekli** olduğunda kullanılıyor —
  bu sette tek örnek T07/6 (`Would you rather listen to a recording or hear music played
  live?`). Kalan 49 soru wh- / how kalıbında, hiçbiri tek kelimeyle kapanmıyor.
- **Tekrardan kaçınma:** T04 ve T05'te "…changed in recent years?" kalıbı iki kez
  kullanılmıştı; bu sette değişim soruları bilinçli olarak farklı kuruldu —
  `What differences have you noticed…` (T06), `How is … different from twenty years ago?`
  (T07), `In what ways is … easier than it used to be?` (T08),
  `How have the shops … changed since you were a child?` (T09),
  `How has the way people keep in touch … changed?` (T10). On dosya boyunca **aynı soru
  metni iki kez geçmiyor** (script bunu tüm part1 havuzunda denetledi).
- **Zorluk düzeni** 1. oturumdaki gibi: 1–3 `easy`, 4–7 `medium`, 8–10 `hard`; 4. sorudan
  sonra hiç `easy` yok. Her sette en az 7 farklı `focus` var (temel bilgi · alışkanlık ·
  tercih ve sebep · açıklama · geçmiş · başkaları açısı ve sebep · varsayım / öneri /
  gelecek · değişim · karşılaştırma).
- `useful_language`: soru başına 4 ifade, band 7 seviyesinde, İngiliz İngilizcesi
  (`fortnight`, `pop in`, `spoilt for choice`, `come round to it`, `queueing`, `cycle
  lanes`). Kültürel tarafsızlık: T06'da belirli bir iklim varsayılmıyor (hem "we get a lot
  of rain" hem "it can be quite humid" seçenek olarak veriliyor), T08'de araba sahipliği
  varsayılmıyor, T09'da harcama gücü varsayılmıyor ("I only buy what I need"), T10'da
  aile/ev düzeni hakkında varsayım yok. Din, alkol, siyaset, bayram geçmiyor; gerçek
  marka/kurum/kişi adı yok.
- Doğrulama: geçici denetim scriptiyle (`tools/_sp2_kontrol.py`, sonra silindi) beş dosya
  için JSON geçerliliği, zarf alanlarının tamlığı, `set_id` ↔ dosya adı eşleşmesi, soru
  sayısı (tam 10), numara sırası, her sorunun **tek cümle** olması (tek `?`, nokta/noktalı
  virgül yok, ≤95 karakter), evet/hayırla kapanabilecek kalıpların yakalanması (seçenekli
  sorular muaf), `useful_language` sayısı (3–5) ve dosya içi tekrar, Amerikan yazımı
  taraması, zorluk düzeni, `focus` çeşitliliği, **tüm part1 havuzunda soru metni tekrarı**
  ve "IELTS" geçmemesi denetlendi — **ilk turda hata 0.** Ardından
  `python tools/dogrula.py`: **şema hatası 0**, konuşma sorusu 100 (oturum 1'in 50'si +
  bu oturumun 50'si), pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0.
  `tools/dogrula.py`'ye 1. oturumda eklenen `konusma_yazma_denetle()` bu dosyaları da
  sorunsuz kapsadı, script'te değişiklik gerekmedi.
- Referans: bu oturumda referans PDF'i açılmadı — 1. oturumda
  `ielts-speaking-sample-tasks-2023.pdf` format için okunmuş ve kararı NOTLAR'a yazılmıştı
  (numaralı kısa sorular düzeni), aynı düzen sürdürüldü. `referans/text/` klasörü hâlâ yok.
  Hiçbir soru/cümle kopyalanmadı.
- Atlanan/sorun: yok. **OPUS5-30'da 16 paketten 2'si tamam (100/550 birim).** Sıradaki iş
  **oturum 3** (spor ve egzersiz · fotoğraf · kitap ve okuma · teknoloji · uyku), yine
  `content/speaking/part1/` altına `T11`–`T15` kimlikleriyle.

## OPUS5-30 (3. çalıştırma: konuşma 1. bölüm — oturum 3, 5 konu × 10 soru)

- Tarih: 2026-08-05
- Depo kontrolü: `content/speaking/part1/` altında **T01–T10 tamdı** (100 soru),
  `content/speaking/part2-3/`, `content/writing/academic-task1/`, `general-task1/` ve
  `task2/` klasörleri **hâlâ boştu**. Çalıştırma listesindeki sıradaki bitmemiş paket
  **Konuşma 1. bölüm, oturum 3** idi, o yapıldı; kullanıcının tanımı ("3. çalıştırma")
  depo durumuyla **birebir uyuştu**. **50 soru** üretildi, hedefle birebir aynı.
- Üretilen dosyalar (prompt A bölümündeki oturum-3 konu dağılımına birebir uyuldu):
  - `content/speaking/part1/T11-sport-and-exercise.json` — spor ve egzersiz
  - `content/speaking/part1/T12-photographs.json` — fotoğraf
  - `content/speaking/part1/T13-books-and-reading.json` — kitap ve okuma
  - `content/speaking/part1/T14-technology.json` — teknoloji
  - `content/speaking/part1/T15-sleep.json` — uyku
- **KULLANILAN KONULAR (sonraki oturumlar tekrar etmesin):** Hometown · Home and
  accommodation · Work or study · Free time · Food · Weather and seasons · Music ·
  Transport · Shopping · Friends · **Sport and exercise · Photographs · Books and
  reading · Technology · Sleep**.
  **Oturum 4'e kalan:** seyahat · sanat ve el işi · hayvanlar · zaman yönetimi · komşuluk.
  Oturum 4 bitince part 1 havuzu (20 konu × 10 soru = 200) tamamlanır; ardından
  **B paketi — `content/speaking/part2-3/`, 15 kart × 4 oturum** başlar.
- 1. oturumdaki **soru kurgusu kararı sürdürüldü:** yardımcı fiille başlayan soru yalnızca
  seçenekli olduğunda kullanılabilir. Bu sette hiç yok — 50 sorunun tamamı wh- / how
  kalıbında (`Which suits you better, a short nap or an early night?` gibi seçenekli
  sorular da wh- ile açılıyor), hiçbiri tek kelimeyle kapanmıyor.
- **Tekrardan kaçınma — bilinçli kalıp dağıtımı yapıldı.** Önceki 10 dosyada
  `Why do some people…?` üç kez, `…changed in recent years?` iki kez geçmişti. Bu sette
  `Why do some people…?` yalnız **bir kez** kullanıldı (T11/7); aynı işlevdeki diğer
  sorular farklı kuruldu: `What makes people want to…` (T12/7), `What stops many adults
  from…` (T13/7), `What do people gain from…` (T14/7), `What advice would you give…`
  (T15/7). Değişim soruları da beş ayrı kalıpta: `How have attitudes towards … changed
  since you were a child?` (T11), `What has changed about the way …?` (T12), `How much has
  the way people read changed …?` (T13), `How has technology changed the way …?` (T14),
  `Why do many people sleep less than they used to?` (T15). **15 dosyalık havuzda aynı
  soru metni iki kez geçmiyor** (script bunu 150 sorunun tamamında denetledi).
- **Zorluk düzeni** önceki iki oturumla aynı: 1–3 `easy`, 4–7 `medium`, 8–10 `hard`;
  4. sorudan sonra hiç `easy` yok. Her sette en az 7 farklı `focus` var (temel bilgi ·
  alışkanlık · tercih ve sebep · açıklama · geçmiş · başkaları açısı ve sebep · öneri ·
  varsayım · gelecek · görüş · değişim · karşılaştırma).
- `useful_language`: soru başına 4 ifade, band 7 seviyesinde, İngiliz İngilizcesi
  (`leisure centre`, `a fortnight`, `get to grips with`, `come round`, `have a go`,
  `programme`, `groggy`). Kültürel tarafsızlık: T11'de spor salonu üyeliği/ekipman
  varsayılmıyor ("I get most of it from daily life"), T12'de seyahat ya da pahalı fotoğraf
  makinesi varsayımı yok, T13'te kitap satın alma gücü varsayılmıyor ("I borrow most of
  them"), T14'te cihaz sahipliği tek tipe indirgenmiyor, T15'te ev düzeni/oda sayısı
  hakkında varsayım yok. Din, alkol, siyaset, savaş, sağlık teşhisi geçmiyor; gerçek
  marka/kurum/kişi adı yok — T14'te uygulama adı yerine `Which application…` soruluyor.
- Doğrulama: geçici denetim scriptiyle (`tools/_sp3_kontrol.py`, sonra silindi) JSON
  geçerliliği, zarf alanları, `set_id` ↔ dosya adı eşleşmesi, soru sayısı (tam 10),
  numara sırası, her sorunun **tek cümle** olması (tek `?`, nokta/noktalı virgül yok,
  ≤95 karakter), evet/hayırla kapanabilecek kalıplar (seçenekli sorular muaf),
  `useful_language` sayısı (3–5) ve dosya içi ifade tekrarı, Amerikan yazımı taraması,
  zorluk düzeni, `focus` çeşitliliği, **15 dosyalık havuzda soru metni tekrarı** ve
  "IELTS" geçmemesi denetlendi — **ilk turda hata 0.** Ardından
  `python tools/dogrula.py`: **şema hatası 0**, konuşma sorusu 150 (50+50+50), pasaj
  lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0. `konusma_yazma_denetle()`
  bu dosyaları da sorunsuz kapsadı, script'te değişiklik gerekmedi.
- Referans: bu oturumda da referans PDF'i açılmadı — format kararı 1. oturumda
  `ielts-speaking-sample-tasks-2023.pdf` okunarak verilmiş ve NOTLAR'a yazılmıştı
  (numaralı kısa sorular düzeni), aynı düzen sürdürüldü. `referans/text/` klasörü hâlâ
  yok. Hiçbir soru/cümle kopyalanmadı.
- Atlanan/sorun: yok. **OPUS5-30'da 16 paketten 3'ü tamam (150/550 birim).** Sıradaki iş
  **oturum 4** (seyahat · sanat ve el işi · hayvanlar · zaman yönetimi · komşuluk), yine
  `content/speaking/part1/` altına `T16`–`T20` kimlikleriyle.

## OPUS5-30 (4. çalıştırma: konuşma 1. bölüm — oturum 4, 5 konu × 10 soru)

- Tarih: 2026-08-05
- Depo kontrolü: `content/speaking/part1/` altında **T01–T15 tamdı** (150 soru),
  `content/speaking/part2-3/`, `content/writing/academic-task1/`, `general-task1/` ve
  `task2/` klasörleri **hâlâ boştu**. Çalıştırma listesindeki sıradaki bitmemiş paket
  **Konuşma 1. bölüm, oturum 4** idi, o yapıldı; kullanıcının tanımı ("4. çalıştırma")
  depo durumuyla **birebir uyuştu**. **50 soru** üretildi, hedefle birebir aynı.
  Bu paketle birlikte **A paketi (konuşma 1. bölüm) tamamlandı: 20 konu × 10 soru = 200.**
- Üretilen dosyalar (prompt A bölümündeki oturum-4 konu dağılımına birebir uyuldu):
  - `content/speaking/part1/T16-travel.json` — seyahat
  - `content/speaking/part1/T17-art-and-crafts.json` — sanat ve el işi
  - `content/speaking/part1/T18-animals.json` — hayvanlar
  - `content/speaking/part1/T19-time-management.json` — zaman yönetimi
  - `content/speaking/part1/T20-neighbours.json` — komşuluk
- **KULLANILAN KONULAR (part 1 havuzu artık kapalı, hiçbiri tekrar edilmeyecek):**
  Hometown · Home and accommodation · Work or study · Free time · Food · Weather and
  seasons · Music · Transport · Shopping · Friends · Sport and exercise · Photographs ·
  Books and reading · Technology · Sleep · **Travel · Art and crafts · Animals · Time
  management · Neighbours**.
  **Sıradaki paket B: `content/speaking/part2-3/`, oturum başına 15 kart + kart başına 3
  tartışma sorusu, 4 oturum (`C01`–`C60`).** Kart türü kotası 60 kart geneli içindir
  (kişi 12 · yer 12 · nesne 12 · olay/deneyim 16 · soyut 8); her oturumda dörtte birini
  (kişi 3 · yer 3 · nesne 3 · olay 4 · soyut 2) üretmek kotayı sonda tutturur.
  Part 1'de kullanılan 20 konu, kart konusu seçilirken de **doğrudan tekrar edilmemeli**
  (ör. "Describe a photograph you like" T12'yle çakışır; kartlar daha somut/olaya bağlı
  kurulmalı).
- 1. oturumdaki **soru kurgusu kararı sürdürüldü:** yardımcı fiille başlayan soru yalnızca
  seçenekli olduğunda kullanılabilir. Bu sette bir örnek var (T20/6
  `Which would you rather have, quiet neighbours or sociable ones?` — `Which` ile açılıyor,
  T17/4 de aynı biçimde). 50 sorunun tamamı wh- / how kalıbında, hiçbiri tek kelimeyle
  kapanmıyor.
- **Tekrardan kaçınma — üç kalıp bilinçli olarak seyreltildi.** Önceki 15 dosyada
  `How is X different from Y?` sekiz kez, `Why do some people…?` beş kez, `How often do
  you…?` altı kez geçmişti. Bu sette `How is X different from Y?` yalnız **bir kez**
  (T18/10); aynı işlevdeki diğer karşılaştırmalar farklı kuruldu:
  `Which gives more satisfaction, … or …?` (T17/10), `How is organising your own time
  different from following someone else's timetable?` (T19/10 — tek diğer örnek),
  `How do relationships between neighbours differ between towns and villages?` (T20/10),
  `In what ways do people change after…?` (T16/10). `Why do some people…?` bu sette **hiç
  yok**; yerine `Why do many adults stop…` (T17/7), `Why do so many people feel short of
  time…` (T19/9), `Why do people in cities often…` (T20/9), `Why are handmade objects
  becoming popular again…` (T17/9) kullanıldı. **20 dosyalık havuzda 200 sorunun tamamı
  benzersiz** (script tüm havuzda denetledi).
- **Zorluk düzeni** önceki üç oturumla aynı: 1–3 `easy`, 4–7 `medium`, 8–10 `hard`;
  4. sorudan sonra hiç `easy` yok. Her sette en az 7 farklı `focus` var (temel bilgi ·
  alışkanlık · son deneyim · geçmiş · tercih ve sebep · açıklama · sebep · gözlem · öneri ·
  strateji · görüş · varsayım · değişim · karşılaştırma · başkaları açısı ve sonuç).
- `useful_language`: soru başına 4 ifade, band 7 seviyesinde, İngiliz İngilizcesi
  (`spur-of-the-moment`, `hanging about`, `keen on`, `shop-bought`, `first-name terms`,
  `keep themselves to themselves`, `off my plate`, `a fortnight`, `organising`).
  **Kültürel tarafsızlık ve ayrıcalık varsayımı yok:** T16 uçakla/yurt dışına seyahat
  varsaymıyor — sorular "day out", "somewhere unfamiliar", "school trips" üzerinden
  kuruldu ve `What kind of places do you enjoy visiting?` ile açılıyor; T17 pahalı malzeme
  ya da müze erişimi varsaymıyor ("there isn't much on offer, to be honest" seçenek olarak
  verildi); T18 **evcil hayvan sahipliği varsaymıyor** (soru 2 "how much contact", soru 7
  başkaları açısından soruluyor); T19 ofis işi ya da esnek çalışma varsaymıyor; T20 müstakil
  ev/bahçe varsaymıyor ("the ones on my floor", "the flats"). Din, alkol, siyaset, savaş,
  avcılık, hayvan hakları tartışması, cinsellik geçmiyor; gerçek marka/kurum/kişi adı yok.
- Doğrulama: geçici denetim scriptiyle (`tools/_sp4_kontrol.py`, sonra silindi) JSON
  geçerliliği, zarf alanları, `set_id` ↔ dosya adı eşleşmesi, soru sayısı (tam 10),
  numara sırası, her sorunun **tek cümle** olması (tek `?`, nokta/noktalı virgül yok,
  ≤95 karakter), evet/hayırla kapanabilecek kalıplar (seçenekli sorular muaf),
  `useful_language` sayısı (3–5) ve dosya içi ifade tekrarı, Amerikan yazımı taraması,
  zorluk düzeni, `focus` çeşitliliği, **20 dosyalık havuzda soru metni tekrarı** ve
  "IELTS" geçmemesi denetlendi — **ilk turda hata 0** (200 benzersiz soru).
  Ardından `python tools/dogrula.py`: **şema hatası 0**, konuşma sorusu **200**
  (50+50+50+50), pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0.
  `konusma_yazma_denetle()` bu dosyaları da sorunsuz kapsadı, script'te değişiklik
  gerekmedi. Rapordaki "TAM TEST BUTUNLUGU … EKSIK" satırları bu paketle ilgisiz —
  henüz üretilmemiş okuma/dinleme soru tipleri.
- Referans: bu oturumda da referans PDF'i açılmadı — format kararı 1. oturumda
  `ielts-speaking-sample-tasks-2023.pdf` okunarak verilmiş ve NOTLAR'a yazılmıştı
  (numaralı kısa sorular düzeni), aynı düzen sürdürüldü. `referans/text/` klasörü hâlâ
  yok. Hiçbir soru/cümle kopyalanmadı. **B paketine başlamadan önce aynı PDF'in 2. ve 3.
  bölüm sayfaları format için tekrar okunmalı** (kart düzeni ve `You should say:` girintisi).
- **DURUM.txt / ilerleme.txt bu oturumda elle güncellenmedi.** Bu oturum `CALISTIR.bat`
  yerine doğrudan başlatıldı; sayaç dosyalarını `tools/calistir.py` kendi commit'iyle
  ("durum: N/88") yazıyor, elle dokunmak runner'ın ilerlemesini bozabilirdi. DURUM.txt'teki
  "Konusma sorusu" satırı bir sonraki runner turunda 200/440 olacak.
- Atlanan/sorun: yok. **OPUS5-30'da 16 paketten 4'ü tamam (200/550 birim).** Sıradaki iş
  **B paketi, oturum 1** — `content/speaking/part2-3/` altına `C01`–`C15`: 15 kart
  (kişi 3 · yer 3 · nesne 3 · olay 4 · soyut 2) + her kart için 3 tartışma sorusu = 60 birim.

## OPUS5-30 (5. çalıştırma: konuşma 2.+3. bölüm — oturum 1, 15 kart + 45 tartışma sorusu)

- Tarih: 2026-08-05
- Depo kontrolü: `content/speaking/part1/` altında **T01–T20 tamdı** (200 soru, A paketi
  kapalı), `content/speaking/part2-3/` klasörü **hiç yoktu**, `content/writing/` altındaki
  üç klasör de boştu. Çalıştırma listesindeki sıradaki bitmemiş paket **B paketi, oturum 1**
  idi, o yapıldı; kullanıcının tanımı ("5. çalıştırma") depo durumuyla **birebir uyuştu**.
  **60 birim** üretildi (15 kart + 45 soru), hedefle birebir aynı.
- Üretilen dosyalar — `content/speaking/part2-3/C01.json` … `C15.json`:
  - **kişi (3):** C01 sabırlı bir kişi · C02 sohbetinden keyif alınan yaşlı biri ·
    C03 yakınlarda tanışılan, daha yakından tanınmak istenen biri
  - **yer (3):** C04 düşünmek için gidilen sessiz bir yer · C05 çevredeki ilginç bir bina ·
    C06 gidilen çok kalabalık bir yer
  - **nesne (3):** C07 sık giyilen bir giysi · C08 birine verilen bir hediye ·
    C09 yanınızdan ayırmadığınız küçük bir eşya
  - **olay/deneyim (4):** C10 tanınmayan birine yardım etmek · C11 uzun süre beklemek ·
    C12 planların son anda değişmesi · C13 bir şeyi ilk kez denemek
  - **soyut (2):** C14 değiştirmek istenen bir alışkanlık · C15 hâlâ hatırlanan bir öğüt
- **KULLANILAN KART KONULARI (sonraki oturumlar tekrar etmesin):** A patient person ·
  An older person you enjoy listening to · Someone you met recently · A quiet place for
  thinking · An interesting building · A crowded place · An item of clothing you wear often ·
  A gift you gave · A small object you always carry · Helping a stranger · A long wait ·
  A change of plans · Trying something for the first time · A habit you would like to
  change · Advice you still remember.
- **Kart türü kotası:** 60 kartlık hedefin (kişi 12 · yer 12 · nesne 12 · olay 16 · soyut 8)
  tam dörtte biri üretildi (3·3·3·4·2). **C16–C60 için kalan:** kişi 9 · yer 9 · nesne 9 ·
  olay 12 · soyut 6 — her oturumda yine 3·3·3·4·2 yapılırsa kota sonda tutar.
- **Part 1 havuzuyla çakışma bilinçli olarak önlendi.** 20 part 1 konusundan hiçbiri kart
  konusu olarak alınmadı: fotoğraf yerine "sık giyilen bir giysi", sanat/el işi yerine
  "birine verilen hediye", komşuluk yerine "tanınmayan birine yardım", zaman yönetimi
  yerine "planların son anda değişmesi", seyahat yerine "gidilen kalabalık bir yer"
  kuruldu. Denetim scripti 200 part 1 sorusunun tamamıyla metin karşılaştırması yaptı —
  **hiçbir soru metni çakışmıyor.**
- **Şema kararı — `part` alanı yazılmadı.** `tools/dogrula.py` içindeki
  `konusma_yazma_denetle()` dosyayı `skill == "speaking" and part == 1` ise part 1,
  **değilse part2-3** sayıyor. Dosyaya `"part": 2` gibi bir alan konsaydı sorun çıkmazdı
  ama prompt şemasında da yok; denetim scripti `part` alanının **bulunmadığını** ayrıca
  doğruluyor. Sonraki part2-3 oturumları da bu alanı yazmasın.
- **Kart biçimi** resmi kalıba uyuyor: başlık `Describe …` ile başlıyor ve tek cümle,
  tam **3 madde** (hepsi küçük harfle başlıyor, noktasız), son satır `and explain …`,
  `preparation_seconds: 60`, `speaking_seconds: [90, 120]`, **2 takip sorusu**
  (`follow_up`), 4 `useful_language` ifadesi.
- **3. bölüm kuralı — artan soyutluk.** Her dosyada üç soru sırasıyla
  **genel açıklama → karşılaştırma → gelecek/görüş (ya da öneri)** eksenine oturuyor,
  zorluk düzeni `medium · medium · hard`. Sorular kişisel değil toplumsal: script her
  part 3 sorusunda `your`/`yourself` geçişini hata sayıyor (45 soruda 0). Her soru tek
  cümle, tek `?`, ≤95 karakter.
- **Kültürel tarafsızlık ve ayrıcalık varsayımı yok:** hiçbir kart para, seyahat geçmişi,
  ev sahipliği ya da cihaz sahipliği gerektirmiyor — C06 kalabalık bir otobüs/pazar kadar
  bir etkinlikle de anlatılabiliyor, C07 herhangi bir giysiyle, C09 "küçük bir eşya" ile.
  Din, alkol, siyaset, savaş, cinsellik geçmiyor; gerçek marka/kurum/kişi adı yok;
  "IELTS" hiçbir dosyada geçmiyor. `useful_language` İngiliz İngilizcesinde
  (`neighbourhood`, `queueing`, `make do and mend`, `take it with a pinch of salt`).
- Doğrulama: geçici denetim scriptiyle (`tools/_sp5_kontrol.py`, sonra silindi) JSON
  geçerliliği, zarf alanları, `set_id` ↔ dosya adı eşleşmesi, `part` alanının olmaması,
  kart türü kotası, başlık kalıbı (`Describe …` + tek cümle), madde sayısı (tam 3) ve
  biçimi, `closing`in `and explain ` ile başlaması, süre alanları, `follow_up` sayısı ve
  tek soru cümlesi olması, `useful_language` sayısı (3–5) ve dosya içi tekrar, part 3
  soru sayısı/numara sırası/tek cümle/uzunluk/kişisellik/zorluk düzeni, `focus` ve
  `topic_tr` alanlarının Türkçe olması, Amerikan yazımı taraması, **15 dosyadaki bütün
  soru ve takip sorusu metinlerinin benzersizliği**, kart başlıklarının benzersizliği ve
  **200 part 1 sorusuyla çakışma** denetlendi. **İlk turda 1 hata çıktı ve düzeltildi:**
  C07 ile C08'in ikinci takip sorusu aynıydı (`Would you choose the same thing again?`) →
  C08'inki `Would you rather choose a gift yourself or be told what someone wants?` olarak
  yeniden yazıldı. Sonra **hata 0**. Ardından `python tools/dogrula.py`: **şema hatası 0**,
  `speaking/part1` 200 + `speaking/part2-3` **60**, pasaj lisansı eksik 0, görünür metinde
  IELTS 0, yasak kaynak 0. Rapordaki "TAM TEST BUTUNLUGU … EKSIK" satırları bu paketle
  ilgisiz (henüz üretilmemiş okuma/dinleme soru tipleri).
- ⚠️ **`tools/calistir.py` düzeltildi (1. oturumda not düşülen sayaç hatası).**
  `_soru_say()` yalnızca üst düzey `items`/`groups` listesini sayıyordu; part2-3
  dosyalarında sorular `part2`/`part3` altında olduğu için 15 dosya **0 birim** sayılıyor
  ve DURUM.txt'teki "Konusma sorusu" satırı olduğundan az gösterecekti. `skill == speaking`
  ve `part2` dolu olan dosyalar için `1 + len(part3.items)` sayan bir dal eklendi
  (dogrula.py'deki sayım kuralının aynısı). Kontrol: `Konusma sorusu` artık **260/440**
  (200 part 1 + 60 part2-3). Bu fonksiyon runner'ın "iş yapıldı mı" izinde de kullanılıyor;
  değişiklik sayıyı bir kez yukarı çektiği için ilerleme tespitini bozmuyor.
- Referans: `referans/ielts-speaking-sample-tasks-2023.pdf` bu oturumda **2. ve 3. bölüm
  sayfaları için tekrar `Read` ile açıldı** (4. oturum notundaki öneri): kart çerçevesi,
  `You should say:` girintisi, üç maddelik düzen, `and explain …` kapanışı, "rounding off
  questions" iki soru, 3. bölümde konudan soyutlanmış genel sorular. **Tek bir soru, cümle
  ya da replik kopyalanmadı** — örnekteki kart konusu ("sahip olunan önemli bir eşya") bu
  oturumda bilinçli olarak kullanılmadı, nesne kartları farklı eksenlerde kuruldu.
  `referans/text/` klasörü hâlâ yok.
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (4. oturumdaki gerekçe geçerli; sayaç
  dosyalarını `tools/calistir.py` kendi commit'iyle yazıyor).
- Atlanan/sorun: yok. **OPUS5-30'da 16 paketten 5'i tamam (260/550 birim).** Sıradaki iş
  **B paketi, oturum 2** — `content/speaking/part2-3/` altına `C16`–`C30`: 15 kart
  (kişi 3 · yer 3 · nesne 3 · olay 4 · soyut 2) + kart başına 3 tartışma sorusu = 60 birim.
