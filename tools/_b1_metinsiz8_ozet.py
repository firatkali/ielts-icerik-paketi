"""8. calistirma ozet istatistikleri: sentence-completion + short-answer.

Kullanim: python tools/_b1_metinsiz8_ozet.py

Set bazinda oran, tur kararliligi, dayanak dagilimi, zorluk etiketi iliskisi ve
soru soru "uc turda ne verildi / anahtar neydi" dokumu uretir.
"""

import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402


def normal(a):
    if a is None:
        return []
    if not isinstance(a, list):
        a = [a]
    return sorted(str(x).strip().lower() for x in a)


def anahtar_yukle(paket):
    tablo = {}
    for p in ortak.bul("content/**/%s.json" % paket):
        if "/DOGRULAMA/" in p:
            continue
        d = ortak.oku(p)
        if d.get("skill") != "reading":
            continue
        set_id = d.get("set_id", os.path.basename(p))
        for it in ortak.sorular(d):
            tablo["%s-%s" % (set_id, it.get("number"))] = {
                "answer": it.get("answer"),
                "accepted": it.get("accepted_variants") or [],
                "set": set_id,
                "number": it.get("number"),
                "difficulty": it.get("difficulty"),
                "type": d.get("question_type"),
            }
    return tablo


def dogru_mu(verilen, k):
    v = normal(verilen)
    if v == normal(k["answer"]):
        return True
    return any(v == normal(alt) for alt in k["accepted"])


def paket_isle(paket):
    anahtar = anahtar_yukle(paket)
    turlar = []
    for n in (1, 2, 3):
        with open(ortak.yol("kalibrasyon", "metinsiz", "%s-tur%d.json" % (paket, n)),
                  encoding="utf-8") as f:
            turlar.append({a["id"]: a for a in json.load(f)["answers"]})

    print("\n=== %s ===" % paket)

    setler = collections.OrderedDict()
    zorluk = collections.defaultdict(lambda: [0, 0])
    dayanak_hepsi = collections.Counter()
    dayanak_isaretli = collections.Counter()
    kararli = 0
    satirlar = []

    for sid, k in anahtar.items():
        verilen = [t.get(sid, {}).get("answer") for t in turlar]
        bazlar = [t.get(sid, {}).get("basis") for t in turlar]
        dogru = [dogru_mu(v, k) for v in verilen]
        kac = sum(dogru)
        uc = kac == 3
        s = setler.setdefault(k["set"], [0, 0])
        s[0] += 1
        if uc:
            s[1] += 1
        z = zorluk[k["difficulty"]]
        z[0] += 1
        if uc:
            z[1] += 1
        for b in bazlar:
            if b:
                dayanak_hepsi[b] += 1
                if uc:
                    dayanak_isaretli[b] += 1
        if len({tuple(normal(v)) for v in verilen}) == 1:
            kararli += 1
        satirlar.append((k["set"], k["number"], k["answer"], verilen, kac,
                         k["difficulty"], bazlar))

    toplam = len(anahtar)
    print("Toplam %d soru | tur kararliligi %d/%d (%%%.0f)"
          % (toplam, kararli, toplam, kararli / toplam * 100))

    print("\nSet bazinda:")
    for s, (t, u) in setler.items():
        print("  %-10s %2d soru  3/3 bilinen %2d  (%%%.0f)" % (s, t, u, u / t * 100))

    print("\nZorluk etiketi:")
    for z, (t, u) in sorted(zorluk.items(), key=lambda x: str(x[0])):
        print("  %-8s %2d soru  3/3 bilinen %2d  (%%%.0f)" % (z, t, u, u / t * 100))

    print("\nDayanak (tum cevaplar / yalniz isaretli sorularda):")
    for b in sorted(set(dayanak_hepsi) | set(dayanak_isaretli)):
        print("  %-20s %3d  /  %3d" % (b, dayanak_hepsi[b], dayanak_isaretli[b]))

    print("\nSoru dokumu:")
    for s, n, ans, verilen, kac, zor, bazlar in sorted(satirlar, key=lambda r: (r[0], r[1])):
        isaret = "***" if kac == 3 else ("  %d" % kac)
        print("  %s %-10s %-3s anahtar=%-28s verilen=%-45s [%s] %s"
              % (isaret, s, n, json.dumps(ans, ensure_ascii=False),
                 " | ".join(str((v or [""])[0]) for v in verilen), zor,
                 "/".join(str(b)[:4] for b in bazlar)))


def main():
    for paket in ("sentence-completion", "short-answer"):
        paket_isle(paket)
    return 0


if __name__ == "__main__":
    sys.exit(main())
