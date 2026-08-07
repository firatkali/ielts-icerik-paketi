# -*- coding: utf-8 -*-
"""Ornek cevap kutuphanesi - 6. grup: General Task 1 (GT06-GT08) + Task 2 (T2-50, T2-54).

KONTROL.md'deki alti calistirmalik dagilim tablosu bu gruba uc General Task 1
mektubu ve iki Task 2 gorevi veriyor; kutuphane bu grupla 30 goreve tamamlaniyor.

Mektup tarafinda GT01-GT05'ten sonraki uc gorev alindi ve ton bilerek ayrildi:
3. grupta dort resmi + bir yari resmi mektup vardi, burada iki yari resmi
(GT06 yoneticiye, GT07 komsuya) ve **ilk kez bir samimi mektup** (GT08 arkadasa)
var. Boylece kutuphanede uc tonun de ornegi bulunuyor.

Task 2 tarafinda 4. grubun olcutu korundu - adayin kendi gunluk hayatindan ornek
verebilecegi konu (5. grup bunun tersini, soyut ve kurumsal konuyu yapmisti).
Kullanilmis on iki gorevin kaliplarindan iki kez kalanlar problem_solution,
discuss_both_views ve advantages_disadvantages idi; ikisi secildi ve ikisi de
kutuphanede hic bulunmayan konu alanindan geliyor:
  T2-50 problem_solution / dil ve iletisim
  T2-54 advantages_disadvantages / suc ve ceza

Metinler burada duz Python dizesi olarak duruyor; kelime sayisi JSON'a elle
yazilmiyor, uretim sirasinda sayiliyor - metin duzeltilince sayac sessizce yanlis
kalmasin diye. Sayim kurali degerlendirme talimatiyla ayni: bosluga gore ayrilan
belirtec sayisi. Task 1'de alt sinir 150, Task 2'de 250.
"""
import json
import os

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEDEF = os.path.join(KOK, "content", "ornek-cevaplar", "writing")


def _say(metin):
    return len(metin.split())


# ================================================================ GT06
# yari resmi: yoneticiye, kurs icin calisma saati degisikligi

GT06_5 = """Dear Ms Farrow,

I am writing you about a course which I am accepted for it, and I want to ask a small change of my working hours.

Firstly, the course is about the accounting program that we use in our office. It start in the next month and it continue for three month. The lesson is in the Tuesday and the Thursday morning, from nine o'clock until half past eleven, in the college near the station. My place is already confirm by the college.

Secondly, please change my working hour in this two days. I must come to the office at twelve o'clock instead of eight o'clock, because the college is twenty minutes far from our building. In the other three days everything can stay same like now.

Thirdly, about my work, don't worry, I will do everything like before and nothing will be late.

I think this course is very useful also for the company, because after it I can prepare the monthly reports faster and with less mistake. I hope you accept my demand.

Thanks a lot,

Kerem Aydin"""

GT06_65 = """Dear Ms Farrow,

I am writing to ask for a change in my working hours for the next three months, because I have been accepted on a short training course.

The course is called Financial Reporting for Small Firms and it is given by the college near the station. It takes place on Tuesday and Thursday mornings, from nine until half past eleven, and it will start on 3 March and finish at the end of May. Unfortunately these hours are exactly the same with our normal starting time, so I cannot attend without your permission.

I would like to begin work at twelve o'clock on this two days and to stay until seven in the evening instead of four. On Monday, Wednesday and Friday my hours would not change at all, so I would still work the same number of hours in a week.

I have also thought about my daily tasks. The supplier invoices which I normally check in the morning can be done in the afternoon, and I have already spoken with Deniz, who is agree to answer the accounts line until I arrive. I will also read my messages before to leave the college.

I believe the course would help our team, because it covers the new reporting rules which we will have to follow them next year. I would be very grateful if you could consider my request.

Kind regards,

Kerem Aydin"""

GT06_8 = """Dear Ms Farrow,

I have been offered a place on a short training course starting next month, and as the sessions fall inside our working day, I would like to ask whether my hours could be adjusted while it runs.

The course, Financial Reporting for Small Firms, is run by the college on Station Road and consists of two morning sessions a week, on Tuesdays and Thursdays from nine until half past eleven. It begins on 3 March and ends in the last week of May, so the arrangement I am asking about would cover roughly twelve weeks.

On those two days I would like to start at half past twelve rather than eight, and to work through until seven in the evening. My hours on the other three days would stay exactly as they are, which means my weekly total would be unchanged and no overtime would be involved.

As for the work itself, the supplier invoices I usually check first thing can be dealt with in the afternoon without holding up the payment run, and Deniz has kindly agreed to cover the accounts line on those two mornings. I will look at my messages between sessions and deal with anything urgent before I leave the college.

The course covers the reporting rules that come into force next January, so I hope it would be of some use to the department as well. I would of course be happy to discuss it, or to look at a different arrangement if the one I have suggested is awkward for the rota.

Kind regards,

Kerem Aydin"""

