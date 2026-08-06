"""CAPRAZ-90 4. adim: kor cevaplara gore orijinal sorulari isaretler.

Kullanim: python tools/_capraz_isaretle.py

Uyusan sorulara "status": "verified", uyusmayan veya dusuk guvenlilere
"status": "flagged" + "flag_reason" ekler. Hicbir soruyu silmez.

Dosyalari yeniden serilestirmek yerine metin duzeyinde ekleme yapar; boylece
elle kurulmus bicimlendirme (kisa dizilerin tek satirda durmasi gibi) bozulmaz.
Her soru nesnesi son alan olarak "difficulty" ile bittigi icin ekleme noktasi
o satirdir; sayi tutmazsa dosyaya dokunulmaz.
"""

import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

DIFF = re.compile(r'^([ \t]*)"difficulty": "[^"]*"(,?)[ \t]*$', re.M)


def normal(a):
    if a is None:
        return []
    if not isinstance(a, list):
        a = [a]
    return sorted(str(x).strip().lower() for x in a)


def kacis(s):
    return json.dumps(s, ensure_ascii=False)


def main():
    cevaplar = sorted(glob.glob(os.path.join(ortak.yol("dogrulama", "cevap"), "*.json")))
    if not cevaplar:
        print("HATA: dogrulama/cevap/ bos.")
        return 1

    toplam_v = toplam_f = 0
    for cy in cevaplar:
        with open(cy, encoding="utf-8") as f:
            c = json.load(f)
        src = c["_source"]
        d = ortak.oku(src)
        cev = {str(a["number"]): a for a in c["answers"]}
        sorular = ortak.sorular(d)

        tam = ortak.yol(src)
        with open(tam, encoding="utf-8") as f:
            metin = f.read()
        yerler = list(DIFF.finditer(metin))
        if len(yerler) != len(sorular):
            print("ATLANDI (%s): difficulty satiri %d, soru %d"
                  % (src, len(yerler), len(sorular)))
            continue

        v = fl = 0
        parcalar = []
        son = 0
        for m, it in zip(yerler, sorular):
            a = cev.get(str(it.get("number")))
            parcalar.append(metin[son:m.end()])
            son = m.end()
            if a is None:
                continue
            girinti = m.group(1)
            ayni = normal(a.get("answer")) == normal(it.get("answer"))
            guven = a.get("confidence", 5)
            if ayni and guven >= 3:
                ek = '%s"status": "verified"' % girinti
                v += 1
            else:
                if not ayni:
                    sebep = ("Capraz dogrulamada %s yerine %s cevaplandi (guven %d). %s"
                             % ("/".join(it.get("answer") or []),
                                "/".join(a.get("answer") or []), guven,
                                a.get("reasoning", "")))
                else:
                    sebep = ("Capraz dogrulamada ayni cevap verildi ama guven dusuk (%d). %s"
                             % (guven, a.get("reasoning", "")))
                ek = ('%s"status": "flagged",\n%s"flag_reason": %s'
                      % (girinti, girinti, kacis(sebep)))
                fl += 1
            # difficulty satirinda virgul yoksa ekle, sonra yeni alanlari yaz.
            if not m.group(2):
                parcalar[-1] += ","
            parcalar.append("\n" + ek)
        parcalar.append(metin[son:])
        yeni = "".join(parcalar)

        json.loads(yeni)  # bozulmadigini dogrula
        with open(tam, "w", encoding="utf-8") as f:
            f.write(yeni)

        toplam_v += v
        toplam_f += fl
        print("%-58s verified=%d flagged=%d" % (src, v, fl))
    print("TOPLAM verified=%d flagged=%d" % (toplam_v, toplam_f))
    return 0


if __name__ == "__main__":
    sys.exit(main())
