"""Ojeadores de IE2 (scouts-ie2), tanda 06: dibujados a partir de su retrato de Victory Road; claves 'scouts-ie2:<id>'.

Casi ninguno tiene modelo 3D: el frente sale del retrato y el perfil y la espalda se deducen de cómo cae ese peinado.
Se reutilizan las ayudas de los ojeadores de IE1 (dome/hl/face de la tanda 09, skull/bowl/gafas de la 03)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars import longhair, messy  # noqa: F401
from chars_scouts_ie1_03 import blush, bowl, freckles, rect_specs, round_specs, side_brow, skull, thick_brows  # noqa: F401
from chars_scouts_ie1_09 import _c, dome, face, face_side, hl, mark  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (28, 22, 24, 255)
PINK = (238, 140, 140, 255)


def F(**k):
    d = {'eyes': 'normal', 'mouth': 'line'}
    d.update(k)
    return d


def P(hair, skin, iris='#302232', **k):
    return pal(hair, skin, iris, **k)


def C(pid, body, palette, f, front, side, back):
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        # el nacimiento del pelo baja por el borde de la cara hasta la barbilla: así su raya no cruza el pelo de los lados
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[f'scouts-ie2:{pid}'] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def fr(pts, c='mid'):
    """Mechón por delante de la cara."""
    return L(outline(pts), c, 'f')


def tail(view, c='mid', side_len=118, x=50, low=78, w=10):
    """Coleta o melena recogida que cae por detrás (se ve de espaldas y de perfil)."""
    if view == 'back':
        return [L(outline([(x - w, low), (x - w - 2, side_len - 12), (x, side_len, 1), (x + w + 2, side_len - 12), (x + w, low)]), c)]
    if view == 'side':
        return [L(outline([(16, low - 10), (4, side_len - 16), (10, side_len, 1), (22, side_len - 18), (28, low - 6)]), c)]
    return []


def ties(view, c, y=96, x0=22, x1=78):
    """Gomas de dos coletas bajas."""
    if view == 'front':
        return [L(ell(x0, y, 4, 3), c, 'f'), L(ell(x1, y, 4, 3), c, 'f')]
    if view == 'side':
        return [L(ell(20, y, 4, 3), c, 'f')]
    return [L(ell(x0, y, 4, 3), c, 'f'), L(ell(x1, y, 4, 3), c, 'f')]


def earrings(c, y=86, side=False):
    if side:
        return [L(ell(46, y, 2.2, 2.2), c, 'f')]
    return [L(ell(15, y, 2.2, 2.2), c, 'f'), L(ell(85, y, 2.2, 2.2), c, 'f')]


# ------------------------------------------------------------------ jugadores

# Payne Green-D-Outler: casco negro con un visor de gafas verdes en forma de ojos, cuernos grises a los lados, cresta de
# pelo verde en pinchos asomando por arriba y un pañuelo negro atado detrás; aprieta los dientes
GR, GL, GY = _c('#3a8a2a'), _c('#7ad040'), _c('#7a7876')
HM = _c('#141414')


def _payne(view):
    if view == 'front':
        return [L(outline([(16, 20), (24, -8, 1), (32, 8), (40, -14, 1), (50, 2), (60, -14, 1), (68, 8), (76, -8, 1), (84, 20)]), GR, 'b'),
                L(outline([(8, 88), (4, 54), (10, 26), (30, 10), (50, 6), (70, 10), (90, 26), (96, 54), (92, 88), (80, 84), (70, 88), (60, 86), (50, 88),
                           (40, 86), (30, 88), (20, 84)]), HM, 'f'),
                L(outline([(2, 60), (-4, 30, 1), (12, 22), (14, 70)]), GY, 'f'), L(outline([(98, 60), (104, 30, 1), (88, 22), (86, 70)]), GY, 'f'),
                L(blob([(24, 64), (34, 52), (44, 60), (46, 78), (36, 82), (26, 76)], 6), GL, 'f', False),
                L(blob([(76, 64), (66, 52), (56, 60), (54, 78), (64, 82), (74, 76)], 6), GL, 'f', False),
                L(blob([(30, 66), (36, 60), (40, 66), (40, 76), (34, 76)], 6), HM, 'f', False),
                L(blob([(70, 66), (64, 60), (60, 66), (60, 76), (66, 76)], 6), HM, 'f', False),
                L(outline([(-6, 70), (-14, 82, 1), (4, 84), (-10, 92, 1), (10, 88)]), HM, 'f')]
    if view == 'side':
        return [L(outline([(30, 14), (36, -10, 1), (48, 6), (58, -12, 1), (66, 4), (76, -6, 1), (82, 14)]), GR, 'b'),
                L(outline([(52, 92), (40, 100), (14, 92), (2, 66), (4, 34), (22, 10), (50, 2), (76, 8), (92, 28), (94, 56), (92, 86), (78, 84), (62, 80)]), HM, 'f'),
                L(blob([(70, 62), (80, 52), (90, 58), (92, 76), (80, 80), (70, 74)], 6), GL, 'f', False),
                L(outline([(36, 50), (30, 22, 1), (46, 30), (48, 60)]), GY, 'f'),
                L(outline([(8, 74), (-12, 80, 1), (2, 86), (-10, 98, 1), (12, 90)]), HM, 'f')]
    return [L(outline([(16, 20), (24, -8, 1), (32, 8), (40, -14, 1), (50, 2), (60, -14, 1), (68, 8), (76, -8, 1), (84, 20)]), GR, 'b'),
            L(outline([(8, 92), (4, 54), (10, 26), (30, 10), (50, 6), (70, 10), (90, 26), (96, 54), (92, 92), (50, 98)]), HM),
            L(outline([(2, 60), (-4, 30, 1), (12, 22), (14, 70)]), GY, 'f'), L(outline([(98, 60), (104, 30, 1), (88, 22), (86, 70)]), GY, 'f'),
            L(outline([(42, 74), (22, 80, 1), (40, 86), (30, 100, 1), (50, 84), (70, 100, 1), (60, 86), (78, 80, 1), (58, 74)]), HM, 'f')]


C('payne-green-d-outler', 'normal', P('#3a8a2a', '#e8c49a'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=95, hairline=False, ears=False),
  _payne('front'), _payne('side'), _payne('back'))

# Pearl Wann: melena morada en casco hasta la barbilla, raya a un lado; ojos grandes redondos, pecas y boca seria
C('pearl-wann', 'chica', P('#644968', '#fcc272', iris='#1e1414', shade='#523b4a', deep='#3e2a33'),
  F(eyes='round', brows=True, mouth='line', mouth_y=94, hairline=[(8, 66), (16, 52), (30, 44), (44, 40), (52, 44), (66, 46), (82, 52), (92, 66)]),
  bowl('front', top=2, side=92) + [fr([(40, 14), (56, 10), (70, 22), (54, 30), (38, 48), (36, 30)])] + freckles(84, 24),
  bowl('side', top=2, nape=94),
  bowl('back', top=2, nape=94))

# Perry Postiche (portero): viejo calvo con dos mechones grises que salen de punta por encima de las orejas; gafitas
# redondas rojas y boca seria
GREY, RED = _c('#7f8a8a'), _c('#c01040')
C('perry-postiche', 'normal', P('#7f8a8a', '#fdc270', iris='#1e1414'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=94, hairline=False, nose=(50, 86, 2.4)),
  [skull(), L(outline([(16, 64), (4, 54), (2, 26, 1), (16, 36), (24, 54)]), GREY), L(outline([(84, 64), (96, 54), (98, 26, 1), (84, 36), (76, 54)]), GREY)] +
  [L(ell(38, 76, 8, 7), RED, 'f'), L(ell(62, 76, 8, 7), RED, 'f'), L([(46, 75), (54, 75)], RED, 'f', False, False, 1.6),
   L([(28, 62), (38, 66), (44, 64)], OUTC, 'f', False, False, 1.4), L([(72, 62), (62, 66), (56, 64)], OUTC, 'f', False, False, 1.4)],
  [L(outline([(40, 66), (28, 56), (24, 30, 1), (38, 40), (50, 58)]), GREY), L(ell(80, 76, 6, 7), RED, 'f'), L([(74, 75), (50, 70)], RED, 'f', False, False, 1.4)],
  [L(outline([(14, 70), (2, 58), (2, 28, 1), (16, 38), (24, 62)]), GREY), L(outline([(86, 70), (98, 58), (98, 28, 1), (84, 38), (76, 62)]), GREY)])

# Pete Manter: pelo gris verdoso muy corto con dos entradas que dejan un pico en el centro; cara larga, ceño fruncido
C('pete-manter', 'delgado', P('#5f786b', '#fcc271', iris='#1e1414', shade='#4a6054', deep='#3a4a42'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=98, face_front=face(chin=108, jaw=1), face_side=face_side(chin=7), nose=(50, 86, 2.4),
    hairline=[(10, 64), (16, 44), (30, 30), (44, 40), (50, 52), (56, 40), (70, 30), (84, 44), (90, 64)]),
  dome('front', top=4, w=44, cy=44, sb=62, shade=True),
  dome('side', top=4, w=44, cy=44, nape=80, fr=40),
  dome('back', top=4, w=44, cy=44, nape=80))

# Pete Pimento: pelo rojo en llamas de pinchos altos hacia arriba; nariz naranja en triángulo, sonrisa pícara y ojos entornados
OR = _c('#e88a30')
C('pete-pimento', 'normal', P('#aa392b', '#f9bb7c', iris='#1e1414', shade='#75271e'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=95, hairline=hl(6, 64, 50, 60, jit=2, seed=3)),
  dome('front', top=-8, w=48, cy=42, n=7, amp=18, seed=21, sb=66) + [L(outline([(44, 82), (56, 82), (50, 90)]), OR, 'f')],
  dome('side', top=-8, w=48, cy=42, n=7, amp=18, seed=21, nape=86, fr=50, sweep=0.2) + [L(outline([(84, 80), (92, 84), (84, 88)]), OR, 'f')],
  dome('back', top=-8, w=48, cy=42, n=7, amp=18, seed=21, nape=86))

# Peter Fakhoury: pelo rubio platino muy corto, piel morena, ojos verde agua y ceño fruncido; cara larga
C('peter-fakhoury', 'delgado', P('#fef7cc', '#af8b71', iris='#3aa8a0', shade='#e0d8a8', deep='#c8bc8a', skin_d='#89604d'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=98, face_front=face(chin=108), face_side=face_side(chin=7), nose=(50, 86, 3),
    hairline=[(10, 62), (16, 48), (30, 44), (50, 42), (70, 44), (84, 48), (90, 62)]),
  dome('front', top=2, w=45, cy=44, sb=60, n=8, amp=4, seed=4),
  dome('side', top=2, w=45, cy=44, nape=80, fr=44, n=8, amp=4, seed=4),
  dome('back', top=2, w=45, cy=44, nape=80, n=8, amp=4, seed=4))

# Phil Pagoda (portero): tupé castaño oscuro peinado hacia atrás con una franja crema, que acaba en una punta por detrás
CR = _c('#eef4da')
C('phil-pagoda', 'normal', P('#562f05', '#f5c094', iris='#1e1414', shade='#412409'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(10, 62), (14, 50), (28, 40), (50, 38), (72, 40), (86, 50), (90, 62)]),
  [L(outline([(12, 62), (6, 36), (18, 4), (46, -8), (80, -2), (100, 30), (102, 60, 1), (90, 50), (88, 64), (80, 48), (20, 48)])),
   L(outline([(58, -6), (72, -4), (88, 30), (96, 56), (86, 40)]), CR, 'b', False),
   L(outline([(70, -4), (80, -2), (100, 30), (102, 60), (90, 46)]), 'shade', 'b', False)],
  [L(outline([(80, 50), (88, 36), (82, 6), (56, -8), (26, -4), (4, 14), (-10, 40, 1), (4, 50), (8, 70), (24, 80), (46, 74), (54, 58), (66, 52)])),
   L(outline([(52, -6), (64, -6), (40, 10), (10, 30), (4, 24)]), CR, 'b', False)],
  [L(outline([(12, 76), (6, 36), (18, 4), (50, -6), (82, 4), (94, 36), (88, 76), (50, 84)])),
   L(outline([(56, -4), (66, -2), (62, 40), (54, 80), (50, 40)]), CR, 'b', False)])

# Phil Seebold: pelo gris morado en pinchos echados a un lado, con un flequillo largo que le tapa un ojo; ojos rojos y
# sonrisa de dientes
C('phil-seebold', 'normal', P('#7e6270', '#efd4a4', iris='#b02020', shade='#603f47', deep='#4e3237'),
  F(eyes='sharp', brows=False, mouth='grin', mouth_y=95, hairline=hl(5, 66, 50, 60, lean=-3, jit=2, seed=6)),
  dome('front', top=-4, w=48, cy=44, n=7, amp=14, sweep=-0.6, seed=22, sb=72) +
  [fr([(20, 40), (40, 34), (52, 46), (48, 72), (40, 88, 1), (34, 70), (22, 58)])],
  dome('side', top=-4, w=48, cy=44, n=7, amp=14, sweep=-0.6, seed=22, nape=88, fr=52),
  dome('back', top=-4, w=48, cy=44, n=7, amp=14, sweep=-0.6, seed=22, nape=88))

# Philippa Konik: melena castaña oscura con dos coletas bajas atadas con gomas turquesa que caen por delante; ojos
# grandes ámbar y sonrisa
TQ = _c('#4eaab3')
C('philippa-konik', 'chica', P('#5d3134', '#fbcfa0', iris='#c87a1a', shade='#432323'),
  F(eyes='round', brows=True, mouth='smile', mouth_y=94, hairline=hl(4, 64, 50, 60, jit=2, seed=7)),
  longhair('front', length=116, flare=6) + ties('front', TQ, 98),
  longhair('side', length=116, flare=6) + ties('side', TQ, 98),
  longhair('back', length=116, flare=6) + ties('back', TQ, 98))

# Polly Targest: melena corta rosa salmón ondulada que se abre en las puntas; ojos redondos de preocupación y boca torcida
C('polly-targest', 'chica', P('#c57065', '#f9bb7c', iris='#4a6a9a', shade='#9d5548', deep='#72392e'),
  F(eyes='round', brows=True, mouth='frown', mouth_y=95, hairline=[(8, 66), (16, 52), (30, 46), (48, 44), (60, 40), (74, 46), (86, 52), (92, 66)]),
  bowl('front', top=2, side=90, w=2) + [L(outline([(8, 88), (-2, 96, 1), (12, 92)])), L(outline([(92, 88), (102, 96, 1), (88, 92)]))],
  bowl('side', top=2, nape=92, w=2),
  bowl('back', top=2, nape=92, w=2))

# Portia Maricle: pelo granate recogido con una cinta azul y blanca en la frente y una coleta larga que le cae a un lado;
# ojos azules enfadados, boca abierta
HB = _c('#5a8aa8')
C('portia-maricle', 'chica', P('#72393d', '#fce9b9', iris='#3a5a8a', shade='#5a2a2e', light='#93555b'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=[(8, 64), (16, 52), (30, 48), (50, 46), (70, 48), (84, 52), (92, 64)]),
  dome('front', top=0, w=48, cy=44, sb=70) +
  [L(outline([(10, 54), (50, 46), (90, 54), (90, 60), (50, 52), (10, 60)]), HB, 'f'), L([(14, 56), (50, 49), (86, 56)], WHITE, 'f', False, False, 1.4),
   L(outline([(84, 70), (96, 80), (98, 104), (90, 118, 1), (88, 96), (80, 82)])), fr([(54, 52), (60, 52), (62, 70), (58, 80, 1), (56, 64)])],
  dome('side', top=0, w=48, cy=44, nape=84, fr=50) + tail('side', side_len=118) +
  [L(outline([(12, 44), (80, 44), (88, 48), (88, 53), (12, 52)]), HB, 'f')],
  dome('back', top=0, w=48, cy=44, nape=84) + tail('back', side_len=118, x=60) + [L(outline([(12, 50), (88, 50), (88, 55), (12, 55)]), HB, 'f')])

# Prunella Keep: gorro rosa con un corazón verde y un lazo verde; flequillo castaño barrido y dos tirabuzones a los lados;
# ojos grandes verde agua, colorete y sonrisa abierta
PKH, GH, BR = _c('#f4b8b0'), _c('#3aa880'), _c('#a6700a')
C('prunella-keep', 'chica', P('#a6700a', '#f8d8b5', iris='#2aa890', shade='#7a5208'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=94, hairline=False),
  [L(outline([(8, 64), (6, 30), (24, 6), (50, -2), (76, 6), (94, 30), (92, 64), (82, 52), (50, 46), (18, 52)]), PKH),
   L(blob([(38, 14), (46, 8), (50, 14), (54, 8), (62, 14), (50, 28)], 6), GH, 'b', False),
   L(outline([(12, 18), (4, 8, 1), (16, 6), (22, 14), (14, 26, 1)]), GH, 'f'),
   fr([(22, 50), (40, 38), (66, 34), (80, 42), (74, 52), (54, 48), (36, 60, 1)]),
   L(outline([(12, 70), (6, 82), (14, 92), (8, 102, 1), (18, 92), (14, 80)])), L(outline([(88, 70), (94, 82), (86, 92), (92, 102, 1), (82, 92), (86, 80)]))] +
  blush(86, 24),
  [L(outline([(10, 70), (4, 36), (22, 6), (50, -4), (78, 4), (94, 26), (94, 54), (60, 50), (30, 62)]), PKH),
   L(outline([(30, 6), (22, -4, 1), (36, -6), (38, 4)]), GH, 'f'), fr([(70, 40), (88, 40), (92, 52), (80, 50)]),
   L(outline([(48, 70), (44, 84), (50, 96), (46, 104, 1), (54, 94), (52, 80)]))],
  [L(outline([(8, 74), (6, 30), (24, 6), (50, -2), (76, 6), (94, 30), (92, 74), (50, 80)]), PKH),
   L(outline([(16, 74), (12, 88), (18, 100, 1), (24, 86)])), L(outline([(84, 74), (88, 88), (82, 100, 1), (76, 86)]))])

# Quill Inker: pelo morado corto con flequillo en mechones y dos horquillas turquesa; boca abierta de sorpresa
TQ2 = _c('#4ab0b0')
C('quill-inker', 'normal', P('#876e91', '#f8bc7d', iris='#1e1414', shade='#624956', deep='#4d363b'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=95, hairline=hl(5, 66, 50, 62, lean=1, jit=2, seed=8)),
  dome('front', top=2, w=48, cy=44, sb=74, n=0) + [L([(16, 52), (22, 46)], TQ2, 'f', False, False, 2.2), L([(84, 52), (78, 46)], TQ2, 'f', False, False, 2.2)],
  dome('side', top=2, w=48, cy=44, nape=88, fr=52) + [L([(66, 50), (74, 46)], TQ2, 'f', False, False, 2.2)],
  dome('back', top=2, w=48, cy=44, nape=88))

# Ralph Fary: melena lisa rosa claro, con la raya a un lado, que le tapa un ojo y cae larga por ese lado; piel morena, ojo verde
C('ralph-fary', 'normal', P('#fcd9fa', '#dca157', iris='#4a6a3a', shade='#c48b9f', deep='#936f78', skin_d='#ab693e'),
  F(eyes='sharp', brows=True, mouth='line', mouth_y=95, hairline=[(8, 64), (14, 50), (26, 42), (40, 40), (50, 44), (60, 40), (80, 46), (92, 64)]),
  dome('front', top=0, w=47, cy=44, sb=74) +
  [fr([(46, 36), (62, 30), (84, 44), (94, 70), (92, 104), (84, 122, 1), (80, 96), (72, 82), (56, 64), (48, 54)]),
   L(outline([(74, 60), (88, 52), (94, 80), (90, 110), (84, 90)]), 'shade', 'f', False)],
  dome('side', top=0, w=47, cy=44, nape=90, fr=52) + [fr([(70, 40), (92, 46), (96, 80), (90, 116, 1), (84, 84), (72, 62)])],
  dome('back', top=0, w=47, cy=44, nape=90) + [L(outline([(6, 60), (2, 100), (8, 116, 1), (18, 90)]))])

# Ralph Vance: un bloque de pelo verde azulado oscuro altísimo y plano por arriba, con una estrella de piel en la frente y
# patillas hasta la barbilla, donde le cruza una correa blanca; ceño fruncido
TL = _c('#146666')
C('ralph-vance', 'corpulento', P('#146666', '#fac273', iris='#1e1414', shade='#124341', deep='#0e3432'),
  F(eyes='round', brows='angry', mouth='none', face_front=face(w=4, chin=106, jaw=2), face_side=face_side(chin=5, jaw=4), nose=(50, 86, 3.6),
    hairline=[(6, 64), (14, 56), (24, 58), (36, 48), (44, 56), (50, 46), (56, 56), (64, 48), (76, 58), (86, 56), (94, 64)]),
  [L(outline([(6, 96), (2, 60), (2, -20), (98, -20), (98, 60), (94, 96), (84, 104), (80, 60), (20, 60), (16, 104)])),
   L(outline([(60, -20), (98, -20), (98, 60), (90, 90), (84, 60)]), 'shade', 'b', False),
   L(ell(50, -8, 8, 9), 'shade', 'b', False),
   L(outline([(20, 98), (50, 102), (80, 98), (80, 104), (50, 108), (20, 104)]), WHITE, 'f')],
  [L(outline([(70, 52), (84, 46), (90, 24), (90, -20), (6, -20), (2, 40), (6, 80), (28, 92), (46, 96), (54, 84), (54, 64)])),
   L(outline([(52, 70), (62, 104), (70, 104), (60, 70)]), WHITE, 'f')],
  [L(outline([(4, 90), (2, -20), (98, -20), (96, 90), (50, 96)])),
   L(outline([(60, -20), (98, -20), (96, 86), (70, 92)]), 'shade', 'b', False)])

# Ramona Wriston: pelo rubio oscuro en pinchos grandes alrededor de la cabeza, con una cinta roja en la frente;
# pendientes rojos y sonrisa
RB = _c('#c8402a')
C('ramona-wriston', 'chica', P('#e9c27b', '#fceec7', iris='#7a3a1a', shade='#bf774b', deep='#984d30'),
  F(eyes='round', brows=True, mouth='smile', mouth_y=94, hairline=hl(5, 66, 54, 62, jit=2, seed=9)),
  dome('front', top=-6, w=52, cy=44, n=9, amp=14, seed=23, sb=72) +
  [L(outline([(12, 52), (50, 42), (88, 52), (88, 60), (50, 50), (12, 60)]), RB, 'f')] + earrings(RB, 88),
  dome('side', top=-6, w=52, cy=44, n=9, amp=14, seed=23, nape=88, fr=50) + [L(outline([(10, 42), (88, 44), (88, 51), (10, 50)]), RB, 'f')] + earrings(RB, 88, True),
  dome('back', top=-6, w=52, cy=44, n=9, amp=14, seed=23, nape=88) + [L(outline([(10, 52), (90, 52), (90, 59), (10, 59)]), RB, 'f')])

# Randolph Lords (portero): pelo azul grisáceo muy corto y plano por arriba, gafas ovaladas finas negras, sonrisa de suficiencia
C('randolph-lords', 'delgado', P('#4b6a74', '#fbc273', iris='#1e1414'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=97, face_front=face(chin=106), face_side=face_side(chin=5), nose=(50, 86, 2.4),
    hairline=[(10, 62), (16, 50), (30, 44), (50, 42), (70, 44), (84, 50), (90, 62)]),
  [L(outline([(12, 62), (8, 30), (16, 6), (50, 2), (84, 6), (92, 30), (88, 62), (80, 48), (20, 48)])),
   L(outline([(60, 4), (84, 6), (92, 30), (88, 58), (78, 34)]), 'shade', 'b', False)] + round_specs('front', BLACK, 77, 15, 10, 6, 1.4),
  [L(outline([(80, 50), (86, 30), (82, 6), (50, 0), (20, 6), (4, 26), (4, 60), (18, 76), (40, 76), (52, 60), (64, 50)]))] + round_specs('side', BLACK, 77, 15, 10, 6, 1.4),
  [L(outline([(10, 74), (8, 30), (16, 6), (50, 2), (84, 6), (92, 30), (90, 74), (50, 80)])),
   L(outline([(60, 4), (84, 6), (92, 30), (90, 70), (70, 76)]), 'shade', 'b', False)])

# Ray Bowing: pelo morado peinado hacia atrás con mechones finos sobre la frente y una coleta baja que sale volando hacia
# un lado; orejas de punta, ojos cerrados de sonrisa y sonrisa ancha
C('ray-bowing', 'delgado', P('#6b5d70', '#fbecc2', iris='#1e1414', shade='#574a51', light='#8c8187'),
  F(eyes='closed', brows='angry', mouth='grin', mouth_y=96, face_front=face(chin=106), face_side=face_side(chin=5), big_ears=2, ear_out=2,
    hairline=[(10, 60), (18, 46), (34, 40), (50, 40), (66, 40), (82, 46), (90, 60)]),
  [L(outline([(12, 60), (8, 30), (20, 6), (50, 0), (80, 6), (92, 30), (88, 60), (80, 46), (20, 46)])),
   L(outline([(60, 2), (80, 6), (92, 30), (88, 56), (76, 30)]), 'shade', 'b', False),
   L(outline([(20, 86), (4, 96), (-14, 100, 1), (6, 90), (16, 80)])),
   strand([(40, 40), (36, 58), (40, 66)], 'deep', 'f', 1.2), strand([(58, 40), (64, 56), (60, 64)], 'deep', 'f', 1.2)],
  [L(outline([(80, 48), (86, 28), (78, 4), (50, -2), (20, 4), (4, 26), (4, 58), (16, 74), (30, 76), (-14, 96, 1), (20, 84), (44, 74), (54, 58), (64, 48)])),
   strand([(76, 42), (82, 56), (80, 66)], 'deep', 'f', 1.2)],
  [L(outline([(10, 70), (8, 30), (20, 6), (50, 0), (80, 6), (92, 30), (90, 70), (50, 76)])),
   L(outline([(44, 74), (56, 74), (70, 90), (100, 100, 1), (66, 98), (50, 84)])),
   L(outline([(60, 2), (80, 6), (92, 30), (90, 66), (70, 72)]), 'shade', 'b', False)])

# Rayce Sprinton: melena naranja lisa hasta los hombros, con un mechón que le tapa un ojo; orejas de punta, piel morena,
# ojos negros afilados y un colmillo
C('rayce-sprinton', 'normal', P('#d06204', '#dca259', iris='#1e1414', shade='#9e4409', deep='#73320c', skin_d='#ab6e3c'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, big_ears=1, ear_out=2,
    hairline=[(8, 64), (14, 50), (28, 42), (44, 44), (54, 40), (70, 42), (86, 50), (92, 64)]),
  longhair('front', length=104, flare=4) + [fr([(46, 38), (60, 36), (64, 56), (58, 84, 1), (50, 60), (44, 50)]),
                                            L(quad((53, 95), (55, 99), (57, 95)) + [(57, 95)], WHITE, 'f', False)],
  longhair('side', length=104, flare=4) + [fr([(76, 38), (90, 40), (92, 60), (88, 82, 1), (82, 56)])],
  longhair('back', length=104, flare=4, ends=3))

# Red Deer Dayers: máscara de ciervo marrón con cuernos crema y orejas, hocico claro con nariz oscura, ojos blancos
# pequeños; enseña los dientes por debajo
DB, DL, AN = _c('#7d490d'), _c('#e5d1b2'), _c('#e8d8b8')
C('red-deer-dayers', 'normal', P('#7d490d', '#d8b896', iris='#1e1414'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  [L(outline([(30, 14), (26, -14), (16, -26, 1), (28, -20), (30, -36, 1), (34, -16), (40, 10)]), AN),
   L(outline([(70, 14), (74, -14), (84, -26, 1), (72, -20), (70, -36, 1), (66, -16), (60, 10)]), AN),
   L(outline([(10, 106), (8, 60), (-12, 40, 1), (12, 34), (30, 18), (50, 14), (70, 18), (88, 34), (112, 40, 1), (92, 60), (90, 106), (76, 108), (66, 100), (34, 100), (24, 108)]), DB, 'f'),
   L(outline([(26, 70), (38, 64), (62, 64), (74, 70), (70, 100), (60, 106), (40, 106), (30, 100)]), DL, 'f', False),
   L(ell(36, 60, 5, 3.6), WHITE, 'f'), L(ell(64, 60, 5, 3.6), WHITE, 'f'), L(ell(36, 60, 1.6, 1.6), BLACK, 'f', False), L(ell(64, 60, 1.6, 1.6), BLACK, 'f', False),
   L(outline([(44, 84), (56, 84), (50, 92)]), _c('#6a3a14'), 'f', False),
   L(outline([(34, 100), (66, 100), (64, 108), (36, 108)]), WHITE, 'f'), L([(40, 104), (60, 104)], OUTC, 'f', False, False, 0.8)],
  [L(outline([(40, 12), (36, -16), (26, -28, 1), (38, -22), (42, -36, 1), (46, -16), (50, 10)]), AN),
   L(outline([(54, 104), (36, 102), (12, 90), (2, 60), (8, 30), (30, 12), (60, 10), (80, 24), (94, 52), (104, 80), (100, 96), (84, 104), (70, 100)]), DB, 'f'),
   L(outline([(30, 40), (18, 26, 1), (40, 32)]), DB, 'f'),
   L(outline([(76, 60), (104, 80), (100, 96), (84, 104), (72, 98)]), DL, 'f', False), L(ell(76, 58, 4, 3), WHITE, 'f')],
  [L(outline([(30, 14), (26, -14), (16, -26, 1), (28, -20), (30, -36, 1), (34, -16), (40, 10)]), AN),
   L(outline([(70, 14), (74, -14), (84, -26, 1), (72, -20), (70, -36, 1), (66, -16), (60, 10)]), AN),
   L(outline([(10, 100), (8, 60), (-12, 40, 1), (12, 34), (30, 18), (50, 14), (70, 18), (88, 34), (112, 40, 1), (92, 60), (90, 100), (50, 106)]), DB, 'f')])

# Reed Harpen: pelo verde oliva en mechones de punta peinados hacia arriba; niño pequeño, ceño fruncido y boquita
C('reed-harpen', 'bajito', P('#7e8a50', '#fbc272', iris='#1e1414', shade='#625f3b', deep='#4e452a'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=94, hairline=hl(4, 62, 48, 56, jit=2, seed=10)),
  [L(outline([(14, 62), (6, 34), (-6, 10, 1), (12, 16), (14, -14, 1), (30, 8), (40, -26, 1), (52, 4), (66, -18, 1), (70, 8), (90, -6, 1), (86, 20), (104, 18, 1),
              (92, 36), (86, 62), (80, 48), (20, 48)])),
   L(outline([(56, 0), (66, -18), (70, 8), (90, -6), (86, 20), (100, 20), (90, 40), (84, 58), (74, 30)]), 'shade', 'b', False)],
  [L(outline([(80, 48), (92, 30), (102, 10, 1), (84, 12), (88, -16, 1), (66, 2), (58, -26, 1), (44, 2), (24, -16, 1), (22, 10), (2, 8, 1), (8, 30), (6, 56), (20, 76), (40, 76), (52, 58), (66, 50)]))],
  [L(outline([(12, 74), (6, 34), (-6, 10, 1), (12, 16), (14, -14, 1), (30, 8), (40, -26, 1), (52, 4), (66, -18, 1), (70, 8), (90, -6, 1), (86, 20), (104, 18, 1),
              (92, 36), (88, 74), (50, 80)]))])

# Reg Strimmer: pelo gris verdoso corto peinado hacia atrás; cara cuadrada enorme de mandíbula ancha, nariz triangular
# y una boca abierta enorme de sonrisa
C('reg-strimmer', 'corpulento', P('#656b5a', '#fcc272', iris='#1e1414', shade='#48473c'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=98, mouth_w=16, face_front=face(w=8, chin=108, jaw=8), face_side=face_side(chin=7, jaw=8),
    hairline=[(6, 58), (14, 46), (30, 40), (50, 38), (70, 40), (86, 46), (94, 58)]),
  [L(outline([(8, 58), (6, 30), (20, 6), (50, 0), (80, 6), (94, 30), (92, 58), (84, 44), (16, 44)])),
   L(outline([(60, 2), (80, 6), (94, 30), (92, 54), (78, 30)]), 'shade', 'b', False),
   L(outline([(44, 80), (56, 80), (50, 90)]), _c('#c8814e'), 'f')],
  [L(outline([(80, 46), (86, 28), (78, 4), (50, -2), (20, 4), (4, 26), (4, 56), (18, 72), (40, 72), (52, 56), (64, 46)])), L(outline([(86, 78), (96, 82), (86, 88)]), _c('#c8814e'), 'f')],
  [L(outline([(8, 70), (6, 30), (20, 6), (50, 0), (80, 6), (94, 30), (92, 70), (50, 76)])),
   L(outline([(60, 2), (80, 6), (94, 30), (92, 66), (70, 72)]), 'shade', 'b', False)])

# Remy Diggun: melena gris parda revuelta hasta los hombros, abierta en puntas; ojos redondos azules preocupados
C('remy-diggun', 'normal', P('#715d55', '#f5be93', iris='#3a5a8a', shade='#57403a', deep='#432e29'),
  F(eyes='round', brows=True, mouth='frown', mouth_y=95, hairline=[(8, 66), (14, 52), (28, 44), (44, 40), (56, 42), (72, 44), (86, 52), (92, 66)]),
  longhair('front', length=100, flare=10, ends=4) + [L(outline([(2, 92), (-8, 100, 1), (6, 98)])), L(outline([(98, 92), (108, 100, 1), (94, 98)]))],
  longhair('side', length=100, flare=10),
  longhair('back', length=100, flare=10, ends=5))

# Rhoda Dough: pelo verde lima recogido en un moño alto enorme, atado con una cinta castaña y una horquilla roja; ojos
# cerrados de sonrisa
LIME, BRN, RD2 = _c('#a1ba3e'), _c('#8c682a'), _c('#c82a2a')
C('rhoda-dough', 'chica', P('#a1ba3e', '#fdeab8', iris='#1e1414', light='#b4cd52'),
  F(eyes='closed', brows=True, mouth='smile', mouth_y=94, hairline=[(10, 62), (16, 50), (30, 44), (50, 42), (70, 44), (84, 50), (90, 62)]),
  [L(outline([(12, 62), (8, 30), (22, 8), (50, 2), (78, 8), (92, 30), (88, 62), (80, 48), (20, 48)])),
   L(outline([(30, 6), (32, -14), (50, -22), (68, -14), (70, 6)]), BRN), L(ell(50, -26, 14, 10)),
   L(ell(70, -30, 4, 4), RD2, 'f'), L([(66, -26), (76, -34)], BLACK, 'f', False, False, 1.2),
   strand([(40, 10), (42, 40)], 'shade', 'b', 1.0), strand([(60, 10), (58, 40)], 'shade', 'b', 1.0)],
  [L(outline([(80, 48), (86, 28), (78, 4), (50, -2), (20, 4), (4, 26), (4, 58), (18, 74), (40, 74), (52, 58), (64, 48)])),
   L(outline([(30, 4), (32, -14), (46, -20), (58, -14), (60, 4)]), BRN), L(ell(44, -24, 13, 10)), L(ell(58, -30, 4, 4), RD2, 'f')],
  [L(outline([(10, 72), (8, 30), (22, 8), (50, 2), (78, 8), (92, 30), (90, 72), (50, 78)])),
   L(outline([(30, 6), (32, -14), (50, -22), (68, -14), (70, 6)]), BRN), L(ell(50, -26, 14, 10)), L(ell(70, -30, 4, 4), RD2, 'f')])

# Richard Trogg: máscara blanca de demonio hannya con cuernos amarillos, cejas tristes, ojos de rendija, boca roja enorme
# y dientes dorados; pelo negro por encima
MW, HY, MR = _c('#efe8cc'), _c('#e8c040'), _c('#c82a2a')
C('richard-trogg', 'normal', P('#201c18', '#f1c79b', iris='#1e1414'),
  F(eyes='none', brows=False, mouth='none', hairline=False),
  [L(outline([(14, 50), (10, 26), (28, 8), (50, 2), (72, 8), (90, 26), (86, 50)])),
   L(outline([(22, 20), (14, -14), (10, -30, 1), (22, -10), (30, 14)]), HY), L(outline([(78, 20), (86, -14), (90, -30, 1), (78, -10), (70, 14)]), HY),
   L(outline([(16, 40), (36, 24), (50, 30), (64, 24), (84, 40), (88, 70), (82, 98), (66, 114), (50, 116), (34, 114), (18, 98), (12, 70)]), MW, 'f'),
   L([(28, 54), (38, 50), (44, 54)], BLACK, 'f', False, False, 1.6), L([(72, 54), (62, 50), (56, 54)], BLACK, 'f', False, False, 1.6),
   L(quad((30, 68), (38, 64), (44, 68)), BLACK, 'f', False, False, 1.8), L(quad((70, 68), (62, 64), (56, 68)), BLACK, 'f', False, False, 1.8),
   L(outline([(24, 86), (36, 94), (50, 96), (64, 94), (76, 86), (72, 108), (50, 114), (28, 108)]), MR, 'f'),
   L(outline([(32, 94), (68, 94), (66, 106), (34, 106)]), _c('#d8c070'), 'f', False), L([(36, 100), (64, 100)], OUTC, 'f', False, False, 0.8)],
  [L(outline([(80, 40), (86, 24), (72, 6), (46, 0), (20, 6), (4, 30), (6, 60), (20, 78), (40, 76), (52, 56), (64, 44)])),
   L(outline([(50, 14), (46, -16), (40, -30, 1), (54, -12), (60, 12)]), HY),
   L(outline([(66, 30), (84, 34), (94, 60), (92, 92), (80, 112), (62, 114), (60, 70)]), MW, 'f'),
   L(outline([(74, 88), (92, 88), (88, 106), (76, 106)]), MR, 'f')],
  [L(outline([(10, 72), (8, 30), (22, 8), (50, 2), (78, 8), (92, 30), (90, 72), (50, 78)])),
   L(outline([(22, 20), (14, -14), (10, -30, 1), (22, -10), (30, 14)]), HY), L(outline([(78, 20), (86, -14), (90, -30, 1), (78, -10), (70, 14)]), HY),
   L([(10, 70), (90, 70)], BLACK, 'f', False, False, 1.4)])

# Rob Cardson: sombrero vaquero azul marino con parches rojos y dos tachuelas doradas; piel morena con rayas rojas
# pintadas, ojos blancos enfadados y dos colmillos cuadrados
NV, RP, GD = _c('#474b64'), _c('#b53f3a'), _c('#d8b040')


def _hat(view):
    if view == 'front':
        return [L(outline([(-12, 54), (4, 52), (10, 20), (30, 4), (60, 2), (84, 16), (92, 50), (112, 40, 1), (100, 62), (50, 58), (-2, 64)]), NV),
                L(outline([(40, 8), (56, 4), (52, 22)]), RP, 'b', False), L(outline([(62, 20), (82, 28), (72, 46)]), RP, 'b', False),
                L(ell(22, 40, 3.4, 4), GD, 'b', False), L(ell(30, 46, 3.4, 4), GD, 'b', False)]
    if view == 'side':
        return [L(outline([(-8, 50), (6, 44), (12, 14), (40, 0), (72, 6), (84, 30), (88, 46), (108, 44, 1), (90, 58), (40, 56), (0, 62)]), NV),
                L(outline([(50, 6), (70, 10), (60, 26)]), RP, 'b', False)]
    return [L(outline([(-12, 60), (4, 54), (10, 20), (30, 4), (60, 2), (84, 16), (96, 54), (112, 60, 1), (50, 66), (-12, 66)]), NV),
            L(outline([(36, 12), (54, 8), (48, 30)]), RP, 'b', False)]


C('rob-cardson', 'corpulento', P('#2b2123', '#cd976b', iris='#1e1414'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=98, face_front=face(w=6, chin=106, jaw=4), face_side=face_side(chin=5, jaw=4), hairline=False, nose=(50, 88, 3)),
  _hat('front') + [L([(16, 70), (22, 92)], RP, 'f', False, False, 2.6), L([(84, 70), (78, 92)], RP, 'f', False, False, 2.6),
                   L(outline([(36, 96), (42, 96), (40, 102)]), WHITE, 'f'), L(outline([(58, 96), (64, 96), (60, 102)]), WHITE, 'f')],
  _hat('side') + [L([(74, 70), (78, 90)], RP, 'f', False, False, 2.6)],
  _hat('back') + [L(outline([(12, 66), (88, 66), (84, 80), (16, 80)]), _c('#2b2123'))])

# Rob Otts (portero): cabeza de robot, un marco gris que la rodea con dos discos naranjas en las orejas, gafas redondas de
# cristal marrón y una boca de dientes cuadrados
RG, RO, RL = _c('#828389'), _c('#e8902a'), _c('#a86a1a')
C('rob-otts', 'normal', P('#828389', '#e3ccae', iris='#1e1414'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, face_front=blob([(16, 30), (84, 30), (84, 106), (16, 106)], 4)),
  [L(outline([(10, 108), (8, 20), (20, 6), (80, 6), (92, 20), (90, 108), (80, 108), (82, 30), (18, 30), (20, 108)]), RG, 'f'),
   L(ell(6, 62, 7, 11), RO, 'f'), L(ell(94, 62, 7, 11), RO, 'f'),
   L(ell(36, 62, 9, 9), RL, 'f'), L(ell(64, 62, 9, 9), RL, 'f'), L([(45, 62), (55, 62)], BLACK, 'f', False, False, 1.4),
   L(outline([(30, 86), (70, 86), (70, 100), (30, 100)]), WHITE, 'f'),
   L([(36, 86), (36, 100)], OUTC, 'f', False, False, 0.8), L([(43, 86), (43, 100)], OUTC, 'f', False, False, 0.8), L([(50, 86), (50, 100)], OUTC, 'f', False, False, 0.8),
   L([(57, 86), (57, 100)], OUTC, 'f', False, False, 0.8), L([(64, 86), (64, 100)], OUTC, 'f', False, False, 0.8), L([(30, 93), (70, 93)], OUTC, 'f', False, False, 0.8)],
  [L(outline([(60, 108), (14, 108), (4, 80), (6, 20), (20, 6), (80, 6), (92, 24), (92, 34), (64, 34), (64, 108)]), RG, 'f'),
   L(ell(36, 62, 8, 12), RO, 'f'), L(ell(84, 62, 6, 7), RL, 'f'), L(outline([(76, 86), (92, 86), (92, 100), (76, 100)]), WHITE, 'f')],
  [L(outline([(8, 108), (8, 20), (20, 6), (80, 6), (92, 20), (92, 108)]), RG, 'f'), L(ell(6, 62, 7, 11), RO, 'f'), L(ell(94, 62, 7, 11), RO, 'f')])

# Robin Traylor: melena azul oscuro ondulada que se abre en dos alas a la altura de los hombros, con un mechón por la
# cara; ojos verdes afilados
C('robin-traylor', 'normal', P('#3a5163', '#f9c275', iris='#6a8a3a', shade='#2a3a4a', deep='#1e2a36'),
  F(eyes='sharp', brows=True, mouth='frown', mouth_y=95, hairline=[(8, 66), (14, 50), (28, 42), (44, 46), (54, 40), (70, 44), (86, 50), (92, 66)]),
  longhair('front', length=96, flare=14, ends=4) + [fr([(46, 40), (56, 40), (60, 60), (54, 90, 1), (50, 64)])],
  longhair('side', length=96, flare=14),
  longhair('back', length=96, flare=14, ends=5))

# Robyn Weaver (portera): un lazo naranja enorme encima de la cabeza; melena castaña corta con flequillo recto y dos
# mechones naranjas por delante; ojos negros redondos, colorete y boca seria
BOW, BW2 = _c('#f9a217'), _c('#c16c1d')
C('robyn-weaver', 'chica', P('#642906', '#f4dec1', iris='#1e1414', shade='#4a1e04'),
  F(eyes='dot', brows=False, mouth='line', mouth_y=95, hairline=[(8, 66), (14, 56), (30, 56), (50, 56), (70, 56), (86, 56), (92, 66)]),
  bowl('front', top=4, side=94) +
  [L(outline([(50, 6), (20, -16), (-4, -10), (4, 14), (30, 16)]), BOW, 'f'), L(outline([(50, 6), (80, -16), (104, -10), (96, 14), (70, 16)]), BOW, 'f'),
   L(ell(50, 6, 8, 7), BW2, 'f'),
   fr([(12, 40), (26, 30), (30, 60), (28, 100, 1), (18, 90), (10, 66)], BOW), fr([(88, 40), (74, 30), (70, 60), (72, 100, 1), (82, 90), (90, 66)], BOW)] + blush(88, 26),
  bowl('side', top=4, nape=94) + [L(outline([(48, 6), (28, -18), (8, -8), (18, 16)]), BOW, 'f'), L(ell(48, 6, 7, 6), BW2, 'f'),
                                 fr([(70, 40), (80, 40), (82, 100, 1), (72, 86)], BOW)],
  bowl('back', top=4, nape=94) + [L(outline([(50, 6), (20, -16), (-4, -10), (4, 14), (30, 16)]), BOW, 'f'),
                                 L(outline([(50, 6), (80, -16), (104, -10), (96, 14), (70, 16)]), BOW, 'f'), L(ell(50, 6, 8, 7), BW2, 'f')])

# Rock Poulon (portero): pelo verde grisáceo en casco con dos bollos a rayas que salen de lado, ojos de sueño entornados y
# boquita en O con labios naranjas
STR = _c('#d0e6e1')
C('rock-poulon', 'normal', P('#5c796c', '#f8bc7d', iris='#1e1414', shade='#465e52'),
  F(eyes='closed', brows=True, mouth='none', hairline=[(8, 62), (14, 54), (30, 54), (50, 54), (70, 54), (86, 54), (92, 62)]),
  bowl('front', top=4, side=64) +
  [L(outline([(10, 30), (-10, 20), (-14, 40, 1), (-4, 36), (6, 44)])), L(outline([(90, 30), (110, 20), (114, 40, 1), (104, 36), (94, 44)])),
   L([(-6, 26), (-2, 38)], STR, 'f', False, False, 1.6), L([(106, 26), (102, 38)], STR, 'f', False, False, 1.6),
   L(ell(50, 96, 5, 5), _c('#e8902a'), 'f'), L(ell(50, 96, 2, 2.2), _c('#6a2a14'), 'f', False)],
  bowl('side', top=4, nape=84) + [L(outline([(30, 30), (20, 16), (10, 34, 1), (22, 38)])), L(ell(88, 96, 3, 4), _c('#e8902a'), 'f')],
  bowl('back', top=4, nape=84) + [L(outline([(10, 30), (-10, 20), (-14, 40, 1), (-4, 36), (6, 44)])), L(outline([(90, 30), (110, 20), (114, 40, 1), (104, 36), (94, 44)]))])

# Rock Scowlon: pinchos verde oscuro altos que salen como una corona; ojos blancos vacíos y piel clara
C('rock-scowlon', 'normal', P('#446958', '#e3ccad', iris='#f0f0f0', shade='#3b463e'),
  F(eyes='none', brows=False, mouth='line', mouth_y=96, hairline=hl(5, 62, 50, 58, jit=2, seed=11)),
  dome('front', top=-6, w=50, cy=44, n=7, amp=18, seed=24, sb=62) +
  [L(blob([(26, 74), (34, 68), (44, 72), (44, 80), (30, 80)], 6), WHITE, 'f'), L(blob([(74, 74), (66, 68), (56, 72), (56, 80), (70, 80)], 6), WHITE, 'f')],
  dome('side', top=-6, w=50, cy=44, n=7, amp=18, seed=24, nape=84, fr=48) + [L(blob([(76, 72), (86, 70), (86, 80), (78, 80)], 6), WHITE, 'f')],
  dome('back', top=-6, w=50, cy=44, n=7, amp=18, seed=24, nape=84))

# Rod Sweeper: melena revuelta verde oliva en pinchos hasta el cuello; cara alargada en punta, ojos blancos de loco y
# sonrisa ancha con dos dientes
C('rod-sweeper', 'delgado', P('#565638', '#e3d1b5', iris='#f0f0f0', shade='#443e2b', deep='#352d23'),
  F(eyes='none', brows=False, mouth='buck', mouth_y=96, face_front=blob([(20, 50), (50, 40), (80, 50), (78, 80), (62, 104), (50, 118), (38, 104), (22, 80)], 8),
    face_side=face_side(chin=12), hairline=hl(5, 64, 50, 60, jit=3, seed=12)),
  messy('front', amp=14, n=12, seed=61, lo=86, rx=52, ry=42) +
  [L(blob([(28, 72), (36, 66), (44, 72), (42, 80), (30, 80)], 6), WHITE, 'f'), L(blob([(72, 72), (64, 66), (56, 72), (58, 80), (70, 80)], 6), WHITE, 'f'),
   L(ell(38, 74, 1.4, 1.4), BLACK, 'f', False), L(ell(62, 74, 1.4, 1.4), BLACK, 'f', False)],
  messy('side', amp=14, n=12, seed=61, lo=86, rx=52, ry=42) + [L(blob([(76, 70), (86, 68), (86, 78), (78, 78)], 6), WHITE, 'f')],
  messy('back', amp=14, n=12, seed=61, lo=86, rx=52, ry=42, nape=96))

# Roman Blac: pelo gris azulado largo con flequillo en mechones por el centro y rizos ondulados hasta los hombros; ojos
# entornados y boca torcida
C('roman-blac', 'normal', P('#7c8c92', '#fabd7d', iris='#4a4a20', shade='#595455'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=hl(5, 66, 50, 64, jit=3, seed=13)),
  longhair('front', length=104, flare=6) +
  [L(outline([(6, 84), (0, 94), (8, 104), (2, 112, 1), (12, 102), (8, 92)])), L(outline([(94, 84), (100, 94), (92, 104), (98, 112, 1), (88, 102), (92, 92)])),
   fr([(36, 30), (50, 26), (62, 34), (56, 60), (50, 70, 1), (44, 58)])],
  longhair('side', length=104, flare=6),
  longhair('back', length=104, flare=6, ends=5))

# Rose Bedd: pelo rubio dorado recogido arriba en rizos de caracola, con mechones de punta a los lados; un pendiente
# rosa en forma de rombo
GL2, PKE = _c('#f3c22d'), _c('#e06a8a')
C('rose-bedd', 'chica', P('#f3c22d', '#fce9b7', iris='#1e1414', shade='#c0821f'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=95, hairline=[(10, 62), (16, 50), (30, 44), (50, 42), (70, 44), (84, 50), (90, 62)]),
  [L(outline([(12, 64), (2, 52, 1), (10, 30), (24, 8), (50, 2), (76, 8), (90, 30), (104, 44, 1), (88, 64), (80, 48), (20, 48)])),
   L(ell(34, 4, 14, 12)), L(ell(62, 0, 16, 13)), strand([(30, 0), (36, -2), (36, 8), (28, 6)], 'shade', 'f', 1.2), strand([(58, -4), (66, -4), (66, 6), (56, 4)], 'shade', 'f', 1.2),
   L(outline([(84, 82), (88, 78), (92, 82), (88, 88)]), PKE, 'f')],
  [L(outline([(80, 48), (86, 28), (78, 4), (50, -2), (20, 4), (4, 26), (4, 58), (18, 72), (40, 72), (52, 56), (64, 48)])), L(ell(40, 0, 18, 14)),
   L(outline([(44, 82), (48, 78), (52, 82), (48, 88)]), PKE, 'f')],
  [L(outline([(10, 72), (6, 30), (24, 8), (50, 2), (76, 8), (94, 30), (90, 72), (50, 78)])), L(ell(34, 4, 14, 12)), L(ell(62, 0, 16, 13))])

# Rose Snelgrove: melena celeste muy clara de princesa con flequillo recto y mechones largos a los lados, recogida arriba
# con un lazo rojo; ojos rojos
LB, RD3 = _c('#ccebf7'), _c('#d02a2a')
C('rose-snelgrove', 'chica', P('#ccebf7', '#fbe8b8', iris='#b02020', shade='#a6a8ad', deep='#827c7d'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=95, hairline=[(8, 66), (14, 62), (30, 62), (50, 62), (70, 62), (86, 62), (92, 66)]),
  longhair('front', length=110, flare=2, fringe=64) + [L(outline([(36, -2), (24, -12), (24, 2)]), RD3, 'f'), L(outline([(64, -2), (76, -12), (76, 2)]), RD3, 'f'),
                                                        L(ell(50, -2, 6, 5), RD3, 'f')],
  longhair('side', length=110, flare=2) + [L(outline([(46, -4), (34, -14), (34, 2)]), RD3, 'f')],
  longhair('back', length=110, flare=2, ends=4) + [L(outline([(36, -2), (24, -12), (24, 2)]), RD3, 'f'), L(outline([(64, -2), (76, -12), (76, 2)]), RD3, 'f'),
                                                   L(ell(50, -2, 6, 5), RD3, 'f')])

# Rosy Roker: tupé morado peinado hacia arriba y hacia un lado, con los lados cortos; ojos azules afilados y media sonrisa
C('rosy-roker', 'chica', P('#895396', '#fce9b8', iris='#3a5aa8', shade='#6a4263', deep='#4d3742'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=95, face_front=face(chin=104), hairline=[(12, 58), (18, 44), (34, 34), (50, 30), (66, 40), (78, 54), (88, 62)]),
  [L(outline([(14, 58), (8, 28), (20, 0), (50, -10), (82, -4), (96, 20), (94, 48), (86, 66, 1), (80, 48), (66, 38), (40, 40), (20, 46)])),
   L(outline([(60, -8), (82, -4), (96, 20), (94, 46), (86, 62), (78, 40)]), 'shade', 'b', False),
   strand([(30, 4), (56, 10), (74, 36)], 'deep', 'b', 1.2)],
  [L(outline([(80, 44), (92, 26), (86, 0), (56, -12), (24, -6), (6, 18), (4, 50), (16, 70), (38, 72), (52, 56), (66, 46)])),
   strand([(30, 0), (60, 4), (84, 24)], 'deep', 'b', 1.2)],
  [L(outline([(12, 70), (6, 28), (20, 0), (50, -10), (82, -4), (96, 20), (92, 70), (50, 76)])),
   L(outline([(60, -8), (82, -4), (96, 20), (92, 66), (70, 72)]), 'shade', 'b', False)])

# Roy Diggins: gorra de repartidor verde con la visera naranja; ojos redondos blancos de dibujo, pecas y sonrisa
CAP, VIS = _c('#537d03'), _c('#e0a020')


def _cap(view):
    if view == 'front':
        return [L(outline([(4, 56), (2, 24), (20, 2), (50, -6), (80, 2), (98, 24), (96, 56)]), CAP),
                L(outline([(8, 52), (50, 46), (92, 52), (90, 62), (50, 58), (10, 62)]), VIS),
                strand([(50, -4), (50, 46)], _c('#3f4a07'), 'b', 1.0), strand([(28, 6), (24, 50)], _c('#3f4a07'), 'b', 1.0), strand([(72, 6), (76, 50)], _c('#3f4a07'), 'b', 1.0)]
    if view == 'side':
        return [L(outline([(2, 60), (0, 26), (18, 2), (50, -6), (80, 2), (96, 26), (96, 52), (60, 54), (20, 60)]), CAP),
                L(outline([(74, 50), (108, 54), (104, 62), (74, 60)]), VIS)]
    return [L(outline([(4, 60), (2, 24), (20, 2), (50, -6), (80, 2), (98, 24), (96, 60), (50, 64)]), CAP),
            strand([(50, -4), (50, 62)], _c('#3f4a07'), 'b', 1.0)]


C('roy-diggins', 'normal', P('#7a5a3a', '#f2be95', iris='#1e1414'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=95, hairline=False, nose=(50, 86, 2.2)),
  _cap('front') + [L(ell(36, 74, 8, 8), WHITE, 'f'), L(ell(64, 74, 8, 8), WHITE, 'f'), L(ell(38, 76, 2.4, 2.4), BLACK, 'f', False), L(ell(62, 76, 2.4, 2.4), BLACK, 'f', False)] +
  freckles(86, 26),
  _cap('side') + [L(ell(82, 74, 5, 7), WHITE, 'f'), L(ell(84, 76, 2, 2), BLACK, 'f', False)],
  _cap('back') + [L(outline([(14, 62), (86, 62), (82, 74), (18, 74)]), _c('#7a5a3a'))])

# Rudy Stemper: pelo azul marino con un caracol enroscado enorme en lo alto y los lados rapados; cejas gruesas negras y
# boca abierta riéndose
C('rudy-stemper', 'normal', P('#4f506a', '#fbc273', iris='#1e1414', shade='#413a43', deep='#2a2430'),
  F(eyes='sharp', brows=False, mouth='grin', mouth_y=96, hairline=[(14, 56), (22, 44), (34, 38), (50, 40), (66, 38), (78, 44), (86, 56)]),
  [L(outline([(16, 56), (12, 30), (24, 6), (40, -2), (50, -18), (68, -14), (72, 2), (82, 14), (88, 34), (84, 56), (78, 44), (22, 44)])),
   L(ell(58, -4, 9, 8), 'shade', 'b', False), L(ell(58, -4, 4, 3.6), 'deep', 'b', False)] + thick_brows(64, BLACK, 4.6, 15, 1.4, 16),
  [L(outline([(80, 44), (88, 28), (80, 4), (62, -12), (44, -16), (30, -4), (12, 14), (8, 40), (20, 60), (40, 62), (52, 52), (66, 46)])),
   L(ell(48, -4, 9, 8), 'shade', 'b', False)] + side_brow(64, BLACK, 4.6, 1.4),
  [L(outline([(14, 66), (10, 30), (24, 6), (40, -2), (50, -18), (68, -14), (72, 2), (82, 14), (90, 34), (86, 66), (50, 72)]))])

# Ruth Karnes: pelo azul claro recogido con dos trenzas que salen disparadas hacia los lados; ceño fruncido
C('ruth-karnes', 'chica', P('#719fc9', '#f4be94', iris='#1e1414', shade='#6183a5', deep='#5d636f'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=hl(4, 64, 48, 60, jit=2, seed=14)),
  dome('front', top=0, w=46, cy=44, sb=70) +
  [L(outline([(12, 80), (-10, 78), (-20, 70, 1), (-14, 82), (-24, 88, 1), (-6, 88), (10, 90)])),
   L(outline([(88, 80), (110, 78), (120, 70, 1), (114, 82), (124, 88, 1), (106, 88), (90, 90)]))],
  dome('side', top=0, w=46, cy=44, nape=86, fr=50) + [L(outline([(30, 80), (8, 76), (-6, 70, 1), (0, 84), (-8, 94, 1), (12, 90), (32, 90)]))],
  dome('back', top=0, w=46, cy=44, nape=86) +
  [L(outline([(12, 80), (-10, 78), (-20, 70, 1), (-14, 82), (-24, 88, 1), (-6, 88), (10, 90)])),
   L(outline([(88, 80), (110, 78), (120, 70, 1), (114, 82), (124, 88, 1), (106, 88), (90, 90)]))])

# Ryan Haywood: cabeza dentro de un robot cuadrado gris con discos naranjas a los lados; por una ventana se le ve la cara
# con un poco de pelo verde; tres botones naranjas debajo
BX, BO = _c('#a29c85'), _c('#ea910a')
C('ryan-haywood', 'normal', P('#5a9a3a', '#f6af6a', iris='#1e1414'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, face_front=blob([(26, 50), (74, 50), (74, 84), (26, 84)], 4)),
  [L(outline([(2, 116), (0, 10), (10, 0), (90, 0), (100, 10), (98, 116), (60, 120), (40, 120)]), BX, 'b'),
   L(outline([(26, 50), (74, 50), (74, 84), (26, 84)]), _c('#f6af6a'), 'b', False),
   L(outline([(28, 52), (72, 52), (66, 60), (34, 60)]), _c('#5a9a3a'), 'f', False),
   L(ell(40, 70, 3, 3.4), BLACK, 'f', False), L(ell(60, 70, 3, 3.4), BLACK, 'f', False),
   L([(34, 63), (44, 66)], BLACK, 'f', False, False, 1.6), L([(66, 63), (56, 66)], BLACK, 'f', False, False, 1.6),
   L(ell(50, 78, 2.2, 1.6), _c('#c87a4a'), 'f', False),
   L(ell(-6, 60, 7, 12), BO, 'f'), L(ell(106, 60, 7, 12), BO, 'f'),
   L(ell(30, 100, 6, 6), BO, 'f'), L(ell(50, 100, 6, 6), BO, 'f'), L(ell(70, 100, 6, 6), BO, 'f')],
  [L(outline([(2, 116), (0, 10), (10, 0), (90, 0), (100, 10), (98, 116)]), BX, 'f'), L(ell(50, 60, 7, 12), BO, 'f'), L(ell(100, 100, 3, 6), BO, 'f')],
  [L(outline([(2, 116), (0, 10), (10, 0), (90, 0), (100, 10), (98, 116)]), BX, 'f'), L(ell(-6, 60, 7, 12), BO, 'f'), L(ell(106, 60, 7, 12), BO, 'f')])

# Ryan O'Laugh: pelo azul petróleo peinado hacia atrás con dos picos que salen a los lados por arriba y patillas finas;
# orejas grandes, ojos blancos de mala uva
C('ryan-o-laugh', 'normal', P('#4c6b76', '#f4be94', iris='#1e1414', shade='#3e4448'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=96, big_ears=2, ear_out=2, face_front=face(chin=106), face_side=face_side(chin=5),
    hairline=[(12, 74), (16, 50), (30, 40), (50, 38), (70, 40), (84, 50), (88, 74)]),
  [L(outline([(14, 74), (10, 44), (2, 14, 1), (18, 20), (30, 4), (50, 0), (70, 4), (86, 14), (104, 4, 1), (92, 30), (88, 74), (82, 46), (18, 46)])),
   L(outline([(60, 2), (86, 14), (100, 6), (92, 30), (86, 60), (76, 30)]), 'shade', 'b', False)],
  [L(outline([(80, 44), (88, 26), (96, 8, 1), (76, 6), (50, -2), (22, 4), (6, 24), (6, 58), (20, 76), (40, 76), (52, 60), (66, 46)]))],
  [L(outline([(12, 74), (10, 44), (2, 14, 1), (18, 20), (30, 4), (50, 0), (70, 4), (86, 14), (104, 4, 1), (92, 30), (90, 74), (50, 80)]))])

# Sable Tatter: melena castaña larga con dos trenzas gruesas por delante y una cinta clara en la frente; piel morena,
# ojos ámbar, una marca roja en la mejilla y labios rojos
HDB, SCR = _c('#e8c8b0'), _c('#c82a3a')
C('sable-tatter', 'chica', P('#563c31', '#cb986f', iris='#a8701a', shade='#452c24', deep='#361e14', skin_d='#96624c'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=95, hairline=[(8, 66), (14, 50), (28, 42), (40, 38), (56, 42), (72, 44), (86, 50), (92, 66)]),
  longhair('front', length=100, flare=2) +
  [L(outline([(10, 52), (50, 44), (90, 52), (90, 58), (50, 50), (10, 58)]), HDB, 'f'),
   L(outline([(16, 96), (10, 110), (16, 124), (12, 136, 1), (22, 124), (24, 108)])), L(outline([(84, 96), (90, 110), (84, 124), (88, 136, 1), (78, 124), (76, 108)])),
   L(outline([(24, 84), (32, 82), (28, 90)]), SCR, 'f', False)],
  longhair('side', length=100, flare=2) + [L(outline([(10, 44), (88, 46), (88, 51), (10, 50)]), HDB, 'f'), L(outline([(52, 96), (46, 112), (52, 128, 1), (58, 110)]))],
  longhair('back', length=100, flare=2, ends=3) + [L(outline([(12, 52), (88, 52), (88, 57), (12, 57)]), HDB, 'f')])

# Sabrina Carow: melena morada en casco liso con raya en medio que baja en pico por la frente y le cae en punta bajo la
# barbilla; sombra lila en los ojos rojos, piel muy clara
C('sabrina-carow', 'chica', P('#985976', '#f6ebca', iris='#a01e1e', shade='#763a4b', deep='#5c2b36'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=95, hairline=[(8, 70), (14, 52), (28, 40), (44, 44), (50, 56), (56, 44), (72, 40), (86, 52), (92, 70)]),
  [L(outline([(10, 112, 1), (2, 70), (6, 34), (24, 8), (50, 0), (76, 8), (94, 34), (98, 70), (90, 112, 1), (80, 82), (80, 60), (20, 60), (20, 82)])),
   L(outline([(60, 4), (80, 10), (94, 36), (96, 70), (90, 104), (82, 70)]), 'shade', 'b', False), strand([(50, 2), (50, 50)], 'deep', 'b', 1.2),
   L([(28, 70), (44, 70)], _c('#c8a0d8'), 'f', False, False, 2.4), L([(56, 70), (72, 70)], _c('#c8a0d8'), 'f', False, False, 2.4)],
  [L(outline([(80, 48), (88, 28), (78, 4), (50, -2), (20, 4), (4, 30), (2, 70), (14, 110, 1), (30, 90), (52, 66), (66, 50)]))],
  [L(outline([(10, 112, 1), (2, 70), (6, 34), (24, 8), (50, 0), (76, 8), (94, 34), (98, 70), (90, 112, 1), (50, 96)])),
   L(outline([(60, 4), (80, 10), (94, 36), (96, 70), (88, 104), (66, 96)]), 'shade', 'b', False)])

# Sabrina Passman: pelo verde menta voluminoso echado a un lado en una ola grande con un mechón de punta hacia arriba;
# ojos con estrellas amarillas y sonrisa
C('sabrina-passman', 'chica', P('#5fb08a', '#f5bf96', iris='#e8c030', shade='#567661', deep='#435145'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=95, hairline=hl(4, 66, 50, 62, lean=-3, jit=2, seed=15)),
  [L(outline([(8, 90), (-4, 60), (-2, 26), (14, 4), (44, -6), (72, -4), (88, -26, 1), (86, 6), (96, 30), (96, 70), (88, 88), (82, 56), (20, 50), (16, 80)])),
   L(outline([(60, -4), (86, 4), (96, 30), (94, 66), (86, 84), (78, 40)]), 'shade', 'b', False),
   fr([(12, 40), (40, 28), (62, 32), (50, 44), (30, 54), (14, 74, 1)])],
  [L(outline([(80, 50), (92, 30), (86, 4), (72, -24, 1), (66, 0), (40, -6), (8, 6), (-6, 40), (2, 80), (20, 84), (40, 74), (52, 58), (66, 50)]))],
  [L(outline([(6, 88), (-4, 60), (-2, 26), (14, 4), (44, -6), (72, -4), (88, -26, 1), (86, 6), (96, 30), (96, 78), (50, 84)]))])

# Sadey Stewer: melena castaña gris lisa y larga echada a un lado que le tapa medio rostro, con un mechón curvo
# levantado arriba; ojo morado de pintura alrededor del ojo visible
PU = _c('#7a3a9a')
C('sadey-stewer', 'chica', P('#5d4a49', '#f9bc7c', iris='#2a1414', shade='#4c3b39'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=95, hairline=[(8, 66), (14, 50), (30, 40), (50, 38), (66, 42), (80, 50), (92, 66)]),
  bowl('front', top=2, side=96, w=2) +
  [fr([(10, 40), (30, 26), (56, 26), (60, 50), (56, 96), (50, 104, 1), (40, 90), (16, 80)]),
   L(outline([(30, 10), (20, -8), (10, -16, 1), (22, -6), (34, 2)])),
   L(ell(66, 76, 9, 7), PU, 'b', False)],
  bowl('side', top=2, nape=96, w=2) + [L(outline([(30, 4), (20, -12), (10, -18, 1), (24, -6), (36, 0)]))],
  bowl('back', top=2, nape=96, w=2) + [L(outline([(30, 10), (20, -8), (10, -16, 1), (22, -6), (34, 2)]))])

# Sally Tare: pelo verde petróleo recogido en un moño alto, con un mechón largo que cae por la sien; orejas de punta,
# ojos rojos afilados y ceño fruncido
C('sally-tare', 'chica', P('#4f7d6f', '#fccf9f', iris='#a02040', shade='#455047', deep='#32302d'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, big_ears=1, ear_out=2, hairline=[(12, 62), (18, 48), (30, 42), (50, 40), (70, 42), (82, 48), (88, 62)]),
  [L(outline([(14, 62), (10, 30), (22, 8), (50, 2), (78, 8), (90, 30), (86, 62), (80, 48), (20, 48)])),
   L(outline([(50, 4), (40, -14), (60, -22), (80, -10), (70, 6)])),
   fr([(14, 40), (24, 38), (22, 70), (18, 90, 1), (12, 66)])],
  [L(outline([(80, 48), (86, 28), (78, 4), (50, -2), (20, 4), (4, 26), (4, 58), (18, 72), (40, 72), (52, 56), (64, 48)])),
   L(outline([(40, 4), (32, -14), (52, -22), (66, -10), (58, 6)]))],
  [L(outline([(12, 72), (8, 30), (22, 8), (50, 2), (78, 8), (92, 30), (88, 72), (50, 78)])), L(outline([(50, 4), (40, -14), (60, -22), (80, -10), (70, 6)]))])

# Sam Banks: cabeza redonda enorme con pelo rojo oscuro en pinchos cortos alrededor; cejas negras gruesas, ojos
# pequeños, nariz de cerdito y sonrisa
NS = _c('#f0a070')
C('sam-banks', 'corpulento', P('#9e0a0b', '#fabb7a', iris='#1e1414', shade='#721914'),
  F(eyes='dot', brows=False, mouth='smile', mouth_y=100, face_front=blob([(10, 54), (50, 40), (90, 54), (98, 82), (88, 106), (50, 118), (12, 106), (2, 82)], 8),
    face_side=face_side(chin=10, jaw=8), hairline=hl(6, 60, 50, 56, jit=2, seed=16), eye_y=74),
  dome('front', top=4, w=50, cy=46, n=14, amp=8, seed=25, sb=62) + thick_brows(64, BLACK, 4.6, 16, 0.8, 14) +
  [L(ell(50, 88, 9, 7), NS, 'f'), L(ell(46, 88, 1.6, 2.2), _c('#7a3a20'), 'f', False), L(ell(54, 88, 1.6, 2.2), _c('#7a3a20'), 'f', False)],
  dome('side', top=4, w=50, cy=46, n=14, amp=8, seed=25, nape=82, fr=48) + side_brow(64, BLACK, 4.6, 0.8) + [L(ell(92, 88, 5, 6), NS, 'f')],
  dome('back', top=4, w=50, cy=46, n=14, amp=8, seed=25, nape=82))

# Sam Willing: pelo castaño con flequillo de mechones y un pico de punta arriba; ojos cerrados y una mascarilla azul
# marino con una boca roja dibujada, atada detrás
MK, MR2 = _c('#3a3c5a'), _c('#c82a2a')
C('sam-willing', 'normal', P('#5b412d', '#f2efd3', iris='#1e1414', shade='#432b1e'),
  F(eyes='closed', brows=True, mouth='none', hairline=hl(5, 66, 50, 62, jit=3, seed=17)),
  dome('front', top=2, w=48, cy=44, sb=72) + [L(outline([(36, 4), (6, -4, 1), (40, -6)])),
                                              L(outline([(18, 84), (50, 82), (82, 84), (80, 100), (50, 108), (20, 100)]), MK, 'f'),
                                              L(outline([(10, 86), (-6, 80, 1), (-2, 92, 1), (14, 92)]), MK, 'f'),
                                              L(quad((38, 94), (50, 102), (62, 94)), MR2, 'f', False, False, 2.4), L(ell(50, 92, 3, 3), MR2, 'f', False)],
  dome('side', top=2, w=48, cy=44, nape=86, fr=52) + [L(outline([(60, 82), (90, 82), (92, 98), (80, 106), (60, 100)]), MK, 'f'), L([(60, 88), (40, 82)], MK, 'f', False, False, 1.6)],
  dome('back', top=2, w=48, cy=44, nape=86) + [L(outline([(44, 84), (56, 84), (64, 96, 1), (50, 90), (36, 96, 1)]), MK, 'f')])

# Sandra Mudd: melena castaña con flequillo recto y dos coletitas cortas a los lados, con una cinta ancha rosa en la
# cabeza; ojos negros y sonrisa
HBP = _c('#d48078')
C('sandra-mudd', 'chica', P('#5e4436', '#eabba3', iris='#1e1414', shade='#452f25'),
  F(eyes='round', brows=False, mouth='smile', mouth_y=94, hairline=[(8, 66), (14, 62), (30, 62), (50, 62), (70, 62), (86, 62), (92, 66)]),
  bowl('front', top=2, side=84) + [L(outline([(10, 36), (50, 22), (90, 36), (92, 46), (50, 32), (8, 46)]), HBP, 'f'),
                                   L(outline([(8, 76), (-6, 82), (-6, 100, 1), (8, 92)])), L(outline([(92, 76), (106, 82), (106, 100, 1), (92, 92)]))],
  bowl('side', top=2, nape=88) + [L(outline([(12, 26), (80, 22), (88, 30), (88, 38), (12, 35)]), HBP, 'f'), L(outline([(20, 74), (8, 84), (10, 100, 1), (24, 88)]))],
  bowl('back', top=2, nape=88) + [L(outline([(10, 40), (90, 40), (90, 48), (10, 48)]), HBP, 'f'),
                                  L(outline([(8, 76), (-6, 82), (-6, 100, 1), (8, 92)])), L(outline([(92, 76), (106, 82), (106, 100, 1), (92, 92)]))])

# Scott Tickle: pinchos naranjas en llamas hacia arriba; cara pintada de blanco de payaso con dos rayas verdes que le
# bajan por los ojos y labios verdes
WP, GP = _c('#fdf8e1'), _c('#7a9a3a')
C('scott-tickle', 'normal', P('#d65c22', '#a87a5a', iris='#1e1414', shade='#8a371c'),
  F(eyes='none', brows=False, mouth='none', hairline=hl(6, 64, 48, 56, jit=2, seed=18)),
  dome('front', top=-12, w=46, cy=42, n=8, amp=18, seed=26, sb=62) +
  [L(outline([(22, 50), (50, 44), (78, 50), (80, 80), (70, 100), (50, 108), (30, 100), (20, 80)]), WP, 'f', False),
   L([(36, 56), (34, 90)], GP, 'f', False, False, 2.4), L([(64, 56), (66, 90)], GP, 'f', False, False, 2.4),
   L(blob([(28, 74), (36, 70), (44, 74), (36, 78)], 6), GP, 'f', False), L(blob([(72, 74), (64, 70), (56, 74), (64, 78)], 6), GP, 'f', False),
   L(ell(37, 74, 2, 2), BLACK, 'f', False), L(ell(63, 74, 2, 2), BLACK, 'f', False),
   L(blob([(40, 96), (50, 92), (60, 96), (50, 100)], 6), GP, 'f')],
  dome('side', top=-12, w=46, cy=42, n=8, amp=18, seed=26, nape=84, fr=48) +
  [L(outline([(70, 46), (86, 50), (90, 80), (82, 104), (66, 104)]), WP, 'f', False), L([(80, 56), (80, 90)], GP, 'f', False, False, 2.4)],
  dome('back', top=-12, w=46, cy=42, n=8, amp=18, seed=26, nape=84))

# Selma Heaver (portera): pelo granate en pinchos gruesos echados hacia arriba y atrás; piel morena, ojos entornados y
# sonrisa de dientes
C('selma-heaver', 'chica', P('#69292d', '#dca259', iris='#1e1414', shade='#542222', skin_d='#a57045'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=95, hairline=hl(5, 64, 48, 56, jit=2, seed=19)),
  dome('front', top=-8, w=48, cy=42, n=7, amp=14, sweep=0.4, seed=27, sb=64),
  dome('side', top=-8, w=48, cy=42, n=7, amp=14, sweep=0.4, seed=27, nape=84, fr=48),
  dome('back', top=-8, w=48, cy=42, n=7, amp=14, sweep=0.4, seed=27, nape=84))

# Serena Besse: melena corta gris con un mechón grande barrido sobre la frente y puntas hacia dentro bajo la barbilla;
# ojos granates grandes y sonrisa
C('serena-besse', 'chica', P('#757e7c', '#fabc7e', iris='#8a1e2e', shade='#625051', deep='#493d3b'),
  F(eyes='round', brows='angry', mouth='smile', mouth_y=94, hairline=[(8, 66), (14, 52), (28, 44), (40, 50), (56, 40), (72, 44), (86, 52), (92, 66)]),
  bowl('front', top=0, side=98, w=2) + [fr([(16, 40), (40, 30), (66, 30), (52, 40), (38, 54, 1), (28, 52)])],
  bowl('side', top=0, nape=96, w=2),
  bowl('back', top=0, nape=96, w=2))

# Shaun Bonnie: pelo oliva corto con raya en medio que baja en dos mechones; gafas ovaladas negras, ojos morados y sonrisa
C('shaun-bonnie', 'normal', P('#6f674d', '#f8bc7e', iris='#8a3aa8', shade='#483b2f'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=95, hairline=[(10, 62), (16, 48), (30, 42), (44, 46), (50, 56), (56, 46), (70, 42), (84, 48), (90, 62)]),
  dome('front', top=2, w=46, cy=44, sb=66) + [strand([(50, 4), (46, 30), (38, 56)], 'deep', 'f', 1.2), strand([(50, 4), (54, 30), (62, 56)], 'deep', 'f', 1.2)] +
  round_specs('front', BLACK, 77, 15, 10, 6, 1.4),
  dome('side', top=2, w=46, cy=44, nape=84, fr=46) + round_specs('side', BLACK, 77, 15, 10, 6, 1.4),
  dome('back', top=2, w=46, cy=44, nape=84))

# Shay Diebold: lleva en la cabeza un cubo de tela blanco rosado con una raja negra y un ojo rojo, bajo un sombrero de
# paja; solo se le ve la boca sonriente
STRW, CLOTH = _c('#d2af47'), _c('#e8d8da')
C('shay-diebold', 'normal', P('#2a1e18', '#97614e', iris='#1e1414'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=96, hairline=False, ears=False),
  [L(outline([(2, 86), (4, 20), (96, 20), (98, 86)]), CLOTH, 'f'),
   L(outline([(-14, 24), (10, 4), (50, -6), (90, 4), (114, 24), (50, 30)]), STRW, 'f'),
   L(outline([(50, 22), (54, 50), (48, 86, 1), (44, 50)]), BLACK, 'f'), L(ell(48, 60, 4, 4), _c('#e01e1e'), 'f', False),
   strand([(20, 40), (18, 82)], _c('#b28e90'), 'f', 1.0), strand([(80, 40), (82, 82)], _c('#b28e90'), 'f', 1.0)],
  [L(outline([(2, 92), (4, 20), (96, 20), (98, 92)]), CLOTH, 'f'), L(outline([(-14, 24), (10, 4), (50, -6), (90, 4), (114, 24), (50, 30)]), STRW, 'f')],
  [L(outline([(2, 92), (4, 20), (96, 20), (98, 92)]), CLOTH, 'f'), L(outline([(-14, 24), (10, 4), (50, -6), (90, 4), (114, 24), (50, 30)]), STRW, 'f')])

# Sherlock Sagers (portero): pelo negro azulado aplastado en un disco ancho y plano que sobresale mucho por los lados,
# con un pico en la frente; cara larga, ojos blancos y sonrisa enorme de dientes
C('sherlock-sagers', 'delgado', P('#37434b', '#dcb177', iris='#f0f0f0', shade='#2a2a2a', skin_d='#ad7241'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=98, mouth_w=14, face_front=face(chin=110, jaw=-2), face_side=face_side(chin=9),
    hairline=[(16, 58), (24, 44), (40, 38), (50, 50), (60, 38), (76, 44), (84, 58)]),
  [L(outline([(16, 58), (12, 34), (-16, 26), (-22, 14, 1), (0, 4), (50, -4), (100, 4), (122, 14, 1), (116, 26), (88, 34), (84, 58), (78, 44), (22, 44)])),
   L(outline([(50, -2), (100, 4), (120, 14), (114, 24), (86, 30)]), 'shade', 'b', False),
   L(blob([(28, 72), (36, 68), (44, 74), (36, 78)], 6), WHITE, 'f'), L(blob([(72, 72), (64, 68), (56, 74), (64, 78)], 6), WHITE, 'f'),
   L([(26, 64), (44, 70)], BLACK, 'f', False, False, 2.2), L([(74, 64), (56, 70)], BLACK, 'f', False, False, 2.2)],
  [L(outline([(78, 44), (88, 28), (110, 20), (112, 8, 1), (60, -6), (0, 0), (-14, 14, 1), (4, 24), (6, 50), (20, 64), (40, 64), (52, 52), (64, 46)])),
   L(blob([(76, 72), (86, 70), (86, 78), (78, 78)], 6), WHITE, 'f')],
  [L(outline([(14, 64), (12, 34), (-16, 26), (-22, 14, 1), (0, 4), (50, -4), (100, 4), (122, 14, 1), (116, 26), (88, 34), (86, 64), (50, 70)]))])

# Shirly Quirk: melena granate lisa con un flequillo largo y recto que le tapa los ojos, y mechones hasta los hombros;
# solo se le ve una sonrisa con un colmillo
C('shirly-quirk', 'chica', P('#753f42', '#f3efd2', iris='#1e1414', shade='#593232', deep='#3b2526'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=95, hairline=[(8, 82), (14, 80), (30, 80), (50, 80), (70, 80), (86, 80), (92, 82)]),
  longhair('front', length=104, flare=0, fringe=82),
  longhair('side', length=104, flare=0) + [fr([(66, 40), (92, 44), (94, 80), (70, 80)])],
  longhair('back', length=104, flare=0, ends=3))

# Shona Shopbell (portera): melena castaña con puntas hacia fuera a la altura de la barbilla y un flequillo grande que le
# tapa un ojo; boquita naranja redonda
C('shona-shopbell', 'chica', P('#784942', '#fbd18c', iris='#1e1414', shade='#60352d', light='#885e55'),
  F(eyes='round', brows=False, mouth='none', hairline=[(8, 66), (14, 52), (30, 42), (50, 40), (66, 44), (82, 52), (92, 66)]),
  bowl('front', top=0, side=90, w=4) +
  [L(outline([(6, 84), (-8, 94, 1), (8, 94)])), L(outline([(94, 84), (108, 94, 1), (92, 94)])),
   fr([(14, 40), (40, 26), (64, 30), (60, 50), (48, 82, 1), (34, 66), (18, 60)]),
   L(ell(50, 96, 3, 3.4), _c('#e8902a'), 'f'), L(ell(50, 96, 1.2, 1.4), _c('#6a2a14'), 'f', False)],
  bowl('side', top=0, nape=92, w=4) + [L(outline([(8, 86), (-6, 96, 1), (12, 94)]))],
  bowl('back', top=0, nape=92, w=4) + [L(outline([(6, 88), (-8, 98, 1), (10, 96)])), L(outline([(94, 88), (108, 98, 1), (90, 96)]))])

# Shu Maimai: pelo castaño anaranjado recogido atrás con una trenza gruesa que le cae por el hombro; ojos verdes afilados
C('shu-maimai', 'chica', P('#b5621f', '#f6ddaf', iris='#2a8a6a', shade='#93460c', deep='#6a3008'),
  F(eyes='sharp', brows=True, mouth='line', mouth_y=95, face_front=face(chin=104), hairline=[(10, 62), (16, 48), (30, 40), (50, 38), (70, 40), (84, 48), (90, 62)]),
  dome('front', top=0, w=46, cy=44, sb=66) + [L(outline([(16, 86), (10, 102), (16, 116), (10, 128, 1), (22, 116), (24, 98)]))],
  dome('side', top=0, w=46, cy=44, nape=84, fr=46) + tail('side', side_len=120),
  dome('back', top=0, w=46, cy=44, nape=84) + tail('back', side_len=124, x=40))

# Sim Cebus (portero): salacot beige con una banda más oscura; pelo granate asomando a los lados, ojos negros redondos
# enormes y sonrisa
HT, HB2 = _c('#debc86'), _c('#ae8c63')


def _helmet(view):
    if view == 'front':
        return [L(outline([(-2, 58), (6, 46), (8, 22), (26, 2), (50, -4), (74, 2), (92, 22), (94, 46), (102, 58), (50, 62)]), HT),
                L(outline([(8, 32), (50, 28), (92, 32), (93, 46), (50, 42), (7, 46)]), HB2, 'b', False),
                strand([(50, -2), (50, 28)], HB2, 'b', 1.0), strand([(30, 4), (24, 30)], HB2, 'b', 1.0), strand([(70, 4), (76, 30)], HB2, 'b', 1.0)]
    if view == 'side':
        return [L(outline([(-8, 62), (2, 48), (4, 22), (24, 2), (52, -4), (78, 4), (94, 26), (96, 48), (106, 60), (50, 62)]), HT),
                L(outline([(4, 34), (94, 32), (95, 46), (3, 48)]), HB2, 'b', False)]
    return [L(outline([(-2, 62), (6, 46), (8, 22), (26, 2), (50, -4), (74, 2), (92, 22), (94, 46), (102, 62), (50, 66)]), HT),
            L(outline([(8, 32), (92, 32), (93, 46), (7, 46)]), HB2, 'b', False)]


C('sim-cebus', 'normal', P('#a83a3a', '#f0b878', iris='#1e1414'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=95, hairline=False, nose=(50, 86, 2.4)),
  _helmet('front') + [L(outline([(12, 60), (8, 76), (18, 72)])), L(outline([(88, 60), (92, 76), (82, 72)])),
                      L(ell(36, 74, 8, 8), WHITE, 'f'), L(ell(64, 74, 8, 8), WHITE, 'f'), L(ell(36, 75, 4, 4.6), BLACK, 'f', False), L(ell(64, 75, 4, 4.6), BLACK, 'f', False)],
  _helmet('side') + [L(outline([(44, 60), (40, 76), (52, 70)])), L(ell(82, 74, 5, 7), WHITE, 'f'), L(ell(84, 75, 2.6, 3.6), BLACK, 'f', False)],
  _helmet('back') + [L(outline([(14, 62), (86, 62), (82, 76), (18, 76)]), _c('#a83a3a'))])

# Simeon Squareyes: pelo amarillo en pinchos grandes con un mechón que cae por la cara; gafas de buceo grises con
# cristales verdes oscuros y sonrisa de dientes
YL, GG, GLS = _c('#c7bc2d'), _c('#b8bcc0'), _c('#3c442f')
C('simeon-squareyes', 'normal', P('#c7bc2d', '#d3c2b5', iris='#1e1414', shade='#997e23'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=96, hairline=hl(5, 64, 48, 58, jit=2, seed=20)),
  dome('front', top=-10, w=52, cy=42, n=8, amp=16, seed=28, sb=66) +
  [L(outline([(12, 70), (50, 64), (88, 70), (88, 84), (50, 82), (12, 84)]), GG, 'f'),
   L(blob([(20, 72), (44, 70), (44, 82), (22, 82)], 6), GLS, 'f', False), L(blob([(80, 72), (56, 70), (56, 82), (78, 82)], 6), GLS, 'f', False),
   fr([(54, 40), (66, 40), (72, 70), (78, 92, 1), (62, 72)])],
  dome('side', top=-10, w=52, cy=42, n=8, amp=16, seed=28, nape=86, fr=50) +
  [L(outline([(62, 68), (92, 68), (92, 84), (62, 84)]), GG, 'f'), L(blob([(74, 70), (90, 70), (90, 82), (76, 82)], 6), GLS, 'f', False)],
  dome('back', top=-10, w=52, cy=42, n=8, amp=16, seed=28, nape=86) + [L(outline([(6, 72), (94, 72), (94, 78), (6, 78)]), GG, 'f')])

# Siria Chattsley: capucha rosa con dos orejas redondas de ratón; flequillo castaño, ojos verdes y una mascarilla crema
# con una boca de animalito dibujada
HOOD, EAR, MASK = _c('#d57771'), _c('#f0c8c0'), _c('#eadac7')
C('siria-chattsley', 'chica', P('#854d3a', '#f0bd96', iris='#3a8a5a', shade='#5b3123'),
  F(eyes='round', brows='angry', mouth='none', hairline=hl(4, 66, 50, 60, jit=2, seed=21)),
  [L(outline([(-4, 96), (0, 40), (16, 10), (50, 0), (84, 10), (100, 40), (104, 96), (88, 92), (84, 56), (16, 56), (12, 92)]), HOOD),
   L(ell(6, 6, 14, 13), EAR), L(ell(94, 6, 14, 13), EAR),
   L(outline([(16, 54), (14, 40), (30, 30), (50, 28), (70, 30), (86, 40), (84, 54)])),
   L(outline([(22, 82), (50, 80), (78, 82), (76, 100), (50, 106), (24, 100)]), MASK, 'f'),
   L(quad((44, 92), (50, 96), (56, 92)), BLACK, 'f', False, False, 1.2), L([(50, 88), (50, 94)], BLACK, 'f', False, False, 1.2)],
  [L(outline([(52, 98), (30, 104), (2, 90), (0, 40), (16, 10), (50, 0), (84, 10), (96, 34), (96, 52), (70, 54), (60, 70)]), HOOD), L(ell(40, 0, 14, 13), EAR),
   L(outline([(62, 82), (90, 82), (92, 98), (66, 102)]), MASK, 'f')],
  [L(outline([(-4, 98), (0, 40), (16, 10), (50, 0), (84, 10), (100, 40), (104, 98), (50, 104)]), HOOD), L(ell(6, 6, 14, 13), EAR), L(ell(94, 6, 14, 13), EAR)])

# Skeet Blaston: pinchos azul petróleo largos en todas direcciones; cara pintada de payaso blanco con sombra celeste en
# los ojos, nariz naranja y una sonrisa enorme roja
CL, CB, CN = _c('#f4f0e4'), _c('#9ed3e2'), _c('#e0702a')
C('skeet-blaston', 'normal', P('#42899b', '#c88a5a', iris='#1e1414', shade='#39555c'),
  F(eyes='none', brows=False, mouth='none', hairline=hl(6, 62, 48, 56, jit=3, seed=22)),
  dome('front', top=-10, w=52, cy=42, n=9, amp=22, seed=29, sb=60) +
  [L(outline([(20, 52), (50, 46), (80, 52), (82, 80), (72, 104), (50, 110), (28, 104), (18, 80)]), CL, 'f', False),
   L(blob([(26, 72), (36, 64), (46, 72), (36, 80)], 6), CB, 'f', False), L(blob([(74, 72), (64, 64), (54, 72), (64, 80)], 6), CB, 'f', False),
   L([(30, 74), (42, 72)], BLACK, 'f', False, False, 1.6), L([(70, 74), (58, 72)], BLACK, 'f', False, False, 1.6),
   L(ell(50, 86, 6, 4), CN, 'f'), L(quad((32, 94), (50, 108), (68, 94)), _c('#c82a2a'), 'f', False, False, 3.0)],
  dome('side', top=-10, w=52, cy=42, n=9, amp=22, seed=29, nape=82, fr=46) +
  [L(outline([(68, 48), (86, 52), (92, 80), (84, 104), (64, 104)]), CL, 'f', False), L(ell(92, 86, 4, 4), CN, 'f')],
  dome('back', top=-10, w=52, cy=42, n=9, amp=22, seed=29, nape=82))
