"""kalibrasyon/ornekler/yazma/*.json dosyalarindaki `word_count` alanini
`response_text` uzerinden sayarak gunceller (goz karari deger birakilmasin).

Sayim kurali: metin bosluklara (satir sonlari dahil) gore bolunur, bos parcalar
atilir. Kalan her parca bir kelime sayilir.

Kullanim: python tools/_a1_kelime_say.py [klasor]
Not: klasor .gitignore'da; bu betik yalniz sayiyi gunceller, metni yazdirmaz.
"""
import json, pathlib, sys

klasor = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "kalibrasyon/ornekler/yazma")
for yol in sorted(klasor.glob("*.json")):
    veri = json.loads(yol.read_text(encoding="utf-8"))
    metin = veri.get("response_text") or veri.get("transcript") or ""
    sayi = len(metin.split())
    eski = veri.get("word_count")
    veri["word_count"] = sayi
    yol.write_text(json.dumps(veri, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{yol.name}: {eski} -> {sayi} (band {veri.get('band')})")
