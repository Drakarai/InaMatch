"""Correcciones de la revisión de diseños (grupo sc_ie2b): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda."""
import copy  # noqa: F401
from chars import CHARS, L, OUTC, blob, ell, outline  # noqa: F401
from chars_scouts_ie1_03 import fr
from chars_scouts_ie1_09 import _c, dome

K = 'scouts-ie2:'


def _get(pid):
    return copy.deepcopy(CHARS[K + pid])


# Shona Shopbell (portera): el flequillo le tapa el ojo derecho (a la izquierda de la imagen) y el otro es un ojo grande
# de anime; antes se le veían los dos ojitos redondos
c = _get('shona-shopbell')
c['face']['eyes'] = 'normal'
c['front'][4] = fr([(12, 40), (40, 24), (64, 28), (62, 50), (56, 76), (50, 90, 1), (36, 86), (20, 76), (12, 62)])
c['front'].append(L([(50 + 14 + 6, 71), (50 + 14 + 10, 68)], OUTC, 'f', False, False, 1.8))  # pestaña del ojo que se ve
CHARS[K + 'shona-shopbell'] = c

# Junior Cage: las gafas de sol redondas negras son bastante más grandes que dos puntitos
c = _get('junior-cage')
for l in c['front']:
    if l['c'] == (24, 18, 20, 255) and not l['w']:
        cx = sum(p[0] for p in l['s']) / len(l['s'])
        l['s'] = ell(cx, 76, 8.6, 8)
for l in c['side']:
    if l['c'] == (24, 18, 20, 255) and not l['w']:
        l['s'] = ell(82, 76, 6.4, 8)
CHARS[K + 'junior-cage'] = c

# Isla Pullens y Mary Cramer: en el retrato son de complexión ancha y fuerte (hombros como los corpulentos)
for pid in ('isla-pullens', 'mary-cramer'):
    c = _get(pid)
    c['body'] = 'corpulento'
    CHARS[K + pid] = c


# Gerald Pourer: mata de rizos rojo oscuro muy abultada por arriba que baja por los lados en rizos gordos hasta debajo de
# la barbilla (por detrás de las orejas) y le tapa la nuca; antes era una boina plana con dos bloques sueltos
def _curls(cx, cy, r, n=8, a0=0.0, k2=0.84):
    import math
    pts = []
    for i in range(n * 2):
        a = a0 + math.pi * 2 * i / (n * 2)
        k = 1.0 if i % 2 == 0 else k2
        pts.append((cx + r[0] * k * math.cos(a), cy + r[1] * k * math.sin(a)))
    return blob(pts, 6)


c = _get('gerald-pourer')
c['face']['hairline'] = [(14, 66), (18, 54), (30, 50), (50, 48), (70, 50), (82, 54), (86, 66)]
c['front'] = [L(_curls(17, 80, (13, 27), 5, 0.4, 0.8)), L(_curls(83, 80, (13, 27), 5, 0.9, 0.8)),
              L(_curls(50, 28, (50, 25), 12)),
              L(_curls(74, 28, (16, 10), 4, 0.3), 'shade', 'b', False),
              L(_curls(86, 90, (6, 16), 4, 0.5), 'shade', 'b', False),
              L(_curls(50, 46, (30, 6), 6), 'mid', 'f')] + \
    [L([(24, 90), (30, 94)], OUTC, 'f', False, False, 0.9), L([(76, 90), (70, 94)], OUTC, 'f', False, False, 0.9)]
c['side'] = [L(_curls(26, 80, (20, 30), 6, 0.2)), L(_curls(46, 28, (48, 26), 10)),
             L(_curls(20, 84, (10, 20), 4, 0.6), 'shade', 'b', False),
             L(_curls(74, 46, (14, 6), 4), 'mid', 'f')]
c['back'] = [L(_curls(50, 74, (44, 32), 9, 0.2)), L(_curls(50, 30, (50, 26), 11)),
             L(_curls(70, 70, (16, 26), 5, 0.4), 'shade', 'b', False)]
CHARS[K + 'gerald-pourer'] = c

# Will Kilmon: su media melena plateada es lisa (solo un pelo de punta arriba); el contorno era de pinchos
c = _get('will-kilmon')
for v in ('front', 'side', 'back'):
    kw = dict(top=2, w=48, cy=46, n=0, amp=0, seed=161, long=94, flare=8, soft=True)
    if v == 'side':
        kw['fr'] = 52
    c[v][0:2] = dome(v, **kw)
CHARS[K + 'will-kilmon'] = c

# Terry Tortoise Pinn (portero): lleva un cuello grueso de caparazón marrón con remaches alrededor del cuello
SHELLB, SHELLBD, RIVET = _c('#5a4030'), _c('#3e2a1e'), _c('#c8b090')
c = _get('terry-tortoise-pinn')
c['front'] += [L(blob([(4, 104), (24, 112), (50, 116), (76, 112), (96, 104), (100, 120), (76, 132), (50, 134), (24, 132), (0, 120)], 6), SHELLB, 'f'),
               L(blob([(10, 118), (50, 128), (90, 118), (88, 126), (50, 132), (12, 126)], 6), SHELLBD, 'f', False)] + \
    [L(ell(x, y, 1.8, 1.8), RIVET, 'f', False) for x, y in ((16, 118), (34, 124), (50, 126), (66, 124), (84, 118))]
