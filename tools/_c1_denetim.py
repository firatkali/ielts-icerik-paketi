# -*- coding: utf-8 -*-
"""Ornek cevap kutuphanesinin yazma yarisi icin ikinci duzey denetim.

1. calistirma sema/kelime sayisi denetimini yapmisti (gecerli JSON, band uclusu,
task_ref-dosya adi uyumu, zorunlu alanlar, kelime sayisi). Bu script onun uzerine
cikip cevabin **gorevle** iliskisini olcuyor:

  A  task_ref havuzdaki gerçek gorev dosyasina cozunuyor mu, tur/modul tutuyor mu
  B  kelime sayisi gorevin kendi `min_words` degerinin uzerinde mi (sabit 150/250 degil)
  C  `why_this_band` dort alani ve `what_would_lift_it` prompt'un koydugu "<=2 cumle"
     sinirinda mi
  D  cevap gercekten o gorevden mi bahsediyor (gorevin ozel adlari / anahtar terimleri
     metinde geciyor mu) - yanlis eslesmis dosya yakalamak icin
  E  Academic Task 1 cevaplarindaki sayilar `visual` verisiyle uyusuyor mu
     (5. grupta AT07'de elle bulunan turden veri hatasi sistematik taransin diye)
  F  dosyalar arasi kopyala-yapistir (ayni cumle iki ayri gorevde)
  G  KONTROL.md 30 gorevin hepsini satirlariyla kapsiyor mu

Cikti: ekrana ozet + bulgu listesi. Hicbir dosyayi degistirmez.
"""

import json
import os
import re
import sys
from collections import defaultdict

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CEVAP = os.path.join(KOK, "content", "ornek-cevaplar", "writing")
HAVUZ = os.path.join(KOK, "content", "writing")
KONTROL = os.path.join(KOK, "content", "ornek-cevaplar", "KONTROL.md")

bulgular = []


def bulgu(dosya, tur, mesaj):
    bulgular.append((dosya, tur, mesaj))


def oku(yol):
    with open(yol, encoding="utf-8") as f:
        return json.load(f)


def gorev_havuzu():
    """set_id -> (yol, veri) ."""
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


def kelime_say(m):
    return len(re.findall(r"[A-Za-z0-9'’-]+", m))


def cumle_say(m):
    """Cumle sayar. Aciklama metinlerinde ornek gosterilirken kullanilan uc nokta
    ('Having started from... gibi') cumle sonu sayilmaz."""
    m = (m or "").strip()
    if not m:
        return 0
    m = m.replace("...", "…")
    parcalar = [p for p in re.split(r"(?<=[.!?])\s+", m) if p.strip()]
    return len(parcalar)


def sayilar(m):
    """Metindeki sayilari (yuzde, tam sayi, ondalik) cikarir."""
    return [float(s) for s in re.findall(r"\d+(?:[.,]\d+)?", m.replace(",", ""))]


def gorsel_degerleri(gorev):
    """visual / visuals icindeki butun sayisal degerler, kategoriler ve seriler."""
    degerler = set()
    kategoriler = set()
    seriler = []

    def gez(v):
        if not isinstance(v, dict):
            return
        for k in v.get("categories") or []:
            kategoriler.add(str(k))
            for s in re.findall(r"\d+", str(k)):
                degerler.add(float(s))
        yerel = []
        for s in v.get("series") or []:
            gecerli = [float(d) for d in (s.get("values") or [])
                       if isinstance(d, (int, float))]
            degerler.update(gecerli)
            if gecerli:
                yerel.append(gecerli)
        # ayni kategorinin seriler arasi toplami da mesru (2005 + 2020 gibi)
        if len(yerel) > 1 and len({len(x) for x in yerel}) == 1:
            yerel.append([sum(sut) for sut in zip(*yerel)])
        seriler.extend(yerel)
        for satir in v.get("rows") or []:
            for h in (satir if isinstance(satir, list) else satir.values()):
                if isinstance(h, (int, float)):
                    degerler.add(float(h))
                else:
                    for s in re.findall(r"\d+(?:\.\d+)?", str(h)):
                        degerler.add(float(s))
        for d in v.get("slices") or []:
            if isinstance(d, dict) and isinstance(d.get("value"), (int, float)):
                degerler.add(float(d["value"]))
        # harita / surec gorsellerinde sayi yerine metin var; ham metni de tara
        for s in re.findall(r"\d+(?:\.\d+)?", json.dumps(v, ensure_ascii=False)):
            degerler.add(float(s))

    gez(gorev.get("visual") or {})
    for v in gorev.get("visuals") or []:
        gez(v)
    return degerler, kategoriler, seriler


