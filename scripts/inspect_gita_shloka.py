import json

with open('scripts/gita_parsed.json', 'r', encoding='utf-8') as f:
    cues = json.load(f)

for c in cues:
    if '00:46:' in c['start'] or '00:47:' in c['start'] or '00:48:' in c['start'] or '00:49:' in c['start']:
        print(f"[{c['start']} -> {c['end']}] {c['text']}")

