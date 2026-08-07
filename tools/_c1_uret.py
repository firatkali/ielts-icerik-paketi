# -*- coding: utf-8 -*-
"""Ornek cevap kutuphanesi - 1. grup: Academic Task 1 (AT01-AT05).

Metinler burada duz Python dizesi olarak duruyor; kelime sayisi JSON'a elle
yazilmiyor, uretim sirasinda sayiliyor. Boylece metin duzeltilince sayac
sessizce yanlis kalmiyor. Sayim kurali degerlendirme talimatiyla ayni:
bosluga gore ayrilan belirtec sayisi.
"""
import json
import os

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEDEF = os.path.join(KOK, "content", "ornek-cevaplar", "writing")


def _say(metin):
    return len(metin.split())


# ---------------------------------------------------------------- AT01
AT01_5 = """The graph is show the percentage of household waste that recycled in three town between 1995 and 2020.

Firstly, in 1995 Hallowfield have 30 percent and it is the most high of the three. Marden is 12 percent and Trentbury is only 8 percent, so Trentbury is the lowest in this year. Secondly, after 2000 the Hallowfield start to go down. In 2010 it is 28 percent and in 2020 it is only 20 percent, so it lose many percent.

Thirdly, Marden and Trentbury is not same. They go up all the time. Marden go from 12 percent to 52 percent and this is a big increase. Trentbury also increase and in 2020 it become 61 percent, the most high number of the graph. Between 2005 and 2010 this two town pass the Hallowfield, because the people there don't want to recycle any more.

In my opinion recycling is very important for the environment and the government must help this town for more recycle."""

AT01_65 = """The line graph shows the percentage of household waste which was recycled in three towns, Marden, Hallowfield and Trentbury, between 1995 and 2020.

Overall, two of the towns increased their recycling rate over the period, while the third one decreased. Trentbury and Marden ended much higher than they started, but Hallowfield finished lower than its first year.

In 1995, Hallowfield had the highest percentage with 30%, compared to 12% in Marden and only 8% in Trentbury. After that, Hallowfield rose a little to 33% in 2000, which was its highest point, and then it went down in every following year until it reached 20% in 2020.

Marden and Trentbury both showed a steady growth. Marden increased from 12% to 27% in 2005 and continued to 52% at the end of the period. Trentbury grew even faster, reaching 25% in 2005 and 61% in 2020, which was the highest figure of all three towns. Between 2005 and 2010 both of them passed Hallowfield, and in the same years Trentbury also became bigger than Marden.

In conclusion, the difference between the three towns was much larger in 2020 than it was in 1995."""

AT01_8 = """The line graph compares the proportion of household waste that was recycled in the towns of Marden, Hallowfield and Trentbury over the twenty-five years from 1995 to 2020.

Overall, recycling rates climbed steeply in two of the three towns while Hallowfield moved in the opposite direction, and the gap between the best and the worst performer widened considerably over the period.

In 1995 Hallowfield was comfortably ahead of its neighbours, recycling 30% of its household waste, roughly two and a half times the figure for Marden and almost four times that of Trentbury, which stood at just 8%. Hallowfield's rate edged up to a peak of 33% in 2000, but it then fell steadily for the remaining twenty years, ending at 20%.

Trentbury, by contrast, saw the most dramatic transformation. Having started from the lowest position, it overtook Marden between 2005 and 2010 and finished at 61%, a rise of more than fifty percentage points. Marden followed a similar though gentler upward path, more than quadrupling its rate from 12% to 52%. Both towns passed Hallowfield during the second half of the 2000s.

By 2020, therefore, the original ranking had been completely reversed, and the spread between the highest and lowest figures had widened from 22 to 41 percentage points."""

