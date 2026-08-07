# Çapraz Kontrol Özeti (Denetim — 2. çalıştırma)

- **Tarih:** 2026-08-07
- **Kaynaklar:** `content/DOGRULAMA/` altındaki bütün raporlar (`RAPOR.md` — çapraz doğrulama,
  `METINSIZ-RAPOR.md` + 19 JSON — parçasız çözüm ölçümü, `OLCU-reading.md` — sayısal ölçüler)
  ve `content/` altındaki 180 `status: "flagged"` sorunun `flag_reason` / `blind_basis` alanları.
- **Kural gereği bu rapor sadece durum tespiti yapar; hiçbir içerik dosyası değiştirilmemiştir.**

İki ayrı kontrol mekanizması çalıştı ve **birbirinden farklı şeyleri ölçtüler**; bu rapor
ikisini ayrı sayıp sonra birleştirir:

1. **Çapraz doğrulama (CAPRAZ-90):** her paketi, onu üretmeyen model cevap anahtarını
   görmeden çözdü → *cevap anahtarı doğru mu?*
2. **Parçasız çözüm ölçümü (METINSIZ):** okuma soruları, parça hiç gösterilmeden üç turda
   çözüldü → *soru parçaya muhtaç mı, yoksa dışarıdan mı biliniyor?*

`content/` altındaki 180 işaretin **tamamı 2. mekanizmadan** geliyor. 1. mekanizma tek bir
kalıcı işaret bırakmadı (nedeni aşağıda).

---

## 1. Toplam sayılar

### 1a. Çapraz doğrulama (kör çözüm, üretmeyen model)

| Oturum kapsamı | Soru | Uyuşan | Oran | Raporda işaretlenen |
|---|---:|---:|---:|---:|
| Okuma: TFNG + YNNG | 80 | 80 | %100 | 0 |
| Okuma: çoktan seçmeli (+ dinleme MC-çoklu) | 35 | 35 | %100 | 0 |
| Okuma: başlık / özellik / cümle sonu eşleştirme | 81 | 81 | %100 | 0 |
| Dinleme: çoktan seçmeli + eşleştirme | 83 | 83 | %100 | 0 |
| Okuma: tamamlama ailesi (7 tip) | 151 | 149 | %98,7 | 2 |
| Okuma: bilgi eşleştirme | 49 | 49 | %100 | 0 |
| Dinleme: form / plan-harita / tamamlama ailesi | 264 | 241 | %91,3 | 23 |
| **TOPLAM** | **743** | **718** | **%96,6** | **25** |

25 işaretin dökümü:

- **1'i yanlış alarm** (okuma short-answer practice/5 — `accepted_variants` cevabı zaten
  kapsıyordu, karşılaştırma scripti yalnız `answer` alanına bakmıştı).
- **24'ü cevap anahtarı biçim/varyant eksiği**, içerik hatası değil: rakam↔yazı (`5`↔`five`),
  tarih biçimi (`2nd`↔`second`), belirteç (`a/the`), boşluk (telefon numarası, `HR 942`),
  tekil/çoğul, bir de kelime sınırının izin verdiği ek sıfat (`seven` → `seven distinct`).
- **Bu denetimde 24'ünün de dosyada kapatıldığı doğrulandı:** 23 dinleme sorusu + AC3
  özet/39'un tamamında doğrulayıcının verdiği cevap artık `accepted_variants` içinde
  (24/24 kontrol edildi). Bu yüzden hiçbirinde `status: "flagged"` durmuyor.
