"""6/7 ve 7/7 yuvalari icin ozet tablo: eski kanit -> yeni kanit, cevap, kip taramasi."""
import json, re, sys

MUTLAK = ['only', 'every', 'all ', 'no ', 'none', 'never', 'always', 'must', 'cannot',
          'at least', 'as well as', 'as effectively', 'identical', 'the first', 'each ',
          'both', 'any ', 'twice', 'entirely', 'alone']
OLCULU = ['may', 'might', 'probably', 'likely', 'roughly', 'about', 'around', 'seems',
          'suggest', 'tend', 'some ', 'often', 'usually', 'plausib', 'appear', 'nearly',
          'more or less', 'up to']

etiket = sys.argv[1] if len(sys.argv) > 1 else '7/7'
j = json.load(open('content/DOGRULAMA/yeniden-uretim-listesi.json', encoding='utf-8'))
cache = {}
for x in j['elenen']:
    y = x.get('yeniden_uretildi') or {}
    if etiket not in y.get('calistirma', ''):
        continue
    f = x['dosya']
    if f not in cache:
        cache[f] = json.load(open(f, encoding='utf-8'))
    it = next(i for i in cache[f]['items'] if i['number'] == x['numara'])
    loc = it.get('evidence_locator') or {}
    p = (it.get('prompt') or '').lower()
    kip = []
    if any(w in p for w in MUTLAK):
        kip.append('mutlak')
    if any(w in p for w in OLCULU):
        kip.append('olculu')
    cev = it.get('answer')
    print('%-46s #%-3s %-4s -> %-4s  %-22s %-14s %s' % (
        f.replace('content/reading/', ''), x['numara'], x['pasaj'],
        '%s/%s' % (loc.get('paragraph'), loc.get('sentence')),
        (cev[0] if isinstance(cev, list) and cev else '')[:22],
        '+'.join(kip) or '-', (it.get('prompt') or '')[:60]))
