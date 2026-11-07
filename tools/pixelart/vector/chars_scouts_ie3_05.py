"""Ojeadores de IE3 (scouts-ie3), tanda 05: dibujados a partir de su retrato de Victory Road (ninguno de esta tanda tiene
modelo 3D); claves 'scouts-ie3:<id>'. El perfil y la espalda se deducen del peinado del retrato. Reutiliza ayudas de las
tandas de IE1 e IE2 (dome/hl/face de ie1_09, bowl/cejas/gafas de ie1_03, calva/orejas/gafas redondas de ie2_03...)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars_scouts_ie1_02 import mir  # noqa: F401
from chars_scouts_ie1_03 import big_grin, blush, bowl, eyes_custom, fr, rect_specs, round_specs, side_brow, side_eye_custom, stache, thick_brows  # noqa: F401
from chars_scouts_ie1_09 import _c, dome, face, face_side, hl, mark  # noqa: F401
from chars_scouts_ie1_10 import nose_line, nose_tri, squint  # noqa: F401
from chars_scouts_ie2_03 import curls, ears_pointy, round_glasses, skull, teeth_grin  # noqa: F401
from chars_scouts_ie2_04 import band, lash_side, lashes, sharp_eye_side, sharp_eyes, strands_down  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401

K = 'scouts-ie3:'
WHITE = (250, 250, 250, 255)
BLACK = (24, 18, 20, 255)
LIP = (200, 96, 90, 255)
MOUTH = (110, 40, 40, 255)


def F(**k):
    d = {'eyes': 'normal', 'mouth': 'line'}
    d.update(k)
    return d


def P(hair, skin, iris='#302232', **k):
    return pal(hair, skin, iris, **k)


def C(pid, body, palette, f, front, side, back):
    """Como en la tanda 09 de IE1: el nacimiento del pelo baja por el borde de la cara para que su raya no cruce el pelo."""
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[K + pid] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def nose_ball(x=50, y=85, r=3.6, c=None):
    """Nariz redonda de color (bola) de frente."""
    return L(ell(x, y, r, r * 0.8), c or 'skin_d', 'f', False, True)


def beak(view, y=84, c=(232, 132, 40, 255)):
    """Nariz de pico naranja."""
    if view == 'front':
        return L([(46, y - 4), (54, y - 4), (50, y + 4)], c, 'f', False, True)
    return L([(84, y - 4), (94, y + 1), (85, y + 4)], c, 'f', False, True)


def tooth_mouth(y=94, w=8, h=5):
    """Boca apretada con los dientes a la vista."""
    return [L([(50 - w, y - h / 2), (50 + w, y - h / 2), (50 + w - 1, y + h / 2), (50 - w + 1, y + h / 2)], WHITE, 'f', False, True),
            L([(50 - w + 1, y), (50 + w - 1, y)], OUTC, 'f', False, False, 0.8)]


def side_teeth(y=94):
    return [L([(80, y - 2.5), (87, y - 3), (86, y + 2.5), (80, y + 2)], WHITE, 'f', False, True)]


def o_mouth(y=94, rx=3.4, ry=4.4, c=MOUTH):
    return L(ell(50, y, rx, ry), c, 'f', False, True)


def headphones(view, c, cup=None, y=70):
    """Cascos de música: el arco por encima de la cabeza y los dos auriculares en las orejas."""
    cup = cup or c
    if view == 'front':
        return [L(quad((10, y), (50, -22), (90, y)), c, 'f', False, False, 4.0),
                L(blob([(2, y - 10), (14, y - 12), (16, y + 10), (4, y + 12)], 4), cup, 'f'), L(blob([(98, y - 10), (86, y - 12), (84, y + 10), (96, y + 12)], 4), cup, 'f')]
    if view == 'side':
        return [L(quad((46, y - 8), (50, -10), (54, y - 8)), c, 'f', False, False, 4.0), L(ell(46, y, 9, 11), cup, 'f')]
    return [L(quad((10, y), (50, -22), (90, y)), c, 'f', False, False, 4.0),
            L(blob([(0, y - 10), (12, y - 12), (14, y + 10), (2, y + 12)], 4), cup, 'f'), L(blob([(100, y - 10), (88, y - 12), (86, y + 10), (98, y + 12)], 4), cup, 'f')]


# ------------------------------------------------------------------------------------------------------------- jugadores

# Paul Kerface (portero): pinchos castaño rojizo de punta hacia arriba; parche metálico gris con una cruz en el ojo derecho,
# sujeto con una cinta blanca que le cruza la frente; nariz redonda naranja, ojo afilado y sonrisa torcida de dientes
GRY, GRYD, NOS = _c('#8a8e92'), _c('#5a5e62'), _c('#d8763a')
def _patch(view):
    if view == 'front':
        return [L([(20, 72), (40, 64), (82, 50)], WHITE, 'f', False, False, 3.0), L(ell(36, 76, 9, 8.5), GRY, 'f'),
                L([(30, 70), (42, 82)], GRYD, 'f', False, False, 2.2), L([(42, 70), (30, 82)], GRYD, 'f', False, False, 2.2)]
    if view == 'side':
        return [L([(46, 60), (90, 54)], WHITE, 'f', False, False, 3.0)]
    return [L([(10, 58), (50, 54), (90, 58)], WHITE, 'f', False, False, 3.0)]
C('paul-stony-kerface', 'normal', P('#6b3530', '#c8915f', iris='#2a1a14'),
  F(eyes='sharp', brows='angry', mouth='none', face_front=face(w=4, chin=102, jaw=3), face_side=face_side(chin=2, jaw=3), big_ears=2, ear_out=3,
    hairline=hl(5, 62, 46, 56, jit=2, seed=3)),
  dome('front', top=-2, w=46, cy=44, n=7, amp=15, seed=31, sb=60) + _patch('front') + [nose_ball(50, 85, 4.2, NOS)] +
  tooth_mouth(95, 10, 5),
  dome('side', top=-2, w=46, cy=44, n=7, amp=15, seed=31, nape=82, fr=46) + _patch('side') + [L(ell(88, 84, 3.2, 3), NOS, 'f', False, True)] + side_teeth(95),
  dome('back', top=-2, w=46, cy=44, n=7, amp=15, seed=31, nape=82) + _patch('back'))

# Pauletta Porter: melena azul petróleo lisa hasta la barbilla, con un flequillo largo en mechones de punta que le cae
# hasta las cejas y un mechón en el centro; ojos azules afilados y labios finos
C('pauletta-rails-porter', 'chica', P('#4a90ac', '#fcefdc', iris='#3a5ab8', shade='#3a6e86', deep='#2c4e60'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=93, hairline=[(6, 70), (14, 64), (22, 70), (30, 62), (40, 70), (50, 74), (60, 70), (70, 62), (78, 70), (86, 64), (94, 70)]),
  dome('front', top=0, w=46, cy=46, long=96, flare=2, ends=3) + lashes(75),
  dome('side', top=0, w=46, cy=46, long=96, flare=2, fr=66) + lash_side(75),
  dome('back', top=0, w=46, cy=46, long=96, flare=2, ends=4))

# Pease Marrowfat: ogro de piel verde agua con la mandíbula enorme; pelo gris de pinchos con un pico que baja en rombo por la
# frente y mechones negros de punta por los lados; ojos blancos pequeños y ceño fruncido, morros verdes de enfado
OG, OGD, BLK = _c('#4a7a5a'), _c('#6e9c8c'), _c('#262a28')
C('pease-marrowfat', 'corpulento', P('#838483', '#8ab8a9', iris='#1a1a1a', shade='#6a6b6a'),
  F(eyes='round', brows='angry', mouth='none', face_front=face(w=7, chin=110, jaw=9), face_side=face_side(chin=8, jaw=8), ear_out=4,
    hairline=[(6, 62), (24, 50), (40, 52), (50, 66), (60, 52), (76, 50), (94, 62)], eye_y=76),
  [L(outline([(8, 76), (2, 58, 1), (10, 54), (4, 42, 1), (16, 46), (20, 60)]), BLK), L(outline([(92, 76), (98, 58, 1), (90, 54), (96, 42, 1), (84, 46), (80, 60)]), BLK)] +
  dome('front', top=-4, w=42, cy=40, n=7, amp=14, seed=33, sb=54) +
  [L(outline([(36, 46), (50, 40), (64, 46), (50, 68, 1)]), 'mid', 'f'), L(outline([(44, 48), (50, 46), (56, 48), (50, 60, 1)]), _c('#6a9a8c'), 'f', False),
   L(blob([(36, 96), (50, 92), (64, 96), (62, 103), (50, 100), (38, 103)], 5), OG, 'f'), L([(38, 98), (50, 95), (62, 98)], OUTC, 'f', False, False, 1.2),
   L(quad((30, 108), (50, 114), (70, 108)), OGD, 'f', False, False, 1.2)],
  [L(outline([(36, 76), (24, 60, 1), (36, 58), (30, 46, 1), (46, 52), (50, 68)]), BLK)] +
  dome('side', top=-4, w=42, cy=40, n=7, amp=14, seed=33, nape=80, fr=50) + [L(blob([(80, 95), (90, 93), (90, 102), (82, 102)], 4), OG, 'f')],
  [L(outline([(8, 80), (2, 58, 1), (12, 54), (6, 42, 1), (94, 42, 1), (88, 54), (98, 58, 1), (92, 80), (50, 86)]), BLK)] +
  dome('back', top=-4, w=42, cy=40, n=7, amp=14, seed=33, nape=80))

# Penny Linguine: pañuelo blanco crema atado tapándole todo el pelo hasta las cejas, con una franja rosa abajo; asoman rizos
# castaños por detrás de las orejas y lleva pendientes dorados; cara redonda, ojos de punto y la boca abierta en O
BAND, PNK, GOLD = _c('#ece6da'), _c('#d8a0a8'), _c('#e0b040')
def _kerchief(view):
    if view == 'front':
        return [L(outline([(12, 64), (12, 36), (28, 14), (50, 8), (72, 14), (88, 36), (88, 64), (50, 58)]), BAND),
                L(outline([(12, 58), (50, 52), (88, 58), (88, 64), (50, 59), (12, 64)]), PNK, 'b', False),
                L(blob([(60, 12), (82, 26), (88, 50), (76, 40)], 5), _c('#d0c8bc'), 'b', False)]
    if view == 'side':
        return [L(outline([(84, 56), (88, 40), (78, 16), (54, 6), (28, 8), (10, 22), (4, 46), (8, 68), (24, 72), (44, 62), (62, 58)]), BAND),
                L(outline([(8, 64), (40, 58), (86, 52), (86, 57), (40, 63), (10, 70)]), PNK, 'b', False),
                L(outline([(10, 66), (2, 82, 1), (16, 76), (14, 90, 1), (24, 74)]), BAND)]
    return [L(outline([(10, 70), (10, 36), (28, 12), (50, 6), (72, 12), (90, 36), (90, 70), (50, 76)]), BAND),
            L(outline([(10, 64), (50, 70), (90, 64), (90, 70), (50, 76), (10, 70)]), PNK, 'b', False),
            L(outline([(42, 72), (36, 92, 1), (50, 80), (64, 92, 1), (58, 72)]), BAND)]
C('penny-linguine', 'chica', P('#6e5a4a', '#fbbc7a', iris='#2a2020'),
  F(eyes='dot', brows=False, mouth='none', face_front=face(w=6, chin=104, jaw=5), hairline=False, eye_y=77),
  [L(curls(12, 74, (8, 11), 4)), L(curls(88, 74, (8, 11), 4))] + _kerchief('front') +
  [L(ell(10, 84, 2, 2), GOLD, 'f', False), L(ell(90, 84, 2, 2), GOLD, 'f', False),
   L([(46, 92), (54, 92), (50, 100)], _c('#e07850'), 'f', False, True)],
  [L(curls(34, 76, (10, 10), 4))] + _kerchief('side') + [L(ell(46, 82, 2, 2), GOLD, 'f', False)],
  [L(curls(16, 80, (9, 10), 4)), L(curls(84, 80, (9, 10), 4))] + _kerchief('back'))

# Percy Verens: pelo azul acero de pinchos echados hacia atrás y arriba, con dos mechones largos que le caen por los lados
# hasta la mandíbula; una tirita en la frente, ojos grandes redondos y sonrisa
TIR = _c('#f0c8a0')
C('percy-verens', 'normal', P('#4d708a', '#daa35b', iris='#1a1a1a', shade='#3a5468'),
  F(eyes='round', brows='angry', mouth='smile', mouth_y=93, hairline=[(6, 70), (14, 52), (24, 44), (50, 42), (76, 44), (86, 52), (94, 70)]),
  dome('front', top=-6, w=46, cy=40, n=6, amp=18, sweep=-0.6, seed=35, sb=60) +
  [L(outline([(18, 50), (8, 66), (10, 92, 1), (20, 76), (22, 60)])), L(outline([(82, 50), (92, 66), (90, 92, 1), (80, 76), (78, 60)])),
   L(blob([(38, 54), (62, 54), (62, 63), (38, 63)], 3), TIR, 'f'), L(blob([(44, 56), (56, 56), (56, 61), (44, 61)], 2), _c('#e0a888'), 'f', False)],
  dome('side', top=-6, w=46, cy=40, n=6, amp=18, sweep=-0.6, seed=35, nape=82, fr=46) +
  [L(outline([(54, 50), (46, 64), (50, 92, 1), (58, 74), (60, 58)])), L(blob([(76, 54), (88, 53), (88, 62), (76, 62)], 3), TIR, 'f')],
  dome('back', top=-6, w=46, cy=40, n=6, amp=18, sweep=-0.6, seed=35, nape=82))

# Pete Parrish: pelo rubio ceniza en casco liso con el flequillo recto cortado sobre las cejas, una gorra militar negra de
# plato con la chapa dorada encima; una cicatriz rosada le cruza la cara en diagonal; ojos oliva afilados y dientes apretados
CAPB, CAPG, SCAR = _c('#1e2220'), _c('#d8a830'), _c('#d89a86')
def _military(view):
    if view == 'front':
        return [L(blob([(22, 18), (30, 0), (50, -6), (70, 0), (78, 18), (50, 22)], 6), CAPB), L(outline([(20, 16), (50, 12), (80, 16), (80, 22), (50, 18), (20, 22)]), CAPG, 'f', False),
                L(ell(50, 12, 4.5, 4), CAPG, 'f'), L(ell(50, 12, 2, 2), CAPB, 'f', False)]
    if view == 'side':
        return [L(blob([(26, 18), (30, -2), (52, -8), (74, -2), (80, 16), (96, 22), (92, 26), (52, 22)], 6), CAPB), L([(28, 18), (80, 16)], CAPG, 'f', False, False, 2.4),
                L(ell(78, 12, 3, 3.5), CAPG, 'f')]
    return [L(blob([(22, 18), (30, 0), (50, -6), (70, 0), (78, 18), (50, 22)], 6), CAPB), L(outline([(20, 16), (50, 12), (80, 16), (80, 22), (50, 18), (20, 22)]), CAPG, 'f', False)]
C('pete-para-parrish', 'normal', P('#d5d0b0', '#f8dfc2', iris='#6a6a30', shade='#b4ae8c'),
  F(eyes='sharp', brows='angry', mouth='none', hairline=[(6, 64), (16, 62), (30, 63), (50, 63), (70, 63), (84, 62), (94, 64)]),
  bowl('front', top=10, side=88, w=2) + _military('front') +
  [L([(66, 40), (60, 60), (44, 78), (34, 96)], SCAR, 'f', False, False, 2.6)] + tooth_mouth(95, 7, 4),
  bowl('side', top=10, nape=92, w=2) + _military('side') + side_teeth(95),
  bowl('back', top=10, nape=92, w=2) + _military('back'))

# Pezi Miste: calvo con la cabeza alargadísima en forma de huevo y las orejas grandes; dos manchas negras redondas alrededor
# de los ojos blancos, como un antifaz, y una sonrisa enorme de dientes; un lunar en la barbilla
C('pezi-miste', 'delgado', P('#dea358', '#dea358', iris='#1a1a1a'),
  F(eyes='none', brows=False, mouth='none', face_front=face(w=-2, chin=106, jaw=0, top=10), face_side=face_side(chin=6), big_ears=2, ear_out=2, hairline=False),
  [L(outline([(18, 64), (16, 30), (26, 2), (50, -14), (74, 2), (84, 30), (82, 64), (50, 70)]), 'skin'),
   L(outline([(60, -10), (76, 4), (84, 32), (82, 60), (74, 30)]), 'skin_d', 'b', False),
   L(blob([(24, 72), (34, 66), (46, 72), (44, 84), (34, 86), (24, 82)], 5), BLACK, 'f', False), L(blob([(76, 72), (66, 66), (54, 72), (56, 84), (66, 86), (76, 82)], 5), BLACK, 'f', False),
   L(ell(36, 77, 3.8, 3.2), WHITE, 'f', False), L(ell(64, 77, 3.8, 3.2), WHITE, 'f', False),
   L(ell(36.5, 77, 1.5, 1.5), BLACK, 'f', False), L(ell(63.5, 77, 1.5, 1.5), BLACK, 'f', False)] + big_grin(92, 14, 9) + [L(ell(50, 106, 1.4, 1.4), BLACK, 'f', False)],
  [L(outline([(80, 56), (88, 36), (80, 8), (56, -12), (30, -8), (12, 12), (4, 44), (8, 70), (22, 84), (42, 84), (54, 70)]), 'skin'),
   L(blob([(74, 70), (88, 68), (90, 84), (76, 84)], 4), BLACK, 'f', False), L(ell(82, 76, 2.6, 3), WHITE, 'f', False), L(ell(83, 76, 1.2, 1.4), BLACK, 'f', False),
   L([(80, 90), (89, 90), (88, 96), (80, 95)], WHITE, 'f', False, True)],
  [L(outline([(16, 76), (12, 36), (24, 4), (50, -12), (76, 4), (88, 36), (84, 76), (50, 84)]), 'skin'),
   L(outline([(58, -8), (78, 8), (88, 40), (84, 72), (70, 40)]), 'skin_d', 'b', False)])

# Phil Debonair: melena ondulada azul petróleo oscuro hasta los hombros, con rizos que le caen por la cara; cascos verde lima
# con el arco por encima; ojos caídos medio cerrados, nariz larga y boca de desgana
LIME, LIMED = _c('#5ad040'), _c('#2a8a30')
C('phil-debonair', 'delgado', P('#28475a', '#e5d1b6', iris='#1a1a1a', shade='#1e3644'),
  F(eyes='sharp', brows=True, mouth='frown', mouth_y=96, face_front=face(w=-1, chin=106), face_side=face_side(chin=6, nose=3),
    hairline=[(6, 70), (18, 54), (30, 48), (46, 54), (60, 46), (76, 50), (90, 60), (94, 70)], nose=(50, 86, 2.4)),
  dome('front', top=2, w=48, cy=46, n=9, amp=6, soft=True, seed=37, long=104, flare=8, ends=4) +
  [L(outline([(32, 46), (24, 62), (28, 80), (22, 94, 1), (34, 80), (36, 60)]), 'mid', 'f'),
   L([(28, 72), (42, 73)], 'skin', 'f', False, False, 3.0), L([(58, 73), (72, 72)], 'skin', 'f', False, False, 3.0)] + headphones('front', LIME, LIMED, 74),
  dome('side', top=2, w=48, cy=46, n=9, amp=6, soft=True, seed=37, long=104, flare=8, fr=56) + [L([(74, 73), (86, 72)], 'skin', 'f', False, False, 3.0)] +
  headphones('side', LIME, LIMED, 74),
  dome('back', top=2, w=48, cy=46, n=9, amp=6, soft=True, seed=37, long=104, flare=8, ends=6) + headphones('back', LIME, LIMED, 74))

# Phil Harmonic: pelo castaño en casco con el flequillo recto, gafas rectangulares rojas, ojos grises, bufanda naranja al
# cuello y sonrisa
RED, SCARF = _c('#c83228'), _c('#f0a020')
C('phil-symphony-harmonic', 'normal', P('#715119', '#fbe8b8', iris='#8a8a90', shade='#5a3e12'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=93, hairline=[(6, 64), (14, 60), (30, 61), (50, 62), (70, 61), (86, 60), (94, 64)]),
  bowl('front', top=0, side=74) + rect_specs('front', RED, 76) +
  [L(blob([(24, 106), (50, 112), (76, 106), (78, 116), (50, 122), (22, 116)], 5), SCARF, 'f'), L(blob([(58, 112), (68, 112), (70, 134), (60, 134)], 4), SCARF, 'f')],
  bowl('side', top=0, nape=86) + rect_specs('side', RED, 76) + [L(blob([(40, 106), (88, 104), (88, 116), (40, 120)], 5), SCARF, 'f')],
  bowl('back', top=0, nape=86) + [L(blob([(20, 104), (50, 108), (80, 104), (80, 116), (50, 120), (20, 116)], 5), SCARF, 'f')])

# Phineas Hudd: pelo azul de pinchos revueltos que se abre a los lados, con un flequillo largo que le tapa el ojo derecho;
# encima, un casco gris con unas gafas de cristal blanco y cascos naranjas en las orejas; nariz de pico naranja, el ojo que
# se ve blanco y redondo, y los dientes apretados
HG, HGD, ORG, YEL = _c('#5a5a60'), _c('#3a3a40'), _c('#e8901e'), _c('#e8c040')
def _rig(view, oy=0):
    if view == 'front':
        return [L(blob([(26, 0 + oy), (74, 0 + oy), (76, 22 + oy), (24, 22 + oy)], 3), HG), L(blob([(28, 22 + oy), (72, 22 + oy), (70, 40 + oy), (30, 40 + oy)], 4), WHITE, 'f'),
                L(blob([(34, 26 + oy), (66, 26 + oy), (64, 36 + oy), (36, 36 + oy)], 3), _c('#d8a8b0'), 'f', False),
                L(quad((16, 46 + oy), (50, 30 + oy), (84, 46 + oy)), YEL, 'f', False, False, 3.0),
                L(ell(14, 44 + oy, 7, 7), ORG, 'f'), L(ell(86, 44 + oy, 7, 7), ORG, 'f')]
    if view == 'side':
        return [L(blob([(30, -2 + oy), (70, -2 + oy), (72, 20 + oy), (30, 22 + oy)], 3), HG), L(blob([(64, 22 + oy), (90, 24 + oy), (88, 40 + oy), (66, 40 + oy)], 4), WHITE, 'f'),
                L(ell(46, 40 + oy, 8, 8), ORG, 'f')]
    return [L(blob([(26, 0 + oy), (74, 0 + oy), (76, 22 + oy), (24, 22 + oy)], 3), HG), L(quad((14, 44 + oy), (50, 28 + oy), (86, 44 + oy)), YEL, 'f', False, False, 3.0),
            L(ell(14, 44 + oy, 7, 7), ORG, 'f'), L(ell(86, 44 + oy, 7, 7), ORG, 'f')]
C('phineas-phones-hudd', 'normal', P('#1e548c', '#e1d6c1', iris='#1a1a1a', shade='#173f6a'),
  F(eyes='none', brows=False, mouth='none', hairline=[(6, 70), (20, 52), (40, 50), (56, 56), (70, 52), (86, 56), (94, 70)]),
  dome('front', top=10, w=52, cy=52, n=9, amp=14, sweep=-0.3, seed=39, sb=76) +
  [L(outline([(24, 44), (52, 46), (46, 70), (40, 88, 1), (34, 74), (24, 62)]), 'mid', 'f')] + _rig('front') +
  [L(ell(64, 76, 5, 4.6), WHITE, 'f'), L(ell(65, 77, 1.4, 1.4), BLACK, 'f', False), L([(56, 68), (72, 70)], OUTC, 'f', False, False, 2.4),
   beak('front', 84, ORG)] + tooth_mouth(95, 7, 4),
  dome('side', top=10, w=50, cy=52, n=9, amp=14, sweep=-0.3, seed=39, nape=90, fr=56) + _rig('side') +
  [L(ell(81, 76, 3.2, 4), WHITE, 'f'), L(ell(82, 76, 1.2, 1.4), BLACK, 'f', False), beak('side', 84, ORG)] + side_teeth(95),
  dome('back', top=10, w=52, cy=52, n=9, amp=14, sweep=-0.3, seed=39, nape=90) + _rig('back'))

# Pius Fisher (portero): carota enorme y mofletuda; pelo negro corto pegado con un moño en cresta de aleta gris azulada
# encima y dos aletas más junto a las orejas; ojos de punto, nariz pequeña y boquita de pez
FIN, FIND = _c('#8aa8b0'), _c('#5a7a84')
C('pius-pisces-fisher', 'corpulento', P('#1e2424', '#fedebe', iris='#1a1a1a'),
  F(eyes='dot', brows=False, mouth='none', face_front=face(w=12, chin=110, jaw=12, top=30), face_side=face_side(chin=10, jaw=10), ear_out=10,
    hairline=[(6, 56), (24, 44), (50, 40), (76, 44), (94, 56)], nose=(50, 86, 2.2)),
  [L(outline([(10, 70), (-4, 60, 1), (2, 78), (12, 84)]), FIN), L(outline([(90, 70), (104, 60, 1), (98, 78), (88, 84)]), FIN)] +
  dome('front', top=14, w=38, cy=48, sb=52, shade=False) +
  [L(outline([(44, 18), (40, 4), (48, -14, 1), (56, -8), (60, 6), (56, 18)]), FIN), L(outline([(48, -8), (52, -12), (56, 2), (52, 16)]), FIND, 'f', False),
   L(ell(50, 96, 3.4, 2.6), _c('#c88a80'), 'f', False, True)],
  dome('side', top=14, w=38, cy=48, nape=74, fr=44, shade=False) +
  [L(outline([(42, 18), (36, 2), (40, -14, 1), (50, -6), (56, 8), (52, 18)]), FIN), L(outline([(40, 70), (24, 62, 1), (30, 80), (42, 82)]), FIN)],
  dome('back', top=14, w=38, cy=48, nape=74, shade=False) +
  [L(outline([(44, 18), (40, 4), (48, -14, 1), (56, -8), (60, 6), (56, 18)]), FIN),
   L(outline([(10, 70), (-4, 60, 1), (2, 78), (12, 84)]), FIN), L(outline([(90, 70), (104, 60, 1), (98, 78), (88, 84)]), FIN)])

# Placido Cannes (portero): carota ancha con un casco gris oscuro, unas gafas blancas de esquí subidas sobre la frente con la
# correa amarilla y cascos amarillos; el pelo morado le sale en pinchos por los lados y tiene perilla morada; ojos entornados,
# nariz de pico naranja y la boca recta
PUR = _c('#8a6aa0')
def _helm(view):
    if view == 'front':
        return [L(blob([(14, 50), (16, 22), (32, 6), (50, 2), (68, 6), (84, 22), (86, 50), (50, 46)], 6), HGD),
                L(blob([(22, 36), (78, 36), (76, 54), (60, 54), (50, 48), (40, 54), (24, 54)], 4), WHITE, 'f'),
                L(blob([(28, 40), (46, 40), (44, 50), (30, 50)], 3), _c('#d8a8b0'), 'f', False), L(blob([(54, 40), (72, 40), (70, 50), (56, 50)], 3), _c('#d8a8b0'), 'f', False),
                L(quad((18, 58), (50, 36), (82, 58)), YEL, 'f', False, False, 3.0), L(blob([(8, 54), (18, 52), (18, 72), (8, 72)], 3), YEL, 'f'),
                L(blob([(92, 54), (82, 52), (82, 72), (92, 72)], 3), YEL, 'f')]
    if view == 'side':
        return [L(outline([(84, 50), (88, 30), (76, 10), (52, 2), (28, 6), (10, 22), (4, 46), (8, 60), (40, 56), (60, 50)]), HGD),
                L(blob([(62, 36), (92, 36), (90, 54), (66, 54)], 4), WHITE, 'f'), L(blob([(38, 56), (52, 56), (52, 74), (38, 74)], 3), YEL, 'f')]
    return [L(blob([(12, 60), (14, 24), (32, 6), (50, 2), (68, 6), (86, 24), (88, 60), (50, 56)], 6), HGD), L(quad((14, 60), (50, 42), (86, 60)), YEL, 'f', False, False, 3.0),
            L(blob([(6, 54), (16, 52), (16, 72), (6, 72)], 3), YEL, 'f'), L(blob([(94, 54), (84, 52), (84, 72), (94, 72)], 3), YEL, 'f')]
C('placido-cans-cannes', 'corpulento', P('#8a6aa0', '#e5d3bb', iris='#1a1a1a', shade='#6a4e80'),
  F(eyes='none', brows=False, mouth='line', mouth_y=96, face_front=face(w=10, chin=106, jaw=10), face_side=face_side(chin=6, jaw=8), ears=False, hairline=False),
  [L(outline([(14, 60), (0, 56, 1), (8, 66), (-2, 76, 1), (10, 76), (4, 88, 1), (18, 82)])),
   L(outline([(86, 60), (100, 56, 1), (92, 66), (102, 76, 1), (90, 76), (96, 88, 1), (82, 82)]))] + _helm('front') +
  [L([(32, 72), (44, 74)], OUTC, 'f', False, False, 2.8), L([(68, 72), (56, 74)], OUTC, 'f', False, False, 2.8),
   L(ell(38, 77, 4.4, 2.6), WHITE, 'f', False), L(ell(62, 77, 4.4, 2.6), WHITE, 'f', False), L(ell(39, 78, 1.3, 1.3), BLACK, 'f', False), L(ell(61, 78, 1.3, 1.3), BLACK, 'f', False),
   beak('front', 86, ORG), L(blob([(36, 104), (50, 102), (64, 104), (58, 112), (50, 114), (42, 112)], 5), PUR, 'f')],
  [L(outline([(36, 58), (20, 56, 1), (28, 66), (18, 78, 1), (32, 76), (26, 88, 1), (42, 80)]))] + _helm('side') +
  [L([(74, 72), (86, 74)], OUTC, 'f', False, False, 2.8), L(ell(81, 78, 3, 2.4), WHITE, 'f', False), beak('side', 86, ORG),
   L(blob([(74, 104), (86, 102), (84, 112), (76, 112)], 4), PUR, 'f')],
  [L(outline([(14, 66), (0, 60, 1), (6, 72), (-2, 84, 1), (12, 82), (8, 94, 1), (22, 86), (50, 90), (78, 86), (92, 94, 1), (88, 82), (102, 84, 1), (94, 72), (100, 60, 1), (86, 66)]))] +
  _helm('back'))

# Pomponius Fanfair: pelo verde en capas de pinchos (verde claro arriba y verde oscuro por debajo), con un flequillo largo
# en punta que le tapa el ojo derecho; ojo castaño rojizo y sonrisa ladeada
GD = _c('#0a4a14')
C('pomponius-fanfair', 'normal', P('#79ab2b', '#f2c896', iris='#8a2a1a', shade='#5a8a1e'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=93, hairline=[(6, 70), (20, 60), (40, 58), (56, 64), (70, 58), (86, 62), (94, 70)]),
  [L(outline([(4, 74), (-4, 60, 1), (6, 56), (-2, 44, 1), (12, 44), (88, 44), (102, 44, 1), (94, 56), (104, 60, 1), (96, 74), (84, 64), (16, 64)]), GD)] +
  dome('front', top=-2, w=48, cy=40, n=9, amp=10, seed=41, sb=54) +
  [L(outline([(16, 44), (54, 44), (56, 64), (48, 84, 1), (42, 70), (34, 82, 1), (28, 64)]), 'mid', 'f'),
   L(outline([(34, 50), (52, 50), (50, 66), (44, 78, 1), (40, 62)]), GD, 'f', False)],
  [L(outline([(10, 80), (0, 62, 1), (10, 58), (4, 44, 1), (40, 44), (60, 60), (50, 82)]), GD)] +
  dome('side', top=-2, w=48, cy=40, n=9, amp=10, seed=41, nape=72, fr=50),
  [L(outline([(4, 84), (-2, 60, 1), (8, 52), (92, 52), (102, 60, 1), (96, 84), (82, 80), (70, 90, 1), (58, 82), (50, 92, 1), (42, 82), (30, 90, 1), (18, 80)]), GD)] +
  dome('back', top=-2, w=48, cy=40, n=9, amp=10, seed=41, nape=72))

# Poppy Workhard: melena enorme castaño rosado de ondas que terminan en rizos de caracola, con un mechón que vuela hacia un
# lado; ojos verdes grandes y sonrisa
C('poppy-workhard-playhard', 'chica', P('#cb9885', '#fdeec6', iris='#5a9a6a', shade='#a87462', deep='#7a4e43'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=[(6, 66), (14, 58), (28, 48), (44, 46), (56, 40), (70, 46), (84, 56), (94, 66)]),
  dome('front', top=-4, w=52, cy=44, n=9, amp=6, soft=True, seed=43, long=100, flare=10, ends=3) +
  [L(curls(14, 88, (12, 12), 5)), L(curls(86, 80, (12, 12), 5)), L(quad((98, 72), (112, 66), (114, 54)), 'mid', 'b', True, False, 4.0),
   L(quad((10, 82), (20, 92), (12, 96)), 'deep', 'f', False, False, 1.2), L(quad((84, 74), (92, 82), (84, 88)), 'deep', 'f', False, False, 1.2)] + lashes(75),
  dome('side', top=-4, w=52, cy=44, n=9, amp=6, soft=True, seed=43, long=100, flare=10, fr=50) + [L(curls(20, 86, (14, 14), 5))] + lash_side(75),
  dome('back', top=-4, w=52, cy=44, n=9, amp=6, soft=True, seed=43, long=100, flare=10, ends=4) + [L(curls(16, 90, (12, 12), 5)), L(curls(84, 90, (12, 12), 5))])

# Preston Creasefree: pinchos azul marino oscuro de punta hacia arriba y unos mechones que le caen por la frente; ojos azules
# afilados con el ceño muy fruncido y la boca apretada
C('preston-creasefree', 'normal', P('#1b293e', '#f8bc7e', iris='#2a5aa8', shade='#121c2c'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 66), (16, 54), (28, 60), (40, 50), (50, 58), (60, 50), (72, 60), (84, 54), (94, 66)]),
  dome('front', top=-8, w=46, cy=42, n=8, amp=18, seed=45, sb=62),
  dome('side', top=-8, w=46, cy=42, n=8, amp=18, seed=45, nape=82, fr=50),
  dome('back', top=-8, w=46, cy=42, n=8, amp=18, seed=45, nape=82))

# Preston Digitator: pelo negro muy corto pegado a la cabeza, piel morena, ojos negros afilados, arrugas de ceño en la
# frente y la boca apretada
C('preston-digitator', 'normal', P('#3a3632', '#c8905f', iris='#1a1a1a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 62), (16, 48), (32, 42), (50, 40), (68, 42), (84, 48), (94, 62)]),
  dome('front', top=8, w=44, cy=46, sb=58, shade=False) + [L([(58, 58), (64, 54)], _c('#9a6a46'), 'f', False, False, 1.2), L([(60, 62), (66, 58)], _c('#9a6a46'), 'f', False, False, 1.2)],
  dome('side', top=8, w=44, cy=46, nape=78, fr=42, shade=False),
  dome('back', top=8, w=44, cy=46, nape=78, shade=False))

# Quincy Wang: pelo azul marino oscuro peinado hacia atrás que cae en dos mechones abiertos junto a la mandíbula, una cinta
# roja fina y un gorrito de caja rojo a rayas blancas encima; cejas gruesas de kabuki, ceño fruncido y una borla roja en la
# barbilla
FEZ, FEZB = _c('#c82a2a'), _c('#7a4a3a')
def _fez(view):
    if view == 'front':
        return [L(blob([(38, 0), (62, 0), (62, 12), (38, 12)], 2), FEZB), L(blob([(38, -24), (62, -24), (62, 2), (38, 2)], 2), FEZ),
                L([(44, -22), (44, 0)], WHITE, 'f', False, False, 1.6), L([(50, -22), (50, 0)], WHITE, 'f', False, False, 1.6), L([(56, -22), (56, 0)], WHITE, 'f', False, False, 1.6),
                L(quad((14, 56), (50, 26), (86, 56)), FEZ, 'f', False, False, 2.0)]
    if view == 'side':
        return [L(blob([(40, 0), (64, 0), (64, 12), (40, 12)], 2), FEZB), L(blob([(40, -24), (64, -24), (64, 2), (40, 2)], 2), FEZ),
                L([(48, -22), (48, 0)], WHITE, 'f', False, False, 1.6), L([(56, -22), (56, 0)], WHITE, 'f', False, False, 1.6), L([(10, 46), (86, 40)], FEZ, 'f', False, False, 2.0)]
    return [L(blob([(38, 0), (62, 0), (62, 12), (38, 12)], 2), FEZB), L(blob([(38, -24), (62, -24), (62, 2), (38, 2)], 2), FEZ),
            L([(44, -22), (44, 0)], WHITE, 'f', False, False, 1.6), L([(56, -22), (56, 0)], WHITE, 'f', False, False, 1.6), L(quad((12, 58), (50, 40), (88, 58)), FEZ, 'f', False, False, 2.0)]
C('quincy-wang', 'normal', P('#463f53', '#fbc172', iris='#1a1a1a', shade='#342e3e'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=94, hairline=[(6, 60), (16, 46), (30, 40), (50, 38), (70, 40), (84, 46), (94, 60)]),
  dome('front', top=8, w=44, cy=46, sb=56) +
  [L(outline([(14, 54), (8, 72), (2, 92, 1), (16, 82), (20, 64)])), L(outline([(86, 54), (92, 72), (98, 92, 1), (84, 82), (80, 64)]))] + _fez('front') +
  thick_brows(63, BLACK, 4.6, 15, 1.6, 15) + [L(outline([(48, 102), (52, 102), (56, 116), (50, 112), (44, 116)]), FEZ, 'f')],
  dome('side', top=8, w=44, cy=46, nape=82, fr=40) + [L(outline([(52, 56), (44, 74), (40, 94, 1), (54, 82), (58, 64)]))] + _fez('side') + side_brow(63, BLACK, 4.6, 1.6),
  dome('back', top=8, w=44, cy=46, nape=82) +
  [L(outline([(14, 60), (8, 76), (2, 94, 1), (16, 86), (20, 70)])), L(outline([(86, 60), (92, 76), (98, 94, 1), (84, 86), (80, 70)]))] + _fez('back'))

# Raine Walker: capucha morada oscura que le tapa la cabeza, con una franja de zigzag naranja y amarillo en el borde de la
# frente; le asoman rizos rosados enormes en espiral a los lados y uno en la frente; ojos rojizos grandes
HOOD, ZZO, ZZY = _c('#453550'), _c('#d8701e'), _c('#e8b830')
def _hood(view):
    if view == 'front':
        zz = [(14, 56)]
        for i in range(8):
            zz += [(18 + i * 8 + 4, 48), (18 + i * 8 + 8, 56)]
        return [L(outline([(10, 66), (8, 36), (24, 10), (50, 0), (76, 10), (92, 36), (90, 66), (84, 52), (16, 52)]), HOOD),
                L(blob([(60, 6), (82, 20), (90, 46), (76, 36)], 5), _c('#342840'), 'b', False),
                L(outline([(12, 52), (30, 44), (50, 41), (70, 44), (88, 52), (88, 58), (50, 52), (12, 58)]), ZZY, 'b', False),
                L(zz + [(86, 56)], ZZO, 'f', False, False, 2.2)]
    if view == 'side':
        return [L(outline([(80, 52), (86, 36), (76, 12), (52, 0), (26, 4), (8, 22), (2, 50), (6, 80), (22, 96), (44, 92), (52, 70), (66, 56)]), HOOD),
                L(outline([(66, 54), (84, 48), (86, 54), (68, 60)]), ZZY, 'b', False)]
    return [L(outline([(8, 90), (6, 40), (24, 10), (50, 0), (76, 10), (94, 40), (92, 90), (50, 98)]), HOOD),
            L(blob([(58, 6), (80, 20), (92, 50), (88, 86), (70, 50)], 5), _c('#342840'), 'b', False)]
C('raine-walker', 'chica', P('#dc977f', '#f8e0c6', iris='#a03a14', shade='#b4705c', deep='#8a4e3e'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=False),
  [L(curls(12, 90, (13, 14), 5)), L(curls(88, 90, (13, 14), 5)),
   L(quad((6, 86), (12, 80), (16, 90)), 'deep', 'f', False, False, 1.2), L(quad((94, 86), (88, 80), (84, 90)), 'deep', 'f', False, False, 1.2)] + _hood('front') +
  [L(curls(50, 62, (6, 5), 4), 'mid', 'f')] + lashes(75),
  [L(curls(30, 92, (14, 14), 5))] + _hood('side') + lash_side(75),
  _hood('back') + [L(curls(16, 96, (11, 10), 4)), L(curls(84, 96, (11, 10), 4))])

# Raleigh Greenstreet: pelo blanco crema en pinchos altísimos de punta, piel morena y unas gafas deportivas azul celeste de
# cristal oscuro; sonrisa
SKY, LENS = _c('#3ab8d8'), _c('#183848')
def _sport(view):
    if view == 'front':
        return [L(blob([(20, 72), (36, 68), (48, 72), (46, 84), (32, 86), (20, 80)], 5), SKY, 'f'), L(blob([(80, 72), (64, 68), (52, 72), (54, 84), (68, 86), (80, 80)], 5), SKY, 'f'),
                L(blob([(24, 74), (36, 71), (45, 74), (43, 82), (32, 83), (24, 79)], 5), LENS, 'f', False),
                L(blob([(76, 74), (64, 71), (55, 74), (57, 82), (68, 83), (76, 79)], 5), LENS, 'f', False)]
    return [L(blob([(72, 70), (90, 70), (90, 84), (74, 84)], 4), SKY, 'f'), L(blob([(76, 73), (88, 73), (88, 81), (77, 81)], 4), LENS, 'f', False),
            L([(72, 74), (48, 70)], SKY, 'f', False, False, 2.4)]
C('raleigh-greenstreet', 'normal', P('#f6f0d0', '#ca966c', iris='#1a1a1a', shade='#d8d0b0'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=93, hairline=hl(5, 62, 46, 56, jit=2, seed=7)),
  dome('front', top=-14, w=44, cy=42, n=7, amp=22, seed=47, sb=58) + _sport('front'),
  dome('side', top=-14, w=44, cy=42, n=7, amp=22, seed=47, nape=80, fr=46) + _sport('side'),
  dome('back', top=-14, w=44, cy=42, n=7, amp=22, seed=47, nape=80))

# Ralph Chasing: una gorra enorme en gajos rojos y azul petróleo oscuro, con el botón dorado arriba, que le tapa la cabeza
# hasta los ojos; piel morena, un clip dorado en la oreja y boca ondulada
HR, HB, HG2 = _c('#af2d2c'), _c('#0e3442'), _c('#d8b030')
def _bigcap(view):
    if view == 'front':
        return [L(blob([(-6, 56), (-8, 26), (10, 2), (50, -10), (90, 2), (108, 26), (106, 56), (80, 74), (50, 76), (20, 74)], 6), HR),
                L(blob([(26, 2), (50, -8), (50, 74), (30, 72)], 5), HB, 'b', False), L(blob([(98, 18), (108, 30), (106, 56), (80, 72), (66, 50)], 5), HB, 'b', False),
                L(blob([(-6, 34), (8, 8), (20, 40), (6, 64)], 5), HB, 'b', False), L(ell(50, -8, 5, 3), HG2, 'f')]
    if view == 'side':
        return [L(blob([(-8, 56), (-6, 24), (14, 0), (50, -10), (88, 2), (104, 30), (100, 60), (70, 72), (30, 72)], 6), HR),
                L(blob([(30, 0), (56, -8), (66, 70), (36, 70)], 5), HB, 'b', False), L(ell(48, -8, 5, 3), HG2, 'f')]
    return [L(blob([(-6, 60), (-8, 26), (10, 2), (50, -10), (90, 2), (108, 26), (106, 60), (80, 80), (50, 82), (20, 80)], 6), HR),
            L(blob([(36, -6), (64, -6), (66, 80), (34, 80)], 5), HB, 'b', False), L(ell(50, -8, 5, 3), HG2, 'f')]
C('ralph-chasing', 'normal', P('#2a1a14', '#b37a3e', iris='#1a1a1a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _bigcap('front') + [L(ell(66, 80, 3.4, 2.2), WHITE, 'f', False), L(ell(67, 80, 1.2, 1.2), BLACK, 'f', False),
                      L(blob([(82, 76), (88, 76), (88, 86), (82, 86)], 2), HG2, 'f'),
                      L([(40, 96), (44, 93), (48, 96), (52, 93), (56, 96), (60, 93)], OUTC, 'f', False, False, 1.4)],
  _bigcap('side') + [L(ell(82, 80, 2.4, 2.2), WHITE, 'f', False), L([(80, 96), (84, 93), (88, 96)], OUTC, 'f', False, False, 1.4)],
  _bigcap('back'))

# Ram Horner: pelo verde oliva en nube encima y dos cuernos de carnero enroscados a los lados de la cara; lleva una máscara de
# madera clara con dos manchas verdes en la frente, ojos redondos de búho y una nariz larga; boca recta
HORN, HORND, MASK = _c('#967957'), _c('#6a5238'), _c('#f0c070')
def _ramhorn(x, s):
    return [L(curls(x, 88, (9, 13), 4, 0.3), HORN, 'f'), L(ell(x, 88, 4.5, 6.5), HORND, 'f', False), L(ell(x, 88, 1.8, 2.6), HORN, 'f', False)]
C('ram-aries-horner', 'normal', P('#647727', '#fcc271', iris='#4a4a20', shade='#4e5c1e'),
  F(eyes='round', brows=False, mouth='line', mouth_y=100, face_front=face(w=3, chin=110, jaw=1), face_side=face_side(chin=9, nose=3), ears=False,
    hairline=[(6, 58), (20, 48), (50, 46), (80, 48), (94, 58)], nose=None),
  [L(curls(50, 26, (52, 26), 11, 0.1)), L(blob([(58, 8), (88, 22), (98, 40), (74, 34)], 5), 'shade', 'b', False)] +
  [L(ell(38, 64, 5, 3.4), _c('#6a8a30'), 'f'), L(ell(62, 64, 5, 3.4), _c('#6a8a30'), 'f'),
   L([(50, 70), (46, 92), (54, 92), (50, 70)], MASK, 'f', False, True)] + _ramhorn(18, 1) + _ramhorn(82, -1),
  [L(curls(46, 26, (50, 26), 10, 0.1))] + _ramhorn(48, 1) + [L([(86, 72), (96, 92), (86, 94)], MASK, 'f', False, True)],
  [L(curls(50, 30, (52, 30), 11, 0.1)), L(blob([(14, 40), (50, 50), (86, 40), (84, 70), (50, 78), (16, 70)], 6))] + _ramhorn(16, 1) + _ramhorn(84, -1))

# Ray Pier: máscara de médico de la peste color crema, con los dos ojos de cristal azul oscuro y el pico largo que le baja
# hasta la barbilla; un sombrero redondo enorme azul celeste encima y el pelo azul oscuro debajo
SKY2, SKY2D, BEAKC, EYEB = _c('#76c4d5'), _c('#488da3'), _c('#ebd9bc'), _c('#1e3a5e')
def _plague(view):
    if view == 'front':
        return [L(blob([(-8, 40), (-4, 14), (20, -6), (50, -12), (80, -6), (104, 14), (108, 40), (80, 50), (50, 52), (20, 50)], 6), SKY2),
                L(blob([(54, -10), (84, -4), (106, 20), (104, 40), (80, 48), (70, 20)], 5), SKY2D, 'b', False),
                L(blob([(14, 44), (50, 34), (86, 44), (84, 56), (50, 50), (16, 56)], 5), 'mid'),
                L(blob([(24, 56), (50, 52), (76, 56), (74, 84), (58, 92), (50, 116), (42, 92), (26, 84)], 5), BEAKC, 'f'),
                L(ell(36, 72, 7, 7.5), EYEB, 'f'), L(ell(64, 72, 7, 7.5), EYEB, 'f'), L([(50, 86), (50, 112)], _c('#c8b090'), 'f', False, False, 1.0)]
    if view == 'side':
        return [L(blob([(-10, 40), (-6, 14), (20, -6), (50, -12), (80, -6), (104, 14), (106, 40), (80, 48), (50, 50), (20, 48)], 6), SKY2),
                L(blob([(30, 40), (60, 40), (64, 70), (44, 86), (26, 80)], 5), 'mid'),
                L(blob([(62, 52), (88, 54), (92, 78), (106, 104), (82, 92), (64, 84)], 5), BEAKC, 'f'), L(ell(82, 70, 4.4, 6), EYEB, 'f')]
    return [L(blob([(-8, 40), (-4, 14), (20, -6), (50, -12), (80, -6), (104, 14), (108, 40), (80, 50), (50, 52), (20, 50)], 6), SKY2),
            L(blob([(12, 44), (50, 40), (88, 44), (88, 84), (50, 90), (12, 84)], 6), 'mid'), L([(14, 66), (86, 66)], _c('#b8a888'), 'f', False, False, 2.4)]
C('ray-spade-pier', 'normal', P('#16405c', '#ebd9bc', iris='#1a1a1a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _plague('front'), _plague('side'), _plague('back'))

# Rebus Stumper: pelo castaño rojizo en casco con el flequillo recto y un mechón altísimo en antena curvado hacia un lado;
# ojos redondos, coloretes, un moco en la nariz y sonrisa
C('rebus-tricky-stumper', 'bajito', P('#8b3d2f', '#f4bf95', iris='#1a1a1a', shade='#692d23'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=95, face_front=face(w=4, chin=102, jaw=3), big_ears=2, ear_out=4,
    hairline=[(6, 62), (14, 60), (30, 61), (50, 62), (70, 61), (86, 60), (94, 62)]),
  bowl('front', top=4, side=86, w=2) + [L(quad((44, 8), (30, -30), (-2, -14)), 'mid', 'b', True, False, 3.2)] + blush(88, 24, 5) +
  [L([(52, 86), (53, 92)], _c('#a8d0d8'), 'f', False, False, 1.6)],
  bowl('side', top=4, nape=90, w=2) + [L(quad((44, 6), (36, -30), (6, -18)), 'mid', 'b', True, False, 3.2)],
  bowl('back', top=4, nape=90, w=2) + [L(quad((50, 6), (36, -30), (4, -14)), 'mid', 'b', True, False, 3.2)])

# Reese Fryer: pinchos azul marino de punta hacia arriba y hacia los lados, cejas gruesas muy fruncidas y morros de enfado
C('reese-fryer', 'normal', P('#263751', '#f9bc7c', iris='#1a1a1a', shade='#1c283c'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=95, hairline=[(6, 64), (16, 50), (30, 44), (50, 48), (70, 44), (84, 50), (94, 64)]),
  dome('front', top=-12, w=48, cy=44, n=9, amp=18, seed=49, sb=66) + thick_brows(64, 'deep', 4.6, 15, 1.8, 14),
  dome('side', top=-12, w=48, cy=44, n=9, amp=18, seed=49, nape=82, fr=50) + side_brow(64, 'deep', 4.6, 1.8),
  dome('back', top=-12, w=48, cy=44, n=9, amp=18, seed=49, nape=82))

# Regina Raffles: melena rubia de rizos con tirabuzones grandes a un lado y una boina verde oscuro ladeada; ojos azules con
# pestañas y la boca seria
BERET = _c('#1e4a1a')
C('regina-rifles-raffles', 'chica', P('#f2e274', '#fdeab7', iris='#3a8ab0', shade='#caa848', deep='#a2843e'),
  F(eyes='normal', brows=True, mouth='frown', mouth_y=94, hairline=[(6, 64), (16, 52), (30, 48), (46, 54), (60, 48), (76, 50), (88, 56), (94, 64)]),
  dome('front', top=0, w=48, cy=46, n=8, amp=5, soft=True, seed=51, long=90, flare=4) +
  [L(curls(8, 76, (10, 12), 5)), L(curls(10, 96, (9, 10), 4)), L(curls(92, 82, (8, 10), 4)),
   L(blob([(10, 18), (26, 0), (52, -4), (62, 8), (48, 20), (22, 26)], 6), BERET)] + lashes(75),
  dome('side', top=0, w=48, cy=46, n=8, amp=5, soft=True, seed=51, long=90, flare=4, fr=52) +
  [L(curls(20, 84, (12, 14), 5)), L(blob([(14, 12), (40, -4), (70, 0), (60, 16), (30, 22)], 6), BERET)] + lash_side(75),
  dome('back', top=0, w=48, cy=46, n=8, amp=5, soft=True, seed=51, long=90, flare=4) +
  [L(curls(90, 80, (10, 12), 5)), L(curls(88, 98, (9, 10), 4)), L(blob([(38, 8), (64, -2), (90, 16), (78, 26), (50, 22)], 6), BERET)])

# Reyes Cabedo: disfraz de pájaro: una capucha crema con la cresta de plumas castañas arriba y un pico enorme castaño oscuro
# que le baja por la frente hasta la nariz; ojos negros redondos enormes y sonrisa
HOODC, FEATH, BEAKD = _c('#e5d7be'), _c('#6f430b'), _c('#2c2007')
def _bird(view):
    if view == 'front':
        return [L(outline([(10, 80), (6, 40), (14, 14), (30, 0), (50, -4), (70, 0), (86, 14), (94, 40), (90, 80), (82, 60), (18, 60)]), HOODC),
                L(outline([(30, 6), (36, -8, 1), (44, 2), (50, -14, 1), (56, 2), (64, -8, 1), (70, 6), (60, 30), (40, 30)]), FEATH, 'f'),
                L(outline([(36, 50), (64, 50), (58, 64), (50, 82, 1), (42, 64)]), BEAKD, 'f')]
    if view == 'side':
        return [L(outline([(82, 54), (86, 34), (74, 10), (50, -2), (26, 2), (8, 22), (2, 54), (10, 86), (30, 96), (50, 84), (60, 62)]), HOODC),
                L(outline([(36, 2), (40, -12, 1), (52, -2), (60, -10, 1), (66, 4), (56, 24), (40, 18)]), FEATH, 'f'),
                L(outline([(76, 52), (92, 56), (104, 72, 1), (88, 70), (78, 64)]), BEAKD, 'f')]
    return [L(outline([(8, 92), (6, 40), (14, 14), (30, 0), (50, -4), (70, 0), (86, 14), (94, 40), (92, 92), (50, 98)]), HOODC),
            L(outline([(30, 6), (36, -8, 1), (44, 2), (50, -14, 1), (56, 2), (64, -8, 1), (70, 6), (66, 44), (50, 60, 1), (34, 44)]), FEATH, 'f')]
C('reyes-kingf-cabedo', 'normal', P('#6f430b', '#fac273', iris='#1a1a1a'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, hairline=False, ears=False),
  _bird('front') + [L(ell(36, 76, 6.4, 7), BLACK, 'f'), L(ell(64, 76, 6.4, 7), BLACK, 'f'),
                    L(ell(34, 73, 2, 2), WHITE, 'f', False), L(ell(62, 73, 2, 2), WHITE, 'f', False)],
  _bird('side') + [L(ell(80, 76, 4, 6), BLACK, 'f'), L(ell(81, 73, 1.4, 1.4), WHITE, 'f', False)],
  _bird('back'))

# Ria Carnival (portera): melena granate oscuro enorme y alborotada, con un tocado de carnaval dorado y naranja encima; piel
# morena, ojos rojos con pestañas, pendientes dorados grandes y sonrisa de dientes
CROWN, CROWNY = _c('#e48516'), _c('#f2c230')
def _crown(view):
    if view == 'front':
        return [L(outline([(24, 46), (20, 24), (32, 16), (40, 0), (50, -14, 1), (60, 0), (68, 16), (80, 24), (76, 46), (50, 40)]), CROWN, 'f'),
                L(outline([(42, 4), (50, -8), (58, 4), (56, 36), (44, 36)]), CROWNY, 'f', False), L(ell(50, 12, 3, 3), CROWN, 'f', False),
                L(ell(50, 26, 3, 3), CROWN, 'f', False)]
    if view == 'side':
        return [L(outline([(60, 44), (56, 20), (66, 6), (76, -8, 1), (84, 8), (90, 22), (88, 44), (74, 40)]), CROWN, 'f'),
                L(outline([(72, 6), (78, -2), (84, 12), (82, 36), (72, 34)]), CROWNY, 'f', False)]
    return [L(blob([(28, 14), (50, 6), (72, 14), (70, 20), (50, 14), (30, 20)], 4), CROWN, 'f')]
C('ria-samba-carnival', 'chica', P('#7b0f0c', '#e2b060', iris='#b0201e', shade='#5a0c0a'),
  F(eyes='normal', brows=False, mouth='none', hairline=[(6, 64), (18, 50), (34, 46), (50, 48), (66, 46), (82, 50), (94, 64)]),
  dome('front', top=-6, w=54, cy=46, n=11, amp=10, seed=53, long=92, flare=10, ends=3) + _crown('front') +
  [L(ell(16, 88, 3.6, 3.6), CROWNY, 'f'), L(ell(84, 88, 3.6, 3.6), CROWNY, 'f')] + tooth_mouth(94, 7, 4) + lashes(75),
  dome('side', top=-6, w=54, cy=46, n=11, amp=10, seed=53, long=92, flare=10, fr=50) + _crown('side') + [L(ell(46, 86, 3.4, 3.4), CROWNY, 'f')] + lash_side(75),
  dome('back', top=-6, w=54, cy=46, n=11, amp=10, seed=53, long=92, flare=10, ends=5) + _crown('back'))

# Ria Vivalist: pelo gris pizarra con dos moños en cuerno de buey a los lados de la cabeza, atados con cintas verde claro, y
# dos mechones que le caen hasta la mandíbula; ojos negros afilados con pestañas y cejas finas
RIB = _c('#b8d8a0')
def _horns(view):
    if view == 'front':
        return [L(outline([(16, 30), (0, 14), (-4, 0, 1), (10, 6), (26, 18)])), L(outline([(84, 30), (100, 14), (104, 0, 1), (90, 6), (74, 18)])),
                L(blob([(10, 14), (18, 10), (24, 24), (16, 28)], 3), RIB, 'f'), L(blob([(90, 14), (82, 10), (76, 24), (84, 28)], 3), RIB, 'f')]
    if view == 'side':
        return [L(outline([(46, 26), (34, 8), (32, -6, 1), (48, 2), (60, 18)])), L(blob([(40, 8), (50, 6), (54, 18), (44, 20)], 3), RIB, 'f')]
    return [L(outline([(16, 30), (0, 14), (-4, 0, 1), (10, 6), (26, 18)])), L(outline([(84, 30), (100, 14), (104, 0, 1), (90, 6), (74, 18)])),
            L(blob([(10, 14), (18, 10), (24, 24), (16, 28)], 3), RIB, 'f'), L(blob([(90, 14), (82, 10), (76, 24), (84, 28)], 3), RIB, 'f')]
C('ria-vivalist', 'chica', P('#555161', '#fcd18a', iris='#1a1a1a', shade='#443f4e'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=93, hairline=[(6, 60), (18, 44), (34, 38), (50, 42), (66, 38), (82, 44), (94, 60)]),
  _horns('front') + dome('front', top=4, w=46, cy=46, sb=60) +
  [L(outline([(14, 54), (8, 76), (14, 96, 1), (22, 78), (22, 60)])), L(outline([(86, 54), (92, 76), (86, 96, 1), (78, 78), (78, 60)]))] + lashes(75),
  _horns('side') + dome('side', top=4, w=46, cy=46, nape=80, fr=42) + [L(outline([(54, 54), (48, 74), (54, 94, 1), (60, 76), (62, 60)]))] + lash_side(75),
  _horns('back') + dome('back', top=4, w=46, cy=46, nape=84) +
  [L(outline([(14, 60), (8, 80), (14, 96, 1), (22, 82), (22, 66)])), L(outline([(86, 60), (92, 80), (86, 96, 1), (78, 82), (78, 66)]))])

# Rich Fowler (portero): pelo gris plata con una cresta en el centro que sube como un cuerno y dos mechones en cuerno que se
# enroscan hacia fuera a los lados, todos con una franja roja y el pelo negro por debajo; piel muy pálida, ojos grises
# entornados y sonrisa ancha con un colmillo
SIL, REDS, BLKH = _c('#b8c4c4'), _c('#c81e24'), _c('#2a2626')
def _fowler(view):
    if view == 'front':
        return [L(outline([(16, 62), (12, 34), (28, 12), (50, 4), (72, 12), (88, 34), (84, 62), (50, 50)]), BLKH),
                L(outline([(20, 46), (8, 34), (6, 20, 1), (22, 22), (30, 36)]), SIL, 'f'), L(outline([(80, 46), (92, 34), (94, 20, 1), (78, 22), (70, 36)]), SIL, 'f'),
                L([(10, 26), (22, 40)], REDS, 'f', False, False, 2.0), L([(90, 26), (78, 40)], REDS, 'f', False, False, 2.0),
                L(outline([(42, 60), (40, 30), (46, 6), (54, -8, 1), (60, 10), (56, 36), (48, 70, 1)]), SIL, 'f'),
                L(quad((54, -4), (52, 30), (46, 66)), REDS, 'f', False, False, 2.4)]
    if view == 'side':
        return [L(outline([(80, 52), (86, 32), (74, 10), (50, 2), (26, 6), (8, 22), (2, 50), (8, 74), (24, 84), (42, 80), (52, 62)]), BLKH),
                L(outline([(60, 40), (60, 14), (68, -6, 1), (78, 10), (76, 34)]), SIL, 'f'), L(quad((68, -2), (70, 18), (68, 38)), REDS, 'f', False, False, 2.2),
                L(outline([(44, 44), (32, 32), (28, 18, 1), (46, 22), (52, 36)]), SIL, 'f'), L([(34, 24), (46, 38)], REDS, 'f', False, False, 2.0)]
    return [L(outline([(14, 80), (10, 36), (26, 12), (50, 4), (74, 12), (90, 36), (86, 80), (50, 86)]), BLKH),
            L(outline([(20, 46), (8, 34), (6, 20, 1), (22, 22), (30, 36)]), SIL, 'f'), L(outline([(80, 46), (92, 34), (94, 20, 1), (78, 22), (70, 36)]), SIL, 'f'),
            L(outline([(42, 40), (40, 20), (46, 4), (54, -8, 1), (60, 10), (58, 40)]), SIL, 'f'), L(quad((54, -4), (52, 20), (50, 40)), REDS, 'f', False, False, 2.4)]
C('rich-red-card-fowler', 'normal', P('#2a2626', '#fdefd3', iris='#4a4a50'),
  F(eyes='sharp', brows=False, mouth='none', hairline=[(6, 58), (18, 46), (34, 42), (50, 46), (66, 42), (82, 46), (94, 58)]),
  _fowler('front') + [L(quad((36, 92), (50, 100), (66, 90)), OUTC, 'f', False, False, 1.8),
                      L([(58, 95), (60, 100), (62, 94)], WHITE, 'f', False, True)],
  _fowler('side') + [L(quad((78, 92), (84, 96), (88, 90)), OUTC, 'f', False, False, 1.8)],
  _fowler('back'))

# Rick Shaw: pelo plateado lavanda largo, echado todo hacia un lado en un mechón que le tapa medio ojo y que acaba en un rizo
# colgando; el otro lado, rapado en gris; ojos amarillos afilados y la boca apretada
C('rick-rickshaw-shaw', 'delgado', P('#c8d2d9', '#fdf1d6', iris='#c8b020', shade='#93878d', deep='#786e71'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, face_front=face(w=-1, chin=104), face_side=face_side(chin=4),
    hairline=[(6, 60), (20, 46), (40, 44), (56, 50), (70, 44), (82, 48), (94, 60)]),
  [L(outline([(70, 60), (66, 30), (74, 14), (84, 30), (86, 60)]), 'shade'),
   L(outline([(70, 52), (74, 20), (60, 4), (34, 2), (12, 10), (-6, 18, 1), (8, 22), (18, 40), (24, 64), (32, 92), (28, 104), (18, 108), (12, 100), (18, 96),
              (22, 104), (26, 96), (20, 80), (14, 62), (26, 50), (40, 56), (50, 52)]))],
  [L(outline([(80, 52), (88, 34), (78, 12), (52, 2), (26, 6), (10, 20), (6, 48), (10, 70), (24, 80), (40, 76), (54, 62), (66, 56)]), 'shade'),
   L(outline([(80, 44), (84, 26), (70, 8), (46, 2), (40, 14), (56, 22), (70, 36)]))],
  [L(outline([(14, 78), (10, 38), (24, 12), (50, 4), (76, 12), (90, 38), (86, 78), (50, 84)]), 'shade'),
   L(outline([(30, 6), (60, 2), (80, 10), (90, 30), (92, 50), (84, 70), (88, 96), (80, 106), (74, 96), (80, 92), (82, 98), (84, 88), (74, 66), (66, 40), (50, 20)]))])

# Riku Matsushita: gorro de pescador de estampado de leopardo y melena castaña oscura lisa y larga hasta el pecho; ojos
# oscuros y sonrisa suave
LEO, LEOS = _c('#d8b878'), _c('#5a3a1e')
def _bucket(view):
    out = []
    if view == 'front':
        out = [L(blob([(-6, 46), (6, 28), (22, 4), (50, -4), (78, 4), (94, 28), (106, 46), (92, 52), (50, 46), (8, 52)], 6), LEO)]
        spots = [(20, 24), (36, 12), (54, 8), (70, 14), (84, 30), (28, 40), (64, 34), (46, 28), (6, 42), (94, 44)]
    elif view == 'side':
        out = [L(blob([(-8, 46), (4, 24), (24, 2), (54, -4), (80, 6), (92, 28), (108, 48), (80, 50), (40, 50)], 6), LEO)]
        spots = [(18, 22), (36, 10), (58, 8), (76, 22), (30, 38), (60, 34), (92, 44)]
    else:
        out = [L(blob([(-6, 46), (6, 28), (22, 4), (50, -4), (78, 4), (94, 28), (106, 46), (92, 52), (50, 50), (8, 52)], 6), LEO)]
        spots = [(20, 24), (36, 12), (54, 8), (70, 14), (84, 30), (28, 40), (64, 34), (46, 28)]
    return out + [L(ell(x, y, 3.4, 2.6), LEOS, 'f', False) for x, y in spots]
C('riku-pants-matsushita', 'chica', P('#5a473a', '#edd0b1', iris='#2a1a14', shade='#4c392c'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=93, hairline=[(6, 60), (18, 52), (34, 56), (50, 60), (66, 56), (82, 52), (94, 60)]),
  dome('front', top=6, w=48, cy=48, long=122, flare=4, ends=3) +
  [L(outline([(30, 46), (56, 46), (48, 62), (36, 70, 1)]), 'mid', 'f')] + _bucket('front') + lashes(75),
  dome('side', top=6, w=48, cy=48, long=122, flare=4, fr=58) + _bucket('side') + lash_side(75),
  dome('back', top=6, w=48, cy=48, long=122, flare=4, ends=5) + _bucket('back'))

# Riku Ryu: pelo castaño medio en capas cortas, con mechones por la frente y las orejas tapadas; ojos castaños y sonrisa
C('riku-ryu', 'normal', P('#7e665c', '#fad5bc', iris='#4a2a20', shade='#695149', deep='#563e39'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=93, hairline=hl(6, 66, 50, 60, lean=-1, jit=2, seed=11)),
  dome('front', top=4, w=47, cy=46, n=10, amp=4, soft=True, seed=55, sb=80),
  dome('side', top=4, w=47, cy=46, n=10, amp=4, soft=True, seed=55, nape=90, fr=56),
  dome('back', top=4, w=47, cy=46, n=10, amp=4, soft=True, seed=55, nape=90))

# Rio Shoring: pelo negro peinado hacia arriba en un moño de lazo alto, con mechas verde lima; los lados rapados con rayas;
# piel clara, ojos rasgados de pillo, aros plateados en las orejas y sonrisa ladina
LIM2, SILV = _c('#83ca2e'), _c('#c8ccd0')
C('rio-g-peas-shoring', 'normal', P('#2a2a26', '#e1d0b4', iris='#1a1a1a'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=94, hairline=[(14, 60), (20, 40), (34, 30), (50, 40), (66, 30), (80, 40), (86, 60)]),
  [L(outline([(16, 62), (14, 36), (30, 16), (50, 8), (70, 16), (86, 36), (84, 62), (78, 50), (50, 40), (22, 50)])),
   L(outline([(40, 12), (36, -6), (44, -20), (58, -20), (64, -6), (60, 12)])), L(ell(50, -10, 5, 5), 'skin', 'f', False),
   L(quad((38, 0), (50, -22), (62, 0)), LIM2, 'f', False, False, 3.0), L([(28, 30), (44, 22)], LIM2, 'f', False, False, 2.4), L([(72, 30), (56, 22)], LIM2, 'f', False, False, 2.4),
   L([(18, 50), (22, 42)], _c('#6a6a60'), 'f', False, False, 1.0), L([(82, 50), (78, 42)], _c('#6a6a60'), 'f', False, False, 1.0),
   L(ell(14, 82, 2.6, 2.6) + [ell(14, 82, 2.6, 2.6)[0]], SILV, 'f', False, False, 1.4), L(ell(86, 82, 2.6, 2.6) + [ell(86, 82, 2.6, 2.6)[0]], SILV, 'f', False, False, 1.4)],
  [L(outline([(80, 50), (84, 30), (72, 12), (50, 6), (28, 10), (12, 26), (8, 48), (16, 60), (32, 56), (52, 50)])),
   L(outline([(40, 10), (34, -6), (42, -20), (56, -20), (62, -6), (58, 10)])), L(ell(48, -10, 5, 5), 'skin', 'f', False),
   L(quad((40, 2), (48, -22), (60, 0)), LIM2, 'f', False, False, 3.0), L(ell(46, 82, 2.6, 2.6) + [ell(46, 82, 2.6, 2.6)[0]], SILV, 'f', False, False, 1.4)],
  [L(outline([(14, 70), (12, 36), (28, 14), (50, 6), (72, 14), (88, 36), (86, 70), (50, 76)])),
   L(outline([(40, 12), (36, -6), (44, -20), (58, -20), (64, -6), (60, 12)])), L(ell(50, -10, 5, 5), 'skin', 'f', False),
   L([(50, -14), (50, 60)], LIM2, 'f', False, False, 3.0)])

# Risako Sugaya: melena castaña larga y lisa hasta el pecho con el flequillo recto; ojos castaños grandes y sonrisa
C('risako-rishako-sugaya', 'chica', P('#604635', '#f9d4b9', iris='#3a2014', shade='#4c3428', deep='#3a2418'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=[(6, 64), (14, 62), (30, 63), (50, 64), (70, 63), (86, 62), (94, 64)]),
  bowl('front', top=2, side=124, w=6) + lashes(76),
  bowl('side', top=2, nape=124, w=6) + lash_side(76),
  bowl('back', top=2, nape=124, w=6))

# Rocco Shale: pelo verde oscuro con la raya en medio que le cae a los dos lados tapando las orejas; ojos grandes afilados y
# boca seria
C('rocco-shale', 'normal', P('#134d3a', '#fcc272', iris='#1a1a1a', shade='#0e3a2c'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 66), (16, 60), (30, 54), (44, 50), (50, 54), (56, 50), (70, 54), (84, 60), (94, 66)]),
  bowl('front', top=0, side=76, w=4) + [L(quad((50, 4), (52, 26), (50, 50)), 'shade', 'f', False, False, 1.4)],
  bowl('side', top=0, nape=88, w=4),
  bowl('back', top=0, nape=88, w=4) + [L([(50, 4), (50, 60)], 'shade', 'f', False, False, 1.4)])

# Roland Allardyce: pinchos negros de punta y una cinta crema en la frente; piel morena, ojos grandes con el ceño fruncido y
# arañazos rojos en una mejilla
CREAM, SCR = _c('#e6e6d7'), _c('#b83a2a')
C('roland-dicey-allardyce', 'normal', P('#2d2e32', '#dda358', iris='#1a1a1a'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 60), (16, 54), (50, 52), (84, 54), (94, 60)]),
  dome('front', top=-10, w=46, cy=44, n=9, amp=16, seed=57, sb=60) + [band('front', 46, 7, CREAM),
   L([(24, 84), (32, 80)], SCR, 'f', False, False, 1.6), L([(24, 89), (33, 85)], SCR, 'f', False, False, 1.6), L([(26, 94), (34, 90)], SCR, 'f', False, False, 1.6)],
  dome('side', top=-10, w=46, cy=44, n=9, amp=16, seed=57, nape=80, fr=46) + [band('side', 44, 7, CREAM)],
  dome('back', top=-10, w=46, cy=44, n=9, amp=16, seed=57, nape=80) + [band('back', 48, 7, CREAM)])

# Roland Lex: pelo crema casi blanco de mechones largos en punta echados a un lado, que le tapan un ojo; piel morena, el ojo
# que se ve afilado y sonrisa
C('roland-lex', 'normal', P('#e6e9c8', '#bb9275', iris='#3a3a40', shade='#c4bca2', deep='#98806e'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=94, hairline=[(6, 66), (20, 52), (40, 50), (56, 54), (72, 52), (88, 58), (94, 66)]),
  dome('front', top=-4, w=48, cy=44, n=7, amp=12, sweep=-0.9, seed=59, sb=72) +
  [L(outline([(-8, 22, 1), (20, 30), (58, 40), (56, 60), (46, 82, 1), (40, 66), (28, 82, 1), (24, 62), (-4, 66, 1), (12, 50)]), 'mid', 'f'),
   L(outline([(30, 44), (52, 46), (48, 66), (40, 78, 1), (38, 58)]), 'shade', 'f', False)],
  dome('side', top=-4, w=48, cy=44, n=7, amp=12, sweep=-0.9, seed=59, nape=84, fr=52),
  dome('back', top=-4, w=48, cy=44, n=7, amp=12, sweep=-0.9, seed=59, nape=84) + [L(outline([(108, 22, 1), (80, 30), (70, 50), (96, 50)]))])

# Roman Fawkes (portero): pelo castaño en rizos abultados como una nube, cara larga morena, cejas gruesas, ojos redondos con
# ojeras oscuras y un morro redondo marrón con la boca
BAG, SNOUT = _c('#a87838'), _c('#8a5028')
C('roman-fawkes', 'normal', P('#623218', '#dca359', iris='#1a1a1a', shade='#44261c'),
  F(eyes='round', brows=False, mouth='none', face_front=face(w=-2, chin=110, jaw=-1), face_side=face_side(chin=9, nose=4), eye_y=74,
    hairline=[(6, 60), (18, 50), (30, 54), (40, 46), (52, 54), (62, 46), (74, 52), (86, 50), (94, 60)]),
  [L(curls(50, 30, (52, 28), 12, 0.2)), L(curls(14, 54, (10, 12), 4)), L(curls(86, 54, (10, 12), 4)),
   L(blob([(64, 6), (90, 18), (100, 40), (80, 36)], 5), 'shade', 'b', False)] + thick_brows(62, 'shade', 4.0, 14, 0, 13) +
  [L(blob([(28, 80), (44, 80), (42, 86), (30, 86)], 4), BAG, 'f', False), L(blob([(72, 80), (56, 80), (58, 86), (70, 86)], 4), BAG, 'f', False),
   L(ell(50, 98, 8, 6.5), SNOUT, 'f'), L(quad((44, 98), (50, 96), (56, 99)), OUTC, 'f', False, False, 1.2)],
  [L(curls(44, 32, (48, 28), 11, 0.2)), L(curls(24, 64, (14, 14), 5))] + side_brow(62, 'shade', 4.0) + [L(ell(88, 96, 5, 6), SNOUT, 'f')],
  [L(curls(50, 34, (52, 32), 12, 0.2)), L(curls(20, 66, (12, 14), 5)), L(curls(80, 66, (12, 14), 5)), L(curls(50, 72, (24, 12), 6))])

# Roo Hopper: disfraz de canguro: capucha naranja que le rodea la cara con un canguro pequeño encima de la cabeza, un poco de
# flequillo castaño, ojos negros enormes y la boca y la nariz tapadas por la tela naranja
KNG, KNGD, CRM = _c('#fb9007'), _c('#c66610'), _c('#f2eed0')
def _roo(view):
    if view == 'front':
        return [L(outline([(8, 84), (4, 50), (14, 22), (34, 8), (66, 8), (86, 22), (96, 50), (92, 84), (80, 64), (20, 64)]), KNG),
                L(outline([(34, 10), (36, -4), (30, -22, 1), (42, -12), (50, -10), (58, -12), (70, -22, 1), (64, -4), (66, 10), (50, 18)]), KNG),
                L(ell(44, -2, 1.6, 1.6), BLACK, 'f', False), L(ell(56, -2, 1.6, 1.6), BLACK, 'f', False), L(ell(50, 6, 4, 3), CRM, 'f', False),
                L(blob([(30, 48), (50, 40), (70, 48), (64, 60), (50, 56), (36, 60)], 5), 'mid', 'f'),
                L(blob([(14, 82), (30, 84), (50, 86), (70, 84), (86, 82), (84, 104), (50, 112), (16, 104)], 5), KNG, 'f'),
                L([(46, 90), (50, 96), (54, 90)], KNGD, 'f', False, False, 1.2)]
    if view == 'side':
        return [L(outline([(80, 56), (84, 34), (72, 12), (50, 4), (26, 8), (8, 26), (2, 60), (8, 92), (26, 104), (60, 110), (90, 104), (92, 86), (70, 84), (62, 64)]), KNG),
                L(outline([(36, 8), (34, -6), (28, -22, 1), (44, -12), (56, -10), (62, 6)]), KNG)]
    return [L(outline([(6, 96), (4, 50), (14, 22), (34, 8), (66, 8), (86, 22), (96, 50), (94, 96), (50, 104)]), KNG),
            L(outline([(34, 10), (36, -4), (30, -22, 1), (42, -12), (50, -10), (58, -12), (70, -22, 1), (64, -4), (66, 10), (50, 18)]), KNG),
            L(blob([(44, 80), (56, 80), (60, 108), (50, 116), (40, 108)], 5), KNGD, 'f')]
C('roo-hopper', 'chica', P('#8d4f09', '#f2eed0', iris='#1a1a1a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _roo('front') + [L(ell(36, 74, 6, 6.6), BLACK, 'f'), L(ell(64, 74, 6, 6.6), BLACK, 'f'), L(ell(34, 71, 2, 2), WHITE, 'f', False), L(ell(62, 71, 2, 2), WHITE, 'f', False)],
  _roo('side') + [L(ell(82, 74, 4, 6), BLACK, 'f'), L(ell(83, 71, 1.4, 1.4), WHITE, 'f', False)],
  _roo('back'))

# Roy Ellway: pinchos naranja tostado alborotados y una gorra granate puesta del revés; ojos afilados de enfado y morro
CAPR, CAPY = _c('#7a2414'), _c('#e0b040')
C('roy-ellway', 'normal', P('#9d4206', '#f9bc7b', iris='#1a1a1a', shade='#7a3206'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=hl(6, 64, 48, 60, lean=1, jit=3, seed=13)),
  [L(blob([(6, 30), (20, 8), (50, 0), (80, 8), (94, 30), (90, 40), (10, 40)], 5), CAPR), L(blob([(70, 6), (92, 12), (98, 24), (88, 28)], 4), CAPY, 'b')] +
  dome('front', top=-4, w=48, cy=44, n=9, amp=14, seed=61, sb=72) +
  [L(blob([(0, 30), (6, 8), (24, -6), (42, -4), (32, 10), (14, 26)], 5), CAPR, 'f'), L(blob([(28, -6), (44, -10), (50, -2), (36, 4)], 3), CAPY, 'f')],
  dome('side', top=-4, w=48, cy=44, n=9, amp=14, seed=61, nape=84, fr=52) +
  [L(blob([(8, 26), (24, 4), (52, -2), (80, 6), (82, 18), (50, 16), (20, 30)], 5), CAPR, 'f'), L(blob([(2, 26), (14, 20), (16, 34), (0, 36)], 3), CAPY, 'f')],
  dome('back', top=-4, w=48, cy=44, n=9, amp=14, seed=61, nape=84) +
  [L(blob([(10, 30), (24, 6), (50, -2), (76, 6), (90, 30), (50, 26)], 5), CAPR, 'f'), L(blob([(30, 24), (50, 20), (70, 24), (66, 40), (50, 44), (34, 40)], 4), CAPY, 'f'),
   L(blob([(42, 26), (58, 26), (56, 34), (44, 34)], 3), 'mid', 'f', False)])

# Rune Sigilsson: capucha gris con costuras que le tapa la cabeza y un pañuelo gris enrollado al cuello; dentro, una máscara
# verde oscuro con los ojos rojos y la boca anaranjada
HDG, HDGD, MSK = _c('#7f8e96'), _c('#605a5e'), _c('#2e4040')
def _rune(view):
    if view == 'front':
        return [L(outline([(6, 96), (4, 50), (14, 18), (34, 0), (50, -8, 1), (66, 0), (86, 18), (96, 50), (94, 96), (78, 70), (22, 70)]), HDG),
                L([(30, 8), (26, 34)], HDGD, 'f', False, False, 1.2), L([(24, 14), (32, 16)], HDGD, 'f', False, False, 1.0), L([(22, 24), (30, 26)], HDGD, 'f', False, False, 1.0),
                L(blob([(20, 54), (50, 46), (80, 54), (80, 92), (50, 104), (20, 92)], 6), MSK, 'f'),
                L(ell(38, 74, 4.6, 3.2), WHITE, 'f', False), L(ell(62, 74, 4.6, 3.2), WHITE, 'f', False),
                L(ell(38, 74, 2.4, 2.4), _c('#c02a2a'), 'f', False), L(ell(62, 74, 2.4, 2.4), _c('#c02a2a'), 'f', False),
                L([(26, 66), (44, 70)], BLACK, 'f', False, False, 2.4), L([(74, 66), (56, 70)], BLACK, 'f', False, False, 2.4),
                L(blob([(38, 88), (50, 84), (62, 88), (60, 98), (40, 98)], 4), _c('#d89048'), 'f', False),
                L(blob([(6, 96), (30, 104), (50, 108), (70, 104), (94, 96), (98, 118), (50, 124), (2, 118)], 6), HDGD, 'f')]
    if view == 'side':
        return [L(outline([(84, 52), (88, 30), (74, 6), (48, -6, 1), (24, 4), (6, 26), (0, 64), (6, 100), (30, 110), (70, 108), (92, 100), (90, 80), (66, 66)]), HDG),
                L(blob([(70, 54), (92, 56), (92, 96), (72, 100)], 5), MSK, 'f'), L(ell(84, 74, 2.8, 3), _c('#c02a2a'), 'f', False),
                L(blob([(10, 98), (60, 104), (94, 98), (94, 116), (50, 122), (8, 116)], 6), HDGD, 'f')]
    return [L(outline([(4, 104), (4, 50), (14, 18), (34, 0), (50, -8, 1), (66, 0), (86, 18), (96, 50), (96, 104), (50, 112)]), HDG),
            L([(50, -6), (50, 90)], HDGD, 'f', False, False, 1.2), L(blob([(4, 100), (50, 108), (96, 100), (98, 120), (50, 126), (2, 120)], 6), HDGD, 'f')]
C('rune-sigilsson', 'normal', P('#3c4748', '#3c4748', iris='#c02a2a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _rune('front'), _rune('side'), _rune('back'))

# S'phis Cheops: calvo, piel morena, cara enorme trapezoidal de mandíbula ancha; una cicatriz en la frente, aros dorados en
# las orejas, ojos pequeños de enfado y una mueca de boca hacia abajo
GLD = _c('#e0a830')
C('s-phis-khufu-cheops', 'corpulento', P('#8a4a28', '#b77339', iris='#1a1a1a'),
  F(eyes='sharp', brows='angry', mouth='none', face_front=face(w=8, chin=112, jaw=14, top=22), face_side=face_side(chin=10, jaw=12), hairline=False, ear_out=6),
  skull('front') + [L([(40, 36), (34, 66)], _c('#8a4a28'), 'f', False, False, 1.4), L(quad((34, 104), (50, 92), (66, 104)), OUTC, 'f', False, False, 2.0),
                    L(ell(10, 84, 3.4, 3.4) + [ell(10, 84, 3.4, 3.4)[0]], GLD, 'f', False, False, 1.8),
                    L(ell(90, 84, 3.4, 3.4) + [ell(90, 84, 3.4, 3.4)[0]], GLD, 'f', False, False, 1.8),
                    L(quad((46, 78), (44, 88), (54, 88)), _c('#8a4a28'), 'f', False, False, 1.2)],
  skull('side') + [L(ell(46, 84, 3.4, 3.4) + [ell(46, 84, 3.4, 3.4)[0]], GLD, 'f', False, False, 1.8)],
  skull('back'))

# Sahara Kalahari (portera): un turbante crema enrollado con cuerdas que le tapa la cabeza y un ojo; le caen mechones
# largos verde grisáceo oscuro hasta el pecho; el ojo que se ve, serio
TUR, TURD, ROPE = _c('#d5caa8'), _c('#b4a888'), _c('#e8dcc0')
def _turban(view):
    if view == 'front':
        return [L(outline([(10, 74), (8, 40), (20, 14), (44, 2), (64, 2), (84, 16), (92, 44), (88, 62), (70, 56), (50, 60), (40, 84), (28, 82), (14, 86)]), TUR),
                L(blob([(62, 6), (84, 18), (92, 44), (76, 40)], 5), TURD, 'b', False),
                L(quad((10, 40), (50, 18), (90, 34)), ROPE, 'f', False, False, 1.6), L(quad((10, 56), (50, 30), (90, 48)), ROPE, 'f', False, False, 1.6),
                L(quad((14, 30), (50, 46), (88, 22)), ROPE, 'f', False, False, 1.6),
                L(blob([(2, 84), (20, 78), (24, 90), (6, 96)], 4), TUR, 'f'), L(blob([(98, 84), (80, 78), (76, 90), (94, 96)], 4), TUR, 'f')]
    if view == 'side':
        return [L(outline([(84, 54), (88, 30), (74, 8), (50, 0), (26, 4), (8, 22), (4, 54), (12, 80), (30, 86), (48, 76), (62, 58)]), TUR),
                L(quad((8, 40), (48, 18), (86, 36)), ROPE, 'f', False, False, 1.6), L(quad((10, 58), (50, 34), (84, 50)), ROPE, 'f', False, False, 1.6)]
    return [L(outline([(8, 80), (8, 40), (20, 14), (44, 2), (64, 2), (84, 16), (92, 40), (92, 80), (50, 86)]), TUR),
            L(quad((8, 44), (50, 22), (92, 40)), ROPE, 'f', False, False, 1.6), L(quad((8, 60), (50, 36), (92, 56)), ROPE, 'f', False, False, 1.6),
            L(blob([(-2, 84), (20, 78), (24, 92), (0, 96)], 4), TUR, 'f'), L(blob([(102, 84), (80, 78), (76, 92), (100, 96)], 4), TUR, 'f')]
C('sahara-kalahari', 'chica', P('#4a4a40', '#fabb7b', iris='#2a2020'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=94, hairline=False),
  [L(outline([(18, 70), (12, 96), (16, 122, 1), (24, 98), (26, 74)])), L(outline([(82, 70), (88, 96), (84, 122, 1), (76, 98), (74, 74)]))] + _turban('front') +
  [L(outline([(60, 58), (66, 72), (62, 92, 1), (56, 72)]), 'mid', 'f')] + lashes(75)[1:],
  [L(outline([(50, 70), (44, 96), (50, 120, 1), (58, 98), (60, 74)]))] + _turban('side') + lash_side(75),
  [L(outline([(16, 70), (10, 100), (16, 122, 1), (30, 104), (40, 120, 1), (50, 104), (60, 120, 1), (70, 104), (84, 122, 1), (90, 100), (84, 70)]))] + _turban('back'))

# Saki Shimizu (portera): melena castaño rojizo en media melena con flequillo; ojos castaños y una sonrisa grande
C('saki-cap-n-shimizu', 'chica', P('#6e3128', '#f8dfb0', iris='#3a1a14', shade='#54201a'),
  F(eyes='normal', brows=False, mouth='grin', mouth_y=94, hairline=hl(6, 66, 54, 62, jit=2, seed=17)),
  dome('front', top=2, w=48, cy=46, n=8, amp=5, soft=True, seed=63, long=96, flare=2, ends=3) + lashes(76),
  dome('side', top=2, w=48, cy=46, n=8, amp=5, soft=True, seed=63, long=96, flare=2, fr=60) + lash_side(76),
  dome('back', top=2, w=48, cy=46, n=8, amp=5, soft=True, seed=63, long=96, flare=2, ends=4))

# Scorpia Venin (portera): pelo ciruela oscuro recogido en un moño alto, con mechas magenta delante de las orejas y una coleta
# gruesa magenta que le cae sobre un hombro; ojos castaños con un perfilado de filigrana y la boca seria
MAG = _c('#9a5161')
C('scorpia-venin', 'chica', P('#4a3139', '#fccfa0', iris='#6a4a2a', shade='#3c252b'),
  F(eyes='normal', brows=True, mouth='frown', mouth_y=94, hairline=[(6, 60), (18, 48), (34, 42), (50, 44), (66, 42), (82, 48), (94, 60)]),
  dome('front', top=6, w=46, cy=46, sb=64) + [L(curls(50, 8, (18, 14), 6)),
   L(outline([(14, 50), (24, 46), (26, 64), (20, 74, 1), (16, 62)]), MAG, 'f'), L(outline([(86, 50), (76, 46), (74, 64), (80, 74, 1), (84, 62)]), MAG, 'f'),
   L(outline([(16, 70), (8, 96), (14, 116), (28, 122, 1), (26, 104), (22, 86)]), MAG, 'f')] + lashes(75) +
  [L(quad((24, 70), (20, 64), (26, 62)), OUTC, 'f', False, False, 1.0), L(quad((76, 70), (80, 64), (74, 62)), OUTC, 'f', False, False, 1.0)],
  dome('side', top=6, w=46, cy=46, nape=82, fr=44) + [L(curls(44, 6, (16, 14), 6)), L(outline([(36, 76), (30, 100), (36, 118, 1), (44, 98), (46, 78)]), MAG)] + lash_side(75),
  dome('back', top=6, w=46, cy=46, nape=82) + [L(curls(50, 8, (18, 14), 6)), L(outline([(20, 72), (12, 98), (18, 118), (30, 122, 1), (30, 102), (30, 80)]), MAG, 'f')])

# Scott Amundsen: pelo rojo oscuro en mechones de punta que se abren como llamas, con dos largos a los lados; una cicatriz
# oscura en la mejilla, ojos afilados y la boca apretada
C('scott-amundsen', 'normal', P('#840205', '#f9bc7d', iris='#1a1a1a', shade='#690909'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=hl(5, 66, 48, 60, jit=3, seed=19)),
  dome('front', top=-12, w=50, cy=44, n=8, amp=18, sweep=0.2, seed=65, long=90, flare=10, ends=2) + [L([(68, 72), (62, 92)], _c('#8a3a2a'), 'f', False, False, 2.4)],
  dome('side', top=-12, w=50, cy=44, n=8, amp=18, sweep=0.2, seed=65, long=90, flare=10, fr=52),
  dome('back', top=-12, w=50, cy=44, n=8, amp=18, sweep=0.2, seed=65, long=90, flare=10, ends=4))

# Seamus Rock: disfraz de criatura con orejas redondas verde claro y un mechón verde oscuro encima; una máscara crema que le
# tapa la cara con dos ojos verdes y una mascarilla verde oscuro en la boca; asoma flequillo rubio
EAR, EARD, MSKC = _c('#b0e167'), _c('#2c6603'), _c('#e7dabf')
def _seamus(view):
    if view == 'front':
        return [L(ell(4, 46, 16, 18), EAR), L(ell(96, 46, 16, 18), EAR), L(outline([(40, 10), (38, -10), (50, -20, 1), (62, -10), (60, 10)]), EARD),
                L(blob([(16, 50), (20, 22), (50, 8), (80, 22), (84, 50), (50, 40)], 6), _c('#fcf69f')),
                L(blob([(20, 44), (50, 34), (80, 44), (80, 82), (50, 90), (20, 82)], 6), MSKC, 'f'),
                L(ell(38, 64, 6, 7), EARD, 'f', False), L(ell(62, 64, 6, 7), EARD, 'f', False), L(ell(38, 64, 3, 4), WHITE, 'f', False), L(ell(62, 64, 3, 4), WHITE, 'f', False),
                L([(50, 36), (50, 80)], _c('#c8b8a0'), 'f', False, False, 1.0),
                L(blob([(26, 82), (50, 76), (74, 82), (68, 104), (50, 110), (32, 104)], 6), EARD, 'f')]
    if view == 'side':
        return [L(ell(40, 44, 16, 18), EAR), L(outline([(44, 10), (40, -10), (52, -20, 1), (62, -8), (60, 10)]), EARD),
                L(blob([(30, 40), (60, 10), (86, 30), (90, 50), (60, 50)], 6), _c('#fcf69f')),
                L(blob([(64, 44), (92, 46), (92, 84), (66, 86)], 5), MSKC, 'f'), L(ell(84, 64, 3.4, 6), EARD, 'f', False),
                L(blob([(66, 84), (94, 82), (92, 104), (70, 106)], 5), EARD, 'f')]
    return [L(ell(4, 46, 16, 18), EAR), L(ell(96, 46, 16, 18), EAR), L(outline([(40, 10), (38, -10), (50, -20, 1), (62, -10), (60, 10)]), EARD),
            L(blob([(12, 76), (14, 26), (50, 8), (86, 26), (88, 76), (50, 84)], 6), _c('#fcf69f'))]
C('seamus-club-rock', 'normal', P('#fcf69f', '#f2c896', iris='#1a1a1a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _seamus('front'), _seamus('side'), _seamus('back'))

# Sean Wujing: disfraz de kappa: un sombrero ancho verde como un caparazón con el plato crema encima, y un pico amarillo que
# le tapa la boca; debajo, los ojos oscuros
KAP, KAPD, PLATE, BEAKY = _c('#4e735c'), _c('#344c3c'), _c('#e2e0b0'), _c('#ddc95c')
def _kappa(view):
    if view == 'front':
        return [L(outline([(-12, 46, 1), (2, 28), (20, 12), (50, 4), (80, 12), (98, 28), (112, 46, 1), (90, 50), (76, 64, 1), (60, 54), (50, 62, 1), (40, 54), (24, 64, 1), (10, 50)]), KAP),
                L(ell(50, 12, 18, 6), PLATE, 'f'), L(blob([(60, 6), (90, 18), (106, 42), (84, 40)], 5), KAPD, 'b', False),
                L(blob([(30, 84), (50, 78), (70, 84), (60, 100), (50, 106), (40, 100)], 5), BEAKY, 'f'), L([(36, 88), (50, 92), (64, 88)], _c('#a89838'), 'f', False, False, 1.2)]
    if view == 'side':
        return [L(outline([(-10, 44, 1), (6, 24), (30, 8), (56, 4), (84, 12), (104, 32), (114, 48, 1), (90, 52), (70, 60, 1), (40, 52), (10, 52)]), KAP),
                L(ell(54, 8, 14, 5), PLATE, 'f'), L(blob([(76, 82), (92, 80), (102, 92, 1), (84, 102), (76, 96)], 5), BEAKY, 'f')]
    return [L(outline([(-12, 46, 1), (2, 28), (20, 12), (50, 4), (80, 12), (98, 28), (112, 46, 1), (90, 52), (50, 58), (10, 52)]), KAP),
            L(ell(50, 12, 18, 6), PLATE, 'f'), L(blob([(14, 50), (50, 54), (86, 50), (84, 82), (50, 88), (16, 82)], 6), _c('#2a2a26'))]
C('sean-sandy-wujing', 'normal', P('#2a2a26', '#e2e9c9', iris='#1a1a1a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _kappa('front') + [L([(28, 70), (44, 74), (40, 78), (30, 76)], BLACK, 'f', False, True), L([(72, 70), (56, 74), (60, 78), (70, 76)], BLACK, 'f', False, True),
                     L(ell(37, 75, 1.4, 1.4), WHITE, 'f', False), L(ell(63, 75, 1.4, 1.4), WHITE, 'f', False)],
  _kappa('side') + [L([(76, 70), (88, 72), (86, 78), (78, 76)], BLACK, 'f', False, True)],
  _kappa('back'))

# Serge Major: carota ancha morena con una gorra de policía azul petróleo oscuro de visera negra y la chapa plateada; le salen
# rizos rubio muy claro por los lados; cejas rubias en pico, ojos blancos de enfado, nariz ganchuda y la boca torcida
POL, POLV = _c('#1a3a40'), _c('#141414')
def _police(view):
    if view == 'front':
        return [L(blob([(14, 34), (20, 12), (50, 2), (80, 12), (86, 34), (50, 30)], 6), POL), L(blob([(16, 30), (50, 26), (84, 30), (84, 40), (50, 36), (16, 40)], 4), POLV, 'f'),
                L(ell(50, 32, 4, 4), _c('#b8bcc0'), 'f'), L(ell(50, 32, 2, 2), _c('#6a6e72'), 'f', False)]
    if view == 'side':
        return [L(blob([(14, 32), (22, 10), (52, 0), (80, 8), (88, 26), (50, 30)], 6), POL), L(blob([(70, 26), (100, 30), (98, 36), (70, 34)], 3), POLV, 'f')]
    return [L(blob([(12, 38), (20, 12), (50, 2), (80, 12), (88, 38), (50, 34)], 6), POL), L([(14, 36), (86, 36)], POLV, 'f', False, False, 3.0)]
BLD = _c('#ebe6b0')
C('serge-major', 'corpulento', P('#ebf0c8', '#af8c71', iris='#1a1a1a', shade='#c8c8a0'),
  F(eyes='none', brows=False, mouth='none', face_front=face(w=8, chin=106, jaw=8), face_side=face_side(chin=6, jaw=6, nose=5), hairline=False),
  [L(curls(8, 56, (12, 16), 5)), L(curls(92, 56, (12, 16), 5)), L(curls(50, 32, (36, 12), 7))] + _police('front') +
  [L(blob([(22, 64), (40, 70), (44, 76), (26, 72)], 3), BLD, 'f'), L(blob([(78, 64), (60, 70), (56, 76), (74, 72)], 3), BLD, 'f'),
   L([(28, 74), (44, 77), (40, 82), (30, 80)], WHITE, 'f', False, True), L([(72, 74), (56, 77), (60, 82), (70, 80)], WHITE, 'f', False, True),
   L(ell(37, 78, 1.5, 1.5), BLACK, 'f', False), L(ell(63, 78, 1.5, 1.5), BLACK, 'f', False),
   L([(48, 72), (52, 86), (46, 90)], _c('#8a6a50'), 'f', False, False, 1.4), L(quad((40, 100), (50, 94), (60, 100)), OUTC, 'f', False, False, 1.6)],
  [L(curls(34, 52, (14, 16), 5)), L(curls(46, 30, (36, 12), 7))] + _police('side') +
  [L([(74, 74), (86, 77), (84, 82), (76, 80)], WHITE, 'f', False, True), L(blob([(70, 66), (86, 70), (84, 74), (72, 72)], 3), BLD, 'f')],
  [L(curls(50, 54, (40, 26), 9))] + _police('back'))

# Seth Paynter: pelo rubio en mechones con un flequillo echado a un lado y una boina azul marino ladeada; ojos castaños
# grandes, pecas y la boca pequeña de preocupación
BER = _c('#1e4f7b')
C('seth-paynter', 'normal', P('#dcb67e', '#f5f2d2', iris='#7a3a14', shade='#b89060'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=95, hairline=[(6, 66), (16, 54), (30, 52), (44, 58), (58, 46), (74, 50), (88, 56), (94, 66)]),
  dome('front', top=4, w=48, cy=46, n=8, amp=6, soft=True, seed=67, sb=80) +
  [L(blob([(12, 26), (20, 4), (50, -6), (82, 2), (96, 16), (84, 30), (50, 22), (20, 32)], 6), BER), L(quad((72, 2), (78, -8), (84, -4)), BER, 'b', True, False, 2.4),
   L(outline([(54, 30), (70, 34), (66, 50), (58, 60, 1), (56, 46)]), 'mid', 'f')] +
  [L(ell(x, 88, 0.9, 0.9), _c('#c08a60'), 'f', False) for x in (30, 34, 32, 66, 70, 68)],
  dome('side', top=4, w=48, cy=46, n=8, amp=6, soft=True, seed=67, nape=88, fr=56) +
  [L(blob([(8, 26), (20, 4), (52, -4), (84, 6), (90, 20), (50, 24), (16, 34)], 6), BER)],
  dome('back', top=4, w=48, cy=46, n=8, amp=6, soft=True, seed=67, nape=88) + [L(blob([(6, 18), (20, 0), (50, -6), (80, 4), (90, 28), (50, 26), (14, 30)], 6), BER)])

# Severin Volei: rastas azul pizarra recogidas hacia atrás con una cinta ancha amarillo anaranjado (con una franja roja y
# negra) en la frente y una trenza envuelta en tela clara que le cae por un lado; ojos verdes y la boca seria
HB2, HBR = _c('#f0b020'), _c('#c02a20')
C('severin-volley-volei', 'chica', P('#35414d', '#cfa47d', iris='#6a7a30', shade='#282c31'),
  F(eyes='normal', brows=True, mouth='frown', mouth_y=94, hairline=[(6, 60), (16, 56), (50, 54), (84, 56), (94, 60)]),
  [L(rope((20, 30), (10, 70), (16, 102), 7)), L(rope((78, 40), (84, 80), (78, 112), 6), _c('#e8dcc0')), L(rope((30, 70), (20, 90), (8, 104), 7))] +
  dome('front', top=6, w=46, cy=46, sb=60) + [band('front', 38, 14, HB2), L([(70, 46), (84, 48)], HBR, 'f', False, False, 2.4)] + lashes(75),
  [L(rope((30, 40), (14, 70), (20, 100), 7)), L(rope((40, 60), (26, 90), (30, 110), 7))] + dome('side', top=6, w=46, cy=46, nape=80, fr=42) + [band('side', 38, 14, HB2)] + lash_side(75),
  [L(rope((24, 40), (16, 80), (22, 108), 7)), L(rope((40, 40), (36, 80), (40, 112), 7)), L(rope((60, 40), (64, 80), (60, 112), 7)), L(rope((76, 40), (84, 80), (78, 108), 7))] +
  dome('back', top=6, w=46, cy=46, nape=80) + [band('back', 40, 14, HB2)])

# Shadi Mesmer: melena morada oscura peinada hacia atrás que se abre en mechones de punta sobre los hombros, con una cinta
# gris fina; piel morena, cara larga con arrugas, ojos azules pequeños, labios gruesos y una perilla fina
C('shadi-mesmer', 'delgado', P('#524255', '#cd956a', iris='#4a5aa0', shade='#423038'),
  F(eyes='sharp', brows='angry', mouth='lips', mouth_y=97, mouth_w=8, face_front=face(w=-1, chin=108), face_side=face_side(chin=8, nose=3),
    hairline=[(6, 58), (18, 44), (34, 38), (50, 40), (66, 38), (82, 44), (94, 58)], nose=(50, 86, 2.4)),
  dome('front', top=6, w=46, cy=46, long=104, flare=14, ends=3) + [L(quad((14, 40), (50, 18), (86, 40)), _c('#b0b0b8'), 'f', False, False, 1.6),
   L([(50, 104), (50, 110)], OUTC, 'f', False, False, 1.2), L([(30, 84), (34, 92)], _c('#9c6747'), 'f', False, False, 1.0), L([(70, 84), (66, 92)], _c('#9c6747'), 'f', False, False, 1.0)],
  dome('side', top=6, w=46, cy=46, long=104, flare=14, fr=40),
  dome('back', top=6, w=46, cy=46, long=104, flare=14, ends=5))

# Shelley Wordsworth: rastas largas granate oscuro hasta la mandíbula con una cinta naranja en la frente; piel morena,
# cejas gruesas muy fruncidas, ojos blancos de enfado y labios gruesos
HBO = _c('#f0a020')
C('shelley-wordsworth', 'normal', P('#5e2a2c', '#d19661', iris='#1a1a1a', shade='#482120'),
  F(eyes='round', brows=False, mouth='lips', mouth_y=97, mouth_w=7, hairline=[(6, 60), (18, 48), (34, 44), (50, 46), (66, 44), (82, 48), (94, 60)]),
  dome('front', top=4, w=48, cy=46, long=104, flare=4, ends=3) +
  [L(rope((16, 40), (12, 70), (14, 104), 7)), L(rope((84, 40), (88, 70), (86, 104), 7)), band('front', 22, 7, HBO)] + thick_brows(64, 'shade', 4.4, 15, 1.4, 14),
  dome('side', top=4, w=48, cy=46, long=104, flare=4, fr=46) + [L(rope((50, 50), (46, 80), (50, 104), 7)), band('side', 20, 7, HBO)] + side_brow(64, 'shade', 4.4, 1.4),
  dome('back', top=4, w=48, cy=46, long=104, flare=4, ends=5) + [band('back', 24, 7, HBO)])

# Shep Woolacombe: disfraz de oveja: lana gris beige en bultos que le cubre la cabeza, con dos cuernos dorados de carnero
# enroscados a los lados; ojos verdes caídos de sueño y la boca pequeña
WOOL, WOOLD, RAM, RAMD = _c('#c4aa91'), _c('#957261'), _c('#c8960e'), _c('#8b590f')
def _ram(x):
    return [L(curls(x, 56, (14, 16), 5, 0.2), RAM, 'f'), L(ell(x, 56, 7, 8), RAMD, 'f', False), L(ell(x, 56, 3, 3.6), RAM, 'f', False)]
C('shep-woolacombe', 'normal', P('#c4aa91', '#feeab8', iris='#6a8a30', shade='#957261'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=96, hairline=[(6, 70), (18, 66), (30, 62), (50, 64), (70, 62), (82, 66), (94, 70)], ears=False),
  [L(curls(50, 40, (48, 34), 11, 0.1)), L(curls(20, 76, (12, 16), 5)), L(curls(80, 76, (12, 16), 5)), L(blob([(58, 10), (86, 26), (94, 50), (74, 40)], 5), 'shade', 'b', False)] +
  _ram(8) + _ram(92) + [L([(30, 72), (44, 74)], OUTC, 'f', False, False, 2.4), L([(70, 72), (56, 74)], OUTC, 'f', False, False, 2.4)],
  [L(curls(44, 44, (48, 36), 11, 0.1))] + _ram(44),
  [L(curls(50, 46, (50, 40), 12, 0.1))] + _ram(8) + _ram(92))

# Si Sosman (portero): gorro de lana crema con la vuelta verde oliva y un pompón rojo; le asoman pinchos castaños por la
# frente y los lados; piercings en una ceja, ojos de enfado y la boca fruncida
BEA, BEAB, POM = _c('#faf6dc'), _c('#a08608'), _c('#c84a20')
def _beanie2(view):
    if view == 'front':
        return [L(blob([(14, 50), (16, 22), (32, 4), (50, -2), (68, 4), (84, 22), (86, 50), (50, 44)], 6), BEA),
                L(blob([(12, 42), (50, 34), (88, 42), (90, 56), (50, 50), (10, 56)], 4), BEAB, 'f'),
                L(outline([(44, -2), (42, -10, 1), (48, -8), (50, -16, 1), (52, -8), (58, -10, 1), (56, -2)]), POM, 'f')]
    if view == 'side':
        return [L(blob([(10, 50), (14, 20), (34, 2), (54, -2), (78, 8), (88, 30), (86, 46), (50, 46)], 6), BEA),
                L(blob([(8, 44), (50, 38), (88, 38), (88, 50), (50, 52), (8, 58)], 4), BEAB, 'f'),
                L(outline([(46, -2), (44, -10, 1), (50, -8), (52, -16, 1), (54, -8), (60, -10, 1), (58, -2)]), POM, 'f')]
    return [L(blob([(12, 56), (16, 22), (32, 4), (50, -2), (68, 4), (84, 22), (88, 56), (50, 50)], 6), BEA),
            L(blob([(10, 48), (50, 40), (90, 48), (90, 62), (50, 56), (10, 62)], 4), BEAB, 'f'),
            L(outline([(44, -2), (42, -10, 1), (48, -8), (50, -16, 1), (52, -8), (58, -10, 1), (56, -2)]), POM, 'f')]
C('si-sosman', 'normal', P('#783b09', '#f2c095', iris='#1a1a1a', shade='#5a2c06'),
  F(eyes='sharp', brows='angry', mouth='none', hairline=[(6, 66), (18, 60), (30, 66), (40, 54), (50, 66), (60, 54), (70, 66), (82, 60), (94, 66)]),
  [L(outline([(12, 56), (6, 72, 1), (14, 70), (10, 90, 1), (20, 78), (24, 60)])), L(outline([(88, 56), (94, 72, 1), (86, 70), (90, 90, 1), (80, 78), (76, 60)])),
   L(outline([(20, 50), (40, 50), (50, 44), (60, 50), (80, 50), (70, 68, 1), (60, 56), (50, 72, 1), (40, 56), (30, 68, 1)]))] + _beanie2('front') +
  [L(ell(60, 63, 1.4, 1.4), _c('#c8ccd0'), 'f', False), L(ell(64, 61, 1.4, 1.4), _c('#c8ccd0'), 'f', False), L(ell(50, 96, 2.4, 2.8), MOUTH, 'f', False, True)],
  [L(outline([(50, 54), (44, 70, 1), (54, 68), (50, 88, 1), (60, 74), (62, 56)])), L(outline([(60, 48), (88, 46), (82, 60, 1), (74, 54), (68, 64, 1)]))] + _beanie2('side'),
  [L(outline([(10, 60), (6, 80, 1), (16, 74), (14, 90, 1), (26, 80), (50, 86), (74, 80), (86, 90, 1), (84, 74), (94, 80, 1), (90, 60)]))] + _beanie2('back'))

# Sigmund Wayfinder: casco vikingo de cúpula azul grisáceo con el reborde y la nasal plateados y dos cuernos blancos; le sale
# el pelo castaño en mechones de punta por los lados; ojos blancos sin pupila, nariz larga y la boca recta
VK, VKS, VKH = _c('#3e5764'), _c('#b5b8b9'), _c('#ece4d4')
def _viking(view):
    if view == 'front':
        return [L(blob([(14, 50), (16, 22), (32, 4), (50, -2), (68, 4), (84, 22), (86, 50), (50, 46)], 6), VK),
                L(blob([(12, 44), (50, 38), (88, 44), (88, 54), (50, 48), (12, 54)], 4), VKS, 'f'), L(blob([(44, -2), (56, -2), (56, 74), (50, 78), (44, 74)], 3), VKS, 'f'),
                L(outline([(18, 24), (4, 18), (-2, 2, 1), (8, 6), (22, 14)]), VKH, 'f'), L(outline([(82, 24), (96, 18), (102, 2, 1), (92, 6), (78, 14)]), VKH, 'f')]
    if view == 'side':
        return [L(blob([(10, 50), (14, 20), (34, 2), (54, -2), (78, 8), (88, 30), (86, 46), (50, 46)], 6), VK),
                L(blob([(8, 44), (50, 38), (88, 38), (88, 48), (50, 50), (8, 56)], 4), VKS, 'f'), L(blob([(82, 36), (90, 38), (92, 70), (86, 72)], 3), VKS, 'f'),
                L(outline([(40, 18), (30, 8), (28, -8, 1), (40, 0), (50, 12)]), VKH, 'f')]
    return [L(blob([(12, 54), (16, 22), (32, 4), (50, -2), (68, 4), (84, 22), (88, 54), (50, 50)], 6), VK),
            L(blob([(10, 48), (50, 42), (90, 48), (90, 58), (50, 52), (10, 58)], 4), VKS, 'f'), L(blob([(46, -2), (54, -2), (54, 44), (46, 44)], 2), VKS, 'f'),
            L(outline([(18, 24), (4, 18), (-2, 2, 1), (8, 6), (22, 14)]), VKH, 'f'), L(outline([(82, 24), (96, 18), (102, 2, 1), (92, 6), (78, 14)]), VKH, 'f')]
C('sigmund-wayfinder', 'normal', P('#742f04', '#fcc171', iris='#1a1a1a', shade='#5a2404'),
  F(eyes='none', brows=False, mouth='line', mouth_y=97, face_front=face(chin=104), hairline=False, nose=(50, 88, 2.4)),
  [L(outline([(16, 50), (0, 56, 1), (10, 64), (-4, 76, 1), (12, 78), (4, 94, 1), (20, 86), (24, 60)])),
   L(outline([(84, 50), (100, 56, 1), (90, 64), (104, 76, 1), (88, 78), (96, 94, 1), (80, 86), (76, 60)]))] + _viking('front') +
  [L(ell(36, 72, 4.4, 3.4), WHITE, 'f'), L(ell(64, 72, 4.4, 3.4), WHITE, 'f')],
  [L(outline([(48, 50), (28, 56, 1), (38, 66), (24, 80, 1), (42, 80), (34, 96, 1), (54, 84), (60, 60)]))] + _viking('side') + [L(ell(80, 72, 3, 3.2), WHITE, 'f')],
  [L(outline([(12, 50), (-2, 60, 1), (8, 70), (0, 86, 1), (16, 84), (14, 96, 1), (30, 88), (50, 92), (70, 88), (86, 96, 1), (84, 84), (100, 86, 1), (92, 70), (102, 60, 1),
              (88, 50)]))] + _viking('back'))

# Simon Borg: pelo gris verdoso en una nube de rizos; un ojo robótico con un aro metálico enorme y una lucecita roja, el otro
# ojo redondo de punto; sonrisa con un diente de menos
MET, METD, RLED = _c('#b8b4a0'), _c('#6a6650'), _c('#c81e1e')
C('simon-roboboy-borg', 'normal', P('#8a9c6e', '#e4cfb8', iris='#1a1a1a', shade='#6e7e56'),
  F(eyes='none', brows=False, mouth='none', hairline=[(6, 62), (18, 52), (30, 56), (42, 48), (54, 56), (66, 48), (78, 54), (94, 62)]),
  [L(curls(50, 34, (50, 32), 12, 0.2)), L(blob([(62, 10), (90, 24), (98, 46), (78, 40)], 5), 'shade', 'b', False)] +
  [L(ell(36, 77, 5.6, 5.6), WHITE, 'f'), L(ell(36, 77, 3, 3), BLACK, 'f', False),
   L(ell(64, 76, 10, 10), MET, 'f'), L(ell(64, 76, 7, 7), METD, 'f', False), L(ell(64, 76, 5.4, 5.4), BLACK, 'f', False), L(ell(62, 74, 1.6, 1.6), WHITE, 'f', False),
   L(ell(74, 66, 3, 3), RLED, 'f'), L([(46, 77), (54, 77)], MET, 'f', False, False, 1.6),
   L([(42, 94), (58, 94), (56, 99), (44, 99)], WHITE, 'f', False, True), L([(48, 94), (48, 99)], BLACK, 'f', False, False, 2.0)],
  [L(curls(44, 36, (48, 32), 11, 0.2))] + [L(ell(82, 76, 7, 9), MET, 'f'), L(ell(83, 76, 4, 5), BLACK, 'f', False), L(ell(86, 66, 2.6, 2.6), RLED, 'f'),
                                           L([(80, 94), (87, 94), (86, 99), (80, 98)], WHITE, 'f', False, True)],
  [L(curls(50, 40, (52, 38), 12, 0.2))])

# Skyler Styler: pelo rojo anaranjado en pinchos alborotados con mechones largos a los lados de la cara; cejas arqueadas,
# ojos afilados, una cicatriz en cruz en la mejilla y sonrisa pícara de dientes
C('skyler-stiler-styler', 'chica', P('#c55944', '#fbc274', iris='#1a1a1a', shade='#933e2c'),
  F(eyes='sharp', brows=True, mouth='none', hairline=hl(6, 66, 48, 60, jit=3, seed=23)),
  dome('front', top=-10, w=50, cy=44, n=9, amp=15, seed=69, long=88, flare=10, ends=2) +
  [L([(26, 84), (34, 92)], _c('#6a3a2a'), 'f', False, False, 1.4), L([(34, 84), (26, 92)], _c('#6a3a2a'), 'f', False, False, 1.4)] + tooth_mouth(94, 8, 4) + lashes(75),
  dome('side', top=-10, w=50, cy=44, n=9, amp=15, seed=69, long=88, flare=10, fr=52) + side_teeth(94) + lash_side(75),
  dome('back', top=-10, w=50, cy=44, n=9, amp=15, seed=69, long=88, flare=10, ends=4))

# Snezhana White: media melena morado oscuro con las puntas vueltas hacia dentro, como Blancanieves, y una diadema roja; ojos
# negros grandes con pestañas y sonrisa
RHB = _c('#e73f14')
C('snezhana-snowy-white', 'chica', P('#4e3868', '#f6edc7', iris='#1a1a1a', shade='#402a42'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=94, hairline=[(6, 64), (16, 50), (30, 44), (50, 46), (70, 44), (84, 50), (94, 64)]),
  dome('front', top=2, w=50, cy=46, sb=70, shade=True) +
  [L(curls(14, 80, (12, 12), 5)), L(curls(86, 80, (12, 12), 5)), L(quad((16, 28), (50, 4), (84, 28)), RHB, 'f', False, False, 4.0)] + lashes(76),
  dome('side', top=2, w=50, cy=46, nape=84, fr=46) + [L(curls(24, 80, (16, 14), 5)), L(quad((50, 8), (60, 20), (76, 22)), RHB, 'f', False, False, 4.0)] + lash_side(76),
  dome('back', top=2, w=50, cy=46, nape=84) + [L(curls(50, 82, (40, 14), 8)), L(quad((16, 30), (50, 8), (84, 30)), RHB, 'f', False, False, 4.0)])
