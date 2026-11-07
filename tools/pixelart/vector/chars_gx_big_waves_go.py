"""Big Waves (GO) (gx-big-waves-go): la selección de Australia de Galaxy, con sus modelos 3D de Inazuma Eleven GO Galaxy
como referencia (busto de frente, perfil y espalda, calcados sobre la rejilla de unidades de cabeza)."""
from chars import CHARS, L, OUTC, bumpy, ell, outline, pal, strand  # noqa: F401
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Jude Gordon (portero): melena lisa azul grisácea muy larga, peinada hacia atrás desde una frente despejada y con dos
# mechones que caen pegados a la cara hasta el pecho; cejas fruncidas y boca torcida
CHARS['jude-gordon'] = {
    'body': 'normal', 'pal': pal('#5a88b4', '#fce4bc', iris='#5a4a5a', shade='#4a5878', deep='#3a4660'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': [(16, 66), (20, 50), (34, 40), (50, 42), (66, 40), (80, 50), (84, 66)]},
    'front': [L(outline([(14, 118), (6, 90), (10, 50), (12, 26), (26, 6), (50, 0), (74, 6), (88, 26), (90, 50), (94, 90), (86, 118), (80, 86), (78, 60), (22, 60), (20, 86)])),
              L(outline([(60, 4), (84, 18), (90, 50), (92, 100), (84, 112), (78, 60)]), 'shade', 'b', False),
              L(outline([(16, 54), (10, 90), (14, 120, 1), (20, 100), (22, 64)]), 'mid', 'f'),
              L(outline([(84, 54), (90, 90), (86, 120, 1), (80, 100), (78, 64)]), 'shade', 'f'),
              strand([(30, 10), (24, 40)], 'deep', 'b', 1.0), strand([(50, 4), (44, 38)], 'deep', 'b', 1.0), strand([(70, 10), (74, 40)], 'deep', 'b', 1.0)],
    'side': [L(outline([(66, 46), (82, 40), (90, 26), (80, 6), (56, -4), (30, 0), (10, 16), (0, 46), (-6, 90), (-10, 128, 1), (8, 112), (18, 132, 1), (30, 108), (44, 96),
                        (52, 74), (58, 58)])),
             L(outline([(0, 40), (26, 46), (34, 100), (10, 110)]), 'shade', 'b', False),
             strand([(70, 10), (40, 20), (10, 60)], 'deep', 'b', 1.0), strand([(78, 22), (40, 40), (20, 100)], 'deep', 'b', 1.0)],
    'back': [L(outline([(10, 118), (4, 80), (8, 40), (16, 16), (34, 2), (50, 0), (66, 2), (84, 16), (92, 40), (96, 80), (90, 118), (70, 126, 1), (50, 120), (30, 126, 1)])),
             L(outline([(56, 2), (84, 16), (94, 50), (94, 116), (66, 120), (70, 50)]), 'shade', 'b', False),
             strand([(40, 10), (30, 60), (34, 116)], 'deep', 'b', 1.0), strand([(64, 10), (70, 60), (66, 116)], 'deep', 'b', 1.0)],
}

# Owen Noyster: media melena lisa gris parda (la capa de debajo marrón) que le tapa la mitad derecha de la cara, con un ojo
# dorado a la vista y una sonrisa enseñando los dientes
CHARS['owe-noyster'] = {
    'body': 'normal', 'pal': pal('#bab6a0', '#fcdcbc', iris='#c8a020', shade='#8a6a5c', deep='#6e5248'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 108), (4, 70), (6, 30), (22, 6), (50, -2), (78, 6), (94, 30), (96, 70), (92, 110), (82, 96), (80, 66), (20, 66), (18, 96)]), 'shade'),
              L(outline([(8, 60), (8, 30), (22, 6), (50, -2), (78, 6), (94, 30), (94, 60), (70, 50), (40, 48)]), 'mid', 'b', False),
              fringe([(12, 70), (12, 40), (24, 18), (50, 10), (76, 18), (90, 40), (94, 80), (92, 112, 1), (84, 100), (72, 112, 1), (60, 100), (54, 80), (52, 60),
                      (44, 50), (36, 58), (28, 52), (20, 66, 1)]),
              L(outline([(56, 16), (84, 26), (92, 56), (76, 46), (60, 40)]), 'mid', 'f', False),
              L(outline([(60, 60), (82, 70), (90, 104), (74, 100)]), 'shade', 'f', False),
              strand([(48, 14), (60, 50), (58, 96)], 'deep', 'f', 1.0)],
    'side': [L(outline([(52, 74), (56, 60), (70, 56), (86, 50), (94, 30), (84, 8), (60, -4), (32, -2), (12, 14), (2, 40), (0, 80), (-4, 110, 1), (14, 100), (26, 108, 1),
                        (38, 96), (46, 86)]), 'shade'),
             L(outline([(4, 40), (12, 14), (32, -2), (60, -4), (84, 8), (94, 30), (70, 30), (40, 30)]), 'mid', 'b', False),
             fringe([(66, 2), (90, 18), (96, 44), (94, 70, 1), (86, 56), (80, 66, 1), (76, 46), (66, 32)])],
    'back': [L(outline([(10, 104), (4, 70), (6, 30), (22, 6), (50, -2), (78, 6), (94, 30), (96, 70), (92, 104), (70, 110), (50, 104), (30, 110)]), 'shade'),
             L(outline([(8, 50), (8, 30), (22, 6), (50, -2), (78, 6), (94, 30), (94, 50), (70, 40), (50, 46), (30, 40)]), 'mid', 'b', False),
             strand([(50, 4), (50, 100)], 'deep', 'b', 1.0)],
}

