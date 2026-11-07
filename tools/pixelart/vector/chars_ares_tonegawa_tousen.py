"""Instituto Ribera (ares-tonegawa-tousen, Tonegawa Tousen): sus modelos 3D de Inazuma Eleven Ares (zukan, 'アレスの天秤') como
referencia (busto de frente, perfil y espalda), calcados sobre la rejilla de unidades de cabeza.

Endou (Endou_AT en la wiki) es su capitán en Ares, con el mismo aspecto que en IE (pelo castaño con la cinta naranja): lleva el
dibujo de siempre."""
from chars import CHARS, L, OUTC, ell, outline, pal, strand
from heads import quad

WHITE = (248, 248, 248, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


def happy_eyes(y=76, sep=15):
    """Ojos cerrados de risa (arcos hacia arriba)."""
    return [L(quad((cx - 6, y + 2), (cx, y - 4), (cx + 6, y + 2)), OUTC, 'f', False, False, 2.4) for cx in (50 - sep, 50 + sep)]


# Noboru Sakanoue (Billy Miller): melena granate de mechones de punta tiesos hacia arriba, que cae hasta las orejas, con
# flequillo de puntas sobre la frente; ojos castaños y media sonrisa
CHARS['billy-miller'] = {
    'body': 'normal', 'pal': pal('#8a141a', '#f6c8a0', iris='#3a2420', shade='#6a0e14', light='#b03034'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 72), (8, 56), (8, 20), (14, -6, 1), (22, 6), (30, -14, 1), (38, 0), (46, -16, 1), (54, -2), (62, -14, 1), (70, 0), (80, -10, 1),
                         (84, 8), (92, 22), (92, 56), (86, 72), (84, 60), (16, 60)])),
              L(outline([(60, 0), (84, 10), (92, 36), (88, 66), (78, 40)]), 'shade', 'b', False),
              fringe([(12, 66), (14, 40), (26, 22), (50, 16), (74, 22), (86, 40), (88, 66), (80, 54), (74, 62, 1), (68, 46), (58, 58, 1), (54, 42), (46, 60, 1),
                      (40, 44), (32, 58, 1), (26, 48), (20, 64, 1)]),
              L(outline([(28, 4), (38, 0), (34, 14)]), 'light', 'f', False)],
    'side': [L(outline([(54, 62), (60, 48), (80, 48), (94, 34), (92, 8), (98, -6, 1), (78, -2), (72, -16, 1), (60, -4), (46, -18, 1), (38, -2), (18, -8, 1), (16, 8),
                        (2, 24), (-4, 60), (6, 80), (20, 90), (34, 86), (46, 74)])),
             L(outline([(0, 36), (24, 40), (28, 80), (6, 76)]), 'shade', 'b', False),
             fringe([(68, 4), (92, 16), (98, 40), (94, 62, 1), (86, 48), (80, 58, 1), (74, 40)])],
    'back': [L(outline([(12, 82), (6, 50), (8, 14), (14, -6, 1), (22, 6), (30, -14, 1), (38, 0), (46, -16, 1), (54, -2), (62, -14, 1), (70, 0), (80, -10, 1),
                        (84, 8), (92, 18), (94, 50), (88, 82), (74, 90, 1), (64, 84), (50, 92, 1), (36, 84), (26, 90, 1)])),
             L(outline([(56, 0), (84, 10), (94, 40), (88, 80), (64, 86)]), 'shade', 'b', False)],
}

# Toshiya Minoshima (Meriwether Beaumont): piel morena, pinchos rojo anaranjado larguísimos que salen hacia arriba en abanico
# por encima de una cinta azul de punto; ojos cerrados de risa y una sonrisa enorme
CHARS['meriwether-beaumont'] = {
    'body': 'normal', 'pal': pal('#c8481e', '#b87a4e', iris='#1e1414', shade='#9a3014', light='#e86a3a', band='#2a6a8a', band_d='#1e4a64'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 52), (10, 38), (-14, 26, 1), (8, 22), (4, -12, 1), (22, 8), (24, -36, 1), (40, 2), (52, -52, 1), (60, 0), (80, -40, 1), (78, 8),
                         (102, -14, 1), (92, 24), (114, 30, 1), (90, 40), (86, 52), (50, 46)])),
              L(outline([(56, -40), (60, 0), (78, -32), (78, 10), (90, 30), (86, 46), (70, 40)]), 'shade', 'b', False),
              L(outline([(10, 48), (12, 36), (50, 30), (88, 36), (90, 48), (50, 44)]), 'band', 'f', ln=True),
              L(outline([(56, 34), (88, 38), (88, 46), (58, 44)]), 'band_d', 'f', False),
              fringe([(14, 56), (16, 46), (30, 44), (50, 46), (70, 44), (84, 46), (86, 56), (76, 50), (70, 58, 1), (62, 50), (50, 56, 1), (40, 50), (30, 58, 1),
                      (22, 50)])] + happy_eyes(),
    'side': [L(outline([(60, 50), (90, 42), (94, 26), (110, -2, 1), (82, 14), (86, -26, 1), (60, 6), (50, -48, 1), (40, 6), (14, -20, 1), (18, 14), (-14, 0, 1),
                        (6, 28), (-10, 40, 1), (8, 44), (4, 70), (18, 84), (34, 80), (44, 66)])),
             L(outline([(4, 44), (24, 46), (26, 76), (8, 72)]), 'shade', 'b', False),
             L(outline([(6, 50), (8, 36), (50, 32), (94, 38), (94, 50), (50, 46)]), 'band', 'f', ln=True),
             L(quad((76, 76), (82, 70), (88, 76)), OUTC, 'f', False, False, 2.2)],
    'back': [L(outline([(14, 72), (8, 40), (-14, 26, 1), (6, 22), (2, -14, 1), (22, 6), (24, -38, 1), (40, 2), (52, -54, 1), (60, 0), (80, -42, 1), (78, 6),
                        (102, -16, 1), (92, 24), (114, 30, 1), (92, 40), (86, 72), (50, 80)])),
             L(outline([(56, -40), (60, 0), (78, -32), (78, 10), (92, 32), (86, 68), (64, 76)]), 'shade', 'b', False),
             L(outline([(8, 50), (10, 38), (50, 34), (90, 38), (92, 50), (50, 46)]), 'band', 'f', ln=True)],
}