# ---------------------------------------------------------------- AT02
AT02_5 = """The bar chart give information about the visits of five age group to the public libraries in one region in 2010 and 2022.

Firstly, in 2010 the group under 15 is the biggest with 4.8 million and the group 60 and over is the smallest with only 2.6 million. The other three group are between 3 and 4 million, so they are similar.

Secondly, in 2022 many group go down. The under 15 fall to 3 million and the group 15-29 fall to 1.4 million, and it is a very big fall. The group 30-44 also fall to 2.6 million people.

Thirdly, two group are different. The group 45-59 rise a little from 3.1 to 3.4 million and the group 60 and over rise from 2.6 to 4.1 million, so now this group visit the library more than all the other group.

I think the young people don't go to the library because they use the internet and the mobile phone for read the books today."""

AT02_65 = """The bar chart compares how many visits were made to public libraries in one region by five different age groups in the years 2010 and 2022.

Overall, the total number of visits decreased over this period, but not every age group followed the same direction. The younger groups visited the libraries less, while the older groups visited them more.

In 2010, people under 15 made the most visits, 4.8 million, and after them there was the 30-44 group with 3.9 million. The 60 and over group was the last one, with only 2.6 million visits.

In 2022 the situation was not the same. The under 15 group dropped to 3 million, and the 15-29 group had the biggest reduction, from 3.2 million to 1.4 million, which is less than a half. The 30-44 group also went down, to 2.6 million.

On the other hand, the two oldest groups made a growth. The 45-59 group stayed almost the same, with a small rise from 3.1 to 3.4 million, but the 60 and over group increased to 4.1 million and became the group with the most visits in 2022. In total, the visits fell from 17.6 million to 14.5 million."""

AT02_8 = """The bar chart compares the number of visits made to public libraries in one region by five age groups in 2010 and in 2022.

Overall, library use declined over the twelve-year period, but the fall was confined to visitors under 45; the two oldest groups actually went more often in 2022, and the age group responsible for the largest number of visits changed completely.

In 2010 the youngest readers were by far the heaviest users of libraries, accounting for 4.8 million visits a year, ahead of those aged 30 to 44 with 3.9 million. By 2022, however, visits by the under-15s had dropped to 3.0 million, and the 60-and-over group had moved into first place with 4.1 million, an increase of well over a half.

The steepest decline came among 15- to 29-year-olds, whose visits more than halved, from 3.2 million to a mere 1.4 million, the lowest figure anywhere on the chart. Those aged 30 to 44 also went less frequently, although their loss of 1.3 million was proportionally less severe.

The 45-to-59 group proved the most stable, edging up from 3.1 to 3.4 million. Taken together, annual visits fell from 17.6 million to 14.5 million."""

# ---------------------------------------------------------------- AT03
AT03_5 = """The two pie chart shows the energy in a average home in one country in 1990 and 2020 for five different thing.

Firstly, in 1990 the space heating is very big, it is 62% and it is more than the half of all the energy. The water heating is 18% and it is the second. The cooking is 9%, the lighting is 6% and the appliances is only 5%, so this three is small.

Secondly, in 2020 the space heating go down to 48%. It is still the first but it is not so big like before. The appliances and electronics is 21% now, so this category use more energy than 1990 and it become the second.

Thirdly, the water heating is 20%, almost the same, and the cooking and the lighting go down a little, they are 7% and 4% in 2020.

So we can see the people in 2020 buy many machine for the home and they use more electricity than the people in 1990."""

AT03_65 = """The two pie charts illustrate the way energy was used in an average house in one country in 1990 and in 2020, divided into five different purposes.

Overall, space heating was the main use of energy in both years, but its percentage became smaller, while appliances and electronics became much more important at the end of the period.

In 1990, space heating took 62% of all the energy, which was the largest part by far. Water heating was in the second position with 18%, and then came cooking with 9%, lighting with 6% and appliances with 5%, so these three categories were quite small.

In 2020, the picture was different. Space heating decreased to 48%, so it lost 14%, although it was still the biggest category. The most important change happened in the appliances and electronics, which climbed from 5% to 21% and took the second position. Water heating almost did not change and stayed at 20%, but for this reason it became the third one.

Cooking and lighting also decreased a little, to 7% and 4%. In conclusion, the energy of the home was shared in a more balanced way in 2020."""

