"""Correcciones de la revisión de diseños (grupo sc_vrc): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda.

Grupo sc_vrc: ojeadores de Victory Road (scouts-vr). Referencia: su retrato (src/assets/pack/portraits/scouts-vr/).
Los colores de piel y pelo están medidos en el retrato (el tono plano dominante de la cara y del pelo)."""
import copy
import math

from chars import CHARS
from heads import L, blob, ell, quad, strand, mirror  # noqa: F401

K = 'scouts-vr:'


# ------------------------------------------------------------------ ayudas (propias: nada de importar de chars)

def hexc(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5)) + (255,)


def tone(c, f):
    return tuple(max(0, min(255, int(v * f))) for v in c[:3]) + (255,)


def mix(c, d, t):
    return tuple(int(c[i] + (d[i] - c[i]) * t) for i in range(3)) + (255,)


def outline(pts, n=6):
    """Contorno cerrado y suave por los puntos; los que llevan un tercer valor, (x, y, 1), son puntas afiladas."""
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


def flat(layers):
    return [x for it in layers for x in (it if isinstance(it, list) else [it])]


def fx(pid):
    """Copia del dibujo actual del ojeador para corregirla (con su misma clave), con las capas en listas planas."""
    c = copy.deepcopy(CHARS[K + pid])
    for v in ('front', 'side', 'back'):
        c[v] = flat(c[v])
    CHARS[K + pid] = c
    return c


def _scale(c, old, new):
    """El tono c con el mismo cambio que va de old a new (para llevar las sombras con el color base)."""
    return tuple(max(0, min(255, round(c[i] * (new[i] + 4) / (old[i] + 4)))) for i in range(3)) + (255,)


def recolor(c, skin=None, hair=None, **keys):
    """Piel y pelo medidos en el retrato: la sombra de la piel y las del pelo (shade, deep, light) siguen al color base
    salvo que se den aparte; keys: otros colores de la paleta ('shade', 'iris', 'brow'...)."""
    p = c['pal']
    if skin:
        s = hexc(skin)
        p['skin_d'] = _scale(p['skin_d'], p['skin'], s)
        if 'nose' in p and p['nose'][:3] == p['skin'][:3]:
            p['nose'] = s
        p['skin'] = s
    if hair:
        h = hexc(hair)
        for k in ('shade', 'deep', 'light'):
            if k in p and k not in keys:
                p[k] = _scale(p[k], p['mid'], h)
        if 'brow' in p and p['brow'][:3] == p['mid'][:3] and 'brow' not in keys:
            p['brow'] = h
        p['mid'] = h
    for k, v in keys.items():
        p[k] = hexc(v) if isinstance(v, str) else v
    return c


