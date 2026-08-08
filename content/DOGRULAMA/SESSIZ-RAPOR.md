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

---

## 4. çalıştırma — tamamlama ailesi B (cümle / özet / akış / kısa cevap) · 2026-08-08

**Kapsam:** `sentence-completion` 39 kalem (alıştırma 15, L1–L6 × 4), `summary-completion`
15 kalem (L3 6, L5 5, L6 4), `flow-chart-completion` 25 kalem (alıştırma 15, L2 5, L4 5),
`short-answer` 28 kalem (alıştırma 15, L1 4, L3 4, L4 5) — **107 kalem / 107 numara**,
dinlemedeki bu dört tipin tamamı. Ses metnine, senaryo klasörüne ve cevap anahtarına yine
hiç bakılmadı; `tools/_e8_sizinti_kontrol.py` **0 ağır hata** verdi.

**Sayım yeniden yapıldı (rule 1):** dinleme 352 kalem / 360 numara; tip bazında
akış 25, form 40, eşleştirme 43, çoktan seçmeli 40 (43 numara), çok cevaplı 5 (10 numara),
not 42, plan/harita/diyagram 45, cümle 39, kısa cevap 28, özet 15, tablo 30.
**Bu çalıştırmayla birlikte 1–4. turlarda ölçülen: 307 kalem** — ölçülmeden kalan tek tip
`plan-map-diagram-labelling` (45 kalem), o da bilerek: görsel gerektirir, metin tabanlı
ölçüm orada kördür.

| Paket | Ölçülen | K1 (kelime) | K3 (anlam) | Ölçüm dışı |
|---|---|---|---|---|
| `sentence-completion` | 39 kalem | 6 (%15.4) | **8 (%20.5)** | 0 |
| `summary-completion` | 15 kalem | 9 (%60.0) | **9 (%60.0)** | 0 |
| `flow-chart-completion` | 25 kalem | 13 (%52.0) | **13 (%52.0)** | 0 |
| `short-answer` | 28 kalem | 13 (%46.4) | **15 (%53.6)** | 0 |
| **Toplam** | **107 kalem** | **41 (%38.3)** | **45 (%42.1)** | **0** |

### 🔴 Asıl bulgu: "tamamlama ailesi" tek bir aile değil — ikiye ayrılıyor

3. çalıştırmanın sonucu (aile A: %17.4) "tamamlama tipleri sızdırmaz" diye okunabilirdi.
Bu tur o okumayı çürütüyor. Aile B'nin dört paketi **iki ayrı gruba** düşüyor:

- **`sentence-completion` %20.5** — aile A ile aynı yerde. Sebebi de aynı: boşluklar
  ders yönetimiyle ilgili **tikel** bilgiler (kaç kelime, hangi gün, hangi oda, kaç dakika).
  39 kalemin 20'si sayı/ad/gün tahmini; hiçbiri tutmadı.
- **`summary-completion` %60.0, `short-answer` %53.6, `flow-chart-completion` %52.0** —
  çoktan seçmeli (%67.6) ve eşleştirmenin (%70.6) yanında. Sebebi tek: bu üç pakette
  boşluğa düşen sözcük çoğu zaman **alanın ders kitabı terimi**, konuşmanın seçtiği bir
  değer değil.

Ayrımı sayıyla söyleyen dayanak `general_knowledge`:

| | Kalem | 3/3 bilinen | Oran |
|---|---|---|---|
| Aile A (form/not/tablo, 3. çalıştırma) | 20 | 6 | %30 |
| Aile B (bu tur) | 45 | 26 | **%58** |

Aile B'de dünya bilgisiyle bilinen 26 kalem şunlar gibi: canlıların kaplaması =
*biofouling*, kurutulup dondurulabilen tohum = *orthodox*, desibelin ölçeği =
*logaritmik*, trafik iki katına çıkınca artış = *3 dB*, sıvı azotta = *−196*,
denizde kaybolan takım = *ghost gear*, tohum bankası sıcaklığı = *−20*, ilk plastik
tabakası = *1950'ler*, 40 km/s üstünde gürültünün kaynağı = *lastikler*. Bu sorularda
**ses kaydı süs**: aday senaryoyu hiç duymadan doğru yazıyor.

