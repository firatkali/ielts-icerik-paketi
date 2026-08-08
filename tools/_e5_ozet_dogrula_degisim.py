# -*- coding: utf-8 -*-
"""E5 / 8. calistirma - korunan alanlarin HEAD ile karsilastirilmasi.

Sinanan: answer / accepted_variants / evidence / evidence_locator /
difficulty / passage_id; ust duzeyde instructions / word_limit /
question_type / word_bank; soru numaralari ve soru sayisi; her boslugun
numarasinin soru metninde ve ozet govdesinde hala durmasi; duzeltilmeyen
sorularin metninin harfi harfine ayni kalmasi.

stem_block bu calistirmada bilerek degisiyor (ozet govdesi bir sizinti
yuzeyi), o yuzden ust alan olarak degil, bosluk isaretleri ve yalniz
beklenen parcalarin degismis olmasi uzerinden sinaniyor.
"""
import json, os, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402
import _e5_ozet_elden_gecir as EG  # noqa: E402

ALANLAR = ["answer", "accepted_variants", "evidence", "evidence_locator",
           "difficulty", "passage_id"]
UST_ALANLAR = ["instructions", "word_limit", "question_type", "passage_id",
               "word_bank", "set_id", "skill"]


def head_surumu(yol):
    ham = subprocess.run(["git", "show", "HEAD:%s" % yol],
                         cwd=ortak.KOK, stdout=subprocess.PIPE, check=True)
    return json.loads(ham.stdout.decode("utf-8"))


def main():
    dosyalar = sorted(set(list(EG.DUZELT) + list(EG.ELE) + list(EG.DOKUN)))
    hata = kontrol = toplam_soru = 0

    for yol in dosyalar:
        eski = head_surumu(yol)
        yeni = ortak.oku(yol)
        duz = EG.DUZELT.get(yol, {})

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

        # --- ozet/not govdesi: her bosluk isareti yerinde mi, yalniz beklenen
        #     parcalar mi degisti
        e_sb, y_sb = eski.get("stem_block"), yeni.get("stem_block")
        if e_sb is not None:
            for n in sorted(y_it):
                kontrol += 1
                if "(%d)" % n in e_sb and "(%d)" % n not in y_sb:
                    print("BOSLUK GOVDEDEN DUSTU: %s #%s" % (yol, n))
                    hata += 1
            beklenen = e_sb
            for a, b in EG.STEM.get(yol, []):
                beklenen = beklenen.replace(a, b, 1)
            kontrol += 1
            if beklenen != y_sb:
                print("GOVDEDE BEKLENMEYEN DEGISIKLIK: %s" % yol)
                hata += 1

        for n in sorted(e_it):
            for a in ALANLAR:
                kontrol += 1
                if e_it[n].get(a) != y_it[n].get(a):
                    print("KORUNAN ALAN HATASI: %s #%s %s" % (yol, n, a))
                    hata += 1

            kontrol += 1
            e_p = e_it[n].get("prompt") or ""
            y_p = y_it[n].get("prompt") or ""
            isaret = "(%d)" % n if "(%d)" % n in e_p else "........"
            if yeni.get("question_type") != "short_answer" and isaret not in y_p:
                print("BOSLUK SORU METNINDEN DUSTU: %s #%s" % (yol, n))
                hata += 1

            kontrol += 1
            if n not in duz and e_p != y_p:
                print("DUZELTILMEYEN SORUNUN METNI DEGISTI: %s #%s" % (yol, n))
                hata += 1

            if n in duz:
                kontrol += 1
                rev = y_it[n].get("revision") or {}
                if rev.get("onceki_prompt") != e_p:
                    print("ONCEKI METIN KAYDEDILMEDI: %s #%s" % (yol, n))
                    hata += 1
                kontrol += 1
                if y_it[n].get("blind_solvable") is not None:
                    print("BLIND_SOLVABLE SIFIRLANMADI: %s #%s" % (yol, n))
                    hata += 1
                kontrol += 1
                if y_it[n].get("status") != "verified":
                    print("DUZELTILEN SORU VERIFIED DEGIL: %s #%s" % (yol, n))
                    hata += 1
                # duzeltilen soru metni govdede aynen gecmeli (tablo haric)
                if y_sb is not None:
                    kontrol += 1
                    # Bazi dosyalarda soru metni govde cumlesinin kirpilmis
                    # halidir (HEAD'de de oyle); son noktayi disarida birak.
                    if y_p.lower().rstrip(" .") not in y_sb.lower():
                        print("YENI METIN GOVDEYLE UYUSMUYOR: %s #%s" % (yol, n))
                        hata += 1

            if n in EG.ELE.get(yol, {}):
                kontrol += 1
                if y_it[n].get("status") != "rejected" or \
                        not y_it[n].get("reject_reason"):
                    print("ELENEN SORU EKSIK ISARETLI: %s #%s" % (yol, n))
                    hata += 1

            if n in EG.DOKUN.get(yol, {}):
                kontrol += 1
                if y_it[n].get("status") != "flagged" or \
                        not y_it[n].get("review_note"):
                    print("DOKUNULMAYAN SORU EKSIK NOTLU: %s #%s" % (yol, n))
                    hata += 1

    print("dosya: %d - soru: %d" % (len(dosyalar), toplam_soru))
    print("sinanan alan: %d" % kontrol)
    print("KORUNAN ALAN HATASI: %d" % hata)
    if hata:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
