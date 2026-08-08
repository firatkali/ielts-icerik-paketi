# -*- coding: utf-8 -*-
"""E5/4 dogrulamasi: korunan alanlar HEAD'e gore degisti mi?

answer / accepted_variants / evidence / evidence_locator / number / word_limit
degismemeli. Kelime bankasinda harf kumesi ve sirasi degismemeli, DOGRU
seceneklerin metni degismemeli (yalniz celdirici metinleri yeniden yazilabilir).
Ayrica her boslugun numarasi stem_block/table icinde hala duruyor olmali.
"""

import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402
from _e5_comp_elden_gecir import DOSYALAR  # noqa: E402

KORUNAN = ("answer", "accepted_variants", "evidence", "evidence_locator")

hata = 0
toplam = 0
banka_degisen = []

for f in DOSYALAR:
    ham = subprocess.run(['git', 'show', 'HEAD:' + f], capture_output=True,
                         text=True, encoding='utf-8').stdout
    eski = json.loads(ham)
    yeni = ortak.oku(f)

    a_list = ortak.sorular(eski)
    b_list = ortak.sorular(yeni)
    if len(a_list) != len(b_list):
        print('HATA soru sayisi degisti:', f)
        hata += 1
        continue
    if eski.get('word_limit') != yeni.get('word_limit'):
        print('HATA word_limit degisti:', f)
        hata += 1

    dogru_harfler = set()
    for it in b_list:
        for a in (it.get('answer') or []):
            if isinstance(a, str) and len(a) == 1:
                dogru_harfler.add(a)

    ea = eski.get('word_bank') or []
    eb = yeni.get('word_bank') or []
    if [o['letter'] for o in ea] != [o['letter'] for o in eb]:
        print('HATA kelime bankasi harfleri/sirasi degisti:', f)
        hata += 1
    for o1, o2 in zip(ea, eb):
        if o1['text'] != o2['text']:
            if o1['letter'] in dogru_harfler:
                print('HATA dogru secenegin metni degisti:', f, o1['letter'])
                hata += 1
            else:
                banka_degisen.append((f, o1['letter'], o1['text'], o2['text']))

    for a, b in zip(a_list, b_list):
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

    # her bosluk numarasi govdede duruyor mu?
    govde = (yeni.get('stem_block') or '')
    if yeni.get('table'):
        govde += ' '.join(' '.join(r) for r in yeni['table']['rows'])
    if govde.strip():
        for b in b_list:
            if '(%d)' % b['number'] not in govde:
                print('HATA bosluk govdede yok:', f, b['number'])
                hata += 1

print()
print('karsilastirilan soru: %d' % toplam)
for f, h, e, y in banka_degisen:
    print('celdirici yeniden yazildi: %s %s: %r -> %r' % (f, h, e, y))
print('KORUNAN ALAN HATASI: %d' % hata)
sys.exit(1 if hata else 0)