### İkinci mekanizma — çapraz sızıntı artık dört yönlü (`cross_question` 5/5)

3. çalıştırma alıştırma not/tablo paketlerinin tam testlerle **aynı senaryoları**
kullandığını bulmuştu. Bu turda aynı kusur **paket tipleri arasında** da çıktı ve
işaretlenen 5 kalemin **beşi de** 3/3 bilindi. Birinin boşluğunu diğerinin düz metni
dolduruyor:

- `L3-summary-34` "mühürlendikten sonra, hangi (34) iyi olduğu kavanozdan önemli" →
  alıştırma akış şeması *SEALING AND FREEZING* adımı aynı cümleyi boşluksuz yazıyor:
  "The quality of the **seal** counts for more than the jar itself."
- `practice-flow-6` "gün ışığı ve su hareketi polimeri (6) yapar" → `L5-summary`
  gövdesi: "leave the polymer **brittle** enough to break apart."
- `practice-flow-12` "sıcak bir gecede (12) yeniden açılır" → `L4-flow-40`:
  "the moment a **window** is opened."
- `practice-flow-14` "gazetelerin yazdığı on beş puanlık artış tek bir (14) dayanıyor" →
  `L6-summary` gövdesi: "the figure the papers carried came from one **pilot** in a
  single town."
- `practice-short-15` "miktar ne sıklıkla ikiye katlandı?" → `L5-summary` gövdesi:
  "the amount has roughly doubled **every fifteen years** since."

Yani sekiz dinleme senaryosu bütün dinleme bacağında yeniden kullanılıyor ve bir pakette
**boşluk** olan şey başka bir pakette **düz metin** olarak duruyor. Alıştırma paketi tam
testten önce çalışılacağı için bu, tam testin sorusunu önceden görmek demek.

### Üçüncü mekanizma — çerçevenin kendi sözü, bir kez de kendi başlığı

`frame_wording` 15 kalemin 8'i. En temiz örnek **şemanın kendi başlığını ele vermesi**:

- `L4-flow-36` "at the source → along the path → at the (36)" — aynı akış şemasının
  birkaç satır aşağıdaki başlığı *AT THE RECEIVER* diye yazıyor. Soru kendi cevabını
  sayfanın içinde basıyor; sesin hiçbir katkısı yok.
- `L5-sentence-28` "ne tablolar ne anket kelime sayısına girer, çünkü ikisi de (28)
  içindedir" → *ek (appendix)*; `L5-sentence-30` "pilot uygulamadan **önce** gönderilecek
  olan (30)" → pilotlanan şey anketin kendisi.
- `practice-short-2` "hangi biçim **var olan bir binanın üstüne** kurulur?" → sorunun
  kendi tanımı *çatı çiftliği* diyor. `practice-short-11` "duvarın trafikle dinleyici
  arasında neyi kesmesi gerekir?" → *görüş hattı*; alıştırma akış şeması ayrıca
  "tekerlekleri görüşten gizleyecek yere konur" diye tekrarlıyor.
- `practice-flow-15` "örneklemler (15) binleri buluyor" → *yüz*. Eşdizim boşluğu:
  İngilizcede "___ of thousands" kalıbının tek doğal doldurması var.

**Dilbilgisi sızıntısı (`grammar_cue`) 2/2:** `practice-sentence-6` "artık bir **an** (6)
olarak veriliyor" ve `L2-sentence-27` "her ölçüm bir **an** (27) içine konur, kelime
sayısına girmez". İkisinde de *an* boşluğu ünlüyle başlayan sözcüğe kilitliyor, "kelime
sayısı dışında kalır" çerçevesi de tek adayı bırakıyor: *appendix*. 3. çalıştırmadaki
`L2-note-40`'ın aynısı — desen tekrar ediyor.

### Dayanak çaprazı — ayrım dördüncü kez de tam

| Dayanak | Kalem | 3/3 bilinen | Bilinmeyen |
|---|---|---|---|
| `cross_question` | 5 | **5** | 0 |
| `grammar_cue` | 2 | **2** | 0 |
| `general_knowledge` | 45 | **26** | 19 |
| `frame_wording` | 15 | **8** | 7 |
| `logic` | 6 | **4** | 2 |
| `guess` | 10 | **0** | 10 |
| `number_guess` | 24 | **0** | 24 |

