"""Son rapor (OPUS5-A4, SON calistirma) icin hesap.

Duzeltme YOK. Bu script alti turun sayilarini yan yana koyar: tamamlanmis uc
yazma turu (1-3), konusma turu (4), alt band turu (5) ve dogrulama turu (6).
Bu asamada sakli kume kalmadi (OPUS5-A4 tablosu: son raporda hepsi gorunur).

Elle ortalama alinmasin diye yazildi; SONUC.md ve SONUC-konusma.md'deki her sayi
buradan gelir.

Kullanim: python tools/_a4_sonuc_son.py
"""
import glob
import json
import os
import statistics

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OLCUM = os.path.join(ROOT, 'kalibrasyon', 'olcum')

YAZMA_OLCUT = ['task_response', 'coherence_cohesion', 'lexical_resource',
               'grammatical_range_accuracy']
KONUSMA_OLCUT = ['fluency_coherence', 'lexical_resource',
                 'grammatical_range_accuracy']

K = json.load(open(os.path.join(OLCUM, 'kumeler.json'), encoding='utf-8'))
setof = {c: s for s, l in K.items() for c in l}

# --- gercek bandlar (yazma + konusma) ---------------------------------------
real, skill = {}, {}
for alt, sk in (('yazma', 'writing'), ('konusma', 'speaking')):
    for f in glob.glob(os.path.join(ROOT, 'kalibrasyon/ornekler', alt, '*.json')):
        d = json.load(open(f, encoding='utf-8'))
        if d.get('kind') != 'official_scored_sample':
            continue
        kod = os.path.basename(f)[:-5]
        real[kod] = d['band']
        skill[kod] = sk

TURLAR = ['1', '2', '3', '4', '5', '6']


def tur_oku(t):
    p = {}
    for f in sorted(glob.glob(os.path.join(OLCUM, 'tur%s' % t, '*.json'))):
        d = json.load(open(f, encoding='utf-8'))
        p.setdefault(d['sample'], []).append(d)
    return p


T = {t: tur_oku(t) for t in TURLAR}


def hat(s):
    print()
    print('=' * 78)
    print(s)
    print('=' * 78)


def fark(t, c):
    """tek seferlik (ilk) puan - gercek band"""
    return T[t][c][0]['predicted_band'] - real[c]


def ozet(kodlar, t):
    ks = [c for c in kodlar if c in T[t]]
    if not ks:
        return None
    f = [fark(t, c) for c in ks]
    yay = [max(x['predicted_band'] for x in T[t][c]) - min(x['predicted_band'] for x in T[t][c])
           for c in ks]
    return dict(n=len(f), oaf=statistics.mean(abs(x) for x in f),
                eg=statistics.mean(f), enb=max(abs(x) for x in f),
                yay=statistics.mean(yay),
                tekrar=statistics.mean(len(T[t][c]) for c in ks))


def yaz(etiket, o):
    if o is None:
        print(' %-10s   —' % etiket)
        return
    print(' %-10s %-4d %-11.3f %+-9.3f %-10.2f %-9.2f %.1f' % (
        etiket, o['n'], o['oaf'], o['eg'], o['enb'], o['yay'], o['tekrar']))


BASLIK = ' %-10s %-4s %-11s %-9s %-10s %-9s %s' % (
    'kume', 'n', 'ort.mutlak', 'egilim', 'en buyuk', 'yayilim', 'tekrar')

hat('1) ALTI TURUN OLCULERI — her turun kendi ornek kumesi')
print(BASLIK)
for t in TURLAR:
    yaz('tur %s' % t, ozet(sorted(T[t]), t))

hat('1b) TUR ICI BECERI KIRILIMI')
for t in TURLAR:
    print('\ntur %s' % t)
    print(BASLIK)
    for sk in ('writing', 'speaking'):
        yaz(sk, ozet([c for c in T[t] if skill[c] == sk], t))

# --- eslesik karsilastirmalar ------------------------------------------------
yazma_ortak = sorted(c for c in set(T['1']) & set(T['2']) & set(T['3']) & set(T['6'])
                     if skill[c] == 'writing')
konusma_ortak = sorted(c for c in set(T['4']) & set(T['6']) if skill[c] == 'speaking')
alt_ortak = sorted(set(T['5']) & set(T['6']))

hat('2) ESLESIK — YAZMA, tur 1/2/3/6 hepsinde puanlanan %d ornek' % len(yazma_ortak))
print(BASLIK)
for t in ['1', '2', '3', '6']:
    yaz('tur %s' % t, ozet(yazma_ortak, t))
