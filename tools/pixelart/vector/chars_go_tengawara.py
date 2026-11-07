"""Colegio Concertado Vía Láctea (go-tengawara): sus modelos 3D de Inazuma Eleven GO como referencia (busto de frente, perfil y
espalda)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from chars_alius import LONG_FACE, SKULL_F
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Starbuck Rogers (portero): tupé altísimo color crema sobre una cinta negra ancha que le tapa los ojos como un antifaz, y una
# melena rosa grisácea de puntas que le sale por detrás de las orejas; piel morena y sonrisa de dientes
CHARS['starbuck-rogers'] = {
    'body': 'normal', 'pal': pal('#f0e8cc', '#c88a5a', shade='#c8a8a0', band='#1e2a28', band_d='#141c1a', mane='#d8b8b4', mane_d='#b0908c'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 70), (2, 76), (-10, 92, 1), (4, 80), (14, 66)]), 'mane'), L(outline([(84, 70), (98, 76), (110, 92, 1), (96, 80), (86, 66)]), 'mane'),
              L(outline([(12, 44), (6, 10), (14, -22), (36, -34), (64, -34), (86, -22), (94, 10), (88, 44)])),
              L(outline([(60, -32), (84, -20), (92, 10), (86, 40), (74, 4)]), 'shade', 'b', False),
              L(outline([(8, 76), (6, 40), (50, 34), (94, 40), (92, 76), (50, 82)]), 'band', 'f', ln=True),
              L(outline([(60, 38), (92, 42), (90, 74), (62, 78)]), 'band_d', 'f', False)],
    'side': [L(outline([(40, 60), (20, 54), (-6, 50, 1), (8, 60), (-14, 72, 1), (6, 74), (-6, 90, 1), (14, 84), (24, 96, 1), (30, 80), (44, 74)]), 'mane'),
             L(outline([(14, 40), (8, 8), (22, -20), (50, -32), (84, -34), (106, -26), (100, -14), (86, -6), (88, 14), (84, 40)])),
             L(outline([(14, 34), (20, -10), (40, -24), (30, 0), (30, 40)]), 'shade', 'b', False),
             L(outline([(12, 66), (12, 36), (50, 34), (94, 40), (94, 70), (50, 66)]), 'band', 'f', ln=True)],
    'back': [L(outline([(14, 70), (-8, 80, 1), (4, 90), (-4, 104, 1), (16, 98), (30, 108, 1), (40, 94), (50, 106, 1), (60, 94), (70, 108, 1), (84, 98), (104, 104, 1),
                        (96, 90), (108, 80, 1), (86, 70)]), 'mane'),
             L(outline([(12, 44), (6, 10), (14, -22), (36, -34), (64, -34), (86, -22), (94, 10), (88, 44)])),
             L(outline([(56, -32), (84, -20), (92, 10), (86, 40), (64, 40)]), 'shade', 'b', False),
             L(outline([(4, 76), (4, 36), (50, 30), (96, 36), (96, 76), (50, 70)]), 'band', 'f', ln=True)],
}

# Worff Chewback: rastas gordas morado oscuro que salen de lo alto y caen por los lados y la espalda, con los lados de la
# cabeza rapados; piel muy morena, bigote y perilla, ojos blancos achinados
CHARS['worff-chewback'] = {
    'body': 'corpulento', 'pal': pal('#2e2236', '#a86a3a', skin_d='#8a5228', buzz='#6a4a34', beard='#3a2418'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': [L(outline([(16, 66), (14, 36), (24, 18), (76, 18), (86, 36), (84, 66)]), 'buzz'),
              L(outline([(10, 112), (2, 80), (8, 40), (20, 10), (38, -4), (62, -4), (80, 10), (92, 40), (98, 80), (90, 112), (84, 104), (86, 70), (80, 40),
                         (70, 24), (64, 56, 1), (58, 24), (44, 24), (36, 56, 1), (30, 24), (20, 40), (14, 70), (16, 104)])),
              strand([(30, 4), (34, 30)], 'deep', 'b', 1.2), strand([(50, 0), (50, 22)], 'deep', 'b', 1.2), strand([(70, 4), (66, 30)], 'deep', 'b', 1.2),
              strand([(8, 50), (6, 100)], 'deep', 'b', 1.2), strand([(92, 50), (94, 100)], 'deep', 'b', 1.2),
              L(outline([(26, 72), (40, 70), (40, 76), (28, 78)]), WHITE, 'f', ln=True), L(outline([(74, 72), (60, 70), (60, 76), (72, 78)]), WHITE, 'f', ln=True),
              L(ell(36, 74, 1.4, 1.4), OUTC, 'f', False), L(ell(64, 74, 1.4, 1.4), OUTC, 'f', False),
              L(outline([(34, 96), (50, 92), (66, 96), (62, 100), (50, 98), (38, 100)]), 'beard', 'f', ln=True),
              L(outline([(40, 104), (60, 104), (56, 112), (44, 112)]), 'beard', 'f', ln=True)],
    'side': [L(outline([(20, 80), (12, 50), (24, 22), (58, 14), (60, 40), (50, 60), (42, 82)]), 'buzz'),
             L(outline([(66, 40), (62, 14), (48, 0), (24, 0), (6, 16), (-2, 50), (-8, 100), (2, 110), (12, 90), (18, 60), (28, 30), (44, 20), (56, 30), (60, 46)])),
             L(outline([(18, 12), (6, 40), (-6, 104), (6, 106), (14, 50), (28, 20)]), 'deep', 'b', False),
             L(outline([(80, 92), (92, 90), (94, 96), (84, 98)]), 'beard', 'f', ln=True), L(outline([(84, 104), (94, 104), (92, 112), (84, 110)]), 'beard', 'f', ln=True),
             L(outline([(80, 72), (90, 70), (88, 76)]), WHITE, 'f', ln=True)],
    'back': [L(outline([(8, 116), (2, 80), (6, 40), (20, 10), (38, -4), (62, -4), (80, 10), (94, 40), (98, 80), (92, 116), (76, 112), (64, 120), (50, 110),
                        (36, 120), (24, 112)])),
             strand([(20, 20), (14, 110)], 'deep', 'b', 1.4), strand([(36, 10), (34, 114)], 'deep', 'b', 1.4), strand([(50, 4), (50, 108)], 'deep', 'b', 1.4),
             strand([(64, 10), (66, 114)], 'deep', 'b', 1.4), strand([(80, 20), (86, 110)], 'deep', 'b', 1.4)],
}

# Dart H. Cylon: pelo azul marino peinado de lado con una franja rosa pálida, que le tapa un ojo y se recoge en una coleta
# gruesa que cae por delante del hombro; cara alargada, ojos rojos con marcas
CHARS['dart-h-cylon'] = {
    'body': 'delgado', 'pal': pal('#1e2a40', '#fce0c0', iris='#b01e1e', stripe='#e0c4c8'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 102, 'hairline': False, 'face_front': LONG_FACE},
    'front': [L(outline([(86, 40), (96, 70), (98, 110), (90, 120, 1), (82, 100), (82, 66)])),
              L(outline([(14, 70), (4, 40), (14, 12), (40, -4), (70, -2), (90, 14), (94, 40), (84, 56), (70, 30), (40, 40), (20, 80), (8, 92)])),
              L(outline([(6, 76), (10, 50), (30, 26), (60, 10), (84, 14), (60, 22), (34, 40), (16, 64)]), 'stripe', 'f', ln=True),
              L(outline([(90, 30), (96, 50), (92, 56)]), 'shade', 'b', False)],
    'side': [L(outline([(58, 46), (80, 40), (92, 24), (82, 4), (56, -6), (28, -2), (8, 14), (0, 44), (6, 70), (20, 88), (36, 90), (48, 70)])),
             L(outline([(4, 54), (40, 50), (86, 30), (88, 38), (40, 60), (6, 64)]), 'stripe', 'f', ln=True),
             L(outline([(4, 64), (30, 70), (36, 88), (10, 84)]), 'shade', 'b', False)],
    'back': [L(outline([(8, 86), (4, 40), (14, 12), (40, -4), (70, -2), (90, 14), (96, 40), (94, 86), (50, 92)])),
             L(outline([(36, 6), (70, 4), (90, 20), (88, 34), (60, 22), (40, 22)]), 'shade', 'b', False),
             L(outline([(4, 60), (50, 50), (96, 58), (96, 68), (50, 60), (4, 70)]), 'stripe', 'f', ln=True),
             L(outline([(70, 80), (90, 90), (96, 118, 1), (82, 104), (66, 90)]), 'mid', 'f')],
}

# Scotty O'Brien: una melena enorme castaño rojizo en bolas esponjosas (una encima y dos a los lados) y unos auriculares
# verdes al cuello; cara alargada y ojos rojos afilados
CHARS['scotty-o-brien'] = {
    'body': 'normal', 'pal': pal('#9a3a1e', '#fce0b8', iris='#b01e1e', phone='#2aa898', phone_d='#1e2a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 100, 'hairline': False, 'face_front': LONG_FACE},
    'front': [L(outline([(16, 92), (-6, 84), (-14, 56), (-6, 26), (20, 14), (26, -6), (50, -16), (74, -6), (80, 14), (106, 26), (114, 56), (106, 84), (84, 92),
                         (78, 54), (62, 48), (50, 72, 1), (38, 48), (22, 54)])),
              L(outline([(80, 16), (106, 30), (112, 60), (100, 84), (86, 60)]), 'shade', 'b', False),
              L(outline([(30, 4), (50, -10), (70, 4), (60, 20), (40, 20)]), 'light', 'b', False),
              strand([(22, 18), (34, 30), (36, 48)], 'deep', 'b', 1.2), strand([(78, 18), (66, 30), (64, 48)], 'deep', 'b', 1.2),
              L(outline([(4, 100), (8, 86), (20, 84), (22, 104), (12, 110)]), 'phone', 'f', ln=True),
              L(outline([(96, 100), (92, 86), (80, 84), (78, 104), (88, 110)]), 'phone', 'f', ln=True)],
    'side': [L(outline([(60, 50), (70, 40), (86, 34), (92, 14), (78, -6), (50, -16), (20, -8), (-2, 10), (-14, 40), (-8, 76), (10, 94), (30, 96), (44, 78),
                        (50, 60)])),
             L(outline([(-10, 46), (16, 50), (24, 88), (0, 86)]), 'shade', 'b', False),
             L(outline([(30, 100), (34, 92), (48, 92), (50, 108), (38, 112)]), 'phone', 'f', ln=True)],
    'back': [L(outline([(16, 96), (-6, 84), (-14, 56), (-6, 26), (20, 14), (26, -6), (50, -16), (74, -6), (80, 14), (106, 26), (114, 56), (106, 84), (84, 96),
                        (50, 100)])),
             L(outline([(54, -10), (80, 16), (110, 40), (108, 86), (70, 96)]), 'shade', 'b', False),
             L(outline([(14, 100), (86, 100), (88, 108), (12, 108)]), 'phone_d', 'f', ln=True),
             L(ell(10, 100, 7, 9), 'phone', 'f', ln=True), L(ell(90, 100, 7, 9), 'phone', 'f', ln=True)],
}

# Billy Lee Adarma: pelo granate oscuro corto con una cresta roja de pinchos de la frente a la nuca; ceño fruncido y dientes
# apretados
CHARS['billy-lee-adarma'] = {
    'body': 'bajito', 'pal': pal('#4a1a24', '#fcd8b4', iris='#2a1a1a', crest='#a81a2a', crest_d='#7a1020'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'hairline': (56, 46)},
    'front': [L(outline([(14, 66), (10, 36), (22, 12), (50, 4), (78, 12), (90, 36), (86, 66)])),
              L(outline([(32, 44), (30, 10), (40, -16), (56, -36, 1), (60, -10), (70, 10), (68, 44), (50, 54, 1)]), 'crest', 'f', ln=True),
              L(outline([(52, -20), (64, 6), (66, 40), (54, 48)]), 'crest_d', 'f', False)],
    'side': [L(outline([(54, 56), (62, 46), (82, 44), (90, 26), (76, 6), (50, 0), (24, 6), (8, 26), (6, 56), (18, 76), (34, 76), (46, 64)])),
             L(outline([(84, 34), (96, 14, 1), (80, 10), (84, -8, 1), (64, 2), (60, -18, 1), (46, 0), (32, -16, 1), (28, 6), (8, -2, 1), (14, 16), (-8, 22, 1), (6, 32),
                        (-4, 46, 1), (8, 50), (20, 30), (50, 16), (76, 24)]), 'crest', 'f', ln=True)],
    'back': [L(outline([(14, 70), (10, 36), (22, 12), (50, 4), (78, 12), (90, 36), (86, 70), (50, 80)])),
             L(outline([(36, 70), (34, 30), (40, 0), (50, -26, 1), (60, 0), (66, 30), (64, 70), (50, 80)]), 'crest', 'f', ln=True),
             strand([(38, 30), (62, 30)], 'crest_d', 'f', 1.2), strand([(36, 52), (64, 52)], 'crest_d', 'f', 1.2)],
}

# Zaphod Riker: melena morada lisa de media melena, con flequillo de mechones en punta; ojos amarillos y sonrisa pícara
CHARS['zaphod-riker'] = {
    'body': 'normal', 'pal': pal('#7a3a8a', '#fcd8b4', iris='#c8a01e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 106), (6, 60), (8, 26), (24, 4), (50, -4), (76, 4), (92, 26), (94, 60), (90, 106), (80, 100), (80, 60), (20, 60), (20, 100)])),
              L(outline([(60, 2), (86, 14), (94, 50), (90, 102), (80, 90), (80, 50)]), 'shade', 'b', False),
              fringe([(8, 96), (10, 46), (22, 18), (50, 8), (78, 18), (90, 46), (92, 96), (84, 92), (82, 60), (76, 66, 1), (70, 46), (60, 62, 1), (54, 44), (48, 70, 1),
                      (40, 44), (30, 64, 1), (24, 48), (18, 64), (16, 96)]),
              strand([(30, 16), (34, 50)], 'shade', 'f', 1.0), strand([(66, 16), (62, 50)], 'shade', 'f', 1.0)],
    'side': [L(outline([(56, 62), (62, 50), (82, 46), (92, 30), (86, 10), (62, -4), (34, -2), (12, 14), (2, 50), (-2, 104, 1), (14, 98), (28, 106, 1), (36, 96),
                        (46, 84)])),
             L(outline([(4, 44), (26, 48), (32, 98), (4, 100)]), 'shade', 'b', False),
             fringe([(66, 2), (88, 16), (94, 42), (90, 70, 1), (82, 54), (74, 40)])],
    'back': [L(outline([(10, 104), (6, 60), (8, 26), (24, 4), (50, -4), (76, 4), (92, 26), (94, 60), (90, 104), (78, 98), (66, 106), (50, 98), (34, 106), (22, 98)])),
             L(outline([(56, 2), (86, 14), (94, 50), (90, 104), (64, 100)]), 'shade', 'b', False),
             strand([(30, 20), (28, 100)], 'deep', 'b', 1.0), strand([(50, 4), (50, 96)], 'deep', 'b', 1.0), strand([(70, 20), (72, 100)], 'deep', 'b', 1.0)],
}

# Cyber Dalekman: un casco blanco redondo con orejeras, del que salen dos mechones castaños de punta por arriba y la nuca,
# y unas gafas verdes de cristales rojos sobre los ojos
CHARS['cyber-dalekman'] = {
    'body': 'bajito', 'pal': pal('#6a3a24', '#d8a070', helmet='#f4f0f0', helmet_d='#d8c8cc', gog='#1e5a4a', lens='#e8401e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False, 'nose': (50, 90, 3)},
    'front': [L(outline([(16, 8), (-6, -2, 1), (4, 16), (-2, 26, 1), (14, 24)])), L(outline([(84, 8), (106, -2, 1), (96, 16), (102, 26, 1), (86, 24)])),
              L(outline([(10, 84), (6, 40), (14, 10), (34, -4), (66, -4), (86, 10), (94, 40), (90, 84), (80, 80), (82, 60), (18, 60), (20, 80)]), 'helmet'),
              L(outline([(60, -2), (86, 12), (94, 46), (90, 80), (82, 56)]), 'helmet_d', 'b', False),
              L(outline([(10, 70), (14, 60), (34, 56), (50, 64), (66, 56), (86, 60), (90, 70), (86, 84), (66, 86), (50, 78), (34, 86), (14, 84)]), 'gog', 'f', ln=True),
              L(ell(32, 72, 10, 9), 'lens', 'f', ln=True), L(ell(68, 72, 10, 9), 'lens', 'f', ln=True),
              L(ell(28, 68, 3, 2.4), WHITE, 'f', False), L(ell(64, 68, 3, 2.4), WHITE, 'f', False)],
    'side': [L(outline([(40, 4), (36, -24, 1), (50, -10), (58, -4)])),
             L(outline([(54, 60), (62, 50), (82, 48), (92, 30), (84, 8), (60, -4), (30, -2), (10, 14), (2, 46), (8, 80), (24, 96), (42, 90), (50, 74)]), 'helmet'),
             L(outline([(4, 46), (30, 50), (34, 92), (10, 84)]), 'helmet_d', 'b', False),
             L(ell(30, 64, 12, 12), 'helmet_d', 'f', ln=True), L(ell(30, 64, 6, 6), 'helmet', 'f', ln=True),
             L(outline([(78, 64), (90, 60), (96, 72), (90, 82), (78, 80)]), 'gog', 'f', ln=True), L(ell(88, 71, 4, 6), 'lens', 'f', ln=True),
             L([(78, 72), (44, 70)], 'gog', 'f', False, False, 3)],
    'back': [L(outline([(16, 8), (-6, -2, 1), (4, 16), (-2, 26, 1), (14, 24)])), L(outline([(84, 8), (106, -2, 1), (96, 16), (102, 26, 1), (86, 24)])),
             L(outline([(10, 84), (6, 40), (14, 10), (34, -4), (66, -4), (86, 10), (94, 40), (90, 84), (50, 90)]), 'helmet'),
             L(outline([(40, 30), (94, 40), (90, 84), (50, 90)]), 'helmet_d', 'b', False),
             L(outline([(36, 88), (50, 80), (64, 88), (56, 100), (44, 100)]), 'mid', 'f')],
}

# Lucas Skywalk: melena rubia dorada lisa por debajo de las orejas, con mechones que le caen sobre la cara, y un antifaz negro
# sobre los ojos; sonrisa de dientes
CHARS['lucas-skywalk'] = {
    'body': 'normal', 'pal': pal('#f0b830', '#fcdcc0', iris='#3a5ab0', mask='#2a2420'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 108), (-6, 102, 1), (4, 86), (2, 50), (8, 20), (26, 2), (50, -4), (74, 2), (92, 20), (98, 50), (96, 86), (106, 102, 1), (90, 108),
                         (82, 64), (18, 64)])),
              L(outline([(60, 0), (86, 14), (96, 50), (98, 96), (84, 70)]), 'shade', 'b', False),
              L(outline([(14, 70), (30, 66), (50, 72), (70, 66), (86, 70), (86, 82), (70, 84), (50, 78), (30, 84), (14, 82)]), 'mask', 'f', ln=True),
              L(ell(34, 76, 4.4, 3.4), WHITE, 'f', False), L(ell(66, 76, 4.4, 3.4), WHITE, 'f', False),
              L(ell(35, 76, 2, 2.4), 'iris', 'f', False), L(ell(65, 76, 2, 2.4), 'iris', 'f', False),
              fringe([(8, 86), (10, 44), (24, 16), (50, 8), (76, 16), (90, 44), (92, 86), (84, 72), (80, 56), (70, 60), (62, 44), (54, 62, 1), (46, 40), (30, 50),
                      (22, 70), (16, 96, 1)]),
              strand([(36, 12), (40, 40)], 'shade', 'f', 1.0)],
    'side': [L(outline([(56, 64), (62, 52), (84, 48), (94, 30), (86, 8), (60, -4), (32, -2), (10, 14), (0, 50), (-4, 96, 1), (12, 88), (24, 100, 1), (34, 88),
                        (46, 80)])),
             L(outline([(2, 44), (26, 48), (32, 90), (4, 92)]), 'shade', 'b', False),
             L(outline([(76, 66), (94, 64), (96, 80), (78, 80)]), 'mask', 'f', ln=True), L([(76, 72), (50, 70)], 'mask', 'f', False, False, 2.4),
             fringe([(66, 2), (90, 16), (96, 42), (92, 64, 1), (84, 50), (76, 40)])],
    'back': [L(outline([(10, 106), (-6, 100, 1), (4, 86), (2, 50), (8, 20), (26, 2), (50, -4), (74, 2), (92, 20), (98, 50), (96, 86), (106, 100, 1), (90, 106),
                        (50, 112)])),
             L(outline([(56, 2), (86, 14), (98, 50), (96, 100), (60, 108)]), 'shade', 'b', False),
             L([(4, 74), (50, 70), (96, 74)], 'mask', 'f', False, False, 2.6)],
}

# Jimmy Kyrk: pelo naranja de pinchos hacia arriba y atrás, con un rizo que le cae a la frente, sujeto con una diadema
# blanca; ojos verdes afilados
CHARS['jimmy-kyrk'] = {
    'body': 'normal', 'pal': pal('#e86a1e', '#fcdcc0', iris='#2a9a6a', band='#f4f4f4'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': (58, 46)},
    'front': [L(outline([(14, 66), (2, 50, 1), (12, 40), (-4, 22, 1), (16, 22), (10, -6, 1), (28, 10), (34, -18, 1), (46, 4), (56, -22, 1), (62, 4), (80, -10, 1),
                         (80, 16), (104, 16, 1), (88, 36), (100, 52, 1), (86, 66)])),
              L(outline([(62, 0), (82, 10), (92, 40), (86, 62), (78, 40)]), 'shade', 'b', False),
              L(quad((12, 54), (50, 16), (88, 54)) + quad((86, 60), (50, 24), (14, 60)), 'band', 'f', ln=True),
              L(outline([(46, 24), (60, 26), (64, 40), (58, 52), (50, 48), (56, 40), (52, 32), (44, 34)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(54, 56), (62, 46), (80, 44), (88, 30), (82, 14), (96, 6, 1), (74, 4), (80, -16, 1), (56, -6), (52, -30, 1), (38, -6), (14, -24, 1), (20, 0),
                        (-12, 4, 1), (8, 18), (-18, 30, 1), (4, 38), (-8, 54, 1), (10, 58), (8, 74), (26, 76), (44, 66)])),
             L(outline([(4, 36), (24, 42), (24, 68), (10, 60)]), 'shade', 'b', False),
             L(quad((74, 46), (40, 14), (8, 46)) + quad((10, 52), (40, 22), (72, 52)), 'band', 'f', ln=True)],
    'back': [L(outline([(16, 72), (4, 60, 1), (12, 48), (-6, 30, 1), (12, 26), (2, 2, 1), (24, 10), (28, -16, 1), (42, 4), (54, -22, 1), (62, 4), (82, -12, 1), (80, 14),
                        (106, 12, 1), (90, 32), (106, 48, 1), (90, 54), (96, 70, 1), (84, 72), (50, 80)])),
             L(outline([(56, 4), (82, 12), (92, 46), (84, 70), (62, 76)]), 'shade', 'b', False),
             L(quad((10, 62), (50, 54), (90, 62)) + quad((90, 70), (50, 62), (10, 70)), 'band', 'f', ln=True)],
}

# Harkness Torchwood: pelo morado de pinchos altísimos hacia arriba, con patillas largas en punta; cara alargada de ojos
# negros rasgados y sonrisa de dientes
CHARS['harkness-torchwood'] = {
    'body': 'normal', 'pal': pal('#4a1e6a', '#fcdcc0', iris='#1e1414'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 100, 'hairline': False, 'face_front': LONG_FACE},
    'front': [L(outline([(16, 100), (12, 70), (6, 50), (-2, 30, 1), (14, 30), (16, 0), (24, -12, 1), (36, 0), (50, -38, 1), (62, -2), (78, -16, 1), (82, 14),
                         (100, 22, 1), (90, 40), (90, 70), (84, 100), (80, 70), (68, 50), (50, 40, 1), (32, 50), (20, 70)])),
              L(outline([(56, -28), (78, -10), (88, 20), (84, 60), (72, 30)]), 'shade', 'b', False)],
    'side': [L(outline([(54, 60), (60, 46), (80, 42), (88, 24), (78, 4), (82, -20, 1), (60, -6), (44, -36, 1), (36, -4), (16, -10, 1), (16, 10), (-6, 10, 1), (8, 30),
                        (0, 54), (12, 70), (26, 72), (44, 66)])),
             L(outline([(52, 60), (58, 90), (54, 102, 1), (50, 80)]), 'mid', 'f'),
             L(outline([(4, 30), (24, 36), (24, 64), (8, 58)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 76), (6, 52), (-4, 30, 1), (14, 30), (16, 0), (24, -12, 1), (36, 0), (50, -38, 1), (62, -2), (78, -16, 1), (82, 14), (104, 26, 1), (92, 50),
                        (84, 76), (50, 84)])),
             L(outline([(56, -28), (80, -8), (92, 30), (84, 72), (62, 80)]), 'shade', 'b', False),
             L(outline([(14, 80), (12, 100), (16, 104, 1), (20, 84)]), 'mid', 'f'), L(outline([(86, 80), (88, 100), (84, 104, 1), (80, 84)]), 'mid', 'f')],
}

# Jean-Luc Janeway: melena larga lisa rojo salmón peinada de lado, con un mechón que le tapa un ojo y la melena hasta media
# espalda; un pendiente negro y ojos verde azulado
CHARS['jean-luc-janeway'] = {
    'body': 'delgado', 'pal': pal('#e0604a', '#fcdcc0', iris='#2a6a7a', ear='#2a2424'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(6, 120), (4, 60), (8, 24), (24, 2), (50, -4), (76, 2), (92, 24), (96, 60), (94, 120), (84, 114), (82, 60), (18, 60), (16, 114)])),
              L(outline([(60, 0), (86, 14), (96, 50), (94, 116), (84, 100), (82, 50)]), 'shade', 'b', False),
              fringe([(16, 70), (18, 40), (30, 14), (54, 6), (80, 16), (90, 44), (92, 116), (84, 114), (82, 70), (76, 54), (66, 76), (60, 100, 1), (56, 66),
                      (50, 46), (40, 36), (28, 40), (22, 56)]),
              L(outline([(10, 74), (16, 72), (16, 82), (10, 84)]), 'ear', 'f', ln=True)],
    'side': [L(outline([(56, 60), (62, 50), (80, 44), (90, 28), (84, 8), (60, -4), (32, -2), (10, 14), (0, 50), (-4, 118, 1), (14, 112), (30, 118, 1), (36, 100),
                        (46, 84)])),
             L(outline([(2, 44), (26, 48), (32, 110), (2, 112)]), 'shade', 'b', False),
             L(outline([(42, 74), (48, 72), (48, 82), (42, 84)]), 'ear', 'f', ln=True)],
    'back': [L(outline([(6, 118), (4, 60), (8, 24), (24, 2), (50, -4), (76, 2), (92, 24), (96, 60), (94, 118), (50, 124)])),
             L(outline([(4, 40), (50, 26), (96, 40), (94, 118), (50, 124), (4, 118)]), 'shade', 'b', False),
             L(outline([(54, 2), (80, 8), (94, 30), (70, 26)]), 'mid', 'b', False)],
}

# Wesley Sheridan (portero suplente): pelo castaño dorado ondulado de raya al lado, con un mechón grande que le tapa medio
# ojo y las puntas rizadas junto a las orejas; mirada de aburrimiento
CHARS['wesley-sheridan'] = {
    'body': 'normal', 'pal': pal('#b0902e', '#fce0b8', iris='#1e1414', shade='#86682a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 92), (4, 60), (6, 24), (24, 2), (50, -4), (76, 2), (94, 24), (96, 60), (92, 92), (82, 86), (82, 60), (18, 60), (18, 86)])),
              L(outline([(60, 0), (86, 14), (96, 50), (92, 88), (84, 70)]), 'shade', 'b', False),
              fringe([(8, 84), (8, 40), (20, 14), (40, 4), (52, 12), (48, 30), (60, 20), (78, 16), (90, 40), (92, 80), (84, 70), (80, 50), (66, 40), (52, 50),
                      (46, 82, 1), (38, 50), (24, 50), (18, 70)]),
              L(outline([(40, 8), (50, 12), (44, 30), (36, 32)]), 'shade', 'f', False),
              strand([(88, 70), (84, 84), (90, 90)], 'shade', 'f', 1.0)],
    'side': [L(outline([(56, 60), (62, 50), (82, 46), (92, 30), (86, 8), (60, -6), (30, -4), (10, 12), (2, 46), (6, 80), (20, 96), (36, 92), (46, 78)])),
             L(outline([(4, 40), (26, 44), (32, 88), (10, 86)]), 'shade', 'b', False),
             fringe([(64, 0), (90, 16), (96, 42), (92, 70, 1), (84, 52), (74, 38)])],
    'back': [L(outline([(10, 88), (4, 60), (6, 24), (24, 2), (50, -4), (76, 2), (94, 24), (96, 60), (92, 88), (70, 94), (62, 84, 1), (50, 96), (38, 84, 1), (30, 94)])),
             L(outline([(56, 2), (86, 14), (96, 50), (92, 88), (62, 90)]), 'shade', 'b', False)],
}

# Sithri Peon: pelo azul marino recogido en un moño alto del que salen tres puntas, piel morena, cejas pintadas y una boca
# enorme de dientes
CHARS['sithri-peon'] = {
    'body': 'corpulento', 'pal': pal('#24285a', '#b47a48', iris='#2a1a1a', mouth='#7a3a1e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'hairline': (58, 44)},
    'front': [L(outline([(36, 6), (24, -12), (8, -16, 1), (28, -20), (40, -30), (48, -44, 1), (56, -30), (70, -24), (92, -18, 1), (76, -10), (64, 6)])),
              L(outline([(14, 66), (10, 36), (20, 12), (50, 2), (80, 12), (90, 36), (86, 66)])),
              L(outline([(60, 4), (82, 14), (90, 40), (84, 62), (76, 36)]), 'shade', 'b', False),
              L(outline([(28, 92), (72, 92), (70, 104), (30, 104)]), 'mouth', 'f', ln=True),
              L(outline([(32, 92), (38, 92), (36, 98)]), WHITE, 'f', False), L(outline([(68, 92), (62, 92), (64, 98)]), WHITE, 'f', False)],
    'side': [L(outline([(40, 4), (32, -14), (36, -36, 1), (46, -22), (56, -30, 1), (54, -12), (52, 4)])),
             L(outline([(54, 56), (62, 46), (80, 44), (88, 26), (76, 6), (50, -2), (24, 4), (8, 24), (6, 56), (20, 76), (36, 74), (46, 64)])),
             L(outline([(6, 36), (24, 42), (24, 66), (10, 60)]), 'shade', 'b', False),
             L(outline([(84, 92), (96, 92), (94, 102), (84, 102)]), 'mouth', 'f', ln=True)],
    'back': [L(outline([(36, 6), (24, -12), (8, -16, 1), (28, -20), (40, -30), (48, -44, 1), (56, -30), (70, -24), (92, -18, 1), (76, -10), (64, 6)])),
             L(outline([(14, 66), (10, 36), (20, 12), (50, 2), (80, 12), (90, 36), (86, 66), (70, 62), (50, 70), (30, 62)])),
             L(outline([(56, 4), (82, 14), (90, 46), (86, 64), (66, 62)]), 'shade', 'b', False)],
}

# Isaac Binks: pelo blanco revuelto de pinchos en todas direcciones, cejas gruesas castañas y nariz larga en punta
CHARS['isaac-binks'] = {
    'body': 'normal', 'pal': pal('#f4eef0', '#fcd8b4', iris='#2a1e1a', shade='#c8a8b0', brow='#a86a3a', nose='#e8a070'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 102, 'hairline': False, 'face_front': LONG_FACE},
    'front': [L(outline([(14, 66), (-6, 60, 1), (6, 50), (-10, 36, 1), (10, 30), (6, 10, 1), (24, 16), (26, -6, 1), (40, 8), (50, -12, 1), (58, 8), (74, -6, 1),
                         (76, 16), (96, 10, 1), (90, 30), (110, 36, 1), (94, 50), (106, 60, 1), (86, 66), (82, 52), (18, 52)])),
              L(outline([(62, 4), (84, 16), (94, 40), (88, 60), (78, 40)]), 'shade', 'b', False),
              fringe([(14, 60), (18, 38), (32, 26), (50, 22), (68, 26), (82, 38), (86, 60), (78, 52), (70, 60, 1), (64, 48), (54, 58, 1), (50, 46), (44, 60, 1),
                      (36, 48), (28, 58, 1), (22, 50)]),
              L(outline([(24, 66), (42, 64), (44, 70), (26, 72)]), 'brow', 'f', ln=True), L(outline([(76, 66), (58, 64), (56, 70), (74, 72)]), 'brow', 'f', ln=True),
              L(outline([(48, 76), (52, 76), (56, 100), (50, 102), (44, 100)]), 'nose', 'f', ln=True)],
    'side': [L(outline([(56, 56), (64, 46), (82, 44), (92, 30), (86, 14), (100, 8, 1), (76, 4), (82, -16, 1), (60, -2), (54, -22, 1), (40, -2), (20, -14, 1), (20, 6),
                        (-6, 6, 1), (8, 22), (-14, 34, 1), (4, 42), (-8, 58, 1), (10, 60), (4, 76, 1), (22, 70), (28, 80, 1), (38, 70), (48, 64)])),
             L(outline([(4, 36), (24, 42), (24, 66), (10, 60)]), 'shade', 'b', False),
             L(outline([(72, 64), (90, 62), (92, 70), (74, 70)]), 'brow', 'f', ln=True),
             L(outline([(86, 76), (110, 94), (88, 98)]), 'nose', 'f', ln=True)],
    'back': [L(outline([(16, 76), (-4, 70, 1), (8, 58), (-10, 42, 1), (8, 36), (2, 12, 1), (22, 16), (24, -8, 1), (40, 6), (50, -16, 1), (60, 6), (76, -8, 1),
                        (78, 16), (98, 12, 1), (92, 36), (110, 42, 1), (92, 58), (104, 70, 1), (84, 76), (70, 86, 1), (60, 78), (50, 90, 1), (40, 78), (30, 86, 1)])),
             L(outline([(56, 6), (84, 16), (94, 50), (86, 74), (62, 80)]), 'shade', 'b', False)],
}

# Carl Rissian: calvo por arriba con una cresta negra fina y alta y dos matas enormes de pelo negro rizado a los lados;
# gafas redondas verdes de montura blanca y dientes apretados
CHARS['carl-rissian'] = {
    'body': 'corpulento', 'pal': pal('#24161e', '#fcd8b0', glass='#2a6a5a', frame='#f0f0ec', nose='#f0a070'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False, 'nose': (50, 86, 3)},
    'front': [L(outline([(20, 70), (-10, 66, 1), (4, 58), (-18, 50, 1), (2, 42), (-12, 30, 1), (8, 26), (14, 40), (18, 60)])),
              L(outline([(80, 70), (110, 66, 1), (96, 58), (118, 50, 1), (98, 42), (112, 30, 1), (92, 26), (86, 40), (82, 60)])),
              L(outline([(-6, 80), (-24, 76, 1), (-8, 66), (-22, 54, 1), (-2, 50), (12, 56), (20, 86), (2, 96, 1)])),
              L(outline([(106, 80), (124, 76, 1), (108, 66), (122, 54, 1), (102, 50), (88, 56), (80, 86), (98, 96, 1)])),
              L(blob(SKULL_F), 'skin'),
              L(outline([(44, 20), (44, -24), (56, -24), (56, 20)]), 'mid', 'f', ln=True),
              L(quad((12, 72), (50, 70), (88, 72)), 'frame', 'f', False, False, 2.4),
              L(ell(36, 74, 7, 7), 'frame', 'f', ln=True), L(ell(64, 74, 7, 7), 'frame', 'f', ln=True),
              L(ell(36, 74, 4.6, 4.6), 'glass', 'f', False), L(ell(64, 74, 4.6, 4.6), 'glass', 'f', False)],
    'side': [L(outline([(48, 92), (22, 88), (12, 64), (14, 30), (32, 10), (58, 4), (80, 14), (88, 36), (76, 44), (60, 48), (52, 62), (50, 80)]), 'skin'),
             L(outline([(40, 40), (14, 30), (-8, 36, 1), (2, 46), (-14, 56, 1), (0, 62), (-10, 76, 1), (6, 80), (2, 96, 1), (18, 90), (30, 100, 1), (36, 84), (46, 74),
                        (48, 56)])),
             L(outline([(10, 26), (22, 4), (50, -14), (84, -6), (100, 10), (88, 14), (60, 2), (30, 14), (18, 32)]), 'mid', 'f', ln=True),
             L(ell(88, 74, 5, 6), 'frame', 'f', ln=True), L(ell(88, 74, 3, 4), 'glass', 'f', False), L([(82, 72), (48, 70)], 'frame', 'f', False, False, 2.2)],
    'back': [L(outline([(16, 40), (84, 40), (88, 70), (72, 90), (28, 90), (12, 70)]), 'skin'),
             L(outline([(4, 90), (-24, 84, 1), (-8, 72), (-26, 58, 1), (-6, 50), (-18, 36, 1), (4, 34), (20, 44), (50, 54), (80, 44), (96, 34), (118, 36, 1), (106, 50),
                        (126, 58, 1), (108, 72), (124, 84, 1), (96, 90), (80, 100, 1), (64, 90), (50, 102, 1), (36, 90), (20, 100, 1)])),
             L(outline([(44, 50), (44, -24), (56, -24), (56, 50)]), 'mid', 'f', ln=True)],
}

# Robert Affett: pelo azul marino que se abre en puntas hacia fuera a la altura de la mandíbula, con un tupé plateado ancho
# que va de la frente a la nuca; piel morena, ojos negros fruncidos
CHARS['robert-affett'] = {
    'body': 'normal', 'pal': pal('#24305a', '#c88a5a', iris='#1e1414', silver='#b8c8dc', silver_d='#8a98aa'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': (56, 30)},
    'front': [L(outline([(14, 90), (-6, 104, 1), (4, 86), (-8, 82, 1), (6, 70), (6, 30), (20, 8), (50, 0), (80, 8), (94, 30), (94, 70), (108, 82, 1), (96, 86),
                         (106, 104, 1), (86, 90), (82, 60), (18, 60)])),
              L(outline([(60, 4), (84, 14), (94, 46), (92, 82), (82, 56)]), 'shade', 'b', False),
              L(outline([(34, 34), (30, 6), (40, -10), (60, -10), (70, 6), (66, 34), (50, 40)]), 'silver', 'f', ln=True),
              L(outline([(52, -8), (66, 4), (64, 30), (52, 36)]), 'silver_d', 'f', False)],
    'side': [L(outline([(56, 56), (62, 46), (82, 42), (92, 26), (84, 6), (60, -4), (30, -2), (10, 14), (0, 50), (-6, 80), (-20, 96, 1), (2, 90), (6, 104, 1), (20, 92),
                        (36, 90), (46, 76)])),
             L(outline([(0, 50), (26, 54), (30, 88), (6, 90)]), 'shade', 'b', False),
             L(outline([(4, 30), (20, 2), (50, -12), (84, -8), (96, 6), (84, 10), (54, 4), (24, 16), (10, 40)]), 'silver', 'f', ln=True)],
    'back': [L(outline([(10, 90), (-12, 100, 1), (2, 84), (-10, 76, 1), (6, 66), (6, 30), (20, 8), (50, 0), (80, 8), (94, 30), (94, 66), (110, 76, 1), (98, 84),
                        (112, 100, 1), (90, 90), (70, 96), (50, 90), (30, 96)])),
             L(outline([(56, 4), (86, 14), (94, 50), (92, 88), (62, 92)]), 'shade', 'b', False),
             L(outline([(30, 4), (40, -8), (60, -8), (70, 4), (60, 50), (50, 80, 1), (40, 50)]), 'silver', 'f', ln=True),
             L(outline([(52, -6), (68, 4), (58, 48), (52, 70)]), 'silver_d', 'f', False)],
}