# Whaly Walker: grandullón de piel morena con el pelo verde oscuro en un tupé ancho y alto, rapado a los lados con una franja
# rosa y una melena que le cae por detrás hasta los hombros; ojos blancos redondos de enfadado
CHARS['whaly-walker'] = {
    'body': 'corpulento', 'pal': pal('#2a5a48', '#f6b276', iris='#1e1414', shade='#1e4436', deep='#16322a', band='#c8706e'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 102, 'hairline': [(18, 66), (22, 56), (36, 52), (50, 58), (64, 52), (78, 56), (82, 66)]},
    'front': [L(outline([(6, 120), (2, 90), (8, 64), (16, 46), (18, 22), (30, 10), (36, 2), (50, 6), (64, 2), (72, 10), (84, 22), (86, 46), (94, 64), (98, 90), (94, 120),
                         (84, 96), (82, 64), (18, 64), (16, 96)])),
              L(outline([(58, 6), (80, 18), (86, 46), (94, 80), (90, 110), (82, 64)]), 'shade', 'b', False),
              L(outline([(18, 44), (26, 46), (24, 62), (18, 60)]), 'band', 'b', False), L(outline([(82, 44), (74, 46), (76, 62), (82, 60)]), 'band', 'b', False),
              strand([(34, 14), (40, 40)], 'deep', 'b', 1.0), strand([(66, 14), (60, 40)], 'deep', 'b', 1.0)],
    'side': [L(outline([(60, 50), (72, 40), (84, 28), (84, 10), (70, -6), (44, -10), (20, -4), (6, 14), (0, 44), (-8, 74), (-6, 104), (12, 112), (30, 108), (44, 96), (50, 78),
                        (56, 62)])),
             L(outline([(46, 26), (70, 20), (82, 26), (60, 34)]), 'band', 'b', False),
             L(outline([(0, 50), (22, 54), (34, 100), (6, 104)]), 'shade', 'b', False)],
    'back': [L(outline([(6, 120), (0, 90), (8, 50), (18, 22), (32, 8), (50, 2), (68, 8), (82, 22), (92, 50), (100, 90), (94, 120), (70, 124), (50, 118), (30, 124)])),
             L(outline([(56, 4), (82, 20), (96, 60), (98, 116), (68, 120), (70, 50)]), 'shade', 'b', False)],
}

