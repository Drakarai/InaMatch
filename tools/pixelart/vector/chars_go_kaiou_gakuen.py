"""Academia Cala Pirata (go-kaiou-gakuen): sus modelos 3D de Inazuma Eleven GO como referencia (busto de frente, perfil
y espalda); el de Santelmo Phyre, que no tiene modelo, de su retrato."""
from chars import CHARS, L, OUTC, ell, outline, pal, rope, strand
from chars_alius import WIDE_FACE
from chars_bigwaves import side_eye, white_eyes
from heads import quad

WHITE = (250, 250, 250, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


def mirror_pts(pts):
    return [(100 - p[0],) + tuple(p[1:]) for p in pts]


# Ishmael Ahab (portero): una melena castaña de león enorme de mechones en punta que le cae por delante de los hombros, una
# máscara blanca que le tapa la cara desde la nariz y pintura azul alrededor de los ojos
_mane_f = [(-6, 120), (-20, 96, 1), (-8, 84), (-30, 66, 1), (-10, 56), (-26, 34, 1), (-6, 28), (-10, 6, 1), (12, 8), (16, -12, 1), (32, 0), (44, -18, 1),
           (54, -2), (68, -16, 1), (74, 2), (94, -6, 1), (96, 14), (118, 22, 1), (106, 36), (128, 52, 1), (110, 62), (126, 82, 1), (108, 90), (118, 116, 1),
           (96, 112), (86, 120), (84, 70), (16, 70), (14, 120)]
CHARS['ishmael-ahab'] = {
    'body': 'normal', 'pal': pal('#a07850', '#f6d0a8', iris='#1e1414', shade='#7a5638', paint='#2a4ab8', mask='#f2ece0', mask_d='#d8ccb8'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': [L(outline(_mane_f)), L(outline([(60, -2), (96, 12), (118, 54), (112, 112), (90, 116), (88, 50)]), 'shade', 'b', False),
              L(outline([(20, 82), (80, 82), (82, 96), (70, 110), (50, 116), (30, 110), (18, 96)]), 'mask', 'f', ln=True),
              L(outline([(46, 88), (54, 88), (50, 94)]), (220, 140, 130, 255), 'f', False),
              L(outline([(22, 70), (34, 66), (44, 72), (40, 80), (28, 80)]), 'paint', 'f', ln=True),
              L(outline([(78, 70), (66, 66), (56, 72), (60, 80), (72, 80)]), 'paint', 'f', ln=True),
              L(ell(34, 74, 3, 2.4), WHITE, 'f', False), L(ell(66, 74, 3, 2.4), WHITE, 'f', False),
              L(ell(34, 74, 1.4, 1.4), OUTC, 'f', False), L(ell(66, 74, 1.4, 1.4), OUTC, 'f', False),
              fringe([(10, 76), (6, 40), (22, 18), (50, 10), (78, 18), (94, 40), (90, 76), (82, 60), (78, 44), (66, 56, 1), (58, 40), (50, 54, 1), (42, 40),
                      (34, 56, 1), (22, 44), (18, 60)]),
              strand([(18, 40), (10, 90), (6, 116)], 'shade', 'f', 1.2), strand([(82, 40), (90, 90), (94, 116)], 'shade', 'f', 1.2)],
    'side': [L(outline([(56, 62), (66, 48), (84, 46), (94, 30), (88, 8), (96, -6, 1), (74, -2), (64, -18, 1), (50, -4), (28, -14, 1), (20, 4), (-6, 0, 1), (2, 20),
                        (-24, 30, 1), (-6, 44), (-30, 62, 1), (-8, 70), (-24, 94, 1), (0, 92), (-6, 118, 1), (20, 104), (40, 120, 1), (46, 96), (54, 80)])),
             L(outline([(-6, 40), (20, 46), (40, 108), (0, 104)]), 'shade', 'b', False),
             L(outline([(70, 82), (94, 80), (98, 96), (84, 110), (66, 104)]), 'mask', 'f', ln=True),
             L(outline([(76, 68), (90, 66), (92, 78), (78, 80)]), 'paint', 'f', ln=True), L(ell(86, 73, 1.6, 2), OUTC, 'f', False),
             fringe([(66, 4), (92, 18), (98, 44), (94, 66, 1), (86, 50), (80, 64, 1), (76, 40)])],
    'back': [L(outline([(-6, 112), (-20, 96, 1), (-8, 84), (-30, 66, 1), (-10, 56), (-26, 34, 1), (-6, 28), (-10, 6, 1), (12, 8), (16, -12, 1), (32, 0), (44, -18, 1),
                        (54, -2), (68, -16, 1), (74, 2), (94, -6, 1), (96, 14), (118, 22, 1), (106, 36), (128, 52, 1), (110, 62), (126, 82, 1), (108, 90),
                        (118, 112, 1), (90, 108), (70, 120, 1), (50, 108), (30, 120, 1), (10, 108)])),
             L(outline([(56, 0), (96, 14), (118, 54), (112, 108), (70, 112)]), 'shade', 'b', False),
             L(ell(50, 24, 12, 6), 'shade', 'b', False)],
}

# Octavus Kraken: cabeza rapada gris con una cresta azul de mechones gruesos en abanico, de la que salen tentáculos de pelo
# azul que caen por los lados y delante de la cara con puntas de cuentas celestes; piel morena y cejas fruncidas
def _tentacles(view):
    if view == 'front':
        return [L(rope((30, 30), (6, 40), (-6, 92), 7), 'mid', 'f'), L(rope((70, 30), (94, 40), (106, 92), 7), 'mid', 'f'),
                L(rope((40, 34), (30, 56), (34, 86), 6), 'mid', 'f'), L(rope((60, 34), (70, 56), (66, 86), 6), 'mid', 'f'),
                L(rope((48, 40), (44, 60), (52, 74), 5), 'mid', 'f'),
                L(outline([(-10, 86), (-2, 86), (-2, 100), (-10, 100)]), 'bead', 'f', ln=True),
                L(outline([(102, 86), (110, 86), (110, 100), (102, 100)]), 'bead', 'f', ln=True)]
    if view == 'side':
        return [L(rope((30, 10), (0, 30), (-6, 96), 7), 'mid', 'b'), L(rope((40, 12), (14, 40), (14, 100), 7), 'mid', 'b'),
                L(rope((64, 18), (84, 40), (88, 90), 6), 'mid', 'f'),
                L(outline([(84, 88), (92, 88), (92, 102), (84, 102)]), 'bead', 'f', ln=True)]
    return [L(rope((50, 14), (10, 30), (-20, 92), 7), 'mid', 'f'), L(rope((50, 14), (90, 30), (120, 92), 7), 'mid', 'f'),
            L(rope((50, 16), (24, 40), (14, 100), 7), 'mid', 'f'), L(rope((50, 16), (76, 40), (86, 100), 7), 'mid', 'f')]


CHARS['octavus-kraken'] = {
    'body': 'corpulento', 'pal': pal('#2a4a8a', '#a8784e', iris='#1e1414', buzz='#a8a49a', buzz_d='#8a8678', bead='#a0d8e8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'hairline': False, 'face_front': WIDE_FACE, 'big_ears': 2},
    'front': [L(outline([(14, 64), (12, 34), (24, 14), (50, 6), (76, 14), (88, 34), (86, 64), (50, 58)]), 'buzz', 'f'),
              L(outline([(34, 30), (30, -10), (40, -26), (50, -30), (60, -26), (70, -10), (66, 30), (50, 34)]), 'mid', 'f'),
              strand([(42, 28), (40, -20)], 'deep', 'f', 1.0), strand([(50, 30), (50, -26)], 'deep', 'f', 1.0), strand([(58, 28), (60, -20)], 'deep', 'f', 1.0)]
             + _tentacles('front'),
    'side': [L(outline([(8, 76), (6, 36), (20, 12), (50, 4), (78, 12), (90, 34), (86, 52), (60, 56), (50, 76), (30, 92), (14, 88)]), 'buzz', 'f'),
             L(outline([(70, 20), (60, -8), (40, -18), (14, -12), (0, 6), (-6, 30), (14, 26), (30, 12), (50, 10)]), 'mid', 'f')] + _tentacles('side'),
    'back': [L(outline([(14, 74), (12, 34), (24, 14), (50, 6), (76, 14), (88, 34), (86, 74), (70, 90), (30, 90)]), 'buzz', 'f'),
             L(outline([(56, 8), (84, 26), (86, 74), (64, 88)]), 'buzz_d', 'f', False),
             L(outline([(34, 24), (30, -10), (40, -26), (50, -30), (60, -26), (70, -10), (66, 24), (50, 28)]), 'mid', 'f')] + _tentacles('back'),
}

# Roger Jolly: pelo blanco rosado tieso hacia arriba en dos cuernos enormes, piel morena, gafas negras de pasta y una
# sonrisa de oreja a oreja con los dientes
CHARS['roger-jolly'] = {
    'body': 'normal', 'pal': pal('#d8c4cc', '#b08050', iris='#1e1414', shade='#a88a98'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False, 'glasses': (30, 30, 30, 255), 'glasses_rect': True,
             'big_ears': 2},
    'front': [L(outline([(14, 62), (10, 40), (12, 20), (-8, -34, 1), (30, 12), (50, 8), (70, 12), (108, -34, 1), (88, 20), (90, 40), (86, 62), (80, 52), (20, 52)])),
              L(outline([(70, 14), (100, -24), (86, 26), (86, 50), (80, 40)]), 'shade', 'b', False),
              L(outline([(4, -16), (12, -6), (22, 12), (14, 10)]), 'light', 'b', False),
              fringe([(14, 58), (18, 40), (32, 32), (50, 30), (68, 32), (82, 40), (86, 58), (76, 50), (66, 56, 1), (60, 44), (50, 54, 1), (40, 44), (34, 56, 1),
                      (24, 50)])],
    'side': [L(outline([(54, 56), (62, 46), (82, 46), (90, 30), (92, 0, 1), (74, 18), (60, -24, 1), (46, 10), (20, -8, 1), (20, 14), (2, 24), (6, 54), (20, 70),
                        (40, 68)])),
             L(outline([(4, 30), (22, 36), (24, 62), (8, 56)]), 'shade', 'b', False),
             fringe([(68, 22), (90, 30), (94, 46), (90, 58, 1), (84, 46), (76, 40)])],
    'back': [L(outline([(16, 76), (12, 40), (12, 20), (-8, -34, 1), (30, 12), (50, 20), (70, 12), (108, -34, 1), (88, 20), (88, 40), (84, 76), (50, 86)])),
             L(outline([(56, 18), (100, -24), (86, 50), (80, 72), (60, 80)]), 'shade', 'b', False)],
}

# Sinbad Saylor: pelo negro de pinchos de punta en todas direcciones, con mechones cortos en la frente y las patillas en
# punta; cara seria
CHARS['sinbad-saylor'] = {
    'body': 'normal', 'pal': pal('#1e1e22', '#f8d0a8', iris='#5a2a1a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 84), (-8, 80, 1), (8, 66), (-10, 56, 1), (6, 44), (-6, 26, 1), (12, 20), (8, -2, 1), (28, 8), (32, -14, 1), (46, 2), (56, -18, 1),
                         (62, 2), (78, -6, 1), (80, 14), (102, 14, 1), (92, 30), (110, 40, 1), (94, 52), (108, 66, 1), (92, 72), (104, 86, 1), (86, 84), (84, 60),
                         (16, 60)])),
              L(outline([(60, 2), (84, 14), (96, 46), (90, 76), (80, 50)]), 'shade', 'b', False),
              fringe([(12, 66), (16, 40), (30, 24), (50, 18), (70, 24), (84, 40), (88, 66), (80, 54), (74, 64, 1), (68, 48), (60, 60, 1), (54, 46), (46, 62, 1),
                      (40, 48), (32, 60, 1), (26, 50), (20, 64, 1)])],
    'side': [L(outline([(56, 60), (62, 48), (82, 48), (92, 34), (90, 14), (100, 0, 1), (78, 4), (72, -14, 1), (56, 0), (40, -18, 1), (32, 2), (8, -6, 1), (14, 14),
                        (-12, 22, 1), (4, 34), (-16, 48, 1), (2, 56), (-10, 74, 1), (10, 72), (4, 92, 1), (22, 82), (30, 96, 1), (40, 80)])),
             L(outline([(2, 34), (22, 40), (26, 74), (6, 66)]), 'shade', 'b', False),
             fringe([(66, 4), (90, 18), (96, 42), (94, 66, 1), (86, 50), (80, 62, 1), (76, 42)])],
    'back': [L(outline([(14, 86), (-10, 82, 1), (6, 68), (-14, 56, 1), (4, 44), (-10, 24, 1), (12, 20), (6, -4, 1), (28, 8), (32, -16, 1), (46, 2), (56, -20, 1),
                        (62, 2), (80, -8, 1), (80, 14), (106, 14, 1), (94, 32), (114, 42, 1), (96, 54), (112, 70, 1), (92, 76), (102, 92, 1), (80, 90), (64, 100, 1),
                        (50, 90), (36, 100, 1), (24, 90)])),
             L(outline([(56, 4), (86, 16), (100, 50), (90, 86), (60, 92)]), 'shade', 'b', False)],
}

