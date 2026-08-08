# -*- coding: utf-8 -*-
"""Elden gecirilen cumle sonu eslestirme sorularini birlestirip basar."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortak  # noqa: E402

d = ortak.oku('content/reading/practice/matching-sentence-endings.json')
for g in d['groups']:
    opts = dict((o['key'], o['text']) for o in g['option_list']['options'])
    print('==', g['group_id'], g['passage_id'])
    for k in sorted(opts):
        print('   ', k, opts[k])
    for it in g['items']:
        a = it['answer'][0]
        print(' %2d %s' % (it['number'], it['prompt']))
        print('     -> %s %s' % (a, opts[a]))
