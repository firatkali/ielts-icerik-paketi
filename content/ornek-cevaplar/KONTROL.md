# Ornek cevap kutuphanesi - kendi kendini denetim

Her grup uretildikten sonra, cevaplar band etiketleri gorulmeden
`degerlendirme/` altindaki duzeltilmis talimatla yeniden puanlaniyor. Verilen puan
hedeflenen bandin 0,5'i disina cikarsa cevap yeniden yaziliyor.

Sutunlar: gorev · hedef band · kendi puanim (4 olcut ve genel) · yeniden yazildi mi.

---

## 1. grup - Academic Task 1 (AT01-AT05)

Talimat: `degerlendirme/yazma-task1-academic.md`. Genel band = dort olcutun ortalamasi,
en yakin yarim banda yuvarlanmis (.25 ve .75 yukari).

| Gorev | Hedef | TA | CC | LR | GRA | Genel | Sapma | Yeniden yazildi mi |
|---|---|---|---|---|---|---|---|---|
| AT01 | 5,0 | 5 | 5,5 | 5 | 4 | **5,0** | 0 | hayir |
| AT01 | 6,5 | 7 | 6,5 | 6 | 7 | **6,5** | 0 | hayir |
| AT01 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |
| AT02 | 5,0 | 5 | 5,5 | 5 | 4 | **5,0** | 0 | hayir |
| AT02 | 6,5 | 7 | 6,5 | 6 | 6,5 | **6,5** | 0 | **evet** (bkz. asagi) |
| AT02 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |
| AT03 | 5,0 | 5 | 5,5 | 5 | 4 | **5,0** | 0 | hayir |
| AT03 | 6,5 | 6,5 | 6,5 | 6 | 7 | **6,5** | 0 | hayir |
| AT03 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |
| AT04 | 5,0 | 5 | 5 | 5 | 4 | **5,0** | 0 | hayir |
| AT04 | 6,5 | 7 | 6,5 | 6 | 7 | **6,5** | 0 | hayir |
| AT04 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |
| AT05 | 5,0 | 5 | 5,5 | 5 | 4 | **5,0** | 0 | hayir |
| AT05 | 6,5 | 7 | 6,5 | 6 | 7 | **6,5** | 0 | hayir |
| AT05 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |

### Yeniden yazilan: AT02 / hedef 6,5

Ilk yazimda **7,0** cikti (TA 7 · CC 7 · LR 6 · GRA 7 = 6,75 → 7,0). Hedefin tam 0,5
uzagi oldugu icin esigin icindeydi, ama bes gorevin 6,5'lari arasinda tek basina
yukarida duruyordu; kutuphane kendi icinde tutarli olsun diye yeniden yazildi.

Yapilan degisiklikler - hepsi 6,5 duzeyinde tipik kusurlar:

- `they were followed by the 30-44 group` → `after them there was the 30-44 group`
- `The situation changed in 2022.` → `In 2022 the situation was not the same.`
  (paragraf acilislari In 2010 / In 2022 kalibina donuyor, gecis mekaniklesiyor)
- `the two oldest groups grew` → `the two oldest groups made a growth` (esdiziim hatasi)
- `In total, visits fell` → `In total, the visits fell` (gereksiz tanimlik)

Yeni puan: TA 7 · CC 6,5 · LR 6 · GRA 6,5 = 6,5.

### Denetimde dikkat cekenler

- **Band 5 orneklerinde GRA 4 cikiyor.** Hatali cumle orani bes cevapta da %80'in
  uzerinde; talimatin tablosu bu orani 4 satirina koyuyor. Anlam hicbir yerde
  kaybolmadigi icin cevaplar 4'e degil 5'e oturuyor - genel band diger uc olcut
  tarafindan 5,0'da tutuluyor. Bu istenen sonuc: band 5 ornegi gercekten hata
  iceriyor, sadece kisa yazilmis duzgun bir metin degil.
- **Band 5 kelime sayilari 164-171.** Sinirin ustunde ama ucunda; dusuklugun sebebi
  eksik kelime degil, olcutler. `max 6` (150 alti) capasi hicbir cevapta ateslenmedi.
- **Band 5'te genel bakis capasi (max 5) bilerek atesleniyor** - bes cevapta da
  butunu ozetleyen cumle yok. Band 6,5 ve 8 cevaplarinda genel bakis var.
- **Band 8'ler kusursuz degil**: her birinde talimatin 8 satirinin izin verdigi
  turden ufak esdiziim ve vurgu kusurlari birakildi; hicbiri 9 hedeflemiyor.

---

## Alti calistirmanin gorev dagilimi (30 gorev)

Prompt "Academic Task 1 · Academic Task 2 · General Task 1 (mektup) · General Task 2
dengeli dagilsin" diyor. 30 gorev / 4 tur, calistirma basina 5 gorev:

| Calistirma | Grup | Gorevler |
|---|---|---|
| 1 | Academic Task 1 | AT01-AT05 |
| 2 | Academic Task 2 | T2-01, T2-06, T2-10, T2-15, T2-17 |
| 3 | General Task 1 (mektup) | GT01-GT05 |
| 4 | General Task 2 | T2-24, T2-09, T2-11, T2-53, T2-57 |
| 5 | Academic Task 1 (3) + Academic Task 2 (2) | AT06-AT08 + T2-44, T2-39 |
| 6 | General Task 1 (3) + General Task 2 (2) | GT06-GT08 + T2 havuzu |

Toplam: AC-T1 8 · AC-T2 7 · GT-T1 8 · GT-T2 7 = 30.

