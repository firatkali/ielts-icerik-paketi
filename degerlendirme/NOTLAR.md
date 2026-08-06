# Değerlendirme talimatı — kaynak ve karar notları

İlk sürüm. Bu klasördeki dosyalar (`yazma-task1-academic.md`, `yazma-task1-general.md`,
`yazma-task2.md`, `konusma.md`, `ORTAK-KURALLAR.md`, `cikti-semasi.json`) uygulamanın kullanıcı
cevabını puanlarken kullanacağı talimatın **ilk sürümüdür**. Ölçülmedi, düzeltilmedi:
`prompts/SONNET5-A3-puanlama-olcumu.md` ve `prompts/OPUS5-A4-puanlama-duzeltmesi.md` bu talimatı
23 resmî örnekle ölçüp düzeltecek.

---

## 1. Hangi ölçüt tanımı hangi belgeden geldi

Resmî belgelerden **cümle kopyalanmadı**; ölçüt adları ve tanımlarının özü alınıp yeniden yazıldı.

| Ölçüt | Kaynak belge | Yer |
|---|---|---|
| Task Achievement (Yazma Görev 1) | `referans/ielts-academic-writing-example-responses-to-parts-1-and-2-with-band-scores-and-examiner-comments.pdf` | Giriş bölümü, "Task 1 → Task Achievement" başlığı (sayfa 1–2) |
| Task Response (Yazma Görev 2) | aynı belge | Giriş bölümü, "Task 2 → Task Response" başlığı (sayfa 1–2) |
| Coherence and Cohesion | aynı belge | Giriş bölümü, "Coherence and Cohesion" başlığı (sayfa 1–2) |
| Lexical Resource | aynı belge | Giriş bölümü, "Lexical Resource" başlığı (sayfa 1–2) |
| Grammatical Range and Accuracy | aynı belge | Giriş bölümü, "Grammatical Range and Accuracy" başlığı (sayfa 1–2) |
| Yazmada 4 ölçütün eşit ağırlığı, yarım band raporlaması | aynı belge | "Writing responses are marked by trained and certificated IELTS examiners… Scores may be reported as whole bands or half bands" paragrafı |
| Görev 1 için 150, Görev 2 için 250 kelime alt sınırı | aynı belge | Ölçüt tanımlarının içinde geçiyor ("using the minimum of 150 words", "using a minimum of 250 words") |
| Madde imli / not biçimindeki cevabın cezalandırılması | aynı belge | Giriş, "responses will be penalised if they are (a) partly or wholly plagiarised, (b) not written as full, connected text" paragrafı |
| General Training Görev 1'in mektup olması, üç madde ve ton | `referans/ielts-general-training-writing-sample-tasks-2023.pdf` + `referans/ielts-general-training-writing-example-responses-...pdf` | Görev yönergeleri ve sınav görevlisi yorumları |
| Sınav görevlisi yorumlarının dili ve ayrıntı düzeyi | her iki "example responses" belgesi + `kalibrasyon/ornekler/yazma/*.json` (23 örnek) | Her cevabın altındaki "Examiner comment / Band N" bölümleri |

⚠️ **Sayfa numarası uyarısı.** Bu makinede `pdftoppm` yok, Read aracı PDF sayfası açamıyor; belgeler
`referans/text/` altındaki metin katmanından okundu (metin katmanı font kaydırmalı, `+29` kaydırma
ile çözüldü). Metin katmanındaki sayfa ayraçları belgeyi iki kez (en-GB / en-US katmanı) tekrar
ettiği için PDF sayfa numarası birebir doğrulanamadı. Yukarıdaki sayfa bilgisi belgenin giriş
bölümü olduğu kesin, numarası ±1 sayfa olabilir; **kesin iz başlık adıdır**, numarası değil.

### Konuşma ölçütleri — kaynak boşluğu

🔴 Konuşma ölçütlerinin resmî tanımı `referans/` altında **yok**:

- `referans/ielts-speaking-sample-tasks-2023.pdf` yalnızca Part 1/2/3 görev kartlarını ve bir örnek
  görüşme dökümünü içeriyor; ölçüt tanımı, band puanı veya sınav görevlisi yorumu içermiyor
  (metin katmanında "Fluency", "Lexical", "Grammatical", "criteria" kelimelerinin hiçbiri geçmiyor).
- Prompt dosyasının işaret ettiği `referans/konusma-band-ornekleri.txt` **diskte yok**
  (`referans/` ve `referans/text/` altında yok). Kök `NOTLAR.md` bunu zaten kaydetmiş: konuşma
  örnekleri çalıştırması hiç yapılamamış, önce `python tools/indir.py` gerekiyor.

