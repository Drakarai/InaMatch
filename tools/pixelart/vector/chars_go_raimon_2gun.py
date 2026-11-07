"""Raimon segundo equipo (go-raimon-2gun): sus modelos 3D de Inazuma Eleven GO como referencia (busto de frente, perfil y espalda).
Aoyama (shunsuke-aoyama) e Ichino (hugues-baudet) tienen aquí el mismo modelo que en el Raimon de GO: se reutilizan sus dibujos."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from chars_alius import SKULL_B, SKULL_F, WIDE_FACE
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Monta A.T. Bano (portero): gordito de cara redonda; pelo azul marino alborotado de puntas encima de una cinta naranja
# ancha atada en la frente, que asoma por debajo en la nuca; ceño fruncido
CHARS['monta-a-t-bano'] = {
    'body': 'corpulento', 'pal': pal('#20245a', '#fcd8b0', iris='#2a6a6a', band='#f0a030', band_d='#c87a1a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 102, 'face_front': WIDE_FACE, 'hairline': False},
    'front': [L(outline([(10, 56), (4, 34), (8, 8), (18, -6), (14, -20, 1), (32, -10), (42, -24, 1), (54, -10), (68, -20, 1), (74, -4), (92, -6, 1), (90, 10), (108, 16, 1),
                         (98, 30), (110, 46, 1), (96, 54), (98, 70, 1), (86, 60), (50, 56)])),
              L(outline([(60, -8), (88, 2), (100, 34), (94, 60), (80, 40)]), 'shade', 'b', False),
              L(outline([(8, 58), (6, 42), (50, 38), (94, 42), (92, 58), (50, 54)]), 'band', 'f', ln=True),
              L(outline([(60, 40), (94, 42), (92, 58), (62, 56)]), 'band_d', 'f', False)],
    'side': [L(outline([(54, 46), (66, 34), (60, 20), (74, 6, 1), (56, 4), (52, -16, 1), (36, -4), (14, -18, 1), (14, 4), (-8, 10, 1), (6, 24), (-10, 40, 1), (8, 48),
                        (2, 74, 1), (20, 70), (22, 90, 1), (34, 74), (44, 62)])),
             L(outline([(4, 34), (24, 40), (24, 66), (6, 60)]), 'shade', 'b', False),
             L(outline([(4, 54), (6, 38), (66, 36), (68, 52)]), 'band', 'f', ln=True)],
    'back': [L(outline([(14, 90), (2, 82, 1), (8, 60), (-4, 46, 1), (6, 34), (4, 8), (18, -6), (14, -20, 1), (32, -10), (42, -24, 1), (54, -10), (70, -20, 1), (74, -4),
                        (94, -6, 1), (90, 10), (110, 16, 1), (98, 32), (110, 48, 1), (96, 62), (100, 82, 1), (86, 90), (70, 98, 1), (60, 90), (50, 98, 1), (40, 90),
                        (28, 98, 1)])),
             L(outline([(56, -8), (88, 2), (100, 34), (94, 84), (66, 92)]), 'shade', 'b', False),
             L(outline([(6, 62), (6, 48), (50, 52), (94, 48), (94, 62), (50, 66)]), 'band', 'f', ln=True),
             L(outline([(44, 60), (40, 76), (50, 70), (60, 76), (56, 60)]), 'band_d', 'f', ln=True)],
}

# Tom Gato: pelo negro con dos picos a los lados de lo alto como orejas de gato, mechones largos y finos que le caen por
# la frente y junto a las mejillas; ojos verdes grandes
CHARS['tom-gato'] = {
    'body': 'normal', 'pal': pal('#2a2a2c', '#fcdcb4', iris='#2a8a5a', light='#4a4a50'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 98), (6, 70), (6, 40), (-2, -6, 1), (20, 8), (50, 2), (80, 8), (102, -6, 1), (94, 40), (94, 70), (86, 98), (82, 64), (18, 64)])),
              L(outline([(62, 6), (90, 6), (94, 46), (90, 90), (80, 50)]), 'shade', 'b', False),
              fringe([(12, 96), (10, 50), (22, 20), (50, 12), (78, 20), (90, 50), (88, 96), (82, 70), (78, 50), (66, 40), (58, 50), (54, 34), (46, 34), (42, 50), (34, 40),
                      (22, 50), (18, 70)]),
              strand([(50, 14), (50, 34)], 'deep', 'f', 1.0)],
    'side': [L(outline([(54, 66), (58, 52), (80, 50), (92, 34), (88, 10), (66, 0), (40, -10), (22, -4), (12, -12, 1), (8, 18), (4, 50), (10, 80), (24, 96, 1), (30, 84),
                        (42, 82)])),
             L(outline([(4, 40), (24, 44), (30, 86), (10, 80)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 42), (94, 80, 1), (86, 56), (78, 40)])],
    'back': [L(outline([(10, 96), (4, 60), (6, 40), (-2, -6, 1), (20, 8), (50, 2), (80, 8), (102, -6, 1), (94, 40), (96, 60), (90, 96), (80, 84), (70, 92, 1), (60, 84),
                        (50, 92, 1), (40, 84), (30, 92, 1), (20, 84)])),
             L(outline([(56, 6), (90, 6), (94, 46), (92, 90), (62, 86)]), 'shade', 'b', False)],
}

# Joaquín Coronado: piel morena oscura, pelo de pinchos rojos encima y negro por debajo, con mechones negros por la
# frente; ojos blancos fieros y un colmillo asomando
CHARS['joaqu-n-coronado'] = {
    'body': 'normal', 'pal': pal('#a81a14', '#9a6a44', iris='#1e1414', under='#2a1a1a', shade='#7a1210'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 70), (6, 54), (8, 30), (92, 30), (94, 54), (84, 70), (80, 56), (20, 56)]), 'under'),
              L(outline([(10, 44), (-8, 36, 1), (6, 26), (-4, 10, 1), (16, 10), (18, -10, 1), (32, 2), (40, -20, 1), (50, -2), (60, -24, 1), (66, 0), (82, -10, 1), (84, 10),
                         (104, 10, 1), (94, 26), (108, 36, 1), (90, 44), (50, 40)])),
              L(outline([(56, -2), (82, -6), (98, 22), (88, 40), (72, 26)]), 'shade', 'b', False),
              fringe([(20, 56), (24, 40), (38, 36), (50, 40), (62, 36), (76, 40), (80, 56), (70, 50), (62, 60, 1), (56, 48), (50, 60, 1), (44, 48), (38, 60, 1), (30, 50)],
                     'under'),
              L([(56, 101), (57, 104), (58, 101)], WHITE, 'f', False, False, 1.4)],
    'side': [L(outline([(54, 58), (60, 46), (82, 46), (90, 30), (82, 18), (10, 22), (2, 50), (12, 74), (26, 80), (42, 70)]), 'under'),
             L(outline([(6, 40), (-10, 30, 1), (8, 22), (0, 4, 1), (20, 6), (26, -12, 1), (40, 0), (56, -16, 1), (64, 0), (84, -6, 1), (82, 12), (100, 18, 1), (84, 30),
                        (50, 32), (24, 40)]))],
    'back': [L(blob(SKULL_B), 'under'),
             L(outline([(4, 62), (-10, 52, 1), (6, 40), (-6, 24, 1), (14, 18), (14, -2, 1), (30, 6), (40, -14, 1), (50, 2), (60, -16, 1), (68, 4), (86, -4, 1), (86, 14),
                        (106, 22, 1), (94, 38), (110, 52, 1), (96, 62), (80, 54), (70, 64, 1), (60, 54), (50, 64, 1), (40, 54), (30, 64, 1), (20, 54)])),
             L(outline([(56, 2), (86, 10), (96, 40), (90, 58), (64, 54)]), 'shade', 'b', False)],
}

# Conant Briain: pelo naranja esponjoso y redondo, de mechones gruesos con puntas vueltas hacia fuera a los lados y dos
# picos arriba; pecas y ojos verde agua
CHARS['conant-briain'] = {
    'body': 'normal', 'pal': pal('#f06a28', '#fcdcc0', iris='#2a9a9a', shade='#c84e18', light='#ff9a5a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 90), (-8, 88), (-12, 70), (2, 58), (-6, 40), (6, 20), (14, 4), (20, -14, 1), (34, -2), (48, -8), (58, -20, 1), (64, -4), (82, 4), (94, 20),
                         (106, 40), (98, 58), (112, 70), (108, 88), (88, 90), (84, 64), (16, 64)])),
              L(outline([(60, -2), (86, 8), (104, 42), (106, 86), (90, 84), (80, 40)]), 'shade', 'b', False),
              fringe([(12, 72), (10, 44), (22, 22), (48, 12), (74, 18), (88, 40), (90, 72), (82, 60), (76, 66, 1), (70, 52), (60, 60), (54, 46), (44, 58), (36, 48), (28, 62),
                      (20, 56)]),
              L(outline([(28, 20), (44, 14), (38, 26)]), 'light', 'f', False),
              L([(30, 88), (31, 89)], OUTC, 'f', False, False, 1.0), L([(34, 90), (35, 91)], OUTC, 'f', False, False, 1.0),
              L([(66, 88), (67, 89)], OUTC, 'f', False, False, 1.0), L([(70, 90), (71, 91)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(56, 64), (60, 52), (82, 50), (94, 36), (90, 14), (78, -2), (80, -18, 1), (64, -8), (50, -18, 1), (40, -6), (14, 4), (-6, 30), (-14, 60), (-6, 80),
                        (16, 86), (32, 80), (44, 78)])),
             L(outline([(-8, 50), (20, 50), (26, 80), (-4, 80)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 16), (96, 42), (92, 64, 1), (84, 48), (76, 36)])],
    'back': [L(outline([(-12, 88), (-14, 66), (-4, 52), (-6, 32), (6, 14), (20, -10, 1), (34, -2), (48, -8), (58, -20, 1), (66, -4), (84, 4), (96, 18), (106, 32), (104, 52),
                        (114, 66), (112, 88), (90, 92), (50, 96), (10, 92)])),
             L(outline([(56, -2), (86, 8), (104, 42), (110, 86), (66, 92)]), 'shade', 'b', False),
             strand([(-6, 60), (50, 54), (106, 60)], 'deep', 'b', 1.0)],
}

# Sirius Starsky: pelo azul petróleo alto y abultado hacia arriba en mechones de punta, con un mechón que le cae por la
# frente y una horquilla de estrella amarilla clara a un lado
CHARS['sirius-starsky'] = {
    'body': 'normal', 'pal': pal('#2a5a78', '#f6c8a0', iris='#1e1414', star='#f8eeb0'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 72), (10, 50), (4, 20), (6, -10, 1), (20, -2), (26, -30, 1), (40, -14), (50, -30, 1), (60, -14), (74, -30, 1), (80, -2), (96, -10, 1), (94, 20),
                         (90, 50), (84, 72), (80, 56), (20, 56)])),
              L(outline([(58, -14), (80, -2), (92, 30), (86, 66), (76, 40)]), 'shade', 'b', False),
              fringe([(14, 66), (16, 42), (28, 26), (40, 22), (46, 2), (54, 0), (58, 22), (72, 26), (84, 42), (86, 66), (76, 52), (62, 46), (56, 58), (50, 46), (44, 58),
                      (38, 46), (24, 52)]),
              L(outline([(76, 10), (79, 18), (88, 18), (81, 23), (84, 31), (76, 26), (68, 31), (71, 23), (64, 18), (73, 18)]), 'star', 'f', ln=True)],
    'side': [L(outline([(56, 58), (62, 46), (82, 46), (92, 30), (86, 8), (96, -16, 1), (74, -6), (60, -34, 1), (44, -14), (14, -24, 1), (20, -4), (4, 14), (0, 44), (8, 70),
                        (24, 80), (42, 72)])),
             L(outline([(4, 30), (24, 36), (26, 66), (8, 60)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 16), (96, 42), (92, 60, 1), (84, 44), (76, 32)])],
    'back': [L(outline([(16, 84), (8, 52), (4, 20), (8, -8, 1), (22, 0), (30, -26, 1), (44, -10), (52, -32, 1), (60, -10), (74, -26, 1), (80, 0), (94, -8, 1), (94, 20),
                        (92, 52), (84, 84), (50, 90)])),
             L(outline([(56, -10), (80, 0), (92, 30), (88, 80), (62, 86)]), 'shade', 'b', False),
             strand([(30, -10), (50, 20), (70, -10)], 'deep', 'b', 1.0)],
}

# Bucky Woodchuck: pelo azul marino corto y redondo con un tupé pequeño, orejas enormes, coloretes, pecas y dos paletas
CHARS['bucky-woodchuck'] = {
    'body': 'bajito', 'pal': pal('#2e3a6a', '#fcd0a0', iris='#1e1414', blush='#f49a8a'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'buck', 'mouth_y': 100, 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 5, 'ear_out': 10},
    'front': [L(outline([(16, 64), (12, 40), (20, 16), (38, 4), (56, 2), (78, 10), (90, 32), (88, 64), (82, 54), (78, 40), (60, 36), (44, 34), (30, 38), (22, 52)])),
              L(outline([(60, 4), (84, 14), (90, 40), (86, 60), (78, 34)]), 'shade', 'b', False),
              L(outline([(30, 30), (36, 16), (52, 8), (46, 22), (40, 36)]), 'mid', 'f', ln=True),
              L(ell(28, 92, 6, 4), 'blush', 'f', False), L(ell(72, 92, 6, 4), 'blush', 'f', False),
              L([(46, 84), (47, 85)], OUTC, 'f', False, False, 1.0), L([(52, 84), (53, 85)], OUTC, 'f', False, False, 1.0), L([(49, 87), (50, 88)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(16, 76), (8, 46), (14, 18), (36, 2), (62, 2), (84, 12), (92, 30), (80, 36), (60, 32), (50, 50), (44, 72), (28, 82)])),
             L(outline([(8, 46), (28, 44), (32, 76), (14, 72)]), 'shade', 'b', False),
             L(ell(84, 90, 5, 4), 'blush', 'f', False)],
    'back': [L(outline([(16, 80), (12, 40), (20, 16), (38, 4), (62, 4), (80, 16), (88, 40), (84, 80), (66, 88), (34, 88)])),
             L(outline([(56, 4), (80, 16), (88, 44), (84, 78), (62, 86)]), 'shade', 'b', False)],
}

# Punkie Mahican: cabeza rapada de cara redonda y una cresta mohicana verde oscura gruesa de la frente a la nuca; ojos
# redondos y sonrisa de gato
CHARS['punkie-mahican'] = {
    'body': 'bajito', 'pal': pal('#2a5a3a', '#f0b078', iris='#1e1414', shade='#1e4028'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'smile', 'mouth_y': 100, 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 1},
    'front': [L(blob(SKULL_F), 'skin'), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'skin_d', 'b', False),
              L(outline([(38, 50), (36, 10), (40, -20), (50, -26), (60, -20), (64, 10), (62, 50), (50, 56)]), 'mid', 'f'),
              L(outline([(52, -22), (60, -18), (62, 10), (60, 46), (54, 50)]), 'shade', 'f', False),
              L(outline([(46, -16), (50, -20), (50, 20), (46, 16)]), 'light', 'f', False)],
    'side': [L(outline([(-6, 60), (-10, 30), (4, 6), (26, -14), (56, -22), (82, -14), (100, 4), (92, 14), (70, 4), (46, 4), (24, 14), (8, 36), (4, 62)]))],
    'back': [L(blob(SKULL_B), 'skin'), L(blob([(56, 30), (80, 40), (80, 80), (62, 94)], 6), 'skin_d', 'b', False),
             L(outline([(38, 96), (36, 40), (38, 0), (44, -20), (56, -20), (62, 0), (64, 40), (62, 96), (50, 100)])),
             L(outline([(52, -18), (60, -10), (62, 40), (60, 94), (52, 96)]), 'shade', 'b', False)],
}

# Jagur Meister: piel morena, cabeza rapada con una cresta lila gruesa encima y dos franjas lila que bajan por las sienes
# hasta las cejas, y una trenza larga de tres nudos que cae por la nuca
CHARS['jagur-meister'] = {
    'body': 'normal', 'pal': pal('#6a6aa8', '#b07a4a', iris='#8a2a2a', shade='#4a4a88', light='#9a9ad0'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 100, 'hairline': False, 'big_ears': 2},
    'front': [L(blob(SKULL_F), 'skin'), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'skin_d', 'b', False),
              L(outline([(36, 24), (36, -6), (44, -18), (56, -18), (64, -6), (64, 24), (50, 30)]), 'mid', 'f'),
              L(outline([(52, -16), (62, -6), (62, 22), (54, 26)]), 'shade', 'f', False),
              L(outline([(36, 26), (22, 40), (20, 66), (28, 64), (28, 44), (42, 30)]), 'mid', 'f', ln=True),
              L(outline([(64, 26), (78, 40), (80, 66), (72, 64), (72, 44), (58, 30)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(20, 20), (24, 4), (44, -10), (70, -8), (86, 4), (88, 14), (70, 10), (44, 10), (26, 26)])),
             L(outline([(70, 12), (80, 30), (82, 50), (76, 50), (74, 30), (66, 18)]), 'mid', 'f', ln=True),
             L(ell(20, 30, 10, 11)), L(ell(12, 52, 10, 11)), L(ell(8, 76, 10, 11)), L(ell(4, 98, 8, 8)),
             L(ell(12, 52, 6, 6), 'shade', 'b', False), L(ell(8, 76, 6, 6), 'shade', 'b', False)],
    'back': [L(blob(SKULL_B), 'skin'), L(blob([(56, 30), (80, 40), (80, 80), (62, 94)], 6), 'skin_d', 'b', False),
             L(outline([(38, 30), (36, 4), (44, -10), (56, -10), (64, 4), (62, 30)])),
             L(ell(50, 44, 12, 12), 'mid', 'f', ln=True), L(ell(50, 70, 12, 13), 'mid', 'f', ln=True), L(ell(54, 96, 11, 12), 'mid', 'f', ln=True),
             L(ell(54, 70, 5, 6), 'shade', 'f', False), L(ell(58, 96, 5, 6), 'shade', 'f', False)],
}

# Friedrich Schiller: pelo verde muy oscuro de pinchos grandes hacia arriba y hacia atrás, con un mechón por la frente;
# cejas gruesas y ojos redondos decididos
CHARS['friedrich-schiller'] = {
    'body': 'normal', 'pal': pal('#16332a', '#fcd8b0', iris='#1e1414', light='#2e5a4a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 72), (2, 66, 1), (10, 52), (-6, 40, 1), (10, 30), (6, 4, 1), (24, 14), (28, -14, 1), (40, 4), (50, -24, 1), (60, 2), (72, -16, 1), (76, 10),
                         (94, 2, 1), (90, 26), (106, 38, 1), (92, 50), (98, 64, 1), (84, 72), (82, 56), (18, 56)])),
              L(outline([(58, 0), (80, 8), (94, 40), (88, 66), (78, 40)]), 'shade', 'b', False),
              fringe([(14, 62), (16, 40), (30, 24), (50, 20), (70, 24), (84, 40), (86, 62), (78, 50), (70, 44), (58, 46), (48, 62, 1), (44, 44), (32, 46), (24, 58, 1)])],
    'side': [L(outline([(56, 58), (62, 46), (82, 46), (90, 30), (86, 12), (100, 6, 1), (80, -6), (64, -30, 1), (50, -10), (20, -16, 1), (24, 2), (-6, 10, 1), (8, 24), (-10, 40, 1),
                        (8, 46), (0, 66, 1), (18, 66), (26, 82), (42, 70)])),
             L(outline([(6, 36), (24, 42), (24, 66), (8, 58)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 82), (2, 72, 1), (10, 56), (-8, 42, 1), (10, 32), (4, 6, 1), (24, 14), (28, -14, 1), (40, 4), (50, -24, 1), (60, 4), (72, -14, 1), (76, 14),
                        (96, 6, 1), (90, 32), (108, 42, 1), (90, 56), (98, 72, 1), (84, 82), (50, 90)])),
             L(outline([(56, 2), (80, 10), (94, 40), (88, 78), (62, 86)]), 'shade', 'b', False)],
}

# Adarn Shame (portero suplente): piel morena, pelo castaño claro verdoso con un pico a cada lado de lo alto como cuernos y
# un flequillo largo de lado que le tapa un ojo; mirada de sueño
CHARS['adarn-shame'] = {
    'body': 'normal', 'pal': pal('#9a8a5a', '#b07a4a', iris='#1e1414', shade='#7a6a42'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 100, 'face_front': WIDE_FACE, 'hairline': False},
    'front': [L(outline([(14, 70), (6, 50), (4, 26), (-4, -4, 1), (16, 8), (50, 0), (84, 8), (104, -4, 1), (96, 26), (94, 50), (86, 70), (82, 56), (18, 56)])),
              L(outline([(60, 2), (90, 4), (96, 40), (88, 64), (78, 36)]), 'shade', 'b', False),
              fringe([(12, 66), (12, 40), (26, 18), (50, 10), (74, 18), (88, 40), (90, 64), (86, 80), (76, 88, 1), (70, 72), (60, 64), (52, 52), (46, 44), (40, 58), (32, 46),
                      (22, 60)])],
    'side': [L(outline([(56, 58), (62, 46), (82, 46), (92, 30), (86, 10), (66, -2), (40, -12), (26, -24, 1), (24, -4), (8, 14), (2, 46), (10, 76), (14, 90, 1), (26, 80),
                        (42, 70)])),
             L(outline([(4, 34), (24, 40), (26, 70), (8, 64)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 16), (96, 42), (92, 70, 1), (84, 50), (76, 36)])],
    'back': [L(outline([(16, 84), (6, 52), (4, 26), (-4, -4, 1), (16, 8), (50, 0), (84, 8), (104, -4, 1), (96, 26), (94, 52), (84, 84), (66, 90), (58, 100, 1), (50, 90),
                        (42, 100, 1), (34, 90)])),
             L(outline([(56, 2), (90, 4), (96, 40), (90, 80), (62, 88)]), 'shade', 'b', False)],
}

# Ota Shape: carota ancha y sonriente de ojos cerrados de felicidad, cejas gruesas y una melena verde oliva oscura de rizos
# abultados por arriba y los lados
CHARS['ota-shape'] = {
    'body': 'corpulento', 'pal': pal('#3a4a14', '#fcdcb4', iris='#1e1414', shade='#2a360c', light='#5a6a2a'),
    'face': {'eyes': 'closed', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98, 'face_front': WIDE_FACE, 'hairline': False},
    'front': [L(outline([(8, 104), (-2, 90), (-8, 70), (0, 54), (-4, 34), (8, 16), (24, 2), (40, 4), (50, -4), (62, 2), (80, 2), (94, 16), (104, 34), (100, 54), (108, 70),
                         (102, 90), (92, 104), (90, 60), (10, 60)])),
              L(outline([(60, 2), (86, 10), (104, 40), (104, 96), (92, 98), (86, 44)]), 'shade', 'b', False),
              fringe([(6, 62), (10, 36), (24, 20), (40, 18), (50, 30), (60, 18), (76, 20), (90, 36), (94, 62), (84, 52), (72, 48), (60, 40), (50, 46), (40, 40), (28, 48),
                      (16, 52)]),
              L(outline([(28, 22), (40, 16), (34, 28)]), 'light', 'f', False)],
    'side': [L(outline([(54, 50), (62, 40), (84, 40), (90, 22), (80, 6), (60, -2), (36, -4), (14, 6), (-2, 24), (-14, 44), (-8, 60), (-16, 74), (-6, 94), (14, 102), (30, 92),
                        (42, 72)])),
             L(outline([(-8, 50), (16, 50), (24, 90), (0, 96)]), 'shade', 'b', False), L(outline([(20, 2), (44, -2), (32, 12)]), 'light', 'b', False)],
    'back': [L(outline([(2, 104), (-6, 86), (-12, 66), (-2, 50), (-6, 30), (8, 12), (26, 0), (50, -4), (74, 0), (92, 12), (106, 30), (102, 50), (112, 66), (106, 86), (98, 104),
                        (50, 110)])),
             L(outline([(56, -2), (86, 10), (104, 40), (108, 100), (70, 106)]), 'shade', 'b', False),
             strand([(-4, 62), (50, 58), (104, 62)], 'deep', 'b', 1.0), strand([(30, 96), (34, 104)], 'deep', 'b', 1.0), strand([(70, 96), (66, 104)], 'deep', 'b', 1.0)],
}

# Nogo Sarikid: pelo azul marino oscuro abundante y revuelto, de mechones redondeados que se abren a los lados y tapan
# las orejas; cejas gruesas y ojos verde agua
CHARS['nogo-sarikid'] = {
    'body': 'normal', 'pal': pal('#24324a', '#f6c8a0', iris='#2a9aa0', light='#3a4a68'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 86), (2, 82, 1), (6, 68), (-6, 58, 1), (4, 48), (-4, 30), (6, 10), (22, -2), (18, -14, 1), (36, -6), (50, -12), (64, -6), (82, -14, 1), (80, -2),
                         (96, 12), (104, 30), (96, 48), (106, 58, 1), (94, 68), (98, 82, 1), (88, 86), (84, 60), (16, 60)])),
              L(outline([(60, -4), (84, 4), (100, 32), (94, 78), (80, 44)]), 'shade', 'b', False),
              fringe([(12, 66), (12, 42), (24, 20), (50, 12), (74, 20), (88, 42), (88, 66), (80, 54), (74, 62, 1), (68, 48), (58, 56, 1), (54, 42), (44, 56, 1), (38, 44),
                      (28, 60, 1), (20, 52)])],
    'side': [L(outline([(56, 60), (60, 48), (82, 48), (94, 34), (90, 10), (76, -6), (54, -12), (30, -8), (10, 4), (-4, 26), (-10, 50), (-6, 74), (6, 90), (24, 92), (40, 80)])),
             L(outline([(-6, 40), (20, 44), (26, 84), (0, 84)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 16), (96, 42), (92, 62, 1), (84, 46), (76, 34)])],
    'back': [L(outline([(10, 92), (-6, 76), (-4, 56), (-8, 36), (4, 12), (20, -2), (50, -12), (80, -2), (96, 12), (108, 36), (104, 56), (106, 76), (90, 92), (70, 96), (50, 100),
                        (30, 96)])),
             L(outline([(56, -10), (84, 2), (102, 36), (100, 86), (66, 94)]), 'shade', 'b', False),
             strand([(10, 40), (30, 50)], 'deep', 'b', 1.0), strand([(90, 40), (70, 50)], 'deep', 'b', 1.0), strand([(30, 80), (50, 86), (70, 80)], 'deep', 'b', 1.0)],
}
