# -*- coding: utf-8 -*-
"""OPUS5-E6 5. calistirma: NOTLAR.md ve UYARILAR.txt kayitlarini ekler.

NOTLAR.md 500 KB'i asiyor, editor araciyla degil script ile ekleniyor.
Ayni baslik zaten varsa hicbir sey yapmaz.
Kullanim: python tools/_e6_mf_not_ekle.py
"""
import io
import os
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTLAR = os.path.join(KOK, "NOTLAR.md")
UYARILAR = os.path.join(KOK, "UYARILAR.txt")

BASLIK = "# OPUS5-E6-yeniden-uretim (5. calistirma - ozellik esleystirme)"

NOT = u"""

""" + BASLIK + u"""

- **Kendi sayimim:** `content/DOGRULAMA/yeniden-uretim-listesi.json` icindeki
  `elenen` listesini yeniden saydim: 71 yuva. Bu calistirmanin kapsami "cumle
  sonu esleystirme + ozellik esleystirme" idi; listede **cumle sonu esleystirme
  (matching_sentence_endings) tipinde tek bir elenen yuva yok**, dolayisiyla
  kapsam yalniz **ozellik esleystirmenin 7 yuvasi**: `practice/
  matching-features.json` **#1, #5** (A10), `tests/AC1/matching-features.json`
  **#25** (A02), `tests/AC2/matching-features.json` **#24, #25, #26** (A05),
  `tests/AC4/matching-features.json` **#24** (A11). Yedisi de ayni dosyaya ayni
  numarayla dolduruldu; hicbir soru silinmedi (1310 soru, 12 tam test 40/40,
  sema hatasi 0). **Bu tipte elenen yuva kalmadi**; listede kalan yuva 47 -> 40.

### Hangi kanit nereye tasindi

| Yuva | Eski kanit (E5 yasakladi) | Yeni kanit | Yeni eksen |
|---|---|---|---|
| practice #1 | A10 F/2 (gurultu siniri) | A10 **D/3** | iki olcumde de karsilastirma duzeninin altina dusen tek tasarim |
| practice #5 | A10 H/1 (geri donmek istememe) | A10 **B/2** | engel turu: ses yalitimli kapi mi, sesi emen panel mi |
| AC1 #25 | A02 C/3 (isik gecirmez bolme) | A02 **D/3** | ustun hayvanin etkilesimlerin ~%76'sini kazanmasi |
| AC2 #24 | A05 G/2 (Bereketli Hilal, 12.000 yil) | A05 **F/2** | "ilk genetik isaret" iddiasinin hangi bugdaya ait oldugu |
| AC2 #25 | A05 G/2 (Karacadag / einkorn) | A05 **B/2** | tanelerin mikroskop altinda hangi forma benzedigi |
| AC2 #26 | A05 A/3 (tarimin Avrupa'ya yayilmasi) | A05 **G/3** | hangi formun beklenenden erken ortaya cikmis olabilecegi |
| AC4 #24 | A11 F/1 (POMS'un alti boyutu) | A11 **E/4** | olcegin madde sayisi (dort madde, en kisasi) |

Yedisinde de yeni kanit E5'in "kacinilacak" dedigi cumleye **hic degmiyor**;
altisinda kanit yasakli cumlenin **paragrafinin da disina** tasindi (AC1 #25'te
paragraf C'den D'ye, AC2 #25'te G'den B'ye). Hicbir yeni kanit dort pasajin
**son paragrafinda (H) degil** - "sinirlilik beyani / hakem degerlendirmesi"
kapanislari bos birakildi.

### Iki dosyada secenek listesi de degisti

**AC1** - E5'in kendi onerisi uygulandi. Sizinti ifadenin kipinde degil secenek
listesindeydi: A ve B gruplari `see-through screen` / `solid screen` diye, yani
tam da kanit cumlesinin (C/3) soyledigi ozellikle adlandirilmisti; ilk asamayla
ilgili her ifade bu iki etikete sozcuk duzeyinde bagliydi. Yeni liste gruplari
**asama/sira ile** adlandiriyor ("bulusmadan onceki iki kosulun birincisi /
ikincisi", "sonraki uc gun"). Bu, E5'in ongordugu gibi **AC1 #26'yi da
guclendirdi**: o yuvanin ifadesi, cevabi ve kaniti degismedi, ama artik cozucu
once C/2'yi okuyup ilk kosulun gorme izni veren kosul oldugunu bulmak zorunda;
eski `option_wording` sizintisi kapandi (`review_note`'a yazildi).

**AC2** - burada liste eksenden degisti, gerekcesi ayrica onemli. A05'in yer
listesi (Catalhoyuk / Karacadag / Bereketli Hilal / Avrupa / Birlesik Krallik)
**tur bakimindan heterojendi**: bes secenekten yalniz biri kazi yeri, yalniz
biri ulke, yalniz biri kita. Bu yuzden "buradan tane cikti" diyen her ifade
**tur elemesiyle**, "tarim buraya yayildi" ya da "basit bugday burada
ehlilestirildi" diyen her ifade **genel kulturle** cozuluyordu. Denenen ve
elenen iki alternatif:

1. *Yalniz A (Catalhoyuk) ve E (Birlesik Krallik) capalarini kullanmak.* Pasajda
   Karacadag yalniz G/2'de (E5 tarafindan yasakli cumle), Bereketli Hilal ve
   Avrupa ise yalniz yayilma anlatisinda geciyor. Dort yuvanin ucu A olurdu ve
   korlemesine "hep A" diyen bir aday 3/4 yapardi.
2. *C ve D'ye capa atmak.* Bu, E5'in tam da eledigi genel-kultur eksenine geri
   donmek olurdu (tarim Bereketli Hilal'de basladi, Avrupa'ya yayildi).

Secilen yol: liste **bugday turlerine** cevrildi (hexaploid / einkorn / emmer /
basit bugdaylar / spelt) - bes secenegin besi de ayni turden, boylece tur
elemesi kapandi. Bunun bedeli, listenin degismesiyle **kapsam disindaki 23
numarali yuvanin da zorunlu olarak yeniden yazilmasi** oldu: eski ifadesi bir
YER sorusuydu ve yeni listede karsiligi kalmiyordu. Soru silinmedi, numarasi ve
sayisi korundu; 3. calistirmanin o yuvaya yazdigi `revision` kaydi
`yeniden_uretim.onceki_revizyon` altina tasindi.

### Kendi kendini sinama (pasaj kapali, K3 - anlamca bilme de bilinen sayilir)

Sekiz ifadenin sekizi de pasaj kapaliyken cozulmeye calisildi:

- practice #1 (C): korlemesine bakinca sezgi "en kotu olan sade acik ofistir"
  diyor, yani **yanlis** secenege gidiyor; bilinmedi. Gecti.
- practice #5 (D): "office" sozcugu kapiyi, "zoned" sozcugu paneli cagristirdigi
  icin B ile D arasinda kararsiz kaliniyor; bilinmedi. Gecti.
- AC1 #25 (C): A ve B bulusma oncesi kosullar oldugu icin elenir, geriye C/D/E
  kalir; oran yalniz D/3'te. Bilinmedi. Gecti.
- AC2 #23 (D): **en zayif halka.** "Iki ornek birden" kaydi, bes secenek icinde
  tek kume secenegi olan D'yi ust duzeyde isaret ediyor; bilgi degil bicim
  ipucu. Alternatifleri (bkz. yukarida) daha kotu oldugu icin birakildi, E7'nin
  olcumune not dusuldu.
- AC2 #24 (E): "ilk genetik isaret" iddiasi A ile E arasinda bolunuyor; ayrim
  ancak F/2'nin "at all" kaydiyla goruluyor. Bilinmedi. Gecti.
- AC2 #25 (A): tanelerin mikroskop altinda neye benzedigi disaridan bilinemez;
  ustelik 23. soru bicim temelli siniflandirmayi basit bugdaylara baglayarak
  bilerek ters yone cekiyor. Gecti.
- AC2 #26 (A): ploidi bilen bir okur "gelismis form = hexaploid" baglantisini
  kurabilir; orta duzeyde risk, ama secenek metni ("hexaploid wheat") tek basina
  "gelismis" demedigi icin birakildi.
- AC4 #24 (D): madde sayilari (alti ve dort) disaridan bilinemez, araclarin
  adlari uzunluk hakkinda hicbir sey soylemez; C ile D arasinda kararsizlik
  kaliyor. Gecti.

### Kip imzasi sayimi (yasak 1)

Ozellik esleystirmede **celdirici metni yok** - secenekler kisa ad obekleri
(`einkorn`, `the team-office design`), dolayisiyla "dogru cevap olculu,
celdirici mutlak" karsitligi secenek duzeyinde olculemiyor. Sayim bu yuzden
**ifadeler** uzerinden yapildi ve ayrica secenek metinlerinin **hicbirinin** kip
tasimadigi dogrulandi (hepsi notr ad obegi). `tools/_e6_mf_eslestirme_kontrol.py`
ciktisi:

- mutlak ifade tasiyan: **5/8 (%62)** - `only`, `every`, `alone/both/any`,
  `the first`, `fewest`
- olculu ifade tasiyan: **5/8 (%62)** - `rather than`, `about`, `cautiously`,
  `some/as though`, `may/suggest`
- esik %33; iki yon de asiyor, uc ifade ikisini birden tasiyor (ornegin AC1 #25:
  `about three interactions in every four`).

### Konumsal duzen sayimi (yasak 2)

| Set | Harf dagilimi |
|---|---|
| practice P-MF-01 (A10, A-D) | B2 C1 D2 |
| practice P-MF-02 (G05, A-E) | A1 C1 D1 E2 |
| AC1 23-26 (A-E) | A1 C1 D1 E1 |
| AC2 23-26 (A-E) | A2 D1 E1 |
| AC4 23-26 (A-D) | B1 C2 D1 |

- **A sikki uc sette dogru cevap** (P-MF-02, AC1, AC2 - AC2'de iki kez); "yalniz
  orta sikklar dogru olur" deseni yok. Son sik da uc sette dogru (E, E, E).
- Ayni harf ikiden fazla tekrarlanmiyor (en yuksek 2).
- **Hicbir dogru cevap son paragrafa demirlenmedi**: yeni kanitlar D/3, B/2,
  D/3, E/1, F/2, B/2, G/3, E/4 - dort pasajin H paragraflari (sinirlilik ve
  genelleme uyarilari) bos kaldi.

### Ortak cumle kayitlari (sonraki calistirmalar icin)

- **AC1 D/3 artik iki gorevde:** ozellik esleystirme #25 (oran: %76) ve cumle
  tamamlama #20 (terim: `dominance hierarchy`). Hedefler farkli, ama ayni test
  icinde ayni cumle; A02'de C/3 disinda ilk asamaya ait baska capa kalmadigi
  icin baska secenek yoktu. E7 bunu olcerken bilsin.
- **A10 D/3** alistirma paketinde ozet tamamlama #1'de de kullaniliyor (blank:
  `popularity`); ikisi ayri alistirma seti.
- Bu adimda dolan cumleler: **A10 B/2 + D/3, A02 D/3, A05 B/2 + E/1 + F/2 + G/3,
  A11 E/4.**

### E7'ye / kalan calistirmalara notlar

- AC2 grubunda **B (einkorn) ve C (emmer) bilerek capasiz**: pasaj ikisini
  yalniz E/1'de birlikte aniyor, tek tek ayiran tek cumle G/2 ve o cumle E5
  tarafindan yasaklandi. Ikisi de saf celdirici.
- AC4 grubunda **A (Profile of Mood States) capasiz kaldi**: aracin ne olctugu
  adindan ve genel bilgiden cikiyor (E5'in eledigi tam da buydu), madde sayisi
  disinda ondan blind-proof soru cikmiyor - o capa da #26'da kullanilmis
  durumda.
- `tools/_e6_liste_isaretle.py` bu calistirmada **gruplu soru dosyalarini** da
  okuyacak bicimde genisletildi (onceki hali yalniz duz `items` bekliyordu,
  `practice/matching-features.json` gruplu).
- Araclar: `tools/_e6_mf_eslestirme.py` (uretim; kanit cumleleri pasajdan birebir
  okunuyor, paragraf/cumle numarasi dogrulaniyor), `tools/
  _e6_mf_eslestirme_kontrol.py` (kontrol), `tools/_e6_mf_capraz.py` (yeni kanit
  cumleleri baska sorularda kullaniliyor mu taramasi).
"""

