# -*- coding: utf-8 -*-
"""Ornek cevap kutuphanesinin yazma yarisi icin ucuncu duzey denetim: band AYRIMI.

Onceki iki denetim baska seylere bakiyordu:
  1. duzey (sema)   - gecerli JSON, band uclusu, zorunlu alanlar, kelime sayisi
  2. duzey (gorev)  - `tools/_c1_denetim.py`; cevap gorevle tutarli mi, sayilar dogru mu

Ikisi de bir cevabin **hedefledigi bandda olup olmadigina** bakmiyor. Prompt'un kirmizi
basligi tam olarak bunu soyluyor:

    "En sik yapilan hata: uc cevabin da duzgun Ingilizce olmasi, sadece uzunlugun
     degismesi. Band 5 cevabi gercekten band 5 olmali - hata icermeli."

Bu script o hatanin olusup olusmadigini disaridan olcuyor. Band etiketine bakmadan yedi
metrik hesaplaniyor, sonra etiketle karsilastiriliyor:

  A  kelime sayisi tirmaniyor mu, band 5 gercekten "sinirin ucunda" mi
  B  sozcuk cesitliligi (TTR) tirmaniyor mu - UZUNLUKTAN ARINDIRILMIS olcum
  C  cumle yapisi cesitleniyor mu (cumle uzunlugu sapmasi + yan cumle yogunlugu)
  D  mekanik baglac (Firstly/Secondly/Thirdly) band 5'te var, band 8'de yok mu
  E  band 5 gercekten dilbilgisi hatasi iceriyor mu, band 8 temiz mi
  F  ayni dosyanin uc bandi arasinda kopyala-yapistir var mi (dosya ICI ortusme;
     2. duzey denetim dosyalar ARASI ortusmeye bakmisti)
  G  bilesik olcut: 5 ile 8 arasindaki fark UZUNLUK DISINDA kac boyutta gorunuyor
     (prompt'un uyardigi "sadece uzunluk degisiyor" durumu tam olarak burada yakalanir)

Metriklerin siniri: bunlar bandin kendisini olcmez, bandin **izlerini** olcer. Puanlama
hala `degerlendirme/` altindaki talimatla insan tarafindan yapilir (KONTROL.md'deki
tablolar). Bu script o puanlamanin gozunden kacan sistematik bir egilim - ozellikle
"band 5'i farkinda olmadan duzgun yazmak" - kalmis mi diye bakar.

Hicbir dosyayi degistirmez. Bulgu varsa cikis 1.
"""

import json
import os
import re
import sys
from collections import Counter

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CEVAP = os.path.join(KOK, "content", "ornek-cevaplar", "writing")
HAVUZ = os.path.join(KOK, "content", "writing")

BANTLAR = (5.0, 6.5, 8.0)

bulgular = []
gozlemler = []   # bulgu sayilmayan ama ozete yazilan olcumler


def bulgu(dosya, tur, mesaj):
    bulgular.append((dosya, tur, mesaj))


def oku(yol):
    with open(yol, encoding="utf-8") as f:
        return json.load(f)


def gorev_havuzu():
    """set_id -> (yol, veri). F denetimi gorevin kendi ifadesini dislayabilsin diye."""
    h = {}
    for kok, _, dosyalar in os.walk(HAVUZ):
        for d in dosyalar:
            if not d.endswith(".json"):
                continue
            yol = os.path.join(kok, d)
            try:
                v = oku(yol)
            except Exception:
                continue
            sid = v.get("set_id")
            if sid:
                h[sid] = (yol, v)
    return h


# --- metin araclari -------------------------------------------------------

def sozcukler(metin):
    """Sozcuk cesitliligi / n-gram icin: yalnizca harf dizileri."""
    return re.findall(r"[A-Za-z']+", metin.lower())


