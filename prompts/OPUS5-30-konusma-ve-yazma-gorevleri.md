# ⚠️ BU DOSYAYI ÇALIŞTIRMADAN ÖNCE: `/model opus`

Bu dosya **16 kez** çalıştırılır (her seferinde ayrı oturum):

| # | İş paketi | Üretilecek | Klasör |
|---|---|---|---|
| 1–4 | Konuşma 1. bölüm — her oturumda 5 konu × 10 soru | 50 soru ×4 = 200 | `content/speaking/part1/` |
| 5–8 | Konuşma 2.+3. bölüm — her oturumda 15 kart + kart başına 3 tartışma sorusu | (15 kart + 45 soru) ×4 = 60 + 180 | `content/speaking/part2-3/` |
| 9–11 | Yazma Academic 1. görev — her oturumda 10 görev | 30 | `content/writing/academic-task1/` |
| 12–13 | Yazma General 1. görev (mektup) — her oturumda 10 görev | 20 | `content/writing/general-task1/` |
| 14–16 | Yazma 2. görev (deneme yazısı) — her oturumda 20 konu | 60 | `content/writing/task2/` |

**Toplam 550 birim.**

Oturum başında ilgili klasöre bak, kaç dosya var say, **sıradaki bitmemiş paketi** yap.
Hepsi bittiyse "OPUS5-30 tamam" de ve çık.

Burada cevap anahtarı yok — o yüzden kalite ölçütü **çeşitlilik ve gerçekçilik**.

---

## Önce oku

1. `content/PLAN-soru-dagilimi.md` — G bölümü, telif ve kalite kuralları
2. Format referansı — `referans/text/` (yoksa `.pdf` Read ile):
   - `ielts-speaking-sample-tasks-2023.txt`
   - `ielts-academic-writing-sample-tasks-2023.txt`
   - `ielts-general-training-writing-sample-tasks-2023.txt`
   - `ielts-academic-writing-example-responses-to-parts-1-and-2-with-band-scores-and-examiner-comments.txt`
   - `ielts-general-training-writing-example-responses-to-parts-1-and-2-with-band-scores-and-examiner-comments.txt`

Band puanlı örnek cevaplar dosyası **çok değerli**: sınavın gerçekten ne beklediğini
oradan gör. Ama **hiçbir görev metnini, hiçbir örnek cevabı kopyalama.**

3. `NOTLAR.md` — daha önce hangi konular kullanıldı? **Tekrar yasak.**

---

## Ortak kurallar

- Görev metinleri **İngilizce**, açıklama alanları **Türkçe**
- İngiliz İngilizcesi yazımı
- Kültürel olarak nötr: aday Kazakistan'da, Malezya'da, BAE'de, Avustralya'da olabilir.
  Belli bir ülkeye özgü kurum/gelenek varsayma. Alkol, din, siyaset, savaş, cinsellik yok
- Uydurma isim/kurum/marka. Gerçek şirket, gerçek kişi yasak
- Görev metinlerinde "IELTS" geçmesin
- Her birimin **benzersiz kimliği** olsun ve **ayrı dosyaya** yazılsın

---

# A. Konuşma 1. bölüm — `content/speaking/part1/`

20 konu, konu başına 10 soru. Sınavda görevli 3 konu seçer, her konudan 3–4 soru sorar;
biz havuzu geniş tutuyoruz.

## Konu havuzu (20 konu — dört oturuma beşer dağıt)

Oturum 1: memleket · ev/daire · iş veya çalışma · boş zaman · yemek
Oturum 2: hava durumu ve mevsimler · müzik · ulaşım · alışveriş · arkadaşlar
Oturum 3: spor ve egzersiz · fotoğraf · kitap ve okuma · teknoloji · uyku
Oturum 4: seyahat · sanat ve el işi · hayvanlar · zaman yönetimi · komşuluk

## Soru kuralları

