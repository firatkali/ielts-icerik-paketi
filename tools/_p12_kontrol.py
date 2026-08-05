"""OPUS5-21 / 12. paket denetimi: content/listening/practice/plan-map-diagram-labelling.json

Kullanim:  python tools/_p12_kontrol.py [hedef.json]

Hicbir dosyayi degistirmez. Uretilen alistirma setini diskten geri okuyup
promptun teslim listesindeki her maddeyi sinar. 11. paketin denetiminden
farklari, tipin kendisinden geliyor:

1. Etiketleme sorusunda `stem_block` yok; boslugun yeri SVG'nin icinde.
   O yuzden "(n) ........" araniz yerine, kelime yazma kumelerinde bosluk
   numarasinin, harf secme kumelerinde secenek harfinin SVG metninde
   gectigi dogrulanir.
2. Harf secme kumelerinde cevap bir harftir; "cevap seste birebir
   soyleniyor mu" kontrolu bu yuzden soru kokundeki yer adinin evidence
   icinde gectigine bakilarak yapilir.
3. SVG kurallari ayrica sinanir: tek satir, viewBox var, sabit
   width/height yok, sadece izinli etiketler, sabit renk yok, kuzey oku ve
   giris isareti var, en az bir sabit referans noktasi adiyla yazili.
"""

import glob
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

HEDEF = (sys.argv[1] if len(sys.argv) > 1
         else "content/listening/practice/plan-map-diagram-labelling.json")
BEKLENEN_SORU = 15
IZINLI_ETIKET = {"svg", "rect", "circle", "line", "path", "polygon", "text"}
DOLGU_KELIME = {"and", "the", "of", "on", "in", "at", "a", "for"}


def kelime_sayisi(s):
    kelime = sayi = 0
    for jeton in s.split():
        temiz = jeton.strip("£$€.,;:()").replace(",", "")
        if not temiz:
            continue
        if re.search(r"[A-Za-z]", temiz):
            kelime += 1
        else:
            sayi += 1
    return kelime, sayi


def sinir_kontrol(s, limit):
    k, n = kelime_sayisi(s)
    if "THREE WORDS" in limit:
        azami_k = 3
    elif "TWO WORDS" in limit:
        azami_k = 2
    else:
        azami_k = 1
    azami_n = 1 if "A NUMBER" in limit else 0
    return k <= azami_k and n <= azami_n


def svg_dene(svg, gid, hata):
    if "\n" in svg or "\r" in svg:
        hata.append("%s: SVG tek satir degil" % gid)
    if not svg.startswith("<svg ") or not svg.endswith("</svg>"):
        hata.append("%s: SVG govdesi <svg ...>...</svg> degil" % gid)
    if "viewBox=" not in svg:
        hata.append("%s: SVG'de viewBox yok" % gid)
    bas = svg[:svg.index(">") + 1]
    if re.search(r'\swidth="', bas) or re.search(r'\sheight="', bas):
        hata.append("%s: <svg> etiketinde sabit width/height var" % gid)
    if re.search(r'(fill|stroke)="#(?!000\b)[0-9a-fA-F]{3,6}"', svg):
        hata.append("%s: SVG'de siyah disinda renk var" % gid)
    if 'font-size="12"' not in svg or 'font-family="sans-serif"' not in svg:
        hata.append("%s: SVG'de font-size=12 / font-family=sans-serif yok" % gid)
    try:
        kok = ET.fromstring(svg)
    except ET.ParseError as e:
        hata.append("%s: SVG XML olarak cozulemedi - %s" % (gid, e))
        return []
    metinler = []
    for e in kok.iter():
        ad = e.tag.split("}")[-1]
        if ad not in IZINLI_ETIKET:
            hata.append("%s: SVG'de izinsiz etiket <%s>" % (gid, ad))
        if ad == "text":
            metinler.append("".join(e.itertext()).strip())
    if "N" not in metinler:
        hata.append("%s: SVG'de kuzey oku etiketi (N) yok" % gid)
    if not any("ENTRANCE" in m for m in metinler):
        hata.append("%s: SVG'de giris isareti yok" % gid)
    sabit = [m for m in metinler
             if len(m) > 2 and m == m.upper() and re.search(r"[A-Z]{3}", m)
             and "ENTRANCE" not in m]
    if len(sabit) < 1:
        hata.append("%s: SVG'de adiyla yazili sabit referans noktasi yok" % gid)
    return metinler


