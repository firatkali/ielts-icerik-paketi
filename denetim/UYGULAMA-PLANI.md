# IELTS Soru Havuzu — "Yayına Hazır" Uygulama Planı

Tarih: 2026-08-17. Kaynak: `denetim/DENETIM-RAPORU.md` §0 KARARLAR + kod incelemesi.
**Amaç:** işaretli 250 sorunun (237 kalem) tamamını, onları işaretleyen ölçümden geçen
içerikle değiştirip havuzu sıfır işaretle derlenebilir hâle getirmek.

---

## 0. Sıra ve neden bu sıra

```
FAZ 0  hazırlık/tarama  ──┬─► FAZ 1  B3-okuma (yeni pasajlar + 157 soru yeniden üretim; B2'nin alıştırma tarafı içinde)
                          ├─► FAZ 2  B3-dinleme (uygulama tarafı "ısınmış kayıt" işareti)
                          │            └─► FAZ 3d  capraz_sizinti 10 kalem
                          ├─► FAZ 3a  secenek_sozu + cerceve_sozu 49 kalem   (bağımsız, paralel)
                          └─► FAZ 3c  genel_kultur 43 kalem                  (bağımsız, paralel)
FAZ 4  B2 kalanı (test tarafı cümle tamamlama)
FAZ 5  ölçüm + denetim yenileme + derleme + uygulama doğrulaması
```

- **Faz 0 önce:** 26 okuma işaretinde `flag_mechanism` boş (eksik gerekçe yanlış düzeltmeye
  götürür) ve "bir olgu, bir paket" taraması yapılmadan kaç yeni pasaj gerektiği bilinmiyor.
- **B3-okuma B2'yi içine alıyor:** `matching_sentence_endings`ın 10 sorusunun 10'u,
  `sentence_completion`ın 15'i alıştırmada. Alıştırma zaten yeniden yazılacağı için bu iki tip
  aynı elden üretilir. B2'den geriye yalnız test tarafındaki 22 cümle tamamlama sorusu kalır.
- **`capraz_sizinti` 10 kalemi B3'e bağlı** (§0).
- 🔴 **Kritik zamanlama kuralı:** dinleme sesleri hiç üretilmedi → bugün senaryo metnine dokunmak
  bedava; ses üretildikten sonra aynı dokunuş yeniden kayıt demek. **Bütün dinleme metni
  düzeltmeleri ses üretiminden önce bitmek zorunda.** Planın en sert kapısı.

---

## FAZ 0 — Hazırlık (mekanik, ucuz model)

### 0.1 Boş mekanizma alanlarını doldur (B8)
✅ **Yapıldı (2026-08-17).** 12 dosyada 26 alan dolduruldu: `genel_kultur` +11, `konumsal_duzen` +11,
`secenek_sozu` +4. Alan boş değil, **tamamen yoktu**; gerekçedeki `dayanak:` etiketi
(`logic`/`general_knowledge`/`option_wording`) sözlüğe eşlenerek yazıldı.
`tools/dogrula.py`: şema 0 hata, 12 sınav 40/40, toplam 1310, işaretli 237.
⚠️ Sözlük dışı bir değer var (eskiden beri): `tanim_sizintisi` — mekanizma bazında gruplarken hesaba kat.

### 0.2 "Bir olgu, bir paket" taraması (B3'ün ölçüsü)
Temel: `tools/_e6_comp_capraz.py`. Yeni araç `tools/capraz-kok.py` üç çakışma türünü ayrı sayar:
1. **kanıt çakışması** — aynı `evidence` cümlesi iki farklı pakette,
2. **kök çakışması** — bir sorunun `prompt`'u başka paketteki sorunun `answer`/`accepted_variants`
   dizgisini düz metin taşıyor (**asıl kanal**),
3. **pasaj/senaryo paylaşımı** — aynı `passage_id`/`script_id` hem alıştırmada hem testte.

