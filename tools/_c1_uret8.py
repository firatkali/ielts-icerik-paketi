# -*- coding: utf-8 -*-
"""Ornek cevap kutuphanesi - 8. grup: konusma Part 2 kartlari (C02, C05, C08, C11, C15).

Prompt'un 7-10. calistirmalarinin ikincisi. Kart secimi KONTROL.md'deki dort
calistirmalik dagilim tablosundan geliyor: 7. grup bes kart turunden birer tane
almisti (C01 kisi, C04 yer, C07 nesne, C10 olay, C14 soyut), bu grup ayni bes turun
ikinci turunu aliyor - C02 kisi, C05 yer, C08 nesne, C11 olay, C15 soyut.

Uretim mekanigi 7. grupla ayni: metin duz Python dizesi olarak duruyor, kelime
sayisi ve sure JSON'a elle yazilmiyor, burada hesaplaniyor. Sure band basina bir
konusma hizindan (kelime/dakika) turetiliyor, cunku puanlama talimati akiciligi bu
orandan okuyor (`konusma.md`, "Speech rate" tablosu):
  band 5,0  -> 80 wpm   (talimatta "slow" araligi, 70-99)
  band 6,5  -> 105 wpm  ("moderate", 100-129)
  band 8,0  -> 127 wpm  ("moderate"in ust ucu; kart 90-120 saniye istiyor)
Sure her kartta 90-120 saniye penceresine dusmek zorunda; script bunu kontrol
ediyor ve disari cikani reddediyor.

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


# ================================================================ C02
# kisi / "Describe an older person you enjoy listening to."
C02_5 = """Okay, so I want to talk about my grandfather, he is the father of my father.
He is eighty-two years old and he live alone in a small village.
We visit him in every summer holiday and we speak in the telephone every Sunday.
My mother calls him first and after that she gives the phone to me.
He always talks about the old times, when he was a young man in the army.
He tell me the same stories many times but I don't say nothing, I only listen.
For example, in his village before there was no electricity and the people go to the town with a horse.
Sometimes he talk about my grandmother also, she is died five years ago.
I enjoy to listen him because his life is very very different from my life.
In my opinion the young people can learn many thing from this stories."""

C02_65 = """So the person I'm going to talk about is my grandfather, my father's father, and he's, er, eighty-two now.
He lives alone in a small village in the Black Sea region, so we can only visit him in the summer, but we speak on the phone every Sunday evening.
Usually my mother calls him first and then she gives the phone to me, and we make a long conversation, maybe twenty minutes.
The thing he talks about the most is his memories from the past, especially the years of his military service.
He tells the same stories many times, I have to be honest, but somehow I don't get bored from them.
For example, he describes his village before the electricity came, when people were going to town by horse, and for me it's like another century.
Sometimes he talks about my grandmother also, she passed away five years ago, and in these moments he becomes quiet.
The reason I enjoy listening him is that his life was completely different from mine.
When I have a problem, he never gives me an advice directly, he just tells one story and I understand the point by myself.
I think this is very valuable, and, er, that's why I like our Sunday conversations."""

C02_8 = """So, the person I'd pick is my grandfather, my dad's father, who's eighty-two and still living on his own in a village up on the Black Sea coast.
We only get up there in the summer, but we ring him most Sunday evenings, and my mum always hands the phone over to me after about five minutes, so I've probably spoken to him more than anyone else in the family has.
He's absolutely full of stories, that's the thing.
Nine times out of ten it's his military service, or, well, the village the way it was before the road went in. No electricity, everyone going into town on horseback, which to me sounds like a completely different world.
And yes, I've heard most of them before, but he has this way of putting things that means you don't really mind. He'll drop in some tiny detail he's never mentioned, and suddenly the whole story lands differently.
He talks about my grandmother as well. She died about five years ago, and he goes very quiet afterwards, so I've learnt to let the silence sit there rather than filling it.
As for why I enjoy it, I think it's that it puts things in perspective.
If I'm panicking about my exams, he'll never tell me straight out what to do. He just tells me something that happened to him in 1962 and leaves me to work out the connection myself, which sounds a bit roundabout, but it works every time."""

