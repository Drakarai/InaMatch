"""Raimon Isla Remota (ares-inakuni-raimon, Inakuni Raimon): sus modelos 3D de Inazuma Eleven Ares (zukan, 'アレスの天秤') como
referencia (busto de frente, perfil y espalda), calcados sobre la rejilla de unidades de cabeza."""
from chars import CHARS, L, OUTC, ell, outline, pal, strand
from heads import quad

WHITE = (248, 248, 248, 255)


def fringe(pts, c='mid'):
    """Flequillo por delante de la cara (las puntas, con un tercer valor, afiladas)."""
    return L(outline(pts), c, 'f')


# Norika Umihara (Sandra Fischer, portera): media melena verde azulado oscuro de rizos gordos que se abren como nubes a los
# lados de la cara y por detrás, flequillo partido en curva sobre la frente; ojos grandes azul marino
CHARS['sandra-fischer'] = {
    'body': 'chica', 'pal': pal('#33544e', '#fcdcc4', iris='#2a3a7a', shade='#243e3a', light='#4e7068'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 100), (0, 104), (-14, 92), (-12, 76), (-4, 64), (0, 44), (8, 22), (26, 6), (50, 0), (74, 6), (92, 22), (100, 44), (104, 62),
                         (114, 74), (112, 92), (100, 104), (84, 100), (84, 70), (16, 70)])),
              L(outline([(60, 4), (86, 16), (100, 44), (108, 72), (106, 96), (88, 96), (84, 60)]), 'shade', 'b', False),
              L(ell(-2, 84, 12, 11), 'mid', 'b', ln=True), L(ell(102, 84, 12, 11), 'mid', 'b', ln=True),
              L(ell(4, 62, 10, 10), 'mid', 'b', ln=True), L(ell(96, 62, 10, 10), 'mid', 'b', ln=True),
              fringe([(12, 70), (12, 42), (24, 20), (46, 12), (50, 20), (56, 12), (78, 20), (88, 40), (90, 70), (84, 52), (74, 38), (58, 30), (52, 40), (48, 40),
                      (42, 30), (26, 38), (16, 54)]),
              L(outline([(26, 22), (40, 16), (34, 26)]), 'light', 'f', False), strand([(50, 4), (50, 22)], 'shade', 'f', 1.2)],
    'side': [L(outline([(54, 64), (60, 50), (80, 50), (92, 36), (88, 14), (66, 0), (36, 0), (14, 12), (4, 34), (-10, 46), (-18, 66), (-14, 86), (-2, 100),
                        (16, 104), (30, 96), (40, 104), (52, 96), (50, 80)])),
             L(ell(-6, 72, 12, 12), 'shade', 'b', ln=True), L(ell(6, 94, 12, 11), 'mid', 'b', ln=True), L(ell(34, 96, 11, 10), 'mid', 'b', ln=True),
             L(outline([(4, 34), (26, 40), (30, 70), (10, 66)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 16), (94, 40), (92, 60), (86, 56), (84, 44), (76, 34), (66, 30)]),
             L(ell(56, 72, 9, 9), 'mid', 'f', ln=True)],
    'back': [L(outline([(16, 76), (-2, 84), (-14, 76), (-10, 56), (0, 40), (8, 18), (26, 4), (50, -2), (74, 4), (92, 18), (100, 40), (110, 56), (114, 76),
                        (102, 84), (84, 80), (90, 98), (76, 106), (64, 98), (50, 106), (36, 98), (24, 106), (10, 98)])),
             L(outline([(56, 2), (86, 14), (104, 44), (112, 78), (92, 102), (66, 100), (72, 50)]), 'shade', 'b', False),
             L(ell(-2, 80, 12, 10), 'shade', 'b', ln=True), L(ell(102, 80, 12, 10), 'shade', 'b', ln=True),
             L(ell(20, 96, 12, 10), 'mid', 'b', ln=True), L(ell(50, 98, 13, 10), 'mid', 'b', ln=True), L(ell(80, 96, 12, 10), 'mid', 'b', ln=True)],
}

# Masakatsu Hiyori (Kiko Calavento): gorra de repartidor marrón oscuro, abombada, y debajo el pelo blanco liso que se abre
# hacia los lados como una campana hasta la mandíbula; piel morena, ojos azules redondos y sonrisa pícara
CHARS['kiko-calavento'] = {
    'body': 'normal', 'pal': pal('#f2f4f6', '#c08458', iris='#2a5ab8', shade='#c8c4c8', deep='#a8a0a8', cap='#3e302c', cap_d='#2a201e'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 74), (-18, 96), (-26, 98, 1), (-6, 102), (16, 98), (24, 70), (76, 70), (84, 98), (106, 102), (126, 98, 1), (118, 96), (86, 74),
                         (90, 40), (10, 40)])),
              L(outline([(64, 44), (92, 52), (118, 94), (90, 96), (82, 66)]), 'shade', 'b', False),
              fringe([(12, 64), (14, 44), (86, 44), (88, 64), (82, 58), (76, 70, 1), (70, 56), (62, 66, 1), (58, 54), (50, 72, 1), (44, 54), (38, 66, 1),
                      (32, 56), (24, 70, 1), (18, 58)]),
              L(outline([(4, 42), (2, 20), (14, 2), (50, -6), (86, 2), (98, 20), (96, 42), (50, 46)]), 'cap', 'f', ln=True),
              L(outline([(56, -4), (86, 4), (96, 22), (94, 40), (70, 42)]), 'cap_d', 'f', False),
              L(quad((4, 34), (50, 44), (96, 34)), 'cap_d', 'f', False, False, 2.0)],
    'side': [L(outline([(54, 62), (60, 50), (80, 50), (86, 44), (40, 40), (10, 44), (-20, 88), (-30, 96, 1), (-4, 98), (16, 92), (30, 98), (44, 84), (48, 70)])),
             L(outline([(10, 46), (30, 48), (30, 84), (-10, 90)]), 'shade', 'b', False),
             fringe([(70, 42), (90, 44), (94, 60, 1), (86, 52), (80, 60, 1), (74, 50)]),
             L(outline([(6, 44), (2, 20), (20, 0), (52, -6), (80, 2), (94, 18), (98, 32), (118, 36), (122, 42), (96, 44), (60, 46)]), 'cap', 'f', ln=True),
             L(outline([(94, 34), (120, 37), (122, 42), (96, 44)]), 'cap_d', 'f', False)],
    'back': [L(outline([(10, 44), (-20, 90), (-28, 98, 1), (0, 100), (20, 94), (50, 100), (80, 94), (100, 100), (128, 98, 1), (120, 90), (90, 44)])),
             L(outline([(56, 46), (90, 46), (118, 92), (90, 98), (70, 96)]), 'shade', 'b', False),
             L(outline([(4, 46), (2, 20), (14, 2), (50, -6), (86, 2), (98, 20), (96, 46), (50, 50)]), 'cap', 'f', ln=True),
             L(outline([(56, -4), (86, 4), (96, 22), (96, 44), (70, 46)]), 'cap_d', 'f', False)],
}

