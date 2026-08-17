# B3 — Okuma alıştırma havuzu: bağımsız yeniden sayım

- **Tarih:** 2026-08-17
- **Kapsam:** `content/reading/practice/*.json` (12 dosya). Görev: FAZ 0.3 — "sayıya
  güvenme, yeniden say."
- **Yöntem:** `python tools/manifest.py` + `python tools/dogrula.py` çalıştırıldı;
  ayrıca her dosya elle (bağımsız script ile) `items`/`groups.items` düzeyinde tek tek
  sayıldı. İki yöntem birebir aynı sonucu verdi.
- **Not:** `denetim/*  2.md` (iCloud kopyaları) okunmadı/yazılmadı — talimata uyuldu.

---

## Sonuç: hangi sayı doğru

**Doğru sayı: 157 kalem (item) / 160 soru numarası (question number) / 12 paket.**
Denetim planındaki "154 kalem / 12 paket" iddiası **doğrulanamadı** — depo genelinde
`154` rakamının "kalem" bağlamında geçtiği tek yer `denetim/UYGULAMA-PLANI.md`'nin
kendisi (bkz. kanıt bölümü); ne `denetim/envanter.md`, ne `denetim/DENETIM-RAPORU.md`,
ne `content/MANIFEST.json`, ne de mevcut içerik dosyaları bu sayıyı üretiyor. 12 paket
sayısı doğru (iki iddiada da ortak).

**157 kalem / 160 numara** ise üç bağımsız kaynakta birebir aynı:
1. `tools/manifest.py` çıktısı → `content/MANIFEST.json`: `reading/practice` toplamı
   **160** (bu araç çift-cevaplı kalemleri `select_count == 2` ile 2 numara sayıyor).
2. `tools/dogrula.py` çıktısı: `reading/practice 160`.
3. Bu görevde yazılan bağımsız sayım scripti (dosyaları `items`/`groups.items`
   düzeyinde elle gezip `number` alanındaki `"3-4"` gibi aralıkları açarak sayan,
   `manifest.py`'den tamamen ayrı bir kod yolu): **157 kalem, 160 numara.**

`PLAN-soru-dagilimi.md`'nin D bölümündeki hedef de **160** (12 tip × hedef adet toplamı)
— yani "numara" sayısı hem hedefle hem iki bağımsız araçla hem de bu turun elle
sayımıyla örtüşüyor. 157/160 farkı **tek kaynaktan geliyor**: `multiple-choice.json`
12 kalem taşıyor ama 3 kalemi çift cevaplı (`"3-4"`, `"7-8"`, `"9-10"`, her biri 2
numara) — 12 kalem + 3 fazladan numara = 15 numara; diğer 11 pakette kalem sayısı
numara sayısına eşit. 157 + 3 = 160.

## Kanıt: "154" nereden geliyor, neden geçersiz

```
grep -rln "154" . | grep -v " 2"
→ denetim/UYGULAMA-PLANI.md  (3 yerde: §0 akış şeması, §0.3 metni, §1.3 başlığı)
```
Bu üç geçişin hepsi planın **kendi içindeki** ifadeler; hiçbiri `envanter.md` veya
`DENETIM-RAPORU.md`'den bir alıntı değil, o iki dosyada "154" rakamı hiç geçmiyor.
`envanter.md`'nin 2b tablosu (`### 2b. Okuma alıştırmaları (hedef 160)`) her tip için
"Hedef 160 → Üretilen 160" diyor — yani denetimin kendi kayıtlı ölçümü de 154 değil
160 (numara bazında). Sonuç: **"154 kalem / 12 paket" izlenemeyen, muhtemelen eski/
yanlış hatırlanmış bir rakam; plana güvenilmez, dosya taraması esas alınır** (planın
kendisinin de önerdiği gibi: "sayıya güvenme, yeniden say").

## `manifest.py` / `dogrula.py` çıktısı (ham)

```
$ python tools/manifest.py
beceri          hedef uretilen     fark
reading           400      400        0
...
Isaretli (flagged) soru: 237

$ python tools/dogrula.py
=== SORU SAYILARI ===
  reading/practice       160
  ...
  TOPLAM                 1310
  isaretli (flagged)     237
=== SEMA HATALARI: 0 ===
```

---

## Paket bazında tam tablo

Kalem→grup→dosya zinciriyle çözülmüş `passage_id`: dosya düzeyinde (`d.passage_id`)
tüm 12 pakette `null` — gerçek değer kalem üstünde (`item.passage_id`) ya da, gruplu
dosyalarda (matching-features, matching-headings, matching-sentence-endings) grup
üstünde (`group.passage_id`, kalemler kendi `passage_id` alanını taşımıyor).

| Paket (`content/reading/practice/`) | Kalem | Numara | İşaretli | Kullandığı pasaj kimlikleri |
|---|---:|---:|---:|---|
| `sentence-completion.json` | 15 | 15 | 8 | A01, A02, A03, A04, A05 |
| `note-completion.json` | 15 | 15 | 5 | A06, A07, A08, A09, A12 |
| `summary-completion.json` | 15 | 15 | 10 | A10, A11, G05, G06 |
| `short-answer.json` | 10 | 10 | 1 | A01, A02, A03, A04, A05, A06, A07, A08, A09, A12 |
| `diagram-labelling.json` | 10 | 10 | 0 | G01, G02, G03, G04 |
| `matching-information.json` | 15 | 15 | 0 | A01, A04, A07, A11 |
| `true-false-not-given.json` | 15 | 15 | 1 | A02, A05, A08, A09 |
| `yes-no-not-given.json` | 15 | 15 | 5 | A06, A10, A11, A12 |
| `multiple-choice.json` | **12** | **15** | 8 | A02, A05, A08, A11 |
| `matching-headings.json` | 15 | 15 | 1 | A01, A09, A12 |
| `matching-features.json` | 10 | 10 | 2 | A10, G05 |
| `matching-sentence-endings.json` | 10 | 10 | 9 | A07, G06 |
| **TOPLAM** | **157** | **160** | **50** | |

`multiple-choice.json`'daki üç çift-cevaplı kalem (numara `3-4`, `7-8`, `9-10`, her biri
`select_count: 2`) tek satırda tutuluyor ama 2 numara işgal ediyor; bu yüzden kalem
(12) ile numara (15) sayısı burada ayrışıyor, diğer 11 pakette ayrışmıyor.

Paket → pasaj eşlemesi `denetim/UYGULAMA-PLANI.md` §1.3'teki tabloyla (bugünkü
pasajlar sütunu) satır satır örtüşüyor; tek fark `short-answer` satırının planda
kısaltılmış yazılması ("A01-A09, A12") — açılımı yukarıdaki tabloyla birebir aynı
(A01, A02, A03, A04, A05, A06, A07, A08, A09, A12 — 10 ayrı pasaj, 10 kalem).

İşaretli (flagged) toplamı bu turda **50**; `denetim/envanter.md`'nin 2b tablosundaki
**53** ile aynı değil — envanter 2026-08-09 tarihli bir kayıt, aradan geçen sürede
(E7 yeniden üretimleri vb.) içerik değişmiş olabilir; bu fark B3 sayımının konusu
değil, yalnız burada not düşülüyor.

---

## Yazılmayan/değiştirilmeyen dosyalar

Bu görevde hiçbir soru/pasaj içeriği değiştirilmedi; yalnız bu rapor (`denetim/
B3-ALISTIRMA-SAYIM.md`) ve ayrı görevde `content/PLAN-EK-kurallar.md` yazıldı.
`content/PLAN-soru-dagilimi.md`'ye dokunulmadı.
