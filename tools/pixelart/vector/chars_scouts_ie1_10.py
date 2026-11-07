"""Ojeadores de IE1 (scouts-ie1), tanda 10 (de rick-hatter a sean-lavender): dibujados a partir de su retrato de Victory Road
(casi ninguno tiene modelo 3D en la enciclopedia); claves 'scouts-ie1:<id>'. El perfil y la espalda están deducidos del
retrato (cómo cae cada peinado por detrás y de lado)."""
from chars import CHARS, L, OUTC, blob, ell, longhair, messy, outline, pal, rope, strand  # noqa: F401
from chars_vr_keizen_arashiyama import cloud, fr
from chars_vr_meiran_gakuin import bangs
from chars_vr_nikogawa import blush, brow_side, brows, crop, ring_glasses
from heads import quad  # noqa: F401

K = 'scouts-ie1:'
WHITE = (248, 248, 248, 255)
BROWN = (130, 70, 50, 255)
MOUTH = (120, 50, 40, 255)

# caras: larga de adulto, ancha y redonda de grandullón
LONG = blob([(18, 50), (50, 28), (82, 50), (84, 80), (76, 100), (62, 110), (50, 112), (38, 110), (24, 100), (16, 80)])
WIDE = blob([(15, 50), (50, 30), (85, 50), (90, 76), (85, 96), (66, 107), (50, 109), (34, 107), (15, 96), (10, 76)])


def skull(view='front'):
    """Calva: la parte de arriba de la cabeza en piel (de frente la cara sola acaba muy abajo)."""
    if view == 'front':
        return [L(outline([(17, 66), (13, 42), (22, 18), (50, 6), (78, 18), (87, 42), (83, 66), (50, 72)]), 'skin'),
                L(outline([(60, 9), (78, 20), (87, 44), (83, 64), (76, 40)]), 'skin_d', 'b', False)]
    return []


def C(pid, spec):
    CHARS[K + pid] = spec


def nose_tri(y=84, w=4, h=8, c=None):
    """Nariz grande de perfil triangular, vista de frente (un triángulo de piel con contorno)."""
    return [L([(50, y - h), (50 + w, y), (50 - w, y)], c or 'skin_d', 'f', False, True)]


def nose_line(y=86):
    return [L(quad((48, y - 8), (46, y), (51, y + 1)), OUTC, 'f', False, False, 1.1)]


def squint(ey=75, sep=14, w=6, up=True):
    """Ojos cerrados de felicidad (^ ^) o de sueño (u u)."""
    d = -4 if up else 4
    return [L(quad((cx - w, ey + 1), (cx, ey + d), (cx + w, ey + 1)), OUTC, 'f', False, False, 2.2) for cx in (50 - sep, 50 + sep)]


def marks(y=86, dx=27, c=BROWN):
    """Rayitas de las mejillas."""
    out = []
    for s in (-1, 1):
        x = 50 + s * dx
        out += [L([(x - 2, y - 1), (x + 2, y - 3)], c, 'f', False, False, 0.9), L([(x - 2, y + 2), (x + 2, y)], c, 'f', False, False, 0.9)]
    return out


def side_spikes(pts):
    return L(outline(pts))


# ---------------------------------------------------------------------------------------------------------------- 1-8

