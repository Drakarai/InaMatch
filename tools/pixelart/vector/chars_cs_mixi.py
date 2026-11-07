"""Chrono Storm (cs-chrono-storm): los once definitivos, todos con su Mixi Max (wiki: Kirino_MM, Tenma_MMArthur, Shindou_MM,
Tsurugi_MM, Fei_MMBig, Nishiki_MMSakamoto, Amemiya_MM, Hakuryuu_MM, Shinsuke_MM, Torb_MM, Kinako_MM, Zanark_MMClaraJ).
Referencias: sus modelos 3D de Chrono Stone en la enciclopedia, comprobados con los sprites '(TR) <nombre> sprite (MM...)' de
la wiki. Se carga después de los demás módulos de Chrono Stone (usa los Mixi Max ya dibujados para el Raimon de CS)."""
from chars import CHARS, L, OUTC, ell, outline, pal, rope, strand
from heads import quad

T = 'cs-chrono-storm'
WHITE = (246, 246, 246, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Fei (Mixi Max con Big: el azul de pinchos) y Amemiya (con Kongming: la melena lila), los mismos que en el Raimon de CS
CHARS[f'{T}:fei-rune'] = CHARS['cs-team-raimon:fei-rune-cs-fei-mmbig']
CHARS[f'{T}:sol-daystar'] = CHARS['cs-team-raimon:sol-daystar-cs-amemiya-mm']

# Shinsuke con Mixi Max: pelo azul de pinchos largos hacia arriba y a los lados, con una cinta blanca rosada ancha en la
# frente; carita redonda con coloretes y cejas fruncidas
CHARS[f'{T}:jean-pierre-lapin'] = {
    'body': 'bajito', 'pal': pal('#3a66c0', '#fcd8b4', iris='#3a2418', band='#ecdcdc', band_d='#b8a8ac', blush='#f4a8a0'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 64), (6, 48), (-8, 42, 1), (6, 30), (0, 6, 1), (20, 12), (26, -12, 1), (40, 2), (54, -20, 1), (60, 2), (80, -14, 1), (82, 8),
                         (104, 4, 1), (92, 26), (110, 34, 1), (94, 46), (86, 64), (80, 52), (20, 52)])),
              L(outline([(60, 0), (84, 10), (94, 40), (86, 60), (76, 36)]), 'shade', 'b', False),
              L(outline([(40, 4), (50, 0), (46, 24)]), 'light', 'b', False),
              L(outline([(10, 52), (8, 32), (50, 26), (92, 32), (90, 52), (50, 48)]), 'band', 'f', ln=True),
              L(outline([(60, 30), (90, 34), (88, 50), (62, 48)]), 'band_d', 'f', False),
              fringe([(30, 50), (36, 64, 1), (42, 52), (50, 70, 1), (56, 52), (64, 62, 1), (70, 50)]),
              L(ell(30, 90, 4.4, 2.4), 'blush', 'f', False), L(ell(70, 90, 4.4, 2.4), 'blush', 'f', False)],
    'side': [L(outline([(54, 56), (62, 44), (82, 40), (92, 26), (100, 8, 1), (78, 10), (74, -14, 1), (58, 0), (42, -20, 1), (32, 4), (8, -6, 1), (12, 14),
                        (-10, 22, 1), (4, 34), (-12, 50, 1), (6, 56), (2, 76, 1), (18, 72), (24, 86, 1), (36, 74), (46, 66)])),
             L(outline([(2, 34), (24, 40), (24, 70), (6, 62)]), 'shade', 'b', False),
             L(outline([(4, 50), (6, 30), (50, 22), (96, 30), (96, 48), (50, 46)]), 'band', 'f', ln=True),
             L(ell(86, 88, 4, 2.4), 'blush', 'f', False)],
    'back': [L(outline([(14, 80), (2, 66, 1), (8, 50), (-8, 40, 1), (6, 30), (0, 6, 1), (20, 12), (26, -12, 1), (40, 2), (54, -20, 1), (60, 2), (80, -14, 1),
                        (82, 8), (104, 4, 1), (92, 26), (110, 36, 1), (94, 50), (100, 66, 1), (86, 80), (60, 84), (50, 96, 1), (40, 84)])),
             L(outline([(56, 4), (84, 12), (94, 44), (86, 78), (62, 82)]), 'shade', 'b', False),
             L(outline([(10, 54), (8, 34), (50, 28), (92, 34), (90, 54), (50, 50)]), 'band', 'f', ln=True)],
}

