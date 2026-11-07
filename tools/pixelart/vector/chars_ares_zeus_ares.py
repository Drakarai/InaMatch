"""Instituto Zeus (Ares) (ares-zeus-ares): el Zeus de Ares (God Bull), con sus modelos 3D de Inazuma Eleven Ares
(アレスの天秤) en la enciclopedia. En Ares están rediseñados: todos van como 'ares:<id>' (los de IE1 siguen para el Zeus de
IE). Perseo (percy-hurst) no tiene modelo 3D: dibujado a partir de su retrato."""
from chars import CHARS, L, OUTC, ell, outline, pal, rope, strand  # noqa: F401
from heads import quad

A = 'ares'
WHITE = (248, 248, 248, 255)


def fr(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Posei Donji "DJ" (portero): enorme y de cara redonda morena, ojos blancos de enfado con una nariz chata y dientes
# apretados; rapado gris con una placa dorada plana en lo alto y rastas doradas gruesas que le caen por detrás
_dj_face = outline([(6, 50), (20, 30), (50, 24), (80, 30), (94, 50), (100, 80), (92, 104), (70, 118), (50, 120), (30, 118), (8, 104), (0, 80)])
CHARS[f'{A}:ross-siddon'] = {
    'body': 'corpulento', 'pal': pal('#5e5e64', '#9a6a46', iris='#1e1414', shade='#46464c', gold='#e0a024', gold_d='#b07818', skin_d='#7e5434', nose='#7e5434'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 100, 'nose': (50, 84, 4), 'hairline': False, 'face_front': _dj_face,
             'big_ears': 3, 'ear_out': 8},
    'front': [L(outline([(16, 40), (22, 24), (50, 18), (78, 24), (84, 40), (50, 34)]), 'mid', 'f', ln=True),
              L(outline([(28, 22), (32, 10), (68, 10), (72, 22), (50, 26)]), 'gold', 'f', ln=True),
              L(outline([(20, 30), (28, 24), (30, 32), (22, 36)]), 'gold', 'f', ln=True), L(outline([(80, 30), (72, 24), (70, 32), (78, 36)]), 'gold', 'f', ln=True),
              L(rope((8, 88), (-6, 100), (-14, 108), 7), 'gold', 'b'), L(rope((92, 88), (106, 100), (114, 108), 7), 'gold', 'b')],
    'side': [L(outline([(20, 30), (40, 18), (70, 20), (86, 40), (60, 40), (30, 50)]), 'mid', 'f', ln=True),
             L(outline([(36, 18), (40, 8), (64, 8), (68, 18)]), 'gold', 'f', ln=True),
             L(rope((30, 20), (6, 40), (-6, 80), 8), 'gold', 'b'), L(rope((34, 24), (14, 50), (6, 90), 8), 'gold', 'b'), L(rope((28, 28), (0, 56), (-14, 96), 7), 'gold', 'b')],
    'back': [L(outline([(10, 70), (12, 36), (30, 18), (50, 14), (70, 18), (88, 36), (90, 70), (50, 76)])),
             L(outline([(32, 16), (36, 4), (64, 4), (68, 16)]), 'gold', 'f', ln=True),
             L(rope((50, 14), (30, 40), (4, 70), 9), 'gold', 'f'), L(rope((50, 14), (70, 40), (96, 70), 9), 'gold', 'f'),
             L(rope((50, 14), (42, 50), (36, 96), 9), 'gold', 'f'), L(rope((50, 14), (58, 50), (64, 96), 9), 'gold', 'f'), L(rope((50, 14), (50, 60), (50, 110), 9), 'gold', 'f')],
}

# Aporo Hikaru: pelo verde oliva revuelto en pinchos cortos con un mechón levantado arriba, y una diadema gris; cicatrices
# en cruz en la frente y la mejilla; ojos verdes y media sonrisa
CHARS[f'{A}:apollo-light'] = {
    'body': 'normal', 'pal': pal('#6a6a24', '#fcdcbc', iris='#4a5a22', shade='#4c4c18', band='#aaaaae', scar='#a86a50'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 90), (0, 84, 1), (8, 70), (-6, 58, 1), (8, 50), (2, 30, 1), (14, 26), (14, 6), (30, -4), (44, -6), (48, -22, 1), (56, -6), (72, -2), (86, 8),
                         (94, 26), (106, 32, 1), (94, 46), (106, 58, 1), (94, 70), (100, 84, 1), (86, 90), (82, 64), (18, 64)])),
              L(outline([(60, -4), (84, 8), (96, 40), (92, 82), (82, 54)]), 'shade', 'b', False),
              fr([(12, 72), (10, 46), (20, 28), (40, 22), (60, 22), (80, 28), (90, 46), (88, 72), (80, 58), (74, 68, 1), (66, 48), (58, 58, 1), (54, 42), (48, 62, 1),
                  (42, 44), (32, 60, 1), (26, 48), (20, 70, 1)]),
              L(quad((12, 34), (50, 10), (88, 34)), 'band', 'f', False, False, 3.6),
              L([(30, 58), (36, 64)], 'scar', 'f', False, False, 1.2), L([(36, 58), (30, 64)], 'scar', 'f', False, False, 1.2),
              L([(64, 90), (72, 96)], 'scar', 'f', False, False, 1.2), L([(72, 90), (64, 96)], 'scar', 'f', False, False, 1.2)],
    'side': [L(outline([(56, 62), (60, 48), (82, 46), (94, 32), (90, 12), (98, 0, 1), (78, 0), (70, -20, 1), (58, -4), (40, -12, 1), (30, 4), (6, -2, 1), (12, 16),
                        (-12, 26, 1), (4, 38), (-14, 52, 1), (2, 58), (-8, 76, 1), (8, 78), (4, 96, 1), (18, 86), (24, 100, 1), (34, 86), (44, 76)])),
             L(outline([(0, 38), (24, 44), (28, 84), (6, 86)]), 'shade', 'b', False),
             L(quad((88, 30), (60, 8), (30, 10)), 'band', 'f', False, False, 3.6),
             fr([(66, 4), (90, 18), (96, 42), (94, 66, 1), (86, 50), (80, 62, 1), (76, 42), (66, 30)])],
    'back': [L(outline([(14, 94), (-2, 90, 1), (8, 74), (-8, 60, 1), (8, 50), (0, 30, 1), (14, 26), (14, 6), (30, -4), (44, -6), (50, -24, 1), (56, -6), (72, -2), (86, 8),
                        (96, 26), (108, 32, 1), (96, 48), (108, 60, 1), (96, 74), (102, 90, 1), (86, 94), (72, 104, 1), (60, 94), (50, 106, 1), (40, 94), (28, 104, 1)])),
             L(outline([(56, -4), (84, 8), (98, 44), (94, 90), (64, 96), (70, 50)]), 'shade', 'b', False),
             strand([(26, 30), (36, 50), (30, 80)], 'deep', 'b', 1.0), strand([(74, 30), (64, 50), (70, 80)], 'deep', 'b', 1.0)],
}

