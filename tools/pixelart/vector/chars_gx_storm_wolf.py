"""Storm Wolves (gx-storm-wolf, Uzbekistán): sus modelos 3D de Inazuma Eleven GO Galaxy como referencia (busto de frente,
perfil y espalda, con la rejilla de unidades de cabeza). Claves de equipo ('gx-storm-wolf:<id>'): varios ids son cortos
(aaron, yuri, server...) y con el id a secas podrían quedarse con los dibujos de otros por prefijo."""
from chars import CHARS, L, OUTC, ell, outline, pal, strand  # noqa: F401
from heads import quad

T = 'gx-storm-wolf'
WHITE = (250, 250, 250, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Aleksei Karimov (portero): pañuelo verde oscuro atado a la nuca que le tapa todo el pelo; por debajo asoman las patillas
# castañas largas y un pico de pelo en la frente; perilla castaña, ojos cerrados y cejas fruncidas
CHARS[f'{T}:aleksei-karimov'] = {
    'body': 'normal', 'pal': pal('#4a2e1c', '#fce2b8', band='#2e4a24', band_d='#1c3016', band_l='#4a6a36'),
    'face': {'eyes': 'closed', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 92, 'hairline': False},
    'front': [L(outline([(14, 48), (20, 50), (22, 86), (17, 90, 1), (12, 70)]), 'mid', 'f'),
              L(outline([(86, 48), (80, 50), (78, 86), (83, 90, 1), (88, 70)]), 'mid', 'f'),
              L(outline([(14, 48), (11, 22), (22, 2), (50, -8), (78, 2), (89, 22), (86, 48), (50, 40)]), 'band', 'f', ln=True),
              L(outline([(56, -4), (78, 4), (88, 24), (86, 44), (70, 42), (68, 12)]), 'band_d', 'f', False),
              L(outline([(22, 10), (40, 0), (34, 14)]), 'band_l', 'f', False),
              fringe([(38, 42), (44, 44), (50, 58, 1), (56, 44), (62, 42), (50, 40)]),
              L(outline([(40, 98), (50, 95), (60, 98), (58, 106), (50, 113, 1), (42, 106)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(10, 58), (28, 56), (30, 80), (18, 84), (10, 74)]), 'mid', 'b'),
             L(outline([(52, 46), (60, 46), (58, 82), (54, 88, 1)]), 'mid', 'f'),
             L(outline([(6, 64), (2, 34), (16, 8), (46, -6), (76, 2), (92, 22), (94, 40), (70, 44), (40, 46), (18, 56)]), 'band', 'f', ln=True),
             L(outline([(4, 60), (-4, 74), (-8, 96, 1), (2, 82), (8, 70)]), 'band_d', 'f', ln=True),
             L(outline([(4, 40), (24, 30), (40, 44), (18, 54)]), 'band_d', 'f', False),
             L(outline([(76, 98), (86, 96), (84, 106), (78, 110, 1)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(18, 70), (82, 70), (78, 90), (60, 94), (40, 94), (22, 90)]), 'mid'),
             L(outline([(14, 78), (10, 30), (22, 4), (50, -6), (78, 4), (90, 30), (86, 78), (50, 82)]), 'band', 'f', ln=True),
             L(outline([(56, -2), (80, 6), (90, 34), (86, 66), (64, 70)]), 'band_d', 'f', False),
             L(outline([(42, 60), (50, 66), (58, 60), (62, 74), (56, 92, 1), (50, 74), (44, 92, 1), (38, 74)]), 'band_d', 'f', ln=True)],
}

# Server: pelo castaño oliva de pinchos altos hacia arriba, con un mechón gris en el lado derecho y las sienes cortas;
# piel morena, orejas grandes, una cicatriz en la frente, nariz larga, perilla pequeña y cejas muy fruncidas
CHARS[f'{T}:server'] = {
    'body': 'normal', 'pal': pal('#5e5428', '#e8a064', iris='#1e1414', streak='#a8a4ae'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'big_ears': 2, 'ear_out': 3,
             'hairline': False},
    'front': [L(outline([(16, 62), (16, 20), (50, 8), (84, 20), (84, 62)]), 'skin', 'b', False),
              L(outline([(14, 64), (8, 30), (12, 2), (20, -30, 1), (30, -12), (38, -38, 1), (48, -16), (56, -42, 1), (64, -16), (74, -34, 1), (80, -8),
                         (90, 16), (92, 64), (86, 64), (84, 30), (80, 22), (70, 26), (60, 16), (52, 26), (44, 18), (36, 30), (28, 22), (18, 30), (16, 64)])),
              L(outline([(60, -14), (82, -6), (92, 20), (90, 60), (80, 30)]), 'shade', 'b', False),
              L(outline([(60, -12), (66, -26, 1), (72, -2), (76, 26), (70, 28), (64, 6)]), 'streak', 'b', ln=True),
              L(quad((38, 42), (52, 38), (66, 42)), OUTC, 'f', False, False, 1.0),
              L([(48, 56), (47, 78), (53, 80)], OUTC, 'f', False, False, 1.2),
              L(outline([(42, 100), (50, 98), (58, 100), (55, 106), (50, 110, 1), (45, 106)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(56, 60), (60, 40), (78, 34), (90, 22), (98, 6, 1), (84, 4), (88, -14, 1), (70, -10), (62, -34, 1), (50, -16), (30, -36, 1), (26, -10),
                        (6, -14, 1), (8, 10), (-6, 22, 1), (4, 34), (0, 56), (12, 72), (34, 66)])),
             L(outline([(2, 30), (22, 34), (24, 64), (8, 60)]), 'shade', 'b', False),
             L(outline([(52, -8), (64, -26, 1), (66, -4), (60, 14)]), 'streak', 'b', ln=True),
             L(outline([(78, 98), (86, 96), (84, 104), (80, 108, 1)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(14, 74), (10, 32), (20, -6), (36, -30, 1), (44, -14), (52, -40, 1), (60, -14), (70, -32, 1), (80, -4), (90, 32), (86, 74), (50, 82)])),
             L(outline([(56, -10), (80, -2), (90, 36), (84, 70), (62, 78)]), 'shade', 'b', False),
             L(outline([(26, -14), (32, -28, 1), (38, -6), (34, 20), (28, 18)]), 'streak', 'b', ln=True)],
}

# Mirjalor Afonin: melena larga ondulada granate que le cae por los hombros, con un flequillo espeso a mechones que le tapa
# la frente y parte del ojo derecho; piel morena, ojos azules y sonrisa de dientes
CHARS[f'{T}:mirjalor-afonin'] = {
    'body': 'normal', 'pal': pal('#8a3048', '#d8904e', iris='#2a5a9a', shade='#6a2238', light='#b05068'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(2, 116), (-8, 100, 1), (0, 84), (-4, 64), (4, 36), (14, 10), (36, -6), (64, -6), (86, 8), (96, 36), (100, 64), (108, 88), (100, 92),
                         (106, 110, 1), (94, 104), (96, 116, 1), (84, 112), (80, 82), (20, 82), (16, 112)])),
              L(outline([(60, -2), (86, 10), (98, 40), (100, 90), (88, 100), (82, 60)]), 'shade', 'b', False),
              fringe([(12, 82, 1), (10, 50), (18, 24), (40, 10), (64, 12), (84, 26), (90, 52), (88, 82, 1), (80, 62), (74, 50), (70, 64, 1), (62, 46), (56, 78, 1),
                      (50, 46), (40, 58, 1), (34, 44), (24, 66, 1), (20, 54)]),
              L(outline([(56, 18), (78, 28), (86, 50), (74, 44)]), 'shade', 'f', False), L(outline([(26, 26), (44, 18), (36, 32)]), 'light', 'f', False),
              strand([(48, 20), (56, 50), (56, 76)], 'shade', 'f', 1.0)],
    'side': [L(outline([(56, 60), (60, 46), (80, 46), (92, 34), (88, 12), (66, -4), (36, -6), (12, 8), (0, 34), (-6, 70), (-10, 100), (-4, 116, 1), (6, 104),
                        (16, 120, 1), (24, 100), (34, 116, 1), (40, 92), (46, 78)])),
             L(outline([(-4, 50), (20, 48), (30, 100), (6, 108)]), 'shade', 'b', False),
             strand([(4, 40), (2, 80), (-2, 104)], 'deep', 'b', 1.0), strand([(20, 30), (22, 70), (18, 100)], 'deep', 'b', 1.0),
             fringe([(66, 2), (90, 18), (96, 44), (92, 74, 1), (86, 56), (80, 70, 1), (76, 46), (66, 32)])],
    'back': [L(outline([(0, 116), (-8, 98, 1), (0, 84), (-4, 60), (6, 30), (16, 6), (40, -6), (64, -6), (86, 8), (98, 36), (100, 64), (106, 88, 1), (98, 92),
                        (104, 116, 1), (84, 112), (68, 120, 1), (52, 110), (36, 120, 1), (20, 110)])),
             L(outline([(56, -2), (86, 10), (100, 46), (100, 108), (66, 114), (70, 50)]), 'shade', 'b', False),
             strand([(30, 30), (24, 70), (28, 110)], 'deep', 'b', 1.0), strand([(70, 30), (76, 70), (72, 110)], 'deep', 'b', 1.0)],
}

