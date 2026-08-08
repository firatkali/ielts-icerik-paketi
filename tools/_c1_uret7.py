# -*- coding: utf-8 -*-
"""Ornek cevap kutuphanesi - 7. grup: konusma Part 2 kartlari (C01, C04, C07, C10, C14).

Bu, prompt'un 7-10. calistirmalarinin ilki: konusma yarisinin ilk grubu. Kart secimi
kart turune gore yapildi - part2-3 havuzunda bes tur var (kisi, yer, nesne, olay,
soyut) ve bu gruba her turden bir kart alindi, havuzun bas tarafindaki ilk uygun
dosya secilerek. Boylece kutuphane daha ilk gruptan bes kart turunun de nasil
konusuldugunu gosteriyor.

Metin yazma tarafindaki gibi duz Python dizesi olarak duruyor; kelime sayisi JSON'a
elle yazilmiyor, uretimde sayiliyor. Konusmada ikinci bir turetilmis alan daha var:
`approx_duration_seconds`. Sure de elle yazilmiyor - band basina bir konusma hizi
(kelime/dakika) secilip metnin kelime sayisindan hesaplaniyor, cunku puanlama
talimati akiciligi bu orandan okuyor (`konusma.md`, "Speech rate" tablosu):
  band 5,0  -> 80 wpm   (talimatta "slow" araligi, 70-99)
  band 6,5  -> 105 wpm  ("moderate", 100-129)
  band 8,0  -> 127 wpm  ("moderate"in ust ucu; kart 90-120 saniye istiyor)
Sure her kartta 90-120 saniye penceresine dusmek zorunda (kartlarin
`speaking_seconds` degeri); script bunu kontrol ediyor. Bu ayni zamanda kelime
sayisini da baglar: band 5 metni uzarsa sure 120 saniyeyi asar ve uretim durur.

Uretilen dosya: content/ornek-cevaplar/speaking/<kart-kodu>.json
Kapsam: Part 2 tek kisilik konusma (kartin `part2` bolumu). Part 3 tartismasi bu
gruba dahil degil, gerekcesi KONTROL.md'de.
"""
import json
import os

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KART_KLASOR = os.path.join(KOK, "content", "speaking", "part2-3")
HEDEF = os.path.join(KOK, "content", "ornek-cevaplar", "speaking")

# Band -> konusma hizi (kelime/dakika). Gerekce dosya basindaki aciklamada.
HIZ = {5.0: 80, 6.5: 105, 8.0: 127}
# Part 2 kartlarinin izin verdigi konusma suresi (saniye).
SURE_ALT, SURE_UST = 90, 120
# Part 2 tek kisilik konusmada 80 kelimenin altina dusen cevap akicilikta
# max 5 capasina takiliyor (konusma.md). Band 5 ornegi bile bunun uzerinde olmali.
KELIME_ALT_SINIR = 80


def _say(metin):
    return len(metin.split())


def _sure(metin, band):
    """Kelime sayisi ve band hizindan konusma suresi (5 saniyeye yuvarli)."""
    saniye = _say(metin) / float(HIZ[band]) * 60.0
    return int(round(saniye / 5.0) * 5)


# ================================================================ C01
# kisi / A patient person - "Describe a person you know who is very patient."
C01_5 = """Okay, er, I want to talk about my aunt, she is the sister of my mother.
She is fifty years old and she work in a primary school.
I know her since I am a child, because she live in the same street with us.
Every weekend we go to her house and we eat together, all the family.
She is very patient in many situation, er, for example in her class.
When the children is very noisy she never shout, she only wait and she speak slow.
Also in my family, when we have a big problem, she stay calm and she listen everybody.
My father is not like this, he get angry very fast and after he is sorry.
I think the patience is useful because the people can trust her and they tell her everything.
Er, yes, this is my aunt, she is a very very patient person."""

C01_65 = """So I'd like to talk about my aunt Nesrin, who is my mother's younger sister, and honestly she's the most patient person that I know.
I've known her all my life, obviously, because we lived in the same neighbourhood when I was small, and I used to spend nearly every weekend in her flat.
She's a teacher in a primary school, so I think her job also taught her a lot of patience.
When the children in her class are making noise, she doesn't shout at all, she just waits, she waits until they become quiet, and after that she starts the lesson again with a very soft voice.
My mother says that she has a very big patience, even with people who really deserve to be shouted.
And in the family it's the same thing.
Last year my cousin had a big problem in his university and everybody was giving him advice at the same time, but my aunt only listened him, I think for two hours, and she didn't say anything.
I think this is useful because people trust her, and, er, they can tell her things that they cannot tell to other persons.
That's why I admire her a lot."""