GT06_NEDEN_5 = {
    "task_response": "Kurs ve istenen saat degisikligi somut sayilarla veriliyor, ama ucuncu madde tek bir dilek cumlesine iniyor: isin nasil yurutulecegine dair hicbir plan yok, yalnizca don't worry deniyor. Emir kipiyle yazilan please change ve Thanks a lot kapanisi yoneticiye yazilan yari resmi tonu bozuyor.",
    "coherence_cohesion": "Firstly / Secondly / Thirdly maddelerin uzerine mekanik olarak oturtulmus ve ucuncu paragraf tek cumlede bitiyor. Kurs-talep-is sirasi yine de mantikli, okuyucu neyin istendigini takip edebiliyor.",
    "lexical_resource": "Sozcuk gunluk ve tekrarli: course, work, hour donup duruyor, mektuba ait tek kalip I am writing. Demand istek yerine kullanilmis ve twenty minutes far, less mistake bicimleri okuru bir an durduruyor.",
    "grammatical_range_accuracy": "Cumlelerin neredeyse tamaminda hata var: writing you, which I am accepted for it, it start, for three month, in the Tuesday, is already confirm, in this two days, stay same like now. Yapilar basit cumle ve because ile eklenmis kisa gerekcelerden ibaret.",
}
GT06_LIFT_5 = "Ucuncu maddeyi gercekten yazmak: sabah bakilan islerin gun icinde nereye kayacagini ve kimin devralacagini somut olarak anlatmak. Please change yerine I would like to ask kalibina gecmek ve Thanks a lot yerine Kind regards kullanmak tonu de yerine oturtur."

GT06_NEDEN_65 = {
    "task_response": "Uc madde de karsilaniyor: kurs adiyla ve saatiyle tanitiliyor, degisiklik saat vererek isteniyor, isin nasil yurutulecegi iki somut cozumle anlatiliyor. Kursun sirkete faydasi tek cumlede kaliyor, talebi guclendirecek kadar acilmamis.",
    "coherence_cohesion": "Paragraf bolunmesi mantikli ve her paragraf tek bir maddeyi tasiyor. Baglantilar Unfortunately / I would like to begin / I have also thought gibi tanidik kaliplarin disina cikmiyor, ilk cumleyle son cumle arasindaki gecis biraz duz.",
    "lexical_resource": "I would be very grateful if you could consider my request, supplier invoices, attend, permission gibi mektuba ve isin alanina uygun ogeler var. The same with, who is agree gibi yerlerde esdizim tam oturmuyor.",
    "grammatical_range_accuracy": "Ilgi cumlecikleri ve kosullu kalip dogru kuruluyor, uzun cumleler dagilmiyor. Cumlelerin yaklasik yarisinda edat, uyum ya da isaret sifati hatasi var (the same with, on this two days, who is agree, before to leave, follow them next year); anlam hicbir yerde engellenmiyor.",
}
GT06_LIFT_65 = "Hatalarin cogu ayni yerde toplaniyor - edatlar ve isaret sifatlari. Mektubu gondermeden once yalnizca bunlara bakan bir okuma yapmak (on these two days, who has agreed, before leaving) dilbilgisini bir band yukari tasir."

GT06_NEDEN_8 = {
    "task_response": "Uc madde de tam: kurs adi, gunleri, tarih araligi ve suresi verilmis; degisiklik saatle istenmis ve haftalik toplamin degismedigi belirtilmis; isin yurutulmesi hem gorev hem kisi adiyla cozulmus. Kapanistaki alternatif arrangement onerisi karari yoneticide birakiyor.",
    "coherence_cohesion": "Bes paragraf mektubun mantigini tasiyor: talep, kurs, saatler, is, kapanis. As for the work itself gibi gecisler goze batmadan yon degistiriyor ve hicbir paragraf ikinci bir konuya kaymiyor.",
    "lexical_resource": "Mektup diline ve is baglamina uygun az kullanilan ogeler var: fall inside our working day, hold up the payment run, come into force, cover the accounts line, awkward for the rota. Bir iki yerde vurgu biraz agir kaliyor.",
    "grammatical_range_accuracy": "Kosullu yapi, ilgi cumlecigi ve edilgen bicim dogru ve dogal kullaniliyor; hatali cumle yok denecek kadar az. Ikinci paragrafin ilk cumlesi uc bilgiyi birden tasidigi icin biraz sikisik duruyor.",
}
GT06_LIFT_8 = "Ikinci paragrafin ilk cumlesini ikiye bolmek: kursun kim tarafindan verildigi ile gun ve saatler ayri cumlelere dusunce ritim rahatlar. Kursun departmana faydasi son paragrafta bir cumle daha acilirsa talep tam yerine oturur."


# ================================================================ GT07
# yari resmi: komsuya, cati tamiri ve gecis izni ricasi

GT07_5 = """Dear Mr Ellery,

I write you this letter for informing you about a work in my house, because it can be a little problem for you also.

Firstly, the roof of my house is very old and in the winter the water come inside from two place. So the workers will change all the tile and they will put a new isolation under it. The work start in 12 May and it take almost two week, every day from eight in the morning to five in the evening.

Secondly, there will be a noise of course, but it is only a normal noise of a work and I think you not hear it too much in the day time.

Thirdly, the workers must to use the path in the side of your house, because in my side there is no place for the ladder and the machine. They will pass with the materials from there in the morning and in the evening, this is the only solution for us.

I will be in the home in this period, so if there is a problem you can knock my door in any time.

Best wishes,

Selin Kaya"""

GT07_65 = """Dear Mr Ellery,

I am writing to let you know about some repair work on my roof next month, and to ask you a small favour.

The tiles above the back bedroom have been leaking from the storm in February, so that side of the roof has to be stripped and laid again. The builders will start on Monday 12 May and they expect to finish in about ten working days. They have promised me to not use the noisy machine before nine in the morning.

I am afraid the work will be unpleasant for you as well. There will be a lot of hammering in the first three days, and some dust will certainly come in your garden. The scaffolding will also take a part of the light from your kitchen window for two week.

My favour is about the path on the side of your house. The builders cannot reach the roof from my garden because of the old plum tree, so they need to carry the ladders through your path, perhaps four times in a day. There would be only two men and they have agreed to clean the path every evening.

Please tell me if this is not convenient and I will ask them to find another way. My phone number is on the back of this letter, so you can call me if the noise become a problem.

Kind regards,

Selin Kaya"""