# Yuri: pelo blanco con sombras malva en forma de casco, cortado recto por los lados con el borde abierto hacia fuera, mechones
# largos que le caen por la cara y una trenza fina con una anilla dorada a un lado; piel clara, ojos verde grisáceo y sonrisa
CHARS[f'{T}:yuri'] = {
    'body': 'normal', 'pal': pal('#ece8f0', '#fcecc8', iris='#7a9a88', shade='#c8b4c4', deep='#a890a8', light='#ffffff', ring='#d8b040'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 76), (6, 74, 1), (10, 40), (20, 14), (50, 6), (80, 14), (92, 40), (96, 74, 1), (86, 76), (84, 56), (16, 56)])),
              L(outline([(58, 10), (82, 18), (92, 44), (90, 70), (80, 44)]), 'shade', 'b', False),
              L(outline([(70, 84), (78, 82), (80, 98), (76, 112), (72, 118, 1), (68, 106), (68, 94)]), 'mid', 'f', ln=True),
              L(outline([(68, 100), (78, 100), (78, 104), (68, 104)]), 'ring', 'f', ln=True),
              strand([(70, 90), (78, 92)], 'deep', 'f', 1.0), strand([(69, 110), (77, 112)], 'deep', 'f', 1.0),
              fringe([(12, 80, 1), (12, 44), (24, 22), (48, 14), (74, 20), (88, 40), (90, 80, 1), (84, 62), (80, 72, 1), (74, 50), (66, 66, 1), (60, 46), (52, 62, 1),
                      (46, 42), (38, 64, 1), (32, 48), (24, 70, 1), (20, 56)]),
              strand([(30, 22), (26, 60)], 'deep', 'f', 1.0), strand([(66, 22), (72, 56)], 'deep', 'f', 1.0)],
    'side': [L(outline([(54, 62), (58, 50), (80, 48), (92, 36), (86, 14), (62, 2), (34, 2), (12, 14), (2, 40), (-2, 64), (-8, 72, 1), (8, 74), (30, 80), (46, 74)])),
             L(outline([(0, 44), (26, 46), (32, 76), (6, 72)]), 'shade', 'b', False),
             fringe([(64, 4), (88, 16), (94, 40), (92, 80, 1), (84, 60), (80, 72, 1), (76, 46), (64, 32)])],
    'back': [L(outline([(10, 70), (2, 72, 1), (6, 40), (18, 12), (50, 4), (82, 12), (94, 40), (98, 72, 1), (90, 70), (50, 76)])),
             L(outline([(56, 6), (84, 14), (94, 46), (90, 66), (62, 70)]), 'shade', 'b', False),
             strand([(30, 10), (24, 66)], 'deep', 'b', 1.0), strand([(70, 10), (76, 66)], 'deep', 'b', 1.0),
             L(outline([(26, 72), (32, 72), (32, 100), (28, 106, 1), (24, 98)]), 'shade', 'f', ln=True),
             L(outline([(68, 72), (74, 72), (76, 98), (72, 106, 1), (68, 100)]), 'shade', 'f', ln=True)],
}

