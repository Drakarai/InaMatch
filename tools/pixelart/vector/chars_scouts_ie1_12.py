"""Ojeadores de IE1 (scouts-ie1), tanda 12: dibujados a partir de su retrato de Victory Road (no tienen modelo 3D en la
enciclopedia); claves 'scouts-ie1:<id>'. Van con la equipación de Mi club (la pone export.py)."""
from chars import CHARS, L, OUTC, blob, ell, messy, outline, pal, rope, strand  # noqa: F401
from chars_vr_nikogawa import blush, brow_side, brows, crop, ring_glasses  # noqa: F401
from heads import quad  # noqa: F401

K = 'scouts-ie1:'
WHITE = (248, 248, 248, 255)
BROWN = (130, 70, 50, 255)
MOUTH = (110, 50, 40, 255)


def fr(pts, c='mid'):
    """Mechones de delante de la cara (flequillo)."""
    return L(outline(pts), c, 'f')


def nose(y=86, c=None):
    """Nariz marcada (trazo en ángulo)."""
    return [L([(49, y - 6), (47, y), (51, y + 0.6)], c or (150, 90, 60, 255), 'f', False, False, 1.2)]


def bob(view, length=92, top=0, w=4, bang=60, cut=True, c='mid'):
    """Melena corta recta (casco) hasta length, con flequillo recto a la altura bang."""
    if view == 'front':
        out = [L(outline([(10 - w, length, 1), (6 - w, 60), (8 - w, 30), (22, 8 + top), (50, top), (78, 8 + top), (92 + w, 30), (94 + w, 60), (90 + w, length, 1),
                          (82, length - 4), (82, 60), (18, 60), (18, length - 4)]), c),
               L(outline([(60, 4 + top), (84, 16 + top), (94 + w, 44), (92 + w, length - 2), (84, length - 6), (82, 46)]), 'shade', 'b', False)]
        if bang:
            out.append(L(outline([(14, bang + 2, 1), (14, 34), (26, 18 + top), (50, 12 + top), (74, 18 + top), (86, 34), (86, bang + 2, 1)] +
                                 ([(70, bang), (50, bang - 1), (30, bang)] if cut else [])), c, 'f'))
        return out
    if view == 'side':
        return [L(outline([(78, 50), (90, 40), (92, 22), (78, 4 + top), (52, -2 + top), (26, 4 + top), (8, 22), (2 - w, 50), (4, length - 10), (8, length, 1),
                           (30, length - 4), (40, length - 2, 1), (42, 76), (44, 60), (60, 56), (70, 60)]), c),
                L(outline([(3 - w, 46), (30, 46), (42, 60), (40, length - 4), (10, length - 2)]), 'shade', 'b', False)]
    return [L(outline([(10 - w, length, 1), (6 - w, 60), (8 - w, 30), (22, 8 + top), (50, top), (78, 8 + top), (92 + w, 30), (94 + w, 60), (90 + w, length, 1),
                       (70, length + 2), (50, length + 3), (30, length + 2)]), c),
            L(outline([(56, 4 + top), (84, 16 + top), (94 + w, 44), (90 + w, length), (66, length + 2), (60, 40)]), 'shade', 'b', False)]


from chars_bigwaves import white_eyes, side_eye  # noqa: E402


def squint(y=75, sep=14, w=2.2):
    """Ojos apretados en > <."""
    return [L([(50 - sep - 7, y - 3.5), (50 - sep + 4, y), (50 - sep - 7, y + 3.5)], OUTC, 'f', False, False, w),
            L([(50 + sep + 7, y - 3.5), (50 + sep - 4, y), (50 + sep + 7, y + 3.5)], OUTC, 'f', False, False, w)]


def mouth(pts, c=BROWN, w=1.5):
    return L(quad(*pts) if len(pts) == 3 else pts, c, 'f', False, False, w)


def freckles(y=86, dx=24, c=(190, 120, 80, 255)):
    out = []
    for s in (-1, 1):
        for ox, oy in ((-3, 0), (0, 2), (3, 0), (1, -2)):
            out.append(L(ell(50 + s * dx + ox, y + oy, 0.7, 0.7), c, 'f', False))
    return out


# Tighe Windsor: pelo castaño oliva oscuro en pinchos revueltos, con un mechón que baja por el centro de la frente; ojos
# apretados en > <, cejas gruesas, nariz grande y boca torcida
CHARS[K + 'tighe-windsor'] = {
    'body': 'normal', 'pal': pal('#4a4424', '#f8dcb4', shade='#3a3418', deep='#2a2410'),
    'face': {'eyes': 'none', 'mouth': 'none', 'hairline': [(15, 60), (20, 46), (34, 44), (50, 50), (66, 44), (80, 46), (85, 60)]},
    'front': messy('front', amp=11, n=9, seed=3, lo=62)
             + [fr([(34, 30), (44, 40), (52, 64, 1), (56, 42), (66, 34), (50, 26)]), fr([(20, 40), (28, 52, 1), (32, 40)]), fr([(68, 40), (76, 54, 1), (80, 40)])]
             + squint() + brows(64, 'deep', 4.0, 15, 1.2) + nose(87) + [mouth([(40, 96), (50, 93), (60, 96)])],
    'side': messy('side', amp=11, n=9, seed=3)
            + [L([(84, 72), (78, 75), (84, 78)], OUTC, 'f', False, False, 2.2)] + brow_side(64, 'deep', 4.0, 1.0)
            + [L([(87, 80), (92, 87), (86, 88)], (150, 90, 60, 255), 'f', False, False, 1.2), L([(80, 96), (86, 95)], BROWN, 'f', False, False, 1.4)],
    'back': messy('back', amp=11, n=9, seed=3),
}

# Tim Bergoods: pelo verde hierba peinado de lado, con unos pelos de punta arriba y un flequillo largo que le tapa el ojo
# derecho; piel tostada, ojo con pestaña y sonrisa
CHARS[K + 'tim-bergoods'] = {
    'body': 'normal', 'pal': pal('#6aa040', '#f0b878', iris='#2a2420', shade='#548434', deep='#3e6626'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 94},
    'front': crop('front', top=0, side=70, w=4)
             + [L(outline([(44, 6), (52, -16, 1), (56, 0), (64, -10, 1), (64, 6)])),
                fr([(12, 64), (14, 38), (30, 20), (56, 18), (66, 30), (60, 48), (56, 66), (50, 90, 1), (46, 76), (36, 88, 1), (32, 78), (22, 86, 1), (18, 72)]),
                strand([(36, 26), (44, 50), (46, 80)], 'deep', 'f', 1.0), strand([(24, 34), (30, 60)], 'deep', 'f', 1.0)]
             + brows(63, 'deep', 3.0, 14, 0.4)[1:],
    'side': crop('side', top=0, w=4) + [L(outline([(48, 0), (56, -16, 1), (60, 2)])),
                                        fr([(70, 36), (88, 30), (94, 50), (90, 72, 1), (84, 56), (78, 46)])] + brow_side(63, 'deep', 3.0),
    'back': crop('back', top=0, w=4, nape=88) + [L(outline([(44, 6), (52, -14, 1), (58, 4)]))],
}

# Tim Crochett: piel morena, pelo morado revuelto de mechones gruesos; ojos blancos redondos y saltones, cejas pobladas,
# nariz ancha y una bocaza de labios gruesos
CHARS[K + 'tim-crochett'] = {
    'body': 'normal', 'pal': pal('#56487e', '#b07a4c', shade='#463a68', deep='#342a50'),
    'face': {'eyes': 'none', 'mouth': 'none', 'hairline': [(15, 64), (18, 50), (30, 46), (40, 54), (48, 44), (60, 54), (66, 44), (82, 50), (85, 64)]},
    'front': messy('front', amp=7, n=8, seed=8, lo=66) + [L(outline([(46, 6), (52, -14, 1), (58, 4)]))]
             + white_eyes(75, 14, 6.4, 6.2, 2.0) + brows(64, 'deep', 3.6, 14, 1.0)
             + [L([(46, 86), (44, 89), (50, 90), (56, 89), (54, 86)], (110, 66, 40, 255), 'f', False, False, 1.2),
                L(ell(50, 97, 14, 7), (120, 70, 40, 255), 'f', ln=True), L(ell(50, 98, 9, 2.6), (90, 46, 30, 255), 'f', False)],
    'side': messy('side', amp=7, n=8, seed=8) + side_eye(75) + brow_side(64, 'deep', 3.6, 1.0)
            + [L(ell(85, 96, 4.4, 4.4), (120, 70, 40, 255), 'f', ln=True)],
    'back': messy('back', amp=7, n=8, seed=8),
}

# Tim Eisback: pelo verde oscuro corto en pinchos por todo alrededor, con pico en la frente; pecas, ojos oliva, cejas
# gruesas y sonrisa
CHARS[K + 'tim-eisback'] = {
    'body': 'normal', 'pal': pal('#2a6a4a', '#f8c890', iris='#6a6230', shade='#22563c', deep='#18402c'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 94,
             'hairline': [(15, 62), (20, 48), (36, 46), (50, 58), (64, 46), (80, 48), (85, 62)]},
    'front': messy('front', amp=12, n=13, seed=5, rx=44, ry=40, lo=64) + brows(63, 'deep', 3.6, 14, 1.0) + freckles(86),
    'side': messy('side', amp=12, n=13, seed=5, rx=44, ry=40) + brow_side(63, 'deep', 3.6, 0.8),
    'back': messy('back', amp=12, n=13, seed=5, rx=44, ry=40, nape=86),
}

# Tim Mittus: un tupé rubio enorme que sube y se vuelca hacia su derecha, con un mechón que le cae sobre la cara; visera de
# cristal rojo anaranjado, orejas puntiagudas y sonrisa
VISOR = (214, 84, 34, 255)
CHARS[K + 'tim-mittus'] = {
    'body': 'normal', 'pal': pal('#e8c42a', '#f8d0a0', shade='#c8a018', deep='#a07c10'),
    'face': {'eyes': 'none', 'mouth': 'smile', 'mouth_y': 95, 'big_ears': 2, 'hairline': [(14, 66), (16, 46), (40, 36), (70, 40), (84, 52), (86, 64)]},
    'front': [L(outline([(86, 64), (90, 40), (86, 16), (70, -6), (46, -16), (20, -14), (2, -6, 1), (14, 4), (8, 20), (10, 44), (14, 66), (20, 52), (80, 50)])),
              L(outline([(56, -10), (80, 2), (90, 30), (88, 60), (80, 40), (70, 14)]), 'shade', 'b', False),
              strand([(20, -6), (50, -6), (74, 10)], 'deep', 'b', 1.0), strand([(14, 10), (44, 8), (70, 24)], 'deep', 'b', 1.0),
              fr([(28, 30), (46, 34), (52, 50), (48, 80, 1), (40, 56), (30, 44)]),
              L(outline([(20, 68), (46, 70), (54, 70), (80, 68), (78, 79), (56, 80), (50, 75), (44, 80), (22, 79)]), VISOR, 'f', ln=True),
              L([(26, 71), (40, 72)], (250, 170, 110, 255), 'f', False, False, 1.2)],
    'side': [L(outline([(72, 54), (84, 46), (94, 28), (100, 6), (90, -10), (66, -18), (40, -16), (18, -6), (4, 16), (2, 44), (8, 66), (22, 82), (36, 78), (40, 62),
                        (54, 54)])),
             L(outline([(4, 40), (30, 44), (40, 60), (36, 76), (22, 80), (8, 64)]), 'shade', 'b', False),
             strand([(30, -10), (64, -10), (92, 6)], 'deep', 'b', 1.0),
             L(outline([(76, 68), (92, 69), (91, 79), (77, 79)]), VISOR, 'f', ln=True)],
    'back': [L(outline([(16, 78), (10, 46), (14, 18), (30, -8), (56, -16), (80, -8), (92, 16), (92, 46), (84, 78), (50, 88)])),
             L(outline([(58, -12), (84, -2), (94, 30), (88, 74), (64, 84)]), 'shade', 'b', False),
             strand([(28, -4), (50, 30), (52, 80)], 'deep', 'b', 1.0)],
}

# Tim Piece: pelo castaño revuelto de longitud media con un mechón de antena arriba y flequillo de puntas sobre la frente;
# ojos negros redondos, cejas fruncidas y boca torcida
CHARS[K + 'tim-piece'] = {
    'body': 'normal', 'pal': pal('#6a5428', '#f0c088', shade='#56441e', deep='#3e3014'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'hairline': False},
    'front': messy('front', amp=7, n=8, seed=11, lo=66) + [L(quad((48, 4), (46, -12), (56, -18)), 'mid', 'b', False, False, 3.2)]
             + [fr([(14, 62), (16, 40), (30, 26), (50, 22), (70, 26), (84, 40), (86, 62), (80, 54), (74, 62, 1), (68, 50), (58, 58, 1), (52, 48), (42, 60, 1), (38, 50),
                    (28, 60, 1), (22, 52)]),
                strand([(40, 28), (42, 46)], 'deep', 'f', 1.0), strand([(62, 28), (60, 46)], 'deep', 'f', 1.0)],
    'side': messy('side', amp=7, n=8, seed=11) + [fr([(66, 30), (90, 34), (94, 52), (86, 62, 1), (82, 50), (74, 46)])],
    'back': messy('back', amp=7, n=8, seed=11) + [L(quad((48, 4), (46, -12), (56, -18)), 'mid', 'b', False, False, 3.2)],
}

# Tim Toppel (portero): melena corta de casco gris malva, recta hasta la mandíbula con flequillo recto; ojitos negros, cejas
# fruncidas y media sonrisa
CHARS[K + 'tim-toppel'] = {
    'body': 'normal', 'pal': pal('#a08890', '#f8caa8', shade='#866e78', deep='#6a5660'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False, 'ears': False},
    'front': bob('front', 92, top=0, w=4, bang=64) + [strand([(30, 30), (30, 62)], 'deep', 'f', 1.0), strand([(50, 26), (50, 62)], 'deep', 'f', 1.0),
                                                      strand([(70, 30), (70, 62)], 'deep', 'f', 1.0)],
    'side': bob('side', 92, top=0, w=4) + [fr([(70, 30), (90, 36), (92, 64, 1), (82, 60), (76, 50)])],
    'back': bob('back', 92, top=0, w=4) + [strand([(50, 4), (50, 90)], 'deep', 'b', 1.0)],
}

