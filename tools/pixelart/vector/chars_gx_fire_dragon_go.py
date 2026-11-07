"""Dragones de Fuego (GO) (gx-fire-dragon-go): la selección de Corea de Galaxy, con sus modelos 3D de Inazuma Eleven GO
Galaxy como referencia (busto de frente, perfil y espalda, calcados sobre la rejilla de unidades de cabeza)."""
from chars import CHARS, L, OUTC, bumpy, ell, outline, pal, strand  # noqa: F401
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Nam Do-hyeon (portero): pelo granate corto con un flequillo largo que le cae en diagonal y le tapa el ojo izquierdo,
# unas puntas sueltas a los lados; ojos azules y media sonrisa
CHARS['do-hyeon-nam'] = {
    'body': 'normal', 'pal': pal('#7c3c3a', '#eeb486', iris='#4a7ac0', shade='#5e2a2a', deep='#4a2020'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 72), (12, 44), (0, 34, 1), (14, 30), (22, 10), (46, 0), (72, 4), (88, 20), (102, 22, 1), (92, 34), (90, 64), (84, 56), (20, 56)])),
              L(outline([(60, 4), (86, 18), (92, 44), (88, 62), (78, 40)]), 'shade', 'b', False),
              fringe([(12, 60), (14, 38), (28, 20), (50, 14), (72, 20), (86, 36), (90, 62), (86, 80), (78, 104, 1), (70, 84), (60, 62), (52, 48), (42, 54), (34, 46),
                      (24, 58, 1), (20, 50)]),
              L(outline([(56, 22), (80, 32), (86, 60), (78, 80), (70, 56)]), 'shade', 'f', False), strand([(46, 18), (64, 50), (76, 96)], 'deep', 'f', 1.0)],
    'side': [L(outline([(56, 62), (60, 50), (82, 48), (94, 34), (90, 12), (70, -2), (40, -4), (18, 6), (6, 28), (-6, 36, 1), (6, 46), (8, 70), (22, 84), (38, 80), (48, 72)])),
             L(outline([(8, 36), (28, 42), (30, 74), (12, 68)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 16), (98, 42), (98, 76, 1), (90, 56), (82, 46), (72, 32)])],
    'back': [L(outline([(16, 84), (12, 44), (2, 34, 1), (14, 28), (24, 8), (50, 0), (76, 8), (88, 26), (100, 28, 1), (90, 40), (88, 84), (66, 90), (50, 100, 1), (34, 90)])),
             L(outline([(56, 2), (82, 14), (92, 50), (88, 82), (62, 88)]), 'shade', 'b', False)],
}

# Choi Shin-jae: media melena gris azulada a capas y despuntada hasta la barbilla, con flequillo de mechones; ojos rosados con
# raya marcada y sonrisa tranquila
CHARS['shinjae-choi'] = {
    'body': 'normal', 'pal': pal('#8aa2b4', '#f6c494', iris='#a83a6a', shade='#6a7c8c', deep='#56646e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 104), (2, 110, 1), (4, 90), (-4, 76, 1), (4, 64), (6, 30), (22, 6), (50, -2), (78, 6), (94, 30), (96, 64), (104, 76, 1), (96, 90), (98, 110, 1),
                         (88, 104), (82, 66), (18, 66)])),
              L(outline([(60, 2), (86, 16), (96, 50), (94, 100), (84, 70)]), 'shade', 'b', False),
              fringe([(10, 72), (10, 40), (24, 18), (50, 10), (76, 18), (90, 40), (90, 72), (82, 58), (76, 66, 1), (70, 50), (62, 62, 1), (58, 46), (50, 64, 1), (44, 46),
                      (36, 62, 1), (30, 50), (22, 66, 1), (16, 56)]),
              L(outline([(14, 70), (10, 96), (8, 112, 1), (18, 96), (20, 74)]), 'mid', 'f'), L(outline([(86, 70), (90, 96), (92, 112, 1), (82, 96), (80, 74)]), 'shade', 'f')],
    'side': [L(outline([(54, 64), (58, 52), (80, 50), (94, 36), (90, 12), (66, -2), (36, -2), (14, 10), (2, 34), (-10, 46, 1), (2, 58), (-8, 80, 1), (6, 84), (4, 104, 1),
                        (18, 92), (24, 110, 1), (32, 92), (46, 84)])),
             L(outline([(2, 40), (26, 46), (32, 90), (8, 90)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 42), (96, 72, 1), (88, 56), (82, 66, 1), (78, 46), (66, 32)])],
    'back': [L(outline([(12, 100), (-2, 108, 1), (4, 84), (-6, 70, 1), (4, 60), (6, 30), (22, 6), (50, -2), (78, 6), (94, 30), (96, 60), (106, 70, 1), (96, 84), (102, 108, 1),
                        (86, 100), (72, 112, 1), (60, 100), (50, 114, 1), (40, 100), (28, 112, 1)])),
             L(outline([(56, 2), (86, 16), (98, 50), (96, 100), (66, 104), (70, 50)]), 'shade', 'b', False),
             strand([(36, 20), (30, 96)], 'deep', 'b', 1.0), strand([(64, 20), (70, 96)], 'deep', 'b', 1.0)],
}