Çıktı: `denetim/CAPRAZ-KOK.md` + `.json`. Aynı tarama dinleme için de koşulur (Faz 3d'nin iş listesi).
**Bu tarama planın girdisi:** yeni pasaj sayısı kararı bu sayıyla verilir.

### 0.3 Sayıları yeniden say, karar dosyasını yaz
✅ **Yapıldı (2026-08-17):** doğru sayı **157 kalem / 160 soru numarası / 12 paket**.
"154 kalem" iddiasının deponun hiçbir yerinde kaynağı yok — plan metnine oradan girmiş.
Fark tek dosyadan: `multiple-choice.json` 12 kalem, 3'ü çift cevaplı (2'şer numara).
Kanıt ve paket bazlı tam tablo: `denetim/B3-ALISTIRMA-SAYIM.md`. **Ders: sayıya güvenme, yeniden say.**

Yeni kurallar `content/PLAN-EK-kurallar.md`'ye yazılır (**`PLAN-soru-dagilimi.md` elle değişmez**):
- yeni pasaj kimlikleri + "alıştırma havuzu ile test havuzu ayrıdır",
- pasaj başına bütçe: **paragraf başına en çok 3 soru, kanıt cümlesi başına en çok 1 soru**,
- "boşluğu kalıbın ucuna değil, kaynağın seçtiği değere aç",
- "gerçek, ünlü olay + kamuya açık sayı yasak" (B4 dersi),
- MSE reçetesi (E7, bağlayıcı): yanlış sonlardan en az ikisi aynı köke anlamca oturacak.

### 0.4 Uygulama engeli: alıştırma pasajı görünmüyor
✅ **2026-08-17'de ÇÖZÜLDÜ** (plandan bağımsız olarak aynı gün bulundu ve düzeltildi).
`QuestionItem` + `QuestionGroup`'a `passage_id` eklendi, `PlacedQuestion.passageID` item→group→set
zinciriyle çözüyor, `ReadingPaper` yeni alanı okuyor, `Tests/IELTSTests/ReadingPaperTests.swift`'e
iki regresyon testi yazıldı. ⚠️ **Yeni pasajlar item/group düzeyinde `passage_id` yazmalı.**

---

## FAZ 1 — B3 okuma: yeni pasajlar + alıştırma havuzunun yeniden üretimi

### 1.1 Kaç pasaj (karar noktası)
Taşınacak yük ~157 kalem. Gerçek sınavda 700-900 kelimelik bir pasaj 13-14 soru taşır.

| Yeni metin | Metin başına soru | Gerçek yoğunluğa göre | Sonuç |
|---|---:|---|---|
| 6 (ilk karar) | ~26 | 2 katı | Aritmetik tutar ama pasaj-içi çakışma riski yüksek: B3'ün hastalığı alıştırma havuzunun içine taşınır |
| **8 (öneri)** | **~20** | 1,5 katı | Bütçe kuralı rahat tutuyor |
| 11 | ~14 | birebir | En temiz, en pahalı |

**Öneri: 8 metin** — 7 akademik (`A13`–`A19`) + 1 GT uzun metni (`G07`). 6 ile ısrar edilirse plan
aynen çalışır; tek fark Faz 1 sonunda 0.2 taramasının alıştırma havuzunun *kendi içinde* tekrar
koşulması (ek yarım tur). 0.2 "gerçek çakışma" sayısını düşük gösterirse üçüncü yol: yalnız
çakışanları taşı, 3 pasajla bitir.

### 1.2 Yeni metinlerin şartnamesi
Kaynak/biçim `prompts/01-pasaj-secimi.md` ile birebir (PLOS · NASA/NOAA/USGS · OpenStax;
700-900 kelime; 7-10 harflendirilmiş paragraf; CC BY / kamu malı; Wikipedia ve The Conversation
yasak). Dosyalar: `passages/academic/A13.json`…`A19.json`, `passages/general/G07.json`,
`passages/INDEX.json` (yeni alan `pool: "practice"`, `assigned_test: null`).

