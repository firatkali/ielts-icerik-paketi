"""OPUS5-E9: kalibrasyon/ornekler/KONTROL.md tablosunun satirlarini uretir.

Yalnizca ust veri yazar (kod, gorev, band, kaynak, supheli mi) - aday cevabindan
ya da sinav gorevlisi yorumundan tek kelime almaz, cunku bu dosya depoya girer.

Kullanim: python tools/_e9_kontrol_tablo.py
"""
import json
import pathlib

KOK = pathlib.Path("kalibrasyon/ornekler")

GOREV = {
    ("writing", "academic", 1): "Yazma - Academic Task 1",
    ("writing", "academic", 2): "Yazma - Academic Task 2",
    ("writing", "general_training", 1): "Yazma - GT Task 1",
    ("writing", "general_training", 2): "Yazma - GT Task 2",
}

KAYNAK = [
    ("ielts-academic-writing-sample-tasks", "Academic Writing Sample Tasks 2023"),
    ("General Training Writing Sample Tasks", "GT Writing Sample Tasks 2023"),
    ("example-responses-to-parts-1-and-2", "Academic Writing Example Responses"),
    ("puan belirleme kaynaklari", "ielts.org band ornekleri sayfasi"),
]


def kisa_kaynak(s):
    for anahtar, ad in KAYNAK:
        if anahtar in s:
            return ad
    return s


satirlar = []
for yol in sorted(KOK.glob("*/*.json")):
    d = json.loads(yol.read_text(encoding="utf-8"))
    if d.get("kind") != "official_scored_sample":
        continue
    if d["skill"] == "speaking":
        gorev = f"Konusma - Part {d['part']}"
    else:
        gorev = GOREV[(d["skill"], d["module"], d["task"])]
    supheli = "evet" if d.get("transcription_suspect") else "hayir"
    satirlar.append((float(d["band"]), yol.stem, gorev,
                     kisa_kaynak(d.get("source", "")), supheli))

satirlar.sort(key=lambda r: (r[0], r[1]))
print("| Kod | Gorev | Gercek band | Kaynak | Supheli mi |")
print("|---|---|---|---|---|")
for band, kod, gorev, kaynak, supheli in satirlar:
    print(f"| `{kod}` | {gorev} | **{band:.1f}**".replace(".", ",", 1)
          + f" | {kaynak} | {supheli} |")
print()
print(f"Toplam {len(satirlar)} ornek; band <= 4,5 olan "
      f"{sum(1 for r in satirlar if r[0] <= 4.5)}.")