# Kirino con Mixi Max (Juana de Arco): melena rubia muy clara, lisa, con flequillo de mechones abierto en medio y las dos
# coletas bajas atadas con gomas negras que salen abiertas hacia los lados; gafas finas negras y ojos verdes
CHARS[f'{T}:gabriel-garcia'] = {
    'body': 'delgado', 'pal': pal('#eccb84', '#fce0c8', iris='#2a9a7a', shade='#c8a464', band='#2a2a2e'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False, 'glasses': OUTC, 'glasses_rect': True},
    'front': [L(outline([(12, 84), (6, 50), (8, 22), (26, 4), (50, -2), (74, 4), (92, 22), (98, 40), (108, 30, 1), (96, 52), (90, 84), (82, 62), (18, 62)])),
              L(outline([(60, 2), (86, 14), (96, 42), (88, 78), (80, 48)]), 'shade', 'b', False),
              L(outline([(14, 84), (-6, 92), (-30, 112, 1), (-10, 96), (-24, 106, 1), (-2, 86), (10, 76)]), 'mid', 'b'),
              L(outline([(86, 84), (106, 92), (130, 112, 1), (110, 96), (124, 106, 1), (102, 86), (90, 76)]), 'mid', 'b'),
              L(ell(10, 82, 3.6, 3.2), 'band', 'f', ln=True), L(ell(90, 82, 3.6, 3.2), 'band', 'f', ln=True),
              fringe([(10, 76), (10, 44), (24, 20), (48, 12), (52, 30), (54, 12), (76, 20), (90, 44), (90, 76), (84, 62), (78, 72, 1), (70, 50), (60, 64, 1),
                      (54, 40), (50, 74, 1), (46, 40), (40, 64, 1), (30, 50), (22, 72, 1), (16, 62)])],
    'side': [L(outline([(52, 70), (56, 56), (80, 52), (94, 38), (90, 16), (68, 0), (40, -2), (16, 10), (4, 34), (4, 62), (14, 80), (32, 84)])),
             L(outline([(16, 74), (0, 86), (-28, 100), (-40, 112, 1), (-18, 104), (-34, 118, 1), (-6, 104), (12, 92), (26, 82)]), 'mid', 'b'),
             L(ell(18, 78, 4, 4), 'band', 'b', ln=True),
             L(outline([(6, 40), (28, 46), (30, 76), (12, 72)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 16), (96, 40), (92, 66, 1), (86, 50), (80, 62, 1), (76, 42), (64, 30)])],
    'back': [L(outline([(12, 76), (6, 50), (8, 22), (26, 4), (50, -2), (74, 4), (92, 22), (94, 50), (88, 76), (70, 88), (30, 88)])),
             L(outline([(56, 2), (86, 14), (94, 46), (88, 74), (64, 86)]), 'shade', 'b', False),
             L(outline([(30, 86), (10, 96), (-20, 112, 1), (2, 98), (-10, 112, 1), (18, 96), (34, 92)]), 'mid', 'f'),
             L(outline([(70, 86), (90, 96), (120, 112, 1), (98, 98), (110, 112, 1), (82, 96), (66, 92)]), 'mid', 'f'),
             L(ell(32, 88, 4, 3.4), 'band', 'f', ln=True), L(ell(68, 88, 4, 3.4), 'band', 'f', ln=True),
             strand([(50, 2), (50, 84)], 'shade', 'b', 1.2)],
}

# Torb con Mixi Max: pelo rojo encendido de plumas en punta abiertas hacia arriba y a los lados (como un penacho), con una
# máscara dorada de pico de ave encima de la frente; ojos redondos y sonrisa enorme de dientes en sierra
_torb_teeth = [L(outline([(32, 92), (68, 92), (62, 106), (50, 110), (38, 106)]), (120, 30, 30, 255), 'f', ln=True),
               L([(34, 93), (38, 98), (42, 93), (46, 98), (50, 93), (54, 98), (58, 93), (62, 98), (66, 93)], WHITE, 'f', False, False, 2.2)]
