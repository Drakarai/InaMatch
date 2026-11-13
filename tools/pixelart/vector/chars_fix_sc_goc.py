"""Correcciones de la revisión de diseños (grupo sc_goc): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda.

Ojeadores de GO (scouts-go) del grupo sc_goc, comparados con su retrato de Victory Road (y el modelo 3D cuando lo hay)."""
import copy
import math
from chars import CHARS, outline, hexc
from heads import L, blob, ell, quad, lerp, mirror  # noqa: F401
from chars_scouts_ie3_02 import ring
from chars_scouts_ie1_09 import face as face_shape

K = 'scouts-go:'
WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)
OUTC = (60, 24, 16, 255)


def _c(h):
    return hexc(h)


def _fx(pid):
    """Copia del dibujo actual del ojeador (capas en lista plana, para poder quitar y cambiar) con su misma clave."""
    c = copy.deepcopy(CHARS[K + pid])
    for v in ('front', 'side', 'back'):
        c[v] = [x for it in c[v] for x in (it if isinstance(it, list) else [it])]
    CHARS[K + pid] = c
    return c


def _drop(c, view, *idx):
    c[view] = [l for i, l in enumerate(c[view]) if i not in idx]


def _hair(c, mid, shade=None, deep=None, light=None):
    """Color del pelo medido en el retrato (con sus sombras)."""
    from chars import tone, mix
    h = hexc(mid)
    p = c['pal']
    p['mid'] = h
    p['shade'] = hexc(shade) if shade else tone(h, 0.78)
    p['deep'] = hexc(deep) if deep else tone(h, 0.6)
    p['light'] = hexc(light) if light else mix(h, (255, 255, 255), 0.38)


def spiral(cx, cy, r, turns=1.5, c='deep', w=1.4, z='f', a0=0.0, sy=1.0):
    """Rizo en espiral (trazo) de radio r."""
    n = 28
    pts = [(cx + r * (1 - t * 0.85) * math.cos(a0 + t * turns * 2 * math.pi), cy + r * sy * (1 - t * 0.85) * math.sin(a0 + t * turns * 2 * math.pi))
           for t in (i / n for i in range(n + 1))]
    return L(pts, c, z, False, False, w)


def lid_eye(cx, ey, rx=6.5, ry=5.5, lid=None, iris=BLACK, ri=2.2, py=1.2, z='f'):
    """Ojo de párpado caído: blanco, pupila abajo y el párpado (color lid) tapando la mitad de arriba con su raya."""
    out = [L(ell(cx, ey, rx, ry), WHITE, z, False), L(ell(cx, ey + py, ri, ri), iris, z, False)]
    if lid:
        out.append(L(quad((cx - rx - 1, ey), (cx, ey - ry * 2.6), (cx + rx + 1, ey)) + quad((cx + rx + 1, ey), (cx, ey - ry * 0.3), (cx - rx - 1, ey))[1:], lid, z, False))
    out.append(L(quad((cx - rx - 1, ey + 0.4), (cx, ey - ry * 0.25), (cx + rx + 1, ey + 0.4)), OUTC, z, False, False, 1.8))
    out.append(L(ell(cx, ey, rx, ry) + [ell(cx, ey, rx, ry)[0]], OUTC, z, False, False, 1.2))
    return out


# ================================================================== tanda 1

# Ciaran Wale: los ojos van tapados a medias por unos párpados grandes y morenos (mirada de sueño), con la pupila abajo
c = _fx('ciaran-wale')
_drop(c, 'front', 2, 3, 4, 5, 6, 7)
LID = _c('#9a6a48')
c['front'] += lid_eye(33, 75, 9.5, 7.5, LID, ri=2.6, py=3.0) + lid_eye(67, 75, 9.5, 7.5, LID, ri=2.6, py=3.0)

# Ruby Catbear: capucha de panda rojo. El rizo gordo baja por el centro de la frente, dos franjas negras curvas salen de él
# hacia las sienes, dos rizos grandes cubren las mejillas por los lados y los ojos van en manchas negras redondas (aro
# blanco e iris naranja); nariz de triángulo y boca en «w». Antes salía una caja naranja con una barra negra y rombos.
ORA, ORD = _c('#e05a1e'), _c('#b8400e')
c = _fx('ruby-catbear')
fr_ = [ring([(2, 104), (-2, 60), (8, 22), (30, 4), (50, 0), (70, 4), (92, 22), (102, 60), (98, 104), (50, 108)],
            [(20, 98), (18, 72), (24, 56), (40, 50), (50, 52), (60, 50), (76, 56), (82, 72), (80, 98), (50, 104)], ORA),
       L(ell(16, 6, 10, 9), BLACK, 'f'), L(ell(84, 6, 10, 9), BLACK, 'f'),
       L(quad((38, 32), (22, 22), (4, 40)), BLACK, 'f', False, False, 5.5), L(quad((62, 32), (78, 22), (96, 40)), BLACK, 'f', False, False, 5.5),
       L(ell(50, 40, 15, 16), ORA, 'f', False, True), spiral(50, 40, 11, 1.3, ORD, 1.6, a0=0.6),
       L(ell(12, 84, 13, 15), ORA, 'f', True, True), spiral(12, 84, 9, 1.3, ORD, 1.6, a0=3.4),
       L(ell(88, 84, 13, 15), ORA, 'f', True, True), spiral(88, 84, 9, 1.3, ORD, 1.6, a0=0.2)]
for cx in (36, 64):
    fr_ += [L(ell(cx, 74, 9, 7.5), BLACK, 'f', False), L(ell(cx, 74, 5.4, 5.4), WHITE, 'f', False), L(ell(cx, 74, 3.8, 3.8), _c('#e07a1e'), 'f', False),
            L(ell(cx, 74, 1.6, 1.6), BLACK, 'f', False)]
fr_ += [L([(47, 84), (53, 84), (50, 88)], _c('#4a2a20'), 'f', False),
        L(quad((44, 90), (47, 93), (50, 90)) + quad((50, 90), (53, 93), (56, 90))[1:], OUTC, 'f', False, False, 1.2)]
c['front'] = fr_
c['side'] = [l for l in c['side'] if l['c'] != (200, 74, 22, 255)] + [L(ell(30, 74, 14, 16), ORA, 'f', True, True), spiral(30, 74, 10, 1.3, ORD, 1.6)]
c['back'] = [l for l in c['back'] if l['c'] != (200, 74, 22, 255)] + [L(quad((30, 30), (14, 24), (0, 44)), BLACK, 'f', False, False, 5.5),
                                                                       L(quad((70, 30), (86, 24), (100, 44)), BLACK, 'f', False, False, 5.5),
                                                                       spiral(50, 56, 16, 1.4, ORD, 1.6)]

# Mirabel "Bella" Tussel: los dos ojos son iguales, rojos con el centro verde azulado (no uno de cada color)
c = _fx('mirabel-bella-tussel')
c['front'] += [L(ell(36, 76, 3.6, 4.6), _c('#2aa0a0'), 'f', False), L(ell(36, 76, 1.8, 2.4), BLACK, 'f', False)]
c['front'] += [L(ell(cx - 2, 72.5, 1.3, 1.5), WHITE, 'f', False) for cx in (36, 64)]

# Sid Steppe: lo que sale de la gorra plana sobre la frente es un rizo gris (no un aro)
c = _fx('sid-steppe')
_drop(c, 'front', 4)
c['front'].insert(4, L(outline([(22, 40), (28, 34), (38, 34), (42, 42), (38, 50), (32, 50), (34, 44), (30, 40), (26, 46)]), _c('#8a8680'), 'f', True))

# Rihanna Lin: la coleta alta ladeada es un manojo de mechones que se abre hacia arriba a la izquierda, con mechas blancas
# (antes eran dos cuernos), atada con la goma roja
c = _fx('rihanna-lin')
PT = [L(outline([(36, 8), (28, -10), (22, -30), (28, -44, 1), (32, -26), (38, -12), (42, 4)]), 'mid', 'b'),
      L(outline([(32, 8), (18, -12), (4, -22), (-10, -16), (-18, 2, 1), (-8, -6), (-12, 14, 1), (-2, 0), (2, 20, 1), (8, 2), (24, 10)]), 'mid', 'b'),
      L(outline([(-4, -14), (8, -16), (14, -8), (2, -8)]), WHITE, 'b', False), L(outline([(26, -20), (28, -38), (30, -18)]), WHITE, 'b', False),
      L(outline([(-6, 0), (0, -4), (0, 10, 1)]), WHITE, 'b', False),
      L(blob([(24, 4), (32, -2), (38, 4), (32, 10)], 4), _c('#c83a2a'), 'f', False, True)]
_drop(c, 'front', 2, 3)
c['front'][2] = L(outline([(56, 34), (72, 30), (82, 44), (80, 60, 1), (72, 44), (60, 40)]), WHITE, 'f')
c['front'] = PT + c['front'] + [L(outline([(16, 52), (24, 46), (28, 70), (22, 84, 1), (18, 66)]), WHITE, 'f')]
c['side'] = [L(outline([(40, 10), (24, -8), (6, -12, 1), (18, -18), (10, -30, 1), (26, -24), (30, -36, 1), (36, -18), (48, -26, 1), (46, -6), (50, 10)]), 'mid', 'b'),
             L(outline([(18, -16), (10, -26), (24, -20)]), WHITE, 'b', False)] + c['side'][:-2] + [L(blob([(36, 4), (46, -2), (50, 6), (42, 10)], 4), _c('#c83a2a'), 'b', True)]