# Cheung Po: grandote, la cabeza afeitada en forma de huevo con un único rizo negro que sale de lo alto, un parche negro en
# el ojo derecho atado en diagonal y el otro ojo guiñado con media sonrisa
CHARS['cheung-po'] = {
    'body': 'corpulento', 'pal': pal('#1e1e1e', '#e8a868', iris='#1e1414', skin_d='#c8884e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 100, 'hairline': False, 'face_front': WIDE_FACE, 'big_ears': 2},
    'front': [L(outline([(16, 64), (14, 30), (26, 4), (50, -8), (74, 4), (86, 30), (84, 64)]), 'skin'),
              L(quad((50, -6), (46, -22), (58, -30)), 'mid', 'b', False, False, 4.0),
              L(outline([(60, -2), (80, 12), (86, 40), (82, 60), (74, 30)]), 'skin_d', 'b', False),
              L(quad((14, 82), (50, 50), (86, 44)), OUTC, 'f', False, False, 1.8),
              L(outline([(22, 70), (42, 66), (46, 78), (36, 86), (24, 84)]), OUTC, 'f', False),
              L(quad((58, 74), (65, 70), (72, 74)), OUTC, 'f', False, False, 2.0), L(quad((56, 62), (64, 60), (70, 66)), OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(10, 60), (10, 28), (26, 4), (50, -8), (74, 2), (88, 26), (92, 50), (80, 60), (50, 62)]), 'skin'),
             L(quad((48, -6), (46, -22), (58, -30)), 'mid', 'b', False, False, 4.0),
             L(outline([(10, 30), (30, 40), (40, 80), (16, 76)]), 'skin_d', 'b', False),
             L(quad((20, 84), (60, 82), (90, 72)), OUTC, 'f', False, False, 1.8), L(outline([(82, 66), (92, 66), (92, 78), (84, 80)]), OUTC, 'f', False)],
    'back': [L(outline([(16, 76), (14, 30), (26, 4), (50, -8), (74, 4), (86, 30), (84, 76), (50, 92)]), 'skin'),
             L(quad((50, -6), (48, -22), (58, -30)), 'mid', 'b', False, False, 4.0),
             L(outline([(56, 0), (82, 18), (86, 70), (62, 88)]), 'skin_d', 'b', False),
             L(quad((14, 40), (50, 50), (86, 82)), OUTC, 'f', False, False, 1.8)],
}