# Hadeno Tetsu: piel morena oscura, media melena lisa en casco gris lila que oscurece a morado en las puntas, con un mechón
# largo que le cae entre los ojos; ojos turquesa serios
CHARS[f'{A}:hadrian-diesel'] = {
    'body': 'normal', 'pal': pal('#a8b4d0', '#8a5a3a', iris='#2ab0b8', shade='#6a5a9a', deep='#4a3a78', low='#7a68b0'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'line', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 94), (4, 60), (6, 24), (24, 2), (50, -4), (76, 2), (94, 24), (96, 60), (88, 94), (82, 66), (18, 66)])),
              L(outline([(6, 60), (14, 94), (24, 90), (20, 62)]), 'low', 'f', False), L(outline([(94, 60), (86, 94), (76, 90), (80, 62)]), 'low', 'f', False),
              L(outline([(60, 2), (86, 14), (96, 44), (92, 88), (82, 56)]), 'shade', 'b', False),
              fr([(10, 80), (8, 40), (22, 14), (48, 6), (74, 12), (90, 36), (92, 80), (84, 64), (78, 48), (66, 40), (58, 60), (52, 86, 1), (46, 58), (38, 44), (28, 52),
                  (20, 80, 1)]),
              L(outline([(46, 58), (58, 60), (52, 86)]), 'low', 'f', False)],
    'side': [L(outline([(54, 64), (58, 50), (80, 48), (94, 34), (92, 12), (70, -4), (40, -6), (14, 4), (0, 30), (0, 70), (10, 96), (34, 96), (44, 82)])),
             L(outline([(0, 56), (10, 96), (34, 96), (40, 70), (20, 60)]), 'low', 'b', False),
             L(outline([(2, 34), (24, 40), (30, 86), (10, 88)]), 'shade', 'b', False),
             fr([(64, 2), (90, 16), (96, 42), (96, 70), (90, 86, 1), (84, 60), (78, 42), (64, 30)])],
    'back': [L(outline([(10, 96), (4, 60), (6, 24), (24, 2), (50, -4), (76, 2), (94, 24), (96, 60), (90, 96), (70, 104), (50, 100), (30, 104)])),
             L(outline([(4, 56), (96, 56), (90, 96), (70, 104), (50, 100), (30, 104), (10, 96)]), 'low', 'b', False),
             L(outline([(56, -2), (86, 14), (98, 44), (94, 70), (70, 60)]), 'shade', 'b', False)],
}