# Bae Jeong-ho (noh-bae): casco de pelo crema claro en forma de seta, con el flequillo a mechones hasta las cejas y la nuca
# rapada; piel muy pálida, ojos rojos rasgados y sonrisa
CHARS['noh-bae'] = {
    'body': 'normal', 'pal': pal('#e8e4c2', '#fdf0e0', iris='#b01e1e', shade='#b8aa88', deep='#9a8e70', nape='#c8a890'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(8, 64), (-2, 50), (2, 24), (22, 2), (50, -4), (78, 2), (98, 24), (102, 50), (92, 64), (84, 58), (16, 58)])),
              L(outline([(60, 0), (88, 12), (100, 40), (94, 60), (84, 50)]), 'shade', 'b', False),
              fringe([(4, 58), (8, 32), (28, 16), (50, 12), (72, 16), (92, 32), (96, 58), (86, 50), (80, 62, 1), (72, 46), (64, 60, 1), (58, 44), (50, 62, 1), (42, 44),
                      (36, 60, 1), (28, 46), (20, 62, 1), (14, 50)]),
              L(outline([(56, 16), (82, 26), (92, 48), (78, 42)]), 'shade', 'f', False)],
    'side': [L(outline([(48, 72), (44, 56), (26, 58), (10, 70), (16, 86), (34, 88)]), 'nape'),
             L(outline([(58, 58), (66, 52), (88, 50), (102, 44), (100, 20), (80, 0), (50, -6), (22, 0), (2, 20), (-6, 50), (10, 58), (30, 56), (46, 58)])),
             L(outline([(-4, 44), (40, 48), (46, 58), (20, 60), (4, 56)]), 'shade', 'b', False),
             fringe([(70, 4), (94, 18), (102, 44), (96, 60, 1), (90, 48), (82, 40)])],
    'back': [L(outline([(14, 66), (86, 66), (82, 90), (50, 96), (18, 90)]), 'nape'),
             L(outline([(8, 66), (-2, 50), (2, 24), (22, 2), (50, -4), (78, 2), (98, 24), (102, 50), (92, 66), (50, 70)])),
             L(outline([(56, 0), (88, 12), (100, 40), (92, 64), (66, 68)]), 'shade', 'b', False)],
}

# Seo Young-jin: cresta de pinchos gris oscuro casi negro, alta y despeinada, con los lados rapados del mismo color; ojos
# negros de enfadado y boca apretada
CHARS['yongjin-seo'] = {
    'body': 'corpulento', 'pal': pal('#3c3e44', '#f2b47c', iris='#1e1414', shade='#2a2c30', deep='#1e2024', buzz='#4a4c52'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'hairline': [(16, 66), (20, 50), (34, 46), (50, 52), (66, 46), (80, 50), (84, 66)]},
    'front': [L(outline([(16, 70), (14, 40), (24, 22), (76, 22), (86, 40), (84, 70), (80, 56), (20, 56)]), 'buzz'),
              L(outline([(30, 40), (22, 10, 1), (36, 16), (36, -14, 1), (46, 4), (50, -30, 1), (56, 4), (64, -14, 1), (64, 16), (78, 10, 1), (70, 40), (58, 50), (50, 56, 1),
                         (42, 50)]), 'mid', 'f', ln=True),
              L(outline([(52, -20), (60, 0), (68, 20), (60, 44), (54, 20)]), 'shade', 'f', False)],
    'side': [L(outline([(56, 56), (62, 46), (84, 42), (90, 26), (80, 14), (40, 10), (12, 22), (6, 50), (16, 72), (34, 74), (46, 66)]), 'buzz'),
             L(outline([(24, 26), (10, 8, 1), (28, 8), (24, -16, 1), (40, 0), (46, -26, 1), (56, -2), (68, -20, 1), (70, 4), (88, -4, 1), (82, 14), (70, 26), (44, 30)]),
               'mid', 'f', ln=True)],
    'back': [L(outline([(16, 80), (14, 40), (24, 22), (76, 22), (86, 40), (84, 80), (50, 88)]), 'buzz'),
             L(outline([(40, 70), (34, 30), (26, 8, 1), (40, 12), (42, -14, 1), (50, 4), (58, -14, 1), (60, 12), (74, 8, 1), (66, 30), (60, 70), (50, 76)]), 'mid', 'f', ln=True)],
}

