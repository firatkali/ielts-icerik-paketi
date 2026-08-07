# -*- coding: utf-8 -*-
"""Ornek cevap kutuphanesi - 5. grup: Academic Task 1 (AT06-AT08) + Academic Task 2 (T2-44, T2-39).

KONTROL.md'deki alti calistirmalik dagilim tablosu bu gruba uc Academic Task 1
gorevi ve iki Task 2 gorevi veriyor. Task 1 tarafinda AT01-AT05'ten sonraki uc
gorev alindi ve gorsel turu bilerek ayrildi: harita (AT06), cizgi grafik (AT07),
sutun grafik (AT08). AT01-AT05'te cizgi/sutun/tablo/pasta vardi; harita ilk kez
bu grupta ilk kez ornekleniyor.

Task 2 tarafinda 2. grubun olcutu korundu - soyut ve kurumsal konu, adayin kendi
gunluk hayatindan ornek veremeyecegi turden. Secilen iki gorev de havuzun `hard`
kademesinden; kutuphanede simdiye kadar hic hard Task 2 yoktu. Kalip tekrar
etmiyor: T2-44 opinion (2. grupta T2-01, 4. grupta T2-24), T2-39 double_question
(T2-17, T2-57). 6. grup icin T2 havuzunun kalanindan iki gorev daha secilecek.

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


# ================================================================ AT06
# harita: Ferndale koyu 1985 ve 2020

AT06_5 = """The two maps is about the village Ferndale in the year 1985 and how it is in 2020.

Firstly, in 1985 there is a big farmland in the north part of the village, on the top of the main road. But in 2020 this farmland is not exist any more, because they build there a housing estate with many small house and street.

Secondly, the school is in the south west and it is a small building in 1985. In 2020 the school become more bigger, the building take more place than before.

Thirdly, in the east side there is a shop near the road. In 2020 this small shop is change to a supermarket and next to the supermarket they make a car park for the car of the customer.

Also the main road is more wide in 2020 and on the river there is a new bridge for the people who walk. So the life of the resident become more comfortable now, because they find everything near the home."""

AT06_65 = """The two maps show the changes which happened in the village of Ferndale between 1985 and 2020.

Overall, the village became much more built up during this period: the farmland in the north was replaced by houses, and the services for the residents were made larger, while the natural features were mostly kept.

In 1985 the whole area to the north of the main road was a farmland. By 2020 this space has been completely covered by a housing estate, which is divided by several small streets. This is the biggest change between the two maps. The woodland in the north east corner, however, stayed exactly the same in the both maps.

There were also changes in the south of the village. The school, which is situated in the south west, was enlarged and now it occupies a bigger area than before. On the eastern side of the road, the small shop disappeared and a supermarket with a car park was built there.

Finally, the main road was widened and a new footbridge was constructed over the river, so the people can cross the water on foot. The row of the houses along the road did not change."""

AT06_8 = """The two maps illustrate how the village of Ferndale changed over the thirty-five years between 1985 and 2020.

Overall, what had been a largely rural settlement became a considerably denser one: the open land north of the main road was given over to housing, the existing services were expanded to match, and only the woodland and the older houses were left untouched.

The most striking change took place in the northern half of the village. In 1985 this area consisted of a single stretch of farmland running west from the woodland. By 2020 the fields had disappeared entirely beneath a housing estate laid out on a grid of streets, which occupies the whole of the space the farm once did. The woodland in the north-eastern corner, by contrast, survived the period intact.

South of the road the pattern is one of expansion rather than replacement. The school remained on its original site but was enlarged, extending both eastwards and southwards, while the modest shop to the east of the road gave way to a supermarket with its own car park alongside it.