CHARS[f'{T}:sor'] = {
    'body': 'normal', 'pal': pal('#d8241e', '#f2c49a', iris='#1e1414', shade='#a81a16', gold='#e8b030', gold_d='#b88418'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'none', 'hairline': False},
    'front': [L(outline([(14, 74), (-10, 80, 1), (4, 62), (-24, 46, 1), (2, 40), (-12, 10, 1), (16, 20), (14, -14, 1), (32, 6), (40, -30, 1), (50, 2), (60, -30, 1),
                         (68, 6), (86, -14, 1), (84, 20), (112, 10, 1), (98, 40), (124, 46, 1), (96, 62), (110, 80, 1), (86, 74), (84, 56), (16, 56)])),
              L(outline([(62, 0), (86, -10), (84, 20), (100, 40), (90, 64), (78, 40)]), 'shade', 'b', False),
              fringe([(14, 64), (16, 48), (30, 42), (40, 54, 1), (46, 44), (54, 44), (60, 54, 1), (70, 42), (84, 48), (86, 64), (76, 56), (68, 64, 1), (60, 56),
                      (40, 56), (32, 64, 1), (24, 56)]),
              L(outline([(24, 30), (30, 10), (50, 2), (70, 10), (76, 30), (62, 34), (56, 54), (50, 64, 1), (44, 54), (38, 34)]), 'gold', 'f', ln=True),
              L(outline([(50, 4), (70, 10), (76, 30), (62, 34), (54, 52)]), 'gold_d', 'f', False),
              L(outline([(40, 22), (46, 20), (46, 28), (40, 28)]), OUTC, 'f', False), L(outline([(54, 20), (60, 22), (60, 28), (54, 28)]), OUTC, 'f', False)]
             + _torb_teeth,
    'side': [L(outline([(54, 60), (60, 48), (76, 46), (88, 34), (96, 18), (84, 10), (90, -10, 1), (70, 0), (60, -30, 1), (46, -2), (24, -24, 1), (24, 4),
                        (-16, 0, 1), (8, 20), (-24, 34, 1), (4, 42), (-18, 60, 1), (6, 64), (-4, 84, 1), (20, 76), (26, 92, 1), (38, 76), (46, 70)])),
             L(outline([(2, 34), (24, 40), (26, 70), (6, 62)]), 'shade', 'b', False),
             L(outline([(64, 6), (86, 10), (102, 26), (112, 52, 1), (96, 40), (88, 38), (72, 30)]), 'gold', 'f', ln=True),
             L(outline([(80, 92), (94, 90), (92, 102), (82, 104)]), (120, 30, 30, 255), 'f', ln=True)],
    'back': [L(outline([(14, 84), (-12, 88, 1), (4, 66), (-24, 50, 1), (2, 42), (-12, 10, 1), (16, 20), (14, -14, 1), (32, 6), (40, -30, 1), (50, 2), (60, -30, 1),
                        (68, 6), (86, -14, 1), (84, 20), (112, 10, 1), (98, 42), (124, 50, 1), (96, 66), (112, 88, 1), (86, 84), (68, 96, 1), (60, 84), (50, 100, 1),
                        (40, 84), (32, 96, 1)])),
             L(outline([(56, 0), (86, -10), (84, 20), (100, 46), (88, 82), (64, 86)]), 'shade', 'b', False),
             L(outline([(28, 22), (50, 16), (72, 22), (70, 30), (50, 26), (30, 30)]), 'gold', 'f', ln=True)],
}