c['back'] = PT + c['back'][:-2]

# Cloudy Forbes: la marca de la frente es un triángulo hacia abajo, color tostado claro (no una gota rosa)
c = _fx('cloudy-forbes')
c['front'][2] = L(outline([(44, 44, 1), (56, 44, 1), (50, 56, 1)]), _c('#c8a078'), 'f', False)

# Turco "Turquoise" Quoisey: dos bultos del gorro de seta bajan a los lados, a la altura de las orejas; lleva gafas redondas de montura blanca gruesa con cristales oscuros y puente (antes parecían
# ojos), y sonríe con la boca abierta
c = _fx('turco-turquoise-quoisey')
_drop(c, 'front', 6, 7, 8, 9, 10)
c['front'] = [L(ell(4, 60, 13, 12), 'mid', 'b'), L(ell(96, 60, 13, 12), 'shade', 'b')] + c['front']
c['back'] = [L(ell(4, 60, 13, 12), 'mid', 'b'), L(ell(96, 60, 13, 12), 'mid', 'b')] + c['back']
c['side'] = [L(ell(36, 62, 13, 12), 'mid', 'b')] + c['side']
for cx in (35, 65):
    c['front'] += [L(ell(cx, 74, 10, 9), WHITE, 'f', True, True), L(ell(cx, 74, 6.4, 5.8), _c('#3f4a4c'), 'f', False),
                   L(ell(cx - 2.4, 71.6, 1.8, 1.4), _c('#9aa4a6'), 'f', False)]
c['front'] += [L([(44, 73), (56, 73)], WHITE, 'f', False, False, 3.0), L([(48, 82), (52, 82), (50, 85)], _c('#e8b8a0'), 'f', False),
               L(quad((42, 90), (50, 89), (58, 90)) + quad((58, 90), (50, 102), (42, 90))[1:], _c('#c8384a'), 'f', False, True),
               L(ell(50, 97, 4, 2.4), _c('#f08a8a'), 'f', False)]

# Molly Gunn: boca abierta de morros (no ceño cerrado); el nacimiento del pelo sigue la masa del pelo
c = _fx('molly-gunn')
c['face']['mouth'] = 'none'
c['face']['brows'] = True
c['face']['hairline'] = [(19, 104), (18.5, 70), (19, 52), (30, 47), (50, 45), (70, 47), (81, 52), (81.5, 70), (81, 104)]
c['front'].append(L(outline([(66, 40), (80, 44), (86, 60), (82, 84), (76, 96, 1), (78, 76), (74, 58), (64, 50)]), 'mid', 'f'))
c['front'] += [L(ell(50, 95, 4.6, 3.4), _c('#c06a5a'), 'f', False, True), L(ell(50, 95.6, 2.6, 1.6), _c('#6a2a2a'), 'f', False)]

# Azrael Andrews: dos cuernos grises curvos (el izquierdo grande, hacia arriba y fuera; el derecho más corto) que salen del
# pelo; el flequillo le tapa el ojo izquierdo y la pintura roja rodea por debajo el derecho
c = _fx('azrael-andrews')
HRN = _c('#5e5458')
c['front'][0] = L(outline([(30, 20), (14, 8), (-4, -10), (-14, -18, 1), (-6, -2), (8, 16), (22, 30)]), HRN, 'b')
c['front'].insert(1, L(outline([(74, 22), (90, 18), (102, 8), (108, 0, 1), (106, 14), (94, 28), (80, 32)]), HRN, 'b'))
c['face']['hairline'] = [(19, 104), (18.5, 70), (19, 52), (30, 47), (50, 45), (70, 47), (81, 52), (81.5, 70), (81, 104)]
c['front'][4] = L(outline([(14, 46), (40, 36), (54, 40), (56, 56), (55, 80), (50, 100, 1), (38, 90), (20, 84), (14, 66)]), 'mid', 'f')
c['front'][5] = L(blob([(57, 81), (66, 84), (76, 82), (82, 74), (80, 66), (76, 76), (66, 80), (58, 78)], 5), _c('#c83a2a'), 'f', False)
c['side'] = [L(outline([(30, 20), (14, 8), (0, -8), (-8, -16, 1), (-2, 0), (10, 16), (22, 30)]), HRN, 'b')] + c['side']
c['back'] = [L(outline([(70, 20), (86, 8), (104, -10), (114, -18, 1), (106, -2), (92, 16), (78, 30)]), HRN, 'b'),
             L(outline([(26, 22), (10, 18), (-2, 8), (-8, 0, 1), (-6, 14), (6, 28), (20, 32)]), HRN, 'b')] + c['back']

# Anthea Tussore: el nacimiento del pelo bajaba por fuera de la cara (raya en ángulo dentro del pelo); ahora sigue la cara
c = _fx('anthea-tussore')
c['face']['hairline'] = [(19, 104), (18.5, 70), (19, 56), (24, 50), (34, 50), (44, 40), (60, 38), (74, 46), (81, 52), (81.5, 70), (81, 104)]

# Snap "Shutter" Breakwater: el pelo que asoma bajo el gorro es salmón rosado, no naranja
c = _fx('snap-shutter-breakwater')
_hair(c, '#da8a70', '#b86a54', '#8e4e3e')

# Seneca Herrmann: melena malva apagada (no morado vivo)
c = _fx('seneca-herrmann')
_hair(c, '#715077', '#553559', '#3e2640')

# Los cinco White-Whitely (Eins, Zwei, Drei, Vier, F-nf): el mismo casco blanco de bola de billar con su número, que les
# baja hasta el ojo izquierdo y tapa el derecho; el borde de abajo del casco es una franja rosada, y por debajo asoman dos
# mechones blancos (con sombra rosa) sobre las mejillas. Antes Eins, Drei y F-nf no tenían ni franja ni mechones, y Zwei y
# Vier llevaban el casco detrás de la cara (se les veía la frente) y los mechones rosas.
PNKB, PNKS = _c('#d8b4a8'), _c('#c89a90')
_BALL = copy.deepcopy(CHARS[K + 'eins-1-white-whitely']['front'][:2])


def _tufts():
    out = []
    for pts in ([(10, 70), (22, 74), (26, 86), (20, 96, 1), (14, 86), (6, 92, 1), (8, 80)],
                [(90, 70), (78, 74), (74, 86), (80, 96, 1), (86, 86), (94, 92, 1), (92, 80)]):
        out += [L(outline(pts), WHITE, 'f', True, True), L(quad(pts[1], lerp(pts[1], pts[2], 0.5), lerp(pts[3], pts[4], 0.5)), PNKS, 'f', False, False, 1.6)]
    return out


for _pid in ('eins-1-white-whitely', 'zwei-2-white-whitely', 'drei-3-white-whitely', 'vier-4-white-whitely', 'f-nf-5-white-whitely'):
    c = _fx(_pid)
    fr_ = c['front']
    if _pid in ('zwei-2-white-whitely', 'vier-4-white-whitely'):
        num = [l for l in fr_ if l['w'] and l['c'] == BLACK]
        eye = [l for l in fr_ if not l['w'] and l['c'] in (WHITE, 'iris', BLACK)] + [l for l in fr_ if l['w'] and l['c'] == OUTC]
        tape = [l for l in fr_ if l['c'] == (242, 226, 208, 255)]
        c['pal']['mid'] = _c('#f4f2ee')
        c['pal']['shade'] = _c('#d8c4c4')
    else:
        num = [l for l in fr_ if l['w'] and l['c'] == (58, 58, 58, 255)]
        eye = [l for l in fr_ if l['c'] in (WHITE, (58, 154, 168, 255)) or (l['c'] == BLACK and not l['w'])]
        tape = [l for l in fr_ if l['c'] == (240, 220, 192, 255)]
    hel = copy.deepcopy(_BALL)
    band = [L(hel[0]['s'], PNKB, 'f', False), L([(x, y * 0.86) for x, y in hel[0]['s']], hel[0]['c'], 'f', False)]
    c['front'] = [hel[0]] + band + [hel[1]] + num + _tufts() + eye + tape

# Rick "R" White-Whitehurst: las marcas de las mejillas son dos mechones blancos (no manchas rosas)
c = _fx('rick-r-white-whitehurst')
for l in c['front']:
    if l['c'] == (232, 184, 200, 255):
        l['c'], l['ln'] = WHITE, True

