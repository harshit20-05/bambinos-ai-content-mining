import re
import os
import json

def parse_vtt(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    cues = []
    blocks = re.split(r'\n\s*\n', content)
    for b in blocks:
        lines = b.strip().split('\n')
        if not lines or lines[0].startswith('WEBVTT') or lines[0].startswith('NOTE'):
            continue
        ts_line = None
        text_lines = []
        for l in lines:
            if '-->' in l:
                ts_line = l
            elif ts_line:
                text_lines.append(l)
        if ts_line and text_lines:
            match = re.search(r'([\d:.]+)\s*-->\s*([\d:.]+)', ts_line)
            if match:
                cues.append({'start': match.group(1), 'end': match.group(2), 'text': ' '.join(text_lines)})
    return cues

files = {
    'English': 'repo/marketing/transcripts/English_2125604619.vtt',
    'Gita': 'repo/marketing/transcripts/Gita_2125422751.vtt',
    'Maths': 'repo/marketing/transcripts/Maths_2125736982.vtt',
    'Science': 'repo/marketing/transcripts/Science_2125687282.vtt'
}

for name, path in files.items():
    cues = parse_vtt(path)
    out_path = f'scripts/{name.lower()}_parsed.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(cues, f, indent=2)
    print(f'{name}: {len(cues)} cues saved to {out_path}')