def kelime_say(metin):
    """IELTS sayimi: sayilar da bir sozcuk sayilir ("30%", "1995", "8.4").

    Ilk yazimda bu fonksiyon yoktu ve sayim `sozcukler()` uzerinden yapiliyordu;
    Academic Task 1 cevaplarinda 15-20 sayi eksik sayilarak dort dosya haksiz yere
    "150 kelimenin altinda" gorundu. Alt sinir denetimi bu sayimla yapilmali.
    """
    return len(re.findall(r"[A-Za-z']+|\d+(?:[.,]\d+)?", metin))


def cumleler(metin):
    """Kaba cumle bolme; kisaltmalardaki noktayi yutmamak icin once maskele."""
    m = re.sub(r"\b(Mr|Mrs|Ms|Dr|St|etc|e\.g|i\.e)\.", r"\1<NOKTA>", metin)
    parcalar = re.split(r"[.!?]+[\s\n]+|[.!?]+$", m)
    return [p.replace("<NOKTA>", ".").strip() for p in parcalar if p.strip()]


def ttr(kelimeler, pencere=140):
    """Tur/belirtec orani - ilk `pencere` sozcuk uzerinden.

    Uzunluktan aritmak sart: TTR uzun metinde kendiliginden duser, yani ham TTR
    band 8'i (daha uzun) haksiz yere dusuk gosterirdi. Sabit pencere bu etkiyi
    kaldiriyor; pencereden kisa metin zaten yok (en kisa cevap 150+ sozcuk).
    """
    p = kelimeler[:pencere]
    if not p:
        return 0.0
    return len(set(p)) / len(p)


# Yan cumle / karmasik yapi isaretleri. Band 8'in "cumle yapilari cesitli"
# olcutunun kaba karsiligi. Tek tek hicbiri kanit degil, yogunlugu anlamli.
YAN_CUMLE = re.compile(
    r"\b(which|whom|whose|although|though|whereas|while|whilst|despite|unless|"
    r"whereby|since|as long as|even if|even though|rather than|not only|"
    r"in order to|so that|given that|provided that|having|thereby|thus)\b",
    re.I,
)

# Prompt: band 5'te baglaclar mekanik ("Firstly... Secondly...").
MEKANIK = re.compile(
    r"(^|[.\n]\s*)(firstly|secondly|thirdly|fourthly|lastly|"
    r"in conclusion|to sum up|to conclude)\b",
    re.I,
)

# --- E: dilbilgisi hatasi isaretleri --------------------------------------
# Yuksek kesinlik hedefleniyor: yakaladigi her sey gercekten hata olsun, hepsini
# yakalamasi gerekmiyor. Amac band 5 ile band 8 arasinda yogunluk farki olculmesi.
TEMEL_FIIL = (r"go|come|show|make|take|start|increase|decrease|have|get|give|do|"
              r"lose|rise|fall|use|need|spend|help|work|live|want|think|know|"
              r"become|grow|reach|stay|remain|continue|change|cause|affect|say|"
              r"break|cook|pay|wait|arrive|send|write|read|open|close|sleep|buy|"
              r"teach|save|decide|forget|look|finish|repair|learn|call|enter|"
              r"understand|feel|bring|put|keep|leave|speak|talk|study|drive")

# Tekil sayilabilir adlar - "many subject", "two month" gibi cogul dusmesini yakalar.
TEKIL_AD = (r"town|year|month|week|day|hour|minute|country|city|person|student|"
            r"child|company|group|reason|problem|thing|way|subject|lesson|"
            r"service|doctor|machine|family|comment|customer|passenger|"
            r"condition|date|place|book|job|hospital|school|shop|room|car")

