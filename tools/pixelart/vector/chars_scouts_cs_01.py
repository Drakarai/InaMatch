"""Ojeadores de CS (scouts-cs), tanda 01: dibujados a partir de su retrato de Victory Road; claves 'scouts-cs:<id>'.

El frente sale del retrato; el perfil y la espalda, del modelo 3D cuando lo hay y es el mismo personaje (Aslei Rune,
Charley Horse, Chester Horse Sr., Faythe Heeler, Gammon Checker, Gilles de Rais, Hiro Hughes, Isami Kondo) y, si no, de
cómo cae ese peinado. Ayudas de las tandas de IE (dome/hl/face de la 09 de IE1, gafas y bigotes de la 03...)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401
from chars_scouts_ie1_09 import _c, dome, face, face_side, hl, mark  # noqa: F401
from chars_scouts_ie1_03 import blush, stache, thick_brows  # noqa: F401
from chars_scouts_ie1_10 import nose_tri, squint  # noqa: F401
from chars_scouts_ie2_03 import ears_pointy, round_glasses, teeth_grin  # noqa: F401
from chars_scouts_ie2_04 import sharp_eye_side, sharp_eyes  # noqa: F401
from chars_scouts_ie3_02 import hood, ring, scarf  # noqa: F401
from chars_scouts_ie3_06 import arc, band, cap  # noqa: F401

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
    """Como en la tanda 09 de IE1: el nacimiento del pelo baja por el borde de la cara para que su raya no cruce el pelo."""
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[K + pid] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def M(pts, c='mid', z='b', sil=True, ln=False):
    return L(outline(pts), c, z, sil, ln)


def mx(pts):
    return [(100 - p[0],) + tuple(p[1:]) for p in pts]


def both(pts, c='mid', z='b', sil=True, ln=False):
    """La forma y su reflejo (x -> 100 - x)."""
    return [M(pts, c, z, sil, ln), M(mx(pts), c, z, sil, ln)]


def W(pts, c, w, z='f'):
    """Raya de grosor w."""
    return L(pts, c, z, False, False, w)


# ---------------------------------------------------------------------------------------------------------- jugadores

# Agnethe Presari: melena lisa naranja larguísima con raya al medio que le cae hasta el pecho, con las puntas atadas en
# dos mechones; ojos afilados ámbar y boca seria
C('agnethe-presari', 'chica', P('#f49a10', '#fdeed4', iris='#d8941a', shade='#c8700e'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=[(8, 70), (16, 50), (30, 40), (48, 38), (50, 46), (52, 38), (70, 40), (84, 50), (92, 70)]),
  dome('front', top=2, w=46, cy=44, long=124, flare=4) + [M([(8, 100), (20, 100), (18, 126), (14, 134, 1), (8, 126)], 'mid', 'f'),
                                                          M([(92, 100), (80, 100), (82, 126), (86, 134, 1), (92, 126)], 'mid', 'f'),
                                                          W([(9, 112), (19, 112)], WHITE, 2.0), W([(81, 112), (91, 112)], WHITE, 2.0)],
  dome('side', top=2, w=46, cy=44, long=124, flare=4, fr=46),
  dome('back', top=2, w=46, cy=44, long=124, flare=4, ends=3))

# Ai Machina (portera): pelo lila abultado en mechones ondulados que salen hacia fuera a los lados, con un aro blanco
# como de auriculares por encima; ojos grandes negros con la pupila roja y sonrisa
LIL = _c('#ece8f0')
C('ai-machina', 'chica', P('#a888dc', '#fbf0e0', iris='#c0202a', shade='#8460a0'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, hairline=[(8, 66), (20, 54), (30, 62), (40, 54), (50, 62), (60, 54), (70, 62), (80, 54), (92, 66)]),
  [M([(-6, 18), (10, -6), (50, -16), (90, -6), (106, 18), (100, 24), (88, 6), (50, -6), (12, 6), (0, 24)], LIL, 'b')] +
  dome('front', top=0, w=48, cy=46, n=8, amp=8, soft=True, long=104, flare=12, seed=3) +
  both([(6, 70), (-10, 78, 1), (4, 84), (-6, 96, 1), (10, 96)]),
  [M([(10, 14), (40, -12), (70, -10), (78, 2), (62, 2), (40, 2), (18, 22)], LIL, 'b')] +
  dome('side', top=0, w=48, cy=46, n=8, amp=8, soft=True, long=104, flare=12, seed=3, fr=50),
  [M([(-6, 18), (10, -6), (50, -16), (90, -6), (106, 18), (100, 24), (88, 6), (50, -6), (12, 6), (0, 24)], LIL, 'f')] +
  dome('back', top=0, w=48, cy=46, n=8, amp=8, soft=True, long=104, flare=12, seed=3, ends=5))

# An Tafuri: melena castaña en forma de seta, muy ancha y redonda, con un moño arriba sujeto con una goma rosa; cara redonda,
# ojos de punto, sonrisa y coloretes
PNK = _c('#f0a090')
def _mush(view):
    if view == 'front':
        return [M([(-4, 64), (-2, 40), (14, 18), (36, 8), (50, 6), (64, 8), (86, 18), (102, 40), (104, 64), (82, 62), (50, 58), (18, 62)]),
                M([(62, 8), (88, 20), (102, 42), (104, 62), (84, 60), (80, 32)], 'shade', 'b', False),
                L(ell(50, -4, 11, 10)), L(ell(50, 6, 9, 3.4), PNK, 'b')]
    if view == 'side':
        return [M([(86, 62), (96, 44), (84, 18), (60, 6), (34, 6), (10, 18), (-6, 40), (-6, 66), (14, 70), (40, 64), (60, 64)]),
                L(ell(44, -4, 10, 10)), L(ell(44, 6, 8, 3.2), PNK, 'b')]
    return [M([(-4, 70), (-2, 40), (14, 18), (36, 8), (50, 6), (64, 8), (86, 18), (102, 40), (104, 70), (80, 74), (50, 76), (20, 74)]),
            M([(62, 8), (88, 20), (102, 42), (104, 68), (80, 72), (76, 36)], 'shade', 'b', False),
            L(ell(50, -4, 11, 10)), L(ell(50, 6, 9, 3.4), PNK, 'f')]
C('an-tafuri', 'chica', P('#5a3a32', '#fabc80', iris='#1e1414'),
  F(eyes='dot', brows=False, mouth='smile', mouth_y=92, face_front=face(w=3, chin=100), hairline=[(6, 64), (14, 60), (50, 58), (86, 60), (94, 64)]),
  _mush('front') + blush(86, 24), _mush('side'), _mush('back'))

# Asbe Stostumi: gordita de piel morena, pelo azul marino peinado hacia arriba en dos ondas (la de su derecha más clara) y
# una coleta azul que le cae por un lado; labios gruesos naranjas en una boca redonda abierta y ojos redondos
BLU = _c('#2e5a84')
C('asbe-stostumi', 'corpulento', P('#1a2440', '#bc844e', iris='#1e1414', shade='#121a30', light='#2e5a84'),
  F(eyes='round', brows=True, mouth='none', face_front=face(w=7, chin=104, jaw=6), face_side=face_side(chin=4, jaw=6),
    hairline=[(4, 60), (14, 42), (30, 36), (50, 40), (70, 36), (86, 42), (96, 60)]),
  [M([(6, 62), (2, 36), (10, 10), (24, -4, 1), (34, 14), (50, 22), (40, 6), (54, -8), (78, -2), (94, 18), (98, 44), (94, 62), (80, 44), (20, 44)]),
   M([(6, 60), (2, 36), (10, 10), (24, -4), (34, 14), (40, 30), (20, 40)], BLU, 'b', False),
   M([(88, 40), (100, 54), (104, 80), (96, 104), (92, 116, 1), (88, 100), (94, 78), (90, 58)], BLU, 'f'),
   L(blob([(38, 92), (50, 86), (62, 92), (60, 102), (50, 106), (40, 102)], 6), _c('#e86a2a'), 'f', False, True),
   L(ell(50, 96, 5, 3), _c('#8a2a1a'), 'f', False), L(ell(50, 84, 3, 2.4), 'skin_d', 'f', False, True)],
  dome('side', top=-6, w=48, cy=42, n=3, amp=10, soft=True, nape=80, fr=44, seed=5) +
  [M([(20, 50), (6, 70), (2, 96), (8, 112, 1), (16, 94), (22, 70)], BLU, 'b'), L(blob([(78, 90), (90, 88), (92, 98), (80, 100)], 4), _c('#e86a2a'), 'f', False, True)],
  dome('back', top=-6, w=48, cy=42, n=3, amp=10, soft=True, nape=80, seed=5) +
  [M([(70, 66), (84, 76), (88, 100), (84, 116, 1), (76, 98), (72, 80)], BLU, 'f')])

# Aslei Rune (modelo 3D): pelo verde menta corto y ondulado, echado hacia atrás con un mechón por delante; ojos verde
# agua afilados, ceño fruncido; capucha blanca rosada caída por detrás del cuello y una bufanda azul marino
HOOD, NAVY = _c('#f4e2dc'), _c('#2c3a5c')
C('aslei-rune', 'normal', P('#a8d8b4', '#fbe6c0', iris='#2a9a8a', shade='#80b090'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=92, hairline=[(8, 62), (18, 48), (28, 56), (36, 44), (50, 50), (62, 42), (76, 52), (84, 46), (92, 62)]),
  [M([(-4, 120), (0, 96), (14, 92), (30, 106), (70, 106), (86, 92), (100, 96), (104, 120)], HOOD, 'b')] +
  dome('front', top=2, w=46, cy=46, n=7, amp=8, sweep=0.5, soft=True, sb=70, seed=11) + scarf('front', NAVY, y=102, h=14),
  [M([(-10, 116), (-6, 86), (10, 76), (30, 90), (40, 110)], HOOD, 'b')] +
  dome('side', top=2, w=46, cy=46, n=7, amp=8, sweep=0.5, soft=True, nape=84, fr=48, seed=11) + scarf('side', NAVY, y=102, h=14),
  [M([(-4, 120), (-4, 84), (20, 74), (50, 72), (80, 74), (104, 84), (104, 120)], HOOD, 'f'),
   M([(10, 120), (12, 96), (50, 90), (88, 96), (90, 120)], 'skin_d', 'f', False)] +
  dome('back', top=2, w=46, cy=46, n=7, amp=8, sweep=0.5, soft=True, nape=78, seed=11))

# Bon Homie: gordo de cara redonda y anaranjada con un gorro de cocinero altísimo de pliegues; orejas grandes, ojos
# pequeñitos, nariz de bolita y una sonrisa enorme de dientes
CHEF, CHEFD = _c('#f8f6f0'), _c('#c8c4c0')
def _chef(view):
    x = 50 if view != 'side' else 46
    out = [M([(x - 22, 40), (x - 24, -36), (x + 24, -36), (x + 22, 40)], CHEF, 'f'),
           M([(x - 28, 38), (x + 28, 38), (x + 28, 46), (x - 28, 46)], CHEF, 'f')]
    out += [W([(x + d, -34), (x + d, 36)], CHEFD, 1.4) for d in (-14, -5, 5, 14)]
    return out
C('bon-homie', 'corpulento', P('#c8a890', '#fbbc7c', iris='#1e1414'),
  F(eyes='dot', brows=False, mouth='none', hairline=False, big_ears=5, ear_out=6, face_front=face(w=10, chin=104, jaw=8, top=36),
    face_side=face_side(chin=4, jaw=8), eye_y=72, nose=(50, 82, 4)),
  _chef('front') + [L(blob([(34, 88), (50, 86), (66, 88), (62, 100), (50, 104), (38, 100)], 6), WHITE, 'f', False, True),
                    W([(36, 94), (64, 94)], OUTC, 1.2)] + blush(84, 28, 5.4),
  _chef('side') + [L(blob([(76, 88), (88, 86), (88, 98), (78, 100)], 4), WHITE, 'f', False, True)],
  _chef('back'))

# Breeze Skyler (portero): pelo blanco crema revuelto con un flequillo largo que le tapa media frente; unas gafas de nieve
# naranjas colgadas al cuello y un pañuelo azul con remolinos de viento a los lados; piel tostada, ojos azules afilados
GOG, GOGF, BL2 = _c('#f07a20'), _c('#2c3a3a'), _c('#3a40c8')
def _goggles_neck(view):
    if view == 'front':
        return scarf('front', BL2, y=104, h=12) + [M([(22, 100), (78, 100), (80, 112), (50, 116), (20, 112)], GOGF, 'f'),
                                                   M([(26, 103), (48, 103), (48, 111), (26, 111)], GOG, 'f', False),
                                                   M([(52, 103), (74, 103), (74, 111), (52, 111)], GOG, 'f', False)]
    if view == 'side':
        return scarf('side', BL2, y=104, h=12) + [M([(60, 100), (90, 100), (90, 112), (60, 112)], GOGF, 'f'), M([(70, 103), (88, 103), (88, 110), (70, 110)], GOG, 'f', False)]
    return scarf('back', BL2, y=104, h=12)
C('breeze-skyler', 'normal', P('#f0e6d4', '#f8cc8c', iris='#4a7ab0', shade='#c8bca8'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=[(8, 64), (18, 50), (30, 58), (40, 48), (50, 66), (60, 50), (70, 60), (82, 48), (92, 64)]),
  [M([(2, 70), (-10, 56, 1), (6, 50)], BL2, 'b'), M([(98, 70), (110, 56, 1), (94, 50)], BL2, 'b')] +
  dome('front', top=-2, w=48, cy=44, n=9, amp=11, sweep=-0.3, seed=21, sb=70) +
  [M([(30, 40), (50, 36), (58, 50), (52, 70, 1), (44, 52)], 'mid', 'f'), strand([(40, 36), (46, 56)], 'shade', 'f', 1.0)] + _goggles_neck('front'),
  dome('side', top=-2, w=48, cy=44, n=9, amp=11, sweep=-0.3, seed=21, nape=86, fr=50) + _goggles_neck('side'),
  dome('back', top=-2, w=48, cy=44, n=9, amp=11, sweep=-0.3, seed=21, nape=86) + _goggles_neck('back'))

# Brick DeVille: pelo morado oscuro en pinchos largos de punta; unas gafas naranjas de montura verde le tapan los ojos y
# lleva una bufanda roja que ondea; boca de sonrisa ladeada
RED, GRN, ORG = _c('#c41a1a'), _c('#3a5a40'), _c('#f08a2a')
def _brick_goggles(view):
    if view == 'front':
        return [M([(12, 66), (50, 62), (88, 66), (86, 84), (60, 84), (50, 78), (40, 84), (14, 84)], GRN, 'f'),
                M([(18, 68), (46, 66), (46, 80), (40, 82), (20, 80)], ORG, 'f', False), M([(82, 68), (54, 66), (54, 80), (60, 82), (80, 80)], ORG, 'f', False),
                L(ell(34, 74, 2.6, 3), GRN, 'f', False), L(ell(66, 74, 2.6, 3), GRN, 'f', False)]
    if view == 'side':
        return [M([(66, 66), (92, 64), (92, 84), (70, 84)], GRN, 'f'), M([(72, 68), (90, 67), (90, 80), (74, 81)], ORG, 'f', False),
                W([(66, 70), (10, 64)], GRN, 3)]
    return [band('back', GRN, 62, 5)]
C('brick-deville', 'normal', P('#4a2656', '#c08a5e', iris='#3a6a3a', shade='#341a40'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, hairline=[(8, 62), (18, 46), (30, 56), (38, 42), (50, 54), (60, 40), (72, 54), (82, 44), (92, 62)]),
  dome('front', top=-6, w=48, cy=44, n=9, amp=16, sweep=0.2, seed=31, sb=72) + _brick_goggles('front') + scarf('front', RED, y=100, h=12) +
  [M([(70, 100), (104, 92), (112, 104, 1), (98, 110), (110, 118, 1), (80, 114)], RED, 'f')],
  dome('side', top=-6, w=48, cy=44, n=9, amp=16, sweep=0.2, seed=31, nape=88, fr=50) + _brick_goggles('side') + scarf('side', RED, y=100, h=12) +
  [M([(30, 102), (2, 96), (-10, 108, 1), (6, 112), (-4, 122, 1), (26, 114)], RED, 'f')],
  dome('back', top=-6, w=48, cy=44, n=9, amp=16, sweep=0.2, seed=31, nape=88) + _brick_goggles('back') + scarf('back', RED, y=100, h=12))

# C-Bear: casco morado con orejas de gato y una franja roja en medio con una luna negra; visera negra con el borde blanco
# en V que le tapa los ojos; solo se le ve la boca
PUR, CRED, VIS = _c('#5a2470'), _c('#cc2220'), _c('#141018')
def _cbear(view):
    if view == 'front':
        return [M([(6, 84), (4, 50), (8, 22), (6, -8, 1), (26, 10), (50, 4), (74, 10), (94, -8, 1), (92, 22), (96, 50), (94, 84), (50, 80)], PUR, 'f'),
                M([(38, 6), (62, 6), (64, 60), (36, 60)], CRED, 'f', False),
                L(ell(49, 32, 8, 9), VIS, 'f', False), L(ell(53, 30, 7, 8), CRED, 'f', False),
                M([(8, 60), (50, 70), (92, 60), (92, 76), (50, 86), (8, 76)], WHITE, 'f'),
                M([(10, 62), (50, 72), (90, 62), (90, 74), (50, 82), (10, 74)], VIS, 'f', False),
                M([(16, 50), (26, 40), (38, 54), (24, 56)], CRED, 'f', False), M([(84, 50), (74, 40), (62, 54), (76, 56)], CRED, 'f', False)]
    if view == 'side':
        return [M([(94, 84), (96, 50), (86, 22), (78, -6, 1), (66, 10), (44, 4), (18, 12), (4, 40), (4, 80), (30, 92), (60, 84)], PUR, 'f'),
                M([(54, 6), (74, 10), (84, 30), (60, 30)], CRED, 'f', False),
                M([(66, 62), (96, 60), (96, 78), (70, 80)], WHITE, 'f'), M([(68, 64), (94, 62), (94, 76), (72, 78)], VIS, 'f', False)]
    return [M([(6, 88), (4, 50), (8, 22), (6, -8, 1), (26, 10), (50, 4), (74, 10), (94, -8, 1), (92, 22), (96, 50), (94, 88), (50, 92)], PUR, 'f'),
            M([(40, 6), (60, 6), (60, 90), (40, 90)], CRED, 'f', False)]
C('c-bear', 'chica', P('#5a2470', '#f2e6d4', iris='#1e1414'),
  F(eyes='none', brows=False, mouth='line', mouth_y=94, hairline=False, ears=False),
  _cbear('front'), _cbear('side'), _cbear('back'))

# Chaa Mehn: pelo gris azulado oscuro peinado hacia atrás que acaba en un mechón por detrás; piel morena, cara alargada,
# ojos afilados de mirada de lado, nariz marcada y boca seria
C('chaa-mehn', 'delgado', P('#44606c', '#ad8760', iris='#1e1414', shade='#304650'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=96, face_front=face(chin=106), face_side=face_side(chin=5, nose=2),
    hairline=[(10, 60), (16, 44), (30, 36), (50, 34), (70, 36), (84, 44), (90, 60)], nose=(50, 86, 2.6)),
  dome('front', top=0, w=44, cy=44, sb=64, seed=41) + [strand([(40, 10), (36, 34)], 'shade', 'b', 1.0), strand([(60, 10), (64, 34)], 'shade', 'b', 1.0)],
  dome('side', top=0, w=44, cy=44, nape=90, fr=36, seed=41) + [M([(8, 70), (-4, 88), (4, 100, 1), (14, 84)])],
  dome('back', top=0, w=44, cy=44, nape=90, seed=41) + [M([(42, 82), (50, 104, 1), (58, 82)])])

# Champ Pignon: cabeza calva y pálida como un nabo con un penacho de hojas verdes arriba; pintura roja a franjas en la
# cara, ojos de panda (manchas negras), nariz de bolita naranja y dientes apretados; orejas de punta
LEAF, LEAFD, RDP = _c('#a8e2bc'), _c('#6aaa80'), _c('#8a2838')
def _leaves(x=50, y=4):
    return [M([(x, y + 8), (x - 20, y - 6), (x - 14, y - 12, 1), (x - 2, y)], LEAF, 'b'), M([(x, y + 8), (x + 20, y - 6), (x + 14, y - 12, 1), (x + 2, y)], LEAF, 'b'),
            M([(x - 4, y + 8), (x - 8, y - 18), (x, y - 26, 1), (x + 6, y - 16), (x + 4, y + 8)], LEAF, 'b'),
            strand([(x, y + 6), (x, y - 16)], LEAFD, 'b', 1.0)]
C('champ-pignon', 'bajito', P('#a8e2bc', '#e6ccb0', iris='#1e1414'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, face_front=face(w=4, chin=102, top=8), face_side=face_side(chin=3)),
  ears_pointy('front', h=10) + _leaves(50, 10) +
  [W([(22, 50), (20, 96)], RDP, 3.4), W([(30, 40), (30, 98)], RDP, 3.0), W([(70, 40), (70, 98)], RDP, 3.0), W([(78, 50), (80, 96)], RDP, 3.4),
   W([(40, 30), (42, 52)], RDP, 2.4), W([(60, 30), (58, 52)], RDP, 2.4),
   L(ell(36, 76, 8, 7), BLACK, 'f', False), L(ell(64, 76, 8, 7), BLACK, 'f', False),
   L(ell(36, 76, 3.6, 3.6), WHITE, 'f', False), L(ell(64, 76, 3.6, 3.6), WHITE, 'f', False),
   L(ell(36, 76, 1.8, 1.8), BLACK, 'f', False), L(ell(64, 76, 1.8, 1.8), BLACK, 'f', False),
   L(ell(50, 84, 4.4, 3.6), _c('#f08a5a'), 'f', False, True),
   L([(38, 94), (62, 94), (60, 100), (40, 100)], WHITE, 'f', False, True), W([(40, 97), (60, 97)], OUTC, 1.0)],
  ears_pointy('side', h=10) + _leaves(46, 8) + [W([(60, 40), (86, 50)], RDP, 2.6), W([(56, 60), (88, 66)], RDP, 2.6), W([(56, 84), (84, 94)], RDP, 2.6),
                                                 L(ell(80, 76, 5, 7), BLACK, 'f', False), L(ell(81, 76, 2, 2.4), WHITE, 'f', False)],
  ears_pointy('back', h=10) + _leaves(50, 10))

# Charley Horse (modelo 3D): pelo negro cortado a cepillo, plano arriba, con los lados cortos; gafas redondas de cristal
# blanco, ojos cerrados de felicidad, coloretes y una boquita de "o"
C('charley-horse', 'bajito', P('#2e2a28', '#f8bc80', iris='#1e1414', shade='#1e1a18', low='#5a4030'),
  F(eyes='none', brows=False, mouth='none', hairline=[(10, 60), (14, 44), (50, 42), (86, 44), (90, 60)], big_ears=2),
  [M([(12, 60), (10, 36), (88, 36), (88, 60), (80, 46), (20, 46)], 'low'),
   M([(10, 40), (10, 6), (14, 2), (86, 2), (90, 6), (90, 40), (50, 44)]),
   M([(60, 2), (86, 2), (90, 6), (90, 38), (76, 34)], 'shade', 'b', False)] +
  round_glasses('front', BLACK, y=76, r=9, lens=_c('#f4f4f8'), w=2.6) + squint(73, 14, 5) + blush(86, 26) +
  [L(ell(50, 94, 2.6, 3.2), OUTC, 'f', False)],
  [M([(56, 56), (62, 44), (88, 42), (88, 30), (20, 30), (6, 40), (8, 66), (24, 76), (42, 72), (52, 62)], 'low'),
   M([(90, 36), (90, 2), (14, 2), (8, 36), (50, 40)])] +
  round_glasses('side', BLACK, y=76, r=9, lens=_c('#f4f4f8'), w=2.6),
  [M([(10, 74), (8, 34), (92, 34), (90, 74), (50, 80)], 'low'), M([(8, 40), (10, 2), (90, 2), (92, 40), (50, 44)]),
   M([(60, 4), (90, 4), (92, 38), (74, 36)], 'shade', 'b', False)])

# Chester Horse Sr. (portero, modelo 3D): señor gordo con el pelo castaño corto que acaba en pico arriba y los lados rapados
# con rayas; bigote gris caído, gafas rectangulares amarillentas y ojos de cansado
C('chester-horse-sr', 'corpulento', P('#7c6450', '#dc9a5c', iris='#1e1414', shade='#5e4a3a'),
  F(eyes='closed', brows=True, mouth='none', hairline=[(8, 56), (14, 46), (30, 40), (50, 26), (70, 40), (86, 46), (92, 56)],
    face_front=face(w=9, chin=106, jaw=8, top=20), face_side=face_side(chin=6, jaw=8), big_ears=2, ear_out=5),
  [M([(10, 56), (12, 38), (30, 24), (50, 6, 1), (70, 24), (88, 38), (90, 56), (70, 44), (30, 44)])] +
  [L(blob([(30, 70), (46, 70), (46, 80), (30, 80)], 3), _c('#e8d888'), 'f', False), L(blob([(54, 70), (70, 70), (70, 80), (54, 80)], 3), _c('#e8d888'), 'f', False),
   L([(28, 70), (48, 70), (48, 81), (28, 81), (28, 70)], OUTC, 'f', False, False, 1.6), L([(52, 70), (72, 70), (72, 81), (52, 81), (52, 70)], OUTC, 'f', False, False, 1.6),
   L([(48, 74), (52, 74)], OUTC, 'f', False, False, 1.4), stache(92, 18, _c('#9a9088'))],
  [M([(60, 46), (66, 36), (84, 30), (64, 8, 1), (40, 12), (16, 26), (8, 48), (12, 70), (30, 74), (44, 66), (52, 54)]),
   W([(14, 46), (44, 50)], 'skin', 2.0), W([(14, 54), (44, 58)], 'skin', 2.0),
   L([(76, 70), (90, 70), (90, 81), (76, 81), (76, 70)], OUTC, 'f', False, False, 1.6), W([(76, 74), (50, 70)], OUTC, 1.4),
   L(blob([(78, 90), (90, 88), (92, 98), (82, 98)], 4), _c('#9a9088'), 'f', False, True)],
  [M([(12, 60), (12, 38), (30, 22), (50, 8, 1), (70, 22), (88, 38), (88, 60), (50, 64)]),
   W([(14, 48), (86, 48)], 'skin', 2.2), W([(14, 56), (86, 56)], 'skin', 2.2)])

# Chester Manc-Mann (portero): cuernos de carnero color crema enroscados a los lados de una gorra azul, con mechones castaños
# asomando; cara rojiza con barba castaña, ojos medio cerrados, nariz roja y boca seria
HORN, HORND, CAPB, BRN = _c('#ece0c4'), _c('#c8b490'), _c('#1e3a6a'), _c('#7a5a1a')
def _ram(view):
    if view == 'front':
        return [L(ell(4, 70, 13, 16), HORN, 'f'), L(ell(4, 70, 7, 9), HORND, 'f', False), L(ell(96, 70, 13, 16), HORN, 'f'), L(ell(96, 70, 7, 9), HORND, 'f', False),
                M([(4, 44), (2, 28), (14, 22), (20, 36)], BRN, 'b'), M([(96, 44), (98, 28), (86, 22), (80, 36)], BRN, 'b'),
                cap('front', CAPB, top=6, rim=50, w=44, z='f'),
                M([(18, 50), (82, 50), (80, 60), (20, 60)], BRN, 'f')]
    if view == 'side':
        return [L(ell(40, 66, 15, 17), HORN, 'f'), L(ell(40, 66, 8, 9), HORND, 'f', False), cap('side', CAPB, top=6, rim=50, w=44, z='f'),
                M([(70, 50), (92, 48), (90, 58), (72, 58)], BRN, 'f')]
    return [L(ell(4, 70, 13, 16), HORN, 'f'), L(ell(96, 70, 13, 16), HORN, 'f'), cap('back', CAPB, top=6, rim=50, w=44, z='f'),
            M([(10, 60), (90, 60), (88, 84), (50, 90), (12, 84)], BRN, 'f')]
C('chester-manc-mann', 'corpulento', P('#7a5a1a', '#c8704e', iris='#1e1414', shade='#5a4012'),
  F(eyes='closed', brows=False, mouth='frown', mouth_y=92, hairline=False, ears=False, face_front=face(w=4, chin=104, jaw=4), nose=(50, 84, 4)),
  _ram('front') + [M([(18, 86), (30, 104), (50, 112), (70, 104), (82, 86), (70, 96), (60, 98), (50, 96), (40, 98), (30, 96)], BRN, 'f'),
                   W([(26, 70), (44, 70)], OUTC, 2.6), W([(56, 70), (74, 70)], OUTC, 2.6),
                   L(ell(50, 84, 4.6, 4), _c('#e04a2a'), 'f', False, True)],
  _ram('side') + [M([(56, 86), (66, 104), (82, 104), (88, 90), (80, 96)], BRN, 'f'), L(ell(88, 84, 3, 3.6), _c('#e04a2a'), 'f', False, True)],
  _ram('back'))

# Choen Ryo: pelo rojo en pinchos enormes hacia arriba y los lados con mechones blancos en medio; pintura de kabuki roja
# alrededor de los ojos azules y rayas negras en las mejillas; boca pequeña roja
KRED, WHT2 = _c('#c02a2a'), _c('#f4ece4')
C('choen-ryo', 'normal', P('#b42c2d', '#b28a6a', iris='#3a7ac0', shade='#8a2020'),
  F(eyes='none', brows=False, mouth='none', hairline=[(8, 62), (18, 46), (30, 56), (42, 44), (50, 56), (58, 44), (70, 56), (82, 46), (92, 62)]),
  [M([(10, 70), (4, 40), (-10, 18, 1), (12, 22), (14, -14, 1), (30, 12), (36, -30, 1), (50, 4), (64, -30, 1), (70, 12), (86, -14, 1), (88, 22), (110, 18, 1),
      (96, 40), (90, 70), (80, 52), (20, 52)]),
   M([(40, 10), (36, -30, 1), (46, 4)], WHT2, 'b', False), M([(60, 10), (64, -30, 1), (54, 4)], WHT2, 'b', False),
   M([(48, 30), (50, 4), (54, 30)], WHT2, 'b', False),
   M([(22, 68), (40, 70), (44, 76), (36, 74), (24, 76)], KRED, 'f', False), M([(78, 68), (60, 70), (56, 76), (64, 74), (76, 76)], KRED, 'f', False)] +
  sharp_eyes(_c('#3a7ac0'), 78) +
  [W([(28, 84), (32, 98)], BLACK, 1.8), W([(72, 84), (68, 98)], BLACK, 1.8),
   L(blob([(47, 94), (53, 94), (50, 99)], 2), KRED, 'f', False)],
  [M([(56, 62), (64, 50), (84, 46), (96, 30), (110, 22, 1), (90, 16), (88, -18, 1), (70, 6), (54, -30, 1), (42, 6), (20, -18, 1), (18, 14), (-4, 18, 1), (6, 40),
      (4, 66), (20, 80), (42, 76), (52, 68)]),
   M([(48, 6), (54, -30, 1), (58, 4)], WHT2, 'b', False)] +
  sharp_eye_side(_c('#3a7ac0'), 78) + [M([(72, 70), (88, 68), (88, 74), (74, 76)], KRED, 'f', False), W([(74, 86), (80, 98)], BLACK, 1.8)],
  [M([(10, 82), (4, 40), (-10, 18, 1), (12, 22), (14, -14, 1), (30, 12), (36, -30, 1), (50, 4), (64, -30, 1), (70, 12), (86, -14, 1), (88, 22), (110, 18, 1),
      (96, 40), (90, 82), (50, 88)]),
   M([(40, 10), (36, -30, 1), (46, 4)], WHT2, 'f', False), M([(60, 10), (64, -30, 1), (54, 4)], WHT2, 'f', False)])

# Chomo-Ba: melena malva revuelta y abultada con una corona dorada pequeña encima; cicatriz en X en la frente, ojos azules
# afilados, perilla y sonrisa de lado
GOLD = _c('#f2c43a')
def _crown(x=50, y=2):
    return [M([(x - 14, y + 8), (x - 16, y - 8, 1), (x - 8, y), (x, y - 12, 1), (x + 8, y), (x + 16, y - 8, 1), (x + 14, y + 8)], GOLD, 'f'),
            L(ell(x, y + 2, 2.4, 2.4), _c('#c83a3a'), 'f', False)]
C('chomo-ba', 'normal', P('#84504e', '#cc9c6a', iris='#3a7ac0', shade='#6a3c36'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=[(8, 66), (18, 52), (30, 60), (38, 44), (50, 50), (62, 42), (72, 56), (84, 50), (92, 66)]),
  dome('front', top=2, w=50, cy=46, n=10, amp=10, soft=True, seed=51, sb=78) + _crown(52, 2) +
  [W([(40, 54), (50, 62)], _c('#8a5a40'), 1.6), W([(50, 54), (40, 62)], _c('#8a5a40'), 1.6),
   L(blob([(46, 100), (54, 100), (50, 108)], 2), 'mid', 'f', False)],
  dome('side', top=2, w=50, cy=46, n=10, amp=10, soft=True, seed=51, nape=92, fr=50) + _crown(48, 0) +
  [L(blob([(80, 100), (86, 100), (82, 108)], 2), 'mid', 'f', False)],
  dome('back', top=2, w=50, cy=46, n=10, amp=10, soft=True, seed=51, nape=92) + _crown(50, 2))

# Constance Durand: melena azul lavanda larga y en mechones de punta, con un mechón crema delante de la cara, una horquilla
# dorada y una trenza a un lado atada con anillas doradas; piel morena, ojos verde agua y ceño fruncido
CRM = _c('#f0e2b0')
C('constance-durand', 'chica', P('#8ca2d8', '#cc996c', iris='#30a0a0', shade='#6a7ab8'),
  F(eyes='big', brows='angry', mouth='frown', mouth_y=93, hairline=[(8, 68), (16, 50), (26, 60), (34, 44), (46, 56), (54, 42), (66, 54), (78, 44), (92, 68)]),
  dome('front', top=0, w=48, cy=46, n=8, amp=10, sweep=-0.4, seed=61, long=100, flare=8) +
  [M([(36, 44), (42, 46), (38, 90, 1), (32, 70)], CRM, 'f'), W([(56, 46), (66, 50)], GOLD, 2.4),
   M([(80, 80), (90, 84), (92, 112), (86, 126, 1), (80, 112)], 'mid', 'f'), W([(82, 104), (92, 104)], GOLD, 2.2), W([(82, 112), (90, 112)], GOLD, 2.2)],
  dome('side', top=0, w=48, cy=46, n=8, amp=10, sweep=-0.4, seed=61, long=100, flare=8, fr=50),
  dome('back', top=0, w=48, cy=46, n=8, amp=10, sweep=-0.4, seed=61, long=100, flare=8, ends=4) +
  [M([(12, 90), (22, 94), (22, 118), (16, 128, 1), (12, 116)], 'mid', 'f')])

# Crester Lipp: pelo rubio muy alto en pinchos hacia arriba, con los lados oscuros; piel morena, ojos redondos muy abiertos
# y una boquita de labios en "o"
C('crester-lipp', 'normal', P('#ecce98', '#bc8c68', iris='#1e1414', shade='#c8a870', low='#2a2420'),
  F(eyes='round', brows=True, mouth='none', hairline=[(8, 62), (14, 50), (30, 46), (50, 44), (70, 46), (86, 50), (92, 62)]),
  [M([(10, 64), (8, 44), (20, 40), (80, 40), (92, 44), (90, 64), (80, 52), (20, 52)], 'low'),
   M([(14, 46), (8, 16), (18, 22), (16, -14, 1), (30, 8), (36, -26, 1), (48, 2), (58, -24, 1), (64, 6), (82, -12, 1), (80, 18), (94, 14, 1), (88, 46)]),
   M([(56, -4), (58, -24), (64, 6), (82, -12), (80, 18), (94, 14), (86, 44), (70, 30)], 'shade', 'b', False),
   L(blob([(44, 92), (50, 88), (56, 92), (54, 98), (46, 98)], 4), _c('#8a5a40'), 'f', False, True), L(ell(50, 93, 2.4, 2), _c('#4a2a20'), 'f', False)],
  [M([(56, 60), (62, 48), (82, 44), (84, 30), (88, 6, 1), (70, 10), (66, -20, 1), (50, 4), (36, -16, 1), (30, 10), (10, 18), (6, 40), (10, 64), (30, 70), (46, 62)]),
   M([(10, 56), (40, 50), (52, 60), (44, 70), (24, 72)], 'low', 'b', False)],
  [M([(10, 80), (8, 44), (14, 16), (16, -14, 1), (30, 8), (36, -26, 1), (48, 2), (58, -24, 1), (64, 6), (82, -12, 1), (80, 18), (90, 40), (90, 80), (50, 86)]),
   M([(10, 62), (90, 62), (90, 82), (50, 88), (10, 82)], 'low', 'f', False)])

# Dennosuke Tokuni: peinado de samurái niño, la coronilla rapada con un moño negro arriba atado con una cinta blanca y los
# lados grises; cara redonda amarilla pálida, coloretes rojos redondos, ojos de ranura y una boca roja en coma
def _chon(view):
    if view == 'front':
        return [M([(10, 60), (8, 40), (14, 30), (24, 42), (22, 60)], 'light'), M([(90, 60), (92, 40), (86, 30), (76, 42), (78, 60)], 'light'),
                L(blob([(18, 50), (16, 30), (30, 14), (50, 8), (70, 14), (84, 30), (82, 50)], 8), 'skin'),
                L(ell(28, -2, 11, 10), 'mid', 'f'), L(ell(72, -2, 11, 10), 'mid', 'f'), M([(36, 6), (64, 6), (64, 14), (36, 14)], WHITE, 'f'),
                M([(36, 0), (50, -8), (64, 0), (64, 8), (36, 8)], 'mid', 'f')]
    if view == 'side':
        return [M([(44, 64), (20, 70), (8, 52), (12, 38), (36, 42)], 'light'), L(blob([(10, 40), (14, 18), (40, 6), (70, 10), (84, 26), (50, 30)], 6), 'skin'),
                L(ell(40, -2, 13, 10), 'mid', 'f'), M([(28, 6), (52, 6), (52, 12), (28, 12)], WHITE, 'f')]
    return [M([(10, 76), (8, 40), (90, 40), (92, 76), (50, 84)], 'light'), L(blob([(14, 50), (16, 26), (50, 8), (84, 26), (86, 50)], 8), 'skin'),
            L(ell(28, -2, 11, 10), 'mid', 'f'), L(ell(72, -2, 11, 10), 'mid', 'f'), M([(36, 6), (64, 6), (64, 14), (36, 14)], WHITE, 'f')]
CRD = _c('#e83020')
C('dennosuke-tokuni', 'normal', P('#121214', '#fcd08a', iris='#1e1414', light='#a8b8a8'),
  F(eyes='none', brows=False, mouth='none', hairline=False, face_front=face(w=5, chin=104, top=14), face_side=face_side(chin=3)),
  _chon('front') + [W([(28, 72), (42, 74)], OUTC, 2.2), W([(58, 74), (72, 72)], OUTC, 2.2), W([(30, 64), (40, 62)], OUTC, 1.6), W([(60, 62), (70, 64)], OUTC, 1.6),
                    L(ell(26, 84, 7, 7), CRD, 'f', False), L(ell(74, 84, 7, 7), CRD, 'f', False),
                    L(blob([(44, 92), (56, 92), (58, 98), (52, 104), (46, 100)], 4), CRD, 'f', False), W([(42, 92), (58, 92)], OUTC, 1.6)],
  _chon('side') + [W([(76, 74), (88, 74)], OUTC, 2.2), L(ell(76, 84, 6, 7), CRD, 'f', False)],
  _chon('back'))

# Dijea Graffin: media melena malva lisa con una horquilla blanca a un lado; ojos afilados rosas y ceño fruncido
C('dijea-graffin', 'chica', P('#a05c6a', '#fcd0a0', iris='#e07ab0', shade='#7a4450'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=[(8, 66), (16, 50), (30, 44), (40, 54), (48, 42), (60, 48), (72, 42), (84, 52), (92, 66)]),
  dome('front', top=2, w=46, cy=46, long=94, flare=6, seed=71) + [W([(76, 46), (80, 58)], WHITE, 2.0), W([(80, 46), (84, 58)], WHITE, 2.0)],
  dome('side', top=2, w=46, cy=46, long=94, flare=6, fr=48, seed=71),
  dome('back', top=2, w=46, cy=46, long=94, flare=6, ends=3, seed=71))

# Eddie Barry Burroughs: capucha verde oscuro y pelo beige con un flequillo largo de mechones que le tapa un ojo; orejas
# de punta de elfo, ojo rojo y boca seria
HOODG = _c('#28503e')
C('eddie-barry-burroughs', 'normal', P('#c8b698', '#fcd28c', iris='#c02a1a', shade='#a08a70'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=93, hairline=False, ears=False),
  hood('front', HOODG, top=-6, w=2, low=108, face_hole=[(20, 104), (14, 70), (20, 44), (50, 32), (80, 44), (86, 70), (80, 104), (50, 112)]) +
  ears_pointy('front', h=14) +
  [M([(16, 104), (14, 60), (22, 40), (50, 34), (78, 40), (86, 60), (84, 100), (78, 70), (60, 56), (48, 70, 1), (40, 58), (24, 64), (20, 90)], 'mid', 'f'),
   M([(18, 52), (40, 40), (60, 44), (48, 92, 1), (36, 64), (20, 76)], 'mid', 'f'),
   strand([(24, 56), (38, 80)], 'shade', 'f', 1.0), M([(14, 104), (-6, 92, 1), (12, 80)], 'mid', 'f')],
  hood('side', HOODG, top=-6, w=2) + ears_pointy('side', h=14) + [M([(70, 40), (90, 44), (92, 70), (86, 92, 1), (80, 66)], 'mid', 'f')],
  hood('back', HOODG, top=-6, w=2, low=108))

# Emmy Altava: media melena castaña ondulada y abultada, cara sencilla de ojos de punto y una sonrisa
C('emmy-altava', 'chica', P('#523a22', '#ecb886', iris='#1e1414', shade='#3a2816'),
  F(eyes='dot', brows=True, mouth='smile', mouth_y=92, hairline=[(8, 62), (18, 50), (32, 44), (50, 46), (62, 40), (76, 44), (86, 52), (92, 62)]),
  dome('front', top=2, w=50, cy=46, n=6, amp=6, soft=True, long=100, flare=10, seed=81),
  dome('side', top=2, w=50, cy=46, n=6, amp=6, soft=True, long=100, flare=10, fr=48, seed=81),
  dome('back', top=2, w=50, cy=46, n=6, amp=6, soft=True, long=100, flare=10, ends=4, seed=81))

# Emosuke Rokudo: pelo verde negruzco tirante hacia atrás con un moño en punta arriba; cejas de kabuki pintadas de rojo y
# los ojos naranjas afilados; boca seria
C('emosuke-rokudo', 'normal', P('#18241c', '#f6bc80', iris='#e08a20', shade='#0e1610'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=94, hairline=[(10, 62), (14, 46), (30, 40), (50, 54), (70, 40), (86, 46), (90, 62)]),
  dome('front', top=4, w=44, cy=46, sb=66, seed=91) +
  [M([(42, 8), (44, -14), (50, -30, 1), (56, -14), (58, 8)]), L(ell(50, 6, 6, 3), _c('#c8a040'), 'f', False)] +
  [M([(20, 66), (40, 62), (46, 68), (38, 70)], KRED, 'f', False), M([(80, 66), (60, 62), (54, 68), (62, 70)], KRED, 'f', False)] +
  sharp_eyes(_c('#e08a20'), 77) + [W([(22, 64), (44, 70)], BLACK, 2.8), W([(78, 64), (56, 70)], BLACK, 2.8)],
  dome('side', top=4, w=44, cy=46, nape=86, fr=40, seed=91) + [M([(40, 6), (40, -16), (46, -30, 1), (52, -14), (50, 6)])] +
  sharp_eye_side(_c('#e08a20'), 77) + [W([(70, 64), (90, 70)], BLACK, 2.8)],
  dome('back', top=4, w=44, cy=46, nape=86, seed=91) + [M([(42, 8), (44, -14), (50, -30, 1), (56, -14), (58, 8)])])

# Endura Vigil: melena enorme y salvaje azul turquesa claro que se abre en mechones de punta; piel morena, ojos redondos
# con líneas rojas pintadas alrededor y una sonrisa de dientes
C('endura-vigil', 'chica', P('#92d6d8', '#c08468', iris='#3a5ab0', shade='#6aaeb0'),
  F(eyes='round', brows=False, mouth='grin', mouth_y=94, hairline=[(8, 64), (18, 54), (30, 60), (40, 50), (50, 58), (60, 50), (70, 60), (82, 54), (92, 64)]),
  dome('front', top=-6, w=56, cy=46, n=12, amp=14, seed=101, long=112, flare=16) +
  [W(quad((24, 70), (34, 66), (44, 72)), _c('#d83a3a'), 1.4), W(quad((56, 72), (66, 66), (76, 70)), _c('#d83a3a'), 1.4),
   W([(30, 84), (38, 80)], _c('#d83a3a'), 1.4), W([(70, 84), (62, 80)], _c('#d83a3a'), 1.4)],
  dome('side', top=-6, w=56, cy=46, n=12, amp=14, seed=101, long=112, flare=16, fr=52),
  dome('back', top=-6, w=56, cy=46, n=12, amp=14, seed=101, long=112, flare=16, ends=5))

# Eoin Geary: pelo azul grisáceo en pinchos, dos de ellos hacia arriba como cuernos, con una cinta blanca en la frente; ojos
# azules grandes y una sonrisa de dientes
C('eoin-geary', 'normal', P('#88a2c0', '#f8d08e', iris='#2a6ac0', shade='#6a80a0'),
  F(eyes='big', brows='angry', mouth='grin', mouth_y=93, hairline=[(8, 64), (18, 52), (28, 62), (38, 54), (50, 68), (62, 54), (72, 62), (82, 52), (92, 64)]),
  dome('front', top=0, w=48, cy=46, n=8, amp=10, seed=111, sb=74) +
  [M([(20, 30), (10, 2), (14, -18, 1), (24, 8), (32, 24)]), M([(80, 30), (90, 2), (86, -18, 1), (76, 8), (68, 24)]), band('front', WHITE, 48, 6)],
  dome('side', top=0, w=48, cy=46, n=8, amp=10, seed=111, nape=88, fr=52) + [M([(40, 20), (44, -6), (52, -18, 1), (54, 10)]), band('side', WHITE, 46, 6)],
  dome('back', top=0, w=48, cy=46, n=8, amp=10, seed=111, nape=88) +
  [M([(20, 30), (10, 2), (14, -18, 1), (24, 8), (32, 24)]), M([(80, 30), (90, 2), (86, -18, 1), (76, 8), (68, 24)]), band('back', WHITE, 48, 6)])

# Erneste Larue (portero): melena lisa blanca crema hasta los hombros, peinada hacia un lado con la raya marcada; ojos azules
# afilados y ceño fruncido
C('erneste-larue', 'delgado', P('#ece0d6', '#f4d6b8', iris='#3a6ab8', shade='#c4b6ac'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, face_front=face(chin=104), face_side=face_side(chin=3),
    hairline=[(8, 70), (16, 50), (26, 44), (36, 54), (40, 40), (60, 40), (78, 46), (88, 56), (92, 70)]),
  dome('front', top=0, w=46, cy=44, long=106, flare=4, seed=121) + [M([(70, 40), (90, 52), (92, 110), (86, 116, 1), (80, 90)], 'mid', 'f'),
                                                                     strand([(40, 4), (36, 40)], 'shade', 'b', 1.0)],
  dome('side', top=0, w=46, cy=44, long=106, flare=4, fr=44, seed=121),
  dome('back', top=0, w=46, cy=44, long=106, flare=4, ends=3, seed=121))

# Esme La Transe: melena negra lisa y larga con raya al medio, una cadena en la frente con una gema azul y pendientes largos
# de cuentas; piel morena, ojos cerrados con pestañas negras gruesas
GEM, BEAD1, BEAD2 = _c('#40c8d8'), _c('#a06a8a'), _c('#e83a6a')
def _earrings(view):
    if view == 'front':
        out = []
        for x in (12, 88):
            out += [W([(x, 78), (x, 116)], BLACK, 1.2), L(ell(x, 92, 3.6, 3.6), BEAD1, 'f', False, True), L(ell(x, 104, 2.6, 2.6), BEAD2, 'f', False, True),
                    L(ell(x, 112, 2.2, 2.2), GEM, 'f', False, True)]
        return out
    return [W([(48, 78), (48, 116)], BLACK, 1.2), L(ell(48, 92, 3.6, 3.6), BEAD1, 'f', False, True), L(ell(48, 104, 2.6, 2.6), BEAD2, 'f', False, True)]
C('esme-la-transe', 'chica', P('#16100e', '#cc966a', iris='#1e1414', shade='#0a0806'),
  F(eyes='closed', brows=True, mouth='frown', mouth_y=94, hairline=[(10, 70), (16, 50), (30, 40), (48, 36), (50, 44), (52, 36), (70, 40), (84, 50), (90, 70)]),
  dome('front', top=2, w=46, cy=44, long=128, flare=2, seed=131) +
  [W(quad((18, 54), (50, 62), (82, 54)), _c('#2a2420'), 1.2), L(blob([(46, 60), (54, 60), (52, 70), (50, 72), (48, 70)], 3), GEM, 'f', False, True)] +
  _earrings('front') + [W([(26, 72), (38, 70)], BLACK, 2.6), W([(62, 70), (74, 72)], BLACK, 2.6)],
  dome('side', top=2, w=46, cy=44, long=128, flare=2, fr=44, seed=131) + _earrings('side'),
  dome('back', top=2, w=46, cy=44, long=128, flare=2, ends=3, seed=131))

# Fae Grimm: pelo rosa recogido hacia arriba en un remolino alto que acaba en punta curvada; orejas de elfo con un pendiente
# dorado; piel muy pálida, ojos rojos y sonrisa
C('fae-grimm', 'chica', P('#f8a2b6', '#fdf0d8', iris='#c02a2a', shade='#d87a90'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=93, hairline=[(12, 62), (16, 48), (30, 40), (50, 44), (70, 40), (84, 48), (88, 62)], ears=False),
  ears_pointy('front', h=16) +
  [M([(14, 62), (12, 36), (24, 16), (40, 2), (40, -20), (52, -36), (68, -36), (72, -28, 1), (60, -26), (56, -14), (64, 4), (80, 18), (88, 36), (86, 62), (76, 46), (24, 46)]),
   M([(52, -30), (62, -34), (58, -16), (64, 4), (80, 18), (88, 36), (86, 58), (70, 30)], 'shade', 'b', False),
   L(ell(96, 62, 2.2, 3.2), GOLD, 'f', False, True)],
  ears_pointy('side', h=16) +
  [M([(56, 56), (62, 44), (82, 40), (86, 24), (64, 4), (54, -16), (46, -34), (34, -34), (30, -26, 1), (40, -24), (40, -8), (20, 8), (6, 30), (8, 54), (24, 64), (44, 60)])],
  ears_pointy('back', h=16) +
  [M([(14, 70), (12, 36), (24, 16), (40, 2), (40, -20), (52, -36), (68, -36), (72, -28, 1), (60, -26), (56, -14), (64, 4), (80, 18), (88, 36), (86, 70), (50, 76)])])

# Fanqs Kamagen: pelo azul marino en pinchos con unas gafas de aviador de cristales naranjas con los números 2 y 4 en la
# frente; ojos rojos y sonrisa
NUMC, GRYF = _c('#d85a2a'), _c('#9aa0a8')
def _num_goggles(view):
    if view == 'front':
        return [band('front', GRYF, 44, 5), L(ell(34, 44, 14, 12), GRYF, 'f'), L(ell(66, 44, 14, 12), GRYF, 'f'),
                L(ell(34, 44, 10.4, 9), NUMC, 'f', False), L(ell(66, 44, 10.4, 9), NUMC, 'f', False),
                W([(30, 39), (37, 39), (37, 44), (30, 50), (38, 50)], WHITE, 1.8), W([(68, 37), (62, 46), (71, 46)], WHITE, 1.8), W([(68, 37), (68, 51)], WHITE, 1.8)]
    if view == 'side':
        return [band('side', GRYF, 42, 5), L(ell(80, 44, 6, 8), GRYF, 'f'), L(ell(80, 44, 4, 6), NUMC, 'f', False)]
    return [band('back', GRYF, 44, 5)]
C('fanqs-kamagen', 'normal', P('#2a3a7a', '#f8bc80', iris='#c02a1a', shade='#1e2a5a'),
  F(eyes='big', brows='angry', mouth='smile', mouth_y=93, hairline=[(8, 66), (18, 54), (26, 70), (34, 56), (46, 66), (54, 56), (66, 66), (74, 56), (82, 70), (92, 66)]),
  dome('front', top=-6, w=48, cy=44, n=9, amp=16, seed=141, sb=84) + _num_goggles('front'),
  dome('side', top=-6, w=48, cy=44, n=9, amp=16, seed=141, nape=90, fr=56) + _num_goggles('side'),
  dome('back', top=-6, w=48, cy=44, n=9, amp=16, seed=141, nape=90) + _num_goggles('back'))

# Faythe Heeler (modelo 3D): media melena gris morado con el flequillo recto y una coleta baja atada con una goma rosa;
# ojos azules y ceño fruncido
PNKS = _c('#f0b8d0')
C('faythe-heeler', 'chica', P('#6c5e66', '#f8d8b8', iris='#3a5ab0', shade='#4c4048'),
  F(eyes='big', brows='angry', mouth='frown', mouth_y=93, hairline=[(8, 62), (16, 58), (50, 58), (84, 58), (92, 62)]),
  [M([(14, 92), (8, 60), (10, 30), (28, 8), (50, 2), (72, 8), (90, 30), (92, 60), (86, 92), (82, 58), (18, 58)]),
   M([(60, 4), (82, 14), (92, 40), (90, 86), (84, 60), (80, 30)], 'shade', 'b', False),
   M([(80, 94), (90, 96), (92, 116), (84, 124, 1), (80, 110)]), L(ell(85, 96, 5, 3.4), PNKS, 'f', False, True)],
  [M([(80, 58), (88, 40), (82, 14), (58, 0), (30, 2), (10, 18), (2, 44), (4, 74), (20, 88), (40, 84), (54, 76), (60, 62)]),
   M([(18, 82), (6, 100), (12, 116, 1), (24, 96)]), L(ell(18, 86, 4, 5), PNKS, 'f', False, True)],
  [M([(10, 88), (6, 56), (10, 26), (28, 6), (50, 2), (72, 6), (90, 26), (94, 56), (90, 88), (50, 94)]),
   M([(44, 88), (56, 88), (54, 114), (50, 122, 1), (46, 114)]), L(ell(50, 90, 6, 3.4), PNKS, 'f', False, True)])

# Gammon Checker (portero, modelo 3D): gorra roja y el pelo castaño oscuro en pinchos que salen por los lados y por detrás;
# piel tostada, perilla, ojos redondos y boca seria; un cordón negro al cuello
CAPR = _c('#cc2e32')
C('gammon-checker', 'normal', P('#2c1e18', '#e8a666', iris='#1e1414', shade='#1e1410'),
  F(eyes='round', brows=True, mouth='frown', mouth_y=93, hairline=[(8, 66), (18, 54), (30, 64), (40, 52), (50, 70), (58, 54), (70, 62), (82, 54), (92, 66)]),
  [M([(8, 66), (-10, 56, 1), (2, 46), (-12, 32, 1), (8, 30), (20, 40), (24, 64)]), M(mx([(8, 66), (-10, 56, 1), (2, 46), (-12, 32, 1), (8, 30), (20, 40), (24, 64)])),
   M([(16, 62), (14, 40), (84, 40), (86, 62), (60, 54), (52, 72, 1), (44, 54)]),
   cap('front', CAPR, top=0, rim=42, w=44, z='f'), M([(30, 40), (70, 40), (72, 46), (28, 46)], _c('#a02024'), 'f', False),
   L(blob([(46, 100), (54, 100), (50, 108)], 2), 'mid', 'f', False), W([(30, 104), (40, 124)], BLACK, 1.2), W([(70, 104), (60, 124)], BLACK, 1.2)],
  [M([(56, 70), (40, 64), (20, 74, 1), (10, 58), (-8, 56, 1), (4, 44), (-6, 30, 1), (14, 30), (40, 40), (60, 50)]),
   cap('side', CAPR, top=0, rim=42, w=44, z='f'), M([(78, 40), (106, 44), (104, 50), (80, 48)], CAPR, 'f')],
  [M([(4, 90), (-12, 66, 1), (4, 64), (-10, 44, 1), (10, 44), (20, 40), (80, 40), (90, 44), (110, 44, 1), (96, 64), (112, 66, 1), (96, 90), (80, 82), (70, 96, 1),
      (58, 82), (50, 98, 1), (42, 82), (30, 96, 1), (20, 82)]),
   cap('back', CAPR, top=0, rim=40, w=44, z='f')])

# Genko Ka: tupé azul marino en pinchos altos hacia atrás; un parche rojo con una raya blanca en un ojo, pendiente verde
# agua, perilla y sonrisa ladeada
EPR = _c('#c42a2a')
C('genko-ka', 'normal', P('#2c3f68', '#f0c08e', iris='#3a5ab0', shade='#1e2c4c'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=[(8, 62), (16, 48), (28, 54), (36, 44), (50, 50), (64, 42), (76, 50), (86, 46), (92, 62)]),
  dome('front', top=-12, w=48, cy=40, n=8, amp=16, sweep=0.4, seed=151, sb=76) +
  [M([(54, 66), (82, 64), (84, 84), (60, 86), (54, 78)], EPR, 'f'), W([(56, 70), (82, 80)], WHITE, 2.0), W([(56, 66), (16, 58)], BLACK, 1.6),
   L(ell(14, 82, 2, 2.6), _c('#30b0a0'), 'f', False, True), L(blob([(46, 100), (54, 100), (50, 106)], 2), 'mid', 'f', False)],
  dome('side', top=-12, w=48, cy=40, n=8, amp=16, sweep=0.4, seed=151, nape=86, fr=48) +
  [M([(74, 66), (90, 64), (90, 84), (76, 86)], EPR, 'f'), W([(74, 66), (40, 62)], BLACK, 1.6)],
  dome('back', top=-12, w=48, cy=40, n=8, amp=16, sweep=0.4, seed=151, nape=86))

# Gezun Dight: melena azul pizarra hasta el cuello con las puntas hacia fuera y un mechón celeste delante; ojos azules
# afilados y ceño fruncido
SKYB = _c('#a0d8f0')
C('gezun-dight', 'normal', P('#445e72', '#f8bc80', iris='#40a0d8', shade='#30465a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=[(8, 66), (16, 50), (28, 44), (40, 54), (50, 42), (64, 52), (76, 44), (86, 52), (92, 66)]),
  dome('front', top=0, w=48, cy=46, long=96, flare=10, seed=161) + [M([(62, 44), (70, 44), (68, 66, 1)], SKYB, 'f')],
  dome('side', top=0, w=48, cy=46, long=96, flare=10, fr=48, seed=161),
  dome('back', top=0, w=48, cy=46, long=96, flare=10, ends=3, seed=161))

# Gilles de Rais (modelo 3D): pelo negro corto y tirante con entradas en pico; una barba fina de línea negra que le recorre
# la mandíbula hasta la perilla; ojeras grises y ojos afilados
C('gilles-de-rais', 'delgado', P('#38343c', '#e2ccae', iris='#8a3a2a', shade='#24222a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, face_front=face(chin=106), face_side=face_side(chin=5),
    hairline=[(12, 62), (16, 46), (28, 40), (40, 46), (50, 30), (60, 46), (72, 40), (84, 46), (88, 62)]),
  dome('front', top=2, w=44, cy=46, sb=64, seed=171, shade=False) +
  [W(quad((18, 76), (22, 98), (42, 102)), BLACK, 3.2), W(quad((82, 76), (78, 98), (58, 102)), BLACK, 3.2),
   L(blob([(44, 100), (56, 100), (50, 112)], 2), BLACK, 'f', False)],
  dome('side', top=2, w=44, cy=46, nape=84, fr=40, seed=171, shade=False) + [W(quad((54, 72), (60, 96), (80, 104)), BLACK, 3.2)],
  dome('back', top=2, w=44, cy=46, nape=84, seed=171, shade=False))

# Giselle Roque: pelo verde oliva en grandes rulos a los lados y una boina plana encima; ojos grandes, coloretes y sonrisa
BERET, BERETD = _c('#8a9a72'), _c('#5a5038')
def _beret(view):
    if view == 'front':
        return [L(blob([(-2, 22), (10, 6), (50, 2), (90, 6), (102, 22), (90, 30), (50, 28), (10, 30)], 6), BERET, 'f'),
                L(blob([(0, 24), (50, 28), (100, 24), (96, 32), (50, 34), (4, 32)], 4), BERETD, 'f', False)]
    if view == 'side':
        return [L(blob([(0, 22), (20, 4), (60, 0), (98, 14), (92, 28), (50, 28), (6, 32)], 6), BERET, 'f')]
    return [L(blob([(-2, 22), (10, 6), (50, 2), (90, 6), (102, 22), (90, 30), (50, 28), (10, 30)], 6), BERET, 'f')]
C('giselle-roque', 'chica', P('#8e9e78', '#f8ba7e', iris='#1e1414', shade='#6a7a58'),
  F(eyes='big', brows=True, mouth='grin', mouth_y=93, hairline=[(8, 62), (16, 52), (30, 44), (50, 42), (70, 44), (84, 52), (92, 62)]),
  [L(ell(8, 60, 12, 16)), L(ell(92, 60, 12, 16)), L(ell(6, 90, 11, 14)), L(ell(94, 90, 11, 14))] +
  dome('front', top=10, w=46, cy=44, sb=70, seed=181) + _beret('front') + blush(86, 24),
  [L(ell(40, 66, 14, 18)), L(ell(36, 94, 12, 14))] + dome('side', top=10, w=46, cy=44, nape=90, fr=48, seed=181) + _beret('side'),
  [L(ell(8, 60, 12, 16)), L(ell(92, 60, 12, 16)), L(ell(6, 90, 11, 14)), L(ell(94, 90, 11, 14))] + dome('back', top=10, w=46, cy=44, nape=94, seed=181) + _beret('back'))

# Giv-R Trupal (portero): una capucha gris con forma de tiburón martillo y una aleta curvada encima; piel muy pálida, ojos
# amarillos con la pupila roja y boca seria
SHK, SHKD = _c('#d4ced0'), _c('#a09898')
def _shark(view):
    if view == 'front':
        return [M([(-6, 60), (-10, 44, 1), (8, 28), (30, 12), (50, 8), (70, 12), (92, 28), (110, 44, 1), (106, 60), (84, 50), (70, 62, 1), (60, 48), (50, 56), (40, 48),
                   (30, 62, 1), (16, 50)], SHK, 'f'),
                M([(44, 12), (56, -12), (78, -30, 1), (66, -6), (58, 12)], SHK, 'f')]
    if view == 'side':
        return [M([(96, 56), (90, 32), (70, 12), (40, 6), (14, 18), (2, 44), (6, 80), (30, 84), (50, 60), (70, 56)], SHK, 'f'),
                M([(40, 10), (30, -14), (6, -30, 1), (18, -6), (24, 12)], SHK, 'f')]
    return [M([(-6, 60), (-10, 44, 1), (8, 28), (30, 12), (50, 8), (70, 12), (92, 28), (110, 44, 1), (106, 60), (90, 84), (50, 90), (10, 84)], SHK, 'f'),
            M([(44, 12), (56, -12), (78, -30, 1), (66, -6), (58, 12)], SHK, 'f'), M([(50, 10), (88, 30), (100, 56), (88, 82), (70, 50)], SHKD, 'f', False)]
C('giv-r-trupal', 'normal', P('#d4ced0', '#fdf2d8', iris='#c02a1a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=False, ears=False),
  _shark('front') + [L(ell(36, 77, 2, 2), _c('#f0c030'), 'f', False), L(ell(64, 77, 2, 2), _c('#f0c030'), 'f', False)],
  _shark('side'), _shark('back'))

# Goldus Janque (portero): máscara de luchador amarilla con aberturas y franjas naranjas que acaban en tiras colgando, y una
# melena castaña que sale por detrás; ojos de enfado y una sonrisa de dientes
LUC, LUCO, LUCB = _c('#f8de38'), _c('#f08a20'), _c('#7c4412')
def _luchador(view):
    if view == 'front':
        return [M([(-14, 110), (-6, 70), (6, 50), (94, 50), (106, 70), (114, 110), (90, 100), (80, 70), (20, 70), (10, 100)], LUCB, 'b'),
                ring([(10, 90), (8, 50), (16, 22), (34, 6), (50, 2), (66, 6), (84, 22), (92, 50), (90, 90), (80, 96), (70, 88), (30, 88), (20, 96)],
                     [(26, 86), (24, 64), (34, 60), (50, 62), (66, 60), (76, 64), (74, 86), (50, 92)], LUC),
                M([(30, 4), (50, 30), (70, 4), (74, 10), (50, 40), (26, 10)], LUCO, 'f', False),
                M([(40, 44), (50, 50), (60, 44), (56, 54), (44, 54)], LUCO, 'f', False),
                M([(18, 88), (26, 92), (22, 118), (16, 116)], LUC, 'f'), M([(82, 88), (74, 92), (78, 118), (84, 116)], LUC, 'f'),
                W([(18, 100), (24, 100)], LUCO, 2.0), W([(76, 100), (82, 100)], LUCO, 2.0)]
    if view == 'side':
        return [M([(30, 60), (-6, 70), (-16, 110), (10, 100), (30, 80)], LUCB, 'b'),
                M([(64, 92), (70, 76), (92, 64), (90, 34), (74, 12), (48, 4), (20, 12), (4, 40), (6, 80), (24, 96)], LUC, 'f'),
                M([(48, 4), (72, 10), (88, 30), (84, 36), (66, 18), (44, 12)], LUCO, 'f', False)]
    return [M([(-14, 116), (-6, 70), (10, 40), (90, 40), (106, 70), (114, 116), (50, 124)], LUCB, 'f'),
            M([(10, 70), (8, 40), (20, 14), (50, 2), (80, 14), (92, 40), (90, 70), (50, 74)], LUC, 'f'),
            M([(44, 4), (56, 4), (56, 72), (44, 72)], LUCO, 'f', False)]
C('goldus-janque', 'corpulento', P('#f8de38', '#c6724e', iris='#1e1414'),
  F(eyes='sharp', brows='angry', mouth='none', hairline=False, ears=False, face_front=face(w=4, chin=104, jaw=4)),
  _luchador('front') + teeth_grin(94, 14, 7), _luchador('side'), _luchador('back'))

# Graham Awn: pelo rojo en pinchos revueltos con unas gafas blancas subidas a la frente; ojos naranjas, una marca en X en la
# mejilla y sonrisa
GOGW = _c('#f4f4f4')
C('graham-awn', 'normal', P('#a8181a', '#f6ba80', iris='#e08a20', shade='#7e1612'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=[(8, 64), (18, 52), (28, 62), (38, 50), (48, 64), (58, 50), (68, 62), (80, 52), (92, 64)]),
  dome('front', top=-4, w=48, cy=44, n=9, amp=14, seed=191, sb=72) +
  [L(blob([(18, 30), (48, 26), (50, 40), (20, 44)], 6), GOGW, 'f'), L(blob([(52, 26), (82, 30), (80, 44), (50, 40)], 6), GOGW, 'f'),
   L(blob([(24, 32), (44, 30), (44, 38), (26, 40)], 4), BLACK, 'f', False), L(blob([(56, 30), (76, 32), (74, 40), (56, 38)], 4), BLACK, 'f', False),
   W([(64, 86), (70, 92)], _c('#7a3a2a'), 1.4), W([(70, 86), (64, 92)], _c('#7a3a2a'), 1.4)],
  dome('side', top=-4, w=48, cy=44, n=9, amp=14, seed=191, nape=88, fr=50) + [L(blob([(64, 28), (88, 28), (88, 40), (66, 42)], 6), GOGW, 'f')],
  dome('back', top=-4, w=48, cy=44, n=9, amp=14, seed=191, nape=88) + [band('back', GOGW, 34, 5)])

# Grub Munsch (portero): gordo, de piel morena y pelo rizado verde negruzco con unas cuentas verdes; ojos redondos, nariz
# ancha y boca abierta sonriente
BEADG = _c('#3aa04a')
C('grub-munsch', 'corpulento', P('#262e2e', '#cc9668', iris='#1e1414', shade='#181e1e'),
  F(eyes='round', brows='angry', mouth='grin', mouth_y=94, face_front=face(w=9, chin=106, jaw=7, top=28), face_side=face_side(chin=6, jaw=7),
    hairline=[(6, 58), (18, 46), (32, 40), (50, 38), (68, 40), (82, 46), (94, 58)], nose=(50, 85, 4)),
  dome('front', top=0, w=48, cy=40, n=12, amp=7, soft=True, seed=201, sb=58) + [L(ell(22, 10, 3, 3), BEADG, 'f', False, True), L(ell(80, 8, 3, 3), BEADG, 'f', False, True)],
  dome('side', top=0, w=48, cy=40, n=12, amp=7, soft=True, seed=201, nape=78, fr=42),
  dome('back', top=0, w=48, cy=40, n=12, amp=7, soft=True, seed=201, nape=78) + [L(ell(22, 10, 3, 3), BEADG, 'f', False, True)])

# Hachinoshin Nitta: melena blanca enorme y desgreñada como la de un león, con una cinta verde azulado con un emblema en
# la frente; ojos redondos, nariz grande y boca seria
TEAL = _c('#3a9aa8')
C('hachinoshin-nitta', 'corpulento', P('#f4f2ee', '#fcd0a0', iris='#1e1414', shade='#c8c4bc'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=96, face_front=face(w=5, chin=104, jaw=4), hairline=False, nose=(50, 86, 5)),
  dome('front', top=-10, w=58, cy=50, n=12, amp=14, seed=211, long=108, flare=18) +
  [band('front', TEAL, 50, 10, w=46), L(blob([(42, 50), (58, 50), (58, 58), (42, 58)], 3), _c('#4a5a60'), 'f', False)],
  dome('side', top=-10, w=58, cy=50, n=12, amp=14, seed=211, long=108, flare=18, fr=52) + [band('side', TEAL, 48, 10)],
  dome('back', top=-10, w=58, cy=50, n=12, amp=14, seed=211, long=108, flare=18, ends=5) + [band('back', TEAL, 50, 10, w=46)])

# Hakki Kyo: pelo verde oscuro en mechones de punta a los lados y una cresta crema altísima en medio; piel pálida, ojos
# verdes, un punto amarillo en la frente, orejas de punta y boca seria
CREST = _c('#ece09a')
C('hakki-kyo', 'normal', P('#28443a', '#fcecb8', iris='#3a8a6a', shade='#1a3028'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=92, ears=False, hairline=[(10, 64), (18, 48), (32, 54), (40, 44), (50, 56), (60, 44), (68, 54), (82, 48), (90, 64)]),
  ears_pointy('front', h=8) +
  [M([(12, 72), (4, 46), (-6, 28, 1), (12, 30), (8, 6, 1), (26, 18), (40, 20), (60, 20), (74, 18), (92, 6, 1), (88, 30), (106, 28, 1), (96, 46), (88, 72), (78, 50), (22, 50)]),
   M([(40, 30), (36, 4), (44, -24), (50, -44, 1), (58, -20), (62, 4), (58, 30)], CREST, 'f'),
   L(ell(50, 60, 2.4, 2.4), _c('#f0c030'), 'f', False, True), W([(22, 84), (28, 88)], OUTC, 1.2), W([(78, 84), (72, 88)], OUTC, 1.2)],
  ears_pointy('side', h=8) +
  [M([(56, 70), (62, 50), (84, 46), (90, 24), (72, 14), (40, 14), (16, 20), (-6, 30, 1), (6, 46), (4, 70), (22, 82), (42, 76)]),
   M([(50, 20), (52, -6), (48, -30), (52, -44, 1), (62, -20), (66, 4), (64, 24)], CREST, 'f')],
  ears_pointy('back', h=8) +
  [M([(12, 84), (4, 46), (-6, 28, 1), (12, 30), (8, 6, 1), (26, 18), (74, 18), (92, 6, 1), (88, 30), (106, 28, 1), (96, 46), (88, 84), (50, 90)]),
   M([(40, 30), (36, 4), (44, -24), (50, -44, 1), (58, -20), (62, 4), (58, 30)], CREST, 'f')])

# Haname Sasakure (portera): gorro rosa abombado con un gran lazo verde agua y amarillo, y media melena roja por debajo;
# ojos grises y sonrisa
HAT, BOW, BOWY = _c('#f4c4cc'), _c('#8ab8a8'), _c('#f2d04a')
def _turban(view):
    if view == 'front':
        return [L(blob([(4, 54), (6, 26), (24, 8), (50, 2), (76, 8), (96, 26), (98, 54), (50, 48)], 8), HAT, 'f'),
                W(quad((12, 44), (50, 30), (90, 40)), _c('#d8a0aa'), 1.4),
                M([(60, 16), (78, 2), (96, 10), (92, 30), (78, 26), (66, 28)], BOW, 'f'), M([(64, 22), (80, 14), (84, 22), (70, 32)], BOWY, 'f')]
    if view == 'side':
        return [L(blob([(2, 54), (6, 24), (30, 4), (60, 2), (90, 18), (96, 46), (60, 50)], 8), HAT, 'f'), M([(20, 10), (38, -4), (52, 6), (44, 20), (28, 22)], BOW, 'f')]
    return [L(blob([(4, 60), (6, 26), (24, 8), (50, 2), (76, 8), (96, 26), (98, 60), (50, 56)], 8), HAT, 'f'), M([(36, 14), (50, 2), (66, 12), (60, 28), (40, 28)], BOW, 'f')]
C('haname-sasakure', 'chica', P('#a8494c', '#fce6d8', iris='#7a7a80', shade='#843436'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(8, 62), (18, 54), (32, 60), (40, 52), (52, 60), (62, 52), (74, 58), (84, 54), (92, 62)]),
  dome('front', top=6, w=48, cy=48, long=92, flare=8, seed=221) + _turban('front'),
  dome('side', top=6, w=48, cy=48, long=92, flare=8, fr=52, seed=221) + _turban('side'),
  dome('back', top=6, w=48, cy=48, long=92, flare=8, ends=3, seed=221) + _turban('back'))

# Herman Chauvin: melena larga gris parda y ondulada hasta los hombros, con raya al medio y la frente despejada; cara larga,
# ojos afilados y boca seria
C('herman-chauvin', 'delgado', P('#a89a88', '#fceab8', iris='#3a5a6a', shade='#82725e'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=96, face_front=face(chin=106, top=20), face_side=face_side(chin=5),
    hairline=[(12, 70), (16, 48), (26, 34), (44, 30), (50, 36), (56, 30), (74, 34), (84, 48), (88, 70)]),
  dome('front', top=0, w=48, cy=44, n=5, amp=6, soft=True, long=108, flare=12, seed=231),
  dome('side', top=0, w=48, cy=44, n=5, amp=6, soft=True, long=108, flare=12, fr=36, seed=231),
  dome('back', top=0, w=48, cy=44, n=5, amp=6, soft=True, long=108, flare=12, ends=4, seed=231))

# Hiro Hughes (modelo 3D): pelo azul marino oscuro con un mechón rizado arriba y mechones largos que le enmarcan la cara;
# ojos castaños grandes y sonrisa
C('hiro-hughes', 'normal', P('#343650', '#fbf0d8', iris='#7a4a2a', shade='#24243a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(8, 64), (18, 50), (28, 60), (36, 48), (48, 60), (56, 46), (68, 58), (80, 48), (92, 64)]),
  dome('front', top=2, w=48, cy=46, n=6, amp=12, sweep=0.3, seed=241, sb=88) +
  [W(quad((50, 4), (38, -20), (58, -18)), 'mid', 3.0, 'b'), M([(10, 60), (16, 100), (10, 110, 1), (6, 80)]), M([(90, 60), (84, 100), (90, 110, 1), (94, 80)])],
  dome('side', top=2, w=48, cy=46, n=6, amp=12, sweep=0.3, seed=241, nape=94, fr=52) + [W(quad((46, 2), (36, -20), (54, -18)), 'mid', 3.0, 'b')],
  dome('back', top=2, w=48, cy=46, n=6, amp=12, sweep=0.3, seed=241, nape=96) + [W(quad((50, 4), (38, -20), (58, -18)), 'mid', 3.0, 'b')])

# Hugo Sauvage: pelo rosa peinado hacia atrás en la parte de arriba y los lados rapados; un tatuaje rojo en un lado de la
# cara, ojos cerrados, pendiente rojo y un pañuelo rosa enroscado al cuello
TAT, SCF = _c('#a82a2a'), _c('#e09090')
C('hugo-sauvage', 'normal', P('#e89494', '#cc966a', iris='#1e1414', shade='#c07070'),
  F(eyes='closed', brows='angry', mouth='frown', mouth_y=94, hairline=False),
  [L(blob([(16, 56), (16, 34), (28, 14), (50, 6), (72, 14), (84, 34), (84, 56)], 8), 'skin_d'),
   M([(30, 50), (28, 16), (40, 2), (62, 2), (72, 16), (70, 50), (60, 40), (40, 40)]),
   W([(64, 66), (78, 64), (76, 78), (66, 80), (74, 90)], TAT, 2.6), L(ell(84, 82, 1.8, 2.6), RED, 'f', False, True),
   L(blob([(44, 100), (56, 100), (50, 106)], 2), 'shade', 'f', False)] + scarf('front', SCF, y=102, h=12) +
  [M([(70, 104), (96, 112), (90, 124), (70, 118)], SCF, 'f')],
  [L(blob([(10, 60), (8, 34), (24, 12), (50, 4), (76, 10), (86, 30), (60, 34), (40, 46), (30, 64)], 8), 'skin_d'),
   M([(20, 40), (20, 14), (44, 0), (70, 4), (86, 20), (80, 30), (50, 26), (30, 36)])] + scarf('side', SCF, y=102, h=12),
  [L(blob([(14, 78), (12, 34), (28, 14), (50, 6), (72, 14), (88, 34), (86, 78), (50, 84)], 8), 'skin_d'),
   M([(32, 50), (30, 16), (42, 2), (60, 2), (70, 16), (68, 50), (50, 56)])] + scarf('back', SCF, y=102, h=12))

# Isami Kondo (modelo 3D): pelo negro en pinchos cortos peinado hacia atrás con un mechón por la frente y una coleta corta
# detrás; piel tostada, cara ancha, ojos afilados, ceño fruncido y barbilla con sombra de barba
C('isami-kondo', 'normal', P('#343434', '#eca662', iris='#1e1414', shade='#222222'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, face_front=face(w=4, chin=104, jaw=5), face_side=face_side(chin=4, jaw=5),
    hairline=[(8, 62), (16, 48), (30, 42), (44, 46), (50, 40), (60, 50), (72, 42), (86, 48), (92, 62)]),
  dome('front', top=-2, w=48, cy=44, n=8, amp=10, seed=251, sb=64) + [M([(46, 40), (58, 42), (54, 62, 1)], 'mid', 'f'),
                                                                      L(blob([(44, 102), (56, 102), (50, 108)], 2), _c('#a07040'), 'f', False)],
  dome('side', top=-2, w=48, cy=44, n=8, amp=10, seed=251, nape=82, fr=44) +
  [M([(14, 40), (-8, 30), (-30, 44, 1), (-12, 50), (-26, 62, 1), (-4, 58), (14, 56)]), L(ell(14, 46, 4, 5), 'deep', 'b')],
  dome('back', top=-2, w=48, cy=44, n=8, amp=10, seed=251, nape=82) + [M([(42, 50), (40, 70), (50, 80, 1), (60, 70), (58, 50)], 'shade', 'f')])

# Jeku Hydia: pelo azul marino oscuro recogido en dos grandes moños trenzados a los lados de la cabeza y una trenza larga
# que le cae por un lado; piel morena, una marca roja en la frente, ojos afilados con raya roja y ceño fruncido
def _braid(x, y0, n=4, r=5):
    return [L(ell(x, y0 + i * r * 1.8, r, r * 1.1), 'mid', 'f') for i in range(n)]
C('jeku-hydia', 'chica', P('#123c60', '#cc986a', iris='#1e1414', shade='#0c2840'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=[(8, 62), (16, 50), (30, 44), (50, 40), (70, 44), (84, 50), (92, 62)]),
  [L(ell(10, 18, 16, 16)), L(ell(90, 18, 16, 16)), strand([(2, 12), (16, 26)], 'shade', 'b', 1.2), strand([(98, 12), (84, 26)], 'shade', 'b', 1.2)] +
  dome('front', top=4, w=46, cy=46, sb=70, seed=261) + _braid(82, 96, 4) +
  [M([(48, 58), (52, 58), (50, 66, 1)], _c('#d02a2a'), 'f'), W([(24, 74), (30, 78)], _c('#d02a2a'), 1.6), W([(76, 74), (70, 78)], _c('#d02a2a'), 1.6),
   strand([(40, 10), (36, 40)], 'shade', 'b', 1.0), strand([(60, 10), (64, 40)], 'shade', 'b', 1.0)],
  [L(ell(46, 14, 16, 16))] + dome('side', top=4, w=46, cy=46, nape=88, fr=44, seed=261) + _braid(40, 96, 4),
  [L(ell(10, 18, 16, 16)), L(ell(90, 18, 16, 16))] + dome('back', top=4, w=46, cy=46, nape=88, seed=261) + _braid(70, 92, 5))
