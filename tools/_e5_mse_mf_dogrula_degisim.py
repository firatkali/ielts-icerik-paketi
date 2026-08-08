# -*- coding: utf-8 -*-
"""E5/3 dogrulamasi: answer, evidence, evidence_locator, number degismedi mi?
Secenek harflerinin kumesi ve sirasi korundu mu? Soru sayisi ayni mi?

HEAD'deki surumle calisma agacindaki surumu alan alan karsilastirir.
"""

import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

FILES = [
    'content/reading/practice/matching-sentence-endings.json',
    'content/reading/practice/matching-features.json',
    'content/reading/tests/AC1/matching-features.json',
    'content/reading/tests/AC2/matching-features.json',
    'content/reading/tests/AC3/matching-features.json',
    'content/reading/tests/AC4/matching-features.json',
]

KORUNAN = ("answer", "evidence", "evidence_locator", "allow_repeat")

hata = 0
toplam = 0
for f in FILES:
    eski = json.loads(subprocess.run(
        ['git', 'show', 'HEAD:' + f], capture_output=True, text=True,
        encoding='utf-8').stdout)
    yeni = ortak.oku(f)

    a_list = ortak.kumeli_sorular(eski)
    b_list = ortak.kumeli_sorular(yeni)
    if len(a_list) != len(b_list):
        print('HATA soru sayisi degisti:', f)
        hata += 1
        continue

    for (ga, a), (gb, b) in zip(a_list, b_list):
        toplam += 1
        if a['number'] != b['number']:
            print('HATA numara degisti:', f, a['number'], '->', b['number'])
            hata += 1
        for k in KORUNAN:
            if a.get(k) != b.get(k):
                print('HATA korunan alan degisti:', f, a['number'], k)
                print('   eski:', a.get(k))
                print('   yeni:', b.get(k))
                hata += 1
        ha = [o['key'] for o in (ga.get('option_list') or {}).get('options', [])]
        hb = [o['key'] for o in (gb.get('option_list') or {}).get('options', [])]
        if ha != hb:
            print('HATA secenek harfleri/sirasi degisti:', f, a['number'])
            hata += 1

    # cevap harflerinin bir kume icinde tekrar etmemesi (allow_repeat=false)
    for g in (yeni.get('groups') or [yeni]):
        if g.get('allow_repeat') is False:
            harfler = [x for it in g['items'] for x in it['answer']]
            if len(harfler) != len(set(harfler)):
                print('HATA allow_repeat=false ama harf tekrari var:', f)
                hata += 1

print('karsilastirilan soru: %d' % toplam)
print('KORUNAN ALAN HATASI: %d' % hata)
sys.exit(1 if hata else 0)
