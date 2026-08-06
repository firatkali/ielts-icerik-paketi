# CAPRAZ-90 — Çapraz Doğrulama Raporu

Her paketi, onu **üretmeyen** model kör olarak (cevap anahtarını görmeden) çözer;
karşılaştırmayı `tools/karsilastir.py` yapar. Aşağıdaki bölümler çalıştırma sırasına
göre eklenir.

---

## doğru/yanlış/verilmemiş + evet/hayır/verilmemiş — 2026-08-06

- Doğrulayan model: opus (üreteni: fable)
- Toplam soru: 80
- Uyuşan: 80 (%100,0)
- İşaretlenen: 0

### Kapsanan dosyalar
| Dosya | Soru |
|---|---|
| content/reading/practice/true-false-not-given.json | 15 |
| content/reading/practice/yes-no-not-given.json | 15 |
| content/reading/tests/AC1/true-false-not-given.json | 7 |
| content/reading/tests/AC2/true-false-not-given.json | 7 |
| content/reading/tests/AC3/true-false-not-given.json | 7 |
| content/reading/tests/AC4/true-false-not-given.json | 7 |
| content/reading/tests/GT1/true-false-not-given.json | 7 |
| content/reading/tests/GT2/true-false-not-given.json | 7 |
| content/reading/tests/GT1/yes-no-not-given.json | 4 |
| content/reading/tests/GT2/yes-no-not-given.json | 4 |

### İşaretlenen sorular
Yok. Uyuşmayan soru çıkmadı ve hiçbir cevap 3'ün altında güvenle verilmedi.

### Örüntü

Sistematik hata görünmüyor; oran %95 eşiğinin üstünde ve işaretlenen soru yok.
Doğrulama sırasında dikkat çeken noktalar:

- **NOT GIVEN soruları gerçekten NOT GIVEN.** Pakette 22 NOT GIVEN cevabı var ve
  hepsinde metinde ilgili bilgi bulunmadığını doğrulamak kolay oldu: soru, metnin
  konuştuğu alanın hemen yanındaki ama metnin hiç değinmediği bir ayrıntıyı soruyor
  (AC1/13 kupun üstündeyken yiyeceği daha net görme, AC4/12 dört düzen arasındaki
  sıcaklık farkı, alıştırma TFNG/10 arazi ekibinin oraya nasıl gittiği). Bu, üretim
  promptundaki "üç şartlı test"in uygulandığını gösteriyor — dünya bilgisiyle
  doldurulabilecek ama metinde olmayan tuzaklar düzgün kurulmuş.
