"""Instituto Raimon de Victory Road (vr-ouja-raimon, 王者雷門): sus modelos 3D de Inazuma Eleven: Victory Road
(英雄たちのヴィクトリーロード) en la enciclopedia. Son personajes nuevos de Victory Road; cada uno tiene un solo modelo
(Haru tiene dos, con la misma cabeza). Ningún id coge por prefijo el dibujo de otro."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars_bigwaves import rect_glasses
from heads import quad  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (24, 22, 26, 255)


def fr(pts, c='mid'):
    return L(outline(pts), c, 'f')


def puff(cx, cy, rx, ry, n=7, a0=0.0, k=0.82):
    """Nube de bultos redondos (moños, rizos, pelo de nube)."""
    import math
    pts = []
    for i in range(n * 2):
        a = a0 + math.pi * 2 * i / (n * 2)
        r = 1.0 if i % 2 == 0 else k
        pts.append((cx + rx * r * math.cos(a), cy + ry * r * math.sin(a)))
    return blob(pts, 6)


# Dantouya Kanata (Zander Warmington, portero): piel morena, pelo rosa blanquecino enorme en pinchos que salen en todas
# direcciones, con pinchos que le caen por la frente hasta los ojos; ojos rojos afilados y media sonrisa chulesca
CHARS['zander-warmington'] = {
    'body': 'normal', 'pal': pal('#f2d4d2', '#a86a48', iris='#c42a2a', shade='#d4aaaa', deep='#b48888'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(16, 84), (2, 80, 1), (8, 66), (-10, 56, 1), (4, 46), (-6, 30, 1), (10, 26), (4, 6, 1), (22, 10), (24, -12, 1), (38, 2), (48, -18, 1),
                         (58, 0), (74, -10, 1), (74, 8), (94, 4, 1), (88, 22), (108, 28, 1), (94, 40), (110, 52, 1), (96, 60), (100, 76, 1), (86, 80), (82, 62),
                         (18, 62)])),
              L(outline([(58, 0), (74, -10), (74, 8), (94, 4), (88, 22), (108, 28), (94, 40), (110, 52), (96, 60), (90, 50), (78, 26)]), 'shade', 'b', False),
              fr([(14, 76, 1), (12, 50), (22, 34), (16, 22, 1), (34, 26), (44, 12, 1), (52, 24), (66, 14, 1), (68, 28), (84, 24, 1), (80, 38), (90, 48), (88, 74, 1),
                  (80, 62), (74, 72, 1), (68, 56), (60, 66, 1), (54, 54), (46, 70, 1), (40, 54), (32, 68, 1), (28, 56), (20, 70)]),
              L(outline([(54, 26), (66, 16), (68, 30), (80, 40), (86, 56), (78, 50), (68, 40)]), 'shade', 'f', False),
              strand([(30, 36), (36, 50)], 'deep', 'f', 1.0), strand([(60, 34), (62, 50)], 'deep', 'f', 1.0)],
    'side': [L(outline([(60, 60), (66, 48), (84, 46), (96, 50, 1), (92, 36), (104, 26, 1), (86, 22), (92, 4, 1), (74, 6), (70, -14, 1), (56, 0), (40, -12, 1),
                        (32, 6), (12, 0, 1), (16, 18), (-6, 22, 1), (6, 36), (-12, 48, 1), (4, 56), (-6, 74, 1), (10, 74), (8, 92, 1), (22, 84), (30, 98, 1), (36, 82),
                        (46, 74)])),
             L(outline([(0, 40), (24, 46), (30, 80), (10, 80)]), 'shade', 'b', False),
             fr([(68, 20), (88, 30), (96, 50, 1), (88, 46), (86, 62, 1), (80, 50), (72, 40)])],
    'back': [L(outline([(16, 92), (2, 86, 1), (8, 72), (-10, 60, 1), (4, 50), (-6, 32, 1), (10, 28), (4, 6, 1), (22, 10), (24, -12, 1), (38, 2), (48, -18, 1), (58, 0),
                        (74, -10, 1), (74, 8), (94, 4, 1), (88, 22), (108, 30, 1), (94, 42), (110, 56, 1), (96, 64), (100, 84, 1), (84, 90), (72, 100, 1), (62, 92),
                        (50, 102, 1), (40, 92), (28, 100, 1)])),
             L(outline([(56, 0), (88, 14), (100, 50), (94, 84), (66, 90), (72, 40)]), 'shade', 'b', False),
             strand([(30, 20), (40, 46), (34, 72)], 'deep', 'b', 1.0), strand([(70, 20), (62, 46), (68, 72)], 'deep', 'b', 1.0)],
}

# Shigure Yuusuke (Viorain Maleby): pelo azul marino oscuro en forma de seta enorme y lisa, con un flequillo que le tapa el
# ojo derecho y llega a la barbilla, y mechones lila por dentro a los lados; piel pálida y un ojo azul caído con sombra lila
CHARS['viorain-maleby'] = {
    'body': 'bajito', 'pal': pal('#1e2a5e', '#f8dccc', iris='#3a8ab8', shade='#141c44', deep='#0e1434', lil='#9c9ce6', lid='#a88ac8'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(10, 100), (-4, 76), (-8, 40), (4, 10), (28, -10), (50, -14), (72, -10), (96, 8), (106, 40), (104, 76), (92, 100), (84, 70), (16, 70)])),
              L(outline([(-2, 60), (10, 96), (20, 100), (14, 70)]), 'lil', 'f', False), L(outline([(102, 60), (92, 96), (82, 100), (86, 70)]), 'lil', 'f', False),
              L(outline([(60, -8), (90, 6), (104, 40), (100, 76), (90, 50)]), 'shade', 'b', False),
              fr([(6, 76), (4, 40), (18, 14), (44, 2), (72, 6), (92, 26), (96, 56), (94, 92, 1), (86, 70), (76, 60), (64, 58), (56, 70), (54, 104, 1), (40, 96), (24, 82),
                  (14, 90, 1)]),
              L(outline([(16, 60), (30, 40), (52, 30), (56, 50), (50, 80), (40, 70)]), 'shade', 'f', False),
              strand([(22, 18), (46, 40), (52, 80)], 'deep', 'f', 1.0),
              L(quad((57, 72), (64, 69), (72, 72)), 'lid', 'f', False, False, 2.0)],
    'side': [L(outline([(70, 96), (64, 76), (56, 66), (70, 52), (88, 48), (98, 30), (94, 8), (74, -10), (44, -14), (16, -6), (-2, 16), (-8, 48), (-4, 80), (8, 98),
                        (30, 102), (46, 96)])),
             L(outline([(-4, 50), (24, 56), (40, 96), (8, 98), (-2, 80)]), 'shade', 'b', False),
             fr([(70, 2), (94, 18), (98, 48), (92, 82), (82, 96, 1), (80, 70), (74, 48), (64, 30)])],
    'back': [L(outline([(10, 100), (-4, 76), (-8, 40), (4, 10), (28, -10), (50, -14), (72, -10), (96, 8), (106, 40), (104, 76), (92, 100), (72, 106), (50, 102),
                        (28, 106)])),
             L(outline([(-2, 60), (40, 70), (60, 70), (102, 60), (92, 100), (72, 106), (50, 102), (28, 106), (10, 100)]), 'shade', 'b', False),
             strand([(30, 0), (60, 40), (96, 50)], 'deep', 'b', 1.0)],
}

# Tenguuji Rei (Clement Mariner): piel tostada con pecas; pelo turquesa recogido arriba en una nube de bultos ancha como
# un sombrero, y dos mechones lisos larguísimos a los lados de la cara hasta el pecho; cejas gruesas verde menta, ojos
# marrones con sombra menta, nariz roja y sonrisa
CHARS['clement-mariner'] = {
    'body': 'delgado', 'pal': pal('#36aeb0', '#d08a5a', iris='#6a3a24', shade='#24868a', deep='#1a6466', mint='#98e6b4', nose='#c85a3a', freckle='#a86038'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False, 'nose': (50, 85, 2.2)},
    'front': [L(outline([(10, 118), (4, 80), (8, 46), (24, 30), (40, 28), (60, 28), (76, 30), (92, 46), (96, 80), (90, 118), (82, 118), (82, 60), (18, 60),
                         (18, 118)])),
              L(puff(8, 30, 20, 13, 5, 0.3)), L(puff(92, 30, 20, 13, 5, 0.6)), L(puff(50, 16, 34, 22, 7, 0.2)),
              L(ell(58, 6, 12, 5), 'light', 'b', False),
              L(outline([(76, 34), (90, 44), (94, 80), (90, 116), (84, 116), (84, 60)]), 'shade', 'b', False),
              fr([(12, 116), (10, 64), (16, 46), (30, 38), (38, 48), (26, 54), (22, 70), (22, 116)]),
              fr([(88, 116), (90, 64), (84, 46), (70, 38), (62, 48), (74, 54), (78, 70), (78, 116)]),
              L(outline([(28, 64), (34, 58), (44, 62), (42, 66), (34, 64)]), 'mint', 'f', ln=True),
              L(outline([(72, 64), (66, 58), (56, 62), (58, 66), (66, 64)]), 'mint', 'f', ln=True),
              L(ell(28, 86, 0.9, 0.9), 'freckle', 'f', False), L(ell(32, 89, 0.9, 0.9), 'freckle', 'f', False), L(ell(26, 90, 0.9, 0.9), 'freckle', 'f', False),
              L(ell(72, 86, 0.9, 0.9), 'freckle', 'f', False), L(ell(68, 89, 0.9, 0.9), 'freckle', 'f', False), L(ell(74, 90, 0.9, 0.9), 'freckle', 'f', False)],
    'side': [L(outline([(58, 56), (66, 42), (82, 40), (86, 30), (70, 24), (40, 22), (16, 34), (4, 60), (-6, 100), (-14, 130), (0, 132), (10, 104), (24, 80),
                        (40, 64), (50, 60)])),
             L(puff(42, 18, 42, 20, 7, 0.3)), L(puff(78, 14, 22, 14, 5, 0.5)), L(ell(52, 4, 14, 5), 'light', 'b', False),
             L(outline([(4, 64), (20, 74), (6, 110), (-8, 128)]), 'shade', 'b', False),
             L(outline([(70, 60), (78, 58), (84, 62), (80, 64)]), 'mint', 'f', ln=True)],
    'back': [L(outline([(14, 100), (10, 60), (16, 34), (50, 26), (84, 34), (90, 60), (86, 100), (80, 130), (64, 132), (50, 120), (36, 132), (20, 130)])),
             L(puff(8, 30, 20, 13, 5, 0.3)), L(puff(92, 30, 20, 13, 5, 0.6)), L(puff(50, 18, 38, 22, 7, 0.2)),
             L(outline([(50, 40), (84, 40), (88, 100), (80, 130), (64, 132), (54, 100)]), 'shade', 'b', False),
             strand([(36, 50), (34, 110)], 'deep', 'b', 1.0), strand([(64, 50), (66, 110)], 'deep', 'b', 1.0)],
}

# Toono Zenya (Boone Wretman): pelo gris verdoso azulado en un tupé grande peinado hacia su izquierda (la derecha de la
# imagen) que cae por ese lado en un mechón curvado; gafas negras de pasta gruesa; cejas gordas del color del pelo
CHARS['boone-wretman'] = {
    'body': 'normal', 'pal': pal('#5eaaaa', '#fcd8c0', iris='#4a4a7a', shade='#3e7e80', deep='#2c5c5e', brow='#5eaaaa'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'line', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(14, 76), (8, 40), (14, 12), (34, -6), (56, -10), (78, -2), (94, 18), (100, 44), (96, 70), (104, 84, 1), (88, 80), (84, 60), (18, 60)])),
              L(outline([(62, -6), (86, 8), (98, 40), (94, 70), (84, 50)]), 'shade', 'b', False),
              fr([(12, 74), (12, 44), (22, 22), (44, 12), (70, 14), (90, 28), (96, 52), (92, 70), (100, 84, 1), (84, 76), (82, 56), (72, 44), (54, 40), (40, 46),
                  (30, 56), (22, 70)]),
              L(outline([(56, 18), (80, 26), (92, 48), (84, 52), (72, 36)]), 'shade', 'f', False),
              strand([(24, 30), (48, 20), (74, 30)], 'deep', 'f', 1.0), strand([(30, 44), (52, 32), (78, 42)], 'deep', 'f', 1.0),
              L(outline([(29, 62), (36, 59), (43, 62), (42, 65), (30, 65)]), 'brow', 'f', ln=True),
              L(outline([(71, 62), (64, 59), (57, 62), (58, 65), (70, 65)]), 'brow', 'f', ln=True),
              L(outline([(22, 69), (46, 69), (45, 81), (24, 81)]) + [(22, 69)], BLACK, 'f', False, False, 3.6),
              L(outline([(78, 69), (54, 69), (55, 81), (76, 81)]) + [(78, 69)], BLACK, 'f', False, False, 3.6),
              L([(46, 72), (54, 72)], BLACK, 'f', False, False, 2.6)],
    'side': [L(outline([(58, 62), (62, 48), (84, 44), (98, 30), (96, 6), (78, -8), (48, -12), (20, -4), (2, 16), (-2, 44), (6, 66), (22, 72), (38, 66), (48, 62)])),
             L(outline([(0, 30), (30, 36), (40, 64), (22, 72), (6, 66)]), 'shade', 'b', False),
             strand([(10, 10), (50, 4), (90, 14)], 'deep', 'b', 1.0), strand([(6, 26), (44, 22), (84, 30)], 'deep', 'b', 1.0),
             L([(76, 68), (90, 68), (89, 80), (77, 80), (76, 68)], BLACK, 'f', False, False, 3.6), L([(50, 70), (76, 70)], BLACK, 'f', False, False, 2.6),
             L(outline([(72, 62), (80, 60), (86, 63), (80, 65)]), 'brow', 'f', ln=True)],
    'back': [L(outline([(18, 86), (8, 50), (12, 16), (32, -6), (56, -10), (80, -2), (94, 18), (98, 50), (86, 86), (70, 92), (50, 94), (30, 92)])),
             L(outline([(10, 40), (50, 30), (96, 40), (86, 86), (70, 92), (50, 94), (30, 92), (18, 86)]), 'shade', 'b', False),
             strand([(20, 20), (50, 10), (84, 20)], 'deep', 'b', 1.0), strand([(30, 60), (40, 88)], 'deep', 'b', 1.0), strand([(70, 60), (60, 88)], 'deep', 'b', 1.0)],
}

# Akasode Matsuri (Jazmine Carmine): pelo blanco plateado con raya en medio (marcada en rojo arriba) que cae a los lados de
# la cara y se enrolla en dos aros grandes a la altura de las orejas, con mechones finos que le llegan al pecho y una
# coletita en la nuca; ojos grises tranquilos
CHARS['jazmine-carmine'] = {
    'body': 'chica', 'pal': pal('#e8e8ee', '#fcdcc8', iris='#8a8a98', shade='#bcbcc8', deep='#9a9aa8', red='#d03a3a'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'line', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(12, 70), (8, 40), (18, 14), (40, 0), (60, 0), (82, 14), (92, 40), (88, 70), (80, 60), (20, 60)])),
              L(puff(4, 76, 15, 14, 4, 0.4, 0.95)), L(puff(96, 76, 15, 14, 4, 0.9, 0.95)),
              L(ell(4, 78, 7, 6), 'shade', 'b', False), L(ell(96, 78, 7, 6), 'shade', 'b', False),
              L(outline([(60, 2), (82, 14), (92, 40), (88, 64), (78, 40)]), 'shade', 'b', False),
              fr([(14, 72), (12, 42), (24, 20), (48, 10), (40, 28), (30, 46), (24, 70)]), fr([(86, 72), (88, 42), (76, 20), (52, 10), (60, 28), (70, 46), (76, 70)]),
              L(rope((22, 66), (18, 100), (20, 126), 3.6), 'mid', 'f'), L(rope((78, 66), (82, 100), (80, 126), 3.6), 'mid', 'f'),
              L([(50, 2), (50, 14)], 'red', 'f', False, False, 1.6), L([(50, 8), (56, 8)], 'red', 'f', False, False, 1.6)],
    'side': [L(outline([(60, 56), (66, 44), (80, 42), (88, 30), (80, 10), (56, 0), (30, 4), (12, 20), (8, 44), (14, 64), (30, 68), (46, 60)])),
             L(puff(30, 74, 16, 15, 4, 0.4, 0.95)), L(ell(30, 76, 7, 7), 'shade', 'b', False),
             L(outline([(10, 30), (30, 34), (38, 56), (20, 64)]), 'shade', 'b', False),
             L(rope((68, 52), (74, 90), (70, 122), 3.6), 'mid', 'f')],
    'back': [L(outline([(14, 74), (8, 40), (18, 14), (40, 0), (60, 0), (82, 14), (92, 40), (86, 74), (50, 84)])),
             L(puff(2, 74, 16, 15, 4, 0.4, 0.95)), L(puff(98, 74, 16, 15, 4, 0.9, 0.95)),
             L(ell(2, 76, 7, 6), 'shade', 'b', False), L(ell(98, 76, 7, 6), 'shade', 'b', False),
             L(outline([(56, 2), (82, 14), (92, 40), (86, 70), (60, 50)]), 'shade', 'b', False),
             L(rope((50, 80), (46, 96), (50, 112), 4.4), 'mid', 'f'), L(ell(50, 82, 2.6, 2.2), OUTC, 'f', False)],
}

# Kido Satoru (Colton Sharps): pelo negro revuelto en mechones de punta, que se abren a los lados a la altura de las
# orejas y caen en puntas por la nuca; flequillo de puntas sobre la frente; cejas gruesas, ojos verdes grandes y sonrisa
CHARS['colton-sharps'] = {
    'body': 'bajito', 'pal': pal('#1c1c22', '#fcd8b8', iris='#6a8a2a', shade='#101014', deep='#2e2e38', light='#3a3a46'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(16, 96), (8, 86, 1), (10, 78), (-8, 80, 1), (4, 66), (-4, 54, 1), (8, 46), (6, 24), (20, 6), (30, -8, 1), (44, 0), (56, -12, 1), (62, 0),
                         (82, 4), (94, 22), (94, 46), (106, 54, 1), (96, 66), (108, 80, 1), (90, 78), (92, 88, 1), (84, 96), (82, 62), (18, 62)])),
              L(outline([(62, 0), (82, 4), (94, 22), (94, 46), (106, 54), (96, 66), (88, 56)]), 'shade', 'b', False),
              fr([(14, 72), (10, 50), (16, 30), (34, 16), (56, 14), (76, 20), (88, 34), (90, 56), (86, 74, 1), (80, 58), (72, 66, 1), (68, 50), (58, 60, 1), (52, 46),
                  (44, 62, 1), (38, 48), (28, 62, 1), (24, 52), (18, 68)]),
              strand([(30, 26), (40, 40)], 'light', 'f', 1.0), strand([(60, 22), (62, 40)], 'light', 'f', 1.0)],
    'side': [L(outline([(62, 58), (66, 46), (82, 44), (92, 30), (96, 16, 1), (84, 14), (80, -2, 1), (66, 6), (54, -10, 1), (42, 4), (20, 0, 1), (16, 14), (-4, 20, 1),
                        (6, 32), (-10, 46, 1), (4, 52), (-8, 68, 1), (6, 70), (0, 88, 1), (14, 82), (14, 100, 1), (24, 88), (30, 104, 1), (36, 86), (46, 74)])),
             L(outline([(2, 36), (24, 42), (32, 82), (10, 82)]), 'shade', 'b', False),
             fr([(68, 14), (88, 24), (94, 44, 1), (86, 40), (84, 56, 1), (78, 44), (70, 36)])],
    'back': [L(outline([(16, 100), (8, 90, 1), (10, 82), (-8, 82, 1), (4, 68), (-4, 56, 1), (8, 48), (6, 24), (20, 6), (30, -8, 1), (44, 0), (56, -12, 1), (62, 0),
                        (82, 4), (94, 22), (94, 48), (106, 56, 1), (96, 68), (108, 82, 1), (90, 82), (92, 92, 1), (80, 96), (70, 108, 1), (62, 96), (52, 110, 1),
                        (42, 96), (30, 108, 1), (24, 96)])),
             L(outline([(56, 0), (84, 8), (96, 46), (92, 90), (64, 96), (70, 50)]), 'shade', 'b', False),
             strand([(30, 20), (36, 50), (30, 80)], 'deep', 'b', 1.0), strand([(70, 20), (64, 50), (70, 80)], 'deep', 'b', 1.0)],
}

# Arashi Daisuke (Maddock Jackson): pelo granate en una corona alta de pinchos gruesos hacia arriba, sujeto con una cinta
# negra en la frente; ojos turquesa enfadados con arrugas en el entrecejo y la nariz, boca apretada
CHARS['maddock-jackson'] = {
    'body': 'normal', 'pal': pal('#6e1e30', '#fcd4b0', iris='#3aa8a8', shade='#521424', deep='#3c0e1a', band='#1c1a1e', wr='#b07a5a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(14, 60), (-2, 52, 1), (6, 36), (-8, 18, 1), (10, 14), (8, -8, 1), (26, 0), (32, -18, 1), (44, -4), (52, -22, 1), (60, -4), (72, -16, 1),
                         (76, 2), (94, -6, 1), (90, 14), (108, 18, 1), (94, 36), (102, 52, 1), (86, 60), (80, 56), (20, 56)])),
              L(outline([(60, -4), (72, -16), (76, 2), (94, -6), (90, 14), (108, 18), (94, 36), (102, 52), (86, 56), (80, 30)]), 'shade', 'b', False),
              strand([(30, 10), (36, 40)], 'deep', 'b', 1.0), strand([(50, 0), (50, 36)], 'deep', 'b', 1.0), strand([(70, 10), (64, 40)], 'deep', 'b', 1.0),
              L(quad((12, 62), (50, 52), (88, 62)), 'band', 'f', False, False, 6.0),
              L([(44, 66), (47, 70)], 'wr', 'f', False, False, 0.9), L([(56, 66), (53, 70)], 'wr', 'f', False, False, 0.9),
              L([(45, 84), (48, 86)], 'wr', 'f', False, False, 0.8), L([(55, 84), (52, 86)], 'wr', 'f', False, False, 0.8)],
    'side': [L(outline([(70, 52), (88, 46), (100, 40, 1), (92, 28), (104, 12, 1), (86, 8), (88, -12, 1), (70, -2), (62, -22, 1), (50, -2), (32, -16, 1), (28, 4),
                        (8, 0, 1), (12, 20), (-6, 30, 1), (8, 40), (4, 60), (18, 76), (34, 72), (40, 58), (56, 54)])),
             L(outline([(4, 40), (30, 44), (36, 70), (18, 76), (4, 60)]), 'shade', 'b', False),
             L(quad((86, 54), (50, 38), (8, 50)), 'band', 'f', False, False, 6.0)],
    'back': [L(outline([(16, 80), (10, 60), (-2, 52, 1), (6, 36), (-8, 18, 1), (10, 14), (8, -8, 1), (26, 0), (32, -18, 1), (44, -4), (52, -22, 1), (60, -4),
                        (72, -16, 1), (76, 2), (94, -6, 1), (90, 14), (108, 18, 1), (94, 36), (102, 52, 1), (90, 60), (84, 80), (50, 86)])),
             L(outline([(56, -4), (90, 14), (100, 50), (84, 80), (64, 84), (70, 40)]), 'shade', 'b', False),
             L(quad((8, 56), (50, 44), (92, 56)), 'band', 'f', False, False, 6.0),
             strand([(30, 10), (36, 40)], 'deep', 'b', 1.0), strand([(70, 10), (64, 40)], 'deep', 'b', 1.0)],
}

# Hoshimura Nao (Eleanor Estrella): pelo turquesa claro en una campana corta y ahuecada con las puntas crema por dentro,
# un rizo en forma de luna creciente sobre la frente y dos mechones finos con la punta crema a los lados; ojos grandes
# azul oscuro con pestañas y sonrisa
CHARS['eleanor-estrella'] = {
    'body': 'chica', 'pal': pal('#5edcd0', '#fcdcc4', iris='#1e3a7a', shade='#3eb0a8', deep='#2a8a84', cream='#f6eec0'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(8, 90), (-6, 92, 1), (2, 70), (6, 40), (18, 12), (40, -2), (60, -2), (82, 12), (94, 40), (98, 70), (106, 92, 1), (92, 90), (82, 62),
                         (18, 62)])),
              L(outline([(-6, 92), (2, 76), (16, 74), (18, 86), (8, 90)]), 'cream', 'f', False), L(outline([(106, 92), (98, 76), (84, 74), (82, 86), (92, 90)]), 'cream', 'f', False),
              L(outline([(62, 0), (84, 14), (96, 46), (96, 72), (84, 50)]), 'shade', 'b', False),
              fr([(14, 76), (12, 50), (20, 30), (40, 18), (62, 18), (80, 28), (88, 48), (88, 76), (78, 62), (70, 54), (56, 52), (40, 56), (28, 62)]),
              L(outline([(30, 50), (32, 38), (44, 30), (56, 32), (54, 38), (44, 38), (36, 46)]), 'cream', 'f', ln=True),
              L(rope((20, 70), (18, 92), (22, 108), 2.6), 'mid', 'f'), L(rope((80, 70), (82, 92), (78, 108), 2.6), 'mid', 'f'),
              L(ell(22, 108, 2.2, 3), 'cream', 'f'), L(ell(78, 108, 2.2, 3), 'cream', 'f'),
              L(quad((28, 70), (36, 64), (44, 69)), OUTC, 'f', False, False, 1.6), L(quad((72, 70), (64, 64), (56, 69)), OUTC, 'f', False, False, 1.6)],
    'side': [L(outline([(62, 60), (70, 50), (86, 46), (92, 30), (82, 8), (56, -4), (30, 0), (12, 16), (4, 40), (2, 70), (-10, 94, 1), (10, 90), (30, 96, 1), (36, 80),
                        (46, 68)])),
             L(outline([(-10, 94), (0, 76), (36, 80), (30, 96), (10, 90)]), 'cream', 'b', False),
             L(outline([(6, 30), (30, 36), (36, 70), (10, 72)]), 'shade', 'b', False),
             L(rope((58, 60), (60, 90), (58, 106), 2.6), 'mid', 'f'), L(ell(58, 106, 2.2, 3), 'cream', 'f')],
    'back': [L(outline([(8, 94), (-6, 96, 1), (2, 70), (6, 40), (18, 12), (40, -2), (60, -2), (82, 12), (94, 40), (98, 70), (106, 96, 1), (92, 94), (70, 100),
                        (50, 96), (30, 100)])),
             L(outline([(-6, 96), (4, 80), (50, 86), (96, 80), (106, 96), (92, 94), (70, 100), (50, 96), (30, 100), (8, 94)]), 'cream', 'b', False),
             L(outline([(56, 0), (84, 14), (98, 46), (96, 76), (60, 70)]), 'shade', 'b', False)],
}

# Tsukikage Ren (Darian Moonward): media melena ondulada verde oliva claro que oscurece a verde hierba en las puntas, con
# raya en medio y mechones que le caen por la frente entre los ojos; ojos verdes con raya gruesa y media sonrisa
CHARS['darian-moonward'] = {
    'body': 'normal', 'pal': pal('#a8c050', '#fcdcc4', iris='#2a8a6a', shade='#7a9a34', deep='#4a8a2a', low='#6a9a34'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(12, 96), (2, 86, 1), (6, 66), (4, 40), (16, 12), (40, -2), (60, -2), (84, 12), (96, 40), (94, 66), (98, 86, 1), (88, 96), (82, 66),
                         (18, 66)])),
              L(outline([(4, 70), (12, 96), (2, 86)]), 'low', 'f', False), L(outline([(96, 70), (88, 96), (98, 86)]), 'low', 'f', False),
              L(outline([(60, 0), (84, 14), (96, 44), (92, 80), (82, 56)]), 'shade', 'b', False),
              fr([(10, 84), (8, 50), (18, 24), (40, 10), (50, 14), (60, 10), (82, 24), (92, 50), (90, 84, 1), (82, 66), (72, 50), (62, 54), (56, 72, 1), (52, 54),
                  (48, 54), (44, 72, 1), (38, 54), (28, 50), (18, 66)]),
              L(outline([(10, 70), (18, 66), (10, 84)]), 'low', 'f', False), L(outline([(90, 70), (82, 66), (90, 84)]), 'low', 'f', False),
              strand([(50, 14), (46, 30), (40, 50)], 'deep', 'f', 1.0), strand([(50, 14), (56, 30), (62, 50)], 'deep', 'f', 1.0)],
    'side': [L(outline([(60, 66), (66, 52), (84, 48), (94, 32), (88, 10), (64, -4), (36, -4), (12, 10), (0, 36), (0, 70), (6, 94, 1), (20, 88), (30, 98, 1),
                        (40, 84), (50, 74)])),
             L(outline([(0, 60), (40, 74), (40, 84), (30, 98), (20, 88), (6, 94)]), 'low', 'b', False),
             L(outline([(4, 30), (28, 36), (36, 70), (8, 66)]), 'shade', 'b', False),
             fr([(66, 6), (90, 20), (96, 46), (92, 66, 1), (84, 50), (74, 40)])],
    'back': [L(outline([(12, 96), (2, 86, 1), (6, 66), (4, 40), (16, 12), (40, -2), (60, -2), (84, 12), (96, 40), (94, 66), (98, 86, 1), (88, 96), (70, 102),
                        (50, 98), (30, 102)])),
             L(outline([(4, 60), (50, 70), (96, 60), (98, 86), (88, 96), (70, 102), (50, 98), (30, 102), (12, 96), (2, 86)]), 'low', 'b', False),
             L(outline([(56, 0), (84, 14), (96, 46), (90, 60), (66, 56)]), 'shade', 'b', False)],
}

# Endou Haru (Harper Evans, protagonista): pelo castaño en pinchos gruesos de punta, con un pincho alto arriba y dos a los
# lados, y un flequillo de mechones en punta sobre la frente; ojos castaños grandes, sonrisa y su bufanda roja al cuello
CHARS['harper-evans'] = {
    'body': 'normal', 'pal': pal('#6a3e24', '#fcd8b8', iris='#4a2a18', shade='#4e2c18', deep='#3a2012', scarf='#e8401e', scarf_d='#b42a10'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(16, 74), (8, 56), (-6, 30, 1), (14, 26), (20, 8), (38, 0), (48, -6), (58, -26, 1), (60, -4), (80, 6), (88, 24), (108, 28, 1), (92, 56),
                         (84, 74), (82, 62), (18, 62)])),
              L(outline([(60, -4), (80, 6), (88, 24), (108, 28), (92, 56), (86, 40), (72, 20)]), 'shade', 'b', False),
              fr([(16, 72, 1), (12, 48), (22, 28), (40, 18), (60, 18), (78, 26), (88, 46), (84, 72, 1), (76, 56), (68, 66, 1), (64, 50), (56, 62, 1), (52, 46),
                  (44, 66, 1), (40, 48), (30, 62, 1), (26, 50), (20, 64)]),
              L(outline([(56, 22), (74, 28), (84, 44), (76, 52), (68, 38)]), 'shade', 'f', False),
              strand([(38, 24), (44, 44)], 'deep', 'f', 1.0), strand([(62, 24), (60, 44)], 'deep', 'f', 1.0),
              L(outline([(24, 100), (50, 106), (76, 100), (80, 112), (50, 118), (20, 112)]), 'scarf', 'f', ln=True)],
    'side': [L(outline([(62, 60), (66, 48), (82, 46), (96, 40, 1), (90, 26), (98, 10, 1), (80, 10), (74, -24, 1), (62, -2), (40, -4), (14, 4, 1), (16, 18), (-6, 28, 1),
                        (8, 38), (2, 58), (14, 74), (32, 72), (44, 62)])),
             L(outline([(4, 38), (26, 44), (32, 70), (14, 74), (2, 58)]), 'shade', 'b', False),
             fr([(68, 16), (88, 26), (94, 44, 1), (86, 40), (82, 56, 1), (76, 42), (70, 34)]),
             L(outline([(40, 100), (70, 104), (84, 100), (84, 114), (60, 118), (34, 112)]), 'scarf', 'f', ln=True)],
    'back': [L(outline([(18, 86), (8, 58), (-6, 30, 1), (14, 26), (20, 8), (38, 0), (48, -6), (58, -26, 1), (60, -4), (80, 6), (88, 24), (108, 28, 1), (92, 58),
                        (82, 86), (64, 94), (56, 102, 1), (50, 94), (36, 94)])),
             L(outline([(58, -2), (82, 8), (90, 26), (106, 30), (92, 58), (82, 86), (62, 92), (68, 40)]), 'shade', 'b', False),
             strand([(50, 30), (40, 50), (30, 70)], 'deep', 'b', 1.0), strand([(50, 30), (60, 50), (70, 70)], 'deep', 'b', 1.0),
             L(outline([(18, 102), (50, 108), (82, 102), (82, 114), (50, 120), (18, 114)]), 'scarf', 'f', ln=True)],
}

# Nogami Yuu (Talon Lewis): melena morada lisa hasta los hombros, peinada hacia atrás con un moñito arriba en la coronilla
# y un mechón que le cae por en medio de la cara; piel muy pálida, ojos azul oscuro afilados con ojeras
CHARS['talon-lewis'] = {
    'body': 'delgado', 'pal': pal('#5a3c84', '#fbe6dc', iris='#2a2a5a', shade='#422c64', deep='#30204a', bag='#d8c0c8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 106), (2, 96, 1), (4, 66), (6, 36), (18, 10), (40, -2), (60, -2), (82, 10), (94, 36), (96, 66), (98, 96, 1), (90, 106), (82, 70),
                         (18, 70)])),
              L(outline([(60, 0), (84, 12), (96, 44), (96, 96), (84, 60)]), 'shade', 'b', False),
              fr([(10, 96), (8, 56), (14, 34), (30, 22), (50, 18), (70, 22), (86, 34), (92, 56), (90, 96, 1), (84, 72), (80, 56), (72, 44), (56, 40), (52, 52), (50, 94, 1),
                  (48, 50), (44, 40), (28, 44), (20, 56), (16, 72)]),
              strand([(30, 24), (34, 10)], 'deep', 'f', 1.0), strand([(42, 20), (44, 4)], 'deep', 'f', 1.0), strand([(58, 20), (56, 4)], 'deep', 'f', 1.0),
              strand([(70, 24), (66, 10)], 'deep', 'f', 1.0),
              L(quad((30, 82), (36, 84), (42, 82)), 'bag', 'f', False, False, 1.0), L(quad((58, 82), (64, 84), (70, 82)), 'bag', 'f', False, False, 1.0)],
    'side': [L(outline([(60, 62), (66, 50), (84, 48), (94, 32), (86, 8), (60, -4), (32, -2), (10, 12), (0, 40), (0, 80), (4, 104, 1), (20, 100), (34, 108, 1),
                        (42, 92), (50, 76)])),
             L(puff(12, 0, 11, 9, 4, 0.3)), L(ell(16, 6, 3, 4), 'deep', 'b', False),
             L(outline([(2, 36), (28, 40), (40, 92), (20, 100), (4, 100)]), 'shade', 'b', False),
             strand([(24, 4), (60, 6), (88, 20)], 'deep', 'b', 1.0),
             fr([(70, 10), (90, 22), (96, 46), (94, 82), (88, 96, 1), (84, 66), (78, 46)])],
    'back': [L(outline([(10, 108), (2, 98, 1), (4, 66), (6, 36), (18, 10), (40, -2), (60, -2), (82, 10), (94, 36), (96, 66), (98, 98, 1), (90, 108), (70, 112),
                        (50, 108), (30, 112)])),
             L(puff(50, 4, 11, 9, 4, 0.3)), L(outline([(46, 10), (54, 10), (56, 26), (44, 26)]), 'shade', 'b'),
             L(outline([(56, 0), (84, 14), (96, 46), (96, 96), (64, 100), (70, 50)]), 'shade', 'b', False),
             strand([(36, 30), (30, 70), (28, 104)], 'deep', 'b', 1.0), strand([(64, 30), (70, 70), (72, 104)], 'deep', 'b', 1.0)],
}

# Ebihara Natsuki (Nino Gamberini): pelo rojo en mechones de punta revueltos, con dos antenas largas curvadas arriba y
# puntas a los lados por delante de las orejas; ojos naranja grandes y sonrisa tranquila
CHARS['nino-gamberini'] = {
    'body': 'normal', 'pal': pal('#c8302a', '#fcd8bc', iris='#d8801e', shade='#9a201e', deep='#781814'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(16, 96), (10, 80), (-4, 66, 1), (6, 56), (-6, 40, 1), (8, 30), (2, 12, 1), (20, 12), (26, -4), (44, -6), (36, -26, 1), (52, -10),
                         (62, -30, 1), (64, -6), (82, 4), (98, 0, 1), (90, 20), (104, 34, 1), (94, 46), (106, 60, 1), (92, 66), (90, 84), (84, 96), (82, 66), (18, 66)])),
              L(outline([(64, -6), (82, 4), (98, 0), (90, 20), (104, 34), (94, 46), (106, 60), (92, 66), (86, 50), (76, 24)]), 'shade', 'b', False),
              fr([(14, 74, 1), (10, 50), (20, 30), (40, 18), (62, 18), (80, 28), (90, 50), (86, 74, 1), (78, 56), (70, 68, 1), (66, 50), (56, 62, 1), (52, 46),
                  (42, 66, 1), (38, 48), (28, 62, 1), (24, 50), (18, 64)]),
              L(rope((16, 66), (12, 84), (18, 98), 3.4), 'mid', 'f'), L(rope((84, 66), (88, 84), (82, 98), 3.4), 'mid', 'f'),
              strand([(36, 24), (42, 44)], 'deep', 'f', 1.0), strand([(64, 24), (62, 44)], 'deep', 'f', 1.0)],
    'side': [L(outline([(62, 62), (66, 50), (82, 48), (96, 44, 1), (90, 30), (100, 16, 1), (82, 14), (86, -2, 1), (64, 4), (60, -30, 1), (50, -4), (36, -24, 1),
                        (34, 0), (12, 2, 1), (16, 18), (-6, 26, 1), (8, 38), (-8, 54, 1), (6, 60), (2, 78, 1), (16, 76), (20, 94, 1), (30, 80), (44, 70)])),
             L(outline([(4, 38), (26, 44), (34, 76), (12, 76)]), 'shade', 'b', False),
             fr([(68, 16), (88, 26), (94, 46, 1), (86, 42), (84, 58, 1), (78, 46), (70, 36)]),
             L(rope((62, 60), (64, 82), (60, 98), 3.4), 'mid', 'f')],
    'back': [L(outline([(16, 96), (10, 80), (-4, 68, 1), (6, 58), (-6, 42, 1), (8, 30), (2, 12, 1), (20, 12), (26, -4), (44, -6), (36, -26, 1), (52, -10),
                        (62, -30, 1), (64, -6), (82, 4), (98, 0, 1), (90, 20), (104, 34, 1), (94, 46), (106, 62, 1), (92, 68), (90, 84), (84, 96), (70, 102, 1),
                        (62, 92), (50, 104, 1), (40, 92), (30, 102, 1)])),
             L(outline([(56, -4), (84, 6), (100, 40), (92, 84), (64, 92), (70, 40)]), 'shade', 'b', False),
             strand([(30, 20), (36, 50), (30, 80)], 'deep', 'b', 1.0), strand([(70, 20), (64, 50), (70, 80)], 'deep', 'b', 1.0)],
}

# Tsuyusaki Tae (Hortensia Raintree): pelo azul marino muy oscuro con dos moños redondos arriba a los lados y una coleta
# larga por detrás; flequillo recto cortado a la altura de las cejas; ojos azul claro grandes con un lunar debajo de cada
# uno, colorete y cejas cortas enfadadas
CHARS['hortensia-raintree'] = {
    'body': 'chica', 'pal': pal('#1e2a4a', '#fcdcc4', iris='#4aa0e0', shade='#141c34', deep='#0e1426', blush='#f4a8a0'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'hairline': False},
    'front': [L(puff(10, 14, 16, 15, 5, 0.3)), L(puff(90, 14, 16, 15, 5, 0.7)),
              L(outline([(12, 96), (6, 60), (10, 30), (26, 10), (50, 4), (74, 10), (90, 30), (94, 60), (88, 96), (82, 62), (18, 62)])),
              L(outline([(60, 6), (84, 18), (94, 50), (88, 92), (82, 56)]), 'shade', 'b', False),
              fr([(14, 82), (12, 50), (20, 30), (40, 20), (60, 20), (80, 30), (88, 50), (86, 82), (80, 64), (74, 62), (68, 66, 1), (64, 60), (52, 62), (48, 66, 1),
                  (44, 60), (34, 62), (30, 66, 1), (26, 62), (20, 64)]),
              L(ell(29, 84, 1.3, 1.3), OUTC, 'f', False), L(ell(71, 84, 1.3, 1.3), OUTC, 'f', False),
              L(ell(28, 90, 4, 2.2), 'blush', 'f', False), L(ell(72, 90, 4, 2.2), 'blush', 'f', False)],
    'side': [L(rope((26, 30), (-6, 60), (-20, 110), 9), 'mid', 'b'),
             L(outline([(60, 62), (66, 50), (86, 48), (94, 30), (84, 8), (56, -2), (30, 2), (10, 20), (4, 50), (8, 80), (24, 92), (40, 84), (50, 70)])),
             L(puff(30, 4, 16, 14, 5, 0.3)), L(puff(56, -4, 13, 11, 4, 0.5)),
             L(outline([(6, 40), (28, 44), (36, 80), (14, 84)]), 'shade', 'b', False),
             fr([(66, 8), (90, 20), (96, 46), (92, 66, 1), (86, 62), (80, 66, 1), (76, 44)]),
             L(ell(76, 90, 3.6, 2.2), 'blush', 'f', False)],
    'back': [L(rope((50, 50), (48, 90), (52, 124), 9), 'mid', 'b'),
             L(outline([(12, 90), (6, 56), (10, 28), (26, 10), (50, 4), (74, 10), (90, 28), (94, 56), (88, 90), (70, 96), (50, 92), (30, 96)])),
             L(puff(10, 14, 16, 15, 5, 0.3)), L(puff(90, 14, 16, 15, 5, 0.7)),
             L(outline([(56, 6), (84, 18), (94, 50), (88, 88), (64, 92), (70, 50)]), 'shade', 'b', False)],
}

# Abuku Michiya (Milan McGrath): pelo azul petróleo oscuro en una media melena lisa y redonda, con el flequillo peinado en
# diagonal hacia su derecha (la izquierda de la imagen) tapando la frente; ojos verdes y sonrisa amable
CHARS['milan-mcgrath'] = {
    'body': 'normal', 'pal': pal('#1e4a60', '#fcdcc4', iris='#3a9a6a', shade='#143648', deep='#0e2634'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(12, 96), (2, 92, 1), (6, 66), (4, 36), (16, 10), (40, -4), (60, -4), (84, 10), (96, 36), (94, 66), (98, 92, 1), (88, 96), (82, 64),
                         (18, 64)])),
              L(outline([(60, -2), (84, 12), (96, 44), (94, 90), (82, 56)]), 'shade', 'b', False),
              fr([(10, 86), (8, 50), (16, 26), (40, 10), (64, 10), (84, 24), (92, 50), (90, 86, 1), (82, 64), (76, 52), (66, 50), (56, 54), (44, 62), (34, 70, 1),
                  (36, 58), (26, 60), (18, 72)]),
              strand([(70, 16), (50, 36), (36, 60)], 'deep', 'f', 1.0), strand([(84, 30), (66, 44)], 'deep', 'f', 1.0)],
    'side': [L(outline([(60, 64), (66, 52), (84, 48), (94, 32), (88, 8), (62, -6), (34, -4), (10, 10), (0, 38), (2, 72), (8, 96, 1), (24, 92), (36, 98, 1), (42, 82),
                        (50, 72)])),
             L(outline([(2, 36), (28, 40), (40, 82), (24, 92), (8, 92)]), 'shade', 'b', False),
             fr([(66, 6), (90, 18), (96, 44), (92, 60, 1), (84, 52), (76, 40)])],
    'back': [L(outline([(12, 96), (2, 92, 1), (6, 66), (4, 36), (16, 10), (40, -4), (60, -4), (84, 10), (96, 36), (94, 66), (98, 92, 1), (88, 96), (70, 100),
                        (50, 96), (30, 100)])),
             L(outline([(56, -2), (84, 12), (96, 46), (94, 90), (64, 96), (70, 50)]), 'shade', 'b', False),
             strand([(36, 20), (30, 60), (30, 94)], 'deep', 'b', 1.0)],
}

# Kasuga Reo (Kaeo Springfield): pelo rosa con un pelo de antena curvado arriba, un flequillo largo de mechones en punta
# que le tapa el ojo izquierdo (derecha de la imagen) y mechones finos a los lados hasta la barbilla; coleta fina y
# larga por detrás; piel pálida, ojos amarillos caídos
CHARS['kaeo-springfield'] = {
    'body': 'delgado', 'pal': pal('#dca2d2', '#fbe6dc', iris='#c8b81e', shade='#b880ae', deep='#98608c'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(14, 74), (8, 40), (18, 12), (40, 0), (60, 0), (82, 12), (92, 40), (90, 66), (82, 62), (18, 62)])),
              L(rope((48, 2), (54, -24), (76, -20), 2.6), 'mid', 'b'),
              L(outline([(60, 2), (82, 14), (92, 44), (88, 64), (80, 40)]), 'shade', 'b', False),
              fr([(14, 66), (10, 44), (20, 22), (44, 12), (66, 16), (86, 30), (100, 54), (104, 76, 1), (90, 62), (84, 78), (80, 96, 1), (74, 76), (70, 86, 1), (64, 66),
                  (54, 56), (46, 50), (36, 52), (26, 60)]),
              L(rope((14, 60), (10, 90), (16, 108), 3.0), 'mid', 'f'),
              L(outline([(56, 22), (80, 32), (94, 54), (84, 60), (70, 44)]), 'shade', 'f', False),
              strand([(48, 14), (66, 40), (76, 80)], 'deep', 'f', 1.0)],
    'side': [L(outline([(60, 58), (66, 46), (84, 44), (94, 30), (86, 8), (60, -2), (32, 2), (12, 18), (6, 44), (12, 64), (30, 70), (46, 62)])),
             L(rope((40, 0), (50, -26), (70, -22), 2.6), 'mid', 'b'),
             L(rope((14, 56), (4, 90), (8, 128), 3.0), 'mid', 'b'),
             L(outline([(8, 30), (30, 36), (36, 62), (14, 64)]), 'shade', 'b', False),
             fr([(66, 10), (90, 22), (98, 50), (96, 80, 1), (88, 60), (82, 70, 1), (76, 44)])],
    'back': [L(outline([(14, 74), (8, 40), (18, 12), (40, 0), (60, 0), (82, 12), (92, 40), (88, 74), (50, 80)])),
             L(rope((50, 2), (56, -24), (78, -20), 2.6), 'mid', 'b'),
             L(rope((50, 74), (52, 100), (50, 128), 3.4), 'mid', 'f'), L(ell(50, 76, 3, 2.4), 'deep', 'f', False),
             L(rope((10, 50), (2, 70), (-6, 96), 3.0), 'mid', 'b'),
             L(outline([(56, 2), (82, 14), (92, 44), (86, 70), (60, 60)]), 'shade', 'b', False)],
}

# Sigdo Mama (Matilda Shadebough, portera): grandota de cara redonda morena clara y mofletes rosas; una melena enorme de
# rizos verdes que le rodea la cara y le cae por los hombros; ojitos redondos, cejas gruesas y boca de gato
_mama_face = blob([(12, 50), (50, 36), (88, 50), (96, 76), (88, 100), (66, 110), (50, 112), (34, 110), (12, 100), (4, 76)])
CHARS['matilda-shadebough'] = {
    'body': 'corpulento', 'pal': pal('#3a9a7a', '#e8b490', iris='#1e1e2a', shade='#2a7a5e', deep='#1e5a44', blush='#f0948a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'none', 'mouth_y': 96, 'hairline': False, 'face_front': _mama_face, 'ears': False},
    'front': [L(puff(4, 96, 18, 18, 5, 0.2)), L(puff(96, 96, 18, 18, 5, 0.6)), L(puff(10, 66, 18, 22, 5, 0.4)), L(puff(90, 66, 18, 22, 5, 0.1)),
              L(puff(50, 24, 56, 34, 9, 0.1)),
              L(puff(62, 14, 30, 18, 5, 0.3), 'shade', 'b', False),
              L(puff(26, 48, 14, 11, 4, 0.2), 'mid', 'f'), L(puff(50, 42, 16, 11, 4, 0.5), 'mid', 'f'), L(puff(74, 48, 14, 11, 4, 0.1), 'mid', 'f'),
              L(puff(4, 100, 10, 8, 4, 0.2), 'mid', 'f'), L(puff(96, 100, 10, 8, 4, 0.6), 'mid', 'f'),
              L(ell(26, 88, 6, 3.6), 'blush', 'f', False), L(ell(74, 88, 6, 3.6), 'blush', 'f', False),
              L(quad((42, 92), (46, 96), (50, 92)) + quad((50, 92), (54, 96), (58, 92))[1:], OUTC, 'f', False, False, 1.6)],
    'side': [L(puff(40, 30, 54, 36, 9, 0.2)), L(puff(20, 80, 26, 30, 6, 0.3)), L(puff(40, 100, 20, 14, 5, 0.1)),
             L(outline([(4, 40), (40, 50), (46, 100), (20, 104), (0, 80)]), 'shade', 'b', False),
             L(puff(76, 30, 18, 14, 5, 0.3), 'mid', 'f'),
             L(ell(78, 90, 5, 3.4), 'blush', 'f', False)],
    'back': [L(puff(50, 30, 58, 38, 9, 0.1)), L(puff(10, 80, 24, 28, 6, 0.4)), L(puff(90, 80, 24, 28, 6, 0.1)), L(puff(50, 94, 34, 20, 7, 0.2)), L(puff(50, 66, 42, 28, 7, 0.3)),
             L(outline([(56, 0), (96, 30), (104, 80), (80, 104), (60, 60)]), 'shade', 'b', False)],
}
