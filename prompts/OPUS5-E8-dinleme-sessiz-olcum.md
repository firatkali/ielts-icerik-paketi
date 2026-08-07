# ⚠️ MODEL: OPUS

Bu dosya **5 kez** çalıştırılır: 1) araçlar + yöntem notu + dinleme çoktan seçmeli (tek
cevaplı) · 2) çoktan seçmeli (çok cevaplı) + eşleştirme (`FABLE5-43`'ün kalanı) · 3) tamamlama
ailesi A (form/not/tablo) · 4) tamamlama ailesi B (cümle/özet/akış/kısa cevap) · 5) toplu
rapor + işaretleme. Hangi çalıştırma olduğun sana ek talimatta söylenir.

---

## Ne yapıyoruz ve neden

360 dinleme sorusu bugüne kadar **hiç** sızıntı ölçümüne girmedi (`denetim/DENETIM-RAPORU.md`
§5, madde A3). `FABLE5-43` yuvasından çıkan 96 soru (çoktan seçmeli 33 + eşleştirme 33 +
alıştırma 30), okumada %100 sızdıran prompt ailesinin akrabası — aynı desenin dinlemede de
olup olmadığı bilinmiyor. Bu adım `OPUS5-B1`'in okuma tarafında yaptığını dinlemeye uyguluyor.

---

## 🔴 Tasarım farkı — dosyanın başında dursun

Okumada "parça" **pasajdı**, dinlemede **ses metnidir** (`content/listening/scripts/`).
Ölçüm "senaryo hiç gösterilmeden soru bilinebiliyor mu"yu sorar.

İkinci fark: form/not tamamlamada cevap çoğu zaman özel ad, sayı, saat — bunlar **yapısal
olarak tahmin edilemez.** Bu tiplerde düşük parçasız-bilinme oranı **beklenir ve başarı
sayılmaz**; ölçüyü asıl ilgilendiren çoktan seçmeli + eşleştirmedir.

## 🔴 Dosya adı çakışması tuzağı

Okuma ve dinlemede paket adları aynı (`multiple-choice`, `matching`…). `tools/metinsiz-kopya.py`
bugün `skill != "reading"` olan dosyaları **bilerek atlıyor** (satır 82) — bu, okumanın ölçüm
altyapısını dinlemenin bozmaması için var, **dokunma.**

Bu adım **mevcut `tools/metinsiz-kopya.py` / `tools/metinsiz-rapor.py`'yi değiştirmeyecek.**
Yanına yeni script'ler yazacak:

- `tools/sessiz-kopya.py` — `metinsiz-kopya.py`'nin dinleme sürümü: senaryo metni, cevap
  anahtarı ve her parça izi (script_id, turn_index, transcript…) silinmiş kopya üretir.
  Çıktı: `dogrulama/sessiz/` (gitignore'da).
- `tools/sessiz-rapor.py` — `metinsiz-rapor.py`'nin dinleme sürümü. Çıktı:
  `kalibrasyon/sessiz/<paket>-tur<N>.json` ve `content/DOGRULAMA/SESSIZ-<paket>.md`.

Okumanın ölçüm dosyalarının (`dogrulama/metinsiz/`, `kalibrasyon/metinsiz/`,
`content/DOGRULAMA/METINSIZ-*`) **üzerine yazmak yasak** — biten işi sessizce bozar.

---

## 🔴 Zorunlu kurallar (her çalıştırmada)

1. **Sayıya güvenme, yeniden say.** `python tools/dogrula.py` / kendi taramanla dinleme soru
   sayısını doğrula; 360 hedef sayıdır, gerçek sayım farklı çıkabilir.
2. **Hiçbir soru silinmez.** İşaretlenen soru dosyada kalır.
3. **Tam testlerde soru sayısı değişmez.** L1-L6 her biri 40 soru; bu adım işaretliyor,
   silmiyor/eklemiyor.
4. **Saklı küme koruması** — geçerli değil.
5. **Token tasarrufu — hedefli okuma.** Senaryo metnini (`content/listening/scripts/`) yalnız
   script'in kendisi okusun; sen (model) çözüm turlarında senaryoya **hiç bakma** — aşağıdaki
   "EN ÖNEMLİ KURAL" bunu detaylandırıyor.
6. 🔴 **Her çalıştırma depoda İZLENEN bir dosyayı değiştirip commit etmek zorunda.**

---

## 🔴 EN ÖNEMLİ KURAL

**Bu oturumda ne dinleme senaryosunu ne cevap anahtarını göreceksin.**
`content/listening/scripts/` klasörünü açma, soru dosyalarını Read ile açma — onlara yalnız
script'ler dokunur. Senaryoyu bir kez okursan bu ölçüm tamamen değersizleşir.

## 1. çalıştırma — Araçlar + yöntem notu + MC (tek cevaplı)

1. `tools/sessiz-kopya.py` ve `tools/sessiz-rapor.py`'yi `metinsiz-kopya.py`/
   `metinsiz-rapor.py`'den uyarlayarak yaz (dinleme şemasına göre: `script_id`, `turn_index`,
   `transcript` gibi alanları sil; okuma-özel alanları (`passage_id`, `evidence_locator`
   paragraf alanı) dinleme şemasına göre uyarla).