# Tiny Forester: grandullón de cara redonda y mofletuda; pelo verde oscuro corto con un rizo en la coronilla y patillas
# hasta la oreja; ojitos negros, nariz de cerdito y sonrisa
CHARS[K + 'tiny-forester'] = {
    'body': 'corpulento', 'pal': pal('#2a6046', '#f0b878', shade='#204c36', deep='#163828'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 99, 'eye_y': 77, 'eye_sep': 16, 'hairline': (60, 46), 'ear_out': 4,
             'face_front': blob([(12, 50), (50, 38), (88, 50), (96, 78), (88, 102), (66, 112), (50, 114), (34, 112), (12, 102), (4, 78)])},
    'front': crop('front', top=4, side=62, w=6)
             + [L(outline([(40, 8), (46, -4), (60, -6), (64, 6), (56, 14), (52, 4), (48, 12)])),
                L(blob([(43, 86), (50, 83), (57, 86), (56, 92), (50, 93), (44, 92)], 6), (226, 160, 104, 255), 'f', ln=True),
                L(ell(47.5, 88.5, 1.0, 1.4), OUTC, 'f', False), L(ell(52.5, 88.5, 1.0, 1.4), OUTC, 'f', False),
                L(quad((36, 108), (50, 112), (64, 108)), (200, 140, 90, 255), 'f', False, False, 1.2)],
    'side': crop('side', top=4, w=6) + [L(outline([(44, 6), (50, -6), (62, -4), (62, 8)])),
                                        L(blob([(86, 84), (92, 86), (91, 92), (86, 92)], 5), (226, 160, 104, 255), 'f', ln=True)],
    'back': crop('back', top=4, w=6, nape=82) + [L(outline([(40, 8), (46, -4), (60, -6), (64, 6)]))],
}

ORANGE = (236, 120, 40, 255)


def stripes(view, top=-8, lo=58, w=6, bands=(), c='mid'):
    """Gorro de lana grande (cúpula hasta lo) con franjas de color: bands, [(y0, y1, color)] (recortadas a la cúpula)."""
    from chars_orion_arab_no_hi_no_tori_gundan import clipy
    if view == 'front':
        dome = outline([(4 - w, lo + 4), (2 - w, 40), (12 - w, 10), (50, top), (88 + w, 10), (98 + w, 40), (96 + w, lo + 4), (50, lo)])
    elif view == 'side':
        dome = outline([(84, 56), (98, 44), (98, 18), (78, -2 + top * 0.5), (50, top), (20, 0), (2 - w, 26), (-2 - w, 56), (10, 76), (30, 70), (50, 60)])
    else:
        dome = outline([(4 - w, lo + 14), (2 - w, 40), (12 - w, 10), (50, top), (88 + w, 10), (98 + w, 40), (96 + w, lo + 14), (50, lo + 20)])
    out = [L(dome, c)]
    for y0, y1, col in bands:
        band = clipy(dome, y0, y1)
        if band:
            out.append(L(band, col, 'b', False))
    return out


# Toby Patient: piel tostada; pelo gris morado de capas, abultado a los lados y con flequillo de lado; dos rayas naranjas de
# pintura en cada mejilla, cejas fruncidas y sonrisa ancha
CHARS[K + 'toby-patient'] = {
    'body': 'normal', 'pal': pal('#665a80', '#b87a4c', shade='#544a6a', deep='#3e3650'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'none', 'hairline': False},
    'front': crop('front', top=-2, side=74, w=10)
             + [L(outline([(10, 70), (-2, 60, 1), (8, 52)])), L(outline([(90, 70), (102, 60, 1), (92, 52)])),
                fr([(12, 62), (16, 36), (36, 20), (64, 20), (84, 32), (88, 58), (78, 46), (64, 42), (48, 46), (34, 52), (22, 62)]),
                strand([(30, 30), (60, 30), (80, 44)], 'deep', 'f', 1.0)]
             + [L(outline([(24, 81), (28, 81), (29, 92), (25, 92)]), ORANGE, 'f', False), L(outline([(31, 81), (35, 81), (35, 90), (31, 90)]), ORANGE, 'f', False),
                L(outline([(76, 81), (72, 81), (71, 92), (75, 92)]), ORANGE, 'f', False), L(outline([(69, 81), (65, 81), (65, 90), (69, 90)]), ORANGE, 'f', False),
                mouth([(38, 92), (50, 99), (62, 92)], BROWN, 1.6)],
    'side': crop('side', top=-2, w=10) + [fr([(66, 30), (90, 36), (92, 56, 1), (82, 48), (72, 46)]),
                                          L(outline([(74, 82), (78, 82), (78, 92), (74, 92)]), ORANGE, 'f', False)],
    'back': crop('back', top=-2, w=10, nape=84) + [L(outline([(10, 74), (-2, 64, 1), (8, 56)])), L(outline([(90, 74), (102, 64, 1), (92, 56)]))],
}

# Todd Tempole: piel morena; pelo gris crema en tazón con flequillo recto hasta las cejas, y un gorrito de lana de rayas
# encima; ojos verdes, cejas fruncidas y boca abierta de dientes apretados
BEANIE = [(176, 60, 40, 255), (70, 120, 60, 255), (140, 90, 50, 255)]
CHARS[K + 'todd-tempole'] = {
    'body': 'normal', 'pal': pal('#d8d2bc', '#b07a4c', iris='#6a8a3a', shade='#b8b29c', deep='#98927c'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'hairline': False},
    'front': bob('front', 84, top=4, w=2, bang=64) + [strand([(36, 30), (36, 62)], 'deep', 'f', 1.0), strand([(62, 30), (62, 62)], 'deep', 'f', 1.0),
                                                      L(outline([(26, 14), (32, -4), (50, -10), (68, -4), (74, 14), (50, 10)]), BEANIE[0], 'f', ln=True),
                                                      L(quad((30, 4), (50, -2), (70, 4)), BEANIE[1], 'f', False, False, 3.0)],
    'side': bob('side', 84, top=4, w=2) + [L(outline([(24, 14), (34, -4), (54, -8), (72, 0), (78, 14), (50, 10)]), BEANIE[0], 'f', ln=True),
                                           L(quad((28, 4), (54, -2), (76, 6)), BEANIE[1], 'f', False, False, 3.0)],
    'back': bob('back', 84, top=4, w=2) + [L(outline([(26, 14), (32, -4), (50, -10), (68, -4), (74, 14), (50, 10)]), BEANIE[0], 'f', ln=True),
                                           L(quad((30, 4), (50, -2), (70, 4)), BEANIE[1], 'f', False, False, 3.0)],
}

# Tom Felix: chico gato: pelo rubio crema esponjoso con dos orejas puntiagudas marrones, un ojo morado, bigotes, naricita
# naranja y un colmillo
EAR = (110, 80, 70, 255)
CHARS[K + 'tom-felix'] = {
    'body': 'normal', 'pal': pal('#f4e2b0', '#f0b878', iris='#2a2420', shade='#dcc890', deep='#c0a870'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'none', 'hairline': (62, 52)},
    'front': [L(outline([(14, 30), (10, 4, 1), (32, 16)]), EAR), L(outline([(86, 30), (90, 4, 1), (68, 16)]), EAR)]
             + messy('front', amp=6, n=10, seed=21, lo=64)
             + [fr([(16, 60), (18, 40), (34, 30), (50, 28), (66, 30), (82, 40), (84, 60), (76, 52), (68, 60, 1), (62, 50), (54, 58, 1), (48, 50), (40, 58, 1), (34, 50),
                    (26, 58, 1)])]
             + [L(ell(64, 75, 8.5, 8.5) + [ell(64, 75, 8.5, 8.5)[0]], (100, 84, 120, 255), 'f', False, False, 2.4),
                L(ell(50, 87, 2, 1.4), ORANGE, 'f', False), mouth([(42, 92), (50, 95), (58, 92)], OUTC, 1.3),
                L([(54, 93), (55, 97), (57, 93)], WHITE, 'f', False),
                L([(14, 84), (26, 86)], OUTC, 'f', False, False, 1.0), L([(14, 90), (26, 89)], OUTC, 'f', False, False, 1.0),
                L([(86, 84), (74, 86)], OUTC, 'f', False, False, 1.0), L([(86, 90), (74, 89)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(40, 16), (38, -10, 1), (58, 8)]), EAR)] + messy('side', amp=6, n=10, seed=21)
            + [L(ell(88, 87, 1.6, 1.2), ORANGE, 'f', False), L([(76, 86), (90, 88)], OUTC, 'f', False, False, 1.0)],
    'back': [L(outline([(14, 30), (10, 4, 1), (32, 16)]), EAR), L(outline([(86, 30), (90, 4, 1), (68, 16)]), EAR)] + messy('back', amp=6, n=10, seed=21),
}

# Tom Stevenson: pelo castaño con raya en medio, que cae en dos cortinas hasta las sienes y se abre en puntas a los lados;
# cara alargada, cejas negras gruesas, ojitos y sonrisa
CHARS[K + 'tom-stevenson'] = {
    'body': 'normal', 'pal': pal('#7a5a40', '#f0b878', shade='#644830', deep='#4a3422'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': crop('front', top=0, side=70, w=6) + [L(outline([(10, 70), (0, 62, 1), (10, 56)])), L(outline([(90, 70), (100, 62, 1), (90, 56)])),
                                                   fr([(14, 64), (18, 38), (34, 20), (50, 18), (48, 30), (36, 42), (24, 54)]),
                                                   fr([(86, 64), (82, 38), (66, 20), (50, 18), (52, 30), (64, 42), (76, 54)])]
             + brows(64, OUTC, 4.0, 15, 0.8) + nose(87),
    'side': crop('side', top=0, w=6) + [fr([(66, 28), (88, 32), (92, 52, 1), (82, 44), (72, 42)])] + brow_side(64, OUTC, 4.0, 0.6),
    'back': crop('back', top=0, w=6, nape=86) + [L(outline([(10, 74), (0, 66, 1), (10, 60)])), L(outline([(90, 74), (100, 66, 1), (90, 60)]))],
}

