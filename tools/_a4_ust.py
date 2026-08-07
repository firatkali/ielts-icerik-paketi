"""Ust band (>=7) gerekcelerini resmi sinav gorevlisi yorumuyla yan yana koyar.

2. duzeltme (OPUS5-A4) icin yazildi: SADECE gorunur kumeler S2+S3. S1 o calistirmanin SAKLI
kumesiydi ve bu script onu hicbir zaman acmaz.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
K = json.load(open(os.path.join(ROOT, 'kalibrasyon/olcum/kumeler.json')))
vis = set(K['S2']) | set(K['S3'])

for c in sorted(vis):
    ex = json.load(open(os.path.join(ROOT, 'kalibrasyon/ornekler/yazma', c + '.json'), encoding='utf-8'))
    if ex['band'] < 7:
        continue
    sc = json.load(open(os.path.join(ROOT, 'kalibrasyon/olcum/tur2', c + '-1.json'), encoding='utf-8'))
    print('=' * 100)
    print(c, '| gercek', ex['band'], '| verilen', sc['predicted_band'], '| T', ex['task'], ex['module'])
    print('-- SINAV GOREVLISI:', ex['examiner_comment'])
    for x in sc['output']['criteria']:
        print('-- %-28s %-4s %s' % (x['name'], x['band'], x['why']))
