import json

j = json.load(open('content/DOGRULAMA/yeniden-uretim-listesi.json', encoding='utf-8'))
pending = [x for x in j['elenen'] if not x.get('yeniden_uretildi')
           and x['tip'] in ('true_false_not_given', 'short_answer')]
for x in pending:
    print('=' * 70)
    print(json.dumps(x, ensure_ascii=False, indent=1))
