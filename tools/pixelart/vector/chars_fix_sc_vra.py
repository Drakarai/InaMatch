"""Correcciones de la revisión de diseños (grupo sc_vra): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda.

Ojeadores de Victory Road (scouts-vr), comparados con su retrato (y con el modelo 3D cuando lo hay):
- La piel de casi todos se ha igualado al tono plano del retrato (los retratos usan una gama fija de tonos: #fee5d3,
  #fed3bd, #fdc7a3, #c88b74, #b67355, #b66a57...). Muchos morenos estaban dibujados bastante más oscuros que en el juego.
- Después, uno a uno, lo que no coincidía: cejas, párpados caídos, ojos de color, gafas, mechones, nubes de rizos...
"""
import copy
import random

from chars import CHARS, outline, tone
from heads import L, blob, ell, quad, strand
from chars_scouts_ie1_09 import _c, mark
from chars_scouts_ie1_03 import thick_brows, side_brow, round_specs, stache  # noqa: F401

K = 'scouts-vr:'
OUTC = (60, 24, 16, 255)
WHITE = (250, 250, 250, 255)
BLACK = (24, 18, 20, 255)


def _get(pid):
    """Copia del dibujo actual con las capas de cada vista aplanadas (sin sublistas)."""
    c = copy.deepcopy(CHARS[K + pid])
    for v in ('front', 'side', 'back'):
        c[v] = [x for l in c[v] for x in (l if isinstance(l, list) else [l])]
    return c


def _set(pid, c):
    CHARS[K + pid] = c


def _col(c):
    return _c(c) if isinstance(c, str) else c


def _drop(layers, colors):
    """Quita las capas de esos colores (por la tupla RGBA)."""
    colors = [_col(c) for c in colors]
    return [l for l in layers if not (isinstance(l, dict) and l['c'] in colors)]


def _hair(c, hexcol, shade=None, deep=None, light=None):
    """Cambia el color del pelo (y sus sombras, en proporción, salvo que se den)."""
    from chars import hexc, mix
    h = hexc(hexcol)
    p = c['pal']
    p['mid'] = h
    p['shade'] = hexc(shade) if shade else tone(h, 0.78)
    p['deep'] = hexc(deep) if deep else tone(h, 0.6)
    p['light'] = hexc(light) if light else mix(h, (255, 255, 255), 0.38)


# ---------------------------------------------------------------------------------------------------------------- piel
# Tono plano de la piel en el retrato de cada ojeador (muestreado en las mejillas y la frente).
SKIN = {
    'belton-mcgirdle': '#fed3bd', 'actie-verran': '#fdc7a4', 'safine-papillonia': '#ecb299', 'ecole-linwood': '#fee5d3',
    'ah-dackchin': '#fdc6a3', 'minna-smallwood': '#fee4d2', 'ottis-quisley': '#fdc7a4', 'ayla-bordaire': '#fee5d3',
    'olivier-gourmand': '#fee2d2', 'fiona-leroux': '#fed3bc', 'trix-rosenblum': '#fee6d9', 'leander-courtman': '#fdcaaa',
    'banner-weaving': '#fecda5', 'ponny-grace': '#fdbc87', 'vivienne-starling': '#fee4d3', 'ballmer-netting': '#fee5cf',
    'proteus-flavout': '#fdc7a3', 'seph-t-forst': '#fddfb0', 'aubrey-mccoy': '#feeae1', 'blue-cleverley': '#fed3bd',
    'evon-newground': '#fee5d3', 'pinn-persica': '#fdcaaa', 'tendance-chausefutt': '#fedfb1', 'bunette-volane': '#fed8ca',
    'bellie-jerant': '#fed8c9', 'levy-vales': '#fde5cf', 'ashe-connelly': '#c98b75', 'lorenzo-dellart': '#feeedb',
    'monica-kinbird': '#feeadf', 'cassiel-longstaff': '#c88b74', 'armani-armure': '#b67355', 'jasper-chatterly': '#fde5cf',
    'berlinda-glitz': '#b67355', 'marjorette-pompom': '#fee5d3', 'batton-farrow': '#c88b75', 'tina-hopkins': '#f1a892',
    'papilla-revert': '#feccaa', 'cocoa-bounce': '#c88b74', 'bartholomew-blitzer': '#e7997b', 'dyne-amic': '#fee5d3',
    'farran-corsa': '#feeadf', 'dunk-highfield': '#fdd3bc', 'davey-lockers': '#b66a57', 'arin-fairey': '#fec6a3',
    'floyn-circuits': '#fdc7a3', 'aram-manton': '#daab99', 'fizz-kablooey': '#fed8c9', 'readon-booke': '#fed3bc',
    'terrell-brightley': '#fec29e', 'alexei-einmeister': '#fee1ce', 'santi-lite': '#e0b0a3', 'lockin-somnal': '#fed3bd',
    'eldon-compayne': '#c28c73', 'marcel-leapman': '#fecda5', 'casper-forman': '#f9caa6', 'hapleigh-mistakian': '#feebe0',
    'eshin': '#fed3bd', 'danica-wynn': '#feeadf', 'avan-floane': '#fdcaaa', 'rondo-harmond': '#fecda5',
    'barley-coldholt': '#fdcdab', 'penelope-mozartin': '#feeadf', 'harrey-tagebard': '#f1b79f', 'burley-billabong': '#c38563',
    'aldus-ogden': '#f9a979', 'bernadine-banquet': '#fed9ca', 'wheyland-schultz': '#fedfb1', 'norma-paranon': '#fed3bd',
    'aura-tempesta': '#fee5d0', 'crag-bolderin': '#b67355', 'vivi-dehues': '#fde5d3', 'barcley-dover': '#feeadf',
    'caellum-orison': '#fdcdaa', 'gusmin-strelbard': '#e09269', 'medwin-silvers': '#f1b79f', 'greef-lonbrusch': '#fed3bd',
    'sophia-goston': '#feeadf', 'choco-racketfeld': '#fee5cf', 'barrett-mistbarrow': '#c88b74', 'elmer-trommel': '#d3987b',
    'douglass-serve': '#b66a57', 'arby-trayton': '#c88b75', 'nolan-ashby': '#fecda5', 'calem-backstrom': '#b66a56',
    'zuna-yokochenko': '#fee5d0', 'leero-pard': '#fee5cf', 'beatrice-estiletto': '#fee5cf', 'rudgar-dennings': '#c88b74',
    'nicolas-pirrant': '#b77356', 'hanah-keller': '#c38563', 'manni-lamasque': '#b66a56', 'brannon-chalant': '#fedfb4',
    'carly-veneer': '#fee4d3', 'cecilia-alabaster': '#fdc7a3', 'hazel-woodrow': '#feeadf', 'wale-gambon': '#dbac9a',
    'kyle-flaggard': '#b67355', 'vincent-melodin': '#fed8c9', 'enna-flashette': '#fdccaa', 'gavin-mallory': '#fdc7a4',
    'juniper-cushionne': '#fcd9bd', 'glorian-flaunt': '#fec7a9', 'heron-champs': '#fdbd87', 'aretha-rumbell': '#c98b75',
    'phoebe-phibs-soarsky': '#f7b7a2', 'emery-hillmere': '#c18a67', 'amita-rudd': '#f9a976', 'adal-miramond': '#daab99',
    'wyatt-stockaway': '#fddfb1', 'rylan-spiker': '#fdc7a3', 'davis-tarvish': '#d38657', 'trip-cresta': '#c88b74',
    'benoni-espinoza': '#b67355', 'altair-aldrin': '#fee5cf', 'bracker-grippe': '#e2b4a2', 'selina-goldpyre': '#feeadf',
    'nova-holloway': '#fde5d3', 'lace-tangler': '#fee5d3', 'rockson-grohl': '#fdccab', 'link-whitstone': '#fdccaa',
    'lacie-pawford': '#fed9c9', 'hedrick-wilspin': '#e0936d', 'colter-fairburn': '#fed3bd', 'cane-fangley': '#c98b75',
    'landric-delphin': '#b76a57', 'ferron-rockfort': '#b66a57', 'flash-lighton': '#b66a57', 'wagner-waltz': '#bb9185',
    'jewelyn-plunkett': '#fed8c9', 'calix-virtus': '#fedfb1', 'heathcliff-humbold': '#b66a57', 'mako-carcher': '#feeae0',
    'lita-vault': '#fed3bd', 'alanna-ordelyne': '#feeadf', 'akela-portner': '#fed3bd', 'octavia-carroll': '#feebe0',
    'eviden-tracer': '#fee0b5', 'hazlo-prophyle': '#c88b75', 'graye-earlnest': '#fde5d0', 'draven-savager': '#c88b75',
    'brooke-reedman': '#fdc9ab', 'veronica-camry': '#fee5cf', 'bechet-ardevout': '#fdc7a3', 'iro-armussel': '#daac99',
    'neve-paisley': '#feeadf', 'flaurine-woodwind': '#fee5d3', 'figgo-balpark': '#fdccab', 'uriah-goldfield': '#fed3bd',
    'culinaro-brons': '#b67355', 'coby-cogsworth': '#fed2bc',
    # muestreados a mano (el automático cogía el pelo o la ropa)
    'fouad-togenick': '#fed2ad', 'harolde-narcissus': '#fee5d3', 'eilidh-innes': '#feeadf', 'cosette-lyricotte': '#fecdab',
}