Two smaller alterations complete the picture. The main road itself was widened, and a footbridge was thrown across the river at the southern edge of the village, where in 1985 there had been no crossing at all. The houses lining the road between the school and the river are shown unchanged on both maps."""

AT06_NEDEN_5 = {
    "task_response": "Bes degisimin dordu (tarim arazisi, okul, dukkan, yol ve kopru) sirayla veriliyor, ama haritanin butununu soyleyen bir cumle hicbir yerde yok ve degismeden kalan orman ile evler hic anilmiyor. Son paragraf haritada olmayan bir yorum ekliyor (hayat daha rahat oldu, alisveris icin sehre gitmiyorlar).",
    "coherence_cohesion": "Firstly / Secondly / Thirdly kalibi paragraflarin mantigini degil yalnizca sirayi tasiyor. Yine de her paragraf tek bir degisimi ele aldigi icin okuyucu yolunu kaybetmiyor.",
    "lexical_resource": "Konum dili big, north part, east side, near the road ile sinirli; opposite, to the east of gibi ogeler yok. More bigger, take more place, more wide bicimleri okuru yavaslatiyor.",
    "grammatical_range_accuracy": "Neredeyse her cumlede hata var: maps is, is not exist, they build there, is change, more bigger, the car of the customer. Butun metin genis zamanda yazilmis, oysa 1985 gecmis; yapilar hemen tamamen basit cumle.",
}
AT06_LIFT_5 = "Son paragraftaki yorumu atip yerine iki haritayi tek cumlede karsilastiran bir genel bakis koymak (kirsal yerlesim yogun yerlesime donusuyor) ve 1985 kismini gecmis zamana cevirmek."

AT06_NEDEN_65 = {
    "task_response": "Genel bakis ikinci paragrafta acikca var ve bes degisimin hepsi, degismeyen orman ve evler dahil, veriliyor. Okulun ve sitenin ne kadar buyudugu olcusuz kaliyor, degisimlerin buyuklugu siralanmiyor.",
    "coherence_cohesion": "Paragraflar mantikli bolunmus: genel bakis, kuzey, guney, kalan iki degisim. Baglantilar dogru ama There were also changes / Finally gibi tanidik kaliplarin disina cikmiyor.",
    "lexical_resource": "Built up, housing estate, enlarged, widened, footbridge gibi gorev icin dogru ogeler var. In the both maps ve was a farmland gibi yerlerde bicim tam oturmuyor.",
    "grammatical_range_accuracy": "Ilgi cumlecikleri ve edilgen yapi dogru kuruluyor, uzun cumleler dagilmiyor. Cumlelerin yarisinda tanimlik ya da zaman hatasi var (a farmland, has been covered, in the both maps, which is situated, the people can cross, the row of the houses); anlam hicbir yerde engellenmiyor.",
}
AT06_LIFT_65 = "Degisimleri esit sirada anlatmak yerine buyukluge gore siralamak - once tarim arazisinin tamamen kaybolmasi, sonra otekiler - ve okulun genislemesini yonuyle tarif etmek."

AT06_NEDEN_8 = {
    "task_response": "Genel bakis hem donusumun yonunu hem de neyin degismedigini soyluyor. Her degisim konumuyla birlikte veriliyor ve degisim ile genisleme ayri iki desen olarak adlandiriliyor; yorum hicbir yere girmiyor.",
    "coherence_cohesion": "Bilgi unsur unsur degil, kuzey/guney ve buyuk/kucuk degisim olarak gruplanmis. By contrast ve rather than replacement gibi ogeler baglantiyi cumlenin kendi isiyle kuruyor.",
    "lexical_resource": "Given over to housing, laid out on a grid of streets, gave way to, survived the period intact gibi az kullanilan ogeler dogru esdiziimle geciyor. Yon dili tutarli ve dogal.",
    "grammatical_range_accuracy": "Past perfect, ortac basli yapi, ilgi cumlecigi ve where ile kurulan yer cumlecigi kontrollu bicimde donuyor. Hata seyrek; thrown across the river biraz agir kaciyor ama okuru durdurmuyor.",
}
AT06_LIFT_8 = "Bu duzeyde ilerleme ayrintidan cok olcude: sitenin kapladigi alani eski tarim arazisiyle oransal olarak karsilastirmak metni bir adim daha kesinlestirir."


# ================================================================ AT07
# cizgi grafik: dort bolgede evde internet baglantisi, 2000-2020

AT07_5 = """The graph is about the percent of the house who have internet in the home in four region from 2000 until 2020.

Firstly, in 2000 the Eastport is the most high with 25 percent and after him the Northvale with 18 percent. The Central Plains have only 6 percent and the Southern Isles is the last one with 3 percent.

Secondly, all the four region go up every year. The Eastport arrive to 71 percent in 2010 and in 2020 it is 93 percent, so it is again the first. The Northvale is very near, it become 91 percent in the end.

Thirdly, the Central Plains and the Southern Isles is more slow in the beginning. But after 2010 they start to grow fast and the Central Plains arrive to 79 percent. The Southern Isles finish with 54 percent only, because in this region there is many island and the connection is more difficult in the island.

For this reason the government must build more internet line in the south of the country."""

AT07_65 = """The line graph shows the percentage of households which had an internet connection at home in four regions of a country between 2000 and 2020.

Overall, the proportion of connected households rose considerably in all the four regions during this period, but the two leading regions were always in front and Southern Isles remained in the last position from the beginning until the end.

In 2000, Eastport was the region who had the highest percentage, with 25%, followed by Northvale with 18%. The other two regions were much lower: Central Plains had only 6% and Southern Isles just 3%. These two regions therefore started from a very low level.

Eastport and Northvale developed almost in the same way. Both of them passed 50% before 2010 and finished the period above 90%, with 93% and 91% respectively. After 2015 their lines become flatter, probably because there were not many households left without a connection.

Central Plains grew more quickly in the second half of the period and reached 79% in 2020, so the distance with the leaders became small. Southern Isles also improved a lot and arrived at 54%, but this region stayed more than 35 percentage point behind Eastport at the end of the period."""

AT07_8 = """The graph traces the share of households with a home internet connection in four regions of a single country at five-year intervals from 2000 to 2020.

Overall, connection rates climbed steeply everywhere and the ranking of the four regions never altered, but the gap between the best and the worst served areas widened sharply during the first decade before narrowing again after 2010.

Eastport and Northvale moved almost in parallel throughout. Starting from 25% and 18% respectively, both had at least doubled their coverage by 2005, passed the two-thirds mark by 2010 and finished within two points of each other, at 93% and 91%. The flattening of both curves after 2015 suggests that these regions were approaching saturation.