- 10 sorunun **ilk 3'ü kolay ve kişisel** (`Do you…?`, `How often…?`), sonrakiler
  gerekçe ister (`Why…?`, `What kind of…?`, `Has that changed…?`)
- Sorular **kısa** olsun — tek cümle, iki satırı geçmesin
- Evet/hayırla kapanan soru yazma; aday 20–40 saniye konuşabilmeli
- Aynı konudaki 10 soru birbirinin tekrarı olmasın: alışkanlık · tercih · geçmiş ·
  gelecek · karşılaştırma · sebep · değişim · başkaları açısı

## Şema — `content/speaking/part1/T01-hometown.json`

```json
{
  "schema_version": "1.0",
  "set_id": "T01-hometown",
  "skill": "speaking",
  "part": 1,
  "topic": "Hometown",
  "topic_tr": "Memleket",
  "generated_by": "opus",
  "expected_answer_seconds": [20, 40],
  "items": [
    {
      "number": 1,
      "prompt": "Where is your hometown?",
      "focus": "temel bilgi",
      "difficulty": "easy",
      "useful_language": ["located in", "in the north of", "a coastal city"]
    }
  ]
}
```

`useful_language`: band 7 seviyesinde adayın kullanabileceği 3–5 ifade. Uygulama ipucu
olarak gösterecek.

---

# B. Konuşma 2. + 3. bölüm — `content/speaking/part2-3/`

Her dosya **bir kart** ve o kartla bağlantılı **3 tartışma sorusu** içerir. 60 dosya.

## Kart kuralları

Resmi kalıp:

```
Describe a time when you had to make a difficult decision.

You should say:
  what the decision was
  why it was difficult
  how long it took you to decide

and explain how you felt about the decision afterwards.
```

- Başlık `Describe …` ile başlar
- Tam **3 madde** + son satırda `and explain …` ile başlayan bir yönlendirme
- Hazırlık 1 dakika, konuşma 1–2 dakika
- Kart türlerini dengele — 60 kart içinde: **kişi 12 · yer 12 · nesne 12 · olay/deneyim
  16 · soyut (bir fikir, bir alışkanlık, bir başarı) 8**
- Konu adayın **hayatından çıkarabileceği** bir şey olmalı: para, ayrıcalık, seyahat
  geçmişi gerektiren konular yasak ("Describe a country you have visited three times" ❌)
- İki takip sorusu (`follow_up`) ekle — görevli kart bittikten sonra bunları sorar

## 3. bölüm kuralları

Kartın konusundan **soyutlanmış** 3 soru. Kişisel değil toplumsal:
- Kart "zor bir karar" ise 3. bölüm "insanlar neden karar vermekte zorlanır?",
  "teknoloji karar vermeyi kolaylaştırdı mı?", "gençler mi yaşlılar mı daha çabuk karar verir?"
- Üç soru **artan soyutlukta** olsun: genel → karşılaştırma → gelecek/görüş
- Her soru tek cümle

## Şema — `content/speaking/part2-3/C01.json`

```json
{
  "schema_version": "1.0",
  "set_id": "C01",
  "skill": "speaking",
  "card_type": "olay",
  "topic": "Difficult decision",
  "topic_tr": "Zor bir karar",
  "generated_by": "opus",
  "part2": {
    "title": "Describe a time when you had to make a difficult decision.",
    "bullets": [
      "what the decision was",
      "why it was difficult",
      "how long it took you to decide"
    ],
    "closing": "and explain how you felt about the decision afterwards.",
    "preparation_seconds": 60,
    "speaking_seconds": [90, 120],
    "follow_up": [
      "Would you make the same decision again?",
      "Did you ask anyone for advice?"
    ],
    "useful_language": ["I was torn between", "in hindsight", "it came down to",
                        "weigh up the pros and cons"]
  },
  "part3": {
    "items": [
      { "number": 1, "prompt": "Why do some people find it hard to make decisions?",
        "focus": "genel açıklama", "difficulty": "medium" },
      { "number": 2, "prompt": "Do you think young people and older people make decisions differently?",
        "focus": "karşılaştırma", "difficulty": "medium" },
      { "number": 3, "prompt": "Will technology change the way important decisions are made in future?",
        "focus": "gelecek / görüş", "difficulty": "hard" }
    ],
    "useful_language": ["it tends to be the case that", "on balance", "a growing number of"]
  }
}
```