# Shin Woo-jin: pelo azul marino muy rizado y abultado, como una nube de bucles; ojos cerrados de risa y sonrisa
CHARS['ujin-shin'] = {
    'body': 'normal', 'pal': pal('#3c3c7c', '#fadcae', iris='#1e1414', shade='#2a2a5c', deep='#20204a'),
    'face': {'eyes': 'closed', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(bumpy(50, 30, 58, 42, 12, 0.1)),
              L(bumpy(66, 30, 34, 34, 8, 0.1), 'shade', 'b', False),
              fringe([(8, 64), (8, 40), (20, 22), (36, 14), (50, 18), (64, 14), (80, 22), (92, 40), (92, 64), (84, 52), (78, 60), (70, 50), (60, 58), (50, 48), (40, 58),
                      (30, 50), (22, 60), (16, 52)]),
              strand([(30, 10), (36, 20)], 'deep', 'f', 1.2), strand([(60, 6), (66, 18)], 'deep', 'f', 1.2), strand([(80, 26), (86, 38)], 'deep', 'f', 1.2)],
    'side': [L(bumpy(44, 32, 54, 44, 12, 0.1)),
             L(outline([(54, 64), (60, 50), (82, 48), (94, 36), (80, 30), (50, 40), (30, 70), (36, 80), (46, 72)]), 'mid', 'b', False),
             L(bumpy(28, 40, 30, 32, 8, 0.1), 'shade', 'b', False)],
    'back': [L(bumpy(50, 36, 58, 48, 12, 0.1)), L(bumpy(64, 40, 34, 40, 8, 0.1), 'shade', 'b', False),
             strand([(30, 20), (36, 30)], 'deep', 'b', 1.2), strand([(56, 40), (62, 50)], 'deep', 'b', 1.2), strand([(40, 60), (46, 70)], 'deep', 'b', 1.2)],
}

# Yang Gun-woo: pelo morado corto peinado hacia delante con un pico en el centro de la frente, los lados y la nuca rapados en
# lila más claro; ojos rasgados de enfadado
CHARS['gunwoo-yang'] = {
    'body': 'normal', 'pal': pal('#6a508c', '#fcdcbc', iris='#1e1414', shade='#544070', deep='#40305a', buzz='#a48cc4', buzz_d='#8a72aa'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 74), (12, 50), (88, 50), (84, 74), (80, 60), (20, 60)]), 'buzz'),
              L(outline([(12, 54), (12, 30), (24, 8), (50, 0), (76, 8), (88, 30), (88, 54), (80, 48), (72, 50), (64, 44), (50, 66, 1), (36, 44), (28, 50), (20, 48)])),
              L(outline([(60, 4), (84, 16), (88, 40), (76, 44), (64, 40)]), 'shade', 'b', False),
              strand([(36, 14), (40, 40)], 'deep', 'b', 1.0), strand([(64, 14), (60, 40)], 'deep', 'b', 1.0)],
    'side': [L(outline([(56, 62), (60, 50), (82, 48), (90, 36), (60, 36), (30, 40), (10, 48), (8, 70), (20, 86), (36, 84), (48, 74)]), 'buzz'),
             L(outline([(8, 46), (12, 18), (34, 2), (64, 0), (86, 12), (94, 30), (92, 42), (80, 38), (60, 34), (40, 44), (28, 34), (18, 46)])),
             L(outline([(10, 44), (26, 36), (40, 44), (24, 52)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 86), (10, 50), (90, 50), (86, 86), (50, 92)]), 'buzz'),
             L(outline([(56, 52), (88, 52), (86, 84), (60, 90)]), 'buzz_d', 'b', False),
             L(outline([(10, 54), (12, 28), (24, 8), (50, 0), (76, 8), (88, 28), (90, 54), (80, 50), (70, 58, 1), (60, 50), (50, 60, 1), (40, 50), (30, 58, 1), (20, 50)])),
             L(outline([(56, 2), (82, 12), (90, 40), (80, 50)]), 'shade', 'b', False)],
}

