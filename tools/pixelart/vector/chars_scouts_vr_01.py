"""Ojeadores de Victory Road (scouts-vr), tanda 01: dibujados a partir de su retrato; claves 'scouts-vr:<id>'.

El frente sale del retrato de Victory Road; el perfil y la espalda se deducen de cómo cae cada peinado (o del modelo 3D
cuando es del mismo personaje). Reutiliza las ayudas de las tandas de IE (dome, hl, face, bowl3, hood...)."""
from chars import CHARS, L, OUTC, blob, ell, longhair, messy, outline, pal, rope, strand  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401
from chars_scouts_ie1_09 import dome, hl, face, face_side, mark, _c  # noqa: F401
from chars_scouts_ie1_03 import fr, round_specs, thick_brows, side_brow, shades, tri_nose  # noqa: F401
from chars_scouts_ie3_02 import ring, skull3, hood, bowl3, side_lock  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)
PINK = (236, 140, 150, 255)
K = 'scouts-vr:'


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


def blush(y=86, dx=22, r=4.4, c=PINK):
    return [L(ell(50 - dx, y, r, r * 0.7), c, 'f', False), L(ell(50 + dx, y, r, r * 0.7), c, 'f', False)]


def R(p0, c, p1, w=6, col='mid', z='f'):
    """Rizo o mechón grueso (rope de chars.py) como capa."""
    return L(rope(p0, c, p1, w), col, z)


def bow(x, y, c, s=1.0):
    """Lazo pequeño (dos lóbulos y un nudo)."""
    return [L(blob([(x, y), (x - 9 * s, y - 6 * s), (x - 11 * s, y + 4 * s)], 4), c, 'f'),
            L(blob([(x, y), (x + 9 * s, y - 6 * s), (x + 11 * s, y + 4 * s)], 4), c, 'f'), L(ell(x, y, 2.6 * s, 2.6 * s), c, 'f')]


def bun(x, y, r, c='mid', z='b'):
    return L(ell(x, y, r, r * 0.92), c, z)


def specs(view, c=BLACK, y=76):
    return round_specs(view, c, y)


# ------------------------------------------------------------------ jugadores

# Abbie Sentridge: coleta alta verde oscuro con un lazo rosa, un mechón grande cayendo por la izquierda y otro largo
# rizado por la derecha; ojos grandes de ojeras azules y boquita triste
GRN = '#3a5a3a'
C('abbie-sentridge', 'chica', P(GRN, '#f8dcc4', iris='#2c4a30'),
  F(eyes='big', mouth='frown', mouth_y=93, hairline=[(8, 70), (20, 50), (40, 44), (52, 60, ), (60, 44), (80, 48), (92, 70)]),
  dome('front', top=6, w=44, cy=46, sb=64, seed=1) +
  [L(outline([(52, 8), (40, -10), (58, -16), (72, -6), (66, 8)]), 'mid'), *bow(54, -8, _c('#e8a0c8'), 0.9),
   fr([(20, 50), (36, 36), (54, 40), (48, 62, 1), (34, 56), (24, 72), (14, 98, 1), (10, 76)]),
   fr([(82, 46), (94, 58), (100, 84), (92, 104, 1), (88, 84), (84, 64)])],
  dome('side', top=6, w=44, cy=46, nape=84, fr=50, seed=1) + [L(outline([(36, 6), (20, -10), (4, 6), (-6, 40), (6, 70, 1), (14, 40), (26, 14)]), 'mid')],
  dome('back', top=6, w=44, cy=46, nape=84, seed=1) + [L(outline([(42, 6), (40, -12), (58, -16), (62, 6)]), 'mid'),
                                                          L(outline([(44, 10), (36, 40), (44, 76, 1), (56, 40), (56, 10)]), 'mid'), *bow(52, -6, _c('#e8a0c8'), 0.9)])

# Actie Verran: pelo castaño grisáceo en casquete con una gran cinta amarilla en la frente y un mechón en arco encima;
# ojos ámbar enfadados, sonrisa de dientes
C('actie-verran', 'chica', P('#a89a88', '#f6c8a0', iris='#c87a1e'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, hairline=[(10, 66), (20, 50), (50, 46), (80, 50), (90, 66)]),
  bowl3('front', top=6, side=86, w=2, fringe=50) +
  [L(blob([(10, 46), (50, 40), (90, 46), (90, 60), (50, 56), (10, 60)], 6), _c('#f0c050'), 'f'),
   fr([(44, 58), (42, 36), (50, 30), (58, 36), (56, 58), (52, 40), (48, 40)])],
  bowl3('side', top=6, nape=94, fringe=50) + [L(blob([(10, 40), (88, 44), (88, 58), (10, 56)], 6), _c('#f0c050'), 'f')],
  bowl3('back', top=6, nape=94) + [L(blob([(6, 44), (94, 44), (94, 58), (6, 58)], 6), _c('#f0c050'), 'f')])

# Adal Miramond: melena azul petróleo muy oscura y despeinada hasta la mandíbula, con mechones de punta; piel morena, ojos
# pequeños con ojeras, marcas negras bajo los ojos y boca torcida
C('adal-miramond', 'normal', P('#1e3a48', '#9a6a44', iris='#2a2a2a'),
  F(eyes='round', brows=True, mouth='frown', mouth_y=94, hairline=hl(5, 66, 50, 60, seed=4)),
  messy('front', amp=12, n=10, seed=7, lo=90) + [mark([(34, 82), (36, 88)], BLACK, w=1.4), mark([(66, 82), (64, 88)], BLACK, w=1.4)],
  messy('side', amp=12, n=10, seed=7, lo=90, nape=96),
  messy('back', amp=12, n=10, seed=7, lo=90, nape=96))

# Adelaide Plainhart: media melena castaña en casco con flequillo recto y gafas redondas negras; sonrisa tranquila
C('adelaide-plainhart', 'chica', P('#8a4a2a', '#f8dcc4', iris='#5a3a4a'),
  F(eyes='normal', mouth='smile', mouth_y=93, hairline=[(8, 58), (92, 58)]),
  bowl3('front', top=2, side=94, w=4, fringe=60) + specs('front'),
  bowl3('side', top=2, nape=96, w=4, fringe=60) + specs('side'),
  bowl3('back', top=2, nape=96, w=4))

# Adele Lettante: pelo lila grisáceo corto y abombado, con las puntas hacia fuera a los lados; ojos azules grandes y
# boquita redonda de sorpresa
C('adele-lettante', 'chica', P('#b4aac0', '#f8dcc4', iris='#3a5aa8'),
  F(eyes='big', mouth='o', mouth_y=94, hairline=[(8, 62), (22, 50), (44, 44), (60, 50), (80, 50), (92, 62)]),
  dome('front', top=2, w=46, cy=44, sb=84, seed=2) + [fr([(6, 74), (-4, 92, 1), (10, 86)]), fr([(94, 70), (106, 80, 1), (92, 84)]),
                                                     fr([(18, 52), (40, 34), (62, 42), (50, 54), (34, 56)])] +
  [L(ell(50, 94, 2.2, 2.6), (120, 50, 50, 255), 'f', False)],
  dome('side', top=2, w=46, cy=44, nape=88, fr=52, seed=2) + [fr([(14, 78), (0, 92, 1), (20, 88)])],
  dome('back', top=2, w=46, cy=44, nape=88, seed=2) + [fr([(6, 74), (-4, 90, 1), (12, 84)]), fr([(94, 74), (104, 90, 1), (88, 84)])])

# Aeron Rushmore: pelo corto azul pizarra con una mancha verde lima como pintura encima; ojos grandes violeta y sonrisa
LIME = _c('#a8e040')
C('aeron-rushmore', 'normal', P('#4a5a88', '#f8dcc4', iris='#7a4aa8'),
  F(eyes='big', mouth='smile', mouth_y=93, hairline=[(10, 66), (22, 52), (40, 56), (56, 50), (72, 56), (90, 66)]),
  dome('front', top=4, w=46, cy=46, sb=78, seed=3) +
  [L(outline([(10, 36), (24, 14), (50, 4), (78, 12), (92, 34), (84, 44), (78, 30), (70, 40), (60, 28), (48, 42), (40, 28), (28, 44), (20, 32)]), LIME, 'f')],
  dome('side', top=4, w=46, cy=46, nape=88, fr=54, seed=3) + [L(outline([(10, 34), (30, 8), (60, 2), (88, 24), (78, 34), (66, 22), (56, 34), (44, 22), (30, 36)]), LIME, 'f')],
  dome('back', top=4, w=46, cy=46, nape=88, seed=3) + [L(outline([(8, 40), (22, 14), (50, 4), (80, 14), (92, 40), (80, 48), (68, 32), (52, 46), (38, 30), (22, 48)]), LIME, 'f')])

