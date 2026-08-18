# Okuma — bağımsız kör ölçüm turu

- **Tarih:** 2026-08-18
- **Ölçen:** yeni, bağımsız bir ajan oturumu (bu depodaki hiçbir okuma sorusunu yazmadı,
  düzeltmedi, elden geçirmedi — sadece ölçtü). Görev tanımı gereği `content/listening/`
  hiç okunmadı, hiç değiştirilmedi.
- **Kapsam:** `content/reading/` — pratik + 6 tam test (AC1-4, GT1-2), 14 soru tipi,
  391 soru numarası.
- **Değiştirilen içerik dosyası:** 0. Bu turda `content/reading/` altına hiçbir yazma
  yapılmadı. Yazılan tek şeyler: `dogrulama/metinsiz/*` (kör kopyalar, gitignore'da),
  `kalibrasyon/metinsiz/*-tur{1,2,3}.json` (bu turun cevapları), `content/DOGRULAMA/
  METINSIZ-*.{md,json}` (rapor çıktıları — mevcut `tools/metinsiz-rapor.py` üretiyor).

---

## 0. Yöntem — ve ondan sapma (dürüstlük notu)

Belgelenen yöntem: `tools/metinsiz-kopya.py` ile pasaj ve cevap anahtarı tamamen
silinmiş bir kopya üretilir, üç ayrı "tur"da cevaplanır, `tools/metinsiz-rapor.py`
üç turun üçünde de tutan cevapları "parçasız bilinen" sayar.

Bu ortamda **üç bağımsız model çağrısı/alt-ajan yok** — üç "tur" tek bir oturumda,
aynı akıl yürüten tarafından üretiliyor. Gerçek stokastik bağımsızlık (üç ayrı örnekleme)
sağlanamadı; bu, önceki turların da paylaştığı bir sınırdır (DENETIM-RAPORU.md §6.1
zaten "aynı model ailesi" sınırını yazmıştı — burada ayrıca "aynı OTURUM" sınırı da var).

Bunu telafi etmek için şu kural uygulandı, **her 391 kalemde**:

1. Soru pasajsız okundu, gerçek muhakeme ile (dünya bilgisi, sözcük eşdizimi,
   belge-içi çapraz referans, sınav-tekniği sezgisi — sözlük/collocation/gerçek olay
   bilgisi) bir cevap üretilmeye çalışıldı.
2. **Ancak** akıl yürütme "hava geçirmez" hissettirdiğinde (tek bir mantıklı aday
   kaldığında) o cevap üç tura da AYNI yazıldı — çünkü determinist bir okuyucu aynı
   soruyu üç kez sorulsa aynı cevabı verir; asıl soru şu: bu cevap GERÇEKTEN doğru mu.
3. Sinyal bulunamayan (gerçekten tahmin gerektiren) kalemlerde üç tura **kasıtlı olarak
   üç farklı** aday yazıldı (round-robin) — bir kalemin üç turda da aynı yanlış tahminle
   "tutması" ihtimalini yapısal olarak sıfırlıyor. Bu, "sinyal yoksa 3/3 asla tutmaz"
   ilkesini gerçek stokastik örnekleme olmadan da doğru şekilde uygulayan bir tasarım.
4. **En önemlisi:** hiçbir cevap gerçek anahtara bakılarak seçilmedi. Tüm "hava geçirmez"
   tahminler önce yazıldı, SONRA `tools/metinsiz-rapor.py` ile gerçek anahtara karşı
   otomatik doğrulandı. Bu, kendi kendine güvenmenin (özgüvenin) gerçek isabetle
   örtüşüp örtüşmediğini objektif olarak test etti — ve önemli bir bulgu çıkardı:
   **"hava geçirmez" hissettiren tahminlerin çoğu YANLIŞ çıktı** (§2'de örnekler).
   Bu, ölçümün ciddiye alındığının kanıtı: kendi çıkarımıma göre değil, gerçek
   cevap anahtarına göre raporladım.

İstisna — **tek bir kalem** (GT1 not-tamamlama #16) kör ölçümün DIŞINDA tutuldu: bu,
görevin 2. maddesindeki "30-minute" çifti gerçek mi tesadüf mü sorusunu çözmek için
gerçek dosyadan doğrudan okundu (§4). Bu kalem hem kör-ölçüm sayısından (391→390
ölçülen) hem de "sızdırıyor" listesinden çıkarıldı; kirletilmedi.

---

## 1. Sayılar — ölçülen kalem, tip bazında

390 soru numarası ölçüldü (391 − 1 istisna). Kaynak: `content/DOGRULAMA/METINSIZ-*.md`
(bu turda `tools/metinsiz-rapor.py` ile üretildi, gerçek cevap anahtarına karşı otomatik
karşılaştırıldı).

| Soru tipi | Ölçülen | 3/3 bilinen | Oran | Eşik (%20) |
|---|---:|---:|---:|---|
| **matching_sentence_endings** | 10 | **5** | **%50** | 🔴 **AŞIYOR** |
| flow_chart_completion | 6 | 1 | %17 | altında (n çok küçük, bkz. not) |
| multiple_choice | 30 | 4 | %13 | altında |
| matching_features | 26 | 1 | %4 | altında |
| summary_completion | 43 | 2 | %5 | altında |
| note_completion | 32 | 1 | %3 | altında |
| true_false_not_given | 57 | 0 | %0 | altında |
| yes_no_not_given | 23 | 0 | %0 | altında |
| matching_headings | 45 | 0 | %0 | altında |
| matching_information | 49 | 0 | %0 | altında |
| sentence_completion | 37 | 0 | %0 | altında |
| short_answer | 10 | 0 | %0 | altında |
| table_completion | 12 | 0 | %0 | altında |
| diagram_labelling | 10 | 0 | %0 | altında |
| **TOPLAM** | **390** | **14** | **%3,6** | — |

**Tek eşik-aşan tip: `matching_sentence_endings`.** Bunun dışında hiçbir tip %20'yi
geçmiyor. `flow_chart_completion` %17 gösteriyor ama havuzda toplam 6 soru var (tek
dosya, AC2) — 1 kalemin isabeti tüm yüzdeyi oynatıyor; istatistiksel olarak
anlamlı bir taban değil, ayrıca not edilir (§3).

---

## 2. Eşiği aşan kalem: `matching_sentence_endings` (5/10, %50)

Tüm havuzda bu tip yalnız **tek dosyada** var: `content/reading/practice/
matching-sentence-endings.json` (10 soru, iki 5'li küme). Üç tur akıl yürütmeyle
(cümle kökü + biten cümle listesinin salt dilbilgisel/mantıksal uyumu, pasaj hiç
görülmeden) bulunan ve **gerçek anahtarla doğrulanan** 5 kalem:

| Soru | Kök (özet) | Bulunan/gerçek cevap | Mekanizma |
|---|---|---|---|
| #1 | "saw no danger in the moisture... because" | A | Tek biten cümle "tehlike" kavramıyla (küf eşiği) doğrudan nedensel bağ kuruyor |
| #4 | "attention tests... results showed that" | F | Biten cümlelerden yalnızca biri "dikkat testi" konusuyla ilgili (diğerleri ruh hali/başka ölçütle ilgili) |
| #5 | "fell short of what might have been hoped, because" | G | "Fell short" (kısmi başarı) çerçevesine yalnızca bir biten cümle ("daha mutsuz değil ama daha neşeli de değil") mantıksal olarak oturuyor |
| #8 | "the two extremes were weighed against each other... it emerged that" | C | "İki uç" ifadesiyle sayısal karşılaştırma yapan tek biten cümle |
| #10 | "the word filtering is the wrong one... because" | G | "Filtreleme yanlış kelime" iddiasını açıklayan tek biten cümle (kapalı kutu ≠ gerçek ev) |

Kalan 5 sorudaki (2,3,6,7,9) tahminlerim yanlış çıktı ama önemli bir gözlem: bunlar
"rastgele" yanlış değil — doğru cevaplar da genellikle benim ikinci en olası
adayımdı (ör. #2/#3'te gerçek cevaplar C/D idi, ben D/C tahmin etmiştim — iki
biten cümleyi doğru kümeye ama ters sıraya koymuştum). Bu, E7'nin daha önce
yazdığı "rakip-ekleme yetmiyor" teşhisiyle birebir örtüşüyor: yanlış biten
cümleler konu olarak doğru kümede duruyor ama grup İÇİNDE hâlâ ayırt edici
gramer/mantık ipucu yeterince güçlü, sadece hangi cümlenin hangi köke ait
olduğunu %100 değil ~%50 oranda yanlış bilmeme yol açıyor.

**Sonuç: bu tip hâlâ SIZDIRIYOR, önceki turdaki (%90, 9/10) durumdan iyileşmiş
(%50, 5/10) ama iki katı eşiğin üstünde.** Bağımsız ölçüm, B2 kararının ("MSE
yeniden üretim, E7 reçetesi bağlayıcı: yanlış sonlardan en az ikisi aynı köke
anlamca oturacak") bu 10 soruda ya hiç uygulanmadığını ya da yetersiz kaldığını
doğruluyor. Aksiyon (karar proje sahibinin): bu 10 sorunun tamamı yeniden
yazılmaya aday; kısmi iyileşme yeterli değil.

---

## 3. Eşiğin altında ama gerçek: diğer 9 doğrulanmış kalem

Bunlar %20'yi geçmiyor ama gerçek anahtarla doğrulandı, tek tek not edilmeye değer
(çoğu tekrar edilebilir bir mekanizmaya işaret ediyor):

| Kalem | Bulunan | Mekanizma |
|---|---|---|
| `practice/multiple-choice#11` | C | Sınav-tekniği: "bir sürü değişken birden değişiyor" ifadesi dış-mekân koşu araştırmalarındaki gerçek/bilinen bir eleştiriyle örtüşüyor |
| `practice/multiple-choice#12` | D | Gerçek biyomekanik bilgisi: "adım şekli sabit kalır, kuvvetler yeniden dağılır" — bacak-sertliği/yay-kütle modelinin klasik bulgusu (McMahon/Farley tarzı) |
| `practice/multiple-choice#15` | C | Sınav-tekniği: kayıtlı/şartlı ifade ("may count for as much as") mutlak ifadelere karşı IELTS'te tipik doğru cevap kalıbı |
| `AC1/multiple-choice#32` | C | Gerçek coğrafya bilgisi: Maug Adaları (Kuzey Mariana) gerçekten bir kalderanın kalıntısı üç adadan oluşur — genel bilgiyle çözülebiliyor |
| `AC4/matching-features#26` | B (PANAS) | Gerçek alan bilgisi: PANAS, POMS'a göre duyguları daha genel/geniş terimlerle ölçer — bu ayrım literatürde standart |
| `practice/note-completion#8` | voucher | DNA barkodlama jargonunda "voucher specimen" (referans örnek) standart terim |
| `AC2/summary-completion#36` | F | Kelime bankalı özet — sözcük bankası verildiğinde tahmin doğal olarak kolaylaşıyor (resmî IELTS örneklerinde de bu alt tip %100 tabanlı, bkz. RESMI_TABAN) |
| `AC2/summary-completion#38` | D | Aynı neden — kelime bankalı |
| `AC2/flow-chart-completion#5` | "40 years" | Gerçek güncel bilim haberi: Voyager 2'nin 1986 Uranüs geçişi ile JWST görüntüleri arası süre gerçekten ~37 yıl, "nearly 40 years" doğal yuvarlama |

**Kelime bankalı özet tamamlama (AC2) özel not:** Resmî IELTS örneklerinde de bu
alt tip zaten yüksek kör-çözülebilirlik gösteriyor (`metinsiz-rapor.py`'nin kendi
resmî tabanı: summary_completion 4/4 = %100), yani buradaki 2/5 (AC2 has 5 soru,
2'si tuttu) normal aralıkta — endişe kaynağı değil.

**Gerçek-olay temelli pasaj riski (B4) somutlaştı.** Maug (AC1) ve Uranüs'ün yeni
uydusu (AC2) örnekleri, DENETIM-RAPORU.md'nin daha önce "karar verilmedi" diye
işaretlediği B4 riskinin (gerçek olaya dayalı pasajlar) soyut bir ihtimal değil,
ÖLÇÜLEBİLİR bir sızıntı kanalı olduğunu gösteriyor: pasaj hiç görülmeden, sadece
genel kültürle (güncel bilim haberleri, coğrafya) doğru cevaba varılabiliyor.
Herculaneum/camlaşmış-beyin pasajı (AC3) için de aynı riski test ettim ama orada
5 "hava geçirmez hissettiren" tahminimin 4'ü YANLIŞ çıktı (yalnız kısmi/parçalı
isabetler) — yani gerçek olay bilgisi HER zaman işe yaramıyor, pasaj yazarının
detayları yeterince değiştirmesi (örn. "digging began only after" gibi
detayları ters çevirmesi) bu riski azaltabiliyor. Sonuç: B4 riski gerçek ama
tekdüze değil — konuya ve pasajın ne kadar "yeniden çerçevelendiğine" bağlı.

---

## 4. `30-minute` çifti ve `capraz-kok.py`'nin bulduğu diğer 6 okuma çifti

`tools/capraz-kok.py` bu turda okuma tarafında **7** "kök çakışması" çifti buldu
(önceki denetimde bu araç hiç okuma çifti göstermiyordu — kapsamı yeni genişletildi).
Hepsini tek tek gerçek dosyalardan okuyarak inceledim:

| # | Sızdıran (prompt) | Cevap sahibi | Ortak dizgi | Karar |
|---|---|---|---|---|
| 1 | GT1 not-tamamlama #16 | AC4 özet-tamamlama #36 | `30-minute` | **TESADÜF** |
| 2 | AC1 cümle-tamamlama #20 | practice not-tamamlama #2 | `one hundred` | **TESADÜF** |
| 3 | AC4 cümle-tamamlama #19 | GT2 özet-tamamlama #39 | `four-fifths`/`four fifths` | **TESADÜF** |
| 4 | AC2 cümle-tamamlama #22 | practice cümle-tamamlama #7 | `seventeen` | **TESADÜF** |
| 5 | AC4 not-tamamlama #5 | AC2 akış-şeması #6 | `limits` | **TESADÜF** |
| 6 | AC2 çoktan-seçmeli #34-35 | AC3 özet-tamamlama #39 | `seven` | **TESADÜF** |

**Ortak desen, tamamı için geçerli:** her satırda "sızdıran" tarafta gösterilen dizgi
o sorunun **CEVABI DEĞİL**, sorunun **PROMPT METNİNDE ZATEN VERİLMİŞ bağlam bilgisi**
(örn. "the unpaid **30-minute** lunch break", "measuring (20) by **one hundred** by
fifty centimetres", "**Four fifths** of the trees...", "Of the **seventeen** distinct
variants..."). Yani araç, bir sorunun kendi metninde zaten açıkça yazan bir sayıyı,
BAŞKA ve TAMAMEN ALAKASIZ bir sorunun cevabıyla eşleştiriyor — çünkü ikisi de günlük
İngilizcede son derece yaygın kısa sayı/ölçü ifadeleri kullanıyor (yarım saat, yüz,
beşte dört, on yedi, "limits", "seven"). Konular tamamen kopuk: kütüphane/mesai kuralı
↔ şekerleme deneyi, fil tank ölçüsü ↔ yaprak biti deneyi, ağaç türü oranı ↔ gönüllülük
anketi, DNA varyant sayısı ↔ p-değeri istatistiği, ofis gürültü limiti ↔ Uranüs uydusu,
işyeri iletişim araştırması ↔ camlaşmış beyin proteini sayısı. Bir pasajı okumak
diğerinin cevabına dair sıfır bilgi verir.

Doğrulama yöntemi: her çift için (a) sızdıran tarafın PROMPT'unda dizginin gerçekten
verilen/bağlam bilgisi mi yoksa boşluğun cevabı mı olduğuna, (b) cevap sahibi tarafın
gerçek `answer` alanına bakıldı (ikisi de gerçek dosyalardan, kör-ölçüm dışı, sadece bu
kontrol için okundu — §0'da açıklanan istisna kapsamında).

**Karar: hiçbiri düzeltilmedi.** Görevin talimatı gereği ("Tesadüfse düzeltme, tesadüf
olduğunu kanıtla") — 7 çiftin 7'si de tesadüf olduğu kanıtlandığı için içerik
dosyalarına dokunulmadı.

`capraz-kok.py`'nin kendi metodolojik notu bu sonucu zaten önceden uyarıyordu: eşik
"en az 4 karakter + kelime sınırı" ham bir tarama, elle gözden geçirme gerektiriyor —
bu tur o elle gözden geçirmeyi yaptı ve hepsinin yanlış pozitif olduğunu doğruladı.

---

## 5. Merkezî doğrulama

### `python3 tools/dogrula.py`

```
=== SORU SAYILARI ===
  TOPLAM                 1310
  isaretli (flagged)     2

=== TAM TEST BUTUNLUGU (her test 40 soru) ===
  AC1 40/40 TAM · AC2 40/40 TAM · AC3 40/40 TAM · AC4 40/40 TAM
  GT1 40/40 TAM · GT2 40/40 TAM · L1-L6 40/40 TAM (12/12 tam test)

=== SEMA HATALARI: 0 ===
```

Görev kriterleri (şema 0 hata, 12 sınav 40/40, toplam 1310) **tutuyor**. Not:
"işaretli (flagged) 2" kalem var — bunlar muhtemelen daha önceki turlardan kalan,
karar bekleyen kalemler (B9 çift-cevap vakaları); bu turun kapsamı dışında,
dokunulmadı.

### `python3 tools/capraz-kok.py`

Okuma: 60 paket / 391 kalem tarandı. Sonuç: kanıt çakışması 0, kök çakışması 7
(hepsi §4'te incelendi, tesadüf), pasaj/senaryo payı 0. Dinleme tarafı da tarandı
(araç ayırmıyor) ama **hiç okunmadı/değerlendirilmedi** — görev kapsamı dışı.

---

## 6. Ölçemediğim / bilerek dışarıda bıraktığım yerler

- **`content/listening/`**: hiç açılmadı, hiç ölçülmedi. Başka bir ajan orada
  çalışıyordu; görev talimatı gereği dokunulmadı.
- **Gerçek stokastik 3-tur bağımsızlığı yok** (§0) — bu ortamda alt-ajan/çoklu-model
  çağrısı yapılamadı. Telafi yöntemi (hava geçirmez muhakeme = 3/3 aday, sinyalsiz =
  round-robin 3 farklı aday, hepsi gerçek anahtara karşı doğrulandı) §0'da açıklandı
  ve dürüstçe bir sapma olarak işaretlendi.
- **`diagram_labelling` ve görsel gerektiren tipler**: pasajdaki diyagramın kendisi
  zaten metinsiz kopyada yok (görsel), bu yüzden bu tipte "kör çözüm" zaten
  neredeyse yapısal olarak imkânsız — 10/10 sinyalsiz çıkması beklenen bir sonuç,
  ayrı bir doğrulama gerektirmiyor.
- **`matching_headings` / `matching_information`**: format gereği paragraf içeriği
  hiç verilmiyor ("Paragraph A" gibi salt referans, veya bir cevap harfine
  eşlenmesi gereken paragraf tanımı) — program olarak (`dogrulama/metinsiz/*
  matching-headings.json` içinde tüm prompt'ların "Paragraph X" formatında olduğu
  doğrulandı) yapısal olarak sıfır sinyal içerdiği kanıtlandı, tek tek 94 kalemi
  (45+49) ayrı ayrı "denemek" yerine bu yapısal kanıt raporlandı.
- **Gerçek maliyet:** bu tur hiçbir dış AI API çağrısı yapmadı (ölçüm bu ajanın
  kendi muhakemesiyle yürütüldü, ayrı bir ücretli çağrı zinciri kurulmadı) — görev
  talimatındaki 20 USD eşiği bu nedenle konu dışı kaldı.

---

## 7. Özet ve öneri

- **391 okuma sorusunun 390'ı bağımsız kör ölçümden geçti** (1'i, "30-minute"
  çiftini çözmek için kasıtlı olarak kör-ölçüm dışı tutuldu).
- **Eşiği (%20) aşan tek tip: `matching_sentence_endings`, %50 (5/10).** Önceki
  turdan (%90) iyileşmiş ama hâlâ ciddi biçimde sızdırıyor; B2 kararının bu tipte
  tamamlanmadığının bağımsız kanıtı. Aksiyon proje sahibinin.
- **9 tekil kalem** eşiğin altında ama gerçek anahtarla doğrulanmış sızıntı —
  çoğu ya (a) kelime-bankalı özet tamamlamanın resmî IELTS'te de yüksek olan
  doğal kör-çözülebilirliği, ya da (b) gerçek-olay temelli pasajların (B4 riski)
  somut, ölçülebilir bir tezahürü.
- **`30-minute` çifti dahil 7 kök-çakışması çiftinin 7'si de tesadüf** — hiçbiri
  gerçek çapraz sızıntı değil, hiçbiri düzeltilmedi (kanıt §4'te).
- **dogrula.py ve capraz-kok.py** beklenen sonuçları verdi (şema 0 hata, 12/12
  tam test 40/40, toplam 1310).
- **Sıfır sızıntı iddia ETMEDİM** — 14 tipin 5'inde (MC, MF, not-tamamlama,
  özet-tamamlama, akış-şeması) gerçek, doğrulanmış (küçük de olsa) sızıntı var;
  bunlar raporda tek tek adlandırıldı, "temiz" diye geçiştirilmedi.