# Kousaku Hashiya (Burleigh Carpenter): el grandullón; cabeza ancha con el pelo castaño muy oscuro de pinchos que se abren
# hacia los lados en horizontal como un tejado; ojos caídos de sueño, cejas gruesas y boca recta
CHARS['burleigh-carpenter'] = {
    'body': 'corpulento', 'pal': pal('#2e2024', '#f2c49a', iris='#1e1414', shade='#1e1418'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 98, 'hairline': False, 'big_ears': 2,
             'face_front': outline([(14, 50), (50, 42), (86, 50), (88, 90), (78, 108), (50, 112), (22, 108), (12, 90)])},
    'front': [L(outline([(16, 64), (14, 44), (-14, 46, 1), (8, 34), (-4, 28, 1), (14, 22), (24, 6), (30, -4, 1), (40, 4), (50, -6, 1), (58, 4), (70, -4, 1),
                         (76, 6), (86, 22), (104, 28, 1), (92, 34), (114, 46, 1), (86, 44), (84, 64), (76, 50), (24, 50)])),
              L(outline([(60, 4), (84, 16), (100, 32), (90, 40), (76, 30)]), 'shade', 'b', False),
              L(outline([(24, 64), (36, 60), (46, 64), (46, 70), (36, 72), (24, 70)]), WHITE, 'f', ln=True),
              L(outline([(54, 64), (64, 60), (76, 64), (76, 70), (64, 72), (54, 70)]), WHITE, 'f', ln=True),
              L([(24, 66), (46, 66)], OUTC, 'f', False, False, 2.0), L([(54, 66), (76, 66)], OUTC, 'f', False, False, 2.0),
              L(ell(38, 69, 1.8, 1.8), OUTC, 'f', False), L(ell(62, 69, 1.8, 1.8), OUTC, 'f', False)],
    'side': [L(outline([(58, 50), (66, 40), (82, 38), (94, 26), (104, 20, 1), (88, 12), (90, -2, 1), (72, 2), (62, -10, 1), (48, 0), (26, -6, 1), (24, 10), (0, 10, 1),
                        (10, 24), (-16, 34, 1), (6, 40), (4, 70), (16, 86), (30, 82), (40, 64)])),
             L(outline([(4, 36), (24, 40), (26, 78), (8, 72)]), 'shade', 'b', False),
             L(outline([(80, 62), (90, 60), (92, 70), (82, 72)]), WHITE, 'f', ln=True), L([(80, 64), (92, 64)], OUTC, 'f', False, False, 2.0)],
    'back': [L(outline([(16, 84), (14, 46), (-14, 46, 1), (8, 34), (-4, 28, 1), (14, 22), (24, 6), (30, -4, 1), (40, 4), (50, -6, 1), (58, 4), (70, -4, 1), (76, 6),
                        (86, 22), (104, 28, 1), (92, 34), (114, 46, 1), (86, 46), (84, 84), (50, 90)])),
             L(outline([(56, 4), (84, 16), (100, 34), (86, 46), (84, 80), (64, 86)]), 'shade', 'b', False)],
}