def _skin_all():
    for pid, h in SKIN.items():
        c = CHARS.get(K + pid)
        if not c:
            continue
        old = c['pal']['skin']
        c['pal']['skin'] = _c(h)
        c['pal']['skin_d'] = tone(_c(h), 0.86)
        # la nariz o las capas que usaban el tono de piel viejo como color fijo pasan al nuevo
        for view in ('front', 'side', 'back'):
            for l in c[view]:
                for x in (l if isinstance(l, list) else [l]):
                    if isinstance(x, dict) and x['c'] == old:
                        x['c'] = 'skin'


_skin_all()


# --------------------------------------------------------------------------------------------------------- ayudas
def lids(ey=75, sep=14, c='skin', drop=4.5, w=2.6, side=False):
    """Párpados caídos (ojos entornados): tapa la parte de arriba del ojo con piel y pone la raya del párpado."""
    out = []
    if side:
        out.append(L(blob([(75, ey - 10), (88, ey - 10), (88, ey - 7 + drop), (75, ey - 7 + drop)], 3), c, 'f', False))
        out.append(L(quad((75.5, ey - 6 + drop), (81, ey - 8 + drop), (87, ey - 6 + drop)), OUTC, 'f', False, False, w))
        return out
    for cx in (50 - sep, 50 + sep):
        out.append(L(blob([(cx - 7.5, ey - 10), (cx + 7.5, ey - 10), (cx + 7.5, ey - 7 + drop), (cx - 7.5, ey - 7 + drop)], 3), c, 'f', False))
        out.append(L(quad((cx - 6.8, ey - 6 + drop), (cx, ey - 8.4 + drop), (cx + 6.8, ey - 6 + drop)), OUTC, 'f', False, False, w))
    return out


def happy_eyes(ey=75, sep=14, c=OUTC, w=2.4):
    """Ojos cerrados de felicidad (^ ^)."""
    return [L(quad((cx - 6, ey + 2), (cx, ey - 4), (cx + 6, ey + 2)), c, 'f', False, False, w) for cx in (50 - sep, 50 + sep)]


def arc_brows(y=63, c=OUTC, w=1.8, sep=14, half=7, lift=3):
    return [L(quad((cx - half, y + 1), (cx, y - lift), (cx + half, y + 1)), c, 'f', False, False, w) for cx in (50 - sep, 50 + sep)]


def bumpy(cx, cy, rx, ry, n=12, amp=0.12, seed=1, a0=0.0, a1=360.0, extra=()):
    """Contorno de nube de rizos: un óvalo de n bultos redondos (de a0 a a1 grados, 0 = derecha, en sentido antihorario);
    extra son los puntos con los que se cierra cuando no es la vuelta entera."""
    import math
    rnd = random.Random(seed)
    sizes = [rnd.uniform(0.7, 1.0) for _ in range(n)]
    pts = []
    k = 8
    for i in range(n):
        for j in range(k):
            u = j / k
            a = math.radians(a0 + (a1 - a0) * (i + u) / n)
            f = 1 + amp * sizes[i] * math.sin(math.pi * u) ** 0.6 - amp * 0.3
            pts.append((cx + rx * f * math.cos(a), cy - ry * f * math.sin(a)))
    if a1 - a0 < 360:
        a = math.radians(a1)
        pts.append((cx + rx * (1 - amp * 0.3) * math.cos(a), cy - ry * (1 - amp * 0.3) * math.sin(a)))
    return pts + list(extra)


def bow2(x, y, c, s=1.0, z='f'):
    """Lazo pequeño de dos lóbulos y nudo."""
    c = _col(c)
    return [L(blob([(x, y), (x - 8 * s, y - 5 * s), (x - 9 * s, y + 4 * s)], 4), c, z), L(blob([(x, y), (x + 8 * s, y - 5 * s), (x + 9 * s, y + 4 * s)], 4), c, z),
            L(ell(x, y, 2.2 * s, 2.2 * s), c, z)]


# ======================================================================================================= jugadores