- Dinleme oturumunun kendi düzeltmesiyle: %91,3'lük oran alt sınırdı, **içerik uyuşması
  %99,6** (264'te 263; tek gerçek ifade seçimi farkı L4/33, o da varyanta eklenmiş).

**Çapraz doğrulamanın net sonucu:** 743 soruda cevap anahtarı içerik düzeyinde pratikte
%100 uyuştu; bulunan her şey anahtar esnekliği meselesiydi ve kapatılmış durumda.
Açık kalan tek anahtar eksiği çapraz doğrulamadan değil METINSIZ raporundan geliyor:
`AC2/flow-chart-completion` soru 1'de yönerge sayıya izin verdiği hâlde
`accepted_variants` hâlâ yalnız `forty minutes` (bkz. §5, açık madde).

### 1b. Parçasız çözüm ölçümü (işaretlerin kaynağı)

| | Sayı |
|---|---:|
| Ölçülen okuma sorusu | 381 (391'in 10'u — diagram-labelling — görsel gerektirdiği için ölçülmedi) |
| Üç turun üçünde de parçasız doğru bilinen → `status: "flagged"` | **180 (%47)** |
| Resmî sınav sorularında aynı ölçümün tabanı | %57 |
| Dinleme / konuşma / yazma | ölçüm kapsamı dışında (hiç ölçülmedi, "temiz" demek değil) |

Genel oran (%47) resmî tabanın (%57) altında — yani havuz bütün olarak resmî sorulardan
daha az sızdırıyor. Sorun ortalamada değil, **dağılımda**: aşağıdaki tabloda üç tip %100
sızdırırken bir tip %6'da.

Ayrıca sayısal ölçü turu (`OLCU-reading.md`) 2 soruyu `status: "review"` yaptı
(practice/matching-headings 9, GT1/matching-information 3) — bunlar 180'e dahil değil.
Aynı ölçünün en yüksek örtüşmeli 10 sorusunun 8'i zaten METINSIZ turunda işaretlenmişti;
iki bağımsız yöntemin aynı soruları göstermesi işaretlerin güvenilirliğini artırıyor.

---

## 2. Soru tipi bazında işaretlenme oranı (okuma, METINSIZ)

| Soru tipi | Ölçülen | İşaretli | Oran | Üreten yuva |
|---|---:|---:|---:|---|
| Çoktan seçmeli | 30 | 30 | **%100** | `FABLE5-41` |
| YES / NO / NOT GIVEN | 23 | 23 | **%100** | `FABLE5-40` |
| Cümle sonu eşleştirme | 10 | 10 | **%100** | `FABLE5-42` |
| Özellik eşleştirme | 26 | 18 | %69 | `FABLE5-42` |
| Akış şeması tamamlama | 6 | 4 | %67 | `OPUS5-10` |
| Özet tamamlama | 43 | 26 | %60 (kelime bankalı alt tip: **14/14**) | `OPUS5-10` |
| TRUE / FALSE / NOT GIVEN | 57 | 30 | %53 | `FABLE5-40` |
| Cümle tamamlama | 37 | 13 | %35 | `OPUS5-10` |
| Tablo tamamlama | 12 | 4 | %33 | `OPUS5-10` |
| Not tamamlama | 33 | 9 | %27 | `OPUS5-10` |
| Kısa cevap | 10 | 2 | %20 | `OPUS5-10` |
| Başlık eşleştirme | 45 | 8 | %18 | `FABLE5-42` |
| Bilgi eşleştirme | 49 | 3 | **%6** | `OPUS5-11` |
| Diyagram etiketleme | 10 | — | **ölçülmedi** | `OPUS5-10` |
| **TOPLAM** | **381** | **180** | **%47** | |

**Evet, işaretler belli tiplerde yoğunlaşıyor.** Üç tip (çoktan seçmeli, YNNG, cümle sonu
eşleştirme) %100 ile tamamen sızdırırken bilgi eşleştirme %6, başlık eşleştirme %18'de.
Ortak payda tipin **yazılı seçenek metni taşıyıp taşımaması**: cevabı harf/konum olan ve
seçenek metni bulunmayan tiplerde (bilgi eşleştirme, başlık eşleştirme) sızıntı en düşük;
yazılmış seçenek/ifade metni olan tiplerde en yüksek. Tamamlama ailesi arada — ama oradaki
%27-35'lik puanlar iyimser: METINSIZ raporunun kendi tespitiyle, anlam düzeyinde
cümle tamamlama %86, özet (parçadan kelime) %93 biliniyordu; puanı kurtaran şey kavrayış
değil, "parçadan kelime kopyala" kuralının kelime tutturmayı zorlaştırması.

Önemli bir çapraz gözlem: **çapraz doğrulamada en temiz çıkan tipler ile METINSIZ'de en
kötü çıkan tipler aynı** (YNNG, MC, eşleştirme tipleri — hepsi %100 uyuşma, sıfır işaret).
Çelişki değil: iki yöntem farklı kusur arıyor. Bu soruların **cevabı doğru**, ama sorunun
kendisi parçasız çözülebiliyor. Cevap anahtarı denetimi bu kusur sınıfını yapısal olarak
göremez.

---

## 3. Üreten model bazında kırılım

Plan (`content/PLAN-soru-dagilimi.md`) her tipi tek bir yuvaya vermiş; model ile soru tipi
bu yüzden iç içe (aşağıdaki yorum bölümünde bu sınırlılık ayrıca söyleniyor). Çapraz
doğrulama yönü: Fable üretimini Opus, Opus üretimini Fable çözdü.

### Okuma (METINSIZ ölçümü + çapraz doğrulama)

| Üreten yuva | Tipler | Ölçülen | İşaretli | Oran | Çapraz doğrulama uyuşması |
|---|---|---:|---:|---:|---:|
| `FABLE5-41` | çoktan seçmeli | 30 | 30 | **%100** | 35/35 |
| `FABLE5-40` | TFNG + YNNG | 80 | 53 | %66 | 80/80 |
| `FABLE5-42` | başlık / özellik / cümle sonu eşl. | 81 | 36 | %44 | 81/81 |
| `OPUS5-10` | tamamlama ailesi (7 tip) | 141 | 58 | %41 | 149/151 |
| `OPUS5-11` | bilgi eşleştirme | 49 | 3 | **%6** | 49/49 |
| **Fable toplamı** | | **191** | **119** | **%62** | 196/196 |
| **Opus toplamı** | | **190** | **61** | **%32** | 198/200 |

### Dinleme (yalnız çapraz doğrulama; METINSIZ dinlemeye uygulanmadı)

| Üreten yuva | Tipler | Soru | Uyuşan | İşaret |
|---|---|---:|---:|---|
| `FABLE5-43` | çoktan seçmeli + eşleştirme | 88 | 88 (%100) | 0 |
| `OPUS5-21` | form / plan-harita / tamamlama ailesi | 264 | 241 (%91,3; içerik %99,6) | 23 (hepsi biçim, hepsi kapatıldı) |

**Fark var ve büyük: Fable üretimi okuma sorularının %62'si, Opus üretimindekilerin %32'si
işaretli.** Ama bu tabloyu "Fable kötü üretti" diye okumadan önce iki şey:

- **Model ile tip ayrıştırılamıyor.** Her tipi tek model üretti; %100 sızdıran üç tipin
  üçü de Fable'a düşen, doğası gereği seçenek metni taşıyan tiplerdi. Fable'a düşen başlık
  eşleştirme %18 ile havuzun en sağlam ikinci tipi — yani aynı model, sızıntıya elverişsiz
  tipte sağlam iş çıkarmış. Opus'a düşen tamamlama ailesinin %41'i de anlam düzeyinde
  %80-90'a çıkıyor (bkz. §2). Fark, model kalitesinden çok **tip + üretim alışkanlığı**
  bileşimi.
- **Buna rağmen model imzası gerçek:** kip imzası kusuru (aşağıda tema 1) yalnız Fable
  yuvalarının iki ayrı tipinde (YNNG, MC) bağımsız olarak çıktı; eşdizim kilidi / terim
  tanımı kusuru (tema 2-3) yalnız Opus'un tamamlama yuvalarında. İki üretim ailesinin
  **farklı sistematik hataları** var.

Dinlemede işaret oranlarının sıfır/sıfıra yakın olması, dinlemenin temiz olduğunu değil,
**dinlemeye parçasız çözüm ölçümü hiç uygulanmadığını** gösterir. Envanter raporundaki
"dinlemede hiç işaret yok" satırının açıklaması budur: ölçüm yapılmadı. Fable'ın okuma
MC'sindeki %100 sızıntının dinleme MC'sinde (`FABLE5-43`, 88 soru) tekrarlayıp
tekrarlamadığı **bilinmiyor** — bu, denetimin gördüğü en somut ölçüm boşluğu.

---

## 4. `flag_reason` temaları

**Önce dürüst bir tespit:** 180 işaretli sorunun `flag_reason` alanındaki metin **birebir
aynı tek cümle**: *"Parça gösterilmeden 3/3 turda doğru bilindi; genel kültürle
çözülebiliyor."* Oysa aynı soruların `blind_basis` alanı dört farklı mekanizma sayıyor:

| `blind_basis` | Soru | Pay |
|---|---:|---:|
| logic (cümle çerçevesi / seçenek eleme) | 78 | %43 |
| general_knowledge | 72 | %40 |
| option_wording (seçenek yazımı) | 20 | %11 |
| guess | 10 | %6 |

Yani `flag_reason` metni 180 sorunun **108'i için yanlış gerekçe** veriyor ("genel kültür"
diyor ama dayanak logic/option_wording/guess). Tema analizi bu yüzden `flag_reason`
metninden değil, `blind_basis` + `METINSIZ-RAPOR.md`'nin soru soru dökümünden yapıldı.
(Seçenek: `flag_reason` alanlarına gerçek mekanizma yazılabilir — karar proje sahibinin;
elden geçirme sırasında yanlış gerekçe yanlış düzeltmeye yönlendirir.)