# ================================================================ C05
# yer / "Describe a building in your area that you find interesting."
C05_5 = """Er, okay, I want to describe a old building in my neighbourhood, it is near the bus station.
It is maybe two hundred years old, but I am not sure exactly about the date.
The building is made from red brick and it have very tall windows.
In the top there is a big clock but the clock is not working since many years.
When I was child my grandfather said me that this building was a hospital before.
Now it is a library and also there is a small cafe in the ground floor.
Many student go there to study, especially in the exam period.
I go there sometimes with my friends because it is quiet and the chairs are comfortable.
I find this building interesting because it is very different from the new buildings around it.
All the other buildings is grey and modern, but this one have a character."""

C05_65 = """Okay, so I'd like to talk about a building in my neighbourhood, just next to the main bus station.
It's quite old, I think from the Ottoman period, but I'm not completely sure about the date.
It's made of red brick with very tall windows, and there is a big clock on the front which unfortunately doesn't work since many years.
The first time I saw it I was a child, and my grandfather told me that in the past it was used like a hospital.
Now it has been converted into a public library, and they also opened a small cafe on the ground floor.
A lot of students go there in the exam period because it's very quiet, and honestly the reading room is much nicer than the one in my university.
I go there myself maybe two times in a month, when I need to concentrate.
The reason I find it interesting is that it stands out from everything around it.
All the other buildings in that street are grey blocks from the eighties, so when you turn the corner and see this old red building, it makes a big difference in the view.
Also I like that they didn't destroy it, they gave it a new life instead of this."""

C05_8 = """Right, the building I've gone for is the old brick place right behind the main bus station. You can't really miss it, it's the only thing on that street that isn't a concrete block from the eighties.
It's Ottoman, apparently, although nobody seems to agree on the exact date. Red brick, tall arched windows, and this enormous clock on the front that's been stuck at twenty past four for as long as I can remember.
When I was little my grandfather told me it had been a hospital, and for years I half believed the place was haunted, to be honest.
It sat empty for ages and it was starting to look like, well, a bit of an eyesore, but about six years ago the council gutted it and turned it into a public library, with a little cafe on the ground floor.
Now it's packed, especially around exam time. You have to get there before nine or you won't get a seat anywhere near a plug.
And why I find it interesting, well, part of it is that contrast, the way it stands out a mile from everything around it.
But mostly it's that they didn't knock it down. It would have been far cheaper to, I imagine, and instead the place has been given a new lease of life, which round here doesn't happen anywhere near often enough."""

# ================================================================ C08
# nesne / "Describe a gift you gave to someone else."
C08_5 = """Okay, I will talk about a gift what I gave to my sister last year.
It was her birthday, she become twenty-five years old.
I thinked a lot about the present for two weeks because she is very difficult person.
At the end I buyed a camera, not a professional one, a small old style camera.
She likes to take photos of the street and the cats, she puts them in Instagram.
I chose this camera because her old one broke during our holiday in Antalya two years ago.
When she opened the box in the kitchen she was very very surprised and she screamed.
She hugged me and she said thank you many times, my mother also was crying.
After that day she take photos of everything, even the food in the table.
I am very happy because for her it was a really good surprise, and she uses it also today."""

C08_65 = """So the gift I want to talk about is a camera which I gave to my sister for her twenty-fifth birthday last year.
She is a person who is really difficult to buy something for, so I was thinking about it for maybe two weeks.
In the end I decided a camera, because her old one was broken during a holiday and after that she never replaced it.
It wasn't an expensive professional one, it was a small vintage camera, second hand actually, and I found it in a shop in the old bazaar.
She takes photos all the time, mostly of street cats and old doors, and she shares them in Instagram.
So I thought it was something that she would really use, not a present that stays in the cupboard for years.
When she opened it, first she didn't say nothing for two seconds, and after that she started to shout.
My mother was crying also, which was a little bit exaggerated in my opinion.
For one month she was taking photos of everything, even our dinner table, and my father was complaining about this.
So I can say that it went down well, and honestly it was a big relief for me."""

C08_8 = """Okay, so the gift I've chosen is a camera I bought my sister for her twenty-fifth, which was, what, about a year ago now.
She's notoriously impossible to buy for. She never wants anything, and if she does want something she's usually gone and bought it herself already, so I racked my brains for a good couple of weeks.
What I landed on was an old film camera, a second-hand one from a little shop in the bazaar. Nothing fancy, and definitely not the sort of thing she'd have picked out herself.
The reason I went for it was that she's always photographing things, street cats, old doors, that kind of thing, but she does it all on her phone, and she'd been going on for ages about how film looks different.
So it was a bit of a gamble, but at least it was something she'd actually use rather than something that ends up at the back of a cupboard.
And she loved it. She went completely silent for a second, which from her is saying something, and then she was straight out on the balcony taking pictures of the neighbour's washing.
It went down really well. She still uses it, which is the part I'm most pleased about, because most presents get put away after a fortnight and that's the last you see of them."""