# Agil Surefall: melena de león crema enorme con la parte de arriba castaño oscuro en punta; piel morena, cejas fruncidas
C('agil-surefall', 'corpulento', P('#e8d4a8', '#9a6a44', iris='#2a2a2a', low='#3a2a1e'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, hairline=[(14, 66), (24, 50), (50, 46), (76, 50), (86, 66)]),
  dome('front', top=-2, w=54, cy=50, n=12, amp=8, soft=True, long=106, flare=8, seed=5) +
  [L(outline([(22, 52), (26, 24), (40, 12), (50, 4, 1), (60, 12), (74, 24), (78, 52), (66, 42), (50, 50, 1), (34, 42)]), 'low', 'f')],
  dome('side', top=-2, w=54, cy=50, n=12, amp=8, soft=True, long=106, flare=8, fr=52, seed=5) +
  [L(outline([(40, 4), (70, 10), (88, 30), (80, 46), (60, 36), (40, 30)]), 'low', 'f')],
  dome('back', top=-2, w=54, cy=50, n=12, amp=8, soft=True, long=106, flare=8, seed=5))

# Ah Dackchin: señor de sombrero de paja crema con cinta negra, gafas de sol de cristal naranja, patillas y perilla negras
STRAW, BAND = _c('#e8dcb8'), _c('#2a2422')
def _hat(view):
    if view == 'front':
        return [L(blob([(-8, 48), (50, 40), (108, 48), (100, 56), (50, 52), (0, 56)], 6), STRAW, 'f'),
                L(outline([(20, 50), (22, 20), (50, 12), (78, 20), (80, 50)]), STRAW, 'f'), L(blob([(21, 40), (79, 40), (80, 50), (20, 50)], 4), BAND, 'f')]
    if view == 'side':
        return [L(blob([(-14, 46), (50, 40), (112, 46), (104, 54), (50, 52), (-6, 54)], 6), STRAW, 'f'),
                L(outline([(14, 48), (18, 18), (50, 10), (80, 18), (84, 48)]), STRAW, 'f'), L(blob([(15, 38), (83, 38), (84, 48), (14, 48)], 4), BAND, 'f')]
    return _hat('front')
C('ah-dackchin', 'normal', P('#2a2422', '#c89870', iris='#2a2a2a'),
  F(eyes='none', mouth='line', mouth_y=94, hairline=False),
  [L(blob([(14, 60), (16, 48), (84, 48), (86, 60), (84, 80), (16, 80)], 6), 'mid')] + _hat('front') + shades('front', 76, _c('#c8603a')) +
  [mark([(42, 104), (50, 108), (58, 104), (50, 100)], 'mid')],
  [L(blob([(8, 50), (50, 46), (56, 80), (20, 84)], 6), 'mid')] + _hat('side') + shades('side', 76, _c('#c8603a')),
  [L(blob([(14, 50), (86, 50), (86, 80), (14, 80)], 6), 'mid')] + _hat('back'))

# Aila Pavey: melena negra azulada lisa hasta los hombros con flequillo de mechones y las puntas abiertas; ojos grises
C('aila-pavey', 'chica', P('#24223a', '#f8dcc4', iris='#7a8090'),
  F(eyes='big', mouth='smile', mouth_y=93, hairline=[(8, 66), (20, 52), (34, 58), (46, 50), (58, 58), (72, 50), (84, 56), (92, 66)]),
  longhair('front', length=104, flare=8, top=2, fringe=60),
  longhair('side', length=104, flare=8, top=2),
  longhair('back', length=104, flare=8, top=2, ends=4))

# Aimee Porteret: pelo castaño rizado en una mata redonda y corta; ojos grises grandes y boca abierta de alegría
C('aimee-porteret', 'chica', P('#8a5030', '#f8dcc4', iris='#7a7a80'),
  F(eyes='big', mouth='grin', mouth_y=94, hairline=[(10, 60), (24, 50), (40, 54), (54, 48), (68, 54), (82, 50), (90, 60)]),
  dome('front', top=-2, w=50, cy=42, n=13, amp=6, soft=True, sb=66, seed=8),
  dome('side', top=-2, w=50, cy=42, n=13, amp=6, soft=True, nape=84, fr=52, seed=8),
  dome('back', top=-2, w=50, cy=42, n=13, amp=6, soft=True, nape=84, seed=8))

# Akela Portner (portero): pelo gris pizarra peinado hacia atrás con dos mechones azul celeste como cuernos sobre las sienes
# y patillas largas que se abren; marcas celestes alrededor de los ojos amarillos y sonrisa de dientes
SKY = _c('#80c8f0')
C('akela-portner', 'delgado', P('#4a5260', '#f2c098', iris='#e8c020'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=96, hairline=[(14, 64), (24, 46), (40, 40), (50, 54), (60, 40), (76, 46), (86, 64)]),
  dome('front', top=2, w=44, cy=44, sb=96, seed=9) +
  [fr([(14, 70), (6, 92), (16, 100, 1), (22, 80)]), fr([(86, 70), (94, 92), (84, 100, 1), (78, 80)]),
   L(outline([(30, 50), (20, 38), (26, 28), (34, 40), (40, 46)]), SKY, 'f'), L(outline([(70, 50), (80, 38), (74, 28), (66, 40), (60, 46)]), SKY, 'f'),
   mark([(26, 70), (40, 72)], SKY, w=1.6), mark([(74, 70), (60, 72)], SKY, w=1.6)],
  dome('side', top=2, w=44, cy=44, nape=96, fr=48, seed=9) + [L(outline([(70, 46), (80, 32), (88, 40), (82, 50)]), SKY, 'f')],
  dome('back', top=2, w=44, cy=44, nape=96, seed=9))

# Alanna Ordelyne: melena verde azulado muy oscuro hasta la mandíbula con flequillo tupido y las puntas hacia fuera; ojos
# grises entornados y boquita seria
C('alanna-ordelyne', 'chica', P('#1a3a34', '#f8dcc4', iris='#7a8a90'),
  F(eyes='sharp', mouth='frown', mouth_y=94, hairline=[(8, 62), (22, 56), (40, 60), (56, 56), (72, 60), (92, 62)]),
  bowl3('front', top=2, side=92, w=6, fringe=62) + [fr([(6, 86), (-4, 100, 1), (12, 96)]), fr([(94, 86), (104, 100, 1), (88, 96)])],
  bowl3('side', top=2, nape=96, w=6, fringe=62),
  bowl3('back', top=2, nape=96, w=6))

# Alara Belmont: melena castaña larga con flequillo de mechones y dos rizos grandes que se enroscan hacia fuera a la altura
# del cuello; ojos castaños grandes con pestañas
C('alara-belmont', 'chica', P('#9a5a30', '#f8d8b8', iris='#7a4a1e'),
  F(eyes='big', mouth='smile', mouth_y=94, hairline=[(8, 66), (22, 52), (36, 60), (50, 50), (64, 60), (78, 52), (92, 66)]),
  longhair('front', length=100, flare=6, top=0, fringe=62) + [R((10, 96), (-8, 104), (0, 92), 6), R((90, 96), (108, 104), (100, 92), 6)],
  longhair('side', length=100, flare=6, top=0) + [R((10, 96), (-6, 106), (2, 94), 6)],
  longhair('back', length=100, flare=6, top=0, ends=3) + [R((10, 96), (-8, 104), (0, 92), 6), R((90, 96), (108, 104), (100, 92), 6)])

# Aldus Ogden (portero): bajito de cabeza rapada gris con una tirita en la coronilla; cejas negras enormes, nariz con tirita
# y otra tirita en la mejilla
TAPE = _c('#f0dcc0')
C('aldus-ogden', 'bajito', P('#6a6a70', '#e8a070', iris='#e8c020'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=96, hairline=[(14, 60), (30, 48), (50, 46), (70, 48), (86, 60)]),
  [L(blob([(16, 62), (18, 36), (30, 16), (50, 8), (70, 16), (82, 36), (84, 62), (70, 52), (30, 52)], 8), 'mid'),
   L(blob([(56, 14), (70, 10), (72, 22), (58, 26)], 4), TAPE, 'f')] + thick_brows(64, BLACK, 6.0, 15, 0.6, 16) +
  [mark([(44, 84), (56, 84), (56, 90), (44, 90)], TAPE), mark([(28, 92), (36, 98), (32, 102), (24, 96)], TAPE)],
  skull3('side', 'mid') + [L(blob([(48, 6), (62, 4), (62, 16), (50, 16)], 4), TAPE, 'f')] + side_brow(64, BLACK, 6.0, 0.6),
  skull3('back', 'mid') + [L(blob([(44, 12), (58, 8), (60, 20), (46, 22)], 4), TAPE, 'f')])