# Rick Hatter: melena roja revuelta hasta la mandíbula con la raya en medio, un pelo de punta arriba y mechones que le caen
# por los lados de la cara; piel morena, ojos verdes afilados y cejas enfadadas
C('rick-hatter', {
    'body': 'normal', 'pal': pal('#c4321a', '#c8844e', iris='#2e9a6a', shade='#9a2412', deep='#741a0c'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': False},
    'front': [L(outline([(4, 100, 1), (10, 86), (2, 76, 1), (8, 58), (8, 34), (20, 14), (40, 4), (50, 2), (52, -16, 1), (56, 3), (76, 8), (90, 26), (94, 50),
                         (92, 70), (98, 82, 1), (90, 88), (94, 100, 1), (80, 92), (80, 70), (20, 70), (20, 92)])),
              L(outline([(58, 4), (84, 16), (94, 48), (92, 80), (84, 70)]), 'shade', 'b', False),
              fr([(16, 88, 1), (12, 62), (14, 38), (26, 20), (44, 12), (50, 20), (56, 12), (74, 20), (86, 38), (88, 62), (84, 88, 1), (80, 70), (78, 56), (70, 44),
                  (58, 32), (52, 44, 1), (48, 32), (36, 42), (26, 56), (22, 70)]),
              strand([(32, 22), (26, 40)], 'deep', 'f', 1.0), strand([(68, 22), (74, 40)], 'deep', 'f', 1.0)],
    'side': [L(outline([(62, 52), (68, 40), (84, 36), (92, 22), (80, 6), (58, -2), (52, -16, 1), (46, -2), (24, 4), (8, 22), (2, 46), (-2, 70, 1), (4, 76),
                        (0, 96, 1), (14, 86), (22, 100, 1), (30, 84), (40, 80), (46, 66), (52, 56)])),
             L(outline([(4, 44), (30, 46), (40, 70), (30, 84), (14, 86)]), 'shade', 'b', False),
             fr([(76, 40), (90, 44), (92, 62, 1), (84, 52)])],
    'back': [L(outline([(6, 98, 1), (10, 80), (4, 62), (8, 32), (22, 10), (46, 0), (52, -16, 1), (56, 0), (78, 10), (92, 32), (96, 62), (90, 80), (94, 98, 1),
                        (78, 88), (70, 100, 1), (60, 88), (50, 100, 1), (40, 88), (30, 100, 1), (22, 88)])),
             L(outline([(58, 4), (84, 16), (96, 60), (92, 96), (66, 90)]), 'shade', 'b', False),
             strand([(50, 6), (50, 40)], 'deep', 'b', 1.0)],
})

# Ricky Charmers: pelo verde oscuro corto con tres pinchos altos en corona y patillas largas y finas hasta la mandíbula; cara
# larga, cejas verdes enfadadas, narizota y la boca abierta de morros
C('ricky-charmers', {
    'body': 'delgado', 'pal': pal('#24503e', '#f2c088', iris='#202020', shade='#1a3c2e', deep='#122a20'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'face_front': LONG, 'hairline': (60, 40)},
    'front': [L(outline([(19, 64), (16, 40), (22, 24), (8, 2, 1), (30, 16), (32, -6, 1), (44, 12), (50, -24, 1), (58, 12), (70, -4, 1), (72, 16), (94, 0, 1),
                         (80, 26), (84, 40), (81, 64), (78, 44), (22, 44)])),
              L(outline([(56, 10), (70, -4), (72, 16), (94, 0), (80, 26), (84, 42), (76, 30)]), 'shade', 'b', False),
              L([(17, 56), (16.2, 88)], 'mid', 'f', False, False, 2.2), L([(83, 56), (83.8, 88)], 'mid', 'f', False, False, 2.2)]
             + brows(64, 'mid', 4.5, 14, 1.0, 12) + nose_tri(88, 5, 12)
             + [L(blob([(40, 99), (50, 95), (60, 99), (58, 104), (50, 105), (42, 104)], 6), MOUTH, 'f', False, True)],
    'side': [L(outline([(70, 46), (80, 40), (84, 26), (96, 6, 1), (72, 12), (68, -8, 1), (54, 8), (44, -24, 1), (36, 8), (20, 2, 1), (14, 20), (4, 40), (8, 70),
                        (22, 82), (34, 78), (40, 64), (48, 56), (60, 50)])),
             L(outline([(4, 42), (30, 46), (40, 62), (34, 78), (22, 82), (8, 70)]), 'shade', 'b', False),
             L([(60, 54), (62, 84)], 'mid', 'f', False, False, 2.6)] + brow_side(64, 'mid', 4.5, 1.0),
    'back': [L(outline([(16, 76), (12, 44), (20, 22), (8, 0, 1), (30, 12), (34, -6, 1), (44, 10), (50, -22, 1), (58, 10), (68, -6, 1), (72, 12), (92, 0, 1),
                        (82, 24), (88, 44), (84, 76), (50, 82)])),
             L(outline([(56, 8), (82, 22), (88, 46), (84, 74), (62, 80)]), 'shade', 'b', False)],
})

# Ringo Spinning (portero): pelo corto granate oscuro con un moñito arriba atado con una goma celeste y el flequillo en picos;
# cejas gruesas, ojos pequeños y sonrisa
C('ringo-spinning', {
    'body': 'normal', 'pal': pal('#5e3a4c', '#f2b880', iris='#1e1a1a', shade='#482c3a', deep='#34202a', band='#8ad0dc'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    'front': [L(ell(50, 2, 9, 7)), L([(42, 9), (58, 9)], 'band', 'b', False, False, 3.0),
              L(outline([(14, 86, 1), (12, 60), (10, 36), (22, 14), (50, 4), (78, 14), (90, 36), (88, 60), (86, 86, 1), (80, 66), (20, 66)])),
              L(outline([(58, 6), (82, 16), (90, 40), (86, 80), (80, 52)]), 'shade', 'b', False),
              bangs(60, 16, 84, 5, 24, jag=8), strand([(40, 10), (36, 30)], 'deep', 'f', 1.0), strand([(60, 10), (64, 30)], 'deep', 'f', 1.0)]
             + brows(64, OUTC, 3.0, 14, 1.0, 11) + marks(84, 26),
    'side': [L(ell(50, 0, 7, 7)), L([(44, 8), (56, 8)], 'band', 'b', False, False, 3.0),
             L(outline([(64, 56), (72, 44), (86, 42), (92, 24), (78, 8), (50, 2), (24, 8), (8, 26), (2, 50), (6, 78), (18, 92, 1), (26, 80), (36, 76), (42, 62), (50, 58)])),
             L(outline([(4, 46), (30, 48), (40, 62), (30, 80), (14, 86)]), 'shade', 'b', False),
             fr([(76, 42), (90, 42), (92, 58, 1), (84, 52)])] + brow_side(64, OUTC, 3.0, 1.0),
    'back': [L(ell(50, 2, 9, 7)), L([(42, 9), (58, 9)], 'band', 'b', False, False, 3.0),
             L(outline([(14, 86, 1), (10, 60), (10, 36), (22, 14), (50, 4), (78, 14), (90, 36), (90, 60), (86, 86, 1), (70, 88), (50, 92), (30, 88)])),
             L(outline([(58, 6), (82, 16), (90, 40), (88, 84), (64, 88)]), 'shade', 'b', False),
             strand([(50, 10), (50, 50)], 'deep', 'b', 1.0)],
})

# Ringo Stagg: pelo castaño en pinchos grandes que salen hacia todos lados, flequillo en picos hasta los ojos y dos mechones
# largos y finos que le caen por delante de las orejas hasta la barbilla; ojos redondos, cejas enfadadas y morros
C('ringo-stagg', {
    'body': 'normal', 'pal': pal('#8a5222', '#f4c494', iris='#1e1a1a', shade='#6c3e18', deep='#4e2c10'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': False},
    'front': messy('front', amp=22, n=9, seed=7, rx=46, ry=40, cy=40, lo=66)
             + [L(outline([(18, 60), (12, 92), (14, 106, 1), (20, 92), (24, 66)])), L(outline([(82, 60), (88, 92), (86, 106, 1), (80, 92), (76, 66)])),
                fr([(16, 66), (12, 44), (26, 26), (50, 20), (74, 26), (88, 44), (84, 66), (76, 56), (70, 64, 1), (64, 52), (56, 62, 1), (50, 50), (44, 62, 1),
                    (36, 52), (30, 64, 1), (24, 56)]),
                strand([(40, 28), (36, 46)], 'deep', 'f', 1.0), strand([(62, 28), (66, 46)], 'deep', 'f', 1.0)],
    'side': messy('side', amp=22, n=9, seed=7, rx=46, ry=40, cy=40) + [L(outline([(70, 56), (72, 90), (68, 104, 1), (66, 88), (64, 58)]), 'mid', 'f')],
    'back': messy('back', amp=22, n=9, seed=7, rx=46, ry=40, cy=40),
})

# Rip Airman: adulto de cara larga y narizota; pelo gris malva corto peinado hacia arriba en punta y los lados cortos; ojos
# entornados con sonrisa ladina
C('rip-airman', {
    'body': 'delgado', 'pal': pal('#a08c98', '#fad6a8', iris='#4a4a66', shade='#80707a', deep='#5e5058'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 99, 'face_front': LONG, 'hairline': (62, 44)},
    'front': [L(outline([(18, 66), (14, 42), (20, 20), (38, 8), (50, 2, 1), (62, 8), (80, 20), (86, 42), (82, 66), (78, 46), (22, 46)])),
              L(outline([(56, 6), (78, 18), (86, 42), (82, 62), (74, 34)]), 'shade', 'b', False),
              strand([(50, 4), (50, 30)], 'deep', 'b', 1.0), strand([(36, 12), (32, 32)], 'deep', 'b', 1.0), strand([(64, 12), (68, 32)], 'deep', 'b', 1.0)]
             + brows(66, OUTC, 2.0, 14, 1.5, 10) + nose_tri(90, 4, 16),
    'side': [L(outline([(70, 46), (80, 38), (84, 22), (72, 8), (56, 0, 1), (36, 2), (16, 12), (6, 34), (8, 64), (22, 80), (34, 76), (40, 62), (50, 52)])),
             L(outline([(6, 40), (30, 42), (40, 62), (34, 76), (22, 80), (8, 64)]), 'shade', 'b', False)] + brow_side(66, OUTC, 2.0, 1.5),
    'back': [L(outline([(16, 76), (12, 42), (20, 20), (38, 8), (50, 2, 1), (62, 8), (80, 20), (88, 42), (84, 76), (50, 82)])),
             L(outline([(56, 6), (78, 18), (88, 44), (84, 74), (62, 80)]), 'shade', 'b', False), strand([(50, 4), (50, 50)], 'deep', 'b', 1.0)],
})

# Rip Winkle: bajito de pelo verde oliva oscuro recogido arriba en un penacho de pinchos (como una palmera) con una goma verde
# y el flequillo en picos; cejas gruesas, nariz redonda naranja, rayitas en las mejillas y sonrisa
C('rip-winkle', {
    'body': 'bajito', 'pal': pal('#5c5426', '#f2a868', iris='#1e1a1a', shade='#46401c', deep='#302c12', band='#6ab84a', nose='#f07838'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'nose': (50, 85, 3.0), 'hairline': False},
    'front': [L(outline([(50, 6), (30, -2), (16, -18, 1), (36, -10), (34, -30, 1), (46, -14), (52, -36, 1), (58, -14), (70, -30, 1), (66, -10), (86, -18, 1),
                         (72, -2)])),
              L([(42, 6), (58, 6)], 'band', 'b', False, False, 3.0),
              L(outline([(14, 70), (12, 40), (22, 16), (50, 6), (78, 16), (88, 40), (86, 70), (80, 56), (20, 56)])),
              L(outline([(58, 8), (80, 18), (88, 42), (84, 64), (78, 40)]), 'shade', 'b', False),
              fr([(14, 66), (12, 42), (24, 22), (50, 14), (76, 22), (88, 42), (86, 66), (80, 52), (72, 60, 1), (64, 46), (54, 58, 1), (48, 44), (40, 58, 1), (34, 46),
                  (26, 60, 1), (20, 52)])]
             + brows(63, 'deep', 5.5, 14, 1.0, 13) + marks(86, 26),
    'side': [L(outline([(52, 4), (38, -6), (30, -24, 1), (48, -12), (56, -32, 1), (60, -12), (74, -24, 1), (66, -2)])), L([(46, 4), (60, 4)], 'band', 'b', False, False, 3.0),
             L(outline([(64, 56), (72, 44), (86, 42), (92, 26), (80, 10), (52, 4), (26, 10), (8, 28), (2, 50), (6, 70), (20, 82), (34, 78), (40, 64), (50, 58)])),
             L(outline([(4, 46), (30, 48), (40, 64), (34, 78), (20, 82), (6, 70)]), 'shade', 'b', False),
             fr([(76, 42), (92, 40), (92, 56, 1), (84, 50)])] + brow_side(63, 'deep', 5.5, 1.0),
    'back': [L(outline([(50, 6), (30, -2), (16, -18, 1), (36, -10), (34, -30, 1), (46, -14), (52, -36, 1), (58, -14), (70, -30, 1), (66, -10), (86, -18, 1),
                        (72, -2)])),
             L([(42, 6), (58, 6)], 'band', 'b', False, False, 3.0),
             L(outline([(14, 80), (10, 40), (22, 16), (50, 6), (78, 16), (90, 40), (86, 80), (50, 86)])),
             L(outline([(58, 8), (80, 18), (90, 42), (86, 78), (62, 84)]), 'shade', 'b', False)],
})

# Rob Anchor: piel morena; melena de seta gris malva con las puntas hacia fuera a la altura de la mandíbula y un flequillo de
# lado que le tapa la frente; ojos cerrados de felicidad (^ ^), nariz naranja y sonrisita
C('rob-anchor', {
    'body': 'normal', 'pal': pal('#9a7c8a', '#c8844c', iris='#1e1a1a', shade='#7a606c', deep='#5c4650', nose='#f08030'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'nose': (50, 86, 2.6), 'hairline': False},
    'front': [L(outline([(-4, 92, 1), (4, 82), (8, 50), (14, 20), (36, 4), (60, 2), (82, 14), (94, 40), (96, 80), (104, 92, 1), (86, 90), (82, 66), (18, 66), (14, 90)])),
              L(outline([(60, 4), (84, 16), (96, 44), (98, 86), (86, 82), (84, 50)]), 'shade', 'b', False),
              fr([(12, 76), (10, 44), (22, 20), (46, 10), (72, 14), (88, 32), (90, 58), (84, 50), (70, 42), (52, 44), (36, 54), (24, 64)]),
              strand([(30, 20), (24, 50)], 'deep', 'f', 1.0), strand([(56, 16), (60, 40)], 'deep', 'f', 1.0)] + squint(76),
    'side': [L(outline([(66, 54), (76, 44), (90, 40), (94, 26), (80, 8), (54, 0), (26, 6), (8, 24), (2, 50), (2, 80), (-6, 92, 1), (14, 90), (30, 88), (40, 70),
                        (50, 60)])),
             L(outline([(4, 46), (34, 50), (40, 70), (30, 88), (6, 88)]), 'shade', 'b', False),
             fr([(74, 42), (92, 38), (94, 58, 1), (84, 52)]), L(quad((76, 76), (80, 73), (84, 76)), OUTC, 'f', False, False, 2.0)],
    'back': [L(outline([(-4, 92, 1), (4, 80), (6, 46), (16, 18), (50, 2), (84, 18), (94, 46), (96, 80), (104, 92, 1), (80, 92), (50, 94), (20, 92)])),
             L(outline([(58, 4), (84, 18), (96, 50), (98, 88), (66, 92)]), 'shade', 'b', False)],
})

# Rob Burnsides: pelo rubio ocre rizado, un casquete de rizos arriba y dos matas de rizos abultadas a los lados detrás de las
# orejas; ojos redondos de punto, una ceja levantada y rayitas en las mejillas
C('rob-burnsides', {
    'body': 'normal', 'pal': pal('#d8a022', '#d49a5e', iris='#1e1a1a', shade='#b07e18', deep='#8a5e10'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (60, 44)},
    'front': [L(cloud(14, 82, 12, 16, 5, 0.3)), L(cloud(86, 82, 12, 16, 5, 0.6)),
              L(cloud(50, 28, 40, 28, 9, 0.2)), L(outline([(16, 64), (14, 40), (86, 40), (84, 64), (80, 46), (20, 46)])),
              L(cloud(62, 22, 22, 16, 6, 0.4), 'shade', 'b', False), L(cloud(40, 18, 10, 8, 4), 'light', 'b', False)] + marks(86, 26),
    'side': [L(cloud(28, 80, 16, 18, 6, 0.3)), L(cloud(44, 30, 42, 30, 9, 0.2)),
             L(outline([(70, 48), (82, 40), (86, 26), (50, 10), (10, 40), (20, 70), (36, 66), (48, 56)])),
             L(cloud(24, 74, 10, 10, 4), 'shade', 'b', False)],
    'back': [L(cloud(16, 82, 14, 16, 5, 0.3)), L(cloud(84, 82, 14, 16, 5, 0.6)), L(cloud(50, 50, 30, 30, 8)), L(cloud(50, 30, 42, 30, 9, 0.2)),
             L(cloud(62, 40, 24, 24, 6, 0.4), 'shade', 'b', False)],
})

# ---------------------------------------------------------------------------------------------------------------- 9-16

# Rob Freeby: cara regordeta; pelo morado oscuro en pinchos echados hacia su izquierda, con un mechón largo que le cae por el
# lado izquierdo de la cara (la derecha de la imagen) hasta la mandíbula; ojos entornados y sonrisa
C('rob-freeby', {
    'body': 'normal', 'pal': pal('#4a3a6a', '#eaa868', iris='#1e1a1a', shade='#382c52', deep='#261e3a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'face_front': WIDE, 'hairline': False},
    'front': [L(outline([(12, 70), (2, 50, 1), (12, 40), (-2, 18, 1), (20, 18), (18, -2, 1), (40, 6), (52, -10, 1), (62, 4), (96, -4, 1), (84, 14), (102, 26, 1),
                         (90, 34), (94, 60), (86, 70), (80, 56), (20, 56)])),
              L(outline([(60, 4), (94, -2), (84, 16), (100, 26), (90, 36), (92, 60), (82, 40)]), 'shade', 'b', False),
              fr([(14, 60), (14, 40), (30, 22), (56, 14), (80, 20), (90, 36), (92, 60), (90, 96, 1), (82, 70), (76, 48), (64, 34), (50, 38), (36, 44), (24, 54)]),
              strand([(60, 22), (82, 44), (86, 70)], 'deep', 'f', 1.0), strand([(44, 22), (30, 36)], 'deep', 'f', 1.0)]
             + marks(84, 26),
    'side': [L(outline([(66, 52), (74, 42), (90, 34), (102, 24, 1), (88, 16), (98, 0, 1), (72, 6), (60, -10, 1), (46, 2), (24, 0, 1), (16, 14), (2, 28, 1), (6, 40),
                        (2, 60), (14, 78), (30, 76), (40, 62), (50, 56)])),
             L(outline([(4, 46), (30, 48), (40, 62), (30, 76), (14, 78)]), 'shade', 'b', False),
             fr([(74, 40), (92, 40), (94, 70, 1), (84, 54)])],
    'back': [L(outline([(12, 78), (2, 52, 1), (12, 42), (-2, 18, 1), (20, 18), (18, -2, 1), (40, 6), (52, -10, 1), (62, 4), (96, -4, 1), (84, 14), (102, 26, 1),
                        (90, 34), (96, 56, 1), (88, 78), (50, 84)])),
             L(outline([(60, 4), (94, -2), (84, 16), (100, 26), (90, 36), (88, 76), (64, 82)]), 'shade', 'b', False)],
})

# Rob Observer-Zervatory: adulto de cara larga; pelo rubio crema corto y ondulado con raya a un lado; ojos redondos pequeños
# con las cejas levantadas, nariz larga y sonrisa
C('rob-observer-zervatory', {
    'body': 'delgado', 'pal': pal('#e6dca2', '#f8d6a2', iris='#1e1a1a', shade='#c4b882', deep='#a09460'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'smile', 'mouth_y': 100, 'face_front': LONG, 'hairline': [(17, 66), (18, 50), (30, 44), (44, 46), (54, 40), (70, 42), (83, 50), (84, 66)]},
    'front': [L(outline([(16, 68), (12, 44), (16, 22), (34, 6), (56, 4), (76, 10), (88, 28), (88, 50), (84, 68), (80, 50), (20, 50)])),
              L(outline([(58, 6), (80, 14), (90, 40), (84, 64), (76, 36)]), 'shade', 'b', False),
              strand([(44, 8), (40, 30)], 'deep', 'b', 1.0), strand([(62, 8), (66, 26)], 'deep', 'b', 1.0)] + nose_line(90),
    'side': [crop('side', top=2, nape=82)[0], crop('side', top=2, nape=82)[1], fr([(72, 44), (88, 38), (90, 52, 1), (82, 48)])],
    'back': crop('back', top=4, nape=82),
})

# Rob Ottley: pelo azul petróleo en mechones de punta echados hacia arriba y a un lado, con el flequillo cayendo en picos;
# gafas redondas negras, cejas finas y sonrisa
C('rob-ottley', {
    'body': 'normal', 'pal': pal('#3c7088', '#f8d0a0', iris='#2a2420', shade='#2c5468', deep='#1e3c4c'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 93, 'hairline': False},
    'front': [L(outline([(16, 70), (8, 44), (14, 20), (6, 2, 1), (28, 6), (34, -10, 1), (50, 0), (66, -12, 1), (72, 4), (96, 6, 1), (86, 20), (92, 44), (86, 70),
                         (80, 56), (20, 56)])),
              L(outline([(60, 2), (94, 8), (86, 22), (92, 44), (86, 66), (80, 40)]), 'shade', 'b', False),
              fr([(14, 64), (12, 42), (26, 24), (50, 16), (74, 22), (88, 40), (86, 64), (80, 52), (74, 58, 1), (66, 42), (58, 60, 1), (52, 40), (44, 58, 1), (38, 44),
                  (28, 58, 1), (22, 50)])]
             + ring_glasses('front', 76, (30, 26, 26, 255), 2.4, 9.5, 7.5, 14),
    'side': [L(outline([(66, 54), (74, 44), (88, 40), (98, 24, 1), (84, 18), (90, 2, 1), (70, 4), (66, -12, 1), (52, 0), (30, -6, 1), (24, 10), (8, 22), (2, 46),
                        (8, 70), (20, 82), (34, 78), (40, 62), (50, 56)])),
             L(outline([(4, 46), (30, 48), (40, 62), (34, 78), (20, 82), (8, 70)]), 'shade', 'b', False),
             fr([(74, 42), (92, 40), (92, 60, 1), (84, 52)])] + ring_glasses('side', 76, (30, 26, 26, 255), 2.4, 9.5, 7.5),
    'back': [L(outline([(14, 80), (8, 46), (14, 20), (6, 2, 1), (28, 6), (34, -10, 1), (50, 0), (66, -12, 1), (72, 4), (96, 6, 1), (86, 20), (92, 46), (86, 80),
                        (50, 86)])),
             L(outline([(60, 2), (94, 8), (86, 22), (92, 46), (86, 78), (64, 84)]), 'shade', 'b', False)],
})

# Rob Ottman (portero): pelo verde azulado con un mechón largo y lacio que le tapa el ojo izquierdo (la derecha de la imagen)
# y pinchos por detrás; un ojo redondo enorme con la ceja negra gruesa y la boca torcida
C('rob-ottman', {
    'body': 'normal', 'pal': pal('#3a8a7e', '#e8a868', iris='#1e1a1a', shade='#2c6c62', deep='#1e4e46'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(14, 70), (8, 44), (14, 22), (10, 4, 1), (30, 10), (40, -6, 1), (54, 4), (80, -8, 1), (78, 10), (96, 18, 1), (88, 30), (92, 56), (86, 70),
                         (80, 56), (20, 56)])),
              L(outline([(56, 4), (80, -6), (78, 12), (94, 20), (88, 32), (90, 56), (80, 40)]), 'shade', 'b', False),
              fr([(14, 60), (14, 40), (30, 24), (52, 16), (76, 22), (88, 40), (90, 70), (86, 96, 1), (80, 82), (72, 96, 1), (64, 70), (56, 48), (42, 44), (26, 52)]),
              strand([(58, 24), (70, 50), (80, 84)], 'deep', 'f', 1.0),
              L(ell(36, 76, 5.4, 6), WHITE, 'f', False, True), L(ell(36.5, 76.5, 3, 3.4), OUTC, 'f', False),
              L(blob([(26, 66), (36, 62), (46, 66), (44, 69), (36, 66), (28, 69)], 6), OUTC, 'f', False)],
    'side': [L(outline([(66, 52), (74, 42), (90, 36), (100, 20, 1), (84, 14), (82, -6, 1), (62, 4), (42, -6, 1), (32, 8), (12, 4, 1), (10, 20), (2, 40), (6, 66),
                        (18, 80), (32, 76), (40, 62), (50, 56)])),
             L(outline([(4, 44), (30, 46), (40, 62), (32, 76), (18, 80), (6, 66)]), 'shade', 'b', False),
             fr([(72, 40), (92, 40), (94, 96, 1), (84, 70), (80, 52)])],
    'back': [L(outline([(14, 80), (8, 46), (14, 22), (10, 4, 1), (30, 10), (40, -6, 1), (54, 4), (80, -8, 1), (78, 10), (96, 18, 1), (88, 30), (92, 50), (86, 80),
                        (50, 86)])),
             L(outline([(56, 4), (80, -6), (78, 12), (94, 20), (88, 32), (88, 78), (64, 84)]), 'shade', 'b', False)],
})

# Robin Catching (portero): gorra crema con una corona dorada y la visera azul verdoso; pelo castaño corto por debajo; tiritas
# blancas en las mejillas, ojos lilas y sonrisa
C('robin-catching', {
    'body': 'normal', 'pal': pal('#6a4630', '#eaa868', iris='#8a7aa0', shade='#52362a', deep='#3a261c', cap='#f4ecbc', cap_d='#d4ca98', brim='#4a8090',
                                 gold='#d8aa2a', tape='#f4ecc4'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': (62, 56)},
    'front': [L(outline([(16, 70), (14, 56), (86, 56), (84, 70), (80, 60), (20, 60)])),
              L(outline([(14, 54), (14, 30), (24, 12), (50, 2), (76, 12), (86, 30), (86, 54)]), 'cap', 'f'),
              L(outline([(60, 4), (78, 14), (86, 32), (86, 52), (76, 50)]), 'cap_d', 'f', False),
              L(outline([(36, 40), (36, 24), (43, 32), (50, 20), (57, 32), (64, 24), (64, 40)]), 'gold', 'f', False, True),
              L(ell(50, 0, 4, 2.6), 'brim', 'f', ln=True),
              L(outline([(6, 60), (14, 50), (50, 46), (86, 50), (94, 60), (50, 58)]), 'brim', 'f'),
              L(blob([(31, 84), (39, 83), (40, 88), (32, 89)], 4), 'tape', 'f', False, True), L(blob([(61, 83), (69, 84), (68, 89), (60, 88)], 4), 'tape', 'f', False, True)],
    'side': [L(outline([(54, 62), (60, 54), (40, 54), (8, 50), (4, 70), (16, 82), (32, 78), (40, 66)])),
             L(outline([(6, 52), (8, 26), (24, 8), (52, 2), (76, 10), (88, 28), (88, 50), (40, 52)]), 'cap', 'f'),
             L(outline([(8, 50), (8, 30), (22, 14), (30, 30), (30, 50)]), 'cap_d', 'f', False),
             L(outline([(70, 48), (88, 46), (106, 54), (104, 58), (86, 56), (68, 54)]), 'brim', 'f'),
             L(blob([(78, 84), (85, 83), (85, 88), (78, 89)], 4), 'tape', 'f', False, True)],
    'back': [L(outline([(16, 82), (12, 56), (88, 56), (84, 82), (50, 86)])),
             L(outline([(12, 58), (12, 30), (24, 12), (50, 2), (76, 12), (88, 30), (88, 58)]), 'cap', 'f'),
             L(outline([(58, 4), (78, 14), (88, 32), (88, 56), (70, 56)]), 'cap_d', 'f', False),
             L(outline([(40, 56), (40, 48), (60, 48), (60, 56)]), 'brim', 'f', False, True), L(ell(50, 0, 4, 2.6), 'brim', 'f', ln=True)],
})

# Robin Cruise (portero): piel morena; melena gris parda enorme en pinchos revueltos con un moñito de pinchos arriba; ojos
# grandes, cejas enfadadas y sonrisa
C('robin-cruise', {
    'body': 'normal', 'pal': pal('#8a7c64', '#b4744a', iris='#1e1a1a', shade='#6c604c', deep='#4e4436'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': messy('front', amp=18, n=12, seed=3, rx=52, ry=42, cy=46, lo=70)
             + [L(outline([(50, 8), (38, 0), (34, -14, 1), (44, -6), (50, -18, 1), (56, -6), (66, -14, 1), (62, 0)])),
                fr([(14, 72), (10, 50), (24, 30), (50, 24), (76, 30), (90, 50), (86, 72), (80, 60), (72, 66, 1), (66, 52), (56, 60, 1), (50, 46), (44, 60, 1),
                    (34, 52), (28, 66, 1), (20, 60)]),
                strand([(40, 28), (36, 46)], 'deep', 'f', 1.0), strand([(62, 28), (66, 46)], 'deep', 'f', 1.0)],
    'side': messy('side', amp=18, n=12, seed=3, rx=50, ry=42, cy=44) + [L(outline([(50, 8), (40, -10, 1), (52, -4), (58, -16, 1), (60, 4)]))],
    'back': messy('back', amp=18, n=12, seed=3, rx=52, ry=42, cy=46) + [L(outline([(50, 8), (38, 0), (34, -14, 1), (44, -6), (50, -18, 1), (56, -6), (66, -14, 1),
                                                                               (62, 0)]))],
})

# Robin Sherwood: grandullón de cara ancha; un pañuelo azul grisáceo atado en la cabeza con dos cordones naranjas cruzados
# arriba; el flequillo naranja asoma por delante en picos; ceño fruncido
C('robin-sherwood', {
    'body': 'corpulento', 'pal': pal('#e8782a', '#f2b070', iris='#1e1a1a', shade='#c05e1c', deep='#984812', cloth='#4a6680', cloth_d='#36506a', rope='#e07a24'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'face_front': WIDE, 'hairline': False, 'ear_out': 4, 'big_ears': 1},
    'front': [L(outline([(14, 54), (14, 34), (26, 16), (50, 10), (74, 16), (86, 34), (86, 54), (50, 50)]), 'cloth'),
              L(outline([(60, 12), (78, 18), (86, 36), (86, 52), (72, 50)]), 'cloth_d', 'b', False),
              L(quad((26, 18), (30, -12), (44, -6)), 'rope', 'f', False, False, 5.0), L(quad((74, 18), (70, -12), (56, -6)), 'rope', 'f', False, False, 5.0),
              L(quad((34, 12), (50, -18), (66, 12)), 'rope', 'f', False, False, 5.0), L(ell(50, 4, 9, 6), 'cloth', 'f', ln=True),
              fr([(16, 50), (30, 44), (50, 42), (70, 44), (84, 50), (76, 58, 1), (68, 52), (60, 62, 1), (54, 52), (46, 60, 1), (40, 52), (30, 58, 1), (24, 52)])] + nose_tri(88, 4, 10),
    'side': [L(outline([(64, 52), (80, 44), (88, 30), (76, 14), (50, 8), (24, 12), (8, 30), (4, 52), (10, 72), (24, 76), (40, 62), (50, 54)]), 'cloth'),
             L(outline([(6, 40), (30, 44), (40, 62), (24, 76), (10, 72)]), 'cloth_d', 'b', False),
             L(quad((34, 14), (44, -16), (60, 8)), 'rope', 'f', False, False, 5.0), L(ell(48, 4, 8, 6), 'cloth', 'f', ln=True),
             fr([(78, 44), (92, 42), (92, 58, 1), (84, 52)])],
    'back': [L(outline([(14, 74), (12, 36), (26, 16), (50, 10), (74, 16), (88, 36), (86, 74), (50, 80)]), 'cloth'),
             L(outline([(58, 12), (78, 18), (88, 40), (86, 72), (64, 78)]), 'cloth_d', 'b', False),
             L(quad((26, 18), (30, -12), (44, -6)), 'rope', 'f', False, False, 5.0), L(quad((74, 18), (70, -12), (56, -6)), 'rope', 'f', False, False, 5.0),
             L(quad((34, 12), (50, -18), (66, 12)), 'rope', 'f', False, False, 5.0), L(ell(50, 4, 9, 6), 'cloth', 'f', ln=True)],
})

# Rocky Rollans: melena lisa naranja rojiza hasta la mandíbula con la raya en medio, que le enmarca la cara; ojos afilados y
# ceño serio
C('rocky-rollans', {
    'body': 'normal', 'pal': pal('#c24c1c', '#f6c69a', iris='#7a4a5a', shade='#9a3a14', deep='#742a0e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': False},
    'front': longhair('front', length=96, flare=2, top=0, part=True, ends=4)
             + [fr([(18, 96, 1), (14, 70), (14, 40), (26, 18), (48, 10), (50, 22), (52, 10), (74, 18), (86, 40), (86, 70), (82, 96, 1), (78, 76), (78, 54), (66, 36),
                    (54, 30), (50, 38), (46, 30), (34, 36), (22, 54), (22, 76)]),
                strand([(34, 24), (22, 60)], 'deep', 'f', 1.0), strand([(66, 24), (78, 60)], 'deep', 'f', 1.0)],
    'side': longhair('side', length=96, flare=2) + [fr([(74, 40), (90, 40), (92, 60, 1), (84, 52)])],
    'back': longhair('back', length=96, flare=2, part=True, ends=4),
})

# ---------------------------------------------------------------------------------------------------------------- 17-24

# Rocky Shears (portero): grandullón adulto de cara cuadrada y ancha; pelo gris morado rapado arriba; ojos blancos de pupila
# pequeña muy enfadados, arrugas y una boca recta larguísima
C('rocky-shears', {
    'body': 'corpulento', 'pal': pal('#8a7a9a', '#f0b070', iris='#1e1a1a', shade='#6e6080', deep='#524866'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': WIDE, 'hairline': (52, 36)},
    'front': crop('front', top=12, side=54, w=-2, flat=8)
             + [L([(26, 72), (44, 76), (40, 80), (28, 79)], WHITE, 'f', False, True), L([(74, 72), (56, 76), (60, 80), (72, 79)], WHITE, 'f', False, True),
                L(ell(38, 77, 1.6, 1.8), OUTC, 'f', False), L(ell(62, 77, 1.6, 1.8), OUTC, 'f', False),
                L([(22, 66), (44, 72)], OUTC, 'f', False, False, 3.0), L([(78, 66), (56, 72)], OUTC, 'f', False, False, 3.0),
                L([(24, 96), (76, 96)], OUTC, 'f', False, False, 1.6), L(quad((28, 86), (32, 92), (26, 96)), BROWN, 'f', False, False, 1.0),
                L(quad((72, 86), (68, 92), (74, 96)), BROWN, 'f', False, False, 1.0)] + nose_line(88),
    'side': crop('side', top=10, nape=80, flat=8) + [L([(72, 66), (86, 72)], OUTC, 'f', False, False, 3.0), L([(76, 75), (86, 77)], OUTC, 'f', False, False, 2.0),
                                                    L([(70, 96), (86, 96)], OUTC, 'f', False, False, 1.6)],
    'back': crop('back', top=12, nape=78, flat=8),
})

# Rod Entwhistle (portero): pelo azul petróleo liso con mechones largos que le caen por los lados de la cara hasta la mandíbula
# y el flequillo de lado; ojos verdes grandes, un arañazo en la frente y media sonrisa
C('rod-entwhistle', {
    'body': 'normal', 'pal': pal('#4a8ea8', '#f2c08e', iris='#4a9a3a', shade='#3a7088', deep='#2a5266'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(10, 100, 1), (8, 70), (8, 40), (18, 14), (40, 2), (64, 2), (84, 14), (92, 40), (92, 70), (90, 100, 1), (82, 80), (82, 62), (18, 62), (18, 80)])),
              L(outline([(62, 4), (84, 16), (92, 44), (90, 92), (84, 66)]), 'shade', 'b', False),
              fr([(14, 96, 1), (12, 60), (16, 34), (32, 16), (56, 12), (78, 20), (88, 38), (88, 60), (86, 96, 1), (80, 70), (76, 50), (66, 38), (56, 50, 1), (50, 36),
                  (36, 46), (26, 60), (20, 76)]),
              strand([(40, 18), (28, 44)], 'deep', 'f', 1.0), strand([(64, 18), (78, 50)], 'deep', 'f', 1.0),
              L([(54, 58), (57, 52), (56, 48)], BROWN, 'f', False, False, 0.9), L([(30, 84), (31, 86)], BROWN, 'f', False, False, 1.2)],
    'side': [L(outline([(66, 54), (76, 42), (90, 38), (92, 22), (78, 6), (52, 0), (26, 6), (8, 24), (2, 50), (4, 80), (10, 96, 1), (20, 86), (34, 80), (40, 64),
                        (50, 58)])),
             L(outline([(4, 46), (30, 48), (40, 64), (34, 80), (10, 92)]), 'shade', 'b', False),
             fr([(72, 40), (90, 40), (92, 96, 1), (84, 72), (80, 52)])],
    'back': longhair('back', length=94, flare=0, ends=5),
})

# Rod Headstock (portero): calvo con un penacho amarillo corto y tieso en lo alto como una brocha; antifaz verde con una uve
# roja encima de los ojos; sonrisa
C('rod-headstock', {
    'body': 'normal', 'pal': pal('#e2c034', '#f2b474', iris='#1e1a1a', shade='#c09e24', deep='#9a7c16', mask='#5aa84a', mask_d='#3c8034', vee='#d8321e',
                                 lens='#f4ecd0'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': skull() + [L(outline([(38, 12), (34, -8), (36, -16), (50, -20), (64, -16), (66, -8), (62, 12)])),
              L(outline([(54, -18), (64, -16), (66, -8), (62, 10), (58, -4)]), 'shade', 'b', False),
              strand([(43, -14), (43, 8)], 'deep', 'b', 1.0), strand([(50, -16), (50, 10)], 'deep', 'b', 1.0), strand([(57, -14), (57, 8)], 'deep', 'b', 1.0),
              L(outline([(14, 66), (16, 76), (30, 86), (44, 82), (50, 76), (56, 82), (70, 86), (84, 76), (86, 66), (70, 62), (50, 66), (30, 62)]), 'mask', 'f', ln=True),
              L(outline([(26, 68), (40, 72), (42, 80), (30, 80)]), 'lens', 'f', False, True), L(outline([(74, 68), (60, 72), (58, 80), (70, 80)]), 'lens', 'f', False, True),
              L(outline([(10, 56), (28, 54), (50, 70, 1), (72, 54), (90, 56), (86, 66), (70, 62), (50, 74, 1), (30, 62), (14, 66)]), 'vee', 'f', ln=True)],
    'side': [L(outline([(42, 24), (40, 4), (46, -4), (60, -4), (64, 4), (60, 24)])), strand([(51, -2), (51, 22)], 'deep', 'b', 1.0),
             L(outline([(62, 66), (86, 64), (88, 80), (74, 84), (62, 76)]), 'mask', 'f', ln=True),
             L(outline([(60, 58), (84, 54), (90, 60), (88, 66), (62, 68)]), 'vee', 'f', ln=True),
             L(outline([(72, 68), (86, 68), (86, 78), (74, 78)]), 'lens', 'f', False, True)],
    'back': [L(outline([(38, 24), (34, 0), (36, -8), (50, -12), (64, -8), (66, 0), (62, 24)])), strand([(50, -10), (50, 20)], 'deep', 'b', 1.0),
             L([(14, 62), (86, 62)], 'mask', 'f', False, False, 4.0)],
})

# Rod Opsin: grandullón de piel morena; pelo rosa malva abultado en bloque con el borde ondulado; ojos entornados, narizota
# redonda y sonrisa de lado
C('rod-opsin', {
    'body': 'corpulento', 'pal': pal('#c8a0a8', '#a07858', iris='#1e1a1a', shade='#a8808a', deep='#86626c', nose='#8a6448'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'face_front': WIDE, 'nose': (50, 88, 6), 'hairline': (56, 46)},
    'front': [L(cloud(50, 30, 44, 30, 10, 0.1, 0.92)), L(outline([(12, 62), (10, 40), (90, 40), (88, 62), (84, 50), (16, 50)])),
              L(cloud(64, 26, 26, 22, 6, 0.4, 0.9), 'shade', 'b', False)] + brows(68, OUTC, 2.2, 15, 1.5, 12),
    'side': [L(cloud(44, 30, 46, 32, 10, 0.1, 0.92)), L(outline([(70, 48), (82, 44), (88, 30), (50, 14), (8, 40), (14, 72), (32, 70), (46, 56)])),
             L(cloud(26, 46, 18, 18, 5, 0.3, 0.9), 'shade', 'b', False)],
    'back': [L(cloud(50, 40, 44, 38, 10, 0.1, 0.92)), L(cloud(62, 46, 28, 30, 6, 0.4, 0.9), 'shade', 'b', False)],
})

# Roger Rocket: pelo castaño redondo con la raya en medio, el flequillo en dos picos hacia abajo y las puntas de los lados
# hacia fuera por encima de las orejas; ojos aceitunados afilados, cejas enfadadas y boca seria
C('roger-rocket', {
    'body': 'normal', 'pal': pal('#8a5024', '#f8d0a0', iris='#7a7a3a', shade='#6c3e1a', deep='#4e2c10'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(16, 72), (14, 64), (0, 60, 1), (10, 52), (10, 30), (24, 10), (50, 2), (76, 10), (90, 30), (90, 52), (100, 60, 1), (86, 64), (84, 72),
                         (80, 58), (20, 58)])),
              L(outline([(58, 4), (80, 14), (90, 34), (90, 54), (80, 40)]), 'shade', 'b', False),
              fr([(14, 64), (12, 44), (24, 24), (48, 16), (50, 24), (52, 16), (76, 24), (88, 44), (86, 64), (80, 54), (64, 46), (54, 54, 1), (50, 40), (46, 54, 1),
                  (36, 46), (20, 54)]),
              strand([(36, 22), (30, 42)], 'deep', 'f', 1.0), strand([(64, 22), (70, 42)], 'deep', 'f', 1.0)],
    'side': [L(outline([(66, 54), (76, 44), (90, 40), (92, 24), (78, 6), (52, 0), (26, 6), (8, 24), (2, 46), (-6, 56, 1), (6, 62), (12, 78), (28, 82), (38, 66),
                        (50, 58)])),
             L(outline([(4, 44), (30, 48), (38, 66), (28, 80), (12, 76)]), 'shade', 'b', False),
             fr([(74, 42), (90, 40), (92, 56, 1), (84, 50)])],
    'back': [L(outline([(16, 80), (12, 64), (0, 60, 1), (10, 52), (10, 30), (24, 10), (50, 2), (76, 10), (90, 30), (90, 52), (100, 60, 1), (88, 64), (84, 80),
                        (50, 86)])),
             L(outline([(58, 4), (80, 14), (90, 34), (88, 78), (64, 84)]), 'shade', 'b', False), strand([(50, 4), (50, 40)], 'deep', 'b', 1.0)],
})

