"""Yeniden uretim listesindeki bos 'yeniden_uretildi' alanlarini icerik dosyalarindan doldurur.

6/7 (tamamlama ailesi) yuvalari calisma agacinda uretilmis ama listeye islenmemisti;
7/7 (kalanlar) bu calistirmada uretildi. Ikisi de ayni kaynaktan, sorunun kendi
'yeniden_uretim' blogundaki 'kaynak_prompt' alanindan ayirt ediliyor.
"""
import json

CALISTIRMA = {
    '6/7': 'OPUS5-E6 6/7 - Tamamlama ailesi yuvalari',
    '7/7': 'OPUS5-E6 7/7 - Kalanlar + tam test butunlugu kontrolu',
}

LISTE = 'content/DOGRULAMA/yeniden-uretim-listesi.json'
j = json.load(open(LISTE, encoding='utf-8'))

cache = {}
dolan = 0
for x in j['elenen']:
    if x.get('yeniden_uretildi'):
        continue
    f = x['dosya']
    if f not in cache:
        cache[f] = json.load(open(f, encoding='utf-8'))
    it = next(i for i in cache[f]['items'] if i['number'] == x['numara'])
    yr = it['yeniden_uretim']
    etiket = '7/7' if '(7/7)' in yr['kaynak_prompt'] else '6/7'
    x['yeniden_uretildi'] = {
        'tarih': yr['tarih'],
        'calistirma': CALISTIRMA[etiket],
        'model': it.get('generated_by', 'opus'),
        'yeni_ifade': it['prompt'],
    }
    dolan += 1

with open(LISTE, 'w', encoding='utf-8') as fh:
    json.dump(j, fh, ensure_ascii=False, indent=2)
    fh.write('\n')

kalan = sum(1 for x in j['elenen'] if not x.get('yeniden_uretildi'))
print('dolduruldu:', dolan, '| listede kalan bos yuva:', kalan, '| toplam:', len(j['elenen']))