---

# C. Yazma — Academic 1. görev — `content/writing/academic-task1/`

30 görev. Aday bir görseli **tanımlar** (görüş bildirmez), en az 150 kelime, 20 dakika.

## Görsel türü dağılımı (30 görev)

| Tür | Adet |
|---|---|
| Çizgi grafik (line graph) | 6 |
| Sütun grafik (bar chart) | 6 |
| Pasta grafik (pie chart) — genelde 2 pasta karşılaştırmalı | 4 |
| Tablo | 4 |
| Süreç şeması (process) | 4 |
| Harita — aynı yerin iki dönemi | 3 |
| Karma (iki farklı görsel bir arada) | 3 |

## Veri kuralları

- **Veriyi sen uyduracaksın** ama tutarlı olmalı: yüzdeler 100 etsin, toplamlar toplasın,
  eğilimler mantıklı olsun
- Görselde **anlatılacak bir şey** olsun: en az bir belirgin eğilim, bir zirve/dip,
  bir kesişme veya bir çarpıcı fark. Düz çizgi = yazılacak bir şey yok = kötü görev
- 4–6 veri serisi/kategoriden fazlası olmasın (aday 20 dakikada yazamaz)
- Birim, yıl aralığı, kaynak satırı net olsun
- Konular nötr ve genel: enerji kullanımı, ulaşım tercihi, geri dönüşüm oranları, nüfus
  yaş dağılımı, internet kullanımı, su tüketimi, tatil türleri, kütüphane ziyaretleri

## Görsel biçimi

**Grafik ve tablolar için** `visual.chart_data` kullan (uygulama kendi çizecek):

```json
"visual": {
  "kind": "line_chart",
  "title": "Household water use in three cities, 2000-2020",
  "x_label": "Year",
  "y_label": "Litres per person per day",
  "categories": ["2000", "2005", "2010", "2015", "2020"],
  "series": [
    { "name": "Riverton", "values": [210, 198, 172, 155, 140] },
    { "name": "Kelford",  "values": [165, 170, 181, 190, 205] }
  ],
  "unit": "litres",
  "svg": null,
  "alt": "Üç şehirde kişi başı günlük su kullanımının 2000-2020 arası değişimi."
}
```

`kind` değerleri: `line_chart` · `bar_chart` · `pie_chart` · `table` · `process` · `map` · `mixed`

- `pie_chart` için `series` yerine tek seri, `categories` dilimler; iki pasta varsa iki seri
- `table` için `chart_data.headers` + `chart_data.rows`
- **`process` ve `map` için `chart_data` null, `svg` dolu** — SVG kuralları:
  sadece `rect`/`circle`/`line`/`path`/`polygon`/`text`/`marker`, siyah çizgi, `viewBox`
  zorunlu, sabit `width`/`height` yasak, `font-size="12"`, `font-family="sans-serif"`.
  Haritada iki durumu yan yana koy ve `BEFORE (1985)` / `AFTER (2020)` diye başlıklandır
- `mixed` için iki ayrı `visual` nesnesi listesi (`visuals`) kullan

## Şema — `content/writing/academic-task1/AT01.json`

