"""FAZ 1.3-1.4: 157 alistirma kaleminin 8 yeni pasaja dagitimi.

Girdi: `content/reading/practice/*.json` (12 paket, 157 kalem / 160 numara).
Cikti: `denetim/B3-pasaj-dagitimi.md` + `denetim/B3-pasaj-dagitimi.json`.

Arac SALT OKUNURDUR: hicbir soru/pasaj dosyasina yazmaz, yalniz `denetim/`
altina rapor uretir. Dagitim karari bu dosyanin icinde veri olarak durur
(`DAGITIM`); arac o karari mevcut icerige karsi DOGRULAR:

1. kaynak kume ortusmesi — her (paket, eski passage_id) kumesi tam bir kez
   dagitilmis mi, uydurma kume var mi (grup butunlugu: bir kume bolunmez),
2. sayim korunumu   — paket bazinda ve toplamda kalem/numara sayisi degismiyor,
3. paket cesidi     — metin basina en cok 5 farkli paket,
4. paragraf butcesi — paragraf basina en cok 3 soru; kanit cumlesi basina en
   cok 1 soru; kisa cevap kalemleri BASKA hicbir sorunun dokunmadigi paragrafa
   capalanacagi icin her biri ayri bir paragrafi tuketir,
5. kisa cevap duzeni — akademik metin basina 1-2 kalem, GT metninde 0, toplam 10,
6. bagli kararlar   — GT kaynakli kumeler + cumle sonu eslestirmenin IKI grubu
   G07'ye; diyagram etiketleme A19'a.

"Kume" = (paket dosyasi, eski passage_id) ikilisi. Duz `items` tasiyan
paketlerde grup alani yok; oradaki kume, ayni pasaja capali kalemlerin
olusturdugu ortuk gruptur (bugun hepsi bitisik numara blogu).

Kullanim: python tools/b3-dagitim.py
"""
import datetime
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

# --- butce sabitleri (content/PLAN-EK-kurallar.md 2. madde + gorev tanimi) ---
SORU_PARAGRAF = 3       # paragraf basina en cok soru
KANIT_SORU = 1          # kanit cumlesi basina en cok soru
METIN_KALEM_HEDEF = 20  # metin basina hedef/tavan kalem (yumusak sinir)
PAKET_UST = 5           # metin basina en cok farkli paket (sert sinir)
PARAGRAF_ALT = 7        # prompts/01-pasaj-secimi.md: 7-10 harflendirilmis paragraf
PARAGRAF_UST = 10
KELIME_ALT = 700
KELIME_UST = 900

PAKET_KOD = {
    "sentence-completion.json": "SC",
    "note-completion.json": "NC",
    "summary-completion.json": "SUM",
    "short-answer.json": "SA",
    "diagram-labelling.json": "DL",
    "matching-information.json": "MI",
    "true-false-not-given.json": "TFNG",
    "yes-no-not-given.json": "YNNG",
    "multiple-choice.json": "MC",
    "matching-headings.json": "MH",
    "matching-features.json": "MF",
    "matching-sentence-endings.json": "MSE",
}
KOD_SIRA = ["SC", "NC", "SUM", "SA", "DL", "MI", "TFNG", "YNNG", "MC", "MH", "MF", "MSE"]
KOD_AD = {
    "SC": "cumle tamamlama", "NC": "not tamamlama", "SUM": "ozet tamamlama",
    "SA": "kisa cevap", "DL": "diyagram etiketleme", "MI": "bilgi eslestirme",
    "TFNG": "TRUE/FALSE/NOT GIVEN", "YNNG": "YES/NO/NOT GIVEN",
    "MC": "coktan secmeli", "MH": "baslik eslestirme", "MF": "ozellik eslestirme",
    "MSE": "cumle sonu eslestirme",
}
GROUP_ONEK = {
    "SC": "P-SC", "NC": "P-NC", "SUM": "P-SUM", "SA": "P-SA", "DL": "P-DL",
    "MI": "P-MI", "TFNG": "P-TF", "YNNG": "P-YN", "MC": "P-MC",
    "MH": "P-MH", "MF": "P-MF", "MSE": "P-MSE",
}

