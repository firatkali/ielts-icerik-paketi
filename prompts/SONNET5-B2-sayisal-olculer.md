# ⚠️ MODEL: SONNET

Bu dosya **2 kez** çalıştırılır: 1) okuma · 2) dinleme.

---

## Ne yapıyoruz ve neden

Bir sınav sorusunu zorlaştıran şey modelin ya da adayın zekâsı değil, **sorunun yapısı**:
cevap metinde birebir aynı kelimelerle mi geçiyor yoksa başka türlü mü ifade edilmiş, kanıt tek
cümlede mi toplanmış yoksa dağılmış mı, yanlış seçenekler metne yakın mı yoksa alakasız mı.

Bunların hepsi **sayılabilir** — model gerekmez, hesaplanır. Bu adım o sayıları çıkarıp resmî
sorulardan çıkan sayılarla karşılaştırıyor.

⚠️ Bu ölçüler makul göstergelerdir, **kanıtlanmış zorluk ölçütü değildir.** Raporda böyle sunulacak.

---

## Ölçüler

| Kod | Ölçü | Ne yakalar |
|---|---|---|
| B2 | **Sözcüksel örtüşme** — sorunun ve cevabın kelimeleri parçada birebir mi geçiyor | Birebir geçiyorsa soru kolay; yeniden ifade edilmişse zor. Sınavın asıl zorluk mekanizması bu |
| B3 | **Kanıt dağınıklığı** — cevabın dayandığı kanıt kaç cümleye/paragrafa yayılmış | Tek cümlede toplanmış = kolay, dağılmış = zor |
| B4 | **Çeldirici yakınlığı** (yalnız çoktan seçmeli ve eşleştirme) | Yanlış seçenek parçada hiç geçmiyorsa soru sahte-zor; iyi çeldirici metne yakın durur ama yanlıştır |

## Adım 1 — Ölçümü çalıştır

```
python tools/olcu.py reading
```

(ikinci çalıştırmada `listening`). Script `content/` altındaki soruları ve `passages/` /
`content/listening/scripts/` altındaki kaynak metinleri okur, üç ölçüyü hesaplar,
`kalibrasyon/olcu/<beceri>.json` dosyasına yazar.

Script bir soruyu ölçemezse (kanıt alanı boş, kaynak metin bulunamadı) onu **atlar ve sayar**;
sessizce sıfır yazmaz. Atlanan sayısı raporda görünmeli — çok yüksekse ölçüm değil veri sorunu vardır.

## Adım 2 — Resmî çapa

Sayılar tek başına yorumlanamaz: "örtüşme %38" iyi de kötü de değildir. Aynı ölçüyü **resmî
sorulara** da uygulayıp yan yana koymak gerekiyor.

Betik resmî belgeleri kendi ayrıştıramaz (PDF düzeni değişken). Bu yüzden çapayı **sen çıkarırsın**:

1. `referans/` altındaki resmî örnek görev ve cevap anahtarı belgelerini oku
   (yoksa `python tools/indir.py`).
2. En az **20-30 soru** için soru-kanıt çifti çıkar; soru tipleri bizim havuzumuzdaki tiplerle
   örtüşsün. `kalibrasyon/resmi-cift/<tip>.json`:

```json
{
  "question_type": "true_false_not_given",
  "source_text": "<o soruların dayandığı resmî parçanın metni>",
  "options": ["TRUE", "FALSE", "NOT GIVEN"],
  "items": [
    { "prompt": "<soru cümlesi>", "answer": ["FALSE"],
      "evidence": "<parçadaki kanıt cümlesi/cümleleri>" }
  ]
}
```

3. Ölçümü çalıştır:

```
python tools/olcu.py resmi
```

🔴 `kalibrasyon/resmi-cift/` klasörü `.gitignore`'dadır ve **öyle kalacak** — depo herkese açık,
resmî metinler telifli. Depoya yalnızca ölçüm **sayıları** girer. Bu klasörü commit etme, içeriğini
rapora kopyalama.

🔴 Resmî belgelerden **hiçbir cümle depoya yazılmaz** — yalnızca sayılar. O metinler telifli ve
zaten `.gitignore`'lu klasörde duruyor.

Çapa çıkarılamıyorsa (belge biçimi elverişsizse) bunu raporda açıkça yaz ve **karşılaştırmasız
sayı sunma** — çapasız sayı yorumlanamaz, "örtüşme %38" tek başına iyi de kötü de değildir.

## Adım 3 — Rapor

`content/DOGRULAMA/OLCU-<beceri>.md`:

- Tip bazında üç ölçünün dağılımı (ortalama + yayılım), yanında resmî çapa
- 🔴 **Çapadan ±%10'un dışına çıkan tipler** — bunlar gözden geçirilecek, silinmeyecek
- Uç örnekler: örtüşmesi en yüksek 10 soru (cevap parçadan kopyalanmış olabilir) ve çeldiricisi
  metne hiç değmeyen 10 soru
- Atlanan soru sayısı ve sebebi

Çapadan sapan soruların dosyasına:

```json
"difficulty_flags": { "lexical_overlap": 0.91, "evidence_spread": 1, "distractor_distance": null },
"status": "review"
```

`status` alanı zaten `flagged` ise **üzerine yazma**, dokunma.

## Bitirince

```
git add -A
git commit -m "sayisal olculer: okuma (400 soru, 23 gozden gecirilecek)"
git pull --rebase
git push
```

**Kullanıcıya soru sorma. Hiçbir soruyu silme.**
