"""Instituto Bastión (Minodouzan, ares-minodouzan): sus modelos 3D de Inazuma Eleven Ares como referencia (busto de frente,
perfil y espalda), calcados sobre la rejilla de unidades de cabeza. El equipo de las fortalezas: torres, almenas y muros
en el pelo y los cascos."""
import copy

from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand
from chars_alius import WIDE_FACE
from chars_bigwaves import side_eye, white_eyes
from heads import quad

WHITE = (248, 248, 248, 255)
TEETH_L = (120, 40, 40, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Knox Loxley (Jousai Kento, portero): pelo beige rosado altísimo de pinchos grandes en todas direcciones, que le cae en
# puntas por los lados hasta la mandíbula; piel morena y ojos azules afilados
CHARS['knox-loxley'] = {
    'body': 'normal', 'pal': pal('#d8b8a8', '#b8825a', iris='#4a6ab8', shade='#a8807a', deep='#8a6058'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 96), (-2, 88, 1), (6, 76), (-10, 64, 1), (4, 56), (-12, 40, 1), (6, 34), (0, 12, 1), (18, 18), (14, -8, 1), (32, 6), (40, -22, 1),
                         (50, 2), (62, -26, 1), (66, 2), (84, -10, 1), (84, 16), (104, 10, 1), (94, 32), (112, 40, 1), (96, 54), (110, 66, 1), (94, 76),
                         (102, 90, 1), (86, 96), (84, 66), (16, 66)])),
              L(outline([(58, 0), (84, -6), (84, 18), (100, 36), (98, 80), (84, 60)]), 'shade', 'b', False),
              fringe([(12, 84, 1), (14, 48), (26, 30), (50, 24), (74, 30), (86, 48), (88, 84, 1), (80, 64), (74, 72, 1), (68, 52), (58, 64, 1), (54, 48),
                      (48, 74, 1), (42, 50), (34, 66, 1), (28, 52), (20, 68, 1)]),
              L(outline([(56, 28), (76, 34), (84, 52), (72, 48)]), 'shade', 'f', False)],
    'side': [L(outline([(54, 66), (60, 52), (78, 50), (88, 36), (98, 18, 1), (80, 14), (80, -8, 1), (62, 4), (50, -24, 1), (38, 0), (16, -12, 1), (18, 12),
                        (-10, 16, 1), (6, 32), (-16, 46, 1), (4, 54), (-8, 72, 1), (10, 72), (4, 92, 1), (22, 84), (26, 100, 1), (38, 86), (48, 78)])),
             L(outline([(2, 34), (24, 40), (28, 80), (8, 74)]), 'shade', 'b', False),
             fringe([(66, 6), (90, 20), (96, 44), (94, 70, 1), (86, 54), (80, 66, 1), (76, 44), (66, 30)])],
    'back': [L(outline([(16, 96), (2, 92, 1), (8, 76), (-8, 66, 1), (6, 56), (-10, 40, 1), (6, 32), (0, 10, 1), (18, 16), (14, -10, 1), (32, 4), (40, -24, 1),
                        (50, 0), (62, -26, 1), (66, 0), (84, -12, 1), (84, 14), (104, 8, 1), (94, 30), (112, 40, 1), (96, 54), (110, 66, 1), (94, 76), (98, 92, 1),
                        (84, 96), (70, 106, 1), (60, 96), (50, 108, 1), (40, 96), (30, 106, 1)])),
             L(outline([(56, 0), (84, -8), (84, 16), (100, 36), (96, 92), (66, 100), (70, 50)]), 'shade', 'b', False),
             strand([(30, 20), (36, 50), (30, 84)], 'deep', 'b', 1.0), strand([(70, 20), (64, 50), (70, 84)], 'deep', 'b', 1.0)],
}

# Björn Brocken (Maeno Taihou): grandullón de piel morena; melena morada oscura ondulada hasta los hombros, con raya en
# medio y mechones finos que se rizan hacia fuera a los lados; ojos blancos redondos de pupila pequeña, cejas fruncidas
CHARS['bj-rn-brocken'] = {
    'body': 'corpulento', 'pal': pal('#3a2a78', '#d0844e', shade='#2a1e5a', deep='#1e143e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False, 'face_front': WIDE_FACE},
    'front': [L(outline([(10, 104), (2, 80), (4, 44), (16, 22), (50, 12), (84, 22), (96, 44), (98, 80), (90, 104), (84, 70), (16, 70)])),
              L(outline([(58, 16), (84, 26), (96, 50), (94, 98), (84, 70)]), 'shade', 'b', False),
              L(quad((6, 70), (-10, 64), (-14, 76)), 'mid', 'b', False, False, 2.4), L(quad((94, 70), (110, 64), (114, 76)), 'mid', 'b', False, False, 2.4),
              L(quad((6, 92), (-8, 96), (-6, 106)), 'mid', 'b', False, False, 2.2), L(quad((94, 92), (108, 96), (106, 106)), 'mid', 'b', False, False, 2.2),
              fringe([(12, 70), (14, 40), (30, 22), (48, 18), (50, 30), (52, 18), (70, 22), (86, 40), (88, 70), (80, 50), (66, 36), (52, 32), (50, 40),
                      (48, 32), (34, 36), (20, 50)])] + white_eyes(76, 14, 6.4, 5.4, 1.8)
             + [L([(30, 66), (42, 70)], OUTC, 'f', False, False, 2.6), L([(70, 66), (58, 70)], OUTC, 'f', False, False, 2.6),
                L([(48, 62), (50, 68), (52, 62)], OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(54, 70), (58, 56), (76, 52), (88, 36), (80, 16), (58, 6), (32, 8), (12, 22), (2, 50), (0, 84), (8, 104), (28, 106), (44, 96), (50, 82)])),
             L(outline([(2, 46), (26, 52), (34, 98), (10, 98)]), 'shade', 'b', False),
             L(quad((4, 70), (-10, 66), (-12, 80)), 'mid', 'b', False, False, 2.4),
             fringe([(62, 8), (86, 20), (92, 44), (88, 64, 1), (80, 46), (72, 34)])] + side_eye(76),
    'back': [L(outline([(10, 102), (2, 74), (4, 40), (18, 18), (50, 10), (82, 18), (96, 40), (98, 74), (90, 102), (70, 110), (30, 110)])),
             L(outline([(56, 12), (84, 22), (98, 50), (94, 100), (66, 108), (70, 50)]), 'shade', 'b', False),
             L(quad((6, 70), (-10, 64), (-14, 76)), 'mid', 'b', False, False, 2.4), L(quad((94, 70), (110, 64), (114, 76)), 'mid', 'b', False, False, 2.4),
             strand([(50, 12), (50, 40)], 'deep', 'b', 1.2)],
}