# Kenja Jo'rayev: grandullón de piel morena con un casco de pelo morado oscuro que le cae recto por los lados hasta la
# mandíbula, con un pico en la frente; cara ancha y baja, orejas enormes, ojos pequeños furiosos y arrugas en el entrecejo
KENJA_FACE = outline([(18, 60), (34, 52), (50, 58), (66, 52), (82, 60), (84, 96), (76, 112), (60, 118), (40, 118), (24, 112), (16, 96)])
CHARS[f'{T}:kenja-jo-rayev'] = {
    'body': 'corpulento', 'pal': pal('#5a4a7a', '#e09048', iris='#1e1414', shade='#3e3258', skin_d='#c07834'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 110, 'eye_y': 84, 'face_front': KENJA_FACE, 'big_ears': 4, 'ear_out': 9,
             'hairline': False},
    'front': [L(outline([(12, 112), (8, 80), (12, 40), (20, 24), (50, 18), (80, 24), (88, 40), (92, 80), (88, 112), (50, 116)])),
              L(outline([(58, 20), (80, 26), (90, 50), (90, 104), (82, 80)]), 'shade', 'b', False),
              fringe([(16, 66), (18, 34), (30, 24), (50, 20), (70, 24), (82, 34), (84, 66), (76, 58), (62, 50), (54, 54), (50, 64, 1), (46, 54), (38, 50), (24, 58)]),
              fringe([(14, 60), (22, 62), (22, 104), (16, 114, 1), (10, 104)]), fringe([(86, 60), (78, 62), (78, 104), (84, 114, 1), (90, 104)]),
              L([(44, 70), (48, 76)], OUTC, 'f', False, False, 1.2), L([(56, 70), (52, 76)], OUTC, 'f', False, False, 1.2),
              L(quad((44, 98), (50, 102), (56, 98)), OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(58, 56), (66, 44), (86, 42), (96, 28), (90, 14), (66, 4), (36, 4), (14, 14), (6, 40), (4, 80), (6, 112), (36, 116), (48, 100), (52, 72)])),
             L(outline([(6, 40), (30, 44), (36, 110), (8, 110)]), 'shade', 'b', False),
             L(outline([(84, 26), (96, 26), (100, 18, 1), (92, 12)]), 'mid', 'f', ln=True),
             L(quad((84, 100), (90, 104), (94, 102)), OUTC, 'f', False, False, 1.2)],
    'back': [L(outline([(12, 112), (8, 80), (12, 40), (22, 22), (50, 16), (78, 22), (88, 40), (92, 80), (88, 112), (50, 116)])),
             L(outline([(56, 18), (80, 24), (90, 50), (90, 108), (62, 112)]), 'shade', 'b', False)],
}