def main():
    hata = []
    uyari = []

    d = ortak.oku(HEDEF)
    ham = open(ortak.yol(HEDEF), encoding="utf-8").read()
    tip = d.get("question_type")

    # --- zarf
    for k, v in [("skill", "listening"), ("practice", True), ("test_id", None),
                 ("generated_by", "opus"), ("visual", None), ("options", None),
                 ("stem_block", None), ("table", None), ("section", None)]:
        if d.get(k) != v:
            hata.append("zarf: %s = %r (beklenen %r)" % (k, d.get(k), v))
    if tip != "plan_map_diagram_labelling":
        hata.append("zarf: question_type '%s'" % tip)
    if not d.get("instructions"):
        hata.append("zarf: instructions bos")

    # --- baska setlerde kullanilmis bilgi noktalari
    baskasinda = set()
    dosyalar = glob.glob(ortak.yol("content/listening/tests/*/*.json"))
    dosyalar += [p for p in glob.glob(ortak.yol("content/listening/practice/*.json"))
                 if os.path.basename(p) != os.path.basename(HEDEF)]
    for p in dosyalar:
        for it in ortak.sorular(json.load(open(p, encoding="utf-8"))):
            baskasinda.add(it["answer_point_id"])

    senaryo = {}
    numaralar = []
    senaryo_sayaci = {}
    alt_tipler = set()

    for g in d["groups"]:
        sid = g["script_id"]
        if sid not in senaryo:
            senaryo[sid] = ortak.oku("content/listening/scripts/%s.json" % sid)
        s = senaryo[sid]
        noktalar = {ap["id"]: ap for ap in s["answer_points"]}
        gid = g["group_id"]
        limit = g.get("word_limit")
        harf_secme = bool(g.get("options"))
        alt_tipler.add("harf" if harf_secme else "kelime")

        if not 3 <= len(g["items"]) <= 5:
            hata.append("%s: kume boyu %d (3-5 olmali)" % (gid, len(g["items"])))
        if not g.get("instructions"):
            hata.append("%s: instructions eksik" % gid)
        if not g.get("context_line"):
            hata.append("%s: context_line bos" % gid)
        if g.get("stem_block") is not None or g.get("table") is not None:
            hata.append("%s: etiketlemede stem_block ve table null olmali" % gid)
        if g.get("question_type") not in (None, tip):
            hata.append("%s: kume question_type zarfla uyusmuyor" % gid)
        if g["script_id"] != s["script_id"]:
            hata.append("%s: script_id senaryo dosyasiyla uyusmuyor" % gid)
        if s.get("section") != 2:
            hata.append("%s: %s 2. bolum senaryosu degil" % (gid, sid))
        if not s.get("spatial_description"):
            hata.append("%s: %s icinde spatial_description yok" % (gid, sid))

        gorsel = g.get("visual") or {}
        if gorsel.get("kind") not in ("plan", "map", "diagram"):
            hata.append("%s: visual.kind '%s'" % (gid, gorsel.get("kind")))
        if not gorsel.get("alt"):
            hata.append("%s: visual.alt bos" % gid)
        metinler = svg_dene(gorsel.get("svg") or "", gid, hata)

        if harf_secme:
            if g["options"] != ["A", "B", "C", "D", "E", "F", "G", "H"]:
                hata.append("%s: options A-H degil" % gid)
            if limit is not None:
                hata.append("%s: harf secmede word_limit null olmali" % gid)
            for h in g["options"]:
                if h not in metinler:
                    hata.append("%s: '%s' secenegi planda yok" % (gid, h))
            if gorsel.get("labels") != g["options"]:
                hata.append("%s: visual.labels secenek listesiyle ayni degil" % gid)
        else:
            if not limit:
                hata.append("%s: kelime yazmada word_limit bos" % gid)
            elif limit not in g["instructions"]:
                hata.append("%s: yonergede kelime siniri yazmiyor" % gid)
            if g.get("options") is not None:
                hata.append("%s: kelime yazmada options null olmali" % gid)
            bekleyen = [str(it["number"]) for it in g["items"]]
            if gorsel.get("labels") != bekleyen:
                hata.append("%s: visual.labels bosluk numaralari degil" % gid)
            for n in bekleyen:
                if n not in metinler:
                    hata.append("%s: %s numarali bosluk planda yok" % (gid, n))

        onceki_turn = -1
        for it in g["items"]:
            no = it["number"]
            etiket = "%s/soru %s" % (gid, no)
            numaralar.append(no)
            senaryo_sayaci[sid] = senaryo_sayaci.get(sid, 0) + 1

            if it.get("script_id") != sid:
                hata.append("%s: item script_id kume ile uyusmuyor" % etiket)

            apid = it["answer_point_id"]
            if apid in baskasinda:
                hata.append("%s: %s baska bir sette kullanilmis" % (etiket, apid))
            if apid not in noktalar:
                hata.append("%s: %s senaryoda yok" % (etiket, apid))
                continue
            ap = noktalar[apid]

            if it["turn_index"] != ap["turn_index"]:
                hata.append("%s: turn_index %s, bilgi noktasi %s" % (
                    etiket, it["turn_index"], ap["turn_index"]))
            asgari_ara = 2 if len(s["speakers"]) > 1 else 1
            if it["turn_index"] <= onceki_turn:
                hata.append("%s: sira kurali bozuk (t%s <= t%s)" % (
                    etiket, it["turn_index"], onceki_turn))
            elif onceki_turn >= 0 and it["turn_index"] - onceki_turn < asgari_ara:
                hata.append("%s: nefes payi yok (t%s -> t%s)" % (
                    etiket, onceki_turn, it["turn_index"]))
            onceki_turn = it["turn_index"]

            replik = s["turns"][it["turn_index"]]["text"]
            if it["evidence"] not in replik:
                hata.append("%s: evidence replikte birebir yok" % etiket)

            if harf_secme:
                # cevap harf: seste gecen sey soru kokundeki yer adi
                if it["answer"] != [it["answer"][0]] or \
                        it["answer"][0] not in (g.get("options") or []):
                    hata.append("%s: cevap secenek listesinde degil" % etiket)
                eksik = [w for w in re.findall(r"[a-z]+", it["prompt"].lower())
                         if w not in DOLGU_KELIME
                         and w not in it["evidence"].lower()]
                if eksik:
                    uyari.append("%s: soru kokundeki %s evidence icinde yok "
                                 "(elle bak)" % (etiket, eksik))
                if it["answer"][0] not in metinler:
                    hata.append("%s: cevap harfi planda yok" % etiket)
            else:
                adaylar = list(it["answer"]) + list(it.get("accepted_variants") or [])
                if not any(a.lower() in replik.lower() for a in adaylar):
                    uyari.append("%s: cevap repligin metninde harfi harfine "
                                 "gecmiyor -> %r" % (etiket, it["answer"]))
                for a in adaylar:
                    if not sinir_kontrol(a, limit or ""):
                        hata.append("%s: '%s' kelime sinirini asiyor (%s)"
                                    % (etiket, a, limit))
                if "(%d)" % no in it["prompt"] or "........" in it["prompt"]:
                    hata.append("%s: etiketlemede promptta bosluk isareti olmamali"
                                % etiket)
                if str(no) not in it["prompt"]:
                    hata.append("%s: prompt bosluk numarasini soylemiyor" % etiket)

            for alan in ["prompt", "answer", "evidence", "explanation", "difficulty"]:
                if not it.get(alan):
                    hata.append("%s: '%s' bos" % (etiket, alan))
            if not re.search(r"[çğıöşüÇĞİÖŞÜ]", it["explanation"]):
                hata.append("%s: explanation Turkce degil" % etiket)
            if it["difficulty"] not in ("easy", "medium", "hard"):
                hata.append("%s: difficulty '%s'" % (etiket, it["difficulty"]))

    # --- toplu kontroller
    if numaralar != list(range(1, BEKLENEN_SORU + 1)):
        hata.append("soru numaralari 1..%d degil: %s" % (BEKLENEN_SORU, numaralar))
    for sid, n in senaryo_sayaci.items():
        if n > 4:
            hata.append("%s senaryosundan %d soru (en fazla 4)" % (sid, n))
    if alt_tipler != {"harf", "kelime"}:
        hata.append("iki alt tip de kullanilmamis: %s" % sorted(alt_tipler))
    if re.search(r"ielts", ham, re.I):
        hata.append("dosyada 'IELTS' geciyor")

    print("=== DENETIM: %s ===" % HEDEF)
    print("  soru sayisi      : %d" % len(numaralar))
    print("  kume sayisi      : %d (%s)" % (
        len(d["groups"]), ", ".join(
            "%s=%d/%s" % (g["group_id"], len(g["items"]),
                          "harf" if g.get("options") else "kelime")
            for g in d["groups"])))
    print("  senaryo dagilimi : %s" % senaryo_sayaci)
    print("  uyari            : %d" % len(uyari))
    for u in uyari:
        print("   ~", u)
    print("  HATA             : %d" % len(hata))
    for h in hata:
        print("   -", h)
    return 0 if not hata else 1


if __name__ == "__main__":
    sys.exit(main())
