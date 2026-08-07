# İşaretli soruları elden geçirme — mekanizma bazında düzeltme

Kaynak talimat: `prompts/OPUS5-E5-isaretli-elden-gecirme.md` (8 çalıştırma).
Bu dosya her çalıştırmada bir bölüm kazanır.

Girdi raporları: `ISARET-GEREKCELERI.md` (E1 — mekanizma etiketleri),
`ANLAM-DUZEYI-RAPOR.md` (E10 — anlam düzeyinde ek işaretliler),
`kalibrasyon/desen/*` (E4), `denetim/capraz-ozet.md` §4.

---

## 1. çalıştırma — YES/NO/NOT GIVEN, kip imzası · 2026-08-08

### Kapsam ve kendi sayımım

Talimatın 1. kuralı gereği sayıya güvenmeyip yeniden saydım. `content/` altında
`question_type: "yes_no_not_given"` taşıyan üç dosya var ve içlerindeki
`status: "flagged"` soru sayısı **23**:

| Dosya | Soru | İşaretli |
|---|---|---|
| `content/reading/practice/yes-no-not-given.json` | 15 | 15 |
| `content/reading/tests/GT1/yes-no-not-given.json` | 4 | 4 |
| `content/reading/tests/GT2/yes-no-not-given.json` | 4 | 4 |
| **toplam** | **23** | **23** |

E1'in dağılım tablosundaki 23 sayısıyla birebir aynı. E10 bu tipe hiç dokunmadı
(üç çalıştırması da tamamlama ailesindeydi), dolayısıyla bu tipte ek işaretli yok.

Tipin tamamı işaretli, çünkü `OPUS5-B1` ölçümünde **23/23 (%100)** parçasız bilindi —
ürünün en yüksek sızıntı oranı bu tipte (`UYARILAR.txt`, 07.08.2026 kaydı).

### Önce: kip imzası gerçekten var mı?

23 ifadeyi cevaplarına göre değil, **yazılış kipine** göre sınıflandırdım:

| Kip | YES (10) | NO (7) | NOT GIVEN (6) |
|---|---|---|---|
| mutlak / eşdeğerlik / üstünlük / normatif | 0 | **7** | 0 |
| ölçülü (can, may, tend to, plausible…) | 5 | 0 | 0 |
| yalın | 5 | 0 | 0 |
| eksen dışı boyut ekliyor | 0 | 0 | **6** |

Üç satırlık bir kural çıkıyor:

> mutlak yazılmışsa → NO · pasajın eksenine yeni bir boyut ekliyorsa → NOT GIVEN ·
> geri kalan → YES

Bu kural 23 sorunun **23'ünü** doğru bilir. B1'in ölçtüğü %100 tam olarak bu.
İki alt imza ayrı ayrı da kusursuz ayırıyordu:

- **Yedi NO'nun yedisi** bir mutlaklık taşıyordu: `clearly`, `failed to produce`,
  `made no difference`, `in much the same way`, `as well as`, `should be counted`,
  `most`. Hiçbir YES ifadesinde mutlaklık yoktu.
- **Altı NOT GIVEN'ın altısı** pasajın hiç ele almadığı bir *boyut* ekliyordu:
  cinsiyet kırılımı (10), yaş kırılımı (13), incelenmemiş bir şirket kategorisi (1),
  deneyden sonra ne olduğu (8), listede geçmeyen bir neden (GT1-36), yazarın hiç
  dile getirmediği bir politika yargısı (GT2-33). Soruyu okumak yetiyordu; pasaja
  bakmaya gerek yoktu.

### Sonuç dağılımı

| Sonuç | Soru | Numaralar |
|---|---|---|
| **Düzeltildi** | 13 | practice 1, 3, 6, 7, 8, 10, 13, 14 · GT1 35, 36 · GT2 33, 35, 36 |
| **Elendi** | 9 | practice 2, 4, 5, 9, 12, 15 · GT1 33, 34 · GT2 34 |
| **Dokunulmadı** | 1 | practice 11 |
| **toplam** | **23** | |