Bu yüzden `konusma.md`'deki üç ölçüt (Fluency and Coherence · Lexical Resource · Grammatical Range
and Accuracy), IELTS'in kamuya açık konuşma ölçüt **adlarına** sadık kalınarak, band tanımları
yeniden yazılarak hazırlandı; hiçbir resmî cümle kopyalanmadı. **Sonuç: konuşma talimatı yazma
talimatı kadar sağlam dayanağa oturmuyor** ve `kalibrasyon/ornekler/konusma/` boş olduğu için
A3 ölçümünde de sınanamayacak. Konuşma band örnekleri indirilip döküldüğünde bu dosya yeniden
gözden geçirilmeli.

---

## 2. Bilinçli sadeleştirmeler

Hepsi ürün kararı; hiçbiri "resmî ölçüt böyle" diye okunmamalı.

1. **Tek JSON anahtar kümesi.** Görev 1'in resmî adı Task Achievement, Görev 2'nin adı Task
   Response; ikisi de JSON'da `task_response` anahtarını kullanıyor. Sebep: tek şema, tek rapor
   scripti. Resmî ad her dosyada başlık olarak duruyor.
2. **"Hata taşıyan cümle oranı" tablosu.** Dilbilgisi ölçütü, niteliksel tanım yerine sayılabilir
   bir orana bağlandı (≤%15 → 8-9, %15-30 → 7, %30-50 → 6, %50-75 → 5, >%75 → 4). Sebep: aynı
   cevaba her seferinde aynı puanı vermek. Resmî tanımda böyle bir eşik yok — bu bizim
   tekrarlanabilirlik için koyduğumuz vekil ölçü ve A3/A4'te ilk ayarlanacak yer burası.
3. **Tavanlar (`max N`).** Genel bakış yoksa görev yanıtı en fazla 5, paragraf yoksa tutarlılık en
   fazla 5, yan cümle hiç yoksa dilbilgisi en fazla 5 gibi kurallar resmî tanımda tek tek yazmıyor.
   Band tanımları tek başına bırakıldığında modelin yukarı kayma eğilimi var; tavanlar bu kaymayı
   engellemek için kondu.
4. **Kelime sayısı eksikliği.** Alt sınırın altındaki cevapta görev ölçütü en fazla 6, alt sınırın
   dörtte üçünün de altındaysa en fazla 5. Resmî ceza şeması bu değil (gerçek sınavda eksiklik
   görev ölçütü içinde tartılır); bu, o tartıyı sayıya çeviren bir sadeleştirme.
5. **Sözcük dağarcığında "en az dört öğe" kuralı.** 7 ve üstü için adayın kendi ürettiği, göreve
   uygun, doğru kullanılmış en az dört daha az yaygın öğe sayılabilmeli. Sayı keyfî ama sayılabilir;
   "iyi bir sözcük dağarcığı" cümlesinin önünü kesiyor.
6. **Konuşmada yetersizlik eşiği 40 kelime.** Yazmadaki 50 kelime eşiği prompt tarafından verildi;
   konuşma için karşılığı verilmemişti. Part 1 cevapları doğal olarak kısa olduğu için eşik daha
   aşağı çekildi.
7. **Konuşma hızı tablosu.** Eşikler (70/100/130/160 kelime/dakika) bizim seçimimiz. Etkisi
   **en fazla yarım band** ile sınırlandı ve döküm birincil kaynak sayıldı: hızlı ama tekrar dolu
   bir dökümü yükseltmesin, yavaş ama düzgün gelişen bir dökümü düşürmesin. Hız verilmemişse tablo
   tamamen yok sayılıyor — model hız uydurmuyor.
8. **Telaffuz yok.** Modele ses gitmiyor; talimatta hem "puanlanmaz" hem "aksan/tonlama/vurgu
   hakkında yorum yazma" diye ayrı ayrı yazıldı, şema da `pronunciation` adlı bir ölçütü reddediyor.
   Dökümde yazım ve noktalama da değerlendirilmiyor (ikisi de dökümü yapanın eseri); buna karşılık
   tekrar, kendini düzeltme, yarım bırakılan cümle ve doldurma sözcükleri geçerli kanıt sayıldı.
9. **Band 1-2 tarif edilmedi.** Tablolar 3'te bitiyor; o seviyedeki cevaplar zaten yetersizlik
   kontrolüne (`insufficient`) takılıyor. Tarif edilmeyen bandı model uydurmasın diye alt sınır
   açıkça 3'te tutuldu.