# Alexei Einmeister: melena negra azulada hasta los hombros con mechones sueltos, una franja azul celeste y otra gris
# plata cayendo por la frente y tapándole un ojo; sonrisa de lado
SILV = _c('#c8c8d8')
C('alexei-einmeister', 'normal', P('#2a2a3a', '#f8dcc4', iris='#7a7a80'),
  F(eyes='sharp', mouth='smile', mouth_y=94, hairline=[(8, 66), (20, 50), (50, 44), (80, 50), (92, 66)]),
  dome('front', top=0, w=48, cy=44, long=100, flare=10, seed=10) +
  [fr([(26, 40), (44, 34), (60, 44), (54, 66), (44, 86, 1), (38, 64), (28, 56)]),
   L(outline([(40, 36), (48, 34), (46, 62), (42, 80, 1), (38, 60)]), SKY, 'f'), L(outline([(58, 36), (66, 40), (64, 60), (58, 56)]), SILV, 'f'),
   R((8, 92), (-8, 100), (0, 104), 5), R((92, 92), (108, 100), (100, 104), 5)],
  dome('side', top=0, w=48, cy=44, long=100, flare=10, fr=52, seed=10) + [L(outline([(36, 6), (50, 4), (30, 60), (20, 54)]), SKY, 'f')],
  dome('back', top=0, w=48, cy=44, long=100, flare=10, seed=10) + [L(outline([(36, 6), (46, 4), (40, 90, 1), (32, 60)]), SKY, 'f'),
                                                                     L(outline([(60, 6), (70, 8), (68, 70, 1), (60, 50)]), SILV, 'f')])

# Allegra Langton: pelo lila rosado en una nube de rizos grandes y redondos, con mechones que bajan hasta las mejillas;
# ojos verdes con pestañas y colorete
C('allegra-langton', 'chica', P('#c890d0', '#f8dcc4', iris='#3a8a6a'),
  F(eyes='big', mouth='smile', mouth_y=94, hairline=[(12, 70), (20, 52), (40, 56), (50, 46), (60, 56), (80, 52), (88, 70)]),
  dome('front', top=-6, w=50, cy=40, n=9, amp=7, soft=True, sb=80, seed=11) + blush(88, 22),
  dome('side', top=-6, w=50, cy=40, n=9, amp=7, soft=True, nape=86, fr=52, seed=11),
  dome('back', top=-6, w=50, cy=40, n=9, amp=7, soft=True, nape=86, seed=11))

# Alonzo Readdie: gorro de lana azul marino con un parche blanco a un lado; asoma pelo azul celeste en las sienes; ojos
# grises grandes y sonrisa amplia
NAVY = _c('#1e2440')
def _beanie(view, c=NAVY):
    if view == 'front':
        return [L(outline([(12, 58), (12, 30), (26, 10), (50, 2), (74, 10), (88, 30), (88, 58), (50, 54)]), c, 'f'),
                L(blob([(64, 30), (76, 28), (78, 40), (66, 42)], 4), WHITE, 'f')]
    if view == 'side':
        return [L(outline([(6, 60), (4, 30), (22, 8), (50, 0), (76, 8), (88, 30), (88, 54), (50, 54)]), c, 'f')]
    return [L(outline([(10, 62), (10, 30), (26, 10), (50, 2), (74, 10), (90, 30), (90, 62), (50, 60)]), c, 'f')]
C('alonzo-readdie', 'normal', P('#5ab8d8', '#f8dcc4', iris='#7a7a80'),
  F(eyes='big', mouth='grin', mouth_y=94, hairline=False),
  [L(blob([(14, 70), (14, 56), (24, 56), (22, 70)], 4), 'mid', 'b'), L(blob([(86, 70), (86, 56), (76, 56), (78, 70)], 4), 'mid', 'b')] + _beanie('front'),
  [L(blob([(40, 56), (56, 54), (58, 66), (44, 68)], 4), 'mid', 'b')] + _beanie('side'),
  _beanie('back'))

# Alphonse Wreckenbach: pelo castaño muy oscuro en casco con flequillo de mechones en punta; ojos castaños y sonrisa
C('alphonse-wreckenbach', 'normal', P('#3a2a20', '#e8b888', iris='#7a5020'),
  F(eyes='normal', mouth='smile', mouth_y=93, hairline=hl(6, 66, 50, 60, seed=12)),
  dome('front', top=0, w=48, cy=44, sb=70, seed=12),
  dome('side', top=0, w=48, cy=44, nape=86, fr=52, seed=12),
  dome('back', top=0, w=48, cy=44, nape=86, seed=12))

# Altair Aldrin: pelo azul turquesa claro ondulado y abultado con un gran mechón que le tapa un ojo; ojo verde con raya
C('altair-aldrin', 'normal', P('#80b8c0', '#f8dcc4', iris='#6a8a30'),
  F(eyes='sharp', mouth='line', mouth_y=94, hairline=[(8, 70), (20, 52), (40, 44), (60, 48), (80, 50), (92, 70)]),
  dome('front', top=-2, w=50, cy=44, n=7, amp=6, soft=True, sb=88, seed=13) +
  [fr([(22, 44), (40, 30), (58, 38), (60, 60), (54, 84), (46, 96, 1), (42, 74), (34, 60), (24, 56)])],
  dome('side', top=-2, w=50, cy=44, n=7, amp=6, soft=True, nape=90, fr=56, seed=13),
  dome('back', top=-2, w=50, cy=44, n=7, amp=6, soft=True, nape=90, seed=13))

# Alyra Verselle: pelo azul medio estirado hacia atrás con un moño de punta arriba y dos alas largas que caen por detrás de
# las orejas; cejas azules gruesas, ojos verdes con raya y boca seria
C('alyra-verselle', 'chica', P('#3a6aa8', '#f6d0b0', iris='#3a9a6a'),
  F(eyes='sharp', mouth='frown', mouth_y=94, hairline=[(14, 60), (26, 44), (50, 40), (74, 44), (86, 60)]),
  [L(outline([(18, 56), (20, 30), (36, 12), (50, 8), (64, 12), (80, 30), (82, 56), (50, 46)]), 'mid'),
   L(outline([(16, 50), (6, 80), (-6, 104, 1), (14, 88), (22, 66)]), 'mid', 'b'), L(outline([(84, 50), (94, 80), (106, 104, 1), (86, 88), (78, 66)]), 'mid', 'b'),
   L(outline([(42, 12), (36, -6), (44, -16, 1), (50, -4), (56, -16, 1), (64, -6), (58, 12)]), 'mid')] + thick_brows(63, 'shade', 3.4, 15, 0.4, 14),
  [L(outline([(54, 60), (40, 46), (24, 22), (40, 6), (66, 6), (86, 26), (88, 48), (70, 50)]), 'mid'), L(outline([(20, 40), (4, 70), (-6, 100, 1), (12, 84), (30, 56)]), 'mid'),
   L(outline([(40, 8), (42, -10, 1), (52, -2), (60, -12, 1), (60, 6)]), 'mid')],
  [L(outline([(16, 80), (14, 40), (30, 14), (50, 8), (70, 14), (86, 40), (84, 80), (50, 86)]), 'mid'),
   L(outline([(16, 50), (4, 80), (-6, 104, 1), (14, 88)]), 'mid'), L(outline([(84, 50), (96, 80), (106, 104, 1), (86, 88)]), 'mid'),
   L(outline([(42, 12), (36, -6), (44, -16, 1), (50, -4), (56, -16, 1), (64, -6), (58, 12)]), 'mid')])

# Amadeus Lyland: pelo rubio dorado peinado en una gran ola hacia un lado que le cubre la frente en diagonal; pecas
GOLD = '#e8a83a'
C('amadeus-lyland', 'normal', P(GOLD, '#f8dcc4', iris='#5a4a2a'),
  F(eyes='normal', mouth='smile', mouth_y=94, hairline=[(10, 64), (20, 44), (46, 38), (70, 50), (90, 60)]),
  [L(outline([(12, 66), (8, 40), (20, 16), (50, 2), (84, 12), (96, 34), (90, 60), (80, 52), (60, 52), (30, 46), (18, 50)]), 'mid'),
   L(outline([(60, 6), (88, 16), (96, 36), (88, 58), (70, 40)]), 'shade', 'b', False),
   mark([(30, 84), (31, 85)], 'shade', w=1.6), mark([(70, 84), (71, 85)], 'shade', w=1.6)],
  dome('side', top=2, w=48, cy=44, nape=84, fr=46, seed=14),
  dome('back', top=2, w=48, cy=44, nape=84, seed=14))