🔴 Şansa açık işaretlenen **34 kalemin hiçbiri** 3/3 tutmadı; 3/3 tutan 45 kalemin
**hepsinin** dayanağı anlamsal. Ham oran = anlamsal-dayanaklı oran (%42.1). Ayrım
1. çalıştırmadan beri dördüncü kez aynı yönde çıkıyor — ölçüt, kararlı-ama-şanslı
sezgiyi bu ailede de üretmedi.

### K3, K1'den dört kalemde ayrıldı

3. çalıştırmada ayrım tek kalemdeydi, burada dört: `practice-sentence-2`,
`L5-sentence-30`, `practice-short-2`, `practice-short-14`. Dördünde de anlam aynı,
sözcük sayısı/eki farklı — kararı yine `tools/_e8_anlam_esle.py` verdi (anahtarı yalnız
script okur, dışarı sayı basar). Ters yön yok: K1'de tutup K3'te düşen kalem **0**.

### Ölçüm aracı bu turda kimseyi kirletmedi

`_e8_sizinti_kontrol.py` dört dosyada "gövdede birebir geçen cevap dizgisi: 1" uyarısı
verdi (alıştırma akış + alıştırma cümle + `L3-summary` + `L4-flow`). 3. çalıştırmanın
dersi gereği bu turda `_e8_govde_cakismasi.py` **hiç çalıştırılmadı** — kirlenme oradan
gelmişti. Uyarı dosya başına yalnız bir **sayı** basıyor, hangi kalem olduğunu
söylemiyor; 15–25 kalemlik bir dosyada tek kalemi daraltmaya yetmez. Bu yüzden bu turda
`haric` işaretli kalem **yok**, 107 kalemin hepsi orana girdi. `L4-flow`'daki uyarının
36. soru olduğu neredeyse kesin — ama onu araç değil, kopyanın kendisi söylüyor
(*AT THE RECEIVER* başlığı sayfada duruyor); orası araç kirlenmesi değil, **gerçek soru
kusuru**.

### Sızıntının olmadığı yer — ölçümün karşı kutbu

Sızmayan 62 kalemin 34'ü sayı/ad/gün tahmini, kalan 28'inde dayanağım anlamsaldı ama
tutmadı. Doğru tasarlanmış boşluğun tarifi bu kalemlerden çıkıyor: **cevap, konuşmanın
seçtiği bir değer olmalı, alanın ders kitabı terimi değil.** Çalışan örnekler:
`L6-summary-37` (büyük denemelerin bulduğu puan artışı — literatürde tek bir sayı yok),
`L2-flow-34` (yolda kaybedilen yüzde), `L4-flow-39` (ağaç şeridinin kaç metre olması
gerektiği), `practice-flow-4` (yedek örneğin nereye gittiği), `practice-flow-9`
(gürültü haritasına giren zemin değişkeni). Bunların hepsinde üç turda üç farklı yanıt
verdim: senaryo olmadan bilinmiyorlar, olmaları gerektiği gibi.

### Şimdilik ne yapıldı, ne yapılmadı

- Ölçüm yapıldı; ham veri `content/DOGRULAMA/SESSIZ-{sentence,summary,flow-chart}-completion.json`
  ve `SESSIZ-short-answer.json`, tur cevapları
  `kalibrasyon/sessiz/<paket>-tur{1,2,3}.json` (her kalemde `basis` + `anlam`), turlar
  `tools/_e8_tamamlama_b_turlar.py` tablosundan üretildi (aile A'daki
  `_e8_tamamlama_turlar.py`nin kardeşi, aynı biçim ve aynı dayanak sınıfı).
- **İşaretleme yapılmadı** — plana göre 5. çalıştırmada, tek tip cümleyle, bir kerede.
  Bu turdan işaretlemeye aday 45 kalemin listesi JSON'ların `uc_turda_bilinen_k3`
  alanında. 1–4. çalıştırmanın toplamı: ham 3/3 **125 kalem** (25 + 36 + 19 + 45),
  bunların dayanağı anlamsal olanı **121 kalem** — aradaki 4 kalem 1. çalıştırmanın
  `number_guess` 3/3'leri, plana göre işaretlenmeyecek ama listede şeffaflık için
  duracak. Kesin liste 5. çalıştırmada JSON'lardan birleştirilecek.
