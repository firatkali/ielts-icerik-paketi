"""Dinleme senaryolarinda turn_index butunlugu kontrolu.

Kullanim:  python3 tools/turn-index-kontrol.py [--yaz]

Uc sey bakar:
  1. Her senaryonun tur sayisi, `denetim/TUR-SAYILARI.json` icindeki referansla ayni mi.
     Senaryoya cumle EKLEMEK/CIKARMAK o senaryoya bagli butun sorularin turn_index'ini
     kaydirir ve hicbir sema testinde gorunmez; bu dosya o kaymayi yakalar.
  2. Her sorunun turn_index'i senaryonun tur araligi icinde mi.
  3. Her sorunun evidence dizgisi, isaret ettigi TURUN icinde birebir geciyor mu.

`--yaz` referans dosyasini gunceller. Senaryoya bilerek tur eklendiginde/cikarildiginda
kullanilir; aksi halde ELLE calistirilmaz.

Bilinen yanlis pozitif YOK (evidence karsilastirmasi birebir dizgi); cevap dizgileri
burada karsilastirilmaz, cunku rakam/kod seste harfle soylenebiliyor
("nine fifteen" <-> 9.15, "G W nine four one" <-> GW941).
"""

import glob
import json
import os
import sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF = os.path.join(KOK, "denetim", "TUR-SAYILARI.json")


def senaryolar():
    out = {}
    for f in sorted(glob.glob(os.path.join(KOK, "content/listening/scripts/*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        out[d["script_id"]] = d
    return out


def sorular():
    pats = ["content/listening/practice/*.json", "content/listening/tests/*/*.json"]
    for pat in pats:
        for f in sorted(glob.glob(os.path.join(KOK, pat))):
            d = json.load(open(f, encoding="utf-8"))
            rel = os.path.relpath(f, KOK)
            if d.get("groups"):
                for g in d["groups"]:
                    for it in g.get("items", []):
                        sid = it.get("script_id") or g.get("script_id") or d.get("script_id")
                        yield rel, sid, it
            else:
                for it in d.get("items", []):
                    sid = it.get("script_id") or d.get("script_id")
                    yield rel, sid, it


def main():
    yaz = "--yaz" in sys.argv
    sc = senaryolar()
    simdi = {k: len(v["turns"]) for k, v in sc.items()}

    if yaz or not os.path.exists(REF):
        json.dump(simdi, open(REF, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("referans yazildi: denetim/TUR-SAYILARI.json (%d senaryo)" % len(simdi))
        if yaz:
            return 0

    ref = json.load(open(REF, encoding="utf-8"))
    hata = 0

    print("=== TUR SAYILARI ===")
    for sid in sorted(simdi):
        bekl = ref.get(sid)
        ok = bekl == simdi[sid]
        if not ok:
            hata += 1
        print("  %-6s %3d/%-3s %s" % (sid, simdi[sid], bekl if bekl is not None else "?", "" if ok else "<-- KAYDI"))
    for sid in sorted(set(ref) - set(simdi)):
        hata += 1
        print("  %-6s KAYIP (referansta var, senaryo yok)" % sid)

    print("\n=== turn_index / evidence ===")
    n = arali = ev = 0
    for paket, sid, it in sorular():
        n += 1
        d = sc.get(sid)
        if d is None:
            arali += 1
            print("  %s #%s -> senaryo %s YOK" % (paket, it.get("number"), sid))
            continue
        ti = it.get("turn_index")
        if ti is None or not (0 <= ti < len(d["turns"])):
            arali += 1
            print("  %s #%s -> turn_index %s, senaryo %s'de %d tur var" % (paket, it.get("number"), ti, sid, len(d["turns"])))
            continue
        e = (it.get("evidence") or "").strip()
        if e and e not in d["turns"][ti]["text"]:
            ev += 1
            print("  %s #%s [%s tur %d] -> evidence turda gecmiyor" % (paket, it.get("number"), sid, ti))
    print("  kalem: %d | turn_index arali disi: %d | evidence tutmayan: %d" % (n, arali, ev))

    toplam = hata + arali + ev
    print("\n=== SONUC: %d hata ===" % toplam)
    return 1 if toplam else 0


if __name__ == "__main__":
    sys.exit(main())