# ---------------------------------------------------------------------------
# Yeni metinler: kimlik + konu onerisi
# Konu kurali (plan 1.2/1): mevcut 18 metnin alt konularina DEGMEYECEK.
# Kaynak kurali (prompts/01-pasaj-secimi.md): yalniz PLOS · NASA/NOAA/USGS ·
# OpenStax; Wikipedia ve The Conversation yasak.
# ---------------------------------------------------------------------------
YENI_PASAJLAR = [
    {
        "passage_id": "A13", "module": "academic", "section": None,
        "konu": "malzeme muhendisligi / kendi kendini onaran beton",
        "konu_ozeti": "Bakteri tasiyan kapsullerle catlagini kendi kapatan beton karisimlarinin "
                      "farkli laboratuvarlarda denenmesi; hangi ekip hangi kosulda ne olctu.",
        "kaynak": "PLOS ONE (biyo-beton / self-healing concrete calismalari)",
        "kaynak_yedegi": "OpenStax Chemistry (baglayici malzeme bolumu)",
        "en_yakin_mevcut": "yok — mevcut 18 metinde muhendislik/malzeme konusu hic yok",
        "ayrim": "Mevcut konularin hicbirine degmiyor (hayvan davranisi, iklim/jeoloji, uzay, "
                 "tarih/arkeoloji, toplum/is, saglik/davranis disinda yeni bir alan).",
    },
    {
        "passage_id": "A14", "module": "academic", "section": None,
        "konu": "bilim pratigi / arastirma verisinin paylasilmamasi",
        "konu_ozeti": "Arastirmacilarin ham verisini neden paylasmadigi uzerine meta-arastirma; "
                      "yazarin degerlendirme ve itiraz cumleleri bol.",
        "kaynak": "PLOS ONE (meta-research / data sharing calismalari)",
        "kaynak_yedegi": "OpenStax Sociology (arastirma yontemleri bolumu)",
        "en_yakin_mevcut": "A06/A10 (toplum-is) — ofis duzeni ve uzaktan calisma",
        "ayrim": "Konu is yeri duzeni degil, bilimsel calismanin kendi pratigi; ofis/uzaktan "
                 "calisma alt konularina hic girmiyor.",
    },
    {
        "passage_id": "A15", "module": "academic", "section": None,
        "konu": "bitki biyolojisi / bitkilerin kimyasal savunmasi",
        "konu_ozeti": "Yaprak zedelendiginde salinan kimyasallarin komsu bitkilerde tepki "
                      "baslatmasi; olculen degerler ve arastirmacinin yorum cumleleri.",
        "kaynak": "PLOS Biology / PLOS ONE (bitki savunma kimyasi)",
        "kaynak_yedegi": "OpenStax Biology (bitki tepkileri bolumu)",
        "en_yakin_mevcut": "A01/A02/A07 (doga) — ama ucu de HAYVAN davranisi",
        "ayrim": "Hayvan yok; konu bitki fizyolojisi/kimyasi. Mevcut doga metinlerinin alt "
                 "konusu (fil, ahtapot, balina davranisi) ile ortusmuyor.",
    },
    {
        "passage_id": "A16", "module": "academic", "section": None,
        "konu": "spor bilimi / kosu biyomekanigi ve zemin degisimi",
        "konu_ozeti": "Kosucularin zemin sertligi degistiginde adim uzunlugu ve temas suresini "
                      "nasil degistirdigi; olcum agirlikli olgusal anlatim.",
        "kaynak": "PLOS ONE (kosu biyomekanigi calismalari)",
        "kaynak_yedegi": "OpenStax Anatomy & Physiology (hareket sistemi bolumu)",
        "en_yakin_mevcut": "A11/A12 (saglik-davranis) — ruh hali ve bellek",
        "ayrim": "Konu ruh hali/bellek degil, olculen hareket mekanigi; psikolojik sonuc "
                 "iddiasi tasimayacak.",
    },
    {
        "passage_id": "A17", "module": "academic", "section": None,
        "konu": "mikrobiyoloji / biyofilmlerin yuzeyleri kolonilestirmesi",
        "konu_ozeti": "Yeni bir yuzeyde mikroorganizma tabakasinin asama asama olusmasi; her "
                      "paragrafta ayri bir bulunabilir olgu.",
        "kaynak": "PLOS ONE (biyofilm olusumu calismalari)",
        "kaynak_yedegi": "OpenStax Microbiology",
        "en_yakin_mevcut": "yok — mevcut 18 metinde mikrobiyoloji hic yok",
        "ayrim": "Saglik/tedavi iddiasina girmeden mikrobiyal ekoloji anlatiliyor.",
    },
    {
        "passage_id": "A18", "module": "academic", "section": None,
        "konu": "genetik yontem / DNA barkodlamayla tur tanimlama",
        "konu_ozeti": "Kucuk bir gen parcasindan tur tanimlama yonteminin nasil kuruldugu ve "
                      "nerede yaniltici oldugu; somut deger ve ad yogun.",
        "kaynak": "PLOS ONE (DNA barcoding calismalari)",
        "kaynak_yedegi": "OpenStax Biology (biyoteknoloji bolumu)",
        "en_yakin_mevcut": "A01/A02/A07 (doga) — hayvan davranisi",
        "ayrim": "Davranis anlatmiyor; laboratuvar yontemi ve yontemin sinirlari anlatiliyor.",
    },
    {
        "passage_id": "A19", "module": "academic", "section": None,
        "konu": "su teknolojisi / gunes enerjili damitma duzenegi (SUREC METNI)",
        "konu_ozeti": "Tuzlu suyun gunesle buharlastirilip yogusturuldugu duzenegin asamalari; "
                      "cizilebilir duzenek — diyagram etiketlemenin 10 kalemi buraya.",
        "kaynak": "PLOS ONE (gunes damitma / solar still calismalari)",
        "kaynak_yedegi": "OpenStax Chemistry (faz degisimi bolumu) · USGS su bilimi sayfalari",
        "en_yakin_mevcut": "A03/A08 (iklim-jeoloji-okyanus)",
        "ayrim": "Iklim/jeoloji olgusu degil, insan yapimi bir duzenegin isleyisi; deniz/okyanus "
                 "surec anlatimina girmeyecek.",
    },
    {
        "passage_id": "G07", "module": "general", "section": 3,
        "konu": "ev bitkileri ve ic hava kalitesi (GT 3. bolum, uzun genel ilgi metni)",
        "konu_ozeti": "Evlerdeki bitkilerin ic hava olcumlerine etkisi uzerine birbiriyle "
                      "cekisen ekipler; neden-sonuc ve karsitlik cumlesi yogun anlati.",
        "kaynak": "PLOS ONE (ic mekan bitkileri / hava kalitesi calismalari)",
        "kaynak_yedegi": "OpenStax Biology (bitki fizyolojisi) — anlatim sadelestirilerek",
        "en_yakin_mevcut": "G05 (gida israfi), G06 (gonulluluk) — ikisi de GT 3. bolum",
        "ayrim": "Tuketim davranisi ve gonullu calisma alt konularina girmiyor; olcum agirlikli "
                 "ev ici hava konusu. (prompts/01-pasaj-secimi.md'nin GT 3. bolum ornek "
                 "listesinde zaten geciyor.)",
    },
]

