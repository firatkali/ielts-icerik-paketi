import json

hedefler = [
    ('content/reading/practice/true-false-not-given.json', 4),
    ('content/reading/tests/AC1/true-false-not-given.json', 10),
    ('content/reading/tests/AC3/true-false-not-given.json', 7),
    ('content/reading/practice/short-answer.json', 4),
    ('content/reading/practice/short-answer.json', 6),
    ('content/reading/practice/short-answer.json', 8),
]

hata = 0
for f, n in hedefler:
    d = json.load(open(f, encoding='utf-8'))
    it = next(i for i in d['items'] if i['number'] == n)
    sorun = []
    if it.get('status') != 'verified':
        sorun.append('status=%s' % it.get('status'))
    if it.get('blind_solvable') is not None:
        sorun.append('blind_solvable set')
    if it.get('generated_by') != 'opus':
        sorun.append('generated_by=%s' % it.get('generated_by'))
    if not it.get('yeniden_uretim'):
        sorun.append('yeniden_uretim yok')
    for k in ('flag_reason', 'flag_mechanism', 'reject_reason'):
        if k in it:
            sorun.append('artik alan: ' + k)
    loc = it.get('evidence_locator') or {}
    yr = it.get('yeniden_uretim') or {}
    if it.get('evidence') and yr.get('eski_kanit_cumlesi') == it['evidence']:
        sorun.append('kanit cumlesi degismemis')
    print('%-52s %-4s %s/%s  %s' % (f.split('/')[-1], n, loc.get('paragraph'), loc.get('sentence'),
                                    'OK' if not sorun else 'SORUN: ' + '; '.join(sorun)))
    hata += len(sorun)

print('toplam sorun:', hata)