Task 2 gorevleri `module: "both"` oldugu icin Academic ve General ayrimi gorevin
kendisinde degil, secimde: 2. gruba bes soru kalibinin (opinion · discuss_both_views ·
problem_solution · advantages_disadvantages · double_question) her birinden bir gorev
alindi, konu alani tekrar etmeyecek sekilde. 4. ve 6. gruplar T2 havuzunun kalanindan
secilecek; burada kullanilan bes gorev tekrar edilmeyecek.

---

## 2. grup - Academic Task 2 (T2-01, T2-06, T2-10, T2-15, T2-17)

Talimat: `degerlendirme/yazma-task2.md`. Genel band = dort olcutun ortalamasi, en yakin
yarim banda yuvarlanmis (.25 ve .75 yukari). Gorevler ve kaliplari:

| Kod | Kalip | Konu |
|---|---|---|
| T2-01 | opinion | egitim - pratik ders zorunlu olmali mi |
| T2-06 | discuss_both_views | ulasim - toplu tasima mi yol mu |
| T2-10 | problem_solution | sehir hayati - merkezde konut pahaliligi |
| T2-15 | advantages_disadvantages | teknoloji - yalnizca cevrim ici hizmetler |
| T2-17 | double_question | kultur - gelenekleri yalnizca yaslilar surduruyor |

| Gorev | Hedef | TA | CC | LR | GRA | Genel | Sapma | Yeniden yazildi mi |
|---|---|---|---|---|---|---|---|---|
| T2-01 | 5,0 | 5 | 5,5 | 5 | 5 | **5,0** | 0 | hayir |
| T2-01 | 6,5 | 7 | 6 | 6,5 | 6,5 | **6,5** | 0 | **evet** (bkz. asagi) |
| T2-01 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |
| T2-06 | 5,0 | 5,5 | 5,5 | 5 | 4 | **5,0** | 0 | hayir |
| T2-06 | 6,5 | 7 | 6,5 | 6 | 6,5 | **6,5** | 0 | **evet** (bkz. asagi) |
| T2-06 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |
| T2-10 | 5,0 | 5 | 5,5 | 5 | 4 | **5,0** | 0 | hayir |
| T2-10 | 6,5 | 7 | 6 | 6,5 | 6,5 | **6,5** | 0 | **evet** (bkz. asagi) |
| T2-10 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |
| T2-15 | 5,0 | 5 | 5,5 | 5 | 4 | **5,0** | 0 | hayir |
| T2-15 | 6,5 | 7 | 6 | 7 | 6 | **6,5** | 0 | **evet** (bkz. asagi) |
| T2-15 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |
| T2-17 | 5,0 | 5 | 5 | 5 | 4 | **5,0** | 0 | hayir |
| T2-17 | 6,5 | 7 | 6 | 6,5 | 6,5 | **6,5** | 0 | **evet** (bkz. asagi) |
| T2-17 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |

### Yeniden yazilan: bes gorevin de 6,5 hedefli cevabi

Ilk yazimda bes cevap da **7,0** cikti. Sebep tek ve ayni: dilbilgisi fazla
temizdi. Talimatin GRA tablosu bandi hatali cumle oranindan okuyor; ilk metinlerde bu
oran %20'nin altindaydi, yani tablonun 8-9 satiri. TA 7 · CC 6 · LR 6,5 · GRA 8 = 6,875
→ 7,0. Sapma tam 0,5 oldugu icin esigin icindeydi ama bes cevapta birden ayni yonde
oldugu icin sistematik bir kusurdu: "band 6,5 cevabi" diye band 7 dilbilgisi
gosteriyorduk.

Duzeltme: her metne, hedef bandda gercekten gorulen turden 4-5 hata eklendi (uyum,
tanimlik, edat, cogul), hatali cumle orani %30 civarina cikarildi - talimatin 7 satiri
(%20-40) ile 6,5 arasi. Ornekler:

- T2-01: `or fix a dripping tap` → `or to fix a dripping tap`; `depend on their family`
  → `depend to their family`; `these abilities` → `this abilities`
- T2-06: `Both positions have` → `Both position have`; `need to reach their workplace`
  → `need to reach to their workplace`; `a good network reduces` → `a good network reduce`
- T2-10: `there are measures` → `there is some measure`; `this produces tiredness`
  → `this produce tiredness`; `need staff` → `need staffs`
- T2-15: `who find it very difficult` → `who find very difficult`; `who never used a
  computer` → `who has never used a computer`; `the difficulties fall` → `falls`
- T2-17: `A generation which grew up with screens has` → `... have`; `some of them
  deserve` → `deserves`

Metnin fikir yapisina, tutumuna ve sozcuk secimine dokunulmadi - yalnizca dilbilgisi
duzeyi hedefe indirildi. Yeni puanlar tablodaki gibi: bes cevap da 6,5.

### Denetimde dikkat cekenler

- **Kelime sayisi capasi hicbir cevapta ateslenmedi.** Band 5 cevaplari 261-278 kelime,
  yani 250'nin ustunde ama ucunda. `max 6` (250 alti) ve `max 5` (188 alti) capalari
  hicbir yerde devreye girmedi; dusuklugun sebebi olcutler, eksik kelime degil.
- **Band 5'lerde GRA 4-5.** Hatali cumle orani dort cevapta %80 civari (talimatin 4
  satiri), T2-01'de %75 (5 satiri). Anlam hicbir yerde kaybolmadigi icin genel band
  diger uc olcut tarafindan 5,0'da tutuluyor - istenen sonuc bu: band 5 ornegi gercekten
  hata iceriyor, sadece kisa yazilmis duzgun bir metin degil.