# ------------------------------------------------------------------ colores medidos en el retrato
# (pelo, piel): None = estaba bien (diferencia que no se ve). Los demás se apartaban del retrato: piel más oscura o
# amarillenta que la del retrato (casi todos), pelo de otro matiz o más saturado.
COLORS = {
    'tiffany-fencourt': ('#063666', '#ffeae0'),
    'maximus-cordray': ('#433f3e', '#c4906c'),
    'darrell-dignard': ('#b13d40', '#fdcbaa'),
    'finley-brooks': ('#767e85', '#dcac9a'),
    'fergus-lougdon': ('#161450', '#fdd5c2'),
    'bowie-buffoon': (None, '#fccdab'),
    'randy-teastock': ('#899753', '#fcbda8'),
    'selen-dippity': ('#ec7a43', '#fed2be'),
    'eden-snowbell': ('#e9e3df', '#ffebe0'),
    'lyla-loveland': ('#7ea9ef', '#ffe3cd'),
    'liselotte-heartsway': ('#f36149', '#ffe4d2'),
    'keyston-typewright': (None, '#ffe6d3'),
    'brandan-broomdorf': ('#ab2c29', '#feebdf'),
    'valentine-lovejoy': ('#d74a4b', '#ffe5d3'),
    'kellan-beatley': (None, '#c88c75'),
    'millicent-milli-vociere': ('#5e9b7b', '#ffeadf'),
    'ordin-scriben': ('#536261', '#eec4a8'),
    'damian-stonewell': (None, '#fdcdab'),
    'pietro-olley': (None, '#f9a978'),
    'memo-rize': ('#559a50', '#fdccab'),
    'romica-glimmerly': (None, None),
    'kairo-reaser': (None, None),
    'oralyn-everfable': ('#3c3264', '#ffe4d2'),
    'rynor-rushenfort': ('#ffdebc', '#b77360'),
    'tobin-tempelhof': (None, '#fdd9ca'),
    'fermin-dealitz': ('#1c1c3f', '#ffeae0'),
    'howell-bloomhurst': ('#3a2a31', '#b37b68'),
    'salpida-longwheel': ('#c5dac1', '#ffebdf'),
    'tris-baylor': ('#adbcbc', '#fbcdab'),
    'azam-darjeel': (None, '#db9b85'),
    'blossom-laine': ('#157194', '#fed3bd'),
    'circe-roundella': ('#a36a79', '#ffd3be'),
    'marcol-leapstone': ('#044247', '#c38565'),
    'caspian-hearken': (None, '#dca38c'),
    'verity-billows': ('#3f4e4f', '#fed4be'),
    'zoey-tippings': ('#5f404f', '#dcad9b'),
    'healan-masson': ('#44527d', '#fdc6a5'),
    'geri-spears': ('#b5aca2', '#fdc8a3'),
    'ferdy-fenwick': ('#e9e7ea', '#feeadf'),
    'cleon-balogh': ('#7b6556', '#fdcbaa'),
    'bang-revell': ('#5f6132', '#fbbd87'),
    'grace-starlet': ('#2e3049', '#ffe5d1'),
    'gemma-coombs': ('#29184b', '#fbe7d7'),
    'giovanni-buston': ('#584563', '#feebdf'),
    'hovard-schulder': (None, '#fdc7a5'),
    'nadia-watershed': ('#b5625a', '#ffeadf'),
    'jayce-chorden': (None, None),
    'divar-deepwell': (None, '#6a5054'),
    'gentino-sorella': ('#80d0d8', '#b57356'),
    'marius-harlow': ('#214a42', '#c98c76'),
    'coraline-quisittor': ('#807373', '#fde6d7'),
    'timmit-bower': ('#533d49', '#fdd8c4'),
    'thompson-hummings': ('#eff6f8', '#fdccab'),
    'nance-meridian': ('#9b8983', '#fdc8b0'),
    'finck-zaplan': ('#455670', '#fdebdd'),
    'ryker-strive': ('#43405c', '#fed3bf'),
    'sylas-saxton': ('#4c5a77', '#fedfb1'),
    'clarissa-gimmich': ('#d0d4e2', '#ffe5d0'),
    'charlotte-graceslowe': ('#0c2650', '#f7cfb3'),
    'shena-ennigans': ('#26485c', '#fdd4be'),
    'amadeus-lyland': ('#dea33e', '#fdc6a3'),
    'sara-lyle': ('#a6968e', '#feeedc'),
    'mira-fiendish': ('#432a21', '#ffd2be'),
    'richter-poole': (None, '#fee4d2'),
    'mireille-modelle': ('#f4e697', '#ffeae0'),
    'azure-marcet': ('#1e3878', '#fee6d5'),
    'megpie-o-neering': ('#b47272', '#ffe4d3'),
    'justine-gardenet': (None, None),
    'ibuto-shinohara': (None, '#c88c74'),
    'sahl-saltzman': ('#5d2648', '#fdc7a3'),
    'minty-shuttlebrook': ('#53507f', '#ffd2bc'),
    'ryden-waverley': ('#4b6475', '#b56b57'),
    'finnard-grit': ('#432f53', '#fee0b2'),
    'gildred-gainstead': ('#e6cba2', '#c88b75'),
    'shiryu-hanabusa': ('#f9c6c5', '#fed1bc'),
    'trew-talif': ('#e8d8dd', '#c98b76'),
    'mina-veyance': (None, '#ffc7b0'),
    'rafton-calmers': (None, '#c38665'),
    'thalia-petras': (None, '#ffeadf'),
    'ana-santini': ('#401a33', '#fee5d2'),
    'huxley-tagg': (None, '#ffe5d3'),
    'aimee-porteret': ('#704a31', '#fee6d8'),
    'jett-allegri': (None, None),
    'olan-ackroyd': ('#cb3541', None),
    'silky-fersken': ('#d45365', '#ffe3d3'),
    'sonata-cherub': (None, '#ffe5d0'),
    'lazaro-coveton': ('#b48aba', '#fed9cb'),
    'clyde-dalen': ('#a87052', '#ffe3cd'),
    'ayle-holland': ('#9b5e65', '#fed3c0'),
    'corday-dremin': ('#3b9e9e', '#ffd3be'),
    'luceus-cloudstrider': ('#a8aeb6', '#ffe5d3'),
    'madeline-milke': ('#341f18', '#ffd3be'),
    'carlisle-laimlight': (None, '#ffe5d1'),
    'petra-cornerstone': (None, '#dbad9a'),
    'edmin-streator': (None, '#fde8df'),
    'zinnia-crylic': ('#aa2e34', '#ffe5d1'),
    'codey-presto': ('#65644e', '#fdd3be'),
    'audreen-slumberey': ('#58b4c0', '#ffe5d3'),
    'mirko-harding': ('#e8556f', '#ffeae0'),
    'tufton-frizzell': (None, '#f6bcaa'),
    'cora-inkton': ('#b58c97', '#fddad0'),
    'corwin-lockhart': (None, '#ffe5d2'),
    'edton-prentt': ('#514b1b', '#fec5a3'),
    'roxy-roarke': (None, '#ffcea6'),
    'donnie-summerfield': ('#56392f', '#fccdab'),
    'judis-nitcher': (None, None),
    'izekiel-truth': (None, '#fee6d5'),
    'griffin-fastwell': (None, '#ffe5d2'),
    'tito-de-core': ('#557bb9', '#fdc7a3'),
    'crest-vertall': ('#172445', '#dbad9b'),
    'wing-hyland': ('#9a3931', '#c98b76'),
    'pillan-hallstead': ('#ce7d16', '#fed1be'),
    'domino-guerrera': ('#282628', '#dbac9a'),
    'dasher-ballard': ('#f4fb9e', '#fed3be'),
    'cornelia-hoopett': ('#8bcaa7', '#ffeae0'),
    'volbert-brackenbal': ('#516e68', '#c98a75'),
    'ezekiel-gravendirge': ('#406195', '#ffc6a6'),
    'jakell-wardly': ('#122316', None),
    'alyra-verselle': ('#4b6fa2', '#fdc7a3'),
    'zaydan-smythe': ('#bf94bf', '#fdccab'),
    'rico-falsettis': (None, None),
    'bowen-fleurmett': ('#d96231', '#fccdab'),
    'alphonse-wreckenbach': (None, '#fec6a2'),
    'vergil-turnaraud': ('#788286', '#ffe5d0'),
    'pina-propp': ('#5f422c', '#fbbd87'),
    'hanz-boll': ('#9b4925', '#c98c76'),
    'capricia-saiz': ('#592024', '#e0ac8a'),
    'orlando-sterlight': (None, None),
    'ezrail-corbell': (None, '#ffe6d1'),
    'landon-crosser': ('#9a292e', '#fdbd87'),
    'trebor-donders': ('#feb4d8', '#fee0b1'),
    'wander-treeday': ('#b04f69', '#ffc7a3'),
    'ellie-fumble': (None, '#ffebe0'),
    'renee-sirensong': ('#8f7653', '#fdccaa'),
    'ralya-chersey': ('#e1a75c', '#fedfb1'),
    'farah-tigressa': ('#4b8d70', '#fed9cb'),
    'agil-surefall': ('#d7cca3', '#c18e6b'),
    'kujira-torikawa': (None, None),
    'aeron-rushmore': ('#5f6c98', '#ffe9df'),
    'torwyn-endeavor': ('#78cce0', '#fdc7a3'),
    'bridget-steepen': (None, None),
    'isolde-bourgeon': (None, '#fdbc88'),
    'fitzbon-vivant': ('#7a7776', None),
    'zacharias-klutchett': ('#957952', '#fac8a8'),
    'edmund-boon': ('#893e82', '#f8cbaa'),
    'octavian-da-lua': ('#9a3536', '#fee0b1'),
    'taxter-coilschmidt': ('#47587f', '#fec6a2'),
    'stellan-checkman': ('#ceb86b', '#fdc5a2'),
    'argion-boneback': (None, '#b67458'),
    'yohannes-drummand': ('#514343', '#fccca9'),
    'tobias-thumpern': ('#c78970', '#dbad9b'),
    'teagan-leafhart': (None, None),
    'paxton-plumfield': ('#49434d', '#f3bca4'),
    'kali-seaborn': (None, None),
    'stouton-savant': (None, '#fed4be'),
    'colette-brushmont': (None, '#ffe5d3'),
    'kohara-staley': (None, None),
    'jackson-bover': (None, '#fdcbaa'),
    'kara-okenridge': (None, None),
    'jubilee-meriday': ('#fcf8d0', None),
    'liron-suesskind': ('#8e8e8e', '#fdc3a3'),
    'bam-buschutt': ('#2a1f1a', '#d3a47d'),
    'linton-judson': ('#262a2d', '#fee6d1'),
    'kenneth-frostner': (None, None),
    'montoodle-wixley': ('#9f4b73', '#fdc7a3'),
    'misia-cheveuse': (None, '#fbccaa'),
    'noelle-harmon': ('#b99988', '#fed3bc'),
    'cid-drewend': ('#334f90', '#fccaa8'),
    'elian-kitronic': ('#564f57', '#fcc7a4'),
    'dazziel-spinwick': ('#ae7f98', '#fed4bd'),
    'micco-chantelle': (None, '#ffe5d0'),
    'kipp-sycamore': (None, '#fdcdab'),
    'drewey-fournell': ('#704f4c', '#fcc7a3'),
    'dashiell-fass': ('#e5d151', '#f9aa79'),
    'matilde-pendlebury': ('#4f2a3e', '#fee7cd'),
    'sabine-jellis': ('#2e0b0c', '#feebe0'),
    'aylin-terpheis': (None, '#ffe4d2'),
    'masala-mettler': ('#bd3b5d', '#ffd2bf'),
    'somnal-brightmore': ('#32344a', '#c48665'),
    'dreamer-havenridge': (None, '#ffe5d0'),
    'francesca-fintootle': ('#6d538e', '#fed4be'),
}
for _pid, (_h, _s) in COLORS.items():
    if _h or _s:
        recolor(fx(_pid), skin=_s, hair=_h)