# Yuuichirou Mansaku (Trevor Cook): gorra de béisbol de copa blanca alta y visera azul marino, y debajo una melena castaña
# ondulada hasta los hombros; ojos azul grisáceo serios bajo la sombra de la visera
CHARS['trevor-cook'] = {
    'body': 'normal', 'pal': pal('#6a5236', '#fcd0a8', iris='#5a6a84', shade='#54402a', deep='#3e2e1e', cap='#eeeef0', cap_d='#c8c4cc', visor='#22408a',
                                 visor_d='#162c66'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 104), (4, 100, 1), (8, 86), (4, 74, 1), (8, 60), (8, 40), (92, 40), (92, 60), (96, 74, 1), (92, 86), (96, 100, 1), (90, 104),
                         (84, 90), (84, 60), (16, 60), (16, 90)])),
              L(outline([(80, 44), (92, 50), (94, 98), (86, 96)]), 'shade', 'b', False),
              strand([(12, 64), (10, 80), (14, 96)], 'deep', 'f', 1.2), strand([(88, 64), (90, 80), (86, 96)], 'deep', 'f', 1.2),
              L(outline([(8, 26), (6, 4), (18, -18), (50, -26), (82, -18), (94, 4), (92, 26), (50, 22)]), 'cap', 'f', ln=True),
              L(outline([(60, -22), (82, -16), (92, 4), (90, 24), (70, 22)]), 'cap_d', 'f', False),
              L(outline([(6, 26), (50, 20), (94, 26), (92, 44), (78, 52), (50, 50), (22, 52), (8, 44)]), 'visor', 'f', ln=True),
              L(outline([(56, 22), (94, 28), (92, 42), (76, 50), (58, 48)]), 'visor_d', 'f', False)],
    'side': [L(outline([(52, 76), (56, 60), (40, 44), (8, 44), (0, 70), (-6, 96), (-4, 106, 1), (6, 98), (12, 108, 1), (20, 98), (30, 106, 1), (34, 94),
                        (44, 90)])),
             L(outline([(4, 48), (24, 50), (28, 92), (6, 92)]), 'shade', 'b', False),
             L(outline([(6, 46), (0, 14), (14, -14), (46, -26), (78, -18), (92, 2), (94, 22), (124, 32), (128, 40), (96, 44), (60, 48)]), 'cap', 'f', ln=True),
             L(outline([(92, 18), (124, 30), (128, 40), (94, 44)]), 'visor', 'f', ln=True),
             L(outline([(10, -6), (44, -22), (40, 0), (20, 20)]), 'cap_d', 'f', False)],
    'back': [L(outline([(8, 100), (4, 96, 1), (6, 80), (4, 60), (6, 40), (94, 40), (96, 60), (94, 80), (96, 96, 1), (92, 100), (80, 104, 1), (70, 98),
                        (60, 106, 1), (50, 98), (40, 106, 1), (30, 98), (20, 104, 1)])),
             L(outline([(56, 42), (94, 42), (94, 96), (66, 100)]), 'shade', 'b', False),
             strand([(26, 50), (22, 70), (28, 96)], 'deep', 'b', 1.2), strand([(74, 50), (78, 70), (72, 96)], 'deep', 'b', 1.2),
             L(outline([(8, 44), (6, 4), (18, -18), (50, -26), (82, -18), (94, 4), (92, 44), (50, 40)]), 'cap', 'f', ln=True),
             L(outline([(56, -22), (82, -16), (94, 4), (92, 42), (60, 40)]), 'cap_d', 'f', False)],
}