# Lunk Ironbrow (Hirata Taizou): grandullón; melena verde oscuro peinada hacia atrás que le cae lisa hasta la espalda,
# frente ancha, ojos medio cerrados con los párpados morados y la boca seria
CHARS['lunk-ironbrow'] = {
    'body': 'corpulento', 'pal': pal('#1e4a2e', '#e0a070', shade='#163a22', deep='#0e2a18', lid='#5a4a8a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': [(16, 60), (20, 30), (36, 22), (50, 24), (64, 22), (80, 30), (84, 60)],
             'face_front': WIDE_FACE},
    'front': [L(outline([(2, 112), (0, 80), (6, 40), (18, 12), (40, 2), (60, 2), (82, 12), (94, 40), (100, 80), (98, 112), (86, 104), (84, 60), (16, 60), (14, 104)])),
              L(outline([(60, 4), (82, 14), (96, 44), (98, 108), (86, 100), (84, 50)]), 'shade', 'b', False),
              strand([(30, 10), (24, 40)], 'deep', 'b', 1.0), strand([(50, 4), (50, 22)], 'deep', 'b', 1.0), strand([(70, 10), (76, 40)], 'deep', 'b', 1.0),
              L(outline([(26, 70), (44, 70), (44, 80), (26, 80)]), 'lid', 'f', ln=True), L(outline([(56, 70), (74, 70), (74, 80), (56, 80)]), 'lid', 'f', ln=True),
              L(outline([(28, 74), (42, 74), (42, 79), (28, 79)]), WHITE, 'f', False), L(outline([(58, 74), (72, 74), (72, 79), (58, 79)]), WHITE, 'f', False),
              L(ell(36, 76, 1.6, 2), OUTC, 'f', False), L(ell(64, 76, 1.6, 2), OUTC, 'f', False),
              L([(28, 58), (42, 60)], OUTC, 'f', False, False, 1.0), L([(72, 58), (58, 60)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(52, 60), (56, 40), (70, 20), (66, 4), (44, -4), (20, 2), (4, 24), (-6, 60), (-16, 100), (-20, 120, 1), (-2, 108), (10, 112, 1), (18, 92),
                        (32, 74), (44, 66)])),
             L(outline([(-4, 50), (16, 54), (14, 96), (-12, 104)]), 'shade', 'b', False),
             L(outline([(76, 70), (90, 70), (90, 80), (76, 80)]), 'lid', 'f', ln=True), L(ell(86, 77, 1.4, 1.6), OUTC, 'f', False)],
    'back': [L(outline([(4, 116), (0, 80), (6, 40), (18, 12), (40, 0), (60, 0), (82, 12), (94, 40), (100, 80), (96, 116), (76, 122), (50, 118), (24, 122)])),
             L(outline([(56, 2), (82, 12), (96, 44), (98, 112), (70, 120), (70, 50)]), 'shade', 'b', False),
             strand([(30, 10), (24, 60), (28, 112)], 'deep', 'b', 1.0), strand([(50, 4), (50, 114)], 'deep', 'b', 1.0), strand([(70, 10), (76, 60), (72, 112)], 'deep', 'b', 1.0)],
}

# Hefton Bulk (Moriagari Moko): cabeza redondísima y gorda, con un casquete de pelo verde agua en punta arriba; ojos de
# punto, bigotes de tres rayas, nariz rosada y una sonrisa con los dos dientes de conejo
_hefton_face = blob([(10, 66), (24, 50), (50, 44), (76, 50), (90, 66), (94, 86), (86, 104), (66, 114), (50, 116), (34, 114), (14, 104), (6, 86)])
CHARS['hefton-bulk'] = {
    'body': 'corpulento', 'pal': pal('#5a9a8a', '#f2b080', shade='#3e7a6a', nose='#f08a80'),
    'face': {'eyes': 'dot', 'eye_y': 68, 'eye_sep': 12, 'brows': False, 'mouth': 'none', 'hairline': False, 'face_front': _hefton_face, 'nose': (50, 76, 2.6)},
    'front': [L(outline([(18, 62), (24, 44), (42, 26), (50, 14, 1), (58, 26), (76, 44), (82, 62), (70, 54), (50, 50), (30, 54)])),
              L(outline([(56, 26), (74, 44), (80, 58), (66, 52)]), 'shade', 'b', False),
              L(quad((38, 84), (50, 92), (62, 84)), OUTC, 'f', False, False, 1.6),
              L(outline([(45, 88), (55, 88), (55, 96), (45, 96)]), WHITE, 'f', ln=True), L([(50, 88), (50, 96)], OUTC, 'f', False, False, 0.8),
              L([(24, 78), (34, 78)], OUTC, 'f', False, False, 1.0), L([(66, 78), (76, 78)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(30, 54), (40, 34), (56, 18), (70, 28), (80, 46), (70, 56), (50, 58)])),
             L(outline([(30, 54), (36, 40), (46, 50)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 72), (22, 50), (40, 30), (50, 16, 1), (60, 30), (78, 50), (84, 72), (50, 78)])),
             L(outline([(56, 30), (76, 50), (82, 70), (60, 74)]), 'shade', 'b', False)],
}
CHARS['hefton-bulk']['face']['face_side'] = blob([(40, 112), (14, 100), (4, 76), (10, 52), (30, 40), (56, 40), (80, 52), (96, 70), (98, 92), (86, 108), (64, 116)])

# Barry Cade (Banri Nagamine): cara enorme y alargada de mandíbula ancha, con el pelo azul claro cortado como una almena
# de castillo (un bloque recto con cinco dientes arriba); grita enseñando todos los dientes y frunce mucho las cejas
_barry_face = blob([(14, 50), (50, 44), (86, 50), (92, 80), (92, 108), (80, 122), (50, 126), (20, 122), (8, 108), (8, 80)])
_crenel = [(16, 52), (16, 6), (24, 6), (24, -2), (32, -2), (32, 6), (40, 6), (40, -2), (48, -2), (48, 6), (54, 6), (54, -2), (62, -2), (62, 6), (70, 6), (70, -2),
           (78, -2), (78, 6), (84, 6), (84, 52), (70, 46), (50, 44), (30, 46)]
