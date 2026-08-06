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

---

## eşleştirme tipleri (başlık + özellik + cümle sonu) — 2026-08-06

- Doğrulayan model: opus (üreteni: fable)
- Toplam soru: 81
- Uyuşan: 81 (%100,0)
- İşaretlenen: 0

### Kapsanan dosyalar
| Dosya | Soru |
|---|---|
| content/reading/practice/matching-headings.json | 15 |
| content/reading/tests/AC1/matching-headings.json | 5 |
| content/reading/tests/AC2/matching-headings.json | 5 |
| content/reading/tests/AC3/matching-headings.json | 5 |
| content/reading/tests/AC4/matching-headings.json | 5 |
| content/reading/tests/GT1/matching-headings.json | 5 |
| content/reading/tests/GT2/matching-headings.json | 5 |
| content/reading/practice/matching-features.json | 10 |
| content/reading/tests/AC1/matching-features.json | 4 |
| content/reading/tests/AC2/matching-features.json | 4 |
| content/reading/tests/AC3/matching-features.json | 4 |
| content/reading/tests/AC4/matching-features.json | 4 |
| content/reading/practice/matching-sentence-endings.json | 10 |

Dağılım: başlık eşleştirme 45, özellik eşleştirme 26, cümle sonu eşleştirme 10.

### İşaretlenen sorular
Yok. Uyuşmayan soru çıkmadı ve hiçbir cevap 3'ün altında güvenle verilmedi.

### Örüntü

Sistematik hata görünmüyor; oran %100 ve işaretlenen soru yok. Doğrulama sırasında
dikkat çeken noktalar:

- **Başlık eşleştirmede çeldiriciler bilinçli olarak "fazla dar" kurulmuş.** Kullanılmayan
  başlıkların çoğu, doğru paragrafın *bir cümlesini* karşılayan ama paragrafın ana fikrini
  karşılamayan ifadeler: AC1'de "Choosing animals of a similar build" (B'nin yalnızca ağırlık
  eşleştirme cümlesi), GT1'de "Skins and other leftovers from preparing meals" (E'nin son
  cümlesi), A09'da "Equipment built especially for the site" (D'deki özel görüntü işleme
  yöntemi — cihaz değil yazılım). Bu, IELTS'in gerçek zorluk kaynağı ve doğru kurulmuş.
- **Ters çevrilmiş çeldiriciler de var ve net.** A08/F için "A glacier stopped in its tracks"
  metnin tam tersini söylüyor (buzul durmuyor, molozu taşıyor); A11/C için "An urban view
  chosen to create stress" metnin açıkça reddettiği bir okuma (kentsel nokta bilerek sakin ve
  trafiksiz seçilmiş). İkisi de dikkatsiz adayı yakalar, dikkatli adayı yanıltmaz.
