"""Diger tools scriptlerinin paylastigi yardimcilar."""

import json
import os
import glob

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TIPLER = set("""note_completion table_completion flow_chart_completion summary_completion
sentence_completion short_answer diagram_labelling form_completion
plan_map_diagram_labelling matching_information matching_headings matching_features
matching_sentence_endings matching true_false_not_given yes_no_not_given
multiple_choice multiple_choice_multi""".split())


def yol(*parcalar):
    return os.path.join(KOK, *parcalar)


def bul(desen):
    """Depo kokune gore glob; her zaman depo-koku-goreli yollar dondurur."""
    tam = glob.glob(os.path.join(KOK, desen), recursive=True)
    return sorted(os.path.relpath(p, KOK).replace(os.sep, "/") for p in tam)


def oku(gorece_yol):
    with open(os.path.join(KOK, gorece_yol), encoding="utf-8") as f:
        return json.load(f)


def yaz(gorece_yol, veri):
    tam = os.path.join(KOK, gorece_yol)
    os.makedirs(os.path.dirname(tam), exist_ok=True)
    with open(tam, "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=2)


def sorular(d):
    """Hem 'items' hem 'groups' yapisindan duz soru listesi cikarir."""
    out = []
    for g in (d.get("groups") or [{"items": d.get("items") or []}]):
        out += (g.get("items") or [])
    return out


def numaralar(it):
    """'34-35' gibi cift cevapli numaralari da acar."""
    n = str(it.get("number"))
    if "-" in n:
        try:
            a, b = n.split("-")
            return list(range(int(a), int(b) + 1))
        except ValueError:
            return []
    try:
        return [int(n)]
    except ValueError:
        return []


def soru_dosyalari():
    """Soru seti JSON'lari (senaryolar, dogrulama raporlari ve manifest haric)."""
    out = []
    for p in bul("content/**/*.json"):
        if "/scripts/" in p or "/DOGRULAMA/" in p:
            continue
        if p.endswith("MANIFEST.json") or p.endswith("PLAN-soru-dagilimi.md"):
            continue
        # Alt cizgiyle baslayan dosyalar soru seti degil, test tanimidir
        # (ornek: _test.json - band esigi tablosu). Ornek cevap kutuphanesi de
        # soru degildir; sema kontrolu ikisini de soru sanmamali.
        if os.path.basename(p).startswith("_") or "/ornek-cevaplar/" in p:
            continue
        out.append(p)
    return out
