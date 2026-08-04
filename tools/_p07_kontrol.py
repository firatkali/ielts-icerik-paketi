"""OPUS5-21 / 7. paket denetimi: content/listening/practice/note-completion.json

Kullanim:  python tools/_p07_kontrol.py

Hicbir dosyayi degistirmez. Uretilen alistirma setini diskten geri okuyup
promptun teslim listesindeki her maddeyi tek tek sinar.
"""

import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

HEDEF = "content/listening/practice/note-completion.json"
BEKLENEN_SORU = 15


def kelime_sayisi(s):
    """(kelime, sayi) jetonu sayar; harf iceren jeton kelimedir."""
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


def main():
    hata = []
    uyari = []

    d = ortak.oku(HEDEF)
    ham = open(ortak.yol(HEDEF), encoding="utf-8").read()

    # --- zarf
    for k, v in [("skill", "listening"), ("practice", True), ("test_id", None),
                 ("generated_by", "opus"), ("question_type", "note_completion")]:
        if d.get(k) != v:
            hata.append("zarf: %s = %r (beklenen %r)" % (k, d.get(k), v))
    if not d.get("instructions"):
        hata.append("zarf: instructions bos")

    # --- tam testlerde kullanilmis bilgi noktalari
    testte = set()
    for p in glob.glob(ortak.yol("content/listening/tests/*/*.json")):
        for it in ortak.sorular(json.load(open(p, encoding="utf-8"))):
            testte.add(it["answer_point_id"])

    senaryo = {}
    numaralar = []
    senaryo_sayaci = {}

    for g in d["groups"]:
        sid = g["script_id"]
        if sid not in senaryo:
            senaryo[sid] = ortak.oku("content/listening/scripts/%s.json" % sid)
        s = senaryo[sid]
        noktalar = {ap["id"]: ap for ap in s["answer_points"]}
        limit = g["word_limit"]
        gid = g["group_id"]

        if not 3 <= len(g["items"]) <= 5:
            hata.append("%s: kume boyu %d (3-5 olmali)" % (gid, len(g["items"])))
        if not g.get("instructions") or not g.get("stem_block"):
            hata.append("%s: instructions/stem_block eksik" % gid)
        if limit not in g["instructions"]:
            hata.append("%s: yonergede kelime siniri yazmiyor" % gid)

        onceki_turn = -1
        for it in g["items"]:
            no = it["number"]
            etiket = "%s/soru %s" % (gid, no)
            numaralar.append(no)
            senaryo_sayaci[sid] = senaryo_sayaci.get(sid, 0) + 1

            if it.get("script_id") != sid:
                hata.append("%s: item script_id kume ile uyusmuyor" % etiket)

            apid = it["answer_point_id"]
            if apid in testte:
                hata.append("%s: %s tam testte kullanilmis" % (etiket, apid))
            if apid not in noktalar:
                hata.append("%s: %s senaryoda yok" % (etiket, apid))
                continue
            ap = noktalar[apid]

            # turn_index
            if it["turn_index"] != ap["turn_index"]:
                hata.append("%s: turn_index %s, bilgi noktasi %s" % (
                    etiket, it["turn_index"], ap["turn_index"]))
            # tek kisilik anlatimda "replik" = paragraf: ayri paragraf yeterli,
            # karsilikli konusmada iki cevabin arasindan en az bir replik gecmeli
            asgari_ara = 2 if len(s["speakers"]) > 1 else 1
            if it["turn_index"] <= onceki_turn:
                hata.append("%s: sira kurali bozuk (t%s <= t%s)" % (
                    etiket, it["turn_index"], onceki_turn))
            elif onceki_turn >= 0 and it["turn_index"] - onceki_turn < asgari_ara:
                hata.append("%s: nefes payi yok (t%s -> t%s)" % (
                    etiket, onceki_turn, it["turn_index"]))
            onceki_turn = it["turn_index"]

            # evidence senaryoda birebir mi
            replik = s["turns"][it["turn_index"]]["text"]
            if it["evidence"] not in replik:
                hata.append("%s: evidence replikte birebir yok" % etiket)

            # cevap seste birebir soyleniyor mu (varyantlardan biri repligin icinde)
            adaylar = list(it["answer"]) + list(it.get("accepted_variants") or [])
            if not any(a.lower() in replik.lower() for a in adaylar):
                uyari.append("%s: cevap repligin metninde harfi harfine gecmiyor "
                             "(sesli okunus mu? elle bak) -> %r" % (etiket, it["answer"]))

            # kelime siniri: cevap + butun varyantlar
            for a in adaylar:
                if not sinir_kontrol(a, limit):
                    hata.append("%s: '%s' kelime sinirini asiyor (%s)" % (etiket, a, limit))

            # prompt gövdede mi
            if it["prompt"] not in g["stem_block"]:
                hata.append("%s: prompt stem_block icinde yok" % etiket)
            if "(%d) ........" % no not in g["stem_block"]:
                hata.append("%s: gövdede '(%d) ........' bosluğu yok" % (etiket, no))

            # zorunlu alanlar
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
    if re.search(r"ielts", ham, re.I):
        hata.append("dosyada 'IELTS' geciyor")

    print("=== 7. PAKET DENETIMI ===")
    print("  soru sayisi      : %d" % len(numaralar))
    print("  kume sayisi      : %d (%s)" % (
        len(d["groups"]), ", ".join("%s=%d" % (g["group_id"], len(g["items"]))
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