The two remaining regions began far behind. Central Plains, with just 6% in 2000, was initially closer to Southern Isles than to the leaders, yet it grew fastest of all after 2010, adding 45 percentage points in ten years to finish at 79%, within striking distance of Northvale. Southern Isles rose from a mere 3% to 54%, a substantial gain in its own terms, although it remained the least connected region at every point measured.

The spread between the top and bottom figures tells the same story in numbers: 22 points in 2000, a peak of 52 points in 2010, and 39 points by 2020."""

AT07_NEDEN_5 = {
    "task_response": "Dort bolgenin rakamlari sirayla okunuyor ama grafigin butununu soyleyen bir cumle yok; makasin once acilip sonra daralmasi hic gorulmuyor. Son iki cumle grafikte olmayan bir sebep (adalar, baglanti zorlugu) ve bir tavsiye ekliyor.",
    "coherence_cohesion": "Firstly / Secondly / Thirdly kalibi mekanik ve paragraf iciyle iliskisi zayif. Bilgiler yine de izlenebilir bir sirada verildigi icin okuyucu takip edebiliyor.",
    "lexical_resource": "Egilim sozcugu go up, grow fast, more slow ile sinirli ve tekrar ediyor. The most high, arrive to, the percent of the house gibi yanlis bicimler okuru yavaslatiyor.",
    "grammatical_range_accuracy": "Hemen her cumlede uyum ya da zaman hatasi var: the house who have, all the four region go up, the Southern Isles is, there is many island. Yapilar neredeyse tamamen basit cumle; butun metin genis zamanda.",
}
AT07_LIFT_5 = "Son paragraftaki sebebi ve tavsiyeyi atip yerine dort bolgenin tamamini tek cumlede ozetleyen bir genel bakis koymak, ve metni gecmis zamana cevirmek."

AT07_NEDEN_65 = {
    "task_response": "Genel bakis var ve siralamanin hic degismedigini soyluyor; benzer seyreden iki bolge birlikte ele alinmis. En yuksek ile en dusuk arasindaki farkin 2010'da zirve yapmasi atlaniyor, bu yuzden makasin hareketi eksik kaliyor.",
    "coherence_cohesion": "Paragraf bolumu mantikli: genel bakis, baslangic durumu, ust iki bolge, alt iki bolge. Baglayicilar dogru ama therefore / also gibi tanidik ogelerin disina cikmiyor.",
    "lexical_resource": "Proportion, remained in the last position, respectively, percentage point gibi gorev icin yeterli ogeler var. The distance with the leaders ve arrived at 54% esdiziim olarak tam oturmuyor.",
    "grammatical_range_accuracy": "Ilgi cumlecikleri ve karsilastirma yapilari dogru kuruluyor, cumlelerin yarisi hatasiz. Kalan yarida tanimlik, ilgi adili, zaman ve cogul hatasi var (all the four regions, the region who had, their lines become flatter, 35 percentage point); anlam engellenmiyor.",
}
AT07_LIFT_65 = "Farki puan olarak adlandirip uc noktada vermek (2000'de 22, 2010'da 52, 2020'de 39 puan); bu tek ekleme genel bakisi eksiksiz hale getirir."

AT07_NEDEN_8 = {
    "task_response": "Genel bakis uc seyi birden soyluyor: her yerde yukselis, siralamanin hic degismemesi ve makasin once acilip sonra daralmasi. Bolgeler ikiser gruplanmis ve her biri secilmis rakamlarla desteklenmis; kapanis farki uc noktada sayiya baglamis.",
    "coherence_cohesion": "Bilgi bolge bolge degil, benzer seyreden ciftler halinde gruplanmis ve son paragraf butun metnin savini sayiyla toparliyor. By contrast, yet, although gibi ogeler dolgu degil, cumlenin isini yapiyor.",
    "lexical_resource": "Traces, the two-thirds mark, approaching saturation, within striking distance, spread gibi az kullanilan ogeler dogru esdiziimle geciyor. In its own terms secimi karsilastirmayi tek ifadeyle tasiyor.",
    "grammatical_range_accuracy": "Ortac basli cumle, past perfect, edilgen ve devrik ogeler kontrollu bicimde donuyor. Hata seyrek; the best and the worst served areas biraz sikisik ama okuru durdurmuyor.",
}
AT07_LIFT_8 = "Bu duzeyde ilerleme kesinlikte: Eastport ile Northvale'in 2015 sonrasi yataylasmasini yillik puan artisiyla olcmek, yorumu veriyle daha siki baglar."


# ================================================================ AT08
# sutun grafik: bes tatil turu, 2005 ve 2020

AT08_5 = """The bar chart give information about five kind of holiday trip that the resident of one country make in 2005 and in 2020.

Firstly, in 2005 the beach holiday is the most popular. It have 8.4 million trip and it is the biggest bar of the chart. The second one is the visit to the relative with 6 million. The city break have only 3.1 million, the walking in the countryside 2.2 million and the outdoor sport 1.3 million, so this is the smallest.

