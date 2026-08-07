# -*- coding: utf-8 -*-
"""6. calistirmanin bolumunu METINSIZ-RAPOR.md'ye ekler (kapanis blogunun oncesine)."""
import io

BOLUM = u"""## 6 — note-completion + table-completion (2026-08-07)

- Ölçülen soru: **45** (6 dosya — note-completion 33, table-completion 12)
- Üç turun üçünde de parçasız bilinen: **13** — **%28.9**
- Üç turda aynı cevabın verildiği soru: 25/45 (%56) — önceki beş çalıştırmanın en
  düşüğü. Beklenen bir sonuç: burada şık yok, aday boşluğa **kelime** yazıyor; aynı
  anlamı farklı kelimeyle vermek mümkün olduğu için turlar doğal olarak ayrışıyor.

### Tip bazında

| Soru tipi | Bizde | Oran | Resmî taban | Sapma |
|---|---|---|---|---|
| note_completion | 9/33 | %27 | 6/6 (%100) | tabanın **altında** |
| table_completion | 4/12 | %33 | 0/5 (%0) | 🔴 tabanın **üstünde** |

🔴 **table_completion tek uyarı veren tip.** Resmî örneklemde tablo tamamlama 0/5 ile
diyagram etiketlemeyle birlikte en sızıntısız tipti; bizde %33. Sebebi aşağıda ayrı
başlıkta — kısaca: **bizim tablo hücrelerimiz veri değil cümle.**

⚠️ İki taban da küçük: resmî taraf tip başına 5-6 soru, bizim table_completion
örneklemimiz 12 soru. %33 ile %0 arasındaki fark 4 soruya dayanıyor; yön güvenilir,
büyüklük değil.

note_completion tersi yönde: %27 ile hem kendi resmî tabanının (6/6) hem genel resmî
ortalamanın (%57) belirgin altında. Resmî 6/6 rakamı altı soruya dayandığı için
gerçekçi bir tavan değil, ama yön açık: not tamamlama bu pakette sağlam çalışıyor.

### Set bazında dağılım

| Set | Tip | Soru | 3/3 bilinen | Oran |
|---|---|---|---|---|
| practice | note | 15 | 2 | %13 |
| AC1 | note | 6 | 2 | %33 |
| AC4 | note | 6 | 2 | %33 |
| GT1 | note | 6 | 3 | **%50** |
| AC3 | table | 6 | 2 | %33 |
| GT2 | table | 6 | 2 | %33 |

practice (%13) en sağlamı; 15 sorunun 13'ü parçasız bilinemedi. GT1 (%50) yine zayıf
halka — 1. ve 3. çalıştırmadaki GT bulgusunun tekrarı. Ama 5. çalıştırmada GT setleri
0/14 ile en temiz sonuçtu; yani sorun GT **malzemesinde** değil, GT malzemesine
sorulanın çoğu zaman "kural" olmasında. Kural, hayat bilgisiyle biliniyor.

### İşaretlenen 13 soru

| Soru | Anahtar | Zorluk | Dayanak |
|---|---|---|---|
| practice 1 | `47` | easy | general_knowledge |
| practice 10 | `500` | easy | general_knowledge |
| AC1 4 | `tyre` | medium | general_knowledge |
| AC1 5 | `corner` | medium | logic |
| AC4 4 | `headphones` | easy | logic |
| AC4 5 | `novelty` | hard | guess |
| GT1 15 | `noticeboard` | easy | logic |
| GT1 16 | `staggered` | medium | logic |
| GT1 19 | `28 days` | easy | general_knowledge |
| AC3 1 | `acrylic` | easy | guess |
| AC3 6 | `right eye` | hard | general_knowledge |
| GT2 16 | `CV` | easy | logic |
| GT2 20 | `mentor` | hard | logic |

Onuüçünün de üç turda **aynı kelime** yazıldı — hiçbirinde üçte bir isabetin üst üste
gelmesi gibi bir şans açıklaması yok. Bu tipte tahmin uzayı sınırsız olduğu için
(şık yok, kelime yazılıyor) 3/3 tutturmak çoktan seçmelideki 3/3'ten çok daha güçlü
bir kanıt.

### İki sızıntı mekanizması

Onuüç sorunun tamamı iki kalıptan birine giriyor.

**1. Eşdizim kilidi (8/13) — boşluk kalıp bir İngilizce öbek dizisinin içinde duruyor,
cümle iskeleti kelimeyi zaten söylüyor.**

| Boşluklu çerçeve | Kilitlenen kelime |
|---|---|
| "hidden round a …" | corner |
| "put on …" (ofiste) | headphones |
| "a … effect" | novelty |
| "put up on the staff …" | noticeboard |
| "breaks are … so that no line is left uncovered" | staggered |
| "a clear … screen" | acrylic |
| "an up-to-date …" (başvuru) | CV |
| "a … from the intern's own department sees them once a week" | mentor |

Bunların hiçbirinde parçayı okumak gerekmiyor; boşluğun **iki yanındaki kelimeler**
cevabı tek bir seçeneğe indiriyor. Bu, düzeltilebilir bir kusur — aynı bilgi için
boşluk öbeğin öbür ucuna taşınabilir ("hidden round a corner" → `corner` yerine
`hidden`; "breaks are staggered" → `staggered` yerine bu düzenin **sebebi**).

**2. Dünya bilgisi (5/13) — boşluktaki değer parçaya değil dünyaya ait bir sabit.**

- `47` — Japonya'nın il sayısı.
- `500` — piroklastik akış sıcaklığı olarak her kaynakta geçen değer.
- `28 days` — Birleşik Krallık'ta tam zamanlı yıllık izin, resmî tatiller dâhil.
- `tyre` — fil araç kullanımı deneyinin yayımlanmış ayrıntısı.
- `right eye` — dişli balinalarda bilinen yanallık.

Bunlar da düzeltilebilir: aynı cümlede parçaya özgü olan başka bir değer var
(kaç ülke, kaç dakika, hangi ölçüm); boşluk oraya taşınırsa soru parçasız
çözülemez hale gelir.

### Neden table_completion tabanın üstünde — hücre cümleye dönünce

İşaretlenen dört tablo sorusunun ikisi (GT2 16 `CV`, GT2 20 `mentor`) tam cümle
hücrelerinde: "Form filled in online, an up-to-date (16) …, and 300 words on why you
want the placement." Bu bir tablo hücresinden çok bir not satırı. Cümle olunca
eşdizim kilidi devreye giriyor.

Aynı dosyada **sayısal** boşluklar hiç bilinemedi: AC3 4 (`kaç ziyaret`), AC3 5
(`ne kadar süre`), GT2 18 (`kabul için kaç gün`) — üçü de 0/3. Resmî tablo
tamamlamanın 0/5 olmasının sebebi tam da bu: resmî tabloda hücreler **veri**
(sayı, birim, ad, tarih), cümle değil. Bizim dört işaretimizin dördü de veri
olmayan hücrelerden geldi.

Yani sapma tipin kendisinden değil, tipin **yazılışından** geliyor — ve bu, bu
raporun çıkardığı en somut düzeltme.

### 2/3'te kalan sorular: yanlış değil, eşanlamlı

Sekiz soruda turların biri ya da ikisi tuttu. Hepsinde kaçırılan tur **anlamca doğru
ama kelimece yanlış** bir cevap verdi:

| Soru | Anahtar | Kaçıran turun cevabı |
|---|---|---|
| practice 6 | small sample | small group |
| AC1 2 | bamboo | wood |
| AC4 1 | reconfigure | rearrange |
| GT1 17 | card reader | time clock / clocking-in machine |
| GT1 18 | shift-swap form | shift change form |
| GT1 20 | staff portal | booking system |
| GT2 15 | sponsorship | a visa |
| GT2 17 | video interview | telephone interview |

Bu tablo tipin **savunma mekanizmasını** gösteriyor. Anlam yuvası parçasız
kestirilebiliyor, ama "parçadan kelime al" kuralı kestirmeyi cevaba çevirmiyor.
Yani `NO MORE THAN TWO WORDS **from the passage**` kısıtı boş bir biçimsellik değil,
ölçünün taşıyıcı kolonu. Bu bir kusur değil, korunacak özellik.

### `basis` dağılımı

Üç turun tamamı (135 cevap):

| Dayanak | Sayı | Oran |
|---|---|---|
| guess | 64 | %47 |
| logic | 44 | %33 |
| general_knowledge | 27 | %20 |
| option_wording | 0 | **%0** |

**`option_wording` = %0, yapısal olarak.** Bu tipte şık yok; yazılmış bir çeldirici
metni olmadığı için "doğru şık ölçülü, çeldirici mutlak" imzası imkânsız. 2. ve 3.
çalıştırmada (YNNG, çoktan seçmeli) paketi tek başına çökerten kusur buydu; tamamlama
tiplerinde hiç doğmuyor.

Yalnız işaretlenen 13 sorunun 39 cevabına bakılırsa dağılım tersine dönüyor:

| Dayanak | Sayı | Oran |
|---|---|---|
| logic | 18 | %46 |
| general_knowledge | 15 | %38 |
| guess | 6 | %15 |

Yani sızıntının ana kanalı `logic` — ve bu tipte `logic` demek "şıkları eledim"
değil, **"cümle çerçevesi kelimeyi zaten söylüyor"** demek. Eşdizim kilidi
bulgusunun sayısal karşılığı bu satır.

### Zorluk etiketiyle ilişki

| Etiket | Soru | 3/3 bilinen | Oran |
|---|---|---|---|
| easy | 15 | 7 | %47 |
| medium | 20 | 3 | %15 |
| hard | 10 | 3 | **%30** |

`easy` → `medium` düşüşü beklenen yönde. Ama `hard` etiketli 10 sorunun 3'ü
parçasız bilindi (AC4 5 `novelty`, AC3 6 `right eye`, GT2 20 `mentor`) — `medium`'un
iki katı. Bu üçü de eşdizim ya da dünya bilgisi kilidi taşıyor; yani "hard"
etiketi burada **kelimenin parçada bulunmasının zorluğunu** ölçmüş, kelimenin
bilinmesinin zorluğunu değil. Önceki çalıştırmalarda etiket temizdi; burada
üç satırlık bir tutarsızlık var.

### Düzeltme yönü (bu rapor uygulamıyor, işaret ediyor)

1. **Tablo hücresini cümle yazmayı bırak.** table_completion'da boşluk sayı/birim/ad/
   tarih hücresine gelsin. İşaretlenen 4 tablo sorusunun 4'ü de cümle hücresinden,
   sayısal hücrelerin 0'ı sızdırdı. Tek başına bu değişiklik tipi tabanın altına
   indirir.
2. **Boşluğu eşdizimin tahmin edilen ucuna koyma.** "hidden round a …", "put on …",
   "a … effect", "an up-to-date …" gibi çerçevelerde boşluk öbeğin öbür ucuna ya da
   cümlenin parçaya özgü kısmına taşınsın.
3. **Dünya sabitini boşluk yapma.** 47 (il sayısı), 500 (°C), 28 days (yasal izin) —
   üçü de parçadan bağımsız doğrular. Aynı cümledeki parçaya özgü değer boşluk
   yapılsın (practice 1'de "23 further countries" gibi).
4. **Üç `hard` etiketini gözden geçir.** AC4 5, AC3 6, GT2 20 parçasız çözüldüğü için
   `hard` sıfatını hak etmiyor.

### Korunacak olan

- **`from the passage` kısıtı.** 2/3 tablosu bunun tek başına sekiz soruyu kurtardığını
  gösteriyor.
- **Sayısal boşluklar.** AC3 4-5, GT2 18, practice 7-8 — hepsi 0/3. Parçaya özgü ölçüm
  ve tarih dışarıdan bilinemiyor.
- **practice dosyasının kurgusu (%13).** On beş sorunun on üçü dayandı.

### Ölçülmeyenler

- Dinleme tarafı bu adımın kapsamı dışında (prompt gereği). `note-completion` ve
  `table-completion` dinleme dosyaları script tarafından "okuma değil" diye atlandı.
- **Diyagram etiketleme: ölçülmedi.** Bu pakette bulunmuyor; görsel gerektiren tiplerde
  metin tabanlı bu ölçüm kördür ve 8. çalıştırmada da "ölçülmedi" olarak geçilecek.

### Araç notu

4. adım (işaretleme) bu çalıştırmada mevcut `tools/_b1_isaretle.py` yerine aynı mantığı
uygulayan tek seferlik bir betikle yapıldı: rapor JSON'undaki 3/3 bilinen kimlikler
orijinal dosyalara `blind_solvable` / `blind_basis` / `status` / `flag_reason` olarak
yazıldı, `blind_basis` üç turun en sık dayağı seçildi, hiçbir soru silinmedi. Yazım
sonrası tüm dosyalarda soru sayısı ve `answer` alanları git'teki önceki hâliyle
karşılaştırılarak doğrulandı (6/6 dosya değişmemiş). Özet istatistikler
`tools/_b1_metinsiz6_ozet.py` ile üretildi.

### Yapılan işaretleme

45 sorunun **13'üne** orijinal dosyasında `blind_solvable: true`, `blind_basis`,
`status: "flagged"` ve `flag_reason` yazıldı; **32'sine** `blind_solvable: false`.
**Hiçbir soru silinmedi**; soru sayısı 45'te sabit.

"""

path = "content/DOGRULAMA/METINSIZ-RAPOR.md"
s = io.open(path, encoding="utf-8").read()
if u"## 6 — note-completion" in s:
    print("bolum zaten var, dokunulmadi")
else:
    anchor = u"---\n\n\U0001f534 Son söz:"
    i = s.rindex(anchor)
    s = s[:i] + u"---\n\n" + BOLUM + s[i:]
    io.open(path, "w", encoding="utf-8").write(s)
    print("eklendi")
