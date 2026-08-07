"""6. calistirma (note-completion + table-completion) icin ozet istatistik."""
import json
import glob
import collections

FILES = {
    "practice": "content/reading/practice/note-completion.json",
    "AC1": "content/reading/tests/AC1/note-completion.json",
    "AC4": "content/reading/tests/AC4/note-completion.json",
    "GT1": "content/reading/tests/GT1/note-completion.json",
    "AC3": "content/reading/tests/AC3/table-completion.json",
    "GT2": "content/reading/tests/GT2/table-completion.json",
}

idmap = {}
for f in glob.glob("dogrulama/metinsiz/*.json"):
    d = json.load(open(f, encoding="utf-8"))
    for it in d["items"]:
        idmap[(d["_source"], it["number"])] = it["id"]

turlar = {}
for p in ("note-completion", "table-completion"):
    for n in (1, 2, 3):
        for a in json.load(open("kalibrasyon/metinsiz/%s-tur%d.json" % (p, n), encoding="utf-8"))["answers"]:
            turlar.setdefault(a["id"], {})[n] = (a["answer"], a["basis"])


def norm(x):
    return tuple(str(v).strip().lower() for v in x)


print("SET  toplam  3/3  oran  ayni-cevap")
for s, f in FILES.items():
    d = json.load(open(f, encoding="utf-8"))
    tot = len(d["items"])
    fl = sum(1 for it in d["items"] if it.get("blind_solvable"))
    stable = 0
    for it in d["items"]:
        i = idmap[(f, it["number"])]
        if len({norm(turlar[i][n][0]) for n in (1, 2, 3)}) == 1:
            stable += 1
    print("%-9s %3d %3d  %d%%  %d/%d" % (s, tot, fl, round(100 * fl / tot), stable, tot))

print("")
print("--- ISARETLENENLER ---")
for s, f in FILES.items():
    d = json.load(open(f, encoding="utf-8"))
    for it in d["items"]:
        if it.get("blind_solvable"):
            i = idmap[(f, it["number"])]
            print("%s %3d | key=%s | verilen=%s | basis=%s | zorluk=%s" % (
                s, it["number"], it["answer"],
                [turlar[i][n][0] for n in (1, 2, 3)],
                it["blind_basis"], it.get("difficulty")))

print("")
print("--- 2/3 TUTANLAR ---")
for s, f in FILES.items():
    d = json.load(open(f, encoding="utf-8"))
    for it in d["items"]:
        if it.get("blind_solvable"):
            continue
        i = idmap[(f, it["number"])]
        key = {str(v).strip().lower() for v in (it.get("accepted_variants") or it["answer"])}
        hit = sum(1 for n in (1, 2, 3) if norm(turlar[i][n][0])[0] in key)
        if hit >= 1:
            print("%s %3d | key=%s | verilen=%s | isabet=%d/3" % (
                s, it["number"], it["answer"], [turlar[i][n][0] for n in (1, 2, 3)], hit))

print("")
print("--- ZORLUK ---")
c = collections.Counter()
cf = collections.Counter()
for s, f in FILES.items():
    d = json.load(open(f, encoding="utf-8"))
    for it in d["items"]:
        c[it.get("difficulty")] += 1
        if it.get("blind_solvable"):
            cf[it.get("difficulty")] += 1
for k in c:
    print(k, c[k], cf[k])

print("")
print("--- BASIS (tum turlar) ---")
b = collections.Counter()
bf = collections.Counter()
flagged_ids = set()
for s, f in FILES.items():
    d = json.load(open(f, encoding="utf-8"))
    for it in d["items"]:
        if it.get("blind_solvable"):
            flagged_ids.add(idmap[(f, it["number"])])
for i, v in turlar.items():
    for n in v:
        b[v[n][1]] += 1
        if i in flagged_ids:
            bf[v[n][1]] += 1
print("tumu:", dict(b), sum(b.values()))
print("isaretlenenler:", dict(bf), sum(bf.values()))
