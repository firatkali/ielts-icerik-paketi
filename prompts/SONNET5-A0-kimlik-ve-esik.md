# ⚠️ MODEL: SONNET

Bu **tek çalıştırmalık, mekanik** bir iştir. Yeni içerik üretilmez, var olan dosyalara
iki alan eklenir. Soru metinlerine, cevaplara, açıklamalara **dokunulmaz.**

Amaç: üretilen içerik başka bir sınav uygulamasında da (aynı hattan) kullanılabilsin diye
her dosya hangi sınava ait olduğunu söylesin; ve okuma/dinleme testlerinde "kaç doğru = hangi
band" eşiği koda gömülü kalmasın, içerik dosyasından ayarlanabilsin.

---

## Adım 1 — Her JSON dosyasına `exam` alanı

`content/` ve `passages/` altındaki **her** `.json` dosyasının en üst düzeyine, `schema_version`
alanının hemen ardına şu alan eklenir:

```json
"exam": "ielts"
```

Zaten varsa dokunma. `dogrulama/` ve `content/DOGRULAMA/` altındaki rapor dosyaları hariç.

Bunu elle değil **script ile** yap; 200'den fazla dosya var ve elle düzenleme alan sırasını
bozar. `tools/` altına `_a0_kimlik.py` adında kısa bir script yaz, çalıştır, sonra scripti
depoda bırak (ne yapıldığının kaydı olur).

Script şu kurallara uymalı:
- `json.load` → sözlüğe alan ekle → `json.dump(..., ensure_ascii=False, indent=2)` ile geri yaz
- alan sırası korunmalı (`exam`, `schema_version`'dan sonra gelmeli)
- dosya okunamıyorsa atla ve sonunda listele — sessizce geçme

Bittiğinde kaç dosyaya eklendiğini, kaçında zaten olduğunu, kaçının okunamadığını yaz.

## Adım 2 — Test başına band eşiği dosyası

Her tam test klasörü için bir **test tanım dosyası** oluştur:

```
content/reading/tests/AC1/_test.json
content/reading/tests/AC2/_test.json
...
content/listening/tests/L1/_test.json
...
```

İçeriği (AC1 örneği):

```json
{
  "exam": "ielts",
  "schema_version": "1.0",
  "test_id": "AC1",
  "skill": "reading",
  "module": "academic",
  "question_count": 40,
  "band_thresholds_source": "official_average_2023",
  "band_thresholds_note": "Resmî ortalama tablo. Gerçek IELTS'te bu tablo her test sürümü için kaydırılır (equating). Buradaki değerler başlangıç değeridir ve canlı kullanım verisi biriktikçe TEST BAŞINA güncellenir. Koda gömülmez, bu dosyadan okunur.",
  "band_thresholds": [
    { "band": 9.0, "min_correct": 39 },
    { "band": 8.5, "min_correct": 37 },
    { "band": 8.0, "min_correct": 35 },
    { "band": 7.5, "min_correct": 33 },
    { "band": 7.0, "min_correct": 30 },
    { "band": 6.5, "min_correct": 27 },
    { "band": 6.0, "min_correct": 23 },
    { "band": 5.5, "min_correct": 19 },
    { "band": 5.0, "min_correct": 15 },
    { "band": 4.5, "min_correct": 13 },
    { "band": 4.0, "min_correct": 10 }
  ]
}
```

🔴 **Tabloları uydurma, aşağıdakileri aynen kullan.** Üç farklı tablo var:

**Academic okuma** (AC1–AC4) — yukarıdaki tablo.

**General Training okuma** (GT1, GT2) — belirgin şekilde daha yüksek eşik ister:

```
9.0→40 · 8.5→39 · 8.0→37 · 7.5→36 · 7.0→34 · 6.5→32 · 6.0→30 · 5.5→27 · 5.0→23 · 4.5→19 · 4.0→15
```

**Dinleme** (L1–L6, Academic ve General **aynı**):

```
9.0→39 · 8.5→37 · 8.0→35 · 7.5→32 · 7.0→30 · 6.5→26 · 6.0→23 · 5.5→18 · 5.0→16 · 4.5→13 · 4.0→11
```

Dinleme dosyalarında `"skill": "listening"` ve `"module": "both"` yaz.

## Adım 3 — Kontrol

```
python tools/dogrula.py
```

Şema hatası çıkmamalı. `exam` alanı eklendikten sonra doğrulama betiği hâlâ 0 hata veriyorsa iş
tamamdır. Hata verirse alan ekleme bir dosyayı bozmuştur — `git checkout` ile geri al, sebebini
bul, tekrar dene.

## Bitirince

`NOTLAR.md` sonuna kısa not: kaç dosyaya `exam` eklendi, kaç test tanım dosyası oluşturuldu.

```
git add -A
git commit -m "kimlik alani ve band esigi dosyalari eklendi"
git pull --rebase
git push
```

**Kullanıcıya soru sorma.**