# Rolly Kerr: piel morena; el pelo crema recogido en un moño alto y abombado con rayas, atado arriba con una goma verde y una
# punta rosa; cejas blancas gruesas y enfadadas, ojos de punto, una cicatriz en cruz en la mejilla y morros
C('rolly-kerr', {
    'body': 'normal', 'pal': pal('#ece0c0', '#b4733e', iris='#1e1a1a', shade='#ccbe9c', deep='#a89a7a', band='#5a7a2a', tip='#f0b4b0'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'frown', 'mouth_y': 94, 'hairline': (60, 50)},
    'front': [L(outline([(16, 66), (12, 44), (14, 20), (26, 4), (40, -4), (60, -4), (74, 4), (86, 20), (88, 44), (84, 66), (80, 52), (20, 52)])),
              L(outline([(58, -2), (76, 6), (88, 30), (86, 62), (78, 40)]), 'shade', 'b', False),
              L(outline([(38, -4), (40, -14), (60, -14), (62, -4)]), 'band'), L(outline([(42, -14), (40, -22, 1), (50, -18), (60, -22, 1), (58, -14)]), 'tip')]
             + [strand([(x, -2 if abs(x - 50) < 14 else 8), (x + (x - 50) * 0.1, 50)], 'deep', 'b', 1.0) for x in (24, 36, 50, 64, 76)]
             + brows(64, WHITE, 4.5, 14, 1.4, 12)
             + [L([(28, 84), (34, 90)], OUTC, 'f', False, False, 1.2), L([(34, 84), (28, 90)], OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(64, 56), (74, 46), (86, 40), (90, 22), (76, 2), (54, -6), (30, -2), (12, 12), (4, 36), (6, 64), (20, 78), (34, 74), (40, 62), (50, 58)])),
             L(outline([(36, -6), (38, -14), (60, -14), (62, -6)]), 'band'), L(outline([(40, -14), (40, -22, 1), (50, -18), (60, -22, 1), (58, -14)]), 'tip'),
             L(outline([(6, 40), (30, 44), (40, 62), (34, 74), (20, 78), (6, 64)]), 'shade', 'b', False)]
            + [strand([(x, 0), (x - 6, 60)], 'deep', 'b', 1.0) for x in (30, 50, 70)] + brow_side(64, WHITE, 4.5, 1.4),
    'back': [L(outline([(16, 80), (10, 44), (14, 20), (26, 4), (40, -4), (60, -4), (74, 4), (86, 20), (90, 44), (84, 80), (50, 86)])),
             L(outline([(58, -2), (76, 6), (90, 30), (86, 78), (64, 84)]), 'shade', 'b', False),
             L(outline([(38, -4), (40, -14), (60, -14), (62, -4)]), 'band'), L(outline([(42, -14), (40, -22, 1), (50, -18), (60, -22, 1), (58, -14)]), 'tip')]
            + [strand([(x, -2 if abs(x - 50) < 14 else 8), (x + (x - 50) * 0.1, 80)], 'deep', 'b', 1.0) for x in (24, 36, 50, 64, 76)],
})

# Roman Candler: calvo con una cresta amarilla alta en medio, como una llama; ojos aceitunados ladinos, rayitas en las
# mejillas y sonrisa
C('roman-candler', {
    'body': 'normal', 'pal': pal('#d8b020', '#f2b474', iris='#6a6a2a', shade='#b08c14', deep='#8a6c0c'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': skull() + [L(outline([(43, 16), (41, -6), (45, -22), (52, -36, 1), (58, -18), (60, 0), (57, 16)])),
                        L(outline([(52, -32), (58, -18), (60, 0), (57, 14), (54, -8)]), 'shade', 'b', False)]
             + marks(86, 27),
    'side': [L(outline([(72, 26), (62, 4), (44, -10), (22, -20, 1), (28, -4), (14, 12), (30, 18), (56, 24)])), L(outline([(28, -4), (14, 12), (30, 18), (50, 22)]), 'shade', 'b', False)],
    'back': [L(outline([(42, 60), (40, 30), (44, 4), (52, -14, 1), (58, 6), (60, 30), (56, 60)])), L(outline([(52, -10), (58, 6), (60, 30), (56, 58), (54, 20)]), 'shade', 'b', False)],
})

# Romeo Montague (portero): pelo azul marino oscuro ondulado y revuelto que le cae hasta la mandíbula en ondas; ojos lilas
# redondos, cejas enfadadas y sonrisa pícara
C('romeo-montague', {
    'body': 'normal', 'pal': pal('#2a4262', '#f2b880', iris='#a89ab8', shade='#203450', deep='#16243a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(10, 96, 1), (2, 82), (8, 70, 1), (2, 56), (8, 34), (20, 12), (44, 2), (66, 4), (84, 14), (96, 36), (94, 56), (100, 70, 1), (92, 80),
                         (90, 96, 1), (82, 84), (82, 62), (18, 62), (18, 84)])),
              L(outline([(62, 6), (84, 16), (96, 40), (94, 90), (84, 70)]), 'shade', 'b', False),
              fr([(14, 72), (10, 50), (22, 26), (48, 14), (74, 20), (88, 40), (88, 64), (82, 56), (76, 46), (66, 54, 1), (60, 40), (50, 50, 1), (44, 38), (34, 48, 1),
                  (26, 46), (20, 60)]),
              strand([(36, 22), (26, 44)], 'deep', 'f', 1.0), strand([(60, 20), (70, 40)], 'deep', 'f', 1.0)],
    'side': [L(outline([(66, 54), (76, 44), (90, 40), (94, 22), (80, 6), (54, 0), (26, 6), (8, 24), (0, 48), (4, 66), (-2, 80, 1), (8, 82), (6, 96, 1), (20, 88),
                        (34, 80), (40, 64), (50, 58)])),
             L(outline([(2, 46), (30, 48), (40, 64), (32, 80), (8, 90)]), 'shade', 'b', False),
             fr([(74, 42), (92, 40), (94, 60, 1), (84, 52)])],
    'back': [L(outline([(10, 96, 1), (2, 80), (8, 66, 1), (2, 52), (8, 30), (22, 10), (50, 2), (78, 10), (92, 30), (98, 52), (92, 66, 1), (98, 80), (90, 96, 1),
                        (76, 88), (64, 96, 1), (50, 88), (36, 96, 1), (24, 88)])),
             L(outline([(58, 4), (80, 14), (96, 50), (92, 94), (66, 90)]), 'shade', 'b', False)],
})

# ---------------------------------------------------------------------------------------------------------------- 25-32

