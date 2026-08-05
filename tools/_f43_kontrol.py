"""FABLE5-43 hizli kontrol: evidence birebir mi, turn_index sirasi ve araligi,
secenek uzunluklari, harf dengesi. Kullanim: python tools/_f43_kontrol.py L1"""
import json
import os
import sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST = sys.argv[1] if len(sys.argv) > 1 else "L1"


def oku(p):
    with open(os.path.join(KOK, p), encoding="utf-8") as f:
        return json.load(f)


def turnler(sid):
    d = oku("content/listening/scripts/%s.json" % sid)
    return [t["text"] for t in d["turns"]]


def itemler(d):
    out = []
    for g in (d.get("groups") or [d]):
        for it in g.get("items") or []:
            sid = it.get("script_id") or g.get("script_id") or d.get("script_id")
            out.append((g, it, sid))
    return out


def main():
    sorun = 0
    cache = {}
    for ad in ["multiple-choice", "matching"]:
        p = "content/listening/tests/%s/%s.json" % (TEST, ad)
        if not os.path.exists(os.path.join(KOK, p)):
            continue
        d = oku(p)
        onceki = {}
        for g, it, sid in itemler(d):
            if sid not in cache:
                cache[sid] = turnler(sid)
            ts = cache[sid]
            no, ti = it["number"], it["turn_index"]
            if it["evidence"] not in ts[ti]:
                sorun += 1
                print("SORUN %s soru %s: evidence %s. replikte birebir yok" % (p, no, ti))
            gid = id(g)
            if gid in onceki:
                fark = ti - onceki[gid]
                if fark < 3:
                    sorun += 1
                    print("SORUN %s soru %s: replik araligi %d (<3)" % (p, no, fark))
            onceki[gid] = ti
            for o in (it.get("options") or []):
                if len(o["text"].split()) > 10:
                    sorun += 1
                    print("SORUN %s soru %s: secenek %s 10 kelimeden uzun" % (p, no, o["letter"]))
            kok_sec = len(str(it["prompt"]).split()) + sum(
                len(o["text"].split()) for o in (it.get("options") or []))
            if it.get("options") and kok_sec > 50:
                sorun += 1
                print("SORUN %s soru %s: kok+secenek %d kelime (>50)" % (p, no, kok_sec))
        for o in ((d.get("box") or {}).get("options") or []):
            if len(o["text"].split()) > 10:
                sorun += 1
                print("SORUN %s kutu %s: 10 kelimeden uzun" % (p, o["letter"]))
    print("Sorun sayisi: %d" % sorun)
    return 1 if sorun else 0


if __name__ == "__main__":
    sys.exit(main())