# sombras y segundos colores medidos aparte (la sombra del retrato no sigue la proporción del tono base)
recolor(CHARS[K + 'selen-dippity'], shade='#c93a2a', deep='#9a2a1e', light='#f39a5e')  # arriba naranja, abajo rojo
recolor(CHARS[K + 'gentino-sorella'], shade='#3a6466', deep='#2a4a4c')  # cresta cian clara, lados verde azulado oscuro
recolor(CHARS[K + 'tito-de-core'], pink='#ea306f')


# ------------------------------------------------------------------ forma y detalles

def _shift(layer, dx, dy):
    layer['s'] = [(x + dx, y + dy) for x, y in layer['s']]


def _swap(c, old, new):
    """Cambia en todas las vistas el color fijo old (tupla) por new."""
    for v in ('front', 'side', 'back'):
        for l in c[v]:
            if isinstance(l['c'], tuple) and l['c'][:3] == old[:3]:
                l['c'] = new


# Selen Dippity: el pelo es naranja arriba y rojo en las puntas de abajo: los dos mechones que salen por los lados, rojos
_c = CHARS[K + 'selen-dippity']
for _l in _c['front'][2:4]:
    _l['c'] = 'shade'

# Gentino Sorella: cresta cian clara y los dos lados rapados verde azulado oscuro (no solo uno)
_c = CHARS[K + 'gentino-sorella']
_c['front'].insert(2, L(mirror(_c['front'][1]['s']), 'shade', 'b', False))