# Takashi Iwato (Cliff Parker): el grandullón, cabeza ancha y cuadrada de piel morena con el pelo azul marino muy corto en un
# cepillo plano; ojos pequeños de cejas pobladas y media sonrisa
CHARS['cliff-parker'] = {
    'body': 'corpulento', 'pal': pal('#1e3448', '#a8744c', iris='#1e1414', shade='#142434'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 100, 'hairline': [(12, 62), (14, 40), (30, 34), (50, 34), (70, 34), (86, 40),
                                                                                              (88, 62)], 'big_ears': 2,
             'face_front': outline([(10, 60), (12, 30), (50, 24), (88, 30), (90, 60), (90, 96), (76, 112), (50, 116), (24, 112), (10, 96)])},
    'front': [L(outline([(10, 62), (8, 26), (14, 4), (50, -2), (86, 4), (92, 26), (90, 62), (86, 40), (14, 40)])),
              L(outline([(60, 0), (86, 6), (92, 30), (86, 40), (70, 34)]), 'shade', 'b', False)],
    'side': [L(outline([(58, 46), (66, 34), (88, 30), (92, 12), (80, 0), (40, -4), (12, 6), (4, 36), (8, 58), (26, 62), (40, 52)])),
             L(outline([(6, 34), (26, 36), (24, 58), (10, 56)]), 'shade', 'b', False)],
    'back': [L(outline([(10, 60), (8, 26), (14, 4), (50, -2), (86, 4), (92, 26), (90, 60), (70, 64), (30, 64)])),
             L(outline([(56, 2), (86, 6), (92, 40), (88, 58), (64, 62)]), 'shade', 'b', False)],
}

# Hanta Hattori (Nino Nango): el ninja; capucha gris oscuro que le cubre toda la cabeza con dos orejas puntiagudas, una muy
# alta, y un nudo en la nuca con dos puntas que ondean; por la abertura asoma la cara con un mechón gris
CHARS['nino-nango'] = {
    'body': 'bajito', 'pal': pal('#8a8488', '#fcd8b4', iris='#2a2a3a', hood='#3e3c3e', hood_d='#2a282a', hood_l='#565456'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(4, 100), (0, 60), (6, 30), (-2, -6), (24, 14), (44, 6), (60, 8), (92, -40, 1), (96, 6), (100, 40), (98, 70), (96, 100), (80, 108),
                         (20, 108)]), 'hood'),
              L(outline([(70, 12), (92, -36), (94, 10), (98, 60), (90, 96), (82, 60)]), 'hood_d', 'b', False),
              L(outline([(14, 66), (16, 46), (30, 34), (50, 30), (70, 34), (84, 46), (86, 66), (86, 98), (70, 110), (30, 110), (14, 98)]), 'skin', 'b', False),
              fringe([(16, 64), (18, 46), (32, 36), (50, 32), (60, 36), (70, 48), (62, 46), (50, 60, 1), (44, 50), (30, 54), (20, 66)]),
              L(outline([(12, 104), (24, 98), (50, 104), (76, 98), (88, 104), (86, 118), (14, 118)]), 'hood', 'f', ln=True)],
    'side': [L(outline([(60, 60), (66, 46), (82, 48), (90, 30), (78, 4), (90, -44, 1), (56, -2), (30, -2), (10, 16), (2, 50), (4, 86), (-10, 96), (-30, 110, 1),
                        (-6, 106), (-24, 120, 1), (8, 110), (40, 108), (56, 98)]), 'hood'),
             L(outline([(4, 40), (30, 44), (34, 96), (8, 96)]), 'hood_d', 'b', False),
             L(outline([(64, 46), (84, 50), (92, 64), (88, 98), (66, 102)]), 'skin', 'b', False),
             fringe([(66, 46), (88, 46), (94, 58), (84, 56), (76, 64, 1), (70, 54)])],
    'back': [L(outline([(4, 104), (2, 60), (6, 30), (-2, -6), (24, 14), (44, 6), (60, 8), (92, -40, 1), (96, 6), (100, 40), (98, 70), (96, 104), (50, 110)]),
               'hood'),
             L(outline([(56, 10), (92, -36), (96, 10), (98, 100), (66, 106)]), 'hood_d', 'b', False),
             L(outline([(40, 96), (60, 96), (62, 106), (38, 106)]), 'hood_d', 'f', ln=True),
             L(outline([(42, 100), (20, 108), (-6, 116, 1), (16, 116), (40, 106)]), 'hood', 'f', ln=True),
             L(outline([(58, 100), (70, 112), (74, 130, 1), (78, 112), (60, 104)]), 'hood', 'f', ln=True)],
}

# Tatsumi Michinari (Maxime Dassier): melena lisa castaño oscuro verdoso hasta los hombros con flequillo recto cortado sobre
# las cejas (corte hime); piel morena clara, ojos castaños y media sonrisa
CHARS['maxime-dassier'] = {
    'body': 'normal', 'pal': pal('#3a3220', '#e8a878', iris='#7a4a1e', shade='#2a2418', light='#4e4430'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(6, 108), (0, 70), (2, 30), (14, 8), (50, -4), (86, 8), (98, 30), (100, 70), (94, 108), (82, 104), (84, 60), (16, 60), (18, 104)])),
              L(outline([(60, 0), (88, 12), (98, 40), (98, 100), (86, 100), (82, 50)]), 'shade', 'b', False),
              fringe([(10, 60), (8, 36), (20, 14), (50, 6), (80, 14), (92, 36), (90, 60), (82, 56), (80, 46), (70, 48), (68, 58), (58, 58), (56, 48), (44, 48),
                      (42, 58), (32, 58), (30, 48), (20, 46), (18, 58)]),
              L(outline([(24, 16), (44, 10), (34, 22)]), 'light', 'f', False)],
    'side': [L(outline([(52, 78), (56, 60), (78, 56), (92, 40), (90, 14), (68, -2), (36, -4), (12, 10), (0, 40), (-4, 80), (0, 108), (20, 112), (40, 104), (48, 92)])),
             L(outline([(0, 40), (24, 46), (30, 100), (6, 104)]), 'shade', 'b', False),
             fringe([(62, 2), (88, 16), (96, 40), (96, 54), (88, 54), (86, 44), (74, 40)])],
    'back': [L(outline([(6, 110), (0, 70), (2, 30), (14, 8), (50, -4), (86, 8), (98, 30), (100, 70), (94, 110), (50, 116)])),
             L(outline([(56, 0), (86, 10), (98, 40), (96, 106), (64, 112), (70, 50)]), 'shade', 'b', False),
             strand([(30, 30), (26, 70), (30, 108)], 'shade', 'b', 1.2), strand([(70, 30), (74, 70), (70, 108)], 'shade', 'b', 1.2)],
}