# Ron Away: melena rubia amarilla de casco hasta la mandíbula que le tapa las orejas, con el flequillo largo sobre los ojos;
# ojos azul lila grandes y sonrisa de dientes
C('ron-away', {
    'body': 'normal', 'pal': pal('#d8b41a', '#f8d2a2', iris='#6a64a8', shade='#b08e12', deep='#8a6c0a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(10, 92, 1), (8, 60), (10, 34), (22, 12), (50, 2), (78, 12), (90, 34), (92, 60), (90, 92, 1), (82, 78), (82, 62), (18, 62), (18, 78)])),
              L(outline([(60, 4), (80, 14), (92, 40), (90, 88), (84, 60)]), 'shade', 'b', False),
              fr([(14, 92, 1), (12, 60), (14, 38), (28, 20), (50, 14), (72, 20), (86, 38), (88, 60), (86, 92, 1), (80, 76), (80, 60), (72, 66, 1), (66, 52), (58, 68, 1),
                  (52, 52), (44, 68, 1), (38, 54), (30, 66, 1), (20, 60), (20, 76)]),
              strand([(40, 20), (36, 48)], 'deep', 'f', 1.0), strand([(62, 20), (66, 48)], 'deep', 'f', 1.0)],
    'side': [L(outline([(66, 54), (76, 42), (90, 40), (92, 22), (78, 6), (50, 0), (24, 6), (6, 26), (2, 56), (4, 86), (12, 94, 1), (30, 90), (40, 76), (46, 62),
                        (52, 58)])),
             L(outline([(4, 46), (32, 48), (42, 66), (32, 88), (10, 90)]), 'shade', 'b', False),
             fr([(72, 40), (90, 40), (94, 68, 1), (84, 60), (80, 50)])],
    'back': [L(outline([(10, 92, 1), (8, 58), (10, 32), (22, 10), (50, 2), (78, 10), (90, 32), (92, 58), (90, 92, 1), (70, 90), (50, 92), (30, 90)])),
             L(outline([(58, 4), (80, 14), (92, 46), (90, 90), (66, 90)]), 'shade', 'b', False)],
})

# Ronny Knowles: cara grande de mandíbula ancha; pelo castaño grisáceo recogido en una coleta alta hacia atrás, con un
# mechón que se riza a un lado; ojos ladinos, narizota y sonrisa
C('ronny-knowles', {
    'body': 'normal', 'pal': pal('#7a6262', '#f6c08a', iris='#1e1a1a', shade='#5e4a4a', deep='#423434'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'face_front': WIDE, 'hairline': (60, 40)},
    'front': [L(outline([(60, 4), (74, -8), (88, 0), (92, 16, 1), (84, 8), (74, 6)])),
              L(outline([(16, 66), (12, 42), (20, 18), (40, 6), (60, 6), (80, 16), (88, 40), (84, 66), (80, 48), (20, 48)])),
              L(outline([(58, 8), (80, 18), (88, 42), (84, 62), (76, 36)]), 'shade', 'b', False),
              strand([(46, 8), (36, 40)], 'deep', 'b', 1.0), strand([(56, 8), (52, 38)], 'deep', 'b', 1.0), strand([(66, 10), (72, 38)], 'deep', 'b', 1.0)]
             + nose_tri(88, 5, 12) + marks(86, 30),
    'side': [L(outline([(30, 12), (14, 0), (0, 12), (-6, 30, 1), (6, 22), (18, 24)])),
             L(outline([(70, 46), (80, 40), (86, 26), (72, 8), (50, 2), (26, 8), (10, 24), (4, 46), (10, 70), (22, 80), (34, 76), (40, 62), (50, 54)])),
             L(outline([(4, 42), (30, 46), (40, 62), (34, 76), (22, 80), (10, 70)]), 'shade', 'b', False)],
    'back': [L(outline([(50, 10), (42, -6), (58, -12), (70, 0), (66, 24), (60, 40), (64, 60, 1), (52, 44), (48, 26)])),
             L(outline([(16, 80), (12, 44), (20, 18), (40, 6), (60, 6), (80, 16), (88, 44), (84, 80), (50, 86)])),
             L(outline([(58, 8), (80, 18), (88, 44), (84, 78), (64, 84)]), 'shade', 'b', False),
             L(outline([(46, 4), (40, -8), (56, -14), (68, -4), (62, 26), (58, 48), (60, 66, 1), (50, 50), (46, 28)]), 'mid', 'f'),
             strand([(52, -6), (54, 44)], 'deep', 'f', 1.0)],
})

# Ronny O'Mania: piel morena; pelo caqui oliva en casquete corto con el flequillo recto; cejas finas, ojos entornados y una
# sonrisa ancha de dientes
C('ronny-o-mania', {
    'body': 'normal', 'pal': pal('#8a7a3e', '#b47c4a', iris='#1e1a1a', shade='#6c5e2e', deep='#4e4420'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'lips', 'mouth_y': 92, 'mouth_w': 8, 'hairline': False},
    'front': crop('front', top=0, side=64, w=1)
             + [bangs(56, 16, 84, 6, 22, jag=4), strand([(40, 6), (38, 30)], 'deep', 'f', 1.0), strand([(60, 6), (62, 30)], 'deep', 'f', 1.0)],
    'side': crop('side', top=-2, nape=86, w=1) + [fr([(72, 44), (88, 40), (90, 56, 1), (82, 52)])],
    'back': crop('back', top=0, nape=86, w=1),
})

