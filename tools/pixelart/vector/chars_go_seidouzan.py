"""Colegio Monte Olimpo (go-seidouzan): sus modelos 3D de Inazuma Eleven GO como referencia (busto de frente, perfil y espalda)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from chars_alius import LONG_FACE
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Theo Divine (portero): melena negra lisa con raya al medio que le cae a los lados hasta los hombros y una banda blanca
# que le tapa la frente; ojos turquesa y sonrisa de dientes
CHARS['theo-divine'] = {
    'body': 'normal', 'pal': pal('#2a2a36', '#fcd8b4', iris='#2a9aa8', band='#f4f4f4'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 112), (4, 70), (6, 30), (20, 6), (50, -2), (80, 6), (94, 30), (96, 70), (90, 112), (80, 108), (80, 60), (20, 60), (20, 108)])),
              L(outline([(60, 2), (86, 14), (94, 50), (90, 108), (82, 100), (80, 50)]), 'shade', 'b', False),
              fringe([(8, 100), (12, 50), (20, 20), (44, 6), (50, 14), (56, 6), (80, 20), (88, 50), (92, 100), (82, 104), (82, 60), (76, 44), (24, 44), (18, 60),
                      (18, 104)]),
              L(outline([(24, 64), (22, 46), (34, 38), (50, 40), (66, 38), (78, 46), (76, 64), (62, 58), (50, 62), (38, 58)]), 'band', 'f', ln=True)],
    'side': [L(outline([(54, 58), (60, 46), (80, 40), (90, 26), (84, 8), (60, -2), (34, 0), (12, 14), (2, 40), (-2, 80), (-8, 112, 1), (8, 104), (14, 120, 1),
                        (20, 98), (36, 92), (48, 74)])),
             L(outline([(2, 40), (24, 44), (32, 92), (6, 104)]), 'shade', 'b', False),
             L(outline([(82, 44), (88, 30), (94, 46), (92, 62), (84, 60)]), 'band', 'f', ln=True)],
    'back': [L(outline([(8, 110), (4, 70), (6, 30), (20, 6), (50, -2), (80, 6), (94, 30), (96, 70), (92, 110), (50, 116)])),
             L(outline([(56, 2), (86, 14), (96, 50), (92, 110), (60, 114)]), 'shade', 'b', False),
             strand([(50, 4), (50, 110)], 'deep', 'b', 1.0)],
}

# Mnemo Pool: melena larga amarillo verdoso peinada hacia atrás desde la frente, con dos mechones largos que le enmarcan
# la cara; dos marcas amarillas en la frente, ojos turquesa
CHARS['mnemo-pool'] = {
    'body': 'normal', 'pal': pal('#c8c040', '#f6c8a0', iris='#2a9a9a', mark='#d8c838', shade='#9a8a30'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': (56, 38)},
    'front': [L(outline([(6, 116), (2, 70), (6, 30), (20, 8), (50, 0), (80, 8), (94, 30), (98, 70), (94, 116), (84, 110), (82, 60), (18, 60), (16, 110)])),
              L(outline([(60, 4), (86, 16), (96, 50), (94, 110), (84, 100), (80, 50)]), 'shade', 'b', False),
              L(outline([(10, 70), (14, 42), (22, 40), (20, 80), (18, 112), (10, 112)]), 'mid', 'f'),
              L(outline([(90, 70), (86, 42), (78, 40), (80, 80), (82, 112), (90, 112)]), 'mid', 'f'),
              strand([(30, 10), (24, 30), (20, 50)], 'shade', 'b', 1.0), strand([(70, 10), (76, 30), (80, 50)], 'shade', 'b', 1.0),
              strand([(46, 4), (38, 20), (34, 38)], 'shade', 'b', 1.0), strand([(54, 4), (62, 20), (66, 38)], 'shade', 'b', 1.0),
              L(outline([(40, 54), (44, 46), (42, 58)]), 'mark', 'f', ln=True), L(outline([(60, 54), (56, 46), (58, 58)]), 'mark', 'f', ln=True)],
    'side': [L(outline([(60, 48), (76, 40), (88, 30), (82, 8), (60, -2), (30, 0), (10, 16), (0, 50), (-6, 100), (-10, 120, 1), (10, 112), (30, 104), (44, 90),
                        (50, 66)])),
             L(outline([(2, 46), (28, 50), (36, 100), (6, 112)]), 'shade', 'b', False),
             fringe([(70, 30), (80, 40), (84, 70), (80, 110, 1), (72, 80), (66, 50)])],
    'back': [L(outline([(6, 116), (2, 70), (6, 30), (20, 8), (50, 0), (80, 8), (94, 30), (98, 70), (94, 116), (50, 122)])),
             L(outline([(4, 40), (50, 30), (96, 40), (98, 116), (4, 116)]), 'shade', 'b', False),
             L(outline([(28, 70), (32, 56), (70, 56), (74, 70), (60, 76), (40, 76)]), 'deep', 'b', False)],
}

# Perses Destroyer: calvo, con una franja de pelo gris aplastada encima de la cabeza; una gran cicatriz en X que le cruza
# la cara, ojillos blancos, nariz grande y orejas de soplillo
CHARS['perses-destroyer'] = {
    'body': 'corpulento', 'pal': pal('#9a9aa8', '#fcd0a0', skin_d='#e0aa78', nose='#f0bc8c', scar='#f8e8d8'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': False, 'big_ears': 3, 'ear_out': 4},
    'front': [L(outline([(16, 64), (12, 30), (26, 8), (50, 2), (74, 8), (88, 30), (84, 64)]), 'skin'),
              L(outline([(24, 24), (30, 8), (50, 2), (70, 8), (76, 24), (60, 18), (40, 18)]), 'mid', 'f', ln=True),
              strand([(36, 8), (38, 20)], 'deep', 'f', 1.0), strand([(50, 4), (50, 18)], 'deep', 'f', 1.0), strand([(64, 8), (62, 20)], 'deep', 'f', 1.0),
              L(outline([(30, 40), (33, 38), (70, 90), (67, 92)]), 'scar', 'f', ln=True),
              L(outline([(70, 40), (67, 38), (30, 90), (33, 92)]), 'scar', 'f', ln=True),
              L(outline([(24, 76), (30, 72), (38, 76), (30, 80)]), WHITE, 'f', ln=True), L(outline([(76, 76), (70, 72), (62, 76), (70, 80)]), WHITE, 'f', ln=True),
              L(ell(30, 76, 1.6, 1.6), OUTC, 'f', False), L(ell(70, 76, 1.6, 1.6), OUTC, 'f', False),
              L(outline([(44, 74), (56, 74), (62, 92), (50, 96), (38, 92)]), 'nose', 'f', ln=True)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (14, 30), (32, 10), (58, 4), (80, 14), (88, 36), (76, 44), (60, 48), (52, 62), (50, 80)]), 'skin'),
             L(outline([(14, 34), (30, 10), (58, 4), (80, 12), (78, 20), (56, 14), (30, 22), (18, 44), (8, 60, 1)]), 'mid', 'f', ln=True),
             L(outline([(70, 50), (73, 48), (84, 84), (81, 86)]), 'scar', 'f', ln=True),
             L(outline([(80, 70), (90, 68), (88, 76)]), WHITE, 'f', ln=True),
             L(outline([(90, 74), (104, 92), (90, 96)]), 'nose', 'f', ln=True)],
    'back': [L(outline([(16, 76), (12, 30), (26, 8), (50, 2), (74, 8), (88, 30), (84, 76), (66, 94), (34, 94)]), 'skin'),
             L(outline([(26, 70), (24, 10), (50, 2), (76, 10), (74, 70), (50, 76)]), 'mid', 'f', ln=True),
             L(outline([(56, 6), (76, 12), (74, 68), (56, 74)]), 'shade', 'f', False)],
}

# Rae Godmother: melena rubia muy clara y esponjosa, con un flequillo que le tapa los ojos (cerrados) y los lados abiertos
# hacia fuera como orejas de perro
CHARS['rae-godmother'] = {
    'body': 'chica', 'pal': pal('#f0e6a8', '#fcdcc0', shade='#b8a070'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 84), (-6, 96, 1), (2, 70), (2, 30), (18, 4), (50, -6), (82, 4), (98, 30), (98, 70), (106, 96, 1), (90, 84), (82, 66), (18, 66)])),
              L(outline([(60, -2), (88, 12), (98, 50), (100, 86), (88, 70)]), 'shade', 'b', False),
              fringe([(8, 76), (8, 40), (24, 14), (50, 4), (76, 14), (92, 40), (92, 76), (84, 64), (76, 78, 1), (66, 64), (58, 76, 1), (50, 62), (42, 76, 1),
                      (34, 64), (24, 78, 1), (16, 64)]),
              strand([(30, 14), (34, 40)], 'shade', 'f', 1.0), strand([(70, 14), (66, 40)], 'shade', 'f', 1.0)],
    'side': [L(outline([(56, 64), (64, 56), (84, 54), (96, 36), (90, 12), (66, -4), (36, -4), (12, 12), (2, 40), (-4, 70), (-12, 90, 1), (8, 84), (24, 90), (40, 84),
                        (48, 74)])),
             L(outline([(4, 40), (28, 44), (36, 84), (8, 84)]), 'shade', 'b', False),
             fringe([(64, 0), (88, 14), (98, 40), (96, 78, 1), (86, 60), (78, 70, 1), (72, 50)])],
    'back': [L(outline([(10, 90), (-8, 98, 1), (0, 70), (2, 30), (18, 4), (50, -6), (82, 4), (98, 30), (100, 70), (108, 98, 1), (90, 90), (50, 96)])),
             L(outline([(4, 40), (50, 28), (96, 40), (100, 90), (50, 96), (2, 90)]), 'shade', 'b', False)],
}

# Hyperion Wise: pelo rosa palo liso, con raya al medio y un pico de flequillo hasta la nariz, mechones largos a los lados
# de la cara y dos cuernos de pelo en lo alto; ojos verdes
CHARS['hyperion-wise'] = {
    'body': 'normal', 'pal': pal('#dcc4cc', '#fce0c4', iris='#2a8a6a', shade='#b89aa4'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 100), (8, 60), (8, 24), (6, -14, 1), (24, 6), (50, 0), (76, 6), (94, -14, 1), (92, 24), (92, 60), (88, 100), (80, 96), (80, 60),
                         (20, 60), (20, 96)])),
              L(outline([(12, 0), (20, 14), (14, 18)]), 'shade', 'b', False), L(outline([(88, 0), (80, 14), (86, 18)]), 'shade', 'b', False),
              fringe([(10, 96), (12, 50), (22, 20), (50, 10), (78, 20), (88, 50), (90, 96), (82, 96), (80, 56), (70, 40), (50, 80, 1), (30, 40), (20, 56),
                      (18, 96)]),
              strand([(36, 18), (42, 50)], 'shade', 'f', 1.0), strand([(64, 18), (58, 50)], 'shade', 'f', 1.0)],
    'side': [L(outline([(56, 62), (62, 52), (80, 46), (90, 30), (84, 10), (90, -16, 1), (66, 0), (40, -2), (16, 10), (4, 34), (2, 70), (10, 92), (28, 94), (44, 84)])),
             L(outline([(4, 36), (26, 40), (32, 88), (10, 88)]), 'shade', 'b', False),
             fringe([(68, 6), (90, 22), (94, 46), (88, 92, 1), (80, 60), (72, 40)])],
    'back': [L(outline([(12, 96), (8, 60), (8, 24), (6, -14, 1), (24, 6), (50, 0), (76, 6), (94, -14, 1), (92, 24), (92, 60), (88, 96), (50, 102)])),
             L(outline([(56, 4), (86, 18), (92, 60), (88, 96), (60, 100)]), 'shade', 'b', False),
             strand([(30, 30), (26, 96)], 'shade', 'b', 1.0), strand([(70, 30), (74, 96)], 'shade', 'b', 1.0)],
}

# Cronus Fourseasons: melena castaña con raya al medio hasta los hombros, las puntas vueltas hacia fuera, y una cinta blanca
# en la frente; ojos rojos rasgados y sonrisa de dientes
CHARS['cronus-fourseasons'] = {
    'body': 'normal', 'pal': pal('#7a4e26', '#fce0bc', iris='#c01e1e', band='#f4ecec'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98, 'hairline': (46, 34)},
    'front': [L(outline([(10, 108), (-4, 116, 1), (4, 96), (2, 60), (6, 24), (22, 4), (50, -4), (78, 4), (94, 24), (98, 60), (96, 96), (104, 116, 1), (90, 108),
                         (82, 64), (18, 64)])),
              L(outline([(60, 0), (88, 14), (98, 60), (96, 100), (84, 70)]), 'shade', 'b', False),
              L(outline([(14, 66), (10, 96), (16, 108), (22, 74)]), 'mid', 'f'), L(outline([(86, 66), (90, 96), (84, 108), (78, 74)]), 'mid', 'f'),
              L(quad((12, 42), (50, 34), (88, 42)) + quad((88, 50), (50, 42), (12, 50)), 'band', 'f', ln=True),
              strand([(50, 0), (46, 12), (50, 36)], 'shade', 'b', 1.0)],
    'side': [L(outline([(56, 60), (62, 50), (80, 44), (90, 28), (84, 8), (60, -4), (32, -2), (10, 14), (2, 50), (0, 90), (-6, 112, 1), (12, 104), (24, 112, 1),
                        (30, 96), (44, 84)])),
             L(outline([(2, 46), (26, 50), (32, 94), (6, 104)]), 'shade', 'b', False),
             L(quad((14, 30), (50, 22), (90, 32)) + quad((90, 40), (50, 30), (12, 38)), 'band', 'f', ln=True)],
    'back': [L(outline([(10, 108), (-4, 116, 1), (4, 96), (2, 60), (6, 24), (22, 4), (50, -4), (78, 4), (94, 24), (98, 60), (96, 96), (104, 116, 1), (90, 108),
                        (50, 112)])),
             L(outline([(56, 2), (88, 14), (98, 60), (96, 104), (60, 110)]), 'shade', 'b', False),
             L(quad((4, 32), (50, 26), (96, 32)) + quad((96, 40), (50, 34), (4, 40)), 'band', 'f', ln=True)],
}

# Coeus Heavens: una mata enorme de pelo esponjoso verde grisáceo claro con las capas de detrás pardas, que le tapa el ojo
# derecho; ojo azul y media sonrisa
CHARS['coeus-heavens'] = {
    'body': 'normal', 'pal': pal('#c4c898', '#fcdcc0', iris='#3a5ab0', shade='#8a7052', deep='#6a5440'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(8, 106), (-8, 90), (-6, 60), (-12, 34), (0, 10), (20, -10), (50, -14), (80, -10), (100, 8), (108, 34), (104, 64), (110, 90), (94, 106),
                         (86, 80), (14, 80)]), 'shade'),
              fringe([(-4, 70), (-6, 40), (4, 14), (24, -6), (50, -10), (76, -6), (96, 12), (102, 40), (100, 64), (90, 72), (84, 50), (74, 64), (70, 44),
                      (60, 60), (58, 100), (40, 106), (22, 96), (8, 100), (0, 86)]),
              strand([(30, -2), (40, 30), (36, 70)], 'shade', 'f', 1.2), strand([(66, 0), (70, 30), (64, 50)], 'shade', 'f', 1.2),
              strand([(10, 20), (20, 50), (14, 80)], 'shade', 'f', 1.2), strand([(90, 16), (92, 40)], 'shade', 'f', 1.2)],
    'side': [L(outline([(60, 50), (78, 46), (94, 30), (90, 6), (66, -10), (36, -12), (10, 2), (-8, 26), (-12, 60), (-2, 88), (16, 100), (34, 100), (44, 86),
                        (52, 66)]), 'shade'),
             fringe([(56, -8), (80, -4), (96, 16), (102, 42), (100, 70, 1), (88, 60), (84, 80, 1), (76, 54), (66, 40), (62, 10)]),
             strand([(10, 20), (6, 60), (16, 90)], 'deep', 'b', 1.2), strand([(34, 0), (30, 50), (36, 90)], 'deep', 'b', 1.2)],
    'back': [L(outline([(8, 100), (-8, 86), (-6, 60), (-12, 34), (0, 10), (20, -10), (50, -14), (80, -10), (100, 8), (108, 34), (104, 64), (110, 86), (92, 100),
                        (74, 110, 1), (50, 104), (26, 110, 1)]), 'shade'),
             L(outline([(6, 10), (26, -8), (50, -12), (60, 0), (40, 4), (20, 12)]), 'mid', 'b', False),
             L(outline([(40, 40), (60, 36), (70, 50), (50, 56)]), 'deep', 'b', False), L(outline([(4, 60), (20, 56), (24, 70), (8, 72)]), 'deep', 'b', False)],
}

# Tet Aqua: melena carmesí lisa hasta la mandíbula, con raya a un lado y un mechón que le cae entre los ojos; ojos dorados
CHARS['tet-aqua'] = {
    'body': 'normal', 'pal': pal('#c42446', '#fcdcc0', iris='#b08a2a'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 108), (6, 60), (8, 26), (22, 6), (50, -2), (78, 6), (94, 26), (96, 60), (92, 108), (82, 104), (80, 60), (20, 60), (20, 104)])),
              L(outline([(60, 2), (86, 14), (96, 50), (92, 104), (82, 96), (80, 50)]), 'shade', 'b', False),
              fringe([(8, 98), (10, 50), (22, 20), (46, 8), (76, 16), (90, 40), (92, 98), (82, 100), (80, 60), (70, 36), (56, 50), (50, 86, 1), (46, 52), (30, 48),
                      (20, 60), (18, 100)]),
              L(outline([(56, 14), (76, 24), (84, 50), (70, 38)]), 'shade', 'f', False), L(outline([(26, 22), (42, 16), (34, 30)]), 'light', 'f', False)],
    'side': [L(outline([(56, 60), (62, 50), (82, 46), (92, 30), (86, 10), (62, -2), (34, 0), (12, 16), (2, 50), (2, 100), (20, 104), (36, 100), (46, 90)])),
             L(outline([(4, 40), (26, 44), (32, 98), (6, 98)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 18), (94, 44), (90, 92, 1), (82, 60), (72, 40)])],
    'back': [L(outline([(10, 104), (6, 60), (8, 26), (22, 6), (50, -2), (78, 6), (94, 26), (96, 60), (92, 104), (50, 110)])),
             L(outline([(4, 40), (50, 30), (96, 40), (94, 104), (6, 104)]), 'shade', 'b', False)],
}

# Atlas Carrier: pelo rubio pálido de pinchos hacia arriba, cara alargada de barbilla en punta y una coleta fina que sale de la
# nuca y cae hacia un lado; ojos azul oscuro afilados
CHARS['atlas-carrier'] = {
    'body': 'normal', 'pal': pal('#ece4a8', '#fcd8b4', iris='#2a2a6a', shade='#c8bc80'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 100, 'hairline': False, 'face_front': LONG_FACE},
    'front': [L(outline([(14, 70), (-4, 54, 1), (10, 46), (0, 22, 1), (16, 20), (14, -10, 1), (30, 8), (40, -18, 1), (50, 4), (64, -18, 1), (68, 6), (90, -14, 1),
                         (86, 20), (104, 26, 1), (90, 44), (102, 60, 1), (86, 70), (84, 52), (16, 52)])),
              L(outline([(62, 0), (84, 10), (92, 40), (86, 64), (78, 44)]), 'shade', 'b', False),
              fringe([(16, 64), (18, 40), (30, 24), (50, 22), (70, 24), (82, 40), (84, 64), (74, 50), (62, 56, 1), (56, 38), (48, 60, 1), (42, 38), (32, 56, 1),
                      (24, 46)]),
              L(outline([(84, 104), (110, 110), (122, 102), (112, 116), (86, 112)]), 'mid', 'b')],
    'side': [L(outline([(56, 56), (64, 46), (82, 44), (94, 30), (88, 12), (92, -4, 1), (72, 0), (68, -18, 1), (54, -2), (38, -18, 1), (32, 2), (8, 0, 1), (16, 18),
                        (-6, 30, 1), (10, 40), (-2, 58, 1), (14, 62), (8, 82, 1), (24, 74), (36, 78), (46, 66)])),
             L(outline([(28, 80), (16, 96), (-10, 110), (-30, 114, 1), (-8, 102), (12, 90), (22, 78)]), 'mid', 'b'),
             L(outline([(4, 34), (24, 40), (26, 66), (10, 60)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 80), (0, 76, 1), (10, 62), (-6, 46, 1), (8, 40), (0, 16, 1), (16, 16), (14, -10, 1), (30, 6), (40, -18, 1), (50, 4), (64, -18, 1),
                        (68, 6), (90, -14, 1), (86, 16), (104, 20, 1), (90, 40), (106, 50, 1), (92, 62), (100, 76, 1), (84, 80), (66, 88), (50, 96, 1), (34, 88)])),
             L(outline([(56, 4), (84, 12), (92, 50), (84, 78), (62, 86)]), 'shade', 'b', False),
             L(outline([(56, 90), (30, 104), (-6, 112), (-16, 110, 1), (8, 100), (36, 92), (52, 86)]), 'mid', 'f')],
}

# Phoebus Moonlight: pelo castaño en forma de seta, con la nuca rapada más oscura; cara larguísima de nariz en punta, ojos
# apretados y una mueca de dientes
CHARS['phoebus-moonlight'] = {
    'body': 'delgado', 'pal': pal('#8a5a2e', '#fcd0a0', shade='#6a4020', buzz='#5a3420'),
    'face': {'eyes': 'closed', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 108, 'hairline': False, 'face_front': LONG_FACE},
    'front': [L(outline([(10, 52), (6, 28), (16, 6), (50, -2), (84, 6), (94, 28), (90, 52), (70, 46), (50, 58, 1), (30, 46)])),
              L(outline([(60, 2), (84, 12), (92, 40), (80, 46), (72, 20)]), 'shade', 'b', False),
              strand([(36, 4), (34, 46)], 'deep', 'b', 1.0), strand([(64, 4), (66, 46)], 'deep', 'b', 1.0),
              L(outline([(46, 70), (54, 70), (56, 96), (48, 100)]), 'skin_d', 'f', ln=True)],
    'side': [L(outline([(28, 90), (14, 80), (10, 50), (24, 40), (40, 46), (50, 60), (44, 80)]), 'buzz'),
             L(outline([(4, 46), (2, 24), (20, 4), (52, -4), (80, 6), (94, 24), (98, 42), (76, 36), (50, 34), (24, 40)]))],
    'back': [L(outline([(16, 46), (84, 46), (82, 70), (64, 92), (36, 92), (18, 70)]), 'buzz'),
             L(outline([(6, 52), (4, 28), (16, 6), (50, -2), (84, 6), (96, 28), (94, 52), (50, 44)])),
             L(outline([(56, 2), (86, 12), (94, 48), (60, 44)]), 'shade', 'b', False)],
}

# Pallas Brandish: melena malva lisa en media melena, con flequillo recto que le llega a los ojos (somnolientos, violeta)
# y un moño alto del que salen mechones como plumas
CHARS['pallas-brandish'] = {
    'body': 'chica', 'pal': pal('#a07a7c', '#fcd8b4', iris='#6a5ab0', shade='#7a5a5c'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(40, 0), (34, -20), (16, -24, 1), (32, -30), (40, -44), (52, -50, 1), (54, -34), (68, -40, 1), (62, -24), (66, -14), (58, 0)])),
              L(outline([(10, 104), (6, 60), (8, 26), (24, 6), (50, 0), (76, 6), (92, 26), (94, 60), (90, 104), (80, 100), (80, 60), (20, 60), (20, 100)])),
              L(outline([(60, 4), (86, 16), (94, 50), (90, 100), (80, 90), (80, 50)]), 'shade', 'b', False),
              fringe([(10, 80), (12, 40), (24, 18), (50, 10), (76, 18), (88, 40), (90, 80), (82, 70), (82, 66), (18, 66), (18, 70)]),
              strand([(30, 20), (30, 64)], 'shade', 'f', 1.0), strand([(50, 12), (50, 64)], 'shade', 'f', 1.0), strand([(70, 20), (70, 64)], 'shade', 'f', 1.0),
              L(ell(48, 2, 6, 2.4), (250, 240, 236, 255), 'f', ln=True)],
    'side': [L(outline([(34, 0), (30, -20), (12, -22, 1), (28, -30), (36, -44), (48, -52, 1), (50, -34), (64, -40, 1), (58, -24), (58, -10), (50, 2)])),
             L(outline([(56, 66), (60, 56), (82, 50), (92, 34), (86, 12), (62, 0), (34, 0), (12, 14), (2, 46), (4, 100), (24, 104), (38, 100), (48, 86)])),
             L(outline([(4, 40), (28, 44), (34, 100), (6, 100)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 16), (94, 42), (92, 70), (82, 64), (80, 48), (72, 36)])],
    'back': [L(outline([(40, 2), (34, -20), (16, -24, 1), (32, -30), (40, -44), (52, -50, 1), (54, -34), (68, -40, 1), (62, -24), (66, -14), (58, 2)])),
             L(outline([(10, 100), (6, 60), (8, 26), (24, 6), (50, 0), (76, 6), (92, 26), (94, 60), (90, 100), (50, 106)])),
             L(outline([(4, 40), (50, 28), (96, 40), (92, 100), (6, 100)]), 'shade', 'b', False)],
}

# Iapetus Pierce (sin modelo 3D: su retrato): pelo plateado en casco con raya al medio y un pico de flequillo que le baja hasta
# la nariz; cara alargada, cejas fruncidas
CHARS['iapetus-pierce'] = {
    'body': 'normal', 'pal': pal('#c4ccd2', '#f6c8a0', iris='#2a1e1a', shade='#9aa4ac', low='#6e5a58'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'hairline': False, 'face_front': LONG_FACE},
    'front': [L(outline([(14, 80), (10, 40), (16, 14), (34, 0), (50, -2), (66, 0), (84, 14), (90, 40), (86, 80), (80, 64), (20, 64)])),
              L(outline([(60, 2), (82, 12), (90, 40), (86, 72), (78, 44)]), 'shade', 'b', False),
              fringe([(12, 70), (14, 40), (26, 16), (50, 8), (74, 16), (86, 40), (88, 70), (80, 60), (74, 44), (60, 40), (50, 76, 1), (40, 40), (26, 44), (20, 60)]),
              strand([(42, 12), (46, 40)], 'shade', 'f', 1.0), strand([(58, 12), (54, 40)], 'shade', 'f', 1.0)],
    'side': [L(outline([(56, 62), (62, 50), (80, 46), (90, 30), (84, 10), (62, -2), (34, 0), (14, 14), (6, 40), (8, 72), (20, 86), (36, 84), (46, 74)])),
             L(outline([(46, 74), (36, 84), (20, 86), (8, 72), (6, 40), (18, 30), (30, 40), (40, 30), (52, 42)]), 'low', 'b', False),
             fringe([(66, 2), (88, 16), (92, 40), (88, 66, 1), (80, 48), (72, 36)])],
    'back': [L(outline([(14, 82), (10, 40), (16, 14), (34, 0), (50, -2), (66, 0), (84, 14), (90, 40), (86, 82), (50, 90)])),
             L(outline([(14, 82), (10, 44), (24, 34), (36, 46), (50, 30), (64, 46), (76, 34), (90, 44), (86, 82), (50, 90)]), 'low', 'b', False),
             L(outline([(56, 2), (82, 12), (90, 36), (76, 32), (64, 44), (60, 20)]), 'shade', 'b', False)],
}

# Oceanus Worldstream: pelo granate con forma de sombrero de ala ancha, con dos alas que salen en punta a los lados y caen
# junto a la cara; marcas de cicatriz bajo los ojos rojos y ceño fruncido
CHARS['oceanus-worldstream'] = {
    'body': 'bajito', 'pal': pal('#8a3434', '#fcd8b4', iris='#c0301e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 100), (12, 70), (-14, 52, 1), (8, 40), (14, 14), (40, -6), (66, -4), (84, 12), (90, 38), (116, 50, 1), (92, 64), (88, 100), (80, 96),
                         (80, 60), (20, 60), (24, 96)])),
              L(outline([(60, -2), (84, 12), (92, 46), (110, 52, 1), (88, 58), (80, 40)]), 'shade', 'b', False),
              fringe([(12, 66), (16, 40), (30, 20), (50, 14), (70, 20), (84, 40), (86, 60), (78, 58), (70, 50), (62, 56), (56, 48), (44, 52), (36, 46), (24, 58),
                      (20, 80)]),
              L(quad((34, 82), (30, 88), (32, 94)), OUTC, 'f', False, False, 1.0), L(quad((66, 82), (70, 88), (68, 94)), OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(56, 62), (62, 52), (82, 48), (92, 32), (86, 8), (60, -6), (30, -4), (10, 12), (2, 36), (-20, 40, 1), (4, 50), (6, 80), (24, 96), (40, 90),
                        (48, 76)])),
             L(outline([(4, 36), (26, 42), (30, 86), (10, 80)]), 'shade', 'b', False),
             fringe([(66, 0), (88, 14), (96, 40), (90, 70, 1), (82, 52), (72, 38)])],
    'back': [L(outline([(16, 96), (12, 70), (-14, 52, 1), (8, 40), (14, 14), (40, -6), (66, -4), (84, 12), (90, 38), (116, 52, 1), (92, 66), (86, 96), (50, 100)])),
             L(outline([(40, 0), (84, 12), (92, 46), (112, 54, 1), (86, 66), (86, 94), (52, 96), (56, 40)]), 'shade', 'b', False)],
}

# Eos Dawn (portero suplente): pelo azul grisáceo en casco redondo con flequillo de mechones; pecas y ojos verdes
CHARS['eos-dawn'] = {
    'body': 'normal', 'pal': pal('#4a6276', '#f6c8a0', iris='#6a8a1e', shade='#34485a'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 78), (2, 50), (6, 20), (24, 2), (50, -4), (76, 2), (94, 20), (98, 50), (90, 78), (82, 60), (18, 60)])),
              L(outline([(60, 0), (86, 14), (96, 46), (88, 72), (80, 44)]), 'shade', 'b', False),
              fringe([(8, 66), (10, 38), (24, 16), (50, 8), (76, 16), (90, 38), (92, 66), (84, 56), (78, 66, 1), (70, 50), (62, 62, 1), (56, 46), (48, 66, 1),
                      (42, 46), (34, 60, 1), (28, 48), (18, 64, 1)]),
              L([(30, 86), (31, 87)], OUTC, 'f', False, False, 1.0), L([(70, 86), (71, 87)], OUTC, 'f', False, False, 1.0),
              L([(34, 88), (35, 89)], OUTC, 'f', False, False, 1.0), L([(66, 88), (67, 89)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(54, 60), (60, 50), (82, 48), (94, 32), (88, 10), (62, -4), (32, -4), (10, 12), (0, 40), (4, 74), (20, 90), (36, 88), (46, 76)])),
             L(outline([(2, 36), (26, 40), (30, 84), (10, 80)]), 'shade', 'b', False),
             fringe([(66, 0), (90, 16), (96, 40), (92, 64, 1), (84, 48), (76, 60, 1), (72, 40)])],
    'back': [L(outline([(10, 82), (2, 50), (6, 20), (24, 2), (50, -4), (76, 2), (94, 20), (98, 50), (90, 82), (50, 92)])),
             L(outline([(4, 50), (50, 40), (96, 50), (90, 82), (50, 92), (10, 82)]), 'shade', 'b', False)],
}

# Themis Law: pelo verde menta muy claro, con un pico de flequillo hasta la nariz y mechones en punta abiertos a los lados;
# dos lunares negros en la frente, ojos rasgados oscuros
CHARS['themis-law'] = {
    'body': 'normal', 'pal': pal('#c8dcc6', '#fcd8b4', iris='#1e1a1a', shade='#9a8a80'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 96), (10, 72), (-10, 62, 1), (8, 52), (6, 24), (24, 2), (50, -4), (76, 2), (94, 24), (92, 52), (110, 62, 1), (90, 72), (84, 96),
                         (80, 64), (20, 64)])),
              L(outline([(60, 0), (86, 14), (94, 48), (104, 62, 1), (86, 66), (80, 40)]), 'shade', 'b', False),
              fringe([(12, 74), (12, 40), (26, 16), (50, 8), (74, 16), (88, 40), (88, 74), (80, 64), (74, 50), (58, 50), (50, 76, 1), (42, 50), (26, 50),
                      (20, 64)]),
              L(ell(40, 62, 1.8, 1.8), OUTC, 'f', False), L(ell(60, 62, 1.8, 1.8), OUTC, 'f', False)],
    'side': [L(outline([(56, 60), (62, 50), (80, 46), (90, 30), (84, 8), (60, -4), (32, -2), (10, 14), (2, 40), (-14, 56, 1), (6, 62), (6, 86), (22, 96), (40, 90),
                        (48, 76)]), 'shade'),
             L(outline([(60, -4), (84, 8), (90, 30), (80, 46), (56, 40), (30, 30), (10, 14), (32, -2)]), 'mid', 'b', False),
             fringe([(66, 0), (88, 16), (92, 42), (88, 70, 1), (80, 48), (72, 36)])],
    'back': [L(outline([(16, 90), (10, 70), (-14, 58, 1), (8, 52), (6, 24), (24, 2), (50, -4), (76, 2), (94, 24), (92, 52), (114, 58, 1), (90, 70), (84, 90),
                        (50, 96)]), 'shade'),
             L(outline([(4, 54), (6, 24), (24, 2), (50, -4), (76, 2), (94, 24), (96, 54), (70, 40), (50, 44), (30, 40)]), 'mid', 'b', False)],
}

# Orion Hunter: pelo gris claro peinado hacia atrás con una cinta verde oscuro por encima, mechones largos que caen junto a
# las orejas hasta el cuello; cejas gruesas claras y ojos celestes
CHARS['orion-hunter'] = {
    'body': 'normal', 'pal': pal('#c8c2b6', '#fcd8b4', iris='#2ab0c8', shade='#9a8a80', band='#1e4a50', brow='#c8c2b6'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': (52, 40)},
    'front': [L(outline([(14, 66), (8, 36), (20, 10), (50, 2), (80, 10), (92, 36), (86, 66)])),
              L(outline([(10, 60), (6, 90), (8, 120, 1), (14, 92), (20, 66)]), 'mid', 'f', ln=True),
              L(outline([(90, 60), (94, 90), (92, 120, 1), (86, 92), (80, 66)]), 'mid', 'f', ln=True),
              strand([(30, 14), (34, 40)], 'shade', 'b', 1.0), strand([(50, 6), (50, 40)], 'shade', 'b', 1.0), strand([(70, 14), (66, 40)], 'shade', 'b', 1.0),
              L(quad((10, 44), (14, 10), (40, 0)), 'band', 'f', False, False, 3.2), L(quad((90, 44), (86, 10), (60, 0)), 'band', 'f', False, False, 3.2),
              L(outline([(26, 66), (40, 62), (42, 68), (28, 70)]), 'brow', 'f', ln=True), L(outline([(74, 66), (60, 62), (58, 68), (72, 70)]), 'brow', 'f', ln=True)],
    'side': [L(outline([(60, 48), (80, 40), (90, 24), (80, 6), (56, -2), (30, 2), (12, 18), (6, 44), (12, 70), (30, 80), (44, 70)])),
             L(outline([(34, 6), (66, 0), (88, 20), (82, 26), (60, 12), (36, 14)]), 'band', 'f', ln=True),
             L(outline([(62, 50), (66, 80), (64, 116, 1), (58, 84), (56, 56)]), 'mid', 'f', ln=True),
             L(outline([(8, 40), (26, 44), (30, 74), (14, 66)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 70), (8, 36), (20, 10), (50, 2), (80, 10), (92, 36), (86, 70), (76, 84), (68, 74, 1), (60, 86), (50, 76, 1), (40, 86), (32, 74, 1),
                        (24, 84)])),
             L(outline([(56, 4), (82, 12), (92, 40), (84, 70), (62, 80)]), 'shade', 'b', False),
             L(quad((6, 30), (50, 4), (94, 30)), 'band', 'f', False, False, 3.2),
             L(outline([(16, 70), (12, 100), (16, 120, 1), (22, 96), (24, 76)]), 'mid', 'f', ln=True),
             L(outline([(84, 70), (88, 100), (84, 120, 1), (78, 96), (76, 76)]), 'mid', 'f', ln=True)],
}
