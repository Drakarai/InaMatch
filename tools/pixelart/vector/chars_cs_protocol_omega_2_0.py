"""Protocolo Omega 2.0 (cs-protocol-omega-2-0): sus modelos 3D de Inazuma Eleven GO 2: Chrono Stone como referencia (busto de
frente, perfil y espalda). Los que repiten de Protocolo Omega están en chars_cs_protocol_omega.py."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from chars_cs_protocol_omega import fringe, po
from heads import quad  # noqa: F401

# Kilo (Ward): grandullón de piel morena, con un casquete de pelo granate muy oscuro que baja en pico hasta la frente y
# una enorme nube de rizos que le sale hacia arriba y a un lado; orejas grandes, ojos amarillos y labios morados
CHARS['kilo'] = po({
    'body': 'corpulento', 'pal': pal('#3a1416', '#c46c3c', iris='#d8c830', shade='#26090c'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'lips', 'mouth_w': 7, 'mouth_y': 100, 'hairline': False, 'big_ears': 5, 'ear_out': 6,
             'face_front': blob([(12, 50), (50, 40), (88, 50), (94, 80), (86, 104), (66, 112), (34, 112), (14, 104), (6, 80)])},
    'front': [L(ell(56, -8, 18, 16)), L(ell(76, -24, 16, 15)), L(ell(88, 0, 14, 13)), L(ell(66, -38, 12, 11)), L(ell(94, -22, 10, 10)),
              L(outline([(12, 66), (12, 34), (28, 14), (50, 8), (72, 14), (88, 34), (88, 66), (74, 48), (58, 44), (50, 62, 1), (42, 44), (26, 48)]), 'mid', 'f'),
              L(outline([(60, 14), (80, 24), (88, 46), (76, 44)]), 'shade', 'f', False),
              strand([(50, -16), (60, -2), (70, -14)], 'shade', 'b', 1.0), strand([(74, -36), (84, -20)], 'shade', 'b', 1.0)],
    'side': [L(ell(30, -14, 18, 16)), L(ell(10, -30, 16, 15)), L(ell(-4, -8, 14, 13)), L(ell(20, -44, 12, 11)),
             L(outline([(58, 44), (66, 30), (84, 34), (90, 24), (80, 10), (58, 2), (32, 4), (12, 20), (6, 46), (12, 70), (30, 70), (44, 56)]), 'mid', 'f'),
             L(outline([(8, 34), (24, 40), (26, 64), (12, 60)]), 'shade', 'f', False)],
    'back': [L(ell(44, -8, 18, 16)), L(ell(24, -24, 16, 15)), L(ell(12, 0, 14, 13)), L(ell(34, -38, 12, 11)), L(ell(6, -22, 10, 10)),
             L(outline([(12, 70), (10, 34), (28, 12), (50, 6), (72, 12), (90, 34), (88, 70), (70, 64), (50, 76), (30, 64)]), 'mid', 'f'),
             L(outline([(56, 10), (84, 24), (88, 64), (64, 66)]), 'shade', 'f', False)],
})

# Foxtrot (Drim): pelo rubio claro de pinchos larguísimos hacia arriba y a los lados, con mechones que caen por la frente,
# y un antifaz morado oscuro que le tapa los ojos
CHARS['foxtrot'] = po({
    'body': 'normal', 'pal': pal('#f4d890', '#fae0c0', iris='#2a1a2a', shade='#d0a860', mask='#4a2a5a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(18, 72), (-10, 66, 1), (8, 54), (-14, 42, 1), (8, 34), (2, 6, 1), (20, 14), (24, -24, 1), (36, 2), (44, -34, 1), (52, -2), (62, -32, 1),
                         (66, 0), (80, -22, 1), (80, 10), (100, 4, 1), (92, 32), (114, 42, 1), (92, 54), (110, 66, 1), (82, 72), (80, 54), (20, 54)])),
              L(outline([(58, -6), (82, 6), (94, 40), (84, 64), (74, 36)]), 'shade', 'b', False),
              fringe([(14, 62), (16, 40), (30, 26), (50, 22), (70, 26), (84, 40), (86, 62), (76, 52), (68, 66, 1), (62, 50), (54, 60, 1), (50, 46), (44, 60, 1),
                      (38, 50), (30, 66, 1), (24, 52)]),
              L(outline([(14, 70), (30, 64), (44, 70), (50, 66), (56, 70), (70, 64), (86, 70), (84, 84), (68, 86), (56, 80), (50, 82), (44, 80), (32, 86), (16, 84)]),
                'mask', 'f', ln=True),
              L(outline([(26, 74), (40, 76), (36, 80), (26, 78)]), (230, 230, 240, 255), 'f', False), L(outline([(74, 74), (60, 76), (64, 80), (74, 78)]), (230, 230, 240, 255), 'f', False)],
    'side': [L(outline([(56, 60), (66, 48), (82, 50), (90, 34), (86, 10), (96, -6, 1), (72, 0), (68, -28, 1), (54, -4), (40, -30, 1), (34, 0), (6, -14, 1), (16, 18),
                        (-12, 24, 1), (8, 38), (-10, 54, 1), (10, 56), (0, 76, 1), (22, 70), (24, 88, 1), (36, 74), (48, 68)])),
             L(outline([(8, 34), (24, 40), (24, 66), (8, 58)]), 'shade', 'b', False),
             L(outline([(70, 66), (94, 66), (96, 82), (72, 80)]), 'mask', 'f', ln=True)],
    'back': [L(outline([(18, 82), (-8, 76, 1), (8, 62), (-12, 48, 1), (8, 40), (2, 10, 1), (20, 16), (24, -22, 1), (36, 4), (46, -32, 1), (54, 2), (64, -30, 1),
                        (68, 4), (82, -20, 1), (82, 12), (100, 8, 1), (92, 36), (112, 48, 1), (92, 62), (108, 76, 1), (82, 82), (66, 94, 1), (56, 84), (44, 94, 1),
                        (34, 84)])),
             L(outline([(56, 2), (84, 14), (94, 50), (84, 80), (60, 86)]), 'shade', 'b', False)],
})

# November (Orca): chica de piel morena con el pelo rosa melocotón recogido en dos enormes lazadas redondas a los lados de
# la cabeza, con dos bultitos arriba como orejas; flequillo y mechones finos junto a la cara; ojos grises
CHARS['november'] = po({
    'body': 'chica', 'pal': pal('#f4c2b0', '#9a6a44', iris='#6a7a8a', shade='#d89a8a'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'line', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(30, 10), (6, -6), (-18, 6), (-26, 30), (-14, 52), (10, 56), (30, 40)])),
              L(outline([(70, 10), (94, -6), (118, 6), (126, 30), (114, 52), (90, 56), (70, 40)])),
              L(ell(18, -10, 8, 9)), L(ell(82, -10, 8, 9)),
              L(outline([(-20, 30), (0, 40), (24, 40)]), 'shade', 'b', False), L(outline([(120, 30), (100, 40), (76, 40)]), 'shade', 'b', False),
              L(outline([(16, 70), (10, 40), (20, 16), (50, 6), (80, 16), (90, 40), (84, 70), (78, 56), (22, 56)])),
              L(outline([(14, 60), (10, 96), (16, 108, 1), (20, 92), (22, 66)]), 'mid', 'f', ln=True),
              L(outline([(86, 60), (90, 96), (84, 108, 1), (80, 92), (78, 66)]), 'mid', 'f', ln=True),
              fringe([(12, 62), (14, 38), (28, 24), (50, 20), (72, 24), (86, 38), (88, 62), (78, 52), (70, 62, 1), (62, 48), (54, 58, 1), (50, 46), (44, 58, 1),
                      (36, 48), (28, 62, 1), (20, 52)])],
    'side': [L(outline([(70, 12), (40, -14), (6, -12), (-14, 10), (-10, 40), (14, 52), (40, 44), (60, 30)])),
             L(outline([(-8, 30), (16, 44), (40, 36), (30, 20)]), 'shade', 'b', False),
             L(outline([(54, 60), (60, 48), (82, 48), (94, 30), (84, 10), (60, 4), (34, 8), (14, 26), (8, 54), (20, 78), (40, 76)])),
             L(outline([(56, 60), (60, 92), (54, 106, 1), (50, 88), (48, 64)]), 'mid', 'f', ln=True),
             fringe([(64, 6), (88, 16), (96, 40), (90, 58, 1), (82, 44), (74, 32)])],
    'back': [L(outline([(30, 14), (6, -2), (-18, 10), (-26, 34), (-14, 56), (10, 60), (34, 50), (50, 40), (66, 50), (90, 60), (114, 56), (126, 34), (118, 10), (94, -2),
                        (70, 14), (50, 6)])),
             L(outline([(52, 10), (94, 0), (124, 30), (112, 54), (66, 48)]), 'shade', 'b', False),
             L(outline([(26, 50), (34, 80), (40, 100), (50, 104), (60, 100), (66, 80), (74, 50), (50, 44)])),
             L(outline([(26, 70), (14, 94), (22, 104, 1), (30, 86)]), 'mid', 'f', ln=True), L(outline([(74, 70), (86, 94), (78, 104, 1), (70, 86)]), 'mid', 'f', ln=True)],
})

# Delta (Minenne): pelo malva grisáceo enorme en dos lazadas que forman un corazón por encima de la cabeza y bajan por los
# lados como una capucha hasta los hombros; una cinta negra ancha en lo alto de la frente y ojos claros verdosos
CHARS['delta'] = po({
    'body': 'chica', 'pal': pal('#b8a2b8', '#fcdcc4', iris='#8ab8a8', shade='#8a7090', band='#1e1e22'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(4, 112), (-12, 70), (-12, 20), (4, -10), (26, -22), (44, -14), (50, -2), (56, -14), (74, -22), (96, -10), (112, 20), (112, 70), (96, 112),
                         (84, 106), (84, 60), (16, 60), (16, 106)])),
              L(outline([(-4, 30), (6, 0), (28, -12), (44, -4), (40, 20), (22, 40), (6, 70)]), 'light', 'b', False),
              L(outline([(56, -4), (72, -12), (94, 0), (104, 30), (94, 70), (78, 40), (60, 20)]), 'light', 'b', False),
              L(outline([(26, 50), (24, 30), (50, 24), (76, 30), (74, 50), (50, 44)]), 'band', 'f', ln=True),
              fringe([(16, 64), (18, 50), (30, 48), (40, 56), (50, 50), (60, 56), (70, 48), (82, 50), (84, 64), (74, 70, 1), (66, 60), (56, 68, 1), (50, 58),
                      (44, 68, 1), (34, 60), (26, 70, 1)])],
    'side': [L(outline([(60, 50), (76, 46), (90, 32), (86, 10), (64, -4), (30, -14), (2, -6), (-14, 20), (-18, 70), (-10, 116, 1), (10, 100), (30, 80), (50, 70)])),
             L(outline([(2, 0), (40, -8), (64, 4), (40, 30), (10, 50), (-8, 50)]), 'light', 'b', False),
             L(outline([(62, 30), (86, 22), (92, 34), (66, 42)]), 'band', 'f', ln=True),
             fringe([(64, 36), (90, 40), (94, 56), (88, 66, 1), (78, 54)])],
    'back': [L(outline([(4, 112), (-12, 70), (-12, 20), (4, -10), (26, -22), (44, -14), (50, -2), (56, -14), (74, -22), (96, -10), (112, 20), (112, 70), (96, 112),
                        (70, 116), (50, 104), (30, 116)])),
             L(outline([(56, -2), (78, -16), (102, 6), (110, 60), (96, 108), (66, 110)]), 'shade', 'b', False),
             strand([(50, 0), (50, 100)], 'deep', 'b', 1.2)],
})