# Safine Papillonia: melena castaña larga y ondulada con muchos mechones RUBIOS mezclados (no dos bloques rubios abajo);
# piel tostada clara y sonrisa abierta
def _safine():
    c = _get('safine-papillonia')
    OLD, BLD = _c('#f0d8a8'), _c('#e8cc98')
    for v in ('front', 'side', 'back'):
        c[v] = [l for l in c[v] if l['c'] != OLD]
    c['front'] += [L(outline([(12, 56), (6, 80), (10, 104), (4, 118, 1), (16, 104), (14, 80), (18, 60)]), BLD, 'f', False),
                   L(outline([(84, 60), (90, 82), (88, 104), (96, 120, 1), (96, 100), (94, 78), (88, 56)]), BLD, 'f', False),
                   L(outline([(52, 40), (60, 50), (70, 62), (78, 80, 1), (68, 66), (58, 54)]), BLD, 'f', False),
                   L(outline([(-2, 92), (2, 106), (-4, 118, 1), (6, 108), (4, 94)]), BLD, 'b', False),
                   L(outline([(102, 92), (98, 106), (104, 118, 1), (94, 108), (96, 94)]), BLD, 'b', False)]
    c['side'] += [L(outline([(10, 60), (2, 84), (8, 108), (0, 122, 1), (14, 108), (12, 84), (18, 62)]), BLD, 'f', False),
                  L(outline([(30, 66), (26, 90), (32, 112, 1), (34, 90), (36, 70)]), BLD, 'f', False)]
    c['back'] += [L(outline([(x, 56), (x - 6, 84), (x - 2, 106), (x - 8, 118, 1), (x + 4, 106), (x + 2, 84), (x + 6, 58)]), BLD, 'f', False) for x in (14, 40, 66, 90)]
    c['face']['mouth'] = 'smile'
    _set('safine-papillonia', c)


_safine()


# Ah Dackchin: piel clara; gafas de aviador grandes de cristal rojizo con montura dorada, cejas oscuras, barba fina por
# el borde de la mandíbula (de patilla a patilla) y bigotillo de puntos
def _ah():
    c = _get('ah-dackchin')
    LENS, GOLD = _c('#c8603a'), _c('#c8a050')
    c['front'] = [l for l in c['front'] if l['c'] != LENS and not (len(l['s']) < 20 and l['c'] == 'mid')]
    c['front'] = [l for l in c['front'] if not (l['c'] == BLACK and l['w'])]
    c['front'] += arc_brows(64, _c('#2a2a3a'), 2.6, 15, 8, 2)
    c['front'] += [L(blob([(23, 71), (46, 71), (45, 80), (37, 84), (27, 82)], 5), LENS, 'f', True),
                   L(blob([(77, 71), (54, 71), (55, 80), (63, 84), (73, 82)], 5), LENS, 'f', True),
                   L([(45, 72), (55, 72)], GOLD, 'f', False, False, 1.6), L([(23, 71), (46, 71)], GOLD, 'f', False, False, 1.4),
                   L([(54, 71), (77, 71)], GOLD, 'f', False, False, 1.4)]
    c['front'] += [L(quad((22, 82), (27, 95), (50, 96)) + quad((50, 96), (73, 95), (78, 82))[1:], _c('#3a3030'), 'f', False, False, 3.0)]
    c['front'] += [L(ell(x, y, 0.7, 0.7), _c('#6a4a3a'), 'f', False) for x, y in ((41, 91.5), (44.5, 90.5), (47.5, 91.5), (52.5, 91.5), (55.5, 90.5), (59, 91.5))]
    c['side'] = [l for l in c['side'] if l['c'] != LENS]
    c['side'] += [L(blob([(74, 71), (88, 71), (87, 80), (77, 83)], 5), LENS, 'f', True), L([(74, 72), (48, 68)], GOLD, 'f', False, False, 1.4),
                  L(quad((52, 84), (60, 100), (80, 102)), _c('#2a2222'), 'f', False, False, 2.2)] + side_brow(64, _c('#2a2a3a'), 2.4)
    _set('ah-dackchin', c)


_ah()


# Banner Weaving: abuelo de ojos ENTORNADOS (no cerrados) gris azulado, con cejas grises gruesas en arco, pecas
def _banner():
    c = _get('banner-weaving')
    c['face'].update(eyes='normal', brows=False, eye_y=77)
    c['pal']['iris'] = _c('#5a6a7a')
    c['front'] += lids(77, drop=5.5) + arc_brows(63, 'mid', 3.6, 15, 8, 5)
    c['front'] += [L(ell(x, y, 0.8, 0.8), _c('#c08a60'), 'f', False) for x, y in ((28, 88), (31, 90), (34, 88), (72, 88), (69, 90), (66, 88))]
    c['side'] += lids(77, drop=5.5, side=True) + side_brow(63, 'mid', 4.0)
    c['face']['mouth'] = 'smile'
    _set('banner-weaving', c)


_banner()


# Hop Sadler: una nube grande y redonda de rizos gris lila (no un gorro plano), con mechones rizados azul marino que le
# caen por la cara; ojos morados entornados
def _hop():
    c = _get('hop-sadler')
    DK = (34, 32, 52, 255)
    from chars import rope
    c['front'] = [L(bumpy(50, 28, 56, 38, 14, 0.1, 5, -30, 210, [(84, 66), (78, 50), (22, 50), (16, 66)]), 'mid', 'b'),
                  L(blob([(60, -6), (98, 14), (104, 46), (86, 56)], 6), 'shade', 'b', False),
                  L(rope((44, 8), (24, 34), (34, 70), 4.4), DK, 'f'), L(rope((54, 6), (72, 34), (62, 66), 4), DK, 'f'),
                  L(rope((36, 14), (16, 40), (18, 76), 4), DK, 'f'), L(rope((64, 12), (86, 40), (82, 74), 4), DK, 'f'),
                  L(rope((48, 10), (46, 40), (50, 56), 3.4), DK, 'f')] + lids(75, drop=3.5)
    c['side'] = [L(bumpy(44, 28, 56, 38, 14, 0.1, 6, -40, 250, [(56, 64), (60, 50)]), 'mid', 'b'),
                 L(rope((60, 10), (80, 36), (76, 62), 4), DK, 'f'), L(rope((30, 20), (14, 50), (22, 86), 4.4), DK, 'f'),
                 L(rope((44, 24), (36, 56), (42, 84), 4), DK, 'f')] + lids(75, drop=3.5, side=True)
    c['back'] = [L(bumpy(50, 30, 56, 40, 14, 0.1, 7), 'mid', 'b')] + \
        [L(rope((x, 30), (x - 6, 62), (x + 2, 88), 4.2), DK, 'f') for x in (22, 40, 60, 78)]
    _set('hop-sadler', c)


_hop()


