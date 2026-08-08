"""E8: 3/3 senaryosuz bilinen sorulari KARAR DAYANAGINA gore ayirir.

Neden: "uc turda ayni dogru cevap" olcutu, gercek sizinti ile KARARLI AMA SANSLI
sezgiyi ayirmiyor (1. calistirmanin ortaya cikardigi zayif nokta). Tur dosyasindaki
`basis` alani bu ayrimi tasiyor: option_wording/general_knowledge = secenegin sozu
ya da dunya bilgisi cevabi veriyor (asil sizinti); coin_flip/guess/number_guess =
iki secenek ayni koke esit uyuyor, tutturma sanstir.

Kullanim: python tools/_e8_dayanak_capraz.py <paket> [<paket> ...]
Cikti yalniz SAYIdir; hicbir cevap degeri basilmaz.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

# Dayanagi anlamsal olan (isaretlemeye aday) vs sansa acik olan.
ANLAMSAL = {"option_wording", "general_knowledge", "logic", "cross_question"}
SANS = {"coin_flip", "guess", "number_guess"}


def main():
    paketler = sys.argv[1:]
    if not paketler:
        print("Kullanim: python tools/_e8_dayanak_capraz.py <paket> [...]")
        return 2
    for paket in paketler:
        rp = ortak.yol("content", "DOGRULAMA", "SESSIZ-%s.json" % paket)
        tp = ortak.yol("kalibrasyon", "sessiz", "%s-tur1.json" % paket)
        if not (os.path.exists(rp) and os.path.exists(tp)):
            print("eksik dosya: %s" % paket)
            continue
        with open(rp, encoding="utf-8") as f:
            r = json.load(f)
        with open(tp, encoding="utf-8") as f:
            t1 = json.load(f)
        basis = {a["id"]: a.get("basis") or "?" for a in t1["answers"]}
        bilinen = set(r["uc_turda_bilinen_k3"])

        tab = {}
        for sid in r["tur_basina_dogru"]:
            b = basis.get(sid, "?")
            v = tab.setdefault(b, [0, 0])
            v[0] += 1
            if sid in bilinen:
                v[1] += 1

        anlamsal = sum(v[1] for b, v in tab.items() if b in ANLAMSAL)
        sans = sum(v[1] for b, v in tab.items() if b in SANS)
        toplam = r["toplam_kalem"]
        print("== %s — %d kalem, 3/3 bilinen %d (%%%.1f)"
              % (paket, toplam, len(bilinen), len(bilinen) / toplam * 100))
        for b in sorted(tab):
            n, k = tab[b]
            print("   %-18s kalem %2d | 3/3 bilinen %2d | bilinmeyen %2d" % (b, n, k, n - k))
        print("   -> dayanagi ANLAMSAL 3/3: %d (%%%.1f)  |  SANSA acik 3/3: %d"
              % (anlamsal, anlamsal / toplam * 100, sans))
    return 0


if __name__ == "__main__":
    sys.exit(main())
