"""FABLE5-43 alistirma kontrolu (7-9. calistirmalar): evidence birebir mi,
turn_index sirasi/araligi ve bilgi noktasiyla uyumu, secenek uzunluklari,
kok+secenek siniri, harf dengesi, senaryo basina soru tavani, baska dosyada
cevap olarak kullanilmis bilgi noktasi. Kullanim: python tools/_p43_kontrol.py [dosya]"""
import collections
import glob
import json
import os
import sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOSYA = sys.argv[1] if len(sys.argv) > 1 else "content/listening/practice/multiple-choice.json"


def oku(p):
    with open(os.path.join(KOK, p), encoding="utf-8") as f:
        return json.load(f)


def main():
    sorun = 0
    d = oku(DOSYA)
    letters, apids, nums = [], [], []
    senaryo = collections.Counter()
    for g in d["groups"]:
        sid = g["script_id"]
        sc = oku("content/listening/scripts/%s.json" % sid)
        ts = [t["text"] for t in sc["turns"]]
        aps = {a["id"]: a for a in sc["answer_points"]}
        prev = None
        for it in g["items"]:
            no, ti = it["number"], it["turn_index"]
            nums.append(no)
            senaryo[sid] += 1
            apids.append(it["answer_point_id"])
            if it["evidence"] not in ts[ti]:
                sorun += 1
                print("SORUN soru %s: evidence %d. replikte birebir yok" % (no, ti))
            if it["answer_point_id"] not in aps:
                sorun += 1
                print("SORUN soru %s: answer_point_id senaryoda yok" % no)
            elif aps[it["answer_point_id"]]["turn_index"] != ti:
                sorun += 1
                print("SORUN soru %s: turn_index bilgi noktasiyla uyusmuyor" % no)
            if prev is not None and ti - prev < 3:
                sorun += 1
                print("SORUN soru %s: replik araligi %d (<3)" % (no, ti - prev))
            prev = ti
            for o in it["options"]:
                if len(o["text"].split()) > 10:
                    sorun += 1
                    print("SORUN soru %s secenek %s: 10 kelimeden uzun" % (no, o["letter"]))
            toplam = len(it["prompt"].split()) + sum(
                len(o["text"].split()) for o in it["options"])
            if toplam > 50:
                sorun += 1
                print("SORUN soru %s: kok+secenek %d kelime (>50)" % (no, toplam))
            letters += it["answer"]
            yanlis = {o["letter"] for o in it["options"]} - set(it["answer"])
            if set(it["distractor_analysis"]) != yanlis:
                sorun += 1
                print("SORUN soru %s: distractor_analysis harfleri eksik/fazla" % no)
        if senaryo[sid] > 4:
            sorun += 1
            print("SORUN: %s senaryosundan 4'ten fazla soru" % sid)
    for a, b in zip(letters, letters[1:]):
        if a == b:
            sorun += 1
            print("SORUN: ust uste ayni harf (%s)" % a)
    if nums != list(range(1, len(nums) + 1)):
        sorun += 1
        print("SORUN: numaralar 1'den ardisik degil:", nums)
    kendi = os.path.normpath(os.path.join(KOK, DOSYA))
    kullanilmis = set()
    for f in glob.glob(os.path.join(KOK, "content/listening/tests/*/*.json")) + \
            glob.glob(os.path.join(KOK, "content/listening/practice/*.json")):
        if os.path.normpath(f) == kendi:
            continue
        dd = json.load(open(f, encoding="utf-8"))
        items = []
        for gg in (dd.get("groups") or []):
            items += gg.get("items") or []
        items += dd.get("items") or []
        for it in items:
            if it.get("answer_point_id"):
                kullanilmis.add(it["answer_point_id"])
    cakisan = [a for a in apids if a in kullanilmis]
    if cakisan:
        sorun += 1
        print("SORUN: baska dosyada cevap olan nokta:", cakisan)
    print("cevap dizisi: %s  dagilim: %s" % (letters, dict(collections.Counter(letters))))
    print("senaryo basina soru:", dict(senaryo))
    print("Sorun sayisi: %d" % sorun)
    return 1 if sorun else 0


if __name__ == "__main__":
    sys.exit(main())
