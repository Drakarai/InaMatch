"""Ojeadores de IE1 (scouts-ie1), tanda 05: dibujados a partir de su retrato de Victory Road; claves 'scouts-ie1:<id>'.
Ninguno de esta tanda tiene modelo 3D salvo Gregory Smith (con su modelo de la enciclopedia): el perfil y la espalda están
deducidos del retrato."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, longhair, messy, outline, pal, rope, strand  # noqa: F401
from chars_alius import LONG_FACE, WIDE_FACE  # noqa: F401
from chars_bigwaves import bald, rect_glasses, side_eye, white_eyes  # noqa: F401
from chars_firedragon import bowl  # noqa: F401
from chars_vr_nikogawa import blush, brow_side, brows, crop, ring_glasses  # noqa: F401
from heads import quad  # noqa: F401

WHITE = (248, 248, 248, 255)
K = 'scouts-ie1:'
SKIN = '#f6bc84'  # la piel anaranjada de los retratos de IE1


def C(pid, spec):
    CHARS[K + pid] = spec


def fr(pts, c='mid'):
    """Mechones de delante de la cara (flequillo) con su contorno."""
    return L(outline(pts), c, 'f', ln=True)


def tie(view, x, y, c=(240, 236, 220, 255)):
    """Goma de pelo (una banda pequeña)."""
    return L(ell(x, y, 4, 2.6), c, 'f', ln=True)


# Fingus Inky: pelo azul marino muy oscuro en casco con la coronilla en pico y dos picos que bajan a las sienes; ojos
# redondos de pasmo, nariz naranja en triángulo y media sonrisa
C('fingus-inky', {
    'body': 'normal', 'pal': pal('#2e3a50', SKIN, shade='#232c3e', deep='#18202e', nose='#e07a34'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'nose': (50, 86, 3.4),
             'hairline': [(14, 68), (18, 50), (23, 62), (28, 48), (50, 42), (72, 48), (77, 62), (82, 50), (86, 68)]},
    'front': [L(outline([(17, 68), (12, 42), (22, 18), (40, 4), (50, -10, 1), (60, 4), (78, 18), (88, 42), (83, 68), (78, 50), (22, 50)])),
              L(outline([(58, 2), (78, 20), (88, 42), (84, 62), (76, 36)]), 'shade', 'b', False)],
    'side': [L(outline([(72, 50), (80, 40), (84, 22), (70, 6), (54, -8, 1), (46, 4), (24, 8), (8, 26), (4, 50), (10, 72), (22, 86), (34, 84), (38, 66), (46, 58),
                        (60, 56), (66, 62, 1)])),
             L(outline([(5, 46), (30, 48), (40, 62), (34, 84), (22, 86), (10, 72)]), 'shade', 'b', False)],
    'back': [L(outline([(17, 76), (12, 42), (22, 18), (40, 4), (50, -10, 1), (60, 4), (78, 18), (88, 42), (83, 76), (66, 86), (50, 88), (34, 86)])),
             L(outline([(58, 4), (80, 20), (88, 46), (83, 76), (64, 86)]), 'shade', 'b', False)],
})

# Finn Attick: melena corta lila grisácea hasta la nuca, que tapa las orejas y se abre en puntas hacia fuera, con la raya
# a un lado y el flequillo barrido; ojos verdes de pestaña marcada y sonrisa pícara
C('finn-attick', {
    'body': 'normal', 'pal': pal('#b49aa8', SKIN, iris='#3a9a6a', shade='#937a88', deep='#6e5866', light='#d8c4cc'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': False, 'ears': False},
    'front': [L(outline([(10, 98, 1), (12, 82), (6, 50), (14, 20), (36, 4), (60, 2), (84, 14), (94, 44), (90, 78), (96, 100, 1), (82, 90), (82, 60), (18, 60), (20, 90)])),
              L(outline([(62, 4), (86, 18), (94, 46), (90, 80), (94, 98), (82, 86), (80, 50)]), 'shade', 'b', False),
              fr([(14, 76), (14, 46), (26, 22), (48, 12), (70, 14), (86, 30), (88, 58), (78, 44), (66, 52), (70, 40), (54, 48), (50, 40), (36, 56), (36, 44),
                  (22, 62, 1)]),
              strand([(54, 16), (40, 40)], 'shade', 'f', 1.0), strand([(70, 18), (64, 38)], 'shade', 'f', 1.0)],
    'side': [L(outline([(70, 46), (82, 44), (90, 30), (82, 10), (58, -2), (30, 2), (10, 18), (2, 46), (4, 76), (-2, 98, 1), (14, 90), (24, 100, 1), (34, 90), (44, 98, 1),
                        (50, 82), (54, 62), (62, 54)])),
             L(outline([(4, 44), (30, 46), (44, 70), (44, 96), (24, 98), (6, 84)]), 'shade', 'b', False),
             fr([(66, 6), (88, 22), (92, 46), (86, 56, 1), (80, 40), (70, 30)])],
    'back': [L(outline([(10, 98, 1), (12, 80), (6, 48), (16, 18), (50, 2), (84, 18), (94, 48), (90, 80), (94, 98, 1), (80, 92), (70, 100, 1), (60, 92), (50, 100, 1),
                        (40, 92), (30, 100, 1), (22, 92)])),
             L(outline([(56, 4), (84, 18), (94, 48), (90, 80), (92, 96), (62, 90)]), 'shade', 'b', False),
             strand([(50, 8), (50, 40)], 'deep', 'b', 1.0)],
})

# Finn Carper (portero): un adulto de cara larga y mentón marcado; pelo castaño oliva en pinchos recogido arriba en una
# coleta corta con goma clara, y un mechón largo que le tapa un ojo; cicatriz cosida en la mejilla y ojos grises afilados
C('finn-carper', {
    'body': 'delgado', 'pal': pal('#5a4c2c', SKIN, iris='#8a8a9a', shade='#463a20', deep='#2e2614', light='#7e6e48'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 100, 'face_front': LONG_FACE, 'eye_y': 76,
             'hairline': [(16, 70), (18, 52), (28, 46), (44, 50), (56, 46), (72, 48), (82, 54), (84, 70)]},
    'front': [L(outline([(16, 70), (10, 46), (-2, 30, 1), (14, 24), (22, 8), (40, 0), (44, -18, 1), (52, -4), (60, -18, 1), (62, 0), (80, 8), (98, 14, 1), (88, 28),
                         (92, 44), (84, 70), (80, 52), (20, 52)])),
              L(outline([(60, 0), (80, 10), (88, 30), (90, 46), (84, 66), (76, 40)]), 'shade', 'b', False),
              L(outline([(42, -4), (50, -14), (58, -4), (50, 0)]), (232, 226, 200, 255), 'f', ln=True),
              fr([(54, 40), (66, 44), (74, 60), (74, 80), (70, 94, 1), (66, 74), (60, 58)]),
              L([(22, 84), (30, 96)], (150, 80, 60, 255), 'f', False, False, 1.2)]
             + [L([(22 + i * 2.6, 88 + i * 3.6), (28 + i * 2.6, 86 + i * 3.6)], (150, 80, 60, 255), 'f', False, False, 0.9) for i in range(3)],
    'side': [L(outline([(78, 54), (84, 44), (94, 36, 1), (86, 28), (84, 12), (70, 2), (60, -18, 1), (52, -2), (40, -14, 1), (34, 2), (14, 12), (4, 34), (-10, 44, 1),
                        (6, 56), (8, 74), (22, 86), (36, 82), (40, 64), (50, 56), (66, 56)])),
             L(outline([(6, 40), (30, 46), (40, 64), (36, 82), (22, 86), (8, 72)]), 'shade', 'b', False),
             L(outline([(46, -10), (56, -14), (60, -2), (50, 0)]), (232, 226, 200, 255), 'f', ln=True),
             fr([(82, 42), (90, 52), (92, 70), (88, 80, 1), (84, 62)])],
    'back': [L(outline([(16, 76), (10, 46), (-4, 32, 1), (12, 24), (22, 8), (40, 2), (44, -16, 1), (52, -4), (60, -16, 1), (62, 2), (80, 8), (100, 18, 1), (88, 28),
                        (92, 46), (84, 76), (66, 84), (50, 86), (34, 84)])),
             L(outline([(56, 4), (82, 14), (90, 44), (84, 76), (62, 84)]), 'shade', 'b', False),
             L(outline([(42, -4), (50, -14), (58, -4), (50, 0)]), (232, 226, 200, 255), 'f', ln=True)],
})

# Finn Sawyer (portero): grandullón de cara ancha y mandíbula cuadrada; melena rosa ondulada hasta la nuca, ahuecada a
# los lados y con el flequillo partido; ojos blancos redondos de pupila pequeña, cejas enfadadas y sonrisa torcida
C('finn-sawyer', {
    'body': 'corpulento', 'pal': pal('#f0a2a6', SKIN, shade='#d6848a', deep='#b0646c', light='#fac8c8'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'face_front': WIDE_FACE, 'hairline': False, 'ears': False},
    'front': [L(outline([(-2, 90), (-6, 70), (0, 40), (14, 12), (40, 0), (62, 0), (88, 12), (102, 40), (106, 70), (102, 90), (90, 92), (86, 60), (14, 60), (10, 92)])),
              L(outline([(62, 2), (88, 14), (102, 40), (104, 86), (90, 90), (86, 50)]), 'shade', 'b', False),
              fr([(8, 80), (8, 50), (20, 24), (40, 14), (60, 14), (80, 24), (92, 50), (92, 80), (84, 62), (76, 54), (66, 60), (58, 44), (50, 54), (42, 44), (34, 58),
                  (24, 54), (16, 64)]),
              strand([(30, 22), (22, 50)], 'shade', 'f', 1.0), strand([(70, 22), (78, 50)], 'shade', 'f', 1.0)]
             + white_eyes(76, 15, 6.2, 5.2, 1.6)
             + [L([(29, 63), (43, 68)], OUTC, 'f', False, False, 3.0), L([(71, 63), (57, 68)], OUTC, 'f', False, False, 3.0)],
    'side': [L(outline([(72, 52), (86, 44), (94, 28), (84, 8), (58, -2), (30, 2), (8, 18), (-4, 46), (-6, 76), (0, 94), (18, 96), (34, 92), (46, 84), (52, 66), (62, 56)])),
             L(outline([(-4, 46), (30, 50), (46, 74), (40, 92), (16, 96), (0, 92)]), 'shade', 'b', False),
             fr([(72, 10), (92, 26), (96, 48), (88, 62, 1), (82, 44), (74, 34)])]
            + side_eye(76),
    'back': [L(outline([(-2, 92), (-6, 70), (0, 40), (14, 12), (50, 0), (86, 12), (100, 40), (106, 70), (102, 92), (80, 98), (50, 100), (20, 98)])),
             L(outline([(58, 4), (86, 14), (100, 42), (104, 90), (64, 98)]), 'shade', 'b', False),
             strand([(30, 20), (24, 90)], 'shade', 'b', 1.0), strand([(50, 10), (50, 94)], 'shade', 'b', 1.0), strand([(70, 20), (76, 90)], 'shade', 'b', 1.0)],
})

# Flora Reinhold: chica de pelo castaño claro con un flequillo en caracol sobre la frente y una coleta de lado (a su
# izquierda) atada con un lazo rojo; ojos castaños y colorete
C('flora-reinhold', {
    'body': 'chica', 'pal': pal('#b48c64', '#fcd8b4', iris='#6a4a2a', shade='#946e4a', deep='#6e5034', light='#d4b490', ribbon='#c8382c'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 93, 'hairline': False},
    'front': [L(outline([(14, 70), (8, 42), (16, 16), (40, 2), (64, 2), (86, 16), (94, 42), (88, 70), (82, 56), (18, 56)])),
              L(outline([(62, 4), (86, 18), (94, 44), (88, 66), (80, 38)]), 'shade', 'b', False),
              L(rope((90, 54), (110, 74), (100, 108), 16), 'mid', 'b'), L(rope((92, 62), (106, 82), (98, 104), 6), 'shade', 'b', False),
              fr([(14, 66), (14, 40), (26, 20), (50, 12), (74, 18), (86, 36), (88, 62), (80, 46), (68, 52), (58, 40), (48, 54), (36, 50), (22, 62, 1)]),
              L(outline([(30, 22), (46, 18), (52, 30), (44, 40), (36, 36), (42, 30)]), 'shade', 'f', ln=True),
              L(outline([(86, 48), (98, 40), (100, 52), (96, 60), (100, 70), (88, 64)]), 'ribbon', 'f', ln=True)]
             + blush(86),
    'side': [L(outline([(70, 46), (84, 44), (90, 28), (80, 8), (56, -2), (30, 2), (10, 18), (2, 44), (8, 68), (20, 80), (36, 78), (44, 62), (58, 52)])),
             L(rope((20, 56), (-4, 76), (6, 108), 16), 'mid', 'b'),
             L(outline([(4, 42), (30, 46), (40, 64), (34, 78), (20, 80), (8, 68)]), 'shade', 'b', False),
             L(outline([(14, 50), (26, 44), (28, 56), (22, 62), (26, 72), (14, 66)]), 'ribbon', 'f', ln=True),
             fr([(68, 8), (88, 22), (92, 46), (86, 54, 1), (80, 40), (70, 30)])],
    'back': [L(outline([(14, 76), (8, 44), (16, 16), (50, 2), (84, 16), (92, 44), (86, 76), (66, 84), (50, 86), (34, 84)])),
             L(rope((16, 56), (-8, 78), (2, 108), 16), 'mid', 'b'),
             L(outline([(56, 4), (84, 18), (92, 46), (86, 76), (62, 84)]), 'shade', 'b', False),
             L(outline([(10, 50), (22, 44), (24, 56), (18, 62), (22, 72), (10, 66)]), 'ribbon', 'f', ln=True)],
})

# Florian Hutter: pelo rubio en tazón con el flequillo recto de mechones y un ricito tieso en lo alto; dos manchas grandes
# azul oscuro alrededor de los ojos (cara de mapache), ojos medio cerrados, nariz naranja y boca seria
C('florian-hutter', {
    'body': 'bajito', 'pal': pal('#e6cc74', SKIN, shade='#c8aa52', deep='#a08436', light='#f6e6a8', mask='#2e4a6e', nose='#e07a34'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 95, 'nose': (50, 86, 3.4), 'hairline': False},
    'front': bowl('front', fringe_y=58)
             + [fr([(10, 68), (10, 40), (22, 18), (50, 10), (78, 18), (90, 40), (90, 68), (82, 62), (76, 66), (70, 58), (62, 64), (56, 56), (50, 64), (44, 56), (38, 64),
                    (30, 58), (24, 66), (18, 62)]),
                L(quad((50, 2), (40, -14), (54, -14)), 'mid', 'b', False, False, 2.6)]
             + [strand([(x, 24), (x, 54)], 'shade', 'f', 1.0) for x in (24, 38, 50, 62, 76)]
             + [L(ell(36, 76, 9.5, 8.5), 'mask', 'f', ln=True), L(ell(64, 76, 9.5, 8.5), 'mask', 'f', ln=True)]
             + white_eyes(77, 14, 4.6, 4.2, 1.8, 0.5),
    'side': bowl('side') + [L(quad((52, 2), (44, -14), (58, -14)), 'mid', 'b', False, False, 2.6), L(ell(83, 76, 6, 8), 'mask', 'f', ln=True)] + side_eye(77, 0.5),
    'back': bowl('back') + [L(quad((50, 2), (40, -14), (54, -14)), 'mid', 'b', False, False, 2.6)],
})

# Florian Selles: pelo castaño muy corto y erizado en pinchos cortos por todo el borde, como un cepillo; cejas gruesas
# de bloque fruncidas, ojos pequeños de punto y boca seria
C('florian-selles', {
    'body': 'normal', 'pal': pal('#8a4c1e', SKIN, shade='#6e3a14', deep='#4e280c', brow='#8a4c1e'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'frown', 'mouth_y': 94,
             'hairline': [(16, 66), (18, 54), (30, 50), (50, 52), (70, 50), (82, 54), (84, 66)]},
    'front': messy('front', amp=6, n=16, seed=5, rx=42, ry=36, cy=42, lo=64)
             + brows(65, 'brow', 4.6, 15, 0.8, 13),
    'side': messy('side', amp=6, n=14, seed=5, rx=40, ry=36, cy=40, nape=86) + brow_side(65, 'brow', 4.6, 0.8),
    'back': messy('back', amp=6, n=16, seed=5, rx=42, ry=36, cy=42, nape=86),
})

# Fontaine Tapper: pelo naranja rojizo recogido arriba en un moño de pinchos tiesos, con la raya en medio y el pelo
# estirado por los lados; ojos afilados de enfado y boca seria
C('fontaine-tapper', {
    'body': 'normal', 'pal': pal('#d2541e', SKIN, iris='#2a2020', shade='#b03e14', deep='#8a2e0c', light='#ec8a50'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95,
             'hairline': [(16, 66), (18, 50), (30, 42), (46, 40), (50, 46), (54, 40), (70, 42), (82, 50), (84, 66)]},
    'front': [L(outline([(16, 66), (12, 42), (22, 18), (50, 8), (78, 18), (88, 42), (84, 66), (80, 50), (20, 50)])),
              L(outline([(58, 10), (78, 20), (88, 42), (84, 62), (76, 34)]), 'shade', 'b', False),
              L(outline([(40, 12), (22, -6, 1), (42, 2), (36, -24, 1), (48, -4), (54, -30, 1), (58, -4), (74, -16, 1), (64, 4), (82, 2, 1), (62, 14)])),
              L(outline([(54, -4), (74, -16), (64, 4), (60, 12)]), 'shade', 'b', False),
              strand([(50, 12), (50, 40)], 'deep', 'b', 1.0), strand([(36, 16), (26, 40)], 'shade', 'b', 1.0), strand([(64, 16), (74, 40)], 'shade', 'b', 1.0)],
    'side': [L(outline([(70, 50), (82, 44), (86, 26), (74, 10), (52, 4), (28, 8), (10, 24), (4, 48), (10, 70), (22, 84), (34, 82), (38, 64), (46, 56), (60, 54)])),
             L(outline([(26, 10), (6, -10, 1), (28, -4), (26, -26, 1), (40, -6), (54, -24, 1), (54, -2), (72, -10, 1), (56, 10)])),
             L(outline([(5, 46), (30, 48), (40, 62), (34, 82), (22, 84), (10, 70)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 74), (12, 42), (22, 18), (50, 8), (78, 18), (88, 42), (84, 74), (66, 84), (50, 86), (34, 84)])),
             L(outline([(56, 10), (80, 20), (88, 46), (84, 74), (62, 84)]), 'shade', 'b', False),
             L(outline([(40, 14), (22, -4, 1), (42, 2), (36, -22, 1), (48, -4), (54, -28, 1), (58, -4), (74, -14, 1), (64, 4), (80, 4, 1), (62, 14)]))],
})

# Fox Copier: adulto de piel morena con melena rizada castaño rojiza hasta la mandíbula; unas gafas redondas enormes de
# cristal blanco con montura verde, labios gruesos naranjas y cara de preocupación
C('fox-copier', {
    'body': 'delgado', 'pal': pal('#c2501e', '#c8844e', shade='#9a3c14', deep='#72280c', light='#e2804a', frame='#4a8a7a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'lips', 'mouth_y': 95, 'mouth_w': 8, 'hairline': False},
    'front': [L(outline([(8, 90, 1), (0, 70), (6, 44), (2, 24), (18, 6), (40, -2), (62, -2), (84, 6), (98, 24), (94, 44), (100, 70), (92, 90, 1), (84, 74), (84, 56),
                         (16, 56), (16, 74)])),
              L(outline([(62, 0), (86, 8), (98, 26), (94, 46), (98, 70), (90, 86), (84, 50)]), 'shade', 'b', False),
              strand([(22, 14), (30, 28), (24, 40)], 'deep', 'b', 1.0), strand([(50, 4), (56, 18), (50, 34)], 'deep', 'b', 1.0), strand([(76, 14), (70, 28), (78, 40)], 'deep', 'b', 1.0),
              L([(30, 62), (42, 60)], OUTC, 'f', False, False, 1.8), L([(70, 62), (58, 60)], OUTC, 'f', False, False, 1.8)]
             + [L(ell(cx, 75, 10, 9), WHITE, 'f', False) for cx in (36, 64)]
             + [L(ell(cx, 75, 10, 9) + [ell(cx, 75, 10, 9)[0]], 'frame', 'f', False, False, 2.4) for cx in (36, 64)]
             + [L([(46, 74), (54, 74)], 'frame', 'f', False, False, 1.8)],
    'side': [L(outline([(70, 48), (84, 44), (92, 26), (80, 6), (56, -4), (30, 0), (10, 16), (2, 40), (-4, 66), (2, 88, 1), (14, 80), (22, 92, 1), (30, 80), (40, 86, 1),
                        (44, 66), (52, 56), (60, 52)])),
             L(outline([(2, 40), (30, 46), (42, 66), (38, 84), (20, 88), (2, 80)]), 'shade', 'b', False),
             L(ell(84, 75, 6, 9), WHITE, 'f', False), L(ell(84, 75, 6, 9) + [ell(84, 75, 6, 9)[0]], 'frame', 'f', False, False, 2.4),
             L([(78, 74), (50, 70)], 'frame', 'f', False, False, 1.8)],
    'back': [L(outline([(8, 90, 1), (0, 70), (6, 44), (2, 24), (18, 6), (50, -2), (82, 6), (98, 24), (94, 44), (100, 70), (92, 90, 1), (80, 82), (70, 92, 1), (60, 84),
                        (50, 94, 1), (40, 84), (30, 92, 1), (20, 82)])),
             L(outline([(58, 0), (84, 8), (98, 28), (94, 46), (98, 70), (92, 88), (62, 86)]), 'shade', 'b', False)]
            + [strand([(x, 10), (x + 4, 40), (x - 2, 70)], 'deep', 'b', 1.0) for x in (24, 46, 68)],
})

# Fran Zimmer: chica de pelo azul verdoso recogido en un moño alto con una goma amarilla, del que sale una cola curva hacia
# un lado; dos mechones largos que le enmarcan la cara hasta la barbilla; ojos verdes afilados y sonrisa
C('fran-zimmer', {
    'body': 'chica', 'pal': pal('#5a9ab0', SKIN, iris='#4a8a3a', shade='#447a8e', deep='#2e5a6a', light='#8cc0d0', band='#e2c46a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93,
             'hairline': [(16, 66), (18, 50), (30, 44), (44, 46), (50, 40), (56, 46), (70, 44), (82, 50), (84, 66)]},
    'front': [L(outline([(16, 66), (12, 42), (22, 18), (50, 8), (78, 18), (88, 42), (84, 66), (80, 50), (20, 50)])),
              L(outline([(58, 10), (78, 20), (88, 42), (84, 62), (76, 34)]), 'shade', 'b', False),
              L(outline([(36, 14), (34, -10), (50, -20), (66, -10), (64, 14)])),
              L(rope((38, -14), (20, -18), (16, -4), 9), 'mid', 'b'),
              L(outline([(34, 4), (66, 4), (66, 14), (34, 14)]), 'band', 'f', ln=True),
              strand([(44, -14), (46, 2)], 'shade', 'b', 1.0), strand([(56, -14), (54, 2)], 'shade', 'b', 1.0),
              fr([(14, 52), (20, 74), (24, 98, 1), (26, 76), (26, 54)]), fr([(86, 52), (80, 74), (76, 98, 1), (74, 76), (74, 54)])],
    'side': [L(outline([(70, 50), (82, 44), (86, 26), (74, 10), (52, 4), (28, 8), (10, 24), (4, 48), (10, 70), (22, 84), (34, 82), (38, 64), (46, 56), (60, 54)])),
             L(outline([(30, 10), (32, -14), (50, -22), (62, -12), (58, 8)])),
             L(rope((36, -14), (14, -16), (12, 0), 9), 'mid', 'b'),
             L(outline([(30, 0), (60, 0), (58, 10), (32, 12)]), 'band', 'f', ln=True),
             L(outline([(5, 46), (30, 48), (40, 62), (34, 82), (22, 84), (10, 70)]), 'shade', 'b', False),
             fr([(76, 50), (82, 70), (80, 96, 1), (76, 74), (72, 54)])],
    'back': [L(outline([(16, 74), (12, 42), (22, 18), (50, 8), (78, 18), (88, 42), (84, 74), (66, 84), (50, 86), (34, 84)])),
             L(outline([(56, 10), (80, 20), (88, 46), (84, 74), (62, 84)]), 'shade', 'b', False),
             L(outline([(36, 14), (34, -10), (50, -20), (66, -10), (64, 14)])), L(rope((62, -14), (80, -18), (84, -4), 9), 'mid', 'b'),
             L(outline([(34, 4), (66, 4), (66, 14), (34, 14)]), 'band', 'f', ln=True)],
})

# Francis Paine: una mata enorme de pelo azul verdoso, ahuecada y en mechones gruesos que se abren a los lados, con el
# flequillo recto de puntas; ojos grandes redondos y sonrisa
C('francis-paine', {
    'body': 'normal', 'pal': pal('#5e94aa', SKIN, shade='#46788e', deep='#30586a', light='#8ebccc'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'smile', 'mouth_y': 93, 'hairline': False},
    'front': [L(outline([(6, 86), (-10, 74, 1), (-4, 56), (-14, 40, 1), (0, 28), (2, 8, 1), (20, 4), (28, -14, 1), (42, -2), (52, -18, 1), (60, -2), (76, -12, 1), (82, 4),
                         (100, 8, 1), (100, 28), (114, 40, 1), (104, 56), (110, 76, 1), (94, 86), (84, 64), (16, 64)])),
              L(outline([(58, -4), (80, 4), (102, 30), (106, 60), (96, 82), (86, 54)]), 'shade', 'b', False),
              fr([(14, 66), (14, 40), (28, 24), (50, 18), (72, 24), (86, 40), (86, 66), (80, 56), (74, 64), (68, 54), (62, 64), (56, 54), (50, 64), (44, 54), (38, 64),
                  (32, 54), (26, 64), (20, 56)])],
    'side': [L(outline([(74, 50), (88, 44), (96, 24), (86, 2), (62, -14), (32, -10), (8, 6), (-8, 30), (-14, 56), (-4, 80), (12, 92), (30, 90), (40, 74), (50, 60),
                        (62, 56)])),
             L(outline([(-10, 40), (30, 46), (42, 70), (30, 90), (8, 90), (-6, 76)]), 'shade', 'b', False),
             fr([(70, 8), (92, 22), (96, 46), (90, 58, 1), (84, 40), (74, 30)])],
    'back': [L(outline([(6, 88), (-10, 76, 1), (-4, 56), (-14, 40, 1), (0, 28), (2, 8, 1), (20, 4), (28, -14, 1), (42, -2), (52, -18, 1), (60, -2), (76, -12, 1), (82, 4),
                        (100, 8, 1), (100, 28), (114, 40, 1), (104, 56), (110, 78, 1), (94, 88), (72, 94), (50, 96), (28, 94)])),
             L(outline([(58, -4), (80, 4), (102, 30), (106, 60), (96, 86), (64, 94)]), 'shade', 'b', False)],
})

# Frank Drake: pelo verde oliva oscuro con mechas verdes más claras que salen de la coronilla, un mechón tieso que se
# levanta en curva y mechones a los lados de la cara; ojos verde oliva, un arañazo en la mejilla y sonrisa pícara
C('frank-drake', {
    'body': 'normal', 'pal': pal('#3e4a2e', SKIN, iris='#6a6a2a', shade='#2e3822', deep='#1e2616', light='#6a8a4a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93,
             'hairline': [(16, 70), (18, 52), (28, 46), (44, 50), (56, 44), (72, 48), (82, 54), (84, 70)]},
    'front': [L(outline([(16, 70), (12, 42), (22, 18), (50, 8), (78, 18), (88, 42), (84, 70), (80, 52), (20, 52)])),
              L(outline([(58, 10), (78, 20), (88, 42), (84, 62), (76, 34)]), 'shade', 'b', False),
              L(quad((50, 10), (50, -14), (74, -20)), 'mid', 'b', False, False, 3.2)]
             + [strand([(50, 14), (x, y)], 'light', 'b', 1.4) for x, y in ((22, 30), (30, 22), (40, 18), (62, 18), (72, 22), (80, 32), (26, 44), (76, 44))]
             + [fr([(16, 56), (22, 70), (24, 86, 1), (28, 66), (28, 54)]), fr([(84, 56), (78, 70), (76, 86, 1), (72, 66), (72, 54)]),
                L([(64, 84), (70, 90)], (150, 80, 60, 255), 'f', False, False, 1.0), L([(70, 84), (64, 90)], (150, 80, 60, 255), 'f', False, False, 1.0)],
    'side': crop('side', top=8, nape=86) + [L(quad((54, 8), (56, -14), (78, -20)), 'mid', 'b', False, False, 3.2)]
            + [strand([(50, 12), (x, y)], 'light', 'b', 1.4) for x, y in ((80, 22), (70, 14), (24, 20), (12, 40))]
            + [fr([(76, 44), (84, 64), (84, 84, 1), (78, 64), (72, 52)])],
    'back': crop('back', top=8, nape=86) + [L(quad((50, 10), (50, -14), (26, -20)), 'mid', 'b', False, False, 3.2)]
            + [strand([(50, 14), (x, y)], 'light', 'b', 1.4) for x, y in ((20, 40), (30, 70), (50, 80), (70, 70), (80, 40))],
})

# Frank Koshar: un adulto de frente muy despejada: el pelo rubio pajizo peinado hacia atrás, ralo arriba, con dos matas
# rizadas a los lados por encima de las orejas; nariz larga, ojos afilados y ceño fruncido
C('frank-koshar', {
    'body': 'delgado', 'pal': pal('#c8b070', SKIN, shade='#a89052', deep='#7e6a38', light='#e2d09a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 99, 'face_front': LONG_FACE, 'eye_y': 76, 'nose': (50, 88, 2.6), 'ears_front': True,
             'hairline': [(16, 60), (22, 34), (36, 20), (50, 22), (64, 20), (78, 34), (84, 60)]},
    'front': [L(outline([(16, 62), (14, 36), (26, 14), (50, 8), (74, 14), (86, 36), (84, 62), (80, 40), (20, 40)])),
              L(outline([(58, 10), (76, 18), (86, 38), (84, 58), (78, 32)]), 'shade', 'b', False),
              strand([(50, 10), (48, 22)], 'deep', 'b', 1.0),
              L(outline([(16, 52), (4, 48), (-2, 60), (4, 72), (0, 82), (10, 88), (18, 80)]), 'mid', 'f', ln=True),
              L(outline([(84, 52), (96, 48), (102, 60), (96, 72), (100, 82), (90, 88), (82, 80)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(68, 30), (80, 22), (70, 10), (50, 6), (28, 10), (10, 26), (2, 50), (-6, 64), (2, 78), (14, 88), (30, 86), (36, 70), (34, 52), (46, 40)])),
             L(outline([(4, 46), (26, 48), (34, 70), (28, 86), (12, 86), (0, 72)]), 'shade', 'b', False)],
    'back': [L(outline([(10, 82), (-2, 70), (4, 56), (8, 36), (22, 14), (50, 6), (78, 14), (92, 36), (96, 56), (102, 70), (90, 82), (66, 86), (50, 88), (34, 86)])),
             L(outline([(58, 8), (80, 18), (92, 40), (100, 70), (90, 82), (64, 86)]), 'shade', 'b', False)],
})

# Frank Meyer: piel morena oscura y una mata ahuecada de pelo amarillo oro en mechones redondos, con una cinta de rayas
# crema y granate en la frente; ojos pequeños, nariz redonda y boca seria
C('frank-meyer', {
    'body': 'normal', 'pal': pal('#e0b828', '#b07a4a', shade='#c09418', deep='#94700e', light='#f2d860', band='#f0e2c8', band2='#7a3a3a', nose='#9a6438'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'frown', 'mouth_y': 95, 'nose': (50, 86, 3.4), 'hairline': False},
    'front': [L(outline([(10, 80), (-6, 70, 1), (0, 52), (-10, 38, 1), (4, 26), (4, 6, 1), (24, 4), (32, -10, 1), (46, 0), (54, -12, 1), (62, 0), (78, -6, 1), (82, 8),
                         (100, 12, 1), (96, 30), (108, 42, 1), (100, 54), (104, 72, 1), (90, 80), (84, 60), (16, 60)])),
              L(outline([(58, -2), (82, 8), (100, 32), (102, 60), (92, 78), (86, 52)]), 'shade', 'b', False),
              L(outline([(16, 62), (16, 46), (30, 36), (50, 32), (70, 36), (84, 46), (84, 62), (70, 52), (50, 48), (30, 52)]), 'band', 'f', ln=True)]
             + [L(quad((x, 52 - abs(x - 50) * 0.1 - 10), (x + 4, 46 - abs(x - 50) * 0.1 - 2), (x + 6, 54 - abs(x - 50) * 0.1)), 'band2', 'f', False, False, 2.4)
                for x in (22, 34, 46, 58, 70)],
    'side': [L(outline([(74, 50), (88, 44), (96, 24), (86, 4), (62, -10), (32, -8), (8, 8), (-6, 32), (-12, 54), (-2, 74), (14, 86), (32, 84), (40, 70), (50, 58),
                        (62, 54)])),
             L(outline([(-8, 40), (28, 46), (40, 66), (30, 84), (10, 84), (-4, 72)]), 'shade', 'b', False),
             L(outline([(52, 42), (66, 30), (86, 30), (90, 42), (72, 44), (58, 54)]), 'band', 'f', ln=True),
             L([(64, 34), (70, 42)], 'band2', 'f', False, False, 2.4), L([(76, 32), (80, 42)], 'band2', 'f', False, False, 2.4)],
    'back': [L(outline([(10, 84), (-6, 72, 1), (0, 52), (-10, 38, 1), (4, 26), (4, 6, 1), (24, 4), (32, -10, 1), (46, 0), (54, -12, 1), (62, 0), (78, -6, 1), (82, 8),
                        (100, 12, 1), (96, 30), (108, 42, 1), (100, 54), (106, 74, 1), (90, 84), (70, 90), (50, 92), (30, 90)])),
             L(outline([(58, -2), (82, 8), (100, 32), (102, 60), (92, 82), (64, 90)]), 'shade', 'b', False)],
})

# Fred Ferrel: melena gris parda en mechones de punta, revuelta y hasta la nuca, con una cinta verde atada en la frente;
# cejas gruesas, dos rayas en las mejillas y sonrisa
C('fred-ferrel', {
    'body': 'normal', 'pal': pal('#8c8472', SKIN, shade='#6e6858', deep='#4e4a3e', light='#aca694', band='#8aaa4a', band_d='#6a8a32'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(6, 92, 1), (8, 70), (-6, 56, 1), (6, 44), (0, 22, 1), (16, 16), (20, -2, 1), (36, 6), (46, -12, 1), (56, 4), (70, -6, 1), (74, 10), (94, 10, 1),
                         (88, 24), (104, 40, 1), (92, 48), (104, 64, 1), (92, 70), (94, 92, 1), (84, 82), (84, 60), (16, 60), (16, 82)])),
              L(outline([(58, 2), (86, 14), (100, 42), (96, 86), (84, 74), (82, 40)]), 'shade', 'b', False),
              L(outline([(12, 60), (12, 46), (30, 40), (50, 38), (70, 40), (88, 46), (88, 60), (70, 54), (50, 52), (30, 54)]), 'band', 'f', ln=True),
              L([(18, 52), (82, 52)], 'band_d', 'f', False, False, 1.0)]
             + brows(63, OUTC, 4.0, 15, 0.4, 13)
             + [L([(26, 84), (32, 82)], (150, 80, 60, 255), 'f', False, False, 1.2), L([(26, 87), (32, 85)], (150, 80, 60, 255), 'f', False, False, 1.2),
                L([(74, 84), (68, 82)], (150, 80, 60, 255), 'f', False, False, 1.2), L([(74, 87), (68, 85)], (150, 80, 60, 255), 'f', False, False, 1.2)],
    'side': [L(outline([(72, 48), (86, 44), (94, 30, 1), (86, 22), (90, 4, 1), (72, 6), (66, -10, 1), (52, 0), (34, -8, 1), (30, 6), (8, 10, 1), (12, 26), (-6, 40, 1),
                        (6, 50), (-6, 66, 1), (8, 72), (4, 94, 1), (20, 84), (30, 96, 1), (38, 80), (46, 62), (58, 54)])),
             L(outline([(2, 44), (30, 48), (42, 66), (36, 84), (20, 86), (6, 76)]), 'shade', 'b', False),
             L(outline([(34, 40), (56, 34), (88, 38), (90, 50), (58, 48), (36, 52)]), 'band', 'f', ln=True),
             L(rope((36, 46), (20, 50), (12, 62), 5), 'band', 'f')] + brow_side(63, OUTC, 4.0, 0.4),
    'back': [L(outline([(6, 94, 1), (8, 70), (-6, 56, 1), (6, 44), (0, 22, 1), (16, 16), (20, -2, 1), (36, 6), (46, -12, 1), (56, 4), (70, -6, 1), (74, 10), (94, 10, 1),
                        (88, 24), (104, 40, 1), (92, 48), (104, 64, 1), (92, 72), (94, 94, 1), (80, 86), (70, 98, 1), (60, 88), (50, 100, 1), (40, 88), (30, 98, 1),
                        (20, 86)])),
             L(outline([(58, 2), (86, 14), (100, 42), (96, 90), (64, 92)]), 'shade', 'b', False),
             L(outline([(12, 50), (30, 44), (50, 42), (70, 44), (88, 50), (88, 60), (50, 54), (12, 60)]), 'band', 'f', ln=True),
             L(rope((50, 54), (44, 66), (36, 76), 5), 'band', 'f'), L(rope((50, 54), (56, 66), (64, 76), 5), 'band', 'f')],
})

# Fred Makepeace: pelo castaño malva peinado hacia arriba en un tupé de punta, con mechones que salen en pico por los
# lados; ojos verdes y sonrisa tranquila
C('fred-makepeace', {
    'body': 'normal', 'pal': pal('#8c6a6a', SKIN, iris='#2a9a6a', shade='#705252', deep='#523a3a', light='#b09090'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93,
             'hairline': [(16, 66), (18, 50), (30, 44), (50, 40), (70, 44), (82, 50), (84, 66)]},
    'front': [L(outline([(17, 66), (12, 46), (2, 40, 1), (12, 32), (16, 18), (8, 12, 1), (24, 10), (40, 0), (50, -14, 1), (60, 0), (76, 10), (92, 12, 1), (84, 18), (88, 32),
                         (98, 40, 1), (88, 46), (83, 66), (78, 50), (22, 50)])),
              L(outline([(56, 0), (76, 12), (86, 32), (86, 58), (76, 34)]), 'shade', 'b', False)]
             + [strand([(50, -10), (x, 40)], 'deep', 'b', 1.0) for x in (36, 44, 56, 64)],
    'side': [L(outline([(72, 50), (82, 44), (90, 26), (78, 6), (62, -10, 1), (52, 2), (28, 6), (14, 14, 1), (16, 22), (4, 36, 1), (8, 44), (6, 64), (14, 80), (30, 82),
                        (38, 66), (46, 58), (60, 54)])),
             L(outline([(6, 44), (30, 48), (40, 64), (30, 82), (14, 80), (6, 64)]), 'shade', 'b', False)],
    'back': [L(outline([(17, 76), (12, 46), (2, 40, 1), (12, 32), (16, 18), (8, 12, 1), (24, 10), (40, 0), (50, -12, 1), (60, 0), (76, 10), (92, 12, 1), (84, 18),
                        (88, 32), (98, 40, 1), (88, 46), (83, 76), (66, 84), (50, 86), (34, 84)])),
             L(outline([(56, 2), (78, 14), (88, 40), (83, 76), (62, 84)]), 'shade', 'b', False)],
})


def lids(y=76, sep=15, w=8):
    """Párpados caídos de sueño: una raya gruesa recta sobre medio ojo."""
    return [L([(50 - sep - w, y - 1), (50 - sep + w, y - 1)], OUTC, 'f', False, False, 2.4), L([(50 + sep - w, y - 1), (50 + sep + w, y - 1)], OUTC, 'f', False, False, 2.4)]


def wide_smile_(y=93, x0=36, x1=64, d=5):
    return [L(quad((x0, y - 2), (50, y + d), (x1, y - 2)), (130, 70, 50, 255), 'f', False, False, 1.6)]


def o_mouth(y=95, c=(150, 70, 60, 255)):
    return [L(ell(50, y, 3.6, 3.0), c, 'f', ln=True), L(ell(50, y + 0.4, 1.8, 1.4), (90, 40, 36, 255), 'f', False)]


# Fry Vollity: cara larga; pelo rosa rojizo peinado hacia arriba en un tupé alto que se inclina hacia un lado, con las
# patillas en cuña; cejas gruesas rosas, ojos de sueño medio cerrados y sonrisa
C('fry-vollity', {
    'body': 'delgado', 'pal': pal('#d07a7e', SKIN, shade='#b05e64', deep='#8a4448', light='#e8a2a4'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 97, 'face_front': LONG_FACE,
             'hairline': [(16, 62), (20, 46), (26, 64), (30, 46), (50, 40), (70, 46), (74, 64), (80, 46), (84, 62)]},
    'front': [L(outline([(17, 64), (14, 40), (20, 18), (30, -6), (44, -24), (64, -26), (76, -14), (80, 6), (86, 30), (86, 46), (83, 64), (78, 50), (22, 50)])),
              L(outline([(56, -22), (74, -14), (80, 8), (86, 36), (84, 56), (70, 20)]), 'shade', 'b', False),
              strand([(54, -20), (46, 10), (40, 36)], 'deep', 'b', 1.2), strand([(66, -20), (64, 10), (60, 36)], 'deep', 'b', 1.2)]
             + brows(64, 'mid', 4.2, 15, 0.0, 14) + white_eyes(76, 15, 6, 5, 1.8, 1.6),
    'side': [L(outline([(72, 50), (84, 42), (88, 22), (82, -2), (68, -24), (48, -26), (32, -14), (16, 4), (6, 28), (4, 50), (10, 72), (22, 84), (34, 82), (38, 66), (46, 56),
                        (60, 54)])),
             L(outline([(5, 46), (30, 48), (40, 62), (34, 82), (22, 84), (10, 70)]), 'shade', 'b', False)]
            + brow_side(64, 'mid', 4.2) + side_eye(76, 1.6),
    'back': [L(outline([(17, 76), (12, 42), (18, 16), (30, -6), (44, -22), (64, -24), (76, -12), (82, 10), (88, 42), (83, 76), (66, 84), (50, 86), (34, 84)])),
             L(outline([(56, -20), (76, -10), (84, 16), (88, 44), (83, 76), (62, 84)]), 'shade', 'b', False)],
})

# Gabriel Shekinah: gorra de béisbol azul marino con una V amarilla, el pelo oscuro asomando por los lados; ojos de sueño,
# nariz naranja en triángulo, dos tiritas granates en las mejillas y una sonrisa ancha
NAVY_CAP = (52, 68, 102, 255)
C('gabriel-shekinah', {
    'body': 'normal', 'pal': pal('#3a3030', SKIN, shade='#2a2222', deep='#1a1414', cap=NAVY_CAP, cap_d=(38, 50, 76, 255), logo='#e8d070', nose='#e07a34', patch='#b07a74'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'nose': (50, 85, 3.8), 'hairline': False},
    'front': crop('front', top=10, side=64)
             + [L(outline([(10, 54), (10, 30), (22, 10), (50, 2), (78, 10), (90, 30), (90, 54), (50, 52)]), 'cap', 'f', ln=True),
                L(outline([(58, 6), (80, 14), (90, 32), (90, 52), (74, 52), (72, 26)]), 'cap_d', 'f', False),
                L(outline([(8, 58), (14, 50), (50, 46), (86, 50), (92, 58), (50, 56)]), 'cap_d', 'f', ln=True),
                L(outline([(38, 18), (44, 18), (50, 30), (56, 18), (62, 18), (50, 40)]), 'logo', 'f', ln=True),
                L(outline([(22, 84), (34, 82), (35, 89), (23, 91)]), 'patch', 'f', False), L(outline([(78, 84), (66, 82), (65, 89), (77, 91)]), 'patch', 'f', False)]
             + white_eyes(75, 15, 5.4, 4.8, 1.6, 1.4) + [L(quad((40, 94), (50, 99), (60, 94)), (130, 70, 50, 255), 'f', False, False, 1.6)],
    'side': crop('side', top=10, nape=84)
            + [L(outline([(14, 50), (6, 30), (20, 10), (50, 0), (76, 8), (86, 26), (84, 46), (50, 46)]), 'cap', 'f', ln=True),
               L(outline([(80, 44), (100, 46), (102, 52), (82, 52)]), 'cap_d', 'f', ln=True),
               L(outline([(74, 14), (80, 18), (78, 30), (72, 30)]), 'logo', 'f', False)] + side_eye(75, 1.4),
    'back': crop('back', top=10, nape=84)
            + [L(outline([(12, 56), (10, 30), (22, 10), (50, 2), (78, 10), (90, 30), (88, 56), (50, 58)]), 'cap', 'f', ln=True),
               L(outline([(40, 52), (60, 52), (60, 58), (40, 58)]), 'cap_d', 'f', ln=True)],
})

# Garland Gathers: pelo azul pizarra en pinchos largos echados hacia un lado (a su izquierda), con patillas en punta;
# ojos de sueño de suficiencia y media sonrisa
C('garland-gathers', {
    'body': 'normal', 'pal': pal('#4a6688', SKIN, shade='#3a5270', deep='#283a52', light='#7a94b0'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 94,
             'hairline': [(16, 72), (18, 52), (24, 60), (30, 46), (50, 44), (70, 46), (76, 60), (82, 52), (84, 72)]},
    'front': [L(outline([(17, 76), (12, 50), (2, 40, 1), (12, 30), (8, 12, 1), (26, 12), (30, -6, 1), (44, 4), (56, -14, 1), (62, 4), (84, -6, 1), (80, 10), (104, 10, 1),
                         (90, 24), (102, 38, 1), (88, 40), (88, 56), (83, 76), (78, 52), (22, 52)])),
              L(outline([(60, 2), (82, -2), (80, 12), (98, 14), (88, 28), (90, 52), (84, 66), (76, 36)]), 'shade', 'b', False),
              strand([(40, 10), (50, 32)], 'deep', 'b', 1.0), strand([(62, 8), (66, 32)], 'deep', 'b', 1.0)]
             + white_eyes(76, 15, 5.6, 4.6, 1.6, 1.2) + [L([(28, 65), (42, 68)], OUTC, 'f', False, False, 1.8), L([(72, 65), (58, 68)], OUTC, 'f', False, False, 1.8)],
    'side': [L(outline([(72, 50), (84, 44), (98, 36, 1), (88, 26), (100, 12, 1), (82, 10), (80, -8, 1), (62, 2), (46, -14, 1), (40, 4), (18, 4, 1), (16, 18), (2, 30, 1),
                        (6, 44), (4, 64), (12, 80), (28, 84), (38, 66), (46, 56), (60, 54)])),
             L(outline([(5, 46), (30, 48), (40, 62), (32, 82), (14, 80), (6, 64)]), 'shade', 'b', False)] + side_eye(76, 1.2),
    'back': [L(outline([(17, 78), (12, 50), (0, 42, 1), (12, 30), (8, 12, 1), (26, 12), (30, -6, 1), (44, 4), (56, -14, 1), (62, 4), (84, -6, 1), (80, 10), (102, 12, 1),
                        (90, 24), (100, 40, 1), (88, 44), (83, 78), (66, 86), (50, 88), (34, 86)])),
             L(outline([(56, 2), (82, -2), (80, 12), (98, 14), (88, 30), (88, 50), (83, 78), (62, 86)]), 'shade', 'b', False)],
})

# Gary Osoto: grandullón de cara ancha y cuello grueso; pelo verde oliva oscuro con la raya en medio, peinado hacia los
# lados y con las puntas que se abren hacia fuera a la altura de la mandíbula; ojitos grises y sonrisa
C('gary-osoto', {
    'body': 'corpulento', 'pal': pal('#4e4a28', SKIN, iris='#7a8a9a', shade='#3c381e', deep='#2a2814', light='#6e6a42'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'face_front': WIDE_FACE, 'hairline': False, 'ears': False},
    'front': [L(outline([(6, 88, 1), (-6, 92, 1), (4, 80), (6, 44), (16, 14), (50, 2), (84, 14), (94, 44), (96, 80), (106, 92, 1), (94, 88, 1), (88, 62), (12, 62)])),
              L(outline([(60, 4), (84, 16), (94, 46), (96, 80), (90, 80), (86, 44)]), 'shade', 'b', False),
              fr([(10, 72), (12, 44), (26, 22), (48, 12), (50, 22), (40, 28), (24, 46), (18, 72)]),
              fr([(90, 72), (88, 44), (74, 22), (52, 12), (50, 22), (60, 28), (76, 46), (82, 72)]),
              strand([(50, 4), (50, 22)], 'deep', 'f', 1.2)],
    'side': [L(outline([(72, 50), (86, 44), (92, 26), (80, 6), (56, -2), (30, 2), (10, 18), (2, 46), (4, 76), (-6, 90, 1), (14, 86), (32, 84), (44, 74), (50, 58),
                        (62, 54)])),
             L(outline([(4, 46), (30, 48), (44, 70), (32, 84), (12, 86), (4, 76)]), 'shade', 'b', False),
             fr([(68, 8), (88, 22), (92, 44), (86, 54, 1), (80, 36)])],
    'back': [L(outline([(6, 90, 1), (-6, 92, 1), (4, 80), (6, 44), (16, 14), (50, 2), (84, 14), (94, 44), (96, 80), (106, 92, 1), (94, 90, 1), (70, 92), (50, 94), (30, 92)])),
             L(outline([(58, 4), (84, 16), (94, 46), (96, 86), (64, 92)]), 'shade', 'b', False), strand([(50, 4), (50, 60)], 'deep', 'b', 1.0)],
})

# Gary Salmon (portero): mofletudo, con la cabeza rapada salvo una cresta corta verde agua de punta, y el pelo muy corto
# del mismo color pegado a los lados; nariz naranja gorda, ojos redondos de enfado y sonrisa
C('gary-salmon', {
    'body': 'corpulento', 'pal': pal('#6ab0a2', SKIN, shade='#4e8e82', deep='#356a60', nose='#e0782e'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 97, 'nose': (50, 87, 6), 'face_front': WIDE_FACE,
             'hairline': [(14, 60), (20, 40), (34, 30), (50, 28), (66, 30), (80, 40), (86, 60)]},
    'front': crop('front', top=12, side=60, w=1)
             + [L(outline([(44, 16), (46, -16), (50, -26, 1), (54, -16), (56, 16)])), strand([(50, -20), (50, 12)], 'shade', 'b', 1.2)],
    'side': crop('side', top=12, nape=80) + [L(outline([(36, 14), (50, -14), (62, -24, 1), (60, -10), (60, 14)]))],
    'back': crop('back', top=12, nape=80) + [L(outline([(44, 18), (46, -14), (50, -24, 1), (54, -14), (56, 18)]))],
})

# Gaston Berry: melena ondulada verde oliva hasta el cuello, ahuecada y con mechones de punta; ojos ovalados negros sin
# blanco, una boquita redonda de sorpresa
C('gaston-berry', {
    'body': 'normal', 'pal': pal('#5c5a26', SKIN, shade='#46441a', deep='#302e10', light='#7e7c46'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'none', 'hairline': False, 'ears': False},
    'front': [L(outline([(6, 96, 1), (2, 76), (8, 60), (2, 40), (12, 14), (36, 0), (64, 0), (88, 14), (98, 40), (92, 60), (98, 76), (94, 96, 1), (84, 86), (82, 60), (18, 60),
                         (16, 86)])),
              L(outline([(62, 2), (88, 16), (98, 42), (92, 62), (96, 90), (84, 82), (82, 44)]), 'shade', 'b', False),
              fr([(14, 70), (14, 42), (26, 22), (50, 14), (74, 22), (86, 42), (86, 70), (80, 52), (72, 60), (66, 46), (58, 58), (50, 44), (42, 58), (36, 46), (26, 62),
                  (20, 52)])]
             + [L(ell(36, 76, 2.8, 4.6), OUTC, 'f', False), L(ell(64, 76, 2.8, 4.6), OUTC, 'f', False), L(ell(46, 86, 0.8, 0.8), OUTC, 'f', False),
                L(ell(54, 86, 0.8, 0.8), OUTC, 'f', False)]
             + o_mouth(95),
    'side': [L(outline([(70, 46), (84, 44), (90, 28), (80, 8), (56, -2), (30, 2), (10, 18), (2, 44), (6, 64), (0, 86), (4, 98, 1), (18, 90), (28, 100, 1), (36, 88),
                        (46, 94, 1), (50, 78), (54, 60), (62, 52)])),
             L(outline([(4, 44), (30, 46), (46, 70), (44, 92), (24, 96), (4, 86)]), 'shade', 'b', False),
             fr([(68, 8), (88, 22), (92, 46), (86, 56, 1), (80, 40), (70, 30)]),
             L(ell(83, 76, 1.8, 4.2), OUTC, 'f', False), L(ell(86, 95, 1.6, 2.4), (150, 70, 60, 255), 'f', ln=True)],
    'back': [L(outline([(6, 96, 1), (2, 76), (8, 60), (2, 40), (12, 14), (50, 0), (88, 14), (98, 40), (92, 60), (98, 76), (94, 96, 1), (82, 90), (72, 100, 1), (62, 90),
                        (50, 100, 1), (38, 90), (28, 100, 1), (18, 90)])),
             L(outline([(58, 2), (88, 16), (98, 42), (92, 62), (96, 92), (64, 92)]), 'shade', 'b', False)],
})

# Gauge Diven: piel morena; pelo rosa corto y a trasquilones, de puntas que se abren por los lados, con un mechón largo
# tieso que sale de la coronilla y se curva; ojos grandes y sonrisa
C('gauge-diven', {
    'body': 'normal', 'pal': pal('#f0a2a0', '#c48a5a', shade='#d28684', deep='#ae6664', light='#f8c8c4'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94,
             'hairline': [(16, 70), (18, 52), (28, 56), (34, 48), (46, 54), (52, 46), (62, 54), (70, 48), (78, 56), (84, 70)]},
    'front': [L(outline([(16, 72), (10, 56), (-4, 60, 1), (6, 46), (8, 28), (24, 10), (50, 2), (76, 10), (92, 28), (94, 46), (104, 60, 1), (90, 56), (84, 72), (80, 54),
                         (20, 54)])),
              L(outline([(60, 4), (80, 14), (92, 32), (100, 58), (88, 52), (78, 32)]), 'shade', 'b', False),
              L(quad((50, 4), (40, -24), (60, -26)) + quad((60, -26), (66, -20), (58, -12)), 'mid', 'b', False, False, 2.8)],
    'side': [L(outline([(72, 54), (82, 46), (90, 50, 1), (88, 36), (84, 18), (68, 4), (44, 2), (22, 8), (6, 26), (2, 50), (-6, 62, 1), (8, 66), (14, 80), (30, 84), (38, 66),
                        (46, 58), (60, 56)])),
             L(outline([(4, 46), (30, 48), (40, 62), (30, 84), (14, 80), (6, 64)]), 'shade', 'b', False),
             L(quad((50, 4), (44, -24), (64, -24)) + quad((64, -24), (70, -18), (62, -10)), 'mid', 'b', False, False, 2.8)],
    'back': [L(outline([(16, 76), (10, 56), (-4, 62, 1), (6, 46), (8, 28), (24, 10), (50, 2), (76, 10), (92, 28), (94, 46), (104, 62, 1), (90, 58), (84, 76), (70, 84, 1),
                        (62, 80), (50, 88, 1), (38, 80), (30, 84, 1)])),
             L(outline([(58, 4), (80, 14), (92, 32), (100, 60), (86, 76), (64, 82)]), 'shade', 'b', False),
             L(quad((50, 4), (60, -24), (40, -26)) + quad((40, -26), (34, -20), (42, -12)), 'mid', 'b', False, False, 2.8)],
})

# Gene Bates: pelo verde oscuro en pinchos largos peinados hacia atrás y hacia los lados; ojos blancos afilados de pupila
# pequeña, ceño de enfado y sonrisa de lado
C('gene-bates', {
    'body': 'normal', 'pal': pal('#2c6a4a', SKIN, shade='#205238', deep='#143a26', light='#4e9a72'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94,
             'hairline': [(16, 68), (18, 52), (24, 46), (36, 44), (50, 40), (64, 44), (76, 46), (82, 52), (84, 68)]},
    'front': [L(outline([(16, 70), (8, 54), (-8, 52, 1), (6, 40), (-4, 22, 1), (14, 18), (14, -2, 1), (32, 6), (42, -12, 1), (54, 2), (72, -10, 1), (74, 8), (98, 6, 1),
                         (88, 22), (106, 30, 1), (94, 40), (108, 56, 1), (90, 56), (84, 70), (80, 52), (20, 52)])),
              L(outline([(58, 0), (72, -6), (74, 10), (94, 10), (88, 24), (100, 34), (92, 42), (100, 54), (86, 52), (78, 30)]), 'shade', 'b', False),
              strand([(34, 10), (42, 30)], 'deep', 'b', 1.0), strand([(60, 8), (60, 30)], 'deep', 'b', 1.0)]
             + [L(outline([(26, 72), (44, 76), (42, 80), (28, 78)]), WHITE, 'f', ln=True), L(outline([(74, 72), (56, 76), (58, 80), (72, 78)]), WHITE, 'f', ln=True),
                L(ell(37, 77, 1.6, 1.8), OUTC, 'f', False), L(ell(63, 77, 1.6, 1.8), OUTC, 'f', False)],
    'side': [L(outline([(72, 50), (84, 44), (92, 32), (86, 18), (94, 4, 1), (74, 6), (70, -10, 1), (54, 0), (36, -14, 1), (32, 4), (10, -2, 1), (14, 14), (-6, 20, 1),
                        (6, 32), (-10, 44, 1), (6, 50), (-2, 66, 1), (10, 70), (16, 84), (30, 86), (38, 66), (46, 56), (60, 54)])),
             L(outline([(5, 46), (30, 48), (40, 62), (30, 86), (16, 84), (8, 68)]), 'shade', 'b', False),
             L(outline([(76, 72), (88, 74), (87, 79), (78, 78)]), WHITE, 'f', ln=True), L(ell(85, 76, 1.2, 1.6), OUTC, 'f', False)],
    'back': [L(outline([(16, 76), (8, 56), (-8, 54, 1), (6, 40), (-4, 22, 1), (14, 18), (14, -2, 1), (32, 6), (42, -12, 1), (54, 2), (72, -10, 1), (74, 8), (98, 6, 1),
                        (88, 22), (106, 30, 1), (94, 40), (108, 58, 1), (90, 58), (84, 76), (66, 86), (50, 88), (34, 86)])),
             L(outline([(58, 0), (72, -6), (74, 10), (94, 10), (88, 24), (100, 34), (92, 42), (100, 56), (86, 60), (84, 76), (62, 86)]), 'shade', 'b', False)],
})

# Gene Bottle: pelo gris violáceo recogido en dos lóbulos enormes como alas de mariposa a los lados de la cabeza, con una
# mecha verde menta en cada uno y rizos menta en la nuca; dos lunares violetas en la frente, ojazos negros con pestañas
C('gene-bottle', {
    'body': 'chica', 'pal': pal('#6e6478', SKIN, iris='#1e1a1e', shade='#564e60', deep='#3e3846', light='#cce2d4', dot='#8a7a9a'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 93,
             'hairline': [(16, 64), (20, 50), (34, 44), (50, 44), (66, 44), (80, 50), (84, 64)]},
    'front': [L(outline([(10, 92), (2, 80), (10, 66), (18, 48), (10, 30), (0, 6), (4, -14, 1), (24, -8), (40, 10), (50, 6), (60, 10), (76, -8), (96, -14, 1),
                         (100, 6), (90, 30), (82, 48), (90, 66), (98, 80), (90, 92), (82, 66), (18, 66)])),
              L(outline([(10, 92), (2, 80), (10, 70), (18, 66), (16, 80)]), 'light', 'b', False), L(outline([(90, 92), (98, 80), (90, 70), (82, 66), (84, 80)]), 'light', 'b', False),
              L(outline([(64, 8), (78, -6), (96, -12), (98, 8), (88, 32), (80, 46), (74, 28)]), 'shade', 'b', False),
              L(quad((24, 40), (14, 10), (16, -8)), 'light', 'b', False, False, 2.6), L(quad((76, 40), (86, 10), (84, -8)), 'light', 'b', False, False, 2.6),
              strand([(30, 30), (20, 2)], 'deep', 'b', 1.0), strand([(70, 30), (80, 2)], 'deep', 'b', 1.0),
              L(ell(42, 60, 2.6, 2.2), 'dot', 'f', ln=True), L(ell(58, 60, 2.6, 2.2), 'dot', 'f', ln=True),
              L([(26, 72), (22, 70)], OUTC, 'f', False, False, 1.6), L([(74, 72), (78, 70)], OUTC, 'f', False, False, 1.6)],
    'side': [L(outline([(72, 50), (82, 44), (86, 26), (74, 12), (60, 10), (50, -10), (34, -16, 1), (30, 4), (14, 14), (4, 36), (6, 64), (0, 80), (10, 94), (24, 90),
                        (34, 80), (38, 64), (46, 56), (60, 54)])),
             L(outline([(4, 70), (16, 66), (30, 76), (22, 90), (10, 94), (0, 82)]), 'light', 'b', False),
             L(quad((40, 30), (36, 4), (36, -12)), 'light', 'b', False, False, 2.6),
             L(outline([(5, 40), (30, 44), (38, 62), (20, 66), (6, 60)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 78), (10, 64), (18, 48), (10, 30), (0, 6), (4, -14, 1), (24, -8), (40, 10), (50, 6), (60, 10), (76, -8), (96, -14, 1), (100, 6), (90, 30),
                        (82, 48), (90, 64), (84, 78), (66, 86), (50, 88), (34, 86)])),
             L(outline([(14, 70), (34, 80), (50, 96), (66, 80), (86, 70), (92, 86), (70, 100), (50, 104), (30, 100), (8, 86)]), 'light', 'b', False),
             L(outline([(62, 10), (78, -6), (96, -12), (98, 8), (88, 32), (82, 50), (84, 74), (66, 84)]), 'shade', 'b', False),
             L(quad((24, 40), (14, 10), (16, -8)), 'light', 'b', False, False, 2.6), L(quad((76, 40), (86, 10), (84, -8)), 'light', 'b', False, False, 2.6)],
})

# Gerry Attrick: melena ondulada verde oliva oscuro hasta el cuello, con una cinta ancha azul verdosa en la frente; cejas
# gruesas, un esparadrapo sobre la nariz y labios gruesos naranjas
C('gerry-attrick', {
    'body': 'normal', 'pal': pal('#4c4c26', SKIN, shade='#3a3a1a', deep='#26260e', band='#5a9ab0', band_d='#447a8e', tape='#f2e8c4'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'lips', 'mouth_y': 95, 'mouth_w': 7, 'hairline': False, 'ears': False},
    'front': [L(outline([(8, 94, 1), (4, 74), (8, 50), (4, 30), (16, 10), (40, -2), (62, -2), (86, 10), (96, 30), (92, 50), (96, 74), (92, 94, 1), (84, 82), (84, 58),
                         (16, 58), (16, 82)])),
              L(outline([(62, 0), (86, 12), (96, 32), (92, 52), (94, 88), (84, 78), (82, 44)]), 'shade', 'b', False),
              L(outline([(12, 56), (12, 38), (30, 28), (50, 26), (70, 28), (88, 38), (88, 56), (70, 48), (50, 46), (30, 48)]), 'band', 'f', ln=True),
              L(outline([(56, 27), (70, 29), (86, 38), (86, 54), (70, 47), (56, 46)]), 'band_d', 'f', False),
              L(outline([(26, 84), (74, 84), (72, 89), (28, 89)]), 'tape', 'f', ln=True)]
             + brows(64, 'deep', 4.0, 15, 0.6, 13),
    'side': [L(outline([(70, 46), (84, 44), (90, 28), (80, 8), (56, -2), (30, 2), (10, 18), (2, 44), (4, 70), (0, 92, 1), (16, 86), (26, 96, 1), (36, 86), (44, 94, 1),
                        (48, 76), (54, 58), (62, 52)])),
             L(outline([(4, 44), (30, 46), (44, 70), (42, 90), (20, 92), (4, 80)]), 'shade', 'b', False),
             L(outline([(48, 36), (62, 28), (88, 30), (92, 44), (64, 46), (50, 50)]), 'band', 'f', ln=True),
             L(outline([(70, 82), (90, 82), (90, 88), (70, 88)]), 'tape', 'f', ln=True)] + brow_side(64, 'deep', 4.0, 0.6),
    'back': [L(outline([(8, 94, 1), (4, 74), (8, 50), (4, 30), (16, 10), (50, -2), (84, 10), (96, 30), (92, 50), (96, 74), (92, 94, 1), (80, 88), (70, 98, 1), (60, 88),
                        (50, 98, 1), (40, 88), (30, 98, 1), (20, 88)])),
             L(outline([(58, 0), (86, 12), (96, 32), (92, 52), (94, 90), (64, 90)]), 'shade', 'b', False),
             L(outline([(6, 44), (30, 36), (50, 34), (70, 36), (94, 44), (94, 54), (50, 46), (6, 54)]), 'band', 'f', ln=True)],
})

# Gil Rivers: un adulto de cara larga y alargada; pelo azul verdoso revuelto en pinchos por todos lados, con un rizo que
# le cae en gancho sobre la frente; ojos de sueño caídos y labios gruesos naranjas
C('gil-rivers', {
    'body': 'delgado', 'pal': pal('#5a98ac', SKIN, shade='#447c8e', deep='#2e5a6a', light='#8cbccc'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'lips', 'mouth_y': 99, 'mouth_w': 7, 'face_front': LONG_FACE, 'eye_y': 78,
             'hairline': [(16, 60), (20, 44), (34, 38), (50, 40), (66, 38), (80, 44), (84, 60)]},
    'front': messy('front', amp=13, n=13, seed=21, rx=46, ry=40, cy=40, lo=60)
             + [L(quad((58, 24), (70, 34), (62, 58)), 'mid', 'f', False, False, 4.0), L(quad((58, 24), (70, 34), (62, 58)), 'deep', 'f', False, False, 0.8)]
             + white_eyes(78, 15, 6, 4.6, 1.8, 1.4) + [L(quad((28, 70), (36, 66), (44, 70)), OUTC, 'f', False, False, 1.4), L(quad((72, 70), (64, 66), (56, 70)), OUTC, 'f', False, False, 1.4)],
    'side': messy('side', amp=13, n=12, seed=21, nape=84) + side_eye(78, 1.4),
    'back': messy('back', amp=13, n=13, seed=21, nape=84),
})

# Gill Able (portero): piel tostada y mandíbula grande; pelo malva rosado ondulado hasta el cuello; cejas gruesas rosas,
# ojos blancos redondos de pupila pequeña y una boca ancha de labios gruesos
C('gill-able', {
    'body': 'corpulento', 'pal': pal('#c08a8c', '#c8925a', shade='#a06e72', deep='#7e5054', light='#dcb0b0', brow='#d08a90'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'lips', 'mouth_y': 97, 'mouth_w': 11, 'face_front': WIDE_FACE, 'hairline': False, 'ears': False},
    'front': [L(outline([(4, 90, 1), (0, 70), (6, 44), (12, 16), (40, 2), (64, 2), (88, 16), (96, 44), (100, 70), (96, 90, 1), (86, 76), (86, 58), (14, 58), (14, 76)])),
              L(outline([(62, 4), (88, 18), (96, 46), (98, 84), (86, 72), (84, 42)]), 'shade', 'b', False),
              fr([(12, 66), (12, 42), (24, 22), (46, 12), (70, 16), (86, 32), (88, 60), (80, 46), (66, 50), (60, 38), (46, 46), (36, 36), (26, 50), (18, 52)])]
             + brows(64, 'brow', 4.2, 15, 0.6, 13) + white_eyes(77, 15, 6.4, 5.6, 1.8),
    'side': [L(outline([(70, 46), (84, 44), (90, 28), (80, 8), (56, -2), (30, 2), (10, 18), (2, 44), (2, 70), (-2, 88, 1), (14, 82), (24, 92, 1), (34, 82), (42, 88, 1),
                        (48, 70), (54, 58), (62, 52)])),
             L(outline([(4, 44), (30, 46), (44, 70), (40, 86), (20, 88), (4, 78)]), 'shade', 'b', False)]
            + brow_side(64, 'brow', 4.2, 0.6) + side_eye(77),
    'back': [L(outline([(4, 90, 1), (0, 70), (6, 44), (12, 16), (50, 2), (88, 16), (96, 44), (100, 70), (96, 90, 1), (80, 86), (70, 96, 1), (60, 86), (50, 96, 1), (40, 86),
                        (30, 96, 1), (20, 86)])),
             L(outline([(58, 4), (88, 18), (96, 46), (98, 88), (64, 88)]), 'shade', 'b', False)],
})

# Gill O'Mend: pelo violeta oscuro liso y largo hasta la barbilla, con un flequillo largo que le tapa un ojo; ojos afilados
# de enfado y boca torcida
C('gill-o-mend', {
    'body': 'normal', 'pal': pal('#4a4270', SKIN, iris='#2a2020', shade='#38325a', deep='#262240', light='#6e66a0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'hairline': False, 'ears': False},
    'front': [L(outline([(6, 100, 1), (8, 76), (4, 44), (16, 14), (40, 0), (64, 0), (86, 12), (96, 40), (94, 76), (96, 98, 1), (84, 88), (84, 60), (16, 60), (18, 88)])),
              L(outline([(62, 2), (86, 14), (96, 42), (94, 92), (84, 84), (82, 44)]), 'shade', 'b', False),
              fr([(10, 92, 1), (12, 60), (16, 34), (34, 16), (60, 12), (80, 20), (88, 40), (88, 66), (80, 50), (66, 52), (54, 60), (46, 76), (40, 90, 1), (36, 70),
                  (24, 74), (18, 92)]),
              strand([(40, 20), (30, 60)], 'deep', 'f', 1.0), strand([(56, 18), (44, 62)], 'deep', 'f', 1.0)],
    'side': [L(outline([(70, 46), (84, 44), (90, 28), (80, 8), (56, -2), (30, 2), (10, 18), (2, 46), (4, 76), (0, 100, 1), (18, 92), (30, 100, 1), (40, 90), (48, 98, 1),
                        (52, 78), (56, 60), (62, 52)])),
             L(outline([(4, 46), (30, 48), (48, 72), (44, 94), (20, 96), (4, 84)]), 'shade', 'b', False),
             fr([(66, 6), (88, 22), (92, 50), (88, 66, 1), (80, 46), (70, 32)])],
    'back': [L(outline([(6, 100, 1), (8, 76), (4, 44), (16, 14), (50, 0), (84, 12), (96, 40), (94, 76), (96, 100, 1), (82, 92), (72, 102, 1), (62, 92), (50, 102, 1), (38, 92),
                        (28, 102, 1), (18, 92)])),
             L(outline([(58, 2), (86, 14), (96, 42), (94, 94), (64, 94)]), 'shade', 'b', False)],
})

# Glen Adeer: cara larga; pelo naranja en pinchos altos de punta que salen hacia arriba y a los lados, con un mechón que
# le cae en medio de la frente; cejas gruesas naranjas, ojos de sueño y media sonrisa
C('glen-adeer', {
    'body': 'delgado', 'pal': pal('#d27c30', SKIN, shade='#b06020', deep='#884614', light='#eca868'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 97, 'face_front': LONG_FACE,
             'hairline': [(16, 64), (20, 48), (34, 42), (50, 44), (66, 42), (80, 48), (84, 64)]},
    'front': [L(outline([(17, 66), (12, 46), (-6, 30, 1), (12, 24), (4, 2, 1), (24, 8), (24, -20, 1), (38, -2), (44, -34, 1), (54, -6), (64, -30, 1), (66, -2), (84, -18, 1),
                         (80, 8), (104, 4, 1), (88, 24), (106, 34, 1), (88, 44), (83, 66), (78, 50), (22, 50)])),
              L(outline([(56, -4), (64, -26), (68, 0), (82, -14), (80, 10), (98, 8), (88, 26), (98, 36), (86, 44), (80, 30)]), 'shade', 'b', False),
              strand([(30, 10), (34, 34)], 'deep', 'b', 1.0), strand([(50, 0), (48, 30)], 'deep', 'b', 1.0), strand([(66, 6), (64, 32)], 'deep', 'b', 1.0),
              fr([(46, 40), (54, 40), (58, 56), (54, 74, 1), (52, 58), (48, 50)])]
             + brows(64, 'mid', 4.0, 15, 0.4, 13) + white_eyes(77, 15, 6, 4.8, 1.8, 1.2),
    'side': [L(outline([(72, 50), (84, 44), (100, 36, 1), (88, 26), (104, 10, 1), (84, 8), (90, -14, 1), (70, 0), (64, -32, 1), (52, -4), (36, -24, 1), (32, 4), (10, -4, 1),
                        (14, 16), (-6, 24, 1), (8, 34), (4, 54), (10, 72), (22, 84), (34, 82), (38, 66), (46, 56), (60, 54)])),
             L(outline([(5, 46), (30, 48), (40, 62), (34, 82), (22, 84), (10, 70)]), 'shade', 'b', False)]
            + brow_side(64, 'mid', 4.0, 0.4) + side_eye(77, 1.2),
    'back': [L(outline([(17, 76), (12, 46), (-6, 32, 1), (12, 24), (4, 2, 1), (24, 8), (24, -20, 1), (38, -2), (44, -32, 1), (54, -6), (64, -28, 1), (66, -2), (84, -16, 1),
                        (80, 8), (104, 6, 1), (88, 24), (106, 36, 1), (88, 46), (83, 76), (66, 84), (50, 86), (34, 84)])),
             L(outline([(56, -4), (64, -26), (68, 0), (82, -14), (80, 10), (98, 8), (88, 26), (98, 38), (86, 48), (83, 76), (62, 84)]), 'shade', 'b', False)],
})

# Glen Garry: gorro de lana amarillo con la vuelta naranja, orejeras naranjas y una borla; asoman mechones verde oliva
# por la frente; cejas de enfado, nariz naranja redonda y boca seria
C('glen-garry', {
    'body': 'bajito', 'pal': pal('#7a8a3a', SKIN, shade='#5e6c28', deep='#42501a', hat='#e2c874', hat_d='#c8aa52', rim='#e07a24', rim_d='#b85e14', nose='#e07a34'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'nose': (50, 86, 4.4), 'hairline': False, 'ears': False},
    'front': [L(outline([(10, 92), (6, 70), (14, 56), (86, 56), (94, 70), (90, 92), (82, 92), (80, 64), (20, 64), (18, 92)]), 'rim'),
              L(outline([(12, 50), (12, 26), (28, 4), (50, -4), (72, 4), (88, 26), (88, 50)]), 'hat', 'f', ln=True),
              L(outline([(60, 0), (76, 8), (88, 28), (88, 48), (76, 48)]), 'hat_d', 'f', False),
              L(ell(50, -12, 10, 9), 'hat', 'f', ln=True),
              L(outline([(8, 64), (8, 46), (50, 40), (92, 46), (92, 64), (50, 58)]), 'rim', 'f', ln=True),
              L(outline([(60, 44), (92, 48), (92, 62), (60, 58)]), 'rim_d', 'f', False),
              fr([(34, 60), (40, 56), (50, 58), (60, 56), (66, 60), (58, 64), (50, 70, 1), (42, 64)])],
    'side': [L(outline([(28, 92), (18, 70), (24, 56), (44, 56), (50, 70), (42, 92)]), 'rim'),
             L(outline([(12, 52), (6, 28), (22, 6), (50, -4), (76, 6), (88, 26), (90, 48), (50, 50)]), 'hat', 'f', ln=True),
             L(ell(48, -12, 10, 9), 'hat', 'f', ln=True),
             L(outline([(8, 64), (6, 48), (50, 42), (92, 46), (92, 60), (50, 58)]), 'rim', 'f', ln=True)],
    'back': [L(outline([(10, 92), (6, 70), (14, 56), (86, 56), (94, 70), (90, 92), (66, 96), (50, 98), (34, 96)]), 'rim'),
             L(outline([(12, 52), (12, 26), (28, 4), (50, -4), (72, 4), (88, 26), (88, 52)]), 'hat', 'f', ln=True),
             L(outline([(56, 0), (76, 8), (88, 28), (88, 50), (70, 50)]), 'hat_d', 'f', False),
             L(ell(50, -12, 10, 9), 'hat', 'f', ln=True),
             L(outline([(8, 66), (8, 48), (50, 42), (92, 48), (92, 66), (50, 60)]), 'rim', 'f', ln=True)],
})

# Gore Lyath: cara larga y huesuda, con arrugas marcadas; pelo rojo intenso peinado hacia atrás en llamas de punta; ojos
# blancos de pupila diminuta y media sonrisa torcida
C('gore-lyath', {
    'body': 'delgado', 'pal': pal('#c2321a', SKIN, shade='#9a2410', deep='#72180a', light='#e2664a'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 99, 'face_front': LONG_FACE, 'eye_y': 76,
             'hairline': [(16, 64), (20, 40), (36, 32), (50, 34), (64, 32), (80, 40), (84, 64)]},
    'front': [L(outline([(17, 66), (8, 48), (-6, 40, 1), (8, 30), (2, 12, 1), (18, 10), (18, -8, 1), (34, 0), (44, -16, 1), (54, -2), (66, -14, 1), (70, 2), (86, -4, 1),
                         (84, 12), (100, 14, 1), (90, 30), (106, 42, 1), (90, 48), (83, 66), (78, 44), (22, 44)])),
              L(outline([(58, 0), (68, -8), (70, 4), (84, 0), (84, 14), (96, 18), (88, 32), (98, 42), (88, 46), (80, 30)]), 'shade', 'b', False),
              strand([(30, 8), (36, 30)], 'deep', 'b', 1.0), strand([(52, 2), (52, 28)], 'deep', 'b', 1.0)]
             + white_eyes(76, 15, 6.4, 4.6, 1.4)
             + [L([(28, 70), (44, 74)], OUTC, 'f', False, False, 2.4), L([(72, 70), (56, 74)], OUTC, 'f', False, False, 2.4),
                L(quad((30, 84), (34, 92), (38, 100)), (150, 80, 60, 255), 'f', False, False, 1.0), L(quad((70, 84), (66, 92), (62, 100)), (150, 80, 60, 255), 'f', False, False, 1.0),
                L(quad((44, 64), (48, 76), (46, 88)), (150, 80, 60, 255), 'f', False, False, 1.0)],
    'side': [L(outline([(70, 40), (84, 30), (98, 22, 1), (84, 16), (90, 0, 1), (72, 4), (66, -14, 1), (52, -2), (34, -12, 1), (30, 4), (10, 2, 1), (14, 18), (-6, 26, 1),
                        (6, 36), (-6, 50, 1), (8, 54), (10, 72), (22, 84), (34, 82), (38, 66), (46, 52), (58, 44)])),
             L(outline([(5, 46), (30, 48), (40, 62), (34, 82), (22, 84), (10, 70)]), 'shade', 'b', False),
             L(ell(84, 76, 3.4, 4.6), WHITE, 'f', ln=True), L(ell(85, 76.5, 1.2, 1.4), OUTC, 'f', False)],
    'back': [L(outline([(17, 76), (8, 50), (-6, 42, 1), (8, 30), (2, 12, 1), (18, 10), (18, -8, 1), (34, 0), (44, -16, 1), (54, -2), (66, -14, 1), (70, 2), (86, -4, 1),
                        (84, 12), (100, 14, 1), (90, 30), (106, 44, 1), (90, 50), (83, 76), (66, 84), (50, 86), (34, 84)])),
             L(outline([(58, 0), (68, -8), (70, 4), (84, 0), (84, 14), (96, 18), (88, 32), (98, 44), (88, 50), (83, 76), (62, 84)]), 'shade', 'b', False)],
})


def beard(c='beard', top=72, chin=108):
    """Barba cerrada de oreja a oreja con bigote."""
    return [L(outline([(17, top), (20, 90), (34, 104), (50, chin), (66, 104), (80, 90), (83, top), (78, 82), (66, 90), (58, 88), (50, 90), (42, 88), (34, 90), (22, 82)]),
              c, 'f', ln=True),
            L(outline([(38, 92), (50, 88), (62, 92), (58, 95), (50, 93), (42, 95)]), c, 'f', ln=True)]


# Graham Hush: piel tostada y cara larga; pelo verde azulado peinado hacia atrás en ondas, con las puntas que se abren en
# la nuca; ojos verdes afilados de enfado y la boca abierta en un grito
C('graham-hush', {
    'body': 'delgado', 'pal': pal('#5a9a8c', '#c88e58', iris='#3a8a8a', shade='#447c70', deep='#2e5a50', light='#8cc0b2'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98, 'face_front': LONG_FACE, 'eye_y': 76,
             'hairline': [(16, 62), (20, 44), (34, 36), (50, 34), (66, 36), (80, 44), (84, 62)]},
    'front': [L(outline([(17, 66), (12, 44), (16, 20), (32, 4), (52, -4), (72, 0), (88, 14), (92, 34), (88, 50), (98, 62, 1), (84, 62), (78, 44), (22, 44)])),
              L(outline([(58, -2), (76, 4), (90, 20), (92, 40), (88, 54), (80, 34)]), 'shade', 'b', False),
              strand([(30, 30), (40, 10), (56, 2)], 'deep', 'b', 1.0), strand([(46, 32), (56, 12), (72, 6)], 'deep', 'b', 1.0), strand([(64, 30), (72, 16), (84, 14)], 'deep', 'b', 1.0)],
    'side': [L(outline([(72, 42), (84, 34), (86, 18), (72, 4), (48, -2), (24, 4), (8, 22), (2, 46), (6, 66), (-4, 78, 1), (14, 78), (16, 88, 1), (28, 82), (36, 66), (46, 52),
                        (60, 46)])),
             L(outline([(4, 44), (30, 48), (40, 62), (28, 82), (12, 80), (6, 64)]), 'shade', 'b', False),
             strand([(80, 24), (60, 10), (30, 12)], 'deep', 'b', 1.0), strand([(70, 36), (50, 22), (16, 30)], 'deep', 'b', 1.0)],
    'back': [L(outline([(17, 76), (12, 44), (18, 18), (50, 2), (82, 18), (88, 44), (84, 76), (96, 86, 1), (74, 86), (62, 92, 1), (50, 86), (38, 92, 1), (26, 86), (4, 86, 1)])),
             L(outline([(56, 4), (80, 18), (88, 46), (84, 76), (62, 86)]), 'shade', 'b', False),
             strand([(50, 4), (46, 40), (50, 80)], 'deep', 'b', 1.0), strand([(30, 12), (26, 50), (30, 80)], 'deep', 'b', 1.0), strand([(70, 12), (74, 50), (70, 80)], 'deep', 'b', 1.0)],
})

# Grant Mardy: cara larga; pelo gris pardo despeinado en mechones de punta con una cinta amarilla de triángulos verdes en
# la frente, y dos mechones largos que le caen junto a la cara con cuentas; ojos blancos redondos y sonrisa torcida
C('grant-mardy', {
    'body': 'delgado', 'pal': pal('#8c8a78', SKIN, shade='#6e6c5c', deep='#4e4c40', light='#b0ae9c', band='#e8c838', band2='#3a7a3a', bead='#6a4a2a'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'face_front': LONG_FACE, 'eye_y': 77, 'hairline': False},
    'front': [L(outline([(17, 62), (8, 46), (-4, 40, 1), (8, 32), (4, 14, 1), (20, 14), (26, -2, 1), (40, 8), (52, -12, 1), (60, 6), (76, -2, 1), (78, 14), (96, 14, 1),
                         (90, 30), (104, 40, 1), (90, 46), (83, 62), (78, 46), (22, 46)])),
              L(outline([(58, 4), (76, 2), (78, 16), (94, 18), (88, 32), (100, 40), (88, 44), (80, 30)]), 'shade', 'b', False),
              L(outline([(12, 56), (12, 40), (30, 34), (50, 32), (70, 34), (88, 40), (88, 56), (70, 50), (50, 48), (30, 50)]), 'band', 'f', ln=True)]
             + [L(outline([(x - 6, 50 - abs(x - 50) * 0.08), (x, 36 - abs(x - 50) * 0.08), (x + 6, 50 - abs(x - 50) * 0.08)]), 'band2', 'f', False) for x in (24, 38, 50, 62, 76)]
             + [fr([(14, 56), (20, 74), (20, 100, 1), (24, 76), (24, 56)]), fr([(86, 56), (80, 74), (80, 100, 1), (76, 76), (76, 56)]),
                L(ell(21, 92, 2.2, 2.6), 'bead', 'f', ln=True), L(ell(79, 92, 2.2, 2.6), 'bead', 'f', ln=True)]
             + white_eyes(77, 15, 6.4, 5.6, 1.6),
    'side': [L(outline([(72, 48), (84, 42), (98, 36, 1), (88, 26), (98, 12, 1), (80, 10), (82, -6, 1), (64, 2), (50, -12, 1), (42, 4), (20, 0, 1), (18, 16), (0, 24, 1),
                        (8, 36), (2, 58), (10, 74), (24, 84), (36, 80), (40, 64), (48, 54), (60, 52)])),
             L(outline([(4, 46), (30, 48), (40, 62), (34, 80), (22, 84), (10, 72)]), 'shade', 'b', False),
             L(outline([(36, 40), (56, 32), (90, 34), (92, 48), (58, 46), (38, 52)]), 'band', 'f', ln=True),
             L(outline([(62, 46), (68, 34), (74, 46)]), 'band2', 'f', False), L(outline([(76, 46), (82, 34), (88, 46)]), 'band2', 'f', False),
             fr([(74, 48), (78, 70), (76, 98, 1), (72, 72), (70, 50)]), L(ell(76, 90, 2.2, 2.6), 'bead', 'f', ln=True)] + side_eye(77),
    'back': [L(outline([(17, 76), (8, 48), (-4, 42, 1), (8, 32), (4, 14, 1), (20, 14), (26, -2, 1), (40, 8), (52, -12, 1), (60, 6), (76, -2, 1), (78, 14), (96, 14, 1),
                        (90, 30), (104, 42, 1), (90, 48), (83, 76), (66, 84), (50, 86), (34, 84)])),
             L(outline([(56, 4), (76, 2), (78, 16), (94, 18), (88, 32), (100, 42), (88, 50), (83, 76), (62, 84)]), 'shade', 'b', False),
             L(outline([(10, 50), (30, 44), (50, 42), (70, 44), (90, 50), (90, 60), (50, 54), (10, 60)]), 'band', 'f', ln=True)],
})

# Grant Slammer: piel tostada; pelo malva rosado en pinchos que asoman por encima de un pañuelo naranja atado a la
# frente, con la cola del nudo colgando a un lado; ojos grandes ámbar, cejas de enfado y boca seria
C('grant-slammer', {
    'body': 'normal', 'pal': pal('#c08aa8', '#c08a58', iris='#c89a1e', shade='#a06e8c', deep='#7e506c', light='#dcb0c8', band='#d8641e', band_d='#b04a12'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(16, 70), (12, 50), (-2, 38, 1), (12, 30), (6, 10, 1), (24, 12), (30, -8, 1), (44, 4), (54, -12, 1), (62, 4), (80, -4, 1), (78, 14), (100, 18, 1),
                         (88, 30), (100, 40, 1), (88, 50), (84, 70), (80, 56), (20, 56)])),
              L(outline([(58, 2), (78, 0), (78, 16), (94, 20), (86, 32), (94, 40), (84, 46), (78, 30)]), 'shade', 'b', False),
              L(outline([(10, 62), (10, 42), (30, 34), (50, 32), (70, 34), (90, 42), (90, 62), (70, 54), (50, 52), (30, 54)]), 'band', 'f', ln=True),
              L(outline([(56, 33), (70, 35), (88, 42), (88, 60), (70, 53), (56, 52)]), 'band_d', 'f', False),
              L(rope((88, 58), (96, 72), (90, 90), 6), 'band', 'f')],
    'side': [L(outline([(72, 50), (84, 44), (98, 36, 1), (88, 26), (98, 10, 1), (80, 10), (80, -6, 1), (62, 2), (48, -12, 1), (42, 4), (20, 0, 1), (20, 14), (2, 22, 1),
                        (8, 36), (4, 58), (10, 74), (22, 84), (34, 82), (38, 66), (46, 56), (60, 54)])),
             L(outline([(5, 46), (30, 48), (40, 62), (34, 82), (22, 84), (10, 72)]), 'shade', 'b', False),
             L(outline([(4, 46), (30, 36), (60, 32), (90, 36), (92, 50), (60, 48), (30, 52), (6, 60)]), 'band', 'f', ln=True),
             L(rope((10, 54), (-6, 62), (0, 80), 6), 'band', 'f')],
    'back': [L(outline([(16, 76), (12, 50), (-2, 40, 1), (12, 30), (6, 10, 1), (24, 12), (30, -8, 1), (44, 4), (54, -12, 1), (62, 4), (80, -4, 1), (78, 14), (100, 18, 1),
                        (88, 30), (100, 42, 1), (88, 50), (84, 76), (66, 84), (50, 86), (34, 84)])),
             L(outline([(56, 2), (78, 0), (78, 16), (94, 20), (86, 32), (94, 42), (86, 52), (84, 76), (62, 84)]), 'shade', 'b', False),
             L(outline([(8, 46), (30, 40), (50, 38), (70, 40), (92, 46), (92, 58), (50, 52), (8, 58)]), 'band', 'f', ln=True),
             L(rope((50, 52), (60, 64), (66, 80), 6), 'band', 'f'), L(rope((50, 52), (40, 64), (36, 78), 6), 'band', 'f')],
})

# Gregory Bones: piel tostada; pelo azul marino oscuro en pinchos revueltos con un mechón blanco verdoso que le cruza la
# frente en diagonal; ojazos redondos y sonrisa
C('gregory-bones', {
    'body': 'normal', 'pal': pal('#2c3c5a', '#c8925a', shade='#202e46', deep='#141e30', light='#cce8e0', light_d='#9cc4bc'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 93, 'hairline': False},
    'front': messy('front', amp=13, n=11, seed=33, rx=46, ry=40, cy=40, lo=62)
             + [fr([(80, 22), (64, 30), (48, 40), (34, 56), (26, 66, 1), (36, 52), (48, 36), (60, 24)], 'light'),
                strand([(72, 26), (46, 42), (32, 58)], 'light_d', 'f', 1.0)],
    'side': messy('side', amp=13, n=10, seed=33, nape=84) + [fr([(56, 18), (76, 26), (88, 40), (90, 52, 1), (80, 38), (66, 30)], 'light')],
    'back': messy('back', amp=13, n=11, seed=33, nape=84),
})

# Gregory Smith (portero, con modelo 3D): un adulto de pelo castaño oscuro muy corto con entradas y la coronilla en
# pinchos cortos, orejas grandes y una barba cerrada gris azulada; ceño fruncido y ojos blancos de mirada dura
C('gregory-smith', {
    'body': 'normal', 'pal': pal('#4a3624', '#c08a5a', shade='#36261a', deep='#24180e', beard='#5c6a84', nose='#a87048'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'big_ears': 2, 'ear_out': 2, 'nose': (50, 86, 3.6),
             'hairline': [(16, 60), (20, 42), (30, 38), (40, 30), (50, 34), (60, 30), (70, 38), (80, 42), (84, 60)]},
    'front': crop('front', top=4, side=60)
             + [L(outline([(38, 8), (44, -6, 1), (50, 6), (56, -4, 1), (62, 8)])),
                L([(30, 70), (44, 74)], OUTC, 'f', False, False, 3.0), L([(70, 70), (56, 74)], OUTC, 'f', False, False, 3.0),
                L(outline([(30, 76), (43, 77), (42, 80), (31, 80)]), WHITE, 'f', ln=True), L(outline([(70, 76), (57, 77), (58, 80), (69, 80)]), WHITE, 'f', ln=True),
                L(ell(37, 78, 1.4, 1.4), OUTC, 'f', False), L(ell(63, 78, 1.4, 1.4), OUTC, 'f', False),
                L(quad((40, 62), (50, 58), (60, 62)), (150, 90, 60, 255), 'f', False, False, 1.0)]
             + beard(),
    'side': crop('side', top=2, nape=84) + [L(outline([(30, 6), (38, -6, 1), (44, 4), (54, -4, 1), (58, 4)])),
                                           L(outline([(46, 66), (54, 64), (60, 82), (72, 88), (86, 88), (90, 96), (80, 106), (64, 104), (50, 92)]), 'beard', 'f', ln=True),
                                           L([(72, 70), (86, 74)], OUTC, 'f', False, False, 3.0), L(outline([(78, 76), (87, 77), (86, 80), (79, 80)]), WHITE, 'f', ln=True)],
    'back': crop('back', top=4, nape=84),
})

# Grew Driver: cara larga y nariz grande; pelo rubio en pinchos altos de punta hacia arriba y pinchos cortos a los lados,
# junto a las orejas; ojos ámbar afilados y sonrisa torcida
C('grew-driver', {
    'body': 'delgado', 'pal': pal('#d8b862', SKIN, iris='#c87a1e', shade='#b89844', deep='#8e722a', light='#ecd896', nose='#e8a070'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 99, 'face_front': LONG_FACE, 'eye_y': 76, 'nose': (50, 88, 3.2),
             'hairline': [(16, 60), (20, 44), (34, 38), (50, 40), (66, 38), (80, 44), (84, 60)]},
    'front': [L(outline([(17, 76), (10, 70, 1), (14, 60), (4, 54, 1), (14, 46), (16, 26), (22, 4, 1), (32, 14), (38, -14, 1), (46, 6), (52, -30, 1), (58, 4), (66, -16, 1),
                         (68, 10), (80, 0, 1), (82, 24), (86, 46), (96, 54, 1), (86, 60), (92, 70, 1), (83, 76), (78, 46), (22, 46)])),
              L(outline([(58, 2), (66, -12), (68, 12), (78, 4), (82, 28), (86, 48), (82, 60), (76, 34)]), 'shade', 'b', False),
              strand([(46, 8), (44, 34)], 'deep', 'b', 1.0), strand([(58, 6), (60, 34)], 'deep', 'b', 1.0)],
    'side': [L(outline([(72, 46), (82, 40), (88, 22), (84, 4, 1), (72, 10), (70, -14, 1), (58, 4), (50, -28, 1), (42, 4), (26, -8, 1), (24, 12), (8, 18, 1), (8, 36),
                        (2, 50, 1), (8, 58), (0, 70, 1), (12, 72), (22, 84), (34, 82), (38, 64), (46, 52), (58, 48)])),
             L(outline([(5, 44), (30, 48), (40, 62), (34, 82), (22, 84), (10, 70)]), 'shade', 'b', False)],
    'back': [L(outline([(17, 78), (10, 72, 1), (14, 62), (4, 56, 1), (14, 46), (16, 26), (22, 4, 1), (32, 14), (38, -14, 1), (46, 6), (52, -28, 1), (58, 4), (66, -14, 1),
                        (68, 10), (80, 2, 1), (82, 24), (86, 46), (96, 56, 1), (86, 62), (92, 72, 1), (83, 78), (66, 86), (50, 88), (34, 86)])),
             L(outline([(56, 2), (66, -12), (68, 12), (78, 4), (82, 28), (86, 50), (84, 78), (62, 86)]), 'shade', 'b', False)],
})

# Griff Strummer (portero): melena castaña lisa y larga hasta los hombros, desfilada en puntas, con un flequillo de
# mechones sobre los ojos; ojazos castaños y sonrisa
C('griff-strummer', {
    'body': 'normal', 'pal': pal('#8a5a30', SKIN, iris='#5a3a1e', shade='#6e4622', deep='#4e3016', light='#b48252'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False, 'ears': False},
    'front': longhair('front', length=112, flare=8, top=-2)
             + [fr([(12, 72), (14, 42), (28, 22), (50, 16), (72, 22), (86, 42), (88, 72), (80, 54), (72, 66, 1), (68, 50), (60, 64, 1), (56, 50), (48, 64, 1), (44, 50),
                    (36, 64, 1), (32, 52), (24, 66, 1), (20, 54)])],
    'side': longhair('side', length=112, flare=6) + [fr([(66, 6), (88, 22), (92, 48), (88, 64, 1), (80, 44), (70, 30)])],
    'back': longhair('back', length=112, flare=8, ends=5),
})

# Grover Bearing (portero): cara larga; pelo naranja muy corto en cepillo plano; ojos blancos redondos de pupila pequeña
# con pestañas, dos rombos verdes pintados en las mejillas y una sonrisa
C('grover-bearing', {
    'body': 'delgado', 'pal': pal('#e88a2c', SKIN, shade='#c86e1a', deep='#a0520e', paint='#6a9a4a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 99, 'face_front': LONG_FACE, 'eye_y': 75,
             'hairline': [(16, 60), (18, 44), (34, 38), (50, 38), (66, 38), (82, 44), (84, 60)]},
    'front': [L(outline([(17, 64), (12, 40), (14, 14), (30, 8), (50, 10), (70, 8), (86, 14), (88, 40), (83, 64), (78, 46), (22, 46)])),
              L(outline([(60, 10), (84, 14), (88, 40), (84, 58), (78, 30)]), 'shade', 'b', False)]
             + white_eyes(75, 15, 5.6, 5.6, 1.6)
             + [L([(24, 72), (20, 68)], OUTC, 'f', False, False, 1.4), L([(25, 76), (20, 76)], OUTC, 'f', False, False, 1.4),
                L([(76, 72), (80, 68)], OUTC, 'f', False, False, 1.4), L([(75, 76), (80, 76)], OUTC, 'f', False, False, 1.4),
                L(outline([(28, 84, 1), (34, 78, 1), (40, 84, 1), (34, 90, 1)]), 'paint', 'f', ln=True), L(outline([(72, 84, 1), (66, 78, 1), (60, 84, 1), (66, 90, 1)]), 'paint', 'f', ln=True)],
    'side': [L(outline([(72, 46), (82, 42), (86, 14), (80, 2), (50, 0), (24, 2), (8, 14), (4, 46), (10, 70), (22, 84), (34, 82), (38, 64), (46, 52), (60, 48)])),
             L(outline([(5, 44), (30, 48), (40, 62), (34, 82), (22, 84), (10, 70)]), 'shade', 'b', False),
             L(outline([(78, 84, 1), (82, 78, 1), (86, 84, 1), (82, 90, 1)]), 'paint', 'f', ln=True)] + side_eye(75),
    'back': [L(outline([(17, 76), (12, 40), (12, 6), (30, 0), (50, 2), (70, 0), (88, 6), (88, 40), (83, 76), (66, 84), (50, 86), (34, 84)])),
             L(outline([(58, 2), (86, 6), (88, 40), (83, 76), (62, 84)]), 'shade', 'b', False)],
})


def beanie(view, c='hat', cd='hat_d', low=60):
    """Gorro de lana ceñido hasta las cejas, con rayas de punto."""
    if view == 'front':
        out = [L(outline([(10, low + 4), (8, 30), (22, 6), (50, -4), (78, 6), (92, 30), (90, low + 4), (50, low)]), c, 'f', ln=True),
               L(outline([(60, -2), (80, 8), (92, 32), (90, low + 2), (76, low)]), cd, 'f', False)]
        return out + [L([(x, 4 + abs(x - 50) * 0.3), (x * 0.96 + 2, low - 2)], cd, 'f', False, False, 0.9) for x in (22, 36, 50, 64, 78)]
    if view == 'side':
        return [L(outline([(10, 66), (4, 34), (20, 6), (50, -4), (76, 4), (90, 24), (90, low - 4), (60, low - 2), (40, 62)]), c, 'f', ln=True)]
    return [L(outline([(10, 72), (8, 30), (22, 6), (50, -4), (78, 6), (92, 30), (90, 72), (50, 76)]), c, 'f', ln=True),
            L(outline([(58, -2), (80, 8), (92, 32), (90, 72), (66, 74)]), cd, 'f', False)]


# Guile Crocket: pelo castaño rojizo con raya en medio que le cae por los lados hasta la mandíbula, en puntas abiertas
# hacia fuera, y un mechón sobre un ojo; ojos azul grisáceo afilados, dientes apretados y rayas en las mejillas
C('guile-crocket', {
    'body': 'normal', 'pal': pal('#a84a2a', SKIN, iris='#5a7a9a', shade='#8a381c', deep='#682812', light='#cc7a52'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 95, 'hairline': False, 'ears': False},
    'front': [L(outline([(6, 90, 1), (2, 78), (8, 54), (4, 30), (18, 8), (40, -2), (60, -2), (82, 8), (96, 30), (92, 54), (98, 78), (94, 90, 1), (84, 78), (84, 58), (16, 58),
                         (16, 78)])),
              L(outline([(58, 0), (82, 10), (96, 32), (92, 56), (96, 86), (84, 74), (82, 40)]), 'shade', 'b', False),
              fr([(14, 76), (12, 46), (24, 22), (44, 12), (50, 4), (56, 12), (76, 22), (88, 46), (86, 76), (80, 56), (70, 48), (60, 50), (54, 40), (50, 54), (44, 70),
                  (40, 84, 1), (38, 64), (28, 54), (20, 62)]),
              L([(26, 84), (32, 82)], (150, 80, 60, 255), 'f', False, False, 1.2), L([(74, 84), (68, 82)], (150, 80, 60, 255), 'f', False, False, 1.2)],
    'side': [L(outline([(70, 46), (84, 44), (90, 28), (80, 8), (56, -2), (30, 2), (10, 18), (2, 44), (4, 70), (-2, 88, 1), (14, 82), (26, 92, 1), (36, 82), (44, 88, 1),
                        (48, 70), (54, 58), (62, 52)])),
             L(outline([(4, 44), (30, 46), (44, 70), (40, 86), (20, 88), (4, 78)]), 'shade', 'b', False),
             fr([(66, 6), (88, 22), (92, 48), (88, 62, 1), (80, 44), (70, 30)])],
    'back': [L(outline([(6, 90, 1), (2, 78), (8, 54), (4, 30), (18, 8), (50, -2), (82, 8), (96, 30), (92, 54), (98, 78), (94, 90, 1), (80, 86), (70, 96, 1), (60, 86),
                        (50, 96, 1), (40, 86), (30, 96, 1), (20, 86)])),
             L(outline([(58, 0), (82, 10), (96, 32), (92, 56), (96, 88), (64, 88)]), 'shade', 'b', False), strand([(50, 2), (50, 40)], 'deep', 'b', 1.0)],
})

# Gus Potter: carota redonda y mofletuda; pelo verde rapado al cero, apenas una franja corta en lo alto de la cabeza;
# ojos blancos redondos de enfado y los dientes apretados entre labios naranjas
C('gus-potter', {
    'body': 'corpulento', 'pal': pal('#5a8a3a', SKIN, shade='#466e2a', deep='#30501c', lips='#e0882e'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'none', 'face_front': WIDE_FACE,
             'hairline': [(14, 46), (20, 30), (34, 22), (50, 20), (66, 22), (80, 30), (86, 46)]},
    'front': crop('front', top=14, side=46, w=1) + white_eyes(76, 15, 6.2, 5.8, 2.0)
             + [L([(26, 66), (42, 70)], OUTC, 'f', False, False, 2.8), L([(74, 66), (58, 70)], OUTC, 'f', False, False, 2.8),
                L(outline([(40, 92), (60, 92), (62, 98), (38, 98)]), 'lips', 'f', ln=True), L(outline([(43, 94), (57, 94), (57, 96.5), (43, 96.5)]), WHITE, 'f', False),
                L([(43, 95.2), (57, 95.2)], OUTC, 'f', False, False, 0.6)],
    'side': crop('side', top=14, nape=76) + side_eye(76),
    'back': crop('back', top=14, nape=74),
})

# Guy Dance: grandullón de piel tostada y cuello ancho; pelo rosa coral revuelto en pinchos con una calva de cicatriz en
# lo alto; nariz grande, ojos achinados de pícaro y una sonrisa de dientes
C('guy-dance', {
    'body': 'corpulento', 'pal': pal('#e27e7e', '#c0885a', shade='#c26262', deep='#9a4646', light='#f2a8a8', nose='#a87048'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 97, 'face_front': WIDE_FACE, 'nose': (50, 86, 4.0),
             'hairline': [(14, 66), (18, 50), (26, 56), (34, 46), (46, 54), (54, 44), (62, 54), (70, 46), (78, 56), (86, 66)]},
    'front': messy('front', amp=14, n=12, seed=44, rx=48, ry=40, cy=40, lo=64)
             + [L(outline([(56, 18), (62, 12), (64, 20), (58, 26)]), 'deep', 'f', False),
                L([(28, 74), (42, 76)], OUTC, 'f', False, False, 2.4), L([(72, 74), (58, 76)], OUTC, 'f', False, False, 2.4)],
    'side': messy('side', amp=14, n=11, seed=44, nape=84) + [L([(76, 76), (86, 77)], OUTC, 'f', False, False, 2.4)],
    'back': messy('back', amp=14, n=12, seed=44, nape=84),
})

# Guy Forker: grandullón de piel tostada y cuello ancho, con un gorro de lana azul pizarra calado hasta las cejas; ojos
# afilados de enfado, una raya en la mejilla y la boca abierta de labios gruesos
C('guy-forker', {
    'body': 'corpulento', 'pal': pal('#2a2222', '#c08a58', shade='#1e1818', deep='#141010', hat='#4c5c72', hat_d='#3a4858', lips='#9a5a3a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'face_front': WIDE_FACE, 'hairline': False},
    'front': beanie('front', low=60) + [L(outline([(38, 92), (50, 88), (62, 92), (60, 100), (50, 102), (40, 100)]), 'lips', 'f', ln=True),
                                        L(outline([(42, 94), (58, 94), (56, 98), (44, 98)]), (90, 36, 30, 255), 'f', False),
                                        L([(70, 84), (76, 82)], (150, 80, 60, 255), 'f', False, False, 1.2)],
    'side': beanie('side', low=60) + [L(ell(85, 95, 3, 3.6), 'lips', 'f', ln=True)],
    'back': beanie('back'),
})

# Gwyn Penn (portero): lleva una capucha de pingüino: arriba azul marino con dos ojos crema y el pico amarillo, y las
# solapas crema que le caen a los lados; asoma el pelo verde oscuro en flequillo; ojazos, cejas gruesas y sonrisa
C('gwyn-penn', {
    'body': 'normal', 'pal': pal('#2a4a2a', SKIN, shade='#1e381e', deep='#142614', hood='#2e3e5e', hood_d='#22304a', cream='#f2e8b4', cream_d='#d8cc90', beak='#e8b82a'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(10, 108), (4, 80), (6, 50), (94, 50), (96, 80), (90, 108), (82, 106), (82, 60), (18, 60), (18, 106)]), 'cream'),
              L(outline([(14, 68), (16, 54), (30, 50), (50, 52), (70, 50), (84, 54), (86, 68), (76, 60), (66, 66), (58, 58), (50, 66), (42, 58), (34, 66), (24, 60)]), 'mid', 'b'),
              L(outline([(8, 56), (-8, 50, 1), (6, 30), (24, 8), (50, 0), (76, 8), (94, 30), (108, 50, 1), (92, 56), (50, 52)]), 'hood', 'f', ln=True),
              L(outline([(60, 4), (78, 10), (94, 30), (104, 48), (88, 52), (80, 30)]), 'hood_d', 'f', False),
              L(ell(28, 30, 10, 13), 'cream', 'f', ln=True), L(ell(72, 30, 10, 13), 'cream', 'f', ln=True),
              L(ell(28, 32, 2.4, 3.2), OUTC, 'f', False), L(ell(72, 32, 2.4, 3.2), OUTC, 'f', False),
              L(outline([(40, 44), (50, 34), (60, 44), (50, 50)]), 'beak', 'f', ln=True),
              L(outline([(8, 58), (14, 54), (20, 100), (12, 104)]), 'cream_d', 'f', False), L(outline([(92, 58), (86, 54), (80, 100), (88, 104)]), 'cream_d', 'f', False)]
             + brows(66, OUTC, 3.4, 15, 0.6, 12)
             + [L([(26, 86), (32, 84)], (150, 80, 60, 255), 'f', False, False, 1.0), L([(74, 86), (68, 84)], (150, 80, 60, 255), 'f', False, False, 1.0)],
    'side': [L(outline([(30, 108), (14, 90), (14, 56), (44, 56), (50, 90), (46, 108)]), 'cream'),
             L(outline([(70, 54), (90, 52), (94, 30), (80, 8), (50, -2), (24, 4), (6, 24), (0, 50), (10, 70), (30, 60), (50, 56)]), 'hood', 'f', ln=True),
             L(ell(76, 26, 8, 12), 'cream', 'f', ln=True), L(ell(78, 28, 2, 3), OUTC, 'f', False),
             L(outline([(88, 40), (102, 46), (90, 50)]), 'beak', 'f', ln=True)],
    'back': [L(outline([(10, 104), (4, 80), (6, 50), (94, 50), (96, 80), (90, 104), (50, 106)]), 'cream'),
             L(outline([(8, 60), (-8, 52, 1), (6, 30), (24, 8), (50, 0), (76, 8), (94, 30), (108, 52, 1), (92, 60), (50, 64)]), 'hood', 'f', ln=True),
             L(outline([(58, 2), (78, 10), (94, 30), (104, 50), (90, 58), (66, 60)]), 'hood_d', 'f', False)],
})

# Haden Seek: piel morena y carota ancha; pelo verde azulado oscuro en una corona alta de picos, con el pelo de debajo más
# oscuro en mechones que bajan a la frente; cejas en espiral, ojos blancos redondos y boca seria
C('haden-seek', {
    'body': 'corpulento', 'pal': pal('#3e7266', '#8a6a4a', shade='#2e5a50', deep='#244038', light='#5e9a8a', under='#2a3e38'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 97, 'face_front': WIDE_FACE,
             'hairline': [(12, 64), (16, 52), (24, 58), (30, 48), (40, 56), (50, 48), (60, 56), (70, 48), (76, 58), (84, 52), (88, 64)]},
    'front': [L(outline([(12, 64), (8, 40), (0, 0, 1), (20, 14), (30, -20, 1), (42, 8), (60, 4), (80, -26, 1), (78, 10), (100, -4, 1), (92, 40), (88, 64), (82, 54), (18, 54)])),
              L(outline([(60, 6), (80, -22), (78, 12), (96, 2), (90, 40), (86, 58), (78, 34)]), 'shade', 'b', False),
              L(outline([(12, 64), (10, 46), (24, 36), (50, 32), (76, 36), (90, 46), (88, 64), (82, 54), (18, 54)]), 'under', 'b', False)]
             + white_eyes(77, 15, 5.8, 5.6, 2.0)
             + [L(quad((24, 68), (30, 62), (40, 66)) + quad((40, 66), (36, 70), (32, 66)), OUTC, 'f', False, False, 1.8),
                L(quad((76, 68), (70, 62), (60, 66)) + quad((60, 66), (64, 70), (68, 66)), OUTC, 'f', False, False, 1.8)],
    'side': [L(outline([(72, 54), (84, 46), (94, 6, 1), (76, 18), (70, -20, 1), (56, 6), (34, 2), (10, -10, 1), (12, 20), (2, 48), (8, 70), (20, 80), (34, 78), (40, 62),
                        (50, 56), (62, 56)])),
             L(outline([(5, 46), (30, 48), (40, 62), (34, 78), (20, 80), (8, 70)]), 'under', 'b', False)] + side_eye(77),
    'back': [L(outline([(14, 74), (8, 40), (0, 0, 1), (20, 14), (30, -20, 1), (42, 8), (60, 4), (80, -26, 1), (78, 10), (100, -4, 1), (92, 40), (86, 74), (66, 82), (50, 84),
                        (34, 82)])),
             L(outline([(14, 50), (50, 46), (88, 50), (86, 74), (66, 82), (50, 84), (34, 82), (14, 74)]), 'under', 'b', False)],
})

# Hal Lebutt (portero): pelo violeta oscuro recogido en un moño alto del que sale una cola larga hacia un lado, con dos
# patillas largas en punta junto a las orejas; ojos blancos redondos, cejas de enfado y boca de gato
C('hal-lebutt', {
    'body': 'normal', 'pal': pal('#4a3c6c', SKIN, shade='#382c54', deep='#261e3c', light='#6e5e98'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'none',
             'hairline': [(16, 72), (18, 52), (30, 44), (50, 42), (70, 44), (82, 52), (84, 72)]},
    'front': [L(outline([(17, 76), (12, 46), (22, 20), (50, 10), (78, 20), (88, 46), (83, 76), (80, 52), (20, 52)])),
              L(outline([(58, 12), (78, 22), (88, 46), (84, 70), (76, 36)]), 'shade', 'b', False),
              L(outline([(40, 16), (44, -6), (58, -10), (64, 4), (60, 16)])),
              L(rope((44, -2), (16, -8), (2, 30), 12), 'mid', 'b'),
              strand([(52, 14), (50, 40)], 'shade', 'b', 1.0),
              L(outline([(14, 66), (12, 86), (16, 96, 1), (20, 84), (20, 66)]), 'mid', 'f', ln=True), L(outline([(86, 66), (88, 86), (84, 96, 1), (80, 84), (80, 66)]), 'mid', 'f', ln=True)]
             + white_eyes(76, 15, 6, 5.6, 1.8) + [L(quad((42, 93), (46, 97), (50, 94)) + quad((50, 94), (54, 97), (58, 93))[1:], OUTC, 'f', False, False, 1.3)],
    'side': [L(outline([(70, 50), (82, 44), (86, 26), (74, 12), (52, 6), (28, 10), (10, 26), (4, 50), (10, 72), (22, 84), (34, 82), (38, 64), (46, 56), (60, 54)])),
             L(outline([(36, 12), (40, -8), (56, -10), (60, 8)])), L(rope((40, -4), (8, -6), (-6, 30), 12), 'mid', 'b'),
             L(outline([(5, 46), (30, 48), (40, 62), (34, 82), (22, 84), (10, 70)]), 'shade', 'b', False),
             L(outline([(66, 56), (72, 56), (70, 92, 1), (64, 70)]), 'mid', 'f', ln=True)] + side_eye(76),
    'back': [L(outline([(17, 78), (12, 46), (22, 20), (50, 10), (78, 20), (88, 46), (83, 78), (66, 86), (50, 88), (34, 86)])),
             L(outline([(56, 12), (80, 22), (88, 46), (83, 78), (62, 86)]), 'shade', 'b', False),
             L(outline([(40, 16), (42, -6), (56, -10), (62, 4), (60, 16)])), L(rope((56, -2), (84, -8), (98, 30), 12), 'mid', 'b')],
})

# Hal Leeward: cara larga; lleva una capucha castaña ribeteada de crema que le enmarca la cara, con un moño azul marino
# que asoma arriba; cejas gruesas castañas, pinturas castañas en las mejillas y la boca abierta de labios gruesos
C('hal-leeward', {
    'body': 'delgado', 'pal': pal('#2c3c5a', SKIN, shade='#202e46', deep='#141e30', hood='#7a4a28', hood_d='#5e361c', trim='#f2e2c0', lips='#c0503a', brow='#6a3e1e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'face_front': LONG_FACE, 'eye_y': 77, 'hairline': False, 'ears': False},
    'front': [L(outline([(8, 100), (4, 60), (12, 26), (30, 10), (50, 6), (70, 10), (88, 26), (96, 60), (92, 100), (84, 104), (82, 60), (74, 36), (50, 30), (26, 36), (18, 60),
                         (16, 104)]), 'hood'),
              L(outline([(16, 104), (18, 60), (26, 36), (50, 30), (74, 36), (82, 60), (84, 104), (78, 104), (76, 62), (70, 42), (50, 36), (30, 42), (24, 62), (22, 104)]), 'trim', 'b', False),
              L(outline([(62, 10), (86, 26), (94, 60), (90, 98), (84, 98), (82, 56)]), 'hood_d', 'b', False),
              L(ell(50, 6, 13, 12))]
             + brows(65, 'brow', 4.4, 15, 0.8, 13)
             + [L(outline([(24, 82), (34, 80), (32, 92), (24, 94)]), 'hood_d', 'f', False), L(outline([(76, 82), (66, 80), (68, 92), (76, 94)]), 'hood_d', 'f', False),
                L(outline([(40, 96), (50, 93), (60, 96), (58, 102), (50, 104), (42, 102)]), 'lips', 'f', ln=True)],
    'side': [L(outline([(66, 30), (52, 10), (28, 6), (8, 22), (0, 56), (4, 100), (40, 104), (48, 70), (56, 52), (68, 40)]), 'hood'),
             L(outline([(70, 32), (64, 40), (54, 54), (48, 74), (46, 104), (54, 104), (56, 74), (62, 56), (76, 38)]), 'trim', 'b', False),
             L(ell(42, 2, 12, 11)), L(outline([(76, 82), (86, 82), (88, 92), (80, 94)]), 'hood_d', 'f', False)],
    'back': [L(outline([(8, 100), (4, 60), (12, 26), (30, 10), (50, 6), (70, 10), (88, 26), (96, 60), (92, 100), (50, 106)]), 'hood'),
             L(outline([(58, 8), (86, 26), (94, 60), (90, 98), (62, 102)]), 'hood_d', 'b', False),
             L(ell(50, 6, 13, 12))],
})


def closed_lash(y=76, sep=15):
    """Ojos cerrados en arco hacia abajo con una pestaña (cara de satisfacción)."""
    out = []
    for cx, s in ((50 - sep, 1), (50 + sep, -1)):
        out.append(L(quad((cx - 7, y - 1), (cx, y + 4), (cx + 7, y - 1)), OUTC, 'f', False, False, 2.2))
        out.append(L([(cx - 7 * s, y - 1), (cx - 10 * s, y - 3)], OUTC, 'f', False, False, 1.6))
    return out


def happy_eyes(y=76, sep=15):
    """Ojos cerrados de risa (^ ^)."""
    return [L(quad((cx - 7, y + 2), (cx, y - 5), (cx + 7, y + 2)), OUTC, 'f', False, False, 2.4) for cx in (50 - sep, 50 + sep)]


# Hal Mullet: cara larga; pelo verde oliva revuelto en pinchos por todos lados, con un rizo que le cae en gancho sobre la
# frente; cejas verdes gruesas, ojos cerrados con pestañas y labios naranjas pintados
C('hal-mullet', {
    'body': 'delgado', 'pal': pal('#6a6a2e', SKIN, shade='#52521e', deep='#383810', light='#8e8e52', lips='#e2702e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': LONG_FACE, 'eye_y': 78,
             'hairline': [(16, 60), (20, 44), (34, 38), (50, 40), (66, 38), (80, 44), (84, 60)]},
    'front': messy('front', amp=14, n=13, seed=55, rx=46, ry=40, cy=40, lo=60)
             + [L(quad((58, 24), (70, 34), (60, 56)), 'mid', 'f', False, False, 4.0), L(quad((58, 24), (70, 34), (60, 56)), 'deep', 'f', False, False, 0.8)]
             + brows(67, 'mid', 4.0, 15, 0.0, 12) + closed_lash(77, 15)
             + [L(outline([(42, 99), (50, 96), (58, 99), (54, 103), (46, 103)]), 'lips', 'f', ln=True)],
    'side': messy('side', amp=14, n=12, seed=55, nape=84) + brow_side(67, 'mid', 4.0) + [L(quad((76, 77), (80, 80), (85, 77)), OUTC, 'f', False, False, 2.0),
                                                                                       L(ell(86, 100, 2.4, 2.6), 'lips', 'f', ln=True)],
    'back': messy('back', amp=14, n=13, seed=55, nape=84),
})

# Hale Quinn: pelo rubio crema en casco liso cortado recto a media frente, con un mechoncito de punta arriba; ojos de
# sueño con las cejas arqueadas, la nariz de dos puntitos y una sonrisa ancha
C('hale-quinn', {
    'body': 'normal', 'pal': pal('#f2e6c0', SKIN, shade='#d6c898', deep='#b0a274', light='#fcf6e2'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': bowl('front', fringe_y=52) + [L(outline([(46, 2), (48, -10, 1), (52, -2), (56, -10, 1), (56, 4)])),
                                          strand([(30, 20), (30, 50)], 'shade', 'b', 1.0), strand([(70, 20), (70, 50)], 'shade', 'b', 1.0)]
             + white_eyes(76, 15, 6, 5.2, 1.8, 1.0)
             + [L(quad((26, 66), (34, 61), (43, 66)), OUTC, 'f', False, False, 2.2), L(quad((74, 66), (66, 61), (57, 66)), OUTC, 'f', False, False, 2.2),
                L(ell(47, 86, 0.9, 0.9), OUTC, 'f', False), L(ell(53, 86, 0.9, 0.9), OUTC, 'f', False)]
             + wide_smile_(93),
    'side': bowl('side') + side_eye(76, 1.0),
    'back': bowl('back'),
})

# Handel Turnon (portero): grandullón de piel muy clara y mandíbula ancha; pelo violeta peinado hacia atrás en un tupé,
# con patillas largas hasta la mandíbula y un mechón que le cae en curva sobre un ojo; ojos cerrados de risa y sonrisa
C('handel-turnon', {
    'body': 'corpulento', 'pal': pal('#5a4a7c', '#fbe6c0', shade='#463a62', deep='#322a48', light='#7e6ea2'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 97, 'face_front': WIDE_FACE,
             'hairline': [(14, 60), (18, 40), (32, 30), (50, 28), (68, 30), (82, 40), (86, 60)]},
    'front': [L(outline([(16, 64), (12, 40), (20, 14), (36, -4), (58, -10), (76, 0), (86, 18), (88, 40), (84, 64), (80, 54), (20, 54)])),
              L(outline([(58, -8), (76, 2), (86, 20), (88, 42), (82, 58), (76, 26)]), 'shade', 'b', False),
              strand([(30, 30), (44, 4), (64, -6)], 'deep', 'b', 1.0), strand([(70, 30), (72, 8)], 'deep', 'b', 1.0),
              fr([(14, 58), (14, 76), (18, 92, 1), (22, 74), (22, 58)]), fr([(86, 58), (86, 76), (82, 92, 1), (78, 74), (78, 58)]),
              fr([(60, 30), (70, 40), (68, 62), (60, 80, 1), (62, 58), (58, 42)])]
             + happy_eyes(76, 15),
    'side': [L(outline([(70, 40), (82, 30), (84, 14), (70, -2), (48, -10), (26, -2), (10, 16), (4, 44), (8, 68), (20, 82), (34, 80), (38, 66), (46, 52), (58, 46)])),
             L(outline([(5, 44), (30, 48), (40, 62), (34, 80), (20, 82), (8, 68)]), 'shade', 'b', False),
             fr([(62, 52), (70, 52), (70, 88, 1), (64, 70)]), L(quad((76, 78), (81, 72), (86, 78)), OUTC, 'f', False, False, 2.2)],
    'back': [L(outline([(16, 76), (12, 40), (20, 14), (36, -2), (58, -8), (76, 2), (86, 18), (88, 40), (84, 76), (66, 84), (50, 86), (34, 84)])),
             L(outline([(58, -6), (76, 4), (86, 20), (88, 44), (84, 76), (62, 84)]), 'shade', 'b', False)],
})

# Hank Halberd (portero): piel tostada; melena rubio oro ondulada hasta los hombros con un pico en medio de la frente;
# cejas gruesas amarillas, dos franjas verde claro pintadas bajo los ojos y una boquita redonda
C('hank-halberd', {
    'body': 'delgado', 'pal': pal('#d8a830', '#c09060', shade='#b88a1e', deep='#8e6a12', light='#ecc866', paint='#c8d8a0'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'none', 'face_front': LONG_FACE, 'eye_y': 77,
             'hairline': [(16, 60), (20, 40), (34, 34), (44, 36), (50, 50), (56, 36), (66, 34), (80, 40), (84, 60)]},
    'front': [L(outline([(6, 108, 1), (2, 90), (8, 70), (4, 44), (14, 16), (40, 2), (62, 2), (86, 16), (96, 44), (92, 70), (98, 90), (94, 108, 1), (84, 96), (84, 60),
                         (16, 60), (16, 96)])),
              L(outline([(62, 4), (86, 18), (96, 46), (92, 72), (96, 104), (84, 92), (82, 44)]), 'shade', 'b', False),
              strand([(44, 6), (46, 40)], 'deep', 'b', 1.0), strand([(56, 6), (54, 40)], 'deep', 'b', 1.0)]
             + brows(65, 'mid', 4.0, 15, 0.4, 13)
             + [L(outline([(26, 82), (32, 82), (32, 100, 1), (28, 94)]), 'paint', 'f', ln=True), L(outline([(74, 82), (68, 82), (68, 100, 1), (72, 94)]), 'paint', 'f', ln=True)]
             + o_mouth(98, (150, 80, 60, 255)),
    'side': [L(outline([(70, 44), (84, 40), (90, 24), (80, 6), (56, -2), (30, 2), (10, 18), (2, 44), (6, 70), (0, 92), (6, 108, 1), (20, 98), (32, 108, 1), (40, 94),
                        (46, 104, 1), (50, 84), (54, 62), (62, 50)])),
             L(outline([(4, 44), (30, 46), (46, 70), (46, 100), (24, 104), (6, 92)]), 'shade', 'b', False),
             L(outline([(80, 84), (84, 84), (84, 100, 1)]), 'paint', 'f', ln=True)] + brow_side(65, 'mid', 4.0),
    'back': [L(outline([(6, 108, 1), (2, 90), (8, 70), (4, 44), (14, 16), (50, 2), (86, 16), (96, 44), (92, 70), (98, 90), (94, 108, 1), (82, 100), (72, 110, 1), (62, 100),
                        (50, 110, 1), (38, 100), (28, 110, 1), (18, 100)])),
             L(outline([(58, 4), (86, 18), (96, 46), (92, 72), (96, 104), (64, 102)]), 'shade', 'b', False)]
            + [strand([(x, 20), (x + 2, 60), (x - 2, 96)], 'deep', 'b', 1.0) for x in (26, 46, 66)],
})

# Hank O'Buff (portero): piel tostada; pelo rosa en rulos gruesos y ondulados a los lados de la cabeza, como una peluca,
# con una cicatriz arriba; cejas rosas, ojos de sueño y una boca ancha de labios gruesos
C('hank-o-buff', {
    'body': 'normal', 'pal': pal('#c87c82', '#c08a58', shade='#a86066', deep='#84464c', light='#e0a4a8', brow='#e0909a', lips='#9a5a3a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': [(16, 66), (20, 46), (34, 40), (50, 38), (66, 40), (80, 46), (84, 66)]},
    'front': [L(outline([(8, 88), (0, 76), (4, 60), (0, 44), (10, 20), (32, 4), (60, 2), (84, 14), (98, 36), (96, 58), (100, 76), (92, 88), (84, 80), (84, 56), (16, 56),
                         (16, 80)])),
              L(outline([(62, 4), (84, 16), (98, 38), (96, 60), (98, 80), (88, 86), (82, 44)]), 'shade', 'b', False)]
             + [strand([(4, y), (22, y - 4)], 'deep', 'b', 1.2) for y in (50, 64, 78)] + [strand([(96, y), (78, y - 4)], 'deep', 'b', 1.2) for y in (50, 64, 78)]
             + [strand([(28, 20), (40, 12), (60, 10)], 'deep', 'b', 1.2), L([(40, 6), (42, 16)], 'deep', 'b', False, False, 1.0)]
             + brows(64, 'brow', 3.6, 15, 0.6, 12) + white_eyes(76, 15, 6, 5, 1.8, 1.4)
             + [L(outline([(36, 92), (50, 89), (64, 92), (60, 98), (50, 99), (40, 98)]), 'lips', 'f', ln=True), L([(38, 94), (62, 94)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(70, 46), (84, 42), (90, 26), (80, 6), (56, -2), (30, 2), (10, 18), (0, 44), (-4, 66), (0, 86), (18, 92), (34, 88), (42, 70), (50, 56), (60, 50)])),
             L(outline([(0, 44), (30, 48), (42, 68), (34, 88), (16, 92), (-2, 84)]), 'shade', 'b', False)]
            + [strand([(2, y), (34, y + 2)], 'deep', 'b', 1.2) for y in (52, 66, 80)] + brow_side(64, 'brow', 3.6) + side_eye(76, 1.4),
    'back': [L(outline([(8, 90), (0, 76), (4, 60), (0, 44), (10, 20), (50, 2), (90, 20), (100, 44), (96, 60), (100, 76), (92, 90), (50, 94)])),
             L(outline([(58, 4), (90, 22), (100, 46), (96, 62), (100, 78), (90, 90), (60, 92)]), 'shade', 'b', False)]
            + [strand([(4, y), (96, y)], 'deep', 'b', 1.2) for y in (54, 70, 84)],
})

# Hank O'Chief (portero): carota redonda y mofletuda con pecas; pelo amarillo muy corto con dos moñitos en forma de
# estrella dorada en lo alto; cejas negras gruesas de enfado, ojos blancos y boca seria
C('hank-o-chief', {
    'body': 'corpulento', 'pal': pal('#e2b62a', '#c08a58', shade='#c0961a', deep='#94700e', light='#f2d660', star='#e8c040'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'face_front': WIDE_FACE,
             'hairline': [(14, 50), (20, 36), (34, 30), (50, 30), (66, 30), (80, 36), (86, 50)]},
    'front': crop('front', top=16, side=50, w=1)
             + [L(outline([(18, 22, 1), (22, 14), (16, 8, 1), (24, 8), (26, 0, 1), (30, 8), (38, 8, 1), (32, 14), (36, 22, 1), (28, 18)]), 'star', 'b', ln=True),
                L(outline([(82, 22, 1), (78, 14), (84, 8, 1), (76, 8), (74, 0, 1), (70, 8), (62, 8, 1), (68, 14), (64, 22, 1), (72, 18)]), 'star', 'b', ln=True)]
             + white_eyes(76, 15, 6, 5.4, 1.8) + brows(65, OUTC, 4.2, 15, 1.0, 14)
             + [L(ell(x, 86 + (i % 2) * 2, 0.9, 0.9), (150, 80, 60, 255), 'f', False) for i, x in enumerate((24, 28, 32, 68, 72, 76))],
    'side': crop('side', top=16, nape=80) + [L(outline([(36, 18, 1), (40, 10), (34, 4, 1), (42, 4), (44, -4, 1), (48, 4), (56, 4, 1), (50, 10), (54, 18, 1), (46, 14)]), 'star', 'b', ln=True)]
            + side_eye(76) + brow_side(65, OUTC, 4.2, 1.0),
    'back': crop('back', top=16, nape=80)
            + [L(outline([(18, 22, 1), (22, 14), (16, 8, 1), (24, 8), (26, 0, 1), (30, 8), (38, 8, 1), (32, 14), (36, 22, 1), (28, 18)]), 'star', 'b', ln=True),
               L(outline([(82, 22, 1), (78, 14), (84, 8, 1), (76, 8), (74, 0, 1), (70, 8), (62, 8, 1), (68, 14), (64, 22, 1), (72, 18)]), 'star', 'b', ln=True)],
})

# Hank Shortman: piel tostada; pelo rubio pajizo en mechones despeinados de punta, con el flequillo en picos sobre los
# ojos; ojos ámbar grandes y sonrisa
C('hank-shortman', {
    'body': 'normal', 'pal': pal('#dcc274', '#c08a58', iris='#c8701e', shade='#bea256', deep='#94803a', light='#eedca2'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': messy('front', amp=9, n=12, seed=66, rx=46, ry=40, cy=40, lo=66)
             + [fr([(14, 66), (14, 42), (26, 24), (50, 16), (74, 24), (86, 42), (86, 66), (80, 52), (72, 62, 1), (66, 48), (56, 58, 1), (52, 44), (44, 60, 1), (40, 46),
                    (30, 60, 1), (24, 50)])],
    'side': messy('side', amp=9, n=11, seed=66, nape=86) + [fr([(66, 8), (88, 22), (92, 46), (88, 58, 1), (80, 40), (70, 30)])],
    'back': messy('back', amp=9, n=12, seed=66, nape=86),
})

# Hans Bigger: pelo naranja cortado en casco con flequillo de mechones, y un pañuelo granate atado a la frente cuyas dos
# colas largas le caen por detrás; ojos afilados de enfado y boca seria
C('hans-bigger', {
    'body': 'normal', 'pal': pal('#d8701e', SKIN, iris='#2a2020', shade='#b45a14', deep='#8a400c', light='#eea05a', band='#6a3a4a', band_d='#522c38'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'hairline': False},
    'front': bowl('front', fringe_y=60)
             + [fr([(10, 70), (10, 44), (22, 22), (50, 14), (78, 22), (90, 44), (90, 70), (82, 60), (74, 68, 1), (68, 56), (58, 66, 1), (52, 54), (44, 66, 1), (38, 54),
                    (30, 66, 1), (22, 58)]),
                L(outline([(8, 50), (8, 34), (30, 26), (50, 24), (70, 26), (92, 34), (92, 50), (70, 42), (50, 40), (30, 42)]), 'band', 'f', ln=True),
                L(outline([(54, 25), (70, 27), (90, 34), (90, 48), (70, 41), (54, 40)]), 'band_d', 'f', False),
                L(rope((90, 44), (106, 62), (100, 96), 7), 'band', 'b')],
    'side': bowl('side') + [L(outline([(6, 40), (30, 28), (60, 24), (92, 28), (94, 42), (60, 40), (30, 46), (8, 54)]), 'band', 'f', ln=True),
                            L(rope((10, 46), (-10, 60), (-6, 96), 7), 'band', 'b'), L(rope((12, 48), (-4, 70), (6, 100), 6), 'band_d', 'b')],
    'back': bowl('back') + [L(outline([(6, 40), (30, 34), (50, 32), (70, 34), (94, 40), (94, 52), (50, 46), (6, 52)]), 'band', 'f', ln=True),
                            L(rope((50, 46), (40, 70), (34, 100), 7), 'band', 'f'), L(rope((50, 46), (62, 70), (68, 100), 7), 'band', 'f')],
})


def curl_cap(view, c='mid', top=-2, lo=62, nape=84):
    """Mata de rizos gruesos (bolas) que cubre la cabeza."""
    if view == 'front':
        pts = [(16, lo)] + [(50 + 40 * __import__('math').cos(a / 10 * 3.1416) * (1.08 if i % 2 else 0.98),
                             36 - (38 - top) * __import__('math').sin(a / 10 * 3.1416) * (1.08 if i % 2 else 0.98)) for i, a in enumerate(range(0, 11))][::-1] + [(84, lo)]
        return [L(blob(pts, 6), c), L(blob([(60, 8), (88, 30), (88, lo - 6), (76, 40)], 6), 'shade', 'b', False)]
    return []


# Harley Trotter: una mata de rizos verdes gruesos y redondos sobre la cabeza; ojos blancos afilados con pestañas y
# sonrisa pícara
def _curls(cx, cy, rx, ry, n=10):
    import math
    return [ell(cx + rx * math.cos(2 * math.pi * i / n), cy + ry * math.sin(2 * math.pi * i / n), 9, 8) for i in range(n)]


C('harley-trotter', {
    'body': 'normal', 'pal': pal('#3a8c3c', '#c48c5a', shade='#2c6e2e', deep='#1e5020', light='#5eac5e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 94,
             'hairline': [(16, 62), (18, 52), (28, 46), (40, 50), (50, 44), (60, 50), (72, 46), (82, 52), (84, 62)]},
    'front': [L(outline([(16, 62), (12, 40), (20, 16), (50, 4), (80, 16), (88, 40), (84, 62), (80, 50), (20, 50)]))]
             + [L(e, 'mid', 'b', True, False) for e in _curls(50, 22, 34, 22, 11)] + [L(ell(50, 22, 26, 16), 'mid', 'b', False)]
             + [L(e, 'mid', 'f', False, True) for e in (ell(22, 48, 8, 7), ell(36, 44, 8, 7), ell(50, 42, 8, 7), ell(64, 44, 8, 7), ell(78, 48, 8, 7))]
             + [L(outline([(26, 72), (44, 76), (42, 81), (28, 79)]), WHITE, 'f', ln=True), L(outline([(74, 72), (56, 76), (58, 81), (72, 79)]), WHITE, 'f', ln=True),
                L(ell(36, 77.5, 1.6, 1.8), OUTC, 'f', False), L(ell(64, 77.5, 1.6, 1.8), OUTC, 'f', False),
                L(quad((26, 70), (34, 64), (44, 70)), OUTC, 'f', False, False, 1.8), L(quad((74, 70), (66, 64), (56, 70)), OUTC, 'f', False, False, 1.8)],
    'side': [L(outline([(70, 50), (82, 44), (86, 26), (74, 10), (52, 4), (28, 8), (10, 24), (4, 48), (10, 70), (22, 82), (34, 80), (38, 64), (46, 56), (60, 54)]))]
            + [L(e, 'mid', 'b', True, False) for e in _curls(44, 30, 34, 26, 11)] + [L(ell(44, 30, 26, 18), 'mid', 'b', False)]
            + [L(outline([(76, 72), (88, 74), (87, 79), (78, 78)]), WHITE, 'f', ln=True), L(ell(85, 76, 1.2, 1.6), OUTC, 'f', False)],
    'back': [L(outline([(16, 74), (12, 40), (20, 16), (50, 4), (80, 16), (88, 40), (84, 74), (66, 82), (50, 84), (34, 82)]))]
            + [L(e, 'mid', 'b', True, False) for e in _curls(50, 34, 36, 34, 13)] + [L(ell(50, 34, 28, 26), 'mid', 'b', False)],
})

# Harly Profett: pelo gris pardo con raya en medio que le cae a los lados en dos mechones gruesos recogidos con anillas
# doradas a la altura de la barbilla, más oscuros por debajo; cejas grises gruesas, ojitos de punto y boca seria
C('harly-profett', {
    'body': 'normal', 'pal': pal('#9a8a80', '#c8925a', shade='#7e6e66', deep='#5e504a', light='#bcaea4', ring='#e2b42a', low='#6e5a4e'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'frown', 'mouth_y': 95, 'hairline': False, 'ears': False},
    'front': [L(outline([(2, 86), (-2, 62), (6, 30), (24, 8), (50, 0), (76, 8), (94, 30), (102, 62), (98, 86), (86, 84), (84, 56), (16, 56), (14, 84)])),
              L(outline([(60, 2), (78, 10), (94, 32), (100, 62), (96, 82), (86, 80), (84, 44)]), 'shade', 'b', False),
              L(outline([(4, 84), (20, 84), (24, 104), (14, 110, 1), (4, 102)]), 'low', 'b'), L(outline([(96, 84), (80, 84), (76, 104), (86, 110, 1), (96, 102)]), 'low', 'b'),
              L(outline([(2, 80), (22, 80), (22, 88), (4, 88)]), 'ring', 'f', ln=True), L(outline([(98, 80), (78, 80), (78, 88), (96, 88)]), 'ring', 'f', ln=True),
              fr([(14, 72), (14, 44), (28, 22), (50, 14), (72, 22), (86, 44), (86, 72), (80, 54), (64, 46), (52, 40), (48, 40), (36, 46), (20, 54)]),
              L(outline([(44, 4), (50, 0), (56, 4), (52, 20), (48, 20)]), 'deep', 'f', False)]
             + brows(66, 'light', 4.4, 15, 0.0, 13),
    'side': [L(outline([(70, 46), (84, 44), (90, 28), (80, 8), (56, -2), (30, 2), (10, 18), (0, 46), (2, 80), (20, 84), (36, 80), (44, 66), (52, 56), (62, 50)])),
             L(outline([(14, 82), (30, 82), (32, 104), (22, 110, 1), (12, 102)]), 'low', 'b'),
             L(outline([(12, 78), (32, 78), (32, 86), (12, 86)]), 'ring', 'f', ln=True),
             L(outline([(2, 44), (30, 48), (44, 66), (34, 80), (14, 82), (2, 72)]), 'shade', 'b', False)] + brow_side(66, 'light', 4.4),
    'back': [L(outline([(2, 86), (-2, 62), (6, 30), (24, 8), (50, 0), (76, 8), (94, 30), (102, 62), (98, 86), (50, 90)])),
             L(outline([(58, 2), (78, 10), (94, 32), (100, 62), (96, 84), (60, 88)]), 'shade', 'b', False),
             L(outline([(4, 84), (24, 84), (24, 104), (14, 110, 1), (4, 102)]), 'low', 'b'), L(outline([(96, 84), (76, 84), (76, 104), (86, 110, 1), (96, 102)]), 'low', 'b'),
             L(outline([(2, 80), (24, 80), (24, 88), (4, 88)]), 'ring', 'f', ln=True), L(outline([(98, 80), (76, 80), (76, 88), (96, 88)]), 'ring', 'f', ln=True),
             strand([(50, 2), (50, 86)], 'deep', 'b', 1.0)],
})

# Harold Derry: grandullón de cara redonda y papada; pelo rubio oro muy corto cortado recto, peinado hacia atrás; cejas
# amarillas gruesas, ojos blancos de pupila pequeña y una boca ancha de labios naranjas
C('harold-derry', {
    'body': 'corpulento', 'pal': pal('#d8b42a', SKIN, shade='#b8941a', deep='#8e700e', lips='#e0782a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': WIDE_FACE, 'nose': (50, 86, 3.4),
             'hairline': [(14, 58), (18, 40), (34, 32), (50, 32), (66, 32), (82, 40), (86, 58)]},
    'front': [L(outline([(16, 60), (12, 40), (14, 12), (30, 4), (50, 6), (70, 4), (86, 12), (88, 40), (84, 60), (80, 46), (20, 46)])),
              L(outline([(60, 6), (84, 12), (88, 40), (84, 56), (78, 30)]), 'shade', 'b', False)]
             + [strand([(x, 8), (x, 34)], 'shade', 'b', 1.0) for x in (26, 38, 50, 62, 74)]
             + brows(64, 'mid', 5.0, 15, -0.6, 14) + white_eyes(76, 15, 6.2, 5.4, 1.8)
             + [L(outline([(36, 94), (50, 91), (64, 94), (62, 100), (50, 101), (38, 100)]), 'lips', 'f', ln=True), L([(38, 96), (62, 96)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(72, 44), (82, 40), (86, 14), (80, 4), (50, 2), (24, 4), (8, 16), (4, 46), (10, 70), (22, 82), (34, 80), (38, 64), (46, 52), (60, 48)])),
             L(outline([(5, 44), (30, 48), (40, 62), (34, 80), (22, 82), (10, 70)]), 'shade', 'b', False)] + brow_side(64, 'mid', 5.0) + side_eye(76),
    'back': [L(outline([(16, 74), (12, 40), (14, 12), (30, 4), (50, 6), (70, 4), (86, 12), (88, 40), (84, 74), (66, 82), (50, 84), (34, 82)])),
             L(outline([(58, 6), (84, 12), (88, 40), (84, 74), (62, 82)]), 'shade', 'b', False)],
})

# Harry Caine (portero): piel tostada; pelo blanco verdoso en melenita lisa que se abre en puntas hacia los lados a la
# altura de las orejas, con el flequillo de mechones; ojos lila afilados de enfado y boca seria
C('harry-caine', {
    'body': 'normal', 'pal': pal('#d2eee6', '#c8925a', iris='#8a7aa8', shade='#a8ccc4', deep='#86aaa2', light='#eefaf6'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(16, 76), (8, 66), (-8, 68, 1), (4, 56), (4, 30), (20, 8), (50, 0), (80, 8), (96, 30), (96, 56), (108, 68, 1), (92, 66), (84, 76), (82, 58), (18, 58)])),
              L(outline([(60, 2), (82, 10), (96, 32), (100, 62), (88, 62), (82, 40)]), 'shade', 'b', False),
              fr([(14, 66), (14, 42), (26, 22), (50, 14), (74, 22), (86, 42), (86, 66), (80, 52), (72, 62, 1), (66, 48), (58, 60, 1), (52, 46), (44, 60, 1), (40, 46),
                  (30, 60, 1), (24, 50)])],
    'side': [L(outline([(70, 46), (84, 44), (90, 28), (80, 8), (56, -2), (30, 2), (10, 18), (2, 46), (6, 64), (-8, 72, 1), (12, 74), (26, 84), (36, 80), (40, 64), (48, 56),
                        (60, 52)])),
             L(outline([(4, 46), (30, 48), (40, 62), (34, 80), (20, 82), (6, 70)]), 'shade', 'b', False),
             fr([(66, 6), (88, 22), (92, 46), (88, 58, 1), (80, 40), (70, 30)])],
    'back': [L(outline([(16, 80), (8, 68), (-8, 70, 1), (4, 58), (4, 30), (20, 8), (50, 0), (80, 8), (96, 30), (96, 58), (108, 70, 1), (92, 68), (84, 80), (66, 88), (50, 90),
                        (34, 88)])),
             L(outline([(58, 2), (82, 10), (96, 32), (100, 64), (84, 80), (62, 88)]), 'shade', 'b', False)],
})

# Harry Harper (portero): pelo azul verdoso con mechones gruesos barridos hacia un lado, uno que le cae sobre un ojo y
# puntas que se abren en la nuca; ojos verde agua y sonrisa de lado
C('harry-harper', {
    'body': 'normal', 'pal': pal('#4c8ca2', SKIN, iris='#3a9a9a', shade='#3a7286', deep='#285464', light='#7cb4c6'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(16, 80), (10, 66), (-6, 62, 1), (6, 50), (4, 28), (20, 8), (46, -2), (56, -12, 1), (60, 0), (80, 8), (96, 30), (96, 52), (106, 60, 1), (90, 64),
                         (84, 80), (82, 58), (18, 58)])),
              L(outline([(60, 2), (82, 10), (96, 32), (100, 58), (88, 60), (82, 40)]), 'shade', 'b', False),
              fr([(14, 68), (14, 42), (28, 20), (54, 12), (76, 18), (88, 38), (86, 62), (78, 46), (70, 54), (64, 46), (54, 56), (44, 70), (36, 84, 1), (34, 64), (24, 62)]),
              strand([(54, 16), (40, 46)], 'deep', 'f', 1.0)],
    'side': [L(outline([(70, 46), (84, 44), (90, 28), (80, 8), (60, -2), (54, -12, 1), (46, 0), (24, 4), (8, 20), (2, 46), (6, 62), (-8, 70, 1), (10, 74), (20, 86), (36, 80),
                        (40, 64), (48, 56), (60, 52)])),
             L(outline([(4, 46), (30, 48), (40, 62), (34, 80), (20, 84), (6, 70)]), 'shade', 'b', False),
             fr([(66, 6), (88, 22), (92, 48), (86, 62, 1), (80, 44), (70, 30)])],
    'back': [L(outline([(16, 82), (10, 68), (-6, 64, 1), (6, 52), (4, 28), (20, 8), (46, -2), (56, -12, 1), (60, 0), (80, 8), (96, 30), (96, 54), (106, 62, 1), (90, 66),
                        (84, 82), (66, 88), (50, 90), (34, 88)])),
             L(outline([(58, 2), (82, 10), (96, 32), (100, 60), (84, 82), (62, 88)]), 'shade', 'b', False)],
})

# Harry Overton (portero): pelo de dos colores: pinchos crema en lo alto y los lados lisos verde grisáceo hasta la
# mandíbula; ojos afilados de enfado y la boca abierta en una mueca de labios rosados
C('harry-overton', {
    'body': 'normal', 'pal': pal('#8a8a6e', SKIN, iris='#2a2020', shade='#6e6e56', deep='#4e4e3c', top='#eee8cc', top_d='#d0c8a6', lips='#c88a8a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none',
             'hairline': [(16, 66), (18, 48), (30, 42), (50, 40), (70, 42), (82, 48), (84, 66)]},
    'front': [L(outline([(16, 92, 1), (12, 66), (12, 40), (24, 20), (76, 20), (88, 40), (88, 66), (84, 92, 1), (80, 70), (80, 50), (20, 50), (20, 70)])),
              L(outline([(26, 30), (10, 14, 1), (28, 14), (24, -6, 1), (40, 6), (50, -12, 1), (58, 6), (76, -6, 1), (72, 14), (92, 14, 1), (74, 30), (50, 40)]), 'top'),
              L(outline([(58, 6), (76, -4), (72, 16), (88, 16), (74, 28), (62, 30)]), 'top_d', 'b', False),
              L(outline([(38, 92), (50, 89), (62, 92), (60, 99), (50, 100), (40, 99)]), 'lips', 'f', ln=True),
              L(outline([(42, 93.5), (58, 93.5), (56, 97), (44, 97)]), (120, 50, 50, 255), 'f', False)],
    'side': [L(outline([(70, 50), (80, 44), (84, 28), (74, 16), (40, 16), (14, 22), (4, 48), (8, 72), (6, 92, 1), (20, 84), (34, 82), (38, 64), (46, 56), (60, 54)])),
             L(outline([(18, 24), (2, 10, 1), (22, 10), (20, -8, 1), (36, 4), (48, -12, 1), (54, 6), (72, -4, 1), (68, 12), (86, 18, 1), (70, 26), (40, 30)]), 'top'),
             L(ell(86, 96, 3, 3.4), 'lips', 'f', ln=True)],
    'back': [L(outline([(14, 90, 1), (12, 66), (12, 40), (24, 20), (76, 20), (88, 40), (88, 66), (86, 90, 1), (66, 88), (50, 90), (34, 88)])),
             L(outline([(26, 30), (10, 14, 1), (28, 14), (24, -6, 1), (40, 6), (50, -12, 1), (58, 6), (76, -6, 1), (72, 14), (92, 14, 1), (74, 30), (50, 36)]), 'top')],
})

# Harry Redcastle: pelo castaño oscuro en casco con el flequillo de mechones y dos puntas abiertas hacia fuera junto a las
# orejas; ojazos redondos y sonrisa
C('harry-redcastle', {
    'body': 'normal', 'pal': pal('#4a3424', SKIN, shade='#38261a', deep='#261810', light='#6e5440'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(16, 72), (8, 62), (-4, 58, 1), (6, 50), (6, 28), (22, 8), (50, 0), (78, 8), (94, 28), (94, 50), (104, 58, 1), (92, 62), (84, 72), (82, 56), (18, 56)])),
              L(outline([(60, 2), (80, 10), (94, 30), (100, 56), (88, 58), (82, 38)]), 'shade', 'b', False),
              fr([(14, 64), (14, 42), (26, 22), (50, 14), (74, 22), (86, 42), (86, 64), (80, 52), (72, 60, 1), (66, 48), (56, 58, 1), (52, 46), (44, 58, 1), (40, 46),
                  (30, 58, 1), (24, 50)])],
    'side': [L(outline([(70, 46), (84, 44), (90, 28), (80, 8), (56, -2), (30, 2), (10, 18), (2, 46), (6, 60), (-6, 66, 1), (10, 70), (20, 84), (34, 82), (38, 64), (46, 56),
                        (60, 52)])),
             L(outline([(4, 46), (30, 48), (40, 62), (34, 82), (20, 84), (8, 70)]), 'shade', 'b', False),
             fr([(66, 6), (88, 22), (92, 46), (88, 56, 1), (80, 40), (70, 30)])],
    'back': [L(outline([(16, 78), (8, 64), (-4, 60, 1), (6, 52), (6, 28), (22, 8), (50, 0), (78, 8), (94, 28), (94, 52), (104, 60, 1), (92, 64), (84, 78), (66, 86), (50, 88),
                        (34, 86)])),
             L(outline([(58, 2), (80, 10), (94, 30), (100, 58), (84, 78), (62, 86)]), 'shade', 'b', False)],
})

# Harvey Lifter: piel morena; pelo melocotón claro en pinchos revueltos que se abren a los lados, con un mechón en punta
# que baja por la frente; ojos pequeños de enfado y una mueca de labios gruesos
C('harvey-lifter', {
    'body': 'normal', 'pal': pal('#f4ccae', '#b08050', shade='#dcae8e', deep='#bc8e6e', light='#fce6d6', lips='#8a4a2e'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'none', 'nose': (50, 86, 2.8),
             'hairline': [(16, 66), (18, 50), (30, 44), (44, 46), (50, 60), (56, 46), (70, 44), (82, 50), (84, 66)]},
    'front': messy('front', amp=14, n=13, seed=77, rx=48, ry=40, cy=40, lo=66)
             + [L(outline([(38, 92), (50, 89), (62, 92), (60, 99), (50, 100), (40, 99)]), 'lips', 'f', ln=True),
                L(outline([(42, 93.5), (58, 93.5), (56, 97), (44, 97)]), (60, 24, 16, 255), 'f', False)],
    'side': messy('side', amp=14, n=12, seed=77, nape=86) + [L(ell(86, 96, 3, 3.4), 'lips', 'f', ln=True)],
    'back': messy('back', amp=14, n=13, seed=77, nape=86),
})

# Harvey Sweats: piel tostada y orejas grandes; pelo rubio crema corto en pinchos tiesos hacia arriba, con el flequillo
# en picos; ojos rojos afilados de pillo y media sonrisa
C('harvey-sweats', {
    'body': 'normal', 'pal': pal('#f6e2b8', '#c08a58', iris='#b02a1e', shade='#dcc494', deep='#bca474', light='#fef4de'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'big_ears': 2, 'ear_out': 2, 'nose': (50, 86, 2.8),
             'hairline': [(16, 62), (20, 50), (26, 58), (32, 48), (40, 58), (48, 48), (56, 58), (64, 48), (72, 58), (78, 50), (84, 62)]},
    'front': [L(outline([(17, 64), (12, 40), (16, 14), (30, 6), (34, -12, 1), (44, 2), (52, -20, 1), (58, 0), (68, -10, 1), (70, 6), (84, 14), (88, 40), (83, 64), (78, 48),
                         (22, 48)])),
              L(outline([(58, 0), (68, -6), (70, 8), (84, 16), (88, 40), (84, 58), (76, 30)]), 'shade', 'b', False)],
    'side': [L(outline([(72, 48), (82, 42), (86, 20), (74, 4), (66, -10, 1), (56, 2), (48, -18, 1), (40, 4), (24, 6), (8, 20), (4, 46), (10, 70), (22, 82), (34, 80), (38, 64),
                        (46, 54), (60, 50)])),
             L(outline([(5, 44), (30, 48), (40, 62), (34, 80), (22, 82), (10, 70)]), 'shade', 'b', False)],
    'back': [L(outline([(17, 74), (12, 40), (16, 14), (30, 6), (34, -12, 1), (44, 2), (52, -18, 1), (58, 0), (68, -10, 1), (70, 6), (84, 14), (88, 40), (83, 74), (66, 82),
                        (50, 84), (34, 82)])),
             L(outline([(56, 2), (68, -6), (70, 8), (84, 16), (88, 42), (83, 74), (62, 82)]), 'shade', 'b', False)],
})

# Healey Proctor: piel tostada y cara larga; pelo amarillo pálido en una mata de pinchos largos echados hacia arriba y a un
# lado, con el flequillo en picos; ojos blancos de pupila pequeña, ceño fruncido y los dientes apretados
C('healey-proctor', {
    'body': 'delgado', 'pal': pal('#e4dc9e', '#c08a58', shade='#c8c07e', deep='#a8a05e', light='#f4f0cc'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 99, 'face_front': LONG_FACE, 'eye_y': 75,
             'hairline': [(16, 60), (20, 48), (26, 56), (32, 46), (40, 56), (48, 46), (56, 56), (64, 46), (72, 56), (78, 48), (84, 60)]},
    'front': [L(outline([(17, 62), (10, 46), (-8, 40, 1), (6, 30), (0, 10, 1), (18, 12), (16, -14, 1), (34, 0), (44, -34, 1), (54, -6), (72, -30, 1), (70, -2), (94, -10, 1),
                         (84, 12), (104, 18, 1), (90, 32), (100, 44, 1), (86, 46), (83, 62), (78, 46), (22, 46)])),
              L(outline([(56, -6), (72, -26), (70, 0), (90, -6), (82, 14), (98, 20), (88, 34), (94, 42), (84, 44), (78, 26)]), 'shade', 'b', False),
              strand([(36, 4), (40, 32)], 'deep', 'b', 1.0), strand([(56, 0), (58, 30)], 'deep', 'b', 1.0)]
             + white_eyes(75, 15, 6, 5, 1.6),
    'side': [L(outline([(72, 46), (84, 40), (98, 30, 1), (86, 22), (100, 4, 1), (80, 6), (84, -18, 1), (64, -4), (58, -32, 1), (46, -2), (26, -16, 1), (24, 6), (6, 4, 1),
                        (10, 20), (-6, 30, 1), (6, 40), (4, 56), (10, 72), (22, 84), (34, 82), (38, 64), (46, 52), (60, 48)])),
             L(outline([(5, 44), (30, 48), (40, 62), (34, 82), (22, 84), (10, 70)]), 'shade', 'b', False)] + side_eye(75),
    'back': [L(outline([(17, 76), (10, 48), (-8, 42, 1), (6, 30), (0, 10, 1), (18, 12), (16, -14, 1), (34, 0), (44, -32, 1), (54, -6), (72, -28, 1), (70, -2), (94, -8, 1),
                        (84, 12), (104, 20, 1), (90, 32), (100, 46, 1), (86, 50), (83, 76), (66, 84), (50, 86), (34, 84)])),
             L(outline([(56, -6), (72, -24), (70, 0), (90, -4), (82, 14), (98, 22), (88, 34), (94, 44), (86, 52), (83, 76), (62, 84)]), 'shade', 'b', False)],
})

# Heath Cover: grandullón de cara ancha y cuello grueso; pelo verde oliva en pinchos revueltos, con un mechón que le cae
# sobre un ojo; ojos blancos redondos de cansancio con ojeras y una raya de boca
C('heath-cover', {
    'body': 'corpulento', 'pal': pal('#5e6226', SKIN, shade='#4a4e1a', deep='#323610', light='#82864a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 97, 'face_front': WIDE_FACE, 'nose': (50, 87, 3.2),
             'hairline': [(14, 64), (18, 50), (30, 44), (44, 46), (56, 42), (70, 46), (82, 50), (86, 64)]},
    'front': messy('front', amp=14, n=12, seed=88, rx=48, ry=40, cy=40, lo=64, sweep=0.3)
             + [fr([(48, 40), (60, 42), (64, 58), (60, 76, 1), (56, 58)])]
             + white_eyes(76, 15, 6.6, 6, 1.8, 0.6)
             + [L(quad((28, 84), (36, 87), (44, 84)), (170, 110, 80, 255), 'f', False, False, 1.0), L(quad((72, 84), (64, 87), (56, 84)), (170, 110, 80, 255), 'f', False, False, 1.0)],
    'side': messy('side', amp=14, n=11, seed=88, nape=86, sweep=0.3) + side_eye(76, 0.6),
    'back': messy('back', amp=14, n=12, seed=88, nape=86, sweep=0.3),
})
