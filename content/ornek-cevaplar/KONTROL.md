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

---

## Yazma yarisinin ikinci duzey denetimi (uretim yok)

Otuz dosya uretildikten sonra iki denetim daha yapildi. Ikisinde de yeni cevap
uretilmedi; var olan 90 cevap disaridan olculdu.

**Birinci denetim (sema):** hepsi gecerli JSON; her dosyada tam olarak band 5,0 / 6,5 / 8,0
uclusu var; `task_ref` dosya adiyla uyusuyor; zorunlu alanlar dolu; JSON'daki `word_count`
degerleri gercek sayimla birebir tutuyor.

**Ikinci denetim (gorevle iliski):** `python tools/_c1_denetim.py`. Semanin degil, cevabin
**gorevin kendisiyle** tutarli olup olmadigina bakiyor - 5. grupta AT07'de elle bulunan
veri hatasi turunden bir kusur baska bir yerde daha kalmis mi diye:

| | Denetim | Sonuc |
|---|---|---|
| A | `task_ref` havuzdaki gercek gorev dosyasina cozunuyor mu, klasor turu tutuyor mu | 30/30 temiz |
| B | kelime sayisi gorevin **kendi** `min_words` degerinin uzerinde mi (sabit 150/250 degil) | 90/90 temiz |
| C | `why_this_band` alanlari ve `what_would_lift_it` "<=2 cumle" sinirinda mi | 90/90 temiz |
| D | cevap gercekten o gorevden mi bahsediyor (icerik sozcugu ortusmesi) | 90/90 temiz |
| E | Academic Task 1 cevaplarindaki sayilar `visual` verisiyle uyusuyor mu | 364 sayi, hepsi temiz |
| F | dosyalar arasi kopyala-yapistir (ayni cumle iki ayri gorevde) | yok |
| G | KONTROL.md 30 gorevin hepsini kapsiyor mu | 30/30 |

Dagilim da script'ten sayildi ve 6. grubun notundaki rakami dogruluyor: AC-T1 8 ·
GT-T1 8 · Task 2 14 (opinion 3 · discuss_both_views 2 · problem_solution 3 ·
advantages_disadvantages 3 · double_question 3).

### Denetimden cikan iki not

- **AT08 / 8,0 ilk taramada takildi**, sonra dogru cikti: metindeki 21 ve 26,5
  gorselde yazmiyor, cunku bes sutunun toplami (8,4+3,1+2,2+6,0+1,3 = 21,0 ve
  6,2+7,5+4,4+5,8+2,6 = 26,5). Rakamlar dogru; eksik olan denetimdi, seri toplamlari
  da mesru sayi kabul edilecek sekilde genisletildi. E denetiminin sinirini burada
  soylemek gerekiyor: **gorselden hicbir yolla turetilemeyen sayiyi yakalar**, yanlis
  yorumu (dogru sayilarla kurulmus hatali cumleyi) yakalamaz.
- **Band 5 cevaplari gorevin sozcuklerini kullanmiyor** - T2-44'te "housing and health
  care" yerine "the house and the hospital", T2-50'de "employees" yerine "the workers
  in the offices", T2-11'de "thrown away" yerine "throw it in the bin". Ortusme band 5'te
  ortalama %50, band 6,5'ta %67. Bu konu disiligi degil, sinirli sozcuk dagarciginin
  kendisi; D denetiminin esigi bu yuzden bandda ayrildi ve amaci yanlis eslesmis dosyayi
  yakalamak, uslup olcmek degil.

---

## Yazma yarisinin ucuncu duzey denetimi: BAND AYRIMI (uretim yok)

Onceki iki denetim semaya ve gorevle iliskiye bakiyordu; ikisi de bir cevabin
**hedefledigi bandda olup olmadigina** bakmiyordu. Prompt'un kirmizi basligi tam
olarak bunu soyluyor:

> "En sik yapilan hata: uc cevabin da duzgun Ingilizce olmasi, sadece uzunlugun
> degismesi. Band 5 cevabi gercekten band 5 olmali - hata icermeli."

`python tools/_c1_ayrim.py` bu hatanin olusup olusmadigini disaridan olcuyor. Band
etiketine bakmadan yedi metrik hesaplaniyor, sonra etiketle karsilastiriliyor.
Hicbir dosya degistirilmedi.

### Sonuc: 90 cevabin band ortalamalari

| band | kelime | TTR (ilk 140 sozcuk) | yan cumle /100 | mekanik baglac | hata izi /100 |
|---|---|---|---|---|---|
| 5,0 | 221 | 0,55 | 0,10 | 2,9 | **3,44** |
| 6,5 | 248 | 0,65 | 0,99 | 0,5 | 0,42 |
| 8,0 | 264 | 0,70 | 1,44 | 0,0 | **0,05** |

Uc seviye her boyutta ayrisiyor, en keskin ayrim dilbilgisinde: band 5'te 100 sozcuge
**3,44** hata izi, band 8'de **0,05** - yaklasik 70 kat. Uzunluk farki ise kucuk
(221 -> 264, %19). Yani kutuphane prompt'un uyardigi tuzaga dusmemis: seviyeler
uzunlukla degil nitelikle ayrisiyor.