# Leonid Mirzayev: melena rubia muy abultada, peinada hacia la derecha con pinchos que salen por arriba y por el lado
# derecho, mechones largos que le enmarcan la cara hasta el cuello y sombras castañas detrás; ojos violeta
CHARS[f'{T}:leonid-mirzayev'] = {
    'body': 'normal', 'pal': pal('#f0d08a', '#fce0c0', iris='#6a5aa8', shade='#c8a070', deep='#a87850', light='#fff0c0'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(14, 112), (4, 80), (4, 44), (12, 14), (26, -4), (42, -12), (50, -38, 1), (58, -10), (74, -22, 1), (80, 0), (96, 20), (104, 28, 1), (94, 40),
                         (102, 56), (106, 70, 1), (92, 72), (90, 100), (84, 112), (78, 90), (22, 90)])),
              L(outline([(60, -6), (86, 10), (100, 40), (92, 100), (82, 70)]), 'shade', 'b', False),
              fringe([(14, 66), (14, 34), (28, 14), (56, 6), (80, 16), (94, 34), (86, 42), (72, 30), (56, 30), (42, 40), (32, 58, 1), (28, 46), (22, 66, 1)]),
              fringe([(12, 50), (26, 52), (26, 96), (16, 112, 1), (10, 92)]), fringe([(76, 44), (88, 46), (92, 96), (82, 110, 1), (78, 84)]),
              L(outline([(28, 12), (52, 6), (40, 18)]), 'light', 'f', False), L(outline([(60, 12), (82, 20), (90, 34), (74, 28)]), 'shade', 'f', False)],
    'side': [L(outline([(56, 62), (60, 48), (80, 48), (92, 34), (90, 12), (74, -2), (80, -20, 1), (58, -8), (46, -30, 1), (36, -6), (14, 2), (-6, 4, 1), (4, 20),
                        (-12, 40, 1), (2, 50), (-12, 66, 1), (4, 74), (0, 96, 1), (16, 88), (20, 112, 1), (30, 92), (44, 80)])),
             L(outline([(0, 30), (24, 36), (30, 86), (8, 84)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 40), (92, 70, 1), (86, 54), (80, 66, 1), (76, 46), (66, 32)])],
    'back': [L(outline([(16, 112), (6, 84), (-10, 72, 1), (6, 60), (-14, 44, 1), (8, 34), (6, 10), (20, -6), (36, -2), (46, -30, 1), (54, -6), (72, -20, 1),
                        (80, 0), (96, 20), (100, 50), (96, 84), (88, 110), (66, 106), (52, 118, 1), (36, 106)]), 'shade'),
             L(outline([(20, -6), (36, -2), (46, -30, 1), (54, -6), (72, -20, 1), (80, 0), (94, 20), (70, 24), (50, 20), (30, 30), (8, 30), (6, 10)]), 'mid', 'b', False)],
}

