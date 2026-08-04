# Gecici yardimci: OPUS5-21 / L6 tam test sorularini uretir ve kendi kendini denetler.
# Is bitince silinir.
import json
import re
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
SENARYO = KOK / "content" / "listening" / "scripts"
CIKTI = KOK / "content" / "listening" / "tests" / "L6"

S = {n: json.loads((SENARYO / f"L6-S{n}.json").read_text(encoding="utf-8")) for n in (1, 2, 3, 4)}


def yaz(ad, veri):
    CIKTI.mkdir(parents=True, exist_ok=True)
    yol = CIKTI / ad
    yol.write_text(json.dumps(veri, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return yol


# --------------------------------------------------------------------------
# 1. bolum: form tamamlama (1-10)
# --------------------------------------------------------------------------
form_stem = (
    "ARDLEIGH COLLEGE - HALL OF RESIDENCE APPLICATION\n"
    "\n"
    "Applicant\n"
    "Surname: (1) ........\n"
    "Course: (2) ........ (three-year programme)\n"
    "Address: (3) ........, Marsden\n"
    "\n"
    "Halls open to first-year applicants\n"
    "Thornbury Hall: closed to applicants this year - the building is being (4) ........\n"
    "Wharton Court: study bedroom, kitchen shared with five other students, £118 a week\n"
    "Cadnam House: bigger kitchens; every room is (5) ........\n"
    "Rent at Cadnam House from September: £(6) ........ a week\n"
    "\n"
    "Contract (38 weeks)\n"
    "Rooms are emptied over the spring break, but (7) ........ may be left in the basement store room\n"
    "Completed form must reach the office by (8) ........ June\n"
    "\n"
    "Arrival\n"
    "Keys are handed out at the (9) ........ on Cadnam Street\n"
    "Write reference (10) ........ on anything sent to the office"
)

form_items = [
    dict(number=1, prompt="Surname: (1) ........",
         answer=["Brathwaite"], accepted_variants=["Brathwaite"],
         evidence="It's Brathwaite — B-R-A-T-H-W-A-I-T-E.",
         answer_point_id="L6-S1-01", turn_index=5, distractor_used=None,
         explanation="Soyadı seste harf harf söyleniyor: B-R-A-T-H-W-A-I-T-E; öğrenci ortada fazladan harf olmadığını da ekliyor.",
         difficulty="easy"),
    dict(number=2, prompt="Course: (2) ........ (three-year programme)",
         answer=["Environmental Engineering"],
         accepted_variants=["Environmental Engineering", "environmental engineering"],
         evidence="Environmental Engineering. It's the three-year one",
         answer_point_id="L6-S1-02", turn_index=7, distractor_used=None,
         explanation="Öğrenci bölümünü söyleyip hemen ardından üç yıllık programda olduğunu belirtiyor; yerleştirmeli dört yıllık sürümü almıyor.",
         difficulty="easy"),
    dict(number=3, prompt="Address: (3) ........, Marsden",
         answer=["22 Hartlow Road"],
         accepted_variants=["22 Hartlow Road", "22 Hartlow Rd"],
         evidence="It's twenty-two Hartlow Road, in Marsden.",
         answer_point_id="L6-S1-05", turn_index=13, distractor_used=None,
         explanation="Adres yazıyla söyleniyor: yirmi iki Hartlow Road; şehir adı (Marsden) formda zaten verilmiş durumda.",
         difficulty="easy"),
    dict(number=4, prompt="Thornbury Hall: closed to applicants this year - the building is being (4) ........",
         answer=["re-roofed"],
         accepted_variants=["re-roofed", "reroofed", "re roofed"],
         evidence="Thornbury is being re-roofed over the winter, so we've taken it out of the offer this year",
         answer_point_id="L6-S1-06", turn_index=16, distractor_used=None,
         explanation="Öğrencinin arkadaşı Thornbury'yi önerse de yurt bu yıl başvuruya kapalı: kış boyunca çatısı yenileniyor.",
         difficulty="medium"),
    dict(number=5, prompt="Cadnam House: bigger kitchens; every room is (5) ........",
         answer=["en-suite"],
         accepted_variants=["en-suite", "ensuite", "en suite"],
         evidence="the rooms there are en-suite — you have your own shower room",
         answer_point_id="L6-S1-09", turn_index=20, distractor_used=None,
         explanation="Cadnam House daha yeni blok olduğu için odaların kendi duş odası var; danışman bunu en-suite diye adlandırıyor.",
         difficulty="medium"),
    dict(number=6, prompt="Rent at Cadnam House from September: £(6) ........ a week",
         answer=["145"],
         accepted_variants=["145", "£145", "145 pounds"],
         evidence="from September it's a hundred and forty-five, I'm afraid",
         answer_point_id="L6-S1-12", turn_index=24, distractor_used="132",
         explanation="Öğrenci sitedeki yüz otuz iki rakamını hatırlatıyor ama o geçen yıla ait; Eylül'den itibaren en-suite oda haftada yüz kırk beş pound.",
         difficulty="medium"),
    dict(number=7, prompt="Rooms are emptied over the spring break, but (7) ........ may be left in the basement store room",
         answer=["one box"],
         accepted_variants=["one box", "1 box"],
         evidence="You can leave one box in the store room in the basement, but otherwise the rooms have to be cleared.",
         answer_point_id="L6-S1-14", turn_index=28, distractor_used=None,
         explanation="Sözleşme kısaldığı için yurtlar bahar tatilinde kapanıyor; bodrumdaki depoya kişi başı yalnızca bir kutu bırakılabiliyor.",
         difficulty="medium"),
    dict(number=8, prompt="Completed form must reach the office by (8) ........ June",
         answer=["30"],
         accepted_variants=["30", "30th", "thirtieth", "the thirtieth"],
         evidence="For accommodation you've got until the thirtieth.",
         answer_point_id="L6-S1-17", turn_index=32, distractor_used="23",
         explanation="Öğrencinin not aldığı yirmi üç burs başvurusunun son günü; konaklama formu için son tarih Haziran'ın otuzu.",
         difficulty="medium"),
    dict(number=9, prompt="Keys are handed out at the (9) ........ on Cadnam Street",
         answer=["porter's lodge"],
         accepted_variants=["porter's lodge", "porters lodge", "porter’s lodge"],
         evidence="From the porter's lodge on Cadnam Street.",
         answer_point_id="L6-S1-22", turn_index=40, distractor_used="main reception",
         explanation="Çoğu öğrenci önce ana resepsiyona gidiyor ama anahtarlar orada durmuyor; anahtarlar Cadnam Street'teki kapıcılık odasından alınıyor.",
         difficulty="medium"),
    dict(number=10, prompt="Write reference (10) ........ on anything sent to the office",
         answer=["HR 942"],
         accepted_variants=["HR 942", "HR942", "H-R 942", "HR-942"],
         evidence="your reference is H-R, nine four two",
         answer_point_id="L6-S1-31", turn_index=52, distractor_used=None,
         explanation="Görüşmenin sonunda verilen başvuru referansı H-R ve dokuz dört iki; öğrenci de tekrarlayarak doğruluyor.",
         difficulty="easy"),
]

form = dict(
    schema_version="1.0", set_id="L6-form-completion", skill="listening", test_id="L6",
    section=1, practice=False, script_id="L6-S1", question_type="form_completion",
    generated_by="opus",
    instructions="Complete the form below. Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each answer.",
    word_limit="NO MORE THAN TWO WORDS AND/OR A NUMBER",
    options=None, visual=None, stem_block=form_stem, table=None, items=form_items,
)

# --------------------------------------------------------------------------
# 2. bolum: plan etiketleme (16-20) - kelime yazma alt tipi
# --------------------------------------------------------------------------
O = []          # svg ogeleri
CIZ = 'fill="none" stroke="#000" stroke-width="1"'


def dikdortgen(x, y, w, h):
    O.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" {CIZ}/>')


def cizgi(x1, y1, x2, y2):
    O.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#000" stroke-width="1"/>')


def yazi(x, y, s, hiza="middle"):
    O.append(f'<text x="{x}" y="{y}" text-anchor="{hiza}">{s}</text>')


# kuzey oku
cizgi(32, 82, 32, 40)
O.append('<polygon points="32,28 26,42 38,42" fill="none" stroke="#000" stroke-width="1"/>')
yazi(32, 100, "N")
# yukleme avlusu (salonun arkasi)
dikdortgen(200, 20, 220, 55)
yazi(310, 52, "LOADING YARD")
# salon duvarlari (dogu duvarinda iki kapi bosluğu, guney duvarinda ana giris)
cizgi(60, 90, 560, 90)
cizgi(60, 90, 60, 600)
cizgi(560, 90, 560, 140)
cizgi(560, 180, 560, 390)
cizgi(560, 430, 560, 600)
cizgi(60, 600, 285, 600)
cizgi(355, 600, 560, 600)
# tuvaletler: dogu duvarindaki yesil tabelali kapidan gecilen ek oda
cizgi(560, 130, 615, 130)
cizgi(615, 130, 615, 190)
cizgi(615, 190, 560, 190)
yazi(588, 164, "toilets")
yazi(585, 414, "side door")
# danisma masasi ve 16 numarali bosluk (girisin iki yani)
dikdortgen(170, 542, 100, 44)
yazi(220, 562, "INFORMATION")
yazi(220, 578, "DESK")
dikdortgen(370, 542, 100, 44)
yazi(420, 570, "16")
# bati duvarindaki uzun tezgah: peynir (kuzey) + ekmek ve pasta (guney)
dikdortgen(90, 350, 100, 170)
cizgi(90, 435, 190, 435)
yazi(140, 385, "CHEESE")
yazi(140, 401, "COUNTER")
yazi(140, 468, "BREAD &amp;")
yazi(140, 484, "CAKE STALL")
# 17 numarali bosluk: sol koridorun en ucu (kuzeybati kose)
dikdortgen(90, 150, 100, 100)
yazi(140, 205, "17")
# ortadaki iki sebze sirasi
dikdortgen(230, 300, 90, 220)
yazi(275, 398, "VEGETABLE")
yazi(275, 414, "STALLS")
dikdortgen(345, 300, 90, 220)
yazi(390, 398, "VEGETABLE")
yazi(390, 414, "STALLS")
# bal ve receller: sebze siralari ile yan kapi arasinda
dikdortgen(460, 330, 90, 100)
yazi(505, 372, "HONEY &amp;")
yazi(505, 388, "PRESERVES")
# 18 numarali bosluk: en uctaki saatin altinda
O.append('<circle cx="330" cy="103" r="9" fill="none" stroke="#000" stroke-width="1"/>')
yazi(398, 107, "clock")
dikdortgen(250, 115, 160, 70)
yazi(330, 155, "18")
# oturma alani
dikdortgen(250, 200, 160, 70)
yazi(330, 228, "SEATING AREA")
yazi(330, 244, "(24 chairs)")
# 19 numarali bosluk: oturma alaninin arkasi, kuzeydogu kose
dikdortgen(450, 115, 100, 80)
yazi(500, 158, "19")
# giris oku (salonun icine dogru)
cizgi(320, 590, 320, 552)
O.append('<polygon points="320,540 314,554 326,554" fill="none" stroke="#000" stroke-width="1"/>')
yazi(320, 618, "MAIN")
yazi(320, 632, "ENTRANCE")
# bahce kapisi ve giris yolu
cizgi(100, 640, 285, 640)
cizgi(355, 640, 520, 640)
yazi(370, 633, "GATE")
cizgi(285, 600, 285, 710)
cizgi(355, 600, 355, 710)
# 20 numarali bosluk: kapinin disinda
dikdortgen(380, 655, 100, 42)
yazi(430, 681, "20")
# cadde
cizgi(30, 710, 590, 710)
yazi(310, 730, "PEVERIL STREET")

svg = ('<svg viewBox="0 0 620 740" xmlns="http://www.w3.org/2000/svg" '
       'font-family="sans-serif" font-size="12">' + "".join(O) + "</svg>")

plan_items = [
    dict(number=16, prompt="Space 16 on the plan",
         answer=["flower stall"], accepted_variants=["flower stall"],
         evidence="Opposite the information desk, on your right, is the flower stall.",
         answer_point_id="L6-S2-12", turn_index=5, distractor_used=None,
         explanation="Girişin hemen solunda etiketli danışma masası var; çiçek tezgâhı onun tam karşısında, yani girişe göre sağda.",
         difficulty="easy"),
    dict(number=17, prompt="Space 17 on the plan",
         answer=["fish counter"], accepted_variants=["fish counter"],
         evidence="it's at the far end of the left-hand aisle, because that corner is the only part of the building with proper drainage",
         answer_point_id="L6-S2-16", turn_index=6, distractor_used="by the entrance",
         explanation="Konuşmacı balık tezgâhının eskisi gibi girişin yanında olmadığını söylüyor: uygun drenaj yalnızca o köşede olduğu için tezgâh sol koridorun en ucunda.",
         difficulty="medium"),
    dict(number=18, prompt="Space 18 on the plan",
         answer=["demonstration kitchen"],
         accepted_variants=["demonstration kitchen"],
         evidence="Straight ahead of you, at the far end under the clock, is the demonstration kitchen",
         answer_point_id="L6-S2-19", turn_index=7, distractor_used=None,
         explanation="Gösteri mutfağı kapıdan bakınca tam karşıda, salonun en ucunda ve planda çizili saatin altındadır; oturma alanı onun önünde yer alıyor.",
         difficulty="easy"),
    dict(number=19, prompt="Space 19 on the plan",
         answer=["refill shop"], accepted_variants=["refill shop", "re-fill shop"],
         evidence="Behind the seating area, in the north-east corner, you'll find the refill shop",
         answer_point_id="L6-S2-21", turn_index=8, distractor_used=None,
         explanation="Dolum dükkânı etiketli oturma alanının arkasında, kuzeydoğu köşededir; tuvaletlere de oradaki kapıdan geçiliyor.",
         difficulty="medium"),
    dict(number=20, prompt="Space 20 on the plan",
         answer=["cycle racks"], accepted_variants=["cycle racks", "cycle rack"],
         evidence="The only thing outside the gate is the cycle racks",
         answer_point_id="L6-S2-23", turn_index=8, distractor_used="the loading yard behind the hall",
         explanation="Bisiklet park yeri salonun içinde değil, bahçe kapısının dışındadır; arkadaki yükleme avlusu yalnızca satıcıların araçlarına ait.",
         difficulty="medium"),
]

plan = dict(
    schema_version="1.0", set_id="L6-plan-map-diagram-labelling", skill="listening", test_id="L6",
    section=2, practice=False, script_id="L6-S2", question_type="plan_map_diagram_labelling",
    generated_by="opus",
    instructions="Label the plan below. Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each answer.",
    word_limit="NO MORE THAN TWO WORDS AND/OR A NUMBER",
    options=None,
    visual=dict(
        kind="plan", svg=svg,
        alt=("Peveril Street'teki kapalı haldeki çiftçi pazarının zemin planı. Ana giriş (güneyde, "
             "Peveril Street'e bakan kapı), danışma masası, ekmek ve pasta tezgâhı ile peynir tezgâhı, "
             "ortadaki iki sebze sırası, bal ve reçel tezgâhı, yan kapı, oturma alanı, saat, tuvaletler, "
             "yükleme avlusu, bahçe kapısı ve kuzey oku etiketlidir; 16-20 numaralı beş yer etiketsiz "
             "bırakılmıştır. Kuzey yukarıda, giriş aşağıda; girişteki ok salonun içine bakar."),
        labels=["16", "17", "18", "19", "20"],
    ),
    stem_block=None, table=None, items=plan_items,
)

# --------------------------------------------------------------------------
# 3. bolum: cumle tamamlama (27-30)
# --------------------------------------------------------------------------
cumle_items = [
    dict(number=27, prompt="Reading the abstracts should bring the list down to about (27) ........ studies.",
         answer=["30"], accepted_variants=["30", "thirty"],
         evidence="Screen the abstracts down to roughly thirty studies.",
         answer_point_id="L6-S3-22", turn_index=27, distractor_used="86",
         explanation="Seksen altı, kütüphanecinin sabah denediği aramanın ilk veri tabanında verdiği sonuç sayısı; özetler elendikten sonra geriye yaklaşık otuz çalışma kalması bekleniyor.",
         difficulty="medium"),
    dict(number=28, prompt="Reasons for rejecting an item have to be written on the (28) ........ from the module page.",
         answer=["screening sheet"], accepted_variants=["screening sheet"],
         evidence="There's a screening sheet on the module page — use it, and write down why you rejected each item.",
         answer_point_id="L6-S3-26", turn_index=31, distractor_used=None,
         explanation="Kütüphaneci ders sayfasındaki eleme formunun kullanılmasını ve elenen her kaynağın gerekçesinin yazılmasını istiyor.",
         difficulty="easy"),
    dict(number=29, prompt="In the reference software the students should set up a (29) ........ so that their records all go to the same place.",
         answer=["group library"], accepted_variants=["group library"],
         evidence="set up a group library so you're both adding to the same one",
         answer_point_id="L6-S3-29", turn_index=35, distractor_used=None,
         explanation="Ortak klasör yerine kaynak yönetim yazılımı öneriliyor; ikisinin de aynı yere eklemesi için bir grup kütüphanesi kurmaları gerekiyor.",
         difficulty="medium"),
    dict(number=30, prompt="No more than (30) ........ can be downloaded from a database in one go.",
         answer=["200 records"], accepted_variants=["200 records", "200"],
         evidence="Two hundred records at a time, that's the limit.",
         answer_point_id="L6-S3-32", turn_index=39, distractor_used=None,
         explanation="Dışarı aktarma işlemi seferde iki yüz kayıtla sınırlı; kütüphaneci bunu aramanın kaydedilmesi uyarısıyla birlikte veriyor.",
         difficulty="medium"),
]

cumle = dict(
    schema_version="1.0", set_id="L6-sentence-completion", skill="listening", test_id="L6",
    section=3, practice=False, script_id="L6-S3", question_type="sentence_completion",
    generated_by="opus",
    instructions="Complete the sentences below. Write NO MORE THAN TWO WORDS AND/OR A NUMBER for each answer.",
    word_limit="NO MORE THAN TWO WORDS AND/OR A NUMBER",
    options=None, visual=None, stem_block=None, table=None, items=cumle_items,
)

# --------------------------------------------------------------------------
# 4. bolum, birinci blok: not tamamlama (31-36)
# --------------------------------------------------------------------------
not_stem = (
    "BEHAVIOURAL ECONOMICS\n"
    "\n"
    "The standard model\n"
    "- a decision-maker whose preferences never change\n"
    "- someone who holds every piece of information needed\n"
    "- attention that is (31) ........\n"
    "\n"
    "Reference points\n"
    "- an outcome is read as a gain or a loss from where we happen to be\n"
    "- the ratio of a loss to a gain of the same size is nearer (32) ........ than the figure usually quoted\n"
    "\n"
    "Framing\n"
    "- one rail company printed the same punctuality figures two ways\n"
    "- the negative version almost doubled the number of (33) ........ in the month that followed\n"
    "\n"
    "Defaults\n"
    "- form needed in order to join a workplace savings scheme: about one in four took part\n"
    "- automatic enrolment, form needed in order to leave: about (34) ........ took part\n"
    "\n"
    "Why a default works\n"
    "- effort: even a trivial obstacle reduces the numbers\n"
    "- the default quietly says what is normal\n"
    "- (35) ........: the intention to act is never carried out\n"
    "\n"
    "Present bias\n"
    "- staff agree now to save more, but the extra money is only taken from the (36) ........"
)

not_items = [
    dict(number=31, prompt="- attention that is (31) ........",
         answer=["unlimited"], accepted_variants=["unlimited"],
         evidence="The standard model assumes a decision-maker with stable preferences, complete information and unlimited attention.",
         answer_point_id="L6-S4-01", turn_index=0, distractor_used=None,
         explanation="Standart modelin üç varsayımı sıralanıyor; notlarda boş bırakılan üçüncüsü sınırsız dikkat.",
         difficulty="easy"),
    dict(number=32, prompt="- the ratio of a loss to a gain of the same size is nearer (32) ........ than the figure usually quoted",
         answer=["two to one"],
         accepted_variants=["two to one", "2 to 1", "2:1", "two-to-one"],
         evidence="The careful estimates actually put it closer to two to one",
         answer_point_id="L6-S4-05", turn_index=1, distractor_used="three to one",
         explanation="Öğretim üyesi yaygın olarak aktarılan üçe bir oranını düzeltiyor: dikkatli tahminler ikiye bire daha yakın.",
         difficulty="medium"),
    dict(number=33, prompt="- the negative version almost doubled the number of (33) ........ in the month that followed",
         answer=["complaints"], accepted_variants=["complaints"],
         evidence="the second version produced nearly twice as many complaints over the following month",
         answer_point_id="L6-S4-08", turn_index=2, distractor_used=None,
         explanation="Aynı dakiklik bilgisi olumsuz ifade edildiğinde izleyen ay gelen şikâyet sayısı neredeyse ikiye katlanıyor.",
         difficulty="medium"),
    dict(number=34, prompt="- automatic enrolment, form needed in order to leave: about (34) ........ took part",
         answer=["nine in ten"],
         accepted_variants=["nine in ten", "9 in 10", "9 in ten", "nine in 10"],
         evidence="participation rose to roughly nine in ten",
         answer_point_id="L6-S4-10", turn_index=3, distractor_used="nobody opted out",
         explanation="Otomatik kayıtta katılım onda dokuza çıkıyor; o dönemde aktarılan hiç kimsenin çıkmadığı iddiası ise doğru değil.",
         difficulty="medium"),
    dict(number=35, prompt="- (35) ........: the intention to act is never carried out",
         answer=["delay"], accepted_variants=["delay"],
         evidence="The third is delay. Most people intend to deal with the form, and go on intending it.",
         answer_point_id="L6-S4-14", turn_index=4, distractor_used=None,
         explanation="Varsayılan seçeneğin işe yaramasının üçüncü nedeni erteleme: insanlar formu doldurmaya niyetlenir ama niyette kalır.",
         difficulty="easy"),
    dict(number=36, prompt="- staff agree now to save more, but the extra money is only taken from the (36) ........",
         answer=["next pay rise"],
         accepted_variants=["next pay rise", "pay rise", "next pay-rise"],
         evidence="with the extra contribution starting only when their next pay rise arrives",
         answer_point_id="L6-S4-16", turn_index=5, distractor_used=None,
         explanation="Bugüne yönelik yanlılığı aşmak için ek katkı bugünkü maaştan değil, bir sonraki zamdan itibaren alınıyor.",
         difficulty="medium"),
]

notlar = dict(
    schema_version="1.0", set_id="L6-note-completion", skill="listening", test_id="L6",
    section=4, practice=False, script_id="L6-S4", question_type="note_completion",
    generated_by="opus",
    instructions="Complete the notes below. Write NO MORE THAN THREE WORDS AND/OR A NUMBER for each answer.",
    word_limit="NO MORE THAN THREE WORDS AND/OR A NUMBER",
    options=None, visual=None, stem_block=not_stem, table=None, items=not_items,
)

# --------------------------------------------------------------------------
# 4. bolum, ikinci blok: ozet tamamlama (37-40)
# --------------------------------------------------------------------------
ozet_stem = (
    "NUDGES IN PUBLIC POLICY, AND HOW THEY ARE TESTED\n"
    "\n"
    "Households behind with a bill were sent a letter saying that most of their neighbours had "
    "already paid, and payment rates went up. How far up is disputed: the figure the papers "
    "carried came from one pilot in a single town, while the larger trials put the rise at about "
    "(37) ........ percentage points. Repeating an intervention across many sites usually leaves "
    "an effect only around (38) ........ the size of the one first published, partly because "
    "striking results are easier to publish than dull ones, and some effects fade once the "
    "novelty has gone. There is also the question of who chooses the default, since that person "
    "has interests of their own; what separates help from obstruction is whether the arrangement "
    "advances the (39) ........ of the individual concerned. Method matters as well: allocating "
    "real customers at random is what shows that the wording caused the difference, and "
    "(40) ........ the prediction openly in advance keeps the analysis from being reworked later."
)

ozet_items = [
    dict(number=37, prompt="the larger trials put the rise at about (37) ........ percentage points",
         answer=["five"], accepted_variants=["five", "5"],
         evidence="Across the larger trials the effect settles at about five percentage points",
         answer_point_id="L6-S4-21", turn_index=7, distractor_used="fifteen",
         explanation="Gazetelere yansıyan on beş puanlık artış tek bir kasabadaki pilot uygulamadan geliyor; geniş denemelerde etki beş puan civarında kalıyor.",
         difficulty="medium"),
    dict(number=38, prompt="Repeating an intervention across many sites usually leaves an effect only around (38) ........ the size of the one first published",
         answer=["half"], accepted_variants=["half"],
         evidence="the average effect is often around half of what the original study reported",
         answer_point_id="L6-S4-24", turn_index=8, distractor_used=None,
         explanation="Aynı müdahale çok sayıda yerde tekrarlandığında ortalama etki, ilk çalışmanın bildirdiğinin yaklaşık yarısı kadar çıkıyor.",
         difficulty="medium"),
    dict(number=39, prompt="what separates help from obstruction is whether the arrangement advances the (39) ........ of the individual concerned",
         answer=["goals"], accepted_variants=["goals"],
         evidence="the usual one is whether the person's own goals are being served",
         answer_point_id="L6-S4-29", turn_index=9, distractor_used=None,
         explanation="Yönlendirme ile engel çıkarmayı ayırt etmek için sorulan olağan soru, kişinin kendi hedeflerine hizmet edilip edilmediğidir.",
         difficulty="medium"),
    dict(number=40, prompt="(40) ........ the prediction openly in advance keeps the analysis from being reworked later",
         answer=["registering"], accepted_variants=["registering"],
         evidence="registering your prediction publicly before you collect the data is what stops the analysis being adjusted afterwards",
         answer_point_id="L6-S4-33", turn_index=10, distractor_used=None,
         explanation="Yöntem bölümünün ikinci güvencesi: tahminin veri toplanmadan önce açıkça kaydedilmesi, sonradan analizin değiştirilmesini engelliyor.",
         difficulty="hard"),
]

ozet = dict(
    schema_version="1.0", set_id="L6-summary-completion", skill="listening", test_id="L6",
    section=4, practice=False, script_id="L6-S4", question_type="summary_completion",
    generated_by="opus",
    instructions="Complete the summary below. Write ONE WORD AND/OR A NUMBER for each answer.",
    word_limit="ONE WORD AND/OR A NUMBER",
    options=None, visual=None, stem_block=ozet_stem, table=None, items=ozet_items,
)

DOSYALAR = [("form-completion.json", form, 1), ("plan-map-diagram-labelling.json", plan, 2),
            ("sentence-completion.json", cumle, 3), ("note-completion.json", notlar, 4),
            ("summary-completion.json", ozet, 4)]


# --------------------------------------------------------------------------
# Denetim
# --------------------------------------------------------------------------
def kelime_say(cev):
    parcalar = [p for p in cev.split() if p.strip()]
    kelime = [p for p in parcalar if re.search(r"[A-Za-z]", p)]
    return len(kelime)


SINIR = {"ONE WORD AND/OR A NUMBER": 1,
         "NO MORE THAN TWO WORDS AND/OR A NUMBER": 2,
         "NO MORE THAN THREE WORDS AND/OR A NUMBER": 3}

hata = []
for ad, veri, bol in DOSYALAR:
    turns = S[bol]["turns"]
    noktalar = {a["id"]: a for a in S[bol]["answer_points"]}
    onceki = -1
    for it in veri["items"]:
        n = it["number"]
        ti = it["turn_index"]
        metin = turns[ti]["text"]
        if it["evidence"] not in metin:
            hata.append(f"{ad} s{n}: evidence {ti}. replikte birebir gecmiyor")
        if ti < onceki:
            hata.append(f"{ad} s{n}: turn_index geri gidiyor ({onceki} -> {ti})")
        elif ti == onceki:
            print(f"  not: {ad} s{n} bir onceki soruyla ayni replikte (replik {ti})")
        onceki = ti
        ap = noktalar.get(it["answer_point_id"])
        if ap is None:
            hata.append(f"{ad} s{n}: answer_point_id senaryoda yok")
        elif ap["turn_index"] != ti:
            hata.append(f"{ad} s{n}: answer_point turn_index {ap['turn_index']} != {ti}")
        for cev in it["answer"] + it["accepted_variants"]:
            if kelime_say(cev) > SINIR[veri["word_limit"]]:
                hata.append(f"{ad} s{n}: '{cev}' kelime sinirini asiyor")
        for cev in it["answer"]:
            golge = cev.replace("£", "")
            if golge.lower() not in metin.lower() and not re.search(r"\d", golge):
                hata.append(f"{ad} s{n}: cevap '{cev}' replikte birebir gecmiyor")
        if not re.search(r"[a-z]", it["explanation"]) or len(it["explanation"]) < 20:
            hata.append(f"{ad} s{n}: aciklama yetersiz")
        if it["prompt"] not in (veri["stem_block"] or it["prompt"]):
            hata.append(f"{ad} s{n}: prompt stem_block icinde yok")
    if veri["stem_block"]:
        for it in veri["items"]:
            if f"({it['number']}) ........" not in veri["stem_block"]:
                hata.append(f"{ad}: stem_block'ta ({it['number']}) bosluğu yok")

numaralar = [it["number"] for _, v, _ in DOSYALAR for it in v["items"]]
if numaralar != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 16, 17, 18, 19, 20, 27, 28, 29, 30,
                 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]:
    hata.append(f"numara dizisi yanlis: {numaralar}")

for _, veri, _ in DOSYALAR:
    govde = json.dumps(veri, ensure_ascii=False)
    if "IELTS" in govde:
        hata.append(f"{veri['set_id']}: IELTS kelimesi geciyor")

for ad, veri, _ in DOSYALAR:
    yol = yaz(ad, veri)
    json.loads(yol.read_text(encoding="utf-8"))

print(f"toplam soru: {len(numaralar)}")
if hata:
    print("HATA:")
    for h in hata:
        print("  -", h)
else:
    print("denetim temiz")