# Kirina Hiura (Valentin Eisner): pelo azul acero en mechones de punta que se abren a los lados, con un gran tupé que cruza la
# frente en diagonal hasta tapar el ojo izquierdo; por debajo y detrás es más oscuro; ojos morados y gesto serio
CHARS['valentin-eisner'] = {
    'body': 'normal', 'pal': pal('#6a92b4', '#fcd8b8', iris='#5a3a8a', shade='#3e4a5e', deep='#2e3644', light='#9ac0dc'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 90), (8, 74, 1), (10, 62), (-10, 50, 1), (6, 42), (-20, 28, 1), (4, 22), (12, 0), (34, -14), (60, -16), (82, -6), (94, 12), (120, 20, 1),
                         (98, 30), (112, 46, 1), (94, 52), (98, 72, 1), (88, 74), (90, 92, 1), (82, 84), (82, 64), (18, 64), (18, 84)]), 'shade'),
              L(outline([(4, 22), (12, 0), (34, -14), (60, -16), (82, -6), (94, 12), (120, 20, 1), (96, 26), (80, 30), (60, 26), (34, 30), (14, 40), (-20, 28, 1)]),
                'mid', 'b', False),
              fringe([(12, 70), (12, 46), (20, 30), (34, 16), (56, 8), (78, 16), (88, 34), (90, 60), (82, 52), (80, 66, 1), (74, 50), (66, 44), (60, 54), (56, 68),
                      (50, 80, 1), (46, 64), (36, 50), (28, 60, 1), (22, 52)]),
              L(outline([(30, 18), (56, 8), (76, 18), (84, 36), (66, 26), (46, 24)]), 'light', 'f', False)],
    'side': [L(outline([(54, 66), (58, 52), (80, 50), (94, 36), (100, 14), (86, -4), (60, -14), (30, -10), (8, 6), (-24, 14, 1), (0, 22), (-20, 40, 1), (2, 44),
                        (-10, 62, 1), (6, 66), (0, 84, 1), (16, 82), (18, 96, 1), (30, 84), (44, 80)]), 'shade'),
             L(outline([(8, 6), (30, -10), (60, -14), (86, -4), (100, 14), (96, 34), (70, 24), (40, 26), (10, 24), (-24, 14, 1)]), 'mid', 'b', False),
             fringe([(66, 2), (92, 14), (100, 36), (96, 62, 1), (88, 48), (82, 60, 1), (76, 42), (66, 30)]),
             L(outline([(70, 4), (94, 16), (98, 30), (82, 22)]), 'light', 'f', False)],
    'back': [L(outline([(16, 92), (8, 76, 1), (6, 60), (-10, 52, 1), (4, 42), (-20, 30, 1), (4, 22), (12, 0), (34, -14), (60, -16), (82, -6), (94, 12), (120, 22, 1),
                        (98, 32), (116, 52, 1), (96, 58), (94, 76, 1), (84, 92), (70, 98, 1), (60, 92), (50, 100, 1), (40, 92), (30, 98, 1)]), 'shade'),
             L(outline([(4, 22), (12, 0), (34, -14), (60, -16), (82, -6), (94, 12), (120, 22, 1), (96, 30), (70, 34), (50, 30), (30, 36), (6, 34), (-20, 30, 1)]),
               'mid', 'b', False)],
}

# Hiro Okuiri (César Montalbán): casco de pelo azul marino en seta, abombado y cortado recto a la altura de las orejas, con
# raya en medio que deja ver la frente; gafas redondas negras y ojos morados
CHARS['c-sar-montalb-n'] = {
    'body': 'normal', 'pal': pal('#24305a', '#fcd8b8', iris='#6a2a5a', shade='#18203e', light='#3a4878'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False, 'glasses': OUTC},
    'front': [L(outline([(10, 72), (2, 56), (4, 26), (20, 6), (50, -2), (80, 6), (96, 26), (100, 56), (90, 72), (84, 62), (16, 62)])),
              L(outline([(60, 2), (84, 10), (98, 34), (94, 64), (82, 48)]), 'shade', 'b', False),
              fringe([(8, 64), (6, 40), (18, 16), (46, 8), (50, 14), (54, 8), (82, 16), (94, 40), (92, 64), (82, 56), (68, 42), (56, 34), (52, 52, 1), (48, 52),
                      (44, 34), (32, 42), (18, 56)]),
              L(outline([(22, 18), (40, 12), (30, 24)]), 'light', 'f', False)],
    'side': [L(outline([(54, 66), (58, 54), (94, 50), (100, 30), (88, 6), (56, -4), (26, 0), (6, 16), (-6, 40), (-4, 66), (10, 78), (30, 78), (46, 74)])),
             L(outline([(-4, 40), (22, 44), (28, 74), (4, 72)]), 'shade', 'b', False),
             fringe([(60, 2), (92, 14), (100, 32), (98, 52), (88, 50), (84, 40), (70, 34)])],
    'back': [L(outline([(10, 80), (2, 60), (4, 26), (20, 6), (50, -2), (80, 6), (96, 26), (100, 60), (90, 80), (70, 86), (30, 86)])),
             L(outline([(56, 2), (84, 10), (98, 38), (92, 78), (66, 84)]), 'shade', 'b', False)],
}

