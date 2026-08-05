"""FABLE5-42 kontrolu: eslestirme tipleri (headings / features / sentence endings).

Kullanim:  python tools/_f42_kontrol.py content/reading/tests/AC1/matching-headings.json ...

Neyi denetler:
  - JSON gecerli, zorunlu zarf alanlari yerinde
  - her evidence ilgili pasajda BIREBIR geciyor ve evidence_locator dogru paragrafi
    gosteriyor
  - secenek sayisi soru sayisindan en az 3 fazla
  - hicbir secenek metni pasajda birebir gecmiyor (kelime avi engeli)
  - tipe ozel kontrol alani (heading_check / feature_check / grammar_check) dolu,
    otekiler null
  - allow_repeat ile hem yonergedeki NB satiri hem cevaplardaki tekrar tutarli
  - bosta kalan (celdirici) secenek var
  - kullaniciya gorunen metinde 'IELTS' gecmiyor
Hicbir dosyayi degistirmez.
"""

import json
import os
import sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALANLAR = {"matching_headings": "heading_check",
           "matching_features": "feature_check",
           "matching_sentence_endings": "grammar_check"}


def pasaj_metni(pid):
    alt = "academic" if pid.startswith("A") else "general"
    with open(os.path.join(KOK, "passages", alt, pid + ".json"), encoding="utf-8") as f:
        d = json.load(f)
    paras = {p["label"]: p["text"] for p in (d.get("paragraphs") or [])}
    for t in (d.get("texts") or []):
        paras[t.get("label", "?")] = t.get("text", "")
    return paras


def kumeler(d):
    if d.get("groups"):
        return [(g, g.get("passage_id") or d.get("passage_id")) for g in d["groups"]]
    return [(d, d.get("passage_id"))]


def denetle(yol):
    sorun = []
    with open(os.path.join(KOK, yol), encoding="utf-8") as f:
        d = json.load(f)

    qt = d.get("question_type")
    if qt not in ALANLAR:
        return ["%s: beklenmeyen question_type '%s'" % (yol, qt)]
    zorunlu_alan = ALANLAR[qt]

    for g, pid in kumeler(d):
        etiket = "%s%s" % (yol, "/" + g["group_id"] if g.get("group_id") else "")
        paras = pasaj_metni(pid)
        tam = "\n".join(paras.values())
        items = g.get("items") or []
        opts = (g.get("option_list") or {}).get("options") or []

        # Baslik ve cumle sonu eslestirmede liste soru sayisindan en az 3 fazla olur.
        # Ozellik eslestirmede kural farkli: liste 3-5 ogedir, soru sayisi listeden
        # fazla bile olabilir (bir harf birden cok kez kullanilabilir).
        if qt == "matching_features":
            if not 3 <= len(opts) <= 5:
                sorun.append("%s: ozellik listesi 3-5 oge olmali (%d var)"
                             % (etiket, len(opts)))
        elif len(opts) < len(items) + 3:
            sorun.append("%s: %d soru icin yalnizca %d secenek (en az %d olmali)"
                         % (etiket, len(items), len(opts), len(items) + 3))

        anahtarlar = [o["key"] for o in opts]
        if len(set(anahtarlar)) != len(anahtarlar):
            sorun.append("%s: secenek anahtari tekrar ediyor" % etiket)

        cevaplar = [a for it in items for a in it["answer"]]
        ornek = (g.get("example") or {}).get("key")
        for c in cevaplar:
            if c not in anahtarlar:
                sorun.append("%s: cevap '%s' secenek listesinde yok" % (etiket, c))
        bosta = [k for k in anahtarlar if k not in cevaplar and k != ornek]
        if not bosta:
            sorun.append("%s: bosta celdirici secenek kalmamis" % etiket)

        tekrar = len(cevaplar) != len(set(cevaplar))
        if tekrar != bool(g.get("allow_repeat")):
            sorun.append("%s: allow_repeat=%s ama cevaplarda tekrar %s"
                         % (etiket, g.get("allow_repeat"), "var" if tekrar else "yok"))
        nb = "NB" in (g.get("instructions") or d.get("instructions") or "")
        if nb != bool(g.get("allow_repeat")):
            sorun.append("%s: NB satiri ile allow_repeat uyusmuyor" % etiket)

        if qt == "matching_headings" and not g.get("example"):
            sorun.append("%s: baslik eslestirmede example zorunlu" % etiket)
        if qt != "matching_headings" and g.get("example"):
            sorun.append("%s: bu tipte example null olmali" % etiket)
        if ornek and ornek in cevaplar:
            sorun.append("%s: ornek basligi ayni zamanda cevap olmus" % etiket)

        # Baslik ve cumle sonu eslestirmede secenek pasajdan birebir alinamaz, yoksa
        # soru kelime avina doner. Ozellik eslestirmede liste zaten pasajdaki
        # kisi/kurum/yer adlarindan kurulur (resmi ornekte de oyle); orada kural
        # ifadelere isler: soru koku pasajdaki cumlenin kopyasi olamaz.
        if qt == "matching_features":
            cumleler = {c.strip().lower() for p in paras.values() for c in p.split(". ")}
            for it in items:
                pr = str(it.get("prompt", "")).strip().rstrip(".").lower()
                if pr and (pr in cumleler or pr in tam.lower()):
                    sorun.append("%s: soru %s - ifade pasajdan birebir kopya"
                                 % (etiket, it.get("number")))
        else:
            for o in opts:
                if o["text"].lower() in tam.lower():
                    sorun.append("%s: secenek pasajda birebir geciyor - '%s'"
                                 % (etiket, o["text"]))

        for it in items:
            no = it.get("number")
            ev = it.get("evidence") or ""
            if ev not in tam:
                sorun.append("%s: soru %s - evidence pasajda birebir yok" % (etiket, no))
            loc = it.get("evidence_locator") or {}
            hedef = paras.get(loc.get("paragraph"), "")
            if ev and ev not in hedef:
                sorun.append("%s: soru %s - evidence_locator yanlis paragrafi gosteriyor (%s)"
                             % (etiket, no, loc.get("paragraph")))
            if not it.get(zorunlu_alan):
                sorun.append("%s: soru %s - %s bos" % (etiket, no, zorunlu_alan))
            for baska in set(ALANLAR.values()) - {zorunlu_alan}:
                if it.get(baska) is not None:
                    sorun.append("%s: soru %s - %s null olmali" % (etiket, no, baska))
            if not it.get("explanation"):
                sorun.append("%s: soru %s - explanation bos" % (etiket, no))
            if qt == "matching_headings" and not str(it.get("prompt", "")).startswith("Paragraph"):
                sorun.append("%s: soru %s - prompt 'Paragraph X' olmali" % (etiket, no))

        gorunur = json.dumps({"i": g.get("instructions") or d.get("instructions"),
                              "o": opts,
                              "s": [it.get("prompt") for it in items]},
                             ensure_ascii=False)
        if "ielts" in gorunur.lower():
            sorun.append("%s: gorunur metinde IELTS geciyor" % etiket)

    return sorun


def main(yollar):
    hepsi = []
    for y in yollar:
        s = denetle(y.replace("\\", "/"))
        hepsi += s
        print("%-52s %s" % (y, "TAMAM" if not s else "%d sorun" % len(s)))
    for s in hepsi:
        print("  -", s)
    print("\nTOPLAM SORUN: %d" % len(hepsi))
    return 0 if not hepsi else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