eksik = sorted(c for c in T['6'] if skill[c] == 'writing' and c not in yazma_ortak)
print('\ndort turun hepsinde olmayan yazma ornegi (%d): %s' % (len(eksik), ', '.join(eksik)))
for c in eksik:
    print('   %-12s gercek %.1f | %s' % (c, real[c], ' '.join(
        'tur%s %+.1f' % (t, fark(t, c)) for t in TURLAR if c in T[t])))

hat('2b) ESLESIK — KONUSMA, tur 4 ve 6 (%d ornek)' % len(konusma_ortak))
print(BASLIK)
for t in ['4', '6']:
    yaz('tur %s' % t, ozet(konusma_ortak, t))

hat('2c) ESLESIK — ALT BAND, tur 5 ve 6 (%d ornek)' % len(alt_ortak))
print(BASLIK)
for t in ['5', '6']:
    yaz('tur %s' % t, ozet(alt_ortak, t))
print()
for c in alt_ortak:
    print('  %-12s gercek %.1f | %s' % (c, real[c], '  '.join(
        'tur%s %+.1f (%.1f)' % (t, fark(t, c), T[t][c][0]['predicted_band'])
        for t in TURLAR if c in T[t])))

# --- kume / ezber kontrolu ---------------------------------------------------
SAKLI = {'2': 'S3', '3': 'S1', '6': 'S2'}  # o turun sinadigi duzeltmenin sakli kumesi

hat('3) KUME BAZINDA — ezber (sakli kume) kontrolu')
print('duzeltme 1 S3 saklidiydi -> tur 2 sinadi')
print('duzeltme 2 S1 saklidiydi -> tur 3 sinadi')
print('duzeltme 3 S2 saklidiydi -> tur 6 sinadi\n')
print('tur  kume  n   ort.mutlak  egilim')
for t in TURLAR:
    for s in ['S1', 'S2', 'S3']:
        o = ozet([c for c in T[t] if setof.get(c) == s], t)
        if o:
            print(' %s   %s%s   %-3d %-11.3f %+.3f' % (
                t, s, '*' if SAKLI.get(t) == s else ' ', o['n'], o['oaf'], o['eg']))
    print()
print('* = o turun sinadigi duzeltmede SAKLI olan kume\n')
print('SAKLI vs GORUNUR (ham, eslesik degil)')
print(' tur  sakli  n   ort.mutlak  egilim | gorunur  n   ort.mutlak  egilim | fark')
for t, s in SAKLI.items():
    a = ozet([c for c in T[t] if setof.get(c) == s], t)
    b = ozet([c for c in T[t] if setof.get(c) and setof[c] != s], t)
    print('  %s   %s     %-3d %-11.3f %+-8.3f| %-8s %-3d %-11.3f %+-8.3f| %.3f' % (
        t, s, a['n'], a['oaf'], a['eg'], '+'.join(sorted({'S1', 'S2', 'S3'} - {s})),
        b['n'], b['oaf'], b['eg'], abs(a['oaf'] - b['oaf'])))
print('\ntur 6 — sakli/gorunur farki beceriye gore')
for sk in ('writing', 'speaking'):
    a = ozet([c for c in T['6'] if setof.get(c) == 'S2' and skill[c] == sk], '6')
    b = ozet([c for c in T['6'] if setof.get(c) != 'S2' and skill[c] == sk], '6')
    print('  %-9s S2(sakli) n=%d oaf %.3f eg %+.3f | S1+S3 n=%d oaf %.3f eg %+.3f | fark %.3f' % (
        sk, a['n'], a['oaf'], a['eg'], b['n'], b['oaf'], b['eg'], abs(a['oaf'] - b['oaf'])))

# --- urunun gercek davranisi -------------------------------------------------


def dagilim(t, kodlar, baslik):
    ks = [c for c in kodlar if c in T[t]]
    f = [(c, fark(t, c)) for c in sorted(ks)]
    n = len(f)
    print('\n%s (n=%d)' % (baslik, n))
    kova = {}
    for c, d in f:
        kova.setdefault(d, []).append(c)
    print('  fark    kac  ornekler')
    for d in sorted(kova):
        print('  %+.1f    %-4d %s' % (d, len(kova[d]), ' '.join(kova[d])))
    print('  tam isabet       : %d/%d (%%%.0f)' % (
        sum(1 for _, d in f if d == 0), n, 100 * sum(1 for _, d in f if d == 0) / n))
    print('  0,5 band icinde  : %d/%d (%%%.0f)' % (
        sum(1 for _, d in f if abs(d) <= 0.5), n, 100 * sum(1 for _, d in f if abs(d) <= 0.5) / n))
    print('  1,0 band icinde  : %d/%d (%%%.0f)' % (
        sum(1 for _, d in f if abs(d) <= 1.0), n, 100 * sum(1 for _, d in f if abs(d) <= 1.0) / n))
    print('  >= 1,5 sapma     : %d/%d  %s' % (
        sum(1 for _, d in f if abs(d) >= 1.5), n,
        ' '.join(c for c, d in f if abs(d) >= 1.5)))
    print('  comert (+) %d · tam %d · cimri (-) %d' % (
        sum(1 for _, d in f if d > 0), sum(1 for _, d in f if d == 0),
        sum(1 for _, d in f if d < 0)))
    print('  verilen puan araligi: %.1f - %.1f  (gercek bandlar %.1f - %.1f)' % (
        min(T[t][c][0]['predicted_band'] for c in ks),
        max(T[t][c][0]['predicted_band'] for c in ks),
        min(real[c] for c in ks), max(real[c] for c in ks)))


