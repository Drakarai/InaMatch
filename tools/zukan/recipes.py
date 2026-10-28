"""Genera src/data/movefx.json: la receta del efecto especial de cada supertécnica.

- tools/zukan/recipes.txt: forma, variante y capas de cada técnica, anotadas mirando su vídeo en la
  enciclopedia oficial (zukan.inazuma.jp).
- tools/zukan/palette.json: colores reales de cada vídeo (tools/zukan/palette.py).
- tools/wiki/movefx_wiki.json: para las que no salen en la enciclopedia, el efecto deducido de su
  descripción en la wiki (tools/wiki/vfx.py), salvo las de FALLBACK, puestas a mano.

Uso (desde la raíz del repo): python3 -I tools/zukan/recipes.py
"""
import json
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
HERE = os.path.dirname(os.path.abspath(__file__))

# técnicas que no están en la enciclopedia, a partir de su imagen en la wiki
FALLBACK = {
    'judge-through': 'impact:kick',
    'judge-through-2': 'impact:kick +impact:spark',
    'judge-through-3': 'impact:kick +fire:burst',
    'lightning-accel': 'lightning:zigzag +speedlines',
    'naraku-otoshi': 'dark:hole',
    'heat-tackle': 'fire:dash',
    'illusion-ball': 'clone:balls +light:rays',
    'go-to-hell': 'dark:vortex +dark:curse',
    'go-to-heaven': 'light:pillar +wings:angel',
    'ignite-steal': 'fire:trail',
    'electrap': 'lightning:barrier',
}


def parse(line):
    mid, rest = line.split(':', 1)
    toks = rest.split()
    return mid.strip(), {'fx': toks[0], 'layers': [t[1:] for t in toks[1:] if t.startswith('+')]}


def main():
    notes = {}
    for line in open(os.path.join(HERE, 'recipes.txt'), encoding='utf-8'):
        line = line.strip()
        if line and not line.startswith('#'):
            mid, r = parse(line)
            notes[mid] = r
    for mid, text in FALLBACK.items():
        notes.setdefault(mid, parse(f'{mid}: {text}')[1])
    palette = json.load(open(os.path.join(HERE, 'palette.json')))
    wiki = json.load(open(os.path.join(ROOT, 'tools', 'wiki', 'movefx_wiki.json')))
    moves = json.load(open(os.path.join(ROOT, 'src', 'data', 'moves.json'), encoding='utf-8'))
    out = {}
    missing = []
    for m in moves:
        r = dict(notes.get(m['id']) or {'fx': wiki.get(m['id'], 'impact'), 'layers': []})
        if m['id'] not in notes:
            missing.append(m['id'])
        if not r['layers']:
            del r['layers']
        if palette.get(m['id']):
            r['colors'] = palette[m['id']]
        out[m['id']] = r
    with open(os.path.join(ROOT, 'src', 'data', 'movefx.json'), 'w', encoding='utf-8') as f:
        f.write('{\n' + ',\n'.join(f' {json.dumps(k)}: {json.dumps(v)}' for k, v in sorted(out.items())) + '\n}\n')
    print(len(out), 'técnicas;', len(out) - len(missing), 'con receta del vídeo', file=sys.stderr)
    if missing:
        print('sin receta (efecto de la wiki):', ', '.join(missing), file=sys.stderr)


if __name__ == '__main__':
    main()
