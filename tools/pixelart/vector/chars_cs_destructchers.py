"""Desesperdidos (cs-destructchers): sus modelos 3D de Inazuma Eleven GO 2: Chrono Stone como referencia (busto de frente, perfil y espalda).
Los alienígenas de Ragnarok: peinados enormes rubio pálido, piel clara y ojos ámbar."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Lotus (portero): grandullón con una capucha marrón enorme de copa plana y ancha que le tapa la cabeza, con una pieza gris
# en V sobre la nariz; ojos ámbar con ojeras negras
CHARS['lotus'] = {
    'body': 'corpulento', 'pal': pal('#b8884a', '#f8d8b8', iris='#e8a820', guard='#7a7470'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 94, 'hairline': False, 'ears': False},
    'front': [L(outline([(-12, 0), (112, 0), (100, 34), (94, 70), (94, 110), (6, 110), (6, 70), (0, 34)])),
              L(outline([(60, 2), (110, 2), (98, 34), (92, 108), (80, 104), (82, 50)]), 'shade', 'b', False),
              L(outline([(24, 6), (44, 4), (38, 14)]), 'light', 'b', False),
              L(outline([(30, 54), (50, 52), (70, 54), (58, 74), (50, 86, 1), (42, 74)]), 'guard', 'f', ln=True),
              L(ell(36, 76, 9, 6), OUTC, 'f', False, False, 2.2), L(ell(64, 76, 9, 6), OUTC, 'f', False, False, 2.2)],
    'side': [L(outline([(64, 110), (22, 112), (4, 84), (0, 36), (12, 8), (48, -4), (82, 4), (98, 28), (96, 50), (72, 50), (64, 72)])),
             L(outline([(4, 40), (30, 30), (40, 80), (24, 106), (8, 90)]), 'shade', 'b', False),
             L(outline([(80, 50), (96, 50), (92, 70), (84, 64)]), 'guard', 'f', ln=True)],
    'back': [L(outline([(-12, 0), (112, 0), (98, 40), (92, 104), (8, 104), (2, 40)])),
             L(outline([(56, 2), (110, 2), (96, 40), (90, 102), (60, 102)]), 'shade', 'b', False)],
}

# Magnol: una seta enorme de pelo beige que le tapa la frente hasta los ojos, con una raya clara en diagonal, y dos moños
# redondos a los lados de la cara; sonrisa de pillo
_cap_f = [(-12, 42), (-6, 12), (18, -8), (50, -14), (82, -8), (106, 12), (112, 42), (98, 62), (72, 70), (50, 72), (28, 70), (2, 62)]
CHARS['magnol'] = {
    'body': 'normal', 'pal': pal('#e2c49a', '#f8dcc0', iris='#e8a820', bun='#f0dcc4', bun_d='#c8a080'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False, 'ears': False},
    'front': [L(ell(10, 80, 14, 11), 'bun'), L(ell(90, 80, 14, 11), 'bun'),
              L(outline([(-2, 86), (12, 90), (22, 84), (16, 90), (4, 92)]), 'bun_d', 'b', False),
              L(outline([(102, 86), (88, 90), (78, 84), (84, 90), (96, 92)]), 'bun_d', 'b', False),
              L(outline(_cap_f), 'mid', 'f'),
              L(outline([(60, -12), (100, 6), (110, 40), (96, 60), (78, 64), (88, 30)]), 'shade', 'f', False),
              L(outline([(10, 6), (30, -6), (24, 10)]), 'light', 'f', False),
              L(quad((66, -12), (40, 30), (36, 70)), 'light', 'f', False, False, 2.6)],
    'side': [L(ell(30, 82, 17, 12), 'bun'), L(outline([(16, 86), (34, 92), (46, 86), (36, 92), (20, 92)]), 'bun_d', 'b', False),
             L(outline([(-12, 44), (-8, 12), (16, -8), (52, -14), (84, -6), (102, 16), (104, 44), (90, 58), (62, 64), (30, 62), (2, 58)]), 'mid', 'f'),
             L(outline([(-10, 40), (30, 50), (62, 54), (90, 52), (60, 62), (20, 60)]), 'shade', 'f', False)],
    'back': [L(ell(4, 80, 15, 12), 'bun'), L(ell(96, 80, 15, 12), 'bun'),
             L(outline([(-12, 46), (-6, 12), (18, -8), (50, -14), (82, -8), (106, 12), (112, 46), (96, 66), (50, 72), (4, 66)])),
             L(outline([(56, -12), (104, 8), (112, 44), (96, 64), (60, 70)]), 'shade', 'b', False),
             L(quad((66, -12), (56, 30), (60, 70)), 'light', 'b', False, False, 2.6)],
}

# Tulip: casco de pelo rubio muy pálido, con dos cuernos grandes de pelo que salen de los lados hacia arriba y dos mechones
# largos junto a la cara; ojos ámbar
_horn_l = [(18, 34), (4, 14), (-6, -14), (-4, -52, 1), (6, -22), (20, 4), (30, 26)]
_horn_r = [(100 - p[0], p[1]) + tuple(p[2:]) for p in _horn_l]
CHARS['tulip'] = {
    'body': 'normal', 'pal': pal('#f0d8a8', '#f4dcc4', iris='#e8a820', shade='#c8a070'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline(_horn_l)), L(outline(_horn_r[::-1])),
              L(outline([(-2, -34), (4, -20), (14, 6), (8, -12)]), 'shade', 'b', False),
              L(outline([(12, 70), (8, 36), (22, 10), (50, 0), (78, 10), (92, 36), (88, 70), (80, 56), (20, 56)])),
              L(outline([(14, 60), (6, 100), (12, 112, 1), (20, 96), (22, 66)]), 'mid', 'f'),
              L(outline([(86, 60), (94, 100), (88, 112, 1), (80, 96), (78, 66)]), 'mid', 'f'),
              fringe([(12, 64), (14, 36), (30, 14), (54, 8), (76, 16), (88, 36), (88, 64), (78, 52), (66, 60, 1), (60, 40), (44, 30), (32, 46), (26, 64, 1),
                      (20, 52)]),
              L(outline([(28, 16), (46, 10), (36, 24)]), 'light', 'f', False), strand([(56, 10), (40, 34), (32, 56)], 'shade', 'f', 1.0)],
    'side': [L(outline([(40, 20), (52, -4), (60, -40), (70, -56, 1), (66, -20), (58, 14), (50, 30)])),
             L(outline([(54, 62), (60, 48), (82, 46), (94, 34), (88, 12), (64, 0), (36, 2), (14, 16), (6, 40), (10, 66), (22, 80), (40, 78)])),
             L(outline([(6, 40), (28, 46), (30, 74), (12, 66)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 14), (96, 40), (92, 62, 1), (86, 46), (84, 104, 1), (76, 60), (70, 36)])],
    'back': [L(outline(_horn_l)), L(outline(_horn_r[::-1])),
             L(outline([(4, 60), (8, 30), (24, 10), (50, 4), (76, 10), (92, 30), (96, 60), (78, 80), (50, 86), (22, 80)])),
             L(outline([(56, 6), (86, 22), (96, 58), (80, 78), (60, 84)]), 'shade', 'b', False),
             strand([(10, 44), (50, 30), (90, 44)], 'deep', 'b', 1.0)],
}

# Argyr: el pelo rubio recogido hacia arriba en una torre altísima de punta, con pinchos cortos a los lados, y una coletilla
# baja atada con una bolita roja; orejas puntiagudas y piel morena clara
CHARS['argyr'] = {
    'body': 'normal', 'pal': pal('#ecc890', '#f0b888', iris='#1e1414', shade='#c09868', tie='#a82020'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': False, 'big_ears': 1, 'ear_out': 4},
    'front': [L(outline([(20, 56), (16, 30), (26, 4), (34, -28), (46, -56), (56, -74, 1), (60, -40), (70, -10), (82, 8), (86, 30), (82, 56)])),
              L(outline([(16, 40), (-4, 34, 1), (14, 24)])), L(outline([(16, 54), (0, 52, 1), (16, 44)])),
              L(outline([(84, 40), (104, 34, 1), (86, 24)])), L(outline([(84, 54), (100, 52, 1), (84, 44)])),
              L(outline([(56, -60), (66, -30), (80, 6), (84, 40), (72, 30), (62, -10)]), 'shade', 'b', False),
              L(outline([(40, -30), (48, -50), (46, -20)]), 'light', 'b', False),
              fringe([(16, 58), (20, 36), (34, 22), (50, 18), (66, 22), (80, 36), (84, 58), (74, 46), (66, 54, 1), (58, 40), (50, 50, 1), (42, 40), (34, 54, 1),
                      (26, 46)]),
              L([(14, 64), (6, 70)], 'skin', 'f', False, False, 3), L([(86, 64), (94, 70)], 'skin', 'f', False, False, 3)],
    'side': [L(outline([(56, 56), (62, 44), (82, 42), (90, 26), (76, 4), (62, -30), (46, -74, 1), (40, -36), (22, -6), (8, 20), (6, 50), (14, 70), (34, 72),
                        (46, 64)])),
             L(outline([(8, 30), (26, 36), (28, 64), (12, 60)]), 'shade', 'b', False),
             L(outline([(14, 62), (4, 74), (-12, 90), (-22, 112, 1), (-4, 98), (8, 84), (18, 70)]), 'mid', 'b'),
             L(ell(14, 66, 4, 4), 'tie', 'b', ln=True),
             L(outline([(28, 40), (4, 34, 1), (22, 30)])), fringe([(66, 6), (88, 18), (94, 42), (90, 54, 1), (82, 40), (74, 30)]),
             L(outline([(40, 66), (34, 52, 1), (46, 62)]), 'skin', 'f', ln=True)],
    'back': [L(outline([(20, 76), (16, 30), (26, 4), (34, -28), (46, -56), (56, -74, 1), (60, -40), (70, -10), (82, 8), (86, 30), (82, 76), (50, 84)])),
             L(outline([(16, 40), (-4, 34, 1), (14, 24)])), L(outline([(84, 40), (104, 34, 1), (86, 24)])),
             L(outline([(56, -60), (68, -30), (82, 8), (84, 74), (60, 80)]), 'shade', 'b', False),
             L(outline([(44, 70), (56, 70), (60, 100), (50, 118, 1), (40, 100)]), 'mid', 'f', ln=True),
             L(ell(50, 72, 4, 4), 'tie', 'f', ln=True)],
}

# Laven: melena larga lisa color ocre con raya en medio que le cae como una capucha hasta el pecho, una cinta negra fina en
# la frente; cara larga con rayas y ojos ámbar de párpados negros
CHARS['laven'] = {
    'body': 'delgado', 'pal': pal('#c89048', '#f6d8c0', iris='#e8a820', shade='#9a6a34'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 94, 'hairline': False, 'ears': False},
    'front': [L(outline([(4, 124), (-2, 70), (4, 30), (22, 6), (50, -2), (78, 6), (96, 30), (102, 70), (96, 124), (84, 112), (84, 60), (16, 60), (16, 112)])),
              L(outline([(60, 2), (90, 18), (100, 70), (94, 120), (86, 104), (84, 50)]), 'shade', 'b', False),
              fringe([(14, 70), (14, 40), (26, 22), (50, 16), (74, 22), (86, 40), (86, 70), (82, 54), (68, 34), (50, 30), (32, 34), (18, 54)]),
              L(quad((24, 32), (50, 20), (76, 32)), OUTC, 'f', False, False, 3.2),
              L([(50, 50), (50, 66)], OUTC, 'f', False, False, 1.0), L([(50, 72), (46, 86), (50, 92), (54, 86), (50, 72)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(56, 64), (60, 50), (82, 46), (94, 32), (86, 10), (62, -2), (34, 0), (12, 16), (2, 44), (0, 90), (6, 124), (36, 124), (50, 100)])),
             L(outline([(4, 50), (28, 56), (40, 116), (8, 118)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 14), (94, 38), (88, 50, 1), (80, 40), (70, 34)]),
             L(quad((60, 30), (76, 22), (90, 30)), OUTC, 'f', False, False, 3.0)],
    'back': [L(outline([(2, 124), (-2, 70), (4, 30), (22, 6), (50, -2), (78, 6), (96, 30), (102, 70), (98, 124), (50, 128)])),
             L(outline([(56, 2), (90, 18), (100, 70), (96, 122), (60, 126)]), 'shade', 'b', False),
             strand([(50, 0), (50, 100)], 'light', 'b', 1.2)],
}

# Viol: grandullón de piel morena con melena rubia de mechones gruesos echados hacia atrás y hacia fuera, con dos picos
# como cuernos arriba y una punta que baja hasta la nariz; ceño fruncido y sonrisa de dientes
CHARS['viol'] = {
    'body': 'corpulento', 'pal': pal('#e2c08a', '#a8703c', iris='#e8a820', shade='#b88c5a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(12, 98, 1), (2, 80), (-16, 72, 1), (2, 62), (-14, 50, 1), (6, 42), (4, 22), (18, 6), (26, -24, 1), (36, 4), (50, 0), (64, 4),
                         (74, -24, 1), (82, 6), (96, 22), (94, 42), (114, 50, 1), (98, 62), (116, 72, 1), (98, 80), (88, 98, 1), (84, 70), (16, 70)])),
              L(outline([(60, 6), (88, 18), (96, 44), (90, 80), (80, 50)]), 'shade', 'b', False),
              fringe([(14, 66), (16, 40), (30, 22), (50, 16), (70, 22), (84, 40), (86, 66), (76, 52), (64, 56), (56, 46), (50, 74, 1), (44, 46), (36, 56), (24, 52)]),
              strand([(40, 24), (46, 56)], 'shade', 'f', 1.0), strand([(60, 24), (54, 56)], 'shade', 'f', 1.0),
              L(outline([(30, 20), (40, 14), (36, 30)]), 'light', 'f', False), L(outline([(70, 20), (60, 14), (64, 30)]), 'light', 'f', False)],
    'side': [L(outline([(56, 60), (62, 48), (82, 46), (90, 30), (78, 10), (66, -20, 1), (56, 4), (38, 0), (14, 10), (-12, 12, 1), (4, 26), (-18, 36, 1), (2, 46),
                        (-16, 62, 1), (4, 64), (-8, 82, 1), (12, 80), (8, 98, 1), (24, 86), (40, 76)])),
             L(outline([(4, 34), (26, 42), (28, 74), (8, 66)]), 'shade', 'b', False),
             fringe([(68, 6), (90, 20), (94, 44), (88, 56, 1), (82, 42), (74, 32)])],
    'back': [L(outline([(14, 96, 1), (4, 80), (-14, 72, 1), (2, 62), (-14, 50, 1), (6, 42), (4, 22), (18, 6), (26, -24, 1), (36, 4), (50, 0), (64, 4),
                        (74, -24, 1), (82, 6), (96, 22), (94, 42), (114, 50, 1), (98, 62), (114, 72, 1), (96, 80), (86, 96, 1), (70, 90), (60, 104, 1), (50, 90),
                        (40, 104, 1), (30, 90)])),
             L(outline([(56, 6), (88, 18), (96, 46), (92, 80), (70, 92)]), 'shade', 'b', False),
             strand([(30, 30), (24, 60), (28, 86)], 'shade', 'b', 1.2), strand([(50, 20), (50, 86)], 'shade', 'b', 1.2),
             strand([(70, 30), (76, 60), (72, 86)], 'shade', 'b', 1.2)],
}

# Dandy: pelo rubio de pinchos de punta hacia arriba como llamas, con un mechón grueso que cae por la frente; ojos ámbar
# de ceño fruncido
CHARS['dandy'] = {
    'body': 'normal', 'pal': pal('#ecc890', '#fcdcc0', iris='#e8a820', shade='#c49a68'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(16, 66), (4, 50, 1), (10, 36), (-4, 18, 1), (14, 14), (12, -14, 1), (28, 2), (32, -30, 1), (44, -4), (54, -34, 1), (62, -4),
                         (76, -24, 1), (78, 4), (98, -2, 1), (90, 18), (108, 26, 1), (92, 38), (98, 54, 1), (84, 66), (82, 52), (18, 52)])),
              L(outline([(58, -10), (80, 2), (92, 34), (86, 58), (76, 36)]), 'shade', 'b', False),
              L(outline([(32, -10), (40, -24), (40, 0)]), 'light', 'b', False), L(outline([(62, -14), (70, -18), (66, 4)]), 'light', 'b', False),
              fringe([(14, 60), (16, 40), (30, 26), (50, 20), (70, 26), (84, 40), (86, 60), (76, 48), (64, 52, 1), (58, 40), (52, 66, 1), (44, 42), (36, 50, 1),
                      (26, 44), (20, 58, 1)])],
    'side': [L(outline([(54, 58), (62, 46), (82, 44), (92, 30), (86, 10), (98, -8, 1), (74, -2), (70, -26, 1), (56, -6), (40, -24, 1), (32, 0), (6, -10, 1),
                        (14, 14), (-10, 22, 1), (6, 34), (-6, 52, 1), (10, 56), (12, 74), (30, 74), (44, 66)])),
             L(outline([(4, 30), (24, 38), (26, 66), (10, 58)]), 'shade', 'b', False),
             fringe([(68, 4), (90, 18), (94, 42), (90, 56, 1), (82, 42), (74, 32)])],
    'back': [L(outline([(16, 78), (6, 64, 1), (10, 50), (-4, 30, 1), (12, 24), (10, -6, 1), (28, 6), (34, -26, 1), (46, 0), (56, -30, 1), (62, 0), (78, -20, 1),
                        (80, 8), (100, 4, 1), (90, 26), (106, 34, 1), (90, 48), (96, 66, 1), (84, 78), (66, 84), (50, 92, 1), (34, 84)])),
             L(outline([(56, -6), (82, 6), (92, 40), (86, 76), (64, 82)]), 'shade', 'b', False),
             strand([(36, 10), (44, 40), (40, 70)], 'shade', 'b', 1.0), strand([(64, 10), (56, 40), (60, 70)], 'shade', 'b', 1.0)],
}

# Chamomile: chica de melena rubia enorme y abombada con una diadema azul marino, un flequillo que le tapa un ojo y la piel
# muy pálida; sombra de ojos azul y ojos ámbar
CHARS['chamomile'] = {
    'body': 'chica', 'pal': pal('#ecc88c', '#faeadc', iris='#e8a820', shade='#c49860', band='#1e3a8a'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(2, 112), (-6, 70), (0, 24), (22, -8), (54, -18), (84, -8), (104, 22), (110, 70), (104, 112), (88, 100), (86, 62), (74, 46), (30, 46),
                         (16, 64), (14, 100)])),
              L(outline([(60, -14), (96, 6), (108, 60), (102, 108), (88, 92), (88, 50)]), 'shade', 'b', False),
              L(quad((20, -2), (50, -26), (82, -6)), 'band', 'b', False, False, 4.0),
              fringe([(14, 66), (16, 40), (30, 24), (56, 20), (74, 30), (66, 52), (56, 74), (44, 96), (30, 104), (14, 100)]),
              L(outline([(30, 30), (50, 26), (40, 40)]), 'light', 'f', False), strand([(58, 26), (46, 60), (32, 96)], 'shade', 'f', 1.0),
              L(ell(64, 70, 7, 2.4), (90, 130, 200, 255), 'f', False)],
    'side': [L(outline([(48, 104), (54, 60), (74, 52), (92, 36), (84, 4), (56, -14), (22, -10), (0, 12), (-8, 50), (-4, 90), (10, 112), (30, 116)])),
             L(outline([(-6, 40), (20, 50), (30, 100), (6, 106)]), 'shade', 'b', False),
             L(quad((40, -16), (70, -12), (86, 10)), 'band', 'f', False, False, 4.0),
             fringe([(62, -2), (86, 12), (94, 40), (90, 64, 1), (82, 46), (72, 34)])],
    'back': [L(outline([(2, 108), (-6, 70), (0, 24), (22, -8), (54, -18), (84, -8), (104, 22), (110, 70), (102, 108), (50, 118)])),
             L(outline([(56, -14), (96, 6), (108, 60), (100, 106), (60, 116)]), 'shade', 'b', False),
             L(quad((20, 0), (50, -26), (82, -4)), 'band', 'b', False, False, 4.0),
             strand([(24, 30), (18, 70), (24, 104)], 'shade', 'b', 1.2), strand([(76, 30), (82, 70), (76, 104)], 'shade', 'b', 1.2)],
}

# Orchid: melena rubia salvaje y ondulada, abierta hacia los lados en mechones largos que acaban en punta curvada; sonrisa de
# dientes y ojos ámbar de loco
CHARS['orchid'] = {
    'body': 'normal', 'pal': pal('#e6c490', '#fcdcc0', iris='#e8a820', shade='#b88c60'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(16, 76), (4, 92), (-22, 96, 1), (-2, 82), (-8, 64), (-30, 58, 1), (-6, 48), (-14, 32, 1), (4, 26), (14, 6), (40, -8), (64, -6), (86, 6),
                         (98, 24), (114, 32, 1), (106, 48), (130, 58, 1), (108, 64), (104, 82), (124, 96, 1), (98, 92), (86, 76), (82, 60), (18, 60)])),
              L(outline([(62, -4), (90, 10), (104, 46), (100, 84), (86, 66)]), 'shade', 'b', False),
              fringe([(14, 66), (14, 40), (28, 18), (50, 10), (72, 18), (86, 40), (86, 66), (78, 52), (66, 42), (58, 24), (54, 48, 1), (46, 24), (36, 40),
                      (24, 54)]),
              L(outline([(26, 22), (42, 14), (34, 28)]), 'light', 'f', False)],
    'side': [L(outline([(54, 60), (60, 48), (82, 46), (92, 30), (84, 10), (62, -4), (34, -6), (10, 8), (-14, 4, 1), (2, 24), (-26, 34, 1), (-4, 44), (-24, 62, 1),
                        (0, 62), (-10, 84, 1), (14, 78), (18, 94, 1), (30, 80), (44, 72)])),
             L(outline([(-2, 30), (24, 40), (26, 74), (2, 66)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 14), (94, 40), (88, 56, 1), (80, 42), (72, 30)])],
    'back': [L(outline([(16, 84), (2, 94), (-22, 98, 1), (-4, 80), (-10, 64), (-32, 58, 1), (-6, 46), (-16, 30, 1), (4, 24), (14, 6), (40, -8), (64, -6),
                        (86, 6), (96, 24), (116, 30, 1), (106, 46), (132, 58, 1), (110, 64), (104, 80), (122, 98, 1), (98, 94), (84, 84), (66, 96, 1), (50, 86),
                        (34, 96, 1)])),
             L(outline([(56, -6), (90, 10), (104, 48), (100, 84), (66, 92)]), 'shade', 'b', False),
             L(ell(36, 70, 6, 4), 'light', 'b', False), L(ell(64, 70, 6, 4), 'light', 'b', False)],
}

# Aster: rastas largas rubio pálido que le caen hasta los hombros, una cinta turquesa en la frente y una rasta que le baja
# entre los ojos; ceño serio
CHARS['aster'] = {
    'body': 'normal', 'pal': pal('#eedcb8', '#f6c8a0', iris='#6a3a1a', shade='#c8a888', deep='#a88868', band='#2ab8b8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(4, 114), (-8, 60), (0, 22), (22, -2), (50, -8), (78, -2), (100, 22), (108, 60), (96, 114), (86, 104), (84, 66), (16, 66), (14, 104)])),
              L(outline([(60, -4), (92, 16), (104, 60), (94, 110), (86, 96), (84, 50)]), 'shade', 'b', False),
              fringe([(14, 56), (16, 36), (30, 20), (50, 14), (70, 20), (84, 36), (86, 56), (70, 50), (50, 52), (30, 50)]),
              L(outline([(12, 52), (50, 44), (88, 52), (88, 62), (50, 56), (12, 62)]), 'band', 'f', ln=True),
              L(outline([(46, 2), (54, 2), (56, 64), (50, 80, 1), (44, 64)]), 'mid', 'f', ln=True),
              L(outline([(10, 60), (18, 60), (22, 112), (14, 116, 1)]), 'mid', 'f', ln=True), L(outline([(90, 60), (82, 60), (78, 112), (86, 116, 1)]), 'mid', 'f', ln=True),
              strand([(30, 20), (26, 46)], 'deep', 'f', 1.0), strand([(70, 20), (74, 46)], 'deep', 'f', 1.0)],
    'side': [L(outline([(56, 60), (62, 48), (82, 44), (92, 30), (82, 8), (58, -4), (30, -2), (8, 10), (-16, 16, 1), (0, 28), (-22, 40, 1), (-2, 50), (-22, 66, 1),
                        (0, 70), (-14, 92, 1), (8, 88), (4, 110, 1), (22, 96), (26, 112, 1), (34, 94), (46, 78)])),
             strand([(10, 30), (-10, 40)], 'deep', 'b', 1.0), strand([(14, 54), (-8, 64)], 'deep', 'b', 1.0), strand([(20, 76), (6, 94)], 'deep', 'b', 1.0),
             L(outline([(54, 46), (92, 44), (94, 54), (56, 58)]), 'band', 'f', ln=True),
             fringe([(64, 2), (86, 12), (92, 30), (82, 44), (74, 30)])],
    'back': [L(outline([(2, 112), (-8, 60), (0, 22), (22, -2), (50, -8), (78, -2), (100, 22), (108, 60), (98, 112), (86, 106), (76, 118, 1), (62, 106),
                        (50, 120, 1), (38, 106), (24, 118, 1), (14, 106)])),
             L(outline([(56, -4), (92, 16), (104, 60), (96, 108), (64, 110)]), 'shade', 'b', False),
             strand([(20, 20), (14, 60), (20, 104)], 'deep', 'b', 1.0), strand([(36, 6), (34, 60), (38, 108)], 'deep', 'b', 1.0),
             strand([(64, 6), (66, 60), (62, 108)], 'deep', 'b', 1.0), strand([(80, 20), (86, 60), (80, 104)], 'deep', 'b', 1.0),
             L([(4, 56), (50, 50), (96, 56)], 'band', 'b', False, False, 4.0)],
}

# Gentian: piel morena, pelo rubio de pinchos cortos echados hacia arriba y hacia atrás en un tupé; ojos ámbar y sonrisa
# torcida
CHARS['gentian'] = {
    'body': 'normal', 'pal': pal('#ecc890', '#a87040', iris='#e8a820', shade='#c49a68'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(16, 70), (6, 56, 1), (12, 44), (0, 30, 1), (14, 22), (14, 0, 1), (28, 8), (30, -18, 1), (42, 0), (50, -22, 1), (58, 0), (70, -18, 1),
                         (72, 8), (86, 0, 1), (86, 22), (100, 30, 1), (88, 44), (94, 56, 1), (84, 70), (82, 54), (18, 54)])),
              L(outline([(58, -4), (80, 6), (92, 36), (86, 60), (76, 36)]), 'shade', 'b', False),
              fringe([(14, 62), (16, 42), (28, 30), (50, 26), (72, 30), (84, 42), (86, 62), (76, 50), (66, 56, 1), (60, 44), (50, 54, 1), (40, 44), (34, 56, 1),
                      (24, 50)]),
              L(outline([(32, 6), (40, -6), (40, 16)]), 'light', 'b', False), L(outline([(58, 6), (64, -6), (64, 16)]), 'light', 'b', False)],
    'side': [L(outline([(54, 58), (62, 46), (82, 46), (92, 32), (86, 14), (96, 0, 1), (76, 2), (66, -16, 1), (50, 0), (30, -10, 1), (26, 8), (2, 6, 1), (12, 22),
                        (-12, 30, 1), (6, 40), (-6, 54, 1), (10, 58), (8, 76, 1), (24, 72), (40, 70)])),
             L(outline([(6, 34), (24, 40), (26, 66), (10, 58)]), 'shade', 'b', False),
             fringe([(68, 6), (90, 20), (94, 44), (88, 56, 1), (82, 42), (74, 32)])],
    'back': [L(outline([(16, 80), (6, 66, 1), (12, 54), (-2, 40, 1), (12, 30), (10, 8, 1), (26, 14), (30, -12, 1), (42, 6), (50, -16, 1), (58, 6), (70, -12, 1),
                        (74, 14), (90, 8, 1), (88, 30), (102, 40, 1), (88, 54), (94, 66, 1), (84, 80), (64, 88), (50, 98, 1), (36, 88)])),
             L(outline([(56, 0), (82, 12), (92, 44), (86, 78), (62, 86)]), 'shade', 'b', False),
             strand([(30, 20), (40, 50), (36, 76)], 'deep', 'b', 1.0), strand([(70, 20), (60, 50), (64, 76)], 'deep', 'b', 1.0)],
}

# Flora: chica de melena larga y lisa azul celeste con raya en medio, que le cae por delante de los hombros con las puntas
# hacia dentro; ojos azules grandes
CHARS['flora'] = {
    'body': 'chica', 'pal': pal('#94dce0', '#fce0c8', iris='#2a5aa8', shade='#70b4bc'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(2, 124), (-4, 70), (2, 26), (22, 4), (50, -2), (78, 4), (98, 26), (104, 70), (98, 124), (86, 116), (84, 64), (16, 64), (14, 116)])),
              L(outline([(60, 2), (92, 18), (102, 70), (96, 120), (86, 102), (84, 50)]), 'shade', 'b', False),
              fringe([(12, 72), (12, 42), (24, 20), (50, 10), (76, 20), (88, 42), (88, 72), (82, 56), (74, 40), (56, 26), (50, 40, 1), (44, 26), (26, 40), (18, 56)]),
              L(outline([(10, 66), (18, 66), (20, 120), (8, 128, 1)]), 'mid', 'f', ln=True), L(outline([(90, 66), (82, 66), (80, 120), (92, 128, 1)]), 'mid', 'f', ln=True),
              strand([(50, 12), (50, 30)], 'shade', 'f', 1.0)],
    'side': [L(outline([(54, 64), (58, 50), (80, 48), (92, 34), (86, 10), (62, -2), (32, 0), (10, 16), (0, 44), (-2, 90), (4, 124), (20, 120), (32, 132, 1),
                        (36, 112), (46, 92)])),
             L(outline([(2, 44), (26, 50), (34, 110), (8, 116)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 14), (94, 40), (90, 70, 1), (82, 52), (76, 112, 1), (72, 60), (68, 34)])],
    'back': [L(outline([(0, 124), (-4, 70), (2, 26), (22, 4), (50, -2), (78, 4), (98, 26), (104, 70), (100, 124), (50, 130)])),
             L(outline([(56, 2), (92, 18), (102, 70), (98, 122), (60, 128)]), 'shade', 'b', False),
             strand([(50, 0), (50, 60)], 'shade', 'b', 1.0)],
}

# Sterne: media melena lisa castaño grisáceo con raya en medio que le llega a la mandíbula, con las puntas hacia dentro;
# ojos azules y sonrisa tranquila
CHARS['sterne'] = {
    'body': 'normal', 'pal': pal('#9a8a68', '#fcdcc0', iris='#2a3a6a', shade='#7a6a4c'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(8, 100), (2, 60), (8, 22), (26, 4), (50, -2), (74, 4), (92, 22), (98, 60), (92, 100), (84, 92), (84, 60), (16, 60), (16, 92)])),
              L(outline([(60, 2), (90, 18), (98, 60), (92, 98), (84, 80), (84, 40)]), 'shade', 'b', False),
              fringe([(12, 76), (12, 42), (24, 20), (50, 10), (76, 20), (88, 42), (88, 76), (82, 60), (74, 44), (58, 30), (50, 36, 1), (42, 30), (26, 44), (18, 60)]),
              strand([(50, 12), (50, 32)], 'shade', 'f', 1.0)],
    'side': [L(outline([(54, 62), (58, 50), (80, 48), (92, 34), (86, 10), (62, -2), (32, 0), (10, 16), (2, 44), (2, 80), (12, 100), (30, 102), (44, 92), (48, 74)])),
             L(outline([(4, 44), (28, 50), (34, 96), (12, 96)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 14), (94, 40), (90, 60, 1), (82, 46), (72, 36)])],
    'back': [L(outline([(6, 100), (2, 60), (8, 22), (26, 4), (50, -2), (74, 4), (92, 22), (98, 60), (94, 100), (50, 106)])),
             L(outline([(56, 2), (90, 18), (98, 60), (94, 98), (60, 104)]), 'shade', 'b', False),
             strand([(50, 0), (50, 50)], 'shade', 'b', 1.0)],
}
