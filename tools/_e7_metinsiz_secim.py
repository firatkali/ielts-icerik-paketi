"""E7 2/2 (sizinti): metinsiz kopyalardan yalniz olcum hedefindeki sorulari ayiklar.

Hedef: blind_solvable null birakilmis 188 soru + AC1 TFNG #11 (E6 devri,
NOTLAR.md). Orijinal dosyalardan yalniz dosya adi + soru numarasi okunur
(cevap alanlarina bakilmaz); soru govdesi metinsiz kopyadan alinir.

Cikti: dogrulama/metinsiz-secim.json (gitignore altindaki dogrulama/).
"""
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

EK_HEDEF = {("content/reading/tests/AC1/true-false-not-given.json", "11")}

hedef = set()
for f in glob.glob('content/reading/**/*.json', recursive=True):
    d = json.load(open(f, encoding='utf-8'))
    if not isinstance(d, dict) or not (d.get('items') or d.get('groups')):
        continue
    yol = f.replace('\\', '/')
    for it in ortak.sorular(d):
        if it.get('blind_solvable', 'YOK') is None:
            hedef.add((yol, str(it.get('number'))))
hedef |= EK_HEDEF

secim = []
bulunan = set()
for mf in sorted(glob.glob('dogrulama/metinsiz/*')):
    d = json.load(open(mf, encoding='utf-8'))
    kaynak = d['_source'].replace('\\', '/')
    sec = [it for it in d['items'] if (kaynak, str(it['number'])) in hedef]
    if not sec:
        continue
    for it in sec:
        bulunan.add((kaynak, str(it['number'])))
    secim.append({
        "_source": kaynak,
        "_question_type": d.get('_question_type'),
        "instructions": d.get('instructions'),
        "options": d.get('options'),
        "option_lists": d.get('option_lists'),
        "items": sec,
    })

with open('dogrulama/metinsiz-secim.json', 'w', encoding='utf-8') as f:
    json.dump(secim, f, ensure_ascii=False, indent=1)

print('hedef:', len(hedef), '| bulunan:', len(bulunan), '| dosya:', len(secim))
for eksik in sorted(hedef - bulunan):
    print('  EKSIK:', eksik)
