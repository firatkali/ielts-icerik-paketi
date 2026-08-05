# ⚠️ MODEL: OPUS

Bu dosya **3 kez** çalıştırılır: 1. düzeltme · 2. düzeltme · son rapor. Hangisi olduğun ek
talimatta yazar; yazmıyorsa `kalibrasyon/olcum/` klasörüne bakıp sıradakini yap.

🔴 **Bir ölçüm turu bitmeden bu adım çalıştırılmaz.** Sıra: ölç → düzelt → ölç → düzelt → ölç → rapor.

---

## Ne yapıyoruz ve neden

Önceki adımda, bizim puanlama talimatımızın gerçek sınav puanlarından ne kadar saptığı ölçüldü.
Bu adım o sapmanın **sebebini bulup talimatı düzeltiyor**. Amaç modelin daha "iyi" puan vermesi
değil, **gerçek puana yaklaşması** — sürekli cömert davranıyorsa sıkılaştırmak, sürekli cimriyse
gevşetmek, belirli bir ölçütte savruluyorsa o ölçütün tanımını netleştirmek.

---

## 🔴 Saklı küme kuralı (atlanamaz)

| Bu çalıştırma | Görebileceğin kümeler | SAKLI |
|---|---|---|
| 1. düzeltme | S1 + S2 | **S3** |
| 2. düzeltme | S2 + S3 | **S1** |
| Son rapor | hepsi (artık düzeltme yapılmıyor) | — |

Saklı kümedeki örneklerin cevaplarını, gerçek bandlarını, sapma satırlarını **açma.**
`tools/puanlama-raporu.py` raporunun saklı küme bölümünü de okuma.

Sebep: talimatı gördüğün örneklere göre tek tek ayarlarsan model o örnekleri ezberler, sapma
raporda küçülür ama gerçekte düzelmez. Saklı küme bunu yakalayan tek şey. Açık kümede iyi +
saklı kümede kötü = o düzeltme geçersiz.

---

## Adım 1 — Raporu oku, örüntü ara

`kalibrasyon/olcum/RAPOR-tur<N>.md` + izinli kümelerin tek tek puanlamaları.

Tek tek örneklere değil **örüntüye** bak:

- Sapma **her bandda aynı yönde** mi (sistematik cömertlik/cimrilik) — bunu düzeltmek en kolayı.
- **Üst bandlar sıkışıyor** mu (8 ve 9'a hiç çıkmıyor, hepsini 7-7,5 veriyor)?
- **Alt bandlar şişiyor** mu (band 4 cevaba 6 veriyor)? Bu en tehlikelisi: kullanıcı hazır
  olmadığı hâlde hazır sanır.
- Sapma **tek bir ölçütten** mi geliyor (ör. dilbilgisi doğru, görev yanıtı savruk)?
- **Yazma ile konuşma** farklı mı davranıyor?
- Aynı cevaba farklı puanlar (tutarsızlık) belirli bir band aralığında mı yoğunlaşıyor?

## Adım 2 — Talimatı düzelt

`degerlendirme/` altındaki ilgili dosyaları düzenle. Her düzenleme bir örüntüye dayanmalı.

İzin verilen düzeltmeler:
- ölçüt tanımını netleştirmek, sınır durumları örneklemek
- band ayrımını keskinleştirmek ("6 ile 7 arasındaki fark şudur")
- çıktı şemasını daraltmak
- puanlama sırasını değiştirmek (ör. önce ölçüt, sonra genel band)

🔴 **Yasak olanlar:**
- Örneğe özel kural yazmak ("grafik betimleyen cevaplarda 0,5 düş" gibi) — bu ezberdir.
- Talimata gerçek band puanı veya örnek cevabın kendisini gömmek.
- Ölçüt sayısını/ağırlığını değiştirmek (yazma 4, konuşma 3 — sabit).
- Telaffuzu geri getirmek (modele ses gitmiyor).
- Çıktıyı uzatmak; uzunluk sınırı maliyet kararıdır.

Her değişikliği `degerlendirme/DEGISIKLIK-KAYDI.md`'ye yaz: hangi örüntü → hangi değişiklik →
beklenen etki. Sonraki ölçüm bu beklentiyi sınayacak.

## Adım 3 — Son rapor çalıştırması

Düzeltme yapma. `kalibrasyon/olcum/SONUC.md` yaz:

1. Üç turun ölçüleri yan yana tablo (ortalama mutlak fark · eğilim · en büyük sapma · tutarsızlık).
2. **Saklı küme ile açık küme karşılaştırması.** İkisi arasında belirgin fark varsa
   🔴 **büyük harfle yaz: ayar örneklere ezberlenmiş olabilir.**
3. Başarı ölçütleri tutuyor mu — tek tek, geçti/kaldı.
4. **Ürünün gerçek davranışı**: tek seferlik puanların dağılımı (ortalama değil). Kullanıcı tek
   puan alıyor; "ortalamada iyi" yetmez.
5. Kalan riskler. En az şunlar yazılacak, sonuç iyi çıksa bile:
   - Konuşmada **Part 1 örneği yok** → tanışma sorularında davranış ölçülmedi.
   - Örnek sayısı az (band başına 1-2) → **band bazlı ince ayar yapılamaz.**
   - Puanlayan da, talimatı yazan da, örnekleri döken de aynı model ailesi → ortak kör noktalar
     görünmez. Farklı aileden ikinci bir puanlayıcıyla kontrol **proje sahibinde bekliyor**.
6. 🔴 Kapanış cümlesi: bu iş **yazma ve konuşma puanlamasının** güvenilirliğini ölçer.
   Okuma/dinlemede "kaç doğru = hangi band" eşiğini **doğrulamaz** — o ancak canlı kullanım
   verisiyle ayarlanır. Bu yüzden üründe **"tahmini band"** ibaresi kalkmaz.

## Bitirince

```
git add -A
git commit -m "puanlama duzeltmesi 1: ust bandlar sikisiyordu"
git pull --rebase
git push
```

**Kullanıcıya soru sorma.**