GT07_8 = """Dear Mr Ellery,

I am writing to warn you about some work due to start on my roof next month, and to ask a favour of you at the same time.

The tiles above the back bedroom have been letting water in since the February storms, and the roofer says patching is no longer worth doing, so the rear slope will be stripped and relaid. The men are booked for Monday 12 May and reckon on ten working days, weather permitting. They will work from eight until five, with the noisier tools kept back until after nine.

I am sorry to say that you will hear a good deal of it. The first three days, when the old tiles come off, will be the worst, and there is bound to be dust in your garden. The scaffolding will stand against the gable and may take some of the light from your kitchen window, although it should be down again by the end of the fortnight.

The favour is this. The old plum tree makes it impossible to bring a ladder up my own side, so the roofer has asked whether his men might use the path along the side of your house. It would be two of them carrying materials, perhaps four times a day, and they have agreed to sweep the path each evening and make good any damage.

Do say if this would be a nuisance and I will ask them to find another way round. My number is on the back of this letter, in case the noise becomes too much.

Kind regards,

Selin Kaya"""

GT07_NEDEN_5 = {
    "task_response": "Yapilacak is ve tarihler somut veriliyor, gecis ricasi da yapiliyor; ama ikinci madde tek cumleye iniyor ve o cumle etkiyi anlatmak yerine kucumsuyor (only a normal noise, you not hear it too much). Ricanin must to use kalibiyla dogrudan istenmesi komsuya yazilan bir mektupta tonu bozuyor.",
    "coherence_cohesion": "Firstly / Secondly / Thirdly uc maddenin uzerine mekanik olarak oturtulmus, ikinci paragraf tek cumlede bitiyor. Is-etki-rica sirasi yine de mantikli ve okuyucu neyin istendigini kaybetmiyor.",
    "lexical_resource": "Sozcuk gunluk ve tekrarli: work, problem, noise donup duruyor, isolation yalitim yerine yanlis secilmis. Mektuba ait tek kalip I am sorry for this situation, ricayi yumusatan bir oge yok.",
    "grammatical_range_accuracy": "Neredeyse her cumlede hata var: I write you, for informing, the water come, from two place, all the tile, start in 12 May, it take, two week, you not hear, must to use, in the side, in the home, knock my door in any time. Yapilar basit cumle ve so / because ile eklenmis kisa gerekcelerden ibaret.",
}
GT07_LIFT_5 = "Ikinci maddeyi kucumsemeden yazmak: gurultunun hangi gunlerde en yuksek olacagini, tozu ve kapanan gecisi durustce anlatmak. Must to use yerine I would be very grateful if you could allow gibi bir rica kalibi kullanmak tonu da yerine oturtur."

GT07_NEDEN_65 = {
    "task_response": "Uc madde de karsilaniyor: is ve suresi tarihle veriliyor, komsuya etkisi gurultu, toz ve isik uzerinden ayri bir paragrafta anlatiliyor, rica kapsamiyla birlikte yapiliyor. Rica kabul edilirse ne kadar surecegi net ama isin bitiminde tam olarak neyin temizlenecegi biraz genel kaliyor.",
    "coherence_cohesion": "Paragraflar mantikli bolunmus ve her biri tek bir maddeyi tasiyor. Baglantilar I am afraid / My favour is about gibi tanidik kaliplarla saglaniyor, gecisler dogru ama duz.",
    "lexical_resource": "Stripped, scaffolding, hammering, convenient, favour gibi gorev icin dogru ogeler var ve rica nazikce kuruluyor. Laid again, take a part of the light gibi yerlerde esdizim tam oturmuyor.",
    "grammatical_range_accuracy": "Ilgi cumlecikleri, edilgen yapi ve kosullu kalip dogru kuruluyor, uzun cumleler dagilmiyor. Cumlelerin yaklasik yarisinda edat, cogul ya da uyum hatasi var (leaking from the storm, to not use, the noisy machine, come in your garden, for two week, through your path, in a day, the noise become); anlam hicbir yerde engellenmiyor.",
}
GT07_LIFT_65 = "Hatalarin cogu edatlarda ve tekil-cogulda toplaniyor; mektubu gondermeden once yalnizca bunlara bakan bir okuma (for two week, in a day, the noise become) dilbilgisini bir band yukari tasir."

GT07_NEDEN_8 = {
    "task_response": "Uc madde de tam ve dengeli: isin ne oldugu ve neden ertelenemeyecegi, komsuya etkisi gun gun, rica ise kac kisi, kac kez ve sonrasinda ne yapilacagiyla birlikte. Sorun cikarsa vazgecme teklifi ve telefon numarasi ricayi kabul edilebilir kiliyor.",
    "coherence_cohesion": "Bes paragraf mektubun mantigini tasiyor ve The favour is this gibi kisa bir cumle donusu isaret ediyor. Zaman ve mekan bilgisi okuyucunun ihtiyac duydugu sirada geliyor, hicbir paragraf ikinci bir konuya kaymiyor.",
    "lexical_resource": "Mektup diline uygun az kullanilan ogeler var: weather permitting, bound to be, make good anything they damage, a nuisance, a fortnight, the rear slope. Ikinci paragrafta teknik ayrinti bir an yogunlasiyor.",
    "grammatical_range_accuracy": "Zaman kiplerinin ve kosullu yapilarin kullanimi esnek ve dogru; hatali cumle yok denecek kadar az. Ucuncu paragrafin ikinci cumlesi uc bilgiyi birden tasidigi icin nefes almadan okunuyor.",
}
GT07_LIFT_8 = "Acilistaki warn sozcugu bir rica mektubu icin fazla sert; let you know ya da give you some warning daha uygun olur. Ucuncu paragrafin uzun cumlesini ikiye bolmek de ritmi rahatlatir."