# Tony Hacker: pelo caqui en tazón con puntas que le caen sobre los ojos; ojos blancos mirando de reojo y boca seria
CHARS[K + 'tony-hacker'] = {
    'body': 'normal', 'pal': pal('#9a8a48', '#f8d0a4', shade='#807238', deep='#605428'),
    'face': {'eyes': 'none', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': bob('front', 76, top=-2, w=6, bang=0)
             + [fr([(12, 66), (14, 36), (30, 20), (50, 16), (70, 20), (86, 36), (88, 66), (80, 56), (74, 74, 1), (68, 56), (58, 68, 1), (54, 54), (44, 76, 1), (40, 56),
                    (30, 70, 1), (24, 56), (18, 66, 1)]),
                strand([(44, 24), (44, 60)], 'deep', 'f', 1.0), strand([(64, 24), (66, 56)], 'deep', 'f', 1.0)]
             + white_eyes(77, 14, 6.4, 5.4, 2.0)
             + [L(ell(41, 77.5, 2.2, 2.4), OUTC, 'f', False), L(ell(69, 77.5, 2.2, 2.4), OUTC, 'f', False)],
    'side': bob('side', 76, top=-2, w=6) + [fr([(66, 30), (92, 38), (92, 66, 1), (84, 56), (76, 52)])] + side_eye(77),
    'back': bob('back', 76, top=-2, w=6),
}

# Tosh Coach: grandullón con cara de oso: orejas redondas arriba, nariz naranja, un casquete de pelo azul grisáceo con una
# raya clara en la coronilla, ojos blancos fruncidos y boca recta
CHARS[K + 'tosh-coach'] = {
    'body': 'corpulento', 'pal': pal('#4a6a8a', '#f0b878', shade='#3a5672', deep='#2a4058'),
    'face': {'eyes': 'none', 'mouth': 'none', 'ears': False, 'hairline': (48, 40),
             'face_front': blob([(12, 50), (50, 34), (88, 50), (96, 78), (88, 102), (66, 112), (50, 114), (34, 112), (12, 102), (4, 78)])},
    'front': [L(ell(14, 40, 10, 10), 'skin'), L(ell(86, 40, 10, 10), 'skin'), L(ell(14, 40, 5, 5), 'skin_d', 'b', False), L(ell(86, 40, 5, 5), 'skin_d', 'b', False),
              L(outline([(22, 44), (26, 24), (40, 14), (60, 14), (74, 24), (78, 44), (50, 38)])),
              L(outline([(44, 15), (56, 15), (54, 36), (46, 36)]), (120, 150, 180, 255), 'b', False)]
             + white_eyes(76, 15, 6, 4.4, 1.6)
             + [L([(26, 68), (40, 72)], OUTC, 'f', False, False, 2.6), L([(74, 68), (60, 72)], OUTC, 'f', False, False, 2.6),
                L(blob([(44, 84), (56, 84), (54, 90), (46, 90)], 6), ORANGE, 'f', ln=True), mouth([(38, 100), (62, 100)], OUTC, 1.6)],
    'side': [L(ell(40, 36, 10, 10), 'skin'), L(outline([(40, 28), (52, 14), (72, 16), (82, 30), (60, 36)])),
             L(blob([(86, 82), (94, 84), (92, 90), (86, 90)], 5), ORANGE, 'f', ln=True)] + side_eye(76),
    'back': [L(ell(14, 40, 10, 10), 'skin'), L(ell(86, 40, 10, 10), 'skin'), L(outline([(22, 44), (26, 24), (40, 14), (60, 14), (74, 24), (78, 44), (50, 40)]))],
}

# Travis McClean: piel tostada; pelo granate muy oscuro liso hasta la mandíbula, con flequillo recto partido en el centro;
# ojos afilados, cejas fruncidas y media sonrisa
CHARS[K + 'travis-mcclean'] = {
    'body': 'normal', 'pal': pal('#4c2a3a', '#c88c5e', shade='#3c202e', deep='#2a1620'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False, 'ears': True},
    'front': bob('front', 96, top=0, w=0, bang=0)
             + [fr([(14, 60), (16, 34), (28, 18), (50, 14), (72, 18), (84, 34), (86, 60), (70, 58), (54, 58), (50, 66, 1), (46, 58), (30, 58)]),
                strand([(30, 26), (30, 56)], 'deep', 'f', 1.0), strand([(70, 26), (70, 56)], 'deep', 'f', 1.0)],
    'side': bob('side', 96, top=0, w=0) + [fr([(70, 30), (90, 36), (92, 60, 1), (80, 58)])],
    'back': bob('back', 96, top=0, w=0) + [strand([(50, 4), (50, 94)], 'deep', 'b', 1.0)],
}

# Trey Bonzer-Cultivator: un gorro de lana enorme a rayas crema, verde azulado y gris que le tapa todo el pelo; pintura verde
# y naranja alrededor de los ojos, nariz naranja y boca seria
GREEN = (60, 120, 60, 255)
CHARS[K + 'trey-bonzer-cultivator'] = {
    'body': 'normal', 'pal': pal('#efe0b8', '#c89060', shade='#d4c49a', deep='#b8a880'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 97, 'hairline': (58, 54), 'ears': False},
    'front': stripes('front', -10, 60, 8, [(-2, 8, (74, 140, 150, 255)), (18, 28, (96, 96, 104, 255)), (38, 48, (74, 140, 150, 255))])
             + [L(quad((24, 74), (34, 64), (46, 72)), GREEN, 'f', False, False, 2.4), L(quad((76, 74), (66, 64), (54, 72)), GREEN, 'f', False, False, 2.4),
                L([(24, 84), (32, 86)], ORANGE, 'f', False, False, 2.0), L([(76, 84), (68, 86)], ORANGE, 'f', False, False, 2.0),
                L(blob([(46, 84), (54, 84), (53, 89), (47, 89)], 5), ORANGE, 'f', ln=True)],
    'side': stripes('side', -10, 60, 8, [(-2, 8, (74, 140, 150, 255)), (18, 28, (96, 96, 104, 255)), (38, 48, (74, 140, 150, 255))]),
    'back': stripes('back', -10, 60, 8, [(-2, 8, (74, 140, 150, 255)), (18, 28, (96, 96, 104, 255)), (38, 48, (74, 140, 150, 255)), (58, 68, (96, 96, 104, 255))]),
}


def hexglasses(view, y=77, frame=(70, 120, 90, 255), lens=(200, 236, 190, 255), sep=14):
    """Gafas de montura gruesa casi cuadrada (octogonal) con cristal de color."""
    if view == 'front':
        out = []
        for cx in (50 - sep, 50 + sep):
            pts = [(cx - 10, y - 3), (cx - 7, y - 7), (cx + 7, y - 7), (cx + 10, y - 3), (cx + 10, y + 3), (cx + 7, y + 7), (cx - 7, y + 7), (cx - 10, y + 3)]
            out.append(L(pts, lens, 'f', False))
            out.append(L(pts + [pts[0]], frame, 'f', False, False, 2.4))
        out.append(L([(50 - sep + 10, y - 2), (50 + sep - 10, y - 2)], frame, 'f', False, False, 2.0))
        return out
    if view == 'side':
        return [L([(76, y - 7), (88, y - 7), (88, y + 7), (78, y + 7)], lens, 'f', False),
                L([(76, y - 7), (88, y - 7), (88, y + 7), (78, y + 7), (76, y - 7)], frame, 'f', False, False, 2.2),
                L([(76, y - 3), (50, y - 5)], frame, 'f', False, False, 2.0)]
    return []


# Trey Dalbum: melena ondulada granate oscuro hasta la mandíbula con raya en medio; ojos verdes grandes, pecas y sonrisa
CHARS[K + 'trey-dalbum'] = {
    'body': 'normal', 'pal': pal('#6a3a44', '#f0b878', iris='#3a9a5a', shade='#562e36', deep='#3e2028'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': [(14, 70), (16, 50), (30, 40), (48, 34), (52, 34), (70, 40), (84, 50), (86, 70)]},
    'front': [L(outline([(8, 96, 1), (-4, 84), (4, 74), (-4, 60), (4, 44), (0, 30), (14, 12), (36, 0), (50, 2), (64, 0), (86, 12), (100, 30), (96, 44), (104, 60), (96, 74),
                         (104, 84), (92, 96, 1), (82, 90), (84, 64), (16, 64), (18, 90)])),
              L(outline([(56, 4), (86, 14), (98, 32), (96, 60), (100, 84), (90, 94), (82, 60)]), 'shade', 'b', False),
              strand([(50, 4), (48, 34)], 'deep', 'b', 1.2), strand([(30, 10), (14, 40)], 'deep', 'b', 1.0), strand([(70, 10), (86, 40)], 'deep', 'b', 1.0)]
             + freckles(87),
    'side': [L(outline([(76, 52), (88, 40), (90, 20), (74, 2), (46, -2), (20, 6), (2, 30), (-4, 60), (2, 80), (-2, 96, 1), (14, 92), (30, 98, 1), (40, 84), (44, 64),
                        (58, 58), (68, 58)])),
             L(outline([(0, 50), (30, 50), (42, 64), (38, 84), (14, 92)]), 'shade', 'b', False)],
    'back': [L(outline([(6, 96, 1), (-4, 84), (4, 74), (-4, 60), (4, 44), (0, 30), (14, 12), (36, 0), (64, 0), (86, 12), (100, 30), (96, 44), (104, 60), (96, 74),
                        (104, 84), (94, 96, 1), (72, 92), (50, 98, 1), (28, 92)])),
             L(outline([(56, 4), (86, 14), (98, 32), (96, 60), (100, 84), (92, 96), (70, 92), (60, 40)]), 'shade', 'b', False),
             strand([(50, 4), (50, 90)], 'deep', 'b', 1.0)],
}

# Trey Hugger (portero): grandullón de mandíbula ancha; pelo rojo liso de mechones largos que le caen por la frente hasta los
# ojos y se abren en puntas a los lados; ojos grises y sonrisa de lado
CHARS[K + 'trey-hugger'] = {
    'body': 'corpulento', 'pal': pal('#c23c1c', '#f0b878', iris='#8a8a9a', shade='#a02e14', deep='#7a220e'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False,
             'face_front': blob([(14, 52), (50, 40), (86, 52), (90, 78), (84, 100), (66, 110), (50, 112), (34, 110), (16, 100), (10, 78)])},
    'front': crop('front', top=-4, side=72, w=6) + [L(outline([(10, 72), (-2, 66, 1), (10, 58)])), L(outline([(90, 72), (102, 66, 1), (90, 58)]))]
             + [fr([(12, 64), (14, 36), (30, 16), (50, 12), (70, 16), (86, 36), (88, 64), (80, 56), (76, 72, 1), (70, 58), (62, 70, 1), (58, 56), (50, 74, 1), (46, 56),
                    (38, 70, 1), (32, 56), (24, 68, 1), (20, 58)]),
                strand([(40, 20), (44, 56)], 'deep', 'f', 1.0), strand([(60, 20), (60, 56)], 'deep', 'f', 1.0), strand([(28, 26), (28, 56)], 'deep', 'f', 1.0)],
    'side': crop('side', top=-4, w=6) + [fr([(66, 28), (92, 34), (94, 62, 1), (84, 52), (76, 50)])],
    'back': crop('back', top=-4, w=6, nape=88) + [L(outline([(10, 76), (-2, 70, 1), (10, 62)])), L(outline([(90, 76), (102, 70, 1), (90, 62)]))],
}

# Trey Spotter: pelo azul marino corto y revuelto de puntas; gafas verdes de montura gruesa casi cuadrada con cristal verde
# claro y sonrisa
CHARS[K + 'trey-spotter'] = {
    'body': 'normal', 'pal': pal('#2c4a6c', '#fcd8b0', shade='#223a56', deep='#182a40'),
    'face': {'eyes': 'dot', 'brows': True, 'mouth': 'smile', 'mouth_y': 95, 'hairline': [(15, 62), (18, 48), (30, 44), (44, 50), (56, 44), (70, 48), (82, 46), (85, 62)]},
    'front': messy('front', amp=9, n=11, seed=31, lo=64) + [L(outline([(46, 4), (54, -16, 1), (58, 2)]))] + hexglasses('front', 77),
    'side': messy('side', amp=9, n=11, seed=31) + hexglasses('side', 77),
    'back': messy('back', amp=9, n=11, seed=31),
}

# Troy Carr: piel tostada; pelo naranja en pinchos altos echados hacia arriba y a su izquierda; cejas negras gruesas y
# fruncidas, ojitos y sonrisa de dientes
CHARS[K + 'troy-carr'] = {
    'body': 'normal', 'pal': pal('#e8782a', '#b87a4c', shade='#c86018', deep='#a04a10'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'grin', 'mouth_y': 95, 'hairline': [(15, 62), (18, 46), (40, 40), (60, 42), (82, 46), (85, 62)]},
    'front': [L(outline([(16, 64), (12, 40), (4, 26, 1), (16, 22), (12, 0, 1), (28, 10), (32, -18, 1), (46, 2), (60, -24, 1), (64, 0), (84, -20, 1), (80, 8), (100, 4, 1),
                         (88, 24), (96, 36, 1), (86, 40), (84, 64), (80, 46), (20, 46)])),
              L(outline([(58, -14), (64, 2), (82, -14), (78, 10), (96, 8), (86, 26), (92, 36), (84, 42), (74, 20)]), 'shade', 'b', False)]
             + brows(64, OUTC, 4.4, 15, 1.6),
    'side': [L(outline([(70, 52), (82, 46), (94, 36, 1), (88, 26), (104, 12, 1), (88, 6), (98, -16, 1), (74, -8), (72, -26, 1), (56, -10), (40, -20, 1), (32, -2), (12, 4, 1),
                        (14, 20), (2, 34), (4, 56), (14, 76), (28, 86), (36, 80), (38, 64), (46, 56), (58, 54)])),
             L(outline([(4, 36), (30, 40), (42, 56), (36, 64), (36, 80), (28, 86), (14, 76)]), 'shade', 'b', False)] + brow_side(64, OUTC, 4.4, 1.2),
    'back': [L(outline([(18, 80), (12, 50), (4, 30, 1), (14, 24), (12, 0, 1), (28, 10), (34, -18, 1), (48, 2), (62, -24, 1), (66, 0), (86, -18, 1), (82, 8), (100, 6, 1),
                        (90, 26), (96, 38, 1), (88, 50), (82, 80), (66, 90), (50, 92), (34, 90)])),
             L(outline([(60, -14), (66, 2), (84, -14), (80, 10), (98, 10), (88, 28), (94, 38), (86, 52), (82, 80), (66, 90), (64, 40)]), 'shade', 'b', False)],
}

# Troy Glodight: una cresta roja de pinchos en llamarada encima y los lados rapados verde grisáceo con pinchitos; ojos
# blancos fruncidos y media sonrisa
SIDES = (92, 120, 110, 255)
CHARS[K + 'troy-glodight'] = {
    'body': 'normal', 'pal': pal('#c03418', '#f0b878', shade='#9a2610', deep='#741c0a'),
    'face': {'eyes': 'none', 'mouth': 'smile', 'mouth_y': 95, 'hairline': (60, 48)},
    'front': [L(outline([(14, 72), (2, 70, 1), (12, 62), (2, 52, 1), (12, 46), (14, 30), (30, 18), (50, 14), (70, 18), (86, 30), (88, 46), (98, 52, 1), (88, 62),
                         (98, 70, 1), (86, 72), (84, 56), (16, 56)]), SIDES),
              L(outline([(30, 30), (16, 6, 1), (40, 18), (44, -12, 1), (52, 12), (58, -18, 1), (62, 14), (84, 4, 1), (70, 30), (50, 34)])),
              L(outline([(52, 12), (58, -18), (62, 14), (84, 4), (70, 30), (56, 30)]), 'shade', 'b', False)]
             + white_eyes(76, 14, 6.4, 4.6, 1.6) + [L([(26, 68), (42, 73)], OUTC, 'f', False, False, 2.6), L([(74, 68), (58, 73)], OUTC, 'f', False, False, 2.6)],
    'side': [L(outline([(64, 52), (76, 44), (86, 30), (70, 16), (44, 12), (20, 20), (6, 40), (-4, 50, 1), (6, 56), (-2, 68, 1), (10, 72), (22, 86), (36, 80), (40, 62),
                        (52, 56)]), SIDES),
             L(outline([(70, 28), (84, 8, 1), (66, 14), (60, -16, 1), (48, 10), (34, -10, 1), (34, 12), (16, 6, 1), (24, 28), (50, 32)]))] + side_eye(76),
    'back': [L(outline([(16, 80), (4, 74, 1), (12, 64), (2, 54, 1), (12, 46), (14, 30), (30, 18), (50, 14), (70, 18), (86, 30), (88, 46), (98, 54, 1), (88, 64),
                        (96, 74, 1), (84, 80), (50, 88)]), SIDES),
             L(outline([(30, 32), (16, 6, 1), (40, 18), (44, -12, 1), (52, 12), (58, -18, 1), (62, 14), (84, 4, 1), (70, 32), (50, 40)]))],
}

# Troy Trucker: grandullón adulto de cara ancha; pelo rosa malva peinado de lado con la raya a su derecha, que se abre en
# puntas sobre las orejas; ojos blancos de párpado caído, pupilas pequeñas y boca torcida
CHARS[K + 'troy-trucker'] = {
    'body': 'corpulento', 'pal': pal('#c49494', '#f0b878', shade='#a87a7a', deep='#8a6060'),
    'face': {'eyes': 'none', 'mouth': 'none', 'hairline': [(13, 66), (16, 46), (30, 34), (60, 32), (80, 40), (86, 54), (87, 66)],
             'face_front': blob([(13, 52), (50, 38), (87, 52), (92, 80), (86, 102), (66, 112), (50, 114), (34, 112), (14, 102), (8, 80)])},
    'front': crop('front', top=-2, side=70, w=6) + [L(outline([(10, 72), (-4, 64, 1), (10, 56)])), L(outline([(90, 72), (104, 64, 1), (90, 56)])),
                                                    fr([(26, 24), (14, 40), (12, 58), (20, 44), (34, 30), (60, 24), (84, 30), (70, 18), (46, 14)]),
                                                    strand([(34, 18), (60, 26), (80, 36)], 'deep', 'f', 1.0)]
             + white_eyes(77, 14, 6.4, 4.8, 1.6, lid=1.2) + [mouth([(36, 99), (44, 97), (54, 99), (64, 96)], BROWN, 1.6)] + nose(88),
    'side': crop('side', top=-2, w=6) + side_eye(77, lid=1.2),
    'back': crop('back', top=-2, w=6, nape=86) + [L(outline([(10, 76), (-4, 68, 1), (10, 60)])), L(outline([(90, 76), (104, 68, 1), (90, 60)]))],
}

# Turner Fortune: pelo verde oliva oscuro liso, con flequillo en puntas hasta las cejas y los lados tapando media oreja;
# cara alargada, ojos verdosos, nariz larga y sonrisa
CHARS[K + 'turner-fortune'] = {
    'body': 'normal', 'pal': pal('#4a4a22', '#f8d4a4', iris='#6a7040', shade='#3a3a18', deep='#2a2a10'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': crop('front', top=-2, side=74, w=6) + [L(outline([(10, 74), (2, 70, 1), (10, 62)])), L(outline([(90, 74), (98, 70, 1), (90, 62)]))]
             + [fr([(12, 64), (14, 36), (30, 18), (50, 14), (70, 18), (86, 36), (88, 64), (82, 56), (78, 64, 1), (70, 54), (62, 64, 1), (56, 52), (46, 66, 1), (42, 54),
                    (32, 64, 1), (26, 54), (20, 64, 1)])] + nose(88),
    'side': crop('side', top=-2, w=6) + [fr([(66, 28), (90, 34), (92, 58, 1), (82, 50), (74, 48)])],
    'back': crop('back', top=-2, w=6, nape=88),
}

# Ty Priter: pelo rubio dorado revuelto con mechones de punta arriba y un flequillo de lado; gafas redondas marrones, ojos
# negros grandes y sonrisa
CHARS[K + 'ty-priter'] = {
    'body': 'normal', 'pal': pal('#e8c430', '#f8d0a4', shade='#c8a018', deep='#9a7a10'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': messy('front', amp=6, n=11, seed=41, lo=66) + [L(outline([(42, 4), (46, -18, 1), (54, 0), (60, -14, 1), (62, 4)]))]
             + [fr([(14, 66), (16, 40), (34, 24), (60, 22), (80, 30), (86, 50), (70, 42), (54, 46), (40, 56), (30, 68, 1), (26, 56), (20, 66)]),
                strand([(36, 30), (60, 32)], 'deep', 'f', 1.0)]
             + ring_glasses('front', 77, (120, 70, 30, 255), 2.2, 9.5, 8, 14),
    'side': messy('side', amp=6, n=11, seed=41) + ring_glasses('side', 77, (120, 70, 30, 255), 2.2, 5, 8),
    'back': messy('back', amp=6, n=11, seed=41) + [L(outline([(42, 4), (46, -18, 1), (54, 0), (60, -14, 1), (62, 4)]))],
}

# Tyche Winham (portero): melena ondulada hasta la mandíbula partida en dos colores: azul marino a su derecha y malva a su
# izquierda; cara redonda, ojos negros afilados y media sonrisa
NAVY = (44, 72, 106, 255)
CHARS[K + 'tyche-winham'] = {
    'body': 'normal', 'pal': pal('#c4a4ac', '#f0b070', shade='#a8888e', deep='#8a6a72'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': [(14, 76), (16, 50), (34, 38), (50, 34), (66, 38), (84, 50), (86, 76)],
             'face_front': blob([(14, 52), (50, 40), (86, 52), (90, 78), (84, 100), (66, 110), (50, 112), (34, 110), (16, 100), (10, 78)])},
    'front': [L(outline([(8, 100, 1), (-2, 86), (4, 74), (-4, 58), (4, 40), (6, 24), (22, 6), (50, 0), (78, 6), (94, 24), (96, 40), (104, 58), (96, 74), (102, 86),
                         (92, 100, 1), (84, 92), (84, 64), (16, 64), (16, 92)])),
              L(outline([(8, 100, 1), (-2, 86), (4, 74), (-4, 58), (4, 40), (6, 24), (22, 6), (50, 0), (50, 40), (16, 64), (16, 92)]), NAVY, 'b', False),
              L(outline([(64, 6), (86, 16), (96, 40), (100, 70), (92, 96), (84, 70)]), 'shade', 'b', False)],
    'side': [L(outline([(76, 52), (88, 40), (90, 20), (74, 2), (46, -2), (20, 6), (2, 30), (-4, 60), (2, 84), (-2, 100, 1), (16, 94), (30, 100, 1), (40, 86), (44, 66),
                        (58, 58), (68, 58)])),
             L(outline([(0, 50), (30, 50), (42, 66), (38, 86), (16, 94)]), 'shade', 'b', False)],
    'back': [L(outline([(6, 100, 1), (-2, 86), (4, 74), (-4, 58), (4, 40), (6, 24), (22, 6), (50, 0), (78, 6), (94, 24), (96, 40), (104, 58), (96, 74), (102, 86),
                        (94, 100, 1), (72, 96), (50, 102, 1), (28, 96)])),
             L(outline([(50, 0), (78, 6), (94, 24), (96, 40), (104, 58), (96, 74), (102, 86), (94, 100), (72, 96), (50, 102)]), NAVY, 'b', False)],
}

from chars_bigwaves import bald  # noqa: E402
from chars_vr_keizen_arashiyama import cloud  # noqa: E402


def spiky_fringe(y=64, x0=14, x1=86, n=5, top=24, jag=10):
    """Flequillo de puntas hasta la altura y."""
    pts = [(x0 - 2, y), (x0, top + 14), (x0 + 16, top), (50, top - 4), (x1 - 16, top), (x1, top + 14), (x1 + 2, y)]
    for i in range(n):
        x = x1 - (i + 0.5) * (x1 - x0) / n
        pts += [(x + (x1 - x0) / n * 0.4, y - jag), (x, y + 2, 1)]
    return fr(pts)


# Tyson Moodey (portero): pelo gris morado revuelto de puntas con una antena arriba y flequillo de picos; ojos afilados,
# cejas fruncidas y boca seria
CHARS[K + 'tyson-moodey'] = {
    'body': 'normal', 'pal': pal('#6a6082', '#f8c890', shade='#58506c', deep='#423c52'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'hairline': False},
    'front': messy('front', amp=9, n=9, seed=51, lo=66) + [L(outline([(44, 4), (50, -20, 1), (56, 2)]))] + [spiky_fringe(66, n=4)],
    'side': messy('side', amp=9, n=9, seed=51) + [L(outline([(44, 2), (52, -20, 1), (58, 2)])), fr([(66, 30), (92, 36), (94, 60, 1), (84, 52), (76, 50)])],
    'back': messy('back', amp=9, n=9, seed=51) + [L(outline([(44, 4), (50, -20, 1), (56, 2)]))],
}

# Urson Brown (portero): grandullón de cara enorme y redonda; pelo verde azulado de puntas arriba con mechones sobre la
# frente; cejas gruesas del mismo color, ojitos, nariz naranja redonda y sonrisa
CHARS[K + 'urson-brown'] = {
    'body': 'corpulento', 'pal': pal('#5a9aa8', '#f8b868', shade='#468290', deep='#346470'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'smile', 'mouth_y': 100, 'eye_y': 78, 'eye_sep': 16, 'hairline': False,
             'face_front': blob([(10, 48), (50, 36), (90, 48), (96, 78), (90, 104), (66, 114), (50, 116), (34, 114), (10, 104), (4, 78)])},
    'front': messy('front', amp=10, n=11, seed=61, rx=48, ry=36, cy=38, lo=58)
             + [spiky_fringe(62, 10, 90, 6, 26, 12)] + brows(66, 'mid', 4.4, 16, -0.6)
             + [L(ell(50, 89, 7, 5.4), ORANGE, 'f', ln=True), L(ell(48, 87.5, 2, 1.2), (250, 170, 110, 255), 'f', False)],
    'side': messy('side', amp=10, n=11, seed=61, rx=48, ry=36, cy=38) + [fr([(66, 30), (94, 36), (96, 56, 1), (86, 50), (76, 48)])]
            + [L(ell(91, 89, 4, 5), ORANGE, 'f', ln=True)],
    'back': messy('back', amp=10, n=11, seed=61, rx=48, ry=36, cy=38, nape=80),
}

# Vance Bookings (portero): pelo gris caqui revuelto de puntas, con mechones que le caen por la frente; ojos cerrados de
# contento y sonrisa
CHARS[K + 'vance-bookings'] = {
    'body': 'normal', 'pal': pal('#8a8468', '#f8c890', shade='#726c54', deep='#58523e'),
    'face': {'eyes': 'none', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': messy('front', amp=10, n=10, seed=71, lo=66)
             + [fr([(14, 64), (16, 40), (30, 26), (50, 22), (70, 26), (84, 40), (86, 62), (78, 52), (72, 60, 1), (64, 48), (56, 64, 1), (52, 46), (44, 60, 1), (40, 48),
                    (30, 60, 1), (24, 50)])]
             + [L(quad((28, 76), (36, 71), (44, 76)), OUTC, 'f', False, False, 2.2), L(quad((56, 76), (64, 71), (72, 76)), OUTC, 'f', False, False, 2.2),
                L([(24, 71), (28, 74)], OUTC, 'f', False, False, 1.2), L([(76, 71), (72, 74)], OUTC, 'f', False, False, 1.2)],
    'side': messy('side', amp=10, n=10, seed=71) + [fr([(66, 30), (92, 36), (94, 58, 1), (84, 50), (76, 48)]),
                                                    L(quad((76, 76), (81, 72), (86, 76)), OUTC, 'f', False, False, 2.2)],
    'back': messy('back', amp=10, n=10, seed=71),
}

# Vaughn DeVille: pelo rojo salmón peinado hacia atrás en un tupé que se vuelca a su izquierda, con los lados cortos y las
# orejas al aire; ojos blancos redondos de pupila pequeña, cejas gruesas y sonrisa
CHARS[K + 'vaughn-deville'] = {
    'body': 'normal', 'pal': pal('#c46262', '#f0b070', shade='#a44c4c', deep='#843838'),
    'face': {'eyes': 'none', 'mouth': 'smile', 'mouth_y': 96, 'hairline': [(16, 64), (18, 46), (34, 40), (60, 38), (80, 44), (84, 64)]},
    'front': [L(outline([(16, 64), (12, 40), (16, 20), (30, 4), (54, -4), (78, 2), (94, 14), (98, 30, 1), (88, 30), (88, 46), (84, 64), (80, 48), (20, 48)])),
              L(outline([(58, 0), (80, 4), (96, 16), (96, 28), (86, 30), (84, 50), (76, 30)]), 'shade', 'b', False),
              strand([(24, 20), (50, 8), (80, 12)], 'deep', 'b', 1.0), strand([(20, 32), (50, 20), (86, 24)], 'deep', 'b', 1.0)]
             + white_eyes(77, 14, 6.6, 6.2, 1.8) + brows(65, 'shade', 3.6, 14, 1.0) + nose(88),
    'side': [L(outline([(70, 50), (84, 44), (94, 30), (100, 16, 1), (88, 14), (80, 0), (56, -6), (30, -2), (12, 12), (4, 36), (8, 60), (20, 76), (34, 72), (40, 60),
                        (52, 52)])),
             L(outline([(4, 36), (30, 42), (40, 58), (34, 70), (20, 74), (8, 58)]), 'shade', 'b', False),
             strand([(28, 4), (60, 0), (90, 16)], 'deep', 'b', 1.0)] + side_eye(77) + brow_side(65, 'shade', 3.6, 0.8),
    'back': [L(outline([(16, 76), (10, 46), (14, 20), (30, 2), (54, -4), (78, 2), (92, 20), (92, 46), (84, 76), (50, 84)])),
             L(outline([(58, 0), (82, 8), (94, 30), (88, 72), (64, 82)]), 'shade', 'b', False)],
}

# Vern Ironfist: adulto; pelo gris malva fino peinado hacia atrás con entradas y un mechón en el centro, y las puntas
# levantadas por detrás de las orejas; ojos malva, cejas fruncidas, sonrisa y barbilla marcada
CHARS[K + 'vern-ironfist'] = {
    'body': 'normal', 'pal': pal('#a08898', '#f0b878', iris='#8a6a7a', shade='#867080', deep='#6a5464'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': [(17, 62), (20, 46), (30, 36), (40, 40), (48, 30), (56, 42), (66, 36), (80, 44), (83, 62)]},
    'front': crop('front', top=0, side=68, w=2)
             + [L(outline([(12, 74), (2, 76, 1), (10, 64)])), L(outline([(88, 74), (98, 76, 1), (90, 64)])),
                strand([(36, 12), (40, 34)], 'deep', 'b', 1.0), strand([(62, 12), (60, 34)], 'deep', 'b', 1.0),
                L(quad((48, 104), (50, 108), (52, 104)), (180, 120, 80, 255), 'f', False, False, 1.0)] + nose(87),
    'side': crop('side', top=0, w=2) + [L(outline([(24, 86), (16, 96, 1), (36, 86)]))],
    'back': crop('back', top=0, w=2, nape=84) + [L(outline([(24, 84), (14, 94, 1), (36, 86)])), L(outline([(76, 84), (86, 94, 1), (64, 86)]))],
}

# Victor Grand: vampiro de piel gris pálida y orejas puntiagudas; pelo castaño oliva oscuro con raya en medio, pegado y con
# las puntas abiertas a la altura de la mandíbula; ojos afilados, nariz larga y colmillos
CHARS[K + 'victor-grand'] = {
    'body': 'delgado', 'pal': pal('#4a3c22', '#e4dccc', iris='#4a4a50', shade='#3a2e18', deep='#2a2010'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'big_ears': 2, 'hairline': [(16, 66), (18, 46), (32, 36), (48, 32), (52, 32), (68, 36), (82, 46), (84, 66)]},
    'front': [L(outline([(16, 88), (2, 94, 1), (8, 80), (10, 50), (16, 22), (34, 6), (50, 4), (66, 6), (84, 22), (90, 50), (92, 80), (98, 94, 1), (84, 88), (82, 60),
                         (18, 60)])),
              L(outline([(56, 6), (82, 20), (90, 50), (90, 82), (84, 84), (80, 50)]), 'shade', 'b', False),
              strand([(50, 6), (49, 30)], 'deep', 'b', 1.2)] + nose(88)
             + [mouth([(40, 96), (50, 98), (60, 95)], OUTC, 1.3), L([(44, 96.5), (45.5, 100), (47, 97)], WHITE, 'f', False), L([(53, 97), (54.5, 100.5), (56, 96.5)], WHITE, 'f', False)],
    'side': [L(outline([(76, 50), (88, 40), (90, 22), (74, 4), (48, 0), (24, 6), (8, 26), (2, 56), (6, 80), (0, 96, 1), (16, 88), (30, 84), (40, 70), (46, 58),
                        (60, 54)])),
             L(outline([(4, 44), (30, 48), (42, 60), (36, 78), (16, 88)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 88), (2, 94, 1), (8, 80), (10, 50), (16, 22), (34, 6), (50, 4), (66, 6), (84, 22), (90, 50), (92, 80), (98, 94, 1), (84, 88), (50, 92)])),
             L(outline([(56, 6), (82, 20), (90, 50), (90, 82), (84, 88), (62, 90)]), 'shade', 'b', False)],
}

# Victor Mancey: pelo verde oliva en un cepillo alto de puntas hacia arriba, con los lados rectos hasta las orejas; cara
# alargada, ojos afilados pequeños, nariz grande y boca seria
CHARS[K + 'victor-mancey'] = {
    'body': 'normal', 'pal': pal('#6a7030', '#f0b878', shade='#565c24', deep='#40441a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 97, 'hairline': [(16, 66), (18, 46), (50, 42), (82, 46), (84, 66)]},
    'front': [L(outline([(16, 68), (12, 40), (8, 8, 1), (22, 14), (24, -14, 1), (36, 6), (44, -22, 1), (52, 4), (62, -20, 1), (66, 6), (80, -10, 1), (78, 14), (94, 6, 1),
                         (88, 40), (84, 68), (80, 48), (20, 48)])),
              L(outline([(60, -14), (66, 6), (78, -6), (78, 16), (92, 10), (88, 40), (84, 64), (78, 40)]), 'shade', 'b', False)] + nose(88),
    'side': [L(outline([(72, 52), (84, 46), (90, 30), (98, 6, 1), (84, 12), (82, -14, 1), (68, 4), (62, -22, 1), (50, 2), (40, -18, 1), (32, 4), (14, -2, 1), (14, 18),
                        (4, 34), (6, 58), (16, 76), (28, 82), (36, 76), (38, 62), (46, 56), (60, 54)])),
             L(outline([(6, 36), (30, 40), (42, 56), (36, 62), (36, 76), (28, 82), (16, 76)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 80), (12, 44), (8, 8, 1), (22, 14), (24, -14, 1), (36, 6), (44, -22, 1), (52, 4), (62, -20, 1), (66, 6), (80, -10, 1), (78, 14), (94, 6, 1),
                        (88, 44), (84, 80), (50, 88)])),
             L(outline([(60, -14), (66, 6), (80, -6), (78, 16), (92, 10), (88, 44), (84, 78), (64, 86)]), 'shade', 'b', False)],
}

# Vin Fleetwood: pelo azul verdoso de puntas que caen por los lados, con un mechón blanco crema enorme rizado en la coronilla
# como una ola; ojitos redondos, cejas fruncidas y boca seria
CREAM = (234, 224, 210, 255)
CHARS[K + 'vin-fleetwood'] = {
    'body': 'normal', 'pal': pal('#4c8098', '#f8d0a8', shade='#3c6a80', deep='#2c5062'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'hairline': False},
    'front': messy('front', amp=10, n=9, seed=81, lo=70, sweep=-0.2)
             + [spiky_fringe(64, n=5), L(outline([(44, 14), (40, -6), (52, -22), (66, -18, 1), (56, -10), (54, 6), (58, 22)]), CREAM, 'b', ln=True)],
    'side': messy('side', amp=10, n=9, seed=81) + [fr([(66, 30), (92, 36), (94, 60, 1), (84, 52), (76, 50)]),
                                                   L(outline([(44, 14), (42, -6), (56, -22), (70, -18, 1), (60, -10), (58, 6), (60, 18)]), CREAM, 'b', ln=True)],
    'back': messy('back', amp=10, n=9, seed=81) + [L(outline([(44, 14), (40, -6), (52, -22), (66, -18, 1), (56, -10), (54, 6), (58, 22)]), CREAM, 'b', ln=True)],
}

# Vin Spinner: pelo verde corto con dos picos a los lados como cuernos y una cresta morada rojiza en el centro que baja en
# pico a la frente; cejas verdes gruesas, ojos blancos saltones y sonrisa ancha
MOHAWK = (154, 96, 96, 255)
CHARS[K + 'vin-spinner'] = {
    'body': 'normal', 'pal': pal('#6a9a40', '#f0b878', shade='#567e32', deep='#406024'),
    'face': {'eyes': 'none', 'mouth': 'none', 'hairline': [(16, 62), (18, 48), (36, 44), (50, 56), (64, 44), (82, 48), (84, 62)]},
    'front': crop('front', top=4, side=62, w=2) + [L(outline([(16, 30), (12, 6, 1), (30, 18)])), L(outline([(84, 30), (88, 6, 1), (70, 18)])),
                                                   L(outline([(38, 12), (44, -2), (56, -2), (62, 12), (58, 34), (50, 56, 1), (42, 34)]), MOHAWK, 'b', False),
                                                   strand([(50, 0), (50, 44)], (120, 70, 70, 255), 'b', 1.0)]
             + white_eyes(76, 14, 6.4, 6, 2.0) + brows(65, 'mid', 4.0, 14, 0.8) + [mouth([(36, 92), (50, 99), (64, 92)], BROWN, 1.6)] + nose(87),
    'side': crop('side', top=4, w=2) + [L(outline([(36, 12), (50, -4), (70, 0), (84, 16), (74, 22), (54, 12)]), MOHAWK, 'b', False)] + side_eye(76)
            + brow_side(65, 'mid', 4.0, 0.6),
    'back': crop('back', top=4, w=2, nape=82) + [L(outline([(16, 30), (12, 6, 1), (30, 18)])), L(outline([(84, 30), (88, 6, 1), (70, 18)])),
                                                 L(outline([(40, 10), (44, -2), (56, -2), (60, 10), (56, 60), (44, 60)]), MOHAWK, 'b', False)],
}

# Vince Bull: la cabeza entera vendada como una momia, con unos pelos verde azulado de punta que asoman; solo se le ve un
# ojo claro, redondo
BANDAGE = (232, 214, 200, 255)
BAND_D = (200, 170, 160, 255)
CHARS[K + 'vince-bull'] = {
    'body': 'normal', 'pal': pal('#3a7a70', '#c08a5e', shade='#2e625a', deep='#224a44'),
    'face': {'eyes': 'none', 'mouth': 'none', 'hairline': False},
    'front': [L(outline([(10, 30), (2, 6, 1), (24, 18)])), L(outline([(84, 22), (100, 2, 1), (92, 30)])), L(outline([(8, 76), (-6, 82, 1), (10, 86)])),
              L(outline([(90, 84), (102, 92, 1), (88, 94)])),
              fr([(10, 60), (14, 26), (34, 8), (60, 6), (84, 20), (92, 48), (88, 86), (70, 104), (50, 108), (30, 104), (14, 88)], BANDAGE),
              L(outline([(60, 66), (80, 64), (82, 82), (64, 86)]), 'skin', 'f', False),
              L(ell(70, 75, 5.6, 6), (240, 232, 170, 255), 'f', ln=True), L(ell(70, 75, 1.6, 1.8), OUTC, 'f', False),
              L(quad((16, 40), (50, 20), (86, 34)), BAND_D, 'f', False, False, 1.4), L(quad((14, 60), (40, 50), (60, 64)), BAND_D, 'f', False, False, 1.4),
              L(quad((18, 88), (50, 78), (84, 92)), BAND_D, 'f', False, False, 1.4), L(quad((60, 90), (70, 96), (84, 86)), BAND_D, 'f', False, False, 1.4)],
    'side': [L(outline([(30, 14), (22, -6, 1), (44, 6)])), L(outline([(4, 60), (-10, 66, 1), (6, 72)])),
             fr([(50, 2), (78, 8), (92, 30), (94, 60), (90, 90), (76, 104), (56, 104), (34, 92), (8, 76), (2, 44), (16, 14)], BANDAGE),
             L(quad((10, 30), (50, 16), (90, 30)), BAND_D, 'f', False, False, 1.4), L(quad((6, 60), (50, 50), (94, 70)), BAND_D, 'f', False, False, 1.4)],
    'back': [L(outline([(16, 26), (6, 4, 1), (30, 16)])), L(outline([(84, 22), (98, 2, 1), (90, 30)])),
             fr([(12, 66), (12, 30), (30, 10), (50, 4), (70, 10), (88, 30), (88, 66), (74, 88), (50, 94), (26, 88)], BANDAGE),
             L(quad((14, 36), (50, 22), (86, 40)), BAND_D, 'f', False, False, 1.4), L(quad((12, 62), (50, 52), (88, 66)), BAND_D, 'f', False, False, 1.4)],
}

# Vinny O'Gaines: pelo verde oliva en un tupé altísimo en forma de llama inclinado a su izquierda, con los lados cortos;
# gafas redondas grandes de cristal blanco opaco y sonrisa
LENS = (238, 232, 216, 255)
CHARS[K + 'vinny-o-gaines'] = {
    'body': 'normal', 'pal': pal('#5a6a30', '#f0b070', shade='#485624', deep='#34401a'),
    'face': {'eyes': 'none', 'mouth': 'smile', 'mouth_y': 96, 'hairline': [(16, 64), (18, 48), (40, 44), (70, 44), (82, 48), (84, 64)]},
    'front': [L(outline([(16, 66), (12, 42), (18, 16), (40, -10), (64, -30), (80, -36, 1), (78, -16), (88, 10), (88, 40), (84, 66), (80, 48), (20, 48)])),
              L(outline([(62, -24), (78, -34), (76, -14), (86, 12), (86, 50), (78, 30), (70, 8)]), 'shade', 'b', False),
              strand([(30, 20), (56, -10), (74, -28)], 'deep', 'b', 1.0), strand([(44, 30), (66, 4), (78, -10)], 'deep', 'b', 1.0)]
             + [L(ell(34, 77, 10, 9), LENS, 'f', False), L(ell(66, 77, 10, 9), LENS, 'f', False)]
             + ring_glasses('front', 77, (196, 110, 50, 255), 2.2, 10, 9, 16),
    'side': [L(outline([(72, 52), (84, 44), (90, 26), (88, 4), (96, -24), (102, -38, 1), (82, -26), (60, -12), (34, -6), (12, 10), (4, 36), (8, 60), (20, 78), (34, 74),
                        (40, 60), (54, 54)])),
             L(outline([(4, 36), (30, 42), (40, 58), (34, 72), (20, 76), (8, 58)]), 'shade', 'b', False),
             L(ell(84, 77, 5, 9), LENS, 'f', False)] + ring_glasses('side', 77, (196, 110, 50, 255), 2.2, 5, 9),
    'back': [L(outline([(16, 78), (12, 46), (16, 18), (36, -4), (60, -26), (78, -34, 1), (80, -10), (90, 16), (90, 46), (84, 78), (50, 86)])),
             L(outline([(60, -22), (78, -32), (80, -10), (90, 20), (88, 72), (64, 84)]), 'shade', 'b', False)],
}

# Vinny Trioquist: pelo rubio crema por debajo y encima unos tirabuzones rojos gruesos como rollos que le salen hacia todos
# lados; ojos azules grandes, pecas y sonrisa
ROLL = (196, 58, 30, 255)
ROLL_D = (150, 40, 20, 255)


def _rolls(view, roll=None, roll_d=None):
    roll, roll_d = roll or ROLL, roll_d or ROLL_D
    import math
    out = []
    if view == 'front':
        spots = [(-145, 40), (-115, 44), (-90, 46), (-65, 44), (-35, 40), (-172, 34), (-8, 34)]
        for a, r in spots:
            ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
            p0 = (50 + ca * 10, 40 + sa * 10)
            p1 = (50 + ca * r, 44 + sa * r * 0.95)
            out.append(L(rope(p0, ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2), p1, 21), roll, 'b'))
        for a, r in spots:
            ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
            for t in (0.5, 0.75):
                x, y = 50 + ca * r * t, 44 + sa * r * 0.95 * t
                out.append(L([(x - sa * 6, y + ca * 6), (x + sa * 6, y - ca * 6)], roll_d, 'b', False, False, 1.0))
        return out
    if view == 'side':
        for a, r in [(-150, 42), (-120, 44), (-90, 44), (-60, 40), (-180, 36), (150, 34)]:
            ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
            p0 = (44 + ca * 10, 40 + sa * 10)
            p1 = (44 + ca * r, 44 + sa * r * 0.95)
            out.append(L(rope(p0, ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2), p1, 21), roll, 'b'))
        return out
    for a, r in [(-140, 40), (-110, 44), (-80, 46), (-50, 42), (-170, 36), (-10, 36), (160, 34), (20, 34)]:
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        p0 = (50 + ca * 10, 44 + sa * 10)
        p1 = (50 + ca * r, 48 + sa * r * 0.95)
        out.append(L(rope(p0, ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2), p1, 21), roll, 'b'))
    return out


CHARS[K + 'vinny-trioquist'] = {
    'body': 'normal', 'pal': pal('#efe0b8', '#f8d0a4', iris='#3a5a8a', shade='#d8c49a', deep='#b8a478'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': [(16, 66), (18, 50), (30, 44), (50, 50), (70, 44), (82, 50), (84, 66)]},
    'front': [L(outline([(16, 68), (12, 42), (20, 20), (50, 10), (80, 20), (88, 42), (84, 68), (80, 52), (20, 52)]))] + _rolls('front') + freckles(87),
    'side': [L(outline([(70, 50), (86, 42), (88, 24), (70, 8), (40, 6), (16, 16), (4, 40), (8, 64), (20, 80), (34, 76), (40, 60), (54, 54)]))] + _rolls('side'),
    'back': [L(outline([(16, 76), (12, 44), (20, 20), (50, 10), (80, 20), (88, 44), (84, 76), (50, 84)]))] + _rolls('back'),
}

# Virgil Lantis: piel tostada; la cabeza rapada verde oliva con una cresta amarilla corta en el centro; cejas negras fruncidas,
# ojitos, nariz grande y boca seria
CHARS[K + 'virgil-lantis'] = {
    'body': 'normal', 'pal': pal('#6a8a40', '#b88050', shade='#587434', deep='#425a26'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': (56, 44)},
    'front': crop('front', top=6, side=56, w=0, shade=False)
             + [L(outline([(40, 10), (44, 2), (56, 2), (60, 10), (56, 36), (50, 46, 1), (44, 36)]), (232, 196, 50, 255), 'b', ln=True),
                strand([(50, 4), (50, 36)], (190, 150, 30, 255), 'b', 1.0)] + brows(65, OUTC, 3.6, 14, 1.4) + nose(88),
    'side': crop('side', top=6, w=0, shade=False) + [L(outline([(40, 8), (60, 2), (80, 12), (84, 24), (66, 18)]), (232, 196, 50, 255), 'b', ln=True)]
            + brow_side(65, OUTC, 3.6, 1.0),
    'back': crop('back', top=6, w=0, nape=80, shade=False) + [L(outline([(42, 8), (46, 2), (54, 2), (58, 8), (56, 50), (44, 50)]), (232, 196, 50, 255), 'b', ln=True)],
}

# Viv Grey: pelo gris crema de puntas con un remolino alto en la coronilla y mechones sobre la frente; gafas de sol
# deportivas amarillas de montura verde, sonrisa y un lunar en la barbilla
CHARS[K + 'viv-grey'] = {
    'body': 'normal', 'pal': pal('#d8d0c0', '#f8d4a8', shade='#bcb4a2', deep='#9a9282'),
    'face': {'eyes': 'none', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': messy('front', amp=9, n=10, seed=91, lo=68) + [L(outline([(44, 4), (52, -26, 1), (54, -6), (62, -16, 1), (60, 4)]))]
             + [spiky_fringe(66, 16, 84, 4, 26, 12)]
             + [L(outline([(20, 72), (46, 74), (50, 78), (54, 74), (80, 72), (78, 82), (60, 84), (50, 80), (40, 84), (22, 82)]), (232, 196, 40, 255), 'f', False),
                L(outline([(20, 72), (46, 74), (50, 78), (54, 74), (80, 72), (78, 82), (60, 84), (50, 80), (40, 84), (22, 82), (20, 72)]), (60, 140, 70, 255), 'f', False,
                  False, 2.2),
                L(ell(54, 101, 0.9, 0.9), OUTC, 'f', False)],
    'side': messy('side', amp=9, n=10, seed=91) + [L(outline([(44, 2), (54, -26, 1), (58, -6), (66, -14, 1), (62, 4)])),
                                                   L(outline([(72, 72), (90, 72), (90, 82), (74, 82)]), (232, 196, 40, 255), 'f', ln=True),
                                                   L([(72, 74), (50, 72)], (60, 140, 70, 255), 'f', False, False, 2.2)],
    'back': messy('back', amp=9, n=10, seed=91) + [L(outline([(44, 4), (52, -26, 1), (54, -6), (62, -16, 1), (60, 4)]))],
}

# Waite Forrit: adulto de cara alargada; pelo gris pardo de puntas hacia los lados con pico en la frente; cejas grises
# gruesas, ojos afilados y sonrisa
CHARS[K + 'waite-forrit'] = {
    'body': 'normal', 'pal': pal('#827a6a', '#f0c088', shade='#6a6456', deep='#524c40'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': [(16, 64), (20, 46), (36, 42), (50, 54), (64, 42), (80, 46), (84, 64)]},
    'front': [L(outline([(16, 66), (12, 52), (-2, 48, 1), (10, 40), (-2, 26, 1), (14, 22), (10, 6, 1), (28, 10), (36, -4, 1), (46, 6), (60, -4, 1), (64, 8), (84, 2, 1),
                         (82, 18), (100, 22, 1), (88, 34), (102, 44, 1), (88, 50), (84, 66), (80, 48), (20, 48)])),
              L(outline([(58, 0), (64, 8), (82, 4), (80, 20), (96, 24), (88, 36), (98, 44), (86, 52), (78, 30)]), 'shade', 'b', False)]
             + brows(64, 'mid', 4.6, 15, 0.8) + nose(88),
    'side': [L(outline([(70, 52), (82, 46), (90, 34), (100, 26, 1), (88, 18), (96, 4, 1), (78, 2), (80, -10, 1), (62, -2), (50, -12, 1), (40, 2), (20, -2, 1), (16, 16),
                        (-4, 24, 1), (6, 36), (-6, 50, 1), (6, 58), (16, 76), (28, 84), (36, 78), (38, 62), (46, 56), (60, 54)])),
             L(outline([(6, 38), (30, 42), (42, 58), (36, 64), (36, 78), (28, 84), (16, 76)]), 'shade', 'b', False)] + brow_side(64, 'mid', 4.6, 0.6),
    'back': [L(outline([(18, 80), (12, 56), (-2, 50, 1), (10, 42), (-2, 28, 1), (14, 22), (10, 6, 1), (28, 10), (36, -4, 1), (48, 6), (60, -4, 1), (66, 8), (86, 2, 1),
                        (82, 20), (100, 24, 1), (88, 36), (102, 48, 1), (88, 54), (82, 80), (50, 88)])),
             L(outline([(60, 0), (66, 8), (84, 4), (80, 22), (96, 26), (88, 38), (98, 48), (86, 56), (82, 78), (64, 86)]), 'shade', 'b', False)],
}

# Walker Sleep (portero): grandullón adulto de cara alargada; pelo azul grisáceo en pinchos hacia arriba con patillas largas;
# ojos blancos de párpado caído, nariz grande y boca recta y ancha
CHARS[K + 'walker-sleep'] = {
    'body': 'corpulento', 'pal': pal('#6a8a9c', '#f0b878', shade='#567284', deep='#405868'),
    'face': {'eyes': 'none', 'mouth': 'none', 'hairline': [(17, 74), (18, 50), (34, 42), (50, 52), (66, 42), (82, 50), (83, 74)]},
    'front': [L(outline([(16, 80), (12, 44), (8, 24, 1), (18, 18), (16, 0, 1), (30, 6), (36, -12, 1), (46, 2), (56, -14, 1), (62, 2), (76, -6, 1), (76, 10), (92, 20, 1),
                         (88, 44), (84, 80), (80, 50), (20, 50)])),
              L(outline([(58, -8), (64, 4), (76, -2), (76, 14), (90, 22), (88, 46), (84, 76), (78, 40)]), 'shade', 'b', False)]
             + white_eyes(77, 14, 6.4, 5, 1.8, lid=1.0) + nose(88) + [mouth([(36, 98), (64, 98)], OUTC, 1.6)],
    'side': [L(outline([(72, 52), (84, 46), (90, 30), (98, 16, 1), (86, 12), (90, -6, 1), (72, 0), (68, -16, 1), (54, -2), (40, -14, 1), (32, 4), (14, 2, 1), (14, 18),
                        (4, 34), (6, 58), (14, 76), (28, 84), (36, 78), (38, 62), (44, 56), (52, 66), (54, 84), (60, 84), (60, 56)])),
             L(outline([(6, 36), (30, 40), (42, 56), (36, 64), (36, 78), (28, 84), (14, 76)]), 'shade', 'b', False)] + side_eye(77, lid=1.0),
    'back': [L(outline([(16, 80), (12, 44), (8, 24, 1), (18, 18), (16, 0, 1), (30, 6), (36, -12, 1), (46, 2), (56, -14, 1), (62, 2), (76, -6, 1), (76, 10), (92, 20, 1),
                        (88, 44), (84, 80), (50, 88)])),
             L(outline([(58, -8), (64, 4), (76, -2), (76, 14), (90, 22), (88, 46), (84, 78), (64, 86)]), 'shade', 'b', False)],
}

# Walter Card: bajito y mofletudo de piel muy clara; pelo naranja en forma de seta (tazón redondo) con un rabito arriba;
# coloretes rosas, ojitos con pestañas, naricita y sonrisa
CHARS[K + 'walter-card'] = {
    'body': 'bajito', 'pal': pal('#e07a2a', '#fce6c0', shade='#c0621a', deep='#9a4a10'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 97, 'hairline': (64, 63),
             'face_front': blob([(14, 50), (50, 40), (86, 50), (94, 78), (86, 100), (66, 110), (50, 112), (34, 110), (14, 100), (6, 78)])},
    'front': [L(outline([(6, 62), (2, 40), (12, 14), (50, 2), (88, 14), (98, 40), (94, 62), (50, 60)])),
              L(outline([(60, 6), (88, 16), (98, 40), (94, 60), (78, 60), (80, 30)]), 'shade', 'b', False),
              L(quad((48, 4), (46, -6), (56, -10)), 'shade', 'b', False, False, 3.0),
              strand([(30, 12), (26, 56)], 'deep', 'f', 1.0), strand([(50, 6), (50, 58)], 'deep', 'f', 1.0), strand([(70, 12), (74, 56)], 'deep', 'f', 1.0),
              L(quad((6, 62), (50, 64), (94, 62)), OUTC, 'f', False, False, 1.4)]
             + blush(88, (240, 160, 150, 255), 26, 6)
             + [L(blob([(46, 86), (54, 86), (53, 90), (47, 90)], 5), (230, 170, 150, 255), 'f', ln=True)],
    'side': [L(outline([(88, 62), (98, 44), (90, 16), (60, 0), (30, 2), (8, 20), (2, 44), (8, 64), (40, 66), (60, 62)])),
             L(outline([(2, 40), (40, 40), (60, 62), (8, 64)]), 'shade', 'b', False), L(quad((50, 2), (48, -8), (58, -12)), 'shade', 'b', False, False, 3.0)],
    'back': [L(outline([(6, 66), (2, 40), (12, 14), (50, 2), (88, 14), (98, 40), (94, 66), (50, 72)])),
             L(outline([(58, 6), (88, 16), (98, 40), (94, 66), (60, 70)]), 'shade', 'b', False), L(quad((48, 4), (46, -6), (56, -10)), 'shade', 'b', False, False, 3.0)],
}

# Walter Geyser: cara de mono con orejas grandes y redondas; pelo rubio arena en pinchos altos arriba y una melena que le cae
# a los lados tapando las orejas; cejas gruesas rubias, ojitos y sonrisa enorme
CHARS[K + 'walter-geyser'] = {
    'body': 'normal', 'pal': pal('#d8c080', '#fce6b8', shade='#bca468', deep='#9a8450'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'none', 'big_ears': 3, 'ear_out': 4, 'hairline': (60, 50)},
    'front': [L(outline([(16, 60), (12, 36), (4, 20, 1), (20, 18), (20, -4, 1), (34, 10), (42, -22, 1), (50, 6), (60, -18, 1), (64, 8), (82, -2, 1), (80, 18), (96, 20, 1),
                         (88, 36), (84, 60), (50, 54)])),
              L(outline([(10, 52), (2, 80), (4, 100, 1), (20, 90), (26, 70), (22, 54)])), L(outline([(90, 52), (98, 80), (96, 100, 1), (80, 90), (74, 70), (78, 54)])),
              L(outline([(58, -10), (64, 8), (80, 2), (80, 20), (92, 22), (88, 36), (84, 56), (74, 30)]), 'shade', 'b', False)]
             + brows(66, 'mid', 5.0, 15, 0.8) + [mouth([(34, 88), (50, 97), (66, 88)], OUTC, 1.6)],
    'side': [L(outline([(70, 50), (84, 42), (94, 30, 1), (86, 22), (100, 8, 1), (84, 4), (88, -14, 1), (70, -4), (66, -24, 1), (54, -4), (36, -18, 1), (32, 2), (12, 2, 1),
                        (14, 20), (2, 36), (2, 64), (8, 90), (16, 100, 1), (24, 88), (34, 80), (40, 62), (54, 54)])),
             L(outline([(4, 38), (30, 42), (40, 60), (30, 82), (14, 90)]), 'shade', 'b', False)],
    'back': [L(outline([(10, 96, 1), (4, 70), (10, 40), (4, 20, 1), (20, 18), (20, -4, 1), (34, 10), (42, -22, 1), (50, 6), (60, -18, 1), (64, 8), (82, -2, 1), (80, 18),
                        (96, 20, 1), (90, 40), (96, 70), (90, 96, 1), (70, 88), (50, 92), (30, 88)])),
             L(outline([(60, -10), (66, 8), (82, 2), (80, 20), (94, 22), (90, 42), (94, 70), (90, 94), (66, 88)]), 'shade', 'b', False)],
}

# Walter Mendip: pelo rojo en tazón con flequillo recto hasta las cejas y dos pelillos rizados de antena; ojos blancos
# redondos grandes, cejas fruncidas y sonrisa
CHARS[K + 'walter-mendip'] = {
    'body': 'normal', 'pal': pal('#c23c1c', '#f0b878', shade='#a02e14', deep='#7a220e'),
    'face': {'eyes': 'none', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': bob('front', 74, top=2, w=4, bang=64)
             + [L(quad((48, 4), (40, -10), (32, -6)), 'deep', 'b', False, False, 1.6), L(quad((52, 4), (60, -10), (68, -6)), 'deep', 'b', False, False, 1.6)]
             + [strand([(30, 30), (30, 62)], 'deep', 'f', 1.0), strand([(50, 26), (50, 62)], 'deep', 'f', 1.0), strand([(70, 30), (70, 62)], 'deep', 'f', 1.0)]
             + white_eyes(78, 14, 6.8, 6.6, 2.4) + [L([(24, 67), (40, 70)], OUTC, 'f', False, False, 2.6), L([(76, 67), (60, 70)], OUTC, 'f', False, False, 2.6)],
    'side': bob('side', 74, top=2, w=4) + [fr([(70, 30), (92, 36), (92, 64, 1), (82, 60), (76, 50)]), L(quad((50, 4), (44, -10), (36, -6)), 'deep', 'b', False, False, 1.6)]
            + side_eye(78),
    'back': bob('back', 74, top=2, w=4) + [L(quad((48, 4), (40, -10), (32, -6)), 'deep', 'b', False, False, 1.6)],
}

# Walter Poseur: presumido: pelo verde con un mechón enorme ondulado que le cae por su izquierda hasta el hombro; ojos
# cerrados con pestañas y sombra verde, labios gruesos marrones
CHARS[K + 'walter-poseur'] = {
    'body': 'delgado', 'pal': pal('#6a9a40', '#f8d0a4', shade='#4c7a2c', deep='#38601e'),
    'face': {'eyes': 'none', 'mouth': 'none', 'hairline': [(16, 68), (16, 46), (30, 40), (50, 36), (70, 40), (84, 48), (84, 68)]},
    'front': [L(outline([(14, 70), (6, 56), (8, 36), (16, 14), (36, 2), (56, -4), (74, 0), (90, 12), (96, 30), (92, 48), (100, 70), (98, 92), (92, 104, 1), (86, 88),
                         (84, 70), (82, 52), (20, 52)])),
              L(outline([(8, 50), (6, 76), (0, 92, 1), (12, 84), (20, 72), (18, 54)]), 'deep'),
              L(outline([(58, 0), (78, 4), (92, 16), (94, 34), (90, 50), (98, 72), (94, 96), (86, 80), (80, 40)]), 'shade', 'b', False),
              strand([(30, 10), (60, 14), (86, 34)], 'light', 'b', 1.4), strand([(40, 4), (72, 8), (90, 22)], 'deep', 'b', 1.0)]
             + [L(quad((26, 76), (35, 72), (44, 76)), OUTC, 'f', False, False, 2.0), L(quad((56, 76), (65, 72), (74, 76)), OUTC, 'f', False, False, 2.0),
                L(quad((26, 72), (35, 66), (44, 71)), (90, 150, 60, 255), 'f', False, False, 2.4), L(quad((56, 71), (65, 66), (74, 72)), (90, 150, 60, 255), 'f', False, False, 2.4),
                L([(24, 75), (22, 73)], OUTC, 'f', False, False, 1.2), L([(76, 75), (78, 73)], OUTC, 'f', False, False, 1.2),
                L(blob([(42, 95), (50, 92), (58, 95), (54, 99), (46, 99)], 6), (140, 80, 60, 255), 'f', ln=True)],
    'side': [L(outline([(74, 50), (86, 42), (92, 26), (82, 8), (58, -6), (32, -2), (12, 12), (2, 36), (2, 60), (-4, 84), (-2, 100, 1), (12, 90), (24, 80), (36, 76), (40, 60),
                        (54, 54)])),
             L(outline([(4, 36), (30, 42), (40, 60), (26, 80), (6, 92)]), 'shade', 'b', False)]
            + [L(quad((76, 76), (81, 73), (86, 76)), OUTC, 'f', False, False, 2.0), L(ell(86, 96, 3, 2.4), (140, 80, 60, 255), 'f', ln=True)],
    'back': [L(outline([(14, 84), (8, 50), (14, 20), (34, 2), (56, -4), (78, 2), (92, 20), (94, 50), (100, 74), (96, 96), (90, 106, 1), (80, 90), (50, 90)])),
             L(outline([(58, 0), (80, 6), (94, 30), (96, 74), (90, 102), (78, 88), (64, 88)]), 'shade', 'b', False)],
}

# Walter Walken: piel morena; los lados rapados azul y una cresta alta azul marino en bloque; ojos grises, cejas fruncidas y
# sonrisa
NAVY2 = (42, 62, 92, 255)
CHARS[K + 'walter-walken'] = {
    'body': 'normal', 'pal': pal('#4c7c9a', '#b87a4c', iris='#8a9a8a', shade='#3c6680', deep='#2c4c62'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': (58, 46)},
    'front': crop('front', top=6, side=60, w=0, shade=False)
             + [L(outline([(40, 20), (40, -20), (46, -26), (54, -26), (60, -20), (60, 20), (50, 30)]), NAVY2, 'b', ln=True),
                L([(44, -16), (56, -16)], (70, 100, 140, 255), 'b', False, False, 1.0), L([(44, -6), (56, -6)], (70, 100, 140, 255), 'b', False, False, 1.0),
                L([(44, 4), (56, 4)], (70, 100, 140, 255), 'b', False, False, 1.0)],
    'side': crop('side', top=6, w=0, shade=False) + [L(outline([(20, 14), (30, -20), (46, -28), (70, -22), (80, 0), (78, 18), (50, 10)]), NAVY2, 'b', ln=True)],
    'back': crop('back', top=6, w=0, nape=82, shade=False) + [L(outline([(40, 24), (40, -20), (46, -26), (54, -26), (60, -20), (60, 24), (50, 40)]), NAVY2, 'b', ln=True)],
}

# Webber Poster: piel tostada; cabeza rapada crema con una franja oliva en el centro; unos cercos oscuros enormes alrededor
# de los ojos (como un mapache), ojitos y boca recta
OLIVE_D = (80, 82, 40, 255)
CHARS[K + 'webber-poster'] = {
    'body': 'normal', 'pal': pal('#e2dab4', '#e8a868', shade='#c8c09a', deep='#a8a07a'),
    'face': {'eyes': 'none', 'mouth': 'none', 'hairline': (54, 42), 'ear_out': 2},
    'front': crop('front', top=6, side=54, w=0, shade=False)
             + [L(outline([(44, 8), (56, 8), (56, 40), (44, 40)]), OLIVE_D, 'b', False)]
             + [L(ell(34, 76, 10, 9), OLIVE_D, 'f', ln=True), L(ell(66, 76, 10, 9), OLIVE_D, 'f', ln=True)]
             + white_eyes(77, 16, 5.2, 4.6, 1.8, lid=1.4) + nose(89) + [mouth([(40, 98), (60, 98)], OUTC, 1.5)],
    'side': crop('side', top=6, w=0, shade=False) + [L(quad((40, 4), (64, 6), (84, 22)), OLIVE_D, 'b', False, False, 6),
                                                     L(ell(82, 76, 6, 9), OLIVE_D, 'f', ln=True)] + side_eye(77, lid=1.4),
    'back': crop('back', top=6, w=0, nape=80, shade=False) + [L(outline([(44, 8), (56, 8), (56, 76), (44, 76)]), OLIVE_D, 'b', False)],
}

# Weldon Wrought: cabeza calva con un mechón cuadrado granate oscuro en la coronilla; cara alargada, ojos afilados
# estrechos, nariz grande y media sonrisa
CHARS[K + 'weldon-wrought'] = {
    'body': 'normal', 'pal': pal('#5a3a4a', '#f0b878', shade='#4a2e3c', deep='#38222c'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False, 'big_ears': 1},
    'front': bald('front') + [L(outline([(40, 16), (34, -6), (50, -12), (66, -6), (60, 16), (50, 24)])),
                              L(outline([(50, -12), (66, -6), (60, 16), (50, 24)]), 'shade', 'b', False)] + nose(88),
    'side': bald('side') + [L(outline([(30, 14), (30, -8), (50, -14), (66, -6), (56, 14), (44, 20)]))],
    'back': bald('back') + [L(outline([(40, 16), (34, -6), (50, -12), (66, -6), (60, 16), (50, 24)]))],
}

# Wes Abbey: pelo crema claro, rosado en las raíces, en tazón con flequillo de puntas; cara redonda, ojos blancos redondos
# con pestañas, cejas crema gruesas y boca de pucheros
CHARS[K + 'wes-abbey'] = {
    'body': 'normal', 'pal': pal('#ecdcc4', '#f0b070', shade='#c8aca4', deep='#a88a84'),
    'face': {'eyes': 'none', 'mouth': 'none', 'hairline': False,
             'face_front': blob([(14, 52), (50, 40), (86, 52), (92, 78), (86, 100), (66, 110), (50, 112), (34, 110), (14, 100), (8, 78)])},
    'front': bob('front', 74, top=0, w=6, bang=0)
             + [fr([(10, 66), (12, 36), (30, 18), (50, 12), (70, 18), (88, 36), (90, 66), (82, 56), (76, 66, 1), (68, 54), (58, 64, 1), (52, 52), (42, 64, 1), (36, 54),
                    (26, 64, 1), (18, 56)]),
                strand([(36, 18), (40, 50)], 'shade', 'f', 1.2), strand([(62, 18), (60, 50)], 'shade', 'f', 1.2)]
             + white_eyes(79, 15, 6.6, 6.2, 2.4) + brows(68, (240, 226, 200, 255), 3.6, 15, 0.8)
             + [L([(18, 77), (22, 74)], OUTC, 'f', False, False, 1.0), L([(82, 77), (78, 74)], OUTC, 'f', False, False, 1.0),
                mouth([(40, 98), (45, 95), (50, 97), (55, 95), (60, 98)], OUTC, 1.5)],
    'side': bob('side', 74, top=0, w=6) + [fr([(68, 30), (92, 36), (94, 62, 1), (84, 56), (76, 52)])] + side_eye(79),
    'back': bob('back', 74, top=0, w=6),
}

# Will Bayeux (portero): pelo naranja corto con dos picos a los lados como orejas de gato y pico en la frente; ojos grises
# grandes, cejas fruncidas y boca seria
CHARS[K + 'will-bayeux'] = {
    'body': 'normal', 'pal': pal('#e07a2a', '#fcd4a8', iris='#8a8098', shade='#c0621a', deep='#9a4a10'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': [(16, 62), (20, 46), (34, 42), (50, 58), (66, 42), (80, 46), (84, 62)]},
    'front': crop('front', top=0, side=64, w=4) + [L(outline([(14, 34), (8, 4, 1), (32, 16)])), L(outline([(86, 34), (92, 4, 1), (68, 16)])),
                                                   strand([(40, 10), (48, 40)], 'deep', 'b', 1.0), strand([(60, 10), (52, 40)], 'deep', 'b', 1.0)],
    'side': crop('side', top=0, w=4) + [L(outline([(36, 14), (34, -10, 1), (54, 6)]))],
    'back': crop('back', top=0, w=4, nape=84) + [L(outline([(14, 34), (8, 4, 1), (32, 16)])), L(outline([(86, 34), (92, 4, 1), (68, 16)]))],
}

# Will Noble (portero): pelo castaño liso hasta los hombros con flequillo largo de mechones; gafas finas doradas de cristal
# rectangular, ojos rojizos y boca seria
GOLD = (196, 150, 60, 255)
CHARS[K + 'will-noble'] = {
    'body': 'normal', 'pal': pal('#7a4a2a', '#f8d0a8', iris='#a04a30', shade='#643a20', deep='#4a2a14'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 108, 1), (4, 80), (4, 40), (16, 12), (50, 0), (84, 12), (96, 40), (96, 80), (90, 108, 1), (82, 96), (82, 60), (18, 60), (18, 96)])),
              L(outline([(60, 4), (86, 16), (96, 44), (94, 104), (84, 94), (82, 50)]), 'shade', 'b', False),
              fr([(14, 76), (14, 40), (28, 20), (50, 14), (72, 20), (86, 40), (86, 76), (80, 62), (74, 72, 1), (68, 56), (58, 68, 1), (54, 52), (46, 70, 1), (40, 54),
                  (30, 66, 1), (22, 58)]),
              strand([(40, 22), (44, 56)], 'deep', 'f', 1.0), strand([(64, 22), (62, 56)], 'deep', 'f', 1.0)]
             + [L(outline([(22, 71), (46, 72), (46, 82), (24, 82), (22, 71)]), GOLD, 'f', False, False, 1.4),
                L(outline([(78, 71), (54, 72), (54, 82), (76, 82), (78, 71)]), GOLD, 'f', False, False, 1.4), L([(46, 75), (54, 75)], GOLD, 'f', False, False, 1.2)],
    'side': [L(outline([(80, 50), (90, 40), (90, 20), (76, 2), (50, -4), (24, 2), (8, 20), (2, 50), (4, 84), (10, 108, 1), (30, 102), (44, 98), (50, 106, 1), (54, 84),
                        (56, 62), (70, 58)])),
             L(outline([(2, 46), (30, 46), (50, 66), (50, 96), (30, 100), (12, 104)]), 'shade', 'b', False),
             L([(76, 71), (88, 71), (88, 82), (77, 82), (76, 71)], GOLD, 'f', False, False, 1.4), L([(76, 74), (50, 72)], GOLD, 'f', False, False, 1.2)],
    'back': [L(outline([(8, 108, 1), (4, 80), (4, 40), (16, 12), (50, 0), (84, 12), (96, 40), (96, 80), (92, 108, 1), (70, 102), (50, 108), (30, 102)])),
             L(outline([(56, 4), (84, 12), (96, 40), (96, 80), (92, 106), (66, 102), (60, 50)]), 'shade', 'b', False)],
}

# Will Racer: pelo morado oscuro ondulado recogido en una coleta rizada que le cae por su izquierda, con una onda encima de la
# frente; ojos blancos de pupila pequeña, cejas fruncidas y boca seria
CHARS[K + 'will-racer'] = {
    'body': 'normal', 'pal': pal('#4c3c6c', '#f8c890', shade='#3c2e58', deep='#2c2242'),
    'face': {'eyes': 'none', 'mouth': 'frown', 'mouth_y': 96, 'hairline': [(16, 66), (16, 48), (30, 40), (52, 42), (70, 38), (84, 48), (84, 66)]},
    'front': crop('front', top=-2, side=68, w=6)
             + [L(outline([(80, 58), (96, 62), (100, 80), (106, 96), (98, 108, 1), (96, 92), (88, 80), (86, 66)])),
                fr([(14, 60), (14, 40), (26, 22), (46, 16), (60, 22), (50, 30), (34, 38), (22, 52)]),
                strand([(30, 22), (52, 14), (74, 20)], 'deep', 'b', 1.0), strand([(90, 66), (98, 84), (98, 100)], 'deep', 'b', 1.0)]
             + white_eyes(77, 14, 6.2, 5.6, 1.8) + [L([(26, 68), (42, 72)], OUTC, 'f', False, False, 2.4), L([(74, 68), (58, 72)], OUTC, 'f', False, False, 2.4)],
    'side': crop('side', top=-2, w=6) + side_eye(77),
    'back': crop('back', top=-2, w=6, nape=86) + [L(outline([(16, 70), (2, 80), (-2, 100), (6, 110, 1), (10, 94), (20, 82)])),
                                                  strand([(8, 80), (4, 100)], 'deep', 'b', 1.0)],
}

# Will Stonehead: cara de simio: pelo rosa rojizo con un tupé de pico en la coronilla y patillas anchas que le bajan por los
# lados de la cara; ojos entornados, nariz ancha y labios gruesos
CHARS[K + 'will-stonehead'] = {
    'body': 'corpulento', 'pal': pal('#c26c6c', '#f0b070', shade='#a45656', deep='#844242'),
    'face': {'eyes': 'none', 'mouth': 'none', 'hairline': (62, 48),
             'face_front': blob([(14, 52), (50, 42), (86, 52), (92, 80), (86, 102), (66, 112), (50, 114), (34, 112), (14, 102), (8, 80)])},
    'front': crop('front', top=8, side=66, w=6)
             + [L(outline([(36, 14), (44, -6), (54, -12, 1), (52, 2), (62, 10)])),
                L(outline([(8, 50), (4, 80), (10, 98), (18, 96), (16, 70), (20, 52)])), L(outline([(92, 50), (96, 80), (90, 98), (82, 96), (84, 70), (80, 52)]))]
             + white_eyes(77, 14, 6.2, 4.6, 1.6, lid=1.0) + brows(68, OUTC, 2.4, 14, 1.0)
             + [L([(44, 88), (42, 91), (50, 92), (58, 91), (56, 88)], (150, 90, 60, 255), 'f', False, False, 1.2),
                L(blob([(38, 99), (50, 96), (62, 99), (58, 104), (42, 104)], 6), (210, 150, 90, 255), 'f', ln=True), L([(40, 100), (60, 100)], OUTC, 'f', False, False, 1.0)],
    'side': crop('side', top=8, w=6) + [L(outline([(40, 12), (50, -6), (60, -12, 1), (58, 4), (66, 12)]))] + side_eye(77, lid=1.0)
            + [L(ell(86, 100, 3.6, 3), (210, 150, 90, 255), 'f', ln=True)],
    'back': crop('back', top=8, w=6, nape=84) + [L(outline([(36, 14), (44, -6), (54, -12, 1), (52, 2), (62, 10)]))],
}

# Will Whist (portero): calvo con una cicatriz cosida en la cabeza y otra en la mejilla; una mascarilla de tela beige con dos
# huesos cruzados morados; ojos blancos fruncidos y cejas gruesas
MASK = (200, 190, 140, 255)
BONE = (140, 120, 160, 255)
CHARS[K + 'will-whist'] = {
    'body': 'corpulento', 'pal': pal('#e0a060', '#e8a060', shade='#c88a4a', deep='#a06a30'),
    'face': {'eyes': 'none', 'mouth': 'none', 'hairline': False},
    'front': bald('front') + [L(quad((30, 30), (50, 16), (70, 28)), OUTC, 'f', False, False, 1.2)]
             + [L([(x, 23 - abs(x - 50) * 0.18 - 3), (x + 1, 23 - abs(x - 50) * 0.18 + 3)], OUTC, 'f', False, False, 1.0) for x in (36, 44, 52, 60)]
             + white_eyes(74, 14, 6.4, 4.6, 2.0) + [L([(24, 64), (42, 69)], OUTC, 'f', False, False, 3.0), L([(76, 64), (58, 69)], OUTC, 'f', False, False, 3.0)]
             + [L(outline([(16, 80), (50, 78), (84, 80), (82, 100), (66, 108), (50, 110), (34, 108), (18, 100)]), MASK, 'f', ln=True),
                L([(38, 86), (62, 102)], BONE, 'f', False, False, 3.6), L([(62, 86), (38, 102)], BONE, 'f', False, False, 3.6),
                L([(16, 82), (8, 76)], MASK, 'f', False, False, 2.0), L([(84, 82), (92, 76)], MASK, 'f', False, False, 2.0)],
    'side': bald('side') + side_eye(74) + [L(outline([(60, 80), (88, 80), (88, 98), (76, 106), (60, 100)]), MASK, 'f', ln=True),
                                           L([(60, 84), (44, 74)], MASK, 'f', False, False, 2.0)],
    'back': bald('back') + [L(quad((14, 80), (50, 86), (86, 80)), MASK, 'f', False, False, 2.0)],
}

# Willow Withers: pelo morado oscuro de pinchos muy altos con una cinta crema anudada en la frente; ojos negros grandes,
# cejas fruncidas, una tirita en la mejilla y sonrisa
BAND = (226, 216, 190, 255)
CHARS[K + 'willow-withers'] = {
    'body': 'normal', 'pal': pal('#4c3c6c', '#f8c890', shade='#3c2e58', deep='#2c2242'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(16, 66), (12, 44), (0, 34, 1), (14, 26), (6, 8, 1), (24, 12), (26, -14, 1), (38, 4), (46, -24, 1), (54, 2), (64, -18, 1), (68, 6), (86, -2, 1),
                         (82, 18), (100, 30, 1), (88, 40), (84, 66), (80, 56), (20, 56)])),
              L(outline([(58, -10), (68, 6), (84, 2), (82, 20), (96, 30), (86, 42), (84, 62), (76, 36)]), 'shade', 'b', False),
              fr([(14, 66), (16, 60), (28, 62, 1), (34, 58), (44, 66, 1), (50, 58), (62, 66, 1), (68, 58), (78, 64, 1), (86, 60), (86, 66), (50, 64)]),
              L(outline([(10, 44), (50, 40), (90, 44), (90, 54), (50, 50), (10, 54)]), BAND, 'f', ln=True),
              L([(20, 48), (80, 48)], (180, 170, 140, 255), 'f', False, False, 1.0),
              L(outline([(24, 84), (32, 82), (33, 88), (25, 90)]), (240, 220, 180, 255), 'f', ln=True)],
    'side': [L(outline([(70, 50), (82, 46), (94, 36, 1), (86, 28), (102, 14, 1), (86, 8), (96, -12, 1), (74, -4), (72, -24, 1), (56, -6), (40, -22, 1), (32, 0), (12, -2, 1),
                        (14, 16), (-2, 26, 1), (6, 38), (4, 58), (14, 76), (28, 84), (36, 78), (38, 62), (46, 56), (58, 54)])),
             L(outline([(6, 40), (30, 44), (42, 58), (36, 64), (36, 78), (28, 84), (14, 76)]), 'shade', 'b', False),
             L(outline([(4, 40), (50, 34), (92, 42), (92, 52), (50, 46), (4, 50)]), BAND, 'f', ln=True),
             L(outline([(4, 46), (-8, 56, 1), (-4, 60), (6, 52)]), BAND, 'f', ln=True)],
    'back': [L(outline([(16, 80), (12, 50), (0, 38, 1), (14, 30), (6, 8, 1), (24, 12), (26, -14, 1), (38, 4), (46, -24, 1), (54, 2), (64, -18, 1), (68, 6), (86, -2, 1),
                        (82, 18), (100, 32, 1), (88, 44), (84, 80), (50, 88)])),
             L(outline([(58, -10), (68, 6), (84, 2), (82, 20), (98, 32), (86, 46), (84, 78), (64, 86)]), 'shade', 'b', False),
             L(outline([(8, 44), (50, 40), (92, 44), (92, 54), (50, 50), (8, 54)]), BAND, 'f', ln=True),
             L(outline([(44, 50), (38, 66, 1), (46, 64), (50, 52)]), BAND, 'f', ln=True), L(outline([(56, 50), (62, 66, 1), (54, 64), (50, 52)]), BAND, 'f', ln=True)],
}

# Winn Debreeze: rastas gruesas oliva que le salen de la cabeza hacia arriba y a los lados en rollos; ojos grises, cejas
# fruncidas, dos rayas naranjas en las mejillas y sonrisa
CHARS[K + 'winn-debreeze'] = {
    'body': 'normal', 'pal': pal('#8a7a40', '#f0b878', iris='#8a8a90', shade='#726432', deep='#584c24'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': (60, 50)},
    'front': [L(outline([(16, 64), (12, 40), (20, 20), (50, 10), (80, 20), (88, 40), (84, 64), (80, 50), (20, 50)]))]
             + _rolls('front', (138, 122, 64, 255), (100, 88, 42, 255))
             + [L(outline([(22, 86), (32, 84), (34, 90), (24, 92)]), ORANGE, 'f', False), L(outline([(78, 86), (68, 84), (66, 90), (76, 92)]), ORANGE, 'f', False)],
    'side': [L(outline([(70, 50), (86, 42), (88, 24), (70, 8), (40, 6), (16, 16), (4, 40), (8, 64), (20, 80), (34, 76), (40, 60), (54, 54)]))]
            + _rolls('side', (138, 122, 64, 255), (100, 88, 42, 255)),
    'back': [L(outline([(16, 76), (12, 44), (20, 20), (50, 10), (80, 20), (88, 44), (84, 76), (50, 84)]))] + _rolls('back', (138, 122, 64, 255), (100, 88, 42, 255)),
}

# Winston Windfall: grandullón adulto de cara ancha; pelo castaño rojizo corto arriba con dos alas grandes y peinadas hacia
# fuera a los lados de la cabeza; cejas fruncidas, nariz grande y boca seria
CHARS[K + 'winston-windfall'] = {
    'body': 'corpulento', 'pal': pal('#b04c1c', '#f0b070', shade='#923c12', deep='#702c0a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': (60, 44),
             'face_front': blob([(14, 50), (50, 40), (86, 50), (92, 78), (86, 102), (66, 112), (50, 114), (34, 112), (14, 102), (8, 78)])},
    'front': crop('front', top=8, side=60, w=2)
             + [L(outline([(16, 64), (2, 52), (-6, 30, 1), (8, 34), (14, 20), (24, 36)])), L(outline([(84, 64), (98, 52), (106, 30, 1), (92, 34), (86, 20), (76, 36)])),
                strand([(2, 40), (14, 52)], 'deep', 'b', 1.0), strand([(98, 40), (86, 52)], 'deep', 'b', 1.0)] + nose(89),
    'side': crop('side', top=8, w=2) + [L(outline([(24, 70), (4, 56), (-6, 32, 1), (10, 36), (20, 24), (34, 44)]))],
    'back': crop('back', top=8, w=2, nape=84) + [L(outline([(16, 68), (2, 54), (-6, 32, 1), (8, 36), (14, 22), (24, 40)])),
                                                 L(outline([(84, 68), (98, 54), (106, 32, 1), (92, 36), (86, 22), (76, 40)]))],
}

# Zak Wallside: piel morena; pelo verde azulado en un huevo altísimo y liso que le tapa hasta las cejas; ojos blancos
# redondos, coloretes y boca abierta de asombro
CHARS[K + 'zak-wallside'] = {
    'body': 'normal', 'pal': pal('#1e6a6c', '#c08a50', shade='#185658', deep='#104042'),
    'face': {'eyes': 'none', 'mouth': 'none', 'hairline': [(14, 68), (50, 64), (86, 68)]},
    'front': [L(outline([(16, 72), (12, 50), (14, 10), (28, -24), (50, -36), (72, -24), (86, 10), (88, 50), (84, 72), (80, 66), (20, 66)])),
              L(outline([(56, -32), (74, -20), (86, 12), (86, 66), (78, 60), (74, 20)]), 'shade', 'b', False),
              L(quad((12, 66), (50, 58), (88, 66)), 'deep', 'f', False, False, 1.4)]
             + white_eyes(76, 14, 6.4, 6.4, 2.6) + blush(86, (200, 120, 80, 255), 24, 5)
             + [L(ell(50, 96, 5, 7), (130, 80, 60, 255), 'f', ln=True), L(ell(50, 99, 3, 3), (180, 110, 90, 255), 'f', False)],
    'side': [L(outline([(78, 60), (90, 50), (92, 26), (84, -4), (64, -30), (40, -34), (18, -16), (6, 16), (2, 50), (10, 72), (24, 80), (36, 74), (40, 62), (60, 60)])),
             L(outline([(4, 36), (30, 40), (40, 60), (30, 76), (10, 70)]), 'shade', 'b', False)] + side_eye(76)
            + [L(ell(88, 96, 3, 5), (130, 80, 60, 255), 'f', ln=True)],
    'back': [L(outline([(16, 80), (12, 50), (14, 10), (28, -24), (50, -36), (72, -24), (86, 10), (88, 50), (84, 80), (50, 88)])),
             L(outline([(56, -32), (74, -20), (86, 12), (86, 78), (64, 86), (68, 20)]), 'shade', 'b', False)],
}

# Zane Laughead: pelo rosa malva con flequillo de lado y la melena corta que se abre en puntas hacia fuera a la altura de la
# mandíbula; ojos azules grandes y sonrisa
CHARS[K + 'zane-laughead'] = {
    'body': 'normal', 'pal': pal('#c4a4ac', '#f8d4a8', iris='#3a5a8a', shade='#a8888e', deep='#8a6a72'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(16, 88), (2, 98, 1), (6, 84), (4, 40), (16, 12), (50, 0), (84, 12), (96, 40), (94, 84), (98, 98, 1), (84, 88), (82, 60), (18, 60)])),
              L(outline([(60, 4), (86, 16), (96, 44), (94, 86), (84, 84), (82, 50)]), 'shade', 'b', False),
              fr([(14, 66), (16, 38), (32, 20), (56, 16), (78, 22), (86, 40), (86, 60), (74, 46), (58, 42), (44, 48), (32, 58), (24, 68, 1), (20, 60)]),
              strand([(30, 30), (56, 26), (76, 34)], 'deep', 'f', 1.0)],
    'side': [L(outline([(80, 50), (90, 40), (90, 20), (76, 2), (50, -4), (24, 2), (8, 20), (2, 50), (4, 80), (-4, 96, 1), (14, 90), (30, 92, 1), (40, 80), (50, 62),
                        (66, 58)])),
             L(outline([(2, 46), (30, 46), (46, 62), (36, 82), (14, 90)]), 'shade', 'b', False), fr([(70, 30), (90, 34), (92, 54, 1), (82, 48), (74, 46)])],
    'back': [L(outline([(16, 90), (2, 98, 1), (6, 84), (4, 40), (16, 12), (50, 0), (84, 12), (96, 40), (94, 84), (98, 98, 1), (84, 90), (50, 94)])),
             L(outline([(56, 4), (84, 12), (96, 40), (94, 84), (98, 96), (84, 90), (60, 92)]), 'shade', 'b', False)],
}