# Rustan: tupé verde azulado en lo alto con un rizo arriba a la derecha y los lados y la nuca rapados en gris; sonrisa de
# dientes, ojos grandes y cejas fruncidas
CHARS[f'{T}:rustan'] = {
    'body': 'normal', 'pal': pal('#2e8a74', '#fcd8b0', iris='#1e1414', shade='#1e6454', light='#5ab098', under='#6a6874', under_d='#555360'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 94, 'hairline': (44, 38)},
    'front': [L(outline([(16, 74), (12, 40), (88, 40), (86, 74), (80, 56), (20, 56)]), 'under'),
              L(outline([(12, 44), (8, 24), (14, 6), (26, -8), (44, -16), (58, -20), (66, -26), (80, -26), (86, -16), (80, -8), (88, 6), (92, 24), (88, 44), (70, 36),
                         (50, 40), (30, 36)])),
              L(outline([(58, -16), (80, -8), (90, 14), (88, 38), (74, 34), (70, 6)]), 'shade', 'b', False),
              L(outline([(20, 4), (40, -10), (32, 6)]), 'light', 'b', False),
              L(ell(74, -18, 5, 5) + [ell(74, -18, 5, 5)[0]], 'shade', 'b', False, False, 2.2),
              strand([(24, 30), (34, 0), (56, -12)], 'shade', 'b', 1.2), strand([(50, 36), (58, 6), (70, -6)], 'shade', 'b', 1.2)],
    'side': [L(outline([(56, 60), (60, 46), (44, 40), (12, 40), (8, 66), (20, 86), (40, 82), (50, 72)]), 'under'),
             L(outline([(4, 46), (2, 24), (14, 0), (36, -18), (62, -24), (84, -14), (94, 4), (94, 26), (84, 34), (60, 36), (30, 40)])),
             L(outline([(4, 40), (8, 18), (30, 24), (40, 38)]), 'shade', 'b', False),
             L(ell(54, -16, 6, 5) + [ell(54, -16, 6, 5)[0]], 'shade', 'b', False, False, 2.2)],
    'back': [L(outline([(16, 44), (84, 44), (86, 76), (76, 94), (50, 100), (24, 94), (14, 76)]), 'under'),
             L(outline([(56, 46), (84, 46), (84, 76), (62, 96)]), 'under_d', 'b', False),
             L(outline([(10, 46), (12, 16), (28, -8), (50, -18), (72, -8), (88, 16), (90, 46), (70, 52), (50, 46), (30, 52)])),
             L(outline([(56, -14), (78, -4), (90, 22), (88, 44), (66, 50)]), 'shade', 'b', False)],
}

