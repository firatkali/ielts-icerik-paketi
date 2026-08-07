"""B1 5. adim yardimcisi: 2. calistirmanin (ynng + baslik eslestirme) ozet sayilari.

Set bazinda oran, anahtar bazinda oran, tur kararliligi ve dayanak dagilimi.
"""

import collections
import importlib.util
import json
import os
import sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(KOK, "tools"))
import ortak  # noqa: E402

spec = importlib.util.spec_from_file_location(
    "mr", os.path.join(KOK, "tools", "metinsiz-rapor.py"))
mr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mr)


def calis(paket):
    anahtar = mr.anahtar_yukle()
    rapor = ortak.oku("content/DOGRULAMA/METINSIZ-%s.json" % paket)
    bilinen = set(rapor["uc_turda_bilinen"])

    turlar = []
    for n in (1, 2, 3):
        with open(ortak.yol("kalibrasyon", "metinsiz", "%s-tur%d.json" % (paket, n)),
                  encoding="utf-8") as f:
            turlar.append({a["id"]: a for a in json.load(f)["answers"]})

    ids = list(turlar[0])
    set_sayac = collections.defaultdict(lambda: [0, 0])
    anahtar_sayac = collections.defaultdict(lambda: [0, 0])
    kararli = 0
    dayanak_hepsi = collections.Counter()
    dayanak_isaretli = collections.Counter()

    for sid in ids:
        kume = sid.rsplit("-", 1)[0].replace("-%s" % paket, "")
        kume = sid.split("-")[0]
        set_sayac[kume][0] += 1
        cev = str(anahtar[sid]["answer"])
        anahtar_sayac[cev][0] += 1
        if sid in bilinen:
            set_sayac[kume][1] += 1
            anahtar_sayac[cev][1] += 1
        vs = [tuple(mr.normal(t[sid]["answer"])) for t in turlar]
        if vs[0] == vs[1] == vs[2]:
            kararli += 1
        for t in turlar:
            b = t[sid].get("basis")
            if b:
                dayanak_hepsi[b] += 1
                if sid in bilinen:
                    dayanak_isaretli[b] += 1

    print("== %s ==" % paket)
    print("toplam %d | 3/3 bilinen %d (%%%.1f)"
          % (len(ids), len(bilinen), len(bilinen) / len(ids) * 100))
    print("uc turda ayni cevap: %d/%d (%%%.0f)"
          % (kararli, len(ids), kararli / len(ids) * 100))
    print("-- set bazinda --")
    for k in sorted(set_sayac):
        t, b = set_sayac[k]
        print("  %-10s %2d soru  %2d bilinen  %%%.0f" % (k, t, b, b / t * 100))
    print("-- anahtar bazinda --")
    for k in sorted(anahtar_sayac):
        t, b = anahtar_sayac[k]
        print("  %-16s %2d  ->  %2d  %%%.0f" % (k, t, b, b / t * 100))
    print("-- dayanak (tum cevaplar / isaretli sorularda) --")
    for k in sorted(set(dayanak_hepsi) | set(dayanak_isaretli)):
        print("  %-18s %3d  /  %3d" % (k, dayanak_hepsi[k], dayanak_isaretli[k]))
    print()


for p in sys.argv[1:]:
    calis(p)
