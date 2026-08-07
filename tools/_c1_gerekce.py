# -*- coding: utf-8 -*-
"""Ornek cevap kutuphanesinin yazma yarisi icin dorduncu duzey denetim: GEREKCE - KANIT.

Onceki uc denetim cevabin kendisine bakiyordu:
  1. duzey (sema)   - gecerli JSON, band uclusu, zorunlu alanlar, kelime sayisi
  2. duzey (gorev)  - `tools/_c1_denetim.py`; cevap gorevle tutarli mi, sayilar dogru mu
  3. duzey (ayrim)  - `tools/_c1_ayrim.py`; cevap hedefledigi bandin izlerini tasiyor mu

Hicbiri `why_this_band` ve `what_would_lift_it` alanlarina bakmiyordu. Oysa kullaniciya
"band 7 boyle yazar" diyen sey cevabin kendisi kadar **onun altindaki gerekce**; gerekce
metinde olmayan bir sey soyluyorsa ornek yanlis seyi ogretir. Uygulamanin puanlama
talimati bunu zaten kural yapmis (`degerlendirme/ORTAK-KURALLAR.md`, BLOCK G):

    "`quote` is a verbatim span of 3-25 words copied exactly from the candidate's
     response. Copy the errors too - do not tidy the spelling, capitalisation or
     grammar of a quote."

Kutuphanenin gerekceleri Turkce yazilmis ama ayni isi yapiyor: iclerinde cevaptan
alinmis Ingilizce parcalar var. Bu script o parcalari cikarip metinle karsilastiriyor.

  A  KANIT     gerekcedeki alinti cevabin kendi metninde bire bir var mi
  B  CAPRAZ    alinti baska bir bandin metninden mi gelmis (A'nin agir hali)
  C  YOKLUK    "su sozcuk hic gecmiyor" denen sey gercekten gecmiyor mu
  D  MERDIVEN  band 5'in "sunu yap" onerisi bir ust bandin metninde karsilik buluyor mu
  E  TAVAN     band 8 kusursuz ilan edilmis mi (prompt: "kusursuz degil - band 9 degil")
  F  TEKRAR    gerekce cumleleri cevaplar arasinda kopyala-yapistir mi
  G  CERCEVE   gerekce cevap yerine kisi/sinav hakkinda konusuyor mu (BLOCK I)
  H  TEMEL     band 5 / 6,5 dilbilgisi gerekcesi en az bir gercek hata ornegi veriyor mu

Alinti cikarma nasil calisiyor: Turkce gerekce icinde, cevap metinlerinden kurulan
Ingilizce sozlukte gecen ardisik tokenler bir aday alinti sayiliyor; noktalama alinti
sinirini kesiyor ("Firstly / Secondly" iki ayri alintidir, tek bir alinti degil).
Aday alintinin cevresindeki Turkce ipuclari alintinin ne iddia ettigini soyluyor:
"...yok", "...hic gecmiyor" ise YOKLUK; "...yerine ... kullanmak" ise ONERI; digerleri
KANIT. Cikarim kalip tabanli, dolayisiyla kordur: bulgu = mutlaka elle okunacak aday,
otomatik hata degil. (3. duzey denetimin dersi: once olcuden suphelen, metni oku.)

Hicbir dosyayi degistirmez. Bulgu varsa cikis 1.
"""

import json
import os
import re
import sys
from collections import Counter, defaultdict

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CEVAP = os.path.join(KOK, "content", "ornek-cevaplar", "writing")

BANTLAR = (5.0, 6.5, 8.0)
OLCUTLER = ("task_response", "coherence_cohesion", "lexical_resource",
            "grammatical_range_accuracy")

# Gerekce Turkce yazildigi icin bazi Turkce sozcukler Ingilizce sozlukle cakisiyor
# ("her", "son", "once", "sure", "not", "plan"). Bunlar alinti baslangici sayilmaz.
TR_CAKISMA = set("""
her son once sure not an am on o de da ne en il bir ve bu tam kim el ay yer alan iki
mi mu dur ama tek yok var ile plan format kadar ise ile plan
""".split())

