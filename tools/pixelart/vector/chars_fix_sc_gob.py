"""Correcciones de la revisión de diseños (grupo sc_gob): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda."""
import copy  # noqa: F401
from chars import CHARS  # noqa: F401
from heads import L, blob, ell, quad, lerp  # noqa: F401

G = 'scouts-go:'


def _c(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5)) + (255,)


def _get(pid):
    return copy.deepcopy(CHARS[G + pid])


FIXED = []  # ids corregidos (para exportar solo esos)


def _put(pid, c):
    CHARS[G + pid] = c
    if pid not in FIXED:
        FIXED.append(pid)


def _bangs(c, y0=30, y1=66, x0=12, x1=88):
    """Rellena de pelo la frente por detrás de la cara: la máscara del nacimiento del pelo ('hairline') lo recorta, así el
    flequillo baja hasta esa línea (la masa del pelo se quedaba en y 50 y la frente salía al aire)."""
    c['front'].append(L(blob([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], 2), 'mid', 'b', False))


# ------------------------------------------------------------------ flequillos rectos que no llegaban a la frente
# (el retrato lleva flequillo hasta las cejas; el dibujo dejaba la frente al aire entre y 50 y la línea del pelo)
for _pid, _hl in (('donna-hooan', 64), ('primrose-proppa', 64), ('precious-cryan', 62), ('deliah-dazzle-azel', 63),
                  ('dreama-paris', 64), ('silke-coombe', 63)):
    _ch = _get(_pid)
    _ch['face']['hairline'] = [(10, 104), (17, _hl), (50, _hl + 1), (83, _hl), (90, 104)]
    _bangs(_ch)
    _put(_pid, _ch)

# los mechones de punta del nacimiento del pelo ('hairline' con hl() o a mano) no se veían: la masa del pelo de frente
# acaba en y 50 y la frente quedaba al aire por encima de las puntas. Con el relleno, el flequillo baja como en el retrato.
for _pid in ('sheldon-trot-myrtle', 'anne-tenney', 'griz-munkie', 'breeze-flurry-windward', 'alan-mccallum', 'keigo-tsunoda',
             'ryan-tamer', 'watta-kicker', 'lynne-wildcat', 'silvio-di-fence', 'bruno-tanner', 'askel-blays', 'kit-cymbal',
             'kingley-k-black-blackcrown', 'millie-cheer', 'montana-fleetfoot', 'colin-urlane', 'taiga-west', 'don-capo',
             'leon-griffin', 'tommie-loveapple', 'indy-rockrolle', 'alex-prof-gottlieb', 'preston-digitate', 'ord-ayshus',
             'calla-de-wild', 'abby-de-valera', 'amy-sargent', 'faye-ted', 'jenral-gaim', 'charity-verchu', 'greena-grasse',
             'sly-sundice', 'freyer-monk', 'moe-tivation', 'turner-newleaf', 'mudhi-uppindown', 'everard-valiant', 'duane-jerus',
             'jack-alltrade', 'kitty-spinster', 'foley-edge', 'trixie-playfair', 'florence-orderly', 'summer-salt',
             'francie-holly', 'joe-leggit', 'evita-goe-gowell', 'frosty-patissier', 'faulk-dansa'):
    _ch = _get(_pid)
    _bangs(_ch)
    _put(_pid, _ch)

# Bonnie Sytree: la raya del nacimiento del pelo cruzaba recta por encima de los rulos de los lados
_ch = _get('bonnie-sytree')
_ch['face']['hairline'] = [(10, 104), (17, 62), (50, 62), (83, 62), (90, 104)]
_put('bonnie-sytree', _ch)


# ------------------------------------------------------------------ cambios de cada uno
from chars_scouts_ie1_09 import dome  # noqa: E402
from chars_scouts_ie1_03 import big_grin  # noqa: E402


def _tone(c, f):
    return tuple(max(0, min(255, int(v * f))) for v in c[:3]) + (255,)


def _skin(c, hexs):
    c['pal']['skin'] = _c(hexs)
    c['pal']['skin_d'] = _tone(c['pal']['skin'], 0.86)


def _recolor(c, old, new, views=('front', 'side', 'back')):
    for v in views:
        for item in c[v]:
            for l in (item if isinstance(item, list) else [item]):
                if l['c'] == old:
                    l['c'] = new


def _grin(pid, y, w, h):
    """Sonrisa ancha de dientes apretados (el retrato enseña toda la fila de dientes de mejilla a mejilla)."""
    c = _get(pid)
    c['face']['mouth'] = 'none'
    c['front'] += big_grin(y, w, h)
    _put(pid, c)


