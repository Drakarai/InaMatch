"""Academia West Manor (vr-nishinomiya): el Nishinomiya de Victory Road, con sus modelos 3D de la enciclopedia
(英雄たちのヴィクトリーロード). Son todos personajes nuevos de VR, con una sola forma."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars_vr_nikogawa import BROWN_LINE, blush, brow_side, brows, cat_mouth, crop, ring_glasses
from heads import quad  # noqa: F401

WHITE = (248, 248, 248, 255)


def rect(view, y=76, c=OUTC, w=1.6, x0=22, x1=46, h0=6, h1=5):
    """Gafas rectangulares (de frente, los dos cristales y el puente; de perfil, un cristal y la patilla)."""
    if view == 'front':
        return [L([(x0, y - h0), (x1, y - h0), (x1, y + h1), (x0 + 1, y + h1), (x0, y - h0)], c, 'f', False, False, w),
                L([(100 - x0, y - h0), (100 - x1, y - h0), (100 - x1, y + h1), (99 - x0, y + h1), (100 - x0, y - h0)], c, 'f', False, False, w),
                L([(x1, y - 2), (100 - x1, y - 2)], c, 'f', False, False, w * 0.8)]
    if view == 'side':
        return [L([(78, y - h0), (90, y - h0), (90, y + h1), (79, y + h1), (78, y - h0)], c, 'f', False, False, w), L([(50, y - 3), (78, y - 3)], c, 'f', False, False, w * 0.8)]
    return []


def worried(y=62, c=OUTC, w=2.0):
    """Cejas de preocupación: la punta de dentro más alta."""
    return [L(quad((24, y + 3), (32, y + 1), (43, y - 3)), c, 'f', False, False, w), L(quad((76, y + 3), (68, y + 1), (57, y - 3)), c, 'f', False, False, w)]


# Dax Prescott (Konomachi Kiryou, portero): un tupé negro enorme de pinchos revueltos que sale hacia arriba y a los lados; la
# frente despejada, cejas de preocupación, ojos grises redondos con ojeras y media sonrisa
CHARS['dax-prescott'] = {
    'body': 'normal', 'pal': pal('#262a28', '#fccca4', iris='#8a9aa4', shade='#1c201e', deep='#121414'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 94,
             'hairline': [(15, 60), (18, 42), (30, 36), (50, 34), (70, 36), (82, 42), (85, 60)]},
    'front': [L(outline([(16, 62), (12, 42), (4, 34, 1), (10, 22), (-8, 8, 1), (8, 0), (2, -22, 1), (22, -14), (24, -38, 1), (40, -22), (52, -44, 1), (60, -24),
                         (80, -38, 1), (78, -16), (98, -14, 1), (88, 4), (106, 14, 1), (90, 24), (98, 38, 1), (86, 40), (84, 62), (80, 46), (20, 46)])),
              L(outline([(56, -22), (80, -36), (78, -14), (98, -12), (88, 6), (104, 16), (90, 26), (96, 38), (84, 40), (76, 16)]), 'shade', 'b', False),
              strand([(30, -10), (40, 10), (36, 30)], 'deep', 'b', 1.0), strand([(56, -18), (58, 6), (66, 26)], 'deep', 'b', 1.0)]
             + worried(60)
             + [L([(30, 85), (32, 86)], OUTC, 'f', False, False, 1.2), L([(70, 85), (68, 86)], OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(66, 52), (78, 42), (86, 30), (96, 22, 1), (88, 12), (104, 0, 1), (86, -8), (94, -26, 1), (72, -22), (70, -42, 1), (50, -26), (36, -40, 1),
                        (28, -20), (6, -24, 1), (12, -8), (-12, -2, 1), (4, 10), (-6, 26, 1), (6, 34), (4, 56), (12, 76), (24, 92), (34, 86), (38, 66), (46, 58),
                        (56, 56)])),
             L(outline([(4, 34), (30, 40), (44, 58), (36, 66), (34, 86), (24, 92), (12, 76)]), 'shade', 'b', False),
             L(quad((72, 62), (78, 60), (85, 56)), OUTC, 'f', False, False, 2.0)],
    'back': [L(outline([(18, 76), (12, 50), (6, 30, 1), (12, 18), (-6, 2, 1), (10, -4), (4, -26, 1), (24, -16), (28, -40, 1), (42, -24), (54, -44, 1), (62, -24), (82, -38, 1),
                        (80, -16), (100, -14, 1), (90, 4), (106, 16, 1), (92, 26), (96, 40, 1), (88, 50), (82, 76), (66, 90), (50, 94, 1), (34, 90)])),
             L(outline([(58, -20), (82, -36), (80, -14), (100, -12), (90, 6), (104, 18), (92, 28), (94, 40), (86, 52), (82, 76), (66, 90), (60, 40)]), 'shade', 'b', False)],
}

# Edvan Trodden (Jimichi Susumi): pelo granate de longitud media con las puntas de los lados abiertas en pinchos hacia fuera
# y un flequillo largo que le tapa el ojo derecho y baja hasta la mejilla; ojo grande con sombra morada, boca nerviosa
CHARS['edvan-trodden'] = {
    'body': 'normal', 'pal': pal('#7a3a52', '#fcd2b0', iris='#2a2a2a', shade='#622e42', deep='#4a2232'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'frown', 'mouth_y': 95,
             'hairline': [(15, 60), (18, 46), (30, 40), (50, 38), (70, 40), (82, 46), (85, 60)]},
    'front': [L(outline([(16, 72), (12, 48), (-6, 42, 1), (8, 34), (-10, 22, 1), (10, 16), (4, 6, 1), (22, 2), (38, -10), (62, -10), (78, 2), (96, 6, 1), (90, 16),
                         (108, 22, 1), (92, 34), (104, 42, 1), (88, 48), (84, 72), (80, 52), (20, 52)])),
              L(outline([(60, -6), (80, 4), (94, 8), (90, 18), (104, 24), (92, 34), (100, 42), (86, 50), (78, 30)]), 'shade', 'b', False),
              L(quad((62, 70), (66, 66), (74, 70)), (170, 130, 200, 255), 'f', False, False, 2.4),
              L(outline([(14, 50), (22, 30), (40, 22), (56, 26), (60, 40), (54, 62), (48, 92, 1), (42, 72), (32, 86, 1), (30, 66), (20, 72, 1), (18, 58)]), 'mid', 'f'),
              strand([(40, 28), (46, 50), (46, 80)], 'deep', 'f', 1.0), strand([(28, 36), (30, 60)], 'deep', 'f', 1.0),
              L(quad((58, 64), (66, 60), (74, 64)), OUTC, 'f', False, False, 1.8)],
    'side': [L(outline([(76, 52), (88, 44), (96, 24), (88, 6), (66, -10), (40, -10), (20, 0), (-2, 6, 1), (8, 18), (-12, 26, 1), (6, 40), (14, 62), (24, 84), (34, 92, 1),
                        (38, 70), (46, 60), (58, 58), (70, 62), (78, 80, 1), (80, 60)])),
             L(outline([(4, 40), (34, 44), (44, 60), (38, 70), (34, 90), (24, 84), (14, 62)]), 'shade', 'b', False)],
    'back': [L(outline([(20, 80), (12, 50), (-6, 42, 1), (8, 34), (-10, 22, 1), (10, 16), (4, 6, 1), (22, 2), (38, -10), (62, -10), (78, 2), (96, 6, 1), (90, 16),
                        (108, 22, 1), (92, 34), (104, 42, 1), (88, 50), (80, 80), (62, 88), (52, 100, 1), (44, 88)])),
             L(outline([(56, -6), (80, 4), (94, 8), (90, 18), (104, 24), (92, 34), (100, 42), (86, 52), (80, 80), (62, 88), (56, 40)]), 'shade', 'b', False)],
}

# Drever Olflaire (Karunori Katsuki): piel tostada; pelo negro revuelto en mechones gruesos, con un pico que se levanta por
# detrás y mechones que le caen por la cara entre los ojos; ojos amarillos entornados y sonrisa torcida de dientes
CHARS['drever-olflaire'] = {
    'body': 'normal', 'pal': pal('#222a2a', '#c48c5e', iris='#c8a838', shade='#1a2020', deep='#101414'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(14, 68), (10, 44), (-4, 38, 1), (6, 28), (-6, 12, 1), (10, 8), (12, -6), (26, -16), (36, -12), (50, -20), (70, -14), (84, -6), (92, 8), (106, 12, 1),
                         (92, 22), (98, 38, 1), (88, 44), (86, 68), (80, 54), (20, 54)])),
              L(outline([(58, -14), (82, -4), (92, 10), (100, 14), (92, 24), (94, 38), (86, 46), (78, 22)]), 'shade', 'b', False),
              L(outline([(14, 60), (16, 36), (28, 26), (50, 22), (72, 26), (84, 36), (86, 60), (80, 50), (72, 58, 1), (66, 48), (56, 54), (52, 84, 1), (46, 56), (40, 66, 1),
                         (34, 50), (24, 56, 1), (20, 50)]), 'mid', 'f'),
              strand([(48, 26), (50, 52), (52, 80)], 'deep', 'f', 1.0), strand([(30, 30), (34, 48)], 'deep', 'f', 1.0), strand([(70, 30), (68, 48)], 'deep', 'f', 1.0)],
    'side': [L(outline([(70, 52), (82, 46), (90, 56), (92, 74, 1), (92, 50), (94, 30), (88, 10), (70, -6), (46, -12), (22, -14), (-6, -14, 1), (12, -4), (2, 10), (-12, 18, 1),
                        (4, 28), (4, 56), (14, 76), (26, 90), (36, 84), (38, 66), (46, 58), (58, 56)])),
             L(outline([(4, 30), (32, 40), (44, 58), (36, 66), (36, 84), (26, 90), (14, 76)]), 'shade', 'b', False)],
    'back': [L(outline([(18, 80), (12, 50), (-4, 40, 1), (8, 30), (-6, 12, 1), (10, 6), (14, -8), (28, -16), (50, -18), (72, -16), (86, -8), (92, 6), (110, -6, 1), (96, 16),
                        (104, 32, 1), (90, 40), (88, 52), (82, 80), (66, 90), (50, 94), (34, 90)])),
             L(outline([(58, -14), (84, -6), (92, 8), (106, -2), (96, 18), (100, 32), (88, 44), (82, 80), (66, 90), (60, 40)]), 'shade', 'b', False)],
}

# Looke Raundoff (Marume Mami): melena corta redonda castaño anaranjado hasta la mandíbula, con flequillo de lado; gafas
# redondas grises de montura fina, ojos azules grandes y sonrisa
CHARS['looke-raundoff'] = {
    'body': 'chica', 'pal': pal('#b8603a', '#fcd8bc', iris='#2a4a8a', shade='#9a4c2c', deep='#7a3a20'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'hairline': False},
    'front': [L(outline([(10, 104, 1), (6, 70), (6, 36), (18, 10), (50, 0), (82, 10), (94, 36), (94, 70), (90, 104, 1), (82, 98), (80, 60), (20, 60), (18, 98)])),
              L(outline([(60, 4), (86, 16), (94, 40), (92, 100), (84, 96), (82, 50)]), 'shade', 'b', False),
              L(outline([(16, 72), (16, 40), (28, 22), (50, 16), (72, 22), (84, 40), (84, 70), (78, 60), (70, 52), (56, 50), (44, 54), (34, 64, 1), (32, 52), (22, 62)]), 'mid', 'f'),
              strand([(28, 30), (40, 40), (50, 48)], 'deep', 'f', 1.0)]
             + ring_glasses('front', 77, (150, 150, 150, 255), 1.6, 9.5, 8, 14) + blush(87),
    'side': [L(outline([(80, 50), (90, 40), (90, 20), (76, 2), (50, -4), (24, 2), (8, 20), (2, 50), (4, 80), (14, 100, 1), (30, 96), (46, 92), (52, 100, 1), (56, 80),
                        (58, 62), (70, 58)])),
             L(outline([(2, 46), (30, 46), (50, 66), (50, 92), (30, 96), (14, 98)]), 'shade', 'b', False)]
            + ring_glasses('side', 77, (150, 150, 150, 255), 1.6, 5, 8),
    'back': [L(outline([(8, 104, 1), (4, 70), (4, 36), (16, 10), (50, 0), (84, 10), (96, 36), (96, 70), (92, 104, 1), (70, 100), (50, 104), (30, 100)])),
             L(outline([(56, 4), (84, 12), (96, 38), (96, 70), (92, 102), (66, 100), (60, 50)]), 'shade', 'b', False)],
}

# Rutheo Wheyston (Shiraishi Michio): una mata enorme de pelo morado azulado ondulado, muy ancha y alta, que le cae hasta
# las cejas; gafas negras rectangulares, ojos verdes y boca fruncida
CHARS['rutheo-wheyston'] = {
    'body': 'normal', 'pal': pal('#4c4c9c', '#fcd8b4', iris='#4a7a6a', shade='#3a3a80', deep='#2a2a60'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'frown', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(16, 70), (10, 56), (0, 44), (-4, 26), (2, 6), (16, -12), (36, -22), (60, -22), (82, -12), (96, 4), (102, 26), (98, 44), (88, 56), (84, 70),
                         (80, 62), (66, 64), (54, 60), (42, 66), (24, 64)])),
              L(outline([(58, -18), (84, -8), (98, 10), (100, 30), (92, 50), (80, 58), (82, 24)]), 'shade', 'b', False),
              strand([(26, -6), (18, 14), (24, 34), (14, 50)], 'deep', 'b', 1.0), strand([(50, -14), (44, 6), (52, 26), (46, 46)], 'deep', 'b', 1.0),
              strand([(74, -6), (80, 16), (74, 36)], 'deep', 'b', 1.0), L(quad((34, 8), (46, 0), (58, 6)), 'light', 'b', False, False, 1.6)]
             + rect('front', 76, (26, 26, 30, 255), 2.2, 22, 46, 5, 5),
    'side': [L(outline([(78, 58), (90, 50), (98, 30), (96, 6), (80, -14), (52, -24), (22, -18), (2, -2), (-8, 24), (-4, 48), (6, 64), (20, 84), (34, 88), (38, 68),
                        (46, 60), (60, 60)])),
             L(outline([(-4, 30), (30, 38), (46, 60), (38, 68), (34, 86), (20, 84), (4, 62)]), 'shade', 'b', False),
             strand([(30, -12), (40, 12), (34, 34)], 'deep', 'b', 1.0), strand([(64, -14), (72, 10), (66, 30)], 'deep', 'b', 1.0)]
            + rect('side', 76, (26, 26, 30, 255), 2.2),
    'back': [L(outline([(18, 76), (8, 56), (-2, 40), (-4, 20), (6, 0), (22, -16), (50, -22), (78, -16), (94, 0), (104, 20), (102, 40), (92, 56), (82, 76), (66, 88),
                        (50, 90), (34, 88)])),
             L(outline([(58, -18), (82, -10), (98, 6), (102, 34), (92, 56), (82, 76), (66, 88), (60, 40)]), 'shade', 'b', False),
             strand([(30, -10), (24, 14), (32, 40)], 'deep', 'b', 1.0), strand([(66, -8), (72, 20)], 'deep', 'b', 1.0)],
}

# Ernesta Beauregard (Majime Naoko): melena granate muy oscura, con mucho volumen arriba (como un moño alto) y larguísima por
# detrás, flequillo recto bajo que le tapa las cejas y mechones a los lados de la cara; ojos rojos y colorete
CHARS['ernesta-beauregard'] = {
    'body': 'chica', 'pal': pal('#5e2840', '#fcdcc4', iris='#a8243c', shade='#4a1e32', deep='#341424'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'hairline': False, 'eye_y': 77},
    'front': [L(outline([(-4, 116, 1), (0, 70), (2, 34), (14, 10), (22, -10), (36, -20), (50, -22), (64, -20), (78, -10), (86, 10), (98, 34), (100, 70), (104, 116, 1),
                         (82, 114), (80, 62), (20, 62), (18, 114)])),
              L(outline([(58, -18), (78, -8), (88, 12), (98, 36), (100, 112), (84, 110), (82, 50)]), 'shade', 'b', False),
              L(quad((24, 12), (50, 4), (76, 12)), 'deep', 'b', False, False, 1.4),
              L(quad((14, 36), (50, 20), (86, 36)), (30, 20, 30, 255), 'f', False, False, 3.2),
              L(outline([(16, 76), (16, 40), (28, 24), (50, 18), (72, 24), (84, 40), (84, 76), (80, 66), (66, 66), (50, 66), (34, 66), (20, 66)]), 'mid', 'f'),
              L(outline([(16, 66), (22, 40), (26, 40), (22, 112)]), 'shade', 'f', False), L(outline([(84, 66), (78, 40), (74, 40), (78, 112)]), 'shade', 'f', False),
              L(quad((32, 30), (50, 24), (68, 30)), 'light', 'f', False, False, 1.4)]
             + blush(86),
    'side': [L(outline([(84, 66), (90, 44), (86, 20), (74, -10), (50, -24), (26, -18), (10, 0), (2, 24), (-8, 50), (-20, 90), (-12, 124, 1), (8, 110), (20, 124, 1),
                        (30, 100), (40, 80), (56, 64), (72, 62), (76, 70)])),
             L(outline([(2, 30), (24, 30), (40, 74), (20, 120), (-14, 120)]), 'shade', 'b', False),
             L(outline([(72, 64), (90, 66), (92, 44), (82, 32)]), 'mid', 'f')],
    'back': [L(outline([(-6, 118, 1), (-2, 70), (2, 34), (16, 8), (26, -12), (50, -22), (74, -12), (84, 8), (98, 34), (102, 70), (106, 118, 1), (80, 122), (50, 124), (20, 122)])),
             L(outline([(56, -18), (76, -10), (86, 10), (98, 36), (102, 70), (106, 116), (64, 122), (58, 50)]), 'shade', 'b', False),
             L(quad((24, 10), (50, 2), (76, 10)), 'deep', 'b', False, False, 1.4)],
}

# Laymark Starwyn (Kinboshi Yatsuru): pelo melocotón muy claro en casco redondo, con el flequillo largo peinado hacia su
# izquierda que le tapa la frente hasta los ojos; gafas plateadas rectangulares y ojos rojizos; bajito
CHARS['laymark-starwyn'] = {
    'body': 'bajito', 'pal': pal('#f2caa2', '#fcd8bc', iris='#a03040', shade='#d8a882', deep='#b88a68'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'frown', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(14, 84), (8, 50), (8, 26), (20, 4), (50, -6), (80, 4), (92, 26), (92, 50), (86, 84), (82, 70), (18, 70)])),
              L(outline([(60, -2), (84, 8), (92, 30), (90, 60), (84, 80), (80, 40)]), 'shade', 'b', False),
              L(outline([(12, 78, 1), (14, 46), (26, 26), (50, 18), (72, 24), (86, 40), (88, 72, 1), (80, 64), (72, 72, 1), (66, 58), (56, 66, 1), (48, 54), (38, 60, 1),
                         (32, 50), (22, 62, 1), (18, 56)]), 'mid', 'f'),
              strand([(46, 6), (30, 30), (24, 54)], 'deep', 'f', 1.0), strand([(56, 10), (62, 34), (70, 56)], 'deep', 'f', 1.0),
              strand([(52, 4), (50, 30), (52, 52)], 'shade', 'f', 1.0)]
             + rect('front', 78, (176, 180, 190, 255), 1.8, 22, 46, 5, 5),
    'side': [L(outline([(76, 60), (88, 54), (94, 34), (88, 12), (68, -4), (40, -6), (18, 4), (4, 24), (2, 50), (8, 74), (20, 88), (34, 86), (38, 68), (46, 60), (60, 58),
                        (70, 70, 1)])),
             L(outline([(2, 40), (30, 46), (44, 60), (38, 68), (34, 86), (20, 88), (8, 74)]), 'shade', 'b', False),
             strand([(40, 0), (54, 24), (60, 48)], 'deep', 'b', 1.0)]
            + rect('side', 78, (176, 180, 190, 255), 1.8),
    'back': [L(outline([(16, 82), (8, 50), (8, 26), (20, 4), (50, -6), (80, 4), (92, 26), (92, 50), (84, 82), (66, 90), (50, 92), (34, 90)])),
             L(outline([(56, -2), (82, 8), (92, 30), (90, 56), (84, 82), (66, 90), (58, 40)]), 'shade', 'b', False),
             strand([(30, 50), (40, 60), (50, 54), (60, 62), (70, 52)], 'deep', 'b', 1.0)],
}

# Moby Tidbitt (Mobunari Kako): pelo rosa malva con un pico en la frente y dos moñitos rizados a los lados, junto a las
# orejas; cara redonda, gafas redondas finas, ojos marrones, colorete y sonrisa de dientes
def _bunches(view):
    if view == 'front':
        return [L(outline([(16, 58), (2, 60, 1), (8, 68), (-2, 76, 1), (8, 82), (2, 92, 1), (16, 88), (20, 72)])),
                L(outline([(84, 58), (98, 60, 1), (92, 68), (102, 76, 1), (92, 82), (98, 92, 1), (84, 88), (80, 72)]))]
    if view == 'back':
        return [L(outline([(16, 60), (2, 62, 1), (8, 70), (-2, 78, 1), (8, 84), (4, 94, 1), (18, 90), (22, 74)]), 'shade'),
                L(outline([(84, 60), (98, 62, 1), (92, 70), (102, 78, 1), (92, 84), (96, 94, 1), (82, 90), (78, 74)]), 'shade')]
    return [L(outline([(20, 60), (6, 54, 1), (10, 66), (-2, 72, 1), (10, 80), (6, 90, 1), (22, 86), (30, 72)]))]


CHARS['moby-tidbitt'] = {
    'body': 'corpulento', 'pal': pal('#b8607a', '#fcd2aa', iris='#7a4a2a', shade='#9a4c64', deep='#7a3a4e'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'grin', 'mouth_y': 95,
             'hairline': [(15, 64), (18, 50), (32, 44), (44, 48), (50, 58), (56, 48), (68, 44), (82, 50), (85, 64)]},
    'front': _bunches('front') + crop('front', top=4, side=66, w=2)
             + ring_glasses('front', 77, (60, 40, 30, 255), 1.4, 9.5, 8, 14) + blush(88, (240, 140, 120, 255)),
    'side': _bunches('side') + crop('side', top=2, nape=86, w=2) + ring_glasses('side', 77, (60, 40, 30, 255), 1.4, 5, 8),
    'back': _bunches('back') + crop('back', top=4, nape=86, w=2),
}

# Edgard Loathe (Itoi Kou): pelo azul marino con raya a un lado y un mechón largo que cae en medio de la cara; dos mechones
# finísimos que bajan desde las sienes hasta la barbilla y se rizan hacia fuera, y una antena en lo alto; ojos grises
# afilados, ceño fruncido
CHARS['edgard-loathe'] = {
    'body': 'normal', 'pal': pal('#1e2a6a', '#fcd8bc', iris='#7a8a9a', shade='#162054', deep='#0e1640'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 70), (10, 44), (14, 16), (30, -2), (50, -8), (72, -2), (88, 16), (92, 44), (86, 70), (80, 52), (20, 52)])),
              L(outline([(60, -4), (84, 10), (92, 40), (86, 66), (78, 30)]), 'shade', 'b', False),
              L(quad((28, -6), (40, -24), (60, -18)), 'mid', 'b', False, False, 2.0),
              L(outline([(14, 54), (16, 30), (30, 16), (50, 10), (74, 16), (86, 32), (86, 56), (76, 44), (60, 40), (52, 58), (50, 82, 1), (46, 58), (36, 44), (24, 50)]), 'mid', 'f'),
              strand([(52, 16), (50, 40), (50, 74)], 'deep', 'f', 1.0),
              L(quad((18, 54), (16, 82), (20, 98)) + quad((20, 98), (12, 104), (6, 100))[1:], 'mid', 'f', False, False, 1.6),
              L(quad((82, 54), (84, 82), (80, 98)) + quad((80, 98), (88, 104), (94, 100))[1:], 'mid', 'f', False, False, 1.6)],
    'side': [L(outline([(70, 52), (82, 46), (90, 30), (86, 8), (66, -8), (40, -10), (18, 0), (4, 22), (2, 50), (6, 80), (12, 98, 1), (22, 86), (34, 80), (38, 66), (46, 58),
                        (58, 56)])),
             L(outline([(2, 40), (30, 44), (44, 58), (36, 66), (32, 82), (16, 92), (6, 70)]), 'shade', 'b', False),
             L(quad((46, -8), (58, -28), (74, -20)), 'mid', 'b', False, False, 2.0),
             L(quad((84, 30), (92, 50), (90, 72)), 'mid', 'f', False, False, 3.0),
             L(quad((76, 56), (78, 84), (74, 98)) + quad((74, 98), (82, 104), (88, 100))[1:], 'mid', 'f', False, False, 1.6)],
    'back': [L(outline([(18, 82), (10, 50), (14, 18), (30, 0), (50, -6), (70, 0), (86, 18), (90, 50), (82, 82), (66, 90), (50, 92), (34, 90)])),
             L(outline([(58, -2), (82, 14), (90, 48), (82, 82), (66, 90), (60, 40)]), 'shade', 'b', False),
             L(quad((32, -4), (50, -26), (70, -14)), 'mid', 'b', False, False, 2.0),
             L(quad((16, 60), (14, 84), (18, 96)) + quad((18, 96), (10, 100), (4, 96))[1:], 'mid', 'b', False, False, 1.6),
             L(quad((84, 60), (86, 84), (82, 96)) + quad((82, 96), (90, 100), (96, 96))[1:], 'mid', 'b', False, False, 1.6)],
}

# Flanko Midspringle (Shikachi Ousuke): un afro enorme verde oliva oscuro, de bultos, con una cinta verde menta en la frente;
# ojos negros entornados, colorete, nariz rosada y sonrisa
MINT = (90, 208, 176, 255)


def _afro(cx, cy, rx, ry, n=11):
    import math
    pts = []
    for i in range(n * 2):
        a = math.pi * 2 * i / (n * 2)
        k = 1.0 if i % 2 == 0 else 0.9
        pts.append((cx + rx * k * math.cos(a), cy + ry * k * math.sin(a)))
    return blob(pts, 6)


CHARS['flanko-midspringle'] = {
    'body': 'normal', 'pal': pal('#4a4a2c', '#eab48e', iris='#1e1e1e', shade='#3a3a22', deep='#2a2a18'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'nose': (50, 86, 2.4),
             'hairline': [(15, 64), (18, 56), (50, 54), (82, 56), (85, 64)]},
    'front': [L(_afro(50, 22, 56, 44, 12)), L(outline([(60, -16), (92, 4), (104, 30), (96, 56), (82, 54), (84, 20)]), 'shade', 'b', False),
              L(outline([(14, 50), (24, 40), (50, 36), (76, 40), (86, 50), (86, 58), (76, 50), (50, 46), (24, 50), (14, 58)]), MINT, 'f'),
              L(quad((32, 64), (38, 62), (44, 64)), OUTC, 'f', False, False, 1.6), L(quad((56, 64), (62, 62), (68, 64)), OUTC, 'f', False, False, 1.6)]
             + blush(87),
    'side': [L(_afro(40, 26, 54, 46, 12)), L(outline([(-12, 30), (30, 40), (60, 70), (20, 70), (-4, 56)]), 'shade', 'b', False),
             L(outline([(62, 44), (84, 42), (90, 50), (86, 56), (62, 54)]), MINT, 'f')],
    'back': [L(_afro(50, 26, 56, 50, 12)), L(outline([(58, -14), (94, 6), (104, 34), (96, 64), (70, 76), (60, 40)]), 'shade', 'b', False),
             L(outline([(24, 66), (76, 66), (68, 86), (50, 90), (32, 86)]), 'deep', 'b', False)],
}

# Berdy Caster (Manabiya Dento): pelo azul petróleo muy oscuro, redondeado y abultado arriba, con un rizo suelto a un lado y
# mechones que le enmarcan la cara hasta la mandíbula; gafas negras finas, ojos azules y sonrisa de dientes
CHARS['berdy-caster'] = {
    'body': 'normal', 'pal': pal('#1e3a50', '#fcd2b0', iris='#3a8ac0', shade='#162c3e', deep='#0e1e2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(16, 96, 1), (10, 60), (2, 54), (-6, 60, 1), (2, 48), (8, 30), (20, 6), (46, -6), (72, -2), (88, 16), (96, 40), (90, 64), (84, 96, 1), (80, 70),
                         (20, 70)])),
              L(outline([(60, -2), (86, 14), (96, 40), (88, 66), (82, 30)]), 'shade', 'b', False),
              L(outline([(14, 70), (16, 40), (30, 24), (50, 20), (72, 24), (86, 40), (86, 70), (80, 52), (66, 44), (50, 50), (38, 46), (28, 54), (20, 64)]), 'mid', 'f'),
              strand([(40, 26), (36, 44)], 'deep', 'f', 1.0), strand([(62, 26), (66, 42)], 'deep', 'f', 1.0)]
             + rect('front', 77, (24, 24, 28, 255), 1.4, 23, 45, 5, 5),
    'side': [L(outline([(70, 56), (82, 50), (92, 36), (88, 12), (68, -4), (42, -6), (18, 4), (4, 24), (0, 50), (-8, 56, 1), (4, 62), (12, 80), (26, 92), (36, 88),
                        (38, 68), (48, 60), (60, 60), (66, 84, 1), (72, 66)])),
             L(outline([(0, 44), (30, 48), (46, 60), (38, 68), (36, 88), (26, 92), (12, 80)]), 'shade', 'b', False)]
            + rect('side', 77, (24, 24, 28, 255), 1.4),
    'back': [L(outline([(18, 84), (10, 52), (8, 30), (20, 6), (50, -6), (80, 6), (92, 30), (92, 52), (104, 56, 1), (90, 60), (82, 84), (66, 92), (50, 94), (34, 92)])),
             L(outline([(58, -2), (82, 8), (92, 30), (92, 54), (82, 84), (66, 92), (60, 40)]), 'shade', 'b', False)],
}

# Chicory Bellflower (Henmi Kikyou): pelo lila ondulado con pico en la frente y dos moños grandes y bajos a los lados del
# cuello; ojos morados, boca seria
LILAC_D = (140, 118, 160, 255)
CHARS['chicory-bellflower'] = {
    'body': 'chica', 'pal': pal('#b0a0d0', '#fcd8bc', iris='#4a3a6a', shade='#9484b4', deep='#76689a'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'line', 'mouth_y': 94,
             'hairline': [(15, 64), (18, 48), (30, 40), (44, 38), (50, 46), (56, 38), (70, 40), (82, 48), (85, 64)]},
    'front': [L(blob([(-6, 84), (0, 72), (14, 70), (22, 82), (18, 98), (4, 100), (-4, 94)], 6)), L(blob([(106, 84), (100, 72), (86, 70), (78, 82), (82, 98), (96, 100), (104, 94)], 6)),
              L(blob([(-4, 92), (6, 98), (18, 96), (12, 100), (0, 100)], 4), LILAC_D, 'b', False), L(blob([(104, 92), (94, 98), (82, 96), (88, 100), (100, 100)], 4), LILAC_D, 'b', False),
              L(outline([(16, 72), (6, 50), (4, 24), (16, 4), (34, -6), (50, -4), (66, -6), (84, 4), (96, 24), (94, 50), (84, 72), (80, 52), (20, 52)])),
              L(outline([(60, -4), (84, 6), (96, 26), (92, 52), (84, 66), (80, 30)]), 'shade', 'b', False),
              strand([(20, 20), (14, 36), (20, 52)], 'deep', 'b', 1.0), strand([(80, 20), (86, 36), (80, 52)], 'deep', 'b', 1.0)],
    'side': [L(blob([(10, 70), (26, 66), (34, 80), (28, 96), (12, 100), (2, 88)], 6)), L(blob([(4, 92), (16, 100), (28, 96), (20, 104), (6, 102)], 4), LILAC_D, 'b', False),
             L(outline([(72, 50), (84, 44), (94, 28), (88, 6), (66, -6), (40, -8), (16, 2), (2, 24), (0, 48), (8, 66), (22, 70), (36, 72), (40, 62), (48, 56), (60, 54)])),
             L(outline([(0, 40), (30, 44), (44, 56), (36, 70), (8, 66)]), 'shade', 'b', False), strand([(70, 6), (84, 28)], 'deep', 'b', 1.0)],
    'back': [L(outline([(16, 74), (6, 50), (4, 24), (16, 4), (50, -6), (84, 4), (96, 24), (94, 50), (84, 74), (50, 80)])),
             L(outline([(56, -4), (84, 6), (96, 26), (94, 50), (84, 74), (60, 78)]), 'shade', 'b', False),
             L(blob([(-8, 76), (2, 64), (20, 64), (30, 76), (24, 94), (6, 96), (-6, 90)], 6)), L(blob([(108, 76), (98, 64), (80, 64), (70, 76), (76, 94), (94, 96), (106, 90)], 6)),
             L(blob([(-6, 86), (10, 92), (26, 88), (20, 96), (2, 96)], 4), LILAC_D, 'b', False), L(blob([(106, 86), (90, 92), (74, 88), (80, 96), (98, 96)], 4), LILAC_D, 'b', False)],
}

# Aysen Demacon (Tsugino Ace): pelo rubio pajizo ondulado hasta los hombros, recogido arriba en un moño-copete con una goma
# negra; ojos cerrados de sonrisa y boquita sonriente
KHAKI_D = (176, 140, 90, 255)
CHARS['aysen-demacon'] = {
    'body': 'bajito', 'pal': pal('#d4cc8c', '#fcd8bc', iris='#2a2a2a', shade='#b8ae70', deep='#968c56'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'smile', 'mouth_y': 93,
             'hairline': [(15, 70), (18, 54), (30, 48), (50, 46), (70, 48), (82, 54), (85, 70)]},
    'front': [L(outline([(36, 2), (34, -12), (40, -20, 1), (44, -14), (50, -24, 1), (56, -14), (62, -20, 1), (66, -10), (64, 2)]), 'shade'),
              L([(36, 2), (64, 2)], OUTC, 'f', False, False, 3.0),
              L(outline([(10, 100, 1), (8, 82), (0, 72, 1), (8, 64), (6, 40), (18, 12), (36, 2), (64, 2), (82, 12), (94, 40), (92, 64), (100, 72, 1), (92, 82), (90, 100, 1),
                         (82, 96), (80, 60), (20, 60), (18, 96)])),
              L(outline([(60, 4), (82, 14), (94, 42), (92, 96), (84, 92), (82, 50)]), 'shade', 'b', False),
              L(outline([(12, 100), (16, 88), (20, 98)]), KHAKI_D, 'b', False), L(outline([(88, 100), (84, 88), (80, 98)]), KHAKI_D, 'b', False),
              strand([(36, 8), (28, 30), (24, 48)], 'deep', 'b', 1.0), strand([(50, 4), (48, 30)], 'deep', 'b', 1.0), strand([(64, 8), (72, 30), (76, 48)], 'deep', 'b', 1.0)],
    'side': [L(outline([(42, 4), (30, -14), (18, -24, 1), (32, -26), (36, -18), (44, -12), (50, 0)]), 'shade'),
             L(outline([(76, 54), (88, 46), (92, 26), (82, 8), (56, 0), (30, 4), (12, 20), (4, 46), (0, 70), (6, 88), (18, 102, 1), (30, 92), (40, 98, 1), (42, 80),
                        (46, 62), (60, 58)])),
             L(outline([(2, 50), (30, 50), (46, 62), (40, 96), (18, 100), (4, 86)]), 'shade', 'b', False),
             L([(40, 2), (48, 0)], OUTC, 'f', False, False, 3.0),
             strand([(56, 4), (76, 16), (86, 32)], 'deep', 'b', 1.0), strand([(42, 8), (64, 22), (78, 40)], 'deep', 'b', 1.0)],
    'back': [L(outline([(36, 4), (34, -12), (40, -22, 1), (44, -14), (52, -26, 1), (58, -14), (64, -22, 1), (66, -10), (64, 4)]), 'shade'),
             L(outline([(10, 100, 1), (6, 80), (-2, 70, 1), (6, 62), (6, 40), (18, 14), (36, 4), (64, 4), (82, 14), (94, 40), (94, 62), (102, 70, 1), (94, 80), (90, 100, 1),
                        (76, 94), (62, 102, 1), (50, 94), (38, 102, 1), (24, 94)])),
             L(outline([(56, 6), (82, 14), (94, 40), (94, 80), (90, 100), (62, 100), (56, 50)]), 'shade', 'b', False),
             L([(36, 4), (64, 4)], OUTC, 'b', False, False, 3.0),
             strand([(30, 20), (24, 60)], 'deep', 'b', 1.0), strand([(50, 10), (50, 60)], 'deep', 'b', 1.0), strand([(70, 20), (76, 60)], 'deep', 'b', 1.0)],
}

# Breppo Terrey (Anba Touya): pelo rojo salmón en casco de champiñón que le tapa la frente hasta las cejas, con los lados
# bajando hasta las orejas; gafas amarillas rectangulares, ojos verdes y boquita apretada
YELLOW = (226, 196, 96, 255)
CHARS['breppo-terrey'] = {
    'body': 'normal', 'pal': pal('#e27272', '#fcdcc8', iris='#3a8a4a', shade='#c45a5a', deep='#a44646'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': [L(outline([(14, 86), (8, 66), (4, 44), (12, 14), (34, -2), (50, -4), (66, -2), (88, 14), (96, 44), (92, 66), (86, 86), (82, 68), (18, 68)])),
              L(outline([(60, 0), (86, 14), (96, 44), (90, 66), (84, 82), (80, 40)]), 'shade', 'b', False),
              L(outline([(10, 66), (14, 40), (30, 26), (50, 22), (70, 26), (86, 40), (90, 66), (80, 62), (66, 64), (50, 62), (34, 64), (20, 62)]), 'mid', 'f'),
              L(quad((16, 48), (50, 34), (84, 48)), 'deep', 'f', False, False, 1.0)]
             + rect('front', 78, YELLOW, 2.0, 22, 46, 6, 6) + cat_mouth(95, BROWN_LINE, 1.3),
    'side': [L(outline([(80, 64), (92, 60), (96, 40), (88, 12), (64, -4), (36, -4), (14, 8), (2, 30), (2, 56), (12, 74), (28, 80), (38, 74), (40, 64), (50, 66),
                        (54, 84, 1), (60, 68), (70, 66)])),
             L(outline([(2, 46), (30, 50), (50, 66), (38, 74), (28, 80), (12, 74)]), 'shade', 'b', False)]
            + rect('side', 78, YELLOW, 2.0, h0=6, h1=6),
    'back': [L(outline([(14, 78), (6, 56), (4, 34), (14, 10), (50, -4), (86, 10), (96, 34), (94, 56), (86, 78), (66, 84), (50, 86), (34, 84)])),
             L(outline([(56, 0), (86, 12), (96, 36), (94, 56), (86, 78), (60, 84), (52, 50)]), 'shade', 'b', False)],
}

# Frie Sorbet (Kimitake Aisu): pelo azul pizarra con flequillo de lado y dos moñitos bajos detrás de las orejas, de los que
# salen dos mechones finos curvados como antenas; ojos marrones grandes y cara pálida
CHARS['frie-sorbet'] = {
    'body': 'chica', 'pal': pal('#4a5a7a', '#fce6d8', iris='#7a4a2a', shade='#3a4864', deep='#2a344a'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'line', 'mouth_y': 94, 'hairline': False},
    'front': [L(ell(6, 60, 9, 9)), L(ell(94, 60, 9, 9)),
              L(quad((10, 56), (-6, 46), (-2, 56)), 'mid', 'b', False, False, 2.0), L(quad((90, 56), (106, 46), (102, 56)), 'mid', 'b', False, False, 2.0),
              L(quad((12, 70), (4, 86), (14, 100)), 'mid', 'f', False, False, 2.0), L(quad((88, 70), (96, 86), (86, 100)), 'mid', 'f', False, False, 2.0),
              L(outline([(16, 70), (10, 44), (14, 16), (30, -2), (50, -6), (70, -2), (86, 16), (90, 44), (84, 70), (80, 52), (20, 52)])),
              L(outline([(60, -2), (84, 12), (90, 40), (86, 66), (78, 30)]), 'shade', 'b', False),
              L(outline([(14, 60), (16, 34), (30, 18), (50, 14), (72, 18), (86, 34), (86, 58), (78, 46), (66, 50), (50, 48), (36, 52), (24, 58)]), 'mid', 'f'),
              strand([(36, 22), (50, 36), (70, 44)], 'deep', 'f', 1.0)],
    'side': [L(ell(22, 66, 10, 10)), L(quad((16, 60), (-4, 54), (-8, 62)), 'mid', 'b', False, False, 2.0), L(quad((18, 74), (4, 82), (8, 94)), 'mid', 'b', False, False, 2.0),
             L(outline([(72, 52), (84, 46), (92, 28), (86, 8), (66, -6), (40, -8), (18, 2), (4, 24), (2, 50), (10, 74), (24, 82), (36, 78), (40, 64), (48, 58), (60, 56)])),
             L(outline([(2, 40), (30, 44), (44, 58), (36, 76), (10, 72)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 76), (10, 48), (14, 18), (30, 0), (50, -6), (70, 0), (86, 18), (90, 48), (84, 76), (66, 84), (50, 86), (34, 84)])),
             L(outline([(58, -2), (82, 14), (90, 46), (84, 76), (66, 84), (60, 40)]), 'shade', 'b', False),
             L(ell(14, 64, 10, 10), 'shade'), L(ell(86, 64, 10, 10), 'shade'),
             L(quad((10, 58), (-6, 46), (-4, 56)), 'mid', 'b', False, False, 2.0), L(quad((90, 58), (106, 46), (104, 56)), 'mid', 'b', False, False, 2.0),
             L(quad((12, 72), (4, 88), (12, 100)), 'mid', 'b', False, False, 2.0), L(quad((88, 72), (96, 88), (88, 100)), 'mid', 'b', False, False, 2.0)],
}

# Eddi Losse (Tohou Kure, portero): pelo castaño corto y esponjoso con las puntas de los lados levantadas y un remolino;
# cascos blancos con orejeras grises; ojillos de punto, pecas y boquita en "o"
PHONE = (236, 236, 240, 255)
PHONE_D = (170, 160, 168, 255)
CHARS['eddi-losse'] = {
    'body': 'bajito', 'pal': pal('#8a6a4a', '#fcdcc4', iris='#2a2a2a', shade='#6e543a', deep='#54402c'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'none', 'hairline': False, 'eye_y': 78},
    'front': [L(outline([(14, 76), (2, 72, 1), (10, 64), (8, 40), (16, 14), (34, 0), (50, -4), (66, 0), (84, 14), (92, 40), (90, 64), (98, 72, 1), (86, 76), (82, 62), (18, 62)])),
              L(outline([(60, 0), (84, 14), (92, 40), (90, 64), (82, 60), (80, 30)]), 'shade', 'b', False),
              L(outline([(46, 0), (42, -12, 1), (50, -4), (56, -10, 1), (54, 2)]), 'mid', 'b'),
              L(outline([(14, 66), (16, 40), (28, 26), (50, 22), (72, 26), (84, 40), (86, 66), (78, 54), (66, 60, 1), (60, 52), (50, 58, 1), (42, 50), (32, 60, 1), (22, 54)]), 'mid', 'f'),
              L(quad((12, 70), (50, -18), (88, 70)), PHONE, 'f', False, False, 3.0),
              L(blob([(6, 70), (14, 66), (16, 80), (14, 92), (6, 92), (4, 80)], 5), PHONE, 'f', ln=True), L(blob([(94, 70), (86, 66), (84, 80), (86, 92), (94, 92), (96, 80)], 5), PHONE, 'f', ln=True),
              L(ell(9, 82, 2.4, 6), PHONE_D, 'f', False), L(ell(91, 82, 2.4, 6), PHONE_D, 'f', False),
              L(ell(50, 94, 1.8, 2.2), BROWN_LINE, 'f', False)]
             + [L(ell(x, y, 0.7, 0.7), (190, 120, 90, 255), 'f', False) for x, y in ((30, 86), (34, 88), (32, 84), (70, 86), (66, 88), (68, 84))],
    'side': [L(outline([(70, 52), (82, 46), (90, 30), (86, 10), (66, -4), (40, -6), (18, 4), (6, 24), (2, 50), (-8, 62, 1), (6, 66), (14, 80), (28, 86), (36, 80), (40, 64),
                        (48, 58), (60, 56)])),
             L(outline([(2, 42), (30, 46), (44, 58), (36, 80), (14, 80)]), 'shade', 'b', False),
             L(quad((54, 66), (44, 30), (40, -4)), PHONE, 'f', False, False, 3.4),
             L(ell(48, 72, 9, 10), PHONE_D, 'f', ln=True), L(ell(48, 72, 5.4, 6.4), (210, 200, 206, 255), 'f', False)],
    'back': [L(outline([(16, 80), (2, 74, 1), (10, 64), (8, 40), (16, 14), (50, -4), (84, 14), (92, 40), (90, 64), (98, 74, 1), (84, 80), (66, 86), (50, 88), (34, 86)])),
             L(outline([(56, 0), (84, 14), (92, 40), (90, 66), (84, 80), (60, 86), (54, 40)]), 'shade', 'b', False),
             L(outline([(48, 0), (44, -14, 1), (52, -6), (58, -12, 1), (56, 2)]), 'mid', 'b'),
             L(quad((12, 72), (50, -16), (88, 72)), PHONE, 'f', False, False, 3.0),
             L(blob([(6, 72), (14, 68), (16, 82), (14, 94), (6, 94), (4, 82)], 5), PHONE_D, 'f', ln=True), L(blob([(94, 72), (86, 68), (84, 82), (86, 94), (94, 94), (96, 82)], 5), PHONE_D, 'f', ln=True)],
}
