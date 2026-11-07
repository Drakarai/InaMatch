"""Inazuma Kids FC (GO) (go-inazuma-kfc-go): sus modelos 3D de Inazuma Eleven GO como referencia (busto de frente, perfil
y espalda): un equipo de críos con gorros, cascos, cintas y peinados de lo más variado."""
from chars import CHARS, L, OUTC, ell, messy, outline, pal, strand
from chars_alius import WIDE_FACE
from chars_bigwaves import side_eye, white_eyes
from heads import quad

WHITE = (250, 250, 250, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


def mirror_pts(pts):
    return [(100 - p[0],) + tuple(p[1:]) for p in pts]


# Vivian Doosley (portero): un casco granate acolchado que le tapa la cabeza hasta los ojos, con orejeras redondas; solo
# se le ve la boca sonriente y la nariz bajo la sombra del casco
CHARS['vivian-doosley'] = {
    'body': 'normal', 'pal': pal('#6a1a48', '#c08050', helm='#6a1a48', helm_d='#4a1030', helm_l='#8a3a68'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 76), (8, 30), (16, 4), (32, -10), (50, -12), (68, -10), (84, 4), (92, 30), (90, 76), (80, 74), (80, 66), (20, 66), (20, 74)]),
                'helm', 'f'),
              L(outline([(60, -8), (82, 4), (90, 34), (88, 72), (80, 64), (76, 20)]), 'helm_d', 'f', False),
              L(ell(34, 14, 10, 6), 'helm_l', 'f', False),
              L(outline([(22, 66), (78, 66), (76, 76), (24, 76)]), 'skin_d', 'f', False),
              L(ell(14, 84, 8, 10), 'helm', 'f', ln=True), L(ell(86, 84, 8, 10), 'helm', 'f', ln=True),
              L([(50, 70), (50, 86)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(4, 74), (2, 30), (12, 4), (32, -10), (58, -12), (80, -4), (94, 14), (98, 40), (96, 66), (80, 66), (62, 64), (54, 74), (40, 92), (20, 94),
                        (6, 86)]), 'helm', 'f'),
             L(outline([(4, 40), (24, 46), (34, 90), (8, 84)]), 'helm_d', 'f', False),
             L(ell(48, 82, 8, 10), 'helm', 'f', ln=True)],
    'back': [L(outline([(10, 80), (8, 30), (16, 4), (32, -10), (50, -12), (68, -10), (84, 4), (92, 30), (90, 80), (74, 94), (26, 94)]), 'helm', 'f'),
             L(outline([(14, 56), (86, 56), (84, 82), (70, 92), (30, 92), (16, 82)]), 'helm_d', 'f', False),
             L(ell(12, 84, 8, 10), 'helm', 'f', ln=True), L(ell(88, 84, 8, 10), 'helm', 'f', ln=True)],
}

# Sean Muller: afro castaño ancho con dos bolas azul marino y amarillas como orejas de oso arriba, y una capucha azul
# marino que le enmarca la cara hasta la barbilla; nariz roja, cejas fruncidas y morros de enfado
_afro_sm = [(4, 62), (-10, 50), (-8, 30), (2, 12), (20, 0), (40, -6), (60, -6), (80, 0), (98, 12), (108, 30), (110, 50), (96, 62), (84, 54), (66, 58), (50, 52),
            (34, 58), (16, 54)]