# Aaron: pelo castaño oliva espeso con pinchos que salen hacia los lados arriba y abajo, mechones largos que le tapan las
# mejillas, un pico en la frente y barba de pocos días; boca abierta gritando y ojos violeta
CHARS[f'{T}:aaron'] = {
    'body': 'normal', 'pal': pal('#6a6a36', '#f8c890', iris='#6a4a8a', shade='#4e4e26', light='#8e8e52'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 94), (6, 98, 1), (14, 84), (2, 80, 1), (12, 70), (10, 50), (-6, 34, 1), (10, 34), (2, 20, 1), (16, 18), (26, 4), (50, 0), (74, 4),
                         (84, 18), (98, 20, 1), (90, 34), (106, 34, 1), (90, 50), (88, 70), (98, 80, 1), (86, 84), (94, 98, 1), (84, 94), (80, 64), (20, 64)])),
              L(outline([(58, 2), (84, 16), (92, 40), (88, 84), (80, 50)]), 'shade', 'b', False),
              fringe([(14, 62), (16, 32), (28, 18), (50, 14), (72, 18), (84, 32), (86, 62), (78, 54), (72, 46), (62, 44), (50, 58, 1), (38, 44), (28, 46), (22, 54)]),
              fringe([(14, 58), (22, 60), (24, 88), (16, 96, 1)]), fringe([(86, 58), (78, 60), (76, 88), (84, 96, 1)]),
              L(outline([(26, 26), (46, 18), (38, 30)]), 'light', 'f', False),
              L([(26, 86), (28, 92)], OUTC, 'f', False, False, 1.0), L([(74, 86), (72, 92)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(56, 62), (60, 48), (80, 48), (92, 34), (88, 12), (66, -2), (36, -2), (14, 10), (6, 30), (-8, 36, 1), (4, 46), (4, 76), (-12, 88, 1), (10, 88),
                        (26, 96), (40, 84), (50, 74)])),
             L(outline([(4, 40), (26, 46), (30, 86), (8, 84)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 16), (96, 40), (92, 60, 1), (84, 48), (80, 92, 1), (74, 60), (66, 32)])],
    'back': [L(outline([(16, 94), (2, 96, 1), (12, 82), (6, 50), (-6, 36, 1), (8, 34), (4, 20, 1), (16, 16), (28, 4), (50, 0), (72, 4), (84, 16), (96, 20, 1), (92, 34),
                        (106, 36, 1), (94, 50), (88, 82), (98, 96, 1), (84, 94), (50, 98)])),
             L(outline([(56, 2), (84, 16), (94, 44), (88, 90), (62, 96)]), 'shade', 'b', False)],
}

# Maksim Alimatov: pelo rubio de pinchos altos hacia arriba, con los lados y la nuca en sombra castaña, orejas grandes y una
# perilla rubia; cejas muy fruncidas
CHARS[f'{T}:maksim-alimatov'] = {
    'body': 'normal', 'pal': pal('#d8c47a', '#fcdcb4', iris='#1e1414', shade='#9a7a54', light='#f0e0a0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'big_ears': 2, 'ear_out': 3,
             'hairline': False},
    'front': [L(outline([(16, 62), (16, 20), (50, 8), (84, 20), (84, 62)]), 'skin', 'b', False),
              L(outline([(16, 82), (8, 74, 1), (14, 62), (10, 40), (14, 12), (20, -8, 1), (30, 4), (40, -24, 1), (48, -6), (54, -30, 1), (62, -8), (72, -22, 1), (76, 4),
                         (86, 8, 1), (86, 36), (90, 62), (96, 74, 1), (86, 82), (84, 62), (82, 42), (72, 34), (60, 40), (50, 36), (40, 40), (28, 34), (18, 42), (16, 62)])),
              L(outline([(10, 40), (20, 34), (22, 74), (14, 80)]), 'shade', 'b', False), L(outline([(90, 40), (80, 34), (78, 74), (86, 80)]), 'shade', 'b', False),
              L(outline([(46, -2), (54, -26), (58, 0), (52, 20)]), 'light', 'b', False),
              L(outline([(40, 98), (50, 96), (60, 98), (56, 106), (50, 110, 1), (44, 106)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(56, 60), (62, 44), (80, 40), (92, 26), (96, 4, 1), (82, 6), (84, -14, 1), (66, -4), (58, -26, 1), (46, -6), (26, -14, 1), (24, 6), (2, 6, 1),
                        (10, 22), (-12, 40, 1), (6, 46), (-6, 62, 1), (10, 66), (8, 84, 1), (24, 80), (40, 76), (50, 70)]), 'shade'),
             L(outline([(46, -6), (58, -26, 1), (66, -4), (84, -14, 1), (82, 6), (92, 24), (76, 30), (60, 20), (44, 12)]), 'mid', 'b', False),
             L(outline([(78, 98), (86, 96), (84, 104), (80, 108, 1)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(14, 84), (10, 50), (2, 64, 1), (6, 34), (10, 6), (22, -8, 1), (32, 2), (44, -20, 1), (52, -4), (62, -22, 1), (72, 0), (84, -8, 1), (88, 20),
                        (92, 50), (100, 64, 1), (90, 66), (86, 84), (50, 90)]), 'shade'),
             L(outline([(22, -8), (32, 2), (44, -20, 1), (52, -4), (62, -22, 1), (72, 0), (84, -8, 1), (88, 20), (70, 24), (50, 16), (30, 22), (10, 20)]), 'mid', 'b', False)],
}

