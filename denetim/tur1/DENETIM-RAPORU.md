# DENETİM RAPORU

- **Tarih:** 2026-08-07
- **Denetleyen:** Fable (Claude ailesi) — bağımsız denetçi gözüyle, 3. ve son çalıştırma
- **Kaynaklar:** `denetim/envanter.md` · `denetim/capraz-ozet.md` · `kalibrasyon/olcum/SONUC.md` ·
  `content/DOGRULAMA/RAPOR.md` · `content/DOGRULAMA/METINSIZ-RAPOR.md` ·
  `content/DOGRULAMA/OLCU-reading.md` (+ ham ölçüm: `kalibrasyon/olcu/reading.json`, `resmi.json`)
- **Kural:** Bu rapor durum tespiti yapar, karar vermez. Hiçbir içerik dosyası değiştirilmedi;
  bütün eleme/kabul kararları proje sahibinindir.

---

## 1. Genel durum

Üretim hedefin tamamını karşıladı (1.310/1.310 soru + bütün pasaj ve senaryolar) ve cevap
anahtarları çapraz kör çözümde içerik düzeyinde pratikte %100 doğrulandı; dinleme, konuşma ve
yazma envanteri bugün teslim edilebilir durumda. Okuma ise değil: parçasız çözüm ölçümü okuma
havuzunun %47'sini (180 soru) "parça okunmadan çözülebiliyor" diye işaretledi ve üç soru tipinin
kullanılabilir stoku fiilen sıfıra indi — okuma, işaretliler hakkında karar verilmeden (at /
elden geçir / yeniden üret) teslim edilemez. Puanlama tarafında yazma değerlendirmesi üç
düzeltme turuyla belirgin iyileşti ama 4 kabul ölçütünden hâlâ 2'sini karşılamıyor; konuşma
puanlaması ve dinlemenin sızıntı ölçümü ise hiç yapılmadı, yani oralarda "sorun yok" değil
"bilgi yok" durumundayız.

---

## 2. Sayılar

Kaynak: `denetim/envanter.md` (ayrıntılı tablolar orada).

| Beceri | Hedef | Üretilen | İşaretli | Kullanılabilir | Durum |
|---|---:|---:|---:|---:|---|
| Okuma | 400 | 400 | 180 | **220** | 🔴 hedefin 180 altında |
| Dinleme | 360 | 360 | 0 | 360 | ✅ (ama sızıntı ölçümü yapılmadı — bkz. §3) |
| Konuşma | 440 | 440 | 0 | 440 | ✅ (ölçüm kapsamı dışında) |
| Yazma | 110 | 110 | 0 | 110 | ✅ (ölçüm kapsamı dışında) |
| **Toplam** | **1.310** | **1.310** | **180** | **1.130** | |

Destek malzemesi tam: 12/12 okuma pasajı, 6/6 GT metin seti, 24/24 dinleme senaryosu.
Test yerleşimi tam: 6 okuma + 6 dinleme testinin her biri 40 soru. Boş cevap anahtarı ve boş
açıklama yok.

Okumada kullanılabilir stokun tipe göre en kritik yerleri:

| Soru tipi (test + alıştırma) | Üretilen | Kullanılabilir |
|---|---:|---:|
| YES / NO / NOT GIVEN | 23 | **0** |
| Cümle sonu eşleştirme | 10 | **0** |
| Özellik eşleştirme | 26 | **8** |
| Çoktan seçmeli | 39 | **9** |
| Özet tamamlama | 43 | 17 (kelime bankalı alt tipte 0) |
| TRUE / FALSE / NOT GIVEN | 57 | 27 |