UYARI = u"""
08.08.2026  OPUS5-E6 5/7 - Ozellik esleystirme
  - practice/matching-features.json #1 ve #5, AC1 #25, AC2 #24-25-26, AC4 #24
    ayni dosyada ayni numarayla yeniden dolduruldu; soru silinmedi.
  - [!] Elenen listesinde CUMLE SONU ESLEYSTIRME yuvasi yok; bu calistirmanin
    kapsami yalniz ozellik esleystirmeydi (7 yuva). Bu tipte elenen yuva
    kalmadi. Listede kalan toplam 47 -> 40 (hepsi tamamlama ailesi + TFNG +
    kisa cevap; 6. ve 7. calistirmanin isi).
  - [!] Iki dosyada SECENEK LISTESI degisti. AC1: gruplar artik bolme turuyle
    degil asama/sira ile adlandiriliyor (E5'in onerisi; AC1 #26'nin sizintisi
    da kapandi, ifade/cevap/kanit degismedi). AC2: yer listesi bugday
    turlerine cevrildi, cunku yer secenekleri tur bakimindan heterojendi ve
    her ifade tur elemesiyle cozuluyordu.
  - [!] AC2 #23 kapsam disi bir yuvaydi ama secenek ekseni degistigi icin
    zorunlu olarak yeniden yazildi (eski ifadesi bir YER sorusuydu). Numarasi
    ve soru sayisi korundu; 3. calistirmanin revision kaydi
    yeniden_uretim.onceki_revizyon altinda duruyor.
  - [!] AC2 #23 bu setin en zayif halkasi: "iki ornek birden" kaydi, bes
    secenek icinde tek kume secenegini isaret ediyor. E7 blind olcumunde
    ozellikle baksin.
  - [!] Kip imzasi: ifadelerin %62'si mutlak, %62'si olculu (esik %33).
    Ozellik esleystirmede celdirici METNI olmadigi icin sayim ifadeler
    uzerinden yapildi; secenek metinlerinin hicbiri kip tasimiyor.
  - [!] Konumsal duzen: A sikki uc sette dogru cevap; en yuksek harf tekrari 2;
    hicbir dogru cevap son paragrafa (H - sinirlilik beyanlari) demirlenmedi.
  - [!] Ortak cumle: AC1 D/3 artik hem ozellik esleystirme #25 (oran) hem cumle
    tamamlama #20 (terim) tarafindan kullaniliyor - ayni test icinde ayni
    cumle. A02'de ilk asamaya ait baska capa kalmamisti.
  - [!] Sonraki calistirmalara - bu adimda dolan cumleler: A10 B/2 + D/3,
    A02 D/3, A05 B/2 + E/1 + F/2 + G/3, A11 E/4.
  - dogrula.py: 12 tam test 40/40, sema hatasi 0, toplam soru 1310.
  - _e6_mf_eslestirme_kontrol.py: hata 0.
  - isaretli (flagged)     33
"""


def main():
    s = open(NOTLAR, encoding="utf-8").read()
    if BASLIK in s:
        print("NOTLAR.md: baslik zaten var, eklenmedi")
    else:
        with open(NOTLAR, "a", encoding="utf-8", newline="\n") as f:
            f.write(NOT)
        print("NOTLAR.md: %d karakter eklendi" % len(NOT))

    u = open(UYARILAR, encoding="utf-8").read()
    if "OPUS5-E6 5/7" in u:
        print("UYARILAR.txt: kayit zaten var, eklenmedi")
    else:
        with open(UYARILAR, "a", encoding="utf-8", newline="\n") as f:
            f.write(UYARI)
        print("UYARILAR.txt: %d karakter eklendi" % len(UYARI))


if __name__ == "__main__":
    main()
