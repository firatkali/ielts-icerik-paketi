# METINSIZ-90/2 — Yeniden Ölçüm: Sızıntı (Parçasız Çözüm) Raporu

Kaynak talimat: `prompts/FABLE5-E7-yeniden-olcum.md` (2. çalıştırma).
`OPUS5-E5`'in düzelttiği ve `OPUS5-E6`'nın yeniden ürettiği sorular, üretmeyen model
(fable) tarafından **okuma parçası ve cevap anahtarı hiç görülmeden** üç turda çözüldü;
karşılaştırmayı `tools/metinsiz-rapor.py` yaptı (ham çıktı:
`METINSIZ-yeniden-olcum.md/.json`), anlam düzeyi (K3) kararları elle verildi.

---

## E5/E6 sonrası değişen sorular — sızıntı — 2026-08-08

- Ölçen model: **fable** (düzelten/yeniden üreten: opus)
- Kapsam: `blind_solvable: null` bırakılmış **188 soru** + **AC1 TFNG #11** (E6 devri,
  NOTLAR.md) = **189 soru**, 52 dosya
- Üç turun üçünde de parçasız bilinen: yüzey düzeyinde **73 (%38,6)**, anlam düzeyinde
  (K3) **82 (%43,4)**
- İşaretlenen: **81 yeni** `status: "flagged"` (AC1-11 zaten işaretliydi); işaretli
  sayısı 35 → **116**. **Hiçbir soru silinmedi**; soru sayısı 1310 sabit, on iki tam
  test 40/40.

### Kapsam ve araç düzeltmesi

Kapsam 1. çalıştırmadaki gibi alan durumundan alındı (`tools/_e7_hedef_listesi.py`:
188 null) + NOTLAR.md'nin devrettiği AC1 TFNG #11. Ölçümden önce `python tools/dogrula.py`
koşuldu: on iki tam test 40/40, şema hatası 0 — E6'dan devreden eksik yok.

🔴 **`tools/metinsiz-kopya.py`'de, 1. çalıştırmanın `kor-kopya.py`'de kapattığı sızıntının
aynısı bulundu ve kapatıldı:** E5/E6'nın eklediği `revision`, `yeniden_uretim`,
`review_note`, `flag_mechanism` alanları metinsiz kopyaya geçiyor ve yer yer cevabı açık
ediyordu (örn. practice MC-1 üretim notu "doğru seçenek mutlak — 'the whole sample'").
Alanlar `SIL` kümesine eklendi, kopyalar temiz sürümden yeniden üretildi. Düzeltmeden
önce ilk kopya setinin yalnız practice MF/MH/MI/MSE bölümleri ile practice MC-1
görülmüştü; bu sorular için aşağıya şerh düşüldü. (`blind_solvable_kelime_duzeyi`
alanı da kopyada kalıyor; cevabı vermiyor ama meta bilgi taşıyor — araca eklendi,
bundan sonraki ölçümler için not.)

### K3 (anlam düzeyi) tablosu ve kabul ölçütü

Ölçüt: 3/3 parçasız bilinme oranı, tipin resmî tabanının (`OPUS5-B1` tablosu) altına
inmeli. K3 ekleri: yüzeyde tutmayıp anlamca bilinen 9 soru (örn. "hierarchy" ≈
"dominance hierarchy", "peel/skins" ≈ "peelings", "twice" ≈ "double", "65-item" ≈
"sixty-five-item", "cube" ≈ "concrete cube").