# ================================================================ C11
# olay / "Describe an occasion when you had to wait a long time for something."
C11_5 = """Er, I want to tell about the day when I waited for my exam result.
It was the university entrance exam, in Turkey we call it YKS.
I made the exam in June but the results came only in the end of July.
So I waited more than one month, it was really a long time for me.
In this period I couldn't sleep good and I was thinking always about my score.
I tried to make some activities, for example I go to the gym with my cousin.
Also I watched many series in the night because my brain didn't stop.
My mother said me every day don't worry, but this is not helping so much.
Finally the day came and my father opened the page because I was too much nervous.
My score was good and after that I felt very light, like a big stone went from my back."""

C11_65 = """So I'm going to talk about the summer when I was waiting for my university exam results.
In Turkey we have one big entrance exam, everybody takes it on the same day in June, and the results are announced at the end of July.
So the waiting was more than one month, which honestly felt like a year, because this exam decides your university and everything.
During this time I couldn't sleep properly, and every morning the first thing on my mind was the same question.
I tried to keep myself busy, for example I was going to the gym with my cousin every day, but even there I couldn't concentrate on nothing.
I also watched a lot of series at night, just to make the time pass more quickly.
My mother was telling me every day not to worry, but this kind of sentences never help in that situation.
The night before the results I didn't sleep at all, I was refreshing the page since three o'clock in the morning.
In the end my father opened it because I was too nervous, and my score was better than I expected.
The feeling after that is difficult to explain, it was like somebody removed a big weight from my shoulders."""

C11_8 = """Right, so the wait I'll talk about is the one for my university entrance results, which is something more or less everyone here goes through.
You sit the exam in June, one exam, one day, and it pretty much decides where you spend the next four years, and then the results don't come out until the very end of July.
So that's five weeks of nothing. Five weeks in limbo, basically.
And it dragged on. I don't think I'd ever been so aware of how slowly a day can go.
I killed time in the obvious ways. I went to the gym with my cousin most mornings, I got through an absurd amount of television, and I reorganised my room twice, which tells you everything really.
My mum kept telling me not to worry, which, I mean, she had a point, but it's easier said than done when there's no end in sight.
The night before, I didn't sleep at all. I was refreshing the page from about three in the morning.
And then when it finally loaded I couldn't bring myself to look, so my dad did it for me, and the score was better than I'd hoped for.
Honestly, the relief was bigger than the happiness. It was a weight off my shoulders more than anything, and I slept about twelve hours straight afterwards.
Worth the wait, I suppose. I wouldn't want to live through that month again, though."""

# ================================================================ C15
# soyut / "Describe a piece of advice you were given that you still remember."
C15_5 = """Okay, so I want to talk about some advice from my chemistry teacher.
He said me study a little every day, don't wait the last week before the exam.
He told me this in the lycee, when I am sixteen years old.
In that time I was studying only in the night before the exam.
Sometimes I got good notes but sometimes I forgetted everything after two week.
After his advice I started to study one hour every day and it was more easy.
My results become better in one term, especially in the chemistry and the physics.
Now I am at the university and I use the same method for all my lessons.
For example I repeat my notes in the same evening, not after two weeks.
I think this is the best advice what somebody gave me, because it is simple and everybody can do it."""

C15_65 = """The advice I want to talk about is something my chemistry teacher told me when I was sixteen years old.
He said, don't study everything in the last week, study a little bit every day and repeat the subject before you forget it.
At that time I was a typical student who was doing all the work in the night before the exam, sometimes until four o'clock.
And the problem was, my marks were okay but after two weeks I couldn't remember nothing from the subject.
So I decided to take his advice on board, and I started to study one hour every evening, even when there was no exam.
It was not easy at the beginning, but after two or three weeks it became a habit.
My results in chemistry and physics got much better in one term, and I was much less stressed before the exams.
Now I am at the university and I am still using the same system, I repeat my lecture notes in the same evening.
Of course it is easier said than done, and sometimes I skip two or three days.
But this advice stayed with me for years, and I think it is the most useful sentence that somebody said me."""

