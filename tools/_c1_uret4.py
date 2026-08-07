# -*- coding: utf-8 -*-
"""Ornek cevap kutuphanesi - 4. grup: General Task 2 (T2-09, T2-11, T2-24, T2-53, T2-57).

Task 2 gorevleri module: "both" oldugu icin Academic / General ayrimi gorevin
kendisinde degil, secimde. 2. gruba (Academic Task 2) soyut ve kurumsal konular
alinmisti; bu gruba gunluk hayata bakan, adayin kendi deneyiminden ornek
verebilecegi konular secildi - ise alma, torun bakimi, evdeki yemek israfi,
oda paylasimi, disarida yemek. Bes soru kalibinin (opinion, discuss_both_views,
problem_solution, advantages_disadvantages, double_question) her birinden bir
gorev alindi ve 2. grubun konu alanlari (egitim, ulasim, sehir hayati, teknoloji,
kultur) tekrar edilmedi.

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


# ---------------------------------------------------------------- T2-24
# opinion / is hayati: ise alirken kisisel nitelikler mi diploma ve deneyim mi
T2_24_5 = """Nowadays when a company want to take a new worker, some people believe the personality is more important than the diploma and the experience. I am agree with this opinion because the character of a person is the most important thing in the work life.

Firstly, a good worker must be reliable. If a worker come late every morning and he don't finish his job in the time, the manager cannot trust him and all the team have a problem. Also the reliable person say the truth when he make a mistake, and this is very important for a company because the small problem don't become a big problem.

Secondly, a good worker must work with the other people. In every office the people work together in a team and if one person don't listen the others, the atmosphere become very bad. A person who is friendly and who help his colleague make the work more easy for everybody.

Also a good worker must be patient and polite with the customer. If the customer is angry and the worker answer him in a bad way, the company lose this customer and after the customer speak bad about the company with his friends.

On the other hand, the diploma is also a good thing because it show that the person study many years in the university. But in my opinion this paper don't say nothing about the character of the person.

In conclusion, I think the employer must look the personality of the candidate, because the good character is more important for the company and the office become a better place for everybody."""

T2_24_65 = """When a company has to choose between two candidates, some people argue that qualities such as reliability and the ability to work in a team count for more than certificates and years of experience. I largely agree with this view, although in some profession a formal qualification cannot be replaced by any personal quality.

The main reason is that technical knowledge can be taught at work, while character cannot. A new employee who does not know a particular program or a particular procedure can learn it in few weeks, because these things are written down and somebody in the office already knows them. An employee who does not come on time, or who cannot accept a comment about his work, will still be the same person after five years. Companies who ignore this often find themselves training a specialist who nobody want to sit next to.

Reliability also affect the whole team and not only one person. When a colleague does not finish his part of a project, the others must repair the situation in a hurry, and this costs the company far more than a small lack of experience would cost.

On the other hand, in several professions the qualification is not simply a paper. A nurse, a pilot or an electrician must hold a licence, because the law demand it and because a mistake can hurt somebody. In these case the employer is not free to prefer the pleasant candidate who has never been trained.

In conclusion, I agree that personal qualities should weigh more in the majority of jobs, but the qualification must come first where the safety and the law are concerned."""

T2_24_8 = """Employers rarely have the luxury of a candidate who is outstanding on every count, so the question of what to weigh most heavily is a real one. My own view is that dispositions such as reliability and a willingness to work with others should usually count for more than a qualification, because they are the part of a candidate that an employer cannot supply later.

Skills have a shelf life and a syllabus; temperament has neither. A recruit who has never used a particular accounting package can be brought up to speed in a fortnight by the colleague at the next desk, and within a year nobody remembers the gap. A recruit who treats deadlines as suggestions, or who cannot take a correction without sulking, imposes a cost on everyone around them for as long as they stay, and no training course reliably repairs it. Since one of these deficits is cheap to remedy and the other is not, a rational employer discounts the first and takes the second seriously.

Experience deserves a word in its own defence, though. It is not merely a stock of knowledge; it is judgement about which problems are worth worrying about, and that is genuinely hard to teach. A manager who dismisses it as a line on a form may well end up with a pleasant team that keeps repeating avoidable mistakes.

There is also a category of work where the argument does not apply at all. Nobody wants an amiable surgeon who has not qualified, and where a licence exists it exists for a reason.

On balance, then, character should be the tie-breaker rather than the entry ticket."""

# ---------------------------------------------------------------- T2-09
# discuss_both_views / aile ve toplum: cocugu buyukanne mi ebeveyn mi buyutmeli
T2_09_5 = """In many family the grandparent and the uncle help for grow the children, and other people think only the mother and the father must do this job. I want to write about the two opinion and after my opinion also.

Firstly, the grandparents are very useful for the family. They have a big experience because they grow their own children before, and they know what to do when the baby is sick or when the child don't want to eat. Also the parents today work all the day and they come home very late, so the grandmother can take the child from the school and give him the dinner. In my family my grandmother stay with me every afternoon when I was a child and I learn many thing from her, for example she tell me the story of our village and she teach me how to make a bread. In the summer we go in her house and all my cousin was there, and she cook for all the people every day and nobody was tired of this. This is a memory very beautiful for me and I think every child must have this chance.

