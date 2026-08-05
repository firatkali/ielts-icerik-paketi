"""B1 1. adim: okuma parcasi VE cevap anahtari olmadan soru kopyasi uretir.

Kullanim:  python tools/metinsiz-kopya.py <paket-adi> [<paket-adi> ...]
Ornek:     python tools/metinsiz-kopya.py true-false-not-given

Cikti: dogrulama/metinsiz/ (gitignore'da, depoya gitmez).

Kor kopyadan farki: burada parcaya dair HER IZ de silinir (passage_id, script_id,
parcadan alinti tasiyan alanlar). Amac, sorunun parcaya bakmadan bilinip
bilinemedigini olcmek; parcanin kimligi bile bilinirse model konuyu tahmin eder.
"""

import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

# Kor kopyada silinenlerin tamami + parca izleri.
SIL = {
    "answer", "accepted_variants", "evidence", "evidence_locator", "explanation",
    "contradiction_point", "not_given_justification", "scan_note",
    "distractor_analysis", "heading_check", "feature_check", "grammar_check",
    "uniqueness_check", "answer_point_id", "turn_index", "distractor_used",
    "difficulty", "status", "flag_reason", "example", "notes",
    "passage_id", "passage_title", "script_id", "source", "passage",
    "transcript", "useful_language", "blind_solvable", "blind_basis",
    "difficulty_flags",
}


def temizle(o):
    if isinstance(o, dict):
        return {k: temizle(v) for k, v in o.items() if k not in SIL}
    if isinstance(o, list):
        return [temizle(v) for v in o]
    return o


def main():
    if len(sys.argv) < 2:
        print("Kullanim: python tools/metinsiz-kopya.py <paket-adi> [...]")
        return 2

    hedef = ortak.yol("dogrulama", "metinsiz")
    if os.path.isdir(hedef):
        shutil.rmtree(hedef)
    os.makedirs(hedef)

    toplam_dosya, toplam_soru = 0, 0
    for paket in sys.argv[1:]:
        yollar = [p for p in ortak.bul("content/**/%s.json" % paket)
                  if "/DOGRULAMA/" not in p]
        if not yollar:
            print("UYARI: '%s' icin dosya bulunamadi." % paket)
            continue
        for p in yollar:
            d = ortak.oku(p)
            if d.get("skill") != "reading":
                # Dinleme bu adimin kapsami disinda; yanlislikla girmesin.
                print("  atlandi (okuma degil):", p)
                continue
            sorular = ortak.sorular(d)
            # Her soruya kararli bir kimlik ver: model cevabini bununla yazacak.
            kimlikli = []
            for it in sorular:
                kimlikli.append({
                    "id": "%s-%s" % (d.get("set_id", os.path.basename(p)), it.get("number")),
                    "number": it.get("number"),
                    "question": temizle(it),
                })
            ad = p.replace("/", "__")
            with open(os.path.join(hedef, ad), "w", encoding="utf-8") as f:
                json.dump({
                    "_source": p,
                    "_question_type": d.get("question_type"),
                    "instructions": d.get("instructions"),
                    "options": d.get("options"),
                    "items": kimlikli,
                }, f, ensure_ascii=False, indent=2)
            toplam_dosya += 1
            toplam_soru += len(kimlikli)
            print("  metinsiz kopya: %s (%d soru)" % (p, len(kimlikli)))

    print("\n%d dosya, %d soru -> dogrulama/metinsiz/" % (toplam_dosya, toplam_soru))
    print("Cevaplarini kalibrasyon/metinsiz/<paket>-tur<N>.json olarak yaz.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