Tekrarlayan temalar, sıklık sırasıyla:

**Tema 1 — Kip imzası: doğru cevap ölçülü, çeldirici mutlak yazılmış (~53 soru: YNNG 23 +
MC 30).** Aday parçayı değil cümlenin kipini okuyor: ölçülü/koşullu ifade → doğru,
mutlaklık sözcüğü ("clearly", "no difference", "only", "essential") → yanlış.
*Örnek:* YNNG'de NO cevaplıların hepsi mutlaklık taşıyor ("**clearly** improved", "made
**no difference**"), YES cevaplıların hepsi ölçülü ("**may** understate", "a **plausible**
one"); MC'de practice 3-4'ün doğru çifti "**probably** work together / **cannot yet** be
excluded", çeldiricileri "is **essential** / changed **nothing at all**". İki ayrı tipte
aynı imza → tek üretim ailesinin (Fable yuvaları) ortak alışkanlığı. Prompt düzeyinde
düzeltilebilir.

**Tema 2 — Genel kültür / dünya sabiti (72 soru, `blind_basis` düzeyinde en net ikinci
küme).** Sorunun cevabı parçaya değil dünyaya ait: Japonya'nın 47 ili, Voyager 2'nin
tarihi, Mount Logan, `28 days` yasal izin, Karacadağ–einkorn bağı, POMS/PANAS ölçek
tanımları, `displacement`/`surge` gibi tek karşılıklı alan terimleri. *Örnek:*
`short-answer` practice 4 — "24 January 1986" parça değişse de aynı cevap. Bu tema iki
alt kola ayrılıyor: **konu seçimi** (ünlü vaka: AC1 mercan, Uranüs uydusu) ve **terim
seçimi** (alanın stok sözcüğü boşluğa konmuş). Promptla değil, soru ekseni değişikliğiyle
düzelir.