# Aresu Ran: pelo rojo teja peinado de lado con una melena que le cae por un lado tapándole un ojo, y recogido abajo en un
# moño bajo de lado; ojos violetas con ojeras y cara de aburrimiento
CHARS[f'{A}:lane-war'] = {
    'body': 'normal', 'pal': pal('#b83a1e', '#f2c8a0', iris='#6a5a8a', shade='#8a2814', band='#2a5aa8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(12, 86), (6, 50), (8, 20), (28, 2), (54, -4), (78, 4), (94, 24), (96, 56), (90, 84), (84, 64), (18, 64)])),
              L(outline([(60, 0), (86, 12), (96, 44), (90, 80), (82, 54)]), 'shade', 'b', False),
              L(ell(84, 96, 11, 10), 'mid', 'f', ln=True), L(ell(74, 92, 3, 3), 'band', 'f', ln=True),
              fr([(8, 96), (6, 50), (16, 18), (44, 6), (70, 10), (88, 30), (90, 60), (82, 48), (70, 40), (58, 44), (50, 60), (48, 92), (38, 104, 1), (30, 84), (18, 100, 1)])],
    'side': [L(outline([(54, 64), (58, 50), (80, 48), (94, 34), (92, 12), (68, -4), (38, -6), (14, 6), (2, 32), (2, 66), (14, 84), (34, 86), (44, 76)])),
             L(ell(20, 92, 12, 10), 'mid', 'b', ln=True), L(ell(8, 96, 8, 7), 'mid', 'b', ln=True), L(ell(32, 88, 3, 3), 'band', 'b', ln=True),
             L(outline([(2, 34), (24, 40), (30, 80), (10, 82)]), 'shade', 'b', False),
             fr([(62, 0), (88, 14), (96, 40), (96, 70), (92, 84, 1), (86, 60), (78, 40), (62, 28)])],
    'back': [L(outline([(10, 84), (6, 50), (8, 20), (28, 2), (54, -4), (78, 4), (94, 24), (96, 56), (90, 84), (50, 90)])),
             L(outline([(56, 0), (86, 12), (96, 46), (90, 82), (66, 88)]), 'shade', 'b', False),
             L(ell(50, 96, 14, 10), 'mid', 'f', ln=True), L(ell(36, 100, 8, 7), 'mid', 'f', ln=True), L(ell(62, 92, 3, 3), 'band', 'f', ln=True)],
}