Elenen 9 sorunun tamamı E1'in `genel_kultur` etiketlediği sorular; elenen ile
`genel_kultur` kümesi bu tipte birebir örtüşüyor.

### Düzeltmenin iki yönü

Kip imzasını kırmak için tek yön yetmiyor. İfadeleri yalnız yumuşatsaydım
"ölçülü = YES" imzası yerine "ölçülü = NO" imzası kurardım — aynı sızıntının
tersi. Bu yüzden iki yönde birden çalıştım:

**a) Mutlak yazılmış NO'lar ölçülü kipe çekildi** (4 soru)

| Soru | Eski | Yeni |
|---|---|---|
| practice-3 | "star performers **clearly** improved…" | "…**tended to** produce **a little** more than they otherwise would" |
| practice-14 | "made **no difference** to how well it was recalled" | "**seems to have mattered little** to how well they were later recalled" |
| GT2-36 | "explain **most** of the health advantage" | "**appear to** account for **a little over half** of the health advantage" |
| practice-6 | "**failed to produce** a clear ordering" | "were able to rank **only two of the four** designs against each other" |

Dördü de hâlâ NO, çünkü kanıt cümleleri aynı kaldı ve ölçülü iddiayı da aynı
netlikte çürütüyor: practice-3'ün kanıtı faydanın "burada hiç görülmediğini"
söylüyor, dolayısıyla küçük bir artışı da dışlıyor.

**b) Bir YES mutlak kipe çekildi** (1 soru)

| Soru | Eski | Yeni |
|---|---|---|
| practice-7 | "came more easily … than the remaining designs" | "outscored **every other design in the trial**" |

Kanıt cümlesi (E/2) iki yarı kapalı düzenin hem tamamen açık hem de sabit masasız
düzenden üstün olduğunu söylüyor; denenen dört düzenden geri kalan ikisi zaten
tam olarak bunlar, dolayısıyla kapsayıcı ifade doğru. Artık sette **mutlak yazılmış
bir YES** var, yani "mutlak = NO" kuralı yanlış cevap veriyor.

**c) Kanıttan sözcük kaldıran düzeltmeler** (2 soru)

| Soru | Eski | Yeni |
|---|---|---|
| GT1-35 | "**may** understate the true extent of food loss" | "Food that households composted or gave to animals **was left out of** the study's main waste totals" |
| GT2-35 | "The idea … **is a plausible one**" | "Volunteering **may** improve health **indirectly, by raising** household income" |

GT2-35 iki yönden sızdırıyordu: `plausible` sözcüğü kanıt cümlesinden birebir
alınmıştı ve "bu fikir akla yatkın mı?" biçimindeki sorular neredeyse her zaman
YES çıkar. Yeni ifade yazarın kurduğu dolaylı yolun kendisini soruyor.

### NOT GIVEN'ların yeniden çapalanması (6 soru)

NOT GIVEN'da korunacak kanıt cümlesi yok — `evidence` zaten `null` ve öyle kaldı;
korunan şey **yokluğun kendisi**, yani cevabın NOT GIVEN olması. Sızıntı ifadenin
*ekseninde*ydi: hepsi pasajın hiç konuşmadığı bir boyut ekliyordu ve bu biçim tek
başına cevabı ele veriyordu. Altısını da pasajın bol bol konuştuğu bir eksene
taşıdım; artık metnin gerçekten karara bağlamadığı bir ayrıntıyı soruyorlar.