# Ropert Chapp: adulto de cara larga; pelo naranja tostado peinado hacia arriba en un tupé; monóculo dorado en el ojo
# izquierdo (la derecha de la imagen), nariz larga y sonrisa ladina
C('ropert-chapp', {
    'body': 'delgado', 'pal': pal('#c86a22', '#f6d0a6', iris='#1e1a1a', shade='#a05218', deep='#7a3c10', gold='#d8b84a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 100, 'face_front': LONG, 'hairline': (60, 46)},
    'front': [L(outline([(18, 66), (14, 42), (6, 22, 1), (22, 24), (24, 6), (44, -4), (70, -6), (92, 4, 1), (84, 14), (88, 36), (82, 66), (78, 48), (22, 48)])),
              L(outline([(62, -4), (90, 4), (84, 16), (88, 38), (82, 62), (76, 34)]), 'shade', 'b', False),
              strand([(30, 10), (58, 0)], 'deep', 'b', 1.0), strand([(34, 22), (70, 6)], 'deep', 'b', 1.0)]
             + nose_tri(92, 4, 14) + [L(ell(64, 76, 8, 8) + [ell(64, 76, 8, 8)[0]], 'gold', 'f', False, False, 1.8), L(quad((72, 78), (78, 92), (74, 104)), 'gold', 'f', False, False, 1.0)],
    'side': [L(outline([(70, 46), (80, 40), (84, 24), (98, 6, 1), (80, 2), (62, -6), (36, -2), (14, 12), (6, 36), (8, 64), (22, 78), (34, 74), (40, 60), (50, 52)])),
             L(outline([(6, 40), (30, 44), (40, 60), (34, 74), (22, 78), (8, 64)]), 'shade', 'b', False),
             L(ell(82, 76, 5, 8) + [ell(82, 76, 5, 8)[0]], 'gold', 'f', False, False, 1.8)],
    'back': [L(outline([(16, 78), (12, 42), (20, 18), (40, 2), (64, -4), (86, 8), (90, 40), (84, 78), (50, 84)])),
             L(outline([(58, 0), (84, 10), (90, 44), (84, 76), (62, 82)]), 'shade', 'b', False)],
})

# Rory Boomer: piel morena; pelo castaño oscuro largo en pinchos revueltos que le caen por los lados, con un mechón naranja
# en el flequillo; ojos grandes y media sonrisa
C('rory-boomer', {
    'body': 'normal', 'pal': pal('#3c2c22', '#b47a4a', iris='#3a2a1e', shade='#2c2018', deep='#1e1610', streak='#e8702a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': messy('front', amp=22, n=10, seed=11, rx=50, ry=42, cy=44, lo=72, sweep=0.3)
             + [L(outline([(10, 70), (2, 98, 1), (16, 84), (18, 70)])), L(outline([(90, 70), (98, 98, 1), (84, 84), (82, 70)])),
                fr([(14, 72), (10, 48), (24, 28), (50, 22), (76, 28), (90, 48), (86, 72), (80, 60), (72, 70, 1), (66, 54), (58, 64, 1), (50, 50), (42, 66, 1),
                    (36, 52), (28, 66, 1), (20, 60)]),
                L(outline([(30, 26), (46, 24), (42, 40), (36, 62, 1), (34, 44)]), 'streak', 'f', False)],
    'side': messy('side', amp=22, n=10, seed=11, rx=50, ry=42, cy=44, sweep=0.3) + [L(outline([(70, 56), (72, 90), (68, 100, 1), (64, 86), (62, 58)]), 'mid', 'f')],
    'back': messy('back', amp=22, n=10, seed=11, rx=50, ry=42, cy=44, sweep=0.3),
})

# Rory Circles: grandullón de cara redonda; pelo crema melocotón ondulado hacia arriba en mechones como llamas; ojitos
# mirando arriba y la boca pequeña
C('rory-circles', {
    'body': 'corpulento', 'pal': pal('#f4d6b6', '#f2b878', iris='#1e1a1a', shade='#d8b496', deep='#b89474'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'line', 'mouth_y': 96, 'face_front': WIDE, 'hairline': (58, 42)},
    'front': [L(outline([(14, 66), (4, 52, 1), (12, 40), (8, 20, 1), (24, 18), (26, 0, 1), (40, 8), (50, -12, 1), (60, 6), (74, -4, 1), (76, 16), (94, 18, 1),
                         (88, 38), (96, 52, 1), (86, 66), (80, 48), (20, 48)])),
              L(outline([(60, 6), (74, -2), (76, 18), (92, 20), (88, 40), (86, 62), (78, 40)]), 'shade', 'b', False),
              strand([(40, 10), (44, 24), (38, 36)], 'deep', 'b', 1.0), strand([(60, 10), (56, 24), (62, 36)], 'deep', 'b', 1.0)],
    'side': [L(outline([(70, 46), (82, 40), (94, 30, 1), (84, 22), (90, 6, 1), (72, 8), (66, -10, 1), (52, 4), (32, -4, 1), (28, 12), (10, 16, 1), (12, 30), (0, 46, 1),
                        (10, 52), (8, 68), (22, 78), (34, 74), (42, 60), (52, 52)])),
             L(outline([(4, 44), (30, 46), (42, 60), (34, 74), (22, 78), (8, 68)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 78), (4, 54, 1), (12, 42), (8, 20, 1), (24, 18), (26, 0, 1), (40, 8), (50, -12, 1), (60, 6), (74, -4, 1), (76, 16), (94, 18, 1), (88, 40),
                        (96, 54, 1), (86, 78), (50, 84)])),
             L(outline([(60, 6), (74, -2), (76, 18), (92, 20), (88, 42), (86, 76), (64, 82)]), 'shade', 'b', False)],
})

# Rory Polisher (portera): pelo rosa recogido en un moño alto con una punta que cae hacia atrás, los lados cortos; ojos verde
# oliva con pestañas, cejas rosas y sonrisa
C('rory-polisher', {
    'body': 'chica', 'pal': pal('#d07888', '#f6c498', iris='#7a7a2a', shade='#b05c6c', deep='#8a4452'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': [(17, 66), (18, 50), (30, 42), (50, 40), (70, 42), (82, 50), (83, 66)]},
    'front': [L(ell(54, 2, 11, 8)), L(outline([(60, -4), (70, -14), (80, -10, 1), (70, -6)])),
              L(outline([(16, 68), (12, 42), (20, 18), (50, 8), (80, 18), (88, 42), (84, 68), (80, 50), (20, 50)])),
              L(outline([(60, 10), (80, 20), (88, 44), (84, 64), (76, 38)]), 'shade', 'b', False),
              strand([(40, 12), (36, 38)], 'deep', 'b', 1.0), strand([(60, 12), (64, 38)], 'deep', 'b', 1.0)]
             + brows(64, 'mid', 2.6, 14, 0.8, 11) + [L([(26, 72), (22, 69)], OUTC, 'f', False, False, 1.2), L([(74, 72), (78, 69)], OUTC, 'f', False, False, 1.2)],
    'side': [L(ell(40, 2, 10, 8)), L(outline([(32, 0), (16, -6), (8, 6, 1), (22, 6)])),
             L(outline([(70, 46), (80, 40), (86, 26), (72, 8), (50, 4), (26, 8), (10, 24), (4, 46), (10, 70), (22, 80), (34, 76), (40, 62), (50, 54)])),
             L(outline([(4, 42), (30, 46), (40, 62), (34, 76), (22, 80), (10, 70)]), 'shade', 'b', False)] + brow_side(64, 'mid', 2.6, 0.8),
    'back': [L(ell(50, 2, 11, 8)), L(outline([(44, 4), (40, 18), (46, 30, 1), (50, 16)])),
             L(outline([(16, 80), (12, 44), (20, 18), (50, 8), (80, 18), (88, 44), (84, 80), (50, 86)])),
             L(outline([(58, 10), (80, 20), (88, 46), (84, 78), (64, 84)]), 'shade', 'b', False)],
})

# Roy Plimsole (portero): pelo verde oscuro en bloque plano por arriba con un pico en medio de la frente; cejas gruesas, ojos
# entornados, pecas y sonrisa; cara cuadrada
C('roy-plimsole', {
    'body': 'normal', 'pal': pal('#1e5a3c', '#f2b878', iris='#1e1a1a', shade='#16462e', deep='#0e3020', freckle='#b46a44'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'face_front': WIDE,
             'hairline': [(13, 62), (14, 46), (30, 44), (48, 46), (50, 56), (52, 46), (70, 44), (86, 46), (87, 62)]},
    'front': [L(outline([(13, 64), (10, 40), (12, 12), (30, 4), (70, 4), (88, 12), (90, 40), (87, 64), (82, 48), (18, 48)])),
              L(outline([(60, 5), (86, 12), (90, 40), (86, 62), (78, 36)]), 'shade', 'b', False)]
             + [strand([(x, 6), (x, 40)], 'deep', 'b', 1.0) for x in (26, 40, 60, 74)]
             + brows(66, OUTC, 3.4, 15, 0.6, 14)
             + [L(ell(x, y, 0.9, 0.9), 'freckle', 'f', False) for x, y in ((24, 84), (28, 87), (32, 84), (68, 84), (72, 87), (76, 84))],
    'side': [L(outline([(70, 46), (82, 42), (86, 26), (82, 8), (60, 2), (30, 2), (10, 12), (4, 40), (8, 66), (22, 78), (34, 74), (40, 62), (50, 54)])),
             L(outline([(5, 40), (30, 44), (40, 62), (34, 74), (22, 78), (8, 66)]), 'shade', 'b', False)] + brow_side(66, OUTC, 3.4, 0.6),
    'back': [L(outline([(14, 78), (10, 40), (12, 12), (30, 4), (70, 4), (88, 12), (90, 40), (86, 78), (50, 84)])),
             L(outline([(60, 5), (86, 12), (90, 40), (86, 76), (64, 82)]), 'shade', 'b', False)],
})

# ---------------------------------------------------------------------------------------------------------------- 33-40

# Rudolph Rainder: grandullón de cara ancha; pelo gris morado corto en pinchos hacia arriba; una nariz enorme, redonda y
# naranja con puntitos, ojillos redondos, cejas gruesas y sonrisa ancha
C('rudolph-rainder', {
    'body': 'corpulento', 'pal': pal('#7a6a8c', '#eaaa6a', iris='#1e1a1a', shade='#5e5070', deep='#423856', nose='#e07a30'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'none', 'face_front': WIDE, 'hairline': (56, 44)},
    'front': [L(outline([(14, 62), (10, 44), (2, 30, 1), (16, 26), (16, 6, 1), (30, 14), (40, -6, 1), (50, 10), (62, -6, 1), (70, 14), (86, 6, 1), (84, 26), (98, 30, 1),
                         (90, 44), (86, 62), (80, 48), (20, 48)])),
              L(outline([(60, 6), (62, -4), (70, 14), (86, 8), (84, 28), (96, 32), (88, 46), (84, 58), (76, 36)]), 'shade', 'b', False)]
             + brows(64, 'shade', 5.0, 15, 0.4, 13)
             + [L(ell(50, 86, 9, 7.5), 'nose', 'f', False, True)] + [L(ell(x, y, 0.8, 0.8), (150, 70, 30, 255), 'f', False) for x, y in
                                                                       ((46, 83), (50, 82), (54, 83), (44, 87), (48, 86), (52, 86), (56, 87), (48, 90), (52, 90))]
             + [L(quad((30, 96), (50, 104), (70, 96)), BROWN, 'f', False, False, 1.6)],
    'side': [L(outline([(70, 46), (82, 42), (90, 28, 1), (82, 22), (88, 6, 1), (70, 10), (64, -6, 1), (50, 6), (34, -4, 1), (28, 12), (10, 14, 1), (12, 28), (2, 40, 1),
                        (8, 50), (10, 66), (22, 76), (34, 72), (42, 60), (52, 52)])),
             L(outline([(6, 44), (30, 46), (42, 60), (34, 72), (22, 76), (10, 66)]), 'shade', 'b', False),
             L(ell(88, 86, 6, 6), 'nose', 'f', False, True)] + brow_side(64, 'shade', 5.0, 0.4),
    'back': [L(outline([(14, 76), (10, 44), (2, 30, 1), (16, 26), (16, 6, 1), (30, 14), (40, -6, 1), (50, 10), (62, -6, 1), (70, 14), (86, 6, 1), (84, 26), (98, 30, 1),
                        (90, 44), (86, 76), (50, 82)])),
             L(outline([(60, 6), (62, -4), (70, 14), (86, 8), (84, 28), (96, 32), (88, 46), (86, 74), (64, 80)]), 'shade', 'b', False)],
})

# Rufus Judge: pelo naranja en pinchos que salen hacia arriba y a los lados, con una diadema dorada de rey mono en la frente;
# ojos ladinos, cejas enfadadas y la boca abierta de morros
C('rufus-judge', {
    'body': 'normal', 'pal': pal('#e2662a', '#f2b474', iris='#1e1a1a', shade='#bc4e1c', deep='#963c12', gold='#e8c43a', gold_d='#b8942a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'hairline': False},
    'front': messy('front', amp=20, n=10, seed=21, rx=46, ry=38, cy=42, lo=64)
             + [fr([(14, 60), (14, 44), (30, 32), (50, 28), (70, 32), (86, 44), (86, 60), (80, 54), (20, 54)]),
                L(outline([(14, 60), (16, 52), (50, 48), (84, 52), (86, 60), (50, 56)]), 'gold', 'f', ln=True),
                L(outline([(40, 52), (46, 44), (50, 50), (54, 44), (60, 52), (50, 56)]), 'gold_d', 'f', False, True),
                L(blob([(40, 96), (50, 92), (60, 96), (58, 102), (50, 103), (42, 102)], 6), MOUTH, 'f', False, True)] + nose_line(88),
    'side': messy('side', amp=20, n=10, seed=21, rx=46, ry=38, cy=42)
            + [L(outline([(54, 58), (60, 50), (88, 46), (90, 54), (62, 58)]), 'gold', 'f', ln=True)],
    'back': messy('back', amp=20, n=10, seed=21, rx=46, ry=38, cy=42) + [L(outline([(12, 58), (14, 50), (50, 54), (86, 50), (88, 58), (50, 62)]), 'gold', 'f', ln=True)],
})

# Rupert Spiers: melena castaño oliva enorme en pinchos revueltos que se abren hacia los lados, con el flequillo en picos;
# ojos afilados aceitunados, una cicatriz en la mejilla y media sonrisa
C('rupert-spiers', {
    'body': 'normal', 'pal': pal('#8a7c4c', '#f6c690', iris='#6a6a3a', shade='#6c6038', deep='#4e4426'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': messy('front', amp=22, n=11, seed=5, rx=52, ry=42, cy=44, lo=70, sweep=0.2)
             + [fr([(14, 70), (12, 48), (24, 28), (50, 22), (76, 28), (88, 48), (86, 70), (80, 58), (72, 66, 1), (66, 52), (58, 62, 1), (52, 48), (46, 62, 1), (38, 50),
                    (30, 64, 1), (22, 58)]),
                L([(24, 86), (32, 82)], BROWN, 'f', False, False, 1.0)],
    'side': messy('side', amp=22, n=11, seed=5, rx=50, ry=42, cy=44, sweep=0.2),
    'back': messy('back', amp=22, n=11, seed=5, rx=52, ry=42, cy=44, sweep=0.2),
})

# Rush Tooset: gorro de lana de rayas verdes y amarillas calado hasta las cejas, con el borde vuelto de canalé; ojos
# aceitunados y sonrisa
C('rush-tooset', {
    'body': 'normal', 'pal': pal('#3a2a1e', '#f8d0a0', iris='#6a6a3a', shade='#2a1e16', deep='#1e1610', wool='#3c7a2c', wool_d='#2c5e20', yel='#e8c43a'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': False},
    'front': [L(outline([(12, 60), (10, 32), (22, 8), (50, -2), (78, 8), (90, 32), (88, 60)]), 'wool', 'f'),
              L(outline([(16, 32), (24, 18), (50, 12), (76, 18), (84, 32), (84, 40), (50, 34), (16, 40)]), 'yel', 'f', False),
              L(outline([(30, 6), (50, 2), (70, 6), (74, 14), (50, 8), (26, 14)]), 'yel', 'f', False),
              L(outline([(10, 66), (10, 50), (50, 46), (90, 50), (90, 66), (50, 62)]), 'wool', 'f')]
             + [strand([(x, 50), (x, 64)], 'wool_d', 'f', 1.0) for x in (18, 26, 34, 42, 50, 58, 66, 74, 82)],
    'side': [L(outline([(88, 60), (90, 30), (78, 8), (50, -2), (22, 6), (6, 30), (4, 64), (40, 66)]), 'wool', 'f'),
             L(outline([(8, 32), (24, 16), (50, 10), (78, 14), (88, 32), (88, 40), (50, 34), (8, 40)]), 'yel', 'f', False),
             L(outline([(4, 72), (4, 54), (50, 50), (90, 52), (90, 66), (50, 64)]), 'wool', 'f')]
            + [strand([(x, 54), (x, 66)], 'wool_d', 'f', 1.0) for x in (10, 20, 30, 40, 74, 84)],
    'back': [L(outline([(10, 72), (8, 32), (22, 8), (50, -2), (78, 8), (92, 32), (90, 72), (50, 76)]), 'wool', 'f'),
             L(outline([(12, 32), (24, 18), (50, 12), (76, 18), (88, 32), (88, 40), (50, 34), (12, 40)]), 'yel', 'f', False),
             L(outline([(8, 76), (8, 58), (50, 56), (92, 58), (92, 76), (50, 80)]), 'wool', 'f')]
            + [strand([(x, 60), (x, 76)], 'wool_d', 'f', 1.0) for x in (16, 26, 38, 50, 62, 74, 84)],
})

# Rusty Spoakes (portero): adulto con entradas enormes: la coronilla calva y el pelo verde oliva solo a los lados y por detrás;
# cejas negras gruesas y enfadadas, barbilla grande y sonrisa
C('rusty-spoakes', {
    'body': 'normal', 'pal': pal('#7a7a3a', '#f2b474', iris='#1e1a1a', shade='#5e5e2c', deep='#42421e'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'face_front': LONG, 'hairline': False},
    'front': [L(outline([(14, 74), (10, 44), (16, 20), (34, 6), (50, 4), (66, 6), (84, 20), (90, 44), (86, 74), (80, 56), (20, 56)])),
              L(outline([(60, 6), (82, 18), (90, 44), (86, 70), (78, 40)]), 'shade', 'b', False),
              L(outline([(22, 56), (24, 30), (34, 12), (50, 8), (66, 12), (76, 30), (78, 56), (50, 52)]), 'skin', 'f'),
              L(outline([(40, 14), (50, 10), (60, 14), (56, 26), (44, 26)]), (252, 226, 190, 255), 'f', False)]
             + brows(66, OUTC, 4.0, 15, 1.6, 13) + [L(quad((42, 104), (50, 110), (58, 104)), BROWN, 'f', False, False, 1.0)],
    'side': [L(outline([(54, 62), (56, 44), (40, 30), (20, 30), (6, 44), (6, 70), (20, 82), (34, 78), (42, 66)])),
             L(outline([(6, 50), (30, 50), (42, 64), (34, 78), (20, 82), (8, 70)]), 'shade', 'b', False)] + brow_side(66, OUTC, 4.0, 1.6),
    'back': [L(outline([(14, 82), (10, 50), (14, 30), (30, 24), (50, 30), (70, 24), (86, 30), (90, 50), (86, 82), (50, 88)])),
             L(outline([(60, 28), (84, 30), (90, 52), (86, 80), (64, 86)]), 'shade', 'b', False)],
})

# Ry Sling: pelo lila rosado corto y revuelto, con mechones de punta hacia un lado y el flequillo en picos; ojos aceitunados
# y boca seria
C('ry-sling', {
    'body': 'normal', 'pal': pal('#b89aaa', '#f2b474', iris='#8a7a4a', shade='#987a8a', deep='#7a5e6c'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(16, 72), (6, 52, 1), (12, 40), (8, 22), (24, 8), (46, 2), (66, 0), (80, -6, 1), (78, 8), (94, 16, 1), (88, 30), (98, 50, 1), (86, 58),
                         (84, 72), (80, 58), (20, 58)])),
              L(outline([(60, 2), (80, -4), (78, 10), (92, 18), (86, 32), (94, 50), (84, 56), (78, 36)]), 'shade', 'b', False),
              fr([(14, 66), (12, 44), (26, 24), (50, 16), (74, 22), (88, 42), (86, 64), (80, 54), (72, 62, 1), (66, 46), (56, 58, 1), (50, 44), (42, 58, 1), (36, 46),
                  (28, 60, 1), (22, 54)])],
    'side': [L(outline([(66, 54), (74, 44), (90, 40), (98, 26, 1), (84, 20), (86, 4, 1), (66, 4), (56, -8, 1), (44, 2), (22, 4), (8, 22), (2, 46), (-6, 56, 1),
                        (8, 66), (18, 80), (32, 78), (40, 64), (50, 58)])),
             L(outline([(4, 46), (30, 48), (40, 64), (32, 78), (18, 80), (8, 66)]), 'shade', 'b', False),
             fr([(74, 42), (90, 40), (92, 58, 1), (84, 52)])],
    'back': [L(outline([(16, 80), (6, 54, 1), (12, 40), (8, 22), (24, 8), (46, 2), (66, 0), (80, -6, 1), (78, 8), (94, 16, 1), (88, 30), (98, 52, 1), (88, 60),
                        (84, 80), (50, 86)])),
             L(outline([(60, 2), (80, -4), (78, 10), (92, 18), (86, 32), (94, 52), (86, 78), (64, 84)]), 'shade', 'b', False)],
})

# Ryan Ferry: pelo verde oliva muy oscuro en pinchos revueltos alrededor de la cabeza; ojos de párpado caído, rayitas en las
# mejillas y sonrisita
C('ryan-ferry', {
    'body': 'bajito', 'pal': pal('#4a4a22', '#f2b878', iris='#1e1a1a', shade='#383818', deep='#262610'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': messy('front', amp=16, n=12, seed=17, rx=48, ry=40, cy=42, lo=66)
             + [fr([(14, 66), (12, 46), (26, 28), (50, 22), (74, 28), (88, 46), (86, 66), (80, 56), (74, 62, 1), (68, 50), (60, 60, 1), (54, 48), (46, 60, 1), (40, 48),
                    (32, 60, 1), (26, 50), (20, 60, 1)]),
                L([(28, 74), (44, 74)], OUTC, 'f', False, False, 1.4), L([(56, 74), (72, 74)], OUTC, 'f', False, False, 1.4)] + marks(86, 26),
    'side': messy('side', amp=16, n=12, seed=17, rx=48, ry=40, cy=42),
    'back': messy('back', amp=16, n=12, seed=17, rx=48, ry=40, cy=42),
})

# Ryder Waverly: piel tostada, cara larga; calvo salvo una cresta alta a franjas verdes y naranjas en medio de la cabeza;
# cejas verdes gruesas, ojos entornados y sonrisa
C('ryder-waverly', {
    'body': 'delgado', 'pal': pal('#6a8a3c', '#d8a064', iris='#1e1a1a', shade='#52702c', deep='#3c5420', band='#d86a2a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'face_front': LONG, 'hairline': False},
    'front': skull() + [L(outline([(42, 30), (40, 4), (44, -14), (50, -20, 1), (56, -14), (60, 4), (58, 30)])),
                        L(outline([(41, -2), (59, -2), (60, 8), (40, 8)]), 'band', 'b', False), L(outline([(43, -14), (57, -14), (58, -8), (42, -8)]), 'band', 'b', False)]
             + brows(64, 'mid', 4.0, 14, 1.2, 12) + nose_tri(88, 3, 10),
    'side': [L(outline([(80, 28), (70, 6), (52, -10), (30, -14, 1), (34, 0), (24, 12), (40, 18), (62, 26)])),
             L(outline([(52, -10), (60, -2), (40, 6), (36, -4)]), 'band', 'b', False), L(outline([(66, 4), (72, 12), (52, 16), (48, 8)]), 'band', 'b', False)]
            + brow_side(64, 'mid', 4.0, 1.2),
    'back': [L(outline([(42, 66), (40, 30), (44, 0), (50, -14, 1), (56, 0), (60, 30), (58, 66)])),
             L(outline([(41, 14), (59, 14), (60, 24), (40, 24)]), 'band', 'b', False), L(outline([(42, 40), (58, 40), (59, 50), (41, 50)]), 'band', 'b', False)],
})

# ---------------------------------------------------------------------------------------------------------------- 41-48

# Ryder Wheeling: casco ajustado verde grisáceo con una cresta por el medio y unas gafas de esquí grandes de cristal amarillo
# encima de los ojos; sonrisita
C('ryder-wheeling', {
    'body': 'normal', 'pal': pal('#4a7a68', '#eaa868', iris='#1e1a1a', shade='#3a6252', deep='#2a4a3c', frame='#f0ecc4', lens='#e8c42a', lens_d='#c89a1a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(14, 76), (10, 44), (18, 18), (50, 6), (82, 18), (90, 44), (86, 76), (82, 60), (18, 60)]), 'mid', 'f'),
              L(outline([(60, 9), (80, 18), (90, 44), (86, 72), (80, 44)]), 'shade', 'f', False),
              L(outline([(46, 50), (46, 12), (50, 4), (54, 12), (54, 50)]), 'shade', 'f', False, True),
              L(outline([(10, 72), (12, 62), (30, 58), (50, 62), (70, 58), (88, 62), (90, 72), (84, 84), (62, 84), (50, 78), (38, 84), (16, 84)]), 'frame', 'f', ln=True),
              L(outline([(16, 70), (30, 64), (48, 68), (50, 76), (40, 80), (20, 80)]), 'lens', 'f', False),
              L(outline([(84, 70), (70, 64), (52, 68), (50, 76), (60, 80), (80, 80)]), 'lens', 'f', False),
              L(outline([(56, 76), (72, 68), (82, 72), (80, 78), (62, 80)]), 'lens_d', 'f', False)],
    'side': [L(outline([(78, 50), (88, 34), (80, 12), (52, 2), (24, 8), (6, 30), (4, 60), (12, 80), (28, 84), (40, 66), (54, 58)]), 'mid', 'f'),
             L(outline([(6, 40), (30, 44), (40, 66), (28, 84), (12, 80)]), 'shade', 'f', False),
             L(outline([(60, 64), (88, 62), (92, 70), (88, 82), (66, 80)]), 'frame', 'f', ln=True), L(outline([(70, 66), (88, 66), (88, 78), (70, 78)]), 'lens', 'f', False),
             L([(60, 72), (36, 66)], 'frame', 'f', False, False, 3.0)],
    'back': [L(outline([(14, 82), (10, 44), (18, 18), (50, 6), (82, 18), (90, 44), (86, 82), (50, 88)]), 'mid', 'f'),
             L(outline([(60, 9), (80, 18), (90, 44), (86, 80), (64, 86)]), 'shade', 'f', False),
             L(outline([(46, 86), (46, 12), (50, 4), (54, 12), (54, 86)]), 'shade', 'f', False, True), L([(10, 68), (90, 68)], 'frame', 'f', False, False, 4.0)],
})

# Sagaminator Saggy: pelo amarillo en pinchos enormes de punta hacia arriba; gafas de sol negras y sonrisa de dientes afilados;
# piel tostada
C('sagaminator-saggy', {
    'body': 'normal', 'pal': pal('#f2ca22', '#d8a064', iris='#1e1a1a', shade='#d0a412', deep='#a8800a', shades='#1e1e24'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(16, 64), (2, 52, 1), (12, 40), (0, 22, 1), (18, 22), (14, -4, 1), (32, 10), (34, -20, 1), (46, 4), (54, -28, 1), (60, 2), (74, -18, 1),
                         (72, 10), (92, -2, 1), (84, 24), (100, 26, 1), (88, 40), (98, 54, 1), (84, 64), (80, 50), (20, 50)])),
              L(outline([(60, 2), (74, -16), (72, 12), (90, 0), (84, 26), (98, 28), (88, 42), (84, 58), (76, 34)]), 'shade', 'b', False),
              fr([(16, 58), (14, 44), (26, 32), (36, 46, 1), (40, 32), (50, 28), (54, 44, 1), (60, 30), (74, 32), (70, 46, 1), (80, 38), (86, 46), (84, 58), (50, 54)]),
              L(outline([(18, 68), (42, 70), (50, 74), (58, 70), (82, 68), (80, 78), (62, 82), (50, 76), (38, 82), (20, 78)]), 'shades', 'f', ln=True),
              L([(26, 72), (36, 74)], (120, 120, 140, 255), 'f', False, False, 1.2)],
    'side': [L(outline([(70, 50), (80, 42), (98, 34, 1), (84, 24), (98, 8, 1), (76, 10), (78, -12, 1), (60, 4), (50, -24, 1), (40, 2), (20, -10, 1), (22, 10), (4, 12, 1),
                        (10, 28), (-4, 40, 1), (8, 48), (8, 66), (22, 78), (34, 74), (42, 62), (52, 54)])),
             L(outline([(6, 44), (30, 46), (42, 62), (34, 74), (22, 78), (8, 66)]), 'shade', 'b', False),
             L(outline([(64, 68), (88, 66), (90, 76), (70, 80)]), 'shades', 'f', ln=True), L([(64, 72), (40, 68)], 'shades', 'f', False, False, 2.4)],
    'back': [L(outline([(16, 76), (2, 54, 1), (12, 42), (0, 22, 1), (18, 22), (14, -4, 1), (32, 10), (34, -20, 1), (46, 4), (54, -28, 1), (60, 2), (74, -18, 1),
                        (72, 10), (92, -2, 1), (84, 24), (100, 26, 1), (88, 42), (98, 56, 1), (84, 76), (50, 82)])),
             L(outline([(60, 2), (74, -16), (72, 12), (90, 0), (84, 26), (98, 28), (88, 44), (84, 74), (62, 80)]), 'shade', 'b', False)],
})

# Sage Wisdom: grandullón adulto de cara ancha; pelo castaño corto en pinchitos revueltos por arriba; ojos entornados, cejas
# enfadadas, arrugas y sonrisa de lado
C('sage-wisdom', {
    'body': 'corpulento', 'pal': pal('#7a4a22', '#d8a064', iris='#4a6a7a', shade='#5e3818', deep='#422810'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'face_front': WIDE, 'hairline': (56, 42)},
    'front': [L(outline([(14, 62), (12, 40), (16, 20), (22, 6, 1), (30, 14), (36, 0, 1), (44, 10), (52, -2, 1), (58, 10), (66, 0, 1), (72, 12), (80, 6, 1), (84, 20),
                         (88, 40), (86, 62), (80, 46), (20, 46)])),
              L(outline([(58, 8), (80, 8), (84, 22), (88, 42), (84, 58), (76, 34)]), 'shade', 'b', False)]
             + nose_tri(88, 4, 10) + [L([(28, 62), (34, 60)], BROWN, 'f', False, False, 0.9)],
    'side': [L(outline([(70, 46), (82, 42), (86, 24), (84, 8, 1), (70, 10), (64, -2, 1), (52, 6), (40, -2, 1), (32, 8), (16, 8, 1), (10, 24), (4, 44), (8, 64), (22, 76),
                        (34, 72), (42, 58), (52, 52)])),
             L(outline([(5, 42), (30, 44), (42, 58), (34, 72), (22, 76), (8, 64)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 74), (12, 40), (16, 20), (22, 6, 1), (30, 14), (36, 0, 1), (44, 10), (52, -2, 1), (58, 10), (66, 0, 1), (72, 12), (80, 6, 1), (84, 20),
                        (88, 40), (86, 74), (50, 80)])),
             L(outline([(58, 8), (80, 8), (84, 22), (88, 42), (86, 72), (62, 78)]), 'shade', 'b', False)],
})