# ---------------------------------------------------------------------------
# Dagitim karari: (paket dosyasi, eski passage_id) -> yeni passage_id
# Grup butunlugu: her satir bir KUME, kume bolunmez.
# ---------------------------------------------------------------------------
DAGITIM = [
    # --- cumle tamamlama (15) ---
    ("sentence-completion.json", "A01", "A13"),
    ("sentence-completion.json", "A02", "A13"),
    ("sentence-completion.json", "A03", "A14"),
    ("sentence-completion.json", "A04", "A17"),
    ("sentence-completion.json", "A05", "A18"),
    # --- not tamamlama (15) ---
    ("note-completion.json", "A06", "A15"),
    ("note-completion.json", "A07", "A16"),
    ("note-completion.json", "A08", "A18"),
    ("note-completion.json", "A09", "A18"),
    ("note-completion.json", "A12", "A19"),
    # --- ozet tamamlama (15): GT kaynakli iki kume G07'ye ---
    ("summary-completion.json", "A10", "A15"),
    ("summary-completion.json", "A11", "A19"),
    ("summary-completion.json", "G05", "G07"),
    ("summary-completion.json", "G06", "G07"),
    # --- kisa cevap (10): 10 tekil kalem -> 7 akademik metne 1-2'ser ---
    ("short-answer.json", "A01", "A13"),
    ("short-answer.json", "A02", "A13"),
    ("short-answer.json", "A03", "A14"),
    ("short-answer.json", "A04", "A15"),
    ("short-answer.json", "A05", "A16"),
    ("short-answer.json", "A06", "A17"),
    ("short-answer.json", "A07", "A18"),
    ("short-answer.json", "A08", "A18"),
    ("short-answer.json", "A09", "A19"),
    ("short-answer.json", "A12", "A19"),
    # --- diyagram etiketleme (10): tamami surec metni A19'a (kullanici karari) ---
    ("diagram-labelling.json", "G01", "A19"),
    ("diagram-labelling.json", "G02", "A19"),
    ("diagram-labelling.json", "G03", "A19"),
    ("diagram-labelling.json", "G04", "A19"),
    # --- bilgi eslestirme (15) ---
    ("matching-information.json", "A01", "A15"),
    ("matching-information.json", "A04", "A17"),
    ("matching-information.json", "A07", "A17"),
    ("matching-information.json", "A11", "A18"),
    # --- TRUE/FALSE/NOT GIVEN (15) ---
    ("true-false-not-given.json", "A02", "A13"),
    ("true-false-not-given.json", "A05", "A16"),
    ("true-false-not-given.json", "A08", "A16"),
    ("true-false-not-given.json", "A09", "A17"),
    # --- YES/NO/NOT GIVEN (15): TFNG metinleriyle ayri metinlerde ---
    ("yes-no-not-given.json", "A06", "A14"),
    ("yes-no-not-given.json", "A10", "A14"),
    ("yes-no-not-given.json", "A11", "A15"),
    ("yes-no-not-given.json", "A12", "A15"),
    # --- coktan secmeli (12 kalem / 15 numara) ---
    ("multiple-choice.json", "A02", "A13"),
    ("multiple-choice.json", "A05", "A14"),
    ("multiple-choice.json", "A08", "A16"),
    ("multiple-choice.json", "A11", "A17"),
    # --- baslik eslestirme (15) ---
    ("matching-headings.json", "A01", "A14"),
    ("matching-headings.json", "A09", "A16"),
    ("matching-headings.json", "A12", "A18"),
    # --- ozellik eslestirme (10): GT kaynakli kume G07'ye ---
    ("matching-features.json", "A10", "A13"),
    ("matching-features.json", "G05", "G07"),
    # --- cumle sonu eslestirme (10): IKI grup da G07'ye ---
    ("matching-sentence-endings.json", "A07", "G07"),
    ("matching-sentence-endings.json", "G06", "G07"),
]

# Bagli kararlar (gorev tanimi): dogrulama bunlari ayrica sinar.
GT_KAYNAKLI_KUMELER = [
    ("summary-completion.json", "G05"), ("summary-completion.json", "G06"),
    ("matching-features.json", "G05"), ("matching-sentence-endings.json", "G06"),
]
MSE_HEDEF = "G07"
DL_HEDEF = "A19"


# ---------------------------------------------------------------------------
# envanter
# ---------------------------------------------------------------------------

def kume_envanter():
    """(paket dosya adi, eski passage_id) -> kalem/numara sayimi."""
    out = {}
    for dosya in sorted(ortak.bul("content/reading/practice/*.json")):
        ad = dosya.rsplit("/", 1)[-1]
        d = ortak.oku(dosya)
        for g, it in ortak.kumeli_sorular(d):
            pid = it.get("passage_id") or g.get("passage_id") or d.get("passage_id")
            k = out.setdefault((ad, pid), {
                "paket": ad, "kod": PAKET_KOD.get(ad, ad), "eski_passage_id": pid,
                "question_type": g.get("question_type") or d.get("question_type"),
                "group_id": g.get("group_id"), "kalem": 0, "numara": 0, "numaralar": [],
            })
            k["kalem"] += 1
            ns = ortak.numaralar(it)
            k["numara"] += len(ns)
            k["numaralar"] += ns
    for k in out.values():
        k["numaralar"] = sorted(k["numaralar"])
    return out


def numara_araligi(numaralar):
    if not numaralar:
        return ""
    if numaralar == list(range(numaralar[0], numaralar[-1] + 1)):
        return "%d-%d" % (numaralar[0], numaralar[-1]) if len(numaralar) > 1 else str(numaralar[0])
    return ", ".join(str(n) for n in numaralar)


def bitisik(numaralar):
    return bool(numaralar) and numaralar == list(range(numaralar[0], numaralar[-1] + 1))


# ---------------------------------------------------------------------------
# paragraf butcesi
# ---------------------------------------------------------------------------

def paragraf_ihtiyaci(kod_kalem):
    """(en az, onerilen) paragraf sayisi.

    - yogunluk: paragraf basina en cok SORU_PARAGRAF soru; kisa cevabin her
      kalemi BASKA hicbir sorunun dokunmadigi bir paragrafi tuketir,
    - ayrik paragraf: baslik/bilgi eslestirmenin her kalemi ayri bir paragrafa
      isaret eder (ikisi ayni paragrafi paylasabilir, kisa cevap paylasamaz),
    - taban: 7-10 paragraf kurali; bilgi/baslik eslestirme varsa en az 8
      harflendirilmis paragraf (bugunku yonergeler "EIGHT paragraphs" diyor).
    """
    sa = kod_kalem.get("SA", 0)
    toplam = sum(kod_kalem.values())
    yogunluk = int(math.ceil((toplam - sa) / float(SORU_PARAGRAF))) + sa
    ayrik = max(kod_kalem.get("MH", 0), kod_kalem.get("MI", 0)) + sa
    taban = 8 if (kod_kalem.get("MH") or kod_kalem.get("MI")) else PARAGRAF_ALT
    en_az = max(yogunluk, ayrik, taban)
    onerilen = min(PARAGRAF_UST, max(en_az + 1, taban))
    if toplam > METIN_KALEM_HEDEF:
        onerilen = PARAGRAF_UST
    return en_az, onerilen


def yuk_metni(paragraf_basi_soru):
    """Paragraf basi soru degeri; kisa cevap tum paragraflari yerse hesaplanamaz."""
    return "hesaplanamiyor" if paragraf_basi_soru is None else "%.2f" % paragraf_basi_soru