c['side'] += [L(blob([(14, 100), (50, 108), (84, 108), (92, 118), (80, 130), (40, 130), (10, 120)], 6), SHELLB, 'f'),
              L(ell(70, 120, 1.8, 1.8), RIVET, 'f', False), L(ell(44, 122, 1.8, 1.8), RIVET, 'f', False)]
c['back'] += [L(blob([(2, 100), (50, 108), (98, 100), (100, 118), (50, 132), (0, 118)], 6), SHELLB, 'f'),
              L(blob([(8, 114), (50, 124), (92, 114), (90, 122), (50, 130), (10, 122)], 6), SHELLBD, 'f', False)]
CHARS[K + 'terry-tortoise-pinn'] = c


# ------------------------------------------------------------------ tono de piel (revisión con el retrato)
# Piel medida en el retrato de Victory Road (mejillas y barbilla, tono iluminado más frecuente): varios dibujos tenían la
# piel rosada/pálida donde el retrato es anaranjado/tostado (o al revés). Se cambia skin (skin_d = 0,86) y las capas de
# color fijo que repetían la piel antigua. Se dejan sin tocar máscaras, cascos y caras pintadas. El tono del pelo ya
# coincidía con el retrato en todos.
from chars import hexc as _sk_hex, tone as _sk_tone  # noqa: E402


def _sk_near(a, b, tol=6):
    return isinstance(a, tuple) and len(a) >= 3 and all(isinstance(x, int) for x in a[:3]) and \
        sum(abs(a[i] - b[i]) for i in range(3)) <= tol


def _sk_reskin(key, h):
    c = copy.deepcopy(CHARS[key])
    p = c['pal']
    old, old_d = p['skin'], p['skin_d']
    p['skin'] = _sk_hex(h)
    p['skin_d'] = _sk_tone(p['skin'], 0.86)
    subs = [(old, p['skin']), (old_d, p['skin_d'])]

    def fix(v):
        for o, n in subs:
            if _sk_near(v, o):
                return n
        return v
    for view in ('front', 'side', 'back'):
        for item in c.get(view, []):
            for l in (item if isinstance(item, list) else [item]):
                if isinstance(l, dict) and 'c' in l:
                    l['c'] = fix(l['c'])
    for k, v in list(c.get('face', {}).items()):
        if isinstance(v, tuple) and len(v) == 4 and all(isinstance(x, int) for x in v):
            c['face'][k] = fix(v)
    CHARS[key] = c


_SKIN2 = {
    'thomas-worth': '#af8c73',
    'farrah-fairway': '#fbbd7b',
    'tim-personator': '#e4ccac',
    'jane-ledbelly': '#fcbc7b',
    'belle-allure': '#fcbc7b',
    'clint-peacock': '#dea257',
    'wiley-blinks': '#dda256',
    'vince-tinct': '#dea356',
    'gregg-deremer': '#fbbc78',
    'toya-boyde': '#fbbc7d',
    'farris-stickman': '#cd9467',
    'ben-whistler': '#fee7b2',
    'chad-jowell': '#f5be92',
    'heath-planner': '#af8b71',
    'isla-pullens': '#af8860',
    'jasmine-veile': '#fdce95',
    'sandra-mudd': '#f6bf93',
    'flip-sliden': '#f6be93',
    'sim-cebus': '#fabc7b',
    'elegance-stuckon': '#fbbc79',
    'ken-mayfield': '#fbbc7c',
    'luke-severin': '#b77239',
    'sam-willing': '#fdebbc',
    'wilma-morgan': '#cf9669',
    'will-ramin': '#dea257',
    'lionel-silent': '#fecf9e',
    'irving-gusher': '#fed28b',
    'bella-shaded': '#fbbc7d',
    'carl-rhodes': '#fcbc7b',
    'waylon-tripp': '#dea256',
    'egon-timing': '#fbbd7c',
    'duke-scrubine': '#cf9568',
    'gerald-pourer': '#cf9567',
    'minnie-stratio': '#fecf9f',
    'dreama-bartle': '#fbbc7a',
    'dotty-hickman': '#f7bf92',
    'phil-seebold': '#fdc370',
    'haden-safe': '#fcbc7b',
    'ian-eel-moray': '#b08c73',
    'al-stringer': '#cd925c',
    'crystal-clears': '#f7bf93',
    'shirly-quirk': '#feeab8',
    'vick-pointer': '#fdd28c',
    'doug-lapp': '#fec26f',
    'ian-fantile': '#fcbc7b',
    'lehman-rind': '#fdb959',
    'gyll-netters': '#fdc370',
    'zach-putter': '#fec370',
    'beck-hand': '#fbbc7b',
    'niki-colbeck': '#feeab7',
    'kaya-haskell': '#f5be92',
}
for _p, _h in _SKIN2.items():
    _sk_reskin('scouts-ie2:' + _p, _h)