# Nitely "N" White-Whitehurst: el mechón de delante es una cresta blanca (con sombra rosada) que sube de la frente y se
# curva hacia arriba a la derecha, sobre el pelo gris
c = _fx('nitely-n-white-whitehurst')
c['front'][2] = L(outline([(42, 62), (34, 40), (36, 14), (52, -4), (76, -12), (98, -14, 1), (80, -2), (64, 8), (56, 24), (56, 44), (50, 62, 1)]), WHITE, 'f')
c['front'].insert(3, L(quad((40, 48), (40, 20), (60, 4)), _c('#e0b8b8'), 'f', False, False, 2.4))
c['side'][2] = L(outline([(56, 40), (50, 16), (60, 0), (80, -10), (100, -14, 1), (84, 0), (70, 10), (66, 30)]), WHITE, 'f')
c['back'].append(L(outline([(36, 14), (52, -4), (76, -12), (98, -14, 1), (80, -2), (60, 10)]), WHITE, 'b'))


def heart(cx, cy, r):
    """Corazón (contorno) centrado en (cx, cy) de medio ancho r."""
    return outline([(cx, cy - r * 0.45), (cx + r * 0.5, cy - r * 0.95), (cx + r, cy - r * 0.45), (cx + r * 0.8, cy + r * 0.2), (cx, cy + r, 1),
                    (cx - r * 0.8, cy + r * 0.2), (cx - r, cy - r * 0.45), (cx - r * 0.5, cy - r * 0.95)])


# Ricky Shee: ojos blancos de enfado con pupila negra y contorno grueso, y cejas negras gruesas en V (no ojos de punto)
c = _fx('ricky-shee')
c['face'].update(eyes='sharp', brows='angry')
c['pal']['iris'] = BLACK
_drop(c, 'front', 1, 2)

# Christian Ball: flequillo recto de puntas hasta las cejas; sin los ricitos sueltos que salían bajo la melena
c = _fx('christian-ball')
_drop(c, 'front', 10, 11)
c['front'].insert(2, L(outline([(18, 60), (20, 40), (34, 30), (50, 28), (66, 30), (80, 40), (82, 60), (76, 56), (72, 64, 1), (66, 54), (60, 62, 1), (54, 54),
                                 (48, 62, 1), (42, 54), (36, 62, 1), (30, 54), (26, 64, 1), (22, 56)]), 'mid', 'f'))

# Singer Long: a los lados de la cara le bajan unos rizos naranjas hasta la mandíbula (patillas rizadas)
c = _fx('singer-long')
for sx in (1, -1):
    x0 = 50 - sx * 32
    pts = [(x0 - sx * 4, 48), (x0 + sx * 9, 52), (x0 + sx * 4, 64), (x0 + sx * 10, 74), (x0 + sx * 3, 84), (x0 + sx * 7, 94), (x0 - sx * 3, 100, 1),
           (x0 - sx * 9, 88), (x0 - sx * 6, 74), (x0 - sx * 10, 62)]
    c['front'].append(L(outline(pts if sx == 1 else pts[::-1]), 'mid', 'f'))
    c['front'].append(L([(x0 + sx * 1, 60), (x0 - sx * 2, 70), (x0 + sx * 0, 84)], 'shade', 'f', False, False, 1.2))
c['side'].append(L(outline([(46, 50), (56, 54), (52, 70), (56, 84), (48, 96, 1), (42, 80), (40, 62)]), 'mid', 'f'))

# Lucius Lox: la mecha blanca es una franja ancha que sale de la coronilla y se curva por el lado izquierdo (no una raya
# fina en ángulo sobre la cabeza)
c = _fx('lucius-lox')
c['front'][7] = L(outline([(54, 4), (34, 6), (16, 18), (6, 36), (4, 50), (12, 50), (16, 36), (28, 22), (44, 14), (56, 12)]), _c('#ece4dc'), 'b', False)

# Dai Mondo: el pelo gris largo cae desde la capucha por delante de la cara y le tapa el ojo derecho
c = _fx('dai-mondo')
c['front'].insert(8, L(outline([(46, 38), (62, 34), (78, 44), (84, 70), (82, 102, 1), (72, 82), (66, 104, 1), (58, 78), (52, 94, 1), (48, 62)]),
                       _c('#a7b2c1'), 'f', False, True))

# Pinkie Harte: el corazón rosa es grande y va en la mejilla izquierda (no uno pequeño junto a la boca)
c = _fx('pinkie-harte')
c['front'][8] = L(heart(30, 87, 6), _c('#e86a8a'), 'f', False, True)

# Drew "Circle" Serkell: las bolas amarillas y blancas son grandes y le cubren toda la parte de arriba e izquierda de la
# cabeza (en el retrato tapan más de media cabeza)
c = _fx('drew-circle-serkell')
YB, YBD = _c('#f8d040'), _c('#d8a820')
_drop(c, 'front', 2, 3, 4, 5, 6)
c['front'][2:2] = [L(ell(10, 12, 13, 12), WHITE, 'b'), L(ell(42, 2, 15, 13), YB, 'b'), L(ell(36, 4, 6, 5), _c('#fbe68a'), 'b', False),
                   L(ell(52, 26, 18, 16), YB, 'b'), L(ell(60, 32, 9, 7), YBD, 'b', False), L(ell(44, 18, 6, 5), _c('#fbe68a'), 'b', False),
                   L(ell(22, 36, 15, 13), WHITE, 'b'), L(ell(26, 42, 8, 5), _c('#e0e0e0'), 'b', False)]
c['side'] = [l for l in c['side'] if l['c'] not in (WHITE, (248, 208, 64, 255))] + [
    L(ell(40, 6, 15, 13), YB, 'b'), L(ell(52, 26, 16, 14), YB, 'b'), L(ell(30, 32, 13, 12), WHITE, 'b'), L(ell(20, 12, 11, 10), WHITE, 'b')]
c['back'] = [l for l in c['back'] if l['c'] not in (WHITE, (248, 208, 64, 255))] + [
    L(ell(90, 12, 13, 12), WHITE, 'b'), L(ell(58, 2, 15, 13), YB, 'b'), L(ell(48, 26, 18, 16), YB, 'b'), L(ell(78, 36, 15, 13), WHITE, 'b')]

# Eolia Amhart: la correa marrón va ceñida a la gorra de aviador (no un ala que sobresale por los lados)
c = _fx('eolia-amhart')
c['front'][2] = L(quad((7, 50), (50, 38), (93, 50)) + quad((93, 58), (50, 46), (7, 58)), _c('#a8501e'), 'f', False, True)

# Alben Moretti: bajo la cinta blanca se ven los ojos en sombra, entornados
c = _fx('alben-moretti')
c['front'] += [L(quad((16, 78), (50, 90), (84, 78)) + [(84, 76), (16, 76)], 'skin_d', 'f', False),
               L(quad((28, 83), (35, 86), (42, 83)), OUTC, 'f', False, False, 2.2), L(quad((58, 83), (65, 86), (72, 83)), OUTC, 'f', False, False, 2.2)]

# Ollie Impix: el flequillo rubio baja en pico hasta el antifaz, con mechones marrones (sin la raya del medio)
c = _fx('ollie-impix')
_drop(c, 'front', 2)
c['face']['hairline'] = [(9.9, 104), (14, 60), (34, 58), (50, 66), (66, 58), (86, 60), (90.1, 104)]
c['front'][2:2] = [L(outline([(30, 50), (50, 46), (70, 50), (56, 60), (50, 68, 1), (44, 60)]), 'mid', 'f', False)] + \
    [L(quad((x, 10), (x + 4, 34), (x + 2 * (50 - x) / 10, 58)), 'deep', 'f', False, False, 1.2) for x in (30, 42, 58, 70)]
c = CHARS[K + 'eolia-amhart']
c['side'][1] = L(quad((4, 46), (50, 30), (90, 40)) + quad((90, 48), (50, 38), (4, 54)), _c('#a8501e'), 'f', False, True)
c['back'][1] = L(quad((5, 50), (50, 40), (95, 50)) + quad((95, 58), (50, 48), (5, 58)), _c('#a8501e'), 'f', False, True)

c = CHARS[K + 'lucius-lox']
c['side'][2] = L(outline([(84, 10), (60, 4), (36, 8), (16, 22), (6, 42), (14, 44), (22, 30), (40, 16), (62, 12), (84, 16)]), _c('#ece4dc'), 'b', False)
c['back'][2] = L(outline([(46, 4), (66, 6), (84, 18), (94, 36), (96, 50), (88, 50), (84, 36), (72, 22), (56, 14), (44, 12)]), _c('#ece4dc'), 'b', False)
_drop(c, 'back', 3)

c = CHARS[K + 'ricky-shee']
c['front'].append(L(outline([(30, 46), (50, 44), (70, 46), (58, 54), (50, 64, 1), (42, 54)]), 'mid', 'f', False))

c = CHARS[K + 'pinkie-harte']
c['front'][8] = L(heart(27, 92, 5), _c('#e86a8a'), 'f', False, True)

c = CHARS[K + 'drew-circle-serkell']
c['front'][2] = L(ell(16, 16, 13, 12), WHITE, 'b')

