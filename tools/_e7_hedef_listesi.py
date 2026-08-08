"""E7 olcum kapsami: blind_solvable alani null birakilmis sorular.

E5 duzelttigi ve E6 yeniden urettigi sorularda blind_solvable null birakildi
("E7 bunlari yeniden olcmeli"). Bu betik cevap alanlarina HIC dokunmadan
dosya + numara + tip + status listesi cikarir; kor cozum oncesi kapsam belirlemek
icindir.
"""
import glob
import json
import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

hedef = []
alan_yok = collections.Counter()
for f in sorted(glob.glob('content/reading/**/*.json', recursive=True)):
    d = json.load(open(f, encoding='utf-8'))
    if not isinstance(d, dict) or not (d.get('items') or d.get('groups')):
        continue
    for it in ortak.sorular(d):
        if 'blind_solvable' not in it:
            alan_yok[f] += 1
            continue
        if it['blind_solvable'] is None:
            hedef.append((f, it.get('number'), d.get('question_type') or it.get('question_type'),
                          it.get('status'), 'E6' if it.get('yeniden_uretim') else 'E5'))

print('HEDEF SORU SAYISI:', len(hedef))
dosya_sayim = collections.Counter(h[0] for h in hedef)
print('\n=== dosya bazinda ===')
for f, n in sorted(dosya_sayim.items()):
    print('  %-58s %d' % (f, n))
print('\n=== soru listesi (dosya, numara, tip, status, kaynak) ===')
for h in hedef:
    print('  %-58s %-5s %-28s %-9s %s' % h)
if alan_yok:
    print('\n=== blind_solvable alani hic olmayan sorular (dosya: adet) ===')
    for f, n in sorted(alan_yok.items()):
        print('  %-58s %d' % (f, n))