# Sunny Fishton: pelo celeste de pinchos altísimos hacia arriba con los lados rapados en gris pardo y una coleta celeste larga
# que le cae por detrás; cejas celestes gruesas, ojos verdes y boca abierta de risa; dos marquitas bajo los ojos
CHARS['sunny-fishton'] = {
    'body': 'normal', 'pal': pal('#a8e4ec', '#f6be8a', iris='#5a9a5a', shade='#7ab0bc', deep='#5a8a96', buzz='#7a6a6c', buzz_d='#5e5052'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False, 'big_ears': 2},
    'front': [L(outline([(16, 70), (14, 44), (22, 30), (78, 30), (86, 44), (84, 70), (78, 58), (22, 58)]), 'buzz'),
              L(outline([(24, 36), (14, 14, 1), (32, 20), (34, -4, 1), (44, 12), (52, -28, 1), (58, 6), (70, -10, 1), (70, 14), (88, 10, 1), (80, 30), (64, 40), (50, 48, 1),
                         (40, 38)]), 'mid', 'f', ln=True),
              L(outline([(56, -14), (66, 6), (76, 18), (64, 34)]), 'shade', 'f', False),
              L(outline([(28, 62), (36, 58), (44, 62), (36, 66)]), 'mid', 'f', ln=True), L(outline([(72, 62), (64, 58), (56, 62), (64, 66)]), 'mid', 'f', ln=True),
              L([(30, 84), (32, 86)], OUTC, 'f', False, False, 1.2), L([(70, 84), (68, 86)], OUTC, 'f', False, False, 1.2),
              L(outline([(80, 70), (86, 90), (84, 112, 1), (78, 92)]), 'mid', 'b')],
    'side': [L(outline([(54, 58), (60, 46), (80, 44), (88, 30), (60, 26), (30, 30), (12, 40), (8, 62), (20, 78), (36, 76), (46, 68)]), 'buzz'),
             L(outline([(20, 30), (10, 40), (-6, 70), (-14, 124, 1), (2, 90), (16, 60), (28, 38)]), 'mid', 'b', ln=True),
             L(outline([(14, 36), (30, 14), (34, -6, 1), (46, 8), (60, -18, 1), (64, 4), (80, -4, 1), (78, 14), (92, 20, 1), (88, 30), (60, 34), (30, 38)]), 'mid', 'f', ln=True),
             L(ell(20, 34, 4, 4), OUTC, 'f', False)],
    'back': [L(outline([(16, 84), (12, 44), (22, 30), (78, 30), (88, 44), (84, 84), (50, 92)]), 'buzz'),
             L(outline([(56, 30), (86, 40), (86, 80), (60, 88)]), 'buzz_d', 'b', False),
             L(outline([(18, 46), (20, 24), (30, 4, 1), (40, 16), (50, -10, 1), (60, 16), (70, 4, 1), (80, 24), (82, 46), (50, 52)]), 'mid', 'f', ln=True),
             L(outline([(44, 46), (56, 46), (60, 80), (54, 124, 1), (48, 90), (42, 70)]), 'mid', 'f', ln=True),
             L(ell(50, 48, 5, 4), OUTC, 'f', False)],
}