def sikisikliklar(m):
    """Kural ihlali degil ama yazimda payi olmayan noktalar."""
    out = []
    if m["kalem"] > METIN_KALEM_HEDEF:
        out.append("%d kalem — metin basina hedef ~%d asiliyor; yuk ancak %d paragrafla tasiniyor"
                   % (m["kalem"], METIN_KALEM_HEDEF, m["paragraf_onerilen"]))
    if m["paragraf_onerilen"] >= PARAGRAF_UST:
        out.append("paragraf sayisi ust sinirda (%d) — metin kisaltilirsa butce bozulur"
                   % PARAGRAF_UST)
    if m["paragraf_basi_soru"] is not None and m["paragraf_basi_soru"] > 2.5:
        out.append("paragraf basina %.2f soru — 3'luk tavana yakin" % m["paragraf_basi_soru"])
    ayrik = max(m["paket_kalem"].get("MH", 0), m["paket_kalem"].get("MI", 0)) \
        + m["paket_kalem"].get("SA", 0)
    if ayrik and m["paragraf_onerilen"] - ayrik <= 1:
        out.append("ayri paragraf isteyen kalemler (baslik/bilgi eslestirme + kisa cevap) %d "
                   "paragraf tutuyor, metinde %d paragraf var — yedek paragraf yok"
                   % (ayrik, m["paragraf_onerilen"]))
    return out


def kelime_araligi(toplam_kalem, module):
    alt = 800 if toplam_kalem >= METIN_KALEM_HEDEF else KELIME_ALT
    if module == "general":
        alt = max(alt, 850)   # GT 3. bolum: 750-900; yuk agir oldugu icin ust banda
    return alt, KELIME_UST


# ---------------------------------------------------------------------------
# tip -> on kosul (plan 1.2 tablosu + butce kuralindan turetilenler)
# ---------------------------------------------------------------------------

def on_kosullar(kod_kalem, en_az_par, onerilen_par):
    """Metnin saglamasi gereken on kosullar. 'kaynak' alani: plan tablosu mu,
    butce kuralindan turetilmis mi."""
    out = []
    toplam = sum(kod_kalem.values())
    tamamlama = sum(kod_kalem.get(k, 0) for k in ("SC", "NC", "SUM", "DL"))
    somut = tamamlama + kod_kalem.get("SA", 0)

    out.append({
        "kaynak": "prompts/01-pasaj-secimi.md + butce",
        "kosul": "%d-%d harflendirilmis paragraf (en az %d, onerilen %d)"
                 % (PARAGRAF_ALT, PARAGRAF_UST, en_az_par, onerilen_par),
    })
    out.append({
        "kaynak": "butce (kanit cumlesi basina en cok %d soru)" % KANIT_SORU,
        "kosul": "birbirinden ayri en az %d kanit cumlesi (her kalem kendi cumlesini alacak)"
                 % toplam,
    })
    if kod_kalem.get("MH"):
        out.append({
            "kaynak": "plan 1.2 tablosu (baslik eslestirme)",
            "kosul": "8-10 paragraf ve HER paragrafin ayirt edilebilir tek ana fikri; "
                     "%d paragraf baslik sorusuna acik olacak" % kod_kalem["MH"],
        })
    if kod_kalem.get("YNNG"):
        out.append({
            "kaynak": "plan 1.2 tablosu (YES/NO/NOT GIVEN)",
            "kosul": "en az %d yazar gorusu/degerlendirme cumlesi (tablo tabani 4; kalem sayisi "
                     "%d oldugu icin cumle basina 1 kural bunu yukseltiyor)"
                     % (max(4, kod_kalem["YNNG"]), kod_kalem["YNNG"]),
        })
    if somut:
        out.append({
            "kaynak": "plan 1.2 tablosu (tamamlama ailesi)",
            "kosul": "en az %d ayri somut sayi/olcu/ad, en az %d ayri paragrafa dagilmis — "
                     "hepsi metnin kendi calismasina ozgu (kamuya acik/ezberlenebilir deger yasak)"
                     % (somut, max(4, int(math.ceil(somut / float(SORU_PARAGRAF))))),
        })
    if kod_kalem.get("MF"):
        out.append({
            "kaynak": "plan 1.2 tablosu (ozellik eslestirme)",
            "kosul": "3-4 adi gecen arastirmaci/kurum ve toplam %d ayirt edici iddia "
                     "(her iddia tek bir ada baglanacak)" % kod_kalem["MF"],
        })
    if kod_kalem.get("MSE"):
        out.append({
            "kaynak": "plan 1.2 tablosu (cumle sonu eslestirme)",
            "kosul": "en az %d neden-sonuc/karsitlik cumlesi (tablo tabani 5; iki grup tasindigi "
                     "icin kalem sayisi belirleyici) — E7 recetesi burada uygulanacak"
                     % max(5, kod_kalem["MSE"]),
        })
    if kod_kalem.get("DL"):
        out.append({
            "kaynak": "plan 1.2 tablosu (diyagram etiketleme)",
            "kosul": "cizilebilir tek bir surec/duzenek anlatimi; en az %d etiketlenebilir "
                     "bilesen/asama, sirasi metinden izlenebilir" % kod_kalem["DL"],
        })
    if kod_kalem.get("TFNG"):
        out.append({
            "kaynak": "turetilmis (butce)",
            "kosul": "en az %d dogrulanabilir OLGU cumlesi (yazar gorusu degil); NOT GIVEN "
                     "kalemleri icin metnin sessiz kaldigi komsu noktalar birakilacak"
                     % kod_kalem["TFNG"],
        })
    if kod_kalem.get("MI"):
        out.append({
            "kaynak": "turetilmis (butce + bugunku yonerge)",
            "kosul": "en az 8 harflendirilmis paragraf ve %d ayri paragrafta bulunabilir olgu "
                     "(ayni paragraf iki bilgi sorusuna kaynak olmayacak)" % kod_kalem["MI"],
        })
    if kod_kalem.get("MC"):
        out.append({
            "kaynak": "turetilmis (butce)",
            "kosul": "%d ayri odak noktasi; her birinde 4 secenegi ayirt edecek kadar ayrinti "
                     "(genel kultur yanlis secenege capalanacak)" % kod_kalem["MC"],
        })
    if kod_kalem.get("SA"):
        out.append({
            "kaynak": "plan 1.4",
            "kosul": "%d paragraf BASKA hicbir sorunun dokunmadigi hale birakilacak; her birinde "
                     "3 kelime veya bir sayiyla cevaplanabilen, calismanin kendi sectigi bir deger"
                     % kod_kalem["SA"],
        })
    return out


# ---------------------------------------------------------------------------
# dagitim + dogrulama
# ---------------------------------------------------------------------------