CHARS['barry-cade'] = {
    'body': 'corpulento', 'pal': pal('#8ab8d0', '#f6c8a0', shade='#5a6a78', deep='#3e4a58', nose='#e8a080'),
    'face': {'eyes': 'round', 'eye_y': 60, 'eye_sep': 10, 'brows': 'angry', 'mouth': 'none', 'hairline': False, 'face_front': _barry_face,
             'nose': (50, 64, 3), 'big_ears': 2, 'ear_out': 6},
    'front': [L([(x, y) for x, y in _crenel]), L(outline([(60, 6), (84, 6), (84, 50), (66, 44)]), 'shade', 'b', False),
              L(outline([(24, 76), (76, 76), (80, 100), (70, 108), (30, 108), (20, 100)]), TEETH_L, 'f', ln=True),
              L(outline([(26, 78), (74, 78), (77, 98), (68, 105), (32, 105), (23, 98)]), WHITE, 'f', False),
              L([(23, 91), (77, 91)], OUTC, 'f', False, False, 1.2)] + [L([(x, 78), (x, 104)], OUTC, 'f', False, False, 1.0) for x in (36, 44, 50, 56, 64)],
    'side': [L(outline([(16, 64), (14, 4), (24, 4), (24, -4), (36, -4), (36, 4), (46, 4), (46, -4), (58, -4), (58, 4), (70, 4), (70, -4), (82, -4), (82, 4),
                        (86, 50), (70, 46), (54, 54), (40, 52), (28, 70)])),
             L(outline([(14, 4), (40, 4), (40, 52), (28, 70), (16, 64)]), 'deep', 'b', False),
             L(outline([(84, 76), (98, 74), (98, 104), (86, 106)]), WHITE, 'f', ln=True)],
    'back': [L(outline([(16, 60), (16, -2), (24, -2), (24, 4), (32, 4), (32, -2), (40, -2), (40, 4), (48, -2), (56, -2), (56, 4), (64, 4), (64, -2), (72, -2),
                        (72, 4), (84, 4), (84, 60), (70, 66), (30, 66)])),
             L(outline([(50, -2), (84, -2), (84, 60), (52, 66)]), 'deep', 'b', False)],
}
CHARS['barry-cade']['face']['face_side'] = blob([(40, 120), (14, 108), (8, 70), (14, 40), (40, 36), (70, 40), (90, 60), (96, 86), (98, 110), (80, 124), (60, 126)])

# Rick Wall (Buroku Tsumio): una torre de ladrillos grises altísima por sombrero, con dos tiras que bajan hasta los hombros;
# antifaz negro de ladrón, piel morena y el pelo azul marino recogido en un pañuelo con una trenza corta detrás
_bricks_f = [L(outline([(10, 60), (8, -40), (92, -40), (90, 60)]), 'brick'), L(outline([(60, -40), (92, -40), (90, 60), (66, 60)]), 'brick_d', 'b', False)]
for _y in (-24, -6, 12, 30, 46):
    _bricks_f.append(L([(9, _y), (91, _y)], 'mortar', 'b', False, False, 1.6))
for _x, _y0, _y1 in ((30, -40, -24), (60, -40, -24), (44, -24, -6), (74, -24, -6), (24, -6, 12), (56, -6, 12), (38, 12, 30), (70, 12, 30), (28, 30, 46), (62, 30, 46)):
    _bricks_f.append(L([(_x, _y0), (_x, _y1)], 'mortar', 'b', False, False, 1.4))
CHARS['rick-wall'] = {
    'body': 'normal', 'pal': pal('#2e4a6a', '#a8704a', brick='#c8c4c8', brick_d='#9a8a90', mortar='#6a5a62', mask='#141414'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 98, 'hairline': False},
    'front': _bricks_f + [L([(12, 60), (12, 116)], 'brick_d', 'f', False, False, 3.6), L([(88, 60), (88, 116)], 'brick_d', 'f', False, False, 3.6),
                          L(outline([(14, 64), (86, 64), (88, 80), (50, 84), (12, 80)]), 'mask', 'f', ln=True),
                          L(outline([(24, 70), (40, 68), (44, 76), (28, 78)]), WHITE, 'f', False), L(outline([(76, 70), (60, 68), (56, 76), (72, 78)]), WHITE, 'f', False),
                          L(ell(36, 74, 2, 2.4), OUTC, 'f', False), L(ell(64, 74, 2, 2.4), OUTC, 'f', False),
                          L(outline([(6, 92), (16, 88), (18, 104), (8, 110)]), 'mid', 'b', ln=True)],
    'side': [L(outline([(0, 64), (6, -40), (94, -40), (90, 54), (70, 60), (20, 64)]), 'brick'), L(outline([(0, 64), (6, -40), (40, -40), (36, 62)]), 'brick_d', 'b', False),
             L([(4, -22), (92, -22)], 'mortar', 'b', False, False, 1.6), L([(3, -4), (91, -4)], 'mortar', 'b', False, False, 1.6),
             L([(2, 14), (91, 14)], 'mortar', 'b', False, False, 1.6), L([(1, 32), (90, 32)], 'mortar', 'b', False, False, 1.6),
             L(outline([(10, 60), (36, 56), (40, 80), (22, 90), (6, 82)])), L(outline([(16, 86), (2, 96), (-6, 108), (6, 104), (20, 96)]), 'mid', 'b', ln=True),
             L(outline([(60, 66), (92, 66), (92, 80), (62, 80)]), 'mask', 'f', ln=True), L(outline([(80, 70), (90, 70), (88, 76), (82, 76)]), WHITE, 'f', False),
             L([(46, 60), (46, 112)], 'brick_d', 'f', False, False, 3.2)],
    'back': _bricks_f + [L([(12, 60), (12, 116)], 'brick_d', 'f', False, False, 3.6), L([(88, 60), (88, 116)], 'brick_d', 'f', False, False, 3.6),
                         L(outline([(16, 60), (84, 60), (80, 86), (50, 92), (20, 86)])),
                         L(outline([(40, 82), (60, 82), (64, 96), (56, 110), (44, 110), (36, 96)]), 'mid', 'f', ln=True)],
}