C01_8 = """Right, so the person I've chosen is my aunt Nesrin, my mum's younger sister, and she's easily the most patient person in our family.
I've known her my whole life, obviously. We lived a couple of streets apart when I was growing up, so I was round at her place most weekends, and I suppose I've watched her deal with, well, a lot of situations that would have finished me off.
She teaches seven-year-olds, which I think would test anyone's patience, but she genuinely takes it all in her stride.
If the class is completely wild, she won't raise her voice, she'll just stand at the front and wait them out, and somehow that works far better than shouting ever does.
Where it really shows, though, is with my grandmother. She's got quite forgetful over the last few years and she'll ask the same question maybe ten times in an afternoon, and my aunt answers it every single time as if she's hearing it for the first time. I'd have lost my temper hours earlier, to be honest.
And why I think that patience is useful, well, it's that people end up telling her things.
There's a lot of people in our family who ring her when something's gone wrong, because she doesn't jump straight in with advice and she doesn't judge you. She just keeps a level head and lets you talk yourself round to it.
Which is rarer than you'd think, actually."""

# ================================================================ C04
# yer / A quiet place for thinking - "Describe a quiet place you go to when you want to think."
C04_5 = """Okay, the quiet place I want to talk about is a small park behind our building.
In this park there is many tree and a old fountain, and it don't have a playground, so the children don't come.
I go there maybe two time in a week, usually in the evening after the work.
Sometimes I go in the morning also.
When I am there I sit in a bench near the fountain and I drink my coffee.
I don't listen music, I only look the trees and the people who pass in the street.
Sometimes I write some thing in my phone about my plan for the next day.
This place help me to think because it is very quiet and nobody know me there.
In my house my brother always watch the television very loud and I cannot concentrate.
So, er, this is my quiet place and I like it very much."""

C04_65 = """The place I want to describe is a small park just behind our apartment building.
It's nothing special, honestly, only a few benches, some old trees and a fountain that doesn't work anymore, but there is no playground, so children don't really go there and it stays quiet.
I go there maybe twice in a week, usually in the evening when I finish work, and sometimes at the weekend if the weather is good. In winter I go less, of course.
What I do there is quite boring, actually. I take a coffee, I sit on the same bench near the fountain, and I watch the people who are passing.
Sometimes I make some notes in my phone about the things I have to do, but most of the time I only sit and I think.
I think this place helps me because at home it's impossible to have a silence.
My brother is always watching television very loudly and my mother is calling me every five minutes for something, so I cannot follow one idea until the end.
In the park nobody knows me and nobody wants nothing from me, so my head becomes more clear and I can decide what I will do."""

C04_8 = """The place that came to mind straight away is a little park tucked in behind our block of flats.
It's a stone's throw from my front door, which is half the appeal, and because there's no playground and no café, hardly anyone bothers with it. You get a couple of dog walkers first thing and that's about it.
I'd say I go two or three times a week, normally in the evening once I've finished work, and definitely more in the summer than in the winter, when it's freezing and pitch dark by five o'clock.
What I actually do there is not much, if I'm honest. I take a coffee, I sit on the same bench by the old fountain, and I let my mind wander for twenty minutes or so.
Now and then I'll jot something down on my phone if an idea seems worth keeping, but mostly I just sit there.
As for why it helps, at home I can never hear myself think. There's the television going, my brother on a call in the next room, my mother asking me to do something every ten minutes, and you can't follow a thought for more than about thirty seconds.
In the park nobody knows me and nobody wants anything from me, so whatever's been going round in my head all day finally settles, and I can usually work out what's really bothering me.
It's not much of a park, mind you. It's just the only quiet thing near me."""

# ================================================================ C07
# nesne / An item of clothing you wear often
C07_5 = """Er, I want to describe a cloth that I wear very often, it is a black jacket.
It is not new, my father buy it for me three years ago in a shop in the city centre.
It was for my birthday, I remember this day very well.
The jacket is black and it have four pocket and a hood, and it is very warm.
I wear it in the autumn and in the winter, almost every day.
When I go to the university or when I meet my friend I take this jacket.
I don't wear it in the summer because it is too much hot.
I wear it very often because it is comfortable and it go with all my trouser.
Also my father gave it to me, so it is important for me.
So this is my favourite cloth, er, I think I will use it two or three year more."""

C07_65 = """I'm going to talk about a black jacket that I wear all the time, probably too much.
My father bought it for me about three years ago for my birthday. We went together to a shop in the city centre and he said that I have to choose something warm, not something fashionable, and in the end he was right.
It's quite simple, black, with four pockets and a hood that you can remove. Nothing special, but the material is really strong, so after three years it still looks almost new, only the elbows are a little bit used.
I wear it from October until maybe April, nearly every day. When I go to the university, when I meet with friends, even when I only go to the market for ten minutes, I take this jacket. In summer, of course, it's impossible, it's too hot.
Why I wear it so often, first, it's very comfortable and it goes with everything, so I don't lose time in the morning to think what I will wear.
And second, it was a present from my father, so there is a sentimental value also. I think I will use it two or three years more, at least until it will break."""