# Deio Geki: cara de bruto morena y cuadrada, con pintura de guerra (tres rayas a cada lado de la boca), ojos entornados y
# una sonrisa enorme de dientes; pelo castaño en trenzas pegadas al cráneo de la frente a la nuca
CHARS[f'{A}:danny-wood'] = {
    'body': 'corpulento', 'pal': pal('#5a4632', '#d89a54', iris='#2a1e1a', shade='#3e3020', deep='#2a2016', paint='#8a7a6a', blue='#3a8ab0', nose='#b87a3a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'nose': (50, 84, 4), 'hairline': False, 'big_ears': 3, 'ear_out': 6,
             'face_front': outline([(12, 50), (50, 44), (88, 50), (92, 80), (86, 104), (66, 114), (34, 114), (14, 104), (8, 80)])},
    'front': [L(outline([(12, 56), (10, 30), (20, 6), (50, -6), (80, 6), (90, 30), (88, 56), (70, 48), (50, 50), (30, 48)])),
              strand([(30, 4), (24, 50)], 'deep', 'f', 2.6), strand([(42, -2), (40, 48)], 'deep', 'f', 2.6), strand([(58, -2), (60, 48)], 'deep', 'f', 2.6),
              strand([(70, 4), (76, 50)], 'deep', 'f', 2.6),
              L([(14, 88), (30, 88)], 'paint', 'f', False, False, 3), L([(14, 96), (30, 96)], 'paint', 'f', False, False, 3),
              L([(70, 88), (86, 88)], 'paint', 'f', False, False, 3), L([(70, 96), (86, 96)], 'paint', 'f', False, False, 3),
              L([(30, 80), (40, 82)], 'blue', 'f', False, False, 2), L([(60, 82), (70, 80)], 'blue', 'f', False, False, 2),
              L(outline([(32, 92), (68, 92), (62, 106), (50, 110), (38, 106)]), (120, 40, 40, 255), 'f', ln=True),
              L(outline([(34, 93), (66, 93), (64, 99), (36, 99)]), WHITE, 'f', False)],
    'side': [L(outline([(70, 40), (56, 4), (30, -6), (10, 8), (2, 40), (8, 70), (22, 80), (40, 76), (56, 60)])),
             strand([(60, 10), (20, 2), (4, 40)], 'deep', 'f', 2.6), strand([(66, 24), (30, 14), (10, 60)], 'deep', 'f', 2.6),
             L([(76, 90), (90, 90)], 'paint', 'f', False, False, 3), L([(76, 98), (90, 98)], 'paint', 'f', False, False, 3),
             L(outline([(80, 93), (94, 93), (92, 102), (82, 102)]), (120, 40, 40, 255), 'f', ln=True)],
    'back': [L(outline([(12, 80), (10, 30), (20, 6), (50, -6), (80, 6), (90, 30), (88, 80), (50, 86)])),
             strand([(22, 10), (20, 80)], 'deep', 'f', 2.8), strand([(36, -2), (36, 84)], 'deep', 'f', 2.8), strand([(50, -4), (50, 86)], 'deep', 'f', 2.8),
             strand([(64, -2), (64, 84)], 'deep', 'f', 2.8), strand([(78, 10), (80, 80)], 'deep', 'f', 2.8)],
}

# Arute Saneki: lleva una máscara blanca lisa de ojos vacíos y rasgos tallados que le tapa toda la cara; pelo verde oscuro
# peinado con raya en medio y abierto hacia los lados en mechones gruesos por encima de las orejas
CHARS[f'{A}:artie-mishman'] = {
    'body': 'normal', 'pal': pal('#2e5a48', '#f6d0ac', iris='#1e1a1a', shade='#1e4034', mask='#ece8e0', mask_d='#c8c0b4'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': [L(outline([(14, 70), (-2, 66, 1), (8, 56), (6, 26), (24, 4), (46, 0), (50, 8), (54, 0), (76, 4), (94, 26), (92, 56), (102, 66, 1), (86, 70), (80, 54),
                         (20, 54)])),
              L(outline([(60, 2), (86, 14), (94, 40), (88, 64), (80, 44)]), 'shade', 'b', False),
              L(outline([(18, 38), (50, 30), (82, 38), (86, 74), (80, 100), (64, 112), (50, 114), (36, 112), (20, 100), (14, 74)]), 'mask', 'f', ln=True),
              L(outline([(60, 36), (82, 40), (84, 80), (70, 104), (66, 70)]), 'mask_d', 'f', False),
              L(outline([(24, 66), (32, 60), (44, 64), (42, 74), (30, 74)]), OUTC, 'f', False), L(outline([(76, 66), (68, 60), (56, 64), (58, 74), (70, 74)]), OUTC, 'f', False),
              L(outline([(26, 66), (32, 62), (42, 65), (40, 72), (30, 72)]), 'mask', 'f', False), L(outline([(74, 66), (68, 62), (58, 65), (60, 72), (70, 72)]), 'mask', 'f', False),
              L([(44, 100), (56, 100)], OUTC, 'f', False, False, 1.2), L([(50, 40), (48, 56)], 'mask_d', 'f', False, False, 1.2)],
    'side': [L(outline([(54, 50), (66, 40), (86, 36), (92, 20), (76, 2), (50, -4), (24, 2), (4, 20), (-12, 34, 1), (4, 40), (-10, 56, 1), (10, 60), (4, 76, 1), (22, 74),
                        (36, 66)])),
             L(outline([(4, 30), (24, 36), (24, 64), (8, 66)]), 'shade', 'b', False),
             L(outline([(70, 36), (90, 40), (96, 76), (94, 100), (80, 112), (72, 100), (70, 60)]), 'mask', 'f', ln=True),
             L(outline([(82, 64), (92, 64), (92, 72), (82, 72)]), OUTC, 'f', False)],
    'back': [L(outline([(14, 84), (-4, 74, 1), (8, 62), (6, 26), (24, 4), (50, -2), (76, 4), (94, 26), (92, 62), (104, 74, 1), (86, 84), (70, 92, 1), (60, 84), (50, 92, 1),
                        (40, 84), (30, 92, 1)])),
             L(outline([(56, 0), (86, 14), (96, 44), (90, 80), (64, 84)]), 'shade', 'b', False)],
}