# Del Aket: el adorno del moño son dos palos crema gruesos a los lados y un aro grande encima; los ojos van en un antifaz
# negro, la nariz es una bola roja alargada a lo ancho y la boca enseña los dientes apretados
c = _fx('del-aket')
CRM = _c('#e8dcae')
_drop(c, 'front', 3, 4, 5)
c['front'][3:3] = [L(outline([(42, 12), (20, 4), (4, 8), (2, 16), (18, 14), (40, 20)]), CRM, 'b'), L(outline([(58, 12), (80, 4), (96, 8), (98, 16), (82, 14), (60, 20)]), CRM, 'b'),
                   L(ell(50, 0, 10, 9) + [ell(50, 0, 10, 9)[0]], CRM, 'b', False, False, 4.2)]
c['front'] += [L(blob([(22, 68), (36, 64), (48, 70), (52, 74), (64, 64), (78, 68), (80, 80), (64, 84), (50, 80), (36, 84), (20, 80)], 5), BLACK, 'f', False),
               L(outline([(28, 72), (42, 72), (40, 80), (30, 79)]), WHITE, 'f', False), L(outline([(72, 72), (58, 72), (60, 80), (70, 79)]), WHITE, 'f', False),
               L(ell(37, 76, 2.2, 2.6), BLACK, 'f', False), L(ell(63, 76, 2.2, 2.6), BLACK, 'f', False),
               L(ell(50, 86, 7, 3.6), _c('#d24a34'), 'f', False, True)]
c['face'].update(eyes='none', mouth='none', nose=None)
c['front'].insert(3, L(outline([(28, 50), (50, 44), (72, 50), (50, 66, 1)]), 'mid', 'f', False))
c['front'] += [L([(32, 92), (68, 92), (64, 102), (36, 102)], WHITE, 'f', False, True), L([(34, 97), (66, 97)], OUTC, 'f', False, False, 1.0)] + \
    [L([(x, 92), (x, 102)], OUTC, 'f', False, False, 0.8) for x in (40, 46, 52, 58)]
for v in ('side', 'back'):
    c[v] = [l for l in c[v] if l['c'] != (232, 220, 174, 255)]
c['side'] += [L(outline([(48, 10), (34, 2), (22, 6), (22, 14), (34, 12), (48, 18)]), CRM, 'b'), L(ell(50, 0, 9, 8) + [ell(50, 0, 9, 8)[0]], CRM, 'b', False, False, 4)]
c['back'] += [L(outline([(42, 12), (20, 4), (4, 8), (2, 16), (18, 14), (40, 20)]), CRM, 'b'), L(outline([(58, 12), (80, 4), (96, 8), (98, 16), (82, 14), (60, 20)]), CRM, 'b'),
              L(ell(50, 0, 10, 9) + [ell(50, 0, 10, 9)[0]], CRM, 'b', False, False, 4.2)]

# Bjorn Thiswey: la cresta blanca rosada sube alta en punta (no un casquete plano) y los ojos son iris amarillos rodeados
# de unas ojeras negras gruesas (no gafas)
c = _fx('bjorn-thiswey')
c['face'].update(eyes='none')
CR = _c('#ece0e4')
c['front'][2] = L(outline([(30, 44), (26, 22), (32, 2), (44, -14), (54, -16), (64, -6), (72, 14), (70, 44), (50, 38)]), CR)
c['front'][3] = L(quad((40, 36), (38, 10), (48, -10)), _c('#c8b4bc'), 'f', False, False, 1.2)
c['front'][4] = L(quad((58, 36), (60, 10), (56, -10)), _c('#c8b4bc'), 'f', False, False, 1.2)
c['front'] = [l for l in c['front'] if not (l['w'] and l['c'] == OUTC and 66 <= min(p[1] for p in l['s']) <= 82)]
c['front'] += [L([(26, 64), (44, 70)], OUTC, 'f', False, False, 3.0), L([(74, 64), (56, 70)], OUTC, 'f', False, False, 3.0)]
for cx in (36, 64):
    c['front'] += [L(ell(cx, 76, 8.6, 7.4), BLACK, 'f', False), L(ell(cx, 76, 5.2, 4.8), _c('#f0d040'), 'f', False), L(ell(cx, 76, 1.6, 1.6), BLACK, 'f', False)]
c['side'][len(c['side']) - 2] = L(outline([(24, 40), (26, 14), (40, -8), (54, -14), (66, -2), (74, 18), (78, 38), (50, 36)]), CR)
c['back'][len(c['back']) - 2] = L(outline([(28, 44), (28, 18), (42, -6), (54, -14), (66, -4), (72, 20), (72, 44), (50, 40)]), CR)

# Boo Fonte: flequillo recto hasta las cejas, y el lazo azul lleva lunares blancos
c = _fx('boo-fonte')
c['front'].insert(4, L(outline([(16, 52), (20, 36), (36, 28), (50, 26), (64, 28), (80, 36), (84, 52), (82, 64), (70, 62), (60, 66), (50, 62), (40, 66), (30, 62), (18, 64)]), 'mid', 'f'))
c['front'] += [L(ell(x, y, 2.6, 2.4), WHITE, 'f', False) for x, y in ((12, 24), (24, 30), (40, 8), (56, 6), (70, 14), (84, 22), (90, 30), (34, 14))]

# Mickey Schmitt: la franja roja de la máscara cuelga en arco (U) y bordea la máscara por los lados; los ojos asoman en
# unas cuencas negras con el iris verde azulado, y el pico de la máscara baja entre ellos hasta la nariz
c = _fx('mickey-schmitt')
RD = (200, 40, 40, 255)
c['front'][3] = L(quad((16, 24), (50, 70), (84, 24)), RD, 'f', False, False, 4.2)
c['front'][4] = L(blob([(22, 72), (32, 66), (44, 70), (44, 80), (30, 82), (22, 78)], 5), BLACK, 'f', False)
c['front'][5] = L(blob([(78, 72), (68, 66), (56, 70), (56, 80), (70, 82), (78, 78)], 5), BLACK, 'f', False)
c['front'][6] = L(ell(34, 75, 4, 3.6), _c('#4a9aa8'), 'f', False)
c['front'][7] = L(ell(66, 75, 4, 3.6), _c('#4a9aa8'), 'f', False)
c['front'] += [L(ell(34, 75, 1.4, 1.4), BLACK, 'f', False), L(ell(66, 75, 1.4, 1.4), BLACK, 'f', False),
               L(quad((14, 30), (10, 56), (18, 80)), RD, 'f', False, False, 3.0), L(quad((86, 30), (90, 56), (82, 80)), RD, 'f', False, False, 3.0),
               L(outline([(44, 60), (56, 60), (54, 82), (50, 88, 1), (46, 82)]), _c('#f4f0ea'), 'f', False, True)]

# Drew Pii: el rubor es naranja y solo en la mejilla derecha (la izquierda la tapa el pelo)
c = _fx('drew-pii')
_drop(c, 'front', 3)
c['front'][3]['c'] = _c('#e8a060')

# Harold Oldings: el pelo baja en pico al centro de la frente; ojos entornados con el párpado caído (no cerrados) y
# nariz grande y chata
c = _fx('harold-oldings')
c['face'].update(eyes='none', nose=(50, 86, 6.5), hairline=[(10.7, 104), (14, 48), (38, 44), (50, 52), (62, 44), (86, 48), (89.3, 104)])
c['front'].insert(1, L(outline([(34, 42), (50, 40), (66, 42), (50, 54, 1)]), 'mid', 'f', False))
c['front'] += lid_eye(35, 76, 6.5, 4, _c('#e8a870'), ri=2, py=1.0) + lid_eye(65, 76, 6.5, 4, _c('#e8a870'), ri=2, py=1.0)

# Juan Avis: flequillo de puntas que le tapa la frente hasta las cejas
c = _fx('juan-avis')
c['front'].insert(2, L(outline([(16, 54), (20, 34), (36, 24), (54, 22), (70, 28), (82, 40), (84, 58), (80, 66, 1), (74, 60), (66, 66, 1), (60, 60),
                                 (52, 64, 1), (46, 60), (40, 66, 1), (34, 60), (26, 64, 1), (22, 60), (20, 66, 1)]), 'mid', 'f'))
c['front'].insert(3, L(outline([(62, 26), (78, 34), (84, 56), (80, 66), (74, 56), (70, 40)]), 'shade', 'f', False))

# Larga Thanlyfe: no es calvo: el pelo blanco grisáceo con raya al medio le cubre la coronilla y cae por los lados
c = _fx('larga-thanlyfe')
c['front'][3:3] = [L(outline([(50, 6), (30, 10), (14, 28), (10, 58), (20, 62), (24, 40), (36, 22), (50, 16)]), 'mid', 'b'),
                   L(outline([(50, 6), (70, 10), (86, 28), (90, 58), (80, 62), (76, 40), (64, 22), (50, 16)]), 'mid', 'b'),
                   L([(50, 6), (50, 16)], 'deep', 'b', False, False, 1.0)]
c['side'].insert(1, L(outline([(84, 26), (70, 6), (46, 2), (20, 10), (6, 34), (10, 60), (40, 50), (60, 30)]), 'mid', 'b'))
c['back'].insert(1, L(outline([(12, 60), (12, 30), (26, 10), (50, 4), (74, 10), (88, 30), (88, 60), (50, 70)]), 'mid', 'b'))
c = CHARS[K + 'mickey-schmitt']
c['side'][2] = L(quad((8, 30), (40, 66), (88, 40)), RD, 'f', False, False, 4.0)
c['side'][3] = L(blob([(74, 70), (88, 68), (90, 80), (76, 82)], 4), BLACK, 'f', False)
c['side'][4] = L(ell(83, 75, 2.6, 3), _c('#4a9aa8'), 'f', False)
c['back'][3] = L(quad((12, 30), (50, 56), (88, 30)), RD, 'f', False, False, 4.2)

