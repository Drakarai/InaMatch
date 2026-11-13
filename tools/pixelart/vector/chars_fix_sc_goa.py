"""Correcciones de la revisión de diseños (grupo sc_goa): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda.

Ojeadores de GO (scouts-go) del grupo: referencia = su retrato de Victory Road (solo unos pocos tienen modelo 3D)."""
import copy  # noqa: F401
from chars import CHARS  # noqa: F401
from heads import L, blob, ell, quad, lerp, strand, mirror  # noqa: F401

K = 'scouts-go:'
OUTC = (60, 24, 16, 255)
WHITE = (248, 248, 248, 255)
INK = (30, 26, 30, 255)


def hx(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5)) + (255,)


def _tone(c, f):
    return tuple(max(0, min(255, int(v * f))) for v in c[:3]) + (255,)


def _mix(c, d, t):
    return tuple(int(c[i] + (d[i] - c[i]) * t) for i in range(3)) + (255,)


def _fx(pid):
    """Copia del dibujo actual del ojeador para corregirla (con su misma clave), con las capas en una lista plana."""
    c = copy.deepcopy(CHARS[K + pid])
    for v in ('front', 'side', 'back'):
        c[v] = [x for it in c[v] for x in (it if isinstance(it, list) else [it])]
    CHARS[K + pid] = c
    return c


def _hair(c, mid, shade=None, deep=None, light=None):
    """Color del pelo medido en el retrato (y sus sombras)."""
    h = hx(mid)
    p = c['pal']
    p['mid'] = h
    p['shade'] = hx(shade) if shade else _tone(h, 0.78)
    p['deep'] = hx(deep) if deep else _tone(h, 0.6)
    p['light'] = hx(light) if light else _mix(h, (255, 255, 255), 0.38)


def _ring(cx, cy, rx, ry, c, w=2.0, z='f'):
    e = ell(cx, cy, rx, ry)
    return L(e + [e[0]], c, z, False, False, w)


def _spiral(cx, cy, r, turns=1.6, c=OUTC, w=1.2, z='f', sgn=1):
    import math
    n = int(24 * turns)
    pts = [(cx + sgn * r * (i / n) * math.cos(2 * math.pi * turns * i / n), cy + r * (i / n) * math.sin(2 * math.pi * turns * i / n)) for i in range(n + 1)]
    return L(pts, c, z, False, False, w)


def _drop(cx, cy, r, c, z='f'):
    """Gota con la punta hacia arriba."""
    return L(quad((cx, cy - r * 2.2), (cx + r * 1.6, cy + r * 0.2), (cx, cy + r)) + quad((cx, cy + r), (cx - r * 1.6, cy + r * 0.2), (cx, cy - r * 2.2))[1:],
             c, z, False, True)


# ------------------------------------------------------------------ Aymer Loozit: nariz grande rojiza, la espiral de la
# barbilla grande y los ojos hundidos en un cerco oliva oscuro
_c = _fx('aymer-loozit')
_c['pal']['nose'] = hx('#b4513c')
_c['face']['nose'] = (50, 85, 6.5)
_c['front'] = [l for l in _c['front'] if not (l['w'] and l['s'][0][1] > 99)]
_c['front'] += [strand(quad((27, 79), (36, 86), (45, 79)), hx('#5a5a2a'), 'f', 2.2), strand(quad((55, 79), (64, 86), (73, 79)), hx('#5a5a2a'), 'f', 2.2),
                _spiral(50, 103, 6, 1.7, OUTC, 1.4)]

# ------------------------------------------------------------------ Toasty Tryadd: el tupé baja hasta la frente y acaba
# en un rizo que cae sobre ella
_c = _fx('toasty-tryadd')
_c['front'].insert(2, L(blob([(40, 30), (50, 24), (61, 30), (60, 40), (54, 47), (47, 44), (42, 38)], 6), 'mid', 'f', False, True))
_c['front'].append(strand([(50, 28), (56, 36), (54, 44), (49, 44), (48, 39), (52, 38)], 'deep', 'f', 1.6))
_c['face']['hairline'] = False

# ------------------------------------------------------------------ Rayne Shawa: la marca de la frente son tres gotas
# azules (la del centro mayor)
_c = _fx('rayne-shawa')
_c['front'] += [_drop(50, 61, 2.6, hx('#2e6aa0')), _drop(43, 63, 1.8, hx('#2e6aa0')), _drop(57, 63, 1.8, hx('#2e6aa0'))]

# ------------------------------------------------------------------ Amelio "Amethyst" Thyst: rizos negros pintados que
# bajan de las sienes y se enroscan junto a los ojos
_c = _fx('amelio-amethyst-thyst')
for _s in (1, -1):
    _x = 50 - 26 * _s
    _c['front'].append(strand([(_x, 54), (_x - 2 * _s, 62), (_x + 1 * _s, 69), (_x + 5 * _s, 68), (_x + 5 * _s, 64), (_x + 2 * _s, 64)],
                              hx('#24161e'), 'f', 1.8))
_c['side'].append(strand([(56, 52), (54, 60), (57, 67), (61, 66), (61, 62), (58, 62)], hx('#24161e'), 'f', 1.8))

# ------------------------------------------------------------------ Andy Kareem: ojos grandes de iris turquesa con
# pestañas gruesas (no puntitos) y ceño
_c = _fx('andy-kareem')
_c['face'].update(eyes='normal', brows='angry')
_c['pal']['iris'] = hx('#2f8a8c')
_c['front'] = [l for l in _c['front'] if not (l['w'] and l['s'][0][1] < 80)]

# ------------------------------------------------------------------ Hulk Flounder: las franjas rubias de los lados de
# la cabeza rapada son anchas y con el borde pardo; nariz grande parda, labios morados abiertos y la baba
_c = _fx('hulk-flounder')
_c['pal']['nose'] = hx('#9c6a58')
_c['face'].update(nose=(50, 85, 5.5), mouth='none')
for _v in ('front', 'back'):
    _c[_v] = [l for l in _c[_v] if not (l['c'] == 'mid' and l['w'])]
    for _s in (1, -1):
        _p = [(50 - 18 * _s, 12), (50 - 30 * _s, 22), (50 - 35 * _s, 40)]
        _c[_v] += [strand(_p, hx('#8a6a3a'), 'f', 11), strand(_p, 'mid', 'f', 7)]
_c['side'] = [l for l in _c['side'] if not (l['c'] == 'mid' and l['w'])]
_c['side'] += [strand([(52, 8), (34, 16), (22, 40)], hx('#8a6a3a'), 'f', 11), strand([(52, 8), (34, 16), (22, 40)], 'mid', 'f', 7)]
_i = next(n for n, l in enumerate(_c['front']) if l['c'] == (138, 176, 216, 255))
_c['front'][_i:_i] = [L(blob([(42, 95), (50, 92), (58, 95), (57, 101), (50, 104), (43, 101)], 5), hx('#9a7a98'), 'f', False, True),
                      L(blob([(45, 97), (50, 96), (55, 97), (54, 99.5), (50, 100.5), (46, 99.5)], 4), hx('#5a3040'), 'f', False),
                      L([(46.5, 96.5), (53.5, 96.5), (53, 98), (47, 98)], WHITE, 'f', False)]

# ------------------------------------------------------------------ Graham Bock: alrededor de los ojos lleva un antifaz
# pintado de rojo relleno (no un aro), con los ojos blancos y afilados dentro
_c = _fx('graham-bock')
_c['front'] = [l for l in _c['front'] if not (l['c'] == (200, 32, 42, 255) and l['s'][0][1] < 90)]
_c['face'].update(brows=False, mouth='none')
_c['front'] = [l for l in _c['front'] if not (l['c'] == (200, 32, 42, 255) and l['w'])]
_c['front'] += [L(quad((36, 96), (50, 100), (64, 96)) + quad((64, 96), (50, 110), (36, 96))[1:], hx('#c8202a'), 'f', False, True),
                L(quad((44, 101), (50, 99), (56, 101)) + quad((56, 101), (50, 106), (44, 101))[1:], hx('#e8803a'), 'f', False)]
for _s in (1, -1):
    _cx = 50 - 14 * _s
    _c['front'] += [L(blob([(_cx - 11 * _s, 70), (_cx, 68), (_cx + 9 * _s, 72), (_cx + 8 * _s, 80), (_cx, 82), (_cx - 10 * _s, 78)], 5), hx('#c8202a'), 'f', False, True),
                    L([(_cx - 8 * _s, 73), (_cx + 6 * _s, 75), (_cx + 4 * _s, 79), (_cx - 6 * _s, 78)], WHITE, 'f', False),
                    L(ell(_cx + 1 * _s, 76.5, 2.2, 2.4), INK, 'f', False),
                    strand([(_cx - 10 * _s, 66), (_cx - 2 * _s, 62), (_cx + 8 * _s, 68)], INK, 'f', 2.6)]
_c['side'] = [l for l in _c['side'] if not (l['c'] == (200, 32, 42, 255) and l['s'][0][1] < 90)]
_c['side'] += [L(blob([(72, 70), (84, 69), (88, 76), (84, 81), (73, 80)], 5), hx('#c8202a'), 'f', False, True),
               strand([(70, 63), (78, 61), (85, 66)], INK, 'f', 2.6)]

# ------------------------------------------------------------------ Ivor "Colonel" Kernel: el flequillo verde azulado
# oscuro le tapa entero el ojo izquierdo (de la imagen) hasta la mejilla; solo se ve el otro, redondo
_c = _fx('ivor-colonel-kernel')
_c['front'][1] = L(blob([(16, 54), (34, 52), (52, 56), (54, 66), (48, 78), (40, 90), (36, 80), (28, 88), (24, 76), (16, 80), (14, 66)], 6), 'mid', 'f', True, False)

