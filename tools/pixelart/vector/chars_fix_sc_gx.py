"""Correcciones de la revisión de diseños (grupo sc_gx): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda.

Ojeadores de GX (scouts-gx), comparados uno a uno con su retrato de Victory Road (y su modelo 3D cuando lo hay)."""
import copy  # noqa: F401
from chars import CHARS, OUTC, hexc, mix, outline  # noqa: F401
from heads import L, blob, ell, lerp, quad  # noqa: F401

K = 'scouts-gx:'
WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)


def _fx(pid):
    """Copia del dibujo actual del ojeador para corregirla (con su misma clave), con las capas en listas planas."""
    c = copy.deepcopy(CHARS[K + pid])
    for v in ('front', 'side', 'back'):
        c[v] = [x for it in c[v] for x in (it if isinstance(it, list) else [it])]
    CHARS[K + pid] = c
    return c


def _bbox(layer):
    xs = [p[0] for p in layer['s']]
    ys = [p[1] for p in layer['s']]
    return min(xs), min(ys), max(xs), max(ys)


def _drop(c, view, pred):
    c[view] = [l for l in c[view] if not pred(l)]


def _scale(new, old_mid, old_d):
    """Sombra nueva con la misma relación de tono que tenía la antigua respecto a su color base."""
    return tuple(max(0, min(255, int(round(new[i] * (old_d[i] / max(1, old_mid[i])))))) for i in range(3)) + (255,)


def _recolor(c, key, hexcol, dep=()):
    """Cambia un color de la paleta (key) y lleva con él sus sombras (dep) en la misma proporción."""
    p = c['pal']
    new = hexc(hexcol) if isinstance(hexcol, str) else hexcol
    old = p[key]
    for d in dep:
        if d in p:
            p[d] = _scale(new, old, p[d])
    p[key] = new


def _lit(c, mid=None, skin=None, t=1.0):
    """Pelo (mid) y piel (skin) medidos en el retrato; t < 1 se queda a medio camino del tono anterior."""
    p = c['pal']
    if mid:
        same = p.get('skin') == p['mid']
        _recolor(c, 'mid', mix(p['mid'], hexc(mid), t), ('shade', 'deep', 'light'))
        if same and not skin:
            _recolor(c, 'skin', p['mid'], ('skin_d',))
    if skin:
        _recolor(c, 'skin', mix(p['skin'], hexc(skin), t), ('skin_d', 'nose'))


def ears_f(view, c='skin', inner='skin_d', y=64, tip=(-6, 46), base=18, h=18):
    """Orejas de punta que asoman por fuera del pelo (por delante de él, como en los retratos)."""
    tx, ty = tip
    if view == 'side':
        return [L(outline([(42, y + 2), (30, ty + 4, 1), (54, y - 2), (52, y + h - 2)]), c, 'f'),
                L(outline([(44, y + 4), (34, ty + 10, 1), (50, y + 2), (48, y + h - 6)]), inner, 'f', False)]
    if view == 'back':
        tx -= 2
    left = [(base + 1, y), (tx, ty, 1), (base - 1, y + h)]
    inn = [(base - 1, y + 3), (tx + 6, ty + 7, 1), (base - 2, y + h - 5)]
    m = lambda pts: [(100 - p[0],) + tuple(p[1:]) for p in pts]  # noqa: E731
    out = [L(outline(left), c, 'f'), L(outline(m(left)), c, 'f')]
    if view == 'front':
        out += [L(outline(inn), inner, 'f', False), L(outline(m(inn)), inner, 'f', False)]
    return out