# Tetsuo Dan (Dan Bowsun): piel morena, pelo negro de punta hacia arriba atado con un pañuelo gris con el nudo arriba, y dos
# patillas larguísimas que bajan hasta la mandíbula y se abren hacia fuera; cejas fruncidas y sonrisa enorme de dientes
CHARS['dan-bowsun'] = {
    'body': 'normal', 'pal': pal('#1a1e28', '#b87a4e', iris='#1e1414', shade='#10131a', cloth='#c0bcc4', cloth_d='#94909a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'hairline': [(14, 56), (20, 40), (34, 34), (50, 40), (66, 34), (80, 40), (86, 56)]},
    'front': [L(outline([(16, 58), (14, 28), (20, -8), (30, 4), (36, -20, 1), (46, -6), (56, -24, 1), (62, -6), (76, -14, 1), (78, 6), (86, 28), (84, 58), (70, 42),
                         (50, 46), (30, 42)])),
              L(outline([(14, 56), (8, 80), (-4, 104, 1), (10, 100), (20, 84), (20, 60)])), L(outline([(86, 56), (92, 80), (104, 104, 1), (90, 100), (80, 84), (80, 60)])),
              L(outline([(10, 34), (12, 20), (50, 14), (88, 20), (90, 34), (50, 30)]), 'cloth', 'f', ln=True),
              L(outline([(40, 16), (50, 6), (60, 16), (50, 24)]), 'cloth_d', 'f', ln=True),
              L(outline([(40, 16), (24, 2), (30, 18)]), 'cloth', 'f', ln=True), L(outline([(60, 16), (76, 4), (70, 20)]), 'cloth', 'f', ln=True),
              L(outline([(12, 30), (-6, 40), (12, 36)]), 'cloth', 'f', ln=True)],
    'side': [L(outline([(54, 56), (60, 44), (80, 40), (92, 26), (90, 6), (98, -16, 1), (76, -2), (66, -22, 1), (54, -4), (40, -20, 1), (32, 0), (12, 10), (4, 40),
                        (8, 66), (22, 80), (40, 106, 1), (44, 86), (50, 72)])),
             L(outline([(4, 36), (24, 40), (26, 70), (8, 66)]), 'shade', 'b', False),
             L(outline([(4, 34), (8, 18), (50, 12), (94, 22), (96, 36), (50, 30)]), 'cloth', 'f', ln=True),
             L(outline([(96, 26), (110, 34), (104, 44), (94, 36)]), 'cloth_d', 'f', ln=True)],
    'back': [L(outline([(16, 80), (12, 30), (20, -8), (30, 4), (36, -20, 1), (46, -6), (56, -24, 1), (62, -6), (76, -14, 1), (78, 6), (88, 30), (84, 80), (50, 92)])),
             L(outline([(56, -4), (80, 4), (88, 40), (84, 76), (64, 86)]), 'shade', 'b', False),
             L(outline([(16, 70), (8, 90), (0, 104, 1), (14, 98), (20, 80)])), L(outline([(84, 70), (92, 90), (100, 104, 1), (86, 98), (80, 80)])),
             L(outline([(8, 34), (10, 20), (50, 14), (90, 20), (92, 34), (50, 30)]), 'cloth', 'f', ln=True)],
}

# Mitsunari Kaneshiro (Jack Sawyer): pelo verde menta muy claro, abultado y revuelto, con mechones que le caen por la frente
# y la cara; por debajo y detrás es gris verdoso oscuro; ojos grandes azules y sonrisa
CHARS['jack-sawyer'] = {
    'body': 'normal', 'pal': pal('#86dcc0', '#fcd8b8', iris='#1e4a8a', shade='#5e7a70', deep='#46605a', light='#b0f0dc'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 74), (6, 70), (-6, 46), (-2, 20), (14, 0), (36, -12), (50, -18, 1), (62, -10), (84, -2), (100, 16), (106, 42), (96, 70), (84, 74),
                         (84, 60), (16, 60)]), 'shade'),
              L(outline([(-2, 20), (14, 0), (36, -12), (50, -18, 1), (62, -10), (84, -2), (100, 16), (104, 36), (80, 30), (50, 26), (20, 32), (0, 38)]), 'mid', 'b', False),
              fringe([(12, 72), (12, 44), (24, 24), (50, 16), (76, 24), (88, 44), (88, 72), (80, 58), (76, 70, 1), (68, 50), (60, 60, 1), (56, 44), (50, 76, 1),
                      (44, 46), (36, 62, 1), (30, 48), (22, 70, 1), (18, 58)]),
              L(outline([(26, 22), (48, 14), (40, 28)]), 'light', 'f', False)],
    'side': [L(outline([(54, 64), (58, 50), (80, 48), (94, 34), (98, 12), (84, -6), (60, -16), (30, -16), (8, -4), (-10, 14), (-14, 44), (-6, 72), (10, 86),
                        (30, 90), (46, 76)]), 'shade'),
             L(outline([(8, -4), (30, -16), (60, -16), (84, -6), (98, 12), (96, 30), (70, 20), (40, 18), (10, 22), (-10, 14)]), 'mid', 'b', False),
             fringe([(66, 2), (92, 16), (98, 40), (94, 66, 1), (86, 50), (80, 62, 1), (76, 42), (66, 30)])],
    'back': [L(outline([(16, 86), (2, 80), (-8, 50), (-4, 20), (14, 0), (36, -12), (50, -18, 1), (62, -10), (84, -2), (102, 18), (108, 50), (98, 80), (84, 86),
                        (50, 92)]), 'shade'),
             L(outline([(-4, 20), (14, 0), (30, -10), (36, -24, 1), (44, -10), (52, -26, 1), (58, -10), (66, -22, 1), (70, -6), (84, -2), (102, 18), (104, 30),
                        (70, 34), (50, 28), (30, 34), (-2, 30)]), 'mid', 'b', False)],
}