| Soru | Eski eksen dışı boyut | Yeni çapa |
|---|---|---|
| practice-1 | incelenmemiş bir şirket kategorisiyle kıyas (ofisli şirketler) | deneyimlilerin rehberlik için kendi çıktısından ödün verip vermediği — F/G/H konuyu işliyor, maliyeti hiç ölçmüyor |
| practice-8 | deneyden sonra hangi düzenin kurulduğu | etkinlik tabanlı ile takım ofisinin gürültüsü — F/1 yalnız açık planı alternatiflerle karşılaştırıyor, alternatifleri kendi aralarında hiç sıralamıyor |
| practice-10 | cinsiyet kırılımı | tazeleyici etkinin 15 dakika içinde nasıl seyrettiği — E, anketlerin yalnız hemen önce ve hemen sonra uygulandığını söylüyor |
| practice-13 | yaş kırılımı (yaşlı yetişkinler) | günün saatinin sınanıp sınanmadığı — C ve D saatleri ayrıntısıyla veriyor, F sınanan değişkenleri sayıyor ve saat yok |
| GT1-36 | neden listesinde geçmeyen bir neden (tarih etiketi) | 215 hanenin nasıl seçildiği — B yöntemi tek tek anlatıyor, seçim yöntemine hiç girmiyor |
| GT2-33 | yazarın hiç dile getirmediği politika yargısı | sağlık avantajının gönüllülük oranı yüksek ülkelerde daha büyük olup olmadığı — D ülke farklarını, C avantajı veriyor, ikisi hiç çaprazlanmıyor |

Altısında da `answer` NOT GIVEN ve `evidence` `null` olarak korundu; yeniden
yazılan alanlar `prompt`, `not_given_justification`, `scan_note`, `explanation`.

### Elenen 9 soru

Hepsinin ortak yanı, sorunun **ekseninin kendisinin** genel kültür olması: ifade
nasıl yazılırsa yazılsın cevap pasajdan değil dünya bilgisinden çıkıyor. Kip
dengelemesi bunu kapatmaz, o yüzden mekanik düzeltmeye uygun değiller.

| Soru | Cevap | Eksen |
|---|---|---|
| practice-2 | YES | rastgele/sıra usulü atama nedensellik çıkarımını güçlendirir (metodoloji kuralı) |
| practice-4 | YES | deneyimli çalışan yeni gelene rehberlik eder (işyeri mentorluğu) |
| practice-5 | YES | açık plan ofis tartışmalı bir konudur (popüler iş yaşamı söylemi) |
| practice-9 | YES | doğa stresi azaltır görüşü yaygın kabul görür |
| practice-12 | YES | doğanın etkisi kışın da sürer + pilot çalışma haberleri olumlu sonuçla çıkar |
| practice-15 | NO | şekerleme gece uykusunun yerini tutmaz (popüler uyku bilimi) |
| GT1-33 | YES | öz-bildirim doğrudan ölçümden güvenilmezdir (metodoloji kuralı) |
| GT1-34 | NO | kabuk/kemik "önlenemez" kategoride sayılır (gıda israfı sınıflandırması) |
| GT2-34 | YES | öz-bildirimli sağlık ölümü öngörür (çok atıf yapılan literatür bulgusu) |

Dokuzu da `status: "rejected"` + `reject_reason` aldı, dosyalarında **numaralarıyla
duruyor** ve `content/DOGRULAMA/yeniden-uretim-listesi.json` dosyasına eklendi.
Her kayıt, o pasajda zaten soru sorulmuş kanıt cümlesini `kacinilacak` altında
taşıyor, böylece E6 aynı cümleye ikinci soru yazmaz.

### Dokunulmayan 1 soru

**practice-11** (NO, A11). Sızıntı ifadenin kipinde değil, **kanıt cümlesinin
kendisinde**: G/1 "The pattern after the building condition was essentially the
reverse" diyor. Bu kanıta dayanan her NO ifadesi, "kontrol koşulu tedavi koşuluyla
aynı sonucu vermez" deney mantığıyla parçasız çözülebiliyor — ifadeyi ölçülü
yazmak yetmiyor, farklı bir kanıt cümlesi gerekiyor. Talimata göre kanıt cümlesini
değiştirmek yarım düzeltme sayıldığı için soru olduğu gibi bırakıldı; gerekçe
`review_note` alanına yazıldı. `status` hâlâ `flagged`.

### Kip imzası kırıldı mı?

Düzeltilen 13 sorunun yeni kip dağılımı:

| Kip | YES (3) | NO (4) | NOT GIVEN (6) |
|---|---|---|---|
| mutlak | **1** (practice-7) | 0 | 0 |
| ölçülü | 1 (GT2-35) | **3** (practice-3, 14, GT2-36) | 0 |
| yalın | 1 (GT1-35) | 1 (practice-6) | 6 |
| eksen dışı boyut ekliyor | 0 | 0 | **0** |