# ------------------------------------------------------------------ colores medidos en el retrato
# (k-means de los píxeles del retrato: el tono iluminado del pelo / casco y de la piel; el dibujo se iba de matiz,
# saturación o claridad). Formato: id: (pelo, piel); None deja el que había.
_COLS = {
    'akram-alvayra': ('#926088', None),           # melena malva grisácea, no morado saturado
    'durmali-altos': ('#3f428a', '#c1e5ed'),
    'nathan-nate-adams': ('#683722', '#f9caa1'),
    'anthocia-arnin': ('#b64436', None),
    'biffy-sausse': ('#b6352e', None),
    'brom-hexine': ('#4f2a36', '#e2cbb0'),
    'dioxily-bocca': (None, '#ac865f'),
    'carabcalkrab-antares': ('#53769e', '#ad8760'),
    'cherrie-menjikko': (None, '#c2e4eb'),
    'claria-leone': (None, '#bee5ec'),
    'derika-cachil': ('#be5461', None),
    'doro-might': ('#38585c', None),
    'hawky-turbay': ('#634571', None),
    'isor-eshen': ('#a59d53', None),
    'jude-caleb-juleb': ('#255650', '#eaba88'),
    'kiroh-beira': ('#e1a009', None),
    'katie-forester': ('#734037', None),
    'karka-poe': ('#767c50', None),
    'cord-ratozol': ('#e6d16f', None),
    'luka-aril': ('#6badc2', '#f6bb80'),
    'mag-nessium': (None, '#ce9768'),
    'jasper-lerner': ('#7c676c', None),
    'josina-mary': (None, '#d19d78'),
    'skip-flashman': ('#352116', '#f6ba7c'),
    'hattar-meppo': ('#f2cbb7', None),
    'menoh-seaweed': ('#9ce180', '#bde5ec'),
    'mesa-bute': (None, '#cd986a'),
    'metha-nol': (None, '#fcd28d'),
    'kaven-mirae': ('#5fb46f', '#e4c749'),
    'mikala-datasby': ('#86252f', '#bce5ed'),
    'milo-agrias': ('#4a3e5a', None),
    'miriam-sharpe': ('#f69225', None),
    'seraph-sharpe': ('#6c3d0a', '#f8ba7c'),
    'sierra-mone': ('#56484c', None),
    'moka-rimmer': ('#b85c3c', '#8fbdaa'),
    'nactena-naksey': (None, '#bce5ee'),
    'norlan-rikwatta': (None, '#8bb5a9'),
    'norritz-ranhatch': ('#f4b955', None),
    'tri-trot-tritrot': ('#e2647a', None),
    'coby-redstone': (None, '#cd986b'),
    'ribo-som': ('#5b5890', None),
    'skoll-pion': ('#aa3d3c', '#eee4f2'),
    'oggris-roya': ('#50d3ab', None),
    'catro-corydoras': ('#f9f2a8', '#b6dcea'),
    'nomare-lusha': ('#64707b', None),
    'tem-akirrol': ('#617ea6', '#bde5ed'),
    'schemer-guile': (None, '#d88e4e'),
    'sena-arata': ('#d5633e', None),
    'seth-yinkley': ('#356db4', '#bfe5ec'),
    'shaurashaula-toxbarb': ('#d4605c', '#bc8a68'),
    'luvy-duvy-luvyduvy': ('#59bbc4', None),
    'sylvany-igan': ('#bc2710', '#fcce9f'),
    'tage-hamley': ('#58729c', None),
    'tau-rin': ('#9ac3d3', None),
    'arion-mark-markion': ('#853812', None),
    'eas-tarmo': ('#937357', None),
    'tetrae-charlong': (None, '#bee4ed'),
    'tetsu-foreman': (None, '#c27e4a'),
    'teodorus-toxsin': ('#fbe490', '#b6e0ec'),
    'thor-nado': ('#7d7cb7', None),
    'tobiah-bragg': ('#5a3c31', None),
    'tog-romack': ('#a886c0', None),
    'hubert-iger': ('#1a120c', None),
    'bailong-victor-baivic': ('#6b97a0', None),
    'bailong-tezcat-tezlong': (None, '#d49c68'),
    'umral-seaslug': ('#876ea3', '#bce3eb'),
    'ricky-regomen': ('#89b7a7', '#f9f6d2'),
    'iwers-mogan': (None, '#c6e1d8'),
    'yolanda-umick': ('#5a8cbe', None),
    'ducksquiggan-tarboyle': ('#e8e468', None),
    'julia-blaze': ('#7b604f', '#f9d4a0'),
    'concord-rigan': (None, '#f8e4b4'),
    'uni-sync-unisync': (None, '#be8c67'),
    'roleia-orbes': ('#8463c0', None),
    'saber-sabel': ('#84101f', None),
    'kanzan-focho': ('#cbb9ce', None),
    'doyle-coco': ('#f8d568', None),
    'sugaken': (None, '#d8a26e'),
}
for _pid, (_h, _s) in _COLS.items():
    _lit(_fx(_pid), _h, _s, 0.85)


