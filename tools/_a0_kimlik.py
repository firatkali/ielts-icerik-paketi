"""A0: content/ ve passages/ altindaki her soru/pasaj dosyasina "exam": "ielts"
alanini schema_version'dan hemen sonra ekler. Tek calistirmalik, mekanik iş;
soru metnine, cevaba, aciklamaya dokunmaz.

Kullanim: python tools/_a0_kimlik.py
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402


def hedef_dosyalar():
    out = set()
    for desen in ("content/**/*.json", "passages/**/*.json"):
        for p in ortak.bul(desen):
            if "/DOGRULAMA/" in p:
                continue
            out.add(p)
    return sorted(out)


def exam_ekle(d):
    """schema_version'dan hemen sonra 'exam': 'ielts' eklenmis yeni sozluk dondurur."""
    yeni = {}
    eklendi = False
    for k, v in d.items():
        yeni[k] = v
        if k == "schema_version":
            yeni["exam"] = "ielts"
            eklendi = True
    if not eklendi:
        yeni = {"exam": "ielts", **yeni}
    return yeni


def main():
    eklendi, zaten_var, atlandi = [], [], []

    for p in hedef_dosyalar():
        try:
            d = ortak.oku(p)
        except Exception as e:
            atlandi.append("%s: okunamadi - %s" % (p, e))
            continue

        if not isinstance(d, dict):
            atlandi.append("%s: en ust duzey nesne (dict) degil, atlandi" % p)
            continue

        if "exam" in d:
            zaten_var.append(p)
            continue

        ortak.yaz(p, exam_ekle(d))
        eklendi.append(p)

    print("=== A0: kimlik alani (exam) ===")
    print("exam eklendi: %d" % len(eklendi))
    print("zaten vardi:  %d" % len(zaten_var))
    print("atlandi:      %d" % len(atlandi))
    if atlandi:
        print("\nAtlanan dosyalar:")
        for a in atlandi:
            print("  -", a)

    return 0


if __name__ == "__main__":
    sys.exit(main())