Secondly, in 2020 the situation is different. The city break go up very much and arrive to 7.5 million, so now it is the number one. The beach holiday go down to 6.2 million and it lose the first place.

Thirdly, the walking and the outdoor sport also increase, they become 4.4 and 2.6 million. The staying with the relative stay almost the same, 5.8 million.

In conclusion, this change happen because the ticket for the foreign country become more expensive and the people prefer a city near the home."""

AT08_65 = """The bar chart compares the number of holiday trips of five different types which were made by the residents of one country in 2005 and in 2020.

Overall, the total number of the holiday trips increased over these fifteen years, and the most important change is that the city break replaced the beach holiday as the most popular type.

In 2005 the beach holiday was clearly in the first position with 8.4 million trips, and staying with relatives was the second one with 6 million. The other three types were much smaller: 3.1 million for city breaks, 2.2 million for walking in the countryside and only 1.3 million for outdoor sports holidays.

By 2020 the picture had changed. The city break more than doubled and reached to 7.5 million trips, which was the highest figure of that year. The beach holiday, on the contrary, fell to 6.2 million and it lost his first place. Staying with relatives remained nearly stable, with a very small decrease from 6 to 5.8 million.

The two smallest categories also grew: walking in the countryside doubled to 4.4 million and the outdoor sports holidays went from 1.3 to 2.6 million. However, they were still the two less popular type of holiday in 2020."""

AT08_8 = """The bar chart compares the number of holiday trips of five kinds taken by the residents of one country in 2005 and again in 2020.

Overall, people took more holidays at the end of the period than at the beginning, the total rising from 21 million to 26.5 million trips, and the order at the top was reversed as the city break overtook the beach holiday, which was the only type to fall appreciably.

That reversal is the clearest single movement in the chart. City breaks, which accounted for just 3.1 million trips in 2005, had risen to 7.5 million by 2020, more than doubling and adding more journeys than any other category. Beach holidays travelled in the opposite direction, slipping from 8.4 million to 6.2 million and ending in second place.

The three remaining types were less dramatic but pointed the same way. Walking in the countryside doubled from 2.2 to 4.4 million, and outdoor sports holidays did much the same, climbing from 1.3 to 2.6 million, though the two of them together still amounted to less than a third of the 2020 total. Staying with relatives was the only genuinely settled category, easing back marginally from 6 million to 5.8 million.

Taken proportionally, therefore, the city break grew faster than anything else and was also responsible for the greater part of the extra travel recorded in 2020, while the two smallest categories simply doubled from a low base."""

AT08_NEDEN_5 = {
    "task_response": "Bes turun rakamlari iki yil icin de veriliyor ve siralamanin degistigi soyleniyor, ama grafigin butununu ozetleyen bir cumle yok ve toplamin artisi hic hesaplanmiyor. Son paragraf grafikte bulunmayan bir sebep uyduruyor (bilet fiyatlari).",
    "coherence_cohesion": "Firstly / Secondly / Thirdly kalibi yillari ayirmaya yariyor ama paragraf ici mantigi tasimiyor. Artan ve azalan kalemler gruplanmadigi icin karsilastirma dagilmis durumda.",
    "lexical_resource": "Go up, go down, become, the most popular disinda egilim sozcugu yok ve prompt'un kendi ifadeleri oldugu gibi tekrarlaniyor. The number one, arrive to, very much secimleri gorev icin fazla gunluk.",
    "grammatical_range_accuracy": "Hemen her cumlede hata var: chart give, five kind of holiday trip, it have, the city break go up, this change happen. Cogul ve uyum hatalari metin boyunca surekli; yapilar basit cumleden cikmiyor.",
}
AT08_LIFT_5 = "Son paragrafi atip yerine iki toplami (21 ve 26,5 milyon) veren bir genel bakis koymak ve artan kalemleri tek paragrafta toplamak."

AT08_NEDEN_65 = {
    "task_response": "Genel bakis ikinci paragrafta var ve zirvedeki yer degisimini dogru adlandiriyor; bes kalemin rakami eksiksiz veriliyor. Toplamin ne kadar artigi sayiyla soylenmiyor, bu yuzden 'toplam artti' ifadesi desteksiz kaliyor.",
    "coherence_cohesion": "Paragraflar yila gore degil, once 2005 sonra degisim ve buyuyen kalemler seklinde bolunmus. Gecisler dogru ama on the contrary yanlis secilmis bir baglayici ve However son cumlede beklenen karsitligi kurmuyor.",
    "lexical_resource": "More than doubled, remained nearly stable, categories, figure gibi gorev icin yeterli ogeler var. On the contrary, lost his first place ve the two less popular type esdiziim ve bicim olarak yanlis.",
    "grammatical_range_accuracy": "Ilgi cumlecigi, past perfect ve edilgen dogru kullaniliyor, uzun cumleler dagilmiyor. Cumlelerin yarisindan biraz fazlasinda tanimlik, edat, adil ya da cogul hatasi var (the total number of the holiday trips, reached to, his first place, the outdoor sports holidays, two less popular type); anlam engellenmiyor.",
}
AT08_LIFT_65 = "Genel bakisi sayiya baglamak: 21 milyondan 26,5 milyona artis yazilirsa hem toplam iddiasi desteklenir hem de gorev yaniti bir band yukari cikar."

AT08_NEDEN_8 = {
    "task_response": "Genel bakis hem toplami sayiyla veriyor hem de zirvedeki tersine donusu adlandiriyor. Kalemler artan ve duran diye gruplanmis, en buyuk mutlak artis ile oransal artis birbirinden ayrilmis; hicbir yerde sebep uydurulmamis.",
    "coherence_cohesion": "Metin tersine donus, kalan kalemler, oransal degerlendirme sirasiyla ilerliyor ve her paragraf tek is yapiyor. Travelled in the opposite direction ve pointed the same way gibi ogeler baglantiyi cumlenin kendi isiyle kuruyor.",
    "lexical_resource": "Slipping from, easing back marginally, from a low base, appreciably gibi az kullanilan ogeler dogru esdiziimle geciyor. Settled category secimi 'neredeyse degismedi' fikrini tek sozcukle tasiyor.",
    "grammatical_range_accuracy": "Mutlak yapi (the total rising from), ilgi cumlecikleri, ortac ogeler ve edilgen kontrollu bicimde donuyor. Hata seyrek; ikinci cumle uc bilgiyi birden tasidigi icin biraz uzun, ama okuru durdurmuyor.",
}
AT08_LIFT_8 = "Ikinci cumleyi ikiye bolmek ve her turun toplam icindeki payini yuzde olarak vermek; su an mutlak sayilar tam, oranlar yalnizca son paragrafta ima ediliyor."


# ================================================================ T2-44
# opinion / kamu butcesi: uzay arastirmasi mi konut ve saglik mi

T2_44_5 = """Nowadays the government give a lot of money for the space and the rocket, and many people think this money is better for the house and the hospital. I am agree with these people because in our life the first thing is the human.