- Hiçbir soru silinmedi; `tools/dogrula.py` bu turda da 12 tam test 40/40, şema hatası 0,
  toplam 1310 soru, işaretli 116 (değişmedi).
- `metinsiz-*` araçlarına ve okumanın ölçüm dosyalarına dokunulmadı.
- Kalan: 5. çalıştırma (toplu rapor + işaretleme).

🔴 Bu ölçüm bozuk soruyu bulur, zorluk ölçmez.

---

## 5. çalıştırma — toplu rapor + işaretleme · 2026-08-08

Ölçüm bitti; bu tur yeni tur çözmüyor, dört turun sonucunu tek tabloda toplayıp
soru dosyalarına işliyor. Ham veri `content/DOGRULAMA/SESSIZ-TOPLU.json`
(`tools/_e8_toplu.py --json` ile üretildi; kaynağı yalnız önceki turların kendi
çıktıları — senaryo ve cevap anahtarı bu turda da açılmadı).

### Sayım (rule 1, son kez yeniden sayıldı)

`tools/sessiz-kopya.py` on paketi birden kopyaladığında **44 dosya, 307 kalem,
315 numara** çıkıyor. Buna ölçülmeyen `plan-map-diagram-labelling` 45 kalem
eklenince dinlemenin tamamı **352 kalem / 360 numara** — 360 hedefi tutuyor.
307 kalemin 3'ü ölçüm dışı bırakıldığı için **oranların paydası 304**.
`tools/dogrula.py`: 12 tam test 40/40, şema hatası 0, toplam 1310 soru.

### Paket bazında ve toplu oran

Ölçüt **K3 anlam düzeyi** (`OPUS5-E10` tanımı: kelime kelime tutturma değil,
anlamca bilme). K1 (kelime düzeyi) karşılaştırma için yanında duruyor. Bir
kalem, üç turun üçünde de doğru bilinmişse "senaryosuz çözülebilir" sayılır.

| Paket | Çalıştırma | Ölçülen | K1 | K3 | K3 oranı | Dayanağı anlamsal |
|---|---|---|---|---|---|---|
| `multiple-choice-cok` | 2 | 8 | 7 | 7 | **%87.5** | 7 |
| `multiple-choice-tek` | 1 | 37 | 25 | 25 | **%67.6** | 21 |
| `matching` | 2 | 43 | 29 | 29 | **%67.4** | 29 |
| `summary-completion` | 4 | 15 | 9 | 9 | **%60.0** | 9 |
| `short-answer` | 4 | 28 | 13 | 15 | **%53.6** | 15 |
| `flow-chart-completion` | 4 | 25 | 13 | 13 | **%52.0** | 13 |
| `note-completion` | 3 | 40 | 9 | 10 | **%25.0** | 10 |
| `sentence-completion` | 4 | 39 | 6 | 8 | **%20.5** | 8 |
| `table-completion` | 3 | 29 | 4 | 4 | **%13.8** | 4 |
| `form-completion` | 3 | 40 | 5 | 5 | **%12.5** | 5 |
| **Toplam** | 1–4 | **304** | **120 (%39.5)** | **125 (%41.1)** | | **121 (%39.8)** |

Aile bazında toplanınca ölçümün tek cümlelik sonucu görünüyor:

| Aile | Ölçülen | 3/3 bilinen (K3) | Oran |
|---|---|---|---|
| Seçenekli tipler (çoktan seçmeli tek + çok + eşleştirme) | 88 | 61 | **%69.3** |
| Tamamlama ailesi B (özet / akış / kısa cevap / cümle) | 107 | 45 | **%42.1** |
| Tamamlama ailesi A (form / not / tablo) | 109 | 19 | **%17.4** |
| `plan-map-diagram-labelling` | 45 | — | **ölçülmedi** |