# ------------------------------------------------------------------ Mick Sologee: mechones rosados entre el pelo crema,
# que caen por el flequillo y los lados
_c = _fx('mick-sologee')
_c['front'].insert(2, L([(18, 48), (82, 48), (84, 62), (77, 57), (71, 67), (63, 57), (55, 65), (48, 55), (41, 66), (35, 56), (27, 65), (21, 57)], 'mid', 'f', False))
_c['front'] += [strand([(30, 36), (28, 52), (26, 62)], 'tip', 'f', 1.6), strand([(66, 34), (70, 50), (71, 64)], 'tip', 'f', 1.6),
                strand([(46, 40), (42, 52), (41, 63)], 'tip', 'f', 1.2)]
_c['side'].append(strand([(40, 30), (44, 50), (48, 66)], 'tip', 'f', 1.6))

# ------------------------------------------------------------------ Xanthe Crosse: los moños de arriba son lazadas
# alargadas que salen en V hacia fuera (no bolas redondas), las de abajo cuelgan alargadas junto a la mandíbula, y la
# frente acaba en arco puntiagudo (raya en medio), no en pico de pelo hacia abajo
import math as _m


def _rot(pts, cx, cy, a):
    ca, sa = _m.cos(a), _m.sin(a)
    return [(cx + (x - cx) * ca - (y - cy) * sa, cy + (x - cx) * sa + (y - cy) * ca) for x, y in pts]


_c = _fx('xanthe-crosse')
_top = lambda cx, a: L(_rot(ell(cx, -6, 8, 17), cx, 8, a), 'mid', 'b', True, True)
_low = lambda cx, a: L(_rot(ell(cx, 94, 6.5, 10), cx, 86, a), 'mid', 'b', True, True)
_c['front'][2], _c['front'][3] = _top(24, -0.55), _top(76, 0.55)
_c['front'][4], _c['front'][5] = _low(15, 0.45), _low(85, -0.45)
_c['back'][2], _c['back'][3] = _top(24, -0.55), _top(76, 0.55)
_c['back'][4], _c['back'][5] = _low(16, 0.45), _low(84, -0.45)
_c['back'][4]['z'] = _c['back'][5]['z'] = 'f'
_c['side'][2] = L(_rot(ell(38, -6, 8, 17), 38, 8, -0.3), 'mid', 'b', True, True)
_c['side'][3] = L(_rot(ell(30, 94, 6.5, 10), 30, 86, 0.3), 'mid', 'b', True, True)
_c['face']['hairline'] = [(19.55, 104), (18, 62), (28, 54), (40, 48), (50, 42), (60, 48), (72, 54), (82, 62), (80.45, 104)]

# ------------------------------------------------------------------ Bluster Tryadd: el pelo celeste cubre toda la parte
# de arriba de la cabeza (no era una cinta sobre la calva), con un rizo en el centro de la frente
_c = _fx('bluster-tryadd')
_c['front'][2] = L(blob([(13, 52), (14, 30), (28, 12), (50, 5), (72, 12), (86, 30), (87, 52), (76, 44), (62, 42), (55, 48), (48, 40), (36, 42), (24, 46)], 6),
                   'mid', 'f', True, True)
_c['front'].insert(3, strand([(50, 10), (56, 24), (54, 40), (49, 42), (48, 36), (52, 35)], 'deep', 'f', 1.4))
_c['side'][1] = L(blob([(10, 50), (8, 28), (24, 8), (52, 2), (78, 10), (88, 30), (86, 46), (70, 40), (56, 44), (40, 54), (24, 60)], 6), 'mid', 'f', True, True)
_c['back'][2] = L(blob([(10, 62), (12, 30), (28, 10), (50, 4), (72, 10), (88, 30), (90, 62), (50, 66)], 6), 'mid', 'b')
for _l in _c['front']:  # ojos verdes (no negros) bajo los párpados caídos
    if _l['c'] == (30, 26, 30, 255) and not _l['w'] and len(_l['s']) == 36:
        _l['c'] = hx('#2f8a64')

# ------------------------------------------------------------------ Jack O'Nonne: el pelo morado es un rollo ancho
# que cubre lo alto de la cabeza (no una franja estrecha), con el moño blanco encima
_c = _fx('jack-o-nonne')
_c['front'][1] = L(blob([(22, 42), (22, 22), (34, 8), (50, 4), (66, 8), (78, 22), (78, 42), (66, 38), (58, 46), (50, 50), (42, 46), (34, 38)], 6),
                   'mid', 'f', True, True)
_c['front'].insert(2, strand([(50, 8), (46, 26), (48, 44)], 'shade', 'f', 1.2))
_c['side'][1] = L(blob([(12, 50), (10, 24), (26, 6), (50, 0), (66, 8), (64, 26), (54, 40), (36, 50)], 6), 'mid', 'f', True, True)
_c['back'][1] = L(blob([(20, 46), (20, 20), (34, 6), (50, 3), (66, 6), (80, 20), (80, 46), (66, 54), (60, 76), (40, 76), (34, 54)], 6), 'mid', 'f', True, True)

# ------------------------------------------------------------------ Gen Tallgiant: mancha gris en lo alto del pelo negro
_c = _fx('gen-tallgiant')
_gp = L(blob([(26, 6), (38, -2), (52, 2), (54, 12), (42, 18), (28, 16)], 6), hx('#5c5c60'), 'b', False)
_c['front'].insert(2, _gp)
_c['back'].append(copy.deepcopy(_gp))
_c['side'].insert(2, L(blob([(30, 2), (44, -4), (58, 2), (54, 12), (36, 12)], 6), hx('#5c5c60'), 'b', False))

# ------------------------------------------------------------------ Sett Lightning: guiña el ojo izquierdo (de la
# imagen), apretado con arrugas; el otro rojo y furioso
_c = _fx('sett-lightning')
_c['front'] += [L(ell(36, 75, 9, 8.5), 'skin', 'f', False), strand(quad((28, 74), (36, 79), (44, 74)), INK, 'f', 2.2),
                strand([(28, 70), (24, 67)], INK, 'f', 1.2), strand([(28, 78), (24, 81)], INK, 'f', 1.2)]
# ...y labios gruesos pardos (no una boquita rosa) y los cristales de las gafas amarillentos
_c = CHARS[K + 'gen-tallgiant']
_c['face']['mouth'] = 'none'
_c['front'] += [L(ell(36, 75, 8, 5.5), hx('#e8d890'), 'f', False), L(ell(64, 75, 8, 5.5), hx('#e8d890'), 'f', False),
                L(ell(34, 74, 2.4, 2.4), INK, 'f', False), L(ell(62, 74, 2.4, 2.4), INK, 'f', False),
                L(blob([(38, 93), (50, 90), (62, 93), (60, 100), (50, 103), (40, 100)], 5), hx('#8a4a2a'), 'f', False, True),
                strand([(40, 96), (50, 97), (60, 96)], hx('#4a2414'), 'f', 1.2)]

# ------------------------------------------------------------------ Holly "Butterfly" Blue: el antifaz es negro y
# relleno, en forma de alas de mariposa que suben hacia las sienes (no unas gafas de montura), con los ojos rojos de
# pestañas largas dentro; labios morado oscuro
_c = _fx('holly-butterfly-blue')
_c['front'] = _c['front'][:2]
_c['face'].update(mouth='none', brows=False)
_c['front'].append(L(blob([(13, 64), (26, 66), (40, 68), (50, 72), (60, 68), (74, 66), (87, 64), (84, 76), (72, 86), (58, 84), (50, 80), (42, 84),
                           (28, 86), (16, 76)], 5), INK, 'f', False, True))
for _s in (1, -1):
    _cx = 50 - 14 * _s
    _c['front'] += [L([(_cx - 8 * _s, 73), (_cx + 7 * _s, 74), (_cx + 5 * _s, 80), (_cx - 6 * _s, 80)], WHITE, 'f', False),
                    L(ell(_cx + 0.5 * _s, 77, 3.2, 3.4), hx('#c02a2a'), 'f', False), L(ell(_cx + 0.5 * _s, 77, 1.4, 1.6), INK, 'f', False),
                    strand([(_cx - 9 * _s, 74), (_cx - 12 * _s, 71)], WHITE, 'f', 0.9)]
_c['front'] += [L(blob([(42, 95), (50, 93), (58, 95), (56, 99), (50, 100.5), (44, 99)], 4), hx('#5a2a4a'), 'f', False, True),
                strand([(43, 96.5), (50, 97), (57, 96.5)], WHITE, 'f', 0.8)]
_c['front'] += [strand(quad((26, 63), (34, 58), (44, 63)), hx('#f0e8e0'), 'f', 1.6), strand(quad((56, 63), (66, 58), (74, 63)), hx('#f0e8e0'), 'f', 1.6)]

# ------------------------------------------------------------------ Camille Aeon: los ojos están cerrados bajo las
# manchas amarillas (se ve la raya del párpado)
_c = _fx('camille-aeon')
_c['front'] += [strand(quad((28, 78), (35, 81), (43, 78)), hx('#3e5a30'), 'f', 1.6), strand(quad((57, 78), (65, 81), (72, 78)), hx('#3e5a30'), 'f', 1.6)]
_c['side'].append(strand(quad((79, 77), (84, 80), (90, 77)), hx('#3e5a30'), 'f', 1.6))

# ------------------------------------------------------------------ Chip Chisel: patillas rojizas largas que bajan por
# las sienes, la nariz es una cuña larga y recta (no un botón) y la boca una raya ancha torcida hacia abajo
_c = _fx('chip-chisel')
_c['face'].update(nose=None, mouth='none')
_c['front'] += [L([(16, 52), (25, 54), (24, 80), (17, 78)], 'mid', 'f', False, True), L([(84, 52), (75, 54), (76, 80), (83, 78)], 'mid', 'f', False, True),
                L([(47, 66), (53, 66), (56, 88), (50, 90), (44, 88)], hx('#a5734e'), 'f', False, True),
                strand(quad((34, 99), (50, 94), (66, 99)), OUTC, 'f', 1.6)]
_c['side'].append(L([(84, 66), (92, 86), (84, 88)], hx('#a5734e'), 'f', False, True))

