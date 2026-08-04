# Üretim notları

Bu dosyaya her oturumda alınan kararlar, atlanan işler ve karşılaşılan sorunlar yazılır.

## Ortam
- İşletim sistemi: Windows
- Çalışan Python komutu: `python` (veya `py` / `python3` — hangisi çalıştıysa)
- Referanslar: `referans/*.pdf` — **`Read` aracının PDF render'ı bu makinede çalışmıyor** (`pdftoppm` kurulu değil, "poppler" hatası verir). Sistemde `pdftotext` (Git for Windows / poppler ile gelen) kurulu; PDF'i okumak için `pdftotext -layout referans/<dosya>.pdf -` ile terminale bas ve öyle oku. `referans/text/` klasörü önceden boştu, gerekirse `pdftotext -layout kaynak.pdf referans/text/kaynak.txt` ile çıktısı orada da tutulabilir.

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
