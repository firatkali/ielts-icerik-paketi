# -*- coding: utf-8 -*-
"""Ornek cevap kutuphanesi - 9. grup: konusma Part 2 kartlari (C16, C19, C22, C25, C29).

Prompt'un 7-10. calistirmalarinin ucuncusu. Kart secimi KONTROL.md'deki dort
calistirmalik dagilim tablosundan geliyor: 7. grup bes kart turunden birer tane
almisti (C01 kisi, C04 yer, C07 nesne, C10 olay, C14 soyut), 8. grup ayni bes turun
ikinci turunu (C02, C05, C08, C11, C15), bu grup ucuncu turunu aliyor - C16 kisi,
C19 yer, C22 nesne, C25 olay, C29 soyut.

Uretim mekanigi 7. ve 8. gruplarla ayni ve bilerek degistirilmedi: metin duz Python
dizesi olarak duruyor, kelime sayisi ve sure JSON'a elle yazilmiyor, burada
hesaplaniyor. Sure band basina bir konusma hizindan (kelime/dakika) turetiliyor,
cunku puanlama talimati akiciligi bu orandan okuyor (`konusma.md`, "Speech rate"):
  band 5,0  -> 80 wpm   (talimatta "slow" araligi, 70-99)
  band 6,5  -> 105 wpm  ("moderate", 100-129)
  band 8,0  -> 127 wpm  ("moderate"in ust ucu; kart 90-120 saniye istiyor)
Sure her kartta 90-120 saniye penceresine dusmek zorunda; script bunu kontrol
ediyor ve disari cikani reddediyor.

8. gruptan tasinan iki sayi (KONTROL.md, "9. gruba kalan"):
  - band 6,5 metinlerinde kelime tavani 210 (105 wpm x 2 dakika). Ilk yazimda iki
    metin bu tavani asmisti; burada tavan bastan gozetildi.
  - hatali cumle orani band 6,5'ta %30 hedeflenir (%40 sinirina yaklasilmaz),
    band 5'te %70 (%80 siniri GRA'yi 4'e, genel bandi 4,5'e dusuruyor).

Uretilen dosya: content/ornek-cevaplar/speaking/<kart-kodu>.json
Kapsam: Part 2 tek kisilik konusma (kartin `part2` bolumu). Part 3 tartismasi bu
gruba da dahil degil, gerekcesi KONTROL.md'de (7. grupla ayni).
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


# ================================================================ C16
# kisi / "Describe someone you know who is good at explaining things."
C16_5 = """Okay, so I want to talk about my cousin Emre, he is a mathematics teacher.
He is only five years older than me but he explain everything very good.
In the last year of the lycee I had a big problem with the mathematic.
My teacher explained one time and after that he pass to the next subject.
But my cousin, he sit with me in the kitchen table and he draw the problem in a paper.
He always start with a easy example from the daily life, for example the football.
After that he make the question more difficult, step by step, until I understand.
He never say to me that this question is easy, and this is very important.
I passed my exam in the end and now I use the same method with my little sister.
I find his way helpful because he is patient and he never makes me feel stupid."""

C16_65 = """So the person I'm going to talk about is my cousin Emre, who is a maths teacher.
He's only five years older than me, so when I was in my last year at high school he was already teaching.
At that time I was having serious problems with maths, especially with derivatives.
The problem was, my teacher at school explained the topic only once and then he passed directly to the next chapter.
My cousin was completely different, he used to sit with me at the kitchen table for two or three hours in the weekend.
The first thing he always did was to break the problem down into small pieces, and he never started from the formula.
For example, he explained the derivative with the speed of a car, and suddenly the whole subject was making sense for me.
Another thing, he never said me that a question is easy, because when somebody says this you feel even more stupid.
In the end I got a good result in the exam, and now I use the same method with my sister.
So the reason I find his way helpful is simple, he thinks about the person in front of him, not about himself."""

C16_8 = """So, someone who's good at explaining things. That would be my cousin Emre, who teaches maths at a state school about an hour outside the city.
He's only five years older than me, which meant that when I was in my final year and completely at sea with maths, he'd already been teaching for two years.
And I was struggling, genuinely. My teacher at school would go through a topic once, at a hundred miles an hour, and then move straight on whether anyone had followed it or not.
Emre took a completely different approach. He'd come round at the weekend, sit down at the kitchen table with me, and, well, not even open the textbook at first.
What he does is break the thing down into pieces small enough that you can't get them wrong, and he never starts with the formula.
Derivatives, for instance. He explained the whole thing through a car speeding up and slowing down, and it just clicked. Ten minutes, after months of getting nowhere.
The other thing, and this is the real skill, is that he never once told me a question was easy. Because the moment somebody says that, you feel like an idiot for not seeing it.
I scraped through that exam in the end, and these days I catch myself using his tricks on my little sister.
Why it works, I suppose, is that he explains it for whoever is sitting in front of him, not for himself."""

# ================================================================ C19
# yer / "Describe a place near your home that has changed in recent years."
C19_5 = """Er, okay, I want to describe the sea side road in my district, near my house.
Before, this place was not beautiful, there was only a big empty ground and some fisherman.
Also there was a small tea garden and my father go there with his friends.
In the winter nobody was going there because the wind is very strong.
Three years ago the municipality made a big project and they changed all the place.
Now there is a new walking road, a bicycle road and many cafe.
They put also grass and lamps, so in the evening this area is full of family.
My mother is very happy because before we go to the centre for a walk, now we go there.
But the tea in the new cafes is three times more expensive than before.
In my opinion the change is good for the young people, but the old men lost their place."""

C19_65 = """Okay, so the place I want to talk about is the seafront in my district, ten minutes walking from my house.
Before, honestly, it was not a nice area, just an empty piece of ground with a few fishermen and a lot of rubbish.
There was a small tea garden with plastic tables, and my father used to go there with his friends every evening.
But in the winter nobody was going, because the wind in that area is really strong and there was no shelter.
Then three years ago the municipality started a big project and they changed the whole area from top to bottom.
Now there is a proper walking path, a cycle lane, modern cafes and a playground for the children.
They also planted grass and put lights, so in the evening it is completely full of families.
My mother is very happy, because before we used to go to the city centre for a walk and now we go down there.
The only problem is the prices, a tea in the new cafes is three times more expensive than before.
So in general I think the change was for the better, but the old men who were sitting there for years lost their place."""

C19_8 = """Right, so the place I'd go for is the seafront in our district, about ten minutes' walk from the flat.
And it's changed beyond recognition, which is really why I've picked it.
When I was growing up it was basically wasteland. A strip of gravel, a few blokes fishing off the rocks, and a tea garden with those white plastic chairs that blow over the second there's any wind.
Which there always was, that's the thing. Nobody went near the place from October to April.
My dad was down there most summer evenings, though, with the same four friends, playing cards and putting the world to rest. Or, well, putting the world to rights, I should say.
Then about three years ago the council did the whole thing up. Proper promenade, cycle lane, decent lighting, a playground, and three or four cafes that wouldn't look out of place in the centre of town.
And now you can't move down there in the evening. It's packed with families.
So on balance, yes, it's been a change for the better. My mum's delighted, we used to trek into town just to go for a walk and now we're five minutes from it.
Although I'd say something went with it. A tea in one of those cafes costs three times what it did in the old place, so my dad and his friends don't really go any more, and nobody put that on the plans."""

# ================================================================ C22
# nesne / "Describe something you own that you have had for a long time."
C22_5 = """Okay, I want to talk about a backgammon, in Turkish we say tavla.
My grandfather gave me this game when I was ten years old.
He said me that his father buyed it in Istanbul, so it is very old.
It is made from wood and in the inside there is mother of pearl.
The box is broken in one corner because one day I dropped it in the stair.
When I was child I played with my grandfather every evening in the summer holiday.
He never let me to win and this made me angry, but after two years I started to win.
Now I am at the university and I bring the game to my flat for my friends.
I keep it because when I open the box I remember my grandfather and his village.
It is not expensive, but for me it has a big value and I will never give it."""

C22_65 = """So the object I want to talk about is a backgammon set, tavla we call it in Turkish, and I have it since I was ten.
My grandfather gave it to me in his village house, and he told me his own father bought it in Istanbul in the fifties.
It's made of dark wood, and on the inside there is a decoration with mother of pearl.
The box is damaged in one corner, because when I was eleven I dropped it on the stairs.
In the beginning we were playing every evening in the summer holidays, always on the balcony.
He never let me win, not even one game, and at that time I was hating this, but now I understand.
After two or three years I started to beat him sometimes, and I still remember his face.
These days I keep the set in my flat, and my friends come and we play maybe two times in a week.
The main reason I hold on to it is of course sentimental, because when I open the box I remember my grandfather immediately.
It has no big money value, it's just an old wooden box, but I would never sell it."""

