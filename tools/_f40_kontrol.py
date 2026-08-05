# -*- coding: utf-8 -*-
"""Gecici kontrol: FABLE5-40 dogru/yanlis paketleri (TFNG + YNNG).

Kullanim: python tools/_f40_kontrol.py [TEST]   (varsayilan AC1)
AC testlerinde 1. pasajin TFNG dosyasi, GT testlerinde hem TFNG (bolum 1)
hem YNNG (bolum 3) dosyasi denetlenir. Pasaj eslemesi PLAN'dan.
TEST yerine PR-TFNG / PR-YNNG verilirse content/reading/practice altindaki
alistirma paketi denetlenir (cok pasajli, numaralar 1'den baslar)."""
import json, os, re, sys, io, glob
from collections import Counter

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST = sys.argv[1] if len(sys.argv) > 1 else "AC1"

# (dosya, pasaj, modul, pasaj klasoru, soru numaralari, tip)
ISLER = {
    "AC1": [("true-false-not-given.json", "A01", "academic", range(7, 14), "tfng")],
    "AC2": [("true-false-not-given.json", "A04", "academic", range(7, 14), "tfng")],
    "AC3": [("true-false-not-given.json", "A07", "academic", range(7, 14), "tfng")],
    "AC4": [("true-false-not-given.json", "A10", "academic", range(7, 14), "tfng")],
    "GT1": [("true-false-not-given.json", "G01", "general", range(8, 15), "tfng"),
            ("yes-no-not-given.json", "G05", "general", range(33, 37), "ynng")],
    "GT2": [("true-false-not-given.json", "G02", "general", range(8, 15), "tfng"),
            ("yes-no-not-given.json", "G06", "general", range(33, 37), "ynng")],
}

TIP = {
    "tfng": {
        "options": ["TRUE", "FALSE", "NOT GIVEN"],
        "question_type": "true_false_not_given",
        "set_eki": "-true-false-not-given",
        "yonerge": ["Do the following statements agree with the information given in the passage?",
                    "TRUE if the statement agrees with the information",
                    "FALSE if the statement contradicts the information",
                    "NOT GIVEN if there is no information on this"],
        "olumsuz": "FALSE",
    },
    "ynng": {
        "options": ["YES", "NO", "NOT GIVEN"],
        "question_type": "yes_no_not_given",
        "set_eki": "-yes-no-not-given",
        "yonerge": ["Do the following statements agree with the claims of the writer in the passage?",
                    "YES if the statement agrees with the claims of the writer",
                    "NO if the statement contradicts the claims of the writer",
                    "NOT GIVEN if it is impossible to say what the writer thinks about this"],
        "olumsuz": "NO",
    },
}


def cumle_bol(par, koru_saat):
    """Cumle bolucu. koru_saat: 'a.m.' / 'p.m.' kisaltmalarinda bolme;
    yalniz ardindan buyuk harf geliyorsa yeni cumle say."""
    if not koru_saat:
        return re.split(r"(?<=[.?!]) +", par)
    k = par.replace("a.m.", "a¤m¤").replace("p.m.", "p¤m¤")
    parcalar = re.split(r"(?<=[.?!]) +", k)
    sonuc = []
    for p_ in parcalar:
        sonuc.extend(re.split(r"(?<=[ap]¤m¤) (?=[A-Z])", p_))
    return [s.replace("a¤m¤", "a.m.").replace("p¤m¤", "p.m.") for s in sonuc]