# Clem Chowdry: casco de pelo rubio melocotón en forma de seta, ancho y redondo, con el flequillo a mechones hasta las cejas;
# ojos grandes violetas y sonrisa de oreja a oreja
CHARS['clem-chowdry'] = {
    'body': 'bajito', 'pal': pal('#f6d8a8', '#fde6c4', iris='#7a4aa8', shade='#d8a888', deep='#c08a70'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 70), (-2, 50), (2, 22), (22, 0), (50, -6), (78, 0), (98, 22), (102, 50), (90, 70), (84, 60), (16, 60)])),
              L(outline([(60, -2), (88, 10), (100, 40), (96, 60), (84, 50)]), 'shade', 'b', False),
              fringe([(4, 56), (8, 30), (28, 14), (50, 10), (72, 14), (92, 30), (96, 56), (86, 50), (80, 64, 1), (72, 48), (64, 60, 1), (58, 46), (50, 62, 1), (42, 46),
                      (36, 60, 1), (28, 48), (20, 64, 1), (14, 50)]),
              L(outline([(60, 14), (84, 24), (92, 46), (78, 40)]), 'shade', 'f', False)],
    'side': [L(outline([(56, 62), (62, 54), (84, 52), (100, 44), (98, 20), (78, 0), (48, -6), (20, 2), (2, 22), (-6, 50), (8, 60), (28, 62), (40, 72)])),
             L(outline([(-4, 46), (40, 50), (48, 66), (30, 80), (14, 76), (6, 60)]), 'shade', 'b', False),
             fringe([(70, 6), (94, 20), (100, 44), (94, 60, 1), (88, 48), (80, 40)])],
    'back': [L(outline([(10, 74), (-2, 50), (2, 22), (22, 0), (50, -6), (78, 0), (98, 22), (102, 50), (90, 74), (50, 80)])),
             L(outline([(56, -2), (88, 10), (100, 40), (94, 70), (66, 76)]), 'shade', 'b', False),
             L(outline([(14, 74), (86, 74), (80, 90), (50, 96), (20, 90)]), 'deep', 'b', False)],
}

# Oscar Squidows: pelo gris plateado corto y despeinado, de pinchos sueltos en todas direcciones (la capa de debajo gris
# violácea); ojos negros afilados y media sonrisa
CHARS['oscar-squidows'] = {
    'body': 'normal', 'pal': pal('#bcc8dc', '#fcdcbc', iris='#1e1414', shade='#8a7888', deep='#6a5a6a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 66), (0, 58, 1), (10, 50), (8, 26), (24, 8), (40, 6), (48, -14, 1), (54, 4), (66, -6, 1), (66, 8), (80, 12), (92, 30), (104, 34, 1), (92, 46),
                         (88, 66), (82, 56), (18, 56)]), 'shade'),
              fringe([(10, 58), (12, 34), (26, 14), (48, 8), (70, 12), (88, 30), (90, 58), (82, 46), (76, 60, 1), (70, 44), (60, 56, 1), (56, 40), (46, 62, 1), (40, 44),
                      (30, 58, 1), (24, 44), (16, 56, 1)]),
              L(outline([(24, 18), (44, 12), (36, 26)]), 'light', 'f', False)],
    'side': [L(outline([(54, 60), (60, 48), (80, 46), (92, 32), (90, 14), (100, 4, 1), (76, 4), (70, -14, 1), (56, 0), (36, -10, 1), (30, 6), (8, 8), (2, 30), (-12, 44, 1),
                        (4, 54), (-4, 72, 1), (14, 72), (14, 88, 1), (28, 78), (42, 72)]), 'shade'),
             L(outline([(30, 6), (56, 0), (70, -14, 1), (76, 4), (100, 4, 1), (92, 26), (70, 26), (40, 22), (20, 30)]), 'mid', 'b', False),
             fringe([(66, 4), (90, 18), (94, 40), (90, 60, 1), (84, 46), (76, 34)])],
    'back': [L(outline([(16, 82), (2, 78, 1), (10, 62), (6, 30), (22, 8), (40, 2), (50, -12, 1), (58, 4), (76, 6), (94, 24), (106, 30, 1), (94, 44), (94, 64), (100, 80, 1),
                        (84, 82), (66, 92, 1), (56, 84), (40, 94, 1), (32, 84)]), 'shade'),
             L(outline([(10, 40), (22, 8), (40, 2), (50, -12, 1), (58, 4), (76, 6), (94, 24), (90, 40), (50, 34)]), 'mid', 'b', False)],
}