🔴 **`plan-map-diagram-labelling` ölçülmedi.** Görsel gerektirir; metin tabanlı
ölçüm orada kördür. Bu, okuma tarafındaki diyagram etiketleme kararının aynısıdır
ve bir eksiklik değil, kapsam sınırıdır — o 45 kalem işaretlenmedi, dokunulmadı.

### 🔴 Düşük oran her yerde iyi haber değil, bazı yerlerde beklenen sonuç

Yöntem notunun 3. maddesi ölçümle doğrulandı: form / not / tablo tamamlamada cevap
çoğu zaman soyadı, cep telefonu, fiyat, saat, tarih — **yapısal olarak tahmin
edilemez.** Oradaki %12–25, soruların iyi tasarlandığının kanıtı değil; ölçünün
o tipte zaten bir şey söyleyemediğinin kanıtı. Dört turun dayanak çaprazı bunu
sayıyla gösteriyor (`tools/_e8_dayanak_toplu.py`):

| Dayanak | Kalem | 3/3 bilinen | Sınıf |
|---|---|---|---|
| `general_knowledge` | 78 | 45 | anlamsal |
| `number_guess` | 74 | **4** | şansa açık |
| `option_wording` | 41 | 37 | anlamsal |
| `frame_wording` | 34 | 16 | anlamsal |
| `guess` | 27 | **0** | şansa açık |
| `logic` | 20 | 10 | anlamsal |
| `cross_question` | 11 | 10 | anlamsal |
| `name_guess` | 9 | **0** | şansa açık |
| `coin_flip` | 7 | **0** | şansa açık |
| `grammar_cue` | 3 | 3 | anlamsal |
| **anlamsal** | **187** | **121** | |
| **şansa açık** | **117** | **4** | |

Soyadı, telefon, fiyat, saat ve tarih soran **117 kalemin yalnız 4'ü** 3/3
tuttu — o dördü de 1. çalıştırmadaki üç seçenekli şans oranı kadar (aşağıya bak).

Bu yüzden ölçünün asıl ilgilendiği yer seçenekli tiplerdir: cevap bir seçenek
havuzundan geldiği için sızıntı seçeneğin sözünden okunabilir, ve orada oran
**%69.3.** İkinci sırada tamamlama ailesi B var (%42.1) — orada da boşluğa
düşen sözcük çoğu zaman alanın ders kitabı terimi.

### İşaretleme

`tools/_e8_isaretle.py` (`_b1_isaretle.py`nin dinleme sürümü; okuma dosyalarına
dokunmaz, `skill != "listening"` olanı atlar) şunu yazdı:

| Ne | Kaç kalem | Yazılan |
|---|---|---|
| 3/3 bilinen, dayanağı anlamsal | **121** | `blind_solvable` · `blind_basis` · `status: "flagged"` · `flag_reason` · `flag_mechanism` |
| 3/3 bilinen, dayanağı şansa açık | 4 | `blind_solvable: true` + `blind_note`; **işaretlenmedi** |
| Ölçüm aracının kirlettiği | 3 | yalnız `blind_note` |
| Geri kalan | 179 | `blind_solvable: false` |

Depo genelinde işaretli soru sayısı **116 → 237.** Hiçbir soru silinmedi, hiçbir
sorunun metni ya da cevabı değiştirilmedi, tam testler 40/40 kaldı.

**İşaretlenmeyen 4 kalem** (`L1-multiple-choice-11`, `L2-multiple-choice-11`,
`L2-multiple-choice-13`, `L6-multiple-choice-21`) 1. çalıştırmanın kararıyla
dışarıda: üçü de saat/fiyat/miktar seçimiydi, `number_guess` dayanaklı 12
kalemde 4 tutturma tam olarak üç seçenekli şans oranı (%33). Kararlı ama şanslı
bir sezgi sızıntı değildir. Şeffaflık için dosyada `blind_solvable: true` +
`blind_note` ile duruyorlar; `status` değişmedi.

**Ölçüm dışı 3 kalem** (`L1-note-completion-34`, `L1-note-completion-35`,
`L2-table-completion-5`) 3. çalıştırmada ölçüm aracının kendisi tarafından
kirletilmişti; kirlenmiş ölçüm ölçüm olmadığı için ne işaretlendiler ne de
`blind_solvable: false` aldılar — yalnız `blind_note` taşıyorlar.