C22_8 = """Right, so the thing I've had the longest is a backgammon set. Tavla, we call it. And it's older than I am by quite a long way.
My grandfather gave it to me when I was about ten, at his place in the village, and apparently his own father had bought it in Istanbul some time in the fifties, so it's been in the family for three generations now.
It's dark wood, with mother-of-pearl inlay on the inside, and one corner is properly bashed in because I dropped it down the stairs when I was eleven and then cried for about an hour.
He taught me on that board. Every evening of every summer, out on the balcony with the mosquitoes.
And he never let me win. Not once, not a single game, which I thought at the time was, well, borderline cruel, but the day I finally beat him fair and square meant considerably more because of it.
The set has lived in about four different flats with me since then. It's worn but still going, and my friends and I get it out most weekends.
As for why I've held on to it, it isn't worth anything, let's be honest. A knock-about wooden box with a dodgy corner and half the pieces chipped.
But I can't open it without hearing him counting under his breath, and you can't exactly buy that, can you. So it'll be going with me wherever I end up."""

# ================================================================ C25
# olay / "Describe an occasion when you learnt something from a mistake."
C25_5 = """Er, I want to talk about a mistake what I did in my first year in the university.
In our system every semester you must choose your lessons from the internet.
I readed the date in the announcement but I didn't wrote it anywhere, I trusted my memory.
That week I was very busy with a project and I forgot completely this thing.
When I opened the system in Monday morning the page was closed and my lessons was not saved.
I go immediately to the department and I asked to the secretary.
She said me that the system is same for everybody and she cannot do nothing.
So in that semester I taked a lesson about statistics that I really didn't want.
After this I bought a small calendar and now I write all the dates in it.
If the same thing happens today, I will check the deadline two or three times."""