# Marsha Ark: melena rubia clara lisa hasta los hombros con raya en medio y dos mechones largos que le enmarcan la cara;
# ojos verdes y sonrisa
CHARS['marsha-ark'] = {
    'body': 'chica', 'pal': pal('#f8e896', '#fde2c0', iris='#6aa83a', shade='#d8b860', deep='#b8984a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 116), (4, 70), (6, 30), (22, 6), (50, -2), (78, 6), (94, 30), (96, 70), (90, 116), (82, 100), (80, 66), (20, 66), (18, 100)])),
              L(outline([(60, 2), (86, 16), (94, 50), (92, 110), (82, 96)]), 'shade', 'b', False),
              fringe([(10, 116), (8, 60), (14, 28), (34, 10), (50, 8), (48, 24), (36, 40), (24, 62), (22, 104)]),
              fringe([(90, 116), (92, 60), (86, 28), (66, 10), (50, 8), (52, 24), (64, 40), (76, 62), (78, 104)]),
              L(outline([(66, 14), (86, 30), (90, 70), (82, 60)]), 'shade', 'f', False), strand([(50, 4), (50, 22)], 'deep', 'f', 1.0)],
    'side': [L(outline([(54, 70), (58, 56), (80, 52), (92, 38), (88, 14), (64, -2), (36, -2), (14, 12), (4, 40), (4, 80), (6, 116), (30, 116), (46, 100), (48, 84)])),
             L(outline([(6, 40), (28, 46), (34, 112), (8, 112)]), 'shade', 'b', False),
             fringe([(62, 4), (88, 18), (96, 44), (96, 90), (90, 108, 1), (84, 70), (76, 44), (64, 32)])],
    'back': [L(outline([(8, 116), (4, 70), (6, 30), (22, 6), (50, -2), (78, 6), (94, 30), (96, 70), (92, 116), (50, 120)])),
             L(outline([(56, 2), (86, 16), (96, 50), (94, 116), (66, 118), (70, 50)]), 'shade', 'b', False),
             strand([(50, 0), (50, 116)], 'deep', 'b', 1.0), strand([(26, 30), (22, 112)], 'deep', 'b', 1.0), strand([(74, 30), (78, 112)], 'deep', 'b', 1.0)],
}

# Cole: melena rubia miel ondulada hasta los hombros, con un flequillo largo que le cruza la frente de izquierda a derecha y le
# roza el ojo; ojos verdes y gesto serio
CHARS['cole'] = {
    'body': 'normal', 'pal': pal('#eac278', '#fde4c4', iris='#2a9a7a', shade='#c09050', deep='#a07438'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 112), (2, 90), (6, 60), (6, 28), (24, 4), (50, -4), (76, 4), (94, 28), (94, 60), (98, 90), (90, 112), (82, 96), (80, 66), (20, 66), (18, 96)])),
              L(outline([(60, 0), (86, 14), (94, 50), (96, 100), (84, 104), (80, 60)]), 'shade', 'b', False),
              fringe([(8, 72), (10, 36), (26, 14), (54, 8), (78, 18), (92, 40), (92, 70), (84, 56), (74, 48), (64, 60), (56, 82, 1), (52, 62), (40, 52), (28, 58), (18, 74, 1)]),
              L(outline([(30, 18), (60, 14), (80, 28), (60, 26)]), 'light', 'f', False), strand([(44, 16), (60, 40), (56, 78)], 'deep', 'f', 1.0)],
    'side': [L(outline([(54, 66), (58, 54), (80, 52), (94, 36), (90, 12), (66, -4), (36, -4), (14, 10), (2, 40), (-2, 80), (-8, 104, 1), (10, 98), (16, 114, 1), (30, 102),
                        (44, 98, 1), (46, 82)])),
             L(outline([(2, 44), (26, 48), (34, 98), (8, 100)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (98, 42), (96, 72, 1), (88, 56), (82, 68, 1), (78, 46), (66, 32)])],
    'back': [L(outline([(8, 108), (2, 70), (6, 28), (24, 4), (50, -4), (76, 4), (94, 28), (98, 70), (92, 108), (74, 116, 1), (60, 106), (46, 116, 1), (32, 106), (20, 114, 1)])),
             L(outline([(56, 0), (86, 14), (98, 50), (94, 106), (66, 110), (70, 50)]), 'shade', 'b', False),
             strand([(36, 10), (28, 60), (34, 104)], 'deep', 'b', 1.0), strand([(64, 10), (72, 60), (66, 104)], 'deep', 'b', 1.0)],
}

