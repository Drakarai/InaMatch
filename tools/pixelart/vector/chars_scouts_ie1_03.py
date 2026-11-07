"""Ojeadores de IE1 (scouts-ie1), tanda 03: dibujados a partir de su retrato de Victory Road (no tienen modelo 3D en la
enciclopedia); claves 'scouts-ie1:<id>'. El perfil y la espalda se deducen del peinado del retrato."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars import dread, longhair, messy  # noqa: F401
from chars_vr_nikogawa import crop
from heads import quad  # noqa: F401

K = 'scouts-ie1:'
WHITE = (250, 250, 250, 255)
BLACK = (24, 18, 20, 255)
PINK = (238, 140, 140, 255)
LIP = (200, 96, 90, 255)


def fr(pts, c='mid'):
    """Mechón o flequillo por delante de la cara."""
    return L(outline(pts), c, 'f')


def skull():
    """Cabeza rapada o calva de frente: la bóveda del cráneo por encima de la cara."""
    return L(blob([(18, 56), (16, 34), (28, 14), (50, 6), (72, 14), (84, 34), (82, 56)], 8), 'skin')


def bowl(view, top=4, side=90, nape=96, w=0, c='mid'):
    """Melena en casco que tapa las orejas (hasta side de frente y nape de espaldas)."""
    if view == 'front':
        return [L(outline([(14 - w * 0.5, side), (7 - w, 62), (10 - w, 32), (28, 10 + top), (50, top), (72, 10 + top), (90 + w, 32), (93 + w, 62), (86 + w * 0.5, side),
                           (82, 60), (18, 60)]), c),
                L(outline([(60, top + 4), (80, 14 + top), (91 + w, 36), (92 + w, 62), (86, side - 4), (82, 50)]), 'shade', 'b', False)]
    if view == 'side':
        return [L(outline([(80, 56), (88, 40), (82, 16), (60, top - 2), (32, top + 2), (12, 16), (2 - w, 42), (2 - w, 70), (8, nape - 4), (28, nape), (44, nape - 4), (56, 84),
                           (62, 62), (72, 58)]), c),
                L(outline([(4 - w, 44), (34, 48), (52, 66), (50, 84), (30, nape - 2), (8, nape - 6)]), 'shade', 'b', False)]
    return [L(outline([(10 - w * 0.5, nape - 2), (5 - w, 62), (8 - w, 32), (26, 10 + top), (50, top + 2), (74, 10 + top), (92 + w, 32), (95 + w, 62), (90 + w * 0.5, nape - 2),
                       (70, nape + 2), (50, nape + 3), (30, nape + 2)]), c),
            L(outline([(58, top + 6), (80, 16 + top), (93 + w, 40), (93 + w, 64), (88, nape - 2), (66, nape + 2), (62, 50)]), 'shade', 'b', False)]


def eyes_custom(kind, ey=75, sep=14, c=BLACK):
    """Ojos dibujados como capas: 'dots' (dos puntos negros), 'squint' (rayitas ^ de felicidad), 'wave' (~)."""
    out = []
    for cx, s in ((50 - sep, 1), (50 + sep, -1)):
        if kind == 'dots':
            out.append(L(ell(cx, ey, 3.0, 3.6), c, 'f', False))
            out.append(L(ell(cx - 0.8, ey - 1.2, 0.9, 0.9), WHITE, 'f', False))
        elif kind == 'squint':
            out.append(L(quad((cx - 6, ey + 2), (cx, ey - 4), (cx + 6, ey + 2)), c, 'f', False, False, 2.2))
        elif kind == 'wave':
            out.append(L([(cx - 6, ey + 1), (cx - 3, ey - 2), (cx, ey + 1), (cx + 3, ey - 2), (cx + 6, ey + 1)], c, 'f', False, False, 2.0))
    return out


def side_eye_custom(kind, ey=75, c=BLACK):
    if kind == 'dots':
        return [L(ell(81, ey, 2.4, 3.4), c, 'f', False)]
    if kind == 'squint':
        return [L(quad((76, ey + 2), (80, ey - 3), (85, ey + 1)), c, 'f', False, False, 2.2)]
    return [L([(76, ey + 1), (79, ey - 2), (82, ey + 1), (85, ey - 2)], c, 'f', False, False, 2.0)]


def blush(y=86, dx=22, r=4.6):
    return [L(ell(50 - dx, y, r, r * 0.75), PINK, 'f', False), L(ell(50 + dx, y, r, r * 0.75), PINK, 'f', False)]


def thick_brows(y=63, c='deep', h=3.6, sep=14, tilt=0.0, w=12):
    out = []
    for cx, s in ((50 - sep, 1), (50 + sep, -1)):
        x0, x1 = cx - s * w * 0.55, cx + s * w * 0.5
        pts = [(x0, y + 1 - tilt * 2), (cx, y - h * 0.6), (x1, y + tilt * 2), (x1, y + h * 0.7 + tilt * 2), (cx, y + h * 0.5), (x0, y + h * 0.6 - tilt * 2)]
        out.append(L(blob(pts, 6), c, 'f', False))
    return out


def side_brow(y=63, c='deep', h=3.6, tilt=0.0):
    return [L(blob([(72, y + 1 - tilt), (78, y - h * 0.6), (86, y + tilt), (86, y + h * 0.7 + tilt), (78, y + h * 0.5), (72, y + h * 0.6)], 6), c, 'f', False)]


# ---------------------------------------------------------------------------------------------------------- tanda 03

# Cameron Mann: melena en casco gris lila que tapa las orejas, con un mechón azul marino que baja de la coronilla al ojo
# derecho; ojos blancos enfadados y boca torcida
CHARS[K + 'cameron-mann'] = {
    'body': 'normal', 'pal': pal('#82789a', '#f6c896', iris='#2a2030', streak='#2a2444'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 92, 'ears': False,
             'hairline': [(12, 92), (15, 70), (20, 58), (34, 54), (50, 57), (66, 54), (80, 58), (85, 70), (88, 92)]},
    'front': bowl('front', side=94) + [fr([(50, 4), (58, 22), (62, 46), (60, 66, 1), (54, 46), (46, 18)], 'streak')],
    'side': bowl('side', nape=94) + [L(outline([(60, 0), (78, 14), (86, 34), (84, 50, 1), (76, 30), (62, 12)]), 'streak', 'b', False)],
    'back': bowl('back', nape=96),
}

# Cardin Hands: melena rubio platino ondulada con raya en medio, que le cae ondulando hasta la mandíbula y tapa las
# orejas; ojos blancos enfadados y media sonrisa
CHARS[K + 'cardin-hands'] = {
    'body': 'normal', 'pal': pal('#efe2a4', '#f2b878', iris='#2a2020'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'ears': False,
             'hairline': [(14, 96), (16, 60), (28, 44), (44, 38), (50, 42), (56, 38), (72, 44), (84, 60), (86, 96)]},
    'front': [L(outline([(12, 106), (6, 94), (10, 82), (4, 68), (8, 52), (4, 38), (14, 18), (32, 6), (50, 4), (68, 6), (86, 18), (96, 38), (92, 52), (96, 68),
                         (90, 82), (94, 94), (88, 106), (82, 96), (82, 60), (18, 60), (18, 96)])),
              L(outline([(60, 6), (84, 18), (94, 38), (90, 54), (94, 70), (88, 84), (90, 100), (84, 96), (82, 60), (74, 30)]), 'shade', 'b', False),
              strand([(50, 6), (50, 40)], 'deep', 'b', 1.2), strand([(30, 16), (20, 36), (26, 54)], 'deep', 'b', 1.0),
              strand([(70, 16), (80, 36), (74, 54)], 'deep', 'b', 1.0), strand([(10, 70), (14, 84), (10, 96)], 'deep', 'b', 1.0),
              strand([(90, 70), (86, 84), (90, 96)], 'deep', 'b', 1.0)],
    'side': [L(outline([(80, 50), (88, 36), (80, 14), (58, 2), (32, 4), (12, 18), (2, 42), (6, 60), (0, 76), (6, 92), (4, 106, 1), (18, 100), (34, 108, 1), (44, 98),
                        (54, 92), (56, 76), (62, 60), (72, 56)])),
             L(outline([(4, 46), (30, 50), (52, 66), (50, 90), (34, 104), (8, 98)]), 'shade', 'b', False),
             strand([(60, 6), (76, 22), (84, 40)], 'deep', 'b', 1.0), strand([(16, 60), (22, 80), (16, 98)], 'deep', 'b', 1.0)],
    'back': [L(outline([(12, 108, 1), (6, 92), (10, 80), (4, 66), (8, 50), (4, 36), (16, 16), (34, 6), (50, 4), (66, 6), (84, 16), (96, 36), (92, 50), (96, 66),
                        (90, 80), (94, 92), (88, 108, 1), (76, 102), (64, 110, 1), (50, 102), (36, 110, 1), (24, 102)])),
             L(outline([(56, 6), (84, 18), (94, 40), (92, 64), (92, 90), (86, 106), (70, 104), (64, 60)]), 'shade', 'b', False),
             strand([(50, 6), (50, 60)], 'deep', 'b', 1.2), strand([(28, 20), (22, 50), (28, 80), (22, 100)], 'deep', 'b', 1.0),
             strand([(72, 20), (78, 50), (72, 80), (78, 100)], 'deep', 'b', 1.0)],
}

# Carey Bean: piel morena, rastas cortas castaño oscuro sobre la cabeza que cuelgan a los lados por debajo de las orejas,
# y una rasta larga que sale de la coronilla arqueada hacia la derecha; ojos redondos enormes y sonrisa de dientes con labios
CHARS[K + 'carey-bean'] = {
    'body': 'normal', 'pal': pal('#3a2418', '#8a5434', iris='#1a1210', shade='#2a180e', deep='#1c100a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'none', 'mouth_y': 92,
             'hairline': [(14, 60), (22, 48), (36, 44), (50, 46), (62, 42), (78, 46), (86, 60)]},
    'front': [L(outline([(16, 62), (12, 38), (22, 18), (40, 8), (60, 8), (78, 18), (88, 38), (84, 62), (76, 46), (24, 46)])),
              L(rope((58, 10), (80, -8), (100, 2), 6)),
              *dread((18, 64), (6, 104), 3.4), *dread((22, 70), (16, 110), 3.4), *dread((82, 64), (94, 104), 3.4), *dread((78, 70), (86, 110), 3.4),
              strand([(30, 16), (34, 40)], 'deep', 'b', 1.0), strand([(46, 10), (46, 40)], 'deep', 'b', 1.0), strand([(64, 12), (62, 40)], 'deep', 'b', 1.0),
              L(blob([(34, 88), (50, 86), (66, 88), (64, 98), (50, 106), (36, 98)], 6), (120, 62, 40, 255), 'f', False),
              L(blob([(38, 89), (50, 88), (62, 89), (60, 97), (50, 102), (40, 97)], 6), WHITE, 'f', False, True),
              L([(39, 94), (61, 94)], OUTC, 'f', False, False, 0.8)],
    'side': [L(outline([(78, 50), (86, 36), (78, 14), (58, 4), (32, 6), (12, 18), (4, 40), (8, 62), (22, 66), (40, 60), (56, 56), (68, 54)])),
             L(rope((58, 8), (74, -12), (96, -2), 6)),
             *dread((14, 60), (2, 100), 3.4), *dread((26, 62), (20, 104), 3.4), *dread((38, 60), (40, 100), 3.4),
             L(blob([(78, 88), (88, 86), (90, 96), (82, 102)], 6), WHITE, 'f', False, True)],
    'back': [L(outline([(14, 70), (10, 40), (22, 18), (40, 8), (60, 8), (78, 18), (90, 40), (86, 70), (50, 76)])),
             L(rope((56, 10), (78, -8), (98, 2), 6)),
             *dread((16, 66), (6, 104), 3.4), *dread((30, 72), (26, 110), 3.4), *dread((50, 74), (50, 110), 3.4), *dread((70, 72), (74, 110), 3.4),
             *dread((84, 66), (94, 104), 3.4)],
}

# Carey Ginu: grandullón de cara redonda con papada; pelo azul marino en casquete con flequillo recto y alto, lados cortos;
# dos cejas redondas como puntos, ojos cerrados de felicidad en ondas, mofletes rosas y labios rojos
CHARS[K + 'carey-ginu'] = {
    'body': 'corpulento', 'pal': pal('#2c4262', '#f6c08a', shade='#22344e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': [(14, 56), (18, 44), (30, 40), (50, 39), (70, 40), (82, 44), (86, 56)],
             'face_front': blob([(16, 48), (50, 32), (84, 48), (90, 76), (88, 98), (72, 112), (50, 116), (28, 112), (12, 98), (10, 76)])},
    'front': [L(outline([(17, 58), (14, 32), (24, 12), (50, 4), (76, 12), (86, 32), (83, 58), (80, 42), (20, 42)])),
              L(outline([(60, 6), (78, 14), (86, 32), (84, 52), (78, 40)]), 'shade', 'b', False),
              L(ell(36, 60, 3.6, 4.0), (52, 74, 110, 255), 'f', False), L(ell(64, 60, 3.6, 4.0), (52, 74, 110, 255), 'f', False),
              *eyes_custom('wave', 75), *blush(86, 24, 5.4),
              L(blob([(44, 96), (50, 94), (56, 96), (50, 100)], 6), LIP, 'f', False, True),
              L(quad((34, 108), (50, 114), (66, 108)), (200, 140, 100, 255), 'f', False, False, 1.0)],
    'side': [L(outline([(80, 44), (86, 30), (76, 10), (52, 2), (28, 6), (10, 20), (4, 44), (8, 66), (22, 74), (34, 68), (40, 56), (60, 46)])),
             L(outline([(5, 44), (30, 48), (38, 58), (30, 70), (10, 66)]), 'shade', 'b', False),
             L(ell(80, 60, 2.6, 3.4), (52, 74, 110, 255), 'f', False), *side_eye_custom('wave', 75),
             L(ell(80, 86, 3.6, 2.8), PINK, 'f', False), L(ell(82, 95, 2.4, 1.8), LIP, 'f', False)],
    'back': crop('back', top=4, nape=80),
}

# Carey Vanpark: pelo corto verde agua claro, revuelto, con un remolino de punta en la coronilla, mechones que le caen por la
# frente hasta los ojos y puntas de pinchos sobre las orejas; ojos entornados de dormido y media sonrisa
CHARS[K + 'carey-vanpark'] = {
    'body': 'normal', 'pal': pal('#9ec8c6', '#f0ae6c', iris='#2a2020', shade='#7aa8a8', deep='#5a8888'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'nose_side': (88, 84, 2),
             'hairline': [(14, 66), (18, 58), (28, 64), (34, 56), (44, 66), (52, 56), (60, 64), (68, 56), (76, 62), (82, 56), (86, 66)]},
    'front': [L(outline([(16, 70), (8, 74, 1), (10, 60), (2, 54, 1), (10, 44), (12, 26), (26, 10), (50, 4), (60, 4), (64, -8, 1), (70, 6), (82, 14), (90, 30), (90, 44),
                         (98, 54, 1), (90, 60), (92, 74, 1), (84, 70), (80, 50), (20, 50)])),
              L(outline([(60, 6), (82, 16), (90, 34), (88, 56), (80, 44)]), 'shade', 'b', False),
              strand([(30, 14), (26, 40)], 'deep', 'b', 1.0), strand([(50, 8), (46, 40)], 'deep', 'b', 1.0), strand([(70, 12), (72, 40)], 'deep', 'b', 1.0),
              L([(28, 72), (44, 74)], OUTC, 'f', False, False, 3.0), L([(56, 74), (72, 72)], OUTC, 'f', False, False, 3.0)],
    'side': [L(outline([(78, 58), (84, 44), (86, 28), (76, 10), (60, 2), (62, -8, 1), (52, 0), (30, 4), (12, 18), (4, 40), (0, 54, 1), (8, 60), (6, 74, 1), (18, 72),
                        (28, 80, 1), (34, 70), (42, 60), (56, 56), (66, 58)])),
             L(outline([(4, 42), (30, 48), (40, 60), (32, 72), (12, 70)]), 'shade', 'b', False),
             L([(74, 72), (86, 73)], OUTC, 'f', False, False, 3.0)],
    'back': [L(outline([(16, 82), (8, 78, 1), (12, 64), (4, 56, 1), (10, 44), (12, 26), (26, 10), (44, 4), (50, -8, 1), (56, 4), (74, 10), (88, 26), (90, 44),
                        (96, 56, 1), (88, 64), (92, 78, 1), (84, 82), (66, 86), (50, 88), (34, 86)])),
             L(outline([(58, 6), (80, 16), (90, 40), (88, 64), (84, 82), (66, 86), (62, 50)]), 'shade', 'b', False)],
}

# Carl Gnu: calvo de cabeza alargada, piel tostada; cejas negras gruesas y enfadadas, ojos verde azulado, boca fruncida y
# orejas grandes
CHARS[K + 'carl-gnu'] = {
    'body': 'normal', 'pal': pal('#c8864e', '#d8955a', iris='#4a9a98'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'frown', 'mouth_y': 94, 'big_ears': 2, 'hairline': False, 'nose': (50, 84, 2.6)},
    'front': [skull(), *thick_brows(63, BLACK, 4.0, 14, 1.0, 13)],
    'side': [*side_brow(63, BLACK, 4.0, 1.0)],
    'back': [],
}

# Carl Nivor (portero): adulto de piel morena grisácea; pelo rubio dorado peinado hacia atrás con dos mechones largos que le
# caen por los lados hasta el cuello; cejas amarillas, ojos blancos afilados, nariz marcada y media sonrisa
CHARS[K + 'carl-nivor'] = {
    'body': 'normal', 'pal': pal('#e8bc30', '#a8866a', iris='#3a3020', shade='#c89a20', deep='#a07a14'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'nose': (50, 85, 2.6),
             'hairline': [(14, 64), (18, 46), (30, 38), (50, 34), (70, 38), (82, 46), (86, 64)]},
    'front': [L(outline([(12, 104), (8, 84), (12, 60), (10, 36), (22, 14), (44, 4), (56, 6), (78, 12), (90, 34), (88, 60), (92, 84), (88, 104), (82, 90), (82, 56),
                         (18, 56), (18, 90)])),
              L(outline([(58, 6), (80, 14), (90, 36), (88, 60), (90, 96), (84, 88), (80, 50)]), 'shade', 'b', False),
              strand([(34, 10), (28, 30), (24, 50)], 'deep', 'b', 1.0), strand([(50, 6), (46, 34)], 'deep', 'b', 1.0), strand([(66, 10), (74, 30), (78, 50)], 'deep', 'b', 1.0),
              *thick_brows(64, (226, 186, 40, 255), 3.0, 14, 1.2, 12)],
    'side': [L(outline([(80, 40), (78, 14), (56, 2), (30, 4), (12, 18), (4, 42), (4, 70), (10, 96), (8, 108, 1), (22, 100), (30, 104, 1), (36, 92), (38, 70), (42, 58),
                        (56, 48), (70, 40)])),
             L(outline([(5, 46), (30, 48), (38, 66), (30, 96), (12, 98)]), 'shade', 'b', False),
             strand([(70, 10), (50, 14), (24, 26)], 'deep', 'b', 1.0), strand([(64, 30), (40, 30), (16, 44)], 'deep', 'b', 1.0),
             *side_brow(64, (226, 186, 40, 255), 3.0, 1.2)],
    'back': [L(outline([(12, 106, 1), (8, 84), (10, 60), (8, 36), (20, 14), (42, 4), (58, 4), (80, 14), (92, 36), (90, 60), (92, 84), (88, 106, 1), (72, 96),
                        (60, 104, 1), (50, 94), (40, 104, 1), (28, 96)])),
             L(outline([(56, 6), (80, 16), (92, 40), (90, 70), (86, 100), (70, 96), (62, 50)]), 'shade', 'b', False),
             strand([(50, 6), (50, 90)], 'deep', 'b', 1.0), strand([(30, 12), (24, 60), (26, 96)], 'deep', 'b', 1.0), strand([(70, 12), (76, 60), (74, 96)], 'deep', 'b', 1.0)],
}

# Carl Penter: pelo verde hierba peinado alto hacia un lado, con los lados cortos y un mechón en horquilla que le cae por la
# frente; cejas verdes gruesas, ojos pequeños redondos, cara alargada y media sonrisa
CHARS[K + 'carl-penter'] = {
    'body': 'normal', 'pal': pal('#76b040', '#d89a62', iris='#1a1410', shade='#5a9030', deep='#3e7020'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'nose': (52, 84, 2.4),
             'hairline': [(14, 60), (18, 48), (30, 42), (44, 40), (56, 42), (70, 40), (82, 46), (86, 60)]},
    'front': [L(outline([(16, 62), (12, 40), (16, 18), (32, 4), (54, -2), (76, 4), (88, 18), (88, 40), (84, 62), (80, 46), (20, 46)])),
              L(outline([(56, 0), (78, 6), (88, 22), (86, 50), (78, 32), (66, 14)]), 'shade', 'b', False),
              strand([(26, 12), (50, 4), (76, 8)], 'deep', 'b', 1.0), strand([(20, 30), (46, 18), (80, 24)], 'deep', 'b', 1.0),
              fr([(34, 30), (42, 40), (46, 56, 1), (44, 44), (40, 54, 1), (38, 42), (30, 34)]),
              *thick_brows(64, 'mid', 3.6, 14, 0.6, 12)],
    'side': [L(outline([(80, 48), (86, 34), (84, 16), (68, 2), (44, -4), (22, 2), (8, 20), (4, 44), (10, 64), (24, 70), (36, 62), (44, 54), (62, 48)])),
             L(outline([(5, 44), (30, 46), (40, 56), (30, 66), (10, 62)]), 'shade', 'b', False),
             strand([(80, 18), (56, 4), (24, 6)], 'deep', 'b', 1.0), strand([(78, 34), (50, 20), (16, 28)], 'deep', 'b', 1.0),
             *side_brow(64, 'mid', 3.6, 0.6)],
    'back': crop('back', top=0, nape=80),
}


def side_curl(cx, cy, r=9, c='mid'):
    """Rulo enrollado (peluca de abogado): bola con la espiral marcada."""
    return [L(ell(cx, cy, r, r * 1.1)), strand([(cx - r * 0.5, cy - r * 0.3), (cx, cy - r * 0.6), (cx + r * 0.5, cy), (cx, cy + r * 0.5), (cx - r * 0.3, cy)], 'deep', 'b', 1.0)]


def tri_nose(y=86, c=BLACK, w=4):
    return [L([(50 - w, y - 2), (50 + w, y - 2), (50, y + 3)], c, 'f', False)]


def lashes_out(ey=75, sep=14, c=OUTC):
    """Pestañas de punta en la esquina de fuera de cada ojo."""
    out = []
    for cx, s in ((50 - sep, 1), (50 + sep, -1)):
        x = cx - s * 7
        out.append(L([(x, ey - 4), (x - s * 4, ey - 8)], c, 'f', False, False, 1.4))
        out.append(L([(x + s * 1, ey - 5), (x - s * 2, ey - 10)], c, 'f', False, False, 1.4))
    return out


# Carl Sacks: señor calvo con cuatro pelos lila grisáceo peinados sobre la coronilla y rulos enrollados encima de las
# orejas, como una peluca de juez; ojos pequeños redondos, nariz grande y boca fruncida
CHARS[K + 'carl-sacks'] = {
    'body': 'corpulento', 'pal': pal('#a88a9c', '#f6be88', iris='#1a1210', shade='#8a6e80', deep='#6a5262'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'hairline': False, 'nose': (50, 85, 3.6), 'ears': False,
             'face_front': blob([(16, 50), (50, 34), (84, 50), (90, 76), (86, 98), (68, 110), (50, 112), (32, 110), (14, 98), (10, 76)])},
    'front': [skull(), L(blob([(24, 30), (36, 18), (50, 14), (64, 18), (76, 30), (64, 26), (50, 24), (36, 26)], 6), 'light', 'b', False),
              strand([(50, 14), (50, 26)], 'shade', 'b', 1.0),
              *side_curl(14, 58, 8), *side_curl(12, 74, 8), *side_curl(86, 58, 8), *side_curl(88, 74, 8)],
    'side': [L(blob([(30, 24), (52, 17), (74, 24), (54, 25)], 6), 'light', 'b', False), *side_curl(34, 50, 9), *side_curl(28, 66, 9), *side_curl(42, 64, 8)],
    'back': [L(blob([(26, 32), (50, 21), (74, 32), (50, 28)], 6), 'light', 'b', False),
             *side_curl(16, 58, 9), *side_curl(14, 76, 9), *side_curl(84, 58, 9), *side_curl(86, 76, 9), *side_curl(32, 80, 9), *side_curl(50, 82, 9), *side_curl(68, 80, 9)],
}

# Carson Haynes: pelo verde oscuro engominado hacia arriba en una punta, con rayas de peinado y los lados cortos, y unas
# puntas que se abren por debajo de las orejas en la nuca; ojos redondos blancos, cejas enfadadas con pestañas, nariz de
# triángulo y sonrisa
CHARS[K + 'carson-haynes'] = {
    'body': 'normal', 'pal': pal('#2a5a3e', '#d8985a', iris='#1a1210', shade='#20462e', deep='#163420'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93,
             'hairline': [(14, 60), (18, 44), (30, 36), (44, 30), (50, 34), (56, 30), (70, 36), (82, 44), (86, 60)]},
    'front': [L(outline([(16, 64), (12, 42), (18, 20), (34, 4), (50, -8, 1), (66, 4), (82, 20), (88, 42), (84, 64), (80, 40), (20, 40)])),
              L(outline([(54, -4), (66, 4), (82, 20), (88, 44), (82, 48), (70, 18)]), 'shade', 'b', False),
              L(outline([(18, 86), (6, 98, 1), (14, 84)]), 'mid', 'b'), L(outline([(82, 86), (94, 98, 1), (86, 84)]), 'mid', 'b'),
              strand([(50, -4), (40, 14), (30, 34)], 'deep', 'b', 1.0), strand([(50, -4), (60, 14), (70, 34)], 'deep', 'b', 1.0),
              strand([(50, -4), (50, 30)], 'deep', 'b', 1.0), *tri_nose(86), *lashes_out(66, 14)],
    'side': [L(outline([(80, 46), (86, 30), (74, 8), (56, -6, 1), (40, 0), (18, 10), (6, 30), (4, 56), (8, 76), (2, 94, 1), (16, 82), (22, 96, 1), (30, 78), (40, 62),
                        (50, 54), (66, 48)])),
             L(outline([(5, 42), (32, 46), (40, 60), (30, 78), (10, 76)]), 'shade', 'b', False),
             strand([(56, -4), (40, 14), (16, 30)], 'deep', 'b', 1.0), strand([(70, 10), (50, 24), (26, 44)], 'deep', 'b', 1.0)],
    'back': [L(outline([(16, 80), (6, 96, 1), (12, 70), (10, 40), (22, 16), (40, 2), (50, -8, 1), (60, 2), (78, 16), (90, 40), (88, 70), (94, 96, 1), (84, 80),
                        (70, 92, 1), (60, 82), (50, 94, 1), (40, 82), (30, 92, 1)])),
             L(outline([(56, 0), (78, 16), (90, 42), (88, 70), (92, 92), (70, 88), (62, 50)]), 'shade', 'b', False),
             strand([(50, -4), (50, 80)], 'deep', 'b', 1.0), strand([(36, 8), (26, 40), (24, 76)], 'deep', 'b', 1.0), strand([(64, 8), (74, 40), (76, 76)], 'deep', 'b', 1.0)],
}

# Carter Nightly: melena azul marino ondulada hasta los hombros, con raya en medio y ondas a los lados de la cara (las
# orejas asoman); cejas onduladas gruesas, ojos entornados y boca seria
CHARS[K + 'carter-nightly'] = {
    'body': 'normal', 'pal': pal('#2e4470', '#f6c48a', iris='#2a2030', shade='#22335a', deep='#182444'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 93,
             'hairline': [(12, 70), (16, 54), (26, 44), (40, 40), (48, 44), (52, 44), (60, 40), (74, 44), (84, 54), (88, 70)]},
    'front': [L(outline([(10, 110), (2, 96), (8, 84), (0, 70), (8, 56), (4, 38), (16, 16), (34, 4), (50, 6), (66, 4), (84, 16), (96, 38), (92, 56), (100, 70), (92, 84),
                         (98, 96), (90, 110), (80, 100), (84, 84), (82, 56), (18, 56), (16, 84), (20, 100)])),
              L(outline([(60, 6), (84, 18), (94, 40), (90, 58), (96, 72), (90, 86), (94, 100), (86, 104), (82, 50)]), 'shade', 'b', False),
              strand([(50, 6), (48, 20), (52, 40)], 'deep', 'b', 1.2), strand([(28, 12), (18, 30), (24, 46)], 'deep', 'b', 1.0),
              strand([(72, 12), (82, 30), (76, 46)], 'deep', 'b', 1.0), strand([(8, 64), (14, 80), (8, 96)], 'deep', 'b', 1.0), strand([(92, 64), (86, 80), (92, 96)], 'deep', 'b', 1.0),
              L([(24, 64), (30, 61), (36, 64), (42, 62)], 'mid', 'f', False, False, 3.4), L([(58, 62), (64, 64), (70, 61), (76, 64)], 'mid', 'f', False, False, 3.4)],
    'side': [L(outline([(80, 50), (88, 36), (80, 14), (58, 2), (32, 4), (12, 18), (2, 40), (6, 56), (-2, 72), (6, 88), (0, 104), (12, 112, 1), (24, 102), (36, 110, 1),
                        (42, 96), (36, 82), (40, 64), (52, 56), (66, 52)])),
             L(outline([(4, 46), (30, 50), (38, 70), (34, 96), (12, 104)]), 'shade', 'b', False),
             strand([(70, 10), (80, 30), (84, 44)], 'deep', 'b', 1.0), strand([(12, 60), (18, 80), (12, 100)], 'deep', 'b', 1.0),
             L([(72, 63), (78, 61), (86, 64)], 'mid', 'f', False, False, 3.4)],
    'back': [L(outline([(10, 112, 1), (2, 96), (8, 82), (0, 68), (8, 52), (4, 36), (16, 16), (34, 4), (50, 4), (66, 4), (84, 16), (96, 36), (92, 52), (100, 68), (92, 82),
                        (98, 96), (90, 112, 1), (76, 104), (64, 112, 1), (50, 104), (36, 112, 1), (24, 104)])),
             L(outline([(56, 6), (84, 18), (94, 40), (94, 70), (94, 100), (84, 108), (66, 104), (64, 60)]), 'shade', 'b', False),
             strand([(50, 6), (50, 60)], 'deep', 'b', 1.2), strand([(26, 20), (18, 50), (24, 76), (18, 100)], 'deep', 'b', 1.0),
             strand([(74, 20), (82, 50), (76, 76), (82, 100)], 'deep', 'b', 1.0)],
}

# Casey Novak: gorro de punto verde oliva muy ceñido y, por debajo, mechones esponjosos color crema que se le escapan a los
# lados por encima de las orejas; ojos blancos redondos, cejas enfadadas, nariz de triángulo y sonrisa
CHARS[K + 'casey-novak'] = {
    'body': 'normal', 'pal': pal('#d8ceb0', '#f6c48a', iris='#1a1210', shade='#b8ae90', cap='#5a5c2e', cap_d='#46481e'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': False},
    'front': [L(blob([(6, 70), (0, 56), (8, 44), (20, 46), (24, 60), (18, 76)], 6)), L(blob([(94, 70), (100, 56), (92, 44), (80, 46), (76, 60), (82, 76)], 6)),
              strand([(6, 56), (14, 60), (10, 68)], 'shade', 'b', 1.0), strand([(94, 56), (86, 60), (90, 68)], 'shade', 'b', 1.0),
              L(outline([(16, 58), (12, 34), (22, 10), (50, 0), (78, 10), (88, 34), (84, 58), (70, 52), (50, 50), (30, 52)]), 'cap', 'f'),
              L(outline([(60, 2), (80, 12), (88, 36), (84, 56), (76, 34)]), 'cap_d', 'f', False), *tri_nose(86)],
    'side': [L(blob([(32, 74), (22, 66), (26, 52), (40, 50), (48, 60), (42, 72)], 6)), strand([(28, 58), (36, 62), (32, 70)], 'shade', 'b', 1.0),
             L(outline([(84, 54), (88, 36), (80, 14), (58, 0), (32, 2), (12, 16), (4, 40), (8, 60), (22, 66), (40, 58), (60, 54)]), 'cap', 'f'),
             L(outline([(6, 40), (30, 44), (40, 56), (24, 64), (8, 60)]), 'cap_d', 'f', False)],
    'back': [L(blob([(8, 74), (2, 60), (10, 48), (22, 50), (24, 66), (18, 80)], 6)), L(blob([(92, 74), (98, 60), (90, 48), (78, 50), (76, 66), (82, 80)], 6)),
             L(blob([(26, 80), (50, 72), (74, 80), (66, 92), (50, 94), (34, 92)], 6)),
             L(outline([(14, 70), (10, 40), (22, 12), (50, 0), (78, 12), (90, 40), (86, 70), (50, 76)]), 'cap', 'f'),
             L(outline([(58, 2), (80, 14), (90, 42), (86, 68), (62, 74)]), 'cap_d', 'f', False)],
}

# Cash Barganier: piel morena, pelo rosa corto y alborotado, y una máscara de luchador crema con el borde naranja que le tapa
# la parte de arriba de la cara, con los agujeros de los ojos azul grisáceo y lunares naranjas; media sonrisa
CHARS[K + 'cash-barganier'] = {
    'body': 'normal', 'pal': pal('#d27484', '#c88850', shade='#b25a6a', deep='#8e4252', mask='#f2e6c8', mask_o='#e0702a', lens='#7aa0b0'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': [(14, 60), (20, 48), (32, 42), (50, 40), (68, 42), (80, 48), (86, 60)]},
    'front': [*messy('front', amp=7, n=10, seed=3, lo=60),
              L(blob([(12, 66), (20, 56), (36, 62), (50, 60), (64, 62), (80, 56), (88, 66), (86, 82), (74, 90), (50, 94), (26, 90), (14, 82)], 6), 'mask_o', 'f', True),
              L(blob([(17, 66), (22, 60), (36, 66), (50, 64), (64, 66), (78, 60), (83, 66), (80, 76), (64, 76), (50, 84), (36, 76), (20, 76)], 6), 'mask', 'f', False),
              L(blob([(26, 72), (36, 70), (44, 76), (38, 82), (28, 80)], 6), 'lens', 'f', False, True), L(blob([(74, 72), (64, 70), (56, 76), (62, 82), (72, 80)], 6), 'lens', 'f', False, True),
              L(ell(50, 74, 3, 3), 'mask_o', 'f', False), L(ell(36, 64, 2, 2), 'mask_o', 'f', False), L(ell(64, 64, 2, 2), 'mask_o', 'f', False)],
    'side': [*messy('side', amp=7, n=10, seed=3, lo=60),
             L(blob([(50, 66), (70, 58), (88, 62), (90, 80), (84, 90), (60, 86), (52, 76)], 6), 'mask_o', 'f', True),
             L(blob([(56, 68), (72, 62), (86, 66), (86, 78), (70, 80), (58, 76)], 6), 'mask', 'f', False),
             L(blob([(76, 70), (86, 70), (86, 80), (78, 80)], 6), 'lens', 'f', False, True),
             L([(52, 72), (30, 68)], 'mask_o', 'f', False, False, 3)],
    'back': [*messy('back', amp=7, n=10, seed=3, lo=60), L([(18, 72), (50, 76), (82, 72)], 'mask_o', 'f', False, False, 3.2)],
}

# Cass Crocker: cara alargada, pelo castaño con raya en medio que se levanta en dos cuernos en las esquinas, y patillas;
# ojos entornados de mirada aburrida, dos marcas naranjas como lágrimas bajo los ojos y sonrisa con un colmillo
CHARS[K + 'cass-crocker'] = {
    'body': 'delgado', 'pal': pal('#6a5030', '#d6a466', iris='#2a2020', shade='#54401e', deep='#3e2e14', tear='#e8782a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(14, 66), (18, 50), (30, 42), (44, 40), (50, 46), (56, 40), (70, 42), (82, 50), (86, 66)],
             'face_front': blob([(18, 50), (50, 34), (82, 50), (84, 80), (76, 100), (60, 112), (50, 114), (40, 112), (24, 100), (16, 80)])},
    'front': [L(outline([(16, 70), (12, 40), (10, 10), (8, -10, 1), (26, 6), (50, 4), (74, 6), (92, -10, 1), (90, 10), (88, 40), (84, 70), (80, 50), (20, 50)])),
              L(outline([(60, 6), (76, 6), (90, -6), (88, 40), (84, 62), (78, 40), (70, 20)]), 'shade', 'b', False),
              strand([(50, 6), (50, 44)], 'deep', 'b', 1.2), strand([(30, 10), (24, 40)], 'deep', 'b', 1.0), strand([(70, 10), (76, 40)], 'deep', 'b', 1.0),
              L([(26, 70), (44, 72)], OUTC, 'f', False, False, 2.8), L([(56, 72), (74, 70)], OUTC, 'f', False, False, 2.8),
              L([(32, 80), (34, 88)], 'tear', 'f', False, False, 2.0), L([(68, 80), (66, 88)], 'tear', 'f', False, False, 2.0),
              L([(54, 95), (55, 99), (57, 95)], WHITE, 'f', False)],
    'side': [L(outline([(80, 50), (86, 34), (82, 14), (86, -8, 1), (66, 4), (40, 2), (16, 12), (6, 34), (6, 58), (12, 76), (28, 76), (38, 64), (44, 54), (62, 50)])),
             L(outline([(6, 40), (32, 44), (38, 60), (28, 74), (10, 70)]), 'shade', 'b', False),
             L([(72, 70), (86, 72)], OUTC, 'f', False, False, 2.8), L([(80, 80), (80, 88)], 'tear', 'f', False, False, 2.0)],
    'back': [L(outline([(16, 80), (10, 40), (8, 8), (6, -10, 1), (26, 6), (50, 4), (74, 6), (94, -10, 1), (92, 8), (90, 40), (84, 80), (50, 86)])),
             L(outline([(58, 6), (76, 6), (92, -6), (90, 40), (84, 78), (62, 84)]), 'shade', 'b', False)],
}

# Caz Yewell (portero): sienes rapadas con un tupé azul grisáceo que le baja en cuña por el centro de la cabeza; orejas
# grandes, ojos afilados enfadados, nariz grande y sonrisa de dientes
CHARS[K + 'caz-yewell'] = {
    'body': 'normal', 'pal': pal('#7aa2ba', '#f6c48a', iris='#2a2030', shade='#5e86a0', deep='#466c86'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 94, 'big_ears': 2, 'nose': (50, 84, 3.0), 'hairline': False},
    'front': [skull(), L(outline([(34, 16), (44, 6), (56, 6), (68, 14), (76, 28), (70, 34), (60, 40), (54, 52, 1), (48, 38), (40, 28)]), 'mid', 'b'),
              L(outline([(56, 8), (68, 14), (76, 28), (70, 34), (62, 22)]), 'shade', 'b', False)],
    'side': [L(outline([(86, 46), (88, 30), (78, 14), (60, 8), (42, 12), (28, 22), (48, 22), (66, 26), (78, 36)]), 'mid', 'b')],
    'back': [L(outline([(36, 26), (40, 12), (50, 8), (60, 12), (64, 26), (56, 38), (44, 38)]), 'mid', 'b')],
}

# Char Shumaker: cara ancha y redonda; pelo verde oliva corto con una cinta azul que le cruza la cabeza y un mechón largo
# que le cae por la frente; ojos enfadados con pestañas, nariz chata y boca fruncida
CHARS[K + 'char-shumaker'] = {
    'body': 'corpulento', 'pal': pal('#8a923e', '#f6c48a', iris='#1a1210', shade='#6e7630', deep='#525a20', band='#3a7ab0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'nose': (50, 86, 3.0),
             'hairline': [(12, 70), (14, 54), (24, 46), (40, 44), (60, 44), (76, 46), (86, 54), (88, 70)],
             'face_front': blob([(14, 50), (50, 36), (86, 50), (92, 78), (86, 100), (68, 112), (50, 114), (32, 112), (14, 100), (8, 78)])},
    'front': [L(outline([(10, 74), (6, 48), (14, 22), (32, 8), (50, 4), (68, 8), (86, 22), (94, 48), (90, 74), (84, 56), (16, 56)])),
              L(outline([(60, 6), (84, 20), (92, 46), (88, 66), (80, 44)]), 'shade', 'b', False),
              L(quad((8, 50), (50, 22), (92, 50)) + quad((92, 56), (50, 28), (8, 56)), 'band', 'b', False),
              fr([(40, 28), (52, 38), (54, 56), (50, 72, 1), (48, 54), (40, 40), (30, 34)]), *lashes_out(75, 14)],
    'side': [L(outline([(80, 54), (88, 38), (80, 14), (58, 2), (32, 4), (12, 18), (2, 44), (6, 70), (20, 74), (36, 66), (46, 58), (66, 54)])),
             L(outline([(4, 46), (30, 50), (40, 62), (24, 74), (8, 70)]), 'shade', 'b', False),
             L(quad((86, 40), (50, 10), (8, 34)) + quad((6, 40), (50, 16), (86, 46)), 'band', 'b', False)],
    'back': crop('back', top=2, w=4, nape=84) + [L(quad((6, 50), (50, 30), (94, 50)) + quad((94, 56), (50, 36), (6, 56)), 'band', 'b', False)],
}


def big_grin(y=94, w=14, h=9, c=WHITE):
    """Sonrisa enorme de dientes (boca en D con la fila de dientes)."""
    return [L(blob([(50 - w, y - 2), (50, y - 1), (50 + w, y - 2), (50 + w * 0.7, y + h * 0.7), (50, y + h), (50 - w * 0.7, y + h * 0.7)], 6), (110, 40, 40, 255), 'f', False),
            L(blob([(50 - w + 2, y - 1), (50, y), (50 + w - 2, y - 1), (50 + w * 0.6, y + h * 0.55), (50, y + h * 0.7), (50 - w * 0.6, y + h * 0.55)], 6), c, 'f', False, True),
            L([(50 - w + 3, y + 2.5), (50 + w - 3, y + 2.5)], OUTC, 'f', False, False, 0.8)]


def stache(y=90, w=14, c='mid'):
    """Bigote grueso que cae por los lados de la boca."""
    return L(blob([(50, y - 3), (50 + w * 0.6, y - 4), (50 + w, y + 2), (50 + w * 0.8, y + 8), (50 + w * 0.5, y + 2), (50, y + 1), (50 - w * 0.5, y + 2),
                   (50 - w * 0.8, y + 8), (50 - w, y + 2), (50 - w * 0.6, y - 4)], 6), c, 'f', False, True)


# Charlie Krelborn: piel tostada, pelo corto gris malva de pinchos revueltos en la coronilla y los lados rapados; orejas
# grandes, ojos grandes verde oliva y boca seria
CHARS[K + 'charlie-krelborn'] = {
    'body': 'normal', 'pal': pal('#9a8090', '#c88a50', iris='#7a8a30', shade='#7e6676', deep='#624e5c'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 92, 'big_ears': 2,
             'hairline': [(16, 60), (20, 46), (30, 42), (40, 46), (50, 40), (60, 46), (70, 42), (80, 46), (84, 60)]},
    'front': [L(outline([(18, 62), (14, 40), (12, 26, 1), (22, 22), (24, 6, 1), (36, 14), (44, -2, 1), (52, 10), (62, 0, 1), (66, 14), (80, 10, 1), (78, 24),
                         (90, 28, 1), (86, 40), (82, 62), (78, 46), (22, 46)])),
              L(outline([(58, 6), (66, 14), (80, 10), (78, 24), (88, 30), (84, 52), (76, 34)]), 'shade', 'b', False)],
    'side': [L(outline([(80, 48), (88, 34, 1), (80, 26), (88, 12, 1), (70, 10), (66, -2, 1), (52, 6), (38, -2, 1), (32, 10), (14, 12, 1), (14, 24), (6, 40), (10, 62), (24, 70),
                        (36, 62), (44, 54), (62, 50)])),
             L(outline([(6, 40), (30, 44), (40, 56), (26, 68), (10, 62)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 76), (12, 40), (8, 26, 1), (20, 20), (22, 4, 1), (36, 12), (46, -2, 1), (54, 10), (64, 0, 1), (68, 14), (82, 8, 1), (80, 22), (92, 28, 1),
                        (88, 40), (84, 76), (50, 82)])),
             L(outline([(58, 6), (82, 10), (90, 40), (84, 74), (62, 80)]), 'shade', 'b', False)],
}

# Charlie Shearing: grandullón de cara ancha bajo una melena rosa en forma de seta, con la punta del casquete abierta como un
# sombrero por encima de las orejas; cejas rosas gruesas, ojos blancos pequeños, nariz grande y sonrisa
CHARS[K + 'charlie-shearing'] = {
    'body': 'corpulento', 'pal': pal('#eca29a', '#f2b674', iris='#1a1210', shade='#d0847c', deep='#b26a62'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'nose': (50, 86, 4.2),
             'hairline': [(10, 56), (30, 54), (50, 56), (70, 54), (90, 56)],
             'face_front': blob([(14, 50), (50, 40), (86, 50), (92, 78), (86, 100), (68, 112), (50, 114), (32, 112), (14, 100), (8, 78)])},
    'front': [L(outline([(-8, 60, 1), (0, 40), (14, 14), (36, -2), (50, -4), (64, -2), (86, 14), (100, 40), (108, 60, 1), (80, 56), (50, 58), (20, 56)])),
              L(outline([(58, -2), (86, 14), (100, 40), (106, 58), (84, 54), (78, 30)]), 'shade', 'b', False),
              *[strand([(x, 4 + abs(x - 50) * 0.3), (x + (x - 50) * 0.25, 54)], 'deep', 'b', 1.0) for x in (20, 32, 44, 56, 68, 80)],
              *thick_brows(65, 'mid', 4.0, 15, -0.4, 13)],
    'side': [L(outline([(100, 58, 1), (92, 34), (76, 8), (50, -4), (24, 4), (6, 26), (-6, 58, 1), (20, 56), (50, 56)])),
             L(outline([(-4, 56), (6, 30), (24, 8), (40, 20), (30, 56)]), 'shade', 'b', False),
             *[strand([(x, 2 + abs(x - 50) * 0.2), (x + (x - 50) * 0.2, 54)], 'deep', 'b', 1.0) for x in (20, 40, 60, 80)], *side_brow(65, 'mid', 4.0)],
    'back': [L(outline([(-8, 62, 1), (0, 40), (14, 14), (36, -2), (50, -4), (64, -2), (86, 14), (100, 40), (108, 62, 1), (80, 60), (50, 62), (20, 60)])),
             L(outline([(56, -2), (86, 14), (100, 40), (106, 60), (70, 60)]), 'shade', 'b', False),
             *[strand([(x, 4 + abs(x - 50) * 0.3), (x + (x - 50) * 0.25, 58)], 'deep', 'b', 1.0) for x in (20, 32, 44, 56, 68, 80)]],
}

# Chaz Anover: pelo verde oliva oscuro con pico en la frente, los lados en punta y una cresta de rayas malva claro en lo alto
# como una cebolla; barbilla larga, ojos blancos de puntito, nariz de perro y sonrisa de dientes
CHARS[K + 'chaz-anover'] = {
    'body': 'normal', 'pal': pal('#4a4a28', '#c8925a', iris='#1a1210', shade='#38381c', deep='#262612', crest='#c4a6b6', crest_d='#9a7e8e'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'grin', 'mouth_y': 94, 'nose': (50, 84, 2.6),
             'hairline': [(14, 62), (20, 48), (34, 42), (50, 54), (66, 42), (80, 48), (86, 62)],
             'face_front': blob([(18, 50), (50, 40), (82, 50), (84, 80), (76, 100), (60, 112), (50, 116), (40, 112), (24, 100), (16, 80)])},
    'front': [L(outline([(16, 66), (12, 44), (6, 30, 1), (18, 28), (24, 14), (40, 10), (60, 10), (76, 14), (82, 28), (94, 30, 1), (88, 44), (84, 66), (80, 48), (20, 48)])),
              L(outline([(60, 12), (76, 16), (84, 30), (92, 32), (86, 46), (82, 60), (78, 40)]), 'shade', 'b', False),
              L(blob([(34, 14), (36, -2), (50, -12), (64, -2), (66, 14), (50, 20)], 8), 'crest'),
              *[strand([(x, -6 + abs(x - 50) * 0.5), (x + (x - 50) * 0.1, 16)], 'crest_d', 'b', 1.0) for x in (40, 46, 52, 58)]],
    'side': [L(outline([(80, 50), (86, 34), (78, 18), (56, 12), (30, 12), (12, 22), (2, 42), (6, 64), (22, 72), (36, 62), (44, 54), (62, 50)])),
             L(outline([(4, 42), (30, 46), (38, 58), (24, 70), (8, 64)]), 'shade', 'b', False),
             L(blob([(34, 16), (36, 0), (52, -12), (70, -2), (72, 14), (52, 20)], 8), 'crest'),
             *[strand([(x, -6 + abs(x - 52) * 0.4), (x, 16)], 'crest_d', 'b', 1.0) for x in (42, 50, 58, 64)]],
    'back': [L(outline([(16, 78), (12, 44), (6, 30, 1), (18, 26), (26, 12), (50, 8), (74, 12), (82, 26), (94, 30, 1), (88, 44), (84, 78), (50, 84)])),
             L(outline([(58, 10), (80, 18), (90, 34), (86, 76), (62, 82)]), 'shade', 'b', False),
             L(blob([(34, 14), (36, -2), (50, -12), (64, -2), (66, 14), (50, 20)], 8), 'crest'),
             *[strand([(x, -6 + abs(x - 50) * 0.5), (x, 16)], 'crest_d', 'b', 1.0) for x in (40, 46, 52, 58)]],
}

# Chaz Biggins: pelo verde oliva oscuro con flequillo barrido hacia un lado, un mechón levantado en la coronilla y patillas
# largas; ojos cerrados en "><" de rabia, nariz marrón y dientes apretados
CHARS[K + 'chaz-biggins'] = {
    'body': 'normal', 'pal': pal('#5a6a2c', '#f2b878', shade='#46541e', deep='#323e12'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'nose': (50, 86, 3.0),
             'hairline': [(14, 76), (16, 56), (24, 48), (40, 50), (60, 44), (80, 46), (86, 76)]},
    'front': [L(outline([(15, 80), (12, 50), (4, 40, 1), (14, 30), (30, 18), (54, 12), (68, 6), (72, -6, 1), (76, 6), (86, 2, 1), (82, 14), (88, 30), (86, 80), (80, 50),
                         (20, 50)])),
              L(outline([(60, 12), (82, 16), (88, 34), (86, 70), (78, 44)]), 'shade', 'b', False),
              fr([(8, 40), (20, 32), (42, 30), (66, 34), (54, 38), (36, 40), (22, 46)]),
              L([(28, 70), (40, 75), (28, 80)], BLACK, 'f', False, False, 2.6), L([(72, 70), (60, 75), (72, 80)], BLACK, 'f', False, False, 2.6),
              L([(32, 64), (44, 70)], BLACK, 'f', False, False, 2.6), L([(68, 64), (56, 70)], BLACK, 'f', False, False, 2.6),
              L(blob([(40, 93), (60, 93), (60, 99), (40, 99)], 4), WHITE, 'f', False, True), L([(40, 96), (60, 96)], OUTC, 'f', False, False, 0.8)],
    'side': [L(outline([(80, 50), (88, 40, 1), (82, 30), (70, 14), (70, 2, 1), (60, 10), (40, 6), (18, 14), (6, 34), (6, 58), (12, 74), (30, 82), (40, 62), (48, 54),
                        (64, 50)])),
             L(outline([(6, 40), (32, 44), (40, 58), (30, 80), (12, 72)]), 'shade', 'b', False),
             L([(76, 72), (84, 76), (76, 80)], BLACK, 'f', False, False, 2.6), L(blob([(80, 94), (87, 94), (86, 99), (80, 99)], 4), WHITE, 'f', False, True)],
    'back': [L(outline([(16, 80), (12, 42), (20, 20), (40, 8), (64, 6), (70, -6, 1), (74, 6), (86, 2, 1), (82, 14), (90, 40), (84, 80), (50, 84)])),
             L(outline([(58, 8), (84, 16), (90, 42), (84, 78), (62, 82)]), 'shade', 'b', False)],
}

# Chelmey: señor adulto (solo tiene sprite de la DS): pelo verde oliva oscuro largo hasta el cuello, peinado hacia atrás,
# y un bigote enorme del mismo color
CHARS[K + 'chelmey'] = {
    'body': 'normal', 'pal': pal('#4e5032', '#d8a26a', iris='#2a2020', shade='#3c3e24', deep='#2a2c18'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'nose': (50, 84, 3.0),
             'hairline': [(14, 66), (18, 48), (30, 40), (50, 38), (70, 40), (82, 48), (86, 66)]},
    'front': [L(outline([(12, 96), (8, 70), (10, 40), (20, 16), (40, 6), (60, 6), (80, 16), (90, 40), (92, 70), (88, 96), (82, 86), (82, 56), (18, 56), (18, 86)])),
              L(outline([(60, 8), (80, 18), (90, 42), (90, 90), (82, 80), (78, 40)]), 'shade', 'b', False),
              strand([(30, 12), (22, 40), (16, 80)], 'deep', 'b', 1.0), strand([(70, 12), (78, 40), (84, 80)], 'deep', 'b', 1.0), stache(92, 15)],
    'side': [L(outline([(80, 40), (78, 14), (56, 2), (30, 4), (12, 18), (4, 42), (4, 70), (10, 96), (32, 98), (40, 80), (40, 62), (48, 54), (66, 44)])),
             L(outline([(5, 46), (30, 48), (38, 66), (32, 94), (12, 94)]), 'shade', 'b', False),
             L(blob([(78, 90), (88, 88), (90, 94), (86, 100), (80, 96)], 6), 'mid', 'f', False, True)],
    'back': [L(outline([(10, 96), (8, 60), (10, 36), (22, 14), (42, 4), (58, 4), (78, 14), (90, 36), (92, 60), (90, 96), (70, 100), (50, 102), (30, 100)])),
             L(outline([(56, 6), (80, 16), (90, 40), (90, 96), (66, 100), (62, 50)]), 'shade', 'b', False),
             strand([(36, 10), (30, 60), (32, 96)], 'deep', 'b', 1.0), strand([(64, 10), (70, 60), (68, 96)], 'deep', 'b', 1.0)],
}

# Ches "Gnashers" Nutcracker (portero): piel morena, melena rubio arena de pinchos salvajes en todas direcciones, una X de
# cicatriz en la frente, trenzas finas a los lados con cuentas verdes; ojos blancos afilados y boca de gato
CHARS[K + 'ches-gnashers-nutcracker'] = {
    'body': 'normal', 'pal': pal('#c8a050', '#b0804a', iris='#f0f0f0', shade='#a8823a', deep='#86622a', bead='#4aa04a', scar='#7a4a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94,
             'hairline': [(14, 64), (18, 50), (28, 46), (34, 52), (42, 44), (50, 50), (58, 44), (66, 52), (72, 46), (82, 50), (86, 64)]},
    'front': messy('front', amp=14, n=12, seed=7, lo=62) + [
              L(rope((20, 66), (16, 86), (20, 100), 3.4)), L(rope((80, 66), (84, 86), (80, 100), 3.4)),
              L(ell(20, 102, 2.6, 3.4), 'bead', 'f', False, True), L(ell(80, 102, 2.6, 3.4), 'bead', 'f', False, True),
              L([(40, 50), (58, 64)], 'scar', 'f', False, False, 2.6), L([(58, 50), (40, 64)], 'scar', 'f', False, False, 2.6)],
    'side': messy('side', amp=14, n=12, seed=7, lo=62) + [L(rope((40, 66), (36, 86), (40, 100), 3.4)), L(ell(40, 102, 2.6, 3.4), 'bead', 'f', False, True)],
    'back': messy('back', amp=14, n=12, seed=7, lo=62, nape=96),
}

# Chick Adiddy: grandullón de cara ancha, pelo castaño abundante peinado en un flequillo que le tapa la frente; rayas verde y
# azul marino pintadas en los mofletes, nariz redonda naranja de payaso y media sonrisa
CHARS[K + 'chick-adiddy'] = {
    'body': 'corpulento', 'pal': pal('#7c4a20', '#f6c48a', iris='#1a1210', shade='#623816', deep='#46280e', paint1='#3a9a6a', paint2='#2a3a6a', clown='#e8902a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98,
             'hairline': [(10, 64), (14, 54), (26, 50), (50, 52), (74, 48), (86, 52), (90, 64)],
             'face_front': blob([(12, 50), (50, 40), (88, 50), (94, 78), (88, 102), (68, 114), (50, 116), (32, 114), (12, 102), (6, 78)])},
    'front': [L(outline([(10, 68), (2, 44), (-4, 26, 1), (12, 16), (30, 0), (54, -6), (78, 0), (96, 16), (104, 30, 1), (98, 44), (90, 68), (84, 54), (16, 54)])),
              L(outline([(60, -2), (84, 4), (98, 22), (96, 46), (88, 60), (80, 36)]), 'shade', 'b', False),
              strand([(30, 6), (20, 30)], 'deep', 'b', 1.0), strand([(50, 0), (44, 30)], 'deep', 'b', 1.0), strand([(70, 2), (76, 30)], 'deep', 'b', 1.0),
              L(blob([(14, 82), (34, 80), (34, 85), (14, 87)], 4), 'paint1', 'f', False), L(blob([(14, 89), (34, 87), (34, 92), (14, 94)], 4), 'paint2', 'f', False),
              L(blob([(86, 82), (66, 80), (66, 85), (86, 87)], 4), 'paint1', 'f', False), L(blob([(86, 89), (66, 87), (66, 92), (86, 94)], 4), 'paint2', 'f', False),
              L(ell(50, 87, 7, 6), 'clown', 'f', False, True)],
    'side': [L(outline([(84, 54), (92, 38), (86, 14), (64, -4), (34, -2), (12, 12), (0, 40), (6, 64), (22, 72), (36, 64), (46, 58), (70, 54)])),
             L(outline([(2, 42), (30, 46), (40, 60), (24, 70), (8, 64)]), 'shade', 'b', False),
             L(blob([(64, 82), (80, 81), (80, 86), (64, 87)], 4), 'paint1', 'f', False), L(blob([(64, 89), (80, 88), (80, 93), (64, 94)], 4), 'paint2', 'f', False),
             L(ell(89, 87, 5, 5), 'clown', 'f', False, True)],
    'back': crop('back', top=-4, w=6, nape=82),
}

# Chops Denton: pelo rojo en una melena plana como un casco con un cuerno en medio y dos alas a los lados; una W roja en la
# frente y pinturas rojas en las mejillas; ojos pequeños de mirada pícara y una sonrisa enorme de dientes
CHARS[K + 'chops-denton'] = {
    'body': 'normal', 'pal': pal('#d24a2a', '#e0a462', iris='#1a1210', shade='#b0381e', deep='#8a2814', paint='#d03a24'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'none', 'hairline': [(14, 60), (20, 50), (50, 48), (80, 50), (86, 60)]},
    'front': [L(outline([(16, 62), (14, 44), (-4, 40, 1), (-2, 26), (16, 26), (28, 18), (42, 16), (46, 2), (54, 2), (58, 16), (72, 18), (84, 26), (102, 26), (104, 40, 1),
                         (86, 44), (84, 62), (80, 52), (20, 52)])),
              L(outline([(58, 16), (72, 18), (84, 26), (102, 28), (100, 38), (84, 44), (82, 56), (76, 34)]), 'shade', 'b', False),
              L([(40, 56), (44, 62), (50, 57), (56, 62), (60, 56)], 'paint', 'f', False, False, 2.6),
              L([(24, 78), (28, 86), (29, 94)], 'paint', 'f', False, False, 2.4), L([(76, 78), (72, 86), (71, 94)], 'paint', 'f', False, False, 2.4),
              *big_grin(90, 16, 10)],
    'side': [L(outline([(84, 52), (86, 38), (82, 26), (68, 18), (56, 16), (54, 2), (46, 2), (40, 16), (22, 18), (4, 22), (-6, 38, 1), (6, 40), (8, 60), (22, 66), (40, 58),
                        (60, 54)])),
             L(outline([(4, 40), (30, 44), (40, 56), (24, 64), (8, 60)]), 'shade', 'b', False),
             L([(74, 80), (76, 88), (76, 94)], 'paint', 'f', False, False, 2.4),
             L(blob([(76, 90), (88, 89), (87, 98), (78, 99)], 6), WHITE, 'f', False, True)],
    'back': [L(outline([(16, 74), (14, 44), (-4, 40, 1), (-2, 26), (16, 26), (28, 18), (42, 16), (46, 2), (54, 2), (58, 16), (72, 18), (84, 26), (102, 26), (104, 40, 1),
                        (86, 44), (84, 74), (50, 80)])),
             L(outline([(58, 16), (84, 26), (102, 28), (100, 38), (86, 44), (84, 72), (62, 78)]), 'shade', 'b', False)],
}


def rect_specs(view, c, y=76, sep=14, w=2.2):
    """Gafas rectangulares de montura de color."""
    if view == 'front':
        out = []
        for cx in (50 - sep, 50 + sep):
            out.append(L([(cx - 10, y - 5), (cx + 9, y - 5), (cx + 8, y + 5), (cx - 9, y + 5), (cx - 10, y - 5)], c, 'f', False, False, w))
        out.append(L([(50 - sep + 9, y - 3), (50 + sep - 9, y - 3)], c, 'f', False, False, w))
        return out
    return [L([(74, y - 5), (87, y - 5), (87, y + 5), (75, y + 5), (74, y - 5)], c, 'f', False, False, w), L([(74, y - 2), (50, y - 6)], c, 'f', False, False, w)]


def freckles(y=84, dx=24):
    out = []
    for s in (-1, 1):
        for ox, oy in ((-3, 0), (0, 2), (3, 0), (-1, -2), (2, -3)):
            out.append(L(ell(50 + s * dx + ox, y + oy, 0.7, 0.7), (150, 90, 50, 255), 'f', False))
    return out


# Chris Glover: melena corta castaño oliva con flequillo barrido hacia su izquierda que acaba en una punta hacia fuera y le
# tapa media frente; ojos grandes gris violeta, cejas enfadadas y boca seria
CHARS[K + 'chris-glover'] = {
    'body': 'normal', 'pal': pal('#a68a52', '#f6c896', iris='#8a8aaa', shade='#866c3a', deep='#665028'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 92, 'ears': False,
             'hairline': [(14, 84), (16, 62), (24, 54), (34, 60), (50, 50), (66, 42), (80, 46), (86, 70)]},
    'front': [L(outline([(14, 88), (8, 64), (8, 38), (20, 14), (40, 4), (62, 4), (82, 14), (94, 30), (104, 34, 1), (90, 44), (88, 70), (84, 80), (80, 56), (20, 56)])),
              L(outline([(62, 6), (82, 16), (94, 32), (102, 36), (90, 44), (86, 66), (80, 40)]), 'shade', 'b', False),
              fr([(14, 66), (18, 44), (34, 28), (60, 26), (84, 34), (102, 34, 1), (80, 40), (60, 40), (42, 50), (30, 60), (22, 70, 1)]),
              strand([(30, 40), (50, 32), (72, 34)], 'deep', 'f', 1.0)],
    'side': [L(outline([(82, 52), (92, 40), (100, 38, 1), (88, 30), (82, 14), (60, 2), (34, 4), (14, 18), (4, 42), (6, 66), (16, 86), (30, 88), (42, 74), (52, 62),
                        (66, 56)])),
             L(outline([(5, 44), (32, 48), (46, 62), (32, 86), (14, 80)]), 'shade', 'b', False)],
    'back': bowl('back', top=4, nape=88),
}

# Chris Hypogee: cara alargada; pelo verde oliva corto peinado hacia atrás con las rayas del peine marcadas; ojos blancos de
# puntito con pestañas, cejas verdes gruesas, nariz grande y boca recta
CHARS[K + 'chris-hypogee'] = {
    'body': 'delgado', 'pal': pal('#7a8a40', '#eaa868', iris='#1a1210', shade='#606e2e', deep='#46521e'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'line', 'mouth_y': 96, 'nose': (50, 86, 3.6),
             'hairline': [(16, 60), (20, 44), (34, 36), (50, 34), (66, 36), (80, 44), (84, 60)],
             'face_front': blob([(18, 50), (50, 38), (82, 50), (84, 80), (76, 100), (60, 112), (50, 114), (40, 112), (24, 100), (16, 80)])},
    'front': [L(outline([(17, 64), (14, 40), (20, 16), (36, 2), (50, -2), (64, 2), (80, 16), (86, 40), (83, 64), (80, 46), (20, 46)])),
              L(outline([(58, 0), (78, 12), (86, 38), (82, 58), (74, 30)]), 'shade', 'b', False),
              *[strand([(x, 0 + abs(x - 50) * 0.3), (x + (x - 50) * 0.2, 38)], 'deep', 'b', 1.0) for x in (30, 40, 50, 60, 70)],
              *thick_brows(64, 'shade', 3.4, 14, 1.0, 12), *lashes_out(75, 14)],
    'side': [L(outline([(80, 44), (84, 30), (76, 10), (56, -2), (30, 2), (12, 16), (4, 40), (8, 62), (22, 70), (36, 62), (44, 54), (62, 46)])),
             L(outline([(5, 42), (30, 46), (40, 58), (24, 68), (8, 62)]), 'shade', 'b', False),
             *[strand([(80 - k * 12, 8 + k * 2), (40 - k * 8, 30 + k * 8)], 'deep', 'b', 1.0) for k in range(3)], *side_brow(64, 'shade', 3.4, 1.0)],
    'back': crop('back', top=-2, nape=80) + [strand([(x, 2), (x + (x - 50) * 0.1, 76)], 'deep', 'b', 1.0) for x in (34, 50, 66)],
}

# Chris Massey: pelo lila revuelto con un remolino en la coronilla y dos mechones a los lados que se enroscan hacia fuera
# como cuernos de carnero; gafas rectangulares verde oliva, ojos azules y boca seria
CHARS[K + 'chris-massey'] = {
    'body': 'normal', 'pal': pal('#c2a2ba', '#f6c48a', iris='#4a8ab0', shade='#a284a0', deep='#826680', specs='#8a8a30'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93,
             'hairline': [(14, 64), (18, 52), (26, 58), (32, 50), (40, 60), (48, 50), (56, 60), (64, 50), (72, 58), (80, 50), (86, 64)]},
    'front': [L(outline([(16, 68), (12, 44), (16, 22), (30, 8), (48, 4), (52, -8, 1), (58, 4), (74, 8), (86, 22), (88, 44), (84, 68), (80, 52), (20, 52)])),
              L(outline([(58, 6), (80, 14), (88, 40), (84, 60), (76, 36)]), 'shade', 'b', False),
              L(rope((14, 56), (-2, 52), (2, 38), 5)), L(rope((14, 62), (-4, 64), (-2, 74), 4)),
              L(rope((86, 56), (102, 52), (98, 38), 5)), L(rope((86, 62), (104, 64), (102, 74), 4)), *rect_specs('front', 'specs', 76)],
    'side': [L(outline([(80, 54), (88, 40), (82, 18), (60, 4), (56, -8, 1), (48, 2), (30, 4), (12, 18), (4, 42), (8, 64), (22, 72), (36, 64), (44, 56), (64, 54)])),
             L(outline([(5, 44), (30, 48), (40, 60), (24, 70), (8, 64)]), 'shade', 'b', False),
             L(rope((40, 56), (30, 44), (36, 34), 5)), *rect_specs('side', 'specs', 76)],
    'back': [L(outline([(16, 78), (12, 44), (16, 22), (30, 8), (48, 4), (52, -8, 1), (58, 4), (74, 8), (86, 22), (88, 44), (84, 78), (50, 84)])),
             L(outline([(58, 6), (80, 14), (88, 40), (84, 76), (62, 82)]), 'shade', 'b', False),
             L(rope((14, 56), (-2, 52), (2, 38), 5)), L(rope((86, 56), (102, 52), (98, 38), 5))],
}

# Chris Pecracker (portero): gorro de lana rosa palo con el borde crema, del que asoman rizos castaños por la frente y los
# lados; ojos cerrados de risa, pecas, nariz grande y sonrisa
CHARS[K + 'chris-pecracker'] = {
    'body': 'normal', 'pal': pal('#7a4a28', '#eaaa6c', shade='#5e3618', deep='#42240e', hat='#c48a8c', hat_d='#a46c70', rim='#f0dcc0'),
    'face': {'eyes': 'closed', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'nose': (50, 86, 3.6), 'hairline': False},
    'front': [L(blob([(12, 76), (8, 60), (16, 52), (22, 62), (20, 78)], 6)), L(blob([(88, 76), (92, 60), (84, 52), (78, 62), (80, 78)], 6)),
              L(outline([(14, 52), (10, 30), (22, 8), (50, -2), (78, 8), (90, 30), (86, 52), (50, 46)]), 'hat', 'f'),
              L(outline([(60, 0), (80, 10), (90, 32), (86, 50), (76, 30)]), 'hat_d', 'f', False),
              L(quad((12, 46), (50, 36), (88, 46)) + quad((88, 54), (50, 44), (12, 54)), 'rim', 'f', False, True),
              L(blob([(36, 52), (40, 44), (48, 46), (54, 42), (62, 46), (66, 54), (58, 58), (50, 56), (42, 58)], 6), 'mid', 'f', True), *freckles(84, 24)],
    'side': [L(blob([(30, 76), (22, 64), (30, 54), (42, 58), (40, 74)], 6)),
             L(outline([(84, 50), (88, 34), (78, 12), (54, -2), (28, 2), (10, 18), (4, 42), (8, 58), (40, 52), (64, 48)]), 'hat', 'f'),
             L(quad((86, 44), (50, 40), (6, 50)) + quad((8, 58), (50, 48), (84, 52)), 'rim', 'f', False, True),
             L(blob([(76, 54), (82, 48), (90, 50), (88, 58)], 6), 'mid', 'f', True)],
    'back': [L(blob([(14, 80), (8, 62), (20, 56), (50, 60), (80, 56), (92, 62), (86, 80), (70, 88), (50, 90), (30, 88)], 8)),
             L(outline([(14, 58), (10, 34), (22, 10), (50, -2), (78, 10), (90, 34), (86, 58), (50, 62)]), 'hat', 'f'),
             L(outline([(58, 0), (80, 12), (90, 36), (86, 56), (62, 60)]), 'hat_d', 'f', False),
             L(quad((12, 52), (50, 58), (88, 52)) + quad((88, 60), (50, 66), (12, 60)), 'rim', 'f', False, True)],
}

# Chris "Smiles" Miles: piel tostada, pelo castaño corto con raya en medio y los lados por encima de las orejas; ojos grandes
# verdes, cejas enfadadas y una sonrisita
CHARS[K + 'chris-smiles-miles'] = {
    'body': 'normal', 'pal': pal('#8a6a3c', '#c8925a', iris='#3a9a5a', shade='#6e5228', deep='#523c18'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93,
             'hairline': [(16, 62), (18, 46), (30, 40), (46, 38), (50, 42), (54, 38), (70, 40), (82, 46), (84, 62)]},
    'front': crop('front', top=4, side=64) + [strand([(50, 6), (48, 20), (50, 40)], 'deep', 'b', 1.2), strand([(30, 14), (22, 40)], 'deep', 'b', 1.0),
                                              strand([(70, 14), (78, 40)], 'deep', 'b', 1.0)],
    'side': crop('side', top=4, nape=80),
    'back': crop('back', top=4, nape=80),
}

# Chris Talise: pelo verde azulado grisáceo con una corona de rastas gruesas que salen de la coronilla y se doblan hacia los
# lados como una palmera (el centro rosado), y los lados cortos con mechones por la frente; ojos redondos, cejas enfadadas
CHARS[K + 'chris-talise'] = {
    'body': 'normal', 'pal': pal('#5c8a80', '#f6c48a', iris='#1a1210', shade='#467068', deep='#30564e', core='#d09a9a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93,
             'hairline': [(16, 66), (20, 50), (30, 56), (36, 46), (44, 56), (50, 46), (56, 56), (64, 46), (70, 56), (80, 50), (84, 66)]},
    'front': crop('front', top=14, side=68) + [
              *[L(rope((50 + dx * 0.15, 14), (50 + dx * 0.55, -16), (50 + dx * 1.0, -2), 9)) for dx in (-44, -30, 30, 44)],
              *[L(rope((50 + dx * 0.15, 12), (50 + dx * 0.4, -20), (50 + dx * 0.9, -16), 9)) for dx in (-16, 16)],
              L(ell(50, 10, 6, 5), 'core')],
    'side': crop('side', top=14, nape=82) + [*[L(rope((46, 12), (46 + dx * 0.55, -16), (46 + dx * 1.0, -2), 9)) for dx in (-40, -16, 16, 40)],
                                             L(ell(46, 10, 5, 4), 'core')],
    'back': crop('back', top=14, nape=82) + [*[L(rope((50 + dx * 0.15, 16), (50 + dx * 0.55, -14), (50 + dx * 1.0, 0), 9)) for dx in (-44, -30, -14, 14, 30, 44)],
                                             L(ell(50, 12, 6, 5), 'core')],
}

# Christian Dear: pelo castaño de pinchos con una cinta ancha azul grisáceo en la frente, y dos trencitas a los lados con
# cuentas rojas; ojos rojos y cejas enfadadas
CHARS[K + 'christian-dear'] = {
    'body': 'normal', 'pal': pal('#8c5028', '#f6c48a', iris='#c02a2a', shade='#703c1a', deep='#542810', band='#6a8aa0', band_l='#e8e0c8', bead='#c82a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93,
             'hairline': [(14, 66), (20, 56), (28, 64), (36, 56), (44, 66), (52, 56), (60, 64), (68, 56), (76, 64), (82, 56), (86, 66)]},
    'front': messy('front', amp=10, n=10, seed=11, lo=64) + [
              L(quad((8, 40), (50, 26), (92, 40)) + quad((92, 52), (50, 38), (8, 52)), 'band', 'f', True),
              L(quad((8, 40), (50, 26), (92, 40)), 'band_l', 'f', False, False, 1.6),
              L(rope((18, 68), (16, 84), (18, 98), 3.4)), L(rope((82, 68), (84, 84), (82, 98), 3.4)),
              L(blob([(15, 86), (21, 86), (21, 96), (15, 96)], 4), 'bead', 'f', False, True), L(blob([(79, 86), (85, 86), (85, 96), (79, 96)], 4), 'bead', 'f', False, True)],
    'side': messy('side', amp=10, n=10, seed=11, lo=64) + [L(quad((90, 46), (50, 22), (6, 40)) + quad((6, 52), (50, 34), (90, 58)), 'band', 'f', True),
                                                           L(rope((42, 68), (40, 84), (42, 98), 3.4)), L(blob([(39, 86), (45, 86), (45, 96), (39, 96)], 4), 'bead', 'f', False, True)],
    'back': messy('back', amp=10, n=10, seed=11, lo=64) + [L(quad((6, 44), (50, 54), (94, 44)) + quad((94, 56), (50, 66), (6, 56)), 'band', 'f', True)],
}

# Chuck Hardy: niño bajito con una melena rojo anaranjado de pinchos salvajes en todas direcciones; ojos de puntito, cejas
# enfadadas y boca seria
CHARS[K + 'chuck-hardy'] = {
    'body': 'bajito', 'pal': pal('#d24c22', '#f6c896', shade='#b03a16', deep='#8a2a0e'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 92,
             'hairline': [(14, 66), (20, 54), (28, 62), (36, 52), (46, 60), (54, 50), (62, 60), (72, 52), (80, 60), (86, 66)]},
    'front': messy('front', amp=18, n=12, seed=21, lo=70),
    'side': messy('side', amp=18, n=12, seed=21, lo=70),
    'back': messy('back', amp=18, n=12, seed=21, lo=70, nape=94),
}


def goggles(view, y=74, frame=(150, 80, 50, 255), lens=(200, 180, 120, 255)):
    """Gafas de aviador sobre los ojos: dos cristales redondeados unidos, con la correa."""
    if view == 'front':
        out = []
        for cx in (36, 64):
            out.append(L(blob([(cx - 11, y - 5), (cx + 10, y - 6), (cx + 11, y + 5), (cx - 10, y + 6)], 6), frame, 'f', True))
            out.append(L(blob([(cx - 8, y - 3), (cx + 8, y - 4), (cx + 8, y + 3), (cx - 8, y + 4)], 6), lens, 'f', False))
        out.append(L([(8, y - 2), (26, y)], frame, 'f', False, False, 3))
        out.append(L([(74, y), (92, y - 2)], frame, 'f', False, False, 3))
        return out
    if view == 'side':
        return [L(blob([(74, y - 6), (88, y - 6), (89, y + 5), (75, y + 6)], 6), frame, 'f', True), L(blob([(77, y - 4), (87, y - 4), (87, y + 3), (77, y + 4)], 6), lens, 'f', False),
                L([(74, y - 1), (40, y - 6)], frame, 'f', False, False, 3)]
    return [L(quad((6, y - 4), (50, y + 2), (94, y - 4)), frame, 'f', False, False, 3)]


def shades(view, y=76, c=(90, 170, 150, 255)):
    """Gafas de sol rectangulares de cristal de color."""
    if view == 'front':
        return [L(blob([(24, y - 5), (46, y - 4), (45, y + 4), (26, y + 5)], 4), c, 'f', True), L(blob([(76, y - 5), (54, y - 4), (55, y + 4), (74, y + 5)], 4), c, 'f', True),
                L([(45, y - 3), (55, y - 3)], OUTC, 'f', False, False, 1.4)]
    return [L(blob([(74, y - 5), (88, y - 5), (88, y + 4), (75, y + 4)], 4), c, 'f', True), L([(74, y - 2), (48, y - 6)], OUTC, 'f', False, False, 1.4)]


# Chunk Gorman: grandullón de cara redonda enorme; pelo castaño como un casquete fino con dos cortinas lisas que le caen por
# detrás de las mejillas hasta la papada; ojos pequeños de enfado, pecas, nariz naranja pequeña y boca fruncida
CHARS[K + 'chunk-gorman'] = {
    'body': 'corpulento', 'pal': pal('#7a4a22', '#f2b878', iris='#1a1210', shade='#603818', deep='#46280e'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'nose': (50, 88, 2.6), 'ear_out': 4, 'hairline': [(10, 50), (30, 42), (50, 40), (70, 42), (90, 50)],
             'face_front': blob([(12, 52), (50, 40), (88, 52), (96, 80), (90, 104), (70, 116), (50, 118), (30, 116), (10, 104), (4, 80)])},
    'front': [L(outline([(6, 110), (2, 70), (8, 36), (24, 14), (50, 6), (76, 14), (92, 36), (98, 70), (94, 110), (88, 110), (88, 60), (12, 60), (12, 110)])),
              L(outline([(60, 8), (78, 16), (92, 38), (96, 70), (92, 106), (88, 60), (78, 30)]), 'shade', 'b', False), *freckles(88, 26)],
    'side': [L(outline([(78, 44), (70, 18), (50, 8), (28, 12), (10, 28), (4, 56), (6, 90), (10, 112), (30, 112), (36, 86), (34, 60), (46, 50), (62, 44)])),
             L(outline([(6, 56), (30, 58), (34, 86), (28, 108), (12, 106)]), 'shade', 'b', False)],
    'back': [L(outline([(4, 112), (2, 70), (8, 36), (24, 14), (50, 6), (76, 14), (92, 36), (98, 70), (96, 112), (50, 116)])),
             L(outline([(58, 8), (78, 16), (92, 38), (96, 70), (94, 110), (64, 114)]), 'shade', 'b', False)],
}

# Clark Rain: pelo azul verdoso en capas desfiladas, con el flequillo hasta las cejas y los lados hasta la mandíbula en
# puntas; ojos grandes negros, cejas azules gruesas y sonrisa
CHARS[K + 'clark-rain'] = {
    'body': 'normal', 'pal': pal('#5a8c9c', '#f2b878', iris='#1a1210', shade='#46707e', deep='#325662'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'ears': False,
             'hairline': [(14, 86), (16, 64), (24, 58), (34, 64), (42, 56), (50, 64), (58, 56), (66, 64), (76, 58), (84, 64), (86, 86)]},
    'front': [L(outline([(16, 92, 1), (10, 78), (4, 80, 1), (8, 56), (6, 36), (18, 12), (40, 2), (62, 2), (82, 12), (94, 36), (92, 56), (98, 80, 1), (90, 78), (84, 92, 1),
                         (80, 70), (20, 70)])),
              L(outline([(62, 4), (84, 14), (94, 38), (92, 60), (96, 78), (86, 80), (80, 50)]), 'shade', 'b', False),
              strand([(30, 10), (24, 40)], 'deep', 'b', 1.0), strand([(50, 4), (46, 40)], 'deep', 'b', 1.0), strand([(70, 8), (74, 40)], 'deep', 'b', 1.0),
              *thick_brows(62, 'mid', 3.6, 14, 0.4, 12)],
    'side': [L(outline([(82, 60), (88, 44), (82, 16), (60, 2), (32, 4), (12, 18), (2, 44), (4, 70), (12, 92, 1), (22, 82), (32, 94, 1), (40, 78), (50, 64), (66, 60)])),
             L(outline([(4, 44), (30, 50), (44, 64), (32, 90), (12, 86)]), 'shade', 'b', False), *side_brow(62, 'mid', 3.6, 0.4)],
    'back': [L(outline([(12, 94, 1), (6, 76), (6, 36), (18, 12), (40, 2), (60, 2), (82, 12), (94, 36), (94, 76), (88, 94, 1), (74, 86), (62, 96, 1), (50, 86), (38, 96, 1),
                        (26, 86)])),
             L(outline([(58, 4), (82, 14), (94, 40), (92, 80), (76, 88), (62, 50)]), 'shade', 'b', False)],
}

# Clark Roach: gorra verde con la visera y el frente crema y una corona blanca bordada, con el botón arriba; el pelo rosa le
# asoma por debajo en la frente y los lados; ojos entornados y media sonrisa
CHARS[K + 'clark-roach'] = {
    'body': 'normal', 'pal': pal('#e09098', '#f2b878', iris='#1a1210', shade='#c07078', deep='#a05860', cap='#6aa040', cap_d='#4e8030', cream='#f2e4b8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': False},
    'front': [L(outline([(14, 74), (10, 58), (16, 50), (26, 60), (22, 72)])), L(outline([(86, 74), (90, 58), (84, 50), (74, 60), (78, 72)])),
              fr([(28, 62), (34, 52), (50, 50), (66, 52), (72, 62), (60, 58), (50, 62), (40, 58)]),
              L(outline([(14, 52), (12, 30), (22, 8), (50, -2), (78, 8), (88, 30), (86, 52), (50, 46)]), 'cap', 'f'),
              L(outline([(30, 50), (28, 22), (50, 14), (72, 22), (70, 50)]), 'cream', 'f', False),
              L(outline([(4, 56), (20, 46), (50, 42), (80, 46), (96, 56), (80, 56), (50, 52), (20, 56)]), 'cream', 'f'),
              L([(40, 38), (38, 26), (44, 32), (50, 22), (56, 32), (62, 26), (60, 38)], WHITE, 'f', False, True),
              L(ell(50, -2, 3.4, 2.6), 'cap', 'f', True)],
    'side': [L(outline([(36, 70), (30, 58), (40, 52), (48, 62)])),
             L(outline([(76, 50), (78, 30), (68, 8), (46, -2), (24, 4), (8, 20), (4, 42), (8, 56), (40, 52), (60, 50)]), 'cap', 'f'),
             L(outline([(62, 48), (64, 24), (76, 20), (84, 32), (84, 48)]), 'cream', 'f', False),
             L(outline([(70, 52), (88, 46), (104, 50), (100, 56), (80, 56)]), 'cream', 'f'), L(ell(46, -2, 3, 2.4), 'cap', 'f', True)],
    'back': [L(blob([(14, 74), (12, 58), (30, 60), (50, 62), (70, 60), (88, 58), (86, 74), (70, 80), (50, 82), (30, 80)], 6)),
             L(outline([(14, 60), (10, 34), (22, 8), (50, -2), (78, 8), (90, 34), (86, 60), (50, 64)]), 'cap', 'f'),
             L(outline([(58, 0), (80, 10), (90, 36), (86, 58), (62, 62)]), 'cap_d', 'f', False),
             L(blob([(40, 56), (60, 56), (58, 62), (42, 62)], 4), 'cream', 'f', False, True), L(ell(50, -2, 3.4, 2.6), 'cap', 'f', True)],
}

# Clark Watcher: cara alargada; pelo castaño con raya en medio, liso y pegado en un casquete hasta las orejas; ojos de
# puntito, cejas gruesas, nariz grande y sonrisa
CHARS[K + 'clark-watcher'] = {
    'body': 'delgado', 'pal': pal('#7a4a22', '#f2b878', iris='#1a1210', shade='#603818', deep='#46280e'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'nose': (50, 86, 3.4),
             'hairline': [(16, 66), (18, 44), (30, 38), (46, 36), (50, 40), (54, 36), (70, 38), (82, 44), (84, 66)],
             'face_front': blob([(18, 50), (50, 38), (82, 50), (84, 80), (76, 100), (60, 112), (50, 114), (40, 112), (24, 100), (16, 80)])},
    'front': crop('front', top=-2, side=70) + [strand([(50, 0), (50, 38)], 'deep', 'b', 1.2), *thick_brows(64, 'deep', 3.6, 14, 0.8, 12)],
    'side': crop('side', top=-2, nape=80),
    'back': crop('back', top=-2, nape=80),
}

# Claude Snap: melena enorme azul marino violáceo de pinchos revueltos; gafas de aviador con la montura marrón y los cristales
# beis sobre los ojos, y una sonrisa enorme de dientes
CHARS[K + 'claude-snap'] = {
    'body': 'normal', 'pal': pal('#4c4c7c', '#d8955a', shade='#3a3a64', deep='#2a2a4c'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none',
             'hairline': [(10, 70), (16, 56), (24, 62), (32, 52), (40, 62), (50, 52), (60, 62), (68, 52), (76, 62), (84, 56), (90, 70)]},
    'front': messy('front', amp=18, n=13, seed=31, rx=52, ry=44, lo=76) + goggles('front', 74) + big_grin(88, 16, 11),
    'side': messy('side', amp=18, n=13, seed=31, rx=52, ry=44, lo=76) + goggles('side', 74) + [L(blob([(74, 88), (88, 87), (88, 96), (78, 98)], 6), WHITE, 'f', False, True)],
    'back': messy('back', amp=18, n=13, seed=31, rx=52, ry=44, lo=76, nape=96) + goggles('back', 74),
}

# Clay Modlin: adulto calvo de piel tostada, con gafas de sol rectangulares verde agua y media sonrisa ladeada
CHARS[K + 'clay-modlin'] = {
    'body': 'normal', 'pal': pal('#c08048', '#d0904e', iris='#1a1210'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False, 'nose': (52, 86, 2.6)},
    'front': [skull(), strand([(36, 22), (40, 40)], 'skin_d', 'b', 1.0), strand([(64, 22), (60, 40)], 'skin_d', 'b', 1.0), *shades('front', 76),
              L(quad((40, 96), (54, 98), (62, 92)), (110, 60, 40, 255), 'f', False, False, 1.6)],
    'side': [*shades('side', 76), L([(80, 96), (86, 94)], (110, 60, 40, 255), 'f', False, False, 1.4)],
    'back': [],
}

# Clerk Welcome: cara alargada; pelo verde claro corto con un tupé alto en forma de llama en la frente; ojos redondos de
# puntito, cejas verdes y sonrisa
CHARS[K + 'clerk-welcome'] = {
    'body': 'delgado', 'pal': pal('#8ac250', '#f2b878', iris='#1a1210', shade='#6ea03a', deep='#548028'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 96,
             'hairline': [(16, 62), (20, 46), (34, 42), (44, 50), (50, 40), (60, 48), (70, 42), (80, 46), (84, 62)],
             'face_front': blob([(18, 50), (50, 38), (82, 50), (84, 80), (76, 100), (60, 112), (50, 114), (40, 112), (24, 100), (16, 80)])},
    'front': crop('front', top=12, side=64) + [L(outline([(30, 40), (32, 14), (44, -4), (52, -12, 1), (58, 0), (66, 16), (70, 40), (58, 34), (50, 46), (42, 34)])),
                                               L(outline([(52, -10), (60, 2), (68, 18), (70, 38), (60, 30)]), 'shade', 'b', False),
                                               strand([(48, 0), (44, 20), (46, 40)], 'deep', 'b', 1.0), *thick_brows(64, 'mid', 3.4, 14, 0.6, 12)],
    'side': crop('side', top=12, nape=80) + [L(outline([(60, 36), (64, 14), (72, 0), (90, -8, 1), (84, 8), (86, 26), (80, 42)]))],
    'back': crop('back', top=12, nape=80) + [L(outline([(34, 20), (40, 2), (50, -10, 1), (60, 2), (66, 20), (50, 26)]))],
}

# Cletus Badden: pelo verde de mechones de pincho largos barridos hacia su izquierda, con un flequillo que le tapa un lado
# de la frente; ojos cerrados contentos y sonrisa
CHARS[K + 'cletus-badden'] = {
    'body': 'normal', 'pal': pal('#5a8c32', '#f2b878', iris='#1a1210', shade='#467024', deep='#325418'),
    'face': {'eyes': 'closed', 'brows': True, 'mouth': 'smile', 'mouth_y': 93,
             'hairline': [(14, 76), (16, 56), (30, 50), (44, 56), (54, 46), (66, 50), (76, 46), (86, 60)]},
    'front': messy('front', amp=12, n=10, seed=41, lo=66, sweep=0.6) + [
              fr([(14, 60), (20, 38), (44, 28), (70, 30), (96, 22, 1), (80, 38), (64, 42), (54, 56, 1), (48, 42), (34, 50), (24, 70, 1)]),
              strand([(30, 40), (52, 34), (76, 32)], 'deep', 'f', 1.0)],
    'side': messy('side', amp=12, n=10, seed=41, lo=66, sweep=0.6),
    'back': messy('back', amp=12, n=10, seed=41, lo=66, sweep=0.6, nape=90),
}


def round_specs(view, c, y=76, sep=14, rx=9.5, ry=7.5, w=1.8):
    if view == 'front':
        return [L(ell(50 - sep, y, rx, ry) + [ell(50 - sep, y, rx, ry)[0]], c, 'f', False, False, w),
                L(ell(50 + sep, y, rx, ry) + [ell(50 + sep, y, rx, ry)[0]], c, 'f', False, False, w),
                L([(50 - sep + rx, y - 1), (50 + sep - rx, y - 1)], c, 'f', False, False, w)]
    return [L(ell(81, y, 6, ry) + [ell(81, y, 6, ry)[0]], c, 'f', False, False, w), L([(75, y - 1), (50, y - 6)], c, 'f', False, False, w)]


# Clint Wester: cara alargada; pelo azul grisáceo de pinchos que se abren a los lados y mechones por la frente; cejas negras
# gruesas y enfadadas, ojos entornados, nariz grande y media sonrisa
CHARS[K + 'clint-wester'] = {
    'body': 'delgado', 'pal': pal('#5a7c92', '#f2b878', iris='#1a1210', shade='#466478', deep='#324a5c'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'nose': (50, 86, 3.6),
             'hairline': [(14, 68), (18, 54), (28, 60), (36, 50), (46, 58), (54, 48), (62, 58), (72, 50), (80, 58), (86, 68)],
             'face_front': blob([(18, 50), (50, 38), (82, 50), (84, 80), (76, 100), (60, 112), (50, 114), (40, 112), (24, 100), (16, 80)])},
    'front': messy('front', amp=14, n=10, seed=51, lo=68) + thick_brows(64, BLACK, 4.0, 15, 1.2, 14),
    'side': messy('side', amp=14, n=10, seed=51, lo=68) + side_brow(64, BLACK, 4.0, 1.2),
    'back': messy('back', amp=14, n=10, seed=51, lo=68, nape=90),
}

# Cody Barani (portero): pelo crema recogido hacia atrás muy tirante, con rayas, y dos moños redondos a los lados de la
# coronilla; frente despejada, ojos de puntito con pestañas, nariz naranja grande, bigotes de gato y sonrisa
CHARS[K + 'cody-barani'] = {
    'body': 'normal', 'pal': pal('#f2e2c2', '#f2b878', iris='#1a1210', shade='#d6c4a2', deep='#b8a684'),
    'face': {'eyes': 'dot', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': [(16, 56), (20, 40), (34, 32), (50, 30), (66, 32), (80, 40), (84, 56)]},
    'front': [L(outline([(17, 58), (14, 36), (22, 14), (50, 4), (78, 14), (86, 36), (83, 58), (78, 40), (22, 40)])),
              *[strand([(x, 6 + abs(x - 50) * 0.2), (x + (x - 50) * 0.3, 34)], 'shade', 'b', 1.0) for x in (30, 40, 50, 60, 70)],
              L(ell(18, 12, 10, 10)), L(ell(82, 12, 10, 10)), strand([(12, 8), (18, 4), (24, 10)], 'shade', 'b', 1.0), strand([(76, 10), (82, 4), (88, 8)], 'shade', 'b', 1.0),
              L(blob([(44, 80), (56, 80), (58, 90), (50, 94), (42, 90)], 6), (226, 134, 60, 255), 'f', False, True),
              L([(22, 86), (30, 87)], OUTC, 'f', False, False, 1.0), L([(22, 90), (30, 89)], OUTC, 'f', False, False, 1.0),
              L([(78, 86), (70, 87)], OUTC, 'f', False, False, 1.0), L([(78, 90), (70, 89)], OUTC, 'f', False, False, 1.0), *lashes_out(75, 14)],
    'side': crop('side', top=4, nape=78) + [L(ell(40, 10, 10, 10)), L(blob([(84, 80), (94, 82), (92, 92), (84, 92)], 6), (226, 134, 60, 255), 'f', False, True)],
    'back': crop('back', top=4, nape=78) + [L(ell(18, 14, 10, 10)), L(ell(82, 14, 10, 10)), strand([(50, 6), (50, 70)], 'shade', 'b', 1.0)],
}

# Col Lector: gorro de lana rojo con el borde vuelto naranja, un zigzag crema y una borla roja enorme, calado hasta taparle un
# ojo; pelo oscuro por debajo, un ojo redondo, nariz naranja y sonrisa con un diente
CHARS[K + 'col-lector'] = {
    'body': 'bajito', 'pal': pal('#2a2422', '#f2b878', iris='#1a1210', hat='#b8301c', hat_d='#962410', rim='#e0782a', rim_d='#c0601c', zig='#f2d8a8'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False, 'nose': (50, 88, 2.6)},
    'front': [L(outline([(16, 84), (12, 70), (20, 72), (24, 86)])),
              L(outline([(12, 64), (10, 36), (22, 10), (50, 0), (78, 10), (90, 36), (88, 64), (50, 60)]), 'hat', 'f'),
              L(outline([(60, 2), (80, 12), (90, 38), (88, 60), (76, 36)]), 'hat_d', 'f', False),
              L([(12, 46), (22, 36), (32, 46), (42, 34), (52, 46), (62, 34), (72, 46), (82, 34), (90, 44)], 'zig', 'f', False, False, 2.6),
              L(outline([(8, 54), (10, 42), (50, 40), (90, 42), (92, 54), (90, 74), (64, 78), (46, 68), (10, 64)]), 'rim', 'f'),
              *[strand([(x, 44), (x, 64 + max(0, x - 44) * 0.22)], 'rim_d', 'f', 1.0) for x in (20, 30, 40, 50, 60, 70, 80)],
              L(ell(50, -6, 9, 8), 'hat', 'f', True),
              L(ell(32, 76, 4.6, 4.8), OUTC, 'f', False), L(ell(32, 76, 3.5, 3.7), WHITE, 'f', False), L(ell(33, 75, 2.2, 2.4), BLACK, 'f', False),
              L(quad((40, 96), (50, 100), (62, 94)), (130, 70, 50, 255), 'f', False, False, 1.4),
              L(blob([(52, 97), (57, 96), (57, 101), (52, 101)], 4), WHITE, 'f', False, True)],
    'side': [L(outline([(36, 82), (30, 70), (42, 72), (46, 84)])),
             L(outline([(86, 64), (88, 38), (76, 10), (52, 0), (26, 6), (8, 24), (4, 50), (10, 66), (40, 62)]), 'hat', 'f'),
             L(outline([(6, 60), (8, 50), (50, 48), (90, 52), (92, 76), (60, 78), (30, 78), (8, 72)]), 'rim', 'f'),
             L([(10, 42), (22, 34), (34, 42), (46, 32), (58, 42), (70, 32), (82, 40)], 'zig', 'f', False, False, 2.6), L(ell(44, -6, 9, 8), 'hat', 'f', True),
             L(blob([(78, 94), (86, 93), (86, 98), (80, 99)], 4), WHITE, 'f', False, True)],
    'back': [L(outline([(12, 66), (10, 36), (22, 10), (50, 0), (78, 10), (90, 36), (88, 66), (50, 64)]), 'hat', 'f'),
             L(outline([(58, 2), (80, 12), (90, 38), (88, 64), (62, 64)]), 'hat_d', 'f', False),
             L([(12, 48), (22, 38), (32, 48), (42, 36), (52, 48), (62, 36), (72, 48), (82, 36), (90, 46)], 'zig', 'f', False, False, 2.6),
             L(outline([(8, 64), (10, 54), (50, 52), (90, 54), (92, 64), (90, 78), (50, 82), (10, 78)]), 'rim', 'f'), L(ell(50, -6, 9, 8), 'hat', 'f', True)],
}

# Cole Coaker (portero): pelo verde oliva oscuro esponjoso y redondo, con un flequillo recto que le cubre la frente; ojos
# azules, rayas verdes pintadas en los mofletes, nariz larga y boca seria
CHARS[K + 'cole-coaker'] = {
    'body': 'delgado', 'pal': pal('#5a6a2e', '#f2b878', iris='#5aa0c0', shade='#46541e', deep='#323e12', paint='#5a8a30'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'nose': (50, 86, 3.2), 'ears': False,
             'hairline': [(10, 74), (14, 62), (30, 62), (50, 64), (70, 62), (86, 62), (90, 74)],
             'face_front': blob([(18, 50), (50, 38), (82, 50), (84, 80), (76, 100), (60, 112), (50, 114), (40, 112), (24, 100), (16, 80)])},
    'front': [L(blob([(8, 78), (0, 60), (2, 36), (14, 14), (34, 0), (50, -4), (66, 0), (86, 14), (98, 36), (100, 60), (92, 78), (84, 70), (16, 70)], 8)),
              L(outline([(60, 0), (86, 14), (98, 38), (98, 62), (88, 72), (82, 40)]), 'shade', 'b', False),
              *[strand([(x, 48), (x + 1, 62)], 'deep', 'b', 1.0) for x in (26, 38, 50, 62, 74)],
              L([(22, 84), (32, 86)], 'paint', 'f', False, False, 2.0), L([(22, 89), (32, 90)], 'paint', 'f', False, False, 2.0),
              L([(78, 84), (68, 86)], 'paint', 'f', False, False, 2.0), L([(78, 89), (68, 90)], 'paint', 'f', False, False, 2.0)],
    'side': [L(blob([(86, 62), (92, 44), (86, 16), (62, -2), (32, 0), (8, 16), (-2, 44), (2, 72), (16, 86), (32, 84), (42, 70), (56, 62)], 8)),
             L(outline([(0, 46), (30, 50), (42, 66), (30, 82), (12, 80)]), 'shade', 'b', False),
             L([(74, 86), (82, 87)], 'paint', 'f', False, False, 2.0), L([(74, 90), (82, 91)], 'paint', 'f', False, False, 2.0)],
    'back': [L(blob([(6, 84), (-2, 60), (2, 36), (14, 14), (34, 0), (50, -4), (66, 0), (86, 14), (98, 36), (102, 60), (94, 84), (50, 90)], 8)),
             L(outline([(58, 0), (86, 14), (98, 38), (98, 70), (90, 84), (62, 88)]), 'shade', 'b', False)],
}

# Cole Easteroll: piel morena, pelo castaño abombado y redondo como un casco; cara alargada, cejas gruesas arqueadas, ojos
# redondos, nariz grande y boca recta
CHARS[K + 'cole-easteroll'] = {
    'body': 'delgado', 'pal': pal('#7a4a1e', '#c8915a', iris='#1a1210', shade='#603814', deep='#46280c'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'line', 'mouth_y': 98, 'nose': (50, 86, 3.6),
             'hairline': [(14, 60), (18, 48), (32, 44), (50, 44), (68, 44), (82, 48), (86, 60)],
             'face_front': blob([(18, 50), (50, 38), (82, 50), (84, 80), (76, 100), (60, 112), (50, 114), (40, 112), (24, 100), (16, 80)])},
    'front': [L(blob([(14, 66), (8, 40), (16, 14), (36, 0), (50, -2), (64, 0), (84, 14), (92, 40), (86, 66), (80, 48), (20, 48)], 8)),
              L(outline([(60, 0), (84, 14), (92, 42), (86, 62), (78, 36)]), 'shade', 'b', False),
              *thick_brows(64, 'deep', 3.6, 14, -0.6, 12)],
    'side': [L(blob([(82, 48), (90, 34), (82, 12), (58, -2), (30, 0), (10, 16), (2, 42), (6, 66), (22, 74), (36, 64), (46, 54), (66, 48)], 8)),
             L(outline([(4, 44), (30, 48), (40, 60), (24, 72), (8, 66)]), 'shade', 'b', False), *side_brow(64, 'deep', 3.6, -0.6)],
    'back': [L(blob([(12, 80), (6, 40), (16, 14), (36, 0), (50, -2), (64, 0), (84, 14), (94, 40), (88, 80), (50, 86)], 8)),
             L(outline([(58, 0), (84, 14), (94, 42), (88, 78), (62, 84)]), 'shade', 'b', False)],
}

# Colin Eager: pelo naranja con raya en medio, peinado en dos ondas hacia los lados y acabado en puntas que se abren hacia
# fuera a la altura de la mandíbula; ojos afilados amarillos y sonrisa
CHARS[K + 'colin-eager'] = {
    'body': 'normal', 'pal': pal('#e27c32', '#f2b878', iris='#d8b020', shade='#c0621e', deep='#9a4a12'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94,
             'hairline': [(14, 80), (16, 58), (26, 46), (40, 44), (48, 50), (52, 50), (60, 44), (74, 46), (84, 58), (86, 80)]},
    'front': [L(outline([(14, 86), (2, 94, 1), (8, 78), (8, 50), (14, 22), (32, 6), (50, 4), (68, 6), (86, 22), (92, 50), (92, 78), (98, 94, 1), (86, 86), (82, 60), (18, 60)])),
              L(outline([(60, 6), (84, 18), (92, 46), (92, 80), (96, 92), (86, 84), (80, 50)]), 'shade', 'b', False),
              strand([(50, 6), (50, 48)], 'deep', 'b', 1.2), strand([(46, 10), (30, 20), (20, 44)], 'deep', 'b', 1.0), strand([(54, 10), (70, 20), (80, 44)], 'deep', 'b', 1.0)],
    'side': [L(outline([(82, 54), (90, 40), (82, 16), (60, 2), (32, 4), (12, 18), (4, 42), (6, 70), (2, 92, 1), (16, 84), (30, 88, 1), (36, 74), (44, 60), (64, 54)])),
             L(outline([(4, 44), (30, 48), (40, 62), (30, 84), (10, 84)]), 'shade', 'b', False)],
    'back': [L(outline([(12, 86), (0, 94, 1), (6, 76), (6, 40), (18, 14), (40, 4), (60, 4), (82, 14), (94, 40), (94, 76), (100, 94, 1), (88, 86), (70, 90), (50, 92), (30, 90)])),
             L(outline([(58, 6), (82, 16), (94, 42), (94, 80), (86, 86), (62, 88)]), 'shade', 'b', False), strand([(50, 6), (50, 88)], 'deep', 'b', 1.0)],
}

# Colin Lection: piel morena, pelo verde oliva en pinchos salvajes que salen en todas direcciones; ojos afilados con dos rayas
# amarillas pintadas que bajan de los ojos, y una sonrisa con colmillo
CHARS[K + 'colin-lection'] = {
    'body': 'normal', 'pal': pal('#6a7232', '#a87040', iris='#1a1210', shade='#525a22', deep='#3a4014', paint='#d8c030'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(14, 64), (20, 52), (28, 60), (36, 48), (46, 58), (54, 46), (62, 58), (72, 48), (80, 58), (86, 64)]},
    'front': messy('front', amp=16, n=13, seed=61, lo=66) + [L([(34, 80), (35, 92)], 'paint', 'f', False, False, 2.2), L([(66, 80), (65, 92)], 'paint', 'f', False, False, 2.2),
                                                           L([(54, 95), (55, 99), (57, 95)], WHITE, 'f', False)],
    'side': messy('side', amp=16, n=13, seed=61, lo=66) + [L([(80, 82), (80, 92)], 'paint', 'f', False, False, 2.2)],
    'back': messy('back', amp=16, n=13, seed=61, lo=66, nape=90),
}

# Colin Salts: melena azul grisáceo en casco que le tapa las orejas, con el flequillo desfilado sobre los ojos; gafas
# redondas doradas, ojos castaños y boca seria
CHARS[K + 'colin-salts'] = {
    'body': 'normal', 'pal': pal('#5a8aa2', '#d8a066', iris='#8a5a30', shade='#467088', deep='#32566c', specs='#c8a040'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'frown', 'mouth_y': 93, 'ears': False,
             'hairline': [(12, 92), (15, 70), (20, 60), (30, 64), (38, 58), (48, 64), (56, 58), (66, 64), (74, 58), (82, 62), (86, 72), (88, 92)]},
    'front': bowl('front', side=94, w=4) + [strand([(30, 10), (26, 50)], 'deep', 'b', 1.0), strand([(50, 4), (50, 50)], 'deep', 'b', 1.0),
                                            strand([(70, 10), (74, 50)], 'deep', 'b', 1.0), *round_specs('front', 'specs', 76)],
    'side': bowl('side', nape=94, w=4) + round_specs('side', 'specs', 76),
    'back': bowl('back', nape=94, w=4),
}

WIDE = blob([(14, 50), (50, 38), (86, 50), (92, 78), (88, 100), (70, 112), (50, 114), (30, 112), (12, 100), (8, 78)])
LONG = blob([(18, 50), (50, 38), (82, 50), (84, 80), (76, 100), (60, 112), (50, 114), (40, 112), (24, 100), (16, 80)])


# Conan Fox (portero): grandullón de mandíbula enorme y piel morena; pelo verde muy oscuro cortísimo en un casquete pequeño
# con pico en la frente, orejas grandes, ojos blancos afilados, nariz y boca fruncida
CHARS[K + 'conan-fox'] = {
    'body': 'corpulento', 'pal': pal('#2a5a32', '#a8805a', iris='#f0f0f0', shade='#204a28', deep='#163a1e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'big_ears': 2, 'ear_out': 2, 'nose': (50, 88, 3.0),
             'hairline': False,
             'face_front': blob([(16, 50), (50, 36), (84, 50), (92, 80), (90, 104), (72, 116), (50, 118), (28, 116), (10, 104), (8, 80)])},
    'front': [skull(), L(outline([(22, 44), (24, 26), (36, 14), (50, 10), (64, 14), (76, 26), (78, 44), (64, 38), (50, 46), (36, 38)]), 'mid', 'f'),
              L(outline([(58, 12), (72, 20), (78, 40), (68, 34)]), 'shade', 'f', False)],
    'side': [L(outline([(80, 40), (78, 24), (64, 12), (44, 10), (26, 16), (20, 30), (36, 32), (56, 34), (70, 40)]))],
    'back': [L(blob([(26, 40), (30, 22), (50, 14), (70, 22), (74, 40), (50, 46)], 8))],
}

# Conn Pass: niño bajito de pelo verde azulado corto y desfilado, con el flequillo hasta las cejas; ojos de puntito, cejas
# enfadadas, nariz pequeña y sonrisa
CHARS[K + 'conn-pass'] = {
    'body': 'bajito', 'pal': pal('#4a8c8c', '#f2b878', iris='#1a1210', shade='#3a7070', deep='#2a5656'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'nose': (50, 84, 1.6),
             'hairline': [(14, 66), (18, 56), (28, 62), (36, 54), (46, 62), (54, 54), (62, 62), (72, 54), (80, 60), (86, 66)]},
    'front': [L(outline([(16, 72, 1), (10, 54), (10, 34), (22, 12), (42, 4), (62, 4), (80, 12), (90, 34), (90, 54), (84, 72, 1), (80, 54), (20, 54)])),
              L(outline([(62, 6), (80, 14), (90, 36), (88, 62), (80, 44)]), 'shade', 'b', False),
              *[strand([(x, 8 + abs(x - 50) * 0.2), (x + (x - 50) * 0.15, 54)], 'deep', 'b', 1.0) for x in (30, 44, 58, 72)]],
    'side': [L(outline([(82, 56), (88, 40), (82, 16), (60, 2), (32, 4), (12, 18), (4, 42), (6, 66), (14, 80, 1), (26, 72), (36, 66), (44, 58), (64, 56)])),
             L(outline([(5, 44), (30, 48), (40, 60), (24, 72), (10, 68)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 80, 1), (10, 56), (10, 34), (22, 12), (42, 4), (60, 4), (80, 12), (90, 34), (90, 56), (86, 80, 1), (70, 76), (60, 84, 1), (50, 76), (40, 84, 1),
                        (30, 76)])),
             L(outline([(58, 6), (80, 14), (90, 38), (88, 74), (64, 78)]), 'shade', 'b', False)],
}

# Connor Bation: pelo morado oscuro peinado en un tupé ondulado que cae hacia su izquierda, con los lados cortos; ojos
# afilados, cejas enfadadas y media sonrisa
CHARS[K + 'connor-bation'] = {
    'body': 'normal', 'pal': pal('#4c3c64', '#f2b878', iris='#1a1210', shade='#3a2c50', deep='#2a1e3c'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94,
             'hairline': [(16, 62), (18, 48), (30, 44), (46, 42), (60, 44), (74, 42), (84, 50), (86, 62)]},
    'front': [L(outline([(17, 66), (12, 44), (16, 20), (32, 4), (54, 0), (76, 6), (90, 18), (100, 30, 1), (90, 34), (88, 50), (84, 66), (80, 48), (20, 48)])),
              L(outline([(58, 2), (78, 8), (92, 22), (98, 30), (88, 34), (86, 54), (78, 32)]), 'shade', 'b', False),
              strand([(22, 24), (44, 10), (74, 12), (92, 26)], 'deep', 'b', 1.0), strand([(20, 40), (46, 26), (84, 34)], 'deep', 'b', 1.0)],
    'side': [L(outline([(80, 50), (92, 40), (100, 32, 1), (88, 26), (84, 12), (64, 0), (38, 0), (16, 10), (4, 34), (6, 60), (22, 70), (36, 62), (44, 54), (64, 50)])),
             L(outline([(5, 40), (30, 44), (40, 58), (24, 68), (8, 62)]), 'shade', 'b', False), strand([(86, 14), (60, 6), (24, 14)], 'deep', 'b', 1.0)],
    'back': crop('back', top=0, nape=80),
}

# Conor Abley (portero): piel morena, pelo verde oscuro de mechones de pincho largos barridos hacia su izquierda, que le caen
# por los lados; ojos afilados verdes y sonrisa
CHARS[K + 'conor-abley'] = {
    'body': 'normal', 'pal': pal('#2a6a4a', '#b08048', iris='#7aa040', shade='#205438', deep='#163e28'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'face_front': WIDE,
             'hairline': [(12, 76), (14, 58), (26, 50), (40, 54), (52, 46), (66, 50), (80, 46), (88, 60)]},
    'front': messy('front', amp=14, n=10, seed=71, lo=74, sweep=0.8) + [
              fr([(12, 66), (18, 42), (40, 28), (70, 26), (102, 18, 1), (84, 36), (66, 42), (56, 56, 1), (50, 42), (36, 50), (22, 76, 1)])],
    'side': messy('side', amp=14, n=10, seed=71, lo=74, sweep=0.8),
    'back': messy('back', amp=14, n=10, seed=71, lo=74, sweep=0.8, nape=92),
}

# Conor Trail (portero): cara ancha; pelo verde en casco con el flequillo en pico sobre la frente; ojos redondos grandes,
# cejas enfadadas y media sonrisa
CHARS[K + 'conor-trail'] = {
    'body': 'normal', 'pal': pal('#6a9a3a', '#f2b878', iris='#1a1210', shade='#527c2a', deep='#3c601c'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'face_front': WIDE,
             'hairline': [(10, 72), (14, 58), (30, 52), (44, 54), (50, 62), (56, 54), (70, 52), (86, 58), (90, 72)]},
    'front': bowl('front', top=6, side=78, w=2) + [strand([(50, 8), (50, 58)], 'deep', 'b', 1.0)],
    'side': bowl('side', top=6, nape=84, w=2),
    'back': bowl('back', top=6, nape=84, w=2),
}

# Cory Andish: piel clara, cara alargada y un gorrito redondo verde grisáceo con el borde amarillo y un moñito naranja
# arriba; ojos de puntito, cejas finas, nariz grande y sonrisa
CHARS[K + 'cory-andish'] = {
    'body': 'delgado', 'pal': pal('#3a2a20', '#f8d8a2', iris='#1a1210', hat='#4c6a52', hat_d='#3a5440', rim='#e0c040', knot='#c8501c'),
    'face': {'eyes': 'dot', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'nose': (50, 86, 3.2), 'hairline': False, 'face_front': LONG},
    'front': [L(outline([(16, 46), (16, 24), (30, 8), (50, 4), (70, 8), (84, 24), (84, 46), (50, 42)]), 'hat', 'f'),
              L(outline([(58, 6), (76, 14), (84, 30), (82, 44), (72, 28)]), 'hat_d', 'f', False),
              L(quad((14, 40), (50, 32), (86, 40)) + quad((86, 48), (50, 40), (14, 48)), 'rim', 'f', True),
              L(blob([(44, 6), (46, -6), (52, -12), (58, -4), (56, 6)], 6), 'knot', 'f', True)],
    'side': [L(outline([(80, 46), (82, 26), (70, 8), (48, 2), (26, 6), (12, 20), (8, 44), (44, 42)]), 'hat', 'f'),
             L(quad((84, 42), (50, 36), (6, 42)) + quad((6, 50), (50, 44), (84, 50)), 'rim', 'f', True),
             L(blob([(42, 4), (44, -8), (50, -12), (56, -4), (54, 4)], 6), 'knot', 'f', True)],
    'back': [L(outline([(14, 50), (14, 26), (28, 8), (50, 4), (72, 8), (86, 26), (86, 50), (50, 48)]), 'hat', 'f'),
             L(outline([(58, 6), (76, 14), (86, 30), (86, 48), (64, 48)]), 'hat_d', 'f', False),
             L(quad((12, 44), (50, 50), (88, 44)) + quad((88, 52), (50, 58), (12, 52)), 'rim', 'f', True),
             L(blob([(44, 6), (46, -6), (52, -12), (58, -4), (56, 6)], 6), 'knot', 'f', True)],
}

# Crane Clawson: piel morena, pelo rubio crema de pinchos revueltos con las puntas rosadas, y unas gafas de esquí blancas
# con el cristal oscuro sobre los ojos; media sonrisa
CHARS[K + 'crane-clawson'] = {
    'body': 'normal', 'pal': pal('#f2e2c4', '#a87a52', shade='#e0b4b0', deep='#c49490', frame='#f2ecdc', lens='#4a3448'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'face_front': WIDE,
             'hairline': [(10, 66), (18, 54), (26, 62), (34, 50), (44, 60), (52, 48), (60, 58), (70, 50), (78, 60), (86, 54), (90, 66)]},
    'front': messy('front', amp=16, n=12, seed=81, rx=52, lo=72) + [
              L(blob([(10, 68), (50, 64), (90, 68), (90, 84), (60, 86), (50, 80), (40, 86), (10, 84)], 6), 'frame', 'f', True),
              L(blob([(16, 72), (50, 69), (84, 72), (84, 81), (60, 82), (50, 77), (40, 82), (16, 81)], 6), 'lens', 'f', False)],
    'side': messy('side', amp=16, n=12, seed=81, rx=52, lo=72) + [
              L(blob([(70, 68), (90, 68), (92, 84), (72, 84)], 6), 'frame', 'f', True), L(blob([(74, 71), (89, 71), (90, 81), (75, 81)], 6), 'lens', 'f', False),
              L([(70, 74), (40, 70)], 'frame', 'f', False, False, 3.0)],
    'back': messy('back', amp=16, n=12, seed=81, rx=52, lo=72, nape=92) + [L(quad((6, 74), (50, 80), (94, 74)), 'frame', 'f', False, False, 3.2)],
}

# Creed Craving (portero): grandullón de piel morena y mandíbula ancha; pelo castaño claro corto peinado hacia atrás con las
# rayas del peine; orejas grandes, ojos afilados, nariz grande y sonrisa de dientes
CHARS[K + 'creed-craving'] = {
    'body': 'corpulento', 'pal': pal('#a68650', '#b08048', iris='#1a1210', shade='#8a6c3a', deep='#6e5228'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98, 'big_ears': 2, 'ear_out': 2, 'nose': (50, 86, 3.6),
             'hairline': [(16, 56), (20, 44), (34, 38), (50, 36), (66, 38), (80, 44), (84, 56)],
             'face_front': blob([(16, 50), (50, 36), (84, 50), (92, 80), (90, 104), (72, 116), (50, 118), (28, 116), (10, 104), (8, 80)])},
    'front': crop('front', top=8, side=58) + [strand([(x, 10 + abs(x - 50) * 0.2), (x + (x - 50) * 0.1, 38)], 'deep', 'b', 1.0) for x in (30, 40, 50, 60, 70)],
    'side': crop('side', top=8, nape=78) + [strand([(80 - k * 14, 14 + k * 2), (30 - k * 6, 26 + k * 8)], 'deep', 'b', 1.0) for k in range(3)],
    'back': crop('back', top=8, nape=78) + [strand([(x, 10), (x, 74)], 'deep', 'b', 1.0) for x in (34, 50, 66)],
}


# Creed Wrighter: gorro de bufón de dos colores (verde grisáceo a un lado y rosa rojizo al otro) con las puntas caídas y el
# borde crema; asoman rizos rubio oliva por la frente; ojos normales y sonrisa
CHARS[K + 'creed-wrighter'] = {
    'body': 'normal', 'pal': pal('#a89a50', '#d8a066', iris='#1a1210', shade='#8a7c3a', deep='#6c6028', hatl='#6a9a94', hatl_d='#4e7e78', hatr='#c86a6a', hatr_d='#a85050',
                                 rim='#f2e4c4'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 93, 'hairline': False},
    'front': [fr([(26, 64), (30, 52), (40, 48), (50, 54), (60, 48), (70, 52), (74, 64), (64, 58), (56, 64), (50, 58), (42, 64), (34, 58)]),
              L(outline([(14, 52), (6, 64, 1), (0, 30), (8, 10), (28, 0), (50, 2), (48, 46), (30, 46)]), 'hatl', 'f'),
              L(outline([(50, 2), (74, -2), (92, 8), (100, 30), (96, 66, 1), (86, 52), (70, 46), (52, 46)]), 'hatr', 'f'),
              L(outline([(76, 2), (92, 10), (98, 32), (94, 60), (86, 44)]), 'hatr_d', 'f', False),
              L(quad((14, 48), (50, 32), (86, 48)) + quad((86, 60), (50, 44), (14, 60)), 'rim', 'f', True)],
    'side': [L(outline([(84, 50), (88, 30), (78, 8), (54, -2), (40, 0), (40, 46)]), 'hatr', 'f'),
             L(outline([(40, 0), (20, 4), (4, 20), (-4, 56, 1), (8, 52), (40, 46)]), 'hatl', 'f'),
             L(quad((86, 46), (50, 38), (6, 48)) + quad((6, 58), (50, 48), (86, 56)), 'rim', 'f', True),
             fr([(78, 58), (82, 52), (90, 54), (88, 62)])],
    'back': [L(outline([(14, 60), (2, 70, 1), (0, 32), (8, 10), (28, 0), (50, 2), (50, 56), (30, 56)]), 'hatr', 'f'),
             L(outline([(50, 2), (72, 0), (92, 10), (100, 32), (98, 70, 1), (86, 60), (70, 56), (50, 56)]), 'hatl', 'f'),
             L(quad((14, 54), (50, 62), (86, 54)) + quad((86, 66), (50, 74), (14, 66)), 'rim', 'f', True)],
}

# Crispin Shooter (portero): grandullón de pelo verde oscuro en pinchos grandes, con dos mechones naranja rojizo que le caen
# por el centro de la frente, y unas gafas de esquí de montura verde agua y cristal amarillo pálido; sonrisa
CHARS[K + 'crispin-shooter'] = {
    'body': 'corpulento', 'pal': pal('#2a6a3c', '#f2b878', shade='#20542e', deep='#163e20', lock='#c84a1c', frame='#6aa0a8', lens='#f4eab8'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'face_front': WIDE,
             'hairline': [(10, 66), (18, 54), (26, 62), (34, 50), (44, 60), (52, 48), (60, 58), (70, 50), (78, 60), (86, 54), (90, 66)]},
    'front': messy('front', amp=16, n=11, seed=91, rx=52, lo=70) + [
              fr([(40, 30), (50, 32), (46, 50), (40, 66, 1), (38, 48)], 'lock'), fr([(52, 30), (62, 30), (60, 46), (54, 64, 1), (52, 46)], 'lock'),
              L(blob([(12, 68), (50, 64), (88, 68), (90, 84), (62, 86), (50, 80), (38, 86), (10, 84)], 6), 'frame', 'f', True),
              L(blob([(18, 71), (50, 68), (82, 71), (82, 81), (60, 82), (50, 77), (40, 82), (18, 81)], 6), 'lens', 'f', False)],
    'side': messy('side', amp=16, n=11, seed=91, rx=52, lo=70) + [
              L(blob([(70, 68), (90, 68), (92, 84), (72, 84)], 6), 'frame', 'f', True), L(blob([(74, 71), (89, 71), (90, 81), (75, 81)], 6), 'lens', 'f', False),
              L([(70, 74), (40, 70)], 'frame', 'f', False, False, 3.0), fr([(80, 46), (88, 48), (90, 64, 1), (82, 56)], 'lock')],
    'back': messy('back', amp=16, n=11, seed=91, rx=52, lo=70, nape=92) + [L(quad((6, 74), (50, 80), (94, 74)), 'frame', 'f', False, False, 3.2)],
}

# Cruz Ligner: melena rubio pálido en casco con un flequillo barrido que le tapa un ojo y las puntas de los lados rosadas;
# ojos redondos grandes con pestañas y sonrisa
CHARS[K + 'cruz-ligner'] = {
    'body': 'normal', 'pal': pal('#f2ecb4', '#d8a066', iris='#1a1210', shade='#d8d098', deep='#c09aa0'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'ears': False,
             'hairline': [(14, 82), (16, 62), (26, 56), (40, 60), (56, 56), (70, 62), (80, 70), (86, 84)]},
    'front': bowl('front', top=2, side=86, w=2) + [
              fr([(16, 60), (22, 40), (44, 26), (72, 26), (88, 40), (86, 60), (78, 56), (72, 80, 1), (66, 58), (52, 50), (36, 52), (24, 66, 1)]),
              L(outline([(10, 78), (14, 90, 1), (18, 76)]), 'deep', 'b', False), L(outline([(90, 78), (86, 90, 1), (82, 76)]), 'deep', 'b', False),
              strand([(30, 34), (56, 32), (74, 40)], 'shade', 'f', 1.0), *lashes_out(75, 14)],
    'side': bowl('side', top=2, nape=88, w=2) + [L(outline([(28, 84), (24, 96, 1), (36, 86)]), 'deep', 'b', False)],
    'back': bowl('back', top=2, nape=88, w=2),
}

# Dai Hart: piel morena, pelo verde azulado oscuro de pinchos con un remolino arriba y un pico en la frente; ojos afilados
# verde pálido, cejas enfadadas y media sonrisa
CHARS[K + 'dai-hart'] = {
    'body': 'normal', 'pal': pal('#4a6a64', '#b08048', iris='#a8a85a', shade='#3a5650', deep='#2a403c'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93,
             'hairline': [(16, 68), (20, 54), (30, 46), (42, 50), (50, 62), (58, 50), (70, 46), (80, 54), (84, 68)]},
    'front': [L(outline([(17, 72), (10, 54, 1), (14, 38), (4, 28, 1), (18, 22), (30, 8), (44, 4), (46, -12, 1), (54, 0), (62, -6, 1), (62, 6), (76, 10), (84, 22), (96, 28, 1),
                         (86, 38), (90, 54, 1), (83, 72), (80, 52), (20, 52)])),
              L(outline([(60, 6), (76, 12), (86, 26), (92, 30), (86, 40), (84, 62), (78, 40)]), 'shade', 'b', False)],
    'side': [L(outline([(80, 52), (88, 40, 1), (82, 30), (90, 18, 1), (74, 12), (62, -2), (60, -12, 1), (50, 2), (30, 4), (12, 16), (6, 38), (0, 50, 1), (8, 60), (14, 76, 1),
                        (26, 70), (36, 64), (44, 56), (64, 52)])),
             L(outline([(6, 40), (30, 46), (40, 58), (26, 70), (12, 66)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 80), (8, 56, 1), (12, 38), (2, 28, 1), (16, 22), (28, 8), (44, 4), (46, -12, 1), (54, 0), (62, -6, 1), (62, 6), (78, 10), (86, 22), (98, 28, 1),
                        (88, 38), (92, 56, 1), (84, 80), (50, 86)])),
             L(outline([(58, 6), (80, 14), (90, 36), (88, 56), (84, 78), (62, 84)]), 'shade', 'b', False)],
}

# Daley Switcher: cara ancha; pelo castaño oliva corto en pinchos con patillas; cejas pobladas enormes, ojos pequeños y boca
# fruncida
CHARS[K + 'daley-switcher'] = {
    'body': 'corpulento', 'pal': pal('#8a7040', '#f2b878', iris='#1a1210', shade='#6e5830', deep='#524020'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'nose': (50, 86, 3.0), 'face_front': WIDE,
             'hairline': [(12, 74), (14, 54), (26, 48), (38, 52), (50, 46), (62, 52), (74, 48), (86, 54), (88, 74)]},
    'front': [L(outline([(13, 78), (10, 50), (12, 30), (4, 24, 1), (20, 20), (26, 6, 1), (38, 12), (48, 0, 1), (56, 10), (68, 2, 1), (72, 14), (84, 18), (96, 24, 1),
                         (88, 32), (90, 50), (87, 78), (80, 52), (20, 52)])),
              L(outline([(60, 8), (72, 14), (86, 20), (92, 28), (88, 50), (86, 70), (78, 40)]), 'shade', 'b', False),
              *thick_brows(64, 'mid', 5.0, 15, -0.6, 15)],
    'side': [L(outline([(80, 50), (88, 38), (84, 22), (92, 16, 1), (76, 10), (70, -2, 1), (56, 6), (40, -2, 1), (32, 8), (14, 14), (4, 36), (6, 60), (16, 80), (28, 80),
                        (38, 64), (44, 56), (64, 50)])),
             L(outline([(5, 40), (30, 46), (40, 58), (28, 78), (12, 74)]), 'shade', 'b', False), *side_brow(64, 'mid', 5.0, -0.6)],
    'back': crop('back', top=2, w=4, nape=82),
}

# Dan Carpenter (portero): cara ancha; pelo castaño oscuro abundante en casco con un flequillo desfilado que le tapa un ojo;
# ojos blancos de puntito y sonrisa
CHARS[K + 'dan-carpenter'] = {
    'body': 'corpulento', 'pal': pal('#4c2e1e', '#f2b878', iris='#1a1210', shade='#3a2214', deep='#28160c'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'face_front': WIDE, 'ears': False,
             'hairline': [(10, 84), (12, 64), (22, 58), (32, 64), (40, 56), (54, 60), (62, 70), (70, 60), (80, 62), (88, 84)]},
    'front': bowl('front', top=0, side=88, w=4) + [
              fr([(24, 44), (44, 34), (66, 36), (82, 50), (74, 60), (66, 86, 1), (60, 58), (50, 50), (40, 58), (32, 66, 1), (28, 54)]),
              strand([(40, 40), (58, 40)], 'deep', 'f', 1.0)],
    'side': bowl('side', top=0, nape=90, w=4),
    'back': bowl('back', top=0, nape=90, w=4),
}

# Dan Castella (portero): grandullón de piel morena y cara redonda; pelo verde oliva muy oscuro en trenzas pegadas hacia atrás
# que le cuelgan por detrás de las orejas hasta el cuello; ojos entornados, una cicatriz en la mejilla y boca recta
CHARS[K + 'dan-castella'] = {
    'body': 'corpulento', 'pal': pal('#3e3e22', '#a87c52', iris='#1a1210', shade='#2e2e18', deep='#20200e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 98, 'nose': (50, 86, 3.0), 'face_front': WIDE,
             'hairline': [(14, 56), (18, 44), (32, 38), (50, 36), (68, 38), (82, 44), (86, 56)]},
    'front': crop('front', top=6, side=60, w=2) + [*[strand([(x, 8 + abs(x - 50) * 0.2), (x + (x - 50) * 0.15, 40)], 'deep', 'b', 1.2) for x in (30, 40, 50, 60, 70)],
                                                   *dread((14, 66), (8, 106), 3.4), *dread((86, 66), (92, 106), 3.4),
                                                   L([(66, 86), (74, 82)], (110, 70, 50, 255), 'f', False, False, 1.2)],
    'side': crop('side', top=6, nape=80, w=2) + [*[strand([(84 - k * 4, 16 + k * 10), (20, 30 + k * 12)], 'deep', 'b', 1.2) for k in range(4)],
                                                 *dread((20, 76), (14, 108), 3.4), *dread((34, 74), (32, 108), 3.4)],
    'back': crop('back', top=6, nape=80, w=2) + [*[strand([(x, 8), (x + (x - 50) * 0.1, 76)], 'deep', 'b', 1.2) for x in (26, 38, 50, 62, 74)],
                                                 *dread((24, 76), (20, 108), 3.4), *dread((40, 80), (40, 110), 3.4), *dread((60, 80), (60, 110), 3.4),
                                                 *dread((76, 76), (80, 108), 3.4)],
}

# Dan Dandy: piel morena, melena azul marino violáceo con flequillo y las puntas de los lados en pico abiertas a la altura de la
# mandíbula; ojos violeta y boca seria
CHARS[K + 'dan-dandy'] = {
    'body': 'normal', 'pal': pal('#2e2c5e', '#b8864e', iris='#9a8ad0', shade='#24224c', deep='#1a183a'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'ears': False,
             'hairline': [(12, 84), (14, 64), (24, 58), (34, 64), (44, 56), (54, 62), (64, 56), (74, 62), (84, 60), (88, 84)]},
    'front': [L(outline([(14, 86), (0, 98, 1), (6, 80), (6, 40), (18, 14), (40, 2), (62, 2), (82, 14), (94, 40), (94, 80), (100, 98, 1), (86, 86), (82, 62), (18, 62)])),
              L(outline([(62, 4), (84, 16), (94, 42), (94, 82), (98, 94), (86, 84), (80, 50)]), 'shade', 'b', False),
              L(blob([(20, 10), (40, 4), (46, 10), (30, 18)], 6), 'light', 'b', False)],
    'side': [L(outline([(82, 58), (88, 42), (82, 16), (60, 2), (32, 4), (12, 18), (2, 44), (4, 74), (0, 94, 1), (18, 84), (34, 92, 1), (40, 76), (50, 62), (66, 58)])),
             L(outline([(4, 44), (30, 50), (42, 64), (30, 86), (10, 86)]), 'shade', 'b', False)],
    'back': [L(outline([(12, 86), (-2, 98, 1), (4, 76), (6, 40), (18, 14), (40, 2), (60, 2), (82, 14), (94, 40), (96, 76), (102, 98, 1), (88, 86), (70, 92), (50, 94),
                        (30, 92)])),
             L(outline([(58, 4), (82, 14), (94, 42), (96, 80), (88, 86), (62, 90)]), 'shade', 'b', False)],
}


# Dan Drobium: pelo castaño oliva peinado hacia atrás con las rayas del peine, que le cae por los lados hasta la mandíbula y
# se abre en puntas; ojos rojizos con pestañas, cejas arqueadas y media sonrisa ladeada
CHARS[K + 'dan-drobium'] = {
    'body': 'normal', 'pal': pal('#9a8040', '#f2b878', iris='#b05a5a', shade='#7e682e', deep='#625020'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94,
             'hairline': [(16, 66), (18, 46), (30, 38), (50, 34), (70, 38), (82, 46), (84, 66)]},
    'front': [L(outline([(16, 90), (4, 96, 1), (10, 80), (10, 40), (20, 14), (40, 2), (60, 2), (80, 14), (90, 40), (90, 80), (96, 96, 1), (84, 90), (82, 56), (18, 56)])),
              L(outline([(60, 4), (80, 16), (90, 42), (90, 82), (94, 94), (84, 86), (80, 50)]), 'shade', 'b', False),
              *[strand([(x, 4 + abs(x - 50) * 0.2), (x + (x - 50) * 0.35, 40)], 'deep', 'b', 1.0) for x in (28, 38, 46, 54, 62, 72)], *lashes_out(75, 14)],
    'side': [L(outline([(80, 44), (84, 30), (76, 10), (54, -2), (30, 2), (12, 16), (4, 40), (6, 74), (2, 94, 1), (18, 86), (30, 90, 1), (36, 74), (44, 58), (62, 46)])),
             L(outline([(5, 44), (30, 48), (40, 62), (30, 84), (10, 84)]), 'shade', 'b', False),
             *[strand([(80 - k * 10, 10 + k * 3), (20 - k * 2, 36 + k * 10)], 'deep', 'b', 1.0) for k in range(4)]],
    'back': [L(outline([(12, 90), (0, 96, 1), (6, 78), (8, 40), (18, 14), (40, 2), (60, 2), (82, 14), (92, 40), (94, 78), (100, 96, 1), (88, 90), (70, 92), (50, 94), (30, 92)])),
             L(outline([(58, 4), (82, 14), (92, 42), (94, 80), (86, 88), (62, 90)]), 'shade', 'b', False),
             *[strand([(x, 4), (x + (x - 50) * 0.1, 88)], 'deep', 'b', 1.0) for x in (30, 42, 50, 58, 70)]],
}

# Dan Nettles (portero): grandullón de piel morena y cabeza de huevo, rapado salvo un bloque plano de pelo rubio crema en lo
# alto, como un taco; ojos blancos amarillentos, ceño fruncido, nariz ancha, boca torcida y papada
CHARS[K + 'dan-nettles'] = {
    'body': 'corpulento', 'pal': pal('#eee4ae', '#a07a5a', iris='#2a2020', shade='#d6c890', deep='#bca870'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'nose': (50, 88, 4.0), 'hairline': False, 'ear_out': 2,
             'face_front': blob([(16, 50), (50, 36), (84, 50), (92, 80), (90, 104), (72, 116), (50, 118), (28, 116), (10, 104), (8, 80)])},
    'front': [L(blob([(22, 52), (22, 30), (34, 14), (50, 10), (66, 14), (78, 30), (78, 52)], 8), 'skin'),
              L(outline([(32, 18), (30, -2), (36, -8), (64, -8), (70, -2), (68, 18), (58, 14), (50, 20), (42, 14)]), 'mid', 'f'),
              L(outline([(56, -8), (64, -8), (70, -2), (68, 16), (60, 12)]), 'shade', 'f', False),
              L(quad((32, 112), (50, 118), (68, 112)), (120, 80, 60, 255), 'f', False, False, 1.0)],
    'side': [L(outline([(46, 18), (44, -2), (50, -8), (72, -8), (78, -2), (76, 22), (60, 20)]), 'mid', 'f')],
    'back': [L(outline([(32, 22), (30, -2), (36, -8), (64, -8), (70, -2), (68, 22), (50, 26)]), 'mid', 'f')],
}

# Dan Rhino: grandullón de piel tostada; pelo castaño oscuro corto y engominado hacia atrás; orejas grandes, ojos cerrados
# apretados de enfado con un toque rojo, nariz marrón grande y boca fruncida
CHARS[K + 'dan-rhino'] = {
    'body': 'corpulento', 'pal': pal('#4a3020', '#c8925a', iris='#1a1210', shade='#3a2416', deep='#28180c'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'big_ears': 3, 'ear_out': 2, 'face_front': WIDE,
             'hairline': [(16, 54), (20, 44), (34, 38), (50, 36), (66, 38), (80, 44), (84, 54)]},
    'front': crop('front', top=8, side=56) + [strand([(x, 10 + abs(x - 50) * 0.2), (x + (x - 50) * 0.1, 38)], 'deep', 'b', 1.0) for x in (32, 42, 50, 58, 68)] + [
              L([(28, 72), (42, 76)], BLACK, 'f', False, False, 2.4), L([(72, 72), (58, 76)], BLACK, 'f', False, False, 2.4),
              L([(26, 68), (32, 70)], (200, 60, 40, 255), 'f', False, False, 1.4), L([(74, 68), (68, 70)], (200, 60, 40, 255), 'f', False, False, 1.4),
              L([(36, 64), (44, 68)], BLACK, 'f', False, False, 2.0), L([(64, 64), (56, 68)], BLACK, 'f', False, False, 2.0),
              L(blob([(42, 82), (58, 82), (60, 90), (50, 92), (40, 90)], 6), (150, 90, 60, 255), 'f', False, True)],
    'side': crop('side', top=8, nape=78) + [L([(74, 74), (86, 76)], BLACK, 'f', False, False, 2.4),
                                            L(blob([(84, 82), (94, 84), (92, 92), (84, 92)], 6), (150, 90, 60, 255), 'f', False, True)],
    'back': crop('back', top=8, nape=78),
}
