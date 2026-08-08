# Dinleme sızıntı ölçümü — senaryo gösterilmeden soru bilinebiliyor mu

## Yöntem notu — okuma ölçümünden dört farkı

**1. Gizlenen şey pasaj değil, ses metni.** Okuma tarafındaki `METINSIZ-*` ölçümü soruyu
pasajdan ayırıyordu; burada soru **ses metninden** (`content/listening/scripts/`) ayrılıyor.
Ölçülen soru şu: "senaryo hiç gösterilmeden bu soru bilinebiliyor mu?" Bu yüzden kopyadan
cevapla birlikte her senaryo izi de silinir — `script_id`, `turn_index`, `answer_point_id`,
`context_line`, `section`, `visual`. `context_line` (senaryonun bir cümlelik tanıtımı) okuma
tarafındaki `passage_title`ın karşılığıdır: konuyu ele verdiği için kopyaya girmez. Modelin
gördüğü tek şey yönergedir + soru kökü + seçenekler/gövde.

**2. Dosya adı çakışması ayrı araç gerektirdi.** Okuma ve dinlemede paket adları aynı
(`multiple-choice.json`, `matching.json`…). `tools/metinsiz-kopya.py` `skill != "reading"`
olan dosyaları bilerek atlar — bu, dinlemenin okumanın ölçüm altyapısını bozmaması için
vardır ve değiştirilmedi. Onun yerine yanına dinleme sürümleri yazıldı:
`tools/sessiz-kopya.py` (→ `dogrulama/sessiz/`, gitignore'da) ve `tools/sessiz-rapor.py`
(→ `content/DOGRULAMA/SESSIZ-*`). İkisi `skill != "listening"` olanı atlar; okumanın
`dogrulama/metinsiz/`, `kalibrasyon/metinsiz/`, `METINSIZ-*` dosyalarına ne okur ne yazar.

**3. Bazı tipler yapısal olarak tahmin edilemez.** Form/not/tablo tamamlamada cevap çoğu
zaman özel ad, sayı ya da saattir. Orada düşük parçasız-bilinme oranı **beklenir ve başarı
sayılmaz** — ölçünün asıl ilgilendiği yer çoktan seçmeli + eşleştirmedir, çünkü orada cevap
bir seçenek havuzundan gelir ve sızıntı seçeneğin sözünden okunabilir.
`plan-map-diagram-labelling` hiç ölçülmedi: görsel gerektirir, metin tabanlı ölçüm orada
kördür (okuma tarafındaki diyagram etiketleme kararının aynısı).

**4. Karşılaştırma tabanı yok.** Okuma raporundaki `RESMI_TABAN` resmî okuma örnek
sorularından ölçülmüştü; dinlemede böyle bir ölçüm hiç yapılmadı
(`denetim/DENETIM-RAPORU.md` §5, madde A3). Bu yüzden bu raporda tabanla karşılaştırma
yapılmaz ve uydurulmuş bir taban sayısı yazılmaz — oranlar kendi içinde, tip bazında okunur.

**Sayım (rule 1, yeniden sayıldı):** dinlemede 352 soru kalemi / **360 numaralı soru**
(aralıklı numaralar açılmış hâliyle) · alıştırma 120 numara, tam testler 240 numara
(L1–L6 × 40, `tools/dogrula.py` tam test bütünlüğü 6/6 TAM). Hiçbir soru silinmedi.

### Ölçüt

Bir soru **üç turun üçünde de** doğru bilinmişse "senaryosuz çözülebilir" sayılır; tek turda
tutturmak şanstır. İki ölçüt ayrı raporlanır: **K1** kelime düzeyi (birebir ya da
`accepted_variants`) ve **K3** anlam düzeyi (`OPUS5-E10` tanımı: kelime kelime tutturma değil,
anlamca bilme). Çoktan seçmeli ve eşleştirmede cevap bir harf olduğu için K1 = K3; K3 asıl
farkı tamamlama ailesinde yapacak (3. ve 4. çalıştırma).

---

## 1. çalıştırma — çoktan seçmeli (tek cevaplı) · 2026-08-08

**Kapsam:** 7 dosya (alıştırma + L1–L6), **37 tek cevaplı** soru. `multiple-choice.json`
içindeki 3 kalem "TWO letters" (çok cevaplı) olduğu için bu tura girmedi — onlar
`multiple-choice-multi` ile birlikte 2. çalıştırmada ölçülecek (`--secim=tek/cok` ayrımı
`select_count` ve aralıklı numaradan yapılıyor, cevap anahtarına bakılmadan).

| Ölçüt | Sonuç |
|---|---|
| Ölçülen soru | 37 |
| 3/3 turda senaryosuz bilinen (K1 = K3) | **25 (%67.6)** |
| Bunlardan dayanağı **anlamsal** olan (aşağı bak) | **21 (%56.8)** |

### Kararın dayanağı — 3/3 bilinen 25 sorunun dağılımı

| Dayanak | 3/3 bilinen | Bilinmeyen | Yorum |
|---|---|---|---|
| `option_wording` | 9 | 1 | Seçeneğin kendi sözü doğruyu işaretliyor: üç seçenekten biri kavramın tanımını yeniden söylüyor, diğer ikisi yüzeysel/ilgisiz kalıyor. **Asıl sızıntı burada.** |
| `general_knowledge` | 8 | 0 | Cevap dünya bilgisiyle biliniyor, sesi dinlemek gereksiz. Bir soruda seçenekler bir terimin ne yaptığını soruyor ve doğru seçenek terimin gerçek işlevi — ses olmadan da doğru. |
| `logic` | 3 | 3 | Seçenekler arası mantıksal ilişki (biri diğerini dışlıyor, biri nedensel olarak tek uyan). Yarı yarıya. |
| `number_guess` | 4 | 8 | Saat/fiyat/miktar seçimi. 12 soruda 4 tutturma ≈ üç seçenekli şans oranı (%33). **Sızıntı sayılmamalı** — aşağıdaki uyarıya bak. |
| `cross_question` | 1 | 0 | Bir sorunun kökü bir sonraki sorunun cevabını veriyor ("**yeni salon** kaç tezgâh alacak?" sorusu, "pazar nereye taşınıyor?" sorusunun cevabını söylüyor). Paket içi tutarlılık kusuru. |

### 🔴 Ölçütün bu turda ortaya çıkan zayıf noktası

"Üç turda aynı cevabı verdi" ölçütü, **kararlı ama şanslı** bir sezgiyi gerçek sızıntıdan
ayırmıyor. Model deterministik bir sezgi kullanıyorsa (ör. "üç sayı arasında ortadaki yuvarlak
olmayan değer seçilir") üç turda da aynı yanıtı verir; doğru çıkarsa 3/3 görünür, ama soru
sızdırmıyordur. Bu turda `number_guess` dayanaklı 12 sorudan 4'ü böyle: tutturma oranı
(%33) tam olarak şans oranı. Bu yüzden yukarıdaki tabloda iki sayı ayrı verildi:
**ham 25 (%67.6)** ve **dayanağı anlamsal olan 21 (%56.8)**. İşaretlemede (5. çalıştırma)
esas alınacak olan ikincisidir; `number_guess` 3/3'leri işaretlenmeyecek, ama listede
şeffaflık için duracak.

### Şimdilik ne yapıldı, ne yapılmadı

- Ölçüm yapıldı, ham veri `content/DOGRULAMA/SESSIZ-multiple-choice-tek.json` içinde
  (soru bazında kaç turda doğru + 3/3 listesi).
- **İşaretleme yapılmadı** — plana göre bütün paketlerin işaretlemesi 5. çalıştırmada,
  tek tip cümleyle, bir kerede yapılacak (E1'in dersi). Hiçbir soru silinmedi, tam
  testlerin soru sayısı değişmedi.
- Bu turda ses metnine, senaryo klasörüne ve cevap anahtarına hiç bakılmadı;
  `tools/_e8_sizinti_kontrol.py` kopyada yasaklı alan kalmadığını doğruladı (0 ağır hata).

🔴 Bu ölçüm bozuk soruyu bulur, zorluk ölçmez.