Sayım dışı iki pürüz: (a) 2 soru `status: "review"`da askıda ve 180'e dahil değil
(`practice/matching-headings` 9, `GT1/matching-information` 3); (b) 22 sorunun `evidence`
alanı boş — hepsi NOT GIVEN cevaplı, yani yapısal olarak beklenen bir boşluk, ama kalite
kuralı "kanıt zorunlu" diyor (dökümü envanter raporunda; 12'si zaten işaretli).

---

## 3. Kalite

Üç ayrı mekanizma çalıştı; farklı şeyleri ölçtüler ve birlikte okununca tablo net.

**Cevap anahtarları doğru.** Çapraz kör doğrulama (üretmeyen model, anahtarı görmeden, 743
soru) içerik düzeyinde pratikte %100 uyuştu. Bulunan 25 işaretin 1'i yanlış alarm, 24'ü
rakam↔yazı / tarih biçimi / belirteç türü anahtar-esnekliği eksiğiydi ve **24'ünün de dosyada
kapatıldığı bu denetimde doğrulandı.** Çapraz doğrulamadan açık kalan tek anahtar eksiği yok;
açık kalan tek anahtar maddesi METINSIZ ölçümünden geliyor (aşağıda, açık sorun A4).

**Ama soruların yarısı parçaya muhtaç değil.** Parçasız çözüm ölçümü (381 okuma sorusu, üçer
tur): 180 soru (%47) üç turun üçünde de parça gösterilmeden doğru bilindi. Genel oran resmî
sınav tabanının (%57) altında — havuz bütün olarak resmî sorulardan daha az sızdırıyor — ama
sorun dağılımda:

| Sağlam tipler | Şüpheli tipler |
|---|---|
| Bilgi eşleştirme **%6** · başlık eşleştirme %18 · kısa cevap %20 · not tamamlama %27 · tablo %33 · cümle tamamlama %35 | Çoktan seçmeli **%100** · YES/NO/NOT GIVEN **%100** · cümle sonu eşleştirme **%100** · kelime bankalı özet **14/14** · özellik eşleştirme %69 · akış şeması %67 · TFNG %53 |

İşaretler dağınık tekil hatalar değil, **iki üretim ailesine göre ayrışan iki sistematik
desen** (ayrıntı `denetim/capraz-ozet.md` §4-5):

1. **Fable yuvaları (seçenek metinli tipler): kip imzası + konumsal düzen.** Doğru cevap hep
   ölçülü ("may", "probably"), çeldirici hep mutlak ("clearly", "only") yazılmış; ayrıca iki
   cevaplı MC'de A ve G şıkkı 9 sorunun 9'unda da çeldirici, {C,F} çifti 4 kez doğru. İki ayrı
   tipte aynı imza → prompt alışkanlığı, prompt düzeyinde düzeltilebilir.
2. **Opus yuvaları (tamamlama ailesi): eşdizim kilidi + terim/tanım sızıntısı.** Boşluk ya
   kalıp öbeğin tahmin edilen ucunda ("an up-to-date ___" → CV) ya da alanın tek karşılıklı
   stok teriminde (displacement, surge); kelime bankalı özette banka tanım/zıt-çift sızdırıyor.
   Aynı ailenin sayısal/parçaya-özgü boşlukları tutarlı biçimde sağlam — sorun tipte değil,
   boşluğun nereye açıldığında.

İki mekanizmanın kesişmemesi önemli: çapraz doğrulamada en temiz çıkan tipler ile parçasız
ölçümde en kötü çıkanlar aynı. Çelişki değil — bu soruların **cevabı doğru ama kendisi
gereksiz**; anahtar denetimi bu kusur sınıfını yapısal olarak göremez.

**Sayısal ölçüler tabloyu doğruluyor.** Sözcüksel örtüşme ölçümünde (`OLCU-reading.md`) 6 tip
resmî çapadan ±%10 dışında; MC ve cümle sonu eşleştirme "fazla örtüşen" (sahte-kolay) yönünde
sapıyor — parçasız ölçümün %100 verdiği tiplerle aynı. En yüksek örtüşmeli 10 sorunun 8'i,
birbirinden habersiz iki yöntemce de işaretlenmişti; bu, 180 işaretin güvenilirliğini artırır.

**Üç dürüstlük notu:**

- **Tamamlama ailesinin oranları iyimser.** Ölçüm "3/3 kelimesi de tuttu" sayıyor; anlam
  düzeyinde cümle tamamlama %81, parçadan-kelime özet %93 biliniyordu — puanı kurtaran şey
  kavrayış değil, "parçadan kelime kopyala" kuralının kelime tutturmayı zorlaştırması. Mevcut
  ölçüt sızıntının yarısını görmüyor (METINSIZ 8. çalıştırmanın kendi tespiti).
- **Dinleme/konuşma/yazma hiç sızıntı ölçümüne girmedi.** Dinlemedeki "0 işaret" temizlik
  değil, ölçülmemişlik. Özellikle dinleme MC + eşleştirme (`FABLE5-43`, 96 soru), okumada
  %100 sızdıran prompt ailesinden geliyor — desen sistematikse orası da risk altında, veri yok.
- **`flag_reason` alanları güvenilmez.** 180 işaretin hepsinde birebir aynı cümle ("genel
  kültürle çözülebiliyor") yazıyor; oysa `blind_basis` alanına göre 180'in 108'inde gerçek
  mekanizma başka (logic / seçenek yazımı / tahmin). Elden geçirme bu metne göre yapılırsa
  yanlış yöne gider.

---

## 4. Puanlama

Kaynak: `kalibrasyon/olcum/SONUC.md`. Üç ölçüm turu + iki düzeltme, tamamı **yazma** üzerinde
(23 örnek; konuşma örneği hiç yok).

| # | Ölçüt | Hedef | tur 1 | tur 3 | Sonuç |
|---|---|---|---|---|---|
| 1 | Ortalama mutlak fark | < 0,5 band | 0,952 | 0,694 | 🔴 kaldı (hedefin %39 üstünde) |
| 2 | En büyük tek sapma | < 1,5 band | 2,00 | 1,50 | 🔴 kaldı (sınıra sıfır payla) |
| 3 | Eğilim | ±0,25 içinde | −0,667 | −0,139 | ✅ geçti |
| 4 | Aynı cevapta yayılım | ≤ 0,5 | 0,33 | 0,19 | ✅ geçti |

Payların dürüst okunuşu:

- **Gerçek iyileşme var:** sapma 0,95'ten 0,69'a indi, ≥1,5 band sapan örnek 7'den 1'e düştü,
  puanların %94'ü artık gerçek banddan en fazla 1 band uzakta. Saklı küme kontrolü temiz —
  ezber işareti yok (fark 0,032 band).
- **Ama tur 3 eksik ölçüldü:** 23 örneğin 18'i puanlandı; puanlanamayan GT-T2 grubu önceki
  turlarda ortalamanın üstünde sapıyordu (−2,0'lık en büyük iki sapma o grupta). Başlık
  sayıları bu yüzden **iyimser taraflı**; ölçüt 2'nin gerçek durumu o 5 örnek puanlanmadan
  bilinemez.
- **Eğilimin geçmesi yanıltıcı olabilir:** üst bandda hâlâ cimri (−0,79), alt bandda şişkin
  (+1,25); −0,139'luk genel eğilim iki zıt hatanın ortalamada birbirini götürmesi. En
  tehlikeli tek bulgu alt band: gerçek bandı 3,0 olan cevaba ürün 4,5 veriyor — kullanıcı
  **hazır olmadığı hâlde hazır sanır**. Bu, 2. düzeltmenin yan hasarı (tur 2'de +0,50 idi) ve
  o aralıkta yalnız 2-3 örnek olduğu için büyüklüğü de belirsiz.
- **Kapsam sınırı:** bu sayıların hiçbiri konuşma puanlaması için geçerli değil (konuşma hiç
  ölçülmedi, tavan değerlerine hiç dokunulmadı) ve okuma/dinlemedeki "kaç doğru = hangi band"
  eşiğini doğrulamaz — o eşik yalnız canlı kullanım verisiyle sınanabilir. "Tahmini band"
  ibaresi üründen kalkamaz.

---

## 5. Açık sorunlar — proje sahibinin karar vereceği maddeler

Hiçbiri "yapıldı" değildir; her maddede seçenekler yazılıdır, karar proje sahibinindir.

**A1 — 180 işaretli okuma sorusu (en büyük madde).** Okuma stoku 220/400'e düştü; YNNG, cümle
sonu eşleştirme ve MC fiilen tükendi. Seçenekler: (a) işaretlileri at ve eksikleri kabul et;
(b) mekanizma bazında elden geçir — kip imzası ve eşdizim kilidi mekanik düzeltmeye uygun
(~73 + ~20 soru), genel-kültür temalılar (~72) soru ekseni değişikliği ister; (c) %100
işaretli üç tipte düzeltilmiş promptlarla yeniden üretim. Öneri: (b)+(c) karışımı — kip
imzalı ve eşdizim kilitli sorular elden geçirilebilir; konu-seçimi kusurlu olanlarda yeniden
üretim daha ucuz olabilir.

**A2 — `flag_reason` metinleri yanlış yönlendiriyor.** 180 kaydın hepsi aynı tek cümle;
108'inde gerçek mekanizmayla çelişiyor. A1'de elden geçirme seçilecekse önce gerekçeler
`blind_basis` + METINSIZ dökümünden düzeltilmeli; yoksa düzeltici yanlış kusuru "düzeltir".

**A3 — Dinleme sızıntı ölçümü yapılmadı.** 360 dinleme sorusunun tamamı sızıntı açısından
ölçüsüz; `FABLE5-43` yuvası (MC + eşleştirme, 96 soru) okumada %100 sızdıran prompt ailesiyle
akraba. Seçenekler: ölçümü dinlemeye (en azından bu yuvaya) genişlet / dinlemeyi mevcut
hâliyle kabul edip riski belgele. Not: dinlemede "parça" ses metni olduğundan ölçüm tasarımı
okumadakinden farklı olacaktır.

**A4 — Tek açık anahtar eksiği:** `AC2/flow-chart-completion` soru 1 — yönerge sayıya izin
veriyor ama `accepted_variants` yalnız `forty minutes`; `40 minutes` eklenmezse aday haksız
puan kaybeder. (METINSIZ turunun ölçümü geriye dönük bozmamak için bilinçli ertelediği tek
düzeltme; tek satırlık iş.)

**A5 — 2 soru `status: "review"`da askıda** (`practice/matching-headings` 9,
`GT1/matching-information` 3; sözcüksel örtüşmeleri 1.0). Seçenekler: elden geçirip
`verified`/`flagged` yap / işaretli say. Şu an hiçbir sayıma girmiyorlar.

**A6 — 22 NOT GIVEN sorusunda `evidence` boş.** Kalite kuralı "kanıt zorunlu" diyor; NOT
GIVEN'da kanıt cümlesi doğası gereği yok. Seçenekler: kuralı "NOT GIVEN hariç" diye güncelle /
alana "bilgi pasajda yok" tipi negatif gerekçe yazdır. (22'nin 12'si zaten işaretli.)

**A7 — Tamamlama ailesinde ölçüt sızıntının yarısını görmüyor.** "3/3 kelimece doğru" yerine
"3/3 anlamca doğru" ölçütüyle cümle tamamlamada 19, özet ailesinde 15 soru daha işaretlenirdi.
Seçenekler: anlam-düzeyi ölçütüyle ek bir işaretleme turu / mevcut işareti yeterli say ve
riski belgele. (Kabul edilirse A1'deki sayı büyür — bunu bilerek karar verilmeli.)

**A8 — Puanlama tur 3 eksik: GT-T2 grubu (5 örnek × 3 tekrar) puanlanmadı.** Ölçüt 2'nin
gerçek durumu bilinmiyor. Seçenek: `SONNET5-A3` talimatıyla (ölçüm bilerek Sonnet'le yapılır)
GT-T2 puanlanıp `python tools/puanlama-raporu.py 3` yeniden çalıştırılır — mevcut altyapıyla
yapılabilir, bekleyen tek şey çalıştırma kararı.

**A9 — Alt band şişmesi (puanlamanın en tehlikeli bulgusu).** Zayıf cevaba fazla puan →
kullanıcı sınava erken girer. Bir sonraki düzeltme turunun birinci maddesi olmalı; ama ≤4,5
aralığında yalnız 3 örnek var — düzeltmeden **önce** alt band örneği çoğaltılmalı, yoksa
düzeltme yine körlemesine olur.

**A10 — Konuşma puanlaması hiç ölçülmedi.** `kalibrasyon/ornekler/` altında konuşma örneği
yok; konuşma ölçütlerine yapılan bütün değişiklikler yazmadan genellendi, tavan değerleri
ayarsız. Seçenekler: konuşma örnek seti kurup ölçüm turu yap / konuşma puanlamasını "hiç
kalibre edilmedi" ibaresiyle yayınla.

**A11 — Kabul ölçütleri karşılanmadan yayın kararı.** Ortalama mutlak fark 0,694 (hedef
< 0,5). Seçenekler: yeni bir düzeltme turu (A9 ile birlikte) / hedefi gevşetip ürünü "±1 band
doğruluğunda" diye dürüstçe etiketle. Mevcut talimatla hedefe ulaşılacağına dair veri yok.

**A12 — Araç borçları (küçük ama tekrarlayan):** `tools/kor-kopya.py` `dogrulama/cevap/`
klasörünü temizlemiyor — aynı karışıklık dört oturumda tekrarladı; `tools/puanlama-raporu.py`
raporu kümeye bölmediği için saklı küme koruması tur 2'de deliniyordu. İkisi de bilinen,
kapatılmamış iş.

---

## 6. Denetimin sınırları

Bu denetimin göremediği şeyler, dürüstçe:

1. **Denetçi, üreticilerle aynı model ailesinden.** Soruları Fable ve Opus üretti, çapraz
   doğrulamayı yine bu ikili yaptı, bu raporu Fable yazdı. Ailenin ortak kör noktası varsa —
   iki modelin de doğru sandığı yanlış bir cevap, ikisinin de doğal bulduğu bir kusur — bu
   kurulumun **hiçbir aşamasında** görünmez. Cevap doğruluğunun son sözü, planlandığı gibi
   farklı aileden bir modelle yapılacak ikinci süzgeçtedir; puanlama için de aynısı geçerli
   (talimatı yazan, örnekleri metne döken ve puanlayan hep aynı aile).
2. **Bu denetim raporları denetledi, soruları değil.** Envanter sayımı dosyalardan yeniden
   yapıldı ve 24 varyant düzeltmesinin dosyaya işlendiği tek tek doğrulandı; ama 1.310 sorunun
   içeriği bu denetimde yeniden çözülmedi. Önceki raporlarda gözden kaçan bir şey varsa burada
   da kaçmıştır.
3. **Ölçülmeyen yerler hakkında bu rapor sessizdir:** dinlemenin sızıntısı (A3), konuşma
   puanlaması (A10), konuşma/yazma içeriğinin kalitesi (hiçbir sızıntı/doğruluk ölçümü bu iki
   beceriye uygulanmadı; konuşma-yazma "temiz" değil, "ölçülmemiş"), diyagram etiketleme
   (görsel gerektirdiği için metin tabanlı ölçüm kör) ve okuma/dinlemede "kaç doğru = hangi
   band" eşiği (yalnız canlı veriyle sınanabilir).
4. **Karşılaştırma tabanları küçük.** Resmî sızıntı tabanı tip başına 3-6 soru, sözcüksel
   örtüşme çapası tek belgeden 116 çift, puanlamada band başına 1-4 örnek. Yönler güvenilir,
   büyüklükler değil.
5. **"Gerçek sınav zorluğunda" iddiası bu projede hiçbir yöntemle doğrulanamadı** — parçasız
   ölçüm bozuk soruyu bulur, zorluğu ölçmez; zorluk ancak binlerce gerçek adayın verisiyle
   ölçülür.
6. Küçük bir talimat uyuşmazlığı kaydı: bu çalıştırmanın talimatı "kalibrasyon/olcu/ altındaki
   sayısal ölçü raporları" der; o klasörde yalnız ham JSON var, okunabilir rapor
   `content/DOGRULAMA/OLCU-reading.md`'dedir. Denetim ikisini de kullandı.
