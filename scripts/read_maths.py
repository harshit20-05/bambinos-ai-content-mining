import json

with open('scripts/maths_parsed.json', 'r', encoding='utf-8') as f:
    cues = json.load(f)

print(f"Total Maths Cues: {len(cues)}")
for i, c in enumerate(cues):
    print(f"[{c['start']} -> {c['end']}] {c['text']}")