# Jou Muhyou (Luke Blank): pelo azul petróleo en casco con flequillo recto que le tapa las cejas, mechones de punta a los lados
# y una antena que se levanta arriba; ojos redondos enormes en blanco con la pupila negra y boca pequeña
CHARS['luke-blank'] = {
    'body': 'bajito', 'pal': pal('#28587a', '#fcd8b8', iris='#1e1414', shade='#1a3a54', light='#4a82aa'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 90), (8, 74, 1), (10, 62), (6, 30), (16, 10), (-4, 2, 1), (20, 0), (40, -6), (60, -4), (66, -24, 1), (70, -2), (90, 4), (96, 30),
                         (94, 62), (96, 76, 1), (88, 90), (84, 64), (16, 64)])),
              L(outline([(60, 0), (86, 8), (96, 36), (90, 84), (80, 50)]), 'shade', 'b', False),
              fringe([(10, 66), (10, 36), (24, 16), (50, 8), (76, 16), (90, 36), (90, 66), (84, 62), (84, 52), (74, 52), (70, 62), (62, 56), (56, 62), (48, 54),
                      (40, 62), (32, 54), (24, 62), (16, 56), (16, 66)]),
              L(outline([(24, 16), (44, 10), (34, 22)]), 'light', 'f', False)],
    'side': [L(outline([(54, 66), (58, 52), (82, 50), (94, 36), (92, 12), (72, -2), (50, -4), (40, -24, 1), (34, -4), (14, 6), (2, 30), (2, 66), (12, 86), (28, 92),
                        (44, 80)])),
             L(outline([(2, 34), (24, 40), (30, 82), (10, 82)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 14), (96, 40), (96, 56), (88, 52), (86, 40), (74, 36)])],
    'back': [L(outline([(14, 92), (6, 76, 1), (6, 50), (6, 30), (16, 10), (-4, 2, 1), (20, 0), (34, -6), (36, -26, 1), (42, -6), (60, -4), (84, 4), (96, 30),
                        (94, 76), (88, 92), (70, 100), (50, 96), (30, 100)])),
             L(outline([(56, 0), (86, 8), (96, 40), (90, 88), (66, 96)]), 'shade', 'b', False)],
}

# Kouji Genba (Gaffer Mason): piel morena, el pelo azul marino muy oscuro en un tupé plano y alto, orejas grandes, nariz de
# bola, ojos de pillo y una sonrisa de oreja a oreja
CHARS['gaffer-mason'] = {
    'body': 'corpulento', 'pal': pal('#1a1e2e', '#d8944e', iris='#1e1414', shade='#10131e', nose='#c47e3e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 100, 'hairline': [(18, 62), (22, 44), (34, 38), (50, 40), (66, 38), (78, 44), (82, 62)],
             'big_ears': 3, 'ear_out': 4, 'nose': (50, 86, 4.4)},
    'front': [L(outline([(18, 64), (16, 30), (22, 4), (50, -4), (78, 4), (84, 30), (82, 64), (80, 46), (20, 46)])),
              L(outline([(60, -2), (78, 6), (84, 34), (80, 58), (72, 38)]), 'shade', 'b', False),
              L(quad((26, 96), (50, 110), (74, 96)), OUTC, 'f', False, False, 2.0)],
    'side': [L(outline([(56, 54), (62, 42), (86, 36), (96, 18), (90, -4), (60, -8), (28, -4), (10, 10), (6, 44), (10, 70), (24, 80), (38, 64)])),
             L(outline([(8, 36), (26, 40), (28, 74), (12, 70)]), 'shade', 'b', False),
             L(outline([(92, 78), (104, 82), (98, 92), (90, 88)]), 'nose', 'f', ln=True)],
    'back': [L(outline([(16, 76), (14, 30), (22, 4), (50, -4), (78, 4), (86, 30), (84, 76), (50, 82)])),
             L(outline([(56, -2), (80, 6), (86, 40), (82, 72), (64, 78)]), 'shade', 'b', False)],
}

# Ikuto Tanoue (Giles Farmer): un casco de pelo azul marino oscuro enorme y redondo como una bola, que le baja hasta las orejas;
# carita pequeña de ojos de punto y sonrisa
CHARS['giles-farmer'] = {
    'body': 'bajito', 'pal': pal('#283648', '#fcd4b0', iris='#1e1414', shade='#1a2432', light='#46586e'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 76), (-4, 70), (-12, 40), (-6, 10), (14, -14), (50, -24), (86, -14), (106, 10), (112, 40), (104, 70), (88, 76), (84, 64), (16, 64)])),
              L(outline([(60, -20), (88, -10), (108, 20), (104, 64), (86, 66), (82, 40)]), 'shade', 'b', False),
              fringe([(10, 70), (10, 46), (22, 34), (40, 30), (50, 40), (60, 30), (78, 34), (90, 46), (90, 70), (82, 60), (70, 52), (50, 56), (30, 52), (18, 60)]),
              L(outline([(10, 10), (34, -10), (54, -16), (36, 0), (16, 22)]), 'light', 'f', False),
              strand([(16, 4), (50, -10), (84, 4)], 'shade', 'f', 1.0), strand([(8, 30), (50, 20), (92, 30)], 'shade', 'f', 1.0)],
    'side': [L(outline([(56, 70), (60, 56), (82, 54), (98, 40), (100, 10), (80, -14), (46, -24), (14, -16), (-8, 6), (-16, 40), (-10, 72), (8, 90), (30, 90), (48, 82)])),
             L(outline([(-10, 30), (20, 40), (30, 86), (2, 84)]), 'shade', 'b', False),
             fringe([(66, 2), (94, 18), (100, 42), (98, 58), (88, 56), (86, 44), (74, 38)])],
    'back': [L(outline([(10, 86), (-6, 72), (-12, 40), (-6, 10), (14, -14), (50, -24), (86, -14), (106, 10), (112, 40), (106, 72), (90, 86), (50, 94)])),
             L(outline([(56, -20), (88, -10), (110, 20), (106, 76), (66, 90), (70, 30)]), 'shade', 'b', False)],
}

