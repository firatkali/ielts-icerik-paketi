# -*- coding: utf-8 -*-
"""E5 / 6. calistirma - olcum (salt okur, HEAD ile karsilastirir).

Iki olcu:

1. **Pasaja ozgu capa.** Duzeltme kuralinin sinandigi yer burasi: duzeltilen
   TRUE/FALSE ifadesi, KANIT CUMLESINDE gecen bir sayiya, olcuye ya da ozel
   ada dayaniyor mu? Dayaniyorsa cevap dunya bilgisinden degil yalniz o
   cumleden cikar. Sayilir: ifadedeki rakam / sayi sozcugu / buyuk harfle
   baslayan ad kumesinin kanit cumlesiyle kesisimi.

2. **NOT GIVEN ifadelerinin eksen orani.** Ifadenin icerik sozcuklerinin kaci
   pasajda geciyor. Eksen disi bir ayrinti ekleyen ifade dusuk oran verir.
   Sozcuk ortusune dayandigi icin kaba bir olcu: baska sozcuklerle
   capalanmis (paraphrase) bir ifadeyi eksen disi sanabilir, o yuzden yalniz
   bu calistirmada yeniden yazilan alti NOT GIVEN icin bakilir.
"""
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402
import _e5_tf_elden_gecir as EG  # noqa: E402

DURAK = set("""a an the of to in on at for from by with and or but not that this
these those is are was were be been being it its as than then so such have has
had do does did will would can could may might must shall should each every any
all both other another same own more most less least very much many few about
into over under after before during while when where which who whom whose what
how why if because although though yet still even also just only there they
them their his her he she we our us you your""".split())

SAYI = set("""one two three four five six seven eight nine ten eleven twelve
twenty thirty forty fifty sixty seventy eighty ninety hundred thousand half
quarter third fourth fifth single double dozen""".split())


def head_surum(yol):
    ham = subprocess.check_output(["git", "show", "HEAD:" + yol], cwd=ortak.KOK)
    return json.loads(ham.decode("utf-8"))


def sozcukler(metin):
    return [w for w in re.findall(r"[a-z]+", (metin or "").lower())
            if w not in DURAK and len(w) > 2]


KAPSAM = set("""all always every everyone everything never none nothing only
most best worst least largest smallest highest lowest entirely completely
exclusively solely""".split())


def sayisal_capa(metin):
    """Ifadedeki sayisal/olcusel capalar: rakam ya da sayi sozcugu."""
    metin = metin or ""
    out = set(re.findall(r"\d+", metin))
    out |= {w for w in re.findall(r"[a-z]+", metin.lower()) if w in SAYI}
    return out


_PASAJ = {}


def pasaj_metni(pid):
    if pid not in _PASAJ:
        _PASAJ[pid] = ""
        for klasor in ("academic", "general"):
            yol = os.path.join(ortak.KOK, "passages", klasor, "%s.json" % pid)
            if os.path.exists(yol):
                with open(yol, encoding="utf-8") as f:
                    d = json.load(f)
                parca = [p.get("text", "") for p in (d.get("paragraphs") or [])]
                parca += [t.get("text", "") for t in (d.get("texts") or [])]
                _PASAJ[pid] = " ".join(parca).lower()
    return _PASAJ[pid]


def soru_bul(veri, numara):
    for g, it in ortak.kumeli_sorular(veri):
        if it["number"] == numara:
            return g, it
    return None, None


def main():
    tf_anahtar = [k for k in EG.DUZELTME
                  if k[0].endswith("true-false-not-given.json")]

    print("== 1) sayisal capa (duzeltilen TRUE/FALSE ifadeleri)")
    print("   Not: duzeltmelerin yalniz bir bolumu sayiya capalandi; geri "
          "kalani yon, rol, neden gibi yapisal capalar kullaniyor ve bu olcu "
          "onlari gormez. Elle denetim ELDEN-GECIRME.md'deki tabloda.")
    once = sonra = toplam = 0
    for yol, no in sorted(tf_anahtar):
        y_veri = ortak.oku(yol)
        e_veri = head_surum(yol)
        _, y = soru_bul(y_veri, no)
        _, e = soru_bul(e_veri, no)
        if (y.get("answer") or [""])[0] == "NOT GIVEN":
            continue
        toplam += 1
        e_capa = sorted(sayisal_capa(e.get("prompt")))
        y_capa = sorted(sayisal_capa(y.get("prompt")))
        once += 1 if e_capa else 0
        sonra += 1 if y_capa else 0
        print("   %-46s #%-3s once=%-16s sonra=%s"
              % (yol.split("reading/")[-1], no,
                 ",".join(e_capa) or "-", ",".join(y_capa) or "-"))
    print("   sayisal capa tasiyan ifade: %d -> %d (%d uzerinden)"
          % (once, sonra, toplam))

    print()
    print("== 2) kapsam/mutlaklik sozcugu tasiyan TFNG ifadeleri (butun tip)")
    for surum, yukle in (("ONCE (HEAD)", head_surum), ("SONRA", ortak.oku)):
        kip = {}
        for yol in sorted({k[0] for k in tf_anahtar}
                          | {p for p in ortak.soru_dosyalari()
                             if p.endswith("true-false-not-given.json")}):
            veri = yukle(yol)
            for _g, it in ortak.kumeli_sorular(veri):
                c = (it.get("answer") or ["?"])[0]
                kip.setdefault(c, [0, 0])
                kip[c][0] += 1
                ham = set(re.findall(r"[a-z]+", (it.get("prompt") or "").lower()))
                if ham & KAPSAM:
                    kip[c][1] += 1
        print("   -- %s" % surum)
        for c in sorted(kip):
            print("      %-10s %2d / %2d" % (c, kip[c][1], kip[c][0]))

    print()
    print("== 3) yeniden yazilan NOT GIVEN ifadelerinin eksen orani")
    print("   Not: sozcuk ortusune dayanan kaba bir olcu; baska sozcuklerle "
          "capalanmis bir ifadeyi eksen disi sanabilir.")
    for yol, no in sorted(tf_anahtar):
        y_veri = ortak.oku(yol)
        e_veri = head_surum(yol)
        g, y = soru_bul(y_veri, no)
        _, e = soru_bul(e_veri, no)
        if (y.get("answer") or [""])[0] != "NOT GIVEN":
            continue
        pid = y.get("passage_id") or (g or {}).get("passage_id") \
            or y_veri.get("passage_id")
        metin = pasaj_metni(pid)

        def oran(p):
            ws = sozcukler(p)
            if not ws or not metin:
                return 0.0
            return sum(1 for w in ws if w[:6] in metin) / float(len(ws))

        print("   %-46s #%-3s %s  once=%.2f  sonra=%.2f"
              % (yol.split("reading/")[-1], no, pid,
                 oran(e.get("prompt")), oran(y.get("prompt"))))


if __name__ == "__main__":
    main()
