# -*- coding: utf-8 -*-
"""Ornek cevap kutuphanesi - 2. grup: Academic Task 2 (T2-01, T2-06, T2-10, T2-15, T2-17).

Gorev secimi: task2 havuzunda bes soru kalibi var (opinion, discuss_both_views,
problem_solution, advantages_disadvantages, double_question). Bu gruba her kaliptan
bir gorev alindi, konu alani tekrar etmeyecek sekilde ilk uygun dosya secilerek.
Boylece kutuphane bes kalibin de nasil cevaplandigini gosteriyor.

Metinler burada duz Python dizesi olarak duruyor; kelime sayisi JSON'a elle
yazilmiyor, uretim sirasinda sayiliyor - metin duzeltilince sayac sessizce yanlis
kalmasin diye. Sayim kurali degerlendirme talimatiyla ayni: bosluga gore ayrilan
belirtec sayisi. Task 2'de alt sinir 250.
"""
import json
import os

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEDEF = os.path.join(KOK, "content", "ornek-cevaplar", "writing")
ALT_SINIR = 250


def _say(metin):
    return len(metin.split())


# ---------------------------------------------------------------- T2-01
# opinion / egitim: pratik ders zorunlu olmali mi
T2_01_5 = """Nowadays some peoples think the student in the secondary school must learn a practical lesson like the cooking or the money, and other people don't think this. In my opinion I am agree with this idea because it is very important for the life.

Firstly, the practical lesson is very useful. When a student finish the school he must live alone and he don't know how to cook a simple food or how to repair a small thing in the house. If the school teach this lesson, the student can do all this thing alone and he don't spend money for call a repair man every time. Also he can save the money every month and this is a good thing for a young person who don't have a big salary.

Secondly, in the school we learn many subject like the mathematic and the history, but this subject don't help us in the daily life. A student can know all the date of the history but he cannot open a bank account and he cannot understand a bill. This is a big problem for the young people today.

On the other hand, some people say the programme of the school is already very full and the teacher don't have time for a new lesson. This is true, but the school can give only one hour in the week and it is enough for learn the basic thing.

In conclusion, I think the practical subject is very useful and the young people must learn it, because the school must prepare the student for the real life and not only for the exam."""

T2_01_65 = """It is often argued that all secondary school students should have to take a practical subject, such as cooking, simple repairs or managing money, as well as their academic ones. I mostly agree with this idea, although I believe one lesson a week would be enough.

Firstly, many young people leave school without the skills they need for daily life. They have studied literature and science for years, but they cannot prepare a healthy meal, deal with a bank account or to fix a dripping tap. As a result, they either waste money on services they could easily do themselves, or they depend to their family for much longer than necessary. A short weekly lesson would give them this abilities before the moment they need them.

Secondly, making the subject compulsory is important for fairness. Some children learn to cook and to control their money at home, because their parents have the time and the knowledge to teach them. Others do not have this chance at all. If the subject stays optional, exactly the students who need it most will not choose it, and the distance between the two group will become bigger.

On the other hand, it is true that the timetable is already crowded and teachers often complain that they cannot finish their programme. Adding another obligatory subject could reduce the hours of mathematics or of a foreign language, which is necessary for the university.

In conclusion, I agree that practical subjects should be a required part of secondary education, but they should take only a small place in the week, so that the academic learning does not suffer from it."""

T2_01_8 = """Whether teenagers should be obliged to study something practical alongside their academic subjects is a question that divides opinion sharply. I broadly agree that a compulsory practical strand is justified, provided it is genuinely taught rather than squeezed into the margins of the timetable.

The strongest argument in its favour is that these skills are unevenly distributed at home. A student whose parents cook, budget carefully and repair what breaks will absorb all of it without a single lesson; a student whose parents work long shifts, or who never had the chance to learn themselves, will not. Leaving the subject optional therefore hands a further advantage to those who already have one, whereas making it compulsory closes a gap that schools are otherwise content to ignore.

There is also a case to be made about what secondary education is for. Schools already claim to prepare young people for adult life, yet a school leaver may be able to analyse a poem and still be unable to read an electricity bill or work out what borrowing actually costs. Financial illiteracy in particular has consequences that last for decades, and a few hours spent on interest rates would be repaid many times over.

The obvious objection is time. Curricula are crowded, examination pressure is intense, and every new requirement takes hours away from something else. That is a genuine cost, and it is precisely why I would keep the requirement modest: one period a week over two or three years, assessed lightly, is enough to build competence without displacing core subjects.

On balance, then, the principle seems sound to me, as long as what follows from it stays proportionate."""

