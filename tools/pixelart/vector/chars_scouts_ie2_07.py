"""Ojeadores de IE2 (scouts-ie2), tanda 07: dibujados a partir de su retrato de Victory Road; claves 'scouts-ie2:<id>'.

Casi ninguno tiene modelo 3D: el frente sale del retrato y el perfil y la espalda se deducen de cómo cae ese peinado.
Se reutilizan las ayudas de los ojeadores de IE1 (dome/hl/face de la tanda 09, bowl/skull de la 03 y la 10, crop/brows de
Nikogawa) y aquí hay unas pocas más (máscaras, gafas de bucear, cascos)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars_scouts_ie1_03 import bowl, round_specs, thick_brows, side_brow  # noqa: F401
from chars_scouts_ie1_09 import dome, face, face_side, hl  # noqa: F401
from chars_scouts_ie1_10 import nose_tri, skull, squint  # noqa: F401
from chars import longhair  # noqa: F401
from chars_bigwaves import rect_glasses, white_eyes, side_eye  # noqa: F401
from chars_vr_nikogawa import blush, brows, brow_side, crop, ring_glasses  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401

K = 'scouts-ie2:'
WHITE = (248, 248, 248, 255)
BLACK = (28, 24, 28, 255)
MOUTH = (130, 70, 50, 255)


def _c(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5)) + (255,)


def C(pid, body, palette, f, front, side, back):
    """Guarda el ojeador; el nacimiento del pelo (lista) baja por el borde de la cara para que su raya no cruce los lados."""
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2 and f.get('hl_down', True):
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


def fr(pts, c='mid', z='f'):
    """Mechón por delante de la cara."""
    return L(outline(pts), c, z)


def mir(pts):
    return [(100 - p[0], p[1]) + tuple(p[2:]) for p in pts]


def dot(x, y, r, c, z='f'):
    return L(ell(x, y, r, r), c, z, False)


def line(pts, c=OUTC, w=1.6, z='f'):
    return L(pts, c, z, False, False, w)


# ------------------------------------------------------------------------------------------------------------ 1-8

# Skip Docker (portero): la cabeza envuelta en una venda crema hasta las cejas; melena castaño rojiza lisa que cae por
# los lados hasta la barbilla, con un mechón por la frente; ojos grandes morados
BAND = _c('#dcc49e')
BAND_D = _c('#b89e78')
def _bandage(view):
    if view == 'front':
        return [L(outline([(8, 66), (5, 40), (16, 14), (50, 2), (84, 14), (95, 40), (92, 66), (70, 60), (50, 62), (30, 60)]), BAND, 'f'),
                line(quad((10, 44), (50, 30), (92, 50)), BAND_D, 1.4), line(quad((8, 56), (40, 44), (90, 34)), BAND_D, 1.4),
                line(quad((30, 14), (60, 22), (88, 26)), BAND_D, 1.2)]
    if view == 'side':
        return [L(outline([(8, 70), (2, 42), (16, 10), (48, 0), (78, 8), (93, 30), (94, 60), (72, 58), (48, 58), (28, 64)]), BAND, 'f'),
                line(quad((4, 44), (46, 34), (92, 46)), BAND_D, 1.4), line(quad((10, 62), (44, 48), (90, 30)), BAND_D, 1.4)]
    return [L(outline([(8, 68), (5, 40), (16, 14), (50, 2), (84, 14), (95, 40), (92, 68), (70, 62), (50, 64), (30, 62)]), BAND, 'f'),
            line(quad((8, 46), (50, 34), (94, 50)), BAND_D, 1.4), line(quad((8, 58), (50, 46), (92, 36)), BAND_D, 1.4)]
C('skip-docker', 'normal', P('#7a3a1e', '#d6a160', iris='#8a64b0', shade='#5a2a16'),
  F(eyes='big', brows=False, mouth='line', mouth_y=93, hairline=False),
  [L(outline([(12, 56), (5, 80), (4, 104), (10, 114, 1), (20, 100), (26, 110, 1), (28, 86), (72, 86), (74, 110, 1), (80, 100), (90, 114, 1), (96, 104),
              (95, 80), (88, 56)])),
   fr([(12, 58), (22, 62), (26, 84), (22, 104, 1), (16, 88)]), fr([(88, 58), (78, 62), (74, 84), (78, 104, 1), (84, 88)]),
   fr([(40, 60), (50, 62), (46, 76), (40, 94, 1), (38, 74)])] + _bandage('front'),
  [L(outline([(42, 56), (20, 58), (4, 72), (0, 100), (8, 112, 1), (20, 104), (30, 114, 1), (40, 100), (52, 94), (56, 70)])),
   fr([(70, 58), (78, 60), (76, 80), (72, 96, 1), (68, 78)])] + _bandage('side'),
  [L(outline([(8, 58), (4, 90), (6, 114, 1), (20, 104), (30, 116, 1), (40, 104), (50, 118, 1), (60, 104), (70, 116, 1), (80, 104), (94, 114, 1),
              (96, 90), (92, 58)]))] + _bandage('back'))

# Skip Vinall (portero): pelo negro grisáceo en pinchos de punta con un mechón granate en medio de la coronilla; piel morena
RED = _c('#a82a48')
_sv = dict(top=-8, w=46, cy=44, n=11, amp=12, seed=21)
C('skip-vinall', 'normal', P('#3e363d', '#c8946a', iris='#201818'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=94, hairline=hl(6, 64, 50, 58, jit=2, seed=5)),
  dome('front', sb=66, **_sv) + [L(outline([(42, 34), (40, 8), (44, -16, 1), (50, 2), (56, -14, 1), (58, 10), (58, 34)]), RED)],
  dome('side', nape=86, fr=48, **_sv) + [L(outline([(46, 30), (46, 4), (52, -16, 1), (58, 2), (66, -10, 1), (66, 14), (62, 30)]), RED)],
  dome('back', nape=86, **_sv) + [L(outline([(44, 30), (42, 6), (48, -14, 1), (54, 4), (58, 30)]), RED)])

# Sofia Brashier: chica; pelo morado oscuro con flequillo recto hasta las cejas y dos moños altos tapados con fundas
# amarillas y rojas; mechones lisos delante de las orejas hasta la barbilla; coloretes rojos
YEL, RD2 = _c('#f2c632'), _c('#e0482a')
def _buns(xs, y=10):
    out = []
    for x in xs:
        out += [L(ell(x, y, 13, 12), YEL), L(outline([(x - 2, y - 12), (x + 12, y - 6), (x + 10, y + 4), (x, y)]), RD2, 'b', False)]
    return out
C('sofia-brashier', 'chica', P('#563c5a', '#f4be94', iris='#201820'),
  F(eyes='normal', brows='angry', mouth='frown', mouth_y=94, hairline=[(14, 70), (18, 64), (82, 64), (86, 70)]),
  _buns((12, 88)) + bowl('front', top=4, side=62) + [fr([(14, 60), (22, 62), (22, 98), (17, 102, 1), (13, 80)]),
                                                     fr([(86, 60), (78, 62), (78, 98), (83, 102, 1), (87, 80)])] + blush(86, (230, 70, 60, 255), 21, 4.4),
  _buns((50,), 2) + bowl('side', top=4, nape=88) + [fr([(66, 56), (74, 58), (74, 94), (70, 98, 1), (66, 80)])],
  _buns((12, 88)) + bowl('back', top=4, nape=88))

# Sonny Cinders: una mata enorme de pelo morado esponjoso, ancha como un corazón por arriba y que baja por los lados hasta
# acabar en rizos junto a las mejillas; ceño fruncido, ojos afilados
C('sonny-cinders', 'normal', P('#6d4d78', '#f2cb9e', iris='#3a2a18'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=[(10, 62), (18, 56), (34, 52), (50, 56), (66, 52), (82, 56), (90, 62)]),
  [L(outline([(14, 94, 1), (9, 80), (16, 70), (6, 56), (-6, 40), (-8, 14), (6, -2), (26, -8), (44, -4), (50, 6, 1), (56, -4), (74, -8), (94, -2), (108, 14),
              (106, 40), (94, 56), (84, 70), (91, 80), (86, 94, 1), (80, 80), (80, 56), (20, 56), (20, 80)])),
   L(outline([(60, 0), (90, -2), (104, 16), (102, 38), (88, 50), (76, 30)]), 'shade', 'b', False)],
  [L(outline([(70, 52), (80, 46), (94, 38), (100, 18), (88, 0), (60, -10), (30, -8), (4, 6), (-8, 30), (-4, 52), (10, 64), (24, 68), (30, 86), (36, 96, 1),
              (44, 78), (46, 60), (56, 56)])),
   L(outline([(-6, 36), (20, 44), (40, 58), (34, 80), (24, 66), (8, 62)]), 'shade', 'b', False)],
  [L(outline([(14, 94, 1), (9, 78), (2, 60), (-8, 40), (-8, 14), (6, -2), (26, -8), (44, -4), (50, 4, 1), (56, -4), (74, -8), (94, -2), (108, 14), (108, 40),
              (98, 60), (91, 78), (86, 94, 1), (70, 86), (50, 88), (30, 86)])),
   L(outline([(58, 0), (92, -2), (106, 18), (104, 44), (92, 70), (64, 80)]), 'shade', 'b', False)])

# Stan "Blue" Treece: máscara blanca que le tapa la cara salvo la boca, con dos franjas azules y amarillas en uve; melena
# rubio pálido ondulada alrededor; sonrisa de dientes
MASK, BLU, YL2 = _c('#f4f4f2'), _c('#4aa8dc'), _c('#f2d44a')
C('stan-blue-s-treece', 'normal', P('#f4eca4', '#c8a68a', shade='#d8c880'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=100, hairline=False),
  dome('front', top=0, w=50, cy=46, n=10, amp=7, soft=True, sb=88, seed=31) +
  [L(outline([(20, 50), (26, 32), (50, 26), (74, 32), (80, 50), (78, 76), (64, 90), (50, 94), (36, 90), (22, 76)]), MASK, 'f'),
   L(outline([(28, 38), (36, 36), (46, 70), (48, 88), (42, 86)]), BLU, 'f', False), L(outline([(72, 38), (64, 36), (54, 70), (52, 88), (58, 86)]), BLU, 'f', False),
   L(outline([(36, 36), (42, 36), (48, 64), (48, 80)]), YL2, 'f', False), L(outline([(64, 36), (58, 36), (52, 64), (52, 80)]), YL2, 'f', False)],
  dome('side', top=0, w=50, cy=46, n=10, amp=7, soft=True, nape=94, fr=50, seed=31) +
  [L(outline([(62, 36), (84, 40), (90, 60), (86, 82), (74, 92), (64, 90), (60, 60)]), MASK, 'f'),
   L(outline([(70, 40), (76, 40), (82, 70), (80, 86), (76, 84)]), BLU, 'f', False)],
  dome('back', top=0, w=50, cy=46, n=10, amp=7, soft=True, nape=94, seed=31) +
  [line([(10, 62), (90, 62)], MASK, 2.6)])

# Steve Sancey: pelo amarillo peinado hacia atrás con dos mechones como cuernos que se curvan hacia arriba a los lados y
# un piquito en medio de la frente; ojos ámbar afilados, ceño fruncido y dientes
YH = _c('#f0e03e')
C('steve-sancey', 'normal', P('#f0e03e', '#fcc270', iris='#b07a1a', shade='#c8b42a'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=95, hairline=[(12, 62), (20, 48), (36, 44), (47, 50), (51, 58), (55, 48), (66, 44), (80, 48), (88, 62)]),
  crop('front', top=0, side=64, w=2) + [L(outline([(22, 26), (12, 14), (8, -10, 1), (17, 4), (27, 18)])), L(outline(mir([(22, 26), (12, 14), (8, -10, 1), (17, 4), (27, 18)])))],
  crop('side', top=0, w=2) + [L(outline([(38, 10), (33, -4), (30, -20, 1), (40, -4), (45, 6)]))],
  crop('back', top=0, w=2) + [L(outline([(22, 26), (12, 14), (8, -10, 1), (17, 4), (27, 18)])), L(outline(mir([(22, 26), (12, 14), (8, -10, 1), (17, 4), (27, 18)])))])

# Steve Squander: hombretón con cara de oso: hocico claro con la nariz marrón, parche negro en un ojo, y el pelo gris
# oscuro plano encima con dos bultos como orejas a los lados
MUZ, NOSE = _c('#ecc48e'), _c('#6a3a22')
BEARF = blob([(10, 50), (50, 36), (90, 50), (96, 78), (90, 102), (70, 114), (50, 116), (30, 114), (10, 102), (4, 78)])
C('steve-squander', 'corpulento', P('#3a3e48', '#d8a058', iris='#201818'),
  F(eyes='none', brows=False, mouth='none', hairline=(46, 40), face_front=BEARF),
  [L(outline([(14, 48), (2, 44), (-4, 26), (6, 14), (20, 18), (30, 6), (50, 2), (70, 6), (80, 18), (94, 14), (104, 26), (98, 44), (86, 48), (70, 42), (30, 42)])),
   L(ell(50, 92, 17, 12), MUZ, 'f', False), L(ell(50, 85, 7, 4.6), NOSE, 'f', False), line(quad((36, 101), (50, 104), (64, 101)), OUTC, 1.6),
   dot(35, 75, 7.5, BLACK), line([(14, 62), (30, 70)], BLACK, 1.4), line([(40, 70), (84, 60)], BLACK, 1.4),
   line([(56, 75), (70, 74)], OUTC, 2.4), dot(64, 76.5, 2.4, OUTC), line([(56, 68), (72, 66)], OUTC, 2.6)],
  [L(outline([(82, 42), (86, 24), (72, 6), (48, 0), (26, 4), (16, 0), (6, 8), (6, 22), (2, 34), (10, 46), (30, 42), (56, 40)])),
   L(blob([(78, 82), (96, 82), (100, 94), (88, 102), (76, 98)], 6), MUZ, 'f'), L(ell(97, 85, 4, 3.4), NOSE, 'f', False),
   line([(72, 74), (84, 73)], OUTC, 2.4), line([(70, 67), (86, 65)], OUTC, 2.6), line([(84, 100), (92, 99)], OUTC, 1.4)],
  [L(outline([(12, 50), (2, 26), (16, 12), (30, 4), (50, 0), (70, 4), (84, 12), (98, 26), (88, 50), (50, 46)])),
   line([(10, 62), (90, 60)], BLACK, 1.4)])

# Stewart Vanguard (tiene modelo 3D): adulto delgado de piel morena con el pelo azul marino peinado a un lado: un mechón
# largo que le cruza la frente hacia la derecha y acaba en punta junto a la oreja, y la melena por detrás hasta la nuca
C('stewart-vanguard', 'delgado', P('#413a5e', '#c48b46', iris='#1a1418', shade='#302a48'),
  F(eyes='normal', brows='angry', mouth='smile', mouth_y=94, hairline=[(14, 68), (16, 56), (24, 48), (30, 54), (40, 42), (60, 46), (76, 56), (88, 66)],
    face_front=face(chin=104)),
  [L(outline([(16, 70), (12, 40), (20, 14), (46, 2), (72, 8), (88, 26), (92, 44), (104, 56, 1), (86, 58), (82, 50), (40, 48), (24, 50), (18, 60)])),
   L(outline([(52, 6), (78, 14), (90, 36), (104, 56), (84, 52)]), 'shade', 'b', False),
   L(outline([(14, 74), (10, 96), (6, 108, 1), (18, 96), (22, 76)]))],
  [L(outline([(80, 40), (88, 26), (82, 8), (60, -2), (32, 0), (12, 14), (4, 40), (2, 70), (-6, 100, 1), (8, 90), (14, 104, 1), (22, 86), (34, 74), (40, 60),
              (54, 54), (68, 50)])),
   L(outline([(4, 44), (30, 48), (38, 62), (20, 86), (8, 90)]), 'shade', 'b', False)],
  [L(outline([(10, 72), (8, 40), (18, 14), (50, 2), (82, 14), (92, 40), (90, 72), (80, 90), (86, 106, 1), (66, 94), (50, 98), (34, 94), (14, 106, 1), (20, 88)])),
   L(outline([(-10, 60, 1), (10, 52), (12, 64)])),
   L(outline([(56, 6), (82, 18), (92, 44), (86, 84), (66, 92)]), 'shade', 'b', False)])


# ------------------------------------------------------------------------------------------------------------ 9-16

# Stu Boilin: pelo gris verdoso peinado hacia atrás con las puntas que se curvan hacia fuera a la altura de la mandíbula y
# una cinta dorada fina en la frente; ojos afilados y media sonrisa
GOLD = _c('#c8a226')
C('stu-boilin', 'normal', P('#56706e', '#eab27a', iris='#201818'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=95, hairline=[(14, 64), (18, 54), (30, 50), (50, 48), (70, 50), (82, 54), (86, 64)]),
  [L(outline([(16, 66), (10, 40), (20, 14), (50, 2), (80, 14), (90, 40), (84, 66), (82, 52), (18, 52)])),
   L(outline([(14, 64), (6, 82), (4, 96, 1), (14, 92), (22, 76)])), L(outline(mir([(14, 64), (6, 82), (4, 96, 1), (14, 92), (22, 76)]))),
   L(outline([(60, 6), (82, 18), (90, 40), (84, 60), (76, 34)]), 'shade', 'b', False),
   line(quad((16, 50), (50, 40), (84, 50)), GOLD, 2.6)],
  [L(outline([(76, 50), (86, 38), (82, 14), (60, 0), (30, 2), (10, 16), (2, 40), (4, 66), (8, 88), (2, 100, 1), (18, 92), (30, 80), (40, 64), (54, 54)])),
   L(outline([(4, 44), (30, 50), (38, 64), (24, 84), (10, 88)]), 'shade', 'b', False),
   line(quad((40, 40), (66, 44), (86, 40)), GOLD, 2.6)],
  [L(outline([(10, 70), (8, 40), (18, 14), (50, 2), (82, 14), (92, 40), (90, 70), (94, 96, 1), (80, 84), (66, 90), (50, 92), (34, 90), (20, 84), (6, 96, 1)])),
   L(outline([(56, 6), (82, 18), (92, 44), (90, 80), (66, 90)]), 'shade', 'b', False)])

# Stu Borneman: melena negro azulada lisa con raya al lado que le tapa un ojo y le cae hasta la mandíbula; mascarilla
# blanca en la boca; el ojo visible entornado y con el ceño fruncido
MASK2 = _c('#ece0c4')
C('stu-borneman', 'normal', P('#2c384e', '#f2b878', iris='#201818', shade='#202a3a'),
  F(eyes='none', brows=False, mouth='none', hairline=False),
  [L(outline([(10, 96), (6, 60), (12, 26), (32, 6), (56, 2), (80, 12), (92, 36), (94, 70), (92, 98, 1), (84, 80), (80, 58), (60, 50), (50, 56), (44, 76),
              (40, 92, 1), (30, 80), (22, 70), (18, 100, 1)])),
   L(outline([(56, 6), (80, 14), (92, 38), (92, 70), (84, 56)]), 'shade', 'b', False),
   line([(56, 76), (72, 74)], OUTC, 2.6), dot(64, 77, 2.6, OUTC), line([(56, 68), (72, 64)], OUTC, 2.8),
   L(outline([(24, 84), (50, 82), (76, 84), (74, 100), (60, 108), (40, 108), (26, 100)]), MASK2, 'f')],
  [L(outline([(78, 52), (88, 38), (84, 14), (60, 0), (30, 2), (10, 18), (2, 46), (4, 80), (10, 100, 1), (20, 86), (34, 74), (40, 60), (56, 56), (66, 60),
              (72, 72), (76, 88, 1), (80, 66)])),
   line([(76, 75), (85, 74)], OUTC, 2.4), line([(74, 67), (86, 65)], OUTC, 2.6),
   L(outline([(66, 84), (88, 84), (88, 98), (78, 106), (64, 100)]), MASK2, 'f'), line([(66, 86), (48, 74)], MASK2, 1.4)],
  [L(outline([(8, 98, 1), (6, 60), (12, 26), (32, 6), (50, 2), (68, 6), (88, 26), (94, 60), (92, 98, 1), (76, 90), (60, 94), (50, 90), (40, 94), (24, 90)])),
   L(outline([(56, 6), (82, 18), (94, 44), (92, 96), (66, 92)]), 'shade', 'b', False),
   line([(12, 84), (88, 84)], MASK2, 1.4)])

# Stu Hoofer: pelo gris revuelto con mechones por la frente y los lados largos recogidos en dos coletas bajas que
# asoman a los lados de la cara; ojos grandes gris verdoso y sonrisa de dientes
C('stu-hoofer', 'normal', P('#6c7480', '#f2c8a0', iris='#a09a78', shade='#545a66'),
  F(eyes='big', brows='angry', mouth='grin', mouth_y=95, hairline=[(14, 66), (20, 50), (32, 56), (42, 44), (52, 58), (60, 46), (72, 54), (82, 48), (86, 66)]),
  dome('front', top=0, w=46, cy=44, n=7, amp=10, sweep=-0.4, seed=41, sb=72) +
  [L(outline([(14, 82), (2, 90), (-4, 106, 1), (10, 100), (18, 92)])), L(outline(mir([(14, 82), (2, 90), (-4, 106, 1), (10, 100), (18, 92)])))],
  dome('side', top=0, w=46, cy=44, n=7, amp=10, sweep=-0.4, seed=41, nape=84, fr=50) +
  [L(outline([(36, 80), (28, 92), (24, 108, 1), (38, 98), (44, 84)]))],
  dome('back', top=0, w=46, cy=44, n=7, amp=10, sweep=-0.4, seed=41, nape=84) +
  [L(outline([(16, 80), (2, 90), (-4, 106, 1), (10, 100), (22, 88)])), L(outline(mir([(16, 80), (2, 90), (-4, 106, 1), (10, 100), (22, 88)])))])

# Stuart Leafe: pelo verde azulado muy oscuro en mechones de punta, con el flequillo picudo sobre los ojos y los lados
# hasta la mandíbula abiertos en puntas; ojos morados entornados
C('stuart-leafe', 'normal', P('#0e5a58', '#f2b878', iris='#6a3a8a', shade='#0a4442'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=95, hairline=[(14, 66), (18, 52), (28, 66), (36, 52), (46, 70), (54, 54), (62, 70), (72, 54), (80, 66), (86, 60)]),
  [L(outline([(16, 74), (4, 96, 1), (8, 70), (2, 54, 1), (10, 40), (12, 20), (30, 4), (54, 0), (78, 8), (92, 26), (104, 30, 1), (94, 42), (98, 58, 1), (90, 66),
              (98, 94, 1), (82, 78), (80, 56), (20, 56)])),
   L(outline([(58, 4), (80, 10), (92, 28), (90, 60), (80, 40)]), 'shade', 'b', False)],
  [L(outline([(78, 54), (88, 40), (90, 22), (76, 4), (50, -2), (24, 4), (8, 20), (0, 44), (-4, 60, 1), (6, 66), (2, 90, 1), (18, 82), (26, 96, 1), (36, 76), (42, 60),
              (56, 56), (70, 58), (76, 70), (84, 66)])),
   L(outline([(0, 46), (30, 50), (38, 64), (26, 88), (12, 82)]), 'shade', 'b', False)],
  [L(outline([(14, 80), (2, 96, 1), (8, 70), (0, 54, 1), (8, 40), (12, 20), (30, 4), (50, 0), (70, 4), (88, 20), (92, 40), (100, 54, 1), (92, 70), (98, 96, 1),
              (82, 84), (66, 92), (50, 88), (34, 92), (18, 84)])),
   L(outline([(56, 4), (82, 14), (94, 44), (90, 84), (66, 90)]), 'shade', 'b', False)])

# Susan Doiley: chica de pelo rosa malva con flequillo recto y dos coletas abultadas a los lados de la cabeza; sonrisa
C('susan-doiley', 'chica', P('#b088a8', '#f4c08c', iris='#201820', shade='#906c8a'),
  F(eyes='normal', brows=True, mouth='grin', mouth_y=95, hairline=[(14, 66), (18, 58), (50, 58), (82, 58), (86, 66)]),
  [L(outline([(12, 30), (-2, 40), (-6, 70), (2, 96), (14, 98, 1), (12, 76), (20, 60)])), L(outline(mir([(12, 30), (-2, 40), (-6, 70), (2, 96), (14, 98, 1), (12, 76), (20, 60)])))] +
  bowl('front', top=4, side=70),
  [L(outline([(26, 22), (12, 30), (4, 60), (10, 92), (24, 98, 1), (24, 74), (30, 48)]))] + bowl('side', top=4, nape=80),
  [L(outline([(12, 30), (-2, 40), (-6, 70), (2, 96), (14, 98, 1), (14, 76), (20, 60)])), L(outline(mir([(12, 30), (-2, 40), (-6, 70), (2, 96), (14, 98, 1), (14, 76), (20, 60)])))] +
  bowl('back', top=4, nape=80))

# Swithin Sainte: pelo castaño con un remolino grande en lo alto echado a un lado y los lados abiertos en dos alas de
# punta a la altura de las orejas; gafas rectangulares finas y ojos verdes
C('swithin-sainte', 'normal', P('#7a4a26', '#f4c08a', iris='#5a8a2a', shade='#5a361c'),
  F(eyes='normal', brows='angry', mouth='frown', mouth_y=95, hairline=[(14, 62), (18, 50), (30, 54), (40, 46), (50, 56), (60, 46), (72, 54), (82, 50), (86, 62)]),
  crop('front', top=6, side=62) + [L(outline([(40, 14), (36, -2), (24, -18, 1), (46, -8), (56, 8)])),
                                    L(outline([(14, 60), (2, 72), (-10, 78, 1), (8, 80), (18, 76)])), L(outline(mir([(14, 60), (2, 72), (-10, 78, 1), (8, 80), (18, 76)])))] +
  rect_glasses('front', 76),
  crop('side', top=6) + [L(outline([(52, 8), (50, -6), (30, -18, 1), (40, 0), (40, 10)])), L(outline([(36, 64), (24, 76), (12, 84, 1), (30, 82), (40, 74)]))] +
  rect_glasses('side', 76),
  crop('back', top=6) + [L(outline([(44, 12), (40, -2), (30, -18, 1), (52, -8), (58, 8)])),
                         L(outline([(16, 62), (2, 72), (-10, 78, 1), (8, 82), (20, 78)])), L(outline(mir([(16, 62), (2, 72), (-10, 78, 1), (8, 82), (20, 78)])))])

# Sym Copate: pelo magenta corto de pinchos con las patillas largas que bajan hasta la mandíbula y se curvan hacia fuera;
# piel morena, ojos afilados y media sonrisa
C('sym-copate', 'normal', P('#c03a7a', '#d89a5a', iris='#201818', shade='#962a5e'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=95, hairline=[(14, 64), (20, 50), (32, 56), (44, 46), (56, 54), (68, 46), (80, 52), (86, 64)]),
  dome('front', top=-6, w=44, cy=42, n=7, amp=14, seed=51, sb=62) +
  [L(outline([(14, 58), (10, 84), (2, 100, 1), (16, 94), (22, 76), (22, 60)])), L(outline(mir([(14, 58), (10, 84), (2, 100, 1), (16, 94), (22, 76), (22, 60)])))],
  dome('side', top=-6, w=44, cy=42, n=7, amp=14, seed=51, nape=82, fr=46) + [L(outline([(54, 58), (56, 84), (48, 100, 1), (62, 92), (64, 60)]))],
  dome('back', top=-6, w=44, cy=42, n=7, amp=14, seed=51, nape=82) +
  [L(outline([(14, 62), (10, 84), (2, 100, 1), (16, 94), (22, 76)])), L(outline(mir([(14, 62), (10, 84), (2, 100, 1), (16, 94), (22, 76)])))])

# Syon Blaze (tiene modelo 3D): una explosión de pinchos color crema con sombras rosadas en todas direcciones, con mechones
# picudos que le caen por la frente; ceño fruncido
C('syon-blaze', 'normal', P('#f6e0c4', '#f2b88a', iris='#201818', shade='#d6aaa0', deep='#b88a86'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=[(14, 70), (20, 56), (30, 68), (40, 54), (48, 70), (56, 56), (66, 70), (74, 56), (84, 64), (86, 70)]),
  dome('front', top=-12, w=50, cy=46, n=14, amp=18, seed=61, sb=80),
  dome('side', top=-12, w=50, cy=46, n=14, amp=18, seed=61, nape=94, fr=54),
  dome('back', top=-12, w=50, cy=46, n=14, amp=18, seed=61, nape=96))


# ------------------------------------------------------------------------------------------------------------ 17-24

# Tailor Wilden: pelo castaño claro de pinchos que se abren hacia arriba como orejas de gato, con mechas oscuras; ojos
# redondos blancos con la pupila pequeña, dos lunares marrones por cejas y rayas de bigote en las mejillas
DKB = _c('#6a4a2a')
C('tailor-wilden', 'normal', P('#aa8a5a', '#f2b07a', shade='#8a6c42'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=95, nose=(50, 85, 2.2), hairline=[(14, 62), (20, 52), (34, 56), (46, 50), (54, 50), (66, 56), (80, 52), (86, 62)]),
  [L(outline([(16, 64), (8, 40), (0, 4, 1), (20, 18), (30, 8), (50, 4), (70, 8), (80, 18), (100, 4, 1), (92, 40), (84, 64), (80, 54), (20, 54)])),
   L(outline([(16, 44), (8, 14), (28, 30)]), DKB, 'b', False), L(outline([(84, 44), (92, 14), (72, 30)]), DKB, 'b', False),
   L(outline([(34, 24), (42, 12), (40, 30)]), DKB, 'b', False), L(outline([(66, 24), (58, 12), (60, 30)]), DKB, 'b', False)] +
  white_eyes(77, 15, 6.6, 6.4, 2.4) + [dot(36, 64, 2.4, DKB), dot(64, 64, 2.4, DKB),
                                       line([(18, 86), (26, 88)], DKB, 1.0), line([(18, 91), (26, 91)], DKB, 1.0),
                                       line([(82, 86), (74, 88)], DKB, 1.0), line([(82, 91), (74, 91)], DKB, 1.0)],
  [L(outline([(76, 50), (86, 38), (86, 18), (70, 4), (54, -12, 1), (50, 4), (30, 2), (10, 16), (2, 40), (6, 64), (20, 80), (34, 76), (40, 60), (56, 54)])),
   L(outline([(56, 4), (56, -6), (64, 8)]), DKB, 'b', False)] + side_eye(77) + [dot(80, 64, 2.2, DKB), line([(80, 88), (86, 89)], DKB, 1.0)],
  [L(outline([(14, 72), (8, 40), (0, 4, 1), (20, 18), (30, 8), (50, 4), (70, 8), (80, 18), (100, 4, 1), (92, 40), (86, 72), (66, 82), (50, 84), (34, 82)])),
   L(outline([(16, 44), (8, 14), (28, 30)]), DKB, 'b', False), L(outline([(84, 44), (92, 14), (72, 30)]), DKB, 'b', False)])

# Tam Boyish: chica de melena lisa azul con flequillo recto y el pelo hasta los hombros; ojos morados caídos y un lunar
C('tam-boyish', 'chica', P('#2c58a0', '#f6dcb0', iris='#6a2a6a', shade='#1e4280'),
  F(eyes='sharp', brows=True, mouth='frown', mouth_y=95, hairline=[(14, 66), (18, 60), (50, 60), (82, 60), (86, 66)]),
  [L(outline([(12, 60), (4, 90), (2, 112, 1), (14, 104), (20, 112, 1), (24, 86), (76, 86), (80, 112, 1), (86, 104), (98, 112, 1), (96, 90), (88, 60)]))] +
  bowl('front', top=2, side=70) + [dot(36, 84, 0.9, OUTC)],
  [L(outline([(36, 56), (14, 60), (2, 80), (0, 108, 1), (14, 102), (26, 112, 1), (34, 96), (48, 88), (54, 70)]))] + bowl('side', top=2, nape=90),
  bowl('back', top=2, nape=96) + [L(outline([(8, 80), (4, 106), (8, 114, 1), (30, 106), (50, 114, 1), (70, 106), (92, 114, 1), (96, 106), (92, 80)]))])

# Tara Gaudier: chica de pelo naranja muy largo con la raya en zigzag, que le cae por delante de los hombros en dos
# mechones atados con cintas verdes y blancas y acaba en trenzas; sonrisa
GRN, CRM = _c('#3a9a4a'), _c('#f0ead0')
def _tails(xs, y0=70, y1=114):
    out = []
    for x in xs:
        out += [L(outline([(x - 5, y0), (x + 5, y0), (x + 5, y1 - 8), (x, y1, 1), (x - 5, y1 - 8)])),
                L(outline([(x - 5.5, y0 + 6), (x + 5.5, y0 + 6), (x + 5.5, y0 + 26), (x - 5.5, y0 + 26)]), GRN, 'f', False),
                line([(x - 5, y0 + 12), (x + 5, y0 + 12)], CRM, 1.6, 'f'), line([(x - 5, y0 + 20), (x + 5, y0 + 20)], CRM, 1.6, 'f')]
    return out
C('tara-gaudier', 'chica', P('#f0a030', '#f8dcb4', iris='#201818', shade='#d07e1a'),
  F(eyes='normal', brows='angry', mouth='smile', mouth_y=95, hairline=[(14, 70), (20, 52), (34, 40), (48, 30), (50, 34), (52, 30), (66, 40), (80, 52), (86, 70)]),
  [L(outline([(12, 64), (10, 36), (24, 12), (50, 2), (76, 12), (90, 36), (88, 64), (84, 76), (16, 76)]))] + _tails((14, 86)),
  [L(outline([(78, 50), (86, 34), (78, 12), (54, 0), (28, 4), (10, 18), (2, 44), (2, 80), (6, 112, 1), (18, 100), (30, 110, 1), (36, 90), (44, 66), (60, 54)]))] +
  _tails((58,), 66, 112),
  [L(outline([(10, 64), (8, 36), (22, 12), (50, 2), (78, 12), (92, 36), (90, 64), (92, 104), (80, 116, 1), (66, 104), (50, 116, 1), (34, 104), (20, 116, 1), (8, 104)]))])

# Taryn Shyder: chica de melena lisa verde menta hasta los hombros, con un mechón largo que le tapa medio ojo; ojos oliva
C('taryn-shyder', 'chica', P('#7aa898', '#f4c494', iris='#7a6a20', shade='#5a8878'),
  F(eyes='normal', brows=False, mouth='frown', mouth_y=95, hairline=[(14, 68), (18, 58), (30, 50), (44, 48), (56, 56), (68, 66), (78, 72), (86, 68)]),
  longhair('front', length=100, flare=6, top=2, ends=3) + [fr([(40, 50), (62, 54), (76, 70), (84, 84, 1), (68, 74), (54, 62)])],
  longhair('side', length=100, flare=6, top=2, ends=3),
  longhair('back', length=100, flare=6, top=2, ends=4))

# Tate Immy: la cabeza es una bola beige redonda de foca con orejitas, un hocico gris y unas gafas redondas con los ojos
# cerrados; en lo alto, una cresta negra de punta
SEAL, SN = _c('#d8c4a2'), _c('#8a8a98')
SEALF = blob([(14, 46), (50, 24), (86, 46), (94, 80), (90, 106), (70, 118), (50, 120), (30, 118), (10, 106), (6, 80)])
C('tate-immy', 'corpulento', P('#1e2a26', '#d8c4a2', skin_d='#b8a482'),
  F(eyes='none', brows=False, mouth='none', hairline=False, face_front=SEALF, ears=False,
    face_side=blob([(46, 24), (72, 28), (88, 44), (92, 70), (90, 96), (76, 112), (54, 114), (36, 104), (20, 84), (14, 58), (22, 34)])),
  [L(outline([(44, 30), (48, -12, 1), (56, 30)])), L(ell(18, 36, 6, 6), _c('#a08868')), L(ell(82, 36, 6, 6), _c('#a08868'))] +
  round_specs('front', _c('#f4f0e8'), 70, 14, 10, 9, 2.6) + squint(70, 14, 5, True) +
  [L(ell(50, 80, 7, 4.4), SN, 'f', False), line(quad((44, 86), (50, 90), (56, 86)), OUTC, 1.2)],
  [L(outline([(48, 28), (50, -12, 1), (58, 28)])), L(ell(44, 36, 6, 6), _c('#a08868'))] +
  round_specs('side', _c('#f4f0e8'), 70, rx=8, ry=9, w=2.6) + [L(ell(91, 80, 4, 4), SN, 'f', False)],
  [L(outline([(44, 30), (48, -12, 1), (56, 30)])), L(ell(18, 36, 6, 6), _c('#a08868')), L(ell(82, 36, 6, 6), _c('#a08868')),
   L(SEALF, 'skin')])

# Teal "Red" Redsky: casco rojo de superhéroe que le tapa la cara con los ojos en amarillo, unas alas blancas a los lados,
# pinchos castaños por encima y un pañuelo rojo anudado que vuela a un lado
RDH, WHT2, YE3 = _c('#d8202a'), _c('#eeeae2'), _c('#f2c03a')
C('teal-red-redsky', 'normal', P('#7a4a22', '#c08a58', shade='#5a3416'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, hairline=False),
  dome('front', top=-16, w=40, cy=36, n=6, amp=16, seed=71, sb=40) +
  [L(outline([(12, 56), (20, 40), (50, 34), (80, 40), (88, 56), (86, 74), (64, 88), (50, 90), (36, 88), (14, 74)]), RDH, 'f'),
   L(outline([(16, 44), (6, 20, 1), (22, 32), (50, 28), (78, 32), (94, 20, 1), (84, 44), (50, 38)]), WHT2, 'f'),
   L(outline([(26, 62), (44, 72), (40, 80), (28, 72)]), YE3, 'f', False), L(outline(mir([(26, 62), (44, 72), (40, 80), (28, 72)])), YE3, 'f', False),
   L(outline([(20, 64), (-2, 58, 1), (6, 70), (-8, 80, 1), (16, 74)]), RDH, 'f')],
  dome('side', top=-16, w=40, cy=36, n=6, amp=16, seed=71, nape=60, fr=40) +
  [L(outline([(52, 44), (80, 40), (90, 56), (88, 76), (74, 88), (60, 84), (54, 64)]), RDH, 'f'),
   L(outline([(50, 46), (34, 22, 1), (52, 34), (84, 36), (82, 44)]), WHT2, 'f'),
   L(outline([(76, 62), (88, 66), (86, 74), (78, 70)]), YE3, 'f', False),
   L(outline([(40, 66), (10, 60, 1), (18, 72), (2, 84, 1), (36, 76)]), RDH, 'f')],
  dome('back', top=-16, w=40, cy=36, n=6, amp=16, seed=71, nape=60) +
  [L(outline([(12, 58), (16, 40), (84, 40), (88, 58), (84, 84), (16, 84)]), RDH, 'f'),
   L(outline([(16, 46), (6, 20, 1), (22, 32), (50, 30), (78, 32), (94, 20, 1), (84, 46), (50, 40)]), WHT2, 'f'),
   L(outline([(50, 70), (24, 64, 1), (30, 76), (16, 88, 1), (50, 78)]), RDH, 'f')])

# Terry Dryden: pelo naranja tostado en pinchos revueltos, piel morena, cara alargada, ojos entornados y una sonrisa
# torcida
C('terry-dryden', 'normal', P('#c0702a', '#c08a5a', iris='#201818', shade='#9a561c'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=98, nose=(50, 88, 2.6), face_front=face(chin=106, jaw=2),
    hairline=[(14, 62), (20, 50), (30, 56), (40, 46), (50, 54), (60, 46), (70, 56), (80, 50), (86, 62)]),
  dome('front', top=-10, w=50, cy=44, n=12, amp=14, seed=81, sb=66),
  dome('side', top=-10, w=50, cy=44, n=12, amp=14, seed=81, nape=86, fr=48),
  dome('back', top=-10, w=50, cy=44, n=12, amp=14, seed=81, nape=86))

# Terry Namby: calvo de cabeza ancha, con unas gafas rectangulares blancas y opacas, el ceño arrugado de preocupación y
# la boca pequeña redonda
GLS = _c('#f4f2e8')
C('terry-namby', 'corpulento', P('#e8a868', '#f8c080'),
  F(eyes='none', brows=False, mouth='none', hairline=False, face_front=face(w=4, chin=106, jaw=3)),
  skull('front') + [L(outline([(20, 72), (46, 72), (46, 80), (20, 80)]), GLS, 'f', ln=True), L(outline([(54, 72), (80, 72), (80, 80), (54, 80)]), GLS, 'f', ln=True),
                    line([(46, 75), (54, 75)], OUTC, 1.4), line(quad((40, 60), (50, 54), (60, 60)), OUTC, 1.4), line(quad((44, 64), (50, 60), (56, 64)), OUTC, 1.2),
                    dot(46, 88, 0.9, OUTC), dot(54, 88, 0.9, OUTC), L(ell(50, 97, 3, 2.4), _c('#7a3a2a'), 'f', False)],
  [L(outline([(70, 72), (84, 72), (84, 80), (70, 80)]), GLS, 'f', ln=True), line([(70, 75), (48, 72)], OUTC, 1.4)],
  [])


# ------------------------------------------------------------------------------------------------------------ 25-32

# Terry Toolan: pelo negro de pinchos hacia arriba con un hachimaki retorcido azul y blanco cuyas puntas asoman por los
# lados; ojos grandes castaños, coloretes y sonrisa
HB, HW = _c('#3a6ab0'), _c('#f2eee4')
def _hachi(view):
    if view == 'front':
        return [L(outline([(10, 44), (50, 34), (90, 44), (90, 52), (50, 42), (10, 52)]), HB, 'f'),
                line(quad((14, 47), (50, 36), (86, 47)), HW, 1.8), L(outline([(10, 48), (-4, 64, 1), (6, 66), (14, 54)]), HB, 'f'),
                L(outline([(90, 48), (104, 64, 1), (94, 66), (86, 54)]), HW, 'f')]
    if view == 'side':
        return [L(outline([(2, 44), (50, 36), (90, 40), (90, 48), (50, 44), (4, 52)]), HB, 'f'), line(quad((6, 48), (50, 38), (88, 43)), HW, 1.8),
                L(outline([(6, 48), (-10, 62, 1), (0, 66), (10, 54)]), HB, 'f')]
    return [L(outline([(8, 46), (50, 38), (92, 46), (92, 54), (50, 46), (8, 54)]), HB, 'f'), line(quad((10, 50), (50, 40), (90, 50)), HW, 1.8),
            L(outline([(46, 50), (40, 70, 1), (50, 66), (60, 70, 1), (54, 50)]), HB, 'f')]
C('terry-toolan', 'normal', P('#2a2626', '#f4b878', iris='#8a4a22'),
  F(eyes='big', brows='angry', mouth='smile', mouth_y=95, hairline=[(14, 62), (22, 54), (32, 60), (40, 52), (50, 58), (60, 52), (68, 60), (78, 54), (86, 62)]),
  dome('front', top=-12, w=44, cy=42, n=7, amp=16, seed=91, sb=62) + _hachi('front') + blush(86, (240, 140, 120, 255), 24, 3.6),
  dome('side', top=-12, w=44, cy=42, n=7, amp=16, seed=91, nape=82, fr=48) + _hachi('side'),
  dome('back', top=-12, w=44, cy=42, n=7, amp=16, seed=91, nape=82) + _hachi('back'))

# Terry Tortoise Pinn (portero): cabeza de tortuga: un caparazón verde oliva en punta le cubre la coronilla, cara beige
# ancha, ojos blancos saltones con la pupila pequeña y una boca torcida con dos colmillos
SHELL = _c('#5a7040')
TURF = blob([(12, 44), (50, 30), (88, 44), (94, 76), (90, 104), (70, 118), (50, 120), (30, 118), (10, 104), (6, 76)])
C('terry-tortoise-pinn', 'corpulento', P('#5a7040', '#d8c8a6'),
  F(eyes='none', brows=False, mouth='none', hairline=False, face_front=TURF, ears=False),
  [L(outline([(18, 62), (14, 30), (34, 4), (50, -6, 1), (66, 4), (86, 30), (82, 62), (66, 52), (50, 50), (34, 52)]), SHELL, 'f'),
   L(outline([(54, -2), (68, 6), (84, 30), (80, 56), (70, 30)]), _c('#46582e'), 'f', False)] +
  [L(ell(36, 66, 7, 6.4), WHITE, 'f', ln=True), L(ell(64, 66, 7, 6.4), WHITE, 'f', ln=True), dot(37, 67, 2.2, OUTC), dot(63, 67, 2.2, OUTC),
   line(quad((34, 92), (50, 84), (66, 92)), OUTC, 1.8), L([(38, 89), (41, 95), (43, 88)], WHITE, 'f', False, True), L([(62, 89), (59, 95), (57, 88)], WHITE, 'f', False, True)],
  [L(outline([(70, 56), (84, 40), (80, 14), (54, -6, 1), (30, 0), (10, 18), (4, 44), (14, 64), (34, 60), (52, 56)]), SHELL, 'f'),
   L(ell(84, 66, 5, 6.4), WHITE, 'f', ln=True), dot(86, 67, 2, OUTC), line([(76, 92), (90, 88)], OUTC, 1.8)],
  [L(outline([(14, 70), (10, 30), (32, 4), (50, -6, 1), (68, 4), (90, 30), (86, 70), (50, 76)]), SHELL, 'f'),
   L(outline([(54, -2), (70, 6), (88, 32), (84, 66), (70, 40)]), _c('#46582e'), 'f', False)])

# Tess Masters: chica de pelo verde oliva en media melena con un flequillo largo de mechones echados a un lado y un
# mechón más largo junto a la mejilla; ojos afilados y ceño fruncido
C('tess-masters', 'chica', P('#8a8a22', '#f6c8a0', iris='#201818', shade='#6c6c18'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=[(14, 70), (18, 54), (28, 64), (36, 50), (48, 62), (56, 50), (68, 62), (78, 54), (86, 70)]),
  bowl('front', top=2, side=84) + [L(outline([(86, 70), (98, 90), (104, 96, 1), (90, 94), (82, 84)]))],
  bowl('side', top=2, nape=86) + [L(outline([(66, 60), (78, 80), (82, 92, 1), (68, 84), (62, 70)]))],
  bowl('back', top=2, nape=88))

# Thomas Worth (portero): bombín morado con la cinta crema, mechones verde pálido revueltos que le tapan un ojo y caen por
# los lados; piel morena, el ojo visible redondo y blanco, nariz redonda y sonrisa
HAT, HATB = _c('#3a2c62'), _c('#ece0c0')
def _bowler(view):
    if view == 'front':
        return [L(outline([(-6, 40), (6, 32), (94, 32), (106, 40), (94, 46), (6, 46)]), HAT, 'f'),
                L(outline([(18, 34), (20, 4), (50, -8), (80, 4), (82, 34)]), HAT, 'f'), L(outline([(18, 26), (82, 26), (82, 34), (18, 34)]), HATB, 'f', False)]
    if view == 'side':
        return [L(outline([(-8, 42), (4, 34), (94, 32), (104, 38), (92, 44), (4, 48)]), HAT, 'f'),
                L(outline([(16, 36), (18, 4), (48, -8), (78, 4), (80, 34)]), HAT, 'f'), L(outline([(16, 28), (80, 26), (80, 34), (16, 36)]), HATB, 'f', False)]
    return _bowler('front')
C('thomas-worth', 'normal', P('#c8e098', '#a87a58', iris='#201818', shade='#a0b878'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=96, nose=(50, 86, 3.4), hairline=False),
  [L(outline([(10, 42), (2, 70), (4, 92, 1), (14, 80), (20, 96, 1), (24, 70), (76, 60), (80, 96, 1), (88, 78), (98, 90, 1), (96, 62), (90, 42)])),
   fr([(14, 44), (54, 46), (52, 64), (40, 78, 1), (34, 62), (22, 72, 1), (18, 56)]),
   L(ell(65, 74, 7, 7), WHITE, 'f', ln=True), dot(66, 75, 2.6, OUTC)] + _bowler('front'),
  [L(outline([(80, 46), (60, 46), (40, 54), (28, 74), (24, 94, 1), (36, 82), (40, 100, 1), (48, 72), (62, 60), (76, 62), (82, 76, 1), (84, 56)])),
   L(ell(83, 74, 4, 6), WHITE, 'f', ln=True), dot(84.5, 75, 1.8, OUTC)] + _bowler('side'),
  [L(outline([(8, 42), (2, 70), (6, 94, 1), (20, 82), (30, 98, 1), (40, 82), (50, 98, 1), (60, 82), (70, 98, 1), (80, 82), (94, 94, 1), (98, 70), (92, 42)]))] +
  _bowler('back'))

# Tigh "Tiger" Gerwhite: melena blanca con rayas negras de tigre que cae por los lados; pintura negra de tigre en las
# mejillas, orejas grandes de punta, nariz triangular marrón, colmillos y una perilla negra en punta
STR, TN = _c('#1e1a1e'), _c('#7a4a2a')
C('tigh-tiger-gerwhite', 'normal', P('#e8eef0', '#f2c0a6', iris='#201818', shade='#c4ccd2'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=96, big_ears=3, ear_out=4, hairline=[(14, 64), (24, 52), (40, 46), (50, 50), (60, 46), (76, 52), (86, 64)]),
  [L(outline([(16, 64), (10, 36), (22, 12), (50, 2), (78, 12), (90, 36), (84, 64), (90, 96), (84, 108, 1), (80, 76), (20, 76), (16, 108, 1), (10, 96)])),
   L(outline([(30, 8), (36, 30), (40, 8)]), STR, 'b', False), L(outline([(60, 8), (64, 30), (70, 8)]), STR, 'b', False),
   L(outline([(14, 30), (26, 40), (16, 46)]), STR, 'b', False), L(outline(mir([(14, 30), (26, 40), (16, 46)])), STR, 'b', False),
   L(outline([(14, 80), (38, 82), (16, 90)]), STR, 'f', False), L(outline(mir([(14, 80), (38, 82), (16, 90)])), STR, 'f', False),
   L(outline([(16, 68), (34, 64), (20, 75)]), STR, 'f', False), L(outline(mir([(16, 68), (34, 64), (20, 75)])), STR, 'f', False),
   L([(46, 84), (54, 84), (50, 89)], TN, 'f', False, True), L(outline([(44, 100), (50, 112, 1), (56, 100)]), STR, 'f', False),
   L([(42, 94), (44, 99), (46, 94)], WHITE, 'f', False, True), L([(58, 94), (56, 99), (54, 94)], WHITE, 'f', False, True)],
  [L(outline([(78, 48), (86, 34), (80, 12), (54, 0), (28, 2), (10, 16), (2, 44), (2, 80), (6, 104, 1), (20, 86), (32, 98, 1), (38, 76), (44, 60), (60, 52)])),
   L(outline([(30, 6), (38, 28), (44, 4)]), STR, 'b', False), L(outline([(8, 30), (24, 40), (10, 46)]), STR, 'b', False),
   L(outline([(70, 84), (86, 84), (72, 88)]), STR, 'f', False), L([(88, 84), (92, 86), (88, 89)], TN, 'f', False, True)],
  [L(outline([(10, 70), (8, 36), (20, 12), (50, 2), (80, 12), (92, 36), (90, 70), (92, 100), (80, 110, 1), (66, 98), (50, 106, 1), (34, 98), (20, 110, 1), (8, 100)])),
   L(outline([(30, 8), (36, 40), (42, 8)]), STR, 'b', False), L(outline([(58, 8), (64, 40), (70, 8)]), STR, 'b', False),
   L(outline([(12, 40), (30, 56), (14, 60)]), STR, 'b', False), L(outline(mir([(12, 40), (30, 56), (14, 60)])), STR, 'b', False)])

# Tim Opener: pinchos morado oscuro muy altos hacia arriba y a los lados, con el pelo largo por detrás hasta el cuello;
# ojos rojos afilados y una sonrisa de dientes
C('tim-opener', 'normal', P('#4a3a5e', '#f2b070', iris='#a02020', shade='#382a48'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=95, hairline=[(14, 62), (20, 50), (30, 58), (40, 46), (50, 56), (60, 46), (70, 58), (80, 50), (86, 62)]),
  dome('front', top=-22, w=48, cy=42, n=11, amp=18, seed=101, sb=70) + [L(outline([(14, 66), (8, 96, 1), (20, 86), (22, 70)])), L(outline(mir([(14, 66), (8, 96, 1), (20, 86), (22, 70)])))],
  dome('side', top=-22, w=48, cy=42, n=11, amp=18, seed=101, nape=100, fr=48),
  dome('back', top=-22, w=48, cy=42, n=11, amp=18, seed=101, nape=100))

# Tim Personator: gorro verde oscuro con dos cuernos hacia los lados, gafas redondas naranjas de cristal crema, y la cara
# de mono (gris tostada arriba y clara alrededor de la boca)
CAPG, GOR, GLN, MON = _c('#1e3a30'), _c('#e0601e'), _c('#f2e6c8'), _c('#dccaa0')
C('tim-personator', 'normal', P('#1e3a30', '#b8a070'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=97, hairline=False),
  [L(outline([(12, 50), (14, 24), (-10, 6, 1), (24, 14), (50, 6), (76, 14), (110, 6, 1), (86, 24), (88, 50), (50, 44)]), CAPG, 'f'),
   L(blob([(24, 80), (50, 74), (76, 80), (80, 96), (66, 108), (50, 110), (34, 108), (20, 96)], 6), MON, 'f', False)] +
  [L(ell(36, 74, 8.6, 8), GOR, 'f', ln=True), L(ell(64, 74, 8.6, 8), GOR, 'f', ln=True), L(ell(36, 74, 5.6, 5), GLN, 'f', False), L(ell(64, 74, 5.6, 5), GLN, 'f', False),
   line([(44, 74), (56, 74)], GOR, 2.0), line([(28, 72), (14, 70)], OUTC, 1.4), line([(72, 72), (86, 70)], OUTC, 1.4)],
  [L(outline([(10, 54), (6, 24), (26, 6), (40, -10, 1), (52, 6), (80, 14), (90, 34), (90, 48), (50, 46)]), CAPG, 'f'),
   L(blob([(66, 80), (90, 80), (92, 96), (80, 106), (66, 100)], 6), MON, 'f', False),
   L(ell(82, 74, 5, 8), GOR, 'f', ln=True), L(ell(83, 74, 3, 5), GLN, 'f', False), line([(76, 72), (48, 68)], OUTC, 1.4)],
  [L(outline([(10, 56), (14, 24), (-10, 6, 1), (24, 14), (50, 6), (76, 14), (110, 6, 1), (86, 24), (90, 56), (50, 52)]), CAPG, 'f'),
   line([(10, 70), (90, 70)], OUTC, 1.4)])

# Tim "Platinum" Platton: escafandra de buzo blanca plateada que le tapa toda la cabeza, con una ventanilla redonda verde
# con remaches y un aro metálico alrededor
HEL, HELD, RIM, WIN = _c('#ece4dc'), _c('#c8bcb2'), _c('#a8c4c8'), _c('#1e9a5a')
def _diver(view):
    if view == 'front':
        out = [L(blob([(4, 62), (6, 28), (24, 4), (50, -6), (76, 4), (94, 28), (96, 62), (88, 92), (70, 104), (30, 104), (12, 92)], 8), HEL, 'f'),
               L(blob([(62, 0), (86, 18), (96, 52), (88, 88), (74, 98), (80, 50)], 6), HELD, 'f', False),
               L(outline([(-2, 56), (102, 56), (102, 66), (-2, 66)]), RIM, 'f'), L(ell(50, 62, 22, 22), RIM, 'f', ln=True), L(ell(50, 62, 16, 16), WIN, 'f', ln=True),
               L(ell(44, 56, 4, 3), _c('#7ad8a0'), 'f', False), L(outline([(26, 104), (74, 104), (78, 112), (22, 112)]), _c('#e8c8c0'), 'f')]
        for a in range(8):
            import math
            out.append(dot(50 + 19 * math.cos(a * math.pi / 4), 62 + 19 * math.sin(a * math.pi / 4), 1.4, _c('#6a8a90')))
        return out
    if view == 'side':
        return [L(blob([(2, 62), (6, 28), (24, 4), (50, -6), (76, 4), (94, 28), (98, 62), (90, 92), (70, 104), (30, 104), (10, 92)], 8), HEL, 'f'),
                L(outline([(0, 56), (100, 56), (100, 66), (0, 66)]), RIM, 'f'), L(ell(90, 62, 10, 20), RIM, 'f', ln=True), L(ell(92, 62, 6, 15), WIN, 'f', ln=True),
                L(outline([(26, 104), (74, 104), (78, 112), (22, 112)]), _c('#e8c8c0'), 'f')]
    return [L(blob([(4, 62), (6, 28), (24, 4), (50, -6), (76, 4), (94, 28), (96, 62), (88, 92), (70, 104), (30, 104), (12, 92)], 8), HEL, 'f'),
            L(outline([(-2, 56), (102, 56), (102, 66), (-2, 66)]), RIM, 'f'), L(outline([(26, 104), (74, 104), (78, 112), (22, 112)]), _c('#e8c8c0'), 'f')]
C('tim-platinum-platton', 'normal', P('#888888', '#d8a070'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _diver('front'), _diver('side'), _diver('back'))


# ------------------------------------------------------------------------------------------------------------ 33-40

# Tim Pression (portero): tupé negro altísimo y plano por arriba, cara alargada morena oscura, ojos redondos con el ceño
# fruncido y la boca torcida
C('tim-pression', 'delgado', P('#2e2834', '#9a7058', iris='#201818'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=100, face_front=face(chin=110, jaw=-1), face_side=face_side(chin=8),
    hairline=[(16, 60), (22, 46), (36, 40), (50, 42), (64, 40), (78, 46), (84, 60)]),
  [L(outline([(18, 62), (14, 30), (4, -2), (8, -18), (30, -24), (50, -20), (70, -24), (92, -18), (96, -2), (86, 30), (82, 62), (78, 48), (22, 48)])),
   L(outline([(60, -20), (90, -16), (94, 0), (84, 30), (80, 54), (74, 20)]), 'shade', 'b', False)],
  [L(outline([(78, 46), (88, 30), (96, -4), (88, -20), (60, -26), (30, -20), (10, -6), (6, 20), (4, 50), (14, 70), (32, 72), (40, 58), (58, 52)])),
   L(outline([(6, 22), (32, 30), (40, 58), (20, 68), (8, 54)]), 'shade', 'b', False)],
  [L(outline([(14, 72), (12, 30), (4, -2), (8, -18), (30, -24), (50, -20), (70, -24), (92, -18), (96, -2), (88, 30), (86, 72), (66, 80), (50, 82), (34, 80)])),
   L(outline([(58, -20), (90, -16), (96, 0), (88, 40), (84, 72), (66, 78)]), 'shade', 'b', False)])

# Tip Bolster: cabezón de cara ancha con papada y un casquete pequeño de rizos castaño anaranjados encima; ojos entornados
# y una boca grande de mal humor
TIPF = blob([(14, 40), (50, 26), (86, 40), (94, 74), (92, 102), (74, 118), (50, 122), (26, 118), (8, 102), (6, 74)])
C('tip-bolster', 'corpulento', P('#c06a2a', '#f6c090', shade='#9a521e'),
  F(eyes='none', brows=False, mouth='none', hairline=False, face_front=TIPF, ear_out=4, eye_y=70,
    face_side=blob([(46, 22), (72, 26), (88, 40), (92, 64), (92, 92), (84, 110), (66, 118), (48, 114), (34, 100), (20, 80), (14, 54), (22, 32)])),
  [L(blob([(22, 40), (20, 24), (30, 10), (50, 4), (70, 10), (80, 24), (78, 40), (50, 36)], 6))] +
  [L(outline([(26 + 8 * i, 30 - (4 if i in (2, 3) else 0)), (30 + 8 * i, 18 - (4 if i in (2, 3) else 0)), (34 + 8 * i, 30 - (4 if i in (2, 3) else 0))]), 'shade', 'b', False)
   for i in range(6)] +
  [line([(28, 68), (44, 68)], OUTC, 2.0), line([(56, 68), (72, 68)], OUTC, 2.0), L(ell(36, 70, 4, 2), WHITE, 'f', False), L(ell(64, 70, 4, 2), WHITE, 'f', False),
   dot(37, 70.5, 1.2, OUTC), dot(63, 70.5, 1.2, OUTC), dot(50, 82, 2.4, 'skin_d'), line(quad((32, 104), (50, 92), (68, 104)), OUTC, 2.0),
   line(quad((40, 114), (50, 110), (60, 114)), 'skin_d', 1.2)],
  [L(blob([(36, 36), (34, 18), (50, 6), (72, 10), (82, 24), (80, 36), (56, 34)], 6)), line([(76, 68), (88, 68)], OUTC, 2.0), dot(90, 82, 2.6, 'skin_d'),
   line(quad((78, 104), (86, 98), (92, 102)), OUTC, 1.8)],
  [L(blob([(22, 42), (20, 24), (30, 10), (50, 4), (70, 10), (80, 24), (78, 42), (50, 40)], 6))])

# Toby Cohill: pelo negro verdoso corto con un remolino en lo alto, antifaz rojo anaranjado en los ojos, ojos caídos de
# cansancio y una sonrisa tímida
ORM = _c('#e84a1e')
C('toby-cohill', 'normal', P('#2e3a2c', '#fae0b8', iris='#6a4a2a'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=96, hairline=[(14, 62), (18, 52), (34, 48), (50, 52), (66, 48), (82, 52), (86, 62)]),
  crop('front', top=4, side=62) + [L(outline([(44, 8), (40, -8, 1), (50, 2), (58, -6, 1), (58, 8)])),
                                    L(blob([(14, 70), (30, 64), (50, 68), (70, 64), (86, 70), (84, 84), (66, 86), (50, 82), (34, 86), (16, 84)], 6), ORM, 'f'),
                                    L(ell(36, 76, 4.6, 3), _c('#f4e2b0'), 'f', False), L(ell(64, 76, 4.6, 3), _c('#f4e2b0'), 'f', False),
                                    dot(36, 77, 2, _c('#6a4a2a')), dot(64, 77, 2, _c('#6a4a2a')), line([(31, 74), (41, 74)], OUTC, 1.8), line([(59, 74), (69, 74)], OUTC, 1.8),
                                    line([(28, 64), (42, 68)], OUTC, 1.6), line([(72, 64), (58, 68)], OUTC, 1.6)],
  crop('side', top=4) + [L(outline([(52, 6), (50, -10, 1), (60, 2)])),
                         L(blob([(60, 68), (88, 68), (90, 84), (70, 86), (60, 82)], 6), ORM, 'f'), L(ell(82, 76, 3, 2.6), _c('#f4e2b0'), 'f', False),
                         line([(78, 74), (86, 74)], OUTC, 1.8)],
  crop('back', top=4) + [L(outline([(44, 10), (40, -6, 1), (50, 4), (58, -6, 1), (58, 10)])), line([(10, 74), (90, 74)], ORM, 2.4)])

# Tom Skipper: sombrero de pirata marrón con el borde y la calavera dorados sobre un pañuelo rojo, melena blanca grisácea
# lisa que cae hasta los hombros, ojos verdes afilados y una sonrisa con colmillo
PH, PG, PR = _c('#6a3a22'), _c('#e8b02a'), _c('#a83030')
def _pirate(view):
    if view in ('front', 'back'):
        out = [L(outline([(10, 54), (12, 42), (50, 36), (88, 42), (90, 54), (50, 48)]), PR, 'f'),
               L(outline([(-6, 42), (8, 20), (30, 4), (50, -2), (70, 4), (92, 20), (106, 40), (94, 46), (70, 34), (50, 32), (30, 34), (6, 46)]), PH, 'f'),
               line(quad((-4, 42), (50, 18), (104, 40)), PG, 2.0)]
        if view == 'front':
            out += [L(ell(50, 18, 6, 5.4), PG, 'f', False), line([(42, 26), (58, 14)], PG, 1.6), line([(42, 14), (58, 26)], PG, 1.6)]
        return out
    return [L(outline([(6, 56), (8, 44), (50, 38), (90, 42), (90, 52), (50, 50)]), PR, 'f'),
            L(outline([(-8, 46), (4, 22), (30, 4), (54, -2), (78, 6), (96, 26), (104, 44), (90, 46), (60, 34), (30, 36), (4, 50)]), PH, 'f'),
            line(quad((-6, 46), (50, 18), (102, 42)), PG, 2.0)]
C('tom-skipper', 'normal', P('#e0d8d0', '#c8885a', iris='#4a9a5a', shade='#bab0a8'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=95, hairline=False),
  longhair('front', length=104, flare=6, top=10, ends=4, fringe=66) + _pirate('front'),
  longhair('side', length=104, flare=6, top=10, ends=3) + _pirate('side'),
  longhair('back', length=106, flare=6, top=10, ends=4) + _pirate('back'))

# Tony Frogge: cara de rana ancha y clara, con el pelo verde oscuro pegado y un rizo en la frente; ojos naranjas en
# cuencas oscuras y una sonrisa enorme de dientes de oreja a oreja
FROGF = blob([(8, 44), (50, 30), (92, 44), (98, 70), (92, 96), (72, 108), (50, 110), (28, 108), (8, 96), (2, 70)])
DSK = _c('#3a4a3a')
C('tony-frogge', 'normal', P('#2a4a3a', '#e4d0b0', iris='#e06a1e'),
  F(eyes='none', brows=False, mouth='none', hairline=[(10, 54), (18, 46), (34, 40), (50, 40), (60, 46), (66, 54), (74, 44), (86, 46), (90, 54)], face_front=FROGF, ear_out=8,
    hl_down=False),
  crop('front', top=4, side=56, w=4) +
  [L(outline([(20, 66), (40, 70), (38, 80), (22, 78)]), DSK, 'f', False), L(outline(mir([(20, 66), (40, 70), (38, 80), (22, 78)])), DSK, 'f', False),
   dot(32, 74, 2.4, _c('#e06a1e')), dot(68, 74, 2.4, _c('#e06a1e')), dot(46, 84, 1, OUTC), dot(54, 84, 1, OUTC),
   L(quad((14, 88), (50, 112), (86, 88)) + quad((86, 88), (50, 96), (14, 88))[1:], WHITE, 'f', False, True),
   line(quad((20, 92), (50, 106), (80, 92)), OUTC, 0.8)],
  crop('side', top=4, w=4) + [L(outline([(70, 68), (88, 70), (86, 80), (72, 78)]), DSK, 'f', False), dot(80, 74, 2, _c('#e06a1e')),
                              L(quad((56, 92), (80, 104), (94, 88)) + quad((94, 88), (80, 96), (56, 92))[1:], WHITE, 'f', False, True)],
  crop('back', top=4, w=4))

# Toya Boyde: chica de pelo verde azulado con un mechón enorme que le cruza la frente hacia un lado y la coleta alta que
# sube por detrás; pupilas de estrella moradas y sonrisa
C('toya-boyde', 'chica', P('#1e9aaa', '#f6c49a', iris='#8a2a9a', shade='#147a88'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=95, hairline=[(14, 62), (16, 52), (30, 48), (50, 50), (70, 56), (84, 66), (86, 66)]),
  crop('front', top=2, side=66) + [L(outline([(54, 10), (60, -14), (76, -24), (86, -8), (82, 20), (70, 30)])),
                                    fr([(70, 38), (40, 46), (10, 60), (-8, 66, 1), (14, 50), (40, 34), (66, 28)])],
  crop('side', top=2) + [L(outline([(30, 8), (26, -14), (40, -28), (54, -18), (52, 2), (44, 10)]))],
  crop('back', top=2) + [L(outline([(40, 12), (36, -12), (50, -26), (64, -12), (60, 12)])), L(outline([(16, 40), (-6, 60, 1), (16, 54)]))])

# Travis Borer: gordito de cara muy redonda con un casquete corto castaño verdoso que acaba en un rizo hacia arriba a un
# lado; gafas redondas y una sonrisa contenta
TRAVF = blob([(10, 50), (50, 40), (90, 50), (96, 76), (92, 100), (72, 114), (50, 116), (28, 114), (8, 100), (4, 76)])
C('travis-borer', 'corpulento', P('#7a6a4a', '#fac080', iris='#201818', shade='#5e5038'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=98, face_front=TRAVF, hairline=[(10, 58), (18, 50), (50, 46), (82, 50), (90, 58)]),
  crop('front', top=14, side=56, w=4) + [L(outline([(80, 30), (96, 22), (106, 8, 1), (98, 26), (86, 40)]))] + round_specs('front', _c('#c8b8a0'), 76, 14, 9, 8, 1.6) +
  [line(quad((40, 108), (50, 112), (60, 108)), 'skin_d', 1.2)],
  crop('side', top=14, w=4) + round_specs('side', _c('#c8b8a0'), 76),
  crop('back', top=14, w=4) + [L(outline([(20, 30), (4, 22), (-6, 8, 1), (2, 26), (14, 40)]))])

# Trixy Wonder: chica de pelo celeste en media melena abierta en puntas hacia fuera, con una chistera diminuta azul marino
# de cinta roja ladeada en la cabeza; ojos rojos afilados
TOP, TOPR = _c('#24306a'), _c('#c8202a')
C('trixy-wonder', 'chica', P('#80e0e0', '#f6caa0', iris='#c02020', shade='#5ec0c4'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=[(14, 66), (20, 54), (34, 64), (44, 50), (56, 60), (66, 50), (80, 58), (86, 66)]),
  [L(outline([(16, 64), (10, 36), (22, 12), (50, 2), (78, 12), (90, 36), (84, 64), (96, 86), (108, 92, 1), (86, 92), (78, 80), (22, 80), (14, 92), (-8, 92, 1),
              (4, 86)])),
   L(outline([(60, 6), (82, 18), (90, 40), (90, 70), (80, 44)]), 'shade', 'b', False),
   L(outline([(62, 10), (66, -12), (84, -16), (88, 4)]), TOP, 'f'), L(outline([(60, 10), (92, 2), (94, 8), (62, 16)]), TOP, 'f'),
   L(outline([(64, 4), (88, -2), (88, 3), (64, 9)]), TOPR, 'f', False)],
  [L(outline([(78, 50), (88, 36), (82, 12), (56, 0), (30, 4), (12, 18), (4, 46), (6, 78), (-6, 90, 1), (16, 88), (34, 84), (40, 62), (56, 56)])),
   L(outline([(44, 4), (46, -18), (64, -20), (68, 0)]), TOP, 'f'), L(outline([(38, 4), (74, 0), (74, 6), (40, 10)]), TOP, 'f')],
  [L(outline([(14, 70), (8, 36), (20, 12), (50, 2), (80, 12), (92, 36), (86, 70), (96, 88), (108, 92, 1), (80, 90), (50, 86), (20, 90), (-8, 92, 1), (4, 88)])),
   L(outline([(12, 10), (16, -12), (34, -16), (38, 4)]), TOP, 'f'), L(outline([(8, 4), (40, 0), (42, 6), (10, 10)]), TOP, 'f')])


# ------------------------------------------------------------------------------------------------------------ 41-48

def hero_mask(view, base, eye, wing=WHITE, scarf=None, hair_c=None, eye_shape=None):
    """Casco de héroe enmascarado (los de Teal y Virgil): tapa la cara hasta la boca, con alas blancas a los lados."""
    if view == 'front':
        out = [L(outline([(12, 56), (16, 34), (50, 26), (84, 34), (88, 56), (86, 76), (66, 88), (50, 90), (34, 88), (14, 76)]), base, 'f'),
               L(outline([(10, 70), (6, 34), (2, 22, 1), (14, 30), (18, 60)]), wing, 'f'), L(outline(mir([(10, 70), (6, 34), (2, 22, 1), (14, 30), (18, 60)])), wing, 'f')]
        es = eye_shape or [(24, 54), (44, 58), (44, 76), (28, 72)]
        out += [L(outline(es), eye, 'f', False), L(outline(mir(es)), eye, 'f', False)]
        if scarf:
            out += [L(outline([(20, 90), (50, 96), (80, 90), (80, 104), (50, 110), (20, 104)]), scarf, 'f'),
                    L(outline([(20, 96), (-4, 92, 1), (6, 102), (-6, 112, 1), (22, 104)]), scarf, 'f')]
        return out
    if view == 'side':
        out = [L(outline([(48, 36), (80, 36), (90, 56), (88, 76), (74, 88), (56, 84), (48, 60)]), base, 'f'),
               L(outline([(52, 70), (40, 34), (34, 20, 1), (50, 30), (60, 64)]), wing, 'f'),
               L(outline([(74, 56), (88, 60), (86, 74), (76, 70)]), eye, 'f', False)]
        if scarf:
            out += [L(outline([(40, 90), (88, 92), (88, 104), (40, 104)]), scarf, 'f'), L(outline([(42, 94), (14, 90, 1), (22, 102), (6, 114, 1), (44, 104)]), scarf, 'f')]
        return out
    out = [L(outline([(12, 58), (16, 36), (84, 36), (88, 58), (84, 84), (16, 84)]), base, 'f'),
           L(outline([(10, 70), (6, 34), (2, 22, 1), (14, 30), (18, 60)]), wing, 'f'), L(outline(mir([(10, 70), (6, 34), (2, 22, 1), (14, 30), (18, 60)])), wing, 'f')]
    if scarf:
        out += [L(outline([(16, 90), (84, 90), (84, 104), (16, 104)]), scarf, 'f'), L(outline([(50, 96), (30, 106, 1), (40, 112), (50, 104), (60, 116, 1), (66, 100)]), scarf, 'f')]
    return out


# Truman "Green" Verdy: casco verde de rana con los ojos saltones amarillo verdosos, alas blancas a los lados, pinchos
# negros por encima y un pañuelo verde que le tapa la barbilla y vuela a un lado
FG, FGE, FGS = _c('#3a9a1e'), _c('#c8e84a'), _c('#2a7a1a')
C('truman-green-verdy', 'normal', P('#262628', '#f2b878'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=94, hairline=False),
  dome('front', top=-6, w=42, cy=38, n=8, amp=10, seed=111, sb=40) + hero_mask('front', FG, FGE, scarf=FGS, eye_shape=[(24, 48), (42, 46), (44, 66), (28, 70)]),
  dome('side', top=-6, w=42, cy=38, n=8, amp=10, seed=111, nape=60, fr=40) + hero_mask('side', FG, FGE, scarf=FGS),
  dome('back', top=-6, w=42, cy=38, n=8, amp=10, seed=111, nape=60) + hero_mask('back', FG, FGE, scarf=FGS))

# Vanity Percy (portera): chica de melena negro verdosa con raya en medio que se abre en puntas a la altura de los
# hombros y una diadema gris lila; piel muy clara, ojos rojos entornados y media sonrisa
LAV = _c('#a8a0c8')
C('vanity-percy', 'chica', P('#1a3a30', '#ecdcbc', iris='#c02020', shade='#122a22'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=95, hairline=[(14, 70), (18, 56), (30, 44), (48, 38), (50, 42), (52, 38), (70, 44), (82, 56), (86, 70)]),
  longhair('front', length=100, flare=14, top=2, ends=4, part=True) + [line(quad((14, 40), (50, 16), (86, 40)), LAV, 2.4)],
  longhair('side', length=100, flare=14, top=2, ends=3) + [line(quad((40, 8), (60, 14), (80, 30)), LAV, 2.4)],
  longhair('back', length=102, flare=14, top=2, ends=5))

# Verity Soliz: chica de piel morena con el pelo recogido bajo un gorro en forma de huevo verde menta con franjas crema;
# sombra azul en los ojos, la nariz pintada en rombo y la boca abierta
MNT, MNC = _c('#9ac8b8'), _c('#ece0c0')
C('verity-soliz', 'chica', P('#9ac8b8', '#8a5030', iris='#202830'),
  F(eyes='sharp', brows=False, mouth='none', hairline=False),
  [L(outline([(16, 74), (8, 40), (18, 10), (50, -6), (82, 10), (92, 40), (84, 74), (74, 60), (60, 52), (50, 64, 1), (40, 52), (26, 60)]), MNT, 'f'),
   L(outline([(14, 20), (60, -2), (76, 6), (24, 34)]), MNC, 'f', False), L(outline([(10, 44), (84, 14), (90, 26), (14, 58)]), MNC, 'f', False),
   L(outline([(25, 67), (44, 70), (43, 73), (27, 71)]), _c('#2a5ab0'), 'f', False), L(outline(mir([(25, 67), (44, 70), (43, 73), (27, 71)])), _c('#2a5ab0'), 'f', False),
   L([(50, 80), (53, 86), (50, 92), (47, 86)], _c('#2a3a6a'), 'f', False, True), L(ell(50, 98, 3, 3.6), _c('#5a1a1a'), 'f', False)],
  [L(outline([(76, 54), (86, 38), (80, 10), (54, -6), (26, 0), (8, 20), (2, 50), (8, 76), (26, 74), (40, 62), (60, 56)]), MNT, 'f'),
   L(outline([(20, 6), (70, -2), (72, 8), (24, 18)]), MNC, 'f', False), L(outline([(4, 42), (84, 18), (88, 30), (8, 56)]), MNC, 'f', False),
   L(outline([(78, 70), (88, 72), (86, 78), (78, 76)]), _c('#2a5ab0'), 'f', False)],
  [L(outline([(14, 82), (8, 40), (18, 10), (50, -6), (82, 10), (92, 40), (86, 82), (50, 90)]), MNT, 'f'),
   L(outline([(14, 20), (60, -2), (76, 6), (24, 34)]), MNC, 'f', False), L(outline([(10, 48), (86, 18), (90, 32), (14, 62)]), MNC, 'f', False)])

# Verne Spring: pelo rubio pálido ondulado y revuelto que le cae por los lados hasta el cuello, con mechones finos por la
# frente; gafas finas y ojos verde azulado
C('verne-spring', 'normal', P('#f2e0a0', '#f2c08a', iris='#3a8a8a', shade='#d8c07a'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=95, hairline=[(14, 70), (20, 52), (28, 66), (36, 48), (44, 64), (52, 46), (62, 62), (70, 48), (80, 60), (86, 70)]),
  dome('front', top=0, w=48, cy=46, n=10, amp=8, seed=121, long=98, flare=10, soft=True) + round_specs('front', _c('#8a6a3a'), 76, 14, 9, 7, 1.2),
  dome('side', top=0, w=48, cy=46, n=10, amp=8, seed=121, long=98, flare=10, fr=52, soft=True) + round_specs('side', _c('#8a6a3a'), 76, w=1.2),
  dome('back', top=0, w=48, cy=46, n=10, amp=8, seed=121, long=98, flare=10, soft=True))

# Vick Pointer: pelo azul acero en mechones de punta echados hacia arriba y a un lado; una máscara azul marino le tapa la
# nariz, la boca y media cara en diagonal, y solo se le ve un ojo
NAVM = _c('#2a2a40')
C('vick-pointer', 'normal', P('#6a98a8', '#f2c088', iris='#201818', shade='#4e7888'),
  F(eyes='normal', brows=True, mouth='none', hairline=[(14, 64), (18, 50), (32, 58), (40, 44), (52, 56), (62, 44), (74, 54), (82, 50), (86, 64)]),
  dome('front', top=-10, w=46, cy=42, n=8, amp=16, sweep=0.6, seed=131, sb=68) +
  [L(outline([(14, 88), (40, 84), (90, 68), (88, 94), (70, 108), (50, 110), (30, 106), (16, 98)]), NAVM, 'f')],
  dome('side', top=-10, w=46, cy=42, n=8, amp=16, sweep=0.6, seed=131, nape=86, fr=48) +
  [L(outline([(60, 80), (88, 76), (90, 92), (80, 104), (62, 100)]), NAVM, 'f'), line([(60, 82), (46, 74)], NAVM, 1.6)],
  dome('back', top=-10, w=46, cy=42, n=8, amp=16, sweep=0.6, seed=131, nape=86) + [line([(12, 80), (88, 80)], NAVM, 1.8)])

# Vince Firewall: melena rosa empolvado lisa con raya en medio que le cae hasta los hombros; ojos castaños, ceño
# fruncido y unas rayitas en las mejillas
C('vince-firewall', 'normal', P('#d8a0a0', '#f2c094', iris='#6a3a22', shade='#b88080'),
  F(eyes='normal', brows='angry', mouth='frown', mouth_y=95, hairline=[(14, 70), (18, 56), (30, 44), (48, 36), (50, 40), (52, 36), (70, 44), (82, 56), (86, 70)]),
  longhair('front', length=104, flare=4, top=2, ends=3, part=True) + [line([(26, 86), (30, 84)], _c('#c06a50'), 1.0), line([(74, 86), (70, 84)], _c('#c06a50'), 1.0)],
  longhair('side', length=104, flare=4, top=2, ends=3),
  longhair('back', length=106, flare=4, top=2, ends=4))

# Vince Tinct (portero): cresta azul marino peinada hacia atrás sobre los lados rapados azul grisáceo, cara alargada y
# morena, orejas grandes, ojos afilados y media sonrisa torcida
SHV = _c('#5a7a9a')
C('vince-tinct', 'delgado', P('#2a4a6a', '#c08048', iris='#201818', shade='#1e3650'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=100, big_ears=3, ear_out=3, face_front=face(chin=110, jaw=-2), face_side=face_side(chin=8),
    hairline=[(16, 58), (24, 46), (40, 40), (50, 54), (60, 40), (76, 46), (84, 58)]),
  [L(outline([(18, 60), (16, 34), (28, 16), (50, 10), (72, 16), (84, 34), (82, 60), (50, 50)]), SHV),
   L(outline([(36, 46), (34, 14), (44, -8), (54, -14, 1), (60, -2), (66, 14), (64, 46), (50, 58, 1)]))],
  [L(outline([(78, 46), (86, 32), (80, 14), (56, 4), (28, 6), (10, 20), (4, 46), (12, 70), (30, 72), (40, 56), (56, 50)]), SHV),
   L(outline([(84, 30), (76, 4), (60, -14, 1), (40, -6), (20, 2), (8, 18), (6, 40), (30, 24), (60, 18)]))],
  [L(outline([(16, 72), (14, 34), (28, 16), (50, 10), (72, 16), (86, 34), (84, 72), (50, 80)]), SHV),
   L(outline([(38, 74), (34, 14), (44, -6), (50, -10, 1), (56, -6), (66, 14), (62, 74), (50, 80)]))])

# Virgil "Yellow" Amber (portero): casco amarillo de héroe con marcas naranjas, alas blancas a los lados, un mechón
# castaño que asoma por arriba y un pañuelo amarillo
YM, YMO, YMS = _c('#f2c81e'), _c('#f08a1e'), _c('#e8b81a')
C('virgil-yellow-amber', 'normal', P('#7a4a22', '#f2b878'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=94, hairline=False),
  crop('front', top=4) + [L(outline([(28, 30), (34, 10), (60, 4), (96, -6, 1), (74, 12), (72, 30)]))] + hero_mask('front', YM, YMO, scarf=YMS) +
  [line([(40, 74), (48, 74)], OUTC, 1.6), line([(52, 74), (60, 74)], OUTC, 1.6)],
  crop('side', top=4) + [L(outline([(40, 32), (40, 10), (60, 2), (96, -8, 1), (76, 12), (76, 32)]))] + hero_mask('side', YM, YMO, scarf=YMS),
  crop('back', top=4) + [L(outline([(28, 30), (34, 10), (60, 4), (96, -6, 1), (74, 12), (72, 30)]))] + hero_mask('back', YM, YMO, scarf=YMS))


# ------------------------------------------------------------------------------------------------------------ 49-56

# Wally Cooper (su modelo 3D es de otro personaje: se sigue el retrato): melena lisa gris oscura hasta los hombros con el
# flequillo que le tapa un ojo, una venda granate cruzada sobre ese ojo; el otro ojo morado y entornado, media sonrisa
BND = _c('#8a2a2e')
C('wally-cooper', 'normal', P('#4a4844', '#f6caa0', iris='#6a4a9a', shade='#363430'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=95, hairline=[(14, 70), (18, 52), (30, 42), (46, 40), (58, 46), (70, 58), (80, 64), (86, 70)]),
  longhair('front', length=104, flare=6, top=2, ends=3) +
  [L(outline([(14, 62), (30, 64), (60, 70), (84, 72), (84, 80), (58, 80), (32, 74), (14, 72)]), BND, 'f'),
   L(ell(66, 77, 5, 4), WHITE, 'f', ln=True), dot(66, 78, 2.6, _c('#6a4a9a')), line([(60, 74), (72, 74)], OUTC, 2.2),
   line([(64, 86), (70, 85)], _c('#c08a7a'), 1.0)],
  longhair('side', length=104, flare=6, top=2, ends=3) + [L(outline([(54, 62), (88, 70), (88, 78), (54, 72)]), BND, 'f')],
  longhair('back', length=106, flare=6, top=2, ends=4) + [line([(8, 66), (92, 66)], BND, 2.4)])

# Wally Waymire: pelo azul pizarra con raya en medio y los lados largos que se curvan hacia dentro en punta junto a la
# mandíbula; gafas negras y ojos ámbar
C('wally-waymire', 'normal', P('#3e5a6a', '#f2b47c', iris='#b08a2a', shade='#2e4654'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=[(14, 66), (18, 54), (30, 44), (48, 38), (50, 42), (52, 38), (70, 44), (82, 54), (86, 66)]),
  [L(outline([(16, 66), (10, 36), (24, 10), (50, 0), (76, 10), (90, 36), (84, 66), (88, 92), (80, 100, 1), (78, 74), (22, 74), (20, 100, 1), (12, 92)])),
   L(outline([(56, 4), (80, 14), (90, 40), (88, 90), (80, 60)]), 'shade', 'b', False)] + round_specs('front', BLACK, 76, 14, 10, 6.5, 2.0),
  [L(outline([(78, 50), (86, 36), (80, 12), (56, 0), (30, 2), (12, 16), (4, 44), (6, 74), (16, 94), (30, 102, 1), (36, 80), (42, 62), (58, 54)]))] +
  round_specs('side', BLACK, 76, rx=6, ry=6.5, w=2.0),
  [L(outline([(12, 74), (8, 36), (22, 10), (50, 0), (78, 10), (92, 36), (88, 74), (86, 96, 1), (66, 90), (50, 92), (34, 90), (14, 96, 1)])),
   L(outline([(56, 4), (82, 14), (92, 40), (88, 90), (66, 88)]), 'shade', 'b', False)])

# Walter Trope: pelo rojo anaranjado salvaje en pinchos hacia arriba y a los lados, con mechones largos que le cruzan la
# cara hasta la barbilla; ojos verde agua y ceño fruncido
C('walter-trope', 'normal', P('#c43c12', '#d89a62', iris='#2a9a9a', shade='#9a2c0a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, hairline=[(14, 60), (20, 50), (30, 56), (40, 46), (50, 54), (60, 46), (70, 56), (80, 50), (86, 60)]),
  dome('front', top=-14, w=50, cy=44, n=10, amp=18, sweep=-0.3, seed=141, sb=72) +
  [fr([(40, 50), (48, 52), (42, 80), (36, 96, 1), (36, 70)]), fr([(56, 50), (64, 52), (62, 76), (64, 100, 1), (56, 74)]),
   fr([(26, 52), (32, 54), (24, 80), (16, 92, 1), (22, 66)])],
  dome('side', top=-14, w=50, cy=44, n=10, amp=18, sweep=-0.3, seed=141, nape=88, fr=50) + [fr([(70, 50), (80, 52), (78, 80), (80, 98, 1), (72, 76)])],
  dome('back', top=-14, w=50, cy=44, n=10, amp=18, sweep=-0.3, seed=141, nape=88))

# Waylon Tripp: pelo castaño oscuro peinado hacia atrás hasta la nuca con las puntas abiertas a los lados; piel morena,
# cara alargada y los ojos apretados de fastidio
C('waylon-tripp', 'delgado', P('#4a3a30', '#c08848', shade='#382c24'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=100, face_front=face(chin=108), face_side=face_side(chin=6),
    hairline=[(14, 62), (18, 50), (30, 42), (50, 40), (70, 42), (82, 50), (86, 62)]),
  [L(outline([(16, 64), (10, 36), (22, 12), (50, 2), (78, 12), (90, 36), (84, 64), (96, 74, 1), (86, 80), (82, 52), (18, 52), (14, 80), (4, 74, 1)])),
   L(outline([(56, 6), (80, 16), (90, 40), (86, 62), (78, 40)]), 'shade', 'b', False)] +
  [line([(28, 72), (40, 76), (28, 80)], OUTC, 2.2), line([(72, 72), (60, 76), (72, 80)], OUTC, 2.2),
   line([(28, 66), (42, 70)], OUTC, 2.2), line([(72, 66), (58, 70)], OUTC, 2.2), line([(48, 70), (52, 70)], OUTC, 1.0)],
  [L(outline([(78, 50), (86, 36), (80, 12), (56, 0), (30, 2), (12, 16), (4, 44), (4, 70), (-6, 84, 1), (12, 80), (22, 88, 1), (30, 72), (40, 60), (56, 54)])),
   line([(76, 72), (84, 76), (76, 80)], OUTC, 2.2)],
  [L(outline([(12, 74), (8, 36), (22, 10), (50, 2), (78, 10), (92, 36), (88, 74), (98, 84, 1), (80, 84), (66, 92), (50, 94), (34, 92), (20, 84), (2, 84, 1)])),
   L(outline([(56, 6), (82, 16), (92, 40), (88, 74), (66, 90)]), 'shade', 'b', False)])

# Wayne Fluke (portero): cara larga y pálida de cortesano antiguo con un gorro negro eboshi pequeño en lo alto, dos
# manchas negras ovaladas por cejas en la frente, ojos entornados y la boca en uve
EBO = _c('#3a3a4a')
WAYNEF = blob([(18, 30), (50, 14), (82, 30), (86, 70), (82, 104), (66, 118), (50, 120), (34, 118), (18, 104), (14, 70)])
C('wayne-fluke', 'delgado', P('#3a3a4a', '#f2e2b4', skin_d='#d8c494'),
  F(eyes='none', brows=False, mouth='none', hairline=False, face_front=WAYNEF,
    face_side=blob([(46, 14), (72, 18), (86, 36), (90, 66), (88, 100), (78, 116), (58, 118), (40, 108), (22, 86), (14, 56), (22, 26)])),
  [L(outline([(38, 18), (36, -10), (50, -18), (64, -10), (62, 18)]), EBO, 'f'),
   L(ell(36, 54, 5, 3.4), EBO, 'f', False), L(ell(64, 54, 5, 3.4), EBO, 'f', False),
   line([(28, 74), (42, 74)], OUTC, 2.2), line([(58, 74), (72, 74)], OUTC, 2.2), dot(36, 75.5, 1.4, OUTC), dot(64, 75.5, 1.4, OUTC),
   line([(48, 82), (50, 90)], _c('#b89a6a'), 1.0), line([(44, 104), (50, 98), (56, 104)], OUTC, 1.6)],
  [L(outline([(48, 18), (46, -10), (58, -18), (70, -10), (70, 18)]), EBO, 'f'), L(ell(80, 54, 4, 3), EBO, 'f', False),
   line([(76, 74), (86, 74)], OUTC, 2.2), line([(82, 104), (88, 100)], OUTC, 1.6)],
  [L(outline([(38, 18), (36, -10), (50, -18), (64, -10), (62, 18)]), EBO, 'f'), L(WAYNEF, 'skin')])

# Wiley Blinks: grandullón de pelo castaño rojizo en rizos redondos alrededor de la cabeza; cejas en espiral enfadadas,
# nariz gorda y una mueca enseñando los dientes apretados
WILF = blob([(10, 50), (50, 40), (90, 50), (96, 76), (92, 102), (72, 114), (50, 116), (28, 114), (8, 102), (4, 76)])
C('wiley-blinks', 'corpulento', P('#b8501e', '#c27a3c', shade='#923e14'),
  F(eyes='round', brows=False, mouth='none', face_front=WILF, ear_out=6, hairline=[(8, 62), (18, 50), (34, 46), (50, 50), (66, 46), (82, 50), (92, 62)]),
  dome('front', top=-4, w=52, cy=44, n=12, amp=7, soft=True, seed=151, sb=70) +
  [line(quad((24, 70), (34, 60), (44, 70)), OUTC, 2.4), line(quad((76, 70), (66, 60), (56, 70)), OUTC, 2.4),
   L(ell(50, 86, 7, 5.4), _c('#9a5a2a'), 'f', False, True),
   L(blob([(30, 96), (50, 92), (70, 96), (66, 108), (50, 110), (34, 108)], 6), WHITE, 'f', False, True), line([(32, 101), (68, 101)], OUTC, 1.0)],
  dome('side', top=-4, w=52, cy=44, n=12, amp=7, soft=True, seed=151, nape=88, fr=50) + [L(ell(90, 86, 5, 5), _c('#9a5a2a'), 'f', False, True)],
  dome('back', top=-4, w=52, cy=44, n=12, amp=7, soft=True, seed=151, nape=88))

# Will Kilmon: pelo gris plateado en media melena despeinada con un pelo de punta en lo alto, gafas redondas finas y
# los ojos cerrados de sonrisa
C('will-kilmon', 'normal', P('#b8bcc8', '#f6dcb4', shade='#969aa8'),
  F(eyes='none', brows=True, mouth='smile', mouth_y=95, hairline=[(14, 68), (20, 52), (30, 62), (40, 48), (50, 60), (60, 48), (70, 62), (80, 52), (86, 68)]),
  dome('front', top=2, w=48, cy=46, n=12, amp=4, seed=161, long=94, flare=8, soft=True) + [L(outline([(50, 6), (58, -12, 1), (62, 4)]))] +
  round_specs('front', _c('#5a5a62'), 76, 14, 10, 7, 1.2) + squint(76, 14, 5, True),
  dome('side', top=2, w=48, cy=46, n=12, amp=4, seed=161, long=94, flare=8, fr=52, soft=True) + [L(outline([(54, 4), (64, -12, 1), (66, 4)]))] +
  round_specs('side', _c('#5a5a62'), 76, w=1.2),
  dome('back', top=2, w=48, cy=46, n=12, amp=4, seed=161, long=94, flare=8, soft=True) + [L(outline([(48, 6), (56, -12, 1), (60, 4)]))])

# Will Ramin: tupé alto castaño oscuro estrecho que sube en punta hacia atrás, cara larga de mandíbula grande, orejas
# grandes, ojos afilados y una sonrisa enorme de dientes
C('will-ramin', 'normal', P('#4a3028', '#d0904c', iris='#201818', shade='#36221c'),
  F(eyes='round', brows='angry', mouth='none', big_ears=3, ear_out=4, face_front=face(chin=110, jaw=4), face_side=face_side(chin=8, jaw=4),
    hairline=[(18, 58), (26, 44), (40, 36), (50, 34), (60, 36), (74, 44), (82, 58)]),
  [L(outline([(20, 60), (18, 34), (30, 12), (46, -10), (60, -22, 1), (64, 0), (78, 16), (82, 34), (80, 60), (50, 48)]))] +
  [L(blob([(30, 94), (50, 90), (70, 94), (68, 106), (50, 110), (32, 106)], 6), WHITE, 'f', False, True), line([(32, 100), (68, 100)], OUTC, 1.0),
   line([(42, 92), (42, 108)], OUTC, 0.8), line([(50, 91), (50, 110)], OUTC, 0.8), line([(58, 92), (58, 108)], OUTC, 0.8), dot(50, 86, 1.6, 'skin_d')],
  [L(outline([(78, 44), (86, 30), (80, 10), (60, -6), (40, -22, 1), (24, -4), (10, 14), (4, 40), (8, 64), (22, 72), (36, 66), (44, 54), (60, 48)])),
   L(blob([(74, 94), (92, 92), (92, 104), (78, 106)], 6), WHITE, 'f', False, True)],
  [L(outline([(16, 70), (16, 34), (30, 12), (44, -10), (56, -22, 1), (62, 0), (76, 14), (84, 34), (84, 70), (50, 78)]))])


# ------------------------------------------------------------------------------------------------------------ 57-60

# Wilma Morgan (portera): chica de piel morena con el pelo gris pardo en trenzas pegadas hacia atrás que se abren a los
# lados en dos alas onduladas hasta los hombros; cinta blanca en la frente, ceño fruncido y la boca abierta
HBW = _c('#ece4d0')
C('wilma-morgan', 'chica', P('#5a5048', '#b07a50', iris='#201818', shade='#463e36'),
  F(eyes='round', brows='angry', mouth='none', hairline=[(14, 62), (20, 52), (50, 48), (80, 52), (86, 62)]),
  [L(outline([(16, 60), (12, 34), (24, 10), (50, 0), (76, 10), (88, 34), (84, 60), (96, 76), (106, 92, 1), (88, 94), (80, 80), (20, 80), (12, 94), (-6, 92, 1),
              (4, 76)])),
   strand([(36, 6), (32, 40)], 'shade', 'b', 1.2), strand([(50, 2), (50, 40)], 'shade', 'b', 1.2), strand([(64, 6), (68, 40)], 'shade', 'b', 1.2),
   L(outline([(12, 46), (50, 38), (88, 46), (88, 56), (50, 50), (12, 56)]), HBW, 'f'), L(ell(50, 98, 3.4, 3), _c('#7a2a2a'), 'f', False, True)],
  [L(outline([(78, 46), (86, 32), (80, 10), (56, -2), (28, 2), (10, 16), (2, 44), (4, 70), (-4, 88, 1), (14, 92), (30, 88), (36, 70), (44, 56), (60, 50)])),
   L(outline([(4, 50), (50, 40), (88, 42), (88, 52), (50, 50), (6, 60)]), HBW, 'f')],
  [L(outline([(14, 70), (10, 34), (22, 10), (50, 0), (78, 10), (90, 34), (86, 70), (98, 80), (106, 94, 1), (86, 96), (70, 86), (50, 88), (30, 86), (14, 96), (-6, 94, 1),
              (2, 80)])),
   strand([(36, 6), (34, 80)], 'shade', 'b', 1.2), strand([(50, 2), (50, 84)], 'shade', 'b', 1.2), strand([(64, 6), (66, 80)], 'shade', 'b', 1.2),
   L(outline([(10, 48), (50, 40), (90, 48), (90, 58), (50, 52), (10, 58)]), HBW, 'f')])

# Wright Tandem: pelo verde azulado oscuro con un mechón de punta en lo alto y los lados largos hasta la mandíbula; ojos
# rojos enfadados y la boca apretada enseñando los dientes
C('wright-tandem', 'normal', P('#1e5a70', '#f8c080', iris='#b02a2a', shade='#164656'),
  F(eyes='normal', brows='angry', mouth='buck', mouth_y=95, hairline=[(14, 64), (20, 52), (34, 58), (46, 48), (58, 56), (70, 48), (80, 54), (86, 64)]),
  [L(outline([(16, 64), (10, 36), (20, 12), (40, 2), (52, -14, 1), (56, 0), (72, -6, 1), (70, 8), (84, 18), (90, 36), (84, 64), (88, 96), (78, 100, 1), (78, 72), (22, 72),
              (22, 100, 1), (12, 96)])),
   L(outline([(58, 4), (82, 16), (90, 40), (88, 92), (80, 62)]), 'shade', 'b', False)],
  [L(outline([(78, 50), (86, 36), (82, 14), (66, 0), (60, -14, 1), (50, 0), (30, 2), (12, 16), (4, 44), (6, 74), (18, 98, 1), (32, 86), (40, 62), (58, 54)]))],
  [L(outline([(12, 74), (8, 36), (20, 12), (42, 2), (52, -14, 1), (58, 0), (72, -6, 1), (72, 8), (86, 18), (92, 36), (88, 74), (88, 98, 1), (66, 90), (50, 92), (34, 90),
              (12, 98, 1)])),
   L(outline([(58, 4), (84, 16), (92, 40), (88, 92), (66, 88)]), 'shade', 'b', False)])

# Yve Dunbar (portera): chica de piel morena con un afro enorme rojo anaranjado; ojos rojos con sombra oscura alrededor y
# la boca entreabierta
C('yve-dunbar', 'chica', P('#e8401a', '#8a5030', iris='#c02020', shade='#b82e10'),
  F(eyes='sharp', brows='angry', mouth='none', hairline=[(10, 64), (18, 56), (34, 52), (50, 54), (66, 52), (82, 56), (90, 64)]),
  dome('front', top=-12, w=58, cy=40, n=14, amp=6, soft=True, seed=171, sb=74) +
  [L(outline([(24, 70), (44, 72), (42, 80), (26, 78)]), _c('#3a1a1a'), 'f', False), L(outline(mir([(24, 70), (44, 72), (42, 80), (26, 78)])), _c('#3a1a1a'), 'f', False),
   L(ell(36, 76, 3.6, 3), _c('#c02020'), 'f', False), L(ell(64, 76, 3.6, 3), _c('#c02020'), 'f', False), L(ell(50, 98, 3, 2.4), _c('#5a1a1a'), 'f', False)],
  dome('side', top=-12, w=58, cy=40, n=14, amp=6, soft=True, seed=171, nape=90, fr=50),
  dome('back', top=-12, w=58, cy=40, n=14, amp=6, soft=True, seed=171, nape=90))

# Zach Putter: casquete castaño ancho y plano como una seta con el flequillo recto, cara alargada de orejas grandes, un
# ojo en blanco y el otro entornado, nariz larga y la boca recta
C('zach-putter', 'delgado', P('#6a4a22', '#f2c080', shade='#4e361a'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=102, big_ears=4, ear_out=4, face_front=face(chin=110, jaw=-2), face_side=face_side(chin=8, nose=4),
    hairline=False),
  [L(outline([(-8, 42), (8, 14), (30, 2), (50, 0), (70, 2), (92, 14), (108, 42), (84, 44), (82, 52), (18, 52), (16, 44)])),
   L(outline([(60, 2), (90, 14), (106, 40), (84, 40)]), 'shade', 'b', False),
   strand([(30, 40), (32, 52)], 'shade', 'f', 1.0), strand([(50, 40), (50, 52)], 'shade', 'f', 1.0), strand([(70, 40), (68, 52)], 'shade', 'f', 1.0),
   line([(26, 74), (42, 72)], OUTC, 2.2), line(quad((27, 75), (34, 79), (41, 75)), OUTC, 1.2), dot(35, 75.5, 1.4, OUTC),
   L(ell(64, 75, 5.6, 5), WHITE, 'f', ln=True), line(quad((50, 70), (46, 86), (52, 90)), _c('#b07a4a'), 1.2)],
  [L(outline([(-10, 44), (4, 14), (30, 0), (56, 0), (80, 8), (98, 28), (106, 44), (86, 46), (60, 48), (30, 52)])),
   L(ell(83, 75, 3.6, 5), WHITE, 'f', ln=True)],
  [L(outline([(-8, 44), (8, 14), (30, 2), (50, 0), (70, 2), (92, 14), (108, 44), (80, 50), (50, 52), (20, 50)]))])