# Sung Ji-hoon: piel morena y pelo castaño rojizo oscuro con una cinta blanca rosada en la frente, una antena que sale de lo
# alto, mechones largos junto a las orejas y una trenza que le cae por la espalda; ojos blancos redondos de enfadado
CHARS['jihun-song'] = {
    'body': 'normal', 'pal': pal('#5c2c24', '#c88a52', iris='#1e1414', shade='#44201a', deep='#341812', band='#f2dcd8', band_d='#c8b0ac'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 86), (4, 96, 1), (8, 70), (8, 34), (22, 10), (50, 2), (78, 10), (92, 34), (92, 70), (96, 96, 1), (86, 86), (82, 62), (18, 62)])),
              L(quad((50, 4), (40, -14), (60, -24)), 'mid', 'b', False, False, 3.2),
              L(outline([(60, 6), (84, 18), (92, 50), (88, 80), (80, 50)]), 'shade', 'b', False),
              fringe([(10, 66), (12, 42), (26, 32), (50, 28), (74, 32), (88, 42), (90, 66), (82, 58), (76, 66, 1), (70, 50), (60, 60, 1), (56, 46), (50, 62, 1), (44, 46),
                      (40, 60, 1), (30, 50), (24, 66, 1), (18, 56)]),
              L(quad((12, 36), (50, 10), (88, 36)) + quad((88, 42), (50, 18), (12, 42))[1:], 'band', 'f', ln=True)],
    'side': [L(outline([(54, 62), (58, 50), (80, 48), (94, 34), (88, 12), (66, -2), (36, -2), (14, 12), (4, 40), (2, 76), (14, 92), (32, 90), (46, 76)])),
             L(quad((48, 0), (40, -16), (58, -24)), 'mid', 'b', False, False, 3.2),
             L(outline([(14, 70), (8, 92), (6, 120, 1), (16, 100), (24, 80)]), 'mid', 'b', ln=True),
             L(outline([(4, 40), (26, 46), (30, 84), (8, 82)]), 'shade', 'b', False),
             L(quad((30, 4), (70, 10), (94, 30)) + quad((94, 38), (68, 18), (32, 12))[1:], 'band', 'f', ln=True),
             fringe([(66, 4), (90, 18), (96, 42), (94, 62, 1), (86, 50), (78, 40)])],
    'back': [L(outline([(14, 84), (8, 50), (10, 28), (24, 8), (50, 0), (76, 8), (90, 28), (92, 50), (86, 84), (50, 92)])),
             L(quad((50, 2), (42, -14), (60, -24)), 'mid', 'b', False, False, 3.2),
             L(outline([(56, 4), (82, 14), (92, 46), (86, 80), (64, 88)]), 'shade', 'b', False),
             L(outline([(42, 84), (58, 84), (60, 104), (56, 124, 1), (50, 128), (44, 124, 1), (40, 104)]), 'mid', 'f', ln=True),
             strand([(42, 98), (58, 102)], 'deep', 'f', 1.2), strand([(42, 112), (58, 116)], 'deep', 'f', 1.2)],
}

