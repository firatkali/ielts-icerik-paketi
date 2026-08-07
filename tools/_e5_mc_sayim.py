# -*- coding: utf-8 -*-
"""E5/2 yardimci sayim: konumsal_duzen yuvalarinda 'cazip ama yok' (pasajda
karsiligi olmayan, uydurma) celdiricilerin sayisi -- once/sonra.
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

P = FILES[0]
KON = set()
for n in (2, 5, 12, 14, 15):
    KON.add((P, n))
KON.add((FILES[1], 33))
KON.add((FILES[2], 32))
KON.add((FILES[2], 33))
KON.add((FILES[2], "34-35"))
KON.add((FILES[3], 33))
KON.add((FILES[4], 32))
KON.add((FILES[5], 21))


def say(getter):
    toplam = 0
    celdirici = 0
    for f in FILES:
        d = getter(f)
        for it in d['items']:
            if (f, it['number']) in KON:
                for v in it['distractor_analysis'].values():
                    celdirici += 1
                    if v.lower().startswith('cazip ama yok'):
                        toplam += 1
    return toplam, celdirici


def eski(f):
    return json.loads(subprocess.run(
        ['git', 'show', 'HEAD:' + f], capture_output=True, text=True,
        encoding='utf-8').stdout)


def yeni(f):
    return json.load(open(f, encoding='utf-8'))


print('konumsal_duzen yuvasi:', len(KON))
print('eski  cazip-ama-yok / celdirici: %d / %d' % say(eski))
print('yeni  cazip-ama-yok / celdirici: %d / %d' % say(yeni))
