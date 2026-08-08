"""Konusma band orneklerini ham sayfa metninden ayiklar.

Kullanim:  python tools/konusma_ayikla.py

Girdi : referans/konusma-band-ornekleri.txt  (tools/indir.py indirir)
Cikti : kalibrasyon/ornekler/konusma/<kod>.json  (12 dosya)

Neden betik: dokum ELLE yazilirsa aday hatalarini farkinda olmadan duzeltme
riski var. Sayfa metni zaten duz metin oldugu icin kopyalama makineye
birakildi; boylece transkript sayfadaki karakterlerin birebir ayni.
Sadece sayfa gurultusu (menu satirlari, "View transcript" dugmesi) atiliyor
ve konusmaci etiketleri EXAMINER: / CANDIDATE: olarak normalize ediliyor.
"""

import json
import os
import re
import sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GIRDI = os.path.join(KOK, "referans", "konusma-band-ornekleri.txt")
CIKTI_KLASOR = os.path.join(KOK, "kalibrasyon", "ornekler", "konusma")

BASLIK = re.compile(r"^Band (\d+(?:\.\d+)?) \| (.+?), (.+)$")
BOLUM = re.compile(r"^Part (\d): (.+)$")
BITIS = "Additional resources"

# Sayfa basligi ile dokumun konusu ortusmuyorsa buraya not dusulur.
NOTLAR = {
    "Monika": ["Sayfa basligi 'Part 3: Famous people' diyor, ancak dokumun tamami "
               "hobiler ve bos zaman uzerine. Baslik kaynakta boyle; degistirilmedi."],
}


def orneleri_bul(satirlar):
    """Ham sayfa metninden (band, ad, ulke, bolum, konu, dokum, yorum) uretir."""
    yerler = [i for i, s in enumerate(satirlar) if BASLIK.match(s.strip())]
    son = next((i for i, s in enumerate(satirlar) if s.strip() == BITIS), len(satirlar))
    sinirlar = yerler + [son]

    for n, bas in enumerate(yerler):
        m = BASLIK.match(satirlar[bas].strip())
        band, ad, ulke = m.group(1), m.group(2), m.group(3)

        blok = [s.rstrip() for s in satirlar[bas + 1:sinirlar[n + 1]]]
        b = BOLUM.match(blok[0].strip())
        if not b:
            raise SystemExit("bolum satiri okunamadi: %s" % blok[0])
        bolum, konu = int(b.group(1)), b.group(2).strip()

        try:
            yorum_bas = next(i for i, s in enumerate(blok) if s.strip() == "Examiner comments")
        except StopIteration:
            raise SystemExit("'Examiner comments' bulunamadi: %s" % ad)

        dokum = [s for s in blok[1:yorum_bas] if s.strip()]
        yorum = [s.strip() for s in blok[yorum_bas + 1:] if s.strip()]
        yield band, ad, ulke, bolum, konu, dokum, yorum


def dokum_duzenle(satirlar, ad):
    """Sayfa dokumunu EXAMINER: / CANDIDATE: etiketli turlara cevirir.

    Konusmaci etiketi tasimayan satirlar bir onceki konusmacinin devamidir;
    sayfadaki satir bolunmesi korunur. Metne baska hicbir sey yapilmaz.
    """
    turler = []  # (konusmaci, [satirlar])
    ex = re.compile(r"^Examiner:\s*(.*)$")
    ay = re.compile(r"^%s:\s*(.*)$" % re.escape(ad))

    for i, ham in enumerate(satirlar):
        s = ham.strip()
        if i == 0:
            s = re.sub(r"^View transcript\s+", "", s)  # sayfa dugmesi
        m = ex.match(s)
        if m:
            turler.append(["EXAMINER", [m.group(1)] if m.group(1) else []])
            continue
        m = ay.match(s)
        if m:
            turler.append(["CANDIDATE", [m.group(1)] if m.group(1) else []])
            continue
        if not turler:
            raise SystemExit("etiketsiz ilk satir: %r" % s)
        turler[-1][1].append(s)

    parcalar = ["%s: %s" % (k, "\n".join(g).strip()) for k, g in turler]
    aday = " ".join(" ".join(g) for k, g in turler if k == "CANDIDATE")
    kelime = len([w for w in aday.split() if re.search(r"[0-9A-Za-z]", w)])
    return "\n".join(parcalar), kelime


def kod_uret(band, sayaclar):
    etiket = band.replace(".", "_")
    sayaclar[etiket] = sayaclar.get(etiket, 0) + 1
    return "SP-band%s-%d" % (etiket, sayaclar[etiket])


def main():
    if not os.path.exists(GIRDI):
        print("Kaynak yok:", GIRDI)
        print("Once 'python tools/indir.py' calistir.")
        return 1

    with open(GIRDI, encoding="utf-8") as f:
        satirlar = f.read().splitlines()

    os.makedirs(CIKTI_KLASOR, exist_ok=True)
    sayaclar, yazilan = {}, []

    for band, ad, ulke, bolum, konu, dokum, yorum in orneleri_bul(satirlar):
        kod = kod_uret(band, sayaclar)
        transkript, aday_kelime = dokum_duzenle(dokum, ad)

        kayit = {
            "exam": "ielts",
            "schema_version": "1.0",
            "kind": "official_scored_sample",
            "skill": "speaking",
            "part": bolum,
            "band": float(band),
            "examiner_comment": "\n\n".join(yorum),
            "transcript": transkript,
            "candidate_word_count": aday_kelime,
            "topic": konu.lower(),
            "source": "ielts.org — puan belirleme kaynaklari sayfasi (Band %s | %s, %s)"
                      % (band, ad, ulke),
        }
        if ad in NOTLAR:
            kayit["transcription_notes"] = NOTLAR[ad]

        yol = os.path.join(CIKTI_KLASOR, kod + ".json")
        with open(yol, "w", encoding="utf-8") as f:
            json.dump(kayit, f, ensure_ascii=False, indent=2)
            f.write("\n")
        yazilan.append((kod, float(band), bolum, aday_kelime, konu.lower(), ad, ulke))
        print("  yazildi: %-14s band %-3s part %d  %4d kelime  %s" %
              (kod, band, bolum, aday_kelime, ad))

    print("\nToplam: %d ornek (beklenen 12)" % len(yazilan))
    return 0 if len(yazilan) == 12 else 1


if __name__ == "__main__":
    sys.exit(main())