CHARS['sean-muller'] = {
    'body': 'normal', 'pal': pal('#6a4020', '#fcd0a0', iris='#1e1414', hood='#283a78', hood_d='#1c2a5a', ylw='#f0b828', nose='#d0603a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False, 'nose': (50, 86, 4.4), 'ears': True},
    'front': [L(ell(18, 6, 11, 11), 'hood'), L(ell(82, 6, 11, 11), 'hood'),
              L(outline([(10, 0), (16, -6), (26, -2), (18, 4)]), 'ylw', 'b', False), L(outline([(90, 0), (84, -6), (74, -2), (82, 4)]), 'ylw', 'b', False),
              L(outline(_afro_sm), 'mid', 'f'),
              L(outline([(60, -4), (84, 2), (104, 28), (100, 54), (86, 50), (80, 20)]), 'shade', 'f', False),
              L(outline([(14, 56), (8, 82), (16, 104), (36, 118), (64, 118), (84, 104), (92, 82), (86, 56), (78, 60), (82, 84), (76, 100), (62, 108), (38, 108),
                         (24, 100), (18, 84), (22, 60)]), 'hood', 'f', ln=True),
              L(outline([(40, 104), (60, 104), (56, 112), (44, 112)]), 'skin_d', 'f', False)],
    'side': [L(ell(56, 0, 11, 11), 'hood'), L(outline([(48, -6), (58, -12), (66, -4), (56, 0)]), 'ylw', 'b', False),
             L(outline([(14, 50), (10, 80), (26, 96), (56, 112), (74, 112), (72, 104), (54, 98), (44, 80), (40, 54)]), 'hood', 'f', ln=True),
             L(outline([(2, 64), (-8, 46), (-6, 22), (8, 4), (30, -6), (56, -8), (80, 0), (96, 16), (100, 38), (92, 54), (76, 48), (58, 54), (42, 50), (24, 62)]),
               'mid', 'f'),
             L(outline([(-6, 40), (14, 44), (22, 60), (2, 62)]), 'shade', 'f', False)],
    'back': [L(ell(18, 6, 11, 11), 'hood'), L(ell(82, 6, 11, 11), 'hood'),
             L(outline([(16, 70), (14, 96), (36, 104), (64, 104), (86, 96), (84, 70)]), 'hood', 'b'),
             L(outline([(2, 70), (-10, 56), (-10, 30), (2, 10), (20, -2), (40, -8), (60, -8), (80, -2), (98, 10), (110, 30), (110, 56), (98, 70), (80, 78),
                        (50, 80), (20, 78)]), 'mid', 'f'),
             L(outline([(56, -4), (86, 4), (108, 34), (104, 66), (80, 74), (78, 30)]), 'shade', 'f', False)],
}

# Abe Roof: gorra azul marino con el frontal blanco, un rayo y las letras KFC en amarillo; pelo negro de puntas por los lados
# y una cola de pelo atada atrás; un mechón le cae sobre el ojo
CHARS['abe-roof'] = {
    'body': 'normal', 'pal': pal('#1e1e22', '#fcdcbc', iris='#6a6a72', cap='#283a7a', cap_d='#1c2a5a', ylw='#f0c030'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 76), (-6, 66, 1), (8, 60), (-4, 50, 1), (12, 46), (88, 46), (104, 50, 1), (92, 60), (106, 66, 1), (88, 76), (84, 62), (16, 62)])),
              L(outline([(10, 48), (10, 24), (22, 4), (50, -4), (78, 4), (90, 24), (90, 48)]), 'cap', 'f'),
              L(outline([(24, 44), (26, 14), (50, 6), (74, 14), (76, 44)]), WHITE, 'f'),
              L(outline([(50, 8), (44, 22), (52, 22), (46, 32), (58, 18), (50, 18), (56, 8)]), 'cap', 'f', False),
              L(outline([(34, 32), (66, 32), (66, 40), (34, 40)]), 'ylw', 'f', ln=True),
              L(outline([(6, 46), (50, 40), (94, 46), (96, 56), (50, 52), (4, 56)]), 'cap_d', 'f'),
              fringe([(26, 56), (42, 54), (48, 76, 1), (38, 64), (30, 74, 1), (24, 62)])],
    'side': [L(outline([(14, 52), (-14, 56), (-30, 82, 1), (-10, 70), (-20, 96, 1), (2, 78), (20, 72)])),
             L(outline([(8, 50), (14, 70), (34, 80), (46, 74), (50, 54)])),
             L(outline([(8, 52), (8, 22), (26, 4), (54, -4), (76, 4), (88, 24), (90, 48), (50, 52)]), 'cap', 'f'),
             L(outline([(62, 0), (80, 8), (88, 28), (88, 46), (66, 46)]), WHITE, 'f'),
             L(outline([(70, 44), (112, 48), (110, 56), (70, 54)]), 'cap_d', 'f'),
             fringe([(70, 54), (84, 54), (88, 70, 1), (78, 62)])],
    'back': [L(outline([(12, 86), (-8, 74, 1), (8, 66), (-4, 54, 1), (12, 48), (88, 48), (104, 54, 1), (92, 66), (108, 74, 1), (88, 86), (60, 92), (50, 104, 1),
                        (40, 92)])),
             L(outline([(10, 52), (10, 24), (22, 4), (50, -4), (78, 4), (90, 24), (90, 52), (50, 56)]), 'cap', 'f'),
             L(outline([(34, 50), (36, 40), (64, 40), (66, 50)]), 'cap_d', 'f', False)],
}