Ek şartlar:
1. **Konu çakışması yok.** Mevcut 18 metin: hayvan davranışı ×3, iklim/jeoloji/okyanus ×2, uzay ×1,
   tarih/arkeoloji ×2, toplum/iş ×2, sağlık/davranış ×2; GT: şehir hizmetleri, boş zaman, personel
   el kitabı, staj, gıda israfı, gönüllülük. Yeni metinler bu alt konuların hiçbirine değmeyecek.
2. **Ünlü gerçek olay yasak** (B4): JWST/Uranus, Kandula, PANAS/POMS, Britanya mevzuatı gibi
   sayıları haberden bilinen olgular alınmayacak; sayısal cevaplar metnin kendi çalışmasının
   seçtiği değerler olacak.
3. Tip ön koşulları metnin yazımında karşılanacak:

| Metin taşıyacaksa | Metinde şart olan |
|---|---|
| Başlık eşleştirme | 8-10 paragraf, her paragrafın ayırt edilebilir tek ana fikri |
| YES/NO/NOT GIVEN | en az 4 yazar görüşü/değerlendirme cümlesi |
| Tamamlama ailesi | en az 4 paragrafta somut sayı/ölçü/ad — hepsi çalışmaya özgü |
| Özellik eşleştirme | 3-4 adı geçen araştırmacı/kurum, her birinin ayrı iddiası |
| Cümle sonu eşleştirme | en az 5 neden-sonuç/karşıtlık cümlesi (E7 reçetesi ancak burada uygulanır) |
| Diyagram etiketleme | çizilebilir bir süreç/düzenek anlatımı |

### 1.3 157 sorunun (160 numara) dağıtımı
Paket bazında ve **grup bütünlüğü korunarak** (bir grup = bir yeni pasaj).

