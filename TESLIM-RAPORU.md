# Teslim raporu — 2026-08-06

## Özet
| Beceri | Hedef | Üretilen | Fark |
|---|---|---|---|
| Okuma | 400 | 400 | 0 |
| Dinleme | 360 | 360 | 0 |
| Konuşma | 440 | 440 | 0 |
| Yazma | 110 | 110 | 0 |
| **TOPLAM** | **1.310** | **1.310** | **0** |

Kaynak: `python tools/manifest.py` çıktısı (`content/MANIFEST.json`).

## Tam testler
| Test | Soru | Durum |
|---|---|---|
| AC1 | 40/40 | tam |
| AC2 | 40/40 | tam |
| AC3 | 40/40 | tam |
| AC4 | 40/40 | tam |
| GT1 | 40/40 | tam |
| GT2 | 40/40 | tam |
| L1 | 40/40 | tam |
| L2 | 40/40 | tam |
| L3 | 40/40 | tam |
| L4 | 40/40 | tam |
| L5 | 40/40 | tam |
| L6 | 40/40 | tam |

Kaynak: `python tools/dogrula.py` → "TAM TEST BUTUNLUGU" bölümü.

## Çapraz doğrulama
(`content/DOGRULAMA/RAPOR.md` — sekiz oturumluk kör çapraz doğrulama arşivi)

| Paket | Toplam | İşaretli (o oturumda) | Oran |
|---|---|---|---|
| Okuma TFNG + YNNG | 80 | 0 | %100,0 |
| Okuma çoktan seçmeli (+ dinleme çoktan-seçmeli-çoklu) | 35 | 0 | %100,0 |
| Okuma eşleştirme (başlık+özellik+cümle sonu) | 81 | 0 | %100,0 |
| Dinleme çoktan seçmeli + eşleştirme | 83 | 0 | %100,0 |
| Okuma tamamlama tipleri (7 alt tip) | 151 | 2 | %98,7 |
| Okuma bilgi eşleştirme | 49 | 0 | %100,0 |
| Dinleme form/plan/tamamlama paketleri | 264 | 23 | %91,3 (içerik uyuşması %99,6) |
| **TOPLAM (çapraz doğrulanan)** | **743** | **25** | **%96,6** |

> Not: Çapraz doğrulama, üretilen 1.310 sorunun okuma+dinleme+alıştırma kısmını
> (toplam 743 soru) kapsar; konuşma ve yazma (550 birim) cevap anahtarı taşımadığı
> için bu yöntemle doğrulanmaz, `python tools/dogrula.py` şema kontrolünden geçmiştir.

## Açık işler
Yok. Plandaki (`content/PLAN-soru-dagilimi.md`) tüm paketler üretildi ve hedef
sayılara tam ulaşıldı; yeniden çalıştırılması gereken prompt kalmadı.

## Şema hataları (düzeltilemeyenler)
Yok — `python tools/dogrula.py` 0 şema hatası ile temiz çıktı.

## İşaretli (flagged) sorular
Bu oturumdan önce 25 soru işaretliydi (bkz. `content/DOGRULAMA/RAPOR.md`, son iki
çapraz doğrulama oturumu). İnceleme, 24'ünün içerik hatası değil **eksik
`accepted_variants`** olduğunu gösterdi (rakam/yazı biçimi — `5`↔`five`; tarih/saat
biçimi — `2nd`↔`second`; belirteç — `(the) water table`; boşluk — telefon/referans
numaraları; bir sette de kelime sınırının izin verdiği ek sıfat — `seven distinct`).
Bunlar `content/DOGRULAMA/RAPOR.md`'deki tabloda birebir belgelenmişti; bu oturumda
her birine belgelenen varyant eklendi ve durum `verified`e çevrildi. Kalan 1 soru
(`content/reading/practice/short-answer.json` #5) yanlış alarmdı —
`accepted_variants` zaten doğru değeri içeriyordu, önceki doğrulama scripti yalnızca
`answer` alanına bakmıştı; durumu `verified`e çevrildi, içerik değişmedi.

Sonuç: **0 işaretli soru kaldı.**

## Telif kontrolü
- Pasaj lisansları: hepsi dolu (19 pasaj, 0 eksik).
- "IELTS" geçen kullanıcı metni: yok.
- Yasak kaynak adı (Cambridge / British Council / IDP / Wikipedia / The Conversation)
  geçen dosya: yok.

## Araç düzeltmesi
`tools/manifest.py`, `content/speaking/part2-3/*` (sorular `part3.items` altında,
üst seviyede değil) ve `content/writing/*` (tekil görev dosyaları, `items` alanı yok)
dosyalarındaki soru/birim sayısını **0** olarak hesaplıyordu; bu yüzden ilk çalıştırmada
"konuşma -240, yazma -110 eksik" gibi yanlış bir fark raporu üretiyordu. İçerik
tarafında eksik yoktu — hata yalnızca sayaç mantığındaydı (`dogrula.py`'deki doğru
`konusma_yazma_denetle` mantığıyla karşılaştırılarak doğrulandı). `tools/manifest.py`
düzeltildi; `content/MANIFEST.json` artık tüm becerilerde hedefle birebir eşleşiyor.

## Proje sahibine notlar
- **Sistematik kalite sorunu yok.** Sekiz çapraz doğrulama oturumunda (743 soru)
  gerçek bir içerik hatası (yanlış cevap, savunulamayan tek-cevap iddiası, kanıtsız
  soru) çıkmadı. Bütün uyuşmazlıklar cevap anahtarı biçimiyle ilgiliydi ve bu oturumda
  kapatıldı.
- **Öneri (opsiyonel, bu teslimde yapılmadı):** `content/DOGRULAMA/RAPOR.md`'de not
  edildiği gibi, tamamlama tiplerinin tamamında (yalnızca işaretlenenlerde değil)
  `accepted_variants` alanı rakam↔yazı, belirteç ve tarih/saat biçimi için topluca
  bir kez taranırsa, gerçek sınav puanlamasına daha yakın bir otomatik değerlendirme
  elde edilir. Bu, mevcut 1.310 soruyu bozmayan, ileride yapılabilecek bir iyileştirme.
- **`tools/manifest.py` düzeltmesi** yukarıda ayrı bölümde açıklandı; `MANIFEST.json`
  artık doğru, uygulama tarafı için ek aksiyon gerekmiyor.