C25_65 = """So the mistake I want to talk about happened in my first year at university, and honestly it was my fault.
In our system, at the beginning of every semester, you choose your courses online, and the system stays open for one week.
I read the date on the department website, but I didn't write it down, I just trusted my memory.
And that week I was extremely busy with a group project, we were staying in the library until midnight, so it went out of my mind.
When I opened the system on Monday morning, the page was already closed and none of my courses were saved.
I went to the department and I explained to the secretary the situation, but she said the rule is the same for everybody.
So in that semester I had to take a statistics course I didn't want, only because it had free places.
It was not a disaster, I passed it with a good mark, but I lost the elective that I was planning since one year.
After that I bought a small paper calendar, and now I write every deadline in it.
If the same situation happens now, I would put an alarm on my phone one week before."""

C25_8 = """Okay, so the mistake. This was my first year at university, and it was entirely self-inflicted.
The way it works is that at the start of each semester there's a one-week window to pick your courses online, and once it shuts, that's that.
I saw the date on the department website. I remember reading it. And then I didn't write it down, because obviously I'd remember, wouldn't I.
That week we were flat out on a group project, in the library till midnight most nights, and it went clean out of my head.
So I logged on on the Monday morning, all organised, and it had closed at midnight.
I went down to the department and made my case to the secretary, who was very nice about it and completely unmovable, which, fair enough, the rule's the same for everyone.
The upshot was a semester of statistics I had no interest in, purely because it was the only thing left.
It wasn't the end of the world. I did quite well in it, oddly enough. But I lost an elective I'd been looking forward to for the best part of a year.
What I'd do differently is embarrassingly simple. Write it down. I keep a paper diary now, and anything with a deadline goes in it the day I hear about it.
A lesson learnt the hard way, I suppose, and the annoying part is it cost me a semester to learn something my mother had been telling me for years."""

# ================================================================ C29
# soyut / "Describe a skill you would like to learn in the future."
C29_5 = """Okay, so the skill what I want to learn is the sign language.
I decided this last year when I was working in a cafe.
One day a customer came and he was deaf, and I couldn't communicate with him nothing.
He wrote his order in a paper and I felt very bad and a little bit shame.
In our city the municipality is opening a free course two times in a year.
I want to go to this course and after that to practise with a deaf person for improve.
I think for the basic level six months is enough if I study regular every week.
But for speaking freely about every subject, maybe two years, because it is not easy.
This skill interests me because I don't want to feel again like that day in the cafe.
Also I think it is a beautiful language, and not many people know it."""

C29_65 = """So the skill I would like to learn is sign language, and I have a concrete reason for this.
Last summer I was working as a waiter in a cafe, and one afternoon a customer came who was deaf.
I couldn't communicate with him at all, so he wrote his order on a napkin and I felt terrible.
It's a strange feeling, you are in front of a person and you cannot help him with the most simple thing.
In my city the municipality opens a free course twice a year, and a friend of mine already finished the first level.
So my plan is to start from scratch with this course and then practise with real people, because a classroom is never enough.
For the basic level, I think six months would be enough if I study regularly, maybe two evenings in a week.
But for a real conversation, honestly I think two years or more, because it is a complete language with its own grammar.
The first reason it interests me is that afternoon in the cafe, I don't want to feel like this again.
And secondly it is a beautiful language to watch, and in my country not many people can use it."""