# ---------------------------------------------------------------- T2-06
# discuss_both_views / ulasim: toplu tasima mi yol mu
T2_06_5 = """In these days the government must decide where they spend the money for the transport. Some people say the bus and the train is more better, and other people say the road for the car and the lorry is more important. I want to explain this two opinion and after I give my idea.

Firstly, the people who support the public transport say it is cheap and everybody can use it. A poor family don't have a car, so if there is a bus in every hour they can go to the work and to the hospital without problem. Also, when many person use the bus, the traffic in the city centre is less and the air is more clean. In my city the bus is always full in the morning and this show the people need it.

Secondly, the other group say the road is also necessary. The lorry carry the food and the other product to the shop and this is important for the economy of the country.

In my opinion the government must give the most money to the bus and the train, because in the big city the road is never enough. When they make a new road, after two year it is full again and the same problem come back. So it is more better to make a metro line and many bus line, and the people leave the car in the house.

In conclusion, the two view have a good point, but I am agree with the first opinion, because the public transport help more people in the same time and it is also better for the environment."""

T2_06_65 = """Governments have a limited transport budget, and there is a disagreement about whether it should go mainly to public transport or to roads. Both position have reasonable arguments behind them, but I believe that buses and trains should receive the larger share in most cases.

Those who support spending on public transport point out that it is available to everyone. People who cannot afford a car, or who are too young or too old to drive, still need to reach to their workplace, their school and their doctor. In addition, a full bus takes the space of only two or three cars, so a good network reduce congestion and pollution at the same time. Cities which have invested in metro lines usually have a faster centre than cities which have not.

On the other side, the supporters of road building make the point that goods do not travel by train to the door of every shop. Lorries need reliable roads, and so do the people who live in villages where a bus service would be empty in most of the day. If these roads are narrow and badly maintained, journeys become slow and dangerous, and the businesses in rural areas suffer from it.

In my opinion, the correct answer depends on the density of the population. In a crowded city, building more roads only attract more cars and the congestion comes back within a few years, so public transport is the better investment. In a region with few inhabitants, however, a bus every three hours helps almost nobody, and the money is better spent on the road itself.

To conclude, I support public transport as the main priority, but roads should not be forgotten where they are the only realistic option."""

T2_06_8 = """How a government divides its transport spending between public networks and the road system is a question with defensible answers on both sides, and the right balance is unlikely to be the same everywhere.

The case for prioritising buses and trains rests on capacity and access. A single railway line can move more people in an hour than several lanes of traffic, and it does so without demanding a parking space at the other end. Just as importantly, a bus fare is within reach of households that could never run a car, so investment here reaches teenagers, elderly passengers and low-paid workers who are otherwise simply excluded. There is also the familiar tendency of new road capacity to fill up again: a few years after a motorway is widened, it often carries the same slow traffic as before, and by then the alternative has been made less attractive still.

The opposing view is not without force. Freight does not run on a timetable, and almost every item on a shop shelf completes its journey by lorry. In thinly populated regions, meanwhile, a service that runs three times a day is no substitute for a car, and money spent on it buys very little mobility compared with resurfacing a road that everybody already uses.

My own view is that the argument turns on density rather than on principle. Where people live close together, public transport is the only way of moving large numbers without paralysing the streets, and it deserves the greater part of the budget. Where they do not, the same money achieves more on the roads. A national policy that ignores this distinction will waste resources in one kind of place while starving the other."""

# ---------------------------------------------------------------- T2-10
# problem_solution / sehir hayati: merkezdeki konut pahali, calisanlar uzakta oturuyor
T2_10_5 = """Today in the big city the house near the centre is very expensive, so the worker must live very far away. This situation make many problem for the people and also for the city.

Firstly, the biggest problem is the time. A person who live outside the city must wake up at five o'clock in the morning and travel two hour for arrive to the work. In the evening he travel again two hour, so he don't have time for his family and for the rest. This is very bad for the health and after some year he become tired and sick, and he cannot work good.

Secondly, the transport is expensive. The train ticket and the petrol take a big part of the salary, so the worker earn the money but after he give it to the transport company. Some family cannot pay this money and they must change the job or leave the city.

Thirdly, the city have a problem too, because the hospital and the restaurant cannot find the employee. The nurse and the waiter don't want to travel four hour in every day for a small salary, so they go to another city and the service is more bad for everybody.

For the measure, the government must build more cheap house in the centre and control the price of the rent. Also the company can give a money for the transport of the employee.

In conclusion, the expensive house create a big problem for the worker and for all the city, and the government must find a solution quickly before the situation become more bad."""

T2_10_65 = """In many large cities, housing close to the centre has become so costly that the people who work there are forced to live far outside. This creates serious difficulties both for the workers themselves and for the city, but there is some measure which can reduce them.

The first problem is the length of the daily journey. Somebody who lives fifty kilometres away may spend three or four hours a day travelling, which leaves very little time for family, exercise or rest. Over the years this produce tiredness and health problems, and the quality of their work also goes down. The second problem is the cost, because train tickets and fuel take a large part of a modest salary, so the money saved on rent is spent again in the road.

There is also a problem for the city itself. Hospitals, schools, shops and restaurants in the centre need staffs who are not highly paid, and these workers are exactly the ones who cannot afford to live nearby. When they decide that the journey is not worth it, the services in the centre become weaker for everyone.

Several measures could be taken. Local authorities should require developers to include a proportion of affordable flats in every new building, and they can also make an offer of empty offices to be transformed into housing. Employers, for their part, could allow home working for some days of the week, which immediately reduce the number of journeys. Finally, a faster and cheaper rail service would make the distance less painful for those who still have to travel.

In conclusion, the main difficulties are exhaustion, expense and a shortage of staff in the centre, and they need action from both city authorities and employers."""