# Asuto Inamori (Sonny Wright): el protagonista; pelo negro de pinchos de punta hacia arriba, dos más altos y otros a los
# lados por encima de las orejas, y un mechón que le cae por la frente; ojos grandes azules y sonrisa
CHARS['sonny-wright'] = {
    'body': 'normal', 'pal': pal('#2e2a30', '#fcd8b8', iris='#2a5a8a', shade='#1e1c20', light='#4a4650'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 70), (14, 56), (-2, 46, 1), (12, 36), (14, 14), (16, -10, 1), (28, 4), (36, -22, 1), (44, 0), (60, 2), (80, -6, 1), (78, 10),
                         (88, 22), (90, 38), (104, 44, 1), (88, 52), (86, 70), (80, 58), (20, 58)])),
              L(outline([(60, 4), (82, 12), (90, 38), (86, 64), (76, 40)]), 'shade', 'b', False),
              fringe([(14, 64), (16, 42), (28, 24), (50, 16), (72, 24), (86, 42), (86, 64), (80, 52), (72, 58, 1), (66, 44), (56, 52, 1), (52, 38), (40, 64, 1),
                      (36, 46), (28, 58, 1), (20, 52)]),
              L(outline([(30, 4), (42, 0), (36, 14)]), 'light', 'f', False)],
    'side': [L(outline([(54, 62), (60, 48), (80, 48), (92, 38), (94, 20), (86, 4), (72, -2), (66, -22, 1), (54, -4), (40, -30, 1), (30, 0), (10, 10), (2, 30),
                        (-14, 36, 1), (2, 46), (2, 66), (14, 80), (24, 92, 1), (32, 80), (46, 74)])),
             L(outline([(4, 34), (24, 40), (28, 72), (8, 66)]), 'shade', 'b', False),
             fringe([(68, 2), (92, 16), (98, 40), (94, 60, 1), (88, 46), (80, 40)])],
    'back': [L(outline([(16, 84), (10, 60), (-10, 42, 1), (10, 36), (12, 14), (8, -12, 1), (26, 2), (36, -22, 1), (46, 0), (66, -2), (78, -24, 1), (80, 4),
                        (90, 20), (92, 36), (110, 40, 1), (92, 50), (90, 84), (74, 82), (66, 96, 1), (58, 84), (42, 84), (34, 96, 1), (26, 84)])),
             L(outline([(56, 2), (82, 8), (92, 40), (88, 80), (64, 82)]), 'shade', 'b', False)],
}

# Sasuke Kozoumaru (Basile Hardy): melena castaño muy oscuro de pinchos alborotados en todas direcciones, con una cinta gris
# verdosa que asoma por los lados; ojos afilados, cejas fruncidas y boca enfadada
CHARS['basile-hardy'] = {
    'body': 'normal', 'pal': pal('#2e2024', '#f6c6a0', iris='#2a2028', shade='#1e1418', band='#5a5e52'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(16, 72), (2, 70, 1), (8, 58), (-12, 46, 1), (6, 38), (-8, 22, 1), (12, 18), (14, 0, 1), (28, 8), (38, -8, 1), (48, 4), (56, -10, 1),
                         (64, 4), (80, -6, 1), (78, 12), (96, 14, 1), (90, 28), (108, 38, 1), (92, 46), (106, 58, 1), (88, 62), (98, 74, 1), (84, 72), (84, 58),
                         (16, 58)])),
              L(outline([(60, 2), (84, 10), (96, 40), (92, 66), (80, 44)]), 'shade', 'b', False),
              L(outline([(12, 50), (20, 46), (20, 62), (12, 64)]), 'band', 'f', ln=True), L(outline([(88, 50), (80, 46), (80, 62), (88, 64)]), 'band', 'f', ln=True),
              fringe([(16, 60), (18, 40), (30, 26), (50, 20), (70, 26), (82, 40), (84, 60), (76, 50), (70, 60, 1), (64, 46), (56, 56, 1), (52, 42), (44, 58, 1),
                      (38, 44), (30, 56, 1), (24, 46)])],
    'side': [L(outline([(56, 60), (62, 48), (82, 46), (96, 30), (102, 10, 1), (84, 12), (80, -6, 1), (64, 4), (54, -16, 1), (44, 2), (24, -8, 1), (22, 10),
                        (-4, 6, 1), (8, 24), (-18, 32, 1), (4, 40), (-20, 54, 1), (2, 58), (-10, 76, 1), (8, 74), (2, 92, 1), (20, 84), (28, 96, 1), (36, 82),
                        (46, 72)])),
             L(outline([(4, 38), (26, 44), (28, 76), (8, 72)]), 'shade', 'b', False),
             L(outline([(28, 50), (60, 46), (62, 54), (30, 60)]), 'band', 'f', ln=True),
             fringe([(68, 4), (92, 18), (98, 40), (92, 60, 1), (86, 46), (78, 38)])],
    'back': [L(outline([(16, 86), (0, 84, 1), (8, 70), (-12, 58, 1), (6, 48), (-10, 32, 1), (10, 26), (6, 2, 1), (24, 10), (32, -10, 1), (44, 4), (54, -12, 1),
                        (62, 4), (80, -8, 1), (78, 12), (100, 14, 1), (90, 30), (112, 40, 1), (94, 50), (108, 66, 1), (90, 70), (100, 86, 1), (84, 86), (70, 96, 1),
                        (62, 86), (50, 98, 1), (40, 86), (30, 96, 1)])),
             L(outline([(56, 4), (84, 12), (100, 42), (94, 82), (66, 88)]), 'shade', 'b', False)],
}

