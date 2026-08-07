"""Son rapor (OPUS5-A4, 3. calistirma) icin hesap.

Duzeltme YOK: bu script yalnizca uc turun sayilarini yan yana koyar. Bu asamada
sakli kume kalmadi (bkz. OPUS5-A4 tablosu: son raporda hepsi gorunur), o yuzden
kume filtresi yok.

Elle ortalama alinmasin diye yazildi; SONUC.md'deki her sayi buradan gelir.

Kullanim: python tools/_a4_sonuc.py
"""
import glob
import json
import os
import statistics

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEYS = ['task_response', 'coherence_cohesion', 'lexical_resource',
        'grammatical_range_accuracy']

K = json.load(open(os.path.join(ROOT, 'kalibrasyon/olcum/kumeler.json')))
setof = {c: s for s, l in K.items() for c in l}

real = {}
for f in glob.glob(os.path.join(ROOT, 'kalibrasyon/ornekler/yazma/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    if d.get('kind') != 'official_scored_sample':
        continue
    real[os.path.basename(f)[:-5]] = d


def tur_oku(t):
    """kod -> [puan, ...] (dosya adi sirasi = tekrar sirasi)"""
    p = {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'kalibrasyon/olcum/tur%s' % t, '*.json'))):
        d = json.load(open(f, encoding='utf-8'))
        p.setdefault(d['sample'], []).append(d)
    return p


T = {t: tur_oku(t) for t in '123'}
ortak = sorted(set(T['1']) & set(T['2']) & set(T['3']))


def hat(s):
    print()
    print('=' * 78)
    print(s)
    print('=' * 78)


def ozet(kodlar, t):
    """tek seferlik (ilk) puan uzerinden ozet"""
    f = [T[t][c][0]['predicted_band'] - real[c]['band'] for c in kodlar if c in T[t]]
    if not f:
        return None
    yay = [max(x['predicted_band'] for x in T[t][c]) - min(x['predicted_band'] for x in T[t][c])
           for c in kodlar if c in T[t]]
    return dict(n=len(f), oaf=statistics.mean(abs(x) for x in f),
                eg=statistics.mean(f), enb=max(abs(x) for x in f),
                yay=statistics.mean(yay))


hat('1) Uc turun olculeri — HER TURUN KENDI ORNEK KUMESI (RAPOR-tur*.md ile ayni)')
print('tur  n   ort.mutlak  egilim   en buyuk  yayilim')
for t in '123':
    o = ozet(sorted(T[t]), t)
    print(' %s  %-3d %-11.3f %+-8.3f %-9.2f %.2f' % (t, o['n'], o['oaf'], o['eg'], o['enb'], o['yay']))

hat('2) ESLESIK karsilastirma — uc turda da puanlanan %d ornek' % len(ortak))
print('tur  n   ort.mutlak  egilim   en buyuk  yayilim')
for t in '123':
    o = ozet(ortak, t)
    print(' %s  %-3d %-11.3f %+-8.3f %-9.2f %.2f' % (t, o['n'], o['oaf'], o['eg'], o['enb'], o['yay']))
eksik = sorted(set(real) - set(ortak))
print('\ntur 3\'te puanlanmayan ornek (%d): %s' % (len(eksik), ', '.join(eksik)))
for c in eksik:
    v = [(t, T[t][c][0]['predicted_band'] - real[c]['band']) for t in '12' if c in T[t]]
    print('   %-12s gercek %.1f | %s' % (c, real[c]['band'],
                                         ' '.join('tur%s %+.1f' % x for x in v)))

hat('3) KUME bazinda (ezber kontrolu)')
print('S1: 2. duzeltmenin SAKLI kumesi (son ayarin gormedigi kume)')
print('S3: 1. duzeltmenin sakli kumesi | S2: iki duzeltmede de gorunur\n')
print('tur  kume  n   ort.mutlak  egilim')
for t in '123':
    for s in ['S1', 'S2', 'S3']:
        o = ozet([c for c in T[t] if setof.get(c) == s], t)
        if o:
            print(' %s   %s    %-3d %-11.3f %+.3f' % (t, s, o['n'], o['oaf'], o['eg']))
    print()
print('tur 3 — S1 (sakli) vs S2+S3 (gorunur), ESLESIK degil ham:')
a = ozet([c for c in T['3'] if setof.get(c) == 'S1'], '3')
b = ozet([c for c in T['3'] if setof.get(c) in ('S2', 'S3')], '3')
print('  S1     n=%d ort.mutlak %.3f egilim %+.3f' % (a['n'], a['oaf'], a['eg']))
print('  S2+S3  n=%d ort.mutlak %.3f egilim %+.3f' % (b['n'], b['oaf'], b['eg']))
print('  fark   %.3f band' % abs(a['oaf'] - b['oaf']))

hat('4) URUNUN GERCEK DAVRANISI — tek seferlik puanlarin dagilimi (tur 3)')
f3 = [(c, T['3'][c][0]['predicted_band'] - real[c]['band']) for c in sorted(T['3'])]
kova = {}
for c, d in f3:
    kova.setdefault(round(d * 2) / 2, []).append(c)
