# -*- coding: utf-8 -*-
"""E5 / 5. calistirma - korunan alanlarin HEAD ile karsilastirilmasi.

Sinanan: answer / accepted_variants / evidence / evidence_locator /
word_limit / instructions / soru numaralari / soru sayisi; kelime bankasinda
harf kumesi, harf sirasi ve DOGRU seceneklerin metinleri; her boslugun
numarasinin ozet govdesinde hala durmasi.
"""

import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

DOSYALAR = [
    "content/reading/tests/AC2/summary-completion.json",
    "content/reading/tests/AC3/summary-completion.json",
    "content/reading/tests/AC4/summary-completion.json",
]

ALANLAR = ["answer", "accepted_variants", "evidence", "evidence_locator"]
UST_ALANLAR = ["instructions", "word_limit", "question_type", "passage_id"]


def head_surumu(yol):
    ham = subprocess.run(["git", "show", "HEAD:%s" % yol],
                         cwd=ortak.KOK, stdout=subprocess.PIPE, check=True)
    return json.loads(ham.stdout.decode("utf-8"))


def main():
    hata = 0
    kontrol = 0

    for yol in DOSYALAR:
        eski = head_surumu(yol)
        yeni = ortak.oku(yol)

        for a in UST_ALANLAR:
            kontrol += 1
            if eski.get(a) != yeni.get(a):
                print("UST ALAN DEGISTI: %s %s" % (yol, a))
                hata += 1

        e_ban = eski.get("word_bank") or []
        y_ban = yeni.get("word_bank") or []
        kontrol += 1
        if [o["letter"] for o in e_ban] != [o["letter"] for o in y_ban]:
            print("BANKA HARF KUMESI/SIRASI DEGISTI: %s" % yol)
            hata += 1

        e_it = {it["number"]: it for it in ortak.sorular(eski)}
        y_it = {it["number"]: it for it in ortak.sorular(yeni)}

        kontrol += 1
        if sorted(e_it) != sorted(y_it):
            print("SORU NUMARALARI DEGISTI: %s" % yol)
            hata += 1

        # dogru seceneklerin metinleri korunmali
        dogru = set()
        for it in y_it.values():
            for c in it.get("answer") or []:
                dogru.add(c)
        for o_e, o_y in zip(e_ban, y_ban):
            if o_e["letter"] not in dogru:
                continue
            kontrol += 1
            if o_e["text"] != o_y["text"]:
                print("DOGRU SECENEK METNI DEGISTI: %s %s"
                      % (yol, o_e["letter"]))
                hata += 1

        for n in sorted(e_it):
            for a in ALANLAR:
                kontrol += 1
                if e_it[n].get(a) != y_it[n].get(a):
                    print("KORUNAN ALAN HATASI: %s #%s %s" % (yol, n, a))
                    hata += 1
            kontrol += 1
            if "(%d)" % n not in (yeni.get("stem_block") or ""):
                print("BOSLUK GOVDEDEN DUSTU: %s #%s" % (yol, n))
                hata += 1
            kontrol += 1
            if "(%d)" % n not in (y_it[n].get("prompt") or ""):
                print("BOSLUK SORU METNINDEN DUSTU: %s #%s" % (yol, n))
                hata += 1
            # soru metni ozet govdesinin bir parcasi olmali; AC3 #37 ve #40
            # HEAD'de de kisaltilmis alintiyla duruyor, o yuzden olcut
            # "HEAD'de ortusuyorduysa simdi de ortusmeli" biciminde.
            kontrol += 1
            e_ok = e_it[n]["prompt"] in (eski.get("stem_block") or "")
            y_ok = y_it[n]["prompt"] in (yeni.get("stem_block") or "")
            if e_ok and not y_ok:
                print("SORU METNI GOVDEYLE ORTUSMUYOR: %s #%s" % (yol, n))
                hata += 1

    print("sinanan alan: %d" % kontrol)
    print("KORUNAN ALAN HATASI: %d" % hata)
    if hata:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
