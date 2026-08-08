# -*- coding: utf-8 -*-
"""E5 / 6. calistirma - korunan alan denetimi.

HEAD'deki surumle su anki surumu alan alan karsilastirir. Degismemesi
gerekenler:
  * her soruda: number, answer, evidence, evidence_locator, difficulty
  * baslik/secenek listelerinde: harf kumesi ve harflerin sirasi
  * baslik listelerinde: DOGRU CEVAP olan harflerin metinleri
  * dosya basina soru sayisi
"""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402
import _e5_tf_elden_gecir as EG  # noqa: E402

KORUNAN = ("number", "answer", "evidence", "evidence_locator", "difficulty")


def head_surum(yol):
    ham = subprocess.check_output(["git", "show", "HEAD:" + yol],
                                  cwd=ortak.KOK)
    return json.loads(ham.decode("utf-8"))


def secenek_listeleri(d):
    """(kap_kimligi, [(harf, metin), ...], o kaptaki dogru harfler) listesi.

    Harf listeleri kume (grup) duzeyinde tanimli oldugu icin dogru cevap
    kumesi de kume duzeyinde hesaplanir; ayni harf baska bir kumede dogru
    olabilir ve bu, bu kumedeki metni kilitlemez.
    """
    out = []
    for g in (d.get("groups") or [d]):
        ol = g.get("option_list") or d.get("option_list")
        if not ol:
            continue
        dogru = set()
        for it in (g.get("items") or []):
            for a in (it.get("answer") or []):
                if isinstance(a, str):
                    dogru.add(a)
        out.append((g.get("group_id"),
                    [(o.get("key"), o.get("text")) for o in ol.get("options") or []],
                    dogru))
    return out


def main():
    hata = 0
    sinama = 0

    for yol in EG.DOSYALAR:
        yeni = ortak.oku(yol)
        eski = head_surum(yol)

        e_sorular = {str(it["number"]): it for it in ortak.sorular(eski)}
        y_sorular = {str(it["number"]): it for it in ortak.sorular(yeni)}

        if set(e_sorular) != set(y_sorular):
            print("SORU NUMARASI DEGISTI: %s" % yol)
            hata += 1
            continue

        for no, e in e_sorular.items():
            y = y_sorular[no]
            for alan in KORUNAN:
                sinama += 1
                if e.get(alan) != y.get(alan):
                    print("KORUNAN ALAN DEGISTI: %s #%s %s" % (yol, no, alan))
                    hata += 1

        for (gid, e_ops, dogru), (_, y_ops, _d) in zip(secenek_listeleri(eski),
                                                       secenek_listeleri(yeni)):
            sinama += 1
            if [k for k, _ in e_ops] != [k for k, _ in y_ops]:
                print("HARF KUMESI/SIRASI DEGISTI: %s %s" % (yol, gid))
                hata += 1
            for (k, et), (_, yt) in zip(e_ops, y_ops):
                if k in dogru:
                    sinama += 1
                    if et != yt:
                        print("DOGRU SECENEGIN METNI DEGISTI: %s %s %s"
                              % (yol, gid, k))
                        hata += 1

    print("sinanan alan: %d" % sinama)
    print("KORUNAN ALAN HATASI: %d" % hata)
    return 1 if hata else 0


if __name__ == "__main__":
    sys.exit(main())