```json
{
  "schema_version": "1.0",
  "set_id": "AT01",
  "skill": "writing",
  "module": "academic",
  "task": 1,
  "generated_by": "opus",
  "prompt": "The chart below shows household water use per person in three cities between 2000 and 2020.\n\nSummarise the information by selecting and reporting the main features, and make comparisons where relevant.",
  "instruction_line": "You should spend about 20 minutes on this task. Write at least 150 words.",
  "min_words": 150,
  "minutes": 20,
  "visual": { },
  "visuals": null,
  "key_points": [
    "Riverton'da kullanım istikrarlı düşüyor (210 → 140)",
    "Kelford'da tersine artıyor ve 2020'de en yükseğe çıkıyor",
    "İki şehrin eğrisi 2007 civarında kesişiyor",
    "Üç şehir arasındaki fark 2020'de 2000'e göre daralıyor"
  ],
  "common_mistakes": [
    "Görüş bildirmek ('cities should reduce…') — bu görevde yasak",
    "Her veri noktasını tek tek listelemek, ana eğilimi vermemek",
    "Karşılaştırma yapmamak"
  ],
  "topic": "su tüketimi",
  "difficulty": "medium"
}
```

`key_points`: uygulamadaki değerlendirme motoru bunu kullanarak "görev karşılama"
puanını verecek — bu yüzden **eksiksiz ve doğru** olmalı. Görselden gerçekten çıkan
4–6 ana bulguyu yaz.

---

# D. Yazma — General 1. görev (mektup) — `content/writing/general-task1/`

20 görev. En az 150 kelime, 20 dakika.

## Ton dağılımı (20 görev)

| Ton | Adet | Örnek durum |
|---|---|---|
| Resmi (formal) | 7 | Bir kuruma şikâyet, iş başvurusu, resmî talep |
| Yarı resmi (semi-formal) | 7 | Ev sahibi, kurs öğretmeni, komşu, iş arkadaşı |
| Samimi (informal) | 6 | Arkadaş, akraba |

## Kurallar

- Durum 2–3 cümlede anlatılır, ardından **tam 3 madde** gelir (`You should say…` değil,
  Task 1 mektupta madde işaretli üç istek)
- Resmi mektuplarda alıcı isimsiz (`Dear Sir or Madam`), yarı resmide isimli
  (`Dear Ms Aldridge`), samimide ilk isim
- Durumlar günlük ve evrensel olsun: gecikmiş sipariş, taşınma, kurs iptali, kayıp eşya,
  ev tadilatı, iş yerinde vardiya değişimi, gönüllü başvurusu, komşuya rica
- **Adayın kişisel geçmişini varsaymayan** durumlar seç

## Şema — `content/writing/general-task1/GT01.json`

```json
{
  "schema_version": "1.0",
  "set_id": "GT01",
  "skill": "writing",
  "module": "general",
  "task": 1,
  "generated_by": "opus",
  "tone": "formal",
  "prompt": "You recently bought a piece of equipment from an online shop, but it arrived damaged.\n\nWrite a letter to the shop. In your letter:\n\n- explain what you bought and when\n- describe the damage\n- say what you would like the shop to do",
  "instruction_line": "You should spend about 20 minutes on this task. Write at least 150 words.",
  "salutation_hint": "Dear Sir or Madam,",
  "min_words": 150,
  "minutes": 20,
  "key_points": [
    "Ürün ve satın alma tarihi belirtilmeli",
    "Hasar somut olarak tarif edilmeli",
    "Net bir talep (iade / değişim / onarım) yazılmalı"
  ],
  "common_mistakes": [
    "Üç maddeden birini atlamak",
    "Resmi mektupta günlük dil kullanmak ('Hi there', kısaltmalar)",
    "Kapanış cümlesi ve imza kalıbını unutmak"
  ],
  "topic": "hasarlı sipariş",
  "difficulty": "easy"
}
```

---

# E. Yazma — 2. görev (deneme yazısı) — `content/writing/task2/`