# Sly Sundice: en el retrato tiene la piel clara (melocotón), no morena
_ch = _get('sly-sundice')
_skin(_ch, '#fcd09f')
_put('sly-sundice', _ch)

# Ord Ayshus: ojos redondos pequeños de pupila negra (no ojos de anime verdes) y la boca entreabierta de labios gruesos
_ch = _get('ord-ayshus')
_ch['face'].update(eyes='round', mouth='lips', mouth_w=6, mouth_y=94)
_put('ord-ayshus', _ch)

# Ryan Tamer: ojos grandes amarillos de pupila negra (el dibujo los tenía redondos y diminutos)
_ch = _get('ryan-tamer')
_ch['face'].update(eyes='big')
_put('ryan-tamer', _ch)

# sonrisas enormes de dientes del retrato
_grin('gus-bagge', 95, 17, 9)
_grin('freyer-monk', 93, 15, 8)
_grin('pepe-bell', 93, 15, 8)
_grin('sheldon-trot-myrtle', 96, 13, 7)

# Sophie Spencer: media melena por la barbilla (el dibujo la llevaba hasta los hombros)
_ch = _get('sophie-spencer')
for _v, _k in (('front', {}), ('side', {'fr': 48}), ('back', {})):
    _ch[_v][:2] = dome(_v, top=0, w=47, cy=46, long=100, flare=3, **_k)
_put('sophie-spencer', _ch)

# Len Grayves: el sombrero es azul petróleo claro (como sus mechones), con el ala de debajo oscura; gafas naranja rojizo
_ch = _get('len-grayves')
_recolor(_ch, _c('#45545c'), _c('#6399a9'))
_recolor(_ch, _c('#38464e'), _c('#4a7684'))
_recolor(_ch, _c('#f0a080'), _c('#e2683a'))
_put('len-grayves', _ch)

# los hermanos Black-Blackley tienen todos la misma piel clara en su retrato (Uno y Quattro salían morenos)
for _pid in ('uno-1-black-blackley', 'due-2-black-blackley', 'tre-3-black-blackley', 'quattro-4-black-blackley',
             'cinque-5-black-blackley'):
    _ch = _get(_pid)
    _skin(_ch, '#fbd8b6')
    _put(_pid, _ch)

# Rain Bowe (con modelo 3D): el flequillo de la nube baja en rizos hasta las cejas (se veía una frente cuadrada) y el
# arcoíris, que va en el lado izquierdo de la cabeza, asoma por arriba de perfil y por el borde de espaldas
from chars_scouts_ie3_06 import arc  # noqa: E402
_RAIN = [_c('#e03a2a'), _c('#f0a030'), _c('#f8e050'), _c('#7ad8e8')]


def _rainbow(cx, cy, a0, a1, z='b', R=30):
    out = []
    for i, col in enumerate(_RAIN):
        r = R - i * 6
        out.append(L(arc(cx, cy, r, r * 0.9, a0, a1) + arc(cx, cy, r - 6, (r - 6) * 0.9, a1, a0), col, z, i == 0))
    return out


_ch = _get('rain-bowe')
_ch['face']['hairline'] = [(10, 104), (17, 64), (25, 56), (33, 61), (41, 55), (50, 59), (59, 55), (67, 61), (75, 56), (83, 64), (90, 104)]
_bangs(_ch)
_ch['side'] = _ch['side'] + _rainbow(58, 40, 165, 55, 'f', 28)
_ch['back'] = _rainbow(70, 40, 110, 10) + _ch['back']
_put('rain-bowe', _ch)


def _outline(pts, n=6):
    """Contorno cerrado y suave por los puntos; los que llevan un tercer valor, (x, y, 1), son puntas afiladas (como el de
    chars, copiado aquí para no importar utilidades de chars)."""
    out, k = [], len(pts)
    for i in range(k):
        p1, p2 = pts[i], pts[(i + 1) % k]
        p0 = p1 if len(p1) > 2 else pts[i - 1]
        p3 = p2 if len(p2) > 2 else pts[(i + 2) % k]
        for j in range(n):
            t = j / n
            out.append(tuple(0.5 * (2 * p1[c] + (-p0[c] + p2[c]) * t + (2 * p0[c] - 5 * p1[c] + 4 * p2[c] - p3[c]) * t * t
                                    + (-p0[c] + 3 * p1[c] - 3 * p2[c] + p3[c]) * t ** 3) for c in (0, 1)))
    return out