# Pinn Persica: el tupé rosa es una masa de RIZOS abultados que cae hacia la derecha (no liso); ojos entornados
def _pinn():
    c = _get('pinn-persica')
    PINKD = _c('#c86a98')
    c['front'][1] = L(outline([(14, 34), (12, 16), (20, 0), (34, -10), (50, -12), (66, -8), (80, 2), (88, 16), (86, 30), (82, 42), (78, 54), (70, 64),
                               (62, 60), (60, 48), (50, 42), (38, 40), (24, 44)], 3), 'mid', 'f')
    c['front'][2] = L(outline([(56, -6), (76, 4), (82, 26), (74, 48), (66, 30)], 4), 'shade', 'f', False)
    c['front'] += [L(ell(x, y, r, r * 0.9), 'mid', 'f') for x, y, r in ((22, 4, 9), (36, -6, 9), (52, -8, 9), (68, -2, 9), (80, 12, 8), (84, 30, 7), (78, 46, 7),
                                                                       (70, 58, 6), (16, 22, 7), (26, 38, 6), (44, 36, 7))]
    c['front'] += [L(quad((x - 4, y + 2), (x, y - 3), (x + 4, y + 2)), PINKD, 'f', False, False, 1.4) for x, y in ((36, -2), (54, -4), (70, 4), (80, 22), (26, 10), (74, 44))]
    c['front'] += lids(75, drop=3.8)
    c['side'][1] = L(outline([(20, 20), (30, -2), (46, -12), (66, -12), (84, -2), (94, 14), (92, 34), (82, 48), (70, 42), (60, 30), (36, 30)], 3), 'mid', 'f')
    c['side'] += [L(ell(x, y, r, r * 0.9), 'mid', 'f') for x, y, r in ((34, -2, 9), (52, -10, 9), (70, -8, 9), (86, 6, 8), (90, 28, 7), (78, 44, 6))]
    c['side'] += lids(75, drop=3.8, side=True)
    c['back'][1] = L(outline([(16, 30), (18, 6), (34, -8), (50, -12), (66, -8), (82, 6), (84, 30), (50, 40)], 3), 'mid', 'f')
    c['back'] += [L(ell(x, y, r, r * 0.9), 'mid', 'f') for x, y, r in ((24, 10, 8), (38, -4, 9), (56, -6, 9), (72, 4, 8), (80, 22, 7))]
    _set('pinn-persica', c)


_pinn()


# Cassiel Longstaff: nube de rizos gris claro más abultada y desigual, que baja por los lados hasta las sienes
def _cassiel():
    c = _get('cassiel-longstaff')
    c['front'][1] = L(bumpy(50, 14, 50, 30, 14, 0.12, 11, -20, 200, [(80, 38), (50, 34), (20, 38)]), 'mid', 'b')
    c['side'][1] = L(bumpy(46, 14, 48, 30, 14, 0.12, 12, -20, 200, [(64, 36), (20, 38)]), 'mid', 'b')
    c['back'][1] = L(bumpy(50, 16, 50, 32, 14, 0.12, 13), 'mid', 'b')
    _set('cassiel-longstaff', c)


_cassiel()


# Ecole Linwood: ojos cerrados de felicidad (^ ^), no dormidos; rubor más grande
def _ecole():
    c = _get('ecole-linwood')
    c['face'].update(eyes='none')
    c['front'] += happy_eyes(76) + arc_brows(64, OUTC, 1.6, 14, 6, 2)
    _set('ecole-linwood', c)


_ecole()


# Sienna Fairborn: las coletas se atan con LAZOS negros (no bolitas)
def _sienna():
    c = _get('sienna-fairborn')
    for v in ('front', 'side', 'back'):
        c[v] = _drop(c[v], [BLACK])
    c['front'] += bow2(10, 36, BLACK, 1.5) + bow2(90, 36, BLACK, 1.5)
    c['side'] += bow2(38, 28, BLACK, 1.5)
    c['back'] += bow2(14, 36, BLACK, 1.5) + bow2(86, 36, BLACK, 1.5)
    _set('sienna-fairborn', c)


_sienna()


# Minna Smallwood: los mechones que enmarcan la cara (por delante de las orejas) son ROSA claro
def _minna():
    c = _get('minna-smallwood')
    PNK = _c('#f0a8d8')
    c['front'] += [L(outline([(14, 48), (24, 50), (26, 70), (24, 90), (19, 100, 1), (13, 80)]), PNK, 'f'),
                   L(outline([(86, 48), (76, 50), (74, 70), (76, 90), (81, 100, 1), (87, 80)]), PNK, 'f')]
    c['side'] += [L(outline([(58, 50), (66, 54), (66, 76), (62, 98, 1), (57, 76)]), PNK, 'f')]
    c['back'] += [L(outline([(8, 60), (14, 62), (14, 84), (10, 92, 1), (6, 80)]), PNK, 'f'), L(outline([(92, 60), (86, 62), (86, 84), (90, 92, 1), (94, 80)]), PNK, 'f')]
    _set('minna-smallwood', c)


_minna()


# Ottis Quisley: naricilla marrón y cejas finas
def _ottis():
    c = _get('ottis-quisley')
    c['face']['nose'] = (50, 84, 2.2)
    c['pal']['nose'] = _c('#c88a6a')
    _set('ottis-quisley', c)


_ottis()


# Belton McGirdle: un mechón castaño oscuro le cruza la frente en curva; sonrisa ladeada
def _belton():
    c = _get('belton-mcgirdle')
    c['front'] += [L(outline([(78, 28), (64, 30), (50, 40), (40, 52), (36, 62, 1), (48, 50), (62, 42), (76, 40)]), _c('#7a4a2a'), 'f')]
    c['side'] += [L(outline([(86, 30), (76, 34), (82, 52, 1), (88, 40)]), _c('#7a4a2a'), 'f')]
    _set('belton-mcgirdle', c)


_belton()


# Olivier Gourmand: ojeras bajo los ojos
def _olivier():
    c = _get('olivier-gourmand')
    c['front'] += [L(quad((cx - 6, 84), (cx, 86.5), (cx + 6, 84)), _c('#c8a090'), 'f', False, False, 1.2) for cx in (36, 64)]
    _set('olivier-gourmand', c)


_olivier()


# Trix Rosenblum: un flequillo ondulado le cruza la frente de un lado a otro
def _trix():
    c = _get('trix-rosenblum')
    c['front'] += [L(outline([(14, 50), (24, 34), (44, 28), (66, 32), (80, 44), (70, 46), (60, 54), (52, 60, 1), (46, 52), (34, 50), (24, 58, 1)]), 'mid', 'f')]
    c['side'] += [L(outline([(60, 34), (80, 40), (88, 54, 1), (74, 50)]), 'mid', 'f')]
    _set('trix-rosenblum', c)


_trix()


# Leander Courtman: cejas gruesas castañas levantadas (sonríe, no está enfadado)
def _leander():
    c = _get('leander-courtman')
    c['face']['brows'] = False
    c['front'] += thick_brows(63, _c('#6a3a1a'), 4.4, 15, 0.4, 15)
    c['side'] += side_brow(63, _c('#6a3a1a'), 4.4)
    _set('leander-courtman', c)


