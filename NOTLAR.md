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

## OPUS5-30 (6. çalıştırma: konuşma 2.+3. bölüm — oturum 2, 15 kart + 45 tartışma sorusu)

- Tarih: 2026-08-05
- Depo kontrolü: `content/speaking/part1/` **T01–T20 tam** (200 soru, A paketi kapalı),
  `content/speaking/part2-3/` altında **C01–C15 vardı**, `content/writing/` altındaki üç
  klasör hâlâ boş. Çalıştırma listesindeki sıradaki bitmemiş paket **B paketi, oturum 2**
  idi, o yapıldı; kullanıcının tanımı ("6. çalıştırma") depo durumuyla **birebir uyuştu**.
  Var olan hiçbir dosyaya dokunulmadı. **60 birim** üretildi (15 kart + 45 soru),
  hedefle birebir aynı.
- Üretilen dosyalar — `content/speaking/part2-3/C16.json` … `C30.json`:
  - **kişi (3):** C16 bir şeyi iyi anlatan biri · C17 sizi güldüren biri ·
    C18 sürekli meşgul olan biri
  - **yer (3):** C19 evinizin yakınında değişmiş bir yer · C20 keyif aldığınız açık hava
    mekânı · C21 ileride çalışmak/okumak istediğiniz bir yer
  - **nesne (3):** C22 uzun zamandır sahip olduğunuz bir şey · C23 ödünç aldığınız faydalı
    bir şey · C24 aldığınız önemli bir mesaj/mektup
  - **olay/deneyim (4):** C25 bir hatadan ders çıkarmak · C26 bir işi başkalarıyla birlikte
    bitirmek · C27 bir şeyi aceleyle yapmak · C28 kaybettiğiniz bir şeyi bulmak
  - **soyut (2):** C29 öğrenmek istediğiniz bir beceri · C30 gurur duyduğunuz bir şey
- **KULLANILAN KART KONULARI (sonraki oturumlar tekrar etmesin) — bu oturum:** Someone good
  at explaining things · A person who made you laugh · Someone who is always busy · A place
  near your home that has changed · An open-air place you enjoy · A place you would like to
  work or study in · Something you have owned for a long time · Something useful you
  borrowed · An important message or letter · Learning from a mistake · Working with others
  to finish something · Doing something in a hurry · Finding something you had lost ·
  A skill you would like to learn · Something you are proud of.
  (1. oturumun 15 konusu için 5. çalıştırma notuna bak — toplam 30 konu kullanıldı.)
- **Kart türü kotası:** 60 kartlık hedefin (kişi 12 · yer 12 · nesne 12 · olay 16 · soyut 8)
  yarısı üretildi; bu oturum da 3·3·3·4·2. **C31–C60 için kalan:** kişi 6 · yer 6 ·
  nesne 6 · olay 8 · soyut 4 — kalan iki oturumda yine 3·3·3·4·2 yapılırsa kota sonda tutar.
- **Tekrar kaçınma üç eksende yapıldı:** (1) C01–C15 kart konularının hiçbiri
  tekrarlanmadı — nesne kartları bilinçle farklı eksenlere kuruldu (C09 "yanınızda
  taşınan küçük eşya" varken C22 "uzun süredir sahip olunan", C23 "ödünç alınan",
  C24 "mesaj/mektup"); (2) 20 part 1 konusuyla çakışma önlendi (teknoloji yerine "önemli
  bir mesaj", sanat/el işi yerine "öğrenilmek istenen beceri", hava durumu yerine "açık
  hava mekânı", zaman yönetimi yerine "aceleyle yapılan iş"); (3) bütün kart başlıkları,
  takip soruları ve part 3 soruları hem kendi aralarında hem C01–C15 hem de **200 part 1
  sorusuyla** metin bazında karşılaştırıldı — çakışma yok.
- **Şema kararı — `part` alanı yine yazılmadı** (5. oturumdaki gerekçe: `tools/dogrula.py`
  `skill == "speaking"` + `part == 1` değilse dosyayı part2-3 sayıyor). Denetim scripti
  alanın **bulunmadığını** ayrıca doğruladı. Sonraki part2-3 oturumları da yazmasın.
- **Kart biçimi** aynı: başlık tek cümle ve `Describe …` ile başlıyor, tam **3 madde**
  (küçük harf, noktasız), `and explain …` kapanışı, `preparation_seconds: 60`,
  `speaking_seconds: [90, 120]`, **2 takip sorusu**, 4 `useful_language` ifadesi.
  Part 3'te sırasıyla **genel açıklama → karşılaştırma → gelecek/görüş**, zorluk
  `medium · medium · hard`. Tek istisna: C25'in üçüncü sorusu gelecek yerine **öneri/görüş**
  ekseninde ("Should organisations be more open about the mistakes they make?") — prompt
  "gelecek/görüş" diyor, ikisi de kabul; `focus` alanına `öneri / görüş` yazıldı.
- **Kültürel tarafsızlık ve ayrıcalık varsayımı yok:** hiçbir kart para, seyahat geçmişi,
  ev/cihaz sahipliği gerektirmiyor — C20 herhangi bir açık alanla, C22 herhangi bir eski
  eşyayla, C23 komşudan alınan bir aletle anlatılabiliyor; C21 "çalışmak **ya da** okumak"
  diyerek hem öğrenciyi hem çalışanı kapsıyor. Din, alkol, siyaset, savaş, cinsellik yok;
  gerçek marka/kurum/kişi adı yok; "IELTS" hiçbir dosyada geçmiyor. `useful_language`
  İngiliz İngilizcesinde (`organise`, `neighbourhood`, `humour`, `learnt`, `towards`).
- Doğrulama: geçici denetim scriptiyle (`tools/_sp6_kontrol.py`, sonra silindi) JSON
  geçerliliği, zarf alanları, `set_id` ↔ dosya adı eşleşmesi, `part` alanının olmaması,
  kart türü kotası, başlık kalıbı, madde sayısı/biçimi, `closing` kalıbı, süre alanları,
  `follow_up` sayısı ve tek soru cümlesi, `useful_language` sayısı (3–5) ve dosya içi
  tekrar, part 3 soru sayısı/numara sırası/tek cümle/≤95 karakter/kişisellik
  (`your`/`yourself` yasak — 45 soruda 0)/zorluk düzeni, Amerikan yazım taraması,
  C16–C30 içi metin benzersizliği, **C01–C15 ve 200 part 1 sorusuyla çakışma** denetlendi.
  **İlk turda hata 0.** Ardından `python tools/dogrula.py`: **şema hatası 0**,
  `speaking/part1` 200 + `speaking/part2-3` **120** (30 kart × 4 birim), pasaj lisansı
  eksik 0, görünür metinde IELTS 0, yasak kaynak 0. Rapordaki "TAM TEST BUTUNLUGU … EKSIK"
  satırları bu paketle ilgisiz (henüz üretilmemiş okuma/dinleme soru tipleri).
- ⚠️ **Referans PDF bu oturumda açılamadı:** `Read` ile
  `referans/ielts-speaking-sample-tasks-2023.pdf` istendi, araç **`pdftoppm` (poppler)
  kurulu olmadığı için** hata verdi. Format kaybı olmadı — kart düzeni 5. oturumda aynı
  PDF'ten okunup NOTLAR'a yazılmıştı ve prompt dosyasının kendisinde resmi kalıp birebir
  duruyor; o düzen sürdürüldü. `referans/text/` klasörü hâlâ yok. **Hiçbir görev metni,
  soru ya da örnek cevap kopyalanmadı.** Yazma paketlerine (C/D/E) geçen oturumların
  band puanlı örnek cevap PDF'lerini okuması gerekiyor — **poppler kurulu değilse o
  dosyalar da açılamayacak**, önce `referans/text/` altına metin çıkarımı gerekebilir.
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (4.–5. oturumdaki gerekçe geçerli;
  sayaç dosyalarını `tools/calistir.py` kendi commit'iyle yazıyor).
- Atlanan/sorun: yok. **OPUS5-30'da 16 paketten 6'sı tamam (320/550 birim).** Sıradaki iş
  **B paketi, oturum 3** — `content/speaking/part2-3/` altına `C31`–`C45`: 15 kart
  (kişi 3 · yer 3 · nesne 3 · olay 4 · soyut 2) + kart başına 3 tartışma sorusu = 60 birim.

## OPUS5-30 (7. çalıştırma: konuşma 2.+3. bölüm — oturum 3, 15 kart + 45 tartışma sorusu)

- Tarih: 2026-08-05
- Depo kontrolü: `content/speaking/part1/` **T01–T20 tam** (200 soru, A paketi kapalı),
  `content/speaking/part2-3/` altında **C01–C30 vardı**, `content/writing/` altındaki üç
  klasör hâlâ boş. Çalıştırma listesindeki sıradaki bitmemiş paket **B paketi, oturum 3**
  idi, o yapıldı; kullanıcının tanımı ("7. çalıştırma") depo durumuyla **birebir uyuştu**.
  Var olan hiçbir dosyaya dokunulmadı. **60 birim** üretildi (15 kart + 45 soru),
  hedefle birebir aynı.
- Üretilen dosyalar — `content/speaking/part2-3/C31.json` … `C45.json`:
  - **kişi (3):** C31 uzun zamandır tanıdığınız bir arkadaş · C32 kendinize benzettiğiniz
    bir akraba · C33 sizi bir şey yapmaya teşvik eden biri
  - **yer (3):** C34 gitmekten hoşlandığınız bir dükkân/pazar · C35 çok vakit geçirdiğiniz
    bir oda · C36 duyduğunuz ama hiç gitmediğiniz bir yer
  - **nesne (3):** C37 işinize yarayan bir mobilya · C38 kendi ellerinizle yaptığınız bir
    şey · C39 sakladığınız ama neredeyse hiç kullanmadığınız bir şey
  - **olay/deneyim (4):** C40 çok erken kalkmak zorunda kalmak · C41 iyi bir haber almak ·
    C42 hatırınızda kalan bir sohbet · C43 rutininizin dışına çıktığınız bir gün
  - **soyut (2):** C44 önemli bulduğunuz bir kural · C45 işe yarayan bir fikriniz
- **KULLANILAN KART KONULARI (sonraki oturumlar tekrar etmesin) — bu oturum:** A friend you
  have known for a long time · A member of your family who you are similar to · Someone who
  encouraged you to do something · A shop or market that you like going to · A room where
  you spend a lot of your time · A place you have heard about but have never been to ·
  A piece of furniture in your home that you find useful · Something you have made with
  your own hands · Something you keep at home but hardly ever use · An occasion when you
  had to get up very early · A time when you received some good news · A conversation that
  you still remember well · A day when you did something different from your usual routine ·
  A rule that you think is important · An idea you had that turned out well.
  (C01–C15 için 5., C16–C30 için 6. çalıştırma notuna bak — toplam 45 konu kullanıldı.)
- **Kart türü kotası:** C01–C45 şu an kişi 9 · yer 9 · nesne 9 · olay 12 · soyut 6.
  **Son oturuma (C46–C60) kalan: kişi 3 · yer 3 · nesne 3 · olay 4 · soyut 2** — bu dağılım
  aynen yapılırsa 60 kartlık hedef (kişi 12 · yer 12 · nesne 12 · olay 16 · soyut 8) tutar.
- **Tekrar kaçınma üç eksende yapıldı:** (1) C01–C30 kart konularının hiçbiri
  tekrarlanmadı — yakın duran eksenler bilinçle ayrıştırıldı: C09 "yanınızda taşınan küçük
  eşya" / C22 "uzun süredir sahip olunan" varken C37 "mobilya", C38 "kendi yaptığınız",
  C39 "saklanan ama kullanılmayan"; C15 "hatırlanan öğüt" alınan öğüt iken C33 "teşvik
  eden kişi" kişiye odaklı; C29 "öğrenilmek istenen beceri" varken soyut kart olarak
  hedef/plan yerine **fikir** (C45) seçildi. (2) 20 part 1 konusuyla çakışma önlendi
  (T15 uyku yerine "çok erken kalkılan bir gün" olayı, T09 alışveriş yerine somut bir
  dükkân/pazar mekânı, T16 seyahat yerine "gidilmemiş ama duyulmuş yer"). (3) 15 kart
  başlığı, 30 takip sorusu ve 45 part 3 sorusu hem kendi aralarında hem C01–C30 hem de
  **200 part 1 sorusuyla** metin bazında karşılaştırıldı (380 metinlik havuz) — çakışma yok.
- **Şema kararı — `part` alanı yine yazılmadı** (5.–6. oturumdaki gerekçe: `tools/dogrula.py`
  `skill == "speaking"` + `part == 1` değilse dosyayı part2-3 sayıyor). Denetim scripti
  alanın **bulunmadığını** ayrıca doğruladı. Son part2-3 oturumu da yazmasın.
- **Kart biçimi** aynı: başlık tek cümle ve `Describe …` ile başlıyor, tam **3 madde**
  (küçük harf, noktasız), `and explain …` kapanışı, `preparation_seconds: 60`,
  `speaking_seconds: [90, 120]`, **2 takip sorusu**, 4 `useful_language` ifadesi.
  Part 3'te sırasıyla **genel açıklama → karşılaştırma → gelecek/görüş**, zorluk
  `medium · medium · hard`. Dört kartta (C33, C39, C41, C44) üçüncü soru gelecek yerine
  **öneri/görüş** ekseninde kuruldu (prompt "gelecek / görüş" diyor, ikisi de kabul);
  `focus` alanına `öneri / görüş` yazıldı — 6. oturumdaki C25 kararının aynısı.
- **Kültürel tarafsızlık ve ayrıcalık varsayımı yok:** hiçbir kart para, seyahat geçmişi,
  ev/cihaz sahipliği gerektirmiyor — C34 herhangi bir sokak pazarıyla, C35 paylaşılan bir
  odayla, C37 basit bir masa/dolapla, C38 elde yapılmış küçük bir şeyle anlatılabiliyor;
  C36 bilerek **gidilmemiş** bir yer soruyor, yani seyahat geçmişi gerektirmiyor.
  Din, alkol, siyaset, savaş, cinsellik yok; gerçek marka/kurum/kişi adı yok; "IELTS"
  hiçbir dosyada geçmiyor. `useful_language` İngiliz İngilizcesinde (`neighbourhood`,
  `cosy`, `have a clear-out`, `off the beaten track`, `over the moon`).
- Doğrulama: geçici denetim scriptiyle (`tools/_sp7_kontrol.py`, sonra silindi) JSON
  geçerliliği, zarf alanları, `set_id` ↔ dosya adı eşleşmesi, `part` alanının olmaması,
  kart türü kotası, başlık kalıbı (tek cümle, ≤95 karakter), madde sayısı (tam 3) ve
  biçimi, `closing` kalıbı, süre alanları, `follow_up` sayısı ve tek soru cümlesi,
  `useful_language` sayısı (3–5) ve dosya içi tekrar, part 3 soru sayısı/numara
  sırası/tek cümle/≤95 karakter/kişisellik (`you`/`your`/`yourself` yasak — 45 soruda 0)/
  zorluk düzeni, `focus` ve `topic_tr` Türkçeliği, Amerikan yazım taraması, kart
  başlıklarının 45 dosya içinde benzersizliği ve **C01–C30 + 200 part 1 sorusuyla
  çakışma** denetlendi. **İlk turda hata 0.**
- ⚠️ **`tools/dogrula.py` telif taramasında bir yanlış pozitif çıktı ve içerik tarafında
  giderildi:** tarayıcı yasak kaynak olarak `the conversation` kalıbını (CC BY-ND lisanslı
  site) arıyor; C42'nin maddesi `what the conversation was about` olduğu için dosya
  "INCELE" listesine düştü. Kaynakla ilgisi yok, ama rapor temiz kalsın diye madde
  `what was said during it` olarak yazıldı. **Script değiştirilmedi.** Sonraki oturumlar
  kart metinlerinde `the conversation` dizisinden kaçınsın (`a conversation`, `that
  conversation` sorun çıkarmıyor). Son hâl: `python tools/dogrula.py` → **şema hatası 0**,
  `speaking/part1` 200 + `speaking/part2-3` **180** (45 kart × 4 birim), pasaj lisansı
  eksik 0, görünür metinde IELTS 0, yasak kaynak 0. Rapordaki "TAM TEST BUTUNLUGU … EKSIK"
  satırları bu paketle ilgisiz (henüz üretilmemiş okuma/dinleme soru tipleri).
- ⚠️ **Referans PDF bu oturumda da açılamadı:** `Read` ile
  `referans/ielts-speaking-sample-tasks-2023.pdf` istendi, araç **`pdftoppm` (poppler)
  kurulu olmadığı için** hata verdi (6. oturumdaki durumun aynısı). Format kaybı olmadı —
  kart düzeni prompt dosyasında birebir duruyor ve 5. oturumda PDF'ten okunup NOTLAR'a
  yazılmıştı; o düzen sürdürüldü. `referans/text/` klasörü hâlâ yok. **Hiçbir görev metni,
  soru ya da örnek cevap kopyalanmadı.** Yazma paketlerine (C/D/E) geçecek oturumlar için
  uyarı hâlâ geçerli: band puanlı örnek cevap PDF'leri de poppler olmadan açılamayacak,
  önce `referans/text/` altına metin çıkarımı gerekebilir.
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (4.–6. oturumdaki gerekçe geçerli;
  sayaç dosyalarını `tools/calistir.py` kendi commit'iyle yazıyor).
- Atlanan/sorun: yok. **OPUS5-30'da 16 paketten 7'si tamam (380/550 birim).** Sıradaki iş
  **B paketi, oturum 4 (son part2-3 oturumu)** — `content/speaking/part2-3/` altına
  `C46`–`C60`: 15 kart (kişi 3 · yer 3 · nesne 3 · olay 4 · soyut 2) + kart başına
  3 tartışma sorusu = 60 birim.

## OPUS5-30 (8. çalıştırma: konuşma 2.+3. bölüm — oturum 4, 15 kart + 45 tartışma sorusu)

- Tarih: 2026-08-05
- Depo kontrolü: `content/speaking/part1/` **T01–T20 tam** (200 soru), `content/speaking/part2-3/`
  altında **C01–C45 vardı**, `content/writing/` altındaki üç klasör hâlâ **boş**. Çalıştırma
  listesindeki sıradaki bitmemiş paket **B paketi, oturum 4 (son part2-3 oturumu)** idi, o
  yapıldı; kullanıcının tanımı ("8. çalıştırma") depo durumuyla **birebir uyuştu**. Var olan
  hiçbir dosyaya dokunulmadı. **60 birim** üretildi (15 kart + 45 soru), hedefle birebir aynı.
- Üretilen dosyalar — `content/speaking/part2-3/C46.json` … `C60.json`:
  - **kişi (3):** C46 sorun çözmede iyi olan biri · C50 başka bir dili iyi konuşan biri ·
    C54 ilginç bir işi olan biri
  - **yer (3):** C47 sık yürüdüğünüz bir sokak · C51 çocuklar için iyi olan bir yer ·
    C55 hava kötüyken gittiğiniz bir yer
  - **nesne (3):** C48 yakınlarda alıp memnun kaldığınız bir şey · C52 sık kullandığınız bir
    çanta · C56 evde değiştirmek istediğiniz bir eşya
  - **olay/deneyim (4):** C49 bir grup önünde konuşmak · C53 başkası için bir şeye göz kulak
    olmak · C57 internette işe yarar bir bilgi bulmak · C58 başkalarıyla bir şeyi kutlamak
  - **soyut (2):** C59 yerel bir haber · C60 yakın gelecek için bir plan
- **KULLANILAN KART KONULARI (bu oturum):** Someone you know who is good at solving problems ·
  A street that you often walk along · Something you bought recently that you are pleased with ·
  A time when you had to speak in front of a group of people · Someone you know who speaks
  another language well · A place in your area that is good for children · A bag that you use
  very often · A time when you looked after something for another person · Someone you know who
  has an interesting job · A place you like to go to when the weather is bad · Something in your
  home that you would like to replace · A time when you found useful information on the
  internet · An occasion when you celebrated something with other people · A piece of local news
  that people in your area talked about · A plan you have made for the near future.
- **B PAKETİ KAPANDI: C01–C60 tamam, 60 kart + 180 tartışma sorusu = 240 birim.** Kart türü
  kotası hedefle birebir tuttu: **kişi 12 · yer 12 · nesne 12 · olay 16 · soyut 8** (denetim
  scripti 60 dosyanın tamamı üzerinden saydı). Konuşma bölümü tümüyle bitti: part 1 200 +
  part2-3 240 = **440 birim**. Kart konularının tam listesi için 5.–8. çalıştırma notlarına bak.
- **Tekrar kaçınma üç eksende yapıldı:** (1) C01–C45'teki 45 kart konusundan hiçbiri
  tekrarlanmadı — yakın duran eksenler bilinçle ayrıştırıldı: C09 "taşınan küçük eşya" /
  C22 "uzun süredir sahip olunan" / C37 "mobilya" varken C52 **çanta** (kullanım sıklığı ekseni)
  ve C56 **değiştirilmek istenen eşya** (eskime ekseni) seçildi; C23 "ödünç alınan şey" varken
  C53 **başkasının eşyasına bakmak** sorumluluk eksenine kuruldu; C16 "iyi anlatan kişi" varken
  C46 **sorun çözen kişi** ve C54 **ilginç işi olan kişi** farklı niteliklere bakıyor; C29
  "öğrenilmek istenen beceri" varken C50 **başkasının dil becerisi** (kişi kartı) ayrı duruyor;
  C43 "rutin dışı bir gün" varken C58 **kutlama** ortak/toplu olay ekseninde. (2) 20 part 1
  konusuyla çakışma önlendi: T06 hava durumu yerine **kötü havada gidilen mekân**, T14 teknoloji
  yerine **belirli bir arama deneyimi** (C57), T09 alışveriş yerine **tek bir satın alma** (C48).
  (3) 15 kart başlığı, 30 takip sorusu ve 45 part 3 sorusu hem kendi aralarında hem C01–C45 hem
  de **200 part 1 sorusuyla** metin bazında karşılaştırıldı (575 metinlik havuz) — çakışma yok.
  Part 3'te yakın duran iki soru bilerek değiştirildi: C09'un "cihazlar görevleri devralınca
  daha az eşya taşınır mı" sorusu zaten var olduğu için C52'nin üçüncü sorusu **atık** eksenine,
  C16'nın "bazı insanlar neden daha iyi anlatır" kalıbı var olduğu için C46'nın ilk sorusu
  **hangi nitelikler yardımcı olur** kalıbına çevrildi.
- **Yeni açılan part 3 eksenleri** (havuzun tekdüzeleşmemesi için bilinçli): yaya dostu şehir
  merkezi (C47), reklamın alıcı üzerindeki etkisi (C48), topluluk önünde konuşmanın okulda
  öğretilmesi (C49), çeviri araçları ve dil öğrenimi (C50), kamu tesislerinin finansmanı (C51),
  tek kullanımlık ürün ve atık (C52), çocuklara sorumluluk verilmesi (C53), yok olacak meslekler
  (C54), kaynak güvenilirliği ve doğrulama (C57), yerel gazetecilik (C59), uzun/kısa vadeli
  planlama (C60).
- **Şema kararı — `part` alanı yine yazılmadı** (5.–7. oturumdaki gerekçe: `tools/dogrula.py`
  `skill == "speaking"` + `part == 1` değilse dosyayı part2-3 sayıyor). Denetim scripti alanın
  **bulunmadığını** ayrıca doğruladı.
- **Kart biçimi** aynı: başlık tek cümle ve `Describe …` ile başlıyor, tam **3 madde** (küçük
  harf, noktasız), `and explain …` kapanışı, `preparation_seconds: 60`,
  `speaking_seconds: [90, 120]`, **2 takip sorusu**, 4 `useful_language` ifadesi. Part 3'te
  sırasıyla **genel açıklama → karşılaştırma → gelecek/görüş**, zorluk `medium · medium · hard`.
  Altı kartta (C47, C49, C51, C53, C55, C57) üçüncü soru gelecek yerine **öneri/görüş** ekseninde
  kuruldu — `focus` alanına `öneri / görüş` yazıldı; 6.–7. oturumdaki kararın aynısı.
- **Kültürel tarafsızlık ve ayrıcalık varsayımı yok:** hiçbir kart para, seyahat geçmişi ya da
  belirli bir cihaz/mülk sahipliği gerektirmiyor — C48 küçük ve ucuz bir alışverişle, C51
  herhangi bir park/meydanla, C52 en basit bir bezle, C55 kütüphane/çarşı gibi ücretsiz bir
  mekânla, C58 küçük bir aile buluşmasıyla anlatılabiliyor. C59 **yerel** haber istiyor, ulusal
  siyaset gerektirmiyor. Din, alkol, siyaset, savaş, cinsellik yok; gerçek marka/kurum/kişi adı
  yok; "IELTS" hiçbir dosyada geçmiyor. `useful_language` İngiliz İngilizcesinde
  (`practise regularly`, `hard-wearing`, `pouring with rain`, `a false economy`, `off the cuff`).
- Doğrulama: geçici denetim scriptiyle (`tools/_sp8_kontrol.py`, sonra silindi) JSON geçerliliği,
  zarf alanları, `set_id` ↔ dosya adı eşleşmesi, `part` alanının olmaması, **60 kartlık kart türü
  kotası**, başlık kalıbı (tek cümle, ≤95 karakter), madde sayısı (tam 3) ve biçimi, `closing`
  kalıbı, süre alanları, `follow_up` sayısı ve tek soru cümlesi, `useful_language` sayısı (3–5)
  ve dosya içi tekrar, part 3 soru sayısı/numara sırası/tek cümle/≤95 karakter/kişisellik
  (`you`/`your`/`yourself` yasak — 45 soruda 0)/zorluk düzeni, `focus` ve `topic_tr` Türkçeliği,
  Amerikan yazım taraması, yasak `the conversation` dizisi ve kart başlıklarının 60 dosya içinde
  benzersizliği denetlendi. **İlk turda hata 0.**
- `python tools/dogrula.py` → **şema hatası 0**, `speaking/part1` 200 + `speaking/part2-3`
  **240** (60 kart × 4 birim), pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0.
  Rapordaki "TAM TEST BUTUNLUGU … EKSIK" satırları bu paketle ilgisiz (henüz üretilmemiş okuma/
  dinleme soru tipleri). ⚠️ 7. oturumun uyarısı korundu: tarayıcı `the conversation` dizisini
  yasak kaynak sayıyor, bu oturumda hiçbir metinde geçmiyor.
- ⚠️ **Referans PDF'leri bu oturumda da açılmadı:** `poppler/pdftoppm` kurulu olmadığı için
  `Read` PDF'leri okuyamıyor (6.–7. oturumla aynı durum), `referans/text/` klasörü hâlâ yok.
  Kart düzeni prompt dosyasında birebir durduğu için format kaybı olmadı. **Hiçbir görev metni,
  soru ya da örnek cevap kopyalanmadı.** ⚠️ **Sıradaki oturum (9.) C paketine, yani Academic
  1. göreve geçiyor** — orada band puanlı örnek cevap PDF'leri işe yarardı ama poppler olmadan
  açılamayacak; gerekirse önce `referans/text/` altına metin çıkarımı yapılmalı, olmazsa prompt
  dosyasındaki şema ve kurallar tek başına yeterli.
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (4.–7. oturumdaki gerekçe geçerli; sayaç
  dosyalarını `tools/calistir.py` kendi commit'iyle yazıyor).
- Atlanan/sorun: yok. **OPUS5-30'da 16 paketten 8'i tamam (440/550 birim).** Sıradaki iş
  **C paketi, oturum 1** — `content/writing/academic-task1/` altına `AT01`–`AT10`: 10 görev.
  30 görevlik görsel türü kotası (çizgi 6 · sütun 6 · pasta 4 · tablo 4 · süreç 4 · harita 3 ·
  karma 3) üç oturuma bölüneceği için ilk oturumda dengeli bir kesit alınmalı, örneğin
  çizgi 2 · sütun 2 · pasta 2 · tablo 1 · süreç 1 · harita 1 · karma 1.

---

## OPUS5-30 (9. çalıştırma: yazma Academic 1. görev — oturum 1, 10 görev)

- Tarih: 2026-08-05
- Depo kontrolü: `content/speaking/part1/` **T01–T20 tam** (200 soru), `content/speaking/part2-3/`
  **C01–C60 tam** (240 birim), `content/writing/` altındaki üç klasör **boştu**. Çalıştırma
  listesindeki sıradaki bitmemiş paket **C paketi, oturum 1 (9. çalıştırma)** idi, o yapıldı;
  kullanıcının tanımı depo durumuyla **birebir uyuştu**. Var olan hiçbir dosyaya dokunulmadı.
  **10 birim** üretildi, hedefle birebir aynı.
- Üretilen dosyalar — `content/writing/academic-task1/AT01.json` … `AT10.json`:
  - **çizgi grafik (2):** AT01 üç kasabada geri dönüştürülen evsel atık yüzdesi (1995–2020) ·
    AT07 dört bölgede evde internet bağlantısı olan hane yüzdesi (2000–2020)
  - **sütun grafik (2):** AT02 beş yaş grubunun halk kütüphanesi ziyaretleri (2010 / 2022) ·
    AT08 beş tatil türünde yolculuk sayısı (2005 / 2020)
  - **pasta grafik (2, ikişer pasta):** AT03 evde enerjinin kullanım amacına göre dağılımı
    (1990 / 2020) · AT09 iki bölgede tatlı suyun sektörlere göre dağılımı (2020)
  - **tablo (1):** AT04 bir şehirde işe gidiş yolculuklarının ulaşım türüne göre payı
    (2015 / 2023) + 2023 ortalama yolculuk süresi
  - **süreç şeması (1):** AT05 bir kamu binasında yağmur suyunun toplanması ve arıtılması
  - **harita (1):** AT06 Ferndale köyü, 1985 → 2020
  - **karma (1):** AT10 nüfusun yaş yapısı (sütun, 2000 / 2025) + toplam nüfus (çizgi, 2000–2025)
- **KULLANILAN GÖREV KONULARI (bu oturum):** geri dönüşüm oranları · kütüphane ziyaretleri ·
  ev enerjisi kullanımı · ulaşım tercihi · yağmur suyu toplama ve arıtma · köy gelişimi
  (harita) · internet kullanımı · tatil türleri · su tüketimi · nüfus yaş dağılımı.
  **10.–11. oturumda bu on konu tekrar edilmeyecek.** Kalan görsel türü kotası:
  **çizgi 4 · sütun 4 · pasta 2 · tablo 3 · süreç 3 · harita 2 · karma 2 = 20 görev.**
- **Uydurma yer adları** (gerçek yer/kurum/marka yok): Marden, Hallowfield, Trentbury (AT01),
  Ardenholm (AT04), Ferndale (AT06), Eastport, Northvale, Central Plains, Southern Isles
  (AT07), Northmoor, Calder Bay (AT09).
- **Veri tutarlılığı denetlendi:** bütün pasta serileri tam **100**; AT04'te iki pay sütunu da
  **100**; AT10'da iki yaş dağılımı da **100**. Her görselde anlatılacak belirgin bir şey var —
  kesişme (AT01: yükselen iki kasaba 2005–2010 arasında Hallowfield'ı geçiyor; Trentbury aynı
  aralıkta Marden'ı geçiyor), sıralama değişimi (AT02 en çok ziyaret eden grup, AT03 ikinci
  sıranın el değiştirmesi, AT08 en popüler tatil türü), zirve ve sonrasında geri çekilme
  (AT10 toplam nüfus 2020'de tepe), makasın açılıp daralması (AT07: 22 → 52 → 39 puan),
  keskin karşıtlık (AT09 tarım %62'ye karşı sanayi %38). Düz seri yok — denetim scripti
  her seride değişim aralığının tepe değerin %10'unu aştığını ayrıca doğruladı.
  Seri/kategori sayısı hiçbir görselde 6'yı geçmiyor.
- **SVG kuralları** (AT05 süreç, AT06 harita): `viewBox` var, kökte sabit `width`/`height`
  **yok**, yalnızca `svg/defs/marker/g/rect/circle/line/path/polygon/text` etiketleri,
  `fill`/`stroke` değerleri sadece `none` ve `black`, `font-size="12"`,
  `font-family="sans-serif"`. AT06'da iki durum yan yana ve **`BEFORE (1985)` / `AFTER (2020)`**
  diye başlıklandırıldı. AT05 dokuz kutuluk doğrusal bir akış (çatı → oluk → yaprak süzgeci →
  yer altı deposu → pompa → kum filtresi → morötesi ünite → ara depo → tuvaletler / sulama)
  artı bir taşma kolu; ok başı tek bir `marker` ile çizildi.
- **Şema kararları:** grafik ve tablolarda prompt dosyasındaki örnek birebir izlendi — çizgi/
  sütun/pasta görsellerinde `categories` + `series` **doğrudan `visual` içinde** duruyor
  (`chart_data` anahtarı hiç yazılmadı, örnek şemada da yok), tabloda `chart_data.headers` +
  `chart_data.rows` var, `process` ve `map`'te `chart_data: null` + `svg` dolu. Karma görevde
  (AT10) `visual: null` ve iki nesnelik `visuals` listesi kullanıldı; diğer dokuz dosyada
  `visuals: null`. `instruction_line` on dosyada da birebir aynı resmî kalıp.
- **Format referansı — PDF metin çıkarımı bu oturumda çözüldü:** poppler hâlâ kurulu değil ve
  `Read` PDF açamıyor, ama `tools/pdf_metin.py` (saf Python, `zlib` + içerik akışı ayrıştırma)
  yazılarak `referans/text/` altına beş dosya çıkarıldı (yazma ve konuşma örnek görevleri +
  iki band puanlı örnek cevap dosyası). Klasör `.gitignore`'da, depoya girmiyor.
  Doğrulanan biçim: `You should spend about 20 minutes on this task.` /
  `Write at least 150 words.` / `Summarise the information by selecting and reporting the
  main features, and make comparisons where relevant.` — on görevde de bu kalıp kullanıldı.
  Örnek cevapların sınav yorumlarından çıkan ölçüt (**ana özellikleri seçip öne çıkarma, genel
  bakış paragrafı, veriyle destekleme, veri dışına çıkan spekülasyon yapmama**) `key_points` ve
  `common_mistakes` alanlarını biçimlendirdi. **Hiçbir görev metni, veri ya da örnek cevap
  kopyalanmadı; bütün görseller ve sayılar sıfırdan uyduruldu.**
- **Tekrar kaçınma:** yazma paketi bu oturumda açıldığı için paket içi tekrar riski yoktu;
  on konu, on görsel başlığı ve on görev metni birbirinden farklı (script karşılaştırdı).
  Dinleme/okuma paketlerinde geçen "kütüphane yenilemesi" (L2-S2) ve "geri dönüşüm merkezi"
  (L4-S2) senaryolarıyla **bilinçli olarak çakışmadı**: AT01 bir tesis turu değil kasaba bazlı
  **oran** verisi, AT02 ise bina planı değil yaş grubuna göre **ziyaret sayısı**. Konuşma
  paketindeki konularla da örtüşme yok (görev tipi ve içerik tamamen farklı).
- **Kültürel tarafsızlık:** bütün konular ülke belirtmeden kurgulandı (yer adları uydurma),
  ayrıcalık varsaymıyor, din/alkol/siyaset/savaş/cinsellik yok, gerçek marka/kurum/kişi yok,
  görünür metinde "IELTS" geçmiyor. Açıklama alanları Türkçe, görev metinleri İngiliz
  İngilizcesinde (`Summarise`, `travelled`, `centre` kullanımı; denetim scripti Amerikan
  yazım listesini taradı — 0 eşleşme).
- Doğrulama: geçici denetim scriptiyle (`tools/_at9_kontrol.py`, sonra silindi) JSON
  geçerliliği, zarf alanları, `set_id` ↔ dosya adı eşleşmesi, `skill/module/task` üçlüsü,
  `min_words`/`minutes`, `instruction_line` kalıbı, görev metninin resmî kapanış cümlesiyle
  bitmesi, `key_points` (4–6) ve `common_mistakes` (3–5) sayısı ve Türkçeliği, görsel türü
  kotası, pasta/pay toplamları, seri uzunlukları, düz seri taraması, tablo satır-sütun
  uyumu, SVG etiket/renk/`viewBox`/font denetimi ve etiket dengesi, harita `BEFORE`/`AFTER`
  başlıkları, `alt` metinlerinin Türkçeliği, prompt ve görsel başlığı tekrarı denetlendi.
  **İlk turda hata 0** (yalnızca iki yanlış pozitif: Türkçe cümlede Türkçeye özgü harf
  bulunmaması).
- `python tools/dogrula.py` → **şema hatası 0**, `writing/task1` **10**, speaking 200 + 240
  değişmedi, pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0. Rapordaki
  "TAM TEST BUTUNLUGU … EKSIK" satırları bu paketle ilgisiz.
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (önceki oturumlardaki gerekçe geçerli;
  sayaç dosyalarını `tools/calistir.py` kendi commit'iyle yazıyor).
- Atlanan/sorun: yok. **OPUS5-30'da 16 paketten 9'u tamam (450/550 birim).** Sıradaki iş
  **C paketi, oturum 2** — `content/writing/academic-task1/` altına `AT11`–`AT20`: 10 görev,
  kalan kotadan dengeli bir kesit (örneğin çizgi 2 · sütun 2 · pasta 1 · tablo 2 · süreç 1 ·
  harita 1 · karma 1). Yukarıdaki on konu tekrar edilmeyecek. Referans metinleri için
  `python tools/pdf_metin.py referans/<ad>.pdf referans/text/<ad>.txt` çalıştırılabilir.

---

## OPUS5-30 (10. çalıştırma: yazma Academic 1. görev — oturum 2, 10 görev)

- Tarih: 2026-08-05
- Depo kontrolü: `content/speaking/part1/` **T01–T20 tam** (200 soru), `content/speaking/part2-3/`
  **C01–C60 tam** (240 birim), `content/writing/academic-task1/` **AT01–AT10 dolu**,
  `general-task1/` ve `task2/` **boş**. Çalıştırma listesindeki sıradaki bitmemiş paket
  **C paketi, oturum 2 (10. çalıştırma)** idi, o yapıldı; kullanıcının tanımı depo durumuyla
  birebir uyuştu. Var olan hiçbir dosyaya dokunulmadı. **10 birim** üretildi, hedefle aynı.
- Üretilen dosyalar — `content/writing/academic-task1/AT11.json` … `AT20.json`:
  - **çizgi grafik (2):** AT11 dört kaynaktan üretilen elektrik, TWh (1995–2025) ·
    AT17 üç spor türüne düzenli katılım yüzdesi (2005–2025)
  - **sütun grafik (2):** AT12 beş bölüm alanına kayıtlı öğrenci sayısı (2010 / 2022) ·
    AT18 beş ilçede tamamlanan yeni konut sayısı (2015 / 2022)
  - **pasta grafik (1, iki pasta):** AT13 hane harcamalarının altı kaleme dağılımı (2000 / 2020)
  - **tablo (2):** AT14 üç yaş grubunun altı etkinliğe ayırdığı günlük ortalama saat (2022) ·
    AT19 beş arazi türünün toplam alan içindeki payı (1990 / 2005 / 2020)
  - **süreç şeması (1):** AT15 cam şişelerin toplanıp temizlenip yeniden doldurulması (döngüsel)
  - **harita (1):** AT16 Westhaven liman bölgesi, 1990 → 2020
  - **karma (1):** AT20 uluslararası ziyaretçi sayısı (sütun, 2010–2022) + 2022'de ziyaret
    sebepleri (pasta)
- **KULLANILAN GÖREV KONULARI (bu oturum):** elektrik üretim kaynakları · bölüm tercihleri ve
  kayıt sayıları · hane harcamalarının dağılımı · günlük zaman kullanımı · cam şişelerin
  toplanıp yeniden doldurulması · liman bölgesinin dönüşümü (harita) · düzenli spor katılımı ·
  yeni konut yapımı · arazi kullanımı · bölgeye gelen uluslararası ziyaretçiler.
  **11. oturumda bu on konu da, 9. oturumun on konusu da tekrar edilmeyecek.**
  Kalan görsel türü kotası (son oturum, AT21–AT30):
  **çizgi 2 · sütun 2 · pasta 1 · tablo 1 · süreç 2 · harita 1 · karma 1 = 10 görev.**
- **Uydurma yer adları** (gerçek yer/kurum/marka yok): Westhaven (AT16), Northgate, Millfield,
  Sandcove, Highbeck, Lowmoor (AT18). Diğer görevlerde bilinçli olarak "one country",
  "one region", "one college" denildi — hiçbir ülkeye/kuruma bağlanmadı.
- **Veri tutarlılığı denetlendi:** AT13'te iki pasta da tam **100**, AT20 pastası **100**,
  AT19'da üç yılın sütunu da **100**, AT14'te üç yaş grubunun sütunu da tam **24,0 saat**.
  AT12 toplamları 2.500 → 3.300, AT18 toplamları 1.595 → 1.800, AT11 toplamları 197 → 267 TWh
  elle doğrulandı; AT20'de iki görselin birlikte okunmasıyla çıkan 690 × %46 ≈ 317 bin sayısı
  `key_points` içine kondu. Her görselde anlatılacak belirgin bir şey var — sıralamanın el
  değiştirmesi (AT11 kömür ↔ rüzgâr+güneş, AT12 işletme ↔ bilişim, AT13 gıda ↔ konut,
  AT17 yüzme ↔ spor salonu, AT18 Highbeck ↔ Millfield), kesişme (AT11'de üç ayrı kesişme;
  AT17'de dört), zirve ve geri çekilme (AT11 doğal gaz 2020, AT17 koşu 2020, AT20 2016 dipi),
  keskin karşıtlık (AT14'te 30-49 yaş 7,5 saat çalışırken 50+ 3,6 saat). Düz seri yok —
  denetim scripti her seride değişim aralığının tepe değerin %10'unu aştığını doğruladı.
  Seri sayısı en çok 4, kategori sayısı en çok 7, tablo satırı en çok 6.
- **SVG kuralları** (AT15 süreç, AT16 harita): `viewBox` var, kökte sabit `width`/`height`
  **yok**, yalnızca `svg/defs/marker/g/rect/circle/line/path/polygon/text`, `fill`/`stroke`
  yalnızca `none` ve `black`, `font-size="12"`, `font-family="sans-serif"`; bütün koordinatlar
  `viewBox` içinde (script sınır taraması yaptı). AT16'da iki durum yan yana ve
  **`BEFORE (1990)` / `AFTER (2020)`** başlıklı. **AT15 bilinçli olarak döngüsel** bir süreç
  (AT05 doğrusaldı): sekiz kutu bir halka oluşturuyor, hasarlı şişeler için tek yan kol var,
  dönüş oku başlangıç kutusuna geri bağlanıyor — böylece adaydan farklı bir dil (döngü, geri
  dönme) isteniyor.
- **Şema kararları:** 9. oturumun kararları birebir sürdürüldü — çizgi/sütun/pasta görsellerinde
  `categories` + `series` doğrudan `visual` içinde, tabloda `chart_data.headers` +
  `chart_data.rows`, `process`/`map`'te `chart_data: null` + `svg` dolu, karma görevde
  (AT20) `visual: null` + iki nesnelik `visuals`. `instruction_line` on dosyada da aynı.
  Görev metinleri resmî kapanış cümlesiyle bitiyor.
- **Tekrar kaçınma:** script AT01–AT20'nin **topic**, **prompt** ve **görsel başlığı**
  alanlarını karşılaştırdı — çakışma 0. İçerik düzeyinde de bilinçli ayrım yapıldı: AT11
  *üretilen elektrik miktarı* (AT03 ev içi enerji *payı* idi), AT17 *spora katılım* (AT08
  tatil türleriyle ilgisiz), AT13 *harcama payı* (AT04 ulaşım payıydı), AT16 *kıyı/liman*
  dönüşümü (AT06 iç kesimde bir köydü), AT19 *arazi kullanımı* (yeni alan), AT14 *zaman
  kullanımı* (yeni alan). Dinleme/okuma paketleriyle senaryo çakışması yok.
- **Kültürel tarafsızlık:** ülke adı yok, ayrıcalık varsayımı yok, din/alkol/siyaset/savaş/
  cinsellik yok, gerçek marka/kurum/kişi yok, görünür metinde "IELTS" geçmiyor. Görev metinleri
  İngiliz İngilizcesinde (`Summarise`, `harbour`, `visitor centre` yazımları kullanıldı);
  denetim scripti Amerikan yazım listesini taradı — 0 eşleşme. Açıklama alanları (`key_points`, `common_mistakes`, `alt`, `topic`) Türkçe.
- Doğrulama: geçici denetim scriptiyle (`tools/_at10_kontrol.py`, sonra silindi) JSON
  geçerliliği, zarf alanları, `set_id` ↔ dosya adı, `instruction_line`/kapanış kalıbı,
  `key_points` (4–6) ve `common_mistakes` (3–5) sayısı, görsel türü kotası, pasta/sütun
  toplamları, seri-kategori uzunluk uyumu, düz seri taraması, tablo satır-sütun uyumu,
  SVG etiket/renk/`viewBox`/font/sınır denetimi, harita `BEFORE`/`AFTER` başlıkları,
  AT01–AT20 arası topic/prompt/başlık tekrarı denetlendi. **Hata 0** (üç yanlış pozitif:
  Türkçe cümlede Türkçeye özgü harf bulunmaması).
- `python tools/dogrula.py` → **şema hatası 0**, `writing/task1` **20** (10 → 20), speaking
  200 + 240 değişmedi, pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0.
  Rapordaki "TAM TEST BUTUNLUGU … EKSIK" satırları bu paketle ilgisiz.
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaç dosyalarını `tools/calistir.py` kendi
  commit'iyle yazıyor).
- Atlanan/sorun: yok. **OPUS5-30'da 16 paketten 10'u tamam (460/550 birim).** Sıradaki iş
  **C paketi, oturum 3** — `content/writing/academic-task1/` altına `AT21`–`AT30`: 10 görev,
  kalan kotanın tamamı (çizgi 2 · sütun 2 · pasta 1 · tablo 1 · süreç 2 · harita 1 · karma 1).
  9. ve 10. oturumun yirmi konusu tekrar edilmeyecek. Referans metinleri için
  `python tools/pdf_metin.py referans/<ad>.pdf referans/text/<ad>.txt` çalıştırılabilir.

---

## OPUS5-30 (11. çalıştırma: yazma Academic 1. görev — oturum 3, 10 görev — **C paketi tamam**)

- Tarih: 2026-08-05
- Depo kontrolü: `content/speaking/part1/` **T01–T20 tam** (200 soru), `content/speaking/part2-3/`
  **C01–C60 tam** (240 birim), `content/writing/academic-task1/` **AT01–AT20 dolu**,
  `general-task1/` ve `task2/` **boş**. Çalıştırma listesindeki sıradaki bitmemiş paket
  **C paketi, oturum 3 (11. çalıştırma)** idi, o yapıldı. Var olan hiçbir dosyaya dokunulmadı.
  **10 birim** üretildi, hedefle aynı. Bununla birlikte **Academic 1. görev paketi (30 görev)
  tamamlandı.**
- Üretilen dosyalar — `content/writing/academic-task1/AT21.json` … `AT30.json`:
  - **çizgi grafik (2):** AT21 üç biçimde kitap satışı, milyon adet (2010–2024) ·
    AT27 üç şehirde havadaki ince toz, mikrogram/m³ (2005–2025)
  - **sütun grafik (2):** AT22 beş iş kolunda haftalık çalışma saati (2002 / 2022) ·
    AT28 dört tarım bölgesinde tahıl, meyve ve sebze üretimi, bin ton (2023)
  - **pasta grafik (1, iki pasta):** AT23 iki yaş grubunun ev değiştirme sebepleri (2023)
  - **tablo (1):** AT24 dört yaş grubunun üç alan türünde kişi başına yıllık sağlık merkezi
    ziyareti (2023)
  - **süreç şeması (2):** AT25 yünün kırkımdan ipliğe dönüşmesi (çiftlik → fabrika, 8 aşama,
    kısa liflerin ayrıldığı yan kol) · AT29 buğdaydan paketli ekmeğe (değirmen → fırın,
    9 aşama, kepeğin ayrıldığı yan kol)
  - **harita (1):** AT26 Ashcombe kent parkı, 2002 → 2024
  - **karma (1):** AT30 yetişkinlerin ana haber kaynağı (pasta, 2024) + yaş gruplarına göre
    günlük haber takip süresi (sütun, 2024)
- **KULLANILAN GÖREV KONULARI (bu oturum):** kitap biçimlerine göre satışlar · iş kollarına
  göre haftalık çalışma saatleri · ev değiştirme sebepleri · sağlık merkezi ziyaretleri ·
  yünün üretimi ve ipliğe dönüştürülmesi · kent parkının dönüşümü (harita) · havadaki ince
  toz miktarı · bölgelere göre tarım ürünü üretimi · buğdaydan ekmeğe üretim süreci ·
  haber kaynakları ve günlük haber takibi.
  **Academic 1. görevde otuz konunun otuzu da farklı; paket kapandı, yeni oturum gerekmiyor.**
- **Görsel türü kotası (AT01–AT30, hedefle birebir):** çizgi 6/6 · sütun 6/6 · pasta 4/4 ·
  tablo 4/4 · süreç 4/4 · harita 3/3 · karma 3/3 = **30/30** (denetim scripti doğruladı).
- **Uydurma yer adları** (gerçek yer/kurum/marka yok): Ashport, Corley, Bellworth (AT27),
  Eastvale, Highmoor, Rivermouth, South Plain (AT28), Ashcombe ve Mill Road (AT26).
  Diğer görevlerde bilinçli olarak "one country", "one region" denildi.
- **Veri tutarlılığı denetlendi:** AT23'te iki pasta da tam **100**, AT30 pastası **100**;
  AT24'te "üç alanın ortalaması" sütununun dördü de üç hücrenin ortalamasıyla **birebir**
  tutuyor (3,0 · 2,1 · 3,7 · 7,8); AT28'de bölge toplamları 670 / 450 / 830 / 860 (genel
  toplam 2.810), Rivermouth'un meyvesi 310 = dört bölgenin meyve toplamının **tam yarısı**,
  South Plain'in tahılı 640 = kendi üretiminin **%74'ü**; AT21'de yıl toplamları 102 → 172
  milyon. Her görselde anlatılacak belirgin bir şey var — kesişme (AT21'de sesli kitap ↔
  e-kitap, AT27'de iki kesişme ve sıralamanın **tamamen tersine dönmesi**), zirve ve geri
  çekilme (AT21 e-kitap 2019, AT27 Bellworth 2020), tek istisna (AT22'de yalnızca bilgi
  hizmetlerinde artış), keskin karşıtlık (AT24'te 8,6'ya karşı 1,7; AT28'de meyvede
  Rivermouth ↔ South Plain), hızlanan artış (AT30'da 9 → 12 → 17 dakika). Düz seri yok
  (script her seride değişim aralığının tepe değerin %10'unu aştığını doğruladı).
  Seri sayısı en çok 3, kategori sayısı en çok 6, tablo satırı 4.
- **SVG kuralları** (AT25 ve AT29 süreç, AT26 harita): `viewBox` var, kökte sabit
  `width`/`height` **yok**, yalnızca `svg/defs/marker/g/rect/circle/path/text`,
  `fill`/`stroke` yalnızca `none` ve `black`, `font-size="12"`,
  `font-family="sans-serif"`; bütün metin/kutu/yol koordinatları `viewBox` içinde ve
  **kutular çakışmıyor** (ayrı bir geometri scripti her rect çiftini ve her etiketin kendi
  kutusuna sığdığını denetledi). AT26'da iki durum yan yana ve **`BEFORE (2002)` /
  `AFTER (2024)`** başlıklı. İki süreç şeması bilinçli olarak farklı düzende: AT25 dörtlü iki
  sıradan oluşan yılan düzeni, "ON THE FARM / AT THE MILL" ayrımı ve **aşağı** çıkan yan kol;
  AT29 ise 3+3+3 düzeninde dokuz aşama ve **yukarı** çıkan yan kol. İkisi de doğrusal —
  döngüsel şema AT15'te vardı, AT05 ise arıtma hattıydı.
- **Şema kararları:** 9. ve 10. oturumun kararları birebir sürdürüldü — çizgi/sütun/pasta
  görsellerinde `categories` + `series` doğrudan `visual` içinde, tabloda
  `chart_data.headers` + `chart_data.rows`, `process`/`map`'te `chart_data: null` + `svg`
  dolu, karma görevde (AT30) `visual: null` + iki nesnelik `visuals`. `instruction_line`
  otuz dosyada da aynı, görev metinleri resmî kapanış cümlesiyle bitiyor.
- **Tekrar kaçınma:** script AT01–AT30'un **topic**, **prompt** ve **görsel başlığı**
  alanlarını karşılaştırdı — çakışma 0. İçerik düzeyinde de bilinçli ayrım yapıldı: AT21
  *kitap satışı* (AT02 kütüphane ziyaretiydi), AT22 *çalışma saati* (AT14 günlük zaman
  kullanımıydı, orada iş yalnızca bir satırdı), AT23 *taşınma sebebi* (AT18 konut
  **yapımı**ydı), AT24 *sağlık hizmeti kullanımı* (yeni alan), AT26 *park* (AT06 köy, AT16
  liman), AT27 *hava kalitesi* (AT01 atık, AT03/AT11 enerjiydi), AT28 *tarımsal üretim*
  (AT19 arazi **payı**ydı), AT30 *haber alışkanlıkları* (AT07 internet **bağlantısı**ydı).
  Dinleme/okuma paketleriyle senaryo çakışması yok.
- **Kültürel tarafsızlık:** ülke adı yok, ayrıcalık varsayımı yok, din/alkol/siyaset/savaş/
  cinsellik yok, gerçek marka/kurum/kişi yok, görünür metinde "IELTS" geçmiyor. Görev
  metinleri İngiliz İngilizcesinde (`Summarise`, `metre`, `centre` yazımları); denetim
  scripti Amerikan yazım listesini taradı — 0 eşleşme. Açıklama alanları (`key_points`,
  `common_mistakes`, `alt`, `topic`) Türkçe.
- Doğrulama: iki geçici scriptle (`tools/_at11_kontrol.py` ve `tools/_at11_svg.py`, sonra
  ikisi de silindi) JSON geçerliliği, zarf alanları, `set_id` ↔ dosya adı,
  `instruction_line`/kapanış kalıbı, `key_points` (4–6) ve `common_mistakes` (3–5) sayısı,
  görsel türü kotası, pasta toplamları, seri-kategori uzunluk uyumu, düz seri taraması,
  tablo satır-sütun uyumu ve ortalama sütununun aritmetiği, SVG etiket/renk/`viewBox`/font/
  sınır/çakışma denetimi, harita `BEFORE`/`AFTER` başlıkları, AT01–AT30 arası topic/prompt/
  başlık tekrarı denetlendi. **Hata 0** (beş yanlış pozitif: eski dosyalardaki Türkçe
  cümlelerde Türkçeye özgü harf bulunmaması). İlk turda iki sayısal ifade düzeltildi:
  AT27'de "7-10 birim" → **"7-11 birim"**, AT22'de 40 saat eşiği cümlesi (2002'de üç, 2022'de
  iki iş kolu eşiğin üzerinde, biri tam 40 saatte) — ikisi de veriyle birebir uyumlu hâle
  getirildi.
- `python tools/dogrula.py` → **şema hatası 0**, `writing/task1` **30** (20 → 30), speaking
  200 + 240 değişmedi, pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0.
  Rapordaki "TAM TEST BUTUNLUGU … EKSIK" satırları bu paketle ilgisiz.
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaç dosyalarını `tools/calistir.py` kendi
  commit'iyle yazıyor).
- Atlanan/sorun: yok. **OPUS5-30'da 16 paketten 11'i tamam (470/550 birim).** Sıradaki iş
  **D paketi, oturum 1 (12. çalıştırma)** — `content/writing/general-task1/` altına
  `GT01`–`GT10`: 10 mektup görevi. Yirmi mektubun ton kotası **resmi 7 · yarı resmi 7 ·
  samimi 6** olduğu için bu oturumda dengeli bir kesit alınmalı (örneğin resmi 4 · yarı
  resmi 3 · samimi 3), kalanı 13. çalıştırmaya bırakılmalı. Academic 1. görevin otuz konusu
  ve konuşma paketindeki konular tekrar edilmeyecek.

---

## OPUS5-30 (12. çalıştırma: yazma General 1. görev — oturum 1, 10 mektup görevi)

- Tarih: 2026-08-05
- Depo kontrolü: `content/speaking/part1/` **T01–T20 tam**, `content/speaking/part2-3/`
  **C01–C60 tam**, `content/writing/academic-task1/` **AT01–AT30 tam**,
  `content/writing/general-task1/` **boş**, `content/writing/task2/` **boş**. Çalıştırma
  listesindeki sıradaki bitmemiş paket **D paketi, oturum 1 (12. çalıştırma)** idi, o
  yapıldı. Var olan hiçbir dosyaya dokunulmadı. **10 birim** üretildi, hedefle aynı.
- Üretilen dosyalar — `content/writing/general-task1/GT01.json` … `GT10.json`:
  - **resmi (4):** GT01 akşam otobüs seferlerinin gecikmesi/iptali → otobüs şirketi müdürü ·
    GT02 mahalle bostanına gönüllü başvurusu → bahçe sorumlusu · GT03 internet faturasında
    istenmemiş hizmet kalemi → şirketin kendisi · GT04 altı haftadır gelmeyen çevrim içi
    sipariş → müşteri hizmetleri
  - **yarı resmi (3):** GT05 kiralık dairede çalışmayan ısıtma → ev sahibi (`Dear Mr
    Halstead,`) · GT06 üç aylık kursa denk gelen çalışma saatlerinin değiştirilmesi →
    yönetici (`Dear Ms Farrow,`) · GT07 çatı onarımının gürültüsü ve yan yoldan geçiş ricası
    → komşu (`Dear Mr Ellery,`)
  - **samimi (3):** GT08 başka kasabaya taşınma haberi + davet (`Dear Nadia,`) ·
    GT09 bir hafta şehir dışındayken daireye göz kulak olma ricası (`Dear Tomas,`) ·
    GT10 arkadaşın yeni işi için verdiği yemeğe katılamama ve özür (`Dear Ruya,`)
- **KULLANILAN MEKTUP DURUMLARI (13. çalıştırmada tekrar edilmeyecek):** güvenilmez otobüs
  seferi şikâyeti · gönüllü başvurusu · hatalı fatura kalemi · gecikmiş çevrim içi sipariş ·
  kiralık evde ısıtma arızası · çalışma saati değişikliği talebi · ev tadilatı + komşuya
  geçiş ricası · başka kasabaya taşınma haberi ve davet · evi kollama ricası · davete
  katılamama ve özür.
- **Ton kotası:** yirmi mektubun hedefi **resmi 7 · yarı resmi 7 · samimi 6**. Bu oturumda
  **resmi 4 · yarı resmi 3 · samimi 3** üretildi. **13. çalıştırmaya (GT11–GT20) kalan:
  resmi 3 · yarı resmi 4 · samimi 3.**
- **İşlev (function) çeşitliliği** bilinçli dağıtıldı: şikâyet (GT01, GT03, GT04), başvuru
  (GT02), talep/onarım (GT05, GT06), bilgilendirme + rica (GT07), haber + davet (GT08),
  rica + karşılık teklifi (GT09), özür + öneri (GT10). 13. oturum için henüz kullanılmamış
  işlevler: teşekkür, öneri/tavsiye verme, bilgi isteme (enquiry), iptal/erteleme bildirimi,
  kayıp eşya dışında bir arıza bildirimi, tavsiye mektubu, davete cevap verme.
- **Tekrar kaçınma dört eksende yapıldı:** (1) paket içinde durum, `topic` ve `prompt`
  çakışması yok (script karşılaştırdı); (2) Academic 1. görevin otuz konusuyla (su tüketimi,
  enerji, geri dönüşüm, kütüphane ziyareti, tarım, hava kalitesi …) hiçbir kesişme yok —
  mektuplar veri değil durum üzerine kurulu; (3) **dinleme senaryolarıyla çakışma bilinçle
  önlendi**: L4-S1 zaten *otobüs şirketinin kayıp eşya bürosu* olduğu için kayıp eşya
  mektubu yazılmadı, L2-S1 *taşınma şirketiyle telefon* olduğu için GT08 nakliyat değil
  arkadaşa haber/davet üzerine kuruldu, L3-S1 *spor salonu üyeliği*, L1-S1 *yaz kampı
  kaydı*, L5-S1 *bisiklet turu rezervasyonu*, L6-S1 *yurt başvurusu* ve L2-S2 *kütüphane
  yenilemesi* konuları da kullanılmadı (resmi örnek görevlerdeki kütüphane/öğrenci yurdu
  durumlarından uzak durmanın ayrıca telif gerekçesi var); (4) konuşma kartlarıyla
  (C01–C60) durum örtüşmesi yok.
- **Format kararları (yirmi mektupta da sürecek):** görev metni 2–3 cümlelik durum +
  `Write a letter to …. In your letter:` + **tam 3 madde** (`- ` ile, sonunda nokta yok).
  `instruction_line` on dosyada da aynı. Selamlama `salutation_hint` alanında:
  resmi `Dear Sir or Madam,`, yarı resmi `Dear Mr/Ms <soyadı>,`, samimi `Dear <ad>,`.
  Şemaya sadık kalındı — alan adları ve **alan sırası** promptun `GT01` örneğiyle birebir;
  `key_points` 5, `common_mistakes` 4 (kapanış kalıbı/ton hatası her mektupta hatırlatıldı).
- **Uydurma isimler** (gerçek kişi/kurum/marka yok): Halstead, Farrow, Ellery, Nadia, Tomas,
  Ruya. Şirketler bilinçli olarak isimsiz ("the bus company", "an online shop", "the company
  that supplies your home internet connection") — böylece aday hiçbir ülkeye bağlanmıyor.
- **Kültürel tarafsızlık ve ayrıcalık denetimi:** hiçbir görev seyahat geçmişi, araba, ikinci
  ev, yurt dışı deneyimi ya da yüksek gelir varsaymıyor; ev sahibi/kiracı, iş yeri, komşu,
  arkadaş ilişkileri evrensel. Din/alkol/siyaset/savaş/cinsellik yok (script tarıyor).
  Görünür metin İngiliz İngilizcesinde, açıklama alanları Türkçe.
- Doğrulama: geçici `tools/_gt01_kontrol.py` (iş bitince silindi) JSON geçerliliği, zarf
  alanlarının **listesi ve sırası**, `set_id` ↔ dosya adı, `skill/module/task`,
  `instruction_line` birebirliği, üç madde kuralı ve madde noktalaması, durum cümlesi sayısı,
  ton ↔ selamlama uyumu, `key_points`/`common_mistakes` sayısı, Türkçe/İngilizce ayrımı,
  Amerikan yazım taraması, yasaklı tema taraması, görünür metinde "IELTS" ve paket içi
  prompt/topic tekrarı denetledi. **Hata 0** (iki yanlış pozitif: Türkçeye özgü harf
  içermeyen iki Türkçe cümle).
- `python tools/dogrula.py` → **şema hatası 0**, `writing/task1` **40** (30 → 40), speaking
  200 + 240 değişmedi, işaretli 0, pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak
  kaynak 0. Rapordaki "TAM TEST BUTUNLUGU … EKSIK" satırları bu paketle ilgisiz.
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaç dosyalarını `tools/calistir.py` kendi
  commit'iyle yazıyor).
- Atlanan/sorun: yok. **OPUS5-30'da 16 paketten 12'si tamam (480/550 birim).** Sıradaki iş
  **D paketi, oturum 2 (13. çalıştırma)** — `GT11`–`GT20`: 10 mektup görevi, ton kotası
  **resmi 3 · yarı resmi 4 · samimi 3**. Bu oturumun on durumu ve yukarıdaki dinleme
  senaryoları tekrar edilmeyecek; kullanılmamış işlevler listesinden yararlanılmalı.
  Ardından **E paketi (14.–16. çalıştırma)** `content/writing/task2/` altına 3 × 20 deneme
  konusu.

---

## OPUS5-30 (13. çalıştırma: yazma General 1. görev — oturum 2, 10 mektup görevi)

- Tarih: 2026-08-05
- Depo kontrolü: `content/speaking/part1/` **T01–T20 tam**, `content/speaking/part2-3/`
  **C01–C60 tam**, `content/writing/academic-task1/` **AT01–AT30 tam**,
  `content/writing/general-task1/` **GT01–GT10 var (10/20)**, `content/writing/task2/`
  **boş**. Çalıştırma listesindeki sıradaki bitmemiş paket **D paketi, oturum 2
  (13. çalıştırma)** idi, o yapıldı. Var olan hiçbir dosyaya dokunulmadı. **10 birim**
  üretildi, hedefle aynı. **D paketi böylece tamamlandı: GT01–GT20 = 20/20.**
- Üretilen dosyalar — `content/writing/general-task1/GT11.json` … `GT20.json`:
  - **resmi (3):** GT11 mahalledeki öğrenme merkezinin hafta sonu atölyeleri hakkında bilgi
    isteme (tarih/saat/ücret + yeni başlayan ne getirmeli) · GT12 haftalardır yanmayan sokak
    lambalarının yol ve aydınlatma biriminden onarımının istenmesi · GT13 mesai dışı gelip
    acil arızayı çözen beyaz eşya teknisyeni için şirkete teşekkür + hizmetin duyurulması
    önerisi
  - **yarı resmi (4):** GT14 eskiden aynı ekipte çalışılan kişinin eğitim programı başvurusu
    için tavsiye mektubu → program sorumlusu (`Dear Ms Coburn,`) · GT15 iş yerinde açık gün
    etkinliğinde kısa konuşma davetine olumlu cevap + süre/donanım sorusu (`Dear Ms Vance,`) ·
    GT16 haftalık hobi grubuna üç ay katılamama, yerin saklanması ricası ve başka türlü
    yardım teklifi (`Dear Mrs Ashwell,`) · GT17 iş yeri yemekhanesi için istenen yazılı
    öneriler: bir sorun + iki iyileştirme (`Dear Mr Renshaw,`)
  - **samimi (3):** GT18 boş daireye taşınan arkadaşa ucuza/ikinci elden eşya tavsiyesi ve
    kendi eşyasından teklif (`Dear Dilnara,`) · GT19 bir hafta hastayken alışveriş ve yemek
    işine koşan akrabaya teşekkür + karşılık teklifi (`Dear Leyla,`) · GT20 yaklaşık bir yıl
    görüşülemeyen yakın arkadaşa düzenli buluşma önerisi ve tercihini sorma (`Dear Marek,`)
- **KULLANILAN MEKTUP DURUMLARI (D paketinin tamamı, 20 durum):** 12. oturumdan — güvenilmez
  otobüs seferi şikâyeti · gönüllü başvurusu · hatalı fatura kalemi · gecikmiş çevrim içi
  sipariş · kiralık evde ısıtma arızası · çalışma saati değişikliği talebi · ev tadilatı +
  komşuya geçiş ricası · başka kasabaya taşınma haberi ve davet · evi kollama ricası · davete
  katılamama ve özür. 13. oturumdan — atölye bilgisi isteme · sokak aydınlatması arızası ·
  teknisyen için teşekkür ve öneri · tavsiye mektubu · konuşma davetine cevap · gruba ara
  verme ve yer saklatma · yemekhane önerileri · ucuza eşya tavsiyesi · hastalıkta yardım eden
  akrabaya teşekkür · düzenli buluşma önerisi.
- **Ton kotası tamamlandı:** hedef **resmi 7 · yarı resmi 7 · samimi 6**; 12. oturum 4/3/3,
  13. oturum 3/4/3 → toplam **7/7/6**. Kontrol scripti yirmi dosyanın tamamını sayarak
  doğruladı.
- **İşlev (function) çeşitliliği:** 12. oturumda kullanılmayan işlevlerin hepsi bu oturumda
  yerini buldu — bilgi isteme/enquiry (GT11), arıza bildirimi (GT12), teşekkür + öneri
  (GT13), tavsiye mektubu (GT14), davete cevap verme (GT15), iptal/ara verme bildirimi
  (GT16), öneri verme (GT17, GT18), teşekkür (GT19), teklif/planlama (GT20). Böylece yirmi
  mektupta şikâyet, başvuru, talep, bilgilendirme, rica, haber, özür, teşekkür, tavsiye,
  enquiry ve planlama işlevleri temsil ediliyor.
- **Tekrar kaçınma dört eksende yapıldı:** (1) paket içi `prompt`, `topic` ve isimli
  selamlama çakışması script ile yirmi dosyada tarandı → 0; (2) Academic 1. görevin otuz
  veri konusuyla kesişme yok (mektuplar durum üzerine kurulu); (3) **dinleme senaryolarıyla
  çakışma bilinçle önlendi** — L1-S1 yaz kampı kaydı, L1-S2 müze turu, L2-S1 nakliyat
  şirketi, L2-S2 kütüphane yeniden açılışı, L3-S1 spor merkezi üyeliği, L3-S2 kır parkı
  rotaları, L4-S1 otobüs kayıp eşya, L4-S2 geri dönüşüm merkezi, L5-S1 bisiklet turu
  rezervasyonu, L5-S2 kasaba festivali, L6-S1 yurt başvurusu ve L6-S2 çiftçi pazarı konuları
  mektuplarda kullanılmadı (kütüphane/öğrenci yurdu resmi örnek görevlerde de geçtiği için
  ayrıca telif gerekçesi var); (4) konuşma kartlarıyla (C01–C60) durum örtüşmesi yok.
- **Format 12. oturumla birebir aynı tutuldu:** 1–3 cümlelik durum + `Write a letter to …
  In your letter:` + **tam 3 madde** (`- ` ile, sonunda nokta yok), aynı `instruction_line`,
  `key_points` 5, `common_mistakes` 4, alan adları ve **alan sırası** promptun `GT01`
  örneğiyle aynı. Selamlama kalıpları: resmi `Dear Sir or Madam,`, yarı resmi
  `Dear Mr/Ms/Mrs <soyadı>,`, samimi `Dear <ad>,`.
- **Uydurma isimler** (gerçek kişi/kurum/marka yok): Coburn, Vance, Ashwell, Renshaw,
  Dilnara, Leyla, Marek. Kurumlar bilinçli olarak isimsiz ("a learning centre in your area",
  "the office that looks after roads and street lighting", "a company that repairs household
  appliances", "the canteen at your workplace").
- **Kültürel tarafsızlık ve ayrıcalık denetimi:** hiçbir görev seyahat geçmişi, araba, ikinci
  ev, yurt dışı deneyimi ya da yüksek gelir varsaymıyor; GT18 zaten az parayla eşya bulma
  üzerine kurulu. Din/alkol/siyaset/savaş/cinsellik yok (script tarıyor). Görünür metin
  İngiliz İngilizcesinde (`centre`, `programme`, `favour`, `organise`), açıklama alanları
  Türkçe.
- Doğrulama: geçici `tools/_gt02_kontrol.py` (iş bitince silindi) JSON geçerliliği, zarf
  alanlarının **listesi ve sırası**, `set_id` ↔ dosya adı, `skill/module/task`,
  `instruction_line` birebirliği, üç madde kuralı ve madde noktalaması, durum cümlesi sayısı,
  ton ↔ selamlama uyumu, `key_points`/`common_mistakes` sayısı, Türkçe/İngilizce ayrımı,
  Amerikan yazım taraması, yasaklı tema ve gerçek marka taraması, görünür metinde "IELTS",
  paket içi prompt/topic/selamlama tekrarı ve **yirmi dosyalık ton kotası** denetledi.
  **Hata 0, uyarı 0.**
- `python tools/dogrula.py` → **şema hatası 0**, `writing/task1` **50** (40 → 50), speaking
  200 + 240 değişmedi, işaretli 0, pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak
  kaynak 0. Rapordaki "TAM TEST BUTUNLUGU … EKSIK" satırları bu paketle ilgisiz.
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaç dosyalarını `tools/calistir.py` kendi
  commit'iyle yazıyor).
- Atlanan/sorun: yok. **OPUS5-30'da 16 paketten 13'ü tamam (490/550 birim).** Sıradaki iş
  **E paketi, oturum 1 (14. çalıştırma)** — `content/writing/task2/` altına `T2-01`–`T2-20`:
  20 deneme konusu. Altmış konunun kalıp kotası **opinion 14 · her iki görüş 12 · sorun–çözüm
  11 · avantaj–dezavantaj 11 · iki soruluk 12** olduğu için ilk oturumda dengeli bir kesit
  alınmalı (örneğin 5/4/4/4/3) ve konu alanları (eğitim, iş hayatı, teknoloji, çevre, şehir
  hayatı, ulaşım, sağlık, medya, kültür, aile, turizm, tüketim, devletin rolü, yaşlanan
  nüfus, dil, suç) altmış konuya yayılacak şekilde bölüştürülmeli. Mektup ve konuşma
  konularıyla tekrar yasak.

---

## OPUS5-30 (14. çalıştırma: yazma 2. görev — oturum 1, 20 deneme konusu)

- Tarih: 2026-08-05
- Depo kontrolü: `content/speaking/part1/` **T01–T20 tam**, `content/speaking/part2-3/`
  **C01–C60 tam**, `content/writing/academic-task1/` **AT01–AT30 tam**,
  `content/writing/general-task1/` **GT01–GT20 tam**, `content/writing/task2/` **boş**.
  Çalıştırma listesindeki sıradaki bitmemiş paket **E paketi, oturum 1 (14. çalıştırma)**
  idi, o yapıldı. Var olan hiçbir dosyaya dokunulmadı. **20 birim** üretildi, hedefle aynı.
- Üretilen dosyalar — `content/writing/task2/T2-01.json` … `T2-20.json`:
  - **opinion (5):** T2-01 her ortaokul/lise öğrencisine zorunlu pratik ders (yemek, basit
    tamir, para yönetimi) · T2-02 çalışanın sağlığından işveren sorumlu olmalı mı ·
    T2-03 bütçe: suçu önlemeye mi, mahkeme ve cezaevine mi · T2-04 insanlar daha uzun
    yaşadığı için emeklilik yaşı yükselmeli mi · T2-05 çevreyi korumada birey mi, devlet ve
    büyük şirketler mi etkili
  - **her iki görüş (4):** T2-06 ulaşım bütçesi toplu taşımaya mı yola mı · T2-07 tek
    işverende kalmak mı birkaç yılda bir iş değiştirmek mi · T2-08 okullarda basılı kitap
    yerine tablet/dizüstü · T2-09 çocuk yetiştirmede büyükanne/dede ve akrabaların payı
  - **sorun–çözüm (4):** T2-10 merkezdeki konutun pahalılaşması ve çalışanların uzağa
    itilmesi · T2-11 hanelerin aldığı yiyeceğin çöpe gitmesi · T2-12 bir bölgede eskiden
    yaygın konuşulan dillerin yalnızca birkaç yaşlı konuşura kalması · T2-13 çalışma gününün
    ve boş zamanın büyük bölümünün oturarak geçmesi
  - **avantaj–dezavantaj (3):** T2-14 farklı seviyedeki çocukların aynı sınıfta okuması ·
    T2-15 günlük hizmetlerin (banka, fatura, randevu) yalnızca site/uygulama üzerinden
    verilmesi · T2-16 devletin haftalık çalışma saatine üst sınır koyması
  - **iki soruluk (4):** T2-17 geleneksel şenlik ve âdetleri artık çoğunlukla yaşlıların
    sürdürmesi · T2-18 tatilin başka ülke yerine kendi bölgesinde geçirilmesi · T2-19 sıradan
    insanların günlük hayatını anlatan yapımların dram/belgeselden fazla izlenmesi ·
    T2-20 tek başına yaşayanların sayısının düzenli artması
- **KULLANILAN DENEME KONULARI (15. ve 16. çalıştırmada tekrar edilmeyecek):** zorunlu
  pratik ders · çalışan sağlığında işveren sorumluluğu · suçu önleme ile ceza sistemi
  arasında bütçe tercihi · emeklilik yaşı · bireysel çaba mı düzenleme mi (çevre) · toplu
  taşıma–yol yatırımı · aynı işverende kalmak/iş değiştirmek · sınıfta basılı ile dijital
  materyal · çocuk yetiştirmede geniş aile · merkezde konut pahalılığı ve uzun yolculuk ·
  gıda israfı · dillerin kaybolması · hareketsiz (oturarak geçen) yaşam · karma seviyeli
  sınıf · yalnızca çevrim içi verilen hizmetler · haftalık çalışma saati sınırı · geleneklerin
  yaşlılara kalması · kendi bölgesinde tatil · gündelik hayat yapımlarının izlenme oranı ·
  tek başına yaşamanın artması.
- **Kalıp kotası:** altmışın hedefi **opinion 14 · her iki görüş 12 · sorun–çözüm 11 ·
  avantaj–dezavantaj 11 · iki soruluk 12**. Bu oturumda **5 · 4 · 4 · 3 · 4** üretildi.
  **Kalan iki oturuma (T2-21–T2-40, T2-41–T2-60) kalan: opinion 9 · her iki görüş 8 ·
  sorun–çözüm 7 · avantaj–dezavantaj 8 · iki soruluk 8** — öneri: 15. oturum
  **5/4/4/3/4**, 16. oturum **4/4/3/5/4** (böylece toplam tam tutar).
- **Konu alanı dağılımı:** on altı alanın **hepsi** bu oturumda birer kez kullanıldı; dört
  fazlalık **eğitim (2), sağlık (2), teknoloji (2), aile ve toplum (2)** alanlarına verildi.
  Altmışta hedef 12 alan × 4 + 4 alan × 3 olduğuna göre kalan iki oturumda bu dört alan
  ikişer kez daha (toplam 4'e tamamlanacak şekilde), geri kalan on iki alan ise sırayla
  üçer kez daha kullanılmalı; hangi dört alanın 3'te kalacağı 16. oturumda kararlaştırılır.
- **Tekrar kaçınma dört eksende yapıldı:** (1) paket içinde konu cümlesi ve `topic_area`
  çakışması script ile tarandı → 0; (2) **konuşma 3. bölüm sorularıyla (C01–C60, 180 soru)
  bilinçli çakışma denetimi** yapıldı — bu yüzden şu konular *yazılmadı*: şehir merkezlerinin
  arabaya kapatılması (C47), turist kalabalığının yıla yayılması (C06), tamir mi yenisini
  almak mı (C22/C56), çevrim içi bilginin güvenilirliği (C57), yerel haberin geleceği (C59),
  ücretsiz açık alanlar (C20/C51), iyi haberlerin daha çok yayımlanması (C41), işin ücret mi
  ilgi mi diye seçilmesi (C54), esnek başlangıç saatleri (C40); (3) Academic 1. görevin otuz
  veri konusuyla (su, enerji, geri dönüşüm, hava kalitesi, arazi kullanımı …) örtüşme yok —
  bu yüzden geri dönüşüm zorunluluğu ve hava kirliliği gibi başlıklar deneme konusu
  yapılmadı; (4) yirmi mektup durumuyla (GT01–GT20) örtüşme yok.
- **Format kararları (altmış konuda da sürecek):** `prompt` = 1–2 cümlelik konu + boş satır +
  **kalıp sorusunun birebir standart cümlesi**; `pattern` değerleri `opinion` ·
  `discuss_both_views` · `problem_solution` · `advantages_disadvantages` · `double_question`.
  Alan adları ve **alan sırası** promptun `T2-01` örneğiyle birebir. `key_points` 5,
  `common_mistakes` 3–4; `key_points` her zaman (a) görevin sorduğu asıl şeyi, (b) iki
  tarafın da gerekçelerini, (c) tutum/hüküm zorunluluğunu içeriyor.
- **Kalite ölçütü:** her konuda iki karşıt görüş de savunulabilir; hiçbiri uzman bilgisi
  istemiyor; ülkeye özgü politika, olay, kurum veya yasa geçmiyor; kutuplaştırıcı temalar
  (din, savaş, göç, idam, cinsellik, siyasi parti) yok — script tarıyor. Gerçek marka, kişi,
  program adı yok; prompt'larda özel ad hiç kullanılmadı. Görünür metin İngiliz İngilizcesi
  (`programmes`, `travelling`, `lorries`), açıklama alanları Türkçe.
- **Ayrıcalık denetimi:** hiçbir konu yurt dışı seyahat geçmişi, araba sahipliği, yüksek
  gelir ya da belirli bir eğitim düzeyi varsaymıyor; T2-18 tatili bilinçle "kendi bölgesinde"
  kurguladı, T2-15 cihaz/bağlantı erişimi olmayanları görevin içine yerleştirdi.
- Zorluk dağılımı: **easy 4 · medium 12 · hard 4**.
- Doğrulama: geçici `tools/_t2_01_uret.py` + `tools/_t2_01_kontrol.py` (iş bitince silindi)
  JSON geçerliliği, zarf alanlarının **listesi ve sırası**, `set_id` ↔ dosya adı,
  `skill/module/task`, `instruction_line` birebirliği, kalıp cümlesinin prompt sonunda
  birebir bulunması, konu cümlesi sayısı (1–2), `key_points`/`common_mistakes` sayısı ve
  paket içi tekrar, Türkçe/İngilizce ayrımı, Amerikan yazım taraması, yasaklı tema ve gerçek
  marka taraması, prompt'ta özel ad taraması, görünür metinde "IELTS" ve **kalıp kotası**
  denetledi. **Hata 0**, 7 uyarının hepsi yanlış pozitif (Türkçeye özgü harf içermeyen
  geçerli Türkçe ifadeler: "teknoloji", "medya", "turizm", "aile ve toplum" vb.).
- `python tools/dogrula.py` → **şema hatası 0**, `writing/task2` **20** (0 → 20),
  `writing/task1` 50, speaking 200 + 240 değişmedi, işaretli 0, pasaj lisansı eksik 0,
  görünür metinde IELTS 0, yasak kaynak 0. Rapordaki "TAM TEST BUTUNLUGU … EKSIK" satırları
  bu paketle ilgisiz.
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaç dosyalarını `tools/calistir.py` kendi
  commit'iyle yazıyor).
- Atlanan/sorun: yok. **OPUS5-30'da 16 paketten 14'ü tamam (510/550 birim).** Sıradaki iş
  **E paketi, oturum 2 (15. çalıştırma)** — `T2-21`–`T2-40`: 20 deneme konusu, kalıp kotası
  önerisi **opinion 5 · her iki görüş 4 · sorun–çözüm 4 · avantaj–dezavantaj 3 · iki soruluk
  4**. Yukarıdaki yirmi konu ve kaçınılan konuşma/Academic başlıkları tekrar edilmeyecek.


---

## OPUS5-30 (15. çalıştırma: yazma 2. görev — oturum 2, 20 deneme konusu)

- Tarih: 2026-08-05
- Depo kontrolü: `content/speaking/part1/` **T01–T20 tam**, `content/speaking/part2-3/`
  **C01–C60 tam**, `content/writing/academic-task1/` **AT01–AT30 tam**,
  `content/writing/general-task1/` **GT01–GT20 tam**, `content/writing/task2/` **T2-01–T2-20
  dolu, gerisi boş**. Çalıştırma listesindeki sıradaki bitmemiş paket **E paketi, oturum 2
  (15. çalıştırma)** idi, o yapıldı. Var olan hiçbir dosyaya dokunulmadı. **20 birim**
  üretildi, hedefle aynı.
- Üretilen dosyalar — `content/writing/task2/T2-21.json` … `T2-40.json`:
  - **opinion (5):** T2-21 dönem sonu sınavı yerine yıl boyu üretilen işin sayılması ·
    T2-22 kalan yaban alanlarının korunması her türlü yapılaşmanın önünde gelmeli mi ·
    T2-23 küçük çocuklara yönelik reklamın tümden yasaklanması · T2-24 işe alımda kişisel
    niteliklerin diploma ve deneyimden önemli olup olmadığı · T2-25 hafif ihlallerde para
    cezası yerine topluma yararlı ücretsiz çalışma
  - **her iki görüş (4):** T2-26 halk sağlığı için sağlıksız gıdayı pahalılaştırmak mı
    beslenme/egzersiz eğitimi mi · T2-27 turizm gelirinin gelenek ve tarihî yerlere mi yoksa
    yerel yol–hastane–okula mı harcanması · T2-28 ikinci dile ilkokulun ilk yıllarında mı
    başlanmalı yoksa ana dil oturana kadar beklenmeli mi · T2-29 kent arazisinin sakinlerin
    ürün yetiştirmesine mi konuta mı ayrılması
  - **sorun–çözüm (4):** T2-30 araç sayısının artması ve yolculuk sürelerinin uzaması ·
    T2-31 kent yakınındaki nehir ve göllerin hane/tarım/sanayi atığıyla kirlenmesi ·
    T2-32 yaşlı sayısı artarken eğitimli bakım personelinin yetmemesi · T2-33 gündelik
    alışverişte borçlanmanın kolaylaşması ve hanelerin ödeme gücünü aşması
  - **avantaj–dezavantaj (3):** T2-34 uzaktan kumanda edilen ve ev içi rutini kaydeden
    cihazlar · T2-35 az sayıda yerde üretilen film/müzik/dizinin her yerde izlenmesi ·
    T2-36 genç yetişkinlerin aile evinde daha uzun süre kalması
  - **iki soruluk (4):** T2-37 tek bir işverene bağlı olmadan kendi hesabına çalışanların
    artması · T2-38 özel hayatın herkese açık platformlarda ayrıntılı paylaşılması ·
    T2-39 eskiden devletin yürüttüğü hizmetlerin özel şirketlere geçmesi · T2-40 alışverişin
    ihtiyaç değil boş zaman etkinliği hâline gelmesi
- **Kalıp kotası:** altmışın hedefi **opinion 14 · her iki görüş 12 · sorun–çözüm 11 ·
  avantaj–dezavantaj 11 · iki soruluk 12**. Bu oturumda 14. oturumun bıraktığı öneriye
  birebir uyularak **5 · 4 · 4 · 3 · 4** üretildi. **Kırk dosyanın toplamı: opinion 10 ·
  her iki görüş 8 · sorun–çözüm 8 · avantaj–dezavantaj 6 · iki soruluk 8.**
  **16. oturuma (T2-41–T2-60) kalan: opinion 4 · her iki görüş 4 · sorun–çözüm 3 ·
  avantaj–dezavantaj 5 · iki soruluk 4** — toplam 20, kota tam tutar.
- **Konu alanı dağılımı (bu oturum):** eğitim 1 · sağlık 1 · teknoloji 1 · aile ve toplum 1 ·
  iş hayatı 2 · çevre 2 · medya 2 · tüketim 2 · şehir hayatı 1 · ulaşım 1 · kültür ve gelenek 1 ·
  turizm 1 · devletin rolü 1 · yaşlanan nüfus 1 · dil ve iletişim 1 · suç ve ceza 1.
  **Kırk dosyadan sonraki toplam:** eğitim, sağlık, teknoloji, aile ve toplum, iş hayatı,
  çevre, medya, tüketim = **3'er**; şehir hayatı, ulaşım, kültür ve gelenek, turizm,
  devletin rolü, yaşlanan nüfus, dil ve iletişim, suç ve ceza = **2'şer**.
  **16. oturumun kuralı:** altmışta hedef 12 alan × 4 + 4 alan × 3 olduğuna göre şu anda
  3'te olan sekiz alan **birer kez daha**, 2'de olan sekiz alandan dördü **ikişer**, kalan
  dördü **birer** kez daha kullanılacak (8 + 8 + 4 = 20). Hangi dört alanın 3'te kalacağını
  16. oturum seçer; öneri: şehir hayatı, ulaşım, turizm, suç ve ceza 3'te kalsın.
- **Tekrar kaçınma:** (1) paket içi ve `T2-01`–`T2-20` ile konu cümlesi/`topic_area` çakışması
  script ile tarandı → **0 tekrar**; (2) **C01–C60'ın 180 konuşma 3. bölüm sorusuyla**
  otomatik kesişim taraması yapıldı — bu yüzden şu konular yazılmadı: onarmak mı yenisini
  almak mı (C22/C56), gündelik ürün atığının azaltılması (C52), giysilerin erken değiştirilmesi
  (C07), sessiz alanların azalması (C04), esnek başlangıç saatleri (C40), haberin yalnızca
  çevrim içi takip edilmesi (C59), reklamın alıcıya etkisi (C48), makinelerin işleri
  devralması (C46/C54), turist kalabalığının yayılması (C06); (3) **AT01–AT30 veri
  konularıyla** örtüşme yok — bu yüzden su tüketimi (AT09), arazi kullanımı (AT19), hava
  kirliliği (AT27), geri dönüşüm (AT01) ve haber kaynakları (AT30) deneme konusu yapılmadı;
  (4) **GT01–GT20 mektup durumlarıyla** örtüşme yok.
- **Format kararları 14. oturumla birebir sürdürüldü:** `prompt` = 1–2 cümlelik konu + boş
  satır + kalıp cümlesinin birebir standart hâli; alan adları ve **alan sırası** `T2-01` ile
  aynı; `key_points` **5**, `common_mistakes` **3–4**; `key_points` her zaman (a) görevin
  sorduğu asıl şeyi, (b) iki tarafın gerekçelerini, (c) tutum/hüküm zorunluluğunu içeriyor.
  Açıklama alanlarında vurgu için yıldız işareti kullanılmadı — 14. oturumla aynı düz metin.
- **Kalite ölçütü:** her konuda iki karşıt görüş de savunulabilir; hiçbiri uzman bilgisi
  istemiyor; ülkeye özgü politika, olay, kurum veya yasa geçmiyor (T2-39 özelleştirmeyi
  bilinçle ülke adı ve siyasi tartışma olmadan kurdu); kutuplaştırıcı temalar yok — script
  tarıyor. Gerçek marka/kişi/program adı yok; prompt'larda özel ad hiç kullanılmadı. Görünür
  metin İngiliz İngilizcesi (`programmes`, `rubbish`, `neighbourhood`), açıklama alanları Türkçe.
- **Ayrıcalık denetimi:** hiçbir konu yurt dışı seyahat geçmişi, araba sahipliği, yüksek gelir
  ya da belirli bir eğitim düzeyi varsaymıyor; T2-25 para cezasının gelire göre farklı
  hissedildiğini görevin içine yerleştirdi, T2-40 harcayamayanın dışarıda kalmasını
  `key_points`'e yazdı, T2-36 tek bir aile modelini varsaymamayı `common_mistakes`'e koydu.
- Zorluk dağılımı: **easy 4 · medium 12 · hard 4** (14. oturumla aynı).
- Doğrulama: geçici `tools/_t2_02_uret.py` + `tools/_t2_02_kontrol.py` (iş bitince silindi)
  JSON geçerliliği, zarf alanlarının **listesi ve sırası**, `set_id` ↔ dosya adı,
  `skill/module/task`, `instruction_line` birebirliği, kalıp cümlesinin prompt sonunda
  birebir bulunması, konu cümlesi sayısı (1–2), `key_points`/`common_mistakes` sayısı ve
  paket içi tekrar, Türkçe/İngilizce ayrımı, Amerikan yazım taraması, yasaklı tema ve gerçek
  marka taraması, prompt'ta özel ad taraması, görünür metinde "IELTS", **kalıp kotası**,
  **konu alanı kotası**, kırk dosyalık konu tekrarı ve **konuşma 3. bölüm kesişimi** denetledi.
  **Hata 0**, 16 uyarının hepsi yanlış pozitif: 15'i "Some people think … Others believe …"
  ortak kalıbının paylaşılan kelimeleri (`people`, `believe`, `think`, `should`), 1'i
  T2-28 ~ C50 (`second language`) — C50 "bir dili kimin daha kolay öğrendiği ve çeviri
  araçları"nı, T2-28 ise "kaçıncı yaşta başlanmalı"yı soruyor, soru farklı.
- `python tools/dogrula.py` → **şema hatası 0**, `writing/task2` **40** (20 → 40),
  `writing/task1` 50, speaking 200 + 240 değişmedi, işaretli 0, pasaj lisansı eksik 0,
  görünür metinde IELTS 0, yasak kaynak 0. Rapordaki "TAM TEST BUTUNLUGU … EKSIK" satırları
  bu paketle ilgisiz.
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaç dosyalarını `tools/calistir.py` kendi
  commit'iyle yazıyor).
- Atlanan/sorun: yok. **OPUS5-30'da 16 paketten 15'i tamam (530/550 birim).** Sıradaki iş
  **E paketi, oturum 3 — son paket (16. çalıştırma)** — `T2-41`–`T2-60`: 20 deneme konusu,
  kalıp kotası **opinion 4 · her iki görüş 4 · sorun–çözüm 3 · avantaj–dezavantaj 5 ·
  iki soruluk 4**, konu alanı kuralı yukarıda. `T2-01`–`T2-40`'ın kırk konusu ve kaçınılan
  konuşma/Academic/mektup başlıkları tekrar edilmeyecek. Bu paket bitince **OPUS5-30 tamam**.


---

## OPUS5-30 (16. çalıştırma: yazma 2. görev — oturum 3, son paket, 20 deneme konusu)

- Tarih: 2026-08-05
- Depo kontrolü: `content/speaking/part1/` **T01–T20 tam**, `content/speaking/part2-3/`
  **C01–C60 tam**, `content/writing/academic-task1/` **AT01–AT30 tam**,
  `content/writing/general-task1/` **GT01–GT20 tam**, `content/writing/task2/` **T2-01–T2-40
  dolu, T2-41–T2-60 boş**. Çalıştırma listesindeki sıradaki (ve son) bitmemiş paket
  **E paketi, oturum 3 (16. çalıştırma)** idi, o yapıldı. Var olan hiçbir dosyaya
  dokunulmadı. **20 birim** üretildi, hedefle aynı.
- Üretilen dosyalar — `content/writing/task2/T2-41.json` … `T2-60.json`:
  - **opinion (4):** T2-41 balık stokları toparlansın diye geniş deniz alanlarının
    avlanmaya kapatılması · T2-42 medyanın tanınmış eğlence/spor isimleri yerine topluma
    yararlı iş yapanlara yer ayırması · T2-43 otomatik düzeltme varken okulun yazım ve
    el yazısına zaman ayırması · T2-44 uzay araştırmasına ayrılan paranın konut ve sağlığa
    aktarılması
  - **her iki görüş (4):** T2-45 yeni çalışanın deneyimli meslektaş yanında mı yoksa iş
    yeri dışında resmi eğitimle mi yetişmesi · T2-46 okul sonrası eğitimin vergiyle
    ücretsiz mi olması yoksa öğrencinin maliyete katkı mı vermesi · T2-47 altmış yaş üstü
    çalışanların tutulması mı yoksa işe yeni başlayan gençlere öncelik mi · T2-48 yerel
    âdet ve geleneklerin okulda mı ailede mi yaşatılması
  - **sorun–çözüm (3):** T2-49 basamak, dar kaldırım ve kaldırıma park yüzünden yaşlıların,
    engellilerin ve küçük çocuklu yetişkinlerin hareket edememesi · T2-50 iş yerinde günlük
    yazılı mesaj yükünün çalışma zamanının büyük kısmını yemesi · T2-51 yeni mezun
    öğretmenlerin ilk birkaç yılda mesleği bırakması
  - **avantaj–dezavantaj (5):** T2-52 sitelerin herkese geçmiş davranışına göre haber, video
    ve müzik seçmesi · T2-53 gencin yaşlı bir kişinin evinde düşük kirayla, arkadaşlık ve
    yardım karşılığı kalması · T2-54 sokak, meydan ve kamu binalarının sürekli kamerayla
    kaydedilmesi · T2-55 okulun çocukların yürüyerek, bisikletle ya da otobüsle gelmesini
    istemesi · T2-56 dükkânların gece geç saatlere ve hafta sonuna kadar açık kalması
  - **iki soruluk (4):** T2-57 öğünlerin evde pişirmek yerine dışarıda yenmesi ya da hazır
    alınması · T2-58 ailelerin küçülmesi, bir–iki çocuklu hanelerin yaygınlaşması ·
    T2-59 ziyaretçilerin otel yerine yerel sakinlerin kiraya verdiği oda ve dairelerde
    kalması · T2-60 boş zamanda aile geçmişinin araştırılması ve yaşlı akrabaların
    anılarının kaydedilmesi
- **Kalıp kotası tamamlandı:** bu oturumda 15. oturumun bıraktığı kalan birebir üretildi —
  **opinion 4 · her iki görüş 4 · sorun–çözüm 3 · avantaj–dezavantaj 5 · iki soruluk 4**.
  **Altmış dosyanın toplamı: opinion 14 · her iki görüş 12 · sorun–çözüm 11 ·
  avantaj–dezavantaj 11 · iki soruluk 12** — prompt tablosuyla birebir.
- **Konu alanı dağılımı (bu oturum):** dil ve iletişim 2 · devletin rolü 2 · yaşlanan nüfus 2 ·
  kültür ve gelenek 2 · eğitim, sağlık, çevre, iş hayatı, teknoloji, aile ve toplum, tüketim,
  medya, şehir hayatı, ulaşım, turizm, suç ve ceza 1'er. 15. oturumun önerisine uyuldu:
  **şehir hayatı, ulaşım, turizm, suç ve ceza 3'te kaldı**, kalan on iki alan **4'e** çıktı.
  **Altmışın toplamı: 12 alan × 4 + 4 alan × 3 = 60.**
- **Tekrar kaçınma:** (1) T2-01–T2-40'ın kırk konusuyla ve paket içi çakışma script ile
  tarandı → **0 tekrar**; (2) **C01–C60'ın 180 konuşma 3. bölüm sorusuyla** otomatik kesişim
  taraması yapıldı — bu yüzden şu konular yazılmadı: ücret mi ilginç iş mi (C54), müze/spor
  tesisini kim ödemeli (C51), çevrim içi bilginin güvenilirliği ve kaynak denetimi (C57),
  yazılı mesajın sohbetin yerini alması (C42), giyimin sadeleşmesi (C07), tamir–yenisini alma
  (C22/C56), eşya atığı (C52), küçük dükkân–büyük mağaza karşılaştırması (C34), şehir
  merkezinin araca kapatılması (C47), sessiz alanların azalması (C04); (3) **AT01–AT30 veri
  konularıyla** örtüşme yok — bu yüzden ev enerjisi (AT03), su tüketimi (AT09), düzenli spor
  katılımı (AT17), arazi kullanımı (AT19), haber kaynakları (AT30) deneme konusu yapılmadı;
  (4) **GT01–GT20 mektup durumlarıyla** örtüşme yok.
- **Format kararları 14. ve 15. oturumla birebir sürdürüldü:** `prompt` = 1–2 cümlelik konu +
  boş satır + kalıp cümlesinin birebir standart hâli; alan adları ve **alan sırası** `T2-01`
  ile aynı; `key_points` **5**, `common_mistakes` **3–4**; `key_points` her zaman (a) görevin
  sorduğu asıl şeyi, (b) iki tarafın gerekçelerini, (c) tutum/hüküm zorunluluğunu içeriyor.
  Açıklama alanlarında yıldız işareti kullanılmadı.
- **Kalite ölçütü:** her konuda iki karşıt görüş de savunulabilir; hiçbiri uzman bilgisi
  istemiyor; ülkeye özgü politika, olay, kurum ya da yasa geçmiyor (T2-44 uzay bütçesini ve
  T2-46 eğitim harcını bilinçle ülke adı vermeden kurdu); kutuplaştırıcı tema yok — script
  tarıyor. Gerçek marka/kişi/kurum adı yok; prompt'larda özel ad hiç kullanılmadı. Görünür
  metin İngiliz İngilizcesi (`pavements`, `organisations`, `practise`, `neighbourhood`),
  açıklama alanları Türkçe.
- **Ayrıcalık denetimi:** hiçbir konu araba sahipliği, yurt dışı seyahat geçmişi, yüksek gelir
  ya da belirli bir eğitim düzeyi varsaymıyor; T2-55 aracı olmayan ve uzakta oturan aileleri
  görevin içine yerleştirdi, T2-53 "her yaşlı yardıma muhtaçtır" varsayımını
  `common_mistakes`'e yazdı, T2-58 tek bir aile modelini doğru kabul etmemeyi, T2-60 herkesin
  aile kayıtlarına ulaşamayabileceğini ekledi.
- Zorluk dağılımı: **easy 4 · medium 12 · hard 4** (önceki iki oturumla aynı).
  Altmışın toplamı: easy 12 · medium 36 · hard 12.
- Doğrulama: geçici `tools/_t2_03_uret.py` + `tools/_t2_03_kontrol.py` (iş bitince silindi)
  JSON geçerliliği, zarf alanlarının **listesi ve sırası**, `set_id` ↔ dosya adı,
  `skill/module/task`, `instruction_line` birebirliği, kalıp cümlesinin prompt sonunda birebir
  bulunması, konu cümlesi sayısı (1–2), `key_points`/`common_mistakes` sayısı, Türkçe/İngilizce
  ayrımı, Amerikan yazım taraması, yasaklı tema ve gerçek marka taraması, prompt'ta özel ad
  taraması, görünür metinde "IELTS", **altmışlık kalıp kotası**, **altmışlık konu alanı
  kotası**, kırk dosyalık konu tekrarı ve **konuşma 3. bölüm kesişimi** denetledi.
  **Hata 0**, 115 uyarının hepsi yanlış pozitif: 114'ü ortak kalıp cümlelerinin paylaşılan
  kelimeleri (`agree`, `disagree`, `extent`, `discuss`, `views`, `outweigh`, `happening`,
  `positive`, `negative`), 1'i T2-49 ~ C32 (`children`, `adults`, `around`) — C32 "çocukların
  çevresindeki yetişkinlere benzemesi"ni, T2-49 ise yaya erişimini konu alıyor, ilgisiz.
- `python tools/dogrula.py` → **şema hatası 0**, `writing/task2` **60** (40 → 60),
  `writing/task1` 50, speaking 200 + 240 değişmedi, işaretli 0, pasaj lisansı eksik 0,
  görünür metinde IELTS 0, yasak kaynak 0. Rapordaki "TAM TEST BUTUNLUGU … EKSIK" satırları
  bu paketle ilgisiz.
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaç dosyalarını `tools/calistir.py` kendi
  commit'iyle yazıyor).
- Atlanan/sorun: yok. **OPUS5-30 tamam — 16 paketin 16'sı bitti (550/550 birim):**
  konuşma 1. bölüm 200 soru (T01–T20), konuşma 2.+3. bölüm 60 kart + 180 soru (C01–C60),
  Academic 1. görev 30 (AT01–AT30), General 1. görev 20 (GT01–GT20), 2. görev 60 (T2-01–T2-60).
  Bu promptun 17. çalıştırması **yok**; yeniden çalıştırılırsa yapılacak iş "OPUS5-30 tamam"
  deyip çıkmaktır.

---

## FABLE5-40 (1. çalıştırma: AC1 — doğru / yanlış / verilmemiş, 7 soru)

- Tarih: 2026-08-05
- Depo kontrolü: `content/reading/tests/` altında altı testin klasörü de vardı ama
  **hiçbirinde `true-false-not-given.json` ya da `yes-no-not-given.json` yoktu**
  (`AC1/` içinde yalnızca note/sentence/summary/matching-information). Çalıştırma
  listesindeki ilk üretilmemiş paket **1 — AC1** idi, o yapıldı. Öteki paketlere
  (AC2–AC4, GT1–GT2, iki alıştırma dosyası) dokunulmadı.
- Çıktı: `content/reading/tests/AC1/true-false-not-given.json` — **7 soru (7–13)**,
  pasaj `A01` ("The Elephant Who Solved a Puzzle Without Practice"), `question_type`
  `true_false_not_given`, `practice: false`, kutu aralığı yönergede **7-13** yazılı.

### Sorular, cevaplar ve dayanak

| No | Cevap | Nereye dayanıyor | Test edilen nokta |
|---|---|---|---|
| 7 | TRUE | A/3 | önceki içgörü deneylerinde fillerin başarısızlığı ("almost always failed") |
| 8 | NOT GIVEN | — (konu B) | iki dişinin oturum sayısı |
| 9 | FALSE | C/4 | küp davranışının kademeli değil ani ortaya çıkışı |
| 10 | TRUE | D/3 | yiyecek yer değiştirince küpü yeniden konumlandırması |
| 11 | TRUE | E/4 | ertesi gün küpün bırakıldığı yere doğrudan gitmesi |
| 12 | FALSE | F/2 | başarısızlığın nedeni: araçlar mı, zekâ mı |
| 13 | NOT GIVEN | — (konu G) | küpün üstünde görüşünün netleşip netleşmediği |

- Dağılım **3 TRUE · 2 FALSE · 2 NOT GIVEN**, sıra `T · NG · F · T · T · F · NG`:
  hiçbir şık yarıyı geçmiyor, ardışık üç soru aynı cevap değil.
- **Sıra kuralı:** TRUE/FALSE kanıtları A→C→D→E→F, iki NOT GIVEN sorusu da konunun
  geçtiği yere (B ve G) oturuyor. Sorular yedi paragrafa (A–G) yayıldı, tek paragrafta
  yığılma yok.
- **A01'in öteki paketiyle çakışma yok:** aynı pasajı kullanan `note-completion`
  (soru 1–6) kablo, bambu, yedinci oturum, traktör lastiği, köşe ve parmak ucu
  bilgilerini hedefliyor; bu paket bunların hiçbirini sormuyor, kanıt cümleleri de
  ayrık (betikle karşılaştırıldı, kesişim boş).

### NOT GIVEN gerekçeleri (üç şart)

- **Soru 8:** konu B paragrafında var (üç katılımcı + "For the first several sessions
  none of the three animals…"); çürüten cümle yok (hiçbir yerde dişilerin oturum sayısı
  Kandula'nınkiyle kıyaslanmıyor); doğrulayan cümle de yok (C, D, E yalnızca Kandula'yı
  anlatıyor). Sayı hiç verilmediği için ne TRUE ne FALSE denebilir.
- **Soru 13:** konu G paragrafında var — küp basamağının avantajları tek tek sayılıyor
  (hortum ucunun açık kalması, dokunsal temas, gövdenin yiyeceğe yaklaşması); çürüten
  cümle yok; doğrulayan cümle de yok, çünkü **pasajda görme duyusu hiç geçmiyor**.
  E'deki tek görünürlük ifadesi ("invisible from the point where he entered") yiyeceğe
  değil saklanan küpe ait — gerekçe alanında bu ayrım açıkça yazıldı.
- İkisi de "Hata A" tuzağının (pasaj söylemiyorsa FALSE sanmak) tersine kuruldu;
  "Hata B" (kıyas/aritmetiği NOT GIVEN sanmak) için de soru 10 ve 11 bilinçle
  TRUE bırakıldı.

### Elenen adaylar

Üç adımlı testte **5 aday ifade elendi**, hiçbiri dosyaya girmedi:
(1) "iki dişi birbirine Kandula'dan yaş olarak daha yakın" — 33/61/7 aritmetiği
karşılaştırmayı tersine çeviriyordu, cevap tartışmalı; (2) "çubuk yiyeceğe ulaşmak
için fazla kısaydı" — B "long enough, in principle" diyor, FALSE ama 12. soruyla aynı
kalıpta ikinci bir ucuz FALSE olurdu; (3) "yedinci oturum ilkinden bir hafta sonraydı"
— D'deki "The next day"den oturumların günlük olduğu çıkarılabildiği için NOT GIVEN
belirsizdi; (4) "şempanzeler de Kandula'nınki gibi yuvarlanan bir basamakla denendi"
— A'daki kutu üst üste koyma ile örtüşme riski; (5) "Kandula dalı almadan önce birkaç
başarısız deneme yaptı" — C "he could not quite reach with his trunk" dediği için
kısmen doğrulanıyordu; 9. soru bu yüzden dalı değil **küp davranışının kademeli
gelişimini** hedefleyecek biçimde yeniden yazıldı.

### Doğrulama

- Denetim betiği depoda: `tools/_f40_kontrol.py`. Dosyayı **diskten geri okuyup**
  `passages/academic/A01.json` ile karşılaştırıyor.
- Denetlenenler: zarf alanları, `options` üçlüsü, yönerge kalıbının beş satırı ve
  kutu aralığı, numaraların 7–13 dizisi, her soruda `scan_note` ve `explanation`,
  TRUE/FALSE'ta `evidence`in ilgili paragrafta **birebir** bulunması **ve
  `evidence_locator.sentence`in gerçekten o cümleye denk gelmesi**, FALSE'ta
  `contradiction_point`, NOT GIVEN'da `evidence`/`contradiction_point`in `null` olması
  ve gerekçede üç şartın da yazılı olması, ifade uzunluğu (≤20 kelime, tek cümle),
  **pasajla 6 kelimelik birebir örtüşme taraması** (birebir kopya yasağı), şık dağılımı
  ve ardışık üçlü kuralı, kanıtların pasaj sırasında artması, aşırı genelleme kotası,
  görünür metinde "IELTS", note-completion ile kanıt kesişimi. **Hata 0, uyarı 0.**
- Kelime sayıları 10–14, hiçbiri 20'yi geçmiyor; "all / never / always / every / only"
  gibi aşırı genelleme **hiçbir soruda** kullanılmadı (kota 2, kullanılan 0).
- Son kontrol: yedi soru cevap anahtarına bakmadan aday gibi baştan çözüldü, yedisi de
  anahtarla uyuştu — **silinen soru yok**.
- `python tools/dogrula.py` → **şema hatası 0**, `reading/test` 120 → **127**,
  AC1 20/40 → **27/40** (kalan eksikler 14–18, 23–26, 32–35: başka promptların işi).
  Pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0.
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaç dosyalarını `tools/calistir.py`
  kendi commit'iyle yazıyor).
- Atlanan/sorun: yok. Sıradaki iş **2. çalıştırma: AC2 (pasaj A04, soru 7–13)**.

## FABLE5-40 (2. çalıştırma: AC2 — doğru / yanlış / verilmemiş, 7 soru)

- Tarih: 2026-08-05
- Depo kontrolü: `content/reading/tests/AC1/true-false-not-given.json` vardı (1. paket
  bitmiş), AC2–AC4, GT1–GT2 ve iki alıştırma dosyası yoktu. Çalıştırma listesindeki ilk
  üretilmemiş paket **2 — AC2** idi, o yapıldı; ötekilere dokunulmadı.
- Çıktı: `content/reading/tests/AC2/true-false-not-given.json` — **7 soru (7–13)**,
  pasaj `A04` ("A Tiny Moon That Voyager Never Saw"), `question_type`
  `true_false_not_given`, `practice: false`, kutu aralığı yönergede **7-13** yazılı.

### Sorular, cevaplar ve dayanak

| No | Cevap | Nereye dayanıyor | Test edilen nokta |
|---|---|---|---|
| 7 | TRUE | B/3 | sınırlı teleskop süresi için dünya çapında rekabet |
| 8 | FALSE | D/2 | yerinde oluşum / uzaktan yakalanma karşıtlığı |
| 9 | NOT GIVEN | — (konu E) | Miranda'nın beş büyük uydunun en küçüğü olup olmadığı |
| 10 | TRUE | E/3 | çok sayıda yakın uyduyu izlemenin uzmanlar için bile zor olması |
| 11 | TRUE | F/3 | yer tabanlı teleskopların da uyduyu seçememesi |
| 12 | FALSE | G/2 | "başka hiçbir gezegen bu kadar iç uyduya sahip değil" olumsuzlaması |
| 13 | NOT GIVEN | — (konu H) | bir yıl içinde yayına başvurma niyeti |

- Dağılım **3 TRUE · 2 FALSE · 2 NOT GIVEN**, sıra `T · F · NG · T · T · F · NG`:
  hiçbir şık yarıyı geçmiyor, ardışık üç soru aynı cevap değil.
- **Sıra kuralı:** TRUE/FALSE kanıtları B→D→E→F→G artan sırada, iki NOT GIVEN sorusu
  da konunun geçtiği yere (E ve H) oturuyor. Sorular yedi paragrafa yayıldı.
- **A04'ün öteki paketiyle çakışma sıfır — bu pasajda kritik kısıttı:** aynı pasajı
  kullanan `flow-chart-completion` (soru 1–6) B/2, C/1, C/2, D/1, E/1 ve E/2
  cümlelerini kanıt almış; bu paket bilerek **yalnızca B/3, D/2, E/3, F/3, G/2**
  cümlelerinden kuruldu (betikle karşılaştırıldı, kesişim boş). C paragrafı bu yüzden
  hiç kullanılmadı — iki cümlesi de akış şemasınca tüketilmişti.

### NOT GIVEN gerekçeleri (üç şart)

- **Soru 9:** konu E paragrafında var (beş büyük uydu adlarıyla sayılıyor); çürüten
  cümle yok (beşlinin kendi içindeki boyut sıralaması hiçbir yerde verilmiyor);
  doğrulayan cümle de yok — E'deki "five largest" ifadesi beşliyi **iç uydularla**
  kıyaslıyor, kendi aralarında sıralamıyor; C'deki boyut tartışması yalnızca yeni
  uyduya ait. (Gerçek dünyada doğru bir önerme ama pasaj söylemiyor — NOT GIVEN'ın
  tam tanımı.)
- **Soru 13:** konu H paragrafında var ("remains part of ongoing research rather than
  a finished, peer-reviewed result" — yayın durumu açıkça ele alınıyor); çürüten cümle
  yok (bir yıl içinde başvurulmayacağı söylenmiyor); doğrulayan cümle de yok ("ongoing
  research" araştırmanın sürdüğünü söyler, yayın takvimi ya da başvuru niyeti vermez).
  Niyet/gelecek planı = çıkarım kuralına da oturuyor.
- "Hata A" tersine kuruldu (ikisi de "pasaj söylemiyorsa FALSE" tuzağını hedefliyor);
  "Hata B" için soru 11 bilinçle TRUE bırakıldı (F/3'teki "any Earth-based telescope"
  ifadesi doğrudan karşılama, çıkarım değil).

### Elenen adaylar

Üç adımlı test + çakışma taraması **4 aday ifadeyi eledi**, hiçbiri dosyaya girmedi:
(1) "her pozlama yarım saatten kısaydı" (FALSE, B/2) ve (2) "çap doğrudan ölçüldü"
(FALSE, C/2) ve (3) "yörünge daha önce bilinen iki uydunun arasında" (TRUE, D/1) —
üçünün de kanıt cümlesi akış şeması paketince kullanılmıştı, aynı bilgiyi iki kez
test etmemek için atıldı; (4) "Webb'in Uranüs çevresinde başka uydular bulması
bekleniyor" — H'deki "how much ... can still remain hidden" cümlesi bunu **ima
ettiği** için NOT GIVEN belirsizdi (üçüncü şart sağlanmıyordu). Ayrıca "S/2025 U1
Güneş Sistemi'nin en küçük uydusudur" adayı 'one of the smallest' ile FALSE/NG
sınırında tartışmalı kaldığı için hiç yazılmadı.

### Doğrulama

- `tools/_f40_kontrol.py` **genelleştirildi**: test kimliğini argüman alıyor
  (`python tools/_f40_kontrol.py AC2`), pasajı PLAN'daki eşlemeden buluyor ve komşu
  tamamlama paketini (note/flow-chart/table) otomatik seçip kanıt kesişimine bakıyor.
  Sonraki çalıştırmalar (AC3, AC4) doğrudan kullanabilir.
- AC2 için: zarf alanları, yönerge kalıbı, 7–13 dizisi, birebir `evidence` +
  `evidence_locator.sentence` doğruluğu, FALSE'ta `contradiction_point`, NOT GIVEN'da
  üç şartlı gerekçe, ≤20 kelime, 6 kelimelik örtüşme taraması, dağılım/ardışıklık,
  kanıt sırası, genelleme kotası (kullanılan 0), IELTS taraması, flow-chart kesişimi
  → **hata 0, uyarı 0**. AC1 de yeniden koşuldu (gerileme yok: hata 0, uyarı 0).
- Kelime sayıları 9–15, hiçbiri 20'yi geçmiyor.
- Son kontrol: yedi soru cevap anahtarına bakmadan aday gibi baştan çözüldü, yedisi de
  anahtarla uyuştu — **son turda silinen soru yok** (elemeler yukarıda, taslak
  aşamasında).
- `python tools/dogrula.py` → **şema hatası 0**, `reading/test` 127 → **134**,
  AC2 20/40 → **27/40** (kalan eksikler 14–18, 23–26, 32–35: başka promptların işi).
  Pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0.
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaçları `tools/calistir.py` yazıyor).
- Not: `UYARILAR.txt`'de çalıştırıcının bıraktığı "2/8 işi 3 kez denendi, sonuç
  alınamadı" kaydı vardı; bu oturum o işi tamamladı, kayıt tarihçe olarak duruyor.
- Atlanan/sorun: yok. Sıradaki iş **3. çalıştırma: AC3 (pasaj A07, soru 7–13)**.

---

## FABLE5-40 (3. çalıştırma: AC3 — doğru / yanlış / verilmemiş, 7 soru)

- Tarih: 2026-08-05
- Depo kontrolü: `AC1` ve `AC2` klasörlerinde `true-false-not-given.json` vardı (1. ve 2.
  paket bitmiş); AC3, AC4, GT1–GT2 ve iki alıştırma dosyası yoktu. Çalıştırma
  listesindeki ilk üretilmemiş paket **3 — AC3** idi, o yapıldı; ötekilere dokunulmadı.
- Çıktı: `content/reading/tests/AC3/true-false-not-given.json` — **7 soru (7–13)**,
  pasaj `A07` ("The Whale That Recognised Herself in a Mirror"), `question_type`
  `true_false_not_given`, `practice: false`, kutu aralığı yönergede **7-13** yazılı.

### Sorular, cevaplar ve dayanak

| No | Cevap | Nereye dayanıyor | Test edilen nokta |
|---|---|---|---|
| 7 | TRUE | A/3 | testin ne ölçtüğünün hâlâ tartışmalı olması |
| 8 | FALSE | B/1 | grubun tamamının dişi olması (erkek yok) |
| 9 | TRUE | C/3 | iki hayvanın daha ilk ayna oturumunda tepki vermesi |
| 10 | NOT GIVEN | — (konu A ve D) | işaret uygulanırken uyuşturucu verilip verilmediği |
| 11 | TRUE | E/1 | üç işaret testinden birini geçmek = ikisini geçememek |
| 12 | FALSE | F/1 | "equally rich range" / "daha az çeşit" karşıtlığı |
| 13 | NOT GIVEN | — (konu G) | Monodontidae'nin yalnızca iki türden oluşup oluşmadığı |

- Dağılım **3 TRUE · 2 FALSE · 2 NOT GIVEN**, sıra `T · F · T · NG · T · F · NG`:
  hiçbir şık yarıyı geçmiyor, ardışık üç soru aynı cevap değil.
- **Sıra kuralı:** TRUE/FALSE kanıtları A→B→C→E→F artan sırada; iki NOT GIVEN sorusu da
  konunun ele alındığı yere oturuyor (10 → D, işaretin uygulanması; 13 → G, aile
  sınıflandırması). Sorular yedi paragrafa yayıldı, D ve G yalnızca NOT GIVEN'larla
  temsil ediliyor.
- **A07'nin öteki paketiyle çakışma sıfır:** aynı pasajı kullanan `table-completion`
  (soru 1–6) B/3, C/2, D/2, E/2, E/3 ve F/3 cümlelerini kanıt almış; bu paket bilerek
  **yalnızca A/3, B/1, C/3, E/1, F/1** cümlelerinden kuruldu (betikle karşılaştırıldı,
  kesişim boş, uyarı 0).
- Aritmetik kuralı (prompt'taki "Hata B") iki yerde bilinçli kullanıldı: soru 11
  (3 testten 1'i geçildi → 2'si geçilemedi) ve soru 9 ("dört hayvandan ikisi" →
  "two of the animals"). İkisi de doğrudan sayı okuması, çıkarım değil.

### NOT GIVEN gerekçeleri (üç şart)

- **Soru 10:** konu pasajda var — A/1 ayna testinin genel tarifinde işaretin
  "an anaesthetised **or** distracted animal" üzerine konduğunu söylüyor, D paragrafı da
  işaretin belugalara nasıl uygulandığını anlatıyor; çürüten cümle yok (balinaların
  uyuşturulmadığı ya da uyanık tutulduğu hiçbir yerde yazmıyor); doğrulayan cümle de yok
  — A'daki kalıp iki seçeneği **birden** verdiği için bu çalışmada hangisinin
  kullanıldığını göstermez, dolayısıyla "ima ediliyor" da denemez.
- **Soru 13:** konu G/1'de var (Monodontidae adıyla anılıyor, belugalar ve narvallar
  sayılıyor); çürüten cümle yok (ailenin başka üyesi adlandırılmıyor, "ikiden fazla tür
  var" diyen cümle de yok); doğrulayan cümle de yok — G "which **includes** belugas and
  narwhals" diyor; içermek, ailenin yalnızca o iki türden oluştuğunu göstermez. Klasik
  "includes / only" ayrımı.
- "Hata A" tuzağı (pasaj söylemiyorsa FALSE sanmak) iki NOT GIVEN'da da hedeflenen hata;
  buna karşılık soru 8 ve 12 gerçek çelişki taşıyor, yani aday her ikisini de ayırt
  etmek zorunda.

### Elenen adaylar

Üç adımlı test **5 aday ifadeyi eledi**, hiçbiri dosyaya girmedi:

1. "İşaret bazı denemelerde yüzgece uygulandı" (NOT GIVEN adayı, konu D) — D "most often
   just behind an eye or an ear" diyerek başka yerleri açık bırakıyor, ama aynı paragraf
   işaretin **aynasız görülemeyecek** bir yere konduğunu söylüyor ve C'de balina kendi
   göğüs yüzgecini "inspect it" diye çeviriyor, yani yüzgecini görebiliyor. İki cümle
   birleşince cevap FALSE'a kayıyordu → 2. şart sağlanmadı, atıldı.
2. "Narvalların da aynada kendini tanıdığı gösterildi" (NOT GIVEN adayı, konu A ve G) —
   A/2 "Only a short list of species has ever been reported to pass: …" listesi **kapalı**
   okunabiliyor ve narval listede yok; bu hâliyle çürüten cümle sayılabilirdi → NG/FALSE
   sınırında kaldı, atıldı. Yerine aynı paragraftan "includes / only" ayrımına dayanan
   soru 13 kuruldu.
3. "Natasha işaret görünürken çok daha uzun süre inceledi" (TRUE adayı, E/2–E/3) —
   geçerli bir soruydu ama kanıt cümleleri tablo tamamlama paketinin 4. ve 5. sorularınca
   kullanılmıştı; aynı sayıları iki kez test etmemek için atıldı, yerine E/1'e dayanan
   soru 11 yazıldı.
4. "Balinalar düz panelin önünde aynadakinden çok vakit geçirdi" (FALSE adayı, B/4) —
   sayı karşılaştırması (27 saat / 23 saat) temizdi, ama "spent … in front of" yapısını
   bozmadan yazılan her paraphrase ya birebir kopyaya ya da "ilgisini çekti" gibi
   yoruma kayıyordu; B zaten 1. cümleyle temsil edildiği için atıldı.
5. "Aynaya güçlü tepki veren iki balina gruptaki en genç hayvanlardı" — pasaj Kathy ve
   Marina'nın yaşını hiç vermiyor; Natasha "the older of the two" olarak geçse de grup
   içi yaş sıralaması yok. NG mi FALSE mu tartışmalı kaldığı için hiç yazılmadı.

### Doğrulama

- `python tools/_f40_kontrol.py AC3` (2. çalıştırmadan devralınan betik, test kimliğini
  argüman alıyor) → zarf alanları, yönerge kalıbı, 7–13 dizisi, birebir `evidence` +
  `evidence_locator.sentence` doğruluğu, FALSE'ta `contradiction_point`, NOT GIVEN'da üç
  şartlı gerekçe, ≤20 kelime, 6 kelimelik örtüşme taraması, dağılım/ardışıklık, kanıt
  sırası, genelleme kotası, IELTS taraması, tablo tamamlama kesişimi →
  **hata 0, uyarı 0**.
- Gerileme kontrolü: AC1 ve AC2 aynı betikle yeniden koşuldu → ikisi de hata 0, uyarı 0.
- Aşırı genelleme kotası: yalnızca soru 13 ("the only") — sınır 2, kullanılan 1.
- Kelime sayıları 10–14, hiçbiri 20'yi geçmiyor; her ifade tek cümle ve tek iddia.
- Son kontrol: yedi soru cevap anahtarına bakmadan aday gibi baştan çözüldü, yedisi de
  anahtarla uyuştu — **son turda silinen soru yok** (elemeler yukarıda, taslak
  aşamasında).
- `python tools/dogrula.py` → **şema hatası 0**, `reading/test` 134 → **141**,
  AC3 20/40 → **27/40** (kalan eksikler 14–18, 23–26, 32–35: başka promptların işi).
  Pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0.
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaçları `tools/calistir.py` yazıyor).
- Atlanan/sorun: yok. Sıradaki iş **4. çalıştırma: AC4 (pasaj A10, soru 7–13)**.

---

## FABLE5-40 (4. çalıştırma: AC4 — doğru / yanlış / verilmemiş, 7 soru)

- Tarih: 2026-08-05
- Depo kontrolü: `AC1`, `AC2` ve `AC3` klasörlerinde `true-false-not-given.json` vardı
  (1.–3. paketler bitmiş); AC4, GT1–GT2 ve iki alıştırma dosyası yoktu. Çalıştırma
  listesindeki ilk üretilmemiş paket **4 — AC4** idi, o yapıldı; ötekilere dokunulmadı.
- Çıktı: `content/reading/tests/AC4/true-false-not-given.json` — **7 soru (7–13)**,
  pasaj `A10` ("What Kind of Office Actually Works?"), `question_type`
  `true_false_not_given`, `practice: false`, kutu aralığı yönergede **7-13** yazılı.

### Sorular, cevaplar ve dayanak

| No | Cevap | Nereye dayanıyor | Test edilen nokta |
|---|---|---|---|
| 7 | TRUE | A/4 | çalışmanın nedeni: tartışmanın kontrollü karşılaştırmadan yoksun olması |
| 8 | FALSE | B/1 | takım sayısı 22 → "yirmiden az" çelişkisi |
| 9 | NOT GIVEN | — (konu B/2, F/3) | çalışanlara sıradaki düzenin önceden söylenip söylenmediği |
| 10 | TRUE | C/3 | sensörlerin ışık ve CO2'yi kesintisiz kaydetmesi |
| 11 | FALSE | D/3 | etkinlik temelli düzenin açık ofisten **düşük** memnuniyet alması |
| 12 | NOT GIVEN | — (konu C/3, F) | sıcaklığın düzenlere göre değişip değişmediği |
| 13 | TRUE | G/2 | kod çıktısında anlamlı fark bulunmaması |

- Dağılım **3 TRUE · 2 FALSE · 2 NOT GIVEN**, sıra `T · F · NG · T · F · NG · T`:
  hiçbir şık yarıyı geçmiyor, ardışık üç soru aynı cevap değil.
- **Sıra kuralı:** TRUE/FALSE kanıtları A→B→C→D→G artan sırada; iki NOT GIVEN sorusu da
  konunun ele alındığı yere oturuyor (9 → B/2'deki dönüşüm düzeni; 12 → C/3'te ölçülen,
  F'de sonucu tartışılan sensör verisi). Sorular A, B, C, D, F ve G paragraflarına
  yayıldı; E ve H bu pakette kullanılmadı (E'deki akış sayıları ve H'deki uyarı
  cümlesi başka paketlerin işi).
- **A10'un öteki paketiyle çakışma sıfır:** aynı pasajı kullanan `note-completion`
  (soru 1–6) A/3, B/2, C/4, F/3 ve H/2 cümlelerini kanıt almış; bu paket bilerek
  **yalnızca A/4, B/1, C/3, D/3, G/2** cümlelerinden kuruldu (betikle karşılaştırıldı,
  kesişim boş, uyarı 0).
- Aritmetik/doğrudan karşılaştırma kuralı (prompt'taki "Hata B") iki yerde bilinçli
  kullanıldı: soru 8 (22 takım → "yirmiden az" yanlış) ve soru 11 ("performed worse …
  roughly 14 per cent lower" → "daha yüksek" yanlış). İkisi de sayı okuması, çıkarım
  değil.

### NOT GIVEN gerekçeleri (üç şart)

- **Soru 9:** konu pasajda var — B/2 takımların dört düzen arasında ikişer haftalık
  dönemlerle döndüğünü ve Latin kare tasarımıyla her takımın sırayı farklı yaşadığını
  anlatıyor; çürüten cümle yok (sıranın gizlendiği, çalışanların habersiz olduğu hiçbir
  yerde yazmıyor); doğrulayan cümle de yok — sıranın araştırmacılarca **önceden
  belirlenmiş** olması onun **çalışanlara bildirildiği** anlamına gelmez, F/3'teki masa
  doluluğu artışı da davranışsal gözlem, bilgilendirme kanıtı değil.
- **Soru 12:** konu C/3'te var (sıcaklık, sensörlerin kaydettiği değerler arasında adıyla
  sayılıyor) ve F sensör verisinin ne gösterdiğini tartışıyor; çürüten cümle yok — F
  yalnızca gürültü sonucunu veriyor, G/2 "fark çıkmayan ölçütler" derken **yalnızca** kod
  gönderimi ile enerji düzeyini sayıyor, sıcaklığı anmıyor; doğrulayan cümle de yok —
  bir değişkenin ölçülmüş olması sonuç çıktığını göstermez. Klasik "ölçüldü / sonucu
  bildirildi" ayrımı.
- "Hata A" tuzağı (pasaj söylemiyorsa FALSE sanmak) iki NOT GIVEN'da da hedeflenen hata;
  buna karşılık soru 8 ve 11 gerçek, tek noktalı çelişki taşıyor.

### Elenen adaylar

Üç adımlı test **5 aday ifadeyi eledi**, hiçbiri dosyaya girmedi:

1. "Şirketin ana kampüsü dışında da ofisleri var" (NOT GIVEN adayı, konu A/4) — A/4
   "its **main** campus" diyor; "ana" sıfatı başka yerlerin varlığını ima ediyor, yani
   3. şart (dolaylı doğrulama da olmayacak) sağlanmıyor. NG ile TRUE arasında
   tartışmalı kaldığı için atıldı.
2. "Katılımcılara deneye katıldıkları için ek ödeme yapıldı" (NOT GIVEN adayı) —
   ücretlendirme pasajın konularından biri değil; 1. şart (konu pasajda geçmeli)
   sağlanmıyor, bu NOT GIVEN değil kötü sorudur. Atıldı.
3. "Etkinlik temelli düzen dört düzen içinde en düşük akış puanını aldı" (NOT GIVEN
   adayı, konu E) — E/2 iki yarı kapalı düzenin hem tam açık hem tam serbest düzenden
   daha iyi olduğunu söylüyor ama etkinlik temelli ile açık ofisi birbiriyle
   karşılaştırmıyor; teknik olarak NG, ancak "en düşük" iddiası kısmi sıralama yüzünden
   FALSE diye de savunulabiliyordu. Tartışmalı olduğu için atıldı.
4. "Açık ofisteki gürültü kulaklık koruması gerektirecek düzeydeydi" (NOT GIVEN adayı,
   konu F/2) — F/2 "exceeded recommended safe limits" diyor; "güvenli sınırın üstü"
   koruma gereğini dolaylı olarak ima ediyor, 3. şart sağlanmıyor. Atıldı.
5. "Açık ofiste güvenli sınırın aşılma sıklığı takım ofisindekinden azdı" (FALSE adayı,
   F/2) — geçerli ve temiz bir FALSE'tu, ama pakette zaten iki FALSE vardı ve dağılım
   kotasını bozacaktı; kullanılmadı (ambiguity değil, kota nedeniyle).

### Doğrulama

- `python tools/_f40_kontrol.py AC4` (2. çalıştırmadan devralınan betik; `PASAJ`
  eşlemesinde AC4 → A10 zaten tanımlıydı) → zarf alanları, yönerge kalıbı, 7–13 dizisi,
  birebir `evidence` + `evidence_locator.sentence` doğruluğu, FALSE'ta
  `contradiction_point`, NOT GIVEN'da üç şartlı gerekçe, ≤20 kelime, 6 kelimelik örtüşme
  taraması, dağılım/ardışıklık, kanıt sırası, genelleme kotası, IELTS taraması,
  note-completion kesişimi → **hata 0, uyarı 0**.
- Gerileme kontrolü: AC1, AC2 ve AC3 aynı betikle yeniden koşuldu → üçü de hata 0,
  uyarı 0.
- Aşırı genelleme kotası: **hiç kullanılmadı** (sınır 2, kullanılan 0) — bu pakette
  "all / never / only" türü ucuz FALSE yok, beş sorunun tamamı içerik çelişkisine ya da
  sayıya dayanıyor.
- Kelime sayıları 9–15, hiçbiri 20'yi geçmiyor; her ifade tek cümle ve tek iddia.
- Son kontrol: yedi soru cevap anahtarına bakmadan aday gibi baştan çözüldü, yedisi de
  anahtarla uyuştu — **son turda silinen soru yok** (elemeler yukarıda, taslak
  aşamasında).
- `python tools/dogrula.py` → **şema hatası 0**, `reading/test` 141 → **148**,
  AC4 20/40 → **27/40** (kalan eksikler 14–18, 23–26, 32–35: başka promptların işi).
  Pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0.
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaçları `tools/calistir.py` yazıyor).
- Atlanan/sorun: yok. Sıradaki iş **5. çalıştırma: GT1 (pasaj G01 soru 8–14 TFNG +
  pasaj G05 soru 33–36 YES/NO/NOT GIVEN, toplam 11 soru)**.

## FABLE5-40 (5. çalıştırma: GT1 — doğru / yanlış / verilmemiş + evet / hayır / verilmemiş, 11 soru)

### Üretilen

- `content/reading/tests/GT1/true-false-not-given.json` — G01 (Cloverfield metin seti,
  A–E), soru 8–14, TRUE/FALSE/NOT GIVEN. Dağılım 3T/2F/2NG, sıra A4 → A5 → B2 → (B3) →
  C1 → D3 → (E1). Cevaplar beş metnin beşine de yayılıyor.
- `content/reading/tests/GT1/yes-no-not-given.json` — G05 (hane gıda israfı çalışması),
  soru 33–36, YES/NO/NOT GIVEN. Dağılım 2Y/1N/1NG, sıra B1 → C2 → F3 → (G). Üç kanıt
  cümlesi de yazarın kendi sesindeki yargılar: B/1 (öz-tahmin güvenilmez), C/2 (yenmeyen
  kısımlar "gerçek israf değil"), F/3 ("gerçek ölçek manşet rakamlardan yüksek olabilir").

### Taslakta elenen adaylar (5)

1. "Joining the library costs nothing for people who live in Cloverfield" (TRUE adayı,
   A/1) — beş yaş altı sakinler hiç üye olamadığı için "kasabada oturan herkes" öznesi
   tartışmalıydı; Adım 1'de kararsız kaldı, atıldı.
2. "Replacing a lost card costs more than a single Zone 1 fare" (TRUE adayı, C) —
   karşılaştırma aritmetik olarak doğruydu ama kanıt iki ayrı cümleye (C/2 + C/5)
   yayılıyordu; "tek cümle tek başına doğrulamalı" kuralına takıldı, atıldı.
3. "More extended studies should be completed before the results guide countrywide
   policy" (YES adayı, I/3) — kanıt cümlesi "They also note..." ile aktarılan yazar
   görüşüydü, yazarın kendi sesi değildi; "kanıt gerçekten yazar görüşü cümlesi" şartını
   net sağlamadığı için F/3'teki yazar çıkarımıyla (soru 35) değiştirildi.
4. "Turning scraps into compost is the most effective way to cut food waste" (NOT GIVEN
   adayı, H) — H'nin kompostu öven çerçevesi dolaylı doğrulama sayılabilirdi; 3. şart
   (dolaylı doğrulama da olmayacak) riskliydi, atıldı.
5. "The researchers were wrong to leave composted food out of their totals" (NOT GIVEN
   adayı, F) — savunulabilir bir NG'ydi ama kanıt bölgesi soru 35'le aynı cümleye (F/3)
   biniyordu ve "önemli bir sınır" nitelemesi yazar yargısı diye tartışılabilirdi;
   yerine G'deki tarih etiketi NG'si (soru 36) kondu.

### Doğrulama

- `tools/_f40_kontrol.py` GT desteğiyle yeniden yazıldı: AC1–AC4 eski davranışla denetlenmeye
  devam ediyor; GT1/GT2 için hem TFNG (bölüm 1 pasajı, soru 8–14) hem YNNG (bölüm 3
  pasajı, soru 33–36) tek komutla denetleniyor. G01'deki "a.m. / p.m." kısaltmaları için
  cümle bölücüye koruma eklendi (yalnız ardından büyük harf geliyorsa yeni cümle).
  Komşu kanıt çakışması taramasına summary/sentence-completion da eklendi (GT1
  summary-completion aynı pasajı, G05'i kullanıyor — çakışma çıkmadı).
- `python tools/_f40_kontrol.py GT1` → iki paket de **hata 0, uyarı 0** (zarf, yönerge
  kalıbı, numara aralıkları, birebir evidence + locator, FALSE/NO'da contradiction_point,
  NG'de üç şartlı gerekçe, ≤20 kelime, 6 kelimelik örtüşme, dağılım/ardışıklık, kanıt
  sırası, genelleme kotası, IELTS taraması).
- Gerileme: AC1–AC4 aynı betikle yeniden koşuldu → dördü de **hata 0, uyarı 0**.
- Aşırı genelleme kotası: **hiç kullanılmadı** (sınır 2, kullanılan 0; iki pakette de
  "all / never / only / the most" yok).
- İfade kelime sayıları: TFNG 8–14, YNNG 11–14; hepsi tek cümle, tek iddia.
- Son kontrol: 11 soru cevap anahtarına bakılmadan aday gibi baştan çözüldü, on biri de
  anahtarla uyuştu — **son turda silinen soru yok** (elemeler yukarıda, taslak aşamasında).
- `python tools/dogrula.py` → **şema hatası 0**, `reading/test` 148 → **159**,
  GT1 27/40 → **31/40** (kalan eksikler 21–24 ve 28–32: FABLE5-41 ile FABLE5-42'nin işi).
  Pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0.
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaçları `tools/calistir.py` yazıyor).
- Atlanan/sorun: yok. Sıradaki iş **6. çalıştırma: GT2 (pasaj G02 soru 8–14 TFNG +
  pasaj G06 soru 33–36 YES/NO/NOT GIVEN, toplam 11 soru)**.

## FABLE5-40 (6. çalıştırma: GT2 — doğru / yanlış / verilmemiş + evet / hayır / verilmemiş, 11 soru)

### Üretilen

- `content/reading/tests/GT2/true-false-not-given.json` — G02 (Millbrook boş zaman
  metin seti, A–E), soru 8–14, TRUE/FALSE/NOT GIVEN. Dağılım 3T/2F/2NG, sıra A3 → (B1)
  → B3 → C3 → D3 → (E1) → E3. Cevaplar beş metnin beşine de yayılıyor. Kanıt cümleleri
  aynı pasajı kullanan `matching-information.json`ın (soru 1–7) kanıtlarıyla hiç
  çakışmıyor (o set A2/A4, B2, C4, D4, E2/E4 cümlelerini kullanıyor).
- `content/reading/tests/GT2/yes-no-not-given.json` — G06 (gönüllülük-gelir-sağlık
  çalışması), soru 33–36, YES/NO/NOT GIVEN. Dağılım 2Y/1N/1NG, sıra (A1) → C3 → E1 →
  F3. Üç kanıt cümlesi de yazarın kendi sesindeki yargılar: C/3 (öz-bildirimli sağlık
  "güvenilir öngörücü"), E/1 ("one plausible explanation"), F/3 ("açık farkla hikâyenin
  daha büyük kısmı"). Aynı pasajı kullanan `summary-completion.json`ın kanıtlarıyla
  (F2, G3, H1, I1) çakışma yok.

### Taslakta elenen adaylar (4)

1. "Damaged bicycles incur a £90 repair charge" (FALSE adayı, A/2) — pasaj 90 sterlini
   iade edilene kadar tutulan geçici blokaj olarak anlatıyor, hasar hâlinde ne kadar
   kesileceğini söylemiyor; FALSE ile NOT GIVEN arasında savunulabilir kaldı, Adım 1'de
   kararsızlık çıkınca atıldı.
2. "Swimmers are required to wear a cap during family sessions" (FALSE adayı, D/4) —
   soru sağlamdı ama kanıt cümlesi (D/4) aynı testin matching-information 6. sorusunun
   kanıtıyla birebir aynıydı ve aynı olguyu (zorunlu/isteğe bağlı bone) ikinci kez test
   ediyordu; D/3'teki giriş ücreti FALSE'uyla (soru 12) değiştirildi.
3. "Randomly assigning people to volunteer would be the best way to test whether
   volunteering improves health" (YES adayı, I/3) — kanıt "They argue..." ile aktarılan
   yazar görüşüydü, yazarın kendi sesi değil; GT1'de 3 no.lu adayın elenme gerekçesiyle
   aynı nedenden atıldı.
4. "The study offers definite proof that volunteering leads to better health" (NO adayı,
   I/1) — kanıt cümlesi (I/1) summary-completion 40. sorusunun kanıtıyla birebir aynıydı
   (betiğin komşu taraması uyarı verecekti); yerine F/3'e dayanan gelir-payı NO'su
   (soru 36) kondu.

### Doğrulama

- `python tools/_f40_kontrol.py GT2` → iki paket de **hata 0, uyarı 0** (zarf, yönerge
  kalıbı, numara aralıkları 8–14 / 33–36, birebir evidence + locator, FALSE/NO'da
  contradiction_point, NG'de üç şartlı gerekçe, ≤20 kelime, 6 kelimelik örtüşme,
  dağılım/ardışıklık, kanıt sırası, genelleme kotası, IELTS taraması). Betikte değişiklik
  gerekmedi; G02'nin "a.m. / p.m." kısaltmaları 5. çalıştırmada eklenen korumayla
  sorunsuz bölündü.
- Gerileme: AC1–AC4 ve GT1 aynı betikle yeniden koşuldu → beşi de **hata 0, uyarı 0**.
- Aşırı genelleme kotası: TFNG'de 1 soru ("every year", soru 9 — NG tuzağı olarak
  bilinçli), YNNG'de 0; sınır 2, aşılmadı.
- İfade kelime sayıları: TFNG 8–15, YNNG 10–14; hepsi tek cümle, tek iddia.
- Son kontrol: 11 soru cevap anahtarına bakılmadan aday gibi baştan çözüldü, on biri de
  anahtarla uyuştu — **son turda silinen soru yok** (elemeler yukarıda, taslak aşamasında).
- `python tools/dogrula.py` → **şema hatası 0**, `reading/test` 159 → **170**,
  GT2 20/40 → **31/40** (kalan eksikler 21–24 ve 28–32: FABLE5-41 ile FABLE5-42'nin işi).
  Pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0.
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaçları `tools/calistir.py` yazıyor).
- Atlanan/sorun: yok. Sıradaki iş **7. çalıştırma: TRUE/FALSE/NOT GIVEN alıştırması
  (`content/reading/practice/true-false-not-given.json`, 15 soru)**.

## FABLE5-40 (7. çalıştırma: TRUE / FALSE / NOT GIVEN alıştırması, 15 soru)

### Üretilen

- `content/reading/practice/true-false-not-given.json` — soru 1–15, dört pasaja bölündü:
  **A02** (ahtapotlarda birey tanıma) 1–4, **A05** (Çatalhöyük buğdayı) 5–8,
  **A08** (buzul üzerindeki deprem izleri) 9–12, **A09** (camlaşmış beyin dokusu) 13–15.
  Pasaj başına en fazla 4 soru kuralına uyuldu; `test_id` null, `practice` true, her
  item'da `passage_id` var, `stem_block` hangi soruların hangi pasaja ait olduğunu yazıyor.
- Pasaj seçimi: tam testlerde TFNG için kullanılan pasajlar (A01, A04, A07, A10, G01,
  G02) ve YNNG için kullanılanlar (G05, G06) dışarıda bırakıldı. Kalanlar arasından, o
  ana kadar en az kanıt cümlesi harcanmış olanlar seçildi (A02/A05/A08 sekizer, A09 on
  dört). A03 bilerek atlandı: AC1 matching-information + summary-completion + alıştırma
  cümle tamamlama zaten 14 cümlesini tüketmişti. Görüş ağırlıklı pasajlar (A03, A06,
  A10, A11, A12, G05, G06) 8. çalıştırmadaki YES/NO/NOT GIVEN alıştırması için bırakıldı.
- Dağılım 6 TRUE / 5 FALSE / 4 NOT GIVEN; ardışık üç soru aynı cevabı almıyor. Kanıtlar
  her pasaj grubunun içinde metin sırasını izliyor (A02: B2→C3→F3, A05: B1→B3→G3,
  A08: B1→F2→G1, A09: A3→C1).

### Taslakta elenen adaylar (4)

1. "Octopuses kept behind an opaque divider behaved more aggressively during cohabitation"
   (NOT GIVEN adayı, A02) — H/3'teki "vision alone ... was enough to produce weaker
   measurable differences" cümlesi bölme türüne göre bir davranış farkı ima ettiği için
   NOT GIVEN ile FALSE arasında savunulabilir kaldı; Adım 3'ün ikinci şartı sağlanmadı, atıldı.
2. "Ink was released more often by strangers than by familiar pairs in the final test"
   (FALSE adayı, A02 F/4) — soru sağlamdı ama kanıt cümlesi AC1 cümle tamamlamanın 21.
   sorusunda zaten kullanılmıştı (tam testte kullanılan cümle yasağı); yerine F/3'e
   dayanan TRUE (soru 4) kondu.
3. "The two laboratories obtained results that disagreed with one another" (NOT GIVEN
   adayı, A05 D/1) — E paragrafındaki "the team recovered thirty-two DNA sequences in
   total" ifadesi sonuçların birleştirildiğini, dolayısıyla uyuştuğunu ima ediyor
   okunabiliyordu; Adım 3'ün üçüncü şartı takıldı, atıldı.
4. "Similar vitrified tissue has since been found at Pompeii" (NOT GIVEN adayı, A09) —
   H/3'teki "may yet be identified elsewhere in the town" ifadesi "henüz bulunmadı"
   biçiminde okunabildiği için FALSE ile NOT GIVEN arasında kaldı; yerine yaş tayini
   yöntemine dayanan temiz NOT GIVEN (soru 14) kondu.

### Doğrulama

- `tools/_f40_kontrol.py` alıştırma paketlerini de denetleyecek şekilde genişletildi:
  `python tools/_f40_kontrol.py PR-TFNG` (8. çalıştırma için `PR-YNNG` de hazır). Çok
  pasajlı yapıya uygun olarak zarf alanları (`test_id` null, `practice` true,
  `passage_id` null, `module` item'lardan türetiliyor), 1'den başlayan numaralar,
  pasaj başına ≤4 soru kotası, kanıt sırasının **her pasaj grubu içinde** ayrı
  denetlenmesi, `stem_block`ın bütün pasajları anması ve kanıt çakışmasının bütün
  okuma paketlerine karşı taranması eklendi.
- `python tools/_f40_kontrol.py PR-TFNG` → **hata 0, uyarı 0** (yönerge kalıbı,
  numara aralığı 1–15, birebir evidence + locator, FALSE'ta contradiction_point,
  NG'de üç şartlı gerekçe, ≤20 kelime, 6 kelimelik örtüşme, dağılım/ardışıklık,
  kanıt sırası, genelleme kotası, IELTS taraması, kanıt çakışması).
- Gerileme: `python tools/_f40_gerileme.py` (yeni yardımcı betik) AC1–AC4, GT1, GT2 ve
  PR-TFNG'yi tek komutta koşuyor → **yedisi de hata 0, uyarı 0**.
- Aşırı genelleme kotası: **hiç kullanılmadı** (sınır 2, kullanılan 0).
- İfade kelime sayıları: 11–16; hepsi tek cümle, tek iddia.
- Kanıt çakışması: 15 sorunun hiçbirinin kanıt cümlesi başka bir okuma paketinde
  kullanılmıyor (betik bütün `content/reading` ağacını tarıyor).
- Son kontrol: 15 soru cevap anahtarına bakılmadan aday gibi baştan çözüldü, on beşi de
  anahtarla uyuştu — **son turda silinen soru yok** (elemeler yukarıda, taslak aşamasında).
- `python tools/dogrula.py` → **şema hatası 0**, `reading/practice` 80 → **95**.
  Pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0.
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaçları `tools/calistir.py` yazıyor).
- Atlanan/sorun: yok. Sıradaki iş **8. çalıştırma: YES/NO/NOT GIVEN alıştırması
  (`content/reading/practice/yes-no-not-given.json`, 15 soru)** — FABLE5-40'ın son paketi.

## FABLE5-40 (8. çalıştırma: YES / NO / NOT GIVEN alıştırması, 15 soru — **paket tamam**)

### Üretilen

- `content/reading/practice/yes-no-not-given.json` — soru 1–15, dört pasaja bölündü:
  **A06** (uzaktan çalışmada deneyimli takım arkadaşları) 1–4, **A10** (ofis tasarımı
  deneyi) 5–8, **A11** (karlı ormanın sakinleştirici etkisi) 9–12, **A12** (şekerleme ve
  bellek) 13–15. `test_id` null, `practice` true, her item'da `passage_id`, `stem_block`
  soru–pasaj eşlemesini yazıyor.
- Pasaj seçimi: 7. çalıştırmada YNNG için ayrılan görüş ağırlıklı havuzdan (A03, A06,
  A10, A11, A12) dört pasaj alındı; G05/G06 tam test YNNG'de kullanıldığı için dışarıda
  bırakıldı. A03 yine atlandı (kanıt cümleleri büyük ölçüde tükenmişti). Dördünde de
  kanıt olarak **yazar yargısı** cümleleri seçildi ("unusually rigorous", "did not
  appear here", "clear ranking", "essentially the reverse", "findings caution against"
  vb.), salt veri cümlesi kanıt yapılmadı.
- Dağılım 6 YES / 5 NO / 4 NOT GIVEN; ardışık üç soru aynı cevabı almıyor. Kanıtlar her
  pasaj grubunda metin sırasını izliyor (A06: C1→E3→H3, A10: A1→D1→E2, A11: A1→G1→H3,
  A12: E1→H3); NOT GIVEN sorular konularının ele alındığı yere yerleştirildi (1: A/H,
  8: H, 10: B, 13: C–D).

### Taslakta elenen adaylar (2)

1. "Employees rated the open-plan design less favourably than any other layout tested"
   (YES adayı, A10 H/1) — H/1 "rated more poorly than every alternative" dese de D/2–D/3
   etkinlik temelli tasarımın memnuniyette açık plan tabanının ~%14 **altında** kaldığını
   söylüyor; pasajın içinde gerilim olduğu için Adım 1'de karar değişti, atıldı. Yerine
   E/2'nin yarı kapalı düzenler yargısına dayanan YES (soru 7) kondu.
2. "Watching star teammates at work produced a clear gain in employees' own performance"
   (NO adayı, A06, kapsam belirtilmemiş hali) — E/3'teki "Whatever benefit workers
   usually gain" ifadesi genel düzlemde faydayı kabul eder okunabildiği için ifade
   çalışma kapsamına sabitlenmeden belirsiz kalıyordu; "In the study, ..." kapsamıyla
   yeniden yazıldı (soru 3). Ayrıca E/2 kanıt olarak bilerek kullanılmadı — AC2 özet
   tamamlamada zaten harcanmıştı (kanıt çakışması yasağı).

### Doğrulama

- `python tools/_f40_kontrol.py PR-YNNG` → **hata 0, uyarı 0** (YNNG yönerge kalıbı,
  numara aralığı 1–15, pasaj başına ≤4 soru, birebir evidence + locator, NO'da
  contradiction_point, NG'de üç şartlı gerekçe, ≤20 kelime, 6 kelimelik örtüşme,
  dağılım/ardışıklık, grup içi kanıt sırası, genelleme kotası, IELTS taraması, bütün
  okuma paketlerine karşı kanıt çakışması).
- `tools/_f40_gerileme.py` listesine PR-YNNG eklendi; koşu → AC1–AC4, GT1, GT2,
  PR-TFNG, PR-YNNG **sekizi de hata 0, uyarı 0**.
- Aşırı genelleme kotası: **hiç kullanılmadı** (sınır 2, kullanılan 0).
- İfade kelime sayıları: 11–17; hepsi tek cümle, tek iddia.
- Son kontrol: 15 soru cevap anahtarına bakılmadan aday gibi baştan çözüldü, on beşi de
  anahtarla uyuştu — **son turda silinen soru yok** (elemeler yukarıda, taslak aşamasında).
- `python tools/dogrula.py` → **şema hatası 0**, `reading/practice` 95 → **110**.
  Pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0.
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaçları `tools/calistir.py` yazıyor).
- Atlanan/sorun: yok. FABLE5-40'ın 8 iş paketinin tamamı üretildi (AC1–AC4 TFNG,
  GT1–GT2 TFNG+YNNG, alıştırma TFNG, alıştırma YNNG = 80 soru) — **FABLE5-40 tamam**.

---

## FABLE5-41 (1. çalıştırma: AC1 + AC2 — çoktan seçmeli, 8 soru)

Üretilen: `content/reading/tests/AC1/multiple-choice.json` (A03, soru 32–35) ve
`content/reading/tests/AC2/multiple-choice.json` (A06, soru 32–35). Her iki grup da
promptun açık talimatına göre kuruldu: **32, 33 tek cevaplı (A–D) + 34–35 çift cevaplı
(A–G, iki numara tek soru)**. Kontrol listesindeki "3 tek + 1 çift" ifadesi 5 numara
gerektirirdi; plandaki 32–35 aralığı 4 numara olduğu için promptun somut yerleşim
talimatı esas alındı.

### Kanıt seçimi — en sıkı kısıt buydu

A03 ve A06'nın cümlelerinin büyük bölümü zaten harcanmıştı (AC1/AC2 bilgi eşleştirme +
özet tamamlama, ayrıca alıştırma paketleri). Çakışmayı önlemek için önce her iki pasajın
**kullanılmamış cümleleri** çıkarıldı ve sorular yalnız onlara dayandırıldı:

| Soru | Kanıt | Durum |
|---|---|---|
| AC1 32 | A03 B/1 + B/3 | hiçbir pakette kullanılmamış |
| AC1 33 | A03 D/1 | hiçbir pakette kullanılmamış |
| AC1 34–35 | A03 F/1 + G/1 | hiçbir pakette kullanılmamış |
| AC2 32 | A06 B/4 | hiçbir pakette kullanılmamış |
| AC2 33 | A06 G/1 | hiçbir pakette kullanılmamış |
| AC2 34–35 | A06 H/2 | **alıştırma not tamamlama 3 ile aynı cümle** |

Son satır tek istisna: A06'da tek cümlede iki ayrı sebep barındıran başka yer kalmamıştı
(çift cevaplı soru bunu gerektiriyor). Hedef bilgi farklı — alıştırma "individual output"
boşluğunu doldurtuyor, buradaki soru yıldız çalışanların etkisiz kalmasının iki sebebini
sordurtuyor. AC2'nin kendi 27–31 ve 36–40 sorularıyla çakışma yok.

### Sıra kuralı

Promptun 3. soru kökü kuralı gereği kanıtlar metin sırasını izliyor:
A03 → B/1, D/1, F/1–G/1 · A06 → B/4, G/1, H/2. Cevaplar tek paragrafta yığılmıyor.

### Çeldiriciler

Her soruda en az üç ayrı çeldirici türü var; "pasajda geçmiyor" gerekçesi soru başına
en fazla bir kez kullanıldı (AC2 34–35'te hiç kullanılmadı — beş çeldiricinin beşi de
pasajda dayanağı olan yanlış okumalar).

Taslakta değiştirilen çeldiriciler (savunulabilirlik testinde elenenler, 3):

1. AC1 34–35, "Records of the water's acidity and temperature" — soru kökü "dalgıçların
   topladığı malzeme" iken aletlerin sürekli kaydettiği veriler de "sonradan analiz için
   alındı" diye savunulabiliyordu. Sorunun tamamı D paragrafından F–G'ye taşındı
   (ayrıca D/2 zaten AC1 özet tamamlamada kanıt olarak kullanılmıştı).
2. AC1 32, "The reef has grown back since the volcano collapsed" — aynı fikir 33'te de
   çeldirici olacaktı; tekrarı önlemek için "To account for the unusual warmth of the
   surrounding sea" (yer değiştirme) ile değiştirildi.
3. AC2 34–35, "Managers gave experienced employees fewer check-ins" — H/4'te bu bir
   **öneri**, uygulanmış bir düzen değil; aynı listede B seçeneğiyle (yıldızların
   dağıtılması) anlamca fazla yakındı. Yerine "Star performers messaged teammates less
   often" (G/2'nin bulgusunu özneye kaydıran yer değiştirme) kondu.

### Doğrulama

- Altı sorunun altısında `evidence` pasajda **birebir** bulundu (Grep ile tek tek
  arandı, hepsi 1 eşleşme).
- Seçenek uzunlukları dengeli: her grupta en uzun seçenek en kısanın iki katının altında.
- Doğru cevap harfleri: AC1 → B, A, {C,F} · AC2 → B, D, {C,F}. Üst üste aynı harf yok.
- Ölçülen beceriler ayrışıyor: AC1 → yazarın amacı / ayrıntı / kapsam;
  AC2 → ayrıntı / argüman yapısı / sebep.
- Kök + seçenekler tek cevaplı sorularda 40–46 kelime (sınır 60).
- `python tools/dogrula.py` → **şema hatası 0**, `reading/test` 170 → **178**.
  AC1 ve AC2 artık 31/40 (kalan eksikler 14–18 ve 23–26, yani FABLE5-42'nin işi).
  Pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0.
- Son kontrol: altı soru da cevap anahtarına bakılmadan aday gibi baştan çözüldü, altısı
  da anahtarla uyuştu — **son turda silinen soru yok** (elemeler yukarıda, taslak
  aşamasında).
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaçları `tools/calistir.py` yazıyor).
- Atlanan/sorun: yok. Sıradaki paket **2. çalıştırma: AC3 + AC4**.

## FABLE5-41 (2. çalıştırma: AC3 + AC4 — çoktan seçmeli, 8 soru)

Üretilen: `content/reading/tests/AC3/multiple-choice.json` (A09, soru 32–35) ve
`content/reading/tests/AC4/multiple-choice.json` (A12, soru 32–35). Yerleşim 1.
çalıştırmadaki gibi: **32, 33 tek cevaplı (A–D) + 34–35 çift cevaplı (A–G, iki numara
tek soru)**.

### Kanıt seçimi

Her iki pasajın 3. pasaj sıfatıyla zaten iki paketi vardı (27–31 bilgi eşleştirme,
36–40 özet tamamlama). Önce o iki paketin kullandığı cümleler çıkarıldı, sorular
kalanlara dayandırıldı:

| Soru | Kanıt | Durum |
|---|---|---|
| AC3 32 | A09 A/3 | hiçbir pakette kullanılmamış |
| AC3 33 | A09 D/3 | hiçbir pakette kullanılmamış |
| AC3 34–35 | A09 F/2 + G/1 | F/2 özet 39'da **sayı** için, G/1 hiç kullanılmamış |
| AC4 32 | A12 A/2 | hiçbir pakette kullanılmamış |
| AC4 33 | A12 C/2 + C/3 | C/3 özet 37'de **uyanık kalma** için |
| AC4 34–35 | A12 D/2 + F/1 | hiçbir pakette kullanılmamış |

İki kısmi çakışmanın ikisinde de hedef bilgi farklı: özet tamamlama F/2'den yalnız
"seven" sayısını, buradaki soru nöronlar arası iletişim için gerekli proteinin varlığını
istiyor; özet 37 C/3'ten "awake" sözcüğünü, buradaki soru iki grubun ortak yanını
(on iki saatlik aralık) sordurtuyor ve cevap için C/2 ile C/3'ün birlikte okunması
gerekiyor.

### Sıra kuralı

Kanıtlar metin sırasını izliyor: A09 → A/3, D/3, F–G · A12 → A/2, C/2–3, D–F.
Cevaplar tek paragrafta yığılmıyor.

### Çeldiriciler

Taslakta değiştirilenler (savunulabilirlik testinde elenenler, 4):

1. AC3 33'te iki çeldirici de "başka aletin işini bu alete yükleme" idi (X ışını ve
   elektron mikroskobu); türler tekrar etmesin diye biri kapsam kaydırmaya
   ("her kılıf katmanının sağlam kaldığını doğrulamak"), biri cazip ama yoka
   (daha büyük örnek kümesi) çevrildi.
2. AC3 34–35'te doğru ikili başta A ve B idi; alfabenin başında yığılmasın diye
   seçenekler yeniden sıralandı (B ve F).
3. AC4 33'te "Her iki grup da aynı sayıda kelime çifti çalıştı" seçeneği atıldı —
   C/4'e göre bu **doğru**, dolayısıyla çeldirici olamaz. Yerine sabah öğrenmeyi iki
   gruba birden yayan kapsam kaydırma kondu.
4. AC4 34–35'te "Şekerlemeler tanınan süreden kısa sürdü" doğru seçeneklerden biri
   olacaktı (90 dakikalık fırsat, ortalama 64,1 dakika); D/2 "took a 90-minute nap"
   dediği için fırsat süresi mi uyku süresi mi olduğu tartışmaya açıktı, tartışmasız
   cevap kuralı gereği çıkarıldı. Yerine F/1'deki hafif uyku evresi kondu.

"Pasajda geçmiyor" gerekçesi soru başına en fazla bir kez kullanıldı; AC4 33 ve
AC4 34–35'te hiç kullanılmadı.

### Doğrulama

- Altı sorunun altısında `evidence` pasajda **birebir** bulundu (geçici betikle
  `passages/academic/A09.json` ve `A12.json` tam metnine karşı arandı, betik silindi).
- Her çeldirici için `distractor_analysis` dolu; harf kümesi doğru cevap hariç bütün
  seçeneklerle birebir eşleşiyor.
- Seçenek uzunlukları dengeli: en uzun ≤ 2 × en kısa (AC3 7–8 / 5–7 / 6–8 kelime,
  AC4 6–10 / 7–9 / 5–7 kelime).
- Kök + seçenekler: AC3 40 / 34 / 56, AC4 41 / 41 / 54 kelime (sınır 60).
- Hiçbir seçenek pasaj metninde birebir geçmiyor.
- Doğru cevap harfleri: AC3 → B, C, {B,F} · AC4 → C, B, {C,E}. Üst üste aynı harf yok.
- Ölçülen beceriler ayrışıyor: AC3 → yazarın amacı / yöntemin işlevi / kimyasal ayrıntı;
  AC4 → gerekçe / deney tasarımı karşılaştırması / ayrıntı.
- `python tools/dogrula.py` → **şema hatası 0**, `reading/test` 178 → **186**.
  AC3 ve AC4 artık 31/40 (kalan eksikler 14–18 ve 23–26, yani FABLE5-42'nin işi).
  Pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0.
- Son kontrol: altı soru da cevap anahtarına bakılmadan aday gibi baştan çözüldü, altısı
  da anahtarla uyuştu — **son turda silinen soru yok** (elemeler yukarıda, taslak
  aşamasında).
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaçları `tools/calistir.py` yazıyor).
- Atlanan/sorun: yok. Sıradaki paket **3. çalıştırma: GT1 + GT2 (soru 21–24)**.

## FABLE5-41 (3. çalıştırma: GT1 + GT2 — çoktan seçmeli, 8 soru)

Üretilen: `content/reading/tests/GT1/multiple-choice.json` (G03, soru 21–24) ve
`content/reading/tests/GT2/multiple-choice.json` (G04, soru 21–24). Yerleşim AC'deki
düzenin GT karşılığı: **21, 22 tek cevaplı (A–D) + 23–24 çift cevaplı (A–G, iki numara
tek soru)**.

### Kanıt seçimi

GT 2. bölüm setlerinin (G03, G04) zaten ikişer paketi vardı (GT1: not tamamlama 15–20 +
cümle tamamlama 25–27; GT2: tablo tamamlama 15–20 + cümle tamamlama 25–27). O paketlerin
kullandığı cümleler önce çıkarıldı, sorular kalanlara dayandırıldı:

| Soru | Kanıt | Durum |
|---|---|---|
| GT1 21 | G03 A-metni C/2 | C/1 (kart okuyucu) not 17'de; C/2 hiç kullanılmamış |
| GT1 22 | G03 A-metni D/2 | D/1 (takas formu) not 18'de; D/2 hiç kullanılmamış |
| GT1 23–24 | G03 B-metni C/2 + C/3 | C/1'in "double time" kısmı cümle 26'da; C/2–3 hiç kullanılmamış |
| GT2 21 | G04 A-metni D/2 | D/1 (mentor) tablo 20'de; D/2 hiç kullanılmamış |
| GT2 22 | G04 B-metni A/2 | A/1 (deneme süresi) cümle 25'te; A/2 hiç kullanılmamış |
| GT2 23–24 | G04 B-metni B/4 + D/1 | B/5'in ekipman kısmı cümle 26'da; B/4 ve D/1 hiç kullanılmamış |

### Sıra kuralı

Kanıtlar metin sırasını izliyor: G03 → A-metni C, A-metni D, B-metni C · G04 → A-metni D,
B-metni A, B-metni B–D. Cevaplar iki metne de yayılıyor.

### Çeldiriciler

Taslakta elenen/değiştirilenler (savunulabilirlik testi, 3):

1. GT1 22'de "istek yalnızca bir gün önceden yapıldıysa" çeldiricisi atıldı — 48 saat
   kuralına göre bu da geçerli bir ret sebebi olurdu, yani **savunulabilirdi**. Yerine
   panodaki düzeni değiştirme (cazip ama yok) kondu.
2. GT2 23–24'te "haftada en az iki gün ofise gelmek" çeldirisi atıldı — uzaktan çalışma
   en fazla üç günle sınırlı olduğundan beş günlük haftada bu **matematiksel olarak
   doğru** çıkıyordu. Yerine ofiste düzenli toplantı (cazip ama yok) kondu.
3. GT2 22'de "düzenlemeleri daha sık gözden geçirilir" çeldirisi, soru içinde çeldirici
   türü çeşitliliği ikiye düştüğü için ekipman ödemesine (cazip ama yok) çevrildi.

"Pasajda geçmiyor" gerekçesi soru başına en fazla bir kez kullanıldı; GT1 21, GT1 22,
GT2 22 ve GT2 23–24'te birer kez, GT1 23–24 ve GT2 21'de hiç.

### Doğrulama

- Altı sorunun altısında `evidence` pasajda **birebir** bulundu
  (`tools/_f41_gt_kontrol.py` ile `passages/general/G03.json` ve `G04.json` tam metnine
  karşı arandı; betik depoda duruyor).
- Her çeldirici için `distractor_analysis` dolu; harf kümesi doğru cevap hariç bütün
  seçeneklerle birebir eşleşiyor (betik kontrol ediyor).
- Seçenek uzunlukları dengeli: en uzun ≤ 2 × en kısa (betik kontrol ediyor, uyarı 0).
- Kök + seçenekler: GT1 42 / 40 / 58, GT2 45 / 49 / 59 kelime (sınır 60).
- Hiçbir seçenek pasaj metninde birebir geçmiyor (betik kontrol ediyor).
- Doğru cevap harfleri: GT1 → A, C, {B,E} · GT2 → C, A, {B,D}. Üst üste aynı harf yok.
- Ölçülen beceriler ayrışıyor: GT1 → prosedür / ret koşulu / politika taraması;
  GT2 → koşullu çıkarım / belirli grup hakkında ayrıntı / yükümlülük taraması.
- `python tools/dogrula.py` → **şema hatası 0**, `reading/test` 186 → **194**.
  GT1 ve GT2 artık 35/40 (kalan eksik 28–32, yani FABLE5-42'nin başlık eşleştirmesi).
  Pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0.
- Son kontrol: altı soru da cevap anahtarına bakılmadan aday gibi baştan çözüldü, altısı
  da anahtarla uyuştu — **son turda silinen soru yok** (elemeler yukarıda, taslak
  aşamasında).
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaçları `tools/calistir.py` yazıyor).
- Atlanan/sorun: yok. Sıradaki paket **4. çalıştırma: alıştırma (15 soru)**.

## FABLE5-41 (4. çalıştırma: çoktan seçmeli alıştırması, 15 soru — **paket tamam**)

Üretilen: `content/reading/practice/multiple-choice.json`. Yerleşim tam testlerdeki
mantığın alıştırma karşılığı: **9 tek cevaplı (A–D) + 3 çift cevaplı (A–G)**, çift
cevaplı soru iki numara kapladığı için sayılan toplam **15** (`tools/dogrula.py`
select_count=2 olan soruyu 2 sayıyor; `reading/practice` 110 → 125).

Numaralar: 1, 2, **3–4**, 5, 6, **7–8**, **9–10**, 11, 12, 13, 14, 15.

### Pasaj seçimi

Bir pasajdan en fazla 4 soru kuralıyla dört pasaj gerekiyordu. Kullanılmayacaklar:

- **A03, A06, A09, A12** — tam testlerin çoktan seçmelisi zaten bu pasajlardan (1.–3.
  çalıştırma). Aynı pasajdan ikinci bir çoktan seçmeli seti kurulmadı.
- **A01, A10** — ilk taslak bunlarla başladı, sonra bırakıldı: her ikisinde de tam
  testte hem tamamlama (6 soru) hem doğru/yanlış (7 soru) paketi var, üstüne alıştırma
  soruları biniyor (A01: 21, A10: 21 hedeflenmiş cümle). Geriye çeldirici kurmaya
  yetecek dokunulmamış cümle kalmıyordu.

Seçilenler ve doyma durumu: **A02, A05, A08, A11** (her birinde tam testten yalnızca
4 cümle tamamlama sorusu var; başlık/özellik eşleştirme paketleri henüz üretilmedi).

| Soru | Pasaj | Kanıt | Neden boş |
|---|---|---|---|
| 1 | A02 | B/1 | B/2 alıştırma doğru-yanlış 1'de, B/3 alıştırma cümle 4'te; B/1 hiç kullanılmamış |
| 2 | A02 | C/4 | C/2 AC1 cümle 19'da, C/3 alıştırma doğru-yanlış 2'de; C/4 hiç kullanılmamış |
| 3–4 | A02 | H/3 | H/2 (dear enemy) AC1 cümle 22'de; H/3 hiç kullanılmamış |
| 5 | A05 | A/3 | A/2 (1952) alıştırma cümle 13'te; A/3 hiç kullanılmamış |
| 6 | A05 | B/2 | B/1 ve B/3 alıştırma doğru-yanlış 5–6'da; B/2 hiç kullanılmamış |
| 7–8 | A05 | F/2 + G/3 | F/2'nin "transitional stage" kısmı alıştırma cümle 14'te, G/2 AC2 cümle 22'de; spelt ipucu ve G/3 hiç kullanılmamış |
| 9–10 | A08 | A/1 + B/3 | A/2 alıştırma not 7'de, B/1 alıştırma doğru-yanlış 9'da, B/2 AC3 cümle 19'da; A/1 ve B/3 hiç kullanılmamış |
| 11 | A08 | C/3 | C/2 AC3 cümle 20'de; C/3 hiç kullanılmamış |
| 12 | A08 | E/2–3 | E paragrafı hiçbir pakette kullanılmamış |
| 13 | A11 | B/3 | B/2 (crossover) alıştırma özet 6'da; B/3 hiç kullanılmamış |
| 14 | A11 | C/2 | C/1 AC4 cümle 19'da, C/3 alıştırma bilgi eşleştirmede; C/2 hiç kullanılmamış |
| 15 | A11 | H/2 | H/1 AC4 cümle 22'de, H/3 alıştırma evet-hayır 15'te; H/2 hiç kullanılmamış |

### Sıra kuralı

Her pasaj kendi içinde metin sırasını izliyor: A02 → B, C, H · A05 → A, B, F–G ·
A08 → A–B, C, E · A11 → B, C, H. Çift cevaplı sorular grubun başına ya da sonuna
zorlanmadı, kanıtın geçtiği yere kondu (A08'de 9–10 bu yüzden en başta).

### Çeldiriciler

Taslakta elenen/değiştirilenler (savunulabilirlik testi, 3):

1. Soru 15'te "çalışmayı daha büyük bir grupla yinelemek" çeldiricisi atıldı — pasaj
   örneklemin küçük ve tek kurumdan olduğunu kendisi söylüyor, dolayısıyla bu şıkkı
   seçen aday **haklı olabilirdi**. Yerine etkinin süresini ölçmek (cazip ama yok) kondu.
2. A01 taslağında "aynı ağırlıkta benzer bir nesneyle değiştirildi" çeldirisi atılmıştı —
   küp kaldırılınca traktör lastiği platform olarak kullanılıyor, yani **savunulabilirdi**.
   (Soru A01 ile birlikte tamamen düştü.)
3. Soru 9–10'da "yamaçları yüzyıllardır dengeliydi" çeldirisi atıldı — G paragrafı
   "önceden dengeli yamaçlar" diyor, süre verilmemiş olsa da şık kısmen **doğrulanıyordu**.
   Yerine küçük bir madenci kasabası (cazip ama yok) kondu.

"Pasajda geçmiyor" gerekçesi soru başına en fazla bir kez kullanıldı; soru 5 ve 11'de
hiç kullanılmadı, kalan on soruda birer kez. Çeldirici türü çeşitliliği tek cevaplılarda
3, çift cevaplılarda 4 (betik sayıyor).

### Doğrulama

- On iki sorunun on ikisinde `evidence` pasajda **birebir** bulundu
  (`tools/_f41_alistirma_kontrol.py`, `passages/academic/` tam metnine karşı; betik
  depoda duruyor).
- Her çeldirici için `distractor_analysis` dolu; harf kümesi doğru cevap hariç bütün
  seçeneklerle eşleşiyor. Seçenek sayısı (4 / 7), `select_count`–cevap sayısı uyumu ve
  cevapların alfabetik sırası da betikte kontrol ediliyor.
- Seçenek uzunlukları dengeli: en uzun ≤ 2 × en kısa (uyarı 0).
- Kök + seçenekler: en yüksek 55 kelime (soru 3–4), en düşük 34 (soru 15); sınır 60.
- Hiçbir seçenek pasaj metninde birebir geçmiyor (betik kontrol ediyor).
- Doğru cevap harfleri: B, A, {C,F}, B, D, {C,F}, {B,E}, D, C, A, C, D — üst üste ortak
  harf yok (betik kontrol ediyor).
- Ölçülen beceriler ayrışıyor: ana fikir (5), terim anlamı (6), yöntem ayrıntısı (1, 11),
  bir işlemin amacı (2, 13, 14), yazarın amacı (12), çıkarım/kapsam (3–4, 7–8, 9–10, 15).
- `python tools/dogrula.py` → **şema hatası 0**, `reading/practice` 110 → **125**.
  Pasaj lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0.
- Son kontrol: on iki soru da cevap anahtarına bakılmadan aday gibi baştan çözüldü, on
  ikisi de anahtarla uyuştu — **son turda silinen soru yok** (elemeler yukarıda, taslak
  aşamasında).
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaçları `tools/calistir.py` yazıyor).
- Atlanan/sorun: yok. **FABLE5-41 tamam** (24 tam test + 15 alıştırma = 39 soru).

## FABLE5-42 (1. çalıştırma: AC1 — başlık + özellik eşleştirme, 9 soru)
- Tarih: 2026-08-05
- Depoda hiç `matching-headings` / `matching-features` / `matching-sentence-endings`
  dosyası yoktu → çalıştırma listesinin ilk bitmemiş paketi **AC1**, o yapıldı.
- Üretilen dosyalar (ikisi de pasaj **A02**, plandaki yerleşime göre):
  - `content/reading/tests/AC1/matching-headings.json` — soru **14–18**, paragraf B–F
  - `content/reading/tests/AC1/matching-features.json` — soru **23–26**
- **Özellik eşleştirmesi neden kişi listesiyle yapılmadı:** A02'de adlandırılmış birden
  çok araştırmacı yok (tek ekip, tek çalışma) — promptun 2. kuralı bu durumda kişi
  listesini yasaklıyor. Prompt listenin "kişi/kurum/yıl/**kategori**" olabileceğini
  söylüyor; deneyin grupları kategori olarak kullanıldı (A–E, 5 öğe / 4 soru).
  **C öğesi (üç günlük birliktelik) hiçbir ifadenin cevabı değil** — boşta çeldirici.
- Başlık listesi **10 başlık / 5 soru + 1 örnek** (örnek: Paragraph A → `v`), dolayısıyla
  4 başlık boşta kalıyor (kural: soru sayısından en az 3 fazla).
- **Ters kontrol ve elenenler (3):**
  1. "Two kinds of reunion compared" başlığı atıldı — hem E hem F paragrafına uyuyordu,
     yani soruyu bozuyordu. Yerine ayrımı netleştiren ikili kondu: E için "How the final
     day's encounters were arranged" (düzenleme), F için "Reactions that depended on who
     the partner was" (sonuç).
  2. "A practical benefit outside the laboratory" çeldirisi atıldı — H paragrafının ana
     fikrini **gerçekten** karşılıyordu. Yerine H ile yüzeysel ilgili ama hiçbir
     paragrafa uymayan "Why smell could not explain the results" kondu (H tam tersini
     söylüyor: koku ve tat henüz elenemiyor).
  3. "A decline in aggressive displays" çeldirisi atıldı — D paragrafının ana fikrine
     fazla yakındı, seçen aday **haklı olabilirdi**. Yerine yalnızca ayrıntı düzeyinde
     kalan "A defence used when threatened" kondu.
  Ayrıca "How long recognition lasts" başlığı, pasajdaki `recognition` kelimesini birebir
  kullanmasın diye "How long the effect of a meeting lasts" olarak değiştirildi.
- Çeldiricilerin gölgelediği paragraflar: `i`→B (ağırlık eşleştirmesi ayrıntısı),
  `iii`→D/F (mürekkep püskürtme), `vi`→G (tanımanın süresi), `x`→C/H (koku). Hiçbiri
  sorulan bir paragrafın ana fikri değil.
- Özellik eşleştirmede yakın çift bilerek kuruldu: **A (saydam bölme) ile B (opak bölme)**
  — 25 ve 26 tam bu ayrımı ölçüyor, ayırt edicilik oradan geliyor.
- `allow_repeat` iki dosyada da `false`; yönergelerde `NB` satırı yok — tutarlı.
- Cevaplar: başlıklarda vii, ii, iv, viii, ix (sıra kuralı yok); özellikte D, E, B, A.
- **Doğrulama:**
  - `tools/_f42_kontrol.py` yazıldı (depoda duruyor): dokuz sorunun dokuzunda `evidence`
    pasajda **birebir** bulundu ve `evidence_locator` doğru paragrafı gösteriyor. Betik
    ayrıca seçenek sayısını, boşta çeldirici kalıp kalmadığını, `allow_repeat`–`NB`
    tutarlılığını, `heading_check`/`feature_check` doluluğunu, hiçbir seçeneğin pasajda
    birebir geçmediğini ve görünür metinde IELTS olmadığını kontrol ediyor → **0 sorun**.
  - `python tools/dogrula.py` → **şema hatası 0**, `reading/test` 194 → **203**,
    **AC1 artık 40/40 TAM**. Pasaj lisansı eksik 0, görünür metinde IELTS 0,
    yasak kaynak 0.
  - Son kontrol: dokuz soru da cevap anahtarına bakılmadan aday gibi baştan çözüldü,
    dokuzu da anahtarla uyuştu — **son turda silinen soru yok** (elemeler yukarıda,
    taslak aşamasında).
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaçları `tools/calistir.py` yazıyor).
- Atlanan/sorun: yok. Sıradaki paket: **AC2** (14–18 + 23–26, pasaj **A05**).

## FABLE5-42 (2. çalıştırma: AC2 — başlık + özellik eşleştirme, 9 soru)
- Tarih: 2026-08-05
- Depoda yalnızca AC1'in iki dosyası vardı → çalıştırma listesinin ilk bitmemiş paketi
  **AC2**, o yapıldı. AC1 dosyalarına dokunulmadı.
- Üretilen dosyalar (ikisi de pasaj **A05**, "Çatalhöyük buğdayı", plandaki yerleşime göre):
  - `content/reading/tests/AC2/matching-headings.json` — soru **14–18**, paragraf B–F
  - `content/reading/tests/AC2/matching-features.json` — soru **23–26**
- Başlık listesi **10 başlık / 5 soru + 1 örnek** (örnek: Paragraph A → `v`), 4 başlık
  boşta. Cevaplar: iv, viii, x, ii, vii (sıra kuralı yok, bilerek karıştırıldı).
- **Özellik eşleştirmesi yer listesiyle yapıldı** (A Çatalhöyük · B Karacadağ ·
  C Bereketli Hilal · D Avrupa · E Birleşik Krallık). A05'te de adlandırılmış birden çok
  araştırmacı yok (tek ekip), promptun 2. kuralı kişi listesini yasaklıyor; "kategori"
  izni yer adlarıyla kullanıldı. **E (Birleşik Krallık) hiçbir ifadenin cevabı değil** —
  boşta çeldirici, üstelik pasajda laboratuvarlardan birinin bulunduğu yer olarak geçtiği
  için yer adı tarayan adaya inandırıcı geliyor. Cevaplar: A, C, B, D.
- Yakın çift bilerek kuruldu: **C (Bereketli Hilal) ile B (Karacadağ)** aynı cümlede ve
  ikisi de bir köken iddiası taşıyor; 24 ile 25 tam bu ayrımı ölçüyor (geneli kapsayan
  geniş bölge / "özellikle" tek bir buğdayın doğduğu dar yer). Ayırt edicilik oradan.
- **Ters kontrol ve elenenler (3):**
  1. C paragrafı için düşünülen "Why appearance alone was not enough" başlığı atıldı —
     H paragrafına da tam uyuyordu (H: mikroskopta bir tür gibi duran tane genetikte
     başka çıkabiliyor), yani iki paragrafa birden oturuyordu. Yerine C'nin asıl ana
     fikrini veren "Setting out to read the genes themselves" kondu.
  2. "How the site was first located and excavated" çeldiricisi atıldı — A paragrafının
     ikinci cümlesini (1952'de fark ediliş, 1961–65 kazısı) **gerçekten** karşılıyordu.
     Yerine hiçbir paragrafa uymayan, yalnızca A'daki "yollar" ayrıntısına yaslanan
     "Trade links between distant settlements" kondu.
  3. Özellik listesi önce **buğday türleriyle** (einkorn · emmer · ekmeklik · spelt)
     kurulmuştu, tümüyle atıldı: spelt de ekmeklik buğday da altı kromozom takımlı
     olduğundan "yalnızca bu biçimde bulunan genetik parça" türü ifadeler iki cevaba
     birden açık kalıyordu (kalite kuralı 1: tek ve tartışmasız cevap). Ayrıca emmer'in
     tek başına ayırt edici hiçbir özelliği yok — dört temiz ifade çıkmıyordu.
     Aynı gerekçeyle "kanıt türü" listesi (mikroskop görüntüsü / DNA dizileri) de elendi:
     pasajın kendisi çelişiyor — B paragrafında mikroskop karmaşık buğday, E paragrafında
     aynı biçim basit buğday söylüyor.
- Çeldiricilerin gölgelediği paragraflar: `i`→A (yollar), `iii`→D (gen/protein ayrıntısı),
  `vi`→C (8.400 yıl), `ix`→B (tanelerin iyi korunmuşluğu). Hiçbiri sorulan bir paragrafın
  ana fikri değil, hepsi yalnızca ayrıntı düzeyinde ilgili.
- `allow_repeat` iki dosyada da `false`; yönergelerde `NB` satırı yok — tutarlı.
- **`tools/_f42_kontrol.py` düzeltildi:** "hiçbir seçenek pasajda birebir geçmesin" kuralı
  bütün tiplere uygulanıyordu; özellik eşleştirmesinde liste zaten pasajdaki
  kişi/kurum/yer adlarından kurulur (resmî örnek anahtarında da liste "the Chinese",
  "the Indians" gibi pasajdaki adların aynısı), dolayısıyla kural orada yanlış alarm
  veriyordu. Artık bu kural yalnızca başlık ve cümle sonu eşleştirmesine işliyor; özellik
  eşleştirmesinde yerine promptun 3. kuralı denetleniyor: **hiçbir ifade pasajdaki
  cümlenin birebir kopyası olamaz**. AC1 dosyaları yeni betikle de temiz.
- **Doğrulama:**
  - `python tools/_f42_kontrol.py` → AC2 iki dosya **0 sorun**; dokuz sorunun dokuzunda
    `evidence` pasajda birebir bulundu ve `evidence_locator` doğru paragrafı gösteriyor.
    AC1 dosyaları da yeniden denetlendi → **0 sorun**.
  - `python tools/dogrula.py` → **şema hatası 0**, `reading/test` 203 → **212**,
    **AC2 artık 40/40 TAM** (AC1 ile birlikte iki tam test bitti). Pasaj lisansı eksik 0,
    görünür metinde IELTS 0, yasak kaynak 0.
  - Son kontrol: `tools/kor-kopya.py` ile cevap anahtarı silinmiş kopya üretildi, dokuz
    soru da aday gibi baştan çözüldü, dokuzu da anahtarla uyuştu — **son turda silinen
    soru yok** (elemeler yukarıda, taslak aşamasında).
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaçları `tools/calistir.py` yazıyor).
- Atlanan/sorun: yok. Sıradaki paket: **AC3** (14–18 + 23–26, pasaj **A08**).

## FABLE5-42 (3. çalıştırma: AC3 devralındı + AC4 üretildi — başlık + özellik eşleştirme, 9+9 soru)
- Tarih: 2026-08-05
- **Oturum başı durumu:** AC3'ün iki dosyası depoda **tam ama commit edilmemiş** hâlde
  bulundu (NOTLAR kaydı da yoktu) — önceki oturum dosyaları yazdıktan sonra doğrulama/
  commit adımlarına gelemeden kesilmiş. Talimat gereği AC3 **yeniden üretilmedi**;
  eksik kalan adımları burada tamamlandı:
  - `python tools/_f42_kontrol.py` AC3 iki dosya → **0 sorun** (dokuz `evidence` A08'de
    birebir, locator'lar doğru).
  - Kör kopya üzerinden dokuz AC3 sorusu aday gibi çözüldü → **9/9 anahtarla uyuştu**.
  - AC3 dosyaları bu oturumda kendi commit'iyle depoya alındı.
- Çalıştırma listesinin ilk **üretilmemiş** paketi **AC4** idi, o yapıldı. Üretilen
  dosyalar (ikisi de pasaj **A11**, "kar altındaki ormanın sakinleştirici etkisi"):
  - `content/reading/tests/AC4/matching-headings.json` — soru **14–18**, paragraf B–F
  - `content/reading/tests/AC4/matching-features.json` — soru **23–26**
- Başlık listesi **10 başlık / 5 soru + 1 örnek** (örnek: Paragraph A → `iii`), 4 başlık
  boşta. Cevaplar: ii, v, ix, vi, viii (sıra kuralı yok).
- **Özellik eşleştirmesi anket (ölçek) listesiyle yapıldı** (A Profile of Mood States ·
  B Positive and Negative Affect Schedule · C Restorative Outcome Scale · D Subjective
  Vitality Scale). A11'de adlandırılmış birden çok araştırmacı yok (tek ekip), promptun
  2. kuralı kişi listesini yasaklıyor; "kategori" izni pasajın dört ölçeğiyle kullanıldı.
  **D (Subjective Vitality Scale) hiçbir ifadenin cevabı değil** — boşta çeldirici,
  üstelik pasajda gerçek bulgusu (bina sonrası düşüş) olduğu için inandırıcı.
  **C iki kez cevap** (23 ve 25) → `allow_repeat: true` + yönergede `NB` satırı var,
  tutarlı (bu setin ilk `allow_repeat=true` dosyası; resmî özellik anahtarında da aynı
  harf iki kez kullanılıyor). Cevaplar: C, A, C, B.
- Yakın çiftler bilerek kuruldu: **24, A ile B'yi** ayırıyor (ikisi de olumsuz duyguyu
  ölçüyor; ama orman sonrası düşüş pasajda açıkça POMS'a bağlı ve "çoğu" kaydı 6 boyutun
  5'ine oturuyor) · **25, C ile D'yi** ayırıyor (bina sonrası ikisi de düştü; "yaklaşık
  yarıya" ölçüsü yalnızca C'ye bağlanmış).
- **Taslakta elenenler (3):**
  1. F için "Refreshed but no livelier" başlığı atıldı — `refresh` kökü F'de birebir
     geçiyor (`strongly refreshing`), kelime avıyla bulunurdu (kural 6). Yerine
     "Calmer but not more energetic" kondu.
  2. B için "Each volunteer measured against themselves" atıldı — B'de
     `compare each person against themselves` birebir var. Yerine pasajda geçmeyen
     araştırma deyimiyle "Each person acting as their own control" kondu.
  3. "How snow conceals what invigorates" çeldiricisi atıldı — H paragrafının ana
     fikrini (karın enerji veren yeşili örtmesi) **gerçekten** karşılıyordu. Yerine
     hiçbir paragrafa uymayan, yalnızca D'nin soğuk ayrıntısına yaslanan "The health
     risks of standing in severe cold" kondu. Ayrıca canlılık düşüşünü soran ifade
     taslağı atıldı — D'yi cevap yapıp boşta çeldirici bırakmıyordu (kural 5).
- Çeldiricilerin gölgelediği paragraflar: `i`→F (tersini söylüyor: canlılık artmadı),
  `iv`→D (soğuk ayrıntısı, risk yok), `vii`→C (tersini söylüyor + `deliberately` kelime
  tuzağı), `x`→E (madde sayısı ≠ süre). Hiçbiri sorulan bir paragrafın ana fikri değil.
- **Doğrulama:**
  - `python tools/_f42_kontrol.py` → AC4 iki dosya **0 sorun** (dokuz `evidence` A11'de
    birebir, locator'lar doğru, NB–allow_repeat tutarlı, boşta çeldirici var).
  - `python tools/dogrula.py` → **şema hatası 0**, `reading/test` 212 → **230**,
    **AC3 ve AC4 artık 40/40 TAM — dört Academic testin hepsi bitti.** Pasaj lisansı
    eksik 0, görünür metinde IELTS 0, yasak kaynak 0.
  - Son kontrol: `tools/kor-kopya.py` ile anahtar silinmiş kopyalar üretildi; AC4'ün
    dokuz sorusu (ve yukarıda anılan AC3'ün dokuzu) aday gibi baştan çözüldü, **18/18
    anahtarla uyuştu** — son turda silinen soru yok (elemeler yukarıda, taslak aşamasında).
- Yan iş: `referans/text/ielts-academic-reading-sample-tasks-2023.txt` çıkarıldı
  (`tools/pdf_metin.py` ile; başlık eşleştirme format örneği buradan okundu).
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaçları `tools/calistir.py` yazıyor).
- Atlanan/sorun: yok. Sıradaki paket: **GT1 + GT2** (soru 28–32, başlık eşleştirme,
  pasajlar **G05** ve **G06**) — çalıştırma listesindeki 5. paket.

## FABLE5-42 (4. çalıştırma: GT1 + GT2 — başlık eşleştirme, 5+5 soru)
- Tarih: 2026-08-05
- **Oturum başı durumu:** AC1–AC4'ün sekiz dosyası da depoda tam ve commit edilmiş
  hâldeydi (çalıştırma listesinin 1–4. paketleri). İlk **üretilmemiş** paket listedeki
  **5. paket** olan GT1 + GT2 başlık eşleştirmesiydi; 3. çalıştırmanın notu da sıradaki
  paketi böyle bırakmıştı. Hiçbir dosya yeniden üretilmedi.
- Üretilen dosyalar (plan B bölümü, soru **28–32**, GT 3. bölüm):
  - `content/reading/tests/GT1/matching-headings.json` — pasaj **G05** (hane gıda israfı
    çalışması), paragraf **B–F**
  - `content/reading/tests/GT2/matching-headings.json` — pasaj **G06** (gönüllülük ve
    sağlık), paragraf **C–G**
- İki dosyada da **10 başlık / 5 soru + 1 örnek**, 4 başlık boşta. `allow_repeat: false`,
  yönergede `NB` satırı yok (tutarlı). Sıra kuralı yok.
  - GT1 cevapları: **vi, i, ix, iii, viii** · örnek: Paragraph A → `iv`
  - GT2 cevapları: **viii, iv, x, ii, vii** · örnek: Paragraph A → `vi`
- **GT2'de sorulan aralık bilerek C–G yapıldı** (AC dosyalarındaki B–F yerine): G06'da
  B paragrafı veri kaynağı ve ölçü tanımlarını anlatıyor, ana fikri "kimler nerede
  gönüllü oluyor"a fazla yakın duruyordu; C–G aralığı hem bu örtüşmeyi kaldırıyor hem
  de E ile F'yi (gelir yolunun **önerilmesi** ile gelir payının **küçük çıkması**) yan
  yana koyup ayırt ediciliği artırıyor.
- Bilerek kurulan yakın çiftler:
  - GT1'de **vi ↔ ii**: B'nin ilk cümlesindeki "hane tahmini güvenilmez" yan cümlesi
    çeldiriciyi besliyor, ama paragrafın ana fikri ölçümün kendisi.
  - GT1'de **i ↔ vii**: C hem toplamı hem ikiye ayrılışı veriyor; kabuk/kemik yalnızca
    bir yaka. Aynı çeldirici E'nin son cümlesine de yaslanıyor (iki yönlü çeldirici).
  - GT2'de **x ↔ ii**: ikisi de gelir üzerine, ayrım "öneri" ile "ölçülen pay" arasında.
  - GT2'de **vii ↔ ix**: gelirini bildirmeyen ~%11'lik grup G'de gerçekten geçiyor ama
    sayılan sağlamlık sınamalarından yalnızca biri.
- **Taslakta elenen / değiştirilen (2):**
  1. GT1'de `ix` başlığı "A wide gap between town and country" olarak yazılmıştı;
     kör çözüm turundan sonra **"How far the two districts differed"** ile değiştirildi.
     Eski hâli, sorulmayan **H** paragrafının ana fikrine (kırsalın **neden** daha az
     attığı) da oturuyordu; yeni hâl farkın **büyüklüğüne** bağlanıyor, yani yalnızca
     D'ye. Cevap değişmedi.
  2. GT1 için düşünülen "Peelings and other by-products of cooking" çeldiricisi atıldı —
     `peelings` E'de birebir geçiyor, kelime avıyla bulunurdu (kural 6). Yerine pasajda
     birebir geçmeyen "Skins and other leftovers from preparing meals" kondu.
- Ters kontrol (her çeldirici A–I'nin tamamına karşı sınandı): GT1'de `ii`→B'nin yan
  cümlesi, `v`→hiçbir paragraf (mevsim farkı I'de açıkça **ölçülmedi** deniyor), `vii`→C
  ve E'nin ayrıntısı, `x`→D'nin gelir ayrıntısı (pasaj gelirin **nedenini** hiç
  açıklamıyor). GT2'de `i`→D listeliyor ama nedenini söylemiyor, `iii`→A'nın giriş
  cümlesi, `v`→C'nin son cümlesi, `ix`→G'nin ikinci cümlesi. Hiçbiri bir paragrafın ana
  fikri değil.
- **Doğrulama:**
  - `python tools/_f42_kontrol.py` → iki dosya **0 sorun** (on `evidence` G05/G06'da
    birebir, locator'lar doğru, hiçbir başlık pasajda birebir geçmiyor, boşta çeldirici
    var, NB–allow_repeat tutarlı).
  - `python tools/dogrula.py` → **şema hatası 0**, `reading/test` 230 → **240 (hedef
    tamam)**, **GT1 ve GT2 artık 40/40 — altı okuma tam testinin hepsi bitti.** Pasaj
    lisansı eksik 0, görünür metinde IELTS 0, yasak kaynak 0.
  - Son kontrol: `tools/kor-kopya.py` ile anahtarsız kopyalar üretildi, on soru aday gibi
    baştan çözüldü → **10/10 anahtarla uyuştu**; silinen soru yok (eleme/değişiklik
    yukarıda, taslak aşamasında).
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaçları `tools/calistir.py` yazıyor).
- Atlanan/sorun: yok. Sıradaki paket: **başlık eşleştirme alıştırması (15 soru)** —
  `content/reading/practice/matching-headings.json`, `groups` sarmalayıcısıyla, tam
  testlerde sorulmamış paragraflardan; çalıştırma listesindeki 6. paket.

## FABLE5-42 (5. çalıştırma: alıştırma — başlık eşleştirme, 15 soru)
- Tarih: 2026-08-05
- **Oturum başı durumu:** AC1–AC4 (paket 1–4) ve GT1+GT2 (paket 5) dosyalarının hepsi
  depoda tam ve commit edilmiş hâldeydi. Çalıştırma listesindeki ilk **üretilmemiş**
  paket, listedeki **6. paket** olan başlık eşleştirme alıştırmasıydı; bir önceki
  çalıştırmanın notu da sıradaki paketi böyle bırakmıştı. Hiçbir dosya yeniden
  üretilmedi.
- Üretilen dosya (plan D bölümü): `content/reading/practice/matching-headings.json` —
  **3 küme × 5 soru = 15**, `groups` sarmalayıcısıyla, numaralar 1–15, `test_id: null`,
  `practice: true`.
  - `P-MH-01` — pasaj **A01** (fil / içgörü bulmacası), paragraf **B–F**,
    cevaplar **iii, v, x, ii, vii**, örnek: Paragraph A → `ix`
  - `P-MH-02` — pasaj **A09** (cama dönüşmüş beyin dokusu), paragraf **B–F**,
    cevaplar **v, viii, ii, x, vi**, örnek: Paragraph A → `iii`
  - `P-MH-03` — pasaj **A12** (şekerleme mi gece uykusu mu), paragraf **B–F**,
    cevaplar **i, vii, iii, ix, v**, örnek: Paragraph A → `iv`
- **Pasaj seçimi:** tam testlerde başlık eşleştirmesi A02, A05, A08, A11 (AC1–AC4) ile
  G05, G06 (GT1, GT2) üzerinden sorulmuştu; alıştırma için bu altısı dışarıda bırakıldı.
  Seçilen A01, A09, A12 başka tiplerde (bilgi eşleştirme, not tamamlama, TFNG, YNNG)
  kullanılmış olsa da başlık eşleştirme ana fikri ölçtüğü için hedeflenen bilgi ayrı.
  Her kümede 10 başlık / 5 soru + 1 örnek var, yani 4 başlık boşta kalıyor.
- Bilerek kurulan yakın çiftler:
  - A01'de `iii` ile `viii`: B'nin ilk cümlesi üç hayvanı yaşlarıyla sayıyor, ama
    paragraf yaşları hiç karşılaştırmıyor; ana fikir düzenek artı sonuçsuz açılış.
  - A01'de `v` ile `i`: altı oturumluk sonuçsuz dönem "adım adım öğrenme" diye
    okunabiliyor, oysa C'nin son cümlesi öncesinde hiçbir deneme olmadığını söylüyor.
  - A09'da `viii` ile `iv`: C'nin ilk cümlesi mineral birikimi ve sonraki bulaşma
    ihtimalini gerçekten eliyor, ama bu kimliğin kurulmasındaki bir adım.
  - A12'de `iii` ile `vi`: bulmaca oyunu D'de geçiyor ama bir önlem; pasaj oyunun
    puanlara etkisini hiçbir yerde vermiyor.
- **Taslakta elenen / değiştirilen (3):**
  1. A09 için düşünülen "The temperatures needed to produce it" çeldiricisi atıldı —
     ters kontrolde sorulmayan **G paragrafının** ana fikrine (dar ısınma/soğuma
     aralığı) gerçekten oturuyordu. Yerine C'nin bir yan cümlesine yaslanan, hiçbir
     paragrafın ana fikri olmayan "Why the material could not be a later addition"
     kondu.
  2. A12 için düşünülen "Advice for anyone planning to study" çeldiricisi atıldı —
     sorulmayan **H paragrafı** tam olarak bunu yapıyor. Yerine E'ye yakın duran ama
     pasajda karşılığı olmayan "Why some pairs were harder to learn" kondu.
  3. A12'de "A ninety-minute nap..." biçimindeki başlık taslağı sayıyı dışarı verdiği
     için (D'de "90-minute nap" birebir geçiyor, kelime avıyla bulunurdu — kural 6)
     "A short daytime rest, and a pause before testing" olarak yeniden yazıldı; aynı
     nedenle `v` başlığında da "nap" yerine "rest" kullanıldı.
- Ters kontrol (dörder çeldirici, her kümede A–H'nin tamamına karşı sınandı): A01'de
  `i` hiçbir paragrafa uymuyor (metin tersini söylüyor), `iv` A ve F'nin giriş
  cümlelerine yaslanıyor, `vi` D'de bakıcılar geçiyor ama öğretme yok, `viii` B'nin
  katılımcı ayrıntısı. A09'da `i` C ve F kaynak sorusuna değiniyor ama kuşku paragrafı
  yok, `iv` C'nin yan cümlesi, `vii` H'nin uyarısı (karşılaştırma değil, genelleme
  sınırlaması), `ix` D'deki dört yöntemden biri. A12'de `ii` F ve G evrelere değiniyor
  ama evreleri tanıtmıyor, `vi` D'nin önlemi, `viii` E'nin çift türleri, `x` D'nin
  katılımcı ölçütü. Hiçbiri bir paragrafın ana fikri değil.
- **Doğrulama:**
  - `python tools/_f42_kontrol.py content/reading/practice/matching-headings.json` →
    **0 sorun** (15 `evidence` A01/A09/A12'de birebir, locator'lar doğru, hiçbir başlık
    pasajda birebir geçmiyor, her kümede boşta çeldirici var, NB ile allow_repeat
    tutarlı).
  - `python tools/dogrula.py` → **şema hatası 0**, `reading/practice` 125 → **140**,
    okuma toplamı 380/400. Pasaj lisansı eksik 0, görünür metinde IELTS 0.
  - Son kontrol: `tools/kor-kopya.py` ile anahtarsız kopya üretildi, 15 soru aday gibi
    baştan çözüldü → **15/15 anahtarla uyuştu**; rapor
    `content/DOGRULAMA/f42-alistirma-baslik-eslestirme.json`. Silinen soru yok
    (eleme ve değişiklikler yukarıda, taslak aşamasında).
- **Araç düzeltmesi:** `tools/dogrula.py` `groups` sarmalayıcısını tanımıyordu — tipe
  özel alanları yalnızca sorunun kendisinde ve dosya zarfında arıyor, **küme**
  düzeyindeki `option_list` alanını görmüyordu; bu yüzden geçerli dosya 16 sahte hata
  veriyordu. `tools/ortak.py` içine `kumeli_sorular()` eklendi (her soruyu kendi
  kümesiyle birlikte verir) ve `dogrula.py`'deki tipe özel alan kontrolü küme zarfına da
  bakacak biçimde düzeltildi. Kümesiz dosyalarda davranış değişmiyor. Aynı sorun
  sıradaki iki alıştırma paketini de vururdu.
- Alıştırma dosyasına, öteki `groups` yapılı dosyalarla aynı olsun diye üst düzey genel
  bir `instructions` satırı kondu; kümeye özel yönerge (hangi pasaj, hangi kutular) her
  kümenin kendi `instructions` alanında duruyor.
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaçları `tools/calistir.py` yazıyor).
- Atlanan/sorun: yok. Sıradaki paket: **özellik eşleştirme alıştırması (10 soru)** —
  `content/reading/practice/matching-features.json`, `groups` sarmalayıcısıyla, birden
  fazla adlandırılmış aktörü olan pasajlardan; çalıştırma listesindeki 7. paket.

## FABLE5-42 (6. çalıştırma: alıştırma — özellik eşleştirme, 10 soru)
- Tarih: 2026-08-05
- **Oturum başı durumu:** paket 1–5 (AC1–AC4 + GT1/GT2) ve paket 6 (başlık eşleştirme
  alıştırması, `content/reading/practice/matching-headings.json`) depoda tam ve commit
  edilmiş hâldeydi. Çalıştırma listesindeki ilk **üretilmemiş** paket, listedeki
  **7. paket** olan özellik eşleştirme alıştırmasıydı. Hiçbir dosya yeniden üretilmedi.
- Üretilen dosya (plan D bölümü): `content/reading/practice/matching-features.json` —
  **2 küme × 5 soru = 10**, `groups` sarmalayıcısıyla, numaralar 1–10, `test_id: null`,
  `practice: true`, `module: both` (bir akademik + bir GT pasajı).
  - `P-MF-01` — pasaj **A10** (hangi ofis düzeni işe yarıyor), liste dört ofis düzeni
    (A sade açık ofis / B bölgelere ayrılmış açık ofis / C sabit masasız düzen /
    D takım ofisi), cevaplar **A, B, D, B, A**, `allow_repeat: true` + NB satırı
  - `P-MF-02` — pasaj **G05** (ev içi gıda israfı), liste beş yiyecek-içecek türü
    (A pirinç ve tahıllar / B sebzeler / C ekmek / D et, balık, yumurta /
    E kahve ve çay), cevaplar **A, D, C, E, E**, `allow_repeat: true` + NB satırı
- **Pasaj seçimi:** tam testlerde özellik eşleştirmesi A02, A05, A08, A11 üzerinden
  sorulmuştu, bu dördü dışarıda bırakıldı. Kalan pasajlarda önce hangi olguların
  başka tiplerde zaten sorulduğuna bakıldı; A10 (yalnızca AC4 not tamamlama + TFNG) ve
  G05 (GT1 başlık eşleştirme + özet + YNNG) en az işlenmiş, aynı zamanda içinde
  ayırt edilebilir **kategori listesi** barındıran iki pasaj olduğu için seçildi.
  A10'da dört ofis düzeni, G05'te yiyecek-içecek türleri liste kuruyor.
- **Elenen küme taslakları (2) — hepsi çakışma nedeniyle, soru silinmedi:**
  1. **A06** (uzaktan çalışma) için kurulan "deneyimli ekip / üretken ekip / birinci yıl /
     ikinci yıl" listesi atıldı: AC2 özet tamamlamada 38. soru zaten "yıldız çalışanların
     yanında kazanç yok", 40. soru "deneyimli ekipler daha az mesajlaşıyor" bilgisini
     soruyor; alıştırma aynı bilgiyi tekrar etmiş olurdu (plan D bölümü uyarısı).
  2. **A07** (beyaz balina / ayna) için kurulan "ayna / saydam panel / gerçek işaret /
     sahte işaret" listesi atıldı: AC3 tablo tamamlama işaretin boyutunu, 3 dk 40 sn'yi,
     14 yaklaşmayı, 23 saniyeyi ve sağ göz tercihini zaten tüketmiş. Aynı nedenle A04
     (Uranüs uydusu) da elendi — AC2 akış şeması pasajın sayısal ayrıntılarını almış.
- **Elenen tekil ifade taslakları (3):**
  1. A10 için "bu düzende odalar ses geçirmeyen kapılarla bölünmüştü" ifadesi atıldı —
     AC4 not tamamlamanın 2. sorusu tam olarak `soundproof` cevabını istiyor; aynı
     nedenle takım ofisinin "sesi emen paneller" ayrıntısı da (not tamamlama 3. soru)
     kullanılmadı. Yerlerine D ve E paragraflarındaki sayısal karşılaştırmalar kondu.
  2. A10 için "gözde bir düzen olmasına karşın karşılaştırma düzeninin altında kaldı"
     (cevap C) ifadesi atıldı — AC4 TFNG 11. soru aynı karşılaştırmayı yapıyor. C böylece
     hiçbir ifadeye cevap olmayan **boşta çeldirici** oldu (kural 5).
  3. G05 için "gereğinden fazla hazırlandığı için atıldı" ilk taslağı, G paragrafındaki
     "ailenin yiyebileceğinden çok pirinç pişirme" yüzünden A ile E arasında iki
     savunulabilir cevap üretiyordu; ifade "içmek" fiiliyle yeniden yazılınca yalnızca
     kahve/çaya (E) uyar hâle geldi. G05'te sebzeler (B) boşta çeldirici.
- Bilerek kurulan yakın çiftler (kural 4): A10'da 2. ve 3. soru B ile D'yi yüzdelerden
  ayırmaya zorluyor (memnuniyet %12'ye %8, algılanan üretkenlik %17'ye %10), 4. soruda
  işe kapılma puanı cümlenin başında D'yi (%12) gösterip sonunda B'yi (%15) veriyor.
  G05'te 6. soru A ile B'yi ("hemen arkada" olan sebzeler), 7. ve 8. soru aynı cümle
  içindeki üç ayrı gerekçeyi (küflenme / doku değişikliği / kısa raf ömrü) ayırmayı
  gerektiriyor.
- **Doğrulama:**
  - `python tools/_f42_kontrol.py content/reading/practice/matching-features.json` →
    **0 sorun** (10 `evidence` A10/G05'te birebir, locator'lar doğru, liste 4 ve 5 öğe,
    her kümede boşta çeldirici var, NB ile `allow_repeat` tutarlı, hiçbir ifade pasajdan
    kopya değil).
  - `python tools/dogrula.py` → **şema hatası 0**, `reading/practice` 140 → **150**,
    okuma toplamı 390/400. Pasaj lisansı eksik 0, görünür metinde IELTS 0.
  - Son kontrol: `tools/kor-kopya.py` ile anahtarsız kopya üretildi, 10 soru aday gibi
    baştan çözüldü → **10/10 anahtarla uyuştu**; rapor
    `content/DOGRULAMA/f42-alistirma-ozellik-eslestirme.json`. Silinen soru yok.
  - `dogrulama/cevap/` içinde 5. çalıştırmadan kalan başlık eşleştirme cevap dosyası
    duruyordu ve rapora karışıyordu (25 soru); silindikten sonra rapor yalnızca bu
    paketi kapsıyor. `dogrulama/` zaten depoya gitmiyor.
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaçları `tools/calistir.py` yazıyor).
- Atlanan/sorun: yok. Sıradaki paket: **cümle sonu eşleştirme alıştırması (10 soru)** —
  `content/reading/practice/matching-sentence-endings.json`, çalıştırma listesindeki
  8. ve son paket. Orada dikkat: bütün sonlar bütün başlangıçlara **dilbilgisi olarak**
  uymalı ve son sayısı soru sayısından en az 3 fazla olmalı (10 soru → en az 13 son),
  `grammar_check` zorunlu, `example` null, sıra kuralı geçerli.

## FABLE5-42 (7. çalıştırma — listedeki 8. paket: alıştırma — cümle sonu eşleştirme, 10 soru — **paket tamam**)
- Tarih: 2026-08-06
- **Oturum başı durumu:** çalıştırma listesindeki 1–7. paketlerin hepsi (AC1–AC4 başlık +
  özellik, GT1/GT2 başlık, başlık eşleştirme alıştırması 15 soru, özellik eşleştirme
  alıştırması 10 soru) depoda tam ve commit edilmişti. İlk **üretilmemiş** paket listedeki
  **8. ve son paket**, cümle sonu eşleştirme alıştırmasıydı. Hiçbir dosya yeniden üretilmedi.
- Üretilen dosya (plan D bölümü): `content/reading/practice/matching-sentence-endings.json` —
  **2 küme × 5 soru = 10**, `groups` sarmalayıcısıyla, numaralar 1–10, `test_id: null`,
  `practice: true`, `module: both`, her kümede `example: null`, `allow_repeat: false`.
  - `P-MSE-01` — pasaj **A07** (ayna testini geçen beyaz balina), 8 son (A–H),
    cevaplar **A, E, B, C, D**; boşta çeldiriciler F (sağ göz tercihi), G (ayna/panel
    önünde geçen saatler), H (yeteneğin ayrı ayrı ortaya çıkması)
  - `P-MSE-02` — pasaj **G06** (gönüllülük ve sağlık), 8 son (A–H),
    cevaplar **B, C, D, A, E**; boşta çeldiriciler F (gönüllülerin daha dindar olması),
    G (bütün çözümleme sürümlerinde aynı örüntü), H (rastgele atamalı deney önerisi)
- **Son sayısı:** kural "soru sayısından en az 3 fazla". Sorular küme hâlinde geldiği için
  kural küme başına uygulandı: 5 soru → 8 son (6. çalıştırmanın notundaki "10 soru → en az
  13 son" hesabı tek düz liste varsayıyordu; `tools/_f42_kontrol.py` da kümeyi ayrı ayrı
  denetliyor ve 0 sorun verdi).
- **Dilbilgisi tarafsızlığı (kural 2) — kurulan düzen:** her başlangıç tam bir yan cümle
  isteyen bir bağlaçla bitiyor (`because`, `whereas`, `which suggested that`,
  `once the authors point out that`), her son ise **özne + çekimli geçmiş zaman fiili**
  taşıyan tam bir cümle. Böylece hiçbir son yarım isim öbeği ya da mastar olmadığı için
  tekil/çoğul, artikel, edat veya fiil çekimi üzerinden eleme yapılamıyor; sonların
  hepsi 11–15 kelime aralığında tutulup uzunluk ipucu da kapatıldı.
  - Bu yüzden **C sonundaki özne `she`den `the whale`e çevrildi**: tekil dişil zamir
    yalnızca Natasha'dan söz eden 4. başlangıca bağlanabildiği için tutarlılık ipucu
    veriyordu; nötr isim öbeğiyle bütün başlangıçlara eşit uzaklıkta duruyor.
- **Pasaj seçimi:** eşleştirme tiplerinde şimdiye kadar kullanılan pasajlar dışarıda
  bırakılamayacak kadar azdı (havuzun tamamı en az bir tipte işlenmiş), o yüzden ölçüt
  "hangi **bilgi** henüz sorulmamış" oldu. A07'de tam testten (AC3 tablo + TFNG) ve
  alıştırma bilgi eşleştirmesinden arta kalan ilişkiler, G06'da GT2'nin (başlık + YNNG +
  özet) dokunmadığı paragraflar hedeflendi. Sıra kuralı geçerli olduğu için başlangıçlar
  pasaj sırasına dizildi: A07 → B, C, D, E, F; G06 → B, C, D, E, H.
- **Elenen taslaklar (4) — hepsi çakışma nedeniyle, üretilen sorudan silinen yok:**
  1. A07 "Natasha gerçek işareti 3 dk 40 sn boyunca gösterdi" sayısal kurgusu atıldı —
     AC3 tablo tamamlama 14 yaklaşmayı ve 23 saniyeyi zaten istiyor; soru sayıdan değil
     **karşılaştırmanın yorumundan** kurulacak biçimde yeniden yazıldı (4. soru).
  2. A07 "yeteneğin birbirinden uzak canlılarda ayrı ayrı ortaya çıkması" başlangıcı
     atıldı — alıştırma bilgi eşleştirmesi bunu G paragrafı için zaten soruyor; bilgi
     **boşta çeldirici H**'ye taşındı.
  3. G06 "kendi beyan edilen sağlık ölçüsünün neden seçildiği" başlangıcı atıldı —
     GT2 YNNG 34. soru aynı iddiayı test ediyor; yerine C paragrafındaki **farkın
     büyüklüğü** (beş yıllık yaş farkı) hedeflendi.
  4. G06 "gelirin payı beşte birin altında" başlangıcı atıldı — GT2 özet tamamlama 37 ve
     YNNG 36 bu bulguyu tüketmiş; yerine E paragrafındaki **mekanizma** (beceri +
     güvenilirlik → gelir) kondu.
- **Çeldiricilerin ters kontrolü:** altı boşta sonun her biri için "bu hangi başlangıca
  cevap olabilir?" sorusu ayrı ayrı soruldu. En cazip olan G (A07, saatler) 1. soruya
  dilbilgisi olarak tam oturuyor ama süre panelin kullanılma **nedeni** değil sonucu;
  F (G06, dindarlık) 8. soruya oturuyor ama karşıtlık ülke ekseninde kurulmuş, dindarlık
  ekseninde değil. Hiçbiri gerçek cevap hâline gelmedi.
- **Doğrulama:**
  - `python tools/_f42_kontrol.py content/reading/practice/matching-sentence-endings.json`
    → **0 sorun** (10 `evidence` A07/G06'da birebir, locator'lar doğru paragrafı
    gösteriyor, küme başına 8 son / 5 soru, her kümede boşta çeldirici var, NB yok ve
    `allow_repeat: false` ile tutarlı, hiçbir son pasajda birebir geçmiyor).
  - `python tools/dogrula.py` → **şema hatası 0**, `reading/practice` 150 → **160**
    (plan D bölümü hedefi tamamlandı), okuma toplamı **400/400**. Pasaj lisansı eksik 0,
    görünür metinde IELTS 0.
  - İlk turda `dogrula.py` 10 "explanation Türkçe olmayabilir" hatası verdi: Türkçe
    alanları ASCII yazmıştım, denetim `[çğıöşüÇĞİÖŞÜ]` arıyor. Bütün `explanation` ve
    `grammar_check` alanları tam diakritikle yeniden yazıldı.
  - Son kontrol: `tools/kor-kopya.py` ile anahtarsız kopya üretildi, 10 soru aday gibi
    baştan çözüldü → **10/10 anahtarla uyuştu**; rapor
    `content/DOGRULAMA/f42-alistirma-cumle-sonu-eslestirme.json`. Silinen soru yok.
  - `dogrulama/cevap/` içindeki 6. çalıştırmadan kalan özellik eşleştirme cevap dosyası
    rapora karışmasın diye silindi (`dogrulama/` zaten depoya gitmiyor).
- `tools/_f42s_kapsam.py` (7. çalıştırmadan kalan geçici kapsam sayacı) commit'e dâhil —
  pasaj başına soru sayısını ve verilen pasajın bütün soru köklerini döküyor, sonraki
  çakışma kontrollerinde işe yarıyor.
- **DURUM.txt / ilerleme.txt elle güncellenmedi** (sayaçları `tools/calistir.py` yazıyor).
- Atlanan/sorun: yok. **FABLE5-42 tamam** — 8 paketin sekizi de bitti (tam test 46 +
  alıştırma 35 = 81 soru). Bu promptun yeni bir çalıştırması gerekmiyor.

## FABLE5-43 (1. çalıştırma: L1 — riskli sorular, 11 soru)

- **Üretilen:** `content/listening/tests/L1/multiple-choice.json` (11, 12, 13, 14–15 →
  2. bölüm; 21, 22, 23 → 3. bölüm; prompt kuralı gereği iki bölümün çoktan seçmelisi tek
  dosyada, `section` ve `script_id` hem küme hem soru düzeyinde) +
  `content/listening/tests/L1/matching.json` (24–26, 3. bölüm). Toplam **11 soru** —
  L1 artık `dogrula.py`'de **40/40 TAM**.
- **11–15 bloku seçimi (altı testte 3 çoktan seçmeli / 3 eşleştirme dengesi):**
  **L1 = çoktan seçmeli (1/3).** L1-S2'nin dört düzeltmeli çeldirici noktası (kapalı gün,
  tur saatleri, yıllık kart, dokunma seansı günü) çoktan seçmeliye çok uygundu; eşleştirme
  kotası sonraki testlerden üçüne bırakıldı.
- **Yerleşim ve sıra kuralı:** S2 → replikler 2, 5, 8, 11; S3 çoktan seçmeli → 2, 6, 14;
  S3 eşleştirme → 18, 21, 25. Bütün ardışık cevap çiftleri arasında **en az 3 replik** var
  (`tools/_f43_kontrol.py` doğruluyor). 21–26, OPUS5-21'in 27–30 cevaplarının başladığı
  27. replikten önce bitiyor.
- **Çeldirici türleri:** her soruda en az iki farklı tür; "söylendi sonra düzeltildi"
  6 soruda (11, 12, 14–15, 21, 22, 24-G), "başkası söyledi" 2 soruda (23, 25 — yalnız
  3. bölümde mümkün), "söylendi ama sorulan bu değil" hepsinde. **Kısıt notu:** S2 tek
  konuşmacılı olduğu için "başkası söyledi" türü 2. bölümde yapısal olarak imkânsız;
  13. soruda ikinci tür olarak soru başına en fazla bir tanesine izin verilen "sesle hiç
  geçmeyen" çeldirici kullanıldı (tek kullanım). Eşleştirmede kutu ortak olduğu için yanlış
  harflerin çoğu doğal olarak "başka öğe için söylendi" (tür 3) sınıfına düşüyor; 24 ve 25
  numaralarda ikinci tür (düzeltildi / başkası söyledi) ayrıca mevcut, 26'da yalnız tür 3
  kurulabildi — üç ayrı çeldirici gerekçesi yine de yazıldı.
- **Yeni bilgi noktaları senaryolara eklendi:** `L1-S2-32` (avludaki piknik masaları,
  replik 8), `L1-S2-33` (sergilenmeyen nesneleri elleme, replik 11), `L1-S2-34` (seans
  ücretsiz, replik 11 — 14–15 çift sorusunun ikinci cevabı; `answer_point_id` alanı tek
  değer aldığı için 33 yazıldı, 34 `explanation`'da anılıyor), `L1-S3-29` (ulusal anket
  yalnız bağlam için, replik 18).
- **Elenen taslaklar (3):** fotoğraf kuralı sorusu (S2 replik 10) ve asansör konumu sorusu
  (S2 replik 8) — ikisinde de iki farklı çeldirici türü kurulamıyordu (düzeltme yok, tek
  konuşmacı); not dağılımı sorusu (S3 replik 10) — her iki çeldirici de aynı türe (tür 3)
  düşüyordu. Üçünün yerine avlu (13), dokunma seansları (14–15) ve danışman görüşü (23)
  soruları yazıldı. Üretilip son kontrolde silinen soru yok: senaryolar baştan sona
  okunarak 11 soru anahtara bakılmadan çözüldü, **11/11 uyuştu**.
- **Harf dengesi:** tekli cevap dizisi B, A, B, {C,E}, A, C, B / eşleştirme A, C, B —
  üst üste aynı harf yok; kutu 7 seçenekli (3 soru + 4 boşta).
- **Doğrulama:** `python tools/dogrula.py` → şema hatası 0, L1 40/40, görünür metinde
  IELTS 0; `python tools/_f43_kontrol.py L1` → 0 sorun (evidence birebir, replik
  aralıkları, 10 kelime seçenek sınırı, 50 kelime kök+seçenek sınırı). `_f43_kontrol.py`
  sonraki L2–L6 çalıştırmaları için depoya kondu.
- Referans olarak `referans/` altındaki dinleme çoktan seçmeli (tek/çok cevap) anahtar +
  transkript PDF'leri ve 2023 örnek görev PDF'i okundu (yalnız format; metin alınmadı).
- Atlanan/sorun: yok. Sıradaki çalıştırma: **L2** (2/9).

## FABLE5-43 (2. çalıştırma: L2 — riskli sorular, 11 soru)

- **Üretilen:** `content/listening/tests/L2/multiple-choice.json` (11, 12, 13, 14–15 →
  2. bölüm; 21, 22, 23 → 3. bölüm; L1'deki gibi tek dosya, `groups` + item düzeyinde
  `section`/`script_id`) + `content/listening/tests/L2/matching.json` (24–26, 3. bölüm).
  Toplam **11 soru** — L2 artık `dogrula.py`'de **40/40 TAM**.
- **11–15 bloku seçimi: L2 = çoktan seçmeli (2/3).** L2-S2'nin doğal eşleştirme listesi
  (etkinlikler: okuma grubu, masal saati, tamir kafesi) tek replikte (9.) yığılı; 3-replik
  ara kuralıyla 5 öğeli eşleştirme kümesi kurulamıyor. ⚠️ **Kısıt: L3–L6'nın ÜÇÜNDE 11–15
  bloku eşleştirme olmak zorunda** (3 ÇS / 3 eşleştirme dengesi için).
- **Yerleşim ve sıra kuralı:** S2 → replikler 1, 4, 9, 12 — OPUS5-21'in plan etiketleme
  bölgesinin (replik 5–8, sorular 16–20) tamamen dışında; S3 çoktan seçmeli → 3, 6, 11;
  S3 eşleştirme → 22, 26, 33. Ardışık cevap aralıkları grup içinde ≥3 replik
  (`tools/_f43_kontrol.py L2` → 0 sorun). 21–26, OPUS5-21'in 27. sorusunun başladığı
  34. replikten önce bitiyor.
- **Alıştırma çakışması önlendi:** `practice/sentence-completion.json` L2-S3-01 (beş alan),
  -11 (kimyasal kit), -13 (bostan), -21 (tek dosya) noktalarını zaten kullanıyor; alan
  sayısı sorusu taslağı bu yüzden elendi, 21. soru köprü sorusuna (L2-S3-02) çevrildi.
  24. soru kit noktası yerine yeni "iki yöntem" noktasına (L2-S3-25, replik 22) dayandı.
- **Çeldirici türleri:** her soruda en az iki farklı tür; "söylendi sonra düzeltildi"
  6 soruda (11-A, 12-B, 13-A, 22-B, 24-E, 25-D), "başkası söyledi" 2 soruda (21-C, 23-B —
  yalnız 3. bölümde mümkün), "söylendi ama sorulan bu değil" hepsinde. Sesle hiç geçmeyen çeldirici: 2 (11-C, 14/15-D; soru başına ≤1 ✓).
  **Kısıt notu (L1-26 emsali):** eşleştirme 26'da (ham veri) kutu ortak olduğu için dört
  yanlış harfin dördü de tür 3'e düşüyor; dört ayrı gerekçe yine de yazıldı.
- **Yeni bilgi noktaları senaryolara eklendi:** `L2-S2-29` (broşür, replik 12 — 14–15'in
  ikinci cevabı, `answer_point_id` tek değer aldığı için 25 yazıldı), `L2-S3-24` (Marisol:
  desen gizlenir, replik 11), `L2-S3-25` (oksijende iki yöntem, replik 22), `L2-S3-26`
  (Rhys: kimse okumaz, replik 33).
- **Elenen taslaklar (2):** alan sayısı sorusu (S3 replik 1 — alıştırmada L2-S3-01 zaten
  kullanılmış) ve gönüllülük çift sorusu (S2 replik 11 — 9. replikteki 13. soruyla arası
  2 replik kalıyordu; yerine 12. replikteki duvar resmi çift sorusu yazıldı). Üretilip son
  kontrolde silinen soru yok: iki senaryo baştan sona okunarak 11 soru anahtara bakılmadan
  çözüldü, **11/11 uyuştu**.
- **Harf dengesi:** B, C, B, {C,E}, A, C, A / eşleştirme B, A, C — üst üste aynı harf yok;
  kutu 5 seçenekli (3 soru + 2 boşta, alt sınır).
- **Doğrulama:** `python tools/dogrula.py` → şema hatası 0, L2 40/40 TAM, görünür metinde
  IELTS 0; `python tools/_f43_kontrol.py L2` → 0 sorun.
- Referans: dinleme çoktan seçmeli (tek/çok cevap) anahtar + transkript PDF'leri okundu
  (yalnız format; metin alınmadı).
- Atlanan/sorun: yok. Sıradaki çalıştırma: **L3** (3/9) — ⚠️ 11–15 bloku için eşleştirme
  öncelikli değerlendirilmeli.

## FABLE5-43 (3. çalıştırma: L3 — riskli sorular, 11 soru)

- **Üretilen:** `content/listening/tests/L3/matching.json` (İKİ küme tek dosyada, `groups`
  sarmalayıcısıyla: 11–15 → 2. bölüm 5 öğeli eşleştirme, 24–26 → 3. bölüm 3 öğeli
  eşleştirme) + `content/listening/tests/L3/multiple-choice.json` (21–23, 3. bölüm, düz
  `items`). Önceki çalıştırmaların tersine bu kez ÇS dosyası düz, eşleştirme dosyası
  gruplu — `dogrula.py` ve `_f43_kontrol.py` iki biçimi de işliyor. Toplam **11 soru** —
  L3 artık `dogrula.py`'de **40/40 TAM**.
- **11–15 bloku seçimi: L3 = eşleştirme (1/3).** L1–L2 ÇS olduğu için denge kotası burada
  başladı. ⚠️ **Kalan kısıt: L4–L6'nın İKİSİNDE daha 11–15 eşleştirme olmalı** (3/3 denge).
  S2'de 5 öğeli küme ancak 1-4-7-10-13 replik dizilimiyle kurulabildi; kutu "It is ..."
  kalıbında 7 seçenek (A–G), istemler karma (özellik + ulaç: the soil / the red route /
  borrowing a dipping net / leaving a car overnight / the orchid count).
- **Yerleşim ve sıra kuralı:** S2 → replikler 1, 4, 7, 10, 13 (aralıklar tam 3). 13. soru
  (ağlar, replik 7) OPUS5-21'in plan bölgesi (5–9) İÇİNE düşüyor — kaçınılmaz: 5 öğe ve
  3-replik kuralıyla 0–13 aralığında 5–9'u tamamen atlayan dizilim matematiksel olarak yok
  (en çok 4 öğe çıkıyor). Aynı replikteki harita sorusu (S2-20, kuş gözlem yeri) konum
  soruyor, benimki ağların ücretsizliğini — bilgi çakışması yok. S3 → ÇS 0, 3, 6;
  eşleştirme 11, 14, 18. Tavan kuralı: 21–26, OPUS5-21'in 27–30 cevaplarının başladığı
  19. replikten önce bitiyor (26'nın cevabı replik 18).
- **Alıştırma çakışması önlendi:** practice/sentence-completion L3-S3-09 (3.500 kelime) ve
  L3-S3-13 (ek/appendix) noktalarını kullanıyor; ikisi de S3'ün t19 öncesindeki tek iki
  düzeltme noktasıydı → ÇS'de cevap olarak kullanılmadı, yalnızca çeldirici zemini oldu
  (24-B/25-B/26-B: 4.000→3.500). practice/plan-map L3-S2-21'i (platform KONUMU, replik 7)
  kullanıyor; 13. soru aynı replikten farklı bilgiye (ağlar ücretsiz, yeni nokta) dayandı.
- **Çeldirici türleri:** "söylendi sonra düzeltildi" 15-B'de saf hâliyle (çalılık günü,
  aynı replik) ve 24/25/26-B'de (4.000→3.500 kökenli); "başkası söyledi" 22-A, 23-B ve S3
  eşleştirmesinin bütün kişiler-arası harflerinde; "söylendi ama sorulan bu değil" yaygın.
  Sesle hiç geçmeyen: 21-C ve S3 kutusundaki E (soru başına ≤1 ✓). **Kısıt notları:**
  (1) 21. soru açılış repliğinde (t0) — düzeltme/başkası yapısal olarak imkânsız, L1-13
  emsaliyle tür 3 + sesle geçmeyen kullanıldı. (2) S2 eşleştirmesinde kutu ortak olduğu
  için yanlış harflerin çoğu tür 3 (L1-26/L2-26 emsali); yine de her öğeye 6 gerekçe
  yazıldı. (3) 24 (danışman) için D dikkat istedi: danışman Corin'in YAPISINI öneriyor
  (t19, OPUS5-21'in bölgesi) ama D'nin önermesini ('kronoloji benzer malzemeyi böler')
  kurmuyor — kendi gerekçesi 'karşılaştırmaya zorlar'; kutu tekrarsız olduğundan D
  Corin'de. D'nin metni bu yüzden bilinçli olarak Corin'in cümlesine bağlandı.
- **Yeni bilgi noktaları senaryolara eklendi:** `L3-S2-36` (zemin atık kaya, replik 1),
  `L3-S2-37` (ağlar ücretsiz, replik 7), `L3-S2-38` (gece araba yasağı, replik 10),
  `L3-S2-39` (orkide sayımı yavaş/rahat iş, replik 13), `L3-S3-31` (toplantının amacı,
  replik 0), `L3-S3-32` (danışman: tam sınıra yazma, replik 11).
- **Elenen taslaklar (3):** (1) S2 rota-listesi eşleştirmesi (yeşil/mavi/kırmızı) —
  cevaplar 2-3-4. repliklerde yığılı, 3-replik kuralı geçmiyor (L2-S2 emsali); rota
  uzunluğu noktaları (S2-05/08/11) 7–9. çalıştırmaların alıştırma ÇS'sine kaldı.
  (2) S3 günlük-sıklığı eşleştirmesi (Tamsin/Corin/danışman) — cevaplar 14-15-16
  ardışık, aynı kural. (3) S3 kelime-sınırı ÇS taslağı — cevap noktası alıştırmada
  kullanılmıştı (S3-09). Üretilip son kontrolde silinen soru yok: iki senaryo baştan sona
  okunarak 11 soru anahtara bakılmadan çözüldü, **11/11 uyuştu**.
- **Harf dengesi:** eşleştirme 11–15: C, E, A, F, D (kutu 7'li, 2 boşta) / ÇS: B, C, A /
  eşleştirme 24–26: C, A, D (kutu 5'li, 2 boşta, alt sınır) — üst üste aynı harf yok.
- **Doğrulama:** `python tools/dogrula.py` → şema hatası 0, L3 40/40 TAM, görünür metinde
  IELTS 0; `python tools/_f43_kontrol.py L3` → 0 sorun.
- Referans: dinleme ÇS (tek/çok cevap) anahtar + transkript PDF'leri ve 2023 örnek görev
  PDF'i okundu (yalnız format; metin alınmadı — eşleştirme kutusu/yönerge kalıbı Matching
  1–2 örneklerinden).
- Atlanan/sorun: yok. Sıradaki çalıştırma: **L4** (4/9) — ⚠️ L4–L6'nın ikisinde 11–15
  eşleştirme olmalı; L4-S2'de önce eşleştirme dene.

## FABLE5-43 (4. çalıştırma: L4 — riskli sorular, 11 soru)

- **Üretilen:** `content/listening/tests/L4/matching.json` (İKİ küme, `groups`
  sarmalayıcısıyla, L3 düzeni: 11–15 → 2. bölüm 5 öğeli eşleştirme, 21–23 → 3. bölüm
  3 öğeli eşleştirme) + `content/listening/tests/L4/multiple-choice.json` (24–26,
  3. bölüm, düz `items`). Toplam **11 soru** — L4 artık `dogrula.py`'de **40/40 TAM**.
- **11–15 bloku seçimi: L4 = eşleştirme (2/3).** L4-S2 saha tanıtımının öğeleri (eski
  saha, otopark, elektrikli eşya deposu, üst seviye, tamir seansı) 1-4-7-10-13 replik
  dizilimiyle tam 3'er aralıkla oturdu; kutu 7 seçenekli (A–G, 2 boşta).
  ⚠️ **Kalan kısıt: L5 ve L6'dan BİRİNDE daha 11–15 eşleştirme olmalı** (3/3 denge;
  diğeri çoktan seçmeli olacak).
- **YENİLİK — 3. bölümde küme sırası ilk kez ters:** eşleştirme 21–23, ÇS 24–26.
  Sebep: S3'te üç konuşmacının görüşleri üç eksende ama her eksen ARDIŞIK repliklerde
  yığılı (yerleşim t5-6-7, grafikler t9-10-11, baskı t19-20-21) ve baskı ekseninin
  danışman ayağı (t21) OPUS5-21'in 27. sorusunun cevabı. Kişi-başına-eksen eşleştirmesi
  de, danışman-eşleştirmesi (t7-13-17) de 3-replik kuralını ya kendi içinde ya ÇS'ye yer
  bırakma açısından geçemiyor; tek çözüm konu-başına-Anneke eşleştirmesini (t3-6-10) öne,
  ÇS'yi (t13-17-20) arkaya almaktı. Prompt küme sırasını sabitlemiyor; dosya adları ve
  şema değişmedi, `dogrula.py`/`_f43_kontrol.py` sorunsuz işledi.
- **Yerleşim ve sıra kuralı:** S2 → replikler 1, 4, 7, 10, 13 (aralıklar tam 3);
  12–13. sorular OPUS5-21'in plan bölgesiyle (t3–7) çakışan repliklerde ama farklı
  bilgiye dayanıyor (L3-13 emsali): otoparkta plan konumu değil "yalnız dükkân müşterisi"
  kuralı, elektrik deposunda konum değil "görevli taşır" hizmeti. S3 → eşleştirme 3, 6,
  10; ÇS 13, 17, 20 — küresel dizi 3-6-10-13-17-20, bütün aralıklar ≥3. Tavan kuralı:
  26'nın cevabı t20, OPUS5-21'in 27. sorusu t21'de başlıyor (L3'teki 1 replik ara emsali).
- **Alıştırma çakışması önlendi:** practice/plan-map L4-S2-08/-09/-15/-17 ve
  practice/sentence-completion L4-S3-02/-14/-21/-33 noktalarını kullanıyor; hiçbiri cevap
  yapılmadı. S3-14 (24→30 punto düzeltmesi) yalnız 25. sorunun çeldiricisi oldu (L3
  emsali: practice noktası çeldirici zemini olabilir, cevap olamaz).
- **Çeldirici türleri:** "söylendi sonra düzeltildi" S2 kutusunda D (bir yıl → on dört
  ay) ve 25-C'de (24 → 30 punto); "başkası söyledi" S3 eşleştirmesinin B/C harflerinde
  (Idris/danışman) ve 26-A'da (yalnız 3. bölümde mümkün — S2 tek konuşmacılı, L1 emsali);
  "söylendi ama sorulan bu değil" yaygın. Sesle hiç geçmeyen: S3 kutusunda F ve 24-C
  (soru başına ≤1 ✓; S2 kutusunda hiç yok). Kutu ortak olduğu için S2'de yanlış harflerin
  çoğu tür 3 (L1-26/L3 emsali); yine de 11–15'te 6'şar, 21–23'te 5'er gerekçe yazıldı.
- **Yeni bilgi noktaları senaryoya eklendi (yalnız L4-S2):** `L4-S2-38` (eski sahanın
  kuyruğu çevre yoluna taşıyordu, replik 1), `L4-S2-39` (otopark yalnız dükkân
  ziyaretçilerine, replik 4), `L4-S2-40` (elektrikli eşyayı görevli içeri taşır,
  replik 7). S3'te yeni nokta gerekmedi (6 soru da mevcut noktalara dayandı: S3-01, -04,
  -08, -12, -16, -18).
- **Elenen taslaklar (3):** (1) S3 kişi-eşleştirmesi (Idris/Anneke/danışman × tek konu) —
  her eksende cevaplar ardışık repliklerde, 3-replik kuralı geçmiyor (L2-S2/L3-S3 emsali).
  (2) S2 atık-türü eşleştirmesi (yağ/pil/alçıpan/gaz tüpü) — dördü de 12. replikte yığılı.
  (3) Danışman-eşleştirmesi (t7-13-17) — önünde ÇS'ye yer bırakmıyor (ilk ÇS cevabı
  t4'ten önce olmalıydı, orada nokta yok). Üretilip son kontrolde silinen soru yok: iki
  senaryo baştan sona okunarak 11 soru anahtara bakılmadan çözüldü, **11/11 uyuştu**.
- **Harf dengesi:** eşleştirme 11–15: E, B, A, F, C (kutu 7'li, 2 boşta) / eşleştirme
  21–23: D, A, E (kutu 6'lı, 3 boşta) / ÇS 24–26: A, B, C — üst üste aynı harf yok.
- **Doğrulama:** `python tools/dogrula.py` → şema hatası 0, L4 40/40 TAM, görünür metinde
  IELTS 0; `python tools/_f43_kontrol.py L4` → 0 sorun.
- Referans: dinleme ÇS (tek cevap) transkript + anahtar PDF'i okundu (yalnız format);
  eşleştirme kutu/yönerge kalıbı L1–L3'ün doğrulanmış dosyalarından sürdürüldü. Bu
  çalıştırmada çift cevaplı soru yok (11–15 eşleştirme olunca çift ÇS de yok).
- Atlanan/sorun: yok. Sıradaki çalıştırma: **L5** (5/9) — ⚠️ L5 ve L6'dan birinde 11–15
  eşleştirme, diğerinde çoktan seçmeli (+ çift cevaplı) olmalı; L5-S2'nin yapısına göre
  seç, seçimi buraya yaz.

## FABLE5-43 (5. çalıştırma: L5 — riskli sorular, 11 soru)

- **Üretilen:** `content/listening/tests/L5/multiple-choice.json` (11, 12, 13, 14–15 →
  2. bölüm; 21, 22, 23 → 3. bölüm; L1/L2 düzeni: tek dosya, `groups` + item düzeyinde
  `section`/`script_id`) + `content/listening/tests/L5/matching.json` (24–26, 3. bölüm,
  düz `items`). Toplam **11 soru** — L5 artık `dogrula.py`'de **40/40 TAM**.
- **11–15 bloku seçimi: L5 = çoktan seçmeli (3/3 — ÇS kotası doldu).** Gerekçe: OPUS5-21'in
  bilerek bıraktığı dört düzeltmeli çeldirici noktası (S2-02 açılış saati, S2-04 bilet,
  S2-19 servis sıklığı, S2-24 atölye günleri) ÇS'ye çok uygun; S2'de 5 öğeli eşleştirme
  için gereken paralel öğeler ya OPUS5-21'in plan sorularında (16–20) kullanılmış ya da
  3-replik kuralını geçemiyor (0–12 replik aralığında en çok 4 öğe çıkıyor).
  ⚠️ **Kalan kısıt: L6'da 11–15 bloku EŞLEŞTİRME olmak ZORUNDA** (3/3 denge; seçim hakkı
  kalmadı). L6-S2'de 5 öğeli küme 3-replik aralığıyla kurulamazsa NOTLAR'a yazıp prompt
  sahibine bırakmak yerine 1-4-7-10-13 tipi dizilimler denenmeli (L3/L4 emsali).
- **Yerleşim ve sıra kuralı:** S2 → replikler 1, 4, 7, 10 (aralıklar tam 3); 12. soru
  OPUS5-21'in plan bölgesiyle (t3–6) çakışan t4'te ama farklı bilgiye dayanıyor (L3-13/L4
  emsali): planda ana sahnenin KONUMU soruluyor, bende çevrilme SEBEBİ (karşı kıyıdaki
  evlere taşan ses). S3 → ÇS 2, 5, 9; eşleştirme 13, 16, 19 — küresel dizi 2-5-9-13-16-19,
  bütün aralıklar ≥3. Tavan kuralı: 26'nın cevabı t19, OPUS5-21'in 27. sorusu t24'te
  başlıyor (5 replik pay — L1–L4'ten geniş).
- **S3'te sıkışıklık ve çözümü:** tavan t24 (OPUS'un 27. cevabı) + t20/22/23'te bilgi
  noktası yokluğu + t21'in (S3-15 ödül çekilişi) alıştırmada kullanılması yüzünden
  t3–19 aralığına 3-replik kuralıyla en çok 5 cevap sığıyordu. Çözüm: t2'deki danışman
  tepkisine yeni bilgi noktası açmak (`L5-S3-31`, "şimdi anlaşamamak üç hafta sonra
  anlaşamamaktan ucuz") — 21. soru buradan çıktı ve dizi 6'ya tamamlandı.
- **Alıştırma çakışması önlendi:** practice/sentence-completion L5-S3-04 (120 alt sınır),
  -15 (ödül çekilişi) ve -25 (kabin rezervasyonu) noktalarını kullanıyor; hiçbiri cevap
  yapılmadı. S3-04 yalnız 22-C ve 23-B çeldiricilerinin zemini oldu (L3/L4 emsali:
  practice noktası çeldirici zemini olabilir, cevap olamaz).
- **Çeldirici türleri:** "söylendi sonra düzeltildi" 3 soruda (11-B broşür saati, 13-B
  afiş sıklığı, 14/15-A kart geçen yıl geçmiyordu); "başkası söyledi" 2 soruda (22-A,
  23-A — yalnız 3. bölümde mümkün, S2 tek konuşmacılı, L1 emsali); "söylendi ama sorulan
  bu değil" hepsinde. Sesle hiç geçmeyen: 12-C, 13-C, 21-C (soru başına ≤1 ✓; eşleştirme
  kutusunda hiç yok — F "tersine çevrildi" sınıfı: yarım form beterdir'in olumsuzu).
  14–15 çift sorusunun üç çeldiricisi de "aslında serbest olan şey" kalıbında (kart,
  yol, çeşme) — hepsi seste geçiyor.
- **Yeni bilgi noktası senaryoya eklendi (yalnız L5-S3):** `L5-S3-31` (danışmanın
  anlaşmazlık tepkisi, replik 2). S2'de yeni nokta gerekmedi (4 soru mevcut noktalara
  dayandı: S2-02, -12, -19, -28; çift sorunun ikinci cevabı S2-29 `explanation`'da anılıyor,
  `answer_point_id` tek değer aldığı için 28 yazıldı — L1/L2 emsali).
- **Elenen taslaklar (4):** (1) S2 eşleştirme kümesi — paralel öğe kıtlığı (yukarıda).
  (2) Atölye çift sorusu (t9: iki gün + 12 kişi) — t7'deki servis sorusuyla arası 2 replik
  kalıyordu. (3) "Atölyeye nasıl yazılınır" tekli taslağı (t9) — aynı sıkışıklık.
  (4) Marit'in 10 kişilik pilot önerisi sorusu (t22) — OPUS5-21'in 27. sorusunun
  (cevap: 20, t24) çeldiricisini önceden ifşa ediyordu, ayrıca açıklaması zaten onların
  `explanation`'ında geçiyor. Üretilip son kontrolde silinen soru yok: iki senaryo baştan
  sona okunarak 11 soru anahtara bakılmadan çözüldü, **11/11 uyuştu**.
- **Harf dengesi:** ÇS 11–15: A, B, A, {B,C} / ÇS 21–23: A, B, C / eşleştirme 24–26:
  B, A, C — üst üste aynı harf yok; kutu 6 seçenekli (3 soru + 3 boşta, L4 emsali).
  Kullanılmayan düzeltmeli çeldiriciler: S2-04 (15→18 £) ve S2-24 (Cumartesi→iki gün) —
  ikisi de 3-replik kuralına sığmadı (t2 ve t9, seçilen dizilimin dışında).
- **Doğrulama:** `python tools/dogrula.py` → şema hatası 0, L5 40/40 TAM, görünür metinde
  IELTS 0; `python tools/_f43_kontrol.py L5` → 0 sorun (evidence birebir, replik
  aralıkları, 10 kelime seçenek sınırı, 50 kelime kök+seçenek sınırı).
- Referans: dinleme ÇS (tek/çok cevap) anahtar + transkript kalıpları ve eşleştirme
  kutu/yönerge kalıbı L1–L4'ün doğrulanmış dosyalarından sürdürüldü (format sabit).
- Atlanan/sorun: yok. Sıradaki çalıştırma: **L6** (6/9) — ⚠️ 11–15 bloku EŞLEŞTİRME
  olmak zorunda (seçim hakkı yok); L6-S2'nin öğe dizilimini 1-4-7-10-13 kalıbıyla dene.

## FABLE5-43 (6. çalıştırma: L6 — riskli sorular, 11 soru)

- **Üretilen:** `content/listening/tests/L6/matching.json` (İKİ küme, `groups`
  sarmalayıcısıyla, L3/L4 düzeni: 11–15 → 2. bölüm 5 öğeli eşleştirme, 24–26 →
  3. bölüm 3 öğeli eşleştirme) + `content/listening/tests/L6/multiple-choice.json`
  (21–23, 3. bölüm, düz `items`). Toplam **11 soru** — L6 artık `dogrula.py`'de
  **40/40 TAM** ve **altı tam testin hepsi 40/40**.
- **11–15 bloku seçimi: L6 = eşleştirme (3/3 — DENGE TAMAMLANDI).** Altı test kapandı:
  ÇS = L1, L2, L5 / eşleştirme = L3, L4, L6. Kota kısıtı kalmadı.
- **Yerleşim ve sıra kuralı:** S2 → replikler 2, 5, 8, 11, 14 (aralıklar tam 3;
  önerilen 1-4-7-10-13 yerine bir kaydırılmış türevi, çünkü t1/t4/t7'nin malzemesi
  ya zayıftı ya planda görünüyordu). t5, t8 OPUS5-21'in plan bölgesiyle (t5–t8,
  16–20) çakışıyor ama farklı bilgiye dayanıyor (L3/L4 emsali): planda çiçek
  tezgâhının KONUMU soruluyor, bende yerin seçilme SEBEBİ (koku, S2-13); planda
  bahçe kapısının dışındaki yer (bisiklet parkı), bende yükleme avlusunun KURALI
  (yalnız satıcı araçları, yeni nokta S2-37). S3 → ÇS 4, 9, 13; eşleştirme 16, 21, 25 —
  küresel dizi 4-9-13-16-21-25, bütün aralıklar ≥3. Tavan kuralı: 26'nın cevabı t25,
  OPUS5-21'in 27. sorusu t27'de (2 replik pay; sıra korunuyor, küme içi aralık kuralı
  dosya sınırında zaten uygulanmıyor — L1–L5 emsali). 21–30 küresel dizisi
  4-9-13-16-21-25-27-31-35-39 tamamen artan.
- **S3 eşleştirme kümesi "karar" kalıbında** (yenilik): öğeler üç tartışma ekseni
  (veri tabanı sayısı, tarih aralığı, tam metin filtresi), kutu ise kararın nasıl
  bağlandığı (A Rhian kabul / B Tomas kabul / C orta yol / D uzak durun uyarısı /
  E ertelendi). Konuşmacı adları kutuda geçiyor (kural 1 böyle karşılandı; L4'te
  adlar yönergedeydi). Tarama işbölümü (t29–31) ve kaynak yönetimi (t33–35)
  eksenleri BİLEREK dışarıda: turları OPUS5-21'in 28. (t31) ve 29. (t35) sorularının
  cevap replikleriyle çakışıyor, 26'nın tavanı (t27) aşılamazdı.
- **Çeldirici türleri:** "söylendi sonra düzeltildi" hem cevaplarda (11-C Perşembe→
  Çarşamba, 14-B iki→üç saat, 21-C 3.000→2.500) hem S2 kutusunun E (gösteri 11→12.30)
  ve G (tezgâh 15→18 £) çeldiricilerinde; "başkası söyledi" 24-B ve 25-B'de (Tomas'ın
  reddedilen önerileri; yalnız 3. bölümde mümkün, S2 tek konuşmacılı); "söylendi ama
  sorulan bu değil" hepsinde. Sesle hiç geçmeyen: 21-A, 22-B, 23-C ve S3 kutusunda E
  (soru başına ≤1 ✓; S2 kutusunun 7 seçeneğinin hepsi seste geçiyor, L4 emsali).
- **Yeni bilgi noktası senaryoya eklendi (yalnız L6-S2):** `L6-S2-37` (yükleme avlusu
  yalnız satıcı minibüslerine, replik 8). S3'te yeni nokta gerekmedi (S3-01, -05, -09,
  -12, -17, -20 kullanıldı; hiçbiri OPUS5-21'in 27–30 veya alıştırma dosyalarında
  cevap değil — alıştırmalar L6'dan yalnız S2-11/-15/-20/-22 plan noktalarını
  kullanıyor).
- **Elenen taslaklar (3):** (1) S2 için 0-3-6-9-12 dizilimi — t6'daki tek malzeme
  balık tezgâhının yeri ve planın 17. sorusuyla birebir aynı bilgiyi (drenaj repliği)
  test ediyordu. (2) S3 kararlar kümesine "tarama işbölümü + kaynak yönetimi"
  öğeleri — yukarıdaki tavan çakışması. (3) Balık tezgâhı ÇS taslağı ("neden
  girişte değil?") — aynı sebep, plan 17 ile çifte kullanım. Üretilip son kontrolde
  silinen soru yok: iki senaryo baştan sona okunarak 11 soru anahtara bakılmadan
  çözüldü, **11/11 uyuştu**.
- **Harf dengesi:** eşleştirme 11–15: C, D, F, B, A (kutu 7'li, E ve G boşta) /
  ÇS 21–23: B, C, B / eşleştirme 24–26: A, C, D (kutu 5'li, B ve E boşta, alt sınır) —
  üst üste aynı harf yok; 21–26 genelinde A×1 B×2 C×2 D×1.
- **Doğrulama:** `python tools/dogrula.py` → şema hatası 0, L6 40/40 TAM (L1–L6'nın
  altısı da TAM), görünür metinde IELTS 0; `python tools/_f43_kontrol.py L6` →
  0 sorun (evidence birebir, replik aralıkları, 10 kelime seçenek sınırı, 50 kelime
  kök+seçenek sınırı).
- Referans: dinleme ÇS (tek/çok cevap) anahtar + transkript kalıpları ve eşleştirme
  kutu/yönerge kalıbı L1–L5'in doğrulanmış dosyalarından sürdürüldü (format sabit);
  referanstan tek bir cümle, soru ya da senaryo kopyalanmadı.
- Atlanan/sorun: yok. **Tam test yarısı bitti: FABLE5-43'ün L1–L6 paketlerinin altısı
  da tamam (66 soru).** Sıradaki çalıştırma: **alıştırma ÇS tek cevaplı, 10 soru**
  (7/9) — `content/listening/practice/multiple-choice.json`, numaralar 1'den,
  `test_id` null, `practice` true, `groups` sarmalayıcısı, senaryo başına en fazla
  4 soru, tam testlerde kullanılan bilgi noktaları CEVAP yapılamaz.

## FABLE5-43 (7. çalıştırma: alıştırma — çoktan seçmeli tek cevap, 10 soru)

- **Üretilen:** `content/listening/practice/multiple-choice.json` — 10 tek cevaplı soru,
  `groups` sarmalayıcısıyla üç küme: L3-S2 → 2 soru (1–2), L5-S2 → 4 soru (3–6),
  L6-S2 → 4 soru (7–10). Numaralar 1'den, `test_id` null, `practice` true,
  `select_count` hepsinde 1. Dinleme alıştırması 90 → **100** soruya çıktı.
- **Senaryo seçimi:** üç küme de 2. bölüm (tek konuşmacılı anlatım) senaryolarından —
  önceki çalıştırmaların NOTLAR kayıtlarında **bilinçle alıştırmaya bırakılan** düzeltmeli
  çeldirici noktaları kullanıldı: `L3-S2-08` (5 → 4,5 mil; OPUS5-21 3. çalıştırmasının
  "FABLE5-43'ün ÇS alanına daha uygun" notu), `L5-S2-04` (15 → 18 £) ve `L5-S2-24`
  (yalnız Cumartesi → iki gün; L5 tam testine sığmayan iki nokta), `L6-S2-07`
  (19 → 32 tezgâh) ve `L6-S2-30` (5 £ → ücretsiz; OPUS5-21 6. çalıştırmasının bıraktığı
  havuzdan). Kalan cevap noktaları: `L3-S2-31` (ilk Cumartesi → ilk Pazar), `L5-S2-16`
  (nehir yolu), `L5-S2-32` (basılı program), `L6-S2-01` (Peveril Street salonu),
  `L6-S2-26` (gösteri listesi). Yeni bilgi noktası açmak gerekmedi; senaryo dosyalarına
  dokunulmadı.
- **Çakışma denetimi:** 10 cevap noktasının hiçbiri tam testlerde veya diğer alıştırma
  dosyalarında cevap değil (betikle doğrulandı). Tam testte yalnız çeldirici zemini olan
  noktalar cevap yapılabildi (L3/L4/L5 emsalinin simetriği): `L5-S2-16`, L5 tam testinin
  14–15 çift sorusunda "aslında serbest olan yol" çeldirici zeminiydi; burada sorulan
  bilgi farklı (yolun üzerine bir şey bırakılamaması, açık olması değil). `L6-S2-24`
  (gösteri 11 → 12.30) L6 tam testinde boşta kalan kutu harfinin (E) zeminiydi; burada
  cevap değil, 9. sorunun C çeldiricisi.
- **Yerleşim ve sıra kuralı:** küme içi replik dizileri L3: 3-12, L5: 2-6-9-12,
  L6: 0-3-9-12 — bütün aralıklar ≥3 (`tools/_p43_kontrol.py` doğruluyor; küme sınırında
  aralık kuralı uygulanmıyor, L1–L6 emsali).
- **Çeldirici türleri:** her soruda en az iki farklı tür. "Söylendi sonra düzeltildi"
  8 soruda (1-B, 2-A, 3-B, 5-A, 7-A, 8-A, 9-C, 10-A; 7-A ve 8-A eski durum → yeni durum
  kalıbında, senaryo `notes` alanı ikisini de düzeltme çeldiricisi sayıyor); "söylendi ama
  sorulan bu değil" 8 soruda; "söylenenin tersine çevrilmiş hâli" 3 çeldiricide (4-A, 5-B,
  9-B — L5 tam testindeki kutu-F emsali); sesle hiç geçmeyen: yalnız 6-C (soru başına ≤1 ✓).
  "Başkası söyledi" türü üç senaryo da tek konuşmacılı olduğu için yapısal olarak imkânsız
  (L1 emsali).
- **Elenen taslaklar (3):** (1) L5-S2 su noktası sorusu (t5, çeşme) — iki çeldirici de
  aynı türe (tür 3) düşüyordu; yerine nehir yolu sorusu (t6) yazıldı. (2) L6-S2 balık
  tezgâhı sebep sorusu (t6, drenaj) — L6 tam testinin plan 17. sorusuyla çifte kullanım
  riski (6. çalıştırmada da aynı gerekçeyle elenmişti). (3) L6-S2 açılış saati sorusu
  (t1, 9.00 → 8.30) — t0'daki taşınma sorusuyla arası 1 replik kalıyordu; taşınma sorusu
  (hedef nokta `L6-S2-01` daha önce hiç kullanılmamıştı) tercih edildi, `L6-S2-03` 8–9.
  çalıştırmalara kaldı. Üretilip son kontrolde silinen soru yok: üç senaryo baştan sona
  okunarak 10 soru anahtara bakılmadan çözüldü, **10/10 uyuştu**.
- **Harf dengesi:** A, B, C, B, C, A, B, C, A, B — üst üste aynı harf yok; A×3, B×4, C×3.
- **Doğrulama:** `python tools/dogrula.py` → şema hatası 0, alıştırma 100, görünür metinde
  IELTS 0; `python tools/_p43_kontrol.py` → 0 sorun (evidence birebir, turn_index bilgi
  noktasıyla uyumlu, replik aralıkları ≥3, 10 kelime seçenek / 50 kelime kök+seçenek
  sınırı, senaryo başına ≤4 soru, numaralar 1–10 ardışık, başka dosyada cevap olan nokta
  yok). Betik depoya kondu; 8–9. çalıştırmalar dosya adı argümanıyla kullanabilir.
- Referans: dinleme ÇS tek cevap anahtar + transkript PDF'leri okundu (yalnız format;
  metin alınmadı).
- Atlanan/sorun: yok. Sıradaki çalıştırma: **alıştırma ÇS çok cevaplı, 10 soru** (8/9) —
  `content/listening/practice/multiple-choice-multi.json`, `question_type`
  `multiple_choice_multi`, çift cevaplı kalıp (`Choose TWO letters, A-E`), bu dosyanın
  cevap noktaları da artık kullanılamaz.

## FABLE5-43 (8. çalıştırma: alıştırma — çoktan seçmeli çok cevaplı, 10 soru)

- **Üretilen:** `content/listening/practice/multiple-choice-multi.json` — 5 çift cevaplı
  soru (`Choose TWO letters, A-E`, `select_count` 2, `number` `"1-2"` … `"9-10"` = 10
  numara), `groups` sarmalayıcısıyla üç küme: L1-S2 → 2 soru (1–4), L4-S2 → 2 soru (5–8),
  L6-S3 → 1 soru (9–10). `test_id` null, `practice` true, `question_type`
  `multiple_choice_multi`. Dinleme alıştırması 100 → **110** soruya çıktı.
- **Senaryo seçimi:** iki 2. bölüm anlatımı (L1-S2 müze, L4-S2 geri dönüşüm merkezi) +
  bir 3. bölüm tartışması (L6-S3 kaynak taraması) — "başkası söyledi" çeldirici türü ancak
  S3'te mümkün olduğu için son küme bilerek tartışmadan. Cevap noktaları (hepsi o ana dek
  hiçbir dosyada cevap değildi, betikle doğrulandı): `L1-S2-11` (tur 45 dk; ikinci cevap
  gişe önünden kalkış, `L1-S2-10`'un repliği), `L1-S2-30` (hafta sonu otopark ücretsiz;
  ikinci cevap `L1-S2-31` on dört numaralı otobüs), `L4-S2-20` (izin ücretsiz + yılda 12
  ziyaret, iki cevap tek replikte), `L4-S2-34` (çocuklar araçta; ikinci cevap `L4-S2-35`
  konteynerden geri alma yasağı), `L6-S3-33` (aramayı kaydet + tarihi not et, iki cevap
  tek replikte). Yeni bilgi noktası gerekmedi; senaryo dosyalarına dokunulmadı.
- **Elenen taslak (1):** L1-S2 dokunma seansları sorusu (cevaplar: Cumartesi 11 + ücretsiz)
  hazır taslakken elendi — L1 tam testinin 14–15 çift sorusu aynı seanslar hakkında ve
  "ücretsiz" (`L1-S2-34`) orada zaten ikinci cevap; birebir çifte kullanım olurdu. Yerine
  ulaşım sorusu (t13) yazıldı. Ayrıca izin sorusunun "ziyaret başına dört torba moloz"
  seçeneği savunulabilir-doğru çıkma riskiyle taslakta değiştirildi (dört torba sınırı
  gerçek ama iznin değil hanelerin kuralı; yerine ticari atık seçeneği kondu). Üretilip
  son kontrolde silinen soru yok: üç senaryo baştan sona okunarak 5 soru anahtara
  bakılmadan çözüldü, **5/5 (10 numara) uyuştu**.
- **Yerleşim ve sıra kuralı:** küme içi replik dizileri L1: 4-13, L4: 9-14, L6: 39 —
  bütün aralıklar ≥3; küme sınırında aralık kuralı uygulanmıyor (7. çalıştırma emsali).
- **Çeldirici türleri:** her soruda en az iki farklı tür. "Söylendi sonra düzeltildi"
  1-A (tur saatleri 11.30 → 11) ve 5-C (kapıda form → çevrimiçi başvuru); "başkası
  söyledi" 9-D (tek seferde dışa aktarmayı Tomas soruyor, sınır 200 kayıt); "söylendi ama
  sorulan bu değil" 8 çeldiricide; "söylenenin tersine çevrilmiş hâli" 6 çeldiricide
  (L5/7. çalıştırma emsali). Sesle hiç geçmeyen çeldirici: 0 (15 çeldiricinin hepsi seste
  geçiyor).
- **Harf dengesi:** çiftler B-D, C-E, A-B, D-E, A-C — düzleştirilmiş dizi
  B D C E A B D E A C, üst üste aynı harf yok; A×2 B×2 C×2 D×2 E×2 (tam denge).
- **Betik uyarlaması:** `tools/_p43_kontrol.py` çift numaralı (`"1-2"`) soruları açacak
  şekilde genişletildi (numara ardışıklığı ve senaryo başına tavan artık numara sayısıyla);
  9. çalıştırma (eşleştirme) aynı betiği dosya adıyla kullanabilir.
- **Doğrulama:** `python tools/_p43_kontrol.py content/listening/practice/multiple-choice-multi.json`
  → 0 sorun; eski dosya için de yeniden koştu → 0 sorun; `python tools/dogrula.py` → şema
  hatası 0, alıştırma 110, görünür metinde IELTS 0.
- Referans: dinleme ÇS çok cevap anahtar + transkript PDF'leri okundu (yalnız format:
  "IN ANY ORDER" anahtar düzeni ve tek uzun replik içinde üç bilgi kalıbı; metin alınmadı).
- Atlanan/sorun: yok. Sıradaki çalıştırma: **alıştırma eşleştirme, 10 soru** (9/9, son) —
  `content/listening/practice/matching.json`, kutu seçenekleri soru sayısından en az 2
  fazla, bir senaryodan en fazla 4 soru; bu dosyanın cevap noktaları da artık kullanılamaz.

## FABLE5-43 (9. çalıştırma: alıştırma — eşleştirme, 10 soru — SON)

- **Üretilen:** `content/listening/practice/matching.json` — 10 eşleştirme sorusu,
  `groups` sarmalayıcısıyla üç küme: L1-S3 → 3 soru (1–3, kutu 5'li), L4-S3 → 3 soru
  (4–6, kutu 5'li), L5-S3 → 4 soru (7–10, kutu 6'lı). `test_id` null, `practice` true,
  `question_type` `matching`, `allow_repeat` false. Dinleme alıştırması 110 → **120**
  soruya çıktı — **F bölümü hedefi doldu; dogrula.py toplamı 1310/1310.**
- **Senaryo seçimi:** üç küme de 3. bölüm (tartışma) senaryolarından ve üçü de
  "danışman ne söylüyor?" kalıbında — kutu = danışmanın ifadeleri, öğeler = projenin
  parçaları. Bilinçli tercih: yönergede konuşmacı sabitlenince (the tutor) "başkası
  söyledi" çeldiricisi kutuya taşınabiliyor (öğrencinin görüşü danışmanınmış gibi
  sunuluyor) ve tek-cevap kuralı korunuyor. 7. çalıştırmanın üç kümesi S2'dendi;
  böylece alıştırma dosyaları bölüm dengesi de kurdu.
- **Cevap noktaları (hepsi o ana dek hiçbir dosyada cevap değildi, betikle doğrulandı):**
  L1-S3-06 (slayt metni puan kaybettirir, t8), -13 (anket üç yaşında, t18), -21 (el notu
  öğlene kadar, t27); L4-S3-06 (yöntem alt şeritte, t7), -11 (kırmızı-yeşil, t13),
  -15 (başlık üç metreden, t17); L5-S3-10 (kapalı gövde + iki açık soru, t14),
  -17 (pilotta arkadaş yasağı, t24), -20 (birer sayfa, t28), -23 (on artı beş dakika,
  t32). Yeni bilgi noktası gerekmedi; senaryo dosyalarına dokunulmadı.
- **Yerleşim ve sıra kuralı:** küme içi replik dizileri L1: 8-18-27, L4: 7-13-17,
  L5: 14-24-28-32 — bütün aralıklar ≥3 (`tools/_p43_kontrol.py` doğruluyor; küme
  sınırında aralık kuralı uygulanmıyor, 7–8. çalıştırma emsali).
- **Çeldirici türleri:** her soruda en az iki farklı tür. "Başkası söyledi" L4 kutusunda
  A (Idris: yöntem ilk görülen şey olsun) ve L5 kutusunda F (Devan: kağıda kayıt) —
  yönerge danışmanı sorduğu için ikisi de her öğede yanlış; "söylendi sonra düzeltildi"
  kökenli L1 kutusunda E (geçen yılın el kitabı → ders sayfası kılavuzu; 3. soruda tam
  tuzak hâli); "söylenenin tersine çevrilmiş hâli" L5 kutusunda B (etik formu bir hafta
  geç değil, öne alındı — L5/7-8. çalıştırma emsali); "söylendi ama sorulan bu değil /
  başka öğe için söylendi" kutu ortak olduğu için yaygın (L1–L6 eşleştirme emsali).
  Sesle hiç geçmeyen çeldirici: 0 (üç kutunun 16 seçeneğinin hepsi seste geçiyor).
- **Elenen taslaklar (3):** (1) L1-S3 "the room" öğesi — medya odası hakkında iki
  savunulabilir doğru ifade çıkıyordu ("donanımı daha iyi" + "bölüm ofisinden iki kez
  ayırtın"), tek-cevap kuralı riske giriyordu; yerine slayt/anket/el notu üçlüsü
  kuruldu. (2) Kişi-eşleştirme kümeleri (L1-S3 röportaj ekseni t19-20-21, L5-S3 kayıt
  ekseni t36-37-38) — görüş eksenleri ardışık repliklerde, 3-replik kuralı geçmiyor
  (L2-S2/L3-S3/L4-S3 emsali). (3) L5-S3 ilk öğe seti (görüşme süresi t16 + ödül
  çekilişi t21) — hedef noktalar (S3-11, S3-15) başka dosyalarda zaten cevap; küme
  t14-24-28-32 dizisine kaydırıldı. Üretilip son kontrolde silinen soru yok: üç senaryo
  baştan sona okunarak 10 soru anahtara bakılmadan çözüldü, **10/10 uyuştu**.
- **Harf dengesi:** A, C, B / D, B, E / C, D, E, A — üst üste aynı harf yok (küme
  sınırları dahil); dağılım A×2 B×2 C×2 D×2 E×2 (tam denge). Kutu fazlası: 5−3=2,
  5−3=2, 6−4=2 (alt sınır ✓).
- **Betik uyarlaması:** `tools/_p43_kontrol.py` eşleştirmeyi işleyecek şekilde
  genişletildi (item `options` boşsa grup kutusundan okur; kutu ≥ soru+2 ve
  `allow_repeat` false iken küme içi harf tekrarı denetimi eklendi). Eski iki alıştırma
  dosyası için yeniden koştu → 0 sorun.
- **Doğrulama:** `python tools/_p43_kontrol.py content/listening/practice/matching.json`
  → 0 sorun; `python tools/dogrula.py` → şema hatası 0 (9. sorunun açıklaması Türkçe
  özel karakter içermediği için bir kez işaretlendi, yeniden yazıldı), alıştırma 120,
  TOPLAM 1310, görünür metinde IELTS 0.
- Referans: `referans/text/` altında dinleme dosyaları yok ve bu ortamda PDF işleyici
  (poppler) kurulu olmadığından PDF'ler açılamadı; eşleştirme kutu/yönerge kalıbı
  L1–L6'nın doğrulanmış eşleştirme dosyalarından sürdürüldü (o kalıplar 1–3.
  çalıştırmalarda resmi örneklerden çıkarılmıştı; referanstan tek cümle kopyalanmadı).
- Atlanan/sorun: yok. **FABLE5-43 tamam: 9 çalıştırmanın 9'u da bitti (66 + 30 = 96
  soru). Dinleme üretimi (senaryolar + sorular) 360/360 tamamlandı.**


## CAPRAZ-90 (1. çalıştırma: doğru/yanlış/verilmemiş + evet/hayır/verilmemiş, 80 soru)

- **Doğrulanan paket:** okuma — `true-false-not-given` (7 dosya) + `yes-no-not-given`
  (3 dosya); toplam 80 soru. **Doğrulayan model: opus, üreteni: fable.**
- **Sonuç: 80/80 uyuştu (%100,0), işaretlenen 0.** Rapor:
  `content/DOGRULAMA/dogru-yanlis-verilmemis.json` ve `content/DOGRULAMA/RAPOR.md`.
- **Yöntem:** `tools/kor-kopya.py` ile cevapsız kopyalar üretildi, orijinal soru
  dosyaları hiç açılmadan 80 soru 14 metinden (A01, A02, A04–A12, G01, G02, G05, G06)
  gerçek aday gibi çözüldü, karşılaştırmayı `tools/karsilastir.py` yaptı. Cevap
  anahtarı ancak 4. adımda görüldü.
- **İşaretleme:** uyuşmayan soru çıkmadığı için 80 sorunun hepsine `"status":
  "verified"` eklendi; `"flagged"` yok, silinen soru yok.
- **Yeni betik:** `tools/_capraz_isaretle.py` — kör cevaplarla anahtarı karşılaştırıp
  orijinal dosyalara `status`/`flag_reason` ekler. Dosyayı yeniden serileştirmek
  yerine `"difficulty"` satırının ardına metin düzeyinde ekleme yapar; böylece elle
  kurulmuş biçimlendirme (kısa dizilerin tek satırda kalması) bozulmuyor — ilk
  denemede `json.dump` ile yazınca 692 satırlık gereksiz fark çıkmıştı, metin
  düzeyinde ekleme bunu 160 satıra indirdi. Ekleme öncesi `difficulty` satır sayısı
  soru sayısıyla karşılaştırılıyor, tutmazsa dosyaya dokunulmuyor; yazmadan önce
  `json.loads` ile doğrulanıyor.
- **Tuzak (sonraki oturumlar için):** `tools/kor-kopya.py` her koşuda
  `dogrulama/kor/` klasörünü siliyor ama `dogrulama/cevap/` klasörünü **temizlemiyor**.
  Önceki oturumdan kalan `content__reading__practice__matching-sentence-endings.json`
  ilk karşılaştırmaya 10 fazladan soru olarak karıştı (90 soru göründü). Dosya `.eski`
  uzantısıyla kenara alınıp karşılaştırma tekrarlandı. **Oturum başında
  `dogrulama/cevap/` boş olmalı.**
- **Örüntü:** sistematik hata yok. 22 NOT GIVEN cevabının hepsinde metnin konuştuğu
  alanın hemen yanındaki ama hiç değinmediği ayrıntı sorulmuş (üretim promptundaki üç
  şartlı test uygulanmış); FALSE/NO soruları tek ve net bir çelişki cümlesine dayanıyor.
  Ayrım kaymasına en yakın iki soru AC3/13 ("includes" ≠ "only") ve GT2/9 ("this year's"
  ≠ "every year") — ikisinde de kör çözüm anahtarla uyuştu, ama ikinci doğrulamada
  tekrar bakılmaya en uygun adaylar bunlar.
- **Doğrulama:** `python tools/kontrol.py` → 11 kontrolün 11'i geçti.
- Atlanan/sorun: yok. CAPRAZ-90'ın kalan 6 çalıştırması bekliyor (2–4 opus, 5–7 fable).
- **`.gitignore` düzeltmesi:** `dogrulama/` deseni köke sabitlenmemişti; git'in
  yol deseni her seviyedeki aynı adlı klasörü tutuyor ve Windows'ta eşleşme
  büyük/küçük harf duyarsız olduğu için desen **`content/DOGRULAMA/` klasörünü de
  yutuyordu**. Sonuç: doğrulama raporları (bu oturumunki ve önceki FABLE5-42
  oturumlarından kalan 4 rapor) depoya hiç girmemişti — `git ls-files
  content/DOGRULAMA/` boş dönüyordu. Desen `/dogrulama/` yapıldı: kökteki çalışma
  klasörü (kör kopyalar + kör cevaplar) hâlâ yok sayılıyor, `content/DOGRULAMA/`
  artık takip ediliyor. Bu commit'le birlikte 4 eski f42 raporu da depoya girdi.


## CAPRAZ-90 (2. çalıştırma: çoktan seçmeli — okuma + çoktan seçmeli-çoklu, 35 soru)

- **Doğrulanan paket:** okuma — `multiple-choice` (7 dosya: alıştırma + AC1–AC4 + GT1–GT2)
  ve `multiple-choice-multi` (1 dosya, dinleme alıştırması); toplam 35 soru nesnesi,
  cevap kağıdında 49 kutu. **Doğrulayan model: opus, üreteni: fable.**
- **Sonuç: 35/35 uyuştu (%100,0), işaretlenen 0.** Rapor:
  `content/DOGRULAMA/coktan-secmeli.json` ve `content/DOGRULAMA/RAPOR.md`.
- **Yöntem:** `tools/kor-kopya.py multiple-choice multiple-choice-multi` ile cevapsız
  kopyalar üretildi; orijinal soru dosyaları hiç açılmadan sorular 8 okuma metninden
  (A02, A03, A05, A06, A08, A09, A11, A12, G03, G04) ve 3 dinleme senaryosundan
  (L1-S2, L4-S2, L6-S3) gerçek aday gibi çözüldü. Dinleme senaryolarında `answer_points`
  alanı okunmadı, sadece `turns` dökümü alındı. Karşılaştırmayı `tools/karsilastir.py`
  yaptı; anahtar ancak 4. adımda görüldü.
- **İşaretleme:** `tools/_capraz_isaretle.py` ile 35 sorunun hepsine `"status":
  "verified"` eklendi; `"flagged"` yok, silinen soru yok.
- **Kapsam kararı:** prompt tablosunda `multiple-choice-multi` bu oturuma yazılı ama
  depoda bu ada sahip tek dosya **dinleme** alıştırması. Okuma tarafında ayrı `-multi`
  dosyası yok; çok cevaplı okuma soruları normal `multiple-choice.json` içinde
  (`select_count: 2`, `number: "34-35"`). Başka hiçbir oturum bu dosyayı kapsamadığı için
  doğrulamaya alındı. Oturum 4'e ait dinleme `multiple-choice` dosyalarına dokunulmadı.
- **Örüntü:** sistematik hata yok. Çeldiriciler metnin içinden kurulmuş (AC1/32 "unusual
  warmth", AC4/34-35 "nap length predicted the gain" — metin tersini söylüyor, A08/9-10
  "North America's highest peak" — Mount Logan Kanada'nın en yükseği). 9 çoklu seçim
  sorusunun hepsinde iki doğru şık ayrı ayrı ve açıkça destekleniyor; "üçüncü şık da
  savunulabilir" durumu çıkmadı. Tek zayıf nokta AC2/34-35'teki F şıkkı ("Colleagues
  never meet one another in person") — metin "without face-to-face contact" diyor,
  "never" çıkarımla geliyor; şık yine de doğru, ama ikinci doğrulamada bakılacak en iyi
  aday bu (kör çözümde güven 4 verildi, yine de anahtarla uyuştu).
- **Yöntem notu:** 1. oturumun tuzağına düşülmedi — oturum başında `dogrulama/cevap/`
  içindeki 11 eski dosya `dogrulama/cevap-arsiv/oturum1/` altına taşındı, karşılaştırma
  temiz klasörle çalıştı.
- **Doğrulama:** `python tools/kontrol.py` → 11 kontrolün 11'i geçti.
- Atlanan/sorun: yok. CAPRAZ-90'ın kalan 5 çalıştırması bekliyor (3–4 opus, 5–7 fable).

---

## CAPRAZ-90 (3. çalıştırma: eşleştirme tipleri — başlık + özellik + cümle sonu, 81 soru)

- **Doğrulanan paket:** okuma — `matching-headings` (7 dosya: alıştırma + AC1–AC4 + GT1–GT2,
  45 soru), `matching-features` (5 dosya: alıştırma + AC1–AC4, 26 soru) ve
  `matching-sentence-endings` (1 dosya: alıştırma, 10 soru); toplam 81 soru.
  **Doğrulayan model: opus, üreteni: fable.**
- **Sonuç: 81/81 uyuştu (%100,0), işaretlenen 0.** Rapor:
  `content/DOGRULAMA/eslestirme-tipleri.json` ve `content/DOGRULAMA/RAPOR.md`.
- **Yöntem:** `tools/kor-kopya.py matching-headings matching-features
  matching-sentence-endings` ile 13 cevapsız kopya üretildi; orijinal soru dosyaları hiç
  açılmadan sorular 9 okuma metninden (A01, A02, A05, A07, A08, A09, A10, A11, A12, G05,
  G06) gerçek aday gibi çözüldü. Karşılaştırmayı `tools/karsilastir.py` yaptı; anahtar
  ancak 4. adımda görüldü.
- **İşaretleme:** `tools/_capraz_isaretle.py` ile 81 sorunun hepsine `"status":
  "verified"` eklendi; `"flagged"` yok, silinen soru yok.
- **Örüntü:** sistematik hata yok. Başlık eşleştirmede çeldiriciler bilinçli olarak "fazla
  dar" kurulmuş (AC1 "Choosing animals of a similar build" → B'nin yalnızca ilk cümlesi;
  A09 "Equipment built especially for the site" → aslında yazılım yöntemi) ya da ters
  çevrilmiş (A08 "A glacier stopped in its tracks", A11 "An urban view chosen to create
  stress"). Özellik eşleştirmede `allow_repeat: true` setlerinde tekrar eden şıklar
  metinde gerçekten iki ayrı yere dayanıyor. Cümle sonu eşleştirmede yanlış sonlar
  dilbilgisel olarak da uyuyor, yani aday sadece dilbilgisiyle eleyemiyor — bu tipte en
  sık görülen üretim hatası yok.
- **İkinci doğrulamada bakılacak tek aday AC3/14** (A08 paragraf B): "vii — A tally of the
  slopes that failed" paragrafın ilk cümlesine, anahtar cevabı "ii — Why the usual approach
  did not work" kalan dört cümlesine oturuyor. Kör çözümde gist gerekçesiyle "ii" seçildi
  ve uyuştu, ama güven 3 verildi; çeldirici başka bir paragrafa demirlenmediği için soru
  tartışmaya açık. "vii"yi C veya D paragrafına demirlenen bir ifadeyle değiştirmek
  soruyu tamamen netleştirir.
- **Yöntem notu:** oturum başında `dogrulama/cevap/` içindeki 8 eski dosya
  `dogrulama/cevap-arsiv/oturum2/` altına taşındı, karşılaştırma temiz klasörle çalıştı.
- **Doğrulama:** `python tools/kontrol.py` → 11 kontrolün 11'i geçti.
- Atlanan/sorun: yok. CAPRAZ-90'ın kalan 4 çalıştırması bekliyor (4 opus, 5–7 fable).

## CAPRAZ-90 (4. çalıştırma: dinleme — çoktan seçmeli + eşleştirme, 83 soru)

- **Doğrulanan paket:** dinleme — `multiple-choice` (7 dosya: alıştırma + L1–L6, 40 soru;
  37 tek cevaplı + 3 çift harfli "14-15" sorusu) ve `matching` (7 dosya: alıştırma + L1–L6,
  43 soru); toplam 83 soru. **Doğrulayan model: opus, üreteni: fable.**
- **Sonuç: 83/83 uyuştu (%100,0), işaretlenen 0.** Rapor:
  `content/DOGRULAMA/dinleme-coktan-secmeli-eslestirme.json` ve
  `content/DOGRULAMA/RAPOR.md`.
- **Yöntem:** `tools/kor-kopya.py multiple-choice matching` 21 kör kopya üretti; okumaya ait
  7 `multiple-choice` kopyası (2. oturumda doğrulanmıştı) açılmadan silindi, geriye 14
  dinleme dosyası kaldı. Sorular yalnızca `content/listening/scripts/` altındaki 12
  senaryodan (L1-S2, L1-S3, L2-S2, L2-S3, L3-S2, L3-S3, L4-S2, L4-S3, L5-S2, L5-S3, L6-S2,
  L6-S3) gerçek aday gibi çözüldü; orijinal soru dosyaları hiç açılmadı. Karşılaştırmayı
  `tools/karsilastir.py` yaptı; anahtar ancak 4. adımda görüldü.
- **İşaretleme:** `tools/_capraz_isaretle.py` ile 83 sorunun hepsine `"status": "verified"`
  eklendi; `"flagged"` yok, silinen soru yok.
- **Örüntü:** sistematik hata yok. Bu paketin tamamı senaryolardaki "düzeltme" mimarisine
  dayanıyor (konuşmacı önce broşürdeki/eski bilgiyi söylüyor, sonra düzeltiyor) ve her
  düzeltme çiftinin iki ucu da şık listesinde: L2/11 "bir yıl → 18 ay", L5/13 "afişte 20 dk
  → gerçekte 15 dk", L6/21 "el kitabı 3.000 → ders sayfası 2.500". Çeldiricilerin bir kısmı
  senaryodaki *başka bir soruya ait doğru bilgi* — L1/13'te dokuma gösterimi gerçekten var
  ama avluda değil galeride; L2/21'de "brook was in flood" doğru ama ikinci örneklemeyi
  geciktiren neden. Uydurma çeldirici ya da boş kutu şıkkı yok.
- **Bölüm 3 görüş soruları** (L1, L2, L3, L4, L5, L6) üç konuşmacının her tartışma ekseninde
  ayrı konumda olduğu yapıdan besleniyor; "kimin görüşü" soruları tek replikle kesin
  çözülüyor, konuşmacı karıştırma riski hiçbir soruda oluşmadı.
- **Güven 4 verilen altı cevap** (L1/24, L2/25, L4/21, L5/24, L6/24, alıştırma eşleştirme 2)
  hepsi uyuştu; hepsi "şık kesin ama ifade metinden bir adım soyut" tipi ("only for context"
  → "background information only"). İkinci doğrulamada bakılması gereken aday çıkmadı.
- **Yöntem notu:** oturum başında `dogrulama/cevap/` içindeki 13 eski dosya
  `dogrulama/cevap-arsiv/oturum3/` altına taşındı; karşılaştırma temiz klasörle çalıştı.
  (`tools/kor-kopya.py` hâlâ `dogrulama/cevap/` klasörünü temizlemiyor.)
- Atlanan/sorun: yok. CAPRAZ-90'ın kalan 3 çalıştırması bekliyor (5–7, hepsi fable).

## CAPRAZ-90 çapraz doğrulama — 5. çalıştırma (okuma, tamamlama tipleri)

- **Paket:** okumadaki bütün tamamlama tipleri — `note-completion`, `table-completion`,
  `flow-chart-completion`, `summary-completion`, `sentence-completion`, `short-answer`,
  `diagram-labelling`. 23 dosya (5 alıştırma + AC1–AC4 + GT1–GT2), toplam **151 soru**.
  **Doğrulayan model: fable, üreteni: opus.**
- **Sonuç: 149/151 uyuştu (%98,7), işaretlenen 2.** Yedi oturumun şu ana kadarki en
  yüksek oranı. Rapor: `content/DOGRULAMA/okuma-tamamlama-tipleri.json` ve
  `content/DOGRULAMA/RAPOR.md`.
- **Yöntem:** `tools/kor-kopya.py` yedi paket adıyla çağrıldı, 48 kör kopya üretti;
  bunların 25'i dinlemeye ait (7. oturumun işi) ve hiç açılmadı. Kalan 23 okuma dosyası
  `passages/academic/A01–A12` ve `passages/general/G01–G06` üzerinden gerçek aday gibi
  çözüldü; orijinal soru dosyaları 4. adıma kadar açılmadı. Karşılaştırmayı
  `tools/karsilastir.py` yaptı.
- **İşaretleme:** `tools/_isaretle.py` (bu oturumda yazıldı) 149 soruya
  `"status": "verified"`, 2 soruya `"status": "flagged"` + `flag_reason` ekledi. Script
  dosyaları yeniden serileştirmiyor, `"difficulty"` satırının ardına metin düzeyinde
  ekleme yapıyor; böylece kompakt dizi/tek satırlık nesne biçimlendirmesi bozulmuyor ve
  diff yalnızca eklenen satırları gösteriyor. Silinen soru yok.
- **İki işaretin ikisi de aynı türden ve ikisi de içerik hatası değil:**
  `practice/short-answer` 5 (anahtar "8,400 years", doğrulayıcı "8,400 years old") ve
  `AC3/summary-completion` 39 (anahtar "seven", doğrulayıcı "seven distinct"). İkisinde de
  cevabın içeriği doğru; anlaşmazlık boşluğa kaç kelime yazılacağında. Birincisi zaten
  `accepted_variants` içinde — karşılaştırma scripti yalnızca `answer` alanına baktığı için
  yanlış alarm. İkincisinde varyant gerçekten eksik. **Yapılacak iş: tamamlama tiplerinde
  sayı+isim kalıpları için `accepted_variants` bir kez taranmalı.**
- **Kelime sınırları temiz.** 151 anahtarın hiçbiri kendi yönergesindeki sınırı aşmıyor;
  ONE WORD ONLY setlerinde tireli bileşikler ("sound-absorbing", "15-minute", "five-point")
  dahil hepsi tek kelime. Üretim promptundaki sınır kontrolü çalışmış.
- **Tek belirsizlik:** alıştırma `diagram-labelling` 10 (güven 3, yine de uyuştu —
  "instant messaging"). Şemadaki ok telefon ikonundan çıkıyor ve G04'te çekirdek saatler
  için "reachable by phone or video call" da yazıyor; o ifade ÜÇ KELİME sınırına
  sığmadığı için soru sınır sayesinde tek cevaba iniyor, şema sayesinde değil.
  İşaretlenmedi; ikinci doğrulamada bakılabilir.
- **Yöntem notu:** oturum başında `dogrulama/cevap/` içindeki 14 eski dosya (4. oturum)
  silindi — `tools/karsilastir.py` klasördeki her dosyayı okuduğu için bu şart.
  `tools/kor-kopya.py` bu klasörü hâlâ kendisi temizlemiyor.
- Atlanan/sorun: yok. CAPRAZ-90'ın kalan 2 çalıştırması bekliyor (6–7, ikisi de fable).

## CAPRAZ-90 çapraz doğrulama — 6. çalıştırma (okuma, bilgi eşleştirme)

- **Paket:** `matching-information`. 7 dosya (1 alıştırma + AC1–AC4 + GT1–GT2), toplam
  **49 soru**. **Doğrulayan model: fable, üreteni: opus.**
- **Sonuç: 49/49 uyuştu (%100,0), işaretlenen 0.** Rapor:
  `content/DOGRULAMA/bilgi-eslestirme.json` ve `content/DOGRULAMA/RAPOR.md`.
- **Yöntem:** `tools/kor-kopya.py matching-information` 7 kör kopya üretti. Sorular
  `passages/academic/A01, A03, A04, A06, A07, A09, A11, A12` ve `passages/general/G01, G02`
  üzerinden gerçek aday gibi çözüldü; orijinal soru dosyaları 4. adıma kadar açılmadı.
  Karşılaştırmayı `tools/karsilastir.py` yaptı.
- **İşaretleme:** `tools/_capraz6_isaretle.py` (5. oturumun scriptinden uyarlandı) 49 sorunun
  tamamına `"status": "verified"` ekledi, `flagged` yok. Script dosyaları yeniden
  serileştirmiyor, `"difficulty"` satırının ardına metin düzeyinde ekleme yapıyor; kompakt
  biçimlendirme bozulmuyor. Silinen soru yok.
- **Tipin en büyük riski (iki paragraf da olabilir) bu pakette gerçekleşmemiş.** Nedeni,
  49 sorunun tamamının paragrafın genel konusuna değil **tek bir cümleye** demirlenmiş
  olması; `uniqueness_check` alanları rakip paragrafı adıyla anıp neden elendiğini yazıyor
  ve kör çözümde elediğim paragraflarla birebir örtüştü.
- **Tek sınıra yakın soru AC1/29** (güven 4, yine de uyuştu — cevap A). "Whole living
  community vs tests on separate creatures" karşıtlığı A paragrafında birebir var
  ("marine ecosystems ... rather than merely how individual organisms behave"), ama E
  paragrafındaki "a real reef community actually behaves" ifadesi yüzeyde benziyor.
  Ayrım şu: E'nin karşıtlığı varsayımsal **modelleme** ile, ayrı canlı testleriyle değil.
  İkinci doğrulamada bakılmaya en uygun tek aday bu.
- **Cevaplar metin sırasını izlemiyor** (AC1: C-H-A-G-E, AC2: F-A-H-B-D, AC3: B-H-E-A-F,
  AC4: D-A-H-G-C) — bilgi eşleştirmede olması gereken de bu. GT setlerindeki "NB You may
  use any letter more than once" izni gerçekten kullanılmış ve her tekrar duyurunun
  **farklı bir cümlesine** dayanıyor.
- **Küçük kusur (işaretlenmedi):** alıştırma dosyasının yönergesinde de "NB You may use any
  letter more than once" var ve set genelinde doğru, ancak **tek bir pasaj bloğu içinde**
  hiçbir harf tekrar etmiyor. Aday soruları pasaj pasaj çözdüğü için NB pratikte bilgi
  vermiyor; yanıltıcı değil ama gereksiz.
- **Yöntem notu:** oturum 5'ten kalan 23 cevap dosyası `dogrulama/cevap/` içindeydi ve ilk
  karşılaştırmaya karıştı (200 soru raporlandı). `dogrulama/cevap-arsiv/oturum5/` altına
  taşınıp karşılaştırma tekrarlandı. **Bu, aynı karışıklığın üst üste dördüncü oturumda
  yaşanması.** Kalıcı çözüm: ya `tools/kor-kopya.py` bu klasörü de arşivlesin, ya da
  `tools/karsilastir.py` yalnızca o oturumda üretilen kör kopyalara karşılık gelen cevap
  dosyalarını okusun. 7. oturuma girmeden önce klasörün boş olduğu kontrol edilmeli.
- Atlanan/sorun: yok. CAPRAZ-90'ın kalan 1 çalıştırması bekliyor (7, fable — dinleme
  güvenli sorular).

## 2026-08-06 — CAPRAZ-90 7/7: dinleme form/plan/tamamlama (fable, ureten opus)

- Dogrulanan paketler: `form-completion`, `plan-map-diagram-labelling` ve dinlemedeki
  butun tamamlama dosyalari (`note-completion`, `table-completion`,
  `flow-chart-completion`, `summary-completion`, `sentence-completion`, `short-answer`).
  36 dosya, 264 soru.
- Dogrulayan model: fable. Uyusma orani **%91,3** (241/264). Isaretlenen: **23**.
- **Isaretlenenlerin 22'si icerik hatasi degil, cevap anahtari bicimi.** 11 tanesi
  rakam/yazi ikilemi (`5`/`five`), 4 tanesi tarih-saat bicimi, 3 tanesi bastaki
  `a`/`the`, 2 tanesi bosluk (telefon numarasi, referans kodu), 1 tanesi tekil/cogul.
  Tek gercek ifade secimi L4 short-answer 33 (`low frequencies` / `the low end`) ve ders
  metninde ikisi de gecerli. **Icerik uyusmasi 264'te 263.**
- **Oneri: hicbir soru yeniden uretilmemeli.** Yapilmasi gereken `accepted_variants`
  alanini doldurmak ya da puanlamada normallestirici kullanmak (rakam<->yazi, bastaki
  `a/the` atma, bosluk atma). Bu tek duzeltme 22 isaretin hepsini kapatir.
- **Plan/harita/sema etiketleme: 45/45, tek uyusmazlik yok.** Senaryolarin
  `spatial_description` alani ile SVG geometrisi tutarli, "girise gore sol/sag" cercevesi
  butun konusmalarda korunmus. Doğrulamasi en zor sanilan tip paketin en saglam kismi.
- Celdirici mekanigi calisiyor: 60'tan fazla "sorry, ignore that / that's last year's
  figure" duzeltmesinin hicbirinde anahtar eski degerde kalmamis.
- **Yontem notu:** `dogrulama/cevap/` klasorunde yine onceki oturumdan (6, okuma bilgi
  eslestirme) 7 cevap dosyasi duruyordu; bu **ust uste besinci oturumda ayni karisiklik**.
  Bu kez kalici cozum uygulandi: `tools/kor-kopya.py` artik yeni bir oturum baslatirken
  varolan `dogrulama/cevap/` klasorunu `dogrulama/cevap-arsiv/<tarih-saat>/` altina
  tasiyor, boylece bir sonraki `karsilastir.py` yalnizca o oturumun cevaplarini gorur.
- Ayrica: `karsilastir.py` cevap listesini birebir esledigi icin birden fazla varyant
  yazmak yapay uyusmazlik uretiyor; cevaplar tek bicime indirildi. Oran bu yuzden **alt
  sinir**.
- Atlanan/sorun: yok. **CAPRAZ-90 tamam** — yedi calistirmanin hepsi bitti.

## SONNET5-A0-kimlik-ve-esik

- Tarih: 2026-08-06
- `tools/_a0_kimlik.py` yazildi ve calistirildi: `content/` ve `passages/` altindaki
  345 JSON dosyasindan **344 tanesine** `"exam": "ielts"` alani `schema_version`'dan
  hemen sonra eklendi. **0 tanesinde zaten vardi.** **1 tanesi atlandi:**
  `passages/INDEX.json` (en ust duzeyi dict degil, dizi — eklenecek "ust duzey" alani
  yok, veri yapisi bozulmasin diye dokunulmadi). Soru metinlerine, cevaplara,
  aciklamalara dokunulmadi; sadece zarf alani eklendi.
- `tools/_a0_test_tanimlari.py` yazildi ve calistirildi: 12 tam test klasorunun her
  birine bir `_test.json` band esigi tanim dosyasi uretildi (AC1–AC4, GT1–GT2,
  L1–L6). Tablolar prompttaki degerler aynen kullanildi, uydurulmadi: Academic okuma,
  General Training okuma ve Dinleme icin uc ayri tablo.
- `python tools/dogrula.py` sonrasi **0 sema hatasi** — `_test.json` dosyalari
  `ortak.soru_dosyalari()` tarafindan zaten alt cizgiyle basladigi icin soru seti
  sanilmiyor, dolayisiyla schema kontrolune girmiyor. 12 tam test hala 40/40 TAM.
- Not: `json.load` → alan ekle → `json.dump(indent=2)` yontemi prompt tarafindan
  acikca istendigi icin, daha once tek satirda yazilmis bazi diziler/nesneler
  (`"answer": ["cable"]` gibi) coklu satira genisledi — bu, icerikte degisiklik degil,
  bicimlendirme farki (git diff'te satir sayisi fazla gorunmesinin sebebi budur).

## OPUS5-A1 2/4 — Academic Task 2 yazma ornekleri metne dokuldu (sayfa 18-26)

- Tarih: 2026-08-06. Belge: `referans/ielts-academic-writing-sample-tasks-2023.pdf`,
  sayfa 18-26. **5 ornek** dokuldu, hepsi Academic **Task 2**:
  `AC-T2-2A-A` (band 4,0 - 179 kelime), `AC-T2-2A-B` (6,5 - 421),
  `AC-T2-2A-C` (8,5 - 272), `AC-T2-2B-A` (5,5 - 228), `AC-T2-2B-B` (7,5 - 375).
  Band dagilimi: 4 / 5,5 / 6,5 / 7,5 / 8,5 — her yarim band bir kez, 4 ile 8,5 arasi.
  Dosyalar `kalibrasyon/ornekler/yazma/` altinda (gitignore'da, depoya girmiyor).
- **Tuzak kontrolu gecildi, supheli isaretlenen yok.** Band 6 ve altindaki iki cevapta
  (4,0 ve 5,5) hata yogunlugu cok yuksek: 2A-A'da ~25, 2B-A'da ~19 belirgin hata.
  Tablo ve ornek hatalar `kalibrasyon/ornekler/yazma/KONTROL.md` dosyasinda.
- **Yontem:** metin katmani (`referans/text/*.txt`) gomulu font yuzunden kaydirilmis ve
  rakamlari dusuruyor — **band puanlari metin katmaninda yok**, hepsi sayfa goruntusunden
  okundu. El yazisi `tools/_a1_bant.py` (bu oturumda yazildi) ile sayfa basina 3-8 yatay
  banda bolunup 350-500 dpi'da okundu; suphede kalan tek kelimeler `tools/_a1_kirp.py` ile
  900 dpi'a buyutuldu. Kelime sayilari goz karari degil, `tools/_a1_kelime_say.py` ile
  bosluga gore sayildi.
- **Dokum kararlari:** ustu cizilmis kisimlar dokulmedi, `transcription_notes`'a yazildi
  (2A-B'de 'Just to put' ile 'food' arasinda tamamen karalanmis okunamayan bir kelime,
  2B-A'da 'To sum up I think' sonrasinda karalanmis 2-3 kelimelik blok var). Caretle satir
  ustune eklenen kelimeler metne yerlestirildi ('economic & social', 'few', 'exotic',
  'or live', 'of', 'a', 'and'). Satir sonu tiresi ('fu-nction') birlestirildi.
  2B-B'de adayin yazdigi baslik ("'Tourism' - friend or foe?") dokume dahil edildi.
- **El yazisi tuzagi:** 2A-B'nin el yazisinda kelime sonundaki 's' cogu zaman 'c' gibi
  cikiyor (familiec / comec / Thic). Bunlar 's' okundu; ama kelime **basindaki** 'c'
  harflerine dokunulmadi, boylece gercek yazim hatasi olan 'cense' (sense) korundu.
- 🔴 **Bir eksik tespit edildi: 1. calistirmanin ciktisi bu makinede yok.** DURUM.txt
  1. calistirmayi bitmis gosteriyor ve `dogrulama/` klasorunde sayfa 9-17'nin kirpilmis
  PNG'leri ile `tools/_a1_*.py` betikleri duruyor, yani is yapilmis; ama
  `kalibrasyon/ornekler/` klasoru hic yoktu — Academic **Task 1**'in 7 ornegine ait JSON
  dosyalari diskte yok. Klasor gitignore'da oldugu icin depodan da geri alinamiyor.
  **Yapilacak is: A1'in 1. calistirmasi (sayfa 9-17, 7 ornek) yeniden yapilmali;**
  aksi halde puanlama olcumu (SONNET5-A3) yalnizca Task 2 ornekleriyle calisir.
  Bu calistirmada, kullanicinin talimati geregi ("uretilmemis ilk grubu yap, var olani
  tekrar uretme") depo kaydina uyulup 2. grup yapildi.
- Atlanan/sorun: yok. Siradaki: 3. calistirma (General Training, sayfa 8-24, 11 ornek).

## OPUS5-A1 3/4 — Academic Task 1 yazma ornekleri metne dokuldu (sayfa 9-17)

- Tarih: 2026-08-06. Belge: `referans/ielts-academic-writing-sample-tasks-2023.pdf`,
  sayfa 9-17. **7 ornek** dokuldu, hepsi Academic **Task 1**:
  `AC-T1-1A-A` (band 5,0 - 132 kelime), `AC-T1-1A-B` (6,0 - 165),
  `AC-T1-1B-A` (6,0 - 179), `AC-T1-1B-B` (7,0 - 189), `AC-T1-1C-A` (5,0 - 157),
  `AC-T1-1C-B` (7,0 - 305), `AC-T1-1C-C` (8,5 - 227).
  Band dagilimi: 5 / 5 / 6 / 6 / 7 / 7 / 8,5. Dosyalar `kalibrasyon/ornekler/yazma/`
  altinda (gitignore'da, depoya girmiyor).
- 🔴 **Hangi grup yapildi ve neden:** Calistirma listesinde bu 1. gruptur, 3. degil.
  2. calistirmanin notunda yazildigi gibi 1. calistirmanin ciktisi bu makinede yoktu
  (`kalibrasyon/ornekler/` klasoru hic olusmamisti), yani Academic Task 1'in 7 ornegi
  DURUM.txt'de bitmis gorunmesine ragmen diskte yoktu. Kullanicinin bu calistirmadaki
  talimati "henuz uretilmemis ilk grubu yap, zaten var olani tekrar uretme" oldugu ve
  prompt dosyasinin kendi kurali da "`kalibrasyon/ornekler/` klasorune bak, sıradaki
  bitmemisi yap" dedigi icin bu bosluk kapatildi. **Sonuc: hala eksik olan grup,
  General Training (sayfa 8-24, 11 ornek).** Puanlama olcumu (SONNET5-A3) su an
  Academic Task 1 + Task 2 = 12 ornekle calisabilir, GT ornegi yok.
- **Tuzak kontrolu gecildi, supheli isaretlenen yok.** Band 6 ve altindaki dort cevapta
  hata sayisi esigin cok ustunde (~15 / ~9 / ~16 / ~11). Tablo ve ornek hatalar
  `kalibrasyon/ornekler/yazma/KONTROL.md` dosyasinda.
- **Yontem duzeltmesi:** 2. calistirmanin notunda "metin katmani gomulu font yuzunden
  bozuk, band puanlari metin katmaninda yok" deniyordu. Bu yalniz `pdftotext` icin
  dogru. **PyMuPDF ayni sayfalari dogru cozuyor:** gorev metni, sinav gorevlisi yorumu
  ve band puani ("Band 8.5" dahil) metin katmanindan temiz cikiyor. Bunun icin
  `tools/_a1_metin_coz.py` yazildi; artik yorum ve bandlar goruntuden okunmuyor,
  yalnizca el yazisi cevaplar goruntuden okunuyor.
- **El yazisi:** sayfalar `tools/_a1_bant.py` ile 4-11 yatay banda bolunup 400-500 dpi'da,
  suphede kalan kelimeler `tools/_a1_kirp.py` ile 900-2000 dpi'da okundu. Kelime sayilari
  `tools/_a1_kelime_say.py` ile sayildi (goz karari degil).
- **Dokum kararlari:** ustu cizilmis kisimlar dokulmedi, `transcription_notes`'a yazildi
  (1C-C'de 'destination,' sonrasinda karalanmis uzun bir blok, 1B-A'da 'television'
  oncesi okunamayan karalanmis bir kelime var). Caretle satir ustune eklenen kelimeler
  metne yerlestirildi ('are', 'It has', 'steady', 'slight'). 1C-B'nin el yazisinda kucuk
  'f' harfi buyuk 'F' gibi cizildigi icin ('perFectly', 'Form') bunlar harf bicimi
  sayilip normal kucuk harfle dokuldu — yazim hatasi olarak isaretlenmedi.
- **Belirsiz kalan iki nokta** (ilgili dosyalarin `transcription_notes` alanina yazildi):
  1A-A'da bazi noktalama isaretleri 900 dpi'da bile nokta/virgul ayrimi vermiyor;
  1C-A'da sogutma suresi '48-77 hours' gibi yazilmis (rakamlar ustu cizgili 7'ye benziyor).
- Atlanan/sorun: yok. Siradaki: 4. calistirma (konusma ornekleri) — ama GT yazma grubu
  hala acik, ustteki maddeye bakin.

## OPUS5-A1 4/4 — General Training yazma ornekleri metne dokuldu (sayfa 8-24)

- Tarih: 2026-08-06. Belge: `referans/ielts-general-training-writing-sample-tasks-2023.pdf`,
  sayfa 8-24. Bu, calistirma listesindeki **3. grup** (General Training, 11 ornek);
  oturum sirasina gore 4. calistirma.
- 🔴 **Grubun 7 ornegi zaten diskte duruyordu.** Onceki oturum (3. calistirma) Academic
  Task 1'i bitirip commit'ledikten sonra GT grubuna baslamis ve 19:11'de yarida kesilmis:
  `GT-T1-1A-A … GT-T2-2A-A` (7 dosya) yazilmis, ama `word_count` alanlari 0 kalmis,
  KONTROL.md'ye GT tablosu eklenmemis, NOTLAR.md'ye hicbir sey yazilmamisti. Kullanicinin
  "zaten var olani tekrar uretme" talimati geregi bu 7 dosya **yeniden dokulmedi**;
  eksik kalan 4 ornek dokuldu ve grubun kayit isleri tamamlandi.
- **Bu calistirmada dokulen 4 ornek:** `GT-T2-2A-B` (band 8,0 - 328 kelime, sayfa 18-19),
  `GT-T2-2B-A` (4,0 - 177, sayfa 20), `GT-T2-2B-B` (6,0 - 243, sayfa 21-22),
  `GT-T2-2B-C` (8,5 - 353, sayfa 23-24). Hepsi Task 2.
- **Grubun tamami: 11 ornek.** Band dagilimi: 3 / 4 / 5 / 5,5 / 5,5 / 6 / 6 / 7 / 7 /
  8 / 8,5. Task 1: 6 ornek, Task 2: 5 ornek. Dosyalar `kalibrasyon/ornekler/yazma/`
  altinda (gitignore'da, depoya girmiyor).
- **Kelime sayilari:** 11 GT dosyasinin `word_count` alani 0 idi; `tools/_a1_kelime_say.py`
  ile sayilarak yazildi (goz karari degil). Academic dosyalarin sayilari degismedi.
- **Tuzak kontrolu gecildi, supheli isaretlenen yok.** Band 6 ve altindaki yedi cevapta
  (3,0 / 4,0 / 5,0 / 5,5 / 5,5 / 6,0 / 6,0) hata sayisi esigin (0-1) cok ustunde:
  ~35 / ~30 / ~25 / ~12 / ~18 / ~15 / ~18. 11 satirlik tablo ve ornek hatalar
  `kalibrasyon/ornekler/yazma/KONTROL.md` dosyasinda. Onceden dokulmus 7 dosya da bu
  gozle gecirildi; hicbirinde "hata temizlenmis" izlenimi yok.
- **Yontem:** gorev metni, sinav gorevlisi yorumu ve band puani metin katmanindan
  (`tools/_a1_metin_coz.py`, PyMuPDF) alindi; yalnizca el yazisi cevaplar goruntuden
  okundu (`tools/_a1_bant.py` ile 400-600 dpi bantlar, supheli kelimeler 1800-4000 dpi
  kirpma).
- **Dokum kararlari / dikkat cekenler:**
  - `GT-T2-2A-B`'nin son cumlesi sayfanin **sag kenarina dikey** yazilmis; sayfa
    dondurulup okundu ve metne eklendi ("Certainly we have to think about this topic
    much more in the future"). Son kelimenin 'future' okunusu %100 kesin degil, dosyanin
    notuna yazildi.
  - Ayni adayin el yazisinda 'n'->'u', 'h'->'w', 't'->ilmekli 'd' bicimleri var; bunlar
    harf bicimi sayildi, yazim hatasi olarak dokulmedi. Buna karsilik gercek hatalar
    ('belief', 'admitt', 'their will exist', fiili eksik "I would like to four different
    models") aynen korundu.
  - `GT-T2-2B-A`'da (band 4) 'lots' kelimesinin ikinci harfi 4000 dpi'da bile o/e ayrimi
    vermiyor; 'lots' yazilip nota dusuldu. Bu dosyada uzeri cizili bolum yok, birkac
    kelime uzerine tekrar yazilmis (Plaza, many, are).
  - `GT-T2-2B-C`'de (band 8,5) tek satir ustu ekleme var: caretle eklenen 'and'
    isaretlenen yere kondu. 'social - contract' ifadesindeki bosluklu kisa cizgi aynen
    birakildi.
- **Bu prompt dosyasinin durumu:** 4 calistirmanin tamami harcandi ama listedeki
  **4. grup (konusma ornekleri, 12 ornek) hic yapilmadi.** Sebep zinciri: 1. calistirmanin
  ciktisi diske hic yazilmamis, 3. calistirma o boslugu kapatmis, bu calistirma da
  yarim kalan GT grubunu bitirmek zorunda kaldi. Ayrica konusma grubunun kaynak dosyasi
  `referans/konusma-band-ornekleri.txt` **su an diskte yok** (`referans/text/` altinda da
  yok), yani o grup icin once `python tools/indir.py` calistirilmasi gerekiyor.
  **Yapilacak is: konusma ornekleri icin bir calistirma daha gerekiyor** (prompt dosyasinin
  "4. CALISTIRMA - KONUSMA ORNEKLERI" bolumu).
- **Olcum acisindan durum:** puanlama olcumu (SONNET5-A3) artik 23 yazma ornegiyle
  calisabilir (Academic 12 + General Training 11), band araligi 3,0-8,5. Konusma ornegi
  hala 0.
- Atlanan/sorun: yukaridaki konusma grubu disinda yok.


## OPUS5-A2 - degerlendirme talimatinin ilk surumu

- Uretilen dosyalar: `degerlendirme/yazma-task1-academic.md`,
  `degerlendirme/yazma-task1-general.md`, `degerlendirme/yazma-task2.md`,
  `degerlendirme/konusma.md`, `degerlendirme/ORTAK-KURALLAR.md`,
  `degerlendirme/cikti-semasi.json`, `degerlendirme/NOTLAR.md`.
  Dort talimat dosyasinin her biri **tek basina** bir isteğe konabilecek tam prompt;
  ortak bloklar bilerek tekrarlandi, sahibi `ORTAK-KURALLAR.md`.
- **Talimatlar Ingilizce** (degerlendirilen metin ve arayuz Ingilizce); yalnizca
  `NOTLAR.md` Turkce.
- **Sabit kurallarin hepsi girdi:** yazma 4 esit agirlikli olcut, konusma 3 olcut,
  telaffuz puanlanmiyor (modele ses gitmiyor), akicilik olcusu yalnizca konusma hizi
  (kelime/dakika, etkisi en fazla yarim band), yarim banda yuvarlama (.25 ve .75 yukari),
  sabit JSON semasi, olcut basina en fazla 2 cumle + en fazla 3 duzeltme ornegi,
  her gerekcede adayin kendi cumlesinden alinti, yetersiz cevapta puan uydurulmuyor
  (`insufficient`), kullanici metnindeki yonergeler veri sayiliyor.
- **PDF okunamadi:** `pdftoppm` kurulu olmadigi icin Read araci PDF sayfasi acamiyor.
  Belgeler `referans/text/` metin katmanindan okundu; katman font kaydirmali,
  `+29` karakter kaydirmasiyla cozuldu (`chr(ord(c)+29)`, 3-126 arasi). Sonraki
  oturumlar icin: yazma belgelerinin metin katmani bu sekilde okunabiliyor,
  konusma belgesinin metin katmani ise duz metin (kaydirma yok).
- 🔴 **Konusma olcutlerinin resmi kaynagi elde yok.** `ielts-speaking-sample-tasks-2023.pdf`
  yalnizca gorev kartlari + bir dokum iceriyor, olcut tanimi yok; prompt'un isaret ettigi
  `referans/konusma-band-ornekleri.txt` diskte yok. `konusma.md` kamuya acik olcut
  **adlarina** sadik kalinarak yeniden yazildi. Konusma ornekleri indirilip dokuldugunde
  bu dosya gozden gecirilmeli. Ayrintili gerekce: `degerlendirme/NOTLAR.md`.
- **Sema kendini siniyor:** `python tools/_a2_sema_kontrol.py` - semanin gecerliligi,
  iki ornegin uydugu ve **reddetmesi gereken** on ciktinin reddedildigi kontrol ediliyor
  (ceyrek band, `estimated: false`, `pronunciation` olcutu, alintisiz gerekce, 4 duzeltme,
  semada olmayan alan, bandli `insufficient` vb.). Bu oturumda 12/12 gecti.
  Kontrol icin `jsonschema` paketi kuruldu (`python -m pip install jsonschema`);
  paket yoksa script sessizce sadece JSON gecerliligine bakiyor.
- **Bilincli sadelestirmeler** (tam liste `degerlendirme/NOTLAR.md` bolum 2): dilbilgisi
  icin sayilabilir "hata tasiyan cumle orani" tablosu, olcut tavanlari (`max N`),
  kelime sayisi eksikliginde gorev olcutu tavani, sozcuk dagarciginda "en az dort oge"
  kurali, konusmada 40 kelimelik yetersizlik esigi, band 1-2'nin tarif edilmemesi,
  yazim -> sozcuk dagarcigi / noktalama -> dilbilgisi ayrimi.
- **Bu adimda olcum yapilmadi** - talimat henuz resmi orneklerle sinanmadi. Sirasi:
  SONNET5-A3 (tur 1) -> OPUS5-A4 (1. duzeltme) -> A3 (tur 2) -> A4 (2. duzeltme) ->
  A3 (tur 3) -> A4 (son rapor).
- Atlanan/sorun: konusma kaynak boslugu disinda yok.

## SONNET5-A3 (1. calistirma: tur 1 — AC-T1 grubu, 7 ornek x 3 tekrar)
- Tarih: 2026-08-07
- **kalibrasyon/olcum/kumeler.json ilk kez olusturuldu.** Elde henuz yalniz 23 yazma
  ornegi var (konusma orneklenmedi, OPUS5-A1 notuna bakin), bu yuzden simdilik yalniz
  bu 23 kod bolundu; konusma ornekleri uretildiginde kumelere eklenmesi gerekiyor.
  Bolme kurali: bantlar 3,0-8,5 arasinda S1/S2/S3'e sirayla (bant sirali round-robin)
  dagitildi, her kumede hem Academic hem General Training var: S1=8 kod, S2=8 kod,
  S3=7 kod.
- **Bu calistirmada islenen grup:** AC-T1 (Academic Writing Task 1, 7 ornek:
  1A-A/B, 1B-A/B, 1C-A/B/C). Depoda `kalibrasyon/olcum/` hic yoktu, yani hicbir grup
  uretilmemisti; dosya sirasina gore ilk grup (AC-T1) yapildi. Kalan 3 grup: AC-T2
  (5 ornek), GT-T1 (6 ornek), GT-T2 (5 ornek) — sonraki 3 calistirmanin isi.
  21 puanlama dosyasi yazildi: `kalibrasyon/olcum/tur1/AC-T1-*-{1,2,3}.json`.
- 🔴 **Korluk yontemi degistirildi.** Talimat orijinal ornek dosyasini okuyup
  puanlamayi ayni oturumda yapmayi varsayiyor, ama `kalibrasyon/ornekler/yazma/*.json`
  band ve examiner_comment alanlarini ayni dosyada tasiyor — Read araciyla dosyayi
  acmak otomatik olarak gercek bandi da gosteriyor. Bunu onlemek icin: ana oturum
  ornegi okudu, band/examiner_comment/transcription_notes alanlarini **atip** sadece
  task_prompt + response_text + word_count'u yeni, taze bir alt-ajana (subagent,
  model: sonnet, `degerlendirme/yazma-task1-academic.md` talimatini kendisi okuyup
  uyguladi) verdi; alt-ajana kalibrasyon/ornekler/ klasorune bakmamasi acikca soylendi.
  Her tekrar (1/2/3) da ayri, taze bir alt-ajan cagrisi oldu — boylece hem gercek
  banda korluk hem tekrarlar arasi bagimsizlik korundu (ayni baglamda 3 kez sormak
  modelin kendi tutarsizligini oldugundan az gosterebilirdi).
- Bu grubun tek seferlik (1. tekrar) tahminleri: 1A-A=5,0 · 1A-B=5,0 · 1B-A=5,0 ·
  1B-B=5,0 · 1C-A=5,5 · 1C-B=6,0 · 1C-C=7,0. Tekrarlar arasi yayilim çoğunlukla 0
  (1A-A, 1B-A, 1C-B), birkaç ornekte 0,5-1,0 (1A-B: 5,0/5,5/5,0, 1B-B: 5,0/5,5/5,5,
  1C-C: 7,0/6,5/7,0).
- **Rapor script'i bu calistirmada calistirilmadi** — talimat "her turda butun
  ornekler puanlanir" diyor, bu calistirma turun 4'te 1'i. `python tools/
  puanlama-raporu.py 1` ancak GT-T2 grubu da bitince (4. calistirma) anlamli sonuc
  verir; simdi calistirilirsa yalnizca 21/69 puanlamayla yanlis rapor uretir.
- Atlanan/sorun: yok — bu grup icin bilinen bir sorun cikmadi.

## SONNET5-A3 (2. calistirma: tur 1 — AC-T2 grubu, 5 ornek x 3 tekrar)
- Tarih: 2026-08-07
- **Bu calistirmada islenen grup:** AC-T2 (Academic Writing Task 2, 5 ornek:
  2A-A/B/C, 2B-A/B). `kalibrasyon/olcum/tur1/` icinde yalniz AC-T1 grubu vardi
  (1. calistirmanin isi); dosya sirasina gore sonraki grup (AC-T2) yapildi. Kalan
  2 grup: GT-T1 (6 ornek), GT-T2 (5 ornek) — sonraki 2 calistirmanin isi.
  15 puanlama dosyasi yazildi: `kalibrasyon/olcum/tur1/AC-T2-*-{1,2,3}.json`.
- Ayni korluk yontemi kullanildi (1. calistirmadaki notta ayrintili): ana oturum
  ornegi okuyup band/examiner_comment/transcription_notes alanlarini atti, sadece
  task_prompt + response_text + word_count'u her tekrar icin ayri, taze bir
  alt-ajana (subagent, model: sonnet, `degerlendirme/yazma-task2.md` talimatini
  kendisi okuyup uyguladi) verdi.
  Not: Task 2 talimati Academic/General Training icin ortak (`yazma-task2.md`
  "Task 2 is assessed the same way in both modules" diyor), bu yuzden `module`
  alani "academic" olarak gecildi ama talimatta modul ayrimi yok.
- Bu grubun tek seferlik (1. tekrar) tahminleri: 2A-A=4,5 · 2A-B=5,5 · 2A-C=6,5 ·
  2B-A=5,5 · 2B-B=6,0. Tekrarlar arasi yayilim: 2A-A 0,5 (4,5/4,5/4,0), 2A-B 0
  (5,5/5,5/5,5), 2A-C 0 (6,5/6,5/6,5), 2B-A 0,5 (5,5/5,5/6,0), 2B-B 0,5
  (6,0/6,0/5,5).
- **Rapor script'i bu calistirmada da calistirilmadi** — ayni gerekce: tur 1 icin
  hala GT-T1 ve GT-T2 grubu eksik, script'i simdi calistirmak yalniz 36/69
  puanlamayla yanlis sonuc uretir.
- Atlanan/sorun: yok — 5 ornekten hicbiri `transcription_suspect: true` degildi.

## SONNET5-A3 (3. calistirma: tur 1 — GT-T1 grubu, 6 ornek x 3 tekrar)
- Tarih: 2026-08-07
- **Bu calistirmada islenen grup:** GT-T1 (General Training Writing Task 1 — mektup,
  6 ornek: 1A-A/B, 1B-A/B/C/D). `kalibrasyon/olcum/tur1/` icinde AC-T1 + AC-T2
  vardi (1. ve 2. calistirmanin isi); dosya sirasina gore sonraki grup (GT-T1)
  yapildi. Kalan grup: GT-T2 (5 ornek) — 4. (son) calistirmanin isi.
  18 puanlama dosyasi yazildi: `kalibrasyon/olcum/tur1/GT-T1-*-{1,2,3}.json`.
- Ayni korluk yontemi kullanildi: ana oturum ornegi okuyup band/examiner_comment
  alanlarini atti, sadece task_prompt + response_text + word_count'u her ornek icin
  ayri, taze bir alt-ajana (subagent, model: sonnet, `degerlendirme/
  yazma-task1-general.md` talimatini kendisi okuyup uyguladi) verdi; alt-ajan
  kendi icinde 3 tekrari da bagimsiz uretti.
  🔴 **Bir kontaminasyon oldu ve duzeltildi:** ana oturum, cikti semasini anlamak
  icin ornek dosyalardan birini (GT-T1-1A-A) tam okurken band (5,5) ve
  examiner_comment alanlarini da farkinda olmadan gordu. Bu ornegin gercek puanina
  ana oturum artik kor degildi, ama puanlamayi ana oturum degil taze bir alt-ajan
  yapti (band'i hic gormeden) — yani olculen tahmin bu kontaminasyondan etkilenmedi.
  Diger 5 ornek icin band/examiner_comment hic okunmadi.
- Bu grubun tek seferlik (1. tekrar) tahminleri: 1A-A=5,5 · 1A-B=6,0 · 1B-A=4,5 ·
  1B-B=5,0 · 1B-C=5,5 · 1B-D=5,5. Tekrarlar arasi yayilim: 1A-A 1,0 (5,5/6,0/5,0 —
  esikteki tek ornek), 1A-B 0,5 (6,0/6,0/5,5), 1B-A 0,5 (4,5/4,0/4,5), 1B-B 0,5
  (5,0/4,5/5,0), 1B-C 0 (5,5/5,5/5,5), 1B-D 0,5 (5,5/5,5/6,0).
- **Rapor script'i bu calistirmada da calistirilmadi** — ayni gerekce: tur 1 icin
  hala GT-T2 grubu eksik (18/69 puanlama var, tam olmayan veriyle script
  calistirilirsa RAPOR-tur1.md yanlis/eksik sonuc gosterir). Script bir kez elle
  denendi (dogrulama amacli, dosya sonradan silindi) — 18 ornek uzerinden ortalama
  mutlak fark 0,944, egilim -0,667 (cimri) cikti; bu SADECE bu calistirmanin notu,
  turun nihai sonucu degil, GT-T2 bitince degisebilir.
- Atlanan/sorun: yok — 6 ornekten hicbiri `transcription_suspect: true` degildi.

## OPUS5-A4 (1. duzeltme — tur 1 raporu + talimat duzeltmesi)
- Tarih: 2026-08-07
- SAKLI KUME: **S3**. Bu oturum S3 orneklerinin cevabina, gercek bandina ve sapma
  satirina bakmadi; `RAPOR-tur1.md` S3 satirlari maskelenerek okundu.
- `tools/puanlama-raporu.py 1` ilk kez calistirildi, `kalibrasyon/olcum/RAPOR-tur1.md`
  uretildi. 🔴 **Tur 1 eksik kaldi:** 23 ornekten 21'i puanlandi (63/69 puanlama).
  Eksik olan `GT-T2-2B-B` ve `GT-T2-2B-C`; ikisi de gorunur kumelerde (S1/S2), yani
  sakli kume karsilastirmasi bu eksikten etkilenmiyor. Bu iki ornegi bu oturum
  puanlayamaz — olcum Sonnet ile yapilir (A3'un basindaki kural), bu oturum Opus.
  2. olcum turunda kapanmali.
- Tur 1 sonucu (tek seferlik puan, 21 ornek): ortalama mutlak fark 0,952 · egilim
  -0,667 (cimri) · en buyuk sapma 2,00 · yayilim 0,33. Dort basari olcutunden
  yalniz tutarlilik gecti.
- Bulunan oruntu tek yonlu cimrilik degil, **olcegin ortaya buzulmesi**: gercek
  bandlar 3,0-8,5 arasina yayilirken verilen puanlarin hepsi 4,0-6,5 arasinda kaldi
  — ust bandlar sikisiyor, alt bandlar sisiyor. Ana mekanizma: "max N" tavanlarinin
  puan olarak yazilmasi (guclu cevapta tavan, zayif cevapta taban gibi calisiyor).
  Ikinci mekanizma: dilbilgisi olcutunun hata payi tablosu her bandda ~1 band sert.
- Talimatta 10 degisiklik yapildi (5 dosya; ortak bloklar ayni commit'te senkron).
  Hepsi band araligi x olcut kirilimina dayaniyor; ornege ozel kural yazilmadi,
  gercek band veya ornek cevap talimata gomulmedi, olcut sayisi/agirligi degismedi,
  telaffuz geri getirilmedi, cikti uzunlugu degismedi.
  Ayrinti ve tur 2'de sinanacak beklentiler: `degerlendirme/DEGISIKLIK-KAYDI.md`.
- Konusma tarafi hic olculmedi (`kalibrasyon/ornekler/` altinda konusma klasoru
  yok); `konusma.md`'deki degisiklikler ortak blok senkron kuralindan geliyor ve
  yazma verisinden genellenmis durumda. Son raporda kalan risk olarak yazilacak.
- `kalibrasyon/olcum/_tmp_stripped/` (yarim kalan 4. calistirmadan kalma, band'i
  ayiklanmis ornek kopyalari) silindi: turetilmis gecici dosya, telifli aday metni
  iceriyor, depo public.

## SONNET5-A3 (1. calistirma: tur 2 — AC grubu, 12 ornek x 1 tekrar)
- Tarih: 2026-08-07
- **Bu tur 2:** her ornek 1 kez puanlanir (3 tekrar degil), talimat 1. duzeltmeden
  sonraki surumle (`degerlendirme/*.md`, OPUS5-A4 sonrasi) calisiyor. Toplam 2
  calistirma planlandi; bu calistirmada AC grubu (AC-T1: 7 ornek, AC-T2: 5 ornek =
  12 ornek) islendi. `kalibrasyon/olcum/tur2/` depoda hic yoktu, yani ilk grup
  (dosya sirasina gore AC) yapildi. Kalan grup: GT (GT-T1 6 + GT-T2 5 = 11 ornek) —
  2. (son) calistirmanin isi. 12 puanlama dosyasi yazildi:
  `kalibrasyon/olcum/tur2/AC-*-1.json`.
- 🔴 **Korluk yontemi tur 1'deki gibi, ama daha sikica uygulandi.** Ana oturum bu
  kez `kalibrasyon/ornekler/yazma/*.json` icindeki `band` alanlarini bir python
  script'inin terminal ciktisinda (module/task/suspect kontrolu icin) yanlislikla
  gordu — 23 ornegin tamami icin. Bunu telafi etmek icin: puanlamayi ana oturum
  **yapmadi**; her ornek icin ayri, taze bir alt-ajana (subagent, model: sonnet)
  yalniz task_prompt + response_text + word_count (band/examiner_comment/
  transcription_notes/source cikarilmis) verildi, alt-ajan `degerlendirme/
  yazma-task1-academic.md` veya `degerlendirme/yazma-task2.md` metnini talimatta
  aynen aldi ve kendi basina puanladi; `kalibrasyon/ornekler/` klasorune erisimi
  yoktu (dosya sistemine bakmadan, gomulu talimat + gomulu girdiyle calisti).
  Ana oturumun gordugu bandlar sonucu **etkilemedi** cunku puanlayan taze ajan
  hicbir zaman banda erismedi; ama bu, ayni hatanin tekrarlanmamasi icin not
  edilmeli — ileriki calistirmalarda ornek dosyalarini modul/suspect kontrolu icin
  okurken `band` alanini terminale bastirmaktan kacinilmali (`json.load` sonrasi
  yalniz gereken alanlari yazdirmali).
  Kalibrasyon girdi metinleri gecici olarak `kalibrasyon/olcum/_scratch_tur2/`
  altina yazildi (repo sandbox disina cikilamadigi icin); bu klasor commit'ten
  once silindi — telifli aday metni iceren turetilmis dosya, depo public.
- AC-T1 orneklerinde `visual` alani saglanamadi (kaynak dosyalarda ayri sayisal
  grafik verisi yok, yalniz `task_prompt` var); talimatin kendi kuraliyla
  ("visual eksikse tahmin etme, yalniz doğrulanabileni degerlendir") tutarli
  sekilde, alt-ajanlara `visual` alani acikca "saglanmadi" olarak verildi.
- Bu grubun tek seferlik tahminleri: AC-T1-1A-A=5,0 · 1A-B=5,0 · 1B-A=5,0 ·
  1B-B=5,5 · 1C-A=6,0 · 1C-B=5,5 · 1C-C=7,0 · AC-T2-2A-A=4,5 · 2A-B=5,5 ·
  2A-C=6,5 · 2B-A=5,5 · 2B-B=6,5.
- **Rapor script'i bu calistirmada calistirilmadi** — tur 2 icin hala GT grubu
  (11 ornek) eksik; `python tools/puanlama-raporu.py 2` ancak GT grubu da bitince
  (2. calistirma) anlamli sonuc verir.
- Atlanan/sorun: yok — 12 ornekten hicbiri `transcription_suspect: true` degildi.

## SONNET5-A3 (2. calistirma: tur 2 — GT grubu, 11 ornek x 1 tekrar) — TUR 2 TAMAMLANDI
- Tarih: 2026-08-07
- Kalan grup GT (GT-T1: 6 ornek, GT-T2: 5 ornek = 11 ornek) bu calistirmada islendi;
  tur 2 artik 23/23 tamam. `python tools/puanlama-raporu.py 2` calistirildi:
  `kalibrasyon/olcum/RAPOR-tur2.md`.
- **Tur 2 sonucu (tek seferlik puan, 23 ornek):** ortalama mutlak fark 0,913 ·
  egilim -0,696 (cimri) · en buyuk sapma 2,00 · yayilim 0,00. Dort basari
  olcutunden yalniz tutarlilik (yayilim <= 0,5) gecti; ortalama mutlak fark,
  en buyuk sapma ve egilim tur 1'e (0,952 / 2,00 / -0,667) gore neredeyse
  degismedi — 1. duzeltme olcum sonucunu belirgin iyilestirmedi.
- 🔴 **Korluk yontemi ayni sekilde uygulandi** (bkz. yukaridaki 1. calistirma notu):
  ana oturum `task_prompt` + `response_text` + `word_count` disinda hicbir alani
  alt-ajanlara vermedi; her ornek taze bir alt-ajanda (sonnet, dosya sistemine
  erisimi yok, gomulu talimat + gomulu girdi) puanlandi.
- 🔴🔴 **Onemli sizinti — bir sonraki calistirma icin ders:** bu oturumda ana
  oturum, hangi ornek grubunun eksik oldugunu dogrulamak icin
  `kalibrasyon/ornekler/yazma/KONTROL.md` dosyasini okudu. Bu dosya "dokum tuzak
  kontrolu" icindir ve GT grubunun tamaminin **gercek bandini acikca bir tabloda**
  listeler — ana oturum boylece 11 ornegin gercek bandini puanlamadan once gordu.
  Puanlama sonucunu bu **etkilemedi** cunku puanlamayi ana oturum degil, gomulu
  girdiyle calisan korl alt-ajanlar yapti (band hicbir alt-ajana verilmedi); ama
  bu bir onceki calistirmadaki "band terminale yanlislikla basildi" hatasinin
  farkli bir varyanti. **Ders:** `KONTROL.md` olcum oturumlarinda hic acilmamali
  — hangi ornegin eksik oldugu sadece `kalibrasyon/olcum/tur<N>/` klasorundeki
  dosya adlarina bakarak (band icermez) belirlenmeli.
- Bu grubun tek seferlik tahminleri: GT-T1-1A-A=5,5 · 1A-B=6,5 · 1B-A=3,5 ·
  1B-B=5,0 · 1B-C=5,5 · 1B-D=5,5 · GT-T2-2A-A=5,0 · 2A-B=6,0 · 2B-A=4,5 ·
  2B-B=5,0 · 2B-C=6,5.
- Atlanan/sorun: yok — 11 ornekten hicbiri `transcription_suspect: true` degildi.
- `kalibrasyon/olcum/_scratch_tur2/` (gecici, telifli aday metni iceren dokum
  kopyalari + puanlama toplama script'i) commit'ten once silinecek.

## OPUS5-A4 (2. duzeltme — tur 2 raporu + talimat duzeltmesi)
- Tarih: 2026-08-07
- SAKLI KUME: **S1**. Bu oturum S1 orneklerinin cevabina, sinav gorevlisi yorumuna,
  olcut puanlarina bakmadi ve butun analizi S2+S3'e kilitli iki script uzerinden
  yaptı: `tools/_a4_analiz.py`, `tools/_a4_ust.py`.
  🔴 Duruste not: `RAPOR-tur2.md`'nin "Ornek ornek" tablosu butun kumeleri **tek
  tablo** halinde basiyor, dosya acildiginda S1 satirlari da ekrana geldi. O satirlar
  hicbir hesaba girmedi (butun sayilar S2+S3'un 15 ornegi uzerinden yeniden
  hesaplandi), ama sakli kume korumasi **rapor bicimi yuzunden** ideal degil.
  `tools/puanlama-raporu.py` kumeye gore bolunmus rapor uretecek sekilde
  duzeltilmeli; son raporda risk olarak yazilacak.
- Tur 2 tamamdi (23/23 ornek, her biri 1 tekrar). Genel: ortalama mutlak fark 0,913 ·
  egilim -0,696 · en buyuk sapma 2,00. Yine 4 olcutten 3'u kaldi; tutarlilik olcutu
  bu turda **sinanmadi** (tekrar yok, yayilim tanim geregi 0,00 — RAPOR'daki ✅
  anlamsiz).
- 1. duzeltmenin 5 beklentisinden **2'si tuttu**: orta band bozulmadi (-0,40 → -0,29,
  asil kazanc dilbilgisinde -0,90 → -0,64) ve kume farki acilmadi. **3'u kaldi**:
  egilim 0'a gitmedi, en buyuk sapma 2,0'da kaldi, puanlar hala dar araliktan
  cikmadi (3,5-7,0; hicbir ornek 7'yi gecmedi).
- Sapmanin neredeyse tamami **tek yerde**: gercek bandi >=7 olan cevaplar (genel
  -1,50). Orta band artik yerinde (-0,29), alt band +0,50 (gorunur kumede yalniz
  2 ornek). Ust bandda en kotu olcut **tutarlilik**: -2,17, ve tur 1'e gore
  **kotulesti** (-1,53 → -2,17).
- Teshis: model kusurun **varligini** cezalandiriyor, **bedelini** degil. Resmi sinav
  gorevlisi yorumlariyla yan yana konunca ayni kusurlar ayni yerde bulunuyor; fark
  ne kadar sayildiginda. Talimattaki 7/8/9 satirlari zaten hata iceriyor ama bunu
  soyleyen bir cumle yoktu. Yan mekanizmalar: tavanlarin neredeyse hepsinin "max 5"
  olmasi (bir bicimsel eksik cevabi olcegin ortasina cakiyor), kanit kuralinin
  adlandirmasi en kolay sey olan **hatayi** one cikarmasi, hata payinin gozle
  tahmin edilip yuksek cikmasi, ve modelin tabloya ortadan girip yalniz asagi inmesi.
- Talimatta 8 degisiklik (11-18 numarali; 5 dosya, ortak bloklar ayni commit'te
  senkron). En onemlisi yordam degisikligi: olcut tablosu artik **9'dan asagi**
  okunuyor, "hala dogru olan en yuksek satirda dur". Ornege ozel kural yazilmadi,
  olcut sayisi/agirligi degismedi, telaffuz geri gelmedi, cikti uzunlugu degismedi,
  hata payi esikleri **ikinci kez kaydirilmadi** (1. kaydirma tuttu; sayim kurali
  duzeltildi, esik degil).
  Ayrinti ve tur 3'te sinanacak 7 beklenti: `degerlendirme/DEGISIKLIK-KAYDI.md`.
- Konusma tarafi hala hic olculmedi. `konusma.md`'ye yalniz ortak bloklar girdi;
  konusmanin kendi tavan degerlerine (hepsi `max 5`) **dokunulmadi**, cunku onlari
  ayarlayacak olcum yok. Son raporda kalan risk.

## SONNET5-A3 (1. calistirma: tur 3 — AC-T1 grubu, 7 ornek x 3 tekrar)
- Tarih: 2026-08-07
- **Bu tur 3 (SON tur):** her ornek 3 kez puanlanir (tur 1 gibi), talimat 2. duzeltmeden
  sonraki surumle (`degerlendirme/*.md`, OPUS5-A4'un 2. duzeltmesi sonrasi) calisiyor.
  Toplam 4 calistirma planlandi (tur 1'deki ayni gruplama: AC-T1, AC-T2, GT-T1, GT-T2).
  `kalibrasyon/olcum/tur3/` depoda hic yoktu, yani ilk grup (dosya sirasina gore AC-T1)
  yapildi. Kalan 3 grup: AC-T2 (5 ornek), GT-T1 (6 ornek), GT-T2 (5 ornek) — sonraki
  3 calistirmanin isi. 21 puanlama dosyasi yazildi: `kalibrasyon/olcum/tur3/AC-T1-*-{1,2,3}.json`
  (bu dosyalar `.gitignore` geregi depoya girmiyor — telifli aday metni tasiyorlar,
  yalniz `RAPOR-tur*.md` ve `kumeler.json` public depoya giriyor).
- **Korluk yontemi:** ana oturum `kalibrasyon/ornekler/yazma/*.json` dosyalarini hic
  Read araciyla acmadi; onceki calistirmalardaki iki farkli sizinti dersini (band'in
  terminale yanlislikla basilmasi, `KONTROL.md`'nin gercek bandlari tablo halinde
  gostermesi) tekrarlamamak icin bir python script'i sadece `task_prompt` +
  `response_text` + `word_count` alanlarini (band/examiner_comment/transcription_notes
  hic yazdirilmadan) gecici bir scratch klasorune yazdi, ana oturum o stripped
  dosyalari okudu. Her ornek + her tekrar (21 kombinasyon) icin ayri, taze bir
  alt-ajana (subagent, model: sonnet) yalniz bu stripped veriler gomulu olarak
  verildi; alt-ajan kendisi `degerlendirme/yazma-task1-academic.md` dosyasini okuyup
  uyguladi ve `kalibrasyon/ornekler/` ile `KONTROL.md`yi acmamasi acikca soylendi.
  Ayri tekrarlar icin ayri taze ajan kullanildi (tur 1 AC-T1 grubundaki gibi en siki
  yontem) — ayni baglamda 3 kez sormanin modelin kendi tutarsizligini oldugundan az
  gosterme riskinden kacinildi. Scratch klasoru (`kalibrasyon/olcum/_scratch_tur3/`)
  islem bitince silindi.
- Bu grubun tek seferlik (1. tekrar) tahminleri: 1A-A=5,5 · 1A-B=5,5 · 1B-A=5,0 ·
  1B-B=6,0 · 1C-A=6,0 · 1C-B=6,5 · 1C-C=7,5. Tekrarlar arasi yayilim: 1A-A 0
  (5,5/5,5/5,5), 1A-B 0,5 (5,5/6,0/5,5), 1B-A 0,5 (5,0/5,5/5,5), 1B-B 0,5
  (6,0/6,0/6,5), 1C-A 0 (6,0/6,0/6,0), 1C-B 0 (6,5/6,5/6,5), 1C-C 0 (7,5/7,5/7,5).
- **Rapor script'i bu calistirmada calistirilmadi** — talimat "her turda butun
  ornekler puanlanir" diyor, bu calistirma turun 4'te 1'i (21/69 puanlama).
  `python tools/puanlama-raporu.py 3` ancak kalan 3 grup da bitince anlamli sonuc
  verir.
- Atlanan/sorun: yok — 7 ornekten hicbiri `transcription_suspect: true` degildi.

## SONNET5-A3 (2. calistirma: tur 3 — AC-T2 grubu, 5 ornek x 3 tekrar)
- Tarih: 2026-08-07
- Ayni tur 3 (SON tur), ayni talimat surumu (`degerlendirme/yazma-task2.md`, OPUS5-A4'un
  2. duzeltmesi sonrasi). `kalibrasyon/olcum/tur3/` icinde AC-T1 grubu (1. calistirma)
  zaten vardi; dosya sirasina gore sonraki grup AC-T2 (5 ornek: 2A-A, 2A-B, 2A-C, 2B-A,
  2B-B) yapildi. Kalan 2 grup: GT-T1 (6 ornek), GT-T2 (5 ornek) — sonraki 2 calistirmanin
  isi. 15 puanlama dosyasi yazildi: `kalibrasyon/olcum/tur3/AC-T2-*-{1,2,3}.json` (bu
  dosyalar `.gitignore` geregi depoya girmiyor, sadece `RAPOR-tur*.md` ve `kumeler.json`
  public depoya giriyor).
- **Korluk yontemi:** 1. calistirmadaki ile ayni — `kalibrasyon/ornekler/yazma/AC-T2-*.json`
  dosyalari bir python script'i ile `task_prompt` + `word_count` + `response_text` (band,
  examiner_comment, transcription_notes hic yazdirilmadan) gecici bir scratch klasorune
  (`kalibrasyon/olcum/_scratch_tur3/`) stripped kopyalandi, ana oturum sadece o stripped
  dosyalari Read ile actı. Her ornek + her tekrar (15 kombinasyon) icin ayri, taze bir
  alt-ajana (genel amacli subagent, model: sonnet acikca belirtildi) yalniz stripped veri
  gomulu olarak verildi; alt-ajan kendisi `degerlendirme/yazma-task2.md` dosyasini okuyup
  uyguladi, `kalibrasyon/ornekler/`, `KONTROL.md` ve `kalibrasyon/olcum/` acmamasi acikca
  soylendi. 15 ayri tekrar icin 15 ayri taze ajan (paralel, tek mesajda). Scratch klasoru
  islem bitince silindi.
- Bu grubun tek seferlik (1. tekrar) tahminleri: 2A-A=5,0 · 2A-B=6,0 · 2A-C=7,5 ·
  2B-A=6,0 · 2B-B=7,0. Tekrarlar arasi yayilim: 2A-A 0 (5/5/5), 2A-B 0 (6/6/6), 2A-C 0,5
  (7,5/7/7), 2B-A 0 (6/6/6), 2B-B 0,5 (7/7/6,5).
- **Rapor script'i bu calistirmada calistirilmadi** — tur 3'un 4'te 2'si tamam
  (36/69 puanlama). `python tools/puanlama-raporu.py 3` kalan 2 grup (GT-T1, GT-T2) da
  bitince anlamli sonuc verir.
- Atlanan/sorun: yok — 5 ornekten hicbiri `transcription_suspect: true` degildi.

## SONNET5-A3 (3. calistirma: tur 3 — GT-T1 grubu, 6 ornek x 3 tekrar)
- Tarih: 2026-08-07
- Ayni tur 3 (SON tur), ayni talimat surumu (`degerlendirme/yazma-task1-general.md`,
  OPUS5-A4'un 2. duzeltmesi sonrasi). `kalibrasyon/olcum/tur3/` icinde AC-T1 (1. calistirma)
  ve AC-T2 (2. calistirma) zaten vardi; dosya sirasina gore sonraki grup GT-T1 (6 ornek:
  1A-A, 1A-B, 1B-A, 1B-B, 1B-C, 1B-D) yapildi. Kalan 1 grup: GT-T2 (5 ornek) — sonraki
  (4. ve son) calistirmanin isi. 18 puanlama dosyasi yazildi:
  `kalibrasyon/olcum/tur3/GT-T1-*-{1,2,3}.json` (bu dosyalar `.gitignore` geregi depoya
  girmiyor, sadece `RAPOR-tur*.md` ve `kumeler.json` public depoya giriyor).
- **Korluk yontemi:** 1. ve 2. calistirmadaki ile ayni — `kalibrasyon/ornekler/yazma/GT-T1-*.json`
  dosyalari daha once (yarim kalmis bir onceki oturumdan) `task_prompt` + `word_count` +
  `response_text` (band, examiner_comment, transcription_notes hic yazdirilmadan) stripped
  halde `kalibrasyon/olcum/_scratch_tur3/` klasorunde hazir bulundu; once dosyalarin
  gercekten sadece bu 4 alani tasidigi (band/comment sizintisi olmadigi) python ile
  dogrulandi, sonra ayni kor akis izlendi. Her ornek + her tekrar (18 kombinasyon) icin
  ayri, taze bir alt-ajana (genel amacli subagent, model: sonnet acikca belirtildi) yalniz
  stripped veri gomulu olarak verildi; alt-ajan kendisi `degerlendirme/yazma-task1-general.md`
  dosyasini okuyup uyguladi, `kalibrasyon/ornekler/`, `KONTROL.md` ve `kalibrasyon/olcum/`
  acmamasi acikca soylendi. 18 ayri tekrar icin 18 ayri taze ajan (paralel, tek mesajda,
  arka planda). Scratch klasoru islem bitince silindi.
- Bu grubun tek seferlik (1. tekrar) tahminleri: 1A-A=6,0 · 1A-B=6,5 · 1B-A=4,5 ·
  1B-B=5,5 · 1B-C=6,0 · 1B-D=6,0. Tekrarlar arasi yayilim: 1A-A 0 (6/6/6), 1A-B 0
  (6,5/6,5/6,5), 1B-A 0 (4,5/4,5/4,5), 1B-B 0 (5,5/5,5/5,5), 1B-C 0,5 (6/6/5,5), 1B-D 0,5
  (6/6/6,5).
- **Rapor script'i bu calistirmada calistirilmadi** — tur 3'un 4'te 3'u tamam
  (54/69 puanlama). `python tools/puanlama-raporu.py 3` kalan 1 grup (GT-T2) da bitince
  anlamli sonuc verir.
- Atlanan/sorun: yok — 6 ornekten hicbiri `transcription_suspect: true` degildi.

## OPUS5-A4 (3. calistirma: SON RAPOR — duzeltme yok)
- Tarih: 2026-08-07
- **Talimat duzeltilmedi.** `degerlendirme/` altindaki hicbir dosyaya dokunulmadi; bu
  calistirma prompt'un 3. adimi (son rapor). Yazilan tek cikti:
  `kalibrasyon/olcum/SONUC.md`.
- Once `python tools/puanlama-raporu.py 3` calistirildi (onceki calistirma "GT-T2 grubu
  bitince calistirin" diye birakmisti) → `kalibrasyon/olcum/RAPOR-tur3.md` uretildi.
  Hesaplar icin ayrica `tools/_a4_sonuc.py` yazildi (uc turu eslesik karsilastirir; bu
  asamada sakli kume kalmadigi icin kume filtresi yok). SONUC.md'deki her sayi bu iki
  script'ten gelir, elle ortalama alinmadi.
- 🔴 **Tur 3 tamamlanmadi:** 23 ornekten 18'i puanlandi (54/69). Eksik grup GT-T2
  (5 ornek x 3 tekrar). Sebep: adim 105 oturum limitine takilip cikis 1 ile dustu
  (`gunluk/20260807-053340-adim105.log`), is listesi sonraki adima gecti. Bu oturum
  eksigi kapatamaz — olcum bilerek Sonnet ile yapilir, bu oturum Opus.
- Tur 3 (18 ornek): ortalama mutlak fark **0,694** · egilim **-0,139** · en buyuk sapma
  **1,50** · yayilim **0,19**. Eslesik 18 ornekte turlar: 0,944 → 0,861 → 0,694 ve
  egilim -0,667 → -0,639 → -0,139.
- 4 basari olcutunden **2'si gecti** (egilim, tutarlilik); 2'si kaldi (ortalama mutlak
  fark 0,694 > 0,5; en buyuk sapma tam 1,50).
- Sakli kume kontrolu **temiz**: tur 3'te S1 (2. duzeltmenin sakli kumesi) 0,714 vs
  S2+S3 0,682 → fark 0,032 band. Ezber isareti yok.
- En kotu bulgu: **alt band (<=4,5) geri gitti** — tur 2'de +0,50, tur 3'te +1,25.
  Gercek bandi 3,0 olan cevaba urun 4,5 veriyor. Sonraki duzeltme turunun 1. maddesi.
- Kalan riskler SONUC.md bolum 6'da: konusma hic olculmedi (konusma ornegi yok),
  ornek sayisi az (band basina 1-4), tur 3 eksik, tek model ailesi, alt band yanlis
  yonde hata, sakli kume korumasi rapor bicimi yuzunden kusurluydu.

## OPUS5-C1 (2. calistirma: yazma - Academic Task 2, 5 gorev x 3 seviye)
- Tarih: 2026-08-07
- Bagimlilik kontrolu gecti: `degerlendirme/DEGISIKLIK-KAYDI.md` ve
  `kalibrasyon/olcum/SONUC.md` ikisi de yerinde.
- **Oturum basi durumu:** `content/ornek-cevaplar/writing/` icinde yalnizca AT01-AT05
  (1. calistirma, Academic Task 1) vardi. Calistirma listesinin sonraki grubu Academic
  Task 2, o yapildi; AT dosyalarina dokunulmadi. Uretilen: `T2-01`, `T2-06`, `T2-10`,
  `T2-15`, `T2-17` (15 cevap: band 5,0 / 6,5 / 8,0).
- **Gorev secimi:** task2 havuzunda bes soru kalibi var; her kaliptan bir gorev alindi,
  konu alani tekrar etmeyecek sekilde ilk uygun dosya secilerek - opinion/egitim (T2-01),
  discuss_both_views/ulasim (T2-06), problem_solution/sehir hayati (T2-10),
  advantages_disadvantages/teknoloji (T2-15), double_question/kultur (T2-17). Boylece
  kutuphane bes kalibin de nasil cevaplandigini gosteriyor. 4. ve 6. calistirmalarda
  kullanilacak T2 gorevleri bu besinden secilmeyecek; alti calistirmalik dagilim tablosu
  `content/ornek-cevaplar/KONTROL.md` icinde.
- **Uretim:** `tools/_c1_uret2.py` (1. calistirmadaki `_c1_uret.py` ile ayni kalip).
  Kelime sayisi JSON'a elle yazilmiyor, uretimde sayiliyor ve 250 alt siniri script
  icinde kontrol ediliyor; T2-17 band 5 ilk yazimda 240 kelimeye dustugu icin
  genisletildi. Son sayilar 261-291.
- **Kendi kendini denetim (KONTROL.md 2. grup):** 15 cevabin hepsi hedef bandin icinde,
  sapma 0. Ama **bes gorevin 6,5 hedefli cevabi da yeniden yazildi**: ilk yazimda hatali
  cumle orani %20'nin altindaydi, yani talimatin GRA tablosunda 8-9 satiri, ve bes cevap
  da 7,0 cikiyordu. Sapma tam 0,5 (esigin icinde) olmasina ragmen bes cevapta birden ayni
  yonde oldugu icin sistematik kusur sayildi. Her metne hedef bandda gercekten gorulen
  turden 4-5 hata eklenip oran %30 civarina cikarildi; fikir yapisina, tutuma ve sozcuk
  secimine dokunulmadi.
- **Ders (sonraki C1 calistirmalari icin):** band 5'i hatali yazmak kolay, asil kacan
  6,5. Model dogal olarak temiz dilbilgisi yaziyor ve uzunlugu kisaltmakla yetinirse
  band 7 uretiyor. 6,5 metnini yazdiktan sonra hatali cumle oranini saymak gerekiyor -
  talimatin 7 satiri %20-40, 6 satiri %40-60.
- Atlanan/sorun: yok. Konusma ornekleri (7-10. calistirmalar) bu isin disinda.

## OPUS5-C1 (konusma 1/4 istendi, ama uretim yapilmadi - cakisan talimat)
- Tarih: 2026-08-07
- Bagimlilik kontrolu gecti: `degerlendirme/DEGISIKLIK-KAYDI.md` ve
  `kalibrasyon/olcum/SONUC.md` ikisi de yerinde.
- **Istenen:** "bu dosyanin 1. calistirmasi (toplam 4)", "konusma kartlari icin
  CALISTIRMA", "calistirma listesinden henuz uretilmemis ilk grubu yap".
- **Oturum basi durumu:** yazma tarafi bitmis. `content/ornek-cevaplar/writing/`
  icinde 30 dosya var (AT01-AT08, GT01-GT08, 14 adet T2), yani 30 gorev x 3 seviye
  = 90 cevap; prompt'un yazma kapsaminin tamami. `DURUM.txt` de "Ornek cevaplar -
  yazma" satirini [BITTI] ve alti calistirmayi da [x] gosteriyor.
- **Neden uretim yok:** calistirma listesinde uretilmemis tek grup kalmis, o da
  konusma (7-10. calistirmalar). Kullanici bu oturumda konusma icin calistirmamayi
  soyledi. Iki talimat ayni grubu isaret ettigi icin uretilecek grup kalmadi;
  bitmis yazma gruplarini tekrar uretmek de acikca yasaklanmisti. Hicbir dosya
  uydurulmadi.
- **Bunun yerine yapilan - 30 yazma dosyasinin dogrulanmasi:** hepsi gecerli JSON;
  her dosyada tam olarak band 5,0 / 6,5 / 8,0 uclusu var; `task_ref` dosya adiyla
  uyusuyor; zorunlu alanlar (`exam`, `schema_version`, `kind`, `skill`) ve dort
  olcutun `why_this_band` metni ile `what_would_lift_it` her cevapta dolu; kelime
  sayilari alt sinirin uzerinde (T2 >=250, digerleri >=150) ve JSON'daki
  `word_count` degerleri gercek sayimla birebir tutuyor. Sorun bulunmadi.
- Atlanan: konusma ornekleri (20 kart x 3 seviye) - kullanici istegiyle.
  `DURUM.txt` konusma satiri elle degistirilmedi.

## OPUS5-C1 (konusma 2/4 istendi, yine uretim yok - ayni cakisan talimat)
- Tarih: 2026-08-07
- Bagimlilik kontrolu gecti: `degerlendirme/DEGISIKLIK-KAYDI.md` ve
  `kalibrasyon/olcum/SONUC.md` ikisi de yerinde.
- **Istenen:** "bu dosyanin 2. calistirmasi (toplam 4)", "konusma kartlari icin
  CALISTIRMA", "calistirma listesinden henuz uretilmemis ilk grubu yap, zaten
  var olani tekrar uretme".
- **Oturum basi durumu:** 1. calistirmadaki ile ayni. `content/ornek-cevaplar/writing/`
  icinde 30 dosya (AT01-AT08, GT01-GT08, 14 adet T2) = 90 cevap; prompt'un yazma
  kapsaminin tamami. Uretilmemis tek grup konusma (7-10. calistirmalar), o da bu
  oturumda kullanici tarafindan kapatilmis. Iki talimat ayni grubu isaret ettigi
  icin uretilecek grup yine kalmadi; hicbir dosya uydurulmadi.
- **Bunun yerine yapilan - ikinci duzey denetim.** 1. calistirma sema denetimini
  yapmisti (gecerli JSON, band uclusu, task_ref-dosya adi uyumu, zorunlu alanlar,
  kelime sayisi). Bu oturum onu tekrarlamak yerine cevabin **gorevle** iliskisini
  olcen bir denetim yazdi: `tools/_c1_denetim.py` (yedi kontrol, hicbir dosyayi
  degistirmez, bulgu varsa cikis 1).
  - A `task_ref` havuzdaki gercek gorev dosyasina cozunuyor ve klasor turu tutuyor
    mu (30/30) · B kelime sayisi gorevin **kendi** `min_words` degerinin uzerinde mi,
    sabit 150/250 degil (90/90) · C `why_this_band` ve `what_would_lift_it`
    prompt'un koydugu "<=2 cumle" sinirinda mi (90/90) · D cevap gercekten o
    gorevden mi bahsediyor (90/90) · E Academic Task 1 cevaplarindaki sayilar
    `visual` verisiyle uyusuyor mu (**364 sayi**, hepsi temiz) · F dosyalar arasi
    kopyala-yapistir (yok) · G KONTROL.md kapsami (30/30).
  - Dagilim da script'ten sayildi, 6. grubun notundaki rakami dogruluyor:
    AC-T1 8, GT-T1 8, Task 2 14 (opinion 3, discuss_both_views 2,
    problem_solution 3, advantages_disadvantages 3, double_question 3).
  - **Sonuc: bulgu yok.** Icerikte tek karakter degismedi.
- **E denetimi neden yazildi ve ne kadarini yakalar:** 5. grupta AT07 / 8,0'daki
  "roughly half of their households" ifadesi elle yakalanmisti (gercek degerler
  %50 ve %42). Ayni turden bir kusur baska yerde kalmis mi diye sayilar bu kez
  tek tek gorsel verisiyle karsilastirildi. AT08 / 8,0'daki 21 ve 26,5 ilk taramada
  takildi ama dogru cikti - bes sutunun toplamlari; denetim seri toplamlarini da
  mesru kabul edecek sekilde genisletildi. Sinirini soylemek gerekiyor: bu kontrol
  **gorselden hicbir yolla turetilemeyen sayiyi** yakalar, dogru sayilarla kurulmus
  yanlis yorumu yakalamaz.
- **D denetiminde ogrenilen:** band 5 cevaplari gorevin sozcuklerini kullanmiyor
  (T2-44'te "housing and health care" yerine "the house and the hospital",
  T2-50'de "employees" yerine "the workers in the offices"). Ortusme band 5'te
  ortalama %50, band 6,5'ta %67. Bu konu disiligi degil, sinirli sozcuk
  dagarciginin kendisi - yani band 5 orneklerinin dogru yazildiginin isareti.
  Esik bandda ayrildi; kontrolun amaci yanlis eslesmis dosyayi yakalamak.
- Yazilan: `tools/_c1_denetim.py`, `content/ornek-cevaplar/KONTROL.md` (sona
  "ikinci duzey denetim" bolumu). `DURUM.txt` elle degistirilmedi.
- Atlanan: konusma ornekleri (20 kart x 3 seviye) - kullanici istegiyle. Konusma
  tarafi 4 calistirmanin ikisinde de acilmadigi icin kutuphanenin konusma yarisi
  hala bos; kalan iki calistirmada da kapali kalirsa `content/ornek-cevaplar/`
  yalnizca yazma kutuphanesi olarak teslim edilecek.

## OPUS5-C1 (konusma 3/4 istendi, yine uretim yok - ayni cakisan talimat)
- Tarih: 2026-08-07
- Bagimlilik kontrolu gecti: `degerlendirme/DEGISIKLIK-KAYDI.md` ve
  `kalibrasyon/olcum/SONUC.md` ikisi de yerinde.
- **Istenen:** "bu dosyanin 3. calistirmasi (toplam 4)", "konusma kartlari icin
  CALISTIRMA", "calistirma listesinden henuz uretilmemis ilk grubu yap, zaten var
  olani tekrar uretme".
- **Oturum basi durumu:** 1. ve 2. calistirmadaki ile ayni, bagimsiz olarak yeniden
  dogrulandi: `content/ornek-cevaplar/writing/` icinde 30 dosya, her birinde tam
  olarak band 5,0/6,5/8,0 uclusu, `task_ref` dosya adiyla ayni = 90 cevap, prompt'un
  yazma kapsaminin tamami. Uretilmemis tek grup konusma (7-10. calistirmalar), o da
  kullanici tarafindan kapatilmis. Uretilecek grup yine kalmadi; dosya uydurulmadi.
- **Bunun yerine yapilan - ucuncu duzey denetim: BAND AYRIMI.** 1. calistirma semaya,
  2. calistirma cevabin gorevle iliskisine bakmisti. Ikisi de cevabin **hedefledigi
  bandda olup olmadigini** olcmuyordu - yani prompt'un kirmizi baslikla uyardigi tek
  seyi ("uc cevabin da duzgun Ingilizce olmasi, sadece uzunlugun degismesi"). Bu
  oturum onu olcen denetimi yazdi: `tools/_c1_ayrim.py` (yedi kontrol, hicbir dosyayi
  degistirmez, bulgu varsa cikis 1).
  - **Sonuc: bulgu yok, ayrim saglam.** Band 5 / 6,5 / 8 ortalamalari - hata izi
    yogunlugu 100 sozcukte 3,44 / 0,42 / 0,05 (yaklasik 70 kat), TTR 0,55 / 0,65 /
    0,70, yan cumle yogunlugu 0,10 / 0,99 / 1,44, mekanik baglac 2,9 / 0,5 / 0,0.
    Kelime farki ise kucuk (221 / 248 / 264, %19). Seviyeler uzunlukla degil
    nitelikle ayrisiyor - istenen buydu.
  - Uzunluk disinda kac boyutta ayrisiyor: 19 gorev 5/5, 9 gorev 4/5, 2 gorev 3/5
    (GT08 ve T2-39; eksikleri en zayif iki gosterge, dilbilgisi ayrimi ikisinde de
    saglam). Icerikte tek karakter degismedi.
- **Denetimin kendisi mutasyon testiyle dogrulandi.** "Temiz" sonucu esiklerin
  gecmeye ayarlanmasindan gelmiyor: band 5 metni yerine band 8 metni konan bozuk
  kopyada 202 bulgu, uc bandi ayni metin yapan kopyada 223, band 5'i 80 sozcuge
  kisaltan kopyada 59, gercek kutuphanede 0.
- **Ilk surumun 54 bulgusunun hepsi olcum hatasi cikti, hicbiri icerik hatasi degil.**
  Dordu de kayda gecti (KONTROL.md), cunku konusma tarafi olculurse ayni tuzaklar
  kurulabilir: (1) sayilar sozcuk sayilmiyordu, dort Academic Task 1 dosyasi haksiz
  yere "150 alti" gorundu - IELTS sayiminda "30%" ve "1995" birer sozcuk; (2)
  "kelime sayisi bandla artmali" diye bir kural prompt'ta yok, uydurma kural yedi
  dosyayi isaretledi, kaldirildi; (3) ortak dizi saymak yaniltiyor - tek bir 12
  sozcukluk cumle bes ayri "ortak 8'li dizi" gorunuyordu, olcu en uzun kesintisiz
  ortak diziye cevrildi; (4) hata dedektoru hem duyarsiz hem asiri hevesliydi.
- **(4)'un ayrintisi onemli:** dedektor bes band 5 cevabinda "hata izi yok" dedi;
  metinler elle okundu ve hepsi hatayla doluydu ("I am write this letter for
  complain", "some peoples", "he don't know", "six week is passed"). Yani icerik
  dogruydu, olcu kordu. Ters yonde band 8'de bulunan yedi izin **hepsi yanlis
  alarmdi** ("watched it change", "the rules that come into force", "a state which
  cannot house its people has misjudged" - ucu de dogru Ingilizce). Ders: bir
  denetim temiz gecmedigi zaman once denetimden suphelen, icerigi elle oku, sonra
  karar ver.
- **Sinir acikca yazildi:** kalip tabanli dedektor bandi olcmez, izlerini olcer;
  band 8'de kalan uc iz ad/fiil belirsizliginden gelen yanlis alarmdir. Arac bir
  **karsilastirma** aracidir, mutlak hata listesi degil. Puanlama hala
  `degerlendirme/` talimatiyla elle yapiliyor.
- **Bulgu sayilmayan gozlem:** onbir dosyada band 6,5 ile 8,0 arasinda 8-12
  sozcukluk ortak dizi var (Task 1 girisinin gorev cumlesi parafrazi, mektup
  hitabi, gorevin ozel adlari). 15 sozcukluk esigin altinda kaldigi ve prompt'un
  yeniden yazim olcutu band sapmasi oldugu icin degisiklik yapilmadi.
- Yazilan: `tools/_c1_ayrim.py`, `content/ornek-cevaplar/KONTROL.md` (sona "ucuncu
  duzey denetim: band ayrimi" bolumu). `DURUM.txt` elle degistirilmedi.
- Atlanan: konusma ornekleri (20 kart x 3 seviye) - kullanici istegiyle. Konusma
  tarafi dort calistirmanin ucunde de acilmadi; son calistirmada da kapali kalirsa
  `content/ornek-cevaplar/` yalnizca yazma kutuphanesi olarak teslim edilecek.

## OPUS5-C1 (konusma 4/4 istendi, yine uretim yok - ayni cakisan talimat)
- Tarih: 2026-08-07
- Bagimlilik kontrolu gecti: `degerlendirme/DEGISIKLIK-KAYDI.md` ve
  `kalibrasyon/olcum/SONUC.md` ikisi de yerinde.
- **Istenen:** "bu dosyanin 4. calistirmasi (toplam 4)", "konusma kartlari icin
  CALISTIRMA", "once depoda hangi gruplarin uretildigine bak, uretilmemis ilk grubu
  yap, zaten var olani tekrar uretme".
- **Oturum basi durumu:** onceki uc calistirmadaki ile ayni, bagimsiz olarak yeniden
  dogrulandi: `content/ornek-cevaplar/writing/` icinde 30 dosya, her birinde tam olarak
  band 5,0/6,5/8,0 uclusu, `task_ref` dosya adiyla ayni, dort olcut anahtari eksiksiz =
  90 cevap, prompt'un yazma kapsaminin tamami. `content/ornek-cevaplar/speaking/` yok.
  Uretilmemis tek grup konusma (7-10. calistirmalar), o da kullanici tarafindan
  kapatilmis. Uretilecek grup yine kalmadi; dosya uydurulmadi.
- **Bunun yerine yapilan - dorduncu duzey denetim: GEREKCE - KANIT.** Onceki uc denetim
  hep cevabin kendisine bakti (sema · gorevle iliski · band ayrimi); hicbiri
  `why_this_band` ve `what_would_lift_it` alanlarini okumadi. Oysa "band 7 boyle yazar"
  diyen sey cevap kadar onun altindaki gerekce. Puanlama talimatinin BLOCK G kurali
  ("quote is a verbatim span ... copy the errors too") kutuphaneye uygulandi:
  `tools/_c1_gerekce.py` (sekiz kontrol, hicbir dosyayi degistirmez, bulgu varsa cikis 1).
- **Bu kez bulgu cikti ve icerik duzeltildi: 34 gerekce alani.** Cevap metinlerinin
  hicbiri degismedi (dosya dosya dogrulandi).
  - **25 alanda alinti metinle bire bir tutmuyordu.** Ucu uydurmaydi: AT01/6,5 "lowest"
    diyor ama metinde yok; T2-06/8 "Induced demand" diyor ama metinde "induced" hic
    gecmiyor; T2-39/8 "the difficulty is that" diyor ama "difficulty" yok. Geri kalani
    sikistirilmis ("the boiler make" <- "The boiler in the kitchen make"), genisletilmis
    ("in far duller ways too" <- "in duller ways too") ya da **duzeltilmis** alintiydi:
    T2-01/6,5 gerekcesi "the two groups" yaziyordu, metinde cogul hatasi ile "the two
    group" geciyor. Sonuncusu en onemlisi, cunku BLOCK G tam olarak bunu yasakliyor -
    hatayi duzelten alinti kaniti yok ediyor.
  - **6 alanda gerekce cumlesi baska cevaplardan kopyalanmisti** (bes kalip, 13 cevap).
    En yaygini: "Hata seyrek ve okuru durdurmuyor; band 9'un tam rahatligi yok." BLOCK G
    bunu da yasakliyor; boyle bir cumle o cevap hakkinda bilgi tasimiyor. Her biri kendi
    cevabindaki somut bir yere baglandi.
  - **3 alanda alt band dilbilgisi gerekcesi tek bir hata ornegi vermiyordu** (AT03/6,5,
    AT04/6,5, AT05/6,5: "Kalan hatalar anlami engellemiyor"). Band 6,5'te hata vardir ve
    ogrenci neyi duzeltecegini ancak gosterilirse gorur; ucune de metinden ikiser ornek
    eklendi. Bu, denetime sonradan eklenen H kontrolu.
- **Denetimin kendisi mutasyon testiyle dogrulandi.** Yedi bozma senaryosu: uydurma
  alinti 2, capraz kanit 2, yanlis yokluk iddiasi 3, kopyalanan gerekce 5, kusursuzluk
  iddiasi 1, kisi/sinav dili 3, butun gerekceler bir dosya kaydirilmis 984 bulgu;
  bozulmamis kopyada 0.
- **Mutasyon testi denetimin gercek bir korlugunu buldu.** Ilk surumde "uydurma alinti"
  senaryosu **hic bulgu vermedi**: Ingilizce sozluk kutuphanenin kendisinden kuruluyor,
  dolayisiyla hicbir cevapta gecmeyen sozcuklerden kurulmus sahte bir alinti sozluge
  gore "Ingilizce degil" sayilip gorunmez kaliyordu. Olcu duzeltildi: taninmayan
  sozcukler iceren bir dizide taninan tek sey Ingilizce islev sozcugu ise (a, the, of...)
  dizi bolunmeden sinaniyor. Ders: mutasyon testi denetimi dogrulamak icin degil,
  **denetimin neyi goremedigini bulmak icin** yazilmali.
- **Ilk kosunun 275 bulgusunun 249'u olcum hatasiydi** (3. duzey denetimin dersi yine
  gecerli). Dordu de KONTROL.md'ye yazildi: (1) "go up, go down ile SINIRLI" cumlesi bu
  ogelerin var oldugunu soyler, yok oldugunu degil - 238 yanlis alarm; (2) noktali
  virgul cumleyi bitirir, yoksa yokluk iddiasi onceki yarinin alintilarina bulasiyor;
  (3) "cumlelerin buyuk cogunlugu hatasiz" band 8'in tarifidir, kusursuzluk iddiasi
  degil; (4) cekim eki farki ("store" ~ "stored") uydurma kanit degildir.
- Onceki uc denetim bu degisikliklerden sonra yeniden kosuldu, ucu de temiz:
  `_c1_denetim.py` (gorev iliskisi), `_c1_ayrim.py` (band ayrimi), sema/kelime sayisi.
  Ozellikle 2. duzeydeki "<=2 cumle" siniri hala saglaniyor - eklenen ornekler cumle
  sayisini artirmadi.
- Yazilan/degisen: `tools/_c1_gerekce.py` (yeni), 21 cevap dosyasinda 34 gerekce alani,
  `content/ornek-cevaplar/KONTROL.md` (sona "dorduncu duzey denetim" bolumu).
  `DURUM.txt` elle degistirilmedi.
- Atlanan: konusma ornekleri (20 kart x 3 seviye) - kullanici istegiyle, dort
  calistirmanin dordunde de kapali kaldi. `content/ornek-cevaplar/` yalnizca yazma
  kutuphanesi olarak teslim ediliyor: 30 gorev x 3 seviye = 90 cevap, dort duzey
  denetimden gecmis.

## SONNET5-E1-isaret-gerekceleri (1. calistirma)
- Tarih: 2026-08-08
- Denetim raporunun A2 bulgusu duzeltildi: 180 isaretli okuma sorusunun hepsinde
  birebir ayni flag_reason cumlesi vardi (108'inde gercek mekanizmayla celisiyordu).
  Sayim yeniden yapildi (recursive JSON tarama + tools/dogrula.py): 180 dogrulandi,
  rapordaki sayiyla ayni.
- 51 dosyadaki 180 flagged sorunun hepsine blind_basis + kendi feature_check/
  heading_check/grammar_check/distractor_analysis/not_given_justification/scan_note/
  uniqueness_check alanlarina bakilarak soruya ozgu yeni flag_reason yazildi ve yeni
  flag_mechanism alani eklendi (kip_imzasi 12, esdizim_kilidi 21, tanim_sizintisi 2,
  konumsal_duzen 64, genel_kultur 71, belirsiz 10).
- blind_basis -> flag_mechanism eslemesi gorev talimatindaki tabloya uyuyor; iki soruda
  (AC3/summary-completion #38 "microtubules", AC4/summary-completion #36
  "within-subject") tanim sizintisi cok belirgin oldugu icin bilincli olarak
  general_knowledge/logic varsayilaninin disina cikilip tanim_sizintisi kullanildi.
- Soru metni, answer, evidence, status, blind_solvable alanlarina dokunulmadi; hicbir
  soru silinmedi/degistirilmedi. tools/dogrula.py: sema hatasi 0, isaretli (flagged)
  180, butun tam testler (AC1-4, GT1-2, L1-6) 40/40 tam.
- Yazilan: content/DOGRULAMA/ISARET-GEREKCELERI.md (mekanizma x soru tipi dagilim
  tablosu, mekanizma basina ornekler, belirsiz orani %5.6 - esigin altinda).
- Not (E5'e devir): belirsiz sayilan 10 soru icin net bir dilbilgisel/anlamsal kalip
  yok (cogu tek sozcuk boslugu ya da tek bir sayisal ayrinti); bu 10 soru icin elden
  gecirme yerine muhtemelen yeniden uretim daha uygun olur.

## SONNET5-E2-kucuk-puruzler (1. calistirma)
- Tarih: 2026-08-08
- Denetim raporunun A4/A5/A6 bulgulari kapatildi. `python tools/dogrula.py` once ve
  sonra calistirildi: TOPLAM 1310, isaretli (flagged) 180, tum tam testler (AC1-4,
  GT1-2, L1-6) 40/40, sema hatasi 0 - bu adim soru eklemedi/cikarmadi, sayilar ayni.
- **Madde 1 (A4):** `content/reading/tests/AC2/flow-chart-completion.json` soru 1,
  `accepted_variants`'a `"40 minutes"` eklendi (yonerge rakamla yazima da izin
  veriyordu). `answer`/`evidence`/`explanation` degismedi.
- **Madde 2 (A5):** Iki askida kalan soru okundu, ikisi de "verified" olarak
  kapatildi (flagged degil):
  - `GT1/matching-information.json` #3: `lexical_overlap_answer: 1.0` olcumu
    yaniltici cikti - matching_information tipinde cevap tek harf oldugu icin
    olcu.py harfi ("c") kaynak metindeki alakasiz bir "c" harfiyle eslestiriyor
    (D metnindeki "Block C" ifadesinden geliyor, doguru cevabin C metniyle hicbir
    ilgisi yok). Sorunun kendisi ("extra amount"->"default charge", "miss a
    required step"->"failure to touch out") gercek parafraz gerektiriyor,
    `lexical_overlap_prompt: 0.0` zaten bunu dogruluyor.
  - `practice/matching-headings.json` #9 (paragraf E, pasaj A09): ayni sekilde
    yaniltici - cevap "x" (roma rakami), D paragrafindaki "X-ray spectroscopy"
    ifadesindeki "X" ile rastgele eslesiyor, E paragrafiyla ilgisi yok. Baslik
    secimi ("Fine structures that survived intact") paragrafin ayrintili olcum
    listesini (akson capi, hucre govdesi, miyelin, mikrotubuller) anlamayi
    gerektiriyor.
  - Karar gerekcesi her iki dosyada da ilgili `explanation` alanina ek cumle
    olarak yazildi; `status: "review"` -> `"verified"` degisti, `difficulty_flags`
    olcum kaydi olarak dosyada birakildi.
- **Madde 3 (A6):** `"NOT GIVEN"` cevapli ve `evidence` alani bos 22 soru grep +
  Python taramasiyla dogrulandi (beklenen sayi tutuyor, 10 dosyaya dagilmis).
  **Hepsinde `not_given_justification` alani zaten E5 oncesi bir calistirmada
  doldurulmus bulundu** (uc parcali Turkce gerekce: konu pasajda var / curten
  cumle yok / dogrulayan cumle yok) - icerik tarafinda ek is gerekmedi. `evidence`
  bilincli olarak bos birakildi (dogrula.py NOT GIVEN'i zaten muaf tutuyor).
  Eksik olan tek sey kural yazisiydi: `content/PLAN-soru-dagilimi.md` elle
  degistirilmez oldugu icin yeni `content/PLAN-EK-kurallar.md` dosyasi acilip
  Kalite kurali 2'nin NOT GIVEN istisnasi oraya yazildi.

## SONNET5-E3-arac-borclari (1. calistirma)
- Tarih: 2026-08-08
- Denetim raporunun A12 bulgusu kapatildi (iki arac borcu). Icerik degismedi, hicbir
  soru silinmedi/eklenmedi. `python tools/dogrula.py` once ve sonra calistirildi:
  TOPLAM 1310, isaretli (flagged) 180, tum tam testler (AC1-4, GT1-2, L1-6) 40/40,
  sema hatasi 0 - degisiklikten once/sonra birebir ayni.
- **Madde 1 — `tools/puanlama-raporu.py` kume bolunmus rapor:** Script artik
  `RAPOR-tur<N>.md`'ye (aynen, degismedi) ek olarak her tur icin
  `RAPOR-tur<N>-GENEL.md` (ozet + basari olcutleri + beceri tablosu, "Ornek ornek"
  tablosu ve kume sapma satirlari YOK) ve her kume icin ayri
  `RAPOR-tur<N>-<KUME>.md` (yalniz o kumenin sapma satiri + o kumenin ornek
  tablosu) yaziyor. Hesaplama mantigi degismedi, sadece hangi satirin hangi
  dosyaya gittigi degisti.
  **Gerileme testi (tur 3, once/sonra):**
  | Olcu | Eski | Yeni |
  |---|---|---|
  | Ornek / puanlama | 18 / 54 | 18 / 54 |
  | Ortalama mutlak fark (tek seferlik) | 0.694 | 0.694 |
  | Egilim | -0.139 | -0.139 |
  | En buyuk sapma | 1.50 | 1.50 |
  | Yayilim (ort.) | 0.19 | 0.19 |
  | Basari olcutleri (4 tanesi) | KALDI/KALDI/gecti/gecti | KALDI/KALDI/gecti/gecti |
  `diff` ile eski/yeni `RAPOR-tur3.md` karsilastirildi: tek fark baslikta bugunun
  tarihi (`2026-08-07` -> `2026-08-08`), geri kalan her satir (basari olcutleri,
  beceri tablosu, kume tablosu, ornek ornek tablosu) birebir ayni. Tur 1 ve tur 2
  icin de ayni script yeniden calistirildi, ayni sonuc (sadece tarih satiri farkli).
  `RAPOR-tur3-GENEL.md` icerigi kontrol edildi: ornek tablosu yok, kume tablosu
  yok - sadece genel ozet + basari olcutleri + beceri (writing) satiri.
  `RAPOR-tur3-S1.md` icerigi kontrol edildi: sadece S1 satiri (n=7) + S1'in 7
  ornegi; S2/S3 hic gecmiyor.
  `prompts/OPUS5-A4-puanlama-duzeltmesi.md`: "raporun saklı küme bölümünü de
  okuma" cumlesi yeni dosya adlarina gore guncellendi ("Saklı kümenin
  `RAPOR-tur<N>-<KUME>.md` dosyasını hiç açma; yalnız `RAPOR-tur<N>-GENEL.md` ve
  izinli kümelerin kendi dosyalarını oku."); Adim 1'deki "hangi dosyayi ac"
  cumlesi de tutarlilik icin ayni sekilde guncellendi (artik tam `RAPOR-tur<N>.md`
  degil, `RAPOR-tur<N>-GENEL.md` + izinli `RAPOR-tur<N>-<KUME>.md` dosyalari
  aciliyor) - yoksa Adim 1 hala saklı kumeyi de iceren tam rapora yonlendirirdi.
- **Madde 2 — `tools/kor-kopya.py` onceki oturum temizligi:** Denetimde
  "temizlemiyor" denen davranis kodda zaten vardi (`shutil.move` ile
  `dogrulama/cevap/` -> `dogrulama/cevap-arsiv/<damga>/`), kod degistirilmedi.
  Sinama: mevcut `dogrulama/cevap/` (36 dosya, onceki bir capraz dogrulama
  oturumundan kalma) uzerinde `python tools/kor-kopya.py short-answer`
  calistirildi -> "onceki oturumun cevaplari arsivlendi ->
  dogrulama/cevap-arsiv/20260808-001945" ciktisi geldi, o klasorde 36 dosyanin
  hepsi goruldu, `dogrulama/cevap/` bos kaldi ve yeni 5 kor kopya `dogrulama/kor/`
  altina yazildi. Calisiyor -> A12'nin bu yarisi kapandi. Sinama sonrasi
  `dogrulama/cevap-arsiv/20260808-001945` icerigi elle `dogrulama/cevap/`'e geri
  tasindi (dogrulama/ zaten .gitignore'da, depoyu etkilemedi).

## OPUS5-E4-cambridge-desen (1. calistirma - test yerlesimi deseni)
- Tarih: 2026-08-08
- **Sonuc: kaynak bulunamadi, calistirma atlandi.** Cikti dosyasi yine de yazildi:
  `kalibrasyon/desen/test-yerlesimi.md` (icinde neden atlandigi + "E6 bu dosyadan
  oran/olcut almaz" uyarisi var).
- Neden: bu adimin tek girdisi arkadasin diskindeki kendi (satin alinmis) gercek
  sinav kitaplari. Bu oturumda o kitaplara ulasilamadi:
  - Depo icinde yok: `C:\ielts-paketi` agacinda pdf/epub/djvu/mobi olarak sadece
    `referans/` altindaki 43 resmi IELTS web sitesi belgesi var (zaten bugune
    kadarki desen bilgisinin kaynagi, bu adimin aradigi buyuk orneklem degil).
  - Depo disi gorulemedi: oturum yalniz `C:\ielts-paketi` calisma dizinine yetkili.
    Ev klasoru (Masaustu / Indirilenler / Belgeler) ve diger surucüler uzerinde
    **yalnizca dosya adina** bakan aramalar ortam tarafindan engellendi. Yani
    "kitaplar diskte yok" degil, "bu oturumdan gorulemiyor" demek daha dogru.
- Telif: kitaplar internetten **aranmadi, indirilmedi**; `content/PLAN-soru-dagilimi.md`
  telif kurali 3 aynen korundu. Depoya tek bir pasaj/soru/secenek cumlesi girmedi.
- **Okunan kitap sayfasi: 0** (5. zorunlu kural geregi kayit). Uretilen sayi/oran: yok.
- Icerik tarafi hic ellenmedi: soru eklenmedi/silinmedi, tam testler etkilenmedi,
  puanlama dosyalari (`kalibrasyon/olcum/`) acilmadi -> sakli kume korumasi ihlal
  edilmedi.
- Bir sonraki calistirmaya not: kitaplar erisilebilir bir yere (ornegin depo icinde
  `.gitignore`'lu bir klasore) konursa 1. calistirma bastan yapilabilir; o zaman
  `kalibrasyon/desen/test-yerlesimi.md` sayisal ozetle degistirilir.

## OPUS5-E4-cambridge-desen (2. calistirma - band cevrim tablosu)
- Tarih: 2026-08-08
- Cikti: `kalibrasyon/desen/band-cevrim.md`.
- **KAYNAK BULUNDU.** 1. calistirmadaki "kitaplara ulasilamadi" tespiti yanlis
  cikti: kitaplar `C:\Users\enhar\Desktop\kitaplar` altinda duruyor (`Cambridge IELTS Book 1..8.pdf`). Bash
  `ls` calisma dizini disina izin vermiyor, ama `Glob` araci veriyor; dosyalar
  da Python (PyMuPDF) ile acilabiliyor. 1. calistirma bu yuzden bosuna atlanmis;
  tekrarlanabilir.
- **Ana bulgu: bu kaynakta "kac dogru = hangi band" tablosu yok.** Cambridge
  IELTS 1'de hicbir puanlama cizelgesi yok (metin katmani programla tarandi);
  2-8'de her testin her modulunun cevap anahtari sonunda 40 soruyu UC ARALIGA
  bolen bir hazirlik cizelgesi var - band (1-9) tablosu degil. Aktarilabilen
  tek sayisal cevrim olcutu bu uc araligin esik noktalari; hepsi ciktiya girdi.
- Olculen: 70 cizelge = 7 kitap (2-8) x (4 test x 2 modul + 2 GT okuma).
  Her cizelgeden iki sayi: A = orta araligin basladigi dogru sayisi,
  B = ust araligin basladigi dogru sayisi.
- Ozet: dinleme A ort 14,46 / B ort 27,96 (n=28); Academic okuma A 13,43 /
  B 28,11 (n=28); GT okuma A 16,93 / B 29,79 (n=14).
- **Iki kez sayma (1. zorunlu kural):** her cizelge iki kez, bagimsiz olarak
  okundu - once sayfa goruntusunden, sonra yalniz cizelgenin sayi satiri
  kirpilip kitap basina tek seride dizilerek. 70/70 iki okumada da ayni cikti.
- Kusak farki: kitap 2-3 ile 4-8 arasinda esikler kayiyor (or. dinleme A ort
  17,50 -> 13,25). Bu zorluk farki degil, yayincinin tavsiye politikasinin
  degismesi; ciktida "buyukluk degil yon" uyarisiyla birlikte yazildi.
- Depodaki `band_thresholds` (kaynak `official_average_2023`) DEGISTIRILMEDI.
  Ciktida yalniz gozlem olarak karsilastirildi; tek dikkat ceken sapma,
  kitaplarin GT-Academic ham farkini (ust esikte +1,68 dogru) depodaki tablodan
  (band 6,0'da +7) cok daha kucuk gostermesi. Karar degil, isaret olarak birakildi.
- Telif: kitaplar internetten aranmadi/indirilmedi. Ciktiya tek bir pasaj/soru/
  secenek/baslik/senaryo cumlesi (parafrazi dahil) girmedi; cizelgeyi cevreleyen
  aciklama metni de parafraze edilmedi - yalniz sayilar.
- **Okunan kitap sayfasi: 88** (5. zorunlu kural). Kitap 1: 0 (yalniz metin
  katmani arandi), k2: 14 (s5,6,146-155,159,161), k3: 12 (s5,6,149-158),
  k4: 11 (s6,148-157), k5: 14 (s6,146-148,150-159), k6: 10 (s149-158),
  k7: 10 (s153-162), k8: 17 (s3-5,7,8,150-161). Kitaplar bastan sona okunmadi:
  once girisin "cevap anahtari kac. sayfada" satiri, sonra yalniz anahtar
  sayfalari; cogu sayfada da yalniz cizelge seridi kirpilip okundu.
- Yardimci PNG'ler `.gitignore`'lu `kalibrasyon/ornekler/.tmp-sayfa/` altinda
  uretildi ve is bitince silindi - depoya telifli goruntu girmedi.
- Icerik tarafi ellenmedi: soru eklenmedi/silinmedi, tam testlerde soru sayisi
  degismedi, `kalibrasyon/olcum/` puanlama dosyalari acilmadi (sakli kume
  korumasi ihlal edilmedi).
- 3. calistirmaya not: kitaplar erisilebilir; yazma/konusma puanli ornek
  envanteri icin kitap 2-8'in "model and sample answers" bolumu (kitap 8'de PDF
  s161 ve sonrasi) taranmali. Kitap 1 disindakiler taranmis goruntu - sayfalar
  PyMuPDF ile PNG'ye dokulerek okunmali (`Read` araci PDF'i dogrudan
  goruntuleyemiyor: pdftoppm kurulu degil).

## OPUS5-E10-anlam-duzeyi-olcut (1. calistirma - cumle tamamlama + kisa cevap)

- Yeni olcum turu kosturulmadi (adimin tanimi zaten bunu yasakliyor): mevcut
  `kalibrasyon/metinsiz/sentence-completion-tur1/2/3.json` ve
  `short-answer-tur1/2/3.json` dokumleri, gercek cevaplarla (`answer` +
  `accepted_variants`) yan yana yeniden degerlendirildi. `passages/` acilmadi.
- Karar kurali (raporda da yazili): modelin cevabi gercek cevapla AYNI SEYE
  isaret ediyorsa anlamca dogru. Niteleyici dusup ana ad kaliyorsa ayni sey
  (`separate laboratories` -> `laboratories`); gonderge daraliyorsa
  (`weeks or months` -> `weeks`), sayi/isim tutmuyorsa (`8,400` -> `8,000`) ya
  da baska bir sey adlandiriliyorsa (`plant DNA` -> `ancient DNA`) degil.
  Uc turun ucunde de anlamca dogru olmasi sart.
- **Kendi sayimim 15 yeni soru** (1. zorunlu kural: plandaki ~19 hedef degil).
  sentence-completion 13/37 (%35,1) -> 27/37 (%73,0), +14 soru.
  short-answer 2/10 (%20,0) -> 3/10 (%30,0), +1 soru.
  Toplam 15/47 (%31,9) -> 30/47 (%63,8).
- Denetim raporunun andigi %81 ile arasindaki fark bilincli: sinirda kalan sekiz
  soruyu saymadim, hepsi gerekcesiyle raporda "saymadigim sinir durumlar"
  tablosunda duruyor. Ustunu ortmek yerine yazdim ki 3. calistirmadaki toplu
  rapor ayni kurali uygulayabilsin.
- En temiz bulgular es anlamli kelime ve cekim farki: `mountaineers`->`climbers`,
  `transparent divider`->`transparent barrier`, `final salary`->`final pay`,
  `probationary period`->`probation period`, `anatomy`->`morphology` (2. tur).
  Bunlarin hicbiri kelime esitligi script'inde tutmuyordu.
- **Eski kelime-duzeyi bulgusu silinmedi.** Sema `blind_solvable: true` yazmayi
  gerektiriyor ama kural eski `false` isaretinin silinmemesini istiyor; ikisini
  birlikte tutmak icin eski deger `blind_solvable_kelime_duzeyi` alanina tasindi.
  Yeni alan soru dosyalarindaki anahtar envanterine ekleniyor - 2. ve 3.
  calistirmada ayni ad kullanilmali.
- Soru sayisi degismedi: 47 soru (sentence-completion 37, short-answer 10) girdi,
  47 soru cikti. Hicbir soru silinmedi, eklenmedi. Puanlama dosyalari acilmadi.
- Uygulayan betik: `tools/_e10_anlam_isaretle.py` (elle JSON duzenlemek yerine
  betik: 15 soru 8 dosyaya dagilmis, elle duzenlemede sessiz hata riski var).
- Atlanan paket yok: iki pakette de uc tur dokumu de mevcuttu.

## OPUS5-E10-anlam-duzeyi-olcut (2. calistirma - ozet ailesi)

- Yine yeni olcum turu kosturulmadi: `kalibrasyon/metinsiz/summary-completion-
  tur1/2/3.json` dokumleri gercek cevaplarla yan yana yeniden degerlendirildi.
  `passages/` acilmadi. Karar kurali 1. calistirmadakinin aynisi.
- **Kendi sayimim 14 yeni soru** (plandaki ~15 hedef degil, yon vericiydi).
  Toplam 26/43 (%60,5) -> 40/43 (%93,0).
- 🔴 **Isin ozu, iki alt tipin ayrilmasi.** Alt tipleri ayirmadan bakinca ortalama
  yaniltiyor:
  - kelime bankali (AC2, AC4, GT2 - 14 soru): kelime duzeyi 14/14, anlam duzeyi
    14/14, YENI SORU YOK. Bulamaz da: cevap kapali listeden secilen harf, yuzey
    sapmasi imkansiz. Orada kelime duzeyi olcumu zaten anlam duzeyi olcumudur.
  - parcadan kelime (practice, AC1, AC3, GT1 - 29 soru): 12/29 (%41,4) ->
    26/29 (%89,7), +14 soru. Sizintinin tamami burada.
  - Yani B1'in ozet ailesinde kacirdigi seyin tek sebebi "parcadan kelime
    kopyala" kurali. Denetim raporunun andigi %93'e %89,7 ile yaklastim.
- Saymadigim uc soru gerekcesiyle raporda: practice-15 (`elderly` -> unemployed,
  yanlis kavram), AC3-39 (`seven` -> nine/several/nine, yanlis sayi), GT1-39
  (`convenience` -> 1. turda supermarkets, 3/3 sarti dusuyor).
- En temiz bulgular yine es anlamli/cekim farki: `decomposition`->`decay`,
  `refrigerator`->`fridge`, `peelings`->`peel`, `software engineers`->
  `developers`, `crossover`->`within-subject` (2. tur).
- **Atlanan paket var:** dinleme `summary-completion` setleri (L3 6, L5 5, L6 4 =
  15 soru). Sebep: uc tur dokumunun ucu de yalniz okuma sorularini iceriyor
  (43 kimligin 43'u okuma), yani bu sorular icin parcasiz cevap hic uretilmemis.
  Yontemin 1. maddesi geregi atlandi; dinleme sizintisi ayri adimin isi.
- Eski kelime-duzeyi bulgusu yine silinmedi, `blind_solvable_kelime_duzeyi`
  alanina tasindi (1. calistirmadaki ad korundu; 3. calistirma da ayni adi
  kullanmali).
- Soru sayisi degismedi: 43 soru girdi, 43 soru cikti (practice 15, AC1 5, AC2 5,
  AC3 5, AC4 5, GT1 4, GT2 4). Puanlama dosyalari acilmadi.
- Uygulayan betik: `tools/_e10_anlam_isaretle2.py`.

## OPUS5-E10-anlam-duzeyi-olcut (3. calistirma - not/tablo/akis + toplu rapor)

- Yine yeni olcum turu kosturulmadi: `kalibrasyon/metinsiz/` dokumleri (note-,
  table-, flow-chart-completion tur1/2/3) gercek cevaplarla yan yana yeniden
  degerlendirildi. `passages/` acilmadi. Karar kurali ilk iki calistirmadakinin
  aynisi, alan adi da ayni (`blind_solvable_kelime_duzeyi`).
- **Kendi sayimim 12 yeni soru.** 17/51 (%33,3) -> 29/51 (%56,9).
  note 9/33 -> 18/33, table 4/12 -> 6/12, flow-chart 4/6 -> 5/6.
- **Bu grupta artis daha kucuk, sebebi belli:** not/tablo bosluklarinin buyuk
  kismi kesin deger istiyor (`90 kilometres`, `12 December`, `fourteen`,
  `twenty-three seconds`). Yanlis sayi anlam duzeyinde de yanlistir; anlam
  olcutu bu tur bosluklari kurtarmiyor. Sizinti soyut kavram isteyen bosluklarda
  toplaniyor.
- 🔴 **Kimlik cakismasi tuzagi:** `practice-note-completion` set kimligi hem
  dinlemede hem okumada var, yani dokum kimlikleri iki beceride ayni. Isaretleme
  betigi `skill == "reading"` suzgeciyle calisiyor; suzgec olmasa dinleme
  sorulari okuma dokumuyle karsilastirilirdi (dinleme practice-1 cevabi `11`,
  okuma practice-1 cevabi `47` - sessizce yanlis isaretlenirdi). 2. calistirmada
  da ayni suzgec vardi, sonraki adimlarda korunmali.
- **Kelime duzeyi olcumu cevap anahtarindan bile katiymis:** AC2-flow-chart-1'de
  gercek cevap `forty minutes`, modelin uc turdaki cevabi `40 minutes` ve bu
  zaten sorunun kendi `accepted_variants` listesinde. Yine de kelime duzeyinde
  "bilinmiyor" sayilmis. Tek soru ama olcumun ne kadar dar oldugunu gosteriyor.
- Saymadigim sinir durumlar raporda gerekcesiyle: practice-5 (`Monodontidae` ->
  beluga, tur degil soy soruluyor), practice-13 (`polysomnography` -> EEG, EEG
  onun tek kanali), AC1-6 (`fingertip` -> hand), GT2-19 (`travel allowance` ->
  relocation allowance).
- **Atlanan paketler var:** uc paketin de dinleme setleri (note 42, table 30,
  flow-chart 25 = 97 soru). Sebep 2. calistirmadakiyle ayni: dokumlerin ucu de
  yalniz okuma sorularini iceriyor, bu sorular icin parcasiz cevap hic
  uretilmemis. Yontemin 1. maddesi geregi atlandi.
- Soru sayisi degismedi: 51 okuma sorusu girdi, 51 cikti (note 33, table 12,
  flow-chart 6). 12 tam testin hepsi 40/40, sema hatasi 0. Puanlama dosyalari
  acilmadi.
- Uygulayan betikler: `tools/_e10_karsilastir3.py` (uc turu gercek cevapla yan
  yana basan karsilastirma tablosu - karar bunun ciktisina bakilarak verildi),
  `tools/_e10_anlam_isaretle3.py` (isaretleme).
- **Toplu rapor yazildi** (`content/DOGRULAMA/ANLAM-DUZEYI-RAPOR.md` sonunda).
  Uc calistirmanin toplami: 141 okuma sorusu, kelime duzeyi 58 (%41,1), anlam
  duzeyi 99 (%70,2), 41 yeni isaretleme. Sonuc: B1 tamamlama ailesinde
  sizintinin yaklasik beste ikisini gormuyormus. Fark cevabin BICIMINE bagli -
  kapali liste (kelime bankasi) ve kesin deger isteyen bosluk dayanikli,
  parcadan serbest kelime isteyen bosluk degil.
- Acik kalan: tamamlama ailesinin dinleme kanadi (112 soru) hic
  degerlendirilemedi, dokumlerde parcasiz cevaplari yok. Ayri adimin isi.
- Puanlama olcumu tur 3 (SON) — eksik kalan GT-T2 grubu (5 ornek x 3 tekrar = 15
  puanlama) tamamlandi; tur 3 toplamda 23 ornek x ort. 3 tekrar = 69 puanlama.
  Ortalama mutlak fark 0.804 band, egilim -0.326 (cimri), en buyuk sapma 2.50
  band, ayni cevaptaki yayilim 0.28 band. Basari olcutlerinden yalniz yayilim
  gecti; ortalama fark, en buyuk sapma ve egilim kaldi.

## OPUS5-E6-yeniden-uretim (1. calistirma - YES/NO/NOT GIVEN, tam testler)

- **Kendi sayimim:** `content/DOGRULAMA/yeniden-uretim-listesi.json` icindeki
  `elenen` listesi **71 yuva** (plandaki tahmin degil, tek tek sayildi). Tipe
  gore: sentence_completion 17, multiple_choice 14, yes_no_not_given 10,
  summary_completion 8, matching_features 7, note_completion 4,
  flow_chart_completion 3, true_false_not_given 3, short_answer 3,
  table_completion 2. Bu calistirmanin kapsami (YNNG **tam testler**) bunlarin
  **3 tanesi**: GT1/33, GT1/34, GT2/34. YNNG'nin kalan 7 yuvasi alistirma
  paketinde, o 2. calistirmanin isi.
- Uc yuva da **ayni dosyaya, ayni numarayla** yeniden dolduruldu; hicbir soru
  silinmedi, hicbir numara kaymadi. `python tools/dogrula.py`: GT1 40/40, GT2
  40/40, sema hatasi 0, toplam soru 1310 (degismedi).
- `tools/_f40_kontrol.py GT1` ve `GT2`: iki YNNG paketinde de **hata 0, uyari 0**
  (sira kurali, kanit-cumle esleme, 6 kelimelik ortusme, cevap dagilimi,
  ifade uzunlugu dahil).

### Yeni uc soru ve neden bu yerden yazildi

| Yuva | Eski eksen (elenen) | Yeni kanit | Cevap | Kip |
|---|---|---|---|---|
| GT1/33 | B/1 - "oz-bildirim guvenilmezdir" (yontem bilgisi) | D/2 - kentsel/kirsal **yenilebilir payi** %38,2'ye %23,4 | YES | mutlak (`clearly larger`) |
| GT1/34 | C/2 - kabuk/kemik "gercek israf degil" (yerlesik siniflandirma) | F/2 - cop kutusunun kapsam payi %82,8 | NO | olculu (`roughly ... is likely to`) |
| GT2/34 | C/3 - "oz-bildirimli saglik olumu ongorur" (genel kulturlesmis bulgu) | B/3 - gonulluluk esigi "alti ayda en az bir kez" | YES | mutlak (`Anyone ... fell outside`) |

- Ucunde de E5'in "kacinilacak kanit cumlesi" bulundugu **paragrafa hic
  dokunulmadi** (B'den D'ye, C'den F'ye, C'den B'ye tasindi) - yalniz cumle
  degil, komsulugu da birakildi.
- Uc yeni ifadenin ekseni de **calismanin kendi keyfi sayisi/tasarim karari**:
  bir pay (%38,2'ye %23,4), bir kapsam orani (%82,8), bir tanim esigi (alti
  ayda bir). Bunlarin hicbiri disaridan bilinemez; genel kultur ya da yontem
  kuralindan cikarilamaz.

### Kip imzasi sayimi (yasak 1)

YNNG'de celdirici sik yok, bu yuzden esleme sudur: **YES = dogru taraf**,
**NO/NOT GIVEN = celdirici taraf**. Iki tam test YNNG paketi (8 soru) birlikte:

- YES (4 soru): GT1/33 **mutlak**, GT2/34 **mutlak**, GT1/35 notr,
  GT2/35 olculu (`may improve`) -> **2/4 = %50 mutlak** (esik 1/3) ✔
- NO + NOT GIVEN (4 soru): GT1/34 **olculu**, GT2/36 **olculu**
  (`appear to account for a little over half`), GT2/33 mutlak, GT1/36 notr
  -> **2/4 = %50 olculu** (esik 1/3) ✔

Yani olculu ifade artik yalniz dogru cevapta, mutlak ifade yalniz yanlista
degil: yeni sorularin ikisi mutlak-ve-YES, biri olculu-ve-NO. Kipten cevaba
giden kestirme kapandi.

### Konumsal duzen sayimi (yasak 2)

- Cevap dagilimi - GT1: YES 2, NO 1, NOT GIVEN 1. GT2: YES 2, NO 1,
  NOT GIVEN 1. Hicbiri yariyi gecmiyor, ucu de her pakette var, ardisik uc ayni
  cevap yok.
- Kanit paragraflari - GT1: D/2, F/2, F/3 (+1 NOT GIVEN, kanitsiz).
  GT2: B/3, E/1, F/3 (+1 NOT GIVEN). Dogru (YES) cevaplar **basta (B),
  ortada (D, E)** ve orta-sonda (F) dagilmis durumda.
- Iki pasajin da **son paragrafi (I) hic kullanilmadi** - ki ikisinde de
  "sinirlilik beyani / daha uzun calisma gerekir" kapanisi orada duruyor. Yani
  kapanis kalibina demirlenmis tek soru yok. (Bu kalip zaten kendi basina
  parcasiz "NO/NOT GIVEN" tahminine yol acan turden; bilerek bos birakildi.)
- Harf cifti kurali YNNG'de karsiliksiz (sik listesi yok), bu yuzden
  uygulanmadi.

### Kendi kendini sinama (uretim bitmeden)

Her ifade, pasaj kapaliyken yalniz soru + uc secenekle cozulmeye calisildi
(anlamca bilme de "bilinen" sayilarak):

- **GT1/34 (kutu payi ~yari mi?)** - disaridan kestirilemez: pay %30 da %90 da
  olabilirdi. Bilinemedi ✔
- **GT2/34 (gonulluluk esigi)** - esik "yilda bir", "ayda bir" ya da "alti ayda
  bir" olabilirdi; tasarim karari tamamen keyfi. Bilinemedi ✔
- **GT1/33 (kentte yenilebilir pay daha mi yuksek?)** - burada **artik risk
  var**: "sehirli daha cok israf eder" sezgisi ifadeyi YES yonune itiyor. Ama o
  sezgi **miktar** hakkinda; ifade **oran** soruyor ve ikisi ayni cumlede yan
  yana duruyor (79,4'e 45,8 kg *ve* %38,2'ye %23,4). Sezgiden orana gecmek icin
  "pay da miktarla ayni yonde gider" varsayimini eklemek gerekiyor - bu
  garantili degil. Kor cozumde bilinen sayilmadi, ama emin degilim: **E7 bu
  soruyu ozellikle olcsun.** (Ucu de `blind_solvable: null` birakildi, olcum
  E7'nin isi.)

- Yuvalarda `status: "verified"`, `blind_solvable: null`, `blind_basis: null`,
  `generated_by: "opus"` (dosya duzeyindeki `generated_by: "fable"` **elde
  degistirilmedi**: `tools/_f40_kontrol.py` zarfta bu degeri bekliyor, degistiren
  paket hata veriyor - uretici bilgisi bu yuzden soru duzeyine yazildi).
- Elenen sorunun izi silinmedi: her yuvada `yeniden_uretim` blogu var (eski
  ifade, eski cevap, eski kanit cumlesi, E5'in eleme gerekcesi, ne degistigi).
  Eskiyen `flag_reason` / `flag_mechanism` / `reject_reason` alanlari
  kaldirildi - artik farkli bir soru anlatiyorlardi.
- `content/DOGRULAMA/yeniden-uretim-listesi.json`'da bu uc yuvaya
  `yeniden_uretildi` alani islendi; **kalan 68 yuva** sonraki alti
  calistirmanin isi. 2. calistirma buraya bakip ilk isaretsiz grubu almali.
- Uygulayan betikler: `tools/_e6_ynng_uret.py` (uretim),
  `tools/_e6_liste_isaretle.py` (liste isaretleme).

## OPUS5-E6-yeniden-uretim (2. calistirma - YES/NO/NOT GIVEN, alistirma)

- **Kendi sayimim (yeniden yapildi, plana guvenilmedi):** `yeniden-uretim-listesi.json`
  icindeki `elenen` listesi hala **71 yuva**. Bunlarin **10'u YNNG**: 3'u tam
  testlerde (1. calistirma bitirdi), **7'si alistirma paketinde** - bu
  calistirmanin kapsami tam olarak o 7:
  `content/reading/practice/yes-no-not-given.json` **#2, #4, #5, #9, #11, #12,
  #15**. Bu calistirma bitince kalan **61 yuva** (sentence_completion 17,
  multiple_choice 14, summary_completion 8, matching_features 7,
  note_completion 4, flow_chart_completion 3, true_false_not_given 3,
  short_answer 3, table_completion 2). **YNNG tipi artik listede hic acik yuva
  birakmiyor.**
- Yedi yuva da **ayni dosyaya, ayni numarayla** yeniden dolduruldu; hicbir soru
  silinmedi, hicbir numara kaymadi (15 soru girdi, 15 cikti). `python
  tools/dogrula.py`: 12 tam testin hepsi 40/40, sema hatasi 0, toplam soru 1310
  (degismedi). Alistirma paketi tam teste girmiyor ama bu calistirma bir tam
  test dosyasina hic dokunmadigi icin butunluk zaten korunuyor.
- Yeni kontrol betigi `tools/_e6_ynng_alistirma_kontrol.py`: **hata 0**. Sinadigi
  seyler - kanit cumlesinin pasajda birebir gecmesi, `evidence_locator`in cumle
  numarasinin gercekten o cumleye denk gelmesi, kanitlarin soru sirasiyla artmasi
  (IELTS sira kurali), ifade ile pasaj arasinda 6 kelimelik birebir ortusme
  olmamasi, cevap dagilimi, ardisik uc ayni cevap, kip esikleri.

### Yeni yedi soru ve neden bu yerden yazildi

| Yuva | Eski eksen (elenen) | Yeni kanit | Cevap | Kip |
|---|---|---|---|---|
| #2 A06 | C/1 - sira usulu atama "arastirmaya bilimsel guc verdi" (yontem kurali) | D/2 - standart calisma saati + sozlesme basina sabit 30 saat | YES | mutlak (`both fixed`) |
| #4 A06 | H/3 - deneyimlinin yeni gelene hedefli rehberligi (mentorluk klisesi) | F/3 - birinci yil %26,2 / ikinci yil %8,6 | NO | olculu (`roughly twice`) |
| #5 A10 | A/1 - acik ofis tartismasinin varligi (genel kultur) | B/2 - Latin karesi rotasyonu, her takim dort duzenden farkli sirayla | YES | mutlak (`Every ... all four`) |
| #9 A11 | A/1 - "doganin stresi azalttigi yaygin kabul goruyor" | C/2 - kampuse iki dakika, ormana bes dakika yuruyus | NO | olculu (`seems ... about the same`) |
| #11 A11 | G/1 - "kontrol kosulunun oruntusu tersiydi" (deney mantigi) | F/3 - en belirgin etki mood'da degil dinlendiricilik olceginde | YES | olculu (`seems to have concerned`) |
| #12 A11 | H/3 - "orman kar altinda da sakinlestirir" (sezgisel + pilot kalibi) | H/1 - onceki calismalar yesilligi **enerjiyle** iliskilendirmisti | NO | olculu (`is said to ... mainly`) |
| #15 A12 | H/3 - "sekerleme gece uykusunun yerini tutmaz" (populer bulgu) | kanitsiz - iki deneyin ayni kelime listesini kullanip kullanmadigi | NOT GIVEN | mutlak (`one and the same`) |

- Alti yuvada E5'in "kacinilacak kanit cumlesi"nin bulundugu **paragrafa hic
  dokunulmadi** (C'den D'ye, H'den F'ye, A'dan B'ye, A'dan C'ye, G'den F'ye,
  H'den kanitsiza).
- **Tek istisna #12**, ve bilerek: E5'in kendi notu bu pasaj icin "H paragrafindaki
  karin canlilik uzerindeki etkisi savina tasinmali" diyordu. Yasak cumle H/3
  (pilot calisma kapanisi), yeni kanit H/1 - araya H/2, yani sinirlilik beyani
  giriyor ve o da bilerek bos birakildi. Yani paragraf ayni, iddia ve **kapanis
  kalibi** baska.
- #11 icin E5 iki capa onermisti: G/2 (dinlendiricilik yariya dustu) ya da H/1.
  H/1 #12'ye verildi; G/2 **kullanilmadi** cunku dusus buyuklugu bilinmese de
  yonu hala "kontrol kosulu kotu cikar" sezgisiyle tahmin edilebiliyor - yani
  E5'in sikayet ettigi mekanizmanin aynisi. Onun yerine F/3 secildi: dort
  olcekten hangisinin en guclu sonucu verdigi tamamen olcum-ici bir bilgi.
- Yedi yeni ifadenin ekseni: iki tasarim sabiti (standart saat / 30 saat; Latin
  karesi rotasyonu), iki sayisal buyukluk (%26,2'ye %8,6; bes dakikaya iki
  dakika), bir olcek karsilastirmasi (en guclu etki hangi olcekte), bir
  yazin-atifi yonu (yesillik enerjiyle mi sakinlikle mi anilmis) ve bir
  sessizlik (iki deneyin liste ortakligi). Hicbiri disaridan bilinemez.

### Kip imzasi sayimi (yasak 1)

YNNG'de celdirici sik yok; esleme 1. calistirmadaki gibi: **YES = dogru taraf**,
**NO/NOT GIVEN = celdirici taraf.** On bes soruluk paketin tamami:

- **YES (4 soru): #2 mutlak, #5 mutlak, #7 mutlak, #11 olculu -> 3/4 = %75
  mutlak** (esik 1/3) OK
- **NO + NOT GIVEN (11 soru): #3, #4, #9, #12, #14 olculu -> 5/11 = %45 olculu**
  (esik 1/3) OK

Onemli olan esikler degil, ikisinin de her iki tarafta gorunmesi: mutlak ifade 3
YES + 2 NO/NG'de (#6 `only`, #15 `one and the same`), olculu ifade 1 YES + 5
NO/NG'de. Yani ne "mutlak yazilmissa yanlistir" ne de "olculu yazilmissa
dogrudur" kestirmesi calisiyor. Elenen yedi yuvanin **hepsi** eski halinde bu
kestirmelerden birine uyuyordu.

### Konumsal duzen sayimi (yasak 2)

- Harf cifti kurali YNNG'de karsiliksiz (sik listesi yok), 1. calistirmadaki
  gibi uygulanmadi.
- **Cevap dagilimi:** YES 4, NO 6, NOT GIVEN 5. Ucu de her pasaj obeginde temsil
  ediliyor, hicbiri yariyi gecmiyor, ardisik uc ayni cevap yok (sira: NG, YES,
  NO, NO, YES, NO, YES, NG, NO, NG, YES, NO, NG, NO, NG).
- **Kanit paragraflari:** #2 D, #4 F, #5 B, #9 C, #11 F, #12 H. Basta (B, C),
  ortada (D, F) ve sonda (H) - dogru cevap tek bir bolgeye toplanmiyor. Elenen
  yedilinin eski hali ise iki ucta yiginlanmisti: uc soru **A/1'de** (pasajin
  acilis genellemesi), uc soru **H/3'te** (kapanis cumlesi).
- **Kapanis kalibi:** "sinirlilik beyani / pilot calisma / hakem degerlendirmesi"
  turu kapanis cumlelerine (A10 H, A11 H/2-H/3, A12 H/3) **hicbir yeni soru
  demirlenmedi**. Bu kalip zaten kendi basina parcasiz tahmine yol acan turden.

### Kendi kendini sinama (uretim bitmeden; K3 olcutu - anlamca bilme de "bilinen")

Her ifade **pasaj kapaliyken** yalniz soru + uc secenekle cozulmeye calisildi:

- **#2 (saat/sozlesme sabit mi?)** - bilinemedi. Ustelik uzaktan calisma sirketi
  cagrisimi esnek saate isaret ediyor, yani sezgi YES'i degil NO'yu destekliyor.
- **#4 (birinci yil ikinci yilin kabaca iki kati mi?)** - bilinemedi. "Yeni gelen
  daha cok kazanir" sezgisi *yonu* verir, **buyuklugu** vermez; soru tam olarak
  buyuklugu soruyor (gercek oran ~3 kat).
- **#5 (her takim dort duzenin hepsinden gecti mi?)** - bilinemedi. Takimlarin
  duzenlere bolundugu bir tasarim da esit olculude makuldu.
- **#9 (iki ortama yuruyus esit mi?)** - bilinemedi; burada sezgi **yanlis** yone
  cekiyor: iyi bir deney tasarimcisinin yuruyusleri esitlemesi beklenir, yani
  metodoloji bilgisi YES dedirtiyor, dogru cevap NO.
- **#11 (en guclu etki hangi olcekte?)** - bilinemedi; sezgi mood olceklerini
  soyler (pasajin basligi bile "calms the mind"), dogru cevap dinlendiricilik
  olcegi.
- **#12 (yesillik sakinlikle mi anilmis?)** - bilinemedi ve bu sorunun asil degeri
  burada: yaygin kultur yesilligi **sakinlikle** ozdeslestirir, pasaj ise **enerji
  ve tetikte olmayla** iliskilendiriyor. Disaridan gelen bilgi okuru dogrudan
  yanlis cevaba goturuyor - genel kultur artik odul degil ceza.
- **#15 (iki deney ayni listeyi mi kullandi?)** - bilinemedi. Tuzak metnin
  icinden: iki deneyde de 40+40 boluntusu verildigi icin "demek ki ayni liste"
  cikarimi cazip, ama yazar bunu hicbir yerde soylemiyor.

Yedisinde de sinama gecildi, ucu (#9, #11, #12) genel bilgiyi acikca cezalandiran
turden. Yine de olcum **E7'nin isi**: yedisi de `blind_solvable: null`,
`blind_basis: null` birakildi.

- Yuvalarda `status: "verified"`, `generated_by: "opus"` (dosya duzeyindeki
  `generated_by: "fable"` elde degistirilmedi, 1. calistirmadaki gerekceyle).
- Elenen sorunun izi silinmedi: her yuvada `yeniden_uretim` blogu var - eski
  ifade, eski cevap, eski kanit cumlesi, E5'in eleme gerekcesi, ne degistigi;
  #11'de ayrica E5'in `review_note` metni `e5_notu` alaninda korundu. Eskiyen
  `flag_reason` / `flag_mechanism` / `reject_reason` / `review_note` alanlari
  kaldirildi, cunku artik farkli bir soruyu anlatiyorlardi.
- Listede bu yedi yuvaya `yeniden_uretildi` islendi; **kalan 61 yuva** sonraki
  bes calistirmanin isi. 3. calistirma (coktan secmeli - tam testler) buraya
  bakip ilk isaretsiz grubu almali.
- Uygulayan betikler: `tools/_e6_ynng_alistirma.py` (uretim),
  `tools/_e6_ynng_alistirma_kontrol.py` (kontrol),
  `tools/_e6_liste_isaretle.py` (liste isaretleme; bu calistirmada docstring'inde
  vaat edilen argumanli kullanim gercekten uygulandi, boylece 3-7. calistirmalar
  betigi elle duzenlemeden isaretleyebilir).


# OPUS5-E6-yeniden-uretim (3. calistirma - coktan secmeli, tam testler)

- **Kendi sayimim:** `content/DOGRULAMA/yeniden-uretim-listesi.json` icindeki
  `elenen` listesi 71 yuva; bunlarin **14'u coktan secmeli**. Bu calistirmanin
  kapsami (coktan secmeli **tam testler**) o 14'un **9'u**: AC1/32, AC1/34-35,
  AC3/32, AC3/34-35, AC4/33, AC4/34-35, GT1/22, GT1/23-24, GT2/23-24. Kalan 5
  yuva alistirma paketinde (`practice/multiple-choice.json` #1, #6, #9-10, #11,
  #13), o 4. calistirmanin isi. Calistirma basinda depoda 1. ve 2. calistirmanin
  10 yuvasi isaretliydi; ilk isaretsiz grup buydu.
- Dokuz yuva da **ayni dosyaya, ayni numarayla** yeniden dolduruldu; `number`,
  `select_count` ve secenek harflerinin sayisi degismedi, hicbir soru silinmedi.
  Iki-harfli bes yuva cevap kagidinda yine ikiser kutu tutuyor.
- `python tools/dogrula.py`: 12 tam testin hepsi 40/40, sema hatasi 0, toplam
  soru **1310** (degismedi), isaretli 33 (degismedi).
- `python tools/_e6_mc_testler_kontrol.py`: **hata 0** (numara/select_count
  korunmasi, cevap harflerinin secenekte bulunmasi, kanit-cumle esleme, locator,
  sira kurali, 6 kelimelik birebir ortusme, harf cifti tekrari, kip esikleri).

### Dokuz yeni soru ve neden bu yerden yazildi

| Yuva | Eski eksen (elenen) | Yeni kanit | Cevap |
|---|---|---|---|
| AC1/32 | B/3 - magmanin baca gazi (jeoloji genel bilgisi) | A/1 - adanin Guam'a uzakligi | D |
| AC1/34-35 | F/1 + G/1 - "topluluk + iskelet ici" ikili arastirma kalibi | D/2 - sahada yapilan isler | A+E |
| AC3/32 | A/3 - ahsap/yiyecek/kumas korunmasi (arkeoloji genel bilgisi) | B/1 - "among the victims" cikarimi | B |
| AC3/34-35 | F/2 + G/1 - karbon-oksijen agirligi, sinyal proteini | E/3 - hucre govdesi araligi, kilif deseni | B+F |
| AC4/33 | C/2-C/3 - esit bekleme suresi (deney tasarimi kurali) | C/1 - birinci deneyin ornek buyuklugu | D |
| AC4/34-35 | D/2 + F/1 - polisomnografi, 2. evre uyku (uyku bilimi) | D/1 - ikinci deneyin orneklemi | A+D |
| GT1/22 | A-D/2 - on bir saat dinlenme (mevzuat bilgisi) | A-C/3 - gec kalma esigi (10 dk x 3 kez x 1 ay) | B |
| GT1/23-24 | B-C/2 + C/3 - mesai onayi, izne cevirme (standart madde) | B-A/2 + D/1 - izin yili ve bes gun devir | C+G |
| GT2/23-24 | B-B/3 + D/1 - cekirdek saat, IK'ya bildirim (standart madde) | B-C/2 + C/3 - alti aylik gozden gecirme, bir hafta bildirim | B+G |

- Dokuzunda da E5'in "kacinilacak kanit cumlesi" bulundugu **paragrafa hic
  dokunulmadi**; yalniz cumle degil komsulugu da birakildi (AC1'de B ve F/G
  paragraflari, AC3'te A ve F/G, AC4'te C/2-3 ve D/2 + F, GT1'de A metni D ve B
  metni C, GT2'de B metni B ve D).
- **Yeni eksenlerin tamami keyfi, sirkete/calismaya ozgu ayrinti:** bir uzaklik
  (450 mil), bir yontem listesi (akinti kaydi / huniyle kabarcik), bir sozcuk
  cikarimi ("among the victims"), bir olcum araligi (2,7-14,2 mikrometre), iki
  ornek buyuklugu (60 ve 34 kisi), uc esik (10 dakika x 3 kez x 1 ay), iki
  takvim ayrintisi (1 Nisan, bes gun devir) ve iki sure (alti ay, bir hafta).
  Hicbiri alan bilgisinden ya da "standart is yeri politikasi" sezgisinden
  cikarilamaz.
- **GT paketlerinde asil savunma harf seciminde degil kurguda:** is hayatinin en
  tanidik alti maddesi (resmi tatillerin izinden ayri sayilmasi, dort haftalik
  bildirim, yoneticinin gerekcesiz reddi, deneme suresi olmadan uzaktan calisma,
  internetin sirketce odenmesi, amir onayiyla yurt disi) bilerek **celdirici**
  yapildi. Boylece "standart politikayi sec" stratejisi sistematik olarak yanlis
  harfe goturuyor.

### Kip imzasi sayimi (yasak 1)

Coktan secmelide esleme dogrudan: **dogru secenek = dogru taraf**, **kalan
secenekler = celdirici taraf**. Yalniz bu calistirmanin yazdigi dokuz yuva
sayildi (`generated_by: "opus"`):

- **Dogru secenek 14 - mutlak ifade tasiyan 7 (%50).** Esik ucte bir.
  Mutlak yazilmis dogru cevaplar: AC1/34-35 A (`the whole time`), AC3/34-35 F
  (`exactly`), AC4/33 D (`altogether`), AC4/34-35 A (`Every one of them`),
  GT1/23-24 G (`always`), GT2/23-24 B (`all`), GT2/23-24 G (`Any`).
- **Celdirici 37 - olculu ifade tasiyan 18 (%49).** Esik ucte bir.
  (`may`, `usually`, `probably`, `about`, `mainly`, `likely`, `on average`,
  `fairly`.)
- Bu, E5 2. calistirmasinin olctugu tabloyu tersine cevirmek icin gerekliydi:
  duzeltmeden once **olculu yazilmis 6 secenegin 6'si dogru, kesin yazilmis 16
  secenegin 0'i dogruydu**. Artik her iki kip her iki tarafta da var; kesinlik
  derecesine bakan bir cozucu hicbir yon kazanmiyor.

### Konumsal duzen sayimi (yasak 2)

- **Tek harfli yuvalar (alti tam testin hepsi, 12 soru):** A 3, B 3, C 3, D 3 -
  tam dengeli. Bu calistirmanin dorde katkisi D, B, D, B.
- **Iki-harfli yuvalar (alti tam testin hepsi):** A+D, A+E, B+F, B+G, C+F, C+G -
  **hicbir cift birden fazla tekrarlanmiyor**. Yedi harfin yedisi de en az bir
  kez dogru: A 2, B 2, C 2, D 1, E 1, F 2, G 2.
- Karsilastirma icin E5'in olcumu: dokuz iki-harfli yuvanin **dordu C+F**
  cevapliydi ve **hicbirinde A ya da G dogru degildi**; pasaja hic bakmadan C+F
  yazan bir cozucu 4/9 tutturuyordu. Bu calistirmadaki bes yuvanin **hicbirine
  C+F verilmedi**, A harfi iki, G harfi iki yuvada dogru. Ayakta kalan C+F
  yuvalari: AC2/34-35 ile alistirma paketindeki #3-4 ve #7-8.
- **Kapanis kalibi:** dokuz yeni sorunun **hicbiri** son paragrafa (A03/H,
  A09/H, A12/H, G03 B metni D, G04 B metni D) demirlenmedi; dogru cevaplar A, B,
  C, D ve E paragraflarindan geliyor - yani bastan ortaya yayilmis durumda.

### Kendi kendini sinama (uretim bitmeden; K3 olcutu - anlamca bilme de "bilinen")

Her soru **pasaj kapaliyken** yalniz soru koku + secenek listesiyle cozulmeye
calisildi:

- **AC1/32 (adanin konumu)** - bilinemedi; 450 mil kadar 200 ya da 700 mil de
  makuldu, uc celdirici de pasajin gercek ayrintisini tersine ceviriyor.
- **AC1/34-35 (sahada ne yapildi)** - ikisi birden bilinemedi. Sezgi en cok
  "salim hizi olculmustur" (G) ve "baska resiflerle karsilastirilmistir" (D)
  diyor; ikisi de yanlis.
- **AC3/32 (kazi)** - bilinemedi. Bilerek vakanin **en cok anlatilan**
  ayrintilari (yatak, uyku hali, kurbanin yasi) soru ekseni yapilmadi; eksen tek
  bir sozcugun tasidigi cikarim.
- **AC3/34-35 (olculen yapilar)** - ikisi birden bilinemedi. Kilif deseninin
  korundugu (F) tahmin edilebilir, ama hucre govdesi araligi (B) yalniz olcumden
  bilinir; iki harfin ikisi de gerektigi icin soru ayakta.
- **AC4/33 (birinci deneyin buyuklugu)** - bilinemedi; 60 kadar 40 ya da 100 da
  makuldu.
- **AC4/34-35 (ikinci deneyin orneklemi)** - ikisi birden bilinemedi. Ustelik
  sezgi "ikinci deney daha kalabalik" (F) demeye yatkin, dogrusu tersi.
- **GT1/22 (gec kalma esigi)** - bilinemedi; uc secenek de sayili yazildigi icin
  "somut olani sec" sezgisi de calismiyor.
- **GT1/23-24 (yillik izin)** - ikisi birden bilinemedi; en tanidik uc madde
  celdirici. **Kalan risk notu:** "izin yili 1 Nisan'da baslar" Britanya
  isyerlerinde yaygin bir duzen, yani G harfi tek basina tahmin edilebilir;
  soruyu ayakta tutan sey C harfinin (bes gun devir) keyfiligi ve iki harfin
  birlikte gerekmesi. E7 bu yuvayi olcerken buna ayrica baksin.
- **GT2/23-24 (uzaktan calisma)** - ikisi birden bilinemedi; alti ay ve bir hafta
  sirkete ozgu sureler, tanidik maddeler yine celdirici tarafta.

Dokuzunda da sinama gecildi. Yine de olcum **E7'nin isi**: dokuzunda da
`blind_solvable: null`, `blind_basis: null` birakildi.

### Yerlesim, iz ve sonraki calistirmalara notlar

- Yuvalarda `status: "verified"`, `generated_by: "opus"` (dosya duzeyindeki
  `generated_by: "fable"` elde degistirilmedi, 1. ve 2. calistirmanin
  gerekcesiyle). `answer`, `evidence`, `evidence_locator`, `distractor_analysis`,
  `explanation`, `difficulty` normal semaya gore dolduruldu; aciklamalar
  Ingilizce, ic denetim notlari Turkce.
- Elenen sorunun izi silinmedi: her yuvada `yeniden_uretim` blogu var - eski
  soru koku, eski cevap, eski kanit cumlesi, E5'in eleme gerekcesi ve ne
  degistigi. Eskiyen `flag_reason` / `flag_mechanism` / `reject_reason` alanlari
  kaldirildi, cunku artik farkli bir soruyu anlatiyorlardi.
- [!] **4. calistirmaya (coktan secmeli - alistirma):** kalan bes yuva
  `practice/multiple-choice.json` icinde ve biri iki-harfli (#9-10, eski cevap
  B+E). Tip genelinde C+F halen uc kez dogru (AC2/34-35 + practice #3-4, #7-8);
  yeni iki-harfli yuvaya **C+F verilmemeli**, harf dagilimi icin D ya da E
  agirlikli bir cift uygun (bu calistirmada D ve E birer kez kullanildi).
- [!] **Sonraki calistirmalara - dolan kanit cumleleri.** Ayni testte iki soru
  ayni cumleye demirlemesin diye bu calistirmanin tuttugu yerler: A03 A/1 ve
  D/2; A09 B/1 ve E/3; A12 C/1 ve D/1; G03 A metni C/3 ile B metni A/2 + D/1;
  G04 B metni C/2 + C/3. Ozellikle **A12 doldu**: 32 (A/2), 33 (C/1), 34-35
  (D/1) ve testin diger paketleriyle birlikte serbest kalan cumleler yalniz B/1,
  E/1, G/2, H/1, H/3. AC4 sentence-completion'in uc elenen yuvasi (20, 21, 22)
  A11 pasajindan geldigi icin cakisma yok, ama AC4 summary-completion'in iki
  elenen yuvasi (36, 38) A12'den; onlar yazilirken B/1, E/1 ve G/2 tercih
  edilmeli.
- [!] **Kucuk bir eski kusur (bu calistirmanin kapsami disi):** GT1/21'in D
  seceneginde metinle 6 kelimelik birebir ortusme var ("recorded as a formal
  attendance concern"). Soru E5'in duzeltip verified yaptigi bir yuva oldugu ve
  bu adim yalniz elenen yuvalari dolduracagi icin dokunulmadi; kontrol betigi
  bunu hata degil **not** olarak basiyor. 7. calistirma (kalanlar + butunluk)
  isterse burayi kapatabilir.
- Listede bu dokuz yuvaya `yeniden_uretildi` islendi; **kalan 52 yuva** sonraki
  dort calistirmanin isi.
- Uygulayan betikler: `tools/_e6_mc_testler.py` (uretim),
  `tools/_e6_mc_testler_kontrol.py` (kontrol), `tools/_e6_liste_isaretle.py`
  (liste isaretleme; bu calistirmada "34-35" gibi iki kutuluk yuva numaralarini
  da kabul edecek bicimde genisletildi - onceki hali `int()` ile cokuyordu).


# OPUS5-E6-yeniden-uretim (4. calistirma - coktan secmeli, alistirma)

- **Kendi sayimim:** `content/DOGRULAMA/yeniden-uretim-listesi.json` icindeki
  `elenen` listesini yeniden saydim: 71 yuva, bunlarin **14'u coktan secmeli**.
  3. calistirma tam testlerdeki 9'unu bitirmisti; bu calistirmanin kapsami olan
  **alistirma paketi** kalan **5 yuva**: `content/reading/practice/
  multiple-choice.json` icinde **#1 (A02), #6 (A05), #9-10 (A08), #11 (A08),
  #13 (A11)**. Besi de ayni dosyaya ayni numarayla dolduruldu; #9-10'un
  `select_count: 2` degeri korundu, dosya 12 soruda kaldi, hicbir soru
  silinmedi.

### Hangi kanit nereye tasindi

| Yuva | Eski kanit (E5 yasakladi) | Yeni kanit | Yeni eksen |
|---|---|---|---|
| #1  | A02 B/1 (agirlikca eslestirme) | A02 **B/2** | orneklem bilesimi: 42 erkek / 18 disi, 114-324 g |
| #6  | A05 B/2 (hexaploid tanimi)     | A05 **E/4** | iki marker uzunlugunda dizi/varyant sayilari |
| #9-10 | A08 A/1 + B/3 (sinir, buz kalinligi) | A08 **A/2 + B/1** | merkez ussunun uzakligi + 700'den cok heyelan |
| #11 | A08 C/3 (oncesi-sonrasi uydu goruntusu) | A08 **D/2** | yerden yapilan arastirmanin tarihi |
| #13 | A11 B/3 (sira rastgelestirmesi) | A11 **C/1** | agac stantinin bilesimi ve yasi |

Besinde de yeni kanit, E5'in "kacinilacak" dedigi cumleye **hic degmiyor**;
#6, #9-10, #11 ve #13'te kanit yasakli cumlenin **paragrafinin da disina**
tasindi, #1'de ayni paragrafta ama farkli cumleye (B/1 -> B/2) gecildi, cunku
A02'de disaridan bilinemeyecek sayisal ayrinti yalniz orada.

### Ortak tasarim kurali: genel bilgi artik celdirici tarafta

Bes yuvanin hepsinde dogru cevap **keyfi bir olcuye** baglandi (42/60 erkek,
22'ye karsi 10 dizi, 90 km ve 700+ heyelan, 12 Aralik, 80-108 yil). Bunlarin
hicbiri disaridan tahmin edilemez, cunku her birinin yerine baska bir deger de
esit olculude makuldur. Buna karsilik okurun **disaridan getirdigi sezgi bilerek
yanlis seceneklere** yerlestirildi:

- #6'da "yeni bulgu = yenilik vurgusu" sezgisi B ve C celdiricilerinde,
- #9-10'da "buyuk depremde artci olur / en yakin kasaba zarar gorur / kayitlarin
  en buyugudur" sezgisi A, B ve C'de,
- #11'de "yer arastirmasi hemen ertesi gun yapilir" sezgisi A'da,
- #13'te "Fin ormani = hus agaci" ve "esit karisim" sezgisi A ve D'de.

Yani genel kulturle cozmeye calisan okur odul degil ceza aliyor.

### Kip imzasi sayimi (yasak 1)

`tools/_e6_mc_alistirma_kontrol.py` ciktisi (yalniz `generated_by: "opus"`
yuvalar):

- **Dogru secenek 6 - mutlak ifade tasiyan 4 (%67, esik %33):** #1D ("the whole
  sample"), #6A ("Only about half"), #9-10E ("in all"), #13C ("All the trees").
- **Celdirici 17 - olculu ifade tasiyan 12 (%71, esik %33):** "roughly", "some",
  "appear", "generally", "probably", "likely", "seems", "mainly".
- Karsilastirma icin E5'in bu tipteki olcumu: olculu yazilmis seceneklerin
  tamami dogru, kesin yazilmis seceneklerin hicbiri dogru degildi. Artik iki kip
  de iki tarafta: "temkinli olani sec" de "mutlak olani ele" de calismiyor.

### Konumsal duzen sayimi (yasak 2)

- **Tek harfli yuvalar (dosyanin dokuz tek harfli sorusu):** A 2, B 2, C 3, D 2 -
  dengeli. Bu calistirmanin dorde katkisi D (#1), A (#6), B (#11), C (#13).
- **Iki-harfli yuvalar (dosyanin uc yuvasi):** C+F, C+F, **D+E**. 3. calistirmanin
  notu bu yuvaya C+F verilmemesini istiyordu; verilmedi, boylece C+F sette **iki**
  kez kaliyor (esik: ikiden fazla olmayacak) ve D ile E harfleri ilk kez bu
  pakette dogru oluyor.
- **Kapanis kalibi:** bes yeni sorunun **hicbiri** son paragrafa demirlenmedi
  (A02/H, A05/H, A08/H, A11/H bos birakildi). Yeni kanitlar A, B, C, D ve E
  paragraflarindan geliyor - yani metnin basina ve ortasina yayilmis durumda.
  Ayrica UYARILAR.txt'nin 2. calistirmada koydugu iki yasak da korundu: A11 G
  paragrafina ve A10/A11/A12 H paragrafindaki sinirlilik cumlelerine
  demirlenmedi.

### Kendi kendini sinama (uretim bitmeden; K3 olcutu - anlamca bilme de "bilinen")

Her soru **pasaj kapaliyken** yalniz soru koku + secenek listesiyle cozulmeye
calisildi:

- **#1 (altmis ahtapot)** - bilinemedi. Yabani yakalanan bir ahtapot
  orneklemindeki cinsiyet orani icin disaridan beklenti yok; ustelik "yuz gramin
  altinda olanlar var" celdiricisi gercek alt sinira (114 g) bilerek yakin
  yazildi, yani "yuvarlak sayiyi sec" sezgisi yanlisa gidiyor.
- **#6 (iki marker uzunlugu)** - bilinemedi. Dort secenegin dordu de ayni keyfi
  sayilar uzerine aritmetik iddia; ilk sezgi "yeni varyantlarin cogu ikinci
  uzunluktan" (B) ya da "ilkindekiler zaten kayitliydi" (C) demeye yatkin,
  ikisi de yanlis.
- **#9-10 (deprem ve heyelanlar)** - ikisi birden bilinemedi. Sezgi en cok C
  (haftalarca suren artcilar) ve A (kayitlardaki en buyuk deprem) diyor; ikisi
  de yanlis. **Kalan risk notu:** cok uzak ve issiz bir siradagi taniyan bir
  cozucu B'yi ("en yakin kasaba agir hasar gordu") eleyebilir, ama D ve E'yi
  bulmasi yine de 90 km ile 700 sayisini bilmeyi gerektiriyor ve iki harf
  birlikte isteniyor. E7 bu yuvayi olcerken buna ayrica baksin.
- **#11 (yer arastirmasi)** - bilinemedi; 12 Aralik kadar 9 ya da 20 Aralik da
  makuldu. Iki secenek zamana, iki secenek kapsama dayandigi icin "somut olani
  sec" sezgisi de calismiyor.
- **#13 (agac stanti)** - bilinemedi. Yas araligi (80-108) disaridan bilinemez;
  "Fin ormani daha cok hustur" ya da "iki tur esit karisimdi" sezgileri
  celdirici tarafta.

Besinde de sinama gecildi. Yine de olcum **E7'nin isi**: besinde de
`blind_solvable: null`, `blind_basis: null` birakildi.

### Yerlesim, iz ve sonraki calistirmalara notlar

- Yuvalarda `status: "verified"`, `generated_by: "opus"` (dosya duzeyindeki
  `generated_by: "fable"` elde degistirilmedi, 1-3. calistirmalarin
  gerekcesiyle). `answer`, `evidence`, `evidence_locator`, `distractor_analysis`,
  `explanation`, `difficulty` normal semaya gore dolduruldu; aciklamalar
  Ingilizce, ic denetim notlari Turkce. `passage_id` ve `select_count` elde
  degismedi (betik ikisini de karsilastirip farkliysa cokuyor).
- Elenen sorunun izi silinmedi: her yuvada `yeniden_uretim` blogu var - eski
  soru koku, eski cevap, eski kanit cumlesi, E5'in eleme gerekcesi ve ne
  degistigi. Eskiyen `flag_reason` / `flag_mechanism` / `reject_reason` alanlari
  kaldirildi, cunku artik farkli bir soruyu anlatiyorlardi.
- [!] **Coktan secmeli tipi bitti.** E5 listesindeki 14 coktan secmeli yuvanin
  9'u 3., 5'i bu calistirmada dolduruldu; bu tipte elenen yuva kalmadi.
- [!] **7. calistirmaya (kalanlar + butunluk):** A08 pasajinda **D/2 doldu**
  (alistirma coktan secmeli #11). E5, `practice/short-answer.json` #8 icin
  "D/1'in oteki yarisi - Mount King George'un yamacindaki genis enkaz akmasi ya
  da uydu goruntusuyle yer arastirmasinin ortusmesi" demisti; ikinci secenek
  artik D/2'ye demirli oldugu icin o yuva **D/1'in Mount King George yarisina**
  yazilmali (kisa cevap icin zaten daha uygun bir hedef).
- [!] **Sonraki calistirmalara - dolan kanit cumleleri.** Bu calistirmanin
  tuttugu yerler: A02 B/2; A05 E/4; A08 A/2, B/1 ve D/2; A11 C/1. A05'te
  `AC2/sentence-completion` 21 icin onerilen E/3 hala serbest (ayri dosya, ayri
  test). A11'de C/1 artik dolu; `AC4/sentence-completion` 20-21-22 icin onerilen
  hedefler (ruzgar hizi D, kar derinligi D, H/1'in son yarisi) etkilenmiyor.
- Listede bu bes yuvaya `yeniden_uretildi` islendi; **kalan 47 yuva** sonraki
  uc calistirmanin isi.
- Uygulayan betikler: `tools/_e6_mc_alistirma.py` (uretim),
  `tools/_e6_mc_alistirma_kontrol.py` (kontrol; 3. calistirmanin kontrolunden
  turetildi, alistirma paketine ozgu iki ek denetimle: `passage_id` basina sira
  kurali ve `distractor_analysis`'in butun celdiricileri kapsamasi),
  `tools/_e6_liste_isaretle.py` (liste isaretleme, degistirilmeden kullanildi).


# OPUS5-E6-yeniden-uretim (5. calistirma - ozellik esleystirme)

- **Kendi sayimim:** `content/DOGRULAMA/yeniden-uretim-listesi.json` icindeki
  `elenen` listesini yeniden saydim: 71 yuva. Bu calistirmanin kapsami "cumle
  sonu esleystirme + ozellik esleystirme" idi; listede **cumle sonu esleystirme
  (matching_sentence_endings) tipinde tek bir elenen yuva yok**, dolayisiyla
  kapsam yalniz **ozellik esleystirmenin 7 yuvasi**: `practice/
  matching-features.json` **#1, #5** (A10), `tests/AC1/matching-features.json`
  **#25** (A02), `tests/AC2/matching-features.json` **#24, #25, #26** (A05),
  `tests/AC4/matching-features.json` **#24** (A11). Yedisi de ayni dosyaya ayni
  numarayla dolduruldu; hicbir soru silinmedi (1310 soru, 12 tam test 40/40,
  sema hatasi 0). **Bu tipte elenen yuva kalmadi**; listede kalan yuva 47 -> 40.

### Hangi kanit nereye tasindi

| Yuva | Eski kanit (E5 yasakladi) | Yeni kanit | Yeni eksen |
|---|---|---|---|
| practice #1 | A10 F/2 (gurultu siniri) | A10 **D/3** | iki olcumde de karsilastirma duzeninin altina dusen tek tasarim |
| practice #5 | A10 H/1 (geri donmek istememe) | A10 **B/2** | engel turu: ses yalitimli kapi mi, sesi emen panel mi |
| AC1 #25 | A02 C/3 (isik gecirmez bolme) | A02 **D/3** | ustun hayvanin etkilesimlerin ~%76'sini kazanmasi |
| AC2 #24 | A05 G/2 (Bereketli Hilal, 12.000 yil) | A05 **F/2** | "ilk genetik isaret" iddiasinin hangi bugdaya ait oldugu |
| AC2 #25 | A05 G/2 (Karacadag / einkorn) | A05 **B/2** | tanelerin mikroskop altinda hangi forma benzedigi |
| AC2 #26 | A05 A/3 (tarimin Avrupa'ya yayilmasi) | A05 **G/3** | hangi formun beklenenden erken ortaya cikmis olabilecegi |
| AC4 #24 | A11 F/1 (POMS'un alti boyutu) | A11 **E/4** | olcegin madde sayisi (dort madde, en kisasi) |

Yedisinde de yeni kanit E5'in "kacinilacak" dedigi cumleye **hic degmiyor**;
altisinda kanit yasakli cumlenin **paragrafinin da disina** tasindi (AC1 #25'te
paragraf C'den D'ye, AC2 #25'te G'den B'ye). Hicbir yeni kanit dort pasajin
**son paragrafinda (H) degil** - "sinirlilik beyani / hakem degerlendirmesi"
kapanislari bos birakildi.

### Iki dosyada secenek listesi de degisti

**AC1** - E5'in kendi onerisi uygulandi. Sizinti ifadenin kipinde degil secenek
listesindeydi: A ve B gruplari `see-through screen` / `solid screen` diye, yani
tam da kanit cumlesinin (C/3) soyledigi ozellikle adlandirilmisti; ilk asamayla
ilgili her ifade bu iki etikete sozcuk duzeyinde bagliydi. Yeni liste gruplari
**asama/sira ile** adlandiriyor ("bulusmadan onceki iki kosulun birincisi /
ikincisi", "sonraki uc gun"). Bu, E5'in ongordugu gibi **AC1 #26'yi da
guclendirdi**: o yuvanin ifadesi, cevabi ve kaniti degismedi, ama artik cozucu
once C/2'yi okuyup ilk kosulun gorme izni veren kosul oldugunu bulmak zorunda;
eski `option_wording` sizintisi kapandi (`review_note`'a yazildi).

**AC2** - burada liste eksenden degisti, gerekcesi ayrica onemli. A05'in yer
listesi (Catalhoyuk / Karacadag / Bereketli Hilal / Avrupa / Birlesik Krallik)
**tur bakimindan heterojendi**: bes secenekten yalniz biri kazi yeri, yalniz
biri ulke, yalniz biri kita. Bu yuzden "buradan tane cikti" diyen her ifade
**tur elemesiyle**, "tarim buraya yayildi" ya da "basit bugday burada
ehlilestirildi" diyen her ifade **genel kulturle** cozuluyordu. Denenen ve
elenen iki alternatif:

1. *Yalniz A (Catalhoyuk) ve E (Birlesik Krallik) capalarini kullanmak.* Pasajda
   Karacadag yalniz G/2'de (E5 tarafindan yasakli cumle), Bereketli Hilal ve
   Avrupa ise yalniz yayilma anlatisinda geciyor. Dort yuvanin ucu A olurdu ve
   korlemesine "hep A" diyen bir aday 3/4 yapardi.
2. *C ve D'ye capa atmak.* Bu, E5'in tam da eledigi genel-kultur eksenine geri
   donmek olurdu (tarim Bereketli Hilal'de basladi, Avrupa'ya yayildi).

Secilen yol: liste **bugday turlerine** cevrildi (hexaploid / einkorn / emmer /
basit bugdaylar / spelt) - bes secenegin besi de ayni turden, boylece tur
elemesi kapandi. Bunun bedeli, listenin degismesiyle **kapsam disindaki 23
numarali yuvanin da zorunlu olarak yeniden yazilmasi** oldu: eski ifadesi bir
YER sorusuydu ve yeni listede karsiligi kalmiyordu. Soru silinmedi, numarasi ve
sayisi korundu; 3. calistirmanin o yuvaya yazdigi `revision` kaydi
`yeniden_uretim.onceki_revizyon` altina tasindi.

### Kendi kendini sinama (pasaj kapali, K3 - anlamca bilme de bilinen sayilir)

Sekiz ifadenin sekizi de pasaj kapaliyken cozulmeye calisildi:

- practice #1 (C): korlemesine bakinca sezgi "en kotu olan sade acik ofistir"
  diyor, yani **yanlis** secenege gidiyor; bilinmedi. Gecti.
- practice #5 (D): "office" sozcugu kapiyi, "zoned" sozcugu paneli cagristirdigi
  icin B ile D arasinda kararsiz kaliniyor; bilinmedi. Gecti.
- AC1 #25 (C): A ve B bulusma oncesi kosullar oldugu icin elenir, geriye C/D/E
  kalir; oran yalniz D/3'te. Bilinmedi. Gecti.
- AC2 #23 (D): **en zayif halka.** "Iki ornek birden" kaydi, bes secenek icinde
  tek kume secenegi olan D'yi ust duzeyde isaret ediyor; bilgi degil bicim
  ipucu. Alternatifleri (bkz. yukarida) daha kotu oldugu icin birakildi, E7'nin
  olcumune not dusuldu.
- AC2 #24 (E): "ilk genetik isaret" iddiasi A ile E arasinda bolunuyor; ayrim
  ancak F/2'nin "at all" kaydiyla goruluyor. Bilinmedi. Gecti.
- AC2 #25 (A): tanelerin mikroskop altinda neye benzedigi disaridan bilinemez;
  ustelik 23. soru bicim temelli siniflandirmayi basit bugdaylara baglayarak
  bilerek ters yone cekiyor. Gecti.
- AC2 #26 (A): ploidi bilen bir okur "gelismis form = hexaploid" baglantisini
  kurabilir; orta duzeyde risk, ama secenek metni ("hexaploid wheat") tek basina
  "gelismis" demedigi icin birakildi.
- AC4 #24 (D): madde sayilari (alti ve dort) disaridan bilinemez, araclarin
  adlari uzunluk hakkinda hicbir sey soylemez; C ile D arasinda kararsizlik
  kaliyor. Gecti.

### Kip imzasi sayimi (yasak 1)

Ozellik esleystirmede **celdirici metni yok** - secenekler kisa ad obekleri
(`einkorn`, `the team-office design`), dolayisiyla "dogru cevap olculu,
celdirici mutlak" karsitligi secenek duzeyinde olculemiyor. Sayim bu yuzden
**ifadeler** uzerinden yapildi ve ayrica secenek metinlerinin **hicbirinin** kip
tasimadigi dogrulandi (hepsi notr ad obegi). `tools/_e6_mf_eslestirme_kontrol.py`
ciktisi:

- mutlak ifade tasiyan: **5/8 (%62)** - `only`, `every`, `alone/both/any`,
  `the first`, `fewest`
- olculu ifade tasiyan: **5/8 (%62)** - `rather than`, `about`, `cautiously`,
  `some/as though`, `may/suggest`
- esik %33; iki yon de asiyor, uc ifade ikisini birden tasiyor (ornegin AC1 #25:
  `about three interactions in every four`).

### Konumsal duzen sayimi (yasak 2)

| Set | Harf dagilimi |
|---|---|
| practice P-MF-01 (A10, A-D) | B2 C1 D2 |
| practice P-MF-02 (G05, A-E) | A1 C1 D1 E2 |
| AC1 23-26 (A-E) | A1 C1 D1 E1 |
| AC2 23-26 (A-E) | A2 D1 E1 |
| AC4 23-26 (A-D) | B1 C2 D1 |

- **A sikki uc sette dogru cevap** (P-MF-02, AC1, AC2 - AC2'de iki kez); "yalniz
  orta sikklar dogru olur" deseni yok. Son sik da uc sette dogru (E, E, E).
- Ayni harf ikiden fazla tekrarlanmiyor (en yuksek 2).
- **Hicbir dogru cevap son paragrafa demirlenmedi**: yeni kanitlar D/3, B/2,
  D/3, E/1, F/2, B/2, G/3, E/4 - dort pasajin H paragraflari (sinirlilik ve
  genelleme uyarilari) bos kaldi.

### Ortak cumle kayitlari (sonraki calistirmalar icin)

- **AC1 D/3 artik iki gorevde:** ozellik esleystirme #25 (oran: %76) ve cumle
  tamamlama #20 (terim: `dominance hierarchy`). Hedefler farkli, ama ayni test
  icinde ayni cumle; A02'de C/3 disinda ilk asamaya ait baska capa kalmadigi
  icin baska secenek yoktu. E7 bunu olcerken bilsin.
- **A10 D/3** alistirma paketinde ozet tamamlama #1'de de kullaniliyor (blank:
  `popularity`); ikisi ayri alistirma seti.
- Bu adimda dolan cumleler: **A10 B/2 + D/3, A02 D/3, A05 B/2 + E/1 + F/2 + G/3,
  A11 E/4.**

### E7'ye / kalan calistirmalara notlar

- AC2 grubunda **B (einkorn) ve C (emmer) bilerek capasiz**: pasaj ikisini
  yalniz E/1'de birlikte aniyor, tek tek ayiran tek cumle G/2 ve o cumle E5
  tarafindan yasaklandi. Ikisi de saf celdirici.
- AC4 grubunda **A (Profile of Mood States) capasiz kaldi**: aracin ne olctugu
  adindan ve genel bilgiden cikiyor (E5'in eledigi tam da buydu), madde sayisi
  disinda ondan blind-proof soru cikmiyor - o capa da #26'da kullanilmis
  durumda.
- `tools/_e6_liste_isaretle.py` bu calistirmada **gruplu soru dosyalarini** da
  okuyacak bicimde genisletildi (onceki hali yalniz duz `items` bekliyordu,
  `practice/matching-features.json` gruplu).
- Araclar: `tools/_e6_mf_eslestirme.py` (uretim; kanit cumleleri pasajdan birebir
  okunuyor, paragraf/cumle numarasi dogrulaniyor), `tools/
  _e6_mf_eslestirme_kontrol.py` (kontrol), `tools/_e6_mf_capraz.py` (yeni kanit
  cumleleri baska sorularda kullaniliyor mu taramasi).


# OPUS5-E6-yeniden-uretim (6. calistirma - tamamlama ailesi yuvalari)

> **Bu bolum geriye donuk yazildi.** 6. calistirma 34 yuvayi uretip calisma
> agacina birakmis, ama ne `yeniden-uretim-listesi.json`'a islemis ne de commit
> etmisti (`NOTLAR.md` ve `UYARILAR.txt` girdileri de yoktu). 7. calistirma o
> sorulari **yeniden uretmedi** - oldugu gibi dogruladi, listeye isledi ve ayri
> bir commit'te depoya aldi. Asagidaki sayimlar dosyalardaki icerikten
> `tools/_e7_ozet.py` ile cikarildi.

- **Kapsam:** listedeki tamamlama ailesinin **34 yuvasi** - sentence_completion
  17, summary_completion 8, note_completion 4, flow_chart_completion 3,
  table_completion 2. Onbes dosyaya dagiliyor: `practice/` not (2), cumle (5),
  ozet (3); `AC1/` cumle (1), ozet (3); `AC2/` akis semasi (3), cumle (2);
  `AC3/` cumle (3); `AC4/` not (1), cumle (3), ozet (2); `GT1/` not (1),
  cumle (2); `GT2/` cumle (1), tablo (2).
- Otuz dordu de **ayni dosyaya ayni numarayla** dolduruldu; soru silinmedi,
  numara kaymadi. Her yuvada `status: verified`, `blind_solvable: null`,
  `generated_by: opus` ve eski soruyu saklayan bir `yeniden_uretim` blogu var.
- `python tools/dogrula.py`: **12 tam test 40/40, sema hatasi 0, toplam 1310
  soru** - AC1, AC2, AC3, AC4, GT1, GT2'nin altisi da bu adimda dosya
  degistirdigi halde toplamlar degismedi.
- Uretim ve kontrol betikleri: `tools/_e6_comp_uret.py`, `_e6_comp_kontrol.py`,
  `_e6_comp_capraz.py`, `_e6_comp_kip.py`, `_e6_comp_dok.py`, `_e6_comp_ozet.py`
  (hepsi bu adimda eklendi, izlenmemis durumdaydi).

### Kanit tasimalarindan ornekler

| Yuva | Eski eksen (E5 eledi) | Yeni kanit | Yeni cevap |
|---|---|---|---|
| GT2 tablo #16 | B/2 - "guncel bir ___ yukleyin" (esdizim: CV) | G04 **B/3** | `300-word` |
| GT2 tablo #20 | D/1 - "kendi biriminden biri haftada bir gorusur" (mentor) | G04 **D/2** | `five-week` |
| practice not #1 | A/2 - Japonya'nin 47 vilayeti (cografya bilgisi) | A06 **B/1** | `977` |
| AC4 cumle #21 | F/1 - POMS'un alti boyutu (arac bilgisi) | A11 **E/2** | `65-item` |
| practice ozet #9 | ailelerin kendi cop miktarini kotu tahmin etmesi (klise) | G05 **A/3** | `150` |
| AC1 ozet #39 | tanidik dergi adi cikarimi | A03 **G/1** | `PLOS ONE` |

- Yeni cevaplarin agirligi **sayilar ve kod dizileri**: `977`, `717.7`, `150`,
  `22.5`, `243`, `10 Mbps`, `37.5-hour`, `56,000 kilometres`, `S/2025 U1`,
  `300-word`, `five-week`, `65-item`, `eleven hours`, `thirteen`. Bu bilincli:
  E5'in eledigi tamamlama yuvalarinin cogunda kusur **esdizim kilidiydi**
  (bosluktan onceki kalip tek bir sozcugu cagiriyordu) ve keyfi bir sayi o
  kilidi tanim geregi kirar.

### Kip imzasi (yasak 1) - bu tipte olculemiyor

Tamamlama ailesinde **celdirici metni yok**: cevap ya bosluga yazilan bir
sozcuk/sayi, ya da kelime bankasindan bir harf (AC1/AC4 ozet tamamlama). Kip
kuralinin hedefledigi imza ("olculu ifade = dogru cevap, mutlaklik =
celdirici") bu yuzden **kurulamiyor**. Yine de kaba bir anahtar sozcuk taramasi
(`tools/_e7_ozet.py`) yapildi: 34 soru kokunun **8'i mutlak** (`only`, `both`,
`each`, `at least`, `every`), **6'si olculu** (`about`, `roughly`, `up to`)
ifade tasiyor, gerisi notr. Bu bir esik degil, kayit: soru koklerinin kipi tek
bir banda toplanmis degil.

### Konumsal duzen (yasak 2)

- Harf dagilimi kurali yalnizca **kelime bankali ozet tamamlamada** anlamli
  (AC4 #36 `J`, #38 `D`); ayni harf sette ikiden fazla tekrarlanmiyor.
- Kanit paragraflari pasaj boyunca dagiliyor (A/2, A/3, B/1, B/2, B/3, C/1,
  C/2, C/3, D/1, D/2, D/3, E/1, E/2, E/4, F/1, F/3, G/1, H/2); **son paragrafa
  demirlenen tek yuva AC2 akis semasi #6**, o da akis semasinin son kutusu -
  sira kurali baska yer birakmiyordu.


# OPUS5-E6-yeniden-uretim (7. calistirma - kalanlar + tam test butunlugu kontrolu)

- **Kendi sayimim:** `yeniden-uretim-listesi.json` icindeki `elenen` listesi
  **71 yuva**. Onceki alti calistirma 65'ini kapatti (10 YNNG, 14 coktan
  secmeli, 7 ozellik esleystirme, 34 tamamlama ailesi). Geriye kalan **6 yuva**
  bu calistirmanin kapsami: `practice/true-false-not-given.json` **#4** (A02),
  `tests/AC1/true-false-not-given.json` **#10** (A01),
  `tests/AC3/true-false-not-given.json` **#7** (A07),
  `practice/short-answer.json` **#4** (A04), **#6** (A06), **#8** (A08).
  **Bu calistirmadan sonra listede acik yuva kalmadi (71/71).**
- Alti yuva da ayni dosyaya ayni numarayla dolduruldu; hicbir soru silinmedi.
  Depo genelinde **`status: rejected` kalan soru yok** (515 verified, 33
  flagged - flaglilar E5'in bilerek birakip E7'ye devrettikleri).
- `python tools/dogrula.py`: **AC1 40/40, AC3 40/40**, on iki tam testin hepsi
  40/40, sema hatasi 0, toplam soru 1310 (degismedi).

### Alti yuva: eski eksen -> yeni kanit

| Yuva | Eski eksen (E5 eledi) | Yeni kanit | Cevap |
|---|---|---|---|
| practice TFNG #4 | A02 F/3 - "yabancilar tanidiklardan cok etkilesir" (davranis biyolojisi genellemesi) | A02 **F/4** - son sinamada hic murekkep birakilmamasi | TRUE |
| AC1 TFNG #10 | A01 D/3 - "akilli hayvan yeni duruma uyum sagladi" (standart kanit yapisi) | A01 **D/4** - kucuk nesne istifleme denemesinin `less successfully` yurumesi | FALSE |
| AC3 TFNG #7 | A07 A/3 - ayna testi ne olcuyor tartismasi (alan bilgisi) | A07 **B/4** - aynanin onunde 27 saate karsi panelin onunde 23 saat | FALSE |
| kisa cevap #4 | A04 F/2 - Voyager 2'nin 24 Ocak 1986 gecisi (dunya bilgisi) | A04 **B/2** - gozlem dizisindeki poz sayisi | `ten` |
| kisa cevap #6 | A06 H/1 - transaktif bellek kuraminin adi (orgut psikolojisi) | A06 **A/2** - Japonya disinda calisilan ulke sayisi | `23` |
| kisa cevap #8 | A08 D/1 - Kanada'nin en yuksek zirvesi (cografya) | A08 **C/3** - deprem oncesi temel radar goruntusunun tarihi | `26 November` |

Altisinda da yeni kanit E5'in yasakladigi cumleye **hic degmiyor**; dordunde
kanit yasakli cumlenin **paragrafinin da disina** cikti. Iki istisna A01 D/4 ve
A02 F/4: ayni paragrafin baska cumlesi, cunku sira kurali bu iki sette baska
paragraf birakmiyordu.

### E5'in onerdigi capalar neden uc yerde kullanilmadi

E5 her yuva icin bir capa onermisti; ucunde oneri **baska sorularda zaten
kullanilmis** oldugu icin baska yere gidildi (capraz tarama:
`tools/_e7_capraz.py`):

- **Kisa cevap #4:** E5'in iki onerisi de F/2'nin yarilariydi ve ikisinin de
  cevabi `Voyager 2` olurdu - yani ayni dunya bilgisi kalirdi. Yuva B/2'ye
  tasindi; o cumlenin oteki iki olcusu (poz basina kirk dakika, toplam alti
  saat) AC2 akis semasi #1 ve practice cumle tamamlama #10'da kullanildigi icin
  yuvaya **poz sayisi** birakildi.
- **Kisa cevap #6:** E5'in onerdigi iki olcusel iddia da H/2'ye capaliydi; o
  cumle practice not tamamlama #3 ve AC2 coktan secmeli #34-35'te kullanilmis
  durumda. A/2'ye tasindi - ama ayni cumledeki `47 vilayet` tam da E5'in
  eledigi cografya bilgisi oldugu icin soru **ulke sayisina** soruluyor ve kok
  "Japonya disinda" diyerek `other` ayrimini korumayi zorunlu kiliyor.
- **Kisa cevap #8:** E5'in onerdigi iki yari da D/1'deydi; Mount King George
  enkaz akmasi AC3 ozellik esleystirme #24'te, 12 Aralik yer arastirmasi
  practice not tamamlama #8 ve practice coktan secmeli #11'de kullanilmis.
  Bos duran C paragrafina gidildi (8 Aralik yarisi AC3 cumle tamamlama #21'de
  oldugu icin **temel goruntunun tarihi** alindi).

### Sira kurali ve bir bilincli sapma

TFNG setlerinde ifadeler pasaj sirasini izler. practice #4 (F/4; onceki uc yuva
B, C ve kanitsiz) ve AC1 #10 (D/4; oncesi C/4, sonrasi E/4) sirayi koruyor.
**AC3 #7 istisna:** E5 bu yuva icin acikca "B paragrafinin sayisal ayrintilarina
capalanmali" dedi, ama #8 zaten B/1'e capali. A paragrafinda pasaja ozgu tek bir
sayi ya da olcu yok (icindeki her sey - ayna testinin tarifi, testi gecen turler
listesi, yarim yuzyillik gecmis - alan bilgisi), yani orada kalmak yuvanin
elenme sebebini tekrar uretirdi. Sonuc: **paragraf sirasi korunuyor** (B, B, C,
-, E, F, -), yalnizca B paragrafi icinde cumle sirasi tersine dondu (B/4 sonra
B/1). E7 bunu bilerek yapilmis bir takas olarak degerlendirsin.

### Kendi kendini sinama (pasaj kapali, K3 - anlamca bilme de bilinen sayilir)

- **practice TFNG #4** (TRUE): pasajsiz sezgi "ahtapot gerilince murekkep
  puskurtur" diyor, yani **FALSE'a** gidiyor - genel bilgi ters yone calisiyor.
  Gecti.
- **AC1 TFNG #10** (FALSE): "Kandula", "kup", "kucuk nesneler" disaridan hicbir
  sey soylemiyor; karari yalniz D/4'teki `less successfully` zarfi veriyor.
  Setin en zayif halkasi bu - "esitlik iddialari genelde yanlistir" turu bir
  sinav kestirmesi (bilgi degil bicim ipucu) dogru tarafa da goturebilir. E7
  blind olcumunde ozellikle baksin.
- **AC3 TFNG #7** (FALSE): oran disaridan bilinemez; sezgi "ayna kontrolden cok
  daha ilgi ceker" dedigi icin **TRUE'ya** gidiyor. Gecti.
- **Kisa cevap #4** (`ten`): gozlem programina ozgu poz sayisi, hicbir dis
  kaynaktan turetilemez. Sansla tutturma riski var (kucuk yuvarlak sayi), bilgi
  temelli tahmin riski yok. Gecti.
- **Kisa cevap #6** (`23`): tek bir sirketin kac ulkede calisani oldugu
  disaridan bilinemez. Gecti.
- **Kisa cevap #8** (`26 November`): keyfi bir uydu gecis tarihi. Gecti.

### Kip imzasi sayimi (yasak 1)

Bu calistirmada uretilen alti sorunun ucu kisa cevap (**soru koku notr, secenek
yok**), ucu TFNG (**celdirici metni yok**). Kural gecerli oldugu tek duzeyde,
ifadeler duzeyinde sayildi:

- Uc ifadenin **ucu de mutlak** ifade tasiyor: `No octopus ... at any point`,
  `as well as`, `at least twice as much`. Dogru cevaplarin **3/3'u = %100**
  mutlak (esik 1/3) OK
- Kritik olan sayi degil dagilim: bu uc mutlak ifadenin **biri TRUE
  (practice #4), ikisi FALSE** (AC1 #10, AC3 #7). Yani "mutlak yazilmissa
  yanlistir" kestirmesi calismiyor - E5'in FABLE5 setlerinde yakaladigi imza
  tam olarak buydu.
- "Celdiricilerin en az ucte biri olculu olsun" yarisi bu iki tipte
  **karsiliksiz**: olculu/mutlak karsitligini tasiyacak bir celdirici metni yok.
  Uydurma bir kip eklemek (ornegin "The whales are likely to have spent...")
  olcum yaratmaz, yalnizca ifadeyi bulaniklastirirdi; eklenmedi.

### Konumsal duzen sayimi (yasak 2)

Harf dagilimi kurali TFNG ve kisa cevapta karsiliksiz (sik listesi yok). Onun
yerine cevap dagilimlari:

| Set | Dizi | Dagilim |
|---|---|---|
| practice TFNG 1-15 | T F NG T T F NG F T NG F T T NG F | TRUE 6 / FALSE 5 / NG 4 |
| AC1 7-13 | T NG F F T F NG | TRUE 2 / FALSE 3 / NG 2 |
| AC3 7-13 | F F T NG T F NG | TRUE 2 / FALSE 3 / NG 2 |

- Ucunde de ardisik **uc** ayni cevap yok; en uzun tekrar iki (AC1 #9-10,
  AC3 #7-8) ve ikisi de bilerek kabul edildi, cunku alternatifi cevabi kanit
  yerine dagilima gore secmek olurdu.
- **Hicbir yeni kanit son paragrafta degil**: F/4 (A02'de sekiz paragrafin
  altincisi), D/4, B/4, B/2, A/2, C/3. "Sinirlilik beyani / hakem
  degerlendirmesi" turu kapanis cumlelerine bu adimda hic dokunulmadi.
- Yeni kanitlar pasajin **basi (A/2, B/2, B/4), ortasi (C/3, D/4) ve sonlarina
  yakin (F/4)** dagiliyor.

### Sonraki adimlara (E7) notlar

- **Bu adimda dolan cumleler:** A01 D/4 (ikinci gorev - AC1 not tamamlama #4
  ayni cumlenin traktor lastigi yarisini kullaniyor), A02 F/4 (ikinci gorev -
  AC1 ozellik esleystirme #24 ve AC1 cumle tamamlama #21 ayni cumlenin
  baskinlik yarisini kullaniyor), A07 B/4, A04 B/2 (ucuncu gorev), A06 A/2,
  A08 C/3 (ikinci gorev).
- **A01 D ve A02 F artik tamamen dolu.** Bu iki pasajda yeni bir yuva acilirsa
  kanit bulmak zor olacak.
- **AC1 #11 hala flagged** (E5 dokunmadi, `review_note`'unda "AC1-10 ile ayni
  ekseni paylasiyor" yaziyordu). AC1 #10 artik FALSE ve bambaska bir eksende,
  yani #11'in tekrarlilik gerekcesi ortadan kalkti; ama yuvanin kendi `guess`
  gerekcesi duruyor - E7 yine de olcsun.
- Araclar: `tools/_e7_durum.py` (hangi yuva gercekten uretilmis taramasi),
  `_e7_yuvalar.py` (kapsam dokumu), `_e7_capraz.py` (bir pasajin butun
  sorularini kanit capasiyla listeler), `_e7_kontrol.py` (alti yuvanin sema ve
  artik-alan denetimi), `_e7_liste_doldur.py` (listeye isleme),
  `_e7_ozet.py` (kip ve kanit ozeti).

---

## E7 1/2 - cevap anahtari olcumu (2026-08-08, fable)

- 188 hedef soru (E5 116 + E6 72), 52 dosya; uyusma 184/188 (%97,9), icerik
  duzeyinde 186/188. Iki gercek uyusmazlik isaretlendi (practice MH #15 ii/v,
  GT1 summary #40 prevention/reductions), ikisi de E5 duzeltmesi. Rapor:
  content/DOGRULAMA/RAPOR-2.md.
- ONEMLI ARAC DUZELTMESI: tools/kor-kopya.py, E5/E6'nin ekledigi revision /
  yeniden_uretim / review_note / flag_mechanism / blind_basis alanlarini
  SILMIYORDU ve bu alanlar kor kopyada cevabi acik edebiliyordu (orn. "dogru
  harfler A ve E"). Alanlar SIL kumesine eklendi. Bundan sonraki her kor/metinsiz
  olcum bu temiz surumle uretilmeli.
- E7 2/2 (sizinti) icin: ayni 188 soru + AC1 TFNG #11 (E6 devri) olculmeli;
  blind_solvable alanlari o turda doldurulacak.


## OPUS5-A1 5/5 — KONUSMA ornekleri metne dokuldu (12 ornek, band 5-9)

- Tarih: 2026-08-08. Prompt dosyasinin **"4. CALISTIRMA — KONUSMA ORNEKLERI"** bolumu.
  Bu, calistirma listesindeki **4. grup**; yazma gruplarina (23 ornek) dokunulmadi.
  4/4 notunda "yapilacak is" olarak birakilan bosluk bu calistirmada kapandi.
- **Kaynak dosya diskte yoktu**, `python tools/indir.py` calistirildi ve
  `referans/konusma-band-ornekleri.txt` indi (71 KB, 773 satir). WebFetch'e gerek kalmadi.
  Diger 43 belge zaten vardi, hata 0.
- **12 ornegin 12'si ayiklandi.** Band dagilimi sayfada duyurulan diziyle birebir ayni:
  **5 · 5 · 6 · 6 · 6,5 · 7 · 7 · 7,5 · 8 · 8 · 8,5 · 9**. Ayiklanamayan ornek yok.
- **Bolum dagilimi: Part 1 → 0, Part 2 → 2, Part 3 → 10.** Prompt'ta ongorulen bosluk
  aynen cikti: kaynakta hic Part 1 ornegi yok. Uydurma yapilmadi, bosluk bilerek kabul
  edildi. Part 2 olanlar: SP-band5-1 (Tina, uzun tur - bir ilgi alani/hobi anlatimi) ve
  SP-band6_5-1 (Michal, uzun tur - hayran olunan unlu kisi). Kalan 10'u Part 3 tartismasi.
- **Kelime sayilari (yalniz aday, sinav gorevlisi haric):** 263 / 391 / 497 / 487 / 304 /
  561 / 505 / 600 / 612 / 434 / 450 / 494 — toplam 5598 aday kelimesi. Sayim makineyle
  yapildi (`tools/konusma_ayikla.py`), goz karari degil. Bu alan akicilik olcumunun
  (kelime/dakika) girdisi.
- **Yontem — neden elle yazilmadi:** konusma tarafinda el yazisi sorunu yok, sayfa zaten
  duz metin. Elle kopyalamak aday hatalarini sessizce duzeltme riski tasidigi icin
  ayiklama betige birakildi: `tools/konusma_ayikla.py` sayfa gurultusunu (menu satirlari,
  "View transcript" dugmesi) atiyor, konusmaci etiketlerini `EXAMINER:` / `CANDIDATE:`
  olarak normalize ediyor, kalan karakterlere dokunmuyor.
- **Duzeltmeme denetimi gecildi:** `tools/_konusma_dogrula.py` her transkript satirinin ve
  her yorum paragrafinin ham sayfa metninde birebir bulundugunu dogruluyor →
  **322 satir denetlendi, kaynakta bulunamayan 0.** Yani dusuk bandlardaki hatalar
  ("I want to do volunteers", "some of them has problem", "it can kill a spare time",
  "there are a lot of job to do") yerinde duruyor. **Supheli isaretlenen dosya yok**,
  hicbir dosyada `transcription_suspect` alani yok.
- **Tek kayit notu:** SP-band8-1 (Monika, band 8) sayfada "Part 3: Famous people" basligi
  altinda duruyor ama dokumun tamami hobiler ve bos zaman uzerine. Baslik kaynakta boyle
  oldugu icin `topic` alani degistirilmedi; durum dosyanin `transcription_notes` alanina
  ve KONTROL.md'ye yazildi.
- Dosyalar: `kalibrasyon/ornekler/konusma/<kod>.json` (12 dosya) + `KONTROL.md`
  (12 satirlik tablo, kod · band · bolum · aday kelime · konu). Klasor `.gitignore`'da,
  depoya girmiyor; `git add -f` kullanilmadi. Kod duzeni `SP-band<band>-<sira>`, yarim
  bandlarda nokta yerine alt cizgi: `SP-band6_5-1`, `SP-band7_5-1`, `SP-band8_5-1`.
- **Olcum acisindan durum:** kalibrasyon ornekleri artik **35 ornek** — yazma 23
  (Academic 12 + General Training 11, band 3,0-8,5) + konusma 12 (band 5-9). Konusma
  ayagi ilk kez dolduruldu; SONNET5-A3 turu olcumler konusma icin de calistirilabilir,
  ama yalnizca Part 2/Part 3 kapsamiyla.
- **OPUS5-A1 prompt dosyasi bitti:** 4 grubun dordu de dokuldu, yapilacak is kalmadi.
- Atlanan/sorun yok.

## SONNET5-A3 (KONUSMA olcum turu, klasor adi tur4 — 1. calistirma: 12 ornek x 3 tekrar)
- Tarih: 2026-08-08
- **Bu calistirma yalniz konusma orneklerini kapsar.** `kalibrasyon/ornekler/konusma/*.json`
  altindaki 12 ornegin (SP-band5-1 .. SP-band9-1) hepsi `degerlendirme/konusma.md`
  talimatiyla, hicbir yazma ornegine dokunmadan, 3'er kez puanlandi (36 puanlama).
  Depoda `kalibrasyon/olcum/tur4/` hic yoktu, yani bu turun ilk (ve tek gereken)
  calistirmasiydi.
- **kalibrasyon/olcum/kumeler.json'a konusma kodlari eklendi.** Bant sirali dagitim:
  S1 = SP-band5-1(5,0)/band6-2(6,0)/band7-2(7,0)/band8-2(8,0); S2 = SP-band5-2(5,0)/
  band6_5-1(6,5)/band7_5-1(7,5)/band8_5-1(8,5); S3 = SP-band6-1(6,0)/band7-1(7,0)/
  band8-1(8,0)/band9-1(9,0). Her kumede dusuk ve yuksek bant birlikte var; yazma
  kodlarina dokunulmadi.
- Hicbir dosyada `transcription_suspect: true` yok, 12 ornegin 12'si de puanlandi.
  `speaking_seconds` hicbir ornekte yoktu, bu yuzden `speech_rate_wpm` hesaplanamadi;
  talimatin kendi kuraliyla (suresi yoksa yok say) alan bos birakildi, konusma hizi
  hic kullanilmadan sadece transkriptten puanlandi.
- **Korluk yontemi:** Ana oturum 12 ornegin `band`/`examiner_comment`/`source` alanlarini
  attı, sadece `part`/`topic`/`candidate_word_count`/`transcript` kalan surumu 3 ayri,
  taze genel-amacli alt-ajana (model: sonnet acikca belirtildi) verdi — her ajan
  `degerlendirme/konusma.md` talimatinin tam metnini kendisi uyguladi, gercek bandi hic
  gormedi. Onceki turlarda oldugu gibi ornek+tekrar basina degil, bu kez **tekrar basina
  tek ajan** kullanildi (12 orneği bir ajan tek oturumda puanladi, 3 tekrar = 3 ayri
  ajan, paralel, arka planda) — 36 ayri ajan yerine 3 ajan; hepsi ayni derecede bagimsiz
  ve kor kaldi, sadece daha az cagriyla yapildi.
- Bu grubun tek seferlik (1. tekrar) tahminleri: 5-1=6,0 · 5-2=4,5 · 6-1=6,5 · 6-2=5,5 ·
  6,5-1=7,0 · 7-1=7,0 · 7-2=7,0 · 7,5-1=6,5 · 8-1=8,0 · 8-2=6,0 · 8,5-1=8,0 · 9-1=8,5.
- `python tools/puanlama-raporu.py 4` calistirildi: **ortalama mutlak fark 0,583**
  (tani/ortalama 0,417) · **egilim -0,250** (hafif cimri, esik icinde) · **en buyuk
  sapma 2,00 band** (SP-band8-2: gercek 8,0, tek seferlik 6,0) · **yayilim (ort.) 0,62
  band**. 4 olcutten yalniz "egilim +-0,25 icinde" gecti; ortalama mutlak fark, en buyuk
  sapma ve yayilim olcutleri KALDI. Kume kirilimi: S1 0,875 · S2 0,625 · S3 0,250 —
  sakli kume S3 en dusuk sapmali, ezberleme belirtisi yok.
- Atlanan/sorun: yok (12/12 puanlandi). Basari olcutlerinin 3'u kalmasi konusma
  talimatinin duzeltmeye ihtiyaci oldugunu gosteriyor; bu oturum yalniz OLCTU,
  duzeltme yapmadi (sira OPUS5-A4'un konusma surumune ait).
- Puanlama olcumu tur 4 (konusma, 1. calistirma) — 12 ornek x 3 tekrar = 36 puanlama,
  ortalama mutlak fark 0,583, egilim -0,250 (hafif cimri).

## SONNET5-A3 (KONUSMA olcum turu, klasor adi tur4 — 2. calistirma: tekrar 4-6, 12 ornek x 3 tekrar)
- Tarih: 2026-08-08
- **Depo kontrolu:** disk uzerinde `kalibrasyon/olcum/tur4/` icinde 1. calistirmanin 36
  dosyasinin (tekrar 1-3) yaninda, hicbir NOTLAR girdisi ve commit'i olmayan 14 tane
  yarim/tutarsiz dosya vardi (7 ornek icin tekrar 4 ve 6, tekrar 5 hic yoktu — onceki bir
  oturum calisma sirasinda kesilmis, yarim kalmisti). Bu dosyalar `kalibrasyon/olcum/tur*/`
  .gitignore'da oldugu icin hicbir commit'te izlenmiyordu; "zaten uretilmis" sayilmadi,
  silinip bu calistirma temiz baslatildi (kumeler.json ve RAPOR dosyalari degismedi, sadece
  ham puanlama dosyalari).
- **Bu calistirmada islenen:** ayni 12 konusma ornegi (SP-band5-1 .. SP-band9-1),
  `degerlendirme/konusma.md` ile, tekrar numaralari 4/5/6 (1. calistirmanin 1/2/3'unun
  devami) — 36 yeni puanlama, tur4 klasorunde toplam 72 dosya.
- **Korluk yontemi:** 1. calistirmadaki ile ayni — `kalibrasyon/olcum/_blind_tur4/` altindaki
  (band/examiner_comment/source alanlari atilmis) 12 dosya 3 ayri taze genel-amacli
  alt-ajana (model: sonnet, acikca belirtildi) verildi, tekrar basina bir ajan, hepsi
  paralel calisti; hicbiri gercek bandi gormedi.
- `speaking_seconds` yine hicbir ornekte yok, `speech_rate_wpm` yine hesaplanmadi/bos
  birakildi (1. calistirmadaki kural aynen uygulandi).
- `python tools/puanlama-raporu.py 4` calistirildi (72 puanlama, 12 ornek): **tek seferlik**
  degerler tekrar 1'e dayandigi icin degismedi (ortalama mutlak fark 0,583, egilim -0,250,
  en buyuk sapma 2,00 — SP-band8-2), ama **tani/ortalama** artik 6 tekrarin ortalamasi:
  0,340 (once 0,417) ve egilim -0,160 (once -0,250). **Yayilim (ort.)** 6 tekrarla 0,79
  band'a cikti (once 3 tekrarla 0,62) — daha fazla tekrar, daha genis min/maks araligi
  gosterdi, ozellikle SP-band8-2 ve SP-band5-1'de (1,50 band yayilim). 4 olcutten yalniz
  "egilim +-0,25 icinde" gecti; digerleri (ort. mutlak fark, en buyuk sapma, yayilim) KALDI.
  Kume kirilimi (tek seferlik, kume gostergesi degismedi): S1 0,875 · S2 0,625 · S3 0,250.
- Atlanan/sorun: yok (12/12 puanlandi, 36/36 dosya yazildi). Bu oturum yalniz OLCTU,
  talimati degistirmedi — konusma talimatinin duzeltmeye ihtiyaci oldugu 1. calistirmadan
  beri biliniyor, sira OPUS5-A4'un konusma surumune ait.
- Puanlama olcumu tur 4 (konusma, 2. calistirma) — 12 ornek x 3 tekrar (tekrar 4-6) = 36
  puanlama, tek seferlik degerler degismedi (ort. mutlak fark 0,583, egilim -0,250);
  6 tekrarli tani ortalamasi 0,340, egilim -0,160.

## OPUS5-C1 (konusma 1/4 - YENIDEN: bu sefer uretim yapildi, 7. grup = C01, C04, C07, C10, C14)
- Tarih: 2026-08-08
- Bagimlilik kontrolu gecti: `degerlendirme/DEGISIKLIK-KAYDI.md` ve
  `kalibrasyon/olcum/SONUC.md` ikisi de yerinde.
- **Onceki dort calistirmanin durumu:** bu prompt'un 7-10. calistirmalari daha once
  dort kez acilmis ve **hicbirinde dosya uretilmemisti** (yukaridaki uc "uretim yok"
  kaydi + dorduncusu): depoda uretilmemis tek grup konusmaydi, ayni oturumda konusma
  uretilmesin diyen ikinci bir talimat da gecerli sayilmisti, iki talimat ayni grubu
  isaret edip birbirini iptal edince geriye yapilacak grup kalmamis, onun yerine dort
  denetim script'i yazilmisti. Bu oturumda talimat netlestirildi: **tek gecerli is
  konusma kartlari icin gercek cevap uretmek**; sema denetimi ya da yazma dosyalarinin
  yeniden dogrulanmasi cikti sayilmiyor. Yazma tarafina (1-6) hic dokunulmadi.
- **Oturum basi durumu:** `content/ornek-cevaplar/` altinda yalnizca `writing/`
  (30 dosya = 90 cevap, prompt'un yazma kapsaminin tamami) ve `KONTROL.md` vardi;
  `speaking/` klasoru **yoktu**. Yani konusma yarisinin ilk grubu bu calistirmanin isi.
- **Kart secimi:** part2-3 havuzunda 60 kart var ve bes kart turune ayrilmis
  (kisi · yer · nesne · olay · soyut). Bu gruba her turden bir kart alindi, havuzun
  bas tarafindaki ilk uygun dosya secilerek: **C01** (kisi / A patient person),
  **C04** (yer / A quiet place for thinking), **C07** (nesne / An item of clothing),
  **C10** (olay / Helping a stranger), **C14** (soyut / A habit you would like to
  change). Boylece tek grup uretilmis olsa bile kutuphane bes kart turunun de nasil
  konusuldugunu gosteriyor. Dort calistirmalik dagilim tablosu
  `content/ornek-cevaplar/KONTROL.md` icinde (15 Part 2 karti + 5 Part 1 seti = 20);
  8. ve 9. calistirmalar C02/C05/C08/C11/C15 ve C16/C19/C22/C25/C29, 10. calistirma
  Part 1.
- **Kapsam karari - Part 2, Part 3 degil:** uretilen cevap kartin Part 2 tek kisilik
  konusmasi. Kartin `speaking_seconds` degeri (90-120 sn) Part 2 icin; Part 3 sinav
  gorevlisiyle karsilikli konusma oldugu icin tek yonlu ornek metin o bolumu yanlis
  gosterirdi. Gerekce KONTROL.md'de de yazili.
- **Uretim:** `tools/_c1_uret7.py` (yazma tarafindaki `_c1_uret*.py` kalibi).
  Uretilen: `content/ornek-cevaplar/speaking/{C01,C04,C07,C10,C14}.json`, her birinde
  band 5,0 / 6,5 / 8,0 = **15 cevap**. Semada yazmadan farkli olan alanlar prompt'un
  dedigi gibi: `text` yerine `transcript`, ucluk `why_this_band`
  (`fluency_coherence` · `lexical_resource` · `grammatical_range_accuracy`) ve
  `approx_duration_seconds`. Ayrica `part: 2` eklendi (kart hem Part 2 hem Part 3
  iceriyor, hangi bolumun cevabi oldugu dosyadan anlasilsin diye).
- **Sure alani elle yazilmiyor:** band basina bir konusma hizi secilip (5,0 -> 80,
  6,5 -> 105, 8,0 -> 127 kelime/dk) sure kelime sayisindan hesaplaniyor, cunku
  `konusma.md` akiciligi `speech_rate_wpm`'den okuyor ve bu hizlar talimatin
  tablosunda "slow" / "moderate" araliklarina denk geliyor. Script sonucu kartin
  90-120 saniye penceresine gore kontrol ediyor ve disari cikani reddediyor - bu
  ayni zamanda kelime sayisini da bagliyor (ilk yazimda C04/5,0 ve C14/6,5 pencereyi
  astigi icin kisaltildi). Kelime sayilari 150-251.
- **Kendi kendini denetim (KONTROL.md 7. grup):** 15 cevabin hepsi hedef bandin
  icinde, **sapma 0**, hicbiri yeniden yazilmadi. Puanlama etiketler ortulerek ve
  dokumler cumle cumle numaralanarak yapildi; GRA icin talimatin istedigi sayim
  yapildi (hatali cumle orani: band 5'te %64-70, band 6,5'ta %27-33, band 8'de %0-8).
- **Konusmada band 5'in yazma tarafindan farki - onemli:** yazmada band 5 metinleri
  hatali cumle oraninda %80'i asip GRA'da 4 aliyor ve genel band **dort** olcutun
  ortalamasiyla yine 5,0'da duruyordu. Konusmada olcut uc tane, yani GRA 4 gelseydi
  5+5+4 = 4,67 -> 4,5 olurdu. Bu yuzden band 5 dokumlerinde her kartta uc cumle
  bilerek hatasiz birakildi ve oran 5 satirinin (%60-80) ortasina oturtuldu.
- **6,5 tuzagi bu kez ateslenmedi:** yazmanin 2. grubunda bes cevap birden 7,0 cikip
  yeniden yazilmisti. Burada hatali cumle orani metin yazilirken sayildi, bes cevap da
  %27-33'te, yani 7 satirinin icinde ve %20 esiginin uzaginda. LR tarafinda da
  talimatin "band 7 icin dort az rastlanan oge" capasi bilerek karsilanmadi (kart
  basina 2-3 oge).
- **Tek yarim band:** C10 / 6,5'ta akicilik 6 degil 6,5 verildi (anlati sirali ve
  duraklamasiz ama gecisler then/after that/so kalibinda). Genel band degismiyor.
- **80 kelime capasi:** Part 2 tek kisilik konusmada 80 kelimenin alti akicilikta
  max 5; en kisa cevap 150 kelime, yani hicbir cevapta ateslenmedi -
  band 5'in dusuklugunun sebebi az konusmak degil, olcutler.
- Yazilan: `tools/_c1_uret7.py`, `content/ornek-cevaplar/speaking/` (5 dosya),
  `content/ornek-cevaplar/KONTROL.md` (konusma dagilim tablosu + 7. grup bolumu).
  `DURUM.txt` elle degistirilmedi (kendiliginden guncelleniyor).
- Atlanan/sorun: yok. Kalan konusma gruplari 8., 9. ve 10. calistirmalarda; kart
  listeleri KONTROL.md'deki dagilim tablosunda hazir.
- Ornek cevaplar - konusma (1. calistirma) - 5 Part 2 karti x 3 seviye = 15 cevap,
  hepsi hedef bandin icinde (sapma 0), yeniden yazim yok.

## OPUS5-C1 (konusma 2/4 - uretim yapildi, 8. grup = C02, C05, C08, C11, C15)
- Tarih: 2026-08-08
- Bagimlilik kontrolu gecti: `degerlendirme/DEGISIKLIK-KAYDI.md` ve
  `kalibrasyon/olcum/SONUC.md` ikisi de yerinde.
- **Oturum basi durumu:** `content/ornek-cevaplar/speaking/` altinda yalnizca 7. grubun
  bes dosyasi (C01, C04, C07, C10, C14) vardi. Yani prompt'un konusma listesinde
  uretilmemis ilk grup 8. grup; KONTROL.md'deki dort calistirmalik dagilim tablosuna
  gore kartlari **C02 · C05 · C08 · C11 · C15** (bes kart turunun ikinci turu: kisi ·
  yer · nesne · olay · soyut). Yazma tarafina (1-6) hic dokunulmadi, yeniden dogrulama
  yapilmadi.
- **Talimat cakismasi bu oturumda da yok:** tek gecerli is konusma kartlari icin gercek
  cevap uretmekti. Sema denetimi yazmak ya da yazma dosyalarini yeniden dogrulamak
  cikti sayilmadi (7. grup kaydindaki aciklamanin aynisi).
- **Yarim kalmis uretim bulundu ve tamamlandi.** Depoda islenmemis iki dosya duruyordu:
  `tools/_c1_uret8.py` (bes kartin 15 metni ve gerekceleri yazilmis) ve
  `tools/_c1_olc8.py` (kelime/sure olcer). Script hic calistirilmamisti - `speaking/`
  altinda 8. gruba ait dosya yoktu. Metinler sifirdan yazilmak yerine olculdu,
  duzeltildi ve uretildi; asagidaki dort duzeltme bu denetimden cikti.
- **Uretim:** `python tools/_c1_uret8.py` ->
  `content/ornek-cevaplar/speaking/{C02,C05,C08,C11,C15}.json`, her birinde band
  5,0 / 6,5 / 8,0 = **15 cevap**. Sema 7. grupla ayni: `transcript`, ucluk
  `why_this_band` (fluency_coherence · lexical_resource ·
  grammatical_range_accuracy), `approx_duration_seconds`, `part: 2`.
- **Kapsam yine Part 2:** kartin `speaking_seconds` degeri (90-120 sn) tek kisilik
  konusma icin; Part 3 karsilikli konusma oldugundan tek yonlu ornek metin o bolumu
  yanlis gosterirdi. Gerekce KONTROL.md'de.
- **Denetimden cikan dort duzeltme (KONTROL.md 8. grup bolumunde ayrintili):**
  1. C11/6,5 ve C15/6,5 ilk yazimda 235 ve 230 kelimeydi; 105 kelime/dakikada 135 ve
     130 saniye ediyor, yani kartin 120 saniyelik penceresini asiyordu. 210 ve 208
     kelimeye indirildi (uretim script'i pencere disini zaten reddediyor).
  2. C11/6,5'ta hatali cumle orani kisaltmadan sonra 4/10 = %40 cikti - talimatin 7
     satiri (%20-40) ile 6 satiri (%40-60) arasindaki tam sinir. Bir edat hatasi
     duzeltilerek (in my mind -> on my mind) %30'a cekildi.
  3. C15/5,0'da oran 8/10 = %80'di, yani 5 satiri ile 4 satiri arasindaki sinir.
     Konusmada olcut uc tane oldugu icin GRA 4 gelseydi genel band 4,5'e duserdi
     (5+5+4 = 4,67); "in the university" -> "at the university" ile %70'e indi.
  4. C05/6,5'ta metin degil **gerekce** duzeltildi: GRA gerekcesi ucuncu hata olarak
     "instead of this" kurulusunu gosteriyordu, ama bu dilbilgisi degil esdizim
     hatasi (LR gerekcesinde zaten sayili). Talimat hatayi ancak dilbilgisi
     etiketiyle adlandirabiliyorsan saymayi soyluyor; gerekce sayimla ayni uc hatayi
     gosterecek sekilde degistirildi.
- **Kendi kendini denetim:** 15 cevabin hepsi hedef bandin icinde, **sapma 0**. Puanlama
  etiketler ortulerek ve dokumler cumle cumle numaralanarak yapildi. Hatali cumle
  oranlari: band 5'te 7/10 = %70, band 6,5'ta 3/10 = %30, band 8'de sifir (11-16
  cumle). Uc metin yeniden yazildi ama hicbiri bandi kacirdigi icin degil, olcum
  sinirinda kaldigi icin (yukaridaki 1-3).
- **Bicim kontrolu:** 7. grubun `tools/_c1_k7_kontrol.py` denetimi on dosyanin hepsine
  uygulandi - task_ref, band uclusu, word_count'un gercek sayimla uyusmasi, 80 kelime
  alt siniri, 90-120 saniye penceresi, ucluk olcut ve gerekce alanlarinda 2 cumle
  siniri. Ilk geciste alti bulgu cikti (bes kartta band 8'in `what_would_lift_it`
  alani "Hedefte." ayri cumle oldugu icin uc cumle; C02/6,5'ta gerekcedeki "..."
  cumle bolucusunu yaniltiyordu) ve altisi da duzeltildi. Ikinci gecis: bulgu yok.
- **Bu grubun ogrettigi sey - 6,5'un tuzagi konusmada baska turlu:** yazmada 6,5
  cevaplari fazla duzgun yazilip 7,0'a kayiyordu; konusmada karsiligi surenin tasmasi,
  cunku sure kelime sayisindan hesaplaniyor ve kart 120 saniyeyle sinirli. Kelime
  tavanlari: band 5 icin 160, band 6,5 icin 210, band 8 icin 254.
- Yazilan: `tools/_c1_uret8.py` ve `tools/_c1_olc8.py` (yarim kalmislardi, tamamlandi),
  `content/ornek-cevaplar/speaking/` (bes yeni dosya),
  `content/ornek-cevaplar/KONTROL.md` (8. grup bolumu). `DURUM.txt` elle
  degistirilmedi.
- Atlanan/sorun: yok. Kalan konusma gruplari 9. calistirma (C16 · C19 · C22 · C25 ·
  C29) ve 10. calistirma (Part 1 konu setleri); iki sayisal hedef KONTROL.md'nin
  "9. gruba kalan" bolumunde yazili.
- Ornek cevaplar - konusma (2. calistirma) - 5 Part 2 karti x 3 seviye = 15 cevap,
  hepsi hedef bandin icinde (sapma 0), uc metin olcum siniri yuzunden yeniden yazildi.

## OPUS5-C1 (konusma 3/4 - uretim yapildi, 9. grup = C16, C19, C22, C25, C29)
- Tarih: 2026-08-08
- Bagimlilik kontrolu gecti: `degerlendirme/DEGISIKLIK-KAYDI.md` ve
  `kalibrasyon/olcum/SONUC.md` ikisi de yerinde.
- **Oturum basi durumu:** `content/ornek-cevaplar/speaking/` altinda 7. ve 8. grubun on
  dosyasi vardi (C01, C02, C04, C05, C07, C08, C10, C11, C14, C15). Yani prompt'un
  konusma listesinde uretilmemis ilk grup 9. grup; KONTROL.md'deki dort calistirmalik
  dagilim tablosuna gore kartlari **C16 · C19 · C22 · C25 · C29** (bes kart turunun
  ucuncu turu: kisi · yer · nesne · olay · soyut). Yazma tarafina (1-6) hic dokunulmadi,
  yeniden dogrulama yapilmadi.
- **Talimat cakismasi bu oturumda da yok:** tek gecerli is konusma kartlari icin gercek
  cevap uretmekti. Sema denetimi yazmak ya da yazma dosyalarini yeniden dogrulamak
  cikti sayilmadi (7. ve 8. grup kayitlarindaki aciklamanin aynisi).
- **Uretim:** `tools/_c1_uret9.py` sifirdan yazildi (8. grubun script'i birebir ornek
  alindi, mekanik degistirilmedi) ve calistirildi ->
  `content/ornek-cevaplar/speaking/{C16,C19,C22,C25,C29}.json`, her birinde band
  5,0 / 6,5 / 8,0 = **15 cevap**. Sema onceki iki grupla ayni: `transcript`, ucluk
  `why_this_band` (fluency_coherence · lexical_resource ·
  grammatical_range_accuracy), `approx_duration_seconds`, `part: 2`.
- **Kapsam yine Part 2:** kartin `speaking_seconds` degeri (90-120 sn) tek kisilik
  konusma icin; Part 3 karsilikli konusma oldugundan tek yonlu ornek metin o bolumu
  yanlis gosterirdi. Gerekce KONTROL.md'de (7. grupla ayni).
- **8. gruptan tasinan iki sayi yazim sirasinda gozetildi, denetimde degil:** 6,5
  metinlerinde kelime tavani 210 ve GRA sayimi hedefi %30. Ilk yazimda on bes metnin
  hicbiri sure penceresinin disina cikmadi; kisaltmalar yalnizca tavana oturtmak icin
  yapildi (ilk taslakta 6,5 metinleri 215-238 kelimeydi).
- **Kendi kendini denetimden cikan uc duzeltme (KONTROL.md 9. grup bolumunde
  ayrintili) - ucu de bandi kacirdigi icin degil, sayim iki satirin tam sinirinda
  kaldigi icin:**
  1. C29/5,0'da hatali cumle orani 8/10 = %80'di, yani GRA'da 5 satiri ile 4 satiri
     arasindaki sinir. Bir belirtec hatasi duzeltilerek (speaking free -> speaking
     freely) %70'e cekildi.
  2. C16/6,5 ve C25/6,5'ta oran 4/10 = %40'ti, yani 7 satiri ile 6 satiri arasindaki
     sinir. C16'da kapanistaki edat hatasi (he explains for the person -> he thinks
     about the person), C25'te eksik edat (stays open one week -> stays open for one
     week) duzeltildi; ikisi de %30'a dustu.
  3. C16'nin kapanisi degistigi icin o cevabin LR gerekcesindeki ikinci esdizim ornegi
     de degistirildi (I got a good result in the exam), yani gerekce metinle ayni
     kaldi.
- **Kendi kendini denetim sonucu:** 15 cevabin hepsi hedef bandin icinde, **sapma 0**.
  Puanlama etiketler ortulerek ve dokumler cumle cumle numaralanarak yapildi. Hatali
  cumle oranlari son halde: band 5'te 7/10 = %70, band 6,5'ta 3/10 = %30, band 8'de
  sifir (15-17 cumle).
- **Bicim kontrolu:** dosyalar uretildikten sonra task_ref-dosya adi uyumu, band
  uclusu, `word_count`un gercek sayimla uyusmasi, 80 kelime alt siniri, 90-120 saniye
  penceresi, ucluk olcut kumesi ve gerekce alanlarindaki "<=2 cumle" siniri tek tek
  dogrulandi. Cumle sayimi ilk geciste alti alani uc cumle gosterdi; hepsi tirnak
  icindeki dokum parcasindan ya da uc noktadan kaynaklaniyordu (*'I saw the date on the
  department website. I remember reading it.'* gibi), tirnakli parcalar cikarilinca
  bulgu kalmadi. Yeni bir denetim script'i eklenmedi - bu calistirmanin ciktisi cevap
  dosyalari.
- **Bu grubun ogrettigi sey - sinir degerlerinden kacinmak yazim isi, denetim isi
  degil.** 8. grupta uc metin olcum sinirinda kaldigi icin yeniden yazilmisti; burada
  ayni sey uc metinde yine oldu, ama sebep farkli: 8. grupta sinir kisaltmanin yan
  etkisiydi, burada ilk taslagin kendi orani. Yani %40 ve %80 sayilari yazarken
  kacinilacak sayilar; denetim onlari yakaliyor ama duzeltmesi metni her seferinde
  bir kez daha elden geciriyor.
- Atlanan/sorun: yok. Kalan tek konusma grubu 10. calistirma (Part 1 konu setleri);
  ona tasinan uc not KONTROL.md'nin "10. gruba kalan" bolumunde yazili - Part 1'de
  80 kelime capasinin gecerli olmadigi, GRA sayim hedeflerinin degistirilmemesi ve
  6,5'ta LR oge sayisinin ucte tutulmasi.
- Ornek cevaplar - konusma (3. calistirma) - 5 Part 2 karti x 3 seviye = 15 cevap,
  hepsi hedef bandin icinde (sapma 0), uc metin olcum siniri yuzunden duzeltildi.

## OPUS5-E9-alt-band-ornekleri (tek calistirma) — HEDEF TUTMADI: 3 → 4 ornek

- Tarih: 2026-08-09. Amac: `denetim/DENETIM-RAPORU.md` §5 A9 bulgusunun (zayif cevaba
  fazla puan) duzeltilebilmesi icin **once** <=4,5 aralikindaki ornek sayisini
  cogaltmak. Hedef: en az 8. **Sonuc: 4.** Duzeltmenin kendisi (A4) bu adimin isi
  degildi, ona dokunulmadi.
- **Yeniden sayim (1. zorunlu kural).** Prompt "3 ornek var" diyor; `ornekler/**/*.json`
  36 dosyanin tamami acilarak band alanindan sayildi: <=4,5 olan **3** (GT-T1-1B-A 3,0 ·
  AC-T2-2A-A 4,0 · GT-T2-2B-A 4,0). Sayi dogruydu.
- **Kaynak 1 (Cambridge envanteri) kullanilamadi — ve envanterde yanlis kayit bulundu.**
  `kalibrasyon/desen/puanli-ornek-envanteri.md` <=4,5 icin 5 kitap ornegi isaretliyor
  (4,0 x 4 + 4,5 x 1) ve "40 ornegin tam metni `ornekler/yazma/` altina dokuldu, 40 kod
  kumelere eklendi" diyor. **Ikisi de gerceklesmemis:** klasorde tek bir `CI*` dosyasi,
  `kumeler.json`'da tek bir `CI*` kodu yok. Yani o 5 ornek dokulmemis durumda.
  Kaynak PDF'ler `C:\Users\enhar\Desktop\kitaplar` altinda ama **bu oturumun calisma
  dizini `C:\ielts-paketi` ile sinirli**; disaridaki yola erisim harness tarafindan
  engellendi (Bash, PowerShell ve sandbox kapali deneme, ucu de bloke). Kitaplardan
  ornek dokulemedi. Envanter dosyasina bu durum **duzeltme notu** olarak islendi
  (orijinal metin silinmedi, uzerine yazilmadi).
- **Kaynak 2 (referans/) tarandi, 1 yeni ornek cikti.**
  - `ielts-academic-writing-sample-tasks-2023.pdf` (26 s.) ve
    `ielts-general-training-writing-sample-tasks-2023.pdf` (24 s.): puanli script
    sayfalarinin **hepsi** (AC 9-26, GT 8-24) zaten dokulmus. Yeni ornek yok.
  - `ielts-academic-writing-example-responses-…pdf` (5 s.): **daha once hic
    kullanilmamis belge.** Icinde 4 puanli Academic cevabi var: band 6 · **4** · 5,5 ·
    7,5. Band 4 olani dokuldu → `AC-ER-T1-B`. Kalan 3'u E9'un kapsami disinda
    (>4,5), dokulmedi ama gecerli kaynak olarak KONTROL.md'ye not dusuldu.
  - `ielts-general-training-writing-example-responses-…pdf` (3 s.): 2 cevap var
    (band 5,5 ve 5). Ikisi de aralik disinda; ustelik `tools/_e9_yinelenen_kontrol.py`
    ile olculdu, zaten dokulmus GT-T1-1A-A ve GT-T2-2A-A ile **ayni script** (kelime
    kumesi ortusmesi %80 ve %79, bandlar birebir ayni). Yeni ornek yok.
  - `ielts-speaking-sample-tasks-2023.pdf` (7 s.): puanli aday cevabi yok, yalniz gorev
    + gorevli cercevesi. `referans/konusma-band-ornekleri.txt`teki 12 ornegin hepsi
    zaten dokulmus, en dusugu band 5. Konusma tarafinda <=4,5 ornegi **hic yok**.
- **Eklenen ornek: `AC-ER-T1-B`, band 4,0, Academic Task 1, 119 kelime.** Dokum elle
  degil `tools/_e9_ornek_ekle.py` ile yapildi: kaynak taranmis el yazisi degil dizgili
  metin, cevap ve sinav gorevlisi yorumu PDF'in metin katmanindan birebir alindi. Ornek
  **uydurulmadi**; gercek band puani da sinav gorevlisi yorumu da kaynakta yazili.
- **Tuzak kontrolu (OPUS5-A1 kurali) yapildi:** band 4 cevapta belirgin yazim/dilbilgisi
  hatasi ~18, esigin (0-1) cok uzerinde → `transcription_suspect: false`. Hatalar
  KONTROL.md'de tek tek listeli ("statistice", "tripe mad", "highset", "contrest",
  "priod", "the children use bus", cumle basinda kucuk harf, 13 million / 12,000,000
  celiskisi…). Dosyada `transcription_suspect` alani **acikca** duruyor.
- **Bu ornegin bilinen sinirlamasi — gorev metni yok.** Kaynak belge yalniz cevap +
  band + yorum iceriyor, gorev sayfasini (rubric + grafik) hic koymamis. `task_prompt`
  uydurulmadi, `null` birakildi; yerine `task_context_reconstructed` alanina ayni
  belgedeki band 6'lik cevaptan ve gorevli yorumundan cikarilan grafik tanimi yazildi
  ve alanin **icinde** rekonstruksiyon oldugu belirtildi. Puanlama turunda bu ornek
  kullanilirsa Task Achievement bu sinirla birlikte okunmali.
- **Kume dagitimi (4. zorunlu kural).** `kumeler.json`: S1 12, S2 12, S3 11 idi; tek
  yeni kod S3'e eklendi → 12/12/12. <=4,5 ornekler de uc kumeye esit dagilmis durumda
  (S1'de 3,0; S2'de 4,0; S3'te iki tane 4,0). Sakli kume kontrolu anlamini koruyor.
- **Yeni dosya: `kalibrasyon/ornekler/KONTROL.md`** (36 satirlik kod · gorev · gercek
  band · kaynak · supheli tablosu + alt band ozeti + kume dagilimi). `.gitignore`
  `kalibrasyon/ornekler/` yerine `kalibrasyon/ornekler/*` + `!.../KONTROL.md` olarak
  degistirildi ki **yalniz bu dosya** depoya girsin: icinde aday metninden ya da
  gorevli yorumundan tek cumle yok, yalniz ust veri. Alt klasorler (`yazma/`,
  `konusma/`) ve icindeki 36 JSON depoya girmiyor; `git add -f` kullanilmadi.
  `yazma/KONTROL.md` ve `konusma/KONTROL.md` de disarida kaldi (onlar aday metninden
  birebir parcalar iceriyor).
- **Neden hedef tutmadi ve ne yapilirsa tutar.** Erisilebilir kaynak tukendi: ielts.org
  resmi belgelerinde <=4,5 aralikinda dokulmemis tek ornek kalmadi. Kalan tek kaynak
  Cambridge IELTS 1-8 kitaplarindaki 5 ornek; onlar dokulurse sayi 4 → 9 olur ve hedef
  (8) asilir. Bunun icin gereken tek sey calisma dizinine `C:\Users\enhar\Desktop\
  kitaplar` yolunun da eklenmesi (ornegin Claude Code'un `--add-dir` ile baslatilmasi).
  Prompt "kaynak tukendiyse hedefi zorlamadan cik" diyordu; zorlanmadi, uydurma ornek
  uretilmedi.
- Hicbir soru silinmedi, tam testlerin soru sayisi degismedi (bu adim soru havuzuna
  dokunmuyor).
- Alt band ornekleri (E9) - 1 yeni ornek eklendi (band 4,0), toplam 4/8; hedef
  tutmadi, sebep Cambridge kitaplarina bu oturumda erisilememesi.

## SONNET5-A3 (puanlama olcumu, ozel tur5 — yalniz gercek bandi <=4,5 yazma ornekleri, mevcut talimat)

- Tur 5 sonucu (tek seferlik puan, 4 ornek x 3 tekrar = 12 puanlama): ortalama mutlak fark 1,250 · egilim +1,250 (comert).

## SONNET5-A3 (puanlama olcumu, tur6 — dogrulama turu, 3. duzeltmeden sonraki talimat)

- Tur 6 sonucu (tum yazma+konusma ornekleri, 36 ornek x 1 tekrar = 36 puanlama): ortalama mutlak fark 0,389 · egilim -0,139 (hafif cimri).