# Buck Tucker: grandullón de piel morena y cabeza ancha con orejas grandes; gorro de rayas gris y morado hasta los ojos, un
# sombrerito de copa azul marino con cinta rosa encima y unas gafas rosas de cristales verdes
_beanie_bt = [(12, 66), (10, 30), (20, 12), (50, 6), (80, 12), (90, 30), (88, 66), (50, 62)]
CHARS['buck-tucker'] = {
    'body': 'corpulento', 'pal': pal('#5a5a6c', '#b07a4a', iris='#2a1a1a', hat='#2e2650', pink='#f07a7a', grey='#8a8a98', lens='#5a8a2a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False, 'face_front': WIDE_FACE, 'big_ears': 3, 'ear_out': 4},
    'front': [L(outline(_beanie_bt), 'grey', 'f'),
              L([(11, 40), (89, 40), (89, 50), (11, 50)], 'mid', 'f', False), L([(17, 22), (83, 22), (86, 30), (14, 30)], 'mid', 'f', False),
              L(outline([(28, 14), (26, -16), (74, -16), (72, 14)]), 'hat', 'f'), L(outline([(27, 4), (73, 4), (72, 12), (28, 12)]), 'pink', 'f', ln=True),
              L(outline([(14, 66), (86, 66), (86, 74), (14, 74)]), 'pink', 'f', ln=True),
              L(ell(38, 70, 6.5, 6), 'pink', 'f', ln=True), L(ell(62, 70, 6.5, 6), 'pink', 'f', ln=True),
              L(ell(38, 70, 4.4, 4), 'lens', 'f', False), L(ell(62, 70, 4.4, 4), 'lens', 'f', False),
              L(ell(38, 70, 1.6, 1.6), OUTC, 'f', False), L(ell(62, 70, 1.6, 1.6), OUTC, 'f', False)],
    'side': [L(outline([(8, 66), (6, 30), (20, 10), (50, 4), (78, 10), (90, 30), (90, 62), (50, 64)]), 'grey', 'f'),
             L([(7, 40), (90, 40), (90, 50), (7, 50)], 'mid', 'f', False), L([(14, 22), (82, 22), (86, 30), (9, 30)], 'mid', 'f', False),
             L(outline([(30, 12), (28, -18), (72, -18), (70, 12)]), 'hat', 'f'), L(outline([(29, 2), (71, 2), (70, 10), (30, 10)]), 'pink', 'f', ln=True),
             L(outline([(50, 66), (92, 64), (92, 72), (50, 74)]), 'pink', 'f', ln=True), L(ell(90, 70, 4, 5), 'lens', 'f', ln=True)],
    'back': [L(outline([(12, 86), (10, 30), (20, 12), (50, 6), (80, 12), (90, 30), (88, 86), (50, 92)]), 'grey', 'f'),
             L([(11, 40), (89, 40), (89, 50), (11, 50)], 'mid', 'f', False), L([(11, 62), (89, 62), (89, 72), (11, 72)], 'mid', 'f', False),
             L([(17, 22), (83, 22), (86, 30), (14, 30)], 'mid', 'f', False),
             L(outline([(28, 14), (26, -16), (74, -16), (72, 14)]), 'hat', 'f'), L(outline([(27, 4), (73, 4), (72, 12), (28, 12)]), 'pink', 'f', ln=True),
             L([(11, 52), (89, 52), (89, 58), (11, 58)], 'pink', 'f', False)],
}

# Edward Headwood: pelo negro en casco redondo con un penacho verde de hojas en lo alto, piel morena, orejas grandes,
# unas gafas redondas enormes de montura blanca y cristales naranjas y dos dientes de conejo
CHARS['edward-headwood'] = {
    'body': 'bajito', 'pal': pal('#1e1e1e', '#a8703e', iris='#2a1a1a', leaf='#2a6a2a', leaf_l='#4a9a3a', lens='#f08a20'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'buck', 'mouth_y': 98, 'hairline': False, 'big_ears': 3, 'ear_out': 4},
    'front': [L(outline([(10, 80), (6, 40), (16, 14), (50, 2), (84, 14), (94, 40), (90, 80), (84, 66), (16, 66)])),
              L(outline([(36, 8), (30, -14, 1), (42, -4), (46, -24, 1), (52, -6), (60, -20, 1), (60, -2), (72, -10, 1), (64, 8)]), 'leaf', 'b'),
              L(outline([(44, -2), (48, -18), (52, -2)]), 'leaf_l', 'b', False),
              fringe([(12, 66), (14, 40), (30, 22), (50, 18), (70, 22), (86, 40), (88, 66), (70, 58), (50, 56), (30, 58)]),
              L(outline([(56, 6), (82, 18), (90, 44), (84, 60), (74, 34)]), 'shade', 'b', False),
              L(ell(34, 78, 12, 10), WHITE, 'f', ln=True), L(ell(66, 78, 12, 10), WHITE, 'f', ln=True),
              L(ell(34, 78, 8.6, 7), 'lens', 'f', ln=True), L(ell(66, 78, 8.6, 7), 'lens', 'f', ln=True),
              L([(30, 74), (38, 80)], WHITE, 'f', False, False, 1.4), L([(62, 74), (70, 80)], WHITE, 'f', False, False, 1.4)],
    'side': [L(outline([(54, 62), (60, 48), (82, 48), (92, 34), (86, 12), (64, 0), (38, 0), (16, 10), (4, 34), (6, 64), (20, 84), (38, 84), (46, 72)])),
             L(outline([(34, 4), (28, -16, 1), (40, -6), (46, -26, 1), (52, -6), (62, -20, 1), (60, 2)]), 'leaf', 'b'),
             L(outline([(4, 34), (24, 40), (26, 74), (8, 66)]), 'shade', 'b', False),
             L(ell(88, 78, 6, 10), WHITE, 'f', ln=True), L(ell(89, 78, 3.6, 7), 'lens', 'f', False),
             L([(82, 76), (54, 70)], WHITE, 'f', False, False, 2.0)],
    'back': [L(outline([(10, 80), (6, 40), (16, 14), (50, 2), (84, 14), (94, 40), (90, 80), (70, 92), (30, 92)])),
             L(outline([(36, 8), (30, -14, 1), (42, -4), (46, -24, 1), (52, -6), (60, -20, 1), (60, -2), (72, -10, 1), (64, 8)]), 'leaf', 'b'),
             L(outline([(56, 4), (84, 16), (94, 44), (88, 80), (64, 90)]), 'shade', 'b', False),
             L(outline([(42, 88), (50, 100, 1), (58, 88)]), 'leaf', 'b')],
}

# Ricky Shea: melena azul pizarra lisa hasta los hombros con flequillo recto que le tapa media frente, dos mechones claros
# en el flequillo y un moño alto; ojos entornados de sueño y sonrisa
CHARS['ricky-shea'] = {
    'body': 'delgado', 'pal': pal('#2c3648', '#f6c898', iris='#2a1a1a', light='#e8e4d0'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(38, 0), (36, -24), (50, -30), (64, -24), (62, 0)])),
              L(outline([(4, 118), (2, 60), (8, 20), (26, 0), (50, -6), (74, 0), (92, 20), (98, 60), (96, 118), (84, 118), (84, 70), (16, 70), (16, 118)])),
              L(outline([(62, 0), (88, 18), (96, 60), (94, 116), (84, 116), (82, 50)]), 'shade', 'b', False),
              fringe([(12, 72), (12, 40), (26, 18), (50, 12), (74, 18), (88, 40), (88, 72), (82, 72), (82, 62), (18, 62), (18, 72)]),
              L(outline([(28, 22), (32, 22), (30, 62), (26, 62)]), 'light', 'f', False), L(outline([(70, 22), (74, 22), (74, 62), (70, 62)]), 'light', 'f', False),
              L(outline([(60, 18), (80, 26), (86, 50), (80, 60), (72, 38)]), 'shade', 'f', False)],
    'side': [L(outline([(30, 2), (24, -22), (38, -30), (52, -22), (50, 0)])),
             L(outline([(52, 66), (58, 58), (84, 60), (92, 40), (88, 14), (70, 0), (44, -4), (20, 4), (4, 24), (-2, 60), (0, 118), (48, 118), (50, 92)])),
             L(outline([(2, 40), (24, 44), (36, 116), (4, 116)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 16), (96, 42), (94, 62, 1), (84, 56), (80, 40)])],
    'back': [L(outline([(38, 0), (36, -24), (50, -30), (64, -24), (62, 0)])),
             L(outline([(4, 118), (2, 60), (8, 20), (26, 0), (50, -6), (74, 0), (92, 20), (98, 60), (96, 118)])),
             L(outline([(56, 0), (88, 18), (96, 60), (94, 116), (64, 116)]), 'shade', 'b', False),
             L(outline([(34, 50), (66, 50), (62, 80), (38, 80)]), 'shade', 'b', False)],
}