C07_8 = """The thing I've picked is a black jacket that I wear far more than I probably should.
My dad bought it for me about three years ago as a birthday present. We went into town together and he insisted I choose something hard-wearing rather than something fashionable, and I remember being slightly annoyed about that at the time, but he was completely right, obviously.
It's a plain black jacket, four pockets, a hood you can zip off. Nothing about it stands out, but the material is tough as anything. Three years on, it's only just starting to look worn at the elbows.
I more or less live in it from October through to April. If I'm heading to a lecture, meeting friends, nipping out for milk, I reach for it without even thinking about it. It's only in the summer that it goes to the back of the wardrobe.
As for why, I suppose there are two reasons. The practical one is that it goes with absolutely everything, so on a cold morning I don't have to stand there weighing up what to wear, I just grab it and go.
The other reason is sentimental, really. My dad isn't a person who says a great deal, so when he does buy you something he's clearly thought about, it stays with you.
I'll probably keep wearing it until it falls apart, and then I'll be annoyed about that as well."""

# ================================================================ C10
# olay / Helping a stranger - "Describe a time when you helped someone you did not know."
C10_5 = """Okay, I want to talk about one time I help a person that I don't know.
It was last year, in the winter.
I was waiting my bus in the bus station near my house and it was very cold.
There was an old woman with two big bags.
She want to go to the hospital but she don't know which bus she must take.
She ask me and first I don't understand because she speak very fast.
After I look in my phone and I find the number of the bus for the hospital.
I carry her bags to the bus and I say to the driver the name of the hospital.
She was very happy and she said thank you many times.
After this I feel very good, all the day I am in a good mood.
It was only five minutes, but for her it was important."""

C10_65 = """I'd like to talk about a time when I helped an old lady at the bus station, it was maybe one year ago in winter.
I was going to my cousin's house and I was waiting for my bus, and it was really cold that evening, so everybody was standing close to the wall.
Then I noticed an old woman with two big bags. She was looking at the timetable and after that at the buses, and it was clear that she was lost.
She asked me something but at the beginning I didn't understand her, because she was speaking very fast and with a strong accent.
After a moment I understood that she needed to go to the state hospital and she didn't know which bus goes there.
So I looked on my phone, I found the number, and I said her to wait with me, because the bus was coming after seven minutes.
When it came I helped her with the bags and I explained to the driver where she wants to get off.
Honestly, it took me five minutes, nothing more. But she thanked me so much that I felt a little bit ashamed, and for all the day I was in a good mood."""

C10_8 = """This happened about a year ago, at the bus station near my flat, one of those freezing winter evenings where everyone's huddled up against the wall pretending they're not cold.
I was waiting for a bus over to my cousin's place and I noticed an elderly woman with two enormous shopping bags. She kept looking up at the timetable and then back at the buses, and she just looked a bit lost, so I asked her if she was all right.
It took me a minute to work out what she needed, to be honest. She was speaking very quickly and she had quite a strong regional accent. But eventually I got that she was trying to reach the state hospital and she had no idea which bus went there. Nobody else had stopped, by the way, although half the queue must have heard her.
So I looked it up on my phone, found out it was the number twelve, and told her to wait with me.
When it turned up I gave her a hand with the bags and had a quick word with the driver so he'd tell her when to get off.
It can't have taken more than five minutes, but she was so grateful that I felt slightly embarrassed, actually.
And I'll admit it put me in a good mood for the rest of the evening, which probably says more about me than it does about her."""

# ================================================================ C14
# soyut / A habit you would like to change
C14_5 = """Er, the habit I want to change is my phone, I look my phone too much in the night.
Every night I go to the bed at eleven o'clock, but after I take my phone and I watch videos.
Sometimes I sleep at two o'clock in the morning.
I have this habit since two year, I think it start after the pandemic.
Before I read a book in the night but now I don't read.
In the morning I am very tired and I don't want to wake up.
In the class I cannot listen the teacher and I forget many thing.
Also my eyes is hurt in the afternoon.
It is difficult because the phone is always near my bed, and I say one video only but after it become five video.
I try to put the phone in the other room but after three days I forget.
Yes, this is my bad habit."""