Eski üç kuralın üçü de artık çalışmıyor: "mutlak → NO" kalan tek mutlak ifadede
(practice-7) yanlış cevap veriyor; "ölçülü → YES" dört ölçülü ifadenin yalnız
birinde tutuyor; "eksen dışı → NOT GIVEN" hiçbir soruda uygulanamıyor.

### 🔴 E6 ve E7'ye devir notları

1. **Kip dengesi set düzeyinde bir iştir ve yarısı E6'da.** Elenen 9 yuva
   dolduruluncaya kadar sette yalnız 3 YES + 4 NO var. E6, 9 yerine soru yazarken
   **en az bir mutlak yazılmış NO ve en az bir mutlak yazılmış YES** koymalı;
   koymazsa bu sette "mutlak = YES" biçiminde **ters** bir imza oluşur (şu anda
   tek mutlak ifade bir YES). Aynı şekilde ölçülü ifadeler de iki cevaba
   dağıtılmalı.
2. **Yeniden çapalanan 6 NOT GIVEN ölçülmemiş sorudur.** Cevap ve `evidence`
   korundu ama yokluk gerekçesi baştan yazıldı; hepsinde `blind_solvable: null`
   duruyor. E7 bunları yeniden ölçmeli.
3. **practice-6 kısmi düzeltme.** Blanket olumsuzlama kaldırıldı ve yerine sayısal
   bir iddia kondu, ama "karşılaştırmalı bir çalışma bir sonuç bildirmiştir"
   sezgisiyle akıl yürüten bir çözücü hâlâ NO'ya varabilir. E7 ölçümünde bu soruya
   ayrıca bakılmalı.
4. **practice-11 açık kalıyor.** Kanıt cümlesi değişmeden düzeltilemez; E6'nın
   yeniden üretim kapsamına alınması yerinde olur.

### Doğrulama

```
python tools/_e5_ynng_elden_gecir.py     # duzeltildi 13 · elendi 9 · dokunulmadi 1
python tools/_e5_dogrula_degisim.py      # KORUNAN ALAN HATASI: 0
python tools/dogrula.py
```

- `answer`, `evidence`, `evidence_locator` üç dosyada da **hiç değişmedi**
  (HEAD ile alan alan karşılaştırıldı, 0 fark).
- Soru sayısı ve numaralar değişmedi: 15 + 4 + 4 = 23 soru girdi, 23 çıktı.
  GT1 ve GT2 tam testleri 40/40; on iki tam testin hepsi 40/40 kaldı.
- `isaretli (flagged)` 221 → **199** (13 verified + 9 rejected; practice-11 flagged
  kaldı).
- Şema hatası **0**.

#### Rebase notu — dil çevirisiyle çakışma

Bu çalıştırma sırasında depoya paralel iki commit girdi (`28ecd89`, `34236cf`:
"Kullaniciya gosterilen tum alanlar Ingilizceye cevrildi"), ve bu üç YNNG dosyasına
da dokundu: 2026-08-08 kuralı gereği bütün `explanation` alanları İngilizceye
çevrildi. Çakışma, üç dosyanın **yukarı akış sürümü esas alınıp E5 betiği onun
üzerine yeniden koşturularak** çözüldü. Sonuç:

- Elenen 9 ve dokunulmayan 1 sorunun `explanation` alanı yukarı akışın İngilizce
  çevirisiyle duruyor (E5 bu alanlara dokunmuyor).
- Düzeltilen 13 sorunun `explanation` alanı zaten E5 tarafından İngilizce yazıldı.
- Yani 23 sorunun 23'ünde `explanation` İngilizce; şema hatası sayısı çakışma
  öncesindeki 743'ten **0**'a indi. Bu düşüşün tamamı yukarı akış çevirisinin
  eseri, E5'in değil.
- `answer` / `evidence` / `evidence_locator` karşılaştırması çözümden **sonra**
  yukarı akış sürümüne karşı yeniden koşuldu: yine 0 fark.
