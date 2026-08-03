"""Sema dogrulamasi + tam test butunlugu + telif taramasi.

Kullanim:  python tools/dogrula.py

Hicbir dosyayi degistirmez, sadece rapor basar.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

import collections
import json

ZORUNLU_ZARF = ["schema_version", "set_id", "skill", "test_id", "practice",
                "question_type", "generated_by", "instructions"]
ZORUNLU_ITEM = ["number", "prompt", "answer", "explanation", "difficulty"]

TIPE_OZEL = {
    "true_false_not_given": ["scan_note"],
    "yes_no_not_given": ["scan_note"],
    "multiple_choice": ["options", "select_count", "distractor_analysis"],
    "multiple_choice_multi": ["options", "select_count", "distractor_analysis"],
    "matching_headings": ["option_list", "heading_check"],
    "matching_features": ["option_list", "feature_check"],
    "matching_sentence_endings": ["option_list", "grammar_check"],
    "matching_information": ["uniqueness_check"],
    "matching": ["distractor_analysis"],
}

TESTLER = [("content/reading/tests", ["AC1", "AC2", "AC3", "AC4", "GT1", "GT2"]),
           ("content/listening/tests", ["L1", "L2", "L3", "L4", "L5", "L6"])]


def turkce_mi(s):
    return bool(re.search(r"[çğıöşüÇĞİÖŞÜ]", s))


def main():
    hatalar = []
    sayim = collections.Counter()
    flagged = 0

    dosyalar = ortak.soru_dosyalari()
    if not dosyalar:
        print("content/ altinda hic soru dosyasi yok.")
        return 1

    for p in dosyalar:
        try:
            d = ortak.oku(p)
        except Exception as e:
            hatalar.append("%s: JSON bozuk - %s" % (p, e))
            continue

        for k in ZORUNLU_ZARF:
            if k not in d:
                hatalar.append("%s: zarf alani eksik '%s'" % (p, k))

        qt = d.get("question_type")
        if qt not in ortak.TIPLER:
            hatalar.append("%s: bilinmeyen question_type '%s'" % (p, qt))

        gorulen = []
        for it in ortak.sorular(d):
            no = it.get("number")
            gorulen += ortak.numaralar(it)

            for k in ZORUNLU_ITEM:
                if k not in it:
                    hatalar.append("%s: soru %s - alan eksik '%s'" % (p, no, k))
            for k in TIPE_OZEL.get(qt, []):
                if it.get(k) in (None, "", {}, []) and k not in d:
                    hatalar.append("%s: soru %s - tipe ozel alan eksik '%s'" % (p, no, k))

            if not it.get("answer"):
                hatalar.append("%s: soru %s - cevap bos" % (p, no))

            cevap = " ".join(str(x).upper() for x in (it.get("answer") or []))
            if not it.get("evidence") and "NOT GIVEN" not in cevap:
                hatalar.append("%s: soru %s - evidence bos" % (p, no))

            exp = it.get("explanation") or ""
            if exp and len(exp.split()) > 6 and not turkce_mi(exp):
                hatalar.append("%s: soru %s - explanation Turkce olmayabilir" % (p, no))

            if d.get("skill") == "listening" and it.get("turn_index") is None:
                hatalar.append("%s: soru %s - turn_index eksik" % (p, no))

            if it.get("status") == "flagged":
                flagged += 1

            anahtar = "%s/%s" % (d.get("skill", "?"),
                                 "practice" if d.get("practice") else "test")
            sayim[anahtar] += 2 if it.get("select_count") == 2 else 1

        if len(set(gorulen)) != len(gorulen):
            hatalar.append("%s: tekrar eden soru numarasi var" % p)

    print("=== SORU SAYILARI ===")
    for k in sorted(sayim):
        print("  %-22s %d" % (k, sayim[k]))
    print("  %-22s %d" % ("TOPLAM", sum(sayim.values())))
    print("  %-22s %d" % ("isaretli (flagged)", flagged))

    print("\n=== TAM TEST BUTUNLUGU (her test 40 soru) ===")
    for kok, testler in TESTLER:
        for t in testler:
            nums = set()
            for p in ortak.bul("%s/%s/*.json" % (kok, t)):
                for it in ortak.sorular(ortak.oku(p)):
                    nums.update(ortak.numaralar(it))
            eksik = sorted(set(range(1, 41)) - nums)
            fazla = sorted(n for n in nums if n < 1 or n > 40)
            durum = "TAM" if not eksik and not fazla else "EKSIK"
            ek = ""
            if eksik:
                ek += "  eksik=%s%s" % (eksik[:12], "..." if len(eksik) > 12 else "")
            if fazla:
                ek += "  ARALIK DISI=%s" % fazla
            print("  %-4s %2d/40  %-5s%s" % (t, len(nums), durum, ek))

    print("\n=== PASAJ LISANSLARI ===")
    eksik_lisans = []
    for p in ortak.bul("passages/**/*.json"):
        if p.endswith("INDEX.json"):
            continue
        d = ortak.oku(p)
        if not (d.get("source") or {}).get("license"):
            eksik_lisans.append(p)
    print("  Pasaj sayisi: %d | lisansi eksik: %d" % (
        len(ortak.bul("passages/**/*.json")), len(eksik_lisans)))
    for p in eksik_lisans:
        print("   - LISANS EKSIK:", p)

    print("\n=== TELIF TARAMASI ===")
    yasak = re.compile(r"cambridge|british council|\bidp\b|wikipedia|the conversation",
                       re.I)
    ielts_gecen, yasak_gecen = [], []
    for p in dosyalar + ortak.bul("passages/**/*.json"):
        with open(ortak.yol(p), encoding="utf-8") as f:
            ham = f.read()
        d = json.loads(ham)
        gorunur = json.dumps({
            "i": d.get("instructions"),
            "s": [it.get("prompt") for it in ortak.sorular(d)],
            "p": d.get("paragraphs"), "t": d.get("texts"), "b": d.get("stem_block"),
        }, ensure_ascii=False)
        if re.search(r"ielts", gorunur, re.I):
            ielts_gecen.append(p)
        if yasak.search(ham):
            yasak_gecen.append(p)
    print("  Kullaniciya gorunen metinde 'IELTS' gecen dosya: %d" % len(ielts_gecen))
    for p in ielts_gecen:
        print("   - TEMIZLE:", p)
    print("  Yasak kaynak adi gecen dosya: %d" % len(yasak_gecen))
    for p in yasak_gecen:
        print("   - INCELE:", p)

    print("\n=== SEMA HATALARI: %d ===" % len(hatalar))
    for h in hatalar[:200]:
        print("  -", h)
    if len(hatalar) > 200:
        print("  ... ve %d tane daha" % (len(hatalar) - 200))

    return 0 if not hatalar else 1


if __name__ == "__main__":
    sys.exit(main())