# Ivor Shield (Tateno Tatsuo): un visor rojo enorme con marco plateado y remaches que le tapa los ojos; el pelo gris morado
# oscuro recogido en un turbante que le baja por los lados, con trenzas finas hasta los hombros y una trenza gruesa detrás
CHARS['ivor-shield'] = {
    'body': 'normal', 'pal': pal('#4a4058', '#c08a5a', shade='#342c40', deep='#221c2c', visor='#9a1e1e', visor_l='#d04a4a', frame='#d8ccd0', frame_d='#9a8a90'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 100), (6, 60), (8, 20), (24, -8), (50, -18), (76, -8), (92, 20), (94, 60), (90, 100), (82, 80), (80, 60), (20, 60), (18, 80)])),
              L(outline([(58, -14), (80, -4), (94, 30), (92, 96), (82, 70)]), 'shade', 'b', False),
              L(outline([(12, 96), (8, 104), (12, 112), (16, 104)]), 'mid', 'f', ln=True), L(outline([(88, 96), (92, 104), (88, 112), (84, 104)]), 'mid', 'f', ln=True),
              L(outline([(14, 14), (26, 2), (50, -2), (74, 2), (86, 14), (88, 44), (78, 64), (50, 70), (22, 64), (12, 44)]), 'frame', 'f', ln=True),
              L(outline([(22, 18), (34, 8), (66, 8), (78, 18), (80, 42), (72, 58), (50, 62), (28, 58), (20, 42)]), 'visor', 'f', ln=True),
              L(ell(42, 20, 8, 4), 'visor_l', 'f', False),
              L(ell(18, 30, 1.6, 1.6), OUTC, 'f', False), L(ell(82, 30, 1.6, 1.6), OUTC, 'f', False), L(ell(50, 66, 1.6, 1.6), OUTC, 'f', False)],
    'side': [L(outline([(60, 50), (66, 24), (70, -2), (44, -16), (18, -10), (2, 14), (0, 60), (2, 94), (14, 100), (26, 92), (40, 76), (54, 64)])),
             L(outline([(0, 40), (24, 46), (30, 90), (6, 92)]), 'shade', 'b', False),
             L(outline([(22, 92), (18, 104), (22, 118), (26, 106)]), 'mid', 'b', ln=True),
             L(outline([(86, 14), (96, 20), (98, 56), (90, 64), (84, 60)]), 'frame', 'f', ln=True), L(outline([(92, 22), (98, 26), (98, 52), (92, 56)]), 'visor', 'f', False)],
    'back': [L(outline([(10, 100), (6, 60), (8, 20), (24, -8), (50, -18), (76, -8), (92, 20), (94, 60), (90, 100), (70, 108), (30, 108)])),
             L(outline([(56, -14), (80, -4), (94, 30), (92, 98), (66, 106), (70, 40)]), 'shade', 'b', False),
             L(outline([(44, 30), (56, 30), (58, 60), (56, 90), (50, 112), (44, 90), (42, 60)]), 'deep', 'f', ln=True),
             strand([(44, 46), (56, 46)], 'mid', 'f', 1.0), strand([(44, 62), (56, 62)], 'mid', 'f', 1.0), strand([(44, 78), (56, 78)], 'mid', 'f', 1.0),
             L(outline([(10, 96), (6, 104), (10, 112), (14, 104)]), 'mid', 'f', ln=True), L(outline([(90, 96), (94, 104), (90, 112), (86, 104)]), 'mid', 'f', ln=True)],
}

# Rocky Hardcastle (Tetsugoushi Kogorou): pelo castaño muy oscuro en casco con las puntas hacia fuera bajo las orejas y un
# flequillo blanco crema cayendo a un lado; orejas en punta, ojos amarillos afilados con ojeras y la piel morena clara
CHARS['rocky-hardcastle'] = {
    'body': 'normal', 'pal': pal('#3e3430', '#d89a68', iris='#e0c020', shade='#2c2420', cream='#f2ead6', cream_d='#d8c8b0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'hairline': False, 'big_ears': 1},
    'front': [L(outline([(16, 96), (6, 98, 1), (12, 84), (8, 50), (12, 20), (30, 2), (50, -4), (70, 2), (88, 20), (92, 50), (88, 84), (94, 98, 1), (84, 96), (82, 60),
                         (18, 60)])),
              L(outline([(60, 2), (84, 16), (92, 50), (86, 88), (80, 50)]), 'shade', 'b', False),
              fringe([(12, 60), (14, 34), (26, 14), (46, 6), (70, 10), (84, 26), (88, 50), (76, 46), (62, 48), (50, 58, 1), (46, 46), (30, 50), (16, 58)]),
              L(outline([(26, 14), (46, 6), (62, 10), (58, 30), (54, 48), (46, 56, 1), (44, 44), (32, 48), (22, 40)]), 'cream', 'f', ln=True),
              L(outline([(48, 10), (60, 12), (54, 40)]), 'cream_d', 'f', False),
              L([(30, 84), (40, 84)], OUTC, 'f', False, False, 0.8), L([(70, 84), (60, 84)], OUTC, 'f', False, False, 0.8)],
    'side': [L(outline([(54, 62), (58, 50), (78, 46), (90, 32), (88, 12), (66, -4), (38, -4), (14, 8), (4, 32), (4, 62), (10, 80), (2, 92, 1), (20, 88), (26, 98, 1),
                        (36, 86), (46, 74)])),
             L(outline([(4, 34), (24, 40), (30, 80), (10, 78)]), 'shade', 'b', False),
             L(outline([(68, 4), (86, 10), (94, 30), (92, 52, 1), (84, 40), (76, 28)]), 'cream', 'f', ln=True)],
    'back': [L(outline([(14, 86), (4, 98, 1), (10, 80), (8, 50), (12, 20), (30, 2), (50, -4), (70, 2), (88, 20), (92, 50), (90, 80), (96, 98, 1), (86, 86), (70, 96, 1),
                        (60, 88), (50, 98, 1), (40, 88), (30, 96, 1)])),
             L(outline([(56, 2), (84, 16), (92, 50), (88, 84), (64, 90)]), 'shade', 'b', False)],
}

# Sebastian Fortwright (Iwagaki Noborou): pelo negro corto por los lados que sube en un tupé enorme de pinchos morados
# hacia arriba y atrás; ojos rojizos afilados y cejas muy fruncidas
CHARS['sebastian-fortwright'] = {
    'body': 'normal', 'pal': pal('#1e1a22', '#f2c8a4', iris='#8a3a2a', shade='#141016', top='#6a4ac0', top_d='#4a2e98'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 64), (12, 34), (24, 18), (76, 18), (88, 34), (86, 64), (80, 52), (20, 52)])),
              L(outline([(14, 30), (10, 4), (2, -14, 1), (18, -2), (20, -24, 1), (34, -10), (44, -30, 1), (54, -12), (66, -32, 1), (70, -10), (88, -24, 1), (84, -2),
                         (100, 0, 1), (90, 16), (104, 22, 1), (86, 32), (70, 24), (50, 20), (30, 24)]), 'top', 'b'),
              L(outline([(60, -10), (88, -22), (86, 0), (98, 2), (88, 18), (70, 22)]), 'top_d', 'b', False),
              fringe([(14, 54), (16, 34), (30, 22), (50, 18), (70, 22), (84, 34), (86, 54), (78, 44), (70, 52, 1), (64, 40), (56, 50, 1), (52, 38), (46, 50, 1),
                      (40, 38), (30, 50, 1), (24, 40)])],
    'side': [L(outline([(56, 56), (62, 44), (80, 42), (90, 28), (86, 12), (70, 6), (40, 6), (16, 16), (8, 40), (12, 60), (26, 70), (44, 64)])),
             L(outline([(70, 10), (84, 0), (80, -16), (62, -26), (40, -32), (16, -34, 1), (30, -22), (6, -16, 1), (20, -8), (0, 0, 1), (16, 6), (6, 18, 1), (24, 16),
                        (44, 12)]), 'top', 'b'),
             L(outline([(16, -34), (40, -30), (30, -20), (6, -16)]), 'top_d', 'b', False)],
    'back': [L(outline([(16, 78), (12, 40), (24, 18), (76, 18), (88, 40), (84, 78), (50, 84)])),
             L(outline([(14, 30), (10, 4), (2, -14, 1), (18, -2), (20, -24, 1), (34, -10), (44, -30, 1), (54, -12), (66, -32, 1), (70, -10), (88, -24, 1), (84, -2),
                        (100, 0, 1), (90, 16), (104, 22, 1), (86, 36), (70, 30), (50, 34), (30, 30)]), 'top', 'b'),
             L(outline([(56, -12), (88, -24), (84, 0), (100, 2), (88, 30), (60, 30)]), 'top_d', 'b', False)],
}

