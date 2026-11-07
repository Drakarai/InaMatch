"""Orden de los Caballeros Templarios (go-kuro-no-kishidan): sus modelos 3D de Inazuma Eleven GO como referencia (busto de frente, perfil y espalda).
Tsurugi (victor-blade) juega aquí con el mismo pelo que en el Raimon de GO: se reutiliza su dibujo."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from chars_alius import LONG_FACE, SKULL_B, SKULL_F, WIDE_FACE
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)
BLACK = (24, 22, 26, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


def star(cx, cy, r=3.2):
    import math
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return L(pts, BLACK, 'f', False)


# Lance Speares (portero): cabeza rapada de piel morena con un casquete de pelo blanco corto que baja en dos puntas por la
# frente, la nuca rosada, franjas rosas pintadas en la cara, ojos blancos redondos y los dientes apretados
CHARS['lance-speares'] = {
    'body': 'normal', 'pal': pal('#f0ead8', '#b8784e', iris='#1e1414', cap='#c8a098', cap_d='#a07a72', paint='#d8a8a0'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98, 'face_front': LONG_FACE, 'hairline': False, 'big_ears': 2},
    'front': [L(outline([(18, 56), (16, 24), (30, 6), (50, 0), (70, 6), (84, 24), (82, 56), (74, 40), (64, 54), (60, 32), (40, 32), (36, 54), (26, 40)]), 'mid', 'f'),
              L(outline([(62, 6), (80, 18), (82, 40), (74, 34), (70, 20)]), 'light', 'f', False),
              L(outline([(18, 60), (26, 62), (30, 86), (22, 92)]), 'paint', 'f', False),
              L(outline([(82, 60), (74, 62), (70, 86), (78, 92)]), 'paint', 'f', False)],
    'side': [L(outline([(12, 70), (12, 30), (30, 8), (56, 2), (80, 10), (90, 30), (84, 46), (60, 46), (52, 62), (50, 80), (32, 92), (16, 86)]), 'cap'),
             L(outline([(14, 66), (30, 72), (50, 76), (48, 86), (30, 92), (16, 86)]), 'cap_d', 'b', False),
             L(outline([(16, 28), (30, 8), (56, 2), (80, 10), (92, 30), (86, 46), (78, 34), (60, 24), (40, 28)]), 'mid'),
             L(outline([(76, 44), (84, 46), (82, 80), (74, 76)]), 'paint', 'f', False)],
    'back': [L(blob(SKULL_B), 'cap'),
             L(outline([(16, 64), (50, 58), (84, 64), (82, 74), (66, 86), (34, 86), (18, 74)]), 'cap_d', 'b', False),
             L(outline([(16, 40), (14, 30), (26, 12), (50, 4), (74, 12), (86, 30), (84, 40), (50, 34)]), 'mid')],
}

# Clay Moor: melena negra abultada en forma de campana, con ondas en capas que le llegan a la mandíbula y por detrás a la
# espalda, raya en medio y la frente despejada con estrellas pintadas; marcas negras triangulares bajo los ojos
CHARS['clay-moor'] = {
    'body': 'corpulento', 'pal': pal('#2a2a2c', '#e8a868', iris='#1e1414'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 100, 'face_front': LONG_FACE, 'hairline': False},
    'front': [L(outline([(16, 104), (-6, 98), (-2, 82), (-10, 66), (0, 48), (2, 24), (22, 6), (50, 0), (78, 6), (98, 24), (100, 48), (110, 66), (102, 82),
                         (106, 98), (84, 104), (84, 62), (16, 62)])),
              L(outline([(62, 4), (90, 18), (100, 50), (106, 92), (88, 96), (84, 50)]), 'shade', 'b', False),
              fringe([(16, 70), (14, 40), (30, 18), (48, 12), (36, 24), (24, 46), (22, 70)]),
              fringe([(84, 70), (86, 40), (70, 18), (52, 12), (64, 24), (76, 46), (78, 70)]),
              strand([(0, 66), (14, 70)], 'deep', 'f', 1.0), strand([(100, 66), (86, 70)], 'deep', 'f', 1.0),
              star(38, 38), star(32, 48, 2.6), star(62, 38), star(68, 48, 2.6),
              L([(28, 80), (42, 80), (36, 96)], BLACK, 'f', False), L([(72, 80), (58, 80), (64, 96)], BLACK, 'f', False)],
    'side': [L(outline([(56, 52), (66, 30), (60, 8), (36, -2), (12, 8), (-2, 30), (-12, 52), (-6, 64), (-24, 76), (-34, 108, 1), (-14, 96), (-8, 112, 1), (6, 96),
                        (14, 110, 1), (22, 92), (34, 80), (48, 70)])),
             L(outline([(-4, 50), (24, 50), (28, 86), (-4, 96)]), 'shade', 'b', False),
             strand([(0, 34), (40, 30)], 'deep', 'b', 1.0), strand([(-8, 64), (34, 62)], 'deep', 'b', 1.0),
             star(80, 44, 2.6), L([(76, 80), (88, 80), (86, 94)], BLACK, 'f', False)],
    'back': [L(outline([(-6, 104), (-4, 84), (-12, 66), (0, 46), (2, 24), (22, 6), (50, 0), (78, 6), (98, 24), (100, 46), (112, 66), (104, 84), (106, 104), (50, 110)])),
             L(outline([(58, 4), (90, 18), (100, 50), (106, 102), (70, 106)]), 'shade', 'b', False),
             strand([(4, 40), (50, 36), (96, 40)], 'deep', 'b', 1.0), strand([(-6, 66), (50, 62), (106, 66)], 'deep', 'b', 1.0),
             strand([(-2, 88), (50, 86), (102, 88)], 'deep', 'b', 1.0)],
}

# Nun Chuck: grandullón de cara ancha; pelo castaño rojizo rizado en un bloque plano encima de la cabeza y dos mechones
# rosas gruesos en forma de cuerno curvado a los lados; ojos verdes y sonrisa de pillo
CHARS['nun-chuck'] = {
    'body': 'corpulento', 'pal': pal('#6a2a1a', '#fcdcb4', iris='#2a9a7a', horn='#e87870', horn_d='#c05a52'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'face_front': WIDE_FACE, 'hairline': False},
    'front': [L(outline([(-6, 24), (-14, 40), (-14, 64), (-6, 86), (6, 98, 1), (4, 76), (8, 50), (10, 34)]), 'horn'),
              L(outline([(106, 24), (114, 40), (114, 64), (106, 86), (94, 98, 1), (96, 76), (92, 50), (90, 34)]), 'horn'),
              L(outline([(-4, 40), (-8, 60), (0, 82), (2, 60)]), 'horn_d', 'b', False), L(outline([(104, 40), (108, 60), (100, 82), (98, 60)]), 'horn_d', 'b', False),
              L(outline([(6, 52), (2, 30), (6, 4), (18, -6), (34, -2), (50, -8), (66, -2), (82, -6), (94, 4), (98, 30), (94, 52), (76, 48), (50, 54), (24, 48)]), 'mid', 'f'),
              L(outline([(60, -2), (82, -4), (96, 28), (92, 48), (78, 44)]), 'shade', 'f', False),
              strand([(16, 16), (28, 10), (40, 16)], 'deep', 'f', 1.0), strand([(56, 14), (70, 8), (84, 16)], 'deep', 'f', 1.0)],
    'side': [L(outline([(10, 48), (8, 26), (14, 4), (32, -6), (56, -4), (78, -8), (94, 4), (98, 26), (92, 46), (70, 50), (52, 60), (42, 82), (24, 88), (12, 72)])),
             L(outline([(48, 30), (40, 50), (42, 80), (52, 98, 1), (60, 76), (60, 48), (56, 32)]), 'horn', 'f', ln=True),
             strand([(24, 14), (40, 6), (54, 14)], 'deep', 'b', 1.0), strand([(62, 20), (78, 14), (88, 22)], 'deep', 'b', 1.0)],
    'back': [L(outline([(-6, 24), (-14, 40), (-14, 64), (-6, 86), (6, 98, 1), (4, 76), (8, 50), (10, 34)]), 'horn'),
             L(outline([(106, 24), (114, 40), (114, 64), (106, 86), (94, 98, 1), (96, 76), (92, 50), (90, 34)]), 'horn'),
             L(outline([(6, 88), (2, 30), (6, 4), (18, -6), (34, -2), (50, -8), (66, -2), (82, -6), (94, 4), (98, 30), (94, 88), (80, 92), (50, 86), (20, 92)])),
             L(outline([(58, -2), (82, -4), (96, 28), (94, 86), (66, 88)]), 'shade', 'b', False)],
}

# Dirk Anlace: piel morena y pelo verde con mechones en punta que salen a los lados por encima de las orejas, flequillo de
# mechones por la frente y puntas vueltas hacia fuera en la nuca
CHARS['dirk-anlace'] = {
    'body': 'normal', 'pal': pal('#2a8a5a', '#a8704a', iris='#1e1414'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 94), (0, 92, 1), (8, 78), (6, 52), (-12, 30, 1), (10, 30), (16, 10), (36, -4), (50, -6), (64, -4), (84, 10), (90, 30), (112, 30, 1),
                         (94, 52), (92, 78), (100, 92, 1), (86, 94), (82, 64), (18, 64)])),
              L(outline([(60, -2), (84, 12), (94, 50), (88, 86), (80, 50)]), 'shade', 'b', False),
              fringe([(12, 74), (14, 44), (26, 22), (50, 12), (74, 22), (86, 44), (88, 74), (80, 60), (74, 70, 1), (68, 50), (58, 64, 1), (54, 46), (44, 66, 1),
                      (40, 48), (30, 62, 1), (24, 50), (18, 66, 1)]),
              L(outline([(30, 20), (46, 14), (38, 26)]), 'light', 'f', False)],
    'side': [L(outline([(54, 62), (58, 50), (80, 50), (94, 36), (88, 14), (96, -6, 1), (72, 2), (50, -8), (24, 0), (8, 18), (-10, 28, 1), (6, 38), (0, 64), (-12, 90, 1),
                        (8, 82), (20, 96, 1), (30, 82), (46, 76)])),
             L(outline([(6, 36), (24, 42), (26, 76), (6, 72)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 42), (92, 64, 1), (84, 48), (78, 58, 1), (74, 40), (64, 30)])],
    'back': [L(outline([(14, 86), (-4, 96, 1), (6, 78), (6, 52), (-14, 30, 1), (10, 30), (16, 10), (36, -4), (50, -6), (64, -4), (84, 10), (90, 30), (114, 30, 1),
                        (94, 52), (94, 78), (104, 96, 1), (86, 86), (70, 96, 1), (60, 86), (50, 96, 1), (40, 86), (30, 96, 1)])),
             L(outline([(56, -2), (84, 12), (94, 50), (90, 84), (64, 90)]), 'shade', 'b', False)],
}

# Spike Stiletto: cabeza rapada de cara alargada con una corona de pinchos azul celeste encima, como una estrella, sobre
# una franja verde oscura que se abre a los lados como alas, y dos mechones finos rizados que le caen por la cara
CHARS['spike-stiletto'] = {
    'body': 'delgado', 'pal': pal('#a8d8f0', '#f0b880', iris='#1e1414', wing='#1e3c3c', shade='#88b4cc'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'face_front': LONG_FACE, 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin'),
              L(outline([(-14, 28), (14, 16), (50, 12), (86, 16), (114, 28), (90, 34), (50, 28), (10, 34)]), 'wing'),
              L(outline([(-6, 2, 1), (20, 8), (24, -12, 1), (38, 0), (46, -24, 1), (56, -2), (66, -14, 1), (72, 4), (106, -2, 1), (82, 22), (60, 26), (40, 22), (30, 28),
                         (16, 22)])),
              L(outline([(56, -2), (66, -14, 1), (72, 4), (106, -2, 1), (82, 22), (64, 22)]), 'shade', 'b', False),
              L(quad((40, 22), (26, 40), (18, 50)) + quad((18, 50), (14, 46), (16, 42))[1:], 'mid', 'f', False, False, 1.8),
              L(quad((46, 24), (30, 52), (24, 64)), 'mid', 'f', False, False, 2.4),
              L([(34, 64), (40, 70)], OUTC, 'f', False, False, 1.0), L([(66, 64), (60, 70)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(10, 34), (8, 22), (26, 16), (44, 10), (30, 6), (40, -10, 1), (52, 2), (62, -14, 1), (68, 4), (88, -4, 1), (82, 18), (96, 26, 1), (70, 26),
                        (50, 24), (30, 30)])),
             L(outline([(-12, 36), (6, 22), (40, 24), (40, 32), (6, 36)]), 'wing'),
             L(quad((86, 22), (96, 40), (92, 56)), 'mid', 'f', False, False, 1.8)],
    'back': [L(blob(SKULL_B), 'skin'),
             L(outline([(-16, 20), (14, 30), (40, 30), (50, 44, 1), (60, 30), (86, 30), (116, 20), (90, 14), (50, 12), (10, 14)]), 'wing'),
             L(outline([(-12, 4), (20, 6), (50, -2), (80, 6), (112, 4), (100, 14), (50, 12), (0, 14)]), 'shade')],
}

# Jack Knife: pelo rubio de puntas hacia arriba con un pico alto en lo alto, flequillo de mechones a los lados de la cara
# y un punto oscuro en la frente; ojos verdes
CHARS['jack-knife'] = {
    'body': 'normal', 'pal': pal('#f0dc90', '#e8b078', iris='#2a8a4a', shade='#c8a060', dot='#5a2a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 84), (8, 50), (4, 24), (20, 4), (34, 6), (46, -20, 1), (54, 0), (66, -2), (84, 6), (96, 24), (92, 50), (86, 84), (80, 60), (20, 60)])),
              L(outline([(60, 0), (84, 10), (96, 32), (88, 74), (80, 44)]), 'shade', 'b', False),
              fringe([(10, 78), (8, 46), (20, 22), (40, 14), (50, 30), (54, 16), (76, 20), (90, 44), (92, 78), (82, 64), (76, 50), (72, 62, 1), (66, 44), (58, 52, 1),
                      (52, 38), (46, 50), (40, 38), (30, 54, 1), (26, 46), (20, 66, 1)]),
              L(ell(50, 58, 2.2, 2.2), 'dot', 'f', False)],
    'side': [L(outline([(54, 64), (58, 50), (80, 48), (94, 34), (88, 10), (96, -10, 1), (72, -2), (64, -18, 1), (52, -6), (26, -4), (8, 16), (2, 44), (8, 74), (24, 84),
                        (40, 78)])),
             L(outline([(4, 36), (24, 40), (28, 76), (8, 70)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 14), (96, 40), (92, 64, 1), (84, 46), (80, 56, 1), (76, 40), (66, 30)])],
    'back': [L(outline([(14, 84), (6, 50), (4, 24), (20, 4), (34, 4), (46, -20, 1), (54, 0), (66, -2), (78, -16, 1), (84, 6), (96, 24), (94, 50), (86, 84), (50, 92)])),
             L(outline([(56, 0), (84, 10), (96, 34), (90, 80), (62, 88)]), 'shade', 'b', False)],
}

# Bilbo Baton: pelo negro verdoso en forma de embudo enorme, muy ancho y plano arriba y que se estrecha hasta las
# sienes, con flequillo recto; gafas grises rectangulares y cejas gruesas
CHARS['bilbo-baton'] = {
    'body': 'normal', 'pal': pal('#2a3438', '#f6c8a0', iris='#1e1414', light='#4a5a60'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'hairline': False, 'big_ears': 2, 'glasses': (150, 150, 140, 255),
             'glasses_rect': True},
    'front': [L(outline([(16, 64), (12, 40), (-44, -6, 1), (-20, -14), (50, -18), (120, -14), (144, -6, 1), (88, 40), (84, 64), (78, 52), (22, 52)])),
              L(outline([(-24, -10), (124, -10), (100, -4), (0, -4)]), 'light', 'b', False),
              L(outline([(56, -12), (130, -8), (90, 34), (84, 50)]), 'shade', 'b', False),
              fringe([(14, 56), (16, 34), (50, 30), (84, 34), (86, 56), (78, 50), (76, 60), (70, 50), (62, 60), (56, 50), (48, 60), (42, 50), (34, 60), (28, 50),
                      (22, 60)])],
    'side': [L(outline([(60, 54), (62, 40), (82, 40), (90, 24), (68, -8), (46, -44, 1), (20, -10), (4, 20), (2, 52), (12, 76), (30, 82), (48, 72)])),
             L(outline([(42, -36), (20, -6), (6, 24), (6, 54), (20, 60), (24, 20)]), 'shade', 'b', False),
             fringe([(66, 20), (90, 24), (94, 44), (86, 44), (74, 36)])],
    'back': [L(outline([(16, 86), (10, 50), (-44, -6, 1), (-20, -14), (50, -18), (120, -14), (144, -6, 1), (90, 50), (84, 86), (50, 92)])),
             L(outline([(56, -12), (130, -8), (90, 50), (84, 84), (62, 88)]), 'shade', 'b', False)],
}

# Bayonet Gunne (sin modelo 3D: del retrato): melena lisa rubia rosada hasta los hombros, con mechones largos que le caen
# por la cara y le tapan media frente; mirada fría
CHARS['bayonet-gunne'] = {
    'body': 'delgado', 'pal': pal('#f0d8c8', '#e8b890', iris='#1e1414', shade='#d8b4a4'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 116), (0, 120, 1), (2, 80), (2, 40), (14, 12), (36, 0), (64, 0), (86, 12), (98, 40), (98, 80), (100, 120, 1), (90, 116), (84, 64),
                         (16, 64)])),
              L(outline([(60, 2), (86, 14), (98, 44), (98, 112), (86, 110), (82, 50)]), 'shade', 'b', False),
              fringe([(10, 90), (10, 44), (24, 18), (50, 8), (76, 18), (90, 44), (90, 90), (84, 76), (80, 62), (72, 76, 1), (68, 54), (60, 66, 1), (56, 48), (48, 92, 1),
                      (44, 50), (36, 70, 1), (32, 50), (22, 86, 1), (18, 66)]),
              L(outline([(56, 18), (78, 26), (86, 50), (74, 44)]), 'shade', 'f', False)],
    'side': [L(outline([(54, 64), (60, 50), (82, 52), (94, 36), (90, 14), (70, 0), (40, -2), (16, 10), (2, 38), (-2, 80), (-4, 118, 1), (12, 110), (24, 120, 1), (34, 104),
                        (44, 86)])),
             L(outline([(2, 40), (24, 44), (32, 104), (6, 106)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 14), (96, 42), (94, 72, 1), (86, 54), (82, 66, 1), (76, 44), (66, 30)])],
    'back': [L(outline([(2, 118), (2, 80), (2, 40), (14, 12), (36, 0), (64, 0), (86, 12), (98, 40), (98, 80), (98, 118), (86, 112), (74, 122, 1), (62, 112), (50, 122, 1),
                        (38, 112), (26, 122, 1), (14, 112)])),
             L(outline([(56, 2), (86, 14), (98, 44), (98, 116), (66, 116)]), 'shade', 'b', False),
             strand([(50, 4), (50, 100)], 'shade', 'b', 1.2)],
}

# Howie Itzer: piel morena y media melena turquesa lisa hasta la mandíbula, con las puntas vueltas hacia fuera y un
# flequillo largo de lado; un ojo rojo y otro verde agua
CHARS['howie-itzer'] = {
    'body': 'normal', 'pal': pal('#5ad8b0', '#9a6a4a', iris='#2aa8a0', shade='#3ab08c'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 96), (-8, 100, 1), (2, 84), (0, 50), (8, 22), (28, 4), (50, -2), (72, 4), (92, 22), (100, 50), (98, 84), (108, 100, 1), (88, 96), (84, 64),
                         (16, 64)])),
              L(outline([(60, 2), (88, 16), (100, 50), (100, 92), (88, 92), (82, 50)]), 'shade', 'b', False),
              fringe([(10, 80), (8, 46), (20, 20), (44, 8), (70, 12), (88, 32), (90, 64), (82, 52), (74, 42), (62, 50, 1), (58, 38), (48, 56, 1), (44, 40), (34, 62, 1),
                      (28, 48), (20, 74, 1)])],
    'side': [L(outline([(54, 66), (60, 52), (82, 52), (94, 38), (90, 14), (68, 0), (40, -2), (16, 10), (2, 38), (0, 78), (-12, 100, 1), (12, 92), (30, 96, 1), (42, 82)])),
             L(outline([(2, 40), (24, 44), (32, 90), (4, 92)]), 'shade', 'b', False),
             fringe([(62, 2), (90, 16), (96, 42), (92, 62, 1), (84, 48), (76, 36)])],
    'back': [L(outline([(10, 96), (-10, 102, 1), (0, 84), (0, 50), (8, 22), (28, 4), (50, -2), (72, 4), (92, 22), (100, 50), (100, 84), (110, 102, 1), (90, 96), (74, 104, 1),
                        (62, 96), (50, 106, 1), (38, 96), (26, 104, 1)])),
             L(outline([(56, 2), (88, 16), (100, 50), (100, 96), (66, 98)]), 'shade', 'b', False)],
}

# Flam Berger: una melena naranja enorme y esponjosa que sube en picos y le tapa casi toda la cara, cayendo en ondas por
# los lados y la espalda; solo se le ve la barbilla
CHARS['flam-berger'] = {
    'body': 'normal', 'pal': pal('#ff6a10', '#f6c8a0', iris='#1e1414', shade='#d84a08', light='#ff9a50'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': [L(outline([(-6, 112), (-14, 92), (-8, 70), (-12, 48), (0, 26), (6, 4), (24, -8), (38, -4), (50, -16, 1), (62, -4), (78, -8), (94, 4), (100, 26), (112, 48),
                         (108, 70), (114, 92), (106, 112), (84, 104), (84, 70), (16, 70), (16, 104)])),
              L(outline([(62, -4), (88, 4), (106, 50), (108, 104), (90, 100), (84, 40)]), 'shade', 'b', False),
              fringe([(10, 96), (4, 70), (6, 40), (20, 14), (40, 4), (50, 14), (60, 4), (80, 14), (94, 40), (96, 70), (90, 96), (82, 90), (70, 98, 1), (60, 86), (54, 94),
                      (50, 84), (46, 94), (40, 86), (30, 98, 1), (18, 90)]),
              L(outline([(56, 10), (82, 20), (92, 50), (84, 84), (70, 40)]), 'shade', 'f', False), L(outline([(24, 20), (40, 12), (34, 30)]), 'light', 'f', False),
              strand([(50, 20), (50, 70)], 'shade', 'f', 1.0)],
    'side': [L(outline([(70, 90), (84, 64), (94, 40), (90, 14), (80, -6), (66, -24, 1), (60, -6), (40, -8), (16, 4), (0, 30), (-14, 56), (-28, 84), (-18, 110), (6, 116),
                        (24, 104), (40, 96), (54, 98)])),
             L(outline([(-8, 50), (20, 50), (30, 96), (0, 108)]), 'shade', 'b', False), L(outline([(24, 2), (52, -4), (40, 14)]), 'light', 'b', False)],
    'back': [L(outline([(-10, 112), (-16, 90), (-10, 66), (-12, 46), (0, 24), (6, 4), (24, -8), (38, -4), (50, -16, 1), (62, -4), (78, -8), (94, 4), (100, 24), (112, 46),
                        (110, 66), (116, 90), (110, 112), (50, 118)])),
             L(outline([(58, -4), (88, 4), (106, 50), (110, 110), (70, 114)]), 'shade', 'b', False),
             L(outline([(30, 30), (44, 22), (56, 30), (46, 40)]), 'light', 'b', False)],
}

# Matt Chetty (portero suplente): bloque de pelo castaño en punta plano por arriba como una meseta, los lados y la nuca
# rapados claros con una raya blanca cosida por detrás, rayas negras bajo los ojos y sonrisa ladina
CHARS['matt-chetty'] = {
    'body': 'normal', 'pal': pal('#8a4a26', '#f6c8a0', iris='#1e1414', buzz='#c8b090', buzz_d='#a8906c', seam='#f0ece4'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 100, 'hairline': (60, 52)},
    'front': [L(outline([(14, 70), (12, 40), (22, 30), (78, 30), (88, 40), (86, 70), (80, 60), (20, 60)]), 'buzz'),
              L(outline([(10, 42), (-4, 30, 1), (4, 18), (-4, 4, 1), (14, 2), (16, -12, 1), (30, -4), (40, -14, 1), (52, -4), (62, -14, 1), (72, -4), (88, -10, 1), (88, 4),
                         (106, 6, 1), (96, 18), (106, 30, 1), (90, 42), (70, 36), (60, 46, 1), (52, 34), (40, 40), (28, 34)]), 'mid', 'f'),
              L(outline([(56, -4), (88, -4), (100, 28), (86, 38), (70, 26)]), 'shade', 'f', False),
              L([(26, 84), (38, 84)], BLACK, 'f', False, False, 2.4), L([(62, 84), (74, 84)], BLACK, 'f', False, False, 2.4)],
    'side': [L(outline([(54, 40), (58, 62), (50, 82), (44, 96), (26, 96), (12, 84), (8, 60), (10, 36)]), 'buzz'),
             L(outline([(14, 40), (24, 92), (32, 96), (22, 40)]), 'seam', 'b', ln=True),
             L(outline([(4, 42), (-8, 30, 1), (4, 18), (-2, 2, 1), (16, 2), (22, -14, 1), (36, -4), (50, -16, 1), (60, -4), (74, -14, 1), (82, 0), (100, 0, 1), (94, 16),
                        (106, 28, 1), (90, 40), (70, 34), (50, 42), (30, 34)]), 'mid', 'f')],
    'back': [L(blob(SKULL_B), 'buzz'),
             L(outline([(44, 36), (56, 36), (56, 96), (44, 96)]), 'seam', 'b', ln=True),
             L(outline([(10, 42), (-4, 30, 1), (4, 18), (-4, 4, 1), (14, 2), (16, -12, 1), (30, -4), (40, -14, 1), (52, -4), (62, -14, 1), (72, -4), (88, -10, 1), (88, 4),
                        (106, 6, 1), (96, 18), (106, 30, 1), (90, 42), (50, 38)]), 'mid', 'f'),
             L(outline([(56, -4), (88, -4), (100, 28), (90, 40), (66, 36)]), 'shade', 'f', False)],
}

# Harold Shields: pelo magenta en forma de seta, un casco liso que se abre muchísimo a los lados a la altura de la cara
# como el ala de un sombrero (oscuro por debajo), con flequillo hasta los ojos; ojos redondos ambarinos
CHARS['harold-shields'] = {
    'body': 'bajito', 'pal': pal('#c83060', '#f8e0b8', iris='#8a6a20', under='#3a2030'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 96), (-14, 92), (-24, 80, 1), (-6, 60), (4, 30), (20, 6), (50, -4), (80, 6), (96, 30), (106, 60), (124, 80, 1), (114, 92), (84, 96), (84, 60),
                         (16, 60)])),
              L(outline([(-20, 82), (-6, 78), (16, 80), (16, 96), (-14, 92)]), 'under', 'b', False),
              L(outline([(120, 82), (106, 78), (84, 80), (84, 96), (114, 92)]), 'under', 'b', False),
              L(outline([(60, 0), (86, 14), (104, 58), (100, 76), (84, 60)]), 'shade', 'b', False),
              fringe([(12, 82), (12, 44), (28, 18), (50, 10), (72, 18), (88, 44), (88, 82), (80, 66), (68, 58), (58, 60), (50, 76, 1), (42, 60), (32, 58), (20, 66)]),
              L(outline([(40, 16), (50, 12), (48, 50), (42, 44)]), 'light', 'f', False)],
    'side': [L(outline([(60, 66), (66, 52), (86, 50), (96, 36), (90, 12), (66, -4), (36, -4), (12, 12), (2, 40), (-10, 72), (-18, 90, 1), (16, 88), (40, 92), (62, 96),
                        (70, 84)])),
             L(outline([(-14, 86), (16, 80), (40, 86), (64, 92), (40, 94), (14, 90)]), 'under', 'b', False),
             fringe([(64, 0), (90, 14), (96, 40), (94, 64, 1), (86, 50), (78, 38)])],
    'back': [L(outline([(-24, 84, 1), (-6, 60), (4, 30), (20, 6), (50, -4), (80, 6), (96, 30), (106, 60), (124, 84, 1), (100, 96), (50, 100), (0, 96)])),
             L(outline([(-20, 84), (10, 74), (50, 72), (90, 74), (120, 84), (100, 94), (50, 98), (0, 94)]), 'under', 'b', False),
             L(outline([(56, 0), (86, 14), (104, 58), (110, 76), (70, 72)]), 'shade', 'b', False)],
}

# Hal Byrd: pelo negro verdoso con dos cuernos altísimos en punta arriba y dos alas en punta a los lados de la cara,
# enmarcándola hasta las mejillas, con rayas negras pintadas bajo los ojos; cara pálida
CHARS['hal-byrd'] = {
    'body': 'delgado', 'pal': pal('#2a4448', '#f6dcb0', iris='#1e1414', shade='#1a2c30'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'face_front': LONG_FACE, 'hairline': False},
    'front': [L(outline([(16, 96), (6, 70), (-20, 40, 1), (8, 44), (12, 20), (22, -30, 1), (34, 10), (50, 6), (66, 10), (78, -30, 1), (88, 20), (92, 44), (120, 40, 1),
                         (94, 70), (84, 96), (80, 60), (20, 60)])),
              L(outline([(66, 12), (78, -26), (88, 20), (92, 50), (112, 44), (90, 70), (82, 86), (80, 50)]), 'shade', 'b', False),
              fringe([(14, 90), (12, 50), (22, 26), (40, 18), (50, 24), (60, 18), (78, 26), (88, 50), (86, 90), (80, 70), (74, 52), (64, 40), (50, 36), (36, 40), (26, 52),
                      (20, 70)]),
              L([(24, 84), (32, 96), (28, 104)], BLACK, 'f', False, False, 2.2), L([(76, 84), (68, 96), (72, 104)], BLACK, 'f', False, False, 2.2)],
    'side': [L(outline([(56, 60), (64, 46), (84, 46), (92, 30), (84, 8), (60, -2), (40, -60, 1), (20, -20), (0, 20), (-10, 60), (6, 80), (24, 90), (40, 78)])),
             L(outline([(36, -50), (22, -16), (4, 24), (-4, 60), (14, 70), (20, 20)]), 'shade', 'b', False),
             fringe([(66, 4), (90, 16), (94, 40), (90, 64, 1), (82, 44), (72, 32)]),
             L([(78, 86), (86, 98)], BLACK, 'f', False, False, 2.2)],
    'back': [L(outline([(16, 76), (2, 40), (-20, 20, 1), (10, 12), (24, -10), (50, -14), (76, -10), (90, 12), (120, 20, 1), (98, 40), (84, 76), (66, 88), (50, 100, 1),
                        (34, 88)])),
             L(outline([(50, -10), (76, -10), (90, 12), (110, 22), (90, 46), (80, 80), (56, 92)]), 'shade', 'b', False),
             L(outline([(30, 0), (42, -4), (50, -14), (58, -4), (70, 0), (50, 8)]), 'light', 'b', False)],
}

# Morgan Stern: pelo verde oliva de puntas con un mechón grande curvado por delante, la parte baja de la cabeza rapada
# negra con dos rayas alrededor, ojos rojos con marcas negras en las mejillas y los dientes apretados
CHARS['morgan-stern'] = {
    'body': 'normal', 'pal': pal('#8a8a30', '#f6c8a0', iris='#c81e2a', buzz='#1a1a1a', band='#4a4a1a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 100, 'hairline': (62, 50)},
    'front': [L(outline([(14, 72), (12, 46), (88, 46), (86, 72), (80, 64), (20, 64)]), 'buzz'),
              L(outline([(12, 50), (-4, 40, 1), (8, 30), (0, 12, 1), (18, 12), (22, -6, 1), (36, 2), (50, -10, 1), (60, 2), (78, -4, 1), (80, 12), (100, 12, 1), (92, 30),
                         (104, 40, 1), (88, 50), (50, 46)])),
              L(outline([(60, 4), (80, 8), (94, 34), (86, 48), (76, 30)]), 'shade', 'b', False),
              L([(10, 56), (90, 56)], 'band', 'f', False, False, 1.6), L([(10, 60), (90, 60)], 'band', 'f', False, False, 1.6),
              fringe([(40, 14), (56, 6), (70, 14), (66, 30), (58, 24), (56, 40), (60, 66, 1), (48, 46), (44, 30)]),
              L([(26, 84), (34, 96)], BLACK, 'f', False, False, 2.4), L([(74, 84), (66, 96)], BLACK, 'f', False, False, 2.4)],
    'side': [L(outline([(54, 46), (58, 62), (50, 82), (44, 96), (26, 96), (12, 84), (8, 60), (10, 44)]), 'buzz'),
             L([(8, 56), (54, 54)], 'band', 'f', False, False, 1.6), L([(8, 60), (54, 58)], 'band', 'f', False, False, 1.6),
             L(outline([(6, 50), (-6, 30, 1), (8, 22), (4, 4, 1), (22, 6), (30, -12, 1), (44, 0), (62, -10, 1), (66, 4), (90, 2, 1), (84, 18), (98, 30, 1), (80, 46), (50, 46),
                        (24, 50)])),
             fringe([(78, 14), (98, 20), (100, 34), (90, 30), (84, 46), (76, 32)])],
    'back': [L(blob(SKULL_B), 'buzz'),
             L([(14, 56), (86, 56)], 'band', 'f', False, False, 1.6), L([(14, 62), (86, 62)], 'band', 'f', False, False, 1.6),
             L(outline([(12, 50), (-4, 40, 1), (8, 30), (0, 12, 1), (18, 12), (22, -6, 1), (36, 2), (50, -10, 1), (60, 2), (78, -4, 1), (80, 12), (100, 12, 1), (92, 30),
                        (104, 40, 1), (88, 50), (50, 46)])),
             L(outline([(56, 2), (80, 8), (94, 34), (86, 48), (64, 44)]), 'shade', 'b', False)],
}

# Roman Ballista: pelo granate de pinchos grandes peinados hacia arriba y hacia atrás, cara pálida con marcas rojas bajo
# los ojos y mirada fiera de ojos rojos
CHARS['roman-ballista'] = {
    'body': 'normal', 'pal': pal('#a8203a', '#f0d8b0', iris='#c81e1e', mark='#c83a3a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(14, 74), (6, 50), (-6, 30, 1), (8, 26), (6, 4), (22, -6), (10, -22, 1), (38, -10), (52, -26, 1), (60, -8), (90, -20, 1), (84, 6), (100, 10, 1),
                         (92, 28), (94, 50), (86, 74), (80, 60), (20, 60)])),
              L(outline([(58, -6), (86, 2), (94, 40), (88, 66), (78, 40)]), 'shade', 'b', False),
              fringe([(12, 66), (12, 40), (24, 18), (44, 10), (64, 14), (82, 30), (88, 60), (80, 50), (72, 40), (60, 36), (52, 52, 1), (46, 36), (34, 40), (24, 60, 1),
                      (18, 50)]),
              L(outline([(30, 18), (46, 12), (36, 26)]), 'light', 'f', False),
              L([(30, 84), (38, 92)], 'mark', 'f', False, False, 2.0), L([(70, 84), (62, 92)], 'mark', 'f', False, False, 2.0)],
    'side': [L(outline([(54, 60), (60, 48), (82, 48), (94, 34), (90, 12), (80, -4), (62, -32, 1), (54, -8), (30, -28, 1), (24, -4), (-10, -8, 1), (6, 14), (-16, 26, 1),
                        (2, 40), (-8, 64, 1), (10, 64), (6, 84, 1), (24, 80), (40, 76)])),
             L(outline([(2, 34), (24, 40), (26, 72), (6, 66)]), 'shade', 'b', False),
             fringe([(68, 4), (90, 16), (96, 40), (92, 58, 1), (84, 44), (76, 32)]), L([(80, 86), (88, 92)], 'mark', 'f', False, False, 2.0)],
    'back': [L(outline([(14, 84), (4, 52), (-8, 30, 1), (8, 24), (4, 4), (22, -6), (12, -24, 1), (40, -10), (54, -28, 1), (62, -8), (96, -24, 1), (84, 8), (104, 12, 1),
                        (92, 30), (96, 52), (88, 84), (70, 94, 1), (60, 86), (50, 96, 1), (40, 86), (30, 94, 1)])),
             L(outline([(56, -6), (86, 2), (94, 40), (90, 82), (62, 88)]), 'shade', 'b', False)],
}