| | Denetim | Sonuc |
|---|---|---|
| A | her cevap alt sinirin (T2 250 · digerleri 150) uzerinde mi | 90/90 temiz |
| B | sozcuk cesitliligi band 5 -> 8 arasinda en az 0,03 artiyor mu | 30/30 temiz |
| C | band 8 yan cumle yogunlugu band 5'i geciyor mu | 30/30 temiz |
| D | band 8 band 5'ten daha mekanik degil mi | 30/30 temiz |
| E | band 5 gercekten hata iceriyor, band 8 temiz mi | 30/30 temiz |
| F | ayni dosyanin iki bandi arasinda kopyala-yapistir | yok |
| G | 5 ile 8 farki uzunluk disinda en az 3 boyutta gorunuyor mu | 30/30 temiz |

G'nin dagilimi: 19 gorev 5 boyutun besinde de ayrisiyor, 9 gorev dortte, 2 gorev
ucte. Uctekiler **GT08 ve T2-39**; ikisinde de eksik olan boyutlar en zayif iki
gosterge (cumle uzunlugu sapmasi ve mekanik baglac), dilbilgisi ayrimi ikisinde de
saglam (band 5'te 6 ve 13 hata izi, band 8'de 0).

### Denetimin kendisi dogrulandi (mutasyon testi)

Bir denetimin "temiz" demesi, esiklerin gecmeye ayarlandigi anlamina da gelebilir.
Bunu dislamak icin kutuphanenin gecici bozuk kopyalari denetimden gecirildi:

| Bozma | Bulgu |
|---|---|
| band 5 metni yerine band 8 metni (ayrim tamamen kaldirilmis) | **202** |
| uc bandin da ayni metin olmasi | **223** |
| band 5 cevaplari 80 sozcuge kisaltilmis | **59** |
| bozma yok (gercek kutuphane) | **0** |

Denetim, prompt'un uyardigi hatayi kuruldugunda yakaliyor.

### Ilk yazimda duzeltilen dort olcum hatasi

Denetimin ilk surumu 54 bulgu vermisti; hepsi incelendi, **hicbiri icerik hatasi
degildi** - dordu de olcumun kendi kusuruydu. Kayda geciyor, cunku ayni tuzaklar
konusma tarafi olculurken de kurulabilir:

1. **Sayilar sozcuk sayilmiyordu.** Sayim yalnizca harf dizilerini aliyordu; AT01-AT04
   15-20 sayi eksik sayilarak "150 kelimenin altinda" gorundu. IELTS sayiminda "30%"
   ve "1995" birer sozcuktur. Ayri bir `kelime_say()` eklendi.
2. **"Kelime sayisi bandla birlikte artmali" diye bir kural yok.** Prompt yalnizca alt
   siniri sart kosuyor. Bu uydurma kural yedi dosyayi bulgu isaretledi; kaldirildi -
   zaten prompt'un butun vurgusu farkin uzunlukta *olmamasi* gerektigi yonunde.
3. **Ortak dizi SAYMAK yaniltiyor.** Tek bir 12 sozcukluk ortak cumle "5 ayri ortak
   8'li dizi" olarak gorunup dosya bes kez kopyalanmis gibi okunuyordu. Olcu, en uzun
   kesintisiz ortak diziye cevrildi; esik 15 sozcuk veya kisa cevabin %10'u.
4. **Hata dedektorunun kesinligi ve duyarligi.** Ilk surum bes band 5 cevabinda "tek
   hata izi yok" dedi; metinler elle okundu, hepsi hatayla dolu cikti ("I am write
   this letter for complain", "some peoples", "he don't know") - dedektorun duyarligi
   dusuktu, kalip sayisi 9'dan 17'ye cikarildi. Ters yonde: band 8'de bulunan yedi
   izin **hepsi yanlis alarmdi** ("watched it change", "the rules that come into
   force", "a state which cannot house its people has misjudged" - ucu de dogru
   Ingilizce); algi fiili, iliski zamiri ve iyelik korumalari eklendi.

### Bu denetimin siniri

Kalip tabanli bir dedektor bandi olcmez, bandin **izlerini** olcer. Band 8'de kalan
uc iz (`the dominant use of energy`, `the city break`) ad/fiil belirsizliginden gelen
yanlis alarmdir ve elenemedi. Dogru okuma sudur: bu bir **karsilastirma araci** -
mutlak hata listesi degil, band 5 ile band 8 arasindaki 70 katlik yogunluk farkinin
kaniti. Puanlamanin kendisi hala `degerlendirme/` talimatiyla ve elle yapiliyor;
yukaridaki gruplarin tablolari o puanlamanin kaydi.

### Bulgu sayilmayan gozlem: bandlar arasi ortak dizi

