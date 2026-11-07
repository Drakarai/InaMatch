"""Ojeadores de IE1 (scouts-ie1), tanda 06 (de heath-freke a josh-rogan): dibujados a partir de su retrato de Victory Road
(ninguno tiene modelo 3D en la enciclopedia); claves 'scouts-ie1:<id>'. Todos son chicos según la wiki."""
from chars import CHARS, L, OUTC, blob, ell, longhair, messy, outline, pal, rope, strand  # noqa: F401
from chars_vr_nikogawa import WIDE, brow_side, brows, crop, ring_glasses, wide_smile  # noqa: F401
from heads import quad  # noqa: F401

K = 'scouts-ie1:'
WHITE = (248, 248, 248, 255)
BLACK = (34, 28, 30, 255)
PAINT = (184, 64, 40, 255)
LIP = (200, 110, 80, 255)


def fr(pts, c='mid'):
    """Flequillo o mechón por delante de la cara (con su línea de contorno)."""
    return L(outline(pts), c, 'f', ln=True)


def fringe(bottom, top=30, c='mid', w=1.2):
    """Flequillo que sale de la masa del pelo: solo lleva contorno en las puntas de abajo (bottom, de izquierda a derecha;
    las puntas con tercer valor), no arriba, así no parece una cinta."""
    pts = [(bottom[0][0], top)] + list(bottom) + [(bottom[-1][0], top)]
    return [L(outline(pts), c, 'f', False), L([p[:2] for p in bottom], OUTC, 'f', False, False, w)]


def dots(pts, c=(176, 110, 70, 255), r=1.0):
    """Pecas o lunares."""
    return [L(ell(x, y, r, r), c, 'f', False) for x, y in pts]


def freckles(y=86, dx=24, c=(176, 110, 70, 255)):
    return dots([(50 - dx + a, y + b) for a, b in ((-3, 0), (0, 2), (3, 0))] + [(50 + dx + a, y + b) for a, b in ((-3, 0), (0, 2), (3, 0))], c)


def side_lines(y=84, dx=27, c=OUTC):
    """Rayitas de expresión en las mejillas."""
    return [L([(50 - dx - 2, y - 2), (50 - dx + 2, y + 2)], c, 'f', False, False, 1.0), L([(50 + dx + 2, y - 2), (50 + dx - 2, y + 2)], c, 'f', False, False, 1.0)]


def paint(view, y=84, c=PAINT, kind='tri'):
    """Pintura de guerra en las mejillas: triángulos ('tri') o franjas ('bar')."""
    if view == 'front':
        if kind == 'tri':
            return [L(blob([(20, y - 4), (36, y - 2), (24, y + 6)], 4), c, 'f', False), L(blob([(80, y - 4), (64, y - 2), (76, y + 6)], 4), c, 'f', False)]
        return [L(outline([(28, y - 10), (33, y - 10), (31, y + 8), (27, y + 6)]), c, 'f', False), L(outline([(72, y - 10), (67, y - 10), (69, y + 8), (73, y + 6)]), c, 'f', False)]
    if view == 'side':
        if kind == 'tri':
            return [L(blob([(64, y - 4), (78, y - 2), (68, y + 6)], 4), c, 'f', False)]
        return [L(outline([(70, y - 10), (75, y - 10), (73, y + 8), (69, y + 6)]), c, 'f', False)]
    return []


def band(view, y=40, h=10, c='band', c2=None, tails=False):
    """Cinta o vendaje alrededor de la cabeza (c2: la raya de en medio)."""
    out = []
    if view == 'front':
        out.append(L(outline([(9, y + 2), (50, y - 4), (91, y + 2), (91, y + h + 2), (50, y + h - 4), (9, y + h + 2)]), c, 'f', ln=True))
        if c2:
            out.append(L(outline([(9, y + h * 0.35 + 2), (50, y + h * 0.35 - 4), (91, y + h * 0.35 + 2), (91, y + h * 0.65 + 2), (50, y + h * 0.65 - 4),
                                  (9, y + h * 0.65 + 2)]), c2, 'f', False))
    elif view == 'side':
        out.append(L(outline([(0, y + 6), (50, y - 2), (93, y - 4), (93, y + h - 4), (50, y + h - 2), (2, y + h + 6)]), c, 'f', ln=True))
        if c2:
            out.append(L(outline([(1, y + 6 + h * 0.35), (50, y - 2 + h * 0.35), (93, y - 4 + h * 0.35), (93, y - 4 + h * 0.65), (50, y - 2 + h * 0.65),
                                  (2, y + 6 + h * 0.65)]), c2, 'f', False))
        if tails:
            out += [L(outline([(4, y + 6), (-12, y + 34, 1), (-4, y + 36), (6, y + 14)]), c, 'f', ln=True),
                    L(outline([(6, y + 8), (-2, y + 44, 1), (6, y + 44), (10, y + 14)]), c, 'f', ln=True)]
    else:
        out.append(L(outline([(8, y + 4), (50, y + 8), (92, y + 4), (92, y + h + 4), (50, y + h + 8), (8, y + h + 4)]), c, 'f', ln=True))
        if c2:
            out.append(L(outline([(8, y + 4 + h * 0.35), (50, y + 8 + h * 0.35), (92, y + 4 + h * 0.35), (92, y + 4 + h * 0.65), (50, y + 8 + h * 0.65),
                                  (8, y + 4 + h * 0.65)]), c2, 'f', False))
        if tails:
            out += [L(outline([(44, y + 10), (36, y + 44, 1), (44, y + 42), (50, y + 14)]), c, 'f', ln=True),
                    L(outline([(52, y + 12), (58, y + 46, 1), (64, y + 42), (56, y + 12)]), c, 'f', ln=True)]
    return out


def glasses_band(view, y=76, frame=(200, 40, 30, 255), lens=(236, 200, 80, 255), w=9.0):
    """Gafas de sol de montura gruesa y cristales de color."""
    if view == 'front':
        out = []
        for cx in (35, 65):
            out.append(L(blob([(cx - 13, y - 5), (cx + 12, y - 6), (cx + 12, y + 3), (cx, y + 6), (cx - 12, y + 3)], 5), frame, 'f', ln=True))
            out.append(L(blob([(cx - 10, y - 3), (cx + 9.5, y - 4), (cx + 9.5, y + 2), (cx, y + 4), (cx - 9.5, y + 2)], 5), lens, 'f', False))
        out.append(L([(46, y - 3), (54, y - 3)], frame, 'f', False, False, 2.6))
        return out
    if view == 'side':
        return [L(blob([(74, y - 6), (90, y - 6), (90, y + 3), (78, y + 5)], 5), frame, 'f', ln=True), L(blob([(77, y - 4), (88, y - 4), (88, y + 2), (79, y + 3)], 5), lens, 'f', False),
                L([(74, y - 3), (48, y - 6)], frame, 'f', False, False, 2.4)]
    return [L([(9, y - 4), (13, y - 3)], frame, 'f', False, False, 2.4), L([(91, y - 4), (87, y - 3)], frame, 'f', False, False, 2.4)]


def bald(view, c='skin'):
    """Coronilla calva (la cabeza entera de piel): para los que llevan solo una cresta."""
    if view == 'side':
        return [L(blob([(48, 14), (74, 16), (88, 34), (88, 56), (50, 54), (20, 70), (8, 46), (16, 24)], 6), c, 'b')]
    return [L(blob([(16, 62), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 62), (50, 58)], 6), c, 'b')]


# ---------------------------------------------------------------------------------------------------------------- hoja 0

# Heath Freke (portero): pelo azul grisáceo claro peinado de lado, con un mechón grande que le cae en diagonal por la frente
# hacia su derecha y las sienes canosas; ojos azul claro y media sonrisa de lado
CHARS[K + 'heath-freke'] = {
    'body': 'normal', 'pal': pal('#a2cace', '#f4c28c', iris='#7ab8cc', shade='#7ea4aa', deep='#5e8288', grey='#8e9aa0'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 92,
             'hairline': [(16, 64), (18, 50), (34, 46), (52, 42), (68, 40), (82, 46), (84, 62)]},
    'front': crop('front', top=4, side=64, w=2)
             + [L(outline([(82, 44), (88, 44), (86, 64), (83, 64)]), 'grey', 'f', False), L(outline([(18, 50), (12, 48), (14, 64), (17, 64)]), 'grey', 'f', False),
                fr([(12, 52), (12, 34), (24, 14), (44, 6), (62, 8), (70, 16), (62, 22), (50, 30), (38, 42), (28, 54), (20, 66, 1)]),
                strand([(56, 12), (40, 26), (26, 48)], 'deep', 'f', 1.0), strand([(66, 12), (74, 24), (80, 40)], 'deep', 'b', 1.0)],
    'side': crop('side', top=2, nape=84, w=2)
            + [L(outline([(36, 66), (42, 56), (50, 54), (46, 66)]), 'grey', 'f', False), strand([(78, 10), (62, 20), (40, 28)], 'deep', 'b', 1.0),
               fr([(70, 10), (86, 18), (92, 34), (88, 48, 1), (80, 36), (70, 24)])],
    'back': crop('back', top=4, nape=84, w=2) + [strand([(30, 12), (50, 30), (60, 60)], 'deep', 'b', 1.0)],
}

# Heath Rower: gorro de aviador de cuero rojizo con las gafas subidas a la frente y orejeras con un auricular redondo;
# debajo, melena rubia corta hasta la barbilla con un flequillo recto; ojos amarillo verdoso
CHARS[K + 'heath-rower'] = {
    'body': 'normal', 'pal': pal('#f2dc9e', '#f4c28c', iris='#a69a34', shade='#d4ba78', deep='#a8905a', cap='#ae5a4c', cap_d='#8a4238',
                                  goggle='#8c6a52', lens='#5e4038', metal='#a8a29c'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    'front': [L(outline([(14, 96), (12, 60), (16, 40), (84, 40), (88, 60), (86, 96), (78, 96), (78, 64), (22, 64), (22, 96)])),
              fr([(18, 68), (18, 40), (82, 40), (82, 68), (72, 66), (62, 68), (50, 66), (38, 68), (28, 66)]),
              strand([(30, 46), (30, 66)], 'deep', 'f', 1.0), strand([(42, 46), (42, 66)], 'deep', 'f', 1.0), strand([(58, 46), (58, 66)], 'deep', 'f', 1.0),
              strand([(70, 46), (70, 66)], 'deep', 'f', 1.0),
              L(outline([(8, 64), (6, 30), (22, 6), (50, -2), (78, 6), (94, 30), (92, 64), (84, 46), (16, 46)]), 'cap', 'f', ln=True),
              L(outline([(60, 0), (80, 8), (94, 30), (92, 60), (86, 44), (78, 22)]), 'cap_d', 'f', False),
              L(outline([(4, 50), (18, 48), (20, 98), (8, 98)]), 'cap', 'f', ln=True), L(outline([(96, 50), (82, 48), (80, 98), (92, 98)]), 'cap', 'f', ln=True),
              L(ell(12, 76, 7, 8), 'metal', 'f', ln=True), L(ell(88, 76, 7, 8), 'metal', 'f', ln=True),
              L(ell(12, 76, 3.5, 4), 'cap_d', 'f', False), L(ell(88, 76, 3.5, 4), 'cap_d', 'f', False),
              L([(8, 30), (92, 30)], 'goggle', 'f', False, False, 3.0),
              L(ell(36, 26, 13, 10), 'goggle', 'f', ln=True), L(ell(64, 26, 13, 10), 'goggle', 'f', ln=True),
              L(ell(36, 26, 9, 6.5), 'lens', 'f', False), L(ell(64, 26, 9, 6.5), 'lens', 'f', False)],
    'side': [L(outline([(4, 62), (30, 62), (32, 94), (10, 94)])),
             L(outline([(4, 62), (2, 32), (18, 6), (50, -4), (78, 4), (92, 24), (93, 44), (80, 44), (60, 42), (46, 50), (30, 62)]), 'cap'),
             L(outline([(4, 40), (40, 42), (44, 56), (30, 62), (4, 62)]), 'cap_d', 'b', False),
             fr([(78, 40), (92, 40), (93, 66), (84, 64)]),
             L(outline([(36, 50), (56, 50), (58, 96), (40, 98)]), 'cap', 'f', ln=True), L(ell(47, 74, 7, 8), 'metal', 'f', ln=True), L(ell(47, 74, 3.5, 4), 'cap_d', 'f', False),
             L([(2, 28), (80, 22)], 'goggle', 'f', False, False, 3.0), L(ell(80, 22, 9, 10), 'goggle', 'f', ln=True), L(ell(82, 22, 5.5, 7), 'lens', 'f', False)],
    'back': [L(outline([(12, 60), (88, 60), (86, 96), (14, 96)])),
             L(outline([(8, 66), (6, 30), (22, 6), (50, -2), (78, 6), (94, 30), (92, 66), (50, 68)]), 'cap'),
             L(outline([(58, 2), (80, 10), (94, 32), (92, 64), (64, 66)]), 'cap_d', 'b', False),
             L(outline([(4, 50), (16, 50), (18, 98), (6, 98)]), 'cap', 'f', ln=True), L(outline([(96, 50), (84, 50), (82, 98), (94, 98)]), 'cap', 'f', ln=True),
             L([(6, 30), (94, 30)], 'goggle', 'f', False, False, 3.0)],
}

# Herb Ivore: pelo morado pizarra en cepillo alto y plano (flat-top) con los lados cortos; ojos negros enormes y redondos,
# cejas moradas, una cicatriz en cruz en la frente y una sonrisita
CHARS[K + 'herb-ivore'] = {
    'body': 'normal', 'pal': pal('#4e4c6e', '#f4c28c', shade='#3c3a58', deep='#2a2840', brow='#7c7aa8'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'eye_sep': 13,
             'hairline': [(17, 62), (18, 48), (30, 44), (50, 44), (70, 44), (82, 48), (83, 62)]},
    'front': [L(outline([(17, 64), (13, 40), (13, 6, 1), (24, -4), (50, -6), (78, -6), (88, -2, 1), (87, 40), (83, 64), (78, 48), (22, 48)])),
              L(outline([(58, -4), (86, -2), (86, 40), (82, 60), (76, 30)]), 'shade', 'b', False),
              strand([(30, 0), (32, 30)], 'deep', 'b', 1.0), strand([(50, -2), (50, 30)], 'deep', 'b', 1.0), strand([(68, 0), (68, 30)], 'deep', 'b', 1.0)]
             + brows(64, 'brow', 4.5, 13, 0.2, 12)
             + [L([(34, 50), (40, 56)], OUTC, 'f', False, False, 1.2), L([(40, 50), (34, 56)], OUTC, 'f', False, False, 1.2)] + side_lines(86, 26),
    'side': [L(outline([(66, 50), (80, 46), (88, 30), (88, -2, 1), (60, -6), (28, -6), (8, 6, 1), (4, 30), (6, 60), (18, 80), (32, 78), (38, 64), (46, 56), (58, 52)])),
             L(outline([(5, 40), (30, 44), (40, 60), (32, 78), (18, 80), (6, 62)]), 'shade', 'b', False)] + brow_side(64, 'brow', 4.5),
    'back': [L(outline([(17, 76), (13, 40), (13, 6, 1), (24, -4), (50, -6), (76, -4), (87, 6, 1), (87, 40), (83, 76), (66, 84), (50, 86), (34, 84)])),
             L(outline([(58, -4), (86, 6), (86, 40), (82, 76), (62, 80)]), 'shade', 'b', False)],
}

# Herc Bigsby: grandullón de piel tostada con el pelo amarillo en pinchos de punta hacia arriba y hacia los lados, ojos
# apretados de rabia, cejas amarillas, pintura de guerra roja en las mejillas y labios gordos
CHARS[K + 'herc-bigsby'] = {
    'body': 'corpulento', 'pal': pal('#eac232', '#b87c4c', shade='#c49a1e', deep='#9a7414'),
    'face': {'eyes': 'closed', 'brows': 'angry', 'mouth': 'none', 'face_front': WIDE,
             'hairline': [(14, 60), (20, 46), (30, 52), (40, 42), (50, 50), (60, 42), (70, 52), (80, 46), (86, 60)]},
    'front': [L(outline([(16, 62), (2, 52, 1), (12, 40), (0, 24, 1), (18, 22), (16, 2, 1), (32, 12), (36, -12, 1), (46, 6), (54, -16, 1), (60, 6), (72, -8, 1),
                         (72, 12), (88, 4, 1), (84, 22), (100, 26, 1), (88, 40), (100, 54, 1), (84, 62), (80, 48), (20, 48)])),
              L(outline([(58, 0), (72, -6), (74, 12), (86, 8), (84, 24), (96, 28), (88, 40), (96, 52), (84, 58), (78, 30)]), 'shade', 'b', False)]
             + brows(66, 'mid', 4.0, 15, 0.6, 13) + paint('front', 86)
             + [L(blob([(38, 94), (50, 90), (62, 94), (58, 100), (50, 102), (42, 100)], 6), (138, 74, 58, 255), 'f', ln=True), L([(40, 95), (60, 95)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(60, 50), (74, 46), (88, 38), (98, 28, 1), (86, 22), (94, 6, 1), (76, 10), (76, -10, 1), (60, 4), (52, -16, 1), (40, 4), (22, -8, 1),
                        (20, 12), (2, 10, 1), (8, 26), (-6, 36, 1), (6, 46), (-2, 60, 1), (12, 66), (20, 80), (34, 76), (40, 62), (50, 54)])),
             L(outline([(6, 44), (30, 46), (40, 60), (34, 76), (20, 80), (8, 64)]), 'shade', 'b', False)] + paint('side', 86) + brow_side(66, 'mid', 4.0, 1.0),
    'back': [L(outline([(16, 74), (2, 60, 1), (12, 48), (0, 30, 1), (16, 26), (14, 4, 1), (32, 12), (36, -12, 1), (46, 6), (54, -16, 1), (60, 6), (72, -8, 1),
                        (72, 12), (88, 4, 1), (84, 26), (100, 30, 1), (88, 48), (100, 60, 1), (84, 74), (66, 84), (50, 86), (34, 84)])),
             L(outline([(56, 0), (72, -6), (74, 12), (86, 8), (84, 28), (96, 32), (88, 48), (96, 60), (84, 72), (62, 80)]), 'shade', 'b', False)],
}