AT03_8 = """The two pie charts show how the energy consumed in an average home in one country was divided between five purposes in 1990 and in 2020.

Overall, space heating remained the dominant use of energy in both years, but its share shrank noticeably, and the ground it lost went almost entirely to appliances and electronic devices, whose proportion grew more than fourfold. The other three categories changed comparatively little.

In 1990, heating the home accounted for 62% of domestic energy, nearly two thirds of the total and more than three times the share of the next largest category, water heating, at 18%. Cooking, lighting and appliances between them made up only a fifth of consumption, with appliances the smallest slice of all at 5%.

Thirty years later, space heating still came first, but at 48% it no longer absorbed half of the total. Appliances and electronics had risen to 21%, moving from last place to second and pushing water heating, which was virtually unchanged at 20%, down into third. The two smallest categories both contracted slightly, cooking from 9% to 7% and lighting from 6% to 4%.

The overall pattern, then, is one of a household energy budget that became rather less concentrated on heating."""

# ---------------------------------------------------------------- AT04
AT04_5 = """The table is about the journey to work in the city Ardenholm in 2015 and 2023 and about the time of the journey in 2023.

Firstly, the car is the most popular in the two year. In 2015 it is 46% and in 2023 it is 34%, so it go down 12%. But it is still the number one in the city.

Secondly, the bicycle become more popular. In 2015 only 9% of people use the bicycle but in 2023 it is 18%, so it is two time more. The bus or tram also go up from 22% to 27%. The walking go down a little, from 18% to 16%, and the train don't change, it is 5% in the two year.

Thirdly, about the minutes. The train need 41 minutes and this is a very long time. The bus or tram need 35 minutes. The car need 28 minutes, the bicycle need 22 minutes and the walking is only 19 minutes, so the walking is the most fast of all."""

AT04_65 = """The table shows the percentage of journeys to work made by five types of transport in a city called Ardenholm in 2015 and 2023, and also how many minutes an average journey needed in 2023.

Overall, the car was still the most popular transport in both years, but it lost a large part of its share, while the bicycle and the bus or tram were used more in 2023. The longest journeys were made by train.

In 2015, almost half of the journeys were done by car, exactly 46%, and the bus or tram was second with 22%. Walking was 18%, the bicycle only 9% and the train just 5%.

In 2023, the car went down to 34%, and this is the biggest fall in the table. The bicycle became two times bigger, from 9% to 18%, which was the biggest growth. The bus or tram also increased, to 27%, and passed the walking, which decreased slightly to 16%. The train did not change at all.

About the time, the train took 41 minutes, which was the longest, and walking took only 19 minutes. A car journey took 28 minutes and a bicycle journey 22 minutes, so the difference between these two was small."""

AT04_8 = """The table gives the share of journeys to work made by five modes of transport in Ardenholm in 2015 and 2023, together with how long an average journey by each mode took in the later year.

Overall, the car lost ground sharply while cycling and public transport gained, so commuting in the city became noticeably less car-dependent. Journey times, meanwhile, bore little relation to popularity: the slowest mode was also the least used.

The car remained the commonest way of getting to work in both years, but its share fell from 46% to 34%, easily the largest movement in the table. Cycling did the opposite: at 9% in 2015 it was one of the minor modes, yet by 2023 it had doubled to 18%. Buses and trams also picked up, climbing five points to 27% and taking second place, while walking slipped marginally from 18% to 16% and the train held steady at 5%.

Turning to duration, the train was much the slowest option at 41 minutes, followed by bus or tram at 35. Walking was the quickest at 19 minutes, and cycling, the fastest-growing mode, took 22 minutes, only six more than driving."""

# ---------------------------------------------------------------- AT05
AT05_5 = """The diagram show how the rain water is collect and clean in a public building for use it again.

Firstly, the rain fall on the roof of the building. The gutters and the pipes take this water and it go to a leaf screen. This screen clean the leaf and the grit from the water.

Secondly, the water go to a big tank under the ground and it stay there. When the tank is full the water go out to the drain.

Thirdly, a pump take the water up to the treatment. There is a sand filter and it take the small particle from the water. After this there is a ultraviolet unit and it kill the bacteria, so the water is clean now.

Finally the water go to another tank in the top of the building. From this tank the people use the water for the toilet and for the plants. This system is very good for save the water and the money of the building."""

