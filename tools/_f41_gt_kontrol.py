import json

def norm(s):
    return " ".join(s.split())

for pid, qfile in [("G03", "content/reading/tests/GT1/multiple-choice.json"),
                   ("G04", "content/reading/tests/GT2/multiple-choice.json")]:
    passage = json.load(open(f"passages/general/{pid}.json", encoding="utf-8"))
    full = norm(" ".join(t["text"] for t in passage["texts"]))
    qs = json.load(open(qfile, encoding="utf-8"))
    for item in qs["items"]:
        ev = norm(item["evidence"])
        parts = [p.strip() for p in ev.split(". ") if p.strip()]
        ok_all = True
        for p in parts:
            if p not in full:
                ok_all = False
                print(f"{qfile} #{item['number']}: EKSIK -> {p[:80]}")
        if ok_all:
            print(f"{qfile} #{item['number']}: kanit birebir OK")
        for o in item["options"]:
            if norm(o["text"]).rstrip(".") in full:
                print(f"  !! secenek {o['letter']} pasajda birebir geciyor")
        letters = {o["letter"] for o in item["options"]}
        expected = letters - set(item["answer"])
        got = set(item["distractor_analysis"].keys())
        if expected != got:
            print(f"  !! celdirici anahtarlari uyusmuyor: beklenen {sorted(expected)}, gelen {sorted(got)}")
        words = len(item["prompt"].split()) + sum(len(o["text"].split()) for o in item["options"])
        print(f"  kok+secenek kelime: {words}")
        lens = [len(o["text"].split()) for o in item["options"]]
        if max(lens) > 2 * min(lens):
            print(f"  !! uzunluk dengesiz: {lens}")