def denetle(dosya, pasaj_id, modul, numaralar, tip_adi):
    hata, uyari = [], []
    t = TIP[tip_adi]
    S = os.path.join(KOK, "content", "reading", "tests", TEST, dosya)
    klasor = "academic" if modul == "academic" else "general"
    P = os.path.join(KOK, "passages", klasor, pasaj_id + ".json")
    d = json.load(open(S, encoding="utf-8"))
    p = json.load(open(P, encoding="utf-8"))

    if p.get("paragraphs"):
        birimler = p["paragraphs"]
        loc_anahtar = "paragraph"
    else:
        birimler = p["texts"]
        loc_anahtar = "text"
    paras = {x["label"]: x["text"] for x in birimler}
    tam = " ".join(x["text"] for x in birimler)
    koru_saat = "a.m." in tam or "p.m." in tam

    bekle = {"schema_version": "1.0", "set_id": TEST + t["set_eki"], "skill": "reading",
             "module": modul, "test_id": TEST, "practice": False, "passage_id": pasaj_id,
             "question_type": t["question_type"], "generated_by": "fable"}
    for k, v in bekle.items():
        if d.get(k) != v:
            hata.append("zarf %s = %r (beklenen %r)" % (k, d.get(k), v))
    if d["options"] != t["options"]:
        hata.append("options yanlis")
    numaralar = list(numaralar)
    kutular = "In boxes %d-%d on your answer sheet, write" % (numaralar[0], numaralar[-1])
    for kalip in t["yonerge"] + [kutular]:
        if kalip not in d["instructions"]:
            hata.append("yonerge eksik: " + kalip)

    items = d["items"]
    if [i["number"] for i in items] != numaralar:
        hata.append("numaralar %d-%d degil" % (numaralar[0], numaralar[-1]))

    dogru, yanlis = t["options"][0], t["options"][1]
    sira_izi = []
    for it in items:
        n = it["number"]
        cev = it["answer"]
        if len(cev) != 1 or cev[0] not in t["options"]:
            hata.append("%d: gecersiz cevap %r" % (n, cev))
        c = cev[0]
        if not (it.get("scan_note") or "").strip():
            hata.append("%d: scan_note bos" % n)
        if not (it.get("explanation") or "").strip():
            hata.append("%d: explanation bos" % n)
        if it.get("difficulty") not in ("easy", "medium", "hard"):
            hata.append("%d: difficulty yanlis" % n)
        kel = len(it["prompt"].split())
        if kel > 20:
            hata.append("%d: ifade %d kelime (>20)" % (n, kel))
        if it["prompt"].count(".") != 1 or not it["prompt"].endswith("."):
            uyari.append("%d: tek cumle olmayabilir" % n)
        if c in (dogru, yanlis):
            ev = it.get("evidence")
            if not ev:
                hata.append("%d: evidence bos" % n)
            else:
                loc = it.get("evidence_locator") or {}
                par = paras.get(loc.get(loc_anahtar))
                if par is None:
                    hata.append("%d: %s bulunamadi %r" % (n, loc_anahtar, loc))
                elif ev not in par:
                    hata.append("%d: evidence %s %s icinde birebir yok" % (n, loc_anahtar, loc.get(loc_anahtar)))
                else:
                    cumleler = cumle_bol(par, koru_saat)
                    idx = loc.get("sentence")
                    if not (isinstance(idx, int) and 1 <= idx <= len(cumleler) and ev == cumleler[idx - 1]):
                        hata.append("%d: sentence %r cumleyle eslesmiyor" % (n, idx))
                    sira_izi.append((n, loc[loc_anahtar], idx))
            if it.get("not_given_justification") is not None:
                hata.append("%d: %s/%s'ta not_given_justification dolu" % (n, dogru, yanlis))
            if c == yanlis and not (it.get("contradiction_point") or "").strip():
                hata.append("%d: %s'ta contradiction_point bos" % (n, yanlis))
            if c == dogru and it.get("contradiction_point") is not None:
                hata.append("%d: %s'da contradiction_point dolu" % (n, dogru))
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
        kelimeler = re.findall(r"[A-Za-z']+", it["prompt"].lower())
        duz = " ".join(re.findall(r"[A-Za-z']+", tam.lower()))
        for i in range(len(kelimeler) - 5):
            parca = " ".join(kelimeler[i:i + 6])
            if parca in duz:
                hata.append("%d: pasajla 6 kelimelik ortusme: %r" % (n, parca))

    cevaplar = [i["answer"][0] for i in items]
    say = Counter(cevaplar)
    for k in t["options"]:
        if say[k] == 0:
            hata.append("dagilim: %s hic yok" % k)
        if say[k] > len(items) / 2:
            hata.append("dagilim: %s yariyi geciyor (%d)" % (k, say[k]))
    for i in range(len(cevaplar) - 2):
        if cevaplar[i] == cevaplar[i + 1] == cevaplar[i + 2]:
            hata.append("ardisik uc ayni cevap: %d-%d" % (items[i]["number"], items[i + 2]["number"]))

    etiketler = [x["label"] for x in birimler]
    anahtar = [(etiketler.index(par_), idx) for _, par_, idx in sira_izi]
    if anahtar != sorted(anahtar):
        hata.append("sira kurali: kanitlar pasaj sirasinda degil %r" % (sira_izi,))

    genel = [i["number"] for i in items
             if re.search(r"\b(all|never|always|every|none|the most|only)\b", i["prompt"], re.I)]
    if len(genel) > 2:
        hata.append("asiri genelleme %d soruda: %r" % (len(genel), genel))

    gorunur = [d["instructions"]] + [i["prompt"] for i in items]
    if any("ielts" in g.lower() for g in gorunur):
        hata.append("gorunur metinde IELTS geciyor")

    for komsu in ("note-completion.json", "flow-chart-completion.json", "table-completion.json",
                  "summary-completion.json", "sentence-completion.json"):
        yol = os.path.join(os.path.dirname(S), komsu)
        if not os.path.exists(yol):
            continue
        nc = json.load(open(yol, encoding="utf-8"))
        if nc.get("passage_id") != pasaj_id:
            continue
        nc_ev = {i.get("evidence") for i in nc["items"]}
        for it in items:
            if it.get("evidence") and it["evidence"] in nc_ev:
                uyari.append("%d: %s ile ayni kanit cumlesi" % (it["number"], komsu))

    print("== %s / %s (%s) ==" % (TEST, dosya, pasaj_id))
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
    return len(hata)