# Amita Rudd: piel morena clara, pelo rosa pálido recogido arriba en un moño en espiral con una bolita dorada y dos
# mechones que se enroscan hacia fuera junto a las orejas; cejas gruesas y boca pequeña seria
PK = '#f0c0d8'
C('amita-rudd', 'chica', P(PK, '#e8a878', iris='#3a2a1e'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=94, hairline=[(14, 60), (26, 44), (50, 40), (74, 44), (86, 60)]),
  [L(outline([(18, 56), (20, 30), (36, 12), (50, 8), (64, 12), (80, 30), (82, 56), (50, 46)]), 'mid'),
   L(outline([(40, 12), (34, -4), (46, -14), (60, -8), (58, 4), (48, 0), (52, 12)]), 'mid'), L(ell(50, 8, 3.4, 3.4), _c('#f0c040'), 'f'),
   R((16, 70), (2, 76), (6, 66), 5), R((84, 70), (98, 76), (94, 66), 5)] + thick_brows(64, 'mid', 4.0, 15, 0.8, 14),
  [L(outline([(54, 60), (40, 46), (24, 22), (40, 6), (66, 6), (86, 26), (88, 48), (70, 50)]), 'mid'),
   L(outline([(36, 8), (30, -8), (44, -14), (56, -6), (50, 6)]), 'mid')],
  [L(outline([(16, 80), (14, 40), (30, 14), (50, 8), (70, 14), (86, 40), (84, 80), (50, 86)]), 'mid'),
   L(outline([(40, 12), (34, -4), (46, -14), (60, -8), (58, 6)]), 'mid'), R((16, 70), (2, 76), (6, 66), 5), R((84, 70), (98, 76), (94, 66), 5)])

# Ana Santini: melena granate muy oscura con dos coletas altas grandes y onduladas que caen hasta el pecho, con gomas
# amarillas; flequillo recto y ojos verdes con raya
WINE = '#4a1e30'
C('ana-santini', 'chica', P(WINE, '#f8dcc4', iris='#3a9a8a'),
  F(eyes='sharp', mouth='smile', mouth_y=94, hairline=[(10, 62), (90, 62)]),
  bowl3('front', top=2, side=90, w=2, fringe=62) +
  [L(outline([(16, 20), (2, 12), (-14, 40), (-12, 80), (-4, 108, 1), (6, 80), (2, 50), (16, 34)]), 'mid', 'b'),
   L(outline([(84, 20), (98, 12), (114, 40), (112, 80), (104, 108, 1), (94, 80), (98, 50), (84, 34)]), 'mid', 'b'),
   L(blob([(14, 18), (20, 14), (22, 22), (16, 24)], 3), _c('#f0c040'), 'f'), L(blob([(86, 18), (80, 14), (78, 22), (84, 24)], 3), _c('#f0c040'), 'f')],
  bowl3('side', top=2, nape=94, w=2, fringe=62) + [L(outline([(30, 6), (10, 0), (-10, 40), (-8, 90, 1), (6, 60), (10, 30)]), 'mid')],
  bowl3('back', top=2, nape=94, w=2) + [L(outline([(16, 20), (2, 12), (-14, 40), (-12, 80), (-4, 108, 1), (6, 80), (2, 50), (16, 34)]), 'mid'),
                                        L(outline([(84, 20), (98, 12), (114, 40), (112, 80), (104, 108, 1), (94, 80), (98, 50), (84, 34)]), 'mid')])

# Annie Glenvale: piel morena, melena azul marino muy oscura con flequillo recto y una trenza larga a cada lado; ojos
# turquesa grandes y sonrisa de dientes
C('annie-glenvale', 'chica', P('#1a2a48', '#b88058', iris='#3aa8a8'),
  F(eyes='big', mouth='grin', mouth_y=94, hairline=[(10, 62), (90, 62)]),
  bowl3('front', top=2, side=90, w=4, fringe=62) + [R((14, 84), (8, 102), (12, 118), 11), R((86, 84), (92, 102), (88, 118), 11)],
  bowl3('side', top=2, nape=94, w=4, fringe=62) + [R((24, 88), (20, 104), (26, 120), 11)],
  bowl3('back', top=2, nape=94, w=4) + [R((20, 88), (16, 104), (20, 120), 11), R((80, 88), (84, 104), (80, 120), 11)])

# Aram Manton: melena lila grisácea larga y lisa hasta los hombros con mechones que caen sobre la frente en V; ojos
# azules afilados con raya y boca seria
C('aram-manton', 'delgado', P('#8a7aa0', '#f6d0b0', iris='#3a6ac8'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, hairline=[(10, 66), (24, 50), (40, 64), (50, 50), (60, 64), (76, 50), (90, 66)]),
  longhair('front', length=100, flare=12, top=0, fringe=64),
  longhair('side', length=100, flare=12, top=0),
  longhair('back', length=100, flare=12, top=0, ends=4))

# Arby Trayton (portero): piel morena, melena blanca crema lisa y muy larga con raya en medio; ojos verde menta redondos
C('arby-trayton', 'normal', P('#f2ecdc', '#a87050', iris='#40c8a0'),
  F(eyes='round', mouth='line', mouth_y=94, hairline=[(8, 66), (30, 44), (50, 40), (70, 44), (92, 66)]),
  longhair('front', length=118, flare=4, top=0, part=True),
  longhair('side', length=118, flare=4, top=0),
  longhair('back', length=118, flare=4, top=0, part=True, ends=4))

# Aretha Rumbell: pelo rojo vivo corto y alborotado en mechones de punta, con las patillas largas; ojos turquesa
C('aretha-rumbell', 'chica', P('#e84a3a', '#f8d8b8', iris='#2a9aa8'),
  F(eyes='big', brows='angry', mouth='frown', mouth_y=94, hairline=hl(6, 66, 50, 62, seed=15)),
  messy('front', amp=9, n=11, seed=15, lo=86),
  messy('side', amp=9, n=11, seed=15, lo=86, nape=92),
  messy('back', amp=9, n=11, seed=15, lo=86, nape=92))

# Argion Boneback: grandullón de piel oscura y cara ancha; pelo azul marino oscuro corto peinado hacia atrás con las
# patillas hacia fuera; cejas pobladas y boca apretada
C('argion-boneback', 'corpulento', P('#2a2a5a', '#8a5a3a', iris='#2a2a2a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, hairline=[(12, 62), (26, 46), (50, 42), (74, 46), (88, 62)],
    face_front=face(w=4, chin=104, jaw=4)),
  dome('front', top=4, w=46, cy=44, n=6, amp=6, sweep=0.4, sb=70, seed=16),
  dome('side', top=4, w=46, cy=44, n=6, amp=6, sweep=0.4, nape=82, fr=46, seed=16),
  dome('back', top=4, w=46, cy=44, n=6, amp=6, sweep=0.4, nape=82, seed=16))

# Aria Fondue: pelo rosa salmón corto y ondulado, abombado a los lados en rizos; ojos azules grandes y sonrisa alegre
C('aria-fondue', 'chica', P('#f0a890', '#f8dcc4', iris='#4a7ac8'),
  F(eyes='big', mouth='smile', mouth_y=94, hairline=[(10, 62), (26, 50), (40, 56), (50, 48), (60, 56), (74, 50), (90, 62)]),
  dome('front', top=0, w=48, cy=44, n=6, amp=5, soft=True, sb=84, seed=17) + [R((10, 80), (-6, 86), (4, 94), 6), R((90, 80), (106, 86), (96, 94), 6)],
  dome('side', top=0, w=48, cy=44, n=6, amp=5, soft=True, nape=88, fr=52, seed=17),
  dome('back', top=0, w=48, cy=44, n=6, amp=5, soft=True, nape=88, seed=17) + [R((10, 80), (-6, 86), (4, 94), 6), R((90, 80), (106, 86), (96, 94), 6)])

