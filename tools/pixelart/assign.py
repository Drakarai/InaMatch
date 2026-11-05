"""Elige el peinado del pixel art para cada jugador: el que más se parece a la silueta de su retrato.

src/data/looks.json trae, de cada retrato, una rejilla de la cabeza (22x20: # pelo, a accesorio, s piel, e ojos).
Se compara con la vista de frente de cada peinado (recortada y llevada al mismo tamaño) casilla a casilla
(pelo, piel o vacío), y se guarda el mejor en el campo "style" de cada jugador.
Los personajes con peinado propio van en OWN.

Uso (desde la raíz del repo): python3 -I tools/pixelart/assign.py
"""
import json
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
import build  # noqa: E402

# peinados dibujados para un personaje concreto (id del jugador, sin el sufijo de versión)
OWN = {'mark-evans': 'mark'}
GW, GH = 22, 20


def cat(c):
    if c in 'Hhd#aRrq':
        return 'h'
    if c in 'SsxeiwmS':
        return 's'
    return '.'


def norm(rows):
    """Recorta lo que no es vacío y lo lleva a GW x GH (vecino más cercano)."""
    cells = [(x, y) for y, r in enumerate(rows) for x, c in enumerate(r) if cat(c) != '.']
    if not cells:
        return ['.' * GW] * GH
    x0, x1 = min(x for x, _ in cells), max(x for x, _ in cells) + 1
    y0, y1 = min(y for _, y in cells), max(y for _, y in cells) + 1
    out = []
    for y in range(GH):
        sy = y0 + (y * (y1 - y0)) // GH
        out.append(''.join(cat(rows[sy][x0 + (x * (x1 - x0)) // GW]) for x in range(GW)))
    return out


def score(a, b):
    s = 0
    for ra, rb in zip(a, b):
        for ca, cb in zip(ra, rb):
            if ca == cb:
                s += 2 if ca == 'h' else 1
            elif '.' not in (ca, cb):
                s -= 1
    return s


def main():
    path = os.path.join(ROOT, 'src', 'data', 'looks.json')
    looks = json.load(open(path, encoding='utf-8'))
    shapes = {name: norm(build.head(name, 'front')[:build.HEAD_H]) for name in build.STYLES if name != 'mark'}
    count = Counter()
    for key, look in looks.items():
        pid = key.split(':', 1)[1]
        own = next((s for base, s in OWN.items() if pid == base or pid.startswith(base + '-')), None)
        if own:
            style = own
        else:
            mask = norm([r.replace('e', 's') for r in look.get('head', [])])
            hair = sum(r.count('h') for r in mask)
            style = 'bald' if hair < 25 else max(shapes, key=lambda n: score(mask, shapes[n]) if n != 'bald' else -1e9)
        look['style'] = style
        count[style] += 1
    with open(path, 'w', encoding='utf-8') as f:
        f.write('{\n' + ',\n'.join(f' {json.dumps(k)}: {json.dumps(v)}' for k, v in sorted(looks.items())) + '\n}\n')
    print(dict(count.most_common()))


if __name__ == '__main__':
    main()