# William Kidd: piel morena, pelo rosa a capas de puntas hasta la nuca y por encima un moño grande verde azulado atado con
# una goma amarilla, del que caen dos mechones por la cara; ojos grandes
CHARS['william-kidd'] = {
    'body': 'chica', 'pal': pal('#c8606a', '#a0703e', iris='#1e1414', teal='#2a7a80', teal_d='#1e5a60', tie='#f0c030'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 100), (4, 110, 1), (8, 90), (4, 60), (8, 26), (24, 6), (50, 0), (76, 6), (92, 26), (96, 60), (92, 90), (96, 110, 1), (90, 100),
                         (84, 66), (16, 66)])),
              L(outline([(30, 14), (24, -10), (36, -26), (54, -22), (62, -36), (74, -26), (70, -4), (76, 10), (60, 18), (44, 16)]), 'teal', 'f'),
              L(ell(30, 8, 4, 3), 'tie', 'f', ln=True), L(ell(72, 14, 4, 3), 'tie', 'f', ln=True),
              fringe([(16, 64), (16, 40), (30, 22), (50, 18), (68, 22), (84, 40), (86, 60), (80, 50), (76, 64, 1), (68, 44), (54, 34), (44, 36), (34, 44),
                      (26, 70, 1), (20, 56)], 'teal'),
              L(outline([(82, 40), (96, 56), (100, 70, 1), (88, 58)]), 'teal', 'f', ln=True)],
    'side': [L(outline([(54, 60), (60, 48), (80, 48), (92, 34), (88, 12), (66, 0), (40, -2), (16, 8), (4, 32), (2, 70), (-6, 98, 1), (12, 86), (16, 104, 1),
                        (26, 84), (34, 100, 1), (42, 80), (48, 70)])),
             L(outline([(30, 6), (26, -16), (40, -28), (60, -22), (72, -8), (68, 8), (50, 12)]), 'teal', 'f'), L(ell(56, 8, 4, 3), 'tie', 'f', ln=True),
             fringe([(70, 6), (90, 18), (94, 40), (92, 64, 1), (86, 48), (80, 34)], 'teal')],
    'back': [L(outline([(10, 100), (4, 110, 1), (8, 86), (4, 60), (8, 26), (24, 6), (50, 0), (76, 6), (92, 26), (96, 60), (92, 86), (96, 110, 1), (84, 100),
                        (70, 108, 1), (60, 96), (50, 108, 1), (40, 96), (30, 108, 1), (20, 98)])),
             L(outline([(56, 2), (88, 20), (96, 60), (92, 96), (66, 100)]), 'shade', 'b', False),
             L(outline([(30, 14), (24, -10), (36, -26), (54, -22), (62, -36), (74, -26), (70, -4), (76, 10), (60, 18), (44, 16)]), 'teal', 'f'),
             L(outline([(26, 14), (8, 36), (4, 60, 1), (16, 44), (30, 24)]), 'teal', 'f'), L(ell(30, 12, 4, 3), 'tie', 'f', ln=True)],
}