# Romulus Fulmen: la melena rubia cae en mechones ondulados hasta los hombros por detrás de las orejas de punta (el dibujo
# la cortaba a la altura de la barbilla)
_ch = _get('romulus-fulmen')
_ch['front'][1] = L(_outline([(16, 58), (2, 78), (12, 86), (-2, 106), (10, 108), (0, 124, 1), (18, 108), (12, 92), (22, 84), (16, 72), (22, 62)]), 'mid')
_ch['front'][2] = L(_outline([(84, 58), (98, 78), (88, 86), (102, 106), (90, 108), (100, 124, 1), (82, 108), (88, 92), (78, 84), (84, 72), (78, 62)]), 'mid')
_ch['side'][0] = L(_outline([(56, 50), (64, 34), (82, 28), (70, 10), (40, 4), (16, 14), (4, 40), (6, 70), (-6, 92), (4, 96), (-4, 120, 1), (14, 104),
                             (22, 112, 1), (26, 90), (34, 74), (30, 62), (44, 56)]))
_ch['back'][0] = L(_outline([(14, 70), (10, 30), (28, 10), (50, 4), (72, 10), (90, 30), (88, 70), (100, 96), (94, 100), (100, 124, 1), (80, 106),
                             (70, 120, 1), (60, 100), (50, 118, 1), (40, 100), (30, 120, 1), (20, 106), (0, 124, 1), (6, 100), (0, 96)]))
_put('romulus-fulmen', _ch)


# ------------------------------------------------------------------ pasada de color de la piel: tono medido en las
# mejillas y la barbilla del retrato de VR (el tono iluminado más frecuente y la media de sus vecinos; si cae junto a uno
# de los tonos fijos de los retratos, ese). Se cambia solo si se alejaba más de 30 (suma RGB) y confirmado a ojo; la
# sombra va al 0,86 y las capas de color fijo que repetían la piel antigua pasan a la nueva.


def _skin_fix(key, hexs):
    h = tuple(int(hexs[i:i + 2], 16) for i in (1, 3, 5)) + (255,)
    c = copy.deepcopy(CHARS[key])
    old, old_d = c['pal']['skin'][:3], c['pal']['skin_d'][:3]
    d = tuple(max(0, min(255, int(v * 0.86))) for v in h[:3]) + (255,)
    c['pal']['skin'], c['pal']['skin_d'] = h, d
    for v in ('front', 'side', 'back'):
        for it in c[v]:
            for l in (it if isinstance(it, list) else [it]):
                if isinstance(l['c'], tuple) and l['c'][:3] == old:
                    l['c'] = h
                elif isinstance(l['c'], tuple) and l['c'][:3] == old_d:
                    l['c'] = d
    CHARS[key] = c


for _pid, _hx in {
    'sheldon-trot-myrtle': '#e4ccac',
    'sheldon-bugg': '#fec270',
    'anne-tenney': '#feeab8',
    'romulus-fulmen': '#e4ccac',
    'primrose-proppa': '#fbd9b6',
    'sal-armando': '#89b8a8',
    'hugh-handy': '#fed08b',
    'silvio-di-fence': '#fbbc7b',
    'renardo-foxe': '#e4ccac',
    'taiga-west': '#feeab8',
    'steph-scorer': '#fbbc7b',
    'don-capo': '#fbbc7b',
    'tommie-loveapple': '#feeab8',
    'slim-pointer': '#e4ccac',
    'preston-digitate': '#fecf9e',
    'ruben-lamp': '#cd714f',
    'alex-prof-gottlieb': '#eea661',
    'lora-fayre': '#cf9669',
    'calla-de-wild': '#fdcf9f',
    'abby-de-valera': '#fed08c',
    'gord-squash': '#fbbc7b',
    'sophie-spencer': '#fef0d5',
    'buddy-muscles-arnolds': '#cf9669',
    'everard-valiant': '#fecf9e',
    'stuart-potty': '#fed18c',
    'snorri-sloth': '#fef1d4',
    'uzi-slugge': '#e4ccac',
    'will-golightly': '#feeab8',
    'bobbie-pompon': '#965435',
    'summer-salt': '#fbbc7b',
    'ken-dough': '#fef1d5',
    'patrick-childs': '#fbbc7b',
    'pepe-bell': '#fbbc7b',
}.items():
    _skin_fix('scouts-go:' + _pid, _hx)