# Kinako con Mixi Max: melena rubia larguísima con flequillo recto y una diadema gris, que se abre por los lados y por
# detrás en grandes mechones curvados hacia fuera, como tentáculos; ojos azules
CHARS[f'{T}:goldie-lemmon'] = {
    'body': 'chica', 'pal': pal('#eccf7e', '#fce0c8', iris='#2a7ab8', shade='#c8aa5e', band='#8a8e98'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(14, 70), (-6, 60), (-26, 30, 1), (-14, 64), (-30, 86, 1), (-4, 92), (-26, 122, 1), (8, 106), (14, 128, 1), (24, 100), (24, 70),
                         (76, 70), (76, 100), (86, 128, 1), (92, 106), (126, 122, 1), (104, 92), (130, 86, 1), (114, 64), (126, 30, 1), (106, 60), (86, 70),
                         (94, 36), (82, 10), (50, 0), (18, 10), (6, 36)])),
              L(outline([(60, 2), (86, 14), (96, 42), (112, 64), (104, 90), (84, 70)]), 'shade', 'b', False),
              fringe([(12, 66), (12, 40), (24, 18), (50, 10), (76, 18), (88, 40), (88, 66), (80, 58), (76, 60), (72, 56), (60, 60), (50, 56), (40, 60), (28, 56),
                      (24, 60), (20, 58)]),
              L(quad((14, 30), (50, 4), (86, 30)), 'band', 'f', False, False, 3.4)],
    'side': [L(outline([(52, 70), (56, 56), (78, 52), (92, 38), (88, 14), (66, -2), (36, -2), (14, 12), (4, 36), (-14, 30, 1), (-6, 56), (-30, 70, 1), (-8, 82),
                        (-26, 112, 1), (2, 100), (6, 128, 1), (20, 104), (30, 124, 1), (38, 96), (46, 82)])),
             L(outline([(4, 40), (26, 48), (30, 92), (8, 88)]), 'shade', 'b', False),
             fringe([(60, 4), (86, 16), (94, 40), (92, 60, 1), (84, 48), (78, 40)]),
             L(quad((30, 6), (60, -2), (86, 18)), 'band', 'f', False, False, 3.4)],
    'back': [L(outline([(10, 70), (-10, 56), (-30, 26, 1), (-18, 64), (-32, 92, 1), (-6, 96), (-24, 128, 1), (10, 112), (24, 134, 1), (36, 112), (50, 132, 1),
                        (64, 112), (76, 134, 1), (90, 112), (124, 128, 1), (106, 96), (132, 92, 1), (118, 64), (130, 26, 1), (110, 56), (90, 70), (94, 36),
                        (82, 10), (50, 0), (18, 10), (6, 36)])),
             L(outline([(56, 2), (86, 14), (96, 46), (114, 64), (110, 96), (80, 110), (70, 60)]), 'shade', 'b', False),
             strand([(50, 4), (50, 110)], 'shade', 'b', 1.2), L(quad((14, 30), (50, 4), (86, 30)), 'band', 'f', False, False, 3.4)],
}

# Tenma con Mixi Max (Arturo): melena dorada de león, con pinchos grandes hacia arriba, dos rizos enrollados a los lados de
# lo alto y mechones largos que le caen por los lados y por detrás hasta los hombros; ojos grandes gris azulado
CHARS[f'{T}:arion-sherwind'] = {
    'body': 'normal', 'pal': pal('#ecd07a', '#fcdcbc', iris='#5a7090', shade='#c8a858', deep='#a88a40'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(14, 70), (2, 94), (-12, 108, 1), (6, 104), (18, 112, 1), (22, 86), (24, 70), (76, 70), (78, 86), (82, 112, 1), (94, 104), (112, 108, 1),
                         (98, 94), (86, 70), (94, 40), (106, 26), (96, 6), (84, 10), (76, -14, 1), (60, 0), (50, -20, 1), (40, 0), (24, -14, 1), (16, 10), (4, 6),
                         (-6, 26), (6, 40)])),
              L(outline([(60, 0), (84, 10), (96, 40), (90, 90), (80, 60)]), 'shade', 'b', False),
              L(ell(4, 22, 9, 8), 'mid', 'b', ln=True), L(ell(96, 22, 9, 8), 'mid', 'b', ln=True),
              L(ell(4, 22, 4, 3.6) + [ell(4, 22, 4, 3.6)[0]], 'deep', 'b', False, False, 1.4), L(ell(96, 22, 4, 3.6) + [ell(96, 22, 4, 3.6)[0]], 'deep', 'b', False, False, 1.4),
              fringe([(12, 66), (14, 42), (28, 24), (50, 16), (72, 24), (86, 42), (88, 66), (80, 52), (72, 60, 1), (64, 44), (54, 54, 1), (50, 40), (46, 54, 1),
                      (36, 44), (28, 60, 1), (20, 52)]),
              strand([(30, 28), (24, 50)], 'shade', 'f', 1.0), strand([(70, 28), (76, 50)], 'shade', 'f', 1.0)],
    'side': [L(outline([(54, 62), (60, 48), (82, 48), (94, 36), (90, 16), (96, 0, 1), (76, 4), (66, -16, 1), (52, 0), (34, -14, 1), (24, 6), (6, 12), (-6, 40),
                        (-10, 70), (-4, 96), (-18, 112, 1), (6, 104), (16, 116, 1), (26, 98), (40, 84), (46, 70)])),
             L(ell(52, 14, 9, 8), 'mid', 'b', ln=True), L(ell(52, 14, 4, 3.6) + [ell(52, 14, 4, 3.6)[0]], 'deep', 'b', False, False, 1.4),
             L(outline([(-4, 40), (20, 46), (26, 96), (2, 92)]), 'shade', 'b', False),
             strand([(4, 50), (8, 90)], 'deep', 'b', 1.0), strand([(18, 40), (24, 86)], 'deep', 'b', 1.0),
             fringe([(66, 4), (90, 18), (96, 42), (94, 64, 1), (86, 50), (80, 60, 1), (76, 42), (66, 30)])],
    'back': [L(outline([(10, 92), (-8, 106, 1), (2, 76), (-6, 40), (4, 6), (16, 10), (24, -14, 1), (40, 0), (50, -20, 1), (60, 0), (76, -14, 1), (84, 10), (96, 6),
                        (106, 40), (98, 76), (108, 106, 1), (90, 92), (76, 108, 1), (64, 94), (50, 110, 1), (36, 94), (24, 108, 1)])),
             L(outline([(56, 0), (84, 10), (100, 46), (94, 96), (64, 100)]), 'shade', 'b', False),
             L(ell(4, 22, 9, 8), 'mid', 'b', ln=True), L(ell(96, 22, 9, 8), 'mid', 'b', ln=True),
             strand([(30, 20), (24, 60), (30, 96)], 'deep', 'b', 1.0), strand([(50, 10), (50, 100)], 'deep', 'b', 1.0), strand([(70, 20), (76, 60), (70, 96)], 'deep', 'b', 1.0)],
}

