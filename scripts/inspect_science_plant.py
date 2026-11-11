import json

with open('scripts/science_parsed.json', 'r', encoding='utf-8') as f:
    cues = json.load(f)

for c in cues:
    if '00:16:' in c['start'] or '00:17:' in c['start'] or '00:18:' in c['start'] or '00:19:' in c['start']:
        print(f"[{c['start']} -> {c['end']}] {c['text']}")