# Waldo Gibbons (Ugou Sarukichi): melena castaña rojiza de pinchos que le rodea toda la cabeza como la de un mono, con un
# pico alto en medio; el pelo le enmarca la cara en una máscara de mono hasta la barbilla; ojos rojos afilados
CHARS['waldo-gibbons'] = {
    'body': 'normal', 'pal': pal('#8a4a24', '#f0b888', iris='#b02020', shade='#6a3418', deep='#4a2410'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(14, 96), (0, 80, 1), (8, 68), (-14, 52, 1), (6, 44), (2, 22, 1), (20, 24), (24, 2, 1), (38, 10), (50, -26, 1), (62, 10), (76, 2, 1),
                         (80, 24), (98, 22, 1), (94, 44), (114, 52, 1), (92, 68), (100, 80, 1), (86, 96), (82, 66), (18, 66)])),
              L(outline([(58, 6), (76, 4), (80, 26), (96, 46), (90, 90), (82, 60)]), 'shade', 'b', False),
              L(outline([(14, 70), (18, 50), (32, 40), (44, 48), (50, 40, 1), (56, 48), (68, 40), (82, 50), (86, 70), (84, 92), (74, 88), (78, 66), (66, 56), (50, 60),
                         (34, 56), (22, 66), (26, 88), (16, 92)]), 'mid', 'f'),
              L(outline([(46, 84), (54, 84), (50, 90)]), 'shade', 'f', False)],
    'side': [L(outline([(56, 62), (60, 48), (74, 46), (84, 30), (78, 10), (60, -20, 1), (50, 6), (28, -8, 1), (26, 14), (-2, 6, 1), (10, 28), (-14, 40, 1), (6, 50),
                        (-10, 66, 1), (10, 70), (2, 88, 1), (20, 84), (24, 100, 1), (36, 86), (46, 78)])),
             L(outline([(2, 34), (24, 40), (28, 80), (8, 76)]), 'shade', 'b', False),
             L(outline([(64, 46), (82, 48), (92, 62), (86, 90), (78, 92), (82, 66), (70, 58)]), 'mid', 'f')],
    'back': [L(outline([(14, 96), (-2, 84, 1), (8, 70), (-14, 54, 1), (6, 44), (2, 22, 1), (20, 24), (24, 2, 1), (38, 10), (50, -26, 1), (62, 10), (76, 2, 1),
                        (80, 24), (98, 22, 1), (94, 44), (114, 54, 1), (92, 70), (102, 84, 1), (86, 96), (70, 104, 1), (60, 96), (50, 106, 1), (40, 96), (30, 104, 1)])),
             L(outline([(56, 6), (76, 4), (80, 26), (96, 46), (90, 94), (66, 100), (70, 50)]), 'shade', 'b', False),
             strand([(30, 30), (40, 56), (32, 86)], 'deep', 'b', 1.0), strand([(70, 30), (60, 56), (68, 86)], 'deep', 'b', 1.0)],
}