# Shindou con Mixi Max (Nobunaga): pelo granate oscuro con un moño alto atado con una cinta blanca del que sale un mechón
# ondeando, mechones de punta a los lados y unos mechones finos que se rizan hacia fuera a la altura de la boca; ojos rojos
CHARS[f'{T}:riccardo-di-rigo'] = {
    'body': 'normal', 'pal': pal('#7a4234', '#fcdcc0', iris='#c81e1e', shade='#5e3026', tie='#ece8e0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(42, 6), (40, -14), (30, -30), (44, -22), (52, -40, 1), (58, -20), (76, -30, 1), (66, -12), (58, 6)])),
              L(outline([(42, -4), (58, -4), (58, 2), (42, 2)]), 'tie', 'f', ln=True),
              L(outline([(16, 90), (12, 66), (2, 74), (-12, 70, 1), (4, 62), (8, 40), (4, 14, 1), (22, 18), (36, 4), (64, 4), (78, 18), (96, 14, 1), (92, 40),
                         (96, 62), (112, 70, 1), (98, 74), (88, 66), (84, 90), (78, 64), (22, 64)])),
              L(outline([(60, 6), (84, 18), (92, 46), (86, 84), (78, 50)]), 'shade', 'b', False),
              L(quad((10, 82), (-6, 90), (-14, 82)), 'mid', 'f', False, False, 2.4), L(quad((90, 82), (106, 90), (114, 82)), 'mid', 'f', False, False, 2.4),
              fringe([(12, 70), (14, 42), (28, 24), (50, 18), (72, 24), (86, 42), (88, 70), (80, 56), (72, 64, 1), (64, 46), (56, 58, 1), (52, 42), (48, 76, 1),
                      (42, 46), (34, 60, 1), (28, 48), (20, 64, 1)])],
    'side': [L(outline([(40, 6), (30, -16), (14, -34), (30, -28), (40, -44, 1), (46, -20), (60, -16), (54, 4)])),
             L(outline([(34, -6), (50, -10), (52, -2), (36, 2)]), 'tie', 'f', ln=True),
             L(outline([(54, 64), (58, 50), (80, 50), (94, 36), (90, 14), (70, 0), (40, 0), (16, 12), (2, 36), (-12, 28, 1), (-2, 52), (2, 76), (-14, 90, 1),
                        (10, 86), (24, 98, 1), (34, 82), (46, 74)])),
             L(outline([(4, 40), (26, 46), (30, 82), (10, 80)]), 'shade', 'b', False),
             fringe([(64, 4), (88, 16), (96, 40), (94, 66, 1), (86, 50), (80, 62, 1), (76, 42), (64, 30)])],
    'back': [L(outline([(42, 8), (40, -14), (30, -30), (44, -22), (52, -40, 1), (58, -20), (76, -30, 1), (66, -12), (58, 8)])),
             L(outline([(42, -4), (58, -4), (58, 2), (42, 2)]), 'tie', 'f', ln=True),
             L(outline([(16, 92), (-2, 92, 1), (8, 76), (-10, 68, 1), (6, 58), (2, 30), (-2, 10, 1), (18, 14), (36, 4), (64, 4), (82, 14), (102, 10, 1), (98, 30),
                        (94, 58), (110, 68, 1), (92, 76), (102, 92, 1), (84, 92), (70, 100, 1), (60, 90), (50, 102, 1), (40, 90), (30, 100, 1)])),
             L(outline([(56, 6), (84, 16), (96, 50), (88, 88), (64, 92)]), 'shade', 'b', False)],
}

