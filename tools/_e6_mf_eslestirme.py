# -*- coding: utf-8 -*-
"""OPUS5-E6 5. calistirma: cumle sonu esleystirme + ozellik esleystirme.

E5'in eledigi yedi ozellik-esleystirme yuvasini ayni dosyaya ayni numarayla
yeniden doldurur (elenen listesinde cumle sonu esleystirme yuvasi yok):

  content/reading/practice/matching-features.json  #1, #5        (A10)
  content/reading/tests/AC1/matching-features.json #25           (A02)
  content/reading/tests/AC2/matching-features.json #24, #25, #26 (A05)
  content/reading/tests/AC4/matching-features.json #24           (A11)

Iki dosyada secenek listesi de degisiyor; gerekcesi NOTLAR.md'de:
  - AC1: E5'in kendi onerisi (gruplari bolme turuyle degil asama/sira ile
    adlandir), cunku sizinti secenek metinlerindeydi.
  - AC2: yer adlarindan olusan liste her ifadeyi tur elemesiyle cozulur
    kiliyordu; liste bugday turlerine cevrildi, bu yuzden kapsam disindaki
    23 numarali yuva da zorunlu olarak yeniden yazildi.

Soru sayisi degismez, hicbir soru silinmez.
Kullanim: python tools/_e6_mf_eslestirme.py
"""
import io
import json
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LISTE = os.path.join(KOK, "content", "DOGRULAMA", "yeniden-uretim-listesi.json")
TARIH = "2026-08-08"
KAYNAK = "prompts/OPUS5-E6-yeniden-uretim.md (5/7)"
GRUP = "Cumle sonu esleystirme + ozellik esleystirme"

SIRA = ["number", "prompt", "answer", "evidence", "evidence_locator",
        "heading_check", "feature_check", "grammar_check", "explanation",
        "difficulty", "status", "blind_solvable", "blind_basis",
        "generated_by", "yeniden_uretim"]

def kanit(pasaj, paragraf, sira, parca):
    """Kanit cumlesini pasajdan birebir alir; paragraf/sira/parca hepsi dogrulanir."""
    p = os.path.join(KOK, "passages", "academic", pasaj + ".json")
    d = json.load(open(p, encoding="utf-8"))
    metin = next(x["text"] for x in d["paragraphs"] if x["label"] == paragraf)
    cumleler = re.split(r"(?<=[.!?])\s+", metin.strip())
    c = cumleler[sira - 1]
    if parca not in c:
        raise SystemExit("kanit bulunamadi: %s %s/%d -- %r" % (pasaj, paragraf, sira, parca))
    return c


A10_B2 = kanit("A10", "B", 2, "sound-absorbing panels")
A10_D3 = kanit("A10", "D", 3, "despite its popularity")
A02_D3 = kanit("A02", "D", 3, "seventy-six per cent")
A05_B2 = kanit("A05", "B", 2, "under the microscope")
A05_E1 = kanit("A05", "E", 1, "originally been classified")
A05_F2 = kanit("A05", "F", 2, "spelt-like wheat")
A05_G3 = kanit("A05", "G", 3, "may have emerged sooner")
A11_E4 = kanit("A11", "E", 4, "four-item Subjective Vitality")