# ================================================================ GT08
# samimi: arkadasa, baska bir kasabaya tasinma

GT08_5 = """Dear Nadia,

I am writing to inform you that I will move to another town in the next month, I hope this letter find you in a good health. The reason of my decision is my job, because my company is open a new office in Kestrel Bay and they offer me a better position there with more salary, and also my rent here is very expensive for me, every month I am paying almost the half of my money for this small flat. Kestrel Bay is a nice town near the sea, it is not so big like here but the people say it is very quiet and the life is more cheap. My new home is a flat in the second floor and it have two room and a small balcony. I am little bit sad because I leave my friends here, specially you, we know each other from ten years and we was going everywhere together. So you must come and stay with me sometime, my home is your home, we can talk all the night like before. Please write me an answer soon and tell me what is the news from you.

Yours faithfully,

Emre"""

GT08_65 = """Dear Nadia,

I hope you are well and that the new job is not keeping you too busy. I have some news for you: in the end of next month I am moving to Kestrel Bay.

The main reason is my work. My company is opening a small office there and they asked me to run it, and honestly I was also tired from this city. My rent has gone up twice in two year and I spend almost two hours in the traffic every day, so I said yes immediately.

You will like Kestrel Bay, I am sure. It is much smaller than here, maybe thirty thousands people, and it is built around a little harbour where the fishing boats still come in. There is a long beach on the north side and a market in the main square on Saturdays. My new flat is on the top floor of an old house two streets from the sea, it has a small balcony and from the corner you can see the water.

So please come and stay with me. The second bedroom is small but it has a proper bed, and I am free on the middle of July if these dates are good for you. We could walk to the lighthouse, eat too much fish and do nothing for a whole week.

Write to me soon and tell me how are you.

Love,

Emre"""

GT08_8 = """Dear Nadia,

I hope the new job is treating you kindly. I have been sitting on some news for a fortnight and cannot keep it any longer: next month I am packing up and moving to Kestrel Bay.

It came out of nowhere, really. The firm is opening a small office there and asked whether I would run it; once I had stopped panicking I realised I wanted to go. This city has been wearing me down anyway: the rent has gone up twice since I moved in, and I lose two hours of every day to traffic that never moves.

You would love the place. It is tiny compared with here, about thirty thousand people, built in a half circle around an old fishing harbour. There is a proper beach ten minutes north, a Saturday market that sells nothing you need, and four cafes, which everyone thinks is plenty. I have taken the top floor of a tall grey house two streets back from the water, and although the ceilings slope in a way that will catch you out, there is a balcony big enough for two chairs and a view of the harbour lights.

So come and stay. The spare room will be ready by the middle of July, and it would be lovely if you could give me a whole week rather than a weekend; I want to take you to the lighthouse and feed you too much fish. Tell me which dates suit you and I will keep them free.

Write soon and tell me everything you have been up to.

Love,

Emre"""

GT08_NEDEN_5 = {
    "task_response": "Tasinma sebebi ve yeni yer anlatiliyor, ama davet come and stay with me sometime ile belirsiz birakiliyor: ne zaman, ne kadar sure, birlikte ne yapilacagi yok. Arkadasa yazilan mektup I am writing to inform you ile aciliyor ve Yours faithfully ile kapaniyor; arasi samimi oldugu icin ton bastan sona degil, uclarda kayiyor.",
    "coherence_cohesion": "Mektup selamlama ile kapanis arasinda tek bir blok halinde yazilmis, hicbir paragraf bolunmesi yok. Sira yine de izlenebiliyor - haber, sebep, yeni kasaba, ev, davet - ve baglantilar calisiyor, bu yuzden okuyucu yolunu kaybetmiyor.",
    "lexical_resource": "Sozcuk gunluk ve tekrarli: nice, small, big donup duruyor, kasaba ve ev iki genel sifatla geciliyor. Samimi mektuba ait tek dogal kalip my home is your home; more cheap ve in a good health bicimleri okuru bir an durduruyor.",
    "grammatical_range_accuracy": "Neredeyse her cumlede hata var: this letter find you, the reason of my decision, my company is open, they offer me, in the second floor, it have two room, we know each other from ten years, we was going, what is the news. Cumleler virgullerle birbirine ekleniyor ve nokta yerine virgul kullanilan yerler cok.",
}
GT08_LIFT_5 = "Daveti somutlastirmak: hangi ay, kac gun ve orada birlikte ne yapilacagi. Mektubu uc dort paragrafa bolmek ve I am writing to inform you / Yours faithfully kaliplarini arkadasa uygun bir acilis ve kapanisla degistirmek de gerekiyor."