# Iggy Motte (Ishikabe Yamori): piel morena; pelo gris oscuro corto como un gorro, con cuatro coletas finas que salen como
# ramas (dos arriba hacia los lados y dos por debajo de las orejas) acabadas en mechones de hoja; boca abierta enorme
_leaf = lambda x, y: L(outline([(x - 6, y), (x - 2, y - 6), (x, y - 2), (x + 3, y - 7), (x + 6, y), (x + 2, y + 2), (x + 4, y + 7), (x, y + 4), (x - 4, y + 7)]), 'mid', 'f', ln=True)
CHARS['iggy-motte'] = {
    'body': 'normal', 'pal': pal('#5a5a58', '#a0704a', shade='#444442', mouth='#c8506a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'none', 'hairline': (52, 46)},
    'front': [L(outline([(14, 66), (12, 34), (24, 14), (50, 6), (76, 14), (88, 34), (86, 66), (80, 52), (20, 52)])),
              L(outline([(60, 8), (82, 20), (88, 44), (84, 62), (76, 40)]), 'shade', 'b', False),
              fringe([(14, 50), (18, 32), (30, 22), (40, 30), (50, 22), (60, 30), (70, 22), (84, 34), (86, 50), (74, 44), (60, 44), (50, 48), (40, 44), (26, 44)]),
              L(quad((22, 22), (10, 14), (-8, 16)), 'mid', 'f', False, False, 2.6), L(quad((78, 22), (90, 14), (108, 16)), 'mid', 'f', False, False, 2.6),
              _leaf(-10, 16), _leaf(110, 16),
              L(quad((16, 66), (4, 84), (8, 100)), 'mid', 'f', False, False, 2.6), L(quad((84, 66), (96, 84), (92, 100)), 'mid', 'f', False, False, 2.6),
              _leaf(6, 104), _leaf(94, 104),
              L(outline([(32, 88), (68, 88), (60, 104), (50, 108), (40, 104)]), 'mouth', 'f', ln=True),
              L(outline([(34, 88), (66, 88), (62, 93), (38, 93)]), WHITE, 'f', False)],
    'side': [L(outline([(56, 54), (62, 42), (80, 40), (88, 26), (80, 8), (56, 0), (30, 4), (12, 18), (4, 40), (8, 62), (22, 72), (40, 66)])),
             L(outline([(4, 36), (24, 40), (26, 66), (10, 60)]), 'shade', 'b', False),
             L(quad((52, 14), (60, 2), (66, -8)), 'mid', 'f', False, False, 2.6), _leaf(66, -10),
             L(quad((20, 70), (10, 90), (16, 104)), 'mid', 'b', False, False, 2.6), _leaf(16, 108),
             L(outline([(80, 90), (96, 88), (94, 100), (84, 102)]), 'mouth', 'f', ln=True)],
    'back': [L(outline([(14, 76), (12, 34), (24, 14), (50, 6), (76, 14), (88, 34), (86, 76), (50, 82)])),
             L(outline([(56, 8), (82, 20), (88, 50), (82, 74), (60, 78)]), 'shade', 'b', False),
             L(quad((22, 22), (10, 14), (-8, 16)), 'mid', 'f', False, False, 2.6), L(quad((78, 22), (90, 14), (108, 16)), 'mid', 'f', False, False, 2.6),
             _leaf(-10, 16), _leaf(110, 16),
             L(quad((16, 70), (4, 86), (8, 100)), 'mid', 'f', False, False, 2.6), L(quad((84, 70), (96, 86), (92, 100)), 'mid', 'f', False, False, 2.6),
             _leaf(6, 104), _leaf(94, 104)],
}

# Corbin Brickham (Kakoi Kouken): pelo castaño grisáceo en media melena con flequillo de mechones, una cinta blanca fina
# alrededor de la cabeza y un mechón en arco que sale de lo alto; ojos rojizos afilados
CHARS['corbin-brickham'] = {
    'body': 'normal', 'pal': pal('#7a6658', '#fcd8b4', iris='#c04a58', shade='#5e4c40', band='#f0eaea'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(quad((40, 4), (52, -26), (66, 2)), 'mid', 'b', False, False, 3.0),
              L(outline([(10, 96), (6, 62), (8, 26), (24, 6), (50, -2), (76, 6), (92, 26), (94, 62), (90, 96), (82, 76), (82, 60), (18, 60), (18, 76)])),
              L(outline([(60, 2), (86, 14), (94, 44), (92, 88), (82, 60)]), 'shade', 'b', False),
              fringe([(12, 78), (12, 46), (24, 40), (50, 38), (76, 40), (88, 46), (88, 78), (80, 62), (74, 70, 1), (68, 52), (58, 62, 1), (54, 48), (46, 64, 1),
                      (40, 50), (32, 62, 1), (26, 52), (20, 70, 1)]),
              L(outline([(8, 30), (50, 26), (92, 30), (92, 36), (50, 32), (8, 36)]), 'band', 'f', ln=True)],
    'side': [L(quad((36, 2), (40, -28), (58, -6)), 'mid', 'b', False, False, 3.0),
             L(outline([(54, 62), (58, 50), (80, 48), (94, 34), (88, 10), (64, -4), (34, -2), (12, 12), (2, 40), (0, 76), (-6, 92, 1), (10, 84), (16, 100, 1), (28, 84),
                        (42, 76)])),
             L(outline([(2, 40), (22, 44), (26, 82), (8, 80)]), 'shade', 'b', False),
             L(outline([(2, 30), (50, 24), (94, 34), (94, 40), (50, 30), (2, 36)]), 'band', 'f', ln=True),
             fringe([(64, 34), (90, 38), (96, 48), (94, 66, 1), (86, 52), (80, 62, 1), (76, 46)])],
    'back': [L(quad((40, 4), (52, -26), (66, 2)), 'mid', 'b', False, False, 3.0),
             L(outline([(10, 96), (4, 62), (8, 26), (24, 6), (50, -2), (76, 6), (92, 26), (96, 62), (90, 96), (74, 104, 1), (64, 94), (50, 102, 1), (36, 94), (26, 104, 1)])),
             L(outline([(56, 2), (86, 14), (96, 50), (90, 94), (64, 98), (70, 50)]), 'shade', 'b', False),
             L(outline([(6, 30), (50, 26), (94, 30), (94, 36), (50, 32), (6, 36)]), 'band', 'f', ln=True)],
}

# Helena Harwood (Kofun Miko, portera): melena gris oscura muy larga, recogida en una coleta alta con una goma blanca y
# adornos de bloques rojos y blancos a los lados; un rizo en bucle sobre la frente, mechones largos junto a la cara y los ojos
# cerrados
_blocks = [L(outline([(2, 18), (12, 18), (12, 28), (2, 28)]), 'red', 'f', ln=True), L(outline([(88, 18), (98, 18), (98, 28), (88, 28)]), 'red', 'f', ln=True),
           L(outline([(12, 8), (24, 8), (24, 16), (12, 16)]), 'pink', 'f', ln=True), L(outline([(76, 8), (88, 8), (88, 16), (76, 16)]), 'pink', 'f', ln=True),
           L(outline([(26, 0), (36, 0), (36, 8), (26, 8)]), 'red', 'f', ln=True), L(outline([(64, 0), (74, 0), (74, 8), (64, 8)]), 'red', 'f', ln=True)]
CHARS['helena-harwood'] = {
    'body': 'chica', 'pal': pal('#4a4642', '#fcdcc0', shade='#36322e', deep='#24201e', red='#b03040', pink='#e8a0a8', tie='#f0eeee', blush='#f0a0a0'),
    'face': {'eyes': 'closed', 'brows': True, 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(42, 4), (40, -14), (50, -22), (60, -14), (58, 4)]), 'mid', 'b', ln=True),
              L(outline([(0, 118), (4, 80), (6, 40), (16, 14), (50, 2), (84, 14), (94, 40), (96, 80), (100, 118), (86, 108), (82, 62), (18, 62), (14, 108)])),
              L(outline([(60, 6), (84, 16), (94, 44), (98, 112), (86, 104), (82, 50)]), 'shade', 'b', False),
              L(outline([(42, -6), (58, -6), (58, -2), (42, -2)]), 'tie', 'f', ln=True),
              fringe([(12, 70), (14, 40), (28, 20), (50, 14), (72, 20), (86, 40), (88, 70), (80, 56), (70, 46), (60, 44), (50, 48), (40, 44), (30, 46), (20, 56)]),
              L(ell(50, 32, 6, 8) + [ell(50, 32, 6, 8)[0]], 'deep', 'f', False, False, 2.4),
              L(ell(30, 84, 3.6, 2), 'blush', 'f', False), L(ell(70, 84, 3.6, 2), 'blush', 'f', False)] + _blocks,
    'side': [L(outline([(40, 6), (32, -16), (44, -24), (50, -8), (40, -4), (24, 10), (10, 40), (0, 80), (-6, 112, 1), (8, 96), (16, 70), (26, 40)]), 'mid', 'b'),
             L(outline([(54, 62), (58, 50), (80, 48), (92, 34), (88, 14), (66, 0), (40, 2), (18, 16), (8, 40), (10, 66), (24, 76), (44, 70)])),
             L(outline([(36, -8), (46, -12), (48, -4), (38, 0)]), 'tie', 'f', ln=True),
             L(outline([(36, 0), (46, 2), (44, 10), (34, 8)]), 'red', 'f', ln=True),
             fringe([(64, 2), (88, 16), (94, 40), (92, 100), (84, 104), (84, 56), (76, 40)]), L(ell(86, 84, 3, 2), 'blush', 'f', False)],
    'back': [L(outline([(42, 4), (40, -14), (50, -22), (60, -14), (58, 4)]), 'mid', 'b', ln=True),
             L(outline([(0, 116), (4, 80), (6, 40), (16, 14), (50, 2), (84, 14), (94, 40), (96, 80), (100, 116), (70, 118), (50, 114), (30, 118)])),
             L(outline([(56, 4), (84, 14), (96, 46), (98, 112), (66, 116), (70, 50)]), 'shade', 'b', False),
             L(outline([(42, -6), (58, -6), (58, -2), (42, -2)]), 'tie', 'f', ln=True),
             strand([(50, 4), (50, 110)], 'deep', 'b', 1.0), strand([(28, 20), (18, 110)], 'deep', 'b', 1.0), strand([(72, 20), (82, 110)], 'deep', 'b', 1.0)] + _blocks,
}