Firstly, in every country there is a poor family who don't have a good house. They live in a small place with the children and sometime the roof is broken and the water come inside. If the government take the money of the space and give it for the house, this family can live in a better condition and the children can study in a warm room.

Secondly, the hospital is also a big problem. Many people wait many month for a operation and in the small city there is not enough doctor. The machine of the hospital is old and it break every time. With more money the government can buy new machine and take more doctor and nurse in the hospital.

Thirdly, the space is very far from us. The scientist send a rocket to the Mars but nobody live in the Mars, so this travel don't help the normal person. We look the photo in the television and after two day we forget it, but the sick person in the hospital don't forget his problem, he wait every day for his operation.

In conclusion, I think the money must go first for the house and the hospital, because this thing are the necessity of the people every day, and after, if it is some money in the budget, the government can look the space also."""

T2_44_65 = """Space programmes cost enormous sums, and many people believe that this money would be more useful if it was spent on housing, hospitals and the other needs inside the country. I agree with this opinion in general, although I do not think that space research should be stopped completely.

The first reason is that the needs at home are urgent and visible. A family which is living in a damp flat, or a patient who must wait eight months for an operation, have a problem today and not in twenty years. Public budget is limited, so when a government choose to build one thing it automatically decide not to build another. In this competition, a hospital seems to me more important than a mission to a planet where nobody will live.

The second reason is that the result of this kind of spending can be measured. If a city builds two hundred flats, everybody can see the flats and count the family who moved inside. The benefit of a space programme is much more difficult to explain to a citizen who pay taxes every month.

However, I do not agree with the people who say that space exploration is a waste of money. Many technology that we use every day, for example the weather forecast, the satellite navigation and the communication systems, came from these programmes. Space agencies also train engineers and scientist who work later in other sector of the economy. Moreover, in the majority of country the space budget is a very small percentage of the total expenses, so closing it would not solve the problem of the hospitals.

In conclusion, I largely agree that housing and health care should come first, but I believe that the correct solution is to reduce the space budget and not to cancel it."""

T2_44_8 = """Every few years a spacecraft leaves the atmosphere at a cost that would have built a hospital, and the comparison is an uncomfortable one. I agree that public money should be weighted heavily towards housing, health care and the other needs people feel directly, though I would stop well short of abolishing space budgets altogether.

The strongest argument for redirecting the money is that need has a timetable. A family raising children in a damp room, or a patient whose operation is eighteen months away, is being harmed now, and the harm compounds: children who are ill miss school, adults who are waiting cannot work. Space science, by contrast, is patient by nature — a probe launched five years later still arrives, and what it finds is no less valuable for the delay. Where two claims on one budget differ this sharply in urgency, the one that cannot wait has the better case.

There is also the question of who pays for a wrong decision. Overspending on housing leaves a country with a surplus of flats; underspending on health while funding prestige projects puts the cost on the people least able to absorb it, and that asymmetry settles which way caution should point.

The opposing case deserves more respect than it usually receives, however. Weather forecasting, satellite navigation and the monitoring of floods all exist because somebody funded research with no obvious application at the time, and space agencies remain among the few institutions that reliably train scientists and engineers who then work elsewhere in the economy. The sums involved, vast as they look in isolation, are also a fraction of one per cent of national spending, so a country that cancelled its programme tomorrow would find its housing shortage unchanged the day after.