# Tetsunosuke Goujin (Adriano Donati): piel morena, pelo morado corto y rizado muy apretado, como un casco alto; ojos blancos
# redondos de pupila pequeña, cejas fruncidas y gesto serio
CHARS['adriano-donati'] = {
    'body': 'normal', 'pal': pal('#4e4a8a', '#a8744c', iris='#1e1414', shade='#363268', deep='#28244e'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'hairline': [(14, 64), (16, 46), (30, 40), (50, 42), (70, 40), (84, 46), (86, 64)]},
    'front': [L(outline([(14, 66), (10, 30), (14, 6), (30, -8), (50, -12), (70, -8), (86, 6), (90, 30), (86, 66), (84, 46), (16, 46)])),
              L(outline([(60, -8), (84, 4), (90, 30), (86, 60), (76, 36)]), 'shade', 'b', False)]
             + [L(ell(x, y, 2.4, 1.6), 'deep', 'b', False) for x, y in ((24, 10), (40, 2), (58, 4), (74, 12), (30, 26), (50, 18), (68, 26), (18, 40), (82, 40))],
    'side': [L(outline([(58, 46), (66, 36), (86, 32), (92, 10), (80, -8), (50, -14), (20, -6), (6, 14), (2, 46), (6, 70), (24, 78), (40, 60)])),
             L(outline([(4, 40), (26, 42), (30, 74), (10, 70)]), 'shade', 'b', False)]
            + [L(ell(x, y, 2.4, 1.6), 'deep', 'b', False) for x, y in ((24, 0), (44, -6), (64, -2), (16, 22), (40, 14), (62, 14), (80, 18), (20, 44))],
    'back': [L(outline([(12, 76), (8, 30), (14, 6), (30, -8), (50, -12), (70, -8), (86, 6), (92, 30), (88, 76), (50, 84)])),
             L(outline([(56, -8), (84, 4), (92, 34), (88, 72), (64, 80)]), 'shade', 'b', False)]
            + [L(ell(x, y, 2.4, 1.6), 'deep', 'b', False) for x, y in ((24, 10), (40, 2), (58, 4), (74, 12), (30, 30), (50, 24), (70, 30), (24, 52), (50, 50),
                                                                       (76, 52))],
}

# Kyuuta Kyouno (Rolland Bowlby, portero): pelo naranja de pinchos larguísimos hacia arriba y hacia los lados, con flequillo
# de puntas; ojos grandes y redondos castaños, pecas y una sonrisa enorme
CHARS['rolland-bowlby'] = {
    'body': 'normal', 'pal': pal('#e8641e', '#fcd8b8', iris='#6a3a1e', shade='#b84a14', light='#ff9a50'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 68), (8, 60, 1), (10, 48), (-16, 40, 1), (8, 30), (2, 6, 1), (20, 12), (20, -20, 1), (36, 0), (46, -10, 1), (54, 0), (66, -14, 1),
                         (70, 4), (88, -2, 1), (82, 18), (112, 26, 1), (92, 36), (104, 48, 1), (90, 54), (92, 68, 1), (84, 66), (84, 56), (16, 56)])),
              L(outline([(60, 2), (84, 10), (96, 36), (90, 62), (78, 40)]), 'shade', 'b', False),
              fringe([(14, 62), (16, 42), (28, 24), (50, 18), (72, 24), (86, 42), (86, 62), (80, 52), (74, 66, 1), (68, 46), (60, 58, 1), (56, 44), (50, 72, 1),
                      (44, 44), (38, 58, 1), (32, 46), (24, 64, 1), (20, 52)]),
              L(outline([(30, 6), (40, 0), (38, 16)]), 'light', 'f', False),
              L(ell(28, 92, 1, 1), OUTC, 'f', False), L(ell(32, 95, 1, 1), OUTC, 'f', False), L(ell(72, 92, 1, 1), OUTC, 'f', False), L(ell(68, 95, 1, 1), OUTC, 'f', False)],
    'side': [L(outline([(54, 60), (60, 46), (80, 46), (94, 34), (98, 12), (92, -6), (106, -30, 1), (74, -8), (64, -2), (50, -20, 1), (40, 2), (14, 0, 1), (16, 18),
                        (-12, 26, 1), (6, 36), (-18, 50, 1), (4, 56), (-6, 72, 1), (12, 72), (8, 88, 1), (24, 80), (36, 88, 1), (42, 76)])),
             L(outline([(4, 36), (24, 42), (26, 72), (8, 66)]), 'shade', 'b', False),
             fringe([(68, 4), (92, 16), (98, 40), (92, 62, 1), (86, 46), (80, 58, 1), (76, 40)])],
    'back': [L(outline([(16, 82), (0, 80, 1), (8, 66), (-16, 54, 1), (6, 46), (-10, 26, 1), (12, 22), (8, -4, 1), (26, 8), (34, -16, 1), (46, 2), (58, -20, 1),
                        (64, 2), (84, -10, 1), (80, 14), (106, 20, 1), (92, 36), (114, 50, 1), (94, 58), (106, 76, 1), (86, 80), (72, 94, 1), (62, 82), (50, 96, 1),
                        (40, 82), (28, 94, 1)])),
             L(outline([(56, 4), (84, 12), (100, 44), (94, 78), (66, 84)]), 'shade', 'b', False)],
}