C14_65 = """The habit I would really like to change is looking at my phone before I sleep. It sounds like a small thing, but for me it's become a serious problem.
Every night I go to bed around eleven, and then I take my phone to check the notifications for two minutes.
And after that I start watching short videos, and when I look at the clock again it's one o'clock or half past one in the morning.
I have this habit since more or less two years, I think it started in the pandemic period when we were all closed at home. Before that I used to read a book in the evening and I slept much better.
The effect on my day is bad. In the morning I'm exhausted, I need two coffees before I can speak with anybody, and in my classes I lose the concentration after twenty minutes.
And why is it difficult? Because the phone is next to my bed and it's the last thing that I see. And honestly these applications are made for you cannot stop, this is their job.
I tried to leave the phone in the kitchen, but after three or four days I forgot, and everything came back like before."""

C14_8 = """The habit I'd change, without a doubt, is scrolling on my phone in bed. It sounds trivial when you say it out loud, but it's got completely out of hand.
The pattern is always the same. I get into bed at about eleven, I pick up my phone just to check my messages, two minutes, that's the plan, and then one video leads into another and suddenly it's half one in the morning and I couldn't tell you a single thing I've watched.
I've been doing it for a good two years now. It crept up on me during the lockdowns, when there wasn't a lot else to do, and it never really went away. Before that I used to read for half an hour and I slept like a log.
The knock-on effect is what actually bothers me. I'm shattered in the mornings, I'm useless before my second coffee, and by the middle of a lecture I've lost the thread completely. It's not that the material is harder, I mean, it's not the material at all, I'm just running on four hours' sleep.
And as for why it's so hard to break, partly the phone is right there on the pillow, and partly these apps are designed by very clever people whose whole job is making sure you don't stop.
I did try leaving it in the kitchen overnight, and it worked brilliantly, for about four days."""