# Herume Matsuaki: calvo, de cabeza redonda, con una marca azul en lo alto, la cara pintada de payaso (nariz azul, boca y
# párpados granates) y una bufanda gris enorme alrededor del cuello
CHARS[f'{A}:arion-matlock'] = {
    'body': 'normal', 'pal': pal('#f6dcb4', '#f6dcb4', iris='#2a1e1a', blue='#3a6a80', paint='#8a3a2a', scarf='#9aa4ac', scarf_d='#6e787e', skin_d='#dcc09a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False, 'big_ears': 2, 'ear_out': 4},
    'front': [L(outline([(16, 72), (14, 30), (28, 6), (50, 0), (72, 6), (86, 30), (84, 72)]), 'skin'),
              L(outline([(60, 6), (84, 28), (84, 64), (72, 52)]), 'skin_d', 'b', False),
              L(outline([(56, 6), (70, 8), (68, 14), (60, 16), (62, 26), (56, 26)]), 'blue', 'f', ln=True),
              L(outline([(26, 76), (40, 68), (46, 80), (32, 82)]), 'paint', 'f', ln=True), L(outline([(74, 76), (60, 68), (54, 80), (68, 82)]), 'paint', 'f', ln=True),
              L(ell(36, 78, 2.4, 2.4), OUTC, 'f', False), L(ell(64, 78, 2.4, 2.4), OUTC, 'f', False),
              L(ell(50, 86, 5, 4), 'blue', 'f', ln=True),
              L(outline([(30, 92), (70, 92), (62, 104), (50, 108), (38, 104)]), 'paint', 'f', ln=True),
              L(outline([(4, 108), (14, 96), (34, 104), (50, 108), (66, 104), (86, 96), (96, 108), (92, 126), (50, 132), (8, 126)]), 'scarf', 'f', ln=True),
              L(outline([(50, 108), (66, 104), (86, 96), (96, 108), (90, 124), (60, 128)]), 'scarf_d', 'f', False)],
    'side': [L(outline([(70, 40), (60, 8), (34, -2), (12, 12), (4, 40), (8, 66), (22, 80), (42, 76), (56, 62)]), 'skin'),
             L(outline([(76, 74), (88, 72), (89, 80), (78, 82)]), 'paint', 'f', ln=True), L(ell(93, 87, 3.4, 3.4), 'blue', 'f', ln=True),
             L(outline([(0, 110), (20, 96), (50, 104), (82, 100), (96, 112), (88, 128), (40, 132), (6, 126)]), 'scarf', 'f', ln=True),
             L(rope((80, 112), (96, 124), (108, 130), 10), 'scarf', 'f')],
    'back': [L(outline([(16, 80), (14, 30), (28, 6), (50, 0), (72, 6), (86, 30), (84, 80), (50, 86)]), 'skin'),
             L(outline([(56, 6), (84, 28), (86, 76), (62, 82)]), 'skin_d', 'b', False),
             L(outline([(2, 108), (14, 94), (50, 102), (86, 94), (98, 108), (92, 128), (50, 132), (8, 128)]), 'scarf', 'f', ln=True),
             L(outline([(54, 104), (86, 96), (96, 110), (90, 126), (60, 128)]), 'scarf_d', 'f', False)],
}

# Atena Tomo: pelo rubio ceniza peinado hacia atrás con los lados rapados en gris, recogido en una coleta altísima en lo alto
# sujeta con una anilla azul; una cicatriz roja en la frente y la mejilla; ojos grises y media sonrisa
CHARS[f'{A}:wesley-knox'] = {
    'body': 'normal', 'pal': pal('#d8c890', '#fcdcbc', iris='#6a7080', shade='#b0a068', buzz='#8a8278', buzz_d='#6e665e', ring='#2a5a8a', scar='#b04030'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 70), (12, 40), (22, 18), (78, 18), (88, 40), (86, 70), (80, 58), (20, 58)]), 'buzz'),
              L(outline([(26, 50), (30, 20), (44, 4), (56, 4), (70, 20), (74, 50), (62, 36), (50, 30), (38, 36)])),
              L(outline([(44, 6), (40, -14), (44, -40), (56, -48), (62, -36), (56, -16), (56, 6)])),
              L(outline([(42, -12), (58, -12), (58, -4), (42, -4)]), 'ring', 'f', ln=True),
              L([(62, 40), (58, 54), (66, 66)], 'scar', 'f', False, False, 1.4), L([(62, 70), (68, 84), (64, 94)], 'scar', 'f', False, False, 1.4)],
    'side': [L(outline([(56, 56), (62, 44), (82, 42), (90, 26), (80, 8), (54, 0), (28, 4), (10, 18), (4, 44), (10, 70), (26, 80), (42, 74)]), 'buzz'),
             L(outline([(80, 20), (60, 6), (34, 6), (16, 16), (20, 30), (40, 20), (60, 18), (80, 30)])),
             L(outline([(40, 6), (30, -20), (16, -46), (-4, -60), (-14, -50), (6, -40), (20, -16), (28, 8)])),
             L(outline([(26, -10), (38, -16), (42, -6), (30, 0)]), 'ring', 'f', ln=True)],
    'back': [L(outline([(14, 80), (12, 40), (22, 18), (78, 18), (88, 40), (86, 80), (50, 86)]), 'buzz'),
             L(outline([(56, 20), (86, 40), (86, 78), (62, 84)]), 'buzz_d', 'b', False),
             L(outline([(28, 22), (40, 4), (60, 4), (72, 22), (60, 40), (50, 36), (40, 40)])),
             L(outline([(44, 8), (42, -20), (50, -50), (60, -40), (58, -18), (56, 8)]), 'mid', 'f', ln=True),
             L(outline([(42, -6), (58, -6), (58, 2), (42, 2)]), 'ring', 'f', ln=True)],
}