def turetilmis(degerler, seriler=()):
    """Cevapta mesru sekilde gecebilecek turetilmis sayilar: farklar, ikili
    toplamlar, seri toplamlari ve ortalamalari, kabaca yuvarlanmislar, kat
    oranlari. (Band 8 cevaplari 'the total rising from 21 to 26.5 million' gibi
    seri toplami veriyor - bunlar gorselde tek tek yazmaz, hesaplanir.)"""
    t = set(degerler)
    liste = sorted(degerler)
    for a in liste:
        t.add(round(a))
        t.add(round(a / 10.0) * 10)
        for b in liste:
            t.add(abs(a - b))
            t.add(a + b)
            if b:
                oran = a / b
                if oran == int(oran):
                    t.add(float(int(oran)))
    for s in seriler:
        degs = [float(x) for x in s if isinstance(x, (int, float))]
        if not degs:
            continue
        toplam = round(sum(degs), 6)
        t.add(toplam)
        t.add(round(toplam))
        t.add(round(toplam / len(degs), 1))
        # bir sutunun toplam icindeki payi (yuzde)
        for d in degs:
            if toplam:
                t.add(round(100.0 * d / toplam))
    return t


ISLEVSEL = set("""about above after again against all also among and any are because been
before being below between both but came can could did does doing down during each
few for from further had has have having here how instead into itself just large
many money more most much must now off once only other others our out over own part
people same should some spend such than that the their them then there these they
this those through time times too under until very what when where which while who
whom why will with would you your write letter task words minutes least give reasons
include relevant examples own knowledge experience opinion discuss views summarise
selecting reporting main features comparisons make below shows show agree disagree
extent problems measures taken positive negative development happening believe""".split())


def kok(k):
    """Kaba govde: cogul ve basit cekim eklerini atar. Band 5 cevaplari gorevin
    sozcugunu tekil/cogul yanlis kullaniyor ('the bus' vs 'buses') - ortusme
    olcumu bunu eksik sanmasin diye."""
    k = k.lower().strip("'-")
    for ek in ("ies", "es", "s", "ing", "ed"):
        if len(k) - len(ek) >= 4 and k.endswith(ek):
            govde = k[: -len(ek)]
            if ek == "ies":
                govde += "y"
            return govde
    return k


def anahtar_terimler(gorev):
    """Gorevin kendine ozgu icerik sozcukleri: gorseldeki seri/dilim adlari,
    baslik ve prompt'taki islevsel olmayan kelimeler. Cevabin bu gorevden mi
    bahsettigini olcmek icin - dosya yanlis eslesmisse ortusme sifira yakin olur."""
    metin = (gorev.get("prompt", "") or "") + " "
    for m in gorev.get("bullets") or []:
        metin += str(m) + " "
    gorsel = gorev.get("visual") or {}
    terimler = set()
    for s in gorsel.get("series") or []:
        if s.get("name") and not re.fullmatch(r"\d+", str(s["name"])):
            terimler.add(str(s["name"]).lower())
    for d in gorsel.get("slices") or []:
        if isinstance(d, dict) and d.get("label"):
            terimler.add(str(d["label"]).lower())
    for k in gorsel.get("categories") or []:
        if not re.fullmatch(r"\d+", str(k)):
            terimler.add(str(k).lower())
    metin += " " + (gorsel.get("title") or "")
    for k in re.findall(r"[A-Za-z][A-Za-z'-]{3,}", metin):
        k = k.lower()
        if k not in ISLEVSEL:
            terimler.add(k)
    return terimler


def govde(metin):
    """Mektuplarda selamlama/imza disi govde - kelime siniri icin."""
    satirlar = [s for s in metin.split("\n") if s.strip()]
    if satirlar and satirlar[0].lower().startswith("dear"):
        satirlar = satirlar[1:]
    while satirlar and kelime_say(satirlar[-1]) <= 4:
        satirlar = satirlar[:-1]
    return "\n".join(satirlar)


