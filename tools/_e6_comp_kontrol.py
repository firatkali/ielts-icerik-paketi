# -*- coding: utf-8 -*-
"""OPUS5-E6 6. calistirma kontrolu: tamamlama ailesi yuvalari.

Denetledigi seyler:
  1. Yeniden doldurulan her yuva: alanlar, yeniden_uretim kaydi, eski isaret
     alanlarinin silinmis olmasi.
  2. Kanit cumlesi pasajda BIREBIR var mi ve evidence_locator dogru mu.
  3. Yeni kanit E5'in "kacinilacak" cumlesine degiyor mu (izin verilen ve
     belgelenen yeniden hedeflemeler disinda).
  4. Cevap kanit cumlesinde geciyor mu; kelime siniri asiliyor mu.
  5. stem_block'taki bosluk metni ile item prompt'u ayni mi; bosluklar artan mi.
  6. Kelime bankali sette cevap harfi bankada mi, bankada tekrar var mi.
  7. Konumsal duzen: kanitlarin paragraf dagilimi, son paragrafa demirlenme.
  8. Kip sayimi: yeni cerceve metinlerinde mutlak / olculu dil.

Kullanim: python tools/_e6_comp_kontrol.py
"""
import collections
import io
import json
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LISTE = os.path.join(KOK, "content", "DOGRULAMA", "yeniden-uretim-listesi.json")

# E5'in kendi onerisi uyarinca ayni cumlede BASKA bir ogeye tasinan yuvalar.
# (Sizdiran hedef cerceveden tumuyle cikarildi; NOTLAR.md'de belgelendi.)
IZINLI_AYNI_CUMLE = {
    ("content/reading/tests/AC2/flow-chart-completion.json", 3),
    ("content/reading/practice/summary-completion.json", 1),
    ("content/reading/tests/GT1/sentence-completion.json", 26),
}

MUTLAK = ["only", "every", "all", "no", "never", "always", "must", "cannot",
          "each", "entirely", "whole"]
OLCULU = ["about", "roughly", "may", "might", "some", "appears", "seemed",
          "suggests", "likely", "rather than", "almost", "partly", "around"]

hata = []


def paragraflar(pid):
    """{'A': ['metin', ...], ...}

    GT pasajlarinda iki ayri metin blogu ayni paragraf harflerini kullaniyor
    (depo geleneginde evidence_locator yalniz harfi tutuyor), bu yuzden her
    harf altinda birden cok paragraf olabilir.
    """
    for kok in ("academic", "general"):
        p = os.path.join(KOK, "passages", kok, pid + ".json")
        if not os.path.exists(p):
            continue
        d = json.load(open(p, encoding="utf-8"))
        out = collections.defaultdict(list)
        for x in (d.get("paragraphs") or []):
            out[x["label"]].append(x["text"])
        for t in (d.get("texts") or []):
            # GT metinlerinde paragraf harfi metnin icinde satir basinda duruyor.
            blok = None
            for satir in t["text"].split("\n"):
                s = satir.strip()
                if re.fullmatch(r"[A-Z]", s):
                    blok = s
                    out[blok].append("")
                elif blok is not None:
                    out[blok][-1] = (out[blok][-1] + "\n" + s).strip()
        return out
    raise SystemExit("pasaj yok: " + pid)


def cumleler(metin):
    """Cumlelere bol; madde imli listelerde her madde bir cumle sayilir."""
    parca = []
    for satir in re.split(r"\n+", metin):
        s = satir.strip()
        if not s:
            continue
        if s.startswith("- "):
            parca.append(s[2:].strip())
        else:
            parca.extend(x for x in re.split(r"(?<=[.!?])\s+", s) if x)
    return parca


def yuvalar(d):
    for g in (d["groups"] if "groups" in d else [d]):
        for it in g.get("items", []):
            yield it


def kelime_say(s):
    return len(re.findall(r"[^\s]+", s))


def sinir(word_limit):
    if not word_limit:
        return None
    m = re.search(r"\b(ONE|TWO|THREE)\b", word_limit)
    return {"ONE": 1, "TWO": 2, "THREE": 3}.get(m.group(1)) if m else None