# Afuro Terumi (Aphrodi en Ares): melena larguísima y lisa rubio verdoso pálido, con un mechón cruzando la frente entre los
# ojos y una pequeña marca en la frente; ojos rojos y sonrisa confiada
CHARS[f'{A}:byron-love'] = {
    'body': 'normal', 'pal': pal('#dcd898', '#fcdcc0', iris='#c8301e', shade='#b0ac6c', deep='#8a8650'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(6, 130), (0, 90), (2, 40), (14, 10), (40, -4), (60, -4), (86, 10), (98, 40), (100, 90), (94, 130), (84, 124), (82, 64), (18, 64), (16, 124)])),
              L(outline([(60, 0), (86, 12), (98, 44), (98, 124), (86, 120), (80, 50)]), 'shade', 'b', False),
              fr([(10, 120), (8, 50), (18, 18), (44, 6), (68, 10), (86, 24), (92, 50), (90, 120), (82, 128, 1), (80, 64), (72, 42), (60, 34), (54, 56), (50, 84, 1), (46, 56),
                  (36, 40), (26, 54), (20, 70), (18, 128, 1)]),
              L(outline([(48, 22), (52, 22), (50, 28)]), 'shade', 'f', False)],
    'side': [L(outline([(54, 62), (58, 50), (80, 48), (94, 34), (90, 12), (66, -4), (36, -4), (12, 8), (0, 34), (-6, 80), (-4, 132), (24, 134), (30, 100), (40, 80)])),
             L(outline([(0, 40), (24, 44), (28, 128), (2, 128)]), 'shade', 'b', False),
             fr([(62, 2), (88, 16), (96, 42), (96, 100), (92, 130, 1), (84, 100), (78, 56), (64, 30)])],
    'back': [L(outline([(4, 134), (0, 90), (2, 40), (14, 10), (40, -4), (60, -4), (86, 10), (98, 40), (100, 90), (96, 134), (50, 138)])),
             L(outline([(56, 0), (86, 12), (98, 46), (98, 130), (66, 136), (70, 50)]), 'shade', 'b', False),
             strand([(30, 20), (24, 130)], 'deep', 'b', 1.0), strand([(70, 20), (76, 130)], 'deep', 'b', 1.0)],
}