- **Ayrım en zayıf yerde bile bozulmuyor — ama bir soru sınıra yakın.** AC3/14 (A08 paragraf B)
  bu paketin tek belirsiz sorusu: paragrafın ilk cümlesi 700+ heyelanı sayıyor ("A tally of the
  slopes that failed"), kalan dört cümlesi olağan haritalama yönteminin buz örtüsü yüzünden
  neden işe yaramadığını anlatıyor ("Why the usual approach did not work"). Kör çözümde gist
  gerekçesiyle ikincisi seçildi ve anahtarla uyuştu (güven 3), ancak *her iki başlık da yalnızca
  bu paragrafa uyuyor* — yani çeldirici, başka bir paragrafa demirlenmiş değil. İkinci
  doğrulamada bakılmaya en uygun tek aday bu; "vii" başlığını C veya D paragrafına
  demirlenebilecek bir ifadeyle değiştirmek soruyu tamamen tartışmasız hâle getirir.
- **Özellik eşleştirmede tekrar izni doğru kullanılmış.** `allow_repeat: true` olan iki sette
  (AC4 anketler, alıştırma P-MF-01/02) tekrar eden şıklar gerçekten metinden iki ayrı yere
  dayanıyor (Restorative Outcome Scale hem F hem G paragrafında; kahve/çay hem B'deki günlük
  yöntemi hem F'deki dökme nedeni). "Tekrar var ama aslında aynı cümleye iki soru" durumu yok.
  Tekrarsız setlerde ise (AC1-AC3) kullanılmayan şık her seferinde metinde geçen gerçek bir
  varlık — uydurma boş seçenek yok.
- **Cümle sonu eşleştirmede dilbilgisi kontrolü tutuyor.** 10 sorunun tamamında kök cümle ile
  doğru son, hem dilbilgisi hem anlam olarak sorunsuz birleşiyor; ayrıca yanlış sonların çoğu
  *dilbilgisel olarak da* uyuyor (yani aday sadece dilbilgisine bakarak eleyemiyor), bu tipte
  en sık görülen üretim hatası burada yok. A07 setinde kullanılmayan üç son (F, G, H) metinde
  gerçekten geçen bilgiler — sağ göz tercihi, ayna/panel önünde geçen saatler, bağımsız evrim.

**Not (yöntem):** Oturum 2'den kalan cevap dosyaları `dogrulama/cevap-arsiv/oturum2/` altına
taşındı; karşılaştırma temiz klasörle çalıştı. (Oturum 1 notundaki uyarı hâlâ geçerli:
`tools/kor-kopya.py` `dogrulama/cevap/` klasörünü temizlemiyor.)

---

## dinleme — çoktan seçmeli + eşleştirme — 2026-08-06

- Doğrulayan model: opus (üreteni: fable)
- Toplam soru: 83
- Uyuşan: 83 (%100,0)
- İşaretlenen: 0

### Kapsanan dosyalar
| Dosya | Soru |
|---|---|
| content/listening/practice/multiple-choice.json | 10 |
| content/listening/tests/L1/multiple-choice.json | 7 |
| content/listening/tests/L2/multiple-choice.json | 7 |
| content/listening/tests/L3/multiple-choice.json | 3 |
| content/listening/tests/L4/multiple-choice.json | 3 |
| content/listening/tests/L5/multiple-choice.json | 7 |
| content/listening/tests/L6/multiple-choice.json | 3 |
| content/listening/practice/matching.json | 10 |
| content/listening/tests/L1/matching.json | 3 |
| content/listening/tests/L2/matching.json | 3 |
| content/listening/tests/L3/matching.json | 8 |
| content/listening/tests/L4/matching.json | 8 |
| content/listening/tests/L5/matching.json | 3 |
| content/listening/tests/L6/matching.json | 3 |

Dağılım: çoktan seçmeli 40 (37 tek cevaplı + 3 çift harfli "14-15" sorusu),
eşleştirme 43. Okumadaki `multiple-choice.json` dosyaları (7 dosya) 2. oturumda
doğrulandığı için kör kopyaları silindi, bu oturumda açılmadı.

### İşaretlenen sorular
Yok. Uyuşmayan soru çıkmadı ve hiçbir cevap 3'ün altında güvenle verilmedi.

### Örüntü

Sistematik hata yok. Bu paketin ayırt edici özelliği, tüm senaryoların **"düzeltme"
mimarisi** üzerine kurulmuş olması: her senaryonun `notes` alanında 4-7 çeldirici
düzeltme sayılıyor (konuşmacı önce eski/yanlış bilgiyi söylüyor, sonra düzeltiyor).
Doğrulama sırasında görülenler:

- **Çeldiriciler sağlam demirlenmiş.** Her düzeltme çiftinin *her iki* ucu da şık
  listesinde yer alıyor: L2/11'de "bir yıl beklentisi" (B değil A) ile "18 ay gerçek",
  L5/13'te afişteki "20 dakika" ile gerçek "15 dakika", L6/21'de el kitabındaki
  "3.000 kelime" ile ders sayfasındaki "2.500". Aday yalnızca ilk duyduğu sayıyı
  yazarsa yakalanıyor — istenen davranış tam olarak bu.
- **Çeldiriciler senaryo içinden *başka bir soruya ait* doğru bilgi olarak da
  kullanılmış.** Bu, bu paketin en iyi tarafı. L1/13'te "watch a weaving demonstration"
  senaryoda gerçekten var ama dokuma galerisinde, avluda değil; L1/14-15'te "twice a
  day" rehberli turlara, "booking required" 8 kişiden büyük gruplara ait; L2/21'de
  "brook was in flood" doğru ama *ikinci örneklemeyi geciktiren* neden, alan
  atlamasının nedeni değil. Uydurma çeldirici yok.
- **Görüş ayrımı soruları (Bölüm 3) tutarlı biçimde üçe ayrılmış.** L1, L2, L3, L4,
  L5, L6 senaryolarının tamamında iki öğrenci ve danışman her tartışma ekseninde ayrı
  konumda ve her konum ayrı bir `answer_point` olarak işaretli. Eşleştirme setleri bu
  yapıdan besleniyor ve "kimin görüşü" soruları tek bir replikle kesin çözülüyor
  (L3/24-26, L4/21-23, L6/24-26). Konuşmacı karıştırma riski hiçbir soruda oluşmadı.
- **Kutu şıklarında kullanılmayan seçenekler gerçek metin verisi.** L3-S2 setinde
  kullanılmayan B ("changed to a different day") ve G ("once a month") senaryodaki
  rehberli yürüyüş ve çalılık temizleme günlerine karşılık geliyor; L4-S2'de
  kullanılmayan G ("behind a locked gate") boya/kimyasal deposu; L5'te kullanılmayan
  D ve E açık uçlu sorularla ilgili. Boş/uydurma şık yok.
- **En düşük güvenle verilen altı cevap** (L1/24, L2/25, L4/21, L5/24, L6/24 ve
  alıştırma eşleştirme 2 — güven 4) hepsi anahtarla uyuştu. Bunlar "doğru şık kesin ama
  ifade metindekinden bir adım soyut" durumları: "only for context" → "background
  information only", 11'e karşı 23 familya → "differed sharply", "something you can
  actually add up" → "can simply be added together". IELTS'te normal ve kabul edilebilir
  bir mesafe; işaretleme gerektirmiyor.

**Not (yöntem):** Oturum 3'ten kalan cevap dosyaları `dogrulama/cevap-arsiv/oturum3/`
altına taşındı. `tools/kor-kopya.py` hem okuma hem dinlemedeki `multiple-choice.json`
dosyalarını birlikte üretiyor (21 dosya); okumaya ait 7 kör kopya, açılmadan önce
silindi.

## okuma — tamamlama tipleri (note / table / flow-chart / summary / sentence completion, short-answer, diagram-labelling) — 2026-08-06

- Doğrulayan model: fable (üreteni: opus)
- Toplam soru: 151 (23 dosya: 5 alıştırma + AC1-AC4 + GT1-GT2)
- Uyuşan: 149 (%98,7)
- İşaretlenen: 2

Tip kırılımı:

| Soru tipi | Soru | İşaretlenen |
|---|---|---|
| summary-completion | 43 | 1 |
| sentence-completion | 37 | 0 |
| note-completion | 33 | 0 |
| table-completion | 12 | 0 |
| diagram-labelling | 10 | 0 |
| short-answer | 10 | 1 |
| flow-chart-completion | 6 | 0 |

### İşaretlenen sorular
| Dosya | Soru | Orijinal | Doğrulayıcı | Güven | Kısa gerekçe |
|---|---|---|---|---|---|
| content/reading/practice/short-answer.json | 5 | 8,400 years | 8,400 years old | 4 | Yanlış alarm: `accepted_variants` zaten "8,400 years old" içeriyor, script yalnızca `answer` alanına bakıyor. Düzeltme gerekmiyor. |
| content/reading/tests/AC3/summary-completion.json | 39 | seven | seven distinct | 4 | Metinde "seven **distinct** proteins" geçiyor, sınır İKİ KELİME; aday sıfatı da yazabilir. `accepted_variants` listesine "seven distinct" eklenmeli. |

### Örüntü

**Sistematik sorun yok — bu, yedi oturumun şu ana kadarki en yüksek uyuşma oranı
(%98,7).** Tamamlama tipleri doğası gereği "metinden kelime kopyalama" soruları
olduğu için yorum payı dar; buna rağmen dikkat çeken üç şey var:

- **İki uyuşmazlığın ikisi de aynı türden: kelime sınırının izin verdiği ekstra
  sıfat/isim.** İkisinde de cevabın *içeriği* doğru; anlaşmazlık yalnızca boşluğa
  kaç kelime yazılacağında. Bu, "yanlış soru" değil, "eksik `accepted_variants`"
  sorunudur ve tek düzeltmesi varyant listesini genişletmektir. Gerçek sınavda
  puanlayıcı her iki cevabı da kabul eder; burada `answer` alanı dar tutulduğu için
  otomatik puanlama adayı haksız yere yanlışa düşürür. **Öneri: tamamlama
  tiplerinin tamamında, boşluğun hemen önündeki/ardındaki sıfat ya da ölçü biriminin
  de yazılabileceği durumlar için `accepted_variants` bir kez taranmalı** — özellikle
  sayı + isim kalıpları ("seven proteins", "8,400 years", "fourteen approaches").
- **Kelime sınırları tutarlı biçimde uygulanmış.** 151 sorunun hiçbirinde anahtar
  cevabı kendi yönergesindeki sınırı aşmıyor; ONE WORD ONLY setlerinde (AC1
  note-completion, AC3 sentence-completion, AC4 note-completion, GT1 summary-completion)
  cevapların hepsi gerçekten tek kelime, tireli bileşikler ("sound-absorbing",
  "15-minute", "five-point") dahil. Üretim promptundaki sınır kontrolü çalışmış.
- **Tek gerçek belirsizlik alıştırma diagram-labelling 10. soruda** (güven 3, yine de
  uyuştu; cevap "instant messaging"). Şemadaki ok telefon ikonundan çıkıyor ve G04
  metninde çekirdek saatler için "reachable by **phone or video call**" da yazıyor;
  ama bu ifade ÜÇ KELİME sınırına sığmadığı için aday zorunlu olarak "instant
  messaging"e yöneliyor. Yani soru **sınır sayesinde** tek cevaba iniyor, şema
  sayesinde değil. İşaretlemeye gerek görmedim, ama şemadaki bağlantı çizgisi telefon
  yerine dizüstü/mesajlaşma tarafından çıksaydı soru kendi başına daha temiz olurdu.
- **Alıştırma dosyalarındaki çoklu-pasaj yapısı sorun çıkarmadı.** Beş alıştırma
  dosyasının hepsinde her soru `passage_id` taşıyor ve boşluk numaralandırması
  pasajlar arasında kesintisiz; 65 alıştırma sorusunun tamamı doğru pasajdan
  çözülebildi.

---

## okuma — bilgi eşleştirme (matching-information) — 2026-08-06

- Doğrulayan model: fable (üreteni: opus)
- Toplam soru: 49
- Uyuşan: 49 (%100,0)
- İşaretlenen: 0

### Kapsanan dosyalar
| Dosya | Soru | Pasaj |
|---|---|---|
| content/reading/practice/matching-information.json | 15 | A01, A04, A07, A11 |
| content/reading/tests/AC1/matching-information.json | 5 | A03 |
| content/reading/tests/AC2/matching-information.json | 5 | A06 |
| content/reading/tests/AC3/matching-information.json | 5 | A09 |
| content/reading/tests/AC4/matching-information.json | 5 | A12 |
| content/reading/tests/GT1/matching-information.json | 7 | G01 (beş duyuru, A-E) |
| content/reading/tests/GT2/matching-information.json | 7 | G02 (beş duyuru, A-E) |

### İşaretlenen sorular
Yok. Uyuşmayan soru çıkmadı ve hiçbir cevap 3'ün altında güvenle verilmedi.
49 cevaptan 48'i güven 5, biri (AC1/29) güven 4 ile verildi ve o da anahtarla uyuştu.

### Örüntü

Sistematik hata yok; oran %100. Bilgi eşleştirme, doğası gereği **"iki paragraf da
olabilir"** tuzağına en açık okuma tipidir — soru kökü metinden bilerek uzaklaştırılmış
bir başka anlatımla yazıldığı için, aynı fikrin izi birden fazla paragrafta bulunabilir.
Bu pakette bunun olmamasının somut nedenleri var:

- **Her soru tek bir cümleye demirlenmiş, paragrafın genel konusuna değil.** 49 sorunun
  tamamında `evidence` alanı tek bir cümleyi gösteriyor ve o cümle, soru kökündeki bilgiyi
  tam olarak karşılıyor. "Paragraf bu konudan söz ediyor, o hâlde cevap budur" biçiminde
  gevşek bir eşleşme hiçbir soruda yok. Bu, bilgi eşleştirmeyi başlık eşleştirmeden ayıran
  kritik fark ve doğru uygulanmış.
- **`uniqueness_check` alanı gerçekten çalışıyor.** Anahtarı gördükten sonra bakıldığında,
  her soruda rakip paragrafın adıyla anıldığı ve neden elendiğinin yazıldığı görülüyor
  (AC1/27'de "B bacaların CO2 saldığını söylüyor ama canlılar üzerindeki kimyasal sonucu
  anlatmıyor; G iskeletin yapımını değil yıkımını anlatıyor"). Kör çözümde elediğim
  paragraflar ile bu alanda elenmiş paragraflar birebir örtüştü — yani ayrım hem üretende
  hem doğrulayanda aynı yerden geçiyor.
- **Tek sınıra yakın soru AC1/29.** "A contrast between what a whole living community
  reveals and what tests on separate creatures reveal" için A paragrafı ("how marine
  ecosystems will actually respond, rather than merely how individual organisms behave
  under short-term laboratory stress") kesin doğru; ama E paragrafı da "rather than
  modelling a hypothetical future, researchers can measure how a real reef community
  actually behaves under it" diyor ve *yüzeyde* aynı karşıtlığı kurar gibi görünüyor.
  Ayrım şurada: E'nin karşıtlığı **varsayımsal modelleme** ile, ayrı ayrı canlılar
  üzerindeki testlerle değil. Soru kökündeki "tests on separate creatures" ifadesi bu
  ayrımı taşıdığı için soru tek cevaplı kalıyor. Yine de ikinci doğrulamada bakılmaya en
  uygun tek aday bu; E'deki "a real reef community" ifadesi bilinçli bir çeldirici olarak
  bırakılmışsa iyi kurulmuş, değilse tesadüfi bir yakınlık.
- **Soru kökleri anahtar kelime avını sistemli biçimde engelliyor.** Neredeyse hiçbir kök,
  metindeki ifadeyi ödünç almıyor: GT2/4 "one day of an event on which things stop several
  hours earlier than on the other days" — adayın 22.30 ile 18.00'i kendisi karşılaştırması
  gerekiyor, metinde "earlier" kelimesi hiç geçmiyor. AC3/27 "how long the remains had been
  on record" için metinde yalnızca "since the 1960s" var, süre yazılı değil. AC2/31 "the
  single count chosen to stand for how much work each person got done" için metin "the
  number of distinct clients" diyor. Bu, tipin en zor ve en doğru biçimi.
- **Cevaplar metin sırasını izlemiyor** — bilgi eşleştirmede olması gereken de bu (başlık
  eşleştirmeden farklı olarak). AC1: C-H-A-G-E, AC2: F-A-H-B-D, AC3: B-H-E-A-F,
  AC4: D-A-H-G-C. Hiçbir sette artan sıra yok, kümelenme yok. Test setlerinde sekiz
  paragraftan beşi kullanılmış ve hiçbir harf tekrar etmemiş.
- **GT setlerinde tekrar izni doğru kullanılmış.** İki GT dosyasında da yönerge "NB You may
  use any letter more than once" diyor ve tekrar gerçekten var: GT1'de A (soru 2 adres kanıtı
  ve soru 6 rezervasyon nedeniyle uzatamama) ile B (soru 4 veli onayı ve soru 7 yarıyıl
  tatili), GT2'de A (soru 2 blokaj ve soru 5 kayıp bedeli) ile E (soru 3 telefonla kayıt ve
  soru 7 asgari öğrenci sayısı). Her tekrar, duyurunun **farklı bir cümlesine** dayanıyor;
  "aynı cümleye iki soru" durumu yok.

**Not (alıştırma dosyası):** 15 soruluk alıştırma seti dört ayrı pasaja bölünmüş
(A01/A04/A07/A11, 4+4+4+3) ve yönergesinde "NB You may use any letter more than once"
yazıyor. İfade set genelinde doğru (A harfi hem 2. hem 14. soruda cevap), ancak **tek bir
pasaj bloğu içinde hiçbir harf tekrar etmiyor**. Aday soruları pasaj pasaj çözdüğü için bu
NB pratikte bilgi vermiyor; yanıltıcı değil ama gereksiz. Diğer altı dosyada sorun yok.

**Not (yöntem):** Oturum 5'ten kalan 23 cevap dosyası `dogrulama/cevap/` klasöründe
duruyordu ve ilk karşılaştırmaya karıştı (200 soru raporlandı, oturum 5'in iki işaretli
sorusu tekrar listelendi). Dosyalar `dogrulama/cevap-arsiv/oturum5/` altına taşınıp
karşılaştırma tekrarlandı; yukarıdaki 49 soruluk sonuç temiz çalıştırmaya aittir.
**Bu, aynı karışıklığın üst üste dördüncü oturumda yaşanması** (1, 2, 3 ve 5. oturum
notlarına bakınız). `tools/kor-kopya.py` `dogrulama/kor/` klasörünü temizliyor ama
`dogrulama/cevap/` klasörüne dokunmuyor; kalıcı çözüm ya scriptin bu klasörü de arşivlemesi
ya da `tools/karsilastir.py`'nin yalnızca o oturumda üretilen kör kopyalara karşılık gelen
cevap dosyalarını okumasıdır.