# Blossom Laine: los dos moños asoman por arriba de la cabeza, con su goma roja por dentro (estaban tapados por el pelo)
_c = CHARS[K + 'blossom-laine']
for _v, _idx in (('front', (0, 1, 2, 3)), ('back', (0, 1, 2, 3))):
    for _i in _idx:
        _l = _c[_v][_i]
        _shift(_l, -3 if _l['s'][0][0] < 50 else 3, -16)
        if isinstance(_l['c'], tuple):
            _l['z'], _l['sil'] = 'f', False
for _l in _c['side'][:2]:
    _shift(_l, 0, -14)
    if isinstance(_l['c'], tuple):
        _l['z'], _l['sil'] = 'f', False
for _v in ('front', 'side', 'back'):  # la goma: una banda roja ancha por el lado de dentro del moño, no un punto
    for _l in _c[_v]:
        if isinstance(_l['c'], tuple) and _l['c'][:3] == (208, 42, 58):
            _x = sum(p[0] for p in _l['s']) / len(_l['s'])
            _y = sum(p[1] for p in _l['s']) / len(_l['s'])
            _d = 1 if _x < 50 else -1
            if _v == 'side':
                _d = 1
            _l['s'] = outline([(_x + _d * 2, _y - 11), (_x + _d * 8, _y - 9), (_x + _d * 9, _y + 9), (_x + _d * 3, _y + 11)])
            _l['ln'] = True

# Charlotte Graceslowe: gorro azul marino oscuro como el del retrato (#002f61), no azul medio
_c = CHARS[K + 'charlotte-graceslowe']
_swap(_c, (30, 58, 110), hexc('#0a3466'))
_swap(_c, (22, 44, 86), hexc('#04264c'))