# Nishiki con Mixi Max (Sakamoto Ryouma): piel morena, pelo azul marino con un tupé alto en punta peinado hacia arriba y
# mechones ondulados como cintas que se abren hacia los lados a la altura de las orejas; ojos verde azulado y sonrisa
_nk_tails = [L(rope((16, 64), (-2, 50), (-20, 62), 8)), L(rope((14, 80), (-8, 90), (-20, 104), 7)),
             L(rope((84, 64), (102, 50), (120, 62), 8)), L(rope((86, 80), (108, 90), (120, 104), 7))]
CHARS[f'{T}:ryoma-nishiki'] = {
    'body': 'normal', 'pal': pal('#1e3c7a', '#c08a5a', iris='#2a8a8a', shade='#162c5a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': _nk_tails + [L(outline([(16, 66), (12, 36), (24, 14), (34, 2), (32, -14), (42, -30), (56, -32, 1), (64, -18), (64, 2), (76, 14), (88, 36), (84, 66), (78, 52), (22, 52)])),
                          L(outline([(54, -24), (62, -10), (66, 6), (80, 18), (88, 40), (82, 60), (72, 30)]), 'shade', 'b', False),
                          fringe([(14, 60), (16, 38), (30, 24), (50, 20), (70, 24), (84, 38), (86, 60), (78, 48), (72, 56, 1), (66, 42), (58, 52, 1), (50, 40),
                                  (42, 52, 1), (34, 42), (28, 56, 1), (22, 48)])],
    'side': [L(rope((22, 66), (0, 56), (-18, 72), 7)), L(rope((20, 80), (0, 86), (-18, 102), 7)),
             L(outline([(54, 58), (60, 46), (82, 46), (92, 32), (86, 12), (70, 2), (60, -18), (48, -38, 1), (36, -18), (20, 0), (8, 22), (6, 52), (18, 74), (34, 72),
                        (46, 64)])),
             L(outline([(8, 30), (28, 36), (28, 64), (12, 58)]), 'shade', 'b', False),
             fringe([(66, 4), (88, 16), (94, 38), (90, 54, 1), (84, 40), (76, 30)])],
    'back': _nk_tails + [L(outline([(16, 78), (12, 36), (24, 14), (34, 2), (32, -14), (42, -30), (56, -32, 1), (64, -18), (64, 2), (76, 14), (88, 36), (84, 78), (50, 86)])),
                         L(outline([(54, -24), (62, -10), (66, 6), (80, 18), (90, 46), (84, 74), (62, 84)]), 'shade', 'b', False)],
}

# Hakuryuu con Mixi Max (Kongming): pelo blanco lila de pinchos de punta hacia arriba y a los lados, con la capa de debajo
# morado oscuro y una coleta baja morada en la nuca; ojos rojizos
CHARS[f'{T}:bailong'] = {
    'body': 'normal', 'pal': pal('#e6def0', '#fcdcc0', iris='#a8341e', shade='#b8aac8', under='#5a3a6a', under_d='#3e2850'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 84), (8, 64), (6, 40), (90, 40), (94, 64), (84, 84), (80, 64), (20, 64)]), 'under'),
              L(outline([(14, 60), (-6, 52, 1), (8, 40), (-10, 20, 1), (14, 18), (14, -6, 1), (30, 8), (38, -18, 1), (50, 4), (62, -18, 1), (70, 8), (86, -6, 1),
                         (86, 18), (110, 20, 1), (92, 40), (106, 52, 1), (86, 60), (80, 46), (20, 46)])),
              L(outline([(60, 2), (86, 12), (94, 36), (86, 54), (76, 34)]), 'shade', 'b', False),
              fringe([(12, 70), (14, 42), (28, 24), (50, 18), (72, 24), (86, 42), (88, 70), (80, 56), (74, 64, 1), (66, 46), (58, 58, 1), (52, 42), (48, 74, 1),
                      (42, 46), (34, 60, 1), (28, 48), (20, 66, 1)])],
    'side': [L(outline([(30, 70), (14, 88), (-8, 100, 1), (8, 82), (20, 66)]), 'under'),
             L(outline([(54, 62), (58, 50), (80, 50), (92, 36), (40, 30), (8, 40), (4, 66), (16, 84), (34, 82), (46, 72)]), 'under'),
             L(outline([(92, 36), (96, 20), (106, 8, 1), (84, 6), (76, -14, 1), (60, 0), (42, -20, 1), (32, 2), (6, -8, 1), (12, 16), (-14, 22, 1), (4, 36), (40, 40)])),
             L(outline([(6, 30), (40, 34), (30, 24), (10, 20)]), 'shade', 'b', False),
             fringe([(66, 4), (90, 18), (96, 42), (94, 66, 1), (86, 50), (80, 62, 1), (76, 42), (66, 30)])],
    'back': [L(outline([(16, 84), (8, 60), (8, 38), (92, 38), (92, 60), (84, 84), (60, 92), (40, 92)]), 'under'),
             L(outline([(56, 40), (90, 40), (90, 60), (82, 82), (62, 90)]), 'under_d', 'b', False),
             L(outline([(42, 84), (58, 84), (60, 110), (50, 120, 1), (40, 110)]), 'under', 'f', ln=True),
             L(outline([(12, 50), (-8, 46, 1), (8, 34), (-10, 18, 1), (14, 16), (14, -6, 1), (30, 8), (38, -18, 1), (50, 4), (62, -18, 1), (70, 8), (86, -6, 1),
                        (86, 16), (110, 18, 1), (92, 34), (108, 46, 1), (88, 50), (70, 44), (50, 52, 1), (30, 44)])),
             L(outline([(56, 4), (86, 12), (96, 34), (86, 48), (70, 40)]), 'shade', 'b', False)],
}

