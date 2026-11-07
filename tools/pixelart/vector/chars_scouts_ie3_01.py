"""Ojeadores de IE3 (scouts-ie3), tanda 01: dibujados a partir de su retrato de Victory Road (casi ninguno tiene modelo 3D;
el de Bucky Rodeo Colt que da la enciclopedia es de otro personaje); claves 'scouts-ie3:<id>'. El perfil y la espalda se
deducen del peinado del retrato. Reutiliza ayudas de las tandas de IE1 e IE2 (dome/hl/face de ie1_09, bowl/cejas/gafas de
ie1_03, narices de ie1_10, curls/gafas redondas de ie2_03, pestañas y ojos afilados de ie2_04)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars import messy  # noqa: F401
from chars_scouts_ie1_02 import mir  # noqa: F401
from chars_scouts_ie1_03 import (big_grin, blush, bowl, eyes_custom, fr, freckles, goggles, round_specs, shades,  # noqa: F401
                                 side_brow, side_eye_custom, stache, thick_brows)
from chars_scouts_ie1_09 import _c, dome, face, face_side, hl, mark  # noqa: F401
from chars_scouts_ie1_10 import nose_line, nose_tri, squint  # noqa: F401
from chars_scouts_ie2_03 import curls, ears_pointy, round_glasses, skull, teeth_grin  # noqa: F401
from chars_scouts_ie2_04 import band, lash_side, lashes, sharp_eye_side, sharp_eyes, strands_down  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401

K = 'scouts-ie3:'
WHITE = (250, 250, 250, 255)
BLACK = (24, 18, 20, 255)
LIP = (214, 110, 90, 255)
RED = (196, 44, 34, 255)
PINK = (232, 120, 140, 255)
GOLD = (216, 168, 48, 255)


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


def ring(cx, cy, rx, ry, c=BLACK, w=2.2):
    pts = ell(cx, cy, rx, ry)
    return L(pts + [pts[0]], c, 'f', False, False, w)


def three(fn, **k):
    return fn('front', **k), fn('side', **k), fn('back', **k)


# ---------------------------------------------------------------------------------------------------------------- 1-8

# Aaron Dainty Gossamer (portero): melena crema clarísima echada a un lado que le tapa el ojo derecho y sale en un ala hacia
# fuera; del otro lado le cae hasta el hombro; ojo verde y boca apretada
C('aaron-dainty-gossamer', 'normal', P('#f8f0cc', '#f6dcc0', '#6a7a2a', shade='#e4d4a4', deep='#c8b888'),
  F(eyes='normal', brows=False, mouth='frown', mouth_y=93, hairline=[(8, 64), (16, 48), (40, 40), (64, 40), (84, 48), (92, 64)]),
  dome('front', top=0, w=47, cy=46, sb=74) +
  [L(outline([(82, 52), (94, 56), (98, 96), (92, 108, 1), (86, 92), (84, 70)]), 'mid', 'f'),
   fr([(8, 54), (22, 32), (46, 24), (68, 30), (62, 46), (54, 62), (50, 88, 1), (44, 72), (36, 86, 1), (30, 72), (18, 80)]),
   fr([(14, 48), (-10, 64, 1), (2, 66), (-6, 76, 1), (16, 70)]),
   strand([(30, 34), (40, 60)], 'shade', 'f', 1.0), strand([(44, 30), (48, 66)], 'shade', 'f', 1.0)],
  dome('side', top=0, w=47, cy=46, long=104, fr=56) + [fr([(66, 30), (88, 40), (92, 56), (84, 54), (80, 66, 1), (74, 50)])],
  dome('back', top=0, w=47, cy=46, long=104, ends=5))

# Abel Forager (portero): pelo granate oscuro peinado en tupé con raya al medio y los lados cortos; cejas gruesas y ojos
# rojizos afilados, boca pequeña de enfado
C('abel-forager', 'normal', P('#67454c', '#f8c27e', '#7a1e1e', shade='#503335', deep='#3a2224'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=[(10, 64), (18, 48), (34, 42), (50, 48), (66, 42), (82, 48), (90, 64)]),
  [L(outline([(16, 66), (12, 44), (16, 20), (30, 6), (46, 4), (50, 12), (54, 2), (72, 4), (86, 18), (90, 44), (84, 66), (80, 52), (20, 52)])),
   L(outline([(56, 4), (76, 8), (88, 26), (88, 50), (80, 30)]), 'shade', 'b', False), strand([(50, 12), (48, 40)], 'deep', 'b', 1.2)],
  dome('side', top=2, w=46, cy=44, nape=82, fr=46) + [fr([(60, 6), (86, 14), (92, 32), (80, 30)])],
  dome('back', top=2, w=46, cy=44, nape=82))

# Adam Montayne: grandullón de piel grisácea, cabeza rapada con un pelo oscuro muy corto y una cresta crema pequeña; ojos
# entornados, perilla oscura en forma de almena, rayas crema en las mejillas y un pañuelo amarillo al cuello
DK, CRM, YEL = _c('#3a2e24'), _c('#e2d2bc'), _c('#c89020')
def _montayne(view):
    if view == 'front':
        return skull('front') + [L(outline([(16, 62), (14, 40), (26, 18), (50, 10), (74, 18), (86, 40), (84, 62), (80, 48), (20, 48)]), DK),
                                 L(outline([(36, 18), (40, 6, 1), (45, 13), (50, 2, 1), (55, 13), (60, 6, 1), (64, 18), (50, 22)]), CRM)]
    if view == 'side':
        return skull('side') + [L(outline([(78, 50), (84, 34), (74, 14), (50, 6), (26, 10), (8, 28), (4, 52), (10, 72), (24, 76), (40, 66), (52, 56), (66, 50)]), DK),
                                L(outline([(40, 10), (46, -2, 1), (52, 8), (60, 0, 1), (64, 12), (52, 16)]), CRM)]
    return skull('back') + [L(outline([(12, 74), (10, 40), (24, 16), (50, 8), (76, 16), (90, 40), (88, 74), (50, 82)]), DK),
                            L(outline([(38, 14), (44, 2, 1), (50, 10), (56, 2, 1), (62, 14), (50, 18)]), CRM)]
C('adam-montayne', 'corpulento', P('#3a2e24', '#ad8b72', '#1e1a1a'),
  F(eyes='none', brows=False, mouth='line', mouth_y=91, hairline=False, face_front=face(w=6, chin=106, jaw=4), ear_out=3),
  _montayne('front') +
  [L([(26, 76), (43, 77)], BLACK, 'f', False, False, 3.0), L([(57, 77), (74, 76)], BLACK, 'f', False, False, 3.0),
   L([(26, 70), (44, 71)], BLACK, 'f', False, False, 3.4), L([(56, 71), (74, 70)], BLACK, 'f', False, False, 3.4),
   mark([(36, 94), (44, 93), (46, 98), (54, 98), (56, 93), (64, 94), (62, 106), (56, 102), (54, 108), (46, 108), (44, 102), (38, 106)], DK),
   L([(20, 84), (26, 82), (30, 86)], CRM, 'f', False, False, 1.8), L([(80, 84), (74, 82), (70, 86)], CRM, 'f', False, False, 1.8),
   L(outline([(16, 98), (50, 108), (84, 98), (90, 108), (62, 116), (50, 124, 1), (38, 116), (10, 108)]), YEL, 'f')],
  _montayne('side') + [L([(76, 76), (86, 76)], BLACK, 'f', False, False, 3.0), mark([(80, 94), (88, 94), (86, 106), (78, 104)], DK),
                       L(outline([(40, 96), (84, 100), (86, 110), (40, 110)]), YEL, 'f')],
  _montayne('back') + [L(outline([(14, 102), (50, 110), (86, 102), (88, 112), (50, 118), (12, 112)]), YEL, 'f')])

# Adam Venturus: coronilla calva crema y rizos verde oliva oscuros a los lados; ojos redondos de enfado, nariz naranja en
# triángulo y labios gruesos
OL = _c('#5a5236')
C('adam-venturus', 'normal', P('#e8dab8', '#f6be76', '#1e1a1a', shade='#d2c098'),
  F(eyes='round', brows='angry', mouth='lips', mouth_y=95, mouth_w=12, hairline=False),
  [L(outline([(16, 64), (14, 36), (26, 12), (50, 4), (74, 12), (86, 36), (84, 64), (50, 60)])),
   L(curls(12, 60, (12, 22), 6, 0.3), OL), L(curls(88, 60, (12, 22), 6, 0.7), OL)] + nose_tri(87, 5, 11, _c('#e08a40')),
  [L(outline([(80, 50), (86, 30), (74, 10), (50, 2), (24, 8), (8, 28), (6, 50), (24, 40), (52, 38)])),
   L(curls(26, 62, (22, 22), 8), OL)],
  [L(outline([(12, 70), (10, 36), (24, 12), (50, 4), (76, 12), (90, 36), (88, 70), (50, 66)])), L(curls(50, 74, (44, 18), 10), OL)])

# Adora Shivers: melena lila larga con un mechón enorme que le baja en curva por un lado de la cara hasta el pecho, y una
# coleta baja al otro lado; ojos ámbar con pestañas y media sonrisa
C('adora-shivers', 'chica', P('#94799a', '#fcd0a2', '#a8822a', shade='#765866', deep='#5c4048'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=93, hairline=[(10, 66), (18, 50), (34, 40), (52, 42), (68, 40), (82, 46), (90, 62)]),
  dome('front', top=0, w=46, cy=44, sb=70) +
  [L(outline([(76, 62), (92, 72), (98, 96), (90, 104, 1), (84, 86), (78, 76)]), 'shade', 'b'),
   fr([(14, 46), (34, 24), (60, 18), (56, 30), (40, 44), (28, 64), (22, 96), (16, 126, 1), (10, 96), (8, 64)]),
   strand([(40, 28), (22, 70), (16, 110)], 'shade', 'f', 1.0)] + lashes(),
  dome('side', top=0, w=46, cy=44, nape=86, fr=48) +
  [L(outline([(16, 64), (2, 70), (-6, 92), (2, 112, 1), (10, 92), (22, 78)]), 'mid', 'b'), L(ell(16, 68, 4, 4), 'deep', 'b')] + lash_side(),
  dome('back', top=0, w=46, cy=44, nape=86) + [L(outline([(54, 72), (70, 76), (74, 100), (64, 118, 1), (56, 100)])), L(ell(60, 76, 6, 4), 'deep', 'b')])

# Aidull Wanabi: canotier blanco con cinta negra, melena lisa negra en casco y un mechón lima en un lado; ojos entornados y
# boca recta de aburrido
HAT, LIME = _c('#d8e8e8'), _c('#c8d84a')
def _boater(view):
    if view == 'front':
        return [L(blob([(2, 32), (30, 22), (70, 16), (100, 22), (98, 30), (70, 28), (30, 34), (4, 40)], 6), HAT, 'f'),
                L(outline([(22, 28), (24, 4), (50, -2), (76, 2), (78, 24), (50, 26)]), HAT, 'f'),
                L(outline([(23, 18), (50, 16), (77, 14), (78, 23), (50, 25), (23, 27)]), BLACK, 'f', False)]
    if view == 'side':
        return [L(blob([(-6, 30), (40, 22), (100, 18), (98, 28), (40, 32), (-4, 38)], 6), HAT, 'f'),
                L(outline([(14, 26), (18, 2), (50, -4), (82, 2), (84, 22), (50, 26)]), HAT, 'f'),
                L(outline([(15, 16), (84, 12), (84, 21), (15, 25)]), BLACK, 'f', False)]
    return [L(blob([(0, 24), (50, 16), (100, 24), (98, 34), (50, 28), (2, 34)], 6), HAT, 'f'),
            L(outline([(22, 26), (24, 2), (50, -4), (76, 2), (78, 26), (50, 24)]), HAT, 'f'),
            L(outline([(23, 16), (77, 16), (78, 25), (23, 25)]), BLACK, 'f', False)]
C('aidull-wanabi', 'normal', P('#1e1e20', '#fbe6b4', '#1e1a1a'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=93, hairline=[(8, 66), (16, 56), (50, 52), (84, 56), (92, 66)]),
  bowl('front', top=12, side=96) + [fr([(28, 50), (34, 50), (30, 96), (26, 106, 1), (24, 80)], LIME)] + _boater('front'),
  bowl('side', top=12, nape=96) + _boater('side'), bowl('back', top=12, nape=98) + _boater('back'))

# Al Opino (portero): piel morena, pelo negro muy corto, cejas gordas de enfado, ojos redondos, nariz grande redonda y
# labios gruesos anaranjados
C('al-opino', 'normal', P('#2e2420', '#9a6a4c', '#1e1a1a', nose='#7a4e36'),
  F(eyes='round', brows='angry', mouth='lips', mouth_y=97, mouth_w=8, nose=(50, 87, 5), big_ears=2, face_front=face(w=2, chin=104),
    hairline=[(12, 62), (20, 46), (50, 42), (80, 46), (88, 62)]),
  dome('front', top=8, w=44, cy=46, sb=62, shade=False),
  dome('side', top=8, w=44, cy=46, nape=80, fr=44, shade=False, side_burn=False),
  dome('back', top=8, w=44, cy=46, nape=80, shade=False))

# Ameen Abel: pelo rubio ocre corto de punta hacia arriba, cara alargada pálida y orejas grandes; ojos de loco con ojeras y
# los dientes apretados
C('ameen-abel', 'delgado', P('#b88c20', '#e2caa8', '#1e1a1a', shade='#8a5c14'),
  F(eyes='round', brows='angry', mouth='grin', mouth_y=97, big_ears=2, face_front=face(chin=108), face_side=face_side(chin=6),
    hairline=hl(5, 60, 44, 54, jit=2, seed=11)),
  dome('front', top=-4, w=44, cy=44, n=7, amp=9, seed=12, sb=60) + [ring(36, 76, 7, 6, (90, 80, 70, 255), 1.4), ring(64, 76, 7, 6, (90, 80, 70, 255), 1.4)],
  dome('side', top=-4, w=44, cy=44, n=7, amp=9, seed=12, nape=80, fr=44),
  dome('back', top=-4, w=44, cy=44, n=7, amp=9, seed=12, nape=80))

# --------------------------------------------------------------------------------------------------------------- 9-16

# Amir "Dreams" Rika: gorra azul marino con estrellas y la visera roja girada a un lado, pelo castaño claro de pinchos que
# asoma por los lados; ojo verde y un globo de chicle verde menta
CAP, STAR, MINT = _c('#22438a'), _c('#c8a8a0'), _c('#b4e4ce')
def _cap(view):
    if view == 'front':
        return [L(outline([(10, 54), (10, 26), (28, 8), (56, 2), (80, 10), (92, 30), (90, 52), (50, 46)]), CAP, 'f'),
                L(blob([(2, 48), (28, 44), (40, 54), (22, 64), (-2, 60)], 6), RED, 'f'),
                L(outline([(60, 14), (64, 22), (72, 22), (66, 28), (68, 36), (60, 31), (52, 36), (54, 28), (48, 22), (56, 22)]), STAR, 'f', False),
                L(ell(52, 4, 3, 2), (220, 190, 60, 255), 'f', False)]
    if view == 'side':
        return [L(outline([(6, 56), (4, 30), (22, 8), (52, 2), (78, 10), (90, 30), (88, 50), (50, 50)]), CAP, 'f'),
                L(blob([(30, 46), (4, 46), (-6, 56), (26, 56)], 6), RED, 'f'),
                L(outline([(56, 14), (60, 22), (68, 22), (62, 28), (64, 36), (56, 31), (48, 36), (50, 28), (44, 22), (52, 22)]), STAR, 'f', False)]
    return [L(outline([(8, 60), (8, 28), (26, 8), (50, 2), (74, 8), (92, 28), (92, 60), (50, 54)]), CAP, 'f'),
            L(blob([(70, 50), (98, 46), (104, 56), (74, 60)], 6), RED, 'f')]
C('amir-dreams-rika', 'normal', P('#b08e6c', '#facf9e', '#4a8a2a', shade='#8a6c50'),
  F(eyes='big', brows=True, mouth='line', mouth_y=92, hairline=[(8, 66), (16, 54), (50, 50), (84, 54), (92, 66)]),
  messy('front', amp=10, n=9, seed=21, lo=70) + _cap('front') + [L(ell(38, 100, 10, 9), MINT, 'f')],
  messy('side', amp=10, n=9, seed=21, nape=88) + _cap('side') + [L(ell(90, 96, 7, 8), MINT, 'f')],
  messy('back', amp=10, n=9, seed=21, nape=90) + _cap('back'))

# Anders Thettock: melena gris a capas hasta la nuca con el flequillo echado a un lado; ojos rosados afilados
C('anders-thettock', 'normal', P('#aca098', '#f6c098', '#b0506a', shade='#8a706a', deep='#6c524c'),
  F(eyes='sharp', brows=True, mouth='line', mouth_y=93, hairline=[(10, 64), (18, 46), (34, 38), (54, 40), (72, 38), (84, 46), (90, 64)]),
  dome('front', top=0, w=47, cy=44, long=98, flare=2) +
  [fr([(12, 58), (20, 36), (44, 26), (72, 30), (86, 46), (88, 60), (76, 50), (64, 58, 1), (58, 46), (44, 60, 1), (36, 48), (24, 62, 1)])],
  dome('side', top=0, w=47, cy=44, long=100, fr=54) + [fr([(64, 30), (88, 40), (92, 58), (84, 52), (80, 64, 1), (74, 48)])],
  dome('back', top=0, w=47, cy=44, long=100, ends=5))

# Andy: pelo castaño verdoso corto de pinchos revueltos; ojitos negros, cejas finas y sonrisa
C('andy', 'normal', P('#5e4d26', '#f8bc7e', '#1e1a1a', shade='#48361e'),
  F(eyes='dot', brows=True, mouth='smile', mouth_y=93, nose=(50, 85, 2.2), hairline=hl(6, 62, 46, 56, jit=2, seed=23)),
  messy('front', amp=9, n=12, seed=24, lo=64), messy('side', amp=9, n=12, seed=24, nape=86), messy('back', amp=9, n=12, seed=24, nape=88))

# Anfaira D Vantage: adulto de cara larga, pelo castaño con raya al medio y una cinta roja con solapas plegadas que le caen
# por los lados de la cabeza como un casco; nariz grande, cejas de enfado
RD2, RD3 = _c('#c92b1c'), _c('#9a1e12')
def _flaps(view):
    if view == 'front':
        out = [L(blob([(8, 50), (30, 42), (50, 40), (70, 42), (92, 50), (92, 58), (70, 52), (50, 50), (30, 52), (8, 58)], 4), RD2, 'f')]
        for s in (-1, 1):
            x = 50 + s * 42
            out += [L(outline([(x - 14 * s, 50, 1), (x + 6 * s, 52, 1), (x + 8 * s, 78, 1), (x - 14 * s, 78, 1)]), RD2, 'f'),
                    L(outline([(x - 14 * s, 74, 1), (x + 8 * s, 74, 1), (x + 10 * s, 100, 1), (x - 12 * s, 100, 1)]), RD3, 'f')]
        return out
    if view == 'side':
        return [L(blob([(2, 50), (40, 42), (88, 40), (90, 48), (40, 52), (2, 58)], 4), RD2, 'f'),
                L(outline([(16, 50, 1), (52, 48, 1), (54, 76, 1), (14, 78, 1)]), RD2, 'f'), L(outline([(14, 74, 1), (50, 74, 1), (52, 100, 1), (12, 102, 1)]), RD3, 'f')]
    return [L(blob([(6, 50), (50, 44), (94, 50), (94, 58), (50, 52), (6, 58)], 4), RD2, 'f'),
            L(outline([(4, 54, 1), (34, 54, 1), (34, 80, 1), (2, 80, 1)]), RD2, 'f'), L(outline([(66, 54, 1), (96, 54, 1), (98, 80, 1), (66, 80, 1)]), RD2, 'f'),
            L(outline([(4, 76, 1), (34, 76, 1), (34, 100, 1), (4, 100, 1)]), RD3, 'f'), L(outline([(66, 76, 1), (96, 76, 1), (96, 100, 1), (66, 100, 1)]), RD3, 'f')]
C('anfaira-d-vantage', 'delgado', P('#6e3412', '#f8ba7c', '#1e1a1a', shade='#4a2410'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=97, face_front=face(chin=108), face_side=face_side(chin=6, nose=3),
    hairline=[(10, 62), (20, 50), (40, 44), (50, 48), (60, 44), (80, 50), (90, 62)]),
  dome('front', top=2, w=46, cy=44, sb=54) + [strand([(50, 6), (50, 40)], 'shade', 'b', 1.2)] + _flaps('front') + nose_tri(88, 4, 13),
  dome('side', top=2, w=46, cy=44, nape=70, fr=46) + _flaps('side'), dome('back', top=2, w=46, cy=44, nape=70) + _flaps('back'))

# Anil "Numbers" Latikal: pelo castaño en pinchos largos hacia todos lados, gafas de soldador verdes en la frente con su
# cinta; cara larga, ojos redondos con ojeras negras y nariz larga
GF, GL = _c('#8c8470'), _c('#3a7a5a')
C('anil-numbers-latikal', 'delgado', P('#705736', '#f8c072', '#1e1a1a', shade='#54402a'),
  F(eyes='round', brows=False, mouth='line', mouth_y=98, face_front=face(chin=108), face_side=face_side(chin=6, nose=4), hairline=[(8, 62), (16, 52), (50, 50), (84, 52), (92, 62)]),
  messy('front', amp=18, n=9, seed=31, lo=60) + [L(blob([(10, 54), (50, 50), (90, 54), (90, 60), (50, 56), (10, 60)], 4), (40, 44, 48, 255), 'f')] +
  goggles('front', 46, GF, GL) + [ring(36, 76, 8, 6.5, BLACK, 3.0), ring(64, 76, 8, 6.5, BLACK, 3.0)] + nose_tri(90, 4, 16),
  messy('side', amp=18, n=9, seed=31, nape=84) + goggles('side', 46, GF, GL),
  messy('back', amp=18, n=9, seed=31, nape=86) + [L(blob([(6, 54), (50, 48), (94, 54), (94, 60), (50, 54), (6, 60)], 4), (40, 44, 48, 255), 'f')])

# Anna Mite: pelo verde oscuro con una venda crema alrededor de la frente, un pico de flequillo entre los ojos y una
# coletita baja; ojos rojos de enfado
BAND = _c('#f4e2c0')
C('anna-mite', 'chica', P('#285246', '#fbc276', '#c02840', shade='#1e3a32'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=[(10, 66), (20, 58), (40, 60), (50, 72), (60, 60), (80, 58), (90, 66)]),
  dome('front', top=2, w=46, cy=44, sb=74) + [band('front', 30, 14, BAND),
                                              L(outline([(80, 78), (90, 86), (92, 100), (86, 106, 1), (82, 92)]), 'mid', 'f')],
  dome('side', top=2, w=46, cy=44, nape=86, fr=56) + [band('side', 30, 14, BAND), L(outline([(16, 76), (6, 84), (2, 102, 1), (12, 94), (22, 84)]))],
  dome('back', top=2, w=46, cy=44, nape=86) + [band('back', 30, 14, BAND), L(outline([(60, 80), (72, 86), (74, 104, 1), (64, 96)]))])

# Archie "S" Tarius Rider: pelo azul marino violáceo que se abre en alas a los lados, un mechón lavanda en pico por el centro
# de la cara y una diadema dorada; piel clara, ojos negros afilados y sonrisa
LAV = _c('#93a2cc')
C('archie-s-tarius-rider', 'normal', P('#4a445e', '#e6ceb0', '#1e1a1a', shade='#383142'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=93, hairline=[(8, 66), (16, 56), (34, 54), (50, 58), (66, 54), (84, 56), (92, 66)]),
  [L(outline([(-6, 68, 1), (10, 52), (16, 24), (50, 8), (84, 24), (90, 52), (106, 68, 1), (82, 66), (18, 66)])),
   L(outline([(56, 10), (82, 24), (90, 52), (96, 70), (80, 50)]), 'shade', 'b', False),
   fr([(40, 14), (50, 8), (60, 14), (56, 40), (50, 80, 1), (44, 40)], LAV),
   L(quad((14, 60), (50, 50), (86, 60)), GOLD, 'f', False, False, 2.6)],
  [L(outline([(78, 54), (86, 34), (74, 12), (50, 4), (24, 8), (6, 28), (0, 56), (-6, 76, 1), (12, 72), (32, 70), (44, 58), (60, 52)])),
   fr([(62, 10), (86, 26), (88, 50), (80, 40)], LAV), L(quad((40, 56), (66, 50), (86, 52)), GOLD, 'f', False, False, 2.6)],
  [L(outline([(-6, 72, 1), (10, 50), (16, 22), (50, 6), (84, 22), (90, 50), (106, 72, 1), (50, 80)])),
   L(outline([(44, 8), (56, 8), (54, 60), (50, 70, 1), (46, 60)]), LAV, 'b', False), L(quad((12, 58), (50, 64), (88, 58)), GOLD, 'f', False, False, 2.6)])

# Arthur "Cancer" Crabbe: pelo verde menta liso en casco con las puntas verde azulado, y dos mechones en pinza de cangrejo
# sobre la cabeza; piel tostada, ojos rosados afilados
TEAL = _c('#3e6a6a')
def _claws(view):
    if view == 'side':
        return [L(quad((48, 6), (40, -10), (24, -12)), TEAL, 'f', False, False, 3.4), L(ell(24, -12, 5, 4), TEAL, 'f'),
                L(quad((58, 6), (64, -10), (76, -14)), TEAL, 'f', False, False, 3.4), L(ell(76, -14, 5, 4), TEAL, 'f')]
    return [L(quad((40, 8), (32, -8), (18, -10)), TEAL, 'f', False, False, 3.4), L(ell(18, -10, 5, 4), TEAL, 'f'),
            L(quad((60, 8), (68, -8), (82, -10)), TEAL, 'f', False, False, 3.4), L(ell(82, -10, 5, 4), TEAL, 'f'),
            L(quad((44, 8), (30, -2), (24, 6)), TEAL, 'f', False, False, 2.4), L(quad((56, 8), (70, -2), (76, 6)), TEAL, 'f', False, False, 2.4)]
C('arthur-cancer-crabbe', 'normal', P('#a8d0c4', '#dca25c', '#b04060', shade='#86a89e'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=[(10, 66), (16, 56), (30, 58), (40, 52), (50, 60), (60, 52), (70, 58), (84, 56), (90, 66)]),
  bowl('front', top=6, side=100) + [L(outline([(6, 88), (18, 88), (16, 104, 1), (8, 100)]), TEAL, 'f'),
                                    L(outline([(94, 88), (82, 88), (84, 104, 1), (92, 100)]), TEAL, 'f')] + _claws('front'),
  bowl('side', top=6, nape=98) + [L(outline([(52, 84), (60, 80), (58, 96, 1)]), TEAL, 'f')] + _claws('side'),
  bowl('back', top=6, nape=100) + [L(outline([(10, 90), (90, 90), (88, 102), (50, 104), (12, 102)]), TEAL, 'f')] + _claws('back'))

# -------------------------------------------------------------------------------------------------------------- 17-24

# Artie Xan: piel morena, afro azul grisáceo en nube de rizos; cejas gruesas azules de enfado, ojos redondos y media sonrisa
C('artie-xan', 'normal', P('#4a6e8a', '#b4733e', '#1e1a1a', shade='#3a5870'),
  F(eyes='round', brows=False, mouth='smile', mouth_y=93, hairline=[(12, 62), (22, 50), (36, 46), (50, 50), (64, 46), (78, 50), (88, 62)]),
  [L(curls(50, 32, (48, 32), 10, 0.2))] + thick_brows(64, 'mid', 4.4, 15, 1.4, 14),
  [L(curls(40, 30, (46, 30), 10, 0.3))] + side_brow(64, 'mid', 4.4, 1.2), [L(curls(50, 40, (50, 38), 10, 0.1))])

# Asif Ecks: piel morena, pelo rubio crema que sube en una llama alta y sale en puntas por los lados de la cara; cadena de
# plata con una media luna en la frente, rayas naranjas en las mejillas y ojos verde agua afilados
SIL, ORG = _c('#d8dcdc'), _c('#e07030')
def _asif_paint():
    out = []
    for s in (-1, 1):
        for i in range(3):
            y = 80 + i * 5
            x = 50 + s * 22
            out.append(L([(x - 3, y), (x + 3, y), (x + 3, y + 3.6), (x - 3, y + 3.6)], ORG, 'f', False, True))
    return out
C('asif-ecks', 'normal', P('#e0dcaa', '#b67139', '#3aa0a0', shade='#b8b080'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, hairline=[(10, 62), (20, 48), (36, 42), (50, 46), (64, 42), (80, 48), (90, 62)]),
  [L(outline([(16, 62), (10, 44), (22, 22), (40, 6), (50, -24, 1), (60, 6), (78, 22), (90, 44), (84, 62), (78, 48), (22, 48)])),
   L(outline([(14, 66), (-2, 84, 1), (12, 80), (6, 94, 1), (18, 84)]), 'mid', 'b'), L(outline([(86, 66), (102, 84, 1), (88, 80), (94, 94, 1), (82, 84)]), 'mid', 'b'),
   L(outline([(54, 0), (60, 6), (78, 22), (88, 42), (78, 36), (62, 20)]), 'shade', 'b', False),
   L(quad((24, 56), (50, 64), (76, 56)), SIL, 'f', False, False, 1.4), L(ell(50, 62, 2.6, 2.6), SIL, 'f')] + _asif_paint(),
  [L(outline([(80, 52), (88, 34), (76, 14), (60, 0), (52, -28, 1), (40, 2), (20, 10), (6, 30), (4, 56), (-6, 74, 1), (16, 70), (8, 88, 1), (30, 76), (44, 60), (60, 54)])),
   L([(88, 60), (62, 58)], SIL, 'f', False, False, 1.4), L([(78, 84), (84, 84), (84, 87.6), (78, 87.6)], ORG, 'f', False, True)],
  [L(outline([(14, 74), (2, 86, 1), (10, 60), (12, 40), (24, 18), (40, 4), (50, -24, 1), (60, 4), (76, 18), (88, 40), (90, 60), (98, 86, 1), (86, 74), (50, 80)])),
   L(outline([(56, 0), (76, 18), (88, 42), (88, 70), (70, 40)]), 'shade', 'b', False)])

# Assumpta Meakin: monja con toca azul marino oscuro que le cae hasta los hombros y una placa blanca que le tapa media
# cara; solo se le ven los labios anaranjados
VEIL, VEIL2, PLATE = _c('#2a2840'), _c('#1e1d2e'), _c('#dcdad2')
C('assumpta-meakin', 'chica', P('#2a2840', '#f2c6a2', '#1e1a1a'),
  F(eyes='none', brows=False, mouth='none', hairline=False),
  [L(outline([(6, 120), (4, 60), (12, 24), (30, 6), (50, 0), (70, 6), (88, 24), (96, 60), (94, 120), (78, 118), (80, 62), (20, 62), (22, 118)]), VEIL),
   L(outline([(50, 2), (70, 8), (88, 26), (95, 60), (93, 118), (80, 116), (82, 60)]), VEIL2, 'b', False),
   L(blob([(20, 44), (50, 36), (80, 44), (82, 78), (68, 90), (50, 92), (32, 90), (18, 78)], 6), PLATE, 'f'),
   L(blob([(44, 98), (50, 96), (56, 98), (50, 101)], 4), LIP, 'f', False), L(blob([(40, 102), (60, 102), (56, 116), (44, 116)], 4), PLATE, 'f')],
  [L(outline([(54, 54), (80, 36), (76, 14), (52, 2), (26, 6), (8, 24), (2, 60), (0, 122), (40, 122), (46, 90), (50, 70)]), VEIL),
   L(blob([(60, 40), (86, 42), (90, 70), (84, 86), (66, 84), (60, 60)], 6), PLATE, 'f'), L(ell(86, 98, 2.6, 1.6), LIP, 'f', False)],
  [L(outline([(4, 122), (4, 60), (12, 24), (30, 6), (50, 0), (70, 6), (88, 24), (96, 60), (96, 122), (50, 124)]), VEIL),
   L(outline([(52, 2), (70, 8), (88, 26), (95, 60), (95, 120), (70, 122), (66, 50)]), VEIL2, 'b', False)])

# Avid Peddler: media melena verde azulada echada a un lado, con las puntas en rizos sobre las orejas; cejas verdes de
# enfado y boca seria
C('avid-peddler', 'normal', P('#4a8074', '#fcdcc0', '#1e1a1a', shade='#38604f'),
  F(eyes='normal', brows='angry', mouth='frown', mouth_y=93, hairline=[(10, 64), (16, 52), (30, 46), (56, 40), (78, 44), (88, 54), (90, 64)]),
  dome('front', top=0, w=46, cy=44, sb=84) +
  [L(curls(14, 88, (10, 9), 5), 'mid', 'b'), L(curls(86, 88, (10, 9), 5), 'mid', 'b'),
   fr([(14, 60), (20, 38), (44, 26), (74, 30), (88, 46), (78, 42), (54, 42), (34, 50), (22, 64, 1)])],
  dome('side', top=0, w=46, cy=44, nape=88, fr=52) + [L(curls(24, 88, (14, 10), 6), 'mid', 'b')],
  dome('back', top=0, w=46, cy=44, nape=86) + [L(curls(20, 88, (12, 9), 5), 'mid', 'b'), L(curls(80, 88, (12, 9), 5), 'mid', 'b'), L(curls(50, 90, (18, 8), 6), 'mid', 'b')])

# Ba Branssen: casco de aviador verde oliva con gafas redondas grises, melena lisa negra hasta los hombros; ojos blancos de
# enfado, dientes apretados y una perilla
OLV, OLV2 = _c('#887d10'), _c('#6a6008')
def _aviator(view):
    if view == 'front':
        return [L(outline([(8, 64), (6, 32), (22, 8), (50, 0), (78, 8), (94, 32), (92, 64), (80, 56), (20, 56)]), OLV, 'f'),
                L(ell(8, 70, 8, 14), OLV, 'f'), L(ell(92, 70, 8, 14), OLV, 'f')] + goggles('front', 40, (130, 120, 110, 255), (50, 46, 52, 255))
    if view == 'side':
        return [L(outline([(84, 54), (88, 32), (76, 10), (50, 0), (24, 6), (6, 26), (2, 56), (20, 64), (44, 60), (60, 54)]), OLV, 'f'),
                L(ell(44, 70, 10, 14), OLV, 'f')] + goggles('side', 40, (130, 120, 110, 255), (50, 46, 52, 255))
    return [L(outline([(6, 66), (6, 32), (22, 8), (50, 0), (78, 8), (94, 32), (94, 66), (50, 60)]), OLV, 'f'),
            L(outline([(52, 2), (78, 10), (93, 34), (93, 64), (70, 40)]), OLV2, 'f', False)] + goggles('back', 40, (130, 120, 110, 255), (50, 46, 52, 255))
C('ba-branssen', 'normal', P('#2e2630', '#e6dac8', '#f6f6f6'),
  F(eyes='sharp', brows=False, mouth='grin', mouth_y=94, hairline=False),
  [L(outline([(8, 112), (6, 60), (94, 60), (92, 112), (80, 112), (80, 70), (20, 70), (20, 112)]))] + _aviator('front') +
  [L([(26, 68), (44, 74)], BLACK, 'f', False, False, 3.0), L([(74, 68), (56, 74)], BLACK, 'f', False, False, 3.0),
   mark([(46, 104), (54, 104), (52, 108), (48, 108)], BLACK)],
  [L(outline([(2, 112), (2, 60), (46, 60), (46, 112)]))] + _aviator('side'),
  [L(outline([(4, 114), (4, 60), (96, 60), (96, 114), (50, 116)]))] + _aviator('back'))

# Balen "Baler" Straw (portero): cara redonda y ancha, pelo verde azulado al cero con una calva naranja en la coronilla;
# cejas gruesas verdes, ojos entornados de enfado, nariz redonda, orejas grandes y los dientes apretados
C('balen-baler-straw', 'corpulento', P('#70a29c', '#f8ba7a', '#1e1a1a'),
  F(eyes='sharp', brows=False, mouth='grin', mouth_y=98, nose=(50, 88, 4), big_ears=3, face_front=face(w=6, chin=108, jaw=4), hairline=False),
  [L(outline([(14, 62), (12, 36), (24, 14), (50, 6), (76, 14), (88, 36), (86, 62), (80, 48), (20, 48)])), L(ell(62, 18, 5, 4), (240, 170, 110, 255), 'f', False)] +
  thick_brows(64, 'shade', 4.4, 15, 1.4, 14),
  [L(outline([(80, 50), (84, 30), (72, 10), (50, 4), (24, 8), (8, 28), (4, 54), (12, 72), (28, 74), (42, 62), (56, 52)])), L(ell(56, 12, 5, 4), (240, 170, 110, 255), 'f', False)] +
  side_brow(64, 'shade', 4.4, 1.2),
  [L(outline([(12, 76), (10, 36), (24, 12), (50, 4), (76, 12), (90, 36), (88, 76), (50, 82)])), L(ell(50, 10, 5, 4), (240, 170, 110, 255), 'f', False)])

# Baron Blackgold: piel tostada, pelo azul marino oscuro ondulado y revuelto; un punto rojo en la frente, ojos gris azulado
# afilados y boca seria
C('baron-blackgold', 'normal', P('#453c54', '#d8a058', '#6a7a94', shade='#342c40'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=hl(6, 62, 44, 54, lean=1, jit=3, seed=41)),
  messy('front', amp=10, n=10, seed=42, lo=66, sweep=0.3) + [L(ell(50, 62, 1.8, 2.0), RED, 'f', False)],
  messy('side', amp=10, n=10, seed=42, nape=88, sweep=0.3), messy('back', amp=10, n=10, seed=42, nape=90, sweep=0.3))

# Bear Zurka (portero): máscara de madera de tótem con una dentadura enorme y una corona de pinchos verde menta; un ojo
# entornado y el otro con un brillo amarillo
WOOD, WOOD2, MNT = _c('#b4743e'), _c('#8a5430'), _c('#c8dcc4')
def _totem(view):
    if view == 'front':
        out = [L(outline([(10, 46), (2, 30, 1), (16, 30), (14, 10, 1), (30, 18), (36, -4, 1), (50, 10), (64, -4, 1), (70, 18), (86, 10, 1), (84, 30), (98, 30, 1),
                          (90, 46), (50, 40)]), MNT),
               L(outline([(16, 40), (84, 40), (88, 104), (12, 104)]), WOOD, 'f'),
               L(outline([(24, 60), (76, 60), (76, 98), (24, 98)]), WHITE, 'f', False, True)]
        for x in (37, 50, 63):
            out.append(L([(x, 60), (x, 98)], OUTC, 'f', False, False, 1.2))
        out += [L([(24, 79), (76, 79)], OUTC, 'f', False, False, 1.2),
                L([(28, 50), (42, 52)], BLACK, 'f', False, False, 3.0), L(ell(64, 50, 4, 3.4), BLACK, 'f', False), L(ell(64, 50, 1.6, 1.6), (240, 210, 60, 255), 'f', False),
                L(ell(12, 74, 3, 6), WOOD2, 'f'), L(ell(88, 74, 3, 6), WOOD2, 'f')]
        return out
    if view == 'side':
        return [L(outline([(10, 50), (0, 34, 1), (14, 30), (14, 10, 1), (30, 16), (40, -4, 1), (54, 10), (66, -4, 1), (72, 18), (88, 14, 1), (86, 34), (96, 38, 1), (88, 50), (50, 44)]), MNT),
                L(outline([(10, 44), (88, 42), (92, 104), (16, 104)]), WOOD, 'f'), L(outline([(72, 60), (92, 60), (92, 98), (72, 98)]), WHITE, 'f', False, True),
                L([(82, 60), (82, 98)], OUTC, 'f', False, False, 1.2), L([(72, 79), (92, 79)], OUTC, 'f', False, False, 1.2), L(ell(82, 50, 3, 3), BLACK, 'f', False)]
    return [L(outline([(10, 46), (2, 30, 1), (16, 30), (14, 10, 1), (30, 18), (36, -4, 1), (50, 10), (64, -4, 1), (70, 18), (86, 10, 1), (84, 30), (98, 30, 1), (90, 46), (50, 40)]), MNT),
            L(outline([(14, 40), (86, 40), (88, 104), (12, 104)]), WOOD2, 'f')]
C('bear-zurka', 'corpulento', P('#c8dcc4', '#b4743e', '#1e1a1a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False), _totem('front'), _totem('side'), _totem('back'))

# -------------------------------------------------------------------------------------------------------------- 25-32

# Becks Binder: melena naranja larga y lisa con raya al medio y las puntas verde azulado que se enroscan hacia fuera;
# ojos redondos azul turquesa enormes y la lengua fuera
TQ = _c('#3a8a8e')
C('becks-binder', 'chica', P('#e8902a', '#fde0c4', '#3ab0c0', shade='#b0601c', deep='#8a4a14'),
  F(eyes='big', brows=False, mouth='none', hairline=[(12, 66), (18, 46), (36, 36), (50, 44), (64, 36), (82, 46), (88, 66)]),
  dome('front', top=0, w=46, cy=44, long=108, flare=2) +
  [fr([(16, 62), (22, 38), (44, 28), (50, 40), (56, 28), (78, 38), (84, 62), (74, 46), (58, 38), (50, 48), (42, 38), (26, 46)]),
   L(outline([(6, 100), (14, 104), (2, 118), (-8, 112, 1), (2, 112)]), TQ, 'f'), L(outline([(94, 100), (86, 104), (98, 118), (108, 112, 1), (98, 112)]), TQ, 'f'),
   L(ell(50, 96, 3.2, 3.4), PINK, 'f'), L([(44, 93), (56, 93)], OUTC, 'f', False, False, 1.2)],
  dome('side', top=0, w=46, cy=44, long=108, fr=56) + [L(outline([(10, 100), (2, 116), (-8, 114, 1), (4, 104)]), TQ, 'f'), L(ell(88, 96, 2, 3), PINK, 'f')],
  dome('back', top=0, w=46, cy=44, long=108, ends=4) + [L(outline([(4, 100), (96, 100), (100, 112), (50, 114), (0, 112)]), TQ, 'f')])

# Bella Baker: pelo rosa con dos trenzas largas a los lados, un remolino en la coronilla y unas gafas de corazón rosas en la
# frente; ojos grandes azul verdoso y sonrisa
HRT, HRT2 = _c('#f08aa8'), _c('#d0406a')
def _heart(cx, cy, s=1.0):
    return blob([(cx, cy + 6 * s), (cx - 9 * s, cy - 1 * s), (cx - 7 * s, cy - 7 * s), (cx - 2 * s, cy - 7 * s), (cx, cy - 4 * s), (cx + 2 * s, cy - 7 * s),
                 (cx + 7 * s, cy - 7 * s), (cx + 9 * s, cy - 1 * s)], 6)
def _braid(x, y0, y1, view='front'):
    out = []
    y = y0
    while y < y1:
        out.append(L(ell(x, y, 6.4, 5.2), 'mid', 'b'))
        y += 7.5
    out.append(L(outline([(x - 4, y1), (x + 4, y1), (x + 2, y1 + 8, 1), (x - 2, y1 + 8, 1)]), 'mid', 'b'))
    return out
C('bella-baker', 'chica', P('#dc968e', '#fce8d8', '#3a8a9a', shade='#b06e64', deep='#8a4c46'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=[(12, 64), (18, 50), (34, 46), (50, 48), (66, 46), (82, 50), (88, 64)]),
  dome('front', top=2, w=46, cy=44, sb=72) + _braid(10, 70, 108) + _braid(90, 70, 108) +
  [L(quad((48, 4), (44, -10), (54, -12)), 'mid', 'f', False, False, 2.6),
   L(_heart(35, 46, 1.5), HRT2, 'f'), L(_heart(35, 46, 1.15), HRT, 'f', False), L(_heart(65, 46, 1.5), HRT2, 'f'), L(_heart(65, 46, 1.15), HRT, 'f', False),
   L([(46, 42), (54, 42)], HRT2, 'f', False, False, 2.0)],
  dome('side', top=2, w=46, cy=44, nape=86, fr=48) + _braid(28, 78, 112) + [L(quad((48, 4), (44, -10), (54, -12)), 'mid', 'f', False, False, 2.6),
                                                                              L(_heart(84, 44, 0.8), HRT, 'f')],
  dome('back', top=2, w=46, cy=44, nape=86) + _braid(14, 76, 110) + _braid(86, 76, 110) + [L(quad((48, 4), (44, -10), (54, -12)), 'mid', 'f', False, False, 2.6)])

# Ben Feuer: adulto grandullón de cara enorme con papada, pelo gris lavanda ondulado y revuelto; ojitos preocupados con las
# cejas levantadas, nariz pequeña y boca torcida
C('ben-feuer', 'corpulento', P('#7a728c', '#e4ccae', '#1e1a1a', shade='#5e5870'),
  F(eyes='dot', brows=True, mouth='frown', mouth_y=100, nose=(50, 88, 3.0), eye_y=74, eye_sep=10,
    face_front=blob([(12, 52), (50, 42), (88, 52), (98, 84), (92, 108), (72, 118), (50, 120), (28, 118), (8, 108), (2, 84)]),
    hairline=hl(6, 60, 44, 52, jit=3, seed=51)),
  messy('front', amp=8, n=10, seed=52, lo=64), messy('side', amp=8, n=10, seed=52, nape=84), messy('back', amp=8, n=10, seed=52, nape=86))

# Bern Ballast (portero): gorra verde con una pluma blanca y roja en un lado, pelo rubio crema con el flequillo largo que le
# tapa un ojo; ojo rojo y sonrisa
GRN, FTH = _c('#5a9242'), _c('#f4ece0')
def _bcap(view):
    if view == 'front':
        return [L(outline([(8, 52), (10, 26), (30, 6), (60, 2), (84, 12), (94, 34), (92, 52), (50, 44)]), GRN, 'f'),
                L(outline([(78, 44), (96, 2, 1), (92, 30)]), FTH, 'f'), L(outline([(90, 14), (96, 2, 1), (94, 18)]), RED, 'f', False)]
    if view == 'side':
        return [L(outline([(6, 56), (6, 30), (24, 8), (54, 2), (80, 10), (92, 30), (90, 50), (50, 48)]), GRN, 'f'),
                L(outline([(30, 40), (10, -4, 1), (22, 30)]), FTH, 'f'), L(outline([(14, 4), (10, -4, 1), (18, 8)]), RED, 'f', False)]
    return [L(outline([(6, 60), (8, 28), (26, 8), (50, 2), (74, 8), (92, 28), (94, 60), (50, 54)]), GRN, 'f'),
            L(outline([(20, 50), (2, 6, 1), (10, 40)]), FTH, 'f')]
C('bern-ballast', 'normal', P('#e2daac', '#fbefcc', '#b02020', shade='#c4b888'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=93, hairline=[(8, 66), (16, 54), (50, 50), (84, 54), (92, 66)]),
  dome('front', top=4, w=46, cy=44, sb=76) + _bcap('front') +
  [fr([(14, 50), (40, 46), (56, 52), (54, 70), (48, 92, 1), (40, 76), (30, 90, 1), (24, 72), (16, 78)]), strand([(32, 52), (36, 80)], 'shade', 'f', 1.0)],
  dome('side', top=4, w=46, cy=44, nape=86, fr=56) + _bcap('side'), dome('back', top=4, w=46, cy=44, nape=86) + _bcap('back'))

# Bernadette Stoker: piel tostada, pelo castaño grisáceo con un mechón enorme en forma de hoz que le rodea la cara desde
# arriba hasta debajo de la barbilla y vuelve a subir por el otro lado; ojos marrones entornados
C('bernadette-stoker', 'chica', P('#7a5e48', '#eeb074', '#7a4a2a', shade='#5e4636', light='#9a8e82'),
  F(eyes='sharp', brows=True, mouth='frown', mouth_y=93, hairline=[(10, 64), (18, 50), (40, 40), (62, 38), (80, 44), (90, 60)]),
  dome('front', top=0, w=46, cy=44, sb=78) +
  [fr([(60, 24), (86, 40), (94, 66), (86, 98), (60, 118), (24, 122), (-6, 104), (-12, 66, 1), (4, 96), (24, 110), (54, 106), (74, 90), (80, 64), (70, 42)]),
   strand([(70, 40), (84, 70), (70, 100), (36, 114)], 'shade', 'f', 1.2)] + lashes(),
  dome('side', top=0, w=46, cy=44, nape=86, fr=50) + [fr([(66, 26), (90, 46), (96, 80), (84, 108), (62, 118), (70, 100), (82, 76), (78, 50)])] + lash_side(),
  dome('back', top=0, w=46, cy=44, nape=86) + [L(outline([(80, 40), (98, 70), (92, 104), (66, 120), (78, 98), (86, 70)]))])

# Bernie Ellement: piel morena, pelo corto rizado rojo oscuro con llamas amarillas por delante; ojos ámbar afilados y sonrisa
YL2, RDK = _c('#edd852'), _c('#901a04')
C('bernie-ellement', 'normal', P('#901a04', '#b4753c', '#d0a020', shade='#6a1202'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=[(12, 62), (20, 48), (36, 44), (50, 48), (64, 44), (80, 48), (88, 62)]),
  dome('front', top=4, w=46, cy=44, n=12, amp=5, soft=True, sb=64, seed=61) +
  [L(outline([(20, 52), (26, 30, 1), (32, 44), (40, 22, 1), (48, 40), (54, 20, 1), (60, 40), (68, 26, 1), (74, 44), (80, 34, 1), (82, 52), (50, 50)]), YL2, 'b', False)],
  dome('side', top=4, w=46, cy=44, n=12, amp=5, soft=True, nape=82, fr=46, seed=61) +
  [L(outline([(60, 50), (66, 30, 1), (72, 42), (80, 24, 1), (84, 40), (90, 34, 1), (90, 50)]), YL2, 'b', False)],
  dome('back', top=4, w=46, cy=44, n=12, amp=5, soft=True, nape=82, seed=61))

# Bernina Nightoil: pelo castaño rubio ondulado recogido hacia atrás con dos rollos abultados sobre las orejas; gafas
# redondas finas, ojos verdes grandes y sonrisa
C('bernina-nightoil', 'chica', P('#d4be92', '#fbe8ba', '#4a8a2a', shade='#a28668', deep='#806648'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=94, hairline=[(14, 62), (20, 46), (36, 40), (50, 44), (64, 40), (80, 46), (86, 62)]),
  dome('front', top=2, w=44, cy=44, sb=70) + [L(curls(12, 76, (11, 13), 5, 0.3), 'mid', 'b'), L(curls(88, 76, (11, 13), 5, 0.6), 'mid', 'b'),
                                               strand([(36, 14), (30, 40)], 'shade', 'b', 1.0), strand([(64, 14), (70, 40)], 'shade', 'b', 1.0)] +
  round_glasses('front', (150, 120, 90, 255), r=7.5, w=1.6),
  dome('side', top=2, w=44, cy=44, nape=80, fr=46) + [L(curls(30, 76, (16, 14), 6), 'mid', 'b')] + round_glasses('side', (150, 120, 90, 255), w=1.6),
  dome('back', top=2, w=44, cy=44, nape=80) + [L(curls(16, 78, (12, 13), 5), 'mid', 'b'), L(curls(84, 78, (12, 13), 5), 'mid', 'b'), L(curls(50, 82, (20, 10), 6), 'mid', 'b')])

# Berthel Stagg: tupé rubio altísimo en punta hacia arriba con los lados cortos; antifaz rojo en V que le baja por la nariz,
# un aro en la oreja y ojos de enfado
C('berthel-stagg', 'normal', P('#e0bc08', '#f6c086', '#1e1a1a', shade='#a46e0e'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=95, hairline=[(12, 62), (20, 48), (50, 46), (80, 48), (88, 62)]),
  [L(outline([(16, 62), (12, 40), (8, -20, 1), (28, -12), (50, -26, 1), (72, -12), (92, -20, 1), (88, 40), (84, 62), (80, 48), (20, 48)])),
   L(outline([(56, -20), (72, -12), (92, -20), (88, 40), (82, 56), (74, 10)]), 'shade', 'b', False),
   strand([(30, -6), (34, 30)], 'shade', 'b', 1.0), strand([(50, -18), (50, 30)], 'shade', 'b', 1.0),
   L(outline([(14, 70), (30, 64), (50, 70), (70, 64), (86, 70), (80, 82), (58, 82), (50, 94, 1), (42, 82), (20, 82)]), RED, 'f')] +
  sharp_eyes(_c('#1e1a1a'), 75) + [ring(85, 82, 2.4, 2.6, (200, 200, 200, 255), 1.4)],
  [L(outline([(82, 54), (86, 30), (88, -20, 1), (70, -12), (52, -26, 1), (34, -12), (14, -18, 1), (8, 30), (6, 56), (20, 70), (40, 66), (56, 56)])),
   L(outline([(60, 66), (90, 66), (90, 82), (70, 82)]), RED, 'f')] + sharp_eye_side(_c('#1e1a1a'), 75) + [ring(46, 82, 2.0, 2.4, (200, 200, 200, 255), 1.4)],
  [L(outline([(12, 70), (10, 40), (8, -20, 1), (28, -12), (50, -26, 1), (72, -12), (92, -20, 1), (90, 40), (88, 70), (50, 76)])),
   L(outline([(56, -20), (72, -12), (92, -20), (90, 40), (86, 66), (74, 10)]), 'shade', 'b', False),
   L(quad((10, 72), (50, 66), (90, 72)), RED, 'f', False, False, 4)])

# -------------------------------------------------------------------------------------------------------------- 33-40

# Bill "Duckie" Mallard: gorro de ornitorrinco beige con dos ojos negros encima, un pico enorme morado oscuro que le tapa
# media cara y unas aletas rosadas a los lados; boca seria
BEI, BILL, FRL = _c('#d2b882'), _c('#4b3e4a'), _c('#c88878')
def _platypus(view):
    if view == 'front':
        return [L(outline([(8, 66), (0, 58, 1), (4, 50), (-6, 44, 1), (10, 40), (14, 60)]), FRL, 'f'),
                L(outline([(92, 66), (100, 58, 1), (96, 50), (106, 44, 1), (90, 40), (86, 60)]), FRL, 'f'),
                L(outline([(8, 60), (8, 30), (24, 8), (50, 0), (76, 8), (92, 30), (92, 60), (50, 56)]), BEI, 'f'),
                L(blob([(10, 52), (50, 40), (90, 52), (94, 66), (74, 76), (50, 74), (26, 76), (6, 66)], 6), BILL, 'f'),
                L(ell(32, 22, 4.4, 4.4), WHITE, 'f'), L(ell(32, 22, 2.6, 2.6), BLACK, 'f', False),
                L(ell(68, 22, 4.4, 4.4), WHITE, 'f'), L(ell(68, 22, 2.6, 2.6), BLACK, 'f', False)]
    if view == 'side':
        return [L(outline([(40, 70), (30, 62, 1), (34, 54), (24, 48, 1), (42, 46), (46, 64)]), FRL, 'f'),
                L(outline([(80, 56), (88, 30), (74, 8), (50, 0), (24, 6), (6, 28), (4, 60), (30, 66), (60, 58)]), BEI, 'f'),
                L(blob([(60, 46), (98, 44), (110, 56), (100, 70), (64, 70)], 6), BILL, 'f'),
                L(ell(70, 22, 4.4, 4.4), WHITE, 'f'), L(ell(72, 22, 2.6, 2.6), BLACK, 'f', False)]
    return [L(outline([(8, 70), (-6, 60, 1), (8, 52), (92, 52), (106, 60, 1), (92, 70)]), FRL, 'f'),
            L(outline([(8, 68), (8, 30), (24, 8), (50, 0), (76, 8), (92, 30), (92, 68), (50, 64)]), BEI, 'f')]
C('bill-duckie-mallard', 'normal', P('#d2b882', '#fbc27e', '#1e1a1a'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=92, hairline=False), _platypus('front'), _platypus('side'), _platypus('back'))

# Bishop Carver (portero): pañuelo verde oliva en la cabeza, melena castaña desgreñada hasta los hombros, cara alargada con
# una nariz naranja enorme, ojos afilados y labios gruesos
BND, NOS = _c('#4f5f32'), _c('#e8964a')
def _bandana(view):
    if view == 'front':
        return [L(outline([(10, 60), (10, 28), (28, 8), (50, 2), (72, 8), (90, 28), (90, 60), (50, 54)]), BND, 'f'),
                L(outline([(56, 4), (74, 10), (88, 30), (88, 56), (76, 30)]), _c('#3a4a24'), 'f', False)]
    if view == 'side':
        return [L(outline([(84, 54), (88, 30), (74, 8), (50, 2), (24, 6), (6, 26), (2, 54), (-8, 66, 1), (10, 62), (40, 58), (60, 54)]), BND, 'f')]
    return [L(outline([(8, 62), (8, 28), (26, 8), (50, 2), (74, 8), (92, 28), (92, 62), (50, 58)]), BND, 'f'),
            L(outline([(46, 58), (40, 76, 1), (50, 64), (60, 76, 1), (54, 58)]), BND, 'f')]
C('bishop-carver', 'delgado', P('#765a2c', '#e0a054', '#1e1a1a', shade='#54401c'),
  F(eyes='sharp', brows='angry', mouth='lips', mouth_y=102, mouth_w=8, face_front=face(chin=112), face_side=face_side(chin=8, nose=8), hairline=False),
  [L(outline([(2, 104, 1), (10, 90), (-2, 82, 1), (12, 70), (12, 54), (88, 54), (88, 70), (102, 82, 1), (90, 90), (98, 104, 1), (80, 98), (76, 70), (24, 70), (20, 98)]))] +
  _bandana('front') + [L(outline([(46, 72), (54, 72), (60, 96, 1), (40, 96, 1)]), NOS, 'f', True, True)],
  [L(outline([(54, 60), (40, 100, 1), (24, 92), (10, 108, 1), (4, 84), (2, 60)]))] + _bandana('side') +
  [L(outline([(84, 72), (100, 94, 1), (86, 96)]), NOS, 'f', True, True)],
  [L(outline([(4, 106, 1), (8, 60), (92, 60), (96, 106, 1), (76, 100), (64, 108, 1), (50, 98), (36, 108, 1), (24, 100)]))] + _bandana('back'))

# Bjorn Heel-Villen: pelo castaño oscuro con franjas naranjas peinado hacia atrás en un moño con mechones sueltos que
# cuelgan; pintura roja de guerra alrededor de los ojos amarillos y rayas rojas en las mejillas; dientes apretados
STR = _c('#b0602a')
C('bjorn-heel-villen', 'normal', P('#46200a', '#c8976e', '#e0c020', shade='#2e1606'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=95, hairline=[(12, 64), (20, 50), (50, 44), (80, 50), (88, 64)]),
  dome('front', top=4, w=44, cy=44, sb=64) +
  [L(quad((50, -6), (60, -14), (66, -4)), 'mid', 'f', False, False, 3.0), L(ell(50, 2, 7, 6), 'mid', 'f'),
   strand([(36, 8), (34, 46)], STR, 'b', 3.4), strand([(50, 4), (50, 46)], STR, 'b', 3.4), strand([(64, 8), (66, 46)], STR, 'b', 3.4),
   strand([(14, 60), (10, 80), (14, 96)], 'mid', 'f', 2.6), strand([(86, 60), (90, 80), (86, 96)], 'mid', 'f', 2.6),
   L(blob([(18, 70), (34, 64), (46, 70), (50, 76), (54, 70), (66, 64), (82, 70), (80, 82), (64, 84), (50, 80), (36, 84), (20, 82)], 4), RED, 'f', False)] +
  sharp_eyes(_c('#e0c020'), 75) +
  [L([(24, 86), (30, 92)], RED, 'f', False, False, 1.6), L([(28, 84), (34, 90)], RED, 'f', False, False, 1.6),
   L([(76, 86), (70, 92)], RED, 'f', False, False, 1.6), L([(72, 84), (66, 90)], RED, 'f', False, False, 1.6)],
  dome('side', top=4, w=44, cy=44, nape=80, fr=46) +
  [L(ell(22, 10, 8, 7), 'mid', 'f'), L(quad((18, 4), (10, -8), (20, -12)), 'mid', 'f', False, False, 3.0),
   strand([(30, 10), (10, 40)], STR, 'b', 3.4), strand([(50, 6), (30, 46)], STR, 'b', 3.4), strand([(52, 62), (48, 96)], 'mid', 'f', 2.6),
   L(blob([(68, 68), (90, 68), (90, 82), (70, 82)], 4), RED, 'f', False)] + sharp_eye_side(_c('#e0c020'), 75),
  dome('back', top=4, w=44, cy=44, nape=80) +
  [L(ell(50, 6, 8, 7), 'mid', 'f'), strand([(30, 10), (24, 70)], STR, 'b', 3.4), strand([(50, 10), (50, 76)], STR, 'b', 3.4), strand([(70, 10), (76, 70)], STR, 'b', 3.4),
   strand([(18, 70), (14, 96)], 'mid', 'f', 2.6), strand([(82, 70), (86, 96)], 'mid', 'f', 2.6)])

# Blagun White: adulto con un pañuelo verde azulado atado a la cabeza cuya cola le cae por un lado; patillas rojas trenzadas
# que le bajan por las mejillas, ojos cerrados apretados y una nariz naranja grande
TB, TB2, RB = _c('#6fa29c'), _c('#4e7e7a'), _c('#913829')
def _tied(view):
    if view == 'front':
        return [L(outline([(12, 58), (12, 30), (28, 10), (50, 4), (72, 10), (88, 30), (88, 58), (50, 52)]), TB, 'f'),
                L(outline([(16, 56), (4, 70), (-4, 104, 1), (10, 96), (8, 116, 1), (20, 84), (26, 60)]), TB2, 'f')]
    if view == 'side':
        return [L(outline([(84, 54), (88, 30), (74, 10), (50, 4), (24, 8), (8, 28), (6, 56), (40, 56), (62, 52)]), TB, 'f'),
                L(outline([(10, 50), (0, 70), (-6, 100, 1), (8, 90), (4, 112, 1), (18, 76), (20, 56)]), TB2, 'f')]
    return [L(outline([(10, 62), (10, 30), (28, 10), (50, 4), (72, 10), (90, 30), (90, 62), (50, 58)]), TB, 'f'),
            L(outline([(16, 58), (6, 74), (0, 106, 1), (14, 96), (12, 116, 1), (24, 80), (28, 60)]), TB2, 'f')]
def _side_braid(x):
    return [L(ell(x, y, 3.8, 4.4), RB, 'f') for y in (74, 82, 90, 98)]
C('blagun-white', 'delgado', P('#6fa29c', '#cf966a', '#1e1a1a'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=98, face_front=face(chin=108), face_side=face_side(chin=6, nose=6), hairline=False),
  _tied('front') + _side_braid(21) + _side_braid(79) +
  [L([(28, 72), (40, 76), (28, 79)], BLACK, 'f', False, False, 2.4), L([(72, 72), (60, 76), (72, 79)], BLACK, 'f', False, False, 2.4)] + nose_tri(90, 6, 16, NOS),
  _tied('side') + _side_braid(52) + [L([(84, 72), (76, 76), (84, 79)], BLACK, 'f', False, False, 2.4),
                                     L(outline([(84, 74), (100, 92, 1), (86, 94)]), NOS, 'f', True, True)],
  _tied('back'))

# Blazer Firefoot (portero): pelo en llamas rojas con el interior naranja que sube y sale hacia los lados, marcas rojas sobre
# los ojos azules, sonrisa y un pañuelo granate al cuello
FL1, FL2, SCF = _c('#c71304'), _c('#f3922b'), _c('#711218')
C('blazer-firefoot', 'normal', P('#c71304', '#ce986e', '#3aa0d8', shade='#9a1006'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=93, hairline=[(10, 64), (18, 52), (30, 58), (40, 50), (50, 58), (60, 50), (70, 58), (82, 52), (90, 64)]),
  [L(outline([(16, 66), (-8, 50, 1), (8, 36), (-4, 8, 1), (20, 18), (22, -14, 1), (40, 6), (52, -26, 1), (62, 6), (82, -12, 1), (80, 18), (104, 10, 1), (92, 38),
              (108, 52, 1), (84, 66), (80, 52), (20, 52)])),
   L(outline([(20, 52), (10, 34, 1), (26, 30), (30, 8, 1), (42, 22), (52, -8, 1), (60, 22), (76, 6, 1), (74, 32), (90, 30, 1), (80, 52)]), FL2, 'b', False),
   L(outline([(24, 64), (38, 62), (36, 66)]), RED, 'f', False), L(outline([(76, 64), (62, 62), (64, 66)]), RED, 'f', False),
   L(outline([(16, 102), (50, 110), (84, 102), (90, 112), (60, 118), (50, 124, 1), (40, 118), (10, 112)]), SCF, 'f')],
  [L(outline([(82, 56), (98, 40, 1), (86, 30), (100, 6, 1), (76, 12), (74, -16, 1), (56, 4), (40, -24, 1), (34, 6), (12, -6, 1), (14, 22), (-8, 30, 1), (6, 48), (-6, 66, 1),
              (16, 66), (36, 66), (52, 58)])),
   L(outline([(60, 54), (80, 34, 1), (64, 26), (66, 6, 1), (50, 18), (40, -4, 1), (34, 24), (16, 22, 1), (24, 42), (40, 52)]), FL2, 'b', False),
   L(outline([(40, 100), (86, 102), (88, 112), (40, 112)]), SCF, 'f')],
  [L(outline([(14, 74), (-8, 54, 1), (8, 40), (-4, 10, 1), (20, 18), (22, -14, 1), (40, 6), (52, -26, 1), (62, 6), (82, -12, 1), (80, 18), (104, 10, 1), (92, 40),
              (108, 54, 1), (86, 74), (50, 80)])),
   L(outline([(16, 102), (50, 108), (84, 102), (86, 112), (50, 116), (14, 112)]), SCF, 'f')])

# Blowie Armstraw: piel tostada, pelo gris pizarra corto y repeinado con un pico en la frente; cejas gruesas de enfado, ojos
# grandes marrones y cara alargada seria
C('blowie-armstraw', 'normal', P('#384044', '#ce9468', '#5a4628', shade='#2a3034'),
  F(eyes='normal', brows='angry', mouth='line', mouth_y=97, face_front=face(chin=106), face_side=face_side(chin=4),
    hairline=[(12, 62), (18, 46), (40, 42), (50, 52), (60, 42), (82, 46), (88, 62)]),
  dome('front', top=6, w=44, cy=44, sb=62) + [strand([(50, 10), (50, 44)], 'shade', 'b', 1.0)],
  dome('side', top=6, w=44, cy=44, nape=80, fr=46), dome('back', top=6, w=44, cy=44, nape=80))

# Bob "Bob Job" Jobbe: piel tostada, pelo azul marino muy abultado en mechones ondulados revueltos; ojos entornados y boca
# pequeña seria
C('bob-bob-job-jobbe', 'normal', P('#32475a', '#c99446', '#1e1a1a', shade='#26343f'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=hl(6, 62, 44, 54, jit=3, seed=71)),
  messy('front', amp=12, n=10, seed=72, rx=52, ry=42, lo=66), messy('side', amp=12, n=10, seed=72, rx=50, ry=42, nape=88),
  messy('back', amp=12, n=10, seed=72, rx=52, ry=42, nape=90))

# Bobby Peeler: gorro de lana azul calado hasta la nariz que le tapa los ojos, con mechones negros que le salen en curva por
# las mejillas; nariz pequeña y sonrisa
BNT, BNT2 = _c('#2f557e'), _c('#24425f')
def _bobby(view):
    if view == 'front':
        return [L(outline([(6, 82), (4, 40), (16, 14), (50, 2), (84, 14), (96, 40), (94, 82), (50, 84)]), BNT, 'f'),
                L(outline([(5, 70), (50, 72), (95, 70), (94, 84), (50, 86), (6, 84)]), BNT2, 'f', False, True),
                L(outline([(56, 4), (84, 16), (95, 42), (94, 68), (82, 40)]), BNT2, 'f', False)]
    if view == 'side':
        return [L(outline([(92, 84), (96, 40), (82, 12), (50, 2), (20, 8), (4, 32), (0, 70), (8, 84), (50, 82)]), BNT, 'f'),
                L(outline([(0, 70), (96, 72), (94, 86), (4, 84)]), BNT2, 'f', False, True)]
    return [L(outline([(6, 84), (4, 40), (16, 14), (50, 2), (84, 14), (96, 40), (94, 84), (50, 86)]), BNT, 'f'),
            L(outline([(5, 72), (95, 72), (94, 86), (6, 86)]), BNT2, 'f', False, True)]
C('bobby-peeler', 'normal', P('#18181a', '#f2bc84', '#1e1a1a'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=96, nose=(50, 89, 2.4), hairline=False),
  _bobby('front') + [L(outline([(10, 80), (26, 84), (38, 100), (30, 104, 1), (20, 94), (10, 100, 1)]), 'mid', 'f'),
                     L(outline([(90, 80), (74, 84), (62, 100), (70, 104, 1), (80, 94), (90, 100, 1)]), 'mid', 'f')],
  [L(outline([(52, 82), (66, 86), (72, 98, 1), (60, 94)]), 'mid', 'f')] + _bobby('side'),
  [L(outline([(10, 84), (90, 84), (88, 96), (50, 98), (12, 96)]), 'mid', 'b')] + _bobby('back'))

# -------------------------------------------------------------------------------------------------------------- 41-48

# Bombasta Flambo Flamboyanzi: piel oscura, una gran mata de pelo negro echada a un lado y atrás, un tocado de plumas rojas
# con un broche dorado y morado; sombra de ojos morada, pendiente dorado y sonrisa
PUR = _c('#8a5ab0')
C('bombasta-flambo-flamboyanzi', 'chica', P('#3e3a36', '#8c5c34', '#3a6a3a', shade='#2c2826'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=93, hairline=[(12, 64), (20, 50), (40, 44), (60, 40), (80, 46), (88, 62)]),
  [L(outline([(12, 70), (8, 40), (24, 14), (50, 4), (80, 8), (98, 36), (102, 84), (92, 112, 1), (86, 84), (82, 58), (20, 56)])),
   L(outline([(60, 6), (86, 14), (100, 44), (100, 90), (90, 70), (82, 36)]), 'shade', 'b', False),
   fr([(8, 56), (-4, 34, 1), (8, 24), (0, 4, 1), (22, 10), (28, -2, 1), (40, 12), (46, 28), (34, 46)], RED),
   L(ell(36, 34, 7.5, 7.5), GOLD, 'f'), L(ell(36, 34, 4.4, 4.4), PUR, 'f', False),
   L(quad((26, 68), (36, 64), (44, 68)), PUR, 'f', False, False, 2.4), L(quad((56, 68), (64, 64), (74, 68)), PUR, 'f', False, False, 2.4),
   L(outline([(17, 80, 1), (20, 80, 1), (20, 92, 1), (17, 92, 1)]), GOLD, 'f')] + lashes(),
  [L(outline([(80, 52), (86, 30), (74, 10), (50, 2), (24, 6), (4, 30), (-2, 70), (2, 108, 1), (16, 96), (30, 80), (44, 62), (62, 54)])),
   fr([(70, 42), (66, 18, 1), (80, 16), (80, 0, 1), (94, 14), (92, 36)], RED), L(ell(82, 30, 5.5, 5.5), GOLD, 'f')] + lash_side(),
  [L(outline([(6, 90), (0, 50), (14, 16), (50, 2), (86, 16), (100, 50), (100, 100), (88, 116, 1), (60, 104), (30, 104), (10, 112, 1)])),
   L(outline([(56, 4), (86, 16), (100, 52), (98, 100), (80, 70)]), 'shade', 'b', False), fr([(4, 50), (-8, 28, 1), (6, 20), (2, 0, 1), (22, 12)], RED)])

# Boo Spector: piel morena, pelo verde oscuro peinado hacia atrás en una cresta estrecha y unas patillas de pinchos sobre
# las orejas; cara larga, ojos apretados, cejas gruesas, nariz grande y la boca abierta de lado
C('boo-spector', 'delgado', P('#22382c', '#b4723c', '#1e1a1a', shade='#18281e'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=100, face_front=face(chin=110), face_side=face_side(chin=8, nose=6),
    hairline=[(24, 56), (32, 44), (50, 40), (68, 44), (76, 56)]),
  [L(outline([(28, 54), (26, 22), (38, 6), (54, 2), (70, 12), (74, 54), (50, 48)])),
   L(outline([(14, 70), (0, 84, 1), (14, 80), (8, 94, 1), (20, 84), (22, 68)])), L(outline([(86, 70), (100, 84, 1), (86, 80), (92, 94, 1), (80, 84), (78, 68)]))] +
  thick_brows(64, 'mid', 4.0, 15, 1.4, 14) +
  [L([(28, 76), (42, 76)], BLACK, 'f', False, False, 2.4), L([(58, 76), (72, 76)], BLACK, 'f', False, False, 2.4)] + nose_tri(90, 5, 14),
  [L(outline([(78, 46), (84, 26), (70, 6), (46, 2), (24, 8), (12, 24), (10, 40), (30, 50), (54, 46)])),
   L(outline([(40, 62), (30, 76, 1), (44, 74), (40, 88, 1), (52, 78), (54, 64)]))] + side_brow(64, 'mid', 4.0, 1.2) +
  [L([(76, 76), (86, 76)], BLACK, 'f', False, False, 2.4), L(outline([(84, 76), (98, 92, 1), (86, 94)]), 'skin', 'f', True, True)],
  [L(outline([(24, 70), (24, 24), (36, 6), (50, 2), (64, 6), (76, 24), (76, 70), (50, 76)]))])

# Brava Hardy: pelo rubio amarillo corto y revuelto con una cinta azul marino con cruces blancas; cejas gordas amarillas,
# ojos grandes azul grisáceo, pecas y la boca entreabierta
NV = _c('#2c3450')
def _xband(view):
    if view == 'front':
        out = [band('front', 38, 11, NV)]
        for x in (24, 37, 50, 63, 76):
            y = 44 - 4 * (1 - abs(x - 50) / 26)
            out += [L([(x - 3, y - 3), (x + 3, y + 3)], WHITE, 'f', False, False, 1.4), L([(x - 3, y + 3), (x + 3, y - 3)], WHITE, 'f', False, False, 1.4)]
        return out
    return [band(view, 38, 11, NV)]
C('brava-hardy', 'chica', P('#e0c010', '#f4c092', '#6a8aa0', shade='#a07814'),
  F(eyes='big', brows=False, mouth='grin', mouth_y=95, hairline=hl(6, 62, 48, 58, jit=2, seed=81)),
  messy('front', amp=9, n=12, seed=82, lo=70) + _xband('front') + thick_brows(63, 'mid', 3.6, 15, 0.6, 13) + freckles(86, 24),
  messy('side', amp=9, n=12, seed=82, nape=88) + _xband('side') + side_brow(63, 'mid', 3.6, 0.6),
  messy('back', amp=9, n=12, seed=82, nape=90) + _xband('back'))

# Brook Dredger: casco gris claro con su correa, pelo azul marino de pinchos que asoma por los lados, unas gafas amarillas
# enormes que le tapan los ojos y la cara alargada y seria
HLM, VIS = _c('#b0aa9a'), _c('#f0c020')
def _helmet(view):
    if view == 'front':
        return [L(outline([(14, 46), (16, 20), (32, 6), (56, 2), (78, 10), (88, 28), (86, 46), (50, 42)]), HLM, 'f'),
                L(quad((14, 44), (50, 38), (86, 44)), _c('#8a8478'), 'f', False, False, 2.4),
                L([(18, 48), (20, 100)], (200, 180, 160, 255), 'f', False, False, 1.6), L([(82, 48), (80, 100)], (200, 180, 160, 255), 'f', False, False, 1.6)]
    if view == 'side':
        return [L(outline([(84, 46), (86, 26), (72, 8), (48, 2), (24, 8), (10, 26), (8, 46), (50, 46)]), HLM, 'f'),
                L([(50, 48), (52, 100)], (200, 180, 160, 255), 'f', False, False, 1.6)]
    return [L(outline([(12, 50), (14, 20), (30, 6), (50, 2), (70, 6), (86, 20), (88, 50), (50, 46)]), HLM, 'f')]
C('brook-dredger', 'delgado', P('#2f3544', '#f8c48c', '#1e1a1a'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=98, face_front=face(chin=108), face_side=face_side(chin=6, nose=3), hairline=[(10, 62), (20, 52), (50, 50), (80, 52), (90, 62)]),
  messy('front', amp=14, n=9, seed=91, rx=50, lo=64) + _helmet('front') +
  [L(blob([(16, 66), (36, 64), (46, 70), (50, 76), (54, 70), (64, 64), (84, 66), (80, 82), (60, 84), (50, 80), (40, 84), (20, 82)], 4), VIS, 'f')],
  messy('side', amp=14, n=9, seed=91, nape=86) + _helmet('side') + [L(blob([(66, 66), (92, 64), (90, 82), (70, 82)], 4), VIS, 'f')],
  messy('back', amp=14, n=9, seed=91, rx=50, nape=88) + _helmet('back') + [L(quad((6, 72), (50, 76), (94, 72)), VIS, 'f', False, False, 2.4)])

# Bucky Rodeo Colt: sombrero vaquero marrón con la cinta clara, pelo rubio ondulado que asoma por los lados, la sombra del
# ala le tapa los ojos; sonrisa y un pañuelo azul al cuello
HT, HT2, BAN = _c('#6c4a3a'), _c('#a88a78'), _c('#2a6ab0')
def _cowboy(view, y=48):
    if view == 'front':
        return [L(outline([(-6, 40), (6, 50), (30, 56), (50, 56), (70, 56), (94, 50), (106, 40), (100, 58), (76, 66), (50, 66), (24, 66), (0, 58)]), HT, 'f'),
                L(outline([(20, 54), (22, 14), (36, 2), (50, 8), (64, 2), (78, 14), (80, 54), (50, 52)]), HT, 'f'),
                L(outline([(21, 40), (50, 38), (79, 40), (80, 52), (50, 50), (21, 52)]), HT2, 'f', False, True)]
    if view == 'side':
        return [L(blob([(-14, 48), (40, 52), (106, 48), (104, 58), (40, 62), (-12, 56)], 6), HT, 'f'),
                L(outline([(14, 52), (18, 14), (34, 2), (60, 2), (78, 12), (82, 52), (50, 50)]), HT, 'f'),
                L(outline([(15, 40), (82, 40), (82, 50), (15, 50)]), HT2, 'f', False, True)]
    return [L(outline([(-6, 46), (50, 56), (106, 46), (100, 62), (50, 68), (0, 62)]), HT, 'f'),
            L(outline([(20, 54), (22, 14), (36, 2), (50, 8), (64, 2), (78, 14), (80, 54), (50, 52)]), HT, 'f'),
            L(outline([(21, 40), (79, 40), (80, 52), (21, 52)]), HT2, 'f', False, True)]
C('bucky-rodeo-colt', 'normal', P('#e6cc92', '#cfae90', '#1e1a1a', shade='#c0a070'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=92, hairline=False),
  [L(outline([(10, 92), (2, 72, 1), (12, 66), (8, 50), (92, 50), (88, 66), (98, 72, 1), (90, 92), (80, 80), (20, 80)]))] + _cowboy('front') +
  [L(blob([(20, 66), (80, 66), (80, 72), (20, 72)], 4), (160, 120, 96, 255), 'f', False),
   L(outline([(18, 96), (50, 106), (82, 96), (92, 104), (66, 112), (50, 120, 1), (36, 112), (8, 104)]), BAN, 'f')],
  [L(outline([(54, 56), (30, 84, 1), (20, 80), (4, 88, 1), (6, 54)]))] + _cowboy('side') + [L(blob([(66, 66), (90, 66), (90, 72), (66, 72)], 4), (160, 120, 96, 255), 'f', False),
                                                                                      L(outline([(40, 98), (86, 100), (88, 110), (40, 110)]), BAN, 'f')],
  [L(outline([(6, 94, 1), (8, 54), (92, 54), (94, 94, 1), (76, 84), (50, 90), (24, 84)]))] + _cowboy('back') +
  [L(outline([(14, 100), (50, 108), (86, 100), (88, 110), (50, 116), (12, 110)]), BAN, 'f')])

# Buff Bagenal: grandullón de piel morena grisácea, pelo castaño oscuro en trencitas pegadas con rastas cortas a los lados;
# gafas de sol oscuras de montura amarilla y labios gruesos
C('buff-bagenal', 'corpulento', P('#2e282c', '#ad8c74', '#1e1a1a', shade='#1e1a1c'),
  F(eyes='none', brows=False, mouth='lips', mouth_y=98, mouth_w=12, face_front=face(w=5, chin=106, jaw=3), nose=(50, 88, 4.6),
    hairline=[(12, 62), (20, 46), (50, 42), (80, 46), (88, 62)]),
  dome('front', top=8, w=44, cy=46, sb=62, shade=False) +
  [strand([(36, 14), (34, 44)], 'shade', 'b', 1.4), strand([(50, 10), (50, 42)], 'shade', 'b', 1.4), strand([(64, 14), (66, 44)], 'shade', 'b', 1.4),
   strand([(12, 72), (8, 96)], 'mid', 'f', 3.0), strand([(88, 72), (92, 96)], 'mid', 'f', 3.0)] +
  shades('front', 76, (40, 36, 40, 255)) + [L(blob([(22, 70), (48, 71), (47, 82), (24, 82)], 4) + [(22, 70)], GOLD, 'f', False, False, 2.0),
                                            L(blob([(78, 70), (52, 71), (53, 82), (76, 82)], 4) + [(78, 70)], GOLD, 'f', False, False, 2.0)],
  dome('side', top=8, w=44, cy=46, nape=82, fr=44, shade=False) + [strand([(40, 66), (36, 92)], 'mid', 'f', 3.0)] + shades('side', 76, (40, 36, 40, 255)),
  dome('back', top=8, w=44, cy=46, nape=84, shade=False) + [strand([(30, 70), (28, 92)], 'mid', 'f', 3.0), strand([(50, 74), (50, 94)], 'mid', 'f', 3.0),
                                                              strand([(70, 70), (72, 92)], 'mid', 'f', 3.0)])

# Buster Lungs: piel morena, pelo blanco grisáceo de pinchos y una cinta ancha naranja con triángulos amarillos y negros que
# le cruza la cabeza tapándole un ojo; una raya negra bajo el otro ojo y sonrisa
OR2, YL3 = _c('#ea6a08'), _c('#f0c040')
def _zband(view):
    if view == 'front':
        out = [L(outline([(6, 56, 1), (94, 34, 1), (96, 48, 1), (8, 74, 1)]), OR2, 'f')]
        for i in range(6):
            x0 = 10 + i * 14
            y0 = 57 - (x0 - 6) * 22 / 88
            out.append(L([(x0, y0), (x0 + 7, y0 - 6), (x0 + 13, y0 - 3)], YL3, 'f', False))
        return out
    if view == 'side':
        return [L(outline([(2, 50), (90, 38), (92, 52), (4, 64)]), OR2, 'f')]
    return [L(outline([(6, 44), (94, 52), (94, 66), (6, 58)]), OR2, 'f')]
C('buster-lungs', 'normal', P('#d8dcd4', '#b47a48', '#1e1a1a', shade='#a8aca4'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=93, hairline=hl(6, 62, 46, 56, jit=3, seed=93)),
  messy('front', amp=12, n=10, seed=94, lo=70) + _zband('front') + [L([(56, 84), (72, 84)], BLACK, 'f', False, False, 3.0)],
  messy('side', amp=12, n=10, seed=94, nape=88) + _zband('side'), messy('back', amp=12, n=10, seed=94, nape=90) + _zband('back'))

# Buzz Supercr Scrambler: casco de motocross verde claro con una estrella amarilla y la mentonera verde; por la visera negra
# se le ven dos ojos amarillos
HG, HG2 = _c('#d2dec0'), _c('#93b45c')
def _moto(view):
    if view == 'front':
        return [L(outline([(6, 90), (4, 44), (16, 14), (50, 2), (84, 14), (96, 44), (94, 90), (70, 106), (30, 106)]), HG, 'f'),
                L(outline([(5, 62), (95, 62), (94, 90), (70, 106), (30, 106), (6, 90)]), HG2, 'f', False, True),
                L(blob([(16, 58), (84, 58), (80, 82), (20, 82)], 4), BLACK, 'f', False),
                L(ell(36, 70, 5, 5), (240, 220, 40, 255), 'f', False), L(ell(64, 70, 5, 5), (240, 220, 40, 255), 'f', False),
                L([(50, 12), (54, 22), (64, 22), (56, 28), (59, 38), (50, 32), (41, 38), (44, 28), (36, 22), (46, 22)], (240, 220, 40, 255), 'f', False, True),
                L(ell(40, 94, 2.4, 2.4), _c('#5a7a3a'), 'f', False), L(ell(50, 96, 2.4, 2.4), _c('#5a7a3a'), 'f', False), L(ell(60, 94, 2.4, 2.4), _c('#5a7a3a'), 'f', False)]
    if view == 'side':
        return [L(outline([(2, 82), (2, 40), (20, 10), (50, 2), (80, 10), (96, 34), (100, 72), (92, 100), (60, 104), (20, 96)]), HG, 'f'),
                L(outline([(50, 62), (100, 60), (100, 72), (92, 100), (60, 104), (40, 94)]), HG2, 'f', False, True),
                L(blob([(64, 56), (98, 54), (96, 76), (66, 78)], 4), BLACK, 'f', False), L(ell(88, 66, 4, 5), (240, 220, 40, 255), 'f', False)]
    return [L(outline([(6, 90), (4, 44), (16, 14), (50, 2), (84, 14), (96, 44), (94, 90), (70, 104), (30, 104)]), HG, 'f'),
            L(outline([(5, 70), (95, 70), (94, 90), (70, 104), (30, 104), (6, 90)]), HG2, 'f', False, True)]
C('buzz-supercr-scrambler', 'normal', P('#d2dec0', '#f2bc84', '#1e1a1a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False), _moto('front'), _moto('side'), _moto('back'))

# -------------------------------------------------------------------------------------------------------------- 49-56

# Caffrey Punt (portero): pelo caoba con raya al medio que le cae hasta la mandíbula y un antifaz de dormir gris sobre los
# ojos; sonrisa tranquila
GRY = _c('#555657')
C('caffrey-punt', 'normal', P('#b25426', '#f6c096', '#1e1a1a', shade='#86401c', deep='#642c18'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=95, face_front=face(chin=106), hairline=[(10, 66), (16, 46), (36, 38), (50, 44), (64, 38), (84, 46), (90, 66)]),
  dome('front', top=0, w=46, cy=44, long=98, flare=2) +
  [fr([(14, 66), (20, 40), (44, 28), (50, 38), (56, 28), (80, 40), (86, 66), (76, 50), (58, 40), (50, 48), (42, 40), (24, 50)]),
   L(blob([(10, 68), (50, 64), (90, 68), (88, 84), (50, 82), (12, 84)], 4), GRY, 'f'), L(quad((36, 76), (40, 72), (44, 76)), (80, 80, 82, 255), 'f', False, False, 1.4)],
  dome('side', top=0, w=46, cy=44, long=98, fr=56) + [L(blob([(30, 66), (92, 64), (92, 82), (30, 80)], 4), GRY, 'f')],
  dome('back', top=0, w=46, cy=44, long=98, ends=4) + [L(blob([(8, 70), (92, 70), (92, 80), (8, 80)], 4), GRY, 'f')])

# Campen Allerjee: casco de obra amarillo con una linterna crema delante y la cinta gris; piel tostada, ojos de párpado caído,
# pecas y la boca en O
HH, LMP = _c('#fcd45c'), _c('#eedeb4')
def _hardhat(view):
    if view == 'front':
        return [L(outline([(10, 52), (12, 26), (28, 6), (50, 0), (72, 6), (88, 26), (90, 52), (50, 48)]), HH, 'f'),
                L(blob([(4, 52), (50, 46), (96, 52), (96, 58), (50, 54), (4, 58)], 4), HH, 'f'),
                L(blob([(12, 42), (50, 38), (88, 42), (88, 50), (50, 46), (12, 50)], 4), _c('#787a7a'), 'f', False),
                L(ell(50, 28, 10, 10), LMP, 'f'), L([(44, 28), (56, 28)], OUTC, 'f', False, False, 1.0), L([(50, 20), (50, 36)], OUTC, 'f', False, False, 1.0)]
    if view == 'side':
        return [L(outline([(82, 52), (86, 26), (72, 6), (48, 0), (24, 6), (8, 26), (6, 52), (50, 50)]), HH, 'f'),
                L(blob([(-2, 54), (50, 50), (100, 50), (98, 58), (50, 58), (0, 60)], 4), HH, 'f'),
                L(outline([(84, 22), (96, 22), (96, 38), (84, 38)]), LMP, 'f')]
    return [L(outline([(10, 54), (12, 26), (28, 6), (50, 0), (72, 6), (88, 26), (90, 54), (50, 50)]), HH, 'f'),
            L(blob([(4, 56), (50, 50), (96, 56), (96, 62), (50, 58), (4, 62)], 4), HH, 'f')]
C('campen-allerjee', 'bajito', P('#2a2018', '#d4a060', '#1e1a1a'),
  F(eyes='round', brows=False, mouth='none', hairline=False),
  _hardhat('front') + [L([(28, 72), (44, 72)], BLACK, 'f', False, False, 2.6), L([(56, 72), (72, 72)], BLACK, 'f', False, False, 2.6),
                       L(ell(50, 94, 4, 4.6), (130, 60, 40, 255), 'f'), L([(18, 50), (16, 92)], _c('#787a7a'), 'f', False, False, 2.0),
                       L([(82, 50), (84, 92)], _c('#787a7a'), 'f', False, False, 2.0)] + freckles(86, 24),
  _hardhat('side') + [L([(76, 72), (86, 72)], BLACK, 'f', False, False, 2.6), L([(50, 52), (52, 92)], _c('#787a7a'), 'f', False, False, 2.0)],
  _hardhat('back'))

# Candy Reviva: pelo rojo oscuro corto con dos mechones que se levantan hacia fuera como cuernos; aros dorados en las orejas,
# ojos negros afilados y sonrisa
C('candy-reviva', 'chica', P('#9c4040', '#f6c096', '#1e1a1a', shade='#782e2e'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=93, hairline=[(12, 62), (18, 48), (36, 40), (50, 46), (64, 40), (82, 48), (88, 62)]),
  dome('front', top=2, w=44, cy=44, sb=62) + [L(outline([(16, 42), (-12, 18, 1), (10, 22), (24, 30)])), L(outline([(84, 42), (112, 18, 1), (90, 22), (76, 30)]))] +
  lashes() + [ring(17, 82, 2.6, 3, GOLD, 1.6), ring(83, 82, 2.6, 3, GOLD, 1.6)],
  dome('side', top=2, w=44, cy=44, nape=80, fr=46) + [L(outline([(30, 30), (6, 2, 1), (24, 10), (40, 20)]))] + lash_side() + [ring(46, 82, 2.4, 2.8, GOLD, 1.6)],
  dome('back', top=2, w=44, cy=44, nape=80) + [L(outline([(16, 42), (-12, 18, 1), (10, 22), (24, 30)])), L(outline([(84, 42), (112, 18, 1), (90, 22), (76, 30)]))])

# Carmen Aria: pelo castaño claro con raya a un lado y un tirabuzón largo que le cae por un lado hasta el pecho, una flor
# blanca detrás de la oreja; ojos grandes morados y sonrisa
def _flower(cx, cy, r=5):
    import math
    out = [L(ell(cx + r * math.cos(a), cy + r * math.sin(a), r * 0.75, r * 0.75), WHITE, 'f') for a in [i * 2 * math.pi / 5 for i in range(5)]]
    return out + [L(ell(cx, cy, r * 0.45, r * 0.45), (240, 220, 120, 255), 'f', False)]
def _drill(x, y0, y1, s=1.0):
    out, y, i = [], y0, 0
    while y < y1:
        out.append(L(ell(x + (2 if i % 2 else -2), y, 7 * s, 5.4 * s), 'mid', 'f'))
        y += 7
        i += 1
    return out
C('carmen-aria', 'chica', P('#c29058', '#fde8b8', '#7a4aa8', shade='#94603c', deep='#724630'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=[(10, 64), (18, 46), (40, 36), (60, 38), (80, 46), (90, 62)]),
  dome('front', top=0, w=46, cy=44, sb=78) + [fr([(16, 56), (26, 32), (54, 22), (40, 38), (26, 52)])] + _drill(88, 64, 116) + _flower(12, 64, 5),
  dome('side', top=0, w=46, cy=44, nape=86, fr=48) + _drill(30, 72, 112, 0.9),
  dome('back', top=0, w=46, cy=44, nape=86) + _drill(14, 72, 116) + _flower(88, 64, 5))

# Carol Fairfoot: pelo rubio verdoso recogido en trenzas que forman lazos a los lados de la cabeza; ojos grandes azules,
# cejas de enfado y boca seria
C('carol-fairfoot', 'chica', P('#bcb45a', '#fceab8', '#3a8ac8', shade='#968a44', deep='#726030'),
  F(eyes='big', brows='angry', mouth='frown', mouth_y=93, hairline=[(14, 62), (20, 48), (36, 42), (50, 46), (64, 42), (80, 48), (86, 62)]),
  dome('front', top=0, w=44, cy=44, sb=66) + _braid(12, 56, 96) + _braid(88, 56, 96) +
  [strand([(30, 10), (24, 40)], 'shade', 'b', 1.4), strand([(50, 4), (50, 38)], 'shade', 'b', 1.4), strand([(70, 10), (76, 40)], 'shade', 'b', 1.4)],
  dome('side', top=0, w=44, cy=44, nape=80, fr=46) + _braid(30, 60, 96) + [strand([(70, 12), (30, 40)], 'shade', 'b', 1.4)],
  dome('back', top=0, w=44, cy=44, nape=80) + _braid(14, 60, 96) + _braid(86, 60, 96) + [strand([(50, 6), (50, 74)], 'shade', 'b', 1.4)])

# Chandler Spillane: piel grisácea, pelo azul marino de pinchos con pico en la frente, orejas puntiagudas; ojos afilados de
# enfado y labios gruesos
C('chandler-spillane', 'normal', P('#31374f', '#ad8d76', '#1e1a1a', shade='#242838'),
  F(eyes='sharp', brows='angry', mouth='lips', mouth_y=97, mouth_w=10, face_front=face(w=2, chin=106), ears=False,
    hairline=[(12, 60), (20, 46), (36, 44), (50, 54), (64, 44), (80, 46), (88, 60)]),
  messy('front', amp=12, n=9, seed=101, lo=62) + ears_pointy('front', 'skin', 10),
  messy('side', amp=12, n=9, seed=101, nape=84) + ears_pointy('side', 'skin', 10), messy('back', amp=12, n=9, seed=101, nape=86) + ears_pointy('back', 'skin', 10))

# Charles Enduro Lemans: casco de piloto morado con rayas amarillas, la mentonera gris y una visera negra con dos ojos
# amarillos de enfado
PH, PH2 = _c('#714bac'), _c('#9a9aa0')
def _racer(view):
    if view == 'front':
        return [L(outline([(6, 92), (4, 44), (16, 14), (50, 2), (84, 14), (96, 44), (94, 92), (70, 106), (30, 106)]), PH, 'f'),
                L(outline([(30, 96), (70, 96), (66, 106), (34, 106)]), PH2, 'f', False, True),
                L(blob([(14, 58), (86, 58), (82, 82), (18, 82)], 4), BLACK, 'f', False),
                L([(30, 68), (44, 72), (40, 76), (30, 74)], (240, 220, 40, 255), 'f', False), L([(70, 68), (56, 72), (60, 76), (70, 74)], (240, 220, 40, 255), 'f', False),
                L([(38, 54), (36, 30), (44, 10), (56, 10), (64, 30), (62, 54)], (220, 210, 70, 255), 'f', False, False, 2.0)]
    if view == 'side':
        return [L(outline([(2, 84), (2, 40), (20, 10), (50, 2), (80, 10), (96, 34), (100, 74), (92, 100), (60, 104), (20, 96)]), PH, 'f'),
                L(blob([(64, 56), (98, 54), (96, 78), (66, 80)], 4), BLACK, 'f', False), L([(82, 64), (94, 66), (92, 70), (82, 70)], (240, 220, 40, 255), 'f', False),
                L(quad((10, 50), (40, 10), (90, 30)), (220, 210, 70, 255), 'f', False, False, 2.0)]
    return [L(outline([(6, 92), (4, 44), (16, 14), (50, 2), (84, 14), (96, 44), (94, 92), (70, 104), (30, 104)]), PH, 'f'),
            L([(38, 96), (36, 30), (44, 10), (56, 10), (64, 30), (62, 96)], (220, 210, 70, 255), 'f', False, False, 2.0)]
C('charles-enduro-lemans', 'normal', P('#714bac', '#f2bc84', '#1e1a1a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False), _racer('front'), _racer('side'), _racer('back'))

# Chauncey Slinka: pelo morado liso hasta los hombros con dos moños abultados arriba y un flequillo recto de puntas como
# goteras; piel pálida, ojos afilados con ojeras y un pañuelo rosa al cuello
C('chauncey-slinka', 'chica', P('#7c66c2', '#e8d4cc', '#2a2440', shade='#5e4c9e', deep='#443578'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=93, hairline=False),
  bowl('front', top=6, side=104) +
  [L(ell(18, 12, 18, 14)), L(ell(82, 12, 18, 14)),
   fr([(12, 44), (30, 30), (50, 26), (70, 30), (88, 44), (88, 64), (82, 60), (80, 70, 1), (74, 60), (68, 66, 1), (62, 58), (56, 68, 1), (50, 58), (44, 68, 1), (38, 58),
       (32, 66, 1), (26, 60), (20, 70, 1), (18, 60), (12, 64)], 'deep'),
   L([(30, 84), (36, 86)], (110, 90, 120, 255), 'f', False, False, 1.4), L([(70, 84), (64, 86)], (110, 90, 120, 255), 'f', False, False, 1.4),
   L(outline([(20, 102), (50, 110), (80, 102), (88, 112), (60, 116), (50, 124, 1), (40, 116), (12, 112)]), PINK, 'f')],
  bowl('side', top=6, nape=104) + [L(ell(30, 8, 16, 13)), L(ell(66, 4, 14, 12)), fr([(64, 30), (90, 40), (92, 64), (86, 58), (84, 68, 1), (78, 56), (70, 50)], 'deep')],
  bowl('back', top=6, nape=106) + [L(ell(18, 12, 18, 14)), L(ell(82, 12, 18, 14))])

# -------------------------------------------------------------------------------------------------------------- 57-59

# Chinami "Chii" Tokunaga: melena castaña larga y ondulada con flequillo; cara dulce, ojos grandes oscuros, pendientes y
# sonrisa (su retrato es de píxeles de la DS)
C('chinami-chii-tokunaga', 'chica', P('#5e4626', '#fad4ba', '#2a1e14', shade='#46321a', deep='#33200c'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=[(12, 64), (16, 50), (28, 58), (40, 52), (50, 60), (60, 52), (72, 58), (84, 50), (88, 64)]),
  dome('front', top=2, w=46, cy=44, long=112, flare=6, ends=4) + [L(ell(17, 84, 1.6, 1.6), GOLD, 'f'), L(ell(83, 84, 1.6, 1.6), GOLD, 'f')],
  dome('side', top=2, w=46, cy=44, long=112, fr=58), dome('back', top=2, w=46, cy=44, long=112, ends=5))

# Chip "Spuds" Tatum: grandullón de cara ancha y mandíbula enorme, cabeza rapada con un casquete azul oscuro y un moño crema
# en lo alto; ojos de enfado con pestañas, nariz larga y boca torcida
TOP = _c('#e8dccc')
C('chip-spuds-tatum', 'corpulento', P('#444850', '#fec26e', '#1e1a1a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=100, mouth_w=12, face_front=face(w=8, chin=112, jaw=6), face_side=face_side(chin=8, jaw=6, nose=6),
    hairline=[(16, 52), (24, 40), (50, 36), (76, 40), (84, 52)]),
  [L(outline([(16, 54), (18, 30), (30, 14), (50, 10), (70, 14), (82, 30), (84, 54), (50, 50)])), L(ell(50, 4, 9, 8), TOP, 'f')] + lashes() + nose_tri(92, 4, 18),
  [L(outline([(78, 42), (78, 22), (64, 10), (46, 8), (26, 12), (12, 28), (10, 48), (26, 46), (50, 44)])), L(ell(48, 2, 9, 8), TOP, 'f')] + lash_side() +
  [L(outline([(84, 76), (100, 96, 1), (86, 98)]), 'skin', 'f', True, True)],
  [L(outline([(14, 58), (16, 30), (30, 14), (50, 10), (70, 14), (84, 30), (86, 58), (50, 64)])), L(ell(50, 4, 9, 8), TOP, 'f')])

# Chuckie "Lasso" Roper: sombrero vaquero marrón con la copa pellizcada, pelo rubio crema con un flequillo largo que le tapa
# un ojo; un pañuelo naranja con cordón al cuello, ojo castaño y sonrisa
HT3, HT4, BNO = _c('#958064'), _c('#6e5c46'), _c('#f0a030')
def _cowboy2(view):
    if view == 'front':
        return [L(outline([(-8, 34), (8, 44), (30, 50), (50, 50), (70, 50), (92, 44), (108, 34), (100, 52), (76, 60), (50, 60), (24, 60), (0, 52)]), HT3, 'f'),
                L(outline([(20, 48), (18, 10), (34, -6, 1), (46, 6), (54, 6), (66, -6, 1), (82, 10), (80, 48), (50, 46)]), HT3, 'f'),
                L(outline([(56, 4), (66, -6), (82, 10), (80, 46), (70, 20)]), HT4, 'f', False)]
    if view == 'side':
        return [L(blob([(-14, 44), (40, 48), (106, 42), (104, 52), (40, 58), (-12, 52)], 6), HT3, 'f'),
                L(outline([(14, 48), (16, 10), (30, -6, 1), (50, 4), (70, -6, 1), (82, 10), (82, 48), (50, 46)]), HT3, 'f')]
    return [L(outline([(-8, 40), (50, 50), (108, 40), (100, 58), (50, 64), (0, 58)]), HT3, 'f'),
            L(outline([(20, 50), (18, 10), (34, -6, 1), (46, 6), (54, 6), (66, -6, 1), (82, 10), (80, 50), (50, 48)]), HT3, 'f')]
C('chuckie-lasso-roper', 'normal', P('#ece0b0', '#fce8c4', '#7a3a1e', shade='#c8bc8a'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=93, hairline=[(8, 66), (16, 56), (50, 54), (84, 56), (92, 66)]),
  dome('front', top=10, w=46, cy=48, sb=80) + _cowboy2('front') +
  [fr([(12, 54), (40, 52), (56, 56), (54, 72), (48, 92, 1), (40, 78), (30, 90, 1), (24, 72), (16, 78)]), strand([(30, 56), (36, 84)], 'shade', 'f', 1.0),
   L(outline([(18, 100), (50, 110), (82, 100), (94, 104), (72, 116), (54, 112), (40, 118), (8, 106)]), BNO, 'f'),
   L([(46, 112), (44, 124)], (240, 230, 210, 255), 'f', False, False, 1.6), L([(54, 112), (56, 124)], (240, 230, 210, 255), 'f', False, False, 1.6)],
  dome('side', top=10, w=46, cy=48, nape=86, fr=58) + _cowboy2('side') + [L(outline([(40, 98), (86, 100), (88, 110), (40, 110)]), BNO, 'f')],
  dome('back', top=10, w=46, cy=48, nape=86) + _cowboy2('back') + [L(outline([(14, 100), (50, 108), (86, 100), (88, 110), (50, 116), (12, 110)]), BNO, 'f')])
