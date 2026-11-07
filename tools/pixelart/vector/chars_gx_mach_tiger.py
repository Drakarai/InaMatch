"""Mach Tiger / Muay Tigers (gx-mach-tiger, Tailandia): sus modelos 3D de Inazuma Eleven GO Galaxy como referencia (busto
de frente, perfil y espalda), calcados sobre la rejilla de unidades de cabeza."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from chars_bigwaves import bald, white_eyes, side_eye
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Udom (portero): una mata enorme de pelo verde oliva en pinchos que le rodea la cabeza como un erizo, con mechones en punta
# sobre la frente; piel morena, ojos blancos redondos y cejas fruncidas
CHARS['udom'] = {
    'body': 'corpulento', 'pal': pal('#6a5c1c', '#a8724a', shade='#4c4214', deep='#3a3210'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False, 'big_ears': 1},
    'front': [L(outline([(16, 96), (6, 90, 1), (12, 80), (0, 70, 1), (8, 62), (-2, 52, 1), (8, 44), (2, 30, 1), (14, 28), (12, 12, 1), (26, 16), (30, 2, 1),
                         (40, 10), (50, -4, 1), (58, 8), (68, 0, 1), (72, 14), (86, 12, 1), (86, 26), (98, 30, 1), (92, 42), (102, 52, 1), (92, 60), (100, 70, 1),
                         (88, 80), (94, 90, 1), (84, 96), (82, 72), (18, 72)])),
              L(outline([(60, 6), (84, 16), (92, 44), (90, 80), (80, 60)]), 'shade', 'b', False),
              fringe([(14, 70), (14, 44), (28, 28), (50, 22), (72, 28), (86, 44), (86, 70), (80, 60), (74, 68, 1), (66, 54), (58, 64, 1), (50, 52), (42, 64, 1),
                      (34, 54), (26, 68, 1), (20, 60)]),
              strand([(40, 26), (44, 50)], 'shade', 'f', 1.0), strand([(60, 26), (56, 50)], 'shade', 'f', 1.0)]
             + white_eyes(78, 15, 6.6, 6.2, 2.0),
    'side': [L(outline([(56, 62), (62, 48), (82, 46), (92, 30), (86, 12), (92, 0, 1), (74, 4), (70, -12, 1), (56, 2), (40, -12, 1), (32, 4), (14, -4, 1), (16, 12),
                        (-4, 8, 1), (6, 24), (-14, 30, 1), (2, 40), (-14, 52, 1), (2, 58), (-10, 72, 1), (6, 74), (0, 88, 1), (16, 84), (20, 96, 1), (32, 86),
                        (46, 76)])),
             L(outline([(0, 40), (26, 46), (30, 84), (6, 80)]), 'shade', 'b', False),
             fringe([(64, 6), (88, 18), (94, 38), (90, 58, 1), (84, 44), (78, 54, 1), (74, 38), (64, 28)])] + side_eye(78),
    'back': [L(outline([(16, 100), (4, 90, 1), (10, 82), (-4, 72, 1), (6, 64), (-6, 52, 1), (6, 44), (-2, 30, 1), (12, 26), (10, 10, 1), (24, 14), (30, -2, 1),
                        (40, 8), (50, -6, 1), (60, 8), (70, -2, 1), (76, 12), (90, 10, 1), (88, 26), (102, 30, 1), (94, 44), (106, 52, 1), (94, 64), (104, 72, 1),
                        (90, 82), (96, 90, 1), (84, 100), (70, 94, 1), (60, 104, 1), (50, 96), (40, 104, 1), (30, 94, 1)])),
             L(outline([(58, 8), (88, 22), (98, 50), (90, 92), (66, 96)]), 'shade', 'b', False),
             L(ell(36, 40, 6, 4), 'deep', 'b', False), L(ell(56, 62, 7, 4), 'deep', 'b', False), L(ell(30, 76, 6, 4), 'deep', 'b', False)],
}

# Yam Poapan: el pelo azul petróleo en pinchos de punta, con un moño pequeño arriba, sobre una cinta rosa pálido en la frente;
# por debajo de la cinta, las sienes y la nuca rapadas en gris; piel morena y marcas en las mejillas
CHARS['yuth-poonlarp'] = {
    'body': 'normal', 'pal': pal('#1e4a62', '#b07448', shade='#143446', band='#ecc8c4', band_d='#b8989a', buzz='#4a4e54', buzz_d='#383c42'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': (58, 50), 'big_ears': 1},
    'front': [L(outline([(16, 70), (15, 46), (85, 46), (84, 70), (80, 58), (20, 58)]), 'buzz'),
              L(outline([(16, 46), (14, 30), (8, 14, 1), (22, 20), (24, 0, 1), (34, 10), (42, -4, 1), (50, 6), (54, -16, 1), (64, -8), (62, 4), (72, -2, 1),
                         (76, 14), (90, 8, 1), (86, 26), (88, 46)])),
              L(ell(58, -14, 6, 5)),
              L(outline([(60, 2), (84, 12), (88, 40), (74, 38)]), 'shade', 'b', False),
              L(outline([(12, 48), (12, 38), (50, 34), (88, 38), (88, 48), (50, 44)]), 'band', 'f', ln=True),
              L(outline([(56, 36), (88, 40), (88, 47), (58, 44)]), 'band_d', 'f', False),
              L([(22, 86), (28, 84)], OUTC, 'f', False, False, 1.0), L([(72, 84), (78, 86)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(54, 52), (40, 48), (12, 50), (8, 64), (16, 80), (32, 86), (48, 76)]), 'buzz'),
             L(outline([(8, 46), (4, 26), (-6, 16, 1), (8, 14), (10, -2, 1), (22, 6), (34, -6, 1), (44, 6), (56, -4, 1), (62, 8), (76, 0, 1), (80, 14), (94, 16, 1),
                        (92, 46)])),
             L(ell(8, -10, 8, 7)), L(outline([(4, -14), (10, -26, 1), (14, -14)])),
             L(outline([(2, 50), (2, 40), (50, 36), (95, 40), (95, 48), (50, 46)]), 'band', 'f', ln=True),
             L([(76, 84), (82, 86)], OUTC, 'f', False, False, 1.0)],
    'back': [L(outline([(16, 48), (84, 48), (86, 74), (70, 90), (30, 90), (14, 74)]), 'buzz'),
             L(outline([(56, 50), (86, 50), (86, 74), (66, 88)]), 'buzz_d', 'b', False),
             L(outline([(16, 46), (12, 28), (6, 14, 1), (20, 16), (24, 0, 1), (36, 8), (44, -6, 1), (56, -6), (64, 8), (76, 0, 1), (80, 16), (94, 14, 1), (88, 28),
                        (84, 46)])),
             L(ell(50, -12, 8, 7)), L(outline([(46, -16), (50, -28, 1), (54, -16)])),
             L(outline([(12, 50), (12, 40), (50, 38), (88, 40), (88, 50), (50, 48)]), 'band', 'f', ln=True)],
}

# Napa Radam: pelo verde muy oscuro en casco redondo, con el flequillo peinado de lado que le tapa media frente y termina en
# un mechón en punta entre los ojos; ojos negros redondos, cejas gruesas fruncidas
CHARS['napa'] = {
    'body': 'normal', 'pal': pal('#174a3a', '#d89a68', shade='#0f3428', iris='#141414'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 76), (10, 44), (18, 20), (36, 6), (54, 4), (74, 10), (88, 28), (90, 50), (86, 76), (82, 58), (18, 58)])),
              L(outline([(62, 8), (84, 22), (90, 48), (86, 70), (80, 44)]), 'shade', 'b', False),
              fringe([(12, 70), (12, 46), (20, 30), (36, 18), (60, 16), (78, 24), (88, 40), (88, 60), (80, 50), (70, 46), (62, 50), (56, 72, 1), (50, 54),
                      (44, 60, 1), (40, 48), (28, 54), (18, 66, 1)]),
              L(outline([(26, 26), (46, 20), (36, 30)]), 'light', 'f', False)],
    'side': [L(outline([(54, 66), (58, 54), (80, 50), (92, 36), (88, 16), (70, 2), (44, -2), (20, 8), (6, 30), (4, 56), (10, 76), (24, 86), (40, 84), (50, 74)])),
             L(outline([(6, 36), (28, 42), (32, 80), (12, 76)]), 'shade', 'b', False),
             fringe([(66, 4), (88, 18), (94, 40), (92, 60, 1), (84, 46), (76, 36)])],
    'back': [L(outline([(14, 78), (10, 44), (18, 20), (36, 6), (64, 6), (82, 20), (90, 44), (86, 78), (68, 88), (32, 88)])),
             L(outline([(58, 8), (82, 20), (90, 48), (84, 76), (64, 86)]), 'shade', 'b', False)],
}

# Nadech Sirilak: pelo castaño muy oscuro corto en casco, con la raya en medio que deja la frente en pico; ojos afilados con
# pestañas y la mirada seria
CHARS['naid-sirisukha'] = {
    'body': 'normal', 'pal': pal('#3a2e22', '#d89c6c', shade='#2a2018', iris='#2a3a4a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': [(12, 62), (26, 52), (40, 36), (50, 26), (60, 36), (74, 52), (88, 62)]},
    'front': [L(outline([(14, 70), (10, 40), (20, 14), (42, 0), (62, 0), (82, 12), (92, 38), (88, 70), (82, 60), (18, 60)])),
              L(outline([(60, 4), (84, 16), (92, 44), (86, 62), (78, 40)]), 'shade', 'b', False),
              strand([(50, 2), (50, 24)], 'deep', 'b', 1.0)],
    'side': [L(outline([(52, 64), (56, 52), (78, 44), (90, 30), (86, 12), (66, -2), (40, -2), (16, 10), (4, 34), (4, 58), (12, 80), (26, 90), (40, 84), (48, 74)])),
             L(outline([(6, 36), (26, 42), (30, 82), (12, 78)]), 'shade', 'b', False),
             L(outline([(52, 64), (60, 70), (58, 80), (50, 74)]), 'mid', 'f')],
    'back': [L(outline([(14, 82), (10, 40), (20, 14), (42, 0), (62, 0), (84, 14), (92, 40), (88, 82), (70, 94), (50, 98, 1), (30, 94)])),
             L(outline([(58, 4), (84, 16), (92, 46), (86, 80), (64, 92)]), 'shade', 'b', False)],
}

# Sarana Kukri: pelo castaño oliva oscuro en casco, con la frente en pico, y una coleta baja en la nuca atada con una goma roja;
# ojos grandes verde azulado y cejas fruncidas
CHARS['sulada'] = {
    'body': 'normal', 'pal': pal('#3c3820', '#d89a6c', shade='#2a2816', iris='#3a8a8a', band='#b8261e'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': [(12, 66), (28, 56), (42, 46), (50, 40), (58, 46), (72, 56), (88, 66)]},
    'front': [L(outline([(14, 76), (10, 42), (20, 16), (42, 2), (62, 2), (82, 14), (92, 40), (88, 76), (82, 64), (18, 64)])),
              L(outline([(60, 6), (84, 18), (92, 46), (86, 70), (78, 44)]), 'shade', 'b', False),
              strand([(50, 4), (50, 36)], 'deep', 'b', 1.0)],
    'side': [L(outline([(20, 78), (8, 92), (-2, 112), (-6, 126, 1), (6, 112), (16, 96), (28, 84)])),
             L(outline([(52, 66), (56, 52), (78, 46), (90, 32), (86, 12), (66, -2), (40, -2), (16, 10), (4, 34), (4, 60), (14, 80), (28, 88), (40, 84), (48, 76)])),
             L(outline([(6, 38), (26, 44), (30, 82), (12, 78)]), 'shade', 'b', False),
             L(ell(24, 82, 4.4, 4), 'band', 'f', ln=True)],
    'back': [L(outline([(14, 80), (10, 40), (20, 14), (42, 0), (62, 0), (84, 14), (92, 40), (88, 80), (68, 92), (32, 92)])),
             L(outline([(58, 4), (84, 16), (92, 46), (86, 78), (64, 90)]), 'shade', 'b', False),
             L(outline([(44, 90), (56, 90), (60, 108), (50, 124, 1), (40, 108)]), 'mid', 'f', ln=True),
             L(ell(50, 92, 5, 4), 'band', 'f', ln=True)],
}

# Sarit Charat: media melena castaña ondulada y abultada, con un flequillo largo que le tapa el ojo izquierdo y las puntas
# abiertas en ondas a los lados; piel muy clara, ojos verde amarillento y media sonrisa
CHARS['suchart'] = {
    'body': 'delgado', 'pal': pal('#4a3020', '#f8e0bc', shade='#34200e', iris='#9a9a2a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 106), (-6, 96, 1), (2, 82), (-4, 70, 1), (6, 58), (4, 36), (16, 10), (40, 0), (64, 2), (84, 14), (94, 36), (94, 58), (104, 70, 1),
                         (96, 82), (102, 96, 1), (86, 106), (82, 82), (80, 64), (20, 64), (18, 82)])),
              L(outline([(60, 4), (84, 16), (96, 44), (96, 96), (84, 84)]), 'shade', 'b', False),
              fringe([(86, 92), (90, 60), (86, 30), (66, 12), (40, 10), (20, 22), (14, 46), (16, 64), (24, 50), (34, 42), (44, 46), (48, 62), (52, 88), (62, 104, 1), (72, 96), (78, 104, 1)]),
              strand([(70, 30), (76, 70)], 'shade', 'f', 1.0), strand([(54, 20), (60, 80)], 'shade', 'f', 1.0)],
    'side': [L(outline([(52, 92), (56, 74), (60, 60), (80, 52), (92, 40), (88, 18), (66, 0), (36, -2), (14, 10), (2, 36), (-4, 64), (-10, 82, 1), (2, 86),
                        (-2, 98, 1), (14, 96), (20, 108, 1), (32, 98), (44, 110, 1)])),
             L(outline([(0, 40), (24, 46), (34, 96), (6, 92)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 18), (96, 42), (94, 66, 1), (86, 52), (80, 62, 1), (76, 44), (64, 30)])],
    'back': [L(outline([(8, 104), (-6, 96, 1), (2, 82), (-4, 70, 1), (4, 56), (4, 36), (16, 12), (40, 0), (64, 2), (86, 14), (96, 36), (96, 56), (104, 70, 1),
                        (98, 82), (104, 96, 1), (90, 104), (76, 100, 1), (64, 108), (50, 100, 1), (36, 108), (24, 100, 1)])),
             L(outline([(56, 4), (86, 14), (98, 50), (98, 100), (70, 104), (70, 50)]), 'shade', 'b', False),
             strand([(30, 30), (24, 70), (28, 98)], 'deep', 'b', 1.0), strand([(70, 30), (76, 70), (72, 98)], 'deep', 'b', 1.0)],
}

# Nawat Lam: pelo castaño oscuro en casco espeso, que le baja hasta las sienes, con la frente en pico; ojos grandes con el iris
# azul en espiral
CHARS['nawarat'] = {
    'body': 'normal', 'pal': pal('#3a2a14', '#d89c6c', shade='#281c0c', iris='#3a3aa8'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': [(12, 68), (24, 60), (38, 48), (50, 40), (62, 48), (76, 60), (88, 68)]},
    'front': [L(outline([(12, 76), (8, 40), (18, 12), (42, -4), (62, -4), (84, 10), (94, 38), (90, 76), (84, 66), (16, 66)])),
              L(outline([(60, 0), (86, 14), (94, 44), (88, 70), (78, 42)]), 'shade', 'b', False),
              L(ell(36, 76, 3, 3) + [ell(36, 76, 3, 3)[0]], (180, 190, 240, 255), 'f', False, False, 0.8),
              L(ell(64, 76, 3, 3) + [ell(64, 76, 3, 3)[0]], (180, 190, 240, 255), 'f', False, False, 0.8)],
    'side': [L(outline([(52, 68), (56, 54), (78, 46), (92, 30), (86, 8), (64, -6), (36, -6), (12, 8), (0, 34), (2, 62), (12, 86), (26, 96), (40, 88), (48, 78)])),
             L(outline([(2, 38), (26, 44), (30, 86), (10, 82)]), 'shade', 'b', False)],
    'back': [L(outline([(12, 84), (8, 40), (18, 12), (42, -4), (62, -4), (86, 12), (94, 40), (90, 84), (70, 96), (50, 100, 1), (30, 96)])),
             L(outline([(58, 0), (86, 14), (94, 46), (88, 82), (64, 94)]), 'shade', 'b', False)],
}

# Mei Chapati: melena larga y lisa castaño malva hasta el pecho, con raya en medio que deja la frente en pico y mechones junto
# a la cara; ojos afilados con pestañas y cejas gruesas
CHARS['mei'] = {
    'body': 'chica', 'pal': pal('#6a4a4e', '#d89a6c', shade='#523638', light='#8a6a70', iris='#2a1e1e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': [(12, 70), (26, 56), (40, 38), (50, 24), (60, 38), (74, 56), (88, 70)]},
    'front': [L(outline([(10, 116), (4, 90), (6, 50), (8, 24), (24, 2), (50, -6), (76, 2), (92, 24), (94, 50), (96, 90), (90, 116), (84, 96), (82, 64), (18, 64),
                         (16, 96)])),
              L(outline([(60, -2), (86, 12), (94, 46), (94, 110), (84, 96), (80, 40)]), 'shade', 'b', False),
              strand([(50, -4), (50, 22)], 'deep', 'b', 1.0),
              L(outline([(14, 66), (10, 100), (14, 112, 1), (20, 100), (20, 70)]), 'mid', 'f'),
              L(outline([(86, 66), (90, 100), (86, 112, 1), (80, 100), (80, 70)]), 'mid', 'f')],
    'side': [L(outline([(52, 70), (56, 56), (78, 50), (92, 36), (88, 12), (66, -6), (36, -6), (12, 8), (2, 36), (-4, 70), (-10, 110), (-16, 126, 1), (4, 116),
                        (20, 104), (34, 92), (46, 82)])),
             L(outline([(0, 40), (24, 46), (28, 96), (2, 110)]), 'shade', 'b', False),
             strand([(10, 50), (0, 100)], 'deep', 'b', 1.0),
             fringe([(64, 2), (88, 16), (94, 40), (94, 70), (90, 96, 1), (84, 66), (78, 42)])],
    'back': [L(outline([(6, 120), (2, 80), (4, 40), (16, 10), (50, -4), (84, 10), (96, 40), (98, 80), (94, 120), (72, 124), (50, 120), (28, 124)])),
             L(outline([(56, -2), (84, 10), (96, 46), (96, 118), (70, 120), (70, 50)]), 'shade', 'b', False),
             strand([(50, 0), (50, 116)], 'deep', 'b', 1.0)],
}

# Bark Sepakraw: una melena roja enorme de mechones en punta, más alta arriba y abierta en rizos de punta por los lados hasta
# la mandíbula; ojos verdes y cejas fruncidas
CHARS['bak'] = {
    'body': 'normal', 'pal': pal('#8a2a22', '#c08a5a', shade='#6a1c18', deep='#4e1410', iris='#1e8a6a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 100), (2, 104, 1), (6, 90), (-6, 84, 1), (4, 76), (-2, 64, 1), (10, 56), (6, 40), (12, 20), (14, 4, 1), (22, 6), (24, -16, 1), (34, -2),
                         (42, -26, 1), (50, -6), (60, -22, 1), (64, -4), (76, -14, 1), (78, 4), (92, 2, 1), (90, 20), (102, 30, 1), (94, 44), (98, 58, 1), (90, 64),
                         (104, 78, 1), (92, 84), (100, 100, 1), (86, 98), (84, 72), (16, 72)])),
              L(outline([(60, -2), (86, 8), (96, 46), (94, 92), (82, 66)]), 'shade', 'b', False),
              fringe([(12, 64), (14, 38), (28, 20), (50, 12), (72, 20), (86, 38), (88, 64), (80, 54), (74, 60, 1), (68, 46), (58, 56, 1), (54, 40), (46, 54, 1),
                      (40, 42), (32, 58, 1), (26, 46), (18, 60, 1)]),
              strand([(36, 18), (38, 40)], 'deep', 'f', 1.0), strand([(62, 18), (60, 40)], 'deep', 'f', 1.0)],
    'side': [L(outline([(56, 60), (62, 46), (84, 46), (94, 30), (90, 12), (98, -2, 1), (76, 0), (72, -20, 1), (56, -6), (44, -30, 1), (34, -6), (12, -18, 1),
                        (14, 4), (-10, 0, 1), (2, 18), (-18, 26, 1), (0, 36), (-16, 50, 1), (2, 56), (-12, 72, 1), (6, 74), (-2, 92, 1), (14, 86), (18, 104, 1),
                        (30, 90), (36, 104, 1), (44, 82), (50, 70)])),
             L(outline([(0, 36), (24, 42), (30, 84), (6, 80)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 16), (96, 40), (94, 62, 1), (86, 48), (80, 58, 1), (76, 40), (66, 28)])],
    'back': [L(outline([(14, 104), (0, 106, 1), (6, 90), (-8, 84, 1), (4, 74), (-6, 62, 1), (8, 54), (-2, 40, 1), (10, 32), (6, 14, 1), (20, 16), (22, -12, 1),
                        (34, 0), (42, -26, 1), (52, -6), (62, -22, 1), (66, -2), (80, -10, 1), (80, 8), (98, 6, 1), (92, 24), (106, 36, 1), (94, 48), (104, 62, 1),
                        (92, 70), (104, 86, 1), (90, 92), (96, 106, 1), (80, 104), (66, 112, 1), (56, 102), (44, 112, 1), (34, 102), (24, 112, 1)])),
             L(outline([(58, -2), (86, 10), (100, 50), (96, 102), (70, 108), (72, 50)]), 'shade', 'b', False),
             strand([(30, 20), (24, 60), (30, 100)], 'deep', 'b', 1.0), strand([(70, 20), (76, 60), (70, 100)], 'deep', 'b', 1.0)],
}

# Kaolan Sagot: calvo, de cabeza grande y orejas muy grandes, con arrugas en la frente; ojos rojos afilados y cejas gruesas
CHARS['kaolan'] = {
    'body': 'corpulento', 'pal': pal('#9a6a42', '#c08a5a', skin_d='#9a6a42', iris='#c82a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'hairline': False, 'big_ears': 4, 'ear_out': 6},
    'front': bald('front') + [L(quad((36, 34), (50, 30), (64, 34)), OUTC, 'f', False, False, 1.2), L(quad((28, 44), (32, 40), (36, 46)), OUTC, 'f', False, False, 1.1),
                              L(quad((64, 46), (68, 40), (72, 44)), OUTC, 'f', False, False, 1.1)],
    'side': bald('side') + [L(quad((70, 30), (78, 28), (84, 34)), OUTC, 'f', False, False, 1.1)],
    'back': bald('back'),
}

# Thamgan Jaa: pelo azul marino peinado hacia atrás con dos puntas como cuernos arriba y la frente en pico, y una coleta baja
# abultada que le cae por detrás; ojos afilados, cejas fruncidas y sonrisa de dientes
CHARS['thanakorn-jaa'] = {
    'body': 'normal', 'pal': pal('#1a3a5a', '#b07448', shade='#102840', light='#3a6a9a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98,
             'hairline': [(12, 62), (24, 50), (36, 44), (44, 50), (50, 40), (56, 50), (64, 44), (76, 50), (88, 62)]},
    'front': [L(outline([(84, 70), (100, 80), (106, 94), (94, 100), (84, 92)])),
              L(outline([(14, 66), (10, 36), (18, 12), (28, 4), (28, -8, 1), (36, 0), (50, -4), (64, 0), (72, -8, 1), (72, 4), (82, 12), (90, 36), (88, 66), (82, 56),
                         (18, 56)])),
              L(outline([(60, 2), (82, 14), (90, 42), (84, 60), (76, 36)]), 'shade', 'b', False),
              strand([(30, 10), (24, 44)], 'shade', 'b', 1.0), strand([(70, 10), (76, 44)], 'shade', 'b', 1.0), strand([(50, 0), (50, 34)], 'shade', 'b', 1.0)],
    'side': [L(outline([(54, 60), (60, 46), (80, 44), (92, 30), (86, 10), (66, -4), (60, -14, 1), (52, -6), (40, -6), (18, 4), (6, 24), (-8, 40), (-14, 70),
                        (-6, 90), (10, 100), (22, 94), (34, 80), (46, 72)])),
             L(outline([(-8, 44), (16, 46), (24, 86), (0, 92)]), 'shade', 'b', False),
             strand([(70, 10), (40, 6), (14, 20)], 'light', 'f', 1.0)],
    'back': [L(outline([(14, 70), (12, 30), (22, 8), (32, 2), (32, -8, 1), (40, -2), (60, -2), (68, -8, 1), (68, 2), (78, 8), (88, 30), (86, 70), (80, 90),
                        (68, 102), (50, 104), (34, 98), (24, 86)])),
             L(outline([(56, 0), (80, 10), (88, 40), (80, 88), (60, 100)]), 'shade', 'b', False),
             strand([(50, 4), (50, 60), (46, 98)], 'deep', 'b', 1.0)],
}

# Rasiree Saranyu (portera): melena larga castaño oscuro, ondulada y voluminosa hasta los hombros, peinada hacia atrás con la
# frente despejada y recogida atrás con un pasador rojo; ojos grandes verde azulado, cejas marcadas y labios
CHARS['rashiri-saran'] = {
    'body': 'chica', 'pal': pal('#3a2c1e', '#d8a070', shade='#281e14', iris='#2a9a8a', clip='#a8241e'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'lips', 'mouth_y': 100, 'hairline': (40, 22)},
    'front': [L(outline([(6, 112), (-8, 98, 1), (-4, 82), (-12, 66, 1), (-2, 52), (-6, 32), (4, 10), (20, -4), (50, -10), (80, -4), (96, 10), (106, 32), (102, 52),
                         (112, 66, 1), (104, 82), (108, 98, 1), (94, 112), (86, 84), (82, 60), (18, 60), (14, 84)])),
              L(outline([(60, -6), (86, 6), (104, 40), (104, 104), (88, 90), (84, 40)]), 'shade', 'b', False),
              strand([(24, 4), (14, 50), (6, 96)], 'deep', 'b', 1.0), strand([(76, 4), (86, 50), (94, 96)], 'deep', 'b', 1.0)],
    'side': [L(outline([(52, 66), (56, 52), (76, 40), (88, 22), (80, 4), (60, -8), (34, -8), (12, 4), (-2, 26), (-10, 50), (-16, 80), (-10, 104), (-2, 118, 1), (12, 110),
                        (26, 118, 1), (34, 100), (42, 86), (48, 76)])),
             L(outline([(-8, 50), (16, 52), (26, 100), (0, 106)]), 'shade', 'b', False),
             L(outline([(14, 20), (24, 14), (28, 26), (18, 30)]), 'clip', 'f', ln=True)],
    'back': [L(outline([(4, 112), (-10, 96, 1), (-6, 80), (-12, 62, 1), (-4, 48), (-4, 26), (10, 6), (50, -8), (90, 6), (104, 26), (104, 48), (112, 62, 1), (106, 80),
                        (110, 96, 1), (96, 112), (80, 118, 1), (66, 110), (50, 120, 1), (34, 110), (20, 118, 1)])),
             L(outline([(56, -6), (88, 6), (104, 46), (104, 108), (70, 114), (72, 50)]), 'shade', 'b', False),
             L(outline([(32, 30), (68, 30), (66, 42), (34, 42)]), 'clip', 'f', ln=True)],
}