# Puanlama talimatinin kendi terimleri; gerekcede alinti degil, olcut adidir.
TERIM = set("""
past present perfect continuous simple passive position task response coherence cohesion
lexical resource grammatical range accuracy band
""".split())

TERIM_IKILI = ("past perfect", "present perfect", "present continuous", "past simple",
               "present simple", "past continuous")

# Iki ayri ipucu kumesi, cunku iki karar farkli yonde yaniliyor:
#
# GEVSEK kume A/B bulgusunu BASTIRMAK icin. Cumlede "yerine", "sinirli", "yok" gibi bir
#   sey geciyorsa alinti kanit olmayabilir; bastirmanin bedeli bir kacirilmis bulgu,
#   bastirmamanin bedeli yuzlerce yanlis alarm.
# SIKI kume C bulgusunu URETMEK icin. Ilk yazimda gevsek kume C icin de kullanildi ve
#   238 yanlis alarm cikti: "go up, go down ile SINIRLI" cumlesi bu ogelerin metinde
#   OLDUGUNU soyluyor, olmadigini degil. "tekrar edilmiyor" da yokluk degildir - oge
#   geciyor ama tekrarlanmiyor demektir. C yalnizca acik yokluk fiiline bakar.
YOKLUK_IPUCU = ("yok", "yoktur", "gecmiyor", "girmiyor", "gecmez", "kullanilmiyor",
                "edilmiyor", "cikmiyor", "gormuyor", "bulunmuyor", "hic", "degil",
                "olmadan", "eksik", "yerine", "olmasa", "disinda", "disina", "sinirli",
                "indirgenmis", "yalnizca", "sadece", "kaliyor", "kalmis")
YOKLUK_SIKI = (r"\bhic (gecmiyor|girmiyor|kullanilmiyor|yok)\b", r"\bgibi [\w ]{0,30}yok\b",
               r"\bgecmiyor\b", r"\bgirmiyor\b", r"\byer almiyor\b", r"\bhic yok\b")
ONERI_IPUCU = ("koymak", "yapmak", "kullanmak", "gecmek", "eklemek", "yazmak", "cevirmek",
               "tasimak", "birlestirmek", "acmak", "baglamak", "olur", "olurdu", "tasir",
               "toparlar", "duzeltir", "oturtur", "gerekir", "daha uygun", "yeterdi",
               "kazandirir", "kesinlestirir", "getirir")

TOKEN = re.compile(r"[A-Za-z][A-Za-z']*")

# Ingilizce kapali sinif sozcukleri: bunlar Turkce metinde gecmez, dolayisiyla bir
# dizinin Ingilizce oldugunun kesin isaretidir. Sozlukte bulunmayan sozcukleri bir
# alintinin icine ancak bunlardan biri varsa aliyoruz (asagida ISLEV_SOZCUK kullanimi).
ISLEV_SOZCUK = set("""
the a an of in on to is are was were be been and or but that which who whom whose for
with from by as at it its this these those their his her they we you he she i not no
more most than there here have has had do does did will would can could should
""".split())

bulgular = []
gozlemler = []


def bulgu(kod, tur, mesaj):
    bulgular.append((kod, tur, mesaj))


def oku(yol):
    with open(yol, encoding="utf-8") as f:
        return json.load(f)


def duzelt_tirnak(s):
    """Tipografik tirnak/kisa cizgi farki alinti karsilastirmasini bozmasin."""
    return (s.replace("‘", "'").replace("’", "'")
             .replace("“", '"').replace("”", '"')
             .replace("–", "-").replace("—", "-"))


def normalize(s):
    """Karsilastirma bicimi: kucuk harf, noktalama bosluk, tek bosluk, bas/son bosluk."""
    s = duzelt_tirnak(s).lower()
    return " " + re.sub(r"[^a-z0-9%]+", " ", s).strip() + " "