# --------------------------------------------------------------------------
# Yeni yuvalar: dosya -> numara -> alanlar
# --------------------------------------------------------------------------
YENI = {
    "content/reading/practice/matching-features.json": {
        1: {
            "prompt": ("Of the four, this was the only design whose satisfaction and "
                       "productivity scores came out below those of the layout used for "
                       "comparison."),
            "answer": ["C"],
            "evidence": A10_D3,
            "evidence_locator": {"paragraph": "D", "sentence": 3},
            "feature_check": (
                "Karistirilabilecek oge A: 'en kotu duzen sade acik ofistir' kanisi "
                "disaridan hazir geldigi icin aday once oraya bakiyor -- oysa A olcumun "
                "kendisine gore yapildigi duzen, yani kendi altina dusmesi tanimsiz. B ve "
                "D de elenir: D/2 ikisini de karsilastirma duzeninin ustune koyuyor "
                "(memnuniyette yuzde 12 ve yuzde 8 daha yuksek). Iki olcumde birden "
                "altina dusen tek duzen D/3'te veriliyor ve o duzen, pasajin 'gunumuz "
                "ofis modasinda populer olmasina ragmen' diye andigi etkinlik temelli "
                "tasarim. Disaridan getirilen sezgi burada bilerek yanlis yone gidiyor."),
            "explanation": ("Paragraph D says the activity-based design performed worse "
                            "than the open-plan baseline on both measures, with "
                            "satisfaction and productivity scores roughly 14 per cent "
                            "lower."),
            "difficulty": "medium",
            "ne_degisti": (
                "Yuva bosaltilip ayni pasajdan yeni bir soruyla dolduruldu. Eski soru "
                "F/2'ye, gurultunun guvenli sinirini en cok asan duzene dayaniyordu; "
                "'acik ofis en gurultuludur' yaygin kanisi cevabi pasajsiz veriyordu. "
                "Yeni kanit baska bir paragrafa (D/3) ve baska bir olcuye tasindi: iki "
                "anket olcumunde de karsilastirma duzeninin ALTINA dusen tek tasarim. "
                "Bu, disaridan beklenenin tersi bir bulgu oldugu icin genel kultur artik "
                "yanlis secenege (A) capalaniyor. Kip: ifade mutlak ('the only design')."),
        },
        5: {
            "prompt": ("Its part-enclosed spaces were screened by panels that absorbed "
                       "sound rather than by doors."),
            "answer": ["D"],
            "evidence": A10_B2,
            "evidence_locator": {"paragraph": "B", "sentence": 2},
            "feature_check": (
                "Karistirilabilecek oge B: secenek adlarindan gidildiginde sezgi iki yone "
                "birden calisiyor -- 'zoned' sozcugu bolmeyi ve kapiyi, 'team office' "
                "sozcugu ise kabini ve paneli cagristiriyor, yani ad duzeyinde ayirt "
                "edici bir ipucu yok. Ayrim yalniz B/2'de: ses yalitimli KAPILAR "
                "bolgelere ayrilmis acik ofiste, sesi EMEN PANELLER takim ofisinde. A "
                "elenir, cunku karsilastirma duzeninde masalar arasinda neredeyse hic "
                "ayirici yok; C de elenir, orada sabit masa yerine serbest masa, ayri "
                "odaklanma odalari ve ortak calisma alanlari var, panelli kabin degil."),
            "explanation": ("Paragraph B describes the team-office design as large, "
                            "partly enclosed cubicles seating four to six people behind "
                            "sound-absorbing panels, whereas the zoned open-plan design "
                            "is divided by soundproof doors."),
            "difficulty": "hard",
            "ne_degisti": (
                "Yuva bosaltilip ayni pasajdan yeni bir soruyla dolduruldu. Eski soru "
                "H/1'e, 'calisanlarin en az geri donmek istedigi duzen' bulgusuna "
                "dayaniyordu; bu da acik ofis hakkindaki yaygin kaniyla birebir ortustugu "
                "icin pasajsiz cevaplanabiliyordu. Yeni kanit sonuc paragrafindan cikip "
                "yontem paragrafina (B/2) tasindi ve eksen bulgu degil, duzenin fiziksel "
                "tarifi oldu: kapi mi, ses emici panel mi. Iki secenek arasindaki bu "
                "ayrim disaridan bilinemez, cunku hangi tasarimin hangi engeli kullandigi "
                "keyfi bir tercih. Kip: ifade olculu-notr, mutlaklik tasimiyor."),
        },
    },
    "content/reading/tests/AC1/matching-features.json": {
        25: {
            "prompt": ("In this group the stronger animal of the pair took about three "
                       "interactions in every four."),
            "answer": ["C"],
            "evidence": A02_D3,
            "evidence_locator": {"paragraph": "D", "sentence": 3},
            "feature_check": (
                "Karistirilabilecek ogeler D ve E: yedinci gunun iki bulusma turunde de "
                "kimin ustun geldigi kaydediliyor, ustelik F/4 yabanci ciftlerde on iki "
                "eslesmenin sekizinde ustunlugun el degistirdigini soyluyor -- yani "
                "'ustun taraf' olcusu o iki gruba da yakisiyor. Ama yuzde yetmis alti "
                "orani yalniz D/3'te, uc gunluk birlikte yasama doneminde veriliyor; "
                "yedinci gun icin boyle bir oran hic verilmiyor. A ve B elenir: o iki "
                "grup ilk asamada bolmenin ardinda ayri tutuluyor, aralarinda sayilacak "
                "bir alisveris olmuyor."),
            "explanation": ("Paragraph D says that across the three days of cohabitation "
                            "a dominance hierarchy emerged, with the stronger animal "
                            "winning an average of seventy-six per cent of interactions."),
            "difficulty": "medium",
            "ne_degisti": (
                "Sizinti sorunun kipinde degil, secenek listesindeydi: A ve B gruplari "
                "'see-through screen' ve 'solid screen' diye, yani tam da kanit "
                "cumlesinin (C/3) soyledigi ozellikle adlandirilmisti; ilk asamayla "
                "ilgili her ifade bu iki etiketten birine sozcuk duzeyinde bagliydi. E5'in "
                "onerisi uygulandi: A ve B artik bolme turuyle degil SIRAYLA "
                "adlandiriliyor ('ilk / ikinci kosul'), C ise 'gunluk bulusmalar' yerine "
                "'sonraki uc gun' oldu. Yuvanin kendisi de C/3'ten tumden cikarilip "
                "D/3'teki keyfi bir oran uzerine kuruldu: ustun hayvanin etkilesimlerin "
                "yaklasik dortte ucunu kazanmasi. Kip: ifade olculu ('about'). Not: ayni "
                "cumleyi AC1 cumle tamamlama 20 de kullaniyor, ama orada hedef terimin "
                "kendisi ('dominance hierarchy'), burada oran; ortak cumle NOTLAR.md'de "
                "kaydedildi."),
        },
    },
    "content/reading/tests/AC2/matching-features.json": {
        23: {
            "prompt": ("Grain shape alone had placed both of the main samples among "
                       "wheats of this kind before any DNA was read."),
            "answer": ["D"],
            "evidence": A05_E1,
            "evidence_locator": {"paragraph": "E", "sentence": 1},
            "feature_check": (
                "Karistirilabilecek ogeler B ve C: ayni cumle iki ornegi einkorn ve emmer "
                "diye tek tek adlandirdigi icin iki secenek de dogruymus gibi duruyor. "
                "Ama ifade IKI ornegi birden ayni kumeye koyuyor ve pasaj o ortak kumeyi "
                "'both simpler wheats' diye adlandiriyor -- tek bir tur degil, basit "
                "bugdaylar butunu. A ve E elenir: ikisi de tane bicimine degil, DNA "
                "okunduktan sonra cikan sonuclara bagli (A icin B/2 ve G/3, E icin F/1-2)."),
            "explanation": ("Paragraph E says the two main samples had originally been "
                            "classified, from their shape alone, as einkorn and emmer, "
                            "both simpler wheats."),
            "difficulty": "medium",
            "ne_degisti": (
                "Bu yuva E5 listesinde YOK; secenek listesi bugday turlerine cevrildigi "
                "icin zorunlu olarak yeniden yazildi. Eski soru bir YER sorusuydu (B/1: "
                "tanelerin baska kazilardakinden iyi korunmus olmasi) ve yeni listede "
                "karsiligi kalmiyordu. Eski cevabin ekseni de listenin kendisiyle "
                "cozuluyordu: bes secenekten yalniz biri kazi yeri oldugu icin 'buradan "
                "tane cikti' diyen her ifade tur elemesiyle bulunuyordu. Yeni soru ayni "
                "pasajdan, E/1'den yazildi ve dogru cevap ancak 'iki ornek birden' "
                "kaydinin okunmasiyla bulunuyor."),
        },
        24: {
            "prompt": ("The team's evidence is put forward, cautiously, as the first "
                       "genetic sign that a wheat of this kind was present in the "
                       "Neolithic Near East."),
            "answer": ["E"],
            "evidence": A05_F2,
            "evidence_locator": {"paragraph": "F", "sentence": 2},
            "feature_check": (
                "Karistirilabilecek oge A: ayni cumle once hexaploid bugdayin ekiminde "
                "erken bir gecis asamasindan soz ediyor, bu yuzden 'ilk genetik isaret' "
                "kaydi ona da yakisiyor. Ama cumle 'ilk kez' iddiasini acikca spelt "
                "benzeri bugdayin varligina bagliyor ve 'at all' diyerek bunu ayirt "
                "ediyor; hexaploid icin soylenen sey ilk kanit degil, gecis asamasi "
                "yorumu. B, C ve D elenir: basit bugdaylarin Neolitik Yakin Dogu'da "
                "bulunmasi zaten beklenen durum, pasaj onlar icin boyle bir ilk "
                "iddiasinda bulunmuyor."),
            "explanation": ("Paragraph F says this is the first genetic evidence hinting "
                            "at the presence of a spelt-like wheat in the Neolithic Near "
                            "East at all, a possibility the researchers treat cautiously."),
            "difficulty": "hard",
            "ne_degisti": (
                "Eski soru G/2'ye dayaniyordu: basit bugday ehlilestirmesinin yaklasik on "
                "iki bin yil once Bereketli Hilal'de baslamasi. Bu ders kitabi duzeyinde "
                "bir tarih onermesi oldugu icin cevap pasajsiz da bulunuyordu. Yeni kanit "
                "hem baska bir paragrafa (F/2) hem de bambaska bir eksene tasindi: "
                "arastirmacilarin hangi bulguyu 'ilk' ve 'ihtiyatla' diye nitelendirdigi. "
                "Secenek listesi de yer adlarindan bugday turlerine cevrildigi icin, "
                "eski sorunun dayandigi 'genis bolge / dar bolge' ayrimi artik yok. Kip: "
                "ifade olculu ('cautiously')."),
        },
        25: {
            "prompt": ("Under magnification, some of the charred grains had looked as "
                       "though they were this type."),
            "answer": ["A"],
            "evidence": A05_B2,
            "evidence_locator": {"paragraph": "B", "sentence": 2},
            "feature_check": (
                "Karistirilabilecek ogeler B, C ve D: bicime bakan siniflandirma iki ana "
                "ornegi basit bugdaylara koydugu icin (E/1) aday mikroskop altindaki "
                "gorunumu de o tarafa baglayabilir -- ustelik 23. soru tam olarak bunu "
                "soyluyor. Ayrim B/2'de: bazi taneler mikroskop altinda alti kromozom "
                "takimi tasiyan daha karmasik forma ait gibi durmus, basit bugdaylar ise "
                "iki ya da dort takim tasiyor. E elenir, cunku spelt adi ancak modern "
                "turlerle karsilastirmadan sonra, F paragrafinda geciyor; mikroskop "
                "asamasinda boyle bir ad hic anilmiyor."),
            "explanation": ("Paragraph B says that under the microscope some of the "
                            "charred seeds looked as though they belonged to hexaploid "
                            "wheat, a form carrying six sets of chromosomes."),
            "difficulty": "hard",
            "ne_degisti": (
                "Eski soru da G/2'ye dayaniyordu: Karacadag'in einkorn ekiminin dogdugu "
                "yer olarak anilmasi. Bu, alan disindan da bilinen spesifik bir arkeoloji "
                "bilgisi. Yeni kanit B/2'ye tasindi ve eksen bir yer iddiasindan tane "
                "gorunumune gecti: tanelerin mikroskop altinda hangi forma benzedigi "
                "disaridan bilinemez. Kip: ifade olculu ('some', 'as though')."),
        },
        26: {
            "prompt": ("The sequences recovered from the settlement suggest this form may "
                       "have arisen earlier, and further from the usual heartland, than "
                       "researchers had thought."),
            "answer": ["A"],
            "evidence": A05_G3,
            "evidence_locator": {"paragraph": "G", "sentence": 3},
            "feature_check": (
                "Karistirilabilecek oge E: F/1 eski dizilerin modern hexaploid turlere, "
                "bu arada spelt gibi kavuzlu turlere benzedigini soyledigi icin 'daha "
                "erken ortaya cikmis olabilir' kaydi spelt'e de yakisiyor. Ama G/3 "
                "yorumunu acikca alti kromozom takimli forma bagliyor; spelt icin "
                "soylenen sey erken cikis degil, benzerlik. B, C ve D elenir: basit "
                "bugdaylarin erken oldugu zaten standart anlatinin kendisi, pasajin "
                "sasirtici buldugu sey bu degil."),
            "explanation": ("Paragraph G says that finding genetic traces of hexaploid "
                            "wheat at the site this early suggests the six-chromosome "
                            "form may have emerged sooner, and further from the "
                            "traditional core, than researchers had assumed."),
            "difficulty": "medium",
            "ne_degisti": (
                "Eski soru A/3'e dayaniyordu: yerlesimin uzerinde bulundugu yollarin "
                "tarim uygulamalarini Avrupa'ya tasimasi. Tarimin Bereketli Hilal'den "
                "Avrupa'ya yayildigi anlatisi ders kitabi duzeyinde bilindigi icin "
                "'yayilmanin yonu' sorusu pasajsiz cevaplanabiliyordu. Yeni kanit G/3'un "
                "yon bildiren kismina degil, tarih ve uzaklik iddiasina baglandi ve "
                "cevap bir yer degil bir bugday turu oldu; boylece yayilma anlatisi "
                "sorunun disinda kaldi. Kip: ifade olculu ('may')."),
        },
    },
    "content/reading/tests/AC4/matching-features.json": {
        24: {
            "prompt": ("Of the four, this one puts the fewest questions to participants, "
                       "two fewer than the next shortest."),
            "answer": ["D"],
            "evidence": A11_E4,
            "evidence_locator": {"paragraph": "E", "sentence": 4},
            "feature_check": (
                "Karistirilabilecek oge C: ayni cumlede gecen dinlendiricilik olcegi de "
                "kisa, alti maddelik; olceklerin adlari uzunluk hakkinda hicbir sey "
                "soylemedigi icin 'en kisa hangisi' sezgisi bu ikisi arasinda bolunuyor. "
                "Ayrim iki sayida: alti maddeye karsi dort madde, yani fark tam iki "
                "madde. A ve B elenir; E/2 ve E/3 onlari altmis bes ve yirmi madde olarak "
                "veriyor, ikisi de dortten uzun."),
            "explanation": ("Paragraph E gives the Subjective Vitality Scale four items "
                            "and the Restorative Outcome Scale six, so it is the shortest "
                            "of the four instruments, by two items."),
            "difficulty": "medium",
            "ne_degisti": (
                "Eski soru F/1'e dayaniyordu: alti olumsuz duygu durumundan besinin orman "
                "sonrasi anlamli bicimde dusmesi. Profile of Mood States'in alti duygu "
                "boyutu olctugu psikolojide yaygin bilinen bir bilgi oldugu icin 'olculen "
                "hos olmayan durumlarin cogu' kaydi pasajsiz da o araca oturuyordu. Yeni "
                "kanit E/4'e tasindi ve eksen olcegin NE OLCTUGUNDEN kac maddeden "
                "olustuguna gecti; madde sayilari (alti ve dort) disaridan bilinemez, "
                "araclarin adlari da uzunluk hakkinda hicbir sey soylemez. Kip: ifade "
                "mutlak ('the fewest ... of the four')."),
        },
    },
}