T2_10_8 = """In city after city, the homes closest to the centre have been priced out of reach of the people whose work keeps that centre running, pushing them into a long daily commute. The consequences fall on individuals and on the city as a whole, and they call for measures at both levels.

For the individual, the most immediate cost is time. Three or four hours a day spent on a train or in traffic is time not spent sleeping, cooking, exercising or with children, and the effects accumulate quietly over years rather than announcing themselves at once. The second cost is financial: fares and fuel claw back much of what was saved on rent, so the household ends up no better off, merely more tired.

The city pays a different price. The centre depends on cleaners, nurses, drivers and kitchen staff, and these are precisely the people whose wages will never cover a flat nearby. Once the commute becomes intolerable, they take work elsewhere, and hospitals and restaurants find themselves short-staffed in the middle of a crowded city.

The remedies have to address supply as well as distance. The most effective is to oblige developers to set aside a fixed share of every new scheme for affordable rent, since without such a rule the market builds only what returns most. Converting redundant office space into flats adds housing without consuming new land. Employers can also help, both by supporting home working where the job allows it and by contributing to travel costs where it does not.

None of these measures works alone, but together they attack the two halves of the problem: the shortage of central housing, and the burden borne by those who cannot reach it."""

# ---------------------------------------------------------------- T2-15
# advantages_disadvantages / teknoloji: gunluk hizmetler yalnizca cevrim ici
T2_15_5 = """In this modern life many service like the bank, the bill and the appointment of the doctor is only in the internet or in the application. Some people think this is a good thing and other people think it is a bad thing. I want to write the advantage and the disadvantage of this situation.

Firstly, the advantage is very clear. The people don't go to the office and don't wait in a long queue for one hour. They open the phone in the house and in five minute the work is finish. Also the internet don't close in the night, so a person who work all the day can pay the bill at eleven o'clock in the night. This save the time and also the money of the transport.

Secondly, there is many disadvantage too. The old people don't know how to use the application and they are afraid to make a mistake with the money. Also some people in the village don't have a good connection and they cannot enter to the system. When the application have a problem, there is nobody for help you and you must call a telephone number and wait very long time.

In my country my grandmother cannot pay her bill alone and every month my father must do it for her. This is not a good situation for a old person.

In conclusion, the online service have a big advantage and also a big disadvantage. Both of them are important and every person must decide alone which one is more strong for him."""

T2_15_65 = """A growing number of everyday services, from banking to booking a medical appointment, can now only be reached through a website or an application. In my view the benefits of this change are greater than the drawbacks, but only if some alternative is kept for those who cannot use a screen.

The main advantage is convenience. A transaction that used to require a bus journey, a queue and half a morning off work can now be completed in a few minutes at any hour of the day or night. This is particularly valuable for people with long working hours or small children, who find very difficult to visit an office between nine and five. Organisations also spend less on buildings and counter staff, and a part of this saving usually return to the customer in the form of lower charges.

However, the disadvantages should not be minimised. Elderly people who has never used a computer, and households in areas with a weak connection, can suddenly find themselves unable to do something they have always done. When the system breaks down, moreover, there is nobody in front of you to explain the problem, and a telephone helpline with a waiting time of forty minutes is a poor replacement for a member of staff.

Overall, I think the advantages do outweigh the disadvantages, because they are felt by the great majority every single week, while the serious difficulties falls on a smaller group. That group is real, however, so companies and public offices should be obliged to keep at least one non-digital way for doing the same thing."""

T2_15_8 = """Banking, paying bills and arranging appointments have quietly migrated to the screen, and in many cases the older counter or telephone route has been closed altogether. Weighed against each other, the gains are substantial enough to justify the shift, though only where a non-digital route survives alongside it.

What has been gained is chiefly time. A task that once meant an hour of queuing, and often an hour taken from the working day, is now finished in a few minutes at whatever hour suits the user. For anyone juggling shift work or childcare, that difference is not a minor convenience but the difference between managing their affairs and postponing them indefinitely. There is a second, less visible gain: a digital record leaves the customer with proof of what was agreed, which used to depend on whoever happened to be behind the desk.

Against this stands a genuine risk of exclusion. A person of eighty who has never owned a computer, or a household on a patchy rural connection, does not simply find the new arrangement less convenient; they find the service unreachable. Failures are harder to resolve as well, since an automated system that rejects an application cannot be reasoned with, and a helpline queue is a poor substitute for someone who can look at the file with you.

My judgement is that the advantages prevail, because they are enjoyed constantly by most users while the losses, though severe, are concentrated on a minority. That conclusion carries a condition, however: it holds only for as long as providers are required to keep one staffed alternative open. Remove that, and the balance tips the other way for the people least able to complain about it."""

