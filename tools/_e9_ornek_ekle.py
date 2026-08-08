"""OPUS5-E9: alt band (<=4,5) yazma ornegini kaynaktan dokup JSON'a yazar.

Kaynak: referans/ielts-academic-writing-example-responses-to-parts-1-and-2-with-
band-scores-and-examiner-comments.pdf, sayfa 3 (Sample Academic Writing Part 1,
Candidate Response 2 - Band 4).

Cevap metni ve sinav gorevlisi yorumu PDF'in metin katmanindan BIREBIR okunur
(elle dokum yok), bu yuzden dokum sirasinda sessizce duzeltme riski yoktur.
Cikti dosyasi .gitignore'dadir; bu betik metni ekrana yazdirmaz.

Kullanim: python tools/_e9_ornek_ekle.py
"""
import json
import pathlib
import re

import fitz

PDF = pathlib.Path(
    "referans/ielts-academic-writing-example-responses-to-parts-1-and-2-"
    "with-band-scores-and-examiner-comments.pdf"
)
CIKTI = pathlib.Path("kalibrasyon/ornekler/yazma/AC-ER-T1-B.json")


def satirlar(sayfa):
    """Sayfadaki metin satirlarini (y, metin) olarak sirali dondurur."""
    out = []
    for blok in sayfa.get_text("dict")["blocks"]:
        if blok.get("type") != 0:
            continue
        for satir in blok["lines"]:
            metin = "".join(s["text"] for s in satir["spans"]).strip()
            if metin:
                out.append((satir["bbox"][1], metin))
    return sorted(out)


def birlestir(parcalar):
    return re.sub(r"\s+", " ", " ".join(parcalar)).strip()


sayfa = fitz.open(PDF)[2]  # 0-tabanli: sayfa 3
satir = satirlar(sayfa)

basliklar = {m: y for y, m in satir}
y_cevap = basliklar["Candidate Response 2"]
y_yorum = basliklar["Examiner comment"]
y_band = basliklar["Band 4"]

cevap = birlestir([m for y, m in satir if y_cevap < y < y_yorum])
yorum = birlestir([m for y, m in satir if y > y_band])

veri = {
    "exam": "ielts",
    "schema_version": "1.0",
    "kind": "official_scored_sample",
    "skill": "writing",
    "module": "academic",
    "task": 1,
    "task_code": "ER1",
    "script": "B",
    "task_prompt": None,
    "task_prompt_note": (
        "Gorev metni kaynak belgede YOK: belge yalnizca aday cevaplarini, band puanini ve "
        "sinav gorevlisi yorumunu iceriyor, gorev sayfasi (rubric + grafik) konmamis. "
        "Uydurulmadi, null birakildi. Puanlamada asagidaki task_context_reconstructed "
        "kullanilmali ve rekonstruksiyon oldugu bilinerek degerlendirilmeli."
    ),
    "task_context_reconstructed": (
        "Academic Writing Task 1. Sutun grafigi: bir ulkede cocuklarin okula gidis-gelis icin "
        "yaptigi yillik yolculuk sayisi (milyon), 1990 ve 2010 karsilastirmasi; ulasim turleri "
        "araba, yuruyerek, bisiklet, yuruyerek+otobus, sadece otobus. REKONSTRUKSIYON: bu tanim "
        "gorev sayfasindan degil, ayni belgedeki band 6'lik 1. aday cevabinin ve sinav gorevlisi "
        "yorumunun icerdigi verilerden cikarildi; resmi gorev metni degildir."
    ),
    "band": 4.0,
    "examiner_comment": yorum,
    "response_text": cevap,
    "word_count": len(cevap.split()),
    "transcription_suspect": False,
    "transcription_notes": [
        "Kaynak PDF taranmis el yazisi degil, DIZGILI METIN: cevap ve yorum PDF'in metin "
        "katmanindan birebir alindi (bu betik), elle dokum yapilmadi; dokum sirasinda sessizce "
        "duzeltme riski yok.",
        "Paragraf bolunmesi: sayfada satir araligi bastan sona duzgun (~11,9 pt), bos satir yok. "
        "Kaynak cevabi tek blok olarak dizmis, bu yuzden tek paragraf yazildi. Adayin orijinal "
        "el yazisindaki paragraf bolunmesi bu belgeden geri getirilemiyor.",
        "Tuzak kontrolu (band <= 6 kurali): belirgin yazim/dilbilgisi hatasi ~18, esigin (0-1) "
        "cok uzerinde -> transcription_suspect false. Yazim: 'statistice' (statistics), 'tripe' "
        "(trips), 'mad' (made), 'to years' (two), 'end from' (and from), 'highset' (highest), "
        "'contrest' (contrast), 'priod' (period), 'care' (car). Dilbilgisi: 'the children use "
        "bus/car/cycling' (5 kez, fiil bicimi), 'are the by far highset' (sozcuk dizilisi), "
        "'significant higher' (belirtec), 'while,' (yanlis virgul). Buyuk/kucuk harf: cumle "
        "ortasinda 'The' (3 kez) ve 'Twice', cumle basinda kucuk 'children' ve 'overall'. Sayi "
        "bicimi tutarsiz (13 million / 12,000,000) ve ayni veri iki farkli sayiyla veriliyor "
        "(yuruyerek 1990: once 13 million, sonra 12,000,000).",
        "Sinav gorevlisi yorumu ayni sayfadan birebir alindi; 'Band 4' satiri yorumun hemen "
        "ustunde duruyor.",
    ],
    "source": (
        "ielts.org resmi belgesi (ielts-academic-writing-example-responses-to-parts-1-and-2-"
        "with-band-scores-and-examiner-comments.pdf), sayfa 3 - Sample Academic Writing Part 1, "
        "Candidate Response 2"
    ),
}

CIKTI.write_text(json.dumps(veri, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"{CIKTI.name}: band {veri['band']}, {veri['word_count']} kelime, "
      f"yorum {len(yorum.split())} kelime")
