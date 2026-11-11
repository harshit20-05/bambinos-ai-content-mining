import json

with open('scripts/english_parsed.json', 'r', encoding='utf-8') as f:
    cues = json.load(f)

for c in cues:
    # Print cues between 05:00 and 20:00
    if '00:08:' in c['start'] or '00:09:' in c['start'] or '00:10:' in c['start'] or '00:11:' in c['start'] or '00:12:' in c['start'] or '00:13:' in c['start'] or '00:14:' in c['start'] or '00:15:' in c['start'] or '00:16:' in c['start']:
        print(f"[{c['start']} -> {c['end']}] {c['text']}")