# Felix Higgins: gorro blanco grande con dos picos como orejas de gato y la cara de un gato negro bordada; por debajo, pelo
# castaño con mechones en punta en la frente y dos mechones largos que le caen junto a las mejillas
CHARS['felix-higgins'] = {
    'body': 'normal', 'pal': pal('#5a3a20', '#fcd8b4', iris='#1e1414', hat='#f2eee8', hat_d='#c8b8b4'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(14, 50), (12, 104), (16, 116, 1), (22, 104), (22, 60)])), L(outline([(86, 50), (88, 104), (84, 116, 1), (78, 104), (78, 60)])),
              L(outline([(4, 48), (-4, -12, 1), (20, 0), (50, -2), (80, 0), (104, -12, 1), (96, 48), (50, 54)]), 'hat', 'f'),
              L(outline([(6, 34), (94, 34), (96, 48), (50, 54), (4, 48)]), 'hat_d', 'f', False),
              L(ell(50, 24, 6, 5), OUTC, 'f', False), L(outline([(44, 22), (44, 14, 1), (48, 20)]), OUTC, 'f', False),
              L(outline([(56, 22), (56, 14, 1), (52, 20)]), OUTC, 'f', False),
              fringe([(18, 50), (42, 50), (48, 66, 1), (40, 58), (32, 68, 1), (26, 58), (18, 60)])],
    'side': [L(outline([(12, 50), (14, 86), (24, 104), (30, 114, 1), (36, 100), (38, 80), (46, 60)])),
             L(outline([(2, 50), (2, 12), (18, -4), (36, -16, 1), (50, 0), (78, 4), (90, 28), (90, 50), (50, 56)]), 'hat', 'f'),
             L(outline([(2, 36), (90, 38), (90, 50), (50, 56), (2, 50)]), 'hat_d', 'f', False),
             fringe([(74, 50), (88, 50), (90, 66, 1), (80, 58)])],
    'back': [L(outline([(16, 60), (14, 100), (18, 112, 1), (24, 100), (26, 66)])), L(outline([(84, 60), (86, 100), (82, 112, 1), (76, 100), (74, 66)])),
             L(outline([(20, 50), (22, 80), (36, 86), (50, 96, 1), (64, 86), (78, 80), (80, 50)])),
             L(outline([(4, 54), (-12, -12, 1), (20, -2), (50, -4), (80, -2), (112, -12, 1), (96, 54), (50, 58)]), 'hat', 'f'),
             L(outline([(50, -2), (80, -2), (108, -8), (94, 52), (60, 56)]), 'hat_d', 'f', False)],
}