# Zhao Jinyun (Mister Yi): el maestro, un gigante de cara redonda enorme; calvo por los lados con el pelo negro recogido en
# un moño del que sale una trenza que se enrosca hacia arriba, bigotes de gato y ojos achinados; abrigo rojo y bufanda parda
CHARS['mister-yi'] = {
    'body': 'corpulento', 'pal': pal('#2e2a30', '#f2d0a8', iris='#c8701e', shade='#1e1c20', scarf='#8a6a30', scarf_d='#6a4e22'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False, 'big_ears': 1,
             'face_front': outline([(8, 60), (12, 34), (30, 22), (50, 18), (70, 22), (88, 34), (92, 60), (96, 86), (84, 106), (50, 114), (16, 106), (4, 86)])},
    'front': [L(outline([(16, 40), (20, 16), (36, 2), (50, 0), (64, 2), (80, 16), (84, 40), (70, 30), (50, 26), (30, 30)])),
              L(outline([(46, 4), (54, 4), (52, -10), (46, -18), (44, -28), (38, -34), (32, -30), (34, -24), (40, -20), (44, -8)]), 'mid', 'b', ln=True),
              strand([(30, 28), (40, 8)], 'shade', 'b', 1.0), strand([(50, 26), (50, 4)], 'shade', 'b', 1.0), strand([(70, 28), (60, 8)], 'shade', 'b', 1.0),
              L(quad((30, 64), (36, 58), (44, 66)), OUTC, 'f', False, False, 2.2), L(quad((56, 66), (64, 58), (70, 64)), OUTC, 'f', False, False, 2.2),
              L(quad((32, 74), (38, 70), (44, 74)), OUTC, 'f', False, False, 1.8), L(quad((56, 74), (62, 70), (68, 74)), OUTC, 'f', False, False, 1.8),
              L(ell(38, 74, 1.6, 1.4), 'iris', 'f', False), L(ell(62, 74, 1.6, 1.4), 'iris', 'f', False),
              L(quad((32, 92), (50, 104), (68, 92)), OUTC, 'f', False, False, 1.8),
              L([(26, 86), (44, 94)], OUTC, 'f', False, False, 1.2), L([(26, 98), (44, 92)], OUTC, 'f', False, False, 1.2),
              L([(74, 86), (56, 94)], OUTC, 'f', False, False, 1.2), L([(74, 98), (56, 92)], OUTC, 'f', False, False, 1.2),
              L(outline([(-10, 104), (10, 92), (30, 106), (50, 110), (70, 106), (90, 92), (110, 104), (108, 128), (-8, 128)]), 'scarf', 'f', ln=True),
              L(outline([(56, 108), (90, 94), (108, 106), (106, 126), (70, 124)]), 'scarf_d', 'f', False)],
    'side': [L(outline([(40, 30), (44, 6), (60, 0), (80, 6), (90, 24), (70, 22), (50, 30)])),
             L(outline([(50, 4), (58, 4), (50, -12), (40, -24), (34, -38), (26, -36), (30, -26), (40, -14)]), 'mid', 'b', ln=True),
             L(quad((84, 66), (90, 60), (96, 66)), OUTC, 'f', False, False, 2.0),
             L(outline([(-14, 108), (10, 80), (40, 92), (80, 96), (104, 106), (100, 128), (-10, 128)]), 'scarf', 'f', ln=True),
             L(outline([(-12, 110), (10, 84), (24, 92), (20, 124), (-8, 124)]), 'scarf_d', 'f', False)],
    'back': [L(outline([(10, 80), (8, 40), (20, 14), (50, 2), (80, 14), (92, 40), (90, 80), (50, 90)])),
             L(outline([(56, 4), (82, 16), (92, 44), (88, 78), (64, 86)]), 'shade', 'b', False),
             L(outline([(46, 6), (54, 6), (60, -6), (72, -12), (84, -10), (90, -2), (84, 0), (72, -2), (60, 6)]), 'mid', 'f', ln=True),
             strand([(30, 60), (40, 20)], 'shade', 'b', 1.0), strand([(50, 70), (50, 10)], 'shade', 'b', 1.0), strand([(70, 60), (60, 20)], 'shade', 'b', 1.0),
             L(outline([(-10, 100), (14, 84), (50, 92), (86, 84), (110, 100), (108, 128), (-8, 128)]), 'scarf', 'f', ln=True),
             L(outline([(56, 92), (86, 86), (108, 102), (106, 124), (64, 122)]), 'scarf_d', 'f', False)],
}

# Yukinori Kameda (Dean Rush): adulto de cara alargada, con el pelo azul marino corto y de punta arriba, orejas grandes, nariz
# grande y ojos redondos saltones
CHARS['dean-rush'] = {
    'body': 'delgado', 'pal': pal('#24344e', '#e8a87c', iris='#1e1414', shade='#18243a', nose='#d8946a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 102, 'hairline': [(14, 60), (16, 40), (34, 30), (50, 36), (66, 30), (84, 40), (86, 60)],
             'big_ears': 3, 'ear_out': 4, 'nose': (50, 86, 4),
             'face_front': outline([(14, 50), (18, 26), (50, 20), (82, 26), (86, 50), (84, 92), (70, 112), (50, 118), (30, 112), (16, 92)])},
    'front': [L(outline([(14, 60), (12, 26), (18, 6), (30, 0), (36, -10, 1), (44, 0), (50, -14, 1), (56, 0), (66, -8, 1), (70, 2), (82, 8), (88, 26), (86, 60),
                         (84, 40), (16, 40)])),
              L(outline([(60, 0), (82, 10), (88, 30), (86, 56), (76, 34)]), 'shade', 'b', False)],
    'side': [L(outline([(56, 50), (62, 38), (78, 34), (90, 22), (88, 4), (96, -4, 1), (74, -2), (68, -14, 1), (54, -2), (40, -14, 1), (34, 0), (14, 4), (4, 30),
                        (4, 64), (16, 80), (30, 76), (42, 60)])),
             L(outline([(4, 30), (24, 34), (26, 70), (8, 64)]), 'shade', 'b', False),
             L(outline([(90, 74), (106, 90), (92, 94)]), 'nose', 'f', ln=True)],
    'back': [L(outline([(14, 82), (10, 30), (18, 8), (32, 0), (38, -10, 1), (46, 0), (54, -12, 1), (60, 0), (70, -8, 1), (74, 4), (84, 10), (90, 30), (86, 82),
                        (50, 88)])),
             L(outline([(56, 2), (84, 12), (90, 40), (86, 78), (64, 84)]), 'shade', 'b', False)],
}