def sozluk_kur(kutuphane):
    """Ingilizce sozluk cevaplarin kendisinden kuruluyor - disaridan liste yok."""
    v = set()
    for d in kutuphane.values():
        for a in d["answers"]:
            v.update(t.lower() for t in TOKEN.findall(duzelt_tirnak(a["text"])))
    return v


def turkce_sozluk(kutuphane, sozluk):
    """Gerekcelerde gecip cevap metinlerinde hic gecmeyen, yani Turkce olan sozcukler.

    Uc ya da daha fazla ayri cevabin gerekcesinde geciyorsa Turkce sayiliyor. Tek bir
    yerde gecen ve sozlukte olmayan sozcuk Turkce degil de UYDURMA BIR ALINTI olabilir -
    ayirim tam olarak buradan geliyor (mutasyon testi 1: "a sharp escalation" gibi,
    kutuphanede hic gecmeyen sozcuklerden kurulmus sahte alinti ilk surumde gorunmez
    kaliyordu, cunku sozluk kutuphanenin kendisinden kuruluyor).
    """
    nerede = defaultdict(set)
    for kod, d in kutuphane.items():
        for a in d["answers"]:
            metinler = list(a["why_this_band"].values()) + [a["what_would_lift_it"]]
            for v in metinler:
                for t in TOKEN.findall(duzelt_tirnak(v)):
                    low = t.lower()
                    if low not in sozluk:
                        nerede[low].add((kod, a["band"]))
    return set(k for k, v in nerede.items() if len(v) >= 3)


def alintilar(metin, sozluk, turkce):
    """Turkce gerekce icindeki ardisik Ingilizce token dizileri (aday alintilar).

    Token uc sinifa ayriliyor: EN (cevap metinlerinin sozlugunde), TR (Turkce sozlukte
    ya da cakisma listesinde), BILINMEYEN (ikisinde de yok). Dizi EN ve BILINMEYEN
    tokenlerden kurulabilir, TR token diziyi keser; noktalama da keser. BILINMEYEN
    token iceren dizi ancak icinde bir Ingilizce islev sozcugu varsa alinti sayilir.
    """
    metin = duzelt_tirnak(metin)
    toklar = [(m.group(0), m.start(), m.end()) for m in TOKEN.finditer(metin)]
    diziler, cur, onceki = [], [], None
    for t, s, e in toklar:
        bosluk = metin[onceki:s] if onceki is not None else ""
        kesik = bool(re.search(r"[^\sA-Za-z'\-]", bosluk))
        low = t.lower()
        if low in TR_CAKISMA or low in turkce:
            sinif = "TR"
        elif low in sozluk:
            sinif = "EN"
        else:
            sinif = "BILINMEYEN"
        if sinif == "TR":
            if cur:
                diziler.append(cur)
            cur = []
        elif kesik:
            if cur:
                diziler.append(cur)
            cur = [(t, s, e, sinif)]
        else:
            cur.append((t, s, e, sinif))
        onceki = e
    if cur:
        diziler.append(cur)

    adaylar = []
    for c in diziler:
        siniflar = [x[3] for x in c]
        if "EN" not in siniflar:
            continue
        if "BILINMEYEN" not in siniflar:
            adaylar.append(c)
            continue
        icerik = [x for x in c if x[3] == "EN" and x[0].lower() not in ISLEV_SOZCUK]
        if not icerik:
            # Taninan tek sey islev sozcugu ("a sharp escalation"): icerik sozcuklerinin
            # hicbiri kutuphanede gecmiyor. Uydurma alintinin imzasi budur, dizi
            # bolunmeden oldugu gibi sinaniyor. Tek bilinmeyen sozcuk yetmez: Turkce
            # "is baglamina" ikilisi de bu bicimde gorunuyor ("is" Ingilizce "is" ile
            # cakisiyor), oysa uydurma alinti en az iki taninmayan sozcuk getirir.
            if sum(1 for x in c if x[3] == "BILINMEYEN") >= 2:
                adaylar.append(c)
            continue
        # Aksi halde bilinmeyenler buyuk olasilikla nadir Turkce sozcukler ("kalibiyla",
        # "ogeleri"); dizi onlardan bolunuyor ve parcalar ayri ayri sinaniyor.
        parca_dizi = []
        for x in c:
            if x[3] == "BILINMEYEN":
                if parca_dizi:
                    adaylar.append(parca_dizi)
                parca_dizi = []
            else:
                parca_dizi.append(x)
        if parca_dizi:
            adaylar.append(parca_dizi)

    out = []
    for c in adaylar:
        parca = " ".join(x[0] for x in c)
        if len(c) == 1 and len(c[0][0]) < 4:
            continue                       # tek harfli/kisa token alinti sayilmaz
        if parca.lower() in TERIM_IKILI:
            continue                       # "past perfect" olcut dili, alinti degil
        if len(c) == 1 and parca.lower() in TERIM:
            continue
        out.append((parca, c[0][1], c[-1][2]))
    return out


