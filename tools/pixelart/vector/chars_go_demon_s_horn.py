"""Cuerno Demoníaco (go-demon-s-horn): sus modelos 3D de Inazuma Eleven GO como referencia (busto de frente, perfil y espalda).
Es un equipo combinado de Garras del Sur y Colmillos del Norte: aquí están todos sus jugadores (los dos equipos los reutilizan)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from chars_go_raimon import fringe
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)
DARK = (24, 20, 24, 255)

# Xavier Shotwell (portero): melena rubia con mechas rosas y blancas peinada toda hacia un lado, que le tapa media cabeza y
# cae larga por ese lado hasta el pecho; el otro lado de la cabeza rapado, con tres lunares negros junto al ojo; sonrisa
CHARS['xavier-shotwell'] = {
    'body': 'delgado', 'pal': pal('#f0c63c', '#fce8c4', iris='#a8541e', pink='#e8a8b4', pink_d='#c8848e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(70, 30), (74, 12), (62, 2), (40, 0), (20, 10), (8, 34), (4, 70), (2, 110), (-4, 128, 1), (10, 116), (14, 130, 1), (18, 104), (22, 70),
                         (30, 44), (50, 30)])),
              L(outline([(22, 6), (54, 0), (68, 8), (40, 18), (20, 36), (10, 70), (8, 40)]), 'pink', 'b', False),
              L(outline([(14, 60), (12, 100), (4, 120), (8, 90)]), 'pink', 'b', False),
              fringe([(74, 14), (60, 26), (40, 34), (24, 48), (18, 70), (16, 50), (24, 28), (42, 14), (62, 6)]),
              L(outline([(30, 30), (54, 16), (70, 14), (50, 26)]), 'pink', 'f', False),
              L(ell(74, 62, 1.8, 1.8), OUTC, 'f', False), L(ell(76, 84, 1.8, 1.8), OUTC, 'f', False), L(ell(72, 92, 1.8, 1.8), OUTC, 'f', False)],
    'side': [L(outline([(70, 18), (88, 26), (92, 40), (80, 30), (62, 32), (50, 44), (40, 70), (28, 110), (14, 132, 1), (6, 100), (2, 60), (8, 24), (30, 4), (54, 2)])),
             L(outline([(40, 6), (58, 4), (36, 40), (22, 90), (16, 120), (14, 80), (24, 30)]), 'pink', 'b', False),
             L(outline([(64, 10), (84, 22), (70, 22), (54, 30), (40, 60), (34, 96), (30, 70), (40, 36)]), 'pink_d', 'b', False)],
    'back': [L(outline([(16, 64), (12, 34), (24, 10), (50, 0), (76, 10), (84, 30), (76, 60), (64, 90), (60, 130, 1), (44, 120), (36, 132, 1), (34, 94), (22, 76)])),
             L(outline([(40, 2), (56, 2), (54, 70), (52, 126), (46, 120), (46, 60)]), 'pink', 'b', False),
             L(outline([(62, 6), (72, 12), (64, 70), (60, 100)]), 'pink_d', 'b', False)],
}

# Crimson Wiseman: una melena gris perla enorme y abombada como una peluca de juez, con rizos en espiral sobre la frente y
# las puntas abiertas hasta los hombros; ojos rojos de mirada fija
CHARS['crimson-wiseman'] = {
    'body': 'corpulento', 'pal': pal('#d8dcd2', '#fcdcc0', iris='#e02a2a', shade='#a8908a', deep='#8a7470'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 66), (-6, 74), (-26, 92, 1), (-8, 84), (-2, 66), (4, 36), (14, 8), (36, -8), (64, -8), (86, 8), (96, 36), (102, 66), (108, 84),
                         (126, 92, 1), (106, 74), (84, 66), (80, 58), (20, 58)])),
              L(outline([(60, -4), (86, 10), (100, 50), (108, 80), (88, 64), (80, 30)]), 'shade', 'b', False),
              fringe([(14, 64), (12, 40), (24, 18), (50, 10), (76, 18), (88, 40), (86, 64), (76, 48), (64, 50), (56, 40), (50, 54), (44, 40), (36, 50), (24, 48)]),
              L(ell(30, 36, 7, 7) + [ell(30, 36, 7, 7)[0]], 'shade', 'f', False, False, 2.2), L(ell(70, 36, 7, 7) + [ell(70, 36, 7, 7)[0]], 'shade', 'f', False, False, 2.2),
              L(ell(30, 36, 3, 3) + [ell(30, 36, 3, 3)[0]], 'shade', 'f', False, False, 1.6), L(ell(70, 36, 3, 3) + [ell(70, 36, 3, 3)[0]], 'shade', 'f', False, False, 1.6)],
    'side': [L(outline([(56, 60), (64, 44), (86, 42), (94, 26), (86, 8), (62, -8), (34, -8), (12, 4), (0, 30), (-12, 56), (-34, 80, 1), (-10, 76), (-6, 92), (8, 86),
                        (20, 100), (34, 84), (44, 70)])),
             L(outline([(-4, 50), (22, 50), (34, 82), (8, 84)]), 'shade', 'b', False),
             L(outline([(20, 0), (40, -4), (34, 10)]), 'shade', 'b', False),
             L(ell(80, 30, 6, 6) + [ell(80, 30, 6, 6)[0]], 'shade', 'f', False, False, 2.2)],
    'back': [L(outline([(-6, 80), (-28, 90, 1), (-8, 70), (2, 40), (14, 8), (36, -8), (64, -8), (86, 8), (98, 40), (108, 70), (128, 90, 1), (106, 80), (100, 96),
                        (82, 92), (66, 104), (50, 96), (34, 104), (18, 92), (0, 96)])),
             L(outline([(4, 50), (50, 40), (96, 50), (104, 84), (50, 92), (-4, 84)]), 'shade', 'b', False),
             L(outline([(40, 4), (50, -2), (60, 4), (50, 10)]), 'deep', 'b', False),
             strand([(30, 50), (28, 84)], 'deep', 'b', 1.0), strand([(50, 50), (50, 88)], 'deep', 'b', 1.0), strand([(70, 50), (72, 84)], 'deep', 'b', 1.0)],
}

# Linder Loper: pelo en forma de capucha partido en dos colores (blanco a un lado, verde azulado al otro) que le enmarca
# la cara hasta la barbilla, y una trenza larga de los dos colores que le cae por delante; cara alargada con ojeras oscuras
CHARS['linder-loper'] = {
    'body': 'delgado', 'pal': pal('#f2efe4', '#e0c8a8', iris='#1e1a1a', shade='#c8aaa4', teal='#3a7a82', teal_d='#2a5a62', ring='#3a3236'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(50, -4), (18, 6), (4, 40), (2, 90), (8, 112), (20, 108), (22, 70), (26, 48), (40, 36), (50, 30)])),
              L(outline([(50, -4), (82, 6), (96, 40), (98, 90), (92, 112), (80, 108), (78, 70), (74, 48), (60, 36), (50, 30)]), 'teal'),
              L(outline([(66, 2), (88, 20), (96, 60), (92, 100), (84, 80), (80, 40)]), 'teal_d', 'b', False),
              L(ell(38, 76, 7, 5), 'ring', 'f', False), L(ell(62, 76, 7, 5), 'ring', 'f', False),
              L(outline([(32, 74), (40, 70), (44, 76), (36, 78)]), WHITE, 'f', False), L(outline([(68, 74), (60, 70), (56, 76), (64, 78)]), WHITE, 'f', False),
              L(ell(39, 75, 1.4, 1.6), OUTC, 'f', False), L(ell(61, 75, 1.4, 1.6), OUTC, 'f', False),
              L([(50, 40), (50, 88)], 'skin_d', 'f', False, False, 1.4)],
    'side': [L(outline([(70, 6), (86, 24), (90, 50), (82, 52), (74, 40), (60, 44), (56, 70), (48, 100), (30, 112), (10, 104), (2, 70), (4, 34), (20, 8), (46, -2)])),
             L(outline([(4, 40), (40, 30), (52, 70), (44, 100), (20, 108), (6, 80)]), 'shade', 'b', False),
             L(ell(84, 76, 4, 5), 'ring', 'f', False), L(ell(85, 76, 1.4, 1.8), OUTC, 'f', False)],
    'back': [L(outline([(50, -4), (82, 6), (96, 40), (98, 90), (84, 108), (50, 100)])),
             L(outline([(50, -4), (18, 6), (4, 40), (2, 90), (16, 108), (50, 100)]), 'teal'),
             L(outline([(60, 4), (86, 20), (96, 60), (92, 96), (66, 100)]), 'shade', 'b', False),
             L(outline([(14, 30), (6, 60), (8, 96), (22, 100), (24, 40)]), 'teal_d', 'b', False)],
}

# Locke Saflowe: melena azul marino oscuro larguísima y lisa que cae por los dos lados hasta la cintura, con un flequillo
# grande azul que le tapa un ojo; un pendiente y media sonrisa
CHARS['locke-saflowe'] = {
    'body': 'chica', 'pal': pal('#24264a', '#fcdcc0', iris='#b84868', light='#4a5ab0'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 70), (8, 36), (20, 10), (50, 0), (80, 10), (92, 36), (94, 80), (104, 140), (112, 170, 1), (84, 150), (80, 100), (82, 70), (76, 56),
                         (24, 56), (18, 100), (16, 150), (-12, 170, 1), (-4, 140), (6, 100)])),
              L(outline([(60, 4), (84, 16), (92, 50), (96, 120), (90, 150), (84, 90)]), 'shade', 'b', False),
              fringe([(12, 66), (12, 38), (26, 16), (52, 8), (76, 16), (88, 36), (86, 56), (70, 48), (60, 44), (52, 60), (48, 88, 1), (36, 76), (24, 62)], 'light'),
              L(outline([(24, 20), (50, 12), (56, 40), (44, 80), (30, 60)]), 'mid', 'f', False)],
    'side': [L(outline([(56, 60), (60, 48), (82, 46), (92, 32), (86, 12), (64, 0), (36, 0), (14, 12), (4, 36), (0, 80), (-6, 140), (-14, 172, 1), (10, 150), (20, 110),
                        (30, 80), (44, 70)])),
             L(outline([(4, 40), (24, 46), (14, 120), (-4, 150), (2, 90)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 40), (92, 60, 1), (84, 46), (74, 36)], 'light'),
             L(ell(48, 84, 2.4, 2.4), (200, 200, 210, 255), 'f', ln=True)],
    'back': [L(outline([(14, 70), (8, 36), (20, 10), (50, 0), (80, 10), (92, 36), (94, 80), (104, 140), (110, 172, 1), (80, 160), (50, 170, 1), (20, 160), (-10, 172, 1),
                        (-4, 140), (6, 80)])),
             L(outline([(56, 4), (84, 16), (94, 60), (100, 140), (80, 156), (70, 80)]), 'shade', 'b', False),
             strand([(30, 40), (24, 100), (20, 150)], 'deep', 'b', 1.0), strand([(50, 30), (50, 160)], 'deep', 'b', 1.0), strand([(70, 40), (76, 100), (80, 150)], 'deep', 'b', 1.0)],
}

# Linden Haregrove: melena castaña lisa y larga hasta los hombros, raya en medio y una franja gris blanca en V que baja de
# lo alto a la frente; cara alargada de ojos cerrados y nariz larga, con la boca torcida hacia abajo
CHARS['linden-haregrove'] = {
    'body': 'delgado', 'pal': pal('#6a4026', '#fcd8b0', iris='#1e1414', band='#dcdcd4', band_d='#a8a8a0'),
    'face': {'eyes': 'closed', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 102, 'hairline': False},
    'front': [L(outline([(16, 60), (14, 30), (22, 6), (50, 0), (78, 6), (86, 30), (84, 60), (88, 120), (94, 136, 1), (76, 128), (76, 70), (74, 50), (26, 50), (24, 70),
                         (24, 128), (6, 136, 1), (12, 120)])),
              L(outline([(60, 2), (80, 12), (86, 60), (88, 124), (82, 100), (78, 40)]), 'shade', 'b', False),
              L(outline([(40, 0), (60, 0), (58, 26), (66, 30), (64, 40), (50, 62, 1), (36, 40), (34, 30), (42, 26)]), 'band', 'f', ln=True),
              L([(50, 70), (46, 92), (52, 92)], 'skin_d', 'f', False, False, 1.4)],
    'side': [L(outline([(70, 6), (84, 18), (88, 36), (76, 36), (60, 40), (52, 70), (40, 110), (12, 136, 1), (6, 100), (6, 50), (14, 16), (40, 0)])),
             L(outline([(64, 4), (82, 14), (88, 30), (80, 28), (72, 14)]), 'band', 'b', ln=True),
             L(outline([(8, 40), (30, 40), (34, 90), (16, 120), (10, 90)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 60), (14, 30), (22, 6), (50, 0), (78, 6), (86, 30), (86, 60), (88, 130), (70, 140), (50, 136), (30, 140), (12, 130)])),
             L(outline([(42, 2), (58, 2), (60, 60), (66, 136), (34, 136), (40, 60)]), 'band', 'b', False),
             L(outline([(50, 60), (64, 136), (52, 136)]), 'band_d', 'b', False)],
}

# Cirrus Whisp: el pelo blanco como una capucha enorme en forma de campana que le rodea la cara hasta los hombros; cejas
# blancas gruesas, ojos verdes y sonrisa
CHARS['cirrus-whisp'] = {
    'body': 'bajito', 'pal': pal('#f2f0e8', '#fcdcc0', iris='#3aa078', shade='#c8aca8', deep='#a8908a', brow='#f4f4f4'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(50, -10), (16, 4), (2, 40), (-6, 90), (-10, 116), (14, 112), (22, 96), (22, 60), (36, 44), (50, 40), (64, 44), (78, 60), (78, 96), (86, 112),
                         (110, 116), (106, 90), (98, 40), (84, 4)])),
              L(outline([(66, -4), (90, 16), (100, 70), (106, 110), (86, 106), (84, 60)]), 'shade', 'b', False),
              L(outline([(-6, 96), (10, 104), (18, 110), (-8, 114)]), 'shade', 'b', False),
              L(outline([(26, 64), (40, 60), (44, 64), (28, 68)]), 'brow', 'f', ln=True), L(outline([(74, 64), (60, 60), (56, 64), (72, 68)]), 'brow', 'f', ln=True)],
    'side': [L(outline([(60, 50), (76, 40), (88, 50), (90, 30), (78, 4), (50, -10), (20, -2), (0, 30), (-6, 80), (-4, 110), (20, 116), (40, 112), (50, 90), (54, 70)])),
             L(outline([(-4, 50), (30, 46), (48, 100), (30, 114), (2, 108)]), 'shade', 'b', False),
             L(outline([(80, 60), (90, 62), (90, 66), (80, 64)]), 'brow', 'f', ln=True)],
    'back': [L(outline([(50, -10), (16, 4), (2, 40), (-8, 90), (-12, 116), (20, 118), (50, 112), (80, 118), (112, 116), (108, 90), (98, 40), (84, 4)])),
             L(outline([(4, 60), (50, 50), (96, 60), (108, 112), (50, 108), (-8, 112)]), 'shade', 'b', False),
             strand([(30, 70), (24, 110)], 'deep', 'b', 1.0), strand([(50, 64), (50, 108)], 'deep', 'b', 1.0), strand([(70, 70), (76, 110)], 'deep', 'b', 1.0)],
}

# Sandy Dryhill: piel morena y la cabeza rapada, con el pelo rubio pálido muy corto arriba (en pico sobre la frente), cejas
# doradas grandes como hojas hacia arriba y una coletilla vendada en la nuca
CHARS['sandy-dryhill'] = {
    'body': 'normal', 'pal': pal('#f6eeb8', '#b07a4a', iris='#1e1414', shade='#a88a6a', leaf='#b89a3a', wrap='#d8b8a0'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(blob([(16, 64), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 64)]), 'skin'),
              L(outline([(16, 46), (16, 26), (28, 10), (50, 4), (72, 10), (84, 26), (84, 46), (72, 40), (64, 50), (50, 40), (36, 50), (28, 40)]), 'mid', 'f', ln=True),
              L(outline([(4, 46), (22, 56), (38, 66), (36, 70), (20, 62)]), 'leaf', 'f', ln=True), L(outline([(96, 46), (78, 56), (62, 66), (64, 70), (80, 62)]), 'leaf', 'f', ln=True)],
    'side': [L(outline([(36, 112), (14, 104), (10, 60), (12, 20), (40, 2), (72, 6), (90, 28), (96, 64), (90, 100), (70, 116)]), 'skin'),
             L(outline([(12, 44), (12, 20), (40, 2), (70, 4), (86, 20), (80, 30), (60, 26), (40, 38), (20, 50)]), 'mid', 'f', ln=True),
             L(outline([(76, 48), (90, 52), (100, 44), (94, 56), (80, 60)]), 'leaf', 'f', ln=True),
             L(outline([(16, 84), (8, 104), (4, 122), (10, 122), (16, 104), (22, 88)]), 'wrap', 'b', ln=True)],
    'back': [L(blob([(16, 70), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 70), (66, 86), (34, 86)]), 'skin'),
             L(outline([(14, 44), (16, 22), (30, 8), (50, 4), (70, 8), (84, 22), (86, 44), (70, 40), (50, 46), (30, 40)]), 'mid', 'b', ln=True),
             L(outline([(46, 84), (54, 84), (56, 120), (44, 120)]), 'wrap', 'f', ln=True),
             strand([(46, 96), (54, 98)], 'shade', 'f', 1.0), strand([(46, 108), (54, 110)], 'shade', 'f', 1.0)],
}

# Romeo Fitzroy: melena rubia verdosa de rizos en espiral, abombada a los lados y con un tirabuzón grueso horizontal hacia
# atrás; ojos violetas y sonrisa de pillo
CHARS['romeo-fitzroy'] = {
    'body': 'normal', 'pal': pal('#b0a456', '#fcdcc0', iris='#6a3ab8', shade='#8a7a3a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 100), (0, 96), (-6, 76), (2, 56), (0, 34), (14, 10), (40, -4), (66, -2), (88, 12), (100, 34), (98, 56), (106, 76), (100, 96), (86, 100),
                         (80, 64), (20, 64)])),
              L(outline([(62, 0), (88, 14), (100, 50), (100, 92), (86, 80), (80, 40)]), 'shade', 'b', False),
              fringe([(12, 66), (12, 40), (24, 18), (48, 8), (74, 16), (88, 38), (90, 66), (80, 56), (72, 46), (60, 50), (54, 40), (40, 48), (30, 46), (20, 60)]),
              L(ell(30, 32, 6, 6) + [ell(30, 32, 6, 6)[0]], 'shade', 'f', False, False, 1.8), L(ell(66, 28, 5, 5) + [ell(66, 28, 5, 5)[0]], 'shade', 'f', False, False, 1.8),
              L(ell(4, 86, 6, 7) + [ell(4, 86, 6, 7)[0]], 'shade', 'f', False, False, 1.8), L(ell(96, 86, 6, 7) + [ell(96, 86, 6, 7)[0]], 'shade', 'f', False, False, 1.8)],
    'side': [L(outline([(56, 62), (62, 48), (84, 48), (94, 32), (86, 10), (62, -4), (34, -2), (12, 12), (2, 40), (0, 70), (8, 92), (26, 98), (42, 88), (48, 74)])),
             L(outline([(20, 56), (-6, 54), (-30, 58), (-34, 70), (-28, 80), (-4, 76), (20, 74)]), 'mid', 'b', ln=True),
             L(outline([(4, 34), (26, 40), (30, 86), (8, 84)]), 'shade', 'b', False),
             L(ell(30, 70, 7, 8) + [ell(30, 70, 7, 8)[0]], 'shade', 'f', False, False, 1.8),
             fringe([(64, 0), (88, 14), (96, 38), (92, 58, 1), (84, 44), (74, 34)])],
    'back': [L(outline([(14, 100), (-2, 94), (-6, 70), (2, 40), (14, 10), (40, -4), (66, -2), (88, 12), (100, 40), (106, 70), (102, 94), (86, 100), (70, 92), (50, 98),
                        (30, 92)])),
             L(outline([(56, 0), (88, 14), (100, 50), (102, 92), (70, 92), (70, 40)]), 'shade', 'b', False),
             strand([(50, 4), (50, 90)], 'deep', 'b', 1.2),
             L(ell(10, 84, 7, 8) + [ell(10, 84, 7, 8)[0]], 'shade', 'b', False, False, 1.8), L(ell(90, 84, 7, 8) + [ell(90, 84, 7, 8)[0]], 'shade', 'b', False, False, 1.8)],
}

# Dryden Zephyr: pelo azul violeta de pinchos peinados hacia arriba y hacia un lado, con un mechón largo que le cae junto a la
# cara por el otro; cejas finas y ojos grises serios
CHARS['dryden-zephyr'] = {
    'body': 'normal', 'pal': pal('#4a3e9a', '#fcdcc0', iris='#5a5a6a', light='#7a70c8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 66), (10, 40), (12, 14), (24, -4), (30, 6), (40, -20, 1), (52, 0), (70, -10, 1), (74, 6), (96, 4, 1), (88, 20), (106, 30, 1), (92, 40),
                         (104, 54, 1), (90, 60), (94, 74, 1), (84, 70), (80, 54), (20, 54)])),
              L(outline([(58, 0), (84, 12), (94, 40), (88, 64), (78, 40)]), 'shade', 'b', False),
              fringe([(14, 60), (16, 36), (30, 18), (52, 8), (72, 14), (86, 30), (88, 56), (76, 40), (60, 34), (44, 36), (30, 50), (24, 76), (22, 110, 1), (16, 90)]),
              L(outline([(30, 20), (52, 10), (66, 14), (44, 22)]), 'light', 'f', False)],
    'side': [L(outline([(56, 58), (62, 46), (84, 46), (94, 30), (90, 12), (100, -2, 1), (78, 0), (70, -18, 1), (56, -4), (40, -16, 1), (32, 2), (10, 4, 1), (14, 18),
                        (-6, 30, 1), (8, 40), (2, 60), (14, 76), (32, 76), (46, 68)])),
             L(outline([(6, 36), (24, 42), (26, 70), (10, 64)]), 'shade', 'b', False),
             fringe([(66, 4), (90, 16), (96, 40), (92, 56, 1), (84, 42), (74, 32)])],
    'back': [L(outline([(16, 80), (10, 50), (12, 14), (24, -4), (30, 6), (40, -20, 1), (52, 0), (70, -10, 1), (74, 6), (96, 4, 1), (88, 20), (108, 30, 1), (92, 42),
                        (106, 56, 1), (90, 64), (88, 82), (50, 88)])),
             L(outline([(56, 2), (84, 14), (96, 46), (88, 80), (62, 86)]), 'shade', 'b', False),
             strand([(26, 30), (40, 50), (34, 76)], 'deep', 'b', 1.0), strand([(72, 30), (60, 50), (66, 76)], 'deep', 'b', 1.0)],
}

# Harry Dwind: melena naranja dorada larga barrida por el viento hacia un lado, con mechones que vuelan por fuera de la
# cabeza y le tapan medio ojo; ojos grises grandes y gesto serio
CHARS['harry-dwind'] = {
    'body': 'delgado', 'pal': pal('#e8a03a', '#fce8d0', iris='#5a5a62'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(84, 80), (90, 50), (88, 20), (70, 2), (44, -2), (20, 10), (6, 34), (-10, 46), (-30, 70, 1), (-8, 64), (-24, 96, 1), (-2, 80), (-10, 106, 1),
                         (10, 86), (14, 64), (24, 56), (80, 56)])),
              L(outline([(62, 4), (84, 18), (90, 50), (84, 76), (78, 40)]), 'shade', 'b', False),
              fringe([(86, 60), (86, 36), (74, 18), (50, 10), (24, 20), (10, 44), (-6, 60, 1), (14, 54), (30, 46), (40, 50), (52, 82, 1), (56, 54), (66, 70, 1), (72, 50),
                      (80, 70, 1)]),
              L(outline([(16, 40), (36, 22), (56, 18), (34, 34)]), 'shade', 'f', False)],
    'side': [L(outline([(56, 62), (60, 48), (82, 50), (94, 36), (90, 14), (70, -2), (40, -4), (14, 8), (0, 30), (-8, 60), (-2, 86), (10, 100), (24, 96), (40, 88), (48, 74)])),
             L(outline([(2, 30), (30, 34), (40, 70), (24, 92), (6, 80)]), 'shade', 'b', False),
             strand([(14, 20), (24, 50), (20, 90)], 'deep', 'b', 1.0), strand([(36, 8), (44, 40), (40, 80)], 'deep', 'b', 1.0),
             fringe([(64, 2), (90, 16), (96, 40), (92, 62, 1), (84, 48), (74, 36)])],
    'back': [L(outline([(16, 80), (10, 40), (22, 10), (50, 0), (78, 8), (92, 30), (96, 60), (110, 76), (124, 96, 1), (100, 90), (92, 104, 1), (80, 88), (50, 90), (30, 88)])),
             L(outline([(56, 4), (84, 16), (96, 50), (112, 88), (80, 86), (72, 40)]), 'shade', 'b', False),
             strand([(30, 20), (60, 50), (100, 84)], 'deep', 'b', 1.0), strand([(50, 10), (70, 40), (90, 90)], 'deep', 'b', 1.0)],
}

# Bracknell Forge: grandullón de piel tostada con una melena gris oscura enorme y salvaje de puntas que le cae hasta la espalda
# y un mechón rojo oscuro en lo alto que se curva como un cuerno; cicatrices en la cara y sonrisa feroz
CHARS['bracknell-forge'] = {
    'body': 'corpulento', 'pal': pal('#2c2c3a', '#c27848', iris='#c81e1e', horn='#7a1e1e', horn_d='#561414', scar='#8a4a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(14, 80), (-6, 86, 1), (2, 70), (-16, 60, 1), (2, 50), (-10, 34, 1), (8, 28), (6, 10), (24, 2), (50, 6), (76, 2), (94, 10), (92, 28),
                         (110, 34, 1), (98, 50), (116, 60, 1), (98, 70), (106, 86, 1), (86, 80), (84, 56), (16, 56)])),
              L(outline([(60, 6), (90, 16), (100, 60), (92, 80), (80, 40)]), 'shade', 'b', False),
              L(outline([(40, 40), (36, 20), (40, 0), (54, -12), (76, -14), (94, -26, 1), (80, -6), (62, -2), (54, 14), (60, 40), (50, 52, 1)]), 'horn', 'f', ln=True),
              L(outline([(42, 30), (40, 8), (52, -4), (48, 14), (50, 40)]), 'horn_d', 'f', False),
              L([(70, 72), (78, 88)], 'scar', 'f', False, False, 1.6), L([(76, 70), (84, 86)], 'scar', 'f', False, False, 1.6)],
    'side': [L(outline([(58, 56), (64, 44), (84, 44), (90, 28), (78, 8), (52, 4), (26, 8), (6, 20), (-14, 14, 1), (-6, 32), (-32, 40, 1), (-10, 52), (-30, 70, 1), (-6, 72),
                        (-18, 96, 1), (4, 90), (4, 110, 1), (20, 94), (34, 80), (48, 66)])),
             L(outline([(-8, 40), (16, 46), (24, 86), (0, 86)]), 'shade', 'b', False),
             L(outline([(70, 30), (64, 10), (50, -6), (30, -10), (10, -24, 1), (34, -20), (56, -16), (74, 0), (80, 26)]), 'horn', 'f', ln=True),
             L([(80, 74), (88, 86)], 'scar', 'f', False, False, 1.6)],
    'back': [L(outline([(8, 96), (-14, 104, 1), (-4, 84), (-22, 70, 1), (-4, 60), (-16, 40, 1), (4, 34), (6, 10), (24, 2), (50, 6), (76, 2), (94, 10), (96, 34),
                        (116, 40, 1), (104, 60), (122, 70, 1), (104, 84), (114, 104, 1), (92, 96), (80, 112, 1), (64, 98), (50, 114, 1), (36, 98), (20, 112, 1)])),
             L(outline([(56, 8), (90, 16), (104, 60), (100, 100), (70, 100), (74, 40)]), 'shade', 'b', False),
             L(outline([(40, 20), (36, 4), (44, -10), (62, -14), (84, -12), (100, -26, 1), (88, -2), (64, 0), (56, 20)]), 'horn', 'f', ln=True)],
}

# Damien Blackloch (Teruyami Muu, capitán): pelo celeste pálido despeinado de puntas, con una antena de pelo en lo alto y las
# capas de debajo rosadas que asoman a los lados de la cara; ojos verde amarillento y media sonrisa
CHARS['damien-blackloch'] = {
    'body': 'normal', 'pal': pal('#c8f0ee', '#fce8cc', iris='#8a9a2a', shade='#a0b8b8', pink='#f0c4c8', pink_d='#d8a0a8'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 66), (10, 98, 1), (18, 90), (20, 66)]), 'pink', 'b', ln=True),
              L(outline([(86, 66), (90, 98, 1), (82, 90), (80, 66)]), 'pink', 'b', ln=True),
              L(outline([(14, 68), (2, 64, 1), (10, 54), (-4, 42, 1), (8, 36), (6, 16), (22, 2), (44, -4), (66, -2), (84, 8), (94, 22), (92, 36), (106, 42, 1), (92, 54),
                         (98, 64, 1), (86, 68), (82, 54), (18, 54)])),
              L(quad((50, -2), (44, -18), (54, -24)), 'mid', 'b', False, False, 2.6),
              L(outline([(60, 0), (84, 12), (94, 40), (88, 62), (78, 40)]), 'shade', 'b', False),
              fringe([(12, 62), (14, 38), (26, 18), (50, 10), (74, 18), (86, 38), (88, 62), (80, 50), (74, 60, 1), (66, 46), (58, 58, 1), (52, 44), (48, 64, 1), (42, 44),
                      (34, 58, 1), (28, 46), (20, 60, 1)])],
    'side': [L(outline([(54, 62), (60, 48), (82, 50), (94, 36), (88, 14), (70, 0), (44, -4), (18, 6), (4, 26), (-6, 34, 1), (4, 46), (-10, 60, 1), (6, 66), (-4, 84, 1),
                        (16, 80), (20, 96, 1), (32, 82), (46, 76)]), 'shade'),
             L(outline([(20, 50), (10, 80), (20, 96), (36, 84), (44, 70)]), 'pink', 'b', False),
             L(quad((46, -2), (40, -18), (50, -24)), 'mid', 'b', False, False, 2.6),
             L(outline([(44, -4), (70, 0), (90, 16), (96, 40), (92, 62, 1), (84, 46), (80, 58, 1), (74, 40), (60, 30), (40, 22), (24, 10)]), 'mid', 'f')],
    'back': [L(outline([(14, 70), (0, 66, 1), (8, 56), (-6, 44, 1), (8, 38), (6, 16), (22, 2), (44, -4), (66, -2), (84, 8), (94, 22), (92, 38), (106, 44, 1), (92, 56),
                        (100, 66, 1), (86, 70), (92, 90, 1), (76, 84), (66, 100, 1), (56, 86), (44, 102, 1), (36, 86), (22, 96, 1), (20, 82)]), 'pink'),
             L(outline([(6, 16), (22, 2), (44, -4), (66, -2), (84, 8), (94, 22), (92, 40), (80, 52), (60, 44), (50, 54), (40, 44), (20, 52), (8, 40)]), 'mid', 'b', False),
             L(quad((50, -2), (46, -18), (54, -24)), 'mid', 'b', False, False, 2.6),
             L(outline([(16, 52), (40, 46), (60, 50), (84, 52), (80, 70), (50, 66), (20, 70)]), 'shade', 'b', False)],
}

# Brutus Nastion (portero de Colmillos del Norte): piel morena, pelo morado oscuro de pinchos hacia arriba y hacia los lados,
# con dos mechones blancos que le caen delante de la cara; ojos amarillos con marcas oscuras y los dientes apretados
CHARS['brutus-nastion'] = {
    'body': 'normal', 'pal': pal('#5a2a6a', '#a8704a', iris='#f0c81e', streak='#f4f4f0', mark='#3a2018'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(16, 76), (2, 80, 1), (8, 62), (-6, 50, 1), (8, 42), (-2, 20, 1), (18, 20), (20, -4, 1), (36, 8), (44, -22, 1), (54, 2), (72, -12, 1), (72, 8),
                         (96, 4, 1), (88, 24), (106, 30, 1), (92, 44), (104, 60, 1), (90, 62), (96, 80, 1), (84, 76), (82, 56), (18, 56)])),
              L(outline([(60, 0), (84, 14), (94, 44), (88, 70), (78, 40)]), 'shade', 'b', False),
              fringe([(16, 62), (18, 40), (30, 26), (50, 20), (70, 26), (84, 40), (86, 62), (76, 50), (66, 54), (58, 46), (50, 54), (42, 46), (34, 54), (24, 50)]),
              L(outline([(40, 30), (34, 50), (30, 80), (24, 108, 1), (36, 84), (42, 56), (50, 40)]), 'streak', 'f', ln=True),
              L(outline([(60, 30), (66, 50), (70, 80), (76, 108, 1), (64, 84), (58, 56), (50, 40)]), 'streak', 'f', ln=True),
              L([(30, 82), (38, 86)], 'mark', 'f', False, False, 1.6), L([(70, 82), (62, 86)], 'mark', 'f', False, False, 1.6)],
    'side': [L(outline([(56, 58), (62, 46), (84, 46), (94, 30), (88, 12), (100, -2, 1), (76, 0), (72, -18, 1), (56, -2), (40, -16, 1), (32, 2), (6, -2, 1), (12, 18),
                        (-12, 28, 1), (6, 38), (-8, 54, 1), (8, 58), (0, 78, 1), (18, 76), (24, 90, 1), (34, 78), (46, 70)])),
             L(outline([(4, 34), (24, 40), (26, 70), (8, 64)]), 'shade', 'b', False),
             L(outline([(76, 40), (82, 60), (84, 90), (88, 110, 1), (78, 92), (72, 60), (68, 44)]), 'streak', 'f', ln=True)],
    'back': [L(outline([(16, 82), (0, 84, 1), (8, 66), (-6, 52, 1), (8, 44), (-2, 20, 1), (18, 20), (20, -4, 1), (36, 8), (44, -22, 1), (54, 2), (72, -12, 1), (72, 8),
                        (96, 4, 1), (88, 24), (108, 30, 1), (92, 46), (106, 62, 1), (90, 66), (98, 84, 1), (82, 82), (50, 90)])),
             L(outline([(56, 2), (84, 14), (94, 48), (88, 80), (62, 86)]), 'shade', 'b', False),
             strand([(30, 26), (40, 50), (34, 76)], 'deep', 'b', 1.0), strand([(70, 26), (60, 50), (66, 76)], 'deep', 'b', 1.0)],
}

# Nate Gobby: piel morena, pelo azul marino en forma de casco redondo con una franja más clara en el centro de la frente y dos
# mechones blancos largos que le cuelgan por debajo de las orejas; ojos blancos redondos de susto
CHARS['nate-gobby'] = {
    'body': 'normal', 'pal': pal('#24306a', '#a8704a', iris='#1e1414', light='#6a76b8', lock='#f0e8e8', lock_d='#c8a8b0'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(16, 76), (12, 104, 1), (22, 96), (24, 76)]), 'lock', 'b', ln=True), L(outline([(84, 76), (88, 104, 1), (78, 96), (76, 76)]), 'lock', 'b', ln=True),
              L(outline([(8, 64), (4, 40), (12, 14), (34, -2), (66, -2), (88, 14), (96, 40), (92, 64), (80, 62), (20, 62)])),
              L(outline([(60, 0), (86, 14), (96, 42), (90, 62), (80, 40)]), 'shade', 'b', False),
              fringe([(6, 62), (8, 40), (18, 22), (34, 12), (50, 10), (66, 12), (82, 22), (92, 40), (94, 62), (84, 58), (76, 52), (66, 58), (58, 50), (50, 66, 1), (42, 50),
                      (34, 58), (24, 52), (16, 58)]),
              L(outline([(44, 4), (56, 4), (58, 40), (50, 62, 1), (42, 40)]), 'light', 'f', False)],
    'side': [L(outline([(56, 60), (60, 48), (82, 48), (96, 36), (92, 12), (70, -2), (40, -4), (16, 8), (2, 32), (0, 56), (10, 70), (30, 72), (46, 70)])),
             L(outline([(4, 36), (30, 40), (34, 68), (10, 66)]), 'shade', 'b', False),
             L(outline([(52, 70), (56, 100, 1), (48, 92), (44, 72)]), 'lock', 'f', ln=True)],
    'back': [L(outline([(8, 64), (4, 40), (12, 14), (34, -2), (66, -2), (88, 14), (96, 40), (92, 64), (76, 72), (50, 76), (24, 72)])),
             L(outline([(56, 0), (86, 14), (96, 44), (90, 64), (66, 72)]), 'shade', 'b', False),
             L(outline([(18, 72), (16, 102, 1), (26, 94), (28, 74)]), 'lock', 'f', ln=True), L(outline([(82, 72), (84, 102, 1), (74, 94), (72, 74)]), 'lock', 'f', ln=True)],
}

# Keith Wellington: pelo azul marino oscuro en forma de champiñón enorme, muy ancho, que le tapa los ojos por completo; por
# detrás cae largo y liso hasta la espalda; boca pequeña abierta
CHARS['keith-wellington'] = {
    'body': 'normal', 'pal': pal('#2a2c4e', '#fce4c4', iris='#1e1414'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 102, 'hairline': False},
    'front': [L(outline([(-12, 60), (-14, 40), (0, 14), (26, 0), (50, -2), (74, 0), (100, 14), (114, 40), (112, 60), (100, 76), (86, 80), (78, 64), (64, 56), (58, 64),
                         (50, 74), (42, 64), (36, 56), (22, 64), (14, 80), (0, 76)]), 'mid', 'f'),
              L(outline([(60, 2), (98, 16), (112, 44), (104, 70), (86, 70), (84, 40)]), 'shade', 'f', False),
              L(outline([(40, 2), (54, 0), (48, 16), (36, 14)]), 'light', 'f', False),
              L(outline([(44, 100), (56, 100), (54, 106), (46, 106)]), (200, 110, 110, 255), 'f', ln=True)],
    'side': [L(outline([(70, 52), (86, 66), (92, 50), (90, 26), (70, 4), (40, -2), (14, 8), (0, 30), (-6, 70), (-8, 120), (-2, 128), (10, 110), (20, 80), (36, 70), (54, 56)])),
             L(outline([(-4, 50), (16, 50), (14, 110), (-4, 120)]), 'shade', 'b', False)],
    'back': [L(outline([(-12, 60), (-14, 40), (0, 14), (26, 0), (50, -2), (74, 0), (100, 14), (114, 40), (112, 60), (98, 72), (84, 76), (80, 130), (50, 136), (20, 130),
                        (16, 76), (0, 72)])),
             L(outline([(56, 2), (98, 16), (112, 46), (98, 70), (82, 76), (80, 128), (60, 132), (70, 40)]), 'shade', 'b', False),
             strand([(40, 80), (38, 130)], 'deep', 'b', 1.0), strand([(60, 80), (62, 130)], 'deep', 'b', 1.0)],
}

# Reggie Alldark: melena roja muy larga y ondulada que le tapa los ojos y cae abierta por los lados hasta los hombros; solo se
# le ve una sonrisa enorme de dientes y una bufanda roja al cuello
CHARS['reggie-alldark'] = {
    'body': 'bajito', 'pal': pal('#c41e30', '#fce4c4', iris='#1e1414', shade='#9a1424', scarf='#c8243a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 92, 'hairline': False},
    'front': [L(outline([(12, 100), (-14, 110, 1), (-8, 90), (-20, 70, 1), (-2, 66), (2, 36), (16, 10), (42, -2), (66, 0), (86, 12), (98, 36), (102, 66), (120, 70, 1),
                         (108, 90), (114, 110, 1), (88, 100), (80, 70), (20, 70)])),
              L(outline([(62, 2), (88, 16), (100, 50), (104, 90), (88, 92), (80, 40)]), 'shade', 'b', False),
              fringe([(10, 84), (8, 50), (20, 24), (48, 12), (76, 20), (90, 46), (92, 84), (84, 70), (78, 86, 1), (72, 64), (62, 78, 1), (58, 62), (50, 80, 1), (42, 62),
                      (36, 78, 1), (28, 64), (20, 86, 1), (16, 70)]),
              L(outline([(14, 100), (34, 96), (50, 104), (66, 96), (86, 100), (84, 114), (50, 118), (16, 114)]), 'scarf', 'f', ln=True)],
    'side': [L(outline([(58, 74), (64, 60), (86, 58), (96, 40), (88, 14), (62, 0), (34, 0), (12, 14), (0, 40), (-10, 70), (-24, 90, 1), (-4, 88), (4, 104, 1), (20, 94),
                        (34, 104, 1), (44, 88)])),
             L(outline([(0, 40), (24, 44), (34, 90), (8, 92)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 16), (98, 40), (96, 74, 1), (86, 56), (82, 70, 1), (76, 46), (66, 36)]),
             L(outline([(44, 100), (78, 100), (82, 110), (48, 114)]), 'scarf', 'f', ln=True)],
    'back': [L(outline([(10, 100), (-14, 108, 1), (-6, 86), (-20, 68, 1), (-2, 62), (2, 34), (16, 10), (42, -2), (66, 0), (86, 12), (98, 34), (102, 62), (120, 68, 1),
                        (106, 86), (114, 108, 1), (90, 100), (70, 108, 1), (60, 96), (50, 110, 1), (40, 96), (30, 108, 1)])),
             L(outline([(56, 2), (88, 16), (100, 50), (106, 100), (70, 100), (70, 40)]), 'shade', 'b', False),
             strand([(24, 30), (14, 70), (8, 96)], 'deep', 'b', 1.0), strand([(76, 30), (86, 70), (92, 96)], 'deep', 'b', 1.0)],
}