# Keeley Hall: pañuelo azul petróleo con una franja blanca atado a la cabeza con el nudo a un lado; melena rubia larga y
# lisa que le tapa un ojo; pecas y ojo amarillo verdoso
_kh_band = [(8, 42), (10, 18), (26, 2), (50, -4), (74, 2), (90, 18), (92, 42), (70, 38), (50, 40), (30, 38)]
CHARS['keeley-hall'] = {
    'body': 'delgado', 'pal': pal('#f0d070', '#f6c898', iris='#9a9a2a', cloth='#3a6a8a', cloth_d='#2a4e6a'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(0, 122), (-4, 70), (6, 34), (94, 34), (104, 70), (100, 122), (84, 120), (84, 70), (16, 70), (16, 120)])),
              L(outline([(60, 36), (96, 40), (102, 76), (98, 118), (86, 118), (84, 66)]), 'shade', 'b', False),
              fringe([(8, 46), (30, 40), (60, 42), (80, 42), (90, 52), (86, 64), (74, 52), (62, 56), (56, 86, 1), (44, 92), (22, 112, 1), (12, 84)]),
              L(outline(_kh_band), 'cloth', 'f', ln=True),
              L(outline([(12, 30), (40, 14), (60, 14), (88, 30), (90, 36), (60, 22), (40, 22), (10, 38)]), WHITE, 'f', False),
              L(outline([(10, 36), (-16, 26, 1), (-6, 40), (-18, 56, 1), (6, 48)]), 'cloth', 'f', ln=True), L(ell(8, 40, 5, 5), 'cloth_d', 'f', ln=True),
              L([(62, 90), (63, 91)], OUTC, 'f', False, False, 1.0), L([(70, 88), (71, 89)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(54, 60), (62, 52), (84, 52), (92, 40), (88, 14), (66, 0), (36, -2), (12, 10), (-2, 40), (-10, 90), (-6, 124, 1), (14, 110), (32, 124, 1),
                        (44, 100), (50, 80)])),
             L(outline([(-4, 50), (20, 50), (30, 110), (0, 118)]), 'shade', 'b', False),
             L(outline([(2, 44), (4, 16), (28, 0), (60, -4), (82, 4), (94, 24), (96, 42), (50, 40)]), 'cloth', 'f', ln=True),
             L(outline([(6, 28), (60, 8), (90, 22), (92, 30), (60, 16), (6, 36)]), WHITE, 'f', False),
             L(outline([(30, 40), (10, 46), (-8, 60, 1), (8, 52), (-4, 72, 1), (22, 50)]), 'cloth', 'f', ln=True),
             fringe([(70, 40), (92, 44), (96, 60), (90, 72, 1), (84, 56), (76, 52)])],
    'back': [L(outline([(0, 122), (-4, 70), (4, 34), (96, 34), (104, 70), (100, 122), (84, 116), (68, 124), (50, 116), (32, 124), (16, 116)])),
             L(outline([(56, 36), (98, 40), (102, 80), (98, 120), (64, 120)]), 'shade', 'b', False),
             L(outline([(8, 46), (10, 18), (26, 2), (50, -4), (74, 2), (90, 18), (92, 46), (50, 50)]), 'cloth', 'f', ln=True),
             L(outline([(88, 36), (116, 26, 1), (106, 40), (118, 56, 1), (92, 48)]), 'cloth', 'f', ln=True), L(ell(90, 42, 5, 5), 'cloth_d', 'f', ln=True)],
}

# Walt Riverside: un afro castaño oscuro enorme alrededor de la cabeza, cascos de música rosas con la diadema verde lima
# por encima; ojos cerrados y sonrisa tranquila
_afro_wr = [(-12, 76), (-20, 44), (-10, 12), (10, -12), (36, -22), (64, -22), (90, -12), (110, 12), (120, 44), (112, 76), (98, 92), (88, 82), (86, 60), (14, 60),
            (12, 82), (2, 92)]
