"""Capraz dogrulama 1. adim: cevap anahtari silinmis 'kor' kopya uretir.

Kullanim:  python tools/kor-kopya.py <paket-adi> [<paket-adi> ...]
Ornek:     python tools/kor-kopya.py true-false-not-given yes-no-not-given

Cikti: dogrulama/kor/ klasoru (bu klasor .gitignore'da, depoya gitmez).

Dogrulayan model bu klasordeki dosyalari okur; orijinal soru dosyalarina
ASLA bakmaz. Yoksa dogrulamanin hicbir degeri kalmaz.
"""

import datetime
import os
import sys
import shutil

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

# Cevaba veya gerekceye dair her sey silinir.
SIL = {
    "answer", "accepted_variants", "evidence", "evidence_locator", "explanation",
    "contradiction_point", "not_given_justification", "scan_note",
    "distractor_analysis", "heading_check", "feature_check", "grammar_check",
    "uniqueness_check", "answer_point_id", "turn_index", "distractor_used",
    "difficulty", "status", "flag_reason", "example", "notes",
    # E5/E6 elden gecirme + yeniden uretim alanlari: eski cevabi, kanit cumlesini
    # ve hatta yeni dogru cevabi anlatabiliyor; kor kopyada kalmalari dogrulamayi
    # gecersiz kilar (E7 1. calistirmada fark edildi).
    "revision", "yeniden_uretim", "review_note", "flag_mechanism",
    "blind_solvable", "blind_basis", "reject_reason",
}


def temizle(o):
    if isinstance(o, dict):
        return {k: temizle(v) for k, v in o.items() if k not in SIL}
    if isinstance(o, list):
        return [temizle(v) for v in o]
    return o


def main():
    if len(sys.argv) < 2:
        print("Kullanim: python tools/kor-kopya.py <paket-adi> [...]")
        return 2

    hedef = ortak.yol("dogrulama", "kor")
    if os.path.isdir(hedef):
        shutil.rmtree(hedef)
    os.makedirs(hedef)

    # Onceki oturumun cevaplari klasorde kalirsa karsilastir.py onlari da okur ve
    # bu oturumun raporuna karistirir. Bes oturum ust uste boyle oldu; bu yuzden
    # yeni oturum baslarken varolan cevaplar arsivlenir.
    cevap = ortak.yol("dogrulama", "cevap")
    if os.path.isdir(cevap) and os.listdir(cevap):
        damga = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        arsiv = ortak.yol("dogrulama", "cevap-arsiv", damga)
        os.makedirs(os.path.dirname(arsiv), exist_ok=True)
        shutil.move(cevap, arsiv)
        print("onceki oturumun cevaplari arsivlendi -> dogrulama/cevap-arsiv/%s" % damga)
    os.makedirs(cevap, exist_ok=True)

    toplam = 0
    for paket in sys.argv[1:]:
        yollar = ortak.bul("content/**/%s.json" % paket)
        if not yollar:
            print("UYARI: '%s' icin dosya bulunamadi (henuz uretilmemis olabilir)" % paket)
            continue
        for p in yollar:
            d = ortak.oku(p)
            ad = p.replace("/", "__")
            with open(os.path.join(hedef, ad), "w", encoding="utf-8") as f:
                import json
                json.dump({"_source": p, "_skill": d.get("skill"),
                           "_passage_id": d.get("passage_id"),
                           "_script_id": d.get("script_id"),
                           "data": temizle(d)}, f, ensure_ascii=False, indent=2)
            toplam += 1
            print("  kor kopya:", p)

    print("\n%d dosya kor kopyalandi -> dogrulama/kor/" % toplam)
    print("Cevaplarini dogrulama/cevap/ altina ayni dosya adiyla yaz.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