# Kakeru Shimomachi (Pacey Hawker): pelo verde intenso abultado y despeinado, con mechones que le caen por la frente y una
# coleta gruesa recogida en la nuca que asoma por un lado; ojos grandes y sonrisa de dientes
CHARS['pacey-hawker'] = {
    'body': 'normal', 'pal': pal('#1e7a34', '#fcd4b0', iris='#1e1414', shade='#145426', light='#3aa050'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 80), (2, 70), (-2, 40), (4, 10), (20, -12), (40, -24), (62, -22), (80, -10), (96, 12), (100, 40), (96, 70), (86, 80), (84, 62), (16, 62)])),
              L(outline([(60, -20), (84, -6), (98, 30), (94, 74), (82, 50)]), 'shade', 'b', False),
              L(outline([(10, 80), (0, 92), (6, 108), (22, 106), (20, 90)])),
              fringe([(12, 70), (12, 42), (24, 22), (50, 14), (76, 22), (88, 42), (88, 70), (80, 56), (76, 66, 1), (68, 48), (60, 60, 1), (56, 44), (48, 64, 1),
                      (42, 46), (34, 60, 1), (28, 48), (20, 66, 1)]),
              L(outline([(20, 0), (40, -12), (34, 6)]), 'light', 'f', False)],
    'side': [L(outline([(54, 62), (58, 48), (82, 46), (96, 30), (96, 4), (78, -16), (50, -24), (20, -18), (2, -2), (-8, 30), (-6, 64), (6, 82), (24, 90), (44, 76)])),
             L(outline([(16, 76), (6, 92), (14, 118), (34, 116), (34, 96)])),
             L(outline([(-6, 30), (20, 36), (24, 76), (0, 70)]), 'shade', 'b', False),
             fringe([(66, 2), (92, 16), (98, 40), (94, 64, 1), (86, 50), (80, 60, 1), (76, 42), (66, 30)])],
    'back': [L(outline([(12, 82), (2, 70), (-4, 40), (4, 10), (20, -12), (40, -24), (62, -22), (80, -10), (96, 12), (104, 40), (98, 70), (88, 82), (50, 90)])),
             L(outline([(56, -20), (84, -6), (102, 30), (96, 76), (66, 86)]), 'shade', 'b', False),
             L(outline([(40, 80), (60, 80), (64, 100), (50, 110), (36, 100)]), 'mid', 'f', ln=True),
             L(outline([(42, 82), (58, 82), (60, 90), (40, 90)]), 'shade', 'f', False)],
}

# Mizuho Kaname (Neville Merchant): pelo gris ceniza en rizos esponjosos que le abultan la cabeza y caen por los lados de la
# cara, con un mechón que cruza la frente; piel muy pálida, ojos grandes azul grisáceo preocupados
CHARS['neville-merchant'] = {
    'body': 'delgado', 'pal': pal('#8a8488', '#fce8dc', iris='#5a6a9a', shade='#5e5458', deep='#463e42', light='#a8a4a6'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 96), (2, 98), (-4, 82), (2, 66), (-6, 50), (2, 30), (14, 8), (36, -6), (60, -8), (82, 4), (98, 26), (104, 50), (98, 68), (104, 86),
                         (96, 100), (84, 94), (84, 62), (16, 62)])),
              L(outline([(60, -4), (86, 8), (100, 40), (100, 92), (86, 92), (82, 50)]), 'shade', 'b', False),
              L(ell(4, 88, 9, 9), 'mid', 'b', ln=True), L(ell(96, 88, 9, 9), 'mid', 'b', ln=True),
              fringe([(12, 66), (14, 40), (26, 20), (50, 12), (74, 20), (88, 40), (88, 66), (80, 52), (66, 40), (54, 48), (48, 40), (36, 50), (24, 46), (18, 60)]),
              L(outline([(26, 20), (44, 14), (36, 26)]), 'light', 'f', False)],
    'side': [L(outline([(54, 66), (58, 52), (80, 50), (94, 36), (90, 12), (70, -4), (40, -8), (14, 4), (0, 26), (-8, 50), (-4, 78), (8, 96), (24, 104), (40, 96),
                        (48, 80)])),
             L(ell(-2, 70, 9, 9), 'shade', 'b', ln=True), L(ell(14, 96, 10, 9), 'mid', 'b', ln=True),
             L(outline([(0, 30), (24, 36), (30, 86), (6, 84)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 16), (94, 40), (92, 62), (86, 56), (84, 44), (76, 36)])],
    'back': [L(outline([(14, 90), (0, 92), (-6, 76), (0, 56), (-4, 40), (6, 20), (22, 2), (50, -8), (78, 2), (94, 20), (104, 40), (100, 56), (106, 76), (100, 92),
                        (86, 90), (76, 100), (60, 94), (50, 102), (40, 94), (24, 100)])),
             L(outline([(56, -4), (86, 8), (102, 44), (100, 88), (66, 96)]), 'shade', 'b', False),
             L(ell(10, 86, 9, 8), 'mid', 'b', ln=True), L(ell(90, 86, 9, 8), 'mid', 'b', ln=True), L(ell(50, 94, 10, 8), 'mid', 'b', ln=True)],
}

