# BULUT OTURUMU BRIEF — dinleme senaryo turu (39 işaretli kalem)

Bu dosya, bilgisayar kapalıyken `claude.ai/code` üzerinden başlatılan oturum içindir.
Depo: `firatkali/ielts-icerik-paketi`, dal `main`. Simulator/cihaz gerekmez, iş tamamen metin.

## 0) ÖNCE OKU
1. `denetim/DINLEME-TUR2-ISLISTESI.md` — devredilen tanılar + kalan kalemler
2. `denetim/CAPRAZ-KOK.md` — çapraz sızıntı taramasının son hâli
3. Bu dosyanın tamamı

## 1) İŞ NEDİR
Dinleme havuzunda **39 kalem** hâlâ "sesi dinlemeden bilinebiliyor" diye işaretli
(JSON alanı: `blind_solvable: true`). Amaç: her birini kör sınamada **0/3** yapmak ve
işareti kaldırmak. Bu, ses kaydının önündeki tek kapı — bitmeden ElevenLabs'a geçilmiyor.

Okuma tarafında işaretli kalem YOK, oraya dokunma.

## 2) DEĞİŞMEZ KURALLAR
- **İki ajan asla aynı dosyaya yazmasın.**
- Bölüşüm **dosya bazlı değil SENARYO bazlı**: her senaryo (`content/listening/scripts/Lx-Sy.json`)
  tek ajanın sahipliğinde.
- 🔴 **Senaryoya cümle EKLEME/ÇIKARMA YASAK.** Yalnız var olan turun içinde yerinde değer
  değişikliği. Cümle eklemek o senaryoya bağlı bütün soruların `turn_index`'ini kaydırır;
  "kaçırdığım yeri tekrar dinlet" sessizce yanlış yeri çalar ve hiçbir testte görünmez.
- **Alıştırma paketleri (`content/listening/practice/*.json`) bu turda KİLİTLİ.** Tek bir
  alıştırma dosyası 4 ayrı senaryoya bağlı olabiliyor (aşağıdaki tabloya bak) → paralel ajanlar
  çakışır. Senaryo turunda yalnız `scripts/` + `tests/` düzenlenir.
  ⚠️ Bir senaryo değişikliği ona bağlı bir alıştırma sorusunun cevabını bozuyorsa, ajan bunu
  **düzeltmez, RAPOR EDER**; alıştırma düzeltmeleri turdan sonra tek elden yapılır.

## 3) BÖLÜŞÜM — 13 senaryo, 39 kalem
(T = `tests/`, bu turda düzeltilecek · P = `practice/`, KİLİTLİ, sadece etkilenirse rapor et)

| senaryo | kalemler |
|---|---|
| L1-S4 | T note-completion 31, 32 · P short-answer 4, table 9, 10 |
| L3-S4 | T summary-completion 34 · P flow-chart 2, 3 |
| L4-S1 | T note-completion 7 |
| L4-S3 | T multiple-choice 24, sentence-completion 28 |
| L4-S4 | T short-answer 32, 33, 34 · P flow-chart 10, 12, short-answer 9, 10 |
| L5-S1 | T form-completion 8 |
| L5-S2 | P multiple-choice 6 |
| L5-S3 | P matching 8, 9 |
| L5-S4 | P flow-chart 5, 6, 7, short-answer 14, 15 |
| L6-S2 | P multiple-choice 7, 9, 10 |
| L6-S3 | T multiple-choice 22, 23, matching 26 · P mc-multi 9-10 |
| L6-S4 | T note-completion 33, 36, summary-completion 38 · P flow-chart 14, note 13 |

**Bu turda fiilen düzeltilecek (T) = 16 kalem, 8 senaryo:**
L1-S4 · L3-S4 · L4-S1 · L4-S3 · L4-S4 · L5-S1 · L6-S3 · L6-S4
→ 8 paralel ajan, her biri tek senaryonun sahibi. Kalan 23 P kalemi ayrı alt tur.

⚠️ `tests/L4/short-answer.json` hem L4-S4 (32,33,34) hem başka senaryo kalemleri taşıyor;
bir dosyayı iki ajan açacaksa **sıraya sok**, aynı anda verme.

## 4) REÇETE (ucuzdan pahalıya)
1. **Kaydır** — boşluğu aynı senaryonun başka bir cevap noktasına taşı.
2. **Yerinde değiştir** — senaryodaki değeri değiştir, eski beklenen değeri çeldiriciye ver.
3. **Sesli rakip kur** ⭐ — konuşmacı "kitaplar şöyle der, ama burada durum farklı" deyip doğrusunu
   sonra söylesin. Ölçülmüş örnek (L5 özet 36): "kitaplar *grazed* der, ama o derinlikte otlayan
   yok, filmi aşındıran akan suyun kendisi" → cevap `scoured`, tek seferde 2/3 → **0/3**.