hat('4) URUNUN GERCEK DAVRANISI — tek seferlik puanlarin dagilimi')
dagilim('6', sorted(T['6']), 'tur 6 — hepsi')
dagilim('6', [c for c in T['6'] if skill[c] == 'writing'], 'tur 6 — yazma')
dagilim('6', [c for c in T['6'] if skill[c] == 'speaking'], 'tur 6 — konusma')
dagilim('3', sorted(T['3']), 'tur 3 — yazma (karsilastirma icin)')
dagilim('4', sorted(T['4']), 'tur 4 — konusma (karsilastirma icin)')

# --- band araligi x olcut ----------------------------------------------------


def buck(b):
    return '>=7  ' if b >= 7 else ('5-6.5' if b >= 5 else '<=4.5')


def olcut_tablo(t, kodlar, keys, baslik):
    ks = [c for c in kodlar if c in T[t]]
    if not ks:
        return
    print('\n%s' % baslik)
    print('%-6s %-4s %s %s' % ('band', 'n', ' '.join('%-8s' % k[:8] for k in keys), 'genel'))
    for bk in ['>=7  ', '5-6.5', '<=4.5']:
        sel = [c for c in ks if buck(real[c]) == bk]
        if not sel:
            continue
        row = []
        for k in keys:
            vals = []
            for c in sel:
                for x in T[t][c][0]['criteria']:
                    if x['name'] == k:
                        vals.append(x['band'] - real[c])
            row.append('%+.2f' % statistics.mean(vals) if vals else '  —  ')
        g = statistics.mean(fark(t, c) for c in sel)
        print('%-6s %-4d %s %+.2f' % (bk, len(sel), ' '.join('%-8s' % r for r in row), g))


hat('5) BAND ARALIGI x OLCUT — yazma')
for t in ['1', '2', '3', '5', '6']:
    olcut_tablo(t, [c for c in T[t] if skill[c] == 'writing'], YAZMA_OLCUT, 'tur %s' % t)

hat('5b) BAND ARALIGI x OLCUT — konusma')
for t in ['4', '6']:
    olcut_tablo(t, [c for c in T[t] if skill[c] == 'speaking'], KONUSMA_OLCUT, 'tur %s' % t)

# --- 3. duzeltmenin tur 6 beklentileri --------------------------------------
hat('6) 3. DUZELTMENIN BEKLENTILERI — tur 6 ile sinaniyor')
w6 = [c for c in T['6'] if skill[c] == 'writing']
alt = [c for c in w6 if real[c] <= 4.5]
orta = [c for c in w6 if 5 <= real[c] <= 6.5]
ust = [c for c in w6 if real[c] >= 7]


def olcut_ort(t, kodlar, key):
    vals = []
    for c in kodlar:
        for x in T[t][c][0]['criteria']:
            if x['name'] == key:
                vals.append(x['band'] - real[c])
    return statistics.mean(vals) if vals else float('nan')


print('1 alt band (<=4,5) genel sapma   : %+.2f  (hedef +0,50 icinde) n=%d' % (
    statistics.mean(fark('6', c) for c in alt), len(alt)))
print('2 alt band tutarlilik olcutu     : %+.2f  (hedef +0,75 icinde)' % olcut_ort(
    '6', alt, 'coherence_cohesion'))
print('  alt band gorev olcutu          : %+.2f  (hedef +0,75 icinde)' % olcut_ort(
    '6', alt, 'task_response'))
print('3 gercek bandi 3,0-4,0 orneklerde verilen tek seferlik puanlar (hedef: en az bir <=4,0):')
for c in sorted(alt):
    print('    %-12s gercek %.1f -> %.1f' % (c, real[c], T['6'][c][0]['predicted_band']))
print('4 ust band (>=7) sapmasi         : %+.2f  (hedef: -1,10\'un altina dusmesin) n=%d' % (
    statistics.mean(fark('6', c) for c in ust), len(ust)))
print('5 orta band (5-6,5) sapmasi      : %+.2f  (hedef -0,35 icinde) n=%d' % (
    statistics.mean(fark('6', c) for c in orta), len(orta)))