# Spike Echidna: en la máscara roja hay dos espirales negras sobre la frente, y los ojos asoman en cuencas negras
# almendradas con el iris gris verdoso (no ojos blancos con cejitas); bajo la máscara, a los lados del pico, se ve la
# piel naranja
c = _fx('spike-echidna')
_drop(c, 'front', 3, 4, 5, 6, 7, 8)
c['face'].update(eyes='none')
c['front'] += [L(blob([(24, 88), (38, 92), (42, 104), (30, 106), (22, 98)], 4), _c('#f0a050'), 'f', False),
               L(blob([(76, 88), (62, 92), (58, 104), (70, 106), (78, 98)], 4), _c('#f0a050'), 'f', False),
               L(outline([(42, 86), (58, 86), (54, 104), (50, 112, 1), (46, 104)]), _c('#c82a24'), 'f', False, True),
               spiral(36, 52, 7, 1.5, BLACK, 1.8, a0=0.0), spiral(64, 52, 7, 1.5, BLACK, 1.8, a0=math.pi, sy=1.0)]
for s_ in (1, -1):
    cx = 50 - s_ * 15
    c['front'] += [L(blob([(cx - s_ * 14, 66), (cx - s_ * 2, 66), (cx + s_ * 11, 74), (cx + s_ * 6, 84), (cx - s_ * 8, 82)], 5), BLACK, 'f', False),
                   L(ell(cx + s_ * 1, 75.5, 5, 4.6), _c('#9ab0a8'), 'f', False), L(ell(cx + s_ * 1, 75.5, 1.8, 2.2), BLACK, 'f', False)]

# Snapper Krabbie: en el centro de la frente le cae un rizo gordo rosa (con su sombra), no un mechón liso
c = _fx('snapper-krabbie')
c['front'] += [L(outline([(42, 40), (40, 24), (50, 14), (64, 18), (68, 32), (62, 44), (66, 58), (58, 66, 1), (54, 50)]), 'mid', 'f', True, True),
               spiral(54, 30, 9, 1.2, 'shade', 2.2, a0=2.6)]

# Amanda Jurr: los moños son caracolas (espirales), y los ojos grandes azul pálido con aros concéntricos
c = _fx('amanda-jurr')
c['front'][1] = spiral(24, 8, 9, 1.4, 'deep', 1.6, z='b')
c['front'][3] = spiral(76, 8, 9, 1.4, 'deep', 1.6, z='b', a0=math.pi)
c['face']['eyes'] = 'none'
for cx in (36, 64):
    c['front'] += [L(ell(cx, 78, 8, 8.4), WHITE, 'f', False, True), L(ell(cx, 78, 6.2, 6.6), _c('#a8d4e8'), 'f', False),
                   L(ell(cx, 78, 4.4, 4.8) + [ell(cx, 78, 4.4, 4.8)[0]], _c('#5a8aa8'), 'f', False, False, 0.9),
                   L(ell(cx, 78, 2.2, 2.4), _c('#2a3a50'), 'f', False), L(ell(cx - 2, 75.5, 1.2, 1.2), WHITE, 'f', False)]
c['front'].insert(9, L(ell(50, 96, 2.2, 3), _c('#7a3030'), 'f', False))
_drop(c, 'front', 6)

# Debbie Dare: ojos de iris amarillo pálido con un aro castaño, raya negra gruesa con pestaña hacia fuera
c = _fx('debbie-dare')
c['face']['eyes'] = 'none'
for cx, s_ in ((36, -1), (64, 1)):
    c['front'] += [L(ell(cx, 76, 6.6, 7.4), WHITE, 'f', False), L(ell(cx, 76.5, 5.4, 5.8), _c('#9a5a32'), 'f', False),
                   L(ell(cx, 76.5, 3.8, 4.2), _c('#f2eca0'), 'f', False), L(ell(cx, 77, 1.4, 1.6), BLACK, 'f', False),
                   L(quad((cx - 8, 72), (cx, 65), (cx + 8, 72)) + [(cx + s_ * 12, 66)], BLACK, 'f', False, False, 2.6)]

# Dave Dreem: el pelo rubio baja hasta la cinta (no se le ve una franja de frente entre el pelo y la cinta)
c = _fx('dave-dreem')
c['front'].insert(2, L(outline([(10, 58), (14, 36), (34, 26), (50, 24), (66, 26), (86, 36), (90, 58)]), 'mid', 'f', False))
c['front'].insert(3, L(outline([(56, 24), (72, 30), (84, 50), (70, 64, 1), (64, 40)]), 'mid', 'f', True))

# Manny Saboy: ojos en espiral amarillos con el aro verde (no blanco y negro)
c = _fx('manny-saboy')
for l in c['front']:
    if l['c'] == (240, 240, 208, 255):
        l['c'] = _c('#ece88a')
    elif l['w'] == 1.2 and l['c'] == BLACK:
        l['c'] = _c('#7a9a40')

# Humphrey Dictable: el pompón blanco es enorme; ojos de párpado pesado (oscuro) con el iris morado
c = _fx('humphrey-dictable')
c['face']['eyes'] = 'none'
c['front'][2] = L(blob([(50, -36), (64, -32), (70, -20), (66, -8), (50, -4), (34, -8), (30, -20), (36, -32)], 6), _c('#f6f8fa'))
c['back'][3] = L(blob([(50, -36), (64, -32), (70, -20), (66, -8), (50, -4), (34, -8), (30, -20), (36, -32)], 6), _c('#f6f8fa'))
c['side'][2] = L(blob([(44, -34), (58, -30), (62, -18), (58, -6), (44, -2), (30, -8), (26, -20), (32, -30)], 6), _c('#f6f8fa'))
c['front'] += lid_eye(35, 76, 7, 5, _c('#7a5a44'), _c('#6a4aa8'), 2.6, 1.0) + lid_eye(65, 76, 7, 5, _c('#7a5a44'), _c('#6a4aa8'), 2.6, 1.0)
c['front'] += [L(quad((27, 82), (35, 85), (43, 82)), _c('#8a6a8a'), 'f', False, False, 1.4), L(quad((57, 82), (65, 85), (73, 82)), _c('#8a6a8a'), 'f', False, False, 1.4)]

# Icarus Damselfly: las gafas negras de libélula son dos óvalos grandes sobre la frente, casi tocándose; la joya dorada es
# una corona con pico, y las coletas de los lados se curvan hacia arriba como cuernos
c = _fx('icarus-damselfly')
c['front'][2] = L(outline([(16, 34), (4, 28), (-8, 34), (-14, 50, 1), (-4, 42), (6, 44), (16, 52)]), 'mid', 'b')
c['front'][3] = L(outline([(84, 34), (96, 28), (108, 34), (114, 50, 1), (104, 42), (94, 44), (84, 52)]), 'mid', 'b')
c['front'][5] = L(ell(32, 50, 16, 11), _c('#2c2c28'), 'f', True)
c['front'][6] = L(ell(68, 50, 16, 11), _c('#2c2c28'), 'f', True)
c['front'][7] = L(outline([(40, 44), (44, 36), (50, 30, 1), (56, 36), (60, 44), (58, 56), (50, 62, 1), (42, 56)]), _c('#e8c030'), 'f', True)
c['front'] += [L(ell(26, 46, 4, 2.4), _c('#5a5a54'), 'f', False), L(ell(62, 46, 4, 2.4), _c('#5a5a54'), 'f', False)]

# Rory "Stripes" Tigre: las rayas de tigre del pelo son gruesas y negras a los lados, y las de las mejillas son rayas
# castañas (marcas de tigre), no bigotes de gato
c = _fx('rory-stripes-tigre')
STR = []
for s_ in (1, -1):
    for y0 in (36, 52, 68):
        x0 = 50 - s_ * 46
        STR.append(L(outline([(x0, y0), (x0 + s_ * 14, y0 + 4), (x0 + s_ * 18, y0 + 7, 1), (x0 + s_ * 12, y0 + 7), (x0, y0 + 6)]), BLACK, 'f', False))
c['front'] = c['front'][:4] + STR + c['front'][8:10]
for s_ in (1, -1):
    for y0 in (80, 87):
        x0 = 50 - s_ * 32
        c['front'].append(L(outline([(x0, y0), (x0 + s_ * 9, y0 + 1), (x0 + s_ * 12, y0 + 2.5, 1), (x0 + s_ * 8, y0 + 3), (x0, y0 + 3.4)]), _c('#9a5028'), 'f', False))

# Egor Coxcomb: sin el pañuelo rojo suelto en la barbilla; las marcas de los lados de la cabeza son rayas rojas gruesas
c = _fx('egor-coxcomb')
_drop(c, 'front', 7)
for l in c['front']:
    if l['w'] == 2.6 and l['c'] == 'shade':
        l['c'], l['w'] = (196, 42, 38, 255), 3.4