C15_8 = """So the advice I keep coming back to came from my chemistry teacher, of all people, when I was about sixteen.
What he said was, don't study more, study sooner. Or, well, what he actually meant was go over something the same evening you learn it, before you've had a chance to forget it.
Which sounds obvious, I know. But at that age I was a classic crammer. I'd do nothing for a month and then pull two all-nighters before the exam.
And the marks weren't even that bad, which was sort of the problem, because it meant I had no real reason to change anything. It all went in one ear and out the other about a fortnight later.
For whatever reason that particular sentence stuck with me, though, and I did actually take it on board. An hour most evenings, exam or no exam.
By the end of that term my grades in chemistry and physics had gone up noticeably and, more to the point, I wasn't in a permanent state of panic.
It's stood me in good stead ever since. I'm at university now and I still go over my lecture notes the same day, even if it's only twenty minutes on the bus home.
It's easier said than done when you're shattered, obviously, and there are weeks where it slips completely. But it's probably the single most useful thing anyone's ever told me, and it took him about ten seconds to say it."""


CEVAPLAR = {
    "C02": [
        (5.0, C02_5,
         {"fluency_coherence": "Kartin dort maddesine de deginiyor ve konusma kesilmiyor, ama her "
                               "madde tek cumleyle gecistiriliyor ve baglantilar and / because / "
                               "also / for example kalibinin disina cikmiyor. Dede ne anlatiyor "
                               "bolumu iki cumleden sonra kapaniyor, ornek acilmadan birakiliyor.",
          "lexical_resource": "Sozcuk gunluk cekirdekte kaliyor: old times, stories, listen, "
                              "different tekrarlaniyor ve vurgu 'very very different' ile "
                              "yapiliyor. Yasli birini dinlemeyi anlatan tek bir esdizim ya da "
                              "deyim yok.",
          "grammatical_range_accuracy": "Cumlelerin coguna uyum, zaman ya da edat hatasi yayilmis "
                                        "(he live, he tell, he talk, the people go, in the "
                                        "telephone, she is died, many thing, this stories) ama "
                                        "anlam hicbir yerde kapanmiyor. Yapilar basit; when ve "
                                        "because ile kurulan iki yan cumle disinda karmasik yapi "
                                        "yok."},
         "Once dedenin anlattigi seylerden birini gercek bir sahne olarak acmak - hangi hikaye, "
         "nerede, ne oldu - cunku su an konular sadece basliklar halinde siralaniyor. Sonra "
         "'he live / he tell / he talk' turu uyum hatalarini duzeltmek, cunku her cumlede "
         "tekrarlaniyor."),
        (6.5, C02_65,
         {"fluency_coherence": "Dort maddeyi de gelistiriyor ve telefon sahnesi ile koy ornegi "
                               "arasindaki gecis dogal duruyor. Buna karsilik bolum acilislari "
                               "'Usually', 'For example', 'Sometimes', 'The reason' kalibinda "
                               "tekrarlaniyor ve anlati bir yerde durup liste haline geliyor.",
          "lexical_resource": "Konuyu tasiyacak sozcugu var (military service, passed away, "
                              "memories, valuable) ve anlam her yerde acik. Esdizim iki noktada "
                              "kayiyor: 'we make a long conversation', 'I don't get bored from "
                              "them'.",
          "grammatical_range_accuracy": "Iliski cumlesi, gecmis surekli, zaman yan cumlesi ve "
                                        "'the reason' ile kurulan ad cumlesi kontrollu; cumlelerin "
                                        "ucte ikisinden fazlasi hatasiz. Kalan hatalar dar bir "
                                        "kumede: edat dusmesi (enjoy listening him), sayilamayan "
                                        "adda tanimlik (an advice), 'get bored from'."},
         "Dedenin hikayelerinden birini bastan sona anlatmak: su an 'he always describes his "
         "village' deniyor ama tek bir hikayenin kendisi hic gelmiyor. Dilde 'listening him' ve "
         "'an advice' gibi tekil hatalari duzeltmek yeter, kalan yapi zaten saglam."),
        (8.0, C02_8,
         {"fluency_coherence": "Anlatim kendi sirasini kuruyor ve bolumler kendiliginden "
                               "baglaniyor ('He's absolutely full of stories, that's the thing', "
                               "'As for why I enjoy it'). Bir yerde kendini duzeltiyor ('or, "
                               "well, the village the way it was'), 8 satirinin izin verdigi "
                               "turden seyrek bir duzeltme.",
          "lexical_resource": "Az rastlanan oge bol ve yerinde: full of stories, nine times out "
                              "of ten, has this way of putting things, a completely different "
                              "world, on horseback, puts things in perspective, tell me straight "
                              "out, work out the connection, a bit roundabout. Kayit bastan sona "
                              "konusma dili.",
          "grammatical_range_accuracy": "Yapi cesitliligi genis: iliski cumleleri, present "
                                        "perfect (I've probably spoken to him more than anyone "
                                        "else in the family has), kosul cumlesi, 'leaves me to "
                                        "work out' kalibi. Sayilabilir hata yok, hatasizlik "
                                        "dinleyiciyi hicbir yerde durdurmuyor."},
         "Hedefte; bir ust duzey icin dedenin anlattiklarindan cikan dersin bugun neye "
         "dokundugunu tek bir somut ornekle kapatmak gerekir; su an 1962 gondermesi ornek "
         "verilmeden birakiliyor. Dilde yapacak bir sey kalmadi."),
    ],
    "C05": [
        (5.0, C05_5,
         {"fluency_coherence": "Binayi yer, gorunus, kullanim ve sebep sirasiyla anlatiyor, yani "
                               "kartin dort maddesi de karsilaniyor, ama her madde bir cumlede "
                               "bitiyor. Gecisler 'Now', 'Also', 'So' ile mekanik ve son iki "
                               "cumle ayni fikri tekrarliyor.",
          "lexical_resource": "Bina anlatimi en temel sozcuklerle yapiliyor: old, big, tall, "
                              "quiet, grey, modern. 'This one have a character' iyi bir deneme "
                              "ama tek basina kaliyor; mimariye ait baska bir oge yok.",
          "grammatical_range_accuracy": "Tanimlik, uyum ve edat hatasi cumlelerin cogunda (a old "
                                        "building, it have, In the top, since many years, I was "
                                        "child, said me, in the ground floor, Many student, "
                                        "buildings is). Yapilar basit; when ve because ile "
                                        "kurulan iki yan cumle disinda karmasik yapi yok.",
          },
         "Binanin nasil kutuphaneye donustugunu anlatmak - su an 'Now it is a library' tek "
         "cumlede geciliyor ve cevabin en ilginc kismi orada. Dilde once 'it have / buildings "
         "is' uyumunu, sonra 'since many years' sure yapisini duzeltmek."),
        (6.5, C05_65,
         {"fluency_coherence": "Dort maddeyi de gelistiriyor ve cocukluk hatirasi ile bugunku "
                               "kullanim arasinda gercek bir baglanti kuruyor. Akis yer yer "
                               "takiliyor: 'Now', 'Also', 'The reason' ile acilan bolumler ayni "
                               "uzunlukta ve kapanis cumlesi aceleye geliyor.",
          "lexical_resource": "Yeterli sozcukle binayi tarif ediyor (converted into, ground "
                              "floor, stands out from, reading room) ve anlam hic kapanmiyor. "
                              "Iki noktada esdizim kayiyor: 'it makes a big difference in the "
                              "view', 'they gave it a new life instead of this'.",
          "grammatical_range_accuracy": "Edilgen (has been converted), iliski cumlesi ve zaman "
                                        "yan cumlesi rahat kuruluyor, cumlelerin cogu hatasiz. "
                                        "Kalan hatalar belirli ve sayilabilir (3/10 cumle): sure "
                                        "yapisi (doesn't work since many years), edat secimi "
                                        "(used like a hospital), sikligin edati (two times in a "
                                        "month)."},
         "Kapanisi acmak: 'they gave it a new life' fikri cevabin en iyi fikri ama son cumlede "
         "tek nefeste soyleniyor. Dilde 'doesn't work since many years' yerine present perfect'e "
         "gecmek (hasn't worked for years)."),
        (8.0, C05_8,
         {"fluency_coherence": "Anlatim rahat ve ayrintili; saatin 'stuck at twenty past four' "
                               "ayrintisi ve dokuzdan once gitme uyarisi anlatiyi tasiyor, "
                               "kapanista ise fikir kendi uzerine donuyor. Bir yerde kendini "
                               "duzeltiyor ('it was starting to look like, well, a bit of an "
                               "eyesore').",
          "lexical_resource": "Deyimsel ve konuya ozgu oge cok: you can't really miss it, tall "
                              "arched windows, half believed, an eyesore, gutted it, packed, "
                              "stands out a mile, knock it down, a new lease of life. Kayit "
                              "bastan sona konusma dili.",
          "grammatical_range_accuracy": "Yapi genis: gecmis mukemmel (it had been a hospital), "
                                        "edilgen (has been given), 'would have been far cheaper "
                                        "to' ile eksiltili kosul, 'for as long as I can "
                                        "remember'. Sayilabilir hata yok."},
         "Hedefte; bir ust duzey icin son cumledeki 'round here doesn't happen often enough' "
         "yargisini bir ornekle desteklemek gerekir - yikilmis baska bir bina. Dilde yapacak bir "
         "sey kalmadi."),
    ],
    "C08": [
        (5.0, C08_5,
         {"fluency_coherence": "Hediye, kisi, sebep ve tepki sirasi duzgun ve konusma kesilmiyor, "
                               "ama tepki bolumu iki cumlede bitiyor. Baglantilar 'At the end', "
                               "'After that day', 'because' ile sinirli ve cumleler ayni "
                               "uzunlukta ilerliyor.",
          "lexical_resource": "Hediye secimini anlatan sozcuk yok denecek kadar az: present, "
                              "gift, camera, photos, surprised tekrarlaniyor. 'Old style camera' "
                              "dogru fikir ama dogru bicime oturmuyor (vintage / second hand "
                              "gelmiyor).",
          "grammatical_range_accuracy": "Duzensiz fiillerde bicim hatasi (thinked, buyed, she "
                                        "become), ilgi adili (a gift what), edat (in Instagram, "
                                        "in the table) ve uyum (she take) cumlelerin cogunda. "
                                        "Yapilar basit; when ve because yan cumleleri disinda "
                                        "karmasik yapi yok."},
         "Kiz kardesin tepkisini bir sahne olarak anlatmak - ne dedi, ne yapti - cunku su an "
         "'she screamed' ve 'she hugged me' ile geciliyor. Dilde once duzensiz fiilleri "
         "(thought / bought) duzeltmek, cunku ucu de anlatinin donum noktasinda."),
        (6.5, C08_65,
         {"fluency_coherence": "Dort maddeyi de gelistiriyor ve secim gerekcesi ile tepki "
                               "arasindaki bag kuruluyor. Akis mekaniklesiyor: bolumler 'So', "
                               "'In the end', 'When she opened it', 'So I can say' ile ayni "
                               "kalipta aciliyor ve anne ayrintisi anlatiyi bir cumle "
                               "yavaslatiyor.",
          "lexical_resource": "Hediye secimini anlatacak sozcugu var (second hand, vintage "
                              "camera, went down well, relief) ve anlam her yerde acik. Secim iki "
                              "noktada kayiyor: 'she shares them in Instagram', 'she would really "
                              "use' yerine daha dogal bir kalip gelmiyor.",
          "grammatical_range_accuracy": "Iliski cumlesi, gecmis surekli ve that yan cumleleri "
                                        "kontrollu, cumlelerin ucte ikisinden fazlasi hatasiz. "
                                        "Kalan hatalar dar bir kumede: fiil kalibi (I decided a "
                                        "camera), edat (in Instagram), cift olumsuz (she didn't "
                                        "say nothing)."},
         "Kamerayi neden bu kisiye sectigini bir cumle daha isletmek: 'difficult to buy for' "
         "iyi bir baslangic ama ornekle desteklenmiyor. Dilde 'decide on something' kalibini ve "
         "'didn't say anything' olumsuzlugunu duzeltmek."),
        (8.0, C08_8,
         {"fluency_coherence": "Anlatim akici ve tepki bolumu tek bir sahneye baglaniyor "
                               "(balkonda komsunun camasirini cekmesi). Bir yerde kendini "
                               "duzeltiyor ('which was, what, about a year ago now'), 8 satirinin "
                               "izin verdigi turden seyrek bir duraklama.",
          "lexical_resource": "Az rastlanan oge bol ve dogru yerlestirilmis: notoriously "
                              "impossible to buy for, racked my brains, what I landed on, nothing "
                              "fancy, going on for ages, a bit of a gamble, at the back of a "
                              "cupboard, went down really well, that's the last you see of them.",
          "grammatical_range_accuracy": "Yapi genis: gecmis mukemmel surekli (she'd been going "
                                        "on), 'if she does want something' ile vurgulu kosul, "
                                        "iliski cumleleri, 'she'd have picked out herself'. Hata "
                                        "seyrek; 'she's usually gone and bought it herself "
                                        "already' konusmada dogal, dinleyiciye hicbir sey "
                                        "kaybettirmiyor."},
         "Hedefte; bir ust duzey icin 'a bit of a gamble' fikrini kapanista geri cagirmak "
         "gerekir - riskin neden tuttugunu soylemek. Dilde yapacak bir sey kalmadi."),
    ],
    "C11": [
        (5.0, C11_5,
         {"fluency_coherence": "Bekleyisin ne oldugu, ne kadar surdugu ve bu surede ne yaptigi "
                               "sirayla geliyor, ama her madde tek cumlede kaliyor ve bekleme "
                               "bolumu uc etkinlik siralanarak gecistiriliyor. Gecisler 'So', "
                               "'Also', 'Finally' kalibinin disina cikmiyor.",
          "lexical_resource": "Duygu anlatimi en temel sozcuklerle yapiliyor: nervous, good, long "
                              "time, happy. Kapanistaki 'like a big stone went from my back' "
                              "birebir ceviri; fikir anlasiliyor ama Ingilizcede oturmuyor.",
          "grammatical_range_accuracy": "Fiil kalibi (tell about, made the exam, said me), edat "
                                        "(in the end of July, in the night), zarf yerlesimi "
                                        "(thinking always) ve olcu (too much nervous) hatalari "
                                        "cumlelerin cogunda. Yapilar basit; because ve when yan "
                                        "cumleleri disinda karmasik yapi yok."},
         "Sonucun aciklandigi ani acmak - kim ne yapti, ilk ne soylendi - cunku cevabin en guclu "
         "yeri orasi ve iki cumlede bitiyor. Dilde once 'made the exam' ve 'said me' gibi fiil "
         "kaliplarini duzeltmek."),
        (6.5, C11_65,
         {"fluency_coherence": "Bes haftalik bekleyisi bastan sona anlatiyor ve dinleyici hicbir "
                               "yerde kaybolmuyor; sonuc gecesi ayri bir sahne olarak kuruluyor. "
                               "Gecisler 'So', 'During this time', 'I also', 'In the end' "
                               "kalibinda tekduze ve etkinlikler listeye donuyor.",
          "lexical_resource": "Bekleyisi anlatacak sozcugu var (keep myself busy, make the time "
                              "pass, refreshing the page, stressed) ve anlam acik. Kapanistaki "
                              "'somebody removed a big weight from my shoulders' deyime yaklasip "
                              "tam oturmuyor.",
          "grammatical_range_accuracy": "Gecmis surekli, edilgen (the results are announced), "
                                        "zaman yan cumlesi ve dolayli anlatim kontrollu; "
                                        "cumlelerin cogu hatasiz. Kalan hatalar belirli: cift "
                                        "olumsuz (couldn't concentrate on nothing), 'this kind of "
                                        "sentences' uyumu, sure edati (since three o'clock)."},
         "Bekleme bolumunu tek bir gunun icinden anlatmak: su an spor salonu, diziler ve anne "
         "ayri ayri cumlelerde siralaniyor. Dilde 'since' yerine 'from' ve cift olumsuzu "
         "duzeltmek yeter."),
        (8.0, C11_8,
         {"fluency_coherence": "Anlati kendi ritmini kuruyor: kisa cumlelerle bekleyisin agirligi "
                               "veriliyor ('And it dragged on') ve kapanis anlatiyi kendi uzerine "
                               "donduruyor. Bir yerde kendini duzeltiyor ('which, I mean, she had "
                               "a point').",
          "lexical_resource": "Az rastlanan oge bol ve dogru: in limbo, it dragged on, killed "
                              "time, got through an absurd amount of, easier said than done, no "
                              "end in sight, couldn't bring myself to look, a weight off my "
                              "shoulders, worth the wait.",
          "grammatical_range_accuracy": "Yapi genis: gecmis mukemmel (I'd ever been, better than "
                                        "I'd hoped for), genellestiren 'you' kullanimi, iliski "
                                        "cumleleri, 'I wouldn't want to live through that month "
                                        "again' ile kosullu. Sayilabilir hata yok."},
         "Hedefte; bir ust duzey icin rahatlamanin mutluluktan buyuk olmasi gozlemini bir cumle "
         "daha isletmek gerekir; su an ilginc bir tespit olarak birakiliyor. Dilde yapacak bir "
         "sey kalmadi."),
    ],
    "C15": [
        (5.0, C15_5,
         {"fluency_coherence": "Ogut, kimden geldigi, ne zaman geldigi ve bugunku faydasi "
                               "sirayla veriliyor, yani kartin dort maddesi de karsilaniyor, ama "
                               "her madde bir cumleyle kapaniyor. Gecisler 'After his advice', "
                               "'Now', 'For example' kalibinda ve son iki cumle ayni fikri "
                               "tekrarliyor.",
          "lexical_resource": "Calisma aliskanligini anlatan sozcuk cok dar: study, exam, notes, "
                              "results tekrarlaniyor. Ogudun kendisi de karsilikli bir kaliba "
                              "oturmuyor; 'notes' Turkce 'not' anlaminda kullaniliyor.",
          "grammatical_range_accuracy": "Fiil kalibi (said me, wait the last week), duzensiz fiil "
                                        "(forgetted), zaman uyumu (when I am sixteen, results "
                                        "become better), karsilastirma (more easy) ve ilgi adili "
                                        "(the best advice what) hatalari cumlelerin cogunda. "
                                        "Yapilar basit, karmasik yapi yok."},
         "Ogudun ise yaradigi tek bir ani anlatmak - hangi sinav, ne degisti - cunku su an fayda "
         "'my results become better' ile ozetleniyor. Dilde once 'said me' ve 'forgetted' gibi "
         "temel bicimleri duzeltmek."),
        (6.5, C15_65,
         {"fluency_coherence": "Ogudu once aktariyor, sonra oncesi ve sonrasiyla karsilastiriyor; "
                               "bu yapi anlatiyi tasiyor ve dort madde de gelisiyor. Akis "
                               "mekaniklesiyor: bolumler 'At that time', 'So I decided', 'Now I "
                               "am' ile ayni kalipta aciliyor.",
          "lexical_resource": "Konuyu tasiyacak sozcugu var (take his advice on board, easier "
                              "said than done, became a habit, lecture notes) ve anlam hic "
                              "kapanmiyor. Ogudun aktariminda ifade duzlesiyor: 'repeat the "
                              "subject', 'study a little bit every day'.",
          "grammatical_range_accuracy": "Iliski cumlesi, gecmis surekli, dolayli anlatim ve zaman "
                                        "yan cumleleri kontrollu; cumlelerin ucte ikisinden "
                                        "fazlasi hatasiz. Kalan hatalar dar bir kumede: edat (in "
                                        "the night before), cift olumsuz (couldn't remember "
                                        "nothing), fiil kalibi (somebody said me).",
          },
         "Ogudun tuttugu ani somutlastirmak: 'my results got much better' yerine tek bir sinavi "
         "anlatmak. Dilde 'say something to somebody' kalibini ve cift olumsuzu duzeltmek yeter, "
         "kalan yapi zaten saglam."),
        (8.0, C15_8,
         {"fluency_coherence": "Anlatim kendi sirasini kuruyor ve ogudu once soyleyip sonra neden "
                               "ise yaradigini acmasi akisi tasiyor; kapanis ogudun kisaligina "
                               "donerek baglaniyor. Bir yerde kendini duzeltiyor ('Or, well, what "
                               "he actually meant was'), 8 satirinin izin verdigi turden bir "
                               "duzeltme.",
          "lexical_resource": "Az rastlanan oge bol ve yerinde: of all people, a classic crammer, "
                              "pull two all-nighters, in one ear and out the other, stuck with "
                              "me, take it on board, more to the point, stood me in good stead, "
                              "easier said than done, shattered.",
          "grammatical_range_accuracy": "Yapi genis: gecmis mukemmel (my grades had gone up), "
                                        "'before you've had a chance to forget it', 'even if it's "
                                        "only twenty minutes' ile odun cumlesi, eksiltili yapilar "
                                        "(An hour most evenings). Sayilabilir hata yok.",
          },
         "Hedefte; bir ust duzey icin ogudun tutmadigi haftalari da acmak gerekir - 'there are "
         "weeks where it slips' tek cumlede birakiliyor. Dilde yapacak bir sey kalmadi."),
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