# Santelmo Phyre (sin modelo 3D; de su retrato): pelo rojo de pinchos hacia atrás con un moño en lo alto atado con una
# anilla verde, patillas en punta, piel morena y sonrisa
CHARS['santelmo-phyre'] = {
    'body': 'normal', 'pal': pal('#c8281e', '#b88050', iris='#3a1a1a', ring='#2a8a6a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(40, 4), (36, -16), (50, -26), (64, -16), (60, 4)])), L(ell(50, -2, 7, 3.4), 'ring', 'f', ln=True),
              L(outline([(16, 74), (6, 60, 1), (10, 40), (16, 18), (34, 4), (50, 0), (66, 4), (84, 18), (98, 26, 1), (90, 40), (94, 60, 1), (84, 74), (82, 56),
                         (18, 56)])),
              L(outline([(60, 4), (84, 16), (92, 44), (86, 66), (78, 40)]), 'shade', 'b', False),
              fringe([(14, 60), (18, 38), (30, 24), (50, 20), (70, 24), (84, 38), (86, 60), (78, 46), (70, 52, 1), (62, 40), (50, 48, 1), (40, 40), (30, 52, 1),
                      (22, 46)])],
    'side': [L(outline([(36, 6), (30, -14), (44, -26), (58, -18), (54, 4)])), L(ell(46, 0, 7, 3.4), 'ring', 'f', ln=True),
             L(outline([(54, 58), (60, 48), (82, 48), (92, 32), (86, 12), (66, 0), (40, 0), (18, 8), (-6, 14, 1), (6, 28), (-10, 42, 1), (6, 50), (8, 70), (22, 78),
                        (40, 72)])),
             L(outline([(4, 30), (24, 36), (26, 66), (8, 60)]), 'shade', 'b', False),
             fringe([(66, 4), (88, 16), (94, 38), (90, 56, 1), (84, 42), (76, 32)])],
    'back': [L(outline([(40, 4), (36, -16), (50, -26), (64, -16), (60, 4)])),
             L(outline([(16, 80), (4, 64, 1), (10, 40), (16, 18), (34, 4), (50, 0), (66, 4), (84, 18), (96, 26, 1), (90, 40), (96, 64, 1), (84, 80), (64, 90, 1),
                        (50, 82), (36, 90, 1)])),
             L(outline([(56, 4), (84, 16), (92, 50), (84, 76), (62, 84)]), 'shade', 'b', False), L(ell(50, -2, 7, 3.4), 'ring', 'f', ln=True)],
}