Onbir dosyada band 6,5 ile 8,0 arasinda 8-12 sozcukluk ortak dizi var; en uzunu
GT02'de 12 sozcuk ("the notice on the gate of the Fenton Street community garden
which"). Bunlar kopyala-yapistir degil turun kendi kalibi: Academic Task 1 girisinin
gorev cumlesinin parafrazi (AT08: "the bar chart compares the number of holiday trips
of five"), mektup hitabi ("Dear Sir or Madam, I am writing about") ve gorevin ozel
adlari. Esigin (15 sozcuk) altinda kaldiklari icin yeniden yazim yapilmadi; prompt'un
yeniden yazim olcutu band sapmasidir, ifade tekrari degil. Konusma tarafi uretilirse
ayni olcum orada da anlamli olur - orada ortak kalip daha az mesrudur, cunku
konusmanin acilisi gorev cumlesinin parafrazi degildir.

---

## Yazma yarisinin dorduncu duzey denetimi: GEREKCE - KANIT (uretim yok)

Onceki uc denetim hep **cevabin kendisine** bakti: semasi dogru mu (1), goreve uyuyor
mu (2), hedefledigi bandin izlerini tasiyor mu (3). Hicbiri `why_this_band` ve
`what_would_lift_it` alanlarini okumadi. Oysa kullaniciya "band 7 boyle yazar" diyen
sey cevap kadar onun altindaki gerekcedir: gerekce metinde olmayan bir seyi
gosteriyorsa ornek yanlis seyi ogretir. Puanlama talimati bunu zaten kural yapmis
(`degerlendirme/ORTAK-KURALLAR.md`, BLOCK G):

> "`quote` is a verbatim span of 3-25 words copied exactly from the candidate's
> response. Copy the errors too - do not tidy the spelling, capitalisation or grammar
> of a quote."

Kutuphanenin gerekceleri Turkce yazilmis ama ayni isi yapiyor: iclerinde cevaptan
alinmis Ingilizce parcalar var. `python tools/_c1_gerekce.py` o parcalari cikarip
metinle karsilastiriyor (1273 aday alinti, 450 gerekce alani). Hicbir dosyayi
degistirmez; bulgu varsa cikis 1.

| | Denetim | Ilk kosu | Duzeltmeden sonra |
|---|---|---|---|
| A | gerekcedeki alinti cevabin kendi metninde bire bir var mi | 23 bulgu | 90/90 temiz |
| B | alinti baska bir bandin metninden mi gelmis | 2 bulgu | 30/30 temiz |
| C | "su oge hic gecmiyor" denen sey gercekten gecmiyor mu | yok | temiz |
| D | band 5 / 6,5 onerisi bir ust bandin metninde karsilik buluyor mu | olcum | 4 / 12 |
| E | band 8 kusursuz ilan edilmis mi | yok | 30/30 temiz |
| F | gerekce cumlesi cevaplar arasinda kopyala-yapistir mi | 5 grup (13 cevap) | 0 |
| G | gerekce cevap yerine kisi/sinav hakkinda mi konusuyor (BLOCK I) | yok | 90/90 temiz |
| H | band 5 / 6,5 dilbilgisi gerekcesi bir hata ornegi veriyor mu | 3 bulgu | 60/60 temiz |

### Duzeltilen 34 gerekce alani (cevap metinleri degismedi)

**25 alanda alinti metinle bire bir tutmuyordu.** Ucu uydurmaydi, geri kalani
sikistirilmis ya da duzeltilmis alintiydi - ki BLOCK G'nin acikca yasakladigi sey
budur ("copy the errors too"):

| Tur | Ornek | Metinde gercekte olan |
|---|---|---|
| uydurma oge | AT01/6,5 sozcuk gerekcesi "lowest" diyor | metinde "lowest" hic yok (highest point, steady growth var) |
| uydurma oge | T2-06/8 "Induced demand" | metinde "induced" hic yok ("without demanding a parking space" var) |
| uydurma oge | T2-39/8 "the difficulty is that" | metinde "difficulty" hic yok ("Most services, though, are not so tidy" var) |
| duzeltilmis alinti | T2-01/6,5 "the distance between the two groups" | "the distance between the two group" - cogul hatasi gerekcede duzeltilmis |
| sikistirilmis alinti | GT05/5 "the boiler make" | "The boiler in the kitchen make" |
| sikistirilmis alinti | T2-11/5 "they don't have nothing" | "the people don't have nothing" |
| genisletilmis alinti | T2-54/8 "in far duller ways too" | "in duller ways too" - gerekce "far" eklemis |
| parafraz | T2-50/8 "uninterrupted stretches", "structural remedies" | "the loss of uninterrupted time", "remedies that last are structural" |

Digerleri ayni turden: AT06/6,5 · GT06/8 · GT07/8 (iki oge) · GT08/8 · T2-01/8 ·
T2-11/6,5 · T2-15/5 ve /6,5 · T2-17/5 · T2-39/6,5 · T2-44/5 · T2-53/5 (iki oge) ve
/6,5 · T2-54/6,5 · T2-57/5 ve /6,5.

**6 alanda gerekce cumlesi baska cevaplardan kopyalanmisti.** Bes kalip 13 cevapta
aynen tekrar ediyordu; en yaygini uc dosyada gecen "Hata seyrek ve okuru durdurmuyor;
band 9'un tam rahatligi yok." BLOCK G bunu ayrica yasakliyor ("recycled band-descriptor
language is forbidden"): boyle bir cumle o cevap hakkinda hicbir sey soylemiyor. Her
biri kendi cevabinda somut bir yere baglandi (T2-01/8, T2-06/8, T2-24/8, T2-44/8,
T2-53/8, T2-50/6,5).

**3 alanda alt band dilbilgisi gerekcesi tek bir hata ornegi vermiyordu** - AT03/6,5,
AT04/6,5, AT05/6,5 hepsi "Kalan hatalar anlami engellemiyor" diyip birakiyordu. Band
6,5 cevabinda hata vardir ve ogrenci neyi duzeltecegini ancak gosterilirse gorur;
ucune de metinden alinmis ikiser ornek eklendi (happened in the appliances and
electronics · this is the biggest fall · arrives to a leaf screen gibi).

### Denetimin kendisi dogrulandi (mutasyon testi)

| Bozma | Bulgu |
|---|---|
| gerekcedeki alinti kutuphanede hic gecmeyen sozcuklerle degistirildi | **2** (A) |
| band 8 metninden alinan bir parca band 5 gerekcesine tasindi | **2** (B) |
| metinde gecen Firstly/Secondly icin "hic gecmiyor" dendi | **3** (C) |
| bir gerekce cumlesi baska bir dosyaya kopyalandi | **5** (A+F) |
| band 8 gerekcesine "tamamen hatasiz" yazildi | **1** (E) |
| oneriye "bu ogrenci sinavda kesinlikle 7 alir" yazildi | **3** (G) |
| butun gerekceler bir dosya kaydirildi (hepsi yanlis cevaba bagli) | **984** (A+B+H) |
| bozma yok (gercek kutuphane) | **0** |

### Ilk yazimda duzeltilen dort olcum hatasi

3. duzey denetimin dersi ("temiz gecmeyen denetimden once suphelen") bu kez de
gecerliydi: ilk kosu 275 bulgu verdi, **249'u olcum hatasiydi.**

1. **"Sinirli" yokluk demek degildir.** "go up, go down ile sinirli kaliyor" cumlesi bu
   ogelerin metinde OLDUGUNU soyluyor; ilk surum bunu yokluk iddiasi sayip 238 yanlis
   alarm verdi. C denetimi yalnizca acik yokluk fiiline ("hic gecmiyor", "girmiyor")
   baglandi, "tekrar edilmiyor" disarida birakildi.
2. **Noktali virgul cumleyi bitirir.** "bill, line ile sinirli; refund hic girmiyor"
   tek cumle sayilinca yokluk iddiasi ilk yarinin alintilarina da bulasti (9 alarm).
   Ayni sekilde "... tekrar ediyor VE resmi kaliplar hic yok" cumlesinde yokluk
   baglactan sonraki oge icindir.
3. **"Cumlelerin buyuk cogunlugu hatasiz" bir kusursuzluk iddiasi degildir**, band 8'in
   tarifidir. Yalin "hatasiz" aramasi AT04'u haksiz yere isaretledi; E artik yalnizca
   mutlak ifadeleri ("tamamen hatasiz", "kusursuz", "hicbir hata yok") ariyor.
4. **Cekim eki farki uydurma kanit degildir.** "collect, store, distribute gibi ogeler"
   diyen bir gerekce ogeyi sozluk bicimiyle yazar, metinde "collected", "stored" gecer
   (AT05, T2-09). Bunlar bulgu degil gozlem.

### Bu denetimin siniri

Alinti cikarma kalip tabanlidir ve iki yonden kordur. Ingilizce sozluk kutuphanenin
kendisinden kuruluyor; bu yuzden **hicbir cevapta gecmeyen sozcuklerden kurulmus sahte
bir alinti** ilk surumde gorunmez kaliyordu (mutasyon 1 bunu yakaladi ve olcu
duzeltildi: taninan tek sey Ingilizce islev sozcukleriyse dizi oldugu gibi sinaniyor).
Ters yonde, nadir Turkce sozcukler ("kalibiyla", "ogeleri") alintiya yapisip yanlis
alarm uretebiliyor; bunlar diziyi bolerek elendi. Denetim bir **alinti dogrulama**
aracidir: gerekcenin dogru olup olmadigini degil, gerekcenin gosterdigi seyin metinde
bulunup bulunmadigini olcer. Gerekcenin bandi dogru aciklayip aciklamadigi hala
`degerlendirme/` talimatiyla ve elle karar veriliyor - yukaridaki grup tablolari o
kaydin kendisi.

---

## Konusma yarisinin dort calistirmalik kart dagilimi (20 kart)

Prompt konusma icin "Part 2 kartlari oncelikli" diyor ve toplam 20 kart istiyor.
Havuzda 60 Part 2 karti (C01-C60) ve 20 Part 1 konu seti var. Dagilim:

| Calistirma | Grup | Kartlar |
|---|---|---|
| 7 | Part 2 - bes kart turunden birer tane | C01 (kisi) · C04 (yer) · C07 (nesne) · C10 (olay) · C14 (soyut) |
| 8 | Part 2 - ikinci tur, ayni bes tur | C02 · C05 · C08 · C11 · C15 |
| 9 | Part 2 - ucuncu tur, ayni bes tur | C16 · C19 · C22 · C25 · C29 |
| 10 | Part 1 konu setleri | part1 havuzundan bes set |

Toplam: 15 Part 2 karti + 5 Part 1 seti = 20 kart x 3 seviye = 60 cevap. Part 2
onceligi bu oranla karsilaniyor (dortte uc). Her calistirma bes kart turunu de
gordugu icin kutuphane tek grup uretilmis olsa bile kisi/yer/nesne/olay/soyut
kartlarinin hepsine ornek veriyor.

**Kapsam notu:** uretilen cevap kartin **Part 2 tek kisilik konusmasi**. Part 3
tartismasi bu gruba dahil edilmedi: kartin `speaking_seconds` degeri (90-120 saniye)
Part 2 icindir, sure alani (`approx_duration_seconds`) o pencereye gore hesaplaniyor,
ve Part 3 sinav gorevlisiyle karsilikli konusma oldugu icin tek yonlu bir ornek metin
o bolumun nasil gectigini yanlis gosterirdi.

---

## 7. grup - konusma Part 2 (C01, C04, C07, C10, C14)

Talimat: `degerlendirme/konusma.md`. Yazma tarafindan iki fark var: olcut **uc**
tanedir (akicilik-tutarlilik · sozcuk · dilbilgisi; telaffuz bu urunde puanlanmiyor)
ve genel band ucunun ortalamasi, en yakin yarim banda yuvarlanmis (.25 ve .75 yukari).

Konusma hizi cevabin kendi verisi degil, uretim parametresi: band basina bir hiz
secilip (5,0 icin 80, 6,5 icin 105, 8,0 icin 127 kelime/dakika) sure kelime
sayisindan hesaplandi, cunku talimat akiciligi bu orandan okuyor. Uc hiz da
talimatin tablosunda "slow" ve "moderate" araliklarina denk geliyor; hicbir cevap
kartin 90-120 saniyelik penceresinin disina cikmiyor (uretim script'i cikani
reddediyor).

| Kart | Hedef | FC | LR | GRA | Genel | Sapma | Kelime | Sure | Kelime/dk | Yeniden yazildi mi |
|---|---|---|---|---|---|---|---|---|---|---|
| C01 | 5,0 | 5 | 5 | 5 | **5,0** | 0 | 151 | 115 | 79 | hayir |
| C01 | 6,5 | 6 | 6 | 7 | **6,5** | 0 | 203 | 115 | 106 | hayir |
| C01 | 8,0 | 8 | 8 | 8 | **8,0** | 0 | 244 | 115 | 127 | hayir |
| C04 | 5,0 | 5 | 5 | 5 | **5,0** | 0 | 154 | 115 | 80 | hayir |
| C04 | 6,5 | 6 | 6 | 7 | **6,5** | 0 | 205 | 115 | 107 | hayir |
| C04 | 8,0 | 8 | 8 | 8 | **8,0** | 0 | 251 | 120 | 126 | hayir |
| C07 | 5,0 | 5 | 5 | 5 | **5,0** | 0 | 154 | 115 | 80 | hayir |
| C07 | 6,5 | 6 | 6 | 7 | **6,5** | 0 | 207 | 120 | 104 | hayir |
| C07 | 8,0 | 8 | 8 | 8 | **8,0** | 0 | 239 | 115 | 125 | hayir |
| C10 | 5,0 | 5 | 5 | 5 | **5,0** | 0 | 150 | 110 | 82 | hayir |
| C10 | 6,5 | 6,5 | 6 | 7 | **6,5** | 0 | 208 | 120 | 104 | hayir |
| C10 | 8,0 | 8 | 8 | 8 | **8,0** | 0 | 241 | 115 | 126 | hayir |
| C14 | 5,0 | 5 | 5 | 5 | **5,0** | 0 | 155 | 115 | 81 | hayir |
| C14 | 6,5 | 6 | 6 | 7 | **6,5** | 0 | 209 | 120 | 104 | hayir |
| C14 | 8,0 | 8 | 8 | 8 | **8,0** | 0 | 238 | 110 | 130 | hayir |

Onbes cevabin hepsi hedef bandin icinde, sapma 0; hicbiri yeniden yazilmadi. Puanlama
etiketler ortulerek, dokumler cumle cumle numaralanarak yapildi - talimat dilbilgisinde
"izlenim" yasaklayip sayim istiyor.

### Hatali cumle orani (GRA'nin dayanagi)

Talimatin GRA tablosu bandi hatali cumle oranindan okuyor: %20 alti 8-9 · %20-40 7 ·
%40-60 6 · %60-80 5 · %80 ustu 4. Sayilan degerler:

| Kart | band 5 | band 6,5 | band 8 |
|---|---|---|---|
| C01 | 7/10 = %70 | 3/9 = %33 | 1/12 = %8 |
| C04 | 7/10 = %70 | 3/10 = %30 | 0/12 |
| C07 | 7/10 = %70 | 3/11 = %27 | 0/14 |
| C10 | 7/11 = %64 | 3/10 = %30 | 0/11 |
| C14 | 7/11 = %64 | 4/12 = %33 | 0/12 |

Band 5 cevaplari %64-70 ile 5 satirinin ortasinda duruyor. Bu bilincli: yazma tarafinda
band 5 metinleri %80'in uzerine cikip GRA'da 4 aliyordu ve genel bandi **dort** olcutun
ortalamasi 5,0'da tutuyordu. Konusmada olcut ucte bir agirlikta, yani GRA 4 gelseydi
5+5+4 = 4,67 -> **4,5** olurdu; cevap esigin icinde kalir ama yanlis etiketlenirdi.
Bu yuzden konusmada band 5 metni yazilirken her kartta uc cumle bilerek hatasiz
birakildi.

Ters yondeki tehlike 6,5'ta ve yazma tarafinin 2. grubunda bir kez gerceklesmisti (bes
cevabin hepsi 7,0 cikip yeniden yazilmisti). Burada oran bastan sayilarak yazildigi
icin bes cevap da %27-33 araliginda: 7 satirinin icinde ama 8-9 esiginin (%20)
belirgin uzaginda.