# --------------------------------------------------------------------------
# Secenek listesi degisiklikleri
# --------------------------------------------------------------------------
AC1_SECENEK = [
    ("A", "the pairs in the first of the two conditions used before they met"),
    ("B", "the pairs in the second of the two conditions used before they met"),
    ("C", "the pairs during the three days they spent together afterwards"),
    ("D", "the animals given back their earlier partner on the seventh day"),
    ("E", "the animals given an unknown partner on the seventh day"),
]
AC2_SECENEK = [
    ("A", "hexaploid wheat"),
    ("B", "einkorn"),
    ("C", "emmer"),
    ("D", "the simpler wheats"),
    ("E", "spelt"),
]
AC2_YONERGE = ("Look at the following statements and the list of wheat types below.\n\n"
               "Match each statement with the correct type, A-E.\n"
               "Write the correct letter, A-E, in boxes 23-26 on your answer sheet.\n\n"
               "NB You may use any letter more than once.")
AC1_26_NOT = (
    "OPUS5-E6 5/7: secenek listesi degistigi icin bu yuvanin kip/secenek sizintisi "
    "kapandi. Eski listede yalniz A 'see-through screen' diye adlandirildigi icin "
    "'tek basina gormek' diyen her ifade sozcuk duzeyinde A'ya bagliydi; yeni listede "
    "A ve B yalniz SIRAYLA aniliyor, dolayisiyla cozucu once C/2'yi okuyup ilk kosulun "
    "gorme izni veren kosul oldugunu bulmak, sonra H/3'e gitmek zorunda. Ifade, cevap "
    "ve kanit degismedi.")