# ------------------------------------------------------------------ orejas de punta que no se veían de frente
# (las dibujaba detrás de la melena y el pelo las tapaba; en el retrato asoman bien por los lados)
for _pid, _kw in {
    'anthocia-arnin': dict(tip=(-8, 44)),
    'dioxily-bocca': dict(tip=(-12, 50)),
    'brom-hexine': dict(tip=(-8, 48)),
    'biffy-sausse': dict(tip=(-8, 44)),
    'catora-peiji': dict(tip=(-12, 46)),
    'diazo-cabot': dict(tip=(-6, 50)),
    'golgi-tai': dict(tip=(-10, 50)),
    'elreid-orbes': dict(tip=(-16, 40)),
    'ribo-som': dict(tip=(-8, 50)),
}.items():
    _c = _fx(_pid)
    _c['front'] += ears_f('front', **_kw)
    _c['back'] += ears_f('back', **_kw)


# ------------------------------------------------------------------ uno a uno

# Claria Leone: el mechón rosa le tapa del todo el ojo izquierdo (el de la derecha de la imagen) hasta la mejilla
c = _fx('claria-leone')
c['front'].append(L(outline([(42, 30), (72, 30), (88, 48), (88, 78), (80, 96, 1), (72, 84), (60, 80, 1), (54, 64), (46, 46)]), 'mid', 'f'))
c['front'].append(L(outline([(62, 36), (80, 44), (84, 74), (78, 88, 1), (74, 70)]), 'shade', 'f', False))

# Hawky Turbay: orejas largas de punta hacia fuera (no unos círculos rosas en las mejillas)
c = _fx('hawky-turbay')
_drop(c, 'front', lambda l: l['c'] == 'skin' or (not isinstance(l['c'], str) and l['c'][:3] == (240, 184, 200) and _bbox(l)[1] > 60))
c['front'] += [L(outline([(22, 66), (-14, 52, 1), (22, 82)]), 'skin', 'f'), L(outline([(78, 66), (114, 52, 1), (78, 82)]), 'skin', 'f'),
               L(outline([(18, 69), (-6, 58, 1), (18, 78)]), hexc('#f0c4d4'), 'f', False), L(outline([(82, 69), (106, 58, 1), (82, 78)]), hexc('#f0c4d4'), 'f', False)]

# Dotmar Tricks y Elu Suay: los botones de los lados de la tele (barras azul marino con punta amarilla / conectores)
c = _fx('dotmar-tricks')
for s in (1, -1):
    m = (lambda x: x) if s == 1 else (lambda x: 100 - x)
    c['front'] += [L(blob([(m(-14), 44), (m(6), 44), (m(6), 52), (m(-14), 52)], 2), hexc('#2a3a4a'), 'f'),
                   L(blob([(m(-20), 42), (m(-12), 42), (m(-12), 54), (m(-20), 54)], 2), hexc('#f0b840'), 'f')]
c = _fx('elu-suay')
for s in (1, -1):
    m = (lambda x: x) if s == 1 else (lambda x: 100 - x)
    c['front'] += [L(blob([(m(-10), 62), (m(6), 62), (m(6), 80), (m(-10), 80)], 2), hexc('#5aa0d8'), 'f'),
                   L(blob([(m(-16), 64), (m(-8), 64), (m(-8), 68), (m(-16), 68)], 1), hexc('#f0d040'), 'f'),
                   L(blob([(m(-16), 74), (m(-8), 74), (m(-8), 78), (m(-16), 78)], 1), hexc('#f0d040'), 'f')]


def _insert_before(c, view, pred, layers):
    """Mete capas justo antes de la primera que cumpla pred (para que queden debajo de ella)."""
    for i, l in enumerate(c[view]):
        if pred(l):
            c[view][i:i] = layers
            return
    c[view] += layers


def _is(col):
    col = hexc(col) if isinstance(col, str) else col
    return lambda l: not isinstance(l['c'], str) and tuple(l['c'][:3]) == tuple(col[:3])


def _mir(pts):
    return [(100 - p[0],) + tuple(p[1:]) for p in pts]