# Nagomu Onba (Eamond Everwing): pelo verde oliva oscuro en casco redondo que le enmarca la cara hasta la barbilla, con dos
# picos como orejas de animal arriba y flequillo en pico; bufanda roja al cuello; ojos grandes y boca pequeña
CHARS['eamond-everwing'] = {
    'body': 'bajito', 'pal': pal('#4a4a24', '#fcd8b8', iris='#6a2a3a', shade='#34341a', scarf='#c8483e', scarf_d='#9a3028'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(8, 104), (0, 70), (2, 30), (-4, 4, 1), (16, 14), (50, 4), (84, 14), (104, 4, 1), (98, 30), (100, 70), (92, 104), (80, 100), (84, 60),
                         (16, 60), (20, 100)])),
              L(outline([(60, 6), (86, 14), (98, 40), (96, 96), (84, 96), (82, 50)]), 'shade', 'b', False),
              fringe([(10, 66), (10, 36), (24, 18), (50, 12), (76, 18), (90, 36), (90, 66), (80, 54), (66, 48), (56, 52), (50, 66, 1), (44, 52), (34, 48), (20, 54)]),
              L(outline([(14, 104), (30, 100), (50, 106), (70, 100), (86, 104), (84, 116), (16, 116)]), 'scarf', 'f', ln=True)],
    'side': [L(outline([(54, 68), (58, 54), (82, 52), (94, 36), (90, 12), (74, 0), (80, -16, 1), (60, -2), (36, -2), (12, 12), (0, 40), (0, 80), (12, 100), (30, 104),
                        (46, 94)])),
             L(outline([(0, 40), (24, 44), (30, 96), (8, 94)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 16), (94, 40), (94, 60), (86, 56), (84, 44), (74, 38)]),
             L(outline([(30, 102), (60, 98), (80, 104), (76, 118), (40, 118), (20, 124, 1), (24, 110)]), 'scarf', 'f', ln=True)],
    'back': [L(outline([(8, 104), (0, 70), (2, 30), (-4, 4, 1), (16, 14), (50, 4), (84, 14), (104, 4, 1), (98, 30), (100, 70), (92, 104), (50, 110)])),
             L(outline([(56, 6), (86, 14), (100, 40), (96, 100), (66, 106), (70, 50)]), 'shade', 'b', False),
             L(outline([(16, 104), (50, 108), (84, 104), (84, 116), (16, 116)]), 'scarf', 'f', ln=True),
             L(outline([(40, 106), (34, 124), (46, 120), (50, 108)]), 'scarf_d', 'f', ln=True)],
}

# Masasada Hatake (Frey Fielding): pelo color arena con manchas más claras, abultado y en pico arriba, que le cae en capas
# hasta las mejillas con las puntas hacia fuera; pecas, ojos castaños y sonrisa pícara
CHARS['frey-fielding'] = {
    'body': 'normal', 'pal': pal('#a89a6e', '#fcd8b8', iris='#4a2a20', shade='#6e5a40', deep='#54442e', light='#c8bc94'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 92), (2, 82, 1), (6, 66), (-8, 50, 1), (2, 40), (-6, 24, 1), (8, 14), (24, -4), (40, -12), (48, -26, 1), (56, -10), (76, -4), (92, 14),
                         (106, 24, 1), (98, 40), (106, 50, 1), (94, 66), (98, 82, 1), (86, 92), (84, 64), (16, 64)])),
              L(outline([(60, -6), (86, 10), (98, 38), (94, 84), (82, 50)]), 'shade', 'b', False),
              fringe([(14, 70), (14, 44), (26, 24), (50, 18), (74, 24), (86, 44), (86, 70), (80, 56), (66, 44), (50, 40), (34, 44), (20, 56)]),
              L(ell(30, 8, 5, 3), 'light', 'f', False), L(ell(70, 10, 5, 3), 'light', 'f', False), L(ell(50, -2, 4, 3), 'light', 'f', False),
              L(ell(30, 90, 1, 1), OUTC, 'f', False), L(ell(34, 93, 1, 1), OUTC, 'f', False), L(ell(70, 90, 1, 1), OUTC, 'f', False), L(ell(66, 93, 1, 1), OUTC, 'f', False)],
    'side': [L(outline([(54, 66), (58, 52), (80, 50), (94, 36), (98, 14), (84, -6), (60, -14), (50, -30, 1), (40, -14), (14, 0), (-8, 18, 1), (0, 30), (-12, 50, 1),
                        (2, 58), (-4, 76, 1), (12, 80), (8, 98, 1), (24, 88), (38, 96, 1), (44, 80)])),
             L(outline([(2, 34), (24, 40), (28, 80), (8, 76)]), 'shade', 'b', False),
             fringe([(66, 2), (92, 16), (98, 40), (94, 64, 1), (86, 50), (80, 60, 1), (76, 42), (66, 30)]),
             L(ell(60, 2, 6, 3), 'light', 'f', False)],
    'back': [L(outline([(14, 94), (0, 84, 1), (6, 66), (-8, 50, 1), (2, 40), (-6, 24, 1), (8, 14), (24, -4), (40, -12), (48, -26, 1), (56, -10), (76, -4), (92, 14),
                        (106, 24, 1), (98, 40), (108, 52, 1), (94, 66), (100, 84, 1), (86, 94), (70, 100, 1), (60, 92), (50, 102, 1), (40, 92), (30, 100, 1)])),
             L(outline([(56, -6), (86, 10), (100, 40), (94, 88), (66, 94)]), 'shade', 'b', False),
             L(ell(36, 20, 6, 4), 'light', 'f', False), L(ell(64, 30, 6, 4), 'light', 'f', False)],
}