# Tsurugi con Mixi Max (Okita Souji): piel morena, pelo morado intenso abultado y peinado hacia atrás, con los dos rizos en
# espiral de siempre junto a las orejas; ojos ámbar afilados y media sonrisa
_ts_spiral = [L(ell(13, 82, 3.6, 3.6) + [ell(13, 82, 3.6, 3.6)[0]], 'mid', 'f', False, False, 2.2), L(ell(87, 82, 3.6, 3.6) + [ell(87, 82, 3.6, 3.6)[0]], 'mid', 'f', False, False, 2.2),
              L([(14, 64), (12, 78)], 'mid', 'f', False, False, 2.4), L([(86, 64), (88, 78)], 'mid', 'f', False, False, 2.4)]
CHARS[f'{T}:victor-blade'] = {
    'body': 'normal', 'pal': pal('#4a22a0', '#c89060', iris='#d89a2a', shade='#341878'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 66), (8, 44), (8, 20), (16, 4), (14, -12, 1), (30, -6), (40, -22, 1), (52, -10), (66, -20, 1), (72, -4), (88, -8, 1), (90, 14),
                         (94, 40), (86, 66), (80, 52), (20, 52)])),
              L(outline([(58, -10), (84, -2), (92, 36), (86, 60), (76, 34)]), 'shade', 'b', False),
              fringe([(14, 58), (16, 36), (28, 18), (50, 10), (72, 18), (84, 36), (86, 58), (76, 44), (64, 36), (54, 50, 1), (48, 34), (36, 40), (24, 54, 1)])]
             + _ts_spiral,
    'side': [L(outline([(54, 58), (60, 46), (82, 46), (92, 32), (90, 10), (80, -6), (62, -16), (38, -16), (14, -8), (-4, 8), (-14, 4, 1), (-6, 22), (2, 52), (16, 72),
                        (34, 70), (46, 64)])),
             L(outline([(4, 26), (24, 32), (26, 64), (10, 56)]), 'shade', 'b', False),
             fringe([(68, 2), (90, 18), (94, 40), (90, 54, 1), (84, 40), (76, 30)]),
             L(ell(56, 82, 4, 4) + [ell(56, 82, 4, 4)[0]], 'mid', 'f', False, False, 2.2), L([(54, 64), (56, 78)], 'mid', 'f', False, False, 2.4)],
    'back': [L(outline([(16, 80), (8, 50), (8, 20), (16, 2), (14, -12, 1), (30, -6), (40, -22, 1), (52, -10), (66, -20, 1), (72, -4), (88, -8, 1), (90, 14), (94, 50),
                        (86, 80), (66, 90), (50, 100, 1), (34, 90)])),
             L(outline([(56, -10), (84, -2), (94, 40), (86, 76), (60, 88)]), 'shade', 'b', False),
             strand([(30, 10), (36, 50), (30, 80)], 'deep', 'b', 1.0), strand([(70, 10), (64, 50), (70, 80)], 'deep', 'b', 1.0)] + _ts_spiral,
}

