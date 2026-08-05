"""Resmi referans belgelerini ielts.org'dan indirir.

Kullanim:  python tools/indir.py

Inen dosyalar referans/ klasorune gider ve .gitignore sayesinde depoya YUKLENMEZ.
Telifli olduklari icin depoda tutulmuyorlar; her makinede bir kez indirilirler.
"""

import html as html_mod
import os
import re
import sys
import urllib.request

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

BASE = "https://ielts.org/cdn/"

DOSYALAR = [
    "Sample-tests/ielts-academic-reading-sample-tasks-2023.pdf",
    "Sample-tests/ielts-academic-writing-sample-tasks-2023.pdf",
    "Sample-tests/ielts-general-reading-sample-tasks-2023.pdf",
    "Sample-tests/ielts-general-training-writing-sample-tasks-2023.pdf",
    "ielts-sample-tests/ielts-listening-sample-tasks-2023.pdf",
    "ielts-sample-tests/ielts-speaking-sample-tasks-2023.pdf",
    "ielts-sample-tests/ielts-listening/ielts-listening-answer-sheet-sample.pdf",
    "ielts-sample-tests/ielts-reading/ielts-reading-answer-sheet-sample.pdf",
    "computer-delivered-sample-tests-academic-writing/ielts-academic-writing-example-responses-to-parts-1-and-2-with-band-scores-and-examiner-comments.pdf",
    "computer-delivered-sample-tests-general-training-writing/ielts-general-training-writing-example-responses-to-parts-1-and-2-with-band-scores-and-examiner-comments.pdf",
    "computer-delivered-sample-tests-academic-reading/ielts-academic-reading-computer-delivered-identifying-information-true-flase-not-given-answer-key.pdf",
    "computer-delivered-sample-tests-academic-reading/ielts-academic-reading-computer-delivered-matching-features-answer-key.pdf",
    "computer-delivered-sample-tests-academic-reading/ielts-academic-reading-computer-delivered-matching-sentence-endings-answer-key.pdf",
    "computer-delivered-sample-tests-academic-reading/ielts-academic-reading-computer-delivered-multiple-choice-more-than-one-answer-answer-key.pdf",
    "computer-delivered-sample-tests-academic-reading/ielts-academic-reading-computer-delivered-multiple-choice-one-answer-answer-key.pdf",
    "computer-delivered-sample-tests-academic-reading/ielts-academic-reading-computer-delivered-note-completion-answer-key.pdf",
    "computer-delivered-sample-tests-academic-reading/ielts-academic-reading-computer-delivered-sentence-completion-answer-key.pdf",
    "computer-delivered-sample-tests-academic-reading/ielts-academic-reading-computer-delivered-summary-completion-selecting-from-list-of-words-or-phrases-answer-key.pdf",
    "computer-delivered-sample-tests-academic-reading/ielts-academic-reading-computer-delivered-summary-completion-selecting-words-from-text-answer-key.pdf",
    "computer-delivered-sample-tests-academic-reading/ielts-academic-reading-computer-delivered-table-completion-answer-key.pdf",
    "computer-delivered-sample-tests-general-training-reading/ielts-general-training-reading-computer-delivered-identifying-information-true-false-not-given-answer-key.pdf",
    "computer-delivered-sample-tests-general-training-reading/ielts-general-training-reading-computer-delivered-matching-features-answer-key.pdf",
    "computer-delivered-sample-tests-general-training-reading/ielts-general-training-reading-computer-delivered-matching-information-answer-key.pdf",
    "computer-delivered-sample-tests-general-training-reading/ielts-general-training-reading-computer-delivered-multiple-choice-answer-key.pdf",
    "computer-delivered-sample-tests-general-training-reading/ielts-general-training-reading-computer-delivered-note-completion-answer-key.pdf",
    "computer-delivered-sample-tests-general-training-reading/ielts-general-training-reading-computer-delivered-sentence-completion-answer-key.pdf",
    "computer-delivered-sample-tests-general-training-reading/ielts-general-training-reading-computer-delivered-summary-completion-answer-key.pdf",
    "computer-delivered-sample-tests-listening/ielts-listening-computer-delivered-flow-chart-completion-answer-key.pdf",
    "computer-delivered-sample-tests-listening/ielts-listening-computer-delivered-flow-chart-completion-transcript.pdf",
    "computer-delivered-sample-tests-listening/ielts-listening-computer-delivered-multiple-choice-more-than-one-answer-answer-key.pdf",
    "computer-delivered-sample-tests-listening/ielts-listening-computer-delivered-multiple-choice-more-than-one-answer-transcript.pdf",
    "computer-delivered-sample-tests-listening/ielts-listening-computer-delivered-multiple-choice-one-answer-answer-key.pdf",
    "computer-delivered-sample-tests-listening/ielts-listening-computer-delivered-multiple-choice-one-answer-transcript.pdf",
    "computer-delivered-sample-tests-listening/ielts-listening-computer-delivered-note-completion-answer-key.pdf",
    "computer-delivered-sample-tests-listening/ielts-listening-computer-delivered-note-completion-transcript.pdf",
    "computer-delivered-sample-tests-listening/ielts-listening-computer-delivered-plan-map-diagram-labelling-answer-key.pdf",
    "computer-delivered-sample-tests-listening/ielts-listening-computer-delivered-plan-map-diagram-labelling-transcript.pdf",
    "computer-delivered-sample-tests-listening/ielts-listening-computer-delivered-sentence-completion-answer-key.pdf",
    "computer-delivered-sample-tests-listening/ielts-listening-computer-delivered-sentence-completion-transcript.pdf",
    "computer-delivered-sample-tests-listening/ielts-listening-computer-delivered-short-answer-answer-key.pdf",
    "computer-delivered-sample-tests-listening/ielts-listening-computer-delivered-short-answer-transcript.pdf",
    "computer-delivered-sample-tests-listening/ielts-listening-computer-delivered-table-completion-answer-key.pdf",
    "computer-delivered-sample-tests-listening/ielts-listening-computer-delivered-table-completion-transcript.pdf",
]