10. **Yazım → sözcük dağarcığı, noktalama → dilbilgisi.** Resmî uygulamayla aynı, ama talimatta
    açıkça yazıldı; yoksa model aynı hatayı iki ölçütte birden cezalandırıyor. Cümle sınırı hatası
    tek istisna: hata olarak dilbilgisinde sayılıyor, okunabilirliğe etkisi tutarlılıkta tartılıyor
    ve bu ayrım talimatta yazılı.
11. **Çıktı uzunluğu.** Ölçüt başına en fazla 2 cümle gerekçe, en fazla 3 düzeltme örneği, tek
    cümlelik tavsiye. Maliyetin çoğu çıktıda; sınır maliyet kararı, sonraki adımlarda gevşetilmeyecek.
12. **"Tahmini" ibaresi tek boolean.** Uzun bir uyarı cümlesi her çıktıda para yakardı; onun yerine
    şemada `"estimated": true` sabiti (şema `false` değeri reddediyor) ve talimatta yasak ifade
    listesi var ("bu senin IELTS puanın", "gerçek sınavda şunu alırsın", "kesin/resmî/garanti").
    Uyarı metnini arayüz gösterir.
13. **Ortak blokların dört dosyada tekrarı bilinçli.** Her dosya tek başına bir isteğe konabilmeli
    diye bloklar kopyalandı. `ORTAK-KURALLAR.md` bu blokların sahibi: biri değişirse dördü birden
    aynı commit'te değişecek. Ayrışmış blok varyant değil, hatadır.
14. **Yarım banda yuvarlama .25 ve .75'te yukarı.** `round(ortalama * 2) / 2`, yarımlar yukarı.
    Her dosyada işlenmiş örnek tablosu var, çünkü modeller bu aritmetiği tek satırlık tanımdan
    tutarlı uygulamıyor.

---

## 3. Telif

Depo **public**; `kalibrasyon/ornekler/` bu yüzden `.gitignore`'da. Bu klasördeki hiçbir dosyada
resmî belgeden alınmış cümle yok: ölçüt tanımları yeniden yazıldı, band tabloları özgün.
`cikti-semasi.json` içindeki örnek çıktının aday cümleleri de **uydurma** — resmî örnek cevaplardan
alıntı değil (ilk taslakta resmî bir aday metninden alıntılanmıştı, telif kuralı gereği
uydurma metinle değiştirildi). Talimatlarda geçen `levelled off`, `at your earliest convenience`
gibi ifadeler genel İngilizce, örnek cevap alıntısı değil.

## 4. Şema kendi kendini sınıyor

`tools/_a2_sema_kontrol.py` — `python tools/_a2_sema_kontrol.py`

Şemanın geçerliliğini, şemadaki iki örneğin uyduğunu ve **reddetmesi gereken** on çıktıyı gerçekten
reddettiğini sınar: 3 ölçütlü yazma çıktısı, 4 ölçütlü konuşma çıktısı, çeyrek band,
`estimated: false`, `pronunciation` adlı ölçüt, alıntısız gerekçe, 4 düzeltme örneği, şemada olmayan
alan, `insufficient` olduğu hâlde band verilmiş çıktı, sebepsiz `insufficient`. Bu oturumda **12
kontrolün 12'si geçti**. Script `jsonschema` paketi yoksa sessizce sadece JSON geçerliliğine bakar;
bu oturumda paket kuruldu (`python -m pip install jsonschema`).

---

## 5. Bu talimatın bilinen zayıf yerleri (A3 ölçümünden önce)

- **Üst bandlar.** 8-9 tanımları örnek üzerinden değil tanım üzerinden yazıldı; modelin 8,5'lik bir
  cevaba 7,5 verme riski açık. Kalibrasyon örneklerinde 8,5 band yalnızca 3 cevapta var.
- **Alt bandlar.** 3-4 aralığında elimizde az örnek var (band 3'te 1, band 4'te 2). Tavanlar bu
  aralığı aşağı çekmek için kondu ama sınanmadı.
- **Konuşma hiç ölçülemeyecek** (yukarıdaki kaynak boşluğu): `kalibrasyon/ornekler/konusma/` boş.
- **Görev 1 görselinin doğruluğu.** Talimat, adayın verdiği sayıyı `visual` alanına bakarak kontrol
  ediyor. `visual` eksik gelirse talimat "kontrol edemediğini cezalandırma" diyor — yani eksik
  görsel sessizce cömertliğe dönüşür. Uygulama tarafında `visual` her zaman gönderilmeli.