| Paket (`content/reading/practice/`) | Kalem | Bugünkü pasajlar |
|---|---:|---|
| `sentence-completion.json` | 15 | A01-A05 (3'er) |
| `note-completion.json` | 15 | A06,A07,A08,A09,A12 |
| `summary-completion.json` | 15 | A10, A11, G05, G06 |
| `short-answer.json` | 10 | A01-A09, A12 — **her soru ayrı pasaj** |
| `diagram-labelling.json` | 10 | G01-G04 (görsel, hiç ölçülmedi) |
| `matching-information.json` | 15 | A01, A04, A07, A11 |
| `true-false-not-given.json` | 15 | A02, A05, A08, A09 |
| `yes-no-not-given.json` | 15 | A06, A10, A11, A12 |
| `multiple-choice.json` | 12 kalem / 15 numara | A02, A05, A08, A11 |
| `matching-headings.json` | 15 | A01, A09, A12 |
| `matching-features.json` | 10 | A10, G05 |
| `matching-sentence-endings.json` | 10 | A07, G06 |

Kurallar:
- **GT kaynaklı 17 kalem** (özet G05×4 + G06×3, MF G05×5, MSE G06×5) tek yeni GT metnine (`G07`);
  MSE'nin iki grubu da buraya — E7 reçetesi tek uzun anlatı metninde çok daha kolay kurulur.
- **Diyagram etiketleme 10 kalem** süreç anlatan akademik metne (`A19`). (Alternatif: yeni GT
  duyuru metni `G08` → +1 metin. Karar noktası.)
- Kalan ~130 kalem 7 akademik metne: metin başına **en çok 20 kalem, en çok 5 farklı paketten**.
- Kesin harita üretimden **önce** betikle: `tools/b3-dagitim.py` → `denetim/B3-pasaj-dagitimi.md`.
  **Yazım bu tablo onaylanmadan başlamaz.**

### 1.4 En zor kalem: `short-answer` (10 soru, 10 ayrı pasaj)
10 yeni pasaj gerekmiyor:
- Yeni düzen: akademik metin başına ~1-2 soru (7 metin × 1-2 = 10). Grup yapısına geçirilir:
  her metin için `group_id` + kendi `passage_id`si + kendi yönergesi
  (`"Questions 1-2 refer to Passage A13"`) — 0.4'teki uygulama düzeltmesiyle birebir uyumlu.
- Her soru, o metinde **başka hiçbir sorunun dokunmadığı** bir paragrafa çapalanır.
- Cevap metnin kendi çalışmasının seçtiği bir değer olacak (bugünkü 10 sorunun 1'i — A04, JWST poz
  sayısı — tam bu yüzden işaretli).
- Kalem sayısı 10'da sabit kalır.

### 1.5 Yeniden üretimin şekli
**Taşıma değil, yeniden yazım** (kanıt cümlesi eski pasaja aitti). Her sorunun `prompt` · `answer` ·
`accepted_variants` · `evidence` · `evidence_locator` · `explanation` alanları yeniden yazılır;
`question_type`, `number`, `instructions`, paket dosyası ve kalem sayısı **değişmez**.

| Tip | Reçete |
|---|---|
| `sentence_completion` (B2) | Boşluk **eşdizim öbeğinin ucuna açılmayacak**. Test: kökü tek başına okuyup boşluğu doldurmayı dene; tek aday çıkıyorsa boşluk yanlış yerde. |
| `matching_sentence_endings` (B2, bağlayıcı) | Sekiz sonun **en az ikisi** her kök için dilbilgisi + anlam olarak oturacak; ayrım yalnız pasaj ayrıntısıyla. `grammar_check` alanında hangi iki rakip sonun oturduğu tek tek yazılacak (bugünkü dosya tek rakiple yetiniyor — ölçüm yetmediğini gösterdi). |
| `multiple_choice`, `matching_features` | E6'nın ölçülmüş tekniği: genel kültürü **yanlış** seçeneğe çapala (yön değiştirme). |
| `summary_completion` (listeden seçmeli) | En riskli alt tip (%71 sızıntı). Ya kelime-yazmalıya çevrilecek ya da kutudaki adayların en az ikisi cümle çerçevesine oturacak. |
| `note`/`table`/`flow` | Boşluk ad-sayı-saat değerine açılır (ölçülmüş temiz kanal). |

---

## FAZ 2 — B3 dinleme: "bu kaydı zaten dinledin" işareti

### 2.1 Neden içerik değil uygulama işi
24 senaryonun 22'si hem testte hem alıştırmada; 6 test × 4 bölüm = 24 senaryoyu tüketiyor,
**yedek senaryo yok**. Yeni senaryo = yeni ses. Tek yol: kullanıcıya durumu söylemek.

### 2.2 Veri modeli — içerik tarafında yeni alan gerekmiyor
Her dinleme sorusu kaydını zaten biliyor (`PlacedQuestion.recordingID`, item→group→set) ve
`RecordingRun` oturumu kayıt bazlı bacaklara ayırıyor. Statik "bu paylaşımlı" bayrağı **yanlış**
olur: kullanıcı o kaydı dinlemediyse uyarı yalanlanır. Doğrusu **dinamik** — fiilen dinlenenleri tut.

### 2.3 Yapılacaklar (uygulama deposu)
1. `Sources/App/Listening/HeardScripts.swift` — `JSONStore` üzerinden `HeardScripts.json`,
   içerik `[scriptID: Date]`.
2. **Yazma anı:** ses gerçekten çalmaya başlayınca (`ListeningSitting.startLeg()` çağıranı) —
   oturum açılışında değil; yarıda bırakılan oturum "dinlendi" sayılmaz. ExamCore'a kalıcılık
   sokulmaz (katman kuralı).
3. **Okuma yerleri:**
   - Oturum başlangıç ekranı (`SessionOffer` + `SessionStartView`): künye altında tek satır —
     *"You have already heard 2 of these 3 recordings — your score here will look better than it is."*
     Sıfırsa satır çizilmez.
   - Kayıt öncesi hazırlık ekranı (`ListeningPreviewView`), bacak bazında:
     *"You've heard this recording before."*
   - İsteğe bağlı: sonuç ekranı (`SessionResultView`) — puanın yanında aynı şerh (karar noktası).
4. Metin dili İngilizce, uyarı değil olgu cümlesi.
5. Test: dinlenmiş kayıt sayısı doğru sayılıyor + satır 0'da çizilmiyor.

**Kapsam dışı not:** daha güçlü çözüm, plan motorunun senaryo paylaşan alıştırmayı **testten sonra**
sıraya koyması olurdu (`DrillCatalogue`/`PlanBuilder`). Sonraki tur fikri.

---

## FAZ 3 — B1: 121 işaretli dinleme sorusu, mekanizma bazında

### 3a. `secenek_sozu` 34 kalem — 14 dosya (`multiple-choice*`, `matching`)
Reçete: **seçeneğin sözünü kökten kopar.** Seçenek metni cevabı adlandırmayacak; üç seçenek de
köke oturacak, ayrım yalnız konuşmadaki ayrıntıyla. Hastalık örneği: "üzerinde çok fazla metin
olması puan götürür" yalnız *slayt* için söylenebilir. Ek: `distractor_analysis` alanına hangi iki
çeldiricinin aynı köke oturduğu yazılacak.

### 3b. `cerceve_sozu` 15 kalem — tamamlama ailesi
Reçete: **çerçevenin karşıtlığını sese taşı.** İskelet tek adayı ayakta bırakan karşıtlık
kurmayacak ("hacimle asla, (12) ile ölçülürdü"). Çerçeve nötrleşir, ayrım konuşmacının cümlesine geçer.

→ 3a + 3b = **49 kalem, tamamı yazım işi**; çoğunda senaryo metnine dokunmak gerekmez.

### 3c. `genel_kultur` 43 kalem — konu/değer değişikliği
Ucuzdan pahalıya:
1. **Aynı senaryonun başka bir cevap noktasına kaydır** (`answer_point_id` + `turn_index`
   güncellenir). Ses maliyeti sıfır. Okuma tarafında E6 tam bunu yaptı ve işledi.
2. Uygun değer yoksa **senaryo metnine kurgusal değer ekle** — bugün bedava, yarın kayıt demek.
   Dosyalar: `content/listening/scripts/L*-S*.json`. Senaryo değişince `word_count`,
   `estimated_minutes` ve o senaryoya çapalı **bütün** soruların `turn_index` değerleri yeniden
   hesaplanır (`tools/turn-index-kontrol.py`).
3. Hastalık örneği: "sıcaklık yıllardır eksi (2) derece" — tohum bankası standardı, senaryonun
   seçtiği değer değil.

### 3d. `capraz_sizinti` 10 kalem — B3'ten sonra
Kalemler: `practice/short-answer`, `practice/multiple-choice`, `practice/flow-chart-completion` ×3,
`practice/table-completion`, `tests/L1/note-completion` ×2, `tests/L5/form-completion`,
`tests/L3/summary-completion`.
Faz 2'nin uyarısı **farkındalık** sağlar, sızıntıyı kapatmaz — kanal, alıştırma sorusunun kökünün
testin cevabını **yazılı** vermesi. Bu yüzden: çakışan çiftin **alıştırma tarafındaki** sorusu aynı
senaryonun başka cevap noktasına kaydırılır (test 40/40 bozulmasın diye teste dokunulmaz); 0.2
taraması temiz çıkana kadar tekrarlanır.

### 3e. Kalan mekanizmalar
`konumsal_duzen` 11 + `esdizim_kilidi` 5 + `kip_imzasi` 3 = 19 kalem. Okuma tarafında bu üç
mekanizmanın reçetesi ölçülerek işledi (TFNG %53→%12, MF %69→%31).

---

## FAZ 4 — B2'nin kalanı: test tarafı cümle tamamlama
`content/reading/tests/{AC1,AC2,AC3,AC4,GT1,GT2}/sentence-completion.json` içindeki 22 soru
(7'si işaretli). Aynı reçete, ama **testte soru sayısı değişmez**: yuva korunur, kanıt cümlesi aynı
pasaj içinde başka yere taşınır (E6 yöntemi). Tip oranı %43'ten resmî tabanın (%20) altına inmediyse
ikinci tur.

---

## FAZ 5 — Ölçüm, doğrulama, derleme

### 5.1 Ölçüm protokolü (kabul şartının kendisi)
**Okuma:**
```
cd ~/Desktop/APPS/IELTS-icerik-paketi
python tools/metinsiz-kopya.py <paket>       # kör kopya → dogrulama/metinsiz/
# TEMİZ oturum: pasajı hiç açmamış bir model 3 bağımsız tur çözer
python tools/metinsiz-rapor.py <paket>       # → content/DOGRULAMA/METINSIZ-<paket>.md
```
**Dinleme:**
```
python tools/sessiz-kopya.py <paket> [--secim=tek|cok]
python tools/sessiz-rapor.py <paket>         # → content/DOGRULAMA/SESSIZ-<paket>.md
```
**Cevap anahtarı** (yeni yazılan her soru): `prompts/CAPRAZ-90-dogrulama.md` — pasaj/senaryo
görünür, cevap anahtarı gizli, üretmeyen model çözer.

🔴 Kırılmaz kurallar: ölçen oturum yazan oturum olamaz; `passages/` ve `content/listening/scripts/`
ölçüm oturumunda hiç açılmaz; hiçbir soru silinmez; tam testler 40 soruda kalır.

### 5.2 "Geçti" eşiği

| Alan | Eşik |
|---|---|
| Okuma, tabanı olan tipler | K3 3/3 oranı `RESMI_TABAN`ın altında |
| `sentence_completion` | ≤ %20 (1/5 resmî taban) |
| `matching_sentence_endings` | Taban bozuk (3 soruluk örnekte 3/3 = %100) → proje ölçütü: ≤ %20 (10 soruda en çok 2) **ve** reçete denetimi |
| Dinleme MC + eşleştirme | Resmî taban yok → öneri ≤ %30 (bugün %65-88) |
| Dinleme tamamlama ailesi | öneri ≤ %20 |
| Her tekil kalem | Daha önce işaretlenen kalem yeni ölçümde 3/3 bilinmeyecek |

Tekrar 3/3 çıkan kalem "düzeltilmedi" sayılır → ikinci tur. İki tur sonunda geçmeyen tip için karar
yeniden istenir (E5/E6 emsali).

### 5.3 Denetim belgelerinin yenilenmesi
```
python tools/dogrula.py      # şema 0 hata, 12 test 40/40, toplam 1310, telif taraması
python tools/manifest.py     # content/MANIFEST.json + işaretli sayısı
python tools/capraz-kok.py   # çakışma 0 olmalı
```
Sonra `denetim/{envanter,capraz-ozet,DENETIM-RAPORU}.md` 3. tur koşulur. Beklenen: işaretli 250 → 0
(görsel tipler hariç — B10 açık madde).
⚠️ Depodaki `denetim/... 2.md` iCloud kopyaları önce temizlensin.

### 5.4 Derleme ve Türkçe bekçisi
```
cd ~/Desktop/APPS/IELTS-app && python3 scripts/icerik-derle.py
```
Zincir: derle → cevap kâğıdı kontrolü (12 sınav) → Türkçe sızıntı taraması → `demo-uret.py`.
- Kullanıcıya görünen alanlar (`prompt`, `answer`, `evidence`, `explanation`, `topic`, `visual.alt`)
  **İngilizce**; denetim alanları (`flag_reason`, `grammar_check`, `distractor_analysis`,
  `scan_note`, `yeniden_uretim`) Türkçe kalır, `IC_ALANLAR` ayıklıyor.
- Yeni denetim alanı eklenirse `scripts/icerik-derle.py` içindeki `IC_ALANLAR` kümesine **aynı
  commit'te** eklenmeli; yoksa Türkçe not bundle'a girer ve bekçi derlemeyi kırar.
- Yeni pasajlarda Türkçe harfli özel isim varsa `BEKCI_IZINLI_OZEL_ISIMLER` listesine eklenir.

### 5.5 Uçtan uca kanıt
```
cd ~/Desktop/APPS/IELTS-icerik-paketi && python tools/dogrula.py && python tools/manifest.py && python tools/capraz-kok.py
cd ~/Desktop/APPS/IELTS-app  && python3 scripts/icerik-derle.py --isaretlileri-cikar
cd ~/Desktop/APPS/IELTS-app/app/Packages/ExamCore && swift test
cd ~/Desktop/APPS/IELTS-app && xcodebuild test -scheme IELTS -destination 'id=00008140-00090DEC1A40801C'
```
**Geçti demek için hepsi birden:**
1. `dogrula.py`: şema hatası 0, 12 test 40/40, toplam 1310,
2. `capraz-kok.py`: paket-arası kök/kanıt çakışması 0,
3. `icerik-derle.py --isaretlileri-cikar`: **"isaretli cikarilan soru: 0"** + "cevap kagidi: 12
   sinavin hepsi tutuyor" + "dil taramasi: Turkce sizinti yok" — bu tek komut "hiç işaretli soru
   kalmadı" ile "her test hâlâ 40 satır" iddiasını aynı anda kanıtlar,
4. ExamCore 82 + IELTSExam 17 + app 67 testi geçiyor (yeni eklenenlerle),
5. Cihazda: bir okuma alıştırması pasajıyla açılıyor (0.4'ün kanıtı) + dinleme başlangıç ekranında
   "ısınmış kayıt" satırı doğru sayı gösteriyor (Faz 2'nin kanıtı).

---

## Model kademesi ve paralelleştirme

| İş | Kademe |
|---|---|
| 8 yeni pasaj yazımı | güçlü (kaynak seçimi + lisans + tip ön koşulları aynı metinde) |
| 157 alıştırma sorusunun yeniden üretimi | güçlü (çeldirici tasarımı, sızıntı sezgisi) |
| B1 dinleme 49 yazım kalemi | güçlü |
| B1 `genel_kultur` 43 kalem | güçlü (hangi değer dünya bilgisi) |
| Kör ölçüm turları | güçlü, **ayrı ve temiz oturum** |
| 26 `flag_mechanism` doldurma | ucuz |
| `capraz-kok.py`, `b3-dagitim.py`, `turn-index-kontrol.py` | ucuz |
| Kimlik/çerçeve toplu güncellemeleri | ucuz |
| Uygulama düzeltmeleri (0.4, Faz 2) | ucuz (şablon kodda var) |
| Envanter/denetim tabloları | ucuz |

**Paralel hatlar** (farklı dosyalar, çakışmıyor):
- **A:** Faz 1 (okuma) — `passages/` + `content/reading/practice/`
- **B:** Faz 3a+3b (dinleme yazım) — `content/listening/`
- **C:** Faz 0.4 + Faz 2 (uygulama deposu)
- **D:** Faz 0.1-0.3 + araçlar + denetim tabloları

Sıralı kalanlar: 3d (B3'ten sonra), Faz 4 (Faz 1 reçetesi doğrulandıktan sonra), Faz 5 (en son).

---

## İş hacmi

| Kalem | Miktar |
|---|---:|
| Yeni pasaj | 8 (öneri) — ~6.500 kelime |
| Yeniden yazılacak okuma sorusu | ~157 alıştırma + 22 test = ~179 |
| Elden geçirilecek dinleme sorusu | 121 |
| Dokunulacak içerik dosyası | ~70 |
| Yeni araç betiği | 3 + `icerik-derle.py`'de 1 satır |
| Uygulama dosyası | 5-7 |
| Ölçüm turu | Okuma 12 paket × 3 tur, dinleme 8 paket × 3 tur + düzeltme turu payı |

---

## Riskler ve tuzaklar

1. **Yeniden üretim yeni sızıntı üretir.** E6'nın 72 yeni sorusunun cevap anahtarı %100 tuttu ama
   sızıntı ölçümünde yeni işaretler çıktı. "Tek turda biter" varsayımı bu projede iki kez yanlış çıktı.
2. **Ölçüm kirlenmesi.** Kapsam için okunan raporlar cevapları içeriyor. Ölçüm oturumu yalnız kör
   kopyayı görecek; kapsam listesi ona dosya adı düzeyinde verilecek.
3. **Aynı model ailesi.** Üreten de ölçen de denetleyen de aynı aile — bilinen ve kabul edilen sınır.
4. **Yoğunluk tuzağı.** 6 pasaja 157 soru sığdırmak B3'ün kapattığı kanalı alıştırma havuzunun
   içinde yeniden açar. Bütçe kuralı + Faz 1 sonu iç tarama zorunlu.
5. 🔴 **Ses kapısı.** Faz 3 bitmeden ses üretilirse her senaryo düzeltmesi yeniden kayıt demek.
6. **`turn_index` sessiz bozulması.** Senaryoya cümle eklenince tur indeksleri kayar; "kaçırdığım
   yeri tekrar dinlet" sessizce yanlış yeri çalar. Betikle denetlenecek.
7. **Test bütünlüğü.** Dinleme testlerinin altısı da işaretli, hiçbiri silinemez → yerinde düzeltme.
8. **`PLAN-soru-dagilimi.md` elle değişmez** — yeni kimlikler `PLAN-EK-kurallar.md`'ye.
9. **Demo paketi havuzdan türüyor** (`demo-uret.py`) — içerik değişince onboarding sorusu gözle
   kontrol edilmeli.
10. **iCloud kopyaları** (`denetim/... 2.md`) yanlış rapora bakma riski.

---

## Karar bekleyen noktalar

1. **Kaç yeni okuma metni?** 6 / 8 (öneri) / 0.2 taramasına göre kısa yol.
2. **Diyagram etiketleme 10 sorusu nereye?** Süreç anlatan yeni akademik metne (metin sayısı artmaz)
   mi, yeni GT metni `G08`'e (+1 metin) mi?
3. **Cümle sonu eşleştirmede "geçti" eşiği?** Öneri ≤ %20 + reçete denetimi.
4. **Dinlemede "geçti" eşiği?** Öneri: seçenekli ≤ %30, tamamlama ≤ %20 — yoksa önce küçük bir
   resmî örnek ölçümü mü?
5. **Test tarafındaki kalan işaretli okuma soruları (≈62 kalem)?** §0 yalnız iki tip için yol seçti;
   `esdizim_kilidi` 43 + `konumsal_duzen` 29'un test kısmı için karar yok. (a) aynı reçeteyle elden
   geçir, (b) riski belgeleyip yayınla.
6. **B4 (gerçek olaya dayalı pasajlar) bu turda mı?** Mevcut test pasajlarındaki ≈16 kalem.
7. **"Isınmış kayıt" satırı sonuç ekranında da görünsün mü?**
8. **Ses üretimi ne zaman?** Plan Faz 3 bitmeden başlamamasını şart koşuyor. Dinlemesiz yayın
   masadaysa sıralama değişir: Faz 2-3'ün önceliği düşer, Faz 1 + Faz 4 tek başına yayın kapısı olur.
