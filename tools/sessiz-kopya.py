"""E8 1. adim: dinleme SENARYOSU VE cevap anahtari olmadan soru kopyasi uretir.

Kullanim:  python tools/sessiz-kopya.py <paket-adi> [<paket-adi> ...]
           python tools/sessiz-kopya.py multiple-choice --secim=tek
Ornek:     python tools/sessiz-kopya.py multiple-choice multiple-choice-multi

Cikti: dogrulama/sessiz/ (gitignore'da, depoya gitmez).

`metinsiz-kopya.py`nin dinleme surumudur; ONUN YERINI ALMAZ. Iki fark:

1. Okumada gizlenen "parca" pasajdi, burada SES METNI (content/listening/scripts/).
   Bu yuzden senaryo izleri de silinir: script_id, turn_index, answer_point_id,
   context_line, section, visual.
2. Dosya adlari okuma/dinlemede ayni (multiple-choice.json her ikisinde var).
   `metinsiz-kopya.py` skill != "reading" olani bilerek atlar; bu script tersini
   yapar, skill != "listening" olani atlar. Ikisi ayri klasore yazar, kimse
   kimsenin olcumunu ezmez.

`--secim=tek` yalniz tek cevapli, `--secim=cok` yalniz cok cevapli soruyu alir
(cok cevapli = select_count > 1 ya da "31-32" gibi aralikli numara). Cevap
anahtarina bakmadan ayirt edilir.
"""

import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

# Kor kopyada silinenler + dinleme senaryo izleri.
SIL = {
    # cevap ve gerekce
    "answer", "accepted_variants", "evidence", "evidence_locator", "explanation",
    "contradiction_point", "not_given_justification", "scan_note",
    "distractor_analysis", "distractor_used", "heading_check", "feature_check",
    "grammar_check", "uniqueness_check", "useful_language",
    # denetim/isaretleme alanlari (cevabi acik edebiliyor)
    "difficulty", "difficulty_flags", "status", "flag_reason", "flag_mechanism",
    "blind_solvable", "blind_basis", "revision", "yeniden_uretim", "review_note",
    "generated_by", "example", "notes",
    # DINLEME senaryo izleri: sorunun ses metnindeki yerini/kimligini verir
    "script_id", "turn_index", "answer_point_id", "transcript", "script",
    "context_line", "section", "visual",
    # okuma tarafindan sizabilecek parca izleri (ayni sema paylasiliyor)
    "passage_id", "passage_title", "passage", "source",
}

# Cok cevapli soruyu tek cevapliden ayiran alan (cevaba bakmadan).
TEK = "tek"
COK = "cok"
HEPSI = "hepsi"


def temizle(o):
    if isinstance(o, dict):
        return {k: temizle(v) for k, v in o.items() if k not in SIL}
    if isinstance(o, list):
        return [temizle(v) for v in o]
    return o


def cok_cevapli(it):
    """select_count>1 ya da aralikli numara => cok cevapli soru."""
    sc = it.get("select_count")
    if isinstance(sc, int) and sc > 1:
        return True
    return len(ortak.numaralar(it)) > 1


def kapsayicilar(d):
    """Dosyanin kendisi ya da gruplari: soruyu tasiyan her kap."""
    return list(d.get("groups") or [d])


def govde_bloklari(d):
    """stem_block / table / box / options — sorunun kendisi, senaryonun degil.

    Dinlemede not-tamamlama iskeleti (`stem_block`) ve tablo (`table`) sorunun
    govdesidir; kopyaya girmezse o tipler bos govdeyle olculur ve cikan sonuc
    sorunun degil kopyanin eksigi olur. Kutu/secenek havuzu da ayni sebeple
    tasinir; hangi soru numaralarini kapsadigi yazilir.
    """
    out = []
    for kap in kapsayicilar(d):
        blok = {}
        for alan in ("instructions", "word_limit", "stem_block", "table",
                     "box", "options", "allow_repeat"):
            if kap.get(alan) is not None:
                blok[alan] = temizle(kap[alan])
        if not blok:
            continue
        blok["items"] = [it.get("number") for it in (kap.get("items") or [])] or None
        out.append(blok)
    return out


def main():
    paketler = [a for a in sys.argv[1:] if not a.startswith("--")]
    secim = HEPSI
    for a in sys.argv[1:]:
        if a.startswith("--secim="):
            secim = a.split("=", 1)[1]
    if not paketler or secim not in (TEK, COK, HEPSI):
        print("Kullanim: python tools/sessiz-kopya.py <paket-adi> [...] [--secim=tek|cok|hepsi]")
        return 2

    hedef = ortak.yol("dogrulama", "sessiz")
    if os.path.isdir(hedef):
        shutil.rmtree(hedef)
    os.makedirs(hedef)

    toplam_dosya, toplam_soru, toplam_numara, atlanan = 0, 0, 0, 0
    for paket in paketler:
        yollar = [p for p in ortak.bul("content/**/%s.json" % paket)
                  if "/DOGRULAMA/" not in p and "/scripts/" not in p]
        if not yollar:
            print("UYARI: '%s' icin dosya bulunamadi." % paket)
            continue
        for p in yollar:
            d = ortak.oku(p)
            if d.get("skill") != "listening":
                # Okuma bu adimin kapsami disinda; metinsiz-* olcumu onu yapiyor.
                print("  atlandi (dinleme degil):", p)
                continue
            kimlikli = []
            for it in ortak.sorular(d):
                if secim == TEK and cok_cevapli(it):
                    atlanan += 1
                    continue
                if secim == COK and not cok_cevapli(it):
                    atlanan += 1
                    continue
                kimlikli.append({
                    "id": "%s-%s" % (d.get("set_id", os.path.basename(p)), it.get("number")),
                    "number": it.get("number"),
                    "question": temizle(it),
                })
            if not kimlikli:
                print("  atlandi (secime uyan soru yok):", p)
                continue
            ad = p.replace("/", "__")
            with open(os.path.join(hedef, ad), "w", encoding="utf-8") as f:
                json.dump({
                    "_source": p,
                    "_question_type": d.get("question_type"),
                    "_test": d.get("test_id"),
                    "instructions": d.get("instructions"),
                    "word_limit": d.get("word_limit"),
                    "blocks": govde_bloklari(d),
                    "items": kimlikli,
                }, f, ensure_ascii=False, indent=2)
            toplam_dosya += 1
            toplam_soru += len(kimlikli)
            toplam_numara += sum(len(ortak.numaralar(it["question"])) or 1
                                 for it in kimlikli)
            print("  sessiz kopya: %s (%d kalem / %d numara)"
                  % (p, len(kimlikli), sum(len(ortak.numaralar(it["question"])) or 1
                                           for it in kimlikli)))

    print("\n%d dosya, %d kalem, %d numara -> dogrulama/sessiz/"
          % (toplam_dosya, toplam_soru, toplam_numara))
    if atlanan:
        print("secim='%s' disinda kalan kalem: %d" % (secim, atlanan))
    print("Cevaplarini kalibrasyon/sessiz/<paket>-tur<N>.json olarak yaz.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