Secondly, some people say only the parents must grow the child. I don't agree with this because the parents don't have the time and the child stay alone in the house with the telephone.

In conclusion, in my opinion the grandparents and the other relative must help the parents, because the family is the most important thing in the life and the child become a better person with them."""

T2_09_65 = """In some societies children are brought up by a whole group of relatives, while in others this is considered the job of the mother and the father only. Both arrangements have their defenders, and in my opinion the answer depends on how the two sides share the decisions.

Those who defend the role of grandparents and other relative usually mention experience and time. A grandmother who has already raised three children is not frightened from a fever at two o'clock in the morning, and she can pass to the child many things that the parents are too tired to teach: how to prepare a traditional dish, or simply how the family lived thirty years ago. In many countries this help is also a financial question, because a nursery is expensive and not every couple can afford it.

The other view is that too many adults around a child create confusion. If the mother says that the television must be closed at eight o'clock and the grandfather allows two more hour, the child learns very quickly to ask the person who says yes. There is also the problem of the responsibility: when everybody looks after the child, sometimes nobody really does, and the parents lose the habit to decide alone.

Personally, I believe that relatives should be involved, but inside the limits that the parents fix. Help with the transport, the meals or the homework is valuable, especially when both parents work full time, but the rules about the sleep, the money and the school should come from one place only.

In conclusion, the two positions are not really opposite. The family can be as large as it wants, on condition that the authority stay clear."""

T2_09_8 = """How much of a child's upbringing should fall to grandparents, aunts and uncles is a question that different societies answer very differently, and there is something to be said for both answers.

The case for a wide circle rests on more than convenience, though convenience matters: in households where two adults work full time, a grandparent collecting a child from school is often what makes the whole arrangement possible. Beyond that, relatives carry things parents are badly placed to pass on. A grandmother is under no obligation to be consistent about bedtime, and that frees her to talk about the past, teach a recipe nobody ever wrote down, or simply be patient at seven in the evening in a way an exhausted parent cannot manage.

The opposing case is about lines of authority rather than affection. A child who works out that one adult forbids what another permits will stop treating either as final, and the negotiations that follow exhaust everybody. There is a subtler cost too: when help is constant and unspoken, parents drift into deferring on decisions that are properly theirs, and taking them back later is awkward.

My own view sits between the two, but not in the middle. I would keep relatives closely involved and set no limit on the hours they give, while reserving to the parents the small set of decisions that shape a child's habits: sleep, screens, money, school. The distinction is between sharing the work and sharing the authority, and the two are far easier to separate in advance than in the middle of a disagreement.

That, rather than the size of the household, seems to me to decide whether a child is raised well."""

# ---------------------------------------------------------------- T2-11
# problem_solution / tuketim: hanelerde yemek israfi
T2_11_5 = """Today in many house the people buy a lot of food and after they throw it in the bin without eat it. This is a very big problem for all the world and I want to explain the problem and after the solution.

Firstly, the money of the family go in the bin. When a family throw the half of the vegetable and the bread every week, at the end of the month this is a big money, and after the same people say they don't have enough money for the other thing like the clothes or the holiday.

Secondly, this situation is very bad because in the same time in many country the people don't have nothing to eat. The children in the poor country sleep with the stomach empty and in the rich country the good food go in the bin every day. This is not correct and all the people must think about this problem. In some place the people die because they cannot find a bread and this is a shame for our century.

Also the rubbish become more and more every year and the truck must take all this rubbish outside of the city.

For the solution, in my opinion the government must do something and make a law for the supermarket. Also the people must be more careful when they do the shopping.

In conclusion, the waste of the food is a big problem for the money of the family and for the poor people, and the government and the people must find a solution together for stop this situation."""

T2_11_65 = """In many homes a considerable part of the food that is bought finishes in the bin. This creates problems both for the family budget and for the environment, and there are several measure that could reduce it.

The first problem is a financial one. A household that throws away vegetables, bread and dairy products every week is losing money that it could spend on something else, and because the loss arrives in very small quantities nobody notice how large it becomes over a year. The families who complain most about the price of the food are often the same families who empty half of the fridge on Sunday evening.

The second problem is less visible. Every tomato that is thrown away was grown with water, carried with fuel and kept cold in a shop, and all of this effort is lost at the moment the fruit goes in the bin. The waste then arrives in the landfill, where the organic material produce gas and the local council must pay for treat it.

Several measures could improve the situation. At home, the simplest one is to plan the week before going to the supermarket and to shop with a short list, because most of the excess is bought without any intention. Shops could help by selling smaller portions and by explaining the difference between the two date that appear on the label, which many customer confuse. Schools could also teach children how to use the food that is already in the kitchen instead of buying a new one.

In conclusion, food waste costs money and resources, and it can be reduced by better planning at home, clearer information in the shops and some education at school."""

T2_11_8 = """Anyone who has cleared out a fridge on a Sunday evening knows how much of the weekly shop never gets eaten. The scale of it is easy to underestimate, and the consequences reach further than the household that pays for them.