AC1_26_FEATURE = (
    "Karistirilabilecek ogeler B ve C. B: ilk asamanin ikinci kosulunda hicbir duyuya "
    "izin verilmiyor, sezgisel olarak 'en zayif fark' orada beklenir -- oysa pasaj zayif "
    "ama olculebilir farki, yalnizca gormeye izin verilen ilk kosula bagliyor. C: uc "
    "gunluk birliktelikte de degisimler kaydediliyor, ama H/3'un sozunu ettigi asama "
    "alistirma asamasi, yani bulusma oncesi donem. Cevap ancak once C/2 (ilk kosulda "
    "gorme var, dokunma ve koku yok), sonra H/3 okunarak A'ya gidiyor.")


def yol(rel):
    return os.path.join(KOK, rel.replace("/", os.sep))


def yaz(p, d):
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")


def secenek(ciftler):
    return [{"key": k, "text": t} for k, t in ciftler]


def elenen_gerekce():
    """(dosya, numara) -> E5'in neden_elendi metni."""
    d = json.load(open(LISTE, encoding="utf-8"))
    return {(x["dosya"], x["numara"]): x["neden_elendi"] for x in d["elenen"]}


def yeni_yuva(eski, alan, gerekce):
    """Eski yuvayi bosaltip yenisini kurar; eski icerik yeniden_uretim'e gecer."""
    it = {
        "number": eski["number"],
        "prompt": alan["prompt"],
        "answer": alan["answer"],
        "evidence": alan["evidence"],
        "evidence_locator": alan["evidence_locator"],
        "heading_check": None,
        "feature_check": alan["feature_check"],
        "grammar_check": None,
        "explanation": alan["explanation"],
        "difficulty": alan["difficulty"],
        "status": "verified",
        "blind_solvable": None,
        "blind_basis": None,
        "generated_by": "opus",
        "yeniden_uretim": {
            "tarih": TARIH,
            "kaynak_prompt": KAYNAK,
            "uretilen_grup": GRUP,
            "eski_prompt": eski["prompt"],
            "eski_cevap": eski["answer"],
            "eski_kanit_cumlesi": eski["evidence"],
            "neden_elendi": gerekce,
            "ne_degisti": alan["ne_degisti"],
        },
    }
    # Onceki calistirmalarin duzeltme kaydi varsa silinmez, altina tasinir.
    if eski.get("revision"):
        it["yeniden_uretim"]["onceki_revizyon"] = eski["revision"]
    if eski.get("review_note"):
        it["yeniden_uretim"]["onceki_review_note"] = eski["review_note"]
    return {k: it[k] for k in SIRA if k in it}