- **Band 5'lerde gorevin bir yarisi bilerek eksik birakildi**, ama her seferinde farkli
  bicimde: T2-06'da ikinci gorus iki cumleye sikismis, T2-10'da onlemler bolumu iki
  cumle, T2-15'te tarti hukmu hic verilmemis ("both of them are important"), T2-17'de
  degerlendirme sorusu hic yanitlanmamis, T2-01'de zorunluluk sorusu yerine fayda sorusu
  cevaplanmis. Bunlarin hepsi gorevlerin `common_mistakes` alanindaki hatalar.
- **Band 8'ler kusursuz degil**: her birinde bir gerekce otekilerden ince kaliyor
  (T2-01'de mufredat itirazi, T2-15'te kayit tutma avantaji) ve `what_would_lift_it`
  alani tam bunu isaret ediyor. Hicbiri band 9 hedeflemiyor.
- **Uc seviyede de tutum ayni tarafta** tutuldu (ayni gorev, ayni pozisyon, farkli
  yurutme). Boylece kullanici uc metni yan yana koydugunda farkin fikirden degil
  dilden ve gelistirmeden geldigini goruyor.

---

## 3. grup - General Task 1 / mektup (GT01-GT05)

Talimat: `degerlendirme/yazma-task1-general.md`. Genel band = dort olcutun ortalamasi, en
yakin yarim banda yuvarlanmis (.25 ve .75 yukari). Gorevler:

| Kod | Ton | Konu |
|---|---|---|
| GT01 | resmi | otobus seferlerindeki aksamalar - sirkete sikayet |
| GT02 | resmi | mahalle bahcesine gonullu basvurusu |
| GT03 | resmi | internet faturasinda istenmeyen kalem |
| GT04 | resmi | alti haftadir teslim edilmeyen siparis |
| GT05 | yari resmi | kiralik evde bozulan kalorifer - ev sahibine |

Kelime sayisi selamlama ve imza dahil sayildi; mektup govdesi (bunlar cikarilinca) en
kisa cevapta bile 171 kelime, yani 150 sinirinin ustunde. `max 6` (150 alti) capasi
hicbir cevapta ateslenmedi.

| Gorev | Hedef | TA | CC | LR | GRA | Genel | Sapma | Yeniden yazildi mi |
|---|---|---|---|---|---|---|---|---|
| GT01 | 5,0 | 5 | 5,5 | 5 | 4 | **5,0** | 0 | hayir |
| GT01 | 6,5 | 7 | 6 | 6,5 | 6 | **6,5** | 0 | hayir |
| GT01 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |
| GT02 | 5,0 | 5 | 5,5 | 5 | 4 | **5,0** | 0 | hayir |
| GT02 | 6,5 | 7 | 6 | 6,5 | 6 | **6,5** | 0 | hayir |
| GT02 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |
| GT03 | 5,0 | 5 | 5 | 5 | 5 | **5,0** | 0 | hayir |
| GT03 | 6,5 | 7 | 6 | 6,5 | 6 | **6,5** | 0 | hayir |
| GT03 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |
| GT04 | 5,0 | 5 | 5,5 | 5 | 4 | **5,0** | 0 | hayir |
| GT04 | 6,5 | 7 | 6,5 | 6,5 | 6 | **6,5** | 0 | hayir |
| GT04 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |
| GT05 | 5,0 | 5 | 5,5 | 5 | 4 | **5,0** | 0 | hayir |
| GT05 | 6,5 | 7 | 6,5 | 6,5 | 6 | **6,5** | 0 | hayir |
| GT05 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |

### Bu grupta neden yeniden yazma yok

Ikinci grubun dersi (bes 6,5 cevabinin da dilbilgisi fazla temiz cikmasi) bu grupta
yazarken uygulandi: 6,5 mektuplarina bastan, hedef bandda gercekten gorulen turden
5-6 hata kondu ve hatali cumle orani %45-60 araliginda tutuldu - talimatin GRA
tablosunda 6 satiri. Denetimde bes cevabin da GRA'si 6 cikti, genel band 6,5'te
kaldi. Sonradan duzeltmek yerine hedefi yazarken tutturmak, ikinci gruptaki
"metin bitti, simdi hata ekleyelim" isleminden daha saglikli sonuc verdi.

### Denetimde dikkat cekenler

- **Band 5 cevaplarinda eksik birakilan madde her gorevde farkli** ve her biri gorevin
  kendi `common_mistakes` listesinden alindi: GT01'de somut talep yok ("please do
  something"), GT02'de uygunluk zamani belirsiz ("in the weekend"), GT03'te hesabi
  tanimlayan hicbir bilgi yok, GT04'te "simdiye kadar ne yaptiniz" maddesi hic
  cevaplanmamis, GT05'te ucuncu maddenin "ne zaman" yarisi eksik. Boylece kullanici
  bes ayri tipik hatayi gercek metin uzerinde goruyor.
- **Ton kaymasi band 5'in ayri bir isareti olarak kullanildi**: GT01 "Dear Sir or
  Madam" ile acilip "Best wishes" ile kapaniyor, GT02 "Thanks a lot" ile bitiyor,
  GT03'te "you have cheated me" var, GT05'te kira odememe tehdidi var. Hicbiri
  bastan sona surmedigi icin "ton acikca yanlis" capasi (max 6) ateslenmedi; ton
  tutarsizligi TA'nin 5 satirindan okundu.
