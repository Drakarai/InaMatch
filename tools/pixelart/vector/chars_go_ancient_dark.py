"""Oscuridad Ancestral (go-ancient-dark): sus modelos 3D de Inazuma Eleven GO como referencia (busto de frente, perfil y espalda).
Varios juegan también en el Equipo Zero (Blake, Tynan, Shady, Yang y Tezcat): se dibujan aquí una vez."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)
RED = (230, 30, 30, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Nero Night (portero): capucha granate ceñida con una franja lila en V desde lo alto hasta el entrecejo y dos cuernos
# verde agua a los lados; la cara en sombra, con dos ojos rojos que brillan, y la capucha cae en punta por la espalda
CHARS['nero-night'] = {
    'body': 'normal', 'pal': pal('#a01e50', '#c8946a', iris='#e01e1e', light='#c8a0dc', horn='#6ab0a8', horn_d='#4a8a84', dark='#24141c'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 34), (-28, 14, 1), (10, 24)]), 'horn', 'b', ln=True), L(outline([(84, 34), (128, 14, 1), (90, 24)]), 'horn', 'b', ln=True),
              L(outline([(16, 32), (-20, 18, 1), (2, 22)]), 'horn_d', 'b', False), L(outline([(84, 32), (120, 18, 1), (98, 22)]), 'horn_d', 'b', False),
              L(outline([(10, 112), (4, 70), (6, 30), (20, 6), (50, -6), (80, 6), (94, 30), (96, 70), (90, 112), (78, 92), (76, 66), (24, 66), (22, 92)])),
              L(outline([(60, -2), (84, 10), (94, 40), (92, 108), (80, 88), (80, 40)]), 'shade', 'b', False),
              L(outline([(18, 30), (32, 6), (50, 0), (68, 6), (82, 30), (68, 44), (50, 66, 1), (32, 44)]), 'light', 'b', ln=True),
              L(ell(50, 16, 13, 10), 'mid', 'b', ln=True),
              L(outline([(22, 60), (50, 70), (78, 60), (78, 86), (22, 86)]), 'dark', 'f', False),
              L(ell(37, 76, 6, 2.6), RED, 'f', False), L(ell(63, 76, 6, 2.6), RED, 'f', False),
              L(outline([(10, 112), (8, 66), (22, 62), (26, 100)]), 'light', 'f', ln=True), L(outline([(90, 112), (92, 66), (78, 62), (74, 100)]), 'light', 'f', ln=True)],
    'side': [L(outline([(68, 62), (80, 40), (76, 14), (56, 0), (30, 2), (12, 20), (4, 50), (-4, 100), (-16, 146, 1), (12, 112), (30, 92), (40, 72), (52, 62)])),
             L(outline([(4, 60), (14, 70), (6, 110), (-6, 128, 1), (-2, 96)]), 'light', 'b', ln=True),
             L(outline([(46, 14), (40, -18, 1), (58, 8)]), 'horn', 'b', ln=True),
             L(outline([(56, 8), (78, 20), (82, 44), (70, 62), (60, 40)]), 'light', 'f', ln=True),
             L(outline([(64, 62), (86, 62), (84, 82), (64, 80)]), 'dark', 'f', False), L(ell(80, 72, 3, 2.2), RED, 'f', False)],
    'back': [L(outline([(16, 32), (-28, 14, 1), (10, 22)]), 'horn', 'b', ln=True), L(outline([(84, 32), (128, 14, 1), (90, 22)]), 'horn', 'b', ln=True),
             L(outline([(4, 118), (2, 70), (6, 30), (20, 6), (50, -6), (80, 6), (94, 30), (98, 70), (96, 118), (70, 106), (50, 124, 1), (30, 106)])),
             L(outline([(58, -2), (84, 10), (96, 50), (96, 114), (60, 110)]), 'shade', 'b', False),
             L(outline([(22, 24), (36, 6), (50, 2), (64, 6), (78, 24), (50, 84, 1)]), 'light', 'b', ln=True),
             L(ell(50, 14, 12, 9), 'mid', 'b', ln=True)],
}

# Morris Moore: piel rojiza, orejas de punta y dos cuernos marrón oscuro curvos; melena verde oliva con raya en medio que cae
# hasta los hombros y se abre en puntas; ojos rojos de ceño fruncido, marcas negras bajo los ojos y perilla
CHARS['morris-moore'] = {
    'body': 'corpulento', 'pal': pal('#8a8a1e', '#b8664a', iris='#c81e1e', horn='#4a3a3a', horn_d='#2e2424', shade='#6a6a14'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': (60, 46), 'ears': False},
    'front': [L(outline([(28, 30), (12, 10), (8, -16), (18, -40, 1), (22, -10), (38, 20)]), 'horn', 'b', ln=True),
              L(outline([(72, 30), (88, 10), (92, -16), (82, -40, 1), (78, -10), (62, 20)]), 'horn', 'b', ln=True),
              L(outline([(14, 78), (10, 30), (24, 10), (50, 4), (76, 10), (90, 30), (86, 78), (98, 92), (120, 94, 1), (104, 104), (118, 120, 1), (92, 114), (80, 102),
                         (80, 70), (20, 70), (20, 102), (8, 114), (-18, 120, 1), (-4, 104), (-20, 94, 1), (2, 92)])),
              L(outline([(56, 8), (80, 16), (88, 50), (96, 96), (84, 100), (78, 50)]), 'shade', 'b', False),
              strand([(50, 6), (50, 40)], 'shade', 'b', 1.2),
              L(outline([(16, 70), (-2, 58, 1), (14, 84)]), 'skin', 'f', ln=True), L(outline([(84, 70), (102, 58, 1), (86, 84)]), 'skin', 'f', ln=True),
              L([(30, 82), (26, 94)], OUTC, 'f', False, False, 1.6), L([(70, 82), (74, 94)], OUTC, 'f', False, False, 1.6),
              L(outline([(46, 104), (54, 104), (50, 114, 1)]), OUTC, 'f', False)],
    'side': [L(outline([(54, 30), (52, 4), (58, -40, 1), (66, 0), (66, 26)]), 'horn', 'b', ln=True),
             L(outline([(56, 54), (60, 40), (78, 34), (84, 16), (64, 2), (36, 2), (14, 20), (6, 50), (-6, 70), (-22, 74, 1), (-10, 86), (-24, 104, 1), (-2, 102),
                        (-8, 118, 1), (16, 108), (26, 118, 1), (34, 98), (44, 86), (50, 70)])),
             L(outline([(4, 50), (24, 56), (30, 96), (4, 100)]), 'shade', 'b', False),
             L(outline([(46, 60), (34, 48, 1), (50, 78)]), 'skin', 'f', ln=True),
             L(outline([(80, 104), (86, 104), (84, 112, 1)]), OUTC, 'f', False)],
    'back': [L(outline([(26, 30), (10, 10), (6, -16), (16, -40, 1), (20, -10), (36, 20)]), 'horn', 'b', ln=True),
             L(outline([(74, 30), (90, 10), (94, -16), (84, -40, 1), (80, -10), (64, 20)]), 'horn', 'b', ln=True),
             L(outline([(10, 90), (10, 30), (24, 10), (50, 4), (76, 10), (90, 30), (90, 90), (106, 92), (120, 112, 1), (96, 110), (84, 124, 1), (70, 108),
                        (50, 124, 1), (30, 108), (16, 124, 1), (4, 110), (-20, 112, 1), (-6, 92)])),
             L(outline([(56, 8), (82, 16), (92, 60), (106, 106), (70, 108), (70, 50)]), 'shade', 'b', False),
             strand([(30, 40), (26, 100)], 'shade', 'b', 1.2), strand([(70, 40), (74, 100)], 'shade', 'b', 1.2)],
}

# Jet Onyx: cabezón calvo en forma de pera (estrecho arriba y ancho en la mandíbula), un moño de gomas moradas con un
# copete azul celeste en lo alto, un antifaz azul de ojos rasgados y los dientes apretados
_JET = blob([(32, 30), (50, 20), (68, 30), (86, 62), (94, 92), (84, 114), (50, 122), (16, 114), (6, 92), (14, 62)], 8)
CHARS['jet-onyx'] = {
    'body': 'corpulento', 'pal': pal('#5a9ec8', '#f0b070', iris='#1e1414', ring='#6a4a7a', mask='#2a4aa8', light='#a8dcf0'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 102, 'hairline': False, 'face_front': _JET, 'big_ears': 2, 'ear_out': 8},
    'front': [L(outline([(36, 20), (34, 6), (48, 2), (60, 6), (66, -10), (56, -18), (40, -16), (30, -6)]), 'mid', 'b', ln=True),
              L(outline([(44, -14), (60, -14), (52, -6)]), 'light', 'b', False),
              L(ell(50, 20, 15, 6), 'ring', 'b', ln=True),
              L(outline([(18, 74), (44, 82), (44, 90), (22, 84)]), 'mask', 'f', ln=True), L(outline([(82, 74), (56, 82), (56, 90), (78, 84)]), 'mask', 'f', ln=True),
              L([(50, 46), (50, 58)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(40, 120), (16, 112), (10, 80), (24, 40), (46, 22), (66, 28), (82, 50), (94, 80), (96, 104), (82, 120)]), 'skin'),
             L(outline([(16, 90), (20, 112), (40, 118), (30, 96)]), 'skin_d', 'b', False),
             L(outline([(36, 22), (34, 8), (46, 2), (56, 6), (64, -10), (52, -18), (38, -14), (30, -4)]), 'mid', 'b', ln=True),
             L(ell(46, 22, 12, 5), 'ring', 'b', ln=True),
             L(outline([(78, 74), (90, 76), (90, 84), (80, 84)]), 'mask', 'f', ln=True)],
    'back': [L(outline([(32, 30), (50, 20), (68, 30), (86, 62), (94, 92), (84, 112), (50, 118), (16, 112), (6, 92), (14, 62)]), 'skin'),
             L(outline([(56, 30), (84, 62), (90, 96), (70, 114)]), 'skin_d', 'b', False),
             L(outline([(36, 20), (34, 6), (48, 2), (60, 6), (66, -10), (56, -18), (40, -16), (30, -6)]), 'mid', 'b', ln=True),
             L(ell(50, 20, 15, 6), 'ring', 'b', ln=True)],
}

# Cole Ebony: pelo rojo de pinchos hacia arriba como una llama, con mechones de punta a los lados; ojos entornados
CHARS['cole-ebony'] = {
    'body': 'normal', 'pal': pal('#c8401e', '#fcdcc0', iris='#2a1a1a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(18, 66), (2, 62, 1), (12, 48), (0, 30, 1), (16, 26), (12, 2, 1), (28, 12), (32, -16, 1), (44, 2), (54, -26, 1), (60, 0), (72, -14, 1),
                         (74, 10), (90, 4, 1), (86, 26), (100, 32, 1), (88, 46), (98, 62, 1), (82, 66), (82, 50), (18, 50)])),
              L(outline([(60, 0), (82, 12), (90, 40), (86, 60), (76, 40)]), 'shade', 'b', False),
              fringe([(16, 60), (18, 40), (32, 28), (50, 24), (68, 28), (82, 40), (84, 60), (76, 50), (70, 58, 1), (62, 46), (52, 56, 1), (46, 44), (38, 56, 1),
                      (30, 46), (24, 58, 1)])],
    'side': [L(outline([(56, 58), (64, 46), (82, 44), (90, 26), (96, 8, 1), (76, 10), (70, -18, 1), (58, 2), (40, -24, 1), (34, 4), (8, -6, 1), (16, 18), (-8, 26, 1),
                        (8, 40), (-6, 56, 1), (12, 60), (8, 78, 1), (24, 72), (40, 70)])),
             L(outline([(6, 34), (24, 40), (24, 66), (8, 58)]), 'shade', 'b', False),
             fringe([(66, 6), (90, 18), (94, 40), (90, 54, 1), (82, 40), (74, 30)])],
    'back': [L(outline([(18, 82), (4, 84, 1), (10, 66), (-4, 52, 1), (10, 44), (0, 22, 1), (16, 22), (14, -2, 1), (30, 10), (36, -18, 1), (46, 4), (56, -24, 1),
                        (62, 4), (80, -10, 1), (80, 14), (100, 20, 1), (90, 38), (104, 50, 1), (90, 62), (96, 84, 1), (82, 82), (50, 90)])),
             L(outline([(56, 4), (84, 14), (92, 50), (86, 78), (60, 84)]), 'shade', 'b', False),
             strand([(30, 30), (40, 54), (36, 76)], 'deep', 'b', 1.0), strand([(70, 30), (60, 54), (64, 76)], 'deep', 'b', 1.0)],
}

# Blake Obscura: pelo rubio claro con un rizo enorme en espiral que sale de lo alto hacia la izquierda, flequillo peinado de
# lado hacia la derecha y dos mechones largos junto a la cara; ojos ámbar afilados
CHARS['blake-obscura'] = {
    'body': 'normal', 'pal': pal('#f0d898', '#fcdcc0', iris='#c8862a', shade='#d0a870'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(44, 8), (28, -6), (8, -22), (0, -42), (14, -58), (36, -58), (46, -44), (40, -32), (30, -36), (24, -46), (14, -42), (16, -28), (32, -14), (50, 0)]), 'mid', 'b', ln=True),
              L(outline([(14, 70), (10, 40), (20, 14), (50, 2), (78, 10), (92, 30), (94, 56), (86, 70), (80, 56), (20, 56)])),
              L(outline([(56, 4), (82, 14), (92, 40), (86, 64), (76, 40)]), 'shade', 'b', False),
              L(outline([(14, 60), (8, 90), (12, 104, 1), (20, 88), (22, 62)]), 'mid', 'f', ln=True),
              L(outline([(86, 60), (92, 90), (88, 104, 1), (80, 88), (78, 62)]), 'mid', 'f', ln=True),
              fringe([(14, 56), (18, 32), (34, 16), (56, 12), (78, 20), (94, 40), (98, 62, 1), (86, 52), (74, 46), (60, 44), (46, 50), (34, 56, 1), (26, 48),
                      (20, 62, 1)]),
              L(outline([(40, 18), (70, 20), (88, 38), (68, 30), (46, 28)]), 'light', 'f', False)],
    'side': [L(outline([(36, 10), (30, -10), (36, -32), (54, -40), (66, -30), (56, -24), (46, -28), (42, -14), (48, 6)]), 'mid', 'b', ln=True),
             L(outline([(54, 58), (58, 46), (80, 44), (92, 30), (86, 10), (64, -2), (38, 0), (16, 12), (6, 36), (8, 66), (22, 84), (38, 82), (48, 70)]), 'shade'),
             L(outline([(30, 4), (64, -2), (86, 10), (92, 30), (70, 26), (44, 20)]), 'mid', 'b', False),
             fringe([(64, 2), (90, 18), (96, 44), (92, 60, 1), (84, 46), (82, 104, 1), (76, 60), (70, 34)])],
    'back': [L(outline([(60, 12), (70, -4), (86, -18), (100, -26), (102, -8), (90, 4), (80, 0), (82, -10), (74, -6), (68, 12)]), 'mid', 'b', ln=True),
             L(outline([(14, 74), (10, 40), (20, 14), (50, 2), (80, 14), (90, 40), (86, 74), (68, 86), (32, 86)]), 'shade'),
             L(outline([(16, 40), (22, 14), (50, 2), (78, 14), (86, 40), (50, 46)]), 'mid', 'b', False),
             L(outline([(14, 64), (10, 92), (14, 104, 1), (22, 88), (22, 70)]), 'mid', 'f', ln=True),
             L(outline([(86, 64), (90, 92), (86, 104, 1), (78, 88), (78, 70)]), 'mid', 'f', ln=True)],
}

# Shady Shwartz: pelo plateado lila en forma de seta enorme (un sombrerete ancho y plano) que le baja hasta los ojos, con dos
# puntas vueltas hacia fuera a la altura de la mandíbula; piel morena y ojos azul claro con mucha raya negra
CHARS['shady-shwartz'] = {
    'body': 'normal', 'pal': pal('#dcd2dc', '#a87048', iris='#68c8e8', shade='#b4a0ac', deep='#8a7480'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 96), (2, 92), (-4, 108, 1), (10, 104), (20, 90)]), 'mid', 'b', ln=True),
              L(outline([(86, 96), (98, 92), (104, 108, 1), (90, 104), (80, 90)]), 'mid', 'b', ln=True),
              L(outline([(14, 72), (4, 46), (-24, 40), (-30, 30, 1), (-12, 18), (14, -2), (50, -12), (86, -2), (112, 18), (130, 30, 1), (124, 40), (96, 46),
                         (86, 72), (78, 56), (68, 70), (58, 60), (50, 76, 1), (42, 60), (32, 70), (22, 56)]), 'mid', 'f'),
              L(outline([(-26, 34), (8, 40), (50, 36), (92, 40), (126, 34), (110, 44), (90, 48), (50, 44), (10, 48), (-10, 44)]), 'shade', 'f', False),
              strand([(32, 44), (34, 66)], 'deep', 'f', 1.0), strand([(50, 40), (50, 70)], 'deep', 'f', 1.0), strand([(68, 44), (66, 66)], 'deep', 'f', 1.0),
              L(outline([(30, 4), (60, -2), (40, 12)]), WHITE, 'f', False)],
    'side': [L(outline([(10, 82), (-10, 92), (-30, 104, 1), (-8, 98), (16, 92)]), 'mid', 'b', ln=True),
             L(outline([(70, 70), (80, 52), (100, 44), (96, 24), (80, 4), (50, -10), (18, -6), (0, 10), (-4, 30), (6, 50), (14, 80), (34, 76), (50, 62), (62, 70)]), 'mid', 'f'),
             L(outline([(4, 40), (40, 40), (90, 34), (98, 42), (80, 50), (40, 48), (8, 52)]), 'shade', 'f', False),
             L(outline([(20, 0), (50, -6), (36, 8)]), WHITE, 'f', False)],
    'back': [L(outline([(16, 96), (0, 100), (-12, 112, 1), (8, 108), (24, 92)]), 'mid', 'b', ln=True),
             L(outline([(84, 96), (100, 100), (112, 112, 1), (92, 108), (76, 92)]), 'mid', 'b', ln=True),
             L(outline([(16, 92), (8, 50), (-24, 44), (-30, 30, 1), (-12, 18), (14, -2), (50, -12), (86, -2), (112, 18), (130, 30, 1), (124, 44), (92, 50), (84, 92),
                        (50, 98)]), 'shade', 'f'),
             L(outline([(-28, 32), (-12, 18), (14, -2), (50, -12), (86, -2), (112, 18), (128, 32), (90, 30), (50, 28), (10, 30)]), 'mid', 'f', False)],
}

# Goth Grimshaw: pelo negro alborotado de pinchos en todas direcciones, con mechones que le caen entre los ojos; piel pálida
# y ojos rojos grandes de mirada fija
CHARS['goth-grimshaw'] = {
    'body': 'normal', 'pal': pal('#241a16', '#fce0c8', iris='#b81e1e'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(20, 84), (2, 96, 1), (8, 76), (-16, 70, 1), (4, 58), (-14, 40, 1), (8, 34), (0, 12, 1), (20, 14), (22, -10, 1), (36, 4), (50, -14, 1),
                         (60, 2), (76, -12, 1), (78, 10), (100, 6, 1), (92, 28), (114, 36, 1), (96, 50), (112, 66, 1), (94, 72), (100, 94, 1), (82, 84), (80, 60),
                         (20, 60)])),
              L(outline([(60, 2), (84, 12), (96, 44), (90, 76), (78, 44)]), 'shade', 'b', False),
              fringe([(14, 70), (14, 40), (28, 22), (50, 16), (72, 22), (86, 40), (88, 70), (80, 58), (76, 74, 1), (66, 52), (58, 66, 1), (54, 50), (50, 82, 1),
                      (46, 50), (40, 66, 1), (32, 52), (24, 74, 1), (20, 58)])],
    'side': [L(outline([(56, 62), (64, 50), (82, 50), (94, 36), (100, 16, 1), (82, 14), (78, -10, 1), (60, 2), (44, -20, 1), (34, 4), (8, -10, 1), (14, 18), (-12, 22, 1),
                        (4, 38), (-18, 50, 1), (2, 58), (-10, 76, 1), (12, 76), (8, 94, 1), (26, 82), (42, 76)])),
             L(outline([(2, 36), (22, 42), (24, 74), (6, 64)]), 'shade', 'b', False),
             fringe([(66, 6), (92, 18), (98, 44), (94, 70, 1), (86, 52), (80, 64, 1), (76, 42), (68, 30)])],
    'back': [L(outline([(18, 90), (0, 98, 1), (8, 76), (-16, 68, 1), (4, 56), (-14, 38, 1), (8, 32), (0, 10, 1), (20, 12), (22, -10, 1), (36, 4), (50, -14, 1),
                        (60, 2), (76, -12, 1), (78, 10), (100, 6, 1), (92, 28), (114, 36, 1), (96, 52), (114, 68, 1), (94, 76), (102, 98, 1), (82, 90), (66, 100, 1),
                        (50, 90), (34, 100, 1)])),
             L(outline([(56, 4), (84, 12), (96, 50), (90, 86), (62, 92)]), 'shade', 'b', False),
             strand([(30, 30), (40, 56), (34, 82)], 'deep', 'b', 1.0), strand([(70, 30), (60, 56), (66, 82)], 'deep', 'b', 1.0)],
}

# Duff Dooley: cabezón calvo y redondo de piel clara con dos moños verdes redondos en lo alto; un antifaz negro con los ojos
# blancos redondos, una nariz roja en rombo y una sonrisa enorme
_DUFF = blob([(14, 50), (30, 30), (50, 26), (70, 30), (86, 50), (94, 80), (86, 106), (50, 120), (14, 106), (6, 80)], 8)
CHARS['duff-dooley'] = {
    'body': 'corpulento', 'pal': pal('#8ab05a', '#ecd0a4', iris='#1e1414', shade='#6a8a40', nose='#d82020'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False, 'face_front': _DUFF, 'big_ears': 3, 'ear_out': 8},
    'front': [L(ell(14, 16, 14, 13)), L(ell(86, 16, 14, 13)),
              L(outline([(4, 10), (14, 4), (26, 12), (14, 26)]), 'shade', 'b', False), L(outline([(76, 10), (86, 4), (98, 12), (86, 26)]), 'shade', 'b', False),
              L(outline([(20, 62), (36, 58), (48, 64), (52, 64), (64, 58), (80, 62), (82, 80), (66, 86), (50, 80), (34, 86), (18, 80)]), OUTC, 'f', False),
              L(ell(34, 72, 5.4, 5.4), WHITE, 'f', False), L(ell(66, 72, 5.4, 5.4), WHITE, 'f', False),
              L(ell(34, 72, 2, 2.4), OUTC, 'f', False), L(ell(66, 72, 2, 2.4), OUTC, 'f', False),
              L(outline([(50, 76, 1), (58, 90, 1), (50, 108, 1), (42, 90, 1)]), 'nose', 'f', ln=True),
              L(quad((24, 94), (50, 112), (76, 94)), OUTC, 'f', False, False, 2.0)],
    'side': [L(outline([(40, 118), (16, 108), (8, 76), (16, 44), (40, 26), (66, 28), (86, 44), (96, 76), (94, 102), (78, 118)]), 'skin'),
             L(ell(44, 18, 13, 12)), L(outline([(32, 10), (44, 4), (56, 12), (44, 26)]), 'shade', 'b', False),
             L(outline([(70, 62), (92, 62), (96, 82), (74, 82)]), OUTC, 'f', False), L(ell(86, 72, 4, 4.4), WHITE, 'f', False),
             L(outline([(92, 80, 1), (112, 92, 1), (94, 100, 1)]), 'nose', 'f', ln=True)],
    'back': [L(outline([(14, 50), (30, 30), (50, 26), (70, 30), (86, 50), (94, 80), (86, 104), (50, 114), (14, 104), (6, 80)]), 'skin'),
             L(outline([(58, 30), (86, 50), (92, 86), (66, 108)]), 'skin_d', 'b', False),
             L(ell(14, 16, 14, 13)), L(ell(86, 16, 14, 13)),
             L(outline([(76, 10), (86, 4), (98, 12), (86, 26)]), 'shade', 'b', False)],
}

# Tynan Crowe: piel morena, cresta morada de pinchos altos con los lados rapados en morado oscuro, un mechón largo que le cae
# por en medio de la cara y dos mechones largos que salen de la nuca y se abren a los lados a la altura de la barbilla; ojos
# naranjas y cejas moradas
CHARS['tynan-crowe'] = {
    'body': 'normal', 'pal': pal('#6a2aa8', '#a8704a', iris='#e05a1e', buzz='#584a7a', shade='#4e1e80'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': (56, 44)},
    'front': [L(outline([(16, 64), (14, 40), (24, 24), (76, 24), (86, 40), (84, 64), (78, 54), (22, 54)]), 'buzz'),
              L(outline([(14, 96), (-20, 112, 1), (2, 96), (-14, 98, 1), (10, 86), (20, 90)]), 'mid', 'b', ln=True),
              L(outline([(86, 96), (120, 112, 1), (98, 96), (114, 98, 1), (90, 86), (80, 90)]), 'mid', 'b', ln=True),
              L(outline([(28, 36), (22, 0), (30, -32, 1), (38, -4), (44, -38, 1), (52, -6), (60, -38, 1), (64, -4), (74, -30, 1), (78, 0), (72, 36), (50, 44)]), 'mid', 'f'),
              L(outline([(56, -4), (72, -26), (70, 30), (56, 38)]), 'shade', 'f', False),
              L(outline([(44, 36), (56, 34), (52, 60), (42, 92, 1), (44, 60)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(54, 44), (60, 62), (52, 82), (44, 96), (26, 96), (12, 84), (8, 60), (12, 36)]), 'buzz'),
             L(outline([(20, 80), (6, 96), (-14, 110, 1), (2, 104), (14, 116, 1), (22, 98), (32, 86)]), 'mid', 'b', ln=True),
             L(outline([(14, 40), (8, 20), (-14, 6, 1), (8, 6), (-4, -14, 1), (18, -8), (14, -30, 1), (34, -14), (40, -36, 1), (52, -12), (66, -26, 1), (70, -4),
                        (84, -10, 1), (82, 8), (96, 16), (98, 48, 1), (86, 22), (64, 18), (40, 30)]), 'mid', 'f'),
             L(outline([(14, 36), (10, 16), (36, 10), (60, 14), (40, 26)]), 'shade', 'f', False)],
    'back': [L(outline([(16, 70), (14, 40), (24, 24), (76, 24), (86, 40), (84, 70), (64, 92), (36, 92)]), 'buzz'),
             L(outline([(30, 30), (24, 0), (30, -32, 1), (38, -4), (44, -38, 1), (52, -6), (60, -38, 1), (64, -4), (74, -30, 1), (78, 0), (72, 30), (64, 60), (66, 110),
                        (50, 118, 1), (34, 110), (36, 60)]), 'mid', 'f'),
             L(outline([(54, -4), (72, -26), (70, 30), (62, 64), (64, 108), (54, 112)]), 'shade', 'f', False)],
}

# Tezcat: pelo negro azulado en media melena lisa con flequillo, dos cuentas turquesa en lo alto y, a los lados de la
# cara, dos colmillos blancos colgados de una cinta roja; piel morena, ojos grandes negros y pecas
CHARS['tezcat'] = {
    'body': 'bajito', 'pal': pal('#24283a', '#d09460', iris='#1e1a1a', bead='#3ac8c0', band='#c8281e'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 90), (8, 50), (14, 20), (32, 4), (50, 0), (68, 4), (86, 20), (92, 50), (86, 90), (80, 64), (20, 64)])),
              L(outline([(60, 4), (84, 18), (92, 50), (86, 84), (78, 50)]), 'shade', 'b', False),
              fringe([(12, 70), (14, 40), (26, 18), (50, 10), (74, 18), (86, 40), (88, 70), (80, 58), (74, 66, 1), (66, 50), (58, 62, 1), (52, 46), (44, 62, 1),
                      (38, 48), (28, 64, 1), (20, 56)]),
              L(ell(34, 14, 4.4, 4), 'bead', 'f', ln=True), L(ell(66, 14, 4.4, 4), 'bead', 'f', ln=True),
              strand([(34, 18), (24, 40), (18, 70)], 'deep', 'f', 1.2), strand([(66, 18), (76, 40), (82, 70)], 'deep', 'f', 1.2),
              L(outline([(12, 80), (22, 80), (22, 86), (12, 86)]), 'band', 'f', ln=True), L(outline([(78, 80), (88, 80), (88, 86), (78, 86)]), 'band', 'f', ln=True),
              L(outline([(14, 86), (22, 86), (20, 108, 1)]), WHITE, 'f', ln=True), L(outline([(78, 86), (86, 86), (80, 108, 1)]), WHITE, 'f', ln=True),
              L([(26, 90), (28, 92)], OUTC, 'f', False, False, 1.2), L([(72, 90), (74, 92)], OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(54, 64), (58, 52), (80, 48), (92, 34), (86, 12), (64, 0), (36, 2), (14, 16), (4, 44), (6, 74), (2, 94, 1), (18, 84), (28, 94, 1), (36, 80),
                        (48, 74)])),
             L(outline([(4, 40), (24, 44), (28, 78), (8, 76)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 16), (94, 40), (92, 56, 1), (84, 44), (76, 30)]),
             L(ell(66, 8, 4, 3.6), 'bead', 'f', ln=True), strand([(64, 10), (62, 40), (60, 66)], 'deep', 'f', 1.2),
             L(outline([(56, 78), (66, 78), (66, 84), (56, 84)]), 'band', 'f', ln=True), L(outline([(58, 84), (64, 84), (62, 106, 1)]), WHITE, 'f', ln=True)],
    'back': [L(outline([(14, 86), (8, 50), (14, 20), (32, 4), (50, 0), (68, 4), (86, 20), (92, 50), (88, 86), (76, 92, 1), (66, 86), (50, 94, 1), (34, 86), (24, 92, 1)])),
             L(outline([(56, 4), (84, 18), (92, 50), (88, 84), (62, 88)]), 'shade', 'b', False),
             L(ell(34, 14, 4.4, 4), 'bead', 'f', ln=True), L(ell(66, 14, 4.4, 4), 'bead', 'f', ln=True)],
}

# Yang: pelo verde azulado peinado hacia arriba, con dos puntas abiertas hacia fuera a los lados como orejas y un flequillo
# corto de mechones; sonrisa amable
CHARS['yang'] = {
    'body': 'normal', 'pal': pal('#3a9a98', '#fcdcbc', iris='#1e1414'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 74), (10, 54), (-6, 56, 1), (4, 40), (10, 16), (-2, -6, 1), (24, 4), (50, -2), (76, 4), (102, -6, 1), (90, 16), (96, 40), (106, 56, 1),
                         (90, 54), (84, 74), (80, 56), (20, 56)])),
              L(outline([(60, 2), (86, 14), (96, 44), (88, 66), (78, 40)]), 'shade', 'b', False),
              fringe([(12, 62), (14, 40), (26, 20), (50, 12), (74, 20), (86, 40), (88, 62), (80, 54), (74, 62, 1), (68, 50), (60, 58, 1), (54, 46), (46, 58, 1),
                      (40, 46), (32, 58, 1), (26, 48), (20, 60, 1)]),
              L(outline([(30, 20), (50, 14), (40, 26)]), 'light', 'f', False)],
    'side': [L(outline([(54, 60), (60, 48), (82, 50), (94, 36), (88, 14), (70, 0), (52, -2), (22, -30, 1), (28, 0), (10, 16), (4, 40), (-12, 64, 1), (8, 62),
                        (16, 80), (30, 78), (44, 70)])),
             L(outline([(4, 40), (24, 44), (26, 72), (8, 66)]), 'shade', 'b', False),
             fringe([(66, 4), (90, 18), (96, 42), (92, 58, 1), (84, 44), (76, 32)])],
    'back': [L(outline([(16, 80), (8, 60), (-10, 62, 1), (2, 44), (8, 16), (-6, -10, 1), (24, 4), (50, -2), (76, 4), (106, -10, 1), (92, 16), (98, 44), (110, 62, 1),
                        (92, 60), (84, 80), (60, 88), (50, 96, 1), (40, 88)])),
             L(outline([(56, 4), (88, 14), (98, 48), (86, 78), (62, 86)]), 'shade', 'b', False),
             strand([(36, 30), (40, 60), (36, 80)], 'deep', 'b', 1.0), strand([(64, 30), (60, 60), (64, 80)], 'deep', 'b', 1.0)],
}