### 🔴 `flag_reason` — E1'in dersi baştan uygulandı

Denetim raporunun bulgusu (`denetim/DENETIM-RAPORU.md` §5, madde A2), 180 okuma
sorusunun hepsine **aynı** cümlenin yazılmış olmasıydı. Burada 121 kalemin
121 ayrı gerekçesi var; her biri o sorunun kendi kökünü, seçeneğini ya da
çerçevesini adıyla anıyor. Tablo `tools/_e8_isaret_tablosu.py` içinde, elle
yazıldı. Biçim tek tip, içerik değil:

> `"Senaryo gösterilmeden 3/3 turda doğru bilindi: <bu soruya özel somut sebep>."`

Gerekçeler yazılırken de senaryo ve cevap anahtarı açılmadı. Kullanılan iki
kaynak: (a) `dogrulama/sessiz/` altındaki kör kopya (senaryo ve cevap zaten
silinmiş), (b) modelin turlarda kendi verdiği cevap — kalemler 3/3 doğru
bilindiği için verilen cevap zaten doğru cevap. Yardımcı
`tools/_e8_gerekce_taslak.py` yalnız bu ikisini birleştirip basıyor.

### `flag_mechanism` — okumanın sözlüğü + dinlemeye özgü üç ad

Okuma tarafında kullanılan adlar korundu (`genel_kultur`, `kip_imzasi`,
`esdizim_kilidi`, `konumsal_duzen`); dinlemede karşılığı olmayan üç mekanizma
için yeni ad açıldı:

- **`secenek_sozu`** — kutudaki/şıktaki seçeneğin kendi sözü ait olduğu kökü
  adlandırıyor. Dinlemenin baskın sızıntısı, eşleştirmede neredeyse tek
  mekanizma (29 kalemin 22'si).
- **`cerceve_sozu`** — `secenek_sozu`nun tamamlamadaki karşılığı: seçenek yok,
  ama form/not/cümle çerçevesinin sözü tek doldurmayı bırakıyor.
- **`capraz_sizinti`** — başka bir soru ya da başka bir **paket** aynı bilgiyi
  düz metin yazıyor. Bu adın açılması gerekti çünkü okumada karşılığı yoktu.

| Soru tipi | capraz_sizinti | cerceve_sozu | esdizim_kilidi | genel_kultur | kip_imzasi | konumsal_duzen | secenek_sozu | Toplam |
|---|---|---|---|---|---|---|---|---|
| `flow_chart_completion` | 3 | 1 | 0 | 6 | 0 | 3 | 0 | **13** |
| `form_completion` | 1 | 2 | 1 | 1 | 0 | 0 | 0 | **5** |
| `matching` | 0 | 0 | 1 | 2 | 1 | 3 | 22 | **29** |
| `multiple_choice` | 1 | 0 | 0 | 8 | 1 | 4 | 10 | **24** |
| `multiple_choice_multi` | 0 | 0 | 0 | 1 | 1 | 0 | 2 | **4** |
| `note_completion` | 2 | 4 | 1 | 3 | 0 | 0 | 0 | **10** |
| `sentence_completion` | 0 | 4 | 2 | 1 | 0 | 1 | 0 | **8** |
| `short_answer` | 1 | 2 | 0 | 12 | 0 | 0 | 0 | **15** |
| `summary_completion` | 1 | 1 | 0 | 7 | 0 | 0 | 0 | **9** |
| `table_completion` | 1 | 1 | 0 | 2 | 0 | 0 | 0 | **4** |
| **Toplam** | **10** | **15** | **5** | **43** | **3** | **11** | **34** | **121** |

Tabloda dinlemenin iki deseni net duruyor: **seçenekli tipler `secenek_sozu`
taşıyor** (34 kalemin 34'ü orada), **tamamlama ailesi ise `genel_kultur`**
(43 kalemin 32'si tamamlama tiplerinde). Yani dinlemenin iki ayrı hastalığı var
ve ikisinin tedavisi ayrı: seçenekli tipte seçeneğin sözü yeniden yazılmalı,
tamamlamada boşluğa düşen sözcük alanın ders kitabı terimi olmaktan çıkarılmalı.

### Dört turdan çıkan üç yapısal bulgu

1. **`capraz_sizinti` bir soru kusuru değil, paket mimarisi kusuru (10 kalem).**
   Sekiz dinleme senaryosu bütün dinleme bacağında yeniden kullanılıyor; bir
   pakette **boşluk** olan şey başka bir pakette **düz metin** olarak duruyor.
   Alıştırma paketleri tam testlerden önce çalışılacağı için pratikte tam testin
   sorusu önceden görülmüş oluyor. `cross_question` dayanaklı **11 kalemin
   10'u** 3/3 bilindi (%91) — ölçümdeki en yüksek isabetli dayanak bu.
2. **Dayanak ayrımı dört turda da tam çıktı.** Turlarda "şansa açık" işaretlenen
   117 kalemden 3/3 tutan yalnız 4 tane (hepsi 1. çalıştırmada, hepsi şans
   oranında); 3/3 tutan 125 kalemin 121'inin dayanağı anlamsal. Yani "üç turda
   aynı cevap" ölçütü, 1. çalıştırmada korkulanın aksine kararlı-ama-şanslı
   sezgiyi sistematik olarak üretmedi.
3. **Sağlam soru tasarımının tarifi ölçümün karşı kutbundan çıktı.** Sızmayan
   179 kalemin ortak yanı: cevap **konuşmanın seçtiği bir değer**, alanın ders
   kitabı terimi değil; ve seçenekli tipte iki seçenek aynı köke eşit uyuyor
   (kişi–görüş eşleştirmeleri, birbirini dışlayan çiftler). Ayrım ancak sesten
   geliyor — olması gerektiği gibi.

### Karşılaştırma tabanı yok — bu rapor onu uydurmuyor

Yöntem notunun 4. maddesi burada da geçerli: dinlemede resmî örnek sorulardan
ölçülmüş bir taban yok (`denetim/DENETIM-RAPORU.md` §5, madde A3). %39.8'in
"yüksek" mi "normal" mi olduğunu söyleyecek sayı elde değil. Rapor bu yüzden
tabanla karşılaştırma yapmıyor; oranlar tip bazında, kendi içinde okunmalı ve
asıl ağırlık mekanizma tablosunda — bir kalemin neden bilindiği, kaçının
bilindiğinden daha çok şey söylüyor.

### Ne yapıldı, ne yapılmadı

- Toplu rapor yazıldı; makine okunur hâli `content/DOGRULAMA/SESSIZ-TOPLU.json`.
- 121 kalem işaretlendi, her birine kendine özgü `flag_reason` + `flag_mechanism`.
- Hiçbir soru silinmedi; hiçbir sorunun metni/cevabı değiştirilmedi; tam testler
  12/12 × 40 soru; şema hatası 0; toplam 1310 soru; işaretli 116 → 237.
- Yeni araçlar: `tools/_e8_toplu.py`, `tools/_e8_isaret_tablosu.py`,
  `tools/_e8_isaretle.py`, `tools/_e8_gerekce_taslak.py`,
  `tools/_e8_mekanizma_tablo.py`, `tools/_e8_dayanak_toplu.py`.
  `sessiz-kopya.py`ye yalnız yeni `blind_note`
  alanı silinenler listesine eklendi (kopya `_e8_sizinti_kontrol.py`den 0 ağır
  hatayla geçiyor).
- `metinsiz-*` araçlarına ve okumanın ölçüm dosyalarına (`dogrulama/metinsiz/`,
  `kalibrasyon/metinsiz/`, `content/DOGRULAMA/METINSIZ-*`) hiç dokunulmadı.
- Ses metnine, `content/listening/scripts/` klasörüne ve cevap anahtarına beş
  çalıştırmanın hiçbirinde bakılmadı.
- **Bu adım işaretledi, düzeltmedi.** 121 kalemin yeniden yazılması ayrı bir iş;
  hangi mekanizmanın nasıl onarılacağı yukarıdaki tabloda duruyor.

🔴 Bu ölçüm bozuk soruyu bulur, zorluk ölçmez.