AT05_65 = """The diagram shows how rainwater is collected and cleaned so that it can be used inside a public building.

Overall, there are nine stages in this process, and it is a linear process which starts with the rain on the roof and finishes with two different uses of the water. The water is also cleaned two times before it is used.

First of all, the rain falls on the roof of the building and the gutters and the pipes collect it. After that, the water arrives to a leaf screen, where the leaves and the grit are taken away. Then the water is stored in a tank which is under the ground. If there is too much water, the extra water goes to the drain.

In the next stage, a pump takes the water up from the tank to the treatment unit. The water goes through a sand filter first, which cleans the small particles, and after that an ultraviolet unit kills the bacteria in the water.

Finally, the clean water is kept in a header tank. From this tank the water is distributed for two purposes: the toilets and watering the plants. The water is not used for drinking."""

AT05_8 = """The diagram illustrates the stages by which rainwater is captured from the roof of a public building, treated, and then put back to use inside it.

Overall, the process is linear and, apart from a single pump, appears to run without human intervention: it begins with rain falling on the roof and ends at two separate points of use, with an overflow returning any surplus to the drain. Cleaning takes place in two distinct phases, one mechanical and one designed to remove bacteria.

At the start, rain that lands on the roof is channelled into gutters and pipes and directed towards a leaf screen, where leaves and grit are strained out before the water travels any further. It is then stored in an underground tank; once this tank is full, the excess simply runs off into the drain.

When the water is needed, a pump lifts it out of the tank and into the treatment unit. Here it first passes through a sand filter, which catches the fine particles that the screen could not, and it is then exposed to ultraviolet light in order to destroy any remaining bacteria.

Finally, the treated water is held in a header tank, from which it is distributed to its two uses: flushing the toilets and watering plants. At no stage is it made fit for drinking."""