That last point is what keeps me from agreeing without reservation. Space budgets should grow only once basic needs at home are met, rather than be closed altogether: a state which cannot house its people has misjudged its priorities, but one which abandons long-term research to pay this year's bills has merely postponed a different failure."""

T2_44_NEDEN_5 = {
    "task_response": "Tutum giriste acikca veriliyor ve sonuna kadar korunuyor, ama uc gerekce de ayni fikrin (insanin ihtiyaci once gelir) tekrari ve hicbiri ornekten oteye gelismiyor. Gorevin bekledigi karsi gorus - uzay calismalarinin gunluk hayattaki karsiliklari - hic anilmiyor.",
    "coherence_cohesion": "Firstly / Secondly / Thirdly / In conclusion iskeleti duzenli ve her gerekce kendi paragrafinda duruyor. Paragraf icinde gelisme yok: cumleler ayni fikri baska sozcuklerle tekrarliyor, gerekceler arasinda baglanti kurulmuyor.",
    "lexical_resource": "Money, government, house, hospital, people sozcukleri prompt'tan oldugu gibi alinip surekli tekrar ediliyor; kamu butcesi alanina ait tek bir oge yok. Take more doctor, look the space, the necessity of the people secimleri yanlis kurulmus.",
    "grammatical_range_accuracy": "Hemen her cumlede hata var: the government give, I am agree, a family who don't, many month, a operation, this thing are. Cogul ve uyum hatalari metin boyunca sistematik; yapilar basit cumle ile tek tuk if/who cumlecigi arasinda kaliyor.",
}
T2_44_LIFT_5 = "Ucuncu paragrafi karsi gorus paragrafina cevirmek: uzay arastirmasinin hava tahmini ve haberlesme gibi gunluk karsiliklarini kabul edip sonra neden yine de konutun once geldigini soylemek."

T2_44_NEDEN_65 = {
    "task_response": "Tutum net ve metin boyunca korunuyor; karsi gorus ayri bir paragrafta uc gerekceyle gercekten kabul ediliyor ve sonucta kismi bir hukum veriliyor. Olculebilirlik gerekcesi otekilere gore ince kaliyor - iki cumlede aciliyor ve ornegi genel.",
    "coherence_cohesion": "The first reason / The second reason / However / In conclusion siralamasi net ve her paragraf tek fikir tasiyor. Baglayicilar kalip duzeyinde; karsi gorus paragrafi metnin geri kalanina yalnizca However ile bagalaniyor.",
    "lexical_resource": "Urgent and visible, public budget, satellite navigation, a very small percentage of the total expenses gibi konuya uygun ogeler dogru kullanilmis. Other sector of the economy, the needs at home ve moved inside esdiziim olarak tam oturmuyor.",
    "grammatical_range_accuracy": "Ilgi cumlecikleri, kosul cumleleri ve karsilastirma yapilari dogru kuruluyor; uzun cumleler dagilmiyor. Cumlelerin yarisindan biraz fazlasinda uyum, tanimlik ya da cogul hatasi var (have a problem, a government choose, a citizen who pay, many technology, in the majority of country); anlam engellenmiyor.",
}
T2_44_LIFT_65 = "Olculebilirlik gerekcesini somutlastirmak - iki yuz dairenin ne kadar surede ve kime teslim edildigi gibi bir olcu eklenirse gerekce otekilerle esitlenir."

T2_44_NEDEN_8 = {
    "task_response": "Tutum ilk paragrafta kosuluyla birlikte kuruluyor ve sonuca kadar ayni kaliyor. Karsi gorus uc ayri gerekceyle, ustelik en guclu haliyle veriliyor; butce payinin kucuklugu kabul edilip hukum bu kabulun uzerine yeniden kuruluyor.",
    "coherence_cohesion": "Metin aciliyet, riskin kime dustugu, karsi gorus ve nitelenmis hukum sirasiyla ilerliyor; her paragraf tek is yapiyor. By contrast, however, that last point gibi ogeler baglantiyi cumlenin kendi isiyle kuruyor, kapanis bastaki karsilastirmaya donuyor.",
    "lexical_resource": "Weighted heavily towards, the harm compounds, prestige projects, asymmetry, without reservation gibi az kullanilan ogeler dogru esdiziimle geciyor. Need has a timetable ve patient by nature secimleri soyut fikri tek ifadeyle tasiyor.",
    "grammatical_range_accuracy": "Iki noktali aciklama, cizgi arasi ekleme, ortac basli yapi ve vast as they look gibi devrik odun cumlecigi kontrollu bicimde donuyor. Hata seyrek ve okuru durdurmuyor; band 9'un tam rahatligi yok.",
}
T2_44_LIFT_8 = "Riskin kime dustugu paragrafi otekilerden kisa kaliyor; 'fazla konut en kotu ihtimalle fazladir' fikri bir ornekle acilirsa hukum daha saglam durur."


# ================================================================ T2-39
# double_question / kamu hizmetlerinin ozel sirketlere gecmesi