# Hershel Layton: el profesor de la chistera: sombrero de copa marrón con la cinta roja, el pelo castaño asomando por los
# lados, ojos de punto y una sonrisa tranquila (alto y delgado)
CHARS[K + 'hershel-layton'] = {
    'body': 'delgado', 'pal': pal('#6c3c2a', '#f2ba8c', shade='#562e20', deep='#3e2016', hat='#4c3428', hat_d='#3a2820', band='#a82020'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'eye_y': 74,
             'hairline': [(17, 70), (18, 52), (50, 48), (82, 52), (83, 70)]},
    'front': crop('front', top=14, side=70, w=1)
             + [L(outline([(18, 46), (20, -36, 1), (80, -36, 1), (82, 46)]), 'hat', 'f', ln=True),
                L(outline([(60, -36), (80, -36), (82, 44), (64, 44)]), 'hat_d', 'f', False),
                L(outline([(19.5, 20), (80.5, 20), (81.5, 32), (18.5, 32)]), 'band', 'f', ln=True),
                L(blob([(-10, 46), (50, 38), (110, 46), (108, 52), (50, 48), (-8, 52)], 6), 'hat', 'f', ln=True)],
    'side': crop('side', top=14, nape=82, w=1)
            + [L(outline([(16, 44), (18, -36, 1), (80, -36, 1), (82, 44)]), 'hat', 'f', ln=True),
               L(outline([(17, 20), (81, 20), (81.5, 32), (16.5, 32)]), 'band', 'f', ln=True),
               L(blob([(-14, 46), (40, 40), (110, 40), (110, 46), (40, 48), (-14, 52)], 6), 'hat', 'f', ln=True)],
    'back': crop('back', top=14, nape=82, w=1)
            + [L(outline([(18, 46), (20, -36, 1), (80, -36, 1), (82, 46)]), 'hat', 'f', ln=True),
               L(outline([(60, -36), (80, -36), (82, 44), (64, 44)]), 'hat_d', 'f', False),
               L(outline([(19.5, 20), (80.5, 20), (81.5, 32), (18.5, 32)]), 'band', 'f', ln=True),
               L(blob([(-10, 46), (50, 40), (110, 46), (108, 52), (50, 50), (-8, 52)], 6), 'hat', 'f', ln=True)],
}

# Hike Basher: casco de pelo malva rosado que le tapa las orejas, con el flequillo de dos cortinas color crema partido en
# medio; ojos entornados de dormido y una sonrisa ancha
CHARS[K + 'hike-basher'] = {
    'body': 'normal', 'pal': pal('#c48a8a', '#f4c28c', shade='#a4706e', deep='#845452', cream='#eadcb2', cream_d='#c8b88c'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'hairline': False, 'ears': False},
    'front': [L(outline([(10, 82), (6, 50), (14, 16), (50, 0), (86, 16), (94, 50), (90, 82), (80, 70), (78, 56), (22, 56), (20, 70)])),
              L(outline([(60, 2), (86, 16), (94, 50), (90, 78), (82, 60)]), 'shade', 'b', False),
              fr([(20, 66), (20, 40), (32, 26), (48, 30), (50, 40), (52, 30), (68, 26), (80, 40), (80, 66), (70, 52), (58, 48), (50, 58), (42, 48), (30, 52)], 'cream'),
              strand([(34, 32), (28, 50)], 'cream_d', 'f', 1.0), strand([(66, 32), (72, 50)], 'cream_d', 'f', 1.0)]
             + wide_smile(92, 36, 64, 5) + [L(quad((26, 70), (36, 66), (46, 70)), OUTC, 'f', False, False, 1.4), L(quad((54, 70), (64, 66), (74, 70)), OUTC, 'f', False, False, 1.4)],
    'side': [L(outline([(70, 58), (84, 52), (90, 30), (78, 6), (50, -2), (22, 4), (6, 24), (2, 50), (8, 76), (22, 86), (36, 84), (44, 72), (50, 60)])),
             L(outline([(4, 46), (30, 50), (44, 70), (36, 84), (22, 86), (8, 74)]), 'shade', 'b', False),
             fr([(74, 30), (90, 32), (92, 56), (84, 60), (80, 46)], 'cream')],
    'back': [L(outline([(10, 82), (6, 50), (14, 16), (50, 0), (86, 16), (94, 50), (90, 82), (66, 88), (50, 90), (34, 88)])),
             L(outline([(58, 2), (86, 16), (94, 50), (90, 82), (62, 86)]), 'shade', 'b', False)],
}

# Hiroshi Dot (sale con su sprite de píxeles): tupé verde azulado echado hacia arriba y atrás con los lados oscuros, piel
# muy clara, ojos afilados, cejas fruncidas y barba de tres días
CHARS[K + 'hiroshi-dot'] = {
    'body': 'normal', 'pal': pal('#3e8c92', '#f8dcb0', iris='#3a3a3a', shade='#2c6a70', deep='#1e4a50', stub='#d8c0a0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 92,
             'hairline': [(17, 62), (18, 48), (30, 46), (46, 44), (60, 46), (74, 44), (82, 48), (83, 62)]},
    'front': [L(outline([(17, 64), (13, 40), (14, 18), (22, 2), (30, -12), (46, -18), (64, -16), (76, -6), (84, 10), (87, 36), (83, 64), (78, 48), (22, 48)])),
              L(outline([(14, 30), (22, 26), (22, 48), (17, 62), (13, 40)]), 'deep', 'b', False), L(outline([(86, 30), (78, 26), (78, 48), (83, 62), (87, 40)]), 'deep', 'b', False),
              L(outline([(56, -14), (76, -6), (84, 10), (80, 26), (66, 14)]), 'shade', 'b', False),
              strand([(30, -6), (44, 20)], 'deep', 'b', 1.0), strand([(46, -14), (54, 20)], 'deep', 'b', 1.0),
              L(blob([(36, 96), (50, 99), (64, 96), (60, 103), (50, 106), (40, 103)], 6), 'stub', 'b', False)],
    'side': [L(outline([(66, 48), (80, 44), (90, 26), (90, 6), (80, -10), (60, -18), (36, -14), (14, -2), (4, 24), (6, 56), (18, 78), (32, 76), (38, 62), (46, 54), (58, 50)])),
             L(outline([(6, 34), (30, 40), (42, 58), (32, 76), (18, 78), (6, 58)]), 'deep', 'b', False),
             strand([(80, -6), (60, 8), (30, 14)], 'shade', 'b', 1.2)],
    'back': [L(outline([(17, 76), (13, 40), (14, 14), (26, -6), (50, -14), (74, -6), (86, 14), (87, 40), (83, 76), (66, 84), (50, 86), (34, 84)])),
             L(outline([(14, 40), (86, 40), (83, 76), (66, 84), (50, 86), (34, 84), (17, 76)]), 'deep', 'b', False)],
}

# Hollis Ticure: pelo verde corto con las puntas levantadas sobre las orejas; cara redonda con pecas, ojos entornados con
# las cejas fruncidas y la boca torcida hacia abajo
CHARS[K + 'hollis-ticure'] = {
    'body': 'corpulento', 'pal': pal('#6c9c3c', '#f2bc8a', shade='#54802c', deep='#3c5e1e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'face_front': WIDE,
             'hairline': [(15, 64), (18, 50), (30, 48), (42, 44), (56, 46), (70, 44), (82, 50), (85, 64)]},
    'front': crop('front', top=2, side=64, w=4)
             + [L(outline([(14, 62), (4, 70, 1), (12, 56)]), 'mid', 'b'), L(outline([(86, 62), (96, 70, 1), (88, 56)]), 'mid', 'b'),
                strand([(40, 8), (42, 30)], 'deep', 'b', 1.0), strand([(58, 8), (56, 30)], 'deep', 'b', 1.0)] + freckles(86, 24),
    'side': crop('side', top=0, nape=84, w=4) + [L(outline([(38, 66), (30, 80, 1), (32, 64)]), 'mid', 'b')],
    'back': crop('back', top=2, nape=84, w=4) + [L(outline([(10, 66), (2, 74, 1), (12, 58)]), 'mid', 'b'), L(outline([(90, 66), (98, 74, 1), (88, 58)]), 'mid', 'b')],
}


def braid(x, y0, y1, c='mid', tie=None, n=5, w=6.0):
    """Trenza colgando: una fila de óvalos de x, de y0 a y1, con su goma arriba (tie)."""
    out = []
    step = (y1 - y0) / n
    for i in range(n):
        out.append(L(ell(x + (1.2 if i % 2 else -1.2), y0 + step * (i + 0.5), w * (1 - 0.06 * i), step * 0.62), c, 'f', ln=True))
    if tie:
        out.append(L(ell(x, y0, w * 0.9, 2.6), tie, 'f', ln=True))
    return out


def stitches(x0, y0, x1, y1, n=4, c=OUTC):
    """Cicatriz cosida: una raya con puntos cruzados."""
    out = [L([(x0, y0), (x1, y1)], c, 'f', False, False, 1.0)]
    for i in range(n):
        t = (i + 0.5) / n
        x, y = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
        out.append(L([(x - 1, y - 2.5), (x + 1, y + 2.5)], c, 'f', False, False, 0.9))
    return out


# ---------------------------------------------------------------------------------------------------------------- hoja 1

# Holly Cricket: melena salmón ondulada hasta la barbilla con las puntas hacia fuera, un pelo de antena y la frente
# asomando entre dos cortinas de flequillo; ojos granate y sonrisa
CHARS[K + 'holly-cricket'] = {
    'body': 'normal', 'pal': pal('#d2706a', '#f8cc9e', iris='#a03828', shade='#b05652', deep='#8a3e3c'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 92, 'hairline': [(18, 60), (30, 46), (50, 42), (70, 46), (82, 60)]},
    'front': [L(outline([(12, 94, 1), (8, 76), (2, 64, 1), (10, 56), (8, 34), (20, 12), (42, 2), (48, -12, 1), (56, 2), (78, 8), (92, 28), (92, 54), (98, 64, 1),
                         (90, 72), (88, 94, 1), (80, 84), (80, 62), (20, 62), (20, 84)])),
              L(outline([(60, 4), (80, 10), (92, 30), (92, 54), (88, 84), (82, 62)]), 'shade', 'b', False),
              fr([(18, 74), (18, 44), (30, 32), (46, 34), (40, 42), (30, 54), (24, 76, 1)]), fr([(82, 74), (82, 44), (70, 32), (54, 34), (60, 42), (70, 54), (76, 76, 1)]),
              strand([(44, 6), (40, 20)], 'deep', 'b', 1.0), strand([(60, 8), (64, 22)], 'deep', 'b', 1.0)],
    'side': [L(outline([(70, 46), (84, 44), (92, 28), (80, 6), (56, -4), (52, -14, 1), (44, -2), (22, 4), (6, 24), (2, 52), (6, 78), (2, 94, 1), (14, 86), (24, 96, 1),
                        (30, 84), (40, 80), (42, 64), (50, 54), (62, 50)])),
             L(outline([(4, 44), (30, 46), (40, 64), (30, 84), (14, 86), (6, 70)]), 'shade', 'b', False),
             fr([(72, 30), (90, 32), (90, 58, 1), (80, 46)])],
    'back': [L(outline([(12, 94, 1), (8, 76), (2, 64, 1), (10, 56), (8, 34), (20, 12), (42, 2), (48, -12, 1), (56, 2), (78, 8), (92, 28), (92, 54), (98, 64, 1),
                        (90, 72), (88, 94, 1), (74, 88), (62, 96, 1), (50, 86), (38, 96, 1), (26, 88)])),
             L(outline([(56, 4), (80, 10), (92, 30), (92, 54), (88, 92), (62, 94)]), 'shade', 'b', False)],
}