# Konusma bolumunun band puanli ornekleri PDF degil, normal bir web sayfasinda
# duruyor: 12 ornek, tam dokum + sinav gorevlisi yorumu + band puani. Puanlama
# ayarinin konusma ayagi tamamen buna dayaniyor.
SAYFALAR = [
    ("https://ielts.org/organisations/ielts-for-organisations/understanding-ielts-scoring/"
     "resources-for-setting-your-ielts-scores", "konusma-band-ornekleri.txt"),
]


def _metne_cevir(ham):
    """Sayfayi kaba bicimde duz metne cevirir - ayiklamayi model yapacak."""
    m = ham.decode("utf-8", "replace")
    m = re.sub(r"(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", m)
    m = re.sub(r"(?i)<br\s*/?>", "\n", m)
    m = re.sub(r"(?i)</(p|div|li|h[1-6]|tr|section)>", "\n", m)
    m = re.sub(r"(?s)<[^>]+>", " ", m)
    m = html_mod.unescape(m)
    m = re.sub(r"[ \t\xa0]+", " ", m)
    m = re.sub(r"\n\s*\n\s*\n+", "\n\n", m)
    return "\n".join(s.strip() for s in m.splitlines()).strip()


def sayfalari_indir(hedef):
    inen, atlanan, hata = 0, 0, []
    for url, ad in SAYFALAR:
        cikti = os.path.join(hedef, ad)
        if os.path.exists(cikti) and os.path.getsize(cikti) > 5000:
            atlanan += 1
            continue
        try:
            istek = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(istek, timeout=60) as r:
                veri = r.read()
            metin = _metne_cevir(veri)
            if len(metin) < 5000 or "Band" not in metin:
                hata.append(ad + " (sayfa beklenen icerigi tasimiyor)")
                continue
            with open(cikti, "w", encoding="utf-8") as f:
                f.write(metin)
            inen += 1
            print("  indi:", ad)
        except Exception as e:
            hata.append("%s (%s)" % (ad, e))
    return inen, atlanan, hata


def main():
    hedef = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                         "referans")
    os.makedirs(hedef, exist_ok=True)

    inen, atlanan, hata = 0, 0, []
    for yol in DOSYALAR:
        ad = os.path.basename(yol)
        cikti = os.path.join(hedef, ad)
        if os.path.exists(cikti) and os.path.getsize(cikti) > 5000:
            atlanan += 1
            continue
        url = BASE + yol
        try:
            istek = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(istek, timeout=60) as r:
                veri = r.read()
            if len(veri) < 5000 or not veri.startswith(b"%PDF"):
                hata.append(ad + " (PDF degil)")
                continue
            with open(cikti, "wb") as f:
                f.write(veri)
            inen += 1
            print("  indi:", ad)
        except Exception as e:
            hata.append("%s (%s)" % (ad, e))

    s_inen, s_atlanan, s_hata = sayfalari_indir(hedef)
    inen += s_inen
    atlanan += s_atlanan
    hata += s_hata

    print()
    print("Inen: %d | Zaten vardi: %d | Hata: %d" % (inen, atlanan, len(hata)))
    print("Toplam beklenen: %d" % (len(DOSYALAR) + len(SAYFALAR)))
    if hata:
        print("\nInemeyenler:")
        for h in hata:
            print("  -", h)
        print("\nBu scripti tekrar calistir; inenler atlanir, sadece eksikler denenir.")
    return 0 if not hata else 1


if __name__ == "__main__":
    sys.exit(main())
