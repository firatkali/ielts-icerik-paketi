import json

def norm(s):
    return " ".join(s.split())

qs = json.load(open("content/reading/practice/multiple-choice.json", encoding="utf-8"))
passages = {}
sayac = {"soru": 0, "uyari": 0}

for item in qs["items"]:
    pid = item["passage_id"]
    if pid not in passages:
        p = json.load(open(f"passages/academic/{pid}.json", encoding="utf-8"))
        passages[pid] = norm(" ".join(t["text"] for t in p["paragraphs"]))
    full = passages[pid]
    sayac["soru"] += 2 if item["select_count"] == 2 else 1

    ev = norm(item["evidence"])
    for part in [x.strip() for x in ev.split(". ") if x.strip()]:
        if part not in full:
            sayac["uyari"] += 1
            print(f"#{item['number']} ({pid}): KANIT EKSIK -> {part[:90]}")

    for o in item["options"]:
        if norm(o["text"]).rstrip(".") in full:
            sayac["uyari"] += 1
            print(f"#{item['number']}: !! secenek {o['letter']} pasajda birebir geciyor")

    letters = {o["letter"] for o in item["options"]}
    beklenen = letters - set(item["answer"])
    gelen = set(item["distractor_analysis"].keys())
    if beklenen != gelen:
        sayac["uyari"] += 1
        print(f"#{item['number']}: !! celdirici anahtarlari uyusmuyor: {sorted(beklenen)} / {sorted(gelen)}")

    if len(item["options"]) != (7 if item["select_count"] == 2 else 4):
        sayac["uyari"] += 1
        print(f"#{item['number']}: !! secenek sayisi yanlis")
    if len(item["answer"]) != item["select_count"]:
        sayac["uyari"] += 1
        print(f"#{item['number']}: !! cevap sayisi select_count ile uyusmuyor")
    if item["answer"] != sorted(item["answer"]):
        sayac["uyari"] += 1
        print(f"#{item['number']}: !! cevap harfleri alfabetik degil")

    kelime = len(item["prompt"].split()) + sum(len(o["text"].split()) for o in item["options"])
    if kelime > 60:
        sayac["uyari"] += 1
        print(f"#{item['number']}: !! kok+secenek {kelime} kelime (sinir 60)")

    lens = [len(o["text"].split()) for o in item["options"]]
    if max(lens) > 2 * min(lens):
        sayac["uyari"] += 1
        print(f"#{item['number']}: !! uzunluk dengesiz: {lens}")

    yok = sum(1 for g in item["distractor_analysis"].values() if g.startswith("Cazip ama yok"))
    if yok > 1:
        sayac["uyari"] += 1
        print(f"#{item['number']}: !! 'pasajda gecmiyor' gerekcesi {yok} kez")

    turler = {g.split(" —")[0] for g in item["distractor_analysis"].values()}
    if len(turler) < 3:
        sayac["uyari"] += 1
        print(f"#{item['number']}: !! celdirici turu cesitliligi {len(turler)}: {sorted(turler)}")

    print(f"#{item['number']} ({pid}) cevap {item['answer']} - kelime {kelime}, uzunluk {lens}, tur {len(turler)}")

harfler = [item["answer"] for item in qs["items"]]
for a, b in zip(harfler, harfler[1:]):
    if set(a) & set(b):
        sayac["uyari"] += 1
        print(f"!! ust uste ayni harf: {a} / {b}")

print(f"\nToplam sayilan soru: {sayac['soru']} (hedef 15) - uyari: {sayac['uyari']}")
