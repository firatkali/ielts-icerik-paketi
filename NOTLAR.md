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