# ------------------------------------------------------------------ Roland "Rodent" Dent: orejas de ardilla grandes y
# redondas que salen por arriba de los mofletes (antes quedaban tapadas por la cara) y párpados naranjas caídos
_c = _fx('roland-rodent-dent')
_c['face']['ears'] = False
_ear = lambda cx, cy: [L(ell(cx, cy, 12, 12), 'skin', 'b', True, False), L(ell(cx, cy, 6.5, 7), hx('#d98a6a'), 'b', False)]
_c['front'] = _ear(0, 44) + _ear(100, 44) + _c['front']
_c['back'] = _ear(5, 48) + _ear(95, 48) + _c['back']
_c['side'] = _c['side'] + [L(ell(40, 46, 11, 12), 'skin', 'f', True, True), L(ell(40, 46, 6, 7), hx('#d98a6a'), 'f', False)]
for _s in (1, -1):
    _cx = 50 - 14 * _s
    _c['front'].append(L(quad((_cx - 8, 75), (_cx, 63), (_cx + 8, 75)) + [(_cx + 8, 76), (_cx - 8, 76)], hx('#e8904a'), 'f', False, True))
_c['side'].append(L(quad((76, 75), (81, 64), (87, 74)) + [(87, 76), (76, 76)], hx('#e8904a'), 'f', False, True))

# ------------------------------------------------------------------ Mariposa Papillon: la sombra del pelo crema tira a
# rosa (las puntas de los lados son rosadas en el retrato)
CHARS[K + 'mariposa-papillon'] = _c = _fx('mariposa-papillon')
_c['pal']['shade'] = hx('#e0bcae')


def _ringed_eyes(c, ey=75, sep=14, iris=None, rim=INK, w=2.6, side=True, thin=False):
    """Ojos blancos y afilados con un cerco negro grueso (maquillaje), pupila pequeña del color del iris."""
    iris = iris or c['pal']['iris']
    out = []
    for s in (1, -1):
        cx = 50 - sep * s
        eye = blob([(cx - 12 * s, ey - 6), (cx - 2 * s, ey - 6.5), (cx + 10 * s, ey - 1), (cx + 8 * s, ey + 5.5), (cx - 2 * s, ey + 6), (cx - 11 * s, ey + 2)], 4)
        white = (blob([(cx - 9.5 * s, ey - 3.8), (cx - 2 * s, ey - 4.4), (cx + 7.6 * s, ey - 0.4), (cx + 6 * s, ey + 3.8), (cx - 2 * s, ey + 4.2), (cx - 8.6 * s, ey + 1.4)], 4)
                 if thin else blob([(cx - 7 * s, ey - 1.5), (cx, ey - 2.2), (cx + 6 * s, ey + 0.5), (cx + 4 * s, ey + 2.5), (cx - 6 * s, ey + 1)], 4))
        r = 3.4 if thin else 2.2
        out += [L(eye, rim, 'f', False), L(white, WHITE, 'f', False),
                L(ell(cx + 1 * s, ey + 0.3, r, r), iris, 'f', False), L(ell(cx + 1 * s, ey + 0.3, r * 0.45, r * 0.45), INK, 'f', False)]
    if c['face'].get('brows') == 'angry':  # con eyes='none' heads no dibuja las cejas: se ponen aquí
        for s in (1, -1):
            cx = 50 - sep * s
            out.append(L([(cx - 8 * s, ey - 13), (cx + 7 * s, ey - 8)], OUTC, 'f', False, False, 3.0))
    c['front'] += out
    c['face'].update(eyes='none')
    if side:
        c['side'] += [L(blob([(72, ey - 5), (87, ey - 3), (86, ey + 5.5), (74, ey + 4.5)], 4), rim, 'f', False),
                      L(blob([(77, ey - 1), (85, ey), (84, ey + 2.4), (78, ey + 1.6)], 4), WHITE, 'f', False), L(ell(82.5, ey + 0.6, 1.6, 1.6), iris, 'f', False)]


# ------------------------------------------------------------------ Devin Hornes: ojos blancos de pupila roja dentro de
# un cerco negro muy marcado, ceño en V y labios morados
_c = _fx('devin-hornes')
_ringed_eyes(_c, 76, 14)
_c['face']['mouth'] = 'none'
_c['front'] += [L(blob([(42, 97), (50, 95.5), (58, 97), (56, 100), (50, 101), (44, 100)], 4), hx('#6a5070'), 'f', False, True),
                strand([(46, 64), (48, 70)], hx('#a89478'), 'f', 1.0), strand([(54, 64), (52, 70)], hx('#a89478'), 'f', 1.0)]

# ------------------------------------------------------------------ Stanley Switch: no lleva gafas de sol; son ojos
# blancos de pupila roja dentro de un cerco negro grueso; piel más clara y patillas grises largas hasta la mandíbula
_c = _fx('stanley-switch')
_c['front'] = [l for l in _c['front'] if not (l['c'] in ((30, 26, 30, 255), (192, 32, 32, 255)) and l['s'][0][1] > 60)]
_c['side'] = [l for l in _c['side'] if not (l['c'] == (30, 26, 30, 255) and l['s'][0][1] > 60)]
_c['back'] = [l for l in _c['back'] if not (l['c'] == (30, 26, 30, 255) and l['w'])]
_c['pal'].update(skin=hx('#e8c8a0'), skin_d=hx('#c8a882'))
_ringed_eyes(_c, 75, 14, w=3)
_c['face']['mouth'] = 'none'
_c['front'] += [L(quad((34, 94), (50, 92), (66, 94)) + quad((66, 94), (50, 106), (34, 94))[1:], WHITE, 'f', False, True),
                strand([(36, 97.5), (64, 97.5)], OUTC, 'f', 0.9)]
_c['front'] += [L([(19, 50), (25, 52), (24, 90), (19, 80)], 'mid', 'f', False, True), L([(81, 50), (75, 52), (76, 90), (81, 80)], 'mid', 'f', False, True)]

# ------------------------------------------------------------------ Rex Ex-Less: la cicatriz en X es parda (no roja) y
# más grande, sobre el entrecejo y el ojo
_c = _fx('rex-ex-less')
_c['front'] = [l for l in _c['front'] if l['c'] != (138, 58, 42, 255)]
_c['front'] += [strand([(34, 58), (54, 74)], hx('#6e3418'), 'f', 2.6), strand([(54, 58), (36, 76)], hx('#6e3418'), 'f', 2.6),
                strand([(28, 78), (25, 84)], hx('#6e3418'), 'f', 1.6)]
_c['face']['mouth'] = 'smile'

# ------------------------------------------------------------------ Tom-Tom Thrasher: sombra de ojos morada alrededor
# de los ojos (antes quedaba tapada detrás de la cara) y la boca es una sonrisa ancha de labios morados con la lengua
_c = _fx('tom-tom-thrasher')
_c['front'] = [l for l in _c['front'] if l['c'] != (122, 90, 160, 255)]
_c['front'] = [l for l in _c['front'] if l['c'] not in ('lip', (220, 90, 110, 255))]
_c['front'] += [_ring(36, 75, 8.5, 7.5, hx('#7a5aa0'), 3.2), _ring(64, 75, 8.5, 7.5, hx('#7a5aa0'), 3.2),
                L(quad((32, 87), (50, 94), (68, 87)) + quad((68, 87), (50, 112), (32, 87))[1:], hx('#4a1a3a'), 'f', False, True),
                strand(quad((32, 87), (50, 94), (68, 87)), 'lip', 'f', 2.4), strand(quad((36, 92), (50, 111), (64, 92)), 'lip', 'f', 2.4),
                L(blob([(45, 95), (55, 95), (57, 104), (50, 110), (43, 104)], 4), hx('#dc5a6e'), 'f', False, True)]

# ------------------------------------------------------------------ Trappy Zeum: el pelo es un cepillo plano y estrecho
# solo en lo alto (los lados de la cabeza son piel), no un casquete entero
_c = _fx('trappy-zeum')
_c['front'][0] = L([(20, 48), (24, 24), (76, 24), (80, 48), (64, 44), (36, 44)], 'mid', 'b')
_c['front'][1] = L([(64, 25), (76, 24), (80, 48), (66, 44)], 'shade', 'b', False)
_c['face']['hairline'] = [(10.44, 104), (14, 54), (22, 48), (36, 44), (64, 44), (78, 48), (86, 54), (89.56, 104)]
_c['back'][0] = L([(20, 50), (24, 24), (76, 24), (80, 50), (50, 54)], 'mid', 'b')
_c['back'][1] = L([(64, 25), (76, 24), (80, 50), (66, 52)], 'shade', 'b', False)
_c['side'] = [L([(12, 52), (18, 22), (70, 20), (74, 42), (40, 46)], 'mid', 'b')] + _c['side'][2:]

# ------------------------------------------------------------------ Mint Royle: los ojos van dentro de una mancha roja
# (antes quedaba detrás de la cara y no se veía)
_c = _fx('mint-royle')
_c['front'] = [l for l in _c['front'] if l['c'] != (192, 40, 40, 255)]
_c['front'] += [_ring(36, 75, 8.2, 7.6, hx('#c02828'), 4.6), _ring(64, 75, 8.2, 7.6, hx('#c02828'), 4.6)]

# ------------------------------------------------------------------ Eartha Toughlove: cejas lilas gruesas y enroscadas
_c = _fx('eartha-toughlove')
_c['front'] = [l for l in _c['front'] if not (l['c'] == (106, 42, 106, 255) and l['w'])]
for _s in (1, -1):
    _cx = 50 - 14 * _s
    _c['front'] += [strand([(_cx + 6 * _s, 66), (_cx - 2 * _s, 62), (_cx - 9 * _s, 64), (_cx - 10 * _s, 69), (_cx - 6 * _s, 70)], hx('#5a2060'), 'f', 4.4),
                    strand([(_cx + 6 * _s, 66), (_cx - 2 * _s, 62), (_cx - 9 * _s, 64), (_cx - 10 * _s, 69), (_cx - 6 * _s, 70)], hx('#c8a0e0'), 'f', 2.6)]