# Dilshod: melena gris larga y salvaje de mechones en punta, con el flequillo cayéndole entre los ojos y mechones largos
# delante de los hombros; piel muy clara, ojos dorados y sonrisa con un colmillo
CHARS[f'{T}:dilshod'] = {
    'body': 'normal', 'pal': pal('#8a8a92', '#fcecd4', iris='#a89a3a', shade='#6a5a62', deep='#4e4048', light='#b4b4bc'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 112), (2, 90), (-6, 62, 1), (4, 50), (-2, 30, 1), (10, 22), (14, 2), (30, -10, 1), (40, 4), (50, -12), (62, 2), (76, -6, 1), (84, 10),
                         (100, 26, 1), (92, 40), (102, 64, 1), (92, 74), (96, 100), (88, 112), (80, 84), (20, 84)])),
              L(outline([(60, -2), (84, 10), (98, 40), (94, 104), (82, 70)]), 'shade', 'b', False),
              fringe([(12, 72), (12, 34), (28, 16), (50, 10), (72, 16), (88, 34), (88, 72), (80, 56), (74, 68, 1), (66, 48), (56, 58), (50, 86, 1), (46, 56), (36, 64, 1),
                      (30, 50), (20, 68, 1)]),
              fringe([(12, 66), (24, 70), (26, 104), (18, 116, 1), (10, 96)]), fringe([(88, 66), (76, 70), (76, 104), (84, 116, 1), (90, 96)]),
              L(outline([(26, 18), (46, 12), (38, 24)]), 'light', 'f', False),
              L(outline([(55, 95), (59, 95), (57, 100, 1)]), WHITE, 'f', False)],
    'side': [L(outline([(56, 62), (60, 48), (80, 46), (92, 34), (88, 10), (98, -2, 1), (72, 0), (60, -16, 1), (44, -2), (20, -14, 1), (20, 6), (-12, 0, 1), (6, 22),
                        (-16, 40, 1), (2, 50), (-12, 70, 1), (2, 76), (-4, 100, 1), (12, 92), (14, 114, 1), (26, 96), (36, 108, 1), (44, 86)])),
             L(outline([(0, 40), (24, 44), (30, 96), (6, 96)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 42), (94, 72, 1), (86, 56), (82, 104, 1), (76, 64), (66, 34)])],
    'back': [L(outline([(10, 112), (0, 86), (-8, 60, 1), (4, 50), (-4, 30, 1), (10, 22), (16, 0), (30, -10, 1), (40, 4), (50, -12), (62, 2), (76, -8, 1), (84, 10),
                        (102, 28, 1), (94, 44), (104, 66, 1), (94, 76), (98, 104), (88, 114), (70, 104), (56, 118, 1), (44, 104), (28, 116, 1)]), 'shade'),
             L(outline([(16, 0), (30, -10, 1), (40, 4), (50, -12), (62, 2), (76, -8, 1), (84, 10), (96, 30), (70, 30), (50, 20), (30, 30), (8, 30)]), 'mid', 'b', False),
             strand([(30, 34), (24, 70), (28, 106)], 'deep', 'b', 1.0), strand([(70, 34), (76, 70), (72, 106)], 'deep', 'b', 1.0)],
}