60 konu. En az 250 kelime, 40 dakika. Academic ve General **aynı görev tipini** kullanır
(General'da dil biraz daha basit olabilir) — `module: "both"` yaz.

## Soru kalıbı dağılımı (60 konu)

| Kalıp | Adet | Kalıp cümlesi |
|---|---|---|
| Katılıyor musun (opinion) | 14 | `To what extent do you agree or disagree?` |
| Her iki görüş + kendi görüşün | 12 | `Discuss both these views and give your own opinion.` |
| Sorun–çözüm | 11 | `What problems does this cause and what measures could be taken?` |
| Avantaj–dezavantaj | 11 | `Do the advantages outweigh the disadvantages?` |
| İki soruluk (double question) | 12 | `Why is this happening? Is it a positive or a negative development?` |

## Konu alanları (60 konu boyunca dengeli dağıt, tekrar yok)

eğitim · iş hayatı · teknoloji · çevre · şehir hayatı · ulaşım · sağlık · medya ·
kültür ve gelenek · aile ve toplum · turizm · tüketim · devletin rolü · yaşlanan nüfus ·
dil ve iletişim · suç ve ceza

## Kurallar

- Konu cümlesi 1–2 cümle, sonra kalıp sorusu
- **Uzman bilgisi gerektirmesin** — herkes fikir üretebilmeli
- Ülkeye özgü politika/olay geçmesin
- Aşırı kutuplaştırıcı konu yok (idam, kürtaj, din, göçmen karşıtlığı, savaş)
- Her konu için 2 karşıt görüşün de **savunulabilir** olduğundan emin ol

## Şema — `content/writing/task2/T2-01.json`

```json
{
  "schema_version": "1.0",
  "set_id": "T2-01",
  "skill": "writing",
  "module": "both",
  "task": 2,
  "generated_by": "opus",
  "pattern": "opinion",
  "prompt": "Some people believe that companies should be required to let employees work from home whenever the job allows it.\n\nTo what extent do you agree or disagree?",
  "instruction_line": "You should spend about 40 minutes on this task. Write at least 250 words.",
  "min_words": 250,
  "minutes": 40,
  "topic_area": "iş hayatı",
  "key_points": [
    "Görev, açık bir tutum (katılıyorum / katılmıyorum / kısmen) bekliyor",
    "Zorunluluk boyutuna değinilmeli — sadece 'evden çalışma iyidir' yetmez",
    "En az iki gerekçe + örnek",
    "Karşı görüşe kısa bir kabul (concession) beklenir"
  ],
  "common_mistakes": [
    "Tutum belirtmeden iki tarafı listelemek",
    "'Zorunlu tutulmalı mı' sorusunu atlayıp genel evden çalışma yazmak",
    "250 kelimenin altında kalmak"
  ],
  "difficulty": "medium"
}
```

---

## Teslim öncesi kendi kontrol listen

- [ ] Bu paketin birim sayısı hedefle birebir aynı
- [ ] Her birim ayrı dosyada, kimlikler çakışmıyor
- [ ] `NOTLAR.md`'deki önceki konularla **hiçbir tekrar yok**
- [ ] Bu paketteki dağılım tabloları (kart türü / görsel türü / ton / kalıp) tutuyor
- [ ] Konuşma soruları tek cümle ve evet/hayırla kapanmıyor
- [ ] Kartlarda tam 3 madde + `and explain…` satırı var
- [ ] Academic 1. görevde veriler tutarlı (yüzdeler 100, toplamlar doğru) ve
      anlatılacak belirgin bir eğilim var
- [ ] SVG kullanılan görsellerde `viewBox` var, sabit renk/boyut yok
- [ ] `key_points` alanları gerçekten görselden/görevden çıkıyor
- [ ] Kültürel olarak nötr, ayrıcalık varsaymıyor
- [ ] Gerçek marka/kişi/kurum yok, "IELTS" geçmiyor
- [ ] JSON geçerli: `python3 -c "import json;json.load(open('DOSYA'))"`

---

## Bitirince

`NOTLAR.md` sonuna **kullandığın bütün konu başlıklarını listele** — sonraki oturumların
tekrardan kaçınması buna bağlı.

```
git add -A
git commit -m "konusma part1: 5 konu x 10 soru (50 soru)"
git pull --rebase
git push
```

**Kullanıcıya soru sorma.**