# Byeon Min-seo (hwang): pelo rosa empolvado en casco con flequillo recto y dos coletas bajas a los lados atadas con lazos de
# plumas; coloretes, ojos negros rasgados y sonrisa pícara
CHARS['hwang'] = {
    'body': 'chica', 'pal': pal('#d8949e', '#fde0c4', iris='#1e1414', shade='#b8747e', deep='#9a5c66', tie='#c88a98', blush='#f4a8a0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False, 'big_ears': 2},
    'front': [L(outline([(16, 76), (12, 40), (22, 12), (50, 2), (78, 12), (88, 40), (84, 76), (80, 60), (20, 60)])),
              L(outline([(60, 6), (82, 18), (88, 44), (82, 66), (76, 40)]), 'shade', 'b', False),
              fringe([(14, 60), (14, 36), (28, 18), (50, 12), (72, 18), (86, 36), (86, 60), (80, 56), (72, 58), (64, 54), (56, 58), (48, 54), (40, 58), (32, 54), (24, 58),
                      (18, 54)]),
              L(outline([(14, 86), (2, 98), (0, 118, 1), (10, 106), (12, 120, 1), (18, 104), (22, 90)]), 'mid', 'f', ln=True),
              L(outline([(86, 86), (98, 98), (100, 118, 1), (90, 106), (88, 120, 1), (82, 104), (78, 90)]), 'mid', 'f', ln=True),
              L(ell(16, 86, 4.6, 4), 'tie', 'f', ln=True), L(ell(84, 86, 4.6, 4), 'tie', 'f', ln=True),
              L(ell(30, 90, 4.4, 2.4), 'blush', 'f', False), L(ell(70, 90, 4.4, 2.4), 'blush', 'f', False)],
    'side': [L(outline([(54, 62), (58, 50), (80, 48), (92, 36), (88, 12), (66, -2), (36, -2), (14, 12), (6, 40), (8, 66), (20, 80), (36, 80), (46, 72)])),
             L(outline([(18, 80), (4, 94), (-6, 116, 1), (6, 104), (6, 120, 1), (16, 102), (26, 88)]), 'mid', 'b', ln=True), L(ell(20, 82, 4.6, 4), 'tie', 'b', ln=True),
             L(outline([(6, 38), (26, 44), (30, 74), (12, 70)]), 'shade', 'b', False),
             fringe([(64, 4), (88, 16), (94, 40), (92, 56), (86, 54), (80, 40)]),
             L(ell(86, 88, 4, 2.4), 'blush', 'f', False)],
    'back': [L(outline([(16, 84), (12, 40), (22, 12), (50, 2), (78, 12), (88, 40), (84, 84), (50, 90)])),
             L(outline([(56, 6), (82, 18), (90, 46), (84, 80), (62, 86)]), 'shade', 'b', False),
             L(outline([(22, 84), (10, 98), (6, 118, 1), (16, 106), (18, 120, 1), (24, 104), (30, 90)]), 'mid', 'f', ln=True),
             L(outline([(78, 84), (90, 98), (94, 118, 1), (84, 106), (82, 120, 1), (76, 104), (70, 90)]), 'mid', 'f', ln=True),
             L(ell(24, 86, 4.6, 4), 'tie', 'f', ln=True), L(ell(76, 86, 4.6, 4), 'tie', 'f', ln=True)],
}

# Shim Seo-yeon: melena castaña larguísima, con un tupé alto recogido en lo alto del que sale una coleta que le cae por la
# espalda, la frente despejada con raya y mechones largos junto a la cara; ojos azules grandes y sonrisa
CHARS['soyeon-sim'] = {
    'body': 'chica', 'pal': pal('#9c7258', '#fde6cc', iris='#2a5ab0', shade='#7a5440', deep='#5e4030'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': [(14, 76), (16, 52), (30, 44), (50, 48), (70, 44), (84, 52), (86, 76)]},
    'front': [L(outline([(8, 118), (2, 80), (8, 40), (14, 18), (30, 2), (36, -18), (50, -24), (64, -18), (70, 2), (86, 18), (92, 40), (98, 80), (92, 118), (82, 96), (80, 66),
                         (20, 66), (18, 96)])),
              L(outline([(60, -16), (70, 4), (88, 22), (94, 60), (94, 110), (82, 90), (76, 40)]), 'shade', 'b', False),
              L(outline([(36, -16), (50, -22), (64, -16), (60, -6), (50, -10), (40, -6)]), 'deep', 'b', False),
              fringe([(14, 64), (8, 100), (10, 118, 1), (20, 100), (22, 66)]), fringe([(86, 64), (92, 100), (90, 118, 1), (80, 100), (78, 66)]),
              strand([(50, 0), (40, 40)], 'deep', 'b', 1.0), strand([(50, 0), (60, 40)], 'deep', 'b', 1.0)],
    'side': [L(outline([(56, 60), (62, 48), (82, 44), (92, 30), (84, 10), (62, 0), (50, -16), (30, -22), (14, -14), (0, 6), (-10, 50), (-14, 120, 1), (2, 118), (10, 70),
                        (20, 80), (36, 80), (48, 72)])),
             L(outline([(-6, 20), (8, 10), (12, 40), (4, 100), (-8, 110)]), 'shade', 'b', False),
             L(outline([(58, 46), (60, 70), (58, 110, 1), (54, 74), (52, 50)]), 'mid', 'f', ln=True),
             strand([(84, 14), (50, 6), (20, 14)], 'deep', 'b', 1.0)],
    'back': [L(outline([(8, 120), (2, 80), (8, 40), (14, 18), (30, 2), (36, -18), (50, -24), (64, -18), (70, 2), (86, 18), (92, 40), (98, 80), (92, 120), (50, 124)])),
             L(outline([(56, -20), (70, 2), (90, 30), (96, 118), (66, 120), (70, 40)]), 'shade', 'b', False),
             strand([(50, -20), (50, 120)], 'deep', 'b', 1.0), strand([(30, 30), (24, 116)], 'deep', 'b', 1.0), strand([(70, 30), (76, 116)], 'deep', 'b', 1.0)],
}

# Lee Choon-yoon (jun-yeong-lee): pelo verde oliva redondeado con flequillo de mechones, unas gafas negras gruesas de pasta y
# ojos amarillos; sonrisa
CHARS['jun-yeong-lee'] = {
    'body': 'normal', 'pal': pal('#7a8a3c', '#f6c898', iris='#c8b020', shade='#5e6c2c', deep='#4a5622'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 84), (6, 50), (8, 24), (26, 4), (50, -2), (74, 4), (92, 24), (94, 50), (88, 84), (82, 64), (18, 64)])),
              L(outline([(60, 2), (86, 16), (94, 46), (88, 78), (80, 50)]), 'shade', 'b', False),
              fringe([(10, 64), (10, 36), (24, 16), (50, 10), (76, 16), (90, 36), (90, 64), (82, 56), (76, 64, 1), (70, 52), (62, 62, 1), (58, 48), (50, 64, 1), (42, 48),
                      (38, 62, 1), (30, 52), (24, 64, 1), (18, 56)]),
              strand([(32, 18), (28, 40)], 'deep', 'f', 1.0), strand([(68, 18), (72, 40)], 'deep', 'f', 1.0),
              L([(22, 67), (45, 67), (45, 83), (23, 83), (22, 67)], OUTC, 'f', False, False, 3.0),
              L([(55, 67), (78, 67), (77, 83), (55, 83), (55, 67)], OUTC, 'f', False, False, 3.0),
              L([(45, 72), (55, 72)], OUTC, 'f', False, False, 2.6)],
    'side': [L(outline([(54, 66), (58, 52), (80, 50), (94, 36), (88, 12), (66, -2), (36, -2), (14, 10), (2, 36), (2, 70), (14, 86), (30, 88), (44, 80)])),
             L(outline([(2, 40), (26, 46), (30, 84), (8, 80)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 42), (94, 60, 1), (86, 48), (78, 38)]),
             L([(77, 68), (91, 68), (91, 83), (78, 83), (77, 68)], OUTC, 'f', False, False, 3.0),
             L([(76, 72), (50, 70)], OUTC, 'f', False, False, 2.6)],
    'back': [L(outline([(12, 86), (6, 50), (8, 24), (26, 4), (50, -2), (74, 4), (92, 24), (94, 50), (88, 86), (70, 92, 1), (50, 88), (30, 92, 1)])),
             L(outline([(56, 2), (86, 16), (94, 50), (88, 84), (64, 88)]), 'shade', 'b', False),
             L([(10, 70), (90, 70)], OUTC, 'f', False, False, 2.6)],
}