# Dane Upchurch (Tsukauchi Ryuuki): un cráneo de ciervo blanco puesto como casco (cuencas negras y nariz en dos rayas) con
# dos astas que suben a los lados; por debajo, el pelo castaño en puntas; ojos redondos enormes, coloretes y sonrisa
_skull_f = [L(outline([(16, 66), (12, 40), (22, 18), (50, 8), (78, 18), (88, 40), (84, 66), (70, 72), (50, 82, 1), (30, 72)]), 'bone', 'b', ln=True),
            L(outline([(58, 12), (78, 20), (88, 42), (82, 62), (70, 40)]), 'bone_d', 'b', False),
            L(outline([(26, 34), (36, 30), (44, 40), (40, 54), (28, 54), (22, 44)]), OUTC, 'f', False),
            L(outline([(74, 34), (64, 30), (56, 40), (60, 54), (72, 54), (78, 44)]), OUTC, 'f', False),
            L([(46, 60), (46, 68)], OUTC, 'f', False, False, 2.2), L([(54, 60), (54, 68)], OUTC, 'f', False, False, 2.2)]
_antlers = [L(quad((24, 20), (18, 0), (22, -22)), 'horn', 'b', False, False, 4.2), L(quad((20, 4), (6, 4), (0, -10)), 'horn', 'b', False, False, 3.4),
            L(quad((76, 20), (82, 0), (78, -22)), 'horn', 'b', False, False, 4.2), L(quad((80, 4), (94, 4), (100, -10)), 'horn', 'b', False, False, 3.4)]
CHARS['dane-upchurch'] = {
    'body': 'normal', 'pal': pal('#7a4a2a', '#fcdcc0', shade='#5e3820', bone='#f0eadc', bone_d='#cfc4b4', horn='#6a5a40', blush='#f08a8a'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False, 'eye_y': 82},
    'front': _antlers + [L(outline([(12, 96), (0, 90, 1), (8, 78), (-4, 70, 1), (10, 64), (14, 50), (86, 50), (90, 64), (104, 70, 1), (92, 78), (100, 90, 1), (88, 96),
                                    (82, 72), (18, 72)])),
                         L(outline([(16, 72), (24, 62), (34, 70), (42, 62), (50, 72, 1), (58, 62), (66, 70), (76, 62), (84, 72), (70, 74), (30, 74)]), 'mid', 'f')]
             + _skull_f + [L(ell(30, 92, 3.6, 2.2), 'blush', 'f', False), L(ell(70, 92, 3.6, 2.2), 'blush', 'f', False)],
    'side': [L(quad((44, 14), (40, -6), (46, -26)), 'horn', 'b', False, False, 4.2),
             L(outline([(54, 66), (60, 54), (80, 52), (90, 38), (84, 14), (60, 4), (34, 6), (14, 20), (6, 44), (-4, 60, 1), (8, 62), (0, 80, 1), (14, 78), (12, 96, 1),
                        (26, 84), (42, 76)])),
             L(outline([(14, 50), (16, 22), (40, 6), (66, 6), (86, 18), (96, 42), (92, 60), (70, 64), (50, 56), (30, 58)]), 'bone', 'f', ln=True),
             L(outline([(76, 34), (88, 34), (90, 50), (78, 52)]), OUTC, 'f', False), L(ell(88, 92, 3, 2), 'blush', 'f', False)],
    'back': _antlers + [L(outline([(12, 96), (0, 90, 1), (8, 78), (-4, 70, 1), (10, 60), (14, 50), (86, 50), (90, 60), (104, 70, 1), (92, 78), (100, 90, 1), (88, 96),
                                   (72, 104, 1), (62, 94), (50, 106, 1), (38, 94), (28, 104, 1)])),
                        L(outline([(56, 54), (86, 54), (90, 80), (84, 96), (62, 98)]), 'shade', 'b', False),
                        L(outline([(14, 64), (12, 40), (22, 18), (50, 8), (78, 18), (88, 40), (86, 64), (50, 70)]), 'bone', 'f', ln=True),
                        L(outline([(56, 12), (78, 18), (88, 40), (86, 62), (60, 66)]), 'bone_d', 'f', False)],
}