GT08_NEDEN_65 = {
    "task_response": "Uc madde de karsilaniyor: tasinma sebebi is ve sehir uzerinden anlatiliyor, kasaba ve ev nufusuyla ve konumuyla tarif ediliyor, davet tarih ve sure vererek yapiliyor. Arkadasin halini soran acilis mektubu gercekci kiliyor, ama sebep paragrafinda karar ani biraz aceleye geliyor.",
    "coherence_cohesion": "Paragraflar konu konu bolunmus ve her biri tek bir maddeyi tasiyor. So please come and stay with me gibi gecisler dogru ama tanidik; ucuncu paragrafta ev ile kasaba ayni paragrafta kaliyor.",
    "lexical_resource": "Harbour, lighthouse, a proper bed, keeping you too busy gibi samimi mektuba uygun ogeler var ve ton bastan sona arkadasca. Thirty thousands ve on the middle of July gibi yerlerde bicim tam oturmuyor.",
    "grammatical_range_accuracy": "Ilgi cumlecikleri ve kosullu yapi dogru kuruluyor, uzun cumleler dagilmiyor. Cumlelerin yaklasik yarisinda edat, cogul ya da soru sirasi hatasi var (in the end of next month, tired from this city, in two year, thirty thousands people, on the middle of July, tell me how are you) ve bir yerde nokta yerine virgul kullanilmis; anlam hicbir yerde engellenmiyor.",
}
GT08_LIFT_65 = "Evi anlatan cumleleri ayri bir paragrafa almak, kasaba ile evi karistirmadan. Dilbilgisinde tekrar eden iki nokta var: zaman edatlari (in the end of, on the middle of) ve dolayli soruda sozcuk sirasi (tell me how you are)."

GT08_NEDEN_8 = {
    "task_response": "Uc madde de tam ve dogal: haber bir kisisel giristen sonra veriliyor, sebep hem is hem sehir yorgunlugu olarak aciliyor, kasaba ve ev tek tek goruluyor, davet tarih, sure ve birlikte yapilacak seylerle somut. Arkadasin haberini soran kapanis mektubu tamamliyor.",
    "coherence_cohesion": "Bes paragraf haber, sebep, yeni yer, davet ve kapanis sirasini izliyor ve gecisler It came out of nowhere / You would love the place gibi konusma ritmiyle yapiliyor. Hicbir paragraf ikinci bir konuya kaymiyor.",
    "lexical_resource": "Samimi mektup icin dogal ve az kullanilan ogeler var: sitting on some news, packing up, wearing me down, catch you out, what you have been up to. Treating you kindly acilisi biraz fazla islenmis duruyor.",
    "grammatical_range_accuracy": "Zaman kipleri, kosullu yapi ve dolayli soru esnek ve dogru kullaniliyor; hatali cumle yok denecek kadar az. Ucuncu paragrafin son cumlesi uc bilgiyi birden tasidigi icin uzun kaliyor.",
}
GT08_LIFT_8 = "Ucuncu paragrafin son cumlesini ikiye bolmek: tavanlar ile balkon ayri cumlelere dusunce mektubun ritmi rahatlar. Acilistaki treating you kindly kalibi sadelestirilirse ton daha dogal olur."


# ================================================================ T2-50
# problem_solution: is yerinde yazili mesaj yuku

T2_50_5 = """Nowadays the workers in the offices are receiving a lot of message in every day, and they must to read and answer all of them. In my opinion this situation is creating a big problem for the companies and for the employee also.

Firstly, the most important problem is the time. If a person get sixty message in a day, he is passing almost the half of his working day only for the reading and the answering, and his real job is staying for the evening. In my old company we was writing to each other all the day, and one time I finish an important report at ten o'clock in the night.

Secondly, a necessary information can be lost between all this messages. The manager send one message about a change of the meeting and after that twenty other message are coming, so the people not see it and after they are saying nobody informed me. This is making a confusion in the team and sometimes the client is waiting for nothing.

Thirdly, the person is cutting his work every ten minutes and starting again from the beginning. This is very tiring for the brain and in the end of the day you are feeling empty, also you are doing more mistake than normal. Some of my friends are looking their telephone in the holiday also, because the messages are coming in the night and in the weekend, and they can not rest in their mind.

For this reason I think the people must send less message and the managers must to find a good solution for this situation."""

T2_50_65 = """It is true that a large part of the working day is now spent on written messages. In my view this creates real difficulties for the employee and for the company, and the best answers are the ones which change the rules of the office instead the habits of one person.

The first problem is that nobody has a long period of quiet time any more. A report needs two or three hours without interruption, but if a message arrives every ten minutes the work is done in small piece. A colleague of mine prepares her monthly figures at home on Sunday, because it is the only silent time.

The second problem is that important information disappears in the crowd. When forty messages arrive in a morning, the one which announces a change of a deadline looks exactly the same like the others, and it is easy to miss it. The team then repeats a work or gives a wrong answer to a customer, and this costs more time than the message saved.

Several measures could reduce this. Companies should make a clear rule about who needs to receive a copy of each message, because half of the readers have no part in the subject. Documents which everybody uses can be kept in one shared place, instead to be sent again and again to everybody. Many organisations also protect a part of the morning, when no internal message is send, and a short conversation replaces a long chain of written answers.

In conclusion, the flood of messages costs attention and hides what is important. Rules made by the organisation would help more than the good intentions of the individual worker, because the interrupted person is not the person who writes."""

