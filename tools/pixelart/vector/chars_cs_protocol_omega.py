"""Protocolo Omega (cs-protocol-omega): sus modelos 3D de Inazuma Eleven GO 2: Chrono Stone como referencia (busto de frente,
perfil y espalda). Todos llevan un micrófono negro de diadema pegado a la mejilla."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from heads import quad  # noqa: F401

MIC = (34, 32, 40, 255)
WHITE = (248, 248, 248, 255)


def mic(view):
    """El micrófono de Protocolo Omega: una cápsula negra en la mejilla (a la izquierda de la imagen de frente)."""
    if view == 'front':
        return [L([(20, 76), (23, 85)], MIC, 'f', False, False, 1.6), L(outline([(21, 84), (30, 87), (32, 93), (28, 96), (22, 92)]), MIC, 'f', ln=True)]
    if view == 'side':
        return [L([(50, 80), (60, 90)], MIC, 'f', False, False, 1.6), L(outline([(59, 88), (72, 90), (73, 97), (60, 97)]), MIC, 'f', ln=True)]
    return []


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


def po(spec):
    """Añade el micrófono a las tres vistas."""
    for v in ('front', 'side'):
        spec[v] = spec[v] + mic(v)
    return spec


# Hotel (Zanou, portero): pelo verde azulado oscuro en llamaradas hacia arriba, con dos mechones rizados que le caen junto a
# las orejas; una marca verde en V en la frente y ojos delineados en negro
CHARS['hotel'] = po({
    'body': 'normal', 'pal': pal('#1e6a7a', '#f4c494', iris='#7a1e1e', mark='#2a9aa0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 66), (6, 40), (0, 4, 1), (16, 14), (20, -24, 1), (34, 0), (44, -34, 1), (54, -4), (70, -30, 1), (72, 0), (90, -16, 1), (88, 14),
                         (102, 10, 1), (94, 40), (84, 66), (78, 52), (22, 52)])),
              L(outline([(58, -6), (80, 2), (94, 40), (84, 62), (74, 34)]), 'shade', 'b', False),
              L(outline([(40, -24), (46, -4), (40, 20)]), 'light', 'b', False),
              fringe([(14, 60), (16, 38), (30, 24), (50, 20), (70, 24), (84, 38), (86, 60), (76, 48), (66, 54, 1), (60, 44), (50, 52), (40, 44), (34, 54, 1), (24, 48)]),
              L(outline([(14, 60), (8, 76), (12, 96), (6, 102, 1), (18, 92), (20, 70)]), 'mid', 'f', ln=True),
              L(outline([(86, 60), (92, 76), (88, 96), (94, 102, 1), (82, 92), (80, 70)]), 'mid', 'f', ln=True),
              L(outline([(36, 58), (50, 70), (64, 58), (60, 64), (50, 74), (40, 64)]), 'mark', 'f', ln=True)],
    'side': [L(outline([(56, 56), (66, 44), (82, 44), (92, 30), (86, 4), (96, -10, 1), (72, -4), (66, -30, 1), (52, -6), (36, -26, 1), (32, 0), (6, -10, 1), (14, 18),
                        (-8, 26, 1), (8, 40), (-6, 56, 1), (12, 58), (6, 76, 1), (22, 72), (28, 86, 1), (38, 74), (48, 66)])),
             L(outline([(6, 36), (24, 42), (24, 70), (8, 60)]), 'shade', 'b', False),
             L(outline([(56, 60), (64, 78), (58, 98), (66, 104, 1), (52, 92), (50, 70)]), 'mid', 'f', ln=True),
             L(outline([(80, 60), (90, 62), (88, 68)]), 'mark', 'f', ln=True)],
    'back': [L(outline([(18, 80), (4, 70, 1), (10, 54), (-4, 40, 1), (12, 30), (8, 2, 1), (24, 12), (28, -22, 1), (40, 2), (50, -30, 1), (58, 0), (74, -24, 1),
                        (74, 6), (94, -6, 1), (90, 22), (106, 32, 1), (92, 46), (102, 64, 1), (86, 72), (84, 84), (50, 90)])),
             L(outline([(56, 0), (84, 14), (92, 50), (84, 80), (62, 86)]), 'shade', 'b', False),
             L(outline([(16, 70), (10, 86), (2, 98, 1), (18, 90), (24, 76)]), 'mid', 'f', ln=True),
             L(outline([(84, 70), (90, 86), (98, 98, 1), (82, 90), (76, 76)]), 'mid', 'f', ln=True)],
})

# Oscar (Medam): pelo corto rubio ceniza con una ancha franja granate que le cruza la cabeza en diagonal y dos mechones
# granates largos que le caen hasta los hombros, más una coleta larga por detrás; ojos violeta, perilla
CHARS['oscar'] = po({
    'body': 'normal', 'pal': pal('#d8d2ae', '#f8dcb0', iris='#7a3aa8', red='#b81e40', red_d='#8a1430'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 64), (12, 34), (24, 10), (50, 0), (76, 10), (88, 34), (86, 64), (80, 50), (20, 50)])),
              L(outline([(44, 2), (64, 0), (82, 14), (88, 36), (82, 50), (70, 30), (54, 16)]), 'red', 'b', ln=True),
              strand([(56, 8), (74, 24), (84, 44)], 'red_d', 'b', 1.0),
              L(outline([(14, 56), (8, 90), (12, 116, 1), (20, 100), (22, 64)]), 'red', 'f', ln=True),
              L(outline([(86, 56), (92, 90), (88, 116, 1), (80, 100), (78, 64)]), 'red', 'f', ln=True),
              L(outline([(46, 104), (54, 104), (52, 110), (48, 110)]), (200, 170, 120, 255), 'f', False)],
    'side': [L(outline([(54, 56), (62, 46), (80, 46), (92, 30), (84, 10), (62, 0), (34, 2), (14, 16), (8, 40), (14, 66), (32, 72), (46, 66)])),
             L(outline([(30, 4), (58, 0), (76, 8), (62, 18), (40, 30), (22, 26)]), 'red', 'b', ln=True),
             L(outline([(14, 26), (2, 50), (-4, 110), (6, 118, 1), (12, 92), (20, 50), (26, 30)]), 'red', 'b', ln=True),
             L(outline([(26, 22), (34, 16), (36, 26)]), 'red_d', 'b', ln=True),
             L(outline([(54, 56), (56, 90), (52, 112, 1), (48, 90), (46, 60)]), 'red', 'f', ln=True)],
    'back': [L(outline([(16, 74), (12, 34), (24, 10), (50, 0), (76, 10), (88, 34), (84, 74), (50, 82)])),
             L(outline([(36, 6), (64, 6), (68, 40), (66, 110), (56, 122, 1), (50, 110), (44, 122, 1), (34, 110), (32, 40)]), 'red', 'f', ln=True),
             L(ell(50, 30, 9, 8), 'red_d', 'f', ln=True), L(ell(50, 52, 7, 6), 'red_d', 'f', ln=True),
             L(outline([(12, 56), (8, 92), (12, 112, 1), (20, 96), (20, 64)]), 'red', 'f', ln=True),
             L(outline([(88, 56), (92, 92), (88, 112, 1), (80, 96), (80, 64)]), 'red', 'f', ln=True)],
})

# Echo (Quor): pelo en forma de casco redondo verde oliva claro, con la parte que enmarca la cara en negro hasta la
# mandíbula; ojos verdes rasgados y sonrisa con dientes
CHARS['echo'] = po({
    'body': 'normal', 'pal': pal('#c8c478', '#fae0b8', iris='#5a8a2a', inner='#3a3a3c', shade='#a89048'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 100), (4, 50), (14, 14), (50, -2), (86, 14), (96, 50), (90, 100), (80, 98), (80, 50), (20, 50), (20, 98)])),
              L(outline([(10, 100), (8, 54), (22, 30), (50, 22), (78, 30), (92, 54), (90, 100), (80, 100), (78, 52), (66, 36), (50, 32), (34, 36), (22, 52), (20, 100)]),
                'inner', 'f', ln=True)],
    'side': [L(outline([(68, 30), (88, 34), (94, 46), (82, 50), (66, 48), (60, 70), (64, 100), (52, 100), (20, 98), (6, 70), (8, 30), (30, 4), (60, 0)])),
             L(outline([(60, 30), (82, 32), (82, 46), (68, 44), (60, 60), (62, 100), (54, 100), (50, 60)]), 'inner', 'f', ln=True),
             L(outline([(10, 60), (34, 60), (40, 96), (20, 96)]), 'shade', 'b', False)],
    'back': [L(outline([(8, 82), (4, 44), (16, 12), (50, -2), (84, 12), (96, 44), (92, 82), (50, 92)])),
             L(outline([(8, 60), (50, 54), (92, 60), (92, 82), (50, 92), (8, 82)]), 'shade', 'b', False),
             L(outline([(70, 60), (88, 62), (86, 94), (74, 96)]), 'inner', 'f', ln=True)],
})

# Golf (Gaura): grandullón de cara de mono, con orejas enormes y una joya roja en la frente; gorro de pelo azul celeste
# con surcos y cinta verde, y detrás una cola de bolas de pelo gris azulado como rocas
CHARS['golf'] = po({
    'body': 'corpulento', 'pal': pal('#7ab8c8', '#e8c8a0', iris='#1e1e1e', band='#2a6a5a', rock='#8a8aa0', rock_d='#5a6a80', gem='#e84a4a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 100, 'hairline': False, 'big_ears': 6, 'ear_out': 8},
    'front': [L(ell(82, 30, 14, 12), 'rock'), L(ell(96, 52, 12, 11), 'rock_d'), L(ell(104, 76, 11, 10), 'rock'),
              L(outline([(18, 50), (16, 26), (30, 6), (50, -4), (70, 6), (84, 26), (82, 50)])),
              strand([(36, 4), (40, 30)], 'shade', 'b', 1.2), strand([(50, -2), (50, 30)], 'shade', 'b', 1.2), strand([(64, 4), (60, 30)], 'shade', 'b', 1.2),
              L(outline([(16, 54), (16, 42), (50, 36), (84, 42), (84, 54), (50, 48)]), 'band', 'f', ln=True),
              L(outline([(50, 60), (55, 65), (50, 70), (45, 65)]), 'gem', 'f', ln=True)],
    'side': [L(ell(10, 50, 14, 13), 'rock'), L(ell(-4, 76, 12, 11), 'rock_d'), L(ell(-2, 100, 11, 10), 'rock'),
             L(outline([(14, 50), (16, 24), (36, 4), (64, 2), (84, 18), (90, 40), (60, 40), (30, 48)])),
             L(outline([(14, 54), (18, 42), (60, 36), (92, 40), (92, 50), (58, 48), (26, 56)]), 'band', 'f', ln=True)],
    'back': [L(ell(30, 30, 16, 14), 'rock'), L(ell(70, 26, 16, 14), 'rock_d'), L(ell(50, 50, 18, 16), 'rock'),
             L(outline([(18, 50), (16, 26), (30, 6), (50, -4), (70, 6), (84, 26), (82, 50), (50, 60)])),
             L(outline([(16, 58), (16, 46), (50, 40), (84, 46), (84, 58), (50, 52)]), 'band', 'f', ln=True),
             L(ell(34, 72, 15, 13), 'rock', 'f', ln=True), L(ell(66, 70, 15, 13), 'rock_d', 'f', ln=True), L(ell(50, 92, 15, 13), 'rock', 'f', ln=True)],
})

# Charlie (Netan): pelo amarillo pálido en forma de cebolla, terminado en pico arriba, con flequillo recto; piel naranja y
# ojos redondos enormes de pasmo
CHARS['charlie'] = po({
    'body': 'normal', 'pal': pal('#eef0b4', '#e8a468', iris='#1e1e1e', shade='#c8b48a'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'line', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(14, 84), (6, 50), (14, 24), (36, 6), (50, -26, 1), (64, 6), (86, 24), (94, 50), (86, 84), (80, 60), (20, 60)])),
              L(outline([(58, 0), (84, 22), (92, 50), (84, 78), (76, 50)]), 'shade', 'b', False),
              strand([(50, -20), (40, 20), (30, 50)], 'shade', 'b', 1.0), strand([(50, -20), (60, 20), (70, 50)], 'shade', 'b', 1.0),
              fringe([(12, 68), (12, 40), (26, 26), (50, 20), (74, 26), (88, 40), (88, 68), (78, 62), (22, 62)])],
    'side': [L(outline([(54, 76), (58, 60), (84, 58), (94, 40), (86, 20), (64, 4), (54, -26, 1), (30, 4), (12, 20), (4, 50), (10, 80), (30, 92), (46, 88)])),
             L(outline([(4, 40), (30, 40), (40, 86), (12, 80)]), 'shade', 'b', False),
             fringe([(66, 20), (90, 30), (96, 50), (92, 62), (70, 58)])],
    'back': [L(outline([(14, 84), (6, 50), (14, 24), (36, 6), (50, -26, 1), (64, 6), (86, 24), (94, 50), (86, 84), (50, 96)])),
             L(outline([(14, 50), (50, 40), (90, 50), (88, 84), (50, 96), (14, 84)]), 'shade', 'b', False)],
})

# Lima (Quorth): melena larga y ondulada morado muy oscuro hasta los hombros, con mechones gruesos y un mechón que le tapa
# un ojo; ojos violeta y sonrisa
CHARS['lima'] = po({
    'body': 'normal', 'pal': pal('#2c2848', '#f2d2b0', iris='#7a5ac8'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 110), (-4, 100, 1), (0, 70), (-6, 40), (6, 14), (30, -2), (60, -4), (86, 8), (104, 36), (100, 70), (106, 100, 1), (88, 110),
                         (84, 66), (16, 66)])),
              L(outline([(60, 0), (86, 12), (100, 40), (98, 96), (86, 100), (82, 50)]), 'shade', 'b', False),
              fringe([(10, 76), (8, 44), (22, 22), (48, 12), (74, 18), (90, 40), (92, 76), (82, 60), (74, 72, 1), (66, 48), (54, 56), (46, 92, 1), (40, 70),
                      (36, 48), (24, 56), (16, 70)]),
              strand([(20, 30), (12, 70), (6, 100)], 'deep', 'b', 1.2), strand([(80, 30), (90, 70), (94, 100)], 'deep', 'b', 1.2)],
    'side': [L(outline([(54, 62), (60, 50), (82, 48), (94, 32), (86, 10), (60, -2), (32, 0), (10, 16), (0, 44), (-8, 80), (-4, 112, 1), (14, 98), (24, 112, 1), (30, 92),
                        (44, 80)])),
             L(outline([(0, 44), (24, 50), (30, 90), (6, 96)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 16), (96, 40), (92, 64, 1), (82, 48), (76, 60, 1), (70, 40)])],
    'back': [L(outline([(6, 108), (-6, 100, 1), (-2, 60), (6, 20), (30, 0), (70, 0), (94, 20), (102, 60), (106, 100, 1), (94, 108), (78, 114, 1), (64, 104),
                        (50, 116, 1), (36, 104), (22, 114, 1)])),
             L(outline([(56, 2), (90, 18), (100, 60), (96, 104), (66, 108)]), 'shade', 'b', False),
             strand([(30, 20), (24, 60), (28, 100)], 'deep', 'b', 1.2), strand([(70, 20), (76, 60), (72, 100)], 'deep', 'b', 1.2)],
})

# Bravo (Jini): cara redonda morena anaranjada metida en una enorme capucha de pelo crema mullido que le rodea toda la
# cabeza; una cinta en la frente y ojos pequeños de enfado
CHARS['bravo'] = po({
    'body': 'corpulento', 'pal': pal('#f0e4c0', '#c8703a', iris='#e0d040', shade='#d8c4a0', deep='#b8a080', band='#e8e0d8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False, 'ears': False},
    'front': [L(outline([(10, 116), (-12, 108, 1), (-6, 90), (-20, 70, 1), (-8, 54), (-16, 30, 1), (0, 22), (6, -2, 1), (24, 4), (36, -12, 1), (50, 0), (64, -12, 1),
                         (76, 4), (94, -2, 1), (100, 22), (116, 30, 1), (108, 54), (120, 70, 1), (106, 90), (112, 108, 1), (90, 116), (84, 108), (16, 108)])),
              L(outline([(64, -8), (94, 4), (108, 50), (106, 104), (90, 110), (88, 40)]), 'shade', 'b', False),
              L(outline([(16, 60), (14, 40), (30, 26), (50, 22), (70, 26), (86, 40), (84, 60)]), 'skin', 'f', False),
              L(outline([(18, 44), (30, 34), (50, 32), (70, 34), (82, 44), (80, 50), (50, 44), (20, 50)]), 'band', 'f', ln=True),
              L(ell(50, 84, 6, 4), (176, 90, 60, 255), 'f', False)],
    'side': [L(outline([(70, 112), (40, 118), (10, 110), (-12, 100, 1), (-8, 78), (-22, 60, 1), (-8, 46), (-14, 24, 1), (4, 18), (8, -6, 1), (30, 2), (44, -12, 1),
                        (58, 0), (78, 2), (94, 18), (100, 36), (84, 40), (70, 60), (72, 92), (84, 108)])),
             L(outline([(0, 40), (30, 40), (40, 100), (6, 100)]), 'shade', 'b', False),
             L(outline([(74, 30), (98, 30), (100, 40), (76, 40)]), 'band', 'f', ln=True)],
    'back': [L(outline([(12, 116), (-10, 106, 1), (-4, 86), (-18, 66, 1), (-6, 50), (-14, 28, 1), (2, 20), (8, -4, 1), (26, 4), (38, -12, 1), (50, 0), (62, -12, 1),
                        (74, 4), (92, -4, 1), (98, 20), (114, 28, 1), (106, 50), (118, 66, 1), (104, 86), (110, 106, 1), (88, 116), (50, 120)])),
             L(outline([(60, -6), (92, 4), (108, 56), (104, 108), (60, 116)]), 'shade', 'b', False)],
})

# India (Neira): casco blanco redondo con una franja negra a la altura de los ojos y una visera, del que salen a los
# lados dos alas de plumas rosa grisáceo
CHARS['india'] = po({
    'body': 'normal', 'pal': pal('#f4f2f0', '#f6d4b0', iris='#1e1e1e', shade='#d8d4d8', wing='#d8a8b0', wing_d='#b88890'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(14, 40), (-14, 20), (-26, 34, 1), (-14, 44), (-30, 56, 1), (-12, 62), (-20, 76, 1), (2, 74), (14, 66)]), 'wing'),
              L(outline([(86, 40), (114, 20), (126, 34, 1), (114, 44), (130, 56, 1), (112, 62), (120, 76, 1), (98, 74), (86, 66)]), 'wing'),
              strand([(-10, 40), (8, 52)], 'wing_d', 'b', 1.0), strand([(110, 40), (92, 52)], 'wing_d', 'b', 1.0),
              L(outline([(12, 86), (8, 40), (20, 10), (40, -14, 1), (50, 0), (60, -14, 1), (80, 10), (92, 40), (88, 86), (78, 78), (22, 78)])),
              L(outline([(62, 0), (82, 14), (92, 44), (88, 80), (80, 50)]), 'shade', 'b', False),
              L(outline([(10, 68), (12, 60), (50, 58), (88, 60), (90, 68), (50, 66)]), OUTC, 'f', False),
              L(outline([(14, 60), (16, 52), (50, 48), (84, 52), (86, 60), (50, 58)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(20, 40), (-12, 14), (-28, 24, 1), (-12, 36), (-30, 50, 1), (-10, 54), (-22, 70, 1), (2, 66), (14, 58)]), 'wing'),
             L(outline([(56, 84), (60, 72), (92, 66), (96, 50), (88, 20), (66, 0), (40, -2), (16, 14), (4, 44), (10, 80), (30, 96), (46, 94)])),
             L(outline([(60, 66), (96, 62), (96, 70), (60, 74)]), OUTC, 'f', False)],
    'back': [L(outline([(14, 40), (-14, 20), (-26, 34, 1), (-14, 44), (-30, 56, 1), (-12, 62), (-20, 76, 1), (2, 74), (14, 66)]), 'wing'),
             L(outline([(86, 40), (114, 20), (126, 34, 1), (114, 44), (130, 56, 1), (112, 62), (120, 76, 1), (98, 74), (86, 66)]), 'wing'),
             L(outline([(12, 86), (8, 40), (20, 10), (40, -14, 1), (50, 0), (60, -14, 1), (80, 10), (92, 40), (88, 86), (50, 94)])),
             L(outline([(56, 2), (82, 14), (92, 46), (88, 84), (62, 92)]), 'shade', 'b', False),
             strand([(50, 0), (50, 90)], 'shade', 'b', 1.0), L(outline([(10, 68), (50, 64), (90, 68), (90, 72), (50, 70), (10, 72)]), OUTC, 'f', False)],
})

# Beta: pelo verde agua claro con dos grandes bucles redondos encima de la cabeza y mechones largos que le caen a los lados
# hasta el pecho; ojos rosados y sonrisa con dientes
CHARS['beta'] = po({
    'body': 'chica', 'pal': pal('#7ab8b8', '#fcdcc4', iris='#b8306a', shade='#5a8a8c'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(ell(22, 6, 20, 18)), L(ell(78, 6, 20, 18)),
              L(outline([(14, 76), (6, 40), (18, 16), (50, 8), (82, 16), (94, 40), (86, 76), (80, 60), (20, 60)])),
              L(outline([(60, 0), (90, 10), (94, 44), (86, 70), (78, 40)]), 'shade', 'b', False),
              L(outline([(12, 60), (2, 90), (8, 118, 1), (18, 108), (24, 86), (20, 64)]), 'mid', 'f', ln=True),
              L(outline([(88, 60), (98, 90), (92, 118, 1), (82, 108), (76, 86), (80, 64)]), 'mid', 'f', ln=True),
              fringe([(12, 64), (14, 38), (28, 24), (50, 20), (72, 24), (86, 38), (88, 64), (78, 50), (66, 58, 1), (60, 44), (50, 52), (40, 44), (34, 58, 1),
                      (22, 50)])],
    'side': [L(ell(40, -2, 18, 18)),
             L(outline([(54, 60), (60, 48), (82, 48), (94, 30), (84, 10), (60, 2), (34, 2), (12, 18), (4, 44), (8, 74), (28, 84), (46, 76)])),
             L(outline([(20, 60), (6, 84), (12, 116, 1), (26, 100), (34, 80), (34, 62)]), 'mid', 'b', ln=True),
             L(outline([(4, 34), (28, 40), (32, 74), (10, 70)]), 'shade', 'b', False),
             fringe([(64, 4), (88, 16), (96, 40), (90, 58, 1), (82, 44), (74, 32)])],
    'back': [L(ell(22, 8, 20, 18)), L(ell(78, 8, 20, 18)),
             L(outline([(10, 96), (4, 44), (16, 16), (50, 8), (84, 16), (96, 44), (90, 96), (70, 104), (50, 96), (30, 104)]), 'shade'),
             L(outline([(4, 44), (16, 16), (50, 8), (84, 16), (96, 44), (70, 40), (50, 48), (30, 40)]), 'mid', 'b', False)],
})

# Juliet (Leiser): melena larga naranja dorada peinada en mechones gruesos retorcidos hacia un lado, que le tapa un ojo y
# cae hasta la espalda; piel morena y ojo azul
CHARS['juliet'] = po({
    'body': 'normal', 'pal': pal('#f0a030', '#9a6440', iris='#2a9ad8', shade='#c87a1e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 116), (-4, 110, 1), (-4, 70), (2, 30), (20, 6), (50, -4), (78, 4), (96, 26), (100, 60), (94, 100), (84, 70), (16, 70)])),
              L(outline([(60, 2), (86, 14), (98, 50), (94, 96), (84, 60)]), 'shade', 'b', False),
              fringe([(0, 108), (0, 70), (8, 36), (26, 12), (56, 4), (80, 14), (94, 36), (88, 54), (74, 42), (64, 52), (58, 74), (48, 96), (32, 104), (18, 116, 1)]),
              strand([(30, 14), (14, 60), (8, 100)], 'shade', 'f', 1.2), strand([(56, 10), (36, 60), (24, 100)], 'shade', 'f', 1.2),
              strand([(78, 16), (60, 46), (52, 80)], 'shade', 'f', 1.2)],
    'side': [L(outline([(54, 62), (60, 50), (82, 48), (94, 32), (84, 8), (60, -2), (30, 0), (8, 18), (-4, 50), (-10, 100), (-2, 118, 1), (14, 104), (30, 110, 1),
                        (36, 90), (46, 76)])),
             strand([(60, 2), (30, 30), (6, 90)], 'shade', 'b', 1.4), strand([(80, 10), (50, 40), (24, 100)], 'shade', 'b', 1.4),
             fringe([(64, 2), (90, 16), (96, 40), (92, 64, 1), (82, 48), (72, 36)])],
    'back': [L(outline([(6, 112), (-6, 100, 1), (-4, 50), (10, 14), (40, -2), (70, 0), (92, 16), (104, 50), (104, 100), (92, 112), (50, 120)])),
             L(outline([(56, 2), (90, 18), (102, 60), (98, 108), (60, 116)]), 'shade', 'b', False),
             strand([(40, 4), (20, 50), (14, 100)], 'shade', 'b', 1.4), strand([(64, 4), (50, 60), (46, 110)], 'shade', 'b', 1.4),
             strand([(84, 14), (84, 60), (80, 104)], 'shade', 'b', 1.4)],
})

# Alpha: pelo malva rosado de casco con las puntas de los lados abiertas hacia fuera y abajo como alas, flequillo de
# mechones; ojos grises serios y orejas puntiagudas
CHARS['alpha'] = po({
    'body': 'normal', 'pal': pal('#a06878', '#fadcbc', iris='#6a6a6a', shade='#7a4a5a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(18, 76), (2, 70), (-14, 82, 1), (-8, 62), (-2, 40), (8, 14), (30, 0), (62, 0), (86, 10), (100, 34), (106, 60), (114, 82, 1), (98, 72),
                         (84, 76), (80, 56), (20, 56)])),
              L(outline([(60, 2), (88, 14), (102, 50), (100, 70), (82, 46)]), 'shade', 'b', False),
              fringe([(14, 62), (16, 38), (30, 20), (52, 14), (74, 20), (86, 38), (88, 62), (78, 50), (72, 60, 1), (64, 44), (54, 54, 1), (48, 40), (40, 56, 1),
                      (34, 42), (24, 56, 1)])],
    'side': [L(outline([(56, 60), (60, 48), (82, 48), (94, 32), (86, 8), (60, -2), (30, 2), (8, 22), (-4, 54), (-18, 76, 1), (6, 70), (22, 82), (40, 76)])),
             L(outline([(0, 44), (26, 46), (30, 72), (6, 68)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 16), (96, 40), (92, 60, 1), (82, 46), (74, 34)])],
    'back': [L(outline([(18, 80), (0, 70), (-16, 82, 1), (-8, 58), (0, 30), (16, 8), (50, -2), (84, 8), (100, 30), (108, 58), (116, 82, 1), (100, 70), (82, 80),
                        (50, 86)])),
             L(outline([(56, 0), (88, 14), (104, 56), (98, 74), (66, 84)]), 'shade', 'b', False),
             strand([(50, 0), (50, 70)], 'deep', 'b', 1.0)],
})

# Mike (Einam): media melena castaño anaranjado lisa en casco, con flequillo de mechones finos y puntas hacia dentro a la
# altura de la barbilla; ojos grises
CHARS['mike'] = po({
    'body': 'normal', 'pal': pal('#c8843e', '#fcdcc0', iris='#7a7a90', shade='#9a5a2a'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 96), (2, 100, 1), (4, 80), (4, 40), (16, 12), (50, -2), (84, 12), (96, 40), (96, 80), (98, 100, 1), (86, 96), (82, 60), (18, 60)])),
              L(outline([(60, 0), (86, 14), (96, 44), (94, 90), (84, 84), (82, 46)]), 'shade', 'b', False),
              fringe([(12, 72), (12, 40), (26, 20), (50, 12), (74, 20), (88, 40), (88, 72), (80, 56), (74, 64, 1), (66, 46), (58, 58, 1), (52, 42), (44, 58, 1),
                      (36, 44), (28, 60, 1), (20, 54)])],
    'side': [L(outline([(54, 62), (58, 50), (82, 48), (94, 32), (86, 10), (60, -2), (32, 0), (10, 16), (2, 44), (4, 80), (14, 96), (36, 100), (52, 98), (46, 80)])),
             L(outline([(4, 40), (28, 44), (34, 90), (12, 90)]), 'shade', 'b', False),
             fringe([(62, 2), (88, 16), (96, 40), (92, 60, 1), (82, 46), (72, 34)])],
    'back': [L(outline([(8, 96), (2, 60), (6, 30), (24, 6), (50, -2), (76, 6), (94, 30), (98, 60), (92, 96), (72, 90), (50, 96), (28, 90)])),
             L(outline([(56, 0), (86, 14), (98, 56), (90, 94), (66, 92)]), 'shade', 'b', False)],
})

# Uniform (Laszlo, portero): pelo negro corto con una pieza gris azulada en forma de V en lo alto y patillas largas en pico
# que bajan por las mejillas; piel naranja y ceño fruncido
CHARS['uniform'] = po({
    'body': 'normal', 'pal': pal('#1e1e22', '#e8a060', iris='#6a3a1e', grey='#6a8088'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(16, 66), (10, 36), (12, 10), (2, -14, 1), (30, 4), (50, 10), (70, 4), (98, -14, 1), (88, 10), (90, 36), (84, 66), (78, 50), (22, 50)])),
              L(outline([(8, -8), (30, 6), (50, 34, 1), (70, 6), (92, -8), (76, 10), (50, 20), (24, 10)]), 'grey', 'f', ln=True),
              L(outline([(14, 50), (24, 46), (34, 52), (24, 60), (20, 92, 1), (16, 66)]), 'mid', 'f'),
              L(outline([(86, 50), (76, 46), (66, 52), (76, 60), (80, 92, 1), (84, 66)]), 'mid', 'f'),
              L(outline([(26, 46), (40, 40), (36, 50)]), 'mid', 'f'), L(outline([(74, 46), (60, 40), (64, 50)]), 'mid', 'f')],
    'side': [L(outline([(56, 56), (64, 44), (84, 40), (92, 20), (90, -8, 1), (68, 2), (40, -4), (16, 10), (6, 40), (10, 70), (24, 86), (40, 82), (50, 70)])),
             L(outline([(24, 4), (60, -6), (90, -8, 1), (70, 8), (40, 10)]), 'grey', 'f', ln=True),
             L(outline([(52, 52), (62, 54), (56, 90, 1), (50, 64)]), 'mid', 'f')],
    'back': [L(outline([(16, 76), (10, 36), (12, 10), (2, -14, 1), (30, 4), (50, 10), (70, 4), (98, -14, 1), (88, 10), (90, 36), (84, 76), (62, 90), (50, 100, 1),
                        (38, 90)])),
             L(outline([(10, -8), (30, 4), (50, 10), (70, 4), (90, -8), (74, 40), (60, 80), (50, 96, 1), (40, 80), (26, 40)]), 'grey', 'f', ln=True)],
})

# Tango (Cople): casco de pelo negro liso con una cinta rosa grisácea que le da la vuelta a la cabeza a media altura; la
# cara es una máscara de color crema con dos agujeros negros por ojos (pupilas naranjas)
CHARS['tango'] = po({
    'body': 'normal', 'pal': pal('#1e1e22', '#f0dcb4', iris='#e87a1e', band='#a88a90'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': [L(outline([(12, 80), (8, 40), (18, 12), (50, -2), (82, 12), (92, 40), (88, 80), (80, 50), (20, 50)])),
              L(outline([(60, 2), (84, 14), (92, 44), (88, 76), (80, 46)]), 'shade', 'b', False),
              L(outline([(18, 50), (34, 38), (50, 36), (66, 38), (82, 50), (50, 46)]), 'mid', 'f'),
              L(outline([(8, 57), (9, 52), (91, 52), (92, 57)]), 'band', 'f', ln=True),
              L(ell(36, 78, 5, 5.4), OUTC, 'f', False), L(ell(64, 78, 5, 5.4), OUTC, 'f', False),
              L(ell(37, 79, 2, 2.4), 'iris', 'f', False), L(ell(65, 79, 2, 2.4), 'iris', 'f', False),
              L(quad((45, 98), (50, 94), (55, 98)), OUTC, 'f', False, False, 1.4)],
    'side': [L(outline([(56, 70), (60, 50), (82, 46), (92, 30), (84, 8), (60, -2), (30, 2), (10, 18), (4, 50), (10, 84), (30, 96), (46, 90)])),
             L(outline([(6, 57), (7, 52), (94, 52), (95, 57)]), 'band', 'f', ln=True),
             L(ell(84, 76, 3.4, 5), OUTC, 'f', False), L(ell(85, 77, 1.4, 2), 'iris', 'f', False)],
    'back': [L(outline([(10, 84), (6, 40), (18, 12), (50, -2), (82, 12), (94, 40), (90, 84), (50, 94)])),
             L(outline([(56, 2), (84, 14), (94, 46), (88, 82), (62, 92)]), 'shade', 'b', False),
             L(outline([(6, 57), (7, 52), (93, 52), (94, 57)]), 'band', 'f', ln=True)],
})

# Zulu (Finik): pelo corto rubio claro en casco con flequillo en pico sobre la frente y la nuca más oscura; piel morena y
# ojos grises enfadados
CHARS['zulu'] = po({
    'body': 'normal', 'pal': pal('#f4e0a0', '#a87048', iris='#8a8a8a', shade='#c88a5a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 74), (8, 40), (18, 12), (50, 0), (82, 12), (92, 40), (86, 74), (80, 56), (20, 56)])),
              L(outline([(60, 2), (84, 14), (92, 44), (86, 70), (78, 44)]), 'shade', 'b', False),
              fringe([(12, 62), (14, 36), (28, 20), (50, 14), (72, 20), (86, 36), (88, 62), (78, 52), (70, 46), (58, 50), (50, 66, 1), (42, 50), (30, 46), (22, 52)])],
    'side': [L(outline([(54, 58), (58, 46), (82, 44), (92, 28), (84, 8), (60, 0), (32, 2), (12, 18), (6, 46), (10, 76), (24, 86), (40, 80)])),
             L(outline([(6, 40), (30, 40), (34, 82), (12, 80)]), 'shade', 'b', False),
             fringe([(62, 4), (88, 14), (94, 36), (90, 52, 1), (80, 42), (70, 32)])],
    'back': [L(outline([(12, 80), (6, 40), (18, 12), (50, 0), (82, 12), (94, 40), (88, 80), (50, 90)]), 'shade'),
             L(outline([(6, 40), (18, 12), (50, 0), (82, 12), (94, 40), (70, 36), (50, 44), (30, 36)]), 'mid', 'b', False)],
})

# X-Ray (Mechius): pelo granate liso y largo con raya en medio, que cae a los lados de la cara hasta el pecho; orejas muy
# grandes y ojos dorados redondos
CHARS['x-ray'] = po({
    'body': 'normal', 'pal': pal('#7a2a2e', '#fae2b4', iris='#a8901e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False, 'big_ears': 5, 'ear_out': 6},
    'front': [L(outline([(16, 112), (8, 80), (6, 40), (18, 12), (50, 0), (82, 12), (94, 40), (92, 80), (84, 112), (80, 60), (20, 60)])),
              L(outline([(60, 2), (84, 14), (94, 44), (90, 104), (82, 50)]), 'shade', 'b', False),
              fringe([(12, 70), (14, 40), (28, 20), (50, 12), (72, 20), (86, 40), (88, 70), (82, 58), (76, 70, 1), (68, 46), (56, 40), (52, 26), (48, 26), (44, 40),
                      (32, 46), (24, 70, 1), (18, 58)]),
              L(outline([(16, 64), (12, 110, 1), (20, 100), (24, 70)]), 'mid', 'f'), L(outline([(84, 64), (88, 110, 1), (80, 100), (76, 70)]), 'mid', 'f')],
    'side': [L(outline([(56, 60), (60, 48), (82, 46), (92, 30), (84, 8), (60, -2), (32, 0), (12, 16), (4, 46), (8, 84), (22, 100), (40, 98), (48, 80)])),
             L(outline([(4, 40), (28, 44), (34, 94), (12, 92)]), 'shade', 'b', False),
             fringe([(62, 2), (88, 14), (94, 38), (90, 66, 1), (84, 48), (78, 112, 1), (72, 60), (70, 36)])],
    'back': [L(outline([(16, 108), (8, 70), (6, 40), (18, 12), (50, 0), (82, 12), (94, 40), (92, 70), (84, 108), (50, 100)])),
             L(outline([(56, 2), (84, 14), (94, 46), (90, 100), (62, 100)]), 'shade', 'b', False),
             strand([(50, 2), (50, 96)], 'deep', 'b', 1.0)],
})