### Band ayriminin sozcuk tarafi

Talimatin LR capasi acik: **7 ve uzeri icin dort ya da daha fazla dogru kullanilmis,
az rastlanan ya da konuya ozgu oge** gerekiyor ve sayilabilmeli. Bes karta gore:

- **band 5** - hicbir cevapta yok; sozcuk gunluk cekirdegin ("very good", "very
  patient", "big bags", "too much hot") disina cikmiyor, yani capa dogrudan atesleniyor.
- **band 6,5** - kart basina iki ya da uc oge (strong accent · sentimental value ·
  in a good mood · notifications). Dordun altinda tutuldu, cunku dorde ciksa band 7
  acilirdi. Yaninda esdizim hatalari duruyor: *she has a very big patience*, *the
  elbows are a little bit used*, *I lose the concentration*, *for all the day*.
- **band 8** - kart basina sekiz ve uzeri: *takes it all in her stride · keeps a level
  head · a stone's throw from · hear myself think · hard-wearing · nipping out ·
  gave her a hand with · crept up on me · slept like a log · knock-on effect*.
  Talimat sekiz ve uzeri dogru, dogal kullanilmis ogenin 8'i destekledigini soyluyor.

### Denetimde dikkat cekenler

- **Band 8 kusursuz degil, ama kusuru dilbilgisinde degil.** Bes cevabin dordunde
  sayilabilir dilbilgisi hatasi yok; 8 ile 9 arasindaki fark akicilikta ve sozcukte
  araniyor: C01'de bir kendini duzeltme (*I've watched her deal with, well, ...*),
  C14'te bir yeniden kurus (*it's not that the material is harder, I mean, ...*),
  C01'de konusmaya ozgu bir uyum kaymasi (*There's a lot of people*). Talimatin 8
  satiri bunlarin ucune de acikca izin veriyor; 9 satiri "hesitation is for content,
  not for language" diyor - bu yuzden hicbiri 9'a cikmiyor.