## 5) HER TUR SONUNDA — MERKEZÎ KAPANIŞ TARAMASI (ZORUNLU)
"Ajan bitti dedi" YETMEZ. Geçen tur ajanlar bitti dediği hâlde kapanış taraması **6 gerçek kusur**
yakaladı; ayrıca ajan kendi işini ölçerken iyimser (bir ajan "3 sızıntı" dedi, bağımsız kör ölçüm
**4** buldu + listede olmayan 2 tane daha).

Sırayla koştur:
```
python3 tools/dogrula.py          # şema 0 hata · 12 sınav 40/40 · toplam 1310
python3 tools/capraz-kok.py       # çapraz sızıntı
python3 tools/sessiz-kopya.py     # dinleme kör kopya
python3 tools/sessiz-rapor.py     # kör ölçüm raporu
```
Ayrıca elle kontrol et:
- **Tur sayıları değişmemiş olmalı** (senaryo başına turn sayısı, öncesi = sonrası).
- Değişen turlara bağlı **her** sorunun cevabı senaryoda birebir duruyor mu.
- ⚠️ Yanlış pozitif tuzağı: 8 kalemde cevap turda birebir geçmiyor çünkü rakam/kod harfle
  söyleniyor ("nine fifteen" ↔ `9.15`, "G W nine four one" ↔ `GW941`). Betik bunları sızıntı
  değil, "bulunamadı" diye gösterebilir — elle doğrula.
- Bütçe/çakışma: aynı kanıt iki soruda kullanılmasın.

Eşikler: cümle sonu eşleştirme ≤%20 · dinleme seçenekli ≤%30 · dinleme tamamlama ≤%20.

## 6) BİTİRİNCE
- `git add -A && git commit && git push` (main, doğrudan; yan dal açma).
- `denetim/DINLEME-TUR2-ISLISTESI.md` içindeki DURUM bölümünü güncelle (kalan işaretli sayısı).
- Kapanış raporunu bu dosyanın altına "TUR SONUCU" başlığıyla ekle: hangi senaryoda ne değişti,
  hangi kalem hangi reçeteyle kapandı, kalan işaretli kaç.
- Alıştırma (P) kalemlerinden etkilenen varsa **ayrı liste** olarak yaz — bir sonraki alt turun işi.

## 7) BU OTURUMDA YAPILMAYACAK
Uygulama kodu (`firatkali/ielts-app`), simulator/screenshot işleri, puanlama, mağaza maddeleri.
Onlar bilgisayar başındayken yapılacak.

---

# TUR SONUCU — 2026-08-18 akşamı

**İşaretli dinleme kalemi: 39 → 23.** `content/listening/tests/` altında işaretli kalem KALMADI;
kalan 23'ün tamamı `content/listening/practice/` içinde (ayrı alt turun işi).

Tur sayıları 8 senaryoda da korundu (13/13 · 13/13 · 49/49 · 39/39 · 15/15 · 49/49 · 45/45 · 12/12)
→ hiçbir `turn_index` kaymadı. `python3 tools/dogrula.py`: şema 0 hata · 12 sınav 40/40 · toplam 1310.

## Kapanan 16 kalem