# Demete Yutaka: un yelmo romano de metal gris que le tapa la cabeza hasta la nariz, con guardas a los lados de la cara y
# una cresta roja altísima encima; ojos grises con cejas pobladas
CHARS[f'{A}:jonas-demetrius'] = {
    'body': 'normal', 'pal': pal('#2e2a26', '#f6d0a8', iris='#6a6a7a', helm='#8e8e94', helm_d='#64646a', helm_l='#b4b4ba', crest='#b8301e', crest_d='#86200e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'hairline': False, 'ears': False},
    'front': [L(outline([(42, 4), (40, -36), (50, -42), (60, -36), (58, 4)]), 'crest', 'b', ln=True),
              L(outline([(8, 104), (4, 60), (8, 22), (26, 2), (50, -4), (74, 2), (92, 22), (96, 60), (92, 104), (80, 96), (82, 72), (70, 60), (58, 62), (54, 84),
                         (46, 84), (42, 62), (30, 60), (18, 72), (20, 96)]), 'helm', 'f', ln=True),
              L(outline([(60, 2), (88, 20), (94, 60), (88, 100), (82, 72), (72, 58)]), 'helm_d', 'f', False),
              L(outline([(22, 20), (40, 10), (36, 18)]), 'helm_l', 'f', False),
              L(outline([(40, 42), (50, 32), (60, 42), (50, 52)]), 'helm_d', 'f', ln=True), strand([(50, 36), (50, 50)], 'helm_l', 'f', 1.0)],
    'side': [L(outline([(52, 6), (30, -24), (10, -30), (-6, -16), (14, -18), (40, 2)]), 'crest', 'b', ln=True),
             L(outline([(76, 64), (90, 60), (94, 40), (84, 14), (60, 0), (34, 0), (12, 12), (0, 36), (2, 70), (14, 92), (30, 96), (38, 76), (56, 70), (64, 92),
                        (72, 100)]), 'helm', 'f', ln=True),
             L(outline([(4, 40), (30, 40), (34, 80), (14, 90)]), 'helm_d', 'f', False)],
    'back': [L(outline([(42, 6), (40, -36), (50, -42), (60, -36), (58, 6)]), 'crest', 'f', ln=True),
             L(outline([(8, 92), (4, 56), (8, 22), (26, 2), (50, -4), (74, 2), (92, 22), (96, 56), (92, 92), (70, 86), (50, 88), (30, 86)]), 'helm', 'f', ln=True),
             L(outline([(56, 0), (88, 18), (96, 56), (90, 90), (64, 86)]), 'helm_d', 'f', False),
             L(outline([(30, 86), (70, 86), (66, 98), (34, 98)]), 'mid', 'f', False)],
}

# Heruse Arisu (Perseo): pelo naranja claro revuelto en mechones cortos de punta, con flequillo que le cae sobre la frente;
# ojos azules y cara decidida (sin modelo 3D: dibujado a partir de su retrato)
CHARS[f'{A}:percy-hurst'] = {
    'body': 'normal', 'pal': pal('#e8a050', '#fcdcbc', iris='#2a7ac8', shade='#c07a30', light='#f6c890'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 80), (2, 74, 1), (8, 60), (0, 44, 1), (10, 38), (8, 16), (24, 2), (44, -6), (60, -2), (78, -10, 1), (80, 6), (94, 20), (102, 36, 1),
                         (92, 44), (100, 64, 1), (88, 66), (86, 80), (80, 60), (20, 60)])),
              L(outline([(60, 2), (84, 12), (94, 40), (88, 74), (80, 50)]), 'shade', 'b', False),
              fr([(12, 68), (12, 40), (24, 20), (46, 12), (66, 16), (82, 28), (90, 46), (88, 68), (80, 56), (74, 64, 1), (66, 48), (58, 58, 1), (54, 42), (48, 60, 1),
                  (42, 44), (32, 58, 1), (26, 46), (20, 64, 1)]),
              L(outline([(28, 22), (44, 16), (36, 28)]), 'light', 'f', False)],
    'side': [L(outline([(56, 60), (60, 48), (82, 46), (94, 32), (92, 12), (102, 2, 1), (80, 0), (74, -16, 1), (58, -4), (36, -12, 1), (30, 4), (8, 0, 1), (12, 18),
                        (-8, 30, 1), (4, 40), (-10, 56, 1), (4, 60), (0, 78, 1), (16, 74), (20, 88, 1), (32, 76), (44, 70)])),
             L(outline([(2, 36), (24, 42), (28, 72), (8, 72)]), 'shade', 'b', False),
             fr([(66, 4), (90, 18), (96, 42), (94, 64, 1), (86, 50), (80, 60, 1), (76, 42), (66, 30)])],
    'back': [L(outline([(14, 86), (0, 82, 1), (8, 66), (-2, 50, 1), (10, 42), (8, 16), (24, 2), (44, -6), (60, -2), (80, -12, 1), (82, 6), (96, 22), (104, 40, 1),
                        (92, 48), (102, 68, 1), (88, 74), (86, 86), (70, 96, 1), (60, 86), (50, 98, 1), (40, 86), (28, 96, 1)])),
             L(outline([(56, 2), (84, 12), (96, 44), (90, 82), (64, 88)]), 'shade', 'b', False)],
}