HATA_IZLERI = [
    # "the graph is show", "they are go"
    ("is/are + yalin fiil",
     re.compile(r"\b(is|are|was|were|am)\s+(%s)\b" % TEMEL_FIIL, re.I)),
    # "I am agree with"
    ("am/is agree",
     re.compile(r"\b(am|is|are|was|were)\s+agree\b", re.I)),
    # "it lose", "this graph show", "he go" - zamir oznesi.
    # "that" listeden cikarildi: iliski zamiri olarak cogul onculu olabiliyor
    # ("the rules that come into force" dogru). Algi/ettirgen fiilden sonra gelen
    # yalin mastar da elenmeli ("I have watched it change" dogru).
    ("3. tekil -s dusmesi",
     re.compile(r"(?<!\bwatch )(?<!\bwatched )(?<!\bsee )(?<!\bsaw )(?<!\bseen )"
                r"(?<!\bhear )(?<!\bheard )(?<!\bmake )(?<!\bmade )(?<!\blet )"
                r"(?<!\bhelp )(?<!\bhelped )(?<!\bwill )(?<!\bcan )(?<!\bmust )"
                r"\b(it|he|she|this)\s+(%s)\b" % TEMEL_FIIL, re.I)),
    # "the bus come very late", "the machine break" - ad oznesi.
    # Iki koruma, ikisi de band 8'de yanlis alarm verdigi icin eklendi:
    #   - ad cogulsa atla ("The consequences fall" dogru)
    #   - "the X" bir edattan sonra geliyorsa atla, cunku o zaman ozne degil edat
    #     tumleci ("the homes closest to the centre have been" -> ozne "homes")
    ("3. tekil -s dusmesi (ad)",
     re.compile(r"(?<!\bto )(?<!\bof )(?<!\bin )(?<!\bon )(?<!\bat )(?<!\bfor )"
                r"(?<!\bfrom )(?<!\bwith )(?<!\bby )(?<!\bnear )(?<!\binto )"
                r"\bthe\s+[a-z]*[^s\W]\s+(%s)\b" % TEMEL_FIIL, re.I)),
    # "he don't know", "the bus don't come", "it don't help"
    ("tekil ozne + don't",
     re.compile(r"\b(he|she|it|this|that|the\s+[a-z]+|nobody|everybody)\s+"
                r"don't\b", re.I)),
    # "people is", "they is", "we is". Iyelik/tanimlik onundeyse atlanir:
    # "a state which cannot house its people has misjudged" - orada "people"
    # ozne degil nesne.
    ("ozne-yuklem uyumsuzlugu",
     re.compile(r"(?<!\bits )(?<!\bhis )(?<!\bher )(?<!\btheir )(?<!\bour )"
                r"(?<!\bthe )(?<!\bmany )(?<!\bfew )"
                r"\b(people|they|we|you|children|men|women|students)\s+"
                r"(is|was|has|does)\b", re.I)),
    # "there is many disadvantage", "there is not enough doctor"
    ("there is + cogul",
     re.compile(r"\bthere\s+(is|was)\s+(many|several|a lot of|lots of|two|"
                r"three|four|five|some\s+\w+s\b)", re.I)),
    # "more higher", "the most high", "more strong"
    ("cift derecelendirme",
     re.compile(r"\b(more|most)\s+(\w+er\b|\w+est\b|high|big|low|good|bad|large|"
                r"small|easy|cheap|strong|safe|clear|hard|rich|poor|happy|quick|"
                r"fast|simple)\b", re.I)),
    # sayilamayan adin cogulu
    ("sayilamayan cogul",
     re.compile(r"\b(peoples|informations|advices|equipments|knowledges|"
                r"researches|furnitures|homeworks|softwares|traffics|moneys)\b",
                re.I)),
    # "three town", "many subject", "six week"
    ("belirtec + tekil ad",
     re.compile(r"\b(two|three|four|five|six|seven|eight|nine|ten|many|several|"
                r"few|all the|these|those)\s+(%s)\b" % TEKIL_AD, re.I)),
    # "didn't went", "did not increased"
    ("did + cekimli fiil",
     re.compile(r"\b(did|didn't|does|doesn't|do|don't)\s+(not\s+)?(\w+ed|went|"
                r"came|took|made)\b", re.I)),
    # "must to take", "can to do"
    ("kip + to",
     re.compile(r"\b(must|can|should|will|may|might)\s+to\s+[a-z]+", re.I)),
    # "for complain", "for learn the basic thing" (amac icin "to" gerekiyor)
    ("for + yalin fiil",
     re.compile(r"\bfor\s+(complain|learn|repair|explain|discuss|improve|"
                r"protect|reduce|solve|prevent)\b", re.I)),
    # "arrive to my home", "enter to the system"
    ("yanlis edat",
     re.compile(r"\b(arrive|arrives|arrived|enter|enters|entered|discuss|"
                r"discussed|mention|mentioned|depend|depends)\s+"
                r"(to|of|about)\b", re.I)),
    # "in the internet"
    ("in the internet",
     re.compile(r"\bin the internet\b", re.I)),
    # "a operation", "a old person" - unlu oncesi a
    ("a/an karisikligi",
     re.compile(r"\ba\s+(?!u|one|euro|Euro)[aeiou][a-z]+", re.I)),
    # "in the 1995"
    ("tanimlik hatasi (yil)",
     re.compile(r"\bin the (19|20)\d\d\b", re.I)),
]


