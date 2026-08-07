# ⚠️ MODEL: SONNET

Bu dosya **1 kez** çalıştırılır.

---

## Ne yapıyoruz ve neden

Denetim raporu bir kusur buldu (`denetim/DENETIM-RAPORU.md` §5, madde A2): işaretli (`status:
"flagged"`) okuma sorularının **hepsinde birebir aynı `flag_reason` cümlesi** yazıyor —
"Parça gösterilmeden 3/3 turda doğru bilindi; genel kültürle çözülebiliyor." Oysa `blind_basis`
alanına bakıldığında gerçek sebep sorudan soruya değişiyor: kimi soru gerçekten genel kültürle
çözülüyor, kimi seçeneklerin dilinden (`option_wording`), kimi mantıkla elemeden (`logic`),
kimi düz tahminden (`guess`).

Bu tek tip cümle tehlikeli çünkü **sonraki adım (E5) buna göre düzeltme yapacak.** Yanlış
gerekçeye göre düzeltme yapılırsa yanlış kusur düzeltilmiş olur — soru bozuk kalır.

Bu adım hiçbir soruyu değiştirmiyor, yalnız **her sorunun kendi gerçek mekanizmasını** yazıyor.

---

## 🔴 Zorunlu kurallar (her çalıştırmada)

1. **Sayıya güvenme, yeniden say.** Denetim raporu 180 diyor, bugün farklı bir sayı olabilir.
   `python tools/dogrula.py` / `python tools/manifest.py` ile **kendi sayımını yaparak** başla;
   plandaki/rapordaki sayılar yön verir, hedef değildir.
2. **Hiçbir soru silinmez.** Elenen soru `status: "rejected"` + `reject_reason` alır, dosyada kalır.
3. **Tam testlerde soru sayısı değişmez.** AC1–AC4, GT1–GT2, L1–L6 her biri 40 soru; elden çıkan
   her yuva aynı numarayla yenisiyle doldurulur (`tools/dogrula.py` bunu denetliyor).
4. **Saklı küme koruması** (yalnız puanlama dosyalarında) — bu çalıştırma puanlama dosyası
   açmıyor, geçerli değil.
5. **Token tasarrufu — hedefli okuma.** Önce içindekiler/dizin, sonra yalnız gereken sayfa
   aralığı; tüm belge hiçbir zaman baştan sona okunmaz. Okunan sayfa aralıkları `NOTLAR.md`'ye
   yazılır.
6. 🔴 **Her çalıştırma depoda İZLENEN bir dosyayı değiştirip commit etmek zorunda** (en az
   `NOTLAR.md`'ye bir bölüm). Sebep: `calistir.py` ilerlemeyi depo imzasına bakarak sayıyor;
   hiçbir şey yazmayan çalıştırma "olmadı" sayılır ve **sonsuza kadar tekrarlanır**. İş
   yapılamıyorsa bile sebep `NOTLAR.md` + `UYARILAR.txt`'ye yazılıp commit edilecek.

---

## Girdi

1. `content/` altındaki `status: "flagged"` okuma soruları (`grep -rl '"status": "flagged"'`
   ile tarayabilirsin) — her birinin `blind_basis` alanı.
2. `content/DOGRULAMA/METINSIZ-*.md` — her paketin soru soru dökümü; hangi soru hangi turda
   hangi gerekçeyle (`basis`) bilindi, oradan görünüyor.
3. `denetim/DENETIM-RAPORU.md` §3 — iki sistematik desenin özeti (aşağıda tekrarlanıyor,
   yön verici, tek başına yeterli değil):
   - **Seçenek metinli tipler** (çoktan seçmeli, YES/NO/NOT GIVEN, cümle sonu eşleştirme):
     doğru cevap ölçülü ifade taşıyor ("may", "probably"), çeldirici mutlaklık taşıyor
     ("clearly", "only") — bu **kip imzası**. Ayrıca bazı harf çiftleri (ör. A+G) tekrar tekrar
     çeldirici/doğru oluyor — bu **konumsal düzen**.
   - **Tamamlama ailesi** (cümle/özet/not/tablo/akış tamamlama): boşluk ya kalıp bir öbeğin
     tahmin edilebilir ucunda ("an up-to-date ___" → CV) — bu **eşdizim kilidi** — ya da
     kelime bankası/tanım metninin kendisi cevabı sızdırıyor — bu **tanım sızıntısı**.

## İş

Her işaretli sorunun `flag_reason` metnini **yeniden yaz.** Dört kalıptan hangisine
uyduğuna `blind_basis`, METINSIZ dökümündeki `basis` dağılımı ve sorunun kendi metni karar
verir:

| `blind_basis` | Olası mekanizma | `flag_reason` neyi anlatmalı |
|---|---|---|
| `general_knowledge` | `genel_kultur` | Cevabın parçaya değil dünya bilgisine dayandığı, **hangi bilgiye** dayandığı somut olarak |
| `option_wording` | `kip_imzasi` veya `konumsal_duzen` | Doğru seçenek ile çeldiricinin kesinlik derecesi/kalıbı nasıl ayrışıyor, **bu sorudaki** somut kelime çiftiyle |
| `logic` | `esdizim_kilidi` veya `konumsal_duzen` | Seçenekler elemeyle mi çözülüyor, boşluk tahmin edilebilir bir kalıbın ucunda mı |
| `guess` | `belirsiz` | Net bir mekanizma yoksa böyle işaretlenir; bu kalıp **istisna** olmalı, çok sık çıkarsa yöntemi gözden geçir |

🔴 **Tek tip cümle yasak.** Her `flag_reason`, o sorunun **kendi** kelimesini/kalıbını/tanımını
adıyla anmalı (ör. "Boşluk 'an up-to-date ___' kalıbının ucunda, tek doğal tamamlama 'CV' —
parçaya bakmadan da tahmin edilir." gibi somut ve o soruya özel).

### Ek alan: `flag_mechanism`

Her işaretli soruya, `flag_reason`'a ek olarak şu alanı yaz — E5 bu alana göre soruları
gruplara bölecek:

```json
"flag_mechanism": "kip_imzasi"
```

Değerler: `kip_imzasi` · `esdizim_kilidi` · `tanim_sizintisi` · `konumsal_duzen` ·
`genel_kultur` · `belirsiz`.

## Yasak

- Soru metnine, cevaba (`answer`), `evidence`'a dokunma.
- `status` değerini değiştirme — hâlâ `"flagged"` kalır, burada karar verilmez.
- `blind_solvable` alanına dokunma.

## Çıktı

1. İçerik dosyalarındaki `flag_reason` + yeni `flag_mechanism` alanları (yerinde güncelleme).
2. `content/DOGRULAMA/ISARET-GEREKCELERI.md`:
   - Mekanizma × soru tipi dağılım tablosu (kaç soru hangi mekanizma, hangi tipte).
   - Her mekanizmadan 2-3 örnek: dosya + soru numarası + yeni `flag_reason`.
   - Toplam işaretli soru sayısı (yeniden sayılmış) ve `belirsiz` sayılan soru sayısı — bu
     sayı yüksekse (ör. %20'nin üstünde) bunu raporda açıkça belirt, E5'e devredilecek not.

## Bitirince

```
git add -A
git commit -m "isaret gerekceleri: 180 soru mekanizmaya gore yeniden yazildi"
git pull --rebase
git push
```

**Kullanıcıya soru sorma. Hiçbir soruyu silme.**