- **Band 5'lerde GRA 4, GT03'te 5.** Hatali cumle orani dort mektupta %80'in uzerinde,
  GT03'te %73. Anlam hicbir yerde kaybolmadigi icin cevaplar 3'e degil 4-5'e oturuyor
  ve genel band diger olcutler tarafindan 5,0'da tutuluyor.
- **Band 8'lerde LR mektup dilinde olculdu**: `advertised time`, `pressure gauge`,
  `credit note`, `smallholding`, `a fortnight` gibi ogeler hem az kullanilan hem de
  mektubun tonuna uygun. Yine de hicbiri kusursuz degil - GT01'de "badly unreliable",
  GT02'de fazla uzun bir cumle, GT03 ve GT05'te son paragraflarin ritmi
  `what_would_lift_it` alanlarinda aciktan isaret edildi.
- **GT05 yari resmi ton icin ayri tutuldu**: uc seviyede de "Dear Mr Halstead" ile
  aciliyor ve kapanis "Best regards / Kind regards". Resmi dort mektuptaki "Yours
  faithfully" kalibiyla karsilastirilinca ton farki kullanicinin gozunde somutlasiyor.

---

## 4. grup - General Task 2 (T2-24, T2-09, T2-11, T2-53, T2-57)

Talimat: `degerlendirme/yazma-task2.md` (Task 2 iki modulde de ayni olcutlerle
puanlaniyor). Genel band = dort olcutun ortalamasi, en yakin yarim banda yuvarlanmis
(.25 ve .75 yukari).

### Gorev secimi

Task 2 gorevleri `module: "both"` oldugu icin Academic / General ayrimi gorevin
kendisinde degil, secimde. 2. gruba soyut ve kurumsal konular alinmisti; bu gruba
adayin kendi gunluk hayatindan ornek verebilecegi konular secildi. Bes soru
kalibinin her birinden bir gorev alindi ve 2. grubun konu alanlari (egitim, ulasim,
sehir hayati, teknoloji, kultur) tekrar edilmedi.

| Kod | Kalip | Konu alani | Konu |
|---|---|---|---|
| T2-24 | opinion | is hayati | ise alirken kisisel nitelikler mi diploma mi |
| T2-09 | discuss_both_views | aile ve toplum | cocugu buyukanne mi ebeveyn mi buyutmeli |
| T2-11 | problem_solution | tuketim | hanelerde yemek israfi |
| T2-53 | advantages_disadvantages | yaslanan nufus | dusuk kira karsiligi oda ve yardim |
| T2-57 | double_question | saglik | disarida yemek ve hazir yiyecek |

| Gorev | Hedef | TA | CC | LR | GRA | Genel | Sapma | Yeniden yazildi mi |
|---|---|---|---|---|---|---|---|---|
| T2-24 | 5,0 | 5 | 5,5 | 5 | 4 | **5,0** | 0 | hayir |
| T2-24 | 6,5 | 7 | 6 | 6,5 | 6 | **6,5** | 0 | hayir |
| T2-24 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |
| T2-09 | 5,0 | 5 | 5 | 5 | 4 | **5,0** | 0 | hayir |
| T2-09 | 6,5 | 7 | 6 | 6,5 | 6 | **6,5** | 0 | **evet** (bkz. asagi) |
| T2-09 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |
| T2-11 | 5,0 | 5 | 5 | 5 | 4 | **5,0** | 0 | hayir |
| T2-11 | 6,5 | 7 | 6 | 6,5 | 6 | **6,5** | 0 | hayir |
| T2-11 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |
| T2-53 | 5,0 | 5 | 5 | 5 | 4 | **5,0** | 0 | hayir |
| T2-53 | 6,5 | 7 | 6 | 6,5 | 6 | **6,5** | 0 | **evet** (bkz. asagi) |
| T2-53 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |
| T2-57 | 5,0 | 5 | 5 | 5 | 4 | **5,0** | 0 | hayir |
| T2-57 | 6,5 | 7 | 6 | 6,5 | 6 | **6,5** | 0 | **evet** (bkz. asagi) |
| T2-57 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |

### Yeniden yazilan: uc gorevin 6,5 hedefli cevabi

Bu grupta denetim, 2. gruptaki gibi bandi degil, **bandin dayanagini** duzeltti.
Hatali cumle orani her metinde tek tek sayildi (talimatin GRA tablosu bandi bu
orandan okuyor) ve uc metin hedef araligin disinda kaldi:

- **T2-57 / 6,5** - oran %38 cikti, yani tablonun 7 satiri (%20-40). Sayilan puan
  TA 7 · CC 6 · LR 6,5 · GRA 7 = 6,625 → 7,0, hedefin 0,5 disinda. Iki hata eklendi
  (`dishes from other countries` → `from other country`, `each meal looks cheap` →
  `each meal look cheap`), oran %54'e cikti, GRA 6 oldu.
- **T2-53 / 6,5** - ters yonde: oran %62 cikti, yani 5 satirinin (%60-80) icine
  dustu. Bir hata geri alindi (`help with the shopping, the technology or the
  garden` → `the computer`), oran %54 oldu.
- **T2-09 / 6,5** - oran %50 ile dogru satirdaydi ama hatalarin dordu de ayni
  turdendi (cogul/tanimlik). Cesitlilik icin biri edata cevrildi
  (`frightened by a fever` → `frightened from a fever`); band degismedi, hata
  profili hedef bandda gercekten gorulen dagilima yaklasti.

Metinlerin fikir yapisina, tutumuna ve sozcuk secimine dokunulmadi.

### Denetimde dikkat cekenler

