# ⚠️ MODEL: OPUS

Bu dosya **8 kez** çalıştırılır, mekanizma bazında (tip bazında değil):

| # | Kapsam |
|---|---|
| 1 | YES/NO/NOT GIVEN — kip imzası |
| 2 | Çoktan seçmeli — kip imzası + konumsal düzen |
| 3 | Cümle sonu eşleştirme + özellik eşleştirme |
| 4 | Tamamlama ailesinde eşdizim kilidi |
| 5 | Kelime bankalı özet — tanım sızıntısı |
| 6 | TRUE/FALSE/NOT GIVEN + kalan tekiller |
| 7 | E10'dan gelen cümle tamamlama + kısa cevap işaretleri |
| 8 | E10'dan gelen özet ailesi işaretleri + genel-kültür temalıların elenme kararı |

Hangi çalıştırma olduğun sana ek talimatta söylenir; söylenmiyorsa yukarıdaki listede henüz
işlenmemiş ilk grubu yap.

---

## Ne yapıyoruz ve neden

`SONNET5-E1` her işaretli soruya gerçek mekanizmasını (`flag_mechanism`) yazdı,
`OPUS5-E10` anlam düzeyinde bilinen ek soruları işaretledi, `OPUS5-E4` gerçek sınav
desenini (oran/ölçüt) çıkardı. Bu adım artık **düzeltmenin kendisini** yapıyor — ama
mekanizma bazında, çünkü aynı mekanizma birden çok soru tipinde tekrarlıyor ve tek tip
düzeltme hepsini kapatabiliyor.

Önce oku:
- `content/DOGRULAMA/ISARET-GEREKCELERI.md` (E1 — hangi soru hangi mekanizma)
- `content/DOGRULAMA/ANLAM-DUZEYI-RAPOR.md` (E10 — anlam düzeyinde ek işaretliler)
- `kalibrasyon/desen/*` (E4 — gerçek sınav oranları, karşılaştırma çapası olarak)
- `denetim/capraz-ozet.md` §4 (üretim hatası deseni özeti)

---

## 🔴 Zorunlu kurallar (her çalıştırmada)

1. **Sayıya güvenme, yeniden say.** Denetim raporu ~180 diyor, E10 sayıyı büyüttü; her
   çalıştırma kendi kapsamındaki işaretli soruları `grep`/kendi taramasıyla yeniden bulur.
2. **Hiçbir soru silinmez.** Elenen soru `status: "rejected"` + `reject_reason` alır, dosyada
   kalır — E6'ya devredilecek "yeniden üretilecek yuva" listesine girer.
3. **Tam testlerde soru sayısı değişmez.** Elenen her yuva E6'da aynı numarayla doldurulacak;
   bu çalıştırma numarayı/yuvayı bozmaz, sadece işaretler.
4. **Saklı küme koruması** — geçerli değil (puanlama dosyası açılmıyor).
5. **Token tasarrufu — hedefli okuma.** Yalnız kendi mekanizma/tip kapsamındaki işaretli
   soruları aç; diğer tiplerin dosyalarını tarama.
6. 🔴 **Her çalıştırma depoda İZLENEN bir dosyayı değiştirip commit etmek zorunda.**

---

## Her soru için üç sonuçtan biri

**1) Düzeltildi** — soru metni yeniden yazılır (kip dengelenir: doğru cevaba ölçülü ifade,
çeldiriciye orantılı kesinlik verilir; boşluk öbeğin öbür ucuna taşınır; kelime bankası/tanım
metni cevabı sızdırmayacak şekilde yeniden düzenlenir…).

- `status: "verified"`
- `blind_solvable: null` (eski ölçüm artık geçersiz — soru değişti, E7 yeniden ölçecek)
- `revision: {"tarih": "...", "mekanizma": "...", "ne_degisti": "..."}`

🔴 **Cevap anahtarı ve kanıt cümlesi (`answer`, `evidence`) KORUNUR** — düzeltme yalnız soru
metnine/seçeneklere yapılır. Kanıt cümlesi değişmek **zorundaysa** bu "düzeltildi" değil
"elendi" sayılır (yarım düzeltme, ölçülmemiş yeni soru üretmiş olursun).

**2) Elendi** — konusu genel kültür olan sorular (denetimde ~70 civarı bekleniyor, kendi
sayımınla doğrula): mekanik düzeltmeye uygun değil, çünkü sorun kip/konum değil **soru
ekseninin kendisi.**

- `status: "rejected"` + `reject_reason` (o sorunun neden mekanik düzeltmeye uygun olmadığı)
- Aynı yuva **E6'nın devir dosyasına** eklenir (aşağıda).

**3) Dokunulmadı** — mekanizma net değilse veya düzeltme cevap/kanıtı bozacaksa: gerekçesi
`explanation`'a veya `NOTLAR.md`'ye yazılır, soru olduğu gibi kalır (`status` değişmez).

## Yasak

- Soru sayısını değiştirmek (elenen yuva E6'da dolacak, burada boş bırakılır).
- Cevap harflerini toptan karıştırmak (ör. bir setteki bütün doğru cevapları yeniden
  dağıtmak) — yalnız işaretlenen soru düzeltilir.
- Aynı pasajın aynı cümlesine ikinci bir soru yazmak.

## E6'ya devir dosyası (zorunlu çıktı, her elenen yuva için güncellenir)

`content/DOGRULAMA/yeniden-uretim-listesi.json`:

```json
{
  "elenen": [
    {
      "dosya": "content/reading/tests/AC2/multiple-choice.json",
      "numara": 12,
      "tip": "multiple_choice",
      "pasaj": "A05",
      "kacinilacak": {
        "kanit_cumlesi": "<bu pasajda zaten soru sorulmuş cümle/paragraf — yeni soru buraya yazılmasın>"
      },
      "neden_elendi": "..."
    }
  ]
}
```

Her çalıştırma kendi bulduğu elenenleri bu dosyanın `elenen` listesine **ekler** (üzerine
yazmaz). İnsan okunur özetini de tut: `content/DOGRULAMA/ELDEN-GECIRME.md` — mekanizma
bazında kaç soru düzeltildi/elendi/dokunulmadı tablosu + örnekler.

## Bitirince (her çalıştırmada)

```
git add -A
git commit -m "isaretli sorulari elden gecir: YES-NO-NOT-GIVEN kip imzasi (1/8)"
git pull --rebase
git push
```

**Kullanıcıya soru sorma. Hiçbir soruyu silme.**