# Housaku Komedawara (Tobin Harveston): cara redondísima de mofletes rosados, pelo castaño corto de puntas con un pico en lo
# alto y dos más como orejas; ojos pequeños y redondos y boca torcida
CHARS['tobin-harveston'] = {
    'body': 'corpulento', 'pal': pal('#8a5a30', '#fcd8b8', iris='#1e1414', shade='#6a4222', blush='#f4a888'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'hairline': False, 'big_ears': 1,
             'face_front': outline([(4, 60), (10, 38), (30, 28), (50, 26), (70, 28), (90, 38), (96, 60), (98, 84), (86, 106), (50, 114), (14, 106), (2, 84)])},
    'front': [L(outline([(14, 54), (16, 32), (12, 20, 1), (26, 22), (36, 8), (50, -6, 1), (60, 8), (74, 22), (88, 20, 1), (84, 32), (86, 54), (76, 42), (66, 50, 1),
                         (60, 40), (50, 50, 1), (40, 40), (34, 50, 1), (24, 42)])),
              L(outline([(56, 4), (70, 18), (84, 34), (84, 50), (74, 40)]), 'shade', 'b', False),
              L(ell(18, 88, 8, 6), 'blush', 'f', False), L(ell(82, 88, 8, 6), 'blush', 'f', False)],
    'side': [L(outline([(60, 46), (70, 36), (86, 30), (86, 14), (70, 4), (60, -10, 1), (52, 4), (30, 4), (20, -4, 1), (18, 12), (6, 20), (-6, 30, 1), (4, 38),
                        (4, 56), (18, 60), (32, 52), (44, 48)])),
             L(outline([(6, 26), (26, 30), (26, 54), (10, 54)]), 'shade', 'b', False),
             L(ell(84, 88, 7, 6), 'blush', 'f', False)],
    'back': [L(outline([(10, 74), (10, 32), (6, 20, 1), (20, 20), (36, 8), (50, -6, 1), (60, 8), (76, 20), (94, 18, 1), (90, 32), (90, 74), (70, 80), (50, 74), (30, 80)])),
             L(outline([(56, 4), (76, 20), (90, 40), (88, 70), (66, 78)]), 'shade', 'b', False)],
}

# Einosuke Sumiyoshi (Everest Brightwell): melena verde oscuro lisa que baja hasta la mandíbula y se abre en puntas hacia los
# lados, con raya en pico; pecas, ojos verdes afilados y un colmillo
CHARS['everest-brightwell'] = {
    'body': 'normal', 'pal': pal('#3e6040', '#fcd8b8', iris='#3a6a3a', shade='#2a442c', deep='#1e3220', light='#5a805a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 96), (-6, 90), (-16, 80, 1), (-2, 74), (2, 40), (12, 10), (32, -10), (50, -16), (68, -10), (88, 10), (98, 40), (102, 74), (116, 80, 1),
                         (106, 90), (86, 96), (84, 64), (16, 64)])),
              L(outline([(60, -10), (86, 8), (98, 40), (106, 88), (88, 90), (82, 50)]), 'shade', 'b', False),
              fringe([(12, 66), (12, 36), (26, 14), (46, 4), (50, 10), (54, 4), (74, 14), (88, 36), (88, 66), (82, 56), (72, 40), (56, 30), (52, 44, 1), (48, 44),
                      (44, 30), (28, 40), (18, 56)]),
              L(outline([(44, 101), (46, 105, 1), (48, 101)]), WHITE, 'f', ln=True),
              L(ell(28, 88, 1, 1), OUTC, 'f', False), L(ell(32, 91, 1, 1), OUTC, 'f', False), L(ell(72, 88, 1, 1), OUTC, 'f', False), L(ell(68, 91, 1, 1), OUTC, 'f', False)],
    'side': [L(outline([(54, 66), (58, 52), (80, 50), (94, 36), (96, 12), (80, -8), (50, -16), (22, -8), (6, 10), (-4, 40), (-14, 70), (-24, 82, 1), (-2, 84), (6, 96),
                        (26, 100), (40, 96), (48, 82)])),
             L(outline([(-4, 40), (24, 46), (30, 92), (4, 92)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 40), (94, 60), (86, 56), (84, 44), (74, 36)])],
    'back': [L(outline([(16, 96), (-8, 92), (-20, 80, 1), (-2, 72), (2, 40), (12, 10), (32, -10), (50, -16), (68, -10), (88, 10), (98, 40), (102, 72), (120, 80, 1),
                        (108, 92), (84, 96), (70, 104, 1), (50, 98), (30, 104, 1)])),
             L(outline([(56, -10), (86, 8), (100, 40), (108, 88), (70, 100), (70, 50)]), 'shade', 'b', False)],
}