# Dakkar Nemo: melena verde azulada larga y lisa peinada hacia atrás desde la frente, con mechones gruesos que se levantan
# arriba y caen por los lados hasta el pecho; cejas finas y media sonrisa
CHARS['dakkar-nemo'] = {
    'body': 'normal', 'pal': pal('#2a8080', '#fcd8b4', iris='#1e1414'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 98, 'hairline': (56, 46)},
    'front': [L(outline([(4, 124), (0, 70), (2, 40), (-6, 20, 1), (8, 16), (20, -4), (36, -12), (50, -8), (64, -12), (80, -4), (92, 16), (106, 20, 1), (98, 40),
                         (100, 70), (96, 124), (84, 124), (84, 70), (16, 70), (16, 124)])),
              L(outline([(60, -8), (86, 4), (96, 40), (94, 120), (84, 120), (82, 50)]), 'shade', 'b', False),
              strand([(30, 0), (32, 30)], 'deep', 'b', 1.0), strand([(50, -6), (50, 30)], 'deep', 'b', 1.0), strand([(70, 0), (68, 30)], 'deep', 'b', 1.0),
              L(outline([(14, 52), (6, 70), (4, 120), (14, 120), (18, 70)]), 'mid', 'f', ln=True),
              L(outline([(86, 52), (94, 70), (96, 120), (86, 120), (82, 70)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(56, 54), (66, 46), (84, 44), (92, 26), (88, 6), (70, -10), (44, -12), (20, -4), (4, 14), (-6, 40), (-10, 90), (-6, 124), (20, 124),
                        (26, 90), (40, 70)])),
             L(outline([(-6, 40), (16, 44), (20, 120), (-6, 120)]), 'shade', 'b', False),
             strand([(30, -6), (60, 0), (80, 10)], 'deep', 'b', 1.0), strand([(20, 6), (50, 12), (74, 24)], 'deep', 'b', 1.0)],
    'back': [L(outline([(2, 124), (-2, 70), (0, 40), (-8, 20, 1), (8, 16), (20, -4), (36, -12), (50, -8), (64, -12), (80, -4), (92, 16), (108, 20, 1), (100, 40),
                        (102, 70), (98, 124)])),
             L(outline([(56, -8), (88, 6), (100, 40), (98, 120), (64, 120)]), 'shade', 'b', False),
             strand([(30, 20), (28, 110)], 'deep', 'b', 1.0), strand([(50, 20), (50, 116)], 'deep', 'b', 1.0), strand([(70, 20), (72, 110)], 'deep', 'b', 1.0)],
}

# Marley Hookson: pelo blanco rosado recogido en una mata ahuecada como un turbante, con dos rizos en espiral que salen por
# un lado, atado con una cinta verde en la frente cuyos extremos cuelgan; ojos grandes
CHARS['marley-hookson'] = {
    'body': 'bajito', 'pal': pal('#e0d4d0', '#fcd8b4', iris='#6a6a20', shade='#bca8a8', band='#2a6a4a', band_d='#1e5038'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(6, 52), (2, 26), (14, 6), (34, -6), (60, -6), (80, 0), (96, -8), (112, -2), (110, 12), (100, 14), (104, 26), (116, 24), (112, 40), (96, 44),
                         (94, 52), (50, 58)])),
              L(outline([(96, -8), (112, -2), (110, 12), (100, 14), (102, 4)]), 'shade', 'b', False),
              strand([(98, 2), (104, 4), (102, 10)], 'deep', 'b', 1.2), strand([(106, 30), (110, 32), (106, 38)], 'deep', 'b', 1.2),
              strand([(30, 8), (40, 20)], 'shade', 'b', 1.2), strand([(54, 4), (62, 18)], 'shade', 'b', 1.2),
              L(outline([(8, 58), (8, 42), (50, 36), (92, 42), (92, 58), (50, 52)]), 'band', 'f', ln=True),
              fringe([(40, 54), (50, 52), (60, 54), (56, 64), (50, 74, 1), (44, 64)]),
              L(outline([(12, 58), (8, 90), (16, 92), (18, 60)]), 'band_d', 'f', ln=True)],
    'side': [L(outline([(4, 54), (0, 26), (14, 2), (30, -14), (40, -26), (52, -30), (58, -20), (52, -14), (60, -8), (82, 2), (94, 22), (94, 48), (50, 56)])),
             strand([(46, -22), (52, -24), (50, -16)], 'deep', 'b', 1.2),
             L(outline([(4, 56), (2, 40), (50, 34), (96, 40), (96, 54), (50, 50)]), 'band', 'f', ln=True),
             L(outline([(10, 52), (-10, 64), (-18, 84, 1), (-2, 76), (8, 92, 1), (18, 60)]), 'band_d', 'f', ln=True)],
    'back': [L(outline([(6, 58), (2, 26), (14, 6), (34, -6), (60, -6), (80, 0), (94, 26), (94, 58), (50, 64)])),
             L(outline([(10, 4), (-8, -8), (-14, 6), (-6, 18), (6, 18)])), L(outline([(56, -4), (86, 8), (94, 40), (90, 56), (60, 60)]), 'shade', 'b', False),
             L(outline([(4, 60), (4, 44), (50, 40), (96, 44), (96, 60), (50, 56)]), 'band', 'f', ln=True)],
}

# Davy Jones: pelo azul grisáceo de pinchos largos hacia arriba y atrás con mechones en punta que le caen a los lados de la
# cara, una cinta azul fina en la frente y una cicatriz en la mejilla
CHARS['davy-jones'] = {
    'body': 'normal', 'pal': pal('#4a6080', '#f6d0a8', iris='#6a3a1a', band='#2a4ab8', scar='#a05a3a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 116), (-6, 112, 1), (8, 96), (6, 60), (14, 20), (20, -6, 1), (34, 6), (50, -30, 1), (66, 6), (80, -6, 1), (86, 20), (94, 60), (92, 96),
                         (106, 112, 1), (88, 116), (84, 70), (16, 70)])),
              L(outline([(56, -6), (82, 6), (92, 56), (90, 100), (80, 60)]), 'shade', 'b', False),
              fringe([(14, 64), (16, 40), (30, 24), (50, 18), (70, 24), (84, 40), (86, 64), (80, 52), (72, 62, 1), (66, 44), (56, 56, 1), (50, 40), (40, 70, 1),
                      (32, 46), (22, 60, 1)]),
              L(outline([(10, 50), (50, 42), (90, 50), (90, 54), (50, 46), (10, 54)]), 'band', 'f', False),
              L([(64, 66), (60, 76), (66, 84)], 'scar', 'f', False, False, 1.4)],
    'side': [L(outline([(58, 56), (66, 46), (84, 44), (94, 30), (96, 8, 1), (78, 10), (70, -8), (50, -16), (20, -22), (-16, -14, 1), (2, 6), (-6, 30), (2, 56),
                        (-6, 92, 1), (14, 80), (24, 100, 1), (34, 80), (46, 70)])),
             L(outline([(0, 30), (22, 36), (26, 74), (6, 70)]), 'shade', 'b', False),
             L(outline([(4, 46), (50, 40), (94, 44), (94, 48), (50, 44), (4, 50)]), 'band', 'f', False),
             fringe([(70, 8), (92, 20), (96, 42), (92, 60, 1), (86, 46), (78, 34)])],
    'back': [L(outline([(10, 112), (-8, 110, 1), (6, 92), (4, 60), (14, 20), (24, -10, 1), (36, 6), (50, -30, 1), (64, 6), (76, -10, 1), (86, 20), (96, 60), (94, 92),
                        (108, 110, 1), (90, 112), (70, 100, 1), (60, 88), (50, 100, 1), (40, 88), (30, 100, 1)])),
             L(outline([(56, -10), (86, 16), (96, 60), (92, 104), (66, 96)]), 'shade', 'b', False),
             L(outline([(6, 48), (50, 44), (94, 48), (94, 52), (50, 48), (6, 52)]), 'band', 'f', False)],
}