# Hawky Turbay, de espaldas: también las orejas de punta
c = CHARS[K + 'hawky-turbay']
_drop(c, 'back', lambda l: l['c'] == 'skin')
c['back'] += [L(outline([(22, 66), (-14, 52, 1), (22, 82)]), 'skin', 'b'), L(outline([(78, 66), (114, 52, 1), (78, 82)]), 'skin', 'b')]

# Wacke Koshra: ojos de aro blanco CON pupila negra, y la cara de debajo del casco crema verdosa (no naranja) desde los ojos
c = _fx('wacke-koshra')
_drop(c, 'front', lambda l: _is('#f6dcb8')(l) and _bbox(l)[1] > 70)
_insert_before(c, 'front', lambda l: _is('#f4f4f4')(l),
               [L(blob([(24, 74), (38, 78), (50, 74), (62, 78), (76, 74), (74, 96), (62, 104), (50, 106), (38, 104), (26, 96)], 6), hexc('#e6e3bf'), 'f'),
                L(blob([(24, 94), (50, 100), (76, 94), (66, 104), (34, 104)], 4), hexc('#c6c2a2'), 'f', False)])
c['front'] += [L(ell(36.4, 68.4, 1.7, 1.9), BLACK, 'f', False), L(ell(63.6, 68.4, 1.7, 1.9), BLACK, 'f', False),
               L([(36, 70), (37, 84)], OUTC, 'f', False, False, 1.2),
               L([(38, 92), (44, 90), (50, 92), (56, 90), (62, 92)], OUTC, 'f', False, False, 1.4)]
_drop(c, 'front', lambda l: l['w'] and len(l['s']) == 2 and l['s'][0] == (40, 90))

# Warim Kalkawa: cada ojo lleva un aro negro grueso alrededor del blanco (antifaz)
c = _fx('warim-kalkawa')
_insert_before(c, 'front', lambda l: l['c'] == WHITE or (not isinstance(l['c'], str) and l['c'][:3] == (248, 248, 248)) or _is('#f6f6f6')(l),
               [L(ell(35, 64, 9.6, 9.8), BLACK, 'f'), L(ell(65, 64, 9.6, 9.8), BLACK, 'f'),
                L(outline([(26, 62), (16, 58, 1), (26, 68)]), BLACK, 'f', False), L(outline([(74, 62), (84, 58, 1), (74, 68)]), BLACK, 'f', False)])

# Kanzan Focho: ojos grandes de iris morado con la raya negra gruesa de arriba que se alarga hacia fuera, hacia las antenas
c = _fx('kanzan-focho')
PU = hexc('#9a5ab0')
for s in (1, -1):
    cx = 50 - 18 * s
    m = (lambda p: p) if s == 1 else _mir
    c['front'] += [L(ell(cx, 57, 7.4, 8.6), WHITE, 'f', True, True), L(ell(cx + 1.2 * s, 58.4, 5.4, 7), PU, 'f', False),
                   L(ell(cx + 1.2 * s, 59, 2.8, 3.8), hexc('#3a1e48'), 'f', False), L(ell(cx - 1.6 * s, 54.6, 1.8, 2), WHITE, 'f', False),
                   L(m(quad((40, 50), (30, 44), (18, 46)) + quad((18, 46), (8, 46), (4, 36))[1:]), OUTC, 'f', False, False, 2.6)]

# Horton Giess: astas verdes largas que salen de las cejas hacia fuera y se curvan hacia arriba (con una rama)
c = _fx('horton-giess')
GN = hexc('#7d8b4f')
ant = [(38, 50), (20, 42), (4, 40), (-8, 30), (-10, 14, 1), (-4, 26), (4, 32), (8, 24), (6, 14, 1), (14, 30), (24, 36), (40, 44)]
c['front'] += [L(outline(ant), GN, 'f'), L(outline(_mir(ant)), GN, 'f')]
c['back'] += [L(outline(ant), GN, 'f'), L(outline(_mir(ant)), GN, 'f')]
c['side'] += [L(outline([(70, 50), (86, 42), (98, 34), (102, 14, 1), (96, 30), (90, 36), (84, 30), (84, 22, 1), (80, 34), (68, 44)]), GN, 'f')]

