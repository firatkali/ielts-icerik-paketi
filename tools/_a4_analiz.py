"""2. duzeltme (OPUS5-A4, 2. calistirma) icin tani.

SADECE gorunur kumeler S2+S3 uzerinden calisir; S1 o calistirmanin SAKLI kumesiydi ve bu script
onu hicbir zaman okumaz. Kume filtresi bilerek sabit: baska bir tur icin yeniden kullanmadan once
`vis` satirini o turun izinli kumeleriyle degistir.

Kullanim: python tools/_a4_analiz.py <tur no>
"""
import json, glob, os, statistics, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
K = json.load(open(os.path.join(ROOT, 'kalibrasyon/olcum/kumeler.json')))
GIZLI = 'S1'
vis = set(K['S2']) | set(K['S3'])
setof = {c: s for s, l in K.items() for c in l}

real = {}
for f in glob.glob(os.path.join(ROOT, 'kalibrasyon/ornekler/yazma/*.json')):
    c = os.path.basename(f)[:-5]
    if c not in vis:
        continue
    d = json.load(open(f, encoding='utf-8'))
    real[c] = d

tur = sys.argv[1] if len(sys.argv) > 1 else '2'
rows = []
for f in sorted(glob.glob(os.path.join(ROOT, 'kalibrasyon/olcum/tur' + tur, '*.json'))):
    d = json.load(open(f, encoding='utf-8'))
    c = d['sample']
    if c not in vis:
        continue
    cr = dict((x['name'], x['band']) for x in d['criteria'])
    rows.append((c, setof[c], real[c]['band'], d['predicted_band'], cr, real[c]))

KEYS = ['task_response', 'coherence_cohesion', 'lexical_resource', 'grammatical_range_accuracy']
print('tur', tur, '- gorunur kumeler S2+S3, n=', len(rows))
print('kod            S   ger  ver  fark   TR    CC    LR    GRA    mod/task/kelime')
for c, s, rb, pb, cr, m in sorted(rows, key=lambda r: -r[2]):
    wc = len(m['response_text'].split())
    print('%-14s %-3s %-4s %-4s %-+6s %-5s %-5s %-5s %-5s  %s/T%s/%s' % (
        c, s, rb, pb, pb - rb, cr[KEYS[0]], cr[KEYS[1]], cr[KEYS[2]], cr[KEYS[3]],
        m['module'][:3], m['task'], wc))


def buck(b):
    return '>=7  ' if b >= 7 else ('5-6.5' if b >= 5 else '<=4.5')


print()
print('band araligi x olcut sapmasi (olcut bandi - gercek genel band)')
for bk in ['>=7  ', '5-6.5', '<=4.5']:
    sel = [r for r in rows if buck(r[2]) == bk]
    if not sel:
        continue
    d = ' '.join('%s %+0.2f' % (k[:3].upper(), statistics.mean(r[4][k] - r[2] for r in sel)) for k in KEYS)
    print('%s n=%-3d %s | genel %+0.2f' % (bk, len(sel), d, statistics.mean(r[3] - r[2] for r in sel)))

print()
print('en dusuk olcut = verilen genel band mi?')
for c, s, rb, pb, cr, m in sorted(rows, key=lambda r: -r[2]):
    lo = min(cr.values())
    print('%-14s ger %-4s ver %-4s enDusukOlcut %-4s ortalamaOlcut %.2f' % (
        c, rb, pb, lo, statistics.mean(cr.values())))