# ---------------------------------------------------------------- gerekceler
# `why_this_band` konusmada uc olcut (konusma.md: Fluency and Coherence ·
# Lexical Resource · Grammatical Range and Accuracy). Yazma tarafindaki gibi
# olcut basina en fazla iki cumle.
CEVAPLAR = {
    "C01": [
        (5.0, C01_5,
         {"fluency_coherence": "Konusma bastan sona suruyor ama tek kalipla ilerliyor: her cumle "
                               "'she ...' ile basliyor ve baglaclar and / because / also ile sinirli. "
                               "Kartin dort maddesine de deginiyor, ancak her birine iki cumle "
                               "dusuyor, ornekler acilmadan birakiliyor.",
          "lexical_resource": "Sozcuk secimi gunluk cekirdegin disina cikmiyor: patient, calm, "
                              "angry, problem tekrar tekrar geliyor ve 'very very patient' ile "
                              "vurgu yapiliyor. Sabri anlatan tek bir deyim ya da esdizim yok.",
          "grammatical_range_accuracy": "Cumlelerin cogunda ozne-yuklem uyumu ya da zaman hatasi "
                                        "var (she work, she live, the children is, he get angry, "
                                        "I know her since I am a child) ama anlam hicbir yerde "
                                        "kaybolmuyor. Yapilar neredeyse tamamen basit cumle; "
                                        "when ile kurulan iki yan cumle disinda karmasik yapi yok."},
         "Once kartin ucuncu maddesini gercek bir olayla acmak - sinifta ya da ailede yasanan tek "
         "bir sahneyi bastan sona anlatmak. Ardindan 'she work / she live' turu uyum hatalarini "
         "duzeltmek, cunku bunlar cevabin her cumlesine yayilmis durumda."),
        (6.5, C01_65,
         {"fluency_coherence": "Uzun konusuyor ve kartin dort maddesini de gelistiriyor, ama akis "
                               "yer yer takiliyor: 'she just waits, she waits until' gibi tekrarlar "
                               "ve 'and after that', 'and in the family it's the same thing' gibi "
                               "basit gecisler var. Kuzen ornegi guzel secilmis ama sonuca "
                               "baglanmadan birakiliyor.",
          "lexical_resource": "Konuyu rahatca anlatacak kadar sozcugu var (neighbourhood, advice, "
                              "soft voice, admire) fakat esdizim kaziyor: 'she has a very big "
                              "patience', 'deserve to be shouted', 'other persons'. Deyim "
                              "kullanmiyor, anlatimi duz.",
          "grammatical_range_accuracy": "Iliski cumlesi, used to, gecmis surekli ve zaman yan "
                                        "cumleleri rahat kuruluyor ve cumlelerin cogu hatasiz. "
                                        "Kalan hatalar dar bir kumede: aktarimda zaman uyumu "
                                        "(he said that I have to), edat dusmesi (listened him, "
                                        "tell to other persons)."},
         "Kuzen hikayesini bir sonuca baglamak: teyzenin ne yaptigini degil, o iki saatin ne "
         "degistirdigini soylemek. Sozcuk tarafinda 'big patience' gibi birebir cevirileri "
         "birakip 'she never loses her patience' turu dogal esdizime gecmek."),
        (8.0, C01_8,
         {"fluency_coherence": "Kendi kendine akan bir anlatim: konuyu kendi sectigi sirayla "
                               "kuruyor ve 'Where it really shows, though, is with my grandmother' "
                               "gibi kendi isaretleyicileriyle donuyor. Bir yerde kendini duzeltiyor "
                               "('I've watched her deal with, well, a lot of situations'), bu 8 "
                               "satirinin izin verdigi seyrek duzeltme.",
          "lexical_resource": "Deyimsel malzeme bol ve dogru yerde: takes it all in her stride, "
                              "wait them out, raise her voice, lost my temper, keeps a level head, "
                              "jump straight in with advice, talk yourself round. Konusma diline "
                              "ait kayit tutarli (round at her place, to be honest).",
          "grammatical_range_accuracy": "Yapi cesitliligi genis: kosul cumlesi, iliski cumlesi, "
                                        "as if yapisi, would have + gecmis katilim. Hata seyrek ve "
                                        "konusmaya ozgu ('There's a lot of people' - konusmada "
                                        "sik gorulen uyum kaymasi), dinleyiciye hicbir sey "
                                        "kaybettirmiyor."},
         "Bu cevap hedefte; bir ust duzey icin buyukanne ornegindeki degerlendirmeyi biraz daha "
         "ileri goturup sabrin bedelini de anlatmak gerekir (teyzesine neye mal oluyor). "
         "Dilde yapacak bir sey kalmadi."),
    ],
    "C04": [
        (5.0, C04_5,
         {"fluency_coherence": "Kartin dort maddesini sirayla gecip birakiyor; her madde bir "
                               "cumle. Baglaclar and / because / so ile sinirli ve 'so, er, this "
                               "is my quiet place' ile aceleyle kapatiyor, yani konusma suresini "
                               "dolduramiyor.",
          "lexical_resource": "Yer anlatimi very quiet, small, old, cold gibi cekirdek sozcuklerle "
                              "yurutuluyor; park iki kez 'quiet', ev iki kez 'loud' ile "
                              "aciklaniyor. Kartin sundugu turden bir ifade (clear my head) hic "
                              "denenmemis.",
          "grammatical_range_accuracy": "Hatalar cumlelerin cogunda ve hep ayni turden: cogul "
                                        "dusmesi (two time, many tree), uyum (it don't have, "
                                        "nobody know), edat (sit in a bench, look the trees, "
                                        "listen music). Butun metin basit cumle; iki when yan "
                                        "cumlesi disinda karmasik yapi yok."},
         "'Why this place helps you to think' maddesini gercekten cevaplamak: sessizligin "
         "kafasinda ne yaptigini bir ornekle anlatmak. Sonra sit on / look at / listen to gibi "
         "fiil-edat esleslerini duzeltmek, cunku bunlar her cumlede tekrarlaniyor."),
        (6.5, C04_65,
         {"fluency_coherence": "Kartin dort maddesini de gelistiriyor ve 'What I do there is quite "
                               "boring, actually' gibi dogal bir doldurmayla devam ediyor. Buna "
                               "karsilik I sit / I take / I watch dizisi mekaniklesiyor ve son "
                               "boluma gecis 'I think this place helps me because' ile duz "
                               "kuruluyor.",
          "lexical_resource": "Yeri anlatacak kadar sozcugu var (benches, fountain, timetable "
                              "yerine passing people, exhausted degil ama 'impossible to have a "
                              "silence') ve anlam her yerde acik. Iki noktada esdizim kayiyor: "
                              "'to have a silence', 'my head becomes more clear'.",
          "grammatical_range_accuracy": "Iliski cumlesi, kosul cumlesi ve zaman yan cumlesi "
                                        "kuruluyor, cumlelerin ucte ikisi hatasiz. Kalan hatalar "
                                        "belirli: cift olumsuzluk (nobody wants nothing), "
                                        "'twice in a week', karsilastirma bicimi (more clear), "
                                        "gelecek zamanin yan cumlede kullanimi."},
         "Ev ile parkin karsilastirmasini tek cumlede toplamak yerine sesin dusuncelere ne "
         "yaptigini anlatmak - cevabin en zayif yeri kapanis. Dilde once 'nobody wants nothing' "
         "gibi cift olumsuzlugu duzeltmek."),
        (8.0, C04_8,
         {"fluency_coherence": "Anlatim kendi sirasini kuruyor ve maddeler arasinda gorunur bir "
                               "kalip yok; 'As for why it helps' ile donuyor, 'It's not much of a "
                               "park, mind you' ile de kendi anlattigina bir yorum ekliyor. "
                               "Doldurmalar (if I'm honest, now and then) akisi bozmuyor.",
          "lexical_resource": "Az rastlanan ogeler dogal yerde: a stone's throw from, hardly "
                              "anyone bothers with it, let my mind wander, jot something down, "
                              "hear myself think, going round in my head, pitch dark, half the "
                              "appeal. Kayit bastan sona konusma dili.",
          "grammatical_range_accuracy": "Genis yapi yelpazesi rahat kullaniliyor: 'once I've "
                                        "finished work', 'whatever's been going round in my head', "
                                        "kiyaslama, iliski cumleleri. Hata neredeyse yok; 'You get "
                                        "a couple of dog walkers first thing' gibi eksiltili "
                                        "konusma yapilari hata degil."},
         "Hedefte. Daha yukarisi icin son bolumdeki fikri biraz daha ileri goturmek gerekir - "
         "sessizligin neden dusunmeyi kolaylastirdigi hala sezgisel duzeyde kaliyor."),
    ],
    "C07": [
        (5.0, C07_5,
         {"fluency_coherence": "Konusma kesilmeden suruyor ama her cumle yeni bir bilgi ekleyip "
                               "duruyor; hicbir madde acilmiyor. Baglaclar and / because / also "
                               "ve iki when yan cumlesinden ibaret.",
          "lexical_resource": "Giysi icin 'cloth' secilmis ve tekrarlaniyor; geri kalan sozcukler "
                              "black, warm, comfortable, favourite ile sinirli. Kartin verdigi "
                              "turden bir ifade (hard-wearing, goes with everything) denenmiyor, "
                              "'it go with all my trouser' en yakin deneme.",
          "grammatical_range_accuracy": "Uyum ve zaman hatasi cumlelerin cogunda (my father buy "
                                        "it, it have four pocket, it go with, too much hot), "
                                        "cogul isaretleri dusuyor (pocket, trouser, year). Anlam "
                                        "her yerde anlasiliyor, ama yapi tamamen basit cumle."},
         "Dorduncu maddeyi - neden bu kadar sik giydigini - tek bir sabahi anlatarak acmak, "
         "boylece cevap liste olmaktan cikar. Sonra gecmis zamani duzeltmek: ceketin alindigi "
         "bolum bastan sona simdiki zamanda anlatilmis."),
        (6.5, C07_65,
         {"fluency_coherence": "Dort maddeyi de karsiliyor ve sebepleri 'first' / 'And second' "
                               "diye numaralayarak duzenli ilerliyor; bu duzen ayni zamanda biraz "
                               "mekanik. Alisveris sahnesi guzel gelistirilmis, kapanis ise tek "
                               "cumlede bitiyor.",
          "lexical_resource": "Giysiyi anlatacak sozcuk var (hood, material, elbows, fashionable, "
                              "sentimental value) ve 'it goes with everything' dogru "
                              "kullanilmis. Buna karsilik 'the elbows are a little bit used' ve "
                              "'I don't lose time' esdizim olarak kaciyor.",
          "grammatical_range_accuracy": "Iliski cumlesi, zaman yan cumlesi ve gecmis zaman "
                                        "kontrollu; cumlelerin cogu hatasiz. Kalan hatalar dar: "
                                        "aktarimda zaman uyumu (he said that I have to choose), "
                                        "zaman yan cumlesinde gelecek (until it will break)."},
         "Kapanisi genisletmek: babanin hediyesinin neden onemli oldugunu bir cumleyle "
         "gecistirmek yerine anlatmak. Dilde 'until it will break' gibi zaman yan cumlesindeki "
         "gelecek kullanimini duzeltmek."),
        (8.0, C07_8,
         {"fluency_coherence": "Konusma dogal bir sirayla ilerliyor ve 'As for why, I suppose "
                               "there are two reasons' ile kendi yapisini kuruyor; kapanistaki "
                               "sakayla da anlatim baglaniyor. Duraklama ve tekrar seyrek.",
          "lexical_resource": "Az rastlanan oge bol: hard-wearing, tough as anything, worn at the "
                              "elbows, live in it, nipping out, reach for it without thinking, "
                              "goes to the back of the wardrobe, weighing up, falls apart. "
                              "Kullanimlar dogru ve konusma diline uygun.",
          "grammatical_range_accuracy": "Yapi cesitliligi acik: kosul cumlesi, vurgu yapisi "
                                        "('It's only in the summer that ...'), iliski cumleleri, "
                                        "gecmis surekli. Hata seyrek ve dinleyiciyi hic "
                                        "durdurmuyor."},
         "Hedefte. Bir ust duzey icin ikinci sebebi - hediye olmasi - biraz daha ileri "
         "goturmek gerekir; su an tek cumleyle ozetlenip birakiliyor."),
    ],
    "C10": [
        (5.0, C10_5,
         {"fluency_coherence": "Olay bastan sona anlatiliyor ve sirasi takip edilebiliyor, ama "
                               "her adim tek cumle ve gecisler after / and ile yapiliyor. "
                               "Kartin son maddesi (sonrasinda nasil hissettigi) iki cumlede "
                               "kapatiliyor.",
          "lexical_resource": "Anlatim gunluk cekirdekle yurutuluyor: very cold, very happy, very "
                              "good, big bags. Yardim etmeyi anlatan tek ifade 'I carry her bags'; "
                              "kartin onerdigi turden bir esdizim yok.",
          "grammatical_range_accuracy": "Anlatim gecmiste basliyor ama cogu yerde simdiki zamana "
                                        "kayiyor (she want, she don't know, I look, I find, I "
                                        "carry, I feel), edat dusmeleri var (waiting my bus). "
                                        "Yapilar basit cumle; bir tane which yan cumlesi var."},
         "Butun anlatimi gecmis zamana cekmek - hikaye dogru kurulmus, onu bozan tek sey zaman "
         "kaymasi. Ardindan son maddeyi acmak: 'very good' yerine o gun ne dusundugunu soylemek."),
        (6.5, C10_65,
         {"fluency_coherence": "Olay sahne sahne gelisiyor (bekleme, fark etme, anlamama, cozum) "
                               "ve dinleyici hicbir yerde kaybolmuyor. Gecisler then / after that "
                               "/ so ile duzenli ama tekdüze; kapanista 'Honestly, it took me five "
                               "minutes' ile ton degistirmesi iyi.",
          "lexical_resource": "Sahneyi kuracak sozcugu var (timetable, strong accent, lost, "
                              "ashamed, in a good mood) ve anlam her yerde acik. Iki yerde secim "
                              "kayiyor: 'for all the day', 'the bus was coming after seven "
                              "minutes'.",
          "grammatical_range_accuracy": "Gecmis surekli, dolayli anlatim ve that yan cumleleri "
                                        "kontrollu; cumlelerin ucte ikisi hatasiz. Kalan hatalar "
                                        "belirli: fiil kalibi (I said her to wait), aktarimda "
                                        "zaman uyumu (where she wants to get off), edat (after "
                                        "seven minutes)."},
         "Kapanisi biraz daha ileri goturmek: utanma duygusunu acikladigi cumle cevabin en "
         "ilginc yeri ama tek cumlede kaliyor. Dilde 'said her' / 'told her' ayrimini duzeltmek."),
        (8.0, C10_8,
         {"fluency_coherence": "Anlati akici ve ayrintili; sahne tek cumleyle kuruluyor "
                               "('everyone's huddled up against the wall pretending they're not "
                               "cold') ve 'Nobody else had stopped, by the way' gibi ara notlarla "
                               "geliskin duruyor. Kapanis anlatiyi kendi uzerine dondurup "
                               "baglaniyor.",
          "lexical_resource": "Deyimsel oge cok ve yerinde: huddled up, looked a bit lost, work "
                              "out, had no idea, turned up, gave her a hand with, had a quick word "
                              "with, put me in a good mood, half the queue. Kayit bastan sona "
                              "konusma dili.",
          "grammatical_range_accuracy": "Genis yapi: gecmis mukemmel (Nobody else had stopped), "
                                        "cikarim yapisi (can't have taken), so + amac, dolayli "
                                        "anlatim. Hata seyrek; 'I got that she was trying to "
                                        "reach' konusmada dogal, dinleyiciye hicbir sey "
                                        "kaybettirmiyor."},
         "Hedefte. Daha yukarisi icin kimsenin durmamis olmasi gozlemini bir cumle daha "
         "isletmek gerekir; su an ilginc bir ayrinti olarak birakiliyor."),
    ],
    "C14": [
        (5.0, C14_5,
         {"fluency_coherence": "Konusma suruyor ve dort maddeye de deginiyor, ama her madde bir "
                               "cumleyle gecistiriliyor ve etkiler bolumunde ayni kalip (In the "
                               "morning / In the class / Also) tekrarlaniyor. Zorluk maddesi tek "
                               "uzun cumlede toplaniyor.",
          "lexical_resource": "Aliskanligi anlatan sozcuk yok denecek kadar az: habit, phone, "
                              "video, tired tekrarlaniyor. 'One video only, but after it become "
                              "five video' iyi bir deneme ama dogru bicime oturmuyor.",
          "grammatical_range_accuracy": "Zaman ve uyum hatasi cumlelerin cogunda (I look my "
                                        "phone, I have this habit since two year, it start, my "
                                        "eyes is hurt), cogul isaretleri dusuyor (two year, many "
                                        "thing, five video). "
                                        "Yapilar basit; because ile kurulan iki yan cumle disinda "
                                        "karmasik yapi yok."},
         "Etkiler bolumunu bir gunun icinden anlatmak - hangi derste ne oldugunu soylemek - "
         "cunku su an uc ayri cumlede uc ayri sonuc siralaniyor. Sonra 'since two year' yapisini "
         "duzeltmek: sureyi anlatan butun cumleler ayni hatayi tasiyor."),
        (6.5, C14_65,
         {"fluency_coherence": "Dort maddeyi de gelistiriyor ve 'And why is it difficult?' gibi "
                               "kendi sorusuyla bolum aciyor, bu akisi tasiyor. Buna karsilik "
                               "etkiler bolumu liste haline geliyor ve baglantilar and / because "
                               "/ also ile tekrarlaniyor.",
          "lexical_resource": "Konuyu tasiyacak sozcuk var (notifications, exhausted, headaches, "
                              "pandemic period) ve anlam hic kapanmiyor. Iki noktada kayiyor: "
                              "'I lose the concentration', 'we were all closed at home'.",
          "grammatical_range_accuracy": "used to, gecmis zaman, zaman yan cumlesi ve dolayli soru "
                                        "kuruluyor; cumlelerin cogu hatasiz. Kalan hatalar dar bir "
                                        "kumede: sure yapisi (I have this habit since two years), "
                                        "'made for you cannot stop' kurulusu, 'came back like "
                                        "before'."},
         "'These applications are made for you cannot stop' cumlesini duzgun kurmak - fikir "
         "cevabin en iyi fikri ama yapi cokuyor. Ayrica sure icin present perfect'e gecmek "
         "(I've had this habit for two years)."),
        (8.0, C14_8,
         {"fluency_coherence": "Anlatim rahat ve bolumler kendiliginden birbirine baglaniyor "
                               "('The pattern is always the same', 'The knock-on effect is what "
                               "actually bothers me'). Bir yerde kendini duzeltiyor ('it's not "
                               "that the material is harder, I mean, it's not the material at "
                               "all'), 8 satirinin izin verdigi turden seyrek bir duzeltme.",
          "lexical_resource": "Az rastlanan oge bol ve dogru: out of hand, crept up on me, slept "
                              "like a log, knock-on effect, shattered, lost the thread, running "
                              "on four hours' sleep, hard to break. Deyimler zorlanmadan "
                              "yerlesiyor.",
          "grammatical_range_accuracy": "Yapi genis: present perfect continuous (I've been doing "
                                        "it), iliski cumleleri (whose whole job is), 'It's not "
                                        "that ...' yapisi, edilgen. Hata seyrek ve dinleyiciyi "
                                        "durdurmuyor.",
          },
         "Hedefte. Bir ust duzey icin son bolumdeki 'tasarim' fikrini biraz daha ileri "
         "goturmek gerekir - su an bir cumlede birakiliyor ve saka ile kapaniyor."),
    ],
}


