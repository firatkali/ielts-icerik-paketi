"""Gecici yardimci: dogrulama/cevap/ altindaki cevaplari tek varyanta indirir
ve bu oturuma ait olmayan (okuma) cevap dosyalarini siler."""

import glob
import json
import os

silinen = 0
for p in glob.glob('dogrulama/cevap/content__reading__*.json'):
    os.remove(p)
    silinen += 1

duzeltilen = 0
for p in glob.glob('dogrulama/cevap/*.json'):
    with open(p, encoding='utf-8') as f:
        d = json.load(f)
    degisti = False
    for a in d.get('answers', []):
        if isinstance(a.get('answer'), list) and len(a['answer']) > 1:
            a['answer'] = a['answer'][:1]
            degisti = True
    if degisti:
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
        duzeltilen += 1

print('silinen okuma dosyasi:', silinen)
print('tek varyanta indirilen dosya:', duzeltilen)
print('kalan cevap dosyasi:', len(glob.glob('dogrulama/cevap/*.json')))