_leander()


# Vivienne Starling: mirada dulce entornada y cejas finas suaves (no ojos afilados)
def _vivienne():
    c = _get('vivienne-starling')
    c['face'].update(eyes='normal')
    c['front'] += lids(75, drop=3.2) + arc_brows(63, OUTC, 1.4, 14, 6, 1.5)
    c['side'] += lids(75, drop=3.2, side=True)
    _set('vivienne-starling', c)


_vivienne()


# Blue Cleverley: ojos redondos de pupila pequeña y cejas castañas gruesas (no ojos grandes azules)
def _blue():
    c = _get('blue-cleverley')
    c['face'].update(eyes='round', brows=False)
    c['front'] += thick_brows(64, _c('#6a4a2a'), 4.0, 15, 0, 14)
    c['side'] += side_brow(64, _c('#6a4a2a'), 4.0)
    _set('blue-cleverley', c)


_blue()


# Hexine Cantation: boquita abierta de sorpresa (no dientes)
def _hexine():
    c = _get('hexine-cantation')
    c['face']['mouth'] = 'none'
    c['front'] += [L(ell(50, 94, 2.6, 2.2), _c('#8a3a3a'), 'f', True, True)]
    _set('hexine-cantation', c)


_hexine()


# Levy Vales: ojos de espiral (anillos grises), no círculos blancos vacíos
def _levy():
    c = _get('levy-vales')
    c['front'] = [l for l in c['front'] if not (isinstance(l['c'], tuple) and min(l['c'][:3]) > 240)]
    for cx in (36, 64):
        c['front'] += [L(ell(cx, 80, 5, 5), (236, 236, 228, 255), 'f', True, True)]
        c['front'] += [L(ell(cx, 80, r, r) + [ell(cx, 80, r, r)[0]], _c('#6a7a6a'), 'f', False, False, 0.9) for r in (3.6, 2.2)]
        c['front'] += [L(ell(cx, 80, 0.9, 0.9), BLACK, 'f', False)]
    c['face']['mouth'] = 'frown'
    _set('levy-vales', c)


_levy()


# Jasper Chatterly: montura de las gafas gris plateado (no celeste)
def _jasper():
    c = _get('jasper-chatterly')
    SILV, OLD = _c('#9a9aa6'), _c('#8acad8')
    for v in ('front', 'side'):
        for l in c[v]:
            if l['c'] == OLD:
                l['c'] = SILV
    _set('jasper-chatterly', c)


_jasper()


# Batton Farrow: ojos entornados (abiertos, con párpado caído), no cerrados
def _batton():
    c = _get('batton-farrow')
    c['face'].update(eyes='normal', eye_y=76)
    c['pal']['iris'] = _c('#3a3a3a')
    c['front'] += lids(76, drop=5)
    c['side'] += lids(76, drop=5, side=True)
    _set('batton-farrow', c)


_batton()


# Tina Hopkins: abuela de cejas blancas gruesas
def _tina():
    c = _get('tina-hopkins')
    c['face']['brows'] = False
    c['front'] += thick_brows(63, (248, 244, 236, 255), 4.4, 15, 0.4, 15)
    c['side'] += side_brow(63, (248, 244, 236, 255), 4.4)
    _set('tina-hopkins', c)


_tina()


# Bartholomew Blitzer: gafas pequeñas redondas de montura roja oscura
def _bart():
    c = _get('bartholomew-blitzer')
    c['front'] += round_specs('front', _c('#a83a3a'), 76, 15, 7.5, 6.5, 1.6)
    c['side'] += round_specs('side', _c('#a83a3a'), 76, 15, 7.5, 6.5, 1.6)
    _set('bartholomew-blitzer', c)


_bart()


# Floyn Circuits: el tupé tiene un remolino oscuro marcado


# Fouad Togenick: el pelo es un cepillo PLANO, ancho y bajo (no una torre), con un rizo en espiral sobre la frente
def _fouad():
    c = _get('fouad-togenick')
    top = [(8, 62), (4, 40), (0, 22), (8, 14), (50, 10), (92, 14), (100, 22), (96, 40), (92, 62), (82, 50), (18, 50)]
    c['front'] = [L(outline(top)), L(outline([(62, 12), (92, 14), (100, 22), (94, 44), (86, 52), (80, 32)]), 'shade', 'b', False),
                  L(blob([(12, 17), (50, 13), (88, 17), (50, 22)], 4), 'light', 'b', False),
                  L(outline([(38, 48), (50, 38), (62, 46), (60, 60), (50, 64), (42, 58), (50, 52), (54, 56)]), 'mid', 'f', False, True)]
    c['front'] += thick_brows(66, 'shade', 4.0, 15, 0, 14)
    c['side'] = [L(outline([(54, 58), (60, 46), (84, 46), (96, 24), (90, 14), (50, 10), (12, 14), (2, 26), (6, 48), (28, 62)])),
                 L(blob([(14, 17), (50, 13), (86, 17), (50, 22)], 4), 'light', 'b', False)] + side_brow(66, 'shade', 4.0)
    c['back'] = [L(outline([(8, 76), (4, 40), (0, 22), (8, 14), (50, 10), (92, 14), (100, 22), (96, 40), (92, 76), (50, 82)]))]
    _set('fouad-togenick', c)


_fouad()


# Lockin Somnal: la masa azul claro es grande y le cae sobre la frente hasta los ojos, dentro de la nube negra
def _lockin():
    c = _get('lockin-somnal')
    TOP = c['pal']['top']
    c['front'] = [l for l in c['front'] if l['c'] != 'top'] + [
        L(outline([(10, 44), (14, 20), (30, 4), (50, 0), (72, 4), (88, 18), (92, 42), (84, 58), (74, 52), (62, 62), (50, 56), (38, 62), (26, 54), (16, 60)]), 'top', 'f'),
        L(outline([(56, 6), (80, 14), (88, 34), (80, 50), (70, 30)]), tone(TOP, 0.85), 'f', False)]
    c['side'] = [l for l in c['side'] if l['c'] != 'top'] + [
        L(outline([(22, 34), (34, 8), (60, 0), (84, 12), (94, 34), (86, 58), (74, 50), (60, 44), (40, 42)]), 'top', 'f')]
    c['face']['brows'] = True
    _set('lockin-somnal', c)


_lockin()