# Sal Curie: piel morena; melena castaño malva ondulada y despeinada hasta la mandíbula; ojos afilados, nariz de pico naranja
# y media sonrisa
C('sal-curie', {
    'body': 'normal', 'pal': pal('#9a6a5c', '#c8885a', iris='#1e1a1a', shade='#7a5246', deep='#5c3c32', beak='#f08030'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(6, 98, 1), (10, 86), (2, 74, 1), (8, 60), (6, 34), (20, 12), (46, 2), (72, 6), (90, 22), (96, 46), (92, 62), (100, 76, 1), (90, 86),
                         (94, 98, 1), (80, 88), (80, 66), (20, 66), (20, 88)])),
              L(outline([(60, 4), (86, 16), (96, 46), (94, 92), (84, 70)]), 'shade', 'b', False),
              fr([(14, 80), (10, 54), (16, 32), (34, 16), (58, 12), (78, 20), (88, 36), (88, 62), (84, 80), (78, 64), (74, 50), (62, 46), (56, 56, 1), (50, 44),
                  (38, 48), (28, 60), (22, 70)]),
              strand([(30, 22), (22, 50)], 'deep', 'f', 1.0), strand([(64, 18), (76, 42)], 'deep', 'f', 1.0),
              L([(44, 84), (56, 84), (50, 92)], 'beak', 'f', False, True)],
    'side': [L(outline([(66, 54), (76, 42), (90, 38), (94, 22), (78, 6), (52, 0), (26, 6), (6, 24), (0, 48), (4, 66), (-4, 78, 1), (8, 82), (6, 98, 1), (20, 88),
                        (34, 82), (40, 66), (50, 58)])),
             L(outline([(2, 46), (30, 48), (40, 66), (34, 82), (8, 90)]), 'shade', 'b', False),
             fr([(74, 42), (92, 40), (94, 60, 1), (84, 52)]), L([(84, 82), (94, 86), (84, 90)], 'beak', 'f', False, True)],
    'back': [L(outline([(6, 98, 1), (10, 84), (2, 70, 1), (8, 56), (6, 30), (22, 10), (50, 2), (78, 10), (94, 30), (96, 56), (100, 70, 1), (90, 84), (94, 98, 1),
                        (76, 90), (64, 98, 1), (50, 90), (36, 98, 1), (24, 90)])),
             L(outline([(58, 4), (82, 14), (96, 50), (92, 94), (66, 92)]), 'shade', 'b', False)],
})

# Sam Aritan: piel morena; pelo morado oscuro peinado hacia arriba en mechones de punta, con unas cejas enormes en zigzag;
# ojos de rombo, pintura verde a rayas en las mejillas y sonrisa
C('sam-aritan', {
    'body': 'normal', 'pal': pal('#4a3a6a', '#b8784a', iris='#1e1a1a', shade='#382c52', deep='#261e3a', paint='#8ab858', paint2='#e8eccc'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': (58, 44)},
    'front': [L(outline([(16, 62), (12, 38), (16, 18), (12, -2, 1), (28, 8), (34, -12, 1), (46, 4), (54, -16, 1), (62, 4), (76, -6, 1), (78, 12), (90, 6, 1), (86, 24),
                         (88, 40), (84, 62), (80, 46), (20, 46)])),
              L(outline([(58, 4), (76, -4), (78, 14), (88, 8), (86, 26), (86, 58), (76, 30)]), 'shade', 'b', False),
              strand([(32, 12), (38, 40)], 'deep', 'b', 1.0), strand([(56, 6), (54, 40)], 'deep', 'b', 1.0), strand([(70, 10), (68, 40)], 'deep', 'b', 1.0)]
             + [L(outline([(20, 66), (28, 60, 1), (32, 66), (38, 60, 1), (46, 68), (36, 70), (24, 70)]), 'mid', 'f', False, True),
                L(outline([(80, 66), (72, 60, 1), (68, 66), (62, 60, 1), (54, 68), (64, 70), (76, 70)]), 'mid', 'f', False, True)]
             + [L([(cx - 7, 76), (cx, 72), (cx + 7, 76), (cx, 80), (cx - 7, 76)], OUTC, 'f', False, False, 1.6) for cx in (36, 64)]
             + [L(ell(cx, 76, 4.6, 2.6), WHITE, 'f', False) for cx in (36, 64)] + [L(ell(cx, 76, 1.4, 1.6), OUTC, 'f', False) for cx in (36, 64)]
             + [L(outline([(x, 81), (x + 4.4, 81), (x + 4.4, 94), (x, 92)]), 'paint', 'f', False, True) for x in (31, 64.6)]
             + [L(outline([(x + 1.5, 82), (x + 2.9, 82), (x + 2.9, 92), (x + 1.5, 91)]), 'paint2', 'f', False) for x in (31, 64.6)],
    'side': [L(outline([(70, 46), (82, 40), (88, 24), (96, 6, 1), (78, 8), (72, -10, 1), (58, 4), (46, -14, 1), (36, 4), (18, 0, 1), (14, 18), (4, 40), (8, 66), (22, 78),
                        (34, 74), (42, 60), (52, 52)])),
             L(outline([(5, 40), (30, 44), (42, 60), (34, 74), (22, 78), (8, 66)]), 'shade', 'b', False),
             L(outline([(70, 66), (78, 60, 1), (82, 66), (88, 62, 1), (90, 68), (80, 70)]), 'mid', 'f', False, True),
             L(outline([(76, 84), (81, 84), (81, 98), (76, 96)]), 'paint', 'f', False, True)],
    'back': [L(outline([(16, 76), (12, 40), (16, 18), (12, -2, 1), (28, 8), (34, -12, 1), (46, 4), (54, -16, 1), (62, 4), (76, -6, 1), (78, 12), (90, 6, 1), (86, 24),
                        (88, 40), (84, 76), (50, 82)])),
             L(outline([(58, 4), (76, -4), (78, 14), (88, 8), (86, 26), (86, 74), (62, 80)]), 'shade', 'b', False)],
})

# Sam Firman (portero): piel morena; casco militar beis con una franja crema de festón y puntitos, y las correas colgando a
# los lados; cejas naranjas, ojos ladinos y sonrisa
C('sam-firman', {
    'body': 'normal', 'pal': pal('#3a2a1e', '#b8784a', iris='#1e1a1a', shade='#2a1e16', deep='#1e1610', helm='#c8a868', helm_d='#a88a50', band='#ecdcb4',
                                 strap='#3a3020', brow='#e07a2a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L([(16, 60), (16, 102)], 'strap', 'f', False, False, 2.6), L([(84, 60), (84, 102)], 'strap', 'f', False, False, 2.6),
              L(outline([(4, 64), (8, 34), (22, 10), (50, 0), (78, 10), (92, 34), (96, 64), (50, 58)]), 'helm', 'f'),
              L(outline([(62, 4), (80, 14), (92, 36), (94, 62), (80, 60), (82, 34)]), 'helm_d', 'f', False),
              L(outline([(6, 52), (8, 40), (20, 44), (30, 36), (40, 42), (50, 34), (60, 42), (70, 36), (80, 44), (92, 40), (94, 52), (50, 50)]), 'band', 'f', False)]
             + [L(ell(x, y, 1.6, 1.6), 'band', 'f', False) for x, y in ((24, 22), (40, 14), (60, 14), (76, 22), (50, 10))]
             + brows(67, 'brow', 3.4, 14, 0.6, 12),
    'side': [L([(60, 60), (64, 100)], 'strap', 'f', False, False, 2.6),
             L(outline([(94, 58), (92, 32), (78, 10), (50, 0), (22, 8), (2, 32), (0, 64), (50, 60)]), 'helm', 'f'),
             L(outline([(2, 40), (24, 34), (24, 62), (0, 62)]), 'helm_d', 'f', False),
             L(outline([(2, 50), (4, 42), (30, 42), (50, 36), (70, 42), (92, 40), (94, 50), (50, 50)]), 'band', 'f', False)] + brow_side(67, 'brow', 3.4, 0.6),
    'back': [L(outline([(4, 70), (8, 34), (22, 10), (50, 0), (78, 10), (92, 34), (96, 70), (50, 74)]), 'helm', 'f'),
             L(outline([(62, 4), (80, 14), (92, 36), (94, 68), (66, 72)]), 'helm_d', 'f', False),
             L(outline([(6, 56), (8, 44), (30, 46), (50, 42), (70, 46), (92, 44), (94, 56), (50, 58)]), 'band', 'f', False)],
})

# Sam Fitspire (portero): grandullón de cara ancha; pelo rosa en pinchos revueltos; cejas negras gruesas y enfadadas, ojos
# lilas grandes y sonrisa
C('sam-fitspire', {
    'body': 'corpulento', 'pal': pal('#eaa2aa', '#f6c08a', iris='#8a84b0', shade='#c8808a', deep='#a8626c'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'face_front': WIDE, 'hairline': False},
    'front': messy('front', amp=16, n=11, seed=31, rx=48, ry=38, cy=42, lo=62)
             + [fr([(14, 60), (12, 44), (26, 28), (50, 22), (74, 28), (88, 44), (86, 60), (80, 50), (72, 58, 1), (66, 46), (58, 56, 1), (52, 44), (44, 56, 1), (38, 44),
                    (30, 56, 1), (22, 50)])]
             + brows(64, OUTC, 4.0, 15, 1.4, 13) + nose_line(88),
    'side': messy('side', amp=16, n=11, seed=31, rx=48, ry=38, cy=42) + brow_side(64, OUTC, 4.0, 1.4),
    'back': messy('back', amp=16, n=11, seed=31, rx=48, ry=38, cy=42),
})

# Sam Gale (portero): pelo azul marino oscuro peinado en un tupé enorme y redondo hacia delante, con los lados planos; ojos
# ladinos y sonrisa chulesca
C('sam-gale', {
    'body': 'normal', 'pal': pal('#2a4262', '#f2b474', iris='#1e1a1a', shade='#203450', deep='#16243a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': [(17, 66), (18, 50), (28, 44), (50, 46), (72, 44), (82, 50), (83, 66)]},
    'front': [L(outline([(16, 68), (14, 44), (12, 22), (18, 2), (34, -10), (56, -14), (76, -8), (90, 6), (88, 26), (86, 44), (84, 68), (80, 50), (20, 50)])),
              L(outline([(58, -12), (80, -6), (90, 8), (88, 28), (78, 30), (70, 10)]), 'shade', 'b', False),
              L(outline([(14, 22), (30, 30), (60, 30), (88, 24), (86, 44), (84, 64), (16, 64), (14, 44)]), 'shade', 'b', False),
              strand([(30, 0), (70, -2)], 'deep', 'b', 1.0), strand([(20, 16), (80, 12)], 'deep', 'b', 1.0)],
    'side': [L(outline([(70, 48), (82, 42), (98, 30), (104, 12), (90, -6), (60, -12), (34, -6), (14, 10), (4, 34), (6, 64), (20, 78), (34, 74), (40, 60), (50, 54)])),
             L(outline([(5, 36), (30, 40), (40, 60), (34, 74), (20, 78), (6, 64)]), 'shade', 'b', False),
             strand([(30, -2), (90, 4)], 'deep', 'b', 1.0), strand([(20, 12), (96, 22)], 'deep', 'b', 1.0)],
    'back': [L(outline([(16, 78), (12, 44), (14, 20), (26, 4), (50, -4), (74, 4), (86, 20), (88, 44), (84, 78), (50, 84)])),
             L(outline([(58, -2), (80, 8), (88, 44), (84, 76), (64, 82)]), 'shade', 'b', False), strand([(50, 0), (50, 60)], 'deep', 'b', 1.0)],
})

# ---------------------------------------------------------------------------------------------------------------- 49-56

# Sam Murray: piel morena; pelo azul marino peinado hacia arriba en un penacho de pinchos con una pinza crema, y dos mechones
# largos que le caen por delante de las orejas; ojos azules, cejas enfadadas y sonrisa
C('sam-murray', {
    'body': 'normal', 'pal': pal('#2c3c5c', '#c8885a', iris='#5a9ac8', shade='#202c46', deep='#161e30', clip='#ece0b8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': [(17, 66), (18, 50), (30, 44), (44, 48), (50, 56), (56, 48), (70, 44), (82, 50), (83, 66)]},
    'front': [L(outline([(16, 66), (12, 40), (18, 18), (10, 0, 1), (30, 6), (34, -12, 1), (46, -2), (54, -16, 1), (60, -2), (76, -10, 1), (74, 8), (92, 2, 1), (84, 20),
                         (88, 40), (84, 66), (80, 50), (20, 50)])),
              L(outline([(58, -2), (76, -8), (74, 10), (90, 4), (84, 22), (88, 42), (84, 62), (76, 36)]), 'shade', 'b', False),
              strand([(50, 4), (40, 40)], 'deep', 'b', 1.0), strand([(50, 4), (60, 40)], 'deep', 'b', 1.0),
              L(outline([(38, 6), (50, 0), (62, 6), (58, 12), (50, 8), (42, 12)]), 'clip', 'f', ln=True),
              L(outline([(17, 56), (12, 88), (15, 98, 1), (18.5, 86), (21, 60)]), 'mid', 'f'), L(outline([(83, 56), (88, 88), (85, 98, 1), (81.5, 86), (79, 60)]), 'mid', 'f')]
             + marks(86, 26),
    'side': [L(outline([(70, 46), (82, 40), (88, 24), (96, 4, 1), (78, 6), (74, -12, 1), (60, 0), (48, -16, 1), (40, 2), (22, -2, 1), (16, 14), (4, 36), (6, 64), (20, 78),
                        (34, 74), (40, 60), (50, 52)])),
             L(outline([(5, 38), (30, 42), (40, 60), (34, 74), (20, 78), (6, 64)]), 'shade', 'b', False),
             L(outline([(46, 2), (54, -2), (60, 4), (54, 8)]), 'clip', 'f', ln=True), L(outline([(56, 54), (58, 88), (55, 98, 1), (52, 86), (50, 56)]), 'mid', 'f')],
    'back': [L(outline([(16, 78), (12, 42), (18, 18), (10, 0, 1), (30, 6), (34, -12, 1), (46, -2), (54, -16, 1), (60, -2), (76, -10, 1), (74, 8), (92, 2, 1), (84, 20),
                        (88, 42), (84, 78), (50, 84)])),
             L(outline([(58, -2), (76, -8), (74, 10), (90, 4), (84, 22), (88, 44), (84, 76), (62, 82)]), 'shade', 'b', False),
             L(outline([(38, 6), (50, 0), (62, 6), (58, 12), (50, 8), (42, 12)]), 'clip', 'f', ln=True), strand([(50, 10), (50, 60)], 'deep', 'b', 1.0)],
})

# Sam O'Reilly: un kabuto de samurái azul marino calado hasta los ojos, con dos cuernos dorados en media luna, remaches y las
# alas del casco a los lados; cordón blanco bajo la barbilla, una cicatriz cosida y sonrisa
C('sam-o-reilly', {
    'body': 'normal', 'pal': pal('#2a2420', '#f2b878', iris='#1e1a1a', shade='#1e1a16', deep='#14100e', helm='#2c4466', helm_d='#203450', gold='#d8b44a',
                                 gold_d='#b08c30', rope='#ece6d6', red='#a03a2a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(2, 92), (4, 66), (10, 54), (90, 54), (96, 66), (98, 92), (86, 84), (84, 66), (16, 66), (14, 84)]), 'helm', 'f'),
              L(outline([(2, 92), (6, 80), (12, 84)]), 'red', 'f', False), L(outline([(98, 92), (94, 80), (88, 84)]), 'red', 'f', False),
              L(outline([(10, 62), (10, 30), (24, 8), (50, 0), (76, 8), (90, 30), (90, 62), (50, 70)]), 'helm', 'f'),
              L(outline([(60, 2), (80, 12), (90, 34), (90, 60), (76, 62)]), 'helm_d', 'f', False),
              L(outline([(50, 22), (30, 16), (14, 6), (4, -10, 1), (20, -6), (34, 4), (50, 10), (66, 4), (80, -6), (96, -10, 1), (86, 6), (70, 16)]), 'gold', 'f', ln=True),
              L(ell(50, 36, 3, 3), 'helm_d', 'f', ln=True), L(ell(30, 46, 2.4, 2.4), 'helm_d', 'f', ln=True), L(ell(70, 46, 2.4, 2.4), 'helm_d', 'f', ln=True),
              L(quad((22, 70), (50, 112), (78, 70)), 'rope', 'f', False, False, 2.2), L(ell(50, 102, 3, 3), 'rope', 'f', ln=True),
              L([(30, 80), (40, 88)], BROWN, 'f', False, False, 1.0), L([(32, 86), (34, 82)], BROWN, 'f', False, False, 0.8), L([(36, 88), (38, 84)], BROWN, 'f', False, False, 0.8)],
    'side': [L(outline([(8, 96), (4, 70), (12, 56), (50, 56), (52, 70), (40, 86), (20, 96)]), 'helm', 'f'),
             L(outline([(92, 62), (92, 32), (78, 10), (50, 0), (22, 8), (6, 30), (4, 60), (50, 66)]), 'helm', 'f'),
             L(outline([(4, 40), (26, 34), (26, 62), (4, 60)]), 'helm_d', 'f', False),
             L(outline([(70, 16), (84, 4), (94, -12, 1), (92, 6), (80, 18)]), 'gold', 'f', ln=True), L(ell(80, 36, 3, 3), 'helm_d', 'f', ln=True),
             L(quad((56, 66), (64, 96), (80, 104)), 'rope', 'f', False, False, 2.2)],
    'back': [L(outline([(2, 96), (4, 66), (10, 54), (90, 54), (96, 66), (98, 96), (50, 100)]), 'helm', 'f'),
             L(outline([(58, 56), (94, 58), (98, 94), (60, 98)]), 'helm_d', 'f', False),
             L(outline([(10, 62), (10, 30), (24, 8), (50, 0), (76, 8), (90, 30), (90, 62), (50, 66)]), 'helm', 'f'),
             L(outline([(60, 2), (80, 12), (90, 34), (90, 60), (66, 64)]), 'helm_d', 'f', False),
             L(outline([(14, 6), (4, -10, 1), (20, -6), (30, 2)]), 'gold', 'f', ln=True), L(outline([(86, 6), (96, -10, 1), (80, -6), (70, 2)]), 'gold', 'f', ln=True)],
})

# Sam Which (portero): cara larga; pelo castaño muy oscuro corto con pinchos arriba, el flequillo en picos y patillas; ojos
# redondos grandes, narizota y sonrisa
C('sam-which', {
    'body': 'delgado', 'pal': pal('#3a3420', '#f2b474', iris='#1e1a1a', shade='#2c2818', deep='#1e1c10'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 100, 'face_front': LONG, 'hairline': False},
    'front': [L(outline([(16, 72), (12, 44), (18, 18), (34, 6), (40, -10, 1), (48, 2), (56, -14, 1), (60, 2), (70, -6, 1), (70, 8), (84, 18), (88, 44), (84, 72),
                         (80, 56), (20, 56)])),
              L(outline([(60, 2), (70, -4), (70, 10), (84, 20), (88, 44), (84, 66), (78, 40)]), 'shade', 'b', False),
              fr([(14, 66), (14, 42), (28, 24), (50, 18), (72, 24), (86, 42), (86, 66), (82, 56), (74, 58, 1), (68, 46), (60, 56, 1), (54, 44), (46, 56, 1), (40, 44),
                  (32, 56, 1), (26, 46), (18, 56)]),
              L([(16, 60), (15.6, 82)], 'mid', 'f', False, False, 2.0), L([(84, 60), (84.4, 82)], 'mid', 'f', False, False, 2.0)] + nose_tri(90, 4, 14),
    'side': [L(outline([(70, 48), (80, 40), (86, 24), (76, 8), (66, -8, 1), (56, 4), (46, -12, 1), (36, 4), (18, 8), (6, 30), (6, 62), (20, 78), (34, 74), (40, 60), (50, 52)])),
             L(outline([(6, 40), (30, 44), (40, 60), (34, 74), (20, 78), (6, 62)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 78), (12, 44), (18, 18), (34, 6), (40, -10, 1), (48, 2), (56, -14, 1), (60, 2), (70, -6, 1), (70, 8), (84, 18), (88, 44), (84, 78),
                        (50, 84)])),
             L(outline([(60, 2), (70, -4), (70, 10), (84, 20), (88, 44), (84, 76), (62, 82)]), 'shade', 'b', False)],
})

