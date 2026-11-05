"""Exporta los sprites de partido dibujados en vectores (body.py y las cabezas head_*.py) a pixel art.

Escribe src/assets/pack/vsprites/<equipo>/<jugador>/{front,back,side0,side1,side2}.png:
- front/back: de frente y de espaldas; side0: de perfil mirando a la derecha; side1/side2: pasos de carrera.
- Todos con la misma escala (REF_PX de alto para el cuerpo normal): los altos miden más que los bajitos.

Uso (desde la raíz del repo): python3 -I tools/pixelart/vector/export.py
"""
import os
import sys

from PIL import Image, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, HERE)
import body as B  # noqa: E402
import chars as C  # noqa: E402
import json  # noqa: E402

B.V.OFF = 0
REF_PX = 64
OUT = (60, 24, 16, 255)

# equipos con todos sus jugadores dibujados (packs): se exportan con los colores de cada equipo
TEAMS = ['ie1-raimon']
# dibujos que no están en chars.py (Axel tiene su propio módulo, head_axel.py)
SPECIAL = {'axel-blaze': None}


def ref_height():
    bb = B.figure('front', 'normal').getbbox()
    return bb[3] - bb[1]


def pixel(im, k):
    """Reduce el dibujo con la escala k, colores duros y un contorno de 1 px."""
    im = im.crop(im.getbbox())
    w, h = max(1, round(im.width * k)), max(1, round(im.height * k))
    s = im.resize((w, h), Image.LANCZOS)
    a = s.split()[3].point(lambda v: 255 if v > 120 else 0)
    rgb = s.convert('RGB').quantize(colors=24, method=Image.MEDIANCUT, dither=Image.Dither.NONE).convert('RGBA')
    rgb.putalpha(a)
    ring = a.filter(ImageFilter.MaxFilter(3))
    out = Image.new('RGBA', (w + 2, h + 2))
    ol = Image.new('RGBA', (w, h), OUT)
    ol.putalpha(ring)
    out.alpha_composite(ol, (1, 1))
    out.alpha_composite(rgb, (1, 1))
    return out


def char_of(pid):
    """Ficha del personaje (por id; las versiones como mark-evans-endou-b usan la del original)."""
    for base in sorted(list(C.CHARS) + list(SPECIAL), key=len, reverse=True):
        if pid == base or pid.startswith(base + '-'):
            return base
    return None


def frames(base, kit, num):
    k = REF_PX / ref_height()
    ch = C.CHARS.get(base)
    tname = ch['body'] if ch else 'normal'
    fig = lambda v, st=0: B.figure(v, tname, st, ch, kit, num)
    return {'front': pixel(fig('front'), k), 'back': pixel(fig('back'), k), 'side0': pixel(fig('side'), k),
            'side1': pixel(fig('side', 1), k), 'side2': pixel(fig('side', 2), k)}


def pad_same(fr):
    """Mismo lienzo para todos los fotogramas, con los pies abajo y centrados, para que no bailen al cambiar."""
    W = max(i.width for i in fr.values())
    H = max(i.height for i in fr.values())
    out = {}
    for name, im in fr.items():
        c = Image.new('RGBA', (W, H))
        c.alpha_composite(im, ((W - im.width) // 2, H - im.height))
        out[name] = c
    return out


def main():
    for tid in TEAMS:
        team = json.load(open(os.path.join(ROOT, 'src', 'data', 'teams', tid + '.json'), encoding='utf-8'))
        for p in team['players']:
            base = char_of(p['id'])
            if base is None:
                print(tid, p['id'], 'sin dibujo')
                continue
            kit = B.kit_for(team['colors'], p['position'] == 'GK')
            dest = os.path.join(ROOT, 'src', 'assets', 'pack', 'vsprites', tid, p['id'])
            os.makedirs(dest, exist_ok=True)
            for name, im in pad_same(frames(base, kit, str(p['number']))).items():
                im.save(os.path.join(dest, name + '.png'))
        print(tid, 'ok')


if __name__ == '__main__':
    main()