# Marcel Leapman: ojos grises; Casper Forman: pelo coral; Greef Lonbrusch: naranja rojizo; Vivi Dehues: azul acero;
# Link Whitstone: azul marino (y el mechón claro más apagado); Hedrick Wilspin: gorro azul violeta apagado; Draven
# Savager: morado más oscuro
def _colors():
    c = _get('marcel-leapman')
    c['pal']['iris'] = _c('#6a6a70')
    _set('marcel-leapman', c)
    c = _get('casper-forman')
    _hair(c, '#ee6450')
    _set('casper-forman', c)
    c = _get('greef-lonbrusch')
    _hair(c, '#e47a4c')
    _set('greef-lonbrusch', c)
    c = _get('vivi-dehues')
    _hair(c, '#3a72aa', shade='#2a5280', deep='#1e3a5e')
    _set('vivi-dehues', c)
    c = _get('link-whitstone')
    old = c['pal']['mid']
    _hair(c, '#34416f')
    for v in ('front', 'side', 'back'):
        for l in c[v]:
            if isinstance(l['c'], tuple) and l['c'][2] > 150 and l['c'] != old:
                l['c'] = _c('#5a6a98')
    _set('link-whitstone', c)
    c = _get('draven-savager')
    _hair(c, '#40387a')
    _set('draven-savager', c)


_colors()


def _hedrick():
    c = _get('hedrick-wilspin')
    for v in ('front', 'side', 'back'):
        for l in c[v]:
            col = l['c']
            if isinstance(col, tuple) and col[2] > 150 and col[0] < 120:
                l['c'] = _c('#4c4b93') if col[2] > 170 else _c('#3a3a7e')
    _set('hedrick-wilspin', c)


_hedrick()


# Rondo Harmond: ojos entornados abiertos (no cerrados)
def _rondo():
    c = _get('rondo-harmond')
    c['front'] = [l for l in c['front'] if l['c'] != OUTC]
    c['side'] = [l for l in c['side'] if not (l['c'] == OUTC and l['w'])]
    c['face'].update(eyes='normal', eye_y=78)
    c['pal']['iris'] = _c('#8a8a40')
    c['front'] += lids(78, drop=6)
    c['side'] += lids(78, drop=6, side=True)
    _set('rondo-harmond', c)


_rondo()


# Penelope Mozartin: media melena naranja de ondas horizontales con la coronilla redonda (no en punta)
def _penelope():
    c = _get('penelope-mozartin')
    c['front'] = [L(outline([(8, 98), (2, 70), (4, 36), (18, 12), (50, 4), (82, 12), (96, 36), (98, 70), (92, 98), (82, 96), (82, 64), (18, 64), (18, 96)])),
                  L(outline([(60, 8), (84, 16), (96, 40), (96, 74), (88, 94), (84, 60)]), 'shade', 'b', False),
                  L(outline([(16, 64), (14, 42), (26, 26), (50, 22), (74, 26), (86, 42), (84, 64), (70, 56), (50, 58), (30, 56)]), 'mid', 'f')] + \
        [l for l in c['front'] if l['w'] or l['c'] not in ('mid', 'shade')]
    c['front'] += [L(quad((20, y), (50, y - 6), (80, y)), 'shade', 'f', False, False, 1.4) for y in (36, 48)]
    c['face']['hairline'] = [(8, 64), (30, 56), (50, 58), (70, 56), (92, 64)]
    _set('penelope-mozartin', c)


_penelope()


# Selena Sopralis: el azul está en las PUNTAS del flequillo y de los mechones (no rayas sueltas)
def _selena():
    c = _get('selena-sopralis')
    for v in ('front', 'side', 'back'):
        c[v] = [l for l in c[v] if not (l['c'] == _c('#2a8ac8') and l['w'])]
    BLU = _c('#2a8ad0')
    c['front'] += [L([(x - 2.2, 59), (x + 2.2, 59), (x + 1.4, 66), (x, 67.5), (x - 1.4, 66)], BLU, 'f', False) for x in (22, 34, 66, 78)]
    c['front'] += [L(outline([(6, 96), (16, 96), (14, 112, 1), (4, 110)]), BLU, 'f', False), L(outline([(94, 96), (84, 96), (86, 112, 1), (96, 110)]), BLU, 'f', False)]
    c['side'] += [L(outline([(4, 100), (14, 100), (12, 112, 1), (2, 110)]), BLU, 'f', False), L(outline([(28, 100), (38, 100), (36, 112, 1), (28, 110)]), BLU, 'f', False)]
    c['back'] += [L(outline([(x - 5, 100), (x + 5, 100), (x + 3, 112, 1), (x - 4, 110)]), BLU, 'f', False) for x in (8, 30, 50, 70, 92)]
    _set('selena-sopralis', c)


_selena()


# Aura Tempesta: cejas finas normales y boca seria pequeña (no enfadada)
def _aura():
    c = _get('aura-tempesta')
    c['face'].update(brows=True, mouth='line')
    _set('aura-tempesta', c)


_aura()


# Barcley Dover y Arby Trayton: ojos de iris de color (naranja / verde agua), no puntos negros
def _iris():
    for pid in ('barcley-dover', 'arby-trayton'):
        c = _get(pid)
        c['face']['eyes'] = 'normal'
        _set(pid, c)
    c = _get('arby-trayton')
    c['face']['brows'] = False
    c['front'] += arc_brows(64, (240, 236, 224, 255), 2.0, 14, 6, 1.5)
    _set('arby-trayton', c)
    # Cecilia Alabaster: ojos verde agua y la melena de rizos grandes que se abulta a los lados de la cara
    c = _get('cecilia-alabaster')
    c['pal']['iris'] = _c('#3aa89a')
    c['front'] = [L(bumpy(8, 82, 14, 20, 5, 0.16, 1), 'mid', 'b'), L(bumpy(92, 82, 14, 20, 5, 0.16, 2), 'mid', 'b')] + c['front']
    c['front'] += [L(quad((x - 5, y), (x, y - 5), (x + 5, y)), 'shade', 'f', False, False, 1.4) for x, y in ((6, 76), (10, 90), (94, 76), (90, 90))]
    c['back'] = [L(bumpy(6, 82, 14, 20, 5, 0.16, 3), 'mid', 'b'), L(bumpy(94, 82, 14, 20, 5, 0.16, 4), 'mid', 'b')] + c['back']
    _set('cecilia-alabaster', c)
    c = _get('calix-virtus')
    c['pal']['iris'] = _c('#a04a8a')
    c['front'] += [L(quad((cx - 7, 70), (cx, 66), (cx + 7, 70)), _c('#9a6ab8'), 'f', False, False, 1.6) for cx in (36, 64)]
    _set('calix-virtus', c)


_iris()


# Barrett Mistbarrow: pelo negro peinado pegado a la cabeza (no una cúpula enorme), con la melena por detrás
def _barrett():
    c = _get('barrett-mistbarrow')
    from chars_scouts_ie1_09 import dome
    c['front'] = dome('front', top=16, w=44, cy=50, long=100, flare=0, seed=30) + [l for l in c['front'] if l['w']]
    c['side'] = dome('side', top=16, w=44, cy=50, long=100, flare=0, fr=50, seed=30) + [l for l in c['side'] if l['w']]
    c['back'] = dome('back', top=16, w=44, cy=50, long=100, flare=0, seed=30)
    c['front'] += [strand([(30, 26), (50, 18), (70, 26)], 'shade', 'f', 1.2), strand([(26, 36), (50, 28), (74, 36)], 'shade', 'f', 1.2)]
    _set('barrett-mistbarrow', c)


