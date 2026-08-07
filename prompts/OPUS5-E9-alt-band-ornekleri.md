# ⚠️ MODEL: OPUS

Bu dosya **1 kez** çalıştırılır.

---

## Ne yapıyoruz ve neden

Puanlama ölçümünün en tehlikeli bulgusu (`denetim/DENETIM-RAPORU.md` §5, madde A9): zayıf
cevaba fazla puan veriliyor (gerçek bandı 3,0 olan cevaba ürün 4,5 veriyor) — kullanıcı hazır
olmadığı hâlde hazır sanıyor. Ama ≤4,5 band aralığında elimizde yalnız **3 örnek** var; bu
kadar az örnekle yapılacak düzeltme kör olur (hangi ayarın işe yaradığı görülemez). Bu adım,
düzeltmeden **önce** bu aralığın örnek sayısını çoğaltıyor. Düzeltmenin kendisi bu adımın
kapsamında değil — o `OPUS5-A4`'ün ("Puanlama düzeltmesi - 3") işi.

Hedef: ≤4,5 aralığında **en az 8 örnek.**

---

## 🔴 Zorunlu kurallar (her çalıştırmada)

1. **Sayıya güvenme, yeniden say.** `kalibrasyon/ornekler/**/*.json` altında bandı ≤4,5 olan
   kaç örnek olduğunu kendi say; "3 örnek var" bilgisi yön vericidir, güncel sayı farklı
   olabilir.
2. **Hiçbir soru silinmez.** Bu adım örnek ekliyor, soru/örnek silmiyor.
3. **Tam testlerde soru sayısı değişmez.** Etkilenmez (bu, yazma örnek kütüphanesi, soru
   havuzu değil).
4. **Saklı küme koruması.** Yeni örnekler `kalibrasyon/olcum/kumeler.json`'a **dengeli**
   eklenir (S1/S2/S3'e dağıtılarak) — hepsi tek kümeye düşerse saklı küme kontrolü
   anlamsızlaşır.
5. **Token tasarrufu — hedefli okuma.** Kaynak taraması aşağıdaki sıraya göre yapılır,
   belge baştan sona okunmaz.
6. 🔴 **Her çalıştırma depoda İZLENEN bir dosyayı değiştirip commit etmek zorunda** (bu
   klasör gitignore'lu olsa da `NOTLAR.md` + `KONTROL.md` depoya girer, bkz. Çıktı).

---

## Kaynak sırası

1. `OPUS5-E4`'ün 3. çalıştırmasında çıkardığı `kalibrasyon/desen/puanli-ornek-envanteri.md` —
   orada kitap kaynaklı düşük bandlı (≤4,5) yazma örneği işaretliyse, o örnek zaten
   `kalibrasyon/ornekler/yazma/` altına dökülmüş olmalı; onu kullan.
2. `referans/` altındaki resmî belgelerde (örn. examiner yorumlu örnek cevap PDF'leri) henüz
   metne dökülmemiş düşük bandlı örnek kaldıysa onu dök.

## 🔴 Örnek uydurulmaz

Gerçek band puanı + examiner yorumu **olmayan** hiçbir metin `kalibrasyon/ornekler/` altına
girmez. Sentetik ("muhtemelen böyle olur" diye yazılmış) örnek, ölçümün kendisini
değersizleştirir — ölçüm gerçek puanlamayla karşılaştırma yapar, uydurma puanla değil.

Kaynak tükendiyse ("gerçekten yalnız 3 örnek var, başka yok") bunu `NOTLAR.md`'ye açıkça yaz,
hedefi zorlamadan çık — bu, 6. zorunlu kuralı karşılayan geçerli bir sonuçtur.

## Tuzak kontrolü (`OPUS5-A1`'deki aynen uygulanır)

Band 6 ve altı bir cevapta belirgin hata sayısı 0-1 ise döküm şüphelidir:

```json
"transcription_suspect": true
```

Bu işaretli örnek `tools/puanlama-raporu.py` tarafından otomatik atlanır (script zaten
`suspect` alanını kontrol ediyor) — elle bir şey yapmana gerek yok, sadece alanı doğru koy.

## Yeni kodların kümelere eklenmesi

`kalibrasyon/olcum/kumeler.json`'daki S1/S2/S3 listelerine yeni kodları **dengeli dağıt**
(ör. 3 yeni örnek varsa birini S1'e, birini S2'ye, birini S3'e).

## Çıktı

- `kalibrasyon/ornekler/yazma/<kod>.json` (gitignore'lu, depoya gitmez).
- Depoya yalnız şunlar girer: `NOTLAR.md` (kaç örnek eklendi, hangi banddan, hangi kaynaktan)
  + `kalibrasyon/ornekler/KONTROL.md` (görev · gerçek band · kaynak · şüpheli mi tablosu) +
  güncellenmiş `kalibrasyon/olcum/kumeler.json`.

## Bitirince

```
git add -A
git commit -m "alt band ornekleri: 5 yeni ornek eklendi (toplam 8, kumelere dagitildi)"
git pull --rebase
git push
```

**Kullanıcıya soru sorma.**