**Tema 3 — Eşdizim kilidi: boşluk, kalıp öbeğin tahmin edilen ucunda (~20 soru, tamamlama
ailesi).** Boşluğun iki yanındaki kelimeler cevabı tek seçeneğe indiriyor; parça yalnızca
teyit ediyor. *Örnek:* "hidden round a ___" → *corner*; "an up-to-date ___" → *CV*;
"breaks are ___ so that no line is left uncovered" → *staggered*. Düzeltmesi mekanik:
boşluğu öbeğin öbür ucuna ya da cümlenin parçaya özgü değerine taşımak.

**Tema 4 — Tanım sızıntısı: ifade/cümle, cevabın tanımını kendisi veriyor (~15-20 soru;
özellik eşleştirme + kelime bankalı özet).** *Örnek:* özellik eşleştirmede "no way at all
of sensing the other animal" → *solid screen* (opak bölmenin tanımı); kelime bankalı
özette "**aynı** gönüllüler her iki koşuldan da geçti" → *within-subject* (terimin ders
kitabı tanımı). Kelime bankalı özetin 14/14 sızdırmasının ana nedeni.

**Tema 5 — Konumsal/yapısal düzen sızıntısı (küçük ama sistematik).** İçerikten tamamen
bağımsız kalıplar: iki cevaplı MC'de A ve G şıkkı 9 sorunun 9'unda da çeldirici, doğru
çift {C,F} 4 kez tekrar; akademik bilgi-eşleştirme setlerinin 4'ünde de A ve H tam birer
kez doğru; "sınırlılık beyanı" sorusu hep son paragrafa demirli. *Örnek:*
bilgi eşleştirme practice 6 + AC3 28 — "henüz hakem değerlendirmesinden geçmedi" tipi
ifade her bilimsel yazıda kapanışta durduğu için parçasız H çıkıyor.

Bir de tema olmayan ama kayda değer bulgu: **NOT GIVEN / FALSE ayrımı sorunu beklenirken
çıkmadı.** Çapraz doğrulama TFNG/YNNG'de 80/80 uyuştu ve NOT GIVEN'ların gerçekten NOT
GIVEN olduğunu ayrıca not etti; METINSIZ'de de TFNG'nin NOT GIVEN cevaplıları en az
bilinen küme (%44). Bu tiplerin sorunu klasik NG/F karışıklığı değil, yukarıdaki kip/konu
sorunları.