The most immediate problem is financial, and it falls hardest on the people least able to absorb it. Waste arrives in instalments — a bag of salad here, half a loaf there — so it never presents itself as a single painful sum, yet across a year it amounts to a substantial share of what a family spends on food. That invisibility is precisely what makes the habit so persistent.

The environmental cost is larger and even less obvious. A discarded cucumber represents water drawn for irrigation, fuel burned in transport and electricity spent keeping it cold in a shop, all of it expended for nothing. Buried in landfill, the same cucumber then decomposes without oxygen and releases methane, so the waste is charged twice: once when the food is produced and again when it rots.

Remedies exist at every level, and none of them depends on people simply resolving to do better. Households waste least when they shop from a list and store food properly, both of which are habits rather than acts of willpower. Retailers can offer smaller pack sizes and stop printing two different dates on a label, since a great deal of perfectly edible food is thrown out on the strength of a misread 'best before'. Local authorities can make separate food collection routine, which turns the waste into compost and, incidentally, shows households how much they are producing.

None of this removes the problem, but together the measures would cut it sharply."""

# ---------------------------------------------------------------- T2-53
# advantages_disadvantages / yaslanan nufus: dusuk kirayla oda karsiligi yardim
T2_53_5 = """In some city the young people can stay in the house of a old person and pay a small rent, and in exchange they help him and make company to him. I want to write the advantage and the disadvantage of this system.

Firstly, the advantage is the money. Today the rent in the big city is very expensive and a young person who start to work cannot pay it alone. In my city the price of the flat become more high every year and the young people must live with the parents until thirty years old. This is a big problem for all the country and the government must build more house for the young generation and control the price.

Also the old person is happy because he is alone in the big house and he cannot do nothing without a help. He cannot go to the market, he cannot clean the house and he don't speak with nobody all the day, so a young person in the house is very good for him.

Secondly, the disadvantage is the privacy. Two person from different generation live in the same house and they don't have the same habit, for example the young person come home late in the night and the old person sleep early. Also they don't eat the same food and they don't watch the same programme in the television, so after some month they can have a big discussion.

In my opinion the advantage and the disadvantage are both important and every person must decide alone what is better for his own situation."""

T2_53_65 = """In several countries an older person with a spare room can offer it to a young adult for a very low rent, in exchange for company and some help with the daily task. In my opinion this arrangement brings more benefits than problems, but only if the two sides agree clearly from the beginning what is expected.

The advantages are easy to see. A student or a young employee obtains a room in a city where the normal rents are impossible for him, and in exchange he gives few hours a week that cost him no money at all. The older person receives practical help with the shopping, the computer or the garden and, what is more important, the house is not silent in the evening. Thanks to this, many people can stay in their own home several years longer instead of moving in a residence.

There are however real disadvantages. Two adults who did not choose each other must share a kitchen and a bathroom, and their habits are usually not the same: the hours, the noise, the visits of the friends. The limit of the help is another difficulty. If it is written nowhere, the young person can slowly become a nurse, and it is very hard to say no to a person who give you a cheap room.

For this reason I think the advantages are stronger, but the arrangement need a frame. A written agreement about the number of hour, a trial period of one month and an association that follows the two sides would remove most of these risks.

In conclusion, this system helps two groups that both need something, on condition that it is organised and not based only on the good will."""

T2_53_8 = """Schemes that place a young adult in an older person's spare room, at a token rent and in return for company and small practical favours, have spread quickly in cities where housing is scarce. Weighed carefully, I think the advantages do outweigh the drawbacks, though the margin depends almost entirely on how the arrangement is set up.

What the young person gains is obvious enough: a room within reach of work or study at a price no ordinary tenancy could match. What the older person gains is more interesting. It is rarely rescue from helplessness — most of the people who take part manage perfectly well — but a lift with the weekly shop, someone who notices when the boiler starts sounding wrong, and the ordinary noise of another life in the house. Between them, those things can postpone by years the decision to leave a home somebody has lived in for decades.

The difficulties are equally concrete. Two people who did not choose each other are sharing a kitchen, and habits diverge sharply across fifty years: sleeping hours, visitors, what counts as tidy. More seriously, the help has no natural boundary. What begins as carrying shopping drifts towards personal care, and a lodger who owes their rent to goodwill is poorly placed to object.

That drift, however, is a failure of design rather than of the idea itself. Where a broker matches the pair, the hours are written down and either side may withdraw after a trial month, the arrangement tends to hold.

So the balance tips positively, but conditionally: the scheme works because of its structure, and an informal version of it, arranged privately between strangers, would deserve a good deal more caution."""

# ---------------------------------------------------------------- T2-57
# double_question / saglik: disarida yemek ve hazir yiyecek
T2_57_5 = """Today the people in many country eat in the restaurant and the cafe or they buy a food ready for heat in the microwave, and they don't cook in the house like before. In this essay I explain the reason of this situation.

Firstly, the people don't have the time. They work all the day and when they come in the house at eight o'clock in the evening they are very tired and they don't want to stay one hour in the kitchen for prepare a dinner. It is more easy to open a box and put it in the microwave for five minute, and after the dinner they must also wash all the plate and the pan and this is a other work.

Secondly, the ready food is not expensive now. Before, the restaurant was only for the special day like the birthday, but today in every street there is a small place where a person can eat with a little money. Also the telephone application bring the food in the door of the house and the person don't move from the sofa.