CHARS['walt-riverside'] = {
    'body': 'normal', 'pal': pal('#4a2a1e', '#b07a4a', iris='#2a1a1a', band='#7ad83a', cup='#a07a80', cup_d='#7a5a60'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': (58, 50)},
    'front': [L(outline(_afro_wr)), L(outline([(60, -18), (96, -8), (118, 30), (110, 80), (94, 86), (90, 30)]), 'shade', 'b', False),
              L(quad((12, 74), (50, 4), (88, 74)), 'band', 'f', False, False, 3.0),
              L(outline([(6, 70), (18, 68), (20, 92), (8, 94)]), 'cup', 'f', ln=True), L(outline([(94, 70), (82, 68), (80, 92), (92, 94)]), 'cup', 'f', ln=True)],
    'side': [L(outline([(60, 50), (76, 46), (98, 34), (106, 10), (88, -14), (60, -24), (30, -22), (4, -10), (-14, 14), (-22, 46), (-14, 78), (4, 100), (28, 104),
                        (46, 90), (52, 66)])),
             L(outline([(-18, 40), (10, 50), (24, 98), (0, 96)]), 'shade', 'b', False),
             L(quad((50, 64), (58, 20), (66, -12)), 'band', 'f', False, False, 3.0),
             L(outline([(40, 62), (56, 60), (60, 84), (44, 88)]), 'cup', 'f', ln=True), L(outline([(44, 68), (54, 66), (56, 80), (46, 82)]), 'cup_d', 'f', False)],
    'back': [L(outline([(-14, 80), (-20, 44), (-10, 12), (10, -12), (36, -22), (64, -22), (90, -12), (110, 12), (120, 44), (114, 80), (96, 100), (70, 108),
                        (30, 108), (4, 100)])),
             L(outline([(56, -20), (96, -8), (118, 34), (110, 84), (70, 104)]), 'shade', 'b', False)],
}

# Warren Cool: pelo morado oscuro muy ancho, de puntas que se abren en horizontal a los lados, con una coletilla atada con
# una goma blanca en la nuca; ojos rojos y sonrisa de pillo
CHARS['warren-cool'] = {
    'body': 'normal', 'pal': pal('#4a3060', '#fcd8b4', iris='#c8202a', tie='#e8e0d8'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 80), (-18, 66, 1), (0, 60), (-14, 48, 1), (2, 40), (8, 18), (26, 2), (44, -6), (50, -16, 1), (56, -4), (76, 2), (92, 18), (98, 40),
                         (116, 48, 1), (102, 60), (120, 68, 1), (92, 80), (86, 62), (14, 62)])),
              L(outline([(60, 0), (88, 14), (100, 44), (96, 70), (84, 50)]), 'shade', 'b', False),
              fringe([(12, 64), (16, 40), (30, 26), (50, 22), (70, 26), (84, 40), (88, 64), (80, 52), (74, 62, 1), (66, 48), (58, 60, 1), (52, 46), (44, 58, 1),
                      (36, 46), (28, 60, 1), (20, 50)])],
    'side': [L(outline([(54, 60), (62, 50), (82, 50), (94, 36), (92, 14), (100, 8, 1), (80, 4), (66, -8), (60, -16, 1), (52, -6), (30, -4), (6, 6), (-16, 12, 1),
                        (0, 22), (-10, 36, 1), (6, 42), (6, 62), (20, 74), (40, 72)])),
             L(outline([(14, 66), (-6, 76), (-14, 94, 1), (2, 82), (20, 74)])), L(ell(14, 68, 3, 3), 'tie', 'f', ln=True),
             L(outline([(4, 26), (24, 34), (26, 62), (8, 56)]), 'shade', 'b', False),
             fringe([(64, 4), (90, 18), (96, 40), (94, 62, 1), (86, 48), (80, 58, 1), (74, 40)])],
    'back': [L(outline([(16, 78), (-20, 70, 1), (-2, 60), (-26, 52, 1), (-4, 42), (4, 20), (24, 4), (44, -4), (50, -14, 1), (56, -4), (76, 4), (96, 20), (104, 42),
                        (126, 52, 1), (102, 60), (120, 70, 1), (84, 78), (50, 82)])),
             L(outline([(56, -2), (96, 20), (112, 54), (84, 76), (60, 78)]), 'shade', 'b', False),
             L(outline([(46, 80), (42, 96), (50, 110, 1), (58, 96), (54, 80)]), 'mid', 'f'), L(outline([(44, 82), (56, 82), (56, 88), (44, 88)]), 'tie', 'f', ln=True)],
}

# Elizabeth Buble: pelo rosa malva corto con dos coletas largas retorcidas que salen hacia fuera y caen, una horquilla con
# una calavera blanca, sombra de ojos morada y ojos grises
_tail_eb = [(16, 22), (-6, 16), (-16, 32), (-10, 62), (-6, 92), (0, 108, 1), (4, 82), (2, 42), (14, 32)]
CHARS['elizabeth-buble'] = {
    'body': 'chica', 'pal': pal('#b86a80', '#fcdcc0', iris='#6a7090'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline(_tail_eb)), L(outline(mirror_pts(_tail_eb))),
              L(outline([(14, 72), (10, 36), (20, 14), (50, 4), (80, 14), (90, 36), (86, 72), (80, 56), (20, 56)])),
              L(outline([(60, 8), (84, 18), (90, 44), (84, 66), (78, 40)]), 'shade', 'b', False),
              fringe([(14, 62), (16, 38), (30, 20), (50, 14), (70, 20), (84, 38), (86, 62), (78, 50), (70, 58, 1), (60, 46), (50, 42), (40, 46), (32, 56, 1),
                      (24, 48)]),
              L(ell(34, 26, 6, 5), WHITE, 'f', ln=True), L(ell(32, 26, 1.2, 1.2), OUTC, 'f', False), L(ell(36, 26, 1.2, 1.2), OUTC, 'f', False)],
    'side': [L(outline([(54, 62), (60, 50), (82, 50), (92, 36), (88, 14), (68, 0), (40, -2), (18, 8), (6, 30), (8, 60), (20, 76), (40, 72)])),
             L(outline([(24, 6), (8, 12), (-2, 36), (2, 80), (8, 104, 1), (14, 78), (14, 40), (28, 20)])),
             L(outline([(6, 30), (24, 36), (26, 66), (10, 60)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 16), (94, 40), (90, 56, 1), (82, 44), (74, 34)])],
    'back': [L(outline(_tail_eb)), L(outline(mirror_pts(_tail_eb))),
             L(outline([(14, 76), (10, 36), (20, 14), (50, 4), (80, 14), (90, 36), (86, 76), (50, 84)])),
             L(outline([(56, 6), (84, 18), (90, 46), (84, 72), (60, 80)]), 'shade', 'b', False)],
}