# Samuel Peeps: adulto de cara larga; un pañuelo rosa claro atado en la cabeza y dos matas de rizos rojizos que le salen a los
# lados por debajo; cejas naranjas, ojos redondos y sonrisa
C('samuel-peeps', {
    'body': 'delgado', 'pal': pal('#c04a1c', '#f6c08a', iris='#1e1a1a', shade='#9a3a14', deep='#742a0e', cloth='#f2c8b8', cloth_d='#d8a898'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 100, 'face_front': LONG, 'hairline': False},
    'front': [L(cloud(10, 78, 12, 14, 5, 0.3)), L(cloud(90, 78, 12, 14, 5, 0.6)),
              L(outline([(16, 64), (12, 40), (20, 16), (50, 4), (80, 16), (88, 40), (84, 64), (50, 58)]), 'cloth', 'f'),
              L(outline([(60, 6), (80, 18), (88, 42), (84, 62), (74, 40)]), 'cloth_d', 'f', False),
              strand([(30, 20), (36, 50)], 'cloth_d', 'f', 1.0), strand([(50, 10), (50, 50)], 'cloth_d', 'f', 1.0)]
             + brows(66, 'mid', 4.0, 14, 1.0, 12) + nose_tri(92, 4, 14),
    'side': [L(cloud(30, 80, 16, 14, 5, 0.3)),
             L(outline([(70, 56), (86, 46), (88, 28), (76, 8), (50, 2), (24, 8), (6, 28), (4, 56), (20, 66), (50, 62)]), 'cloth', 'f'),
             L(outline([(6, 36), (28, 36), (30, 62), (6, 58)]), 'cloth_d', 'f', False), L(cloud(26, 82, 8, 8, 4), 'shade', 'b', False)] + brow_side(66, 'mid', 4.0, 1.0),
    'back': [L(cloud(14, 82, 14, 14, 5, 0.3)), L(cloud(86, 82, 14, 14, 5, 0.6)), L(cloud(50, 86, 24, 12, 6)),
             L(outline([(12, 74), (10, 40), (20, 16), (50, 4), (80, 16), (90, 40), (88, 74), (50, 78)]), 'cloth', 'f'),
             L(outline([(60, 6), (80, 18), (90, 42), (88, 72), (66, 76)]), 'cloth_d', 'f', False), L(ell(50, 74, 6, 4), 'cloth_d', 'f', ln=True)],
})

# Sandy Beecher: pelo verde oscuro con un mechón ancho rosa que le cruza la frente de lado, el pelo tapándole la frente y las
# orejas; ojos azules afilados y sonrisa
C('sandy-beecher', {
    'body': 'normal', 'pal': pal('#3c7a5a', '#f2b474', iris='#5aa2c8', shade='#2c5e44', deep='#1e4430', pink='#c88a80', pink_d='#a86a62'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(10, 84, 1), (6, 60), (8, 34), (22, 12), (50, 2), (78, 12), (92, 34), (94, 60), (90, 84, 1), (82, 70), (82, 62), (18, 62), (18, 70)])),
              L(outline([(60, 4), (80, 14), (92, 38), (92, 78), (84, 60)]), 'shade', 'b', False),
              fr([(12, 76), (10, 50), (20, 26), (44, 12), (70, 14), (86, 30), (90, 54), (86, 74), (80, 60), (72, 50), (60, 54), (48, 56), (36, 60), (24, 66)]),
              L(outline([(30, 14), (52, 8), (70, 16), (84, 40), (88, 70, 1), (78, 56), (66, 40), (50, 28), (36, 22)]), 'pink', 'f', False, True),
              strand([(52, 14), (74, 40), (84, 62)], 'pink_d', 'f', 1.0)],
    'side': [L(outline([(66, 54), (76, 42), (90, 38), (94, 22), (80, 6), (54, 0), (26, 6), (8, 24), (2, 50), (4, 72), (12, 84, 1), (24, 80), (36, 76), (42, 62), (50, 58)])),
             L(outline([(4, 46), (30, 48), (42, 62), (36, 76), (12, 80)]), 'shade', 'b', False),
             L(outline([(50, 2), (78, 6), (94, 22), (92, 40), (80, 34), (66, 18)]), 'pink', 'f', False, True), fr([(74, 42), (92, 40), (94, 58, 1), (84, 52)])],
    'back': [L(outline([(10, 84, 1), (6, 58), (8, 32), (22, 10), (50, 2), (78, 10), (92, 32), (94, 58), (90, 84, 1), (70, 86), (50, 88), (30, 86)])),
             L(outline([(58, 4), (80, 14), (94, 46), (90, 82), (66, 86)]), 'shade', 'b', False),
             L(outline([(70, 6), (84, 16), (94, 40), (84, 36), (74, 20)]), 'pink', 'f', False, True)],
})

# Sandy Hope: adulto de piel tostada; pelo gris peinado hacia atrás con las puntas de los lados en pinchos; ojos enfadados,
# arrugas y sonrisa torcida
C('sandy-hope', {
    'body': 'normal', 'pal': pal('#8c8678', '#c8905a', iris='#1e1a1a', shade='#6e6a5e', deep='#524e44'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'face_front': LONG, 'hairline': (60, 42)},
    'front': [L(outline([(16, 72), (6, 66, 1), (12, 58), (2, 46, 1), (12, 40), (16, 18), (34, 4), (50, 0), (66, 4), (84, 18), (88, 40), (98, 46, 1), (88, 58), (94, 66, 1),
                         (84, 72), (80, 48), (20, 48)])),
              L(outline([(58, 4), (82, 16), (88, 42), (84, 66), (76, 36)]), 'shade', 'b', False)]
             + [strand([(x, 4 if abs(x - 50) < 16 else 12), (x + (x - 50) * 0.1, 42)], 'deep', 'b', 1.0) for x in (30, 42, 50, 58, 70)]
             + [L(quad((26, 88), (30, 92), (28, 96)), BROWN, 'f', False, False, 0.9), L(quad((74, 88), (70, 92), (72, 96)), BROWN, 'f', False, False, 0.9)],
    'side': [L(outline([(70, 46), (80, 40), (84, 24), (72, 6), (50, 0), (26, 4), (10, 18), (4, 40), (-6, 50, 1), (6, 56), (2, 70, 1), (12, 72), (20, 82), (34, 76),
                        (40, 62), (50, 52)])),
             L(outline([(5, 40), (30, 44), (40, 62), (34, 76), (20, 82), (8, 66)]), 'shade', 'b', False),
             strand([(70, 10), (20, 30)], 'deep', 'b', 1.0), strand([(76, 24), (16, 46)], 'deep', 'b', 1.0)],
    'back': [L(outline([(16, 82), (6, 70, 1), (12, 60), (2, 48, 1), (12, 40), (16, 18), (34, 4), (50, 0), (66, 4), (84, 18), (88, 40), (98, 48, 1), (88, 60), (94, 70, 1),
                        (84, 82), (50, 88)])),
             L(outline([(58, 4), (82, 16), (88, 42), (84, 80), (64, 86)]), 'shade', 'b', False)]
            + [strand([(x, 6), (x + (x - 50) * 0.1, 70)], 'deep', 'b', 1.0) for x in (34, 50, 66)],
})

# Sandy Insolls: piel parda grisácea; pelo melocotón claro corto en pinchos de punta hacia arriba; ojos tranquilos, cejas finas
# y sonrisa
C('sandy-insolls', {
    'body': 'normal', 'pal': pal('#f6d2b2', '#9a7c64', iris='#1e1a1a', shade='#dab294', deep='#ba9274'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'face_front': LONG, 'hairline': (60, 44)},
    'front': [L(outline([(18, 64), (12, 46), (4, 34, 1), (16, 30), (12, 12, 1), (28, 18), (32, 0, 1), (42, 12), (50, -4, 1), (58, 12), (68, 0, 1), (72, 18), (88, 12, 1),
                         (84, 30), (96, 34, 1), (88, 46), (82, 64), (78, 48), (22, 48)])),
              L(outline([(58, 10), (68, 2), (72, 20), (86, 14), (84, 32), (94, 36), (86, 48), (82, 60), (74, 36)]), 'shade', 'b', False)] + nose_line(88),
    'side': [L(outline([(70, 46), (82, 42), (94, 34, 1), (84, 26), (92, 10, 1), (72, 12), (68, -4, 1), (54, 8), (38, -2, 1), (30, 12), (12, 12, 1), (12, 28), (2, 40, 1),
                        (8, 48), (8, 64), (22, 76), (34, 72), (42, 58), (52, 52)])),
             L(outline([(6, 44), (30, 46), (42, 58), (34, 72), (22, 76), (8, 64)]), 'shade', 'b', False)],
    'back': [L(outline([(18, 76), (12, 46), (4, 34, 1), (16, 30), (12, 12, 1), (28, 18), (32, 0, 1), (42, 12), (50, -4, 1), (58, 12), (68, 0, 1), (72, 18), (88, 12, 1),
                        (84, 30), (96, 34, 1), (88, 46), (82, 76), (50, 82)])),
             L(outline([(58, 10), (68, 2), (72, 20), (86, 14), (84, 32), (94, 36), (86, 48), (82, 74), (62, 80)]), 'shade', 'b', False)],
})

# Sascha Powder (portero): pelo amarillo con dos mechones de punta que salen hacia arriba por encima de las orejas como
# cuernos, y el flequillo en picos; ojos negros grandes con pestañas y sonrisa
C('sascha-powder', {
    'body': 'normal', 'pal': pal('#e2ba1c', '#f6c08a', iris='#1e1a1a', shade='#c09612', deep='#98760a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(12, 80), (6, 52), (8, 30), (2, 2, 1), (20, 14), (36, 4), (50, 2), (64, 4), (80, 14), (98, 2, 1), (92, 30), (94, 52), (88, 80), (82, 64), (18, 64)])),
              L(outline([(60, 4), (80, 16), (96, 4), (92, 32), (92, 74), (82, 50)]), 'shade', 'b', False),
              fr([(12, 72), (10, 48), (22, 26), (50, 16), (78, 26), (90, 48), (88, 72), (82, 60), (76, 66, 1), (70, 52), (62, 62, 1), (56, 48), (48, 62, 1), (42, 50),
                  (34, 62, 1), (28, 52), (20, 64, 1)]),
              strand([(40, 22), (36, 44)], 'deep', 'f', 1.0), strand([(62, 22), (66, 44)], 'deep', 'f', 1.0)]
             + [L([(24, 72), (20, 69)], OUTC, 'f', False, False, 1.2), L([(76, 72), (80, 69)], OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(66, 54), (76, 42), (90, 40), (92, 22), (78, 6), (52, 0), (40, -2), (30, -18, 1), (24, 4), (8, 22), (2, 50), (4, 74), (16, 84), (30, 80), (40, 66),
                        (50, 58)])),
             L(outline([(4, 46), (30, 48), (40, 66), (30, 80), (16, 84)]), 'shade', 'b', False),
             fr([(74, 42), (90, 40), (92, 60, 1), (84, 52)])],
    'back': [L(outline([(12, 86), (6, 52), (8, 30), (2, 2, 1), (20, 14), (36, 4), (50, 2), (64, 4), (80, 14), (98, 2, 1), (92, 30), (94, 52), (88, 86), (50, 90)])),
             L(outline([(60, 4), (80, 16), (96, 4), (92, 32), (90, 84), (64, 88)]), 'shade', 'b', False)],
})

# ---------------------------------------------------------------------------------------------------------------- 57-67

# Saul Dowd: cara redonda y ancha; pelo verde en casquete con un pañuelo crema anudado arriba; ojos ladinos con pestañas,
# nariz de cerdito y una sonrisa ancha
C('saul-dowd', {
    'body': 'normal', 'pal': pal('#5a8a2a', '#d8a064', iris='#1e1a1a', shade='#46701e', deep='#325214', cloth='#ece0c4', cloth_d='#c8b898', snout='#c88870'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'none', 'face_front': WIDE, 'hairline': (54, 44)},
    'front': [L(outline([(12, 60), (10, 36), (20, 14), (50, 4), (80, 14), (90, 36), (88, 60), (84, 46), (16, 46)])),
              L(outline([(60, 6), (80, 16), (90, 38), (88, 58), (78, 34)]), 'shade', 'b', False)]
             + [strand([(x, 12 if abs(x - 50) < 20 else 22), (x + (x - 50) * 0.1, 46)], 'deep', 'b', 1.0) for x in (22, 34, 46, 58, 70, 80)]
             + [L(outline([(30, 6), (50, 0), (70, 6), (76, -6, 1), (64, -4), (50, -8), (36, -4), (24, -6, 1)]), 'cloth', 'f', ln=True),
                L([(30, 6), (50, 2), (70, 6)], (180, 80, 60, 255), 'f', False, False, 1.0),
                L(ell(50, 86, 5.4, 4), 'snout', 'f', False, True), L(ell(48, 86, 0.9, 1.2), OUTC, 'f', False), L(ell(52, 86, 0.9, 1.2), OUTC, 'f', False),
                L(quad((32, 94), (50, 104), (68, 94)), OUTC, 'f', False, False, 1.6),
                L([(22, 74), (18, 71)], OUTC, 'f', False, False, 1.2), L([(78, 74), (82, 71)], OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(70, 46), (82, 40), (88, 26), (76, 8), (50, 2), (24, 8), (8, 26), (4, 46), (8, 66), (22, 76), (34, 72), (42, 58), (52, 52)])),
             L(outline([(5, 42), (30, 44), (42, 58), (34, 72), (22, 76), (8, 66)]), 'shade', 'b', False),
             L(outline([(30, 4), (50, -2), (66, 4), (70, -8, 1), (56, -6), (40, -8), (28, -4)]), 'cloth', 'f', ln=True), L(ell(88, 86, 3.6, 4), 'snout', 'f', False, True)],
    'back': [L(outline([(14, 76), (10, 38), (20, 14), (50, 4), (80, 14), (90, 38), (86, 76), (50, 82)])),
             L(outline([(60, 6), (80, 16), (90, 40), (86, 74), (64, 80)]), 'shade', 'b', False),
             L(outline([(30, 6), (50, 0), (70, 6), (76, -6, 1), (64, -4), (50, -8), (36, -4), (24, -6, 1)]), 'cloth', 'f', ln=True)],
})

