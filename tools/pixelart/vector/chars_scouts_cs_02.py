"""Ojeadores de CS (scouts-cs), tanda 02: dibujados a partir de su retrato de Victory Road; claves 'scouts-cs:<id>'.

El frente sale del retrato y el perfil y la espalda se deducen (con el modelo 3D de apoyo cuando es del mismo personaje:
Katsu, Kyoko Hanabayashi, La Hire, Nagahide Niwa, Percival Travis, Prince Charles). Muchos son personajes históricos
del Chrono Stone (samuráis, caballeros, oni), con moños, cascos y barbas."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401
from chars_scouts_ie1_09 import dome, hl, face, face_side, mark, _c  # noqa: F401
from chars_scouts_ie1_03 import thick_brows, side_brow, stache  # noqa: F401
from chars_scouts_ie3_02 import ring, hood, bowl3, scarf, side_lock, skull3  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)
K = 'scouts-cs:'


def F(**k):
    d = {'eyes': 'normal', 'mouth': 'line'}
    d.update(k)
    return d


def P(hair, skin, iris='#302232', **k):
    return pal(hair, skin, iris, **k)


def C(pid, body, palette, f, front, side, back):
    """El nacimiento del pelo baja por el borde de la cara para que su raya no cruce el pelo de los lados."""
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[K + pid] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def bun(x, y, r, c='mid', z='b'):
    """Moño redondo."""
    return L(ell(x, y, r, r * 0.9), c, z)


def stick(p0, p1, c, w=1.6):
    """Palillo o mondadientes en la boca."""
    return L([p0, p1], c, 'f', False, False, w)


def tusk(x, y, s):
    """Colmillo blanco que sube desde la comisura (s = 1 izquierda, -1 derecha)."""
    return L(outline([(x - 5 * s, y + 4), (x - 9 * s, y - 10, 1), (x + 4 * s, y + 3)]), WHITE, 'f', True)


def beard(pts, c='mid'):
    return L(outline(pts), c, 'f')


def eye_patch(cx, cy, c, strap=None):
    out = [L(ell(cx, cy, 8, 7), c, 'f')]
    if strap:
        out.insert(0, L(strap, c, 'f', False, False, 2.0))
    return out


TAN = '#c08858'
LIGHT = '#f4c69a'
PALE = '#fadcc0'

# ------------------------------------------------------------------ jugadores

# Jetaime Horitara (portero): pelo rizado rubio ceniza en bola, con una cinta blanca de raya azul anudada en lazo sobre la
# frente; ojos azules entornados y un palillo en la boca
NAVY = _c('#283c84')
def _jet_band(view):
    if view == 'front':
        return [L(outline([(6, 52), (50, 44), (94, 52), (94, 62), (50, 56), (6, 62)]), WHITE, 'f'),
                L(outline([(6, 55), (50, 47), (94, 55), (94, 58), (50, 51), (6, 58)]), NAVY, 'f', False),
                L(blob([(50, 50), (64, 40), (72, 48), (64, 58)], 5), WHITE, 'f'), L(blob([(50, 50), (36, 40), (28, 48), (36, 58)], 5), WHITE, 'f'),
                L(ell(50, 51, 4, 4), WHITE, 'f')]
    if view == 'side':
        return [L(outline([(4, 50), (50, 44), (92, 48), (92, 58), (50, 56), (4, 60)]), WHITE, 'f'),
                L(outline([(4, 53), (50, 47), (92, 51), (92, 54), (50, 50), (4, 56)]), NAVY, 'f', False)]
    return [L(outline([(4, 54), (50, 50), (96, 54), (96, 64), (50, 60), (4, 64)]), WHITE, 'f'),
            L(outline([(4, 57), (50, 53), (96, 57), (96, 60), (50, 56), (4, 60)]), NAVY, 'f', False)]
C('jetaime-horitara', 'normal', P('#b8aa72', '#f6c690', iris='#4a6ab0', shade='#8c7c4c'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=92, eye_y=77, hairline=[(6, 66), (20, 58), (50, 56), (80, 58), (94, 66)]),
  dome('front', top=-2, w=50, cy=44, n=14, amp=6, soft=True, sb=78, seed=11) + _jet_band('front') +
  [L(blob([(26, 72), (42, 72), (42, 75), (26, 75)], 3), 'skin_d', 'f', False), L(blob([(58, 72), (74, 72), (74, 75), (58, 75)], 3), 'skin_d', 'f', False),
   stick((56, 93), (70, 100), _c('#d8b070'))],
  dome('side', top=-2, w=48, cy=44, n=14, amp=6, soft=True, nape=90, fr=56, seed=11) + _jet_band('side') + [stick((84, 93), (94, 99), _c('#d8b070'))],
  dome('back', top=-2, w=50, cy=44, n=14, amp=6, soft=True, nape=90, seed=11) + _jet_band('back'))

# Jinpei Ashiga: viejo de piel tostada con el pelo blanco rosado peinado hacia atrás en un moñito; parche rojo redondo de
# rejilla en un ojo, cejas arrugadas y boca torcida
RED = _c('#c8302a')
C('jinpei-ashiga', 'delgado', P('#f2d8d6', TAN, iris='#202020', shade='#d4b0b0'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, face_front=face(chin=104), face_side=face_side(chin=4),
    hairline=[(10, 60), (20, 46), (34, 40), (50, 38), (66, 40), (80, 46), (90, 60)]),
  dome('front', top=10, w=42, cy=44, n=9, amp=4, seed=12, sb=64) + [L(ell(56, 0, 8, 7)), L(outline([(56, 4), (62, -10), (66, -2)]))] +
  eye_patch(36, 76, RED, [(26, 66), (78, 50)]) + [L([(30, 70), (42, 82)], BLACK, 'f', False, False, 1.6), L([(30, 78), (42, 72)], BLACK, 'f', False, False, 1.6),
                                                  L([(20, 88), (26, 92)], OUTC, 'f', False, False, 1.0), L([(74, 88), (80, 84)], OUTC, 'f', False, False, 1.0)],
  dome('side', top=10, w=42, cy=44, n=9, amp=4, seed=12, nape=86, fr=38) + [L(ell(14, 14, 8, 7))] + [L([(52, 56), (88, 66)], RED, 'f', False, False, 2.0)],
  dome('back', top=10, w=42, cy=44, n=9, amp=4, seed=12, nape=86) + [L(ell(56, 8, 8, 7)), L([(18, 64), (82, 58)], RED, 'f', False, False, 2.0)])

# Johnny Kato: pinchos azules alborotados con un moño alto y mechones que le cuelgan junto a las orejas; ojos redondos y
# ceño fruncido
C('johnny-kato', 'normal', P('#2a6aa0', '#c99060', iris='#1e1e1e', shade='#1c4e7c'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=93, hairline=hl(6, 66, 48, 58, jit=2, seed=13)),
  dome('front', top=6, w=50, cy=46, n=10, amp=10, seed=13, sb=76) + [bun(50, 0, 12), L(outline([(40, 4), (50, -18, 1), (60, 4)])),
                                                                       side_lock(12, 66, 92), side_lock(88, 66, 92)],
  dome('side', top=6, w=48, cy=46, n=10, amp=10, seed=13, nape=88, fr=52) + [bun(40, 0, 12), L(outline([(32, 4), (40, -18, 1), (48, 4)]))],
  dome('back', top=6, w=50, cy=46, n=10, amp=10, seed=13, nape=90) + [bun(50, 0, 12)])

# Jor Braykur: ogro calvo de piel naranja, con colmillos que le salen de la boca, cejas en arco y orejas grandes
C('jor-braykur', 'corpulento', P('#e8a060', '#eca468', iris='#1e1e1e'),
  F(eyes='closed', brows=True, mouth='line', mouth_y=96, hairline=False, big_ears=3, face_front=face(w=4, chin=106, jaw=3), face_side=face_side(chin=6, jaw=4)),
  [L(blob([(14, 60), (14, 30), (30, 8), (50, 2), (70, 8), (86, 30), (86, 60)], 8), 'skin'), tusk(34, 96, 1), tusk(66, 96, -1)],
  skull3('side') + [L(outline([(80, 98), (86, 86, 1), (88, 98)]), WHITE, 'f')],
  skull3('back'))

# Kakui Ten (portero): melena castaña en pinchos con una cresta amarilla, patillas que se juntan con la barba, cicatriz
# en la cara y dientes apretados
YEL = _c('#f0d020')
C('kakui-ten', 'corpulento', P('#6a4428', '#c48a58', iris='#7a3020', shade='#4c2e1a'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, face_front=face(w=2, chin=104), hairline=hl(4, 68, 48, 56, seed=14)),
  dome('front', top=6, w=52, cy=48, n=9, amp=12, seed=14, sb=94) + [L(outline([(40, 40), (44, 4), (50, -18, 1), (56, 4), (60, 40)]), YEL)] +
  [beard([(18, 86), (26, 98), (40, 106), (50, 114, 1), (60, 106), (74, 98), (82, 86), (78, 102), (62, 112), (50, 118), (38, 112), (22, 102)]),
   L([(28, 70), (44, 86)], _c('#e8c8a0'), 'f', False, False, 2.0)],
  dome('side', top=6, w=50, cy=48, n=9, amp=12, seed=14, nape=94, fr=56) + [L(outline([(40, 20), (52, -16, 1), (64, 14)]), YEL),
                                                                            beard([(54, 80), (70, 100), (86, 106), (76, 114), (56, 106)])],
  dome('back', top=6, w=52, cy=48, n=9, amp=12, seed=14, nape=94) + [L(outline([(40, 40), (44, 4), (50, -18, 1), (56, 4), (60, 40)]), YEL)])

# Kanchu Ko: pelo negro peinado hacia atrás en una coleta alta con un mechón blanco, cejas negras gruesas, ojos amarillos
# afilados, bigote blanco caído hasta la barbilla, perilla y pendientes dorados
GOLD = _c('#d8a830')
C('kanchu-ko', 'delgado', P('#1e1e24', TAN, iris='#e0b020', shade='#101014'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=94, face_front=face(chin=106), face_side=face_side(chin=6),
    hairline=[(10, 60), (22, 44), (50, 38), (78, 44), (90, 60)]),
  dome('front', top=10, w=44, cy=44, n=0, sb=62, seed=15) + [L(outline([(48, 14), (54, -10), (76, -18), (92, -10, 1), (70, -8), (60, 12)])),
                                                             L(quad((56, 2), (70, -12), (88, -10)), WHITE, 'f', False, False, 2.2)] +
  thick_brows(64, BLACK, 5, 15, 0.6, 14) +
  [L(outline([(40, 88), (34, 94), (32, 110, 1), (38, 96), (48, 90)]), WHITE, 'f'), L(outline([(60, 88), (66, 94), (68, 110, 1), (62, 96), (52, 90)]), WHITE, 'f'),
   L(outline([(46, 100), (50, 114, 1), (54, 100)]), WHITE, 'f'), L(ell(16, 84, 2.6, 2.6), GOLD, 'f'), L(ell(84, 84, 2.6, 2.6), GOLD, 'f')],
  dome('side', top=10, w=44, cy=44, n=0, nape=82, fr=38, seed=15) + [L(outline([(36, 10), (20, -10), (4, -12, 1), (16, -2), (28, 14)]))] +
  side_brow(64, BLACK, 5) + [L(outline([(80, 88), (78, 100), (78, 110, 1), (84, 98), (88, 90)]), WHITE, 'f'), L(ell(46, 82, 2.4, 2.4), GOLD, 'f')],
  dome('back', top=10, w=44, cy=44, n=0, nape=82, seed=15) + [L(outline([(44, 14), (50, -12), (60, -14), (56, 14)])),
                                                              L([(50, -10), (54, 10)], WHITE, 'f', False, False, 2.0)])

# Katsu (modelo 3D): melena morada casi negra en casco, flequillo recto, un moño redondo arriba y dos mechones largos que
# le caen por delante hasta el pecho; ojos castaños grandes
C('katsu', 'chica', P('#2e2434', LIGHT, iris='#5a3a2a', shade='#1e1824'),
  F(eyes='big', brows=True, mouth='line', mouth_y=92, hairline=[(8, 62), (50, 60), (92, 62)]),
  bowl3('front', top=6, side=82, fringe=60) + [bun(50, 0, 13), side_lock(16, 70, 112, wd=7), side_lock(84, 70, 112, wd=7)],
  bowl3('side', top=6, nape=92, fringe=60) + [bun(44, 0, 13), L(outline([(64, 70), (70, 70), (68, 110, 1)]), 'mid', 'f')],
  bowl3('back', top=6, nape=92) + [bun(50, 4, 13)])

# Keenan Mustard: sombrero vaquero marrón de ala ancha, pelo naranja que asoma por debajo y un pañuelo rojo que le tapa
# la nariz y la boca
BRN, BRD, BAND = _c('#6e4434'), _c('#4c2e22'), _c('#2a1c18')
BAND_RED = _c('#d42a2a')
def _cowboy(view):
    if view == 'front':
        return [L(blob([(-12, 46), (10, 34), (50, 30), (90, 34), (112, 46), (104, 54), (50, 46), (-4, 54)], 6), BRN, 'f'),
                L(outline([(20, 38), (24, 6), (40, -6), (50, 0), (60, -6), (76, 6), (80, 38)]), BRN, 'f'),
                L(outline([(22, 30), (78, 30), (79, 38), (21, 38)]), BAND, 'f', False)]
    if view == 'side':
        return [L(blob([(-20, 40), (20, 34), (60, 30), (110, 36), (104, 46), (60, 42), (0, 48)], 6), BRN, 'f'),
                L(outline([(18, 36), (20, 4), (50, -6), (80, 4), (84, 36)]), BRN, 'f'), L(outline([(19, 28), (83, 28), (84, 36), (18, 36)]), BAND, 'f', False)]
    return [L(blob([(-12, 48), (10, 36), (50, 32), (90, 36), (112, 48), (104, 56), (50, 48), (-4, 56)], 6), BRD, 'f'),
            L(outline([(20, 40), (24, 6), (50, -2), (76, 6), (80, 40)]), BRN, 'f'), L(outline([(22, 32), (78, 32), (79, 40), (21, 40)]), BAND, 'f', False)]
C('keenan-mustard', 'normal', P('#f09a28', LIGHT, iris='#1e1e1e', shade='#c8701c'),
  F(eyes='round', brows='angry', mouth='none', hairline=False),
  dome('front', top=26, w=48, cy=50, n=7, amp=8, seed=16, sb=82) + [L(outline([(20, 44), (40, 46), (34, 70, 1), (28, 56), (18, 66, 1)]), 'mid', 'f'),
                                                                     L(blob([(14, 82), (50, 80), (86, 82), (90, 106), (50, 116), (10, 106)], 6), BAND_RED, 'f')] + _cowboy('front'),
  dome('side', top=26, w=46, cy=50, n=7, amp=8, seed=16, nape=90, fr=56) + [L(blob([(48, 80), (92, 80), (94, 104), (62, 112)], 6), BAND_RED, 'f')] + _cowboy('side'),
  dome('back', top=26, w=48, cy=50, n=7, amp=8, seed=16, nape=92) + [L(blob([(10, 92), (50, 90), (90, 92), (86, 104), (50, 108), (14, 104)], 6), BAND_RED, 'f')] +
  _cowboy('back'))

# Kim Canter (Terberry): melena larga blanca lila con mechones verde agua que se enroscan como tentáculos, orejas
# puntiagudas, ojos azules con raya rosa
MINT = _c('#86e8cc')
C('kim-canter-terberry', 'chica', P('#e2dcee', PALE, iris='#3a6aa0', shade='#b8b0cc'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, hairline=[(8, 62), (22, 46), (40, 40), (56, 50), (64, 40), (82, 46), (92, 62)]),
  dome('front', top=0, w=46, cy=44, n=0, long=108, flare=6, seed=17) +
  [L(outline([(44, 36), (60, 34), (58, 60), (54, 96), (50, 112, 1), (46, 92), (48, 60)]), 'mid', 'f'),
   L(blob([(24, 14), (6, 6), (-8, 24), (4, 50), (14, 70), (10, 92), (16, 92), (22, 70), (14, 46), (4, 26), (12, 16)], 6), MINT, 'f'),
   L(blob([(78, 40), (96, 46), (104, 66), (96, 80), (88, 72), (94, 60), (86, 50)], 6), MINT, 'f'),
   L(ell(28, 70, 2, 3), _c('#e86aa0'), 'f', False), L(ell(72, 70, 2, 3), _c('#e86aa0'), 'f', False)],
  dome('side', top=0, w=46, cy=44, n=0, long=108, flare=6, fr=50, seed=17) + [L(blob([(30, 10), (2, 20), (-6, 50), (6, 80), (12, 76), (4, 50), (12, 26)], 6), MINT, 'f')],
  dome('back', top=0, w=46, cy=44, n=0, long=108, flare=6, seed=17) + [L(blob([(70, 10), (98, 24), (104, 60), (96, 90), (90, 86), (96, 58), (88, 26)], 6), MINT, 'f'),
                                                                       L(blob([(30, 10), (2, 24), (-4, 60), (4, 90), (10, 86), (4, 58), (12, 26)], 6), MINT, 'f')])

# Kippoji Ani (portero): pelo azul morado oscuro en pinchos con patillas largas y perilla, cejas gruesas, un ojo guiñado y
# un palillo en la boca
C('kippoji-ani', 'corpulento', P('#3a2c5c', '#f6cc98', iris='#3a6a3a', shade='#261c40'),
  F(eyes='sharp', brows=False, mouth='grin', mouth_y=94, face_front=face(w=2, chin=104, jaw=2), hairline=hl(5, 66, 46, 54, seed=18)),
  dome('front', top=4, w=50, cy=46, n=9, amp=9, seed=18, sb=94) + thick_brows(64, 'mid', 5, 15, 0.8, 15) +
  [L(ell(64, 76, 7, 4), 'skin', 'f', False), L(quad((58, 76), (64, 80), (70, 76)), OUTC, 'f', False, False, 1.6),
   beard([(16, 80), (22, 96), (34, 106), (40, 100), (28, 92)]), beard([(84, 80), (78, 96), (66, 106), (60, 100), (72, 92)]),
   beard([(44, 104), (50, 114, 1), (56, 104)]), stick((58, 95), (74, 100), _c('#d8b070'))],
  dome('side', top=4, w=48, cy=46, n=9, amp=9, seed=18, nape=90, fr=52) + side_brow(64, 'mid', 5) + [beard([(52, 74), (60, 96), (76, 104), (66, 106), (54, 96)])],
  dome('back', top=4, w=50, cy=46, n=9, amp=9, seed=18, nape=90))

# Kocho Kyo: cara roja de oni con una melena verde azulada que sube en dos cuernos de pelo y una gema roja arriba, barba
# verde, ojos en espiral y dientes apretados
TEAL, GEM = _c('#2a6a64'), _c('#c81e1e')
C('kocho-kyo', 'corpulento', P('#2a6a64', '#c8603e', iris='#1e1e1e', shade='#1c4a46'),
  F(eyes='round', brows=False, mouth='grin', mouth_y=96, face_front=face(w=3, chin=104, jaw=2), hairline=[(8, 66), (20, 52), (50, 46), (80, 52), (92, 66)]),
  dome('front', top=10, w=52, cy=48, n=8, amp=8, seed=19, sb=94) + [L(outline([(10, 40), (4, 14), (2, -8, 1), (20, 6), (30, 30)])),
                                                                     L(outline([(90, 40), (96, 14), (98, -8, 1), (80, 6), (70, 30)])),
                                                                     L(outline([(44, 8), (46, 0), (54, 0), (56, 8)]), GEM)] +
  [L(quad((24, 62), (36, 58), (44, 64)), 'deep', 'f', False, False, 3.0), L(quad((76, 62), (64, 58), (56, 64)), 'deep', 'f', False, False, 3.0),
   L(ell(36, 75, 8, 7) + [ell(36, 75, 8, 7)[0]], TEAL, 'f', False, False, 2.6), L(ell(64, 75, 8, 7) + [ell(64, 75, 8, 7)[0]], TEAL, 'f', False, False, 2.6),
   beard([(20, 92), (30, 106), (50, 116, 1), (70, 106), (80, 92), (70, 100), (50, 104), (30, 100)])],
  dome('side', top=10, w=50, cy=48, n=8, amp=8, seed=19, nape=94, fr=52) + [L(outline([(40, 20), (48, -8, 1), (60, 16)])),
                                                                            beard([(56, 88), (74, 104), (88, 108), (72, 116), (54, 104)])],
  dome('back', top=10, w=52, cy=48, n=8, amp=8, seed=19, nape=96) + [L(outline([(10, 40), (4, 14), (2, -8, 1), (20, 6), (30, 30)])),
                                                                     L(outline([(90, 40), (96, 14), (98, -8, 1), (80, 6), (70, 30)]))])

# Kojuro Katsuragi: pelo verde oscuro abultado en rizos grandes con una goma naranja arriba, cejas verdes en rizo, bigotes
# de gato y un colmillo
ORG = _c('#e88a2a')
C('kojuro-katsuragi', 'normal', P('#3a5c2e', '#f6d29a', iris='#3a7a3a', shade='#26401e'),
  F(eyes='big', brows=False, mouth='buck', mouth_y=94, hairline=[(6, 66), (14, 50), (30, 42), (50, 46), (70, 42), (86, 50), (94, 66)]),
  dome('front', top=0, w=52, cy=46, n=10, amp=7, soft=True, seed=20, sb=86) + [bun(50, -2, 12), L(ell(50, 6, 4, 3), ORG)] +
  [L(blob([(26, 64), (38, 58), (44, 66), (36, 64), (30, 70)], 4), 'mid', 'f'), L(blob([(74, 64), (62, 58), (56, 66), (64, 64), (70, 70)], 4), 'mid', 'f')] +
  [L([(18, 86), (28, 88)], OUTC, 'f', False, False, 1.0), L([(18, 92), (28, 90)], OUTC, 'f', False, False, 1.0),
   L([(82, 86), (72, 88)], OUTC, 'f', False, False, 1.0), L([(82, 92), (72, 90)], OUTC, 'f', False, False, 1.0)],
  dome('side', top=0, w=50, cy=46, n=10, amp=7, soft=True, seed=20, nape=92, fr=52) + [bun(42, -2, 12)],
  dome('back', top=0, w=52, cy=46, n=10, amp=7, soft=True, seed=20, nape=92) + [bun(50, -2, 12), L(ell(50, 6, 4, 3), ORG)])

# Konano Futsuno: pelo castaño oscuro recogido en un moño ahuecado con una diadema naranja, dos mechones finos que le caen
# junto a la cara; ojos verdes y mejillas sonrosadas
PINK = _c('#f4a0a0')
C('konano-futsuno', 'chica', P('#4a3426', LIGHT, iris='#3a8a5a', shade='#34241a'),
  F(eyes='big', brows=True, mouth='frown', mouth_y=93, hairline=[(8, 66), (16, 50), (34, 42), (50, 46), (66, 42), (84, 50), (92, 66)]),
  [bun(50, 10, 20)] + dome('front', top=2, w=46, cy=44, n=0, sb=80, seed=21) + [L(quad((26, 10), (50, -2), (74, 10)), ORG, 'f', False, False, 3.0),
                                                            side_lock(14, 70, 108, wd=4), side_lock(86, 70, 108, wd=4),
                                                            L(ell(30, 86, 5, 3), PINK, 'f', False), L(ell(70, 86, 5, 3), PINK, 'f', False)],
  dome('side', top=2, w=46, cy=44, n=0, nape=84, fr=48, seed=21) + [bun(18, 30, 16)],
  dome('back', top=2, w=46, cy=44, n=0, nape=84, seed=21) + [bun(50, 50, 18)])

# Konomi Kodawara: pelo verde muy oscuro en un moño alto con una peineta rosa y pinchos de pelo que salen de él; piel
# morena, ojos granate afilados y una bufanda a rayas magenta
COMB, SCF = _c('#e0a0d0'), _c('#c04898')
C('konomi-kodawara', 'chica', P('#1a3a34', TAN, iris='#8a1e2e', shade='#102824'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=92, hairline=[(8, 66), (20, 50), (34, 42), (50, 58), (66, 42), (80, 50), (92, 66)]),
  dome('front', top=6, w=46, cy=46, n=0, sb=74, seed=22) + [bun(50, 2, 15), L(blob([(36, -6), (50, -14), (64, -6), (60, 2), (40, 2)], 5), COMB, 'f'),
                                                            L(quad((38, 0), (20, -18), (8, -10)), 'mid', 'b', True, False, 2.4),
                                                            L(quad((62, 0), (80, -18), (92, -10)), 'mid', 'b', True, False, 2.4)] + scarf('front', SCF, 100, 12),
  dome('side', top=6, w=46, cy=46, n=0, nape=86, fr=50, seed=22) + [bun(40, 2, 15)] + scarf('side', SCF, 100, 12),
  dome('back', top=6, w=46, cy=46, n=0, nape=86, seed=22) + [bun(50, 4, 15), L(blob([(36, -4), (50, -12), (64, -4), (60, 4), (40, 4)], 5), COMB, 'f')] +
  scarf('back', SCF, 100, 12))

# Kwa Fiyur: cresta azul alta curvada hacia delante sobre la cabeza rapada, con una línea de pelo que baja por los lados;
# ojos verde agua afilados
C('kwa-fiyur', 'normal', P('#2a7ac8', '#c99060', iris='#2a8a8a', shade='#1c5a9a'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=93, hairline=False),
  [L(blob([(16, 62), (16, 34), (30, 14), (50, 8), (70, 14), (84, 34), (84, 62)], 8), 'skin'),
   L(outline([(16, 66), (18, 40), (36, 30), (36, 40), (24, 50), (22, 66)])), L(outline([(84, 66), (82, 40), (64, 30), (64, 40), (76, 50), (78, 66)])),
   L(outline([(40, 40), (40, 14), (52, -14), (62, -32, 1), (60, -6), (60, 40), (50, 50, 1)]))],
  skull3('side') + [L(outline([(30, 30), (40, 0), (60, -20), (78, -30, 1), (74, -8), (64, 20), (60, 40)]))],
  skull3('back') + [L(outline([(40, 70), (40, 10), (50, -14), (60, 10), (60, 70)]))])

# Kyohi Sho (portera): melena rosa con forma de campana y un lazo blanco arriba con dos cuentas verde agua a los lados;
# ojos lila y mejillas sonrosadas
BEAD = _c('#2a9a8a')
C('kyohi-sho', 'chica', P('#e090b4', PALE, iris='#8a5aa0', shade='#b86890'),
  F(eyes='big', brows=True, mouth='line', mouth_y=92, hairline=[(8, 62), (22, 52), (40, 58), (50, 50), (60, 58), (78, 52), (92, 62)]),
  dome('front', top=8, w=50, cy=46, n=0, long=108, flare=8, seed=23) +
  [L(outline([(42, 8), (32, -10), (40, -12), (48, 4)]), WHITE), L(outline([(58, 8), (68, -10), (60, -12), (52, 4)]), WHITE), L(ell(50, 8, 5, 4), WHITE),
   L(ell(16, 16, 4, 4), BEAD), L(ell(84, 16, 4, 4), BEAD), L(ell(30, 86, 5, 3), PINK, 'f', False), L(ell(70, 86, 5, 3), PINK, 'f', False)],
  dome('side', top=8, w=50, cy=46, n=0, long=108, flare=8, fr=56, seed=23) + [L(ell(46, 6, 6, 5), WHITE), L(ell(30, 14, 4, 4), BEAD)],
  dome('back', top=8, w=50, cy=46, n=0, long=108, flare=8, seed=23) + [L(ell(50, 8, 6, 5), WHITE), L(ell(16, 16, 4, 4), BEAD), L(ell(84, 16, 4, 4), BEAD)])

# Kyoko Hanabayashi (modelo 3D): pelo negro rizado en melena corta abultada, piel morena, ojos verdes y un lunar
C('kyoko-hanabayashi', 'chica', P('#24222a', '#c99060', iris='#4a8a3a', shade='#141218'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(8, 66), (18, 50), (30, 44), (44, 52), (58, 42), (76, 46), (92, 64)]),
  dome('front', top=2, w=50, cy=46, n=12, amp=6, soft=True, seed=24, sb=90) + [L(ell(70, 86, 1.2, 1.2), BLACK, 'f', False)],
  dome('side', top=2, w=48, cy=46, n=12, amp=6, soft=True, seed=24, nape=94, fr=50),
  dome('back', top=2, w=50, cy=46, n=12, amp=6, soft=True, seed=24, nape=94))

# La Hire (modelo 3D): pelo verde oliva en pinchos largos alborotados, con una trenza larga que le cae por un lado; ojos
# naranja con raya negra gruesa y ceño fruncido
C('la-hire', 'normal', P('#6a7a52', LIGHT, iris='#c87a20', shade='#4c5a3a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=hl(6, 66, 44, 58, jit=3, seed=25)),
  dome('front', top=2, w=52, cy=44, n=11, amp=14, seed=25, sb=80) +
  [L(rope((14, 70), (6, 100), (12, 122), 9), 'mid', 'f'), L(quad((24, 68), (36, 64), (44, 70)), BLACK, 'f', False, False, 2.4),
   L(quad((76, 68), (64, 64), (56, 70)), BLACK, 'f', False, False, 2.4)],
  dome('side', top=2, w=50, cy=44, n=11, amp=14, seed=25, nape=90, fr=50) + [L(rope((24, 80), (16, 100), (22, 120), 9), 'mid')],
  dome('back', top=2, w=52, cy=44, n=11, amp=14, seed=25, nape=90) + [L(rope((80, 80), (88, 100), (82, 122), 9), 'mid', 'f')])

# Lave Hato: pelo verde azulado corto con tres pinchos arriba, piel rojiza, cejas fruncidas y una sonrisa enorme de dientes
C('lave-hato', 'corpulento', P('#2a4e5a', '#c0664a', iris='#1e1e1e', shade='#1c3640'),
  F(eyes='round', brows='angry', mouth='grin', mouth_y=94, face_front=face(w=4, chin=104, jaw=3), hairline=[(6, 62), (20, 50), (50, 48), (80, 50), (94, 62)]),
  dome('front', top=16, w=46, cy=46, n=5, amp=11, seed=26, sb=62),
  dome('side', top=16, w=44, cy=46, n=5, amp=11, seed=26, nape=80, fr=48),
  dome('back', top=16, w=46, cy=46, n=5, amp=11, seed=26, nape=82))

# Leila Sway: melena azul marino ondulada y abultada que le tapa un ojo, con un moño en flor arriba y dos cuentas
# amarilla y verde; piel morena, ojos azules
BY, BT = _c('#f0c040'), _c('#40b0a0')
C('leila-sway', 'chica', P('#1e2a5a', '#d09868', iris='#3a8ac8', shade='#141c40'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(8, 66), (20, 50), (36, 44), (56, 48), (72, 44), (92, 64)]),
  dome('front', top=6, w=52, cy=48, n=8, amp=6, soft=True, seed=27, long=96, flare=8) +
  [L(outline([(20, 48), (44, 40), (48, 56), (40, 78, 1), (30, 70), (20, 66)]), 'mid', 'f'),
   L(blob([(64, 2), (74, -12), (86, -8), (84, 4), (74, 10)], 5)), L(ell(66, 6, 4, 3.5), BY), L(ell(72, 0, 3, 3), BT)],
  dome('side', top=6, w=50, cy=48, n=8, amp=6, soft=True, seed=27, long=96, flare=8, fr=56) + [L(blob([(50, 2), (60, -12), (72, -8), (70, 4)], 5))],
  dome('back', top=6, w=52, cy=48, n=8, amp=6, soft=True, seed=27, long=96, flare=8) + [L(blob([(36, 2), (26, -12), (14, -8), (16, 4)], 5))])

# Liana Moonicorn: melena larga rubia claro en tirabuzones, flequillo de mechones, ojos azul claro afilados y gesto serio
C('liana-moonicorn', 'chica', P('#f2dc8a', PALE, iris='#5ab0d0', shade='#c8a85a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=hl(6, 66, 46, 58, seed=28)),
  dome('front', top=2, w=50, cy=44, n=10, amp=5, soft=True, seed=28, long=116, flare=10),
  dome('side', top=2, w=48, cy=44, n=10, amp=5, soft=True, seed=28, long=116, flare=10, fr=52),
  dome('back', top=2, w=50, cy=44, n=10, amp=5, soft=True, seed=28, long=116, flare=10, ends=6))

# Lise La Transe: pelo negro largo con una coleta altísima que se curva hacia un lado, mechones finos junto a la cara;
# piel morena y ojos negros
C('lise-la-transe', 'chica', P('#141418', '#c08a58', iris='#141418', shade='#08080a'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=92, hairline=[(8, 62), (20, 46), (36, 40), (50, 46), (64, 40), (80, 46), (92, 62)]),
  dome('front', top=4, w=46, cy=44, n=0, sb=76, seed=29) + [L(outline([(46, 6), (50, -10), (70, -16), (92, -4), (96, 24), (86, 50, 1), (88, 20), (76, -4), (58, 2)])),
                                                            L(ell(50, -6, 4, 3), _c('#3ac0d0')), side_lock(14, 66, 114, wd=4), side_lock(86, 66, 114, wd=4)],
  dome('side', top=4, w=46, cy=44, n=0, nape=86, fr=48, seed=29) + [L(outline([(36, 6), (24, -12), (2, -10), (-10, 20), (-4, 60, 1), (0, 22), (12, 0), (40, 12)]))],
  dome('back', top=4, w=46, cy=44, n=0, nape=86, seed=29) + [L(outline([(44, 6), (50, -12), (70, -16), (92, -2), (96, 28), (86, 56, 1), (86, 22), (72, -4)]))])

# Lunete Taliesin: melena larga morada azulada y lisa con raya al medio, piel morena y sonrisa
C('lunete-taliesin', 'chica', P('#3c3496', '#d09868', iris='#2a2020', shade='#28226e'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=92, hairline=[(8, 62), (20, 48), (40, 42), (50, 44), (60, 42), (80, 48), (92, 62)]),
  dome('front', top=2, w=46, cy=44, n=0, long=118, flare=4, seed=30),
  dome('side', top=2, w=46, cy=44, n=0, long=118, flare=4, fr=50, seed=30),
  dome('back', top=2, w=46, cy=44, n=0, long=118, flare=4, seed=30))

# Lupin Wolfe: pelo crema blanco en pinchos altos echados hacia arriba, con un mechón verde agua; ojos rojos con ojeras
# oscuras y un pendiente de cereza
TEAL2, CHERRY = _c('#3a8a7a'), _c('#c81e2a')
C('lupin-wolfe', 'normal', P('#ece6c8', PALE, iris='#c81e2a', shade='#c8c09a'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=93, hairline=[(8, 64), (20, 48), (34, 40), (50, 44), (66, 40), (80, 48), (92, 64)]),
  [L(outline([(12, 70), (8, 40), (10, 6, 1), (24, 24), (30, -16, 1), (42, 12), (50, -30, 1), (58, 12), (70, -16, 1), (76, 24), (90, 6, 1), (92, 40), (88, 70), (80, 56),
              (20, 56)])), L(outline([(56, 10), (70, -16), (76, 24), (90, 6), (92, 40), (88, 66), (78, 40)]), 'shade', 'b', False),
   L(outline([(30, 10), (36, 40), (32, 70, 1), (28, 40)]), TEAL2, 'f'),
   L(quad((26, 74), (36, 82), (46, 74)), _c('#7a5a6a'), 'f', False, False, 1.6), L(quad((54, 74), (64, 82), (74, 74)), _c('#7a5a6a'), 'f', False, False, 1.6),
   L(ell(84, 84, 2.4, 2.4), CHERRY, 'f')],
  [L(outline([(56, 52), (62, 42), (82, 38), (96, 20), (90, 4, 1), (74, 10), (72, -24, 1), (56, 4), (40, -20, 1), (32, 8), (12, 0, 1), (8, 30), (6, 56), (22, 72), (40, 68),
              (52, 58)]))],
  [L(outline([(12, 76), (8, 40), (10, 6, 1), (24, 24), (30, -16, 1), (42, 12), (50, -30, 1), (58, 12), (70, -16, 1), (76, 24), (90, 6, 1), (92, 40), (88, 76), (50, 84)])),
   L(outline([(56, 10), (70, -16), (76, 24), (90, 6), (92, 40), (88, 74), (70, 60)]), 'shade', 'b', False)])

# Macha Green: melena larga lisa morada hasta el pecho con flequillo recto, ojos afilados y gesto enfadado
C('macha-green', 'chica', P('#3e2c8c', PALE, iris='#6a2a3a', shade='#2a1e66'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=[(8, 62), (30, 60), (50, 62), (70, 58), (92, 62)]),
  dome('front', top=2, w=46, cy=44, n=0, long=116, flare=4, seed=41) + [side_lock(84, 60, 118, wd=10, z='b')],
  dome('side', top=2, w=46, cy=44, n=0, long=116, flare=4, fr=58, seed=41),
  dome('back', top=2, w=46, cy=44, n=0, long=116, flare=4, seed=41))

# Mai Assam (Assamu): pelo castaño revuelto con mechones de punta y un mechón de antena, una coleta baja que le cae por
# un hombro; ojos rosas grandes y sonrisa
C('mai-assam-assamu', 'chica', P('#7a6250', LIGHT, iris='#d0607a', shade='#5a4636'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=hl(6, 66, 46, 60, jit=3, seed=42)),
  dome('front', top=2, w=48, cy=44, n=9, amp=7, seed=42, sb=88) + [L(quad((48, 4), (46, -10), (56, -14)), 'mid', 'b', True, False, 2.2),
                                                                   L(rope((78, 92), (92, 108), (80, 124), 9), 'mid', 'f')],
  dome('side', top=2, w=46, cy=44, n=9, amp=7, seed=42, nape=92, fr=52) + [L(rope((60, 92), (68, 108), (60, 124), 9), 'mid', 'f')],
  dome('back', top=2, w=48, cy=44, n=9, amp=7, seed=42, nape=92) + [L(rope((24, 92), (12, 108), (22, 124), 9), 'mid', 'f')])

# Marc Mystique (portero): pelo castaño rojizo ondulado echado a un lado, birrete gris de graduado, gafas redondas
# negras, pecas y barbilla larga
GREY, GREYD = _c('#7a7e86'), _c('#4e5258')
def _mortar(view):
    if view == 'front':
        return [L(outline([(30, 18), (70, 18), (68, 6), (32, 6)]), GREYD, 'f'), L(outline([(6, 4), (50, -8), (96, 4), (50, 14)]), GREY, 'f'),
                L([(88, 6), (92, 30)], _c('#e0c050'), 'f', False, False, 1.6)]
    if view == 'side':
        return [L(outline([(28, 18), (72, 18), (70, 6), (30, 6)]), GREYD, 'f'), L(outline([(4, 6), (60, -6), (98, 4), (40, 14)]), GREY, 'f')]
    return [L(outline([(30, 18), (70, 18), (68, 6), (32, 6)]), GREYD, 'f'), L(outline([(6, 4), (50, -8), (96, 4), (50, 14)]), GREY, 'f')]
C('marc-mystique', 'delgado', P('#a8582e', '#f6c08a', iris='#3a6a8a', shade='#7c3e1e'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, glasses=BLACK, face_front=face(chin=108, jaw=-2), face_side=face_side(chin=8),
    hairline=[(8, 66), (14, 50), (30, 40), (50, 42), (70, 44), (90, 56)]),
  dome('front', top=14, w=48, cy=46, n=6, amp=5, soft=True, sweep=-0.6, seed=43, sb=84) +
  [L(outline([(10, 50), (6, 70), (14, 88, 1), (20, 70), (22, 54)]), 'mid', 'f')] + _mortar('front') +
  [L(ell(30, 86, 1, 1), _c('#a05a30'), 'f', False), L(ell(34, 88, 1, 1), _c('#a05a30'), 'f', False), L(ell(66, 88, 1, 1), _c('#a05a30'), 'f', False),
   L(ell(70, 86, 1, 1), _c('#a05a30'), 'f', False)],
  dome('side', top=14, w=46, cy=46, n=6, amp=5, soft=True, seed=43, nape=88, fr=50) + _mortar('side'),
  dome('back', top=14, w=48, cy=46, n=6, amp=5, soft=True, seed=43, nape=90) + _mortar('back'))

# Masaichi Motoyoshi: pelo azul marino en pinchos con un moño alto y un mechón largo que le tapa un ojo; ojo azul grande
C('masaichi-motoyoshi', 'normal', P('#1e3462', LIGHT, iris='#3a6aa0', shade='#142446'),
  F(eyes='big', brows='angry', mouth='frown', mouth_y=93, hairline=hl(5, 66, 46, 56, seed=44)),
  dome('front', top=6, w=48, cy=46, n=8, amp=9, seed=44, sb=84) + [bun(52, -2, 10), L(outline([(46, 2), (52, -16, 1), (58, 2)])),
                                                                   L(outline([(16, 46), (48, 40), (52, 60), (46, 86, 1), (36, 76), (22, 70)]), 'mid', 'f')],
  dome('side', top=6, w=46, cy=46, n=8, amp=9, seed=44, nape=90, fr=52) + [bun(40, -2, 10)],
  dome('back', top=6, w=48, cy=46, n=8, amp=9, seed=44, nape=90) + [bun(52, 0, 10)])

# Matsuri Chai: pelo gris verdoso oscuro recogido en una coleta alta con una goma gris, mechones largos a los lados; gafas
# redondas finas, ojos ámbar y sonrisa
C('matsuri-chai', 'chica', P('#3e4a40', LIGHT, iris='#c88a20', shade='#2a342c'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, glasses=_c('#9a9aa0'), hairline=[(8, 64), (20, 48), (36, 42), (52, 50), (68, 42), (84, 50), (92, 64)]),
  dome('front', top=6, w=46, cy=46, n=0, sb=80, seed=45) + [bun(56, -2, 14), L(ell(54, 10, 5, 3), _c('#9aa0a8')),
                                                            L(outline([(10, 66), (18, 66), (22, 100), (14, 112, 1), (8, 96)])),
                                                            L(outline([(90, 66), (82, 66), (78, 100), (86, 112, 1), (92, 96)]))],
  dome('side', top=6, w=46, cy=46, n=0, nape=88, fr=50, seed=45) + [bun(30, -2, 14), L(outline([(26, 4), (10, 20), (6, 50, 1), (18, 28), (32, 12)]))],
  dome('back', top=6, w=46, cy=46, n=0, nape=88, seed=45) + [bun(50, 0, 14), L(outline([(44, 8), (40, 40), (50, 60, 1), (60, 40), (56, 8)]))])

# May Mayfair (Fayeux): melena crema enorme y esponjosa en mechones, y una máscara marrón cosida que le tapa la frente y
# la nariz con agujeros para los ojos
MASK, MASKD = _c('#7a4a1e'), _c('#4e2e10')
C('may-mayfair-fayeux', 'chica', P('#f6ecc0', LIGHT, iris='#1e1e1e', shade='#d8c890'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=94, hairline=[(8, 62), (22, 48), (50, 44), (78, 48), (92, 62)]),
  dome('front', top=-6, w=56, cy=44, n=10, amp=12, soft=True, seed=46, sb=88) +
  [L(blob([(22, 64), (34, 56), (50, 58), (66, 56), (78, 64), (76, 84), (62, 94), (50, 96), (38, 94), (24, 84)], 6), MASK, 'f'),
   L(ell(36, 76, 6.5, 6), WHITE, 'f', False), L(ell(64, 76, 6.5, 6), WHITE, 'f', False), L(ell(37, 77, 3, 3.6), BLACK, 'f', False),
   L(ell(63, 77, 3, 3.6), BLACK, 'f', False), L([(50, 60), (50, 90)], MASKD, 'f', False, False, 1.4), L([(46, 66), (54, 66)], MASKD, 'f', False, False, 1.2),
   L([(46, 72), (54, 72)], MASKD, 'f', False, False, 1.2)],
  dome('side', top=-6, w=54, cy=44, n=10, amp=12, soft=True, seed=46, nape=94, fr=52) +
  [L(blob([(64, 60), (90, 58), (94, 86), (78, 94), (66, 86)], 6), MASK, 'f'), L(ell(82, 76, 4, 5), WHITE, 'f', False), L(ell(83, 77, 2.4, 3.2), BLACK, 'f', False)],
  dome('back', top=-6, w=56, cy=44, n=10, amp=12, soft=True, seed=46, nape=96))

# Meg (Meggi) Imai (portera): melena larga azul con tres cuernos de pelo trenzado arriba, gafas redondas negras muy
# gruesas, ojos verde agua, piel morena y boca abierta sonriente
C('meg-meggi-imai', 'chica', P('#1e5a96', '#c99060', iris='#3ab0b0', shade='#143e6a'),
  F(eyes='big', brows=False, mouth='grin', mouth_y=94, hairline=[(8, 62), (22, 50), (50, 46), (78, 50), (92, 62)]),
  dome('front', top=6, w=46, cy=46, n=0, long=116, flare=4, seed=47) +
  [L(outline([(42, 10), (50, -16, 1), (58, 10)])), L(outline([(16, 22), (8, -2, 1), (30, 8)])), L(outline([(84, 22), (92, -2, 1), (70, 8)]))] +
  [L(ell(36, 76, 10, 9) + [ell(36, 76, 10, 9)[0]], BLACK, 'f', False, False, 3.0), L(ell(64, 76, 10, 9) + [ell(64, 76, 10, 9)[0]], BLACK, 'f', False, False, 3.0),
   L([(46, 75), (54, 75)], BLACK, 'f', False, False, 2.4)],
  dome('side', top=6, w=46, cy=46, n=0, long=116, flare=4, fr=52, seed=47) +
  [L(outline([(40, 10), (48, -16, 1), (56, 10)])), L(ell(81, 76, 6, 8) + [ell(81, 76, 6, 8)[0]], BLACK, 'f', False, False, 3.0)],
  dome('back', top=6, w=46, cy=46, n=0, long=116, flare=4, seed=47) +
  [L(outline([(42, 10), (50, -16, 1), (58, 10)])), L(outline([(16, 22), (8, -2, 1), (30, 8)])), L(outline([(84, 22), (92, -2, 1), (70, 8)]))])

# Mei Gongzhu: pelo castaño rojizo peinado hacia atrás con una coleta larga que le cae por un lado, un adorno negro de
# dos cuernos arriba; ojos naranja afilados
ORN = _c('#22202a')
C('mei-gongzhu', 'chica', P('#a8462a', PALE, iris='#c8681e', shade='#7a2e1a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=92, hairline=[(8, 64), (18, 46), (34, 40), (52, 50), (66, 40), (82, 46), (92, 64)]),
  [L(outline([(28, 10), (20, -10, 1), (40, 2), (50, -4), (60, 2), (80, -10, 1), (72, 10)]), ORN)] + dome('front', top=4, w=46, cy=46, n=0, sb=82, seed=48) +
  [L(rope((80, 70), (98, 100), (86, 128), 10), 'mid', 'f')],
  dome('side', top=4, w=46, cy=46, n=0, nape=88, fr=50, seed=48) + [L(rope((30, 70), (14, 100), (28, 128), 10), 'mid'),
                                                                    L(outline([(30, 10), (24, -10, 1), (50, 4)]), ORN)],
  dome('back', top=4, w=46, cy=46, n=0, nape=88, seed=48) + [L(rope((24, 70), (8, 100), (20, 128), 10), 'mid', 'f'),
                                                             L(outline([(28, 10), (20, -10, 1), (40, 2), (50, -4), (60, 2), (80, -10, 1), (72, 10)]), ORN)])

# Mimi Ceylon (portera): melena larga gris parda y ondulada con un gran lazo rojo arriba, ojos verde amarillento y
# sonrisa con dientes
BOW = _c('#c41e28')
def _bow(y=0):
    return [L(blob([(50, y + 2), (24, y - 10), (14, y + 4), (24, y + 14)], 5), BOW), L(blob([(50, y + 2), (76, y - 10), (86, y + 4), (76, y + 14)], 5), BOW),
            L(ell(50, y + 2, 6, 5), BOW)]
C('mimi-ceylon', 'chica', P('#7a6e5a', PALE, iris='#9aa030', shade='#5a503e'),
  F(eyes='big', brows=True, mouth='grin', mouth_y=93, hairline=[(8, 62), (22, 48), (38, 44), (52, 54), (64, 44), (80, 48), (92, 62)]),
  dome('front', top=4, w=48, cy=46, n=6, amp=5, soft=True, long=116, flare=8, seed=49) + _bow(4),
  dome('side', top=4, w=48, cy=46, n=6, amp=5, soft=True, long=116, flare=8, fr=52, seed=49) + [L(blob([(40, 6), (20, -6), (14, 10), (30, 16)], 5), BOW)],
  dome('back', top=4, w=48, cy=46, n=6, amp=5, soft=True, long=116, flare=8, seed=49) + _bow(6))

# Mmor Pegg: pelo rojo cortado en una cúpula plana con los lados negros, un antifaz negro de líneas con dos discos sobre
# los ojos y sombra roja; orejas puntiagudas y sonrisa enorme
RD2 = _c('#a81e1e')
C('mmor-pegg', 'normal', P('#a01c1c', '#f4c896', iris='#d08a20', shade='#701212'),
  F(eyes='sharp', brows=False, mouth='grin', mouth_y=94, big_ears=2, hairline=[(10, 60), (14, 44), (50, 40), (86, 44), (90, 60)]),
  [L(outline([(14, 60), (12, 34), (20, 16), (80, 16), (88, 34), (86, 60), (80, 46), (20, 46)]), BLACK),
   L(blob([(22, 40), (22, 12), (50, 2), (78, 12), (78, 40)], 6)),
   L(quad((22, 74), (36, 64), (48, 72)), RD2, 'f', False, False, 3.0), L(quad((78, 74), (64, 64), (52, 72)), RD2, 'f', False, False, 3.0),
   L([(18, 66), (30, 66), (36, 72), (44, 72), (50, 66), (56, 72), (64, 72), (70, 66), (82, 66)], BLACK, 'f', False, False, 1.8),
   L(ell(40, 76, 3.4, 3.4), BLACK, 'f', False), L(ell(60, 76, 3.4, 3.4), BLACK, 'f', False)],
  [L(outline([(54, 60), (40, 60), (10, 48), (8, 26), (20, 14), (50, 6), (78, 10), (86, 30), (80, 44), (60, 44)]), BLACK),
   L(blob([(20, 36), (20, 12), (50, 2), (80, 10), (84, 34)], 6)), L([(60, 66), (90, 66)], BLACK, 'f', False, False, 1.8), L(ell(82, 74, 3, 3), BLACK, 'f', False)],
  [L(outline([(14, 76), (12, 34), (20, 16), (80, 16), (88, 34), (86, 76), (50, 84)]), BLACK), L(blob([(22, 44), (22, 12), (50, 2), (78, 12), (78, 44)], 6))])

# Munetsugu Niseya: pelo verde oscuro ondulado hasta el cuello con dos lazadas de pelo arriba y una cinta blanca con la
# punta rosa en la frente; ojos afilados y sonrisa
C('munetsugu-niseya', 'normal', P('#2c5442', LIGHT, iris='#2a3a3a', shade='#1e3a2e'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=92, hairline=[(8, 66), (18, 54), (50, 58), (82, 54), (92, 66)]),
  dome('front', top=4, w=48, cy=46, n=7, amp=5, soft=True, long=104, flare=6, seed=50) +
  [L(ell(30, 6, 9, 7)), L(ell(70, 6, 9, 7)), L(outline([(14, 54), (50, 48), (86, 54), (86, 60), (50, 56), (14, 60)]), WHITE, 'f'),
   L(outline([(40, 50), (60, 50), (60, 56), (40, 56)]), _c('#e8a0b0'), 'f', False)],
  dome('side', top=4, w=46, cy=46, n=7, amp=5, soft=True, long=104, flare=6, fr=52, seed=50) +
  [L(ell(40, 6, 9, 7)), L(outline([(40, 50), (90, 52), (90, 58), (40, 58)]), WHITE, 'f')],
  dome('back', top=4, w=48, cy=46, n=7, amp=5, soft=True, long=104, flare=6, seed=50) +
  [L(ell(30, 6, 9, 7)), L(ell(70, 6, 9, 7)), L(outline([(10, 56), (90, 56), (90, 62), (10, 62)]), WHITE, 'f')])

# Nagahide Niwa (modelo 3D): pelo largo azul marino recogido atrás en una coleta alta hasta la espalda, con mechones
# largos que le caen junto a la cara y flequillo recto en mechones; ojos lila y una sonrisa ladeada
C('nagahide-niwa', 'normal', P('#262a6a', PALE, iris='#7a6aa8', shade='#1a1c4a'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=92, hairline=[(8, 62), (20, 58), (32, 62), (44, 58), (56, 62), (68, 58), (80, 62), (92, 62)]),
  dome('front', top=2, w=46, cy=44, n=0, long=118, flare=2, seed=51),
  dome('side', top=2, w=46, cy=44, n=0, nape=88, fr=60, seed=51) + [L(outline([(80, 60), (88, 62), (88, 112), (82, 120, 1), (78, 100)]), 'mid', 'f'),
                                                                    L(rope((20, 8), (-6, 50), (8, 116), 14), 'mid')],
  dome('back', top=2, w=46, cy=44, n=0, nape=88, seed=51) + [L(rope((50, 8), (42, 60), (50, 120), 16), 'mid', 'f'), L(ell(50, 14, 5, 3), 'deep', 'f')])

# Neville Foodcake: pelo rubio revuelto en mechones de punta, ojos azules y una bufanda gorda marrón clara abotonada
SCF2 = _c('#9a7a5a')
C('neville-foodcake', 'normal', P('#d8c050', LIGHT, iris='#3a5a90', shade='#a89030'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=hl(6, 66, 46, 60, jit=3, seed=52)),
  dome('front', top=2, w=50, cy=44, n=10, amp=10, seed=52, sb=78) + [L(blob([(4, 96), (30, 90), (50, 96), (74, 90), (96, 96), (98, 118), (50, 124), (2, 118)], 6), SCF2, 'f'),
                                                                     L(ell(70, 104, 2.4, 2.4), _c('#5a4430'), 'f', False)],
  dome('side', top=2, w=48, cy=44, n=10, amp=10, seed=52, nape=88, fr=52) + [L(blob([(26, 94), (60, 90), (92, 94), (94, 116), (60, 122), (24, 116)], 6), SCF2, 'f')],
  dome('back', top=2, w=50, cy=44, n=10, amp=10, seed=52, nape=88) + [L(blob([(4, 96), (50, 92), (96, 96), (98, 118), (50, 124), (2, 118)], 6), SCF2, 'f')])

# Nirasane Nebuka: pelo azul marino recogido en una coleta alta con goma roja, mechones largos junto a la cara y uno que
# vuela hacia un lado; ojos negros afilados y ceño fruncido
C('nirasane-nebuka', 'normal', P('#262e66', LIGHT, iris='#141414', shade='#1a1e48'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=[(8, 66), (20, 48), (34, 42), (50, 52), (66, 42), (80, 48), (92, 66)]),
  dome('front', top=6, w=46, cy=46, n=0, sb=74, seed=53) + [bun(50, -2, 12), L(ell(50, 8, 4, 3), _c('#c81e2a')),
                                                            L(outline([(12, 60), (20, 60), (22, 100), (16, 110, 1), (10, 96)])),
                                                            L(outline([(86, 60), (80, 64), (84, 82), (104, 92, 1), (90, 76)]))],
  dome('side', top=6, w=46, cy=46, n=0, nape=86, fr=50, seed=53) + [bun(36, -2, 12), L(outline([(30, 4), (14, 20), (10, 50, 1), (22, 26), (36, 12)]))],
  dome('back', top=6, w=46, cy=46, n=0, nape=86, seed=53) + [bun(50, 0, 12), L(outline([(44, 8), (40, 40), (50, 60, 1), (60, 40), (56, 8)]))])

# Nizo Koda: pelo verde oscuro en pinchos echados hacia arriba con un mechón blanco, piel morena, sonrisa de dientes y
# barbita
C('nizo-koda', 'normal', P('#264a3a', '#c48a58', iris='#3a5a7a', shade='#183428'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=93, hairline=hl(5, 64, 46, 54, lean=2, seed=54)),
  dome('front', top=-2, w=50, cy=44, n=8, amp=14, sweep=0.5, seed=54, sb=72) + [L(outline([(28, 40), (32, 10), (40, -10, 1), (40, 14), (36, 42)]), WHITE, 'f'),
                                                                                L([(44, 104), (56, 104)], OUTC, 'f', False, False, 1.2)],
  dome('side', top=-2, w=48, cy=44, n=8, amp=14, sweep=0.5, seed=54, nape=86, fr=48),
  dome('back', top=-2, w=50, cy=44, n=8, amp=14, sweep=0.5, seed=54, nape=86))

# Onor Doodad: melena negra azulada lisa con flequillo recto (por el que asoma la frente en franjas), unas gafas enormes
# de lentes rojas y una sonrisa ancha; piel amarillo pálido
C('onor-doodad', 'normal', P('#1e2048', '#f6ecb4', iris='#c81e1e', shade='#121430'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, hairline=[(8, 60), (30, 60), (34, 46), (38, 60), (62, 60), (66, 46), (70, 60), (92, 60)]),
  dome('front', top=2, w=46, cy=44, n=0, long=112, flare=2, seed=55) +
  [L(blob([(10, 70), (30, 64), (50, 70), (70, 64), (90, 70), (90, 84), (70, 88), (50, 82), (30, 88), (10, 84)], 6), _c('#e0e0e8'), 'f'),
   L(ell(34, 76, 7, 7), _c('#c8c8d0'), 'f', False), L(ell(66, 76, 7, 7), _c('#c8c8d0'), 'f', False),
   L(ell(34, 76, 4, 4), _c('#d01e2a'), 'f', False), L(ell(66, 76, 4, 4), _c('#d01e2a'), 'f', False)],
  dome('side', top=2, w=46, cy=44, n=0, long=112, flare=2, fr=58, seed=55) +
  [L(blob([(60, 66), (92, 66), (94, 86), (62, 86)], 6), _c('#e0e0e8'), 'f'), L(ell(84, 76, 4, 5), _c('#d01e2a'), 'f', False)],
  dome('back', top=2, w=46, cy=44, n=0, long=112, flare=2, seed=55))

# Ori Gami: melena azul marino en casco abultado con un moño pequeño arriba y un lazo rojo; ojos castaños y mejillas
# sonrosadas
C('ori-gami', 'chica', P('#262a6a', LIGHT, iris='#6a3a2a', shade='#1a1c4a'),
  F(eyes='big', brows=True, mouth='frown', mouth_y=93, hairline=[(8, 62), (50, 60), (92, 62)]),
  bowl3('front', top=6, side=92, w=6, fringe=60) + [bun(50, -2, 10)] + _bow(2) + [L(ell(30, 86, 5, 3), PINK, 'f', False), L(ell(70, 86, 5, 3), PINK, 'f', False)],
  bowl3('side', top=6, nape=94, w=6, fringe=60) + [bun(44, -2, 10)],
  bowl3('back', top=6, nape=94, w=6) + [bun(50, 0, 10)] + _bow(2))

# Pam Duff (portera): melena corta rosa en casco con flequillo, ojos enormes totalmente negros y una sonrisa
C('pam-duff', 'chica', P('#d89aa8', PALE, iris='#141414', shade='#b07888'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=93, hairline=[(8, 60), (30, 58), (50, 60), (70, 58), (92, 60)]),
  bowl3('front', top=4, side=96, fringe=60) + [L(ell(36, 76, 7, 8.5), BLACK, 'f', False), L(ell(64, 76, 7, 8.5), BLACK, 'f', False),
                                               L(ell(34, 73, 2, 2), WHITE, 'f', False), L(ell(62, 73, 2, 2), WHITE, 'f', False)],
  bowl3('side', top=4, nape=96, fringe=60) + [L(ell(82, 76, 4, 8), BLACK, 'f', False)],
  bowl3('back', top=4, nape=96))

# Peachy Keen: pelo gris azulado corto con una coleta alta, unas gafas de nieve naranjas sobre la frente y un pañuelo
# rosa anudado al cuello; ojos azules y sonrisa
GOG, GOGD, PSCF = _c('#f08a1e'), _c('#1e1e22'), _c('#f07890')
C('peachy-keen', 'chica', P('#6a8a96', LIGHT, iris='#3a7aa8', shade='#4c6a76'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=hl(5, 64, 50, 60, seed=56)),
  dome('front', top=6, w=48, cy=46, n=8, amp=7, seed=56, sb=86) + [bun(52, -4, 11),
                                                                   L(outline([(14, 30), (50, 24), (86, 30), (86, 44), (50, 40), (14, 44)]), GOGD, 'f'),
                                                                   L(outline([(20, 30), (48, 27), (48, 38), (20, 40)]), GOG, 'f', False),
                                                                   L(outline([(80, 30), (52, 27), (52, 38), (80, 40)]), GOG, 'f', False)] + scarf('front', PSCF, 100, 10),
  dome('side', top=6, w=46, cy=46, n=8, amp=7, seed=56, nape=88, fr=52) + [bun(34, -4, 11), L(outline([(30, 32), (90, 26), (92, 40), (30, 44)]), GOGD, 'f'),
                                                                           L(outline([(66, 28), (90, 26), (90, 38), (66, 40)]), GOG, 'f', False)] + scarf('side', PSCF, 100, 10),
  dome('back', top=6, w=48, cy=46, n=8, amp=7, seed=56, nape=88) + [bun(50, -2, 11), L(outline([(10, 34), (90, 34), (90, 42), (10, 42)]), GOGD, 'f')] +
  scarf('back', PSCF, 100, 10))

# Percival Travis (modelo 3D): adulto de pelo castaño oscuro con un flequillo largo echado a un lado que le tapa un ojo,
# perilla y bigote finos
C('percival-travis', 'delgado', P('#4e3e38', '#f0c08a', iris='#2a2020', shade='#342824'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=94, face_front=face(chin=106), face_side=face_side(chin=6),
    hairline=[(8, 62), (18, 48), (36, 42), (56, 46), (76, 44), (92, 60)]),
  dome('front', top=4, w=48, cy=46, n=7, amp=8, sweep=0.4, seed=57, sb=84) +
  [L(outline([(48, 40), (78, 40), (88, 56), (80, 84, 1), (70, 70), (58, 60)]), 'mid', 'f'),
   beard([(36, 100), (50, 98), (64, 100), (58, 108), (50, 112, 1), (42, 108)]), L([(42, 90), (58, 90)], 'mid', 'f', False, False, 1.6)],
  dome('side', top=4, w=46, cy=46, n=7, amp=8, sweep=0.4, seed=57, nape=90, fr=56) + [beard([(74, 98), (88, 98), (86, 110), (76, 110)])],
  dome('back', top=4, w=48, cy=46, n=7, amp=8, sweep=0.4, seed=57, nape=90))

# Phil de Rol: gorro de bufón rojo de dos puntas con cascabeles, y una máscara de payaso: gafas azules arriba, gafas negras
# sobre los ojos y labios azules
JR, JRD, BELL, MBLUE = _c('#a82020'), _c('#701414'), _c('#1e1e22'), _c('#4a8ab0')
def _jester(view):
    if view == 'front':
        return [L(outline([(4, 110), (0, 60), (-18, 52), (-30, 60, 1), (-14, 40), (14, 18), (40, 0), (50, -10, 1), (60, 0), (86, 18), (114, 40), (130, 60, 1), (118, 52),
                           (100, 60), (96, 110), (82, 110), (84, 62), (50, 52), (16, 62), (18, 110)]), JR, 'f'),
                L(ell(-30, 62, 4, 4), BELL, 'f'), L(ell(130, 62, 4, 4), BELL, 'f')]
    if view == 'side':
        return [L(outline([(60, 110), (66, 60), (80, 40), (100, 30), (120, 40, 1), (96, 20), (60, -6), (30, 0), (4, 20), (-20, 40, 1), (0, 36), (-4, 70), (0, 110)]), JR, 'f'),
                L(ell(120, 42, 4, 4), BELL, 'f')]
    return [L(outline([(4, 110), (0, 60), (-18, 52), (-30, 60, 1), (-14, 40), (14, 18), (40, 0), (50, -10, 1), (60, 0), (86, 18), (114, 40), (130, 60, 1), (118, 52),
                       (100, 60), (96, 110), (50, 116)]), JR, 'f'),
            L(outline([(50, -10), (60, 0), (86, 18), (100, 60), (96, 110), (60, 114), (66, 40)]), JRD, 'f', False)]
C('phil-de-rol', 'normal', P('#a82020', '#f6ecdc', iris='#1e1e1e'),
  F(eyes='none', brows=False, mouth='none', hairline=False),
  [L(blob([(18, 58), (50, 50), (82, 58), (84, 96), (50, 106), (16, 96)], 6), _c('#f4f0ea'), 'f')] + _jester('front') +
  [L(ell(38, 60, 7, 6), MBLUE, 'f'), L(ell(62, 60, 7, 6), MBLUE, 'f'), L(ell(38, 60, 3.6, 3), BLACK, 'f', False), L(ell(62, 60, 3.6, 3), BLACK, 'f', False),
   L(ell(50, 68, 3.6, 3), _c('#c83030'), 'f'), L(outline([(26, 72), (46, 72), (50, 76), (54, 72), (74, 72), (74, 84), (56, 84), (50, 80), (44, 84), (26, 84)]), WHITE, 'f'),
   L(ell(38, 78, 2.4, 3), BLACK, 'f', False), L(ell(62, 78, 2.4, 3), BLACK, 'f', False),
   L(blob([(34, 92), (50, 88), (66, 92), (60, 98), (50, 100), (40, 98)], 4), MBLUE, 'f')],
  [L(blob([(60, 56), (90, 58), (92, 96), (66, 104)], 6), _c('#f4f0ea'), 'f')] + _jester('side') +
  [L(ell(82, 60, 5, 6), MBLUE, 'f'), L(outline([(68, 72), (92, 72), (92, 84), (70, 84)]), WHITE, 'f'), L(ell(84, 78, 2, 3), BLACK, 'f', False),
   L(blob([(78, 92), (92, 90), (92, 98), (80, 98)], 4), MBLUE, 'f')],
  _jester('back'))

# Phil English: pelo rubio ceniza corto y revuelto con una coleta corta en la nuca, ojos castaños y una sonrisa abierta
C('phil-english', 'normal', P('#b0a47a', '#f0c08a', iris='#5a3a2a', shade='#8a7e56'),
  F(eyes='big', brows='angry', mouth='grin', mouth_y=93, hairline=hl(6, 66, 46, 58, jit=3, seed=58)),
  dome('front', top=2, w=48, cy=44, n=10, amp=8, seed=58, sb=74),
  dome('side', top=2, w=46, cy=44, n=10, amp=8, seed=58, nape=86, fr=50) + [L(rope((14, 80), (0, 96), (6, 110), 8))],
  dome('back', top=2, w=48, cy=44, n=10, amp=8, seed=58, nape=86) + [L(rope((50, 82), (58, 100), (52, 112), 9), 'mid', 'f')])

# Prince Charles (modelo 3D): melena larga blanca rosada y lisa con raya al medio, piel amarillo pálido, ojos afilados con
# ojeras y sonrisa torcida
C('prince-charles', 'delgado', P('#f2e2e6', '#f6ecc0', iris='#2a2020', shade='#d4bcc4'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, face_front=face(chin=106), face_side=face_side(chin=6),
    hairline=[(8, 62), (20, 48), (40, 40), (50, 42), (60, 40), (80, 48), (92, 62)]),
  dome('front', top=2, w=46, cy=44, n=0, long=120, flare=2, seed=59) +
  [L(quad((26, 80), (36, 84), (46, 80)), _c('#8a7a8a'), 'f', False, False, 1.4), L(quad((54, 80), (64, 84), (74, 80)), _c('#8a7a8a'), 'f', False, False, 1.4)],
  dome('side', top=2, w=46, cy=44, n=0, long=120, flare=2, fr=50, seed=59),
  dome('back', top=2, w=46, cy=44, n=0, long=120, flare=2, seed=59) + [L(outline([(40, 66), (60, 66), (60, 76), (40, 76)]), _c('#8a6a3e'), 'f')])