def dagit(envanter):
    metinler = {}
    for p in YENI_PASAJLAR:
        metinler[p["passage_id"]] = {
            "passage_id": p["passage_id"], "module": p["module"], "section": p["section"],
            "konu": p["konu"], "konu_ozeti": p["konu_ozeti"], "kaynak": p["kaynak"],
            "kaynak_yedegi": p["kaynak_yedegi"], "en_yakin_mevcut": p["en_yakin_mevcut"],
            "ayrim": p["ayrim"], "kumeler": [], "kalem": 0, "numara": 0, "paket_kalem": {},
        }
    hatalar, uyarilar = [], []
    gorulen = {}
    for paket, eski, yeni in DAGITIM:
        anahtar = (paket, eski)
        if anahtar not in envanter:
            hatalar.append("DAGITIM'da olmayan kume: %s / %s" % (paket, eski))
            continue
        if anahtar in gorulen:
            hatalar.append("kume iki kez dagitilmis (grup butunlugu): %s / %s" % (paket, eski))
            continue
        gorulen[anahtar] = yeni
        if yeni not in metinler:
            hatalar.append("bilinmeyen hedef pasaj: %s (%s / %s)" % (yeni, paket, eski))
            continue
        k = envanter[anahtar]
        m = metinler[yeni]
        m["kumeler"].append({
            "paket": k["paket"], "kod": k["kod"], "question_type": k["question_type"],
            "eski_passage_id": eski, "eski_group_id": k["group_id"],
            "kalem": k["kalem"], "numara": k["numara"],
            "numaralar": k["numaralar"], "numara_araligi": numara_araligi(k["numaralar"]),
        })
        m["kalem"] += k["kalem"]
        m["numara"] += k["numara"]
        m["paket_kalem"][k["kod"]] = m["paket_kalem"].get(k["kod"], 0) + k["kalem"]

    for anahtar in sorted(envanter):
        if anahtar not in gorulen:
            hatalar.append("dagitilmamis kume: %s / %s (%d kalem)"
                           % (anahtar[0], anahtar[1], envanter[anahtar]["kalem"]))

    # metin ici olcumler
    for m in metinler.values():
        m["kumeler"].sort(key=lambda x: (KOD_SIRA.index(x["kod"]), x["numaralar"][:1]))
        m["paket_sayisi"] = len(m["paket_kalem"])
        en_az, onerilen = paragraf_ihtiyaci(m["paket_kalem"])
        m["paragraf_en_az"] = en_az
        m["paragraf_onerilen"] = onerilen
        alt, ust = kelime_araligi(m["kalem"], m["module"])
        m["kelime_alt"], m["kelime_ust"] = alt, ust
        sa = m["paket_kalem"].get("SA", 0)
        serbest = onerilen - sa
        m["kisa_cevap_kalem"] = sa
        m["paragraf_basi_soru"] = round((m["kalem"] - sa) / float(serbest), 2) if serbest else None
        m["on_kosullar"] = on_kosullar(m["paket_kalem"], en_az, onerilen)
        m["sikisikliklar"] = sikisikliklar(m)
        # onerilen yeni grup kimlikleri (kisa cevapta ZORUNLU, digerlerinde oneri)
        m["onerilen_gruplar"] = []
        for kod in KOD_SIRA:
            kumeler = [c for c in m["kumeler"] if c["kod"] == kod]
            if not kumeler:
                continue
            nums = sorted(n for c in kumeler for n in c["numaralar"])
            m["onerilen_gruplar"].append({
                "kod": kod, "paket": kumeler[0]["paket"],
                "question_type": kumeler[0]["question_type"],
                "onerilen_group_id": "%s-%s" % (GROUP_ONEK[kod], m["passage_id"]),
                "kalem": sum(c["kalem"] for c in kumeler),
                "numara_araligi": numara_araligi(nums),
                "birlesen_kume_sayisi": len(kumeler),
                "yonerge_ilk_satiri": ("Question %s refers to Passage %s" if len(nums) == 1
                                        else "Questions %s refer to Passage %s")
                                       % (numara_araligi(nums), m["passage_id"]),
                "numaralar_bitisik": bitisik(nums),
            })

    return metinler, hatalar, uyarilar


