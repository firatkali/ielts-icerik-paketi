# Puanlı örnek kütüphanesi — kontrol tablosu

Son güncelleme: 2026-08-09 · Üreten adım: `prompts/OPUS5-E9-alt-band-ornekleri.md`

Bu dosya **depoya girer**; `kalibrasyon/ornekler/` klasörünün geri kalanı (`yazma/`,
`konusma/` ve içlerindeki `*.json`) `.gitignore`'dadır ve girmez. Sebep: örneklerin
kendisi telifli resmî malzemenin metne dökülmüş hâli, bu tablo ise yalnız **üst veri** —
aday cevabından ya da sınav görevlisi yorumundan tek cümle içermez.

Tablo elle yazılmadı, `python tools/_e9_kontrol_tablo.py` ile dosyalardan üretildi.

## Örnekler

| Kod | Görev | Gerçek band | Kaynak | Şüpheli mi |
|---|---|---|---|---|
| `GT-T1-1B-A` | Yazma - GT Task 1 | **3,0** | GT Writing Sample Tasks 2023 | hayır |
| `AC-ER-T1-B` | Yazma - Academic Task 1 | **4,0** | Academic Writing Example Responses | hayır |
| `AC-T2-2A-A` | Yazma - Academic Task 2 | **4,0** | Academic Writing Sample Tasks 2023 | hayır |
| `GT-T2-2B-A` | Yazma - GT Task 2 | **4,0** | GT Writing Sample Tasks 2023 | hayır |
| `AC-T1-1A-A` | Yazma - Academic Task 1 | **5,0** | Academic Writing Sample Tasks 2023 | hayır |
| `AC-T1-1C-A` | Yazma - Academic Task 1 | **5,0** | Academic Writing Sample Tasks 2023 | hayır |
| `GT-T2-2A-A` | Yazma - GT Task 2 | **5,0** | GT Writing Sample Tasks 2023 | hayır |
| `SP-band5-1` | Konuşma - Part 2 | **5,0** | ielts.org band örnekleri sayfası | hayır |
| `SP-band5-2` | Konuşma - Part 3 | **5,0** | ielts.org band örnekleri sayfası | hayır |
| `AC-T2-2B-A` | Yazma - Academic Task 2 | **5,5** | Academic Writing Sample Tasks 2023 | hayır |
| `GT-T1-1A-A` | Yazma - GT Task 1 | **5,5** | GT Writing Sample Tasks 2023 | hayır |
| `GT-T1-1B-B` | Yazma - GT Task 1 | **5,5** | GT Writing Sample Tasks 2023 | hayır |
| `AC-T1-1A-B` | Yazma - Academic Task 1 | **6,0** | Academic Writing Sample Tasks 2023 | hayır |
| `AC-T1-1B-A` | Yazma - Academic Task 1 | **6,0** | Academic Writing Sample Tasks 2023 | hayır |
| `GT-T1-1B-C` | Yazma - GT Task 1 | **6,0** | GT Writing Sample Tasks 2023 | hayır |
| `GT-T2-2B-B` | Yazma - GT Task 2 | **6,0** | GT Writing Sample Tasks 2023 | hayır |
| `SP-band6-1` | Konuşma - Part 3 | **6,0** | ielts.org band örnekleri sayfası | hayır |
| `SP-band6-2` | Konuşma - Part 3 | **6,0** | ielts.org band örnekleri sayfası | hayır |
| `AC-T2-2A-B` | Yazma - Academic Task 2 | **6,5** | Academic Writing Sample Tasks 2023 | hayır |
| `SP-band6_5-1` | Konuşma - Part 2 | **6,5** | ielts.org band örnekleri sayfası | hayır |
| `AC-T1-1B-B` | Yazma - Academic Task 1 | **7,0** | Academic Writing Sample Tasks 2023 | hayır |
| `AC-T1-1C-B` | Yazma - Academic Task 1 | **7,0** | Academic Writing Sample Tasks 2023 | hayır |
| `GT-T1-1A-B` | Yazma - GT Task 1 | **7,0** | GT Writing Sample Tasks 2023 | hayır |
| `GT-T1-1B-D` | Yazma - GT Task 1 | **7,0** | GT Writing Sample Tasks 2023 | hayır |
| `SP-band7-1` | Konuşma - Part 3 | **7,0** | ielts.org band örnekleri sayfası | hayır |
| `SP-band7-2` | Konuşma - Part 3 | **7,0** | ielts.org band örnekleri sayfası | hayır |
| `AC-T2-2B-B` | Yazma - Academic Task 2 | **7,5** | Academic Writing Sample Tasks 2023 | hayır |
| `SP-band7_5-1` | Konuşma - Part 3 | **7,5** | ielts.org band örnekleri sayfası | hayır |
| `GT-T2-2A-B` | Yazma - GT Task 2 | **8,0** | GT Writing Sample Tasks 2023 | hayır |
| `SP-band8-1` | Konuşma - Part 3 | **8,0** | ielts.org band örnekleri sayfası | hayır |
| `SP-band8-2` | Konuşma - Part 3 | **8,0** | ielts.org band örnekleri sayfası | hayır |
| `AC-T1-1C-C` | Yazma - Academic Task 1 | **8,5** | Academic Writing Sample Tasks 2023 | hayır |
| `AC-T2-2A-C` | Yazma - Academic Task 2 | **8,5** | Academic Writing Sample Tasks 2023 | hayır |
| `GT-T2-2B-C` | Yazma - GT Task 2 | **8,5** | GT Writing Sample Tasks 2023 | hayır |
| `SP-band8_5-1` | Konuşma - Part 3 | **8,5** | ielts.org band örnekleri sayfası | hayır |
| `SP-band9-1` | Konuşma - Part 3 | **9,0** | ielts.org band örnekleri sayfası | hayır |

