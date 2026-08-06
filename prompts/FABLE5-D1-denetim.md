# ⚠️ MODEL: FABLE

Bu dosya **3 kez** çalıştırılır: 1) envanter uyuşması · 2) çapraz kontrol özeti · 3) denetim raporu.
Hangi çalıştırma olduğun sana ek talimatta söylenir.

---

## Ne yapıyoruz ve neden

Bütün üretim ve ölçüm işleri bitti. Bu adım **bağımsız bir denetçi gözüyle** son duruma bakıyor:
sayılar hedefle uyuşuyor mu, çapraz kontrol nerelerde sorun buldu, ölçüm raporları ne diyor.

🔴 **EN ÖNEMLİ KURAL: Bu adım RAPOR YAZAR, KARAR VERMEZ.**
- Hiçbir soruyu silme, düzeltme, işaretleme veya işaretini kaldırma.
- `content/`, `passages/`, `degerlendirme/`, `kalibrasyon/` altındaki **hiçbir dosyayı değiştirme** — sadece oku.
- Tek yazacağın yer: `denetim/` klasörü.
- Sorun bulursan raporda listele ve seçenekleri yaz; eleme/kabul kararını proje sahibi verecek.

Raporlar proje sahibi için yazılıyor: **düz Türkçe, dürüst, süslemesiz.** Sorun varsa açıkça yaz,
yoksa "sorun yok" de — iyimser yuvarlama yapma.

---

## 1. çalıştırma — Envanter uyuşması → `denetim/envanter.md`

1. `python tools/manifest.py` çalıştır (güncel `content/MANIFEST.json` üretir).
2. `content/PLAN-soru-dagilimi.md` içindeki hedeflerle karşılaştır.
3. `denetim/envanter.md` dosyasına yaz:
   - Beceri bazında **hedef / üretilen / fark** tablosu (okuma, dinleme, konuşma, yazma, pasaj).
   - Soru tipi bazında aynı tablo — hangi tipte eksik var, kaç tane.
   - `status: "flagged"` olan soruların sayısı **ayrı sütunda**: işaretliler düşülünce
     kullanılabilir sayı hedefi tutuyor mu?
   - Cevap anahtarı, açıklama (`explanation`) veya kanıt alanı **boş** olan soru var mı — varsa
     dosya adı + soru numarasıyla listele.
   - Sonunda tek cümlelik özet: envanter tamam mı, değilse en büyük eksik ne.

## 2. çalıştırma — Çapraz kontrol özeti → `denetim/capraz-ozet.md`

1. `content/DOGRULAMA/` altındaki bütün `.json` raporlarını ve `RAPOR.md`'yi oku.
2. `content/` altındaki `status: "flagged"` soruların `flag_reason` alanlarını topla.
3. `denetim/capraz-ozet.md` dosyasına yaz:
   - Toplam kaç soru doğrulandı, kaçı işaretlendi, genel uyuşma oranı.
   - **Soru tipi bazında** işaretlenme oranı tablosu — işaretler belli tiplerde mi yoğunlaşıyor?
   - **Üreten model bazında** kırılım (hangi paketleri hangi model üretmişti, işaret oranları farklı mı).
   - `flag_reason` metinlerindeki **tekrarlayan temalar** (ör. hep NOT GIVEN / FALSE ayrımı mı,
     hep çeldirici sorunu mu) — en sık 3-5 tema, her birine bir örnek.
   - Deseni yorumla: bu bir **üretim hatası deseni** mi (aynı hata sistematik tekrarlıyor) yoksa
     dağınık tekil hatalar mı? Sistematikse hangi soru tipleri risk altında?

## 3. çalıştırma — Denetim raporu → `denetim/DENETIM-RAPORU.md`

Proje sahibinin okuyacağı **tek dosya** bu. Önce şunları oku:
- `denetim/envanter.md` + `denetim/capraz-ozet.md` (ilk iki çalıştırmanın çıktısı)
- `kalibrasyon/olcum/SONUC.md` (puanlama son raporu — başarı ölçütleri tuttu mu)
- Bozuk soru ayıklama sonuçları (metinsiz çözümde işaretlenenler) ve
  `kalibrasyon/olcu/` altındaki sayısal ölçü raporları
- `content/DOGRULAMA/RAPOR.md`

Sonra `denetim/DENETIM-RAPORU.md` dosyasını yaz:

1. **Genel durum** — üç cümleyle: içerik teslim edilebilir durumda mı?
2. **Sayılar** — envanterin özeti (hedef/üretilen/kullanılabilir).
3. **Kalite** — çapraz kontrol + metinsiz çözüm + sayısal ölçülerin birleşik özeti;
   hangi soru tipleri sağlam, hangileri şüpheli.
4. **Puanlama** — ölçüm turlarının sonucu; ölçütler tuttuysa hangi payla, tutmadıysa nerede.
5. **Açık sorunlar** — proje sahibinin karar vermesi gereken her madde, her birinde:
   sorun ne · kaç soruyu etkiliyor · seçenekler ne (ör. "işaretlileri at" / "elden geçir" /
   "bu tipte yeni üretim"). **Öneri yazabilirsin ama "yapıldı" diye bir şey olmayacak.**
6. **Denetimin sınırları** — bu denetimin göremeyeceği şeyleri dürüstçe say (ör. soruları
   üreten modellerle aynı aileden bir model denetliyor; cevap doğruluğunun son sözü
   farklı aileden yapılacak ikinci süzgeçte).

## Bitirince (her çalıştırmada)

```
git add denetim/ && git commit -m "denetim: <hangi çalıştırma>" && git push
```
