# -*- coding: utf-8 -*-
"""E5/4 - elenen yuvalari E6'nin devir dosyasina ekler (uzerine yazmaz)."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402
from _e5_comp_elden_gecir import ELEME  # noqa: E402

LISTE = 'content/DOGRULAMA/yeniden-uretim-listesi.json'


def main():
    d = ortak.oku(LISTE)
    var = set((k['dosya'], k['numara']) for k in d['elenen'])
    eklendi = 0

    for yol in sorted(set(y for y, _ in ELEME)):
        s = ortak.oku(yol)
        for it in ortak.sorular(s):
            anahtar = (yol, it['number'])
            if anahtar not in ELEME or anahtar in var:
                continue
            if it.get('status') != 'rejected':
                raise SystemExit('elenmis olmasi gerekiyordu: %s' % (anahtar,))
            d['elenen'].append({
                'dosya': yol,
                'numara': it['number'],
                'tip': s['question_type'],
                'pasaj': it.get('passage_id') or s.get('passage_id'),
                'kacinilacak': {
                    'kanit_cumlesi': it['evidence'],
                    'ifade': it['prompt'],
                },
                'neden_elendi': it['reject_reason'],
            })
            eklendi += 1

    ortak.yaz(LISTE, d)
    print('eklenen kayit: %d - listedeki toplam: %d'
          % (eklendi, len(d['elenen'])))


if __name__ == '__main__':
    main()