# Matsuzaka Kiyo: anciana bajita de cara redonda y sonriente, con arrugas y ojos de punto; pelo gris recogido atrás en un moño
CHARS[f'{A}:deirdre-staples'] = {
    'body': 'bajito', 'pal': pal('#9a9298', '#fcdcc4', iris='#1e1a1a', shade='#746c72', skin_d='#e8c0a4'),
    'face': {'eyes': 'dot', 'brows': True, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False,
             'face_front': outline([(10, 52), (50, 44), (90, 52), (96, 80), (88, 104), (66, 116), (50, 118), (34, 116), (12, 104), (4, 80)])},
    'front': [L(outline([(10, 72), (6, 40), (18, 14), (50, 2), (82, 14), (94, 40), (90, 72), (84, 54), (60, 44), (40, 44), (16, 54)])),
              L(outline([(60, 6), (84, 18), (94, 46), (88, 66), (80, 46)]), 'shade', 'b', False),
              strand([(24, 30), (50, 18), (76, 30)], 'shade', 'f', 1.2),
              L(quad((40, 56), (50, 52), (60, 56)), 'skin_d', 'f', False, False, 1.2), L(quad((30, 92), (34, 96), (32, 100)), 'skin_d', 'f', False, False, 1.2),
              L(quad((70, 92), (66, 96), (68, 100)), 'skin_d', 'f', False, False, 1.2)],
    'side': [L(outline([(56, 54), (62, 42), (82, 40), (90, 24), (76, 6), (50, 0), (24, 6), (8, 24), (2, 50), (10, 74), (26, 80), (42, 72)])),
             L(ell(10, 60, 14, 14), 'mid', 'b', ln=True), L(outline([(4, 34), (24, 40), (26, 70), (8, 68)]), 'shade', 'b', False)],
    'back': [L(outline([(10, 80), (6, 40), (18, 14), (50, 2), (82, 14), (94, 40), (90, 80), (50, 86)])),
             L(outline([(56, 6), (84, 18), (96, 46), (90, 78), (64, 84)]), 'shade', 'b', False),
             L(ell(50, 66, 18, 16), 'mid', 'f', ln=True), strand([(36, 62), (64, 70)], 'shade', 'f', 1.2)],
}

# Ushijima Ikurou (portero suplente, adulto): pelo castaño muy oscuro en una seta abultada, con un flequillo grueso peinado
# de lado sobre la frente; ojos verdes y sonrisa amable
CHARS[f'{A}:alexander-scrivener'] = {
    'body': 'delgado', 'pal': pal('#3e3034', '#fcd8b8', iris='#6a7a3a', shade='#2a2024'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(10, 80), (2, 50), (6, 16), (26, -6), (50, -12), (76, -6), (94, 16), (98, 50), (90, 80), (82, 60), (18, 60)])),
              L(outline([(60, -8), (86, 6), (98, 40), (92, 74), (82, 50)]), 'shade', 'b', False),
              fr([(8, 70), (8, 36), (20, 12), (48, 2), (76, 8), (92, 30), (92, 64), (82, 54), (72, 46), (60, 50), (40, 54), (24, 50), (14, 60)]),
              strand([(30, 10), (60, 30), (84, 34)], 'shade', 'f', 1.2), strand([(46, 4), (70, 24), (90, 26)], 'shade', 'f', 1.2)],
    'side': [L(outline([(56, 60), (60, 48), (84, 46), (98, 30), (92, 8), (70, -8), (40, -12), (14, 0), (0, 26), (0, 60), (12, 82), (34, 86), (44, 74)])),
             L(outline([(2, 30), (26, 36), (30, 80), (10, 82)]), 'shade', 'b', False),
             fr([(62, -2), (92, 12), (100, 36), (96, 52), (86, 46), (72, 40)])],
    'back': [L(outline([(10, 84), (2, 50), (6, 16), (26, -6), (50, -12), (76, -6), (94, 16), (98, 50), (90, 84), (50, 90)])),
             L(outline([(56, -8), (86, 6), (98, 44), (92, 82), (64, 88)]), 'shade', 'b', False)],
}