# Zin Giber: pelo oliva muy oscuro en una nube de rizos alta; cejas gruesas oliva, ojos blancos mirando de reojo, nariz
# ancha y labios gruesos
CHARS[K + 'zin-giber'] = {
    'body': 'normal', 'pal': pal('#4c4c22', '#f0b878', shade='#3c3c18', deep='#2c2c10'),
    'face': {'eyes': 'none', 'mouth': 'none', 'hairline': [(16, 62), (20, 48), (34, 44), (50, 50), (66, 44), (80, 48), (84, 62)]},
    'front': [L(outline([(16, 64), (12, 46), (84, 46), (84, 64), (50, 56)])), L(cloud(50, 14, 46, 40, 10, 0.3, 0.86)),
              L(blob([(60, -18), (80, -8), (92, 22), (86, 56), (74, 30)], 6), 'shade', 'b', False),
              L(quad((20, 6), (32, 0), (40, 8)), 'deep', 'b', False, False, 1.2), L(quad((56, -10), (66, -16), (74, -8)), 'deep', 'b', False, False, 1.2),
              L(quad((30, 30), (40, 24), (48, 32)), 'deep', 'b', False, False, 1.2), L(quad((60, 20), (70, 14), (78, 22)), 'deep', 'b', False, False, 1.2)]
             + white_eyes(77, 14, 6.4, 5.4, 2.0) + [L(ell(39, 77, 2.4, 2.6), OUTC, 'f', False), L(ell(67, 77, 2.4, 2.6), OUTC, 'f', False)]
             + brows(66, 'mid', 4.6, 15, 1.0) + [L([(44, 88), (42, 91), (50, 92), (58, 91), (56, 88)], (150, 90, 60, 255), 'f', False, False, 1.2),
                                                 L(blob([(38, 98), (50, 95), (62, 98), (58, 102), (42, 102)], 6), (150, 90, 60, 255), 'f', ln=True)],
    'side': [L(outline([(70, 50), (84, 42), (60, 40), (40, 50), (30, 76), (14, 72), (6, 50)])), L(cloud(46, 16, 46, 40, 10, 0.2, 0.86)),
             L(blob([(4, 30), (30, 40), (40, 60), (30, 76), (12, 66)], 6), 'shade', 'b', False)] + side_eye(77) + brow_side(66, 'mid', 4.6, 0.8),
    'back': [L(outline([(16, 80), (10, 50), (90, 50), (84, 80), (50, 88)])), L(cloud(50, 20, 48, 44, 10, 0.3, 0.86)),
             L(blob([(60, -18), (82, -6), (94, 24), (90, 60), (80, 80), (64, 84), (70, 30)], 6), 'shade', 'b', False)],
}
