"""A0 adim 2: her tam test klasoru icin band esigi tanim dosyasi (_test.json)
uretir. Tek calistirmalik yardimci; tablolar prompttan aynen alinmistir,
uydurulmamistir.

Kullanim: python tools/_a0_test_tanimlari.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

NOT_METNI = (
    "Resmî ortalama tablo. Gerçek IELTS'te bu tablo her test sürümü için "
    "kaydırılır (equating). Buradaki değerler başlangıç değeridir ve canlı "
    "kullanım verisi biriktikçe TEST BAŞINA güncellenir. Koda gömülmez, bu "
    "dosyadan okunur."
)

AC = [(9.0, 39), (8.5, 37), (8.0, 35), (7.5, 33), (7.0, 30), (6.5, 27),
      (6.0, 23), (5.5, 19), (5.0, 15), (4.5, 13), (4.0, 10)]
GT = [(9.0, 40), (8.5, 39), (8.0, 37), (7.5, 36), (7.0, 34), (6.5, 32),
      (6.0, 30), (5.5, 27), (5.0, 23), (4.5, 19), (4.0, 15)]
LI = [(9.0, 39), (8.5, 37), (8.0, 35), (7.5, 32), (7.0, 30), (6.5, 26),
      (6.0, 23), (5.5, 18), (5.0, 16), (4.5, 13), (4.0, 11)]


def esikler(tablo):
    return [{"band": b, "min_correct": m} for b, m in tablo]


def tanim(test_id, skill, module, tablo):
    return {
        "exam": "ielts",
        "schema_version": "1.0",
        "test_id": test_id,
        "skill": skill,
        "module": module,
        "question_count": 40,
        "band_thresholds_source": "official_average_2023",
        "band_thresholds_note": NOT_METNI,
        "band_thresholds": esikler(tablo),
    }


def main():
    uretildi = []

    for tid in ["AC1", "AC2", "AC3", "AC4"]:
        p = "content/reading/tests/%s/_test.json" % tid
        ortak.yaz(p, tanim(tid, "reading", "academic", AC))
        uretildi.append(p)

    for tid in ["GT1", "GT2"]:
        p = "content/reading/tests/%s/_test.json" % tid
        ortak.yaz(p, tanim(tid, "reading", "general", GT))
        uretildi.append(p)

    for tid in ["L1", "L2", "L3", "L4", "L5", "L6"]:
        p = "content/listening/tests/%s/_test.json" % tid
        ortak.yaz(p, tanim(tid, "listening", "both", LI))
        uretildi.append(p)

    print("uretilen test tanim dosyasi: %d" % len(uretildi))
    for p in uretildi:
        print("  -", p)


if __name__ == "__main__":
    main()