- **Konusma dili gercekten konusma dili.** Yarim cumleler (*Nothing special, but the
  material is really strong*), doldurma sozcukleri (er, okay, honestly, to be honest,
  mind you), kendini duzeltme ve yeniden baslama var. Talimat bunlari dilbilgisi
  hatasi saymiyor (eksiltili yapi ve onarilan yanlis baslangic hata degil) ama
  akicilik kanitidir; band 5'te en yogun, band 8'de en seyrek.
- **80 kelime capasi hicbir cevapta ateslenmedi.** Talimat Part 2 tek kisilik
  konusmada 80 kelimenin altini akicilikta max 5 ile sinirliyor; en kisa cevap 150
  kelime (C10 / band 5). Yani band 5'in dusuk olmasinin sebebi az konusmus olmak
  degil, olcutlerin kendisi - yazma tarafindaki 150/250 kelime kuralinin konusmadaki
  karsiligi bu.
- **Tek yarim band burada:** C10 / 6,5'ta akicilik 6 degil **6,5** verildi. Anlati
  sirali, dinleyici hicbir yerde kaybolmuyor ve gorunur duraklama yok; ama gecisler
  then / after that / so kalibinda kaliyor, yani 7 satirinin istedigi baglac esnekligi
  tam yok. Iki satir arasi yarim band talimatin sinir ornekte normal saydigi cevap.
  Genel band degismiyor (6,5+6+7 = 6,5).