def baglam_turu(metin, bas, son, alan):
    """Alinti ne iddia ediyor: KANIT mi, YOKLUK mu, ONERI mi.

    Karar alintinin icinde bulundugu cumleye bakilarak veriliyor; "yerine", "hic
    gecmiyor", "... yok" gibi ipuclari alintiyi kanit olmaktan cikariyor.
    """
    metin = duzelt_tirnak(metin)
    nokta_once = max(metin.rfind(".", 0, bas), metin.rfind(";", 0, bas)) + 1
    # Cumle sonu noktali virgulle de biter: "bill, line ile sinirli; refund hic girmiyor"
    # tek cumle sayilirsa yokluk iddiasi ilk yarinin alintilarina da bulasir (ilk
    # yazimda oyle oldu, dokuz yanlis alarm).
    adaylar = [i for i in (metin.find(".", son), metin.find(";", son)) if i != -1]
    nokta_sonra = min(adaylar) if adaylar else len(metin)
    cumle = metin[nokta_once:nokta_sonra].lower()
    sonrasi = metin[son:nokta_sonra].lower()
    # "bus, very, problem tekrar ediyor VE resmi mektup kaliplari hic yok" - yokluk
    # iddiasi baglactan sonraki oge icin gecerli, alintinin kendisi icin degil.
    for baglac in (" ve ", " ama ", " ancak ", " oysa "):
        if baglac in sonrasi:
            sonrasi = sonrasi.split(baglac)[0]
    if any(re.search(p, sonrasi) for p in YOKLUK_SIKI) and "yerine" not in sonrasi:
        return "YOKLUK"                    # acik yokluk iddiasi, alintidan sonra
    if alan == "lift":
        return "ONERI"
    if any(ip in cumle for ip in ONERI_IPUCU):
        return "BELIRSIZ"
    if any(re.search(r"\b%s\b" % ip, cumle) for ip in YOKLUK_IPUCU):
        return "BELIRSIZ"                  # kanit mi yokluk mu ayirt edilemiyor: bastir
    return "KANIT"


def cekimli_var_mi(parca, metin):
    """Alinti metinde cekim eki farkiyla geciyor mu: "store" ~ "stored", "collect" ~
    "collected", "arrangement" ~ "arrangements".

    Sozcuk alani sayan bir gerekce ("collect, store, distribute gibi ogeler var")
    ogeyi sozluk bicimiyle yazar, metinde ise cekimli hali gecer. Bu bir uydurma
    kanit degil, bicim farkidir; bulgu degil gozlem olarak raporlanir.
    """
    parcalar = [re.escape(t.lower()) for t in TOKEN.findall(parca)]
    if not parcalar:
        return False
    kalip = r"\W+".join(p + r"(?:s|es|d|ed|ing|ly)?" for p in parcalar)
    return re.search(r"\b%s\b" % kalip, metin.lower()) is not None