def hata_izleri(metin):
    bulunan = []
    for ad, kalip in HATA_IZLERI:
        for e in kalip.finditer(metin):
            bulunan.append((ad, e.group(0).strip()))
    return bulunan


def ngramlar(kelimeler, n=5):
    return set(tuple(kelimeler[i:i + n]) for i in range(len(kelimeler) - n + 1))


def en_uzun_ortak(a, b):
    """En uzun ortak KESINTISIZ sozcuk dizisi (uzunluk, metin).

    Ortak n-gram SAYMAK yaniltiyordu: tek bir 12 sozcukluk ortak cumle, 5 ayri
    "ortak 8'li dizi" olarak gorunuyor ve dosya bes kez kopyalanmis gibi
    okunuyordu. Onemli olan sayi degil en uzun dizinin uzunlugu.
    """
    onceki = [0] * (len(b) + 1)
    en_iyi, son = 0, 0
    for i in range(1, len(a) + 1):
        simdiki = [0] * (len(b) + 1)
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                simdiki[j] = onceki[j - 1] + 1
                if simdiki[j] > en_iyi:
                    en_iyi, son = simdiki[j], i
        onceki = simdiki
    return en_iyi, " ".join(a[son - en_iyi:son])


# --- olcum ----------------------------------------------------------------

def olc(metin):
    kel = sozcukler(metin)
    cum = cumleler(metin)
    uzunluklar = [len(sozcukler(c)) for c in cum] or [0]
    ort = sum(uzunluklar) / len(uzunluklar)
    sapma = (sum((u - ort) ** 2 for u in uzunluklar) / len(uzunluklar)) ** 0.5
    hatalar = hata_izleri(metin)
    return {
        "kelime": kelime_say(metin),
        "ttr": ttr(kel),
        "cumle": len(cum),
        "cumle_ort": ort,
        "cumle_sapma": sapma,
        "yan_cumle": 100.0 * len(YAN_CUMLE.findall(metin)) / max(1, len(kel)),
        "mekanik": len(MEKANIK.findall(metin)),
        "hata": hatalar,
        "hata_yog": 100.0 * len(hatalar) / max(1, len(kel)),
        "kelimeler": kel,
    }


