# Değerlendirme talimatı — düzeltme kaydı

Her satır: **hangi örüntü → hangi değişiklik → beklenen etki**. Bir sonraki ölçüm turu bu
beklentileri sınar. Değişiklik gerekçesi ölçümden gelmiyorsa buraya yazılmaz.

---

## 1. düzeltme — 2026-08-07

| | |
|---|---|
| Ölçüm | `kalibrasyon/olcum/RAPOR-tur1.md` (tur 1, her örnek 3 tekrar) |
| Görülen kümeler | **S1 + S2** (14 örnek × 3 puanlama) |
| SAKLI küme | **S3** — bu oturumda o kümenin hiçbir örneğine, gerçek bandına, sapma satırına bakılmadı |
| Değişen dosyalar | `ORTAK-KURALLAR.md`, `yazma-task1-academic.md`, `yazma-task1-general.md`, `yazma-task2.md`, `konusma.md` |

### 🔴 Ölçümün eksikliği (bu düzeltmenin dayanağı hakkında)

Tur 1 **tamamlanmadan** bu adıma gelindi: 23 örnekten **21'i** puanlandı (63/69 puanlama).
Eksik olan iki örnek `GT-T2-2B-B` ve `GT-T2-2B-C`; ikisi de görünür kümelerde (S1 ve S2), yani
saklı küme bu eksikten etkilenmiyor. `tools/puanlama-raporu.py 1` bu 21 örnek üzerinden
çalıştırıldı ve RAPOR-tur1.md eksik veriyle üretildi. Puanlamayı bu oturum **yapamaz**: ölçüm
Sonnet ile yapılır (bkz. `prompts/SONNET5-A3-puanlama-olcumu.md` başlığı), bu oturum Opus.
Eksik iki örnek 2. ölçüm turunda kapanacak. Aşağıdaki örüntüler 14 görünür örneğin 42 puanlamasına
dayanıyor ve hepsi tek tek örneğe değil, **band aralığı × ölçüt** kırılımına dayanıyor.

Ayrıca: kök `NOTLAR.md`, ölçüm turunun her grubu için **tahmin edilen** bandları listeliyor
(gerçek bandları veya sapmaları değil). Bu oturum saklı kümenin gerçek bandına ve sapmasına
bakmadı; saklı küme karşılaştırması hâlâ geçerli.

### Ölçüm ne dedi

Tek seferlik puan üzerinden, görünür kümeler (S1+S2, n=14): ortalama mutlak fark **0,93 band**,
eğilim **−0,57 band** (cimri), en büyük tek sapma **2,0 band**, aynı cevaptaki yayılım **0,33**.
Dört başarı ölçütünden yalnız tutarlılık geçti.

Örüntü, tek yönlü bir cimrilik değil — **ölçeğin ortaya doğru büzülmesi**:

| Gerçek band | Ölçüt sapmaları (ölçüt bandı − gerçek genel band) |
|---|---|
| ≥ 7 | görev −1,80 · tutarlılık −1,73 · kelime −1,23 · dilbilgisi −1,73 |
| 5 – 6,5 | görev −0,26 · tutarlılık −0,21 · kelime −0,36 · **dilbilgisi −0,95** |
| ≤ 4,5 | görev **+1,33** · tutarlılık +0,92 · kelime +0,58 · dilbilgisi +0,33 |

Gerçek bandlar 3,0–8,5 arasında yayılırken verilen tek seferlik puanların **tamamı 4,0–6,5**
aralığına düştü. Yani: üst bandlar sıkışıyor **ve** alt bandlar şişiyor. Alt band şişmesi
tehlikeli olan taraf: hazır olmayan kullanıcı hazır sanır.

İki ek örüntü:

1. **Cimriliğin en büyük tek kaynağı tavanlar (caps).** Puanlama gerekçelerinde tavan koşulu
   tetiklendiğinde model tavan değerini **puan olarak** yazıyor. Aynı mekanizma iki yönde birden
   hata üretiyor: güçlü cevapta tek bir tavan koşulu bandı 5'e çekiyor, zayıf cevapta ise tavan
   bir **taban** gibi çalışıp cevabı 5'e yükseltiyor. Tavan koşullarının kendisi de tartışmayla
   tetikleniyordu (ör. "genel bir bakış yok", "açık bir tutum yok" kararları, gerçek sınav
   görevlisinin aynı cevapta görmediği yerlerde veriliyordu).