_barrett()


# Zuna Yokochenko: cejas cortas y gruesas (de punto), no finas
def _zuna():
    c = _get('zuna-yokochenko')
    c['face']['brows'] = False
    c['front'] += [L(blob([(cx - 4, 64), (cx + 4, 63), (cx + 3, 67), (cx - 3, 67)], 3), 'deep', 'f', False) for cx in (37, 63)]
    _set('zuna-yokochenko', c)


_zuna()


# Beatrice Estiletto: mirada dulce de ojos castaño anaranjado con pestañas y cejas suaves, sonrisa (no ojos rojos afilados)
def _beatrice():
    c = _get('beatrice-estiletto')
    c['face'].update(eyes='normal', brows=False, mouth='smile')
    c['pal']['iris'] = _c('#b8704a')
    c['front'] += lids(75, drop=2.6) + arc_brows(63, OUTC, 1.4, 14, 6, 1.5)
    c['side'] += lids(75, drop=2.6, side=True)
    _set('beatrice-estiletto', c)


_beatrice()


# Nicolas Pirrant, Wyatt Stockaway y Uriah Goldfield: ojos como en el retrato
def _eyes():
    c = _get('nicolas-pirrant')
    c['face']['eyes'] = 'normal'
    c['pal']['iris'] = _c('#5a6a7a')
    _set('nicolas-pirrant', c)
    for pid in ('wyatt-stockaway', 'uriah-goldfield'):
        c = _get(pid)
        c['face']['eyes'] = 'round'
        _set(pid, c)


_eyes()


# Hanah Keller: el pelo pasa de rojo anaranjado arriba a carmesí oscuro por los lados y abajo
def _hanah():
    c = _get('hanah-keller')
    CR = _c('#9a2030')
    c['front'] += [L(outline([(6, 60), (16, 58), (20, 76), (16, 96, 1), (8, 84)]), CR, 'f'), L(outline([(94, 60), (84, 58), (80, 76), (84, 96, 1), (92, 84)]), CR, 'f')]
    c['side'] += [L(outline([(6, 56), (40, 60), (52, 70), (40, 92, 1), (14, 88)]), CR, 'f')]
    c['back'] += [L(outline([(4, 56), (96, 56), (96, 84), (50, 92), (4, 84)]), CR, 'f')]
    _set('hanah-keller', c)


_hanah()


# Gavin Mallory: dos pelos de antena encima
def _gavin():
    c = _get('gavin-mallory')
    for v in ('front', 'back'):
        c[v] += [L(quad((48, 4), (42, -10), (36, -8)), 'mid', 'b', False, False, 2.4), L(quad((52, 4), (56, -12), (64, -10)), 'mid', 'b', False, False, 2.4)]
    c['side'] += [L(quad((46, 4), (44, -12), (36, -10)), 'mid', 'b', False, False, 2.4)]
    _set('gavin-mallory', c)


_gavin()


# Aretha Rumbell: piel morena; melena roja ONDULADA en bob (no de pinchos), mechones por la frente; mirada seria
def _aretha():
    c = _get('aretha-rumbell')
    from chars_scouts_ie1_09 import dome
    c['front'] = dome('front', top=0, w=50, cy=46, n=10, amp=5, soft=True, sb=92, seed=15) + [
        L(outline([(18, 46), (34, 30), (50, 28), (66, 30), (82, 46), (80, 60), (70, 52), (62, 64, 1), (56, 50), (46, 64, 1), (40, 52), (30, 62, 1), (24, 52)]), 'mid', 'f')]
    c['side'] = dome('side', top=0, w=48, cy=46, n=10, amp=5, soft=True, nape=96, fr=58, seed=15)
    c['back'] = dome('back', top=0, w=50, cy=46, n=10, amp=5, soft=True, nape=96, seed=15)
    c['face'].update(brows=True, mouth='line', hairline=[(6, 66), (20, 54), (50, 50), (80, 54), (94, 66)])
    _set('aretha-rumbell', c)


_aretha()


# Adal Miramond: piel clara grisácea con rayas blancas que le bajan de los ojos y una marca roja en el puente de la nariz
def _adal():
    c = _get('adal-miramond')
    c['front'] = [l for l in c['front'] if not (l['c'] == BLACK and l['w'])]
    c['front'] += [L([(cx, 82), (cx, 92)], WHITE, 'f', False, False, 1.6) for cx in (36, 64)]
    c['front'] += [L([(48, 76), (52, 80)], _c('#c84040'), 'f', False, False, 1.6), L([(52, 76), (48, 80)], _c('#c84040'), 'f', False, False, 1.6)]
    _set('adal-miramond', c)


_adal()


# Rockson Grohl: tirita en la mejilla izquierda
def _rockson():
    c = _get('rockson-grohl')
    c['front'] += [L(blob([(24, 84), (34, 82), (35, 88), (25, 90)], 3), _c('#e8a878'), 'f', True, True)]
    _set('rockson-grohl', c)


_rockson()


# Cane Fangley: piel tostada clara; la marca negra es una V que baja de la frente al puente de la nariz y sombra alrededor
# de los ojos, no un antifaz
def _cane():
    c = _get('cane-fangley')
    DB = _c('#3a2a24')
    c['front'] = [l for l in c['front'] if not (l['z'] == 'f' and isinstance(l['c'], tuple) and (l['c'] in (DB, _c('#c8a07a')) or min(l['c'][:3]) > 240))]
    c['face'].update(eyes='normal')
    c['pal']['iris'] = _c('#8a7a6a')
    c['front'] += [L(outline([(40, 54), (50, 60), (60, 54), (54, 72), (50, 80, 1), (46, 72)]), DB, 'f', False)]
    c['front'] += [L(quad((cx - 8, 72), (cx, 66), (cx + 8, 72)), DB, 'f', False, False, 2.4) for cx in (36, 64)]
    c['side'] = [l for l in c['side'] if not (l['z'] == 'f' and isinstance(l['c'], tuple) and (l['c'] == DB or min(l['c'][:3]) > 240))]
    c['side'] += [L(outline([(80, 56), (88, 62), (88, 74), (84, 70)]), DB, 'f', False)]
    _set('cane-fangley', c)


_cane()