# Hwang Joon-ho (joo-won): pelo gris azulado repeinado hacia atrás en un tupé alto con un rizo que cae sobre la frente, la nuca
# rapada en gris pardo y dos mechones largos delante de las orejas; sombra oscura en los ojos y gesto serio
CHARS['joo-won'] = {
    'body': 'normal', 'pal': pal('#86a2b0', '#fadcc0', iris='#1e1414', shade='#6a7c88', deep='#4e5a62', buzz='#7a6e6e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'hairline': [(14, 66), (16, 50), (30, 44), (50, 46), (70, 44), (84, 50), (86, 66)]},
    'front': [L(outline([(16, 66), (12, 36), (20, 12), (40, -4), (60, -6), (80, 4), (90, 24), (88, 56), (84, 66), (80, 52), (20, 52)])),
              L(outline([(60, -2), (82, 8), (90, 30), (84, 56), (76, 32)]), 'shade', 'b', False),
              L(outline([(68, 30), (82, 32), (90, 46), (80, 44), (74, 40)]), 'mid', 'f', ln=True),
              L(outline([(14, 56), (10, 84), (14, 106, 1), (20, 86), (22, 60)]), 'mid', 'f', ln=True),
              L(outline([(86, 56), (90, 84), (86, 106, 1), (80, 86), (78, 60)]), 'mid', 'f', ln=True),
              L([(28, 69), (44, 67)], (80, 84, 96, 255), 'f', False, False, 1.6), L([(72, 69), (56, 67)], (80, 84, 96, 255), 'f', False, False, 1.6),
              strand([(30, 10), (40, 40)], 'deep', 'b', 1.0), strand([(50, 2), (56, 40)], 'deep', 'b', 1.0)],
    'side': [L(outline([(48, 76), (40, 64), (20, 66), (8, 80), (18, 92), (36, 90)]), 'buzz'),
             L(outline([(56, 56), (62, 46), (82, 42), (92, 28), (88, 6), (68, -10), (40, -10), (16, 0), (4, 24), (2, 60), (16, 66), (30, 60), (46, 62)])),
             L(outline([(4, 30), (24, 30), (30, 60), (8, 60)]), 'shade', 'b', False),
             L(outline([(58, 50), (60, 76), (58, 102, 1), (54, 78), (52, 52)]), 'mid', 'f', ln=True),
             strand([(88, 10), (50, -2), (14, 16)], 'deep', 'b', 1.0), strand([(90, 28), (50, 18), (6, 40)], 'deep', 'b', 1.0)],
    'back': [L(outline([(14, 66), (86, 66), (84, 90), (50, 96), (16, 90)]), 'buzz'),
             L(outline([(12, 70), (8, 36), (20, 10), (40, -4), (60, -6), (80, 4), (92, 30), (90, 70), (76, 64), (50, 74), (24, 64)])),
             L(outline([(56, -2), (82, 8), (92, 40), (88, 68), (70, 66)]), 'shade', 'b', False),
             strand([(36, 4), (40, 60)], 'deep', 'b', 1.0), strand([(64, 4), (60, 60)], 'deep', 'b', 1.0)],
}

# Choi Chang-soo de mayor (en Galaxy, ya adulto): pelo negro verdoso en un tupé enorme y esponjoso, con patillas largas que le
# bajan hasta la mandíbula; ojos cerrados y gesto tranquilo
CHARS['gx:changsu-choi'] = {
    'body': 'delgado', 'pal': pal('#2c383c', '#f2b882', iris='#1e1414', shade='#1e282c', deep='#141c1e'),
    'face': {'eyes': 'closed', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 100, 'hairline': [(14, 70), (18, 50), (32, 40), (50, 44), (68, 40), (82, 50), (86, 70)]},
    'front': [L(bumpy(50, 24, 60, 36, 11, 0.08)),
              L(outline([(4, 50), (2, 80), (10, 100), (18, 104), (20, 70), (16, 50)])), L(outline([(96, 50), (98, 80), (90, 100), (82, 104), (80, 70), (84, 50)])),
              L(bumpy(70, 26, 32, 28, 8, 0.08), 'shade', 'b', False),
              L(outline([(12, 60), (20, 60), (20, 104), (14, 100)]), 'mid', 'f'), L(outline([(88, 60), (80, 60), (80, 104), (86, 100)]), 'mid', 'f'),
              strand([(30, 4), (40, 14)], 'deep', 'b', 1.2), strand([(56, -4), (64, 8)], 'deep', 'b', 1.2)],
    'side': [L(bumpy(44, 26, 56, 40, 11, 0.08)),
             L(outline([(4, 50), (2, 84), (14, 100), (30, 96), (40, 80), (50, 64), (44, 50)])),
             L(outline([(54, 58), (60, 58), (62, 100), (56, 102)]), 'mid', 'f'),
             L(bumpy(26, 40, 26, 30, 8, 0.08), 'shade', 'b', False)],
    'back': [L(bumpy(50, 30, 60, 42, 11, 0.08)),
             L(outline([(4, 50), (2, 84), (16, 100), (50, 104), (84, 100), (98, 84), (96, 50)])),
             L(bumpy(66, 36, 34, 40, 8, 0.08), 'shade', 'b', False)],
}