print('6 yazma egilimi                  : %+.3f (hedef -0,25 ile +0,10 arasi)' % ozet(w6, '6')['eg'])
a = ozet([c for c in T['6'] if setof.get(c) == 'S2'], '6')
b = ozet([c for c in T['6'] if setof.get(c) != 'S2'], '6')
print('7 sakli kume (S2) farki          : %.3f band (tur 3\'te 0,25 · tur 4\'te 0,625)' % abs(
    a['oaf'] - b['oaf']))
s4, s6 = ozet(konusma_ortak, '4'), ozet(konusma_ortak, '6')
print('8 konusma MAE                    : tur4 %.3f -> tur6 %.3f  (hedef 0,583 +- 0,15)' % (
    s4['oaf'], s6['oaf']))

# --- basari olcutleri --------------------------------------------------------
hat('7) BASARI OLCUTLERI — tur 6 (urun davranisi)')
for etiket, kodlar in (('hepsi', sorted(T['6'])),
                       ('yazma', [c for c in T['6'] if skill[c] == 'writing']),
                       ('konusma', [c for c in T['6'] if skill[c] == 'speaking'])):
    o = ozet(kodlar, '6')
    print('\n%s (n=%d)' % (etiket, o['n']))
    print('  ort. mutlak fark < 0,5      : %.3f  %s' % (o['oaf'], 'GECTI' if o['oaf'] < 0.5 else 'KALDI'))
    print('  hicbir ornekte >= 1,5 sapma : %.2f   %s' % (o['enb'], 'GECTI' if o['enb'] < 1.5 else 'KALDI'))
    print('  egilim +-0,25 icinde        : %+.3f %s' % (o['eg'], 'GECTI' if abs(o['eg']) <= 0.25 else 'KALDI'))
    print('  yayilim <= 0,5              : %.2f   %s (tekrar %.1f)' % (
        o['yay'], 'GECTI' if o['yay'] <= 0.5 else 'KALDI', o['tekrar']))

hat('8) TUTARSIZLIK — tekrarli olculen turlarda yayilim')
for t in ['1', '3', '4', '5']:
    o = ozet(sorted(T[t]), t)
    kt = [c for c in sorted(T[t]) if max(x['predicted_band'] for x in T[t][c]) !=
          min(x['predicted_band'] for x in T[t][c])]
    print('\ntur %s (tekrar %.0f) ortalama yayilim %.2f · oynayan ornek %d/%d' % (
        t, o['tekrar'], o['yay'], len(kt), o['n']))
    for c in kt:
        v = [x['predicted_band'] for x in T[t][c]]
        print('   %-12s gercek %.1f  %s  yayilim %.1f' % (c, real[c], v, max(v) - min(v)))

hat('9) KONUSMA — ornek ornek, tur 4 vs tur 6')
print('%-14s %-7s %-22s %-8s %-8s' % ('kod', 'gercek', 'tur4 (6 tekrar)', 'tur4-1s', 'tur6'))
for c in sorted(konusma_ortak, key=lambda c: real[c]):
    v4 = [x['predicted_band'] for x in T['4'][c]]
    print('%-14s %-7.1f %-22s %-8.1f %-8.1f' % (
        c, real[c], str(v4), v4[0], T['6'][c][0]['predicted_band']))

hat('10) KONUSMA — olcut bazinda sapma')
print('%-28s %-12s %-12s %s' % ('olcut', 'tur4 (6 ort)', 'tur4 (tek)', 'tur6 (tek)'))
for key in KONUSMA_OLCUT:
    vo, v4, v6 = [], [], []
    for c in konusma_ortak:
        vo.append(statistics.mean(
            x['band'] for k in T['4'][c] for x in k['criteria'] if x['name'] == key) - real[c])
        v4 += [x['band'] - real[c] for x in T['4'][c][0]['criteria'] if x['name'] == key]
        v6 += [x['band'] - real[c] for x in T['6'][c][0]['criteria'] if x['name'] == key]
    print('  %-26s %+-12.2f %+-12.2f %+.2f' % (
        key, statistics.mean(vo), statistics.mean(v4), statistics.mean(v6)))

hat('11) ORNEK ORNEK — butun turlar (tek seferlik puan / sapma)')
print('%-14s %-4s %-7s %-6s %s' % ('kod', 'kume', 'beceri', 'gercek',
                                   ' '.join('tur%s ' % t for t in TURLAR)))
for c in sorted(real, key=lambda c: (skill[c], real[c], c)):
    hucre = []
    for t in TURLAR:
        hucre.append('%+5.1f' % fark(t, c) if c in T[t] else '    ·')
    print('%-14s %-4s %-7s %-6.1f %s' % (
        c, setof.get(c, '—'), skill[c][:4], real[c], ' '.join(hucre)))