# Calico Corsair: melena azul marino oscuro lisa hasta la mandíbula con las puntas abiertas, un flequillo de lado que se
# levanta a un lado y un mechón rojo en medio de la frente; cejas fruncidas
CHARS['calico-corsair'] = {
    'body': 'normal', 'pal': pal('#2a3448', '#fcd8b4', iris='#1e1414', red='#c83a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 104), (2, 112, 1), (6, 92), (4, 60), (10, 24), (28, 4), (50, -2), (72, 4), (90, 24), (96, 50), (110, 60, 1), (96, 66), (96, 92),
                         (100, 112, 1), (88, 104), (84, 66), (16, 66)])),
              L(outline([(60, 2), (86, 18), (96, 50), (94, 96), (84, 60)]), 'shade', 'b', False),
              fringe([(12, 70), (12, 40), (26, 20), (50, 12), (74, 20), (86, 36), (100, 46, 1), (88, 48), (84, 56), (76, 48), (66, 54, 1), (60, 40), (52, 54, 1),
                      (40, 36), (30, 50), (22, 70, 1)]),
              L(outline([(44, 20), (52, 18), (56, 50), (50, 62, 1), (46, 48)]), 'red', 'f', ln=True)],
    'side': [L(outline([(54, 62), (60, 50), (82, 50), (94, 36), (90, 14), (70, 0), (44, -4), (20, 4), (4, 28), (0, 70), (-12, 96, 1), (8, 86), (6, 108, 1), (22, 92),
                        (30, 106, 1), (40, 86), (48, 74)])),
             L(outline([(2, 40), (24, 44), (32, 92), (6, 92)]), 'shade', 'b', False),
             L(outline([(76, 10), (86, 14), (92, 40), (86, 50)]), 'red', 'f', ln=True),
             fringe([(64, 2), (90, 16), (96, 42), (94, 62, 1), (86, 50), (80, 40)])],
    'back': [L(outline([(10, 104), (-2, 112, 1), (4, 90), (2, 60), (10, 24), (28, 4), (50, -2), (72, 4), (90, 24), (98, 60), (96, 90), (102, 112, 1), (88, 104),
                        (72, 112, 1), (62, 100), (50, 112, 1), (40, 100), (28, 112, 1), (20, 102)])),
             L(outline([(56, 2), (88, 20), (98, 60), (96, 100), (66, 104)]), 'shade', 'b', False)],
}

# Rob Crusoe: pelo verde oliva de mechones gruesos en punta que se abren hacia los lados, con uno que le cae entre los ojos
CHARS['rob-crusoe'] = {
    'body': 'normal', 'pal': pal('#5a6a14', '#fcd8b4', iris='#1e1414'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 92), (-10, 88, 1), (6, 72), (-16, 60, 1), (6, 50), (2, 26), (-6, 12, 1), (14, 12), (26, -4), (40, -10), (50, -24, 1), (58, -8),
                         (74, -6), (90, 10), (106, 8, 1), (98, 26), (96, 50), (116, 60, 1), (94, 72), (110, 88, 1), (86, 92), (84, 66), (16, 66)])),
              L(outline([(60, -6), (88, 10), (96, 46), (92, 84), (82, 50)]), 'shade', 'b', False),
              fringe([(12, 70), (14, 40), (28, 22), (50, 16), (72, 22), (86, 40), (88, 70), (80, 56), (72, 66, 1), (66, 48), (56, 56), (50, 86, 1), (46, 52),
                      (36, 48), (28, 66, 1), (20, 56)])],
    'side': [L(outline([(56, 60), (62, 48), (82, 48), (94, 32), (90, 12), (98, 2, 1), (76, 0), (62, -16, 1), (50, -4), (24, -6), (8, 10), (-12, 18, 1), (2, 30),
                        (-6, 60), (-20, 70, 1), (-2, 76), (6, 94, 1), (20, 82), (34, 90), (46, 76)])),
             L(outline([(0, 34), (22, 40), (28, 80), (4, 76)]), 'shade', 'b', False),
             fringe([(66, 4), (90, 18), (96, 42), (94, 66, 1), (86, 50), (80, 62, 1), (76, 42)])],
    'back': [L(outline([(14, 92), (-14, 86, 1), (4, 72), (-18, 58, 1), (4, 50), (2, 26), (-8, 12, 1), (14, 12), (26, -4), (40, -10), (50, -24, 1), (58, -8),
                        (74, -6), (90, 10), (108, 10, 1), (98, 26), (96, 50), (118, 58, 1), (96, 72), (114, 86, 1), (86, 92), (64, 96), (50, 106, 1), (36, 96)])),
             L(outline([(56, -6), (90, 10), (98, 50), (92, 88), (62, 94)]), 'shade', 'b', False),
             strand([(40, 70), (50, 76), (60, 70)], 'deep', 'b', 1.0)],
}

