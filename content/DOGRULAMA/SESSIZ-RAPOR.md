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