# Zafar: melena lisa larguísima blanco lavanda que le cae por la izquierda tapándole media cara, y recogida detrás en una
# coleta larga; piel oscura, un solo ojo a la vista y la oreja derecha descubierta
CHARS[f'{T}:zafar'] = {
    'body': 'normal', 'pal': pal('#e2e2f4', '#b07040', iris='#2a1e1a', shade='#a890a8', deep='#806a84', light='#ffffff'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(4, 106), (-2, 84), (2, 40), (12, 8), (36, -12), (62, -12), (82, 0), (94, 26), (96, 60), (102, 100, 1), (90, 96), (86, 70), (82, 40), (60, 30)])),
              L(outline([(60, -8), (82, 2), (94, 30), (96, 70), (88, 74), (82, 36)]), 'shade', 'b', False),
              fringe([(0, 102, 1), (4, 60), (10, 22), (30, 0), (56, -6), (64, 8), (58, 28), (54, 56), (52, 84), (44, 100), (34, 114, 1), (26, 100), (16, 112, 1), (10, 100)]),
              strand([(22, 10), (16, 60), (14, 100)], 'shade', 'f', 1.2), strand([(40, 4), (36, 60), (30, 104)], 'shade', 'f', 1.2),
              L(outline([(30, 4), (48, -2), (40, 10)]), 'light', 'f', False)],
    'side': [L(outline([(56, 60), (60, 46), (80, 44), (92, 30), (90, 6), (70, -10), (40, -12), (14, 0), (0, 30), (-6, 70), (-10, 110, 1), (4, 96), (10, 116, 1), (22, 96),
                        (30, 110, 1), (38, 86), (48, 74)])),
             L(outline([(-4, 44), (22, 48), (28, 100), (4, 104)]), 'shade', 'b', False),
             strand([(10, 20), (4, 70), (0, 106)], 'deep', 'b', 1.0), strand([(30, 10), (26, 60), (22, 100)], 'deep', 'b', 1.0),
             fringe([(62, -6), (90, 8), (96, 34), (94, 60, 1), (86, 44), (78, 32), (66, 20)])],
    'back': [L(outline([(6, 104), (0, 70), (4, 36), (14, 8), (36, -12), (64, -12), (86, 4), (96, 36), (100, 70), (96, 104), (80, 100), (66, 112, 1), (50, 98), (34, 112, 1),
                        (20, 100)]), 'shade'),
             L(outline([(14, 8), (36, -12), (64, -12), (86, 4), (94, 30), (70, 34), (50, 30), (30, 34), (6, 30)]), 'mid', 'b', False),
             L(outline([(44, 34), (56, 34), (58, 70), (56, 106), (50, 118, 1), (44, 106), (42, 70)]), 'mid', 'f', ln=True),
             L(outline([(44, 32), (56, 32), (56, 38), (44, 38)]), 'skin', 'f', ln=True)],
}

# Nikolai Gagarin: adulto de pelo caqui con pinchos arriba y un flequillo en zigzag, gafas rectangulares de montura azul
# marino, nariz larga, bigote y cejas fruncidas
CHARS[f'{T}:nikolai-gagarin'] = {
    'body': 'delgado', 'pal': pal('#a8a87a', '#fcdcb4', iris='#3a5a4a', shade='#7a6a4e', light='#c8c89a', nose='#e8c09a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 104, 'glasses': (42, 58, 90, 255), 'glasses_rect': True, 'big_ears': 2,
             'hairline': False},
    'front': [L(outline([(16, 62), (16, 20), (50, 8), (84, 20), (84, 62)]), 'skin', 'b', False),
              L(outline([(14, 92), (8, 60), (2, 30, 1), (12, 24), (14, 0), (28, -14), (40, -28, 1), (46, -14), (58, -24, 1), (66, -6), (82, 4), (96, 30, 1), (86, 36), (88, 60),
                         (86, 92), (82, 64), (84, 40), (70, 32), (56, 32), (52, 44), (40, 46), (44, 40), (34, 32), (18, 38), (18, 64)])),
              L(outline([(58, -10), (82, 6), (92, 32), (88, 88), (80, 50)]), 'shade', 'b', False),
              L([(50, 82), (48, 92), (54, 94)], OUTC, 'f', False, False, 1.2),
              L(outline([(36, 98), (50, 94), (64, 98), (66, 108), (58, 104), (50, 102), (42, 104), (34, 108)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(56, 62), (60, 48), (80, 44), (92, 30), (96, 16, 1), (82, 14), (74, -4), (56, -24, 1), (50, -8), (30, -12), (12, 0), (2, 30), (2, 62), (12, 84), (30, 90),
                        (44, 80)])),
             L(outline([(2, 34), (26, 40), (30, 84), (8, 80)]), 'shade', 'b', False),
             L(outline([(80, 100), (92, 98), (92, 108), (82, 106)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(16, 92), (8, 60), (4, 30), (14, 4), (30, -12), (40, -26, 1), (48, -10), (58, -22, 1), (68, -4), (86, 6), (96, 30), (90, 60), (86, 92), (60, 98), (50, 108, 1),
                        (40, 98)])),
             L(outline([(56, -8), (84, 8), (94, 36), (88, 88), (62, 94)]), 'shade', 'b', False)],
}