- **Band 5'te oran yuksek ama anlam kapanmiyor.** Talimat "5 ve alti icin anlamin
  bozulmaya baslamasi gerekir, hatanin sayilabilir olmasi yetmez" diyor. Bes cevapta da
  anlam ayakta; oran 5 satirinda, tarif ise ("karmasik denemeler basitlerden daha
  hatali, hatalar bir olcude zorluk cikariyor") *she listen everybody*, *it go with all
  my trouser*, *my eyes is hurt* gibi yerlerde karsilaniyor. Daha asagi bir band icin
  cevaplarin anlamini bozmak gerekirdi; bu ornek kutuphanesinin isine yaramaz -
  ogrenci burada kendi hatasini taniyabilmeli.

---

## 8. grup - konusma Part 2 (C02, C05, C08, C11, C15)

Dagilim tablosunun ikinci sirasi: ayni bes kart turunun ikinci turu - **C02** (kisi /
"Describe an older person you enjoy listening to"), **C05** (yer / "a building in your
area that you find interesting"), **C08** (nesne / "a gift you gave to someone else"),
**C11** (olay / "an occasion when you had to wait a long time for something"),
**C15** (soyut / "a piece of advice you were given that you still remember").

Yontem 7. grupla ayni ve bilerek degistirilmedi: talimat `degerlendirme/konusma.md`,
olcut uc tane, genel band ucunun ortalamasi (en yakin yarim banda, .25 ve .75 yukari).
Sure yine kelime sayisindan turetildi (band 5,0 -> 80, 6,5 -> 105, 8,0 -> 127
kelime/dakika) ve uretim script'i kartin 90-120 saniyelik penceresi disina cikan metni
reddediyor.

| Kart | Hedef | FC | LR | GRA | Genel | Sapma | Kelime | Sure | Kelime/dk | Yeniden yazildi mi |
|---|---|---|---|---|---|---|---|---|---|---|
| C02 | 5,0 | 5 | 5 | 5 | **5,0** | 0 | 151 | 115 | 79 | hayir |
| C02 | 6,5 | 6 | 6 | 7 | **6,5** | 0 | 211 | 120 | 106 | hayir |
| C02 | 8,0 | 8 | 8 | 8 | **8,0** | 0 | 248 | 115 | 129 | hayir |
| C05 | 5,0 | 5 | 5 | 5 | **5,0** | 0 | 152 | 115 | 79 | hayir |
| C05 | 6,5 | 6 | 6 | 7 | **6,5** | 0 | 214 | 120 | 107 | hayir (gerekce duzeltildi) |
| C05 | 8,0 | 8 | 8 | 8 | **8,0** | 0 | 230 | 110 | 125 | hayir |
| C08 | 5,0 | 5 | 5 | 5 | **5,0** | 0 | 153 | 115 | 80 | hayir |
| C08 | 6,5 | 6 | 6 | 7 | **6,5** | 0 | 205 | 115 | 107 | hayir |
| C08 | 8,0 | 8 | 8 | 8 | **8,0** | 0 | 227 | 105 | 130 | hayir |
| C11 | 5,0 | 5 | 5 | 5 | **5,0** | 0 | 152 | 115 | 79 | hayir |
| C11 | 6,5 | 6 | 6 | 7 | **6,5** | 0 | 210 | 120 | 105 | **evet** (sure + oran) |
| C11 | 8,0 | 8 | 8 | 8 | **8,0** | 0 | 241 | 115 | 126 | hayir |
| C15 | 5,0 | 5 | 5 | 5 | **5,0** | 0 | 148 | 110 | 81 | **evet** (oran) |
| C15 | 6,5 | 6 | 6 | 7 | **6,5** | 0 | 208 | 120 | 104 | **evet** (sure) |
| C15 | 8,0 | 8 | 8 | 8 | **8,0** | 0 | 247 | 115 | 129 | hayir |

Onbes cevabin son halinde sapma 0. Puanlama yine etiketler ortulerek ve dokumler cumle
cumle numaralanarak yapildi.

### Uc yeniden yazim: ucu de bandi kacirdigi icin degil, olcum sinirinda kaldigi icin

Prompt yeniden yazimi "kendi puanin hedef bandin 0,5'i disinda kalirsa" diye tanimliyor;
burada bu durum hic olusmadi. Yine de uc metin degistirildi, sebepleri ayri ayri:

- **C11 / 6,5 ve C15 / 6,5 - sure penceresi.** Ilk yazimda 235 ve 230 kelimeydi; 105
  kelime/dakikada 135 ve 130 saniye ediyor, yani kartin 120 saniyelik ust sinirini
  asiyor. Ikisi de 210 ve 208 kelimeye indirildi (atilan yerler tekrar eden ayrinti
  cumleleri: C11'de "maybe three or four episodes together", C15'te "especially when
  you are tired"). Band tasiyan ogeler - cift olumsuz, sure edati, deyimler -
  korundu, bu yuzden puan degismedi. 7. grupta da ayni denetim iki metni kisaltmisti.
- **C11 / 6,5 - hatali cumle orani sinirda.** Kisaltmadan sonra sayim 4/10 = **%40**
  cikti; bu, talimatin tablosunda 7 satiri (%20-40) ile 6 satiri (%40-60) arasindaki
  tam sinir. Talimat sinirda **ust bandi** almayi soyluyor, yani 7 yine gelirdi, ama
  etiket tek bir sayim tartismasina bagli kalirdi. "the first thing in my mind" edat
  hatasi duzeltildi (-> "on my mind"), oran 3/10 = %30 oldu.
- **C15 / 5,0 - ayni sorun ters yonde.** Sayim 8/10 = **%80** cikmisti, yani 5 satiri
  (%60-80) ile 4 satiri (%80 ustu) arasindaki sinir. Burada asagi kaymanin bedeli
  gercek: GRA 4 gelseydi genel band 5+5+4 = 4,67 -> **4,5** olurdu ve cevap yanlis
  etiketlenirdi. "Now I am in the university" -> "at the university" ile oran
  7/10 = %70'e indi.
- **C05 / 6,5 - metin degil gerekce duzeltildi.** GRA gerekcesi ucuncu hata olarak
  "'instead of this' kurulusu"nu gosteriyordu, ama bu dilbilgisi degil esdizim hatasi
  (ve zaten LR gerekcesinde sayili). Talimat "hatayi ancak dilbilgisi etiketiyle
  adlandirabiliyorsan say" diyor. Gerekce, sayimla ayni uc hatayi gosterecek sekilde
  degistirildi: doesn't work since many years - used like a hospital - two times in a
  month. Cevap metni degismedi.

### Hatali cumle orani (GRA'nin dayanagi)

| Kart | band 5 | band 6,5 | band 8 |
|---|---|---|---|
| C02 | 7/10 = %70 | 3/10 = %30 | 0/12 |
| C05 | 7/10 = %70 | 3/10 = %30 | 0/11 |
| C08 | 7/10 = %70 | 3/10 = %30 | 0/11 |
| C11 | 7/10 = %70 | 3/10 = %30 | 0/16 |
| C15 | 7/10 = %70 | 3/10 = %30 | 0/15 |

Onbes cevap 7. grupla ayni yerlerde duruyor: band 5 %70 ile 5 satirinin ortasinda
(%80 esiginden uzak, cunku konusmada olcut uc tane ve GRA 4 gelirse genel band 4,5'e
duser), band 6,5 %30 ile 7 satirinin ortasinda (%20 esiginden uzak), band 8'de
sayilabilir hata yok.

Band 5'te hatalar dagilmis durumda ve hepsi adlandirilabilir: uyum (*he live*, *he
tell*, *buildings is*, *she take*), duzensiz fiil (*thinked*, *buyed*, *forgetted*),
fiil kalibi (*said me*, *made the exam*, *tell about*, *enjoy to listen*), edat (*in
the telephone*, *in the ground floor*, *in the night*, *in Instagram*), tanimlik (*a
old building*, *the chemistry*), cogul (*many thing*, *two week*, *Many student*),
ilgi adili (*a gift what*, *the best advice what*) ve cift olumsuz (*I don't say
nothing*). Anlam hicbirinde kapanmiyor - talimat 5 ve alti icin anlamin bozulmaya
baslamasini istiyor, hatanin sayilabilir olmasini degil.

### Band ayriminin sozcuk tarafi

Talimatin LR capasi: 7 ve uzeri icin **dort ya da daha fazla** dogru kullanilmis, az
rastlanan ya da konuya ozgu oge sayilabilmeli.

- **band 5** - bes cevabin hicbirinde yok. Sozcuk gunluk cekirdekte kaliyor (*old
  times*, *big clock*, *very very surprised*, *good notes*, *a long time*) ve vurgu
  tekrarla yapiliyor. Capa dogrudan atesleniyor.
- **band 6,5** - kart basina iki ya da uc oge: *military service* - *passed away*
  (C02), *converted into* - *reading room* (C05), *second hand* - *went down well* -
  *a big relief* (C08), *keep myself busy* - *refreshing the page* (C11), *take his
  advice on board* - *easier said than done* - *became a habit* (C15). Dordun altinda
  tutuldu, cunku dorde ciksa band 7 acilirdi. **En sinirda olan C15 / 6,5** (uc oge);
  yaninda duran esdizim hatalari - *repeat the subject*, *somebody said me* - bandi
  6'da tutuyor. Diger dort cevapta da ayni denge var: *we make a long conversation*,
  *I don't get bored from them*, *it makes a big difference in the view*, *she shares
  them in Instagram*.
- **band 8** - kart basina sekiz ve uzeri: *nine times out of ten* - *has this way of
  putting things* - *puts things in perspective* - *a bit roundabout* (C02),
  *an eyesore* - *gutted it* - *stands out a mile* - *a new lease of life* (C05),
  *racked my brains* - *what I landed on* - *a bit of a gamble* - *at the back of a
  cupboard* (C08), *in limbo* - *it dragged on* - *no end in sight* - *a weight off my
  shoulders* (C11), *a classic crammer* - *pull two all-nighters* - *in one ear and out
  the other* - *stood me in good stead* (C15). Talimat sekiz ve uzeri dogru kullanilmis
  ogenin 8'i destekledigini soyluyor.

### Denetimde dikkat cekenler

- **Konusmada 6,5'un tuzagi yazmadakinden farkli: fazla duzgun degil, fazla uzun.**
  Yazma tarafinda 6,5 cevaplari fazla duzgun yazilarak 7,0'a kayiyordu. Konusmada
  bunun karsiligi surenin tasmasi, cunku sure kelime sayisindan hesaplaniyor ve kart
  120 saniyeyle sinirli: bes 6,5 metninden ikisi (C11, C15) ilk yazimda pencereyi
  asti. Bu yapisal bir sinir - 6,5'ta kelime tavani 210 (105 kelime/dakika x 2
  dakika), band 8'de 254, band 5'te 160.
- **Band 8'in kusuru yine dilbilgisinde degil.** Bes cevabin hicbirinde sayilabilir
  dilbilgisi hatasi yok; 8'i 9'dan ayiran sey akicilikta ve sozcukte araniyor:
  C02'de bir kendini duzeltme (*or, well, the village the way it was*), C05'te bir
  yeniden kurus (*it was starting to look like, well, a bit of an eyesore*), C08'de
  bir duraklama (*which was, what, about a year ago now*), C11'de bir araya girme
  (*which, I mean, she had a point*), C15'te bir yeniden ifade (*Or, well, what he
  actually meant was*). Talimatin 8 satiri "occasional repetition or self-correction"a
  acikca izin veriyor; 9 satiri duraklamanin dil icin degil icerik icin olmasini
  istiyor, bu yuzden hicbiri 9'a cikmiyor.