def main():
    if not os.path.isdir(HEDEF):
        os.makedirs(HEDEF)
    ozet = []
    for kod in sorted(CEVAPLAR):
        kart_yol = os.path.join(KART_KLASOR, kod + ".json")
        with open(kart_yol, encoding="utf-8") as fh:
            kart = json.load(fh)
        alt, ust = kart["part2"]["speaking_seconds"]
        assert (alt, ust) == (SURE_ALT, SURE_UST), kod

        cevaplar = []
        for band, metin, gerekce, yukselt in CEVAPLAR[kod]:
            kelime = _say(metin)
            saniye = _sure(metin, band)
            if kelime < KELIME_ALT_SINIR:
                raise SystemExit("%s / band %s: %d kelime, 80 alt sinirinin altinda"
                                 % (kod, band, kelime))
            if not (SURE_ALT <= saniye <= SURE_UST):
                raise SystemExit("%s / band %s: %d saniye, kartin %d-%d penceresi disinda"
                                 % (kod, band, saniye, SURE_ALT, SURE_UST))
            cevaplar.append({
                "band": band,
                "transcript": metin,
                "word_count": kelime,
                "approx_duration_seconds": saniye,
                "why_this_band": gerekce,
                "what_would_lift_it": yukselt,
            })
            ozet.append((kod, band, kelime, saniye,
                         int(round(kelime / float(saniye) * 60))))

        veri = {
            "exam": "ielts",
            "schema_version": "1.0",
            "kind": "model_answer_set",
            "skill": "speaking",
            "part": 2,
            "task_ref": kod,
            "answers": cevaplar,
        }
        yol = os.path.join(HEDEF, kod + ".json")
        with open(yol, "w", encoding="utf-8") as fh:
            json.dump(veri, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        print("yazildi: %s" % os.path.relpath(yol, KOK))

    print("\nkart  band  kelime  saniye  kelime/dk")
    for kod, band, kelime, saniye, wpm in ozet:
        print("%-5s %-5s %6d %7d %10d" % (kod, band, kelime, saniye, wpm))


if __name__ == "__main__":
    main()