def dosya_isle(rel, yuvalar, gerekceler):
    p = yol(rel)
    d = json.load(open(p, encoding="utf-8"))
    gruplar = d["groups"] if "groups" in d else [d]
    n = 0
    for g in gruplar:
        for i, it in enumerate(g["items"]):
            if it["number"] in yuvalar:
                alan = yuvalar[it["number"]]
                g["items"][i] = yeni_yuva(it, alan, gerekceler.get((rel, it["number"])))
                n += 1

    if rel.endswith("AC1/matching-features.json"):
        d["option_list"]["options"] = secenek(AC1_SECENEK)
        for it in d["items"]:
            if it["number"] == 26:
                it["feature_check"] = AC1_26_FEATURE
                it["review_note"] = AC1_26_NOT
    if rel.endswith("AC2/matching-features.json"):
        d["option_list"]["label"] = "List of Wheat Types"
        d["option_list"]["options"] = secenek(AC2_SECENEK)
        d["instructions"] = AC2_YONERGE
        d["allow_repeat"] = True

    yaz(p, d)
    print("%-52s yeniden dolduruldu: %d" % (rel, n))
    return n


def main():
    gerekceler = elenen_gerekce()
    toplam = 0
    for rel, yuvalar in YENI.items():
        toplam += dosya_isle(rel, yuvalar, gerekceler)
    print("toplam yuva:", toplam)


if __name__ == "__main__":
    main()