# Nick Tofobia (portero suplente): pelo negro verdoso en casco redondo con flequillo recto y dos mechones largos en punta que
# le caen por delante hasta el pecho; cara redonda morena y ojos amarillos saltones con la pupila pequeña
CHARS['nick-tofobia'] = {
    'body': 'corpulento', 'pal': pal('#1e2a2e', '#a8784a', iris='#1e1414', ring='#e0b020'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': False, 'face_front': WIDE_FACE},
    'front': [L(outline([(10, 80), (2, 50), (6, 20), (24, 0), (50, -6), (76, 0), (94, 20), (98, 50), (90, 80), (84, 60), (16, 60)])),
              L(outline([(60, -2), (86, 14), (96, 46), (90, 70), (80, 40)]), 'shade', 'b', False),
              fringe([(10, 64), (10, 40), (24, 18), (50, 10), (76, 18), (90, 40), (90, 64), (82, 62), (82, 56), (18, 56), (18, 62)]),
              L(outline([(14, 60), (6, 90), (2, 124, 1), (16, 100), (22, 70)]), 'mid', 'f'), L(outline([(86, 60), (94, 90), (98, 124, 1), (84, 100), (78, 70)]), 'mid', 'f'),
              L(ell(36, 70, 8, 7), 'ring', 'f', ln=True), L(ell(64, 70, 8, 7), 'ring', 'f', ln=True)]
             + white_eyes(70, 14, 5.4, 4.6, 1.4),
    'side': [L(outline([(54, 58), (60, 46), (84, 46), (94, 30), (88, 8), (66, -4), (38, -4), (14, 6), (2, 30), (2, 60), (14, 80), (36, 82), (46, 70)])),
             L(outline([(2, 30), (24, 36), (26, 74), (6, 68)]), 'shade', 'b', False),
             L(outline([(68, 56), (84, 90), (92, 116, 1), (76, 96), (62, 64)]), 'mid', 'f'),
             fringe([(66, 2), (92, 18), (96, 40), (94, 56), (84, 54), (78, 40)]),
             L(ell(86, 68, 4.6, 6.4), 'ring', 'f', ln=True)] + side_eye(68),
    'back': [L(outline([(6, 84), (-4, 56), (2, 22), (22, 0), (50, -6), (78, 0), (98, 22), (104, 56), (94, 84), (70, 88), (50, 80), (30, 88)])),
             L(outline([(56, -2), (88, 14), (100, 50), (92, 82), (68, 86)]), 'shade', 'b', False),
             L(outline([(16, 76), (12, 100), (18, 112, 1), (24, 92), (26, 80)]), 'mid', 'f'), L(outline([(84, 76), (88, 100), (82, 112, 1), (76, 92), (74, 80)]), 'mid', 'f')],
}

# Bart Black: melena naranja lisa recogida en una coleta alta que sale tiesa de lo alto con una anilla dorada; dos mechones
# largos le enmarcan la cara y uno en pico en la frente; ojos blancos de enfado
CHARS['bart-black'] = {
    'body': 'normal', 'pal': pal('#e0601e', '#f8d0a8', iris='#1e1414', ring='#d8a020'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(36, 6), (30, -24), (40, -34), (50, -30), (60, -34), (70, -24), (64, 6)])), L(outline([(36, 4), (64, 4), (62, 12), (38, 12)]), 'ring', 'f', ln=True),
              L(outline([(14, 70), (12, 36), (24, 14), (50, 8), (76, 14), (88, 36), (86, 70)])),
              L(outline([(60, 12), (82, 22), (88, 46), (84, 68), (76, 40)]), 'shade', 'b', False),
              L(outline([(18, 40), (12, 70), (12, 112, 1), (22, 90), (24, 54)]), 'mid', 'f', ln=True),
              L(outline([(82, 40), (88, 70), (88, 112, 1), (78, 90), (76, 54)]), 'mid', 'f', ln=True),
              fringe([(22, 46), (34, 30), (50, 26), (66, 30), (78, 46), (64, 44), (56, 50), (50, 66, 1), (44, 50), (36, 44)])],
    'side': [L(outline([(34, 8), (30, -22), (44, -32), (58, -26), (56, 6)])), L(outline([(32, 6), (58, 4), (58, 14), (34, 14)]), 'ring', 'f', ln=True),
             L(outline([(54, 58), (60, 46), (82, 44), (92, 30), (86, 10), (64, 2), (36, 4), (14, 14), (4, 38), (6, 70), (16, 100), (22, 112, 1), (30, 90), (44, 76)])),
             L(outline([(4, 36), (24, 42), (28, 92), (12, 90)]), 'shade', 'b', False),
             fringe([(68, 6), (90, 18), (94, 40), (86, 70), (84, 104, 1), (80, 70), (76, 36)])],
    'back': [L(outline([(36, 6), (30, -24), (40, -34), (50, -30), (60, -34), (70, -24), (64, 6)])),
             L(outline([(12, 104), (10, 36), (24, 14), (50, 8), (76, 14), (90, 36), (88, 104), (70, 96), (50, 100), (30, 96)])),
             L(outline([(56, 12), (82, 22), (90, 50), (86, 100), (64, 96)]), 'shade', 'b', False),
             strand([(30, 30), (30, 94)], 'deep', 'b', 1.0), strand([(50, 20), (50, 96)], 'deep', 'b', 1.0), strand([(70, 30), (70, 94)], 'deep', 'b', 1.0),
             L(outline([(36, 4), (64, 4), (62, 12), (38, 12)]), 'ring', 'f', ln=True)],
}