c['front'][2] = L(outline([(36, 34), (30, 8), (36, -10), (42, 2), (44, -22, 1), (52, -4), (58, -24, 1), (60, 0), (68, -12, 1), (70, 10), (64, 34)]), 'mid', 'b')

# Rith McCal: el flequillo baja en mechones de punta sobre la frente, y los cristales turquesa llevan su brillo blanco
c = _fx('rith-mccal')
c['front'].insert(2, L(outline([(20, 44), (30, 32), (50, 28), (70, 32), (80, 44), (74, 50), (68, 62, 1), (62, 48), (54, 58, 1), (48, 46), (40, 60, 1),
                                 (36, 46), (28, 56, 1)]), 'mid', 'f'))
c['front'] += [L([(24, 78), (30, 72), (32, 76), (38, 70)], WHITE, 'f', False, False, 1.6), L([(60, 78), (66, 72), (68, 76), (74, 70)], WHITE, 'f', False, False, 1.6)]

# Donald "Don" Hooan: flequillo recto a la altura de las cejas y las franjas negras de los lados, más anchas
c = _fx('donald-don-hooan')
c['face']['hairline'] = [(19.5, 104), (16, 66), (50, 66), (84, 66), (80.5, 104)]
c['front'][2] = L(outline([(8, 32), (14, 30), (18, 60), (16, 104), (6, 98)]), _c('#1a2024'), 'b', False)
c['front'][3] = L(outline([(92, 32), (86, 30), (82, 60), (84, 104), (94, 98)]), _c('#1a2024'), 'b', False)

# Cole Bludd: el tupé rosa no flota sobre la cabeza: baja hasta la frente y acaba en pico; los rizos rosas de los lados le
# caen sobre las mejillas, por debajo de los ojos
c = _fx('cole-bludd')
c['front'][1] = L(outline([(26, 34), (24, 10), (38, -6), (58, -6), (72, 6), (76, 30), (68, 46), (56, 60, 1), (50, 46), (40, 42)]), (249, 205, 186, 255), 'f', True, True)
c['front'][2] = L(quad((44, 0), (40, 24), (54, 52)), (216, 160, 144, 255), 'f', False, False, 1.2)
c['front'][5] = L(outline([(16, 82), (26, 86), (30, 96), (22, 100, 1), (18, 94), (12, 98, 1), (12, 88)]), (249, 205, 186, 255), 'f', True, True)
c['front'][6] = L(outline([(84, 82), (74, 86), (70, 96), (78, 100, 1), (82, 94), (88, 98, 1), (88, 88)]), (249, 205, 186, 255), 'f', True, True)
c['face']['hairline'] = [(19.5, 104), (18, 56), (30, 48), (50, 46), (70, 48), (82, 56), (80.5, 104)]

# Cara Mass: las pestañas de los ojos cerrados son largas y marcadas
c = _fx('cara-mass')
for l in c['front']:
    if l['w'] == 1.2 and l['c'] == OUTC:
        l['w'] = 1.8
        (x0, y0), (x1, y1) = l['s'][0], l['s'][-1]
        l['s'] = [(x0, y0), (x1 + (x1 - x0) * 0.3, y1 + 1)]

# Luna Reid: el rizo que le nace en la frente es grande y blanco (con la sombra lila) y se enrolla hacia la derecha
c = _fx('luna-reid')
c['front'][2] = L(outline([(44, 54), (36, 34), (38, 14), (50, 0), (66, -4), (78, 6), (78, 22), (68, 28), (64, 16), (56, 12), (50, 20), (48, 34), (52, 50, 1)]), WHITE, 'f')
c['front'].insert(3, L(outline([(62, -2), (76, 4), (78, 20), (68, 28), (66, 14)]), _c('#d8c8e0'), 'f', False))

# Tye Foon: encima de la cabeza lleva dos rizos (uno a cada lado de la coronilla) con el lazo rojo en medio, no un moño
c = _fx('tye-foon')
c['front'][6] = L(ell(32, 6, 13, 9), 'mid', 'b')
c['front'][7] = L(blob([(46, 2), (54, 2), (56, 8), (44, 8)], 4), (200, 58, 58, 255), 'b')
c['front'][7:7] = [L(ell(68, 6, 13, 9), 'mid', 'b'), spiral(32, 6, 7, 1.2, (53, 54, 40, 255), 1.4, 'b'), spiral(68, 6, 7, 1.2, (53, 54, 40, 255), 1.4, 'b', a0=math.pi)]
c['front'] += [L([(40, 58), (44, 66)], OUTC, 'f', False, False, 1.0), L([(60, 58), (56, 66)], OUTC, 'f', False, False, 1.0)]

# Rosa Welle: la cúpula roja del sombrero de platillo es ancha y baja, con tres luces cian (no una punta)
c = _fx('rosa-welle')
c['front'][1] = L(outline([(4, 32), (14, 12), (32, 2), (50, 0), (68, 2), (86, 12), (96, 32)]), (200, 40, 42, 255), 'f')
c['front'][4] = L(ell(28, 14, 5, 3.4), (90, 208, 200, 255), 'f', False)
c['front'][5] = L(ell(72, 14, 5, 3.4), (90, 208, 200, 255), 'f', False)
c['front'].insert(6, L(ell(50, 8, 5, 3.4), (90, 208, 200, 255), 'f', False))

# Wyther Longfeys: cara muy larga con la barbilla ancha, nariz larga y una sonrisa ancha
c = _fx('wyther-longfeys')
c['face'].update(face_front=face_shape(w=4, chin=116, jaw=6), mouth='none', mouth_y=100)
c['front'] += [L(quad((34, 96), (50, 104), (66, 96)), (130, 70, 50, 255), 'f', False, False, 1.6),
               L(quad((50, 70), (54, 82), (52, 88)), 'skin_d', 'f', False, False, 2.0)]

# Chrissy Urchin: boca torcida enseñando los dientes de lado (mueca), y cejas oscuras gruesas y arqueadas
c = _fx('chrissy-urchin')
c['face']['mouth'] = 'none'
c['front'][3]['c'] = c['front'][4]['c'] = _c('#3a2a30')
c['front'] += [L(outline([(40, 100), (52, 96), (64, 98), (62, 104), (50, 106), (42, 104)]), WHITE, 'f', False, True),
               L(quad((41, 102), (52, 100), (63, 101)), OUTC, 'f', False, False, 0.9)]

# Barbara "Bunny" Bitt: la capucha de conejo le tapa la frente hasta las cejas pero deja la cara ancha al aire; la franja
# rosa baja del centro y el botón blanco (con dos puntitos) es grande; bajo la capucha asoma un mechón morado en pico
# hasta el entrecejo; ojos grandes rosas
c = _fx('barbara-bunny-bitt')
HD = (244, 238, 238, 255)
c['front'][0] = ring([(-4, 108), (-2, 50), (8, 18), (30, 2), (50, -2), (70, 2), (92, 18), (102, 50), (104, 108), (50, 112)],
                     [(19, 92), (18, 72), (21, 58), (34, 52), (50, 50), (66, 52), (79, 58), (82, 72), (81, 92), (50, 100)], HD)
c['front'][4] = L(outline([(38, 0), (62, 0), (66, 26), (62, 50), (38, 50), (34, 26)]), (240, 144, 144, 255), 'f', False)
c['front'][5] = L(ell(50, 32, 8, 7), WHITE, 'f', False, True)
c['front'] += [L(ell(47, 31, 1.4, 1.4), _c('#c87878'), 'f', False), L(ell(53, 33, 1.4, 1.4), _c('#c87878'), 'f', False),
               L(outline([(36, 52), (64, 52), (56, 60), (50, 70, 1), (44, 60)]), _c('#5a4a6a'), 'f', False)]
c['pal']['iris'] = _c('#e07a8a')

# Keir Mudgeon: el mechón del centro es más ancho y baja hasta la nariz, un poco hacia el ojo derecho; no tiene bigote,
# solo la perilla
c = _fx('keir-mudgeon')
c['front'][2] = L(outline([(44, 44), (62, 44), (64, 70), (60, 90, 1), (54, 72), (48, 56)]), 'mid', 'f')
_drop(c, 'front', 4)

# Noah "Anon" Nymous: el pelo baja en pico al centro de la frente
c = _fx('noah-anon-nymous')
c['front'].append(L(outline([(22, 50), (50, 46), (78, 50), (58, 56), (50, 66, 1), (42, 56)]), 'mid', 'f', False))
c['face']['hairline'] = [(19.5, 104), (18, 56), (30, 54), (50, 64), (70, 54), (82, 56), (80.5, 104)]

# Rob-O-Meca: el casco blanco baja por los lados de la cara como orejeras
c = _fx('rob-o-meca')
c['front'][1:1] = [L(outline([(6, 40), (20, 44), (22, 96), (12, 100), (6, 70)]), WHITE, 'f'), L(outline([(94, 40), (80, 44), (78, 96), (88, 100), (94, 70)]), WHITE, 'f')]
c['face']['ears'] = False

