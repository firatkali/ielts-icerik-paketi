# ⚠️ MODEL: OPUS

Bu dosya **3 kez** çalıştırılır: 1) cümle tamamlama + kısa cevap · 2) özet ailesi (kelime
bankalı + parçadan kelime) · 3) not/tablo/akış tamamlama + toplu rapor. Hangi çalıştırma
olduğun sana ek talimatta söylenir.

---

## Ne yapıyoruz ve neden

`OPUS5-B1` ölçümü şu soruyu soruyor: "cevabın **3/3 turda kelimesi kelimesine** tuttu mu?"
Bu, tamamlama ailesinde sızıntının **yarısını kaçırıyor.** Denetimin kendi bulgusu
(`denetim/DENETIM-RAPORU.md` §3, "üç dürüstlük notu"): anlam düzeyinde bakıldığında cümle
tamamlama %81, parçadan-kelime özet %93 oranında **zaten biliniyordu** — puanı düşük gösteren
şey kavrayışın zayıf olması değil, "parçadan kelime kopyala" kuralının kelimeyi birebir
tutturmayı zorlaştırmasıydı (model anlamı doğru biliyor ama farklı bir kelime/çekimle
yazıyor, kelime eşleşmesi script'te "yanlış" sayılıyor).

Bu adım **yeni bir ölçüm turu koşturmuyor** — mevcut `kalibrasyon/metinsiz/<paket>-tur<N>.json`
dökümlerini (modelin daha önce parçasız verdiği cevapları) **yeniden değerlendiriyor**: model
parçayı görmeden cevabı **anlamca** bildiyse (eş anlamlı kelime, farklı çekim, doğru kavram
ama yanlış yüzey kelime), bu da "biliniyor" sayılır.

---

## 🔴 Zorunlu kurallar (her çalıştırmada)

1. **Sayıya güvenme, yeniden say.** Plandaki "cümle tamamlamada ~19, özet ailesinde ~15"
   rakamları **hedef değil yön vericidir.** Kendi bulduğun sayı farklı çıkabilir, olduğu gibi
   yaz.
2. **Hiçbir soru silinmez.** Yeni işaretlenen soru `status: "flagged"` olur, silinmez.
3. **Tam testlerde soru sayısı değişmez.** Bu adım işaretleme yapıyor, soru eklemiyor/çıkarmıyor.
4. **Saklı küme koruması** — geçerli değil (puanlama dosyası açılmıyor).
5. **Token tasarrufu — hedefli okuma.** Bu adım **yeni parça okumaz** — mevcut
   `kalibrasyon/metinsiz/` dökümlerini ve ilgili soru dosyalarını okur; okuma parçasının
   kendisini (`passages/`) açmaya gerek yok, yalnız verilen cevap ile gerçek cevabı
   karşılaştırıyorsun.
6. 🔴 **Her çalıştırma depoda İZLENEN bir dosyayı değiştirip commit etmek zorunda** (en az
   `NOTLAR.md`'ye bir bölüm).

---

## Yöntem — üç çalıştırmada ortak

1. İlgili paketlerin `kalibrasyon/metinsiz/<paket>-tur1/2/3.json` dosyalarını oku (3 tur da
   var olmalı; yoksa o paket bu turda atlanır, sebebi `NOTLAR.md`'ye yaz).
2. Her soru için üç turun **üçünü de** oku. Gerçek cevaba (`answer` + `accepted_variants`)
   bak.
3. Karar: model **anlamca** doğru cevap verdi mi? Şunlar "anlamca doğru" sayılır:
   - eş anlamlı kelime (`designation` yerine `title`/`name` gibi anlamı karşılayan kelime)
   - farklı çekim/biçim (`reflect` yerine `reflects`/`reflecting`)
   - doğru kavram, yüzeyde farklı ifade (sayının yazıyla/rakamla yazılması, kısaltma/açık hali)
   Şunlar **anlamca da yanlış** sayılır: yanlış kavram, yanlış sayı/isim, konuyu tutturmuş ama
   sorulan ayrıntıyı tutturmamış cevap.
   🔴 **Üç turun üçünde de anlamca doğruysa** "anlam düzeyinde biliniyor" sayılır — tek turda
   tutturmak (kelimece de, anlamca da) hâlâ şans olabilir.
4. Anlamca bilinen ama daha önce (kelime düzeyinde) "bilinmiyor" sayılmış her soruya yeni
   işaretleme uygula (aşağıda).

## 1. çalıştırma — Cümle tamamlama + kısa cevap

Paketler: `sentence-completion`, `short-answer` (okuma, tüm test + alıştırma dosyaları).

## 2. çalıştırma — Özet ailesi

Paketler: `summary-completion` (hem kelime bankalı hem metinden-kelime alt tipi).

## 3. çalıştırma — Not/tablo/akış tamamlama + toplu rapor

Paketler: `note-completion`, `table-completion`, `flow-chart-completion`. Bu üçü bitince
**toplu raporu** yaz (aşağıda).

## İşaretleme (silme değil, ekleme)

Anlamca bilinen her soruya, **orijinal dosyasında**, aynı şema:

```json
"blind_solvable": true,
"blind_basis": "logic",
"status": "flagged",
"flag_reason": "Parça gösterilmeden anlamca 3/3 turda doğru bilindi: farklı kelimeyle ama doğru kavramla cevaplandı.",
"flag_mechanism": "esdizim_kilidi"
```

🔴 **Mevcut `blind_solvable: false` işaretleri silinmez** — yalnızca yeni anlamca-doğru
bulgular eklenir; eski kelime-düzeyi ölçüm bulguları da dursun (ikisi farklı şeyi ölçüyor).

## Çıktı

`content/DOGRULAMA/ANLAM-DUZEYI-RAPOR.md` (3. çalıştırmada tamamlanır, ilk iki çalıştırma
kendi bölümünü **ekler**):

- Paket bazında: kelime-düzeyi oran (eski ölçüm) vs anlam-düzeyi oran (yeni ölçüm), fark.
- Toplam yeni işaretlenen soru sayısı (kendi sayımınla, plandaki ~19/~15 sadece yön verir).
- 3-4 somut örnek: gerçek cevap → modelin anlamca doğru ama kelimece farklı cevabı.
- Son cümle: "Bu ölçüm anlam düzeyinde bilinen soruyu bulur, kelime tutturma başarısını değil."

## Bitirince (her çalıştırmada)

```
git add -A
git commit -m "anlam duzeyi olcut: cumle tamamlama + kisa cevap yeniden degerlendirildi"
git pull --rebase
git push
```

**Kullanıcıya soru sorma. Hiçbir soruyu silme.**
