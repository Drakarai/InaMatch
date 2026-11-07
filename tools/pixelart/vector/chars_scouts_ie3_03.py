"""Ojeadores de IE3 (scouts-ie3), tanda 03: dibujados a partir de su retrato de Victory Road (ninguno tiene modelo 3D
que cuadre); claves 'scouts-ie3:<id>'. El perfil y la espalda se deducen del retrato. Muchos van con casco, capucha o
máscara: esas piezas son capas de delante. Reutiliza ayudas de las tandas de IE1 e IE2 (sin editarlas)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars_scouts_ie1_03 import blush, eyes_custom, side_eye_custom, thick_brows, side_brow  # noqa: F401
from chars_scouts_ie1_09 import _c, dome, face, face_side, hl, mark  # noqa: F401
from chars_scouts_ie1_10 import nose_line, nose_tri, squint  # noqa: F401
from chars_scouts_ie2_03 import curls, round_glasses, skull, teeth_grin  # noqa: F401
from chars_scouts_ie1_03 import freckles  # noqa: F401
from chars_scouts_ie2_04 import lash_side, lashes, sharp_eye_side, sharp_eyes  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401

K = 'scouts-ie3:'
WHITE = (250, 250, 250, 255)
BLACK = (26, 20, 24, 255)
DARK = (40, 34, 40, 255)
LIP = (200, 96, 100, 255)


def F(**k):
    d = {'eyes': 'normal', 'mouth': 'line'}
    d.update(k)
    return d


def P(hair, skin, iris='#302232', **k):
    return pal(hair, skin, iris, **k)


def C(pid, body, palette, f, front, side, back):
    """El nacimiento del pelo baja por el borde de la cara (si no, su raya cruza el pelo de los lados)."""
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[K + pid] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def mirx(pts):
    """Refleja puntos (con o sin punta) en x: 100 - x."""
    return [(100 - p[0], p[1]) + tuple(p[2:]) for p in pts][::-1]


def both(pts, c='mid', z='f', sil=True, ln=False):
    """La misma forma a los dos lados de la cara."""
    return [L(outline(pts), c, z, sil, ln), L(outline(mirx(pts)), c, z, sil, ln)]


def horns(view, c, rx=30, y=30, up=-10, out=14):
    """Cuernos de casco vikingo a los lados (de perfil, uno que sale hacia atrás y arriba)."""
    if view == 'front':
        pts = [(50 - rx + 4, y + 6), (50 - rx - out, y - 2), (50 - rx - out - 2, up, 1), (50 - rx - out + 8, y - 8), (50 - rx + 8, y - 2)]
        return both(pts, c)
    if view == 'side':
        return [L(outline([(36, y + 4), (22, y - 6), (26, up - 4, 1), (32, y - 10), (44, y - 2)]), c, 'f')]
    pts = [(50 - rx + 4, y + 6), (50 - rx - out, y - 2), (50 - rx - out - 2, up, 1), (50 - rx - out + 8, y - 8), (50 - rx + 8, y - 2)]
    return both(pts, c)


def hood(view, c, cd, open_=True):
    """Capucha que tapa la cabeza y baja hasta los hombros; de frente deja ver la cara en un hueco oscuro."""
    if view == 'front':
        out = [L(outline([(4, 112), (2, 60), (10, 20), (50, -4), (90, 20), (98, 60), (96, 112), (70, 110), (30, 110)]), c, 'f')]
        if open_:
            out.append(L(outline([(22, 100), (18, 66), (28, 44), (50, 38), (72, 44), (82, 66), (78, 100), (50, 108)]), cd, 'f', False))
        return out
    if view == 'side':
        return [L(outline([(2, 112), (-2, 60), (8, 18), (46, -4), (82, 10), (96, 40), (92, 60), (80, 50), (70, 64), (74, 104), (40, 112)]), c, 'f')]
    return [L(outline([(4, 112), (2, 60), (10, 20), (50, -4), (90, 20), (98, 60), (96, 112), (50, 116)]), c, 'f'),
            L(outline([(56, 2), (84, 18), (94, 56), (90, 108), (66, 110)]), cd, 'f', False)]


# ------------------------------------------------------------------------------------------------------------ jugadores

# Gracey Grapples: melena enorme gris azulado en ondas que le baja hasta la barbilla; una cinta en pico verde con el
# centro azul y el borde crema sobre la frente; piel morena, ojos verdes afilados, sonrisa y pendientes de bola crema
GRN, BLU, CRM = _c('#7ac83a'), _c('#26489a'), _c('#f0e2b0')
C('gracey-grapples', 'chica', P('#9ab4c8', '#b47c52', iris='#3a9a3a', shade='#7a96ac', deep='#5e7890'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=93, hairline=False),
  dome('front', top=-2, w=54, cy=48, n=10, amp=7, soft=True, long=104, flare=8, seed=31) +
  [L(outline([(12, 60), (14, 46), (30, 34), (50, 40), (70, 34), (86, 46), (88, 60), (70, 52), (50, 58), (30, 52)]), CRM, 'f'),
   L(outline([(18, 56), (20, 48), (32, 39), (50, 45), (68, 39), (80, 48), (82, 56), (68, 49), (50, 54), (32, 49)]), GRN, 'f', False),
   L(outline([(36, 44), (50, 48), (64, 44), (60, 51), (50, 53), (40, 51)]), BLU, 'f', False),
   L(ell(14, 86, 4, 4), CRM, 'f'), L(ell(86, 86, 4, 4), CRM, 'f')],
  dome('side', top=-2, w=54, cy=48, n=10, amp=7, soft=True, long=104, flare=8, seed=31, fr=52) +
  [L(outline([(6, 50), (40, 38), (80, 34), (90, 42), (88, 52), (60, 48), (8, 60)]), CRM, 'f'),
   L(outline([(10, 52), (40, 42), (78, 38), (86, 44), (84, 49), (60, 45), (10, 56)]), GRN, 'f', False), L(ell(48, 84, 3.6, 3.6), CRM, 'f')],
  dome('back', top=-2, w=54, cy=48, n=10, amp=7, soft=True, long=104, flare=8, seed=31, ends=5) +
  [L(outline([(6, 56), (50, 46), (94, 56), (92, 62), (50, 54), (8, 62)]), GRN, 'f')])

# Graham "F1" Dupree (portero): casco de carreras integral naranja rojizo con franjas blancas y negra por el centro y una
# visera negra con dos ojos amarillos; no se le ve la cara
ORN, ORD, VIS, YEL = _c('#e0502a'), _c('#b8381e'), _c('#1e1a1c'), _c('#f4e030')
def _f1(view):
    if view == 'front':
        return [L(outline([(6, 104), (2, 60), (10, 20), (50, -2), (90, 20), (98, 60), (94, 104), (50, 110)]), ORN, 'f'),
                L(outline([(64, 2), (88, 20), (97, 60), (92, 102), (74, 106), (80, 60)]), ORD, 'f', False),
                L(outline([(36, -1), (64, -1), (64, 56), (36, 56)]), WHITE, 'f', False),
                L(outline([(43, -2), (57, -2), (57, 56), (43, 56)]), VIS, 'f', False),
                L(outline([(36, 88), (64, 88), (62, 108), (38, 108)]), WHITE, 'f', False),
                L(outline([(43, 88), (57, 88), (56, 109), (44, 109)]), VIS, 'f', False),
                L(outline([(10, 58), (90, 58), (88, 88), (12, 88)]), (196, 196, 200, 255), 'f'),
                L(outline([(14, 61), (86, 61), (84, 85), (16, 85)]), VIS, 'f', False),
                L(outline([(24, 70), (36, 66), (44, 72), (34, 78)]), YEL, 'f', False), L(outline([(76, 70), (64, 66), (56, 72), (66, 78)]), YEL, 'f', False),
                L(outline([(4, 56), (10, 54), (10, 72), (4, 72)]), YEL, 'f'), L(outline([(96, 56), (90, 54), (90, 72), (96, 72)]), YEL, 'f')]
    if view == 'side':
        return [L(outline([(2, 96), (0, 50), (14, 12), (50, -2), (82, 10), (98, 44), (98, 92), (70, 106), (30, 104)]), ORN, 'f'),
                L(outline([(14, 8), (34, 0), (40, 4), (20, 18), (8, 50), (2, 50)]), WHITE, 'f', False),
                L(outline([(24, 2), (30, 0), (12, 30), (6, 40), (4, 34)]), VIS, 'f', False),
                L(outline([(58, 58), (98, 54), (99, 88), (64, 88)]), (196, 196, 200, 255), 'f'),
                L(outline([(62, 61), (97, 58), (97, 85), (66, 85)]), VIS, 'f', False),
                L(outline([(80, 68), (94, 66), (94, 76), (82, 76)]), YEL, 'f', False),
                L(outline([(40, 56), (48, 54), (48, 72), (40, 72)]), YEL, 'f')]
    return [L(outline([(6, 104), (2, 60), (10, 20), (50, -2), (90, 20), (98, 60), (94, 104), (50, 110)]), ORN, 'f'),
            L(outline([(64, 2), (88, 20), (97, 60), (92, 102), (74, 106), (80, 60)]), ORD, 'f', False),
            L(outline([(36, -1), (64, -1), (64, 108), (36, 108)]), WHITE, 'f', False),
            L(outline([(43, -2), (57, -2), (57, 109), (43, 109)]), VIS, 'f', False)]
C('graham-f1-dupree', 'normal', P('#302020', '#c08a5a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False), _f1('front'), _f1('side'), _f1('back'))

# Gram "Vinyl" Vineela: pelo rubio ceniza en mechones lisos con un tupé alto echado hacia atrás y un flequillo largo que
# le tapa un ojo; los mechones de los lados caen hasta la mandíbula; ojo negro entornado y media sonrisa
C('gram-vinyl-vineela', 'normal', P('#d8cc9c', '#f4c896', iris='#1e1a1a', shade='#b4a878', deep='#8a8058'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=92, eye_sep=14, hairline=[(6, 70), (18, 54), (30, 46), (50, 44), (70, 46), (86, 54), (94, 70)]),
  [L(outline([(10, 98), (8, 50), (16, 22), (34, 4), (52, -8), (66, -18, 1), (64, -4), (80, 10), (92, 34), (92, 98), (86, 74), (16, 74)])),
   L(outline([(56, -2), (80, 12), (92, 40), (90, 96), (82, 60), (72, 30)]), 'shade', 'b', False),
   strand([(30, 10), (24, 40), (18, 80)], 'deep', 'b', 1.0), strand([(78, 20), (84, 50), (86, 86)], 'deep', 'b', 1.0),
   L(outline([(46, 40), (60, 34), (80, 46), (86, 68), (82, 92, 1), (74, 74), (66, 86, 1), (60, 62), (54, 52)]), 'mid', 'f'),
   strand([(62, 42), (70, 60), (72, 78)], 'deep', 'f', 1.0)],
  [L(outline([(54, 56), (62, 46), (82, 44), (94, 28), (84, 10), (66, -2), (60, -16, 1), (48, -2), (24, 4), (8, 22), (2, 50), (6, 92), (18, 98), (30, 86),
              (44, 76), (52, 66)])),
   L(outline([(70, 40), (90, 36), (96, 52), (92, 74, 1), (86, 58)]), 'mid', 'f'),
   strand([(56, 4), (30, 20), (14, 60)], 'deep', 'b', 1.0)],
  [L(outline([(10, 100), (6, 50), (16, 20), (36, 4), (52, -6), (64, -16, 1), (64, -2), (82, 10), (94, 40), (92, 100), (76, 94, 1), (60, 102, 1), (44, 94, 1),
              (28, 102, 1)])),
   L(outline([(56, 0), (82, 12), (94, 44), (90, 98), (70, 70)]), 'shade', 'b', False),
   strand([(40, 10), (36, 50), (32, 92)], 'deep', 'b', 1.0), strand([(62, 12), (66, 52), (68, 94)], 'deep', 'b', 1.0)])

# Graplen "Grapnel" Hawk: pinchos azul marino altos con llamas naranjas, una placa gris oscuro en la frente y una máscara
# de tela azul marino oscuro que le tapa desde debajo de los ojos hasta el cuello; ojos azul claro afilados
NV, NVD, FL, PL, MK = _c('#26386e'), _c('#1a2650'), _c('#e0602a'), _c('#5e6266'), _c('#2c3a4c')
def _graplen(view):
    if view == 'front':
        return [L(outline([(10, 56), (8, 30), (2, 0, 1), (18, 14), (20, -24, 1), (34, 4), (44, -32, 1), (52, 0), (64, -30, 1), (68, 4), (84, -22, 1), (84, 16),
                           (98, 2, 1), (92, 32), (90, 56)]), NV),
                L(outline([(24, 30), (24, 0), (32, 22)]), FL, 'b', False), L(outline([(42, 28), (44, -14), (50, 24)]), FL, 'b', False),
                L(outline([(60, 26), (64, -12), (66, 24)]), FL, 'b', False), L(outline([(76, 30), (82, -4), (80, 30)]), FL, 'b', False),
                L(outline([(12, 58), (14, 46), (50, 42), (86, 46), (88, 58), (70, 62), (50, 64), (30, 62)]), PL, 'f'),
                L(outline([(14, 84), (24, 82), (36, 84), (50, 80), (64, 84), (76, 82), (86, 84), (90, 108), (70, 118), (30, 118), (10, 108)]), MK, 'f')]
    if view == 'side':
        return [L(outline([(52, 62), (58, 48), (78, 46), (96, 30, 1), (80, 22), (92, 2, 1), (72, 8), (70, -26, 1), (56, 2), (40, -30, 1), (34, 4), (14, -14, 1),
                           (16, 16), (2, 26), (2, 60), (16, 78), (34, 76)]), NV),
                L(outline([(36, 22), (40, -16), (46, 20)]), FL, 'b', False), L(outline([(62, 22), (68, -16), (68, 22)]), FL, 'b', False),
                L(outline([(4, 54), (40, 44), (88, 44), (90, 56), (40, 58), (6, 64)]), PL, 'f'),
                L(outline([(30, 92), (54, 84), (76, 84), (92, 86), (94, 104), (76, 116), (36, 116)]), MK, 'f')]
    return [L(outline([(10, 84), (8, 30), (2, 0, 1), (18, 14), (20, -24, 1), (34, 4), (44, -32, 1), (52, 0), (64, -30, 1), (68, 4), (84, -22, 1), (84, 16),
                       (98, 2, 1), (92, 32), (90, 84), (50, 90)]), NV),
            L(outline([(42, 28), (44, -14), (50, 24)]), FL, 'b', False), L(outline([(64, 26), (66, -14), (70, 24)]), FL, 'b', False),
            L(outline([(6, 56), (50, 50), (94, 56), (94, 64), (50, 58), (6, 64)]), PL, 'f'),
            L(outline([(10, 96), (50, 92), (90, 96), (90, 112), (50, 118), (10, 112)]), MK, 'f')]
C('graplen-grapnel-hawk', 'normal', P('#26386e', '#b8845a', iris='#8ab8e0'),
  F(eyes='sharp', brows='angry', mouth='none', eye_y=74, hairline=False), _graplen('front'), _graplen('side'), _graplen('back'))

# Grim Jinxweaver: capucha verde azulado oscuro remendada con cuernos de ciervo; la cara en sombra con una máscara gris de
# pico y ojos rojos
HD, HDD, BK, RE = _c('#1e5a5a'), _c('#103a3a'), _c('#8a8a86'), _c('#d0303a')
def _antlers(view):
    a = [(30, 8), (22, -8), (12, -14, 1), (20, -12), (18, -24, 1), (24, -12), (26, -20, 1), (30, -8), (36, 4)]
    if view == 'side':
        return [L(outline([(40, 6), (34, -10), (26, -20, 1), (36, -12), (36, -26, 1), (42, -12), (46, -18, 1), (46, -6), (50, 4)]), HD, 'f')]
    return [L(outline(a), HD, 'f'), L(outline(mirx(a)), HD, 'f')]
C('grim-jinxweaver', 'normal', P('#1e5a5a', '#a87a5a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _antlers('front') + hood('front', HD, BLACK) +
  [L(outline([(28, 68), (50, 60), (72, 68), (60, 74), (50, 96, 1), (40, 74)]), BK, 'f'),
   L(outline([(30, 70), (42, 70), (40, 76)]), RE, 'f', False), L(outline([(70, 70), (58, 70), (60, 76)]), RE, 'f', False),
   L([(40, 20), (44, 30), (40, 40)], (150, 170, 170, 255), 'f', False, False, 1.0)],
  _antlers('side') + hood('side', HD, BLACK) + [L(outline([(78, 60), (100, 70, 1), (84, 76)]), BK, 'f')],
  _antlers('back') + hood('back', HD, HDD))

# Grover Noggin: cabeza redonda con un casquete de pelo verde y siete brotes verdes en corona; ojos cerrados de risa (> <),
# coloretes, boca en O y una perilla verde; pañuelo verde azulado al cuello
GV, BUD = _c('#7aa83a'), _c('#a8c84a')
def _buds(view):
    xs = [(14, 20), (26, 10), (38, 4), (50, 0), (62, 4), (74, 10), (86, 20)] if view != 'side' else [(14, 16), (30, 6), (48, 0), (66, 4), (80, 14)]
    out = []
    for x, y in xs:
        out += [L(outline([(x - 5, y + 8), (x - 6, y - 4), (x, y - 14, 1), (x + 6, y - 4), (x + 5, y + 8)]), BUD, 'b'),
                strand([(x, y - 10), (x, y + 6)], (90, 130, 40, 255), 'b', 1.0)]
    return out
C('grover-noggin', 'bajito', P('#7aa83a', '#f4c896', shade='#5e8a2a'),
  F(eyes='none', brows=False, mouth='none', hairline=[(6, 54), (20, 46), (34, 42), (44, 46), (50, 40), (56, 46), (66, 42), (80, 46), (94, 54)],
    face_front=face(w=4, chin=102, jaw=3), ear_out=4),
  _buds('front') + [L(outline([(10, 56), (12, 30), (30, 14), (50, 10), (70, 14), (88, 30), (90, 56), (70, 50), (30, 50)]))] +
  [L([(28, 72), (38, 76), (28, 80)], OUTC, 'f', False, False, 2.2), L([(72, 72), (62, 76), (72, 80)], OUTC, 'f', False, False, 2.2)] +
  blush(84, 22, 5) + [L(ell(50, 90, 3.2, 4.2), (230, 120, 120, 255), 'f', True, True), L(ell(50, 84, 2, 1.6), (230, 150, 120, 255), 'f', False),
                      L(outline([(36, 102), (44, 98), (50, 102), (56, 98), (64, 102), (56, 108), (44, 108)]), GV, 'f')],
  _buds('side') + [L(outline([(52, 60), (60, 46), (82, 40), (88, 26), (70, 10), (44, 6), (20, 12), (6, 32), (6, 56), (22, 72), (40, 70)])),
                   L([(78, 72), (86, 76), (78, 80)], OUTC, 'f', False, False, 2.2), L(ell(86, 92, 2, 3), (230, 120, 120, 255), 'f', True)],
  _buds('back') + [L(outline([(10, 66), (12, 30), (30, 14), (50, 10), (70, 14), (88, 30), (90, 66), (50, 72)]))])

# Gruff "Bruiser" Dorman: grandullón de mandíbula enorme; pinchos azul marino; sombra de ojos azul, cejas moradas, nariz
# roja, una cicatriz cosida en la mejilla y la boca torcida enseñando los dientes apretados
EYB, NOSE = _c('#4a6ac8'), _c('#c8384a')
C('gruff-bruiser-dorman', 'corpulento', P('#2a3a8a', '#f2c8a0', iris='#1e1a1a', brow='#6a3a8a'),
  F(eyes='sharp', brows=False, mouth='none', face_front=face(w=8, chin=112, jaw=10), face_side=face_side(chin=10, jaw=10), eye_y=72, ear_out=8,
    hairline=[(6, 58), (18, 50), (28, 44), (50, 44), (72, 44), (82, 50), (94, 58)]),
  [L(outline([(14, 56), (12, 36), (4, 18, 1), (20, 22), (22, -4, 1), (34, 14), (44, -10, 1), (52, 10), (62, -8, 1), (66, 12), (80, -2, 1), (80, 20), (96, 16, 1),
              (88, 36), (86, 56), (70, 48), (30, 48)])),
   mark([(22, 70), (34, 64), (44, 70), (36, 76), (24, 76)], EYB), mark([(78, 70), (66, 64), (56, 70), (64, 76), (76, 76)], EYB),
   L([(22, 62), (42, 68)], _c('#6a3a8a'), 'f', False, False, 3.6), L([(78, 62), (58, 68)], _c('#6a3a8a'), 'f', False, False, 3.6),
   L(outline([(44, 84), (56, 84), (52, 92, 1), (48, 92, 1)]), NOSE, 'f'),
   L([(18, 84), (30, 96)], OUTC, 'f', False, False, 1.2), L([(18, 90), (26, 86)], OUTC, 'f', False, False, 1.0), L([(22, 94), (30, 90)], OUTC, 'f', False, False, 1.0),
   L(outline([(34, 104), (42, 98), (50, 100), (58, 98), (66, 104), (58, 108), (50, 106), (42, 108)]), WHITE, 'f', True, True),
   L([(38, 103), (62, 103)], OUTC, 'f', False, False, 0.8)],
  [L(outline([(52, 56), (58, 46), (78, 42), (94, 26, 1), (80, 22), (90, 4, 1), (70, 10), (68, -10, 1), (54, 4), (40, -8, 1), (34, 8), (14, 4, 1), (16, 20), (2, 30),
              (4, 56), (18, 72), (40, 70)])),
   L(outline([(72, 68), (84, 64), (88, 72), (76, 76)]), EYB, 'f', False), L(outline([(86, 82), (96, 84), (90, 90, 1)]), NOSE, 'f'),
   L(outline([(80, 104), (92, 102), (92, 108), (82, 108)]), WHITE, 'f', True, True)],
  [L(outline([(14, 66), (12, 36), (4, 18, 1), (20, 22), (22, -4, 1), (34, 14), (44, -10, 1), (52, 10), (62, -8, 1), (66, 12), (80, -2, 1), (80, 20), (96, 16, 1),
              (88, 36), (86, 66), (50, 72)]))])

# Gudrun Lodestone: casco vikingo gris claro con dos cuernos hacia fuera; asoma pelo rubio verdoso en mechones de punta
# por la frente y los lados; ojos azul claro, ceño fruncido
HLM, HLD = _c('#d8d0c4'), _c('#aaa298')
def _viking(view, top=-2, rim=52):
    if view == 'front':
        return [L(outline([(10, rim + 4), (12, 24), (30, 6), (50, top - 8, 1), (70, 6), (88, 24), (90, rim + 4), (50, rim)]), HLM, 'f'),
                L(outline([(56, top), (78, 12), (88, 30), (88, rim + 2), (72, rim)]), HLD, 'f', False),
                L(outline([(10, rim - 2), (50, rim - 6), (90, rim - 2), (90, rim + 6), (50, rim + 2), (10, rim + 6)]), HLD, 'f', True, True)]
    if view == 'side':
        return [L(outline([(2, rim + 8), (6, 24), (24, 4), (48, top - 8, 1), (74, 6), (92, 26), (94, rim), (50, rim + 2)]), HLM, 'f'),
                L(outline([(2, rim + 2), (50, rim - 4), (94, rim - 6), (94, rim + 2), (50, rim + 4), (4, rim + 10)]), HLD, 'f', True, True)]
    return [L(outline([(10, rim + 10), (12, 24), (30, 6), (50, top - 8, 1), (70, 6), (88, 24), (90, rim + 10), (50, rim + 6)]), HLM, 'f'),
            L(outline([(56, top), (78, 12), (88, 30), (88, rim + 8), (72, rim + 6)]), HLD, 'f', False)]
C('gudrun-lodestone', 'chica', P('#c4b048', '#f6d0a8', iris='#5a9ad0', shade='#a08a30'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=False),
  [L(outline([(10, 96), (6, 60), (14, 50), (86, 50), (94, 60), (90, 96, 1), (82, 76), (18, 76)]))] +
  horns('front', HLM, rx=30, y=34, up=8, out=18) + _viking('front') +
  [L(outline([(14, 54), (26, 54), (22, 70, 1)]), 'mid', 'f'), L(outline([(26, 54), (44, 54), (34, 68, 1)]), 'mid', 'f'),
   L(outline([(56, 54), (74, 54), (66, 70, 1)]), 'mid', 'f'), L(outline([(74, 54), (88, 54), (82, 72, 1)]), 'mid', 'f')],
  [L(outline([(54, 60), (40, 70), (20, 84), (4, 76), (6, 56), (60, 56)]))] + [L(outline([(18, 30), (-4, 18), (-12, 2, 1), (-2, 10), (16, 22)]), HLM, 'f')] + _viking('side'),
  [L(outline([(10, 100), (8, 60), (92, 60), (90, 100), (70, 92, 1), (50, 100, 1), (30, 92, 1)]))] +
  horns('back', HLM, rx=30, y=34, up=8, out=18) + _viking('back'))

# Gunnar Boatwright: casco vikingo granate con franjas grises y dos cuernos crema que le tapa hasta la nariz; nariz grande
# naranja, boca torcida hacia abajo, patillas oscuras y piel tostada
MAR, MGR, HRN = _c('#6a3830'), _c('#7a7276'), _c('#f0e2c0')
def _gunnar(view):
    if view == 'front':
        return [L(outline([(10, 74), (10, 36), (26, 12), (50, 4), (74, 12), (90, 36), (90, 74), (50, 72)]), MAR, 'f'),
                L(outline([(24, 16), (40, 8), (42, 64), (24, 64)]), MGR, 'f', False), L(outline([(76, 16), (60, 8), (58, 64), (76, 64)]), MGR, 'f', False),
                L(outline([(8, 64), (50, 60), (92, 64), (92, 78), (50, 74), (8, 78)]), _c('#4a2420'), 'f', True, True)]
    if view == 'side':
        return [L(outline([(4, 80), (6, 36), (24, 10), (50, 2), (76, 10), (92, 36), (94, 72), (50, 74)]), MAR, 'f'),
                L(outline([(40, 4), (56, 4), (52, 66), (38, 66)]), MGR, 'f', False),
                L(outline([(2, 72), (50, 66), (96, 64), (96, 78), (50, 80), (4, 86)]), _c('#4a2420'), 'f', True, True)]
    return [L(outline([(10, 84), (10, 36), (26, 12), (50, 4), (74, 12), (90, 36), (90, 84), (50, 82)]), MAR, 'f'),
            L(outline([(42, 6), (58, 6), (58, 80), (42, 80)]), MGR, 'f', False),
            L(outline([(8, 74), (50, 70), (92, 74), (92, 86), (50, 84), (8, 86)]), _c('#4a2420'), 'f', True, True)]
C('gunnar-boatwright', 'normal', P('#2a3a2a', '#d89a4e'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, hairline=False),
  horns('front', HRN, rx=34, y=34, up=4, out=12) + _gunnar('front') +
  [L(outline([(38, 80), (50, 76), (62, 80), (60, 88), (50, 90), (40, 88)]), _c('#c8782e'), 'f', True, True),
   L(outline([(14, 78), (20, 78), (20, 94), (14, 90)]), 'mid', 'f', False), L(outline([(86, 78), (80, 78), (80, 94), (86, 90)]), 'mid', 'f', False)],
  [L(outline([(26, 34), (12, 18), (14, 0, 1), (22, 16), (36, 24)]), HRN, 'f')] + _gunnar('side') +
  [L(outline([(84, 80), (96, 82), (94, 90), (84, 90)]), _c('#c8782e'), 'f', True, True)],
  horns('back', HRN, rx=34, y=34, up=4, out=12) + _gunnar('back'))

# Gustav "Weather" Weathervane: melena azul celeste alborotada con un remolino en espiral arriba y un flequillo largo que
# le tapa el ojo derecho; ojo rosa, sonrisa de pillo y una bufanda azul que vuela
SCF = _c('#1e5a8a')
C('gustav-weather-weathervane', 'normal', P('#5ab4d8', '#f4d0b0', iris='#c03a7a', shade='#3a8ab0', deep='#2a6a8a', light='#bce4f4'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=92, hairline=[(6, 70), (18, 52), (34, 44), (50, 42), (66, 44), (82, 52), (94, 70)]),
  [L(outline([(10, 92), (6, 50), (14, 18), (34, 0), (56, -6), (80, 2), (96, 24), (98, 60), (94, 96), (86, 74), (16, 74)])),
   L(outline([(60, -2), (84, 8), (96, 34), (94, 88), (84, 60), (74, 22)]), 'shade', 'b', False),
   L(ell(62, -2, 12, 9), 'light', 'b', True, True), strand([(56, -2), (62, -6), (68, -2), (62, 2), (60, -1)], 'shade', 'b', 1.2),
   L(outline([(30, 36), (56, 30), (82, 40), (90, 60), (86, 90, 1), (76, 72), (70, 92, 1), (62, 70), (54, 54), (40, 46)]), 'mid', 'f'),
   strand([(58, 40), (68, 58), (72, 80)], 'deep', 'f', 1.0),
   L(outline([(30, 102), (50, 106), (70, 102), (84, 108), (96, 122, 1), (74, 116), (50, 114), (26, 112)]), SCF, 'f')],
  [L(outline([(56, 56), (64, 44), (86, 42), (98, 26), (90, 6), (66, -6), (40, -2), (18, 8), (4, 32), (0, 70), (8, 96), (20, 86), (36, 76), (48, 68)])),
   L(ell(56, -4, 12, 8), 'light', 'b', True, True), L(outline([(74, 38), (96, 36), (98, 58), (92, 78, 1), (86, 58)]), 'mid', 'f'),
   L(outline([(40, 104), (70, 104), (92, 102), (94, 112), (60, 114), (20, 124, 1), (34, 110)]), SCF, 'f')],
  [L(outline([(8, 98), (6, 50), (14, 18), (34, 0), (56, -6), (80, 2), (96, 24), (98, 60), (94, 100), (76, 90, 1), (60, 100, 1), (44, 90, 1), (28, 100, 1)])),
   L(ell(56, -2, 12, 9), 'light', 'b', True, True), L(outline([(56, 2), (84, 12), (96, 40), (92, 96), (70, 70)]), 'shade', 'b', False),
   L(outline([(20, 104), (80, 104), (100, 118, 1), (76, 114), (24, 114)]), SCF, 'f')])

# Hans Popov: grandullón con un casco gris con cuernos amarillos y protector de nariz; parche negro en un ojo, el otro negro
# y entornado; mofletes, sonrisa torcida y una cicatriz en la barbilla
GRY, GRD, YH = _c('#8a8a8e'), _c('#626266'), _c('#d0b040')
def _hans(view):
    if view == 'front':
        return [L(outline([(16, 62), (14, 36), (28, 16), (50, 10), (72, 16), (86, 36), (84, 62), (50, 56)]), GRY, 'f'),
                L(outline([(60, 12), (80, 24), (86, 42), (84, 60), (72, 56)]), GRD, 'f', False),
                L(outline([(44, 50), (56, 50), (56, 82), (50, 86), (44, 82)]), GRY, 'f', True, True)]
    if view == 'side':
        return [L(outline([(6, 64), (8, 34), (26, 12), (52, 8), (76, 16), (90, 36), (90, 58), (50, 58)]), GRY, 'f'),
                L(outline([(86, 50), (94, 50), (96, 80), (90, 84)]), GRY, 'f', True, True)]
    return [L(outline([(16, 66), (14, 36), (28, 16), (50, 10), (72, 16), (86, 36), (84, 66), (50, 62)]), GRY, 'f'),
            L(outline([(60, 12), (80, 24), (86, 42), (84, 64), (72, 60)]), GRD, 'f', False)]
C('hans-popov', 'corpulento', P('#4a4a3a', '#efd0a8', iris='#1e1a1a'),
  F(eyes='none', brows=False, mouth='none', face_front=face(w=8, chin=108, jaw=6), face_side=face_side(chin=8, jaw=6), ear_out=8, hairline=False),
  horns('front', YH, rx=24, y=28, up=0, out=14) + _hans('front') +
  [L(outline([(22, 68), (40, 64), (44, 76), (30, 80)]), BLACK, 'f'), L([(16, 62), (44, 70)], BLACK, 'f', False, False, 1.4),
   L(outline([(58, 70), (74, 66), (76, 74), (60, 76)]), WHITE, 'f', False), L(ell(66, 72, 3, 3.4), BLACK, 'f', False),
   L([(56, 64), (76, 62)], OUTC, 'f', False, False, 2.6),
   L(quad((38, 100), (52, 94), (66, 98)) + [(72, 94)], OUTC, 'f', False, False, 1.6), L([(42, 104), (46, 110)], OUTC, 'f', False, False, 1.0)],
  [L(outline([(30, 30), (16, 16), (16, -2, 1), (24, 12), (38, 22)]), YH, 'f')] + _hans('side') +
  [L(outline([(78, 70), (88, 68), (88, 76), (80, 76)]), WHITE, 'f', False), L(ell(84, 72, 2.4, 3), BLACK, 'f', False)],
  horns('back', YH, rx=24, y=28, up=0, out=14) + _hans('back'))

# Harley Hogg (portero): casco de sandía verde a rayas con dos pinchos grises; melena verde oliva ondulada por los lados;
# gafas de sol negras redondas, nariz de pico amarilla y boca enfurruñada; cara ancha
WM, WMD, SP = _c('#4a8a3a'), _c('#2a5a22'), _c('#9a9aa0')
C('harley-hogg', 'corpulento', P('#7a7a2a', '#f4c8a0', shade='#5a5a1e'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=97, face_front=face(w=8, chin=106, jaw=5), face_side=face_side(chin=6, jaw=5), ears=False, hairline=False),
  [L(outline([(4, 100), (0, 70), (8, 44), (92, 44), (100, 70), (96, 100), (88, 90), (86, 64), (14, 64), (12, 90)]))] +
  [L(outline([(34, 6), (36, -18, 1), (44, 6)]), SP, 'f'), L(outline([(56, 6), (64, -18, 1), (66, 6)]), SP, 'f'),
   L(outline([(10, 52), (14, 26), (32, 8), (50, 4), (68, 8), (86, 26), (90, 52), (50, 48)]), WM, 'f'),
   strand([(28, 12), (22, 30), (24, 50)], WMD, 'f', 2.4), strand([(44, 6), (40, 30), (42, 48)], WMD, 'f', 2.4),
   strand([(60, 6), (62, 30), (60, 48)], WMD, 'f', 2.4), strand([(76, 14), (80, 32), (78, 50)], WMD, 'f', 2.4),
   L(ell(36, 74, 9, 7), BLACK, 'f', True, True), L(ell(64, 74, 9, 7), BLACK, 'f', True, True), L([(45, 73), (55, 73)], BLACK, 'f', False, False, 2.0),
   L(ell(33, 72, 3, 1.6), (120, 120, 130, 255), 'f', False), L(ell(61, 72, 3, 1.6), (120, 120, 130, 255), 'f', False),
   L(outline([(44, 80), (56, 80), (50, 90, 1)]), _c('#e8c04a'), 'f', True, True)],
  [L(outline([(4, 98), (0, 60), (10, 44), (50, 50), (52, 70), (40, 90), (20, 100)])),
   L(outline([(56, 6), (64, -16, 1), (66, 8)]), SP, 'f'),
   L(outline([(4, 60), (8, 26), (28, 8), (54, 4), (78, 12), (92, 32), (92, 54), (50, 54)]), WM, 'f'),
   strand([(30, 10), (24, 50)], WMD, 'f', 2.4), strand([(56, 6), (54, 52)], WMD, 'f', 2.4), strand([(78, 14), (82, 52)], WMD, 'f', 2.4),
   L(ell(82, 74, 7, 6), BLACK, 'f', True, True), L([(58, 72), (76, 72)], BLACK, 'f', False, False, 2.0),
   L(outline([(86, 80), (98, 86, 1), (86, 90)]), _c('#e8c04a'), 'f', True, True)],
  [L(outline([(4, 104), (2, 60), (98, 60), (96, 104), (80, 96), (64, 104), (50, 96), (36, 104), (20, 96)])),
   L(outline([(34, 6), (36, -18, 1), (44, 6)]), SP, 'f'), L(outline([(56, 6), (64, -18, 1), (66, 6)]), SP, 'f'),
   L(outline([(8, 62), (12, 26), (32, 8), (50, 4), (68, 8), (88, 26), (92, 62), (50, 58)]), WM, 'f'),
   strand([(28, 12), (22, 58)], WMD, 'f', 2.4), strand([(50, 4), (50, 58)], WMD, 'f', 2.4), strand([(72, 12), (78, 58)], WMD, 'f', 2.4)])

# Hattie Couture: pelo verde menta recogido arriba en un moño alto con un adorno amarillo, y dos mechones largos lisos que
# le caen por delante hasta el pecho; piel muy pálida, ojos verdes con pestañas y labios oscuros
C('hattie-couture', 'chica', P('#4ab47a', '#f8ead8', iris='#3a9a5a', shade='#2e8a5a', deep='#1e6a44'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=94, hairline=[(6, 70), (14, 56), (28, 46), (50, 42), (72, 46), (86, 56), (94, 70)]),
  [L(outline([(26, 14), (30, -10), (50, -20), (70, -10), (74, 14), (50, 20)])), L(outline([(40, -14), (50, -22), (60, -14), (50, -10)]), _c('#e0b030'), 'b'),
   L(outline([(14, 64), (10, 34), (24, 12), (50, 6), (76, 12), (90, 34), (86, 64), (50, 50)])),
   L(outline([(56, -12), (72, -6), (74, 12), (86, 30), (86, 60), (70, 40)]), 'shade', 'b', False),
   L(outline([(16, 54), (24, 50), (26, 90), (22, 120), (16, 118), (14, 86)]), 'mid', 'f'), L(outline([(84, 54), (76, 50), (74, 90), (78, 120), (84, 118), (86, 86)]), 'mid', 'f'),
   L([(24, 92), (22, 95)], LIP, 'f', False, False, 0.1), L(outline([(44, 93), (50, 92), (56, 93), (50, 96)]), _c('#5a3a4a'), 'f', False)] + lashes(),
  [L(outline([(30, 10), (34, -12), (52, -20), (68, -10), (68, 10)])),
   L(outline([(54, 52), (62, 42), (78, 36), (88, 26), (74, 8), (50, 4), (24, 8), (8, 26), (6, 50), (14, 64), (30, 62), (44, 58)])),
   L(outline([(62, 50), (70, 48), (72, 90), (70, 120), (64, 118), (64, 86)]), 'mid', 'f')] + lash_side(),
  [L(outline([(26, 14), (30, -10), (50, -20), (70, -10), (74, 14), (50, 20)])), L(outline([(40, -14), (50, -22), (60, -14), (50, -10)]), _c('#e0b030'), 'b'),
   L(outline([(14, 76), (10, 34), (24, 12), (50, 6), (76, 12), (90, 34), (86, 76), (50, 80)])),
   strand([(50, 10), (50, 74)], 'deep', 'b', 1.0), strand([(34, 14), (26, 70)], 'deep', 'b', 1.0), strand([(66, 14), (74, 70)], 'deep', 'b', 1.0)])

# Haydn "Bluey" Woe: calvo, con una cresta de tubos turquesa y blancos de la frente a la nuca; ojeras oscuras, mirada
# torva, una pieza de metal gris sobre la nariz y un collarín metálico
TQ, TQD, MT = _c('#2a8a8a'), _c('#1e6060'), _c('#8a8a8e')
def _tubes(view):
    if view == 'front':
        return [L(outline([(36, 30), (36, 6), (44, -12), (56, -12), (64, 6), (64, 30), (58, 30), (56, 4), (50, -4), (44, 4), (42, 30)]), TQ, 'f'),
                L(outline([(44, 30), (44, 4), (50, -6), (56, 4), (56, 30)]), WHITE, 'f')]
    if view == 'side':
        return [L(outline([(70, 30), (66, 4), (50, -10), (26, -6), (10, 12), (6, 36), (14, 38), (18, 16), (30, 4), (50, 2), (60, 10), (62, 30)]), TQ, 'f'),
                L(outline([(58, 30), (56, 12), (48, 6), (30, 8), (20, 20), (16, 38), (22, 38), (26, 22), (34, 14), (48, 12), (52, 30)]), WHITE, 'f')]
    return [L(outline([(36, 60), (36, 6), (44, -12), (56, -12), (64, 6), (64, 60), (56, 60), (56, 4), (50, -4), (44, 4), (44, 60)]), TQ, 'f'),
            L(outline([(44, 60), (44, 4), (50, -6), (56, 4), (56, 60)]), WHITE, 'f')]
C('haydn-bluey-woe', 'normal', P('#2a8a8a', '#e8cca8', iris='#1e1a1a'),
  F(eyes='dot', brows='angry', mouth='frown', mouth_y=98, hairline=False, face_front=face(chin=104)),
  skull('front') + _tubes('front') +
  [mark([(24, 72), (36, 70), (44, 76), (36, 82), (26, 80)], _c('#5a5050')), mark([(76, 72), (64, 70), (56, 76), (64, 82), (74, 80)], _c('#5a5050')),
   L(outline([(46, 76), (54, 76), (56, 90), (50, 92), (44, 90)]), MT, 'f', True, True)],
  skull('side') + _tubes('side') + [L(outline([(84, 76), (92, 82), (92, 92), (86, 92)]), MT, 'f', True, True)],
  skull('back') + _tubes('back'))

# Hedwig "Headset" Setter: gorra negra con un triángulo gris, cascos de música amarillos sobre un pelo verde rizado; cara
# larga gris tostada, ojos grandes redondos de pupila diminuta, nariz naranja y dientes apretados; barbilla larga
CAP, HP = _c('#2a2a2e'), _c('#e0a02a')
def _headset(view):
    if view == 'front':
        return [L(outline([(12, 48), (14, 22), (32, 6), (50, 2), (68, 6), (86, 22), (88, 48), (50, 44)]), CAP, 'f'),
                L(outline([(40, 10), (60, 10), (50, 36, 1)]), (150, 150, 156, 255), 'f', False),
                L(outline([(8, 62), (16, 56), (20, 84), (12, 88)]), HP, 'f', True, True), L(outline([(92, 62), (84, 56), (80, 84), (88, 88)]), HP, 'f', True, True),
                L(quad((14, 86), (50, 128), (86, 86)), BLACK, 'f', False, False, 2.2)]
    if view == 'side':
        return [L(outline([(6, 52), (8, 22), (28, 6), (52, 2), (76, 10), (90, 30), (92, 46), (50, 46)]), CAP, 'f'),
                L(outline([(36, 60), (50, 58), (52, 86), (38, 88)]), HP, 'f', True, True), L(quad((46, 88), (70, 122), (90, 112)), BLACK, 'f', False, False, 2.2)]
    return [L(outline([(12, 52), (14, 22), (32, 6), (50, 2), (68, 6), (86, 22), (88, 52), (50, 48)]), CAP, 'f'),
            L(outline([(8, 62), (16, 56), (20, 84), (12, 88)]), HP, 'f', True, True), L(outline([(92, 62), (84, 56), (80, 84), (88, 88)]), HP, 'f', True, True)]
C('hedwig-headset-setter', 'delgado', P('#3a8a3a', '#c8b494', iris='#1e1a1a'),
  F(eyes='none', brows=False, mouth='none', face_front=face(w=-2, chin=114), face_side=face_side(chin=12), ears=False, hairline=False),
  [L(outline([(2, 76), (0, 52), (12, 42), (88, 42), (100, 52), (98, 76), (84, 70), (16, 70)]))] + _headset('front') +
  [L(ell(36, 70, 7, 7), WHITE, 'f', True, True), L(ell(64, 70, 7, 7), WHITE, 'f', True, True), L(ell(37, 71, 1.8, 1.8), BLACK, 'f', False), L(ell(63, 71, 1.8, 1.8), BLACK, 'f', False),
   L(ell(50, 82, 5, 3.4), _c('#e8782a'), 'f', True, True),
   L(outline([(40, 100), (60, 100), (58, 108), (42, 108)]), WHITE, 'f', True, True), L([(50, 100), (50, 108)], OUTC, 'f', False, False, 0.8)],
  [L(outline([(2, 80), (0, 50), (14, 42), (54, 48), (50, 74), (30, 82)]))] + _headset('side') +
  [L(ell(82, 70, 5, 6), WHITE, 'f', True, True), L(ell(84, 71, 1.4, 1.4), BLACK, 'f', False), L(ell(92, 82, 3.4, 3), _c('#e8782a'), 'f', True, True)],
  [L(outline([(2, 82), (0, 52), (100, 52), (98, 82), (50, 86)]))] + _headset('back'))

# Hedwig "Heghodge" Hodge (portero): pinchos rojo oscuro en todas direcciones como un erizo, con un bicho marrón (un
# topillo) tumbado encima de la cabeza; ojos negros enfadados y boca pequeña
MOL = _c('#9a7a5a')
C('hedwig-heghodge-hodge', 'normal', P('#a8302a', '#f4c08a', iris='#1e1a1a', shade='#82221e'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=hl(6, 64, 50, 58, jit=3, seed=21)),
  dome('front', top=-2, w=58, cy=50, n=14, amp=16, seed=22, sb=82) +
  [L(outline([(28, 34), (34, 20), (50, 14), (66, 20), (72, 34), (62, 30), (50, 32), (38, 30)]), MOL, 'f'),
   L(outline([(30, 30), (24, 40), (34, 38)]), MOL, 'f'), L(outline([(70, 30), (76, 40), (66, 38)]), MOL, 'f')],
  dome('side', top=-2, w=56, cy=50, n=12, amp=16, seed=22, nape=92, fr=54) + [L(outline([(30, 14), (50, 6), (72, 12), (80, 20), (60, 22), (34, 22)]), MOL, 'f')],
  dome('back', top=-2, w=58, cy=50, n=14, amp=16, seed=22, nape=92) + [L(outline([(30, 30), (36, 16), (50, 12), (64, 16), (70, 30), (50, 26)]), MOL, 'f')])

# Heidi "Li'l Red" Rood: caperuza roja que le enmarca la cara, con el pelo naranja dorado en flequillo y mechones por los
# lados; ojos verdes grandes, sonrisa y un lazo rojo al cuello
RH, RHD = _c('#c8321e'), _c('#9a2414')
C('heidi-li-l-red-rood', 'chica', P('#e8962a', '#f6cca0', iris='#3a8a3a', shade='#c8761e'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, hairline=[(6, 66), (16, 54), (30, 50), (44, 54), (50, 48), (58, 54), (72, 50), (84, 54), (94, 66)]),
  [L(outline([(4, 102), (2, 56), (12, 18), (50, -2), (88, 18), (98, 56), (96, 102), (80, 96), (82, 60), (18, 60), (20, 96)]), RH, 'b'),
   L(outline([(60, 2), (86, 18), (97, 58), (95, 100), (84, 94), (84, 50)]), RHD, 'b', False),
   L(outline([(16, 90), (14, 60), (24, 40), (50, 32), (76, 40), (86, 60), (84, 90), (78, 70), (22, 70)])),
   L(outline([(36, 102), (50, 106), (64, 102), (66, 112), (50, 108), (34, 112)]), RH, 'f'), L(ell(50, 106, 4, 3.6), RHD, 'f')],
  [L(outline([(2, 104), (-2, 56), (8, 18), (46, -2), (80, 10), (92, 30), (88, 42), (64, 40), (54, 60), (52, 100), (30, 108)]), RH, 'f'),
   L(outline([(60, 40), (84, 40), (90, 52), (86, 66, 1), (78, 54)]), 'mid', 'f')],
  [L(outline([(4, 106), (2, 56), (12, 18), (50, -2), (88, 18), (98, 56), (96, 106), (50, 112)]), RH, 'f'),
   L(outline([(58, 2), (86, 18), (97, 58), (95, 104), (70, 108)]), RHD, 'f', False)])

# Helmut Hardy: casco de piloto blanco con llamas rojas y naranjas y dos aletas amarillas en cuerno; visera negra que le
# tapa los ojos y correas amarillas que cuelgan; cara pálida y boca pequeña
HW, HO, HR = _c('#f2eee6'), _c('#f0a020'), _c('#e0401e')
def _hardy(view):
    if view == 'front':
        return [L(outline([(26, 20), (24, -10), (34, -20, 1), (38, 8)]), HO, 'f'), L(outline([(74, 20), (76, -10), (66, -20, 1), (62, 8)]), HO, 'f'),
                L(outline([(10, 70), (8, 38), (20, 14), (50, 4), (80, 14), (92, 38), (90, 70), (50, 66)]), HW, 'f'),
                L(outline([(28, 50), (32, 28), (40, 36), (46, 16), (52, 32), (58, 12), (64, 34), (70, 26), (72, 50), (50, 56)]), HR, 'f', False),
                L(outline([(36, 50), (42, 36), (48, 44), (54, 30), (60, 44), (64, 50), (50, 54)]), HO, 'f', False),
                L(outline([(10, 60), (50, 56), (90, 60), (88, 80), (50, 78), (12, 80)]), BLACK, 'f', True, True),
                L([(20, 66), (80, 66)], (120, 120, 130, 255), 'f', False, False, 1.4),
                L(quad((14, 76), (12, 100), (16, 118)), HO, 'f', False, False, 2.0), L(quad((86, 76), (88, 100), (84, 118)), HO, 'f', False, False, 2.0)]
    if view == 'side':
        return [L(outline([(48, 14), (44, -14), (54, -22, 1), (58, 10)]), HO, 'f'),
                L(outline([(2, 76), (4, 36), (20, 10), (50, 2), (78, 10), (94, 34), (96, 62), (60, 64)]), HW, 'f'),
                L(outline([(30, 50), (34, 26), (42, 34), (50, 14), (56, 30), (64, 24), (66, 50)]), HR, 'f', False),
                L(outline([(56, 58), (96, 56), (98, 78), (60, 78)]), BLACK, 'f', True, True),
                L(quad((44, 70), (40, 100), (46, 118)), HO, 'f', False, False, 2.0)]
    return [L(outline([(26, 20), (24, -10), (34, -20, 1), (38, 8)]), HO, 'f'), L(outline([(74, 20), (76, -10), (66, -20, 1), (62, 8)]), HO, 'f'),
            L(outline([(10, 82), (8, 38), (20, 14), (50, 4), (80, 14), (92, 38), (90, 82), (50, 78)]), HW, 'f'),
            L(outline([(26, 60), (30, 30), (40, 40), (46, 18), (52, 34), (58, 14), (64, 36), (70, 28), (74, 60), (50, 66)]), HR, 'f', False)]
C('helmut-hardy', 'normal', P('#3a2a20', '#f8e2c8'),
  F(eyes='none', brows=False, mouth='line', mouth_y=94, hairline=False, ears=False), _hardy('front'), _hardy('side'), _hardy('back'))

# Helmut Hoarder: yelmo plateado con dos cuernos curvados hacia arriba y un emblema en la frente, que le baja hasta las
# cejas; melena gris verdosa desgreñada hasta el cuello; ojos turquesa afilados y ceño fruncido
SIL, SILD = _c('#d4d0cc'), _c('#a29e9a')
def _hoarder(view):
    if view == 'front':
        return [L(outline([(20, 30), (12, 6), (16, -16, 1), (24, 2), (32, 16)]), SIL, 'f'), L(outline([(80, 30), (88, 6), (84, -16, 1), (76, 2), (68, 16)]), SIL, 'f'),
                L(outline([(12, 66), (12, 34), (28, 12), (50, 2, 1), (72, 12), (88, 34), (88, 66), (70, 60), (50, 70, 1), (30, 60)]), SIL, 'f'),
                L(outline([(58, 8), (78, 20), (86, 40), (86, 62), (72, 58)]), SILD, 'f', False),
                L(outline([(40, 40), (50, 30), (60, 40), (56, 54), (50, 60), (44, 54)]), SILD, 'f', False)]
    if view == 'side':
        return [L(outline([(40, 26), (30, 4), (34, -18, 1), (42, 2), (52, 16)]), SIL, 'f'),
                L(outline([(4, 64), (6, 32), (24, 10), (52, 2, 1), (78, 12), (92, 36), (92, 60), (72, 58), (40, 60)]), SIL, 'f')]
    return [L(outline([(20, 30), (12, 6), (16, -16, 1), (24, 2), (32, 16)]), SIL, 'f'), L(outline([(80, 30), (88, 6), (84, -16, 1), (76, 2), (68, 16)]), SIL, 'f'),
            L(outline([(12, 70), (12, 34), (28, 12), (50, 2, 1), (72, 12), (88, 34), (88, 70), (50, 66)]), SIL, 'f'),
            L(outline([(58, 8), (78, 20), (86, 40), (86, 68), (72, 64)]), SILD, 'f', False)]
C('helmut-hoarder', 'normal', P('#a4a07a', '#f2cca4', iris='#3aa0a0', shade='#828058'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=False),
  [L(outline([(10, 110), (2, 86, 1), (8, 70), (0, 56, 1), (14, 50), (86, 50), (100, 56, 1), (92, 70), (98, 86, 1), (90, 110), (80, 96), (82, 72), (18, 72), (20, 96)]))] +
  _hoarder('front') + [L(outline([(16, 62), (24, 60), (20, 76, 1)]), 'mid', 'f'), L(outline([(84, 62), (76, 60), (80, 76, 1)]), 'mid', 'f')],
  [L(outline([(54, 60), (40, 74), (36, 100), (20, 110, 1), (16, 96), (2, 98, 1), (6, 80), (-4, 70, 1), (6, 56), (60, 56)]))] + _hoarder('side'),
  [L(outline([(8, 108), (2, 86, 1), (8, 66), (92, 66), (98, 86, 1), (92, 108), (78, 100, 1), (64, 110, 1), (50, 100, 1), (36, 110, 1), (22, 100, 1)]))] + _hoarder('back'))

# Holly Marx (portera): media melena turquesa lisa con flequillo recto hasta las cejas y dos moños en forma de cilindro a
# los lados de la cabeza; ojos marrones grandes y boquita enfadada
C('holly-marx', 'chica', P('#3aa4a0', '#f6c896', iris='#7a4a2a', shade='#2a8480', deep='#1e6460'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=94, hairline=[(6, 66), (14, 62), (30, 62), (50, 62), (70, 62), (86, 62), (94, 66)]),
  [L(outline([(8, 22), (-6, 14), (-8, 30), (8, 34)])), L(outline([(92, 22), (106, 14), (108, 30), (92, 34)])),
   L(ell(-6, 22, 4, 8), 'shade', 'b', True, True), L(ell(106, 22, 4, 8), 'shade', 'b', True, True),
   L(outline([(12, 96), (8, 50), (16, 18), (50, 4), (84, 18), (92, 50), (88, 96), (80, 96), (78, 66), (22, 66), (20, 96)])),
   L(outline([(60, 6), (84, 18), (92, 50), (88, 94), (82, 66)]), 'shade', 'b', False)] +
  [strand([(x, 20), (x, 60)], 'deep', 'b', 1.0) for x in (28, 40, 52, 64, 76)],
  [L(outline([(36, 22), (26, 12), (20, 18), (28, 30)])),
   L(outline([(56, 62), (60, 50), (84, 50), (92, 30), (76, 8), (50, 2), (24, 8), (6, 28), (2, 60), (6, 96), (30, 98), (50, 96), (54, 80)])),
   strand([(30, 20), (24, 90)], 'deep', 'b', 1.0), strand([(50, 10), (46, 92)], 'deep', 'b', 1.0)],
  [L(outline([(8, 22), (-6, 14), (-8, 30), (8, 34)])), L(outline([(92, 22), (106, 14), (108, 30), (92, 34)])),
   L(outline([(10, 98), (8, 50), (16, 18), (50, 4), (84, 18), (92, 50), (90, 98), (50, 100)])),
   L(outline([(60, 6), (84, 18), (92, 50), (88, 96), (70, 98)]), 'shade', 'b', False)])

# Ian Flappable: melena larga rubia pálida ondulada con mechones que se rizan hacia fuera y un flequillo que le tapa el
# ojo derecho; el otro ojo, lila con espiral; sonrisa tranquila
C('ian-flappable', 'normal', P('#ecdc9a', '#f6dcc0', iris='#8a72b4', shade='#c8b474', deep='#a08a50'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=93, eye_sep=14, hairline=[(6, 70), (18, 52), (32, 44), (50, 42), (68, 44), (82, 52), (94, 70)]),
  [L(outline([(6, 108), (-4, 84, 1), (6, 76), (0, 50), (-8, 34, 1), (6, 30), (16, 10), (40, -4), (66, 0), (88, 14), (98, 40), (108, 50, 1), (98, 58), (100, 84),
              (110, 96, 1), (94, 108), (84, 86), (16, 86)])),
   L(outline([(60, 0), (86, 14), (98, 42), (98, 100), (86, 80)]), 'shade', 'b', False),
   L(outline([(6, 30), (-4, 18), (-6, 0, 1), (2, 16), (12, 22)]), 'mid', 'b'),
   L(outline([(16, 40), (40, 30), (54, 40), (58, 60), (50, 82), (40, 100, 1), (34, 80), (26, 60), (18, 54)]), 'mid', 'f'),
   strand([(30, 40), (42, 64), (40, 90)], 'deep', 'f', 1.0)],
  [L(outline([(56, 60), (64, 46), (86, 44), (96, 24), (82, 4), (54, -4), (26, 2), (8, 22), (2, 50), (-6, 70, 1), (4, 80), (0, 104, 1), (16, 100), (26, 112, 1),
              (34, 96), (46, 80), (52, 68)])),
   L(outline([(74, 40), (94, 38), (96, 56), (90, 70, 1), (84, 54)]), 'mid', 'f'), strand([(40, 6), (24, 50), (20, 96)], 'deep', 'b', 1.0)],
  [L(outline([(6, 110), (-4, 84, 1), (6, 76), (0, 50), (-8, 34, 1), (6, 30), (16, 10), (40, -4), (66, 0), (88, 14), (98, 40), (108, 50, 1), (98, 58), (100, 84),
              (110, 96, 1), (94, 110), (76, 100, 1), (60, 112, 1), (44, 100, 1), (28, 112, 1)])),
   L(outline([(60, 0), (86, 14), (98, 42), (98, 100), (74, 100)]), 'shade', 'b', False)])

# Ian "Infantry" Fountry: casco gris verdoso en forma de huevo con una corona de hojas verdes, que le tapa los ojos; pelo
# naranja en llamas a los lados, nariz grande y sonrisa enorme de dientes
EGG, EGGD, LEAF = _c('#a8ae94'), _c('#868c74'), _c('#3a8a3a')
def _wreath(view):
    xs = [(18, 56), (28, 50), (38, 48), (50, 46), (62, 48), (72, 50), (82, 56)] if view != 'side' else [(30, 56), (48, 52), (66, 52), (84, 54)]
    return [L(outline([(x - 6, y + 2), (x - 4, y - 6), (x + 2, y - 10, 1), (x + 6, y - 2), (x + 2, y + 6)]), LEAF, 'f', True, True) for x, y in xs]
C('ian-infantry-fountry', 'normal', P('#e0602a', '#d89a5a', shade='#b8401e'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, face_front=face(w=4, chin=104, jaw=4)),
  [L(outline([(16, 66), (-8, 56, 1), (4, 66), (-10, 76, 1), (6, 78), (-2, 90, 1), (16, 84)])), L(outline([(84, 66), (108, 56, 1), (96, 66), (110, 76, 1), (94, 78), (102, 90, 1), (84, 84)])),
   L(outline([(12, 70), (12, 40), (24, 10), (42, -10), (50, -14, 1), (58, -10), (76, 10), (88, 40), (88, 70), (50, 66)]), EGG, 'f'),
   L(outline([(58, -8), (78, 12), (88, 40), (86, 68), (74, 66)]), EGGD, 'f', False), strand([(50, -12), (48, 20), (52, 40)], EGGD, 'f', 1.4)] + _wreath('front') +
  [L(outline([(44, 74), (56, 74), (56, 88), (44, 88)]), 'skin_d', 'f', True, True),
   L(outline([(28, 92), (50, 96), (72, 92), (68, 102), (50, 106), (32, 102)]), WHITE, 'f', True, True)] +
  [L([(x, 93), (x, 104)], OUTC, 'f', False, False, 0.8) for x in (36, 43, 50, 57, 64)],
  [L(outline([(40, 66), (20, 58, 1), (28, 70), (14, 80, 1), (30, 82), (24, 96, 1), (42, 86)])),
   L(outline([(6, 74), (4, 40), (20, 10), (40, -10), (50, -14, 1), (62, -8), (80, 10), (92, 36), (94, 70), (50, 70)]), EGG, 'f')] + _wreath('side') +
  [L(outline([(88, 74), (98, 76), (98, 88), (88, 88)]), 'skin_d', 'f', True, True), L(outline([(80, 94), (94, 92), (92, 102), (80, 102)]), WHITE, 'f', True, True)],
  [L(outline([(12, 76), (12, 40), (24, 10), (42, -10), (50, -14, 1), (58, -10), (76, 10), (88, 40), (88, 76), (50, 72)]), EGG, 'f'),
   L(outline([(58, -8), (78, 12), (88, 40), (86, 74), (74, 72)]), EGGD, 'f', False)] + _wreath('back') +
  [L(outline([(14, 74), (-6, 66, 1), (4, 80), (-4, 94, 1), (20, 88)])), L(outline([(86, 74), (106, 66, 1), (96, 80), (104, 94, 1), (80, 88)]))])

# Ian Pentam-Bick: pelo rojo anaranjado en mechones largos de punta echados hacia su izquierda, con una coleta alta que sale
# hacia atrás y un flequillo que le cruza la cara; ojos ámbar y sonrisa
C('ian-pentam-bick', 'normal', P('#e04a1e', '#f8d8b4', iris='#b87020', shade='#b8341a', deep='#8a2412'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 66), (16, 50), (30, 44), (50, 42), (70, 44), (84, 50), (94, 66)]),
  [L(outline([(30, 10), (36, -14), (56, -22, 1), (52, -8), (60, 4)])),
   L(outline([(12, 80), (8, 44), (18, 16), (40, 2), (66, 2), (88, 14), (108, 18, 1), (96, 30), (106, 46, 1), (92, 50), (98, 70, 1), (88, 74), (86, 92, 1), (80, 70),
              (18, 70)])),
   L(outline([(62, 4), (88, 14), (96, 30), (92, 50), (84, 68), (74, 34)]), 'shade', 'b', False),
   L(outline([(20, 46), (36, 34), (62, 36), (80, 50), (90, 70, 1), (70, 58), (64, 78, 1), (56, 56), (44, 52), (30, 60, 1)]), 'mid', 'f'),
   strand([(40, 40), (58, 50), (66, 70)], 'deep', 'f', 1.0)],
  [L(outline([(54, 58), (62, 46), (84, 46), (100, 30, 1), (88, 24), (96, 8, 1), (74, 6), (60, -6), (40, -18, 1), (40, -4), (18, 4), (-4, -6, 1), (6, 14), (2, 40),
              (6, 70), (20, 80), (36, 76), (46, 66)])),
   L(outline([(70, 40), (94, 40), (100, 58, 1), (88, 56)]), 'mid', 'f')],
  [L(outline([(30, 10), (36, -14), (56, -22, 1), (52, -8), (60, 4)])),
   L(outline([(12, 84), (8, 44), (18, 16), (40, 2), (66, 2), (88, 14), (108, 18, 1), (96, 30), (106, 46, 1), (92, 50), (94, 84), (74, 78, 1), (50, 86, 1), (28, 78, 1)])),
   L(outline([(62, 4), (88, 14), (96, 30), (92, 50), (90, 80), (70, 40)]), 'shade', 'b', False)])

# Indira Patil (portera): pañuelo crema que le envuelve la cabeza y los hombros, con una franja roja anaranjada; un bindi
# rojo en la frente, piel morena, ojos negros grandes con pestañas y sonrisa
SCV, SCR = _c('#f0e2c8'), _c('#d8502a')
C('indira-patil', 'chica', P('#2a1e1a', '#b47a4a', iris='#1e1a1a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=False),
  [L(outline([(4, 112), (2, 60), (10, 18), (50, -2), (90, 18), (98, 60), (96, 112), (80, 104), (82, 60), (18, 60), (20, 104)]), SCV, 'b'),
   L(outline([(16, 64), (18, 36), (34, 18), (50, 14), (66, 18), (82, 36), (84, 64), (74, 50), (50, 40), (26, 50)]), SCR, 'b', False),
   L(outline([(16, 100), (40, 112), (60, 112), (84, 100), (94, 114), (60, 124), (40, 124), (6, 114)]), SCR, 'f'),
   L(outline([(10, 108), (40, 116), (60, 116), (90, 108), (92, 112), (60, 120), (40, 120), (8, 112)]), SCV, 'f', False),
   L(ell(50, 60, 2.2, 2.2), (200, 30, 40, 255), 'f', False)] + lashes(),
  [L(outline([(2, 114), (-2, 60), (8, 16), (46, -2), (78, 8), (92, 30), (86, 44), (62, 42), (52, 60), (52, 104), (30, 112)]), SCV, 'f'),
   L(outline([(62, 44), (86, 42), (92, 32), (90, 28), (84, 38), (62, 38), (54, 56), (56, 100), (52, 100), (50, 58)]), SCR, 'f', False),
   L(outline([(40, 104), (70, 106), (94, 110), (90, 120), (40, 118)]), SCR, 'f')] + lash_side(),
  [L(outline([(4, 114), (2, 60), (10, 18), (50, -2), (90, 18), (98, 60), (96, 114), (50, 118)]), SCV, 'f'),
   L(outline([(6, 104), (50, 112), (94, 104), (96, 114), (50, 120), (4, 114)]), SCR, 'f', False)])

# Indy "Glacial" Ferrante: pelo castaño rojizo en mechones gruesos y esponjosos en todas direcciones; gafas rectangulares
# plateadas sobre unos ojos ámbar, con cordones que le cuelgan hasta el cuello; pecas y sonrisa
GLS = _c('#b4b0a8')
def _rect_goggles(view, y=74):
    if view == 'front':
        return [L(outline([(24, y - 6), (44, y - 6), (44, y + 6), (24, y + 6)]), GLS, 'f', True, True), L(outline([(56, y - 6), (76, y - 6), (76, y + 6), (56, y + 6)]), GLS, 'f', True, True),
                L(outline([(28, y - 3), (40, y - 3), (40, y + 3), (28, y + 3)]), WHITE, 'f', False), L(outline([(60, y - 3), (72, y - 3), (72, y + 3), (60, y + 3)]), WHITE, 'f', False),
                L(ell(34, y, 2.6, 2.6), _c('#c8801e'), 'f', False), L(ell(66, y, 2.6, 2.6), _c('#c8801e'), 'f', False),
                L([(44, y), (56, y)], GLS, 'f', False, False, 2.4), L([(24, y), (14, y - 2)], GLS, 'f', False, False, 2.4), L([(76, y), (86, y - 2)], GLS, 'f', False, False, 2.4),
                L(quad((14, y), (12, y + 30), (22, y + 44)), BLACK, 'f', False, False, 1.4), L(quad((86, y), (88, y + 30), (78, y + 44)), BLACK, 'f', False, False, 1.4)]
    return [L(outline([(76, y - 6), (90, y - 6), (90, y + 6), (76, y + 6)]), GLS, 'f', True, True), L(ell(84, y, 2.4, 2.4), _c('#c8801e'), 'f', False),
            L([(76, y), (50, y - 2)], GLS, 'f', False, False, 2.4), L(quad((50, y), (46, y + 30), (56, y + 44)), BLACK, 'f', False, False, 1.4)]
C('indy-glacial-ferrante', 'normal', P('#a04a32', '#f6c896', iris='#c8801e', shade='#7e3624', deep='#5e2618'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=92, hairline=hl(6, 62, 48, 58, jit=3, seed=41)),
  dome('front', top=-4, w=52, cy=46, n=10, amp=10, soft=True, seed=42, sb=66) + _rect_goggles('front') + freckles(86, 22),
  dome('side', top=-4, w=50, cy=46, n=10, amp=10, soft=True, seed=42, nape=86, fr=50) + _rect_goggles('side'),
  dome('back', top=-4, w=52, cy=46, n=10, amp=10, soft=True, seed=42, nape=86))

# Inke Marks (portera): pelo verde lima echado hacia su derecha en ondas que le caen por un lado hasta el hombro; un tatuaje
# negro tribal le baja por la mitad izquierda de la cara; ojos rojos con pestañas, boca en O con un plato labial naranja y
# pendientes grandes crema
TAT = _c('#1e1a1a')
C('inke-marks', 'chica', P('#8ac83a', '#fae6c8', iris='#a82a1e', shade='#6aa42a', deep='#4a7a1e', brow='#5aa02a'),
  F(eyes='big', brows=False, mouth='none', hairline=[(6, 70), (14, 50), (30, 40), (50, 36), (70, 40), (84, 48), (94, 64)]),
  [L(outline([(4, 108), (-2, 80), (4, 50), (12, 22), (34, 4), (62, 0), (84, 12), (92, 34), (88, 54), (70, 42), (40, 46), (24, 60), (22, 96), (16, 112)])),
   L(outline([(60, 2), (84, 14), (90, 34), (86, 50), (72, 32)]), 'shade', 'b', False),
   L(outline([(70, 44), (78, 46), (80, 62), (76, 74), (78, 88), (66, 104, 1), (70, 86), (72, 72), (70, 58)]), TAT, 'f', False),
   L([(26, 64), (40, 66)], _c('#5aa02a'), 'f', False, False, 2.4), L([(74, 64), (60, 66)], _c('#5aa02a'), 'f', False, False, 2.4),
   L(ell(50, 94, 4, 5), _c('#e88a3a'), 'f', True, True), L(ell(50, 94, 2, 2.6), _c('#8a3a2a'), 'f', False),
   L(ell(17, 88, 5, 5), CRM, 'f'), L(ell(83, 88, 5, 5), CRM, 'f')] + lashes(),
  [L(outline([(54, 58), (62, 44), (80, 40), (92, 26), (76, 6), (50, 0), (24, 6), (6, 26), (2, 50), (0, 80), (6, 110), (20, 104), (24, 80), (40, 70)])),
   L(ell(48, 88, 4.6, 4.6), CRM, 'f'), L(ell(88, 94, 3, 4), _c('#e88a3a'), 'f', True, True)] + lash_side(),
  [L(outline([(6, 110), (0, 80), (8, 40), (20, 14), (50, 2), (80, 14), (92, 40), (92, 80), (70, 84), (40, 92), (24, 112)])),
   L(outline([(58, 4), (82, 16), (92, 42), (90, 78), (70, 80)]), 'shade', 'b', False)])

# Irina Swift: afro crema esponjoso y un pañuelo verde con lunares naranjas atado sobre la cabeza; piel morena, ojos grandes
# redondos con pestañas, boquita en O
AF, BND, DOT = _c('#f4d8a0'), _c('#3a7a2a'), _c('#e0602a')
def _bandana(view):
    if view == 'front':
        out = [L(outline([(12, 62), (14, 36), (30, 22), (50, 18), (70, 22), (86, 36), (88, 62), (80, 70), (78, 50), (50, 46), (22, 50), (20, 70)]), BND, 'f')]
        out += [L(ell(x, y, 4.6, 4), DOT, 'f', False) for x, y in ((26, 36), (40, 28), (54, 26), (68, 30), (80, 40), (34, 44), (62, 40), (18, 50), (84, 54))]
        return out
    if view == 'side':
        return [L(outline([(4, 62), (8, 32), (28, 18), (54, 16), (80, 24), (90, 40), (86, 50), (50, 48), (14, 66)]), BND, 'f')] + \
            [L(ell(x, y, 4.6, 4), DOT, 'f', False) for x, y in ((20, 36), (38, 26), (58, 26), (76, 34), (30, 48), (54, 40))]
    return [L(outline([(10, 70), (12, 36), (30, 22), (50, 18), (70, 22), (88, 36), (90, 70), (50, 74)]), BND, 'f')] + \
        [L(ell(x, y, 4.6, 4), DOT, 'f', False) for x, y in ((26, 36), (44, 28), (62, 30), (76, 40), (34, 54), (56, 50), (74, 60), (20, 60))]
C('irina-swift', 'chica', P('#f4d8a0', '#b88050', iris='#1e1a1a', shade='#d8b478'),
  F(eyes='big', brows=False, mouth='none', hairline=[(6, 66), (20, 54), (34, 52), (50, 50), (66, 52), (80, 54), (94, 66)]),
  [L(curls(50, 30, (52, 34), 10))] + _bandana('front') + [L(ell(50, 94, 2.4, 3), (120, 50, 40, 255), 'f', True, True)] + lashes(),
  [L(curls(44, 30, (50, 34), 10))] + _bandana('side') + lash_side(),
  [L(curls(50, 34, (52, 38), 10))] + _bandana('back'))

# Isodoura Bouquet: pelo turquesa liso con raya a un lado, peinado hacia atrás y en una media melena que le llega a la
# mandíbula en mechones; ojos marrones y una sonrisa suave
C('isodoura-bouquet', 'chica', P('#5ac4c8', '#f8d8b8', iris='#8a5a2a', shade='#3aa0a4', deep='#2a7a7e'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 70), (14, 56), (26, 44), (40, 38), (60, 34), (76, 40), (88, 52), (94, 68)]),
  [L(outline([(10, 100), (8, 54), (14, 22), (36, 4), (64, 2), (86, 16), (94, 44), (92, 100), (84, 84), (16, 84)])),
   L(outline([(64, 4), (86, 18), (94, 46), (92, 98), (84, 70)]), 'shade', 'b', False),
   strand([(40, 4), (30, 40), (20, 80)], 'deep', 'b', 1.0), strand([(62, 4), (76, 40), (84, 84)], 'deep', 'b', 1.0)],
  [L(outline([(56, 58), (64, 44), (84, 40), (94, 24), (78, 4), (50, -2), (24, 4), (6, 24), (2, 60), (8, 98), (24, 100), (40, 84), (50, 70)])),
   strand([(46, 2), (28, 40), (20, 96)], 'deep', 'b', 1.0)],
  [L(outline([(10, 100), (8, 54), (14, 22), (36, 4), (64, 2), (86, 16), (94, 44), (92, 100), (76, 94, 1), (62, 102, 1), (48, 94, 1), (34, 102, 1), (20, 94, 1)])),
   L(outline([(60, 4), (86, 18), (94, 46), (92, 98), (70, 70)]), 'shade', 'b', False)])

# Jacko Lenton: una calabaza de Halloween naranja le tapa toda la cabeza, con los ojos y la boca recortados y un rabito
# verde enroscado arriba
PMP, PMD, STM = _c('#e8902a'), _c('#c06c18'), _c('#4a8a3a')
def _pumpkin(view):
    out = [L(outline([(4, 108), (-2, 70), (4, 30), (24, 6), (50, 2), (76, 6), (96, 30), (102, 70), (96, 108), (50, 114)]), PMP, 'f')]
    for x in ((26, 40) if view != 'side' else (30,)):
        out.append(strand([(x, 8), (x - 6, 60), (x, 110)], PMD, 'f', 1.6))
        out.append(strand([(100 - x, 8), (106 - x, 60), (100 - x, 110)], PMD, 'f', 1.6))
    out += [L(quad((50, 4), (46, -6), (56, -12)), STM, 'f', False, False, 3.0), L(quad((56, -12), (66, -14), (62, -6)), STM, 'f', False, False, 1.6)]
    if view == 'front':
        out += [L([(24, 58), (34, 44), (42, 58)], BLACK, 'f', False), L([(58, 58), (66, 44), (76, 58)], BLACK, 'f', False),
                L([(18, 72), (30, 80), (36, 76), (40, 84), (50, 80), (60, 84), (64, 76), (70, 80), (82, 72), (76, 92), (64, 88), (50, 96), (36, 88), (24, 92)], BLACK, 'f', False)]
    elif view == 'side':
        out += [L([(80, 58), (88, 44), (94, 58)], BLACK, 'f', False), L([(76, 76), (98, 72), (96, 90), (80, 92)], BLACK, 'f', False)]
    return out
C('jacko-lenton', 'normal', P('#3a2a20', '#c08a5a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False), _pumpkin('front'), _pumpkin('side'), _pumpkin('back'))

# Jeanie "Tajine" Tanner: capucha y bufanda azul marino casi negro que le envuelven la cabeza y el cuello; asoman mechones
# gris azulado por la frente; piel oscura, ojos ámbar y boca seria
JH = _c('#22223a')
C('jeanie-tajine-tanner', 'chica', P('#9ab4c8', '#8a5a34', iris='#d8a020', shade='#7a94a8'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=95, hairline=[(6, 66), (20, 56), (30, 52), (42, 58), (50, 50), (58, 58), (70, 52), (80, 56), (94, 66)]),
  [L(outline([(4, 116), (2, 60), (10, 16), (50, -4), (90, 16), (98, 60), (96, 116), (80, 108), (82, 62), (18, 62), (20, 108)]), JH, 'b'),
   L(outline([(20, 90), (16, 60), (26, 40), (50, 32), (74, 40), (84, 60), (80, 90), (76, 66), (24, 66)])),
   L(outline([(18, 100), (40, 112), (60, 112), (84, 98), (90, 120), (56, 128), (30, 128), (10, 118)]), JH, 'f')],
  [L(outline([(2, 116), (-2, 60), (8, 16), (46, -4), (80, 8), (92, 30), (86, 46), (62, 44), (54, 62), (54, 104), (30, 116)]), JH, 'f'),
   L(outline([(62, 44), (86, 44), (88, 58, 1), (76, 52)]), 'mid', 'f'),
   L(outline([(40, 104), (70, 106), (94, 108), (90, 124), (40, 122)]), JH, 'f')],
  [L(outline([(4, 118), (2, 60), (10, 16), (50, -4), (90, 16), (98, 60), (96, 118), (50, 122)]), JH, 'f'),
   L(outline([(60, 0), (86, 16), (96, 58), (94, 116), (72, 118)]), _c('#16162a'), 'f', False)])

# Jen "Gemini" Miniver: pelo castaño oscuro con flequillo recto y dos moños enormes enrollados a los lados (con las puntas
# rosas) y una diadema verde agua con lazos; ojos azul claro, cejas de punto y boquita en O
TEAL, PNK = _c('#5ab4b0'), _c('#d89a9a')
def _buns(view):
    if view == 'front':
        return [L(ell(10, 50, 14, 15)), L(ell(90, 50, 14, 15)), L(ell(6, 50, 7, 8), PNK, 'b', True, True), L(ell(94, 50, 7, 8), PNK, 'b', True, True),
                strand([(2, 50), (6, 44), (10, 50), (6, 56)], 'deep', 'b', 1.0), strand([(98, 50), (94, 44), (90, 50), (94, 56)], 'deep', 'b', 1.0)]
    if view == 'side':
        return [L(ell(40, 46, 16, 16)), L(ell(40, 46, 8, 8), PNK, 'b', True, True)]
    return [L(ell(10, 50, 14, 15)), L(ell(90, 50, 14, 15))]
C('jen-gemini-miniver', 'chica', P('#4a3028', '#fae8d0', iris='#6aa4b4', shade='#382218', deep='#28160e'),
  F(eyes='big', brows=False, mouth='none', hairline=[(6, 64), (14, 60), (30, 60), (50, 60), (70, 60), (86, 60), (94, 64)]),
  _buns('front') + [L(outline([(14, 84), (12, 44), (22, 18), (50, 8), (78, 18), (88, 44), (86, 84), (78, 66), (22, 66)])),
                    L(outline([(14, 34), (30, 22), (50, 18), (70, 22), (86, 34), (86, 40), (70, 28), (50, 24), (30, 28), (14, 40)]), TEAL, 'f'),
                    L(outline([(18, 30), (10, 14), (24, 18)]), TEAL, 'f'), L(outline([(82, 30), (90, 14), (76, 18)]), TEAL, 'f'),
                    L(ell(36, 58, 1.6, 1.6), OUTC, 'f', False), L(ell(64, 58, 1.6, 1.6), OUTC, 'f', False),
                    L(ell(50, 94, 2, 2.6), (150, 70, 70, 255), 'f', True, True)],
  [L(outline([(56, 60), (62, 48), (84, 44), (90, 26), (74, 10), (50, 4), (24, 10), (8, 30), (4, 60), (14, 80), (34, 82), (48, 72)]))] + _buns('side') +
  [L(outline([(10, 30), (40, 18), (80, 18), (90, 26), (86, 30), (40, 24), (12, 36)]), TEAL, 'f')],
  _buns('back') + [L(outline([(14, 86), (12, 44), (22, 18), (50, 8), (78, 18), (88, 44), (86, 86), (50, 90)])),
                   L(outline([(14, 36), (50, 26), (86, 36), (86, 42), (50, 32), (14, 42)]), TEAL, 'f')])

# Jen "Heart" Erris (portera): un gorro enorme rojo con forma de corazón y volantes crema, y una máscara rosa de cerdo con
# dos agujeros rojos que le tapa toda la cara
HT, HTD, FR, PIG, PGD = _c('#d02028'), _c('#a0141c'), _c('#f0dcc0'), _c('#f0a0b0'), _c('#c87888')
def _heart(view):
    if view == 'side':
        return [L(outline([(0, 70), (-4, 30), (10, 4), (40, -12), (70, -6), (90, 14), (94, 40), (84, 56), (40, 60), (8, 80)]), HT, 'f'),
                L(curls(54, 52, (30, 10), 8), FR, 'f')]
    hat = L(outline([(50, 14), (36, -4), (12, -8), (-4, 14), (-2, 46), (16, 70), (84, 70), (102, 46), (104, 14), (88, -8), (64, -4)]), HT, 'f')
    return [hat, L(outline([(60, 4), (88, -4), (102, 18), (98, 46), (84, 66), (74, 30)]), HTD, 'f', False), L(curls(50, 56, (36, 12), 9), FR, 'f')]
C('jen-heart-erris', 'chica', P('#f0dcc0', '#f6d0b0'),
  F(eyes='none', brows=False, mouth='none', hairline=False),
  _heart('front') + [L(outline([(18, 62), (50, 56), (82, 62), (80, 96), (50, 108, 1), (20, 96)]), PIG, 'f'), strand([(50, 58), (50, 104)], PGD, 'f', 1.2),
                     L(ell(36, 80, 6, 8), _c('#b80c18'), 'f', True, True), L(ell(64, 80, 6, 8), _c('#b80c18'), 'f', True, True)],
  _heart('side') + [L(outline([(64, 60), (96, 60), (100, 92), (80, 104, 1), (66, 96)]), PIG, 'f'), L(ell(88, 80, 4, 7), _c('#b80c18'), 'f', True, True)],
  _heart('back') + [L(outline([(16, 66), (84, 66), (84, 76), (16, 76)]), PGD, 'f')])

# Jen "Liberty" Derites: melena roja de rizos muy abultada con una diadema azul y tres horquillas de estrella amarillas y
# crema; ojos lilas grandes, marcas rojas en la frente y sonrisa
STR, STC, HB = _c('#f0c030'), _c('#f2e6c4'), _c('#2a4aa0')
def star(cx, cy, r, c, z='f'):
    import math
    pts = []
    for i in range(10):
        a = -math.pi / 2 + math.pi * i / 5
        k = r if i % 2 == 0 else r * 0.45
        pts.append((cx + k * math.cos(a), cy + k * math.sin(a)))
    return L(pts, c, z, True, True)
C('jen-liberty-derites', 'chica', P('#c84a3a', '#fadcc0', iris='#7a5ac0', shade='#a03428', deep='#7a2418'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, hairline=[(6, 66), (16, 54), (30, 48), (50, 46), (70, 48), (84, 54), (94, 66)]),
  [L(curls(50, 50, (56, 50), 11)), L(outline([(14, 50), (30, 36), (50, 32), (70, 36), (86, 50), (84, 56), (70, 44), (50, 40), (30, 44), (16, 56)]), HB, 'f'),
   star(24, 44, 9, STC), star(34, 30, 7, STR), star(76, 46, 7, STR),
   L([(38, 66), (42, 62)], _c('#c83a3a'), 'f', False, False, 1.4), L([(62, 66), (58, 62)], _c('#c83a3a'), 'f', False, False, 1.4)],
  [L(curls(30, 52, (36, 48), 9)), L(outline([(50, 60), (60, 44), (80, 40), (78, 26), (56, 8), (40, 10)])),
   L(outline([(6, 40), (40, 28), (76, 30), (80, 38), (40, 36), (8, 48)]), HB, 'f'), star(66, 34, 7, STR)],
  [L(curls(50, 54, (56, 52), 11)), L(outline([(10, 48), (50, 40), (90, 48), (90, 54), (50, 46), (10, 54)]), HB, 'f'), star(20, 46, 8, STC), star(80, 46, 7, STR)])

# Jib Spinaker: pelo verde grisáceo corto con un flequillo de puntas y un rizo que se levanta arriba; gafas de pasta negra
# con el cristal derecho tapado de blanco; cara pálida y boca seria
C('jib-spinaker', 'normal', P('#4a6a5a', '#f8dcbc', iris='#3a2a2a', shade='#34503e', deep='#22382a'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=95, eye_sep=14,
    hairline=[(6, 62), (16, 50), (24, 58), (32, 48), (42, 62), (50, 50), (58, 60), (68, 48), (76, 56), (84, 48), (94, 62)]),
  dome('front', top=0, w=48, cy=44, n=7, amp=8, seed=51, sb=66) + [L(quad((60, 2), (72, -6), (78, 0)), 'mid', 'b', False, False, 3.2)] +
  [L(outline([(22, 70), (44, 68), (44, 80), (24, 80)]), BLACK, 'f', False, False, 2.2), L(outline([(56, 68), (80, 68), (78, 82), (56, 80)]), WHITE, 'f', True, True),
   L([(44, 72), (56, 72)], BLACK, 'f', False, False, 2.0), L([(22, 70), (14, 68)], BLACK, 'f', False, False, 2.0), L([(80, 70), (86, 68)], BLACK, 'f', False, False, 2.0)],
  dome('side', top=0, w=46, cy=44, n=7, amp=8, seed=51, nape=84, fr=48) + [L(outline([(74, 68), (90, 68), (90, 82), (76, 82)]), BLACK, 'f', False, False, 2.2),
                                                                          L([(74, 72), (50, 70)], BLACK, 'f', False, False, 2.0)],
  dome('back', top=0, w=48, cy=44, n=7, amp=8, seed=51, nape=84) + [L(quad((60, 2), (72, -6), (78, 0)), 'mid', 'b', False, False, 3.2)])

# Joachim "Sumo" Zooner: luchador de sumo enorme; un paño morado le cubre la cabeza y cae a los lados en tela lila hasta los
# hombros; piel tostada, orejas grandes, mandíbula ancha y dientes apretados con la boca hacia abajo
PUR, LIL = _c('#4a2a6a'), _c('#d0c4d8')
C('joachim-sumo-zooner', 'corpulento', P('#4a2a6a', '#b4743e', iris='#1e1a1a'),
  F(eyes='dot', brows='angry', mouth='none', face_front=face(w=10, chin=112, jaw=10), face_side=face_side(chin=12, jaw=10), big_ears=3, ear_out=10, hairline=False),
  [L(outline([(4, 116), (2, 70), (8, 40), (20, 30), (80, 30), (92, 40), (98, 70), (96, 116), (88, 110), (84, 60), (16, 60), (12, 110)]), LIL, 'b'),
   L(outline([(14, 50), (16, 30), (32, 18), (50, 14), (68, 18), (84, 30), (86, 50), (68, 48), (50, 56), (32, 48)]), PUR, 'f'),
   L(outline([(16, 46), (50, 40), (84, 46), (84, 52), (50, 46), (16, 52)]), LIL, 'f', False),
   L(outline([(34, 92), (50, 88), (66, 92), (64, 100), (50, 96), (36, 100)]), WHITE, 'f', True, True),
   L([(38, 94), (62, 94)], OUTC, 'f', False, False, 0.8), L(quad((38, 104), (50, 98), (62, 104)), OUTC, 'f', False, False, 1.6)],
  [L(outline([(2, 116), (-2, 60), (6, 30), (40, 20), (54, 60), (52, 110), (30, 118)]), LIL, 'f'),
   L(outline([(6, 52), (10, 26), (32, 12), (54, 10), (76, 18), (90, 34), (90, 50), (60, 54)]), PUR, 'f'),
   L(outline([(84, 92), (94, 90), (94, 98), (84, 98)]), WHITE, 'f', True, True)],
  [L(outline([(4, 118), (2, 60), (14, 30), (86, 30), (98, 60), (96, 118), (50, 122)]), LIL, 'f'),
   L(outline([(14, 54), (16, 30), (32, 18), (50, 14), (68, 18), (84, 30), (86, 54), (50, 60)]), PUR, 'f')])

# Joe Java: pelo verde oscuro rapado; piel morena, cara grande, nariz enorme marrón, ojos entornados y una sonrisa de oreja a
# oreja con los dientes
C('joe-java', 'corpulento', P('#1e5040', '#a07858', iris='#1e1a1a'),
  F(eyes='dot', brows=True, mouth='none', face_front=face(w=8, chin=108, jaw=6), face_side=face_side(chin=8, jaw=6, nose=8), ear_out=8,
    hairline=[(6, 54), (16, 44), (30, 38), (50, 36), (70, 38), (84, 44), (94, 54)]),
  [L(outline([(12, 60), (12, 34), (28, 14), (50, 8), (72, 14), (88, 34), (88, 60), (70, 48), (30, 48)]))] +
  [L(outline([(40, 70), (50, 66), (60, 70), (64, 86), (50, 90), (36, 86)]), _c('#7a5236'), 'f', True, True),
   L(outline([(30, 94), (50, 98), (70, 94), (66, 104), (50, 108), (34, 104)]), WHITE, 'f', True, True), L([(32, 99), (68, 99)], OUTC, 'f', False, False, 0.8),
   L(quad((24, 70), (34, 68), (44, 72)), OUTC, 'f', False, False, 2.0), L(quad((76, 70), (66, 68), (56, 72)), OUTC, 'f', False, False, 2.0)],
  [L(outline([(52, 52), (60, 40), (80, 34), (86, 22), (70, 8), (46, 4), (22, 10), (6, 28), (4, 54), (16, 74), (34, 72), (46, 64)])),
   L(outline([(84, 70), (100, 80), (96, 90), (86, 88)]), _c('#7a5236'), 'f', True, True), L(outline([(80, 96), (94, 96), (92, 104), (80, 104)]), WHITE, 'f', True, True)],
  [L(outline([(12, 70), (12, 34), (28, 14), (50, 8), (72, 14), (88, 34), (88, 70), (50, 76)]))])

# Joe "Pigsy" Bajie: cara de cerdo rosa con el hocico grande, ojos entornados y boca de enfado; un pañuelo morado atado a la
# cabeza con las puntas que salen a los lados
PGK, PGN, BDN = _c('#e8a4a4'), _c('#c87a7e'), _c('#5a2a8a')
C('joe-pigsy-bajie', 'corpulento', P('#5a2a8a', '#e8a4a4', iris='#1e1a1a', skin_d='#cc8888'),
  F(eyes='dot', brows='angry', mouth='frown', mouth_y=100, face_front=face(w=10, chin=110, jaw=8), face_side=face_side(chin=10, jaw=8, nose=10), big_ears=2, ear_out=8,
    hairline=False),
  [L(outline([(14, 48), (16, 28), (32, 14), (50, 10), (68, 14), (84, 28), (86, 48), (70, 44), (50, 46), (30, 44)]), BDN, 'f'),
   L(outline([(14, 44), (-6, 52, 1), (4, 40), (-4, 30, 1), (16, 36)]), BDN, 'f'), L(outline([(86, 44), (106, 52, 1), (96, 40), (104, 30, 1), (84, 36)]), BDN, 'f'),
   L(ell(50, 84, 10, 8), PGN, 'f', True, True), L(ell(46, 84, 2, 3), (110, 50, 60, 255), 'f', False), L(ell(54, 84, 2, 3), (110, 50, 60, 255), 'f', False)],
  [L(outline([(6, 52), (10, 26), (32, 12), (54, 10), (76, 18), (88, 34), (88, 48), (50, 50)]), BDN, 'f'),
   L(outline([(10, 44), (-10, 40, 1), (0, 32), (-8, 22, 1), (12, 30)]), BDN, 'f'), L(outline([(86, 74), (100, 76), (100, 92), (86, 92)]), PGN, 'f', True, True)],
  [L(outline([(14, 56), (16, 28), (32, 14), (50, 10), (68, 14), (84, 28), (86, 56), (50, 60)]), BDN, 'f'),
   L(outline([(44, 56), (36, 74, 1), (50, 62), (64, 74, 1), (56, 56)]), BDN, 'f')])

# Joy Peach-Seeker: pelo negro con flequillo de mechones, recogido en una coleta lateral alta que le cae por la izquierda
# hasta el pecho, con un adorno rosa; cara pálida, ojos grises y cejas enfadadas
C('joy-peach-seeker', 'chica', P('#1e1a1e', '#fae6c8', iris='#8a8a90', shade='#2e2830', deep='#0e0a0e'),
  F(eyes='big', brows='angry', mouth='line', mouth_y=95, hairline=[(6, 66), (16, 52), (26, 46), (38, 52), (48, 44), (60, 50), (72, 44), (84, 52), (94, 66)]),
  [L(outline([(24, 10), (14, -6), (6, 10), (0, 40), (2, 80), (12, 110, 1), (16, 80), (14, 40), (22, 22)])),
   L(outline([(12, 76), (10, 40), (22, 14), (50, 6), (78, 14), (90, 40), (88, 76), (80, 64), (20, 64)])),
   L(outline([(84, 30), (96, 40), (98, 70), (86, 90), (88, 70), (84, 56)])),
   L(ell(78, 30, 5, 6), _c('#e8909a'), 'f', True, True), L(ell(84, 40, 4, 5), _c('#e8909a'), 'f', True, True)] + lashes(),
  [L(outline([(54, 60), (62, 46), (82, 42), (90, 24), (74, 8), (50, 2), (24, 6), (8, 24), (4, 52), (10, 70), (30, 72), (46, 66)])),
   L(ell(50, 30, 5, 6), _c('#e8909a'), 'f', True, True)] + lash_side(),
  [L(outline([(24, 10), (14, -6), (6, 10), (0, 40), (2, 80), (12, 110, 1), (16, 80), (14, 40), (22, 22)])),
   L(outline([(12, 80), (10, 40), (22, 14), (50, 6), (78, 14), (90, 40), (88, 80), (50, 84)])),
   L(ell(76, 30, 5, 6), _c('#e8909a'), 'f', True, True)])

# Jude "Diamond" Ellery: un gorro enorme en forma de rombo naranja y dorado y una máscara crema de pájaro con dos huecos
# oscuros que le tapa la cara; asoman las orejas
DH, DHD, DHY, SKM = _c('#d8701e'), _c('#8a3a14'), _c('#f0b030'), _c('#f2e2c4')
def _diamond(view):
    if view == 'side':
        return [L(outline([(4, 54), (40, -20, 1), (96, 50, 1), (80, 58), (40, 4), (18, 60)]), DH, 'f'),
                L(outline([(40, -14), (88, 48), (80, 52), (40, 2)]), DHY, 'f', False)]
    return [L(outline([(-6, 50, 1), (50, -24, 1), (106, 50, 1), (90, 62), (50, 16), (10, 62)]), DH, 'f'),
            L(outline([(2, 46), (50, -16), (98, 46), (92, 50), (50, -6), (8, 50)]), DHY, 'f', False),
            L(outline([(20, 56), (50, 24), (80, 56), (50, 48)]), DHD, 'f', False)]
C('jude-diamond-ellery', 'normal', P('#3a2a20', '#f6c896'),
  F(eyes='none', brows=False, mouth='line', mouth_y=100, hairline=False),
  _diamond('front') + [L(outline([(26, 62), (50, 52), (74, 62), (72, 84), (54, 98, 1), (46, 98, 1), (28, 84)]), SKM, 'f'),
                       L(ell(38, 74, 7, 8), _c('#5a2a1a'), 'f', False), L(ell(62, 74, 7, 8), _c('#5a2a1a'), 'f', False), strand([(50, 56), (50, 96)], (200, 180, 150, 255), 'f', 1.0)],
  _diamond('side') + [L(outline([(66, 60), (92, 62), (100, 84), (86, 96, 1), (70, 88)]), SKM, 'f'), L(ell(84, 74, 4, 7), _c('#5a2a1a'), 'f', False)],
  _diamond('back'))

# Judge "Justice" Jury: pelo verde oliva corto con una cresta de mechones en punta; un pañuelo rojo y azul con estrellas
# amarillas le tapa de la nariz al cuello; piel tostada, ojos negros enfadados y cejas gruesas
JR, JB = _c('#c8322a'), _c('#2a4aa8')
C('judge-justice-jury', 'normal', P('#6a6a2a', '#c88a52', iris='#1e1a1a'),
  F(eyes='sharp', brows=False, mouth='none', eye_y=72, hairline=[(6, 56), (16, 46), (30, 40), (50, 38), (70, 40), (84, 46), (94, 56)]),
  [L(outline([(12, 60), (12, 32), (28, 14), (50, 8), (72, 14), (88, 32), (88, 60), (70, 46), (30, 46)])),
   L(outline([(44, 12), (46, -16, 1), (50, 4), (54, -16, 1), (56, 12)]), 'deep'),
   L(outline([(14, 82), (50, 76), (86, 82), (88, 110), (50, 118), (12, 110)]), JB, 'f'),
   L(outline([(14, 82), (40, 78), (30, 100), (14, 108)]), JR, 'f', False),
   star(44, 96, 7, STR), star(70, 98, 8, STR)] + thick_brows(62, OUTC, 4.0, tilt=1.2),
  [L(outline([(52, 54), (60, 42), (80, 36), (86, 22), (70, 8), (46, 4), (22, 10), (6, 28), (4, 54), (16, 70), (34, 70), (46, 62)])),
   L(outline([(40, 12), (46, -16, 1), (52, 8)]), 'deep'),
   L(outline([(40, 86), (62, 80), (92, 80), (94, 106), (60, 118), (36, 112)]), JB, 'f'), star(74, 98, 6, STR)] + side_brow(62, OUTC, 4.0, 1.0),
  [L(outline([(12, 70), (12, 32), (28, 14), (50, 8), (72, 14), (88, 32), (88, 70), (50, 74)])),
   L(outline([(44, 12), (46, -16, 1), (50, 4), (54, -16, 1), (56, 12)]), 'deep'),
   L(outline([(12, 88), (50, 84), (88, 88), (88, 96), (50, 92), (12, 96)]), JB, 'f'), L(outline([(44, 90), (40, 110, 1), (50, 96), (60, 110, 1), (56, 90)]), JR, 'f')])

# Julia Mason (portera): melena gris azulado con grandes ondas arriba que le cae lisa hasta los hombros, con dos adornos
# redondos rojos a los lados; ojos rosas, cejas de preocupación y sonrisa tímida
RBD = _c('#d8401e')
C('julia-mason', 'chica', P('#7a9aa4', '#fae6c8', iris='#c0608a', shade='#5e7e88', deep='#46646c'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 66), (16, 54), (30, 46), (42, 50), (50, 44), (58, 50), (70, 46), (84, 54), (94, 66)]),
  [L(outline([(8, 112), (2, 70), (6, 40), (-2, 24, 1), (12, 18), (24, 2), (50, -4), (76, 2), (88, 18), (102, 24, 1), (94, 40), (98, 70), (92, 112), (82, 100), (84, 70),
              (16, 70), (18, 100)])),
   L(outline([(60, 0), (86, 16), (96, 40), (96, 100), (86, 80)]), 'shade', 'b', False),
   strand([(24, 8), (34, 22), (44, 18)], 'deep', 'b', 1.0), strand([(76, 8), (66, 22), (56, 18)], 'deep', 'b', 1.0),
   L(ell(16, 88, 5, 5), RBD, 'f', True, True), L(ell(84, 88, 5, 5), RBD, 'f', True, True)],
  [L(outline([(56, 58), (64, 44), (84, 42), (100, 26, 1), (84, 14), (60, 0), (30, 2), (8, 22), (0, 60), (4, 112), (20, 110), (36, 84), (50, 70)])),
   L(ell(48, 88, 5, 5), RBD, 'f', True, True)],
  [L(outline([(8, 114), (2, 70), (6, 40), (-2, 24, 1), (12, 18), (24, 2), (50, -4), (76, 2), (88, 18), (102, 24, 1), (94, 40), (98, 70), (92, 114), (50, 118)])),
   L(outline([(60, 0), (86, 16), (96, 40), (94, 112), (70, 114)]), 'shade', 'b', False), strand([(50, 4), (50, 110)], 'deep', 'b', 1.0)])

# Justice Gavel: pelo malva con dos moñitos arriba, flequillo recto en mechones y dos trenzas que le cuelgan por delante de
# las orejas; coloretes naranjas, ojos negros afilados con pestañas y boca enfadada
C('justice-gavel', 'chica', P('#a4789a', '#f6c896', iris='#1e1a1a', shade='#86607c', deep='#664860'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 62), (16, 56), (30, 54), (50, 54), (70, 54), (84, 56), (94, 62)]),
  [L(ell(26, 6, 10, 10)), L(ell(74, 6, 10, 10)),
   L(outline([(12, 80), (10, 40), (22, 14), (50, 8), (78, 14), (90, 40), (88, 80), (80, 66), (20, 66)])),
   L(outline([(16, 64), (22, 64), (22, 110), (16, 110)]), 'mid', 'f'), L(outline([(84, 64), (78, 64), (78, 110), (84, 110)]), 'mid', 'f')] +
  [strand([(16, y), (22, y + 4)], 'deep', 'f', 1.0) for y in (76, 86, 96)] + [strand([(84, y), (78, y + 4)], 'deep', 'f', 1.0) for y in (76, 86, 96)] +
  blush(84, 24, 6) + lashes(),
  [L(ell(46, 4, 10, 10)), L(outline([(54, 58), (62, 46), (82, 44), (90, 26), (74, 8), (50, 2), (24, 8), (8, 26), (4, 56), (12, 72), (32, 72), (46, 64)])),
   L(outline([(52, 66), (58, 66), (58, 112), (52, 112)]), 'mid', 'f')] + lash_side(),
  [L(ell(26, 6, 10, 10)), L(ell(74, 6, 10, 10)), L(outline([(12, 82), (10, 40), (22, 14), (50, 8), (78, 14), (90, 40), (88, 82), (50, 86)])),
   L(outline([(16, 70), (22, 70), (22, 110), (16, 110)]), 'mid', 'f'), L(outline([(84, 70), (78, 70), (78, 110), (84, 110)]), 'mid', 'f')])

# Kandhul Lai: moño negro en lo alto, un turbante de tela crema con un adorno rojo y una visera granate que le tapa medio
# ojo; pendientes grandes granates y boca seria
TC, VSR = _c('#ecdcc4'), _c('#7a1e1e')
def _kandhul(view):
    if view == 'side':
        return [L(ell(46, -6, 10, 11)), L(outline([(6, 56), (8, 26), (28, 10), (54, 8), (78, 16), (90, 36), (88, 52), (50, 52)]), TC, 'f'),
                L(outline([(56, 54), (90, 50), (104, 62, 1), (90, 64), (60, 62)]), VSR, 'f')]
    out = [L(ell(50, -6, 11, 12)), L(ell(50, 6, 4, 3), _c('#c8302a'), 'f', True, True),
           L(outline([(12, 56), (14, 30), (30, 14), (50, 10), (70, 14), (86, 30), (88, 56), (50, 52)]), TC, 'f'),
           strand([(20, 34), (50, 26), (80, 34)], (200, 180, 150, 255), 'f', 1.2), strand([(18, 44), (50, 38), (82, 44)], (200, 180, 150, 255), 'f', 1.2)]
    if view == 'front':
        out += [L(ell(50, 30, 5, 4), _c('#c8302a'), 'f', True, True),
                L(outline([(14, 54), (50, 50), (86, 54), (84, 66), (50, 72), (16, 66)]), VSR, 'f')]
    return out
C('kandhul-lai', 'normal', P('#1e1a1e', '#f0b46a', iris='#1e1a1a'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=94, eye_y=76, hairline=False),
  _kandhul('front') + [L(ell(14, 86, 4, 6), VSR, 'f', True, True), L(ell(86, 86, 4, 6), VSR, 'f', True, True)],
  _kandhul('side') + [L(ell(46, 86, 4, 6), VSR, 'f', True, True)],
  _kandhul('back') + [L(outline([(16, 54), (50, 50), (84, 54), (84, 64), (50, 60), (16, 64)]), VSR, 'f')])

# Karl Kappa (portero): un kappa: pelo azul de mechones con un plato verde en la coronilla; ojos negros redondos con los
# párpados verdes, nariz pequeña, pico amarillo y unas rayitas verdes en las mejillas
KPB, PLT, BEAK = _c('#2a4ab0'), _c('#8ac83a'), _c('#e0c838')
C('karl-kappa', 'normal', P('#2a4ab0', '#f6d0a8', iris='#1e1a1a', shade='#1e3488', deep='#14246a'),
  F(eyes='round', brows=False, mouth='none', hairline=[(6, 64), (16, 56), (24, 64), (34, 56), (42, 64), (50, 56), (58, 64), (66, 56), (76, 64), (84, 56), (94, 64)]),
  dome('front', top=4, w=50, cy=48, n=9, amp=10, seed=61, sb=86) +
  [L(ell(50, 6, 14, 6), PLT, 'b', True, True), L(ell(50, 4, 9, 3), _c('#b8e05a'), 'b', False),
   L([(28, 68), (42, 68)], _c('#3a8a3a'), 'f', False, False, 2.4), L([(58, 68), (72, 68)], _c('#3a8a3a'), 'f', False, False, 2.4),
   L(outline([(38, 92), (50, 86), (62, 92), (50, 98)]), BEAK, 'f', True, True), L([(40, 92), (60, 92)], OUTC, 'f', False, False, 0.8),
   L(ell(50, 84, 1.4, 1), OUTC, 'f', False)] +
  [L([(x, 84), (x + 2, 88)], _c('#3a8a3a'), 'f', False, False, 1.0) for x in (20, 24, 76, 80)],
  dome('side', top=4, w=48, cy=48, n=9, amp=10, seed=61, nape=92, fr=56) +
  [L(ell(50, 6, 12, 4), PLT, 'b', True, True), L(outline([(84, 90), (98, 92, 1), (86, 98)]), BEAK, 'f', True, True)],
  dome('back', top=4, w=50, cy=48, n=9, amp=10, seed=61, nape=92) + [L(ell(50, 6, 14, 6), PLT, 'b', True, True)])

# Kay "KMC" Emcee: pelo negro alborotado con un gran mechón amarillo arriba; gafas negras rectangulares, perilla y piel
# tostada (su retrato es un sprite pixelado de la DS)
C('kay-kmc-emcee', 'normal', P('#1e1a1e', '#d89a5a', iris='#1e1a1a', light='#f0d030'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=94, hairline=hl(5, 64, 46, 58, lean=2, jit=3, seed=71)),
  dome('front', top=-2, w=50, cy=46, n=9, amp=12, sweep=-0.4, seed=72, sb=74) +
  [L(outline([(48, 4), (60, -14, 1), (66, 4), (84, 0, 1), (80, 14), (92, 24, 1), (78, 30), (64, 40), (54, 28)]), 'light', 'f'),
   L(outline([(22, 70), (44, 70), (44, 80), (24, 80)]), BLACK, 'f', False, False, 2.4), L(outline([(56, 70), (78, 70), (76, 80), (56, 80)]), BLACK, 'f', False, False, 2.4),
   L([(44, 73), (56, 73)], BLACK, 'f', False, False, 2.0),
   L(outline([(44, 100), (50, 98), (56, 100), (52, 108, 1)]), 'mid', 'f')],
  dome('side', top=-2, w=48, cy=46, n=9, amp=12, sweep=-0.4, seed=72, nape=88, fr=50) +
  [L(outline([(54, 0), (70, -14, 1), (76, 6), (92, 10, 1), (82, 24), (66, 20)]), 'light', 'f'),
   L(outline([(74, 70), (90, 70), (90, 80), (76, 80)]), BLACK, 'f', False, False, 2.4), L([(74, 73), (50, 72)], BLACK, 'f', False, False, 2.0),
   L(outline([(80, 100), (88, 98), (86, 108, 1)]), 'mid', 'f')],
  dome('back', top=-2, w=50, cy=46, n=9, amp=12, sweep=-0.4, seed=72, nape=88) +
  [L(outline([(48, 4), (60, -14, 1), (66, 4), (84, 0, 1), (80, 14), (70, 24), (54, 20)]), 'light', 'f')])

# Keenan "Kigu" Guru: capucha de oso marrón con orejas redondas y dos ojos saltones arriba, con una fila de dientes que le
# enmarca la cara; asoma pelo verde claro ondulado; ojos redondos, coloretes y una boca cosida en rombo
BR, BRD, BRL = _c('#9a5a3a'), _c('#7a4228'), _c('#d8b08a')
def _bear(view):
    if view == 'side':
        return [L(ell(36, 2, 10, 10), BR, 'f'),
                L(outline([(2, 110), (-2, 60), (8, 16), (46, -6), (80, 6), (94, 30), (90, 46), (66, 44), (56, 60), (56, 104), (30, 112)]), BR, 'f'),
                L(ell(70, 18, 8, 7), WHITE, 'f', True, True), L(ell(72, 18, 4, 4), BLACK, 'f', False)]
    z = 'b' if view == 'front' else 'f'
    out = [L(ell(12, 12, 11, 11), BR, 'f'), L(ell(88, 12, 11, 11), BR, 'f'), L(ell(12, 12, 6, 6), BRD, 'f', False), L(ell(88, 12, 6, 6), BRD, 'f', False),
           L(outline([(4, 110), (2, 60), (10, 16), (50, -6), (90, 16), (98, 60), (96, 110), (50, 116)]), BR, z)]
    if view == 'front':
        out += [L(ell(34, 16, 9, 8), WHITE, 'f', True, True), L(ell(66, 16, 9, 8), WHITE, 'f', True, True),
                L(ell(34, 17, 4.6, 4.6), BLACK, 'f', False), L(ell(66, 17, 4.6, 4.6), BLACK, 'f', False)]
        out += [L(outline([(x - 3, y), (x, y - 5, 1), (x + 3, y)]), BRL, 'f', False) for x, y in ((22, 44), (30, 36), (42, 31), (58, 31), (70, 36), (78, 44))]
    return out
C('keenan-kigu-guru', 'normal', P('#c8d0a0', '#f8dcbc', iris='#1e1a1a', shade='#a8b080'),
  F(eyes='round', brows=False, mouth='none', face_front=face(w=4, chin=104), hairline=[(6, 60), (18, 54), (30, 58), (40, 52), (50, 58), (60, 52), (70, 58), (82, 54), (94, 60)]),
  _bear('front')[:5] + [L(curls(50, 46, (34, 14), 9), 'mid', 'b')] + _bear('front')[5:] + blush(86, 22, 5) +
  [L(outline([(42, 94), (50, 88), (58, 94), (50, 100)]), WHITE, 'f', True, True), L([(42, 94), (58, 94)], OUTC, 'f', False, False, 0.8)],
  _bear('side') + [L(outline([(66, 46), (84, 44), (92, 52), (84, 60), (70, 56)]), 'mid', 'f')],
  _bear('back'))

# Keshia Readingplace: melena rubia larga y lisa hasta el pecho con un mechón que le cae por el centro de la cara, diadema
# verde azulado y una coronita dorada ladeada; ojos azules grandes y sonrisa
CRW = _c('#e8c890')
C('keshia-readingplace', 'chica', P('#f0dc8a', '#fae8d2', iris='#4a8ac8', shade='#ccb460', deep='#a48a3a'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, hairline=[(6, 70), (16, 54), (30, 46), (50, 44), (70, 46), (84, 54), (94, 70)]),
  [L(outline([(8, 116), (4, 60), (12, 22), (50, 6), (88, 22), (96, 60), (92, 116), (82, 112), (84, 70), (16, 70), (18, 112)])),
   L(outline([(60, 8), (88, 22), (96, 60), (92, 114), (84, 80)]), 'shade', 'b', False),
   L(outline([(16, 34), (34, 22), (50, 18), (66, 22), (84, 34), (84, 40), (66, 28), (50, 24), (34, 28), (16, 40)]), _c('#2a8a8a'), 'f'),
   L(outline([(8, 22), (4, 6, 1), (12, 10), (16, -2, 1), (20, 10), (28, 2, 1), (28, 18), (18, 26)]), CRW, 'f', True, True),
   L(outline([(46, 40), (56, 40), (56, 64), (50, 84, 1), (46, 64)]), 'mid', 'f')],
  [L(outline([(56, 58), (64, 44), (84, 42), (94, 24), (76, 6), (50, 0), (24, 6), (6, 26), (0, 70), (4, 116), (24, 116), (40, 84), (50, 70)])),
   L(outline([(10, 30), (40, 20), (78, 22), (88, 30), (84, 34), (40, 26), (12, 36)]), _c('#2a8a8a'), 'f')],
  [L(outline([(8, 118), (4, 60), (12, 22), (50, 6), (88, 22), (96, 60), (92, 118), (50, 122)])),
   L(outline([(60, 8), (88, 22), (96, 60), (92, 116), (70, 118)]), 'shade', 'b', False),
   L(outline([(10, 40), (50, 30), (90, 40), (90, 46), (50, 36), (10, 46)]), _c('#2a8a8a'), 'f'),
   L(outline([(72, 22), (68, 6, 1), (76, 10), (80, -2, 1), (84, 10), (92, 2, 1), (92, 18), (82, 26)]), CRW, 'f', True, True)])

# Kev "Keffiyeh" Fiyah: keffiyeh crema que le cae por los lados hasta los hombros, sujeta con un cordón marrón; piel
# oscura, cejas moradas gruesas, ojos entornados, labios gruesos y una barba morada recortada
KF, KFD, AG, PB = _c('#e8dcc4'), _c('#c4b498'), _c('#5a3a2a'), _c('#6a4a8a')
C('kev-keffiyeh-fiyah', 'normal', P('#6a4a8a', '#8a5a34', iris='#1e1a1a'),
  F(eyes='dot', brows=False, mouth='lips', mouth_y=96, mouth_w=8, face_front=face(w=4, chin=106, jaw=3), face_side=face_side(chin=6), hairline=False),
  [L(outline([(4, 114), (0, 70), (6, 30), (24, 8), (50, 2), (76, 8), (94, 30), (100, 70), (96, 114), (84, 108), (84, 60), (16, 60), (16, 108)]), KF, 'b'),
   L(outline([(10, 52), (12, 34), (30, 18), (50, 14), (70, 18), (88, 34), (90, 52), (70, 46), (50, 48), (30, 46)]), KF, 'f'),
   L(outline([(8, 44), (50, 34), (92, 44), (92, 52), (50, 42), (8, 52)]), AG, 'f', True, True),
   L(outline([(20, 86), (30, 104), (50, 112), (70, 104), (80, 86), (72, 100), (50, 106), (28, 100)]), PB, 'f', False),
   L([(26, 64), (42, 66)], PB, 'f', False, False, 3.4), L([(74, 64), (58, 66)], PB, 'f', False, False, 3.4)],
  [L(outline([(2, 116), (-2, 60), (6, 26), (30, 6), (56, 2), (80, 10), (92, 30), (92, 50), (62, 50), (54, 64), (54, 108), (30, 116)]), KF, 'f'),
   L(outline([(4, 44), (50, 36), (92, 38), (92, 46), (50, 44), (6, 52)]), AG, 'f', True, True),
   L(outline([(62, 96), (78, 104), (86, 98), (84, 106), (70, 110)]), PB, 'f', False), L([(72, 64), (86, 66)], PB, 'f', False, False, 3.0)],
  [L(outline([(4, 116), (0, 70), (6, 30), (24, 8), (50, 2), (76, 8), (94, 30), (100, 70), (96, 116), (50, 120)]), KF, 'f'),
   L(outline([(58, 4), (88, 22), (98, 70), (94, 114), (70, 116)]), KFD, 'f', False),
   L(outline([(8, 46), (50, 38), (92, 46), (92, 54), (50, 46), (8, 54)]), AG, 'f', True, True)])

# Khefren "Khafra" Chepren: calvo de cabeza enorme y piel morena, con una cadena dorada en la frente, dos cicatrices sobre
# los ojos entornados, aros dorados en las orejas y la boca hacia abajo enseñando los dientes
GLD = _c('#e0b030')
C('khefren-khafra-chepren', 'corpulento', P('#3a2a1a', '#a8703e', iris='#1e1a1a'),
  F(eyes='dot', brows='angry', mouth='none', face_front=face(w=8, chin=110, jaw=8, top=14), face_side=face_side(chin=10, jaw=8), ear_out=8, hairline=False),
  skull('front') + [strand([(22, 40), (36, 34), (50, 32), (64, 34), (78, 40)], GLD, 'f', 2.0)] +
  [L(ell(x, y, 1.6, 1.6), GLD, 'f', False) for x, y in ((30, 37), (42, 33), (58, 33), (70, 37))] +
  [L([(30, 58), (40, 84)], _c('#e8c8a0'), 'f', False, False, 1.2), L([(70, 58), (60, 84)], _c('#e8c8a0'), 'f', False, False, 1.2),
   L(ell(10, 82, 3.6, 3.6) + [ell(10, 82, 3.6, 3.6)[0]], GLD, 'f', False, False, 1.6), L(ell(90, 82, 3.6, 3.6) + [ell(90, 82, 3.6, 3.6)[0]], GLD, 'f', False, False, 1.6),
   L(outline([(32, 100), (50, 94), (68, 100), (64, 106), (50, 100), (36, 106)]), WHITE, 'f', True, True), L(quad((32, 106), (50, 96), (68, 106)), OUTC, 'f', False, False, 1.2)],
  skull('side') + [strand([(36, 34), (60, 30), (84, 38)], GLD, 'f', 2.0), L(ell(44, 82, 3.4, 3.4) + [ell(44, 82, 3.4, 3.4)[0]], GLD, 'f', False, False, 1.6)],
  skull('back') + [strand([(16, 44), (50, 40), (84, 44)], GLD, 'f', 2.0)])

# Kit Fischer: cabeza en forma de huevo, calvo salvo una cresta roja de plumas que le cae hacia un lado; orejas de punta;
# una banda negra en los ojos con los ojos blancos afilados, nariz chata y una sonrisa de pillo con un caramelo
CRS = _c('#c8404a')
C('kit-fischer', 'normal', P('#c8404a', '#f6b86a', iris='#1e1a1a'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, face_front=face(w=-2, chin=104, top=6), ears=False, hairline=False),
  skull('front') + [L(outline([(16, 64), (-2, 52, 1), (14, 78)]), 'skin', 'b'), L(outline([(84, 64), (102, 52, 1), (86, 78)]), 'skin', 'b'),
                    L(outline([(44, 40), (30, -14, 1), (46, 4), (44, -24, 1), (56, 0), (62, -18, 1), (62, 8), (76, -2, 1), (64, 20), (56, 50, 1)]), CRS, 'f'),
                    strand([(48, 8), (52, 30)], _c('#9a2a34'), 'f', 1.0),
                    L(outline([(20, 70), (40, 66), (50, 72), (60, 66), (80, 70), (76, 80), (60, 78), (50, 82), (40, 78), (24, 80)]), BLACK, 'f'),
                    L(outline([(26, 72), (40, 70), (42, 76), (30, 77)]), WHITE, 'f', False), L(outline([(74, 72), (60, 70), (58, 76), (70, 77)]), WHITE, 'f', False),
                    L(ell(50, 84, 3, 1.8), 'skin_d', 'f', True, True), L(ell(62, 96, 2.4, 2.4), WHITE, 'f', True, True)],
  skull('side') + [L(outline([(40, 66), (26, 50, 1), (52, 62), (50, 78)]), 'skin', 'f'),
                   L(outline([(70, 30), (56, -18, 1), (46, 0), (30, -10, 1), (34, 10), (16, 4, 1), (24, 22), (10, 30, 1), (30, 34), (50, 30)]), CRS, 'f'),
                   L(outline([(64, 70), (90, 68), (90, 80), (66, 80)]), BLACK, 'f'), L(outline([(76, 72), (88, 71), (86, 77), (78, 77)]), WHITE, 'f', False)],
  skull('back') + [L(outline([(16, 64), (-2, 52, 1), (14, 78)]), 'skin', 'f'), L(outline([(84, 64), (102, 52, 1), (86, 78)]), 'skin', 'f'),
                   L(outline([(42, 60), (40, -14, 1), (50, 4), (56, -20, 1), (60, 6), (62, 60)]), CRS, 'f')])

# Lacy Cagney: media melena verde oliva lisa con flequillo recto hasta los ojos; ojos negros redondos y grandes y boquita
# entreabierta de susto
C('lacy-cagney', 'chica', P('#8a8a3a', '#fadcc0', iris='#1e1a1a', shade='#6c6c26', deep='#4e4e18'),
  F(eyes='round', brows=False, mouth='none', eye_y=77, hairline=[(6, 68), (14, 66), (30, 66), (50, 66), (70, 66), (86, 66), (94, 68)]),
  [L(outline([(10, 98), (8, 50), (16, 16), (50, 2), (84, 16), (92, 50), (90, 98), (82, 98), (80, 70), (20, 70), (18, 98)])),
   L(outline([(60, 4), (84, 16), (92, 50), (90, 96), (82, 70)]), 'shade', 'b', False)] + [strand([(x, 14), (x, 66)], 'deep', 'b', 1.0) for x in (30, 42, 54, 66)] +
  [L(ell(50, 94, 3, 2.4), (150, 60, 60, 255), 'f', True, True)],
  [L(outline([(56, 66), (62, 50), (86, 48), (92, 26), (74, 6), (50, 0), (24, 6), (6, 26), (2, 60), (6, 98), (30, 100), (50, 94), (54, 80)]))],
  [L(outline([(10, 100), (8, 50), (16, 16), (50, 2), (84, 16), (92, 50), (90, 100), (50, 104)])),
   L(outline([(60, 4), (84, 16), (92, 50), (90, 98), (70, 100)]), 'shade', 'b', False)])

# Laititia Cheeseman: media melena gris oscuro lisa con flequillo recto inclinado; ojos ámbar con pestañas y boca seria
C('laititia-cheeseman', 'chica', P('#4a5054', '#f8dcc0', iris='#a88a3a', shade='#363c40', deep='#22272a'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=94, hairline=[(6, 66), (14, 56), (30, 58), (50, 60), (70, 62), (86, 64), (94, 66)]),
  [L(outline([(10, 92), (8, 48), (16, 14), (50, 2), (84, 14), (92, 48), (90, 92), (82, 92), (80, 70), (20, 70), (18, 92)])),
   L(outline([(60, 4), (84, 14), (92, 48), (90, 90), (82, 68)]), 'shade', 'b', False)] + lashes(),
  [L(outline([(56, 62), (62, 48), (86, 46), (92, 24), (74, 6), (50, 0), (24, 6), (6, 26), (2, 60), (6, 92), (30, 94), (50, 90), (54, 76)]))] + lash_side(),
  [L(outline([(10, 94), (8, 48), (16, 14), (50, 2), (84, 14), (92, 48), (90, 94), (50, 98)])),
   L(outline([(60, 4), (84, 14), (92, 48), (90, 92), (70, 94)]), 'shade', 'b', False)])

# Laurie Driver (portero): pelo verde de pinchos hacia arriba y unas gafas de aviador naranjas con correa marrón sobre la
# frente; cejas verdes enfadadas, ojos negros y una sonrisa de dientes
GGF, GGL = _c('#e8d0a8'), _c('#f08a20')
C('laurie-driver', 'normal', P('#5a8a3a', '#f6c08a', iris='#1e1a1a', shade='#426a28', deep='#2e4e1a'),
  F(eyes='sharp', brows=False, mouth='grin', mouth_y=94, hairline=hl(6, 62, 54, 60, jit=2, seed=81)),
  dome('front', top=-6, w=46, cy=44, n=8, amp=18, seed=82, sb=62) +
  [L(outline([(10, 52), (50, 46), (90, 52), (90, 60), (50, 54), (10, 60)]), _c('#6a3a1e'), 'f', True, True),
   L(ell(36, 52, 9, 8), GGF, 'f', True, True), L(ell(64, 52, 9, 8), GGF, 'f', True, True),
   L(ell(36, 52, 6, 5.4), GGL, 'f', False), L(ell(64, 52, 6, 5.4), GGL, 'f', False),
   L([(26, 66), (42, 70)], 'mid', 'f', False, False, 3.0), L([(74, 66), (58, 70)], 'mid', 'f', False, False, 3.0)],
  dome('side', top=-6, w=44, cy=44, n=8, amp=18, seed=82, nape=84, fr=50) +
  [L(outline([(4, 54), (50, 48), (90, 46), (90, 54), (50, 56), (6, 62)]), _c('#6a3a1e'), 'f', True, True), L(ell(82, 50, 6, 8), GGF, 'f', True, True),
   L(ell(83, 50, 4, 5.4), GGL, 'f', False), L([(72, 66), (86, 70)], 'mid', 'f', False, False, 3.0)],
  dome('back', top=-6, w=46, cy=44, n=8, amp=18, seed=82, nape=84) +
  [L(outline([(8, 56), (50, 50), (92, 56), (92, 64), (50, 58), (8, 64)]), _c('#6a3a1e'), 'f', True, True)])

# Lee Bei (portero): yelmo chino dorado con el borde azul y adornos de nube, con un penacho blanco detrás; una máscara azul
# le tapa de la nariz a la barbilla; ojos rojizos enfadados
YG, YGD, YB = _c('#c8b47a'), _c('#a08a50'), _c('#2a4a8a')
def _leebei(view):
    if view == 'side':
        return [L(outline([(30, 8), (10, -14), (-4, -4, 1), (6, 2), (20, 14)]), WHITE, 'f'),
                L(outline([(4, 100), (0, 50), (10, 14), (40, -4), (70, 4), (90, 24), (94, 56), (70, 60), (60, 100), (30, 106)]), YB, 'f'),
                L(outline([(8, 96), (6, 50), (14, 18), (40, 2), (66, 8), (84, 26), (88, 54), (66, 56), (56, 96), (30, 100)]), YG, 'f', False),
                L(outline([(64, 80), (96, 80), (96, 104), (70, 110)]), YB, 'f')]
    out = [L(outline([(60, 2), (76, -12), (92, -8, 1), (82, 2), (72, 10)]), WHITE, 'f'),
           L(outline([(8, 112), (4, 50), (14, 14), (50, -6, 1), (86, 14), (96, 50), (92, 112), (76, 112), (78, 64), (22, 64), (24, 112)]), YB, 'f'),
           L(outline([(12, 108), (10, 50), (20, 18), (50, 2, 1), (80, 18), (90, 50), (88, 108), (80, 108), (82, 60), (18, 60), (20, 108)]), YG, 'f', False)]
    if view == 'front':
        out += [L(outline([(18, 60), (30, 44), (50, 40), (70, 44), (82, 60), (70, 64), (50, 60), (30, 64)]), YG, 'f'),
                strand([(50, 4), (50, 58)], YGD, 'f', 1.2), L(ell(36, 30, 6, 5), YGD, 'f', False), L(ell(64, 30, 6, 5), YGD, 'f', False),
                L(outline([(22, 82), (50, 78), (78, 82), (76, 110), (50, 116), (24, 110)]), YB, 'f')]
    else:
        out = [L(outline([(8, 112), (4, 50), (14, 14), (50, -6, 1), (86, 14), (96, 50), (92, 112), (50, 116)]), YB, 'f'),
               L(outline([(12, 108), (10, 50), (20, 18), (50, 2, 1), (80, 18), (90, 50), (88, 108), (50, 112)]), YG, 'f', False),
               L(outline([(40, 6), (50, -16), (64, -10, 1), (56, 0)]), WHITE, 'f')]
    return out
C('lee-bei', 'normal', P('#3a2a20', '#d89a5a', iris='#a83a2a'),
  F(eyes='sharp', brows='angry', mouth='none', eye_y=72, hairline=False, ears=False), _leebei('front'), _leebei('side'), _leebei('back'))

# Lee "Freedom" Bartarian: afro enorme castaño oscuro; gafas de estrella amarillas con el cristal rojo; cara larga, ojos
# azules enfadados, nariz grande con una tirita y boca abierta de enfado
AFD = _c('#3a2a20')
C('lee-freedom-bartarian', 'delgado', P('#3a2a20', '#f2c08a', iris='#3a5ab0', shade='#2a1e16'),
  F(eyes='sharp', brows='angry', mouth='none', face_front=face(chin=112), face_side=face_side(chin=10, nose=8), hairline=[(6, 58), (20, 50), (50, 46), (80, 50), (94, 58)]),
  [L(curls(50, 30, (60, 38), 11))] + [star(36, 64, 10, STR), star(64, 64, 10, STR), star(36, 64, 5, _c('#d02a2a')), star(64, 64, 5, _c('#d02a2a'))] +
  [L(outline([(44, 74), (56, 74), (60, 92), (50, 96), (40, 92)]), 'skin_d', 'f', True, True),
   L(outline([(38, 82), (62, 80), (62, 86), (38, 88)]), _c('#f2ece0'), 'f', True, True),
   L(outline([(40, 102), (50, 98), (60, 102), (56, 108), (44, 108)]), _c('#8a3a3a'), 'f', True, True)],
  [L(curls(40, 30, (52, 38), 11)), star(84, 64, 8, STR), L(outline([(86, 72), (100, 88), (92, 96), (86, 92)]), 'skin_d', 'f', True, True)],
  [L(curls(50, 34, (60, 40), 11))])

# Leighton Bolt: pelo amarillo en pinchos de rayo que salen hacia todos lados, con una cinta turquesa; piel oscura, cara
# larga, ojos redondos muy abiertos, nariz larga y una sonrisa enorme; pañuelo naranja al cuello
TQB, ORS = _c('#3ac8b4'), _c('#e86a1e')
C('leighton-bolt', 'delgado', P('#f0d040', '#8a5a34', iris='#1e1a1a', shade='#c8a828', light='#f8ec98'),
  F(eyes='round', brows='angry', mouth='none', face_front=face(chin=112), face_side=face_side(chin=10, nose=6), hairline=[(6, 56), (20, 50), (50, 46), (80, 50), (94, 56)]),
  [L(outline([(12, 70), (-8, 64, 1), (6, 56), (-6, 40, 1), (10, 34), (4, 10, 1), (22, 18), (26, -6, 1), (40, 10), (50, -12, 1), (60, 8), (76, -6, 1), (78, 16),
              (98, 8, 1), (90, 32), (106, 40, 1), (92, 54), (104, 66, 1), (88, 70), (84, 56), (16, 56)])),
   L(outline([(10, 44), (30, 34), (50, 30), (70, 34), (92, 44), (92, 52), (70, 42), (50, 38), (30, 42), (10, 52)]), TQB, 'f'),
   L(outline([(40, 70), (50, 66), (58, 92), (50, 96), (44, 90)]), 'skin_d', 'f', False),
   L(outline([(30, 98), (50, 104), (70, 98), (64, 108), (50, 112), (36, 108)]), WHITE, 'f', True, True),
   L(outline([(28, 110), (50, 116), (72, 110), (86, 118), (96, 128, 1), (70, 122), (50, 124), (24, 120)]), ORS, 'f')],
  [L(outline([(54, 56), (62, 44), (80, 40), (98, 26, 1), (82, 20), (92, 2, 1), (72, 8), (68, -14, 1), (54, 4), (36, -12, 1), (32, 8), (10, 2, 1), (16, 22), (-6, 28, 1),
              (6, 44), (-4, 60, 1), (10, 66), (2, 82, 1), (22, 78), (40, 70)])),
   L(outline([(4, 40), (40, 30), (84, 32), (90, 40), (40, 38), (6, 48)]), TQB, 'f'),
   L(outline([(84, 76), (96, 90), (90, 96), (84, 94)]), 'skin_d', 'f', True, True),
   L(outline([(78, 102), (94, 100), (92, 108), (80, 110)]), WHITE, 'f', True, True),
   L(outline([(40, 112), (70, 112), (94, 116), (90, 124), (40, 122)]), ORS, 'f')],
  [L(outline([(12, 80), (-8, 64, 1), (6, 56), (-6, 40, 1), (10, 34), (4, 10, 1), (22, 18), (26, -6, 1), (40, 10), (50, -12, 1), (60, 8), (76, -6, 1), (78, 16),
              (98, 8, 1), (90, 32), (106, 40, 1), (92, 54), (104, 66, 1), (88, 80), (50, 86)])),
   L(outline([(8, 48), (50, 40), (92, 48), (92, 56), (50, 48), (8, 56)]), TQB, 'f'), L(outline([(30, 112), (70, 112), (96, 126, 1), (70, 122), (30, 122)]), ORS, 'f')])

# Lennon Trousers: gorra enorme de cuadros naranja, crema y azul; un antifaz negro con dos ojos blancos redondos; pelo
# castaño por los lados y una sonrisa
CO, CC, CB = _c('#e0782a'), _c('#f2e6a8'), _c('#1e6a8a')
def _checkcap(view):
    if view == 'side':
        return [L(outline([(2, 52), (0, 20), (20, -2), (54, -8), (84, 2), (98, 22), (96, 44), (60, 52)]), CC, 'f'),
                L(outline([(20, -2), (54, -8), (56, 20), (24, 24)]), CB, 'f', False), L(outline([(56, 20), (96, 22), (96, 44), (60, 48)]), CO, 'f', False)]
    cap = [L(outline([(2, 54), (-4, 24), (14, 0), (50, -8), (86, 0), (104, 24), (98, 54), (50, 60)]), CC, 'f'),
           L(outline([(14, 0), (36, -6), (36, 24), (2, 28)]), CO, 'f', False), L(outline([(64, -6), (86, 0), (100, 26), (64, 24)]), CB, 'f', False),
           L(outline([(36, 24), (64, 24), (64, 56), (36, 56)]), CB, 'f', False), L(outline([(2, 30), (36, 26), (36, 54), (6, 50)]), CC, 'f', False),
           L(outline([(64, 26), (98, 28), (96, 52), (64, 54)]), CC, 'f', False)]
    if view == 'front':
        cap.append(L(outline([(12, 56), (50, 52), (88, 56), (86, 62), (50, 58), (14, 62)]), _c('#8a3a1e'), 'f', True, True))
    return cap
C('lennon-trousers', 'normal', P('#5a3a1e', '#f6c08a', iris='#1e1a1a'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=92, hairline=False),
  [L(outline([(12, 90), (10, 60), (88, 60), (90, 90), (82, 76), (18, 76)]))] + _checkcap('front') +
  [L(outline([(18, 68), (50, 64), (82, 68), (80, 80), (50, 78), (20, 80)]), BLACK, 'f'),
   L(ell(36, 72, 5, 4.6), WHITE, 'f', False), L(ell(64, 72, 5, 4.6), WHITE, 'f', False), L(ell(36, 72, 2, 2), BLACK, 'f', False), L(ell(64, 72, 2, 2), BLACK, 'f', False)],
  [L(outline([(54, 60), (40, 76), (14, 84), (4, 60)]))] + _checkcap('side') +
  [L(outline([(60, 68), (92, 66), (92, 80), (62, 80)]), BLACK, 'f'), L(ell(82, 72, 4, 4.6), WHITE, 'f', False), L(ell(84, 72, 1.8, 2), BLACK, 'f', False)],
  [L(outline([(10, 90), (8, 60), (92, 60), (90, 90), (50, 94)]))] + _checkcap('back'))

# Lenton Gouger: pelo naranja peinado en forma de calabaza, con gajos y un rabito verde arriba; los ojos como agujeros
# oscuros, nariz triangular naranja y un bigote negro rizado
C('lenton-gouger', 'normal', P('#e8902a', '#f8d0a8', iris='#1e1a1a', shade='#c06c18', deep='#8a4a10'),
  F(eyes='none', brows=False, mouth='none', hairline=[(6, 62), (16, 56), (26, 62), (36, 56), (46, 62), (54, 56), (64, 62), (74, 56), (84, 62), (94, 62)]),
  [L(outline([(10, 66), (4, 40), (14, 14), (32, 2), (50, 0), (68, 2), (86, 14), (96, 40), (90, 66), (70, 60), (30, 60)])),
   strand([(30, 6), (24, 34), (28, 60)], 'shade', 'b', 1.6), strand([(50, 2), (50, 60)], 'shade', 'b', 1.6), strand([(70, 6), (76, 34), (72, 60)], 'shade', 'b', 1.6),
   L(quad((50, 2), (48, -10), (54, -16)), STM, 'b', False, False, 3.4),
   L(ell(36, 76, 5, 4), _c('#4a3a3a'), 'f', True, True), L(ell(64, 76, 5, 4), _c('#4a3a3a'), 'f', True, True),
   L(outline([(47, 82), (53, 82), (50, 88, 1)]), _c('#e0802a'), 'f', False),
   L(outline([(28, 96), (36, 90), (44, 92), (50, 90), (56, 92), (64, 90), (72, 96), (66, 98), (58, 96), (50, 98), (42, 96), (34, 98)]), BLACK, 'f')],
  [L(outline([(52, 62), (60, 48), (82, 44), (92, 26), (74, 6), (50, 0), (24, 4), (6, 24), (2, 50), (12, 72), (34, 74), (46, 66)])),
   strand([(26, 6), (14, 40), (20, 70)], 'shade', 'b', 1.6), strand([(52, 2), (46, 40), (44, 70)], 'shade', 'b', 1.6),
   L(quad((52, 2), (50, -10), (56, -16)), STM, 'b', False, False, 3.4), L(ell(82, 76, 3.4, 4), _c('#4a3a3a'), 'f', True, True),
   L(outline([(80, 94), (88, 90), (96, 94), (90, 98)]), BLACK, 'f')],
  [L(outline([(10, 80), (4, 40), (14, 14), (32, 2), (50, 0), (68, 2), (86, 14), (96, 40), (90, 80), (50, 86)])),
   strand([(30, 6), (24, 40), (28, 80)], 'shade', 'b', 1.6), strand([(50, 2), (50, 84)], 'shade', 'b', 1.6), strand([(70, 6), (76, 40), (72, 80)], 'shade', 'b', 1.6),
   L(quad((50, 2), (48, -10), (54, -16)), STM, 'b', False, False, 3.4)])

# Leo Maine: melena dorada de león en pinchos grandes alrededor de la cara, con las puntas castaño oscuro arriba; piel
# tostada, ojos amarillos afilados, bigotes de gato marcados en las mejillas y media sonrisa
C('leo-maine', 'normal', P('#e0b440', '#c08a52', iris='#c8b830', shade='#b88a28', deep='#5e4a14'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=hl(5, 62, 48, 60, jit=3, seed=91)),
  dome('front', top=-6, w=56, cy=50, n=12, amp=16, seed=92, long=104, flare=8) +
  [L(outline([(30, 6), (24, -18, 1), (40, 0)]), 'deep', 'b'), L(outline([(56, -2), (62, -24, 1), (68, 2)]), 'deep', 'b'),
   L(outline([(74, 10), (86, -6, 1), (82, 16)]), 'deep', 'b')] +
  [L([(20, 88), (30, 90)], OUTC, 'f', False, False, 1.0), L([(20, 94), (30, 92)], OUTC, 'f', False, False, 1.0),
   L([(80, 88), (70, 90)], OUTC, 'f', False, False, 1.0), L([(80, 94), (70, 92)], OUTC, 'f', False, False, 1.0)],
  dome('side', top=-6, w=54, cy=50, n=12, amp=16, seed=92, long=104, flare=8, fr=56) + [L(outline([(40, 0), (40, -24, 1), (50, -2)]), 'deep', 'b')],
  dome('back', top=-6, w=56, cy=50, n=12, amp=16, seed=92, long=104, flare=8, ends=5) + [L(outline([(30, 6), (24, -18, 1), (40, 0)]), 'deep', 'b'),
                                                                                       L(outline([(56, -2), (62, -24, 1), (68, 2)]), 'deep', 'b')])
