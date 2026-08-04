# Gecici yardimci: L5 senaryolarinda turn_index / word_count / estimated_minutes doldurur.
# Is bitince silinir.
import json
import re
import sys
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
KLASOR = KOK / "content" / "listening" / "scripts"


def kelime_say(metin: str) -> int:
    # Sadece harf/rakam iceren parcalar kelime sayilir; tek basina tire/uzun tire sayilmaz.
    return len([p for p in metin.split() if re.search(r"[A-Za-z0-9]", p)])


def l4_kontrol():
    for s in range(1, 5):
        d = json.loads((KLASOR / f"L4-S{s}.json").read_text(encoding="utf-8"))
        gercek = sum(kelime_say(t["text"]) for t in d["turns"])
        print(f"  L4-S{s}: kayitli={d['word_count']} hesaplanan={gercek}")


def isle():
    hata = 0
    for s in range(1, 5):
        yol = KLASOR / f"L5-S{s}.json"
        d = json.loads(yol.read_text(encoding="utf-8"))
        metinler = [t["text"] for t in d["turns"]]
        tam = "\n".join(metinler)

        for ap in d["answer_points"]:
            q = ap["quote"]
            adet = tam.count(q)
            if adet == 0:
                print(f"HATA {ap['id']}: alinti metinde YOK -> {q[:60]}")
                hata += 1
                continue
            if adet > 1:
                print(f"HATA {ap['id']}: alinti {adet} kez geciyor -> {q[:60]}")
                hata += 1
                continue
            idx = [i for i, m in enumerate(metinler) if q in m]
            if len(idx) != 1:
                print(f"HATA {ap['id']}: alinti replik siniri asiyor")
                hata += 1
                continue
            ap["turn_index"] = idx[0]
            if ap["speaker"] != d["turns"][idx[0]]["speaker"]:
                print(f"HATA {ap['id']}: speaker uyusmuyor "
                      f"({ap['speaker']} != {d['turns'][idx[0]]['speaker']})")
                hata += 1

        wc = sum(kelime_say(m) for m in metinler)
        d["word_count"] = wc
        d["estimated_minutes"] = round(wc / 150, 1)
        yol.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"L5-S{s}: kelime={wc} dakika={d['estimated_minutes']} "
              f"replik={len(d['turns'])} bilgi_noktasi={len(d['answer_points'])}")
    return hata


if __name__ == "__main__":
    print("L4 kelime sayimi dogrulamasi (yontem kontrolu):")
    l4_kontrol()
    print()
    sys.exit(1 if isle() else 0)