# ---------------------------------------------------------------- T2-17
# double_question / kultur ve gelenek: gelenekleri yaslilar surduruyor
T2_17_5 = """In many place today the traditional festival and the old custom is continue only by the old member of the community, and the young people don't participate very much. There is some reason for this situation.

Firstly, the life of a young person is very busy in this days. He work all the week, sometime also in the weekend, and when he come to the house he is very tired. The festival need a lot of preparation, for example the food and the clothes and the dance, and the young people don't have this time.

Secondly, many young people leave the village and they go to the big city for the university or for a better work. When a person live five hundred kilometre far, he cannot come every year for a festival of two day. So he lose the connection with the tradition of his family.

Thirdly, today there is many other thing for the free time. The young people watch the film in the phone, they play the game and they go to the shopping centre with the friend. This activity is more easy for them than a old custom, because they don't need a preparation.

Also I think the family is not same like before. In the past the grandmother live in the same house and she explain the tradition to the child. Today the young family live alone in a flat, so the child don't know the meaning of the festival.

In conclusion, the young people don't participate because they don't have the time, they live far away and they have many other activity. This is a big change in the society of today."""

T2_17_65 = """In a number of communities, traditional festivals and customs are now maintained almost entirely by older residents, while young people stay away. There are several reasons for this, and in my opinion the development is mainly a negative one.

The first reason is migration. Young adults move to cities for study or for better paid work, and once they live several hundred kilometres from their home town, to return for a two-day celebration every year becomes complicated and expensive. The second reason is the way free time is spent today. A generation which grew up with screens have an enormous choice of entertainment available at any moment, and a ceremony which requires days of preparation cannot easily compete with it. Finally, many of these customs are connected to an agricultural work or to crafts which most young people have never practised, so the meaning behind the festival is no longer obvious to them.

I consider this change harmful for two reasons. Traditions of this kind are one of the few occasions when different generations of a community do something together, and when they disappear the contact between the old and the young become weaker. In addition, the practical knowledge involved, such as a particular way of cooking, weaving or playing an instrument, only survives if it is passed from hand to hand, and it can be lost in a single generation.

It is fair to admit that customs have always changed and that some of them deserves to disappear. Nevertheless, losing them through simple neglect is different from replacing them consciously, and for this reason I regard the current tendency as a negative development."""

T2_17_8 = """In many communities the old festivals are still observed, but the people observing them are increasingly the older ones, with younger residents present as spectators at best. The reasons for this are largely practical, and while the change is not entirely negative, I think its costs outweigh its benefits.

The most powerful cause is simply where young people now live. Study and work draw them to cities, and a custom that assumes everyone is within walking distance of the same square cannot easily survive a diaspora of several hundred kilometres. Working patterns compound this: festivals that once fitted the rhythm of the agricultural year sit awkwardly beside shift work and fixed annual leave. There is also a question of meaning. Many of these observances grew out of harvests, crafts or trades that no longer form part of anyone's working life, so what remains is the ceremony without the experience that once made sense of it.

The strongest argument that this is not a loss is that traditions have never been fixed. Customs have always been abandoned, reinvented or absorbed into new forms, and a festival kept alive purely out of duty may already be an empty performance.

Even so, I find the trend regrettable. These occasions are among the few in which a community's generations do anything together, and their disappearance quietly removes one of the last shared spaces between the young and the old. The skills embedded in them are more fragile still: a technique of cooking or a way of playing an instrument is transmitted by imitation, and one generation of inattention is enough to end it. Change is not the problem; losing something valuable without ever deciding to is."""