print('fark    kac ornek  ornekler')
for d in sorted(kova):
    print('%+.1f    %-10d %s' % (d, len(kova[d]), ' '.join(kova[d])))
n = len(f3)
print('\ntam isabet          : %d/%d (%%%.0f)' % (sum(1 for _, d in f3 if d == 0), n,
                                                  100 * sum(1 for _, d in f3 if d == 0) / n))
print('0,5 band icinde     : %d/%d (%%%.0f)' % (sum(1 for _, d in f3 if abs(d) <= 0.5), n,
                                                100 * sum(1 for _, d in f3 if abs(d) <= 0.5) / n))
print('1,0 band icinde     : %d/%d (%%%.0f)' % (sum(1 for _, d in f3 if abs(d) <= 1.0), n,
                                                100 * sum(1 for _, d in f3 if abs(d) <= 1.0) / n))
print('>= 1,5 band sapma   : %d/%d  %s' % (sum(1 for _, d in f3 if abs(d) >= 1.5), n,
                                           ' '.join(c for c, d in f3 if abs(d) >= 1.5)))
print('verilen puan araligi: %.1f - %.1f  (gercek bandlar %.1f - %.1f)' % (
    min(T['3'][c][0]['predicted_band'] for c in T['3']),
    max(T['3'][c][0]['predicted_band'] for c in T['3']),
    min(real[c]['band'] for c in T['3']), max(real[c]['band'] for c in T['3'])))

print('\ntutarsizlik — ayni cevaba 3 puanlamada verilen farkli puanlar (tur 3)')
for c in sorted(T['3']):
    v = [x['predicted_band'] for x in T['3'][c]]
    if max(v) != min(v):
        print('  %-12s %s  (yayilim %.1f)' % (c, v, max(v) - min(v)))


def buck(b):
    return '>=7  ' if b >= 7 else ('5-6.5' if b >= 5 else '<=4.5')


hat('5) BAND ARALIGI x OLCUT — turlar yan yana (eslesik %d ornek)' % len(ortak))
for t in '123':
    print('\ntur %s' % t)
    print('%-6s %-4s %-7s %-7s %-7s %-7s %s' % ('band', 'n', 'gorev', 'tutarlk', 'kelime', 'dilbil', 'genel'))
    for bk in ['>=7  ', '5-6.5', '<=4.5']:
        sel = [c for c in ortak if buck(real[c]['band']) == bk]
        if not sel:
            continue
        cr = {c: dict((x['name'], x['band']) for x in T[t][c][0]['criteria']) for c in sel}
        d = ['%+.2f' % statistics.mean(cr[c][k] - real[c]['band'] for c in sel) for k in KEYS]
        g = statistics.mean(T[t][c][0]['predicted_band'] - real[c]['band'] for c in sel)
        print('%-6s %-4d %-7s %-7s %-7s %-7s %+.2f' % (bk, len(sel), d[0], d[1], d[2], d[3], g))

hat('6) 2. DUZELTMENIN BEKLENTILERI (tur 3 ile sinaniyor)')
u = [c for c in T['3'] if real[c]['band'] >= 7]
uc = {c: dict((x['name'], x['band']) for x in T['3'][c][0]['criteria']) for c in u}
o3 = ozet(sorted(T['3']), '3')
orta = [c for c in T['3'] if 5 <= real[c]['band'] <= 6.5]
alt = [c for c in T['3'] if real[c]['band'] <= 4.5]
print('1 ust band (>=7) genel sapma      : %+.2f  (hedef: -0,75 icinde) n=%d' % (
    statistics.mean(T['3'][c][0]['predicted_band'] - real[c]['band'] for c in u), len(u)))
print('  >=7 orneklerde en yuksek puan   : %.1f  (hedef: en az bir 7,5+)' % max(
    T['3'][c][0]['predicted_band'] for c in u))
print('2 ust bandda tutarlilik olcutu    : %+.2f  (hedef: -1,00 icinde)' % statistics.mean(
    uc[c]['coherence_cohesion'] - real[c]['band'] for c in u))
print('3 en buyuk tek sapma              : %.2f   (hedef: < 2,0)' % o3['enb'])
print('4 egilim                          : %+.3f (hedef: -0,35 icinde)' % o3['eg'])
print('5 orta band (5-6,5) sapmasi       : %+.2f  (hedef: +0,25 gecmesin) n=%d' % (
    statistics.mean(T['3'][c][0]['predicted_band'] - real[c]['band'] for c in orta), len(orta)))
print('6 alt band (<=4,5) sapmasi        : %+.2f  (hedef: +0,50 uzerine cikmasin) n=%d' % (
    statistics.mean(T['3'][c][0]['predicted_band'] - real[c]['band'] for c in alt), len(alt)))
print('7 sakli kume (S1) farki           : %.3f band' % abs(a['oaf'] - b['oaf']))