Thirdly, many young people don't know how to cook because nobody teach them. In the past the girl learn in the kitchen with the family but now everybody study and work and nobody have the time for teach this thing, and after they marry they continue to buy the same box every evening.

In my opinion this is a negative development because the ready food is not healthy."""

T2_57_65 = """In a growing number of countries families eat outside or buy dishes that only need to be heated, instead of preparing the meal at home. There are clear reasons for this change and, although it has some good sides, I consider it mostly negative.

The first reason is the working day. In many cities people leave the house at seven and come back after eight, and after such a day very few of them have the energy for cook a meal from the beginning and wash the pans afterwards. A second reason is the price: prepared dishes and small restaurants have become much cheaper than before, so eating outside is no more an event reserved to a birthday. Delivery applications have also made the whole process extremely simple, and finally many young adults have never learn to cook, because nobody at home had the time to show them.

There are certainly some advantage. The time that is saved goes to the children or to the rest that the parents need, and people discover dishes from other country that they would never prepare themselves.

However, the negative effects seem to me stronger. When somebody else cooks, the customer has no control on the quantity of salt, sugar and oil, and these quantities are much higher than at home, which affects the health after some years. The cost is also higher in the long term, even if each meal look cheap. Above all, a skill that was transmitted from one generation to the other is disappearing, and a person who cannot cook has no choice at all.

In conclusion, the change is understandable, but in my opinion its disadvantages weigh more than its advantages."""

T2_57_8 = """The kitchen is being used less and less. In a growing number of households dinner arrives ready to heat or is eaten in a café, and the reasons for that are not hard to identify.

Working patterns come first. When both adults leave before eight and return after seven, cooking competes with the only free hours of the day, and it loses. Prepared food has also become genuinely cheap relative to income, so eating out no longer marks an occasion, and delivery platforms have removed even the walk to the restaurant. Underneath all this sits a quieter cause: a generation is reaching adulthood without having watched anyone cook, and a skill that is never demonstrated is not acquired.

Some of the consequences are welcome. Time released from the stove goes somewhere, usually to children or to rest, and the range of food an ordinary household eats is far wider than it was a generation ago. There is a fairness argument too, since the burden of cooking every evening has historically fallen on women.

Even so, I regard the trend as negative overall. Handing the cooking to somebody else means handing over control of salt, sugar and fat, which are used far more generously in a commercial kitchen than in a domestic one, and the effects accumulate quietly across decades rather than announcing themselves. The economics are worse than they look, too: each individual meal seems affordable, while the monthly total rarely is. Most importantly, a household that cannot cook has lost the ability to choose, and that loss is not easily reversed once a generation has passed.

