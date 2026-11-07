"""Ojeadores de IE1 (scouts-ie1), tanda 07: dibujados a partir de su retrato de Victory Road (ninguno tiene modelo 3D en la
enciclopedia); claves 'scouts-ie1:<id>'. El perfil y la espalda están deducidos del peinado del retrato."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, longhair, messy, outline, pal, rope, strand  # noqa: F401
from chars_bigwaves import rect_glasses
from chars_vr_keizen_arashiyama import cloud, fr
from chars_vr_meiran_gakuin import bangs, long_back, long_front, long_side
from chars_vr_nikogawa import WIDE, blush, brow_side, brows, crop, ring_glasses
from heads import quad  # noqa: F401

K = 'scouts-ie1:'
WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)
RED = (200, 50, 40, 255)
SKIN = {'pale': '#f8d2a8', 'light': '#f6c290', 'tan': '#eeb07a', 'med': '#d8975e', 'dark': '#b87a48', 'deep': '#9a6238'}
CHUB = blob([(15, 50), (50, 30), (85, 50), (92, 78), (86, 98), (66, 108), (50, 110), (34, 108), (14, 98), (8, 78)])
LONGF = blob([(19, 50), (50, 28), (81, 50), (82, 80), (74, 100), (58, 108), (50, 109), (42, 108), (26, 100), (18, 80)])


def S(pid, body, hair, skin, iris='#302232', face=None, front=(), side=(), back=(), **extra):
    CHARS[K + pid] = {'body': body, 'pal': pal(hair, SKIN.get(skin, skin), iris=iris, **extra), 'face': face or {},
                      'front': list(front), 'side': list(side), 'back': list(back)}


def three(fn, **kw):
    """Las tres vistas de un peinado hecho con una función (vista, **kw)."""
    return {v: fn(v, **kw) for v in ('front', 'side', 'back')}


def spikes(view, **kw):
    return messy(view, **kw)


def tuft(pts, c='mid', z='b'):
    return L(outline(pts), c, z)


def side_tufts(view, y=60, c='mid'):
    """Pinchitos cortos que asoman por los lados (patillas en punta)."""
    if view == 'front':
        return [tuft([(16, y - 12), (6, y, 1), (16, y + 2), (10, y + 10, 1), (18, y + 8)], c),
                tuft([(84, y - 12), (94, y, 1), (84, y + 2), (90, y + 10, 1), (82, y + 8)], c)]
    if view == 'back':
        return [tuft([(16, y - 12), (6, y, 1), (16, y + 2), (10, y + 10, 1), (18, y + 8)], c),
                tuft([(84, y - 12), (94, y, 1), (84, y + 2), (90, y + 10, 1), (82, y + 8)], c)]
    return []


def headband(view, y=50, c='band', h=9):
    if view == 'front':
        return [L(outline([(13, y), (50, y - 4), (87, y), (87, y + h), (50, y + h - 4), (13, y + h)]), c, 'f')]
    if view == 'side':
        return [L(outline([(10, y - 6), (52, y - 6), (88, y - 2), (88, y + h - 2), (52, y + h - 6), (8, y + h - 4)]), c, 'f')]
    return [L(outline([(10, y + 2), (50, y), (90, y + 2), (90, y + h + 2), (50, y + h), (10, y + h + 2)]), c, 'f')]


def ballcap(view, c='capc', brim='brim', top=0):
    """Gorra de béisbol con la visera hacia delante."""
    if view == 'front':
        return [L(outline([(12, 56), (12, 34), (24, 14 + top), (50, 6 + top), (76, 14 + top), (88, 34), (88, 56), (50, 52)]), c, 'f'),
                L(outline([(8, 56), (50, 50), (92, 56), (90, 64), (50, 60), (10, 64)]), brim, 'f')]
    if view == 'side':
        return [L(outline([(6, 60), (4, 34), (18, 12 + top), (48, 4 + top), (76, 12 + top), (88, 34), (90, 50), (40, 54)]), c, 'f'),
                L(outline([(80, 46), (108, 52), (110, 58), (82, 56)]), brim, 'f')]
    return [L(outline([(10, 64), (10, 34), (24, 12 + top), (50, 4 + top), (76, 12 + top), (90, 34), (90, 64), (50, 60)]), c, 'f'),
            L(outline([(40, 58), (60, 58), (60, 64), (40, 64)]), brim, 'f')]


# ------------------------------------------------------------------ hoja 0

# Julian Siezer: pelo azul marino en seta con flequillo grueso hasta las cejas; ojos verdes afilados; boca grande de labios
h = three(crop, top=6, side=62, nape=84, w=4)
S('julian-siezer', 'normal', '#2c4766', 'tan', '#5a8a3a',
  {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'lips', 'mouth_w': 9, 'mouth_y': 92, 'hairline': (62, 58)},
  h['front'] + [bangs(62, 12, 88, 6, 24, jag=5), strand([(50, 10), (48, 24)], 'deep', 'f', 1.2)],
  h['side'] + [fr([(60, 20), (90, 30), (94, 56, 1), (84, 46), (74, 56, 1), (64, 40)])], h['back'])

# Julius Vernon (portero): pelo pardo grisáceo corto, con dos mechones de punta a los lados como cuernos y pinchos en la frente;
# ojos redondos de pupila pequeña, cejas enfadadas
h = three(crop, top=8, side=60, nape=84, w=3)
S('julius-vernon', 'normal', '#9c827a', 'light', '#302232',
  {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'hairline': (60, 56)},
  h['front'] + [tuft([(14, 36), (8, 14, 1), (24, 22)]), tuft([(86, 36), (92, 14, 1), (76, 22)]),
                fr([(18, 40), (30, 30), (70, 30), (84, 40), (80, 56, 1), (72, 48), (64, 58, 1), (56, 48), (48, 58, 1), (40, 48), (32, 56, 1), (24, 48)])],
  h['side'] + [tuft([(30, 14), (22, -4, 1), (42, 8)]), fr([(66, 22), (90, 30), (92, 52, 1), (84, 44), (76, 54, 1), (70, 40)])],
  h['back'] + [tuft([(14, 36), (8, 14, 1), (24, 22)]), tuft([(86, 36), (92, 14, 1), (76, 22)])])

# Kay Acker: melena revuelta azul oscuro de puntas por los lados, cinta verde con triángulos amarillos; cejas gruesas, ojos de punto
h = three(spikes, amp=12, n=12, seed=7, lo=74, nape=96)
S('kay-acker', 'normal', '#2a4664', 'tan', '#302232',
  {'eyes': 'dot', 'brows': False, 'mouth': 'frown', 'hairline': (60, 58)},
  h['front'] + side_tufts('front', 74) + headband('front', 46) + [L(outline([(36, 52), (40, 45), (44, 52)]), 'tri', 'f', False),
                                                                   L(outline([(46, 50), (50, 43), (54, 50)]), 'tri', 'f', False),
                                                                   L(outline([(56, 52), (60, 45), (64, 52)]), 'tri', 'f', False)] + brows(64, 'mid', 4, tilt=0.3),
  h['side'] + headband('side', 46) + brow_side(64, 'mid', 4),
  h['back'] + side_tufts('back', 76) + headband('back', 46), band='#4a8a3a', tri='#e8c83a')

# Keanu Dell: pelo rojo corto peinado con dos alas onduladas a los lados; cara ancha y mofletuda, piel clara; sonrisa torcida
S('keanu-dell', 'corpulento', '#c44a20', 'pale', '#302232',
  {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'face_front': CHUB, 'hairline': (56, 46), 'ear_out': 4},
  [L(outline([(16, 62), (2, 44), (6, 30, 1), (20, 32), (24, 18), (50, 16), (76, 18), (80, 32), (94, 30, 1), (98, 44), (84, 62), (78, 46), (22, 46)])),
   L(outline([(60, 18), (78, 20), (82, 34), (94, 32), (96, 44), (84, 58), (76, 40)]), 'shade', 'b', False), strand([(40, 20), (44, 34)], 'deep', 'b', 1.0)],
  [L(outline([(60, 46), (76, 40), (90, 30), (84, 16), (60, 12), (36, 14), (16, 22), (4, 40), (6, 62), (18, 78), (32, 76), (40, 62), (48, 52)])),
   L(outline([(6, 40), (30, 44), (40, 60), (32, 76), (18, 78)]), 'shade', 'b', False)],
  [L(outline([(16, 72), (4, 44), (8, 30, 1), (22, 30), (28, 18), (50, 14), (72, 18), (78, 30), (92, 30, 1), (96, 44), (84, 72), (50, 80)])),
   L(outline([(58, 16), (76, 20), (80, 32), (92, 32), (94, 46), (84, 70), (62, 78)]), 'shade', 'b', False)])

# Keenan Brainard: pelo gris verdoso rizado y corto, más oscuro (gris) por los lados y la nuca; cejas negras gruesas, ceño
h = three(crop, top=10, side=66, nape=88, w=6)
S('keenan-brainard', 'normal', '#6e9c98', 'tan', '#302232',
  {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 94, 'face_front': LONGF, 'hairline': (60, 48)},
  [L(cloud(12, 66, 8, 14, 4), 'side_c'), L(cloud(88, 66, 8, 14, 4), 'side_c')] + h['front'] + [L(cloud(50, 26, 40, 18, 9), 'mid', 'b', False)]
  + brows(63, BLACK, 4.5, tilt=0.6),
  h['side'] + [L(cloud(18, 62, 14, 18, 5), 'side_c')] + brow_side(63, BLACK, 4.5, 0.6),
  h['back'] + [L(outline([(12, 56), (50, 62), (88, 56), (86, 80), (50, 92), (14, 80)]), 'side_c')], side_c='#6a6a70')

# Keifer Tiliser: rubio con raya al lado y melena hasta la mandíbula en puntas abiertas; piel clara, cara larga, ojos rosados
S('keifer-tiliser', 'delgado', '#d8a52a', 'pale', '#9a5a6a',
  {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 94, 'face_front': LONGF, 'hairline': False, 'nose': (50, 84, 2.2)},
  [L(outline([(12, 92, 1), (14, 70), (8, 44), (18, 18), (42, 6), (70, 10), (88, 30), (92, 56), (88, 80), (96, 94, 1), (82, 84), (80, 60), (20, 60), (20, 84)])),
   fr([(14, 64), (16, 34), (34, 14), (56, 10), (76, 18), (88, 36), (88, 62, 1), (80, 46), (66, 34), (50, 30), (40, 40), (28, 56), (20, 72, 1)]),
   L(outline([(56, 12), (78, 20), (88, 36), (86, 56), (76, 38)]), 'light', 'f', False)],
  [L(outline([(60, 50), (78, 44), (92, 32), (84, 12), (58, 4), (32, 8), (12, 24), (4, 50), (4, 80), (-2, 96, 1), (14, 88), (26, 96, 1), (34, 80), (42, 64), (50, 54)])),
   L(outline([(4, 50), (30, 50), (40, 64), (32, 82), (14, 88)]), 'shade', 'b', False)],
  [L(outline([(12, 92, 1), (10, 60), (14, 30), (32, 10), (50, 6), (68, 10), (86, 30), (90, 60), (88, 92, 1), (70, 86), (60, 96, 1), (50, 86), (40, 96, 1), (30, 86)])),
   L(outline([(56, 8), (80, 24), (90, 60), (88, 90), (66, 86)]), 'shade', 'b', False)])

# Ken Broad: pelo azul marino peinado hacia atrás con pinchos en la nuca y a los lados; cara ancha y cuadrada, ceño
S('ken-broad', 'corpulento', '#2a4466', 'tan', '#302232',
  {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'face_front': CHUB, 'hairline': (54, 46), 'nose': (50, 85, 3)},
  [L(outline([(14, 74), (2, 66, 1), (12, 58), (6, 46, 1), (14, 40), (20, 20), (50, 8), (80, 20), (86, 40), (94, 46, 1), (88, 58), (98, 66, 1), (86, 74), (80, 50), (20, 50)])),
   L(outline([(58, 10), (80, 22), (86, 42), (84, 66), (76, 40)]), 'shade', 'b', False), strand([(40, 14), (42, 40)], 'deep', 'b', 1.0),
   strand([(60, 14), (58, 40)], 'deep', 'b', 1.0)],
  [L(outline([(70, 44), (84, 38), (90, 24), (76, 8), (50, 4), (24, 10), (8, 26), (-4, 40, 1), (6, 46), (-6, 60, 1), (6, 64), (0, 80, 1), (16, 78), (20, 92, 1),
              (30, 80), (40, 64), (54, 54)])),
   strand([(84, 30), (50, 20), (20, 30)], 'deep', 'b', 1.0)],
  [L(outline([(14, 78), (0, 70, 1), (10, 60), (2, 46, 1), (12, 40), (20, 20), (50, 8), (80, 20), (88, 40), (98, 46, 1), (90, 60), (100, 70, 1), (86, 78), (74, 88, 1),
              (64, 84), (50, 94, 1), (36, 84), (26, 88, 1)])),
   L(outline([(56, 10), (80, 22), (90, 44), (88, 76), (64, 84)]), 'shade', 'b', False)])

# Ken Sewer (portero): gorro crema abombado con costuras marrones (como un balón de rugby) que le tapa el pelo; asoma pelo
# verde agua por los lados; ojos redondos y sonrisa
S('ken-sewer', 'bajito', '#5aa4a0', 'light', '#302232',
  {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': (66, 62)},
  [tuft([(16, 80), (8, 70, 1), (16, 60), (24, 70)]), tuft([(84, 80), (92, 70, 1), (84, 60), (76, 70)]),
   L(bumpy(50, 36, 46, 34, 22, 0.04), 'hat', 'f'), L(outline([(6, 52), (50, 46), (94, 52), (94, 62), (50, 56), (6, 62)]), 'seam', 'f'),
   L(outline([(46, 4), (54, 4), (54, 48), (46, 48)]), 'seam', 'f', False)] + brows(66, 'mid', 3, w=9),
  [tuft([(40, 80), (30, 72, 1), (40, 62), (50, 72)]),
   L(bumpy(46, 34, 46, 34, 22, 0.04), 'hat', 'f'), L(outline([(0, 54), (50, 50), (94, 48), (94, 58), (50, 60), (0, 64)]), 'seam', 'f'),
   L(outline([(44, 0), (52, 0), (60, 52), (52, 52)]), 'seam', 'f', False)],
  [L(bumpy(50, 38, 46, 36, 22, 0.04), 'hat', 'f'), L(outline([(6, 56), (50, 52), (94, 56), (94, 66), (50, 62), (6, 66)]), 'seam', 'f'),
   L(outline([(46, 4), (54, 4), (54, 56), (46, 56)]), 'seam', 'f', False)], hat='#f4dcc0', seam='#a8502a')

# ------------------------------------------------------------------ hoja 1

# Kevin Boardman (portero): pelo castaño con un flequillo largo de lado que le tapa un ojo y la melena abierta en puntas a la
# altura de la mandíbula; cara de adulto, mandíbula ancha y sonrisa
S('kevin-boardman', 'normal', '#8c6a3c', 'tan', '#302232',
  {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'face_front': WIDE, 'hairline': False, 'nose': (50, 84, 3)},
  [L(outline([(16, 64), (12, 40), (22, 18), (50, 8), (78, 18), (88, 40), (86, 66), (98, 82, 1), (82, 78), (80, 56), (20, 56), (18, 78), (2, 86, 1)])),
   fr([(14, 60), (18, 34), (34, 16), (60, 12), (80, 22), (88, 38), (82, 46), (64, 40), (54, 56), (44, 76, 1), (40, 54), (28, 50), (18, 70, 1)]),
   L(outline([(58, 12), (80, 22), (88, 40), (86, 62), (76, 40)]), 'shade', 'b', False), strand([(34, 22), (40, 50)], 'deep', 'f', 1.0)],
  [L(outline([(64, 48), (80, 40), (92, 30), (84, 12), (58, 4), (30, 8), (12, 24), (4, 50), (8, 74), (-2, 88, 1), (18, 84), (26, 94, 1), (34, 80), (42, 64), (52, 54)])),
   fr([(70, 18), (92, 28), (94, 56, 1), (84, 42), (76, 36)])],
  [L(outline([(14, 76), (10, 44), (20, 18), (50, 8), (80, 18), (90, 44), (86, 76), (100, 88, 1), (80, 86), (66, 92, 1), (50, 86), (34, 92, 1), (20, 86), (0, 88, 1)])),
   L(outline([(56, 10), (80, 20), (90, 46), (86, 76), (64, 88)]), 'shade', 'b', False)])

# Kevin Doors (portero): pelo verde recogido en lo alto en un moño de mechones de punta que se abren como hojas; piel morena
h = three(crop, top=8, side=58, nape=82, w=0)
S('kevin-doors', 'bajito', '#6a9c3a', 'dark', '#302232',
  {'eyes': 'dot', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': (58, 50)},
  h['front'] + [tuft([(44, 10), (34, -12, 1), (48, 2), (52, -20, 1), (54, 2), (78, -10, 1), (58, 10)]),
                strand([(30, 20), (36, 44)], 'deep', 'b', 1.0), strand([(70, 20), (64, 44)], 'deep', 'b', 1.0),
                fr([(20, 44), (36, 32), (50, 30), (64, 32), (80, 44), (70, 50), (60, 44), (50, 56, 1), (42, 44), (30, 50)])],
  h['side'] + [tuft([(44, 8), (30, -12, 1), (50, 0), (60, -18, 1), (60, 4), (80, -6, 1), (64, 10)])],
  h['back'] + [tuft([(44, 10), (34, -12, 1), (48, 2), (52, -20, 1), (54, 2), (78, -10, 1), (58, 10)]), strand([(50, 12), (50, 80)], 'deep', 'b', 1.0)])

# Kim Arite (portero): pelo gris lila muy corto, con entradas; cara redonda y mofletuda, nariz grande; ceño fruncido
h = three(crop, top=20, side=52, nape=78, w=-3)
S('kim-arite', 'corpulento', '#8c7ca4', 'med', '#302232',
  {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'face_front': CHUB, 'hairline': [(14, 54), (22, 40), (36, 36), (44, 42), (50, 46), (56, 42),
                                                                                                        (64, 36), (78, 40), (86, 54)],
   'nose': (50, 85, 4.2)}, h['front'], h['side'], h['back'], nose='#9a6a48')

# Kim Ono: media melena platino con flequillo y las puntas rosadas; ojos grandes negros y sonrisa
S('kim-ono', 'normal', '#f2e8cc', 'light', '#1e1a1e',
  {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'hairline': False},
  [L(outline([(10, 92), (6, 50), (16, 18), (50, 4), (84, 18), (94, 50), (90, 92), (80, 90), (80, 60), (20, 60), (20, 90)])),
   L(outline([(8, 70), (20, 66), (20, 92), (10, 92)]), 'tip'), L(outline([(92, 70), (80, 66), (80, 90), (90, 92)]), 'tip'),
   bangs(62, 14, 86, 5, 22, jag=6), L(outline([(60, 8), (84, 20), (94, 50), (92, 70), (82, 50)]), 'shade', 'b', False)],
  [L(outline([(62, 50), (80, 44), (92, 30), (84, 10), (56, 2), (28, 8), (10, 26), (4, 56), (6, 92), (30, 94), (38, 74), (44, 60), (52, 54)])),
   L(outline([(5, 70), (36, 70), (34, 94), (6, 92)]), 'tip'), fr([(70, 18), (92, 30), (94, 56, 1), (82, 46)])],
  [L(outline([(10, 92), (6, 50), (16, 18), (50, 4), (84, 18), (94, 50), (90, 92), (50, 96)])),
   L(outline([(8, 72), (50, 76), (92, 72), (90, 92), (50, 96), (10, 92)]), 'tip')], tip='#e8b4b0')

# Kit Chapman: pelo crema altísimo en pinchos hacia arriba, rosado por debajo; piel morena; ojos grandes y boquita redonda
S('kit-chapman', 'bajito', '#f2e0c8', 'dark', '#302232',
  {'eyes': 'big', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 94, 'hairline': (58, 52)},
  [L(outline([(16, 70), (8, 46), (2, 24, 1), (16, 22), (14, -6, 1), (30, 8), (36, -22, 1), (48, 2), (60, -20, 1), (66, 4), (84, -8, 1), (82, 20), (98, 22, 1),
              (92, 46), (84, 70), (80, 52), (20, 52)])),
   L(outline([(8, 46), (16, 70), (22, 54), (24, 40)]), 'pink', 'b', False), L(outline([(92, 46), (84, 70), (78, 54), (76, 40)]), 'pink', 'b', False),
   L(outline([(30, 12), (36, 34), (42, 10)]), 'pink', 'b', False), L(outline([(58, 10), (64, 34), (70, 12)]), 'pink', 'b', False)],
  [L(outline([(64, 48), (80, 40), (94, 26), (100, 6, 1), (84, 12), (80, -12, 1), (64, 2), (48, -18, 1), (40, 6), (20, -2, 1), (20, 16), (2, 24, 1), (8, 40), (4, 60),
              (14, 76), (30, 78), (40, 62), (52, 54)])),
   L(outline([(6, 40), (30, 42), (40, 60), (30, 78), (14, 76)]), 'pink', 'b', False)],
  [L(outline([(16, 76), (8, 46), (2, 24, 1), (16, 22), (14, -6, 1), (30, 8), (36, -22, 1), (48, 2), (60, -20, 1), (66, 4), (84, -8, 1), (82, 20), (98, 22, 1),
              (92, 46), (84, 76), (50, 82)])),
   L(outline([(8, 50), (30, 60), (40, 50), (50, 62), (60, 50), (70, 60), (92, 50), (86, 76), (50, 82), (14, 76)]), 'pink', 'b', False)], pink='#dca4a0')

# Knight Reader: pelo azul marino oscuro peinado hacia atrás y largo por detrás en ondas hasta los hombros; cejas azules
# gruesas, cara alargada
S('knight-reader', 'delgado', '#28385a', 'light', '#302232',
  {'eyes': 'dot', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'face_front': LONGF, 'hairline': (50, 40), 'nose': (50, 84, 2.6)},
  [L(outline([(14, 120), (4, 104, 1), (10, 90), (2, 76, 1), (12, 62), (12, 36), (24, 14), (50, 6), (76, 14), (88, 36), (88, 62), (98, 76, 1), (90, 90), (96, 104, 1),
              (86, 120), (80, 100), (80, 50), (20, 50), (20, 100)])),
   strand([(40, 10), (40, 40)], 'deep', 'b', 1.0), strand([(60, 10), (60, 40)], 'deep', 'b', 1.0)] + brows(64, 'mid', 4.5, tilt=0.2),
  [L(outline([(70, 42), (86, 36), (88, 20), (70, 6), (44, 4), (20, 12), (6, 32), (2, 62), (-6, 80, 1), (4, 88), (-4, 104, 1), (8, 108), (6, 124, 1), (22, 112),
              (34, 104, 1), (36, 84), (42, 64), (54, 50)])),
   strand([(84, 28), (50, 18), (16, 30)], 'deep', 'b', 1.0)] + brow_side(64, 'mid', 4.5),
  [L(outline([(12, 116), (2, 100, 1), (10, 88), (2, 72, 1), (10, 58), (12, 34), (24, 12), (50, 6), (76, 12), (88, 34), (90, 58), (98, 72, 1), (90, 88), (98, 100, 1),
              (88, 116), (70, 110), (60, 122, 1), (50, 110), (40, 122, 1), (30, 110)])),
   L(outline([(56, 8), (80, 20), (90, 58), (90, 110), (66, 112)]), 'shade', 'b', False)])

# Kurt O'Graphy: gorra verde con un círculo amarillo de diana y visera amarilla; pelo morado pardo por debajo; ojos redondos
S('kurt-o-graphy', 'normal', '#7a5c8a', 'light', '#302232',
  {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': (66, 66)},
  [L(outline([(16, 78), (12, 54), (88, 54), (84, 78), (76, 64), (24, 64)])), fr([(18, 58), (40, 58), (32, 70, 1), (26, 62)])] + ballcap('front')
  + [L(ell(50, 32, 11, 9), 'brim', 'f', False), L(ell(50, 32, 6, 5), 'capc', 'f', False), L(ell(50, 32, 2.6, 2.2), 'brim', 'f', False)],
  [L(outline([(40, 80), (30, 60), (54, 56), (52, 72)]))] + ballcap('side'),
  [L(outline([(16, 76), (14, 60), (86, 60), (84, 76), (50, 82)]))] + ballcap('back'), capc='#6a9a40', brim='#e6c22a')

# Kurt Price: pelo naranja rojizo corto con una coleta tiesa hacia arriba en lo alto; cara redonda y mofletuda; cejas naranjas
h = three(crop, top=10, side=62, nape=84, w=2)
S('kurt-price', 'corpulento', '#c85a26', 'light', '#302232',
  {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'face_front': CHUB, 'hairline': (60, 44), 'nose': (50, 86, 3)},
  [tuft([(44, 12), (40, -4), (52, -20, 1), (60, -12, 1), (56, 12)])] + h['front'] + [L(ell(50, 10, 6, 4), 'band', 'b')] + brows(64, 'shade', 4, tilt=0.2),
  [tuft([(40, 8), (36, -8), (48, -24, 1), (56, -14, 1), (54, 8)])] + h['side'] + [L(ell(46, 6, 6, 4), 'band', 'b')] + brow_side(64, 'shade', 4),
  [tuft([(44, 12), (40, -4), (52, -20, 1), (60, -12, 1), (56, 12)])] + h['back'] + [L(ell(50, 10, 6, 4), 'band', 'b')], band='#8a4a2a')

# ------------------------------------------------------------------ hoja 2

# Kurt Tweedy: pelo pardo oliva en casco con el flequillo cortado recto y la nuca más oscura; ojos afilados y media sonrisa
h = three(crop, top=6, side=62, nape=82, w=2)
S('kurt-tweedy', 'normal', '#7a7044', 'tan', '#6a6a3a',
  {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'hairline': (60, 58)},
  h['front'] + [L(outline([(14, 58), (14, 40), (30, 26), (70, 26), (86, 40), (86, 58), (50, 56)]), 'mid', 'f'),
                L(outline([(14, 52), (50, 50), (86, 52), (86, 58), (50, 56), (14, 58)]), 'deep', 'f', False)],
  h['side'] + [fr([(60, 22), (90, 30), (92, 54), (64, 52)])], h['back'])

# Lance Lotts (portero): melena lisa rosa malva hasta la barbilla con raya en medio; piel morena; ojos redondos
S('lance-lotts', 'normal', '#b07272', 'dark', '#302232',
  {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': (60, 40)},
  longhair('front', length=96, flare=2, top=4, part=True), longhair('side', length=96, flare=2, top=4), longhair('back', length=96, flare=2, top=4, part=True))

# Larry Helps: media melena naranja con un flequillo largo de lado; ojos grandes verde agua y sonrisa
S('larry-helps', 'normal', '#e07a2e', 'light', '#4aa0a0',
  {'eyes': 'big', 'brows': False, 'mouth': 'grin', 'mouth_y': 94, 'hairline': False},
  [L(outline([(12, 90), (8, 50), (18, 16), (50, 4), (82, 16), (92, 50), (88, 90), (80, 88), (80, 60), (20, 60), (20, 88)])),
   L(outline([(60, 8), (82, 18), (92, 50), (90, 86), (82, 50)]), 'shade', 'b', False),
   fr([(12, 64), (16, 30), (36, 14), (64, 14), (84, 30), (86, 56), (76, 44), (60, 40), (44, 50), (30, 66, 1), (28, 52), (18, 76, 1)])],
  [L(outline([(62, 50), (80, 44), (92, 30), (84, 10), (56, 2), (28, 8), (10, 26), (4, 56), (6, 90), (30, 92), (38, 74), (44, 60), (52, 54)])),
   fr([(70, 18), (92, 30), (94, 58, 1), (82, 46)])],
  [L(outline([(10, 90), (6, 50), (16, 16), (50, 4), (84, 16), (94, 50), (90, 90), (50, 96)])),
   L(outline([(56, 6), (82, 18), (94, 50), (90, 88), (64, 94)]), 'shade', 'b', False)])

# Larry Oldman: señor de pelo platino corto en pinchos hacia arriba; piel tostada, ojos entornados y cejas claras
h = three(spikes, amp=8, n=10, seed=3, lo=56, nape=84, ry=36)
S('larry-oldman', 'normal', '#f2dcc0', 'med', '#302232',
  {'eyes': 'dot', 'brows': False, 'mouth': 'line', 'mouth_y': 96, 'face_front': LONGF, 'hairline': (56, 48), 'nose': (50, 84, 2.8)},
  h['front'] + brows(64, (232, 216, 160, 255), 3.5, tilt=0.4), h['side'] + brow_side(64, (232, 216, 160, 255), 3.5), h['back'])

# Leaf Scarlett: melenón rosa salmón en pinchos por todos lados con una coleta en lo alto; un parche verde en la frente
h = three(spikes, amp=14, n=13, seed=11, lo=74, nape=96, rx=48)
S('leaf-scarlett', 'normal', '#d07a6e', 'tan', '#302232',
  {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'hairline': (62, 54)},
  [tuft([(40, 12), (34, -10, 1), (46, -2), (50, -16, 1), (56, -2), (68, -8, 1), (60, 12)])] + h['front']
  + [L(ell(50, 12, 6, 3), 'band', 'b'), L(outline([(38, 58), (62, 58), (62, 68), (38, 68)]), 'patch', 'f'), L(outline([(43, 60), (57, 60), (57, 66), (43, 66)]), 'patch_l', 'f', False)],
  [tuft([(38, 10), (30, -12, 1), (44, -4), (50, -18, 1), (54, -2), (64, -10, 1), (58, 10)])] + h['side'],
  [tuft([(40, 12), (34, -10, 1), (46, -2), (50, -16, 1), (56, -2), (68, -8, 1), (60, 12)])] + h['back'] + [L(ell(50, 12, 6, 3), 'band', 'b')],
  band='#a85a40', patch='#4a9a5a', patch_l='#c8e0a0')

# Lee Dorr (portero): pelo lila rosado corto y revuelto; cejas lilas gruesas, ojos afilados
h = three(spikes, amp=8, n=10, seed=5, lo=58, nape=86, sweep=0.3)
S('lee-dorr', 'normal', '#c8a2b2', 'light', '#302232',
  {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': (58, 50)},
  h['front'] + brows(63, 'shade', 4, tilt=0.4), h['side'] + brow_side(63, 'shade', 4), h['back'])

# Lee Figreene: pelo gris morado en pinchos arriba y los lados rapados con rayas; cara ancha, cejas enfadadas
S('lee-figreene', 'normal', '#6c6a8c', 'light', '#302232',
  {'eyes': 'dot', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'face_front': WIDE, 'hairline': (56, 46)},
  [L(outline([(16, 64), (14, 40), (86, 40), (84, 64), (80, 50), (20, 50)]), 'buzz'),
   strand([(16, 46), (22, 60)], 'deep', 'b', 0.8), strand([(84, 46), (78, 60)], 'deep', 'b', 0.8),
   L(outline([(14, 42), (0, 30, 1), (18, 28), (16, 10, 1), (32, 18), (40, 0, 1), (50, 14), (62, 0, 1), (68, 18), (86, 10, 1), (84, 28), (100, 30, 1), (86, 42), (50, 46)]))],
  [L(outline([(50, 56), (60, 46), (20, 40), (6, 50), (8, 70), (20, 82), (34, 80), (40, 64)]), 'buzz'),
   L(outline([(84, 40), (94, 30, 1), (82, 26), (88, 10, 1), (70, 16), (66, -2, 1), (52, 12), (36, 0, 1), (32, 18), (12, 14, 1), (16, 30), (6, 40), (50, 44)]))],
  [L(outline([(14, 50), (86, 50), (84, 76), (50, 86), (16, 76)]), 'buzz'),
   L(outline([(14, 52), (0, 30, 1), (18, 28), (16, 10, 1), (32, 18), (40, 0, 1), (50, 14), (62, 0, 1), (68, 18), (86, 10, 1), (84, 28), (100, 30, 1), (86, 52), (50, 58)]))],
  buzz='#8c8a9c')

# Lee Gleagle: pelo muy corto pardo oscuro con la raya afeitada a los lados; piel morena; gafas redondas doradas; sonrisa
h = three(crop, top=12, side=56, nape=80, w=0)
S('lee-gleagle', 'normal', '#5a4e30', 'dark', '#b06a6a',
  {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 94, 'hairline': (56, 44), 'glasses': (190, 170, 60, 255)},
  h['front'] + [strand([(18, 46), (22, 56)], 'skin', 'b', 1.0), strand([(82, 46), (78, 56)], 'skin', 'b', 1.0)],
  h['side'] + [strand([(10, 50), (40, 56)], 'skin', 'b', 1.0)], h['back'])

# ------------------------------------------------------------------ hoja 3

# Len Scapp (portero): adulto de pelo pardo oliva corto peinado hacia arriba en una punta en medio de la frente
S('len-scapp', 'delgado', '#7c6a3c', 'tan', '#302232',
  {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 94, 'face_front': LONGF, 'hairline': (58, 44), 'nose': (50, 84, 2.4)},
  [L(outline([(16, 66), (12, 40), (24, 14), (50, -4, 1), (76, 14), (88, 40), (84, 66), (80, 50), (20, 50)])),
   strand([(50, 0), (40, 30)], 'deep', 'b', 1.0), strand([(50, 0), (60, 30)], 'deep', 'b', 1.0), strand([(50, 4), (50, 36)], 'deep', 'b', 1.0)],
  [L(outline([(58, 50), (76, 42), (88, 34), (92, 14, 1), (70, 6), (44, 4), (20, 12), (6, 32), (4, 56), (12, 76), (24, 86), (34, 80), (40, 64), (48, 54)])),
   strand([(88, 18), (50, 14), (20, 24)], 'deep', 'b', 1.0)],
  [L(outline([(16, 76), (12, 44), (22, 16), (50, 2), (78, 16), (88, 44), (84, 76), (50, 86)])), L(outline([(56, 4), (80, 18), (88, 46), (84, 74), (62, 84)]), 'shade', 'b', False)])

# Len Stint (portero): pelo gris plata revuelto de largo medio, con las puntas de abajo más oscuras; gafas de sol oscuras
h = three(spikes, amp=8, n=12, seed=9, lo=70, nape=92, rx=48)
S('len-stint', 'normal', '#c8c6b0', 'tan', '#302232',
  {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': (66, 54)},
  h['front'] + [fr([(16, 52), (30, 34), (70, 34), (84, 52), (78, 64, 1), (68, 52), (58, 62, 1), (50, 50), (42, 62, 1), (32, 52), (22, 64, 1)]),
                L(outline([(14, 60), (20, 72), (16, 76, 1)]), 'tip', 'b', False), L(outline([(86, 60), (80, 72), (84, 76, 1)]), 'tip', 'b', False),
                L(ell(37, 76, 11, 7), 'lens', 'f'), L(ell(63, 76, 11, 7), 'lens', 'f'), L([(46, 74), (54, 74)], BLACK, 'f', False, False, 1.4)],
  h['side'] + [L(ell(82, 76, 6, 6), 'lens', 'f'), L([(76, 74), (50, 70)], BLACK, 'f', False, False, 1.4)],
  h['back'] + [L(outline([(10, 76), (50, 82), (90, 76), (86, 90), (50, 94), (14, 90)]), 'tip', 'b', False)], tip='#9a8a7a', lens='#4a4430')

# Lenny Lakeman (portero): melena verde oliva con raya en medio hasta la mandíbula, abierta en las puntas; cara ancha y sonrisa
S('lenny-lakeman', 'normal', '#7c8a3a', 'tan', '#302232',
  {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 94, 'face_front': WIDE, 'hairline': (62, 40)},
  longhair('front', length=92, flare=10, top=6, part=True), longhair('side', length=92, flare=8, top=6), longhair('back', length=92, flare=10, top=6, part=True))

# Leon Lawn: cresta naranja de pinchos en lo alto y los lados rapados; piel tostada; estrellas amarillas pintadas en los ojos
S('leon-lawn', 'corpulento', '#e06a28', 'med', '#302232',
  {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'face_front': CHUB, 'hairline': (54, 40)},
  [L(outline([(32, 58), (28, 36), (34, 20), (26, 0, 1), (40, 10), (42, -10, 1), (50, 6), (58, -10, 1), (60, 10), (74, 0, 1), (66, 20), (72, 36), (68, 58), (50, 66)]))]
  + [L(outline([(36 + dx - 9, 77), (36 + dx - 2, 74), (36 + dx, 66, 1), (36 + dx + 2, 74), (36 + dx + 9, 77), (36 + dx + 3, 80), (36 + dx + 4, 88, 1), (36 + dx, 82),
                (36 + dx - 4, 88, 1), (36 + dx - 3, 80)]), 'star', 'f', False) for dx in (0, 28)]
  + [L(ell(cx, 75, rr, rr * 1.05), cc, 'f', False) for cx in (36, 64) for rr, cc in ((4.4, OUTC), (3.3, WHITE), (2.5, BLACK))],
  [L(outline([(70, 40), (86, 36), (96, 26, 1), (82, 22), (88, 6, 1), (70, 10), (66, -10, 1), (54, 6), (44, -14, 1), (40, 6), (26, 0, 1), (30, 16), (40, 40)]))],
  [L(outline([(34, 60), (28, 30), (34, 14), (28, -6, 1), (40, 6), (42, -16, 1), (50, 2), (58, -16, 1), (60, 6), (74, -6, 1), (66, 14), (72, 30), (66, 60), (50, 64)]))],
  star='#e8c428')

# Les Abel: pelo azul grisáceo claro revuelto con flequillo y un mechón de punta arriba; ojos afilados ámbar
h = three(spikes, amp=10, n=11, seed=13, lo=66, nape=90, sweep=-0.2)
S('les-abel', 'normal', '#9ac2ca', 'tan', '#a08a3a',
  {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'hairline': (60, 54)},
  h['front'] + [tuft([(44, 10), (54, -12, 1), (56, 10)]),
                fr([(18, 46), (34, 30), (66, 30), (82, 46), (78, 60, 1), (68, 50), (60, 62, 1), (52, 50), (42, 64, 1), (34, 50), (24, 60, 1)])],
  h['side'] + [tuft([(44, 6), (58, -14, 1), (58, 8)])], h['back'] + [tuft([(44, 10), (54, -12, 1), (56, 10)])])

# Les Belisha: pelo castaño oscuro corto con un mechón rojo rosado de cresta en medio; cara larga, sonrisa
h = three(crop, top=4, side=64, nape=86, w=2)
S('les-belisha', 'normal', '#4a3020', 'light', '#302232',
  {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'face_front': LONGF, 'hairline': (60, 52), 'nose': (50, 84, 2.6)},
  h['front'] + side_tufts('front', 64) + [fr([(18, 44), (34, 34), (66, 34), (82, 44), (80, 58, 1), (70, 50), (60, 58, 1), (54, 50), (46, 50), (38, 58, 1), (30, 50), (22, 58, 1)]),
                                          L(outline([(44, 4), (56, 4), (56, 56), (50, 64, 1), (44, 56)]), 'streak', 'f')],
  h['side'] + [L(outline([(48, 0), (60, 2), (88, 30), (80, 38)]), 'streak', 'f')], h['back'] + [L(outline([(44, 6), (56, 6), (54, 40), (46, 40)]), 'streak', 'f')],
  streak='#d06a7a')

# Les Knightley (portero): pelo gris pardo abultado con un moño pequeño en lo alto y dos bultos de pinchos a los lados; piel morena
S('les-knightley', 'normal', '#9a9080', 'dark', '#302232',
  {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': (62, 50)},
  [L(cloud(14, 50, 12, 14, 5), 'mid'), L(cloud(86, 50, 12, 14, 5), 'mid'), L(blob([(16, 60), (14, 36), (26, 18), (50, 12), (74, 18), (86, 36), (84, 60), (50, 50)])),
   L(ell(52, 4, 9, 9)), L(outline([(60, 14), (80, 22), (88, 40), (82, 58), (74, 38)]), 'shade', 'b', False)],
  [L(cloud(18, 52, 16, 18, 6), 'mid'), L(outline([(58, 50), (76, 42), (88, 32), (82, 14), (60, 8), (36, 10), (14, 24), (6, 48), (12, 72), (26, 80), (38, 66), (48, 56)])),
   L(ell(46, 2, 9, 9))],
  [L(cloud(14, 52, 12, 14, 5), 'mid'), L(cloud(86, 52, 12, 14, 5), 'mid'), L(blob([(16, 76), (12, 40), (26, 18), (50, 12), (74, 18), (88, 40), (84, 76), (50, 84)])),
   L(ell(50, 4, 9, 9)), L(outline([(56, 14), (80, 22), (88, 44), (84, 74), (62, 82)]), 'shade', 'b', False)])

# Les Tarrant (portero): adulto de pelo gris oliva corto en pinchos, con patillas de punta; ojos redondos rosados
h = three(spikes, amp=8, n=11, seed=17, lo=70, nape=88)
S('les-tarrant', 'delgado', '#8c8a70', 'light', '#b07a8a',
  {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'face_front': LONGF, 'hairline': (58, 48), 'nose': (50, 84, 2.6)},
  h['front'] + side_tufts('front', 70), h['side'], h['back'] + side_tufts('back', 72))

# ------------------------------------------------------------------ hoja 4

# Lincoln Hawking: grandullón mayor de pelo rubio canoso corto en pinchos; piel tostada, ojos entornados, nariz ancha
h = three(spikes, amp=9, n=12, seed=19, lo=60, nape=86, rx=48)
S('lincoln-hawking', 'corpulento', '#e8dcb2', 'med', '#302232',
  {'eyes': 'closed', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'face_front': CHUB, 'hairline': (56, 46), 'nose': (50, 86, 4.6)},
  h['front'], h['side'], h['back'], nose='#9a6a42')

# Linden Dray: pelo verde agua peinado de lado con mechones de punta y la nuca más oscura; cejas verdes y ojos redondos
h = three(spikes, amp=9, n=10, seed=21, lo=60, nape=88, sweep=0.4)
S('linden-dray', 'normal', '#6aa8a0', 'tan', '#302232',
  {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': (58, 48)},
  [tuft([(16, 62), (6, 76, 1), (18, 72)], 'deep'), tuft([(84, 62), (94, 76, 1), (82, 72)], 'deep')] + h['front'] + brows(64, 'shade', 3.5),
  h['side'] + brow_side(64, 'shade', 3.5), h['back'])

# Lloyd Tabb: pequeño de pelo verde azulado muy oscuro en pinchos grandes por todos lados; ojos redondos y ceño
h = three(spikes, amp=16, n=11, seed=23, lo=72, nape=96, rx=48)
S('lloyd-tabb', 'bajito', '#1e4a4e', 'tan', '#302232',
  {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'hairline': (62, 56)},
  h['front'] + [fr([(30, 40), (50, 34), (70, 40), (60, 50), (50, 66, 1), (42, 50)])], h['side'], h['back'])

# Lon Grainger (portero): tupé enorme gris verdoso en voluta; orejas de punta; piel morena; colmillo
S('lon-grainger', 'normal', '#6a7a70', 'dark', '#302232',
  {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': (56, 44), 'big_ears': 2},
  [L(outline([(16, 64), (12, 40), (16, 18), (34, 4), (66, -2), (90, 6), (96, 24), (84, 32), (86, 64), (80, 50), (20, 50)])),
   L(outline([(30, 20), (60, 8), (88, 12), (90, 24), (70, 22)]), 'light', 'b', False), L(outline([(84, 32), (86, 60), (78, 44)]), 'shade', 'b', False)],
  [L(outline([(60, 48), (78, 40), (98, 34), (108, 20), (98, 6), (70, -4), (40, 0), (16, 12), (4, 36), (6, 62), (16, 80), (30, 82), (40, 64), (50, 54)])),
   L(outline([(50, 6), (80, 0), (100, 10), (100, 22), (80, 16)]), 'light', 'b', False)],
  [L(outline([(14, 78), (10, 44), (18, 16), (50, 2), (82, 16), (90, 44), (86, 78), (50, 86)])), L(outline([(56, 4), (80, 18), (90, 46), (86, 76), (62, 84)]), 'shade', 'b', False)])

# Lou Beigh (portero): pelo rosa malva corto con dos mechones largos tiesos como antenas; ojos rojos afilados
h = three(crop, top=8, side=62, nape=84, w=2)
S('lou-beigh', 'normal', '#c07282', 'light', '#b0301e',
  {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'hairline': (60, 52)},
  h['front'] + [L(quad((48, 14), (40, -6), (34, -20)), 'deep', 'b', False, False, 2.6), L(quad((52, 14), (70, 0), (90, -4)), 'deep', 'b', False, False, 2.6),
                fr([(18, 44), (34, 32), (66, 32), (82, 44), (76, 60, 1), (66, 48), (56, 66, 1), (50, 48), (40, 62, 1), (30, 50), (22, 60, 1)])],
  h['side'] + [L(quad((48, 8), (44, -10), (36, -22)), 'deep', 'b', False, False, 2.6), L(quad((52, 8), (70, -2), (92, -4)), 'deep', 'b', False, False, 2.6)],
  h['back'] + [L(quad((48, 14), (40, -6), (34, -20)), 'deep', 'b', False, False, 2.6), L(quad((52, 14), (70, 0), (90, -4)), 'deep', 'b', False, False, 2.6)])

# Lou Paster: pelo rosa en pinchos cortos con un mechón levantado delante; ojos cerrados en sonrisa pícara
h = three(spikes, amp=9, n=11, seed=25, lo=64, nape=88)
S('lou-paster', 'normal', '#d07272', 'tan', '#302232',
  {'eyes': 'closed', 'brows': 'angry', 'mouth': 'smile', 'hairline': (58, 50)},
  h['front'] + [tuft([(40, 14), (48, -10, 1), (56, -4), (60, 14)]), fr([(30, 40), (50, 34), (70, 40), (58, 48), (50, 62, 1), (42, 48)])],
  h['side'] + [tuft([(54, 8), (72, -10, 1), (74, 4), (66, 12)])], h['back'] + [tuft([(40, 14), (48, -10, 1), (56, -4), (60, 14)])])

# Loughrey Mose: pelo castaño largo en puntas con un mechón amarillo grande que le tapa el ojo derecho; piel morena, ojo verde
S('loughrey-mose', 'normal', '#6a5020', 'dark', '#7a9a2a',
  {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
  [L(outline([(10, 100, 1), (8, 60), (6, 30), (20, 10), (34, -6, 1), (50, 4), (70, -4, 1), (82, 12), (94, 34), (94, 70), (92, 100, 1), (80, 90), (80, 60), (20, 60), (20, 90)])),
   fr([(14, 66), (16, 36), (30, 18), (40, 30), (34, 50), (22, 76, 1)]),
   fr([(40, 26), (56, 14), (74, 24), (84, 42), (82, 64), (70, 84, 1), (64, 66), (54, 58), (44, 42)], 'streak')],
  [L(outline([(66, 46), (82, 40), (94, 24), (86, 4), (62, -6, 1), (40, 2), (20, 6), (6, 30), (2, 60), (0, 96, 1), (16, 90), (26, 98, 1), (34, 80), (42, 64), (52, 54)])),
   fr([(74, 14), (94, 28), (96, 56, 1), (86, 42)], 'streak')],
  [L(outline([(10, 100, 1), (6, 60), (8, 30), (20, 10), (34, -6, 1), (50, 4), (70, -4, 1), (82, 12), (94, 34), (94, 60), (92, 100, 1), (76, 92), (64, 102, 1),
              (50, 92), (36, 102, 1), (24, 92)])),
   L(outline([(56, 6), (82, 14), (94, 40), (92, 96), (66, 94)]), 'shade', 'b', False)], streak='#e8c22a')

# Lucky Winn: pelo azul corto en casco con flequillo de mechones; piel clara; ojos cansados y boca triste
h = three(crop, top=6, side=64, nape=84, w=3)
S('lucky-winn', 'normal', '#2a6aa8', 'pale', '#302232',
  {'eyes': 'dot', 'brows': True, 'mouth': 'frown', 'mouth_y': 94, 'hairline': (60, 58)},
  h['front'] + [bangs(60, 14, 86, 6, 26, jag=7)] + [L(quad((30, 74), (36, 71), (42, 74)), OUTC, 'f', False, False, 1.4), L(quad((58, 74), (64, 71), (70, 74)), OUTC, 'f', False, False, 1.4)],
  h['side'] + [fr([(62, 22), (90, 30), (92, 56, 1), (82, 46), (72, 54, 1), (66, 40)])], h['back'])

# ------------------------------------------------------------------ hoja 5

# Luke O'Cyte: pelo naranja en cepillo altísimo de pinchos rectos hacia arriba; piel tostada, cejas naranjas
S('luke-o-cyte', 'normal', '#e0781e', 'med', '#302232',
  {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': (60, 56)},
  [L(outline([(16, 66), (12, 40), (8, -6, 1), (22, 8), (24, -20, 1), (36, 4), (40, -24, 1), (50, 2), (60, -24, 1), (64, 4), (76, -20, 1), (78, 8), (92, -6, 1),
              (88, 40), (84, 66), (80, 52), (20, 52)])),
   L(outline([(60, 2), (76, -16), (78, 8), (90, -2), (88, 40), (84, 62), (76, 40)]), 'shade', 'b', False),
   fr([(40, 46), (50, 40), (56, 46), (48, 60, 1)])] + brows(64, 'shade', 3.5, tilt=0.3),
  [L(outline([(60, 50), (78, 44), (90, 32), (96, -4, 1), (80, 8), (78, -20, 1), (64, 2), (56, -24, 1), (46, 2), (34, -20, 1), (30, 6), (14, -6, 1), (14, 20), (4, 40),
              (6, 62), (16, 78), (30, 78), (40, 62), (50, 54)]))] + brow_side(64, 'shade', 3.5),
  [L(outline([(16, 76), (12, 40), (8, -6, 1), (22, 8), (24, -20, 1), (36, 4), (40, -24, 1), (50, 2), (60, -24, 1), (64, 4), (76, -20, 1), (78, 8), (92, -6, 1),
              (88, 40), (84, 76), (50, 84)])), L(outline([(60, 2), (76, -16), (78, 8), (90, -2), (88, 40), (84, 74), (62, 82)]), 'shade', 'b', False)])

# Luke Raffles: pelo morado pardo corto con un moño y dos orejas grandes de koala de color crema a los lados; nariz grande de
# koala marrón; piel morena; ojos de punto
h = three(crop, top=6, side=60, nape=84, w=2)
S('luke-raffles', 'normal', '#7a4a66', 'dark', '#302232',
  {'eyes': 'dot', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': (60, 50), 'ears': False},
  [L(ell(8, 40, 14, 12), 'koala'), L(ell(92, 40, 14, 12), 'koala'), L(ell(8, 42, 8, 7), 'koala_d', 'b', False), L(ell(92, 42, 8, 7), 'koala_d', 'b', False)]
  + h['front'] + [L(ell(50, 6, 10, 8)), fr([(20, 44), (34, 32), (66, 32), (80, 44), (72, 54, 1), (62, 46), (50, 62, 1), (38, 46), (28, 54, 1)]),
                  L(outline([(44, 78), (56, 78), (58, 88), (50, 92), (42, 88)]), 'nose', 'f')],
  [L(ell(36, 44, 12, 14), 'koala')] + h['side'] + [L(ell(46, 4, 10, 8))],
  [L(ell(8, 42, 14, 12), 'koala'), L(ell(92, 42, 14, 12), 'koala')] + h['back'] + [L(ell(50, 8, 10, 8))],
  koala='#efd6c4', koala_d='#c8a898', nose='#6a3a1e')

# Luke Triton: niño de gorra azul de visera (gorra de repartidor) y pelo castaño corto; ojos grandes y redondos, sonrisa
S('luke-triton', 'bajito', '#8a6a3c', 'light', '#1e1a1e',
  {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'hairline': (66, 66)},
  [L(outline([(16, 80), (12, 58), (88, 58), (84, 80), (78, 66), (22, 66)])), fr([(18, 60), (82, 60), (78, 70, 1), (68, 64), (56, 70, 1), (44, 64), (32, 70, 1), (22, 64)]),
   L(blob([(8, 50), (6, 30), (24, 12), (50, 6), (76, 12), (94, 30), (92, 50), (50, 52)]), 'capc', 'f'),
   L(outline([(10, 50), (50, 46), (90, 50), (88, 60), (50, 56), (12, 60)]), 'brim', 'f')],
  [L(outline([(40, 82), (30, 62), (60, 58), (56, 74)])), L(blob([(4, 54), (4, 30), (24, 10), (52, 4), (80, 12), (92, 32), (90, 52), (40, 56)]), 'capc', 'f'),
   L(outline([(78, 48), (102, 54), (100, 60), (80, 58)]), 'brim', 'f')],
  [L(outline([(16, 78), (14, 60), (86, 60), (84, 78), (50, 84)])), L(blob([(8, 58), (6, 32), (24, 12), (50, 6), (76, 12), (94, 32), (92, 58), (50, 62)]), 'capc', 'f')],
  capc='#4a78a8', brim='#3a6290')

# Luther Rio (portero): melena rubia crema en bob con flequillo recto y dos rizos en espiral a los lados; corona verde agua con
# bola rosa encima; piel morena; ojos grises entornados
S('luther-rio', 'normal', '#f2e2c2', 'dark', '#8a8aa0',
  {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
  [L(outline([(12, 84), (8, 50), (18, 20), (50, 10), (82, 20), (92, 50), (88, 84), (80, 80), (80, 60), (20, 60), (20, 80)])),
   L(ell(12, 82, 9, 9)), L(ell(88, 82, 9, 9)), strand(quad((8, 82), (12, 76), (16, 82)) + quad((16, 82), (12, 88), (10, 80))[1:], 'shade', 'b', 1.2),
   strand(quad((92, 82), (88, 76), (84, 82)) + quad((84, 82), (88, 88), (90, 80))[1:], 'shade', 'b', 1.2),
   bangs(62, 16, 84, 7, 26, jag=0),
   L(outline([(28, 22), (24, 4, 1), (38, 12), (50, 0, 1), (62, 12), (76, 4, 1), (72, 22), (50, 26)]), 'crown', 'f'),
   L(ell(50, 0, 7, 6), 'ball', 'f')],
  [L(outline([(62, 50), (80, 44), (92, 30), (84, 12), (56, 6), (28, 10), (10, 28), (4, 56), (6, 84), (30, 88), (38, 72), (44, 60), (52, 54)])),
   L(ell(30, 84, 10, 10)), L(outline([(30, 16), (28, -2, 1), (44, 8), (58, -2, 1), (72, 10), (70, 22), (48, 24)]), 'crown', 'f'), L(ell(50, -2, 7, 6), 'ball', 'f')],
  [L(outline([(12, 84), (8, 50), (18, 20), (50, 10), (82, 20), (92, 50), (88, 84), (50, 90)])), L(ell(14, 84, 9, 9)), L(ell(86, 84, 9, 9)),
   L(outline([(28, 22), (24, 4, 1), (38, 12), (50, 0, 1), (62, 12), (76, 4, 1), (72, 22), (50, 26)]), 'crown', 'f'), L(ell(50, 0, 7, 6), 'ball', 'f')],
  crown='#5aa4a0', ball='#d88a8a')

# Lux Botty-Sidebottom (portero): adulto de pelo verde muy oscuro en pinchos revueltos; cejas verdes gruesas; cicatriz
h = three(spikes, amp=10, n=11, seed=27, lo=60, nape=88)
S('lux-botty-sidebottom', 'normal', '#36584a', 'tan', '#302232',
  {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'face_front': LONGF, 'hairline': (58, 50), 'nose': (50, 84, 2.8)},
  h['front'] + side_tufts('front', 62) + brows(64, 'mid', 4.5, tilt=0.2) + [L([(24, 88), (30, 100)], OUTC, 'f', False, False, 1.0)],
  h['side'] + brow_side(64, 'mid', 4.5), h['back'] + side_tufts('back', 64))

# Lyle O'Day: niño de piel morena con pelo pardo grisáceo en casco y un mechón en pico que baja por la frente; ojos redondos
# y sonrisa con un diente
h = three(crop, top=6, side=64, nape=84, w=4)
S('lyle-o-day', 'bajito', '#8a7a6a', 'dark', '#302232',
  {'eyes': 'round', 'brows': False, 'mouth': 'buck', 'mouth_y': 94, 'hairline': (62, 54)},
  h['front'] + [fr([(16, 52), (30, 36), (50, 30), (70, 36), (84, 52), (76, 58), (60, 50), (50, 70, 1), (40, 50), (24, 58)]),
                strand([(50, 30), (50, 62)], 'deep', 'f', 1.0)],
  h['side'] + [fr([(62, 22), (92, 30), (92, 58), (66, 48)])], h['back'])

# Mack Ramey: pelo verde con flequillo recto y rizos en espiral a los lados, como una peluca de juez; piel clara
S('mack-ramey', 'normal', '#6a9c3c', 'pale', '#302232',
  {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
  [L(cloud(10, 66, 10, 30, 5)), L(cloud(90, 66, 10, 30, 5)), L(blob([(14, 56), (16, 26), (50, 10), (84, 26), (86, 56), (50, 50)])), bangs(58, 18, 82, 6, 26, jag=0)]
  + [strand(quad((c - 4, y), (c, y - 4), (c + 4, y)) + quad((c + 4, y), (c, y + 4), (c - 2, y))[1:], 'deep', 'b', 1.0) for c in (10, 90) for y in (48, 64, 80)],
  [L(cloud(30, 66, 16, 30, 6)), L(outline([(60, 50), (80, 44), (92, 30), (84, 12), (56, 6), (28, 10), (10, 28), (8, 50), (40, 50)]))],
  [L(blob([(10, 92), (6, 50), (16, 22), (50, 10), (84, 22), (94, 50), (90, 92), (50, 98)])),
   L(cloud(20, 80, 14, 16, 5), 'shade', 'b', False), L(cloud(80, 80, 14, 16, 5), 'shade', 'b', False), L(cloud(50, 84, 14, 14, 5), 'shade', 'b', False)])

# Macky Valley: melena lisa dorada hasta los hombros, peinada hacia atrás con un rizo en medio de la frente; ojos verdes
S('macky-valley', 'normal', '#d8a828', 'dark', '#4a9a5a',
  {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': (56, 42)},
  longhair('front', length=110, flare=6, top=2) + [L(quad((46, 50), (48, 42), (54, 46)) + quad((54, 46), (52, 52), (48, 50))[1:], 'deep', 'f', False, False, 1.4)],
  longhair('side', length=110, flare=6, top=2), longhair('back', length=110, flare=6, top=2))

# ------------------------------------------------------------------ hoja 6

# Madison Cabinet (portero): casco con forma de balón rojo y crema con el borde verde oliva; ojos afilados y sonrisa
S('madison-cabinet', 'normal', '#3a2a1a', 'light', '#302232',
  {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': (66, 66)},
  [L(blob([(10, 64), (8, 30), (26, 6), (50, 0), (74, 6), (92, 30), (90, 64), (82, 60), (50, 56), (18, 60)]), 'helm', 'f'),
   L(outline([(38, 4), (62, 4), (68, 22), (50, 34), (32, 22)]), 'patch', 'f', False), L(outline([(12, 34), (26, 30), (30, 50), (14, 52)]), 'patch', 'f', False),
   L(outline([(88, 34), (74, 30), (70, 50), (86, 52)]), 'patch', 'f', False),
   L(outline([(8, 56), (50, 52), (92, 56), (90, 66), (82, 92), (76, 90), (80, 64), (50, 62), (20, 64), (24, 90), (18, 92), (10, 66)]), 'rim', 'f')],
  [L(blob([(4, 66), (2, 30), (22, 6), (50, 0), (78, 6), (94, 30), (92, 56), (60, 60), (40, 66)]), 'helm', 'f'),
   L(outline([(40, 4), (64, 6), (70, 24), (50, 34), (34, 22)]), 'patch', 'f', False), L(outline([(8, 32), (22, 30), (26, 50), (10, 52)]), 'patch', 'f', False),
   L(outline([(92, 50), (60, 54), (40, 62), (6, 62), (6, 70), (40, 70), (60, 62), (92, 58)]), 'rim', 'f')],
  [L(blob([(8, 72), (6, 30), (26, 6), (50, 0), (74, 6), (94, 30), (92, 72), (50, 80)]), 'helm', 'f'),
   L(outline([(38, 30), (62, 30), (68, 50), (50, 60), (32, 50)]), 'patch', 'f', False),
   L(outline([(6, 66), (50, 74), (94, 66), (94, 74), (50, 82), (6, 74)]), 'rim', 'f')],
  helm='#b8302a', patch='#f0e6c8', rim='#7a8a4a')

# Mal Inger: pelo rojo anaranjado en seta abombada con patillas y barba rojiza por la mandíbula; ojos entornados, dientes de
# conejo y nariz naranja
S('mal-inger', 'normal', '#c8501e', 'light', '#302232',
  {'eyes': 'dot', 'brows': False, 'mouth': 'buck', 'mouth_y': 96, 'hairline': (58, 54), 'nose': (50, 86, 2.6)},
  [L(blob([(10, 60), (8, 30), (26, 6), (50, 0), (74, 6), (92, 30), (90, 60), (50, 56)])),
   L(outline([(60, 4), (84, 16), (92, 36), (88, 58), (78, 40)]), 'shade', 'b', False),
   bangs(60, 12, 88, 5, 30, jag=4),
   L(outline([(18, 60), (24, 60), (24, 86), (36, 100), (50, 104), (64, 100), (76, 86), (76, 60), (82, 60), (84, 90), (70, 108), (50, 112), (30, 108), (16, 90)]), 'mid', 'f')]
  + [L(quad((30, 74), (36, 71), (42, 74)), OUTC, 'f', False, False, 1.4), L(quad((58, 74), (64, 71), (70, 74)), OUTC, 'f', False, False, 1.4)],
  [L(blob([(60, 52), (84, 46), (94, 28), (82, 6), (50, -2), (22, 6), (4, 30), (4, 60), (20, 78), (36, 72), (44, 58)])),
   L(outline([(50, 60), (56, 60), (60, 88), (76, 104), (66, 106), (52, 92)]), 'mid', 'f')],
  [L(blob([(8, 74), (6, 32), (26, 6), (50, 0), (74, 6), (94, 32), (92, 74), (50, 84)])), L(outline([(56, 4), (82, 16), (94, 44), (90, 72), (62, 82)]), 'shade', 'b', False)],
  nose='#e07a3a')

# Manny Atom: casco rojo con orejas de gato y una franja naranja en medio, que le tapa el pelo; piel morena, ojos amarillos
S('manny-atom', 'normal', '#c84a22', 'dark', '#c8a028',
  {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': (60, 60)},
  [L(outline([(10, 96), (8, 50), (10, 20), (12, -2, 1), (30, 8), (50, 4), (70, 8), (88, -2, 1), (90, 20), (92, 50), (90, 96), (80, 94), (80, 62), (20, 62), (20, 94)]), 'mid', 'b'),
   L(outline([(38, 6), (62, 6), (60, 58), (40, 58)]), 'stripe', 'b', False), L(outline([(14, 8), (26, 12), (16, 24)]), 'deep', 'b', False),
   L(outline([(86, 8), (74, 12), (84, 24)]), 'deep', 'b', False)],
  [L(outline([(60, 54), (84, 46), (92, 26), (86, 8), (70, 0, 1), (60, 6), (40, 4), (20, 10), (6, 30), (2, 60), (4, 96), (34, 96), (40, 76), (46, 60)]), 'mid', 'b'),
   L(outline([(40, 6), (60, 6), (90, 30), (88, 44), (60, 20)]), 'stripe', 'b', False)],
  [L(outline([(10, 96), (8, 50), (10, 20), (12, -2, 1), (30, 8), (50, 4), (70, 8), (88, -2, 1), (90, 20), (92, 50), (90, 96), (50, 100)]), 'mid', 'b'),
   L(outline([(38, 6), (62, 6), (60, 96), (40, 96)]), 'stripe', 'b', False)], stripe='#e07a30')

# Manny Carbs: grandullón de pelo azul grisáceo con dos mechones de punta a los lados como cuernos; sonrisa torcida
h = three(crop, top=8, side=62, nape=84, w=2)
S('manny-carbs', 'corpulento', '#3e5474', 'light', '#302232',
  {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'face_front': CHUB, 'hairline': (58, 50), 'nose': (50, 86, 3)},
  h['front'] + [tuft([(14, 38), (6, 12, 1), (26, 24)]), tuft([(86, 38), (94, 12, 1), (74, 24)]),
                fr([(18, 44), (34, 32), (66, 32), (82, 44), (76, 58, 1), (66, 48), (56, 60, 1), (48, 48), (38, 60, 1), (30, 48), (22, 58, 1)])],
  h['side'] + [tuft([(30, 14), (20, -6, 1), (42, 8)])],
  h['back'] + [tuft([(14, 38), (6, 12, 1), (26, 24)]), tuft([(86, 38), (94, 12, 1), (74, 24)])])

# Manny Gerry: pelo castaño en pinchos altos y patillas de punta; ojos naranjas afilados
h = three(spikes, amp=14, n=10, seed=29, lo=64, nape=90, ry=38)
S('manny-gerry', 'normal', '#8a6a3c', 'tan', '#c86a1e',
  {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'hairline': (58, 54)},
  h['front'] + side_tufts('front', 70) + [tuft([(40, 14), (50, -16, 1), (60, 14)])], h['side'] + [tuft([(40, 8), (52, -20, 1), (60, 10)])],
  h['back'] + side_tufts('back', 72) + [tuft([(40, 14), (50, -16, 1), (60, 14)])])

# Manny Kinsland: grandullón de pelo verde oliva en media melena con flequillo recto y las puntas enroscadas en espiral
S('manny-kinsland', 'corpulento', '#6a6a2a', 'light', '#302232',
  {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'face_front': CHUB, 'hairline': False, 'nose': (50, 86, 3)},
  [L(blob([(4, 92), (2, 50), (16, 16), (50, 4), (84, 16), (98, 50), (96, 92), (82, 92), (82, 60), (18, 60), (18, 92)])),
   L(ell(10, 88, 11, 11)), L(ell(90, 88, 11, 11)),
   strand(quad((4, 88), (10, 80), (16, 88)) + quad((16, 88), (10, 94), (8, 86))[1:], 'deep', 'b', 1.2),
   strand(quad((96, 88), (90, 80), (84, 88)) + quad((84, 88), (90, 94), (92, 86))[1:], 'deep', 'b', 1.2),
   bangs(58, 16, 84, 6, 22, jag=0), L(outline([(16, 52), (84, 52), (84, 58), (16, 58)]), 'deep', 'f', False)],
  [L(blob([(62, 50), (82, 44), (94, 28), (84, 8), (54, 0), (24, 6), (6, 28), (2, 60), (4, 92), (30, 96), (40, 76), (46, 60)])), L(ell(18, 90, 12, 11))],
  [L(blob([(4, 92), (2, 50), (16, 16), (50, 4), (84, 16), (98, 50), (96, 92), (50, 98)])), L(ell(12, 90, 11, 11)), L(ell(88, 90, 11, 11)),
   L(outline([(56, 6), (84, 18), (98, 50), (94, 88), (64, 96)]), 'shade', 'b', False)])

# Manny Steele: grandullón de cabeza grande con el pelo rosa rapado; ojos afilados y sonrisa de dientes
h = three(crop, top=16, side=54, nape=78, w=-2)
S('manny-steele', 'corpulento', '#d88a8a', 'light', '#302232',
  {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'face_front': CHUB, 'hairline': (52, 42)},
  h['front'], h['side'], h['back'])

# Manuel Gere: casco de aviador azul marino con una flecha crema encima y orejeras crema; pelo naranja por delante; ojos rosados
S('manuel-gere', 'normal', '#e07a30', 'light', '#b06a7a',
  {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'hairline': (62, 60), 'ears': False},
  [L(outline([(14, 62), (16, 40), (84, 40), (86, 62), (80, 54), (20, 54)])),
   fr([(18, 42), (82, 42), (78, 60, 1), (68, 50), (58, 62, 1), (50, 50), (42, 62, 1), (32, 50), (22, 60, 1)]),
   L(outline([(8, 96), (6, 50), (14, 20), (50, 6), (86, 20), (94, 50), (92, 96), (82, 96), (82, 50), (50, 40), (18, 50), (18, 96)]), 'helm', 'f'),
   L(outline([(30, 14), (50, 8), (70, 14), (66, 28), (58, 26), (50, 40, 1), (42, 26), (34, 28)]), 'arrow', 'f', False),
   L(ell(10, 74, 7, 10), 'arrow', 'f'), L(ell(90, 74, 7, 10), 'arrow', 'f')],
  [L(outline([(70, 46), (90, 40), (92, 56), (74, 54)])),
   L(outline([(70, 44), (88, 36), (90, 24), (74, 6), (46, 0), (20, 8), (4, 32), (2, 70), (10, 96), (30, 96), (40, 84), (56, 80), (60, 52)]), 'helm', 'f'),
   L(outline([(50, 2), (76, 8), (86, 22), (70, 24), (50, 14)]), 'arrow', 'f', False), L(ell(46, 72, 9, 11), 'arrow', 'f')],
  [L(outline([(8, 96), (6, 50), (14, 20), (50, 6), (86, 20), (94, 50), (92, 96), (50, 100)]), 'helm', 'f'),
   L(outline([(44, 8), (56, 8), (56, 60), (44, 60)]), 'arrow', 'f', False)], helm='#2c4868', arrow='#e2d6a8')

# ------------------------------------------------------------------ hoja 7

# Marc O'Lepsy: grandullón calvo de piel morena con cabeza de huevo y un mechón rojizo de cresta en lo alto; boca grande
S('marc-o-lepsy', 'corpulento', '#c0562a', 'dark', '#302232',
  {'eyes': 'round', 'brows': 'angry', 'mouth': 'lips', 'mouth_w': 11, 'mouth_y': 94, 'face_front': CHUB, 'hairline': False, 'nose': (50, 84, 3.6)},
  [L(blob([(12, 70), (14, 36), (30, 14), (50, 6), (70, 14), (86, 36), (88, 70), (50, 60)]), 'skin'),
   L(outline([(44, 20), (42, 6), (50, -6, 1), (58, 6), (56, 20), (50, 24)])), strand([(50, -2), (50, 20)], 'deep', 'b', 1.0)],
  [L(blob([(60, 50), (80, 30), (60, 8), (30, 8), (10, 30), (6, 60), (20, 80), (40, 70)]), 'skin'),
   L(outline([(40, 16), (40, 2), (50, -10, 1), (58, 2), (56, 16), (48, 20)]))],
  [L(outline([(44, 20), (42, 6), (50, -6, 1), (58, 6), (56, 20), (50, 24)]))], nose='#a06a40')

# Mario Nette: pelo malva rosado corto y ondulado; ojos redondos negros, ceño
h = three(crop, top=6, side=64, nape=86, w=5)
S('mario-nette', 'normal', '#b88282', 'light', '#1e1a1e',
  {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'hairline': (60, 54)},
  h['front'] + [L(cloud(14, 58, 6, 10, 3)), L(cloud(86, 58, 6, 10, 3)),
                fr([(18, 46), (32, 32), (68, 32), (82, 46), (76, 58), (66, 50), (58, 56), (50, 48), (42, 56), (34, 50), (24, 58)])],
  h['side'] + [fr([(62, 22), (92, 30), (92, 52), (80, 48), (68, 52)])], h['back'])

# Mark Brent: pelo naranja salvaje en mechones de punta por todos lados con un rizo arriba; ojos afilados, ceño
h = three(spikes, amp=12, n=13, seed=31, lo=72, nape=94, rx=48, sweep=0.2)
S('mark-brent', 'normal', '#e0782c', 'tan', '#302232',
  {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'hairline': (60, 54)},
  h['front'] + side_tufts('front', 74) + [L(quad((48, 10), (42, -6), (54, -8)) + quad((54, -8), (60, -4), (54, 2))[1:], 'mid', 'b', False, False, 2.4),
                                          fr([(24, 44), (40, 34), (60, 34), (76, 44), (70, 58, 1), (60, 48), (50, 62, 1), (42, 48), (30, 58, 1)])],
  h['side'], h['back'] + side_tufts('back', 76))

# Mark Perfect (portero): turbante gris morado enrollado que le tapa el pelo; gafas rectangulares naranjas; piel morena
S('mark-perfect', 'corpulento', '#9c8494', 'dark', '#302232',
  {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'face_front': CHUB, 'hairline': (60, 58), 'nose': (50, 86, 3)},
  [L(blob([(12, 62), (8, 34), (22, 10), (50, 2), (78, 10), (92, 34), (88, 62), (50, 56)])),
   strand([(14, 50), (40, 20), (78, 12)], 'deep', 'b', 1.4), strand([(16, 60), (50, 30), (88, 30)], 'deep', 'b', 1.4), strand([(30, 58), (60, 42), (88, 48)], 'deep', 'b', 1.4),
   L(outline([(22, 70), (46, 70), (46, 80), (24, 80)]), 'lens', 'f'), L(outline([(78, 70), (54, 70), (54, 80), (76, 80)]), 'lens', 'f'),
   L([(46, 73), (54, 73)], 'lens_d', 'f', False, False, 1.4)],
  [L(blob([(70, 50), (90, 40), (92, 20), (70, 2), (40, 0), (14, 12), (4, 40), (8, 66), (30, 70), (50, 58)])),
   strand([(10, 30), (50, 10), (88, 24)], 'deep', 'b', 1.4), strand([(8, 50), (50, 30), (90, 40)], 'deep', 'b', 1.4),
   L(outline([(78, 70), (90, 70), (90, 80), (78, 80)]), 'lens', 'f'), L([(50, 72), (78, 72)], 'lens_d', 'f', False, False, 1.4)],
  [L(blob([(10, 72), (8, 34), (22, 10), (50, 2), (78, 10), (92, 34), (90, 72), (50, 80)])),
   strand([(12, 40), (50, 20), (88, 40)], 'deep', 'b', 1.4), strand([(10, 58), (50, 40), (90, 58)], 'deep', 'b', 1.4)], lens='#f0a040', lens_d='#a86a20')

# Mark Skidfree: melena rizada amarilla abultada con bucles largos a los lados; piel morena; cejas amarillas; pendiente en la nariz
S('mark-skidfree', 'normal', '#e2b024', 'dark', '#302232',
  {'eyes': 'dot', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'face_front': LONGF, 'hairline': (56, 46)},
  [L(cloud(14, 76, 10, 30, 6)), L(cloud(86, 76, 10, 30, 6)), L(cloud(50, 24, 42, 26, 10))]
  + brows(64, 'mid', 4) + [L(ell(46, 84, 1.6, 1.6), (90, 160, 90, 255), 'f')],
  [L(cloud(28, 70, 18, 34, 7)), L(cloud(48, 24, 42, 26, 10))] + brow_side(64, 'mid', 4),
  [L(cloud(50, 60, 42, 44, 12)), L(cloud(70, 64, 18, 30, 6), 'shade', 'b', False)])

# Mark Sudor (portero): capucha verde oliva peluda (cabeza de gorila) que le tapa la cabeza y le enmarca la cara; piel morena
S('mark-sudor', 'corpulento', '#6a7a3a', 'dark', '#302232',
  {'eyes': 'dot', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'face_front': CHUB, 'hairline': (66, 54), 'nose': (50, 84, 3.4)},
  [L(outline([(4, 100), (0, 60), (8, 30), (30, 10), (50, 6), (70, 10), (92, 30), (100, 60), (96, 100), (84, 104), (86, 70), (50, 62), (14, 70), (16, 104)]), 'mid', 'f'),
   L(outline([(30, 60), (50, 50), (70, 60), (60, 68), (40, 68)]), 'shade', 'f', False)],
  [L(outline([(70, 52), (90, 40), (88, 18), (64, 4), (36, 4), (12, 16), (0, 46), (4, 90), (40, 100), (56, 80), (60, 60)]), 'mid', 'f')],
  [L(outline([(4, 100), (0, 60), (8, 30), (30, 10), (50, 6), (70, 10), (92, 30), (100, 60), (96, 100), (50, 106)]), 'mid', 'f'),
   L(outline([(56, 10), (84, 24), (98, 60), (94, 98), (64, 104)]), 'shade', 'f', False)], nose='#8a5a30')

# Mark Tinney: adulto delgado de pelo gris corto peinado hacia atrás con entradas; barbilla larga, ojos entornados
h = three(crop, top=8, side=60, nape=84, w=0)
S('mark-tinney', 'delgado', '#9c9a8a', 'tan', '#5a7a7a',
  {'eyes': 'dot', 'brows': True, 'mouth': 'smile', 'mouth_y': 98, 'face_front': LONGF, 'nose': (50, 86, 2.6),
   'hairline': [(14, 60), (18, 46), (30, 42), (40, 50), (50, 44), (60, 50), (70, 42), (82, 46), (86, 60)]},
  h['front'] + [strand([(50, 10), (50, 40)], 'deep', 'b', 1.0), strand([(40, 12), (36, 42)], 'deep', 'b', 1.0), strand([(60, 12), (64, 42)], 'deep', 'b', 1.0),
                L(quad((30, 74), (36, 71), (42, 74)), OUTC, 'f', False, False, 1.4), L(quad((58, 74), (64, 71), (70, 74)), OUTC, 'f', False, False, 1.4)],
  h['side'] + [strand([(84, 28), (50, 16), (20, 26)], 'deep', 'b', 1.0)], h['back'])

# Martin Sheller: grandullón con un tupé naranja altísimo en ola hacia atrás; ojos entornados y sonrisa
S('martin-sheller', 'corpulento', '#e0782c', 'light', '#302232',
  {'eyes': 'dot', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'face_front': CHUB, 'hairline': (56, 46), 'nose': (50, 86, 3)},
  [L(outline([(16, 66), (12, 40), (22, 18), (40, 4), (66, -16), (84, -24, 1), (78, -8), (86, 14), (88, 40), (84, 66), (80, 50), (20, 50)])),
   strand([(30, 30), (60, 0), (80, -18)], 'deep', 'b', 1.0), strand([(40, 36), (68, 10), (82, -6)], 'deep', 'b', 1.0),
   L(quad((30, 74), (36, 71), (42, 74)), OUTC, 'f', False, False, 1.4), L(quad((58, 74), (64, 71), (70, 74)), OUTC, 'f', False, False, 1.4)],
  [L(outline([(60, 50), (76, 44), (88, 34), (94, 12), (84, -2), (60, -8), (30, -18), (10, -22, 1), (20, -8), (8, 14), (4, 40), (8, 62), (20, 78), (34, 76), (42, 60), (50, 54)])),
   strand([(90, 14), (60, 0), (20, -12)], 'deep', 'b', 1.0)],
  [L(outline([(16, 76), (12, 40), (22, 16), (40, 4), (60, -6), (72, -12, 1), (76, 6), (88, 40), (84, 76), (50, 84)])),
   L(outline([(56, 2), (78, 14), (88, 44), (84, 74), (62, 82)]), 'shade', 'b', False)])

# ------------------------------------------------------------------ hoja 8

# Marty Gras: pelo verde corto en pinchos con pico en la frente; piel morena; orejas de punta y colmillo
S('marty-gras', 'normal', '#4a9a5a', 'dark', '#302232',
  {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'big_ears': 2, 'face_front': LONGF,
   'hairline': [(14, 56), (20, 46), (34, 46), (44, 52), (50, 64), (56, 52), (66, 46), (80, 46), (86, 56)]},
  [L(outline([(16, 62), (10, 50), (8, 38, 1), (16, 30), (18, 14), (34, 4), (50, 0), (66, 4), (82, 14), (84, 30), (92, 38, 1), (90, 50), (84, 62), (80, 50), (20, 50)])),
   L(outline([(58, 4), (80, 16), (84, 34), (84, 56), (76, 36)]), 'shade', 'b', False)]
  + [L([(56, 96), (57, 100), (58, 96)], WHITE, 'f', False, False, 1.4)],
  [L(outline([(60, 48), (76, 42), (88, 30), (84, 12), (60, 4), (34, 6), (14, 18), (2, 30, 1), (8, 40), (4, 60), (14, 76), (28, 80), (38, 64), (48, 54)]))],
  [L(outline([(16, 74), (8, 50), (6, 38, 1), (16, 30), (18, 14), (34, 4), (50, 0), (66, 4), (82, 14), (84, 30), (94, 38, 1), (92, 50), (84, 74), (50, 82)])),
   L(outline([(56, 4), (80, 16), (90, 48), (84, 72), (62, 80)]), 'shade', 'b', False)])

# Marv Errick (portero): grandullón de pelo naranja liso pegado hacia atrás; un visor en arco verde agua y naranja que le cruza
# el ojo derecho; boca apretada enseñando los dientes
h = three(crop, top=8, side=58, nape=82, w=-2)
S('marv-errick', 'corpulento', '#e06a28', 'tan', '#302232',
  {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'face_front': CHUB, 'hairline': (56, 44)},
  h['front'] + [strand([(40, 10), (38, 40)], 'deep', 'b', 1.0), strand([(50, 8), (50, 40)], 'deep', 'b', 1.0), strand([(60, 10), (62, 40)], 'deep', 'b', 1.0),
                L(quad((22, 48), (14, 78), (30, 100)), 'visor', 'f', False, False, 4.0), L(quad((26, 48), (19, 78), (34, 98)), 'visor2', 'f', False, False, 2.4)],
  h['side'] + [strand([(84, 26), (50, 14), (20, 24)], 'deep', 'b', 1.0)], h['back'], visor='#d0601e', visor2='#5a9aa0')

# Mat Char: gorro de bufón azul marino de dos puntas con cascabeles amarillos y la banda amarilla; piel morena, ojos entornados
S('mat-char', 'bajito', '#2a4060', 'dark', '#302232',
  {'eyes': 'dot', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': (60, 60), 'nose': (50, 84, 3)},
  [L(outline([(16, 56), (14, 36), (4, 30), (-8, 46, 1), (2, 20), (26, 8), (50, 12), (74, 8), (98, 20), (108, 46, 1), (96, 30), (86, 36), (84, 56)]), 'mid', 'f'),
   L(outline([(14, 44), (50, 36), (86, 44), (86, 58), (50, 52), (14, 58)]), 'bell', 'f'), L(ell(-6, 48, 5, 5), 'bell', 'f'), L(ell(106, 48, 5, 5), 'bell', 'f')]
  + brows(66, (110, 120, 60, 255), 3)
  + [L(quad((30, 76), (36, 73), (42, 76)), OUTC, 'f', False, False, 1.4), L(quad((58, 76), (64, 73), (70, 76)), OUTC, 'f', False, False, 1.4)],
  [L(outline([(10, 60), (6, 34), (20, 10), (48, 6), (60, 8), (80, 0), (102, 4), (108, 24, 1), (96, 14), (86, 22), (88, 46), (50, 52)]), 'mid', 'f'),
   L(outline([(8, 50), (50, 44), (88, 42), (88, 54), (50, 56), (8, 62)]), 'bell', 'f'), L(ell(108, 28, 5, 5), 'bell', 'f')],
  [L(outline([(16, 62), (14, 36), (4, 30), (-8, 46, 1), (2, 20), (26, 8), (50, 12), (74, 8), (98, 20), (108, 46, 1), (96, 30), (86, 36), (84, 62), (50, 66)]), 'mid', 'f'),
   L(outline([(14, 50), (50, 44), (86, 50), (86, 64), (50, 60), (14, 64)]), 'bell', 'f'), L(ell(-6, 48, 5, 5), 'bell', 'f'), L(ell(106, 48, 5, 5), 'bell', 'f')],
  bell='#e2c060')