| Soru tipi | K3 3/3 | Oran | Resmî taban | B1'deki oran | Karar |
|---|---|---|---|---|---|
| sentence_completion | 9/21 | **%43** | 1/5 (%20) | — | 🔴 **düzelmedi** (tabanın üstünde) |
| matching_sentence_endings | 9/10 | **%90** | 3/3 (%100) | %100 | ⚠️ teknikçe tabanın altında, **fiilen düzelmedi** |
| multiple_choice | 18/30 | %60 | taban yok | %100 | düştü ama sızıntı yüksek |
| flow_chart_completion | 3/4 | %75 | taban yok | — | GK sızıntısı (aşağıda) |
| summary_completion | 15/29 | %52 | 4/4 (%100) | — | tabanın altında; kırılım: listeden seçmeli **10/14 (%71)**, kelime yazmalı 5/15 (%33) |
| matching_features | 8/18 | %44 | 3/4 (%75) | %69 | tabanın altında ✓ |
| yes_no_not_given | 9/23 | %39 | taban yok | %100 | büyük düzelme ✓ |
| short_answer | 1/3 | %33 | taban yok | — | tek sızıntı GK (aşağıda) |
| note_completion | 2/8 | %25 | 6/6 (%100) | %27 | tabanın altında ✓ |
| true_false_not_given | 7/30 | %23 | 3/3 (%100) | %53 | tabanın altında ✓ |
| matching_headings | 1/8 | %12 | 4/4 (%100) | %18 | tabanın altında ✓ |
| table_completion | 0/3 | %0 | 0/5 (%0) | %33 🔴 | tabana **eşit** (%0'ın altına inilemez); B1'deki 🔴 kapandı ✓ |
| matching_information | 0/2 | %0 | taban yok | %6 | temiz ✓ |
| **toplam** | **82/189** | **%43,4** | genel resmî ort. %57 | — | |

**Kabul ölçütü sonucu:** bir tip açıkça **düzelmedi** — `sentence_completion`
(%43 > %20). Bir tip fiilen yerinde saydı — `matching_sentence_endings` (%100 → %90;
taban %100 olduğu için ölçüt teknikçe geçiyor, ama 10 sorunun 9'u hâlâ parçasız
çözülüyor). İyimser yuvarlama yapılmadı: iki tipin sızdıran soruları tek tek
işaretlendi (aşağıda).

### Asıl örüntü 1 — sızıntının en büyük tek kaynağı artık soru yazımı değil, **pasaj paylaşımı**

Aynı pasaj hem alıştırma paketlerinde hem tam testlerde kullanılıyor ve bir paketteki
soru kökü/çeldiricisi diğer paketteki sorunun cevabını veriyor. Ölçümde 3/3 bilinen
soruların en az **20'si** bu kanaldan çözüldü. Örnekler:

- practice MC-11 ("yer araştırması hangi gün?") cevabını **practice TFNG-10'un kökü**
  açıkça veriyor ("The ground survey of 12 December…"). Aynı pasaj (A08), aynı
  alıştırma havuzu.
- practice MC-9-10 (D+E: "90 km" ve "700'den fazla") cevaplarını **AC3 MF-26 ve
  AC3 SC-19'un kökleri** veriyor (aynı A08 pasajı test tarafında).
- practice MC-7-8 (C+F) ile **AC2 MF-24/26'nın kökleri** birbirini doğruluyor
  ("first genetic sign", "arisen earlier… further from the heartland").
- practice YNNG-3/6/7 cevapları **AC2 özet 38-39 ve practice özet 1-2'nin
  köklerinden** çıkıyor (aynı verimlilik/ofis çalışmaları).
- practice YNNG-9 cevabı **AC4 SC-20'nin kökünden** çıkıyor ("kampüs yalnız …,
  ormana beş dakika" → yürüyüş süresi eşit değil → NO).
- GT1 YNNG-33 cevabı **practice özet-12'nin kökünden** çıkıyor (kentli atığın daha
  büyük payı yenilebilir).
- Aynı **test içinde**: GT2 özet-39'un kökü ("the greater share of the effect that
  money cannot account for") hem GT2 özet-37'yi (B) hem GT2 YNNG-36'yı (NO) çözüyor;
  AC3 özet-38'in kökü AC3 MC-34-35'i (B+F) çözüyor; AC1 SC-20'nin kökü ("üç gün süren
  on beşer dakikalık buluşmalar") AC1 SC-22'yi ("fifteen minutes") çözüyor. Test içi
  olanlar gerçek adayda sorun değil (pasaj zaten önünde) ama **aynı dosyada bir kökün
  komşu sorunun cevabını harfiyen içermesi** (AC1 SC-20→22) yine de kusur.

Alıştırma↔test paylaşımı E5/E6 tarzı soru düzeltmesiyle kapanmaz; ya alıştırma
pasajları ayrılır ya da paylaşılan pasajlarda **aynı olguya iki paketten soru
yazılmaz** (E6'nın kanıt-çakışması taraması tam bu kuralın soru içi hâli; paket
arası köke de genişletilmeli).

### Asıl örüntü 2 — gerçek olaya dayalı pasajlar genel kültürle çözülüyor

- **JWST/Uranus ayı (A04):** practice SC-11 (`S/2025 U1`), SC-12 (`56,000 kilometres`),
  kısa cevap 4 (`ten` poz), AC2 akış-1 (`40 minutes`), akış-3 (`ten kilometres`) —
  hepsi 3/3, hepsi `general_knowledge`: keşif gerçek ve kamuoyuna duyurulmuş, sayılar
  haberlerde. E6'nın "küçük yuvarlak sayı" riski notu doğrulandı.
- **Maug adası:** AC1 MC-32 (D: "450 mil kuzeyde") NOAA metinlerinden bilinen rakam.
- **PANAS/POMS:** AC4 MF-26 (B: 20 madde) ve AC4 SC-21 (`65-item`) yayımlanmış ölçek
  tanımı — E5'in "madde sayısına çapala" düzeltmesi işlemedi, çünkü madde sayılarının
  kendisi genel kültür.