VERI = [
    ("T2-01", [
        (5.0, T2_01_5, {
            "task_response": "Tutum ilk paragrafta soyleniyor ama esas soru olan zorunluluk hicbir yerde tartisilmiyor: metin bastan sona pratik derslerin faydali oldugunu anlatiyor, ki bu tek basina soruyu karsilamiyor. Gerekceler ayni fikri (gunluk hayatta ise yarar) iki kez tekrar ediyor ve ornekler somutlasmiyor.",
            "coherence_cohesion": "Firstly / Secondly / On the other hand / In conclusion iskeleti duzgun ve okur nerede oldugunu biliyor, ama baglantiyi bu dort kalip disinda hicbir sey tasimiyor. Paragraf iclerinde fikir gelistirilmiyor, cumleler yan yana diziliyor.",
            "lexical_resource": "Very important, very useful, a good thing kaliplari surekli tekrar ediyor; egitim ya da mufredat icin ozel tek bir sozcuk yok. Peoples, for learn, spend money for call gibi bicim hatalari okuru yavaslatiyor.",
            "grammatical_range_accuracy": "Neredeyse her cumlede uyum, tanimlik ya da kip hatasi var: I am agree, a student finish, he don't know, this subject don't help, the teacher don't have. If ve when cumlecikleri deneniyor ama gerisi basit cumle.",
        }, "Her paragrafa 'bu ders zorunlu mu olmali, secmeli mi' sorusunu acikca yanitlayan bir cumle eklemek; su haliyle metin sorulan soruya degil, komsu bir soruya cevap veriyor."),
        (6.5, T2_01_65, {
            "task_response": "Tutum girişte kosullu olarak konuyor (katiliyorum ama haftada bir ders) ve sonda ayni bicimde kapaniyor; zorunluluk boyutu ikinci paragrafta esitlik uzerinden gercekten tartisiliyor. Birinci gerekce ornekle destekleniyor, karsi gorus ise tek paragrafta ve gelistirilmeden geciliyor.",
            "coherence_cohesion": "Paragraf duzeni net: tutum, birinci gerekce, ikinci gerekce, karsi gorus, sonuc. Firstly / Secondly / On the other hand / In conclusion zinciri dogru ama tahmin edilebilir; gecisler icerikten degil kaliptan geliyor.",
            "lexical_resource": "Compulsory, optional, timetable, obligatory gibi konuya ait ogeler dogru kullanilmis. Control their money, the distance between the two groups ve suffer from it esdiziim olarak tam oturmuyor.",
            "grammatical_range_accuracy": "Ilgi cumlecigi, kosul cumlecigi ve zit baglaclar dogru kuruluyor ve hatasiz cumle sayisi fazla. Ucte bire yakin cumlede yine de bir hata var (or to fix a dripping tap, depend to their family, this abilities, the two group, which is necessary); hicbiri anlami engellemiyor.",
        }, "Karsi gorus paragrafini kendi ornegiyle gelistirmek ve ardindan neden yine de yetersiz kaldigini soylemek; su an itiraf ediliyor ama yanitlanmiyor."),
        (8.0, T2_01_8, {
            "task_response": "Tutum kosuluyla birlikte kuruluyor (zorunlu olsun, ama olculu olsun) ve son cumleye kadar ayni kosul tasiniyor. Esitlik gerekcesi somut bir karsitlikla, ikinci gerekce ise sonucun suresini gostererek gelistiriliyor; itiraz gercek bir maliyet olarak kabul edilip tutumun icine katiliyor.",
            "coherence_cohesion": "Paragraflar tez, iki gerekce, itiraz ve tartili sonuc olarak ilerliyor; her paragrafin tek bir merkezi var. Baglanti therefore, whereas, precisely why gibi ogelerle cumlenin isini yaparak kuruluyor, basa yapistirilan isaretlerle degil.",
            "lexical_resource": "Compulsory strand, unevenly distributed, curricula, financial illiteracy, proportionate gibi az kullanilan ogeler dogru esdiziimle geciyor. Squeezed into the margins ve repaid many times over gibi secimler dogal.",
            "grammatical_range_accuracy": "Noktali virgulle bagli karsitlik, ilgi cumlecikleri, yer degistirmis vurgu (it is precisely why) kontrollu bicimde kullanilmis. Hata seyrek ve okuru durdurmuyor; yine de band 9'un tam esnekligi yok.",
        }, "Bu duzeyde kazanc kesinlikten geliyor: 'olculu' derken kastedilen saatin ve degerlendirme bicimin bir kez daha somutlastirilmasi tezi daha da sikilastirir."),
    ]),
    ("T2-06", [
        (5.0, T2_06_5, {
            "task_response": "Toplu tasima gorusu iki gerekceyle anlatiliyor ama karsi gorus yalnizca iki cumle aliyor ve hic gelistirilmiyor; gorevin iki yukumlulugunden biri boylece karsilanmamis oluyor. Kendi gorus var ve tutarli, bu yuzden metin konunun disina dusmuyor.",
            "coherence_cohesion": "Firstly / Secondly / In my opinion / In conclusion sirasi izlenebilir, okur yolunu kaybetmiyor. Ama Secondly ile baslayan paragraf ikinci gorusun tamami, yani isaret ile icerik ayni agirlikta degil.",
            "lexical_resource": "Cheap, important, good, more better disina cikan ulasim sozcugu yok; traffic ve environment tekrar ediyor. More better ve more clean gibi karsilastirma bicimleri yanlis.",
            "grammatical_range_accuracy": "Uyum ve tanimlik hatalari her paragrafta: the bus and the train is, a poor family don't have, many person use, the lorry carry, I am agree. Yapilar cogunlukla basit ya da and/because ile baglanmis.",
        }, "Ikinci gorusu de en az bir paragrafa cikarip kendi ornegiyle desteklemek; su haliyle 'her iki gorusu tartis' talimatinin yarisi bos kaliyor."),
        (6.5, T2_06_65, {
            "task_response": "Her iki gorus de ayri paragrafta ve kendi gerekceleriyle veriliyor, kendi gorus ise nufus yogunluguna baglanarak kosullu bicimde soyleniyor. Kosul ilgi cekici ama tek cumlede geciyor, ornekle acilmiyor.",
            "coherence_cohesion": "Bolumleme dengeli: giris, birinci gorus, ikinci gorus, kendi gorus, sonuc. On the other side ve To conclude gibi tanidik kaliplarin disina cikilmiyor, gecisler mekanik kaliyor.",
            "lexical_resource": "Congestion, network, density, inhabitants, reliable gibi konuya uygun ogeler var. Have a faster centre, suffer from it ve helps almost nobody esdiziim olarak zorlama.",
            "grammatical_range_accuracy": "Ilgi cumlecikleri (people who cannot afford a car), zit yapilar ve kosul anlatimi dogru kurulmus; hatasiz cumle sayisi fazla. Ucte bire yakin cumlede uyum ya da edat hatasi var (Both position, reach to their workplace, a good network reduce, empty in most of the day, only attract more cars), ama anlam hicbir yerde bozulmuyor.",
        }, "Yogunluk kosulunu tek cumlede birakmayip somut bir karsilastirmaya donusturmek: ayni paranin kalabalik bir ilcede ve seyrek bir bolgede ne satin aldigini gostermek."),
        (8.0, T2_06_8, {
            "task_response": "Iki gorus de kendi en guclu haliyle sunuluyor: toplu tasima kapasite ve erisim uzerinden, yol ise yuk tasimaciligi ve seyrek nufus uzerinden. Kendi gorus tartisilan gerekcelerden cikiyor ve bir ilke degil bir olcut oneriyor (yogunluk), sonuc bu olcutle kapaniyor.",
            "coherence_cohesion": "Metin gorus-gorus-hakemlik seklinde ilerliyor ve her paragraf tek bir iddiayi tasiyor. Baglanti just as importantly, meanwhile, by then gibi ogelerle anlam duzeyinde kuruluyor; kapanis cumlesi iki tarafi tek karsitlikta topluyor.",
            "lexical_resource": "Induced demand, freight, thinly populated, resurfacing, paralysing gibi ogeler dogru esdiziimle kullanilmis. Within reach of households ve buys very little mobility secimleri dogal ve ekonomik.",
            "grammatical_range_accuracy": "Iki noktali aciklama, ortac yapilari ve zaman-yer cumlecikleri (where people live close together) esnek bicimde donusuyor. Hata seyrek; cumle uzunlugu bilincli olarak degisiyor.",
        }, "Yogunluk olcutunu sayisallastiran tek bir cumle (hangi buyuklukten sonra metro mantikli hale gelir) tezi daha da kesinlestirir."),
    ]),
    ("T2-10", [
        (5.0, T2_10_5, {
            "task_response": "Sorunlar uc paragrafta anlatiliyor ama onlemler iki cumleye sikismis ve hicbiri gelistirilmemis; gorevin iki yarisindan biri boylece bos kaliyor. Sorunlarin kendisi ilgili ve dogru secilmis, bu yuzden metin konunun disina dusmuyor.",
            "coherence_cohesion": "Firstly / Secondly / Thirdly / For the measure / In conclusion iskeleti sirayi gosteriyor ve okur takip edebiliyor. For the measure gecisi kaba ve bolumun kisaligini daha da gorunur kiliyor.",
            "lexical_resource": "Problem, expensive, money, bad sozcukleri tekrar ediyor; konut ya da ulasim icin ozel bir oge yok. More bad ve work good gibi bicimler yanlis, cannot find the employee esdiziim olarak tutmuyor.",
            "grammatical_range_accuracy": "Uyum, tanimlik ve cogul hatalari her cumlede: this situation make, a person who live, two hour, he don't have, the city have, in every day. Ilgi cumlecigi deneniyor ama gerisi basit cumle.",
        }, "Onlemler bolumunu en az bir paragrafa cikarip her onlemi bir sorunla eslestirmek ve kimin uygulayacagini yazmak; su haliyle sorulan iki seyden biri yanitsiz."),
        (6.5, T2_10_65, {
            "task_response": "Iki soru da ayri bolumlerde yanitlaniyor: uc sorun ve dort onlem, onlemlerin cogu sorunlarla eslesiyor ve uygulayicisi belirtiliyor. Ev calismasi ve tren hizmeti onerileri tek cumlede kaliyor, sonuclari acilmiyor.",
            "coherence_cohesion": "Bolumleme mantikli: birey duzeyinde sorunlar, sehir duzeyinde sorun, onlemler, sonuc. The first problem / The second problem / Several measures kaliplari duzenli ama mekanik ilerliyor.",
            "lexical_resource": "Affordable flats, developers, local authorities, modest salary gibi konuya uygun ogeler var. Make an offer of empty offices ve the quality of their work also goes down esdiziim olarak zorlama.",
            "grammatical_range_accuracy": "Edilgen cati, ilgi cumlecikleri ve zaman cumlecikleri dogru kullanilmis; hatasiz cumle sayisi fazla. Ucte bire yakin cumlede uyum, cogul ya da edat hatasi var (there is some measure, this produce tiredness, spent again in the road, need staffs, which immediately reduce); hicbiri okuru durdurmuyor.",
        }, "Her onlemin yaninda beklenen etkiyi bir cumleyle soylemek: hangi sorunu ne kadar hafifletiyor. Su an oneriler dogru ama sonuclariyla baglanmiyor."),
        (8.0, T2_10_8, {
            "task_response": "Sorunlar birey ve sehir olarak ayrilip her biri kendi mekanizmasiyla anlatiliyor, onlemler ise arz ve mesafe olarak iki basliga bolunup sorunlarla acikca eslestiriliyor. Kapanis hicbir onlemin tek basina yetmedigini soyleyerek tartisilanlari topluyor.",
            "coherence_cohesion": "Iki soru iki blok halinde ve her blogun ic sirasi gerekceli: once en dogrudan maliyet, sonra dolayli olan. Once, meanwhile, and by then gibi baglantilar anlam tasiyor, dolgu degil.",
            "lexical_resource": "Priced out of reach, commute, accumulate, redundant office space, claw back, short-staffed gibi ogeler dogal esdiziimle kullanilmis. Merely more tired gibi vurgu bicimleri ekonomik.",
            "grammatical_range_accuracy": "Ortac yapisi (pushing them into a long daily commute), iki noktali aciklama ve zit yapilar kontrollu. Hata seyrek; uzun cumleler okunurlugu bozmuyor.",
        }, "Onlemlerin hangisinin kisa hangisinin uzun vadede etki verecegini isaretlemek; sonuc paragrafi bunu ima ediyor ama soylemiyor."),
    ]),
    ("T2-15", [
        (5.0, T2_15_5, {
            "task_response": "Iki taraf da yaziliyor ama sonda hukum verilmiyor: both of them are important diyerek tarti sorusu yanitsiz birakiliyor, oysa gorev bir agirlik kararini istiyor. Buyukanne ornegi konuya bagli ama tek bir dezavantaji tekrar etmekten oteye gitmiyor.",
            "coherence_cohesion": "Firstly / Secondly / In conclusion sirasi var ve avantajlar ile dezavantajlar ayri paragraflarda, bu yuzden takip edilebiliyor. Dorduncu paragraf onceki paragrafa baglanmadan basliyor, ilerleme orada kopuyor.",
            "lexical_resource": "Good thing, bad thing, save the time, big advantage kaliplari tekrar ediyor; cevrim ici hizmet icin ozel tek bir oge yok. Enter to the system ve the work is finish bicim olarak yanlis.",
            "grammatical_range_accuracy": "Uyum ve tanimlik hatalari yaygin: many service is, the internet don't close, there is many disadvantage, the application have, a old person. Yapilar basit cumle ile and/also baglantisindan ibaret.",
        }, "Son paragrafi 'ikisi de onemli' yerine acik bir hukumle degistirmek: hangi taraf daha agir basiyor ve neden. Gorev tam olarak bunu soruyor."),
        (6.5, T2_15_65, {
            "task_response": "Hukum girişte kosuluyla birlikte veriliyor (avantajlar agir basiyor, ama alternatif kanal kalmak sartiyla) ve sonda ayni kosulla tekrarlaniyor. Avantajlar kimin icin gecerli oldugu belirtilerek anlatiliyor; dezavantaj bolumu dogru ama iki grupla sinirli kaliyor.",
            "coherence_cohesion": "Paragraf duzeni net: hukum, avantajlar, dezavantajlar, tarti. However ve Overall gecisleri dogru ama kalip; paragraf iclerinde baglanti moreover disina cikmiyor.",
            "lexical_resource": "Convenience, transaction, helpline, charges, non-digital gibi uygun ogeler var. Should not be minimised ve a poor replacement for a member of staff yerinde; find themselves unable biraz tekrar ediyor.",
            "grammatical_range_accuracy": "Ilgi cumlecikleri, kosul yapisi ve zit baglaclar dogru kurulmus; hatasiz cumle sayisi fazla. Ucte bire yakin cumlede hata var (who find very difficult to visit, who has never used, a part of this saving usually return, the difficulties falls, one non-digital way for doing); okuru durdurmuyorlar.",
        }, "Tartiyi sayiyla degil olcutle kurmak: hangi durumda avantaj agir basar, hangi durumda basmaz. Su an karar dogru ama gerekcesi tek cumlede."),
        (8.0, T2_15_8, {
            "task_response": "Hukum acik ve kosullu: avantajlar agir basiyor, ama yalnizca personelli bir alternatif acik kaldigi surece. Her iki taraf da kimin icin ne anlama geldigi ayrilarak veriliyor ve kapanista kosul kaldirildiginda dengenin tersine dondugu soyleniyor.",
            "coherence_cohesion": "Metin kazanc, kayip ve hukum olarak ilerliyor; her paragraf tek bir iddiayi tasiyor. Against this stands ve That conclusion carries a condition gibi gecisler bir onceki paragrafin sonucunu tasiyarak baglaniyor.",
            "lexical_resource": "Migrated to the screen, patchy rural connection, concentrated on a minority, staffed alternative gibi ogeler dogru ve dogal. Cannot be reasoned with secimi otomatik sistemin sorununu tek ifadede topluyor.",
            "grammatical_range_accuracy": "Devrik yapi (Against this stands...), noktali virgulle bagli karsitlik ve ic ice ilgi cumlecikleri kontrollu. Hata seyrek; son paragrafta kisa cumle bilincli olarak vurgu icin kullanilmis.",
        }, "Kayitlarin kalmasi gibi ikinci avantaji da bir sonucla baglamak; su an dogru ama diger gerekcelerden daha az gelistirilmis."),
    ]),
    ("T2-17", [
        (5.0, T2_17_5, {
            "task_response": "Sebep sorusu dort gerekceyle yanitlaniyor, ama ikinci soru olan olumlu mu olumsuz mu degerlendirmesi hicbir yerde yapilmiyor; sonuc paragrafi yalnizca sebepleri ozetliyor. Gorevin iki yariminin biri boylece bos kaliyor.",
            "coherence_cohesion": "Firstly / Secondly / Thirdly sirasi izlenebilir, ama dorduncu sebep Also I think ile numarasiz giriyor ve sonuc paragrafi yalnizca uc sebebi sayiyor; iskelet metinle ortusmuyor. Baglanti bu birkac kalibin disina hic cikmiyor.",
            "lexical_resource": "Old custom, young people, free time gibi gorevin kendi sozcukleri yeniden yazilmadan tekrar ediyor. Tradition disinda kulture ait oge yok; this activity is more easy ve lose the connection bicim ve esdiziim olarak zayif.",
            "grammatical_range_accuracy": "Uyum, tanimlik ve cogul hatalari sureklilesmis: the festival and the custom is, he work, he come, there is many other thing, a festival of two day. Yapilar basit cumle ve when/because baglantisiyla sinirli.",
        }, "Metnin sonuna degil ortasina bir degerlendirme paragrafi eklemek: bu degisim olumlu mu olumsuz mu ve neden. Sorunun ikinci yarisi su an hic yanitlanmiyor."),
        (6.5, T2_17_65, {
            "task_response": "Iki soru da yanitlaniyor: uc sebep sirasiyla veriliyor, degerlendirme ise acikca olumsuz olarak konuyor ve iki gerekceyle destekleniyor. Karsi tarafa kisa bir kabul de var, ama tek cumlede kaliyor ve hangi geleneklerin kaybolmayi hak ettigi ornekle acilmiyor.",
            "coherence_cohesion": "Bolumleme dogru: sebepler, degerlendirme, kabul, sonuc. Sebepler tek paragrafa yiginlmis ve The first reason / The second reason / Finally ile sayiliyor; bu paragraf ici ilerlemeyi mekaniklestiriyor.",
            "lexical_resource": "Migration, ceremony, crafts, generations, neglect gibi konuya uygun ogeler var. Practical knowledge ve passed from hand to hand yerinde; an enormous choice of entertainment biraz genel kaliyor.",
            "grammatical_range_accuracy": "Ilgi cumlecikleri, zaman cumlecikleri ve edilgen yapi dogru kullanilmis; hatasiz cumle sayisi fazla. Ucte bire yakin cumlede uyum ya da tanimlik hatasi var (A generation which grew up with screens have, an agricultural work, the contact between the old and the young become, some of them deserves); anlam bozulmuyor.",
        }, "Sebep paragrafini ikiye bolup en az birini ornekle acmak; su an uc sebep ayni paragrafta sirayla sayildigi icin hicbiri gelisemiyor."),
        (8.0, T2_17_8, {
            "task_response": "Sebepler yer, calisma duzeni ve anlam kaybi olarak ayrilip her biri kendi mekanizmasiyla anlatiliyor; degerlendirme ise once en guclu karsi arguman kabul edilerek, sonra kosullu bicimde olumsuz olarak veriliyor. Kapanis cumlesi hukmu degisim ile kayip arasindaki ayrima oturtuyor.",
            "coherence_cohesion": "Metin sebep, karsi arguman, hukum sirasiyla ilerliyor ve her paragraf tek bir isi yapiyor. Compound this ve even so gibi baglantilar onceki paragrafin sonucunu tasiyor; son cumle bastaki ifadeyi kapatiyor.",
            "lexical_resource": "Diaspora, shift work, observances, embedded, transmitted by imitation gibi ogeler dogru esdiziimle geciyor. An empty performance ve one generation of inattention gibi secimler ekonomik ve dogal.",
            "grammatical_range_accuracy": "Ortac yapilari, ilgi cumlecikleri ve karsitlik yapilari esnek bicimde donusuyor; son cumlenin devrik yapisi kontrollu. Hata seyrek ve okuru durdurmuyor.",
        }, "Kaybolan becerilerden birine somut bir ornek vermek; gerekce dogru kurulmus ama ornekle desteklenirse daha da agir basar."),
    ]),
]


def main():
    os.makedirs(HEDEF, exist_ok=True)
    for kod, cevaplar in VERI:
        answers = []
        for band, metin, neden, yukselt in cevaplar:
            n = _say(metin)
            if n < ALT_SINIR:
                raise SystemExit("%s band %s: %d kelime, %d'nin altinda"
                                 % (kod, band, n, ALT_SINIR))
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
