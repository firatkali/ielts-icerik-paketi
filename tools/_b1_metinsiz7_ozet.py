"""B1 7. calistirma ozet istatistikleri (summary-completion + flow-chart-completion).

Kullanim: python tools/_b1_metinsiz7_ozet.py

Rapor bolumunu yazmak icin gereken sayilari uretir: tur kararliligi, alt-tip
(kelime bankasi / parcadan kelime) kirilimi, zorluk etiketi iliskisi, isaretli
sorularin anahtar-cevap dokumu, dayanak dagilimlari.
"""

import collections
import glob
import json
import os

PAKETLER = ("summary-completion", "flow-chart-completion")


def oku(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def turlar(paket):
    out = []
    for n in (1, 2, 3):
        d = oku("kalibrasyon/metinsiz/%s-tur%d.json" % (paket, n))
        out.append({a["id"]: a for a in d["answers"]})
    return out


def norm(a):
    if not isinstance(a, list):
        a = [a]
    return tuple(sorted(str(x).strip().lower() for x in a))


def main():
    for paket in PAKETLER:
        rap = oku("content/DOGRULAMA/METINSIZ-%s.json" % paket)
        bil = set(rap["uc_turda_bilinen"])
        t = turlar(paket)
        print("=" * 70)
        print(paket)
        print("=" * 70)

        kararli = sum(1 for sid in t[0]
                      if norm(t[0][sid]["answer"]) == norm(t[1][sid]["answer"])
                      == norm(t[2][sid]["answer"]))
        print("Tur kararliligi: %d/%d (%%%.0f)"
              % (kararli, len(t[0]), kararli / len(t[0]) * 100))

        zor = collections.Counter()
        zor_bil = collections.Counter()
        for p in sorted(glob.glob("content/reading/**/%s.json" % paket, recursive=True)):
            d = oku(p)
            sid0 = d.get("set_id")
            wb = "LISTE" if d.get("word_bank") else "METINDEN"
            f = [it for it in d["items"] if "%s-%s" % (sid0, it["number"]) in bil]
            print("\n%-48s %-9s %2d/%2d" % (p.replace(os.sep, "/"), wb,
                                            len(f), len(d["items"])))
            for it in d["items"]:
                sid = "%s-%s" % (sid0, it["number"])
                zor[it.get("difficulty")] += 1
                if sid in bil:
                    zor_bil[it.get("difficulty")] += 1
                    print("   [X] %-3s %-16s anahtar=%-28s verilen=%s  (%s/%s)"
                          % (it["number"], it.get("difficulty"),
                             "|".join(map(str, it["answer"])),
                             "|".join(norm(t[0][sid]["answer"])),
                             t[0][sid]["basis"], it.get("blind_basis")))
                else:
                    kac = sum(1 for tt in t
                              if norm(tt[sid]["answer"]) == norm(it["answer"])
                              or any(norm(tt[sid]["answer"]) == norm(v)
                                     for v in (it.get("accepted_variants") or [])))
                    print("   [ ] %-3s %-16s anahtar=%-28s turlar=%s  (%d/3)"
                          % (it["number"], it.get("difficulty"),
                             "|".join(map(str, it["answer"])),
                             " / ".join("|".join(norm(tt[sid]["answer"])) for tt in t),
                             kac))

        print("\nZorluk: " + " · ".join(
            "%s %d/%d" % (k, zor_bil[k], zor[k]) for k in ("easy", "medium", "hard")))
        d_hepsi = collections.Counter()
        d_isaretli = collections.Counter()
        for tt in t:
            for sid, a in tt.items():
                d_hepsi[a["basis"]] += 1
                if sid in bil:
                    d_isaretli[a["basis"]] += 1
        print("Dayanak (tum): " + " · ".join("%s %d" % kv for kv in d_hepsi.most_common()))
        print("Dayanak (isaretli): " +
              " · ".join("%s %d" % kv for kv in d_isaretli.most_common()))
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