# Noah Yu: el tupé es una espiral retorcida de franjas verde azulado y azul lavanda
c = _fx('noah-yu')
TEAL = (36, 93, 103, 255)
c['front'][1:2] = [L(quad((16, 42), (22, 10), (50, -6)), TEAL, 'f', False, False, 6),
                   L(quad((32, 50), (44, 16), (74, 2)), TEAL, 'f', False, False, 6),
                   L(quad((56, 52), (70, 26), (90, 20)), TEAL, 'f', False, False, 6)]
c['front'].append(L(outline([(34, 50), (50, 46), (66, 50), (50, 62, 1)]), 'mid', 'f', False))

# Caul Erpa: el pelo baja en pico al centro de la frente
c = _fx('caul-erpa')
c['front'].insert(2, L(outline([(20, 50), (24, 36), (50, 30), (76, 36), (80, 50), (58, 52), (50, 62, 1), (42, 52)]), 'mid', 'f', False))

# Serena Halcyon: melena castaño muy oscuro aceitunado, no negra
c = _fx('serena-halcyon')
_hair(c, '#403c33', '#312d2a', '#24211e', '#5c574c')

# Patton Fairway: nariz larga y grande
c = _fx('patton-fairway')
c['face']['nose'] = None
c['front'].append(L(outline([(48, 72), (52, 72), (57, 88), (50, 91), (43, 88)]), 'skin_d', 'f', False, True))

# Esme Hexe: el mechón verde le tapa del todo el ojo izquierdo (solo se ve el derecho)
c = _fx('esme-hexe')
c['front'][6] = L(outline([(12, 48), (34, 44), (56, 46), (58, 64), (54, 96, 1), (44, 84), (32, 98, 1), (22, 82), (12, 96, 1)]), 'mid', 'f')

# Rundeep Stillwater: el pelo baja en un pico largo hasta el entrecejo, y los ojos cerrados son dos «> <» marcados
c = _fx('rundeep-stillwater')
c['face'].update(eyes='none', hairline=[(19.5, 104), (22, 40), (36, 34), (50, 62), (64, 34), (78, 40), (80.5, 104)])
c['front'].insert(2, L(outline([(36, 34), (50, 30), (64, 34), (54, 48), (50, 62, 1), (46, 48)]), 'mid', 'f', False))
c['front'] += [L([(27, 71), (42, 76), (28, 80)], OUTC, 'f', False, False, 2.4), L([(73, 71), (58, 76), (72, 80)], OUTC, 'f', False, False, 2.4)]

# Richard Roake: pelo gris pardo oscuro (no negro); los mechones le caen por el centro de la cara y le tapan el ojo
# derecho; la raya de pintura naranja solo cruza la mejilla izquierda
c = _fx('richard-roake')
_hair(c, '#655a56', '#4a403d', '#2d2524', '#857a74')
c['front'][3] = L(outline([(42, 34), (60, 30), (74, 44), (72, 70), (64, 98, 1), (57, 76), (50, 92, 1), (46, 62)]), 'mid', 'f')
c['front'][4] = L([(20, 82), (44, 79)], (224, 122, 42, 255), 'f', False, False, 2.6)
_drop(c, 'front', 5)

# Armand Sedate: el casquete de pelo baja por los lados hasta las orejas (no una mancha alta), y la boca abierta con
# labios rojos
c = _fx('armand-sedate')
c['front'][2] = L(outline([(10, 64), (8, 40), (18, 20), (36, 8), (50, 6), (64, 8), (82, 20), (92, 40), (90, 64), (82, 50), (66, 40), (50, 38), (34, 40), (18, 50)]), 'mid', 'f')
c['face']['mouth'] = 'none'
c['front'] += [L(ell(50, 94, 8, 4.2), _c('#d06060'), 'f', False, True), L(blob([(44, 92), (56, 92), (54, 95), (46, 95)], 4), WHITE, 'f', False)]

# Baz "B-Boy" Boyes: la antena son dos rizos curvos (no un cuadrado) y la diadema de los cascos pasa por encima de la
# cabeza, de oreja a oreja (no por la frente)
c = _fx('baz-b-boy-boyes')
c['front'][2] = L(quad((48, 6), (40, -20), (60, -24)) + quad((60, -24), (66, -16), (58, -12))[1:], 'mid', 'f', False, False, 3.4)
c['front'][3] = L(quad((8, 64), (50, -26), (92, 64)), _c('#c84030'), 'b', False, False, 5.0)
c['front'].insert(3, L(quad((58, 6), (58, -10), (70, -14)), 'mid', 'f', False, False, 3.0))
c['front'].insert(5, L(quad((12, 62), (50, -18), (88, 62)), (240, 232, 224, 255), 'b', False, False, 2.0))

# Riff Ormd: el pelo son rastas onduladas gruesas que salen hacia fuera por todos lados, con un mechón blanco ondulado
c = _fx('riff-ormd')
DR = []
for pts in ([(14, 40), (0, 34), (-10, 40, 1), (-2, 46), (12, 50)], [(12, 60), (-2, 62), (-8, 72, 1), (2, 70), (12, 70)],
            [(86, 40), (100, 34), (110, 40, 1), (102, 46), (88, 50)], [(88, 60), (102, 62), (108, 72, 1), (98, 70), (88, 70)],
            [(30, 12), (20, 0), (24, -12, 1), (30, -2), (40, 8)], [(70, 12), (80, 0), (76, -12, 1), (70, -2), (60, 8)],
            [(48, 8), (44, -8), (50, -16, 1), (52, -4), (56, 8)]):
    DR.append(L(outline(pts), 'mid', 'b'))
c['front'] = DR + c['front']
c['front'][len(DR) + 5] = L(outline([(50, 16), (58, 24), (54, 36), (60, 48), (54, 60), (58, 72, 1), (50, 58), (54, 46), (48, 34), (52, 26)]), (168, 200, 216, 255), 'f')

# Janice Queen: el ojo que se ve es grande con el iris rojo, y los labios azulados entreabiertos
c = _fx('janice-queen')
c['face'].update(eyes='big', mouth='none')
c['pal']['iris'] = _c('#c8202a')
c['front'] += [L(ell(54, 95, 5, 2.4), _c('#9ab8c0'), 'f', False, True), L([(50, 95), (58, 95)], OUTC, 'f', False, False, 0.9)]

# Scaris Cowler: la venda negra cruza en diagonal y le tapa el ojo derecho; el izquierdo (rojo) queda al aire con una
# cicatriz en rayo debajo
c = _fx('scaris-cowler')
c['front'][3] = L([(14, 58), (92, 70), (92, 86), (56, 81), (14, 64)], (30, 26, 30, 255), 'f', True)
c['front'][4] = L([(52, 76), (60, 72)], (110, 110, 110, 255), 'f', False, False, 1.2)
c['front'][5] = L(outline([(10, 40), (24, 40), (22, 70), (18, 98, 1), (12, 80), (8, 60)]), 'mid', 'f')
c['face']['eyes'] = 'sharp'
c['pal']['iris'] = _c('#c83030')
c['front'].append(L([(30, 82), (34, 87), (28, 90), (32, 96)], WHITE, 'f', False, False, 1.4))

# Phoenix "Firebird" Southers: las plumas amarillas de los lados son grandes y se abren hacia fuera desde las sienes
c = _fx('phoenix-firebird-southers')
c['front'][6] = L(outline([(22, 58), (6, 62), (10, 72), (-2, 82, 1), (12, 82), (8, 96, 1), (22, 88), (26, 72)]), (240, 176, 48, 255), 'f', True)
c['front'][7] = L(outline([(78, 58), (94, 62), (90, 72), (102, 82, 1), (88, 82), (92, 96, 1), (78, 88), (74, 72)]), (240, 176, 48, 255), 'f', True)

c = CHARS[K + 'baz-b-boy-boyes']
c['side'][2] = L(quad((46, 4), (38, -20), (58, -24)), 'mid', 'f', False, False, 3.4)
c['side'][3] = L(quad((40, 70), (44, -12), (52, 4)), _c('#c84030'), 'f', False, False, 5.0)
c['back'][2] = L(quad((8, 64), (50, -26), (92, 64)), _c('#c84030'), 'f', False, False, 5.0)

c = CHARS[K + 'armand-sedate']
c['face']['nose'] = (50, 85, 3.4)
c['side'][1] = L(outline([(78, 34), (70, 14), (48, 6), (24, 12), (10, 32), (8, 56), (24, 64), (36, 50), (58, 36)]), 'mid', 'f')
c['back'][2] = L(outline([(12, 70), (10, 40), (20, 18), (50, 8), (80, 18), (90, 40), (88, 70), (50, 74)]), 'mid', 'f')

c = CHARS[K + 'riff-ormd']
c['side'] = [L(outline(p), 'mid', 'b') for p in ([(20, 30), (6, 18), (-4, 22, 1), (4, 30), (14, 40)], [(10, 60), (-6, 62), (-12, 72, 1), (0, 72), (10, 74)],
                                                 [(16, 86), (6, 96), (8, 106, 1), (14, 98), (26, 92)], [(54, 6), (56, -10), (64, -16, 1), (64, -2), (66, 8)])] + c['side']