# Saul Searcher: pelo verde azulado oscuro en pinchos revueltos con el flequillo en picos; ojos negros de punto, rayitas en las
# mejillas y sonrisa
C('saul-searcher', {
    'body': 'normal', 'pal': pal('#3a5a52', '#f8d0a0', iris='#1e1a1a', shade='#2c463e', deep='#1e322c'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': False},
    'front': messy('front', amp=14, n=11, seed=41, rx=48, ry=40, cy=42, lo=68)
             + [fr([(14, 68), (12, 46), (26, 28), (50, 20), (74, 28), (88, 46), (86, 68), (80, 58), (74, 62, 1), (68, 48), (60, 58, 1), (54, 46), (46, 60, 1), (40, 46),
                    (32, 58, 1), (26, 50), (20, 62, 1)])] + marks(86, 26),
    'side': messy('side', amp=14, n=11, seed=41, rx=48, ry=40, cy=42),
    'back': messy('back', amp=14, n=11, seed=41, rx=48, ry=40, cy=42),
})

# Sayer Lemon: piel tostada; pelo amarillo pálido peinado hacia arriba en una punta en medio, con dos picos pequeños a los
# lados por encima de las orejas; ojos afilados y boca seria
C('sayer-lemon', {
    'body': 'normal', 'pal': pal('#e6dc9c', '#d8a064', iris='#1e1a1a', shade='#c4b87a', deep='#a0945a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'hairline': (58, 42)},
    'front': [L(outline([(16, 66), (12, 46), (2, 30, 1), (16, 30), (22, 14), (40, 2), (50, -10, 1), (60, 2), (78, 14), (84, 30), (98, 30, 1), (88, 46), (84, 66), (80, 48),
                         (20, 48)])),
              L(outline([(56, 0), (76, 14), (84, 32), (96, 32), (86, 48), (82, 62), (74, 34)]), 'shade', 'b', False)]
             + [strand([(50, -4), (x, 40)], 'deep', 'b', 1.0) for x in (30, 40, 60, 70)],
    'side': [L(outline([(70, 46), (82, 40), (86, 22), (72, 4), (52, -8, 1), (34, 0), (16, 12), (6, 32), (-4, 36, 1), (6, 44), (8, 64), (22, 78), (34, 74), (40, 60), (50, 52)])),
             L(outline([(6, 40), (30, 44), (40, 60), (34, 74), (22, 78), (8, 64)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 76), (12, 46), (2, 30, 1), (16, 30), (22, 14), (40, 2), (50, -10, 1), (60, 2), (78, 14), (84, 30), (98, 30, 1), (88, 46), (84, 76), (50, 82)])),
             L(outline([(56, 0), (76, 14), (84, 32), (96, 32), (86, 48), (84, 74), (62, 80)]), 'shade', 'b', False)],
})

# Scamp Shrimplin (portero): piel morena; melena rubia ceniza hasta la mandíbula con un flequillo largo de lado que le tapa
# el ojo derecho (la izquierda de la imagen); un ojo entornado y sonrisa ladina
C('scamp-shrimplin', {
    'body': 'normal', 'pal': pal('#d8b862', '#c8885a', iris='#1e1a1a', shade='#b09444', deep='#8a722c'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(8, 98, 1), (6, 60), (10, 32), (26, 10), (52, 2), (76, 10), (90, 30), (92, 60), (88, 96, 1), (82, 78), (82, 62), (18, 62), (18, 80)])),
              L(outline([(62, 4), (82, 14), (92, 40), (88, 92), (84, 64)]), 'shade', 'b', False),
              fr([(10, 98, 1), (8, 60), (14, 34), (32, 16), (58, 10), (78, 18), (88, 34), (86, 58), (80, 48), (68, 40), (56, 50), (50, 70), (44, 88), (32, 104, 1),
                  (34, 88), (24, 92)]),
              strand([(54, 16), (40, 50), (30, 90)], 'deep', 'f', 1.0), strand([(36, 22), (18, 60)], 'deep', 'f', 1.0),
              L(outline([(56, 74), (70, 72), (72, 78), (62, 80)]), WHITE, 'f', False, True), L(ell(65, 76.5, 2.2, 2.4), OUTC, 'f', False),
              L([(56, 73), (72, 71)], OUTC, 'f', False, False, 2.4)],
    'side': [L(outline([(66, 54), (76, 42), (90, 38), (92, 22), (78, 6), (52, 0), (26, 6), (8, 24), (2, 50), (4, 86), (12, 98, 1), (26, 92), (36, 82), (42, 64), (50, 58)])),
             L(outline([(4, 46), (30, 48), (42, 64), (36, 82), (12, 94)]), 'shade', 'b', False),
             fr([(74, 42), (90, 40), (92, 58, 1), (84, 52)]), L([(76, 74), (86, 72)], OUTC, 'f', False, False, 2.4), L(ell(83, 76, 2, 2.4), OUTC, 'f', False)],
    'back': [L(outline([(8, 98, 1), (6, 58), (10, 30), (26, 8), (50, 2), (74, 8), (90, 30), (92, 58), (90, 98, 1), (70, 94), (50, 96), (30, 94)])),
             L(outline([(58, 4), (80, 14), (92, 46), (90, 94), (66, 94)]), 'shade', 'b', False)],
})

# Scean Spector: piel tostada; melena gris parda lisa hasta la mandíbula con la raya a un lado, que le tapa el ojo izquierdo
# (la derecha de la imagen); el otro ojo de párpado caído y la boca seria
C('scean-spector', {
    'body': 'normal', 'pal': pal('#9a9282', '#c8905a', iris='#1e1a1a', shade='#7c7666', deep='#5e584a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(8, 96, 1), (6, 60), (10, 32), (24, 10), (46, 2), (72, 6), (90, 26), (94, 60), (92, 96, 1), (82, 78), (82, 62), (18, 62), (18, 80)])),
              L(outline([(60, 4), (84, 16), (94, 44), (92, 92), (84, 64)]), 'shade', 'b', False),
              fr([(12, 92, 1), (10, 60), (14, 34), (28, 16), (44, 10), (64, 12), (82, 22), (90, 40), (92, 64), (90, 96, 1), (80, 86), (70, 92, 1), (66, 74), (60, 56),
                  (52, 40), (44, 46), (32, 52), (22, 64), (18, 80)]),
              strand([(44, 12), (56, 40), (66, 72)], 'deep', 'f', 1.0), strand([(64, 14), (78, 40), (82, 80)], 'deep', 'f', 1.0),
              L(outline([(28, 74), (42, 73), (42, 78), (30, 79)]), WHITE, 'f', False, True), L(ell(36, 76.5, 2.2, 2.2), OUTC, 'f', False),
              L([(27, 73), (43, 72)], OUTC, 'f', False, False, 2.4)],
    'side': [L(outline([(66, 54), (76, 42), (92, 40), (94, 22), (78, 6), (50, 0), (24, 6), (8, 24), (2, 50), (4, 84), (12, 96, 1), (26, 90), (36, 82), (42, 64), (50, 58)])),
             L(outline([(4, 46), (30, 48), (42, 64), (36, 82), (12, 92)]), 'shade', 'b', False),
             fr([(72, 40), (92, 40), (96, 80, 1), (86, 70), (82, 54)])],
    'back': [L(outline([(8, 96, 1), (6, 58), (10, 30), (26, 8), (50, 2), (74, 8), (90, 30), (94, 58), (92, 96, 1), (70, 92), (50, 94), (30, 92)])),
             L(outline([(58, 4), (80, 14), (94, 46), (92, 92), (66, 92)]), 'shade', 'b', False)],
})

# Scot Chopper: pelo verde oliva muy oscuro partido en medio en dos alas redondas que suben como un corazón, con los lados
# hasta las orejas; ojos redondos de punto, rayitas en las mejillas y sonrisa
C('scot-chopper', {
    'body': 'normal', 'pal': pal('#4a4424', '#f2b474', iris='#1e1a1a', shade='#38341a', deep='#262410'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': [(16, 70), (18, 52), (30, 46), (48, 50), (50, 56), (52, 50), (70, 46), (82, 52), (84, 70)]},
    'front': [L(outline([(14, 74), (10, 50), (6, 24), (12, 2), (28, -6), (42, 0), (50, 10, 1), (58, 0), (72, -6), (88, 2), (94, 24), (90, 50), (86, 74), (80, 54), (20, 54)])),
              L(outline([(58, 2), (74, -4), (88, 4), (94, 26), (88, 70), (80, 44)]), 'shade', 'b', False)]
             + [strand([(x, 2), (x + (x - 50) * 0.15, 46)], 'deep', 'b', 1.0) for x in (22, 32, 40, 60, 68, 78)] + marks(86, 26),
    'side': [L(outline([(70, 48), (82, 42), (90, 26), (88, 4), (70, -6), (50, -2), (30, -6), (12, 4), (4, 26), (4, 56), (14, 76), (30, 78), (40, 64), (50, 56)])),
             L(outline([(4, 40), (30, 44), (40, 64), (30, 78), (14, 76)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 80), (10, 50), (6, 24), (12, 2), (28, -6), (42, 0), (50, 10, 1), (58, 0), (72, -6), (88, 2), (94, 24), (90, 50), (86, 80), (50, 86)])),
             L(outline([(58, 2), (74, -4), (88, 4), (94, 26), (88, 78), (64, 84)]), 'shade', 'b', False)],
})

# Scot Enguard: cara larga; pelo naranja peinado hacia atrás con un mechón que se riza en la coronilla y mechones largos que le
# caen por los lados hasta la mandíbula; cejas enfadadas, narizota y boca seria
C('scot-enguard', {
    'body': 'delgado', 'pal': pal('#e8782a', '#f2c08a', iris='#1e1a1a', shade='#c05e1c', deep='#984812'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'face_front': LONG, 'hairline': (58, 42)},
    'front': [L(outline([(16, 66), (12, 42), (18, 18), (36, 4), (56, 2), (76, -2), (92, 4, 1), (84, 12), (88, 40), (84, 66), (80, 48), (20, 48)])),
              L(outline([(58, 4), (84, 12), (88, 42), (84, 62), (76, 34)]), 'shade', 'b', False),
              strand([(50, 4), (44, 40)], 'deep', 'b', 1.0), strand([(62, 4), (60, 40)], 'deep', 'b', 1.0), strand([(38, 8), (30, 40)], 'deep', 'b', 1.0),
              L(outline([(20, 50), (16, 90), (20, 104, 1), (24, 86), (26, 56)]), 'mid', 'f'), L(outline([(80, 50), (84, 90), (80, 104, 1), (76, 86), (74, 56)]), 'mid', 'f')]
             + nose_tri(90, 5, 12),
    'side': [L(outline([(70, 46), (80, 40), (84, 24), (72, 6), (50, 0), (26, 4), (10, 14), (-4, 18, 1), (6, 28), (4, 46), (8, 66), (20, 80), (34, 76), (40, 62), (50, 52)])),
             L(outline([(6, 40), (30, 44), (40, 62), (34, 76), (20, 80), (8, 66)]), 'shade', 'b', False),
             L(outline([(60, 50), (64, 90), (60, 104, 1), (56, 86), (54, 54)]), 'mid', 'f')],
    'back': [L(outline([(16, 80), (12, 42), (18, 18), (36, 4), (56, 2), (76, 4), (88, 18), (92, 42), (86, 80), (50, 86)])),
             L(outline([(58, 4), (84, 14), (92, 44), (86, 78), (62, 84)]), 'shade', 'b', False),
             L(outline([(46, 2), (36, -10), (24, -6), (30, 2, 1), (38, 4)])), strand([(50, 4), (50, 60)], 'deep', 'b', 1.0)],
})

# Scott Springer: pelo azul marino oscuro abultado y ondulado, con un bloque de pelo que le cae hacia delante sobre la frente
# como una visera; cejas azules gruesas, ojos entornados y sonrisa
C('scott-springer', {
    'body': 'normal', 'pal': pal('#2a4262', '#f2b878', iris='#1e1a1a', shade='#203450', deep='#16243a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': [(17, 70), (18, 56), (30, 52), (50, 54), (70, 52), (82, 56), (83, 70)]},
    'front': [L(outline([(14, 76), (4, 60, 1), (10, 50), (2, 34, 1), (12, 20), (26, 4), (50, -4), (74, 2), (92, 14), (100, 32, 1), (90, 44), (98, 60, 1), (86, 64), (84, 76),
                         (80, 58), (20, 58)])),
              L(outline([(60, -2), (86, 10), (98, 32), (90, 46), (94, 60), (84, 62), (80, 40)]), 'shade', 'b', False),
              L(outline([(18, 50), (16, 30), (30, 18), (60, 16), (82, 22), (88, 36), (80, 48), (60, 40), (40, 42)]), 'deep', 'b', False),
              strand([(30, 20), (24, 48)], 'deep', 'b', 1.0), strand([(70, 18), (78, 40)], 'deep', 'b', 1.0)]
             + brows(66, 'mid', 4.0, 14, 0.6, 12),
    'side': [L(outline([(70, 52), (82, 46), (96, 42), (102, 28, 1), (90, 10), (64, -4), (36, -4), (14, 8), (2, 30), (-6, 46, 1), (4, 56), (4, 72), (18, 84), (32, 80),
                        (40, 66), (50, 58)])),
             L(outline([(4, 44), (30, 48), (40, 66), (32, 80), (18, 84), (6, 72)]), 'shade', 'b', False)] + brow_side(66, 'mid', 4.0, 0.6),
    'back': [L(outline([(14, 84), (4, 64, 1), (10, 52), (2, 34, 1), (12, 20), (26, 4), (50, -4), (74, 2), (92, 14), (100, 34, 1), (90, 48), (98, 64, 1), (86, 84), (50, 90)])),
             L(outline([(60, -2), (86, 10), (98, 34), (90, 48), (94, 64), (86, 82), (64, 88)]), 'shade', 'b', False)],
})

# Scout Messenger: piel tostada; pelo rosa malva en pinchos que suben hacia arriba y a un lado, con mechones que le caen por
# la frente; ojos azul grisáceo y boca seria
C('scout-messenger', {
    'body': 'normal', 'pal': pal('#c07880', '#c88a5a', iris='#6a8a9a', shade='#9e5c64', deep='#7c444a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(16, 66), (10, 44), (12, 20), (8, -2, 1), (24, 8), (30, -12, 1), (42, 2), (52, -14, 1), (60, 2), (74, -10, 1), (74, 10), (92, 4, 1), (86, 22),
                         (90, 44), (84, 66), (80, 52), (20, 52)])),
              L(outline([(58, 2), (74, -8), (74, 12), (90, 6), (86, 24), (90, 44), (84, 62), (78, 36)]), 'shade', 'b', False),
              fr([(14, 60), (12, 40), (28, 22), (54, 16), (76, 22), (88, 40), (86, 60), (78, 50), (66, 44), (56, 54, 1), (52, 42), (40, 44), (30, 52), (22, 58)]),
              strand([(40, 22), (30, 44)], 'deep', 'f', 1.0), strand([(64, 22), (74, 42)], 'deep', 'f', 1.0)] + marks(86, 26),
    'side': [L(outline([(66, 52), (76, 42), (90, 38), (98, 24, 1), (84, 18), (88, 2, 1), (70, 4), (66, -12, 1), (52, 2), (34, -10, 1), (28, 8), (10, 18), (4, 44), (8, 66),
                        (20, 80), (34, 76), (40, 62), (50, 56)])),
             L(outline([(5, 42), (30, 46), (40, 62), (34, 76), (20, 80), (8, 66)]), 'shade', 'b', False),
             fr([(74, 40), (90, 38), (92, 56, 1), (84, 50)])],
    'back': [L(outline([(16, 78), (10, 44), (12, 20), (8, -2, 1), (24, 8), (30, -12, 1), (42, 2), (52, -14, 1), (60, 2), (74, -10, 1), (74, 10), (92, 4, 1), (86, 22),
                        (90, 44), (84, 78), (50, 84)])),
             L(outline([(58, 2), (74, -8), (74, 12), (90, 6), (86, 24), (90, 44), (84, 76), (62, 82)]), 'shade', 'b', False)],
})

# Scrap Salvadge (portero): un penacho verde agua de hojas en lo alto de la cabeza y dos mechones azul marino largos y caídos
# a los lados como orejas de perro hasta la mandíbula; ojos redondos, nariz naranja y boca seria
C('scrap-salvadge', {
    'body': 'normal', 'pal': pal('#6aa898', '#eaa868', iris='#1e1a1a', shade='#4e8a7a', deep='#36685a', ear='#2a3a5a', ear_d='#1e2a44', nose='#f08a3a'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'frown', 'mouth_y': 95, 'nose': (50, 86, 3.4), 'hairline': False, 'ears': False},
    'front': [L(outline([(20, 30), (6, 50), (2, 80), (8, 100), (20, 98), (26, 76), (26, 44)]), 'ear'), L(outline([(80, 30), (94, 50), (98, 80), (92, 100), (80, 98), (74, 76),
                                                                                                               (74, 44)]), 'ear'),
              L(outline([(84, 40), (94, 54), (96, 84), (90, 96), (84, 80)]), 'ear_d', 'b', False),
              L(outline([(50, 40), (30, 34), (14, 20, 1), (32, 18), (24, 2, 1), (42, 10), (50, -6, 1), (58, 10), (76, 2, 1), (68, 18), (86, 20, 1), (70, 34)])),
              L(outline([(56, 8), (76, 4), (68, 20), (84, 22), (68, 34), (54, 38)]), 'shade', 'b', False),
              L(outline([(50, 30), (40, 48), (50, 60, 1), (60, 48)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(60, 30), (44, 40), (36, 70), (40, 100), (52, 98), (56, 70), (66, 44)]), 'ear', 'f'),
             L(outline([(70, 38), (52, 30), (36, 20, 1), (54, 16), (46, 0, 1), (62, 8), (70, -6, 1), (76, 10), (92, 6, 1), (84, 22), (96, 30, 1), (80, 36)]))],
    'back': [L(outline([(20, 30), (6, 50), (2, 80), (8, 100), (20, 98), (26, 76), (26, 44)]), 'ear'), L(outline([(80, 30), (94, 50), (98, 80), (92, 100), (80, 98), (74, 76),
                                                                                                              (74, 44)]), 'ear'),
             L(outline([(50, 40), (30, 34), (14, 20, 1), (32, 18), (24, 2, 1), (42, 10), (50, -6, 1), (58, 10), (76, 2, 1), (68, 18), (86, 20, 1), (70, 34)]))],
})

# Sean Lavender: bajito; una nube enorme de pelo rojo granate ahuecado alrededor de la cabeza, con el flequillo recto; colorete,
# cejas enfadadas y morros
C('sean-lavender', {
    'body': 'bajito', 'pal': pal('#a83a16', '#f6c49a', iris='#1e1a1a', shade='#86280c', deep='#661c06'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': False},
    'front': [L(cloud(50, 52, 58, 50, 9, 0.2, 0.86)), L(cloud(66, 44, 30, 34, 6, 0.4, 0.86), 'shade', 'b', False),
              bangs(62, 16, 84, 6, 30, jag=5), strand([(40, 32), (40, 58)], 'deep', 'f', 1.0), strand([(60, 32), (60, 58)], 'deep', 'f', 1.0)] + blush(86, dx=26),
    'side': [L(cloud(42, 50, 56, 50, 9, 0.2, 0.86)), L(cloud(30, 56, 28, 30, 6, 0.4, 0.86), 'shade', 'b', False), fr([(72, 40), (90, 42), (92, 60, 1), (82, 56)])],
    'back': [L(cloud(50, 52, 58, 50, 9, 0.2, 0.86)), L(cloud(64, 56, 32, 36, 6, 0.4, 0.86), 'shade', 'b', False)],
})