- **FALSE/NO soruları tek ve net bir çelişki noktasına dayanıyor.** Hepsinde metinde
  ifadeyi doğrudan çürüten tek bir cümle var (AC2/12 "no other planet ... as many
  small inner moons as Uranus", AC3/8 dört belugadan dördü de dişi, GT2/12 £5.20).
  Kısmî örtüşmeden doğan "yarı yanlış" ifade yok.
- **Ayrım kaymasına en yakın iki soru** AC3/13 (Monodontidae'nin "includes" ifadesi
  "only" anlamına gelmediği için NOT GIVEN) ve GT2/9 ("This year's ... in Castle Park"
  ifadesinin her yıl anlamına gelmemesi). İkisinde de kör çözüm anahtarla uyuştu,
  yani ayrım hem üretende hem doğrulayanda aynı yerden geçiyor. Yine de bu iki soru,
  ikinci bir doğrulamada tekrar bakılmaya en uygun adaylar.
- **YNNG paketi görüş/olgu ayrımına sadık kalmış.** GT2/33 (hükümetlerin daha fazlasını
  yapması gerektiği) yazarın hiç görüş bildirmediği bir nokta olduğu için NOT GIVEN;
  YNNG'de sık görülen "metinde konu geçiyor, o hâlde YES" hatası bu pakette yok.

**Not (yöntem):** 3. adımı çalıştırırken `dogrulama/cevap/` klasöründe önceki bir
oturumdan kalan `matching-sentence-endings` cevap dosyası bulundu ve ilk karşılaştırmaya
10 fazladan soru olarak karıştı. Dosya `.eski` uzantısıyla kenara alınıp karşılaştırma
tekrarlandı; yukarıdaki 80 soruluk sonuç temiz çalıştırmaya aittir. `tools/kor-kopya.py`
`dogrulama/kor/` klasörünü siliyor ama `dogrulama/cevap/` klasörünü temizlemiyor —
sonraki oturumlarda aynı karışıklığın olmaması için oturum başında bu klasörün boş
olduğu kontrol edilmeli.

---

## çoktan seçmeli (okuma) + çoktan seçmeli-çoklu — 2026-08-06

- Doğrulayan model: opus (üreteni: fable)
- Toplam soru: 35
- Uyuşan: 35 (%100,0)
- İşaretlenen: 0

### Kapsanan dosyalar
| Dosya | Soru |
|---|---|
| content/reading/practice/multiple-choice.json | 12 |
| content/reading/tests/AC1/multiple-choice.json | 3 |
| content/reading/tests/AC2/multiple-choice.json | 3 |
| content/reading/tests/AC3/multiple-choice.json | 3 |
| content/reading/tests/AC4/multiple-choice.json | 3 |
| content/reading/tests/GT1/multiple-choice.json | 3 |
| content/reading/tests/GT2/multiple-choice.json | 3 |
| content/listening/practice/multiple-choice-multi.json | 5 |

Soru sayıları soru **nesnesi** sayısıdır; "34-35" gibi iki kutuluk çoklu seçim
soruları tek nesne sayılır. Cevap kağıdı kutusu olarak toplam 49 kutu eder
(24 test + 15 okuma alıştırma + 10 dinleme alıştırma).

### İşaretlenen sorular
Yok. Uyuşmayan soru çıkmadı; tek düşük güvenli cevap AC2/34-35 (güven 4) idi ve o da
anahtarla uyuştu.

### Örüntü

Sistematik hata görünmüyor; oran %100 ve işaretlenen soru yok. Dikkat çeken noktalar:

- **Çeldiriciler metnin içinden kuruluyor, uydurma değil.** Neredeyse her çeldirici,
  metinde geçen ama sorunun sorduğu şey olmayan gerçek bir ayrıntı: AC1/32'de "unusual
  warmth" (metin asitlenmeden söz ediyor, ısınmadan değil), AC4/34-35'te "nap length
  predicted the memory gain" (metin tam tersini söylüyor), A08/9-10'da "North America's
  highest peak" (Mount Logan Kanada'nın en yükseği). Bu, aday için gerçek ayrım gerektiren
  ama tek doğru cevabı olan sağlam bir yapı.
- **Çoklu seçim (TWO letters) soruları en riskli tip olmasına rağmen temiz.** 9 çoklu
  seçim sorusunun hepsinde iki doğru şık metinde ayrı ayrı ve açıkça destekleniyor,
  kalan beş şık ya tersine çevrilmiş ya da başka bir paragrafa ait. "Üçüncü bir şık da
  savunulabilir" durumu hiçbirinde çıkmadı.
- **Tek zayıf nokta AC2/34-35 F şıkkı:** "Colleagues never meet one another in person."
  Metin "without face-to-face contact" diyor ve şirketin hiç fiziksel ofisi olmadığını
  söylüyor, yani şık doğru — ama "never" metinde birebir yok, çıkarımla geliyor. Diğer
  şıklar açıkça yanlış olduğu için soru yine tek cevaplı; buna rağmen ikinci doğrulamada
  bakılmaya en uygun aday bu.
- **Amaç/işlev soruları ("Why does the writer...") doğru kurulmuş.** AC1/32, AC3/32,
  AC4/32, A08/12 gibi sorularda cevap, metnin ilgili cümlesinin işlevini birebir
  karşılıyor; bu tipte sık görülen "metinde geçen bir bilgiyi doğru ama alakasız amaç
  olarak sunma" hatası yok. AC3/32'de C şıkkı (birikinti derinliği) nedenselliği ters
  çeviriyor — kasıtlı ve iyi kurulmuş bir çeldirici.

**Not (kapsam):** Prompt tablosunda `multiple-choice-multi` bu oturuma yazılmış, ancak
depoda bu ada sahip tek dosya **dinleme** alıştırma dosyası (`content/listening/practice/
multiple-choice-multi.json`). Okuma tarafında ayrı bir `-multi` dosyası yok; çok cevaplı
okuma soruları normal `multiple-choice.json` dosyalarının içinde. Başka hiçbir oturum bu
dosyayı kapsamadığı için doğrulamaya dahil edildi (5 soru, hepsi uyuştu). Oturum 4'ün
kapsamındaki dinleme `multiple-choice` dosyalarına dokunulmadı.

**Not (yöntem):** Oturum 1'den kalan cevap dosyaları bu oturuma karışmasın diye
`dogrulama/cevap-arsiv/oturum1/` altına taşındı; karşılaştırma temiz klasörle çalıştı.