- **Sayim tahminin yerini aldi.** 3. grupta hedef yazarken tutturulmustu; burada
  ayni sey yapildi ama denetimde oran yine de elle sayildi ve bes metnin ucunde
  tahminle sayim ayrisiyordu. Ikisi de asagi degil **yukari** yondeydi: goz "burada
  yeterince hata var" derken tablo 7 satirini gosteriyordu. Talimatin "count; do not
  estimate by impression" uyarisi ters yonde de calisiyor.
- **Band 5'lerde gorevin bir yarisi bilerek eksik**, her gorevde farkli bicimde ve
  her biri gorevin kendi `common_mistakes` listesinden: T2-24'te karsilastirma hic
  yapilmayip iyi calisan ozellikleri siralanmis, T2-09'da ikinci gorus savunulmadan
  iki cumlede reddedilmis ve metin kendi aile anisina donmus, T2-11'de sorunlar
  bolumu aclik konusuna kayip onlemler iki dilek cumlesine inmis, T2-53'te iki liste
  yazilip hukum hic verilmemis, T2-57'de degerlendirme tek desteksiz cumleye
  indirgenmis. Bes cevapta da TA'nin "iki yukumlulukten biri karsilanmiyor →
  max 5" capasi acikca atesleniyor.
- **Band 5 kelime sayilari 252-272.** Hepsi 250'nin ustunde ama ucunda; en dusugu
  T2-57 (252). `max 6` (250 alti) ve `max 5` (188 alti) capalari hicbir cevapta
  devreye girmedi - dusuklugun sebebi olcutler, eksik kelime degil.
- **Band 5'lerde GRA 4.** Hatali cumle orani bes cevapta da %80'in uzerinde ve
  range sinirli (basit cumle + tek tuk if/who). Anlam hicbir yerde kaybolmadigi
  icin cevaplar 3'e degil 4'e oturuyor, genel band diger uc olcut tarafindan
  5,0'da tutuluyor.
