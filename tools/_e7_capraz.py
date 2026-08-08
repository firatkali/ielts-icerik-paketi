import json, glob, sys

pid = sys.argv[1]
for f in glob.glob('content/reading/**/*.json', recursive=True):
    d = json.load(open(f, encoding='utf-8'))
    if not isinstance(d, dict) or 'items' not in d:
        continue
    fp = d.get('passage_id')
    for it in d['items']:
        p = it.get('passage_id') or fp
        if p != pid:
            continue
        loc = it.get('evidence_locator') or {}
        print('%-55s %-6s %s/%s  %s' % (f.replace('content/reading/', ''), it.get('number'),
                                        loc.get('paragraph'), loc.get('sentence'),
                                        (it.get('prompt') or it.get('statement') or '')[:70]))