T2_50_8 = """In many organisations the working day begins and ends with a screen full of written messages, and a considerable proportion of the time meant for the job itself goes on answering them. The difficulties this creates are real, and in my view they are best met by rules the organisation sets rather than by asking individuals to show restraint.

The first cost is the loss of uninterrupted time. Work of any depth - a set of accounts, a design, an analysis - needs stretches of two or three hours, and a message every few minutes breaks them into fragments. The result is not merely slower work but poorer work, since the mind never settles far enough into the problem.

The second cost is that the important message becomes invisible. When forty arrive in a morning, the one announcing a moved deadline looks exactly like the thirty-nine that could have waited. The team then duplicates work or gives a customer an answer that was overtaken two days earlier, and the time lost is greater than the time saved.

The remedies that last are structural rather than personal. A rule about who genuinely needs a copy removes a surprising share of the traffic, since half the recipients have no part in the subject. Shared documents kept in one place, rather than circulated repeatedly as attachments, remove another. Some organisations also protect a stretch of the morning during which nothing internal is sent, and encourage a two-minute conversation instead of nine written replies.

None of this asks anyone to communicate less; it asks the organisation to decide what is worth writing down and to whom. That decision cannot be left to the individual, because the person who bears the interruption never chose to send it."""

T2_50_NEDEN_5 = {
    "task_response": "Sorunlar bolumu ucuncu paragrafa kadar somut ornekle yuruyor, ama gorevin ikinci yarisi olan onlemler tek bir dilek cumlesine indirgenmis: daha az mesaj gonderilmeli ve yoneticiler bir cozum bulmali. Bu cumlenin arkasinda ne kim yapacak ne de nasil yapilacak var, yani iki yukumlulukten biri karsilanmiyor.",
    "coherence_cohesion": "Firstly / Secondly / Thirdly paragraflarin mantigini degil yalnizca sirayi tasiyor ve son paragraf tek cumlede bitiyor. Yine de her paragraf tek bir soruna baktigi icin okuyucu yolunu kaybetmiyor.",
    "lexical_resource": "Sozcuk gunluk ve tekrarli: message, problem, time donup duruyor, alanin sozcugu yok. Cutting his work, rest in their mind ve empty gibi secimler okuru bir an durduruyor.",
    "grammatical_range_accuracy": "Neredeyse her cumlede hata var: a lot of message, must to read, a person get, we was writing, I finish, a necessary information, all this messages, the manager send, twenty other message, the people not see, more mistake, less message. Butun metin genis zamanla simdiki zaman arasinda gidip geliyor ve yapilar basit cumleden ibaret.",
}
T2_50_LIFT_5 = "Son paragrafi atip yerine gercek bir onlemler bolumu yazmak: mesajin kime gonderilecegine kural koymak, ortak belgeleri tek bir yerde tutmak, gunun bir bolumunu yazismasiz birakmak - her biri hangi soruna karsilik geldigi soylenerek. Boylece gorevin ikinci yarisi karsilanir."

T2_50_NEDEN_65 = {
    "task_response": "Gorevin iki yarisi da yaziliyor: iki sorun ornekle aciliyor, onlemler bolumu uc somut oneri veriyor ve sonucta kurallarin kisisel aliskanliktan daha etkili oldugu soyleniyor. Onlemler ile sorunlar arasindaki eslesme yalnizca ikinci onlemde acikca kuruluyor, otekilerde okuyucunun kendi kurmasi gerekiyor.",
    "coherence_cohesion": "Dort bolum duzenli: sorun, sorun, onlemler, sonuc; her paragrafin bir konusu var. The first problem / The second problem / Several measures kaliplari duzeni tasiyor ama gecisler mekanik ve paragraf iclerindeki sirayi baska bir baglayici desteklemiyor.",
    "lexical_resource": "Uninterrupted olmasa da quiet time, announces a change of a deadline, the flood of messages, good intentions gibi ogeler konuyu tasiyor ve tekrar sinirli. Instead the habits ve looks exactly the same like gibi yerlerde esdizim tam oturmuyor.",
    "grammatical_range_accuracy": "Ilgi cumlecikleri ve kosullu yapi dogru kuruluyor, uzun cumleler dagilmiyor. Cumlelerin yaklasik yarisinda edat, tanimlik ya da cogul hatasi var (instead the habits, in small piece, the same like, easy to miss it, repeats a work, instead to be sent, is send); anlam hicbir yerde engellenmiyor.",
}
T2_50_LIFT_65 = "Her onlemin hangi soruna karsilik geldigini acikca yazmak - ortak belge deposu hangi sorunu, sessiz saat hangisini cozuyor. Dilbilgisinde de tekrar eden iki nokta var: instead kalibi ve the same as."

T2_50_NEDEN_8 = {
    "task_response": "Gorevin iki yarisi da tam: iki sorun sebep zinciriyle acilyor, uc onlem bunlarla eslesiyor ve son paragraf onlemlerin neden kurumun sorumlulugunda oldugunu gerekcelendiriyor. Position bastan sona ayni: kurallar kisisel kisitlamadan daha kalici.",
    "coherence_cohesion": "Bes paragraf ilerlemeyi kendiliginden tasiyor ve baglantilar The first cost / The second cost disinda cumle icine gomulu. Son paragraf onceki bolumleri ozetlemek yerine onlarin uzerine bir hukum kuruyor.",
    "lexical_resource": "Konuya ait esnek ogeler var: a considerable proportion, uninterrupted stretches, structural remedies, overtaken two days earlier, circulated repeatedly as attachments. Bir iki yerde vurgu biraz agir kaliyor.",
    "grammatical_range_accuracy": "Uzun cumleler ara cumleciklerle kuruluyor ve hicbiri dagilmiyor; hatali cumle yok denecek kadar az. Ucuncu paragrafin son cumlesi iki fikri birden tasidigi icin biraz sikisik.",
}
T2_50_LIFT_8 = "Onlemler paragrafinda ucuncu oneri (sessiz saat) otekilerden kisa kaliyor; bir cumlelik somut sonucu eklenirse paragraf dengelenir. Ucuncu paragrafin son cumlesini ikiye bolmek de okumayi rahatlatir."