2. Kısa bir yöntem notu yaz: `content/DOGRULAMA/SESSIZ-RAPOR.md`'nin en başına — okuma
   ölçümünden farkları (yukarıdaki tasarım farkı + dosya adı çakışması) özetleyen 3-4 cümle.
3. Dinleme çoktan seçmeli (tek cevaplı) paketlerini ölç: kopya üret, 3 tur çöz, rapor.

## 2. çalıştırma — MC (çok cevaplı) + eşleştirme

`FABLE5-43`'ün ürettiği kalan paketler: çoktan seçmeli (çok cevaplı) + eşleştirme.

## 3. çalıştırma — Tamamlama ailesi A

`form-completion`, `note-completion`, `table-completion` (dinleme sürümleri).

## 4. çalıştırma — Tamamlama ailesi B

`sentence-completion`, `summary-completion`, `flow-chart-completion` (dinleme sürümleri
varsa), `short-answer`.

🔴 **Plan/harita/diyagram etiketleme (`plan-map-diagram-labelling`) ölçülmez** — görsel
gerektirir, metin tabanlı ölçüm orada kör. Raporda "ölçülmedi" yaz — okuma tarafındaki
diyagram etiketleme kararının aynısı.

## 5. çalıştırma — Toplu rapor + işaretleme

`content/DOGRULAMA/SESSIZ-RAPOR.md`'yi tamamla:

- Paket bazında + toplu oran (3/3 turda bilinen / toplam).
- 🔴 **Ölçüt anlam düzeyi** (K3, okuma tarafındaki yeni ölçütle aynı — `OPUS5-E10`'daki
  tanım): kelime kelime tutturma değil, anlamca bilme.
- Yapısal olarak tahmin edilemeyen tiplerde (form/not — özel ad, sayı, saat) düşük oran
  **beklenir, başarı sayılmaz**; bunu raporda açıkça yaz, MC + eşleştirmeye odaklan.
- İşaretleme, aynı şema (E1'in dersi baştan uygulanır — tek tip cümle yazma):

```json
"blind_solvable": true,
"blind_basis": "option_wording",
"status": "flagged",
"flag_reason": "Senaryo gösterilmeden 3/3 turda doğru bilindi: <bu soruya özel somut sebep>.",
"flag_mechanism": "kip_imzasi"
```

- Son satır her zaman: **"bu ölçüm bozuk soruyu bulur, zorluk ölçmez."**

## Bitirince (her çalıştırmada)

```
git add -A
git commit -m "dinleme sizinti olcumu: araclar + coktan secmeli tek cevapli (1/5)"
git pull --rebase
git push
```

**Kullanıcıya soru sorma. Hiçbir soruyu silme.**
