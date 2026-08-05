# -*- coding: utf-8 -*-
"""Gecici kontrol: FABLE5-40 / AC1 true-false-not-given paketi."""
import json, os, re, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = os.path.join(KOK, "content", "reading", "tests", "AC1", "true-false-not-given.json")
P = os.path.join(KOK, "passages", "academic", "A01.json")

hata, uyari = [], []
d = json.load(open(S, encoding="utf-8"))
p = json.load(open(P, encoding="utf-8"))
paras = {x["label"]: x["text"] for x in p["paragraphs"]}
tam = " ".join(x["text"] for x in p["paragraphs"])

# zarf
bekle = {"schema_version": "1.0", "set_id": "AC1-true-false-not-given", "skill": "reading",
         "module": "academic", "test_id": "AC1", "practice": False, "passage_id": "A01",
         "question_type": "true_false_not_given", "generated_by": "fable"}
for k, v in bekle.items():
    if d.get(k) != v:
        hata.append("zarf %s = %r (beklenen %r)" % (k, d.get(k), v))
if d["options"] != ["TRUE", "FALSE", "NOT GIVEN"]:
    hata.append("options yanlis")
for kalip in ["Do the following statements agree with the information given in the passage?",
              "In boxes 7-13 on your answer sheet, write",
              "TRUE if the statement agrees with the information",
              "FALSE if the statement contradicts the information",
              "NOT GIVEN if there is no information on this"]:
    if kalip not in d["instructions"]:
        hata.append("yonerge eksik: " + kalip)

items = d["items"]
if [i["number"] for i in items] != list(range(7, 14)):
    hata.append("numaralar 7-13 degil")

sira_izi = []
for it in items:
    n = it["number"]
    cev = it["answer"]
    if len(cev) != 1 or cev[0] not in ("TRUE", "FALSE", "NOT GIVEN"):
        hata.append("%d: gecersiz cevap %r" % (n, cev))
    c = cev[0]
    # scan_note her soruda zorunlu
    if not (it.get("scan_note") or "").strip():
        hata.append("%d: scan_note bos" % n)
    if not (it.get("explanation") or "").strip():
        hata.append("%d: explanation bos" % n)
    if it.get("difficulty") not in ("easy", "medium", "hard"):
        hata.append("%d: difficulty yanlis" % n)
    # ifade uzunlugu ve tek cumle
    kel = len(it["prompt"].split())
    if kel > 20:
        hata.append("%d: ifade %d kelime (>20)" % (n, kel))
    if it["prompt"].count(".") != 1 or not it["prompt"].endswith("."):
        uyari.append("%d: tek cumle olmayabilir" % n)
    # alan doldurma kurallari
    if c in ("TRUE", "FALSE"):
        ev = it.get("evidence")
        if not ev:
            hata.append("%d: evidence bos" % n)
        else:
            loc = it.get("evidence_locator") or {}
            par = paras.get(loc.get("paragraph"))
            if par is None:
                hata.append("%d: paragraf bulunamadi %r" % (n, loc))
            elif ev not in par:
                hata.append("%d: evidence paragraf %s icinde birebir yok" % (n, loc.get("paragraph")))
            else:
                # cumle numarasi kontrolu
                cumleler = re.split(r"(?<=[.?!]) +", par)
                idx = loc.get("sentence")
                if not (isinstance(idx, int) and 1 <= idx <= len(cumleler) and ev == cumleler[idx - 1]):
                    hata.append("%d: sentence %r cumleyle eslesmiyor" % (n, idx))
                sira_izi.append((n, loc["paragraph"], idx))
        if it.get("not_given_justification") is not None:
            hata.append("%d: TRUE/FALSE'ta not_given_justification dolu" % n)
        if c == "FALSE" and not (it.get("contradiction_point") or "").strip():
            hata.append("%d: FALSE'ta contradiction_point bos" % n)
        if c == "TRUE" and it.get("contradiction_point") is not None:
            hata.append("%d: TRUE'da contradiction_point dolu" % n)
    else:
        if it.get("evidence") is not None or it.get("evidence_locator") is not None:
            hata.append("%d: NOT GIVEN'da evidence dolu" % n)
        if it.get("contradiction_point") is not None:
            hata.append("%d: NOT GIVEN'da contradiction_point dolu" % n)
        j = it.get("not_given_justification") or ""
        if not j.strip():
            hata.append("%d: not_given_justification bos" % n)
        for isaret in ("(1)", "(2)", "(3)"):
            if isaret not in j:
                hata.append("%d: not_given_justification'da %s sarti yok" % (n, isaret))
    # birebir kopya yasagi: ifadenin 6 kelimelik hicbir dizisi pasajda gecmesin
    kelimeler = re.findall(r"[A-Za-z']+", it["prompt"].lower())
    duz = " ".join(re.findall(r"[A-Za-z']+", tam.lower()))
    for i in range(len(kelimeler) - 5):
        parca = " ".join(kelimeler[i:i + 6])
        if parca in duz:
            hata.append("%d: pasajla 6 kelimelik ortusme: %r" % (n, parca))

# cevap dagilimi
cevaplar = [i["answer"][0] for i in items]
from collections import Counter
say = Counter(cevaplar)
for k in ("TRUE", "FALSE", "NOT GIVEN"):
    if say[k] == 0:
        hata.append("dagilim: %s hic yok" % k)
    if say[k] > len(items) / 2:
        hata.append("dagilim: %s yarıyı geciyor (%d)" % (k, say[k]))
for i in range(len(cevaplar) - 2):
    if cevaplar[i] == cevaplar[i + 1] == cevaplar[i + 2]:
        hata.append("ardisik uc ayni cevap: %d-%d" % (items[i]["number"], items[i + 2]["number"]))

# sira kurali (TRUE/FALSE kanitlarinin pasajdaki yeri artan olmali)
etiketler = [x["label"] for x in p["paragraphs"]]
anahtar = [(etiketler.index(par), idx) for _, par, idx in sira_izi]
if anahtar != sorted(anahtar):
    hata.append("sira kurali: kanitlar pasaj sirasinda degil %r" % (sira_izi,))

# asiri genelleme
genel = [i["number"] for i in items
         if re.search(r"\b(all|never|always|every|none|the most|only)\b", i["prompt"], re.I)]
if len(genel) > 2:
    hata.append("asiri genelleme %d soruda: %r" % (len(genel), genel))

# gorunur metinde IELTS
gorunur = [d["instructions"]] + [i["prompt"] for i in items]
if any("ielts" in g.lower() for g in gorunur):
    hata.append("gorunur metinde IELTS geciyor")

# ayni testteki diger paketlerle cakisma (A01 = note-completion)
nc = json.load(open(os.path.join(os.path.dirname(S), "note-completion.json"), encoding="utf-8"))
nc_ev = {i.get("evidence") for i in nc["items"]}
for it in items:
    if it.get("evidence") and it["evidence"] in nc_ev:
        uyari.append("%d: note-completion ile ayni kanit cumlesi" % it["number"])

print("dagilim:", dict(say))
print("cevap sirasi:", cevaplar)
print("kanit sirasi:", sira_izi)
print("ifade kelime sayilari:", [len(i["prompt"].split()) for i in items])
print("genelleme iceren:", genel)
print("HATA %d" % len(hata))
for h in hata:
    print("  X", h)
print("UYARI %d" % len(uyari))
for u in uyari:
    print("  !", u)