# Dry Karwack: antifaz negro alrededor de cada ojo (ojos gris lila claro dentro)
c = _fx('dry-karwack')
_insert_before(c, 'front', lambda l: l['c'] == WHITE or (not isinstance(l['c'], str) and l['c'][:3] == (248, 248, 248)),
               [L(outline([(20, 70), (26, 64), (40, 64), (48, 70), (46, 80), (34, 82), (22, 80), (12, 76, 1)]), BLACK, 'f'),
                L(outline(_mir([(20, 70), (26, 64), (40, 64), (48, 70), (46, 80), (34, 82), (22, 80), (12, 76, 1)])), BLACK, 'f')])
c['pal']['iris'] = hexc('#8a90b0')

# Doctor Cross Word Cryptix: el bigote enorme que se curva hacia los lados (perfilado, si no se confundía con el pelo) y la
# barba de puntas
c = _fx('doctor-cross-word-cryptix')
_drop(c, 'front', lambda l: l['c'] == 'mid' and _bbox(l)[1] >= 80)
c['front'] += [L(outline([(50, 104), (64, 100), (74, 92), (80, 100), (76, 112, 1), (68, 110), (62, 120, 1), (56, 112), (50, 124, 1), (44, 112), (38, 120, 1),
                          (32, 110), (24, 112, 1), (20, 100), (26, 92), (36, 100)]), 'mid', 'f', True, True),
               L(outline([(50, 86), (62, 82), (78, 84), (92, 78), (102, 68, 1), (98, 84), (84, 94), (64, 94), (50, 90), (36, 94), (16, 94), (2, 84),
                          (-2, 68, 1), (8, 78), (22, 84), (38, 82)]), 'mid', 'f', True, True),
               L(outline([(56, 88), (70, 88), (86, 86), (94, 80), (84, 92), (64, 92)]), 'shade', 'f', False),
               L([(50, 86), (50, 90)], OUTC, 'f', False, False, 1.0)]

# Moka Rimmer: el flequillo le tapa los ojos, pero se ven la nariz ancha, la boca de dientes y la barba naranja que le
# rodea la boca desde las mejillas
c = _fx('moka-rimmer')
c['face'].update(mouth='grin', mouth_y=94, nose=(50, 84, 4.2))
c['pal']['nose'] = hexc('#6a9e88')
hair = c['front'][0]
c['front'] = [hair,
              L(outline([(14, 40), (30, 28), (50, 26), (70, 28), (86, 40), (86, 70), (78, 76, 1), (72, 66), (64, 74, 1), (58, 66), (50, 76, 1), (42, 66), (36, 74, 1),
                         (28, 66), (22, 76, 1), (14, 70)]), 'mid', 'f'),
              L(outline([(62, 30), (80, 36), (84, 66), (76, 72, 1), (70, 56)]), 'shade', 'f', False),
              L(outline([(12, 74), (24, 82), (32, 98), (42, 104), (58, 104), (68, 98), (76, 82), (88, 74), (90, 100), (80, 116, 1), (66, 120), (58, 130, 1),
                         (50, 124), (42, 130, 1), (34, 120), (20, 116, 1), (10, 100)]), 'mid', 'f'),
              L(outline([(66, 100), (80, 86), (86, 100), (76, 114)]), 'shade', 'f', False),
              L(ell(12, 84, 2.4, 3), hexc('#3a8ad0'), 'f')]

# Globulus Ava: ojos abiertos de párpado caído (no cerrados) y, en la frente, la piel morena sube en dos picos a los lados
# del mechón verde central
c = _fx('globulus-ava')
c['face'].update(eyes='sharp', brows='angry', eye_y=76)
c['pal']['iris'] = hexc('#4a2a1e')
_drop(c, 'front', lambda l: l['c'] == hexc('#4e6a5a') and _bbox(l)[1] < 0)
pk = [(28, 58), (36, 8, 1), (46, 50)]
c['front'] += [L(outline(pk), 'skin', 'f', False, True), L(outline(_mir(pk)), 'skin', 'f', False, True),
               L(outline([(40, 30), (50, 4), (60, 30), (56, 46), (50, 60, 1), (44, 46)]), 'mid', 'f', False, True),
               L(outline([(52, 10), (58, 30), (54, 44), (51, 56, 1)]), 'shade', 'f', False)]