# Arin Fairey: pelo negro azulado con tupé alto hacia atrás y las puntas de los lados disparadas hacia fuera; ojos ámbar
C('arin-fairey', 'normal', P('#1e2234', '#f8dcc4', iris='#a87a3a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(12, 62), (26, 46), (42, 40), (50, 50), (58, 40), (74, 46), (88, 62)]),
  [L(outline([(14, 62), (12, 40), (24, 16), (50, -2), (76, 16), (88, 40), (86, 62), (50, 48)]), 'mid'),
   L(outline([(14, 50), (-6, 56, 1), (10, 62), (-2, 72, 1), (16, 70)]), 'mid'), L(outline([(86, 50), (106, 56, 1), (90, 62), (102, 72, 1), (84, 70)]), 'mid')],
  [L(outline([(52, 62), (40, 50), (20, 32), (24, 10), (52, -2), (80, 8), (90, 30), (86, 46), (66, 48)]), 'mid'), L(outline([(14, 50), (-8, 56, 1), (10, 64), (0, 74, 1), (20, 70)]), 'mid')],
  [L(outline([(14, 78), (12, 40), (24, 16), (50, -2), (76, 16), (88, 40), (86, 78), (50, 86)]), 'mid'),
   L(outline([(14, 50), (-6, 56, 1), (10, 62), (-2, 72, 1), (16, 70)]), 'mid'), L(outline([(86, 50), (106, 56, 1), (90, 62), (102, 72, 1), (84, 70)]), 'mid')])

# Armani Armure (portero): grandullón de piel oscura y cara cuadrada; pelo azul en casquete con dos picos como orejas de
# gato; cejas azules gruesas, ojos rojos, tirita en la mejilla y boca apretada
C('armani-armure', 'corpulento', P('#4a5aa8', '#7a4a30', iris='#c82a2a'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=98, hairline=[(12, 56), (88, 56)], face_front=face(w=8, chin=106, jaw=8)),
  [L(outline([(10, 58), (8, 30), (2, 6, 1), (28, 22), (50, 20), (72, 22), (98, 6, 1), (92, 30), (90, 58)]), 'mid')] +
  thick_brows(66, 'mid', 5.0, 15, 1.0, 16) + [mark([(30, 88), (40, 86), (40, 92), (30, 94)], TAPE)],
  [L(outline([(50, 56), (20, 50), (8, 30), (10, 8, 1), (40, 16), (76, 18), (88, 34), (86, 50)]), 'mid')],
  [L(outline([(10, 72), (8, 30), (2, 6, 1), (28, 22), (50, 20), (72, 22), (98, 6, 1), (92, 30), (90, 72), (50, 80)]), 'mid')])

# Ashe Connelly: piel morena, pelo fucsia abombado con horquillas de colores y las puntas rubias claras rizadas a los
# lados; ojos rosas grandes y marcas amarillas bajo los ojos
FUC, BLOND = '#e840a8', _c('#f8e898')
C('ashe-connelly', 'chica', P(FUC, '#b88058', iris='#e84aa8'),
  F(eyes='big', mouth='line', mouth_y=94, hairline=[(10, 62), (24, 50), (50, 46), (76, 50), (90, 62)]),
  dome('front', top=0, w=48, cy=44, sb=80, seed=18) +
  [L(blob([(2, 80), (14, 76), (18, 92), (6, 98)], 6), BLOND, 'f'), L(blob([(98, 80), (86, 76), (82, 92), (94, 98)], 6), BLOND, 'f'),
   mark([(56, 20), (70, 14)], _c('#80c040'), w=2.0), mark([(80, 34), (84, 46)], _c('#f08030'), w=2.0), mark([(16, 36), (20, 48)], _c('#40a8e8'), w=2.0),
   mark([(30, 84), (32, 86)], _c('#f0d040'), w=1.6), mark([(70, 84), (68, 86)], _c('#f0d040'), w=1.6)],
  dome('side', top=0, w=48, cy=44, nape=88, fr=52, seed=18) + [L(blob([(12, 82), (26, 80), (28, 94), (14, 98)], 6), BLOND, 'f')],
  dome('back', top=0, w=48, cy=44, nape=88, seed=18) + [L(blob([(2, 80), (14, 76), (18, 92), (6, 98)], 6), BLOND, 'f'),
                                                         L(blob([(98, 80), (86, 76), (82, 92), (94, 98)], 6), BLOND, 'f')])

# Aubrey McCoy: pelo granate muy oscuro recogido en un moño alto, con dos mechones finos y largos que caen por delante de
# las orejas hasta el pecho; gafas negras grandes casi cuadradas y ojos rojos
C('aubrey-mccoy', 'chica', P('#3a1e2a', '#f8dcc4', iris='#c83a2a'),
  F(eyes='big', mouth='frown', mouth_y=94, hairline=[(12, 62), (26, 50), (40, 56), (50, 48), (60, 56), (74, 50), (88, 62)]),
  dome('front', top=4, w=44, cy=44, sb=62, seed=19) + [bun(50, -4, 12, z='b'), side_lock(18, 60, 120, wd=4), side_lock(82, 60, 120, wd=4)] +
  [L(blob([(22, 68), (46, 68), (46, 84), (24, 84)], 4) + [(22, 68)], BLACK, 'f', False, False, 2.4),
   L(blob([(78, 68), (54, 68), (54, 84), (76, 84)], 4) + [(78, 68)], BLACK, 'f', False, False, 2.4), L([(46, 72), (54, 72)], BLACK, 'f', False, False, 2.0)],
  dome('side', top=4, w=44, cy=44, nape=84, fr=52, seed=19) + [bun(36, -2, 12)] + specs('side'),
  dome('back', top=4, w=44, cy=44, nape=84, seed=19) + [bun(50, -4, 12)])

# Audreen Slumberey: pelo turquesa en forma de seta gigante, una campana que le cae hasta la barbilla con flequillo recto
# sobre los ojos lilas entornados; boca pequeña
C('audreen-slumberey', 'chica', P('#40a8b0', '#f8dcc4', iris='#9a7ac8'),
  F(eyes='sharp', mouth='line', mouth_y=94, hairline=[(8, 68), (92, 68)]),
  [L(outline([(-8, 92), (-10, 60), (4, 26), (30, 6), (50, 2), (70, 6), (96, 26), (110, 60), (108, 92), (86, 96), (82, 68), (18, 68), (14, 96)]), 'mid'),
   L(outline([(62, 6), (94, 26), (106, 60), (104, 90), (90, 92), (86, 60)]), 'shade', 'b', False)],
  [L(outline([(70, 70), (84, 66), (86, 40), (70, 10), (40, 2), (10, 18), (-10, 50), (-10, 90), (20, 98), (56, 96), (60, 80)]), 'mid')],
  [L(outline([(-8, 92), (-10, 60), (4, 26), (30, 6), (50, 2), (70, 6), (96, 26), (110, 60), (108, 92), (50, 100)]), 'mid')])

# Aura Tempesta: pelo naranja vivo en una nube de rizos abombada con dos coletitas rizadas bajo las orejas; pecas y ojos
# castaños rojizos
C('aura-tempesta', 'chica', P('#f08040', '#f8dcc4', iris='#7a3a2a'),
  F(eyes='big', brows='angry', mouth='frown', mouth_y=94, hairline=[(12, 62), (24, 50), (40, 56), (50, 48), (60, 56), (76, 50), (88, 62)]),
  dome('front', top=-6, w=52, cy=40, n=10, amp=7, soft=True, sb=72, seed=20) + [R((16, 90), (6, 98), (12, 104), 7), R((84, 90), (94, 98), (88, 104), 7),
                                                                                  mark([(30, 84), (31, 85)], 'shade', w=1.4), mark([(70, 84), (69, 85)], 'shade', w=1.4)],
  dome('side', top=-6, w=52, cy=40, n=10, amp=7, soft=True, nape=88, fr=52, seed=20) + [R((30, 90), (22, 98), (28, 104), 7)],
  dome('back', top=-6, w=52, cy=40, n=10, amp=7, soft=True, nape=88, seed=20) + [R((16, 90), (6, 98), (12, 104), 7), R((84, 90), (94, 98), (88, 104), 7)])

# Ava Ehrenreich: pelo rubio muy claro con dos moños redondos a los lados de la coronilla con una flor blanca cada uno y la
# melena hasta la mandíbula; cejas tristes, ojos verdes llorosos y boca temblorosa
CREAM = '#efe0b0'
FLOWER = _c('#ffffff')
C('ava-ehrenreich', 'chica', P(CREAM, '#f8dcc4', iris='#3a8a6a'),
  F(eyes='big', brows=True, mouth='frown', mouth_y=94, hairline=[(10, 66), (24, 48), (50, 42), (76, 48), (90, 66)]),
  dome('front', top=4, w=46, cy=46, long=94, flare=2, seed=21) + [bun(14, 20, 13), bun(86, 20, 13),
                                                                   L(ell(22, 12, 4, 4), FLOWER, 'f'), L(ell(78, 12, 4, 4), FLOWER, 'f')],
  dome('side', top=4, w=46, cy=46, long=94, flare=2, fr=52, seed=21) + [bun(34, 8, 13)],
  dome('back', top=4, w=46, cy=46, long=94, flare=2, seed=21) + [bun(14, 20, 13, z='f'), bun(86, 20, 13, z='f')])

# Avan Floane: pelo violeta peinado en dos alas hacia arriba a los lados de la cabeza y un mechón largo que le cae en
# diagonal sobre la cara; ojos azules y boca seria
VIO = '#9a5ac8'
C('avan-floane', 'normal', P(VIO, '#f8dcc4', iris='#3a8ac8'),
  F(eyes='big', mouth='frown', mouth_y=96, hairline=[(14, 62), (26, 44), (50, 40), (74, 44), (86, 62)]),
  [L(outline([(16, 60), (14, 40), (4, 14, 1), (26, 22), (40, 10), (60, 10), (74, 22), (96, 14, 1), (86, 40), (84, 60), (50, 46)]), 'mid'),
   fr([(54, 24), (66, 30), (64, 60), (60, 84, 1), (54, 60), (48, 40)])],
  [L(outline([(52, 60), (40, 48), (24, 30), (10, 8, 1), (40, 12), (70, 8), (94, 0, 1), (86, 30), (86, 46), (66, 48)]), 'mid')],
  [L(outline([(16, 80), (14, 40), (4, 14, 1), (26, 22), (40, 10), (60, 10), (74, 22), (96, 14, 1), (86, 40), (84, 80), (50, 86)]), 'mid')])

# Avatar: el jugador sin cara definida (no tiene retrato); pelo castaño corto de protagonista y gesto decidido
C('avatar', 'normal', P('#6a4a2a', '#f8dcc4', iris='#5a3a1e'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=93, hairline=hl(5, 64, 50, 58, seed=22)),
  dome('front', top=2, w=47, cy=44, n=8, amp=7, sb=70, seed=22),
  dome('side', top=2, w=47, cy=44, n=8, amp=7, nape=86, fr=52, seed=22),
  dome('back', top=2, w=47, cy=44, n=8, amp=7, nape=86, seed=22))

# Ayla Bordaire: melena azul petróleo hasta los hombros con flequillo de mechones y horquillas grises; un visor grande gris
# con cristal amarillo de rejilla tapándole los ojos
VIS, VISG = _c('#8a8a90'), _c('#c8b04a')
C('ayla-bordaire', 'chica', P('#1e5a80', '#f8dcc4', iris='#3a3a3a'),
  F(eyes='none', mouth='line', mouth_y=94, hairline=[(8, 66), (22, 50), (36, 60), (50, 48), (64, 60), (78, 50), (92, 66)]),
  longhair('front', length=100, flare=6, top=0, fringe=62) +
  [L(blob([(10, 70), (50, 66), (90, 70), (88, 84), (50, 82), (12, 84)], 6), VIS, 'f'), L(blob([(18, 72), (50, 69), (82, 72), (80, 81), (50, 79), (20, 81)], 6), VISG, 'f'),
   L([(34, 70), (34, 80)], VIS, 'f', False, False, 1.0), L([(50, 69), (50, 79)], VIS, 'f', False, False, 1.0), L([(66, 70), (66, 80)], VIS, 'f', False, False, 1.0)],
  longhair('side', length=100, flare=6, top=0) + [L(blob([(54, 70), (90, 68), (90, 84), (56, 82)], 4), VIS, 'f'), L(blob([(70, 71), (88, 70), (88, 81), (72, 80)], 4), VISG, 'f')],
  longhair('back', length=100, flare=6, top=0, ends=4) + [L(blob([(8, 70), (92, 70), (92, 76), (8, 76)], 3), VIS, 'f')])

# Ayle Holland: pelo castaño rojizo en casquete corto con raya y flequillo de mechones finos; ojos verde oliva, rubor y
# sonrisa tranquila (es el mismo del modelo 3D)
C('ayle-holland', 'normal', P('#9a5c5a', '#f8d8b8', iris='#6a6a2a'),
  F(eyes='big', mouth='smile', mouth_y=93, hairline=[(10, 66), (22, 50), (34, 58), (46, 48), (58, 58), (70, 50), (80, 58), (90, 66)]),
  dome('front', top=2, w=48, cy=44, n=9, amp=5, soft=True, sb=80, seed=23) + blush(86, 20, 4.6, _c('#f0a080')),
  dome('side', top=2, w=48, cy=44, n=9, amp=5, soft=True, nape=88, fr=54, seed=23),
  dome('back', top=2, w=48, cy=44, n=9, amp=5, soft=True, nape=88, seed=23))

# Aylin Terpheis: media melena gris azulado con las puntas hacia fuera y un flequillo largo que le tapa un ojo; ojo violeta
# con sombra verde y boca triste
C('aylin-terpheis', 'chica', P('#6a8aa0', '#f8dcc4', iris='#7a5aa8'),
  F(eyes='sharp', mouth='frown', mouth_y=94, hairline=[(8, 70), (20, 50), (40, 44), (60, 48), (80, 50), (92, 70)]),
  dome('front', top=2, w=46, cy=44, sb=84, seed=24) + [fr([(20, 46), (40, 34), (56, 44), (52, 70), (40, 86, 1), (32, 66), (22, 60)]),
                                                     fr([(10, 80), (0, 94, 1), (14, 90)]), fr([(90, 80), (100, 94, 1), (86, 90)])],
  dome('side', top=2, w=46, cy=44, nape=88, fr=56, seed=24),
  dome('back', top=2, w=46, cy=44, nape=88, seed=24) + [fr([(10, 80), (0, 94, 1), (14, 90)]), fr([(90, 80), (100, 94, 1), (86, 90)])])

# Azam Darjeel (portero): calvo de piel morena clara con tres puntos rojizos en la frente; cejas negras enormes en bloque,
# ojos verdes y boca seria
C('azam-darjeel', 'corpulento', P('#2a2422', '#d89a7a', iris='#5aa83a'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=96, hairline=False, face_front=face(w=2, chin=104, jaw=2)),
  skull3('front') + thick_brows(66, BLACK, 6.0, 15, 1.0, 18) +
  [L(ell(50, 46, 2.2, 2.2), _c('#b85a4a'), 'f', False), L(ell(45, 52, 2.2, 2.2), _c('#b85a4a'), 'f', False), L(ell(55, 52, 2.2, 2.2), _c('#b85a4a'), 'f', False)],
  skull3('side') + side_brow(66, BLACK, 6.0, 1.0),
  skull3('back'))

# Azure Marcet: melena azul intenso hasta la mandíbula con un mechón largo que le cae por el centro de la cara; ojos azules
C('azure-marcet', 'normal', P('#1e3a98', '#f8dcc4', iris='#4a7ac8'),
  F(eyes='sharp', mouth='frown', mouth_y=95, hairline=[(8, 68), (20, 50), (40, 44), (60, 44), (80, 50), (92, 68)]),
  bowl3('front', top=-2, side=96, w=4, fringe=52) + [fr([(40, 46), (52, 44), (56, 70), (50, 94, 1), (46, 70)])],
  bowl3('side', top=-2, nape=98, w=4, fringe=54),
  bowl3('back', top=-2, nape=98, w=4))

# Ballmer Netting: cara muy redonda de mofletes rosados; pelo azul grisáceo en casquete redondo con mechones redondeados
# verde agua sobre la frente; ojos pequeños dorados
MINT = _c('#a0d8c8')
C('ballmer-netting', 'corpulento', P('#4a7a8a', '#f8dcc4', iris='#8a7a2a'),
  F(eyes='round', mouth='smile', mouth_y=96, hairline=[(8, 62), (92, 62)], face_front=face(w=10, chin=104, jaw=8, top=30)),
  bowl3('front', top=8, side=80, w=10, fringe=58) + [L(blob([(18, 58), (28, 50), (36, 62), (24, 70)], 6), MINT, 'f'),
                                                   L(blob([(82, 58), (72, 50), (64, 62), (76, 70)], 6), MINT, 'f'),
                                                   L(blob([(40, 54), (48, 50), (52, 60), (42, 64)], 6), MINT, 'f')] + blush(88, 28, 5.6),
  bowl3('side', top=8, nape=90, w=10, fringe=58),
  bowl3('back', top=8, nape=90, w=10))

# Bam Buschutt: piel morena; pelo castaño oscuro en pinchos enormes disparados hacia arriba y los lados; ojos azules grandes
# y una tirita en la nariz
C('bam-buschutt', 'bajito', P('#3a2418', '#c89068', iris='#3a7ac8'),
  F(eyes='big', mouth='smile', mouth_y=94, hairline=hl(5, 66, 50, 62, seed=25)),
  messy('front', amp=22, n=9, seed=25, lo=72, sweep=0.2) + [mark([(44, 84), (56, 84), (56, 89), (44, 89)], TAPE)],
  messy('side', amp=22, n=9, seed=25, lo=72, nape=88),
  messy('back', amp=22, n=9, seed=25, lo=72, nape=88))

# Bang Revell: pelo verde oliva corto con un mechón rizado en antena y dos cuernos negros de pelo a los lados; cejas
# oliva gruesas y sonrisa de dientes
C('bang-revell', 'normal', P('#7a8040', '#f8d8b0', iris='#3a3a5a'),
  F(eyes='big', brows=False, mouth='grin', mouth_y=95, hairline=[(14, 62), (26, 48), (50, 44), (74, 48), (86, 62)]),
  dome('front', top=6, w=44, cy=46, sb=66, seed=26) + [L(outline([(16, 34), (12, 8, 1), (26, 22), (30, 38)]), BLACK, 'f'), L(outline([(84, 34), (88, 8, 1), (74, 22), (70, 38)]), BLACK, 'f'),
                                                     R((50, 10), (40, -8), (54, -14), 4)] + thick_brows(64, 'mid', 4.0, 15, 0.4, 14),
  dome('side', top=6, w=44, cy=46, nape=84, fr=50, seed=26) + [L(outline([(54, 20), (60, -4, 1), (70, 18)]), BLACK, 'f'), R((44, 8), (34, -10), (48, -16), 4)],
  dome('back', top=6, w=44, cy=46, nape=84, seed=26) + [L(outline([(16, 34), (12, 8, 1), (26, 22), (30, 38)]), BLACK, 'f'), L(outline([(84, 34), (88, 8, 1), (74, 22), (70, 38)]), BLACK, 'f')])

# Banner Weaving: señor mayor de pelo gris peinado hacia atrás con canas blancas arriba; cejas en arco, ojos caídos,
# pecas y sonrisa de lado
C('banner-weaving', 'normal', P('#7a7a7e', '#f8d8b8', iris='#3a3a3a', light='#d8d8d8'),
  F(eyes='closed', brows=True, mouth='smile', mouth_y=95, hairline=[(14, 62), (28, 46), (50, 42), (72, 46), (86, 62)]),
  dome('front', top=2, w=46, cy=44, sb=72, seed=27) + [L(outline([(26, 30), (40, 12), (60, 12), (74, 30), (60, 24), (40, 24)]), 'light', 'f'),
                                                     mark([(30, 86), (31, 87)], 'shade', w=1.4), mark([(70, 86), (69, 87)], 'shade', w=1.4)],
  dome('side', top=2, w=46, cy=44, nape=84, fr=46, seed=27) + [L(outline([(40, 6), (70, 10), (80, 24), (60, 18)]), 'light', 'f')],
  dome('back', top=2, w=46, cy=44, nape=84, seed=27))

# Barcley Dover: pelo blanco plateado liso con raya en medio y mechones largos que caen por delante de las orejas; ojos
# naranjas redondos
C('barcley-dover', 'normal', P('#d8d8e4', '#f8dcc4', iris='#e87a2a'),
  F(eyes='round', mouth='line', mouth_y=94, hairline=[(8, 70), (24, 54), (40, 50), (50, 40), (60, 50), (76, 54), (92, 70)]),
  bowl3('front', top=0, side=96, w=4, fringe=50) + [side_lock(20, 50, 100, wd=10), side_lock(80, 50, 100, wd=10), strand([(50, 4), (50, 36)], 'shade', 'f', 1.0)],
  bowl3('side', top=0, nape=96, w=4, fringe=52),
  bowl3('back', top=0, nape=96, w=4))

# Barley Coldholt: afro castaño muy oscuro enorme y redondo sobre la frente despejada; cejas como dos puntos y mofletes
C('barley-coldholt', 'normal', P('#3a3028', '#f8d8b8', iris='#6a6a5a'),
  F(eyes='closed', brows=False, mouth='smile', mouth_y=94, hairline=[(16, 60), (30, 46), (50, 44), (70, 46), (84, 60)]),
  dome('front', top=-14, w=54, cy=34, n=11, amp=7, soft=True, sb=60, seed=28) + [L(ell(36, 62, 3.6, 3.6), 'deep', 'f'), L(ell(64, 62, 3.6, 3.6), 'deep', 'f')] + blush(88, 26),
  dome('side', top=-14, w=54, cy=34, n=11, amp=7, soft=True, nape=74, fr=46, seed=28),
  dome('back', top=-14, w=54, cy=34, n=11, amp=7, soft=True, nape=74, seed=28))

# Barnaby Livergain: piel morena; pelo azul celeste claro peinado hacia atrás con una diadema negra, y mechones largos que
# caen por detrás de las orejas hasta el pecho; cejas celestes pobladas y perilla celeste
ICE = '#a8c8f0'
C('barnaby-livergain', 'delgado', P(ICE, '#b8805a', iris='#5a8ac8'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=96, hairline=[(14, 60), (26, 44), (50, 40), (74, 44), (86, 60)]),
  dome('front', top=2, w=46, cy=44, long=112, flare=4, seed=29) + [L(quad((14, 40), (50, 12), (86, 40)), BLACK, 'f', False, False, 2.2)] +
  thick_brows(64, 'mid', 4.4, 15, 1.0, 15) + [mark([(44, 102), (50, 106), (56, 102), (50, 98)], 'mid')],
  dome('side', top=2, w=46, cy=44, long=112, flare=4, fr=48, seed=29) + [L(quad((70, 40), (46, 6), (20, 30)), BLACK, 'f', False, False, 2.2)],
  dome('back', top=2, w=46, cy=44, long=112, flare=4, seed=29))

# Barrac Kuda (portero): pelo verde azulado en un tupé enorme que se enrolla hacia arriba y atrás como una ola; cejas
# gruesas verde azulado, ojos azules con pestañas y boca seria
C('barrac-kuda', 'delgado', P('#2a9a90', '#f8e4d0', iris='#3a8ac8'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=96, hairline=[(14, 60), (26, 46), (50, 40), (74, 46), (86, 60)]),
  [L(outline([(16, 62), (12, 36), (20, 16), (40, 6), (70, 0), (96, -14, 1), (88, 8), (86, 36), (84, 62), (50, 46)]), 'mid'),
   L(outline([(56, 4), (90, -8), (86, 30), (80, 52), (66, 24)]), 'shade', 'b', False)] + thick_brows(63, 'mid', 4.4, 15, 1.0, 15),
  [L(outline([(54, 62), (40, 50), (16, 36), (16, 12), (44, 0), (80, -12), (100, -20, 1), (92, 14), (86, 42), (68, 48)]), 'mid')],
  [L(outline([(16, 80), (12, 36), (22, 12), (50, 2), (80, -6), (96, -14, 1), (88, 36), (84, 80), (50, 86)]), 'mid')])

# Barrett Mistbarrow: grandullón de piel morena y cara ancha; pelo negro liso pegado y largo por detrás de las orejas;
# gafas finas de montura roja, cejas fruncidas y boca recta
C('barrett-mistbarrow', 'corpulento', P('#1e1a1a', '#9a6a44', iris='#2a2a2a'),
  F(eyes='round', brows='angry', mouth='line', mouth_y=98, hairline=[(12, 62), (28, 48), (50, 44), (72, 48), (88, 62)], face_front=face(w=8, chin=104, jaw=8)),
  dome('front', top=6, w=48, cy=46, long=100, flare=0, seed=30) + round_specs('front', _c('#c84a4a'), 76, 15, 8.5, 6.5, 1.6),
  dome('side', top=6, w=48, cy=46, long=100, flare=0, fr=48, seed=30) + round_specs('side', _c('#c84a4a'), 76, 15, 8.5, 6.5, 1.6),
  dome('back', top=6, w=48, cy=46, long=100, flare=0, seed=30))

# Bartholomew Blitzer: grandullón de cara redonda rosada; pelo negro corto de pinchos rectos arriba con los lados rapados
# grises; ojos redondos, tirita en la nariz y mofletes
C('bartholomew-blitzer', 'corpulento', P('#1e1a1e', '#f0b090', iris='#c83a2a', low='#8a8a8a'),
  F(eyes='round', brows=True, mouth='line', mouth_y=96, hairline=[(14, 56), (30, 44), (50, 42), (70, 44), (86, 56)], face_front=face(w=10, chin=104, jaw=8)),
  [L(blob([(10, 66), (12, 40), (88, 40), (90, 66), (80, 56), (20, 56)], 6), 'low')] +
  dome('front', top=4, w=40, cy=36, n=9, amp=5, sb=44, seed=31, shade=False) + [mark([(44, 84), (56, 84), (56, 89), (44, 89)], TAPE)] + blush(90, 28, 5.6),
  [L(blob([(6, 66), (10, 36), (56, 40), (56, 66)], 6), 'low')] + dome('side', top=4, w=40, cy=36, n=9, amp=5, nape=50, fr=40, seed=31, shade=False),
  [L(blob([(8, 76), (10, 40), (90, 40), (92, 76), (50, 84)], 6), 'low')] + dome('back', top=4, w=40, cy=36, n=9, amp=5, nape=50, seed=31, shade=False))

# Bastian Brineford: piel morena; pelo verde grisáceo claro recogido en una coleta altísima y ondulada con una goma roja,
# y mechones que caen por la frente; cejas finas y sonrisa de lado
SAGE = '#b8c098'
C('bastian-brineford', 'normal', P(SAGE, '#b8805a', iris='#3a8a8a'),
  F(eyes='sharp', mouth='smile', mouth_y=96, hairline=[(14, 62), (26, 46), (40, 52), (50, 42), (60, 52), (74, 46), (86, 62)]),
  dome('front', top=4, w=46, cy=46, sb=68, seed=32) +
  [L(outline([(44, 10), (36, -12), (20, -24), (34, -30), (56, -24), (60, -6), (56, 10)]), 'mid', 'b'), L(blob([(42, 2), (52, -4), (56, 4), (46, 8)], 4), _c('#e85a3a'), 'f')],
  dome('side', top=4, w=46, cy=46, nape=86, fr=50, seed=32) + [L(outline([(30, 8), (14, -6), (-8, 20), (-10, 60, 1), (4, 36), (20, 22)]), 'mid'),
                                                             L(blob([(24, 2), (32, -4), (36, 6), (28, 10)], 4), _c('#e85a3a'), 'f')],
  dome('back', top=4, w=46, cy=46, nape=86, seed=32) + [L(outline([(44, 10), (36, -12), (40, -28), (60, -24), (60, 10)]), 'mid'),
                                                         L(outline([(44, 10), (38, 50), (48, 80, 1), (60, 40), (58, 10)]), 'mid')])

# Batton Farrow: piel morena; afro gris pizarra corto y redondo; cejas grises pobladas, ojos entornados y boca apretada
C('batton-farrow', 'corpulento', P('#5a6068', '#9a6a44', iris='#2a2a2a'),
  F(eyes='closed', brows=False, mouth='frown', mouth_y=96, hairline=[(14, 60), (30, 48), (50, 46), (70, 48), (86, 60)], face_front=face(w=6, chin=102, jaw=6)),
  dome('front', top=-2, w=48, cy=40, n=11, amp=6, soft=True, sb=64, seed=33) + thick_brows(66, 'mid', 5.0, 15, 0.6, 16),
  dome('side', top=-2, w=48, cy=40, n=11, amp=6, soft=True, nape=80, fr=48, seed=33),
  dome('back', top=-2, w=48, cy=40, n=11, amp=6, soft=True, nape=80, seed=33))

# Beatrice Estiletto: melena azul acero con flequillo de mechones largos y dos trenzas gruesas que caen hasta el pecho con
# las puntas atadas; ojos rojizos entornados y sonrisa
STEEL = '#2a6a98'
C('beatrice-estiletto', 'chica', P(STEEL, '#f8dcc4', iris='#c84a3a'),
  F(eyes='sharp', mouth='smile', mouth_y=94, hairline=[(8, 66), (22, 52), (36, 62), (50, 50), (64, 62), (78, 52), (92, 66)]),
  dome('front', top=0, w=48, cy=44, sb=86, seed=34) + [R((14, 84), (2, 102), (14, 120), 12), R((86, 84), (98, 102), (86, 120), 12)],
  dome('side', top=0, w=48, cy=44, nape=88, fr=56, seed=34) + [R((28, 86), (18, 104), (30, 120), 12)],
  dome('back', top=0, w=48, cy=44, nape=88, seed=34) + [R((20, 84), (8, 102), (18, 120), 12), R((80, 84), (92, 102), (82, 120), 12)])

# Bechet Ardevout: pelo gris corto con un gorro de lana blanca enroscada como un turbante esponjoso encima; patillas
# grises, cejas fruncidas, ojos de lado y boca recta
WOOL = _c('#f2eee6')
C('bechet-ardevout', 'normal', P('#8a8a90', '#f8d8b8', iris='#5a5a6a'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=96, hairline=[(14, 60), (86, 60)]),
  [L(blob([(14, 80), (14, 50), (86, 50), (86, 80), (80, 66), (20, 66)], 6), 'mid'), L(outline([(26, 30), (36, 8), (50, -2, 1), (64, 8), (74, 30)]), 'mid'),
   L(blob([(8, 50), (6, 38), (20, 28), (50, 24), (80, 28), (94, 38), (92, 50), (70, 52), (50, 50), (30, 52)], 6), WOOL, 'f')],
  [L(blob([(8, 50), (54, 50), (54, 80), (14, 84)], 6), 'mid'), L(outline([(20, 30), (40, 4), (56, -2, 1), (70, 10), (80, 30)]), 'mid'),
   L(blob([(2, 50), (4, 34), (50, 24), (90, 32), (90, 48), (50, 52)], 6), WOOL, 'f')],
  [L(blob([(14, 82), (14, 50), (86, 50), (86, 82), (50, 88)], 6), 'mid'), L(outline([(26, 30), (36, 8), (50, -2, 1), (64, 8), (74, 30)]), 'mid'),
   L(blob([(8, 50), (6, 38), (20, 28), (50, 24), (80, 28), (94, 38), (92, 50), (50, 54)], 6), WOOL, 'f')])

# Bellie Jerant: gorro de lana negro alto con una franja blanca; melena verde azulado larga y ondulada por los lados;
# ojos turquesa con pestañas marcadas
TEAL = '#1e8a80'
def _tallcap(view):
    if view == 'front':
        return [L(outline([(10, 56), (10, 26), (22, 4), (50, -8), (78, 4), (90, 26), (90, 56), (50, 52)]), BLACK, 'f'),
                L(blob([(10, 40), (50, 36), (90, 40), (90, 44), (50, 40), (10, 44)], 4), WHITE, 'f')]
    if view == 'side':
        return [L(outline([(4, 56), (4, 24), (22, 0), (50, -8), (80, 2), (90, 24), (88, 52), (50, 54)]), BLACK, 'f'),
                L(blob([(4, 40), (89, 38), (89, 42), (4, 44)], 4), WHITE, 'f')]
    return _tallcap('front')
C('bellie-jerant', 'chica', P(TEAL, '#f8dcc4', iris='#2a9a9a'),
  F(eyes='big', mouth='line', mouth_y=94, hairline=[(14, 64), (30, 56), (50, 54), (70, 56), (86, 64)]),
  longhair('front', length=114, flare=8, top=10) + _tallcap('front'),
  longhair('side', length=114, flare=8, top=10) + _tallcap('side'),
  longhair('back', length=114, flare=8, top=10, ends=4) + _tallcap('back'))

# Belton McGirdle: pelo castaño claro alborotado en un tupé con ondas y un mechón grande que cae por la frente; ojos ámbar
# y sonrisa amplia
C('belton-mcgirdle', 'normal', P('#c08a50', '#f8dcc4', iris='#c8a020'),
  F(eyes='sharp', mouth='smile', mouth_y=95, hairline=[(14, 62), (26, 46), (50, 40), (64, 52), (78, 46), (86, 62)]),
  dome('front', top=-6, w=48, cy=40, n=8, amp=7, soft=True, sb=66, seed=35) + [fr([(56, 34), (70, 38), (72, 54), (64, 64, 1), (60, 48)])],
  dome('side', top=-6, w=48, cy=40, n=8, amp=7, soft=True, nape=84, fr=48, seed=35),
  dome('back', top=-6, w=48, cy=40, n=8, amp=7, soft=True, nape=84, seed=35))

# Benoni Espinoza: piel morena; rastas negras verdosas cortas que caen alrededor de la cabeza con un mechón en antena
# arriba; cejas gruesas, ojos dorados y sonrisa de dientes
C('benoni-espinoza', 'normal', P('#1e2a24', '#8a5a3a', iris='#c8a020'),
  F(eyes='sharp', brows=False, mouth='grin', mouth_y=95, hairline=[(14, 62), (28, 46), (50, 42), (72, 46), (86, 62)]),
  dome('front', top=2, w=46, cy=44, sb=60, seed=36) + [R((50, 6), (44, -8), (54, -16), 4)] +
  [R((12 + i * 8, 54), (10 + i * 8, 72), (12 + i * 8, 88), 6) for i in range(2)] + [R((80 + i * 8, 54), (82 + i * 8, 72), (80 + i * 8, 88), 6) for i in range(2)] +
  thick_brows(64, BLACK, 4.0, 15, 1.0, 14),
  dome('side', top=2, w=46, cy=44, nape=84, fr=50, seed=36) + [R((10 + i * 10, 50), (8 + i * 10, 72), (12 + i * 10, 92), 6) for i in range(4)],
  dome('back', top=2, w=46, cy=44, nape=84, seed=36) + [R((12 + i * 12, 50), (10 + i * 12, 74), (12 + i * 12, 94), 6) for i in range(7)])

# Berlinda Glitz: piel morena; melena gris perla lisa hasta la mandíbula con raya a un lado y un flequillo largo que le
# tapa media cara; ojos turquesa afilados y labios rosados
C('berlinda-glitz', 'chica', P('#c8c8bc', '#8a5a3a', iris='#2a8a9a'),
  F(eyes='sharp', brows='angry', mouth='lips', mouth_y=96, mouth_w=5, hairline=[(8, 70), (20, 50), (40, 44), (60, 46), (80, 52), (92, 70)]),
  bowl3('front', top=0, side=100, w=4, fringe=54) + [fr([(46, 40), (60, 36), (80, 46), (88, 70), (80, 96, 1), (70, 70), (62, 56)])],
  bowl3('side', top=0, nape=100, w=4, fringe=56),
  bowl3('back', top=0, nape=100, w=4))