# Homer Pidgeon: pelo verde esmeralda revuelto de pinchos con mechones en punta que le caen por la frente; ojos negros,
# cejas verdes fruncidas y media sonrisa
CHARS[K + 'homer-pidgeon'] = {
    'body': 'normal', 'pal': pal('#30a066', '#f4c28c', iris='#26222a', shade='#24804e', deep='#18603a'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': [(16, 62), (20, 48), (50, 44), (80, 48), (84, 62)]},
    'front': messy('front', amp=9, n=10, seed=5, lo=64)
             + fringe([(18, 64), (20, 50), (26, 64, 1), (34, 50), (40, 64, 1), (48, 50), (54, 66, 1), (62, 50), (68, 64, 1), (74, 52), (80, 62, 1), (82, 48)], 34)
             + brows(64, 'shade', 3.4, 14, 0.7, 11) + side_lines(86, 26),
    'side': messy('side', amp=9, n=10, seed=5) + [fr([(72, 30), (90, 36), (92, 60, 1), (84, 50), (80, 62, 1), (74, 46)])] + brow_side(64, 'shade', 3.4, 1.0),
    'back': messy('back', amp=9, n=10, seed=5),
}

# Homer Sockshell: piel tostada; pelo verde oliva con dos picos arriba como orejas, un mechón que le baja por el centro de la
# frente y las puntas abiertas sobre las orejas; ojazos, cejas verdes fruncidas y boca enfadada (bajito)
CHARS[K + 'homer-sockshell'] = {
    'body': 'bajito', 'pal': pal('#7c9c3c', '#c8925a', iris='#7a5656', shade='#62802c', deep='#46601e'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 93, 'hairline': [(15, 64), (20, 50), (50, 46), (80, 50), (85, 64)]},
    'front': [L(outline([(14, 66), (2, 58, 1), (12, 46), (10, 24), (6, 2, 1), (24, 8), (40, -2), (50, 4), (60, -2), (76, 8), (94, 2, 1), (90, 24), (88, 46), (98, 58, 1),
                         (86, 66), (80, 48), (20, 48)])),
              L(outline([(60, 0), (76, 10), (92, 6), (88, 28), (88, 50), (82, 60), (76, 30)]), 'shade', 'b', False),
              fr([(40, 40), (50, 32), (60, 40), (54, 50), (50, 60, 1), (46, 50)])] + brows(63, 'shade', 3.6, 14, 0.8, 11),
    'side': [L(outline([(66, 48), (82, 44), (90, 26), (88, 4, 1), (70, 6), (50, -2), (30, 2), (12, 12), (4, 30), (-6, 50, 1), (6, 58), (20, 78), (34, 76), (40, 62), (48, 54)])),
             L(outline([(5, 40), (30, 44), (40, 60), (34, 76), (20, 78), (6, 58)]), 'shade', 'b', False)] + brow_side(63, 'shade', 3.6, 1.0),
    'back': [L(outline([(14, 76), (2, 62, 1), (12, 50), (10, 24), (6, 2, 1), (24, 8), (50, 0), (76, 8), (94, 2, 1), (90, 24), (88, 50), (98, 62, 1), (86, 76),
                        (66, 84), (50, 86), (34, 84)])),
             L(outline([(58, 2), (76, 8), (92, 6), (88, 50), (86, 76), (62, 80)]), 'shade', 'b', False)],
}

# Horace Coop: melena larga castaño oliva con raya en medio y dos trenzas con gomas rojas por delante de los hombros; una
# cinta blanca con raya roja en la frente, ojos entornados, rayas en las mejillas y labios gruesos naranjas
CHARS[K + 'horace-coop'] = {
    'body': 'normal', 'pal': pal('#5c4c30', '#f2bc8a', shade='#463a24', deep='#30281a', band='#f2ece2', red='#c03a28', lip='#e47c3c'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'hairline': [(18, 62), (24, 50), (50, 46), (76, 50), (82, 62)]},
    'front': longhair('front', length=92, flare=2, part=True)
             + band('front', 40, 10, 'band', 'red') + braid(15, 84, 118, 'mid', 'red', 5, 5.5) + braid(85, 84, 118, 'mid', 'red', 5, 5.5)
             + [L(quad((26, 70), (36, 67), (46, 71)), OUTC, 'f', False, False, 2.0), L(quad((54, 71), (64, 67), (74, 70)), OUTC, 'f', False, False, 2.0),
                L(blob([(40, 93), (50, 90), (60, 93), (56, 99), (50, 100), (44, 99)], 6), 'lip', 'f', ln=True), L([(41, 94.5), (59, 94.5)], OUTC, 'f', False, False, 1.0)]
             + side_lines(84, 27),
    'side': longhair('side', length=94, flare=2) + band('side', 40, 10, 'band', 'red') + braid(42, 90, 120, 'mid', 'red', 5, 5.5)
            + [L(blob([(80, 92), (88, 91), (88, 97), (82, 98)], 5), 'lip', 'f', ln=True)],
    'back': longhair('back', length=96, flare=2, part=True) + band('back', 40, 10, 'band', 'red'),
}

# Horace Nelson (portero): hombretón de piel gris parda con un tupé rubio anaranjado que sube en punta hacia su izquierda y
# los lados casi rapados; cicatrices cosidas en la frente y la barbilla, mirada torva y orejas grandes
CHARS[K + 'horace-nelson'] = {
    'body': 'corpulento', 'pal': pal('#d8a652', '#a6866a', iris='#2e2a2a', shade='#b88a3e', deep='#8e6a2c'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'big_ears': 2, 'face_front': WIDE,
             'hairline': [(18, 58), (22, 46), (40, 42), (60, 40), (80, 44), (84, 58)]},
    'front': [L(outline([(18, 60), (16, 36), (22, 18), (38, 6), (56, -6), (74, -24, 1), (80, -4), (84, 20), (84, 40), (82, 60), (78, 44), (22, 44)])),
              L(outline([(62, -8), (74, -22), (80, -4), (84, 22), (82, 50), (76, 28)]), 'shade', 'b', False),
              strand([(30, 12), (52, -2), (70, -16)], 'deep', 'b', 1.0), strand([(36, 24), (60, 8), (76, -8)], 'deep', 'b', 1.0)]
             + stitches(28, 54, 46, 48, 4) + stitches(46, 103, 58, 101, 3),
    'side': [L(outline([(70, 46), (84, 40), (90, 20), (96, -14, 1), (74, -6), (50, -4), (26, 4), (10, 20), (4, 44), (8, 66), (20, 76), (34, 72), (40, 60), (50, 52), (60, 48)])),
             L(outline([(6, 44), (30, 46), (40, 60), (34, 72), (20, 76), (8, 64)]), 'shade', 'b', False),
             strand([(30, 10), (60, 0), (90, -10)], 'deep', 'b', 1.0)] + stitches(74, 52, 86, 48, 3),
    'back': [L(outline([(18, 72), (16, 36), (22, 16), (38, 4), (56, -6), (74, -20, 1), (80, -2), (84, 20), (84, 40), (82, 72), (66, 80), (50, 82), (34, 80)])),
             L(outline([(16, 44), (84, 44), (82, 72), (66, 80), (50, 82), (34, 80), (18, 72)]), 'shade', 'b', False)],
}

# Horty Courture: piel morena; pelo blanco verdoso peinado hacia atrás hasta la nuca, con un mechón gris por un lado; gafas
# de montura roja y cristales amarillos, sonrisa y un piercing en la barbilla
CHARS[K + 'horty-courture'] = {
    'body': 'normal', 'pal': pal('#d8efe6', '#b47c4c', shade='#b4ccc4', deep='#90a8a2', grey='#a2a2aa'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': [(18, 72), (22, 52), (50, 44), (78, 52), (82, 72)]},
    'front': [L(outline([(14, 92), (10, 60), (12, 30), (26, 8), (50, 0), (74, 8), (88, 30), (90, 60), (86, 92), (80, 82), (80, 50), (20, 50), (20, 82)])),
              L(outline([(60, 2), (82, 14), (90, 40), (88, 88), (82, 60)]), 'shade', 'b', False),
              strand([(34, 6), (30, 40)], 'deep', 'b', 1.0), strand([(50, 2), (50, 40)], 'deep', 'b', 1.0), strand([(66, 6), (70, 40)], 'deep', 'b', 1.0),
              fr([(20, 52), (26, 46), (30, 56), (28, 84, 1), (22, 74)], 'grey')]
             + glasses_band('front', 76) + [L(ell(50, 100, 1.4, 1.4), (60, 50, 50, 255), 'f', False)],
    'side': [L(outline([(66, 50), (82, 46), (90, 28), (80, 6), (50, -2), (24, 4), (8, 20), (2, 48), (4, 80), (10, 96, 1), (22, 88), (34, 82), (40, 66), (48, 56)])),
             L(outline([(4, 44), (30, 48), (40, 66), (30, 84), (10, 92)]), 'shade', 'b', False),
             strand([(80, 10), (50, 6), (20, 20)], 'deep', 'b', 1.0), strand([(84, 30), (50, 24), (14, 44)], 'deep', 'b', 1.0)] + glasses_band('side', 76),
    'back': [L(outline([(14, 92), (10, 60), (12, 30), (26, 8), (50, 0), (74, 8), (88, 30), (90, 60), (86, 92), (66, 98), (50, 100), (34, 98)])),
             L(outline([(58, 2), (82, 14), (90, 40), (86, 92), (60, 96)]), 'shade', 'b', False),
             strand([(36, 6), (36, 92)], 'deep', 'b', 1.0), strand([(50, 2), (50, 96)], 'deep', 'b', 1.0), strand([(64, 6), (64, 92)], 'deep', 'b', 1.0)]
            + glasses_band('back', 76),
}

# Hugh Dyer (portero): casco de pelo verde azulado con un pelo de antena; una venda caqui con tres rombos amarillos le tapa los
# ojos y se ata a un lado con dos tiras; sonrisa
CHARS[K + 'hugh-dyer'] = {
    'body': 'normal', 'pal': pal('#6aa8a0', '#f4c28c', shade='#528a84', deep='#3c6a66', band='#8a8a6c', gold='#e8c430'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    'front': [L(outline([(12, 68), (6, 40), (16, 12), (50, 0), (84, 12), (94, 40), (88, 68), (80, 58), (20, 58)])),
              L(outline([(60, 2), (84, 12), (94, 40), (88, 64), (82, 50)]), 'shade', 'b', False),
              strand([(30, 10), (24, 52)], 'deep', 'b', 1.0), strand([(42, 4), (40, 54)], 'deep', 'b', 1.0), strand([(58, 4), (60, 54)], 'deep', 'b', 1.0),
              strand([(70, 10), (76, 52)], 'deep', 'b', 1.0), L(quad((48, 2), (46, -12), (58, -10)), 'mid', 'b', False, False, 2.6)]
             + [L(outline([(10, 64), (50, 60), (90, 64), (90, 82), (50, 80), (10, 82)]), 'band', 'f', ln=True)]
             + [L(blob([(x - 6, 71), (x, 64), (x + 6, 71), (x, 78)], 3), 'gold', 'f', ln=True) for x in (30, 50, 70)]
             + [L(blob([(x - 3, 71), (x, 67.5), (x + 3, 71), (x, 74.5)], 3), 'band', 'f', False) for x in (30, 50, 70)]
             + [L(outline([(12, 70), (-2, 90, 1), (4, 92), (14, 76)]), 'band', 'f', ln=True), L(outline([(12, 74), (2, 100, 1), (8, 100), (16, 78)]), 'band', 'f', ln=True)],
    'side': [L(outline([(70, 56), (86, 52), (92, 30), (80, 6), (50, -2), (22, 4), (6, 24), (2, 50), (8, 72), (22, 80), (36, 78), (42, 66), (50, 58)])),
             L(outline([(4, 46), (30, 50), (42, 66), (36, 78), (22, 80), (8, 70)]), 'shade', 'b', False),
             L(quad((48, 0), (46, -12), (58, -10)), 'mid', 'b', False, False, 2.6),
             L(outline([(4, 62), (50, 62), (92, 64), (92, 80), (50, 78), (6, 78)]), 'band', 'f', ln=True),
             L(blob([(78, 71), (84, 65), (90, 71), (84, 77)], 3), 'gold', 'f', ln=True)],
    'back': [L(outline([(12, 76), (6, 40), (16, 12), (50, 0), (84, 12), (94, 40), (88, 76), (66, 84), (50, 86), (34, 84)])),
             L(outline([(58, 2), (84, 12), (94, 40), (88, 76), (62, 82)]), 'shade', 'b', False),
             L(quad((48, 2), (46, -12), (58, -10)), 'mid', 'b', False, False, 2.6)] + band('back', 62, 16, 'band', None, True),
}

# Hugh Marble: piel tostada; pelo morado corto con flequillo de puntas y dos puntas abiertas sobre las orejas; ojos en blanco
# mirando arriba, cejas fruncidas, boca torcida y una rayita en la mejilla
CHARS[K + 'hugh-marble'] = {
    'body': 'normal', 'pal': pal('#56498c', '#c48c56', iris='#2e2a34', shade='#42386e', deep='#2e2650'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': [(16, 62), (20, 50), (50, 46), (80, 50), (84, 62)]},
    'front': crop('front', top=2, side=62, w=2)
             + [L(outline([(16, 58), (0, 70, 1), (14, 66)]), 'mid', 'b'), L(outline([(84, 58), (100, 70, 1), (86, 66)]), 'mid', 'b'),
                ] + fringe([(18, 56), (24, 60, 1), (32, 48), (38, 60, 1), (46, 48), (52, 60, 1), (60, 48), (66, 60, 1), (74, 50), (80, 58, 1), (82, 46)], 30)
             + side_lines(84, 25),
    'side': crop('side', top=0, nape=84, w=2) + [L(outline([(38, 62), (28, 78, 1), (34, 60)]), 'mid', 'b'), fr([(74, 30), (90, 34), (90, 56, 1), (82, 44)])],
    'back': crop('back', top=2, nape=84, w=2) + [L(outline([(14, 62), (0, 74, 1), (14, 70)]), 'mid', 'b'), L(outline([(86, 62), (100, 74, 1), (86, 70)]), 'mid', 'b')],
}


def leaf(x, y, ang, s=1.0, c='leaf'):
    """Hoja (de un brote en la coronilla)."""
    import math
    ca, sa = math.cos(ang), math.sin(ang)
    pts = [(0, 0), (4, -6), (0, -16, 1), (-4, -6)]
    return L(outline([(x + (px * ca - py * sa) * s, y + (px * sa + py * ca) * s) + tuple(p[2:]) for p in pts for px, py in [p[:2]]]), c, 'f', ln=True)


# ---------------------------------------------------------------------------------------------------------------- hoja 2

# Hunter Glory: cabeza rapada morena con un brote de hojas verde oliva en la coronilla; una venda verde oscuro le tapa los
# ojos, con un ojo dibujado de espiral roja en medio, y se ata a un lado; sonrisa
CHARS[K + 'hunter-glory'] = {
    'body': 'normal', 'pal': pal('#7a8a36', '#c0884e', shade='#5e6c26', deep='#44501a', leaf='#7e8e36', band='#3a4c46', red='#d0605a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    'front': bald('front') + [leaf(50, 10, -1.0, 1.5), leaf(50, 10, 1.0, 1.5), leaf(50, 10, -0.4, 1.8), leaf(50, 10, 0.4, 1.8), leaf(50, 12, 0.0, 2.0)]
             + [L(outline([(9, 58), (50, 54), (91, 58), (91, 82), (50, 80), (9, 82)]), 'band', 'f', ln=True),
                L(blob([(38, 70), (50, 62), (62, 70), (50, 78)], 5), WHITE, 'f', ln=True), L(ell(50, 70, 4.6, 4.6), 'red', 'f', False), L(ell(50, 70, 2.0, 2.0), WHITE, 'f', False),
                L(outline([(11, 64), (-4, 86, 1), (3, 88), (13, 72)]), 'band', 'f', ln=True), L(outline([(11, 70), (0, 98, 1), (7, 98), (15, 76)]), 'band', 'f', ln=True)],
    'side': bald('side') + [leaf(46, 10, -0.7, 1.7), leaf(46, 10, 0.6, 1.7), leaf(48, 12, 0.0, 2.0)]
            + [L(outline([(4, 60), (50, 58), (92, 60), (92, 80), (50, 78), (6, 80)]), 'band', 'f', ln=True)],
    'back': bald('back') + [leaf(50, 10, -1.0, 1.5), leaf(50, 10, 1.0, 1.5), leaf(50, 12, 0.0, 2.0)] + band('back', 58, 20, 'band', None, True),
}

# Ifan Tassy: pelo verde azulado oscuro en pinchos arriba con patillas largas y rectas; cejas gruesas del mismo color, ojos
# entornados con pestañas, nariz naranja en triángulo y cara larga con papada
CHARS[K + 'ifan-tassy'] = {
    'body': 'normal', 'pal': pal('#3c6a6a', '#f2bc88', shade='#2c5252', deep='#1e3a3a', nose='#e2862c'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'hairline': [(17, 62), (20, 48), (50, 46), (80, 48), (83, 62)]},
    'front': messy('front', amp=10, n=10, seed=7, lo=56)
             + [L(outline([(15, 50), (23, 50), (22, 86), (16, 86)]), 'mid', 'b'), L(outline([(85, 50), (77, 50), (78, 86), (84, 86)]), 'mid', 'b')]
             + brows(62, 'mid', 5.0, 14, 0.0, 13)
             + [L(outline([(45, 80), (55, 80), (50, 92, 1)]), 'nose', 'f', ln=True), L(quad((36, 96), (50, 98), (64, 96)), OUTC, 'f', False, False, 1.4),
                L(quad((40, 104), (50, 107), (60, 104)), OUTC, 'f', False, False, 1.0)],
    'side': messy('side', amp=10, n=10, seed=7) + [L(outline([(52, 52), (60, 52), (60, 84), (54, 84)]), 'mid', 'b')] + brow_side(62, 'mid', 5.0)
            + [L(outline([(86, 80), (94, 86, 1), (86, 90)]), 'nose', 'f', ln=True)],
    'back': messy('back', amp=10, n=10, seed=7),
}

# Iggy Loyaller: melena verde oliva por los hombros con flequillo hasta las cejas y mechones largos a los lados de la
# cara; ojos oliva, cejas fruncidas y boca seria
CHARS[K + 'iggy-loyaller'] = {
    'body': 'normal', 'pal': pal('#6c6a2e', '#f4c28c', iris='#8c7c3e', shade='#545222', deep='#3c3a16'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': False},
    'front': longhair('front', length=104, flare=2, fringe=64)
             + [L(outline([(16, 64), (22, 64), (26, 104, 1), (18, 98)]), 'mid', 'f', ln=True), L(outline([(84, 64), (78, 64), (74, 104, 1), (82, 98)]), 'mid', 'f', ln=True)],
    'side': longhair('side', length=104, flare=2) + [fr([(74, 30), (92, 40), (92, 62, 1), (82, 52)])],
    'back': longhair('back', length=106, flare=2, ends=4),
}

# Ike Banner (portero): melena corta roja revuelta con las puntas abiertas hacia fuera a los lados y un flequillo de
# mechones; ojos oliva y sonrisa
CHARS[K + 'ike-banner'] = {
    'body': 'normal', 'pal': pal('#c2321e', '#f8cc9e', iris='#8c7c3e', shade='#9a2416', deep='#74180e'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    'front': [L(outline([(12, 82), (-6, 74, 1), (8, 66), (6, 40), (16, 14), (50, 0), (84, 14), (94, 40), (92, 66), (106, 74, 1), (88, 82), (82, 64), (18, 64)])),
              L(outline([(60, 2), (84, 14), (94, 40), (92, 64), (100, 72), (86, 76), (82, 50)]), 'shade', 'b', False)]
             + fringe([(18, 70), (22, 56), (28, 70, 1), (36, 54), (44, 66, 1), (50, 52), (56, 66, 1), (64, 54), (72, 70, 1), (78, 56), (82, 70)], 30)
             + [strand([(36, 10), (30, 34)], 'deep', 'b', 1.0), strand([(62, 10), (70, 34)], 'deep', 'b', 1.0)],
    'side': [L(outline([(70, 52), (86, 48), (92, 28), (80, 6), (50, -2), (22, 4), (6, 24), (2, 50), (6, 70), (-6, 84, 1), (12, 80), (22, 90, 1), (30, 80), (40, 66), (50, 56)])),
             L(outline([(4, 46), (30, 48), (40, 66), (30, 80), (12, 80), (6, 66)]), 'shade', 'b', False),
             fr([(72, 30), (92, 36), (92, 62, 1), (84, 52), (80, 64, 1), (76, 46)])],
    'back': [L(outline([(12, 82), (-6, 74, 1), (8, 66), (6, 40), (16, 14), (50, 0), (84, 14), (94, 40), (92, 66), (106, 74, 1), (88, 82), (74, 86), (66, 94, 1), (56, 86),
                        (44, 94, 1), (34, 86), (24, 90, 1)])),
             L(outline([(58, 2), (84, 14), (94, 40), (92, 66), (100, 74), (86, 82), (62, 86)]), 'shade', 'b', False)],
}

# Ike Flinger-Doerflinger: piel morena; pelo blanco plateado revuelto con un flequillo largo de puntas que le llega a los
# ojos; ojos verdes, cejas fruncidas y media sonrisa
CHARS[K + 'ike-flinger-doerflinger'] = {
    'body': 'normal', 'pal': pal('#e2ddce', '#b47a4a', iris='#3a9c6c', shade='#bcb6a6', deep='#948e7e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    'front': messy('front', amp=8, n=10, seed=11, lo=70)
             + fringe([(14, 76), (16, 60), (22, 74, 1), (30, 58), (36, 70, 1), (44, 56), (50, 68, 1), (56, 56), (64, 70, 1), (70, 58), (78, 74, 1), (84, 60), (86, 76)], 34)
             + [strand([(40, 10), (34, 40)], 'deep', 'b', 1.0), strand([(60, 10), (64, 40)], 'deep', 'b', 1.0)],
    'side': messy('side', amp=8, n=10, seed=11) + [fr([(70, 30), (92, 40), (94, 66, 1), (86, 56), (82, 70, 1), (76, 48)])],
    'back': messy('back', amp=8, n=10, seed=11),
}

# Innes Caving (portero): pelo rubio revuelto con las puntas levantadas en la nuca y bajo las orejas; mirada chulesca de
# ojos entornados, cejas rubias gruesas y fruncidas y media sonrisa
CHARS[K + 'innes-caving'] = {
    'body': 'normal', 'pal': pal('#e8c66e', '#f4c28c', iris='#3a2e2a', shade='#c8a450', deep='#a07e34'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': [(16, 62), (20, 50), (50, 44), (80, 50), (84, 62)]},
    'front': messy('front', amp=11, n=10, seed=13, lo=62)
             + [L(outline([(14, 70), (2, 86, 1), (16, 80)]), 'mid', 'b'), L(outline([(86, 70), (98, 86, 1), (84, 80)]), 'mid', 'b')]
             + fringe([(18, 60), (24, 52), (30, 62, 1), (38, 48), (46, 58, 1), (54, 46), (62, 58, 1), (70, 50), (78, 60, 1), (82, 52)], 32)
             + brows(64, 'shade', 4.5, 14, 0.8, 12),
    'side': messy('side', amp=11, n=10, seed=13) + [L(outline([(24, 84), (12, 100, 1), (30, 92)]), 'mid', 'b'), L(outline([(36, 82), (34, 98, 1), (42, 86)]), 'mid', 'b')]
            + brow_side(64, 'shade', 4.5, 1.0),
    'back': messy('back', amp=11, n=10, seed=13) + [L(outline([(24, 84), (14, 100, 1), (34, 90)]), 'mid', 'b'), L(outline([(76, 84), (86, 100, 1), (66, 90)]), 'mid', 'b')],
}

# Irv Washinton: cabezón enorme y redondo, calvo salvo una cresta naranja estrecha en lo alto; orejas grandes, cejas negras
# gruesas en ángulo, ojos de punto, nariz de botón con agujeros y la boca enfadada
CHARS[K + 'irv-washinton'] = {
    'body': 'corpulento', 'pal': pal('#e27a32', '#fadaa8', shade='#c05e20', deep='#9a4a18', nose='#f2c896'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'frown', 'mouth_y': 97, 'big_ears': 3, 'ear_out': 12, 'eye_y': 76, 'eye_sep': 16, 'hairline': False,
             'face_front': blob([(8, 50), (50, 14), (92, 50), (98, 76), (90, 100), (66, 112), (50, 114), (34, 112), (10, 100), (2, 76)]),
             'face_side': blob([(48, 10), (76, 16), (92, 40), (94, 66), (90, 90), (76, 106), (58, 108), (40, 98), (22, 82), (12, 56), (20, 26)]), 'nose': (50, 86, 4.5)},
    'front': [L(outline([(26, 32), (36, 14), (50, 8), (64, 14), (74, 32), (62, 26), (50, 24), (38, 26)]), 'mid', 'f', ln=True)]
             + [L([(28, 62), (42, 70)], OUTC, 'f', False, False, 4.0), L([(72, 62), (58, 70)], OUTC, 'f', False, False, 4.0),
                L(ell(48, 86, 0.8, 1.2), OUTC, 'f', False), L(ell(52, 86, 0.8, 1.2), OUTC, 'f', False)],
    'side': [L(outline([(70, 26), (58, 10), (42, 8), (26, 16), (20, 30), (32, 24), (46, 22), (60, 26)]), 'mid', 'f', ln=True),
             L([(80, 62), (90, 68)], OUTC, 'f', False, False, 4.0)],
    'back': [L(blob([(14, 62), (12, 34), (28, 12), (50, 4), (72, 12), (88, 34), (86, 62), (80, 88), (50, 100), (20, 88)], 6), 'skin', 'b'),
             L(outline([(26, 36), (36, 14), (50, 8), (64, 14), (74, 36), (62, 28), (50, 26), (38, 28)]), 'mid', 'f', ln=True)],
}

# Isaac Goss: pelo verde azulado oscuro con dos picos que se levantan a los lados como cuernos y entradas en el centro; cara
# larga de adulto, cejas gruesas, nariz grande y sonrisa
CHARS[K + 'isaac-goss'] = {
    'body': 'normal', 'pal': pal('#3c5c56', '#f2bc88', shade='#2c4642', deep='#1e322e'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'nose': (50, 84, 3.6),
             'hairline': [(16, 62), (20, 48), (36, 42), (50, 46), (64, 42), (80, 48), (84, 62)]},
    'front': [L(outline([(16, 64), (12, 40), (6, 8, 1), (22, 18), (36, 12), (50, 18), (64, 12), (78, 18), (94, 8, 1), (88, 40), (84, 64), (78, 46), (22, 46)])),
              L(outline([(60, 14), (78, 18), (92, 10), (88, 40), (84, 60), (78, 32)]), 'shade', 'b', False)]
             + brows(63, 'mid', 4.5, 14, 0.5, 13) + side_lines(86, 27),
    'side': [L(outline([(66, 48), (82, 44), (88, 24), (78, 12), (60, 14), (40, 10), (18, 14), (0, 0, 1), (6, 24), (4, 50), (16, 76), (32, 74), (38, 62), (48, 54)])),
             L(outline([(5, 40), (30, 44), (38, 62), (32, 74), (16, 76), (6, 56)]), 'shade', 'b', False)] + brow_side(63, 'mid', 4.5, 0.5),
    'back': [L(outline([(16, 76), (12, 40), (6, 8, 1), (22, 18), (50, 12), (78, 18), (94, 8, 1), (88, 40), (84, 76), (66, 84), (50, 86), (34, 84)])),
             L(outline([(58, 14), (78, 18), (92, 10), (88, 40), (84, 76), (62, 80)]), 'shade', 'b', False)],
}


def coils(x, y0, y1, w=7.0, c='mid', z='f', ln=True):
    """Rasta gruesa vertical con las vueltas marcadas."""
    out = [L(rope((x, y0), (x + 2, (y0 + y1) / 2), (x, y1), w), c, z, ln=ln)]
    n = max(2, int(abs(y1 - y0) / 6))
    for i in range(1, n):
        y = y0 + (y1 - y0) * i / n
        out.append(L([(x - w * 0.45, y - 1), (x + w * 0.45, y + 1)], 'deep', z, False, False, 1.0))
    return out


# ---------------------------------------------------------------------------------------------------------------- hoja 3

# Isaiah Shutt: rastas enrolladas naranja rojizo amontonadas en lo alto y una rasta larguísima que le cae por un lado hasta
# el pecho; cejas gruesas castañas, cara larga de adulto y sonrisa
CHARS[K + 'isaiah-shutt'] = {
    'body': 'delgado', 'pal': pal('#c85c1e', '#f4c28c', shade='#a24614', deep='#7a320c', brow='#8c4a28'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': [(18, 58), (22, 46), (50, 42), (78, 46), (82, 58)]},
    'front': [L(outline([(18, 60), (14, 36), (20, 10), (50, -2), (80, 10), (86, 36), (82, 60), (78, 44), (22, 44)]))]
             + [l for x in (24, 36, 50, 64, 76) for l in coils(x, 44 if x in (24, 76) else 40, -2 if x in (36, 50, 64) else 8, 9.0, 'mid', 'b', True)]
             + coils(16, 44, 116, 7.5) + brows(62, 'brow', 5.0, 14, 0.0, 13) + side_lines(86, 27),
    'side': [L(outline([(66, 46), (82, 42), (88, 24), (76, 2), (50, -4), (22, 2), (6, 20), (2, 44), (8, 64), (20, 74), (34, 70), (40, 58), (48, 50)]))]
            + [l for x, y in ((20, 6), (36, 0), (52, -2), (68, 2)) for l in coils(x, y + 44, y, 9.0, 'mid', 'b', True)]
            + coils(30, 60, 112, 7.5) + brow_side(62, 'brow', 5.0),
    'back': [L(outline([(16, 74), (12, 40), (20, 10), (50, -2), (80, 10), (88, 40), (84, 74), (66, 82), (50, 84), (34, 82)]))]
            + [l for x in (22, 34, 46, 58, 70, 80) for l in coils(x, 80 if 30 < x < 70 else 72, 4 if 30 < x < 70 else 14, 9.0, 'mid', 'b', True)]
            + coils(84, 50, 114, 7.5),
}

# Ivor Parrot: pelo gris verdoso echado entero hacia un lado en un mechón largo que le cae por la sien hasta la mejilla, con
# el otro lado rapado; ojos de rabia, cicatriz en la mejilla y la boca abierta enseñando los dientes
CHARS[K + 'ivor-parrot'] = {
    'body': 'normal', 'pal': pal('#5c867a', '#f4c28c', iris='#2a2626', shade='#466a60', deep='#304c44', buzz='#c8a682'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'hairline': False},
    'front': [L(blob([(30, 30), (60, 12), (80, 24), (84, 48), (60, 46)], 6), 'buzz', 'b', False),
              L(outline([(12, 86), (8, 50), (14, 20), (32, 2), (56, -4), (72, 2), (70, 12), (56, 20), (42, 34), (30, 52), (24, 88, 1)])),
              L(outline([(40, 0), (68, 2), (64, 14), (48, 24), (34, 40), (26, 30)]), 'shade', 'b', False),
              fr([(16, 46), (30, 30), (42, 26), (34, 42), (28, 58), (24, 88, 1), (18, 74)]),
              strand([(56, 4), (34, 24), (20, 56)], 'deep', 'b', 1.0),
              L(outline([(70, 44), (66, 54, 1), (62, 46)]), 'mid', 'b', False),
              L(blob([(38, 91), (50, 89), (62, 91), (61, 100), (50, 103), (39, 100)], 6), (110, 52, 44, 255), 'f', ln=True),
              L(blob([(41, 92), (59, 92), (58, 95), (42, 95)], 4), WHITE, 'f', False), L(blob([(42, 99), (58, 99), (56, 101.5), (44, 101.5)], 4), WHITE, 'f', False)]
             + stitches(66, 80, 74, 90, 3),
    'side': [L(outline([(60, 40), (76, 30), (82, 16), (68, 2), (44, -4), (22, 0), (6, 16), (0, 40), (4, 72), (16, 88, 1), (22, 74), (26, 56), (40, 44)])),
             L(outline([(2, 40), (24, 40), (26, 56), (16, 86), (4, 70)]), 'shade', 'b', False),
             strand([(70, 6), (40, 8), (12, 30)], 'deep', 'b', 1.0)],
    'back': [L(blob([(18, 60), (20, 32), (50, 20), (80, 32), (82, 60), (78, 84), (50, 96), (22, 84)], 6), 'buzz', 'b', False),
             L(outline([(10, 84), (6, 50), (14, 20), (32, 2), (56, -4), (76, 4), (88, 22), (80, 30), (60, 34), (36, 50), (24, 88, 1)])),
             L(outline([(6, 50), (34, 50), (24, 86)]), 'shade', 'b', False)],
}

# Jack Frosty: pelo blanco verdoso abombado con dos puntas largas que salen hacia los lados y un pincho fino hacia arriba;
# una tirita en la mejilla, ojos de pillo y cejas fruncidas
CHARS[K + 'jack-frosty'] = {
    'body': 'normal', 'pal': pal('#d6efe6', '#f4c28c', iris='#2a2626', shade='#b0ccc4', deep='#8eaaa2', tape='#ecc8a0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': [(16, 62), (20, 52), (34, 48), (50, 50), (66, 48), (80, 52), (84, 62)]},
    'front': [L(outline([(16, 64), (-8, 50, 1), (10, 42), (12, 26), (26, 10), (44, 4), (48, -22, 1), (56, 4), (74, 10), (88, 26), (90, 42), (108, 50, 1), (84, 64), (80, 50), (20, 50)])),
              L(outline([(60, 6), (74, 10), (88, 26), (90, 42), (104, 50), (84, 60), (78, 32)]), 'shade', 'b', False),
              strand([(36, 14), (30, 40)], 'deep', 'b', 1.0), strand([(62, 14), (68, 40)], 'deep', 'b', 1.0),
              L(blob([(22, 82), (30, 78), (34, 86), (26, 90)], 3), 'tape', 'f', ln=True)],
    'side': [L(outline([(66, 50), (82, 46), (90, 30), (78, 8), (54, 2), (52, -22, 1), (44, 0), (22, 6), (8, 22), (-12, 44, 1), (8, 50), (8, 64), (20, 78), (34, 76), (40, 62),
                        (48, 54)])),
             L(outline([(8, 40), (30, 44), (40, 60), (34, 76), (20, 78), (8, 62)]), 'shade', 'b', False),
             L(blob([(70, 82), (78, 78), (82, 86), (74, 90)], 3), 'tape', 'f', ln=True)],
    'back': [L(outline([(16, 76), (-8, 54, 1), (10, 46), (12, 26), (26, 10), (44, 4), (48, -22, 1), (56, 4), (74, 10), (88, 26), (90, 46), (108, 54, 1), (84, 76), (66, 84),
                        (50, 86), (34, 84)])),
             L(outline([(58, 6), (74, 10), (88, 26), (90, 46), (104, 54), (84, 74), (62, 80)]), 'shade', 'b', False)],
}

# Jack Lumbar (portero): piel parda grisácea, calvo con una franja de pelo naranja corto en lo alto de la cabeza, orejas
# grandes, ojos verdes de mirada fija, un lunar y una sonrisa leve (adulto)
CHARS[K + 'jack-lumbar'] = {
    'body': 'normal', 'pal': pal('#c85c2c', '#a4826a', iris='#3a8a6c', shade='#a4461e', deep='#7a3214'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 94, 'big_ears': 3, 'ear_out': 3, 'nose': (50, 84, 3.4), 'hairline': False},
    'front': bald('front') + [L(outline([(18, 44), (24, 18), (50, 6), (76, 18), (82, 44), (72, 26), (50, 18), (28, 26)]), 'mid', 'f', ln=True)]
             + [L(ell(70, 86, 1.0, 1.0), (60, 40, 30, 255), 'f', False)],
    'side': bald('side') + [L(outline([(80, 30), (70, 12), (50, 6), (30, 10), (16, 24), (24, 26), (40, 16), (60, 16), (72, 26)]), 'mid', 'f', ln=True)],
    'back': bald('back') + [L(outline([(20, 40), (26, 18), (50, 8), (74, 18), (80, 40), (70, 28), (50, 20), (30, 28)]), 'mid', 'f', ln=True)],
}

# Jack Mate: pelo rubio pálido en pinchos largos echados hacia su izquierda, con un pelo suelto hacia el otro lado; ojos
# entornados con pestañas y media sonrisa
CHARS[K + 'jack-mate'] = {
    'body': 'normal', 'pal': pal('#eedca2', '#f4c28c', iris='#2a2626', shade='#cebc80', deep='#a89660'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    'front': [L(outline([(16, 66), (10, 48), (0, 40, 1), (12, 34), (6, 14, 1), (22, 14), (28, -4, 1), (42, 8), (56, 0), (64, 6), (86, -2, 1), (80, 14), (106, 22, 1),
                         (88, 32), (108, 46, 1), (88, 48), (98, 64, 1), (84, 64), (80, 50), (20, 50)])),
              L(outline([(62, 6), (84, 0), (80, 16), (102, 24), (88, 34), (104, 46), (86, 50), (78, 30)]), 'shade', 'b', False)]
             + fringe([(16, 62), (22, 52), (28, 64, 1), (38, 50), (48, 68, 1), (54, 50), (66, 66, 1), (72, 52), (84, 60, 1), (84, 48)], 30)
             + [L([(26, 70), (24, 66)], OUTC, 'f', False, False, 1.0), L([(74, 70), (76, 66)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(66, 50), (82, 46), (96, 40, 1), (88, 30), (104, 18, 1), (84, 14), (90, -2, 1), (68, 4), (56, -6, 1), (40, 2), (14, 0, 1), (16, 14), (0, 22, 1), (8, 34),
                        (-4, 48, 1), (8, 56), (20, 76), (34, 74), (40, 60), (48, 54)])),
             L(outline([(6, 44), (30, 46), (40, 60), (34, 74), (20, 76), (8, 60)]), 'shade', 'b', False),
             fr([(72, 32), (94, 40), (90, 62, 1), (82, 50)])],
    'back': [L(outline([(16, 74), (8, 52), (-2, 44, 1), (10, 36), (6, 14, 1), (22, 14), (28, -4, 1), (42, 8), (56, 0), (64, 6), (86, -2, 1), (80, 14), (104, 24, 1), (88, 34),
                        (104, 50, 1), (86, 54), (84, 76), (66, 84), (50, 86), (34, 84)])),
             L(outline([(60, 6), (84, 0), (80, 16), (100, 26), (88, 36), (100, 50), (84, 74), (62, 80)]), 'shade', 'b', False)],
}

# Jack Nimble: piel tostada; melena azul marino muy oscuro cortada recta a la altura de la barbilla, con flequillo recto;
# ojos pequeños y redondos, nariz naranja y boca seria
CHARS[K + 'jack-nimble'] = {
    'body': 'normal', 'pal': pal('#2c3c5c', '#c48c56', shade='#202c46', deep='#161e32', nose='#e88a3a'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'line', 'mouth_y': 94, 'hairline': False, 'nose': (50, 86, 2.8)},
    'front': [L(outline([(10, 98, 1), (8, 60), (12, 24), (28, 6), (50, 0), (72, 6), (88, 24), (92, 60), (90, 98, 1), (80, 98), (80, 62), (20, 62), (20, 98)])),
              L(outline([(60, 2), (86, 20), (92, 60), (90, 96), (82, 96), (82, 50)]), 'shade', 'b', False)]
             + fringe([(18, 60), (30, 62), (32, 54), (44, 58), (46, 52), (58, 58), (60, 52), (70, 60), (72, 54), (82, 58)], 30),
    'side': [L(outline([(70, 56), (86, 52), (92, 30), (80, 6), (50, -2), (22, 4), (6, 24), (2, 60), (4, 98, 1), (40, 98, 1), (42, 80), (44, 64), (54, 58)])),
             L(outline([(4, 50), (30, 52), (40, 70), (40, 96), (6, 96)]), 'shade', 'b', False),
             fr([(74, 30), (92, 36), (92, 58), (84, 58)])],
    'back': [L(outline([(10, 98, 1), (8, 60), (12, 24), (28, 6), (50, 0), (72, 6), (88, 24), (92, 60), (90, 98, 1), (50, 100)])),
             L(outline([(58, 2), (86, 20), (92, 60), (90, 96), (62, 98)]), 'shade', 'b', False)],
}

# Jack Pott (portero): grandullón de cara redonda; pelo gris verdoso con flequillo recto y dos moños a los lados de la
# cabeza; ojos de rabia, cejas fruncidas, un pendiente amarillo y una sonrisa de satisfacción
CHARS[K + 'jack-pott'] = {
    'body': 'corpulento', 'pal': pal('#5e7c76', '#f2bc88', iris='#2a2626', shade='#4a625c', deep='#344642', gold='#e8c430'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'face_front': WIDE, 'hairline': False},
    'front': [L(ell(10, 60, 11, 11), 'mid', 'b'), L(ell(90, 60, 11, 11), 'mid', 'b'),
              L(outline([(14, 66), (10, 40), (18, 14), (50, 2), (82, 14), (90, 40), (86, 66), (80, 56), (20, 56)])),
              L(outline([(60, 4), (82, 14), (90, 40), (86, 62), (80, 40)]), 'shade', 'b', False)]
             + fringe([(14, 58), (24, 62), (26, 54), (38, 60), (40, 52), (50, 58), (52, 52), (62, 60), (64, 54), (76, 62), (78, 54), (86, 58)], 30)
             + [L(ell(14, 82, 1.6, 1.6), 'gold', 'f', False), L(ell(86, 82, 1.6, 1.6), 'gold', 'f', False)],
    'side': [L(outline([(70, 54), (86, 50), (92, 30), (80, 6), (50, -2), (22, 4), (6, 24), (2, 50), (8, 72), (22, 80), (36, 78), (42, 64), (50, 56)])),
             L(outline([(4, 44), (30, 48), (42, 64), (36, 78), (22, 80), (8, 70)]), 'shade', 'b', False),
             L(ell(40, 46, 11, 11), 'mid', 'f', ln=True), L(blob([(36, 40), (44, 42), (42, 50)], 4), 'shade', 'f', False), fr([(76, 30), (92, 36), (92, 56), (84, 56)])],
    'back': [L(outline([(14, 76), (10, 40), (18, 14), (50, 2), (82, 14), (90, 40), (86, 76), (66, 84), (50, 86), (34, 84)])),
             L(outline([(58, 4), (82, 14), (90, 40), (86, 76), (62, 80)]), 'shade', 'b', False),
             L(ell(10, 58, 11, 11), 'mid', 'f', ln=True), L(ell(90, 58, 11, 11), 'mid', 'f', ln=True)],
}

# Jack Trades-Tradesman: pelo azul marino oscuro corto y peinado, con un moño pequeño en lo alto; pecas, cara alargada con la
# barbilla marcada y una sonrisa pícara (adulto)
CHARS[K + 'jack-trades-tradesman'] = {
    'body': 'normal', 'pal': pal('#2c3a6c', '#f4c28c', iris='#2a2626', shade='#202c54', deep='#161e3c'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 94, 'nose': (50, 84, 3.0),
             'hairline': [(16, 62), (18, 48), (32, 44), (50, 42), (68, 44), (82, 48), (84, 62)]},
    'front': crop('front', top=8, side=62, w=1)
             + [L(ell(50, -2, 9, 8), 'mid', 'b'), L(blob([(44, 4), (56, 4), (54, 8), (46, 8)], 3), 'deep', 'b', False), L(quad((54, -8), (60, -14), (64, -10)), 'mid', 'b', False, False, 2.4),
                strand([(34, 14), (40, 30)], 'deep', 'b', 1.0), strand([(66, 14), (60, 30)], 'deep', 'b', 1.0)]
             + freckles(84, 22) + [L(quad((44, 104), (50, 106), (56, 104)), OUTC, 'f', False, False, 1.0)],
    'side': crop('side', top=6, nape=82, w=1) + [L(ell(46, -2, 9, 8), 'mid', 'b'), L(quad((40, -6), (34, -14), (30, -10)), 'mid', 'b', False, False, 2.4)],
    'back': crop('back', top=8, nape=82, w=1) + [L(ell(50, -2, 9, 8), 'mid', 'b'), L(blob([(44, 4), (56, 4), (54, 8), (46, 8)], 3), 'deep', 'b', False)],
}


# ---------------------------------------------------------------------------------------------------------------- hoja 4

# Jack Trumper: pelo castaño oliva peinado de lado, con el flequillo cruzando la frente en diagonal y una punta levantada
# sobre la oreja; ojos grises claros grandes, cejas fruncidas y sonrisa de pillo
CHARS[K + 'jack-trumper'] = {
    'body': 'normal', 'pal': pal('#5c5428', '#f8cc9e', iris='#b4b8ac', shade='#46401c', deep='#302c12'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': [(16, 62), (20, 50), (50, 44), (80, 50), (84, 62)]},
    'front': crop('front', top=0, side=62, w=3)
             + [L(outline([(84, 40), (102, 40, 1), (88, 54)]), 'mid', 'b')]
             + fringe([(14, 62), (20, 54), (32, 48), (46, 42), (62, 38), (76, 38), (90, 42, 1)], 26)
             + [strand([(70, 8), (50, 22), (30, 44)], 'deep', 'b', 1.0)],
    'side': crop('side', top=-2, nape=84, w=3) + [fr([(70, 28), (92, 36), (94, 56, 1), (82, 46)])],
    'back': crop('back', top=0, nape=84, w=3) + [L(outline([(86, 40), (102, 42, 1), (88, 54)]), 'mid', 'b')],
}

# Jacky Lantern (portero): grandullón de cara redonda y morena; mata de pelo gris pardo revuelta y abultada con puntas hacia
# los lados; cejas negras rectas y gruesas, ojos negros redondos, nariz de cerdito y sonrisa
CHARS[K + 'jacky-lantern'] = {
    'body': 'corpulento', 'pal': pal('#9c9680', '#dc9a5e', shade='#7c7664', deep='#5c584a', nose='#e8aa72'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'face_front': WIDE, 'nose': (50, 86, 4.4), 'hairline': False},
    'front': messy('front', amp=12, n=10, seed=17, rx=52, lo=64)
             + fringe([(10, 62), (18, 50), (24, 60, 1), (34, 46), (42, 56, 1), (52, 44), (60, 56, 1), (70, 46), (78, 60, 1), (86, 50), (92, 62)], 30)
             + [L([(28, 66), (42, 64)], OUTC, 'f', False, False, 3.6), L([(58, 64), (72, 66)], OUTC, 'f', False, False, 3.6),
                L(ell(48, 86, 0.8, 1.2), OUTC, 'f', False), L(ell(52, 86, 0.8, 1.2), OUTC, 'f', False)],
    'side': messy('side', amp=12, n=10, seed=17, rx=50) + [fr([(70, 30), (94, 40), (96, 64, 1), (86, 54)]), L([(74, 64), (86, 63)], OUTC, 'f', False, False, 3.6)],
    'back': messy('back', amp=12, n=10, seed=17, rx=52),
}

# Jacob Grimley: melena castaña por los hombros con un mechón rosa por delante que le tapa un ojo; un monóculo de aro verde
# azulado en el otro y una sonrisita
CHARS[K + 'jacob-grimley'] = {
    'body': 'delgado', 'pal': pal('#6c4a2c', '#f4c28c', iris='#3a2e2a', shade='#563a22', deep='#3e2a16', pink='#d4707a', pink_d='#b05862', rim='#5a8c8c'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 93, 'nose': (50, 84, 3.2), 'hairline': [(18, 62), (24, 46), (50, 40), (76, 46), (82, 62)]},
    'front': longhair('front', length=98, flare=3)
             + [fr([(46, 4), (64, 2), (80, 14), (86, 38), (82, 70), (76, 92, 1), (70, 66), (62, 46), (50, 30)], 'pink'), strand([(58, 8), (70, 40), (76, 80)], 'pink_d', 'f', 1.0)]
             + [L(ell(36, 76, 9, 9) + [ell(36, 76, 9, 9)[0]], 'rim', 'f', False, False, 2.2), L(quad((27, 78), (22, 90), (24, 104)), 'rim', 'f', False, False, 0.9)],
    'side': longhair('side', length=98, flare=3) + [fr([(64, 2), (86, 16), (94, 40), (92, 72, 1), (84, 54), (78, 30)], 'pink')],
    'back': longhair('back', length=100, flare=3, ends=4) + [L(outline([(70, 6), (86, 18), (94, 44), (86, 40), (74, 22)]), 'pink', 'b', False)],
}

# Jak Hammer-Hammerslam: grandullón calvo con una cresta naranja rojiza pequeña y en punta; pintura roja en rayos alrededor de
# los ojos apretados, cejas fruncidas y boca seria
CHARS[K + 'jak-hammer-hammerslam'] = {
    'body': 'corpulento', 'pal': pal('#d0522a', '#f4c08c', shade='#a83c1c', deep='#7c2a12', red='#c8361e'),
    'face': {'eyes': 'closed', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'face_front': WIDE, 'nose': (50, 84, 3.4), 'hairline': False},
    'front': bald('front') + [L(outline([(42, 14), (44, 0), (50, -16, 1), (56, 0), (58, 14), (54, 22), (46, 22)]), 'mid', 'f', ln=True),
                              L(outline([(52, -6), (56, 0), (58, 14), (54, 20)]), 'shade', 'f', False)]
             + [L(outline([(18, 66), (40, 70), (24, 74, 1)]), 'red', 'f', False), L(outline([(82, 66), (60, 70), (76, 74, 1)]), 'red', 'f', False),
                L(outline([(22, 60), (40, 66), (30, 64, 1)]), 'red', 'f', False), L(outline([(78, 60), (60, 66), (70, 64, 1)]), 'red', 'f', False)],
    'side': bald('side') + [L(outline([(68, 22), (66, 6), (56, -14, 1), (40, -6), (20, 4), (16, 12), (40, 6), (58, 6)]), 'mid', 'f', ln=True),
                            L(outline([(64, 64), (84, 70), (70, 74, 1)]), 'red', 'f', False)],
    'back': bald('back') + [L(outline([(44, 40), (44, 0), (50, -14, 1), (56, 0), (56, 40), (50, 44)]), 'mid', 'f', ln=True)],
}

# Jay Archer: pelo azul marino que le enmarca la cara con dos patillas enormes en punta hacia fuera (como garras) a la
# altura de las mejillas; cara ancha, ojos entornados, nariz grande y sonrisa ancha
CHARS[K + 'jay-archer'] = {
    'body': 'corpulento', 'pal': pal('#2c5c8c', '#c8925c', iris='#2a2626', shade='#20466e', deep='#163250', nose='#b47c4a'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'none', 'face_front': WIDE, 'nose': (50, 84, 4.6), 'ears': False,
             'hairline': [(14, 78), (20, 58), (36, 52), (50, 58), (64, 52), (80, 58), (86, 78)]},
    'front': [L(outline([(12, 92), (-6, 96, 1), (6, 80), (4, 62), (-8, 52, 1), (8, 46), (10, 22), (22, 6), (50, 0), (78, 6), (90, 22), (92, 46), (108, 52, 1), (96, 62),
                         (94, 80), (106, 96, 1), (88, 92), (84, 76), (84, 58), (16, 58), (16, 76)])),
              L(outline([(60, 2), (86, 16), (92, 44), (104, 52), (94, 62), (92, 80), (100, 94), (86, 90), (84, 60)]), 'shade', 'b', False)]
             + wide_smile(96, 34, 66, 6),
    'side': [L(outline([(70, 56), (86, 52), (92, 30), (80, 6), (50, -2), (22, 4), (6, 24), (2, 50), (8, 72), (20, 82), (34, 96, 1), (44, 84), (66, 98, 1), (60, 80), (56, 64)])),
             L(outline([(4, 44), (30, 48), (44, 70), (36, 82), (20, 80), (8, 68)]), 'shade', 'b', False),
             fr([(74, 30), (92, 38), (94, 60, 1), (84, 52)])],
    'back': [L(outline([(12, 92), (-6, 96, 1), (6, 80), (4, 62), (-8, 52, 1), (8, 46), (10, 22), (22, 6), (50, 0), (78, 6), (90, 22), (92, 46), (108, 52, 1), (96, 62),
                        (94, 80), (106, 96, 1), (88, 92), (66, 90), (50, 92), (34, 90)])),
             L(outline([(58, 2), (86, 16), (92, 44), (104, 52), (94, 62), (92, 80), (100, 94), (64, 90)]), 'shade', 'b', False)],
}

# Jay Pan (portero): grandullón de cara redonda; pelo verde oliva peinado hacia atrás con un moño en lo alto, como un
# luchador de sumo; pintura roja en franjas bajo los ojos, cejas fruncidas y boca apretada
CHARS[K + 'jay-pan'] = {
    'body': 'corpulento', 'pal': pal('#5c5a2a', '#f4c48e', iris='#2a2626', shade='#46441e', deep='#302e12', red='#c03220'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 96, 'face_front': WIDE, 'nose': (50, 84, 3.4),
             'hairline': [(14, 62), (18, 46), (32, 40), (50, 38), (68, 40), (82, 46), (86, 62)]},
    'front': crop('front', top=6, side=62, w=3)
             + [L(ell(50, -4, 9, 10), 'mid', 'b'), L(blob([(42, 4), (58, 4), (56, 8), (44, 8)], 3), 'deep', 'b', False),
                strand([(30, 14), (34, 34)], 'deep', 'b', 1.0), strand([(50, 8), (50, 34)], 'deep', 'b', 1.0), strand([(70, 14), (66, 34)], 'deep', 'b', 1.0)]
             + paint('front', 80, 'red', 'bar') + [L(quad((40, 104), (50, 107), (60, 104)), OUTC, 'f', False, False, 1.0)],
    'side': crop('side', top=4, nape=84, w=3) + [L(ell(44, -4, 9, 10), 'mid', 'b')] + paint('side', 80, 'red', 'bar'),
    'back': crop('back', top=6, nape=84, w=3) + [L(ell(50, -4, 9, 10), 'mid', 'b'), L(blob([(42, 4), (58, 4), (56, 8), (44, 8)], 3), 'deep', 'b', False)],
}

# Jebb Ettow: piel morena; pelo naranja en cresta puntiaguda que cubre la cabeza como un tejado, peinado en rayas hacia la
# punta; gafas de visera amarillo pálido con los cristales oscuros y sonrisa
CHARS[K + 'jebb-ettow'] = {
    'body': 'normal', 'pal': pal('#cc5c22', '#aa7244', shade='#a44616', deep='#7a320c', frame='#ece4a6', lens='#5c5c5c'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'hairline': [(17, 62), (20, 50), (50, 48), (80, 50), (83, 62)]},
    'front': [L(outline([(17, 64), (14, 38), (24, 14), (42, 0), (50, -14, 1), (58, 0), (76, 14), (86, 38), (83, 64), (78, 48), (22, 48)])),
              L(outline([(52, -10), (76, 14), (86, 38), (82, 60), (68, 24)]), 'shade', 'b', False)]
             + [strand([(50, -10), (x, 44)], 'deep', 'b', 1.0) for x in (24, 34, 44, 56, 66, 76)]
             + glasses_band('front', 76, 'frame', 'lens'),
    'side': [L(outline([(66, 50), (82, 46), (90, 30), (80, 10), (58, -4), (40, -14, 1), (36, -2), (16, 10), (4, 30), (6, 58), (20, 76), (34, 74), (40, 60), (48, 52)])),
             L(outline([(5, 40), (30, 44), (40, 60), (34, 74), (20, 76), (6, 58)]), 'shade', 'b', False)]
            + [strand([(40, -10), (x, y)], 'deep', 'b', 1.0) for x, y in ((80, 40), (66, 44), (20, 50), (10, 36))] + glasses_band('side', 76, 'frame', 'lens'),
    'back': [L(outline([(17, 76), (14, 38), (24, 14), (42, 0), (50, -14, 1), (58, 0), (76, 14), (86, 38), (83, 76), (66, 84), (50, 86), (34, 84)])),
             L(outline([(52, -10), (76, 14), (86, 38), (83, 76), (62, 80)]), 'shade', 'b', False)]
            + [strand([(50, -10), (x, 80)], 'deep', 'b', 1.0) for x in (30, 42, 58, 70)] + glasses_band('back', 76, 'frame', 'lens'),
}

# Jeeves Dropper: pelo rosa corto con las puntas abiertas a los lados y flequillo de puntas; piel muy clara, ojillos
# rasgados casi cerrados, cejas rosas fruncidas y boca enfurruñada (bajito)
CHARS[K + 'jeeves-dropper'] = {
    'body': 'bajito', 'pal': pal('#cc6c7c', '#fadcc2', iris='#2a2626', shade='#aa5464', deep='#843e4c'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'frown', 'mouth_y': 94, 'hairline': [(16, 62), (20, 50), (50, 46), (80, 50), (84, 62)]},
    'front': crop('front', top=2, side=62, w=2)
             + [L(outline([(16, 56), (2, 66, 1), (14, 64)]), 'mid', 'b'), L(outline([(84, 56), (98, 66, 1), (86, 64)]), 'mid', 'b')]
             + fringe([(18, 56), (24, 60, 1), (30, 50), (38, 58, 1), (46, 48), (54, 56, 1), (62, 48), (70, 58, 1), (76, 50), (82, 58, 1)], 30)
             + [L(outline([(28, 64), (40, 62), (36, 66, 1)]), 'shade', 'f', False), L(outline([(72, 64), (60, 62), (64, 66, 1)]), 'shade', 'f', False)],
    'side': crop('side', top=0, nape=84, w=2) + [L(outline([(38, 62), (30, 76, 1), (34, 60)]), 'mid', 'b'), fr([(74, 30), (90, 34), (90, 54, 1), (82, 46)])],
    'back': crop('back', top=2, nape=84, w=2) + [L(outline([(14, 60), (0, 72, 1), (14, 70)]), 'mid', 'b'), L(outline([(86, 60), (100, 72, 1), (86, 70)]), 'mid', 'b')],
}


from chars_ares_barcelona_orb import curls  # noqa: E402


def afro(view, cx=50, cy=34, rx=56, ry=46, n=10, nape=86):
    """Afro redondo de bultos (de frente, perfil o espalda)."""
    if view == 'side':
        return [L(curls(40, cy, (rx * 0.96, ry), n, 0.3)), L(blob([(4, cy + 6), (30, cy + 14), (40, nape - 10), (16, nape - 6)], 6), 'shade', 'b', False)]
    return [L(curls(cx, cy, (rx, ry), n, 0.2 if view == 'front' else 0.5)),
            L(blob([(cx + 10, cy - ry * 0.8), (cx + rx * 0.9, cy - 6), (cx + rx * 0.8, cy + ry * 0.7), (cx + 20, cy + 10)], 6), 'shade', 'b', False)]


# ---------------------------------------------------------------------------------------------------------------- hoja 5

# Jem Paste (portero): afro grande castaño grisáceo de bultos redondos con una cinta verde de puntas naranjas en la frente;
# cejas negras gruesas, ojos de mirada segura y sonrisa
CHARS[K + 'jem-paste'] = {
    'body': 'normal', 'pal': pal('#7c705a', '#c8925a', iris='#2a2626', shade='#625846', deep='#4a4234', band='#5c8c3a', orange='#e27c2c'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'hairline': [(14, 74), (18, 54), (50, 50), (82, 54), (86, 74)]},
    'front': afro('front', 50, 36, 56, 48) + band('front', 38, 12, 'orange')
             + [L(outline([(30, 36), (50, 34), (70, 36), (70, 48), (50, 46), (30, 48)]), 'band', 'f', False)] + brows(63, OUTC, 4.0, 14, 0.3, 13),
    'side': afro('side', 50, 36, 54, 48) + band('side', 38, 12, 'orange') + [L(outline([(60, 37), (93, 34), (93, 46), (60, 49)]), 'band', 'f', False)]
            + brow_side(63, OUTC, 4.0, 0.3),
    'back': afro('back', 50, 40, 56, 50) + band('back', 40, 12, 'orange'),
}

# Jen Quibble (portero): moreno y calvo, con un mechón crema en lo alto abierto como una flor de pétalos en punta y una punta
# que le baja hasta la frente; cara larga de adulto, cejas claras, nariz larga y sonrisa
CHARS[K + 'jen-quibble'] = {
    'body': 'normal', 'pal': pal('#e6dcbc', '#c28a52', iris='#2a2626', shade='#c4b898', deep='#a09474'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'nose': (50, 84, 3.6), 'hairline': False},
    'front': bald('front') + [leaf(50, 18, a, s, 'mid') for a, s in ((-1.3, 1.4), (1.3, 1.4), (-0.6, 1.8), (0.6, 1.8), (0.0, 2.0))]
             + [L(outline([(42, 20), (58, 20), (50, 54, 1)]), 'mid', 'f', ln=True)] + brows(63, 'shade', 3.0, 14, 0.3, 12),
    'side': bald('side') + [leaf(56, 16, a, s, 'mid') for a, s in ((-1.0, 1.6), (0.4, 1.8), (1.2, 1.4))]
            + [L(outline([(62, 16), (72, 18), (86, 40, 1), (70, 28)]), 'mid', 'f', ln=True)] + brow_side(63, 'shade', 3.0),
    'back': bald('back') + [leaf(50, 16, a, s, 'mid') for a, s in ((-1.3, 1.4), (1.3, 1.4), (0.0, 1.8))],
}

# Jess Uplement: grandullón de cara redonda; pelo azul pizarra en pinchos grandes en todas direcciones, gafas redondas de
# alambre negro, cejas fruncidas y sonrisa
CHARS[K + 'jess-uplement'] = {
    'body': 'corpulento', 'pal': pal('#3e5a76', '#f2bc88', iris='#2a2626', shade='#2e465c', deep='#203242'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'face_front': WIDE, 'hairline': [(14, 62), (20, 50), (50, 46), (80, 50), (86, 62)]},
    'front': messy('front', amp=18, n=9, seed=19, lo=60) + ring_glasses('front', 77, OUTC, 2.2, 8.5, 8, 15) + [L([(13, 74), (6, 72)], OUTC, 'f', False, False, 2.0),
                                                                                                           L([(87, 74), (94, 72)], OUTC, 'f', False, False, 2.0)],
    'side': messy('side', amp=18, n=9, seed=19) + ring_glasses('side', 77, OUTC, 2.2, 5, 8),
    'back': messy('back', amp=18, n=9, seed=19),
}

# Jig Charley-Charleston: pelo amarillo pálido en un cepillo altísimo de puntas rectas hacia arriba y los lados cortos; gafas
# de sol de montura amarilla y cristales naranjas, sonrisa y un lunar en la barbilla
CHARS[K + 'jig-charley-charleston'] = {
    'body': 'normal', 'pal': pal('#e2dea2', '#f4c28c', shade='#c2bc80', deep='#9c9660', frame='#eac232', lens='#d8481c'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': [(17, 62), (20, 48), (50, 46), (80, 48), (83, 62)]},
    'front': [L(outline([(18, 62), (16, 30), (8, -34, 1), (20, -28), (26, -44, 1), (36, -32), (44, -48, 1), (52, -32), (62, -44, 1), (70, -30), (80, -40, 1), (84, -26),
                         (92, -32, 1), (86, 30), (82, 62), (78, 48), (22, 48)])),
              L(outline([(62, -40), (70, -30), (80, -38), (84, -26), (90, -30), (86, 30), (82, 56), (74, 20)]), 'shade', 'b', False)]
             + [strand([(x, -26), (x + (50 - x) * 0.1, 40)], 'deep', 'b', 1.0) for x in (24, 36, 50, 64, 76)]
             + glasses_band('front', 76, 'frame', 'lens') + [L(ell(50, 100, 1.2, 1.2), (90, 60, 40, 255), 'f', False)],
    'side': [L(outline([(66, 50), (82, 46), (88, 28), (90, -24, 1), (78, -30), (72, -44, 1), (60, -32), (50, -48, 1), (40, -32), (28, -44, 1), (20, -28), (8, -34, 1), (6, 30),
                        (6, 58), (20, 76), (34, 74), (40, 60), (48, 52)])),
             L(outline([(6, 40), (30, 44), (40, 60), (34, 74), (20, 76), (6, 58)]), 'shade', 'b', False)] + glasses_band('side', 76, 'frame', 'lens'),
    'back': [L(outline([(18, 76), (16, 30), (8, -34, 1), (20, -28), (26, -44, 1), (36, -32), (44, -48, 1), (52, -32), (62, -44, 1), (70, -30), (80, -40, 1), (84, -26),
                        (92, -32, 1), (86, 30), (82, 76), (66, 84), (50, 86), (34, 84)])),
             L(outline([(62, -40), (70, -30), (80, -38), (84, -26), (90, -30), (86, 30), (82, 76), (62, 80)]), 'shade', 'b', False)] + glasses_band('back', 76, 'frame', 'lens'),
}

# Jim Cook: pelo crema corto con un rizo en lo alto; unas gafas redondas enormes de montura gris, ojos de punto, cejas
# fruncidas y boca enfurruñada (bajito)
CHARS[K + 'jim-cook'] = {
    'body': 'bajito', 'pal': pal('#f2e2b2', '#f4c28c', shade='#d2c090', deep='#ac9a6c', frame='#4c525a'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': [(16, 62), (20, 50), (36, 46), (50, 48), (64, 46), (80, 50), (84, 62)]},
    'front': crop('front', top=4, side=62, w=3)
             + [L(blob([(50, 20), (62, 10), (70, 18), (62, 30), (54, 24)], 6), 'light', 'b', False), strand([(52, 22), (62, 14), (66, 20)], 'shade', 'b', 1.2)]
             + fringe([(16, 56), (24, 52), (30, 58, 1), (38, 48), (46, 54, 1), (54, 46), (62, 54, 1), (70, 48), (78, 56, 1), (84, 52)], 30)
             + ring_glasses('front', 77, 'frame', 2.4, 12, 11, 15),
    'side': crop('side', top=2, nape=84, w=3) + ring_glasses('side', 77, 'frame', 2.4, 6, 11) + [fr([(72, 30), (90, 34), (90, 52, 1), (82, 44)])],
    'back': crop('back', top=4, nape=84, w=3) + [L([(12, 74), (16, 76)], 'frame', 'f', False, False, 2.4), L([(88, 74), (84, 76)], 'frame', 'f', False, False, 2.4)],
}

# Jim Makegood: rastas rosa parduzco recogidas hacia arriba en un manojo con una goma amarilla, que caen hacia los lados por
# arriba; cejas rosadas, sonrisa de lado y una cicatriz en cruz en la barbilla
CHARS[K + 'jim-makegood'] = {
    'body': 'normal', 'pal': pal('#b27c6c', '#f2bc88', iris='#2a2626', shade='#946252', deep='#74483c', tie='#e8c442', brow='#c08a90', scar='#c89a52'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'nose': (50, 84, 3.4), 'hairline': [(17, 60), (20, 48), (50, 44), (80, 48), (83, 60)]},
    'front': crop('front', top=12, side=60, w=1)
             + [l for x in (34, 42, 50, 58, 66) for l in coils(x, 44, 2, 7.5, 'mid', 'b', True)]
             + [L(rope((50, 0), (30, -18), (18, 6), 7), 'mid', 'b', ln=True), L(rope((50, 0), (70, -18), (82, 6), 7), 'mid', 'b', ln=True),
                L(rope((48, 0), (40, -22), (28, -10), 7), 'mid', 'b', ln=True), L(rope((52, 0), (60, -22), (72, -10), 7), 'mid', 'b', ln=True),
                L(ell(50, 4, 12, 3.4), 'tie', 'b', ln=True)]
             + brows(63, 'brow', 3.6, 14, 0.4, 12)
             + [L([(44, 98), (56, 106)], 'scar', 'f', False, False, 2.2), L([(56, 98), (44, 106)], 'scar', 'f', False, False, 2.2)],
    'side': crop('side', top=12, nape=82, w=1) + [l for x in (40, 50, 60) for l in coils(x, 40, 2, 7.5, 'mid', 'b', True)]
            + [L(rope((50, 0), (30, -18), (16, 8), 7), 'mid', 'b', ln=True), L(rope((52, 0), (70, -18), (80, 4), 7), 'mid', 'b', ln=True), L(ell(50, 4, 10, 3.4), 'tie', 'b', ln=True)]
            + brow_side(63, 'brow', 3.6),
    'back': crop('back', top=12, nape=82, w=1) + [l for x in (34, 42, 50, 58, 66) for l in coils(x, 48, 2, 7.5, 'mid', 'b', True)]
            + [L(rope((50, 0), (30, -18), (18, 8), 7), 'mid', 'b', ln=True), L(rope((50, 0), (70, -18), (82, 8), 7), 'mid', 'b', ln=True), L(ell(50, 4, 12, 3.4), 'tie', 'b', ln=True)],
}

# Jim Nastick: pelo verde corto con flequillo de puntas desiguales; ojos negros grandes de pillo y sonrisa abierta
CHARS[K + 'jim-nastick'] = {
    'body': 'normal', 'pal': pal('#5c9c3c', '#f4c28c', iris='#26222a', shade='#46802c', deep='#32601e'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': [(16, 62), (20, 50), (50, 46), (80, 50), (84, 62)]},
    'front': crop('front', top=0, side=62, w=3)
             + [L(outline([(40, 2), (44, -8, 1), (50, 0), (56, -6, 1), (60, 2)]), 'mid', 'b')]
             + fringe([(16, 58), (22, 52), (26, 62, 1), (34, 50), (40, 60, 1), (46, 48), (52, 58, 1), (58, 48), (64, 60, 1), (70, 50), (76, 60, 1), (84, 52)], 28)
             + side_lines(86, 27),
    'side': crop('side', top=-2, nape=84, w=3) + [fr([(72, 28), (92, 34), (92, 56, 1), (84, 46)])],
    'back': crop('back', top=0, nape=84, w=3),
}

# Jim Reed: piel morena; afro enorme castaño oliva con una cinta verde de raya amarilla; ojazos redondos, cejas fruncidas,
# rayas amarillas pintadas en las mejillas y labios gruesos
CHARS[K + 'jim-reed'] = {
    'body': 'normal', 'pal': pal('#5e4c22', '#aa7244', shade='#483a18', deep='#32280e', band='#6aa242', yellow='#e8d44c', lip='#b4664a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'none', 'hairline': [(14, 74), (18, 56), (50, 52), (82, 56), (86, 74)]},
    'front': afro('front', 50, 34, 60, 50) + band('front', 40, 12, 'band', 'yellow')
             + [L(outline([(22, 82), (34, 86), (34, 89), (22, 85)]), 'yellow', 'f', False), L(outline([(22, 88), (34, 92), (34, 95), (22, 91)]), 'yellow', 'f', False),
                L(outline([(78, 82), (66, 86), (66, 89), (78, 85)]), 'yellow', 'f', False), L(outline([(78, 88), (66, 92), (66, 95), (78, 91)]), 'yellow', 'f', False),
                L(blob([(38, 94), (50, 91), (62, 94), (58, 100), (50, 102), (42, 100)], 6), 'lip', 'f', ln=True), L([(40, 96), (60, 96)], OUTC, 'f', False, False, 1.0)],
    'side': afro('side', 50, 34, 58, 50) + band('side', 40, 12, 'band', 'yellow') + [L(outline([(66, 82), (78, 86), (78, 89), (66, 85)]), 'yellow', 'f', False)],
    'back': afro('back', 50, 38, 60, 52) + band('back', 40, 12, 'band', 'yellow'),
}


from chars_bigwaves import rect_glasses  # noqa: E402


def happy_eyes(y=75, sep=14, w=2.2):
    """Ojos cerrados de felicidad (arcos hacia arriba)."""
    return [L(quad((50 - sep - 6, y + 1), (50 - sep, y - 4), (50 - sep + 6, y + 1)), OUTC, 'f', False, False, w),
            L(quad((50 + sep - 6, y + 1), (50 + sep, y - 4), (50 + sep + 6, y + 1)), OUTC, 'f', False, False, w)]


def teeth_mouth(y=94, x0=38, x1=62, h=8):
    """Boca apretada enseñando los dientes (mueca)."""
    return [L(blob([(x0, y - h / 2), (x1, y - h / 2), (x1 + 1, y), (x1, y + h / 2), (x0, y + h / 2), (x0 - 1, y)], 4), (120, 70, 56, 255), 'f', ln=True),
            L(blob([(x0 + 2, y - h / 2 + 1.5), (x1 - 2, y - h / 2 + 1.5), (x1 - 2, y + h / 2 - 1.5), (x0 + 2, y + h / 2 - 1.5)], 4), WHITE, 'f', False),
            L([(x0 + 2, y), (x1 - 2, y)], OUTC, 'f', False, False, 0.9)]


# ---------------------------------------------------------------------------------------------------------------- hoja 6

# Jim Sweatman (portero): grandullón de cara ancha; pelo granate oscuro corto y peinado, con un mechón de punta en lo alto y
# dos picos en las sienes; ojos de rabia, nariz grande y una mueca enseñando los dientes
CHARS[K + 'jim-sweatman'] = {
    'body': 'corpulento', 'pal': pal('#5c3c3e', '#e8a868', iris='#2a2626', shade='#462c2e', deep='#301e20'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'face_front': WIDE, 'nose': (50, 84, 4.2),
             'hairline': [(14, 58), (18, 46), (34, 42), (50, 40), (66, 42), (82, 46), (86, 58)]},
    'front': crop('front', top=8, side=58, w=3)
             + [L(outline([(16, 54), (2, 40, 1), (16, 42)]), 'mid', 'b'), L(outline([(84, 54), (98, 40, 1), (84, 42)]), 'mid', 'b'),
                L(outline([(44, 10), (50, -10), (58, -18, 1), (56, -6), (58, 10)]), 'mid', 'b')] + teeth_mouth(96, 36, 64, 9),
    'side': crop('side', top=6, nape=82, w=3) + [L(outline([(48, 8), (54, -10), (62, -18, 1), (60, -4), (60, 8)]), 'mid', 'b'), L(outline([(76, 48), (92, 36, 1), (82, 46)]), 'mid', 'b')],
    'back': crop('back', top=8, nape=82, w=3) + [L(outline([(44, 10), (50, -10), (58, -18, 1), (56, -6), (58, 10)]), 'mid', 'b'),
                                                L(outline([(16, 54), (2, 40, 1), (16, 42)]), 'mid', 'b'), L(outline([(84, 54), (98, 40, 1), (84, 42)]), 'mid', 'b')],
}

# Jimmy Mach: piel morena; melena lisa color crema hasta los hombros que se vuelve rosa en las puntas, con un mechón que le
# cae por el centro de la cara; ojos verde oliva, cejas fruncidas y media sonrisa
CHARS[K + 'jimmy-mach'] = {
    'body': 'normal', 'pal': pal('#ece0c6', '#ac7648', iris='#7c8c42', shade='#ccbfa6', deep='#a69a82', pink='#c8928e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': [(18, 62), (26, 44), (50, 40), (74, 44), (82, 62)]},
    'front': longhair('front', length=110, flare=4)
             + [fr([(28, 42), (50, 30), (68, 40), (60, 54), (54, 76, 1), (48, 56), (38, 52)]), L(outline([(50, 62), (56, 64), (54, 76, 1)]), 'pink', 'f', False),
                fr([(18, 64), (20, 44), (30, 40), (26, 60), (24, 84, 1)]), fr([(82, 64), (80, 44), (70, 40), (74, 60), (76, 84, 1)]),
                L(outline([(19, 66), (25.5, 66), (24, 84, 1)]), 'pink', 'f', False), L(outline([(81, 66), (74.5, 66), (76, 84, 1)]), 'pink', 'f', False)],
    'side': longhair('side', length=110, flare=4) + [L(outline([(4, 86), (40, 86), (40, 94), (24, 104), (4, 104)]), 'pink', 'b', False),
                                                     fr([(70, 30), (90, 40), (92, 70, 1), (82, 54)])],
    'back': longhair('back', length=112, flare=4, ends=4) + [L(outline([(6, 88), (94, 88), (96, 106), (50, 108), (4, 106)]), 'pink', 'b', False)],
}

# Jody MacGough: pelo gris malva revuelto con dos pelos de antena hacia un lado y flequillo de puntas; ojos castaños y boca
# seria
CHARS[K + 'jody-macgough'] = {
    'body': 'normal', 'pal': pal('#9c8496', '#f4c28c', iris='#5c3c2a', shade='#7e6878', deep='#604e5a'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 93, 'hairline': False},
    'front': messy('front', amp=9, n=10, seed=23, lo=66)
             + [L(quad((62, 6), (70, -14), (80, -16)), 'mid', 'b', False, False, 3.0), L(quad((66, 8), (80, -4), (88, -2)), 'mid', 'b', False, False, 2.6)]
             + fringe([(16, 68), (22, 54), (28, 66, 1), (36, 52), (42, 64, 1), (50, 50), (56, 64, 1), (64, 52), (70, 66, 1), (78, 54), (84, 68)], 32),
    'side': messy('side', amp=9, n=10, seed=23) + [L(quad((60, 4), (70, -14), (80, -14)), 'mid', 'b', False, False, 3.0), fr([(72, 30), (92, 38), (92, 62, 1), (84, 52)])],
    'back': messy('back', amp=9, n=10, seed=23) + [L(quad((40, 4), (32, -14), (22, -16)), 'mid', 'b', False, False, 3.0)],
}

# Joe Lamkin: pelo blanco crema peinado hacia atrás y levantado en una punta en lo alto; gafas finas rectangulares, ojos
# cerrados de felicidad y sonrisa amable (adulto)
CHARS[K + 'joe-lamkin'] = {
    'body': 'normal', 'pal': pal('#ece4c2', '#f4c28c', shade='#ccc29e', deep='#a69c7a'),
    'face': {'eyes': 'none', 'brows': True, 'mouth': 'smile', 'mouth_y': 93, 'hairline': [(17, 62), (18, 46), (32, 40), (50, 38), (68, 40), (82, 46), (83, 62)]},
    'front': crop('front', top=4, side=62, w=0)
             + [L(outline([(36, 8), (50, -16, 1), (64, 8), (50, 16)]), 'mid', 'b')] + [strand([(50, -8), (x, 36)], 'deep', 'b', 1.0) for x in (26, 38, 50, 62, 74)]
             + happy_eyes(76) + rect_glasses('front', 76, (60, 56, 52, 255)) + [L(quad((40, 64), (44, 62), (48, 64)), OUTC, 'f', False, False, 1.2),
                                                                                L(quad((52, 64), (56, 62), (60, 64)), OUTC, 'f', False, False, 1.2)],
    'side': crop('side', top=2, nape=82, w=0) + [L(outline([(60, 2), (76, -14, 1), (78, 10)]), 'mid', 'b'), strand([(80, 8), (40, 6), (12, 30)], 'deep', 'b', 1.0)]
            + rect_glasses('side', 76, (60, 56, 52, 255)),
    'back': crop('back', top=4, nape=82, w=0) + [L(outline([(36, 8), (50, -16, 1), (64, 8), (50, 16)]), 'mid', 'b')]
            + [strand([(50, 4), (x, 80)], 'deep', 'b', 1.0) for x in (30, 42, 58, 70)],
}

# Joe Nalist (portero): pelo rosa rojizo peinado de lado con un flequillo largo que le cruza la frente en diagonal y puntas
# abiertas a los lados; ojos entornados de rabia y media sonrisa
CHARS[K + 'joe-nalist'] = {
    'body': 'normal', 'pal': pal('#c86c6c', '#f4c28c', iris='#2a2626', shade='#a65454', deep='#843e3e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': [(16, 64), (20, 50), (50, 46), (80, 50), (84, 64)]},
    'front': crop('front', top=0, side=64, w=4)
             + [L(outline([(14, 62), (0, 74, 1), (14, 70)]), 'mid', 'b'), L(outline([(86, 60), (100, 70, 1), (86, 68)]), 'mid', 'b')]
             + fringe([(14, 64), (20, 58), (30, 54), (40, 52), (50, 48), (62, 44), (74, 42), (84, 44), (90, 48, 1)], 24)
             + [strand([(82, 10), (60, 22), (34, 44)], 'deep', 'b', 1.0), strand([(70, 6), (44, 24), (22, 52)], 'deep', 'b', 1.0)],
    'side': crop('side', top=-2, nape=84, w=4) + [L(outline([(38, 64), (28, 80, 1), (34, 62)]), 'mid', 'b'), fr([(70, 26), (92, 34), (94, 58, 1), (84, 48)])],
    'back': crop('back', top=0, nape=84, w=4) + [L(outline([(14, 64), (0, 76, 1), (14, 72)]), 'mid', 'b'), L(outline([(86, 64), (100, 76, 1), (86, 72)]), 'mid', 'b')],
}

# Joe Rassock (portero): pelo castaño oliva en un mechón enorme que sube y cae en curva hacia su derecha, con un pañuelo
# rojo atado en el otro lado de la cabeza; cejas oliva gruesas, nariz grande y sonrisa (adulto)
CHARS[K + 'joe-rassock'] = {
    'body': 'normal', 'pal': pal('#7c6c32', '#f2bc88', iris='#2a2626', shade='#605224', deep='#443a18', red='#c23422', red_d='#9a2618', brow='#8c7c3a'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'nose': (50, 84, 4.0), 'hairline': [(16, 62), (20, 48), (50, 42), (80, 48), (84, 62)]},
    'front': crop('front', top=4, side=62, w=2)
             + [L(outline([(12, 80, 1), (6, 56), (10, 30), (2, 6, 1), (18, 6), (28, -10), (46, -12), (60, -4), (52, 8), (40, 20), (30, 36), (22, 56)])),
                L(outline([(30, -8), (56, -6), (44, 6), (32, 20), (20, 16)]), 'shade', 'b', False),
                L(outline([(46, 4), (64, -2), (84, 8), (92, 28), (90, 48), (84, 50), (76, 26), (58, 16)]), 'red', 'f', ln=True),
                L(outline([(88, 36), (104, 56, 1), (98, 60), (86, 46)]), 'red', 'f', ln=True), L(outline([(86, 42), (96, 70, 1), (90, 72), (84, 50)]), 'red_d', 'f', ln=True)]
             + brows(63, 'brow', 5.0, 14, 0.0, 13),
    'side': crop('side', top=2, nape=84, w=2)
            + [L(outline([(60, -8), (86, 0), (92, 20), (86, 44), (78, 30), (70, 10)]), 'mid', 'b'),
               L(outline([(10, 20), (40, 0), (66, 2), (70, 14), (44, 18), (12, 36)]), 'red', 'f', ln=True),
               L(outline([(12, 26), (-6, 48, 1), (0, 52), (16, 34)]), 'red', 'f', ln=True)] + brow_side(63, 'brow', 5.0),
    'back': crop('back', top=4, nape=84, w=2)
            + [L(outline([(88, 80, 1), (94, 56), (90, 30), (98, 6, 1), (82, 6), (72, -10), (54, -12), (46, 0), (60, 20), (72, 40), (80, 60)])),
               L(outline([(12, 40), (10, 18), (30, 2), (54, -2), (48, 14), (30, 30)]), 'red', 'f', ln=True),
               L(outline([(30, 24), (24, 54, 1), (32, 54), (38, 28)]), 'red', 'f', ln=True)],
}

# Joe Stick: pelo verde peinado hacia atrás con mechones que le caen por las sienes; una cicatriz en forma de estrella en la
# mejilla, cejas fruncidas, nariz grande y sonrisa ladina
CHARS[K + 'joe-stick'] = {
    'body': 'normal', 'pal': pal('#2c8c5c', '#f2bc88', iris='#2a2626', shade='#206e46', deep='#165034', star='#e89c3c'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'nose': (50, 84, 4.2), 'hairline': [(16, 62), (20, 48), (34, 42), (50, 40), (66, 42), (80, 48), (84, 62)]},
    'front': crop('front', top=2, side=62, w=2)
             + [strand([(30, 8), (26, 40)], 'deep', 'b', 1.0), strand([(44, 4), (42, 38)], 'deep', 'b', 1.0), strand([(58, 4), (60, 38)], 'deep', 'b', 1.0),
                strand([(72, 8), (76, 40)], 'deep', 'b', 1.0),
                fr([(22, 44), (30, 40), (28, 56), (22, 68, 1)]), fr([(78, 44), (70, 40), (72, 56), (78, 68, 1)]),
                L(outline([(70, 80), (72, 84), (77, 84), (73, 87), (75, 92), (70, 89), (65, 92), (67, 87), (63, 84), (68, 84)]), 'star', 'f', ln=True)],
    'side': crop('side', top=0, nape=84, w=2) + [strand([(80, 8), (40, 6), (10, 30)], 'deep', 'b', 1.0), strand([(84, 30), (50, 24), (14, 48)], 'deep', 'b', 1.0),
                                                L(outline([(74, 80), (76, 84), (81, 84), (77, 87), (79, 92), (74, 89), (69, 92), (71, 87), (67, 84), (72, 84)]), 'star', 'f', ln=True)],
    'back': crop('back', top=2, nape=84, w=2) + [strand([(50, 4), (x, 80)], 'deep', 'b', 1.0) for x in (30, 42, 58, 70)],
}

# Joe Straiter (portero): pelo verde azulado corto con un tupé enorme en cresta que se enrolla hacia delante, a rayas rosa
# grisáceo; ojos azules grandes, cejas fruncidas y boca seria
CHARS[K + 'joe-straiter'] = {
    'body': 'normal', 'pal': pal('#5c9caa', '#f4c28c', iris='#6aa8d2', shade='#467e8a', deep='#30606a', pink='#b88c9a', pink_d='#966e7c'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': [(16, 62), (20, 50), (50, 46), (80, 50), (84, 62)]},
    'front': crop('front', top=6, side=62, w=2)
             + [L(outline([(34, 44), (30, 12), (36, -10), (52, -24), (70, -20), (76, -6), (70, 4), (62, -4), (56, 6), (60, 44), (48, 52, 1)]), 'mid', 'f', ln=True),
                L(outline([(40, -6), (54, -20), (62, -18), (50, -2), (44, 20)]), 'pink', 'f', False),
                L(outline([(58, -14), (68, -18), (72, -8), (64, -2)]), 'pink', 'f', False),
                L(outline([(46, 30), (56, 20), (58, 34), (50, 44)]), 'pink', 'f', False)],
    'side': crop('side', top=4, nape=84, w=2)
            + [L(outline([(40, 4), (50, -18), (72, -28), (92, -18), (96, 0), (86, 10), (82, -4), (70, -8), (60, 6), (56, 14)]), 'mid', 'f', ln=True),
               L(outline([(54, -10), (72, -24), (80, -22), (66, -8), (58, 6)]), 'pink', 'f', False)],
    'back': crop('back', top=6, nape=84, w=2) + [L(outline([(38, 30), (36, 0), (50, -22), (64, 0), (62, 30)]), 'mid', 'b'),
                                                L(outline([(44, 20), (44, 0), (50, -16), (56, 0), (56, 20)]), 'pink', 'b', False)],
}


def wolverine(view, flick=False):
    """Pelo que enmarca la cara con dos patillas enormes en punta hacia fuera (Jay Archer, John Maggie)."""
    if view == 'front':
        top = [(10, 22), (22, 6), (50, 0), (78, 6), (90, 22)] if not flick else [(10, 22), (22, 4), (48, -4), (70, 0), (100, -2, 1), (90, 12), (92, 24)]
        return [L(outline([(12, 92), (-6, 96, 1), (6, 80), (4, 62), (-8, 52, 1), (8, 46)] + top + [(92, 46), (108, 52, 1), (96, 62), (94, 80), (106, 96, 1), (88, 92), (84, 76),
                           (84, 58), (16, 58), (16, 76)])),
                L(outline([(60, 2), (86, 16), (92, 44), (104, 52), (94, 62), (92, 80), (100, 94), (86, 90), (84, 60)]), 'shade', 'b', False)]
    if view == 'side':
        return [L(outline([(70, 56), (86, 52), (92, 30), (80, 6), (50, -2), (22, 4), (6, 24), (2, 50), (8, 72), (20, 82), (34, 96, 1), (44, 84), (66, 98, 1), (60, 80), (56, 64)])),
                L(outline([(4, 44), (30, 48), (44, 70), (36, 82), (20, 80), (8, 68)]), 'shade', 'b', False), fr([(74, 30), (92, 38), (94, 60, 1), (84, 52)])]
    return [L(outline([(12, 92), (-6, 96, 1), (6, 80), (4, 62), (-8, 52, 1), (8, 46), (10, 22), (22, 6), (50, 0), (78, 6), (90, 22), (92, 46), (108, 52, 1), (96, 62),
                       (94, 80), (106, 96, 1), (88, 92), (66, 90), (50, 92), (34, 90)])),
            L(outline([(58, 2), (86, 16), (92, 44), (104, 52), (94, 62), (92, 80), (100, 94), (64, 90)]), 'shade', 'b', False)]


def bob(view, length=92, flick=8, c='mid'):
    """Melena corta hasta la mandíbula con las puntas hacia fuera."""
    if view == 'front':
        return [L(outline([(12, length, 1), (2, length + 4, 1), (8, length - 10), (8, 50), (14, 22), (30, 6), (50, 0), (70, 6), (86, 22), (92, 50), (92, length - 10),
                           (98, length + 4, 1), (88, length, 1), (80, length - 12), (80, 60), (20, 60), (20, length - 12)]), c),
                L(outline([(60, 2), (84, 18), (92, 50), (92, length - 12), (82, length - 14), (82, 50)]), 'shade', 'b', False)]
    if view == 'side':
        return [L(outline([(70, 52), (86, 48), (92, 28), (80, 6), (50, -2), (22, 4), (6, 24), (2, 56), (4, length - 8), (-4, length + 4, 1), (12, length), (30, length + 2, 1),
                           (36, length - 10), (42, 70), (52, 58)]), c),
                L(outline([(4, 46), (30, 50), (40, 70), (34, length - 8), (6, length - 6)]), 'shade', 'b', False)]
    return [L(outline([(12, length, 1), (2, length + 4, 1), (8, length - 10), (8, 50), (14, 22), (30, 6), (50, 0), (70, 6), (86, 22), (92, 50), (92, length - 10),
                       (98, length + 4, 1), (88, length, 1), (70, length - 4), (50, length - 2), (30, length - 4)]), c),
            L(outline([(58, 2), (84, 18), (92, 50), (92, length - 10), (64, length - 4)]), 'shade', 'b', False)]


# ---------------------------------------------------------------------------------------------------------------- hojas 7 y 8

# John Baird: piel morena; pelo castaño oliva peinado hacia atrás con unos mechones sueltos sobre la frente y las puntas
# abiertas hacia fuera a la altura de la mandíbula; ojazos blancos de pupila pequeña y sonrisa ladina
CHARS[K + 'john-baird'] = {
    'body': 'normal', 'pal': pal('#5c4c2a', '#a87442', iris='#2a2626', shade='#463a1e', deep='#302814'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': [(18, 72), (22, 50), (36, 44), (50, 40), (64, 44), (78, 50), (82, 72)]},
    'front': [L(outline([(10, 96, 1), (14, 72), (12, 40), (20, 14), (50, 2), (80, 14), (88, 40), (86, 72), (90, 96, 1), (80, 82), (80, 58), (20, 58), (20, 82)])),
              L(outline([(60, 4), (80, 14), (88, 40), (86, 72), (88, 92), (80, 80), (80, 50)]), 'shade', 'b', False),
              fr([(38, 40), (48, 32), (50, 44), (44, 60, 1), (42, 48)]), fr([(52, 36), (60, 34), (60, 48), (56, 56, 1)]),
              strand([(36, 8), (30, 40)], 'deep', 'b', 1.0), strand([(64, 8), (70, 40)], 'deep', 'b', 1.0)] + side_lines(84, 27),
    'side': [L(outline([(66, 46), (82, 42), (88, 24), (76, 4), (50, -2), (22, 4), (6, 22), (2, 50), (6, 80), (-2, 96, 1), (14, 88), (26, 98, 1), (32, 84), (40, 68), (48, 54)])),
             L(outline([(4, 44), (30, 46), (40, 66), (30, 84), (8, 84)]), 'shade', 'b', False), strand([(80, 8), (40, 6), (12, 30)], 'deep', 'b', 1.0)],
    'back': [L(outline([(10, 96, 1), (14, 72), (12, 40), (20, 14), (50, 2), (80, 14), (88, 40), (86, 72), (90, 96, 1), (70, 88), (50, 90), (30, 88)])),
             L(outline([(58, 4), (80, 14), (88, 40), (86, 72), (88, 92), (64, 88)]), 'shade', 'b', False)],
}

# John Coralli (portero): pelo verde azulado oscuro con raya en medio y dos cortinas de flequillo que le tapan las sienes;
# cara larga, ojos afilados, cejas fruncidas y media sonrisa
CHARS[K + 'john-coralli'] = {
    'body': 'normal', 'pal': pal('#3e6c66', '#f4c28c', iris='#2a2626', shade='#2e5450', deep='#203c38'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': [(16, 64), (20, 48), (36, 42), (50, 40), (64, 42), (80, 48), (84, 64)]},
    'front': crop('front', top=2, side=64, w=2)
             + [fr([(50, 30), (34, 32), (22, 42), (18, 64, 1), (26, 52), (36, 44), (48, 42)]), fr([(50, 30), (66, 32), (78, 42), (82, 64, 1), (74, 52), (64, 44), (52, 42)]),
                strand([(50, 4), (50, 32)], 'deep', 'b', 1.2)],
    'side': crop('side', top=0, nape=84, w=2) + [fr([(66, 26), (88, 34), (92, 58, 1), (82, 46)])],
    'back': crop('back', top=2, nape=84, w=2) + [strand([(50, 4), (50, 80)], 'deep', 'b', 1.0)],
}

# John Corder: casco de pelo morado oscuro con flequillo recto y dos puntas abiertas a los lados; ojos verde azulado
# entornados, nariz chiquita y sonrisa pícara (bajito)
CHARS[K + 'john-corder'] = {
    'body': 'bajito', 'pal': pal('#4c3c6c', '#f4c28c', iris='#5ca2a2', shade='#3a2e54', deep='#28203c'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'nose': (50, 84, 2.4), 'hairline': False},
    'front': [L(outline([(14, 64), (2, 52, 1), (12, 46), (12, 22), (26, 6), (50, 0), (74, 6), (88, 22), (88, 46), (98, 52, 1), (86, 64), (80, 58), (20, 58)])),
              L(outline([(60, 2), (86, 18), (88, 46), (94, 52), (84, 60), (80, 40)]), 'shade', 'b', False)]
             + fringe([(16, 58), (84, 58)], 30) + [strand([(x, 8), (x, 56)], 'deep', 'b', 1.0) for x in (30, 42, 58, 70)],
    'side': [L(outline([(70, 56), (86, 52), (92, 30), (80, 6), (50, -2), (22, 4), (6, 24), (-4, 46, 1), (6, 52), (8, 72), (22, 80), (36, 78), (42, 64), (50, 58)])),
             L(outline([(4, 44), (30, 48), (42, 64), (36, 78), (22, 80), (8, 70)]), 'shade', 'b', False), fr([(74, 30), (92, 36), (92, 58), (84, 58)])],
    'back': [L(outline([(14, 76), (2, 56, 1), (12, 48), (12, 22), (26, 6), (50, 0), (74, 6), (88, 22), (88, 48), (98, 56, 1), (86, 76), (66, 84), (50, 86), (34, 84)])),
             L(outline([(58, 2), (86, 18), (88, 48), (94, 56), (86, 76), (62, 80)]), 'shade', 'b', False)],
}

# John Demi: pelo verde peinado hacia atrás en mechones, largo hasta la nuca; cejas verdes gruesas, ojos entornados, nariz
# grande y una sonrisa de lado (adulto, alto)
CHARS[K + 'john-demi'] = {
    'body': 'delgado', 'pal': pal('#6caa3c', '#eeba88', iris='#2a2626', shade='#54882c', deep='#3c641e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'nose': (50, 84, 4.4), 'hairline': [(18, 66), (22, 48), (36, 42), (50, 40), (64, 42), (78, 48), (82, 66)]},
    'front': [L(outline([(12, 96), (10, 60), (12, 30), (26, 8), (50, 0), (74, 8), (88, 30), (90, 60), (88, 96), (80, 86), (80, 50), (20, 50), (20, 86)])),
              L(outline([(60, 2), (82, 14), (90, 40), (88, 92), (82, 60)]), 'shade', 'b', False)]
             + [strand([(x, 4), (x + (x - 50) * 0.3, 44)], 'deep', 'b', 1.0) for x in (34, 44, 56, 66)] + brows(63, 'shade', 5.0, 14, 0.5, 13) + side_lines(86, 28),
    'side': [L(outline([(66, 48), (82, 44), (88, 26), (76, 4), (50, -2), (22, 4), (6, 22), (2, 52), (4, 86), (10, 100, 1), (24, 92), (34, 84), (40, 66), (48, 54)])),
             L(outline([(4, 44), (30, 48), (40, 66), (30, 86), (10, 96)]), 'shade', 'b', False)]
            + [strand([(84, 10 + k * 10), (40, 6 + k * 12), (10, 30 + k * 14)], 'deep', 'b', 1.0) for k in range(3)] + brow_side(63, 'shade', 5.0, 0.5),
    'back': [L(outline([(12, 96), (10, 60), (12, 30), (26, 8), (50, 0), (74, 8), (88, 30), (90, 60), (88, 96), (66, 100), (50, 102), (34, 100)])),
             L(outline([(58, 2), (82, 14), (90, 40), (88, 96), (60, 100)]), 'shade', 'b', False)]
            + [strand([(x, 6), (x, 96)], 'deep', 'b', 1.0) for x in (32, 44, 56, 68)],
}

# John Maggie: grandullón de cara ancha; pelo azul marino con un pico echado hacia un lado y dos patillas enormes en punta
# hacia fuera; ojos pequeños, cejas fruncidas y la boca muy enfadada
CHARS[K + 'john-maggie'] = {
    'body': 'corpulento', 'pal': pal('#2c4c7c', '#f4c28c', iris='#2a2626', shade='#203a60', deep='#162844'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 97, 'face_front': WIDE, 'nose': (50, 85, 3.6), 'ears': False,
             'hairline': [(14, 78), (20, 58), (36, 52), (50, 58), (64, 52), (80, 58), (86, 78)]},
    'front': wolverine('front', True) + [L(quad((40, 98), (50, 93), (60, 98)), OUTC, 'f', False, False, 1.8)],
    'side': wolverine('side'),
    'back': wolverine('back'),
}

# Jon Driedon: pelo verde azulado en pinchos echados hacia atrás; cejas negras gruesas en ángulo, ojillos negros, cara
# larga de adulto y la boca seria
CHARS[K + 'jon-driedon'] = {
    'body': 'normal', 'pal': pal('#4c8c9c', '#f4c28c', iris='#2a2626', shade='#3a6e7c', deep='#28505c'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'line', 'mouth_y': 95, 'hairline': [(17, 62), (20, 48), (34, 44), (50, 42), (66, 44), (80, 48), (83, 62)]},
    'front': [L(outline([(17, 64), (4, 58, 1), (14, 48), (8, 30, 1), (18, 24), (16, 6, 1), (32, 10), (40, -6, 1), (52, 4), (64, -4, 1), (70, 8), (86, 4, 1), (84, 22),
                         (96, 30, 1), (88, 44), (98, 56, 1), (83, 64), (78, 48), (22, 48)])),
              L(outline([(60, 0), (70, 8), (84, 6), (84, 24), (94, 32), (86, 46), (82, 58), (76, 28)]), 'shade', 'b', False)]
             + [L([(28, 62), (44, 68)], OUTC, 'f', False, False, 4.2), L([(72, 62), (56, 68)], OUTC, 'f', False, False, 4.2)],
    'side': [L(outline([(66, 48), (82, 44), (90, 30), (86, 12), (70, 2), (62, -8, 1), (48, 0), (30, -6, 1), (24, 6), (2, 4, 1), (8, 20), (-10, 30, 1), (4, 40), (-8, 56, 1), (8, 60),
                        (20, 78), (34, 76), (40, 62), (48, 54)])),
             L(outline([(6, 40), (30, 44), (40, 60), (34, 76), (20, 78), (8, 60)]), 'shade', 'b', False), L([(74, 62), (86, 66)], OUTC, 'f', False, False, 4.2)],
    'back': [L(outline([(17, 76), (2, 64, 1), (14, 52), (6, 34, 1), (18, 26), (14, 8, 1), (32, 12), (40, -4, 1), (52, 6), (64, -2, 1), (70, 10), (88, 6, 1), (84, 26), (98, 34, 1),
                        (88, 50), (100, 62, 1), (83, 76), (66, 84), (50, 86), (34, 84)])),
             L(outline([(58, 2), (70, 10), (86, 8), (84, 28), (96, 36), (88, 52), (83, 76), (62, 80)]), 'shade', 'b', False)],
}

# Jon Quill: melena gris parda hasta la mandíbula con raya casi en medio, un rizo en lo alto y las puntas hacia fuera; ojos
# verde azulado con pestañas y sonrisa de pillo
CHARS[K + 'jon-quill'] = {
    'body': 'normal', 'pal': pal('#9c9678', '#f4c28c', iris='#5ca2a2', shade='#7e785e', deep='#605a44'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': [(18, 66), (24, 50), (38, 44), (46, 40), (52, 46), (64, 44), (78, 50), (82, 66)]},
    'front': bob('front', 90) + [L(quad((44, 4), (52, 14), (46, 24)), 'shade', 'b', False, False, 2.6), strand([(46, 2), (44, 40)], 'deep', 'b', 1.2)]
             + [L([(25, 70), (23, 67)], OUTC, 'f', False, False, 1.0), L([(75, 70), (77, 67)], OUTC, 'f', False, False, 1.0)],
    'side': bob('side', 90),
    'back': bob('back', 90),
}

# Jonah Troutman: pelo gris beige en pinchos de punta, con un mechón verde oliva largo que le tapa un ojo; ojos verde
# azulado, cejas fruncidas y media sonrisa
CHARS[K + 'jonah-troutman'] = {
    'body': 'normal', 'pal': pal('#a29c86', '#f4c28c', iris='#5ca2a2', shade='#827c68', deep='#625e4c', olive='#5c5c2a'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': [(16, 62), (20, 50), (50, 46), (80, 50), (84, 62)]},
    'front': [L(outline([(16, 64), (2, 58, 1), (14, 50), (4, 34, 1), (16, 30), (12, 10, 1), (30, 14), (36, -4, 1), (48, 8), (62, -2, 1), (66, 10), (90, 0, 1), (84, 22),
                         (100, 30, 1), (88, 42), (98, 58, 1), (84, 64), (80, 48), (20, 48)])),
              L(outline([(62, 0), (66, 10), (86, 4), (84, 24), (96, 32), (88, 44), (84, 58), (76, 30)]), 'shade', 'b', False),
              fr([(22, 30), (40, 20), (54, 28), (44, 44), (36, 66), (30, 92, 1), (26, 64), (20, 50)], 'olive')],
    'side': [L(outline([(66, 48), (82, 44), (94, 34, 1), (86, 26), (96, 10, 1), (78, 10), (78, -6, 1), (62, 4), (50, -10, 1), (40, 4), (20, -2, 1), (20, 12), (2, 14, 1), (8, 30),
                        (-6, 42, 1), (6, 50), (20, 76), (34, 74), (40, 60), (48, 54)])),
             L(outline([(6, 40), (30, 44), (40, 60), (34, 74), (20, 76), (8, 58)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 76), (2, 62, 1), (14, 54), (4, 36, 1), (16, 30), (12, 10, 1), (30, 14), (36, -4, 1), (48, 8), (62, -2, 1), (66, 10), (90, 0, 1), (84, 22),
                        (100, 30, 1), (88, 46), (98, 62, 1), (84, 76), (66, 84), (50, 86), (34, 84)])),
             L(outline([(60, 0), (66, 10), (86, 4), (84, 24), (96, 32), (88, 48), (84, 74), (62, 80)]), 'shade', 'b', False),
             L(outline([(72, 10), (84, 20), (82, 40), (74, 34)]), 'olive', 'b', False)],
}

# Jonny Strutt: pelo rubio en un tupé enorme que sube en bloque hacia su izquierda, con el flequillo de mechones y una
# coletita en la nuca; ojos verdes, cejas fruncidas y sonrisa
CHARS[K + 'jonny-strutt'] = {
    'body': 'normal', 'pal': pal('#e2c262', '#f4c28c', iris='#6a9c3c', shade='#c2a044', deep='#9a7c2c'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': [(16, 62), (20, 50), (50, 46), (80, 50), (84, 62)]},
    'front': [L(outline([(16, 64), (12, 40), (8, 8), (12, -12, 1), (40, -14), (70, -16), (98, -20, 1), (90, 4), (88, 30), (84, 64), (80, 48), (20, 48)])),
              L(outline([(60, -14), (96, -18), (90, 4), (88, 30), (84, 58), (78, 20)]), 'shade', 'b', False)]
             + fringe([(18, 58), (26, 50), (34, 60, 1), (42, 46), (52, 58, 1), (60, 46), (70, 62, 1), (78, 50), (86, 66, 1), (84, 46)], 28)
             + [strand([(20, -8), (34, 40)], 'deep', 'b', 1.0), strand([(50, -12), (58, 40)], 'deep', 'b', 1.0)],
    'side': [L(outline([(66, 48), (82, 44), (96, 34), (100, 6), (106, -18, 1), (78, -12), (50, -10), (24, -4), (8, 14), (2, 40), (6, 62), (20, 78), (34, 76), (40, 62), (48, 54)])),
             L(outline([(4, 40), (30, 44), (40, 60), (34, 76), (20, 78), (6, 60)]), 'shade', 'b', False),
             L(outline([(8, 70), (-6, 84, 1), (12, 78)]), 'mid', 'b'), fr([(74, 30), (94, 38), (96, 62, 1), (86, 52)])],
    'back': [L(outline([(16, 76), (12, 40), (8, 8), (12, -12, 1), (40, -14), (70, -16), (98, -20, 1), (90, 4), (88, 30), (84, 76), (66, 84), (50, 86), (34, 84)])),
             L(outline([(60, -14), (96, -18), (90, 4), (88, 30), (84, 74), (62, 80)]), 'shade', 'b', False),
             L(outline([(44, 80), (50, 98, 1), (56, 80)]), 'mid', 'f', ln=True)],
}

# Jools Iceberg: pelo gris pardo recogido en una coleta alta en lo alto, con mechones ondulados a los lados hasta la
# mandíbula; ojos apretados como cruces, rayitas en las mejillas y una sonrisa ondulada
CHARS[K + 'jools-iceberg'] = {
    'body': 'normal', 'pal': pal('#9c8c6c', '#f4c28c', shade='#7e7054', deep='#60543e', tie='#6c6c3a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': [(18, 62), (24, 48), (50, 44), (76, 48), (82, 62)]},
    'front': crop('front', top=6, side=62, w=1)
             + [L(outline([(42, 6), (40, -12), (50, -24), (62, -20), (58, -10), (52, -14), (58, 6)]), 'mid', 'b'), L(ell(50, 4, 8, 3), 'tie', 'b', ln=True),
                L(rope((18, 60), (12, 76), (18, 92), 6), 'mid', 'f', ln=True), L(rope((82, 60), (88, 76), (82, 92), 6), 'mid', 'f', ln=True)]
             + fringe([(18, 56), (26, 50), (32, 58, 1), (40, 46), (48, 56, 1), (56, 46), (64, 56, 1), (72, 48), (80, 56, 1), (82, 48)], 28)
             + [L([(28, 72), (40, 76), (28, 80)], OUTC, 'f', False, False, 2.0), L([(72, 72), (60, 76), (72, 80)], OUTC, 'f', False, False, 2.0),
                L([(40, 92), (44, 90), (48, 92), (52, 90), (56, 92), (60, 90)], OUTC, 'f', False, False, 1.4)] + side_lines(86, 28),
    'side': crop('side', top=4, nape=82, w=1)
            + [L(outline([(40, 6), (36, -12), (46, -24), (58, -20), (54, -10), (48, -14), (54, 6)]), 'mid', 'b'), L(rope((60, 58), (66, 76), (62, 92), 6), 'mid', 'f', ln=True),
               L([(78, 72), (86, 76), (78, 80)], OUTC, 'f', False, False, 2.0)],
    'back': crop('back', top=6, nape=82, w=1) + [L(outline([(42, 6), (40, -12), (50, -24), (62, -20), (58, -10), (52, -14), (58, 6)]), 'mid', 'b'),
                                                L(ell(50, 4, 8, 3), 'tie', 'b', ln=True)],
}

# Josh Rogan: piel morena; melena azul marino con puntas abiertas a los lados, un punto rojo (bindi) en la frente, ojos
# amarillos con pestañas y sonrisa
CHARS[K + 'josh-rogan'] = {
    'body': 'normal', 'pal': pal('#2c4668', '#b07a4a', iris='#e8d020', shade='#203452', deep='#16243a', bindi='#b84a22'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 93, 'hairline': [(16, 66), (20, 50), (36, 44), (50, 46), (64, 44), (80, 50), (84, 66)]},
    'front': [L(outline([(14, 72), (-2, 52, 1), (8, 44), (12, 22), (26, 6), (50, 0), (74, 6), (88, 22), (90, 50), (96, 66, 1), (86, 70), (82, 56), (18, 56)])),
              L(outline([(60, 2), (86, 18), (90, 50), (94, 64), (84, 64), (80, 40)]), 'shade', 'b', False),
              strand([(50, 2), (50, 40)], 'deep', 'b', 1.0),
              L(ell(50, 54, 2.4, 3.4), 'bindi', 'f', ln=True)]
             + [L([(25, 70), (22, 67)], OUTC, 'f', False, False, 1.0), L([(75, 70), (78, 67)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(70, 52), (86, 48), (92, 28), (80, 6), (50, -2), (22, 4), (6, 24), (2, 50), (6, 72), (-4, 82, 1), (14, 80), (24, 86), (36, 80), (42, 64), (52, 56)])),
             L(outline([(4, 46), (30, 50), (42, 64), (36, 80), (14, 80), (6, 68)]), 'shade', 'b', False), fr([(74, 30), (92, 36), (92, 56, 1), (84, 48)])],
    'back': [L(outline([(14, 80), (-2, 56, 1), (8, 48), (12, 22), (26, 6), (50, 0), (74, 6), (88, 22), (92, 50), (100, 70, 1), (86, 80), (66, 86), (50, 88), (34, 86)])),
             L(outline([(58, 2), (86, 18), (92, 50), (98, 68), (86, 78), (62, 84)]), 'shade', 'b', False)],
}