Convenience, in short, has been bought at a price that is real but deferred."""


VERI = [
    ("T2-24", [
        (5.0, T2_24_5, {
            "task_response": "Tutum ilk paragrafta acikca konuyor ama gorevin asil istedigi karsilastirma yapilmiyor: metin bastan sona iyi bir calisanin ozelliklerini siraliyor, diploma ve deneyim yalnizca bir cumlede aniliyor ve neden daha hafif bastigi hicbir yerde tartisilmiyor. Somut bir is ornegi de verilmedigi icin gerekceler genel kaliyor.",
            "coherence_cohesion": "Firstly / Secondly / Also / On the other hand / In conclusion iskeleti okuru kaybettirmiyor ve her paragrafin bir konusu var. Baglantiyi bu bes kalip disinda hicbir sey tasimiyor; paragraf iclerinde fikir ornekle degil tekrarla uzatiliyor.",
            "lexical_resource": "Important, good worker, the company ogeleri surekli tekrar ediyor; ise alim alanina ait tek bir ozel sozcuk yok (candidate disinda). The diploma, the personality gibi secimler soruyu oldugu gibi geri veriyor.",
            "grammatical_range_accuracy": "Neredeyse her cumlede uyum, tanimlik ya da olumsuzluk hatasi var: a company want, I am agree, a worker come late, he don't finish, the team have, this paper don't say nothing. If ve who cumlecikleri deneniyor ama gerisi basit ve kisa cumle."
        }, "Her paragrafa 'bu nitelik diplomadan neden daha agir basiyor' sorusunu yanitlayan tek bir cumle eklemek; su haliyle metin karsilastirma degil, ozellik listesi."),
        (6.5, T2_24_65, {
            "task_response": "Tutum giriste kosuluyla birlikte veriliyor (cogu iste nitelikler agir basar, meslek belgesi gerekli olan islerde basmaz) ve sonuc ayni kosulu tekrarliyor; karsilastirma gercekten yapiliyor cunku ogretilebilirlik olcutu ustunden yurutuluyor. Ikinci gerekce (ekip maliyeti) iki cumleye sikismis ve ornekle acilmamis.",
            "coherence_cohesion": "Paragraf duzeni net: tutum, ana gerekce, ikinci gerekce, karsi durum, sonuc; her paragrafin tek merkezi var. The main reason is / On the other hand / In conclusion gecisleri dogru ama tahmin edilebilir, baglanti icerikten degil kaliptan geliyor.",
            "lexical_resource": "Qualification, certificate, procedure, licence, candidate gibi alanin ogeleri dogru kullanilmis. Count for more, repair the situation ve a small lack of experience esdiziim olarak tam oturmuyor.",
            "grammatical_range_accuracy": "Ilgi cumlecigi, zaman ve kosul cumlecikleri kuruluyor, uzun cumleler dagilmiyor. Cumlelerin yarisinda tekil-cogul ya da uyum hatasi var (in some profession, in few weeks, who nobody want, Reliability also affect, the law demand it, in these case); hicbiri anlami engellemiyor."
        }, "Ekip maliyeti paragrafina bir ornek koymak - projeyi geciktiren tek kisinin otekilere ne yaptirdigi gosterilirse gerekce ikinci bir tekrar olmaktan cikar."),
        (8.0, T2_24_8, {
            "task_response": "Tutum bir olcute baglanarak kuruluyor - isverenin sonradan saglayabilecegi sey beceri, saglayamayacagi sey mizac - ve bu olcut metnin sonuna kadar tasiniyor. Deneyim lehine gercek bir itiraz kabul ediliyor ve lisans gerektiren isler ayri bir kategori olarak disarida birakiliyor.",
            "coherence_cohesion": "Paragraflar tez, gerekce, itiraf edilen itiraz, istisna ve tartili hukum olarak ilerliyor. Baglanti Since one of these deficits / though / then gibi ogelerle cumlenin isini yaparak kuruluyor, basa yapistirilan isaretlerle degil; son cumle bastaki agirlik metaforunu kapatiyor.",
            "lexical_resource": "Dispositions, shelf life and a syllabus, temperament, brought up to speed, a fortnight, amiable, tie-breaker gibi az kullanilan ogeler dogru esdiziimle geciyor. Discounts the first ve entry ticket secimleri ekonomik ve dogal.",
            "grammatical_range_accuracy": "Noktali virgulle kurulan karsitlik, ic ice ilgi cumlecikleri ve Since ile acilan gerekce yapisi kontrollu. Hata seyrek ve okuru durdurmuyor; yine de band 9'un tam esnekligi yok."
        }, "Deneyim paragrafi otekilerden ince kaliyor: 'hangi sorunun onemli oldugunu bilmek' iddiasi tek somut durumla gosterilse tez daha da sikisir."),
    ]),
    ("T2-09", [
        (5.0, T2_09_5, {
            "task_response": "Gorev iki gorusun de tartisilmasini istiyor, ama ikinci gorus tek paragrafta anilip iki cumlede reddediliyor - savunulmadigi icin tartisilmis sayilmiyor. Birinci gorus ise yarisindan sonra kendi ailesinin anisina donuyor ve koy hikayesi, ekmek, yaz tatili gibi ayrintilar soruyla ilgisiz.",
            "coherence_cohesion": "Firstly / Secondly / In conclusion iskeleti var ve okur nerede oldugunu biliyor. Ikinci paragraf ic duzenini kaybediyor: destek, deneyim ve kisisel ani ayni yerde birikiyor, cumleler ve baglaciyla yan yana diziliyor.",
            "lexical_resource": "Grow the children ve grow the child yanlis sozcuk secimi ve metnin merkezinde tekrar ediyor. Very useful, very beautiful, many thing kaliplari surekli donuyor; cocuk yetistirme alanina ait tek bir ozel oge yok.",
            "grammatical_range_accuracy": "Hemen her cumlede uyum, tanimlik, zaman ya da cogul hatasi var: in many family, the two opinion, the child don't want, I learn many thing, all my cousin was there, the child become. Zaman kaymasi ozellikle anlati paragrafinda surekli (stay / was / learn / tell)."
        }, "Ikinci gorusu reddetmeden once savunmak: neden bazi ailelerin bu isi yalniz yapmak istedigini bir paragrafta anlatmak, gorev metnin bir yarisini bosluk olmaktan cikarir."),
        (6.5, T2_09_65, {
            "task_response": "Iki gorus de kendi paragrafinda, kendi gerekcesiyle ve somut ornekle veriliyor (gece atesi, sekiz televizyon kurali); kendi gorus ayri bir paragrafta ve kosullu bicimde soyleniyor, sonucta ayni kosul tekrarlaniyor. Ikinci gorusun sorumluluk yarisi ise ornekle acilmadan geciliyor.",
            "coherence_cohesion": "Metin gorus, karsi gorus, kendi gorusu, sonuc sirasiyla duzgun ilerliyor ve her paragraf tek is yapiyor. The other view is that / Personally / In conclusion gecisleri etiket gibi duruyor, son paragraf da onceki paragrafi biraz tekrar ediyor.",
            "lexical_resource": "Brought up, nursery, afford, arrangement, defenders gibi konuya uygun ogeler dogru yerde. The television must be closed ve the authority stay clear esdiziim olarak yanlis, pass to the child da devrik duruyor.",
            "grammatical_range_accuracy": "Kosul cumleleri, ilgi cumlecikleri ve iki noktali aciklama yapisi dogru kuruluyor. Cumlelerin yarisindan biraz fazlasinda cogul, edat ya da uyum hatasi var (other relative, frightened from a fever, two more hour, the habit to decide, inside the limits, the authority stay clear); anlam hicbir yerde kaybolmuyor."
        }, "Sorumluluk dagilmasi fikrini bir ornekle acmak - kimin karar verdigi belirsizken neyin aksadigi gosterilse ikinci gorus birinciyle esit agirliga cikar."),
        (8.0, T2_09_8, {
            "task_response": "Iki gorus de en guclu haliyle kuruluyor: genis aile lehine yalniz kolaylik degil, ebeveynin yapamayacagi aktarim; karsi taraf lehine ise sevgi degil yetki cizgisi. Kendi gorus 'arada ama ortada degil' diye acikca konumlaniyor ve isi paylasmak ile yetkiyi paylasmak ayrimiyla somutlasiyor.",
            "coherence_cohesion": "Paragraflar tek merkezli ve sirali; her biri bir oncekinin biraktigi yerden devam ediyor. Beyond that, There is a subtler cost too ve son cumlenin That, rather than... yapisi baglantiyi icerikle tasiyor, isaret sozcugu yapistirmadan.",
            "lexical_resource": "Upbringing, lines of authority, deferring, badly placed to pass on, a recipe nobody ever wrote down gibi ogeler hem az kullanilan hem de dogal. Under no obligation to be consistent secimi fikri tek ifadede tasiyor.",
            "grammatical_range_accuracy": "Ilgi cumlecikleri, ortac yapilari, iki noktali siralama ve devrik vurgu esnek bicimde donuyor. Hata seyrek ve okuru durdurmuyor; band 9'un butun rahatligina ulasmiyor."
        }, "Yetki listesi (uyku, ekran, para, okul) verilirken bunlardan birinin cakismasi tek cumleyle gosterilse ayrim soyut olmaktan tumuyle cikar."),
    ]),
    ("T2-11", [
        (5.0, T2_11_5, {
            "task_response": "Gorev iki sey istiyor: sorunlar ve onlemler. Sorunlar bolumu ucuncu paragrafta aclik konusuna kayiyor ve orada uc cumle kaliyor, onlemler bolumu ise iki desteksiz cumleden ibaret (devlet bir yasa yapmali, insanlar dikkatli olmali) - gorevin yarisi bos.",
            "coherence_cohesion": "Firstly / Secondly / Also / For the solution / In conclusion siralamasi okuru yonlendiriyor ama onlemler paragrafinda iskelet iceriksiz kaliyor. Aclik paragrafi konuyu degistirdigi icin metnin ortasinda ilerleme kopuyor.",
            "lexical_resource": "Big problem, very bad, a lot of kaliplari tekrar ediyor; israf ya da atik alanina ait tek bir ozel oge yok. The waste of the food ve do the shopping gibi secimler gunluk konusma duzeyinde kaliyor.",
            "grammatical_range_accuracy": "Hemen her cumlede hata var: in many house, without eat it, the money go, they don't have nothing, the rubbish become, for stop this situation. Cift olumsuzluk ve mastar yerine yalin fiil kullanimi metin boyunca tekrarliyor."
        }, "Onlemler bolumunu ayri bir paragrafa cikarip her onlemin kimin ne yapacagini soylemek; su an iki dilek cumlesi gorevin yarisini karsiliyor gorunuyor."),
        (6.5, T2_11_65, {
            "task_response": "Iki soru da ayri bolumlerde yanitlaniyor: iki sorun neden-sonuc zinciriyle veriliyor (kucuk kayiplarin fark edilmemesi, uretim icin harcanan kaynagin bosa gitmesi) ve onlemler hane, magaza, okul olmak uzere uc ayri duzeyden geliyor. Cop sahasi ve gaz kismi tek cumleye sikismis, otekiler kadar acilmamis.",
            "coherence_cohesion": "The first problem / The second problem / Several measures / In conclusion iskeleti duzenli ve paragraflar iceride gercekten gelisiyor. Gecisler yine de kalip duzeyinde kaliyor; onlemler paragrafi uc onlemi ayni cumle bicimiyle art arda diziyor.",
            "lexical_resource": "Landfill, organic material, dairy products, portions, excess, budget gibi konuya ait ogeler dogru kullanilmis. Arrives in the landfill, the loss arrives in very small quantities ve finishes in the bin esdiziim olarak tam oturmuyor.",
            "grammatical_range_accuracy": "Ilgi cumlecikleri, edilgen yapi ve zaman cumlecikleri dogru kuruluyor, uzun cumleler dagilmiyor. Cumlelerin yaklasik yarisinda cogul ya da uyum hatasi var (several measure, nobody notice, the material produce, the two date, many customer, pay for treat it); anlam bozulmuyor."
        }, "Cop sahasi sorununu ikinci paragrafa somut bir sonucla baglamak - gazin nereye gittigi ya da belediyeye ne kadara mal oldugu soylenirse ikinci sorun birincisi kadar agir basar."),
        (8.0, T2_11_8, {
            "task_response": "Iki sorun da mekanizmasiyla anlatiliyor: mali kayip taksitle geldigi icin gorunmez oluyor, cevresel maliyet ise hem uretimde hem curumede iki kez odeniyor. Onlemler uc ayri duzeyden geliyor ve her biri neden ise yaradigini kendi icinde soyluyor; 'insanlar dikkatli olsun' turu bos onlem bilincli olarak reddediliyor.",
            "coherence_cohesion": "Paragraflar sorun, sorun, cozum, hukum sirasiyla ilerliyor ve her birinin tek merkezi var. That invisibility, the same cucumber, together the measures gibi geri gonderimler baglantiyi tasiyor; hicbir paragraf isaret sozcugune ihtiyac duymuyor.",
            "lexical_resource": "Instalments, irrigation, decomposes without oxygen, methane, pack sizes, compost gibi az kullanilan ogeler dogru esdiziimle geciyor. Charged twice ve a misread 'best before' secimleri fikri tek ifadede tasiyor.",
            "grammatical_range_accuracy": "Cizgi ile araya giren yapi, ortac basli cumleler, iki noktali aciklama ve since ile kurulan gerekce kontrollu bicimde donuyor. Hata seyrek ve okuru durdurmuyor; band 9 hedeflenmiyor."
        }, "Belediye onlemi otekilerden kisa kaliyor: ayri toplamanin haneye neyi gosterdigi bir cumleyle acilirsa uc onlem esit agirlikta olur."),
    ]),
    ("T2-53", [
        (5.0, T2_53_5, {
            "task_response": "Gorev acik bir hukum bekliyor - avantajlar agir basiyor mu - ama son paragraf 'ikisi de onemli, herkes kendi durumuna gore karar versin' diyerek hukmu vermiyor. Ustelik ilk paragrafin yarisi konut fiyatlari ve devlet politikasina kayiyor, ve yasli kisi bastan sona yardima muhtac varsayiliyor.",
            "coherence_cohesion": "Firstly / Also / Secondly / In my opinion siralamasi var ama Firstly avantaji, Secondly dezavantaji karsiliyor; sayilar iki farkli listeyi ayni diziye koydugu icin okur yapiyi kalibin kendisinden degil iceriginden cikariyor. Paragraf iclerinde fikir ornekle degil tekrarla uzuyor.",
            "lexical_resource": "Make company to him, the price become more high, a big discussion gibi secimler yanlis; the advantage ve the disadvantage sorudan alinip degistirilmeden tekrarlaniyor. Konut ya da paylasim alanina ait tek bir ozel oge yok.",
            "grammatical_range_accuracy": "Hemen her cumlede hata var: in some city, a old person, a person who start, he cannot do nothing, two person from different generation, after some month. Cift olumsuzluk ve tekil-cogul karisikligi metin boyunca surekli."
        }, "Son paragrafta hangi tarafin agir bastigini bir cumleyle soylemek; su an iki liste yazilmis ama gorevin sordugu hukum hic verilmemis."),
        (6.5, T2_53_65, {
            "task_response": "Hukum giriste veriliyor, kosuluyla birlikte (avantajlar agir basar, ama iki taraf bastan anlasirsa) ve son paragrafta ayni kosul tekrarlaniyor; iki taraf da kendi paragrafinda tartisiliyor. Yardimin sinirinin belirsizligi guclu bir dezavantaj olarak kuruluyor, arkadaslik yani ise tek cumlede kaliyor.",
            "coherence_cohesion": "The advantages are easy to see / There are however real disadvantages / For this reason iskeleti net ve her paragraf tek is yapiyor. Gecisler kalip duzeyinde; ucuncu paragraf iki ayri dezavantaji ayni yerde toplayip araya kisa bir baslik cumlesi koyarak ilerliyor.",
            "lexical_resource": "Spare room, trial period, arrangement, tenancy yerine kullanilan rent, association gibi ogeler yerinde. Make more benefits, based only on the good will ve moving in a residence esdiziim ve edat olarak tam oturmuyor.",
            "grammatical_range_accuracy": "Ilgi cumlecikleri, kosul cumlecikleri ve on condition that yapisi dogru kuruluyor. Cumlelerin yarisindan biraz fazlasinda cogul, tanimlik ya da uyum hatasi var (the daily task, gives few hours, moving in a residence, a person who give you, the arrangement need, the number of hour); anlam engellenmiyor."
        }, "Yasli kisinin kazanci somut bir gunluk ornekle gosterilmeli - su an 'ev aksam sessiz degil' cumlesi avantaj listesinin en zayif halkasi."),
        (8.0, T2_53_8, {
            "task_response": "Hukum acik ve kosullu: avantajlar agir basiyor ama fark duzenlemenin bicimine bagli. Iki taraf da somut olarak veriliyor ve yaslinin kazanci bilincli olarak 'caresizlikten kurtarilma' varsayimindan ayriliyor; dezavantaj ise fikrin degil tasarimin kusuru olarak yeniden cerceveleniyor.",
            "coherence_cohesion": "Paragraflar giris ve hukum, avantajlar, dezavantajlar, tasarim itirazi, kosullu kapanis olarak ilerliyor. Between them, those things / That drift, however gibi geri gonderimler her paragrafi bir oncekine bagliyor; son cumle bastaki kosulu kapatiyor.",
            "lexical_resource": "Token rent, tenancy, lodger, broker, diverge sharply, poorly placed to object gibi az kullanilan ogeler dogru esdiziimle geciyor. Notices when the boiler starts sounding wrong ve the ordinary noise of another life secimleri hem ekonomik hem dogal.",
            "grammatical_range_accuracy": "What... is yapisi, cizgi arasi ekleme, ortac basli cumle ve Where ile kurulan kosul esnek bicimde donuyor. Hata seyrek ve okuru durdurmuyor; band 9'un tam rahatligi yok."
        }, "'Reported outcomes are good' turu genel ifade metnin en zayif halkasi; hangi tarafin neyi bildirdigi soylenirse hukum daha saglam durur."),
    ]),
    ("T2-57", [
        (5.0, T2_57_5, {
            "task_response": "Gorevin iki yarisi var: sebepler ve degerlendirme. Sebepler duzgun bicimde uc paragrafta veriliyor, ama olumlu mu olumsuz mu sorusu tek desteksiz cumleyle kapatiliyor ve o cumle konuyu 'hazir yiyecek sagliksizdir' cumlesine indirgiyor - gorevin ikinci yarisi karsilanmiyor.",
            "coherence_cohesion": "Firstly / Secondly / Thirdly iskeleti duzenli ve her sebep kendi paragrafinda. Degerlendirme icin hicbir gecis kurulmuyor: son cumle metne baglanmadan yapistirilmis, sonuc paragrafi yok.",
            "lexical_resource": "The people, the food, very tired, a little money kaliplari tekrar ediyor; beslenme ya da hazir gida alanina ait ozel bir oge yok. Ready for heat ve telephone application gibi secimler yanlis kurulmus.",
            "grammatical_range_accuracy": "Hemen her cumlede hata var: in many country, a food ready for heat, for prepare a dinner, for five minute, the application bring, nobody have the time. Cogul ve tanimlik hatalari ile for + yalin fiil kalibi metin boyunca tekrarliyor."
        }, "Son cumleyi bir paragrafa cevirip hem olumlu hem olumsuz yani tartmak; su an sebepler yaziliyor ama sorulan hukum verilmemis sayiliyor."),
        (6.5, T2_57_65, {
            "task_response": "Iki soru da yanitlaniyor: dort sebep sirasiyla veriliyor ve hukum giriste ve sonucta acikca olumsuz. Olumsuz yan uc gerekceyle acilirken olumlu yan iki cumlede kaliyor, bu yuzden tarti tek tarafli duruyor.",
            "coherence_cohesion": "The first reason / A second reason / There are certainly / However / In conclusion siralamasi net ve paragraflar iceride gelisiyor. Sebepler paragrafi dort sebebi tek yerde topluyor, son ikisi ayni cumleye siginiyor; gecisler kalip duzeyinde.",
            "lexical_resource": "Prepared dishes, delivery applications, in the long term, quantity of salt gibi konuya uygun ogeler dogru kullanilmis. No more an event reserved to a birthday, goes to the rest that the parents need ve transmitted from one generation to the other esdiziim olarak tam oturmuyor.",
            "grammatical_range_accuracy": "Zaman cumlecikleri, ilgi cumlecikleri ve although yapisi dogru kuruluyor, uzun cumleler dagilmiyor. Cumlelerin yarisindan biraz fazlasinda edat, cogul ya da fiil bicimi hatasi var (energy for cook, reserved to a birthday, have never learn, some advantage, from other country, no control on, each meal look); anlam engellenmiyor."
        }, "Olumlu yani ucuncu bir gerekceyle acmak - kazanilan zamanin nereye gittigi somutlastirilirsa hukum tek tarafli degil, tartilmis gorunur."),
        (8.0, T2_57_8, {
            "task_response": "Sebepler calisma duzeni, fiyat, teslimat ve aktarilmayan beceri olarak ayrilip her biri kendi mekanizmasiyla veriliyor. Degerlendirme once olumlu yani gercekten kabul ederek - kazanilan zaman ve ev isi yukunun paylasimi - sonra uc gerekceyle olumsuz olarak veriliyor; hukum son cumlede ertelenmis maliyet fikrine oturuyor.",
            "coherence_cohesion": "Metin sebepler, olumlu yan, olumsuz yan, hukum sirasiyla ilerliyor ve her paragraf tek is yapiyor. Underneath all this sits a quieter cause ve Even so gibi ogeler baglantiyi cumlenin kendi isiyle kuruyor; kapanis bastaki mutfak imgesine donuyor.",
            "lexical_resource": "Working patterns, relative to income, delivery platforms, commercial kitchen, accumulate quietly, deferred gibi az kullanilan ogeler dogru esdiziimle geciyor. A skill that is never demonstrated is not acquired secimi fikri tek cumlede tasiyor.",
            "grammatical_range_accuracy": "Devrik yapi, iki noktali aciklama, while ile kurulan karsitlik ve edilgen ogeler kontrollu bicimde donuyor. Hata seyrek ve okuru durdurmuyor; band 9'un tam esnekligi yok."
        }, "Adalet argumani tek cumlede birakilmis; kimin yukunun nasil degistigi bir adim acilirsa olumlu taraf hukmu daha cok zorlar."),
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
