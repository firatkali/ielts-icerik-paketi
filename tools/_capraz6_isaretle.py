"""4. adim: karsilastirma raporuna gore orijinal dosyalari isaretler.

Dosyalari yeniden serilestirmez; her sorunun son alani olan "difficulty"
satirinin ardina alanlari metin duzeyinde ekler, boylece bicimlendirme
(kompakt diziler, tek satirlik nesneler) oldugu gibi kalir.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

RAPOR = "content/DOGRULAMA/bilgi-eslestirme.json"
PAT = re.compile(r'("difficulty": "[a-z]+")\n(\s*)\}')

# Bu oturumda uyusmayan veya dusuk guvenli soru cikmadi.
GEREKCE = {}


def main():
    rapor = ortak.oku(RAPOR)
    isaretli = {}
    for r in rapor["sonuclar"]:
        for d in r.get("detay", []):
            isaretli.setdefault(r["file"], set()).add(str(d["number"]))

    v_top = f_top = 0
    for r in rapor["sonuclar"]:
        src = r["file"]
        tam = ortak.yol(src)
        with open(tam, encoding="utf-8") as f:
            raw = f.read()
        numaralar = [str(it.get("number")) for it in ortak.sorular(json.loads(raw))]
        bayrakli = isaretli.get(src, set())
        sira = iter(numaralar)

        def ekle(m):
            nonlocal v_top, f_top
            n = next(sira)
            girinti = m.group(2) + "  "
            if n in bayrakli:
                f_top += 1
                ek = ('%s"status": "flagged",\n%s"flag_reason": %s'
                      % (girinti, girinti,
                         json.dumps(GEREKCE[(src, n)], ensure_ascii=False)))
            else:
                v_top += 1
                ek = '%s"status": "verified"' % girinti
            return "%s,\n%s\n%s}" % (m.group(1), ek, m.group(2))

        yeni, sayi = PAT.subn(ekle, raw)
        if sayi != len(numaralar):
            print("ATLANDI (eslesme sayisi tutmadi):", src)
            continue
        json.loads(yeni)  # gecerlilik kontrolu
        with open(tam, "w", encoding="utf-8", newline="") as f:
            f.write(yeni)
        print("guncellendi:", src)

    print("\nverified: %d | flagged: %d" % (v_top, f_top))


if __name__ == "__main__":
    main()