# Ponko Tanukigahara (Kia Tanner): pelo castaño con dos moños en aro arriba como orejas de mapache y una hoja verde en lo alto,
# flequillo recto y mechones lisos a los lados; tirita en la nariz, coloretes y boca abierta de alegría
CHARS['kia-tanner'] = {
    'body': 'chica', 'pal': pal('#9a5a1e', '#fcdcc4', iris='#c8701e', shade='#6e3e14', light='#c48040', leaf='#5ab84a', leaf_d='#3a8a30', tape='#f0c870',
                                blush='#f8a8a0'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 100, 'hairline': False},
    'front': [L(ell(10, -2, 14, 13), 'mid', 'b', ln=True), L(ell(90, -2, 14, 13), 'mid', 'b', ln=True),
              L(ell(10, -2, 6, 5), (255, 255, 255, 0), 'b', False), L(ell(90, -2, 6, 5), (255, 255, 255, 0), 'b', False),
              L(outline([(12, 70), (8, 36), (20, 12), (50, 2), (80, 12), (92, 36), (88, 70), (84, 60), (16, 60)])),
              L(outline([(60, 4), (84, 14), (92, 44), (86, 66), (78, 40)]), 'shade', 'b', False),
              L(outline([(12, 60), (8, 98), (14, 104), (22, 96), (22, 64)]), 'mid', 'f'), L(outline([(88, 60), (92, 98), (86, 104), (78, 96), (78, 64)]), 'mid', 'f'),
              fringe([(10, 62), (10, 36), (24, 16), (50, 10), (76, 16), (90, 36), (90, 62), (80, 62), (80, 54), (70, 62), (70, 54), (60, 62), (60, 54), (50, 62),
                      (50, 54), (40, 62), (40, 54), (30, 62), (30, 54), (20, 62)]),
              L(outline([(50, 4), (40, -4), (50, -10), (62, -6), (56, 4)]), 'leaf', 'f', ln=True),
              L(outline([(40, 84), (60, 84), (60, 90), (40, 90)]), 'tape', 'f', ln=True),
              L(ell(24, 92, 5, 3), 'blush', 'f', False), L(ell(76, 92, 5, 3), 'blush', 'f', False)],
    'side': [L(outline([(36, 6), (40, -24), (52, -26), (54, 0)]), 'mid', 'b', ln=True),
             L(outline([(54, 66), (58, 52), (80, 50), (94, 36), (90, 12), (70, 0), (40, 0), (16, 12), (4, 36), (4, 66), (14, 84), (30, 88), (46, 78)])),
             L(outline([(4, 36), (26, 42), (30, 80), (10, 78)]), 'shade', 'b', False),
             L(outline([(52, 62), (54, 100), (60, 104), (64, 92), (62, 62)]), 'mid', 'f'),
             fringe([(64, 2), (90, 16), (96, 40), (96, 56), (88, 54), (86, 44), (74, 38)]),
             L(outline([(60, 4), (56, -6), (70, -6), (74, 4)]), 'leaf', 'f', ln=True),
             L(outline([(88, 82), (98, 82), (98, 88), (88, 88)]), 'tape', 'f', ln=True)],
    'back': [L(ell(10, -2, 14, 13), 'mid', 'b', ln=True), L(ell(90, -2, 14, 13), 'mid', 'b', ln=True),
             L(outline([(12, 80), (8, 36), (20, 12), (50, 2), (80, 12), (92, 36), (88, 80), (66, 88), (34, 88)])),
             L(outline([(56, 4), (84, 14), (92, 46), (86, 78), (64, 86)]), 'shade', 'b', False),
             L(outline([(14, 70), (10, 96), (16, 102), (22, 92), (24, 76)]), 'mid', 'f'), L(outline([(86, 70), (90, 96), (84, 102), (78, 92), (76, 76)]), 'mid', 'f'),
             strand([(50, 4), (50, 84)], 'shade', 'b', 1.0), strand([(14, 60), (86, 60)], 'shade', 'b', 1.0)],
}
