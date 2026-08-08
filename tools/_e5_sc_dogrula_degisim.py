# -*- coding: utf-8 -*-
"""E5 / 7. calistirma - korunan alanlarin HEAD ile karsilastirilmasi.

Sinanan: answer / accepted_variants / evidence / evidence_locator /
difficulty / passage_id; ust duzeyde instructions / word_limit /
question_type; soru numaralari ve soru sayisi; her boslugun numarasinin
soru metninde hala durmasi; kisa cevap dosyasinda soru metninin soru
biciminde kalmasi.
"""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402
import _e5_sc_elden_gecir as EG  # noqa: E402

ALANLAR = ["answer", "accepted_variants", "evidence", "evidence_locator",
           "difficulty", "passage_id"]
UST_ALANLAR = ["instructions", "word_limit", "question_type", "passage_id",
               "word_bank", "stem_block"]


def head_surumu(yol):
    ham = subprocess.run(["git", "show", "HEAD:%s" % yol],
                         cwd=ortak.KOK, stdout=subprocess.PIPE, check=True)
    return json.loads(ham.stdout.decode("utf-8"))


def main():
    dosyalar = sorted({k[0] for k in
                       list(EG.DUZELT) + list(EG.ELE) + list(EG.DOKUNMA)})
    hata = 0
    kontrol = 0
    toplam_soru = 0

    for yol in dosyalar:
        eski = head_surumu(yol)
        yeni = ortak.oku(yol)

        for a in UST_ALANLAR:
            kontrol += 1
            if eski.get(a) != yeni.get(a):
                print("UST ALAN DEGISTI: %s %s" % (yol, a))
                hata += 1

        e_it = {it["number"]: it for it in ortak.sorular(eski)}
        y_it = {it["number"]: it for it in ortak.sorular(yeni)}
        toplam_soru += len(y_it)

        kontrol += 1
        if sorted(e_it) != sorted(y_it):
            print("SORU NUMARALARI DEGISTI: %s" % yol)
            hata += 1

        for n in sorted(e_it):
            for a in ALANLAR:
                kontrol += 1
                if e_it[n].get(a) != y_it[n].get(a):
                    print("KORUNAN ALAN HATASI: %s #%s %s" % (yol, n, a))
                    hata += 1

            # Bosluk isareti soru metninde durmali. AC3/AC4 dosyalari HEAD'de
            # de numarasiz "........" kullaniyor, o yuzden olcut "HEAD'de
            # nasilsa simdi de oyle" biciminde.
            if yeni.get("question_type") != "short_answer":
                kontrol += 1
                e_p = e_it[n].get("prompt") or ""
                y_p = y_it[n].get("prompt") or ""
                isaret = "(%d)" % n if "(%d)" % n in e_p else "........"
                if isaret not in y_p:
                    print("BOSLUK SORU METNINDEN DUSTU: %s #%s" % (yol, n))
                    hata += 1

            # dokunulmayan ve elenen sorularin metni hic degismemeli
            kontrol += 1
            if (yol, n) not in EG.DUZELT:
                if e_it[n].get("prompt") != y_it[n].get("prompt"):
                    print("DUZELTILMEYEN SORUNUN METNI DEGISTI: %s #%s"
                          % (yol, n))
                    hata += 1

            # duzeltilen sorularda eski metin revision icinde saklanmali
            if (yol, n) in EG.DUZELT:
                kontrol += 1
                rev = y_it[n].get("revision") or {}
                if rev.get("onceki_prompt") != e_it[n].get("prompt"):
                    print("ONCEKI METIN KAYDEDILMEDI: %s #%s" % (yol, n))
                    hata += 1
                kontrol += 1
                if y_it[n].get("blind_solvable") is not None:
                    print("BLIND_SOLVABLE SIFIRLANMADI: %s #%s" % (yol, n))
                    hata += 1

            # elenen sorular dosyada numarasiyla ve gerekceyle kalmali
            if (yol, n) in EG.ELE:
                kontrol += 1
                if y_it[n].get("status") != "rejected" or \
                        not y_it[n].get("reject_reason"):
                    print("ELENEN SORU EKSIK ISARETLI: %s #%s" % (yol, n))
                    hata += 1

    print("dosya: %d - soru: %d" % (len(dosyalar), toplam_soru))
    print("sinanan alan: %d" % kontrol)
    print("KORUNAN ALAN HATASI: %d" % hata)
    if hata:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