VERI = [
    ("AT01", [
        (5.0, AT01_5, {
            "task_response": "Grafigin butununu ozetleyen bir cumle yok; paragraflar sirayla rakam okuyor ve kesisme noktasi bir sonuc olarak degil bir ayrinti olarak geciyor. Son paragraf veride olmayan bir sebep ve bir gorus ekliyor (the government must help), bu da gorevin disina cikiyor.",
            "coherence_cohesion": "Firstly / Secondly / Thirdly kalibi mekanik ve paragraf iceriginin mantigini degil sadece sirayi gosteriyor. Yine de bilgiler izlenebilir bir sirada, bu yuzden okuyucu yolunu kaybetmiyor.",
            "lexical_resource": "Egilim sozcugu go up, go down, big increase ile sinirli kaliyor ve tekrar ediyor. The most high, lose many percent gibi yanlis bicimler okuru yavaslatiyor.",
            "grammatical_range_accuracy": "Cumlelerin cogunda ozne-yuklem uyumu ya da zaman hatasi var: is show, Hallowfield have, Marden go, this two town pass. Yapilar neredeyse tamamen basit cumle; yan cumle yok denecek kadar az.",
        }, "Son paragraftaki gorusu atip yerine grafigin butununu soyleyen tek bir cumle koymak (iki kasaba yukseliyor, biri dusuyor) ve butun metni gecmis zamanda yazmak."),
        (6.5, AT01_65, {
            "task_response": "Genel bakis ikinci paragrafta acikca var ve uc kasabanin da rakamlari veriliyor, kesisme donemi belirtiliyor. Ancak farkin 22 puandan 41 puana acilmasi gibi karsilastirmalar sayiyla desteklenmeden geciliyor.",
            "coherence_cohesion": "Paragraf bolumu mantikli: genel bakis, dusen kasaba, yukselen kasabalar, sonuc. Baglayicilar dogru ama After that / In conclusion gibi tanidik kaliplarin disina cikmiyor.",
            "lexical_resource": "Highest, lowest, steady growth, reached gibi gorev icin yeterli sozcuk var. Became bigger than Marden ve the third one decreased gibi yerlerde esdiziim tam oturmuyor.",
            "grammatical_range_accuracy": "Ilgi cumlecigi ve zaman cumlecigi kullaniliyor, cumlelerin cogu hatasiz. Kalan hatalar (a steady growth, in every following year) anlami engellemiyor.",
        }, "Yuzde farklarini puan olarak adlandirmak ve son cumleyi 22'den 41 puana gibi somut bir sayiyla baglamak; bu tek degisiklik gorev yanitini bir band yukari tasir."),
        (8.0, AT01_8, {
            "task_response": "Genel bakis hem yonu hem de sonucu (farkin acilmasi) soyluyor, ve her kasaba secilmis rakamlarla destekleniyor. Siralamanin tersine donmesi ayri bir bulgu olarak kapanista veriliyor.",
            "coherence_cohesion": "Bilgi kasaba kasaba degil, once dusen sonra yukselenler seklinde anlamli bir sirada gruplanmis. By contrast ve therefore gibi baglayicilar cumlenin isini yapiyor, dolgu degil.",
            "lexical_resource": "Edged up, peak, quadrupling, spread, percentage points gibi az kullanilan ogeler dogru esdiziimle geciyor. Comfortably ahead gibi secimler dogal.",
            "grammatical_range_accuracy": "Having started from... gibi ortac yapisi, ilgi cumlecikleri ve past perfect kontrollu bicimde kullanilmis. Hata seyrek ve okuru durdurmuyor; yine de band 9'un tam esnekligi yok.",
        }, "Bu duzeyde ilerleme ayrinttadan cok kesinlikte: her kasaba icin degisimin hizini da (ornegin yillik ortalama) verecek bir olcu eklemek."),
    ]),
    ("AT02", [
        (5.0, AT02_5, {
            "task_response": "Butun gruplarin rakamlari veriliyor ama toplamin dustugu ya da genc-yasli ayrimi hicbir yerde tek cumleyle soylenmiyor. Son paragraf veride olmayan bir sebep uyduruyor ve 2.6 million people diyerek ziyaret sayisini kisi sayisi sanip yanlis okuyor.",
            "coherence_cohesion": "Firstly / Secondly / Thirdly disinda baglayici yok ve bunlar da yalnizca paragraf numarasi islevi goruyor. Sira izlenebilir oldugu icin okur akisi kaybetmiyor.",
            "lexical_resource": "Big, small, fall, rise, go down disina cikmayan dar bir sozcuk kumesi surekli tekrar ediyor. For read the books gibi bicim hatalari var.",
            "grammatical_range_accuracy": "Neredeyse her cumlede uyum ya da cogul hatasi var: the bar chart give, five age group, many group go down, this group visit. Butun cumleler basit ya da and ile baglanmis.",
        }, "Son paragraftaki tahmini atip yerine 'dusus sadece 45 yas altinda oldu' diyen bir genel bakis cumlesi yazmak; ardindan cogul -s'leri tek tek kontrol etmek."),
        (6.5, AT02_65, {
            "task_response": "Genel bakis hem toplam dususu hem de gruplarin ters yonlerini soyluyor, ve her grup rakamla destekleniyor. En cok ziyaret eden grubun degismesi ise bulgu olarak degil, siradan bir ayrinti gibi geciyor.",
            "coherence_cohesion": "2010 ve 2022 ayri paragraflarda, On the other hand ile karsit grup ayriliyor; ilerleme net. Gecisler mekanik: paragraflar In 2010 / In 2022 kalibiyla aciliyor.",
            "lexical_resource": "Dropped, reduction, stayed almost the same gibi yeterli cesitlilik var. Made a growth, was the last one ve less than a half esdiziim olarak tutmuyor.",
            "grammatical_range_accuracy": "Ilgi cumlecigi ve karsilastirma yapilari dogru kullanilmis, cumlelerin cogu hatasiz. Kalan hatalar (after them there was, the visits fell) anlami bozmuyor ama dikkat cekiyor.",
        }, "Siralamanin degistigini acikca yazmak: 2010'da en cok 15 yas alti, 2022'de 60 yas ustu. Bu tek cumle gorev yanitini belirgin bicimde yukari tasir."),
        (8.0, AT02_8, {
            "task_response": "Genel bakis uc seyi birden soyluyor: toplam dusus, dususun 45 yas altiyla sinirli olmasi ve birinci siranin el degistirmesi. Secilen rakamlar bu bulgulari destekliyor, gereksiz hucre okumasi yok.",
            "coherence_cohesion": "Metin yillara gore degil, bulguya gore duzenlenmis: once yer degistiren birincilik, sonra en keskin dusus, sonra istikrarli grup. Baglantilar cogunlukla referans ve zaman ifadeleriyle kuruluyor, kalip baglayiciyla degil.",
            "lexical_resource": "Confined to, accounting for, edging up, proportionally less severe gibi az kullanilan ogeler dogru yerde. A mere 1.4 million secimi vurguyu tasiyor.",
            "grammatical_range_accuracy": "Past perfect, ilgi cumlecigi (whose visits more than halved) ve karsitlik yapilari kontrollu. Hata seyrek; cumle uzunlugu bilincli olarak degisiyor.",
        }, "Toplamlari yalnizca kapanista degil, dususun buyuklugunu okura erken hissettirecek bir yerde de kullanmak (ornegin yuzde olarak toplam dusus)."),
    ]),
    ("AT03", [
        (5.0, AT03_5, {
            "task_response": "Bes dilim iki yil icin tek tek okunuyor ama en carpici degisimin cihazlar oldugu bir bulgu olarak one cikarilmiyor. Son cumle pastalarin pay gosterdigini unutup use more electricity diyor ve grafikte olmayan bir aciklama ekliyor.",
            "coherence_cohesion": "Firstly / Secondly / Thirdly sadece siralama isareti; paragraflar arasi mantik bagi kurulmuyor. Yine de 1990 ve 2020 ayri ayri ele alindigi icin izlenebilir.",
            "lexical_resource": "Big, small, go down disina cikan pay sozcugu yok; percentage, proportion, share hic gecmiyor. Not so big like before gibi yanlis karsilastirma kaliplari var.",
            "grammatical_range_accuracy": "Uyum ve tanimlik hatalari yayginlasmis: the two pie chart shows, a average home, the appliances is, this three is small. Zaman secimi bastan sona genis zaman, gecmis anlatimi yok.",
        }, "Sonuc cumlesini atip yerine 'isitmanin payi kucularak yerini cihazlara birakti' diyen bir genel bakis yazmak, ve butun cumlelerde tekil-cogul uyumunu duzeltmek."),
        (6.5, AT03_65, {
            "task_response": "Genel bakis isitmanin dususunu ve cihazlarin yukselisini birlikte soyluyor; butun kategoriler rakamla veriliyor ve siralama degisimi fark edilmis. It lost 14% ifadesi yuzde ile yuzde puanini karistiriyor, bu bir olcu hatasi.",
            "coherence_cohesion": "Yillara gore paragraf bolumu net, kapanis cumlesi metni topluyor. In the second position kalibinin tekrari akisi biraz mekaniklestiriyor.",
            "lexical_resource": "Took, climbed, decreased, category, purpose gibi gorev icin uygun sozcukler var. The third one ve for this reason yerine oturmuyor.",
            "grammatical_range_accuracy": "Ilgi cumlecigi ve karsitlik baglaclari dogru; cumlelerin cogu hatasiz. Kalan hatalar okuru durdurmuyor.",
        }, "Yuzde farklarini percentage points olarak yazmak; boylece pay grafiginde en sik yapilan olcu hatasindan kurtulur."),
        (8.0, AT03_8, {
            "task_response": "Genel bakis yalnizca degisimi degil, kaybedilen payin nereye gittigini soyluyor. Kategoriler secilerek ele aliniyor, siralama degisimi ve degismeyenler ayri ayri kaydediliyor.",
            "coherence_cohesion": "Thirty years later gecisi iki grafigi tek anlatiya baglıyor. Then ve The overall pattern gibi isaretler seyrek ama tam yerinde.",
            "lexical_resource": "Dominant, shrank, slice, absorbed, contracted, concentrated on gibi ogeler dogal esdiziimle kullanilmis. Nearly two thirds gibi yaklasik ifadeler pay diline uygun.",
            "grammatical_range_accuracy": "Ic ice yerlestirilmis ilgi cumlecikleri ve past perfect kontrollu bicimde isliyor. Hata seyrek; cumleler uzun ama okunakliligini koruyor.",
        }, "Bes kategorinin toplaminin her iki yilda da %100 oldugunu acikca isaretlemek; pay grafiginde bu, okurun sayilari dogru cerceveye oturtmasini saglar."),
    ]),
    ("AT04", [
        (5.0, AT04_5, {
            "task_response": "Tablodaki her hucre sirayla okunuyor; en buyuk artis ile en buyuk dusus secilmis degil, listenin icinde kaybolmus. Iki sutun ayri ayri anlatiliyor ama pay ile sure arasinda hicbir baglanti kurulmuyor ve genel bakis yok.",
            "coherence_cohesion": "Thirdly, about the minutes gibi bir baslik cumlesi disinda baglanti yok. Paragraf bolumu var, bu yuzden okur yine de nerede oldugunu biliyor.",
            "lexical_resource": "Go up, go down, two time more, the most fast ile sinirli bir kume tekrar ediyor. Popular disinda pay anlatan sozcuk yok.",
            "grammatical_range_accuracy": "Uyum ve zaman hatalari yaygin: it go down, the train don't change, the car need, in the two year. Yapilarin tamami basit cumle.",
        }, "Metnin basina 'otomobil payini kaybetti, bisiklet iki katina cikti' diyen bir genel bakis koymak ve bastan sona gecmis zamana gecmek."),
        (6.5, AT04_65, {
            "task_response": "Genel bakis hem pay degisimini hem de en uzun sureyi soyluyor; her iki sutun da kullaniliyor. Sure sutunu yalnizca siralaniyor, en cok buyuyen turun suresiyle iliskisi kurulmuyor.",
            "coherence_cohesion": "2015, 2023 ve sureler ayri paragraflarda; ilerleme net. About the time gecisi biraz kaba, konusma diline yakin.",
            "lexical_resource": "Share, fall, growth, decreased slightly gibi uygun ogeler var. Became two times bigger ve passed the walking esdiziim olarak zorlama.",
            "grammatical_range_accuracy": "Ilgi cumlecigi ve karsilastirmalar dogru kurulmus, cumlelerin cogu hatasiz. Kalan hatalar anlami engellemiyor.",
        }, "Sure sutununu paylarla birlestiren tek bir cumle eklemek: en cok buyuyen tur olan bisiklet otomobilden yalnizca alti dakika daha uzun suruyor."),
        (8.0, AT04_8, {
            "task_response": "Genel bakis iki sutunu birden yorumluyor ve sure ile yayginlik arasinda iliski olmadigini soyluyor; bu tablodan cikarilmasi gereken asil bulgu. Secilen rakamlar en buyuk hareketi ve en carpici karsitligi destekliyor.",
            "coherence_cohesion": "Paylar ve sureler ayri ama birbirine bagli iki blok halinde; Turning to duration gecisi net. Cumleler arasi baglanti cogunlukla anlamla kuruluyor, kalip baglayiciyla degil.",
            "lexical_resource": "Lost ground, car-dependent, picked up, climbing five points, held steady, slipped marginally gibi ogeler dogal ve dogru. Much the slowest gibi vurgu bicimleri esnek.",
            "grammatical_range_accuracy": "Iki noktali aciklama, zit yapilar ve ortac kullanimi kontrollu; cumlelerin buyuk cogunlugu hatasiz. Uzun cumleler okunurlugu bozmuyor.",
        }, "Iki yilda da paylarin toplaminin 100 oldugunu isaretlemek ve bir turun artisinin digerinin kaybindan geldigini acikca soylemek."),
    ]),
    ("AT05", [
        (5.0, AT05_5, {
            "task_response": "Dokuz asamanin cogu siraya uygun veriliyor ama surecin butunu (iki cikisla bitmesi, insansiz olmasi) hicbir yerde ozetlenmiyor. Son cumle semada olmayan bir bilgi ekliyor: para ve tasarruf.",
            "coherence_cohesion": "Firstly / Secondly / Thirdly / Finally kalibi var ve sira dogru, bu yuzden surec izlenebiliyor. Ama asamalar arasi baglanti bu dort sozcugun disina cikmiyor.",
            "lexical_resource": "Take ve go fiilleri butun asamalari tasiyor; collect, filter, store gibi surece ozgu sozcukler tekrar edilmiyor. For save the water bicim hatasi.",
            "grammatical_range_accuracy": "Edilgen cati denenip birakiliyor (is collect and clean) ve uyum hatalari her paragrafta var: it go, it kill, a ultraviolet unit. Yapilar basit cumleden ibaret.",
        }, "Edilgen catiyi duzgun kurmak (is collected, is filtered) ve son cumleyi atip yerine surecin nerede baslayip nerede bittigini soyleyen bir genel bakis yazmak."),
        (6.5, AT05_65, {
            "task_response": "Butun asamalar dogru sirada ve dogru adlarla veriliyor; tasma kolu ve iki ayri kullanim noktasi atlanmamis. Genel bakis var ama asama sayisini saymakla yetiniyor, surecin nasil isledigini soylemiyor.",
            "coherence_cohesion": "First of all, After that, In the next stage, Finally zinciri dogru ve takip edilebilir, ama tahmin edilebilir bicimde mekanik. Paragraflar toplama, depolama ve aritma asamalarina gore ayrilmis.",
            "lexical_resource": "Collect, store, distribute, treatment unit gibi uygun sozcukler var. Arrives to ve cleans the small particles esdiziim olarak yanlis.",
            "grammatical_range_accuracy": "Edilgen cati bastan sona dogru kullanilmis, ilgi cumlecikleri isliyor. Kalan hatalar sayica az ve anlami engellemiyor.",
        }, "Genel bakisi asama saymaktan cikarip surecin ozelligini soyleyecek bicimde yazmak: dogrusal, tek makine kullaniyor ve iki farkli cikisla bitiyor."),
        (8.0, AT05_8, {
            "task_response": "Genel bakis surecin sekli hakkinda konusuyor: dogrusal, neredeyse insansiz, iki cikisli ve iki asamali aritma. Butun asamalar kapsanmis, tasma kolu ve icme suyu olmadigi bilgisi de dahil.",
            "coherence_cohesion": "Asamalar toplama, depolama, aritma ve dagitim olarak gruplanmis; At the start, When the water is needed, Finally gecisleri gerektigi kadar. Referans sozcukleri (it, this tank) net.",
            "lexical_resource": "Captured, channelled, strained out, surplus, exposed to, fit for drinking gibi ogeler dogal ve tam yerinde. Mechanical / designed to remove bacteria ayrimi aritmayi ozetliyor.",
            "grammatical_range_accuracy": "Edilgen cati, zaman cumlecikleri ve amac yapisi (in order to) esnek bicimde donusuyor. Hata seyrek; At no stage ile kurulan devrik kapanis kontrollu.",
        }, "Asamalarin kac tane oldugunu bir kez sayiyla vermek ve pompanin surecin tek mekanik parcasi olduguna daha erken isaret etmek."),
    ]),
]


def main():
    os.makedirs(HEDEF, exist_ok=True)
    for kod, cevaplar in VERI:
        answers = []
        for band, metin, neden, yukselt in cevaplar:
            n = _say(metin)
            if n < 150:
                raise SystemExit("%s band %s: %d kelime, 150'nin altinda" % (kod, band, n))
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