# Amanda Ray: melena larga verde claro con flequillo recto hasta las cejas, dos mechones largos junto a la cara que se abren
# hacia fuera por abajo y las puntas de atrás hasta la espalda; ojos rosas grandes y sonrisa
CHARS['amanda-ray'] = {
    'body': 'chica', 'pal': pal('#bcdc8c', '#fde4c8', iris='#c83a7a', shade='#8a8c50', deep='#6e7040'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 110), (0, 118, 1), (4, 80), (6, 30), (22, 6), (50, -2), (78, 6), (94, 30), (96, 80), (100, 118, 1), (90, 110), (82, 96), (80, 66), (20, 66),
                         (18, 96)])),
              L(outline([(60, 2), (86, 16), (94, 50), (96, 110), (84, 100)]), 'shade', 'b', False),
              fringe([(12, 66), (12, 34), (28, 16), (50, 10), (72, 16), (88, 34), (88, 66), (84, 60), (80, 64), (72, 60), (64, 64), (56, 60), (48, 64), (40, 60), (32, 64),
                      (24, 60), (18, 64)]),
              fringe([(12, 60), (6, 96), (-4, 116, 1), (14, 104), (22, 66)]), fringe([(88, 60), (94, 96), (104, 116, 1), (86, 104), (78, 66)])],
    'side': [L(outline([(54, 70), (58, 56), (80, 52), (92, 38), (88, 14), (64, -2), (36, -2), (14, 12), (4, 40), (-4, 80), (-16, 122, 1), (10, 110), (30, 118, 1), (40, 100),
                        (48, 84)])),
             L(outline([(2, 40), (26, 46), (34, 108), (4, 112)]), 'shade', 'b', False),
             fringe([(62, 4), (88, 18), (94, 42), (92, 60), (86, 60), (90, 98), (84, 112, 1), (78, 66), (72, 44)])],
    'back': [L(outline([(8, 112), (-6, 122, 1), (2, 70), (6, 30), (22, 6), (50, -2), (78, 6), (94, 30), (98, 70), (106, 122, 1), (92, 112), (50, 122)])),
             L(outline([(56, 2), (86, 16), (98, 50), (98, 112), (66, 118), (70, 50)]), 'shade', 'b', False),
             strand([(30, 20), (24, 110)], 'deep', 'b', 1.0), strand([(70, 20), (76, 110)], 'deep', 'b', 1.0)],
}