# ------------------------------------------------------------------ Hart O'Gold: labios gruesos pardo oscuro (no rosa),
# ojos de cerco negro y la raya de la nariz
_c = _fx('hart-o-gold')
_c['face']['mouth'] = 'none'
_c['front'] += [L(quad((38, 95), (50, 89), (62, 95)) + quad((62, 95), (50, 104), (38, 95))[1:], hx('#7a4a24'), 'f', False, True),
                strand([(39, 95.5), (50, 96.5), (61, 95.5)], hx('#3c1e10'), 'f', 1.2),
                strand([(44, 62), (50, 70), (48, 84)], hx('#7a5434'), 'f', 1.4)]
_ringed_eyes(_c, 76, 14)

# ------------------------------------------------------------------ Oz Rater: ojos con cerco negro muy marcado
_c = _fx('oz-rater')
_ringed_eyes(_c, 76, 14, iris=hx('#8a4a1a'), thin=True)

# ------------------------------------------------------------------ Shortcake Holmes: el ala del sombrero-tarta es
# rosada (no blanca como la nata)
_c = _fx('shortcake-holmes')
for _v in ('front', 'side', 'back'):
    _c[_v][1]['c'] = hx('#f4d8d4')

# ------------------------------------------------------------------ Spark Volt: calvo; el pelo amarillo es solo un
# reborde estrecho en lo alto, plano con dos picos, que baja en zigzag por las sienes; cejas negras gruesas en rayo
_c = _fx('spark-volt')
_c['front'].insert(1, L([(22, 24), (34, 22), (66, 22), (78, 24), (80, 40), (74, 46), (79, 54), (72, 58), (62, 54), (38, 54), (28, 58), (21, 54),
                         (26, 46), (20, 40)], 'skin', 'f', False))
_c['front'] = [l for l in _c['front'] if not (l['c'] == (30, 26, 30, 255) and l['w'] == 3 and l['s'][0][1] < 80)]
for _s in (1, -1):
    _cx = 50 - 14 * _s
    _c['front'].append(L([(_cx - 10 * _s, 62), (_cx - 4 * _s, 66), (_cx + 2 * _s, 60), (_cx + 9 * _s, 68), (_cx + 8 * _s, 71), (_cx + 2 * _s, 65),
                          (_cx - 4 * _s, 70), (_cx - 11 * _s, 65)], INK, 'f', False))
_c['face']['mouth'] = 'none'
_c['front'] = [l for l in _c['front'] if not (l['w'] and l['s'][0][1] > 90)]
_om = [(44, 108), (41, 102), (42, 97), (46, 94), (50, 93.5), (54, 94), (58, 97), (59, 102), (56, 108)]
_c['front'] += [strand(quad((32, 92), (50, 80), (68, 92)), OUTC, 'f', 2.2), strand(_om, INK, 'f', 2.6),
                strand([(39, 108), (45, 108)], INK, 'f', 2.6), strand([(55, 108), (61, 108)], INK, 'f', 2.6)]

# ------------------------------------------------------------------ Prosper Cooka: labios gruesos grisáceos (no rosa)
_c = _fx('prosper-cooka')
_c['face']['mouth'] = 'none'
_c['front'] += [L(blob([(38, 93), (50, 89), (62, 93), (60, 98), (50, 100), (40, 98)], 5), hx('#9a7a64'), 'f', False, True),
                strand([(40, 94.5), (50, 95), (60, 94.5)], OUTC, 'f', 1.0)]

# ------------------------------------------------------------------ Oswald Bones: guiña el ojo derecho (izquierda de la
# imagen es el abierto): el otro está cerrado con pestañas y sombra gris
_c = _fx('oswald-bones')
_c['front'] += [L(ell(64, 75, 9, 7), 'skin', 'f', False), L(ell(64, 76, 8, 5), hx('#6a6a70'), 'f', False),
                strand(quad((55, 76), (64, 80), (73, 75)), INK, 'f', 2.0), strand([(73, 75), (77, 72)], INK, 'f', 1.4)]
_c = CHARS[K + 'spark-volt']  # (la espalda y el perfil también calvos, con el reborde amarillo)
_c['back'].append(L(blob([(16, 24), (50, 18), (84, 24), (86, 60), (80, 82), (50, 90), (20, 82), (14, 60)], 6), 'skin', 'f', False))
_c['side'].insert(1, L(blob([(14, 26), (50, 18), (80, 22), (84, 50), (60, 62), (30, 74), (10, 60)], 6), 'skin', 'f', False))

# ------------------------------------------------------------------ Bonza Barnett: los cuernos de pelo son celestes con
# anillos negros (no negros con la punta celeste); ojos grandes redondos de iris azul y sonrisa ancha
_c = _fx('bonza-barnett')
_c['pal']['horn'] = hx('#8ce6f0')
_bands_f = [((3, 9), (8, 20)), ((13, 16), (18, 30))]
for _v in ('front', 'back'):
    _c[_v][0]['c'] = _c[_v][1]['c'] = 'horn'
    _c[_v] = [l for l in _c[_v] if l['c'] != (160, 243, 244, 255)]
    for _a, _b in _bands_f:
        _c[_v].insert(2, L([_a, _b], 'mid', 'b', False, False, 6.0))
        _c[_v].insert(2, L([(100 - _a[0], _a[1]), (100 - _b[0], _b[1])], 'mid', 'b', False, False, 6.0))
_c['side'][0]['c'] = 'horn'
_c['side'] = [l for l in _c['side'] if l['c'] != (160, 243, 244, 255)]
_c['side'].insert(1, L([(28, -2), (24, 8)], 'mid', 'b', False, False, 6.0))
_c['side'].insert(1, L([(40, 2), (36, 15)], 'mid', 'b', False, False, 6.0))
_c['face'].update(eyes='big', mouth='none')
_c['front'].append(strand(quad((36, 90), (50, 100), (64, 90)), (130, 70, 50, 255), 'f', 1.6))

# ------------------------------------------------------------------ Robbie Tout: el casco lleva una sola franja ancha
# gris oscuro en el centro entre dos blancas (no dos negras con azul en medio)
_c = _fx('robbie-tout')
for _v in ('front', 'back'):
    _c[_v] = [l for l in _c[_v] if l['c'] != (30, 30, 34, 255)]
    _y1 = 74 if _v == 'front' else 80
    _c[_v].insert(2, L([(39, 7), (61, 7), (61, _y1), (39, _y1)], hx('#3c3c42'), 'f', False))

# ------------------------------------------------------------------ Taranis Virga: ojos grandes negros con un brillo en
# cruz blanco, marcas celestes en las mejillas y el pelo de arriba en mechones de punta revueltos (no una cúpula lisa)
_c = _fx('taranis-virga')
_c['front'] = [l for l in _c['front'] if l['c'] != WHITE]
_c['face']['eyes'] = 'none'
for _s in (1, -1):
    _cx = 50 - 14 * _s
    _c['front'] += [L(ell(_cx, 76, 5.6, 6), INK, 'f', False), L([(_cx - 3.6, 76), (_cx + 3.6, 76)], WHITE, 'f', False, False, 1.4),
                    L([(_cx, 72.4), (_cx, 79.6)], WHITE, 'f', False, False, 1.4),
                    L([(_cx - 12 * _s, 84), (_cx - 8 * _s, 80), (_cx - 6 * _s, 86), (_cx - 10 * _s, 90)], hx('#6ad0c8'), 'f', False)]
_c['side'].append(L([(70, 84), (74, 80), (76, 86), (72, 90)], hx('#6ad0c8'), 'f', False))
_tuft = L([(-2, 46), (0, 26), (-6, 10), (8, 14), (12, 0), (24, 4), (30, -12), (44, -4), (56, -14), (66, -4), (80, -10), (84, 4), (100, 2), (98, 16),
           (110, 22), (102, 34), (104, 46)], hx('#7ad8e8'), 'b')
for _v, _i in (('front', 2), ('back', 1)):
    _c[_v][_i] = copy.deepcopy(_tuft)
_c['side'][1] = L([(-6, 46), (-4, 26), (-10, 12), (6, 12), (10, -2), (26, 0), (34, -12), (48, -4), (60, -14), (70, -2), (86, -6), (88, 8), (104, 12),
                   (98, 26), (108, 36), (100, 46)], hx('#7ad8e8'), 'b')

# ------------------------------------------------------------------ Buzz O'Hare: el ojo que se ve es blanco con una
# pupila negra pequeña (no amarillento) bajo una ceja recta y gruesa
_c = _fx('buzz-o-hare')
_c['face'].update(eyes='none', brows=False)
_c['front'] += [L(blob([(56, 74), (64, 71.5), (73, 73), (72, 78), (64, 79), (57, 77.5)], 4), WHITE, 'f', False, True),
                L(ell(64, 75.5, 2.2, 2.6), INK, 'f', False), L([(55, 72.5), (73, 71)], INK, 'f', False, False, 2.4),
                L([(55, 66), (74, 63)], OUTC, 'f', False, False, 3.0)]
_c['side'] += [L(blob([(76, 74), (86, 73), (86, 78), (77, 78)], 4), WHITE, 'f', False, True), L(ell(82, 75.5, 1.8, 2.4), INK, 'f', False),
               L([(72, 66), (86, 64)], OUTC, 'f', False, False, 3.0)]

# ------------------------------------------------------------------ Trey Prongs: la pieza central gris del casco baja
# por la frente como un protector de nariz en punta, y una marca negra baja desde cada ojo por las mejillas
_c = _fx('trey-prongs')
_c['front'] = [l for l in _c['front'] if not (l['c'] == (30, 26, 30, 255) and l['z'] == 'b')]
_c['front'][3]['s'] = [(44, 2), (56, 2), (57, 58), (55, 80), (50, 88), (45, 80), (43, 58)]
_c['front'][3]['ln'] = True
for _s in (1, -1):
    _c['front'].append(L([(50 - 22 * _s, 70), (50 - 26 * _s, 74), (50 - 25 * _s, 92), (50 - 21 * _s, 82)], INK, 'f', False))