# Titch Allhare (portero suplente): un afro dorado enorme en forma de seta que le cubre la frente; carita pequeña y risueña
_afro_ta = [(-6, 64), (-12, 30), (0, 4), (20, -14), (50, -20), (80, -14), (100, 4), (112, 30), (106, 64), (90, 70), (70, 62), (50, 68), (30, 62), (10, 70)]
CHARS['titch-allhare'] = {
    'body': 'bajito', 'pal': pal('#c88a20', '#fcd8b4', iris='#2a1a1a'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline(_afro_ta), 'mid', 'f'), L(outline([(56, -16), (90, -6), (110, 30), (104, 60), (88, 64), (82, 20)]), 'shade', 'f', False),
              L(outline([(20, 0), (40, -10), (32, 6)]), 'light', 'f', False)],
    'side': [L(outline([(-8, 66), (-14, 30), (0, 2), (24, -16), (54, -20), (82, -12), (100, 6), (108, 30), (100, 60), (82, 62), (62, 58), (48, 70), (40, 86),
                        (20, 88), (4, 80)]), 'mid', 'f'),
             L(outline([(-10, 40), (14, 48), (24, 84), (2, 80)]), 'shade', 'f', False)],
    'back': [L(outline([(-8, 70), (-12, 30), (0, 4), (20, -14), (50, -20), (80, -14), (100, 4), (112, 30), (108, 70), (86, 90), (50, 96), (14, 90)]), 'mid', 'f'),
             L(outline([(56, -16), (90, -6), (110, 30), (104, 70), (80, 88), (76, 20)]), 'shade', 'f', False)],
}

# Puck Fishley: pelo negro con una cinta naranja y amarilla en la frente y mechones largos y gruesos que salen de los lados
# hacia abajo y hacia fuera hasta los hombros
_lock_pf = [(16, 40), (-2, 56), (-16, 92, 1), (2, 72), (-2, 98, 1), (12, 76), (22, 56)]
CHARS['puck-fishley'] = {
    'body': 'normal', 'pal': pal('#1a1a1e', '#fcd8b4', iris='#5a5a62', band='#f07a20', band2='#f0b828'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(14, 66), (12, 30), (26, 8), (50, 2), (74, 8), (88, 30), (86, 66), (80, 54), (20, 54)])),
              fringe([(20, 52), (30, 46), (36, 60, 1), (42, 48), (50, 46), (58, 48), (64, 60, 1), (70, 46), (80, 52), (80, 40), (20, 40)]),
              L(outline([(12, 46), (12, 30), (50, 22), (88, 30), (88, 46), (50, 40)]), 'band', 'f', ln=True),
              L(outline([(50, 23), (88, 30), (88, 46), (50, 40)]), 'band2', 'f', False),
              L(outline(_lock_pf), 'mid', 'f'), L(outline(mirror_pts(_lock_pf)), 'mid', 'f')],
    'side': [L(outline([(54, 60), (60, 48), (82, 48), (92, 34), (86, 12), (64, 0), (38, 0), (16, 10), (6, 32), (6, 60), (20, 76), (40, 74)])),
             L(outline([(4, 46), (6, 24), (50, 18), (92, 28), (92, 44), (50, 40)]), 'band', 'f', ln=True),
             L(outline([(50, 19), (92, 28), (92, 44), (50, 40)]), 'band2', 'f', False),
             L(outline([(30, 30), (6, 50), (-16, 96, 1), (4, 76), (0, 104, 1), (18, 76), (38, 44)]), 'mid', 'f')],
    'back': [L(outline([(14, 80), (12, 30), (26, 8), (50, 2), (74, 8), (88, 30), (86, 80), (50, 88)])),
             L(outline([(12, 50), (12, 32), (50, 26), (88, 32), (88, 50), (50, 46)]), 'band', 'f', ln=True),
             L(outline([(50, 27), (88, 32), (88, 50), (50, 46)]), 'band2', 'f', False),
             L(outline([(20, 30), (-2, 50), (-22, 92, 1), (-2, 72), (-6, 100, 1), (12, 74), (24, 50)]), 'mid', 'f'),
             L(outline([(80, 30), (102, 50), (122, 92, 1), (102, 72), (106, 100, 1), (88, 74), (76, 50)]), 'mid', 'f')],
}

# Reed Maind: melena azul lisa muy larga con flequillo recto, sujeta con una diadema blanca con dos piedras rojas; cejas
# fruncidas y gesto serio
CHARS['reed-maind'] = {
    'body': 'normal', 'pal': pal('#5878b8', '#fcd8b4', iris='#1e1414', gem='#c81e3a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(4, 120), (2, 60), (8, 20), (26, 0), (50, -6), (74, 0), (92, 20), (98, 60), (96, 120), (84, 120), (84, 70), (16, 70), (16, 120)])),
              L(outline([(62, 0), (88, 18), (96, 60), (94, 118), (84, 118), (82, 50)]), 'shade', 'b', False),
              fringe([(12, 66), (12, 44), (88, 44), (88, 66), (80, 60), (74, 66), (66, 60), (58, 66), (50, 60), (42, 66), (34, 60), (26, 66), (18, 60)]),
              L(outline([(10, 46), (90, 46), (90, 50), (10, 50)]), WHITE, 'f', ln=True),
              L(ell(38, 48, 4, 4), WHITE, 'f', ln=True), L(ell(62, 48, 4, 4), WHITE, 'f', ln=True),
              L(ell(38, 48, 2.4, 2.4), 'gem', 'f', False), L(ell(62, 48, 2.4, 2.4), 'gem', 'f', False)],
    'side': [L(outline([(52, 66), (58, 58), (84, 60), (92, 40), (88, 14), (70, 0), (44, -4), (20, 4), (4, 24), (-2, 60), (-20, 118), (46, 118), (50, 92)])),
             L(outline([(2, 40), (24, 44), (36, 116), (-10, 116)]), 'shade', 'b', False),
             L(outline([(4, 42), (90, 42), (92, 48), (4, 48)]), WHITE, 'f', ln=True), L(ell(88, 45, 4, 4), 'gem', 'f', ln=True),
             fringe([(70, 44), (92, 46), (94, 64), (86, 62)])],
    'back': [L(outline([(4, 120), (2, 60), (8, 20), (26, 0), (50, -6), (74, 0), (92, 20), (98, 60), (96, 120)])),
             L(outline([(56, 0), (88, 18), (96, 60), (94, 118), (64, 118)]), 'shade', 'b', False),
             L(outline([(4, 46), (96, 46), (96, 50), (4, 50)]), WHITE, 'f', ln=True)],
}

