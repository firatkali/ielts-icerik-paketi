# -*- coding: utf-8 -*-
"""E5/3 - elenen yuvalari E6'nin devir dosyasina ekler (uzerine yazmaz)."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

LISTE = 'content/DOGRULAMA/yeniden-uretim-listesi.json'

KAYNAK = [
    'content/reading/practice/matching-features.json',
    'content/reading/tests/AC2/matching-features.json',
    'content/reading/tests/AC4/matching-features.json',
]

PASAJ = {
    ('content/reading/practice/matching-features.json', 1): 'A10',
    ('content/reading/practice/matching-features.json', 5): 'A10',
    ('content/reading/tests/AC2/matching-features.json', 24): 'A05',
    ('content/reading/tests/AC2/matching-features.json', 25): 'A05',
    ('content/reading/tests/AC2/matching-features.json', 26): 'A05',
    ('content/reading/tests/AC4/matching-features.json', 24): 'A11',
}


def main():
    d = ortak.oku(LISTE)
    var = set((k['dosya'], k['numara']) for k in d['elenen'])
    eklendi = 0

    for yol in KAYNAK:
        s = ortak.oku(yol)
        for g, it in ortak.kumeli_sorular(s):
            if it.get('status') != 'rejected':
                continue
            anahtar = (yol, it['number'])
            if anahtar not in PASAJ or anahtar in var:
                continue
            d['elenen'].append({
                'dosya': yol,
                'numara': it['number'],
                'tip': s['question_type'],
                'pasaj': PASAJ[anahtar],
                'kacinilacak': {
                    'kanit_cumlesi': it['evidence'],
                    'ifade': it['prompt'],
                },
                'neden_elendi': it['reject_reason'],
            })
            eklendi += 1

    ortak.yaz(LISTE, d)
    print('eklenen kayit: %d - listedeki toplam: %d' % (eklendi, len(d['elenen'])))


if __name__ == '__main__':
    main()