T2_39_5 = """In many country today the service like the rubbish, the bus and some part of the health are not more in the hand of the state, a private company make this work. There is different reason for this situation.

The first reason is the money. The government have many expense for the school, the road, the army and after all this the budget is finish. When a private company come and say 'I make this service and I pay myself the new truck and the new bus', the minister is very happy because he don't spend nothing from his budget.

The second reason is the competition. When there is only the state, the citizen have no choice and if the service is bad he cannot do nothing. But when there is three or four company, every company want to take the contract and for this they try to make the price more low and the service more fast. The state can also change the company if the work is not good.

The third reason is the specialist. Today there is big company who only make the rubbish collection in many city of many country. They have the experience and the machine, and it is more easy for a small town to call this company than to buy all the truck and take all the worker alone.

In my opinion this development is positive because the competition is always good for the customer.

So this is the reason why the state give the service to the private company and I think it is not a bad thing for the people."""

T2_39_65 = """In a growing number of countries, tasks that used to belong to the state - collecting rubbish, running buses, even parts of the health service - are now carried out by private firms working under a contract. There are several reason for this change, and in my view it brings benefits only when the state keeps a strong control on the company.

The main cause is financial. Public budgets are under pressure everywhere, and a service like an urban bus network need constant investment in vehicles and depots. When a private firm agrees to make this investment itself in exchange of a contract of fifteen years, a government can renew the service without borrowing money. A second cause is the belief in competition: if several firms want the same contract, they must promise a lower price, and the authority can change the firm when the results are poor. Finally, specialised companies now exist in these sector, and a small town can buy their experience cheaper than creating its own department.

The positive effects are real. Costs are usually controlled more carefully, because a private firm which loses money disappears, while a public department simply asks for a bigger budget. Contracts also make the standards measurable: the number of the collections per week, the maximum waiting time, the penalties.

However, there are serious risks. A company works for a profit, so it has little interest in the districts where this profit is small, and the price for the citizen tends to rise after the first years. It is also more difficult to know who is responsible when something goes wrong, because the authority says that it is the company and the company says that it is not in the contract.

In conclusion, the change is happening mainly for financial reasons, and I consider it positive for the services which can be measured easily, such as the rubbish collection, but negative for those where the citizen has no possibility to choose another supplier."""

T2_39_8 = """Rubbish collection, bus routes and parts of health care were, within living memory, delivered by public employees almost everywhere; in many countries they are now the business of firms working to a contract. The reasons are largely financial, and my own view is that the shift helps in narrow circumstances and does harm outside them.

The first driver is the state of public finances. Services of this kind consume capital continuously - fleets wear out, depots need rebuilding - and a government short of money can transfer both the investment and the risk to a company for fifteen years. The second is a belief about incentives: a firm that must win the contract again has a reason to control its costs, whereas a department whose budget arrives regardless does not. A third is the rise of specialist operators large enough to run waste services in dozens of towns; buying their expertise is cheaper for a small authority than building it.

Where a service is easy to specify, the arrangement works well. Collections per week, punctuality, response times: all of these can be written into a contract and audited, and a supplier who fails them can be replaced, which is more than can usually be said of an underperforming public department.

Most services, though, are not so tidy. A profit-seeking operator has every reason to serve dense, prosperous districts attentively and remote ones grudgingly, and once the first contract expires prices tend to move upwards rather than down. Accountability blurs as well: when a bus route is cut, the authority points to the contract and the company points to the authority, and the passenger has nobody to complain to. Where people cannot take their custom elsewhere, competition exists only in the month the contract is signed, which is a thin form of discipline.

On balance, then, I regard the trend as neither straightforwardly good nor bad, but as dependent on something the debate usually ignores: the capacity of the authority that writes and polices the contract. Where that capacity is strong, a private provider is a useful instrument; where it is weak, handing over a service is not delegation but abandonment."""

T2_39_NEDEN_5 = {
    "task_response": "Birinci soru duzgun karsilaniyor: uc sebep sirayla ve ornekle veriliyor. Ikinci soru tek desteksiz cumleye indirgenmis (rekabet musteri icin her zaman iyidir) ve olumsuz yan hic tartilmamis; gorevin iki yukumlulugunden biri karsilanmiyor.",
    "coherence_cohesion": "The first reason / The second reason / The third reason kalibi duzenli ve her sebep kendi paragrafinda. Degerlendirme icin hicbir gecis kurulmuyor: tek cumlelik gorus paragrafi metne baglanmadan araya giriyor, son cumle giristeki cumleyi tekrarliyor.",
    "lexical_resource": "The service, the company, the state, the money sozcukleri prompt'tan alinip tekrarlaniyor; sozlesme, denetim ya da hizmet olcutu alanina ait tek bir oge yok. Make this service, the budget is finish, more low secimleri yanlis kurulmus.",
    "grammatical_range_accuracy": "Hemen her cumlede hata var: in many country, there is different reason, the government have, he don't spend nothing, there is three or four company, big company who only make. Cift olumsuzluk ve cogul hatalari sistematik; yapilar basit cumle ile when/if cumleciklerinden ibaret.",
}
T2_39_LIFT_5 = "Tek cumlelik gorusu bir paragrafa cevirmek: olumlu yani bir gerekceyle desteklemek ve en az bir olumsuz yani (karsiz bolgeler, fiyat artisi) yazmak - su an gorevin ikinci yarisi cevaplanmamis sayiliyor."

