# Dinleme sızıntı ölçümü — senaryo gösterilmeden soru bilinebiliyor mu

## Yöntem notu — okuma ölçümünden dört farkı

**1. Gizlenen şey pasaj değil, ses metni.** Okuma tarafındaki `METINSIZ-*` ölçümü soruyu
pasajdan ayırıyordu; burada soru **ses metninden** (`content/listening/scripts/`) ayrılıyor.
Ölçülen soru şu: "senaryo hiç gösterilmeden bu soru bilinebiliyor mu?" Bu yüzden kopyadan
cevapla birlikte her senaryo izi de silinir — `script_id`, `turn_index`, `answer_point_id`,
`context_line`, `section`, `visual`. `context_line` (senaryonun bir cümlelik tanıtımı) okuma
tarafındaki `passage_title`ın karşılığıdır: konuyu ele verdiği için kopyaya girmez. Modelin
gördüğü tek şey yönergedir + soru kökü + seçenekler/gövde.

**2. Dosya adı çakışması ayrı araç gerektirdi.** Okuma ve dinlemede paket adları aynı
(`multiple-choice.json`, `matching.json`…). `tools/metinsiz-kopya.py` `skill != "reading"`
olan dosyaları bilerek atlar — bu, dinlemenin okumanın ölçüm altyapısını bozmaması için
vardır ve değiştirilmedi. Onun yerine yanına dinleme sürümleri yazıldı:
`tools/sessiz-kopya.py` (→ `dogrulama/sessiz/`, gitignore'da) ve `tools/sessiz-rapor.py`
(→ `content/DOGRULAMA/SESSIZ-*`). İkisi `skill != "listening"` olanı atlar; okumanın
`dogrulama/metinsiz/`, `kalibrasyon/metinsiz/`, `METINSIZ-*` dosyalarına ne okur ne yazar.

**3. Bazı tipler yapısal olarak tahmin edilemez.** Form/not/tablo tamamlamada cevap çoğu
zaman özel ad, sayı ya da saattir. Orada düşük parçasız-bilinme oranı **beklenir ve başarı
sayılmaz** — ölçünün asıl ilgilendiği yer çoktan seçmeli + eşleştirmedir, çünkü orada cevap
bir seçenek havuzundan gelir ve sızıntı seçeneğin sözünden okunabilir.
`plan-map-diagram-labelling` hiç ölçülmedi: görsel gerektirir, metin tabanlı ölçüm orada
kördür (okuma tarafındaki diyagram etiketleme kararının aynısı).

**4. Karşılaştırma tabanı yok.** Okuma raporundaki `RESMI_TABAN` resmî okuma örnek
sorularından ölçülmüştü; dinlemede böyle bir ölçüm hiç yapılmadı
(`denetim/DENETIM-RAPORU.md` §5, madde A3). Bu yüzden bu raporda tabanla karşılaştırma
yapılmaz ve uydurulmuş bir taban sayısı yazılmaz — oranlar kendi içinde, tip bazında okunur.

**Sayım (rule 1, yeniden sayıldı):** dinlemede 352 soru kalemi / **360 numaralı soru**
(aralıklı numaralar açılmış hâliyle) · alıştırma 120 numara, tam testler 240 numara
(L1–L6 × 40, `tools/dogrula.py` tam test bütünlüğü 6/6 TAM). Hiçbir soru silinmedi.

### Ölçüt

Bir soru **üç turun üçünde de** doğru bilinmişse "senaryosuz çözülebilir" sayılır; tek turda
tutturmak şanstır. İki ölçüt ayrı raporlanır: **K1** kelime düzeyi (birebir ya da
`accepted_variants`) ve **K3** anlam düzeyi (`OPUS5-E10` tanımı: kelime kelime tutturma değil,
anlamca bilme). Çoktan seçmeli ve eşleştirmede cevap bir harf olduğu için K1 = K3; K3 asıl
farkı tamamlama ailesinde yapacak (3. ve 4. çalıştırma).

---

## 1. çalıştırma — çoktan seçmeli (tek cevaplı) · 2026-08-08

**Kapsam:** 7 dosya (alıştırma + L1–L6), **37 tek cevaplı** soru. `multiple-choice.json`
içindeki 3 kalem "TWO letters" (çok cevaplı) olduğu için bu tura girmedi — onlar
`multiple-choice-multi` ile birlikte 2. çalıştırmada ölçülecek (`--secim=tek/cok` ayrımı
`select_count` ve aralıklı numaradan yapılıyor, cevap anahtarına bakılmadan).

| Ölçüt | Sonuç |
|---|---|
| Ölçülen soru | 37 |
| 3/3 turda senaryosuz bilinen (K1 = K3) | **25 (%67.6)** |
| Bunlardan dayanağı **anlamsal** olan (aşağı bak) | **21 (%56.8)** |

### Kararın dayanağı — 3/3 bilinen 25 sorunun dağılımı

| Dayanak | 3/3 bilinen | Bilinmeyen | Yorum |
|---|---|---|---|
| `option_wording` | 9 | 1 | Seçeneğin kendi sözü doğruyu işaretliyor: üç seçenekten biri kavramın tanımını yeniden söylüyor, diğer ikisi yüzeysel/ilgisiz kalıyor. **Asıl sızıntı burada.** |
| `general_knowledge` | 8 | 0 | Cevap dünya bilgisiyle biliniyor, sesi dinlemek gereksiz. Bir soruda seçenekler bir terimin ne yaptığını soruyor ve doğru seçenek terimin gerçek işlevi — ses olmadan da doğru. |
| `logic` | 3 | 3 | Seçenekler arası mantıksal ilişki (biri diğerini dışlıyor, biri nedensel olarak tek uyan). Yarı yarıya. |
| `number_guess` | 4 | 8 | Saat/fiyat/miktar seçimi. 12 soruda 4 tutturma ≈ üç seçenekli şans oranı (%33). **Sızıntı sayılmamalı** — aşağıdaki uyarıya bak. |
| `cross_question` | 1 | 0 | Bir sorunun kökü bir sonraki sorunun cevabını veriyor ("**yeni salon** kaç tezgâh alacak?" sorusu, "pazar nereye taşınıyor?" sorusunun cevabını söylüyor). Paket içi tutarlılık kusuru. |

### 🔴 Ölçütün bu turda ortaya çıkan zayıf noktası

"Üç turda aynı cevabı verdi" ölçütü, **kararlı ama şanslı** bir sezgiyi gerçek sızıntıdan
ayırmıyor. Model deterministik bir sezgi kullanıyorsa (ör. "üç sayı arasında ortadaki yuvarlak
olmayan değer seçilir") üç turda da aynı yanıtı verir; doğru çıkarsa 3/3 görünür, ama soru
sızdırmıyordur. Bu turda `number_guess` dayanaklı 12 sorudan 4'ü böyle: tutturma oranı
(%33) tam olarak şans oranı. Bu yüzden yukarıdaki tabloda iki sayı ayrı verildi:
**ham 25 (%67.6)** ve **dayanağı anlamsal olan 21 (%56.8)**. İşaretlemede (5. çalıştırma)
esas alınacak olan ikincisidir; `number_guess` 3/3'leri işaretlenmeyecek, ama listede
şeffaflık için duracak.

### Şimdilik ne yapıldı, ne yapılmadı

- Ölçüm yapıldı, ham veri `content/DOGRULAMA/SESSIZ-multiple-choice-tek.json` içinde
  (soru bazında kaç turda doğru + 3/3 listesi).
- **İşaretleme yapılmadı** — plana göre bütün paketlerin işaretlemesi 5. çalıştırmada,
  tek tip cümleyle, bir kerede yapılacak (E1'in dersi). Hiçbir soru silinmedi, tam
  testlerin soru sayısı değişmedi.
- Bu turda ses metnine, senaryo klasörüne ve cevap anahtarına hiç bakılmadı;
  `tools/_e8_sizinti_kontrol.py` kopyada yasaklı alan kalmadığını doğruladı (0 ağır hata).

🔴 Bu ölçüm bozuk soruyu bulur, zorluk ölçmez.

---

## 2. çalıştırma — çoktan seçmeli (çok cevaplı) + eşleştirme · 2026-08-08

`FABLE5-43`'ün ürettiği kalan iki aile. **Kapsam:** çok cevaplı çoktan seçmeli 8 kalem /
16 numara (`multiple-choice-multi` 5 kalem + L1/L2/L5 `multiple-choice.json` içindeki
"TWO letters" kalemleri 3 × 1) ve eşleştirme 43 kalem / 43 numara (alıştırma 10, L1 3,
L2 3, L3 8, L4 8, L5 3, L6 8). Toplam **51 kalem / 59 numara.** Ses metnine, senaryo
klasörüne ve cevap anahtarına yine hiç bakılmadı; `tools/_e8_sizinti_kontrol.py` her iki
kopya kümesinde **0 ağır hata** verdi.

| Paket | Ölçülen | 3/3 turda senaryosuz bilinen (K1 = K3) |
|---|---|---|
| `multiple-choice-cok` | 8 kalem | **7 (%87.5)** |
| `matching` | 43 kalem | **29 (%67.4)** |
| **Toplam** | **51 kalem** | **36 (%70.6)** |

Çoktan seçmeli ve eşleştirmede cevap bir harf olduğu için K1 = K3 (yöntem notundaki
beklentiyle aynı); K3 asıl farkı 3. ve 4. çalıştırmadaki tamamlama ailesinde yapacak.

### 1. çalıştırmanın açtığı zayıf noktaya cevap: dayanak çaprazı

1. çalıştırma "üç turda aynı cevap" ölçütünün **kararlı ama şanslı** sezgiyi gerçek
sızıntıdan ayırmadığını göstermişti. Bu turda karar dayanağı baştan iki sınıfa ayrılarak
kaydedildi ve çapraz `tools/_e8_dayanak_capraz.py` ile alındı:

- **anlamsal** — `option_wording`, `general_knowledge`, `logic`, `cross_question`
- **şansa açık** — `coin_flip` (iki seçenek aynı köke eşit uyuyor), `guess` (hiçbir
  dayanak yok), `number_guess`

| Dayanak | Kalem | 3/3 bilinen | Bilinmeyen |
|---|---|---|---|
| `option_wording` | 31 | **28** | 3 |
| `general_knowledge` | 5 | **5** | 0 |
| `logic` | 4 | 3 | 1 |
| `coin_flip` | 7 | **0** | 7 |
| `guess` | 3 | **0** | 3 |
| `number_guess` | 1 | **0** | 1 |

🔴 **Ayrım tam çıktı:** şansa açık işaretlenen 11 kalemin **hiçbiri** 3/3 tutmadı, 3/3
tutan 36 kalemin **hepsinin** dayanağı anlamsal. Yani bu iki ailede ham oran ile
anlamsal-dayanaklı oran aynı — 1. çalıştırmadaki `number_guess` gürültüsü burada yok.
İşaretleme (5. çalıştırma) bu 36 kalem üzerinden yapılabilir.

### Sızıntının mekanizması — eşleştirmede `option_wording` %89

Eşleştirmede `option_wording` dayanaklı 27 kalemin 24'ü (%89) senaryosuz bilindi. Mekanizma
tek ve tekrar eden: **kutudaki seçeneğin sözü, ait olduğu kökü kendi başına adlandırıyor.**
Örnekler (senaryo görülmeden, yalnız kutu + kök listesinden):

- "Taş ocağı atığından yapılmış" → yalnızca *toprak* kökü mümkün (L3 11).
- "Düzgün yürüyüş ayakkabısı gerektirir" → yalnızca bir *yürüyüş rotası* (L3 12).
- "Yeri kokusu için seçildi" → yalnızca *çiçek tezgâhı* (L6 12).
- "Esnaf araçlarına ayrılmış" → yalnızca *yükleme avlusu* (L6 13).
- "Alışverişçiler kendilerininkini getirmek zorunda" → yalnızca *poşetler* (L6 15).
- "Üç ayrı grafik tek grafiğe dönmeli" → "charts" sözü *grafikler* kökünü birebir söylüyor (L4 23).

Üç alt tür ayrıca kayda değer:

1. **Dilbilgisi sızıntısı.** Alıştırma 5: seçenek "**Two of them** look alike…" diyor;
   çoğul zamir çoğul kök gerektiriyor ve kutuda tek çoğul kök var (*çizgilerin renkleri*).
   Ses hiç gerekmiyor — seçeneğin dilbilgisi cevabı veriyor.
2. **Kutupsallık sızıntısı.** L3 14: kutudaki tek yasak cümlesi ("İzin verilmiyor")
   köklerdeki tek yasak-biçimli kökle ("geceleyin parkta araba bırakmak") eşleşiyor.
   Aynı desen çok cevaplı tarafta da var: L5 14-15 ve alıştırma 7-8 "visitors are **not
   allowed** to" diye soruyor, ama beş seçenekten yalnız ikisi gerçek hayatta
   yasaklanabilecek şey; kalan üçü etkinliğin tanıttığı imkânlar. Polarite tek başına
   cevabı veriyor.
3. **Alan bilgisi sızıntısı.** L6 26 ve alıştırma 9-10: sistematik derleme yöntemi
   ("full text available" filtresine karşı uyarı, aramayı kaydet + çalıştırma tarihini
   not et) ders kitabı bilgisi; seçeneğin sözü doğru yöntemi tekrar ediyor.
   Alıştırma 5-6'da seçenek D ("sıradan arabalar için gerekli") soru kökünün kendisiyle
   ("van izni") çelişerek eleniyor.

### Nerede sızıntı YOK — ölçümün karşı kutbu

Sızmayan 15 kalemin 11'i, seçeneğin sözünün kökü adlandırmadığı yerler (kalan 4'ünde
dayanağım anlamsaldı ama tutmadı — orada seçenek beni yanlış köke çekti):

- **Kişi–görüş eşleştirmesi** (L3 24-26 Tamsin/Corin, L6 24-26 Rhian/Tomas): hangi
  görüşü kimin söylediği senaryosuz bilinemez — üç turda üç farklı yanıt verdim. Bu
  tipin tasarımı **doğru**; kutu görüşleri taşıyor, kökler ise kişi adı, aralarında
  sözel köprü yok.
- **Birbirini dışlayan çiftler**: L6 14 otopark (ücretsiz süre uzadı ↔ artık daha pahalı),
  L4 14 üst kat (görevliler taşır ↔ hâlâ aydınlatma yok), L1 26 (iki konuşmacı katılır ↔
  beş dakikayla sınırlı). İki seçenek de aynı köke eşit uyuyor; ayrım ancak sesten gelir.
  **Sağlam soru tasarımının çalışan örneği bu.**
- Çok cevaplı tarafta yalnız alıştırma 1-2 (tur bilgisi: saat / buluşma yeri / süre /
  ücret) sızdırmadı; beş seçenek de bir turda söylenebilecek şeyler.

### Şimdilik ne yapıldı, ne yapılmadı

- Ölçüm yapıldı, ham veri `content/DOGRULAMA/SESSIZ-multiple-choice-cok.json` ve
  `content/DOGRULAMA/SESSIZ-matching.json` içinde; tur cevapları
  `kalibrasyon/sessiz/{multiple-choice-cok,matching}-tur{1,2,3}.json` (her kalemde
  `basis` + kısa gerekçe).
- **İşaretleme yapılmadı** — plana göre 5. çalıştırmada, tek tip cümleyle, bir kerede.
  Hiçbir soru silinmedi; `tools/dogrula.py` bu turda da 12 tam test 40/40, şema hatası 0,
  toplam 1310 soru, işaretli 116 (değişmedi).
- Yeni araç: `tools/_e8_dayanak_capraz.py` (yalnız sayı basar, cevap değeri basmaz).
  `metinsiz-*` araçlarına ve okumanın ölçüm dosyalarına dokunulmadı.

🔴 Bu ölçüm bozuk soruyu bulur, zorluk ölçmez.

---

## 3. çalıştırma — tamamlama ailesi A (form / not / tablo) · 2026-08-08

**Kapsam:** `form-completion` 40 kalem (L1, L3, L5, L6 × 10), `note-completion` 42 kalem
(alıştırma 15, L1 6, L2 5, L4 10, L6 6), `table-completion` 30 kalem (alıştırma 15, L2 10,
L5 5) — **112 kalem / 112 numara**, dinlemedeki bu üç tipin tamamı (yeniden sayıldı:
dinleme 352 kalem / 360 numara, aile A 112/112). Ses metnine, senaryo klasörüne ve cevap
anahtarına yine hiç bakılmadı.

**Bu ailede düşük oran beklenirdi ve düşük çıktı** — yöntem notunun 3. maddesi: cevap çoğu
zaman soyadı, telefon, fiyat, saat, tarih. Aşağıdaki sayılar bu yüzden **başarısızlık değil,
beklentinin doğrulanması**; ölçünün asıl bulgusu tabloda değil, altındaki iki başlıkta.

| Paket | Ölçülen | K1 (kelime) | K3 (anlam) | Ölçüm dışı |
|---|---|---|---|---|
| `form-completion` | 40 kalem | 5 (%12.5) | **5 (%12.5)** | 0 |
| `note-completion` | 40 kalem | 9 (%22.5) | **10 (%25.0)** | 2 |
| `table-completion` | 29 kalem | 4 (%13.8) | **4 (%13.8)** | 1 |
| **Toplam** | **109 kalem** | **18 (%16.5)** | **19 (%17.4)** | **3** |

Karşılaştırma için: 1. çalıştırma (çoktan seçmeli tek) %67.6, 2. çalıştırma (çok cevaplı +
eşleştirme) %70.6. Aradaki dört kat fark, yöntem notundaki ayrımın ölçümle doğrulanmış hâli.

### K3 ilk kez K1'den ayrıldı — ve ayrımı script yaptı

1. ve 2. çalıştırmada cevap harf olduğu için K1 = K3'tü. Burada ayrım anlamlı hâle geliyor:
`L4-note-7`'de üç turun ikisinde "charity shop", birinde "charity" yazdım — K1'de üç turu
tutturamıyor, K3'te aynı şeyi söylüyor. Tek fark bu (18 → 19).

Bu kararı **ölçümü yapan model veremez**: anlamca eşitliğe bakmak cevap anahtarını görmeyi
gerektirir, o da ölçümü bitirir. Bu yüzden `tools/_e8_anlam_esle.py` yazıldı — anahtarı
yalnız script okuyor, dışarı **sayı** basıyor, tur dosyalarına `anlam: true/false` yazıyor.
Eşleşme kuralı bilerek dar: küçük harf + noktalama/para sadeleştirmesi, baş takı (`a/an/the`)
atma, yirmiye kadar sayı sözcüğü ↔ rakam, `per cent` → `%`, çoğul `-s`, ve biri diğerinin
**sözcük düzeyinde alt dizisi** olması. Geniş bir eşleştirici sızıntıyı olduğundan büyük
gösterirdi.

### 🔴 Asıl bulgu: alıştırma paketleri tam testlerle aynı senaryoları kullanıyor

Aile A'da sızıntının en güçlü kanalı seçenek sözü değil (zaten seçenek yok), **paketler arası
çapraz**. Alıştırma `note-completion` dört bloğu ve alıştırma `table-completion` dört bloğu,
tam testlerdeki sekiz senaryonun aynısını kullanıyor. Bir aday (ya da model) iki dosyayı yan
yana koyduğunda, birinin boşluğunu diğerinin **düz metni** dolduruyor:

- `L1-note-31` "19. yüzyıl yasaları bahçesi olmayan hanelere (31) sağlamaya zorladı" →
  alıştırma tablo 9 aynı şeyi boşluksuz yazıyor: "**bahçesi olmayan haneler için kiralık
  parseller** …". 3/3 bilindi.
- `L1-note-32` "(32) — en yaygını, kimsenin işine yaramayan zeminde" → alıştırma tablo 10
  üç biçimi sırayla sayıyor: "**topluluk bahçeleri**, çatı çiftlikleri ve (10) tarım". 3/3.
- Aynı satır ters yönde de sızdırıyor: alıştırma tablo 10'un boşluğunu `L1-note` "lambayla
  aydınlatılan bir iç mekân çiftliği" satırı + tablonun kendi notu ("raflarda, kapalı
  alanda, lamba altında") veriyor → *dikey*. 3/3.
- `L5-form-8` "Sürücünün getirmesi gereken: bir (8)" → alıştırma not bloğu düpedüz yazıyor:
  "kasklar dağıtılıyor **ama sürücülerin kendi su şişesi** gerekiyor". 3/3.

Bu, 2. çalıştırmadaki `cross_question`ın aynısı ama **dosya sınırını aşan** hâli: orada bir
sorunun kökü komşu sorunun cevabını veriyordu, burada alıştırma paketi tam testin cevabını
veriyor. Alıştırma paketi tam testten önce çalışılacağı için pratikte tam testin dört sorusu
önceden görülmüş oluyor. **Paket içi tutarlılık kusuru değil, paketler arası kusur.**

### İkinci mekanizma: çerçevenin kendi sözü (`frame_wording`)

Çoktan seçmelideki `option_wording`in tamamlamadaki karşılığı: seçenek yok, ama form/not
çerçevesinin sözü tek doldurmayı bırakıyor. 19 kalem böyle işaretlendi, 8'i 3/3 bilindi:

- `L3-form-6` "İptal için: merkeze bir ay önceden (6) bildirin" → *yazılı olarak*. Deyimin
  kendisi cevabı söylüyor; ses gereksiz.
- `L3-form-9` "Dersler: internetten ya da uygulamadan — (9) ile değil" → *telefon*.
  Çerçeve iki kanalı sayıp üçüncüyü dışlıyor; dışlanan kanal tek.
- `L4-note-9` "ad kanıtı, örn. ehliyet ya da bir (9)" → *pasaport*.
- `L2-note-38` "kanalların birkaç yılda bir (38) kazınması gerekiyordu" → *çamur/mil*.
- `L6-form-5` "Cadnam House: daha büyük mutfaklar; her oda (5)" → karşı satır Wharton'ı
  "mutfağı beş kişiyle paylaşılan" diye tanımlıyor; kalan tek ayrım *banyolu (en-suite)*.
- `L6-note-33` "olumsuz sürüm ertesi ay (33) sayısını neredeyse iki katına çıkardı" →
  *şikâyet*. `L6-note-35/36` (erteleme · bir sonraki zam) ise alan bilgisiyle biliniyor.

**Dilbilgisi sızıntısı burada da var** (2. çalıştırmadaki alıştırma 5'in akrabası):
`L2-note-40` "artık bir (40) getirmiyordu" cümlesindeki **"an"**, boşluğu ünlüyle başlayan
sözcüğe kilitliyor; anlamla birleşince tek aday kalıyor. Bu yüzden ayrı bir dayanak adı
açıldı: `grammar_cue`.

### Dayanak çaprazı — 2. çalıştırmanın ayrımı burada da tuttu

`tools/_e8_dayanak_capraz.py`, iki yeni dayanakla (`frame_wording`, `grammar_cue` anlamsal
tarafa; `name_guess` şansa açık tarafa) güncellendi.

| Dayanak | Kalem | 3/3 bilinen | Bilinmeyen |
|---|---|---|---|
| `cross_question` | 5 | **4** | 1 |
| `frame_wording` | 19 | **8** | 11 |
| `general_knowledge` | 20 | **6** | 14 |
| `grammar_cue` | 1 | **1** | 0 |
| `logic` | 5 | 0 | 5 |
| `guess` | 14 | **0** | 14 |
| `name_guess` | 9 | **0** | 9 |
| `number_guess` | 37 | **0** | 37 |

🔴 Ayrım yine tam: şansa açık işaretlenen **60 kalemin hiçbiri** 3/3 tutmadı; 3/3 tutan 19
kalemin **hepsinin** dayanağı anlamsal. Yani ham oran = anlamsal-dayanaklı oran (%17.4),
1. çalıştırmadaki `number_guess` gürültüsü bu ailede de yok. Soyadı, cep telefonu, fiyat,
saat ve tarih soran 60 kalemde parçasız bilinme **sıfır** — bu tipler için beklenen ve
doğru olan sonuç.

### 🔴 Ölçüm aracının kendisi üç kalemi kirletti

`tools/_e8_sizinti_kontrol.py` "gövdede birebir geçen cevap dizgisi: N" uyarısı veriyor.
Uyarının nerede olduğunu görmek için `tools/_e8_govde_cakismasi.py` yazıldı; alan **yolunu**
bastı (değeri değil), ama not iskeleti kısa olduğu için yol tek başına cevabı ölçümü yapan
model açısından daralttı. Etkilenen üç kalem — `L1-note-34`, `L1-note-35`, `L2-table-5` —
`haric: true` ile **ölçüm dışı** bırakıldı: kirlenmiş ölçüm, ölçüm değildir. Soruların
kendisine dokunulmadı, dosyalarında duruyorlar.

Üçünde de çakışma **rastlantısal**: cevap sözcüğü sayfanın başka bir yerinde (başka bir
satırda, başka bir sütunda) geçen bir sözcüğün içinde kalıyor — kâğıda bakan aday bundan
cevabı çıkaramaz. Yani bunlar gerçek sızıntı değil, alt dizi eşleşmesinin yan ürünü.

Araç tarafında düzeltildi: `_e8_govde_cakismasi.py` artık ayrıntıyı ekrana değil
`dogrulama/sessiz-tani.txt`e (gitignore'da) yazıyor, ekrana yalnız sayı geliyor;
`_e8_sizinti_kontrol.py`nin başına da bu uyarının ağır hata olmadığı ve ayrıntısının ölçümü
yapan modele gösterilmemesi gerektiği yazıldı. `sessiz-rapor.py` `haric` alanını tanıyor ve
ölçüm dışı kalemi ayrıca raporluyor (geriye dönük uyumlu: 1. ve 2. çalıştırmanın tur
dosyalarında bu alan yok, çıktıları değişmez).

### Şimdilik ne yapıldı, ne yapılmadı

- Ölçüm yapıldı; ham veri `content/DOGRULAMA/SESSIZ-{form,note,table}-completion.json`,
  tur cevapları `kalibrasyon/sessiz/{form,note,table}-completion-tur{1,2,3}.json`
  (her kalemde `basis` + `anlam`), turlar `tools/_e8_tamamlama_turlar.py` tablosundan üretildi.
- **İşaretleme yapılmadı** — plana göre 5. çalıştırmada, tek tip cümleyle, bir kerede.
  İşaretlemeye aday 19 kalemin listesi JSON'ların `uc_turda_bilinen_k3` alanında.
- Hiçbir soru silinmedi; `tools/dogrula.py` bu turda da 12 tam test 40/40, şema hatası 0,
  toplam 1310 soru, işaretli 116 (değişmedi).
- `metinsiz-*` araçlarına ve okumanın ölçüm dosyalarına dokunulmadı.
- Kalan: 4. çalıştırma (cümle/özet/akış/kısa cevap), 5. çalıştırma (toplu rapor +
  işaretleme). `plan-map-diagram-labelling` (45 kalem) **ölçülmeyecek** — görsel gerekir.

🔴 Bu ölçüm bozuk soruyu bulur, zorluk ölçmez.