**Toplam 36 örnek** (yazma 24 + konuşma 12). Şüpheli işaretli örnek **yok**.

## Alt band (≤ 4,5) durumu — E9'un takip ettiği sayı

| | Adet |
|---|---|
| Band 3,0 | 1 |
| Band 4,0 | 3 |
| Band 4,5 | 0 |
| **≤ 4,5 toplam** | **4** |

E9'un hedefi **en az 8**. Bu çalıştırmada 3 → 4 çıkıldı; hedef tutturulamadı, sebep
`NOTLAR.md`'de yazılı (erişilebilir kaynak tükendi, kalan kaynak bu oturumda okunamadı).
**Örnek uydurulmadı.**

## Kümelere dağılım

`kalibrasyon/olcum/kumeler.json`: S1 = 12, S2 = 12, S3 = 12 örnek. ≤ 4,5 örnekler üç
kümeye eşit dağılmış durumda — **her kümede 1 tane**: S1 `GT-T1-1B-A` (3,0),
S2 `AC-T2-2A-A` (4,0), S3 `GT-T2-2B-A` (4,0) + bu çalıştırmada eklenen `AC-ER-T1-B`
(4,0) da S3'e girdi. S3 hem eleman sayısı hem alt band sayısı bakımından geride olduğu
için seçildi; saklı küme kontrolü anlamını koruyor.

## Şüpheli (`transcription_suspect`) kuralı

Band 6 ve altı bir cevapta belirgin dilbilgisi/yazım hatası sayısı 0-1 ise döküm
şüphelidir (dökerken farkında olmadan düzeltilmiş olabilir) ve dosyaya
`"transcription_suspect": true` konur; `tools/puanlama-raporu.py` o örneği ölçümden
otomatik düşürür. Her örneğin hata sayımı ve dökümle ilgili notları kendi dosyasının
`transcription_notes` alanında; ayrıntılı hata dökümleri `yazma/KONTROL.md` ve
`konusma/KONTROL.md` dosyalarında (ikisi de depoya girmez, çünkü aday metninden
birebir parçalar içerirler).