def main():
    e5 = {(x["dosya"], x["numara"]): x for x in
          json.load(open(LISTE, encoding="utf-8"))["elenen"]}

    dosyalar = sorted(set(k[0] for k in e5))
    par_say = collections.Counter()
    yeni_cerceveler = []
    toplam = 0

    for rel in dosyalar:
        yol = os.path.join(KOK, rel.replace("/", os.sep))
        d = json.load(open(yol, encoding="utf-8"))
        pid_ust = d.get("passage_id")
        wl = sinir(d.get("word_limit"))
        banka = {o["letter"]: o["text"] for o in (d.get("word_bank") or [])}
        stem = d.get("stem_block") or ""

        for it in yuvalar(d):
            anahtar = (rel, it["number"])
            if anahtar not in e5:
                continue
            yu = it.get("yeniden_uretim")
            if not yu or yu.get("uretilen_grup") != "Tamamlama ailesi yuvalari":
                continue
            toplam += 1
            ad = "%s#%s" % (rel.split("/")[-2] + "/" + rel.split("/")[-1], it["number"])

            # 1. alanlar
            for alan in ("prompt", "answer", "evidence", "evidence_locator",
                         "explanation", "difficulty", "accepted_variants"):
                if not it.get(alan):
                    hata.append("%s: %s bos" % (ad, alan))
            if it.get("status") != "verified":
                hata.append("%s: status verified degil" % ad)
            if it.get("blind_solvable") is not None:
                hata.append("%s: blind_solvable null degil" % ad)
            if it.get("generated_by") != "opus":
                hata.append("%s: generated_by opus degil" % ad)
            for alan in ("flag_reason", "flag_mechanism", "reject_reason",
                         "review_note", "revision"):
                if alan in it:
                    hata.append("%s: eski alan silinmemis (%s)" % (ad, alan))

            # 2. kanit pasajda birebir mi
            pid = it.get("passage_id") or pid_ust
            pars = paragraflar(pid)
            loc = it["evidence_locator"]
            bulundu = False
            for govde in pars.get(loc["paragraph"], []):
                cl = cumleler(govde)
                if loc["sentence"] <= len(cl) and \
                        cl[loc["sentence"] - 1].strip() == it["evidence"].strip():
                    bulundu = True
            if not bulundu:
                hata.append("%s: kanit cumlesi %s/%s ile eslesmiyor" %
                            (ad, loc["paragraph"], loc["sentence"]))

            # 3. E5'in yasakladigi cumleye deginme
            yasak = (e5[anahtar]["kacinilacak"].get("kanit_cumlesi") or "").strip()
            if yasak and yasak == it["evidence"].strip() and anahtar not in IZINLI_AYNI_CUMLE:
                hata.append("%s: kanit E5'in yasakladigi cumle" % ad)

            # 4. cevap kanitta mi + kelime siniri
            for c in it["answer"]:
                if banka:
                    if c not in banka:
                        hata.append("%s: cevap harfi bankada yok (%s)" % (ad, c))
                    elif banka[c].lower().split()[-1] not in it["evidence"].lower():
                        hata.append("%s: banka metni kanitla ortusmuyor (%s)" % (ad, c))
                else:
                    if c.lower() not in it["evidence"].lower():
                        hata.append("%s: cevap kanit cumlesinde gecmiyor (%s)" % (ad, c))
                    if wl and kelime_say(c) > wl:
                        hata.append("%s: cevap kelime sinirini asiyor (%s)" % (ad, c))

            # 5. stem_block ile prompt ayni mi
            if stem:
                govde = it["prompt"].split(": ", 1)[-1] if d["question_type"] == "note_completion" \
                    else it["prompt"]
                if govde not in stem:
                    hata.append("%s: prompt stem_block'ta bulunamadi" % ad)

            par_say[(pid, loc["paragraph"])] += 1
            yeni_cerceveler.append((ad, it["prompt"]))

    # 6. banka tekrari
    for rel in dosyalar:
        d = json.load(open(os.path.join(KOK, rel.replace("/", os.sep)), encoding="utf-8"))
        wb = d.get("word_bank")
        if wb:
            metinler = [o["text"] for o in wb]
            if len(set(metinler)) != len(metinler):
                hata.append("%s: word_bank'ta tekrar var" % rel)

    # 7. stem_block bosluk sirasi
    for rel in dosyalar:
        d = json.load(open(os.path.join(KOK, rel.replace("/", os.sep)), encoding="utf-8"))
        stem = d.get("stem_block")
        if not stem:
            continue
        nums = [int(x) for x in re.findall(r"\((\d+)\) \.\.\.", stem)]
        if nums != sorted(nums):
            hata.append("%s: stem_block'ta bosluk sirasi artan degil %s" % (rel, nums))

    print("\n== yeniden doldurulan yuva: %d" % toplam)

    print("\n== konumsal duzen (kanitlarin paragraf dagilimi)")
    son_par = 0
    for (pid, par), n in sorted(par_say.items()):
        pars = paragraflar(pid)
        sonuncu = sorted(pars)[-1]
        isaret = "  <-- SON PARAGRAF" if par == sonuncu else ""
        if par == sonuncu:
            son_par += n
        print("  %s/%s : %d%s" % (pid, par, n, isaret))
    print("  toplam %d kanit, %d paragraf, son paragrafa demirlenen: %d" %
          (sum(par_say.values()), len(par_say), son_par))

    print("\n== kip sayimi (yeni cerceve metinleri)")
    def tasiyor(metin, sozler):
        return any(re.search(r"\b" + re.escape(k) + r"\b", metin, re.I) for k in sozler)

    mut = [a for a, p in yeni_cerceveler if tasiyor(p, MUTLAK)]
    olc = [a for a, p in yeni_cerceveler if tasiyor(p, OLCULU)]
    print("  mutlak ifade tasiyan: %d/%d (%%%d)" %
          (len(mut), len(yeni_cerceveler), 100 * len(mut) // max(1, len(yeni_cerceveler))))
    print("  olculu ifade tasiyan: %d/%d (%%%d)" %
          (len(olc), len(yeni_cerceveler), 100 * len(olc) // max(1, len(yeni_cerceveler))))

    print("\n== hata: %d" % len(hata))
    for h in hata:
        print("  - " + h)
    return 1 if hata else 0


sys.exit(main())
