# -*- coding: utf-8 -*-
"""E5/4 - ELDEN-GECIRME.md dosyasina 4. calistirma bolumunu ekler."""

import io
import os

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YOL = os.path.join(KOK, "content", "DOGRULAMA", "ELDEN-GECIRME.md")
BASLIK = "## 4. çalıştırma — tamamlama ailesinde eşdizim kilidi"

METIN = u"""
---

## 4. çalıştırma — tamamlama ailesinde eşdizim kilidi · 2026-08-08

### Kapsam ve kendi sayımım

Talimatın 1. kuralı gereği yeniden saydım. Bu çalıştırma tipe değil **mekanizmaya**
bakıyor: `content/reading` altında tamamlama ailesinde (`note` / `sentence` /
`summary` / `table` / `flow_chart_completion`) `flag_mechanism: "esdizim_kilidi"`
taşıyan **61** işaretli soru var (62'nci eşdizim kilidi sorusu tamamlama ailesinde
değil, `practice/short-answer` #6).

Bu 61 soru iki ayrı kaynaktan geliyor ve bunu tek tek doğruladım
(`python tools/_e5_comp_kapsam.py`): E10'un eklediği sorularda
`blind_solvable_kelime_duzeyi` alanı var, E1'inkilerde yok.

| Kaynak | Soru | Bu çalıştırmanın kapsamında mı |
|---|---|---|
| E1 (kelime düzeyi işaret) | 21 | evet |
| E10 — not/tablo/akış tamamlama | 12 | evet |
| E10 — cümle tamamlama | 14 | hayır → 7. çalıştırma |
| E10 — özet ailesi | 14 | hayır → 8. çalıştırma |
| **bu çalıştırma** | **33** | |

Kapsam sınırını böyle çizdim, çünkü çalıştırma listesinin 7. ve 8. maddeleri
E10'un cümle tamamlama ve özet ailesi işaretlerini açıkça kendilerine ayırıyor;
geriye kalan E10 grubunu (not/tablo/akış, 12 soru) hiçbir madde talep etmiyor ve
mekanizması bu maddenin başlığıyla birebir aynı. E1'in dağılım tablosundaki
eşdizim kilidi sayısı (21) kendi sayımımla birebir tuttu.

### Sonuç dağılımı

| Sonuç | Soru | Nerede |
|---|---|---|
| **Düzeltildi** | 15 | E1 kökenli 14 · E10 kökenli 1 |
| **Elendi** | 7 | E1 kökenli 7 |
| **Dokunulmadı** | 11 | E10 kökenli 11 |
| **toplam** | **33** | |

🔴 **Elenen küme ile `genel_kultur` kümesi bu çalıştırmada hiç kesişmiyor.**
Elenen yedi sorunun yedisi de `esdizim_kilidi` etiketli; hiçbiri genel kültür
sorusu değil. Eleme gerekçesi ilk üç çalıştırmadakinden farklı ve aşağıda ayrıca
anlatılıyor.

### Bu mekanizma öncekilerden yapıca farklı

1., 2. ve 3. çalıştırmada sızıntı **çerçevedeydi**: ifadenin kipi, seçeneklerin
biçimi, son listesinin konusu. Çerçeve düzeltilebilir bir şey, çünkü `answer` ve
`evidence` ona dokunmadan yeniden yazılabiliyor. Eşdizim kilidinde durum
tersine dönüyor — sızıntı çoğu zaman **cevabın kendisinde**. 33 soruyu okuyunca
üç alt biçim çıktı:

| Alt biçim | Ne oluyor | Düzeltilebilir mi |
|---|---|---|
| **a) Çerçeve kilidi** | Boşluğun çevresinde, tek bir tamamlaması olan bir kalıp var (`keep a ___`, `put up on the staff ___`, `stay ___`, `the mere ___ of time`). Kalıbı kaldırınca boşluğa birden çok aday uyar hale geliyor. | **Evet** — 14 soru |
| **b) Hesaplanabilir boşluk** | Sızıntı eşdizim değil aritmetik: gövde hem çarpanı hem çarpımı veriyor. | **Evet** — 1 soru |
| **c) Hedef kilidi** | Boşluğun *hedeflediği kavramın* İngilizcede tek karşılığı var (`popularity`, `humidity`, `CV`, `mentor`, `reflects light`). Çerçeve ne yapılırsa yapılsın aynı sözcüğü veriyor; açmak için boşluğu başka bir ayrıntıya taşımak, yani `answer`'ı değiştirmek gerekiyor. | **Hayır** — 7 soru elendi, 11 soru dokunulmadan bırakıldı |

Yani bu mekanizmada "düzeltmek" ile "yeniden üretmek" arasındaki sınır, öteki
mekanizmalardakinden çok daha erken geliyor. Bu çalıştırmanın asıl bulgusu bu.

### a) Çerçeve kilidi — 14 düzeltme

Uygulanan tek kural:

> Boşluğun çevresindeki kilitleyici sözcük (fiil, edat ya da sıfat) kaldırılır ve
> geriye, **pasajın kendi dünyasından en az iki adayın** uyduğu bir yuva bırakılır.
> Cevap artık kalıptan değil yalnız kanıt cümlesinden bulunuyor.

Serbest cevaplı (parçadan kelime) yedi soru:

| Soru | Kaldırılan kilit | Yeni çerçevede uyan adaylar |
|---|---|---|
| practice-sc-8 | `a ___ of what is coming` | preview · warning · benchmark · window |
| practice-sum-10 | `keeping a week-long ___` | diary · log · record · journal |
| AC1-nc-5 | `hidden round a ___` | corner · door · wall · screen |
| AC3-sc-20 | `appear ___ , whereas … looks dark` | bright · white · clearly · strongly |
| GT1-nc-15 | `put up on the staff ___` | noticeboard · portal · intranet |
| GT1-nc-16 | boşluğun önündeki "aynı anda durmuyorlar" tanımı | staggered · scheduled · rotated · coordinated |
| GT1-sum-40 | `collecting and disposing … rather than its ___` | prevention · reduction · progress · change |

GT1-nc-15 örnek olarak anlamlı: aynı belge kümesi hem bir personel ilan panosunu
hem de çevrimiçi bir personel portalını anlatıyor. Eski çerçeve (`put up on`)
portalı dilbilgisiyle eliyordu; yeni çerçeve (`appears on the staff ___`) ikisini
de açık bırakıyor, dolayısıyla 15 ile 20 artık birbirini kısıtlıyor ve ikisi de
metne bakmayı gerektiriyor.

Kelime bankalı özette (7 soru) aynı kural iki yönde birden çalıştı — çünkü orada
kilit yalnız cümlede değil, **bankada uygun rakip bulunmamasında**:

| Soru | Kaldırılan kilit | Artık uyan rakip seçenek(ler) |
|---|---|---|
| AC4-37 | `stayed ___` ("stay awake") | H, metni `the length of the nap` → **`in the laboratory`** yapıldı |
| AC4-39 | `produced almost ___` ("almost" yakınlık istiyor) | G `much weaker results` (artık dilbilgisi olarak uyuyor) |
| AC4-40 | `simply getting ___` ("get a chance to…") | E, metni `deeper sleep` → **`an unbroken night`** yapıldı |
| GT2-37 | `carry only ___` ("only" küçüklük istiyor) | F `roughly half` · H `the main driver` |
| GT2-38 | `the outcome stayed ___ throughout` ("stay stable") | C `contradictory` · D `easily explained` |
| GT2-39 | `___ rather than firm answers` + listedeki "possible" | E `proof of a cause` |
| GT2-40 | boşluğu çevreleyen "karıştırıcı etkenler" ve "rastgele atamalı deneme gerekir" kayıtları | D `easily explained` · E `proof of a cause` |

🔴 Kelime bankasında **yalnız çeldirici metinleri** değişti (AC4'te E ve H). Harf
kümesi, harflerin sırası ve **doğru seçeneklerin metinleri** iki bankada da
korundu; doğrulama betiği bunu ayrıca sınıyor. AC4'te `deeper sleep` çeldirici
sayılmıyordu, çünkü "uykunun iç yapısı"nın kendisiydi ve 40. sorunun cümlesiyle
çelişiyordu; `an unbroken night` aynı yere gerçek bir rakip olarak oturuyor.

GT2-40'ta düzeltme cümlenin kendisiyle sınırlı kalamadı: cevabı asıl sızdıran
şey, boşluğun **önünde** duran "gönüllü olmayı seçenler zaten farklı olabilir"
cümlesi ile **arkasında** duran "rastgele atamalı bir deneme gerekirdi" kaydıydı.
İkisi birlikte "yalnızca bir ilişki" cevabını çerçeveden okutuyordu; ikisi de
özetten çıkarıldı. Kanıt cümlesi (I/1) ve cevap harfi aynı kaldı.

### b) Hesaplanabilir boşluk — 1 düzeltme

**AC2-fc-1** (`forty minutes`) bu çalıştırmanın en net bulgusu ve E10'un
işaretlediği tek not/tablo/akış sorusunun düzeltilebileni. E10 raporu bu soruyu
"ölçüm anahtardan bile katıydı" diye anmıştı, çünkü modelin verdiği `40 minutes`
zaten `accepted_variants` içinde. Asıl mesele başkaydı: akış şemasının ilk kutusu
hem poz **sayısını** ("ten") hem toplam **süreyi** ("roughly six hours")
veriyordu. 6 saat ÷ 10 ≈ 36 dakika; en yakın yuvarlak değer kırk dakika. Yani
cevap pasaja hiç bakılmadan **hesaplanabiliyordu** — sızıntı eşdizim değil
aritmetikti. İki sayı da kutudan çıkarıldı ve şemanın başka bir kutusunda
tekrarlanmadı.

### Elenen 7 soru — hedef kilidi

Bu yedisinde sorun soru metninde değil, **boşluğun neyi hedeflediğinde**. Boşluk,
İngilizcede tek karşılığı olan bir kavramı istiyor; çerçeve nasıl yazılırsa
yazılsın o sözcük çıkıyor. Açmanın tek yolu boşluğu cümlenin başka bir ayrıntısına
taşımak, o da `answer`'ı değiştirmek demek — talimat bunu "yarım düzeltme"
saydığı için düzeltme değil eleme.

| Soru | Cevap | Neden hedef kilitli | E6'ya önerilen yeni çapa |
|---|---|---|---|
| practice-sum-1 | `popularity` | Özet "moda olmasına rağmen kötü sonuç verdi" karşıtlığını taşımak zorunda; bu karşıtlıkta boşluğun tek sözcüğü budur | aynı cümledeki %14'lük düşüş |
| AC2-fc-3 | `reflects` | Parlaklıktan çap tahmini varsayımı İngilizcede yalnız `reflect` fiiliyle kurulur | çap tahmininin sayısı ya da "ölçülemeyecek kadar sönük" gerekçesi |
| AC4-nc-4 | `headphones` | Gürültü çalışmasında gözlemcinin saydığı gündelik alışkanlık = kulaklık; kanıttaki öteki iki örnek de aynı ölçüde tahmin edilebilir | kod commit sayımı |
| AC4-sc-20 | `humidity` | Dört hava değerinden yalnız biri yüzdeyle verilir; birim tek başına cevabı söyler | rüzgâr hızı (1.13 m/s) ya da kar derinliği |
| AC4-sc-21 | `passage` | `the passage of time` tam kalıplaşmış; `of time` kaldırılınca cümle anlamsızlaşıyor | anketlerin on beş dakikanın hemen öncesi/sonrasında uygulanması |
| GT2-tc-16 | `CV` | "Güncel bir ___ yükleyin" satırının başvuru dünyasında tek tamamlaması | 300 kelimelik gerekçe metni ya da 28 Şubat son tarihi |
| GT2-tc-20 | `mentor` | Kanıt cümlesinin bütün içeriği ("kendi biriminden biri, on hafta, haftada bir görüşme") doğrudan bu rolü tanımlıyor | aylık ücret ya da on haftalık süre |

Yedisi de `status: "rejected"` + `reject_reason` aldı, dosyalarında
**numaralarıyla duruyor** ve `content/DOGRULAMA/yeniden-uretim-listesi.json`
dosyasına eklendi (liste 29 → **36** kayıt). Her kayıt kanıt cümlesini ve soru
metnini `kacinilacak` altında, önerilen yeni çapayı da `neden_elendi` içinde
taşıyor.

### Dokunulmayan 11 soru — E10'un anlam düzeyi işaretleri

E10'un not/tablo/akış grubundan gelen 12 sorunun 11'i (12'ncisi yukarıdaki
AC2-fc-1) aynı biçimde: model parçasız üç turda da doğru **kavramı** verdi,
tutmayan şey sözcüğün kendisiydi.

| Soru | Cevap | Modelin verdiği |
|---|---|---|
| practice-nc-3 | individual output | individual performance ×3 |
| practice-nc-4 | Eurasian magpie | magpie ×3 |
| practice-nc-6 | small sample | small group / small sample |
| practice-nc-11 | wooden bed | bed ×3 |
| practice-nc-12 | skeletal remains | bones ×3 |
| AC4-nc-1 | reconfigure | rearrange / reconfigure |
| GT1-nc-17 | card reader | time clock / card reader / clocking-in machine |
| GT1-nc-18 | shift-swap form | shift swap form / shift change form |
| GT1-nc-20 | staff portal | booking system / staff portal |
| AC3-tc-3 | cosmetic | dye ×3 |
| GT2-tc-15 | sponsorship | sponsorship / a visa |

Bunlar hedef kilidinin daha yumuşak bir hâli: kavram çerçeveden çıkıyor ama
sözcük çıkmıyor, dolayısıyla **kelime düzeyinde soru hâlâ çalışıyor** — bir aday
`bones` yazsa yanlış sayılır. Yedi sorunun elenmesi zaten dört tam testte yedi
yuva açtı; bu on biri de elemek aynı dosyaları yeniden üretime bağımlı hale
getirirdi. Bu yüzden bilinçli bir editoryal karar olarak `status` değiştirilmedi
(`flagged` kaldı), her birine `review_note` alanında gerekçe ve E6 için somut bir
yeni çapa önerisi yazıldı. Karar tartışmaya açık; E6 isterse bu on biri de
yeniden üretim kapsamına alabilir, gerekli bilgi dosyaların içinde duruyor.

### 🔴 E6 ve E7'ye devir notları

1. **Eşdizim kilidi, elden geçirmeyle kapanan bir kusur değil.** Bu çalıştırmanın
   kapsamındaki 33 sorunun yalnız 15'i mekanik olarak düzeltilebildi; 18'inde
   sızıntı boşluğun hedefinde. Tamamlama ailesinde yeni soru yazılırken kural şu
   olmalı: **boşluk, İngilizcede tek karşılığı olan bir kavramı hedeflemesin.**
   Sayı, tarih, özel ad ve kapalı liste isteyen boşluklar dayanıklı (E10'un toplu
   raporu da bunu söylüyor); serbest kavram isteyen boşluklar değil.
2. **Elenen yedi yuvanın her birine somut bir yeni çapa önerisi yazıldı** ve
   `neden_elendi` alanında duruyor. AC4-sc-20 ile AC4-sc-21 aynı pasajdan (A11),
   GT2-tc-16 ile GT2-tc-20 aynı metinden (G04) geliyor; ikişerini **ayrı
   paragraflara** çapalamak gerekiyor, kanıt cümleleri listede `kacinilacak`
   altında.
3. **AC4 kelime bankası artık iki yeni çeldirici taşıyor** (E `an unbroken night`,
   H `in the laboratory`). E6 bu bankaya dokunursa bu iki metnin 37 ve 40'ın
   rakipleri olduğunu bilmeli; kaldırılırsa eşdizim kilidi geri gelir.
4. **5. çalıştırmanın kapsamı bu çalıştırmadan etkilenmedi.** Kelime bankalı
   özetteki iki `tanim_sizintisi` sorusu (AC3-38, AC4-36) ile bunların bankadaki
   karşıt seçenekleri (AC4'te C `between-subjects`, I `unrelated in meaning`)
   bilinçli olarak hiç ellenmedi.
5. **Düzeltilen 15 soru ölçülmemiş sorudur.** `answer`, `accepted_variants` ve
   `evidence` korundu ama soru metinleri ve özet/not/akış gövdeleri baştan
   yazıldı; hepsinde `blind_solvable: null` duruyor. E7 bunları yeniden ölçmeli.
   Özellikle GT2 özetinin dördü birden değiştiği için o dosya, kelime bankalı
   özette çeldirici tazelemesinin tek başına yeterli olup olmadığını gösteren en
   temiz örnek olacak.
6. **AC4-sum-39'da küçük bir kesinlik kaybı var.** Eski cümle "produced almost
   equal benefits" diyordu; "almost" kaldırılınca F seçeneği (`equal benefits`)
   pasajın 0.71/0.68 rakamlarına göre bir tık fazla kesin duruyor. Kanıt cümlesi
   "very similar benefits" dediği için seçim hâlâ tek doğru, ama E7 ölçümünde bu
   soruya ayrıca bakılmalı.

### Doğrulama

```
python tools/_e5_comp_kapsam.py            # kapsam: 61 esdizim kilidi, 33'u bu calistirmada
python tools/_e5_comp_elden_gecir.py       # duzeltildi 15 - elendi 7 - dokunulmadi 11
python tools/_e5_comp_devir.py             # eklenen kayit 7 - toplam 36
python tools/_e5_comp_dogrula_degisim.py   # KORUNAN ALAN HATASI: 0
python tools/dogrula.py
```

- `answer`, `accepted_variants`, `evidence`, `evidence_locator` ve `word_limit`
  on dört dosyanın hepsinde **hiç değişmedi** (HEAD ile alan alan karşılaştırıldı,
  102 soruda 0 fark). Kelime bankalarında harf kümesi ve sırası korundu, doğru
  seçeneklerin metinleri korundu; değişen tek şey AC4'teki iki çeldirici metni.
- Her boşluk numarasının özet/not/akış gövdesinde ya da tablo hücresinde hâlâ
  durduğu ayrıca sınandı.
- Soru sayısı ve numaralar değişmedi: 14 dosyada 102 soru girdi, 102 çıktı. On
  iki tam testin hepsi 40/40 kaldı.
- `isaretli (flagged)` 142 → **120** (15 verified + 7 rejected; dokunulmayan 11
  soru flagged kaldı). `esdizim_kilidi` işaretli soru 62 → **40**; kalan 40'ın
  11'i bu çalıştırmanın bilinçli olarak bıraktıkları, 29'u 7. ve 8.
  çalıştırmaların kapsamında.
- Şema hatası **0**; `explanation` alanlarının hepsi İngilizce yazıldı,
  `revision`, `reject_reason` ve `review_note` gibi iç denetim notları Türkçe
  kaldı.
"""


def main():
    s = io.open(YOL, encoding="utf-8").read()
    if BASLIK in s:
        print("bolum zaten var, dokunulmadi")
        return
    if not s.endswith("\n"):
        s += "\n"
    io.open(YOL, "w", encoding="utf-8").write(s + METIN)
    print("4. calistirma bolumu eklendi")


if __name__ == "__main__":
    main()