def pasaj_yukle(pasaj_id):
    klasor = "academic" if pasaj_id.startswith("A") else "general"
    p = json.load(open(os.path.join(KOK, "passages", klasor, pasaj_id + ".json"), encoding="utf-8"))
    if p.get("paragraphs"):
        return p, p["paragraphs"], "paragraph"
    return p, p["texts"], "text"


def denetle_alistirma(tip_adi):
    """Alistirma paketi: cok pasajli, numaralar 1..N, test_id null, practice true."""
    hata, uyari = [], []
    t = TIP[tip_adi]
    dosya = t["set_eki"][1:] + ".json"
    S = os.path.join(KOK, "content", "reading", "practice", dosya)
    d = json.load(open(S, encoding="utf-8"))
    items = d["items"]

    moduller = set()
    for it in items:
        moduller.add("academic" if (it.get("passage_id") or "").startswith("A") else "general")
    modul = moduller.pop() if len(moduller) == 1 else "both"

    bekle = {"schema_version": "1.0", "set_id": "practice" + t["set_eki"], "skill": "reading",
             "module": modul, "test_id": None, "practice": True, "passage_id": None,
             "question_type": t["question_type"], "generated_by": "fable"}
    for k, v in bekle.items():
        if d.get(k) != v:
            hata.append("zarf %s = %r (beklenen %r)" % (k, d.get(k), v))
    if d["options"] != t["options"]:
        hata.append("options yanlis")

    numaralar = list(range(1, len(items) + 1))
    if [i["number"] for i in items] != numaralar:
        hata.append("numaralar 1-%d degil" % len(items))
    kutular = "In boxes 1-%d on your answer sheet, write" % len(items)
    for kalip in t["yonerge"] + [kutular]:
        if kalip not in d["instructions"]:
            hata.append("yonerge eksik: " + kalip)

    dogru, yanlis = t["options"][0], t["options"][1]
    pasaj_bilgi, sira_izi, grup_say = {}, {}, Counter()
    for it in items:
        n = it["number"]
        pid = it.get("passage_id")
        if not pid:
            hata.append("%d: passage_id bos" % n)
            continue
        grup_say[pid] += 1
        if pid not in pasaj_bilgi:
            pasaj_bilgi[pid] = pasaj_yukle(pid)
        p, birimler, loc_anahtar = pasaj_bilgi[pid]
        paras = {x["label"]: x["text"] for x in birimler}
        tam = " ".join(x["text"] for x in birimler)
        koru_saat = "a.m." in tam or "p.m." in tam

        cev = it["answer"]
        if len(cev) != 1 or cev[0] not in t["options"]:
            hata.append("%d: gecersiz cevap %r" % (n, cev))
            continue
        c = cev[0]
        if not (it.get("scan_note") or "").strip():
            hata.append("%d: scan_note bos" % n)
        if not (it.get("explanation") or "").strip():
            hata.append("%d: explanation bos" % n)
        if it.get("difficulty") not in ("easy", "medium", "hard"):
            hata.append("%d: difficulty yanlis" % n)
        kel = len(it["prompt"].split())
        if kel > 20:
            hata.append("%d: ifade %d kelime (>20)" % (n, kel))
        if it["prompt"].count(".") != 1 or not it["prompt"].endswith("."):
            uyari.append("%d: tek cumle olmayabilir" % n)

        if c in (dogru, yanlis):
            ev = it.get("evidence")
            if not ev:
                hata.append("%d: evidence bos" % n)
            else:
                loc = it.get("evidence_locator") or {}
                par = paras.get(loc.get(loc_anahtar))
                if par is None:
                    hata.append("%d: %s bulunamadi %r" % (n, loc_anahtar, loc))
                elif ev not in par:
                    hata.append("%d: evidence %s %s icinde birebir yok" % (n, loc_anahtar, loc.get(loc_anahtar)))
                else:
                    cumleler = cumle_bol(par, koru_saat)
                    idx = loc.get("sentence")
                    if not (isinstance(idx, int) and 1 <= idx <= len(cumleler) and ev == cumleler[idx - 1]):
                        hata.append("%d: sentence %r cumleyle eslesmiyor" % (n, idx))
                    sira_izi.setdefault(pid, []).append((n, loc[loc_anahtar], idx))
            if it.get("not_given_justification") is not None:
                hata.append("%d: %s/%s'ta not_given_justification dolu" % (n, dogru, yanlis))
            if c == yanlis and not (it.get("contradiction_point") or "").strip():
                hata.append("%d: %s'ta contradiction_point bos" % (n, yanlis))
            if c == dogru and it.get("contradiction_point") is not None:
                hata.append("%d: %s'da contradiction_point dolu" % (n, dogru))
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

        kelimeler = re.findall(r"[A-Za-z']+", it["prompt"].lower())
        duz = " ".join(re.findall(r"[A-Za-z']+", tam.lower()))
        for i in range(len(kelimeler) - 5):
            parca = " ".join(kelimeler[i:i + 6])
            if parca in duz:
                hata.append("%d: pasajla 6 kelimelik ortusme: %r" % (n, parca))

    for pid, adet in grup_say.items():
        if adet > 4:
            hata.append("pasaj kotasi: %s icin %d soru (>4)" % (pid, adet))

    for pid, iz in sira_izi.items():
        p, birimler, _ = pasaj_bilgi[pid]
        etiketler = [x["label"] for x in birimler]
        anahtar = [(etiketler.index(par_), idx) for _, par_, idx in iz]
        if anahtar != sorted(anahtar):
            hata.append("sira kurali (%s): kanitlar pasaj sirasinda degil %r" % (pid, iz))

    cevaplar = [i["answer"][0] for i in items]
    say = Counter(cevaplar)
    for k in t["options"]:
        if say[k] == 0:
            hata.append("dagilim: %s hic yok" % k)
        if say[k] > len(items) / 2:
            hata.append("dagilim: %s yariyi geciyor (%d)" % (k, say[k]))
    for i in range(len(cevaplar) - 2):
        if cevaplar[i] == cevaplar[i + 1] == cevaplar[i + 2]:
            hata.append("ardisik uc ayni cevap: %d-%d" % (items[i]["number"], items[i + 2]["number"]))

    genel = [i["number"] for i in items
             if re.search(r"\b(all|never|always|every|none|the most|only)\b", i["prompt"], re.I)]
    if len(genel) > 2:
        hata.append("asiri genelleme %d soruda: %r" % (len(genel), genel))

    gorunur = [d["instructions"], d.get("stem_block") or ""] + [i["prompt"] for i in items]
    if any("ielts" in g.lower() for g in gorunur):
        hata.append("gorunur metinde IELTS geciyor")

    # stem_block her pasaj grubunu anmali
    sb = d.get("stem_block") or ""
    for pid in grup_say:
        if pid not in sb:
            hata.append("stem_block'ta %s yok" % pid)

    # kanit cakismasi: butun diger okuma paketleri
    baskalari = {}
    for yol in glob.glob(os.path.join(KOK, "content", "reading", "**", "*.json"), recursive=True):
        if os.path.abspath(yol) == os.path.abspath(S):
            continue
        o = json.load(open(yol, encoding="utf-8"))
        for oi in o["items"]:
            opid = oi.get("passage_id") or o.get("passage_id")
            if oi.get("evidence"):
                baskalari.setdefault((opid, oi["evidence"]), []).append(
                    os.path.basename(os.path.dirname(yol)) + "/" + os.path.basename(yol))
    for it in items:
        anahtar = (it.get("passage_id"), it.get("evidence"))
        if it.get("evidence") and anahtar in baskalari:
            uyari.append("%d: %s ile ayni kanit cumlesi" % (it["number"], ", ".join(sorted(set(baskalari[anahtar])))))

    print("== alistirma / %s ==" % dosya)
    print("pasaj dagilimi:", dict(grup_say))
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
    return len(hata)


if TEST in ("PR-TFNG", "PR-YNNG"):
    toplam = denetle_alistirma("tfng" if TEST == "PR-TFNG" else "ynng")
else:
    toplam = sum(denetle(*is_) for is_ in ISLER[TEST])
sys.exit(1 if toplam else 0)