# Seraph Sharpe: las gafas son de montura fina oscura, no dorada
c = _fx('seraph-sharpe')
for v in ('front', 'side'):
    for l in c[v]:
        if _is('#a07838')(l):
            l['c'] = hexc('#3c3230')

# Durmali Altos: flequillo azul recto por debajo del gorro, hasta las cejas
c = _fx('durmali-altos')
_insert_before(c, 'front', lambda l: l['c'] == 'yel',
               [L(outline([(10, 42), (90, 42), (90, 64), (80, 60), (70, 63), (60, 60), (50, 63), (40, 60), (30, 63), (20, 60), (10, 64)]), 'mid', 'f'),
                L(outline([(4, 46), (12, 44), (14, 62), (2, 60, 1)]), 'mid', 'f'), L(outline([(96, 46), (88, 44), (86, 62), (98, 60, 1)]), 'mid', 'f')])

# Golgi Tai: sin flequillo: la frente queda despejada (el pelo nace alto y cae por los lados)
c = _fx('golgi-tai')
c['face']['hairline'] = [(4, 66), (16, 54), (30, 42), (50, 38), (70, 42), (84, 54), (96, 66)]

# Moka Rimmer: la melena es greñuda (puntas por todo el borde), no un casco liso
c = CHARS[K + 'moka-rimmer']
c['front'][0] = L(outline([(2, 104), (-6, 86, 1), (0, 74), (-8, 58, 1), (2, 46), (-2, 30, 1), (10, 24), (12, 8, 1), (26, 8), (34, -4, 1), (44, 2), (54, -6, 1),
                           (62, 2), (74, -2, 1), (78, 10), (92, 10, 1), (90, 24), (102, 30, 1), (98, 46), (108, 58, 1), (100, 74), (106, 86, 1), (98, 104),
                           (84, 100), (80, 80), (20, 80), (16, 100)]), 'mid')

# Gyan Cinquedea (con su modelo 3D): el pelo nace alto y redondeado (no en una raya recta como el ala de un sombrero) y los
# abanicos de puntas de los lados salen a la altura de las orejas
c = _fx('gyan-cinquedea')
c['front'][0] = L(outline([(18, 80), (0, 88, 1), (8, 72), (-6, 64, 1), (10, 58), (12, 40), (14, 24), (30, 8), (50, 2), (70, 8), (86, 24), (88, 40), (90, 58),
                           (106, 64, 1), (92, 72), (100, 88, 1), (82, 80), (82, 56), (74, 42), (50, 34), (26, 42), (18, 56)]), 'mid')
c['front'][1] = L(outline([(60, 4), (80, 14), (88, 36), (92, 60), (102, 66), (90, 74), (84, 56), (78, 40)]), 'shade', 'b', False)

# Biffy Sausse: las dos coletas son trenzas largas que le caen hasta el pecho (no dos tacos)
c = _fx('biffy-sausse')
for v in ('front', 'back'):
    _drop(c, v, lambda l: l['c'] == 'mid' and _bbox(l)[1] >= 84 and (_bbox(l)[0] < 10 or _bbox(l)[2] > 90))
    br = []
    for s in (1, -1):
        for i, (x, y) in enumerate([(12, 92), (11, 102), (10, 112), (9, 122), (8, 131)]):
            xx = x if s == 1 else 100 - x
            r = 6.4 - i * 0.5
            br.append(L(ell(xx, y, r, r * 0.95), 'mid', 'b'))
            br.append(L(quad((xx - r * 0.7, y - 1), (xx, y + r * 0.5), (xx + r * 0.7, y - 1)), 'shade', 'b', False, False, 1.2))
    c[v][:0] = br

# Mag Nessium: los cuernos de los lados son cuernos de verdad (marrón oscuro, curvados hacia fuera y con la punta arriba),
# no dos mechones de pelo
c = _fx('mag-nessium')
HN = hexc('#3a2a20')
hrn = [(24, 32), (8, 26), (-6, 24), (-16, 14), (-16, -2, 1), (-8, 12), (4, 14), (26, 20)]
for v in ('front', 'back'):
    _drop(c, v, lambda l: l['c'] == 'mid' and _bbox(l)[0] < 0)
    c[v] += [L(outline(hrn), HN, 'b'), L(outline(_mir(hrn)), HN, 'b')]
