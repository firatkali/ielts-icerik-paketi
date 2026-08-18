# BULUT OTURUMU BRIEF — dinleme senaryo turu (39 işaretli kalem)

Bu dosya, bilgisayar kapalıyken `claude.ai/code` üzerinden başlatılan oturum içindir.
Depo: `firatkali/ielts-icerik-paketi`, dal `main`. Simulator/cihaz gerekmez, iş tamamen metin.

## 0) ÖNCE OKU
1. `denetim/DINLEME-TUR2-ISLISTESI.md` — devredilen tanılar + kalan kalemler
2. `denetim/CAPRAZ-KOK.md` — çapraz sızıntı taramasının son hâli
3. Bu dosyanın tamamı

## 1) İŞ NEDİR
Dinleme havuzunda **39 kalem** hâlâ "sesi dinlemeden bilinebiliyor" diye işaretli
(JSON alanı: `blind_solvable: true`). Amaç: her birini kör sınamada **0/3** yapmak ve
işareti kaldırmak. Bu, ses kaydının önündeki tek kapı — bitmeden ElevenLabs'a geçilmiyor.

Okuma tarafında işaretli kalem YOK, oraya dokunma.

## 2) DEĞİŞMEZ KURALLAR
- **İki ajan asla aynı dosyaya yazmasın.**
- Bölüşüm **dosya bazlı değil SENARYO bazlı**: her senaryo (`content/listening/scripts/Lx-Sy.json`)
  tek ajanın sahipliğinde.
- 🔴 **Senaryoya cümle EKLEME/ÇIKARMA YASAK.** Yalnız var olan turun içinde yerinde değer
  değişikliği. Cümle eklemek o senaryoya bağlı bütün soruların `turn_index`'ini kaydırır;
  "kaçırdığım yeri tekrar dinlet" sessizce yanlış yeri çalar ve hiçbir testte görünmez.
- **Alıştırma paketleri (`content/listening/practice/*.json`) bu turda KİLİTLİ.** Tek bir
  alıştırma dosyası 4 ayrı senaryoya bağlı olabiliyor (aşağıdaki tabloya bak) → paralel ajanlar
  çakışır. Senaryo turunda yalnız `scripts/` + `tests/` düzenlenir.
  ⚠️ Bir senaryo değişikliği ona bağlı bir alıştırma sorusunun cevabını bozuyorsa, ajan bunu
  **düzeltmez, RAPOR EDER**; alıştırma düzeltmeleri turdan sonra tek elden yapılır.

## 3) BÖLÜŞÜM — 13 senaryo, 39 kalem
(T = `tests/`, bu turda düzeltilecek · P = `practice/`, KİLİTLİ, sadece etkilenirse rapor et)

| senaryo | kalemler |
|---|---|
| L1-S4 | T note-completion 31, 32 · P short-answer 4, table 9, 10 |
| L3-S4 | T summary-completion 34 · P flow-chart 2, 3 |
| L4-S1 | T note-completion 7 |
| L4-S3 | T multiple-choice 24, sentence-completion 28 |
| L4-S4 | T short-answer 32, 33, 34 · P flow-chart 10, 12, short-answer 9, 10 |
| L5-S1 | T form-completion 8 |
| L5-S2 | P multiple-choice 6 |
| L5-S3 | P matching 8, 9 |
| L5-S4 | P flow-chart 5, 6, 7, short-answer 14, 15 |
| L6-S2 | P multiple-choice 7, 9, 10 |
| L6-S3 | T multiple-choice 22, 23, matching 26 · P mc-multi 9-10 |
| L6-S4 | T note-completion 33, 36, summary-completion 38 · P flow-chart 14, note 13 |

**Bu turda fiilen düzeltilecek (T) = 16 kalem, 8 senaryo:**
L1-S4 · L3-S4 · L4-S1 · L4-S3 · L4-S4 · L5-S1 · L6-S3 · L6-S4
→ 8 paralel ajan, her biri tek senaryonun sahibi. Kalan 23 P kalemi ayrı alt tur.

⚠️ `tests/L4/short-answer.json` hem L4-S4 (32,33,34) hem başka senaryo kalemleri taşıyor;
bir dosyayı iki ajan açacaksa **sıraya sok**, aynı anda verme.

## 4) REÇETE (ucuzdan pahalıya)
1. **Kaydır** — boşluğu aynı senaryonun başka bir cevap noktasına taşı.
2. **Yerinde değiştir** — senaryodaki değeri değiştir, eski beklenen değeri çeldiriciye ver.
3. **Sesli rakip kur** ⭐ — konuşmacı "kitaplar şöyle der, ama burada durum farklı" deyip doğrusunu
   sonra söylesin. Ölçülmüş örnek (L5 özet 36): "kitaplar *grazed* der, ama o derinlikte otlayan
   yok, filmi aşındıran akan suyun kendisi" → cevap `scoured`, tek seferde 2/3 → **0/3**.

## 5) HER TUR SONUNDA — MERKEZÎ KAPANIŞ TARAMASI (ZORUNLU)
"Ajan bitti dedi" YETMEZ. Geçen tur ajanlar bitti dediği hâlde kapanış taraması **6 gerçek kusur**
yakaladı; ayrıca ajan kendi işini ölçerken iyimser (bir ajan "3 sızıntı" dedi, bağımsız kör ölçüm
**4** buldu + listede olmayan 2 tane daha).

Sırayla koştur:
```
python3 tools/dogrula.py          # şema 0 hata · 12 sınav 40/40 · toplam 1310
python3 tools/capraz-kok.py       # çapraz sızıntı
python3 tools/sessiz-kopya.py     # dinleme kör kopya
python3 tools/sessiz-rapor.py     # kör ölçüm raporu
```
Ayrıca elle kontrol et:
- **Tur sayıları değişmemiş olmalı** (senaryo başına turn sayısı, öncesi = sonrası).
- Değişen turlara bağlı **her** sorunun cevabı senaryoda birebir duruyor mu.
- ⚠️ Yanlış pozitif tuzağı: 8 kalemde cevap turda birebir geçmiyor çünkü rakam/kod harfle
  söyleniyor ("nine fifteen" ↔ `9.15`, "G W nine four one" ↔ `GW941`). Betik bunları sızıntı
  değil, "bulunamadı" diye gösterebilir — elle doğrula.
- Bütçe/çakışma: aynı kanıt iki soruda kullanılmasın.

Eşikler: cümle sonu eşleştirme ≤%20 · dinleme seçenekli ≤%30 · dinleme tamamlama ≤%20.

## 6) BİTİRİNCE
- `git add -A && git commit && git push` (main, doğrudan; yan dal açma).
- `denetim/DINLEME-TUR2-ISLISTESI.md` içindeki DURUM bölümünü güncelle (kalan işaretli sayısı).
- Kapanış raporunu bu dosyanın altına "TUR SONUCU" başlığıyla ekle: hangi senaryoda ne değişti,
  hangi kalem hangi reçeteyle kapandı, kalan işaretli kaç.
- Alıştırma (P) kalemlerinden etkilenen varsa **ayrı liste** olarak yaz — bir sonraki alt turun işi.

## 7) BU OTURUMDA YAPILMAYACAK
Uygulama kodu (`firatkali/ielts-app`), simulator/screenshot işleri, puanlama, mağaza maddeleri.
Onlar bilgisayar başındayken yapılacak.