- **Band 8'ler kusursuz degil**: her birinde bir gerekce otekilerden ince kaliyor
  (T2-24'te deneyim paragrafi, T2-11'de belediye onlemi, T2-53'te "reported
  outcomes are good" genellemesi, T2-57'de adalet argumani) ve `what_would_lift_it`
  alani tam bunu isaret ediyor. Hicbiri band 9 hedeflemiyor.
- **Uc seviyede de tutum ayni tarafta** tutuldu, 2. gruptaki gibi: ayni gorev, ayni
  pozisyon, farkli yurutme. Fark fikirden degil dilden ve gelistirmeden geliyor.
- **Metinler `tools/_c1_uret4.py` icinde duruyor**, kelime sayisi uretimde
  sayiliyor - metin duzeltilince JSON'daki sayac sessizce yanlis kalmasin diye.
  2. gruptaki `_c1_uret2.py` ile ayni kalip.

---

## 5. grup - Academic Task 1 (AT06-AT08) + Academic Task 2 (T2-44, T2-39)

Talimatlar: `degerlendirme/yazma-task1-academic.md` ve `degerlendirme/yazma-task2.md`.
Genel band = dort olcutun ortalamasi, en yakin yarim banda yuvarlanmis (.25 ve .75 yukari).

### Gorev secimi

Dagilim tablosu bu gruba uc Task 1 ve iki Task 2 gorevi veriyor. Task 1'de AT01-AT05'ten
sonraki uc gorev alindi ve gorsel turu bilerek ayrildi; **harita ilk kez bu grupta
ornekleniyor** (1. grupta cizgi, sutun, tablo ve pasta vardi).

| Kod | Gorsel | Konu |
|---|---|---|
| AT06 | harita (once/sonra) | Ferndale koyu 1985 ve 2020 |
| AT07 | cizgi grafik | dort bolgede evde internet baglantisi, 2000-2020 |
| AT08 | sutun grafik | bes tatil turu, 2005 ve 2020 |

Task 2'de 2. grubun olcutu korundu - soyut ve kurumsal konu, adayin kendi gunluk
hayatindan ornek veremeyecegi turden (4. grup bunun tersini yapmisti). Iki gorev de
havuzun `hard` kademesinden secildi: kutuphanede simdiye kadar hic hard Task 2 yoktu,
oysa gercek sinavda konu bu soyutlukta gelebiliyor.

| Kod | Kalip | Konu alani | Konu |
|---|---|---|---|
| T2-44 | opinion | kamu butcesi | uzay arastirmasi mi konut ve saglik mi |
| T2-39 | double_question | kamu hizmeti | hizmetlerin ozel sirketlere gecmesi |

| Gorev | Hedef | TA | CC | LR | GRA | Genel | Sapma | Yeniden yazildi mi |
|---|---|---|---|---|---|---|---|---|
| AT06 | 5,0 | 5 | 5,5 | 5 | 4 | **5,0** | 0 | hayir |
| AT06 | 6,5 | 7 | 6,5 | 6,5 | 6 | **6,5** | 0 | hayir |
| AT06 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |
| AT07 | 5,0 | 5 | 5,5 | 5 | 4 | **5,0** | 0 | hayir |
| AT07 | 6,5 | 7 | 6,5 | 6,5 | 6 | **6,5** | 0 | hayir |
| AT07 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | **evet** (bkz. asagi) |
| AT08 | 5,0 | 5 | 5,5 | 5 | 4 | **5,0** | 0 | hayir |
| AT08 | 6,5 | 7 | 6 | 6,5 | 6 | **6,5** | 0 | hayir |
| AT08 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |
| T2-44 | 5,0 | 5 | 5 | 5 | 4 | **5,0** | 0 | hayir |
| T2-44 | 6,5 | 7 | 6 | 6,5 | 6 | **6,5** | 0 | hayir |
| T2-44 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | **evet** (bkz. asagi) |
| T2-39 | 5,0 | 5 | 5 | 5 | 5 | **5,0** | 0 | hayir |
| T2-39 | 6,5 | 7 | 6 | 6,5 | 6 | **6,5** | 0 | hayir |
| T2-39 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | **evet** (bkz. asagi) |

### Yeniden yazilanlar

Bu grupta hicbir cevap **band** sapmasi yuzunden yeniden yazilmadi; uc duzeltmenin ikisi
uzunluk, biri veri dogrulugu.

- **AT07 / 8,0 - veri hatasi.** Ilk yazimda "both had connected roughly half of their
  households by 2005" yaziyordu; 2005 degerleri %50 ve %42. Talimatta `visual` ile
  celisen rakam Task Achievement altinda dogruluk hatasi sayiliyor ve band 8 satiri
  bunu tasimaz. "Both had at least doubled their coverage by 2005" ile degistirildi -
  25→50 ve 18→42 icin ikisi de dogru. Bandi degistirmedi, ama denetim yapilmasaydi
  "band 8 boyle yazar" diyen bir ornekte yanlis rakam kalacakti.
- **T2-44 / 8,0 ve T2-39 / 8,0 - uzunluk.** Ilk yazimda 386 ve 388 kelimeydiler.
  Kutuphanedeki oteki 8'ler 275-290 araliginda; 40 dakikada 390 kelime yazmasi beklenen
  bir ornek, hedef kullaniciya (band 6'dan 7'ye cikmak isteyen biri) yanlis model
  gosterir. Fikir yapisina dokunulmadan sikistirildi: 350 ve 360. Yine de kutuphanenin
  ustunde duruyorlar - iki gorev de iki yukumluluklu ve `hard`, bu yuzden bu kadar
  asagi cekilebildi.
- Ayni sebeple **uc Task 1 band 5 cevabi** 188-190'dan 171-174'e indirildi; 1. gruptaki
  band 5'ler 164-171 idi ve "sinirin ucunda" olmalari kasitli.

### Denetimde dikkat cekenler

- **Hatali cumle orani her metinde tek tek sayildi**, 4. gruptaki gibi tahmin edilmedi.
  Task 1 band 6,5'larda oran %50-55 (AT06 6/11, AT07 5/10, AT08 5/10), Task 2
  band 6,5'larda %43-57 (T2-44 8/14, T2-39 6/14) - hepsi talimatin 6 satirinda (%40-60).
- **T2-39 / 5,0 band 5'lerin genel kalibini kirdi: GRA 4 degil 5 cikti.** Hatali cumle
  orani %64 (14 cumlenin 9'u), yani talimatin 5 satiri (%60-80). Sebep, metnin uc
  sebebini tanitan kisa cumlelerin ("The first reason is the money.") hatasiz olmasi.
  Genel band yine 5,0 oldugu icin yeniden yazilmadi; tersine, kutuphaneye simdiye kadar
  bulunmayan bir profil ekliyor - band 5, GRA 4 demek zorunda degil.
- **Butun band 5'lerde genel bakis / hukum capasi bilerek atesleniyor.** Uc Task 1
  cevabinda da genel bakis yok (max 5) ve son paragraf gorselde bulunmayan bir sebep
  uyduruyor (max 6): AT06'da hayatin rahatlamasi, AT07'de adalar ve devlet tavsiyesi,
  AT08'de ucak biletlerinin pahalanmasi. T2-39'da ikinci yukumluluk (olumlu mu olumsuz
  mu) tek desteksiz cumleye indirgenmis, yani "iki yukumlulukten biri karsilanmiyor →
  max 5" capasi aciktan atesleniyor.
- **Kelime sayisi capasi hicbir cevapta ateslenmedi.** Task 1 band 5'leri 171-174
  (sinir 150), Task 2 band 5'leri 269-272 (sinir 250). `max 6` ve `max 5` kelime
  capalari hicbir yerde devreye girmedi - dusuklugun sebebi olcutler, eksik kelime degil.
- **Haritada band farki konum diliyle olculdu.** Band 5 in the north part / in the east
  side ile yetiniyor, band 6,5 to the north of the main road / on the eastern side
  kaliplarina geciyor, band 8 given over to housing, gave way to, survived the period
  intact ile degisimin turunu de adlandiriyor. AT06'nin `common_mistakes` listesindeki
  ilk iki madde (yon dili kullanmamak, iki haritayi ayri ayri betimlemek) tam olarak
  band 5 cevabinda gorunuyor.
- **Band 8'ler kusursuz degil**: AT06'da "thrown across the river" biraz agir, AT07'de
  "the best and the worst served areas" sikisik, AT08'de ikinci cumle uc bilgiyi birden
  tasiyor, T2-44'te riskin kime dustugu paragrafi otekilerden kisa, T2-39'da ucuncu
  sebep ince. Hepsi `what_would_lift_it` alaninda aciktan isaret edildi; hicbiri band 9
  hedeflemiyor.
- **Uc seviyede de tutum ayni tarafta** tutuldu (T2-44'te konut ve saglik once,
  T2-39'da nitelenmis olumlu): ayni gorev, ayni pozisyon, farkli yurutme.
- **Metinler `tools/_c1_uret5.py` icinde duruyor**, kelime sayisi uretimde sayiliyor ve
  alt sinir gorev turune gore (150 / 250) kontrol ediliyor. `_c1_uret2.py` ve
  `_c1_uret4.py` ile ayni kalip.

### 6. gruba kalan

GT06-GT08 (General Task 1 mektup) + T2 havuzundan iki gorev. Kullanilmis on iki Task 2
gorevi: T2-01, 06, 09, 10, 11, 15, 17, 24, 39, 44, 53, 57. Bes kaliptan opinion ve
double_question ucer kez kullanildi; 6. grup icin gunluk hayata bakan iki konu ve iki
kez kalmis kaliplardan ikisi (problem_solution, discuss_both_views ya da
advantages_disadvantages) uygun olur.

---

## 6. grup - General Task 1 (GT06-GT08) + Task 2 (T2-50, T2-54)

Talimatlar: `degerlendirme/yazma-task1-general.md` ve `degerlendirme/yazma-task2.md`.
Genel band = dort olcutun ortalamasi, en yakin yarim banda yuvarlanmis (.25 ve .75 yukari).
Bu grup kutuphanenin yazma yarisini 30 goreve tamamliyor.

### Gorev secimi

Mektup tarafinda GT01-GT05'ten sonraki uc gorev alindi ve **ton bilerek ayrildi**. 3. grupta
dort resmi + bir yari resmi mektup vardi; burada iki yari resmi ve **ilk kez bir samimi
mektup** var. Boylece kutuphanede uc tonun de ornegi bulunuyor ve kullanici ayni bandin
uc farkli tonda nasil gorundugunu karsilastirabiliyor.

| Kod | Ton | Konu |
|---|---|---|
| GT06 | yari resmi | kurs icin calisma saati degisikligi - yoneticiye |
| GT07 | yari resmi | cati tamiri ve gecis izni ricasi - komsuya |
| GT08 | samimi | baska bir kasabaya tasinma - arkadasa |

Task 2'de 4. grubun olcutu korundu: adayin kendi gunluk hayatindan ornek verebilecegi
konu (5. grup bunun tersini, soyut ve kurumsal konuyu yapmisti). 5. grubun notu iki kez
kalmis kaliplardan ikisini oneriyordu; secilen iki gorev de kutuphanede **hic bulunmayan
konu alanindan** geliyor.

| Kod | Kalip | Konu alani | Konu |
|---|---|---|---|
| T2-50 | problem_solution | dil ve iletisim | is yerinde yazili mesaj yuku |
| T2-54 | advantages_disadvantages | suc ve ceza | kamusal alanlarda kamera |

Otuz gorevin son dagilimi: AC-T1 8 · GT-T1 8 · Task 2 14 (opinion 3 · discuss_both_views 2 ·
problem_solution 3 · advantages_disadvantages 3 · double_question 3).

| Gorev | Hedef | TA | CC | LR | GRA | Genel | Sapma | Yeniden yazildi mi |
|---|---|---|---|---|---|---|---|---|
| GT06 | 5,0 | 5 | 5,5 | 5 | 4 | **5,0** | 0 | hayir |
| GT06 | 6,5 | 7 | 6 | 6,5 | 6 | **6,5** | 0 | **evet** (bkz. asagi) |
| GT06 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |
| GT07 | 5,0 | 5 | 5,5 | 5 | 4 | **5,0** | 0 | hayir |
| GT07 | 6,5 | 7 | 6 | 6,5 | 6 | **6,5** | 0 | hayir |
| GT07 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |
| GT08 | 5,0 | 5 | 5,5 | 5 | 4 | **5,0** | 0 | hayir |
| GT08 | 6,5 | 7 | 6 | 6,5 | 6 | **6,5** | 0 | hayir |
| GT08 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |
| T2-50 | 5,0 | 5 | 5 | 5 | 4 | **5,0** | 0 | hayir |
| T2-50 | 6,5 | 7 | 6 | 6,5 | 6 | **6,5** | 0 | hayir |
| T2-50 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |
| T2-54 | 5,0 | 5 | 5 | 5 | 4 | **5,0** | 0 | hayir |
| T2-54 | 6,5 | 7 | 6 | 6,5 | 6 | **6,5** | 0 | **evet** (bkz. asagi) |
| T2-54 | 8,0 | 8 | 8 | 8 | 8 | **8,0** | 0 | hayir |

### Yeniden yazilan: GT06 / 6,5 ve T2-54 / 6,5

Hatali cumle orani on cevabin her birinde tek tek sayildi (talimatin GRA tablosu bandi bu
orandan okuyor). Iki metin hedef araligin **iki ayri yonunde** disarda kaldi - ayni denetimin
her iki yonde de calistigi 4. grupta gorulmustu, burada tek grupta ikisi birden cikti:

- **GT06 / 6,5 - oran %64**, yani tablonun 5 satiri (%60-80). Sayilan puan TA 7 · CC 6 ·
  LR 6,5 · GRA 5 = 6,125 → 6,0; hedefin tam 0,5 disinda degil ama altinda. Iki hata geri
  alindi (`will start in 3 March` → `on 3 March`, `the same number of the hours` →
  `the same number of hours`), oran %45 oldu, GRA 6'ya cikti.
- **T2-54 / 6,5 - oran %29**, yani tablonun 7 satiri (%20-40). Genel band yine 6,5 cikiyordu
  (TA 7 · CC 6 · LR 6,5 · GRA 7 = 6,625 → 6,5) ama dayanagi yanlisti: "band 6,5 cevabi" diye
  band 7 dilbilgisi gosteriyorduk - 2. ve 4. gruptaki kusurun aynisi. Uc hata eklendi ve
  turleri bilerek ayrildi: cogul (`the two sides` → `the two side`), uyum (`a person who is
  doing nothing wrong` → `the people who is doing nothing wrong`), yine uyum ama farkli
  yapida (`the access to the images is limited` → `are limited`). Oran %50 oldu, GRA 6.

Iki metnin de fikir yapisina, tutumuna ve sozcuk secimine dokunulmadi.

### Denetimde dikkat cekenler

- **Uzunluk bu kez denetimden once duzeltildi.** 5. grubun dersi (386-388 kelimelik band 8'ler
  hedef kullaniciya yanlis model gosteriyor) bastan uygulanmadi ve ilk uretimde metinler yine
  uzun cikti: T2-50 / 8,0 365, T2-54 / 8,0 342, GT08 / 8,0 308, GT07 / 8,0 301 kelime. Hepsi
  fikir yapisina dokunulmadan sikistirildi; son degerler 265-294, yani kutuphanenin geri
  kalaniyla ayni araliktalar. **Bu kusur ucuncu kez ayni yerde cikiyor** - 40 dakikada
  yazilabilecek uzunluk, uretim sirasinda kendiliginden korunmuyor.
- **Hatali cumle oranlari** (sayilan / toplam): band 5'lerde GT06 9/11, GT07 8/8, GT08 7/7,
  T2-50 10/12, T2-54 11/12 - hepsi %80'in uzerinde, yani GRA 4. Band 6,5'larda duzeltmeden
  sonra GT06 5/11, GT07 6/12, GT08 7/13, T2-50 6/14, T2-54 7/14 - hepsi %43-54 arasinda,
  talimatin 6 satirinda (%40-60).
- **Band 5'lerde eksik birakilan yukumluluk her gorevde farkli** ve her biri gorevin kendi
  `common_mistakes` listesinden: GT06'da ucuncu madde "don't worry" ile geciliyor (isin nasil
  yurutulecegi hic yok), GT07'de ikinci madde etkiyi anlatmak yerine kucumsuyor, GT08'de davet
  "come and stay with me sometime" ile belirsiz birakiliyor, T2-50'de onlemler bolumu tek dilek
  cumlesi, T2-54'te dezavantaj tarafi hic yazilmayip ceza agirligi tartismasina kayiyor.
  Sonuncusu talimatin "yanindaki baska soruyu cevapliyor → max 5" capasini da atesliyor.
- **Ton kaymasi uc mektupta uc ayri bicimde** kullanildi: GT06'da emir kipi ve Thanks a lot
  kapanisi, GT07'de "must to use" ile yumusatilmamis rica, GT08'de samimi mektubun
  "I am writing to inform you" ile acilip "Yours faithfully" ile kapanmasi. Hicbiri bastan sona
  surmedigi icin "ton acikca yanlis" capasi (max 6) ateslenmedi; tutarsizlik TA'nin 5 satirindan
  okundu - 3. gruptaki olcutun aynisi.
- **GT08 / 5,0 bilerek tek blok halinde yazildi**, gorevin `common_mistakes` listesindeki
  "paragrafsiz tek blok" maddesi gercek metin uzerinde gorunsun diye. Paragraf capasi (max 6)
  ve cumle siniri capasi (max 6) atesleniyor, ama sira izlenebildigi icin CC 5'e degil 5,5'e
  oturuyor. Genel band yine 5,0.
- **Kelime sayisi capasi hicbir cevapta ateslenmedi.** Mektup band 5'leri 182-199 (sinir 150),
  Task 2 band 5'leri 268-270 (sinir 250). Mektuplarda selamlama ve imza dahil sayildi; bunlar
  cikarilinca en kisa mektup (GT06 / 5,0) 174 kelime, yani yine sinirin ustunde.
- **Band 8'ler kusursuz degil**: GT06'da ikinci paragrafin ilk cumlesi uc bilgiyi birden
  tasiyor, GT07'de acilistaki `warn` bir rica mektubu icin fazla sert, GT08'de ucuncu paragrafin
  son cumlesi uzun, T2-50'de sessiz saat onerisi otekilerden kisa, T2-54'te maliyet argumani
  yalnizca son paragrafta geciyor. Hepsi `what_would_lift_it` alaninda aciktan isaret edildi;
  hicbiri band 9 hedeflemiyor.
- **Uc seviyede de tutum ayni tarafta** tutuldu: T2-50'de kurum kurallari kisisel aliskanliktan
  once, T2-54'te kosullu olumlu. Ayni gorev, ayni pozisyon, farkli yurutme.
- **Metinler `tools/_c1_uret6.py` icinde duruyor**, kelime sayisi uretimde sayiliyor ve alt
  sinir gorev turune gore (150 / 250) kontrol ediliyor. `_c1_uret2.py`, `_c1_uret4.py` ve
  `_c1_uret5.py` ile ayni kalip.

### Yazma yarisi bitti - konusmaya kalan

Otuz yazma gorevi × uc seviye = 90 cevap tamam. Kalan dort calistirma konusma kartlari:
20 kart × 3 seviye = 60 cevap, Part 2 kartlari oncelikli. Konusmada olcut ucluye dusuyor
(akicilik · sozcuk · dilbilgisi), `text` yerine `transcript` yaziliyor ve
`approx_duration_seconds` ekleniyor; talimat `degerlendirme/konusma.md`. Yazma tarafindan
tasinacak iki ders: **hedef bandi yazarken tutturmak sonradan duzeltmekten saglikli sonuc
veriyor** (3. grup) ve **uzunluk uretimde kendiliginden korunmuyor, denetimde olculmeli**
(5. ve 6. grup).
