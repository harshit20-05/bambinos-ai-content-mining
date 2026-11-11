import json

def inspect_cues(parsed_json_path, subject):
    with open(parsed_json_path, 'r', encoding='utf-8') as f:
        cues = json.load(f)
    print(f"================ {subject} ({len(cues)} cues) ================")
    # Print segments with high interaction, praise, explanations, questions
    for i, c in enumerate(cues):
        t = c['text']
        # Filter for interesting keywords or dialogues longer than 40 chars
        if any(w in t.lower() for w in ['story', 'mountain', 'character', 'shloka', 'krishna', 'arjuna', 'gravity', 'water', 'air', 'experiment', 'excellent', 'wow', 'superb', 'awesome', 'tell me', 'because']):
            print(f"[{c['start']} -> {c['end']}] {t[:120]}")

inspect_cues('scripts/english_parsed.json', 'ENGLISH')