# Warden Watchford (Kadotsu Keiei): pelo castaño peinado hacia atrás pegado a la cabeza, con entradas, patillas largas que le
# bajan hasta la mandíbula y una coleta corta en la nuca; ojos blancos redondos, cejas en espiral y una sonrisa ancha
CHARS['warden-watchford'] = {
    'body': 'normal', 'pal': pal('#6a4a30', '#eaaa78', shade='#523822', deep='#3a2818'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': [(12, 66), (14, 40), (22, 26), (36, 22), (50, 28), (64, 22), (78, 26), (86, 40), (88, 66)]},
    'front': [L(outline([(12, 72), (10, 40), (20, 16), (50, 6), (80, 16), (90, 40), (88, 72), (82, 60), (18, 60)])),
              L(outline([(60, 8), (82, 18), (90, 44), (86, 66), (78, 40)]), 'shade', 'b', False),
              strand([(30, 12), (34, 26)], 'deep', 'b', 1.0), strand([(50, 6), (50, 26)], 'deep', 'b', 1.0), strand([(70, 12), (66, 26)], 'deep', 'b', 1.0),
              L(outline([(12, 62), (20, 62), (22, 90), (30, 104), (22, 104), (14, 90)]), 'mid', 'f'),
              L(outline([(88, 62), (80, 62), (78, 90), (70, 104), (78, 104), (86, 90)]), 'mid', 'f')]
             + white_eyes(76, 14, 6, 6, 1.8)
             + [L(ell(33, 62, 5, 3.4) + [ell(33, 62, 5, 3.4)[0]], 'deep', 'f', False, False, 2.0), L(ell(67, 62, 5, 3.4) + [ell(67, 62, 5, 3.4)[0]], 'deep', 'f', False, False, 2.0),
                L(quad((32, 96), (50, 102), (68, 96)), OUTC, 'f', False, False, 1.6), L(quad((42, 86), (50, 90), (58, 86)), OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(48, 60), (54, 40), (76, 30), (84, 14), (62, 0), (34, 0), (12, 14), (2, 40), (4, 66), (14, 80), (30, 76), (44, 68)])),
             L(outline([(16, 72), (2, 74), (-12, 82, 1), (2, 84), (-6, 92, 1), (10, 88), (20, 80)]), 'mid', 'b', ln=True),
             L(outline([(4, 36), (24, 40), (26, 70), (10, 66)]), 'shade', 'b', False),
             L(outline([(62, 60), (70, 60), (72, 84), (80, 96), (72, 96), (64, 84)]), 'mid', 'f'),
             L(ell(86, 62, 4, 3) + [ell(86, 62, 4, 3)[0]], 'deep', 'f', False, False, 2.0)] + side_eye(76),
    'back': [L(outline([(12, 80), (10, 40), (20, 16), (50, 6), (80, 16), (90, 40), (88, 80), (50, 86)])),
             L(outline([(56, 8), (82, 18), (90, 50), (84, 78), (60, 82)]), 'shade', 'b', False),
             L(outline([(42, 78), (58, 78), (66, 90), (72, 100, 1), (58, 94), (50, 102, 1), (42, 94), (28, 100, 1), (34, 90)]), 'mid', 'f', ln=True),
             strand([(30, 14), (30, 76)], 'deep', 'b', 1.0), strand([(50, 6), (50, 78)], 'deep', 'b', 1.0), strand([(70, 14), (70, 76)], 'deep', 'b', 1.0)],
}

# Kabeyama en Ares: el mismo casco de pelo verde, pero más ancho y bajo como una seta, que le tapa hasta los ojos; la cara,
# ancha y corta por debajo, con los labios gruesos y una perilla; ojos pequeños redondos
_jack = copy.deepcopy(CHARS['jack-wallside'])
_jack['face'] = {**_jack['face'], 'eye_y': 82, 'eye_sep': 16, 'mouth_y': 98, 'nose': (50, 90, 4.4), 'ear_out': 9,
                 'face_front': blob([(8, 74), (30, 70), (50, 70), (70, 70), (92, 74), (96, 92), (86, 108), (68, 116), (50, 118), (32, 116), (14, 108), (4, 92)])}
_jack['front'] = [L(blob([(-6, 84), (-8, 56), (6, 30), (30, 14), (50, 10), (70, 14), (94, 30), (108, 56), (106, 84), (90, 78), (50, 76), (10, 78)])),
                  L(blob([(14, 30), (34, 18), (50, 16), (34, 28), (20, 40)], 6), 'light', 'b', False),
                  L(blob([(70, 22), (98, 44), (104, 78), (92, 76), (86, 48)], 6), 'shade', 'b', False),
                  L(blob([(4, 76), (12, 78), (14, 100), (20, 110), (12, 108), (4, 94)]), 'mid', 'f'),
                  L(blob([(96, 76), (88, 78), (86, 100), (80, 110), (88, 108), (96, 94)]), 'mid', 'f'),
                  L(blob([(42, 108), (58, 108), (54, 116), (46, 116)]), 'mid', 'f')]
_jack['back'] = [L(blob([(-6, 88), (-8, 56), (6, 30), (30, 14), (50, 10), (70, 14), (94, 30), (108, 56), (106, 88), (80, 100), (20, 100)])),
                 L(blob([(14, 30), (34, 18), (50, 16), (34, 28), (20, 40)], 6), 'light', 'b', False),
                 L(blob([(60, 30), (100, 50), (102, 86), (74, 98), (80, 60)], 6), 'shade', 'b', False)]
_jack['side'] = [L(blob([(10, 92), (-4, 60), (6, 28), (34, 10), (64, 12), (92, 28), (102, 56), (98, 80), (80, 80), (62, 82), (50, 96), (30, 102)])),
                 L(blob([(22, 26), (44, 14), (62, 16), (44, 26), (28, 36)], 6), 'light', 'b', False),
                 L(blob([(0, 60), (10, 88), (34, 100), (18, 70)], 6), 'shade', 'b', False),
                 L(blob([(70, 80), (76, 80), (78, 100), (86, 110), (78, 110), (70, 100)]), 'mid', 'f')]
_jack['face']['nose_side'] = (92, 90, 4)
CHARS['ares:jack-wallside'] = _jack