def cumleler(s):
    return [c.strip() for c in re.split(r"(?<=[.!?])\s+", s.strip()) if c.strip()]


def main():
    # Mutasyon testi bozulmus bir kopyayi denetleyebilsin diye klasor disaridan verilebilir.
    klasor = sys.argv[1] if len(sys.argv) > 1 else CEVAP
    dosyalar = sorted(f for f in os.listdir(klasor) if f.endswith(".json"))
    kutuphane = {}
    for f in dosyalar:
        kutuphane[f[:-5]] = oku(os.path.join(klasor, f))
    sozluk = sozluk_kur(kutuphane)
    turkce = turkce_sozluk(kutuphane, sozluk)

    sayac = Counter()
    merdiven = Counter()
    cumle_havuzu = defaultdict(list)

    for kod, d in sorted(kutuphane.items()):
        cevaplar = {a["band"]: a for a in d["answers"]}
        metinler = {b: normalize(cevaplar[b]["text"]) for b in cevaplar}

        for band in sorted(cevaplar):
            a = cevaplar[band]
            kendi = metinler[band]
            alanlar = [(k, a["why_this_band"][k]) for k in OLCUTLER]
            alanlar.append(("lift", a["what_would_lift_it"]))

            # --- H: alt bandlarda dilbilgisi gerekcesi hatayi gostermeli.
            # "Kalan hatalar okuru durdurmuyor" gibi bir cumle ogrenciye neyi
            # duzeltecegini soylemez; band 8'de gosterilecek hata olmayabilir, band
            # 5 ve 6,5'te vardir.
            if band < 8.0:
                gra = a["why_this_band"]["grammatical_range_accuracy"]
                if not any((" " + normalize(p).strip() + " ") in kendi
                           for p, _, _ in alintilar(gra, sozluk, turkce)):
                    bulgu(kod, "H", "band %s dilbilgisi gerekcesi metinden tek bir hata "
                                    "ornegi vermiyor" % band)

            for alan, deger in alanlar:
                # --- F: gerekce cumlesi baska bir cevapta aynen tekrar ediyor mu
                for c in cumleler(deger):
                    if len(c.split()) >= 6:
                        cumle_havuzu[normalize(c).strip()].append((kod, band, alan))

                # --- G: cerceve (BLOCK I) - kisi / gercek sinav / kesinlik dili
                dusuk = deger.lower()
                for kalip in ("sinavda", "sinavi", "ogrenci", "adayin", "kesinlikle",
                              "garanti", "resmi sonuc", "alacak", "alir "):
                    if kalip in dusuk:
                        bulgu(kod, "G", "band %s %s: cevap yerine kisi/sinav dili (%r)"
                              % (band, alan, kalip))

                for parca, bas, son in alintilar(deger, sozluk, turkce):
                    tur = baglam_turu(deger, bas, son, alan)
                    n = normalize(parca).strip()
                    icinde = (" " + n + " ") in kendi
                    baska = [b for b in metinler if b != band and (" " + n + " ") in metinler[b]]
                    sayac[tur] += 1

                    if tur == "KANIT" and not icinde:
                        if cekimli_var_mi(parca, a["text"]):
                            gozlemler.append((kod, band, parca, "cekim farki"))
                        elif baska:
                            bulgu(kod, "B", "band %s %s: %r alintisi bu cevapta yok, "
                                            "band %s metninde var (capraz kanit)"
                                  % (band, alan, parca,
                                     "/".join(str(x) for x in sorted(baska))))
                        else:
                            bulgu(kod, "A", "band %s %s: %r alintisi metinde bire bir yok"
                                  % (band, alan, parca))
                    elif tur == "YOKLUK" and icinde:
                        bulgu(kod, "C", "band %s %s: %r yok deniyor ama metinde var"
                              % (band, alan, parca))
                    elif tur == "ONERI" and alan == "lift" and band < 8.0 and not icinde:
                        # D olcumdur, bulgu degil: oneri zaten cevapta gecen bir cumleyi
                        # ("su cumleyi ikiye bol") gosteriyor olabilir, kalip bunu
                        # onerilen yeni bicimden ayiramaz. Ust bandda karsilik bulan
                        # oneri merdivenin isledigini gosterir.
                        ust = [b for b in baska if b > band]
                        merdiven["karsiligi var" if ust else "ust bandda yok"] += 1
                        if ust:
                            gozlemler.append((kod, band, parca, "band %s metninde var"
                                              % "/".join(str(x) for x in sorted(ust))))

            # --- E: tavan (band 8 kusursuz ilan edilmemeli)
            if band == 8.0:
                hepsi = " ".join(a["why_this_band"].values()).lower()
                # "cumlelerin buyuk cogunlugu hatasiz" band 8'in kendi tarifidir, iddia
                # degil; ilk yazimda yalin "hatasiz" arandi ve AT04 haksiz yere isaretlendi.
                # Yalnizca mutlak ifadeler bulgu: tamamen/butun/hicbir ile kurulanlar.
                for kalip in (r"tamamen hatasiz", r"butun cumleler hatasiz", r"kusursuz",
                              r"mukemmel", r"hicbir hata yok", r"hata yok\b"):
                    if re.search(kalip, hepsi):
                        bulgu(kod, "E", "band 8 gerekcesi kusursuzluk iddia ediyor (%r)" % kalip)
                lift = a["what_would_lift_it"].strip()
                if len(lift.split()) < 6:
                    bulgu(kod, "E", "band 8 what_would_lift_it fazla kisa/bos: %r" % lift)
                for kalip in ("yapilacak bir sey yok", "gelistirilecek", "hicbir sey"):
                    if kalip in lift.lower():
                        bulgu(kod, "E", "band 8 what_would_lift_it somut adim vermiyor")

    # --- F: havuzda birden fazla yere dusen gerekce cumleleri
    for c, yerler in sorted(cumle_havuzu.items()):
        if len(yerler) > 1:
            bulgu(yerler[0][0], "F", "gerekce cumlesi %d cevapta aynen tekrar ediyor (%s): %r"
                  % (len(yerler), ", ".join("%s/%s" % (k, b) for k, b, _ in yerler), c[:70]))

    # --- ozet ---------------------------------------------------------------
    print("Denetlenen gorev: %d  (cevap: %d, gerekce alani: %d)"
          % (len(kutuphane), 3 * len(kutuphane), 15 * len(kutuphane)))
    print()
    print("Cikarilan alinti: %d" % sum(sayac.values()))
    for t in ("KANIT", "YOKLUK", "ONERI", "BELIRSIZ"):
        print("  %-8s %4d" % (t, sayac[t]))
    print()
    print("Merdiven (band 5/6,5 onerisinin ust bandda karsiligi):")
    for k in sorted(merdiven):
        print("  %-16s %3d" % (k, merdiven[k]))
    print()
    print("Tekrar eden gerekce cumlesi (>=6 sozcuk): %d"
          % sum(1 for y in cumle_havuzu.values() if len(y) > 1))

    if gozlemler:
        print()
        print("Gozlem (bulgu degil):")
        for kod, band, parca, ne in gozlemler:
            print("  %-8s band %-4s %-45r %s" % (kod, band, parca, ne))

    print()
    if not bulgular:
        print("BULGU YOK - sekiz gerekce denetiminin hepsi temiz.")
    else:
        print("BULGU: %d" % len(bulgular))
        for kod, tur, mesaj in bulgular:
            print("  [%s] %-8s %s" % (tur, kod, mesaj))
    return 1 if bulgular else 0


if __name__ == "__main__":
    sys.exit(main())
