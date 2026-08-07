# -*- coding: utf-8 -*-
"""E5/2 dogrulamasi: answer, evidence, evidence_locator, number, select_count
degismedi mi? Ayrica secenek harflerinin kumesi ve sirasi korundu mu?

HEAD'deki surumle calisma agacindaki surumu karsilastirir.
"""
import json
import subprocess

FILES = [
    'content/reading/practice/multiple-choice.json',
    'content/reading/tests/AC1/multiple-choice.json',
    'content/reading/tests/AC2/multiple-choice.json',
    'content/reading/tests/AC3/multiple-choice.json',
    'content/reading/tests/AC4/multiple-choice.json',
    'content/reading/tests/GT1/multiple-choice.json',
    'content/reading/tests/GT2/multiple-choice.json',
]

KORUNAN = ("answer", "evidence", "evidence_locator", "select_count")

hata = 0
toplam_soru = 0
for f in FILES:
    eski = json.loads(subprocess.run(
        ['git', 'show', 'HEAD:' + f], capture_output=True, text=True,
        encoding='utf-8').stdout)
    yeni = json.load(open(f, encoding='utf-8'))

    if len(eski['items']) != len(yeni['items']):
        print('HATA yuva sayisi degisti:', f)
        hata += 1
        continue

    for a, b in zip(eski['items'], yeni['items']):
        if a['number'] != b['number']:
            print('HATA numara degisti:', f, a['number'], '->', b['number'])
            hata += 1
        for k in KORUNAN:
            if a.get(k) != b.get(k):
                print('HATA korunan alan degisti:', f, a['number'], k)
                print('   eski:', a.get(k))
                print('   yeni:', b.get(k))
                hata += 1
        ha = [o['letter'] for o in a['options']]
        hb = [o['letter'] for o in b['options']]
        if ha != hb:
            print('HATA secenek harfleri/sirasi degisti:', f, a['number'])
            hata += 1
        toplam_soru += 2 if b.get('select_count') == 2 else 1

    durum = {}
    for b in yeni['items']:
        durum[b.get('status')] = durum.get(b.get('status'), 0) + 1
    print('%-52s yuva %2d  %s' % (f, len(yeni['items']), durum))

print('toplam soru (select_count agirlikli):', toplam_soru)
print('KORUNAN ALAN HATASI:', hata)