c['back'] = [L(outline(p), 'mid', 'b') for p in ([(14, 40), (0, 34), (-10, 40, 1), (-2, 46), (12, 50)], [(12, 70), (-2, 74), (-8, 84, 1), (2, 82), (14, 80)],
                                                 [(86, 40), (100, 34), (110, 40, 1), (102, 46), (88, 50)], [(88, 70), (102, 74), (108, 84, 1), (98, 82), (86, 80)],
                                                 [(30, 96), (26, 108), (32, 114, 1), (36, 104), (42, 96)], [(70, 96), (74, 108), (68, 114, 1), (64, 104), (58, 96)])] + c['back']

# Rosie Redd (con modelo 3D): la melena es un casco liso y redondeado, más ancho y abombado a la altura de la mandíbula
# (no un contorno ondulado a bultos), con sombra en el lado derecho y detrás
c = _fx('rosie-redd')
BOB_F = blob([(50, 2), (74, 8), (90, 26), (96, 48), (102, 70), (98, 86), (84, 92), (78, 70), (74, 50), (50, 38), (26, 50), (22, 70), (16, 92), (2, 86),
              (-2, 70), (4, 48), (10, 26), (26, 8)], 8)
c['front'][0] = L(BOB_F, 'mid', 'b')
c['front'].insert(1, L(blob([(64, 10), (84, 22), (94, 46), (100, 70), (96, 84), (86, 88), (80, 64), (74, 44)], 6), 'shade', 'b', False))
c['side'][0] = L(blob([(70, 20), (60, 6), (40, 2), (18, 10), (4, 30), (-2, 56), (0, 78), (12, 90), (36, 90), (48, 74), (46, 54), (66, 40)], 8), 'mid', 'b')
c['side'].insert(1, L(blob([(4, 50), (24, 46), (40, 60), (40, 84), (14, 88), (2, 72)], 6), 'shade', 'b', False))
c['back'][0] = L(blob([(50, 2), (76, 8), (92, 26), (100, 54), (100, 80), (88, 92), (50, 96), (12, 92), (0, 80), (0, 54), (8, 26), (24, 8)], 8), 'mid', 'b')
c['back'].insert(1, L(blob([(6, 60), (50, 54), (94, 60), (96, 82), (50, 92), (4, 82)], 6), 'shade', 'b', False))

# Spotter (con modelo 3D): la nariz de perro es grande, ancha y negra brillante
c = _fx('spotter')
c['front'][9] = L(blob([(38, 84), (50, 80), (62, 84), (60, 94), (50, 98), (40, 94)], 6), (30, 26, 30, 255), 'f', True)
c['front'].insert(10, L(ell(46, 85, 3, 1.6), _c('#6a6a6a'), 'f', False))
c['side'][4] = L(blob([(98, 70), (108, 72), (110, 80), (100, 82)], 4), (30, 26, 30, 255), 'f', True)

# Jade Greene (con modelo 3D): el lazo azul de la diadema es grande, con dos lazadas que se abren hacia arriba
c = _fx('jade-greene')
BOW = (58, 110, 126, 255)
c['front'] += [L(outline([(46, 6), (32, -8), (22, -14, 1), (30, 0), (44, 12)]), BOW, 'f'), L(outline([(54, 6), (68, -8), (78, -14, 1), (70, 0), (56, 12)]), BOW, 'f')]
c['back'] += [L(outline([(46, 6), (32, -8), (22, -14, 1), (30, 0), (44, 12)]), _c('#2a4048'), 'f'), L(outline([(54, 6), (68, -8), (78, -14, 1), (70, 0), (56, 12)]), _c('#2a4048'), 'f')]

# ================================================================== detalles menores

# Cornelius Roes: entre las franjas amarillas del pelo hay surcos anchos de color anaranjado (no rayitas de sombra)
c = _fx('cornelius-roes')
GRV = _c('#e0a040')
for v in ('front', 'side', 'back'):
    for l in c[v]:
        if l['w'] == 3.0 and l['c'] == 'shade':
            l['c'], l['w'] = GRV, 4.2

# Drummond Bays: unos mechones azules del flequillo caen por delante de la cinta hasta los ojos
c = _fx('drummond-bays')
c['front'] += [L(outline([(30, 50), (40, 50), (38, 64), (32, 72, 1), (32, 60)]), 'mid', 'f'), L(outline([(54, 50), (64, 50), (64, 62), (60, 70, 1), (58, 60)]), 'mid', 'f'),
               L(outline([(70, 50), (78, 50), (80, 60), (78, 66, 1), (74, 58)]), 'shade', 'f')]

# Millie Terry: de perfil se ve el lado sin flequillo: el mechón negro va detrás de la oreja, no sobre la mejilla
c = _fx('millie-terry')
c['side'][0] = L(outline([(30, 52), (44, 54), (42, 78), (36, 90, 1), (30, 72)]), 'mid', 'b')

# Gale Sweep: la masa de pelo azul grisáceo lleva mechones gris oscuro barridos hacia la izquierda
c = _fx('gale-sweep')
DK = _c('#6a7a88')
c['front'] += [L(quad((70, 10), (30, 18), (-14, 40)), DK, 'b', False, False, 1.8), L(quad((74, 30), (34, 40), (-10, 70)), DK, 'b', False, False, 1.8),
               L(quad((60, 46), (40, 60), (20, 92)), DK, 'f', False, False, 1.6)]
c['side'] += [L(quad((80, 14), (40, 20), (-10, 40)), DK, 'b', False, False, 1.8), L(quad((80, 40), (40, 50), (-12, 80)), DK, 'b', False, False, 1.8)]
c['back'] += [L(quad((30, 14), (70, 20), (108, 40)), DK, 'b', False, False, 1.8), L(quad((26, 40), (66, 50), (106, 80)), DK, 'b', False, False, 1.8)]

# Francis Shoe: cejas gris claro gruesas y en V de enfado (no dos bandas planas que parecían otra fila de ojos)
c = _fx('francis-shoe')
c['front'][2] = L([(24, 60), (44, 66), (44, 71), (26, 66)], 'shade', 'f', False)
c['front'][3] = L([(76, 60), (56, 66), (56, 71), (74, 66)], 'shade', 'f', False)
c['side'][2] = L([(70, 61), (88, 66), (88, 70), (72, 66)], 'shade', 'f', False)


def _skin(c, rgb):
    """Piel medida: skin y skin_d (0,86), y las capas de color fijo que repetían la piel o su sombra pasan a la nueva."""
    from chars import tone
    p = c['pal']
    old = {p['skin'][:3]: 'skin', p['skin_d'][:3]: 'skin_d'}
    p['skin'] = tuple(rgb) + (255,)
    p['skin_d'] = tone(p['skin'], 0.86)
    for v in ('front', 'side', 'back'):
        for l in c[v]:
            if isinstance(l['c'], tuple) and l['c'][:3] in old:
                l['c'] = old[l['c'][:3]]


# ================================================================== piel medida en el retrato
# Tono de piel iluminado más frecuente de mejillas y barbilla (media de los vecinos) donde el dibujo se alejaba más de 30
# (suma de diferencias RGB). Se cambian también las capas fijas que repetían la piel o la sombra antiguas.
for _pid, _sk in {
    'pyro-piranha-nyah': (227, 205, 173),
    'ruby-catbear': (255, 209, 139),
    'rocky-zine': (227, 204, 173),
    'rihanna-lin': (254, 208, 138),
    'howard-robin': (254, 209, 139),
    'gabe-roundy-roundhouse': (238, 166, 95),
    'ruth-ruby-byron': (254, 208, 159),
    'stace-strikes': (254, 207, 158),
    'sid-steppe': (254, 207, 158),
    'rio-samba-sands': (207, 151, 104),
    'eira-dynamic': (254, 207, 159),
    'roland-netland': (207, 149, 104),
    'rick-tangle': (207, 149, 103),
    'seneca-herrmann': (207, 149, 103),
    'ricky-shee': (229, 204, 172),
    'sepia-bartletti': (254, 234, 184),
    'bolt-cagey': (254, 195, 112),
    'jon-himmel': (254, 241, 213),
    'juan-avis': (254, 207, 158),
    'tatsuya-okumura': (240, 183, 128),
    'amanda-jurr': (254, 235, 183),
    'esteban-range': (164, 96, 69),
    'narcisse-rotondo': (228, 205, 172),
    'rory-stripes-tigre': (254, 194, 112),
    'rob-o-meca': (206, 149, 103),
    'ro-st-nutts': (205, 113, 79),
    'rundeep-stillwater': (254, 207, 158),
    'rosie-redd': (251, 216, 181),
    'baz-b-boy-boyes': (253, 207, 158),
    'riff-ormd': (207, 149, 103),
    'scaris-cowler': (254, 239, 211),
    'ron-flappibal': (228, 204, 172),
}.items():
    _skin(_fx(_pid), _sk)

# Riff Ormd: las rastas son gris verdoso azulado más claro (medido en el retrato), no pizarra
_hair(_fx('riff-ormd'), '#6a8288', '#52666c', '#3c4a50')
