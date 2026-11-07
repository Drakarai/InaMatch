"""Dragon Link (go-dragonlink): sus modelos 3D de Inazuma Eleven GO como referencia (busto de frente, perfil y espalda).
Casi todos llevan el pelo blanco con sombras malva."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)


def wpal(skin, iris='#302232', **extra):
    """Pelo blanco con las sombras malva de los modelos."""
    return pal('#dcdfe4', skin, iris=iris, shade='#a8949c', deep='#806a72', light='#ffffff', **extra)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Quentin Cinquedea (portero): piel morena, pelo rosa salmón peinado hacia atrás en una cresta que acaba en pico sobre la
# frente, con mechones largos en punta que salen hacia fuera y hacia atrás por los lados; ojos azules
CHARS['quentin-cinquedea'] = {
    'body': 'normal', 'pal': pal('#e8706a', '#b07a52', iris='#5aa0c8', shade='#c8524e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': [(16, 60), (24, 44), (34, 46), (40, 36), (50, 40), (60, 36), (66, 46), (76, 44), (84, 60)]},
    'front': [L(outline([(16, 64), (12, 40), (24, 14), (40, 2), (50, -16, 1), (60, 2), (76, 14), (88, 40), (84, 64)])),
              L(outline([(56, 4), (78, 16), (88, 44), (78, 54)]), 'shade', 'b', False),
              L(outline([(16, 64), (4, 70), (-12, 72, 1), (6, 78), (-8, 88, 1), (10, 86), (14, 100, 1), (20, 80)]), 'mid', 'b'),
              L(outline([(84, 64), (96, 70), (112, 72, 1), (94, 78), (108, 88, 1), (90, 86), (86, 100, 1), (80, 80)]), 'mid', 'b'),
              strand([(50, -10), (50, 30)], 'shade', 'b', 1.2), strand([(38, 8), (34, 34)], 'shade', 'b', 1.0), strand([(62, 8), (66, 34)], 'shade', 'b', 1.0)],
    'side': [L(outline([(70, 40), (86, 30), (84, 10), (64, -6), (40, -8), (18, 2), (-10, 18, 1), (8, 24), (-22, 44, 1), (2, 48), (-20, 70, 1), (4, 70),
                        (-12, 94, 1), (10, 86), (14, 104, 1), (24, 84), (36, 70), (48, 52)])),
             L(outline([(0, 30), (30, 34), (34, 70), (10, 80)]), 'shade', 'b', False),
             strand([(80, 14), (50, 4), (10, 14)], 'shade', 'b', 1.0), strand([(76, 26), (44, 18), (4, 40)], 'shade', 'b', 1.0),
             strand([(66, 36), (40, 34), (6, 64)], 'shade', 'b', 1.0)],
    'back': [L(outline([(18, 80), (12, 40), (24, 14), (40, 2), (50, -16, 1), (60, 2), (76, 14), (88, 40), (82, 80), (96, 76), (112, 70, 1), (98, 86),
                        (108, 96, 1), (86, 96), (60, 92), (50, 112, 1), (40, 92), (14, 96), (-8, 96, 1), (2, 86), (-12, 70, 1), (4, 76)])),
             L(outline([(56, 4), (80, 16), (88, 50), (80, 84), (60, 90)]), 'shade', 'b', False),
             L(outline([(44, 4), (50, -14, 1), (56, 4), (54, 40), (46, 40)]), 'shade', 'b', False)],
}

# Aim Quintet: pelo blanco en gruesos mechones rizados recogidos arriba en un moño de nudos, los lados rapados en gris,
# dos mechones finos que le caen junto a la cara y una trenza gruesa por detrás que asoma por el hombro
CHARS['aim-quintet'] = {
    'body': 'normal', 'pal': wpal('#e8a468', iris='#2a1a1a', buzz='#6a6058'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': (60, 50)},
    'front': [L(outline([(16, 66), (14, 40), (24, 24), (76, 24), (86, 40), (84, 66), (78, 54), (22, 54)]), 'buzz'),
              L(outline([(14, 34), (6, 20), (10, 4), (22, 0), (30, -10), (42, -4), (50, -14), (58, -4), (70, -10), (78, 0), (90, 4), (94, 20), (86, 34),
                         (72, 30), (60, 40), (50, 32), (40, 40), (28, 30)]), 'mid', 'f'),
              L(outline([(60, -2), (78, 2), (92, 20), (84, 32), (72, 22)]), 'shade', 'f', False),
              strand([(30, 0), (34, 20)], 'deep', 'f', 1.0), strand([(50, -8), (50, 24)], 'deep', 'f', 1.0), strand([(70, 0), (66, 20)], 'deep', 'f', 1.0),
              L(quad((30, 34), (14, 60), (18, 104)), 'mid', 'f', False, False, 2.6), L(quad((70, 34), (86, 60), (82, 100)), 'mid', 'f', False, False, 2.6)],
    'side': [L(outline([(58, 44), (60, 64), (50, 84), (40, 96), (22, 94), (10, 76), (8, 52), (14, 30)]), 'buzz'),
             L(outline([(12, 36), (6, 18), (16, 4), (36, -6), (60, -6), (80, 4), (92, 18), (88, 34), (74, 30), (60, 38), (40, 30), (24, 40)]), 'mid', 'f'),
             L(outline([(14, 30), (12, 18), (30, 24)]), 'shade', 'f', False),
             strand([(30, 0), (34, 22)], 'deep', 'f', 1.0), strand([(56, -4), (56, 24)], 'deep', 'f', 1.0),
             L(quad((84, 30), (92, 70), (84, 104)), 'mid', 'f', False, False, 2.6)],
    'back': [L(outline([(16, 66), (14, 40), (24, 26), (76, 26), (86, 40), (84, 66), (70, 90), (30, 90)]), 'buzz'),
             L(outline([(14, 34), (6, 20), (10, 4), (22, 0), (30, -10), (42, -4), (50, -14), (58, -4), (70, -10), (78, 0), (90, 4), (94, 20), (86, 34),
                        (62, 40), (50, 46), (38, 40)]), 'mid', 'f'),
             L(rope((50, 40), (54, 70), (42, 110), 16), 'mid', 'f', ln=True),
             strand([(42, 60), (58, 64)], 'shade', 'f', 1.2), strand([(42, 76), (56, 82)], 'shade', 'f', 1.2), strand([(40, 92), (52, 98)], 'shade', 'f', 1.2)],
}

# Eljas Viisi: pelo blanco de pinchos que salen hacia arriba y a los lados, con mechones afilados por la frente y una
# melenita que le baja por la nuca; ojos violetas
CHARS['eljas-viisi'] = {
    'body': 'normal', 'pal': wpal('#e8a468', iris='#6a5ab8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 70), (8, 54), (-8, 52, 1), (8, 40), (2, 20, 1), (20, 20), (22, -4, 1), (38, 8), (48, -18, 1), (56, 6), (74, -8, 1), (76, 12),
                         (102, 10, 1), (90, 30), (108, 42, 1), (92, 50), (88, 70), (80, 56), (20, 56)])),
              L(outline([(60, 4), (84, 16), (92, 44), (86, 66), (76, 40)]), 'shade', 'b', False),
              fringe([(14, 64), (16, 42), (30, 26), (50, 20), (70, 26), (84, 42), (86, 66), (78, 54), (72, 66, 1), (66, 48), (58, 58), (54, 76, 1), (48, 50),
                      (38, 62, 1), (34, 48), (24, 66, 1), (20, 54)])],
    'side': [L(outline([(54, 60), (60, 48), (80, 46), (92, 32), (86, 12), (100, -2, 1), (72, 0), (64, -20, 1), (50, -2), (28, -16, 1), (26, 6), (-2, 6, 1),
                        (12, 24), (-6, 38, 1), (8, 46), (6, 70), (2, 96, 1), (18, 86), (26, 100, 1), (34, 84), (46, 76)])),
             L(outline([(6, 40), (26, 42), (30, 80), (10, 80)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 14), (94, 40), (92, 64, 1), (84, 48), (78, 60, 1), (74, 40), (66, 30)])],
    'back': [L(outline([(16, 84), (10, 56), (-6, 50, 1), (8, 40), (0, 18, 1), (20, 20), (22, -4, 1), (38, 8), (48, -18, 1), (56, 6), (74, -8, 1), (76, 12),
                        (102, 10, 1), (90, 30), (108, 42, 1), (92, 52), (86, 84), (74, 100, 1), (64, 88), (54, 104, 1), (46, 88), (36, 102, 1), (28, 88)])),
             L(outline([(56, 8), (86, 18), (92, 50), (84, 82), (62, 90)]), 'shade', 'b', False),
             L(outline([(40, 30), (54, 34), (50, 60)]), 'light', 'b', False)],
}

# Pentra Chek: grandullón de piel morena oscura, la cabeza rapada en gris pardo con una franja de mechones blancos en
# rodillo encima, de la frente a la coronilla; cejas con cicatriz y una sonrisa de dientes
CHARS['pentra-chek'] = {
    'body': 'corpulento', 'pal': wpal('#a07048', iris='#1e1414', buzz='#6e5a4c', buzz_d='#5a4a3e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 100, 'hairline': (58, 44)},
    'front': [L(outline([(16, 66), (12, 36), (22, 14), (50, 8), (78, 14), (88, 36), (84, 66), (78, 50), (22, 50)]), 'buzz'),
              L(outline([(20, 36), (18, 10), (30, -2), (50, -6), (70, -2), (82, 10), (80, 36), (70, 26), (60, 34), (50, 26), (40, 34), (30, 26)]), 'mid', 'f'),
              strand([(30, 4), (30, 28)], 'shade', 'f', 1.2), strand([(42, 0), (42, 30)], 'shade', 'f', 1.2), strand([(58, 0), (58, 30)], 'shade', 'f', 1.2),
              strand([(70, 4), (70, 28)], 'shade', 'f', 1.2)],
    'side': [L(outline([(66, 44), (60, 64), (50, 84), (40, 96), (22, 94), (10, 76), (8, 46), (16, 20), (40, 6), (66, 10), (84, 20), (88, 36)]), 'buzz'),
             L(outline([(16, 30), (20, 10), (40, -2), (64, -2), (84, 8), (90, 22), (80, 24), (60, 14), (36, 18)]), 'mid', 'f'),
             L(outline([(20, 40), (30, 60), (24, 84)]), 'buzz_d', 'b', False)],
    'back': [L(outline([(16, 66), (12, 36), (22, 14), (50, 8), (78, 14), (88, 36), (84, 66), (70, 92), (30, 92)]), 'buzz'),
             L(outline([(56, 14), (84, 30), (84, 70), (64, 90)]), 'buzz_d', 'b', False),
             L(outline([(20, 34), (18, 10), (30, -2), (50, -6), (70, -2), (82, 10), (80, 34), (74, 46, 1), (68, 32), (62, 46, 1), (56, 32), (50, 46, 1), (44, 32),
                        (38, 46, 1), (32, 32), (26, 46, 1)]), 'mid', 'f')],
}

# Federigo Cinco: melena blanca enorme de mechones gruesos como rastas que salen en todas direcciones y le caen por la
# frente hasta los ojos; cara pequeña y seria
CHARS['federigo-cinco'] = {
    'body': 'normal', 'pal': wpal('#e8a468', iris='#1e1414'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 96), (-6, 90), (-10, 70), (-6, 50), (-8, 30), (2, 14), (16, 2), (30, -6), (40, -14), (50, -6), (60, -14), (70, -6), (84, 2),
                         (98, 14), (108, 30), (106, 50), (110, 70), (106, 90), (88, 96), (84, 64), (16, 64)])),
              L(outline([(62, -4), (90, 10), (106, 46), (104, 88), (88, 86), (80, 40)]), 'shade', 'b', False),
              fringe([(10, 74), (8, 48), (18, 26), (40, 16), (60, 16), (82, 26), (92, 48), (90, 74), (82, 68), (80, 56), (72, 70), (64, 54), (56, 70), (50, 52),
                      (42, 70), (36, 54), (28, 70), (20, 56), (18, 70)]),
              strand([(22, 30), (14, 70)], 'shade', 'f', 1.2), strand([(40, 18), (36, 60)], 'shade', 'f', 1.2), strand([(60, 18), (64, 60)], 'shade', 'f', 1.2),
              strand([(78, 30), (86, 70)], 'shade', 'f', 1.2),
              L(outline([(36, 0), (48, -16), (56, -2)]), 'mid', 'f', ln=True), L(outline([(46, -2), (60, -16), (66, 0)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(56, 64), (60, 50), (82, 54), (98, 40), (96, 14), (78, -6), (50, -14), (22, -8), (2, 10), (-10, 34), (-12, 62), (-6, 88), (12, 100),
                        (34, 98), (46, 86)])),
             L(outline([(-8, 40), (20, 44), (28, 92), (0, 90)]), 'shade', 'b', False),
             strand([(10, 6), (-6, 40)], 'shade', 'b', 1.2), strand([(30, 0), (8, 60)], 'shade', 'b', 1.2), strand([(46, 8), (26, 80)], 'shade', 'b', 1.2),
             fringe([(66, 2), (92, 16), (100, 42), (96, 70), (88, 56), (82, 68), (76, 44), (66, 32)])],
    'back': [L(outline([(10, 100), (-6, 90), (-10, 70), (-6, 50), (-8, 30), (2, 14), (16, 2), (30, -6), (40, -14), (50, -6), (60, -14), (70, -6), (84, 2),
                        (98, 14), (108, 30), (106, 50), (110, 70), (106, 90), (90, 100), (70, 106), (50, 102), (30, 106)])),
             L(outline([(56, -4), (90, 10), (106, 46), (104, 92), (70, 102), (70, 40)]), 'shade', 'b', False),
             strand([(14, 20), (6, 90)], 'shade', 'b', 1.2), strand([(34, 6), (30, 100)], 'shade', 'b', 1.2), strand([(50, 0), (50, 100)], 'shade', 'b', 1.2),
             strand([(66, 6), (70, 100)], 'shade', 'b', 1.2), strand([(86, 20), (94, 90)], 'shade', 'b', 1.2)],
}

# Ferdinand Delafuente: piel rojiza, pelo blanco en una corona de llamas de puntas hacia arriba, sujeto con una cinta
# blanca y naranja ancha en la frente; pinturas blancas en las mejillas y ojos verdes
CHARS['ferdinand-delaf-nfe'] = {
    'body': 'normal', 'pal': wpal('#c8643e', iris='#3a8a5a', band='#f4ece0', band2='#e07a3a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(18, 52), (12, 30), (4, -6, 1), (22, 10), (26, -18, 1), (38, 4), (50, -24, 1), (62, 4), (74, -18, 1), (78, 10), (96, -6, 1), (88, 30),
                         (82, 52)])),
              L(outline([(58, 0), (78, 8), (88, 30), (80, 48)]), 'shade', 'b', False),
              L(outline([(36, 6), (50, -10), (64, 6), (60, 46), (40, 46)]), 'mid', 'b', ln=True),
              L(outline([(10, 58), (10, 42), (50, 36), (90, 42), (90, 58), (50, 52)]), 'band', 'f', ln=True),
              L(quad((10, 48), (50, 42), (90, 48)), 'band2', 'f', False, False, 3.0),
              L([(22, 70), (32, 64)], 'band', 'f', False, False, 2.4), L([(78, 70), (68, 64)], 'band', 'f', False, False, 2.4)],
    'side': [L(outline([(26, 46), (20, 20), (8, -8, 1), (28, 6), (40, -20, 1), (52, 2), (70, -14, 1), (72, 10), (90, 6, 1), (86, 28), (84, 46)])),
             L(outline([(4, 60), (6, 40), (50, 34), (96, 40), (96, 58), (50, 54)]), 'band', 'f', ln=True),
             L(quad((4, 50), (50, 44), (96, 50)), 'band2', 'f', False, False, 3.0)],
    'back': [L(outline([(18, 52), (12, 30), (4, -6, 1), (22, 10), (26, -18, 1), (38, 4), (50, -24, 1), (62, 4), (74, -18, 1), (78, 10), (96, -6, 1), (88, 30),
                        (82, 52)])),
             L(outline([(56, 0), (80, 10), (88, 32), (80, 50)]), 'shade', 'b', False),
             L(outline([(10, 58), (10, 42), (50, 38), (90, 42), (90, 58), (50, 54)]), 'band', 'f', ln=True),
             L(quad((10, 48), (50, 44), (90, 48)), 'band2', 'f', False, False, 3.0)],
}

# Fivier Saviola: melena blanca en casco redondo hasta la barbilla, con raya a un lado y la punta hacia dentro; gafas
# negras de pasta, cejas blancas gruesas y sonrisa
CHARS['fivier-saviola'] = {
    'body': 'normal', 'pal': wpal('#fcdcc0', iris='#2a1a1a'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False, 'glasses': OUTC, 'glasses_rect': True},
    'front': [L(outline([(8, 100), (2, 70), (4, 36), (18, 12), (44, 0), (70, 4), (90, 20), (98, 50), (96, 80), (90, 100), (80, 92), (84, 64), (16, 64), (18, 92)])),
              L(outline([(62, 6), (88, 20), (98, 52), (92, 94), (84, 88), (82, 40)]), 'shade', 'b', False),
              fringe([(10, 74), (10, 44), (22, 22), (44, 12), (66, 16), (82, 32), (86, 58), (74, 44), (60, 38), (44, 40), (30, 50), (20, 62)]),
              L(outline([(26, 22), (46, 16), (34, 30)]), 'light', 'f', False),
              L([(26, 62), (40, 60)], 'mid', 'f', False, False, 3.0), L([(60, 60), (74, 62)], 'mid', 'f', False, False, 3.0)],
    'side': [L(outline([(52, 74), (58, 54), (78, 48), (92, 34), (88, 14), (66, 0), (36, -2), (12, 12), (2, 40), (4, 76), (16, 98), (40, 100), (54, 96)])),
             L(outline([(4, 40), (40, 40), (52, 94), (16, 94)]), 'shade', 'b', False),
             fringe([(62, 4), (88, 16), (94, 40), (90, 84, 1), (84, 60), (78, 42)])],
    'back': [L(outline([(6, 96), (2, 70), (4, 36), (18, 12), (44, 0), (70, 4), (90, 20), (98, 50), (96, 80), (92, 96), (70, 100), (50, 98), (30, 100)])),
             L(outline([(56, 4), (88, 20), (98, 52), (94, 96), (64, 98), (66, 40)]), 'shade', 'b', False)],
}

# Quinque Flores: pelo blanco liso peinado de lado en una ola que le tapa el ojo derecho, con puntas abiertas por detrás;
# ojos violetas de párpado caído
CHARS['quinque-flores'] = {
    'body': 'normal', 'pal': wpal('#fcdcc0', iris='#6a5aa8'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(14, 70), (8, 40), (0, 22, 1), (14, 18), (16, 0), (36, -8), (60, -10), (84, 0), (104, 6, 1), (92, 20), (100, 40, 1), (90, 46), (88, 70),
                         (80, 56), (20, 56)])),
              L(outline([(64, -4), (88, 6), (94, 40), (86, 64), (78, 36)]), 'shade', 'b', False),
              fringe([(12, 66), (14, 40), (30, 20), (56, 12), (80, 22), (88, 44), (88, 66), (80, 52), (70, 46), (60, 50), (54, 70), (48, 92, 1), (38, 82),
                      (24, 86, 1), (22, 74)]),
              L(outline([(24, 26), (50, 16), (40, 30)]), 'light', 'f', False)],
    'side': [L(outline([(54, 62), (60, 50), (80, 48), (92, 34), (88, 12), (70, -6), (40, -10), (4, -6, 1), (16, 8), (-8, 20, 1), (8, 32), (4, 60), (12, 80),
                        (28, 84), (42, 76)]), 'shade'),
             L(outline([(30, -8), (60, -10), (84, 0), (94, 20), (96, 46), (90, 62, 1), (82, 46), (70, 34), (40, 22), (14, 20), (4, -6, 1)]), 'mid', 'f')],
    'back': [L(outline([(16, 84), (10, 56), (-6, 48, 1), (8, 40), (0, 20, 1), (16, 16), (24, -2), (50, -8), (76, -2), (86, 16), (104, 22, 1), (92, 40), (106, 48, 1),
                        (90, 56), (84, 84), (66, 92), (50, 88), (34, 92)]), 'shade'),
             L(outline([(24, -2), (50, -8), (76, -2), (86, 16), (70, 26), (60, 20), (50, 30), (36, 20), (16, 24)]), 'mid', 'b', False)],
}

# Jacques Cinquini: melena blanca lisa con raya en medio que le cae por los lados hasta debajo de las orejas, con las puntas
# abiertas; ojos rojos
CHARS['jacques-cinquini'] = {
    'body': 'normal', 'pal': wpal('#f8c89c', iris='#b01e1e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': [(14, 80), (20, 44), (34, 36), (50, 30), (66, 36), (80, 44), (86, 80)]},
    'front': [L(outline([(12, 100), (-2, 100, 1), (6, 84), (4, 40), (16, 12), (50, 0), (84, 12), (96, 40), (94, 84), (102, 100, 1), (88, 100), (84, 60), (16, 60)])),
              L(outline([(62, 4), (86, 16), (96, 44), (92, 94), (84, 80)]), 'shade', 'b', False),
              strand([(50, 2), (50, 30)], 'deep', 'b', 1.2), strand([(40, 6), (20, 50), (16, 90)], 'shade', 'b', 1.0), strand([(60, 6), (80, 50), (84, 90)], 'shade', 'b', 1.0)],
    'side': [L(outline([(54, 76), (58, 56), (76, 52), (92, 36), (86, 12), (62, -2), (32, 0), (10, 16), (2, 46), (2, 86), (-6, 102, 1), (16, 94), (30, 104, 1),
                        (40, 92), (54, 96, 1)]), 'shade'),
             L(outline([(62, -2), (88, 10), (94, 36), (90, 60), (80, 92, 1), (76, 54), (60, 30), (34, 10)]), 'mid', 'f')],
    'back': [L(outline([(10, 100), (-2, 102, 1), (4, 84), (4, 40), (16, 12), (50, 0), (84, 12), (96, 40), (96, 84), (102, 102, 1), (88, 100), (74, 104, 1), (62, 96),
                        (50, 104, 1), (38, 96), (26, 104, 1)]), 'shade'),
             L(outline([(16, 40), (16, 12), (50, 0), (84, 12), (84, 40), (70, 30), (50, 36), (30, 30)]), 'mid', 'b', False),
             strand([(50, 2), (50, 90)], 'deep', 'b', 1.0)],
}

# David Quintola: piel morena, pelo blanco corto con dos cuernos gruesos de pelo que salen hacia arriba y hacia fuera a los
# lados y flequillo de picos cortos; ojos castaños
CHARS['david-quintola'] = {
    'body': 'normal', 'pal': wpal('#b07c52', iris='#5a3a1e'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 64), (6, 50), (4, 10), (14, -8, 1), (24, 20), (40, 16), (60, 16), (76, 20), (86, -8, 1), (96, 10), (94, 50), (84, 64)])),
              L(outline([(10, 70), (0, 66, 1), (8, 50), (16, 50)]), 'mid', 'b'), L(outline([(90, 70), (100, 66, 1), (92, 50), (84, 50)]), 'mid', 'b'),
              L(outline([(84, 0), (94, 14), (90, 50), (80, 30)]), 'shade', 'b', False), L(outline([(8, 10), (14, 2), (16, 30), (10, 40)]), 'shade', 'b', False),
              fringe([(14, 56), (16, 34), (30, 26), (50, 24), (70, 26), (84, 34), (86, 56), (78, 46), (72, 56, 1), (66, 46), (58, 56, 1), (52, 46), (44, 56, 1),
                      (38, 46), (30, 56, 1), (22, 46)])],
    'side': [L(outline([(56, 60), (62, 48), (82, 46), (92, 32), (84, 18), (70, 10), (50, -16, 1), (44, 8), (26, 4), (-4, -10, 1), (12, 18), (6, 40), (4, 70),
                        (14, 88), (30, 90), (44, 76)])),
             L(outline([(6, 40), (26, 42), (30, 80), (10, 80)]), 'shade', 'b', False),
             fringe([(68, 12), (88, 22), (94, 40), (90, 54, 1), (84, 42), (76, 34)])],
    'back': [L(outline([(16, 84), (10, 50), (6, 10), (14, -10, 1), (26, 18), (40, 14), (60, 14), (74, 18), (86, -10, 1), (94, 10), (90, 50), (84, 84), (66, 92),
                        (50, 100, 1), (34, 92)])),
             L(outline([(58, 16), (84, 20), (90, 54), (84, 82), (62, 90)]), 'shade', 'b', False),
             strand([(30, 30), (36, 70)], 'shade', 'b', 1.0)],
}

# Erik Pentona: piel morena y cabeza rapada, con una trenza blanca gruesa que le cruza la cabeza desde la frente hasta la
# nuca y cae por detrás hasta el hombro; ojos verdes
CHARS['erik-pentona'] = {
    'body': 'normal', 'pal': wpal('#a87a52', iris='#2a8a6a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(blob([(16, 64), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 64)]), 'skin'),
              L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'skin_d', 'b', False),
              L(rope((40, 40), (40, 0), (66, 16), 14), 'mid', 'f', ln=True),
              strand([(34, 30), (46, 28)], 'shade', 'f', 1.2), strand([(34, 16), (46, 12)], 'shade', 'f', 1.2), strand([(46, 4), (54, 10)], 'shade', 'f', 1.2),
              L(rope((14, 80), (4, 96), (14, 112), 10), 'mid', 'f', ln=True)],
    'side': [L(rope((82, 30), (54, 4), (24, 20), 13), 'mid', 'f', ln=True), L(rope((24, 20), (8, 56), (24, 100), 13), 'mid', 'f', ln=True),
             strand([(70, 12), (74, 22)], 'shade', 'f', 1.2), strand([(52, 6), (54, 18)], 'shade', 'f', 1.2), strand([(34, 12), (40, 22)], 'shade', 'f', 1.2),
             strand([(12, 48), (24, 48)], 'shade', 'f', 1.2), strand([(14, 72), (26, 70)], 'shade', 'f', 1.2)],
    'back': [L(ell(50, 8, 9, 8), 'mid', 'f', ln=True), L(rope((44, 14), (20, 40), (22, 80), 13), 'mid', 'f', ln=True),
             L(rope((22, 80), (46, 104), (80, 90), 12), 'mid', 'f', ln=True),
             strand([(22, 36), (34, 40)], 'shade', 'f', 1.2), strand([(16, 58), (28, 60)], 'shade', 'f', 1.2), strand([(40, 90), (44, 102)], 'shade', 'f', 1.2),
             strand([(60, 92), (62, 102)], 'shade', 'f', 1.2)],
}

# Leonidas Epsilon (portero; sin modelo 3D, del retrato): piel morena y pelo blanco revuelto a mechones ondulados que le
# caen por la frente y los lados; ojos verde azulado
CHARS['leonidas-epsilon'] = {
    'body': 'normal', 'pal': wpal('#c08a5a', iris='#2a8a9a'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 86), (4, 70), (2, 40), (10, 16), (30, 0), (54, -4), (78, 4), (94, 22), (98, 50), (96, 76), (88, 88), (84, 60), (16, 60)])),
              L(outline([(62, 2), (88, 16), (96, 50), (90, 82), (82, 50)]), 'shade', 'b', False),
              fringe([(10, 74), (10, 44), (24, 22), (50, 12), (76, 20), (88, 42), (90, 72), (82, 58), (76, 66, 1), (70, 46), (60, 56, 1), (54, 42), (44, 58, 1),
                      (36, 44), (26, 60, 1), (18, 52)]),
              strand([(30, 22), (40, 40)], 'shade', 'f', 1.0), strand([(62, 22), (70, 40)], 'shade', 'f', 1.0)],
    'side': [L(outline([(54, 62), (60, 50), (80, 48), (92, 34), (88, 12), (66, -4), (36, -6), (12, 8), (2, 36), (0, 66), (8, 88), (24, 94), (40, 84)])),
             L(outline([(4, 40), (26, 44), (30, 86), (10, 86)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 42), (92, 64, 1), (84, 48), (78, 58, 1), (74, 40), (66, 30)])],
    'back': [L(outline([(10, 88), (2, 70), (2, 40), (10, 16), (30, 0), (54, -4), (78, 4), (94, 22), (98, 50), (98, 76), (90, 90), (70, 98), (50, 94), (30, 98)])),
             L(outline([(58, 2), (88, 16), (98, 50), (92, 88), (66, 96)]), 'shade', 'b', False),
             strand([(30, 20), (24, 60), (30, 90)], 'shade', 'b', 1.0), strand([(70, 20), (76, 60), (70, 90)], 'shade', 'b', 1.0)],
}

# George Wu: pelo blanco de pinchos peinados hacia atrás y hacia la derecha, con un mechón suelto que sale por el lado
# derecho de la cara y uno que le cruza la frente; ojos redondos y cara de pasmo
CHARS['george-wu'] = {
    'body': 'normal', 'pal': wpal('#fcdcc0', iris='#2a1a1a'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 66), (4, 50), (2, 22), (8, -8, 1), (24, 8), (38, -6), (58, -4), (74, -14, 1), (82, 8), (94, 16), (98, 40), (90, 64), (86, 50),
                         (20, 50)])),
              L(outline([(84, 60), (100, 76), (110, 82, 1), (92, 80), (82, 70)]), 'mid', 'b'),
              L(outline([(60, 0), (84, 10), (96, 40), (88, 60), (78, 36)]), 'shade', 'b', False),
              fringe([(12, 60), (14, 34), (30, 16), (54, 10), (78, 18), (88, 38), (88, 56), (80, 40), (64, 34), (44, 36), (30, 44), (20, 56)])],
    'side': [L(outline([(54, 60), (60, 48), (82, 46), (92, 30), (84, 12), (96, -10, 1), (70, -2), (60, -20, 1), (46, -4), (24, -10, 1), (22, 8), (-12, 6, 1), (8, 24),
                        (-16, 40, 1), (8, 46), (-6, 70, 1), (14, 66), (16, 84), (34, 80), (46, 70)]), 'shade'),
             L(outline([(60, -4), (82, 6), (94, 28), (92, 48), (80, 40), (62, 26), (40, 24)]), 'mid', 'f')],
    'back': [L(outline([(16, 80), (8, 60), (-16, 70, 1), (4, 46), (-6, 24, 1), (12, 22), (14, -4, 1), (32, 8), (46, -8, 1), (56, 8), (76, -6, 1), (78, 14),
                        (104, 6, 1), (92, 34), (112, 44, 1), (92, 54), (94, 76, 1), (84, 80), (50, 88)]), 'shade'),
             L(outline([(14, -4, 1), (32, 8), (46, -8, 1), (56, 8), (76, -6, 1), (78, 14), (60, 24), (40, 22), (20, 28)]), 'mid', 'b', False)],
}

# Geert Vandevijf: melena blanca en casco con flequillo recto que le tapa las cejas y los lados lisos hasta la barbilla;
# ojos azules entornados, mirada seria
CHARS['geert-vandevijf'] = {
    'body': 'normal', 'pal': wpal('#f8c89c', iris='#4a8ab8'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 104), (6, 70), (6, 36), (18, 12), (50, 0), (82, 12), (94, 36), (94, 70), (88, 104), (82, 98), (84, 64), (16, 64), (18, 98)])),
              L(outline([(62, 4), (86, 16), (94, 44), (90, 100), (84, 90)]), 'shade', 'b', False),
              fringe([(12, 70), (12, 40), (24, 18), (50, 10), (76, 18), (88, 40), (88, 70), (82, 66), (16, 66)]),
              strand([(30, 30), (30, 64)], 'shade', 'f', 1.0), strand([(50, 20), (50, 64)], 'shade', 'f', 1.0), strand([(70, 30), (70, 64)], 'shade', 'f', 1.0)],
    'side': [L(outline([(48, 92), (50, 70), (60, 60), (82, 60), (92, 38), (88, 14), (66, 0), (36, -2), (12, 12), (4, 40), (6, 90), (24, 96)]), 'shade'),
             L(outline([(36, -2), (66, 0), (88, 14), (94, 38), (94, 64), (86, 80, 1), (78, 64), (64, 44), (40, 30), (12, 30), (12, 12)]), 'mid', 'f')],
    'back': [L(outline([(10, 96), (6, 70), (6, 36), (18, 12), (50, 0), (82, 12), (94, 36), (94, 70), (90, 96), (82, 102, 1), (50, 98), (18, 102, 1)]), 'shade'),
             L(outline([(18, 30), (18, 12), (50, 0), (82, 12), (86, 36), (60, 30), (40, 40), (20, 44)]), 'mid', 'b', False)],
}

# Folke Fem: pelo blanco liso peinado hacia atrás, pegado a la cabeza, con un mechón que cae por la sien; sonrisa de dientes
# y ojos amarillos
CHARS['folke-fem'] = {
    'body': 'normal', 'pal': wpal('#e8a468', iris='#b88a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98, 'hairline': [(16, 66), (20, 42), (34, 32), (50, 30), (66, 32), (80, 42), (84, 66)]},
    'front': [L(outline([(16, 66), (12, 36), (24, 12), (50, 2), (76, 12), (88, 36), (84, 66)])),
              L(outline([(60, 6), (82, 18), (88, 44), (80, 60)]), 'shade', 'b', False),
              strand([(40, 6), (30, 30), (22, 60)], 'shade', 'b', 1.0), strand([(60, 6), (70, 30), (78, 60)], 'shade', 'b', 1.0),
              L(quad((28, 30), (20, 48), (22, 70)), 'mid', 'f', False, False, 3.0)],
    'side': [L(outline([(70, 40), (86, 28), (78, 8), (56, -2), (30, 0), (12, 16), (6, 44), (10, 74), (22, 86), (36, 82), (46, 64), (52, 46)])),
             L(outline([(8, 40), (28, 40), (34, 78), (14, 78)]), 'shade', 'b', False),
             strand([(80, 14), (50, 8), (14, 30)], 'shade', 'b', 1.0), strand([(70, 30), (40, 28), (14, 60)], 'shade', 'b', 1.0)],
    'back': [L(outline([(16, 80), (12, 40), (24, 14), (50, 2), (76, 14), (88, 40), (84, 80), (66, 92), (34, 92)])),
             L(outline([(56, 6), (82, 18), (88, 50), (80, 82), (60, 90)]), 'shade', 'b', False)],
}

# Naji Khamsa: pelo blanco liso con raya a un lado, un mechón largo que le cae por el centro de la frente y dos coletas
# finas a los lados de la nuca; ojos amarillos
CHARS['naji-khamsa'] = {
    'body': 'normal', 'pal': wpal('#e8a468', iris='#c8a01e'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': [(16, 66), (20, 44), (34, 34), (48, 30), (62, 36), (80, 44), (84, 66)]},
    'front': [L(outline([(16, 70), (10, 38), (24, 12), (50, 2), (76, 12), (90, 38), (84, 70)])),
              L(outline([(60, 6), (82, 18), (90, 44), (82, 64)]), 'shade', 'b', False),
              L(outline([(10, 74), (2, 90), (6, 112, 1), (14, 94), (16, 80)]), 'mid', 'b'), L(outline([(90, 74), (98, 90), (94, 112, 1), (86, 94), (84, 80)]), 'mid', 'b'),
              fringe([(40, 10), (56, 14), (52, 40), (54, 68), (46, 84, 1), (44, 50), (36, 30)]),
              strand([(44, 6), (40, 30)], 'shade', 'f', 1.0)],
    'side': [L(outline([(68, 40), (86, 30), (80, 8), (58, -2), (30, 0), (12, 16), (6, 44), (10, 72), (22, 84), (36, 80), (46, 62), (54, 46)])),
             L(outline([(14, 70), (6, 94), (12, 114, 1), (22, 92), (26, 76)]), 'mid', 'b'),
             L(outline([(8, 40), (28, 40), (34, 74), (14, 76)]), 'shade', 'b', False),
             strand([(80, 14), (50, 8), (14, 34)], 'shade', 'b', 1.0), fringe([(80, 10), (96, 30), (100, 60), (92, 76, 1), (90, 50), (80, 30)])],
    'back': [L(outline([(16, 80), (12, 40), (24, 14), (50, 2), (76, 14), (88, 40), (84, 80), (66, 90), (34, 90)])),
             L(outline([(56, 6), (82, 18), (88, 50), (80, 80), (60, 88)]), 'shade', 'b', False),
             L(outline([(28, 84), (18, 98), (20, 116, 1), (30, 100), (36, 88)]), 'mid', 'f'), L(outline([(72, 84), (82, 98), (80, 116, 1), (70, 100), (64, 88)]), 'mid', 'f'),
             L(ell(32, 86, 3.4, 3), OUTC, 'f', False), L(ell(68, 86, 3.4, 3), OUTC, 'f', False)],
}
