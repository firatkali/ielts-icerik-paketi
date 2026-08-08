import json, collections

j = json.load(open('content/DOGRULAMA/yeniden-uretim-listesi.json', encoding='utf-8'))
pending = [x for x in j['elenen'] if not x.get('yeniden_uretildi')]
cache = {}
eksik = []
tamam = []
for x in pending:
    f = x['dosya']
    if f not in cache:
        cache[f] = json.load(open(f, encoding='utf-8'))
    d = cache[f]
    qs = d.get('items') or d.get('questions') or []
    q = next((q for q in qs if q.get('number') == x['numara']), None)
    if q is None:
        eksik.append((f, x['numara'], 'SORU YOK'))
        continue
    if q.get('generated_by') == 'opus' and q.get('yeniden_uretim'):
        tamam.append((f, x['numara']))
    else:
        eksik.append((f, x['numara'], x['tip'], q.get('status')))

print('URETILMIS (bookkeeping eksik):', len(tamam))
print('URETILMEMIS:', len(eksik))
for e in eksik:
    print('  ', e)
