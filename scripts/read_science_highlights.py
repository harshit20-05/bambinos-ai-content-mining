import json

def inspect_cues(parsed_json_path, subject):
    with open(parsed_json_path, 'r', encoding='utf-8') as f:
        cues = json.load(f)
    print(f"================ {subject} ({len(cues)} cues) ================")
    for i, c in enumerate(cues):
        t = c['text']
        if any(w in t.lower() for w in ['water', 'air', 'glass', 'experiment', 'see', 'look', 'why', 'sink', 'float', 'heavy', 'light', 'candle', 'fire', 'magic', 'wow', 'superb', 'tell me', 'paper', 'tissue']):
            print(f"[{c['start']} -> {c['end']}] {t[:120]}")

inspect_cues('scripts/science_parsed.json', 'SCIENCE')