C29_8 = """Right, so the skill I'd like to pick up is sign language. Turkish sign language, that is.
And it comes from one specific afternoon. I was waiting tables in a cafe a couple of summers ago, and a customer came in who turned out to be deaf.
I had absolutely nothing. Not a word. He ended up writing his order on a napkin, perfectly cheerfully, and I stood there feeling two inches tall.
That's the bit that stayed with me. Not that I couldn't do it, but that he'd clearly done that a thousand times before and had stopped expecting anything else.
Or, well, that's what it looked like to me anyway. I could be wrong about that.
As for how, the council runs a free course twice a year and a friend of mine has been through the first level, so there's an obvious way in.
But I'd want to get past the classroom quickly. From what she says, you can learn the signs on your own and still be hopeless the moment somebody signs back at normal speed.
Six months would probably get me through the basics. Holding my own in a proper conversation, though, two years at the very least, because it's a full language, grammar and all, not a code for Turkish.
And why it appeals, beyond that afternoon, is that it's the only language I'd learn where being fluent isn't the point. Being able to help one person on a bad day would be enough."""


CEVAPLAR = {
    "C16": [
        (5.0, C16_5,
         {"fluency_coherence": "Kartin uc maddesi de ve kapanis sorusu da siraya giriyor, konusma "
                               "kesilmiyor; ama her madde tek cumlede bitiyor ve gecisler 'After "
                               "that', 'for example', 'because' kalibinin disina cikmiyor. "
                               "Kuzenin nasil anlattigi bolumu uc cumleyle gecistiriliyor, tek bir "
                               "ders sahnesi acilmiyor.",
          "lexical_resource": "Anlatma isini tarif eden sozcuk gunluk cekirdekte: explain, "
                              "example, easy, difficult, patient tekrarlaniyor ve vurgu 'very "
                              "good', 'very important' ile yapiliyor. 'Step by step' tek basina "
                              "duruyor; kartin isteyecegi turden ikinci bir esdizim yok.",
          "grammatical_range_accuracy": "Uyum hatasi cumlelerin cogunda ve ayni bicimde "
                                        "tekrarlaniyor (he explain, he pass, he sit, he draw, he "
                                        "start, he make, he never say), yaninda tanimlik (a easy, "
                                        "the mathematic) ve edat (in the kitchen table, in a "
                                        "paper) hatalari var; anlam yine de hicbir yerde "
                                        "kapanmiyor. Yapilar basit, when ve because yan cumleleri "
                                        "disinda karmasik yapi yok."},
         "Tek bir konuyu kuzenin nasil anlattigini bastan sona gostermek - hangi soru, once ne "
         "dedi, sonra ne cizdi - cunku su an yontem 'easy example' ve 'step by step' basliklariyla "
         "ozetleniyor. Dilde once ucuncu tekil -s'yi duzeltmek, cunku cevabin her cumlesinde ayni "
         "hata donuyor."),
        (6.5, C16_65,
         {"fluency_coherence": "Uc maddeyi de gelistiriyor ve okuldaki ogretmenle kuzeni "
                               "karsilastirmasi anlatiyi tasiyor; turev ornegi somut ve yerinde. "
                               "Akis mekaniklesiyor: bolumler 'The problem was', 'The first "
                               "thing', 'Another thing', 'So the reason' ile ayni kalipta aciliyor "
                               "ve cumleler ayni uzunlukta ilerliyor.",
          "lexical_resource": "Konuyu tasiyacak sozcugu var (break the problem down into small "
                              "pieces, make sense, derivatives, a good result) ve anlam hicbir "
                              "yerde kapanmiyor. Ifade iki noktada duzlesiyor: 'making sense for "
                              "me', 'I got a good result in the exam'.",
          "grammatical_range_accuracy": "Iliski cumlesi, 'used to', gecmis surekli ve 'the first "
                                        "thing he did was' ile kurulan vurgulu yapi kontrollu; "
                                        "cumlelerin ucte ikisinden fazlasi hatasiz. Kalan hatalar "
                                        "dar bir kumede: edat (in the weekend, make sense for), "
                                        "fiil kalibi (he never said me)."},
         "Turev ornegini bir cumle daha isletmek: arabanin hizi fikri cevabin en iyi yeri ama tek "
         "cumlede birakiliyor. Dilde 'say something to somebody' kalibini ve 'at the weekend' "
         "edatini duzeltmek yeter, kalan yapi zaten saglam."),
        (8.0, C16_8,
         {"fluency_coherence": "Anlatim kendi sirasini kuruyor: okuldaki ogretmen bir karsit "
                               "olarak kuruluyor, sonra tek bir ornek (turev) uzerinden yontem "
                               "gosteriliyor ve kapanis yontemi tek cumleye topluyor. Bir yerde "
                               "kendini duzeltiyor ('and, well, not even open the textbook at "
                               "first'), 8 satirinin izin verdigi turden seyrek bir duraklama.",
          "lexical_resource": "Az rastlanan oge bol ve yerinde: completely at sea with, at a "
                              "hundred miles an hour, move straight on, come round, break the "
                              "thing down, it just clicked, months of getting nowhere, scraped "
                              "through, catch myself using his tricks. Kayit bastan sona konusma "
                              "dili.",
          "grammatical_range_accuracy": "Yapi genis: gecmis mukemmel surekli (he'd already been "
                                        "teaching), aliskanlik 'would' (would go through a topic "
                                        "once), 'whether anyone had followed it or not' ile "
                                        "dolayli soru, 'pieces small enough that you can't get "
                                        "them wrong' ile sonuc yapisi. Sayilabilir hata yok."},
         "Hedefte; bir ust duzey icin kapanistaki 'he explains it for whoever is sitting in front "
         "of him' yargisini ikinci bir kisiyle desteklemek gerekir - kardesine ayni yontemi "
         "uygularken ne degistigi. Dilde yapacak bir sey kalmadi."),
    ],
    "C19": [
        (5.0, C19_5,
         {"fluency_coherence": "Yer, eski hali, degisen sey ve degerlendirme sirayla veriliyor, "
                               "yani kartin dort maddesi de karsilaniyor, ama her madde bir "
                               "cumleyle kapaniyor. Gecisler 'Also', 'Now', 'But', 'In my "
                               "opinion' kalibinda ve yeni halin anlatimi bir esya listesine "
                               "donuyor.",
          "lexical_resource": "Yer tarifi en temel sozcuklerle yapiliyor: beautiful, big, empty, "
                              "new, modern, full tekrarlaniyor. 'Walking road' ve 'bicycle road' "
                              "fikri anlasiliyor ama dogru bicime oturmuyor (promenade / cycle "
                              "lane gelmiyor).",
          "grammatical_range_accuracy": "Cogul (some fisherman, many cafe, full of family), uyum "
                                        "(my father go), zaman kaymasi (nobody was going ... the "
                                        "wind is; before we go to the centre) ve niceleyici "
                                        "(changed all the place) hatalari cumlelerin cogunda; "
                                        "anlam yine de ayakta. Yapilar basit, because yan cumlesi "
                                        "disinda karmasik yapi yok."},
         "Degisimden once orasi nasil bir yerdi sorusunu tek bir sahneyle anlatmak - babasi ve "
         "arkadaslari cay bahcesinde ne yapiyordu - cunku su an eski hal iki cumlede "
         "ozetleniyor. Dilde once cogul ekini (fisherman / cafe / family) duzeltmek."),
        (6.5, C19_65,
         {"fluency_coherence": "Dort maddeyi de gelistiriyor ve eski hal ile yeni hal arasindaki "
                               "karsilastirma anlatiyi bastan sona tasiyor; kapanista iki tarafli "
                               "bir yargi veriliyor. Akis mekaniklesiyor: bolumler 'Before', "
                               "'Then three years ago', 'Now there is', 'The only problem' "
                               "ile ayni kalipta aciliyor.",
          "lexical_resource": "Yeri tarif edecek sozcugu var (from top to bottom, cycle lane, "
                              "promenade yerine walking path, for the better, shelter) ve anlam "
                              "hic kapanmiyor. Ifade iki noktada duzlesiyor: 'ten minutes walking "
                              "from my house', 'a big project'.",
          "grammatical_range_accuracy": "'Used to', gecmis surekli, iliski cumlesi ve varlik "
                                        "yapilari (there was / there is) kontrollu; cumlelerin "
                                        "ucte ikisinden fazlasi hatasiz. Kalan hatalar belirli ve "
                                        "sayilabilir: zaman kaymasi (nobody was going ... the wind "
                                        "is), sayilamayan adda tanimlik (a tea in the new cafes), "
                                        "gecmis mukemmel eksigi (the old men who were sitting "
                                        "there for years)."},
         "Kapanisi acmak: 'the old men lost their place' cevabin en guclu fikri ama son cumlede "
         "tek nefeste soyleniyor - babasinin simdi nereye gittigi soylenirse fikir yerine oturur. "
         "Dilde 'who had been sitting there for years' gecmis mukemmeline gecmek."),
        (8.0, C19_8,
         {"fluency_coherence": "Anlati kendi ritmini kuruyor: kisa cumlelerle eski halin resmi "
                               "veriliyor ('Which there always was, that's the thing') ve kapanis "
                               "olumlu yargiyi bozmadan bir bedel ekliyor. Bir yerde kendini "
                               "duzeltiyor ('putting the world to rest. Or, well, putting the "
                               "world to rights, I should say').",
          "lexical_resource": "Az rastlanan oge bol ve dogru yerlestirilmis: changed beyond "
                              "recognition, basically wasteland, blokes fishing off the rocks, "
                              "blow over, did the whole thing up, wouldn't look out of place, you "
                              "can't move, packed with families, on balance, for the better, trek "
                              "into town.",
          "grammatical_range_accuracy": "Yapi genis: 'that blow over the second there's any wind' "
                                        "ile zaman yan cumlesi, 'used to trek', 'costs three "
                                        "times what it did in the old place' ile karsilastirma, "
                                        "eksiltili yapilar (Proper promenade, cycle lane, decent "
                                        "lighting). Sayilabilir hata yok.",
          },
         "Hedefte; bir ust duzey icin 'nobody put that on the plans' yargisini bir ornekle "
         "kapatmak gerekir - babasi ve arkadaslarinin simdi nerede toplandigi. Dilde yapacak bir "
         "sey kalmadi."),
    ],
    "C22": [
        (5.0, C22_5,
         {"fluency_coherence": "Nesne, nasil alindigi, yillar icinde nasil kullanildigi ve neden "
                               "saklandigi sirayla geliyor ve konusma kesilmiyor, ama her madde "
                               "tek cumlede kaliyor. Gecisler 'Now', 'because', 'but' ile sinirli "
                               "ve son iki cumle ayni fikri iki kez soyluyor.",
          "lexical_resource": "Nesne tarifi en temel sozcuklerle yapiliyor: old, wood, broken, "
                              "expensive, big value. 'Mother of pearl' dogru bir oge ama tek "
                              "basina kaliyor; duygusal degeri anlatan bir kalip ('sentimental "
                              "value', 'hold on to') gelmiyor.",
          "grammatical_range_accuracy": "Tanimlik (a backgammon, when I was child), duzensiz fiil "
                                        "(buyed), fiil kalibi (said me, let me to win), edat ve "
                                        "cogul (in the inside, in the stair) hatalari cumlelerin "
                                        "cogunda; zaman bir yerde bugune kayiyor (I bring the game "
                                        "to my flat). Yapilar basit, when ve because yan cumleleri "
                                        "disinda karmasik yapi yok."},
         "Dedeyle oynanan aksamlardan birini sahne olarak anlatmak - ilk kazandigi oyun - cunku "
         "yillar icindeki kullanim su an iki cumlede ozetleniyor. Dilde once 'said me' ve 'let me "
         "to win' fiil kaliplarini duzeltmek."),
        (6.5, C22_65,
         {"fluency_coherence": "Dort maddeyi de gelistiriyor ve kutunun kirik kosesi, kaybedilen "
                               "oyunlar ve bugunku kullanim birbirine bagli duruyor; dinleyici "
                               "hicbir yerde kaybolmuyor. Akis mekaniklesiyor: bolumler 'In the "
                               "beginning', 'After two or three years', 'These days', 'The main "
                               "reason' ile ayni kalipta aciliyor.",
          "lexical_resource": "Konuyu tasiyacak sozcugu var (hold on to it, sentimental, mother of "
                              "pearl, damaged) ve anlam her yerde acik. Ifade iki noktada "
                              "duzlesiyor: 'it has no big money value', 'a decoration with mother "
                              "of pearl'.",
          "grammatical_range_accuracy": "Iliski cumlesi, dolayli anlatim, gecmis surekli ve "
                                        "kosullu 'I would never sell it' kontrollu; cumlelerin "
                                        "ucte ikisinden fazlasi hatasiz. Kalan hatalar dar bir "
                                        "kumede: sure yapisi (I have it since I was ten), durum "
                                        "fiilinin surekli hali (I was hating this), sikligin "
                                        "edati (two times in a week)."},
         "Dedeyi ilk yendigi gunu acmak: 'I still remember his face' iyi bir cumle ama ne oldugu "
         "soylenmiyor. Dilde 'I've had it since I was ten' present perfect'ine gecmek, cunku "
         "cevabin ilk cumlesinde duruyor."),
        (8.0, C22_8,
         {"fluency_coherence": "Anlatim rahat ve ayrintili; kirik kose, sivrisinekli balkon ve "
                               "dedenin kendi kendine sayisi anlatiyi tasiyor, kapanis nesnenin "
                               "degersizligiyle degerini karsi karsiya getiriyor. Bir yerde "
                               "kendini duzeltiyor ('which I thought at the time was, well, "
                               "borderline cruel').",
          "lexical_resource": "Az rastlanan oge bol ve yerinde: by quite a long way, properly "
                              "bashed in, mother-of-pearl inlay, fair and square, worn but still "
                              "going, get it out, held on to it, a knock-about wooden box, a dodgy "
                              "corner, counting under his breath.",
          "grammatical_range_accuracy": "Yapi genis: gecmis mukemmel (his own father had bought "
                                        "it), 'it's been in the family for three generations', "
                                        "'the day I finally beat him ... meant considerably more' "
                                        "ile ad obegi ozne, eksiltili yapilar (Not once, not a "
                                        "single game). Sayilabilir hata yok."},
         "Hedefte; bir ust duzey icin 'wherever I end up' fikrini bir cumle daha isletmek gerekir "
         "- takimi kime birakacagi. Dilde yapacak bir sey kalmadi."),
    ],
    "C25": [
        (5.0, C25_5,
         {"fluency_coherence": "Hatanin ne oldugu, ne zaman oldugu, ne yapildigi ve bugun ne "
                               "yapacagi sirayla veriliyor, ama her madde bir cumleyle kapaniyor. "
                               "Gecisler 'So', 'After this', 'If' kalibinda ve bolume ayrilan "
                               "cumle sayisi hicbir yerde artmiyor.",
          "lexical_resource": "Kayit ve son tarih konusunu anlatan sozcuk cok dar: date, system, "
                              "lesson, week tekrarlaniyor ve 'lesson' ders anlaminda kullaniliyor "
                              "(course gelmiyor). Hatayi anlatan bir kalip ('I got it wrong', 'put "
                              "it right') hic yok.",
          "grammatical_range_accuracy": "Duzensiz fiil (readed, taked), yardimci fiilden sonra "
                                        "bicim (didn't wrote), ilgi adili (a mistake what), zarf "
                                        "yerlesimi (forgot completely this thing), edat (in Monday "
                                        "morning, asked to the secretary), uyum (my lessons was) "
                                        "ve cift olumsuz (cannot do nothing) hatalari cumlelerin "
                                        "cogunda; anlam yine de ayakta.",
          },
         "Bolumdeki konusmayi acmak - sekretere ne dedi, o ne cevap verdi - cunku cevabin donum "
         "noktasi orasi ve iki cumlede bitiyor. Dilde once duzensiz fiilleri (read / took) ve "
         "'didn't wrote' bicimini duzeltmek."),
        (6.5, C25_65,
         {"fluency_coherence": "Dort maddeyi de gelistiriyor; kutuphanede gecen hafta, pazartesi "
                               "sabahi ve bolumdeki konusma ayri sahneler halinde duruyor ve "
                               "anlati bunlarin uzerinde ilerliyor. Akis mekaniklesiyor: "
                               "bolumler 'So', 'And that week', 'When I opened', 'After that' ile "
                               "ayni kalipta aciliyor.",
          "lexical_resource": "Konuyu tasiyacak sozcugu var (trusted my memory, elective, "
                              "deadline, free places) ve anlam hicbir yerde kapanmiyor. Iki "
                              "noktada secim kayiyor: 'it went out of my mind', 'I passed it with "
                              "a good mark'.",
          "grammatical_range_accuracy": "Iliski cumlesi, gecmis surekli, zorunluluk (I had to "
                                        "take) ve 'none of my courses were saved' kontrollu; "
                                        "cumlelerin ucte ikisinden fazlasi hatasiz. Kalan hatalar "
                                        "belirli: soz dizimi (I explained to the secretary the "
                                        "situation), sure yapisi (I was planning since one year), "
                                        "kosul cumlesinde zaman karisimi (If the same situation "
                                        "happens now, I would put)."},
         "Bugun ne yapardi bolumunu somutlastirmak: 'put an alarm on my phone' iyi ama tek cumlede "
         "kaliyor, oysa cevabin sonucu orasi. Dilde 'I had been planning for a year' ve kosul "
         "cumlesinin zamanini duzeltmek yeter."),
        (8.0, C25_8,
         {"fluency_coherence": "Anlati kendi ritmini kuruyor: kisa cumleler hatanin kacinilmazligi "
                               "duygusunu veriyor ('I saw the date on the department website. I "
                               "remember reading it.') ve kapanis dersi anneye baglayarak "
                               "anlatiyi kendi uzerine donduruyor. Bir yerde araya giriyor "
                               "('which, fair enough, the rule's the same for everyone').",
          "lexical_resource": "Az rastlanan oge bol ve dogru: entirely self-inflicted, once it "
                              "shuts that's that, flat out, went clean out of my head, made my "
                              "case, completely unmovable, the upshot was, the end of the world, "
                              "for the best part of a year, a lesson learnt the hard way.",
          "grammatical_range_accuracy": "Yapi genis: gecmis mukemmel (it had closed at midnight, "
                                        "I'd been looking forward to), 'because obviously I'd "
                                        "remember, wouldn't I' ile eklenti soru, 'What I'd do "
                                        "differently is' ile yarik cumle, eksiltili buyruk (Write "
                                        "it down). Sayilabilir hata yok."},
         "Hedefte; bir ust duzey icin kagit ajandanin gercekten ise yarayip yaramadigini bir "
         "ornekle soylemek gerekir; su an sistem anlatiliyor ama sonucu verilmiyor. Dilde yapacak "
         "bir sey kalmadi."),
    ],
    "C29": [
        (5.0, C29_5,
         {"fluency_coherence": "Beceri, nasil ogrenilecegi, ne kadar surecegi ve neden ilgi "
                               "cektigi sirayla veriliyor, yani kartin dort maddesi de "
                               "karsilaniyor, ama her madde tek cumlede bitiyor. Gecisler 'One "
                               "day', 'After that', 'Also' kalibinda ve kafedeki olay anlatinin "
                               "en guclu yeri oldugu halde iki cumlede kapaniyor.",
          "lexical_resource": "Sozcuk gunluk cekirdegin disina cikmiyor: learn, course, level, "
                              "easy, beautiful tekrarlaniyor ve duygu 'very bad' ile anlatiliyor. "
                              "'A little bit shame' dogru fikir ama dogru bicime oturmuyor "
                              "(ashamed gelmiyor).",
          "grammatical_range_accuracy": "Ilgi adili (the skill what), gereksiz tanimlik (the sign "
                                        "language), cift olumsuz (couldn't communicate with him "
                                        "nothing), edat (in a paper, two times in a year, for "
                                        "improve), uyum (six months is enough) ve belirtec bicimi "
                                        "(study regular) hatalari cumlelerin cogunda; anlam yine "
                                        "de ayakta. Yapilar basit, if ve when yan cumleleri "
                                        "disinda karmasik yapi yok.",
          },
         "Kafedeki ani acmak - musteri ne yapti, o ne yapti, sonra ne oldu - cunku cevabin butun "
         "gerekcesi orada ve iki cumlede geciliyor. Dilde once 'for improve' ve 'study regular' "
         "gibi bicim hatalarini duzeltmek."),
        (6.5, C29_65,
         {"fluency_coherence": "Dort maddeyi de gelistiriyor ve kafedeki olay hem giris hem kapanis "
                               "olarak kullanildigi icin cevap kendi cercevesini kuruyor. Akis "
                               "mekaniklesiyor: bolumler 'So my plan is', 'For the basic level', "
                               "'The first reason', 'And secondly' ile ayni kalipta aciliyor.",
          "lexical_resource": "Konuyu tasiyacak sozcugu var (start from scratch, a concrete "
                              "reason, a complete language with its own grammar) ve anlam hicbir "
                              "yerde kapanmiyor. Iki noktada ifade duzlesiyor: 'I felt terrible', "
                              "'a beautiful language to watch'.",
          "grammatical_range_accuracy": "Kosul cumlesi (if I study regularly), iliski cumlesi, "
                                        "genellestiren 'you' kullanimi ve 'would be enough' "
                                        "kontrollu; cumlelerin ucte ikisinden fazlasi hatasiz. "
                                        "Kalan hatalar dar bir kumede: ustunluk bicimi (the most "
                                        "simple thing), gecmis mukemmel eksigi (a friend of mine "
                                        "already finished), sikligin edati (two evenings in a "
                                        "week)."},
         "Sureyi neye dayandirdigini soylemek: alti ay ve iki yil rakamlari veriliyor ama "
         "arkadasinin deneyiminden geldigi belirtilmiyor. Dilde 'has already finished' present "
         "perfect'ine ve 'the simplest thing' bicimine gecmek."),
        (8.0, C29_8,
         {"fluency_coherence": "Anlatim tek bir ogleden sonradan cikip plana, sureye ve gerekceye "
                               "aciliyor; kapanis akiciligi degil tek bir kisiye yardim etmeyi "
                               "olcut yaparak anlatiyi kendi uzerine donduruyor. Bir yerde "
                               "kendini duzeltiyor ('Or, well, that's what it looked like to me "
                               "anyway. I could be wrong about that').",
          "lexical_resource": "Az rastlanan oge bol ve yerinde: pick up, waiting tables, feeling "
                              "two inches tall, stayed with me, an obvious way in, get past the "
                              "classroom, be hopeless the moment somebody signs back, holding my "
                              "own, at the very least, grammar and all.",
          "grammatical_range_accuracy": "Yapi genis: gecmis mukemmel (he'd clearly done that a "
                                        "thousand times before and had stopped expecting anything "
                                        "else), kosullu (I'd want to, would probably get me "
                                        "through), 'not a code for Turkish' ile eksiltili "
                                        "karsitlik, 'where being fluent isn't the point' ile "
                                        "iliski cumlesi. Sayilabilir hata yok."},
         "Hedefte; bir ust duzey icin kapanistaki 'help one person on a bad day' olcutunu bir "
         "adim daha goturmek gerekir - kimin icin, hangi durumda. Dilde yapacak bir sey kalmadi."),
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