_drop(c, 'side', lambda l: l['c'] == 'mid' and _bbox(l)[0] > 15 and _bbox(l)[2] < 45)
c['side'] += [L(outline([(42, 26), (30, 18), (20, 10), (16, -6, 1), (24, 8), (36, 14), (46, 18)]), HN, 'b')]

# Norritz Ranhatch: los cuernos plateados son gruesos: bajan desde lo alto por el borde de dentro de los ojos morados
# hasta juntarse en la nariz
c = _fx('norritz-ranhatch')
for v in ('front', 'back', 'side'):
    _drop(c, v, lambda l: l['w'] > 0 and _bbox(l)[1] < 0)
SV = hexc('#d4d8de')
band = [(24, -14, 1), (32, 0), (40, 22), (46, 42), (50, 64, 1), (42, 46), (34, 26), (26, 4)]
c['front'] += [L(outline(band), SV, 'f', False, True), L(outline(_mir(band)), SV, 'f', False, True)]
c['back'] += [L(outline([(26, 10), (24, -14, 1), (34, 8)]), SV, 'f', False, True), L(outline(_mir([(26, 10), (24, -14, 1), (34, 8)])), SV, 'f', False, True)]
c['side'] += [L(outline([(60, 8), (62, -16, 1), (72, 6), (86, 40), (92, 60, 1), (80, 40)]), SV, 'f', False, True)]

# Shiro Hatch: las nubes de pelo rizado de los lados son anchas y esponjosas, a la altura del cuello
c = _fx('shiro-hatch')
cloud = [(20, 90), (14, 78), (2, 80), (-6, 74), (-16, 84), (-24, 82), (-22, 94), (-28, 102), (-16, 106), (-8, 112), (6, 106), (18, 104)]
_drop(c, 'front', lambda l: l['c'] == 'mid' and _bbox(l)[1] > 70)
c['front'] += [L(blob(cloud, 4), 'mid', 'b'), L(blob(_mir(cloud), 4), 'mid', 'b')]

# Anthocia Arnin: el mechón en forma de gota que le cae en medio de la frente
c = CHARS[K + 'anthocia-arnin']
c['front'] += [L(blob([(50, 30), (57, 42), (55, 54), (50, 60), (45, 54), (43, 42)], 6), 'mid', 'f', True, True),
               L(blob([(50, 40), (53, 47), (50, 53), (47, 47)], 4), 'shade', 'f', False)]

# Ares Zumish: la sombra negra de la visera le tapa toda la franja de los ojos (en uve sobre la nariz) y le caen dos
# mechones largos azul marino por delante de los hombros
c = _fx('ares-zumish')
_drop(c, 'front', lambda l: l['c'] == 'shadow')
c['front'] += [L(outline([(24, 72), (76, 72), (74, 82), (58, 84), (50, 89, 1), (42, 84), (26, 82)]), 'shadow', 'f', False)]
c['front'] += [L(outline([(4, 84), (16, 92), (20, 106), (14, 120, 1), (6, 104)]), 'helm', 'f', True, True),
               L(outline([(96, 84), (84, 92), (80, 106), (86, 120, 1), (94, 104)]), 'helm', 'f', True, True)]

# Amon Boaker: las dos antenas negras cruzan por delante del casco en aspa y bajan hasta los ojos
c = _fx('amon-boaker')
for s in (1, -1):
    pts = [(4, -34, 1), (14, -22), (30, 10), (44, 48), (46, 62, 1), (38, 46), (22, 14), (8, -18)]
    c['front'].append(L(outline(pts if s == 1 else _mir(pts)), 'ant', 'f', False, True))

# Mr. Shipwood (con su modelo 3D): las gafas azules de montura rectangular ya coincidían; el pelo es castaño grisáceo
# claro (#a2917a iluminado, #715d4e en sombra) y la piel crema clara, medidos en el modelo
c = _fx('mr-shipwood')
c['pal']['mid'], c['pal']['shade'], c['pal']['deep'] = hexc('#a2917a'), hexc('#857360'), hexc('#715d4e')
c['pal']['light'] = mix(c['pal']['mid'], (255, 255, 255), 0.38)
_recolor(c, 'skin', '#fbe4b4', ('skin_d', 'nose'))
