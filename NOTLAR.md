# Üretim notları

Bu dosyaya her oturumda alınan kararlar, atlanan işler ve karşılaşılan sorunlar yazılır.

## Ortam
- İşletim sistemi: Windows
- Çalışan Python komutu: `python` (veya `py` / `python3` — hangisi çalıştıysa)
- Referanslar: `referans/*.pdf` — **metne çevrilmedi, Read aracıyla doğrudan PDF okunacak**

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