2. **Dilbilgisi ölçütü ayrıca ve toplamalı olarak sert.** Diğer üç ölçütün doğru olduğu orta
   bandda bile −0,95. Hata payı tablosunun eşikleri, "içinde en az bir hata olan cümle" sayımıyla
   birlikte, temiz ama küçük kusurlu metni bir band aşağı itiyor.

### Yapılan değişiklikler

| # | Örüntü | Değişiklik | Beklenen etki |
|---|---|---|---|
| 1 | Tavan değeri puan olarak kullanılıyor; alt bandlar 5'e şişiyor | ADIM 2'ye tavan tanımı eklendi: tavan **yalnızca üst sınır**, "max 5" = "5 veya altı"; tablodan okunan band ile tavanın **düşüğü** alınır; tavan hiçbir zaman bandı yükseltmez. Aynı ölçütte iki tavan birden tetiklendiyse band tablodan okunur | Alt bandlarda görev ölçütünün +1,33'lük şişmesi kapanır; gerçek band 3–4 olan cevaplar 4,5–5 yerine 3–4 alır |
| 2 | Tavanlar tartışmayla, zorlanarak tetikleniyor | Aynı kurala tetikleme eşiği eklendi: tavan ancak koşul bu cevapta **açıkça doğruysa** ve kanıtı gösterilebiliyorsa işler; savunmak gerekiyorsa işlemez | Üst bandlarda görev ölçütünün −1,80'lik çöküşü azalır |
| 3 | Ölçütler arası eşik davranışı hep aşağı yuvarlıyordu ("iki band arasındaysa düşüğünü al") | Kural değişti: iki band arasındaysa **aradaki yarım band** verilir; alt tam banda ancak üst bandın çekirdek koşulu hiç karşılanmadığında inilir | Sistematik cimriliğin ~0,25 bandlık kısmı kalkar; ölçüt düzeyinde çözünürlük artar |
| 4 | Puanlar 4,0–6,5'e büzülüyor, ölçeğin uçları hiç kullanılmıyor | ADIM 2'ye ölçek kullanımı kuralı eklendi: 3–9 arasındaki her band olağan bir sonuçtur; belirsizlik ortaya kaçmak için gerekçe değildir; 5 ve 6 varsayılan iniş yeri değildir | Hem üst hem alt uçta büzülme azalır; dağılım gerçek dağılıma yaklaşır |
| 5 | Dilbilgisi ölçütü her bandda ~1 band sert | Hata payı tablosunun eşikleri yaklaşık 10 puan yukarı kaydırıldı (8–9: ≤%20, 7: %20–40, 6: %40–60, 5: %60–80, 4: >%80) ve tabloya yorum eklendi: hata taşıyan cümle başarısız cümle değildir, 5 ve altı için anlamın gerçekten bozulması gerekir | Dilbilgisinin −1,05'lik sapması ~0 civarına iner; orta bandın genel puanı yaklaşık +0,25 yükselir |
| 6 | "Okuyucuyu tahmine zorlayan hata **ikiden fazla** → max 5" mutlak sayımı uzun ve iyi metni cezalandırıyor | Oransal hâle getirildi: cümlelerin **beşte birinden fazlası** yeniden okunmak zorundaysa; sayılacak olan hatalı cümle değil, yeniden okunması gereken cümle | 250+ kelimelik güçlü metinlerde dilbilgisinin 5'e çakılması biter |
| 7 | Kelime ölçütünde 7 kapısı yalnız aşağı çalışıyordu ("dört tane sayamıyorsan 6 veya altı") | Kural çift yönlü yapıldı: dördü sayabiliyorsan 7 **açıktır** ve genel izlenimle geri çekilemez; sekiz veya daha fazlası doğru kullanılmışsa 8'i destekler | Üst bandda kelime ölçütünün 6–7'ye çakılması azalır |
| 8 | Görev ölçütünün tavan koşulları, sınav görevlisinin görmediği yerde tetikleniyor | Koşulların tanımı netleştirildi (örneğe özel kural değil, tanım): genel bakış her yerde ve *Overall* etiketi olmadan da olabilir · tutum, taraf tutmayan gerekçeli bir sonuç da olabilir · bir madde "işlenmiş" sayılmak için ayrı paragraf gerektirmez, dolaylı karşılık da sayılır | Üst bandda görev ölçütünün tek başına 5'e düşmesi biter |
| 9 | Talimattaki örnek JSON çıktısı somut band değerleri içeriyordu (ör. 5/5/5/4); ölçümde puan vektörü zaman zaman bu örneğe birebir eşitti | Örnek çıktıdaki bütün band değerleri `<band>` yer tutucusuna çevrildi; "örnek yalnız **biçim** gösterir" notu eklendi. `ORTAK-KURALLAR.md` BLOK J'ye bir daha somut sayı konulmaması kuralı yazıldı | Çıktı örneğinin çapa etkisi kalkar; benzer cevaplara verilen aynı vektör azalır |
| 10 | Rol metni tek yönlü sertlik telkin ediyordu ("You are strict… şişirilmiş tahmin en kötü sonuç") | Rol metni simetrik hâle getirildi: amaç doğru bandı bulmak; şişirme de düşürme de kullanıcıya zarar verir, ikisi de "güvenli taraf" değildir | Sistematik −0,57'lik eğilimin bir kısmı kapanır |