_c['side'].append(L([(70, 72), (74, 76), (72, 92), (68, 82)], INK, 'f', False))

# ------------------------------------------------------------------ Douglas "Dogfish" Fische: el antifaz negro es una
# uña ancha que cae en punta hasta la nariz (no una banda recta) y una cicatriz naranja junto al ojo derecho de la imagen
_c = _fx('douglas-dogfish-fische')
_c['front'][4]['s'] = blob([(15, 70), (30, 70), (42, 74), (50, 76), (58, 74), (70, 70), (85, 70), (80, 80), (64, 82), (54, 86), (50, 92), (46, 86),
                            (36, 82), (20, 80)], 5)
_c['front'] = [l for l in _c['front'] if not (l['c'] == (232, 144, 42, 255))]
_c['front'] += [strand([(78, 62), (74, 72)], hx('#e8902a'), 'f', 2.0), strand([(72, 82), (68, 92)], hx('#e8902a'), 'f', 2.0),
                strand([(40, 62), (46, 74)], hx('#8a6048'), 'f', 1.2), strand([(60, 62), (54, 74)], hx('#8a6048'), 'f', 1.2)]

# ------------------------------------------------------------------ Ruff Weedon: de las sienes bajan dos mechones rosas
# gruesos hasta la mandíbula, acabados en rizo (no unas rayitas finas)
_c = _fx('ruff-weedon')
_c['front'] = [l for l in _c['front'] if l['c'] != (242, 160, 176, 255)]
for _s in (1, -1):
    _x = 50 - 31 * _s
    _p = [(_x, 50), (_x - 1 * _s, 66), (_x + 2 * _s, 82), (_x + 7 * _s, 88), (_x + 9 * _s, 82), (_x + 5 * _s, 79)]
    _c['front'] += [strand(_p, OUTC, 'f', 7.4), strand(_p, 'mid', 'f', 5.0)]
    _c['front'] += [strand([(50 - 22 * _s, 66), (50 - 12 * _s, 63), (50 - 8 * _s, 67)], WHITE, 'f', 1.4)]
_c['side'] += [strand([(56, 50), (56, 66), (60, 82), (66, 88), (68, 82), (64, 79)], OUTC, 'f', 7.4),
               strand([(56, 50), (56, 66), (60, 82), (66, 88), (68, 82), (64, 79)], 'mid', 'f', 5.0)]

# ------------------------------------------------------------------ Kyu Lightning: el tupé cae sobre la cara y le tapa
# el ojo izquierdo de la imagen... del lado derecho de la imagen, hasta la nariz; en el ojo que se ve, una marca negra en
# rayo
_c = _fx('kyu-lightning')
_c['front'][2] = L(blob([(14, 50), (24, 34), (50, 28), (76, 32), (88, 46), (86, 70), (76, 84), (62, 86), (52, 76), (48, 62), (36, 56), (22, 58)], 6),
                   'mid', 'f', True, True)
_c['front'][3] = L([(54, 52), (78, 42), (104, 34), (88, 48), (80, 66), (68, 80), (58, 72)], hx('#4a3020'), 'f', False, True)
_c['front'].append(L([(24, 66), (34, 74), (30, 78), (40, 82), (36, 84), (26, 78), (30, 76)], INK, 'f', False))

# ------------------------------------------------------------------ Gee "Geek" Kasoid: nariz grande salmón en cuña
# (no un botón) sobre un labio superior ancho y abultado del mismo tono
_c = _fx('gee-geek-kasoid')
_c['face'].update(nose=None, mouth='none')
_c['front'] += [L(blob([(30, 90), (40, 84), (60, 84), (70, 90), (66, 98), (50, 100), (34, 98)], 5), hx('#f0a088'), 'f', False, True),
                L(blob([(44, 70), (56, 70), (60, 86), (50, 90), (40, 86)], 5), hx('#d47868'), 'f', False, True),
                strand(quad((36, 98), (50, 101), (64, 98)), OUTC, 'f', 1.2)]
_c['face']['eyes'] = 'none'
for _s in (1, -1):  # ojos de párpado caído bajo las gafas
    _cx = 50 - 14 * _s
    _c['front'] += [L(blob([(_cx - 6, 66), (_cx, 64), (_cx + 6, 66), (_cx + 5, 70), (_cx, 71), (_cx - 5, 70)], 4), WHITE, 'f', False),
                    L(ell(_cx, 68.5, 2.2, 2.2), INK, 'f', False), L(quad((_cx - 7, 67), (_cx, 63), (_cx + 7, 67)), INK, 'f', False, False, 2.0)]

# ------------------------------------------------------------------ Adi "Gecko" Sivfeet: lo alto de la cabeza es pelo
# verde con una diadema amarilla en arco por encima (no una franja verde sobre la frente), mechones verdes que se
# enroscan junto a las mejillas y la boca ancha enseñando los dientes
_c = _fx('adi-gecko-sivfeet')
_c['front'][1] = L(quad((14, 40), (50, 2), (86, 40)) + quad((80, 44), (50, 12), (20, 44)), hx('#dac63b'), 'f', True, True)
_c['front'].insert(1, L(blob([(10, 50), (14, 30), (30, 18), (50, 14), (70, 18), (86, 30), (90, 50), (74, 44), (60, 50), (50, 44), (40, 50), (26, 44)], 6),
                        'mid', 'f', True, True))
_c['front'] = [l for l in _c['front'] if not (l['c'] == (148, 175, 116, 255) and l['w'])]
for _s in (1, -1):
    _p = [(50 - 34 * _s, 60), (50 - 36 * _s, 72), (50 - 30 * _s, 78), (50 - 27 * _s, 72), (50 - 30 * _s, 70)]
    _c['front'] += [strand(_p, OUTC, 'f', 5.0), strand(_p, 'mid', 'f', 3.0)]
_c['face']['mouth'] = 'none'
_c['front'] = [l for l in _c['front'] if not (l['w'] and l['s'][0][1] > 90)]
_c['front'] += [L(quad((32, 93), (50, 98), (68, 93)) + quad((68, 93), (50, 102), (32, 93))[1:], WHITE, 'f', False, True)]
_c['side'][1] = L(quad((14, 36), (50, 0), (86, 30)) + quad((82, 36), (50, 10), (20, 42)), hx('#dac63b'), 'f', True, True)
_c['side'].insert(1, L(blob([(8, 50), (12, 28), (30, 14), (56, 10), (78, 18), (88, 34), (70, 34), (50, 40), (30, 52)], 6), 'mid', 'f', True, True))
_c['back'][1] = L(quad((14, 40), (50, 2), (86, 40)) + quad((80, 44), (50, 12), (20, 44)), hx('#dac63b'), 'f', True, True)
_c['back'].insert(1, L(blob([(8, 60), (12, 30), (30, 16), (50, 12), (70, 16), (88, 30), (92, 60), (72, 70), (50, 74), (28, 70)], 6), 'mid', 'f', True, True))

# ------------------------------------------------------------------ Carny Voris: barbita parda en punta bajo el hueso
_c = _fx('carny-voris')
_c['front'].append(L(blob([(42, 104), (50, 103), (58, 104), (55, 109), (50, 112), (45, 109)], 5), 'mid', 'f', False, True))

# ------------------------------------------------------------------ Tuff Weedon: como su hermano Ruff, de las sienes
# le bajan mechones verdes gruesos hasta la mandíbula, acabados en rizo
_c = _fx('tuff-weedon')
_c['front'] = [l for l in _c['front'] if not (l['c'] == 'mid' and l['w'])]
for _s in (1, -1):
    _x = 50 - 31 * _s
    _p = [(_x, 50), (_x - 1 * _s, 66), (_x + 1 * _s, 82), (_x + 6 * _s, 88), (_x + 8 * _s, 82), (_x + 4 * _s, 79)]
    _c['front'] += [strand(_p, OUTC, 'f', 7.4), strand(_p, 'mid', 'f', 5.0)]
_c['side'] += [strand([(56, 50), (56, 66), (60, 82), (66, 88), (68, 82), (64, 79)], OUTC, 'f', 7.4),
               strand([(56, 50), (56, 66), (60, 82), (66, 88), (68, 82), (64, 79)], 'mid', 'f', 5.0)]

# ------------------------------------------------------------------ Wally Ramm: los cuernos de carnero son claros (beis
# grisáceo, como la lana) con la espiral marcada en pardo, no pardos enteros
_c = _fx('wally-ramm')
for _v in ('front', 'side', 'back'):
    for _l in _c[_v]:
        if _l['c'] == (160, 136, 120, 255):
            _l['c'] = hx('#c4ad94')
        elif _l['c'] == (127, 106, 94, 255):
            _l['c'] = hx('#8a6a5a')
            _l['w'] = 2.4

# ------------------------------------------------------------------ Shaun Asparr: maquillaje kabuki de trazos rojos
# gruesos que suben desde las cejas hacia las sienes; la boca es un arco ancho hacia abajo con la lengua roja en pico
_c = _fx('shaun-asparr')
_c['front'] = [l for l in _c['front'] if not (l['c'] == (200, 40, 30, 255) and (l['w'] == 2.2 or not l['w']))]
for _s in (1, -1):
    _c['front'] += [L([(50 - 6 * _s, 70), (50 - 20 * _s, 62), (50 - 32 * _s, 58), (50 - 30 * _s, 62), (50 - 20 * _s, 67), (50 - 7 * _s, 73)], hx('#c8281e'), 'f', False)]
_c['face']['mouth'] = 'none'
_c['front'] += [strand(quad((38, 100), (50, 88), (62, 100)), OUTC, 'f', 1.6), L(ell(38, 100.5, 1.3, 1.3), OUTC, 'f', False), L(ell(62, 100.5, 1.3, 1.3), OUTC, 'f', False),
                L([(45, 96), (55, 96), (50, 106)], hx('#c8281e'), 'f', False, True)]

