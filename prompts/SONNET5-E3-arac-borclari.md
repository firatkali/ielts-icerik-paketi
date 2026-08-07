# ⚠️ MODEL: SONNET

Bu dosya **1 kez** çalıştırılır.

---

## Ne yapıyoruz ve neden

Denetim raporu (`denetim/DENETIM-RAPORU.md` §5, madde A12) iki "araç borcu" tespit etti:
`tools/puanlama-raporu.py` saklı küme korumasını rapor biçimi yüzünden deliyordu (kümeleri
tek dosyada karıştırıyordu), `tools/kor-kopya.py`'nin eski oturumları temizlemesi gerekiyordu.
Bu adım ikisini de kapatıyor — biri gerçek bir kod değişikliği, öbürü sadece doğrulama.

Bundan sonraki bütün puanlama düzeltme oturumları (`OPUS5-A4`) bu adımın çıktısına göre
çalışacak: saklı kümeyi görmemesi gerekiyorsa artık o veri **hiçbir dosyada** önüne gelmeyecek.

---

## 🔴 Zorunlu kurallar (her çalıştırmada)

1. **Sayıya güvenme, yeniden say.** Değişiklikten önce ve sonra `python tools/dogrula.py` ve
   ilgili raporları çalıştırıp sayıları karşılaştır.
2. **Hiçbir soru silinmez.** Bu adım içerik değil araç değiştiriyor.
3. **Tam testlerde soru sayısı değişmez.** Etkilenmez, yine de dokunma.
4. **Saklı küme koruması** — bu adımın **konusu** bu; küçük bir sınamayla gerçekten
   çalıştığını göstermeden "düzeldi" deme.
5. **Token tasarrufu — hedefli okuma.** `tools/puanlama-raporu.py` ve `tools/kor-kopya.py`
   dışındaki dosyaları taramaya gerek yok.
6. 🔴 **Her çalıştırma depoda İZLENEN bir dosyayı değiştirip commit etmek zorunda.**

---

## Madde 1 — `tools/puanlama-raporu.py`: küme bölünmüş rapor

Bugün script tek bir `RAPOR-tur<N>.md` yazıyor; "Küme bazında" bölümü aynı dosyada duruyor,
yani düzeltme oturumunda saklı olması gereken kümenin sapma satırı da aynı dosyanın içinde —
okumaması gerekeni okumamak, dosyayı açmayan bir insana bile güvenmek demek, ki bu kırılgan.

Değişiklik:

- `RAPOR-tur<N>.md` **aynen üretilmeye devam etsin** (son rapor adımı — `OPUS5-A4` son
  çalıştırması — hâlâ onu okuyor, ismini kırma).
- Ek olarak, her küme için ayrı dosya yaz: `RAPOR-tur<N>-<KUME>.md` (ör. `RAPOR-tur3-S1.md`)
  — o kümenin örnek tablosu ve sapma satırları yalnız orada.
- Ayrıca örnek tablosu **içermeyen** bir `RAPOR-tur<N>-GENEL.md` yaz: genel özet, basari
  ölçütleri, beceri bazında tablo — ama "Ornek ornek" tablosu ve küme bazlı sapma satırları yok.

🔴 **Hesaplama mantığı değişmeyecek** — sadece çıktının hangi dosyaya, hangi bölümün gittiği
değişiyor. Sayılar birebir aynı kalmalı.

**Gerileme testi (zorunlu kanıt):** değişiklikten sonra `python tools/puanlama-raporu.py 3`
çalıştır, üretilen `RAPOR-tur3.md`'nin **sayılarının** (ortalama mutlak fark, eğilim, en büyük
sapma, tutarsızlık) değişiklik öncesiyle birebir aynı olduğunu doğrula ve bunu `NOTLAR.md`'ye
yaz (eski/yeni sayıları yan yana koy).

Bu değişiklikten sonra düzeltme oturumları (`prompts/OPUS5-A4-puanlama-duzeltmesi.md`) artık
yalnızca izinli küme dosyalarını (`RAPOR-tur<N>-GENEL.md` + izin verilen `RAPOR-tur<N>-<KUME>.md`
dosyaları) açacak; saklı kümenin kendi dosyasını hiç açmayacak.

Bu yüzden `prompts/OPUS5-A4-puanlama-duzeltmesi.md` içindeki "raporun saklı küme bölümünü
okuma" cümlesini, yeni dosya adlarını gösterecek şekilde **tek cümlelik** bir güncellemeyle
değiştir (ör. "Saklı kümenin `RAPOR-tur<N>-<KUME>.md` dosyasını hiç açma; yalnız
`RAPOR-tur<N>-GENEL.md` ve izinli kümelerin kendi dosyalarını oku.").

## Madde 2 — `tools/kor-kopya.py`: zaten çalışıyor, doğrula

Denetimde "temizlemiyor" denen davranış bugün depoda **mevcut** — script zaten önceki
oturumun `dogrulama/cevap/` klasörünü `dogrulama/cevap-arsiv/<damga>/` altına taşıyor
(satır 50-58, `shutil.move`). Görev: bunu **silmek değil doğrulamak.**

Küçük bir sınama yap: `dogrulama/cevap/` altına örnek bir dosya koy, `python tools/kor-kopya.py
<var-olan-bir-paket>` çalıştır, `dogrulama/cevap-arsiv/<damga>/` altına taşındığını gözle
doğrula. Çalışıyorsa A12'nin bu yarısını "kapandı" diye `NOTLAR.md`'ye yaz — **kodu değiştirme.**
Çalışmıyorsa (beklenmez ama) neyin bozuk olduğunu yaz, düzelt, aynı sınamayı tekrarla.

## Bitirince

```
git add -A
git commit -m "arac borclari: kumeli puanlama raporu + kor-kopya dogrulamasi"
git pull --rebase
git push
```

**Kullanıcıya soru sorma. Hiçbir soruyu silme.**
