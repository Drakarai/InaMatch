"""Exporta los sprites de partido dibujados en vectores (body.py y las cabezas head_*.py) a pixel art.

Escribe src/assets/pack/vsprites/<equipo>/<jugador>/{front,back,side0,side1,side2}.png:
- front/back: de frente y de espaldas; side0: de perfil mirando a la derecha; side1/side2: pasos de carrera.
- Todos con la misma escala (REF_PX de alto para el cuerpo normal): los altos miden más que los bajitos.

Uso (desde la raíz del repo): python3 -I tools/pixelart/vector/export.py [ids de equipo...]
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
REF_PX = 80
OUT = (60, 24, 16, 255)

# equipos con todos sus jugadores dibujados (packs): se exportan con los colores de cada equipo
TEAMS = ['ie1-raimon', 'ie1-teikoku-gakuen', 'ie1-occult', 'ie1-nose', 'ie1-shuuyou-meito-gakuen', 'ie1-ichibangai-sally-s', 'ie1-sengoku-igajima', 'ie1-kidokawa-seishuu', 'ie1-mikage-sennou', 'ie1-zeus', 'ie1-senbayama', 'ie1-kasamino', 'ie1-inazuma-kfc', 'ie1-inazuma-eleven', 'ie2-second-raimon', 'ie2-dark-emperors', 'ie2-young-inazuma', 'ie2-gemini-storm', 'ie2-epsilon', 'ie2-epsilon-kai', 'ie2-diamond-dust', 'ie2-prominence', 'ie2-chaos', 'ie2-the-genesis', 'ie2-hakuren', 'ie2-jukai-team', 'ie2-keibi-machines', 'ie2-manyuuji', 'cs-soccer-robots', 'gx-osoroshii-kage', 'ie2-osaka-gals-ccc', 'ie2-oumihara', 'ie2-shin-teikoku-gakuen', 'ie2-sp-fixers', 'ie2-yokato', 'ie3-inazuma-japan', 'ie3-nippon-daihyou-kouho-a', 'ie3-nippon-daihyou-kouho-b', 'ie3-neo-japan', 'ie3-big-waves', 'ie3-desert-lion', 'ie3-fire-dragon']
# dibujos que no están en chars.py (Axel tiene su propio módulo, head_axel.py)
SPECIAL = {}


def ref_height():
    bb = B.figure('front', 'normal').getbbox()
    return bb[3] - bb[1]


def pixel(im, k):
    """Reduce el dibujo con la escala k a pixel art limpio: cada píxel toma el color plano más cercano del propio
    dibujo (sin tonos intermedios borrosos) y la silueta lleva un contorno de 1 px."""
    im = im.crop(im.getbbox())
    w, h = max(1, round(im.width * k)), max(1, round(im.height * k))
    # paleta: los colores planos del dibujo (los que ocupan bastante superficie)
    counts = im.getcolors(1 << 20)
    total = sum(c for c, _ in counts if _[3] == 255)
    pal = [col[:3] for c, col in counts if col[3] == 255 and c > total * 0.0004]
    s = im.resize((w, h), Image.BOX)
    a = s.split()[3].point(lambda v: 255 if v > 110 else 0)
    out_px = []
    for (r, g, b, al) in s.getdata():
        if al < 20:
            out_px.append((0, 0, 0, 0))
            continue
        # el color sin el fondo transparente
        r, g, b = (r * 255 // al, g * 255 // al, b * 255 // al) if al < 255 else (r, g, b)
        best = min(pal, key=lambda p: (p[0] - r) ** 2 + (p[1] - g) ** 2 + (p[2] - b) ** 2)
        out_px.append(best + (255,))
    flat = Image.new('RGBA', (w, h))
    flat.putdata(out_px)
    flat.putalpha(a)
    ring = a.filter(ImageFilter.MaxFilter(3))
    out = Image.new('RGBA', (w + 2, h + 2))
    ol = Image.new('RGBA', (w, h), OUT)
    ol.putalpha(ring)
    out.alpha_composite(ol, (1, 1))
    out.alpha_composite(flat, (1, 1))
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


def key_for(tid, pid):
    """Dibujo de un jugador en un equipo: la versión de ese equipo ('<equipo>:<jugador>'), la de su temporada ('ie3:<jugador>':
    el aspecto que tiene en ese juego) o la suya de siempre."""
    for k in (f'{tid}:{pid}', f"{tid.split('-')[0]}:{pid}"):
        if k in C.CHARS:
            return k
    return char_of(pid)


def main():
    only = sys.argv[1:]  # ids de equipo: solo esos (sin argumentos, todos)
    for tid in TEAMS:
        if only and tid not in only:
            continue
        team = json.load(open(os.path.join(ROOT, 'src', 'data', 'teams', tid + '.json'), encoding='utf-8'))
        for p in team['players']:
            # versión propia de este equipo (los Jóvenes Inazuma son los veteranos de niños): '<equipo>:<jugador>'
            base = key_for(tid, p['id'])
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