# Frank Drake: un sombrero de pescador verde oliva enorme, de ala ancha y caída en ondas, con una cinta de dos tonos de
# marrón, calado hasta la nariz: solo se le ve la boca seria
CHARS['frank-drake'] = {
    'body': 'normal', 'pal': pal('#1e1e1e', '#fce0c4', iris='#1e1414', hat='#3e5228', hat_d='#2c3c1c', hat_l='#56703a', band='#b88a50', band_d='#8a6038'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(-12, 74), (-16, 54), (4, 48), (8, 30), (18, 6), (50, -4), (82, 6), (92, 30), (96, 48), (116, 54), (112, 74), (98, 76), (92, 88), (78, 82),
                         (64, 90), (50, 84), (36, 90), (22, 82), (8, 88), (2, 76)]), 'hat', 'f'),
              L(outline([(10, 44), (14, 30), (50, 24), (86, 30), (90, 44), (50, 40)]), 'band', 'f', ln=True),
              L(outline([(12, 36), (50, 30), (88, 36), (88, 40), (50, 34), (12, 40)]), 'band_d', 'f', False),
              L(outline([(-10, 60), (110, 60), (100, 72), (0, 72)]), 'hat_d', 'f', False), L(ell(40, 12, 10, 5), 'hat_l', 'f', False)],
    'side': [L(outline([(-24, 70), (-20, 52), (4, 46), (8, 26), (20, 6), (50, -4), (78, 4), (90, 26), (94, 46), (118, 42), (112, 58), (94, 66), (90, 82), (72, 80),
                        (54, 88), (30, 80), (14, 86), (2, 74)]), 'hat', 'f'),
             L(outline([(6, 42), (8, 28), (50, 22), (90, 28), (92, 42), (50, 38)]), 'band', 'f', ln=True),
             L(outline([(-20, 60), (110, 52), (94, 66), (0, 72)]), 'hat_d', 'f', False)],
    'back': [L(outline([(-12, 70), (-16, 52), (4, 46), (8, 28), (18, 6), (50, -4), (82, 6), (92, 28), (96, 46), (116, 52), (112, 70), (96, 76), (90, 90), (72, 84),
                        (50, 92), (28, 84), (10, 90), (4, 76)]), 'hat', 'f'),
             L(outline([(10, 42), (14, 28), (50, 22), (86, 28), (90, 42), (50, 38)]), 'band', 'f', ln=True),
             L(outline([(-10, 58), (110, 58), (100, 72), (0, 72)]), 'hat_d', 'f', False)],
}

# Barnabas Rossa: pelo castaño rojizo como una capucha que le enmarca la cara en pico, con dos mechones larguísimos que se
# alzan como orejas de conejo; ojos verdes y cejas fruncidas
CHARS['barnabas-rossa'] = {
    'body': 'normal', 'pal': pal('#8a4a30', '#fcd8b4', iris='#3a8a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(18, 20), (10, -40), (16, -60, 1), (24, -36), (30, -64, 1), (34, -30), (36, 10)])),
              L(outline([(82, 20), (90, -40), (84, -60, 1), (76, -36), (70, -64, 1), (66, -30), (64, 10)])),
              L(outline([(8, 108), (2, 60), (8, 24), (28, 4), (50, 0), (72, 4), (92, 24), (98, 60), (92, 108), (84, 104), (82, 62), (18, 62), (16, 104)])),
              L(outline([(60, 4), (86, 18), (96, 56), (90, 104), (82, 60)]), 'shade', 'b', False),
              fringe([(14, 66), (14, 40), (28, 22), (50, 16), (72, 22), (86, 40), (86, 66), (74, 52), (60, 50), (50, 66, 1), (40, 50), (26, 52)]),
              L(outline([(30, 24), (46, 18), (40, 30)]), 'light', 'f', False)],
    'side': [L(outline([(40, 10), (24, -40), (20, -64, 1), (36, -40), (50, -60, 1), (52, -30), (56, 6)])),
             L(outline([(54, 62), (60, 50), (80, 50), (92, 34), (88, 12), (66, 0), (40, 0), (16, 10), (4, 36), (2, 72), (14, 100), (36, 108), (46, 90), (50, 74)])),
             L(outline([(4, 40), (24, 44), (30, 100), (8, 92)]), 'shade', 'b', False),
             fringe([(66, 4), (90, 18), (96, 42), (94, 66, 1), (86, 52), (80, 40)])],
    'back': [L(outline([(18, 20), (10, -40), (16, -60, 1), (24, -36), (30, -64, 1), (34, -30), (36, 10)])),
             L(outline([(82, 20), (90, -40), (84, -60, 1), (76, -36), (70, -64, 1), (66, -30), (64, 10)])),
             L(outline([(8, 104), (2, 60), (8, 24), (28, 4), (50, 0), (72, 4), (92, 24), (98, 60), (92, 104), (50, 110)])),
             L(outline([(56, 4), (86, 18), (98, 56), (92, 100), (64, 106)]), 'shade', 'b', False),
             L(ell(50, 30, 16, 12), 'light', 'b', False)],
}