# ------------------------------------------------------------------ Tish Badum: cejas gruesas del color del pelo en
# cuña hacia arriba y fuera, y la sonrisa ancha enseñando los dientes
_c = _fx('tish-badum')
_c['front'] = [l for l in _c['front'] if l['c'] not in ((12, 69, 78, 255), WHITE)]
for _s in (1, -1):
    _c['front'].append(L([(50 - 6 * _s, 67), (50 - 20 * _s, 60), (50 - 30 * _s, 52), (50 - 26 * _s, 62), (50 - 14 * _s, 68)], 'mid', 'f', False, True))
_c['face']['mouth'] = 'none'
_c['front'] += [L(quad((32, 90), (50, 96), (68, 90)) + quad((68, 90), (50, 106), (32, 90))[1:], WHITE, 'f', False, True),
                strand(quad((34, 92), (50, 99), (66, 92)), OUTC, 'f', 0.8)]

# ------------------------------------------------------------------ Charr Lightning: el mechón naranja en rayo baja por
# la frente hasta el entrecejo (no solo es un pincho arriba)
_c = _fx('charr-lightning')
_c['front'].insert(2, L([(52, 10), (62, 8), (54, 30), (60, 30), (46, 66), (48, 40), (42, 40)], hx('#fbb443'), 'f', False, True))
CHARS[K + 'carny-voris']['front'].append(L(blob([(42, 80), (50, 77), (58, 80), (56, 86), (50, 89), (44, 86)], 5), hx('#e07030'), 'f', False, True))

# ------------------------------------------------------------------ Sloan Steddy: el pelo es un casquete corto y bajo
# de rizos en lo alto (no un afro enorme), la cara redonda y mofletuda, ojos redondos y sonrisa ancha; tirita en cruz
_c = _fx('sloan-steddy')
_cap = L(blob([(14, 52), (14, 36), (22, 26), (30, 22), (38, 18), (46, 20), (54, 17), (62, 20), (70, 22), (78, 27), (86, 36), (86, 52), (74, 46), (50, 44),
               (26, 46)], 4), 'mid', 'b')
_c['front'][0] = _cap
_c['front'][1] = L(blob([(64, 22), (78, 27), (86, 36), (86, 52), (74, 46), (66, 34)], 4), 'shade', 'b', False)
_c['back'][0] = L(blob([(14, 64), (14, 36), (24, 24), (38, 18), (50, 18), (62, 18), (76, 24), (86, 36), (86, 64), (50, 70)], 4), 'mid', 'b')
_c['back'][1] = L(blob([(64, 20), (76, 24), (86, 36), (86, 64), (68, 68), (70, 40)], 4), 'shade', 'b', False)
_c['side'][0] = L(blob([(16, 60), (10, 40), (20, 24), (40, 16), (60, 18), (76, 26), (80, 40), (60, 40), (40, 46), (30, 62)], 4), 'mid', 'b')
_c['side'][1] = L(blob([(16, 60), (10, 40), (22, 44), (30, 62)], 4), 'shade', 'b', False)
_c['face'].update(eyes='round', mouth='none', hairline=[(10.69, 104), (16, 54), (26, 48), (50, 46), (74, 48), (84, 54), (89.31, 104)])
_c['front'] += [strand(quad((34, 89), (50, 97), (66, 89)), OUTC, 'f', 1.4),
                strand([(43, 101), (57, 107)], hx('#c09050'), 'f', 0.8), strand([(43, 107), (57, 101)], hx('#c09050'), 'f', 0.8)]

# ------------------------------------------------------------------ Nick Yergrub: ojeras azuladas hundidas alrededor de
# los ojos y la boca es un arco ancho hacia abajo (de mal humor)
_c = _fx('nick-yergrub')
_c['face']['mouth'] = 'none'
_c['front'] = [l for l in _c['front'] if not (l['w'] == 1.6 and l['s'][0][1] > 90)]
_c['front'] += [strand(quad((26, 76), (36, 87), (46, 77)), hx('#5a6a8a'), 'f', 3.4), strand(quad((54, 77), (64, 87), (74, 76)), hx('#5a6a8a'), 'f', 3.4),
                strand(quad((34, 102), (50, 86), (66, 102)), OUTC, 'f', 1.8)]

# ------------------------------------------------------------------ Orson Riffe: labios pequeños verde oscuro
_c = _fx('orson-riffe')
_c['face']['mouth'] = 'none'
_c['front'].append(L(blob([(46, 95), (50, 94), (54, 95), (53, 97.5), (50, 98.5), (47, 97.5)], 4), hx('#2f5a56'), 'f', False))

# ------------------------------------------------------------------ Apnus Braithwaite: el pelo le tapa la frente hasta
# casi los ojos (flequillo recto bajo) y los labios gruesos son pardos, no rosas
_c = _fx('apnus-braithwaite')
_c['front'].insert(2, L(blob([(12, 66), (13, 40), (30, 30), (50, 28), (70, 30), (87, 40), (88, 66), (76, 62), (50, 62), (24, 62)], 6), 'mid', 'f', False))
_c['face']['mouth'] = 'none'
_c['front'] += [L(blob([(40, 94), (50, 91), (60, 94), (58, 99), (50, 101), (42, 99)], 5), hx('#7a4a2a'), 'f', False, True),
                strand([(42, 95.5), (50, 96), (58, 95.5)], OUTC, 'f', 1.0)]

# ------------------------------------------------------------------ Rhonda House: la cinta crema va por encima de la
# frente (se ve entera, en arco), no escondida detrás de la cara
_c = _fx('rhonda-house')
_c['front'][2] = L(quad((14, 54), (50, 30), (86, 54)) + quad((86, 62), (50, 40), (14, 62)), hx('#e8dcc0'), 'f', True, True)
_c['face']['hairline'] = [(19.55, 104), (16, 60), (30, 52), (50, 48), (70, 52), (84, 60), (80.45, 104)]

# ------------------------------------------------------------------ Orel Knighter: ojos pequeños redondos de pupila
# negra con cerco (no puntitos) y arrugas de preocupación en la frente
_c = _fx('orel-knighter')
_c['face']['eyes'] = 'round'
_c['front'] += [strand(quad((40, 62), (50, 58), (60, 62)), hx('#a89478'), 'f', 1.0), strand(quad((42, 66), (50, 63), (58, 66)), hx('#a89478'), 'f', 1.0)]

# ------------------------------------------------------------------ Sunny Fairweather: los dos mechones largos de las
# sienes acaban enroscándose hacia fuera
_c = _fx('sunny-fairweather')
for _s in (1, -1):
    _p = [(50 - 40 * _s, 100), (50 - 44 * _s, 106), (50 - 49 * _s, 105), (50 - 49 * _s, 101)]
    _c['front'] += [strand(_p, OUTC, 'f', 7.0), strand(_p, 'mid', 'f', 4.6)]
    _c['back'] += [strand(_p, OUTC, 'b', 7.0), strand(_p, 'mid', 'b', 4.6)]
_c['side'] += [strand([(60, 100), (56, 106), (51, 105), (51, 101)], OUTC, 'f', 7.0),
               strand([(60, 100), (56, 106), (51, 105), (51, 101)], 'mid', 'f', 4.6)]

# ------------------------------------------------------------------ Rocky McCanns: ojos blancos grandes con cerco negro
# grueso y pupila pequeña (no ojitos redondos)
_c = _fx('rocky-mccanns')
_c['face']['eyes'] = 'none'
for _s in (1, -1):
    _cx = 50 - 14 * _s
    _e = blob([(_cx - 9 * _s, 72), (_cx, 71), (_cx + 8 * _s, 75), (_cx + 7 * _s, 82), (_cx - 1 * _s, 84), (_cx - 8 * _s, 80)], 5)
    _c['front'] += [L(_e, WHITE, 'f', False), L(_e + [_e[0]], INK, 'f', False, False, 2.6), L(ell(_cx + 1.5 * _s, 77.5, 2.6, 3), INK, 'f', False),
                    L([(_cx - 9 * _s, 62), (_cx + 7 * _s, 68)], OUTC, 'f', False, False, 3.0)]
_c['side'] += [L(blob([(76, 72), (86, 73), (86, 82), (77, 81)], 4), WHITE, 'f', False, True), L(ell(83, 77.5, 2, 3), INK, 'f', False),
               L([(70, 63), (85, 67)], OUTC, 'f', False, False, 3.0)]

# ------------------------------------------------------------------ Freddie Aster Stayre: el sombrero blanco lleva el
# borde del ala rosado también por detrás y de perfil
_c = _fx('freddie-aster-stayre')
_c['side'].append(L([(4, 43), (101, 42), (100, 45), (6, 46)], hx('#c8a8b0'), 'f', False))
_c['back'].append(L([(4, 44), (96, 44), (96, 50), (4, 50)], hx('#c8a8b0'), 'f', False))

# ------------------------------------------------------------------ Beatrix "Bee" Hunny: entre el gorro y las gafas
# asoma una franja naranja
_c = _fx('beatrix-bee-hunny')
_c['front'].insert(5, L([(4, 58), (96, 58), (96, 66), (4, 66)], hx('#f0a020'), 'f', False))

# ------------------------------------------------------------------ Falco Peregrine: el flequillo largo cae sobre el ojo
# derecho de la imagen y el ojo que se ve (el izquierdo de la imagen) lleva el cerco amarillo; estaba al revés
_c = _fx('falco-peregrine')
for _i in (4, 5):
    _c['front'][_i]['s'] = mirror(_c['front'][_i]['s'])
_c['face']['hairline'] = [(21.53, 104), (20, 54), (40, 44), (60, 40), (80, 48), (78.47, 104)]

