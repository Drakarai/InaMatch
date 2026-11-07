"""Ojeadores de IE2 (scouts-ie2), tanda 04: dibujados a partir de su retrato de Victory Road (casi ninguno tiene modelo 3D);
claves 'scouts-ie2:<id>'. El perfil y la espalda se deducen de cómo cae cada peinado.
Reutiliza las ayudas de las tandas de IE1 (dome/hl/face de la 09, bowl/gafas/cejas de la 03, messy/longhair de chars)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars import longhair, messy  # noqa: F401
from chars_scouts_ie1_03 import (big_grin, blush, bowl, eyes_custom, fr, freckles, goggles, rect_specs, round_specs,  # noqa: F401
                                 shades, side_brow, side_eye_custom, skull, stache, thick_brows, tri_nose)
from chars_scouts_ie1_09 import _c, dome, face, face_side, hl, mark  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401

K = 'scouts-ie2:'
WHITE = (250, 250, 250, 255)
BLACK = (24, 18, 20, 255)
LIP = (196, 96, 86, 255)
PINK = (238, 140, 150, 255)


def C(pid, body, palette, f, front, side, back):
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2 and f.get('hl_down', True):
        # el nacimiento del pelo baja por el borde de la cara: así su raya no cruza el pelo de los lados
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    f.pop('hl_down', None)
    CHARS[K + pid] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def F(**k):
    d = {'eyes': 'normal', 'mouth': 'line'}
    d.update(k)
    return d


def P(hair, skin, iris='#302232', **k):
    return pal(hair, skin, iris, **k)


def lashes(ey=75, sep=14, c=OUTC):
    """Pestañas: una punta en la esquina de fuera de cada ojo."""
    return [L([(50 - sep - 6, ey - 4), (50 - sep - 10, ey - 7)], c, 'f', False, False, 1.8),
            L([(50 + sep + 6, ey - 4), (50 + sep + 10, ey - 7)], c, 'f', False, False, 1.8)]


def lash_side(ey=75, c=OUTC):
    return [L([(76, ey - 4), (73, ey - 7)], c, 'f', False, False, 1.8)]


def sharp_eyes(iris, ey=75, sep=14):
    """Ojos afilados como capas de delante (para dibujarlos encima de una pintura o antifaz de la cara)."""
    out = []
    for cx, s_ in ((50 - sep, 1), (50 + sep, -1)):
        eye = [(cx - 8 * s_, ey - 4), (cx + 7 * s_, ey - 1.5), (cx + 5.5 * s_, ey + 5), (cx - 6 * s_, ey + 3.5)]
        out += [L(eye, WHITE, 'f', False), L(ell(cx + s_, ey + 1, 3.4, 4.2), iris, 'f', False), L([eye[0], eye[1]], OUTC, 'f', False, False, 3.0)]
    return out


def sharp_eye_side(iris, ey=75):
    eye = [(74, ey - 3.5), (85, ey - 2), (84.5, ey + 5.5), (75, ey + 4.5)]
    return [L(eye, WHITE, 'f', False), L(ell(82, ey + 1.5, 3, 4), iris, 'f', False), L([eye[0], eye[1]], OUTC, 'f', False, False, 3.0)]


def strands_down(x, y0, y1, c='mid', w=2.4, bend=0):
    """Mechón fino que cuelga (de frente)."""
    return L(quad((x, y0), (x + bend, (y0 + y1) / 2), (x + bend * 0.4, y1)), c, 'f', False, False, w)


def band(view, y, h=8, c='band'):
    """Cinta o diadema alrededor de la cabeza a la altura y."""
    if view == 'front':
        return L(blob([(12, y + 4), (30, y - 3), (50, y - 5), (70, y - 3), (88, y + 4), (88, y + 4 + h), (70, y + h - 2), (50, y + h - 4), (30, y + h - 2), (12, y + 4 + h)], 4), c, 'f')
    if view == 'side':
        return L(blob([(4, y + 2), (40, y - 4), (86, y - 2), (88, y + h - 2), (40, y + h - 2), (4, y + h + 4)], 4), c, 'f')
    return L(blob([(8, y + 4), (50, y - 2), (92, y + 4), (92, y + 4 + h), (50, y + h - 2), (8, y + 4 + h)], 4), c, 'f')


# ------------------------------------------------------------------------------------------------------------ jugadores

# Harpo Kendrick: pelo rubio dorado de pinchos revueltos echados a su izquierda, con mechones que le caen por la frente;
# ojos verdes afilados y una máscara antigás gris oscuro que le tapa nariz y boca, con dos filtros redondos
GM, GMD = _c('#4a4d52'), _c('#2e3034')


def _gasmask(view):
    if view == 'front':
        return [L(blob([(30, 80), (50, 76), (70, 80), (72, 96), (58, 108), (42, 108), (28, 96)], 6), GM, 'f'),
                L(ell(50, 96, 7, 6), GMD, 'f'), L(ell(24, 102, 9, 8), GM, 'f'), L(ell(76, 102, 9, 8), GM, 'f'),
                L(ell(24, 102, 4.5, 4), GMD, 'f', False), L(ell(76, 102, 4.5, 4), GMD, 'f', False)]
    if view == 'side':
        return [L(blob([(70, 80), (88, 82), (94, 94), (86, 106), (70, 104)], 6), GM, 'f'), L(ell(88, 102, 7, 7), GM, 'f'),
                L(ell(89, 102, 3.5, 3.5), GMD, 'f', False), L([(70, 86), (46, 78)], GMD, 'f', False, False, 2.2)]
    return [L(quad((8, 82), (50, 88), (92, 82)), GMD, 'f', False, False, 2.4)]


C('harpo-kendrick', 'normal', P('#f8c43c', '#f2c28e', iris='#3a7a3a'),
  F(eyes='sharp', brows='angry', mouth='none', hairline=hl(5, 66, 54, 70, lean=3, jit=3, seed=2)),
  messy('front', amp=16, n=11, seed=7, lo=70, sweep=0.35) + [fr([(34, 46), (42, 74, 1), (48, 50)]), fr([(54, 48), (60, 70, 1), (66, 48)])] + _gasmask('front'),
  messy('side', amp=16, n=11, seed=7, lo=70, sweep=0.35) + _gasmask('side'),
  messy('back', amp=16, n=11, seed=7, lo=70, sweep=0.35) + _gasmask('back'))

# Harpo Thermier: pelo malva liso con un flequillo enorme barrido hacia la derecha de la imagen que acaba en punta hacia
# fuera, dos mechones como cuernos curvados hacia arriba y mechones lisos que caen por los lados hasta la mandíbula;
# piel muy clara, ojos afilados y ceño fruncido
HT = P('#7c616e', '#fdeccc', iris='#3a2a2a')
C('harpo-thermier', 'normal', HT,
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(16, 70), (20, 52), (40, 46), (60, 44), (80, 50), (84, 70)]),
  [L(outline([(14, 96, 1), (10, 60), (14, 30), (30, 12), (50, 6), (72, 12), (88, 30), (90, 60), (86, 96, 1), (80, 64), (20, 64)])),
   L(outline([(26, 14), (8, -6), (18, -22, 1), (22, -4), (34, 10)])), L(outline([(66, 10), (86, -4), (84, -24, 1), (78, -6), (72, 14)])),
   fr([(-14, 62, 1), (12, 44), (30, 30), (56, 26), (78, 34), (84, 46), (64, 48), (46, 58), (30, 68, 1), (24, 60)]),
   L(outline([(60, 8), (84, 24), (90, 56), (86, 90), (80, 60)]), 'shade', 'b', False)],
  [L(outline([(56, 60), (70, 50), (88, 44), (92, 30), (80, 10), (54, 2), (28, 6), (10, 22), (4, 50), (8, 88, 1), (24, 82), (40, 90, 1), (46, 70)])),
   L(outline([(40, 8), (36, -14, 1), (52, 4)])), fr([(64, 20), (98, 30), (82, 44), (66, 44)]),
   L(outline([(6, 40), (30, 44), (40, 84), (22, 80), (8, 84)]), 'shade', 'b', False)],
  [L(outline([(12, 96, 1), (8, 60), (12, 30), (30, 12), (50, 8), (70, 12), (88, 30), (92, 60), (88, 96, 1), (70, 88), (50, 90), (30, 88)])),
   L(outline([(26, 14), (8, -6), (18, -22, 1), (22, -4), (34, 10)])), L(outline([(66, 10), (86, -4), (84, -24, 1), (78, -6), (72, 14)])),
   L(outline([(58, 10), (84, 24), (92, 60), (86, 92), (64, 88)]), 'shade', 'b', False)])

# Harriet Reaching (portera): melena castaña recogida en cuatro moños redondos alrededor de la cabeza, con una diadema
# rosa; gafas de sol rosas de cristal naranja y sonrisa de dientes; piel tostada
HR = P('#6a3410', '#dc9a5c', band='#f07890', lens='#f08a3a', frame='#f07890')


def _harriet_buns(view):
    if view == 'front':
        return [L(ell(6, 26, 13, 12)), L(ell(94, 26, 13, 12)), L(ell(2, 54, 12, 12)), L(ell(98, 54, 12, 12))]
    if view == 'side':
        return [L(ell(40, 0, 13, 12)), L(ell(12, 20, 13, 12)), L(ell(4, 50, 12, 12))]
    return [L(ell(6, 26, 13, 12)), L(ell(94, 26, 13, 12)), L(ell(2, 54, 12, 12)), L(ell(98, 54, 12, 12)), L(ell(50, 66, 12, 10))]


C('harriet-reaching', 'chica', HR,
  F(eyes='none', brows=False, mouth='grin', mouth_y=94, hairline=[(16, 60), (22, 46), (40, 40), (60, 40), (78, 46), (84, 60)]),
  _harriet_buns('front') + dome('front', top=4, w=42, cy=46, sb=58, seed=3) + [band('front', 24, 6)] +
  [L(blob([(22, 70), (46, 70), (46, 82), (24, 82)], 4), 'frame', 'f'), L(blob([(54, 70), (78, 70), (76, 82), (54, 82)], 4), 'frame', 'f'),
   L(blob([(25, 72.5), (43.5, 72.5), (43.5, 79.5), (26.5, 79.5)], 4), 'lens', 'f', False), L(blob([(56.5, 72.5), (75, 72.5), (73.5, 79.5), (56.5, 79.5)], 4), 'lens', 'f', False)],
  _harriet_buns('side') + dome('side', top=4, w=42, cy=46, nape=74, fr=46, seed=3) + [band('side', 24, 6),
   L(blob([(72, 70), (90, 70), (89, 82), (73, 82)], 4), 'frame', 'f'), L(blob([(75, 72.5), (87, 72.5), (86.5, 79.5), (75.5, 79.5)], 4), 'lens', 'f', False),
   L([(72, 74), (50, 70)], 'frame', 'f', False, False, 2.0)],
  _harriet_buns('back') + dome('back', top=4, w=42, cy=46, nape=72, seed=3) + [band('back', 24, 6)])

# Harry Angue: pelo morado peinado hacia atrás pegado al cráneo, con un pico que le baja hasta el centro de la frente y
# mechones finos que le caen por delante de las orejas hasta la mandíbula; ojos grandes oscuros con una raya roja en el
# rabillo y boca seria
HA = P('#6a3c72', '#f6c696', iris='#22202e')
C('harry-angue', 'normal', HA,
  F(eyes='big', brows=False, mouth='frown', mouth_y=94,
    hairline=[(16, 64), (20, 46), (32, 38), (42, 44), (50, 64), (58, 44), (68, 38), (80, 46), (84, 64)]),
  dome('front', top=6, w=40, cy=48, sb=56, seed=1) + [strands_down(17, 56, 100, 'mid', 2.6, -2), strands_down(83, 56, 100, 'mid', 2.6, 2),
   L([(26, 72), (19, 68)], (200, 40, 40, 255), 'f', False, False, 2.2), L([(74, 72), (81, 68)], (200, 40, 40, 255), 'f', False, False, 2.2)],
  dome('side', top=6, w=42, cy=48, nape=84, fr=46, seed=1) + [L(quad((60, 60), (58, 82), (60, 100)), 'mid', 'f', False, False, 2.6)],
  dome('back', top=6, w=42, cy=48, nape=86, seed=1) + [strand([(50, 12), (50, 80)], 'deep', 'b', 1.0)])

# Harry Keenan: melena roja en grandes rollos redondeados (tres por lado) que le enmarcan la cara hasta la mandíbula, con
# el flequillo abierto en medio; piel clara, ojos afilados y unos labios enormes en sonrisa
HK = P('#c4302a', '#ecd8c0', iris='#4a1a1a')


def _rolls(view):
    if view == 'front':
        out = []
        for y in (34, 58, 82):
            out += [L(ell(14, y, 10, 13)), L(ell(86, y, 10, 13))]
        return out
    if view == 'side':
        return [L(ell(28, y, 12, 13)) for y in (36, 60, 84)] + [L(ell(12, y, 10, 13)) for y in (44, 70)]
    out = []
    for y in (40, 64, 88):
        out += [L(ell(16, y, 11, 13)), L(ell(50, y + 4, 14, 13)), L(ell(84, y, 11, 13))]
    return out


C('harry-keenan', 'normal', HK,
  F(eyes='sharp', brows='angry', mouth='lips', mouth_w=14, mouth_y=92, hairline=[(16, 64), (22, 44), (40, 38), (50, 50), (60, 38), (78, 44), (84, 64)]),
  _rolls('front') + dome('front', top=0, w=44, cy=42, sb=60, seed=2) + [fr([(14, 52), (24, 28), (44, 22), (50, 46, 1), (40, 40), (24, 44)]),
                                                                         fr([(86, 52), (76, 28), (56, 22), (50, 46, 1), (60, 40), (76, 44)])],
  _rolls('side') + dome('side', top=0, w=44, cy=42, nape=90, fr=48, seed=2),
  _rolls('back') + dome('back', top=0, w=44, cy=42, nape=80, seed=2))

# Heath Planner: afro azul marino muy oscuro, piel morena, gafas redondas rojas, perilla castaña y labios gruesos
HP = P('#2c3c52', '#9a6a46', iris='#1a1210', beard='#5a3418')
C('heath-planner', 'normal', HP,
  F(eyes='dot', brows=True, mouth='lips', mouth_w=8, mouth_y=93, hairline=[(14, 60), (20, 46), (40, 40), (60, 40), (80, 46), (86, 60)]),
  dome('front', top=-6, w=52, cy=40, n=14, amp=5, soft=True, sb=66, seed=5) + round_specs('front', _c('#e03a2a'), 75, 14, 9, 7.5, 2.4) +
  [L(blob([(42, 98), (58, 98), (56, 106), (44, 106)], 4), 'beard', 'f')],
  dome('side', top=-6, w=52, cy=40, n=14, amp=5, soft=True, nape=86, fr=50, seed=5) + round_specs('side', _c('#e03a2a'), 75, 14, 9, 7.5, 2.4) +
  [L(blob([(78, 98), (88, 98), (86, 106), (78, 104)], 4), 'beard', 'f')],
  dome('back', top=-6, w=52, cy=40, n=14, amp=5, soft=True, nape=86, seed=5))

# Herbie Garnet (portero): pelo malva en media melena lisa con un moño redondo encima; sombra rosa en los párpados,
# pestañas y media sonrisa
HG = P('#7c5a68', '#fad8b4', iris='#2a1a22')
C('herbie-garnet', 'normal', HG,
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=94, hairline=[(16, 66), (20, 48), (36, 42), (56, 44), (76, 40), (84, 52), (84, 66)]),
  [L(ell(52, -6, 10, 9))] + dome('front', top=4, w=44, cy=48, sb=86, seed=4) + [fr([(14, 60), (20, 34), (46, 24), (76, 30), (86, 44), (66, 40), (40, 46), (24, 58)])] +
  lashes() + [L(blob([(24, 66), (44, 68), (40, 71), (26, 70)], 4), PINK, 'f', False), L(blob([(56, 68), (76, 66), (74, 70), (60, 71)], 4), PINK, 'f', False)],
  [L(ell(40, -8, 10, 9))] + dome('side', top=4, w=44, cy=48, nape=92, fr=46, seed=4) + lash_side(),
  [L(ell(50, -6, 10, 9))] + dome('back', top=4, w=44, cy=48, nape=92, seed=4))

# Hide King: retrato de la DS; pelo azul oscuro peinado hacia atrás que le cae largo hasta la nuca, piel tostada, cejas
# muy fruncidas, nariz marcada y boca apretada
HK2 = P('#2a4a72', '#d8a070', iris='#1a1210')
C('hide-king', 'normal', HK2,
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, nose=(50, 86, 2.4), hairline=[(16, 62), (22, 44), (36, 38), (50, 36), (64, 38), (78, 44), (84, 62)]),
  dome('front', top=4, w=44, cy=44, sb=74, seed=6) + [strand([(36, 14), (30, 40)], 'deep', 'b', 1.2), strand([(64, 14), (70, 40)], 'deep', 'b', 1.2)],
  dome('side', top=4, w=44, cy=44, long=100, flare=4, fr=40, seed=6) + [strand([(70, 14), (40, 30), (20, 60)], 'deep', 'b', 1.2)],
  dome('back', top=4, w=44, cy=44, long=100, flare=2, ends=4, seed=6) + [strand([(50, 10), (50, 90)], 'deep', 'b', 1.2)])

# Hilda Bronski: melena lisa naranja oscuro hasta los hombros con la raya en medio, una diadema azul en la frente y una
# venda gris sobre los ojos; sonrisa tranquila
HB = P('#c06a1e', '#f0bf88', band='#6a80c8', blind='#787c84')
C('hilda-bronski', 'chica', HB,
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, hairline=[(16, 60), (24, 44), (50, 38), (76, 44), (84, 60)]),
  longhair('front', length=108, flare=6, top=2, part=True) + [band('front', 46, 10)] +
  [L(blob([(14, 68), (50, 66), (86, 68), (86, 80), (50, 80), (14, 80)], 4), 'blind', 'f')],
  longhair('side', length=108, flare=6, top=2) + [band('side', 46, 10), L(blob([(54, 68), (90, 66), (90, 80), (54, 80)], 4), 'blind', 'f')],
  longhair('back', length=108, flare=6, top=2, part=True, ends=5) + [band('back', 46, 10), L(blob([(8, 70), (92, 70), (92, 80), (8, 80)], 4), 'blind', 'f')])

# Horace Shlock: pelo gris oliva en pinchos revueltos que se abren hacia los lados; la cara pintada de marrón oscuro como
# un antifaz alrededor de los ojos, con rayas naranjas; ojos rojos
HS = P('#6c6648', '#e8a868', iris='#c02a1a', paint='#4a2a1e', stripe='#f0a040')
C('horace-shlock', 'normal', HS,
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, hairline=hl(5, 64, 52, 64, lean=-2, jit=3, seed=9)),
  messy('front', amp=18, n=10, seed=13, lo=66, rx=48) +
  [L(blob([(18, 62), (50, 70), (82, 62), (84, 80), (66, 92), (50, 88), (34, 92), (16, 80)], 6), 'paint', 'f', False),
   L([(22, 86), (30, 76)], 'stripe', 'f', False, False, 2.2), L([(78, 86), (70, 76)], 'stripe', 'f', False, False, 2.2)] + sharp_eyes(_c('#c02a1a')),
  messy('side', amp=18, n=10, seed=13, lo=66, rx=48) + [L(blob([(66, 64), (88, 66), (88, 86), (70, 90)], 6), 'paint', 'f', False),
                                                        L([(72, 90), (76, 82)], 'stripe', 'f', False, False, 2.2)] + sharp_eye_side(_c('#c02a1a')),
  messy('back', amp=18, n=10, seed=13, lo=66, rx=48))

# Hugh Dunnit (portero): gorra plana grande verde a cuadros amarillos, con el pelo rubio claro asomando en mechones por
# los lados; ojos castaños grandes y sonrisa
HD = P('#f2e2aa', '#fbe6c8', iris='#7a4a1a', cap='#4a8a2a', check='#d8c83a')


def _flatcap(view):
    if view == 'front':
        return [L(blob([(2, 44), (10, 18), (36, 4), (66, 4), (92, 16), (100, 40), (90, 52), (50, 48), (10, 52)], 8), 'cap', 'f'),
                L([(24, 10), (16, 48)], 'check', 'f', False, False, 2.0), L([(46, 4), (42, 48)], 'check', 'f', False, False, 2.0),
                L([(70, 6), (72, 48)], 'check', 'f', False, False, 2.0), L(quad((6, 26), (50, 18), (96, 26)), 'check', 'f', False, False, 2.0)]
    if view == 'side':
        return [L(blob([(0, 40), (8, 12), (40, -2), (76, 4), (98, 26), (96, 40), (60, 40), (20, 46)], 8), 'cap', 'f'),
                L([(30, 2), (26, 42)], 'check', 'f', False, False, 2.0), L([(62, 2), (64, 40)], 'check', 'f', False, False, 2.0),
                L(quad((4, 24), (50, 14), (96, 28)), 'check', 'f', False, False, 2.0)]
    return [L(blob([(2, 46), (10, 18), (36, 4), (66, 4), (92, 16), (98, 46), (50, 54)], 8), 'cap', 'f'),
            L([(30, 8), (26, 50)], 'check', 'f', False, False, 2.0), L([(70, 8), (74, 50)], 'check', 'f', False, False, 2.0),
            L(quad((4, 30), (50, 22), (96, 30)), 'check', 'f', False, False, 2.0)]


C('hugh-dunnit', 'normal', HD,
  F(eyes='big', brows=True, mouth='smile', mouth_y=94, hairline=[(16, 62), (24, 50), (50, 48), (76, 50), (84, 62)]),
  dome('front', top=10, w=42, cy=50, sb=74, seed=2) + [fr([(14, 72), (16, 50), (30, 46), (26, 70, 1), (22, 56)]), fr([(86, 72), (84, 50), (70, 46), (74, 70, 1), (78, 56)])] +
  _flatcap('front'),
  dome('side', top=10, w=42, cy=50, nape=86, fr=50, seed=2) + _flatcap('side'),
  dome('back', top=10, w=42, cy=50, nape=86, seed=2) + _flatcap('back'))

# Hugh Tinter (portero): pelo verde azulado muy oscuro en pinchos que salen hacia los lados y mechones de punta por la
# frente; ojos afilados y ceño
HTI = P('#1c4c50', '#f0bb84', iris='#1a1210')
C('hugh-tinter', 'normal', HTI,
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=hl(5, 64, 52, 68, lean=-1, jit=4, seed=4)),
  messy('front', amp=13, n=10, seed=21, lo=64, rx=48, sweep=-0.25) + [fr([(40, 44), (46, 70, 1), (52, 48)])],
  messy('side', amp=13, n=10, seed=21, lo=64, rx=48, sweep=-0.25),
  messy('back', amp=13, n=10, seed=21, lo=64, rx=48, sweep=-0.25))

# Iain Igma: pelo rubio dorado liso en casco, con un flequillo de mechones de punta que le tapa media frente; ojos
# grandes oscuros, unas rayitas en las mejillas y boca seria
II = P('#e0a822', '#f6c896', iris='#1a1210')
C('iain-igma', 'normal', II,
  F(eyes='big', brows=False, mouth='frown', mouth_y=94, hairline=False),
  bowl('front', top=4, side=74) + [fr([(14, 62), (18, 36), (40, 24), (64, 24), (86, 38), (86, 62), (78, 54), (72, 68, 1), (64, 54), (56, 70, 1), (48, 54), (40, 72, 1),
                                        (32, 56), (24, 68, 1), (20, 56)])] +
  [L([(24, 86), (30, 84)], OUTC, 'f', False, False, 1.0), L([(24, 89), (30, 87)], OUTC, 'f', False, False, 1.0),
   L([(76, 86), (70, 84)], OUTC, 'f', False, False, 1.0), L([(76, 89), (70, 87)], OUTC, 'f', False, False, 1.0)],
  bowl('side', top=4, nape=88) + [fr([(66, 24), (92, 40), (88, 62, 1), (80, 50), (72, 46)])],
  bowl('back', top=4, nape=88))

# Ian Eel-Moray: piel morena; pelo gris oscuro peinado hacia atrás, con dos mechones que salen hacia los lados como
# aletas y dos mechones finos que le caen largos por delante de las orejas; ojos azules afilados, puntos en la frente y
# boca de dientes en zigzag
IE = P('#4a4e58', '#9a7254', iris='#3a8ac0', fin='#7a7e88')


def _zigzag(y=96):
    pts = [(40, y)]
    for i in range(6):
        pts.append((42 + i * 3.2, y + (3 if i % 2 == 0 else -1)))
    return [L(blob([(38, y - 3), (62, y - 3), (60, y + 5), (40, y + 5)], 4), WHITE, 'f', True), L(pts + [(60, y)], OUTC, 'f', False, False, 1.2)]


C('ian-eel-moray', 'normal', IE,
  F(eyes='sharp', brows=False, mouth='none', hairline=[(16, 62), (22, 44), (36, 36), (50, 46), (64, 36), (78, 44), (84, 62)]),
  [L(outline([(16, 40), (-6, 30), (-10, 38, 1), (8, 52)]), 'fin'), L(outline([(84, 40), (106, 30), (110, 38, 1), (92, 52)]), 'fin')] +
  dome('front', top=6, w=40, cy=48, sb=56, seed=3) + [strands_down(20, 60, 110, 'mid', 2.6, -3), strands_down(80, 60, 110, 'mid', 2.6, 3)] +
  [L(ell(44, 58, 1.2, 1.2), OUTC, 'f', False), L(ell(56, 58, 1.2, 1.2), OUTC, 'f', False), L(ell(50, 54, 1.2, 1.2), OUTC, 'f', False)] + _zigzag(96),
  dome('side', top=6, w=42, cy=48, nape=84, fr=46, seed=3) + [L(outline([(30, 38), (2, 24), (-6, 32, 1), (20, 50)]), 'fin', 'f')] +
  [L(quad((62, 62), (60, 90), (64, 110)), 'mid', 'f', False, False, 2.6), L(blob([(80, 94), (88, 94), (88, 99), (80, 99)], 4), WHITE, 'f', True)],
  [L(outline([(16, 40), (-6, 30), (-10, 38, 1), (8, 52)]), 'fin'), L(outline([(84, 40), (106, 30), (110, 38, 1), (92, 52)]), 'fin')] +
  dome('back', top=6, w=42, cy=48, nape=86, seed=3))

# Ian Fantile (bajito): pelo castaño rojizo corto que se abre en mechones hacia los lados, con un flequillo recto
# corto; orejas grandes, ojos de puntito, cejas preocupadas y boca pequeña ondulada
IF = P('#8a3a12', '#f6c690', iris='#1a1210')
C('ian-fantile', 'bajito', IF,
  F(eyes='dot', brows=False, mouth='none', big_ears=3, ear_out=3, hairline=[(16, 58), (22, 52), (40, 56), (60, 56), (78, 52), (84, 58)]),
  dome('front', top=2, w=50, cy=40, n=9, amp=7, soft=True, sb=58, seed=11) +
  [L([(28, 66), (40, 62)], OUTC, 'f', False, False, 2.0), L([(72, 66), (60, 62)], OUTC, 'f', False, False, 2.0),
   L([(44, 94), (47, 92), (50, 94), (53, 92), (56, 94)], (130, 70, 50, 255), 'f', False, False, 1.4)],
  dome('side', top=2, w=50, cy=40, n=9, amp=7, soft=True, nape=78, fr=54, seed=11),
  dome('back', top=2, w=50, cy=40, n=9, amp=7, soft=True, nape=78, seed=11))

# Ian Watchen: coleta alta castaño rojizo atada con una goma azul que cae por detrás, y un mechón largo que le cruza la
# cara; cejas gruesas fruncidas, ojos azules afilados
IW = P('#8a3218', '#f4c890', iris='#3a6ac8', tie='#5a7ad0')
C('ian-watchen', 'normal', IW,
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=[(16, 60), (22, 46), (40, 40), (60, 40), (78, 46), (84, 60)]),
  [L(outline([(40, 4), (24, -14), (6, 10), (-4, 50, 1), (8, 30), (22, 10), (34, 14)]))] + dome('front', top=2, w=42, cy=46, sb=64, seed=8) +
  [L(ell(42, 0, 5, 4), 'tie', 'f'), fr([(46, 30), (60, 50), (72, 80), (76, 100, 1), (66, 80), (52, 54), (40, 40)])] + thick_brows(64, OUTC, 3.2, 14, 1.6, 13),
  [L(outline([(36, 2), (8, 4), (-8, 40), (-12, 90, 1), (2, 50), (14, 20), (30, 16)]))] + dome('side', top=2, w=42, cy=46, nape=80, fr=46, seed=8) +
  [L(ell(32, 4, 5, 5), 'tie', 'f'), fr([(80, 40), (90, 60), (88, 90, 1), (82, 60)])],
  dome('back', top=2, w=42, cy=46, nape=80, seed=8) + [L(outline([(42, 4), (58, 4), (60, 50), (50, 100, 1), (40, 50)])), L(ell(50, 6, 6, 4), 'tie', 'f')])

# In Chikita: afro enorme castaño muy oscuro, cara alargada, gafas de aviador blancas de cristal marrón, nariz larga y
# sonrisa
C('in-chikita', 'normal', P('#3c3826', '#f0b878', lens='#7a3a1a'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=98, nose=(50, 88, 2.2), hairline=[(16, 60), (22, 46), (40, 40), (60, 40), (78, 46), (84, 60)],
    face_front=face(chin=108)),
  dome('front', top=-12, w=58, cy=40, n=16, amp=5, soft=True, sb=72, seed=17) +
  [L(blob([(22, 70), (46, 70), (44, 84), (26, 84)], 4), WHITE, 'f'), L(blob([(54, 70), (78, 70), (74, 84), (56, 84)], 4), WHITE, 'f'),
   L(blob([(26, 73), (43, 73), (41.5, 81), (28, 81)], 4), 'lens', 'f', False), L(blob([(57, 73), (74, 73), (72, 81), (58.5, 81)], 4), 'lens', 'f', False)],
  dome('side', top=-12, w=58, cy=40, n=16, amp=5, soft=True, nape=92, fr=54, seed=17) +
  [L(blob([(72, 70), (90, 70), (88, 84), (74, 84)], 4), WHITE, 'f'), L(blob([(75, 73), (87, 73), (85.5, 81), (76, 81)], 4), 'lens', 'f', False),
   L([(72, 74), (50, 70)], WHITE, 'f', False, False, 2.0)],
  dome('back', top=-12, w=58, cy=40, n=16, amp=5, soft=True, nape=92, seed=17))

# Irving Gusher: pelo castaño anaranjado con un pañuelo crema anudado sobre la frente; un mechón rizado hacia fuera a la
# izquierda y el pelo cae liso por los lados; ojos castaños afilados y ceño
C('irving-gusher', 'normal', P('#c07a20', '#ecac6c', iris='#7a2a1a', band='#f2e6c8'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=[(16, 64), (20, 52), (40, 52), (60, 52), (80, 52), (84, 64)]),
  dome('front', top=0, w=44, cy=46, sb=72, seed=19) + [L(blob([(14, 50), (24, 34), (50, 28), (76, 34), (86, 50), (78, 56), (50, 52), (22, 56)], 6), 'band', 'f'),
   fr([(18, 56), (2, 52), (-2, 42, 1), (6, 50), (16, 48)]), fr([(80, 50), (90, 62), (86, 76, 1), (82, 60)])],
  dome('side', top=0, w=44, cy=46, nape=86, fr=50, seed=19) + [L(blob([(30, 32), (60, 26), (88, 36), (88, 50), (60, 44), (30, 46)], 6), 'band', 'f'),
   L(outline([(28, 36), (8, 30), (4, 44, 1), (20, 46)]), 'band', 'f')],
  dome('back', top=0, w=44, cy=46, nape=86, seed=19) + [L(blob([(10, 46), (50, 36), (90, 46), (90, 56), (50, 48), (10, 56)], 6), 'band', 'f'),
   L(outline([(46, 50), (36, 66, 1), (50, 56), (64, 66, 1), (54, 50)]), 'band', 'f')])

# Isabell Mish: rubia con una trenza que le rodea la cabeza como una corona y la melena que cae hasta los hombros con las
# puntas hacia fuera; ojos azules entornados, coloretes y sonrisa
IM = P('#e0b024', '#f6c898', iris='#3a4a9a')


def _braid_crown(view):
    if view == 'front':
        out = [L(blob([(14, 50), (20, 30), (36, 18), (50, 16), (64, 18), (80, 30), (86, 50), (78, 46), (64, 30), (50, 28), (36, 30), (22, 46)], 6), 'shade', 'f')]
        for x, y in ((20, 42), (26, 30), (36, 23), (50, 21), (64, 23), (74, 30), (80, 42)):
            out.append(L([(x - 3, y - 3), (x + 3, y + 3)], 'deep', 'f', False, False, 1.2))
        return out
    if view == 'side':
        return [L(blob([(30, 18), (60, 14), (84, 30), (86, 48), (78, 44), (60, 28), (34, 28)], 6), 'shade', 'f')]
    return [L(blob([(10, 50), (20, 26), (50, 16), (80, 26), (90, 50), (80, 44), (50, 28), (20, 44)], 6), 'shade', 'f')]


C('isabell-mish', 'chica', IM,
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=94, hairline=[(16, 60), (22, 46), (40, 42), (60, 42), (78, 46), (84, 60)]),
  longhair('front', length=104, flare=12, top=4) + _braid_crown('front') + blush(84, 22, 3.6),
  longhair('side', length=104, flare=12, top=4) + _braid_crown('side'),
  longhair('back', length=104, flare=12, top=4, ends=5) + _braid_crown('back'))

# Isla Pullens (portera): gorra roja y una mata de pelo crema esponjoso que le sale hacia los lados; piel morena, cara
# alargada, ojos blancos redondos y una sonrisa enorme de dientes
C('isla-pullens', 'chica', P('#e8d2a0', '#9a7048', cap='#d8282a', capd='#a81a1e'),
  F(eyes='round', brows=False, mouth='none', hairline=False, face_front=face(chin=108, jaw=2)),
  [L(blob([(-4, 50), (0, 34), (14, 30), (20, 44), (16, 66), (2, 66)], 6)), L(blob([(104, 50), (100, 34), (86, 30), (80, 44), (84, 66), (98, 66)], 6))] +
  [L(blob([(16, 50), (16, 26), (30, 12), (50, 8), (70, 12), (84, 26), (84, 50), (50, 46)], 8), 'cap', 'f'),
   L(blob([(60, 12), (78, 20), (84, 40), (76, 44)], 6), 'capd', 'f', False)] + big_grin(92, 16, 12),
  [L(blob([(4, 50), (6, 30), (24, 30), (36, 50), (26, 72), (8, 70)], 6)),
   L(blob([(14, 40), (20, 16), (50, 6), (80, 14), (90, 34), (100, 42), (90, 46), (50, 44)], 8), 'cap', 'f')],
  [L(blob([(-4, 50), (0, 34), (50, 30), (100, 34), (104, 50), (98, 70), (50, 74), (2, 70)], 6)),
   L(blob([(14, 50), (16, 24), (34, 10), (50, 8), (66, 10), (84, 24), (86, 50), (50, 54)], 8), 'cap', 'f')])

# James Hearson: piel morena; pelo crema en mechones abiertos a los lados como una melena erizada; una diadema de
# auriculares morada y unas gafas de visera moradas con el borde verde que le tapan los ojos
JH = P('#f0e0aa', '#a8744c', band='#3a2a6a', visor='#3a2a5a', rim='#3ac860')
C('james-hearson', 'normal', JH,
  F(eyes='none', brows=False, mouth='line', mouth_y=96, hairline=[(16, 58), (24, 44), (50, 36), (76, 44), (84, 58)]),
  [L(outline([(16, 56), (-12, 58, 1), (4, 46), (-10, 36, 1), (10, 30), (24, 10), (50, 4), (76, 10), (90, 30), (110, 36, 1), (96, 46), (112, 58, 1), (84, 56), (84, 48),
              (16, 48)]))] + [L(quad((14, 60), (50, -6), (86, 60)), 'band', 'f', False, False, 3.2),
   L(blob([(10, 70), (50, 66), (90, 70), (88, 84), (60, 86), (50, 80), (40, 86), (12, 84)], 6), 'visor', 'f'),
   L([(18, 82), (40, 82), (50, 76), (60, 82), (82, 82)], 'rim', 'f', False, False, 2.2)],
  [L(outline([(56, 52), (66, 44), (84, 40), (90, 24), (70, 4), (40, 2), (14, 12), (-8, 30, 1), (8, 40), (-6, 56, 1), (10, 58), (22, 70, 1), (34, 58), (46, 56)])),
   L(quad((44, 72), (40, 20), (60, -2)), 'band', 'f', False, False, 3.2), L(blob([(66, 68), (92, 68), (92, 84), (68, 84)], 6), 'visor', 'f')],
  [L(outline([(10, 60), (-12, 60, 1), (4, 46), (-10, 36, 1), (10, 30), (24, 10), (50, 4), (76, 10), (90, 30), (110, 36, 1), (96, 46), (112, 60, 1), (90, 60), (70, 70, 1),
              (50, 62), (30, 70, 1)])), L(quad((10, 64), (50, -6), (90, 64)), 'band', 'f', False, False, 3.2)])

# James Strang: pelo gris oliva rapado muy corto, pegado a la coronilla; piel tostada, orejas grandes, ojos verde azulado
# afilados y cejas fruncidas
C('james-strang', 'normal', P('#6c6a52', '#d89a62', iris='#2a7a7a'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=95, big_ears=2, hairline=[(18, 58), (24, 44), (40, 38), (50, 36), (60, 38), (76, 44), (82, 58)]),
  [L(blob([(18, 58), (20, 30), (34, 12), (50, 8), (66, 12), (80, 30), (82, 58), (50, 44)], 8)),
   L(blob([(60, 12), (78, 26), (82, 50), (72, 44)], 6), 'shade', 'b', False)],
  [L(blob([(56, 54), (66, 40), (82, 34), (80, 18), (56, 6), (30, 8), (12, 22), (6, 46), (12, 70), (30, 66), (44, 58)], 8))],
  [L(blob([(14, 62), (16, 30), (32, 12), (50, 8), (68, 12), (84, 30), (86, 62), (70, 70), (50, 72), (30, 70)], 8))])

# Jan Jared: sombrero de seta rojo con lunares naranjas; debajo, pelo verde corto en mechones de punta que salen por los
# lados; ojos grandes rojos, coloretes y sonrisa
JJ = P('#78b838', '#fbe2c0', iris='#c8282a', cap='#c8302a', dot='#f0a070')


def _mushroom(view):
    if view == 'front':
        return [L(blob([(-6, 50), (4, 18), (26, 0), (50, -6), (74, 0), (96, 18), (106, 50), (50, 44)], 8), 'cap', 'f'),
                L(ell(50, 6, 6, 5), 'dot', 'f', False), L(ell(22, 24, 6, 6), 'dot', 'f', False), L(ell(78, 24, 6, 6), 'dot', 'f', False),
                L(ell(4, 42, 4, 5), 'dot', 'f', False), L(ell(96, 42, 4, 5), 'dot', 'f', False), L(ell(40, 34, 4, 4), 'dot', 'f', False), L(ell(62, 34, 4, 4), 'dot', 'f', False)]
    if view == 'side':
        return [L(blob([(-8, 50), (2, 16), (30, -4), (60, -6), (90, 12), (104, 46), (50, 42)], 8), 'cap', 'f'),
                L(ell(40, 6, 6, 5), 'dot', 'f', False), L(ell(14, 24, 6, 6), 'dot', 'f', False), L(ell(76, 20, 6, 6), 'dot', 'f', False), L(ell(56, 34, 4, 4), 'dot', 'f', False)]
    return [L(blob([(-6, 50), (4, 18), (26, 0), (50, -6), (74, 0), (96, 18), (106, 50), (50, 56)], 8), 'cap', 'f'),
            L(ell(50, 10, 6, 5), 'dot', 'f', False), L(ell(22, 26, 6, 6), 'dot', 'f', False), L(ell(78, 26, 6, 6), 'dot', 'f', False), L(ell(50, 38, 5, 4), 'dot', 'f', False)]


C('jan-jared', 'chica', JJ,
  F(eyes='big', brows=False, mouth='smile', mouth_y=94, hairline=hl(5, 62, 52, 62, jit=2, seed=5)),
  [L(outline([(16, 60), (2, 66, 1), (10, 50), (16, 40), (84, 40), (90, 50), (98, 66, 1), (84, 60)]))] + _mushroom('front') + blush(86, 22, 3.6) +
  [fr([(20, 46), (30, 64, 1), (38, 46), (46, 62, 1), (54, 46), (62, 62, 1), (70, 46), (78, 64, 1), (84, 46)])],
  [L(outline([(54, 56), (64, 46), (86, 44), (80, 30), (20, 30), (6, 50), (2, 70, 1), (20, 66), (30, 80, 1), (44, 62)]))] + _mushroom('side'),
  [L(outline([(10, 50), (2, 68, 1), (20, 64), (34, 76, 1), (50, 66), (66, 76, 1), (80, 64), (98, 68, 1), (90, 50)]))] + _mushroom('back'))

# Jane Ledbelly: media melena castaña grisácea lisa con la raya a un lado; orejas grandes, ojos castaños grandes y la boca
# en una o de sorpresa
C('jane-ledbelly', 'chica', P('#7c6a5a', '#f4c48e', iris='#7a4a1a'),
  F(eyes='big', brows=True, mouth='none', big_ears=2, hairline=[(16, 64), (20, 48), (34, 40), (44, 46), (60, 42), (80, 48), (84, 64)]),
  bowl('front', top=4, side=70) + [fr([(14, 60), (18, 36), (36, 20), (60, 18), (80, 28), (86, 44), (66, 40), (46, 48), (30, 54)])] +
  [L(ell(50, 96, 2.8, 3.4), (110, 40, 40, 255), 'f', True)],
  bowl('side', top=4, nape=84),
  bowl('back', top=4, nape=84))

# Jarmon Fisk: pelo castaño esponjoso en grandes rizos abultados; pecas, ojos grandes y boca seria
C('jarmon-fisk', 'normal', P('#8c5a2a', '#f6c496', iris='#4a3a2a'),
  F(eyes='big', brows='angry', mouth='frown', mouth_y=95, hairline=[(14, 58), (22, 46), (40, 44), (60, 44), (78, 46), (86, 58)]),
  dome('front', top=-8, w=54, cy=36, n=10, amp=8, soft=True, sb=62, seed=25) + freckles(86, 24),
  dome('side', top=-8, w=54, cy=36, n=10, amp=8, soft=True, nape=80, fr=50, seed=25),
  dome('back', top=-8, w=54, cy=36, n=10, amp=8, soft=True, nape=80, seed=25))

# Jasmin Trier: recogido de geisha morado oscuro (un moño alto enorme) con una flor roja y una horquilla dorada; piel muy
# blanca, ojos morados con raya roja y boca pequeña sonriente
JT = P('#3a2a6a', '#fbf2e2', iris='#4a3a8a', flower='#f04a2a', gold='#f0c040')


def _geisha(view):
    flower = [L(ell(76, 6, 7, 7), 'flower', 'f'), L(ell(76, 6, 2.6, 2.6), 'gold', 'f', False), L(blob([(72, 12), (80, 12), (80, 22), (72, 22)], 2), 'gold', 'f')]
    if view == 'front':
        return [L(ell(50, 4, 28, 18)), L(blob([(10, 64), (8, 38), (22, 20), (50, 14), (78, 20), (92, 38), (90, 64), (80, 52), (20, 52)], 8)),
                L(blob([(60, -10), (76, 0), (78, 16), (66, 14)], 6), 'shade', 'b', False)] + flower
    if view == 'side':
        return [L(ell(40, 0, 26, 18)), L(blob([(56, 54), (66, 44), (86, 40), (80, 18), (50, 10), (20, 16), (6, 40), (10, 70), (28, 72), (44, 60)], 8)),
                L(ell(14, 66, 12, 10))] + [L(ell(60, 2, 7, 7), 'flower', 'f'), L(ell(60, 2, 2.6, 2.6), 'gold', 'f', False)]
    return [L(ell(50, 4, 28, 18)), L(blob([(10, 64), (8, 38), (22, 20), (50, 14), (78, 20), (92, 38), (90, 64), (70, 76), (50, 78), (30, 76)], 8)),
            L(ell(50, 72, 16, 10))] + [L(ell(24, 6, 7, 7), 'flower', 'f'), L(ell(24, 6, 2.6, 2.6), 'gold', 'f', False)]


C('jasmin-trier', 'chica', JT,
  F(eyes='big', brows=True, mouth='smile', mouth_y=94, hairline=[(16, 60), (22, 48), (36, 44), (50, 50), (64, 44), (78, 48), (84, 60)]),
  _geisha('front') + [L([(26, 76), (20, 72)], (210, 50, 40, 255), 'f', False, False, 2.2), L([(74, 76), (80, 72)], (210, 50, 40, 255), 'f', False, False, 2.2)],
  _geisha('side'),
  _geisha('back'))

# Jasmine Veile: melena granate en corte hime con flequillo recto, un mechón en espiral encima y dos trenzas bajas a los
# lados; ojos azules grandes, coloretes naranjas y sonrisa
JV = P('#6a1a2c', '#fbdcc0', iris='#3a8ac8')
C('jasmine-veile', 'chica', JV,
  F(eyes='big', brows=False, mouth='smile', mouth_y=94, hairline=False),
  longhair('front', length=92, flare=0, top=2) + [L(outline([(48, 4), (40, -12), (54, -20), (66, -12), (58, -6), (52, -12, 1), (50, 2)])),
   fr([(14, 64), (16, 36), (32, 20), (50, 16), (68, 20), (84, 36), (86, 64), (80, 64), (80, 60), (20, 60), (20, 64)])] +
  [L(ell(14, 96, 6, 7)), L(ell(16, 108, 5, 6)), L(ell(86, 96, 6, 7)), L(ell(84, 108, 5, 6))] + blush(86, 24, 4.4),
  longhair('side', length=92, flare=0, top=2) + [L(outline([(40, 0), (34, -14), (48, -22), (58, -12), (46, -10, 1), (46, 2)])), L(ell(56, 98, 6, 7)), L(ell(54, 110, 5, 6))],
  longhair('back', length=92, flare=0, top=2, ends=3) + [L(outline([(48, 4), (40, -12), (54, -20), (66, -12), (58, -6), (52, -12, 1), (50, 2)])),
                                                          L(ell(16, 98, 6, 7)), L(ell(84, 98, 6, 7))])

# Jay Asher: sombrero de paja cónico muy ancho; ojos cerrados, orejas grandes de lóbulo largo, un bigotito y perilla gris
C('jay-asher', 'normal', P('#5a4a3a', '#f0b26e', hat='#c8a060', hatd='#9a7a44'),
  F(eyes='closed', brows=False, mouth='line', mouth_y=96, big_ears=4, ear_out=2, hairline=(56, 54)),
  [L(blob([(-14, 54), (8, 30), (30, 14), (50, 10), (70, 14), (92, 30), (114, 54), (50, 50)], 8), 'hat', 'f'),
   L([(28, 34), (72, 34)], 'hatd', 'f', False, False, 1.2), L([(40, 26), (40, 44)], 'hatd', 'f', False, False, 1.2), L([(60, 26), (60, 44)], 'hatd', 'f', False, False, 1.2),
   L(blob([(42, 92), (50, 90), (58, 92), (54, 96), (46, 96)], 4), (120, 120, 120, 255), 'f', False)],
  [L(blob([(-18, 54), (4, 28), (40, 8), (70, 12), (100, 32), (118, 54), (50, 50)], 8), 'hat', 'f'), L([(30, 30), (70, 30)], 'hatd', 'f', False, False, 1.2)],
  [L(blob([(-14, 54), (8, 30), (30, 14), (50, 10), (70, 14), (92, 30), (114, 54), (50, 60)], 8), 'hat', 'f'), L([(28, 34), (72, 34)], 'hatd', 'f', False, False, 1.2)])

# Jerry Bateman: media melena morado grisáceo con un flequillo largo que le tapa el ojo izquierdo (derecha de la imagen
# no), puntas hacia fuera; ojos castaños entornados y sonrisa
C('jerry-bateman', 'normal', P('#7a5a6c', '#f8c48c', iris='#5a3a2a'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=95, hairline=[(16, 64), (20, 48), (40, 44), (60, 44), (80, 48), (84, 64)]),
  dome('front', top=2, w=46, cy=46, sb=86, seed=29) + [fr([(-6, 36, 1), (18, 28), (44, 20), (70, 26), (84, 40), (66, 44), (58, 70), (52, 92, 1), (44, 70), (34, 50), (22, 42)]),
   fr([(84, 70), (94, 86, 1), (86, 86)])],
  dome('side', top=2, w=46, cy=46, nape=92, fr=46, seed=29) + [fr([(66, 22), (96, 36), (86, 60), (80, 76, 1), (76, 54), (68, 44)])],
  dome('back', top=2, w=46, cy=46, nape=92, seed=29))

# Jess Winkles: pelo rosa salmón con flequillo recto, mechones largos que caen por delante de los hombros y un lazo enorme
# encima; ojos pequeños redondos y sonrisa
JW = P('#e86a6a', '#fbd6b4', iris='#1a1210')
C('jess-winkles', 'chica', JW,
  F(eyes='round', brows=False, mouth='smile', mouth_y=94, hairline=False),
  [L(outline([(48, 10), (18, -10), (14, -4, 1), (36, 12)])), L(outline([(52, 10), (82, -10), (86, -4, 1), (64, 12)]))] +
  dome('front', top=6, w=44, cy=48, sb=70, seed=31) + [fr([(14, 64), (16, 36), (32, 22), (50, 18), (68, 22), (84, 36), (86, 64), (20, 64)]),
   fr([(14, 60), (20, 60), (24, 112, 1), (16, 104)]), fr([(86, 60), (80, 60), (76, 112, 1), (84, 104)])],
  [L(outline([(44, 8), (24, -12), (18, -6, 1), (34, 12)]))] + dome('side', top=6, w=44, cy=48, nape=86, fr=60, seed=31) + [fr([(56, 60), (62, 60), (64, 112, 1), (56, 104)])],
  [L(outline([(48, 10), (18, -10), (14, -4, 1), (36, 12)])), L(outline([(52, 10), (82, -10), (86, -4, 1), (64, 12)]))] + dome('back', top=6, w=44, cy=48, nape=90, seed=31))

# Jesse Spiller: pelo naranja rojizo con tres moños retorcidos como cuernos (uno en medio en espiral y dos a los lados) y
# mechones de punta por la frente; orejas grandes, un parche redondo morado en un ojo, sonrisa torcida
JS = P('#d84a12', '#f0b674', iris='#1a1210', patch='#3a2048')
C('jesse-spiller', 'normal', JS,
  F(eyes='sharp', brows=False, mouth='none', big_ears=4, ear_out=4, hairline=hl(5, 60, 48, 60, jit=3, seed=12)),
  [L(outline([(42, 8), (46, -14), (52, -24, 1), (58, -10), (60, 8)])), L(ell(18, 18, 9, 8)), L(ell(82, 18, 9, 8)),
   L(outline([(10, 18), (2, 12, 1), (12, 12)])), L(outline([(90, 18), (98, 12, 1), (88, 12)]))] +
  dome('front', top=4, w=42, cy=46, sb=58, seed=12) + [strand([(46, -10), (54, -6), (48, 2)], 'deep', 'f', 1.0),
   L(ell(36, 76, 9, 9), 'patch', 'f'), L([(26, 70), (12, 64)], 'patch', 'f', False, False, 1.6),
   L([(42, 96), (46, 94), (50, 96), (54, 94), (58, 92)], (130, 70, 50, 255), 'f', False, False, 1.4)],
  [L(outline([(34, 6), (36, -16), (42, -26, 1), (48, -12), (52, 6)])), L(ell(20, 16, 9, 8))] + dome('side', top=4, w=42, cy=46, nape=80, fr=48, seed=12) +
  [L([(84, 74), (40, 64)], 'patch', 'f', False, False, 1.6)],
  [L(outline([(42, 8), (46, -14), (52, -24, 1), (58, -10), (60, 8)])), L(ell(18, 18, 9, 8)), L(ell(82, 18, 9, 8))] + dome('back', top=4, w=42, cy=46, nape=80, seed=12) +
  [L(quad((8, 66), (50, 60), (92, 66)), 'patch', 'f', False, False, 1.6)])

# Jim Bunner (portero, grandullón): cara redonda enorme y morena; un gorro gris con unas gafas de buceo de cristal verde
# sobre la frente que le tapan los ojos; nariz chata y boca pequeña
JB = P('#5a6a72', '#b07442', cap='#5a6a72', frame='#d8d4d8', lens='#3a6a2a')
C('jim-bunner', 'corpulento', JB,
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, ear_out=6, hairline=False, nose=(50, 88, 2.0),
    face_front=blob([(12, 56), (50, 40), (88, 56), (96, 80), (86, 102), (50, 112), (14, 102), (4, 80)])),
  [L(blob([(14, 62), (16, 36), (32, 24), (50, 20), (68, 24), (84, 36), (86, 62), (50, 56)], 8), 'cap'),
   L(blob([(10, 58), (50, 52), (90, 58), (90, 74), (50, 72), (10, 74)], 6), 'frame', 'f'),
   L(ell(36, 64, 7, 6), 'lens', 'f', False), L(ell(64, 64, 7, 6), 'lens', 'f', False)],
  [L(blob([(56, 54), (70, 40), (86, 36), (80, 22), (56, 14), (30, 18), (12, 34), (10, 56), (30, 62)], 8), 'cap'),
   L(blob([(20, 50), (60, 50), (92, 54), (92, 72), (60, 70), (20, 66)], 6), 'frame', 'f'), L(ell(84, 62, 6, 6), 'lens', 'f', False)],
  [L(blob([(12, 66), (14, 34), (32, 20), (50, 16), (68, 20), (86, 34), (88, 66), (50, 72)], 8), 'cap'),
   L(blob([(8, 58), (50, 54), (92, 58), (92, 70), (50, 68), (8, 70)], 6), 'frame', 'f')])

# Jimmy Brim: capucha de animal azul verdoso (con orejas redondas y una cara de oso pintada encima) de la que cuelgan dos
# cordones largos con bolas; flequillo naranja; coloretes rosas enormes, ojos como dos rayas negras y boca triste
JBR = P('#f07a1a', '#fbe0c0', hood='#2a7a8c', hoodd='#1e5a6a')


def _bearhood(view):
    if view == 'front':
        return [L(ell(16, 2, 10, 9), 'hood', 'f'), L(ell(84, 2, 10, 9), 'hood', 'f'), L(ell(16, 2, 5, 4), PINK, 'f', False), L(ell(84, 2, 5, 4), PINK, 'f', False),
                L(blob([(8, 70), (6, 36), (20, 12), (50, 4), (80, 12), (94, 36), (92, 70), (82, 56), (80, 42), (50, 34), (20, 42), (18, 56)], 8), 'hood', 'f'),
                L([(36, 18), (42, 16)], OUTC, 'f', False, False, 1.2), L([(58, 16), (64, 18)], OUTC, 'f', False, False, 1.2), L(quad((42, 24), (50, 28), (58, 24)), OUTC, 'f', False, False, 1.2),
                L([(12, 70), (10, 100)], 'hoodd', 'f', False, False, 3), L([(88, 70), (90, 100)], 'hoodd', 'f', False, False, 3),
                L(ell(10, 104, 6, 6), 'hood', 'f'), L(ell(90, 104, 6, 6), 'hood', 'f')]
    if view == 'side':
        return [L(ell(40, -2, 10, 9), 'hood', 'f'), L(blob([(70, 50), (86, 40), (88, 22), (64, 2), (30, 4), (8, 24), (2, 60), (14, 84), (40, 82), (56, 70)], 8), 'hood', 'f'),
                L([(54, 72), (58, 100)], 'hoodd', 'f', False, False, 3), L(ell(58, 104, 6, 6), 'hood', 'f')]
    return [L(ell(16, 2, 10, 9), 'hood', 'f'), L(ell(84, 2, 10, 9), 'hood', 'f'),
            L(blob([(6, 74), (6, 36), (20, 12), (50, 4), (80, 12), (94, 36), (94, 74), (70, 86), (50, 88), (30, 86)], 8), 'hood', 'f'),
            L([(12, 70), (10, 100)], 'hoodd', 'f', False, False, 3), L([(88, 70), (90, 100)], 'hoodd', 'f', False, False, 3), L(ell(10, 104, 6, 6), 'hood', 'f'), L(ell(90, 104, 6, 6), 'hood', 'f')]


C('jimmy-brim', 'normal', JBR,
  F(eyes='none', brows=False, mouth='frown', mouth_y=94, hairline=False),
  [fr([(18, 64), (22, 46), (40, 38), (60, 38), (80, 46), (82, 64), (76, 56), (68, 60, 1), (60, 52), (50, 58, 1), (40, 52), (32, 60, 1), (24, 56)])] + _bearhood('front') +
  blush(86, 24, 6) + [L(blob([(30, 74), (42, 74), (42, 78), (30, 78)], 2), BLACK, 'f', False), L(blob([(58, 74), (70, 74), (70, 78), (58, 78)], 2), BLACK, 'f', False),
                       L([(30, 68), (40, 66)], OUTC, 'f', False, False, 1.4), L([(70, 68), (60, 66)], OUTC, 'f', False, False, 1.4)],
  _bearhood('side') + [L(blob([(78, 74), (86, 74), (86, 78), (78, 78)], 2), BLACK, 'f', False)],
  _bearhood('back'))

# Joe Chugger: pelo rosa claro en mechones largos peinados hacia arriba y hacia la derecha, con un mechón que cae por la
# frente; piel muy clara, ojos afilados, pendientes finos y boca seria
C('joe-chugger', 'normal', P('#f0a6b8', '#fbe4c8', iris='#7a3a4a', ear='#a0a0a8'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=95, hairline=[(16, 62), (22, 48), (40, 42), (50, 50), (60, 42), (78, 46), (84, 62)]),
  [L(outline([(16, 60), (12, 34), (20, 10), (40, -6), (60, -14), (90, -16, 1), (76, -4), (104, -2, 1), (86, 10), (106, 22, 1), (88, 28), (92, 48), (86, 62), (80, 48), (20, 48)])),
   L(outline([(56, -10), (88, -12), (80, 6), (90, 30), (86, 56), (74, 30)]), 'shade', 'b', False), fr([(40, 30), (52, 62, 1), (58, 34)]),
   L([(17, 82), (17, 92)], 'ear', 'f', False, False, 1.2), L([(83, 82), (83, 92)], 'ear', 'f', False, False, 1.2)],
  [L(outline([(56, 54), (64, 44), (82, 42), (92, 30), (110, 22, 1), (90, 18), (104, 2, 1), (80, 4), (90, -14, 1), (60, -6), (30, 0), (10, 18), (4, 46), (14, 66), (34, 62), (46, 56)])),
   L([(46, 82), (46, 92)], 'ear', 'f', False, False, 1.2)],
  [L(outline([(16, 64), (10, 34), (20, 10), (40, -6), (60, -14), (90, -16, 1), (76, -4), (104, -2, 1), (86, 10), (106, 22, 1), (90, 30), (92, 64), (70, 74), (50, 76), (30, 74)])),
   L(outline([(56, -8), (88, -12), (82, 8), (92, 34), (88, 64), (66, 72)]), 'shade', 'b', False)])

# Joe Divide: pelo verde oscuro corto encima y largo blanco por los lados hasta la mandíbula; una cinta azul marino con
# rombos rojos en la frente; triángulos rojos pintados en las mejillas, ojos redondos grandes y sonrisa de dientes
JD = P('#e6e0d2', '#f4bd84', iris='#1a1210', top='#3a6a2a', band='#2a3a6a', red='#d8282a')
C('joe-divide', 'normal', JD,
  F(eyes='round', brows='angry', mouth='grin', mouth_y=95, hairline=[(16, 64), (20, 56), (50, 56), (80, 56), (84, 64)]),
  longhair('front', length=104, flare=2, top=4) + [L(blob([(14, 40), (22, 14), (50, 2), (78, 14), (86, 40)], 8), 'top', 'f'),
   L(blob([(10, 38), (50, 32), (90, 38), (90, 56), (50, 52), (10, 56)], 4), 'band', 'f'),
   L([(36, 44), (40, 40), (44, 44), (40, 48)], 'red', 'f', False), L([(56, 44), (60, 40), (64, 44), (60, 48)], 'red', 'f', False),
   L([(46, 40), (54, 40), (50, 46)], 'red', 'f', False), L([(46, 50), (54, 50), (50, 44)], 'red', 'f', False),
   L([(24, 84), (34, 80), (34, 88)], 'red', 'f', False), L([(76, 84), (66, 80), (66, 88)], 'red', 'f', False)],
  longhair('side', length=104, flare=2, top=4) + [L(blob([(14, 34), (24, 10), (56, 0), (84, 12), (88, 36)], 8), 'top', 'f'),
   L(blob([(4, 40), (50, 30), (90, 36), (90, 52), (50, 48), (4, 56)], 4), 'band', 'f'), L([(80, 84), (88, 80), (88, 88)], 'red', 'f', False)],
  longhair('back', length=104, flare=2, top=4) + [L(blob([(12, 40), (22, 14), (50, 2), (78, 14), (88, 40)], 8), 'top', 'f'),
   L(blob([(8, 40), (50, 34), (92, 40), (92, 56), (50, 52), (8, 56)], 4), 'band', 'f')])

# John Bleach: pelo verde oliva en pinchos revueltos; piel tostada, ojos blancos redondos con la pupila pequeña, cejas de
# pillo y sonrisa
C('john-bleach', 'normal', P('#6a7a2a', '#e8a868', iris='#1a1210'),
  F(eyes='round', brows='angry', mouth='smile', mouth_y=94, hairline=hl(5, 62, 50, 62, jit=3, seed=36)),
  messy('front', amp=16, n=11, seed=36, lo=64, rx=48, sweep=0.15),
  messy('side', amp=16, n=11, seed=36, lo=64, rx=48, sweep=0.15),
  messy('back', amp=16, n=11, seed=36, lo=64, rx=48, sweep=0.15))

# Jon Izumo: pelo lila recogido en un moño ancho con dos mechones altos como cuernos; marcas rosas curvas en las mejillas,
# ojos afilados y ceño
JI = P('#a080d0', '#f0bf88', iris='#1a1210', mark='#f08aa8')
C('jon-izumo', 'normal', JI,
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=[(16, 62), (22, 48), (40, 44), (50, 50), (60, 44), (78, 48), (84, 62)]),
  [L(outline([(24, 30), (14, -18, 1), (40, 14)])), L(outline([(76, 30), (86, -18, 1), (60, 14)]))] + dome('front', top=4, w=46, cy=46, sb=62, seed=37) +
  [L(quad((24, 70), (30, 80), (28, 92)), 'mark', 'f', False, False, 2.4), L(quad((76, 70), (70, 80), (72, 92)), 'mark', 'f', False, False, 2.4)],
  [L(outline([(36, 26), (30, -20, 1), (54, 12)]))] + dome('side', top=4, w=46, cy=46, nape=80, fr=48, seed=37) + [L(quad((76, 72), (72, 82), (76, 92)), 'mark', 'f', False, False, 2.4)],
  [L(outline([(24, 30), (14, -18, 1), (40, 14)])), L(outline([(76, 30), (86, -18, 1), (60, 14)]))] + dome('back', top=4, w=46, cy=46, nape=82, seed=37))

# Juan Word (portero): pañuelo azul atado a la cabeza con el nudo y las puntas cayendo a un lado; orejas grandes, ojos
# redondos de iris naranja rojizo y boca triste
JWO = P('#2a5a8a', '#f2b070', iris='#c04a1a', band='#2a5a8a', bandd='#1e4268')


def _bandana(view):
    if view == 'front':
        return [L(blob([(8, 62), (6, 36), (20, 12), (50, 4), (80, 12), (94, 36), (92, 62), (50, 56)], 8), 'band', 'f'),
                L(blob([(60, 10), (82, 20), (92, 44), (86, 58)], 6), 'bandd', 'f', False),
                L(outline([(88, 56), (104, 70), (100, 96, 1), (92, 80), (84, 96, 1), (82, 66)]), 'band', 'f')]
    if view == 'side':
        return [L(blob([(86, 52), (88, 28), (64, 4), (30, 6), (8, 26), (4, 60), (50, 56)], 8), 'band', 'f'),
                L(outline([(8, 54), (-8, 70), (-4, 96, 1), (4, 80), (14, 96, 1), (16, 64)]), 'band', 'f')]
    return [L(blob([(6, 64), (6, 36), (20, 12), (50, 4), (80, 12), (94, 36), (94, 64), (50, 70)], 8), 'band', 'f'),
            L(outline([(14, 60), (-2, 72), (2, 98, 1), (10, 82), (18, 98, 1), (22, 66)]), 'band', 'f')]


C('juan-word', 'normal', JWO,
  F(eyes='round', brows=False, mouth='frown', mouth_y=95, big_ears=4, ear_out=2, hairline=False),
  _bandana('front'), _bandana('side'), _bandana('back'))

# June Stagner: corte hime verde con el flequillo recto y mechones largos a los lados; gafas de sol negras estrechas y
# labios sonrientes
C('june-stagner', 'chica', P('#1a9a6a', '#fbe0c4', glass='#1a1a1e'),
  F(eyes='none', brows=False, mouth='lips', mouth_w=7, mouth_y=93, hairline=False),
  longhair('front', length=108, flare=0, top=2) + [fr([(14, 66), (16, 36), (32, 20), (50, 16), (68, 20), (84, 36), (86, 66), (80, 66), (80, 62), (20, 62), (20, 66)]),
   L(blob([(16, 72), (50, 68), (84, 72), (80, 80), (50, 78), (20, 80)], 4), 'glass', 'f')],
  longhair('side', length=108, flare=0, top=2) + [L(blob([(66, 70), (92, 70), (90, 80), (68, 80)], 4), 'glass', 'f')],
  longhair('back', length=108, flare=0, top=2, ends=4))

# Junior Cage: calvo de cráneo grande color crema con arrugas en la frente; gafas pequeñas redondas negras y una tela
# marrón que le tapa la boca y la barbilla; cara alargada
JC = P('#d8c8a8', '#e8d4b0', cloth='#8a7a5a')
C('junior-cage', 'delgado', JC,
  F(eyes='none', brows=False, mouth='none', hairline=False, face_front=face(chin=108, top=10)),
  [L(blob([(18, 60), (16, 26), (30, 4), (50, -4), (70, 4), (84, 26), (82, 60)], 8), 'skin'),
   L(quad((38, 50), (50, 44), (62, 50)), OUTC, 'f', False, False, 1.2), L(quad((40, 56), (50, 52), (60, 56)), OUTC, 'f', False, False, 1.2),
   L(ell(38, 76, 6, 6), BLACK, 'f'), L(ell(62, 76, 6, 6), BLACK, 'f'), L([(44, 75), (56, 75)], BLACK, 'f', False, False, 1.4),
   L(blob([(22, 88), (50, 84), (78, 88), (74, 104), (50, 112), (26, 104)], 6), 'cloth', 'f')],
  [L(blob([(56, 56), (82, 34), (78, 12), (54, -4), (26, 0), (10, 20), (8, 50), (20, 66)], 8), 'skin'), L(ell(82, 76, 5, 6), BLACK, 'f'),
   L([(77, 75), (50, 70)], BLACK, 'f', False, False, 1.4), L(blob([(58, 86), (88, 84), (90, 100), (74, 110), (58, 104)], 6), 'cloth', 'f')],
  [L(blob([(16, 64), (16, 26), (30, 4), (50, -4), (70, 4), (84, 26), (84, 64), (50, 74)], 8), 'skin'), L(quad((10, 80), (50, 86), (90, 80)), 'cloth', 'f', False, False, 3)])

# Junior Gambit: pelo azul pizarra en pinchos altos de punta; piel grisácea, unas gafas redondas grandes que le tapan los
# ojos (con dos círculos dibujados) y la barbilla larga y afilada
JG = P('#3a4a64', '#ece0cc', glassc='#2a2a2e')
C('junior-gambit', 'delgado', JG,
  F(eyes='none', brows=False, mouth='line', mouth_y=98, hairline=[(16, 60), (22, 46), (40, 44), (50, 50), (60, 44), (78, 46), (84, 60)],
    face_front=face(chin=112, jaw=-2)),
  [L(outline([(16, 60), (6, 42, 1), (16, 36), (6, 4, 1), (30, 18), (36, -18, 1), (50, 10), (64, -18, 1), (70, 18), (94, 4, 1), (84, 36), (94, 42, 1), (84, 60), (80, 50), (20, 50)])),
   L(outline([(60, 10), (64, -14), (72, 18), (90, 10), (84, 38), (88, 56), (78, 40)]), 'shade', 'b', False)] +
  [L(ell(36, 76, 10, 8), WHITE, 'f'), L(ell(64, 76, 10, 8), WHITE, 'f'), L(ell(36, 76, 6, 4) + [ell(36, 76, 6, 4)[0]], OUTC, 'f', False, False, 1.2),
   L(ell(64, 76, 6, 4) + [ell(64, 76, 6, 4)[0]], OUTC, 'f', False, False, 1.2), L([(46, 75), (54, 75)], 'glassc', 'f', False, False, 1.6)],
  [L(outline([(56, 52), (64, 42), (84, 38), (90, 20), (100, 8, 1), (80, 10), (76, -16, 1), (58, 4), (40, -16, 1), (32, 6), (8, 2, 1), (14, 20), (0, 40, 1), (8, 54), (24, 64), (44, 56)])),
   L(ell(82, 76, 6, 8), WHITE, 'f'), L([(76, 74), (50, 70)], 'glassc', 'f', False, False, 1.6)],
  [L(outline([(16, 64), (6, 42, 1), (16, 36), (6, 4, 1), (30, 18), (36, -18, 1), (50, 10), (64, -18, 1), (70, 18), (94, 4, 1), (84, 36), (94, 42, 1), (84, 64), (50, 72)]))])

# Justin Cush (portero): envuelto en un turbante crema que le tapa la cabeza y le da vueltas alrededor de la cara y el
# cuello; piel tostada, ojos azules afilados y boca torcida con un colmillo
JCU = P('#f2ece0', '#c08a5a', iris='#4a5a9a', wrap='#f2ece0', wrapd='#d8b0b0')


def _wrap(view):
    if view == 'front':
        return [L(blob([(10, 70), (8, 34), (24, 10), (50, 2), (76, 10), (92, 34), (90, 70), (80, 60), (78, 48), (50, 44), (22, 48), (20, 60)], 8), 'wrap', 'f'),
                L(blob([(30, 14), (60, 10), (80, 24), (70, 28), (40, 22)], 6), 'wrapd', 'f', False),
                L(blob([(4, 80), (18, 92), (40, 106), (60, 108), (84, 96), (98, 80), (100, 104), (80, 118), (50, 122), (20, 118), (0, 104)], 8), 'wrap', 'f'),
                L(blob([(10, 100), (40, 112), (70, 110), (92, 98), (80, 114), (40, 118)], 6), 'wrapd', 'f', False)]
    if view == 'side':
        return [L(blob([(84, 50), (88, 28), (64, 4), (30, 4), (8, 24), (2, 70), (10, 100), (40, 110), (70, 116), (92, 106), (90, 94), (60, 92), (40, 80), (50, 56)], 8), 'wrap', 'f'),
                L(blob([(30, 70), (60, 96), (88, 100), (70, 110), (30, 96)], 6), 'wrapd', 'f', False)]
    return [L(blob([(4, 100), (6, 34), (22, 10), (50, 2), (78, 10), (94, 34), (96, 100), (80, 118), (50, 122), (20, 118)], 8), 'wrap', 'f'),
            L(blob([(20, 60), (50, 50), (80, 60), (84, 80), (50, 74), (16, 80)], 6), 'wrapd', 'f', False)]


C('justin-cush', 'normal', JCU,
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=False),
  _wrap('front') + [L([(56, 94), (58, 98), (60, 94)], WHITE, 'f', False)], _wrap('side'), _wrap('back'))

# Justin Primm (portero): mata enorme de pelo negro azulado en rizos revueltos que se abren hacia los lados; ojos verdes
# afilados, unos arañazos en las mejillas y boca seria
C('justin-primm', 'normal', P('#2c2840', '#f4c08a', iris='#2a8a7a'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=95, hairline=hl(5, 62, 50, 62, jit=4, seed=43)),
  dome('front', top=-8, w=56, cy=40, n=12, amp=9, soft=True, sb=76, seed=43) + [fr([(34, 40), (40, 70, 1), (46, 46)]),
   L([(24, 84), (32, 82)], OUTC, 'f', False, False, 0.9), L([(68, 82), (76, 84)], OUTC, 'f', False, False, 0.9)],
  dome('side', top=-8, w=56, cy=40, n=12, amp=9, soft=True, nape=90, fr=50, seed=43),
  dome('back', top=-8, w=56, cy=40, n=12, amp=9, soft=True, nape=92, seed=43))

# Kate Later: piel morena; melena rosa melocotón larga barrida hacia un lado que cae hasta los hombros; ojos ámbar,
# cejas marcadas y boca en o
C('kate-later', 'chica', P('#f4b0a0', '#9a6a46', iris='#c08a2a'),
  F(eyes='sharp', brows='angry', mouth='none', hairline=[(16, 64), (20, 46), (36, 36), (60, 34), (80, 44), (84, 64)]),
  longhair('front', length=104, flare=6, top=2) + [fr([(14, 66), (16, 36), (36, 20), (64, 18), (86, 34), (88, 60), (76, 44), (52, 40), (30, 50), (20, 64)])] +
  [L(ell(50, 96, 2.8, 3.6), (110, 40, 40, 255), 'f', True)],
  longhair('side', length=104, flare=6, top=2),
  longhair('back', length=104, flare=6, top=2, ends=5))

# Kath Leaflin: pelo amarillo en pinchos de punta en todas direcciones; aros plateados en las orejas, cejas gruesas
# fruncidas, ojos afilados y ceño
C('kath-leaflin', 'chica', P('#e0c024', '#f6c494', iris='#1a1210', ring='#c8c8d0'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=95, hairline=hl(6, 62, 50, 60, jit=3, seed=45)),
  messy('front', amp=18, n=13, seed=45, lo=62, rx=48) + thick_brows(64, 'deep', 3.4, 14, 1.4, 12) +
  [L(ell(15, 86, 3, 3.4) + [ell(15, 86, 3, 3.4)[0]], 'ring', 'f', False, False, 1.4), L(ell(85, 86, 3, 3.4) + [ell(85, 86, 3, 3.4)[0]], 'ring', 'f', False, False, 1.4)],
  messy('side', amp=18, n=13, seed=45, lo=62, rx=48) + [L(ell(46, 84, 3, 3.4) + [ell(46, 84, 3, 3.4)[0]], 'ring', 'f', False, False, 1.4)],
  messy('back', amp=18, n=13, seed=45, lo=62, rx=48))

# Katy Punter: pelo verde hoja en mechones de punta barridos a un lado, con mechones largos que caen junto a la cara;
# ojos azules grandes
C('katy-punter', 'chica', P('#6aac2c', '#f6c894', iris='#2a5aa8'),
  F(eyes='big', brows=True, mouth='line', mouth_y=95, hairline=[(16, 64), (20, 46), (36, 38), (60, 36), (80, 46), (84, 64)]),
  messy('front', amp=14, n=10, seed=46, lo=62, rx=48, sweep=0.3) + [fr([(16, 56), (12, 104, 1), (24, 70)]), fr([(84, 56), (92, 104, 1), (76, 70)]),
   fr([(20, 50), (34, 30), (60, 26), (82, 36), (60, 42), (38, 56, 1)])],
  messy('side', amp=14, n=10, seed=46, lo=62, rx=48, sweep=0.3) + [fr([(60, 56), (58, 104, 1), (66, 70)])],
  messy('back', amp=14, n=10, seed=46, lo=62, rx=48, sweep=0.3))

# Kay Gateley: melena larga carmesí que le cae por delante de la cara y le tapa media cara; gafas de sol de montura
# amarilla y una mascarilla crema
C('kay-gateley', 'chica', P('#b02032', '#c08a5a', frame='#d8b830', lens='#4a4a4e', mask='#ecdcc0'),
  F(eyes='none', brows=False, mouth='none', hairline=[(16, 64), (24, 46), (50, 36), (76, 46), (84, 64)]),
  longhair('front', length=112, flare=4, top=0) + [L(blob([(20, 70), (48, 72), (46, 82), (22, 80)], 4), 'frame', 'f'), L(blob([(52, 72), (80, 70), (78, 80), (54, 82)], 4), 'frame', 'f'),
   L(blob([(24, 73), (45, 75), (44, 80), (25, 79)], 4), 'lens', 'f', False), L(blob([(55, 75), (76, 73), (75, 79), (56, 80)], 4), 'lens', 'f', False),
   L(blob([(26, 86), (50, 84), (74, 86), (70, 100), (50, 106), (30, 100)], 6), 'mask', 'f'),
   fr([(14, 60), (24, 30), (46, 20), (40, 50), (30, 90), (26, 114, 1), (16, 96)]), fr([(86, 60), (76, 30), (54, 20), (60, 50), (70, 90), (74, 114, 1), (84, 96)])],
  longhair('side', length=112, flare=4, top=0) + [L(blob([(70, 70), (90, 72), (88, 82), (72, 80)], 4), 'frame', 'f'), L(blob([(70, 86), (90, 86), (88, 100), (72, 102)], 6), 'mask', 'f')],
  longhair('back', length=112, flare=4, top=0, ends=5))

# Kaya Haskell: pelo castaño claro con una trenza que le rodea la cabeza, el flequillo barrido a un lado y dos trenzas
# bajas que caen por los hombros; ojos verde azulado grandes y sonrisa
KH = P('#a8682e', '#fbd2ac', iris='#3a9a9a')
C('kaya-haskell', 'chica', KH,
  F(eyes='big', brows=True, mouth='smile', mouth_y=94, hairline=[(16, 62), (20, 46), (34, 40), (60, 38), (80, 46), (84, 62)]),
  dome('front', top=0, w=48, cy=44, sb=76, seed=48) + _braid_crown('front') + [fr([(16, 56), (22, 40), (44, 32), (70, 30), (86, 42), (66, 42), (46, 50), (30, 60)]),
   L(ell(14, 92, 6, 7)), L(ell(14, 104, 5, 6)), L(ell(86, 92, 6, 7)), L(ell(86, 104, 5, 6))],
  dome('side', top=0, w=48, cy=44, nape=84, fr=50, seed=48) + _braid_crown('side') + [L(ell(56, 96, 6, 7)), L(ell(56, 108, 5, 6))],
  dome('back', top=0, w=48, cy=44, nape=84, seed=48) + _braid_crown('back') + [L(ell(20, 94, 6, 7)), L(ell(80, 94, 6, 7))])

# Kelly Scrivens: melena azul claro larga y ondulada que se abre abajo, flequillo recto y un lazo rojo enorme encima con
# cintas que caen; ojos verde azulado grandes y boca pequeña
C('kelly-scrivens', 'chica', P('#7a9ae0', '#f6c894', iris='#2a8a8a', bow='#e83a1e'),
  F(eyes='big', brows=False, mouth='line', mouth_y=95, hairline=False),
  longhair('front', length=112, flare=18, top=4) + [fr([(14, 64), (16, 36), (32, 20), (50, 16), (68, 20), (84, 36), (86, 64), (80, 64), (80, 60), (20, 60), (20, 64)]),
   L(blob([(50, 6), (30, -8), (18, 0), (24, 12), (50, 10), (76, 12), (82, 0), (70, -8)], 6), 'bow', 'f'), L(ell(50, 6, 5, 5), 'bow', 'f'),
   L([(30, 8), (20, 40)], 'bow', 'f', False, False, 2.4), L([(70, 8), (84, 30), (90, 36)], 'bow', 'f', False, False, 2.4)],
  longhair('side', length=112, flare=18, top=4) + [L(blob([(44, 4), (26, -10), (16, 0), (24, 10)], 6), 'bow', 'f'), L(ell(46, 4, 5, 5), 'bow', 'f')],
  longhair('back', length=112, flare=18, top=4, ends=5) + [L(blob([(50, 6), (30, -8), (18, 0), (24, 12), (50, 10), (76, 12), (82, 0), (70, -8)], 6), 'bow', 'f'),
                                                           L(ell(50, 6, 5, 5), 'bow', 'f')])

# Ken Mayfield: pelo azul marino oscuro revuelto y abultado; piel tostada, ojos blancos redondos y una sonrisa de labios
# rojos
C('ken-mayfield', 'normal', P('#22304e', '#dca06a', iris='#1a1210'),
  F(eyes='round', brows=False, mouth='lips', mouth_w=9, mouth_y=93, hairline=hl(5, 60, 48, 56, jit=3, seed=50)),
  dome('front', top=-4, w=48, cy=40, n=9, amp=8, soft=True, sb=66, seed=50),
  dome('side', top=-4, w=48, cy=40, n=9, amp=8, soft=True, nape=82, fr=50, seed=50),
  dome('back', top=-4, w=48, cy=40, n=9, amp=8, soft=True, nape=82, seed=50))

# Kim Knotted: melena verde azulado muy larga y lisa con la raya en medio y la frente despejada; ojos castaños afilados
C('kim-knotted', 'chica', P('#1a7a7c', '#f4c494', iris='#7a4a1a'),
  F(eyes='sharp', brows=True, mouth='line', mouth_y=95, hairline=[(16, 64), (20, 44), (30, 34), (50, 30), (70, 34), (80, 44), (84, 64)]),
  longhair('front', length=128, flare=0, top=0, part=True),
  longhair('side', length=128, flare=0, top=0),
  longhair('back', length=128, flare=0, top=0, part=True, ends=5))

# Kurt Sermons (portero): cabeza rapada con una cresta naranja larga peinada hacia la derecha en mechones de punta; unas
# gafas de visera moradas y aros dorados
KS = P('#e8701e', '#d8a46a', visor='#8a5aaa', gold='#e8c030')
C('kurt-sermons', 'normal', KS,
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, hairline=False),
  [skull(), L(outline([(38, 50), (32, 20), (40, -6), (56, -14), (76, -18, 1), (68, -6), (92, -6, 1), (76, 4), (92, 14, 1), (70, 16), (80, 34, 1), (62, 28), (56, 60, 1), (50, 34)])),
   L(blob([(14, 72), (32, 68), (50, 76), (68, 68), (86, 72), (82, 84), (64, 82), (50, 86), (36, 82), (18, 84)], 6), 'visor', 'f'),
   L(ell(15, 88, 2.6, 3) + [ell(15, 88, 2.6, 3)[0]], 'gold', 'f', False, False, 1.6), L(ell(85, 88, 2.6, 3) + [ell(85, 88, 2.6, 3)[0]], 'gold', 'f', False, False, 1.6)],
  [L(blob([(56, 56), (82, 34), (78, 12), (54, -2), (26, 2), (10, 22), (8, 50), (20, 66)], 8), 'skin'),
   L(outline([(70, 20), (80, 0, 1), (56, 0), (50, -18, 1), (36, 0), (14, -6, 1), (22, 12), (4, 20, 1), (24, 24), (40, 14), (56, 10)])),
   L(blob([(66, 70), (92, 70), (92, 84), (68, 84)], 6), 'visor', 'f'), L(ell(46, 86, 2.6, 3) + [ell(46, 86, 2.6, 3)[0]], 'gold', 'f', False, False, 1.6)],
  [L(blob([(16, 64), (16, 26), (30, 4), (50, -4), (70, 4), (84, 26), (84, 64), (50, 74)], 8), 'skin'),
   L(outline([(42, 60), (38, 20), (44, -6), (56, -14), (70, -14, 1), (64, 0), (86, -2, 1), (70, 10), (80, 24, 1), (62, 26), (58, 60)])),
   L(quad((10, 76), (50, 82), (90, 76)), 'visor', 'f', False, False, 3)])

# Lacey Threader: gorro de punto rosa con dos franjas turquesa y una melena castaña larga y ondulada; ojos grandes, ceño
# y unas marcas en las mejillas
C('lacey-threader', 'chica', P('#7a4a22', '#f2ba82', iris='#3a2a1a', hat='#f08a8a', stripe='#6ac8c8'),
  F(eyes='big', brows='angry', mouth='frown', mouth_y=95, hairline=[(16, 62), (22, 56), (50, 56), (78, 56), (84, 62)]),
  longhair('front', length=112, flare=14, top=10) + [L(blob([(10, 58), (8, 30), (20, 6), (50, -4), (80, 6), (92, 30), (90, 58), (50, 54)], 8), 'hat', 'f'),
   L(blob([(14, 24), (38, 22), (38, 30), (14, 32)], 2), 'stripe', 'f', False), L(blob([(14, 38), (38, 36), (38, 44), (14, 46)], 2), 'stripe', 'f', False),
   L([(24, 86), (28, 84)], OUTC, 'f', False, False, 0.9), L([(76, 86), (72, 84)], OUTC, 'f', False, False, 0.9)],
  longhair('side', length=112, flare=14, top=10) + [L(blob([(4, 50), (6, 20), (30, 0), (64, -4), (90, 14), (92, 50), (50, 46)], 8), 'hat', 'f'),
   L(blob([(60, 18), (80, 20), (80, 28), (60, 26)], 2), 'stripe', 'f', False)],
  longhair('back', length=112, flare=14, top=10, ends=5) + [L(blob([(8, 60), (8, 30), (20, 6), (50, -4), (80, 6), (92, 30), (92, 60), (50, 66)], 8), 'hat', 'f')])

# Lamar Bonesteel: tupé verde azulado oscuro peinado hacia atrás y a la derecha en un gran rizo, con la sien rapada; piel
# muy clara, orejas puntiagudas, ojos castaños afilados y sonrisa de lado
C('lamar-bonesteel', 'normal', P('#3a5a5c', '#fbe6c0', iris='#6a3a1a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=95, hairline=[(16, 58), (24, 44), (36, 40), (46, 58), (56, 40), (78, 42), (84, 58)]),
  [L(outline([(16, 58), (14, 34), (24, 10), (44, -2), (66, -4), (86, 8), (92, 28), (88, 56), (82, 46), (60, 34), (50, 58, 1), (40, 34), (22, 44)])),
   L(outline([(50, 6), (72, 0), (88, 14), (90, 34), (78, 20), (60, 14)]), 'shade', 'b', False),
   L(outline([(18, 70), (8, 58, 1), (18, 62)]), 'skin', 'f'), L(outline([(82, 70), (92, 58, 1), (82, 62)]), 'skin', 'f')],
  [L(outline([(56, 56), (64, 44), (86, 38), (96, 22), (80, 2), (50, -6), (22, 0), (8, 18), (4, 44), (12, 64), (30, 62), (44, 56)])),
   L(outline([(30, 6), (60, 0), (88, 18), (70, 22), (40, 18)]), 'shade', 'b', False)],
  [L(outline([(14, 66), (10, 34), (22, 10), (44, -2), (66, -4), (86, 8), (92, 28), (90, 66), (70, 74), (50, 76), (30, 74)])),
   L(outline([(56, 2), (84, 10), (92, 40), (88, 64), (66, 72)]), 'shade', 'b', False)])

# Lana Service: pelo castaño ondulado con una diadema turquesa y dos moños abultados bajos a los lados; ojos verdes,
# pecas y ceño
C('lana-service', 'chica', P('#a85a24', '#f6c696', iris='#2a8a6a', band='#6ab8a8'),
  F(eyes='big', brows='angry', mouth='frown', mouth_y=95, hairline=[(16, 60), (20, 46), (36, 40), (60, 42), (80, 46), (84, 60)]),
  [L(ell(8, 84, 12, 13)), L(ell(92, 84, 12, 13))] + dome('front', top=2, w=48, cy=44, sb=74, seed=55) + [band('front', 18, 7),
   fr([(16, 56), (22, 38), (46, 30), (74, 32), (86, 46), (68, 42), (52, 48), (36, 46), (26, 58)])] + freckles(86, 24),
  [L(ell(46, 88, 13, 13))] + dome('side', top=2, w=48, cy=44, nape=80, fr=50, seed=55) + [band('side', 18, 7)],
  [L(ell(12, 86, 12, 13)), L(ell(88, 86, 12, 13))] + dome('back', top=2, w=48, cy=44, nape=80, seed=55) + [band('back', 18, 7)])

# Langley Span: gorro gris con una cinta crema de tres puntos naranjas; ojos negros afilados muy fruncidos, una cicatriz
# en la mejilla y boca torcida
C('langley-span', 'normal', P('#5a6672', '#f4c494', cap='#5a6672', band='#ece2cc', dot='#e88a4a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, hairline=False),
  [L(blob([(12, 56), (14, 28), (30, 10), (50, 6), (70, 10), (86, 28), (88, 56), (50, 52)], 8), 'cap', 'f'),
   L(blob([(10, 44), (50, 38), (90, 44), (90, 60), (50, 56), (10, 60)], 4), 'band', 'f'),
   L(ell(38, 49, 2.6, 2.6), 'dot', 'f', False), L(ell(50, 47, 2.6, 2.6), 'dot', 'f', False), L(ell(62, 49, 2.6, 2.6), 'dot', 'f', False),
   L([(24, 88), (34, 84)], OUTC, 'f', False, False, 1.0), L([(26, 91), (32, 89)], OUTC, 'f', False, False, 1.0)],
  [L(blob([(10, 54), (12, 22), (40, 4), (70, 8), (88, 28), (88, 54), (50, 50)], 8), 'cap', 'f'), L(blob([(6, 42), (50, 36), (90, 42), (90, 58), (50, 54), (6, 58)], 4), 'band', 'f')],
  [L(blob([(12, 58), (14, 28), (30, 10), (50, 6), (70, 10), (86, 28), (88, 58), (50, 62)], 8), 'cap', 'f'), L(blob([(8, 46), (50, 42), (92, 46), (92, 60), (50, 58), (8, 60)], 4), 'band', 'f')])

# Lara Creamer: pelo azul marino recogido tirante hacia atrás como un casco liso; gafas rectangulares negras, ojos castaños
# adormilados, coloretes grandes, boca en o y un pañuelo rojo al cuello
LC = P('#2a3a6a', '#f4c494', iris='#7a4a1a', scarf='#d83a1e')
C('lara-creamer', 'chica', LC,
  F(eyes='sharp', brows=False, mouth='none', hairline=[(16, 64), (20, 44), (34, 34), (50, 30), (66, 34), (80, 44), (84, 64)]),
  bowl('front', top=0, side=90) + rect_specs('front', BLACK, 76, 14, 2.0) + blush(88, 24, 5) +
  [L(ell(50, 98, 2.8, 3.4), (150, 90, 40, 255), 'f', True),
   L(blob([(20, 104), (50, 112), (80, 104), (96, 116), (70, 122), (50, 118), (30, 122), (4, 116)], 4), 'scarf', 'f')],
  bowl('side', top=0, nape=92) + rect_specs('side', BLACK, 76) + [L(blob([(50, 106), (80, 108), (90, 118), (60, 120), (40, 114)], 4), 'scarf', 'f')],
  bowl('back', top=0, nape=92) + [L(ell(50, 96, 8, 7)), L(blob([(14, 106), (50, 110), (86, 106), (86, 116), (14, 116)], 4), 'scarf', 'f')])

# Larry Pogue: casco rojo de robot con paneles y un rayo amarillo en la frente, con placas que bajan por los lados hasta
# los hombros; ojos como dos anillos blancos y sonrisa
LP = P('#d8282a', '#f4b874', helmet='#d8282a', helmetd='#a81a1e', bolt='#f8e060')


def _robot(view):
    if view == 'front':
        return [L(outline([(10, 54), (4, 10, 1), (20, 18), (24, -10, 1), (40, 2), (50, -14, 1), (60, 2), (76, -10, 1), (80, 18), (96, 10, 1), (90, 54), (50, 48)]), 'helmet', 'f'),
                L(blob([(34, 18), (66, 18), (64, 52), (36, 52)], 2), 'helmetd', 'f'), L([(46, 24), (56, 24), (50, 34), (58, 34), (44, 48), (48, 36), (42, 36)], 'bolt', 'f', False),
                L(blob([(10, 54), (20, 54), (20, 104), (8, 108)], 2), 'helmet', 'f'), L(blob([(80, 54), (90, 54), (92, 108), (80, 104)], 2), 'helmet', 'f'),
                L(ell(36, 74, 7, 7), WHITE, 'f'), L(ell(36, 74, 3.6, 3.6), BLACK, 'f', False), L(ell(64, 74, 7, 7), WHITE, 'f'), L(ell(64, 74, 3.6, 3.6), BLACK, 'f', False)]
    if view == 'side':
        return [L(outline([(88, 52), (90, 20), (98, 10, 1), (78, 6), (70, -14, 1), (50, 0), (30, -12, 1), (20, 8), (4, 14, 1), (6, 54), (50, 50)]), 'helmet', 'f'),
                L(blob([(30, 54), (50, 54), (50, 104), (30, 108)], 2), 'helmet', 'f'), L(ell(82, 74, 6, 7), WHITE, 'f'), L(ell(83, 74, 3, 3.6), BLACK, 'f', False)]
    return [L(outline([(8, 60), (4, 10, 1), (20, 18), (24, -10, 1), (40, 2), (50, -14, 1), (60, 2), (76, -10, 1), (80, 18), (96, 10, 1), (92, 60), (50, 66)]), 'helmet', 'f'),
            L(blob([(10, 60), (22, 60), (20, 104), (8, 108)], 2), 'helmet', 'f'), L(blob([(78, 60), (90, 60), (92, 108), (80, 104)], 2), 'helmet', 'f')]


C('larry-pogue', 'normal', LP, F(eyes='none', brows=False, mouth='smile', mouth_y=95, hairline=False, nose=(50, 86, 1.6)), _robot('front'), _robot('side'), _robot('back'))

# Laura Quilter: pelo castaño recogido arriba, con mechones rizados que caen junto a las orejas; unas gafas de visera
# verde oliva con dos cristales verdes oscuros sobre los ojos; sonrisa
C('laura-quilter', 'chica', P('#6a4232', '#f6c696', visor='#8a8a5a', lens='#1e4a2a'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=95, hairline=[(16, 62), (20, 48), (36, 42), (50, 46), (64, 42), (80, 48), (84, 62)]),
  [L(ell(50, 6, 18, 12))] + dome('front', top=4, w=44, cy=46, sb=64, seed=59) +
  [L(quad((16, 66), (8, 78), (16, 88)), 'mid', 'f', False, False, 2.6), L(quad((84, 66), (92, 78), (84, 88)), 'mid', 'f', False, False, 2.6),
   L(blob([(16, 66), (50, 64), (84, 66), (82, 86), (50, 88), (18, 86)], 6), 'visor', 'f'), L(ell(36, 76, 7, 8), 'lens', 'f', False), L(ell(64, 76, 7, 8), 'lens', 'f', False)],
  [L(ell(40, 4, 18, 12))] + dome('side', top=4, w=44, cy=46, nape=80, fr=48, seed=59) + [L(blob([(66, 66), (92, 66), (92, 86), (68, 86)], 6), 'visor', 'f'),
   L(ell(84, 76, 5, 7), 'lens', 'f', False), L(quad((48, 66), (40, 78), (48, 88)), 'mid', 'f', False, False, 2.6)],
  [L(ell(50, 6, 18, 12))] + dome('back', top=4, w=44, cy=46, nape=82, seed=59) + [L(quad((8, 76), (50, 80), (92, 76)), 'visor', 'f', False, False, 3)])

# Laurie Nowlin: pelo rojo corto con el flequillo barrido a un lado y una coletita baja detrás; ojos azules afilados,
# cejas fruncidas y unas marcas en las mejillas
C('laurie-nowlin', 'chica', P('#c03a1a', '#f4ba82', iris='#3a6a9a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=[(16, 62), (20, 46), (34, 38), (60, 36), (80, 46), (84, 62)]),
  dome('front', top=2, w=44, cy=46, sb=70, seed=60) + [fr([(14, 60), (18, 36), (40, 24), (68, 24), (86, 38), (86, 52), (70, 42), (50, 44), (30, 56)]),
   L([(24, 86), (30, 84)], OUTC, 'f', False, False, 0.9), L([(76, 86), (70, 84)], OUTC, 'f', False, False, 0.9)],
  dome('side', top=2, w=44, cy=46, nape=82, fr=48, seed=60) + [L(outline([(18, 76), (2, 96, 1), (10, 78)]))],
  dome('back', top=2, w=44, cy=46, nape=82, seed=60) + [L(outline([(44, 80), (50, 100, 1), (56, 80)]))])

# Lee Screener (grandullón): pañuelo verde en la cabeza, cara grande, ojos blancos entornados, una barba castaña espesa que
# le cubre toda la boca y la mandíbula y un aro dorado en la oreja
C('lee-screener', 'corpulento', P('#4a8a3a', '#e8b07a', beard='#8a5a3e', gold='#e8c030'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ear_out=6, nose=(50, 84, 2.2),
    face_front=blob([(10, 56), (50, 44), (90, 56), (94, 80), (88, 104), (50, 112), (12, 104), (6, 80)])),
  [L(blob([(10, 60), (12, 30), (28, 12), (50, 8), (72, 12), (88, 30), (90, 60), (50, 54)], 8), 'mid', 'f'),
   L(blob([(60, 12), (80, 22), (88, 46), (78, 50)], 6), 'shade', 'f', False),
   L(blob([(22, 66), (40, 64), (40, 74), (22, 74)], 4), WHITE, 'f'), L(blob([(60, 64), (78, 66), (78, 74), (60, 74)], 4), WHITE, 'f'),
   L(ell(34, 70, 2, 2.4), BLACK, 'f', False), L(ell(66, 70, 2, 2.4), BLACK, 'f', False), L([(20, 66), (42, 64)], OUTC, 'f', False, False, 2.2), L([(58, 64), (80, 66)], OUTC, 'f', False, False, 2.2),
   L(blob([(14, 88), (50, 86), (86, 88), (88, 104), (50, 112), (12, 104)], 6), 'beard', 'f'), L([(36, 98), (64, 98)], OUTC, 'f', False, False, 1.4),
   L(ell(9, 86, 2.4, 2.8) + [ell(9, 86, 2.4, 2.8)[0]], 'gold', 'f', False, False, 1.6)],
  [L(blob([(10, 56), (12, 22), (40, 4), (70, 8), (88, 28), (88, 56), (50, 52)], 8), 'mid', 'f'),
   L(blob([(64, 86), (90, 86), (90, 104), (70, 110), (58, 100)], 6), 'beard', 'f'), L(ell(46, 86, 2.4, 2.8) + [ell(46, 86, 2.4, 2.8)[0]], 'gold', 'f', False, False, 1.6)],
  [L(blob([(10, 62), (12, 30), (28, 12), (50, 8), (72, 12), (88, 30), (90, 62), (50, 68)], 8), 'mid', 'f')])

# Lehman Rind: afro naranja tostado de rizos grandes, gafas redondas azul claro, orejas grandes y sonrisa
C('lehman-rind', 'normal', P('#c0561c', '#f0b06a', iris='#1a1210'),
  F(eyes='dot', brows=False, mouth='smile', mouth_y=94, big_ears=3, ear_out=4, hairline=hl(5, 60, 50, 56, jit=2, seed=62)),
  dome('front', top=-10, w=56, cy=38, n=12, amp=8, soft=True, sb=70, seed=62) + round_specs('front', _c('#5ab0d8'), 75, 14, 8.5, 7, 2.2),
  dome('side', top=-10, w=56, cy=38, n=12, amp=8, soft=True, nape=86, fr=52, seed=62) + round_specs('side', _c('#5ab0d8'), 75, 14, 8.5, 7, 2.2),
  dome('back', top=-10, w=56, cy=38, n=12, amp=8, soft=True, nape=86, seed=62))