# Zanark con Mixi Max (Clara Jane): piel oscura, pelo verde azulado muy oscuro de pinchos hacia arriba que le cae largo y
# liso por los lados hasta el pecho, orejas puntiagudas de elfo y ojos amarillos
CHARS[f'{T}:zanark-avalonic'] = {
    'body': 'normal', 'pal': pal('#124a52', '#9a6040', iris='#e0b020', shade='#0c343a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False, 'ears': False},
    'front': [L(outline([(14, 70), (-6, 62, 1), (12, 60)]), 'skin', 'b', ln=True), L(outline([(86, 70), (106, 62, 1), (88, 60)]), 'skin', 'b', ln=True),
              L(outline([(18, 120), (8, 96), (8, 66), (6, 40), (0, 20, 1), (16, 22), (18, 0, 1), (30, 12), (40, -14, 1), (50, 6), (62, -20, 1), (68, 6), (84, -4, 1),
                         (84, 18), (100, 20, 1), (94, 40), (92, 66), (92, 96), (82, 120), (80, 70), (20, 70)])),
              L(outline([(60, 4), (86, 16), (94, 50), (86, 112), (82, 70)]), 'shade', 'b', False),
              fringe([(12, 76), (14, 44), (28, 26), (50, 20), (72, 26), (86, 44), (88, 76), (80, 60), (72, 70, 1), (64, 50), (56, 62, 1), (52, 44), (48, 80, 1),
                      (42, 48), (34, 64, 1), (28, 52), (20, 72, 1)])],
    'side': [L(outline([(54, 64), (58, 50), (80, 48), (92, 34), (94, 14), (104, 2, 1), (80, 4), (72, -18, 1), (56, -2), (32, -16, 1), (24, 6), (0, 4, 1), (10, 22),
                        (2, 50), (6, 90), (12, 124, 1), (22, 100), (30, 120, 1), (34, 92), (46, 76)])),
             L(outline([(46, 64), (56, 72), (40, 58, 1)]), 'skin', 'f', ln=True),
             L(outline([(6, 34), (26, 40), (30, 96), (12, 92)]), 'shade', 'b', False),
             fringe([(66, 4), (90, 18), (96, 42), (94, 66, 1), (86, 50), (80, 62, 1), (76, 42), (66, 30)])],
    'back': [L(outline([(14, 120), (6, 90), (6, 40), (0, 20, 1), (16, 22), (18, 0, 1), (30, 12), (40, -14, 1), (50, 6), (62, -20, 1), (68, 6), (84, -4, 1), (84, 18),
                        (100, 20, 1), (94, 40), (94, 90), (86, 120), (74, 104), (62, 124, 1), (50, 106), (38, 124, 1), (26, 104)])),
             L(outline([(56, 4), (86, 16), (96, 50), (88, 116), (66, 110), (70, 50)]), 'shade', 'b', False),
             L(outline([(4, 70), (-14, 62, 1), (6, 60)]), 'skin', 'b', ln=True), L(outline([(96, 70), (114, 62, 1), (94, 60)]), 'skin', 'b', ln=True)],
}

# El Raimon de Chrono Stone usa la misma forma de Hakuryuu (con Kongming): el de pelo turquesa con moño blanco es su
# Mixi Max con Tsurugi, que no es el del juego
CHARS['cs-team-raimon:bailong-cs-hakuryuu-mm'] = CHARS[f'{T}:bailong']