- **Britanya iş hukuku/âdetleri:** GT1 not-19 (`eleven hours`), GT1 MC-23-24 (C+G:
  beş gün devir + 1 Nisan; E6'nın kendi risk notu birebir doğrulandı), GT1 MC-21/22,
  GT2 MC-22.
- **Kandula (A01):** AC1 TFNG-12 (FALSE: sopa verilmişti) ünlü deneyin bilinen
  ayrıntısı; TFNG-11 (TRUE) sibling not-tamamlama kökünden.
- **Radar GK:** AC3 SC-20 (`bright`), practice TFNG-11 (buzul denize akar → FALSE).

Bu küme de soru yazımıyla kapanmaz; **pasaj/konu seçimi** kararı ister (kurgusal ya da
az bilinen olay + pasaja özgü sayı).

### Asıl örüntü 3 — listeden seçmeli özetler anlamsal olarak kendini tamamlıyor

AC4 özet 4/5, GT2 özet 4/4 bilindi: "remained ___ until an evening test" → *awake*;
"the two turned out to offer ___" → *equal benefits*; "across those versions the
picture was ___" → *stable*; "describe what they have shown as ___" → *a link rather
than a cause*. Cümle çerçevesi doğru cevabı tek başına seçiyor; resmî tabanın da
%100 olması tipin doğasını gösteriyor. Kelime-yazmalı özet/tamamlamalarda ise oran
%33'e düşüyor ve E5/E6 düzeltmeleri görünür biçimde çalışıyor (aşağıda).

### Düzeltmelerin gerçekten çalıştığı yerler

- B1'de %100 olan üç tipten ikisi ciddi düştü: **çoktan seçmeli %100 → %60**,
  **YNNG %100 → %39**. TFNG %53 → %23, matching-features %69 → %44,
  table-completion'daki 🔴 (%33 → %0) kapandı.
- E6'nın "kendi kendini sınama"da geçti dediği sorular ölçümde de geçti: practice
  TFNG-4 (sezgi FALSE'a gitti, anahtar TRUE), AC3 TFNG-7 (sezgi TRUE, anahtar FALSE),
  AC1 özet-36 (sezgi "rim", anahtar "inner shoreline"), AC3 SC-22 (sezgi "analysts",
  anahtar "glaciologists"), AC3 tablo-6 (sezgi "left/preferred eye", anahtar "right
  eye"), AC1 not-4 (sezgi "ball", anahtar "tyre"), AC3 MF-24/25 (sezgiler B/C'ye,
  anahtarlar tersine). **Yön değiştirme tekniği** (genel kültürü yanlış seçeneğe
  çapalama) ölçülebilir biçimde işliyor.
- E5'in kip dengelemesi: YNNG'de eski "mutlak→NO / ölçülü→YES / eksen dışı→NG" kuralı
  artık çalışmıyor; bilinen 9 YNNG'nin 7'si kip değil **çapraz-pasaj** kanalından geldi.

### E5/E6'nın kendi uyardığı zayıf halkalar — dördü de doğrulandı

| Uyarı | Sonuç |
|---|---|
| AC2 MF-23 "tek küme seçeneği D'yi biçim ipucu gösteriyor" (E6) | 3/3 bilindi (option_wording) |
| AC1 TFNG-10 "eşitlik iddiaları yanlıştır kestirmesi doğruya götürebilir" (E6) | 3/3 bilindi (option_wording) |
| GT1 MC-23-24 "1 Nisan tek başına tahmin edilebilir" (E6) | 3/3 bilindi (C+G, general_knowledge) |
| practice YNNG-6 "kısmi düzeltme, çözücü yine NO'ya varabilir" (E5) | 3/3 bilindi |

### matching_sentence_endings — neden düzelmedi

E5'in eklediği rakip sonlar yalnız 7. soruda çalıştı (ölçümde G/C arasında bölündüm,
anahtar C — bilinemedi). Kalan dokuzda kök hâlâ tek sona kilitleniyor: "very first
session" → "two hours yetti" (2), işaret konumu → "kendisi göremez" (3), dışlanma →
tek dışlanma sonu (6, E5'in kendi itirafı), ülke karşıtlığı → tek ülke listesi (8).
Bu tip **kök-son çerçeve eşleşmesi** üzerine kurulu; rakip-ekleme yetmiyor, ayrım
pasaja taşınacaksa sonların en az ikisinin aynı köke anlamca da oturması gerekiyor.
Yeniden üretim kararı E-zincirinin sonraki halkasına devredildi (soru silinmedi,
9'u işaretli).

### 🔴 Yöntem şerhleri (dürüstlük kaydı)

1. **Kirlenme.** Kapsamı belirlemek için okunan `RAPOR-2.md` ve `ELDEN-GECIRME.md`
   (1-3. bölümler) bazı cevapları içeriyordu: MSE'nin 10 cevabı, E5'in düzelttiği
   YNNG'lerin cevapları, bazı MC harf çiftleri, GT1 özet-40 ("prevention") ve practice
   MH-15 ("v"). Çözümlerde karar yalnız soru metni gerekçesiyle verildi ve gerçek
   kararsızlık turlara yansıtıldı (örn. GT1 özet-40 "reduction/prevention/reduction"
   yazıldı → bilinmedi sayıldı; practice MH-15 v/ii/v → bilinmedi sayıldı; MC 34-35
   çiftlerinin üçü kararsız bırakıldı → bilinmedi). Yine de **MSE ve E5-YNNG
   sorularının ölçümü "tam kör" sayılmamalı**; MSE için güven, B1'in kirlenmesiz
   ölçümünün aynı sonucu (10/10) vermiş olmasından geliyor.
2. **Tur bağımsızlığı sınırlı.** Üç tur aynı oturumda çözüldü; turlar arası kararlılık
   istatistiği bu yüzden rapora konmadı. Kararsız sorularda turlar bilerek
   ayrıştırıldı; 3/3 süzgecini taşıyan şey turlar değil, tek turda cevabı zorlayan
   işaretin kendisidir (B1 3. çalıştırmasındaki dürüstlük notunun aynısı).
3. **Sıra:** anahtarlar yalnız üç tur dosyası yazıldıktan sonra açıldı; K3 kararları
   (9 ekleme) bu rapordaki listeyle sınırlı ve `tools/_e7_k3_kontrol.py` çıktısına
   dayanıyor. Pasaj klasörü hiç açılmadı.
4. `tools/metinsiz-rapor.py` çıktısındaki dayanak dağılımı (`general_knowledge` 126 ·
   `logic` 273 · `guess` 144 · `option_wording` 24) üç turun toplamıdır; `logic`
   payının büyük kısmı yukarıdaki çapraz-pasaj kanalıdır, biçim ipucu değil.

### İşaretleme

- **82** soruya `blind_solvable: true` + `blind_basis`; 81'ine yeni `status: "flagged"`
  + `flag_reason` yazıldı (AC1 TFNG-11 zaten işaretliydi, gerekçesi korundu).
- **107** soruya `blind_solvable: false`, `blind_basis: null` yazıldı. 1. çalıştırmanın
  işaretlediği iki soru (practice MH-15, GT1 özet-40) bu ölçümde bilinmedi;
  `blind_solvable: false` aldı, işaretleri (cevap anahtarı gerekçeli) yerinde duruyor.
- Araçlar: `tools/_e7_metinsiz_secim.py` (hedef ayıklama), `tools/_e7_metinsiz_cevaplar.py`
  (üç tur cevabı), `tools/_e7_k3_kontrol.py` (K3 sınır kontrolü), `tools/_e7_isaretle2.py`
  (işaretleme). Tur dosyaları: `kalibrasyon/metinsiz/yeniden-olcum-tur{1,2,3}.json`.
- Doğrulama: `python tools/dogrula.py` → şema hatası 0, on iki tam test 40/40, toplam
  soru 1310 (değişmedi), işaretli 35 → **116**.

### Sonraki adıma devir

1. **Çapraz-pasaj kuralı:** E6'nın kanıt-çakışması taraması paket arası **kök**
   çakışmasına genişletilmeli ("bir olgu, bir paket"). En acil çiftler: A08
   (practice MC/TFNG ↔ AC3), A04/JWST (practice SC/kısa cevap ↔ AC2 akış), A05
   (practice YNNG/özet ↔ AC2), G06 (practice MSE ↔ GT2), G03 (practice özet ↔ GT1).
2. **Gerçek olay pasajları:** sayısal cevabı haberlerden bilinen beş JWST sorusu ile
   Maug-450, PANAS/POMS ve Britanya-mevzuat soruları işaretli; düzeltme yolu soru
   değil pasaj/olgu seçimi.
3. **MSE yeniden üretimi:** 9/10 işaretli; rakip-ekleme yaklaşımı bu tipte yetersiz.
4. **AC1 SC-22** kökündeki "fifteen minutes" tekrarını kaldırmak tek cümlelik iş
   (SC-20 kökü aynı süreyi veriyor).
5. AC1 TFNG-11 hâlâ sızdırıyor (sibling not-5 kökü cevabı doğruluyor); işaret yerinde.