# Anna Mikado (Regina Mulgrave, portera): melena larga lisa melocotón hasta la espalda, con flequillo de mechones finos que
# le cae sobre las cejas y dos mechones largos junto a la cara; ojos grandes azules
CHARS['regina-mulgrave'] = {
    'body': 'chica', 'pal': pal('#f6b48a', '#fce0cc', iris='#2a7ac8', shade='#d88a6a', deep='#b86a50', light='#ffd4b8'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(4, 120), (-2, 80), (2, 36), (16, 8), (50, -4), (84, 8), (98, 36), (102, 80), (96, 120), (84, 112), (84, 60), (16, 60), (16, 112)])),
              L(outline([(60, 0), (88, 12), (100, 44), (100, 114), (88, 110), (82, 50)]), 'shade', 'b', False),
              L(outline([(12, 60), (6, 110), (12, 124, 1), (20, 104), (20, 64)]), 'mid', 'f'), L(outline([(88, 60), (94, 110), (88, 124, 1), (80, 104), (80, 64)]), 'mid', 'f'),
              fringe([(10, 66), (8, 40), (22, 16), (50, 8), (78, 16), (92, 40), (90, 66), (84, 54), (80, 64, 1), (74, 50), (66, 62, 1), (62, 48), (56, 64, 1),
                      (50, 48), (44, 64, 1), (38, 48), (34, 62, 1), (26, 50), (20, 64, 1), (16, 54)]),
              L(outline([(24, 16), (46, 10), (34, 24)]), 'light', 'f', False)],
    'side': [L(outline([(52, 78), (56, 60), (78, 56), (92, 40), (90, 14), (66, -2), (34, -2), (10, 14), (-2, 44), (-8, 90), (-6, 124, 1), (10, 112), (24, 124, 1),
                        (36, 108), (46, 96)])),
             L(outline([(-2, 44), (24, 48), (30, 110), (0, 116)]), 'shade', 'b', False),
             fringe([(62, 2), (90, 16), (96, 42), (94, 64, 1), (86, 50), (84, 108, 1), (76, 60), (70, 40)])],
    'back': [L(outline([(2, 120), (-2, 80), (2, 36), (16, 8), (50, -4), (84, 8), (98, 36), (102, 80), (98, 120), (84, 128, 1), (70, 120), (50, 130, 1), (30, 120),
                        (16, 128, 1)])),
             L(outline([(56, 0), (86, 10), (100, 44), (100, 120), (66, 124), (70, 50)]), 'shade', 'b', False),
             strand([(30, 30), (24, 80), (28, 120)], 'shade', 'b', 1.0), strand([(70, 30), (76, 80), (72, 120)], 'shade', 'b', 1.0)],
}

# Tsukushi Ootani (Aurelia Dingle): pelo castaño con raya al lado y un flequillo que cruza la frente, recogido en una coleta
# baja con un lazo lila; ojos grandes castaños y sonrisa
CHARS['aurelia-dingle'] = {
    'body': 'chica', 'pal': pal('#7a5a30', '#fcdcc0', iris='#8a4a1a', shade='#5e4424', light='#9a7a4c', bow='#a090d0'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 86), (6, 50), (12, 18), (34, 2), (50, 0), (66, 2), (88, 18), (94, 50), (88, 86), (84, 60), (16, 60)])),
              L(outline([(60, 2), (84, 14), (94, 46), (88, 80), (80, 50)]), 'shade', 'b', False),
              fringe([(10, 70), (10, 40), (22, 16), (44, 8), (68, 12), (86, 28), (90, 58), (82, 46), (70, 34), (54, 28), (40, 40), (30, 54), (20, 70)]),
              L(outline([(28, 16), (48, 10), (40, 20)]), 'light', 'f', False)],
    'side': [L(outline([(54, 64), (58, 50), (80, 48), (92, 32), (86, 10), (64, -2), (36, 0), (14, 12), (4, 38), (6, 66), (20, 80), (36, 80), (46, 72)])),
             L(outline([(18, 62), (4, 72), (-4, 96), (0, 110, 1), (10, 96), (16, 80), (26, 70)])),
             L(ell(20, 66, 4, 3), 'bow', 'f', ln=True),
             L(outline([(4, 38), (26, 42), (30, 74), (10, 72)]), 'shade', 'b', False),
             fringe([(62, 2), (88, 16), (94, 40), (90, 60, 1), (84, 46), (76, 36)])],
    'back': [L(outline([(12, 80), (6, 50), (12, 18), (34, 2), (50, 0), (66, 2), (88, 18), (94, 50), (88, 80), (66, 88), (34, 88)])),
             L(outline([(56, 2), (84, 14), (94, 50), (88, 78), (64, 86)]), 'shade', 'b', False),
             L(outline([(40, 70), (60, 70), (62, 90), (56, 112, 1), (50, 98), (44, 112, 1), (38, 90)]), 'mid', 'f', ln=True),
             L(outline([(40, 70), (32, 64), (32, 76)]), 'bow', 'f', ln=True), L(outline([(60, 70), (68, 64), (68, 76)]), 'bow', 'f', ln=True),
             L(ell(50, 70, 3, 2.6), 'bow', 'f', ln=True),
             strand([(50, 4), (50, 60)], 'shade', 'b', 1.0)],
}