# ------------------------------------------------------------------ Sylvester Tung: un aro pardo grueso alrededor del
# ojo izquierdo (de la imagen) y la cinta verde agua más ancha, que se ve entre las rastas
_c = _fx('sylvester-tung')
_c['front'] = [l for l in _c['front'] if not (l['c'] == (154, 216, 200, 255))]
_c['front'].insert(1, L([(12, 44), (62, 44), (62, 56), (12, 56)], hx('#9ad8c8'), 'f', False, True))
_c['front'].append(_ring(36, 75, 6.6, 7, hx('#7a4a30'), 3.0))

# ------------------------------------------------------------------ Harriet Bunne: la flor morada del moño es grande y
# de pétalos (no un botón)
_c = _fx('harriet-bunne')
import math as _m2
_fl = []
for _k in range(8):
    _a = 2 * _m2.pi * _k / 8
    _fl.append((66 + 14 * _m2.cos(_a), 0 + 14 * _m2.sin(_a)))
    _fl.append((66 + 8 * _m2.cos(_a + _m2.pi / 8), 0 + 8 * _m2.sin(_a + _m2.pi / 8)))
for _v in ('front', 'back'):
    _c[_v] = [l for l in _c[_v] if l['c'] not in ((122, 90, 184, 255), (240, 200, 64, 255))]
    _c[_v] += [L(blob(_fl, 3), hx('#7a5ab8'), 'f', True, True), L(ell(66, 0, 3.4, 3.4), hx('#f0c840'), 'f', False)]
_c['side'] = [l for l in _c['side'] if l['c'] != (122, 90, 184, 255)]
_c['side'] += [L(ell(56, -2, 6, 10), hx('#7a5ab8'), 'f', True, True)]

# ------------------------------------------------------------------ Gonzalo Karter: el pelo verde baja en una V
# puntiaguda hasta el centro de la frente (entre las cejas)
_c = _fx('gonzalo-karter')
_c['face']['hairline'] = [(19.55, 104), (18, 52), (30, 50), (42, 56), (50, 64), (58, 56), (70, 50), (82, 52), (80.45, 104)]
_c['front'].insert(1, L([(26, 40), (74, 40), (60, 54), (50, 66), (40, 54)], 'mid', 'f', False))
_c['front'].insert(2, strand([(30, 50), (40, 55), (50, 66), (60, 55), (70, 50)], OUTC, 'f', 1.3))

# ------------------------------------------------------------------ Hippolytus "Hippo" Horseriver: la boca es un arco
# ancho hacia abajo que cruza casi toda la cara
_c = _fx('hippolytus-hippo-horseriver')
_c['face']['mouth'] = 'none'
_c['front'].append(strand(quad((33, 95), (50, 89), (67, 95)), OUTC, 'f', 1.8))

# ------------------------------------------------------------------ Indy Iffrent: orejas de elfo puntiagudas
_c = _fx('indy-iffrent')
_c['front'] = [L([(20, 66), (4, 54), (20, 80)], 'skin', 'b', True, False), L([(80, 66), (96, 54), (80, 80)], 'skin', 'b', True, False)] + _c['front']
_c['back'] = [L([(20, 64), (4, 52), (20, 78)], 'skin', 'b', True, False), L([(80, 64), (96, 52), (80, 78)], 'skin', 'b', True, False)] + _c['back']

# ------------------------------------------------------------------ Nai Swanson: ojos celestes dentro de un cerco
# oscuro grueso y patillas azules que bajan por las mejillas
_c = _fx('nai-swanson')
_ringed_eyes(_c, 76, 14, iris=hx('#7ab0c8'), thin=True)
_c['front'] += [L([(18, 52), (24, 52), (23, 82), (18, 74)], 'mid', 'f', False, True), L([(82, 52), (76, 52), (77, 82), (82, 74)], 'mid', 'f', False, True)]

# ------------------------------------------------------------------ Selwyn Crawler: el pañuelo verde lleva espirales
# blancas (no círculos)
_c = _fx('selwyn-crawler')
for _v in ('front', 'side', 'back'):
    _new = []
    for _l in _c[_v]:
        if _l['c'] == WHITE and _l['w']:
            _xs = [p[0] for p in _l['s']]
            _ys = [p[1] for p in _l['s']]
            _new.append(_spiral((min(_xs) + max(_xs)) / 2, (min(_ys) + max(_ys)) / 2, 11, 2.0, WHITE, 1.6))
        else:
            _new.append(_l)
    _c[_v] = _new
_c['front'].insert(1, L(blob([(8, 66), (10, 40), (50, 36), (90, 40), (92, 66), (50, 62)], 5), hx('#4a7a4a'), 'f', False))

# ------------------------------------------------------------------ Fritzy Flaps: la sombra del gorro es granate oscuro
# (era casi negra, del color del pelo)
_c = _fx('fritzy-flaps')
_c['front'][1]['c'] = hx('#6a2434')

# ------------------------------------------------------------------ Lucan Thorpe: grandes patillas pardas en punta que
# bajan desde las sienes por los lados de la cara hasta la mandíbula (de hombre lobo)
_c = _fx('lucan-thorpe')
for _s in (1, -1):
    _c['front'].append(L([(50 - 32 * _s, 50), (50 - 22 * _s, 56), (50 - 18 * _s, 84), (50 - 16 * _s, 98), (50 - 26 * _s, 88), (50 - 32 * _s, 72)], 'mid', 'f', False, True))
_c['side'].append(L([(56, 54), (66, 58), (72, 88), (68, 98), (60, 82)], 'mid', 'f', False, True))

# ------------------------------------------------------------------ Silas Andice: el ojo rojo que se ve tiene una sombra
# oscura alrededor
_c = _fx('silas-andice')
_c['front'].append(strand(quad((55, 80), (64, 86), (73, 79)), hx('#4a2a2e'), 'f', 2.4))

# ------------------------------------------------------------------ Xander Noddle: la placa metálica y la cinta de tela
# le tapan la frente (iban detrás de la cara y casi no se veían) y por los lados le cae el pelo largo oscuro
_c = _fx('xander-noddle')
for _i in (1, 2, 3, 4):
    _c['front'][_i]['z'] = 'f'
_c['front'][1]['ln'] = _c['front'][2]['ln'] = True
_c['front'].insert(0, L(blob([(6, 50), (20, 44), (24, 60), (24, 108), (10, 112), (4, 90)], 5), 'mid', 'b'))
_c['front'].insert(0, L(blob([(94, 50), (80, 44), (76, 60), (76, 108), (90, 112), (96, 90)], 5), 'mid', 'b'))

# ------------------------------------------------------------------ Othello Go: las gafas de sol van justo bajo la
# visera (no hay una segunda franja negra encima)
_c = _fx('othello-go')
_c['front'] = [l for l in _c['front'] if l['c'] != (42, 42, 46, 255)]
for _l in _c['front']:
    if _l['c'] in ((30, 30, 34, 255), (74, 74, 82, 255)):
        _l['s'] = [(x, y - 10) for x, y in _l['s']]
_c['side'] = [l for l in _c['side'] if l['c'] != (42, 42, 46, 255)]
for _l in _c['side']:
    if _l['c'] == (30, 30, 34, 255):
        _l['s'] = [(x, y - 10) for x, y in _l['s']]

# ------------------------------------------------------------------ Grandpa Danger (modelo 3D): el bigote negro es
# enorme, dos lóbulos que tapan la boca y llegan a la barbilla y a las mejillas; mofletes rojos; por detrás solo tiene
# pelo en los lados (no una franja que cruce la nuca)
_c = _fx('grandpa-danger')
_must = blob([(50, 84), (62, 81), (78, 84), (90, 94), (86, 110), (72, 114), (60, 106), (50, 98), (40, 106), (28, 114), (14, 110), (10, 94), (22, 84),
              (38, 81)], 5)
_c['front'][8] = L(_must, 'mid', 'f', True, True)
_c['front'][9]['s'] = ell(19, 80, 3.6, 2.6)
_c['front'][10]['s'] = ell(81, 80, 3.6, 2.6)
_c['side'][2] = L(blob([(70, 84), (84, 82), (96, 88), (98, 100), (90, 108), (78, 104), (68, 96)], 5), 'mid', 'f', True, True)
_c['back'] = [l for l in _c['back'] if not (l['c'] == 'mid' and min(p[0] for p in l['s']) > 10 and max(p[0] for p in l['s']) > 80 and min(p[0] for p in l['s']) < 20)]

# ------------------------------------------------------------------ Cato "Caterpillar" Pillar: el pelo que asoma bajo el
# gorro de oruga es verde muy oscuro y abultado, no negro
_c = _fx('cato-caterpillar-pillar')
_c['front'][6]['c'] = hx('#34402c')

# ------------------------------------------------------------------ Av Antguard: ojeras marcadas bajo los ojos caídos
_c = _fx('av-antguard')
_c['front'] += [strand(quad((28, 84), (36, 87), (44, 83)), hx('#8a7a70'), 'f', 1.2), strand(quad((56, 83), (64, 87), (72, 84)), hx('#8a7a70'), 'f', 1.2)]

# ------------------------------------------------------------------ Sidney Cal: el ojo que se ve (derecha de la imagen)
# es blanco con pupila, dentro de una ojera oscura redonda (no tapado por una mancha), y las rastas llevan anillas rojas
# a lo largo, no solo en las puntas
_c = _fx('sidney-cal')
_c['front'][3] = _ring(64, 77, 6.4, 6.6, hx('#5a4a3a'), 3.0)
_c['front'][3:3] = [L(ell(64, 77, 5.4, 5.2), WHITE, 'f', False), L(ell(64.5, 77.5, 2.4, 2.4), INK, 'f', False)]
_c['face']['eyes'] = 'none'
_c['front'].insert(2, L(blob([(24, 50), (40, 46), (48, 60), (46, 86), (40, 104), (30, 96), (26, 76)], 5), 'mid', 'f', False))
_c['front'].insert(3, strand([(34, 52), (36, 80), (34, 100)], 'deep', 'f', 1.2))
for _x in (6, 94):
    for _y in (78, 90):
        _c['front'] += [L([(_x - 4, _y), (_x + 4, _y - 1), (_x + 4, _y + 3), (_x - 4, _y + 4)], hx('#c84a40'), 'f', False)]