# Lob Stark: piel morena y pelo rojo oscuro de pinchos enormes en llamarada, hacia arriba y hacia los lados; cejas rojas
# gruesas y ojos verde azulado de enfadado
CHARS['lob-stark'] = {
    'body': 'normal', 'pal': pal('#8a1010', '#c4844e', iris='#2a9a8a', shade='#640a0a', deep='#4a0606'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 72), (-6, 80, 1), (4, 62), (-14, 48, 1), (6, 40), (-6, 20, 1), (16, 18), (12, -8, 1), (30, 6), (34, -22, 1), (46, 0), (56, -34, 1), (62, -2),
                         (76, -20, 1), (76, 6), (94, -4, 1), (90, 20), (108, 24, 1), (94, 40), (110, 52, 1), (94, 62), (104, 80, 1), (84, 72), (84, 58), (16, 58)])),
              L(outline([(60, -4), (76, -16), (78, 8), (94, 28), (92, 60), (80, 40)]), 'shade', 'b', False),
              fringe([(14, 62), (16, 40), (30, 26), (50, 22), (70, 26), (84, 40), (86, 62), (76, 50), (68, 58, 1), (62, 46), (52, 56, 1), (46, 44), (36, 56, 1), (30, 46),
                      (22, 58, 1)]),
              L(outline([(28, 64), (42, 66), (40, 70), (30, 68)]), 'mid', 'f', False), L(outline([(72, 64), (58, 66), (60, 70), (70, 68)]), 'mid', 'f', False)],
    'side': [L(outline([(56, 60), (62, 48), (80, 46), (90, 32), (104, 22, 1), (86, 14), (96, -8, 1), (72, 0), (66, -28, 1), (52, -4), (30, -22, 1), (26, 2), (2, -6, 1), (10, 18),
                        (-16, 26, 1), (4, 40), (-18, 56, 1), (2, 62), (-10, 82, 1), (12, 80), (10, 100, 1), (28, 84), (44, 74)])),
             L(outline([(2, 40), (24, 46), (26, 76), (6, 70)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 84), (-6, 90, 1), (4, 68), (-16, 52, 1), (4, 42), (-8, 20, 1), (14, 18), (10, -8, 1), (30, 6), (34, -24, 1), (48, 0), (56, -34, 1), (62, -2),
                        (76, -22, 1), (76, 6), (96, -6, 1), (90, 20), (110, 22, 1), (96, 42), (114, 54, 1), (96, 68), (106, 90, 1), (84, 84), (66, 96, 1), (50, 86),
                        (34, 96, 1)])),
             L(outline([(56, 0), (76, -16), (78, 8), (96, 30), (98, 84), (64, 90), (70, 40)]), 'shade', 'b', False)],
}