# Lita Vault: por debajo de las orejas el pelo acaba en tirabuzones BLANCOS a los lados
def _lita():
    from chars import rope
    c = _get('lita-vault')
    GR = _c('#c8c8d0')
    for x, s in ((12, 1), (88, -1)):
        c['front'] += [L(rope((x, 66), (x - 8 * s, 78), (x, 88), 8.5), WHITE, 'f'), L(rope((x, 86), (x + 7 * s, 94), (x - 1 * s, 102), 7.5), WHITE, 'f'),
                       L(quad((x - 3 * s, 74), (x + 2 * s, 80), (x - 2 * s, 86)), GR, 'f', False, False, 1.2)]
    c['side'] += [L(rope((36, 66), (28, 78), (36, 90), 6.5), WHITE, 'f'), L(rope((36, 88), (44, 96), (36, 104), 5.5), WHITE, 'f')]
    for x, s in ((14, 1), (86, -1)):
        c['back'] += [L(rope((x, 66), (x - 8 * s, 78), (x, 90), 6.5), WHITE, 'f'), L(rope((x, 88), (x + 7 * s, 96), (x, 104), 5.5), WHITE, 'f')]
    _set('lita-vault', c)


_lita()


# Kota (modelo 3D): sombrero negro de copa alta hendida con cinta y ala más estrecha (de perfil se ve la copa, no un hongo)
def _kota():
    c = _get('kota')
    H, B, HL = _c('#2b2121'), _c('#1a1414'), _c('#3e3232')
    hat_f = [L(outline([(-6, 42), (50, 32), (106, 42), (100, 50), (50, 44), (0, 50)]), H, 'f', True, True),
             L(outline([(12, 38), (14, 10), (30, -4), (50, 2), (70, -4), (86, 10), (88, 38)]), H, 'f', True, True),
             L(outline([(13, 28), (87, 28), (88, 38), (12, 38)]), B, 'f', False),
             L(outline([(62, -2), (80, 8), (84, 26), (72, 26)]), HL, 'f', False)]
    hat_s = [L(outline([(-12, 46), (40, 34), (110, 26), (108, 34), (40, 44), (-10, 54)]), H, 'f', True, True),
             L(outline([(10, 38), (12, 8), (30, -6), (60, -6), (80, 4), (86, 32)]), H, 'f', True, True),
             L(outline([(10, 28), (86, 22), (86, 32), (10, 38)]), B, 'f', False)]
    hat_b = [L(outline([(-6, 44), (50, 38), (106, 44), (100, 54), (50, 50), (0, 54)]), H, 'f', True, True),
             L(outline([(12, 40), (14, 10), (30, -4), (50, 0), (70, -4), (86, 10), (88, 40)]), H, 'f', True, True),
             L(outline([(13, 30), (87, 30), (88, 40), (12, 40)]), B, 'f', False)]
    keep = lambda v: [l for l in c[v] if l['c'] not in (H, HL)]
    c['front'], c['side'], c['back'] = keep('front') + hat_f, keep('side') + hat_s, keep('back') + hat_b
    _set('kota', c)


_kota()


# Eviden Tracer: monóculo dorado en el ojo que se le ve
def _eviden():
    c = _get('eviden-tracer')
    c['front'] += [L(ell(64, 75, 8, 8) + [ell(64, 75, 8, 8)[0]], _c('#d8b030'), 'f', False, False, 1.8), L(quad((70, 80), (78, 92), (74, 104)), _c('#d8b030'), 'f', False, False, 1.0)]
    c['side'] += [L(ell(81, 75, 6, 8) + [ell(81, 75, 6, 8)[0]], _c('#d8b030'), 'f', False, False, 1.8)]
    _set('eviden-tracer', c)


_eviden()


# Flaurine Woodwind: solo un par de rulos a los lados, a la altura de la boca (no dos pares)
def _flaurine():
    c = _get('flaurine-woodwind')
    c['front'] = [l for l in c['front'] if not (l['c'] == 'mid' and len(l['s']) == 36 and l['s'][0][1] > 95)]
    c['front'] = [l if not (l['c'] == 'mid' and len(l['s']) == 36) else L(ell(sum(p[0] for p in l['s']) / 36, 86, 14, 8.5)) for l in c['front']]
    c['front'] += [L([(x0, 76), (x1, 76)], 'shade', 'f', False, False, 1.2) for x0, x1 in ((-6, 10), (90, 106))]
    c['front'] = [L(l['s'] if l['w'] == 0 else [(x, 86) for x, _ in l['s']], l['c'], l['z'], l['sil'], l['ln'], l['w']) if (l['w'] and l['s'][0][1] == 76) else l for l in c['front']]
    _set('flaurine-woodwind', c)


_flaurine()


# Terrell Brightley (modelo 3D): la melena va recogida detrás en un moño bajo en la coronilla; las puntas rojas solo
# asoman por los lados
def _terrell():
    c = _get('terrell-brightley')
    RED = _c('#d84a2a')
    c['back'] = [l for l in c['back'] if l['c'] != RED]
    c['back'] += [L(outline([(2, 86), (16, 86), (14, 98), (4, 98)]), RED, 'f', False), L(outline([(98, 86), (84, 86), (86, 98), (96, 98)]), RED, 'f', False),
                  L(ell(50, 24, 12, 10), 'shade', 'f', True, True),
                  L([(42, 32), (50, 28), (58, 32)], 'deep', 'f', False, False, 1.6),
                  strand([(30, 14), (44, 28)], 'deep', 'f', 1.0), strand([(70, 14), (56, 28)], 'deep', 'f', 1.0)]
    c['side'] += [L(ell(8, 24, 10, 9), 'shade', 'f', True, True), L([(16, 18), (20, 30)], 'deep', 'f', False, False, 1.4)]
    _set('terrell-brightley', c)


_terrell()


# Rina Eastvale (modelo 3D): de perfil la coleta sale por detrás de la oreja, atada con la goma, y cae hacia atrás
def _rina():
    c = _get('rina-eastvale')
    TIE = _c('#f0e0a0')
    c['side'] = [l for l in c['side'] if l['c'] != TIE]
    c['side'] += [L(outline([(30, 60), (40, 58), (36, 90), (30, 128, 1), (22, 100)]), 'mid', 'f'), L(ell(34, 60, 4, 4), TIE, 'f')]
    _set('rina-eastvale', c)


_rina()


# Josephine (modelo 3D): de espaldas el capuchón blanco enmarca la cabeza y la nuca es del color de la piel (topo)
def _josephine():
    c = _get('josephine')
    TAUPE = _c('#c8a4a0')
    c['back'] += [L(blob([(18, 50), (36, 32), (64, 32), (82, 50), (84, 80), (70, 104), (50, 110), (30, 104), (16, 80)], 6), TAUPE, 'f', False),
                  L(blob([(56, 36), (80, 52), (82, 80), (68, 102), (62, 70)], 6), tone(TAUPE, 0.86), 'f', False)]
    _set('josephine', c)


_josephine()


# Juniper Cushionne: ojos grandes y oscuros (no puntitos)
def _juniper():
    c = _get('juniper-cushionne')
    c['face']['eyes'] = 'big'
    c['pal']['iris'] = _c('#2a2020')
    _set('juniper-cushionne', c)


_juniper()
