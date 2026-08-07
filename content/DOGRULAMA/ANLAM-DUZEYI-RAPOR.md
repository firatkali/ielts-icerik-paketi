# Anlam düzeyi ölçüt — parçasız cevabın *anlamca* tutup tutmadığı

Bu rapor yeni bir ölçüm turu koşturmuyor. Mevcut `kalibrasyon/metinsiz/<paket>-tur1/2/3.json`
dökümlerini — modelin parçayı görmeden verdiği cevapları — yeniden değerlendiriyor. Eski
`OPUS5-B1` ölçümü "cevap 3/3 turda **kelimesi kelimesine** tuttu mu?" diye soruyordu; bu ölçüm
"cevap 3/3 turda **anlamca** tuttu mu?" diye soruyor.

## Karar kuralı (üç çalıştırmada aynı)

Modelin cevabı, gerçek cevapla **aynı şeye işaret ediyorsa** anlamca doğru sayıldı:

- eş anlamlı kelime (`mountaineers` ↔ `climbers`, `salary` ↔ `pay`)
- aynı kelimenin farklı çekimi/biçimi (`probationary period` ↔ `probation period`)
- niteleyici düşmüş ama ana ad duruyor, gönderge aynı (`separate laboratories` → `laboratories`)
- aynı kavramın başka sözcüğü (`ongoing research` → `preliminary`)

Anlamca **yanlış** sayılanlar: gönderge daralıyor ya da değişiyor (`weeks or months` → `weeks`,
`plant DNA` → `ancient DNA`), sayı/isim tutmuyor (`8,400 years` → `8,000 years`), yanlış kavram.
🔴 Üç turun **üçünde de** anlamca doğru olması şart — tek turda tutturmak hâlâ şans olabilir.

---

## 1. çalıştırma — cümle tamamlama + kısa cevap · 2026-08-08

| Paket | Soru | Kelime düzeyi (eski) | Anlam düzeyi (yeni) | Fark | Yeni işaretlenen |
|---|---|---|---|---|---|
| sentence-completion | 37 | 13 (%35.1) | 27 (%73.0) | +37.9 puan | 14 |
| short-answer | 10 | 2 (%20.0) | 3 (%30.0) | +10.0 puan | 1 |
| **toplam** | **47** | **15 (%31.9)** | **30 (%63.8)** | **+31.9 puan** | **15** |

Kendi sayımım **15 yeni soru.** Plandaki "cümle tamamlamada ~19" rakamına ulaşmadım: cümle
tamamlamada 14 yeni soru buldum, anlam düzeyi oranı %73.0 çıktı. Denetim raporunun andığı %81
ile arasındaki fark, sınırda kalan sekiz soruyu (aşağıda) saymamış olmamdan geliyor — gönderge
daralan ya da sayısı tutmayan cevabı "biliniyor" saymadım.

### Yeni işaretlenen sorular

`sentence-completion` (14): practice 2, 3, 4, 6, 7, 12 · AC1 19, 20 · AC2 20 · AC3 22 ·
AC4 22 · GT1 27 · GT2 25, 26
`short-answer` (1): practice 6

### Somut örnekler — gerçek cevap → modelin anlamca doğru ama kelimece farklı cevabı

| Soru | Gerçek cevap | Modelin üç turdaki cevabı | Neden anlamca doğru |
|---|---|---|---|
| AC3-22 | `mountaineers` | climbers · climbers · climbers | Tam eş anlamlı; "dağcılar" göndergesi birebir aynı, yalnız sözcük farklı. |
| AC1-19 | `transparent divider` | transparent barrier ×3 | Tankı bölen saydam engel; `divider`/`barrier` aynı nesneyi adlandırıyor. |
| GT2-25 | `probationary period` | probation period ×3 | Aynı kelimenin sıfat/ad çekimi; kavram deneme süresi, birebir aynı. |
| practice-12 | `ongoing research` | preliminary ×3 | "Hakem değerlendirmesinden geçmemiş, bitmemiş bulgu" kavramı; farklı sözcük, aynı iddia. |
| practice-3 | `anatomy` | anatomy · **morphology** · anatomy | Kelime düzeyinde 2/3 tuttuğu için "bilinmiyor" sayılmıştı; `morphology` biyolojide `anatomy`nin eş anlamlısı, anlamca 3/3. |

### Anlamca da saymadığım sınır durumlar (şeffaflık için)

| Soru | Gerçek cevap | Modelin cevabı | Neden sayılmadı |
|---|---|---|---|
| practice-sc-5 | `first contact` | contact · **approach** · contact | Parça mesafe korumayı temastan ayırıyor; `approach` ≠ `contact`. |
| practice-sc-9 | `hypothetical future` | simulation · prediction · prediction | Modelleme kavramı var, "gelecek" ögesi yok. |
| practice-sc-14 | `transitional stage` | beginning · stage · start | Ayırt edici öge (`transitional`) iki turda düşmüş. |
| AC2-sc-19 | `plant DNA` | ancient DNA ×3 | Sorulan ayrıntı (`plant`) tutmuyor; `ancient` başka bir şey söylüyor. |
| GT2-sc-27 | `four weeks` | four weeks · **one month** · four weeks | Birim çevrimi sayı değişikliği sayıldı; sayıda kesinlik kuralı gevşetilmedi. |
| practice-sa-3 | `weeks or months` | weeks ×3 | Gönderge daralıyor: `weeks` aralığın yalnız alt ucunu veriyor. |
| practice-sa-5 | `8,400 years` | 8,000 years ×3 | Yanlış sayı. |
| practice-sa-9 | `scanning electron microscopy` | electron microscopy · **transmission** electron microscopy · electron microscopy | 2. tur başka bir tekniği (TEM) adlandırıyor. |

### İşaretlemenin şekli

Anlamca bilinen her soruya orijinal dosyasında şu alanlar yazıldı:

```json
"blind_solvable": true,
"blind_solvable_kelime_duzeyi": false,
"blind_basis": "logic",
"status": "flagged",
"flag_reason": "Parça gösterilmeden anlamca 3/3 turda doğru bilindi: ...",
"flag_mechanism": "esdizim_kilidi"
```

Eski kelime-düzeyi bulgusu silinmedi: `blind_solvable: false` değeri
`blind_solvable_kelime_duzeyi` alanına taşındı, çünkü iki ölçüm farklı şeyi ölçüyor — biri
kavrayışı, öteki kelime tutturmayı. Hiçbir soru silinmedi; 47 sorunun 47'si yerinde
(`sentence-completion` 37, `short-answer` 10), tam testlerde soru sayısı değişmedi.

Uygulayan betik: `tools/_e10_anlam_isaretle.py`.

---

Bu ölçüm anlam düzeyinde bilinen soruyu bulur, kelime tutturma başarısını değil.