def main():
    havuz = gorev_havuzu()
    dosyalar = sorted(d for d in os.listdir(CEVAP) if d.endswith(".json"))
    print("Denetlenen cevap dosyasi: %d" % len(dosyalar))
    print("Havuzdaki yazma gorevi   : %d" % len(havuz))
    print()

    cumleler = defaultdict(list)   # cumle -> [(dosya, band)]
    dagilim = defaultdict(int)
    sayac = defaultdict(int)
    ortusme = []
    toplam_cevap = 0

    for d in dosyalar:
        yol = os.path.join(CEVAP, d)
        veri = oku(yol)
        kod = d[:-5]
        ref = veri.get("task_ref")

        # A - havuzda var mi, tur tutuyor mu
        if ref not in havuz:
            bulgu(d, "A", "task_ref '%s' havuzda yok" % ref)
            gorev = None
        else:
            gyol, gorev = havuz[ref]
            klasor = os.path.basename(os.path.dirname(gyol))
            beklenen = ("academic-task1" if kod.startswith("AT")
                        else "general-task1" if kod.startswith("GT")
                        else "task2")
            if klasor != beklenen:
                bulgu(d, "A", "gorev '%s' klasoru %s, beklenen %s"
                      % (ref, klasor, beklenen))
            dagilim[klasor] += 1
            if gorev.get("pattern"):
                dagilim["kalip:" + gorev["kalip"] if "kalip" in gorev
                        else "kalip:" + gorev["pattern"]] += 1

        terimler = anahtar_terimler(gorev) if gorev else set()
        if gorev:
            gdeg, _, gser = gorsel_degerleri(gorev)
            izinli = turetilmis(gdeg, gser) if gdeg else set()
        else:
            izinli = set()

        for cevap in veri.get("answers", []):
            toplam_cevap += 1
            band = cevap.get("band")
            metin = cevap.get("text") or cevap.get("transcript") or ""
            etiket = "%s/%s" % (kod, band)

            # B - gorevin kendi min_words degeri
            if gorev:
                alt = gorev.get("min_words") or (250 if gorev.get("task") == 2 else 150)
                sayim = kelime_say(govde(metin) if kod.startswith("GT") else metin)
                if sayim < alt:
                    bulgu(d, "B", "%s: %d kelime < gorevin min_words %d"
                          % (etiket, sayim, alt))

            # C - <=2 cumle siniri
            wtb = cevap.get("why_this_band") or {}
            for alan, deger in wtb.items():
                n = cumle_say(deger)
                if n > 2:
                    bulgu(d, "C", "%s: why_this_band.%s %d cumle (sinir 2)"
                          % (etiket, alan, n))
            n = cumle_say(cevap.get("what_would_lift_it") or "")
            if n > 2:
                bulgu(d, "C", "%s: what_would_lift_it %d cumle (sinir 2)" % (etiket, n))

            # D - cevap gorevden mi bahsediyor (icerik sozcugu ortusmesi)
            if len(terimler) >= 5:
                alt = set(kok(k) for k in re.findall(r"[A-Za-z][A-Za-z'-]*",
                                                     metin.lower()))
                metin_kucuk = metin.lower()
                gecen = [t for t in terimler
                         if kok(t) in alt or (" " in t and t in metin_kucuk)]
                oran = len(gecen) / float(len(terimler))
                ortusme.append((etiket, band, len(gecen), len(terimler), oran))
                # Band 5 cevabi gorevin sozcugunu kullanmak yerine basitlestiriyor
                # ('housing and health care' -> 'the house and the hospital'); bu
                # sinirli sozcuk dagarciginin kendisi, konu disiligin isareti degil.
                # Esik bu yuzden bandda ayrilir; amac yanlis eslesmis dosyayi
                # yakalamak, uslup olcmek degil.
                asgari, taban = (2, 0.10) if band <= 5.0 else (4, 0.15)
                if len(gecen) < asgari or oran < taban:
                    bulgu(d, "D", "%s: gorevle ortusme dusuk (%d/%d terim, %%%d)"
                          % (etiket, len(gecen), len(terimler), round(100 * oran)))

            # E - Academic Task 1 sayi dogrulugu
            if kod.startswith("AT") and izinli:
                supheli = []
                for s in sayilar(metin):
                    sayac["sayi"] += 1
                    if s in izinli:
                        continue
                    if any(abs(s - i) < 0.51 for i in izinli):
                        continue
                    supheli.append(s)
                if supheli:
                    bulgu(d, "E", "%s: gorselde karsiligi bulunmayan sayi(lar): %s"
                          % (etiket, ", ".join(("%g" % x) for x in supheli)))

            # F - kopyala-yapistir icin cumle havuzu
            for c in re.split(r"(?<=[.!?])\s+", metin):
                c = c.strip()
                if kelime_say(c) >= 8:
                    cumleler[c.lower()].append((kod, band))

    # F - iki ayri gorevde gecen ayni cumle
    for c, yerler in cumleler.items():
        kodlar = {k for k, _ in yerler}
        if len(kodlar) > 1:
            bulgu("-", "F", "ayni cumle %s dosyalarinda: \"%s...\""
                  % ("/".join(sorted(kodlar)), c[:70]))

    # G - KONTROL.md kapsami
    with open(KONTROL, encoding="utf-8") as f:
        kontrol = f.read()
    for d in dosyalar:
        kod = d[:-5]
        if not re.search(r"\|\s*%s\s*\|" % re.escape(kod), kontrol):
            bulgu("KONTROL.md", "G", "%s icin satir yok" % kod)

    print("Toplam cevap: %d" % toplam_cevap)
    print("Gorev dagilimi: %s" % dict(dagilim))
    print("Gorselle karsilastirilan sayi (Academic Task 1): %d" % sayac["sayi"])
    if ortusme:
        print()
        print("Gorev terimleriyle ortusme (bilgi, bulgu degil):")
        for b in (5.0, 6.5, 8.0):
            satir = [o for o in ortusme if o[1] == b]
            if satir:
                ort = sum(o[4] for o in satir) / len(satir)
                en_az = min(satir, key=lambda o: o[4])
                print("  band %-3s ortalama %%%2d  -  en dusuk %s (%%%d)"
                      % (b, round(100 * ort), en_az[0], round(100 * en_az[4])))
    print()
    if not bulgular:
        print("BULGU YOK - yedi denetimin hepsi temiz.")
    else:
        print("BULGU: %d" % len(bulgular))
        for dosya, tur, mesaj in bulgular:
            print("  [%s] %-12s %s" % (tur, dosya, mesaj))
    return 1 if bulgular else 0


if __name__ == "__main__":
    sys.exit(main())
