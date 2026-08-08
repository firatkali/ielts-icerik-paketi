# 3. duzeltme (A4) tani scripti — SADECE S1 + S3 kumeleri.
# S2 bu oturumda SAKLI kume: asagidaki KUMELER listesi disindaki hicbir ornek okunmaz.
# Kullanim: python tools/_a4_alt.py <tur_no> [<tur_no> ...]
import json, os, re, sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OLCUM = os.path.join(KOK, "kalibrasyon", "olcum")
GORUNUR = ("S1", "S3")          # S2 aciklmaz
KUMELER = json.load(open(os.path.join(OLCUM, "kumeler.json"), encoding="utf-8"))
IZINLI = {k for g in GORUNUR for k in KUMELER[g]}


def gercek_bandlar(tur):
    """Gercek bandlari yalniz izinli kumelerin RAPOR-tur<N>-<KUME>.md dosyalarindan okur."""
    out = {}
    for g in GORUNUR:
        yol = os.path.join(OLCUM, "RAPOR-tur%d-%s.md" % (tur, g))
        if not os.path.exists(yol):
            continue
        for satir in open(yol, encoding="utf-8"):
            p = [h.strip() for h in satir.strip().strip("|").split("|")]
            if len(p) >= 5 and p[0] in IZINLI:
                try:
                    out[p[0]] = float(p[3])
                except ValueError:
                    pass
    return out


def puanlamalar(tur, kod):
    d = os.path.join(OLCUM, "tur%d" % tur)
    for ad in sorted(os.listdir(d)):
        if re.match(r"^%s-\d+\.json$" % re.escape(kod), ad):
            yield json.load(open(os.path.join(d, ad), encoding="utf-8"))


def ortalama(xs):
    return sum(xs) / len(xs) if xs else None


def dilim(gercek):
    if gercek >= 7:
        return ">= 7"
    if gercek >= 5:
        return "5 - 6,5"
    return "<= 4,5"


def tur_raporu(tur):
    gercek = gercek_bandlar(tur)
    if not gercek:
        print("tur %d: izinli kumede olcum yok" % tur)
        return
    kova = {}
    print("\n=== tur %d — kumeler %s (n=%d ornek) ===" % (tur, "+".join(GORUNUR), len(gercek)))
    for kod, g in sorted(gercek.items(), key=lambda kv: kv[1]):
        kayitlar = list(puanlamalar(tur, kod))
        if not kayitlar:
            continue
        genel = ortalama([k["predicted_band"] for k in kayitlar])
        olcut = {}
        for k in kayitlar:
            for c in k.get("criteria", []):
                olcut.setdefault(c["name"], []).append(c["band"])
        d = kova.setdefault(dilim(g), {"genel": [], "olcut": {}})
        d["genel"].append(genel - g)
        for ad, bl in olcut.items():
            d["olcut"].setdefault(ad, []).append(ortalama(bl) - g)
        print("  %-12s gercek %.1f  verilen %.2f  sapma %+0.2f   %s" % (
            kod, g, genel, genel - g,
            "  ".join("%s %+0.2f" % (ad[:4], ortalama(bl) - g) for ad, bl in sorted(olcut.items()))))
    print("  --- band araligi x olcut (olcut bandi - gercek genel band) ---")
    for ad in ("<= 4,5", "5 - 6,5", ">= 7"):
        if ad not in kova:
            continue
        d = kova[ad]
        print("  %-8s n=%-2d genel %+0.2f | %s" % (
            ad, len(d["genel"]), ortalama(d["genel"]),
            "  ".join("%s %+0.2f" % (k[:4], ortalama(v)) for k, v in sorted(d["olcut"].items()))))


for t in (sys.argv[1:] or ["3", "4", "5"]):
    tur_raporu(int(t))