- **Yarim band bu grupta hic gerekmedi.** 7. grupta C10 / 6,5'ta akicilik 6,5
  verilmisti. Burada bes 6,5 cevabinin da gecisleri bilerek kalip halinde birakildi
  (*So*, *In the end*, *Now*, *The reason*, *At that time*), yani hepsi 6 satirinin
  "baglaclar kullaniliyor ama her zaman yerinde degil" tarifine oturuyor.
- **80 kelime capasi yine ateslenmedi.** En kisa cevap 148 kelime (C15 / band 5).
  Band 5'in dusuklugunun sebebi az konusmus olmak degil, olcutlerin kendisi.
- **Konusma dili korundu.** Doldurma sozcukleri (er, okay, honestly, to be honest,
  apparently, I suppose), yarim cumleler (*Five weeks in limbo, basically.* /
  *An hour most evenings, exam or no exam.*), kendini duzeltme ve yeniden baslama her
  seviyede var - band 5'te en yogun, band 8'de en seyrek ve en kontrollu. Talimat
  eksiltili yapiyi ve onarilan yanlis baslangici dilbilgisi hatasi saymiyor, bu
  yuzden hicbiri GRA sayimina girmedi.

### 9. gruba kalan

Dagilim tablosuna gore 9. calistirma **C16 - C19 - C22 - C25 - C29** (ayni bes kart
turunun ucuncu turu), 10. calistirma Part 1 konu setleri. Bu gruptan cikan iki sayi
oraya tasiniyor: 6,5 metinlerinde kelime tavani 210 ve GRA sayimi %30 hedeflenmeli
(%40 sinirina yaklasilmamali), band 5'te sayim %70 hedeflenmeli (%80 siniri genel
bandi 4,5'e dusuruyor).

---