def main():
    dosyalar = sorted(d for d in os.listdir(CEVAP) if d.endswith(".json"))
    if not dosyalar:
        print("Cevap dosyasi yok: %s" % CEVAP)
        return 1

    havuz = gorev_havuzu()
    olcumler = {}   # kod -> {band: metrik}
    for d in dosyalar:
        kod = d[:-5]
        veri = oku(os.path.join(CEVAP, d))
        cevaplar = {float(a["band"]): a for a in veri.get("answers", [])}
        if set(cevaplar) != set(BANTLAR):
            bulgu(d, "-", "band uclusu eksik: %s" % sorted(cevaplar))
            continue
        olcumler[kod] = {b: olc(cevaplar[b]["text"]) for b in BANTLAR}

    ayrim_sayaci = Counter()

    for kod in sorted(olcumler):
        m = olcumler[kod]
        t2 = kod.startswith("T2")
        alt_sinir = 250 if t2 else 150

        # A - alt sinir. Prompt yalnizca su iki seyi soyluyor: her cevap alt sinirin
        # uzerinde olacak ve band 5 "sinirin ucunda" olacak. Bantlar arasi kelime
        # artisini SART KOSMUYOR - band 8 daha kisa da olabilir, cunku fark uzunlukta
        # degil nitelikte aranmali. Ilk yazimda buraya konan "kelime sayisi tirmanmali"
        # kurali prompt'ta yok; yedi dosyayi bulgu olarak isaretledi, kaldirildi.
        for b in BANTLAR:
            if m[b]["kelime"] < alt_sinir:
                bulgu(kod, "A", "band %s alt sinirin altinda: %d < %d"
                      % (b, m[b]["kelime"], alt_sinir))

        # B - sozcuk cesitliligi (uzunluktan arindirilmis)
        if m[8.0]["ttr"] - m[5.0]["ttr"] < 0.03:
            bulgu(kod, "B", "band 5 ile 8 arasinda sozcuk cesitliligi farki yok: "
                            "TTR %.2f -> %.2f" % (m[5.0]["ttr"], m[8.0]["ttr"]))
        if m[6.5]["ttr"] < m[5.0]["ttr"] - 0.02:
            bulgu(kod, "B", "band 6,5 sozcuk cesitliligi band 5'in altinda: "
                            "%.2f < %.2f" % (m[6.5]["ttr"], m[5.0]["ttr"]))

        # C - cumle yapisi. Olcut yan cumle yogunlugu; cumle uzunlugu sapmasi
        # bilerek bulgu uretmiyor, cunku band 5'te sapmayi yukselten sey iyi degil
        # kotu bir sey: bagsiz uzayan cumleler. Yani yuksek sapma tek basina ust
        # band isareti degil - ozette bilgi olarak yaziliyor.
        if m[8.0]["yan_cumle"] <= m[5.0]["yan_cumle"]:
            bulgu(kod, "C", "band 8 yan cumle yogunlugu band 5'i gecmiyor: "
                            "%.1f <= %.1f" % (m[8.0]["yan_cumle"], m[5.0]["yan_cumle"]))

        # D - mekanik baglac. Prompt bunu band 5'in isaretlerinden biri olarak
        # sayiyor, hepsinde bulunmasi gereken bir sart olarak degil; "band 5'te
        # yok" tek basina bulgu degil (mektupta Firstly/Secondly zaten daha az
        # dogal). Bulgu sayilan sey ters yon: band 8'in band 5'ten mekanik olmasi.
        if m[8.0]["mekanik"] > m[5.0]["mekanik"]:
            bulgu(kod, "D", "band 8 band 5'ten daha mekanik: %d > %d"
                  % (m[8.0]["mekanik"], m[5.0]["mekanik"]))

        # E - band 5 gercekten hatali mi, band 8 temiz mi
        if len(m[5.0]["hata"]) == 0:
            bulgu(kod, "E", "band 5 cevabinda tek bir dilbilgisi hata izi yok - "
                            "'farkinda olmadan duzgun yazilmis' olabilir")
        if len(m[8.0]["hata"]) > 2:
            bulgu(kod, "E", "band 8'de %d hata izi: %s"
                  % (len(m[8.0]["hata"]),
                     ", ".join("%s (%s)" % (a, b) for a, b in m[8.0]["hata"][:4])))
        if len(m[5.0]["hata"]) <= len(m[8.0]["hata"]):
            bulgu(kod, "E", "band 5 band 8'den daha hatali degil: %d <= %d"
                  % (len(m[5.0]["hata"]), len(m[8.0]["hata"])))

        # F - dosya ici kopyala-yapistir. Aranan kusur: ayni metnin iki banda
        # yapistirilmasi. Esik ona gore konuyor - en uzun ORTAK KESINTISIZ DIZI
        # 15 sozcuk veya ustu, ya da ortusme kisa cevabin %10'unu gecmis.
        # Bunun altindaki ortusme turun kendi kalibi: Task 1 girisi gorevin
        # cumlesinin paraforu, mektupta hitap/kapanis, her iki cevapta da gecen
        # ozel adlar ("the Fenton Street community garden"). Bunlar ozete
        # gozlem olarak yaziliyor, bulgu sayilmiyor.
        for a, b in ((5.0, 6.5), (6.5, 8.0), (5.0, 8.0)):
            n_ortak, dizi = en_uzun_ortak(m[a]["kelimeler"], m[b]["kelimeler"])
            oran = n_ortak / max(1, min(len(m[a]["kelimeler"]),
                                        len(m[b]["kelimeler"])))
            if n_ortak >= 15 or oran >= 0.10:
                bulgu(kod, "F", "band %s ile %s arasinda %d sozcukluk ortak dizi "
                                "(%%%.0f): %s" % (a, b, n_ortak, 100 * oran, dizi))
            elif n_ortak >= 8:
                gozlemler.append((kod, a, b, n_ortak, dizi))

        # G - fark uzunluk disinda kac boyutta gorunuyor
        boyutlar = {
            "sozcuk": m[8.0]["ttr"] - m[5.0]["ttr"] >= 0.03,
            "yan_cumle": m[8.0]["yan_cumle"] > m[5.0]["yan_cumle"] * 1.5,
            "cumle_sapma": m[8.0]["cumle_sapma"] > m[5.0]["cumle_sapma"] * 1.2,
            "hata": len(m[5.0]["hata"]) >= len(m[8.0]["hata"]) + 3,
            "mekanik": m[5.0]["mekanik"] > m[8.0]["mekanik"],
        }
        n = sum(boyutlar.values())
        ayrim_sayaci[n] += 1
        if n < 3:
            bulgu(kod, "G", "band 5 ile 8 arasindaki fark yalnizca %d boyutta: %s "
                            "(uzunluk disinda ayrisma yetersiz)"
                  % (n, ", ".join(k for k, v in boyutlar.items() if v) or "hicbiri"))

    # --- ozet -------------------------------------------------------------
    print("Olculen gorev: %d  (cevap: %d)" % (len(olcumler), 3 * len(olcumler)))
    print()
    print("Band ortalamalari (90 cevap):")
    print("  %-6s %7s %6s %8s %8s %7s %7s" % ("band", "kelime", "TTR", "yancumle",
                                              "c.sapma", "mekanik", "hata/100"))
    for b in BANTLAR:
        d = [olcumler[k][b] for k in olcumler]
        n = len(d)
        print("  %-6s %7.0f %6.2f %8.2f %8.1f %7.1f %7.2f"
              % (b,
                 sum(x["kelime"] for x in d) / n,
                 sum(x["ttr"] for x in d) / n,
                 sum(x["yan_cumle"] for x in d) / n,
                 sum(x["cumle_sapma"] for x in d) / n,
                 sum(x["mekanik"] for x in d) / n,
                 sum(x["hata_yog"] for x in d) / n))

    print()
    print("Uzunluk disinda kac boyutta ayrisiyor (5 boyut uzerinden):")
    for n in sorted(ayrim_sayaci, reverse=True):
        print("  %d boyut: %2d gorev" % (n, ayrim_sayaci[n]))

    print()
    tur_sayaci = Counter()
    for k in olcumler:
        for ad, _ in olcumler[k][5.0]["hata"]:
            tur_sayaci[ad] += 1
    print("Band 5'te en sik hata izleri:")
    for ad, s in tur_sayaci.most_common(8):
        print("  %-28s %3d" % (ad, s))

    if gozlemler:
        print()
        print("Bandlar arasi ortak dizi (8-14 sozcuk - bulgu degil, gozlem):")
        for kod, a, b, n, dizi in gozlemler:
            print("  %-8s band %s/%s  %2d sozcuk  \"%s\"" % (kod, a, b, n, dizi))

    print()
    if not bulgular:
        print("BULGU YOK - yedi ayrim denetiminin hepsi temiz.")
    else:
        print("BULGU: %d" % len(bulgular))
        for dosya, tur, mesaj in bulgular:
            print("  [%s] %-8s %s" % (tur, dosya, mesaj))
    return 1 if bulgular else 0


if __name__ == "__main__":
    sys.exit(main())
