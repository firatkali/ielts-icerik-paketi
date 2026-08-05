"""OPUS5-21 / 12. paket uretici: content/listening/practice/plan-map-diagram-labelling.json

Kullanim:  python tools/_p12_uret.py

Dort kume, 15 soru. Iki kume harf secme (A-H), iki kume kelime yazma.
SVG'ler burada elle cizilir; sadece rect/circle/line/path/polygon/text
kullanilir, viewBox zorunlu, sabit width/height yok.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

HEDEF = "content/listening/practice/plan-map-diagram-labelling.json"


# --- kucuk SVG yardimcilari -------------------------------------------------

def L(x1, y1, x2, y2, w=1):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#000" '
            'stroke-width="%s"/>' % (x1, y1, x2, y2, w))


def R(x, y, w, h):
    return ('<rect x="%s" y="%s" width="%s" height="%s" fill="none" '
            'stroke="#000" stroke-width="1"/>' % (x, y, w, h))


def C(cx, cy, r):
    return ('<circle cx="%s" cy="%s" r="%s" fill="none" stroke="#000" '
            'stroke-width="1"/>' % (cx, cy, r))


def P(d):
    return '<path d="%s" fill="none" stroke="#000" stroke-width="1"/>' % d


def POLY(pts):
    return ('<polygon points="%s" fill="none" stroke="#000" '
            'stroke-width="1"/>' % pts)


def T(x, y, s, anchor="middle"):
    return '<text x="%s" y="%s" text-anchor="%s">%s</text>' % (x, y, anchor, s)


def TROT(x, y, s):
    return ('<text x="%s" y="%s" text-anchor="middle" '
            'transform="rotate(-90 %s %s)">%s</text>' % (x, y, x, y, s))


def LET(cx, cy, ch):
    """Harf secme planinda secenek konumu: daire + harf."""
    return C(cx, cy, 12) + T(cx, cy + 4, ch)


def BLANK(cx, cy, n):
    """Kelime yazma planinda bosluk: numara + altina cizgi."""
    return T(cx, cy, str(n)) + L(cx - 25, cy + 12, cx + 25, cy + 12)


def KUZEY(x, y):
    """Kuzey oku: govde y..y-45, ucu y-58, harf y+22."""
    return (L(x, y, x, y - 45) + POLY("%s,%s %s,%s %s,%s" % (
        x, y - 58, x - 7, y - 42, x + 7, y - 42)) + T(x, y + 22, "N"))


def SARMA(view, parcalar):
    return ('<svg viewBox="%s" xmlns="http://www.w3.org/2000/svg" '
            'font-family="sans-serif" font-size="12">%s</svg>'
            % (view, "".join(parcalar)))


# --- 1. kume: L3-S2, kir parki haritasi, kelime yazma (1-4) -----------------

def svg_l3():
    g = []
    # park siniri (guney cephesinde giris bosluğu)
    g += [L(40, 35, 545, 35), L(40, 35, 40, 700), L(545, 35, 545, 700),
          L(40, 700, 265, 700), L(305, 700, 545, 700)]
    # ana giris ve kuzey oku
    g += [L(285, 760, 285, 722), POLY("285,710 278,726 292,726"),
          T(285, 782, "MAIN ENTRANCE (Cranmore Road)")]
    g += [KUZEY(600, 150)]
    # yol
    g += [L(267, 700, 267, 560), L(303, 700, 303, 560), TROT(285, 645, "drive")]
    # ziyaretci merkezi (1), tuvaletler, otopark
    g += [R(110, 610, 140, 78), BLANK(180, 645, 1)]
    g += [R(110, 505, 140, 78), T(180, 550, "TOILETS")]
    g += [R(330, 610, 140, 78), T(400, 655, "CAR PARK")]
    # bilgi kulubesi (2)
    g += [R(253, 505, 66, 52), BLANK(286, 530, 2)]
    # piknik alani
    g += [R(210, 415, 120, 66), T(270, 447, "PICNIC"), T(270, 465, "AREA")]
    # gol ve ada
    g += [P("M 305,395 L 278,335 L 300,278 L 362,255 L 435,268 L 462,320 "
            "L 448,378 L 385,405 Z"), T(352, 340, "LAKE")]
    g += [C(405, 310, 14), T(405, 285, "island")]
    # kus gozlem kulubesi ve havuz tarama platformu (3)
    g += [R(480, 295, 62, 48), T(511, 317, "BIRD"), T(511, 335, "HIDE")]
    g += [R(470, 215, 72, 52), BLANK(506, 240, 3), L(470, 245, 444, 272)]
    # kirecocagi, cayir, manzara noktasi (4)
    g += [R(265, 185, 80, 52), T(305, 208, "LIME"), T(305, 226, "KILN")]
    g += [L(305, 185, 305, 160)]
    g += [R(180, 105, 250, 55), T(305, 132, "WILDFLOWER"), T(305, 150, "MEADOW")]
    g += [L(305, 105, 305, 93)]
    g += [R(245, 45, 120, 48), BLANK(305, 72, 4)]
    return SARMA("0 0 640 800", g)


# --- 2. kume: L4-S2, geri donusum merkezi, harf secme (5-8) -----------------

def svg_l4():
    g = []
    # saha siniri: dogu duvarinda cikis bosluğu, guneyde giris bosluğu
    g += [L(40, 30, 520, 30), L(40, 30, 40, 720), L(520, 30, 520, 190),
          L(520, 250, 520, 720), L(40, 720, 245, 720), L(305, 720, 520, 720)]
    # giris bariyeri ve ana giris
    g += [L(247, 706, 303, 706, 3), T(312, 710, "entrance barrier", "start")]
    g += [L(275, 778, 275, 745), POLY("275,733 268,747 282,747"),
          T(275, 795, "MAIN ENTRANCE (Ferry Lane)")]
    g += [KUZEY(570, 126)]
    # ic yol
    g += [L(245, 720, 245, 400), L(305, 720, 305, 400), T(275, 676, "drive")]
    # saha ofisi + C (tuvaletler ve su noktasi)
    g += [R(95, 575, 130, 85), T(160, 612, "SITE"), T(160, 630, "OFFICE")]
    g += [R(95, 485, 130, 72), LET(160, 521, "C")]
    # A (otopark), uzun bina: F (ust) ve B (alt uc)
    g += [R(330, 575, 150, 85), LET(405, 617, "A")]
    g += [R(330, 410, 150, 152), L(330, 500, 480, 500),
          LET(405, 455, "F"), LET(405, 531, "B")]
    # H (yolun bati tarafi, uzun binanin karsisi)
    g += [R(95, 395, 130, 75), LET(160, 432, "H")]
    # bahce atigi bolmeleri
    g += [R(185, 300, 58, 60), R(248, 300, 58, 60), R(311, 300, 58, 60),
          R(374, 300, 58, 60), T(95, 320, "GARDEN"), T(95, 338, "WASTE BAYS")]
    # yolun ikiye ayrilmasi
    g += [P("M 262,400 L 262,382 L 139,382 L 139,300"),
          P("M 288,400 L 288,382 L 495,382 L 495,215")]
    # rampa (yukari yonu okla)
    g += [L(100, 300, 100, 100), L(178, 300, 178, 100), T(139, 215, "RAMP"),
          P("M 116,270 L 139,254 L 162,270"), P("M 116,160 L 139,144 L 162,160")]
    # rampanin sagindaki konteynerler
    g += [R(190, 240, 88, 50), T(234, 270, "WOOD"),
          R(190, 175, 88, 50), T(234, 205, "RUBBLE"),
          R(190, 110, 88, 50), T(234, 132, "SCRAP"), T(234, 150, "METAL")]
    # G (sahanin arkasi, ahsap konteynerinin yani, kilitli kapi)
    g += [R(295, 230, 120, 58), LET(357, 259, "G"), L(295, 240, 295, 278, 3)]
    # D (rampanin en ucu, iki buyuk konteyner)
    g += [R(100, 40, 174, 54), L(187, 40, 187, 94), LET(143, 67, "D")]
    # E (rampanin sonu ile cikis bariyeri arasi)
    g += [R(330, 120, 140, 75), LET(400, 157, "E")]
    # rampa ucundan cikisa giden yol + cikis bariyeri
    g += [P("M 178,98 L 300,98 L 300,215 L 495,215")]
    g += [L(520, 196, 520, 244, 3), L(508, 215, 548, 215),
          POLY("560,215 546,209 546,221"), T(556, 180, "exit barrier")]
    return SARMA("0 0 620 800", g)


# --- 3. kume: L6-S2, kapali ciftci pazari, kelime yazma (9-12) --------------

def svg_l6():
    g = []
    # salon duvarlari: doguda yan kapi, guneyde ana giris
    g += [L(60, 40, 520, 40), L(60, 40, 60, 640), L(520, 40, 520, 330),
          L(520, 400, 520, 640), L(60, 640, 265, 640), L(335, 640, 520, 640)]
    g += [T(528, 370, "side door", "start")]
    g += [L(300, 715, 300, 672), POLY("300,660 293,676 307,676"),
          T(300, 733, "MAIN ENTRANCE (Peveril Street)")]
    g += [KUZEY(575, 146)]
    # saat + gosteri mutfagi + oturma alani (11)
    g += [C(300, 66, 14), L(300, 66, 300, 56), L(300, 66, 308, 70),
          T(340, 70, "clock", "start")]
    g += [R(215, 90, 170, 70), T(300, 118, "DEMONSTRATION"), T(300, 136, "KITCHEN")]
    g += [R(215, 180, 170, 70), BLANK(300, 212, 11)]
    # dolum dukkani + tuvaletler (12)
    g += [R(410, 90, 100, 90), T(460, 128, "REFILL"), T(460, 146, "SHOP")]
    g += [R(410, 200, 100, 80), BLANK(460, 235, 12)]
    g += [L(415, 190, 447, 190, 3), T(452, 194, "green sign", "start")]
    # sol siradaki tezgahlar: balik, peynir (10), ekmek ve pasta, danisma (9)
    g += [R(95, 215, 120, 90), T(155, 252, "FISH"), T(155, 270, "COUNTER")]
    g += [R(95, 370, 120, 165), L(95, 455, 215, 455), BLANK(155, 405, 10),
          T(155, 490, "BREAD AND"), T(155, 508, "CAKE STALL")]
    g += [R(95, 545, 120, 70), BLANK(155, 578, 9)]
    # cicek tezgahi
    g += [R(385, 545, 120, 70), T(445, 573, "FLOWER"), T(445, 591, "STALL")]
    # sebze siralari
    g += [R(245, 280, 60, 230), R(315, 280, 60, 230),
          TROT(275, 395, "VEGETABLE"), TROT(345, 395, "STALLS")]
    # bal ve receller
    g += [R(400, 330, 105, 70), T(452, 362, "HONEY AND"), T(452, 380, "PRESERVES")]
    # bisiklet park yeri (kapinin disinda)
    g += [R(380, 655, 95, 38), T(427, 679, "CYCLE RACKS")]
    return SARMA("0 0 620 740", g)


# --- 4. kume: L1-S2, muze, harf secme (13-15) ------------------------------

def svg_l1():
    g = []
    g += [T(235, 40, "GROUND FLOOR"), T(600, 40, "FIRST FLOOR")]
    g += [KUZEY(740, 130)]
    # --- zemin kat
    g += [L(60, 60, 410, 60), L(60, 60, 60, 330), L(410, 60, 410, 330),
          L(60, 330, 215, 330), L(255, 330, 410, 330)]
    g += [L(235, 392, 235, 352), POLY("235,340 229,354 241,354"),
          T(235, 410, "MAIN ENTRANCE (Bridge Street)")]
    g += [R(205, 296, 60, 12), T(235, 288, "TICKET DESK")]
    g += [TROT(235, 180, "corridor")]
    # bati kolonu
    g += [R(63, 250, 127, 77), LET(126, 288, "D")]
    g += [R(63, 160, 127, 85), LET(126, 202, "B")]
    g += [R(63, 63, 127, 92), T(126, 102, "WEAVING"), T(126, 120, "GALLERY")]
    # dogu kolonu
    g += [R(280, 250, 127, 77), LET(343, 288, "A")]
    g += [R(280, 200, 127, 45), T(343, 227, "CLOAKROOM")]
    g += [R(280, 150, 127, 45), L(285, 158, 402, 158), L(285, 166, 402, 166),
          L(285, 174, 402, 174), T(343, 190, "STAIRS")]
    g += [R(280, 105, 127, 42), LET(343, 126, "C")]
    g += [R(280, 63, 127, 38), LET(343, 84, "E")]
    # --- ust kat
    g += [L(490, 60, 710, 60), L(490, 60, 490, 330), L(710, 60, 710, 330),
          L(490, 330, 710, 330)]
    g += [R(493, 63, 214, 70), T(600, 92, "TEMPORARY EXHIBITION"),
          T(600, 110, "GALLERY")]
    g += [R(493, 140, 214, 60), LET(600, 170, "F")]
    g += [R(493, 205, 77, 122), LET(531, 266, "H")]
    g += [R(630, 205, 77, 122), LET(668, 266, "G")]
    g += [R(574, 240, 52, 87), L(578, 252, 622, 252), L(578, 266, 622, 266),
          L(578, 280, 622, 280)]
    g += [L(600, 238, 600, 220), POLY("600,210 594,224 606,224"),
          T(612, 218, "up", "start")]
    return SARMA("0 0 760 420", g)


HARFLER = ["A", "B", "C", "D", "E", "F", "G", "H"]

KUMELER = [
    dict(
        group_id="P-PM-01",
        script_id="L3-S2",
        context_line=("You will hear a park ranger telling a group of visitors "
                      "about three new walking routes and about the layout of "
                      "the park."),
        instructions=("Label the map below. Write NO MORE THAN THREE WORDS "
                      "AND/OR A NUMBER for each answer."),
        word_limit="NO MORE THAN THREE WORDS AND/OR A NUMBER",
        options=None,
        visual=dict(
            kind="map",
            svg=svg_l3(),
            alt=("Stonecrop kır parkının ziyaretçi haritası. Ana giriş "
                 "(Cranmore Road), yol, tuvaletler, otopark, piknik alanı, "
                 "göl, gölün içindeki küçük ada, kuş gözlem kulübesi, kireç "
                 "ocağı, kır çiçeği çayırı ve kuzey oku etiketli; 1-4 numaralı "
                 "dört yer etiketsiz bırakılmış."),
            labels=["1", "2", "3", "4"],
        ),
        items=[
            dict(number=1, prompt="Space 1 on the map",
                 answer=["visitor centre"],
                 accepted_variants=["visitor centre", "visitor center"],
                 evidence="the visitor centre is immediately on your left",
                 answer_point_id="L3-S2-14", turn_index=5, distractor_used=None,
                 explanation=("Ana girişten içeri girildiğinde ziyaretçi merkezi "
                              "hemen solda kalıyor; tuvaletler de haritada onun "
                              "arkasında etiketli duruyor."),
                 difficulty="easy"),
            dict(number=2, prompt="Space 2 on the map",
                 answer=["information hut"],
                 accepted_variants=["information hut"],
                 evidence=("Straight ahead of you, where the drive ends, is the "
                           "information hut"),
                 answer_point_id="L3-S2-17", turn_index=6, distractor_used=None,
                 explanation=("Yolun bittiği yerde, girişin tam karşısında duran "
                              "küçük yapı bilgi kulübesidir; görevlisi yoktur ama "
                              "broşürler orada durur."),
                 difficulty="easy"),
            dict(number=3, prompt="Space 3 on the map",
                 answer=["pond-dipping platform"],
                 accepted_variants=["pond-dipping platform", "pond dipping platform"],
                 evidence=("Next to the hide, and easy to walk past, is the "
                           "pond-dipping platform"),
                 answer_point_id="L3-S2-21", turn_index=7, distractor_used=None,
                 explanation=("Kuş gözlem kulübesinin hemen yanındaki, gölün sığ "
                              "ucuna uzanan alçak ahşap güverte havuz tarama "
                              "platformudur."),
                 difficulty="medium"),
            dict(number=4, prompt="Space 4 on the map",
                 answer=["viewpoint"],
                 accepted_variants=["viewpoint", "view point"],
                 evidence=("at the very top, at the far end of the meadow path, "
                           "is the viewpoint"),
                 answer_point_id="L3-S2-24", turn_index=8, distractor_used=None,
                 explanation=("Çayır patikasının en ucunda, yamacın en tepesindeki "
                              "taş halka manzara noktasıdır; kireç ocağı ile çayır "
                              "haritada zaten yazılı."),
                 difficulty="medium"),
        ],
    ),
    dict(
        group_id="P-PM-02",
        script_id="L4-S2",
        context_line=("You will hear the supervisor of a household recycling "
                      "centre talking to local residents about the rebuilt site "
                      "and how to use it."),
        instructions=("Label the plan below. Write the correct letter, A–H, next "
                      "to Questions 5–8."),
        word_limit=None,
        options=HARFLER,
        visual=dict(
            kind="plan",
            svg=svg_l4(),
            alt=("Halstock geri dönüşüm merkezinin saha planı. Ana giriş "
                 "(Ferry Lane), giriş bariyeri, iç yol, saha ofisi, bahçe atığı "
                 "bölmeleri, rampa ve rampanın yukarı yönü, ahşap, moloz ve "
                 "hurda metal konteynerleri, çıkış bariyeri ve kuzey oku "
                 "etiketli; A-H harfli sekiz konum etiketsiz bırakılmış."),
            labels=HARFLER,
        ),
        items=[
            dict(number=5, prompt="Toilets and water point",
                 answer=["C"], accepted_variants=["C"],
                 evidence=("The toilets and the drinking water point are behind "
                           "the site office"),
                 answer_point_id="L4-S2-08", turn_index=3, distractor_used=None,
                 explanation=("Ferry Lane'deki bariyerden girince solda kalan yeşil "
                              "kabin saha ofisidir; tuvaletler ve içme suyu noktası "
                              "onun arkasında, yani planda C ile gösterilen yerdedir."),
                 difficulty="easy"),
            dict(number=6, prompt="Car park",
                 answer=["A"], accepted_variants=["A"],
                 evidence=("Opposite the office, on your right, is the small car "
                           "park"),
                 answer_point_id="L4-S2-09", turn_index=4, distractor_used=None,
                 explanation=("Sekiz araçlık küçük otopark ofisin tam karşısında, "
                              "yolun sağ tarafındadır; atık bırakanlar için değil, "
                              "dükkâna gelenler içindir."),
                 difficulty="easy"),
            dict(number=7, prompt="Glass, cans and plastic banks",
                 answer=["E"], accepted_variants=["E"],
                 evidence=("between the end of the ramp and the exit barrier "
                           "you'll find the banks for glass, cans and plastic "
                           "bottles"),
                 answer_point_id="L4-S2-15", turn_index=6,
                 distractor_used="beside the site office",
                 explanation=("Kumbaralar eskiden ofisin yanındaydı, konuşmacı bunu "
                              "söyleyip düzeltiyor: artık rampanın sonu ile çıkış "
                              "bariyeri arasındalar."),
                 difficulty="hard"),
            dict(number=8, prompt="Paint and chemicals store",
                 answer=["G"], accepted_variants=["G"],
                 evidence=("The paint and chemicals store is at the back of the "
                           "site, next to the wood skip, behind a locked gate"),
                 answer_point_id="L4-S2-17", turn_index=7, distractor_used=None,
                 explanation=("Boya ve kimyasal deposu sahanın arkasında, ahşap "
                              "konteynerinin bitişiğinde ve kilitli kapının "
                              "ardındadır; planda kalın çizgi o kapıdır."),
                 difficulty="medium"),
        ],
    ),
    dict(
        group_id="P-PM-03",
        script_id="L6-S2",
        context_line=("You will hear the manager of a farmers' market talking to "
                      "local residents about the market's move into a covered "
                      "hall."),
        instructions=("Label the plan below. Write NO MORE THAN TWO WORDS AND/OR "
                      "A NUMBER for each answer."),
        word_limit="NO MORE THAN TWO WORDS AND/OR A NUMBER",
        options=None,
        visual=dict(
            kind="plan",
            svg=svg_l6(),
            alt=("Peveril Street kapalı halindeki çiftçi pazarının zemin planı. "
                 "Ana giriş (Peveril Street), çiçek tezgâhı, ekmek ve pasta "
                 "tezgâhı, balık reyonu, sebze sıraları, bal ve reçel tezgâhı, "
                 "yan kapı, saatin altındaki gösteri mutfağı, dolum dükkânı, "
                 "bisiklet park yeri ve kuzey oku etiketli; 9-12 numaralı dört "
                 "yer etiketsiz bırakılmış."),
            labels=["9", "10", "11", "12"],
        ),
        items=[
            dict(number=9, prompt="Space 9 on the plan",
                 answer=["information desk"],
                 accepted_variants=["information desk"],
                 evidence="Immediately on your left is the information desk",
                 answer_point_id="L6-S2-11", turn_index=4, distractor_used=None,
                 explanation=("Peveril Street'e bakan geniş kapıdan girilince hemen "
                              "solda danışma masası var; müdür de gün boyu orada "
                              "duruyor."),
                 difficulty="easy"),
            dict(number=10, prompt="Space 10 on the plan",
                 answer=["cheese counter"],
                 accepted_variants=["cheese counter"],
                 evidence=("beyond that, sharing the same long counter, the cheese "
                           "counter"),
                 answer_point_id="L6-S2-15", turn_index=5, distractor_used=None,
                 explanation=("Ekmek ve pasta tezgâhının devamı, aynı uzun tezgâhı "
                              "paylaşan bölüm peynir reyonudur."),
                 difficulty="medium"),
            dict(number=11, prompt="Space 11 on the plan",
                 answer=["seating area"],
                 accepted_variants=["seating area"],
                 evidence="the seating area is in front of it",
                 answer_point_id="L6-S2-20", turn_index=7, distractor_used=None,
                 explanation=("Yirmi dört sandalyeli oturma alanı, salonun en "
                              "ucundaki gösteri mutfağının tam önünde yer alıyor."),
                 difficulty="medium"),
            dict(number=12, prompt="Space 12 on the plan",
                 answer=["toilets"],
                 accepted_variants=["toilets"],
                 evidence=("the toilets are past the refill shop, through the door "
                           "with the green sign above it"),
                 answer_point_id="L6-S2-22", turn_index=8, distractor_used=None,
                 explanation=("Tuvaletlere dolum dükkânını geçip yeşil tabelalı "
                              "kapıdan geçiliyor; planda o kapı kalın çizgiyle "
                              "gösterilmiştir."),
                 difficulty="medium"),
        ],
    ),
    dict(
        group_id="P-PM-04",
        script_id="L1-S2",
        context_line=("You will hear a member of staff welcoming visitors to a "
                      "museum that has recently opened."),
        instructions=("Label the plans below. Write the correct letter, A–H, next "
                      "to Questions 13–15."),
        word_limit=None,
        options=HARFLER,
        visual=dict(
            kind="plan",
            svg=svg_l1(),
            alt=("Weavers' Yard müzesinin zemin kat ve üst kat planı. Ana giriş "
                 "(Bridge Street), bilet bankosu, koridor, dokuma galerisi, "
                 "vestiyer, merdiven, üst kattaki geçici sergi galerisi, "
                 "merdivenin çıkış yönü ve kuzey oku etiketli; A-H harfli sekiz "
                 "konum etiketsiz bırakılmış."),
            labels=HARFLER,
        ),
        items=[
            dict(number=13, prompt="Shop",
                 answer=["A"], accepted_variants=["A"],
                 evidence="Opposite the café, on your right, is the shop",
                 answer_point_id="L1-S2-16", turn_index=6, distractor_used=None,
                 explanation=("Mağaza kafenin tam karşısında, girişin sağ tarafında "
                              "kalıyor; vestiyer planda adıyla yazılı olduğu için "
                              "karışma ihtimali yok."),
                 difficulty="easy"),
            dict(number=14, prompt="Lift",
                 answer=["C"], accepted_variants=["C"],
                 evidence=("between the lecture theatre and the shop there's a "
                           "lift"),
                 answer_point_id="L1-S2-21", turn_index=8, distractor_used=None,
                 explanation=("Asansör konferans salonu ile mağaza arasındadır; "
                              "aradaki vestiyer ve merdiven planda yazılı olduğu "
                              "için geriye tek bir konum kalıyor."),
                 difficulty="hard"),
            dict(number=15, prompt="Reading room",
                 answer=["G"], accepted_variants=["G"],
                 evidence="the reading room, at the top of the stairs on your right",
                 answer_point_id="L1-S2-23", turn_index=9, distractor_used=None,
                 explanation=("Okuma odası üst katta, merdivenin başında sağa "
                              "düşen odadır; merdivenin çıkış yönü planda okla "
                              "gösterilmiştir."),
                 difficulty="medium"),
        ],
    ),
]


def main():
    veri = dict(
        schema_version="1.0",
        set_id="practice-plan-map-diagram-labelling",
        skill="listening",
        test_id=None,
        section=None,
        practice=True,
        question_type="plan_map_diagram_labelling",
        generated_by="opus",
        instructions=("Label the plans and maps below. Follow the instruction "
                      "given above each plan: for some sets you write a letter, "
                      "for others you write the missing word or words."),
        word_limit="NO MORE THAN THREE WORDS AND/OR A NUMBER",
        options=None,
        visual=None,
        stem_block=None,
        table=None,
        groups=[],
    )
    for k in KUMELER:
        kume = dict(
            group_id=k["group_id"],
            script_id=k["script_id"],
            question_type="plan_map_diagram_labelling",
            context_line=k["context_line"],
            instructions=k["instructions"],
            word_limit=k["word_limit"],
            options=k["options"],
            visual=k["visual"],
            stem_block=None,
            table=None,
            items=[],
        )
        for it in k["items"]:
            yeni = dict(it)
            yeni["script_id"] = k["script_id"]
            kume["items"].append(dict(
                number=yeni["number"],
                script_id=yeni["script_id"],
                prompt=yeni["prompt"],
                answer=yeni["answer"],
                accepted_variants=yeni["accepted_variants"],
                evidence=yeni["evidence"],
                answer_point_id=yeni["answer_point_id"],
                turn_index=yeni["turn_index"],
                distractor_used=yeni["distractor_used"],
                explanation=yeni["explanation"],
                difficulty=yeni["difficulty"],
            ))
        veri["groups"].append(kume)

    ortak.yaz(HEDEF, veri)
    print("yazildi: %s (%d kume, %d soru)" % (
        HEDEF, len(veri["groups"]), sum(len(g["items"]) for g in veri["groups"])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