T2_39_NEDEN_65 = {
    "task_response": "Iki soru da yanitlaniyor: uc sebep sirasiyla veriliyor ve hukum sonucta hizmet turune gore ayrilarak nitelendiriliyor. Olumlu yan iki gerekceyle acilirken olumsuz yan da iki gerekceyle veriliyor, ama ikisi de ornege inmeden genel kaliyor.",
    "coherence_cohesion": "The main cause / A second cause / Finally / The positive effects / However / In conclusion siralamasi net ve paragraflar iceride gelisiyor. Sebepler paragrafi uc sebebi tek yerde topluyor, bu yuzden ucuncu sebep otekilerden kisa kaliyor; gecisler kalip duzeyinde.",
    "lexical_resource": "Under a contract, public budgets, measurable standards, penalties, supplier gibi konuya uygun ogeler dogru kullanilmis. Keeps a strong control on, in exchange of ve has no possibility to choose esdiziim olarak tam oturmuyor.",
    "grammatical_range_accuracy": "Ilgi cumlecikleri, kosul cumleleri ve iki noktali siralama dogru kuruluyor, uzun cumleler dagilmiyor. Cumlelerin yarisinda cogul, tanimlik ya da edat hatasi var (several reason, network need, in exchange of, in these sector, the number of the collections, works for a profit); anlam engellenmiyor.",
}
T2_39_LIFT_65 = "Olumsuz yani somutlastirmak: hangi tur bolgenin nasil eksik hizmet aldigini bir ornekle gostermek, su an iddia dogru ama desteksiz duruyor."

T2_39_NEDEN_8 = {
    "task_response": "Uc sebep birbirinden ayri mekanizmalarla veriliyor (sermaye yuku, tesvik yapisi, uzmanlasmis isletmeci). Degerlendirme once hangi kosulda ise yaradigini kabul edip sonra uc gerekceyle sinirini ciziyor; hukum en sonda sozlesmeyi yazan kurumun kapasitesine baglanarak nitelendiriliyor.",
    "coherence_cohesion": "Metin sebepler, isleyen durum, islemeyen durum, hukum sirasiyla ilerliyor ve her paragraf tek is yapiyor. Where a service is easy to specify ve the difficulty is that gibi ogeler baglantiyi cumlenin kendi isiyle kuruyor; kapanis bastaki sozlesme fikrine donuyor.",
    "lexical_resource": "Within living memory, consume capital, accountability blurs, take their custom elsewhere, a thin form of discipline gibi az kullanilan ogeler dogru esdiziimle geciyor. Not delegation but abandonment kapanisi hukmu tek ifadede topluyor.",
    "grammatical_range_accuracy": "Cizgi arasi ekleme, iki noktali aciklama, ilgi cumlecikleri ve where ile kurulan kosul esnek bicimde donuyor. Hata seyrek ve okuru durdurmuyor; band 9'un tam rahatligi yok.",
}
T2_39_LIFT_8 = "Ucuncu sebep (uzmanlasmis isletmeciler) otekilerden kisa; kucuk bir belediyenin neyi satin aldigi bir adim acilirsa uc sebep esit agirlikta durur."


# ---------------------------------------------------------------- veri
VERI = [
    ("AT06", 150, [
        (5.0, AT06_5, AT06_NEDEN_5, AT06_LIFT_5),
        (6.5, AT06_65, AT06_NEDEN_65, AT06_LIFT_65),
        (8.0, AT06_8, AT06_NEDEN_8, AT06_LIFT_8),
    ]),
    ("AT07", 150, [
        (5.0, AT07_5, AT07_NEDEN_5, AT07_LIFT_5),
        (6.5, AT07_65, AT07_NEDEN_65, AT07_LIFT_65),
        (8.0, AT07_8, AT07_NEDEN_8, AT07_LIFT_8),
    ]),
    ("AT08", 150, [
        (5.0, AT08_5, AT08_NEDEN_5, AT08_LIFT_5),
        (6.5, AT08_65, AT08_NEDEN_65, AT08_LIFT_65),
        (8.0, AT08_8, AT08_NEDEN_8, AT08_LIFT_8),
    ]),
    ("T2-44", 250, [
        (5.0, T2_44_5, T2_44_NEDEN_5, T2_44_LIFT_5),
        (6.5, T2_44_65, T2_44_NEDEN_65, T2_44_LIFT_65),
        (8.0, T2_44_8, T2_44_NEDEN_8, T2_44_LIFT_8),
    ]),
    ("T2-39", 250, [
        (5.0, T2_39_5, T2_39_NEDEN_5, T2_39_LIFT_5),
        (6.5, T2_39_65, T2_39_NEDEN_65, T2_39_LIFT_65),
        (8.0, T2_39_8, T2_39_NEDEN_8, T2_39_LIFT_8),
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