Değişiklik 1–4 ve 9–10 **her beş dosyada** aynı; 5–7 dört puanlama talimatında aynı (hata payı
tablosu `ORTAK-KURALLAR.md`'ye **BLOK K** olarak alındı, dört dosyada aynen tekrarlanıyor);
8 her görev türünde kendi ölçütünün diline göre yazıldı.

### Bilerek yapılmayanlar

- **Örneğe özel hiçbir kural yazılmadı.** Hiçbir örnek kodu, cevabı, gerçek bandı veya konusu
  talimata girmedi. Bütün değişiklikler band aralığı × ölçüt kırılımına dayanıyor.
- Ölçüt sayısı ve ağırlığı değişmedi (yazma 4, konuşma 3).
- Telaffuz geri getirilmedi; konuşmada yine üç ölçüt var.
- Çıktı uzunluğu sınırları değişmedi.
- `cikti-semasi.json` değişmedi: makine sözleşmesi aynı, üretilen alanlar aynı. Şemadaki
  örnek dolu bir puanlamadır ama şema dosyası puanlayan modele **gönderilmiyor** (talimat
  dosyaları standalone), o yüzden çapa etkisi yok.

### 🔴 Konuşma tarafı ölçülmedi

`kalibrasyon/ornekler/` altında **konuşma klasörü hiç yok** (yalnız `yazma/` var): bu turda
puanlanan 21 örneğin hepsi yazma.
`konusma.md`'ye yapılan değişiklikler ortak blokların senkron tutulması kuralından geliyor
(`ORTAK-KURALLAR.md` bakım kuralı) ve yazma verisinden **genellenmiş** durumda — konuşmada
ölçülmüş bir örüntüye dayanmıyor. Konuşma puanlamasının sapması bu projede **hâlâ ölçülmemiştir**;
son raporda kalan risk olarak yazılmalı.

### Sınanacak beklenti (tur 2)

1. Eğilim −0,57'den **0'a doğru** hareket etmeli (hedef ±0,25 içi).
2. En büyük tek sapma 2,0'ın **altına** inmeli.
3. Tek seferlik puanlar 4,0–6,5 aralığından çıkmalı; gerçek band ≥7 olan örneklerde en az bir
   7 veya üstü, gerçek band ≤4 olan örneklerde en az bir 4 veya altı görülmeli.
4. Orta bandın (5–6,5) şu anda tutan doğruluğu **bozulmamalı** — asıl risk bu: 5 ve 10 numaralı
   değişiklikler orta bandı cömertliğe kaydırırsa düzeltme yanlış yöne gitmiştir.
5. Saklı küme (S3) ile görünür kümeler arasındaki fark **açılmamalı**. Açılırsa ayar örneklere
   ezberlenmiştir.