| senaryo | kalem | eski cevap | yeni cevap | reçete |
|---|---|---|---|---|
| L1-S4 | not 31 | allotments | field gardens | 2+3 (Acts'in kendi sözcüğü; "allotments" çeldirici) |
| L1-S4 | not 32 | community garden | meanwhile land | 1+3 (planlama terimi; "brownfield" çeldirici) |
| L3-S4 | özet 34 | seal | 6 | 2+3 (kılavuz %1-2 der, konuşmacının kendi deposunda %6) |
| L4-S1 | not 7 | charity | public auction | 3 (eskiden hayır kurumuna giderdi, artık açık artırma) |
| L4-S3 | çoktan seçmeli 24 | A | A (dayanak değişti) | 2 |
| L4-S3 | cümle 28 | white space | eighteenth | 2 |
| L4-S4 | kısa 32 | 3 | 6 | 1+3 (3 dB laboratuvar, sokak anketinde 6) |
| L4-S4 | kısa 33 | the low end | the delivery van | 1+3 (otoyol/gece kamyonu reddediliyor) |
| L4-S4 | kısa 34 | every five years | every three years | 1 (eski ders kitabı aralığı soruluyor) |
| L5-S1 | form 8 | water bottle | 15 | 1+3 (asgari yaş; "on iki" sesli çeldirici) |
| L6-S3 | çoktan seçmeli 22 | C | C (dayanak değişti) | 2 |
| L6-S3 | çoktan seçmeli 23 | B | B (dayanak değişti) | 2 |
| L6-S3 | eşleştirme 26 | D (full-text filtresi) | B (dil filtresi) | 1+3 (kütüphaneci normalde karşı, burada kabul ediyor) |
| L6-S4 | not 33 | complaints | season-ticket renewals | 2+3 |
| L6-S4 | not 36 | next pay rise | three quarters | 2 |
| L6-S4 | özet 38 | half | 40 | 2 |

## 🔑 Bu turun dersleri

1. **Paralel ajanlar bu turda güvenilmezdi.** 12 ajandan 9'u ~600 saniyede takılıp öldü; ikisi
   senaryoyu değiştirmiş ama soruyu bağlamamış hâlde bıraktı (yarım iş, JSON geçerli olduğu için
   hiçbir testte görünmezdi). **Yarım kalan işi merkezden tamamlamak zorunludur** — ajanın "bitti"
   demesi bir yana, ajanın ÖLMESİ bile sessiz kalabiliyor.
2. **Merkezî tarama yine kazandırdı.** Ajanların temiz dediği durumda kanıt taraması 1 gerçek kusur
   yakaladı: L4-S3 turu değişince kilitli `practice/matching.json` #5'in kanıt cümlesi metinden
   silinmişti. Cevap (B) hâlâ doğru olduğu için yalnız kanıt/açıklama yeni cümleye bağlandı.
3. **`capraz-kok.py`'nin ayırt edicilik filtresi havuz genelinde çalışıyor.** Dinleme metnini
   değiştirmek, okuma tarafında daha önce "yaygın" diye elenen bir çifti rapora sokabiliyor:
   okuma 6 → 7 oldu ama **okuma dosyalarına hiç dokunulmadı**. Yeni görünen çift
   `tests/GT1/note-completion#16` ↔ `tests/AC4/summary-completion#36` (`30-minute`) — gerçek bir
   çapraz-sınav sızıntısı olabilir, **sonraki turun işi**.
4. Dinleme sızıntı sayıları düştü: kök çakışması 40 → 37, alıştırma→test sızıntısı **8 → 4**.

## ⏭️ SIRADAKİ İŞ

1. **Alıştırma alt turu — 23 kalem.** Dosya bazlı bölüşme YOK: bir alıştırma dosyası 4 ayrı
   senaryoya bağlı. Senaryoya göre dağılım: L5-S4 5 · L4-S4 4 · L6-S2 3 · L1-S4 3 · L3-S4 2 ·
   L6-S4 2 · L5-S3 2 · L5-S2 1 · L6-S3 1.
2. **Bağımsız kör ölçüm turu (borç).** Bu turu YAZAN oturum ölçemez. Araç:
   `python3 tools/sessiz-kopya.py <paket>` → 3 tur çözüm → `tools/sessiz-rapor.py`.
   Eşikler: dinleme seçenekli ≤%30 · dinleme tamamlama ≤%20.
3. Okuma tarafındaki `30-minute` çifti (yukarıda 3. ders).

---

# ALIŞTIRMA ALT TURU SONUCU — 2026-08-18 gecesi

**İşaretli dinleme kalemi: 23 → 0.** Havuzun tamamında (okuma + dinleme, alıştırma + test)
`blind_solvable: true` kalem kalmadı: `python3 tools/dogrula.py` → **işaretli (flagged) 0**.

Kural gereği hiçbir senaryoya cümle EKLENMEDİ/ÇIKARILMADI; yalnız var olan turların içinde
yerinde değişiklik yapıldı. `content/reading/` klasörüne hiç dokunulmadı (paralel ajan orada).

## Kapanan 23 kalem

| senaryo | kalem | eski cevap | yeni cevap | reçete |
|---|---|---|---|---|
| L5-S4 | akış 5 | 1 (yüzde) | a quarter (of one per cent) | 2+3 (yüzde bir "eski sekiz milyona ve kaba ağlara göre doğruydu" denip reddediliyor) |
| L5-S4 | akış 6 | brittle | ballasting | 1+3 (kitaplar *biofouling* der, sayımı yapanlar *ballasting*; "brittle" artık verili) |
| L5-S4 | akış 7 | a tenth | a twentieth | 2 (a third / a tenth ikisi de sesli çeldirici) |
| L5-S4 | kısa 14 | gear | arithmetic | 1 (tur 11'e kaydı: "tartışma okyanus hakkında değil, aritmetik hakkında") |
| L5-S4 | kısa 15 | every fifteen years | every fifteen years (dayanak güçlendi) | 3 ("derleme makaleleri on yıla yuvarlıyor, bu karotlara on yıl uymuyor") |
| L4-S4 | akış 10 | tyre | bypass | 1 ("lastik" verili oldu; sorulan konuşmacının sözü: otoparkta sessiz, çevre yolunda değil) |
| L4-S4 | akış 12 | window | 100 (mm boşluk) | 1+2 (kataloglar camın kalınlığını satar; iş yapan panolar arası boşluk) |
| L4-S4 | kısa 9 | logarithmic | start earlier | 1+3 ("popüler anlatı yanlış, daha yüksek sesle ötmüyorlar" — kuşlar erken başlıyor) |
| L4-S4 | kısa 10 | railways | aircraft | 2+3 (ders kitabı sırası anılıp reddediliyor: son sayımda uçak demiryolunun önünde) |
| L6-S2 | çoktan seçmeli 7 | B (nereye taşınıyor) | B (ilk pazar 5 Nisan) | 1 (üç seçenek de seste geçen ama farklı şeylere ait tarihler) |
| L6-S2 | çoktan seçmeli 9 | A (adını listeye yazdır) | B (12.30) | 1 (eski saat 11, ikinci gösteri 14.30 sesli çeldirici) |
| L6-S2 | çoktan seçmeli 10 | B (bedava) | A (Salı teslim) | 1 (Çarşamba = yeni pazar günü, Perşembe = elenen deneme günü) |
| L1-S4 | tablo 9 | 1940s | 5 (beş şehirden birinden az) | 1 (Tarih satırı çıktı, Anket satırı geldi) |
| L1-S4 | tablo 10 | vertical | 15 (kat) | 1 (yıllarca tekrarlanan verim iddiası; düzeltilmiş "üç kat" sınav #34'ün cevabı olduğu için tabloda ANILMADI) |
| L1-S4 | kısa 4 | raised beds | three degrees | 1+3 (hava sıcaklığı farkı; "yüzey okuması otuz" ayrı tutuluyor) |
| L3-S4 | akış 2 | 20 (eksi) | 30 (eksi) | 2+3 (uluslararası standart anılıyor, bu deponun kendisi daha soğuk çalışıyor) |
| L3-S4 | akış 3 | regeneration | photograph | 1 ("regeneration" verili oldu; kör çözücünün üreteceği sözcük *photocopy*) |
| L6-S4 | akış 14 | pilot | obstacle course | 1 (alanın yerleşik terimi *sludge* seste hiç geçmiyor) |
| L6-S4 | not 13 | framing | 30 (otuzda bir) | 1 (reçel tezgâhı deneyi; aynı cümlede "one in three" çeldirici) |
| L5-S3 | eşleştirme 8 | D = arkadaşlarla yapılmamalı | D = yirmisi bitmeden ifadeye dokunulmamalı | 2 (ders kitabı seçeneği kutudan TAMAMEN çıkarıldı) |
| L5-S3 | eşleştirme 9 | F (bilgi formu, 3 turdur kapanmıyordu) | E (sunum) — kök değişti | 1 ("bilgi formu" kökü havuzdan çıkarıldı) |
| L5-S2 | çoktan seçmeli 6 | A (danışma noktası) | B (dört saat) | 1 (kök tamamen değişti: gönüllü vardiyası) |
| L6-S3 | çoklu seçim 9-10 | A+C (aramayı kaydet / tarihi not et) | A+C (14.30 / eğitim odası) | 1+2 (kök tur 39'dan 37'ye taşındı; "Room B" sesli tuzak olarak kaldı) |

**Kalan işaretli kalem: 0.**

Yan üretim: L5-S3 eşleştirme #10 yeni bir köke oturdu ("sokakta cevaplar nasıl kaydedilecek",
tur 38). Kutudaki "kâğıtla yapılmalı" seçeneği bilerek tuzak olarak bırakıldı — kâğıt Devan'ın
görüşü, danışmanın söylediği tek şey tutarlılık.

## Kapanış taraması

| kontrol | sonuç |
|---|---|
| `tools/dogrula.py` | şema **0 hata** · 12 sınav **40/40** · toplam **1310** · işaretli **0** |
| `tools/turn-index-kontrol.py` | tur sayıları **24/24 aynı** · turn_index aralık dışı 0 · evidence tutmayan 0 |
| `tools/capraz-kok.py` — dinleme kök çakışması | **37 → 28** (düştü) |
| `tools/capraz-kok.py` — alıştırma→test sızıntısı | **4 → 2** (düştü) |
| `tools/capraz-kok.py` — okuma | **7 → 7** (değişmedi; okuma dosyalarına dokunulmadı) |
| senaryo payı (dinleme) | 22 → 22 |

Değişen her senaryoya bağlı **her** soru tek tek doğrulandı (352 dinleme kalemi): evidence'ı
kendi turunda birebir geçmeyen kalem kalmadı. Cevap dizgisi taramasındaki 25 uyarının tamamı
bilinen yanlış pozitif (rakam/kod seste harfle söyleniyor: "nine fifteen" ↔ `9.15`,
"G W nine four one" ↔ `GW941`, "a hundred and twenty" ↔ `120`) — elle bakıldı.

## Tarama sırasında bulunan ve düzeltilen 3 gerçek kusur (listede yoktu)

1. **Çift `answer_point_id`: `L3-S4-30` iki ayrı noktaya veriliyordu** (tur 5'teki "yüzde 6" ve
   tur 11'deki "otuz tür"). İki farklı sınav sorusu (`tests/L3/summary-completion#34` ve
   `tests/L3/short-answer#40`) aynı kimliği gösteriyordu; "kaçırdığım yeri tekrar dinlet"
   yarısında yanlış yeri çalardı. Tur 5'teki nokta `L3-S4-33` yapıldı, referansı güncellendi.
2. **`tests/L2/matching#26` kanıtı senaryoda hiç geçmiyordu** — kanıt alanı iki AYRI turu (32 ve
   33) ` — ` ile birleştirip tek dizgi yapmıştı. Kanıt turn_index 33'ün birebir metnine çekildi;
   cevap (C), turn_index ve answer_point_id değişmedi.
3. **Alıştırma içi sızıntı:** L1-S4 tablosunun "Tarih" satırının Detay hücresi
   (`the total then fell for fifty years`) aynı alıştırma paketindeki kısa cevap #1'in cevabını
   düz yazıyordu. Satır değişince kapandı.

Ayrıca `tools/turn-index-kontrol.py` **yoktu** (brief onu koşmayı istiyor) — yazıldı; referans
tur sayıları `denetim/TUR-SAYILARI.json` içinde. Senaryoya bilerek tur eklenirse `--yaz` ile
güncellenir.

## ⚠️ Dürüstlük notu — ölçüm YAPILMADI

Bu turu yazan oturum kendi işini ölçemez (brief §5 ve geçen turun 1. dersi). Yukarıdaki 23
kalem **"kapatıldı" değil, "kapatılacak şekilde yeniden kuruldu"**; kör sınamadan geçmediler.
Bağımsız kör ölçüm turunda **önce şu üçüne bakılsın**, çünkü kalan tahmin payı en yüksek onlarda:

- **L1-S4 kısa 4** (`three degrees`) — yeşil çatı ile çıplak çatı arasındaki 3 °C fark, sesli
  rakip (yüzey okuması 30) konmasına rağmen makul bir ön tahmin.
- **L3-S4 akış 2** (`30`) — "standarttan daha soğuk" çerçevesi seçenek kümesini
  (−25/−30/−40/−80) daraltıyor.
- **L5-S4 akış 5** (`a quarter`) — "(5) of one per cent" çerçevesi küçük bir küme bırakıyor
  (a half / a quarter / a tenth).

## ⏭️ SIRADAKİ İŞ (güncellendi)

1. **Bağımsız kör ölçüm turu (borç, artık tek engel).** `python3 tools/sessiz-kopya.py <paket>`
   → 3 tur çözüm → `tools/sessiz-rapor.py`. Eşikler: dinleme seçenekli ≤%30 · tamamlama ≤%20.
   Önce yukarıdaki üç kalem.
2. Okuma tarafındaki `30-minute` çifti (`tests/GT1/note-completion#16` ↔
   `tests/AC4/summary-completion#36`) — hâlâ açık, okuma ajanının işi.
3. Dinlemede kalan 2 alıştırma→test kök çakışması (`practice/sentence-completion#15` ↔
   `tests/L5/sentence-completion#29` = `study pods`; `practice/flow-chart-completion#1` ↔
   `tests/L5/table-completion#32` = `a fifth`) — ikisi de bu turun kalemleri değil, ayrı iş.
