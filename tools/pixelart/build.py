"""Compone el pixel art de los partidos y lo exporta para el juego.

- Cabezas: los peinados de styles.py (tres vistas), con el pelo sombreado y el contorno puestos solos.
- Cuerpos: body.py (frente, espalda y perfil con dos pasos de carrera), sacados del prototipo de Mark.
- Exporta src/gfx/pixelart.json, que el juego colorea con los colores de cada jugador y de su equipo.

Uso (desde la raíz del repo):
  python3 -I tools/pixelart/build.py               # exporta
  python3 -I tools/pixelart/build.py preview.png   # además, una hoja con todos los peinados
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import body  # noqa: E402
from styles import FACES, STYLES  # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
W = 24
HEAD_H = 20
HAIR = set('Hhd')
SKIN = set('Sxseiwm')


def full(row):
    if row is None:
        return None
    if len(row) == 12:
        row = row + row[::-1]
    assert len(row) == W, (len(row), row)
    return row


def face(spec, default):
    if isinstance(spec, str):
        return list(FACES[spec])
    base = FACES[default]
    return [r if r is not None else base[i] for i, r in enumerate(spec + [None] * (8 - len(spec)))]


def shade(g):
    """Luces arriba a la izquierda y sombra abajo y a la derecha, solo en el pelo sin forzar."""
    H = len(g)
    src = [list(r) for r in g]
    out = [list(r) for r in g]
    at = lambda x, y: src[y][x] if 0 <= y < H and 0 <= x < W else '.'
    for y in range(H):
        for x in range(W):
            if src[y][x] != 'h':
                continue
            up, down, right = at(x, y - 1), at(x, y + 1), at(x + 1, y)
            if up in '.o' and x < 16:
                out[y][x] = 'H'
            elif down in SKIN or down in '.o' or (right in '.o' and x >= 14):
                out[y][x] = 'd'
    return [''.join(r) for r in out]


def outline(g):
    H = len(g)
    out = [list(r) for r in g]
    for y in range(H):
        for x in range(W):
            if g[y][x] != '.':
                continue
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                X, Y = x + dx, y + dy
                if 0 <= X < W and 0 <= Y < H and g[Y][X] not in '.o':
                    out[y][x] = 'o'
                    break
    return [''.join(r) for r in out]


def head(style, view):
    s = STYLES[style]
    default = {'front': 'burn', 'side': 'side', 'back': 'back'}[view]
    top = [full(r) for r in s[view + '_top']]
    assert len(top) == 12, (style, view, len(top))
    rows = top + [full(r) for r in face(s.get(view + '_face', default), default)]
    rows += [full(r) for r in s.get(view + '_extra', [])]
    return outline(shade(rows))


def lift(rows, left):
    """Paso de carrera de frente o de espaldas: la pierna sube dos filas (se quitan una de rodilla y una de media)."""
    g = [list(r) for r in rows]
    x0, x1 = (0, 12) if left else (12, 24)
    legs = [r[x0:x1] for r in g[11:]]
    keep = [r for i, r in enumerate(legs) if i not in (2, 4)]
    keep += [['.'] * 12] * (len(legs) - len(keep))
    for i, r in enumerate(keep):
        g[11 + i][x0:x1] = r
    return [''.join(r) for r in g]


def body_frames():
    return {
        'front': [body.BODY_FRONT, lift(body.BODY_FRONT, True), lift(body.BODY_FRONT, False)],
        'back': [body.BODY_BACK, lift(body.BODY_BACK, False), lift(body.BODY_BACK, True)],
        'side': [body.BODY_SIDE_STAND, body.BODY_SIDE_A, body.BODY_SIDE_B],
    }


def compose(hd, bd):
    """Cabeza sobre el cuerpo: la cabeza ocupa las filas 0-19 y lo que sobra (pelo largo) pisa el cuerpo."""
    g = [list(r) for r in ['.' * W] * HEAD_H + list(bd)]
    for y, r in enumerate(hd):
        for x, c in enumerate(r):
            if c != '.' and y < len(g):
                g[y][x] = c
    return [''.join(r) for r in g]


def export():
    data = {
        'w': W,
        'headH': HEAD_H,
        'body': body_frames(),
        'styles': {name: {v: head(name, v) for v in ('front', 'side', 'back')} for name in STYLES},
    }
    with open(os.path.join(ROOT, 'src', 'gfx', 'pixelart.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, separators=(',', ':'))
    return data


# ------------------------------------------------------------------ vista previa

PREVIEW = {
    'o': '#2a1610', 'H': '#8a6040', 'h': '#5e3a22', 'd': '#3c2414',
    'R': '#ff9a4a', 'r': '#ee6418', 'q': '#b8400c',
    'S': '#ffe2c2', 's': '#f9c69c', 'x': '#df9c72', 'e': '#1c1210', 'i': '#3e2212', 'w': '#ffffff', 'm': '#b4583e',
    'T': '#ffd75a', 't': '#f2c230', 'y': '#b88e10', 'A': '#ffd75a', 'a': '#f2c230', 'z': '#b88e10',
    'C': '#4a7fe0', 'c': '#2a5fc0', 'G': '#f9c69c', 'g': '#df9c72',
    'P': '#4a7fe0', 'p': '#2a5fc0', 'n': '#1a3f88', 'K': '#ffffff', 'k': '#cfd6dc', 'v': '#2a5fc0', 'V': '#1a3f88',
    'B': '#3a3a46', 'b': '#1e1e26', 'N': '#ffffff',
}


def render(g, scale, pal=PREVIEW):
    from PIL import Image
    im = Image.new('RGBA', (W, len(g)))
    for y, r in enumerate(g):
        for x, c in enumerate(r):
            if c in pal:
                v = pal[c]
                im.putpixel((x, y), (int(v[1:3], 16), int(v[3:5], 16), int(v[5:7], 16), 255))
    return im.resize((W * scale, len(g) * scale), Image.NEAREST)


def preview(path, data, names=None):
    from PIL import Image, ImageDraw
    names = names or list(data['styles'])
    sc = 5
    cw, ch = (W + 2) * sc, 44 * sc
    frames = [('front', 0), ('side', 0), ('side', 1), ('back', 0)]
    im = Image.new('RGBA', (len(frames) * cw + 20, len(names) * ch), (46, 120, 58, 255))
    d = ImageDraw.Draw(im)
    for r, name in enumerate(names):
        for c, (v, k) in enumerate(frames):
            g = compose(data['styles'][name][v], data['body'][v][k])
            im.alpha_composite(render(g, sc), (10 + c * cw, r * ch + 4))
        d.text((4, r * ch + 2), name, fill=(255, 255, 255))
    im.save(path)


if __name__ == '__main__':
    data = export()
    if len(sys.argv) > 1:
        preview(sys.argv[1], data, sys.argv[2].split(',') if len(sys.argv) > 2 else None)
    print(len(data['styles']), 'peinados')