for _y in (78, 90):
    _c['front'] += [L([(32, _y + 4), (42, _y + 3), (42, _y + 7), (32, _y + 8)], hx('#c84a40'), 'f', False)]

# ------------------------------------------------------------------ Saul Hermit: boca pequeña de labios finos (sin
# dientes de conejo)
_c = _fx('saul-hermit')
_c['face']['mouth'] = 'none'
_c['front'].append(strand(quad((44, 100), (50, 102), (56, 99)), OUTC, 'f', 1.2))

# ------------------------------------------------------------------ Spacey Flipper: gafas pequeñas rectangulares y la
# boca es ancha, abierta y gris, con la forma de una judía
_c = _fx('spacey-flipper')
_c['face'].update(mouth='none', glasses=OUTC, glasses_rect=True)
_c['front'] += [L(blob([(32, 96), (42, 92), (50, 93), (58, 92), (68, 96), (66, 102), (50, 100), (34, 102)], 5), hx('#8a8a8a'), 'f', False, True)]

# ------------------------------------------------------------------ Rhys Eller: patillas azules en punta hasta la
# mandíbula y la sonrisa ancha de medio lado
_c = _fx('rhys-eller')
_c['front'] += [L([(16, 52), (24, 56), (24, 90), (18, 80), (12, 82)], 'mid', 'f', False, True), L([(84, 52), (76, 56), (76, 90), (82, 80), (88, 82)], 'mid', 'f', False, True)]
_c['face']['mouth'] = 'none'
_c['front'].append(strand(quad((38, 95), (52, 100), (64, 94)), OUTC, 'f', 1.4))

# ------------------------------------------------------------------ Captain Jokar: el casco negro lleva una raya amarilla
# en forma de Y tumbada (baja en diagonal desde arriba y se abre hacia la derecha) y una pieza amarilla en U por la
# mandíbula, no una mancha vertical
_c = _fx('captain-jokar')
_Y = hx('#ddc734')
_c['front'][3] = L([(58, 4), (70, 8), (52, 46), (40, 44)], _Y, 'f', False)
_c['front'][4:4] = [L([(46, 36), (84, 30), (88, 40), (50, 48)], _Y, 'f', False),
                    L(quad((12, 80), (50, 130), (88, 80)) + quad((80, 86), (50, 112), (20, 86)), _Y, 'f', False)]
_c['side'][2] = L([(48, 4), (60, 8), (70, 40), (92, 36), (92, 46), (62, 50)], _Y, 'f', False)
_c['side'].insert(3, L(quad((50, 88), (70, 112), (92, 86)) + quad((90, 92), (70, 102), (54, 90)), _Y, 'f', False))

# ------------------------------------------------------------------ Leafy Tryadd: lleva un casquete de pelo verde que
# cubre lo alto de la cabeza, con un rizo que cae por el centro de la frente (no la cabeza calva con hojas)
_c = _fx('leafy-tryadd')
_cap = blob([(14, 50), (14, 30), (28, 12), (50, 6), (72, 12), (86, 30), (86, 50), (74, 42), (60, 44), (54, 54), (46, 54), (42, 44), (26, 42)], 6)
_c['front'].insert(1, L(_cap, 'mid', 'f', True, True))
_c['front'].insert(2, strand([(50, 12), (46, 30), (48, 46), (54, 50), (55, 44), (51, 42)], 'deep', 'f', 1.4))
_c['back'].insert(1, L(blob([(12, 62), (14, 30), (28, 12), (50, 6), (72, 12), (86, 30), (88, 62), (50, 68)], 6), 'mid', 'f', True, True))
_c['side'].insert(1, L(blob([(8, 56), (10, 30), (26, 10), (54, 4), (78, 14), (88, 36), (76, 44), (56, 40), (36, 52), (20, 64)], 6), 'mid', 'f', True, True))
_c['face']['eyes'] = 'big'

# ------------------------------------------------------------------ Jemima "Jelly" Ellison: ojos azules (no negros)
_c = _fx('jemima-jelly-ellison')
_c['face']['eyes'] = 'normal'

# ------------------------------------------------------------------ Robin O'Cruise: las cuencas son grandes y pardas
# oscuras con un ojo blanco pequeño de pupila negra dentro; la boca, un parche ancho pardo oscuro con muescas (de
# calavera) y coloretes junto a las sienes
_c = _fx('robin-o-cruise')
_SK = hx('#4a3e34')
_c['front'] = _c['front'][:1] + [l for l in _c['front'][1:] if l['c'] == (232, 160, 144, 255)]
for _s in (1, -1):
    _cx = 50 - 16 * _s
    _c['front'] += [L(blob([(_cx - 11, 50), (_cx, 44), (_cx + 11, 50), (_cx + 10, 60), (_cx, 64), (_cx - 10, 60)], 5), _SK, 'f', False),
                    L(ell(_cx, 54, 4.6, 4.6), WHITE, 'f', False), L(ell(_cx, 54, 2, 2), INK, 'f', False),
                    L(ell(50 - 33 * _s, 60, 4, 5), hx('#c8907a'), 'f', False)]
_mp = [(34, 86), (39, 86), (39, 83), (45, 83), (45, 86), (55, 86), (55, 83), (61, 83), (61, 86), (66, 86), (66, 100), (61, 100), (61, 103),
       (55, 103), (55, 100), (45, 100), (45, 103), (39, 103), (39, 100), (34, 100)]
_c['front'] += [L(_mp, _SK, 'f', False), strand(quad((45, 94), (50, 90), (55, 94)), INK, 'f', 1.0)]
_c['side'] = [l for l in _c['side'] if not (l['c'] == INK and l['s'][0][1] > 85)]
_c['side'] += [L([(70, 90), (86, 90), (86, 106), (70, 106)], _SK, 'f', False)]
for _l in _c['side']:
    if _l['c'] == INK:
        _l['c'] = _SK

# ------------------------------------------------------------------ Jon Gleur: un mechón del pelo azul oscuro cae sobre
# el centro de la frente y la sonrisa pintada es un arco ancho de mejilla a mejilla
_c = _fx('jon-gleur')
_c['front'].insert(5, L(blob([(36, 54), (46, 46), (60, 48), (66, 56), (56, 58), (48, 62), (42, 58)], 5), 'mid', 'f', False, True))
_c['front'] = [l for l in _c['front'] if not (l['w'] == 1.4 and l['s'][0][1] > 90)]
_c['front'].insert(12, strand(quad((26, 82), (50, 102), (74, 82)), OUTC, 'f', 2.0))

# ------------------------------------------------------------------ Drakaina Eastwick: sombra de ojos morada y raya
# negra marcada
_c = _fx('drakaina-eastwick')
_c['front'] += [strand(quad((26, 68), (36, 64), (46, 69)), hx('#8a6ab0'), 'f', 2.0), strand(quad((54, 69), (64, 64), (74, 68)), hx('#8a6ab0'), 'f', 2.0)]

# ------------------------------------------------------------------ Cain Cavalier: sobre el ojo izquierdo (de la imagen)
# lleva un parche redondo malva liso (no un ojo con aro) y la chistera es gris perla
_c = _fx('cain-cavalier')
_c['front'][2]['c'] = hx('#a86a90')
_c['front'][2]['ln'] = True
del _c['front'][3:5]
for _v in ('front', 'side', 'back'):
    for _l in _c[_v]:
        if _l['c'] == WHITE:
            _l['c'] = hx('#e4e4e8')

# ------------------------------------------------------------------ Piero Mantisse: de perfil el ojo de mantis también
# lleva su pupila negra
_c = _fx('piero-mantisse')
_r = [l for l in _c['side'] if not l['w'] and l['c'] not in ('mid', 'shade', 'deep', 'light', 'skin', 'skin_d')]
if _r:
    _xs = [p[0] for p in _r[0]['s']]
    _ys = [p[1] for p in _r[0]['s']]
    _c['side'].append(L(ell((min(_xs) + max(_xs)) / 2 + 3, (min(_ys) + max(_ys)) / 2, 2.6, 3.6), INK, 'f', False))


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
    'rhiannon-hoode': '#fef1d6',
    'ivor-colonel-kernel': '#fbbc7b',
    'strata-pudden': '#fbbc7b',
    'corvus-cardson': '#bf854c',
    'camille-aeon': '#fed09e',
    'tarquin-chatty-chatstone': '#cf9669',
    'rex-ex-less': '#cf9669',
    'damo-dj-jukes': '#c0844c',
    'spark-volt': '#cf9669',
    'erwin-goel': '#fed08b',
    'robbie-tout': '#fef0d4',
    'taranis-virga': '#feeab8',
    'mia-tior': '#fecf9f',
    'gee-geek-kasoid': '#fecf9e',
    'sloan-steddy': '#eea65f',
    'raphael-allegro': '#fef1d4',
    'rocky-mccanns': '#fdcf9e',
    'beatrix-bee-hunny': '#fbd8b5',
    'celer-lightfoot': '#fbbc7b',
    'soren-uphigh': '#cf9669',
    'silas-andice': '#e4ccac',
    'gerda-dogge': '#fbbc7b',
    'mel-o-drahma': '#eea660',
    'cato-caterpillar-pillar': '#fed08a',
    'ada-vyper': '#f6bf93',
    'teo-chaspet': '#fecf95',
    'esau-tariq': '#fccda0',
    'romeo-wheedler': '#cf9669',
    'ruff-weedon': '#cf9669',
    'sunny-fairweather': '#cf9669',
    'sal-hughes': '#cf9669',
    'rhonda-house': '#bf8d69',
    'mariposa-papillon': '#fef1d4',
    'trajan-leet': '#e4ccac',
}.items():
    _skin_fix('scouts-go:' + _pid, _hx)
