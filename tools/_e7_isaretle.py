"""E7 1. calistirma (cevap anahtari) sonucu: uyusmayan 2 soruyu yeniden isaretler.

Kaynak rapor: content/DOGRULAMA/yeniden-olcum-cevap-anahtari.json
Yanlis alarmlar (accepted_variants zaten kapsiyor) isaretlenmez.
Hicbir soru silinmez; yalniz status + flag_reason degisir.
"""
import json

HEDEFLER = [
    ("content/reading/practice/matching-headings.json", "15",
     "E7 cevap anahtari olcumu (2026-08-08): kor cozum ii dedi, anahtar v. A12 F "
     "paragrafi icin ii ('The internal make-up of the daytime naps') ve v ('What the "
     "length of the rest did not explain') YALNIZ bu paragrafa demirleniyor ve ikisi de "
     "paragrafin birer yarisini kapsiyor (bilesim + sonucsuzluk). AC3/14'teki oruntuyle "
     "ayni: celdirici baska paragrafa demirli degil. ii'yi baska bir paragrafa "
     "baglanabilir bir ifadeyle degistirmek soruyu tartismasiz yapar."),
    ("content/reading/tests/GT1/summary-completion.json", "40",
     "E7 cevap anahtari olcumu (2026-08-08): kor cozum 'reductions' dedi, anahtar "
     "'prevention'. Kanit cumlesi iki adayi da tasiyor: 'has focused on collection and "
     "disposal rather than PREVENTION, and that meaningful REDUCTIONS will depend on "
     "tackling the specific items'. Ozet cumlesi 'real ___ will depend on campaigns' "
     "kalibiyla pasajin 'reductions will depend on' obegini nerdeyse birebir yankiladigi "
     "icin 'reductions' en az 'prevention' kadar savunulabilir. En az maliyetli duzeltme: "
     "accepted_variants listesine 'reductions' eklemek ya da boslugu tek adayli bir "
     "kaliba tasimak."),
]

for yol, numara, gerekce in HEDEFLER:
    d = json.load(open(yol, encoding="utf-8"))
    items = []
    for g in (d.get("groups") or [{"items": d.get("items") or []}]):
        items += g.get("items") or []
    it = next(i for i in items if str(i.get("number")) == numara)
    eski = it.get("status")
    it["status"] = "flagged"
    it["flag_reason"] = gerekce
    with open(yol, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print("%s #%s: %s -> flagged" % (yol, numara, eski))