# Octa: piel morena oscura y pelo blanco rosado peinado hacia atrás, con unos picos cortos que le caen sobre la frente, dos
# mechones largos por delante de las orejas y una coleta baja atada con una pinza; ojos azules y cejas fruncidas
CHARS['octa'] = {
    'body': 'normal', 'pal': pal('#e6d0dc', '#a8724c', iris='#3a8ad0', shade='#c0a0b4', deep='#9a7a90', clip='#5a5a60'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': [(14, 64), (18, 46), (30, 46), (40, 56), (50, 48), (60, 56), (70, 46), (82, 46), (86, 64)]},
    'front': [L(outline([(16, 64), (12, 34), (24, 10), (50, 2), (76, 10), (88, 34), (84, 64), (80, 52), (20, 52)])),
              L(outline([(60, 6), (82, 16), (88, 40), (82, 60), (74, 36)]), 'shade', 'b', False),
              L(outline([(14, 56), (12, 84), (16, 104, 1), (22, 84), (22, 60)]), 'mid', 'f', ln=True),
              L(outline([(86, 56), (88, 84), (84, 104, 1), (78, 84), (78, 60)]), 'mid', 'f', ln=True),
              strand([(30, 14), (34, 40)], 'deep', 'b', 1.0), strand([(50, 8), (50, 40)], 'deep', 'b', 1.0), strand([(70, 14), (66, 40)], 'deep', 'b', 1.0)],
    'side': [L(outline([(56, 54), (62, 44), (82, 40), (90, 26), (84, 8), (62, -2), (34, 0), (14, 12), (6, 36), (8, 60), (20, 76), (36, 74), (46, 66)])),
             L(outline([(6, 36), (28, 40), (30, 70), (12, 64)]), 'shade', 'b', False),
             L(outline([(14, 64), (2, 80), (4, 100, 1), (14, 84), (24, 72)]), 'mid', 'b', ln=True), L(outline([(12, 62), (22, 60), (22, 70), (12, 72)]), 'clip', 'b', ln=True),
             L(outline([(58, 46), (60, 70), (58, 96, 1), (54, 72), (52, 50)]), 'mid', 'f', ln=True),
             strand([(84, 14), (50, 12), (20, 30)], 'deep', 'b', 1.0), strand([(86, 30), (50, 26), (14, 50)], 'deep', 'b', 1.0)],
    'back': [L(outline([(16, 80), (12, 34), (24, 10), (50, 2), (76, 10), (88, 34), (84, 80), (50, 86)])),
             L(outline([(56, 6), (82, 16), (90, 44), (84, 76), (64, 82)]), 'shade', 'b', False),
             L(outline([(44, 80), (56, 80), (60, 96), (66, 108, 1), (54, 100), (46, 108, 1), (42, 96)]), 'mid', 'f', ln=True),
             L(outline([(42, 76), (58, 76), (58, 84), (42, 84)]), 'clip', 'f', ln=True),
             strand([(36, 14), (40, 74)], 'deep', 'b', 1.0), strand([(64, 14), (60, 74)], 'deep', 'b', 1.0)],
}

# Orlando Sherman: adulto de piel tostada con el pelo rubio en un tupé alto peinado hacia atrás y a un lado, las sienes
# repeinadas y patillas; ojos verde azulado y media sonrisa
CHARS['orlando-sherman'] = {
    'body': 'delgado', 'pal': pal('#f2d48e', '#e8a868', iris='#3a9aa8', shade='#d0a860', deep='#b08848'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': [(14, 76), (16, 52), (30, 44), (50, 42), (70, 44), (84, 52), (86, 76)]},
    'front': [L(outline([(14, 80), (10, 44), (14, 20), (30, 0), (52, -10), (74, -4), (90, 14), (92, 44), (86, 80), (82, 56), (18, 56)])),
              L(outline([(60, -6), (84, 6), (92, 36), (86, 70), (78, 40)]), 'shade', 'b', False),
              L(outline([(22, 26), (34, 4), (56, -8), (78, 2), (74, 12), (54, 8), (38, 20), (30, 36)]), 'light', 'b', False),
              strand([(30, 30), (50, 10), (76, 8)], 'deep', 'b', 1.0), strand([(22, 44), (40, 26), (66, 22)], 'deep', 'b', 1.0),
              L(outline([(14, 60), (20, 60), (20, 92), (16, 94)]), 'mid', 'f'), L(outline([(86, 60), (80, 60), (80, 92), (84, 94)]), 'mid', 'f')],
    'side': [L(outline([(58, 52), (66, 42), (86, 38), (96, 22), (94, 2), (78, -12), (50, -14), (26, -6), (10, 12), (4, 40), (8, 64), (20, 80), (36, 78), (50, 66)])),
             L(outline([(4, 40), (26, 44), (30, 74), (10, 70)]), 'shade', 'b', False),
             L(outline([(56, 62), (62, 62), (62, 90), (58, 92)]), 'mid', 'f'),
             strand([(92, 6), (60, -4), (24, 10)], 'deep', 'b', 1.0), strand([(94, 24), (60, 16), (16, 34)], 'deep', 'b', 1.0)],
    'back': [L(outline([(14, 82), (10, 44), (14, 20), (30, 2), (50, -6), (70, 2), (86, 20), (90, 44), (86, 82), (50, 88)])),
             L(outline([(56, -2), (84, 14), (92, 50), (86, 80), (64, 84)]), 'shade', 'b', False),
             strand([(30, 14), (40, 50), (36, 80)], 'deep', 'b', 1.0), strand([(70, 14), (60, 50), (64, 80)], 'deep', 'b', 1.0)],
}
