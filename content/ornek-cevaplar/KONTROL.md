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
| 4 | General Task 2 | henuz secilmedi (T2 havuzundan, 2. gruptakiler haric) |
| 5 | Academic Task 1 (3) + Academic Task 2 (2) | AT06-AT08 + T2 havuzu |
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
