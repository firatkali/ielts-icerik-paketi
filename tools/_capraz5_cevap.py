"""Bu oturumun (5. calistirma) kor cevaplarini dogrulama/cevap/ altina yazar."""
import json
import os

CEVAP = "dogrulama/cevap"

PAKETLER = {
    "content/reading/practice/sentence-completion.json": [
        (1, ["swat flies"], 5, "A paragrafi: 'use branches to swat flies' - laboratuvar calismalari kismi."),
        (2, ["sensory contact"], 5, "G paragrafi: 'keeps the trunk tip open and in constant sensory contact with the object'."),
        (3, ["anatomy"], 5, "H paragrafi: 'the equipment offered does not suit its particular anatomy'."),
        (4, ["running seawater"], 5, "B paragrafi: 'supplied with running seawater kept at a constant 24 C'."),
        (5, ["first contact"], 5, "F paragrafi: 'took noticeably longer to make first contact ... keep a cautious distance'."),
        (6, ["unique individual"], 5, "G paragrafi: 'need not identify a unique individual ... only sort others into ... known and unknown'."),
        (7, ["laboratory tank"], 5, "A paragrafi: 'something no laboratory tank can fully replicate'."),
        (8, ["preview"], 4, "C paragrafi: 'effectively offering a preview of the future'. Tek kelime; 'a preview' bicimi de olabilir."),
        (9, ["hypothetical future"], 5, "E paragrafi: 'rather than modelling a hypothetical future, researchers can measure how a real reef community actually behaves'."),
        (10, ["seventh"], 5, "A paragrafi: 'Uranus, the seventh planet from the Sun'."),
        (11, ["forty years"], 5, "F paragrafi: 'unnoticed for the nearly forty years between that flyby and Webb's observations'."),
        (12, ["ongoing research"], 5, "H paragrafi: 'remains part of ongoing research rather than a finished, peer-reviewed result'."),
        (13, ["1952"], 5, "A paragrafi: 'it was first noticed in 1952 and then excavated in detail between 1961 and 1965'."),
        (14, ["transitional stage"], 5, "F paragrafi: 'evidence of an early, transitional stage in the cultivation of hexaploid wheat'."),
        (15, ["naked eye"], 5, "H paragrafi: 'agricultural history that is simply invisible to the naked eye'."),
    ],
    "content/reading/practice/short-answer.json": [
        (1, ["nine times"], 5, "A01 D paragrafi: 'he repeated the trick nine times within a single session' (ertesi gun)."),
        (2, ["Bay of Naples"], 5, "A02 B paragrafi: 'collected sixty octopuses from the Bay of Naples'."),
        (3, ["weeks or months"], 5, "A03 C paragrafi: 'experiments typically run for only weeks or months'."),
        (4, ["24 January 1986"], 5, "A04 F paragrafi: 'Voyager 2 spacecraft flew past Uranus on 24 January 1986'."),
        (5, ["8,400 years old"], 4, "A05 C paragrafi: 'charred grains, roughly 8,400 years old'. '8,400 years' bicimi de gecerli olabilir."),
        (6, ["transactive memory system"], 5, "A06 H paragrafi: 'the idea of a transactive memory system ... letting members find the right person to ask'."),
        (7, ["98"], 5, "A07 B paragrafi: 'the animals took part in 98 separate sessions'."),
        (8, ["Mount Logan"], 5, "A08 D paragrafi: 'around Mount Logan, Canada's tallest peak'."),
        (9, ["scanning electron microscopy"], 5, "A09 D paragrafi: 'Scanning electron microscopy allowed them to visualise the fine internal structure ... at extremely high magnification'."),
        (10, ["30-minute puzzle game"], 5, "A12 D paragrafi: 'To reduce the grogginess ... all participants completed a 30-minute puzzle game before their final recall test'."),
    ],
    "content/reading/practice/note-completion.json": [
        (1, ["47"], 5, "A06 A paragrafi: 'spread across all 47 of Japan's prefectures and 23 other countries'."),
        (2, ["operational logs"], 5, "A06 B paragrafi: uc kaynak - HR records, operational logs, internal messaging records."),
        (3, ["individual output"], 5, "A06 H paragrafi: 'Caster pays employees according to individual output alone'."),
        (4, ["Eurasian magpie"], 5, "A07 A paragrafi: 'a species of cleaner fish and, remarkably, the Eurasian magpie'."),
        (5, ["Monodontidae"], 5, "A07 G paragrafi: 'a different lineage of toothed whales, the Monodontidae'."),
        (6, ["small sample"], 5, "A07 H paragrafi: 'if only a single individual, or a small sample, is studied'."),
        (7, ["90 kilometres"], 5, "A08 A paragrafi: 'roughly 90 kilometres north of the coastal town of Yakutat'."),
        (8, ["12 December"], 5, "A08 D paragrafi: 'A ground survey carried out on 12 December confirmed what the satellite images had suggested'."),
        (9, ["surface roughness"], 5, "A08 H paragrafi: 'Without an instrument able to detect subtle changes in surface roughness from space'."),
        (10, ["500"], 5, "A09 A paragrafi: 'can reach temperatures of around 500 degrees Celsius'."),
        (11, ["wooden bed"], 5, "A09 B paragrafi: 'found lying face down on a wooden bed where he had apparently been sleeping'."),
        (12, ["skeletal remains"], 5, "A09 H paragrafi: 'detail that is almost never available from skeletal remains alone'."),
        (13, ["polysomnography"], 5, "A12 D paragrafi: 'took a 90-minute nap, during which brain activity was recorded using polysomnography'."),
        (14, ["brand-new associations"], 4, "A12 G paragrafi: 'brand-new associations with no existing link to prior knowledge'. Sadece 'new associations' da beklenebilir."),
        (15, ["unfamiliar name"], 5, "A12 H paragrafi: 'such as an unfamiliar name or a new vocabulary item studied in isolation'."),
    ],
    "content/reading/practice/summary-completion.json": [
        (1, ["popularity"], 5, "A10 D paragrafi: 'The activity-based design, despite its popularity in contemporary office trends'."),
        (2, ["absorbed"], 4, "A10 E paragrafi: 'flow, the psychological state of being deeply absorbed and focused on a task'. 'deeply absorbed' de olabilir."),
        (3, ["safe limits"], 5, "A10 F paragrafi: 'Noise levels in the open-plan office exceeded recommended safe limits'."),
        (4, ["software engineers"], 5, "A10 G paragrafi: 'experienced software engineers accustomed to their tools were not obviously slowed down or sped up'."),
        (5, ["leafy"], 5, "A11 A paragrafi: 'comes from studies conducted in green, leafy forests during spring or summer'."),
        (6, ["crossover"], 5, "A11 B paragrafi: 'took part in a crossover experiment ... in a different order depending on their group'."),
        (7, ["sharply"], 5, "A11 F paragrafi: 'the Restorative Outcome Scale, which increased sharply after time in the forest'."),
        (8, ["draining"], 5, "A11 G paragrafi: 'even a calm, traffic-free campus scene was mildly draining relative to a walk in the snow'."),
        (9, ["digital scales"], 5, "G05 B paragrafi: 'weighed the solid food waste ... using digital scales accurate to two grams'."),
        (10, ["diary"], 5, "G05 B paragrafi: 'participants kept a seven-day diary noting the type and amount of any beverage poured away'."),
        (11, ["eggshells"], 5, "G05 C paragrafi: 'inedible parts such as fruit peels, bones and eggshells'."),
        (12, ["double"], 5, "G05 D paragrafi: '79.4 kilograms ... almost double the 45.8 kilograms recorded in rural Sukajaya'."),
        (13, ["five-point"], 5, "G06 B paragrafi: 'health was self-reported on a five-point scale running from very bad to very good'."),
        (14, ["mortality"], 5, "G06 C paragrafi: 'shown it to reliably predict future illness and mortality'."),
        (15, ["elderly"], 5, "G06 D paragrafi: 'somewhat less likely to be elderly or to have migrated from another country'."),
    ],
    "content/reading/practice/diagram-labelling.json": [
        (1, ["Block C"], 5, "G01 D metni: 'General waste is collected every Monday from the bins behind Block C'."),
        (2, ["entrance hall"], 5, "G01 D metni: 'check the colour-coded calendar in the entrance hall for exact dates'."),
        (3, ["estate office"], 5, "G01 D metni: 'residents must book a separate collection through the estate office at least five working days in advance'."),
        (4, ["docking stations"], 5, "G02 A metni: 'Bicycles may be hired from any of the twelve docking stations across Millbrook'."),
        (5, ["helmets"], 5, "G02 A metni: 'Helmets are not provided and riders are responsible for their own safety equipment'."),
        (6, ["core hours"], 5, "G03 A metni: 'with core hours between 8 a.m. and 4 p.m.'."),
        (7, ["early"], 5, "G03 A metni: 'Employees on the early shift begin at 6 a.m. and finish at 2 p.m.'."),
        (8, ["15-minute"], 5, "G03 A/B metni: 'An additional 15-minute break for shifts longer than eight hours'."),
        (9, ["10 Mbps"], 5, "G04 B metni: 'Provide their own reliable internet connection of at least 10 Mbps'."),
        (10, ["instant messaging"], 3, "G04 B metni: 'Be available on instant messaging during core hours' - 'answer on' kalibina uyan tek secenek. Ama C paragrafi cekirdek saatlerde 'reachable by phone or video call' diyor ve semadaki ok telefondan cikiyor; o ifade uc kelime sinirina sigmiyor. Belirsiz."),
    ],
    "content/reading/tests/AC1/note-completion.json": [
        (1, ["cable"], 5, "B paragrafi: 'A piece of fruit was suspended from an overhead cable'."),
        (2, ["bamboo"], 5, "B paragrafi: 'the researchers also offered a bamboo stick long enough ... to knock the food down'."),
        (3, ["seventh"], 5, "C paragrafi: 'The turning point came in the seventh session'."),
        (4, ["tyre"], 5, "D paragrafi: 'he pushed a large tractor tyre into use as a substitute platform'."),
        (5, ["corner"], 5, "E paragrafi: 'the researchers hid the cube around a corner, in a walled passage'."),
        (6, ["fingertip"], 5, "F paragrafi: 'comparable in sensitivity to a human fingertip'."),
    ],
    "content/reading/tests/AC1/sentence-completion.json": [
        (19, ["transparent divider"], 5, "C paragrafi: 'neighbouring tanks separated by a transparent divider, allowing them to see but not touch or smell each other'."),
        (20, ["dominance hierarchy"], 5, "D paragrafi: 'Across these encounters a dominance hierarchy consistently emerged ... seventy-six per cent of interactions'."),
        (21, ["two strangers"], 5, "F paragrafi: 'Reversals of dominance ... occurred only when the pair consisted of two strangers'."),
        (22, ["dear enemy"], 5, "H paragrafi: 'a pattern long described in other species as the dear enemy effect'."),
    ],
    "content/reading/tests/AC1/summary-completion.json": [
        (36, ["caldera"], 5, "B paragrafi: 'three small islands arranged in a rough circle around a flooded caldera'."),
        (37, ["dye"], 5, "D paragrafi: 'divers collected coral cores, applied dye to mark new growth'."),
        (38, ["weedy algae"], 5, "F paragrafi: 'Immediately around the vents, weedy algae tend to dominate the seafloor'."),
        (39, ["bioerosion"], 5, "G paragrafi: 'accelerating a process called bioerosion in which the skeleton is weakened and broken down from within'."),
        (40, ["warning system"], 5, "H paragrafi: 'scientists regard the island ... as an early warning system'."),
    ],
    "content/reading/tests/AC2/flow-chart-completion.json": [
        (1, ["forty minutes"], 5, "B paragrafi: 'a series of ten long-exposure images, each lasting forty minutes'."),
        (2, ["designation"], 5, "C paragrafi: 'has been given the provisional designation S/2025 U1'."),
        (3, ["reflects"], 5, "C paragrafi: 'assuming it reflects light in a similar way to Uranus's other small moons'."),
        (4, ["Ophelia"], 5, "D paragrafi: 'in the gap between two previously known moons, Ophelia and Bianca'."),
        (5, ["fourteenth"], 5, "E paragrafi: 'the new object becomes the fourteenth member of its group of small inner moons'."),
        (6, ["International Astronomical Union"], 5, "E paragrafi: 'the newcomer's eventual name will still need formal approval from the International Astronomical Union'."),
    ],
    "content/reading/tests/AC2/sentence-completion.json": [
        (19, ["plant DNA"], 5, "C paragrafi: 'Success would place the wheat among the oldest plant DNA ever recovered and analysed'."),
        (20, ["separate laboratories"], 4, "D paragrafi: 'carried out in two physically separate laboratories, one at the University of Manchester ... and the other at Middle East Technical University'. Sadece 'laboratories' da beklenebilir."),
        (21, ["D genome"], 5, "E paragrafi: 'the so-called D genome, a segment of genetic material found only in hexaploid wheat'."),
        (22, ["Karacadağ"], 5, "G paragrafi: 'the region of Karacadağ in southern Turkey generally credited as the birthplace of einkorn cultivation'."),
    ],
    "content/reading/tests/AC2/summary-completion.json": [
        (36, ["A"], 5, "C paragrafi: 'letting the researchers treat team composition almost as if it had been assigned in a controlled experiment' = A."),
        (37, ["C"], 5, "D paragrafi: 'the number of clients handled is a dependable stand-in' = C, a reliable measure."),
        (38, ["I"], 5, "E paragrafi: 'produced no measurable improvement ... even ... in the top quarter' = I."),
        (39, ["H"], 5, "F paragrafi: 'teams with the most experienced average tenure' = H, length of service."),
        (40, ["B"], 5, "G paragrafi: 'frequent messaging may sometimes distract rather than assist workers who already know what they are doing' = B."),
    ],
    "content/reading/tests/AC3/table-completion.json": [
        (1, ["acrylic"], 5, "B paragrafi: 'a transparent acrylic panel of identical size was used instead as a control'."),
        (2, ["barrel rolls"], 5, "C paragrafi: 'blowing strings of bubbles ... performing slow barrel rolls, stretching their necks ... rotating a pectoral flipper'."),
        (3, ["cosmetic"], 5, "D paragrafi: 'A harmless cosmetic mark, five to eight centimetres across'."),
        (4, ["fourteen"], 5, "E paragrafi: 'three minutes and forty seconds doing so across fourteen separate approaches'."),
        (5, ["twenty-three seconds"], 5, "E paragrafi: 'the equivalent behaviour lasted only twenty-three seconds across four approaches'."),
        (6, ["right eye"], 5, "F paragrafi: 'Both whales ... preferred to view the mirror with their right eye, a bias that hints at ... lateralised processing'."),
    ],
    "content/reading/tests/AC3/sentence-completion.json": [
        (19, ["displacement"], 5, "B paragrafi: 'the usual method, comparing ground displacement before and after an earthquake, depends on being able to see the bedrock'."),
        (20, ["bright"], 5, "C paragrafi: 'Rough, broken debris ... appears bright ... while smooth, undisturbed ice ... appears dark'."),
        (21, ["surge"], 5, "F paragrafi: 'had already entered a fast-moving surge phase in November ... roughly 50 feet every day'."),
        (22, ["mountaineers"], 5, "G paragrafi: 'new hazards for mountaineers and scientific expeditions that use Yakutat as a staging point'."),
    ],
    "content/reading/tests/AC3/summary-completion.json": [
        (36, ["decomposition"], 5, "C paragrafi: 'heated fast enough and to a high enough temperature to prevent normal decomposition, and then cooled again almost as quickly'."),
        (37, ["reference databases"], 5, "D paragrafi: 'comparison against reference databases of proteins expressed in the human brain'."),
        (38, ["microtubules"], 5, "E paragrafi: 'Even microtubules, the tiny internal scaffolding of individual cells ... around 23 nanometres in diameter'."),
        (39, ["seven distinct"], 4, "F paragrafi: 'The team detected seven distinct proteins known to be expressed specifically in brain tissue'. Sadece 'seven' de beklenebilir."),
        (40, ["thermal conditions"], 5, "G paragrafi: 'only an extremely narrow set of thermal conditions, rapid heating followed by almost immediate cooling'."),
    ],
    "content/reading/tests/AC4/note-completion.json": [
        (1, ["reconfigure"], 5, "A paragrafi: 'they are cheaper to build and easier to reconfigure than offices divided into permanent rooms'."),
        (2, ["soundproof"], 5, "B paragrafi: 'a zoned open-plan design with soundproof doors dividing spaces into rooms holding no more than 40 people'."),
        (3, ["sound-absorbing"], 5, "B paragrafi: 'large, partly enclosed cubicles seating four to six people behind sound-absorbing panels'."),
        (4, ["headphones"], 5, "C paragrafi: 'noting details such as how often employees wore headphones'."),
        (5, ["novelty"], 5, "F paragrafi: 'a behavioural preference for the newer arrangement rather than simply a novelty effect'."),
        (6, ["workflows"], 5, "H paragrafi: 'the findings come from a single technology company with its own particular culture and workflows'."),
    ],
    "content/reading/tests/AC4/sentence-completion.json": [
        (19, ["silver birch"], 5, "C paragrafi: 'a stand of Norway spruce and silver birch trees, roughly 80 and 20 per cent of the stand respectively'."),
        (20, ["humidity"], 5, "D paragrafi: 'humidity of 94.25 per cent, and only a light wind of 1.13 metres per second'."),
        (21, ["passage"], 5, "E paragrafi: 'rather than to the simple passage of time'."),
        (22, ["vegetation"], 5, "H paragrafi: 'a thick covering of snow hides the green vegetation that other studies have linked to increased energy and alertness'."),
    ],
    "content/reading/tests/AC4/summary-completion.json": [
        (36, ["J"], 5, "B paragrafi: 'the second used a within-subject design in which the same participants experienced both a nap and a period of wakefulness' = J."),
        (37, ["B"], 5, "C paragrafi: 'The wake group learned the same material at nine in the morning ... having remained awake throughout' = B."),
        (38, ["D"], 5, "C/E paragrafi: '40 of them semantically related, such as pairs of words already connected in meaning' = D."),
        (39, ["F"], 5, "E paragrafi: 'For unrelated word pairs ... very similar benefits, with effect sizes of 0.71 and 0.68' = F."),
        (40, ["A"], 5, "F paragrafi: 'simply having the opportunity to nap mattered more than its precise internal structure' = A."),
    ],
    "content/reading/tests/GT1/note-completion.json": [
        (15, ["noticeboard"], 5, "A metni: 'Shift patterns rotate every four weeks and are published on the staff noticeboard no later than the preceding Friday'."),
        (16, ["staggered"], 5, "A metni: 'Breaks must be staggered within each team so that production lines are never left unattended'."),
        (17, ["card reader"], 5, "A metni: 'All staff must clock in and out using the card reader at the staff entrance, including for lunch breaks'."),
        (18, ["shift-swap form"], 5, "A metni: 'submit the request in writing to their supervisor at least 48 hours in advance, using the shift-swap form available from the staff office'."),
        (19, ["28 days"], 5, "B metni: 'Full-time employees are entitled to 28 days of paid annual leave per year, including public holidays'."),
        (20, ["staff portal"], 5, "B metni: 'Submit requests through the online staff portal at least two weeks in advance'."),
    ],
    "content/reading/tests/GT1/sentence-completion.json": [
        (25, ["department manager"], 5, "B metni: 'Leave requested during the final two weeks of December must be approved by the department manager directly'."),
        (26, ["double time"], 5, "B metni: 'at double time for work on public holidays' (digerlerinde 1.5 kat)."),
        (27, ["final salary"], 5, "B metni: 'Employees leaving the company are paid for any accrued but untaken leave as part of their final salary'."),
    ],
    "content/reading/tests/GT1/summary-completion.json": [
        (37, ["peelings"], 5, "E paragrafi: 'fruit and vegetable peelings, dominated by banana and mango skins, made up the largest category by far'."),
        (38, ["refrigerator"], 5, "G paragrafi: 'Dairy products were frequently forgotten at the back of the refrigerator until they had to be discarded'."),
        (39, ["convenience"], 5, "H paragrafi: 'Urban residents, by contrast, tended to favour convenience and were more prone to buying more than they needed'."),
        (40, ["prevention"], 5, "I paragrafi: 'food waste policy ... has focused on collection and disposal rather than prevention'."),
    ],
    "content/reading/tests/GT2/sentence-completion.json": [
        (25, ["probationary period"], 5, "B metni: 'Employees who have completed their probationary period may apply to work remotely'."),
        (26, ["home-office equipment"], 5, "B metni: 'Claim reimbursement for approved home-office equipment, up to 150 pounds per year'."),
        (27, ["four weeks"], 5, "B metni: 'such approval is rarely granted for periods longer than four weeks'."),
    ],
    "content/reading/tests/GT2/table-completion.json": [
        (15, ["sponsorship"], 5, "A metni: 'hold the right to work in the country for the full ten weeks without requiring sponsorship'."),
        (16, ["CV"], 5, "A metni: 'Complete the online application form and upload a current CV by 28 February'."),
        (17, ["video interview"], 5, "A metni: 'Applicants shortlisted after the written stage will be invited to a video interview during March'."),
        (18, ["ten working days"], 5, "A metni: 'must confirm their place within ten working days'."),
        (19, ["travel allowance"], 5, "A metni: 'a salary of 2,100 pounds per month, plus a travel allowance for those relocating temporarily'."),
        (20, ["mentor"], 5, "A metni: 'Each intern is paired with a mentor from their assigned department who meets with them weekly'."),
    ],
    "content/reading/tests/GT2/summary-completion.json": [
        (37, ["B"], 5, "F paragrafi: 'Income differences accounted for well under a fifth of the total association' = B, a small part."),
        (38, ["G"], 5, "G paragrafi: 'In every version of the analysis the same basic pattern held' = G, stable."),
        (39, ["I"], 5, "H paragrafi: 'suggest several candidate explanations ... while stressing that their data cannot confirm any of them directly' = I."),
        (40, ["A"], 5, "I paragrafi: 'careful to describe their results as an association rather than proof that volunteering causes better health' = A."),
    ],
}


def main():
    os.makedirs(CEVAP, exist_ok=True)
    toplam = 0
    for src, sorular in PAKETLER.items():
        ad = src.replace("/", "__")
        veri = {
            "_source": src,
            "answers": [
                {"number": n, "answer": a, "confidence": c, "reasoning": r}
                for (n, a, c, r) in sorular
            ],
        }
        with open(os.path.join(CEVAP, ad), "w", encoding="utf-8") as f:
            json.dump(veri, f, ensure_ascii=False, indent=2)
        toplam += len(sorular)
        print("yazildi:", ad, len(sorular))
    print("\nToplam %d soru, %d dosya." % (toplam, len(PAKETLER)))


if __name__ == "__main__":
    main()
