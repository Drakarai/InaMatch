"""Tropa Acrobática del Fútbol (orion-soccer-zatsugidan, wiki "Soccer Zatsugidan"): la selección china de Orion (Inazuma
Eleven: Orion no Kokuin). Modelos 3D de オリオンの刻印; cada uno tiene una sola forma. Li Hao (jimmy-wongfu) sale en la wiki como
'リ・ハオ (real name)': su modelo es el de リ・ハオ. Xiao Longbao (wilson-ip) es el entrenador y Li Yuchen (lucy-wongfu) la mánager.
Todos van como 'orion-soccer-zatsugidan:<id>'."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import quad  # noqa: F401

T = 'orion-soccer-zatsugidan'
PALE = '#fde4c4'
WHITE = (248, 248, 248, 255)
GOLD = (222, 184, 110, 255)
BLACK = (24, 22, 26, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


def thick(pts, c, w=3.0, z='f'):
    """Trazo con contorno (mechones sueltos, trenzas finas)."""
    return [L(pts, OUTC, z, False, False, w + 2.2), L(pts, c, z, False, False, w)]


# Kung Fuche (Bruce Lau, portero): melena negra lisa y larga peinada hacia atrás, con un pico que sobresale hacia arriba en
# cada lado de la frente como un tupé partido; le cae hasta el pecho; punto en la frente, ojos verdes muy marcados y ceño
CHARS[f'{T}:bruce-lau'] = {
    'body': 'normal', 'pal': pal('#2c2c34', PALE, iris='#2aa088', shade='#202026', deep='#141418'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': [(16, 66), (20, 48), (30, 42), (40, 46), (50, 42), (60, 46), (70, 42), (80, 48), (84, 66)]},
    'front': [L(outline([(10, 124, 1), (8, 90), (12, 56), (6, 36), (-6, 12, 1), (16, 18), (32, 8), (50, 6), (68, 8), (86, 14), (104, 4, 1), (94, 30), (90, 56), (92, 90), (90, 124, 1),
                         (82, 104), (80, 60), (20, 60), (20, 104)])),
              L(outline([(56, 8), (84, 16), (100, 8), (92, 30), (88, 56), (90, 110), (82, 96), (80, 56), (70, 28)]), 'shade', 'b', False),
              strand(quad((14, 24), (18, 20), (22, 26)), 'deep', 'b', 1.0), strand([(30, 18), (26, 50)], 'deep', 'b', 1.0), strand([(70, 18), (74, 50)], 'deep', 'b', 1.0),
              L(ell(50, 58, 1.8, 1.8), OUTC, 'f', False),
              L([(27, 81), (44, 80)], OUTC, 'f', False, False, 1.0), L([(73, 81), (56, 80)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(78, 52), (84, 40), (92, 26), (110, 18, 1), (86, 12), (66, 4), (40, 4), (18, 16), (6, 40), (4, 76), (-2, 110), (-10, 126, 1), (10, 116), (24, 92),
                        (34, 72), (44, 58), (60, 54)])),
             L(outline([(6, 40), (28, 46), (34, 72), (20, 96), (2, 108)]), 'shade', 'b', False)],
    'back': [L(outline([(8, 124, 1), (6, 90), (8, 56), (2, 34), (-6, 12, 1), (16, 16), (32, 6), (50, 4), (68, 6), (86, 14), (106, 8, 1), (96, 32), (92, 56), (94, 90), (92, 124, 1),
                        (70, 112), (50, 120), (30, 112)])),
             L(outline([(54, 6), (84, 16), (96, 34), (92, 60), (92, 118), (70, 108), (60, 60)]), 'shade', 'b', False),
             strand([(30, 20), (26, 110)], 'deep', 'b', 1.0), strand([(50, 10), (50, 116)], 'deep', 'b', 1.0)],
}

# Tao Lu (Cindy Fong): chica de pelo naranja con un moño en la coronilla, flequillo largo de lado y dos mechones finos que le
# caen junto a la cara hasta el pecho; ojos violeta con raya roja, labios marrones
CHARS[f'{T}:cindy-fong'] = {
    'body': 'chica', 'pal': pal('#ec7a4a', PALE, iris='#7a5ab0', shade='#c85c34', deep='#a04424'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'lips', 'mouth_y': 96, 'mouth_w': 5, 'hairline': (60, 46)},
    'front': [L(outline([(14, 66), (12, 40), (22, 18), (38, 8), (62, 8), (80, 18), (88, 40), (86, 66), (80, 52), (20, 52)])),
              L(outline([(56, 8), (78, 18), (88, 40), (86, 62), (74, 36)]), 'shade', 'b', False),
              fringe([(18, 62), (20, 40), (34, 24), (52, 20), (70, 26), (82, 42), (84, 60), (72, 48), (56, 40), (40, 42), (28, 50)]),
              L(outline([(30, 28), (52, 22), (66, 28), (48, 32)]), 'light', 'f', False),
              thick(quad((20, 56), (16, 84), (18, 116)), 'mid', 3.4), thick(quad((80, 56), (84, 84), (82, 116)), 'mid', 3.4),
              L(quad((27, 79), (34, 82), (44, 80)), (190, 50, 40, 255), 'f', False, False, 1.2), L(quad((73, 79), (66, 82), (56, 80)), (190, 50, 40, 255), 'f', False, False, 1.2)],
    'side': [L(ell(18, 14, 11, 10), 'mid', 'b', ln=True),
             L(outline([(78, 54), (86, 40), (82, 16), (62, 4), (36, 6), (16, 18), (8, 40), (12, 62), (24, 70), (36, 64), (46, 56), (62, 54)])),
             L(outline([(8, 36), (30, 42), (38, 60), (22, 68), (10, 60)]), 'shade', 'b', False),
             thick(quad((82, 54), (88, 84), (84, 116)), 'mid', 3.4)],
    'back': [L(outline([(16, 74), (12, 44), (20, 20), (38, 8), (62, 8), (80, 20), (88, 44), (84, 74), (50, 80)])),
             L(outline([(56, 8), (80, 20), (88, 44), (84, 72), (62, 78)]), 'shade', 'b', False),
             L(ell(50, 30, 13, 12), 'mid', 'b', ln=True), L(ell(50, 30, 6, 6), 'shade', 'b', False),
             strand([(34, 14), (24, 70)], 'deep', 'b', 1.0), strand([(66, 14), (76, 70)], 'deep', 'b', 1.0), strand([(50, 44), (50, 78)], 'deep', 'b', 1.0),
             thick(quad((20, 70), (18, 92), (20, 116)), 'mid', 3.4, 'b'), thick(quad((80, 70), (82, 92), (80, 116)), 'mid', 3.4, 'b')]}

# Xiao Lau (Michelle Luo): chica de melena negra larguísima, recogida arriba en un moño alto con hilos dorados, con un mechón
# que se le riza por fuera a un lado; sombra violeta en los ojos, ojos violeta y sonrisa
CHARS[f'{T}:michelle-luo'] = {
    'body': 'chica', 'pal': pal('#2a1418', PALE, iris='#8a7ad8', shade='#1c0c10', deep='#100406'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 94, 'hairline': [(16, 66), (22, 50), (34, 44), (50, 52), (64, 42), (78, 48), (84, 66)]},
    'front': [L(outline([(38, 14), (36, -6), (50, -18), (64, -6), (62, 14)])),
              L(outline([(10, 124, 1), (8, 90), (12, 56), (14, 30), (26, 12), (50, 4), (74, 12), (86, 30), (88, 56), (92, 80), (102, 88), (108, 78, 1), (110, 92), (98, 100),
                         (90, 110), (90, 124, 1), (80, 104), (80, 60), (20, 60), (20, 104)])),
              L(outline([(56, 6), (76, 14), (88, 34), (88, 60), (80, 50), (72, 28)]), 'shade', 'b', False),
              L(quad((40, -6), (50, -12), (60, -6)), GOLD, 'f', False, False, 1.2), L(quad((38, 2), (50, -4), (62, 2)), GOLD, 'f', False, False, 1.2),
              L(quad((36, 10), (50, 4), (64, 10)), GOLD, 'f', False, False, 1.2),
              L(quad((25, 68), (34, 64), (44, 68)), (150, 80, 180, 255), 'f', False, False, 2.4), L(quad((75, 68), (66, 64), (56, 68)), (150, 80, 180, 255), 'f', False, False, 2.4)],
    'side': [L(outline([(44, 18), (30, 2), (30, -16), (44, -26), (58, -18), (60, 0), (54, 14)])),
             L(outline([(78, 54), (86, 40), (82, 16), (62, 4), (36, 8), (16, 22), (8, 46), (6, 80), (2, 110), (-4, 126, 1), (14, 118), (26, 96), (34, 74), (44, 58), (62, 54)])),
             L(outline([(8, 40), (30, 46), (34, 74), (20, 100), (4, 108)]), 'shade', 'b', False),
             L(quad((32, -8), (44, -14), (58, -8)), GOLD, 'f', False, False, 1.2),
             L(outline([(78, 52), (88, 58), (88, 80), (82, 74)]), 'mid', 'f')],
    'back': [L(outline([(38, 14), (36, -6), (50, -18), (64, -6), (62, 14)])),
             L(outline([(8, 124, 1), (6, 90), (8, 56), (14, 30), (26, 12), (50, 4), (74, 12), (86, 30), (92, 56), (94, 90), (92, 124, 1), (70, 112), (50, 120), (30, 112)])),
             L(outline([(56, 6), (76, 14), (90, 34), (92, 60), (92, 118), (70, 108), (60, 60)]), 'shade', 'b', False),
             L(quad((40, -6), (50, -12), (60, -6)), GOLD, 'f', False, False, 1.2), L(quad((22, 46), (50, 38), (78, 46)), GOLD, 'b', False, False, 1.2),
             L(outline([(-6, 94), (-14, 86, 1), (-8, 100), (6, 104), (8, 94)]))]}

# Min Yingqi (Sammo Tong): grandullón con un sombrero de bambú marrón redondo y ancho, con una punta encima; ojos cerrados
# sonrientes, espirales naranjas en los mofletes y una sonrisa enorme
SWIRL = (230, 150, 70, 255)
CHARS[f'{T}:sammo-tong'] = {
    'body': 'corpulento', 'pal': pal('#9a6a3e', PALE, shade='#7a5030', deep='#5a3820', light='#c49a6a'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'none', 'eye_y': 80, 'hairline': False,
             'face_front': blob([(14, 50), (50, 40), (86, 50), (90, 76), (86, 100), (66, 112), (50, 114), (34, 112), (14, 100), (10, 76)])},
    'front': [L(outline([(48, 0), (54, -18, 1), (60, -2)]), 'shade'),
              L(outline([(-10, 72), (-6, 50), (6, 24), (26, 6), (50, 0), (74, 6), (94, 24), (106, 50), (110, 72), (94, 74), (50, 70), (6, 74)]), 'mid', 'f'),
              L(outline([(-10, 66), (50, 60), (110, 66), (110, 74), (50, 72), (-10, 74)]), 'shade', 'f', False),
              L(outline([(60, 4), (86, 16), (100, 36), (108, 62), (88, 58), (74, 30)]), 'shade', 'f', False),
              L(quad((6, 60), (50, 48), (94, 60)), 'light', 'f', False, False, 2.0),
              strand([(30, 10), (18, 62)], 'deep', 'f', 1.0), strand([(50, 2), (50, 58)], 'deep', 'f', 1.0), strand([(70, 10), (82, 62)], 'deep', 'f', 1.0),
              L(quad((30, 92), (26, 86), (32, 84)) + quad((32, 84), (36, 90), (30, 94))[1:], SWIRL, 'f', False, False, 1.4),
              L(quad((70, 92), (74, 86), (68, 84)) + quad((68, 84), (64, 90), (70, 94))[1:], SWIRL, 'f', False, False, 1.4),
              L(quad((46, 86), (50, 90), (54, 86)), OUTC, 'f', False, False, 1.0),
              L(quad((34, 98), (50, 108), (66, 98)), OUTC, 'f', False, False, 1.6)],
    'side': [L(outline([(56, 2), (62, -18, 1), (70, 0)]), 'shade'),
             L(outline([(-12, 76), (-6, 50), (8, 22), (30, 4), (56, -2), (82, 6), (100, 26), (110, 52), (112, 74), (90, 72), (50, 70), (10, 74)]), 'mid', 'f'),
             L(outline([(-12, 70), (50, 62), (112, 68), (112, 76), (50, 72), (-12, 78)]), 'shade', 'f', False),
             L(outline([(-6, 50), (8, 22), (30, 4), (40, 10), (20, 40), (10, 70), (-10, 72)]), 'shade', 'f', False),
             strand([(56, 0), (76, 66)], 'deep', 'f', 1.0), strand([(30, 6), (34, 66)], 'deep', 'f', 1.0)],
    'back': [L(outline([(44, 2), (50, -18, 1), (56, 2)]), 'shade'),
             L(outline([(-10, 74), (-6, 50), (6, 24), (26, 6), (50, 0), (74, 6), (94, 24), (106, 50), (110, 74), (50, 78)])),
             L(outline([(52, 2), (76, 8), (96, 26), (108, 52), (110, 74), (70, 76), (64, 40)]), 'shade', 'b', False),
             strand([(30, 10), (18, 70)], 'deep', 'b', 1.0), strand([(50, 2), (50, 76)], 'deep', 'b', 1.0), strand([(70, 10), (82, 70)], 'deep', 'b', 1.0)],
}

# Che Lin (David Liang): flequillo negro de tazón muy recto con los lados y la nuca rapados (gris), y de la coronilla sale una
# trenza fina que sube en arco y cuelga, atada con cintas blancas; dos manchas negras redondas alrededor de los ojos, como
# un panda, con la pupila blanca en espiral
GREYSH = '#9a9898'
CHARS[f'{T}:david-liang'] = {
    'body': 'bajito', 'pal': pal('#1c1c22', PALE, shade='#121216', deep='#08080a', shaved=GREYSH),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 96, 'big_ears': 1, 'hairline': False},
    'front': [L(outline([(16, 72), (14, 50), (20, 46), (80, 46), (86, 50), (84, 72), (80, 56), (20, 56)]), 'shaved', 'f'),
              L(outline([(12, 58), (14, 34), (24, 18), (40, 10), (60, 10), (76, 18), (86, 34), (88, 58), (12, 58)]), 'mid', 'f'),
              L(outline([(56, 12), (74, 18), (86, 34), (88, 56), (76, 56), (70, 30)]), 'shade', 'f', False),
              L(outline([(44, 12), (56, 12), (56, 4), (44, 4)]), WHITE, 'f', ln=True),
              thick(quad((50, 4), (52, -40), (66, -38)) + quad((66, -38), (74, -30), (72, -14))[1:], 'mid', 3.4),
              L(outline([(68, -18), (76, -18), (76, -12), (68, -12)]), (210, 180, 190, 255), 'f', ln=True), L(ell(72, -6, 4, 4), 'mid', 'f', ln=True),
              L(ell(34, 76, 11, 10), BLACK, 'f', False), L(ell(66, 76, 11, 10), BLACK, 'f', False),
              L(ell(34, 76, 5.5, 5.5), WHITE, 'f', False), L(ell(66, 76, 5.5, 5.5), WHITE, 'f', False),
              L(quad((32, 74), (36, 78), (34, 80)), BLACK, 'f', False, False, 1.0), L(quad((64, 74), (68, 78), (66, 80)), BLACK, 'f', False, False, 1.0)],
    'side': [L(outline([(20, 64), (10, 50), (14, 40), (60, 40), (70, 50), (50, 56), (36, 70)]), 'shaved'),
             L(outline([(84, 46), (88, 30), (80, 14), (60, 6), (34, 8), (16, 20), (8, 40), (40, 42), (70, 44)])),
             L(outline([(8, 40), (16, 20), (34, 8), (40, 10), (24, 28), (20, 42)]), 'shade', 'b', False),
             thick(quad((48, 6), (30, -36), (2, -30)) + quad((2, -30), (-8, -22), (-6, -8))[1:], 'mid', 3.4, 'b'),
             L(ell(-6, -4, 4, 4), 'mid', 'f', ln=True),
             L(ell(82, 76, 6, 9), BLACK, 'f', False), L(ell(82, 76, 3, 4), WHITE, 'f', False)],
    'back': [L(blob([(16, 72), (14, 50), (24, 46), (76, 46), (86, 50), (84, 72), (74, 88), (50, 94), (26, 88)], 6), 'shaved'),
             L(outline([(12, 56), (14, 34), (24, 18), (40, 10), (60, 10), (76, 18), (86, 34), (88, 56), (12, 56)])),
             L(outline([(52, 12), (74, 18), (86, 34), (88, 54), (64, 54)]), 'shade', 'b', False),
             L(outline([(44, 12), (56, 12), (56, 4), (44, 4)]), WHITE, 'f', ln=True),
             thick(quad((50, 4), (48, -40), (34, -38)) + quad((34, -38), (26, -30), (28, -14))[1:], 'mid', 3.4),
             L(ell(28, -6, 4, 4), 'mid', 'f', ln=True)],
}

# Tan Tanmin (Donnie Yang): media melena lisa azul marino que se aclara abajo, con raya en medio y dos mechones en pico sobre
# la frente; pendientes de aro negros, ojos castaños entornados y una sonrisa
CHARS[f'{T}:donnie-yang'] = {
    'body': 'normal', 'pal': pal('#2c4468', PALE, iris='#8a6a2a', shade='#22344e', deep='#16243a', low='#466a9c'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 94, 'hairline': (60, 46)},
    'front': [L(outline([(12, 90), (10, 60), (14, 34), (26, 14), (50, 4), (74, 14), (86, 34), (90, 60), (88, 90), (80, 84), (80, 60), (20, 60), (20, 84)])),
              L(outline([(10, 70), (20, 66), (20, 84), (12, 90)]), 'low', 'b', False), L(outline([(90, 70), (80, 66), (80, 84), (88, 90)]), 'low', 'b', False),
              L(outline([(56, 6), (76, 16), (88, 36), (88, 60), (80, 52), (72, 28)]), 'shade', 'b', False),
              fringe([(18, 62), (22, 40), (36, 24), (50, 22), (64, 24), (78, 40), (82, 62), (72, 52), (58, 44), (52, 60, 1), (50, 42), (48, 60, 1), (42, 44), (28, 52)]),
              L(ell(16, 86, 2.6, 2.6), OUTC, 'f', False), L(ell(84, 86, 2.6, 2.6), OUTC, 'f', False)],
    'side': [L(outline([(78, 54), (86, 40), (82, 16), (62, 4), (36, 6), (16, 18), (6, 40), (6, 66), (16, 82), (34, 80), (40, 64), (46, 56), (62, 54)])),
             L(outline([(6, 56), (30, 56), (38, 72), (30, 82), (12, 78)]), 'low', 'b', False),
             L(outline([(6, 36), (30, 42), (36, 56), (8, 56)]), 'shade', 'b', False),
             L(ell(46, 82, 2.6, 3), OUTC, 'f', False), L(ell(46, 82, 1.2, 1.4), 'skin', 'f', False)],
    'back': [L(outline([(12, 86), (10, 58), (14, 34), (26, 14), (50, 4), (74, 14), (86, 34), (90, 58), (88, 86), (74, 90), (64, 84), (50, 90), (36, 84), (26, 90)])),
             L(outline([(10, 66), (50, 60), (90, 66), (88, 86), (50, 90), (12, 86)]), 'low', 'b', False),
             L(outline([(56, 6), (76, 16), (88, 36), (90, 64), (62, 62)]), 'shade', 'b', False),
             strand([(36, 14), (30, 80)], 'deep', 'b', 1.0), strand([(64, 14), (70, 80)], 'deep', 'b', 1.0),
             L(ell(14, 86, 2.6, 2.6), OUTC, 'f', False), L(ell(86, 86, 2.6, 2.6), OUTC, 'f', False)],
}

# Wu Longchi (Bolo Cheung): grandullón de piel morena con el pelo rubio claro recogido en un moño pequeño en lo alto, dos
# pinchos que se levantan a los lados de la cabeza como cuernos y el resto en rollos tras las orejas; cejas rubias gruesas
# fruncidas, ojos redondos y nariz ancha
CHARS[f'{T}:bolo-cheung'] = {
    'body': 'corpulento', 'pal': pal('#f2e2a4', '#8e5c3c', iris='#8a2a2a', shade='#d2bc7a', deep='#aa9658'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'big_ears': 2, 'ear_out': 3, 'eye_y': 78, 'eye_sep': 15, 'hairline': (46, 38),
             'face_front': blob([(14, 50), (50, 40), (86, 50), (90, 76), (86, 100), (66, 112), (50, 114), (34, 112), (14, 100), (10, 76)])},
    'front': [L(ell(50, 8, 7, 7)),
              L(outline([(14, 60), (8, 40), (4, 18), (2, -2, 1), (14, 14), (26, 6), (38, 2), (50, 0), (62, 2), (74, 6), (86, 14), (98, -2, 1), (96, 18), (92, 40), (86, 60), (80, 46), (20, 46)])),
              L(outline([(4, 100), (-2, 92), (4, 82), (12, 88), (12, 100)])), L(outline([(96, 100), (102, 92), (96, 82), (88, 88), (88, 100)])),
              L(outline([(60, 4), (76, 8), (86, 16), (96, 2), (94, 20), (90, 40), (84, 56), (74, 32)]), 'shade', 'b', False),
              strand([(36, 18), (40, 40)], 'deep', 'b', 1.0), strand([(64, 18), (60, 40)], 'deep', 'b', 1.0),
              L(outline([(24, 66), (44, 70), (42, 74), (26, 72)]), 'mid', 'f', ln=True), L(outline([(76, 66), (56, 70), (58, 74), (74, 72)]), 'mid', 'f', ln=True),
              L(outline([(44, 82), (50, 80), (56, 82), (60, 92), (50, 94), (40, 92)]), 'skin_d', 'f', False),
              L(quad((40, 92), (50, 96), (60, 92)), OUTC, 'f', False, False, 1.2)],
    'side': [L(ell(58, 8, 7, 7)),
             L(outline([(70, 36), (74, 22), (60, 14), (40, 14), (22, 22), (10, 36), (8, 56), (0, 70), (-2, 86), (10, 96), (26, 92), (36, 80), (42, 64), (52, 50)])),
             L(outline([(56, 18), (42, -4, 1), (70, 18)])),
             L(outline([(-2, 74), (14, 66), (30, 72), (34, 86), (20, 94), (4, 90)]), 'shade', 'b', False),
             L(outline([(74, 64), (88, 66), (86, 72), (74, 70)]), 'mid', 'f', ln=True)],
    'back': [L(ell(50, 8, 7, 7)),
             L(outline([(4, 98), (-4, 86), (8, 74), (10, 48), (4, 18), (2, -2, 1), (14, 14), (26, 6), (38, 2), (50, 0), (62, 2), (74, 6), (86, 14), (98, -2, 1), (96, 18), (90, 48), (92, 74), (104, 86), (96, 98),
                        (76, 94), (64, 100), (50, 94), (36, 100), (24, 94)])),
             L(outline([(54, 2), (74, 6), (86, 14), (96, 2), (94, 20), (88, 46), (90, 72), (66, 88), (60, 40)]), 'shade', 'b', False),
             L(outline([(2, 92), (20, 84), (36, 94), (50, 88), (64, 94), (80, 84), (98, 92), (76, 98), (50, 96), (24, 98)]), 'shade', 'b', False)],
}

# Zhou Xing (Jackie Tan, capitán): pelo lila en pinchos echados hacia atrás, con dos alas grises oscuras a los lados y la nuca
# azul oscura; varios mechones largos y finos le caen por delante de la cara; ojos azul claro afilados y media sonrisa
CHARS[f'{T}:jackie-tan'] = {
    'body': 'normal', 'pal': pal('#a8a2e4', PALE, iris='#5aa8d8', shade='#8480c0', deep='#5a5890', wing='#56606e', nape='#1e2440'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': (56, 44)},
    'front': [L(outline([(16, 60), (2, 50, 1), (6, 34), (0, 14, 1), (16, 22), (24, 10)]), 'wing'), L(outline([(84, 60), (98, 50, 1), (94, 34), (100, 14, 1), (84, 22), (76, 10)]), 'wing'),
              L(outline([(16, 62), (14, 40), (24, 20), (40, 8), (46, -14, 1), (54, 4), (66, 8), (80, 20), (86, 40), (84, 62), (78, 48), (22, 48)])),
              L(outline([(50, 0), (54, 4), (66, 8), (80, 20), (86, 40), (84, 58), (74, 34)]), 'shade', 'b', False),
              strand([(46, -8), (44, 30)], 'deep', 'b', 1.0),
              thick(quad((44, 40), (30, 66), (36, 96)), 'mid', 1.6), thick(quad((56, 40), (70, 66), (64, 96)), 'mid', 1.6),
              thick(quad((40, 44), (22, 70), (20, 110)), 'nape', 1.6), thick(quad((60, 44), (80, 70), (80, 110)), 'nape', 1.6)],
    'side': [L(outline([(80, 50), (86, 38), (96, 30), (110, 6, 1), (88, 16), (84, 4), (70, -18, 1), (60, 2), (40, 4), (20, 14), (8, 32), (6, 52), (18, 64), (34, 58), (46, 52),
                        (62, 50)])),
             L(outline([(4, 40), (34, 44), (42, 54), (26, 64), (8, 58)]), 'nape', 'b', False),
             L(outline([(30, 40), (6, 26), (-14, 2, 1), (14, 14), (40, 26)]), 'wing'),
             thick(quad((82, 46), (90, 70), (82, 104)), 'nape', 1.6)],
    'back': [L(outline([(16, 70), (12, 44), (4, 34), (-4, 10, 1), (16, 22), (28, 12), (44, 6), (50, -14, 1), (56, 6), (72, 12), (84, 22), (104, 10, 1), (96, 34), (88, 44),
                        (84, 70), (50, 76)])),
             L(outline([(12, 46), (50, 40), (88, 46), (86, 70), (50, 76), (14, 70)]), 'nape', 'b', False),
             L(outline([(4, 34), (-4, 10), (16, 22), (24, 40)]), 'wing', 'b', False), L(outline([(96, 34), (104, 10), (84, 22), (76, 40)]), 'wing', 'b', False),
             thick(quad((22, 72), (18, 92), (22, 110)), 'nape', 1.6, 'b'), thick(quad((78, 72), (82, 92), (78, 110)), 'nape', 1.6, 'b')],
}

# Li Hao (Jimmy Wongfu): pelo verde oscuro alborotado en mechones que se abren a los lados y por detrás, con un pelo de antena
# y flequillo de puntas; ojos grandes gris azulado, coloretes y una sonrisa
BLUSH = (238, 150, 150, 255)
CHARS[f'{T}:jimmy-wongfu'] = {
    'body': 'bajito', 'pal': pal('#2e6a5a', PALE, iris='#4a5a7a', shade='#225046', deep='#163a32', light='#5a9a88'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 94,
             'hairline': [(16, 66), (22, 54), (28, 62), (34, 50), (42, 62), (50, 50), (58, 62), (66, 50), (72, 62), (78, 54), (84, 66)]},
    'front': [L(outline([(16, 74), (10, 82, 1), (12, 64), (-6, 56, 1), (8, 44), (-8, 34, 1), (12, 26), (14, 8, 1), (30, 14), (40, 4), (48, 6), (54, -2), (62, 6), (74, 4, 1),
                         (74, 16), (92, 12, 1), (88, 30), (108, 36, 1), (92, 44), (104, 58, 1), (88, 62), (90, 82, 1), (84, 74), (80, 56), (20, 56)])),
              L(outline([(56, 4), (74, 6), (74, 18), (90, 14), (88, 32), (104, 38), (90, 46), (100, 58), (86, 58), (76, 34)]), 'shade', 'b', False),
              L(quad((50, 4), (48, -10), (56, -14)), OUTC, 'f', False, False, 2.4), L(quad((50, 4), (48, -10), (56, -14)), 'mid', 'f', False, False, 1.0),
              strand([(30, 24), (36, 40)], 'deep', 'b', 1.0), strand([(70, 24), (64, 40)], 'deep', 'b', 1.0),
              L(ell(28, 88, 4, 2.4), BLUSH, 'f', False), L(ell(72, 88, 4, 2.4), BLUSH, 'f', False)],
    'side': [L(outline([(76, 56), (82, 44), (92, 42, 1), (86, 32), (90, 18), (74, 6), (60, 2), (60, -12, 1), (50, 2), (30, 4), (14, 14), (-4, 18, 1), (8, 28), (-8, 40, 1), (6, 46),
                        (0, 62, 1), (14, 60), (22, 70), (36, 64), (46, 56), (62, 54)])),
             L(outline([(4, 34), (28, 40), (38, 58), (22, 68), (8, 56)]), 'shade', 'b', False),
             L(ell(80, 88, 3, 2), BLUSH, 'f', False)],
    'back': [L(outline([(16, 82), (6, 90, 1), (10, 72), (-10, 62, 1), (6, 52), (-12, 40, 1), (8, 30), (6, 10, 1), (24, 14), (36, 4), (50, 6), (64, 4), (76, 14), (94, 10, 1),
                        (92, 30), (112, 40, 1), (94, 52), (110, 62, 1), (90, 72), (94, 90, 1), (80, 82), (64, 92, 1), (56, 82), (50, 94, 1), (44, 82), (36, 92, 1)])),
             L(outline([(54, 6), (76, 16), (92, 12), (90, 32), (108, 42), (92, 52), (106, 62), (88, 72), (90, 86), (78, 80), (62, 88), (60, 40)]), 'shade', 'b', False),
             L(quad((50, 6), (52, -8), (60, -12)), OUTC, 'f', False, False, 2.4), L(quad((50, 6), (52, -8), (60, -12)), 'mid', 'f', False, False, 1.0)],
}

# Wan Tanmeo (Jet Long): lleva un gorro rojo oscuro en forma de cono, que le cubre todo el pelo, con una cinta blanca y roja
# con una greca negra alrededor de la frente y la punta del gorro caída hacia atrás; ojos redondos pequeños y sonrisa
BAND = (240, 210, 210, 255)
CHARS[f'{T}:jet-long'] = {
    'body': 'normal', 'pal': pal('#8a1820', PALE, iris='#1a1418', shade='#6a1018', deep='#4a0a10', light='#b03a40'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False, 'eye_y': 78},
    'front': [L(outline([(10, 60), (14, 36), (28, 10), (44, -18), (50, -24, 1), (56, -18), (72, 10), (86, 36), (90, 60), (80, 64), (20, 64)]), 'mid', 'f'),
              L(outline([(52, -18), (72, 12), (86, 38), (88, 56), (74, 50), (64, 20)]), 'shade', 'f', False),
              L(outline([(40, -4), (50, -20), (54, 0), (46, 10)]), 'light', 'f', False),
              L(outline([(12, 50), (50, 44), (88, 50), (90, 64), (50, 60), (10, 64)]), BAND, 'f', ln=True),
              L([(18, 56), (26, 56), (26, 52), (32, 52), (32, 58), (40, 58), (40, 53), (48, 53), (48, 57), (56, 57), (56, 53), (62, 53), (62, 58), (70, 58), (70, 52), (76, 52),
                 (76, 56), (84, 56)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(86, 60), (90, 36), (80, 14), (60, 0), (50, -18, 1), (40, 2), (20, 10), (6, 30), (2, 52), (8, 66), (30, 64), (60, 62)])),
             L(outline([(14, 22), (0, 30), (-16, 42), (-12, 52, 1), (-4, 40), (8, 36)])),
             L(outline([(4, 48), (40, 46), (90, 46), (92, 62), (40, 64), (6, 66)]), BAND, 'f', ln=True),
             L([(14, 56), (24, 56), (24, 52), (32, 52), (32, 58), (44, 58), (44, 53), (54, 53), (54, 57), (66, 57), (66, 53), (76, 53), (76, 58), (86, 58)], OUTC, 'f', False, False, 1.0),
             L(outline([(40, 4), (60, 4), (80, 16), (86, 40), (60, 44), (30, 40)]), 'shade', 'b', False)],
    'back': [L(outline([(10, 64), (14, 36), (28, 10), (44, -18), (50, -24, 1), (56, -18), (72, 10), (86, 36), (90, 64), (50, 70)])),
             L(outline([(52, -18), (72, 12), (86, 38), (90, 62), (62, 66), (60, 20)]), 'shade', 'b', False),
             L(outline([(12, 50), (50, 46), (88, 50), (90, 64), (50, 62), (10, 64)]), BAND, 'f', ln=True),
             L([(18, 57), (84, 57)], OUTC, 'f', False, False, 1.0),
             L(outline([(46, 60), (54, 60), (60, 80), (52, 90, 1), (44, 80)]), 'mid', 'f', ln=True)],
}

# Xiu Chuna (Stephen Chang): pelo negro en forma de seta, una cúpula abombada en gajos que le tapa la frente con el borde
# recto y la nuca más oscura; orejas grandes, ojos grises con ojeras y gesto serio
CHARS[f'{T}:stephen-chang'] = {
    'body': 'normal', 'pal': pal('#3a3c3e', PALE, iris='#6a7480', shade='#2a2c2e', deep='#1c1c1e'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'line', 'mouth_y': 96, 'big_ears': 3, 'ear_out': 3, 'hairline': (60, 58)},
    'front': [L(outline([(8, 62), (2, 44), (8, 22), (24, 6), (50, 0), (76, 6), (92, 22), (98, 44), (92, 62), (50, 60)])),
              L(outline([(56, 2), (78, 8), (94, 26), (96, 46), (90, 60), (70, 58), (72, 28)]), 'shade', 'b', False),
              strand(quad((26, 60), (20, 40), (30, 22)), 'deep', 'b', 1.0), strand(quad((50, 60), (46, 36), (50, 10)), 'deep', 'b', 1.0),
              strand(quad((74, 60), (80, 40), (70, 22)), 'deep', 'b', 1.0),
              L(quad((28, 84), (34, 86), (42, 84)), OUTC, 'f', False, False, 0.8), L(quad((72, 84), (66, 86), (58, 84)), OUTC, 'f', False, False, 0.8)],
    'side': [L(outline([(88, 60), (98, 48), (96, 26), (78, 6), (50, 0), (24, 8), (6, 26), (0, 50), (10, 66), (30, 62), (50, 60), (70, 62)])),
             L(outline([(4, 40), (40, 44), (52, 60), (30, 64), (10, 66)]), 'shade', 'b', False),
             L(outline([(14, 66), (24, 64), (30, 82), (18, 80)]), 'deep', 'b', False)],
    'back': [L(outline([(8, 64), (2, 44), (8, 22), (24, 6), (50, 0), (76, 6), (92, 22), (98, 44), (92, 64), (50, 68)])),
             L(outline([(16, 64), (50, 60), (84, 64), (80, 84), (50, 90), (20, 84)]), 'shade'),
             L(outline([(56, 2), (78, 8), (94, 26), (98, 46), (92, 62), (66, 60)]), 'shade', 'b', False),
             strand([(50, 4), (50, 60)], 'deep', 'b', 1.0)],
}

# Chao Mao (Mars Hung): hombre de cara larga, mandíbula ancha, cejas negras gruesas y nariz grande; pelo rosa oscuro peinado
# hacia atrás en una coleta de pinchos que salen en abanico por detrás de la cabeza, y pinchos sueltos a los lados
CHARS[f'{T}:mars-hung'] = {
    'body': 'normal', 'pal': pal('#b05068', PALE, iris='#5a6a70', shade='#8a3a50', deep='#6a2a3a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 104, 'hairline': (44, 32),
             'face_front': blob([(18, 44), (50, 32), (82, 44), (86, 76), (82, 104), (66, 116), (50, 118), (34, 116), (18, 104), (14, 76)])},
    'front': [L(outline([(10, 70), (-14, 66, 1), (4, 56), (-14, 44, 1), (8, 40), (-2, 22, 1), (16, 24), (16, 4, 1), (28, 14), (40, 6), (50, 4), (60, 6), (72, 14), (84, 4, 1),
                         (84, 24), (102, 22, 1), (92, 40), (114, 44, 1), (96, 56), (114, 66, 1), (90, 70), (84, 50), (16, 50)])),
              L(outline([(56, 6), (72, 16), (84, 26), (98, 24), (90, 40), (108, 46), (94, 56), (84, 48)]), 'shade', 'b', False),
              L(quad((40, 8), (34, 30), (36, 44)), 'deep', 'b', False, False, 1.0), L(quad((60, 8), (66, 30), (64, 44)), 'deep', 'b', False, False, 1.0),
              L([(24, 64), (34, 60), (44, 64)], OUTC, 'f', False, False, 3.6), L([(76, 64), (66, 60), (56, 64)], OUTC, 'f', False, False, 3.6),
              L(outline([(44, 80), (50, 78), (56, 80), (60, 92), (50, 95), (40, 92)]), 'skin_d', 'f', False),
              L(quad((40, 92), (50, 96), (60, 92)), OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(26, 40), (2, 30), (-26, 22, 1), (0, 22), (-20, 6, 1), (6, 14), (-6, -12, 1), (14, 6), (16, -20, 1), (26, 6), (40, 2), (30, 30)])),
             L(outline([(84, 40), (88, 24), (72, 8), (50, 4), (30, 10), (20, 26), (24, 44), (34, 50), (50, 44), (70, 42)])),
             L(outline([(20, 30), (34, 36), (30, 50), (22, 44)]), 'deep', 'b', ln=True),
             L(outline([(4, 34), (-22, 44, 1), (6, 40), (-8, 60, 1), (16, 44)]), 'shade')],
    'back': [L(outline([(50, 30), (30, 18), (14, 2, 1), (36, 12), (34, -10, 1), (46, 8), (50, -16, 1), (56, 8), (68, -10, 1), (64, 12), (86, 2, 1), (70, 18), (94, 22, 1),
                        (70, 28), (104, 40, 1), (70, 38), (96, 58, 1), (64, 44), (74, 74, 1), (56, 48), (50, 76, 1), (44, 48), (26, 74, 1), (36, 44), (4, 58, 1), (30, 38),
                        (-4, 40, 1), (30, 28), (6, 22, 1)])),
             L(outline([(16, 54), (14, 34), (26, 14), (50, 8), (74, 14), (86, 34), (84, 54), (50, 50)]), 'mid', 'b', ln=True),
             L(outline([(54, 30), (68, -6), (64, 12), (86, 4), (70, 18), (92, 24), (70, 28), (100, 40), (70, 38), (92, 56), (64, 44), (58, 40)]), 'shade', 'b', False)],
}

# Xiao Longbao (Wilson Ip, entrenador): melena negra enorme de rizos gordos que se abomba a los lados como una nube, con un
# gorrito chino de gajos morados y amarillos con un botón encima; gafas redondas doradas, bigote fino de puntas y la boca
# abierta riendo
CAP_Y = (214, 176, 60, 255)
CAP_P = (120, 60, 110, 255)
CHARS[f'{T}:wilson-ip'] = {
    'body': 'normal', 'pal': pal('#2a3434', PALE, iris='#1a1418', shade='#1e2626', deep='#121818'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'none', 'hairline': (50, 40), 'glasses': (190, 170, 120, 255), 'eye_y': 74},
    'front': [L(outline([(16, 90), (-6, 92), (-18, 80), (-20, 62), (-12, 50), (-14, 36), (-2, 26), (10, 26), (24, 14), (40, 8), (60, 8), (76, 14), (90, 26), (102, 26), (114, 36),
                         (112, 50), (120, 62), (118, 80), (106, 92), (84, 90), (80, 60), (20, 60)])),
              L(outline([(-16, 66), (0, 56), (16, 64), (14, 86), (-4, 88), (-16, 80)]), 'shade', 'b', False),
              L(outline([(116, 66), (100, 56), (84, 64), (86, 86), (104, 88), (116, 80)]), 'shade', 'b', False),
              strand(quad((-8, 40), (0, 46), (8, 40)), 'deep', 'b', 1.0), strand(quad((92, 40), (100, 46), (108, 40)), 'deep', 'b', 1.0),
              L(outline([(36, 12), (36, 2), (42, -6), (58, -6), (64, 2), (64, 12)]), CAP_P, 'f', ln=True),
              L(outline([(44, -6), (56, -6), (56, 12), (44, 12)]), CAP_Y, 'f', False), L(outline([(34, 8), (66, 8), (66, 14), (34, 14)]), CAP_Y, 'f', ln=True),
              L(ell(50, -8, 3.4, 3), CAP_P, 'f', ln=True),
              L(ell(36, 74, 2.4, 2.4), OUTC, 'f', False), L(ell(64, 74, 2.4, 2.4), OUTC, 'f', False),
              L(quad((46, 86), (36, 86), (30, 96)), OUTC, 'f', False, False, 1.4), L(quad((54, 86), (64, 86), (70, 96)), OUTC, 'f', False, False, 1.4),
              L(outline([(38, 90), (62, 90), (58, 104), (50, 108), (42, 104)]), (120, 30, 30, 255), 'f', ln=True),
              L(outline([(42, 98), (58, 98), (54, 106), (46, 106)]), (230, 120, 110, 255), 'f', False),
              L(outline([(40, 90), (60, 90), (59, 93), (41, 93)]), WHITE, 'f', False)],
    'side': [L(outline([(76, 40), (78, 20), (60, 6), (40, 6), (20, 14), (6, 26), (-10, 30), (-22, 44), (-24, 62), (-18, 80), (-4, 92), (14, 94), (30, 86), (36, 70), (42, 56),
                        (60, 48)])),
             L(outline([(-20, 60), (6, 52), (30, 62), (32, 84), (10, 92), (-14, 84)]), 'shade', 'b', False),
             L(outline([(46, 12), (46, 2), (52, -6), (66, -6), (72, 2), (72, 12)]), CAP_P, 'f', ln=True), L(outline([(44, 8), (74, 8), (74, 14), (44, 14)]), CAP_Y, 'f', ln=True),
             L(ell(59, -8, 3.4, 3), CAP_P, 'f', ln=True),
             L(ell(82, 74, 2, 2.4), OUTC, 'f', False), L(quad((86, 86), (80, 88), (76, 96)), OUTC, 'f', False, False, 1.4)],
    'back': [L(outline([(14, 92), (-8, 92), (-20, 80), (-22, 62), (-14, 48), (-16, 34), (-4, 24), (10, 24), (24, 12), (40, 6), (60, 6), (76, 12), (90, 24), (104, 24), (116, 34),
                        (114, 48), (122, 62), (120, 80), (108, 92), (86, 92), (70, 100), (50, 96), (30, 100)])),
             L(outline([(-18, 66), (10, 56), (50, 62), (90, 56), (118, 66), (118, 80), (100, 92), (70, 98), (50, 94), (30, 98), (0, 92), (-18, 80)]), 'shade', 'b', False),
             L(outline([(36, 12), (36, 2), (42, -6), (58, -6), (64, 2), (64, 12)]), CAP_P, 'f', ln=True),
             L(outline([(44, -6), (56, -6), (56, 12), (44, 12)]), CAP_Y, 'f', False), L(outline([(34, 8), (66, 8), (66, 14), (34, 14)]), CAP_Y, 'f', ln=True),
             L(ell(50, -8, 3.4, 3), CAP_P, 'f', ln=True)],
}

# Chi Chinsu (Gordon Siu): cabeza rapada con una cresta azul que sube muy alta en pinchos, un mechón que le cae por la frente,
# gafas de sol negras de rendija y unos bigotes azules enormes que se curvan hacia fuera; sonrisa de dientes
SHADES = (20, 18, 22, 255)
CHARS[f'{T}:gordon-siu'] = {
    'body': 'normal', 'pal': pal('#5a8ab8', PALE, iris='#1a1418', shade='#3e6890', deep='#2c4c6a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 94, 'hairline': False,
             'face_front': blob([(20, 44), (50, 20), (80, 44), (84, 76), (78, 100), (50, 110), (22, 100), (16, 76)])},
    'front': [L(outline([(38, 30), (36, 6), (34, -26, 1), (46, -8), (50, -34, 1), (56, -10), (64, -20, 1), (62, 6), (60, 30), (50, 34)]), 'mid', 'f'),
              L(outline([(50, -30), (56, -10), (62, -16), (60, 8), (58, 28), (52, 10)]), 'shade', 'f', False),
              thick(quad((48, 28), (42, 52), (46, 70)), 'mid', 2.6),
              L(outline([(14, 66), (50, 64), (86, 66), (84, 74), (50, 72), (16, 74)]), SHADES, 'f'),
              L(quad((30, 62), (36, 58), (44, 62)), 'mid', 'f', False, False, 2.0), L(quad((70, 62), (64, 58), (56, 62)), 'mid', 'f', False, False, 2.0),
              L(outline([(38, 86), (24, 84), (8, 92), (-4, 92, 1), (6, 84), (22, 78), (40, 82)]), 'mid', 'f', ln=True),
              L(outline([(62, 86), (76, 84), (92, 92), (104, 92, 1), (94, 84), (78, 78), (60, 82)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(70, 26), (74, 6), (90, -10, 1), (72, -6), (70, -28, 1), (56, -6), (40, -24, 1), (40, 0), (44, 26), (56, 30)])),
             L(outline([(54, -6), (70, -24), (72, -4), (68, 22)]), 'shade', 'b', False),
             thick(quad((74, 22), (88, 40), (84, 62)), 'mid', 2.6),
             L(outline([(20, 64), (60, 62), (90, 66), (88, 74), (60, 70), (22, 70)]), SHADES, 'f'),
             L(outline([(76, 86), (60, 84), (40, 92), (28, 92, 1), (40, 84), (60, 78), (80, 82)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(38, 30), (36, 6), (34, -26, 1), (46, -8), (50, -34, 1), (56, -10), (64, -20, 1), (62, 6), (60, 30), (50, 34)])),
             L(outline([(50, -30), (56, -10), (62, -16), (60, 8), (58, 28), (52, 10)]), 'shade', 'b', False),
             L([(18, 66), (50, 64), (82, 66)], SHADES, 'f', False, False, 2.4),
             L(outline([(30, 92), (14, 90), (-2, 98), (-14, 96, 1), (-2, 88), (14, 84), (30, 86)]), 'mid', 'f', ln=True),
             L(outline([(70, 92), (86, 90), (102, 98), (114, 96, 1), (102, 88), (86, 84), (70, 86)]), 'mid', 'f', ln=True)],
}

# Li Yuchen (Lucy Wongfu, mánager): chica de pelo violeta con flequillo recto, recogido en dos trenzas que caen y se doblan en
# lazo a los lados de la cara, atadas con lazos negros; ojos verdes, coloretes y boca seria
BOW = (26, 24, 30, 255)


def _braid_loop(s, z='f'):
    m = lambda pts: [(50 + (q[0] - 50) * s,) + tuple(q[1:]) for q in pts]  # noqa: E731
    out = [L(m(quad((18, 74), (0, 92), (10, 108)) + quad((10, 108), (22, 112), (20, 92))[1:]), OUTC, z, False, False, 7.0),
           L(m(quad((18, 74), (0, 92), (10, 108)) + quad((10, 108), (22, 112), (20, 92))[1:]), 'mid', z, False, False, 4.6)]
    for (x, y) in ((8, 88), (6, 98), (12, 106), (18, 104)):
        out.append(L(m([(x - 2, y - 1), (x + 2, y + 1)]), 'deep', z, False, False, 1.0))
    out.append(L(m(outline([(18, 70), (8, 64), (8, 78), (18, 74), (28, 80), (28, 64)])), BOW, z, ln=False))
    return out


CHARS[f'{T}:lucy-wongfu'] = {
    'body': 'chica', 'pal': pal('#6a5aa0', PALE, iris='#7a9a2a', shade='#524480', deep='#3c3060'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': (62, 60)},
    'front': [L(outline([(14, 74), (10, 50), (16, 26), (32, 10), (50, 6), (68, 10), (84, 26), (90, 50), (86, 74), (80, 62), (20, 62)])),
              L(outline([(56, 8), (76, 16), (88, 36), (88, 62), (80, 56), (72, 30)]), 'shade', 'b', False),
              fringe([(18, 64), (20, 46), (30, 34), (50, 32), (70, 34), (80, 46), (82, 64), (18, 64)]),
              strand([(34, 36), (34, 64)], 'deep', 'f', 0.8), strand([(50, 32), (50, 64)], 'deep', 'f', 0.8), strand([(66, 36), (66, 64)], 'deep', 'f', 0.8),
              _braid_loop(1), _braid_loop(-1),
              L(ell(28, 88, 4, 2.4), BLUSH, 'f', False), L(ell(72, 88, 4, 2.4), BLUSH, 'f', False)],
    'side': [L(outline([(80, 62), (86, 44), (80, 18), (60, 6), (36, 8), (16, 20), (6, 44), (10, 66), (24, 74), (36, 68), (46, 62), (62, 62)])),
             L(outline([(8, 40), (30, 46), (38, 64), (22, 72), (10, 64)]), 'shade', 'b', False),
             L(outline([(80, 44), (88, 50), (88, 64), (80, 64)]), 'mid', 'f'),
             [dict(l, s=[(q[0] + 16,) + tuple(q[1:]) for q in l['s']]) for l in _braid_loop(1)]],
    'back': [L(outline([(14, 78), (10, 50), (16, 26), (32, 10), (50, 6), (68, 10), (84, 26), (90, 50), (86, 78), (50, 84)])),
             L(outline([(56, 8), (76, 16), (88, 36), (90, 64), (84, 78), (60, 82), (56, 40)]), 'shade', 'b', False),
             strand([(50, 8), (50, 82)], 'deep', 'b', 1.0),
             _braid_loop(1, 'b'), _braid_loop(-1, 'b')],
}
