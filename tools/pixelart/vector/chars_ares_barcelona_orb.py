"""Barcelona Orb (ares-barcelona-orb): sus modelos 3D de Inazuma Eleven Ares como referencia (busto de frente, perfil y espalda).
En Ares cada uno tiene una sola forma; ninguno coge por prefijo el dibujo de otro personaje."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars_bigwaves import rect_glasses
from heads import quad  # noqa: F401

WHITE = (248, 248, 248, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


def curls(cx, cy, r, n=8, a0=0.0):
    """Contorno de nube de rizos (bultos redondos alrededor de un centro)."""
    import math
    pts = []
    for i in range(n * 2):
        a = a0 + math.pi * 2 * i / (n * 2)
        k = 1.0 if i % 2 == 0 else 0.8
        pts.append((cx + r[0] * k * math.cos(a), cy + r[1] * k * math.sin(a)))
    return blob(pts, 6)


# Salvador Castell (Alonso Fibiano, portero): grandullón de cara redonda y mofletuda; una nube de rizos crema muy claros que
# le enmarca toda la cara y abulta a los lados como lana; ojos cerrados con dos círculos blancos encima y boca de gato
CHARS['salvador-castell'] = {
    'body': 'corpulento', 'pal': pal('#f4e8c4', '#f6c898', shade='#d8c49a', deep='#b8a07a'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'none', 'hairline': False, 'eye_y': 80},
    'front': [L(curls(10, 66, (16, 22), 6, 0.2)), L(curls(90, 66, (16, 22), 6, 0.5)), L(curls(50, 30, (54, 36), 10)),
              L(outline([(60, 0), (86, 12), (102, 40), (100, 80), (92, 92), (84, 56)]), 'shade', 'b', False),
              L(curls(50, 40, (36, 18), 7, 0.2), 'mid', 'f'), L(curls(48, 18, (10, 9), 4), 'light', 'f', False),
              strand([(26, 26), (30, 40)], 'deep', 'f', 1.0), strand([(74, 26), (70, 40)], 'deep', 'f', 1.0), strand([(44, 12), (40, 22), (48, 28)], 'deep', 'f', 1.0),
              L(ell(36, 72, 4.6, 4.6), WHITE, 'f', ln=True), L(ell(64, 72, 4.6, 4.6), WHITE, 'f', ln=True),
              L(quad((40, 96), (45, 100), (50, 96)) + quad((50, 96), (55, 100), (60, 96))[1:], OUTC, 'f', False, False, 1.6)],
    'side': [L(curls(22, 66, (24, 24), 7)), L(curls(42, 30, (50, 36), 10)),
             L(outline([(-2, 44), (26, 50), (34, 98), (8, 96)]), 'shade', 'b', False),
             L(curls(72, 30, (20, 16), 6, 0.4), 'mid', 'f'),
             L(ell(84, 72, 3.4, 3.4), WHITE, 'f', ln=True)],
    'back': [L(curls(16, 82, (18, 18), 5)), L(curls(84, 82, (18, 18), 5)), L(curls(50, 90, (26, 16), 6)), L(curls(50, 34, (54, 40), 9)),
             L(outline([(56, 2), (86, 10), (104, 40), (100, 92), (74, 100), (72, 50)]), 'shade', 'b', False),
             strand([(26, 30), (30, 54), (24, 80)], 'deep', 'b', 1.0), strand([(74, 30), (70, 54), (76, 80)], 'deep', 'b', 1.0)],
}

# Antoni Valls (Oscar Agito): pelo azul espeso y alborotado con un flequillo largo de mechones que le cae entre los ojos y
# dos mechones que se curvan hacia fuera a la altura de la barbilla; ojos grandes morados y sonrisa tranquila
CHARS['antoni-valls'] = {
    'body': 'normal', 'pal': pal('#1e66b8', '#fcdcbc', iris='#6a4ab0', shade='#16508e', deep='#0e3a6a'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 80), (4, 92), (2, 100), (12, 102), (20, 92), (18, 66), (82, 66), (80, 92), (88, 102), (98, 100), (96, 92), (88, 80), (96, 60),
                         (100, 30), (102, 18), (92, 14), (82, 4), (60, -6), (40, -6), (20, 2), (8, 12), (0, 16), (4, 26), (0, 54)])),
              L(outline([(60, -2), (84, 8), (98, 32), (94, 62), (84, 50)]), 'shade', 'b', False),
              fringe([(10, 70), (12, 40), (24, 18), (46, 10), (68, 14), (84, 28), (90, 52), (88, 68), (80, 56), (76, 66, 1), (70, 46), (60, 54, 1), (58, 40),
                      (50, 84, 1), (44, 50), (36, 64, 1), (30, 46), (20, 66, 1), (16, 54)]),
              L(outline([(56, 18), (76, 26), (84, 44), (72, 40)]), 'shade', 'f', False), strand([(30, 20), (24, 44)], 'deep', 'f', 1.0)],
    'side': [L(outline([(54, 64), (58, 50), (80, 46), (94, 32), (90, 10), (70, -4), (40, -6), (14, 6), (0, 30), (-2, 60), (4, 84), (0, 96), (10, 100), (22, 102),
                        (34, 92), (46, 78)])),
             L(outline([(0, 40), (24, 44), (30, 88), (8, 90)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 16), (96, 40), (94, 70, 1), (86, 52), (80, 62, 1), (76, 44), (64, 30)])],
    'back': [L(outline([(10, 84), (2, 96), (4, 104), (14, 104), (24, 94), (50, 98), (76, 94), (86, 104), (96, 104), (98, 96), (90, 84), (96, 56), (100, 30),
                        (102, 18), (92, 14), (82, 2), (60, -8), (40, -8), (18, 2), (8, 12), (0, 16), (2, 28), (2, 56)])),
             L(outline([(56, -4), (84, 8), (98, 34), (94, 84), (66, 94), (70, 40)]), 'shade', 'b', False),
             strand([(30, 20), (24, 50), (30, 84)], 'deep', 'b', 1.0), strand([(50, 4), (52, 90)], 'deep', 'b', 1.0), strand([(70, 20), (76, 50), (70, 84)], 'deep', 'b', 1.0)],
}

# Jordi Belloch (Federico Dazzlo): media melena gris pardo lisa con raya al lado, un flequillo largo que le tapa el ojo
# izquierdo de la imagen y las puntas abiertas hacia fuera a la altura de la mandíbula; ojo ámbar afilado
CHARS['jordi-belloch'] = {
    'body': 'normal', 'pal': pal('#b4a89c', '#fce0c8', iris='#c88a1e', shade='#8e8278', deep='#6e645c'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 92), (-4, 94, 1), (6, 80), (4, 50), (8, 24), (26, 6), (50, 0), (76, 6), (92, 24), (96, 50), (94, 80), (104, 94, 1), (90, 92), (84, 64),
                         (16, 64)])),
              L(outline([(60, 4), (86, 16), (96, 44), (94, 84), (84, 60)]), 'shade', 'b', False),
              fringe([(8, 92), (6, 56), (14, 28), (36, 12), (62, 12), (80, 22), (90, 40), (90, 66), (84, 54), (74, 44), (62, 46), (56, 62), (52, 90, 1), (44, 82),
                      (34, 96, 1), (24, 86), (16, 98, 1)]),
              strand([(30, 22), (22, 70)], 'shade', 'f', 1.2), strand([(48, 18), (42, 80)], 'shade', 'f', 1.0)],
    'side': [L(outline([(54, 62), (58, 48), (80, 46), (94, 32), (90, 10), (68, -2), (38, -2), (14, 10), (2, 34), (2, 66), (6, 86), (-4, 98, 1), (14, 92), (20, 104, 1),
                        (30, 90), (44, 80)])),
             L(outline([(2, 40), (26, 44), (32, 86), (10, 88)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 16), (96, 40), (94, 64, 1), (86, 50), (80, 58), (74, 40), (64, 30)])],
    'back': [L(outline([(8, 90), (-6, 96, 1), (4, 80), (2, 50), (8, 22), (26, 4), (50, -2), (74, 4), (92, 22), (98, 50), (96, 80), (106, 96, 1), (92, 90), (80, 98, 1),
                        (68, 88), (60, 100, 1), (50, 90), (40, 100, 1), (32, 88), (20, 98, 1)])),
             L(outline([(56, 2), (86, 16), (98, 48), (96, 90), (68, 92), (72, 48)]), 'shade', 'b', False)],
}

# Gerard Carbonell (Gregorio Jaballo): piel morena, pelo rubio muy pálido corto y despeinado de mechones en punta hacia
# los lados, gafas negras rectangulares y ojos azules afilados
CHARS['gerard-carbonell'] = {
    'body': 'normal', 'pal': pal('#ecd8b4', '#b47a50', iris='#4a8ac8', shade='#c8ac88', deep='#a08868'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 70), (-6, 66, 1), (6, 54), (-4, 40, 1), (8, 34), (6, 12, 1), (22, 16), (26, -4, 1), (40, 8), (50, -10, 1), (58, 6), (74, -6, 1),
                         (76, 12), (96, 8, 1), (92, 28), (106, 40, 1), (94, 52), (104, 66, 1), (86, 70), (84, 56), (16, 56)])),
              L(outline([(60, 4), (80, 6), (94, 36), (92, 60), (82, 42)]), 'shade', 'b', False),
              L(outline([(34, 6), (42, 4), (40, 22)]), 'light', 'b', False),
              fringe([(12, 64), (14, 40), (28, 22), (50, 16), (72, 22), (86, 40), (88, 64), (80, 52), (76, 62, 1), (70, 46), (62, 58, 1), (56, 42), (48, 62, 1),
                      (42, 44), (34, 58, 1), (28, 46), (20, 62, 1)]),
              strand([(30, 24), (24, 50)], 'deep', 'f', 1.0), strand([(70, 24), (76, 50)], 'deep', 'f', 1.0)] + rect_glasses('front', 77),
    'side': [L(outline([(56, 58), (62, 46), (80, 44), (92, 30), (90, 12), (104, 4, 1), (80, 2), (76, -14, 1), (60, 0), (44, -16, 1), (36, 2), (12, -6, 1), (16, 14),
                        (-8, 22, 1), (6, 34), (-10, 48, 1), (6, 54), (-2, 72, 1), (14, 70), (16, 86, 1), (30, 74), (46, 68)])),
             L(outline([(4, 34), (24, 40), (28, 70), (10, 66)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 16), (96, 40), (94, 60, 1), (86, 46), (80, 56, 1), (76, 40), (66, 30)]),
             L(ell(82, 77, 6, 6) + [ell(82, 77, 6, 6)[0]], OUTC, 'f', False, False, 1.4), L([(76, 76), (52, 72)], OUTC, 'f', False, False, 1.2)],
    'back': [L(outline([(14, 80), (-4, 76, 1), (6, 60), (-6, 44, 1), (8, 36), (6, 12, 1), (22, 16), (26, -4, 1), (40, 8), (50, -10, 1), (58, 6), (74, -6, 1),
                        (76, 12), (96, 8, 1), (92, 30), (108, 44, 1), (94, 58), (104, 76, 1), (86, 80), (72, 92, 1), (62, 82), (50, 94, 1), (38, 82), (28, 92, 1)])),
             L(outline([(56, 4), (82, 8), (96, 40), (92, 76), (66, 84)]), 'shade', 'b', False),
             strand([(30, 20), (36, 50), (30, 76)], 'deep', 'b', 1.0), strand([(70, 20), (64, 50), (70, 76)], 'deep', 'b', 1.0)],
}

# Carles Ripoll (Daniel Madrone): piel oscura, pelo lavanda esponjoso de rizos con mechones en punta arriba y rizos que le
# cuelgan a los lados de la cara y en la nuca; ojos grandes morados y pecas en la nariz
CHARS['carles-ripoll'] = {
    'body': 'normal', 'pal': pal('#a8a8e2', '#8a5a3a', iris='#8a6ab0', shade='#8282c0', deep='#6262a0', freck='#f0d0b0'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(curls(14, 82, (8, 10), 4)), L(curls(86, 82, (8, 10), 4)),
              L(outline([(10, 70), (-4, 60, 1), (6, 50), (4, 26), (16, 6), (20, -6, 1), (32, 2), (50, -4), (68, 2), (80, -8, 1), (84, 6), (96, 26), (94, 50), (104, 60, 1),
                         (90, 70), (84, 58), (16, 58)])),
              L(outline([(60, 0), (84, 8), (96, 30), (92, 62), (82, 44)]), 'shade', 'b', False),
              fringe([(10, 64), (12, 40), (24, 22), (44, 14), (62, 16), (80, 24), (88, 40), (90, 64), (82, 56), (74, 62, 1), (68, 48), (58, 56, 1), (54, 42), (46, 58, 1),
                      (40, 44), (32, 56, 1), (24, 46), (18, 60, 1)]),
              strand([(30, 26), (40, 22), (46, 30)], 'deep', 'f', 1.0), strand([(56, 24), (66, 20), (74, 28)], 'deep', 'f', 1.0),
              L(ell(46, 86, 1.0, 1.0), 'freck', 'f', False), L(ell(54, 86, 1.0, 1.0), 'freck', 'f', False), L(ell(50, 89, 1.0, 1.0), 'freck', 'f', False)],
    'side': [L(curls(30, 90, (10, 9), 4)), L(curls(14, 74, (8, 9), 4)),
             L(outline([(54, 58), (60, 46), (80, 44), (94, 30), (88, 10), (94, -6, 1), (74, 2), (60, -8, 1), (48, 0), (28, -2), (12, 10), (2, 30), (-10, 42, 1), (2, 50),
                        (0, 64), (18, 70), (34, 72), (44, 64)])),
             L(outline([(2, 34), (24, 40), (26, 66), (8, 62)]), 'shade', 'b', False),
             fringe([(66, 2), (88, 14), (96, 38), (92, 58, 1), (84, 46), (76, 34)])],
    'back': [L(curls(22, 92, (10, 9), 4)), L(curls(78, 92, (10, 9), 4)), L(curls(8, 76, (8, 9), 4)), L(curls(92, 76, (8, 9), 4)),
             L(outline([(12, 80), (-2, 66, 1), (6, 54), (4, 26), (16, 6), (20, -8, 1), (32, 2), (50, -6), (68, 2), (80, -10, 1), (84, 6), (96, 26), (94, 54), (104, 66, 1),
                        (88, 80), (50, 86)])),
             L(outline([(56, 0), (84, 8), (96, 34), (92, 74), (64, 82)]), 'shade', 'b', False)],
}

# Josep Anglesola (Rubérn Boigk): pelo negro azulado en pinchos larguísimos que salen hacia arriba y hacia los lados como
# una explosión, con la frente despejada y la línea del pelo en pico; ojos oscuros afilados y media sonrisa
CHARS['josep-anglesola'] = {
    'body': 'normal', 'pal': pal('#2c2a3a', '#fcdcbc', iris='#3a2420', shade='#1e1c28', deep='#121018'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98,
             'hairline': [(12, 64), (16, 44), (24, 32), (36, 30), (46, 22), (50, 26), (54, 22), (64, 30), (76, 32), (84, 44), (88, 64)]},
    'front': [L(outline([(14, 64), (8, 50), (-20, 40, 1), (2, 34), (-12, 16, 1), (12, 18), (4, -8, 1), (24, 6), (22, -30, 1), (38, -2), (46, -36, 1), (54, -4), (66, -32, 1),
                         (68, 0), (88, -14, 1), (84, 12), (110, 6, 1), (92, 28), (118, 38, 1), (92, 46), (86, 64), (80, 50), (20, 50)])),
              L(outline([(56, -10), (66, -26), (70, 0), (88, 8), (94, 36), (86, 56), (76, 30)]), 'shade', 'b', False),
              strand([(30, 30), (36, 8)], 'deep', 'b', 1.2), strand([(50, 24), (50, -10)], 'deep', 'b', 1.2), strand([(70, 30), (64, 8)], 'deep', 'b', 1.2)],
    'side': [L(outline([(58, 56), (66, 44), (80, 34), (92, 22), (104, 0, 1), (82, 8), (84, -20, 1), (64, -2), (58, -32, 1), (44, -6), (24, -24, 1), (24, 2), (-4, -8, 1),
                        (10, 16), (-16, 28, 1), (4, 34), (-14, 52, 1), (6, 56), (-4, 74, 1), (16, 70), (22, 84, 1), (34, 72), (46, 66)])),
             L(outline([(2, 34), (24, 40), (26, 66), (8, 60)]), 'shade', 'b', False)],
    'back': [L(outline([(18, 82), (8, 70), (-18, 58, 1), (4, 48), (-14, 24, 1), (10, 22), (2, -6, 1), (24, 6), (22, -30, 1), (38, -2), (46, -36, 1), (54, -4), (66, -32, 1),
                        (68, 0), (90, -12, 1), (84, 14), (112, 18, 1), (94, 34), (116, 54, 1), (94, 62), (84, 82), (60, 88), (50, 100, 1), (40, 88)])),
             L(outline([(56, -8), (66, -26), (70, 0), (90, 10), (98, 46), (86, 80), (62, 86)]), 'shade', 'b', False)],
}

# Xavi Casals (Trancy Cornet): pelo negro espeso y ondulado, revuelto, con dos picos que se levantan arriba y un mechón en
# la frente; dos lunares redondos en lugar de cejas, ojos enormes celeste y la boca abierta de sorpresa
CHARS['xavi-casals'] = {
    'body': 'normal', 'pal': pal('#363640', '#fce4cc', iris='#6ab0c8', shade='#26262e', deep='#18181e', blush='#f4b0a0'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': [L(outline([(10, 80), (2, 70), (6, 58), (0, 44), (8, 30), (6, 16), (22, 8), (26, -6, 1), (36, 4), (50, 0), (66, 2), (74, -8, 1), (78, 6), (94, 18), (94, 32),
                         (100, 46), (94, 58), (98, 70), (90, 80), (86, 62), (14, 62)])),
              L(outline([(60, 2), (84, 10), (96, 36), (92, 74), (82, 50)]), 'shade', 'b', False),
              fringe([(10, 66), (12, 40), (24, 22), (46, 14), (66, 16), (82, 26), (90, 44), (90, 66), (82, 56), (76, 62), (70, 50), (60, 54), (54, 44), (48, 50),
                      (44, 40), (36, 52), (26, 50), (18, 60)]),
              L(outline([(50, 30), (58, 40), (54, 52), (50, 42)]), 'skin', 'f', ln=True),
              L(ell(38, 62, 2.6, 2.2), OUTC, 'f', False), L(ell(62, 62, 2.6, 2.2), OUTC, 'f', False),
              L(ell(26, 88, 4, 2.4), 'blush', 'f', False), L(ell(74, 88, 4, 2.4), 'blush', 'f', False),
              L(outline([(46, 96), (54, 96), (52, 102), (48, 102)]), (150, 50, 50, 255), 'f', ln=True)],
    'side': [L(outline([(54, 62), (58, 50), (80, 48), (94, 34), (90, 12), (72, -2), (68, -12, 1), (60, -4), (40, -6), (18, 4), (8, 16), (-6, 14, 1), (2, 30), (-4, 48),
                        (2, 64), (-2, 80), (10, 90), (26, 90), (38, 82), (46, 72)])),
             L(outline([(2, 36), (24, 42), (28, 82), (8, 80)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 16), (96, 40), (92, 60), (84, 50), (76, 40)]),
             L(ell(86, 88, 3.4, 2.2), 'blush', 'f', False)],
    'back': [L(outline([(10, 86), (0, 74), (4, 58), (-2, 42), (6, 26), (8, 12), (22, 4), (28, -8, 1), (36, 2), (50, -2), (66, 0), (74, -10, 1), (78, 4), (94, 14), (96, 30),
                        (102, 46), (96, 60), (100, 76), (90, 88), (70, 94), (50, 90), (30, 94)])),
             L(outline([(56, 0), (84, 10), (98, 40), (96, 84), (66, 92), (70, 40)]), 'shade', 'b', False),
             strand([(24, 30), (30, 50), (22, 76)], 'deep', 'b', 1.0), strand([(76, 30), (70, 50), (78, 76)], 'deep', 'b', 1.0)],
}

# Ronaldo Ramallets (Donnell Gotti): piel morena oscura, pelo rubio pálido en una mata esponjosa alta arriba y a los lados
# de la cabeza, recogido en un moño redondo en la nuca; cejas rubias gruesas, ojos grandes redondos y sonrisa de dientes
CHARS['ronaldo-ramallets'] = {
    'body': 'normal', 'pal': pal('#f4eeb4', '#9a6038', iris='#2a1e1a', shade='#d8c890', deep='#b8a870'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(curls(50, 18, (40, 22), 7)),
              L(outline([(12, 70), (6, 50), (10, 30), (90, 30), (94, 50), (88, 70), (82, 52), (18, 52)])),
              L(outline([(60, 2), (84, 12), (92, 40), (88, 64), (80, 44)]), 'shade', 'b', False),
              fringe([(12, 48), (14, 34), (30, 30), (50, 32), (70, 30), (86, 34), (88, 48), (78, 42), (70, 46), (60, 40), (50, 46), (40, 40), (30, 46), (20, 42)]),
              L(outline([(28, 62), (44, 64), (42, 68), (30, 67)]), 'mid', 'f', ln=True), L(outline([(72, 62), (56, 64), (58, 68), (70, 67)]), 'mid', 'f', ln=True)],
    'side': [L(curls(8, 70, (14, 12), 5), 'light', 'b', ln=True),
             L(outline([(54, 56), (60, 44), (80, 40), (92, 26), (88, 4), (66, -6), (38, -6), (16, 4), (4, 22), (2, 40), (6, 56), (20, 66), (40, 64), (48, 60)])),
             L(outline([(4, 26), (40, 22), (70, 30), (90, 30), (88, 14), (60, 6), (30, 8)]), 'shade', 'b', False),
             L(outline([(70, 60), (84, 62), (82, 66), (72, 66)]), 'mid', 'f', ln=True)],
    'back': [L(curls(50, 18, (42, 22), 7)),
             L(outline([(12, 76), (6, 52), (10, 30), (90, 30), (94, 52), (88, 76), (50, 82)])),
             L(outline([(56, 24), (90, 32), (92, 70), (64, 80)]), 'shade', 'b', False),
             L(curls(50, 94, (15, 12), 5), 'light', 'f', ln=True)],
}

# Sergi Hernández (Clario Orvan): grandullón de cara ancha y mandíbula grande; pelo castaño corto y pegado, una cúpula baja
# con pinchos cortos echados hacia su izquierda (la derecha de la imagen) y un pico que le baja por la frente hasta las cejas;
# los lados cortos hasta lo alto de la oreja; raya negra gruesa alrededor de los ojos azules, rubor rojo y pendientes oscuros
RED = (214, 70, 60, 255)
CHARS['sergi-hern-ndez'] = {
    'body': 'corpulento', 'pal': pal('#7a5852', '#fcd0a8', iris='#4a7ab0', shade='#5e4440', deep='#463230'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 97, 'ear_out': 7,
             'hairline': [(12, 66), (18, 58), (24, 62), (28, 54), (38, 58), (44, 69), (48, 58), (58, 56), (68, 56), (74, 60), (78, 53), (88, 64)],
             'face_front': blob([(15, 52), (50, 44), (85, 52), (89, 76), (86, 100), (67, 112), (50, 114), (33, 112), (14, 100), (11, 76)])},
    'front': [L(outline([(17, 68), (11, 50), (13, 32), (22, 18), (34, 9), (38, -2, 1), (46, 6), (56, -6, 1), (60, 5), (78, 0, 1), (72, 12), (84, 20), (90, 36),
                         (89, 52), (84, 68), (70, 72), (50, 76), (30, 72)])),
              L(outline([(60, 5), (78, 0), (72, 12), (84, 20), (90, 36), (88, 54), (80, 40), (68, 24)]), 'shade', 'b', False),
              strand([(40, 8), (44, 22), (40, 34)], 'deep', 'b', 1.0), strand([(58, 6), (60, 20), (66, 30)], 'deep', 'b', 1.0),
              strand([(24, 30), (30, 44)], 'deep', 'b', 1.0),
              L(quad((22, 72), (30, 83), (44, 80)), OUTC, 'f', False, False, 3.4), L(quad((78, 72), (70, 83), (56, 80)), OUTC, 'f', False, False, 3.4),
              L([(19, 70), (25, 72)], OUTC, 'f', False, False, 2.8), L([(81, 70), (75, 72)], OUTC, 'f', False, False, 2.8),
              L([(30, 87), (33, 84)], RED, 'f', False, False, 1.2), L([(34, 88), (37, 85)], RED, 'f', False, False, 1.2),
              L([(70, 87), (67, 84)], RED, 'f', False, False, 1.2), L([(66, 88), (63, 85)], RED, 'f', False, False, 1.2),
              L(ell(9, 80, 1.6, 1.6), OUTC, 'f', False), L(ell(91, 80, 1.6, 1.6), OUTC, 'f', False)],
    'side': [L(outline([(78, 56), (82, 47), (94, 45, 1), (86, 38), (100, 28, 1), (88, 24), (96, 12, 1), (80, 12), (84, 0, 1), (68, 6), (62, -2, 1), (52, 8),
                        (36, 6), (18, 12), (6, 28), (2, 48), (6, 66), (14, 77), (26, 78), (36, 68), (44, 59), (56, 58), (66, 60), (72, 54)])),
             L(outline([(3, 46), (30, 50), (44, 58), (36, 68), (26, 78), (14, 77), (6, 66)]), 'shade', 'b', False),
             strand([(60, 10), (70, 22), (84, 26)], 'deep', 'b', 1.0), strand([(42, 12), (56, 24)], 'deep', 'b', 1.0),
             L(ell(46, 78, 1.5, 1.5), OUTC, 'f', False)],
    'back': [L(outline([(21, 82), (18, 60), (16, 36), (26, 18), (40, 9), (45, 4, 1), (52, 9), (60, 7, 1), (64, 12), (76, 18), (86, 34), (84, 60), (80, 82),
                        (66, 86), (50, 87), (34, 86)])),
             L(outline([(17, 56), (34, 62), (50, 63), (66, 62), (85, 56), (80, 82), (66, 86), (50, 87), (34, 86), (21, 82)]), 'shade', 'b', False),
             L(outline([(58, 8), (78, 20), (87, 40), (86, 56), (70, 50)]), 'shade', 'b', False)],
}

# Leo Segarra (Luther Fandam): pelo naranja rojizo en pinchos altos de punta hacia arriba, sobre los lados y la nuca
# rapados con tres rayas afeitadas; orejas grandes, ojos ámbar y el ceño fruncido
CHARS['leo-segarra'] = {
    'body': 'normal', 'pal': pal('#e8521e', '#fcdcbc', iris='#c89a1e', shade='#b83e16', deep='#8a2c10'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'big_ears': 3, 'ear_out': 4,
             'hairline': [(14, 54), (20, 44), (30, 52), (40, 40), (50, 50), (58, 40), (70, 52), (80, 44), (86, 54)]},
    'front': [L(outline([(16, 54), (12, 34), (4, 20, 1), (20, 18), (20, -4, 1), (34, 8), (38, -28, 1), (50, 0), (60, -14, 1), (64, 6), (82, 0, 1), (80, 20), (92, 26, 1),
                         (86, 34), (84, 54), (78, 44), (22, 44)])),
              L(outline([(56, -6), (62, -10), (66, 8), (82, 4), (80, 22), (86, 36), (80, 48), (72, 26)]), 'shade', 'b', False),
              L(outline([(36, 6), (42, -14), (48, 6)]), 'shade', 'b', False)],
    'side': [L(outline([(58, 48), (66, 40), (80, 36), (92, 24), (98, 6, 1), (82, 10), (86, -10, 1), (68, 4), (70, -28, 1), (54, -2), (36, -20, 1), (32, 6), (14, 4, 1),
                        (18, 20), (8, 30), (20, 40), (40, 42), (52, 44)])),
             L(outline([(18, 30), (40, 36), (36, 42), (20, 40)]), 'shade', 'b', False),
             L(quad((14, 58), (26, 52), (38, 56)), OUTC, 'f', False, False, 1.0), L(quad((14, 64), (26, 58), (38, 62)), OUTC, 'f', False, False, 1.0),
             L(quad((16, 70), (28, 64), (40, 68)), OUTC, 'f', False, False, 1.0)],
    'back': [L(outline([(16, 56), (12, 36), (6, 22, 1), (20, 20), (22, -2, 1), (34, 8), (40, -24, 1), (50, 2), (62, -12, 1), (64, 8), (82, 0, 1), (80, 22), (94, 26, 1),
                        (88, 36), (84, 56), (50, 60)])),
             L(outline([(56, 0), (82, 6), (88, 38), (82, 54), (62, 58)]), 'shade', 'b', False),
             L(quad((22, 66), (50, 60), (78, 66)), OUTC, 'f', False, False, 1.0), L(quad((22, 72), (50, 66), (78, 72)), OUTC, 'f', False, False, 1.0),
             L(quad((24, 78), (50, 72), (76, 78)), OUTC, 'f', False, False, 1.0)],
}

# Joan Asensi (Bergamo Regult): piel morena, pelo rosa salmón enorme y erizado en mechones gruesos que salen en todas
# direcciones, con dos mechones que le caen por la frente; ojos azules afilados y ceño fruncido
CHARS['joan-asensi'] = {
    'body': 'normal', 'pal': pal('#f2aa92', '#a46a44', iris='#4a7ac8', shade='#d48a74', deep='#b46a56'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 66), (-4, 58, 1), (4, 46), (-6, 32, 1), (6, 24), (2, 4, 1), (20, 8), (22, -14, 1), (36, -2), (44, -18, 1), (54, -4), (66, -16, 1), (70, 0),
                         (88, -6, 1), (86, 12), (104, 14, 1), (94, 28), (106, 42, 1), (94, 50), (102, 62, 1), (88, 66), (84, 54), (16, 54)])),
              L(outline([(58, -2), (84, 4), (96, 32), (92, 60), (80, 40)]), 'shade', 'b', False),
              strand([(26, 10), (32, 30)], 'deep', 'b', 1.0), strand([(48, 0), (50, 22)], 'deep', 'b', 1.0), strand([(74, 10), (68, 30)], 'deep', 'b', 1.0),
              fringe([(14, 58), (16, 42), (30, 32), (50, 30), (70, 32), (84, 42), (86, 58), (78, 50), (66, 46), (58, 60, 1), (54, 44), (46, 44), (42, 70, 1), (36, 48),
                      (24, 52)])],
    'side': [L(outline([(58, 56), (66, 46), (82, 44), (94, 30), (104, 18, 1), (86, 12), (92, -6, 1), (70, 2), (64, -16, 1), (50, -2), (30, -14, 1), (26, 6), (2, 2, 1),
                        (12, 22), (-12, 30, 1), (6, 40), (-10, 56, 1), (8, 60), (0, 78, 1), (18, 72), (24, 86, 1), (34, 72), (48, 64)])),
             L(outline([(2, 34), (24, 40), (26, 68), (6, 62)]), 'shade', 'b', False),
             fringe([(70, 6), (92, 20), (98, 42), (94, 60, 1), (86, 46), (78, 36)])],
    'back': [L(outline([(14, 80), (-4, 72, 1), (6, 58), (-8, 40, 1), (6, 30), (2, 6, 1), (20, 10), (22, -14, 1), (36, -2), (46, -18, 1), (56, -4), (66, -16, 1), (70, 0),
                        (90, -6, 1), (86, 14), (106, 18, 1), (94, 34), (108, 50, 1), (94, 58), (104, 74, 1), (86, 80), (68, 90, 1), (60, 80), (50, 92, 1), (40, 80),
                        (30, 90, 1)])),
             L(outline([(56, -2), (86, 6), (98, 40), (92, 76), (64, 82)]), 'shade', 'b', False),
             strand([(28, 20), (34, 50)], 'deep', 'b', 1.0), strand([(72, 20), (66, 50)], 'deep', 'b', 1.0)],
}

# Augusto Gómez (Agapito Goméz): pelo rojo peinado hacia arriba en un tupé con una coleta alta larguísima que cae por
# detrás, y mechones largos y finos que le cuelgan a los lados de la cara hasta el cuello; ojos amarillos y sonrisa
CHARS['augusto-gomez'] = {
    'body': 'normal', 'pal': pal('#d24c4c', '#fcdcbc', iris='#d8c01e', shade='#a83838', deep='#802828'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98,
             'hairline': [(12, 70), (14, 46), (26, 34), (40, 30), (50, 40), (60, 30), (74, 34), (86, 46), (88, 70)]},
    'front': [L(outline([(42, 0), (44, -18), (54, -26), (60, -16), (58, 2)])), L(outline([(44, -18), (58, -20), (58, -14), (46, -12)]), OUTC, 'f', False),
              L(outline([(12, 70), (8, 40), (18, 14), (36, 2), (50, 6), (64, 2), (82, 14), (92, 40), (88, 70), (82, 50), (18, 50)])),
              L(outline([(60, 4), (82, 14), (92, 40), (86, 60), (76, 34)]), 'shade', 'b', False),
              fringe([(40, 4), (50, 34), (62, 4), (70, 12), (54, 40), (46, 40), (30, 12)]),
              L(quad((14, 52), (4, 80), (2, 104)), 'mid', 'f', False, False, 3.0), L(quad((18, 54), (12, 82), (16, 100)), 'mid', 'f', False, False, 2.4),
              L(quad((86, 52), (96, 80), (98, 104)), 'mid', 'f', False, False, 3.0), L(quad((82, 54), (88, 82), (84, 100)), 'mid', 'f', False, False, 2.4)],
    'side': [L(outline([(40, 4), (24, -18), (2, -24), (-16, -12), (-24, 20), (-28, 70), (-24, 110, 1), (-14, 72), (-6, 40), (4, 20), (20, 10)])),
             L(outline([(54, 58), (60, 46), (80, 44), (94, 30), (90, 10), (70, -2), (40, -2), (18, 8), (6, 28), (6, 58), (16, 72), (30, 72), (44, 64)])),
             L(outline([(28, -10), (40, -14), (42, -6), (30, -2)]), OUTC, 'f', False),
             L(outline([(6, 32), (26, 38), (28, 66), (10, 62)]), 'shade', 'b', False),
             L(quad((54, 58), (58, 80), (54, 100)), 'mid', 'f', False, False, 3.0)],
    'back': [L(outline([(12, 74), (8, 40), (18, 14), (36, 2), (50, 6), (64, 2), (82, 14), (92, 40), (88, 74), (50, 80)])),
             L(outline([(40, 4), (44, -20), (56, -28), (62, -16), (62, 20), (64, 70), (58, 116, 1), (52, 80), (46, 116, 1), (40, 70), (38, 20)]), 'mid', 'f', ln=True),
             L(outline([(42, -6), (60, -6), (60, 0), (42, 0)]), OUTC, 'f', False),
             L(quad((12, 60), (6, 84), (8, 104)), 'mid', 'f', False, False, 3.0), L(quad((88, 60), (94, 84), (92, 104)), 'mid', 'f', False, False, 3.0),
             strand([(50, 20), (52, 110)], 'deep', 'f', 1.0)],
}

# Geraldo Enrique (Gerard Enrique): melena castaña larga y lisa con flequillo recto a la altura de las cejas, mechones largos
# junto a la cara y una coleta baja que le cae por la espalda; ojos grandes morados y un lunar bajo el ojo
CHARS['geraldo-enrique'] = {
    'body': 'chica', 'pal': pal('#8a6a5a', '#fce0c8', iris='#7a5ad8', shade='#6c5246', deep='#523c32'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 96), (4, 60), (6, 24), (22, 2), (50, -6), (78, 2), (94, 24), (96, 60), (90, 96), (84, 68), (16, 68)])),
              L(outline([(60, -2), (84, 8), (96, 36), (94, 90), (86, 60)]), 'shade', 'b', False),
              L(outline([(12, 64), (8, 110), (18, 98), (22, 70)]), 'mid', 'f'), L(outline([(88, 64), (92, 110), (82, 98), (78, 70)]), 'mid', 'f'),
              fringe([(10, 64), (10, 34), (24, 14), (50, 8), (76, 14), (90, 34), (90, 64), (82, 62), (80, 60), (70, 62), (66, 60), (58, 62), (54, 60), (46, 62), (42, 60),
                      (34, 62), (30, 60), (20, 62)]),
              strand([(34, 16), (30, 58)], 'deep', 'f', 1.0), strand([(50, 12), (50, 58)], 'deep', 'f', 1.0), strand([(66, 16), (70, 58)], 'deep', 'f', 1.0),
              L(ell(70, 86, 1.2, 1.2), OUTC, 'f', False)],
    'side': [L(outline([(52, 68), (56, 56), (78, 52), (92, 38), (88, 14), (66, -2), (36, -4), (14, 8), (2, 34), (2, 70), (10, 94), (0, 110), (-16, 124, 1), (8, 116),
                        (20, 96), (36, 90), (46, 84)])),
             L(outline([(2, 40), (24, 46), (30, 88), (8, 90)]), 'shade', 'b', False),
             fringe([(62, 4), (86, 16), (94, 40), (92, 60), (84, 58), (82, 104), (76, 104), (76, 62), (70, 42)])],
    'back': [L(outline([(10, 92), (4, 56), (6, 22), (22, 2), (50, -6), (78, 2), (94, 22), (96, 56), (90, 92), (70, 100), (50, 96), (30, 100)])),
             L(outline([(56, -2), (86, 8), (96, 40), (92, 92), (66, 96), (70, 40)]), 'shade', 'b', False),
             L(outline([(44, 92), (56, 92), (58, 110), (50, 124, 1), (42, 110)]), 'mid', 'f', ln=True),
             strand([(50, 4), (50, 90)], 'deep', 'b', 1.0)],
}

# Alessio Ganonti (Salomón Ganonti): hombre mayor de cara alargada, con un afro enorme castaño claro, cejas gruesas rubias,
# gafitas redondas y un bigote negro fino; ceño fruncido
CHARS['alessio-ganonti'] = {
    'body': 'delgado', 'pal': pal('#bca06e', '#fcd8b4', iris='#2a1e1a', shade='#8e7250', deep='#6e5638'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'frown', 'mouth_y': 102, 'hairline': False, 'glasses': (90, 90, 96, 255), 'eye_y': 80,
             'face_front': blob([(18, 56), (50, 50), (82, 56), (86, 80), (80, 104), (62, 116), (50, 118), (38, 116), (20, 104), (14, 80)])},
    'front': [L(curls(50, 30, (58, 38), 9)),
              L(outline([(60, -2), (88, 10), (106, 36), (100, 62), (84, 50)]), 'shade', 'b', False),
              L(outline([(26, 66), (44, 66), (42, 71), (28, 72)]), 'mid', 'f', ln=True), L(outline([(74, 66), (56, 66), (58, 71), (72, 72)]), 'mid', 'f', ln=True),
              L(outline([(38, 92), (50, 90), (62, 92), (60, 95), (50, 93), (40, 95)]), OUTC, 'f', False)],
    'side': [L(curls(40, 30, (52, 38), 9)),
             L(outline([(-6, 40), (30, 50), (40, 68), (6, 66)]), 'shade', 'b', False),
             L(outline([(76, 66), (88, 66), (86, 70), (76, 71)]), 'mid', 'f', ln=True),
             L(outline([(84, 92), (96, 90), (94, 94), (84, 95)]), OUTC, 'f', False)],
    'back': [L(curls(50, 32, (58, 40), 9)),
             L(outline([(56, -4), (90, 10), (108, 40), (100, 68), (70, 70)]), 'shade', 'b', False)],
}