# ================================================================ T2-54
# advantages_disadvantages: kamusal alanlarda kamera

T2_54_5 = """In many towns today there are cameras in the streets and in the squares, and they are recording the people all the day and all the night. In my opinion this is more good than bad for the society.

Firstly, the camera is helping when something bad is happen. If two car are crashing in a crossroad, nobody can lie about who was passing in the red light, because the police is looking the record and they are seeing the truth. Last year my uncle lose his bag in the bus station and the security find it in the camera, so after two day he take his bag back.

Secondly, the people are feeling more safe in the night. My sister is finishing her work at eleven o'clock and she is walking alone until her home, and she say she is not afraid so much in the streets where there is a camera, because if somebody follow her there is a proof after.

Thirdly, the punishment in my country is very light and this is the real problem. The person who is stealing a telephone is going out from the police station after some hour, and after one week he is doing the same thing again. If the judges are giving a serious punishment, the people will think two time before they are doing a crime, and the camera also will be more useful. Many people are saying the same thing in the television.

So for all this reasons, the cameras in the public places are a good thing and every town must to put more of them."""

T2_54_65 = """In many towns today the streets, the squares and the public buildings are watched by cameras during all the day and the night. In my opinion the benefits are bigger than the problems, but only if there are clear rules about the records.

The main advantage is that a camera shows what really happened. After a traffic accident or a fight in front of a bar, the two side are usually telling different stories, and without a record the police cannot decide who is right. A camera also helps in ordinary situations: last year my uncle left his bag in the bus station and the staff found it in twenty minutes. Many people, especially who are walking alone at night, also feel calmer when they know that the street is not empty of witnesses.

There are however real disadvantages. The first one is the feeling of being watched all the time, which is not comfortable even for the people who is doing nothing wrong. The second one is that nobody knows exactly who is looking at these images and how long they are keeping them. If the records are given to any person who asks for it, the camera becomes a danger instead a protection. It is also true that a camera does not stop a crime, it only moves it: the thief goes to the next street.

In conclusion, I believe the advantages are stronger, because a record which shows what happened protects both the victim and the innocent person who is accused wrongly. But this is only valid when the access to the images are limited and the recordings are deleted after a short period. Without these rules the disadvantages would grow quickly."""

T2_54_8 = """Cameras now watch over streets and public buildings in most towns, around the clock. On balance the gains outweigh the costs, though only under conditions that are easy to state and often ignored.

The clearest gain is that a recording settles what actually happened. After a collision at a junction or a scuffle outside a bar, the accounts given to the police are irreconcilable, and the case rests on whichever witness sounds more convincing. That protects the person wrongly accused at least as much as it protects the victim. Cameras earn their place in duller ways too: a bag left on a bench is traced in twenty minutes, and someone walking home late knows the street is not empty.

The costs are not imaginary either. Being recorded continuously changes how people behave in public space, and that is a small loss of freedom even for those with nothing to hide. More concretely, few residents could say who holds the images of their town, who may look at them, or how long they are kept, and a recording that can be copied becomes a threat rather than a safeguard. Nor do cameras remove crime so much as relocate it, since a thief who knows which corner is watched works the next one.

The balance still falls on the side of the cameras, but the conditions matter more than the cameras. Access should be restricted to investigators working on a named incident, footage should be deleted within weeks unless it is needed, and the money should not come from street lighting or from officers on the ground. Used in that way, a camera is a useful witness; used in any other way, it is a machine that knows too much about people who have done nothing."""

T2_54_NEDEN_5 = {
    "task_response": "Avantaj tarafi iki somut ornekle veriliyor ve bastaki hukum sonda tekrar ediliyor, ama dezavantaj tarafi hic yazilmamis: ucuncu paragraf cezalarin hafifligine kayiyor, yani sorulan sorunun yanindaki baska bir soru cevaplaniyor. Iki yukumlulukten biri boylece hic karsilanmiyor.",
    "coherence_cohesion": "Firstly / Secondly / Thirdly paragraflari sirali tutuyor ve her paragraf tek bir noktaya bakiyor. Ucuncu paragrafin konusu digerleriyle bagli olmadigi icin ilerleme burada kopuyor ve okuyucu kameradan cezaya nasil gecildigini kendi kurmak zorunda kaliyor.",
    "lexical_resource": "Sozcuk gunluk ve tekrarli: camera, people, good donup duruyor, konunun sozcugu proof disinda yok. More good, safe in the night, in the television gibi secimler okuru bir an durduruyor.",
    "grammatical_range_accuracy": "Neredeyse her cumlede hata var: something bad is happen, two car are crashing, in a crossroad, passing in the red light, the police is looking the record, my uncle lose, after two day, she say, until her home, if somebody follow her, after some hour, think two time, must to put. Butun metin simdiki zamana sikismis ve gecmis anlatilirken de zaman degismiyor.",
}
T2_54_LIFT_5 = "Ucuncu paragrafi tamamen degistirmek: cezalarin agirligi bu sorunun konusu degil. Yerine dezavantajlar yazilmali - surekli izlenme duygusu, kayitlarin kimde kaldigi, sucun baska sokaga kaymasi - ve ancak ondan sonra hukum verilmeli."