---

## 5. Desen yorumu: sistematik mi, dağınık mı?

**Sistematik — hem de tek tip sistematik değil, iki üretim ailesine göre ayrışan iki ayrı
desen:**

1. **Fable yuvalarının deseni (seçenek metinli tipler): kip imzası + konumsal düzen.**
   Aynı imzanın iki bağımsız tipte (YNNG, MC) ve ayrıca konum düzeninin (A/G asla doğru
   değil, {C,F} tekrarı) çıkması tesadüfle açıklanamaz; üretim promptunun cümle yazma
   alışkanlığı. **Risk altındaki tipler:** YES/NO/NOT GIVEN, çoktan seçmeli, cümle sonu
   eşleştirme — üçü de %100 işaretli, kullanılabilir stok fiilen 0-6 soruya inmiş
   (envanter raporuyla tutarlı). Dinleme MC/eşleştirme (`FABLE5-43`) aynı promptlar
   ailesinden geliyor ve **hiç ölçülmedi** — desen sistematikse orası da risk altında,
   ama şu an veri yok.
2. **Opus yuvalarının deseni (tamamlama ailesi): eşdizim kilidi + terim tanımı + kelime
   bankasında tanım/zıt-çift sızıntısı.** Üç ayrı çalıştırmada (6, 7, 8) aynı iki mekanizma
   tekrarlıyor; kelime bankalı özet alt tipi 14/14 ile bu ailenin en ağır vakası.
   **Risk altındaki tipler:** kelime bankalı özet, akış şeması, cümle/not tamamlamanın
   "alan terimi" soruları. Buna karşılık aynı ailenin sayısal/parçaya-özgü boşlukları
   tutarlı biçimde sağlam — sorun tipte değil, boşluğun nereye açıldığında.

Sistematik **olmayan** kısım da net: bilgi eşleştirme (%6) ve başlık eşleştirme (%18)
neredeyse temiz; oradaki birkaç işaret (son-paragraf sınırlılık kalıbı, AC3'ün iki zayıf
kanıtlı işareti) tekil ve raporlarda tek tek gerekçelendirilmiş. GT malzemesi de üç ayrı
çalıştırmada doğrulandığı gibi kendiliğinden bozuk soru üretmiyor; GT'deki sızıntılar hep
"kural ne olmalı" tipi soru kurgusundan geldi.

**Sonuç cümlesi:** Cevap anahtarları iki modelin çapraz kör çözümünde pratikte %100
doğrulandı ve bulunan 25 biçim eksiğinin 24'ü kapatıldı; buna karşılık parçasız çözüm
ölçümü, üretim ailelerine göre ayrışan iki sistematik sızıntı deseni buldu ve okuma
havuzunun %47'sini (180 soru) işaretledi — asıl karar yükü, %100 işaretli üç tip ile
kelime bankalı özet üzerinde.

### Bu rapordan çıkan, karar bekleyen maddeler (karar proje sahibinin)

1. **180 işaretli okuma sorusu** — seçenekler: işaretlileri at / mekanizma bazında elden
   geçir (kip imzası ve eşdizim kilidi mekanik düzeltmeye uygun; genel-kültür temalılar
   soru ekseni değişikliği ister) / %100'lük üç tipte yeni üretim. (Envanter raporundaki
   madde ile aynı; bu rapor mekanizma kırılımını ekliyor.)
2. **`flag_reason` metinleri tek tip ve 108 soru için yanlış gerekçe veriyor** — elden
   geçirme yapılacaksa önce gerekçelerin `blind_basis`/rapor dökümünden düzeltilmesi
   yanlış yönlendirmeyi önler.
3. **Dinleme hiç parçasız ölçülmedi** — özellikle `FABLE5-43` (MC + eşleştirme, 96 soru)
   okumada %100 sızdıran promptlarla akraba; ölçüm dinlemeye (en azından bu yuvaya)
   genişletilebilir.
4. **`AC2/flow-chart-completion` soru 1:** yönerge sayıya izin veriyor ama
   `accepted_variants` hâlâ yalnız `forty minutes`; `40 minutes` eklenmedikçe aday haksız
   puan kaybeder (METINSIZ raporunun bilinçli olarak ertelediği tek anahtar düzeltmesi).
5. **2 soru `status: "review"`da askıda** (practice/matching-headings 9,
   GT1/matching-information 3) — envanter raporunda da listelenmişti; sayım dışı kalmaya
   devam ediyorlar.
