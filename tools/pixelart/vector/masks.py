"""Mapas de equipación de los sprites dibujados, para vestir a los jugadores de Mi club con otro uniforme.

Para cada sprite (src/assets/pack/vsprites/<equipo>/<jugador>/<vista>.png) escribe al lado mask-<vista>.png: en cada
píxel que es ropa, R = 16 * papel (camiseta, mangas, pantalón...) y G = 255 * tono (1 = color base, menos = sombra);
el resto, negro. El juego (src/club/uniforms.ts) cambia esos píxeles por los colores del uniforme.

Cómo: se vuelve a dibujar el jugador con una equipación "en clave" (cada papel con un color puro G = 0 cuya proporción
B/R dice cuál es) y se compara con el sprite ya exportado: solo se marcan los píxeles que en el sprite tienen de verdad
el color de ese papel de su equipación (así no se pinta nada que no sea ropa).

Uso (desde la raíz del repo): python3 -I tools/pixelart/vector/masks.py [ids de equipo...] [--jobs=4]
"""
import os
import sys
from multiprocessing import Pool

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import export as E  # noqa: E402
import body as B  # noqa: E402
import json  # noqa: E402

# papeles de la equipación (el índice va en el mapa; src/club/uniforms.ts tiene la misma lista)
ROLES = ['shirt', 'sleeve', 'shorts', 'sock', 'stripe', 'collar', 'num', 'zig', 'vstripes', 'pants', 'hand']
SHADE = {'shirt_d': ('shirt', 0.84), 'sleeve_d': ('sleeve', 0.75), 'shorts_d': ('shorts', 0.72), 'sock_d': ('sock', 0.78)}


def code(i):
    """Color en clave del papel i (1..): rojo y azul en proporción i/15, sin verde."""
    return (240, 0, 16 * i, 255)


def resolved(kit):
    """Color con el que se dibuja cada papel en esta equipación (los que faltan caen en otro, como en body.py)."""
    out = {'shirt': kit['shirt'], 'sleeve': kit['sleeve'], 'shorts': kit['shorts'], 'sock': kit['sock'], 'stripe': kit['stripe'],
           'collar': kit.get('collar', kit['sleeve']), 'num': kit.get('num', kit['sleeve']), 'pants': kit.get('pants', kit['shorts'])}
    for k in ('zig', 'vstripes', 'hand'):
        if k in kit:
            out[k] = kit[k]
    return out


def coded_kit(kit):
    k = dict(kit)
    for r in resolved(kit):
        k[r] = code(ROLES.index(r) + 1)
    for d, (base, f) in SHADE.items():
        k[d] = B.tone(k[base], f)
    return k


def decode(px):
    """(papel, tono) de un píxel del dibujo en clave, o None."""
    r, g, b = px[:3]
    if g != 0 or r < 50:
        return None
    i = round(b * 15 / r)
    if not 1 <= i <= len(ROLES):
        return None
    return ROLES[i - 1], r / 240


def mask_of(sprite, coded, cols, kit=None):
    w, h = sprite.size
    m = Image.new('RGB', (w, h))
    sp, cp = sprite.load(), coded.load()
    # tonos de cada papel que hay en la equipación de verdad (base y sombras de body.py)
    tones = [1.0, 0.84, 0.75, 0.72, 0.78, 0.8]

    def same(a, c, f):
        return all(abs(a[i] - min(255, int(c[i] * f))) <= 6 for i in range(3))

    for y in range(h):
        for x in range(w):
            a = sp[x, y]
            if a[3] == 0:
                continue
            got = decode(cp[x, y])
            hit = None
            # 1) lo que dice el dibujo en clave, si el sprite tiene de verdad ese color
            if got and got[0] in cols and same(a, cols[got[0]], got[1]):
                hit = got
            else:
                # 2) el sprite tiene ahí un color de la equipación (el contorno suavizado cae a veces en otro papel):
                # se toma el papel que dice la clave si lo hay, y si no, el primero que tenga ese color
                for role, c in cols.items():
                    f = next((f for f in tones if same(a, c, f)), None)
                    if f is not None:
                        hit = (got[0], f) if got and got[0] in cols and same(a, cols[got[0]], f) else (role, f)
                        break
                # 3) sombras que no son un tono exacto de su color (las medias blancas por defecto)
                if not hit and kit:
                    for d, (base, f) in SHADE.items():
                        if d in kit and same(a, kit[d], 1.0):
                            hit = (base, f)
                            break
            if hit:
                role, f = hit
                m.putpixel((x, y), ((ROLES.index(role) + 1) * 16, max(1, min(255, round(f * 255))), 0))
    return m


def job(args):
    tid, pid, base, colors, gk, num = args
    kit = B.kit_for(colors, gk)
    dest = os.path.join(E.ROOT, 'src', 'assets', 'pack', 'vsprites', tid, pid)
    if not os.path.isdir(dest):
        return 0
    coded = E.pad_same(E.frames(base, coded_kit(kit), num))
    cols = resolved(kit)
    n = 0
    for view, im in coded.items():
        f = os.path.join(dest, view + '.png')
        if not os.path.exists(f):
            continue
        sprite = Image.open(f).convert('RGBA')
        if sprite.size != im.size:
            continue
        mask_of(sprite, im, cols, kit).save(os.path.join(dest, f'mask-{view}.png'), optimize=True)
        n += 1
    return n


def jobs_for(only):
    out = []
    for tid in E.TEAMS + E.SCOUTS:
        if only and tid not in only:
            continue
        scouts = tid in E.SCOUTS
        team = E.load_team(tid)
        for p in team['players']:
            base = (f"{tid}:{p['id']}" if f"{tid}:{p['id']}" in E.C.CHARS else None) if scouts else E.key_for(tid, p['id'])
            if base is None:
                continue
            src = team['colors'].get('kitFrom', {}).get(p['id'])
            colors = json.load(open(os.path.join(E.ROOT, 'src', 'data', 'teams', src + '.json'), encoding='utf-8'))['colors'] if src else team['colors']
            out.append((tid, p['id'], base, colors, p['position'] == 'GK', '' if scouts else str(p['number'])))
    return out


def main():
    only = [a for a in sys.argv[1:] if not a.startswith('--')]
    n = next((int(a[7:]) for a in sys.argv[1:] if a.startswith('--jobs=')), os.cpu_count() or 1)
    todo = jobs_for(only)
    done = 0
    with Pool(n) as pool:
        for i, k in enumerate(pool.imap_unordered(job, todo, chunksize=4)):
            done += k
            if i % 200 == 0:
                print(f'{i}/{len(todo)}', flush=True)
    print('mapas:', done)


if __name__ == '__main__':
    main()