def dogrula(envanter, metinler, hatalar, uyarilar):
    # 1) sayim korunumu
    kaynak_kalem = sum(k["kalem"] for k in envanter.values())
    kaynak_numara = sum(k["numara"] for k in envanter.values())
    hedef_kalem = sum(m["kalem"] for m in metinler.values())
    hedef_numara = sum(m["numara"] for m in metinler.values())
    if kaynak_kalem != hedef_kalem:
        hatalar.append("kalem sayisi degisti: kaynak %d -> hedef %d" % (kaynak_kalem, hedef_kalem))
    if kaynak_numara != hedef_numara:
        hatalar.append("numara sayisi degisti: kaynak %d -> hedef %d" % (kaynak_numara, hedef_numara))

    # paket bazinda korunum
    kaynak_paket, hedef_paket = {}, {}
    for k in envanter.values():
        kaynak_paket[k["kod"]] = kaynak_paket.get(k["kod"], 0) + k["kalem"]
    for m in metinler.values():
        for kod, n in m["paket_kalem"].items():
            hedef_paket[kod] = hedef_paket.get(kod, 0) + n
    for kod in sorted(set(list(kaynak_paket) + list(hedef_paket))):
        if kaynak_paket.get(kod, 0) != hedef_paket.get(kod, 0):
            hatalar.append("paket kalem sayisi degisti (%s): %d -> %d"
                           % (kod, kaynak_paket.get(kod, 0), hedef_paket.get(kod, 0)))

    # 2) metin basina butce
    for pid in [p["passage_id"] for p in YENI_PASAJLAR]:
        m = metinler[pid]
        if m["paket_sayisi"] > PAKET_UST:
            hatalar.append("%s: %d farkli paket (sinir %d)" % (pid, m["paket_sayisi"], PAKET_UST))
        if m["paragraf_en_az"] > PARAGRAF_UST:
            hatalar.append("%s: en az %d paragraf gerekiyor, ust sinir %d — yuk bu metne sigmiyor"
                           % (pid, m["paragraf_en_az"], PARAGRAF_UST))
        if m["paragraf_basi_soru"] is None:
            hatalar.append("%s: kisa cevabin tukettigi dokunulmamis paragraflar (%d) onerilen "
                           "paragraf sayisini (%d) bitiriyor — diger sorulara paragraf kalmiyor"
                           % (pid, m["kisa_cevap_kalem"], m["paragraf_onerilen"]))
        elif m["paragraf_basi_soru"] > SORU_PARAGRAF:
            hatalar.append("%s: paragraf basina %.2f soru (sinir %d)"
                           % (pid, m["paragraf_basi_soru"], SORU_PARAGRAF))
        if m["kalem"] > METIN_KALEM_HEDEF:
            uyarilar.append("%s: %d kalem — metin basina hedef ~%d asildi (paragraf butcesi hala "
                            "tutuyor: %d paragrafta paragraf basina %s soru)"
                            % (pid, m["kalem"], METIN_KALEM_HEDEF, m["paragraf_onerilen"],
                               yuk_metni(m["paragraf_basi_soru"])))
        if m["numara"] > METIN_KALEM_HEDEF and m["numara"] > m["kalem"]:
            uyarilar.append("%s: %d soru numarasi (kalem %d) — cift cevapli coktan secmeli "
                            "kalem numarayi kalemden fazla gosteriyor; cevap kagidinda %d satir"
                            % (pid, m["numara"], m["kalem"], m["numara"]))
        if m["paragraf_en_az"] == PARAGRAF_UST:
            uyarilar.append("%s: en az paragraf ihtiyaci ust sinira esit (%d) — paragraf payi yok"
                            % (pid, PARAGRAF_UST))
        for g in m["onerilen_gruplar"]:
            if not g["numaralar_bitisik"]:
                uyarilar.append("%s / %s: numaralar bitisik degil (%s) — paket dosyasinda kalem "
                                "sirasi yeniden duzenlenmeli" % (pid, g["kod"], g["numara_araligi"]))

    # 3) kisa cevap duzeni (plan 1.4)
    sa_toplam = 0
    for pid in [p["passage_id"] for p in YENI_PASAJLAR]:
        m = metinler[pid]
        sa = m["paket_kalem"].get("SA", 0)
        sa_toplam += sa
        if m["module"] == "academic" and sa not in (1, 2):
            hatalar.append("%s: kisa cevap %d kalem — akademik metin basina 1-2 olmali" % (pid, sa))
        if m["module"] == "general" and sa:
            hatalar.append("%s: GT metnine kisa cevap dusmus (%d kalem)" % (pid, sa))
    if sa_toplam != 10:
        hatalar.append("kisa cevap toplami %d (10 olmali)" % sa_toplam)

    # 4) bagli kararlar
    yerlesim = {(p, e): y for p, e, y in DAGITIM}
    for anahtar in GT_KAYNAKLI_KUMELER:
        if yerlesim.get(anahtar) != "G07":
            hatalar.append("GT kaynakli kume G07'ye gitmemis: %s / %s" % anahtar)
    for paket, eski, yeni in DAGITIM:
        if paket == "matching-sentence-endings.json" and yeni != MSE_HEDEF:
            hatalar.append("cumle sonu eslestirme grubu %s'e gitmemis: %s" % (MSE_HEDEF, eski))
        if paket == "diagram-labelling.json" and yeni != DL_HEDEF:
            hatalar.append("diyagram etiketleme kumesi %s'a gitmemis: %s" % (DL_HEDEF, eski))

    # 5) TFNG/YNNG ayni metinde mi (icerik uyarisi)
    for pid in [p["passage_id"] for p in YENI_PASAJLAR]:
        m = metinler[pid]
        if m["paket_kalem"].get("TFNG") and m["paket_kalem"].get("YNNG"):
            uyarilar.append("%s: TFNG ve YNNG ayni metinde — olgu/gorus ayrimi bulaniklasabilir" % pid)

    return {
        "kaynak_kalem": kaynak_kalem, "kaynak_numara": kaynak_numara,
        "hedef_kalem": hedef_kalem, "hedef_numara": hedef_numara,
        "paket_kalem_kaynak": kaynak_paket, "paket_kalem_hedef": hedef_paket,
    }


# ---------------------------------------------------------------------------
# rapor
# ---------------------------------------------------------------------------

def md_tablo(basliklar, satirlar):
    out = ["| " + " | ".join(str(b) for b in basliklar) + " |",
           "|" + "|".join(["---"] * len(basliklar)) + "|"]
    for s in satirlar:
        out.append("| " + " | ".join(str(x) for x in s) + " |")
    return "\n".join(out)


def icloud_kopyalari():
    dizin = ortak.yol("denetim")
    return sorted(a for a in os.listdir(dizin) if a.endswith(" 2.md"))


