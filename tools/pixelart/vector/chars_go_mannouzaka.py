"""Colegio Poderosa Fe (go-mannouzaka): sus modelos 3D de Inazuma Eleven GO como referencia (busto de frente, perfil y espalda).
F. Rimmer Jung no tiene modelo 3D: se dibuja a partir de su retrato."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from chars_alius import LONG_FACE, SKULL_B, SKULL_F, WIDE_FACE
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)
BLACK = (24, 22, 26, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Aum Nirvana (portero): piel morena y pelo verde agua recogido en un remolino enorme en forma de cebolla, con pétalos que
# acaban en punta arriba; un antifaz negro en los ojos, dos mechones finos a los lados y la boca en "o"
_onion = [(8, 62), (2, 36), (10, 10), (26, -10), (42, -22), (56, -30, 1), (64, -14), (80, -4), (94, 14), (98, 38), (92, 62), (70, 58), (50, 62), (30, 58)]
CHARS['aum-nirvana'] = {
    'body': 'normal', 'pal': pal('#4ab88a', '#b07a50', iris='#1e1414', shade='#2e8a64', light='#7ad8ac', lip='#8a3a3a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': [L(outline([(14, 60), (12, 92, 1), (18, 66)]), 'mid', 'f'), L(outline([(86, 60), (88, 92, 1), (82, 66)]), 'mid', 'f'),
              L(outline(_onion), 'mid', 'f'),
              L(outline([(56, -26), (64, -14), (80, -4), (94, 14), (98, 38), (92, 60), (76, 52), (70, 10)]), 'shade', 'f', False),
              L(outline([(20, 30), (40, 0), (54, -16), (44, 14), (28, 44)]), 'light', 'f', False),
              strand([(30, 54), (40, 20), (56, -10)], 'deep', 'f', 1.0), strand([(64, 56), (70, 20), (60, -6)], 'deep', 'f', 1.0),
              L(outline([(12, 64), (88, 64), (88, 78), (50, 80), (12, 78)]), BLACK, 'f', False),
              L(outline([(26, 70), (40, 68), (38, 74), (28, 74)]), WHITE, 'f', False), L(outline([(74, 70), (60, 68), (62, 74), (72, 74)]), WHITE, 'f', False),
              L(ell(50, 98, 4, 3.2), 'lip', 'f', ln=True), L(ell(50, 98, 1.8, 1.2), BLACK, 'f', False)],
    'side': [L(outline([(10, 66), (2, 40), (8, 12), (26, -8), (50, -18), (70, -26, 1), (76, -8), (90, 8), (98, 34), (92, 60), (70, 60), (50, 72), (36, 80), (20, 78)])),
             L(outline([(2, 36), (24, 40), (34, 76), (10, 68)]), 'shade', 'b', False),
             strand([(30, 70), (40, 30), (64, -10)], 'deep', 'b', 1.0),
             L(outline([(72, 64), (96, 66), (94, 78), (72, 78)]), BLACK, 'f', False), L(outline([(84, 70), (92, 70), (92, 74), (84, 74)]), WHITE, 'f', False)],
    'back': [L(outline([(8, 80), (2, 36), (10, 10), (26, -10), (44, -22), (50, -30, 1), (58, -18), (76, -8), (92, 12), (98, 38), (92, 80), (50, 88)])),
             L(outline([(56, -18), (76, -6), (94, 16), (96, 76), (70, 84), (66, 20)]), 'shade', 'b', False),
             strand([(50, -20), (36, 20), (34, 70)], 'deep', 'b', 1.0), strand([(50, -20), (64, 20), (66, 70)], 'deep', 'b', 1.0),
             strand([(10, 70), (50, 76), (90, 70)], 'deep', 'b', 1.0)],
}

# Adamant Walhalla: piel rojiza, pelo gris azulado peinado hacia atrás en surcos y largo por detrás, con mechones gruesos
# que le caen sobre los hombros a los lados; ojos blancos de párpado caído y los dientes apretados
CHARS['adamant-walhalla'] = {
    'body': 'corpulento', 'pal': pal('#8a92a8', '#d0784a', iris='#1e1414', light='#aab4c8'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 102, 'hairline': False, 'big_ears': 2},
    'front': [L(outline([(-24, 120), (-14, 98), (4, 92), (10, 70), (14, 30), (28, 8), (50, 0), (72, 8), (86, 30), (90, 70), (96, 92), (114, 98), (124, 120), (100, 116),
                         (86, 106), (84, 56), (16, 56), (14, 106), (0, 116)])),
              L(outline([(60, 4), (82, 16), (90, 60), (92, 96), (110, 104), (88, 104), (80, 40)]), 'shade', 'b', False),
              fringe([(14, 64), (16, 34), (28, 14), (50, 6), (72, 14), (84, 34), (86, 64), (78, 46), (64, 42), (50, 44), (36, 42), (22, 46)]),
              strand([(30, 42), (32, 20), (40, 10)], 'deep', 'f', 1.0), strand([(42, 42), (44, 18), (50, 8)], 'deep', 'f', 1.0),
              strand([(58, 42), (56, 18), (50, 8)], 'deep', 'f', 1.0), strand([(70, 42), (68, 20), (60, 10)], 'deep', 'f', 1.0),
              L([(30, 70), (40, 72)], OUTC, 'f', False, False, 1.4), L([(70, 70), (60, 72)], OUTC, 'f', False, False, 1.4)],
    'side': [L(outline([(54, 46), (66, 34), (72, 16), (56, 2), (30, 0), (10, 12), (2, 40), (0, 80), (-10, 110), (-30, 126, 1), (6, 118), (24, 104), (40, 86), (46, 62)])),
             L(outline([(2, 40), (26, 46), (36, 86), (6, 112)]), 'shade', 'b', False),
             strand([(14, 14), (66, 16)], 'deep', 'b', 1.0), strand([(6, 30), (68, 32)], 'deep', 'b', 1.0), strand([(4, 46), (52, 48)], 'deep', 'b', 1.0)],
    'back': [L(outline([(-24, 120), (-14, 100), (6, 90), (10, 60), (12, 30), (28, 8), (50, 0), (72, 8), (88, 30), (90, 60), (94, 90), (114, 100), (124, 120), (90, 116),
                        (66, 104), (50, 110), (34, 104), (10, 116)])),
             L(outline([(56, 4), (82, 16), (90, 60), (96, 96), (116, 108), (70, 104)]), 'shade', 'b', False),
             strand([(50, 4), (50, 60)], 'deep', 'b', 1.0), strand([(30, 14), (24, 60)], 'deep', 'b', 1.0), strand([(70, 14), (76, 60)], 'deep', 'b', 1.0),
             strand([(40, 70), (48, 104)], 'deep', 'b', 1.0), strand([(60, 70), (52, 104)], 'deep', 'b', 1.0)],
}

# Omega Elysium: grandullón con una mata de pelo morado explosiva enorme de puntas abiertas encima de una cinta gris
# atada en la frente, patillas moradas por las mejillas, nariz gorda y los dientes apretados
CHARS['omega-elysium'] = {
    'body': 'corpulento', 'pal': pal('#5a3a8a', '#f0dcb0', iris='#1e1414', band='#a0a8b0', band_d='#7a828c', nose='#c8806a', shade='#3e2668'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 100, 'hairline': False, 'nose': (50, 84, 5)},
    'front': [L(outline([(14, 66), (16, 92), (22, 96), (24, 66)]), 'mid', 'b'), L(outline([(86, 66), (84, 92), (78, 96), (76, 66)]), 'mid', 'b'),
              L(outline([(14, 54), (-6, 50), (-20, 36, 1), (-2, 30), (-16, 6, 1), (6, 4), (0, -20, 1), (22, -14), (26, -38, 1), (42, -20), (54, -40, 1), (62, -18), (80, -34, 1),
                         (82, -10), (106, -14, 1), (96, 6), (118, 10, 1), (102, 30), (120, 38, 1), (104, 50), (86, 54)]), 'mid', 'f'),
              L(outline([(60, -18), (82, -10), (100, 8), (104, 46), (86, 50), (76, 20)]), 'shade', 'f', False),
              L(outline([(14, 52), (50, 48), (86, 52), (86, 62), (50, 58), (14, 62)]), 'band', 'f', ln=True)],
    'side': [L(outline([(50, 54), (64, 52), (60, 30), (78, 22), (66, 6), (80, -18, 1), (52, -10), (40, -36, 1), (30, -12), (4, -26, 1), (8, 0), (-22, 0, 1), (-4, 20),
                        (-20, 40, 1), (0, 46), (-8, 70, 1), (14, 66), (20, 90), (34, 72), (44, 60)])),
             L(outline([(-4, 30), (20, 34), (24, 70), (0, 64)]), 'shade', 'b', False),
             L(outline([(14, 52), (62, 48), (62, 58), (14, 62)]), 'band', 'f', ln=True)],
    'back': [L(outline([(16, 92), (-4, 80), (-20, 56, 1), (-2, 46), (-22, 26, 1), (-4, 18), (-14, -8, 1), (14, -6), (14, -34, 1), (36, -16), (50, -40, 1), (64, -16),
                        (86, -34, 1), (86, -6), (114, -8, 1), (104, 18), (122, 26, 1), (102, 46), (120, 56, 1), (104, 80), (84, 92), (50, 98)])),
             L(outline([(56, -16), (86, -6), (104, 20), (104, 76), (84, 90), (66, 30)]), 'shade', 'b', False),
             L(outline([(14, 52), (50, 48), (86, 52), (86, 62), (50, 58), (14, 62)]), 'band_d', 'f', ln=True)],
}

# F. Rimmer Jung (sin modelo 3D: del retrato): piel morena, pelo azul marino oscuro de pinchos de punta hacia arriba y
# una mascarilla blanca en la boca; cejas fruncidas y ojos verdes
CHARS['f-rimmer-jung'] = {
    'body': 'normal', 'pal': pal('#1e2244', '#b07a4a', iris='#4a8a2a', mask='#f0f0f0', mask_d='#c8c8cc'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'hairline': False},
    'front': [L(outline([(16, 66), (6, 52), (2, 30), (8, 12), (16, 14), (18, -10, 1), (32, 4), (40, -22, 1), (50, 0), (62, -26, 1), (66, 0), (82, -14, 1), (84, 12),
                         (94, 14), (98, 30), (94, 52), (84, 66), (80, 56), (20, 56)])),
              L(outline([(60, -6), (82, 2), (96, 32), (90, 60), (78, 36)]), 'shade', 'b', False),
              fringe([(14, 60), (16, 36), (30, 22), (50, 18), (70, 22), (84, 36), (86, 60), (78, 46), (68, 54, 1), (62, 40), (52, 50, 1), (46, 38), (36, 52, 1), (30, 42),
                      (22, 56, 1)]),
              L(outline([(26, 88), (50, 84), (74, 88), (72, 104), (50, 110), (28, 104)]), 'mask', 'f', ln=True),
              L([(32, 94), (68, 94)], 'mask_d', 'f', False, False, 1.0), L([(34, 100), (66, 100)], 'mask_d', 'f', False, False, 1.0)],
    'side': [L(outline([(56, 56), (62, 44), (82, 42), (90, 26), (84, 6), (92, -14, 1), (68, -2), (60, -26, 1), (46, -6), (24, -22, 1), (20, 0), (-6, 4, 1), (8, 22),
                        (-6, 40, 1), (8, 48), (2, 70, 1), (20, 68), (30, 80), (44, 66)])),
             L(outline([(6, 36), (24, 42), (24, 66), (8, 58)]), 'shade', 'b', False),
             L(outline([(70, 86), (94, 84), (96, 104), (76, 106)]), 'mask', 'f', ln=True), L([(70, 90), (50, 80)], 'mask_d', 'f', False, False, 1.4)],
    'back': [L(outline([(16, 82), (4, 60), (2, 30), (8, 12), (16, 12), (18, -10, 1), (32, 4), (40, -22, 1), (50, 0), (62, -26, 1), (66, 0), (82, -14, 1), (84, 12),
                        (94, 14), (98, 30), (96, 60), (84, 82), (66, 92, 1), (58, 84), (50, 94, 1), (42, 84), (34, 92, 1)])),
             L(outline([(56, -2), (82, 4), (96, 34), (90, 78), (62, 86)]), 'shade', 'b', False),
             L([(14, 92), (50, 96), (86, 92)], 'mask', 'f', False, False, 1.6)],
}

# Zenith Shangrila: pelo azul marino en un casco de seta muy ancho y redondo, con flequillo recto, y la nuca rapada gris;
# cara pálida de ojos rojizos afilados
CHARS['zenith-shangrila'] = {
    'body': 'normal', 'pal': pal('#2a3a58', '#fcecd0', iris='#a84a22', buzz='#7a8080', shade='#1e2a42', light='#4a5a78'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(-2, 64), (-8, 50), (-4, 24), (12, 2), (34, -10), (50, -12), (66, -10), (88, 2), (104, 24), (108, 50), (102, 64), (84, 62), (50, 64), (16, 62)]), 'mid',
                'f'),
              L(outline([(64, -8), (90, 6), (104, 30), (104, 60), (86, 60), (80, 20)]), 'shade', 'f', False),
              L(outline([(18, 8), (40, -4), (30, 12)]), 'light', 'f', False),
              strand([(30, 60), (32, 20)], 'shade', 'f', 1.0), strand([(50, 62), (50, 14)], 'shade', 'f', 1.0), strand([(70, 60), (68, 20)], 'shade', 'f', 1.0)],
    'side': [L(outline([(14, 60), (26, 84), (44, 90), (54, 72), (50, 50)]), 'buzz'),
             L(outline([(-12, 62), (-14, 38), (-4, 12), (18, -6), (46, -12), (74, -6), (94, 10), (100, 34), (96, 62), (80, 64), (56, 58), (30, 66), (8, 62)])),
             L(outline([(-12, 40), (12, 44), (30, 62), (0, 62)]), 'shade', 'b', False)],
    'back': [L(outline([(26, 60), (24, 90), (50, 96), (76, 90), (74, 60)]), 'buzz'),
             L(outline([(-6, 64), (-10, 40), (-2, 16), (16, -2), (50, -12), (84, -2), (102, 16), (110, 40), (106, 64), (80, 70), (50, 64), (20, 70)])),
             L(outline([(-6, 50), (50, 40), (106, 50), (104, 64), (80, 70), (50, 64), (20, 70), (-4, 64)]), 'shade', 'b', False),
             L(outline([(20, 8), (50, 0), (34, 14)]), 'light', 'b', False)],
}

# Optimum Limbo: piel morena, cabeza rapada: lo alto gris verdoso, una franja negra por debajo con una raya naranja fina y
# las sienes grises; ojos verdes, cejas gruesas y perilla negra
CHARS['optimum-limbo'] = {
    'body': 'normal', 'pal': pal('#7a9488', '#b07a48', iris='#3a8a6a', band=BLACK, line='#d0882a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False, 'big_ears': 3, 'ear_out': 4},
    'front': [L(outline([(16, 58), (14, 34), (26, 12), (50, 4), (74, 12), (86, 34), (84, 58), (76, 52), (76, 40), (24, 40), (24, 52)]), 'band', 'f'),
              L(outline([(18, 30), (26, 12), (50, 4), (74, 12), (82, 30), (50, 24)]), 'mid', 'f'),
              L(quad((18, 32), (50, 24), (82, 32)), 'line', 'f', False, False, 1.4),
              L(outline([(14, 58), (22, 54), (22, 70), (14, 68)]), 'mid', 'f'), L(outline([(86, 58), (78, 54), (78, 70), (86, 68)]), 'mid', 'f'),
              L(outline([(42, 104), (58, 104), (56, 112), (44, 112)]), 'band', 'f', False)],
    'side': [L(outline([(12, 70), (10, 36), (26, 12), (54, 4), (78, 12), (86, 30), (60, 34), (54, 54), (48, 80), (30, 90), (14, 84)]), 'mid'),
             L(outline([(12, 30), (28, 12), (54, 4), (78, 12), (86, 26), (60, 30), (40, 30), (10, 50)]), 'band'),
             L(quad((14, 28), (50, 6), (84, 18)), 'line', 'f', False, False, 1.4),
             L(outline([(78, 104), (88, 104), (86, 112), (78, 110)]), 'band', 'f', False)],
    'back': [L(blob(SKULL_B), 'mid'),
             L(outline([(14, 36), (26, 12), (50, 4), (74, 12), (86, 36), (50, 30)]), 'band'),
             L(quad((16, 30), (50, 8), (84, 30)), 'line', 'f', False, False, 1.4),
             L(outline([(56, 36), (84, 40), (84, 72), (62, 88)]), 'shade', 'b', False)],
}

# Panacea Utopia: piel morena y pelo blanco como una capucha, liso y redondeado, que le cae hasta la barbilla con un
# mechón por delante del ojo; la nuca rosada en dos puntas
CHARS['panacea-utopia'] = {
    'body': 'normal', 'pal': pal('#f4f4f0', '#a8784e', iris='#1e1414', shade='#d8c8c4', deep='#b89a98'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 108), (4, 96), (0, 60), (2, 30), (14, 6), (36, -6), (64, -6), (86, 6), (98, 30), (100, 60), (96, 96), (88, 108), (84, 64), (16, 64)])),
              L(outline([(60, -4), (86, 8), (98, 40), (96, 96), (88, 104), (84, 50)]), 'shade', 'b', False),
              fringe([(10, 96), (8, 50), (18, 22), (44, 6), (62, 8), (40, 26), (28, 50), (24, 76), (18, 104, 1)]),
              fringe([(90, 96), (92, 50), (82, 24), (64, 10), (56, 18), (72, 36), (80, 60), (82, 104, 1)])],
    'side': [L(outline([(52, 66), (58, 52), (80, 48), (92, 32), (86, 8), (62, -6), (32, -6), (10, 10), (0, 40), (0, 80), (12, 104), (30, 104), (44, 90)])),
             L(outline([(0, 40), (30, 30), (54, 46), (44, 90), (14, 102)]), 'shade', 'b', False)],
    'back': [L(outline([(6, 104), (0, 60), (2, 30), (14, 6), (36, -6), (64, -6), (86, 6), (98, 30), (100, 60), (94, 104), (80, 96), (74, 106, 1), (66, 90), (34, 90),
                        (26, 106, 1), (20, 96)])),
             L(outline([(4, 46), (30, 26), (70, 26), (96, 46), (94, 100), (78, 92), (22, 92), (6, 100)]), 'shade', 'b', False)],
}

# Acme Rapture: pelo verde oscuro liso por encima de la cabeza que cae en mechones gruesos y planos, abiertos hacia fuera
# a los lados como tentáculos; una tira blanca en V por la nariz, ojos fieros y los dientes apretados
CHARS['acme-rapture'] = {
    'body': 'normal', 'pal': pal('#4a6a2a', '#d8a068', iris='#1e1414', tape='#f0f0f0', shade='#34501e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(4, 56), (-14, 80), (-6, 102), (4, 100), (6, 84), (14, 70)])), L(outline([(96, 56), (114, 80), (106, 102), (96, 100), (94, 84), (86, 70)])),
              L(outline([(14, 66), (6, 50), (8, 24), (26, 4), (50, -2), (74, 4), (92, 24), (94, 50), (86, 66), (80, 56), (20, 56)])),
              L(outline([(60, 2), (86, 14), (94, 46), (84, 62), (76, 36)]), 'shade', 'b', False),
              fringe([(12, 66), (14, 40), (28, 20), (50, 14), (72, 20), (86, 40), (88, 66), (78, 56), (66, 50), (50, 46), (34, 50), (22, 56)]),
              L([(24, 80), (50, 90), (76, 80)], 'tape', 'f', False, False, 3.2)],
    'side': [L(outline([(54, 56), (62, 44), (84, 44), (92, 26), (80, 6), (56, -4), (28, 0), (10, 14), (-10, 30), (-34, 44), (-36, 56), (-16, 50), (-28, 70), (-26, 82),
                        (-6, 66), (6, 74), (20, 84), (34, 70), (44, 62)])),
             L(outline([(-30, 50), (-6, 38), (20, 44), (24, 70), (0, 62)]), 'shade', 'b', False),
             L([(82, 82), (94, 90)], 'tape', 'f', False, False, 3.2)],
    'back': [L(outline([(4, 52), (-16, 80), (-8, 104), (4, 100), (8, 80)])), L(outline([(96, 52), (116, 80), (108, 104), (96, 100), (92, 80)])),
             L(outline([(12, 90), (6, 50), (8, 24), (26, 4), (50, -2), (74, 4), (92, 24), (94, 50), (88, 90), (50, 96)])),
             L(outline([(20, 60), (50, 54), (80, 60), (86, 90), (50, 96), (14, 90)]), 'shade', 'b', False)],
}

# Ultima Nextworld: un copete blanco esponjoso como un gorro de cocinero encima de una banda marrón oscura que le envuelve
# la cabeza, gafas de sol negras de visera y una melena blanca larga que le cae por detrás hasta la espalda
CHARS['ultima-nextworld'] = {
    'body': 'normal', 'pal': pal('#e8ece8', '#f0b878', iris='#1e1414', wrap='#3a2a24', wrap_d='#2a1e1a', shade='#b8c4c0'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(-12, 116), (-4, 96), (10, 80), (20, 100), (14, 120)])), L(outline([(112, 116), (104, 96), (90, 80), (80, 100), (86, 120)])),
              L(outline([(16, 60), (14, 36), (18, 24), (82, 24), (86, 36), (84, 60), (76, 52), (76, 40), (24, 40), (24, 52)]), 'wrap', 'f'),
              L(outline([(18, 28), (16, 10), (24, -8), (38, -12), (50, -8), (62, -12), (76, -8), (84, 10), (82, 28), (50, 32)]), 'mid', 'f'),
              L(outline([(62, -10), (76, -6), (84, 12), (80, 26), (66, 26)]), 'shade', 'f', False),
              strand([(38, 26), (38, -8)], 'shade', 'f', 1.0), strand([(62, 26), (62, -8)], 'shade', 'f', 1.0),
              L(outline([(12, 66), (88, 66), (84, 80), (60, 80), (50, 74), (40, 80), (16, 80)]), BLACK, 'f', False),
              L(outline([(18, 68), (40, 68), (30, 72)]), (90, 90, 96, 255), 'f', False)],
    'side': [L(outline([(52, 40), (40, 64), (20, 84), (-10, 106), (-30, 124, 1), (10, 120), (30, 100), (48, 76)])),
             L(outline([(12, 56), (10, 26), (60, 22), (84, 30), (86, 44), (60, 44), (52, 60), (26, 64)]), 'wrap'),
             L(outline([(12, 28), (12, 8), (24, -10), (50, -14), (76, -8), (88, 10), (86, 30), (50, 26)]), 'mid'),
             L(outline([(70, 68), (96, 66), (96, 78), (72, 80)]), BLACK, 'f', False), L([(70, 72), (48, 66)], BLACK, 'f', False, False, 2.4)],
    'back': [L(outline([(-12, 118), (-6, 92), (10, 76), (18, 60), (50, 56), (82, 60), (90, 76), (106, 92), (112, 118), (80, 112), (50, 120), (20, 112)])),
             L(outline([(50, 60), (82, 60), (106, 96), (112, 116), (60, 112)]), 'shade', 'b', False),
             L(outline([(14, 66), (12, 26), (88, 26), (86, 66), (50, 70)]), 'wrap'),
             strand([(16, 40), (84, 40)], 'wrap_d', 'f', 1.0), strand([(16, 52), (84, 52)], 'wrap_d', 'f', 1.0),
             L(outline([(18, 28), (16, 10), (24, -8), (38, -12), (50, -8), (62, -12), (76, -8), (84, 10), (82, 28), (50, 32)]), 'mid'),
             L(outline([(62, -10), (76, -6), (84, 12), (80, 26), (66, 26)]), 'shade', 'b', False)],
}

# Maxim Millennium: pelo granate ondulado con dos moños grandes a los lados de lo alto, como orejas, y flequillo de ondas;
# ojos morados, ojeras oscuras y cara seria
CHARS['maxim-millennium'] = {
    'body': 'normal', 'pal': pal('#9a3a4a', '#fce0c4', iris='#6a3a8a', shadow='#6a5a5a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(ell(4, 16, 16, 18)), L(ell(96, 16, 16, 18)),
              L(outline([(10, 92), (4, 60), (6, 30), (18, 8), (50, -2), (82, 8), (94, 30), (96, 60), (90, 92), (84, 66), (16, 66)])),
              L(outline([(60, 2), (84, 12), (96, 40), (90, 86), (80, 50)]), 'shade', 'b', False),
              fringe([(8, 80), (10, 46), (24, 22), (48, 12), (72, 20), (88, 42), (92, 80), (84, 70), (80, 56), (70, 60, 1), (66, 46), (56, 54), (50, 42), (40, 58, 1), (34, 44),
                      (24, 60), (18, 76, 1)]),
              L(ell(64, 86, 6, 2.4), 'shadow', 'f', False)],
    'side': [L(ell(30, 14, 18, 18)),
             L(outline([(54, 66), (58, 52), (82, 52), (94, 36), (88, 12), (66, 0), (36, 0), (14, 14), (4, 42), (6, 76), (18, 96), (34, 96), (46, 84)])),
             L(outline([(4, 42), (26, 46), (34, 92), (12, 92)]), 'shade', 'b', False), L(ell(30, 14, 12, 12) + [ell(30, 14, 12, 12)[0]], 'deep', 'b', False, False, 1.0),
             fringe([(64, 4), (88, 16), (96, 42), (94, 66, 1), (86, 52), (78, 40)])],
    'back': [L(ell(4, 18, 16, 18)), L(ell(96, 18, 16, 18)),
             L(outline([(8, 90), (4, 60), (6, 30), (18, 8), (50, -2), (82, 8), (94, 30), (96, 60), (92, 90), (50, 96)])),
             L(outline([(56, 2), (84, 12), (96, 40), (92, 88), (64, 94)]), 'shade', 'b', False)],
}

# Infinity Beyond: pelo azul marino corto con una cresta alta en punta en el centro y dos piezas blancas curvas como
# cuernos que salen a los lados de la cabeza; ojos turquesa y sonrisa de lado
CHARS['infinity-beyond'] = {
    'body': 'normal', 'pal': pal('#1e2a44', '#fce0c0', iris='#2a9aa8', horn='#ece4ea', horn_d='#b8a8b4'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 76), (12, 40), (24, 14), (36, 6), (44, -12), (50, -30, 1), (56, -12), (64, 6), (76, 14), (88, 40), (84, 76), (80, 56), (20, 56)])),
              L(outline([(20, 40), (2, 10), (-6, -6, 1), (10, 16), (24, 30)]), 'horn', 'f', ln=True),
              L(outline([(80, 40), (98, 10), (106, -6, 1), (90, 16), (76, 30)]), 'horn', 'f', ln=True),
              fringe([(18, 66), (20, 40), (34, 20), (50, 6), (66, 20), (80, 40), (82, 66), (72, 48), (60, 40), (52, 58, 1), (46, 40), (34, 46), (26, 60, 1)]),
              L(outline([(50, -24), (56, -10), (62, 10), (54, 20)]), 'shade', 'f', False)],
    'side': [L(outline([(56, 58), (62, 46), (82, 46), (92, 30), (84, 12), (96, -6), (76, -4), (60, -20), (36, -26, 1), (40, -12), (20, -2), (6, 20), (4, 52), (16, 76),
                        (34, 78), (46, 66)])),
             L(outline([(60, 20), (52, 0), (60, -16, 1), (66, 4), (70, 22)]), 'horn', 'f', ln=True),
             L(outline([(6, 30), (24, 36), (26, 66), (8, 60)]), 'shade', 'b', False),
             L([(40, 70), (20, 90), (4, 110)], 'horn_d', 'f', False, False, 2.4)],
    'back': [L(outline([(14, 80), (12, 40), (24, 14), (40, 4), (50, -24, 1), (60, 4), (76, 14), (88, 40), (86, 80), (50, 88)])),
             L(outline([(20, 40), (0, 14), (-8, -2, 1), (8, 20), (24, 32)]), 'horn', 'f', ln=True),
             L(outline([(80, 40), (100, 14), (108, -2, 1), (92, 20), (76, 32)]), 'horn', 'f', ln=True),
             L(outline([(56, 6), (80, 16), (88, 46), (84, 76), (62, 84)]), 'shade', 'b', False)],
}

# Apex Paradiso (portero suplente): melena morada larga y lisa con raya en medio, que le enmarca la cara alargada y cae
# por los lados y la espalda; ojos rojos con ojeras
CHARS['apex-paradiso'] = {
    'body': 'delgado', 'pal': pal('#3a2a7a', '#ecdcb4', iris='#c81e1e', shadow='#a08a7a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 102, 'face_front': LONG_FACE, 'hairline': False},
    'front': [L(outline([(6, 120), (0, 80), (2, 40), (14, 10), (36, -4), (64, -4), (86, 10), (98, 40), (100, 80), (94, 120), (82, 116), (82, 64), (18, 64), (18, 116)])),
              L(outline([(60, -2), (86, 12), (98, 44), (96, 116), (84, 112), (82, 50)]), 'shade', 'b', False),
              fringe([(14, 100), (12, 50), (22, 20), (48, 6), (50, 14), (36, 30), (26, 60), (22, 104, 1)]),
              fringe([(86, 100), (88, 50), (78, 20), (52, 6), (50, 14), (64, 30), (74, 60), (78, 104, 1)]),
              L(ell(36, 84, 6, 2.2), 'shadow', 'f', False), L(ell(64, 84, 6, 2.2), 'shadow', 'f', False)],
    'side': [L(outline([(56, 60), (62, 46), (82, 46), (94, 30), (88, 8), (64, -6), (34, -4), (12, 10), (0, 40), (-6, 80), (-20, 110), (-34, 124, 1), (4, 118), (24, 100),
                        (40, 84)])),
             L(outline([(0, 40), (28, 44), (36, 88), (2, 112)]), 'shade', 'b', False),
             fringe([(64, -2), (90, 12), (94, 40), (92, 80, 1), (84, 52), (76, 34)])],
    'back': [L(outline([(0, 120), (0, 80), (2, 40), (14, 10), (36, -4), (64, -4), (86, 10), (98, 40), (100, 80), (100, 120), (50, 126)])),
             L(outline([(56, -2), (86, 12), (98, 44), (100, 120), (64, 122)]), 'shade', 'b', False), strand([(50, 0), (50, 60)], 'deep', 'b', 1.0)],
}

# Pearl Gates: pelo azul marino con raya en medio que cae liso y se abre en puntas a los lados a la altura de la mandíbula;
# una banda gris le tapa la nariz y la boca por debajo de los ojos naranjas, y sonríe
CHARS['pearl-gates'] = {
    'body': 'normal', 'pal': pal('#1e2a48', '#f6d4a8', iris='#e0781e', band='#a0a0a8', band_d='#7a7a84'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 102, 'hairline': False},
    'front': [L(outline([(16, 96), (10, 82), (-12, 84, 1), (4, 70), (-10, 62, 1), (6, 54), (4, 30), (16, 8), (36, -4), (50, 0), (64, -4), (84, 8), (96, 30), (94, 54),
                         (110, 62, 1), (96, 70), (112, 84, 1), (90, 82), (84, 96), (82, 60), (18, 60)])),
              L(outline([(60, -2), (84, 10), (96, 40), (92, 80), (80, 50)]), 'shade', 'b', False),
              fringe([(14, 80), (12, 44), (24, 18), (46, 4), (48, 18), (38, 34), (30, 60), (26, 90, 1), (20, 70)]),
              fringe([(86, 80), (88, 44), (76, 18), (54, 4), (52, 18), (62, 34), (70, 60), (74, 90, 1), (80, 70)]),
              L(outline([(18, 80), (50, 82), (82, 80), (80, 92), (50, 94), (20, 92)]), 'band', 'f', ln=True)],
    'side': [L(outline([(54, 60), (60, 48), (82, 48), (94, 32), (88, 10), (64, -4), (34, -2), (12, 12), (2, 36), (-14, 50, 1), (2, 56), (-12, 74, 1), (6, 74), (0, 94, 1),
                        (20, 86), (34, 96, 1), (42, 78)])),
             L(outline([(2, 40), (26, 44), (30, 80), (8, 76)]), 'shade', 'b', False),
             L(outline([(54, 78), (96, 80), (96, 92), (56, 90)]), 'band', 'f', ln=True),
             fringe([(64, 0), (90, 14), (96, 40), (94, 66, 1), (86, 50), (78, 38)])],
    'back': [L(outline([(10, 86), (-12, 86, 1), (2, 70), (-12, 58, 1), (4, 50), (4, 30), (16, 8), (36, -4), (50, 0), (64, -4), (84, 8), (96, 30), (96, 50), (112, 58, 1),
                        (98, 70), (112, 86, 1), (90, 86), (74, 96, 1), (62, 86), (50, 96, 1), (38, 86), (26, 96, 1)])),
             L(outline([(56, -2), (84, 10), (96, 40), (94, 84), (62, 88)]), 'shade', 'b', False),
             L([(12, 86), (50, 90), (88, 86)], 'band_d', 'f', False, False, 2.0)],
}

# Perpetuo Xanadu: pelo verde oliva en forma de llama: un solo pico alto en punta por encima de la cabeza, con un
# flequillo de mechones; los ojos cerrados y la boca torcida
CHARS['perpetuo-xanadu'] = {
    'body': 'normal', 'pal': pal('#6a7a3a', '#f6c8a0', iris='#1e1414', shade='#4e5a2a'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 70), (8, 46), (10, 24), (26, 4), (34, -12), (46, -34), (54, -44, 1), (58, -20), (70, -2), (86, 16), (92, 40), (86, 70), (80, 56), (20, 56)])),
              L(outline([(56, -30), (70, -2), (88, 20), (90, 46), (82, 66), (76, 30), (60, 10)]), 'shade', 'b', False),
              fringe([(14, 62), (16, 38), (30, 20), (52, 14), (72, 20), (86, 38), (86, 62), (78, 48), (70, 56, 1), (64, 40), (54, 52, 1), (48, 38), (38, 52, 1), (32, 40),
                      (22, 54, 1)])],
    'side': [L(outline([(56, 58), (62, 46), (82, 46), (90, 28), (82, 8), (64, -10), (40, -30), (14, -48, 1), (20, -20), (6, 0), (2, 30), (6, 58), (20, 76), (36, 76),
                        (46, 66)])),
             L(outline([(14, -40), (20, -16), (8, 4), (4, 40), (20, 60), (24, 10)]), 'shade', 'b', False),
             fringe([(66, 2), (88, 16), (92, 40), (88, 56, 1), (80, 42), (72, 32)])],
    'back': [L(outline([(16, 80), (8, 50), (10, 24), (26, 4), (36, -14), (50, -40, 1), (64, -14), (74, 4), (90, 24), (92, 50), (84, 80), (64, 86, 1), (56, 82), (50, 90, 1),
                        (44, 82), (36, 86, 1)])),
             L(outline([(52, -34), (70, -2), (90, 26), (88, 76), (62, 84)]), 'shade', 'b', False),
             strand([(50, -30), (40, 20), (40, 70)], 'deep', 'b', 1.0), strand([(50, -30), (60, 20), (60, 70)], 'deep', 'b', 1.0)],
}

# Sempiterno Bliss: pelo granate oscuro con lo alto recogido como un pañuelo atado y una melena lisa que le cae por los
# lados y por detrás hasta la espalda; un antifaz negro en forma de estrella de cuatro puntas en los ojos verdes
CHARS['sempiterno-bliss'] = {
    'body': 'normal', 'pal': pal('#8a1a2a', '#f0b878', iris='#8aa02a', shade='#6a1220'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(8, 116), (-4, 108), (2, 70), (6, 36), (18, 10), (40, 0), (60, 0), (82, 10), (94, 36), (98, 70), (104, 108), (92, 116), (84, 66), (16, 66)])),
              L(outline([(60, 2), (84, 12), (96, 46), (100, 106), (86, 110), (82, 50)]), 'shade', 'b', False),
              fringe([(10, 74), (8, 46), (20, 18), (50, 6), (80, 18), (92, 46), (90, 74), (84, 62), (80, 48), (68, 44), (60, 56, 1), (54, 40), (46, 40), (40, 56, 1), (32, 44),
                      (20, 48), (16, 62)]),
              L(outline([(22, 74), (40, 68), (50, 54, 1), (60, 68), (78, 74), (60, 80), (50, 96, 1), (40, 80)]), BLACK, 'f', False),
              L(outline([(28, 74), (42, 72), (42, 80), (30, 79)]), WHITE, 'f', False), L(outline([(72, 74), (58, 72), (58, 80), (70, 79)]), WHITE, 'f', False),
              L(ell(38, 76, 2.6, 3), 'iris', 'f', False), L(ell(62, 76, 2.6, 3), 'iris', 'f', False)],
    'side': [L(outline([(54, 62), (58, 50), (80, 46), (94, 32), (86, 8), (60, -4), (30, 0), (12, 14), (2, 36), (-10, 52), (-30, 80), (-34, 104, 1), (-12, 94), (-4, 112, 1),
                        (14, 92), (30, 82), (44, 74)])),
             L(outline([(2, 30), (10, 18), (60, 14), (64, 24), (10, 34)]), 'shade', 'b', False),
             L(outline([(-10, 50), (18, 50), (24, 76), (-14, 96)]), 'shade', 'b', False),
             L(outline([(74, 74), (86, 68), (94, 70), (92, 78), (84, 82)]), BLACK, 'f', False)],
    'back': [L(outline([(-8, 116), (-4, 80), (6, 40), (18, 10), (40, 0), (60, 0), (82, 10), (94, 40), (104, 80), (108, 116), (50, 122)])),
             L(outline([(56, 2), (84, 12), (96, 46), (106, 114), (66, 118)]), 'shade', 'b', False),
             L(outline([(10, 44), (50, 36), (90, 44), (90, 54), (50, 48), (10, 54)]), 'shade', 'f', ln=True),
             L(outline([(40, 46), (60, 46), (60, 58), (40, 58)]), 'shade', 'f', ln=True)],
}

# Myriad Arcadia: piel morena, pelo celeste grisáceo en un tupé de surcos peinado hacia atrás, las sienes y la nuca grises;
# gafas redondas finas, cejas gruesas celestes y gesto serio
CHARS['myriad-arcadia'] = {
    'body': 'normal', 'pal': pal('#a8d8e8', '#b07a50', iris='#1e1414', side='#8aa0a8', shade='#7ab0c4'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'hairline': False, 'glasses': (200, 180, 160, 255), 'big_ears': 2},
    'front': [L(outline([(16, 60), (14, 40), (86, 40), (84, 60), (78, 52), (22, 52)]), 'side', 'f'),
              L(outline([(10, 46), (6, 26), (14, 6), (30, -6), (50, -10), (70, -6), (86, 6), (94, 26), (90, 46), (70, 40), (50, 42), (30, 40)]), 'mid', 'f'),
              L(outline([(60, -6), (86, 6), (94, 26), (90, 44), (74, 38)]), 'shade', 'f', False),
              strand([(30, 40), (34, 10), (46, -6)], 'shade', 'f', 1.0), strand([(50, 42), (50, 8), (54, -8)], 'shade', 'f', 1.0),
              strand([(70, 40), (66, 10), (60, -4)], 'shade', 'f', 1.0),
              L([(26, 66), (42, 64)], 'mid', 'f', False, False, 3.2), L([(74, 66), (58, 64)], 'mid', 'f', False, False, 3.2)],
    'side': [L(outline([(12, 70), (10, 36), (30, 20), (60, 24), (60, 40), (52, 56), (48, 80), (30, 90), (14, 84)]), 'side'),
             L(outline([(4, 40), (2, 18), (16, -2), (44, -10), (74, -4), (92, 10), (94, 30), (70, 26), (40, 30), (14, 40)])),
             strand([(10, 14), (90, 18)], 'shade', 'b', 1.0), strand([(6, 28), (80, 26)], 'shade', 'b', 1.0)],
    'back': [L(blob(SKULL_B), 'side'),
             L(outline([(8, 44), (4, 24), (14, 4), (32, -8), (50, -10), (68, -8), (86, 4), (96, 24), (92, 44), (70, 34), (50, 52, 1), (30, 34)])),
             strand([(50, -8), (50, 48)], 'shade', 'b', 1.0), strand([(30, -4), (40, 40)], 'shade', 'b', 1.0), strand([(70, -4), (60, 40)], 'shade', 'b', 1.0)],
}
