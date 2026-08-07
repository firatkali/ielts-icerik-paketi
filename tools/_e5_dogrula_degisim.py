# -*- coding: utf-8 -*-
"""E5/1 dogrulamasi: answer, evidence, evidence_locator ve soru sayisi degismedi mi?

HEAD'deki surumle calisma agacindaki surumu karsilastirir.
"""
import json
import subprocess

FILES = [
    'content/reading/practice/yes-no-not-given.json',
    'content/reading/tests/GT1/yes-no-not-given.json',
    'content/reading/tests/GT2/yes-no-not-given.json',
]

KORUNAN = ("answer", "evidence", "evidence_locator")

hata = 0
for f in FILES:
    eski = json.loads(subprocess.run(
        ['git', 'show', 'HEAD:' + f], capture_output=True, text=True,
        encoding='utf-8').stdout)
    yeni = json.load(open(f, encoding='utf-8'))

    if len(eski['items']) != len(yeni['items']):
        print('HATA soru sayisi degisti:', f)
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

    durum = {}
    for b in yeni['items']:
        durum[b.get('status')] = durum.get(b.get('status'), 0) + 1
    print('%-52s %s' % (f, durum))

print('KORUNAN ALAN HATASI:', hata)
