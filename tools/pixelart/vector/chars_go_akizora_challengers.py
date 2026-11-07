"""Edad Dorada (go-akizora-challengers): sus modelos 3D de Inazuma Eleven GO como referencia (busto de frente, perfil y espalda).
Un equipo de abuelos (y Scott, ya mayor, en GO)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from chars_bigwaves import rect_glasses, side_eye, white_eyes
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Chuck Pumpkins (portero): gordo de piel morena con una gorra rosa de visera corta calada hasta las cejas; patillas grises
# en forma de gancho por la mandíbula y el cogote gris; ojos de sueño y labios gruesos
CHARS['chuck-pumpkins'] = {
    'body': 'corpulento', 'pal': pal('#4a5866', '#b67c4a', cap='#ec7a8a', cap_d='#c85a6a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'lips', 'mouth_y': 98, 'mouth_w': 8, 'hairline': False, 'face_front': blob([(12, 50), (50, 44), (88, 50), (92, 80), (88, 104), (70, 116), (30, 116), (12, 104), (8, 80)])},
    'front': [L(outline([(10, 56), (6, 30), (14, 4), (50, -6), (86, 4), (94, 30), (90, 56), (50, 52)]), 'cap', 'f', ln=True),
              L(outline([(8, 30), (50, 26), (92, 30), (92, 40), (50, 36), (8, 40)]), 'cap_d', 'f', False),
              L(outline([(60, -2), (86, 6), (92, 50), (74, 52)]), 'cap_d', 'f', False),
              L(outline([(12, 60), (18, 62), (18, 96), (26, 100), (26, 108), (14, 104), (12, 80)]), 'mid', 'f', ln=True),
              L(outline([(88, 60), (82, 62), (82, 96), (74, 100), (74, 108), (86, 104), (88, 80)]), 'mid', 'f', ln=True)]
             + white_eyes(70, 14, 6, 4, 1.6, lid=1),
    'side': [L(outline([(10, 92), (8, 50), (40, 46), (50, 60), (46, 92), (24, 100)]), 'mid'),
             L(outline([(6, 52), (4, 24), (18, 2), (54, -4), (84, 8), (90, 38), (106, 50, 1), (84, 52), (50, 50)]), 'cap', 'f', ln=True),
             L(outline([(4, 34), (60, 32), (92, 40), (90, 46), (50, 40), (4, 44)]), 'cap_d', 'f', False),
             L(outline([(58, 64), (64, 66), (64, 98), (72, 102), (70, 108), (58, 104)]), 'mid', 'f', ln=True)] + side_eye(70, lid=1),
    'back': [L(outline([(12, 100), (8, 52), (92, 52), (88, 100), (50, 106)]), 'mid'),
             L(outline([(60, 54), (90, 54), (86, 98), (64, 104)]), 'shade', 'b', False),
             L(outline([(8, 56), (4, 30), (14, 4), (50, -6), (86, 4), (96, 30), (92, 56), (50, 58)]), 'cap', 'f', ln=True),
             L(outline([(6, 30), (50, 26), (94, 30), (94, 40), (50, 36), (6, 40)]), 'cap_d', 'f', False)],
}

# Scott Banyan en GO (Kogure Yuuya, ya mayor): pelo negro azulado corto con cuatro picos como cuernos, dos hacia arriba y
# dos hacia los lados; ojos naranjas de pillo y sonrisa
CHARS['go:scott-banyan'] = {
    'body': 'normal', 'pal': pal('#1e3644', '#fcd2a8', iris='#e0801e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 64), (12, 50), (-10, 44, 1), (10, 34), (14, 16), (4, -10, 1), (28, 4), (50, 0), (72, 4), (96, -10, 1), (86, 16), (90, 34),
                         (110, 44, 1), (88, 50), (84, 64), (78, 54), (22, 54)])),
              L(outline([(60, 4), (84, 14), (92, 42), (84, 60), (76, 40)]), 'shade', 'b', False),
              fringe([(14, 56), (16, 40), (30, 24), (50, 18), (70, 24), (84, 40), (86, 56), (70, 44), (58, 48), (50, 64, 1), (42, 48), (30, 44)]),
              L(outline([(38, 18), (52, 16), (46, 26)]), 'light', 'f', False)],
    'side': [L(outline([(54, 58), (62, 46), (82, 46), (92, 30), (84, 10), (64, -2), (60, -22, 1), (44, -2), (20, 4), (6, 22), (6, 50), (16, 72), (34, 72),
                        (46, 62)])),
             L(outline([(30, 30), (6, 20, 1), (22, 44)]), 'mid', 'b'),
             L(outline([(6, 40), (22, 46), (24, 66), (10, 60)]), 'shade', 'b', False),
             fringe([(66, 2), (88, 14), (94, 36), (90, 52, 1), (82, 42), (74, 32)])],
    'back': [L(outline([(16, 80), (12, 50), (-12, 44, 1), (10, 34), (14, 16), (2, -12, 1), (28, 4), (50, 0), (72, 4), (98, -12, 1), (86, 16), (90, 34),
                        (112, 44, 1), (88, 50), (84, 80), (50, 90)])),
             L(outline([(56, 4), (84, 14), (92, 46), (84, 78), (62, 86)]), 'shade', 'b', False)],
}

# Filbert Chestnut: abuelo flaco de nariz larguísima con un sombrero azul marino de ala ancha y plana (sin copa: asoma el pelo
# gris peinado hacia atrás), bigote azul marino fino y cejas de mala uva
CHARS['filbert-chestnut'] = {
    'body': 'delgado', 'pal': pal('#b0a490', '#f6c08a', iris='#2a1a1a', hat='#1e3058', hat_d='#141e3a', nose='#f0a878'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 104, 'hairline': (52, 36)},
    'front': [L(outline([(16, 64), (12, 34), (22, 8), (50, 0), (78, 8), (88, 34), (84, 64), (80, 50), (20, 50)])),
              strand([(30, 10), (34, 34)], 'shade', 'b', 1.0), strand([(50, 4), (50, 32)], 'shade', 'b', 1.0), strand([(70, 10), (66, 34)], 'shade', 'b', 1.0),
              L(outline([(-12, 36), (8, 28), (50, 26), (92, 28), (112, 36), (92, 42), (50, 40), (8, 42)]), 'hat', 'f', ln=True),
              L(outline([(44, 74), (56, 74), (58, 98), (50, 104), (42, 98)]), 'nose', 'f', ln=True),
              L(outline([(20, 96), (36, 92), (50, 96), (64, 92), (80, 96), (64, 100), (50, 98), (36, 100)]), 'hat', 'f', ln=True)],
    'side': [L(outline([(52, 56), (54, 38), (70, 28), (80, 20), (70, 4), (44, -2), (20, 6), (8, 28), (6, 54), (14, 76), (30, 80), (44, 66)])),
             L(outline([(4, 54), (10, 30), (26, 46), (34, 70), (20, 80)]), 'shade', 'b', False),
             L(outline([(-24, 36), (20, 32), (80, 28), (100, 30), (60, 38), (10, 40)]), 'hat', 'f', ln=True),
             L(outline([(84, 70), (108, 96), (100, 102), (86, 92)]), 'nose', 'f', ln=True),
             L(outline([(82, 96), (100, 96), (98, 100), (84, 100)]), 'hat', 'f', ln=True)],
    'back': [L(outline([(16, 84), (12, 34), (22, 8), (50, 0), (78, 8), (88, 34), (84, 84), (50, 92)]), 'shade'),
             L(outline([(14, 40), (22, 8), (50, 0), (78, 8), (86, 40), (50, 36)]), 'mid', 'b', False),
             L(ell(50, 36, 60, 9), 'hat', 'f', ln=True), L(ell(50, 38, 56, 6), 'hat_d', 'f', False)],
}

# Gadish Oldman: abuelo calvo de cráneo en punta y piel parda, con dos matas enormes de pelo rosa claro esponjoso a los
# lados; nariz larga, ojos pequeños verdes y arrugas
CHARS['gadish-oldman'] = {
    'body': 'delgado', 'pal': pal('#f4d4dc', '#b08a64', iris='#5a7a2a', shade='#d8a8b4', nose='#a07a54'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 104, 'hairline': False,
             'face_front': blob([(18, 56), (36, 10), (50, -14), (64, 10), (82, 56), (84, 90), (74, 112), (50, 120), (26, 112), (16, 90)])},
    'front': [L(outline([(16, 74), (-4, 82, 1), (-2, 66), (-16, 56, 1), (0, 46), (-10, 30, 1), (8, 30), (6, 12, 1), (20, 22), (30, 26), (24, 50), (18, 70)])),
              L(outline([(84, 74), (104, 82, 1), (102, 66), (116, 56, 1), (100, 46), (110, 30, 1), (92, 30), (94, 12, 1), (80, 22), (70, 26), (76, 50), (82, 70)])),
              L(outline([(44, 74), (56, 74), (60, 96), (50, 100), (40, 96)]), 'nose', 'f', ln=True),
              L(quad((36, 54), (50, 50), (64, 54)), OUTC, 'f', False, False, 1.0), L(quad((38, 60), (50, 57), (62, 60)), OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(48, 90), (28, 90), (14, 66), (20, 30), (40, 0), (54, -12), (64, 6), (86, 40), (94, 70), (90, 100), (76, 112), (60, 108)]), 'skin'),
             L(outline([(14, 74), (-8, 82, 1), (-4, 64), (-18, 54, 1), (-2, 44), (-10, 26, 1), (8, 30), (12, 12, 1), (26, 24), (40, 30), (44, 54), (34, 70)])),
             L(outline([(84, 70), (108, 92), (94, 100), (84, 92)]), 'nose', 'f', ln=True)],
    'back': [L(outline([(18, 80), (16, 56), (36, 10), (50, -14), (64, 10), (84, 56), (82, 80), (50, 90)]), 'skin'),
             L(outline([(18, 74), (-6, 82, 1), (-4, 64), (-18, 54, 1), (-2, 44), (-10, 28, 1), (8, 30), (10, 14, 1), (24, 24), (50, 30), (76, 24), (90, 14, 1),
                        (92, 30), (110, 28, 1), (102, 44), (118, 54, 1), (104, 64), (106, 82, 1), (82, 74), (50, 66)]))],
}

# Autumn Leaf: pelo rosa enorme de mechones en punta que salen en todas direcciones, sobre todo hacia los lados; ojos
# afilados y boca pequeña
CHARS['autumn-leaf'] = {
    'body': 'normal', 'pal': pal('#f2aac2', '#fcd8b8', iris='#1e1414'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 74), (0, 70, 1), (8, 60), (-14, 50, 1), (4, 42), (-8, 22, 1), (14, 22), (14, 0, 1), (30, 8), (40, -14, 1), (50, 2), (62, -16, 1),
                         (66, 4), (84, -4, 1), (82, 16), (106, 22, 1), (94, 38), (114, 50, 1), (94, 58), (104, 72, 1), (84, 74), (82, 58), (18, 58)])),
              L(outline([(58, 4), (84, 12), (96, 44), (88, 68), (76, 40)]), 'shade', 'b', False),
              fringe([(14, 66), (16, 42), (30, 24), (50, 18), (70, 24), (84, 42), (86, 66), (76, 52), (68, 62, 1), (62, 48), (52, 58, 1), (46, 46), (36, 60, 1),
                      (30, 48), (22, 62, 1)])],
    'side': [L(outline([(54, 60), (62, 48), (82, 50), (94, 36), (100, 20, 1), (82, 14), (78, -10, 1), (60, 0), (40, -14, 1), (34, 4), (8, -4, 1), (14, 16),
                        (-12, 22, 1), (4, 34), (-14, 48, 1), (6, 54), (-4, 72, 1), (14, 70), (16, 84, 1), (30, 74), (44, 72)])),
             L(outline([(4, 34), (22, 40), (26, 66), (8, 62)]), 'shade', 'b', False),
             strand([(10, 30), (40, 28)], 'shade', 'b', 1.0), strand([(6, 50), (34, 50)], 'shade', 'b', 1.0)],
    'back': [L(outline([(16, 80), (-2, 76, 1), (8, 64), (-14, 54, 1), (4, 44), (-10, 24, 1), (14, 22), (14, 0, 1), (30, 8), (40, -14, 1), (50, 2), (62, -16, 1),
                        (66, 4), (84, -4, 1), (82, 16), (108, 22, 1), (94, 40), (116, 52, 1), (94, 62), (104, 78, 1), (84, 80), (50, 88)])),
             L(outline([(56, 4), (84, 14), (96, 46), (86, 78), (62, 84)]), 'shade', 'b', False)],
}

# Skeeter Hawk: pelo naranja tostado peinado hacia atrás en un tupé alto que cae en ondas gruesas por los lados hasta la
# mandíbula; gafas de sol redondas verdes y dientes de conejo
CHARS['skeeter-hawk'] = {
    'body': 'normal', 'pal': pal('#d0601a', '#fcc890', shade='#a8461a', lens='#3aa84a', lens_d='#1e6a2a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'buck', 'mouth_y': 100, 'hairline': [(10, 92), (20, 60), (34, 44), (50, 54), (66, 44), (80, 60), (90, 92)]},
    'front': [L(outline([(2, 104), (-4, 84), (2, 60), (14, 26), (30, 4), (40, -10), (60, -10), (70, 4), (86, 26), (98, 60), (104, 84), (98, 104), (86, 100),
                         (80, 70), (20, 70), (14, 100)])),
              L(outline([(56, -6), (84, 20), (100, 70), (100, 100), (86, 96), (78, 40)]), 'shade', 'b', False),
              strand([(44, -6), (40, 40)], 'deep', 'b', 1.0), strand([(56, -6), (60, 40)], 'deep', 'b', 1.0),
              strand([(6, 70), (8, 100)], 'deep', 'b', 1.0), strand([(94, 70), (92, 100)], 'deep', 'b', 1.0),
              L(ell(34, 72, 10, 8), 'lens', 'f', ln=True), L(ell(66, 72, 10, 8), 'lens', 'f', ln=True),
              L(ell(37, 74, 6, 4), 'lens_d', 'f', False), L(ell(69, 74, 6, 4), 'lens_d', 'f', False),
              L([(44, 70), (56, 70)], OUTC, 'f', False, False, 1.4)],
    'side': [L(outline([(56, 52), (60, 38), (72, 20), (64, 2), (40, -8), (16, 4), (4, 30), (-2, 60), (2, 90), (10, 104), (30, 100), (38, 80), (48, 68)])),
             L(outline([(2, 40), (24, 44), (34, 94), (12, 100)]), 'shade', 'b', False),
             strand([(16, 20), (8, 60), (14, 96)], 'deep', 'b', 1.0), strand([(36, 6), (28, 50), (32, 92)], 'deep', 'b', 1.0),
             L(ell(86, 72, 6, 7), 'lens', 'f', ln=True), L([(80, 70), (50, 66)], OUTC, 'f', False, False, 1.4)],
    'back': [L(outline([(2, 104), (-4, 84), (2, 60), (14, 26), (30, 4), (40, -10), (60, -10), (70, 4), (86, 26), (98, 60), (104, 84), (98, 104), (50, 100)])),
             L(outline([(56, -6), (84, 20), (100, 70), (98, 102), (70, 100), (70, 40)]), 'shade', 'b', False),
             strand([(30, 10), (24, 60), (28, 98)], 'deep', 'b', 1.0), strand([(50, 0), (50, 98)], 'deep', 'b', 1.0),
             strand([(70, 10), (76, 60), (72, 98)], 'deep', 'b', 1.0)],
}

# Guy-Jean Harvestman: pelo castaño claro corto y mullido con las puntas abiertas a los lados, gafas negras rectangulares,
# ojos azules y sonrisa amable
CHARS['guy-jean-harvestman'] = {
    'body': 'normal', 'pal': pal('#b0986c', '#fcd8b4', iris='#3a8ac8', shade='#8a7050'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 84), (-2, 92, 1), (4, 74), (6, 46), (14, 16), (30, 2), (50, -2), (74, 4), (90, 20), (94, 46), (96, 74), (104, 92, 1), (88, 84),
                         (84, 62), (16, 62)])),
              L(outline([(60, 2), (86, 16), (96, 48), (94, 80), (84, 70), (80, 40)]), 'shade', 'b', False),
              fringe([(12, 66), (14, 38), (28, 18), (52, 10), (76, 18), (88, 38), (90, 66), (82, 52), (74, 58, 1), (68, 42), (58, 54, 1), (50, 38), (40, 50, 1),
                      (34, 38), (24, 56, 1), (18, 46)])] + rect_glasses('front', 75),
    'side': [L(outline([(54, 62), (58, 50), (80, 48), (94, 34), (98, 16, 1), (80, 12), (62, 0), (36, -2), (16, 8), (4, 30), (2, 58), (-10, 74, 1), (6, 76),
                        (4, 92, 1), (20, 84), (24, 96, 1), (34, 84), (46, 76)])),
             L(outline([(4, 34), (26, 40), (30, 80), (10, 76)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 14), (94, 36), (90, 50, 1), (82, 40), (72, 32)])] + rect_glasses('side', 75),
    'back': [L(outline([(12, 84), (-4, 92, 1), (4, 74), (6, 46), (14, 16), (30, 2), (50, -2), (74, 4), (90, 20), (94, 46), (96, 74), (106, 92, 1), (88, 84),
                        (72, 94, 1), (62, 86), (50, 96, 1), (38, 86), (28, 94, 1)]), 'shade'),
             L(outline([(10, 40), (14, 16), (30, 2), (50, -2), (74, 4), (90, 20), (92, 40), (70, 34), (50, 40), (30, 34)]), 'mid', 'b', False)],
}

# Hal L.W.N.: pelo azul grisáceo liso en forma de seta, un casco que se ensancha hacia abajo hasta acabar en un borde ancho
# a la altura de las orejas, con un flequillo de mechones; ojos castaños y gesto serio
CHARS['hal-l-w-n'] = {
    'body': 'normal', 'pal': pal('#6a78a0', '#fcd2b0', iris='#7a4a2a', shade='#4a4a68'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 74), (-2, 66), (2, 50), (12, 18), (30, 2), (50, -2), (70, 2), (88, 18), (98, 50), (102, 66), (90, 74), (84, 60), (16, 60)])),
              L(outline([(60, 2), (86, 16), (98, 50), (98, 66), (86, 66), (80, 36)]), 'shade', 'b', False),
              fringe([(10, 64), (14, 40), (28, 20), (50, 14), (72, 20), (86, 40), (90, 64), (84, 54), (76, 50), (70, 58, 1), (62, 46), (50, 46), (38, 46), (30, 58, 1),
                      (24, 50), (16, 54)]),
              L(outline([(28, 24), (44, 18), (40, 30)]), 'light', 'f', False)],
    'side': [L(outline([(54, 56), (60, 44), (82, 44), (94, 34), (90, 14), (70, 0), (44, -4), (18, 6), (2, 30), (-8, 56), (0, 62), (10, 60), (20, 92), (36, 84),
                        (46, 66)])),
             L(outline([(-6, 48), (40, 46), (54, 54), (40, 60), (0, 62)]), 'shade', 'b', False),
             fringe([(66, 2), (88, 14), (94, 36), (90, 50, 1), (82, 42), (74, 32)])],
    'back': [L(outline([(-2, 66), (2, 50), (12, 18), (30, 2), (50, -2), (70, 2), (88, 18), (98, 50), (102, 66), (50, 60)])),
             L(outline([(4, 64), (50, 58), (96, 64), (84, 74), (78, 92), (64, 88), (56, 98, 1), (48, 88), (40, 96, 1), (34, 88), (20, 90), (16, 74)]), 'shade'),
             L(outline([(60, 2), (86, 16), (98, 50), (98, 64), (80, 60)]), 'shade', 'b', False)],
}

# Jacko Lantern: piel morena, una melena morada enorme de mechones redondeados en capas que le abulta hasta los hombros;
# ojos cerrados de felicidad y una sonrisa de oreja a oreja
CHARS['jacko-lantern'] = {
    'body': 'normal', 'pal': pal('#8a2e8a', '#b07848', shade='#6a1e6a'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': [(10, 80), (20, 50), (40, 38), (50, 44), (60, 38), (80, 50), (90, 80)]},
    'front': [L(outline([(14, 120), (0, 112), (-6, 92), (-14, 76), (-6, 60), (-12, 42), (0, 30), (2, 10), (18, 0), (30, -10), (50, -12), (70, -10), (82, 0),
                         (98, 10), (100, 30), (112, 42), (106, 60), (114, 76), (106, 92), (100, 112), (86, 120), (80, 92), (84, 70), (16, 70), (20, 92)])),
              L(outline([(58, -8), (84, 4), (106, 50), (104, 108), (88, 116), (84, 70), (80, 30)]), 'shade', 'b', False),
              strand([(-4, 60), (14, 62)], 'deep', 'b', 1.0), strand([(104, 60), (86, 62)], 'deep', 'b', 1.0),
              strand([(0, 92), (16, 92)], 'deep', 'b', 1.0), strand([(100, 92), (84, 92)], 'deep', 'b', 1.0)],
    'side': [L(outline([(56, 52), (62, 36), (78, 32), (88, 20), (78, 0), (58, -10), (32, -10), (12, 0), (-2, 16), (-12, 34), (-6, 50), (-14, 66), (-4, 82),
                        (-8, 100), (6, 112), (24, 116), (40, 108), (44, 90), (38, 72), (48, 62)])),
             L(outline([(-6, 40), (20, 44), (36, 100), (6, 106)]), 'shade', 'b', False),
             strand([(-10, 50), (20, 54)], 'deep', 'b', 1.0), strand([(-8, 80), (24, 84)], 'deep', 'b', 1.0)],
    'back': [L(outline([(14, 120), (-2, 112), (-8, 92), (-14, 76), (-6, 60), (-12, 42), (0, 30), (2, 10), (18, 0), (30, -10), (50, -12), (70, -10), (82, 0),
                        (98, 10), (100, 30), (112, 42), (106, 60), (114, 76), (108, 92), (102, 112), (86, 120), (50, 124)])),
             L(outline([(58, -8), (84, 4), (106, 50), (104, 110), (70, 120), (72, 40)]), 'shade', 'b', False),
             strand([(-6, 30), (50, 40), (106, 30)], 'deep', 'b', 1.0), strand([(-10, 60), (50, 70), (110, 60)], 'deep', 'b', 1.0),
             strand([(-6, 92), (50, 100), (106, 92)], 'deep', 'b', 1.0)],
}

# Bobine Apples: abuela de cara redonda y mofletuda con una mata enorme de rizos color crema; el lado derecho, rosa con
# rayas blancas en zigzag, y una horquilla de corazón rosa
CHARS['bobine-apples'] = {
    'body': 'normal', 'pal': pal('#f6ecc0', '#fcdcbc', shade='#d8c494', pink='#f08898', heart='#ec5a8a'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False,
             'face_front': blob([(12, 60), (50, 54), (88, 60), (94, 84), (86, 106), (66, 116), (34, 116), (14, 106), (6, 84)])},
    'front': [L(outline([(6, 76), (-6, 66), (-6, 50), (-2, 30), (8, 12), (24, 0), (40, -8), (52, -16), (66, -8), (84, 0), (98, 14), (106, 34), (106, 56), (96, 72),
                         (84, 64), (70, 54), (50, 52), (24, 54), (14, 66)])),
              L(outline([(54, -12), (66, -8), (84, 0), (98, 14), (106, 34), (106, 56), (96, 72), (84, 64), (70, 54), (60, 40), (56, 14)]), 'pink'),
              L(quad((64, 6), (84, 10), (100, 26)), WHITE, 'b', False, False, 2.4), L(quad((66, 24), (86, 30), (104, 44)), WHITE, 'b', False, False, 2.4),
              L(outline([(14, 30), (22, 16), (40, 8), (30, 26)]), 'shade', 'b', False),
              L(outline([(26, 46), (20, 38), (24, 32), (30, 36), (36, 32), (40, 38), (34, 46), (30, 50)]), 'heart', 'f', ln=True)],
    'side': [L(outline([(56, 58), (62, 44), (78, 40), (92, 26), (84, 4), (62, -10), (36, -12), (12, -2), (-6, 18), (-10, 44), (-4, 66), (10, 84), (30, 88),
                        (44, 74)])),
             L(outline([(-6, 40), (24, 46), (34, 84), (6, 80)]), 'shade', 'b', False),
             L(outline([(76, 40), (72, 32), (76, 26), (82, 30), (88, 26), (92, 32), (86, 40), (82, 44)]), 'heart', 'f', ln=True)],
    'back': [L(outline([(-6, 74), (-8, 50), (-2, 30), (8, 12), (24, 0), (40, -8), (52, -16), (52, 96), (24, 92), (6, 86)])),
             L(outline([(52, -16), (66, -8), (84, 0), (98, 14), (106, 34), (108, 50), (106, 74), (94, 86), (76, 92), (52, 96)]), 'pink'),
             L(quad((54, 30), (80, 26), (104, 40)), WHITE, 'b', False, False, 2.6), L(quad((54, 58), (80, 54), (106, 66)), WHITE, 'b', False, False, 2.6),
             L(outline([(10, 30), (30, 20), (40, 60), (20, 80)]), 'shade', 'b', False)],
}

# Sibylle Equinox: pelo azul liso que se abre a los lados en un ala ancha como un sombrero, con un moño redondo encima,
# flequillo recto y dos mechones finos y largos delante de las orejas
CHARS['sibylle-equinox'] = {
    'body': 'chica', 'pal': pal('#1e4e9a', '#fcdcc0', iris='#2a6a7a', shade='#163a74'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(ell(50, -10, 12, 9)),
              L(outline([(16, 66), (-10, 54), (-14, 42), (0, 24), (20, 8), (50, 0), (80, 8), (100, 24), (114, 42), (110, 54), (84, 66), (84, 56), (16, 56)])),
              L(outline([(56, 2), (84, 10), (110, 40), (108, 54), (86, 60), (80, 30)]), 'shade', 'b', False),
              fringe([(16, 64), (18, 36), (30, 20), (50, 14), (70, 20), (82, 36), (84, 64), (80, 60), (78, 52), (22, 52), (20, 60)]),
              strand([(30, 44), (30, 52)], 'shade', 'f', 1.0), strand([(42, 44), (42, 52)], 'shade', 'f', 1.0), strand([(58, 44), (58, 52)], 'shade', 'f', 1.0),
              strand([(70, 44), (70, 52)], 'shade', 'f', 1.0),
              L(outline([(16, 62), (22, 62), (22, 120), (16, 120)]), 'mid', 'f', ln=True), L(outline([(84, 62), (78, 62), (78, 120), (84, 120)]), 'mid', 'f', ln=True)],
    'side': [L(ell(44, -8, 12, 10)),
             L(outline([(56, 54), (62, 40), (82, 40), (100, 30), (92, 12), (66, 0), (36, 0), (10, 10), (-12, 30), (-16, 46), (0, 52), (18, 56), (22, 82), (40, 80),
                        (48, 64)])),
             L(outline([(-14, 44), (30, 44), (50, 56), (20, 60)]), 'shade', 'b', False),
             L(outline([(60, 54), (66, 54), (66, 120), (60, 120)]), 'mid', 'f', ln=True)],
    'back': [L(ell(50, -10, 12, 9)),
             L(outline([(-12, 54), (-14, 42), (0, 24), (20, 8), (50, 0), (80, 8), (100, 24), (114, 42), (112, 54), (50, 60)])),
             L(outline([(14, 56), (86, 56), (84, 86), (50, 92), (16, 86)]), 'shade'),
             L(outline([(56, 2), (84, 10), (110, 40), (108, 54), (80, 52)]), 'shade', 'b', False),
             L([(20, 86), (18, 120)], 'mid', 'f', False, False, 3), L([(80, 86), (82, 120)], 'mid', 'f', False, False, 3)],
}