T2_54_NEDEN_65 = {
    "task_response": "Iki taraf da yaziliyor ve sonuc kosullu ama net: avantajlar agir basiyor, ancak erisim ve saklama kurali varsa. Avantaj tarafi somut orneklerle yuruyor, dezavantajlarda sucun yer degistirmesi maddesi tek cumlede kaliyor ve maliyet konusuna hic girilmiyor.",
    "coherence_cohesion": "Dort bolum duzenli: giris ve hukum, avantajlar, dezavantajlar, sonuc. There are however real disadvantages ile donus acikca isaretleniyor, ama The first one / The second one kalibi paragraf icinde mekanik duruyor.",
    "lexical_resource": "Konuya uygun ogeler var: witnesses, records, access, protection, accused wrongly. Instead a protection ve especially who are walking gibi yerlerde bicim tam oturmuyor, camera sozcugu da sik tekrarlaniyor.",
    "grammatical_range_accuracy": "Ilgi cumlecikleri ve kosullu yapi dogru kuruluyor, uzun cumleler dagilmiyor. Cumlelerin yarisinda tanimlik, edat, cogul ya da uyum hatasi var (during all the day, the two side, especially who are walking, the people who is, who asks for it, instead a protection, the access are limited, it only moves it virgulle baglanmis); anlam hicbir yerde engellenmiyor.",
}
T2_54_LIFT_65 = "Dezavantaj tarafina maliyet maddesini eklemek ve sucun yer degistirmesini bir cumle daha acmak, iki tarafi esitler. It is also true that a camera does not stop a crime, it only moves it cumlesindeki virgul de noktali virgul olmali."

T2_54_NEDEN_8 = {
    "task_response": "Iki taraf da ayrintili ve hukum kosullariyla birlikte veriliyor: kameralar yararli, ama erisim, saklama suresi ve butce kosullariyla. Avantajlarda hem ciddi hem siradan ornek var, dezavantajlarda uc ayri madde geciyor ve son paragraf kosullari tek tek sayiyor.",
    "coherence_cohesion": "Dort paragraf ilerlemeyi kendiliginden tasiyor ve baglantilar cumle icine gomulu (on balance, more concretely, nor do cameras). Kapanistaki iki kisa cumle hukmu ozetlemek yerine karsitlik kurarak bitiriyor.",
    "lexical_resource": "Konuya ait esnek ogeler var: around the clock, irreconcilable, a safeguard, relocate, footage, reassurance. Cameras earn their place in far duller ways too biraz fazla islenmis duruyor.",
    "grammatical_range_accuracy": "Devrik yapi, ara cumlecik ve kosullu bicimler dogru ve dogal kullaniliyor; hatali cumle yok denecek kadar az. Ucuncu paragrafin ikinci cumlesi uc soruyu birden tasidigi icin uzun kaliyor.",
}
T2_54_LIFT_8 = "Maliyet argumani (paranin sokak aydinlatmasindan alinmasi) yalnizca son paragrafta geciyor; dezavantajlar paragrafinda bir cumleyle kurulursa hukum daha saglam durur. Ucuncu paragrafin uzun cumlesini bolmek de okumayi rahatlatir."


VERI = [
    ("GT06", 150, [
        (5.0, GT06_5, GT06_NEDEN_5, GT06_LIFT_5),
        (6.5, GT06_65, GT06_NEDEN_65, GT06_LIFT_65),
        (8.0, GT06_8, GT06_NEDEN_8, GT06_LIFT_8),
    ]),
    ("GT07", 150, [
        (5.0, GT07_5, GT07_NEDEN_5, GT07_LIFT_5),
        (6.5, GT07_65, GT07_NEDEN_65, GT07_LIFT_65),
        (8.0, GT07_8, GT07_NEDEN_8, GT07_LIFT_8),
    ]),
    ("GT08", 150, [
        (5.0, GT08_5, GT08_NEDEN_5, GT08_LIFT_5),
        (6.5, GT08_65, GT08_NEDEN_65, GT08_LIFT_65),
        (8.0, GT08_8, GT08_NEDEN_8, GT08_LIFT_8),
    ]),
    ("T2-50", 250, [
        (5.0, T2_50_5, T2_50_NEDEN_5, T2_50_LIFT_5),
        (6.5, T2_50_65, T2_50_NEDEN_65, T2_50_LIFT_65),
        (8.0, T2_50_8, T2_50_NEDEN_8, T2_50_LIFT_8),
    ]),
    ("T2-54", 250, [
        (5.0, T2_54_5, T2_54_NEDEN_5, T2_54_LIFT_5),
        (6.5, T2_54_65, T2_54_NEDEN_65, T2_54_LIFT_65),
        (8.0, T2_54_8, T2_54_NEDEN_8, T2_54_LIFT_8),
    ]),
]


def main():
    os.makedirs(HEDEF, exist_ok=True)
    for kod, alt_sinir, cevaplar in VERI:
        answers = []
        for band, metin, neden, yukselt in cevaplar:
            n = _say(metin)
            if n < alt_sinir:
                raise SystemExit("%s band %s: %d kelime, %d'nin altinda"
                                 % (kod, band, n, alt_sinir))
            answers.append({
                "band": band,
                "text": metin,
                "word_count": n,
                "why_this_band": neden,
                "what_would_lift_it": yukselt,
            })
        belge = {
            "exam": "ielts",
            "schema_version": "1.0",
            "kind": "model_answer_set",
            "skill": "writing",
            "task_ref": kod,
            "answers": answers,
        }
        yol = os.path.join(HEDEF, kod + ".json")
        with open(yol, "w", encoding="utf-8") as f:
            json.dump(belge, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(kod, [a["word_count"] for a in answers])


if __name__ == "__main__":
    main()