def rapor_yaz(veri, metinler, envanter):
    sira = [p["passage_id"] for p in YENI_PASAJLAR]
    kullanilan_kodlar = [k for k in KOD_SIRA
                         if any(metinler[p]["paket_kalem"].get(k) for p in sira)]
    md = []
    md.append("# B3 — 157 alistirma kaleminin 8 yeni pasaja dagitimi (FAZ 1.3 + 1.4)\n")
    md.append("Tarih: %s. Arac: `tools/b3-dagitim.py` (salt okunur; yalniz `denetim/` altina yazar).\n"
              % veri["olusturma_tarihi"])
    md.append("Girdi: `content/reading/practice/*.json` — **%d kalem / %d soru numarasi / %d paket** "
              "(`denetim/B3-ALISTIRMA-SAYIM.md` ile birebir).\n"
              % (veri["korunum"]["kaynak_kalem"], veri["korunum"]["kaynak_numara"],
                 len(PAKET_KOD)))
    md.append("Cikti: 7 akademik (`A13`-`A19`) + 1 General Training (`G07`) metnin **sartnamesi**. "
              "Metinler henuz yazilmadi; bu tablo yazimin girdisidir "
              "(`denetim/B3-pasaj-dagitimi.json`).\n")
    if veri["icloud_kopyalari_denetim"]:
        md.append("⚠️ `denetim/` altinda iCloud kopyasi var (okunmadi/yazilmadi): %s\n"
                  % ", ".join(veri["icloud_kopyalari_denetim"]))

    md.append("\n## 1. Metin x paket x kalem (capraz tablo)\n")
    satirlar = []
    for pid in sira:
        m = metinler[pid]
        satir = [pid] + [m["paket_kalem"].get(k, "") for k in kullanilan_kodlar]
        satir += ["**%d**" % m["kalem"], m["numara"], m["paket_sayisi"]]
        satirlar.append(satir)
    toplam_satir = ["**toplam**"]
    for k in kullanilan_kodlar:
        toplam_satir.append("**%d**" % sum(metinler[p]["paket_kalem"].get(k, 0) for p in sira))
    toplam_satir += ["**%d**" % veri["korunum"]["hedef_kalem"],
                     "**%d**" % veri["korunum"]["hedef_numara"], ""]
    satirlar.append(toplam_satir)
    md.append(md_tablo(["metin"] + kullanilan_kodlar + ["kalem", "numara", "paket"], satirlar))
    md.append("\nKisaltmalar: " + " · ".join("**%s** %s" % (k, KOD_AD[k]) for k in kullanilan_kodlar))

    md.append("\n\n## 2. Kume kume tasima haritasi\n")
    md.append("Grup butunlugu korunur: bir kume (paket + eski pasaj) tek bir yeni pasaja gider, "
              "bolunmez. Numaralar degismez (`number` sabit) — asagidaki araliklar yeni metinde "
              "de ayni.\n")
    satirlar = []
    for pid in sira:
        for c in metinler[pid]["kumeler"]:
            satirlar.append([pid, c["kod"], c["paket"], c["eski_passage_id"],
                             c["eski_group_id"] or "—", c["kalem"], c["numara_araligi"]])
    md.append(md_tablo(["yeni metin", "tip", "paket", "eski pasaj", "eski group_id",
                        "kalem", "numara"], satirlar))

    md.append("\n## 3. Metin metin sartname\n")
    for pid in sira:
        m = metinler[pid]
        md.append("\n### %s — %s\n" % (pid, m["konu"]))
        md.append("- **Modul:** %s%s · **kelime:** %d-%d · **paragraf:** en az %d, onerilen %d "
                  "(ust sinir %d)"
                  % (m["module"], "" if m["section"] is None else " (bolum %d)" % m["section"],
                     m["kelime_alt"], m["kelime_ust"], m["paragraf_en_az"],
                     m["paragraf_onerilen"], PARAGRAF_UST))
        md.append("- **Yuk:** %d kalem / %d numara, %d farkli paket (sinir %d) — paragraf basina "
                  "%s soru (sinir %d)"
                  % (m["kalem"], m["numara"], m["paket_sayisi"], PAKET_UST,
                     yuk_metni(m["paragraf_basi_soru"]), SORU_PARAGRAF))
        md.append("- **Tasidigi tipler:** " + ", ".join(
            "%s (%s) %d kalem" % (KOD_AD[g["kod"]], g["kod"], g["kalem"])
            for g in m["onerilen_gruplar"]))
        md.append("- **Konu:** %s" % m["konu_ozeti"])
        md.append("- **Kaynak:** %s · yedek: %s" % (m["kaynak"], m["kaynak_yedegi"]))
        md.append("- **Konu cakismasi:** en yakin mevcut metin: %s. %s"
                  % (m["en_yakin_mevcut"], m["ayrim"]))
        md.append("\n**Metnin saglamasi gereken on kosullar:**\n")
        for o in m["on_kosullar"]:
            md.append("- %s  _(%s)_" % (o["kosul"], o["kaynak"]))
        md.append("\n**Yeni grup yapisi** (yonerge satiri yeni pasaj kimligini soyleyecek; "
                  "`passage_id` kalem veya grup duzeyinde yazilacak — `PLAN-EK-kurallar.md` 6):\n")
        md.append(md_tablo(
            ["onerilen group_id", "paket", "question_type", "kalem", "numara", "yonerge ilk satiri"],
            [[g["onerilen_group_id"], g["paket"], g["question_type"], g["kalem"],
              g["numara_araligi"], "`%s`" % g["yonerge_ilk_satiri"]]
             for g in m["onerilen_gruplar"]]))

    md.append("\n## 4. Butce dogrulamasi\n")
    md.append("Kurallar: metin basina en cok **%d farkli paket** (sert), hedef **~%d kalem** "
              "(yumusak), **paragraf basina en cok %d soru**, **kanit cumlesi basina en cok %d "
              "soru**, kisa cevabin her kalemi **dokunulmamis** bir paragraf tuketir.\n"
              % (PAKET_UST, METIN_KALEM_HEDEF, SORU_PARAGRAF, KANIT_SORU))
    satirlar = []
    for pid in sira:
        m = metinler[pid]
        satirlar.append([
            pid, m["kalem"], "OK" if m["kalem"] <= METIN_KALEM_HEDEF else "⚠️ %d" % m["kalem"],
            m["paket_sayisi"], "OK" if m["paket_sayisi"] <= PAKET_UST else "HATA",
            "%d/%d" % (m["paragraf_en_az"], m["paragraf_onerilen"]),
            yuk_metni(m["paragraf_basi_soru"]),
            "OK" if (m["paragraf_basi_soru"] is not None
                     and m["paragraf_basi_soru"] <= SORU_PARAGRAF) else "HATA",
            m["kisa_cevap_kalem"], m["kalem"],
        ])
    md.append(md_tablo(["metin", "kalem", "kalem <= %d" % METIN_KALEM_HEDEF, "paket",
                        "paket <= %d" % PAKET_UST, "paragraf en az/onerilen",
                        "paragraf basi soru", "yogunluk", "kisa cevap (serbest paragraf)",
                        "gereken ayri kanit cumlesi"], satirlar))

    md.append("\n### Korunum\n")
    md.append(md_tablo(
        ["olcu", "kaynak", "hedef", "durum"],
        [["kalem", veri["korunum"]["kaynak_kalem"], veri["korunum"]["hedef_kalem"],
          "OK" if veri["korunum"]["kaynak_kalem"] == veri["korunum"]["hedef_kalem"] else "HATA"],
         ["soru numarasi", veri["korunum"]["kaynak_numara"], veri["korunum"]["hedef_numara"],
          "OK" if veri["korunum"]["kaynak_numara"] == veri["korunum"]["hedef_numara"] else "HATA"]]))
    md.append("")
    md.append(md_tablo(
        ["paket", "kaynak kalem", "hedef kalem", "durum"],
        [[KOD_AD[k] + " (" + k + ")", veri["korunum"]["paket_kalem_kaynak"].get(k, 0),
          veri["korunum"]["paket_kalem_hedef"].get(k, 0),
          "OK" if veri["korunum"]["paket_kalem_kaynak"].get(k, 0)
                  == veri["korunum"]["paket_kalem_hedef"].get(k, 0) else "HATA"]
         for k in KOD_SIRA]))

    md.append("\n### Hatalar / uyarilar\n")
    if veri["hatalar"]:
        for h in veri["hatalar"]:
            md.append("- 🔴 %s" % h)
    else:
        md.append("- Sert kural ihlali **yok** (kume ortusmesi, sayim korunumu, paket cesidi, "
                  "paragraf butcesi, kisa cevap duzeni, bagli kararlar).")
    md.append("")
    if veri["uyarilar"]:
        for u in veri["uyarilar"]:
            md.append("- ⚠️ %s" % u)
    else:
        md.append("- Uyari yok.")

    md.append("\n### Sikisan noktalar (kural ihlali degil, yazimda pay yok)\n")
    satirlar = [[pid, s] for pid in sira for s in metinler[pid]["sikisikliklar"]]
    if satirlar:
        md.append(md_tablo(["metin", "sikisiklik"], satirlar))
    else:
        md.append("(yok)")

    md.append("\n## 5. Konu onerileri ve izinli kaynak\n")
    md.append("Mevcut 18 metnin konulari (plan 1.2/1 yasak listesi): hayvan davranisi x3, "
              "iklim/jeoloji/okyanus x2, uzay x1, tarih/arkeoloji x2, toplum/is x2, "
              "saglik/davranis x2; GT: sehir hizmetleri, bos zaman, personel el kitabi, staj, "
              "gida israfi, gonulluluk. Asagidaki onerilerin hicbiri bu alt konulara degmiyor.\n")
    md.append(md_tablo(
        ["metin", "onerilen alan", "izinli kaynak", "yedek kaynak", "en yakin mevcut metin", "ayrim"],
        [[pid, metinler[pid]["konu"], metinler[pid]["kaynak"], metinler[pid]["kaynak_yedegi"],
          metinler[pid]["en_yakin_mevcut"], metinler[pid]["ayrim"]] for pid in sira]))
    md.append("\nKaynak kurali (`prompts/01-pasaj-secimi.md`): yalniz **PLOS · NASA/NOAA/USGS · "
              "OpenStax**; CC BY / kamu mali; Wikipedia ve The Conversation yasak. Somut sayilar "
              "metnin kendi calismasinin sectigi degerler olacak (`PLAN-EK-kurallar.md` 4).\n")

    md.append("\n## 6. Yontem ve sinirlar\n")
    md.append("- \"Kume\" = (paket dosyasi, eski `passage_id`). Duz `items` tasiyan 9 pakette "
              "grup alani yok; kume, ayni pasaja capali kalemlerin olusturdugu ortuk gruptur.\n"
              "- Paragraf sayilari **tahmin degil turetim**: yogunluk (paragraf basina en cok %d "
              "soru) + kisa cevabin tukettigi dokunulmamis paragraflar + baslik/bilgi "
              "eslestirmenin ayri paragraf ihtiyaci + 7-10 paragraf tabani.\n"
              "- Kanit cumlesi sayisi kalem sayisina esit alindi (cumle basina en cok %d soru); "
              "700-900 kelimelik bir metinde ~40-50 cumle olur, en agir metin bunun ~%d%%'ini "
              "kullanir.\n"
              "- Numaralar (`number`) degismiyor; bu yuzden bir metne dusen kumelerin numaralari "
              "bitisik olacak sekilde secildi — paket dosyasi icinde kalem sirasi bozulmuyor.\n"
              "- Arac hicbir icerik dosyasini degistirmedi; `content/` altina yazmiyor."
              % (SORU_PARAGRAF, KANIT_SORU,
                 int(round(100.0 * max(metinler[p]["kalem"] for p in sira) / 45))))

    with open(ortak.yol("denetim", "B3-pasaj-dagitimi.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")


def main():
    envanter = kume_envanter()
    metinler, hatalar, uyarilar = dagit(envanter)
    korunum = dogrula(envanter, metinler, hatalar, uyarilar)

    sira = [p["passage_id"] for p in YENI_PASAJLAR]
    veri = {
        "olusturma_tarihi": datetime.date.today().isoformat(),
        "arac": "tools/b3-dagitim.py",
        "kaynak": "content/reading/practice/*.json",
        "butce": {
            "paragraf_basi_soru": SORU_PARAGRAF, "kanit_cumlesi_basi_soru": KANIT_SORU,
            "metin_basi_kalem_hedefi": METIN_KALEM_HEDEF, "metin_basi_paket_ust": PAKET_UST,
            "paragraf_alt": PARAGRAF_ALT, "paragraf_ust": PARAGRAF_UST,
        },
        "korunum": korunum,
        "hatalar": hatalar,
        "uyarilar": uyarilar,
        "kaynak_kumeler": [
            {"paket": k["paket"], "kod": k["kod"], "eski_passage_id": k["eski_passage_id"],
             "question_type": k["question_type"], "eski_group_id": k["group_id"],
             "kalem": k["kalem"], "numara": k["numara"],
             "numara_araligi": numara_araligi(k["numaralar"])}
            for _, k in sorted(envanter.items())
        ],
        "metinler": [metinler[p] for p in sira],
        "icloud_kopyalari_denetim": icloud_kopyalari(),
    }

    ortak.yaz("denetim/B3-pasaj-dagitimi.json", veri)
    rapor_yaz(veri, metinler, envanter)

    print("kaynak: %d kume / %d kalem / %d numara"
          % (len(envanter), korunum["kaynak_kalem"], korunum["kaynak_numara"]))
    for pid in sira:
        m = metinler[pid]
        print("  %s  %2d kalem / %2d numara | %d paket | paragraf %d-%d | par.basi %s | %s"
              % (pid, m["kalem"], m["numara"], m["paket_sayisi"], m["paragraf_en_az"],
                 m["paragraf_onerilen"], yuk_metni(m["paragraf_basi_soru"]),
                 ",".join("%s%d" % (k, m["paket_kalem"][k])
                          for k in KOD_SIRA if m["paket_kalem"].get(k))))
    print("hedef toplam: %d kalem / %d numara" % (korunum["hedef_kalem"], korunum["hedef_numara"]))
    print("hata: %d | uyari: %d" % (len(hatalar), len(uyarilar)))
    for h in hatalar:
        print("  HATA: %s" % h)
    for u in uyarilar:
        print("  uyari: %s" % u)
    print("yazildi: denetim/B3-pasaj-dagitimi.md + denetim/B3-pasaj-dagitimi.json")
    return 1 if hatalar else 0


if __name__ == "__main__":
    sys.exit(main())