# Ibuto Shinohara: franja malva rosada que le cruza lo alto de la cabeza de la frente a la nuca (el resto, pardo oscuro)
_c = CHARS[K + 'ibuto-shinohara']
_c['pal']['stripe'] = hexc('#9b5b7d')
_c['pal']['stripe_d'] = hexc('#6e3a56')
_c['front'].insert(2, L(outline([(40, 40), (42, 14), (50, 9), (58, 14), (60, 40), (50, 44)]), 'stripe', 'b', False))
_c['front'].insert(3, L(outline([(52, 8), (58, 12), (60, 40), (55, 42)]), 'stripe_d', 'b', False))
_c['side'].insert(2, L(outline([(20, 16), (40, 9), (62, 12), (72, 30), (64, 34), (52, 18), (34, 18), (18, 28)]), 'stripe', 'b', False))
_c['back'].insert(2, L(outline([(41, 10), (50, 8), (59, 10), (59, 60), (50, 66), (41, 60)]), 'stripe', 'b', False))

# Trew Talif: los rizos oscuros morados son grandes: dos lóbulos arriba (como cuernos) y racimos a los lados de la cara,
# no cuatro lunares
_c = CHARS[K + 'trew-talif']
_c['pal']['curl'] = hexc('#4a3552')
_c['pal']['curl_l'] = hexc('#6f5d6a')
for _v in ('front', 'side', 'back'):
    _c[_v] = [l for l in _c[_v] if not (isinstance(l['c'], tuple) and len(l['s']) == 36 and l['z'] == 'b' and not l['sil'])]
_c['front'][1:1] = [L(blob([(22, 6), (34, -6), (46, -2), (44, 8), (32, 10)], 6), 'curl', 'b', False),
                    L(blob([(78, 6), (66, -6), (54, -2), (56, 8), (68, 10)], 6), 'curl', 'b', False),
                    L(blob([(-2, 34), (8, 22), (18, 30), (16, 52), (6, 60), (-2, 50)], 6), 'curl', 'b', False),
                    L(blob([(102, 34), (92, 22), (82, 30), (84, 52), (94, 60), (102, 50)], 6), 'curl', 'b', False),
                    L(blob([(2, 68), (10, 62), (16, 72), (10, 82)], 6), 'curl_l', 'b', False),
                    L(blob([(98, 68), (90, 62), (84, 72), (90, 82)], 6), 'curl_l', 'b', False)]
_c['side'][1:1] = [L(blob([(30, -4), (46, -8), (54, 2), (40, 8)], 6), 'curl', 'b', False),
                   L(blob([(4, 30), (16, 22), (30, 32), (26, 56), (10, 62)], 6), 'curl', 'b', False)]
_c['back'][1:1] = [L(blob([(22, 6), (34, -6), (46, -2), (44, 8), (32, 10)], 6), 'curl', 'b', False),
                   L(blob([(78, 6), (66, -6), (54, -2), (56, 8), (68, 10)], 6), 'curl', 'b', False),
                   L(blob([(-2, 34), (8, 22), (20, 32), (18, 58), (4, 64)], 6), 'curl', 'b', False),
                   L(blob([(102, 34), (92, 22), (80, 32), (82, 58), (96, 64)], 6), 'curl', 'b', False)]

# Fitzbon Vivant: no es calvo: lleva el pelo gris corto y liso que le cubre toda la cabeza, con la raya del nacimiento
# recta por encima de la frente y patillas cortas por delante de las orejas; cejas grises
from chars_scouts_ie1_09 import dome  # noqa: E402

_c = CHARS[K + 'fitzbon-vivant']
_c['pal'].update(mid=hexc('#7d7a7a'), shade=hexc('#5f5d5e'), brow=hexc('#6a6868'))
for _v in ('front', 'side', 'back'):
    _c[_v] = [l for l in _c[_v] if not (isinstance(l['c'], tuple) and l['c'][:3] == (138, 138, 142)) and l['c'] not in ('skin', 'skin_d')]
_c['face']['hairline'] = [(10, 60), (18, 48), (32, 41), (50, 40), (68, 41), (82, 48), (90, 60)]
_c['front'] = dome('front', top=6, w=45, cy=46, sb=70) + _c['front']
_c['side'] = dome('side', top=6, w=45, cy=46, nape=82, fr=46) + _c['side']
_c['back'] = dome('back', top=6, w=45, cy=46, nape=82) + _c['back']

# Linton Judson: el pelo corto acaba arriba en una cresta en pico (como una punta de flecha), no en una bóveda redonda
_c = CHARS[K + 'linton-judson']
_c['front'].append(L(outline([(26, 16), (50, 1, 1), (74, 16), (50, 14)]), 'mid', 'b'))
_c['side'].append(L(outline([(24, 12), (46, 0, 1), (70, 14), (46, 12)]), 'mid', 'b'))
_c['back'].append(L(outline([(26, 16), (50, 1, 1), (74, 16), (50, 14)]), 'mid', 'b'))