# Jacqueline Rabbit: gorro negro ajustado con una estrella turquesa y el borde blanco alrededor de la cara; dos coletas
# castañas de puntas que salen tiesas hacia los lados y un mechón en la frente; ojos naranjas grandes
_tail_jr = [(12, 36), (-8, 22, 1), (-4, 32), (-30, 26, 1), (-16, 40), (-36, 50, 1), (-14, 52), (-26, 66, 1), (-2, 56), (10, 50)]
CHARS['jacqueline-rabbit'] = {
    'body': 'chica', 'pal': pal('#a0602a', '#fce0c4', iris='#d8701e', hat='#1e1e24', star='#5ad8c0'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline(_tail_jr)), L(outline(mirror_pts(_tail_jr))),
              L(outline([(8, 86), (6, 30), (18, 8), (50, -2), (82, 8), (94, 30), (92, 86), (84, 90), (84, 60), (16, 60), (16, 90)]), 'hat', 'f'),
              L(outline([(18, 100), (12, 62), (22, 42), (50, 34), (78, 42), (88, 62), (82, 100), (76, 98), (80, 64), (70, 50), (50, 46), (30, 50), (20, 64),
                         (24, 98)]), WHITE, 'f', ln=True),
              L(outline([(50, 8), (53, 15), (60, 15), (55, 20), (57, 27), (50, 23), (43, 27), (45, 20), (40, 15), (47, 15)]), 'star', 'f', ln=True),
              fringe([(40, 50), (56, 48), (60, 66, 1), (52, 58), (46, 64, 1)])],
    'side': [L(outline([(30, 30), (16, 12, 1), (14, 26), (-8, 16, 1), (2, 34), (-14, 40, 1), (4, 46), (-6, 58, 1), (20, 52), (34, 44)])),
             L(outline([(52, 90), (52, 60), (62, 48), (88, 46), (92, 24), (76, 4), (48, -4), (22, 4), (6, 26), (4, 60), (16, 84), (36, 92)]), 'hat', 'f'),
             L(outline([(60, 92), (58, 60), (68, 46), (90, 44), (92, 52), (72, 54), (66, 64), (68, 92)]), WHITE, 'f', ln=True)],
    'back': [L(outline([(16, 40), (-10, 26, 1), (-6, 36), (-36, 30, 1), (-20, 44), (-40, 56, 1), (-16, 56), (-28, 72, 1), (-2, 60), (14, 56)])),
             L(outline([(84, 40), (110, 26, 1), (106, 36), (136, 30, 1), (120, 44), (140, 56, 1), (116, 56), (128, 72, 1), (102, 60), (86, 56)])),
             L(outline([(10, 70), (8, 30), (20, 8), (50, -2), (80, 8), (92, 30), (90, 70), (70, 88), (30, 88)]), 'hat', 'f')],
}

# Bert Trapper: pelo verde azulado revuelto de mechones en punta que le tapa la frente, y un antifaz rojo oscuro sobre los ojos
CHARS['bert-trapper'] = {
    'body': 'normal', 'pal': pal('#2a7a7a', '#f2c090', iris='#1e1414', mask='#8a2a2a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': messy('front', 12, 10, seed=411, rx=52, ry=42, cy=40, lo=70)
             + [fringe([(10, 64), (12, 36), (30, 18), (50, 12), (70, 18), (88, 36), (90, 64), (80, 54), (74, 66, 1), (66, 50), (58, 64, 1), (52, 48), (44, 64, 1),
                        (38, 50), (30, 64, 1), (22, 52)]),
                L(outline([(14, 70), (30, 66), (50, 72), (70, 66), (86, 70), (84, 82), (70, 86), (50, 80), (30, 86), (16, 82)]), 'mask', 'f', ln=True)]
             + white_eyes(76, 15, 5, 4, 1.8),
    'side': messy('side', 12, 9, seed=411, rx=48, ry=42, cy=40, nape=90, sweep=-0.3)
            + [fringe([(66, 4), (90, 18), (96, 42), (94, 62, 1), (86, 50), (80, 60, 1), (76, 42)]),
               L(outline([(74, 70), (94, 68), (94, 82), (76, 82)]), 'mask', 'f', ln=True)] + side_eye(76),
    'back': messy('back', 12, 10, seed=411, rx=52, ry=42, cy=40, nape=92),
}
