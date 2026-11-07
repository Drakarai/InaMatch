"""Zanark Domain (cs-zanark-domain): sus modelos 3D de Inazuma Eleven GO 2: Chrono Stone como referencia (busto de frente,
perfil y espalda). Zanark Avalonic está en chars_cs_zan.py."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Eka (portero): pelo rubio claro de pinchos que se abren a los lados como cuernos, flequillo de mechones, orejas de elfo
# y piel morena; ojos ámbar afilados
CHARS['eka'] = {
    'body': 'normal', 'pal': pal('#f0e0a8', '#a87850', iris='#d8901e', shade='#d0b880'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False, 'big_ears': 2, 'ear_out': 6},
    'front': [L(outline([(14, 66), (-14, 30, 1), (8, 24), (14, 4), (30, -2), (40, -24, 1), (50, -4), (62, -2), (74, -26, 1), (78, 2), (90, 20), (114, 26, 1), (88, 40),
                         (86, 66), (80, 52), (20, 52)])),
              L(outline([(60, 0), (84, 12), (94, 36), (88, 60), (78, 40)]), 'shade', 'b', False),
              fringe([(14, 64), (16, 40), (30, 24), (50, 18), (70, 24), (84, 40), (86, 64), (78, 52), (72, 60, 1), (64, 46), (56, 62, 1), (50, 44), (44, 62, 1), (36, 46),
                      (28, 60, 1), (22, 50)])],
    'side': [L(outline([(54, 56), (62, 44), (82, 44), (92, 30), (86, 10), (90, -10, 1), (70, 0), (56, -18, 1), (44, 0), (22, 4), (6, 20), (-18, 22, 1), (4, 36), (4, 58),
                        (16, 74), (32, 72), (46, 64)])),
             L(outline([(6, 34), (26, 40), (26, 66), (10, 60)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 16), (94, 40), (90, 62, 1), (84, 46), (76, 34)])],
    'back': [L(outline([(16, 80), (-14, 32, 1), (8, 26), (14, 4), (30, -2), (40, -24, 1), (50, -4), (62, -2), (74, -26, 1), (78, 2), (90, 20), (114, 28, 1), (90, 40),
                        (84, 80), (50, 88)])),
             L(outline([(56, 0), (86, 14), (92, 46), (84, 78), (62, 86)]), 'shade', 'b', False),
             strand([(30, 10), (32, 80)], 'shade', 'b', 1.0), strand([(50, 4), (50, 86)], 'shade', 'b', 1.0), strand([(70, 10), (68, 80)], 'shade', 'b', 1.0)],
}

# Dva: pelo morado negruzco en un tupé plano altísimo, como una mesa, con los lados rapados en rosa claro; dos lunares
# negros en la frente sobre unas gafas pintadas y dos lazos blancos atados en la nuca
CHARS['dva'] = {
    'body': 'normal', 'pal': pal('#2e2236', '#b07a4c', iris='#1e1414', buzz='#e8c8c8', bow='#f0dcdc', knot='#2a8a4a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 70), (14, 40), (24, 26), (76, 26), (86, 40), (84, 70), (78, 60), (22, 60)]), 'buzz'),
              L(outline([(14, 34), (-6, -6), (106, -6), (86, 34), (50, 30)]), 'mid', 'f', ln=True),
              L(outline([(60, -4), (104, -4), (86, 30), (70, 28)]), 'shade', 'f', False),
              strand([(20, 0), (30, 30)], 'deep', 'f', 1.0), strand([(40, -4), (44, 30)], 'deep', 'f', 1.0), strand([(60, -4), (58, 30)], 'deep', 'f', 1.0),
              strand([(80, 0), (72, 30)], 'deep', 'f', 1.0),
              L(ell(34, 58, 3.4, 3.4), OUTC, 'f', False), L(ell(66, 58, 3.4, 3.4), OUTC, 'f', False),
              L(outline([(24, 70), (44, 70), (46, 78), (26, 78)]), WHITE, 'f', ln=True), L(outline([(76, 70), (56, 70), (54, 78), (74, 78)]), WHITE, 'f', ln=True),
              L([(46, 74), (54, 74)], OUTC, 'f', False, False, 1.6),
              L(outline([(16, 88), (4, 84), (6, 100), (16, 96)]), 'bow', 'b', ln=True), L(outline([(84, 88), (96, 84), (94, 100), (84, 96)]), 'bow', 'b', ln=True)],
    'side': [L(outline([(60, 40), (60, 70), (44, 92), (20, 92), (8, 70), (10, 36)]), 'buzz'),
             L(outline([(4, 40), (-6, -6), (104, -6), (90, 30), (60, 40), (30, 40)]), 'mid', 'f', ln=True),
             L(outline([(4, 38), (-4, 0), (40, -4), (30, 38)]), 'shade', 'f', False),
             L(outline([(16, 86), (-8, 80), (-4, 98), (10, 94)]), 'bow', 'f', ln=True), L(ell(18, 88, 3.4, 3.4), 'knot', 'f', ln=True)],
    'back': [L(outline([(14, 40), (86, 40), (86, 70), (72, 92), (28, 92), (14, 70)]), 'buzz'),
             L(outline([(12, 44), (-6, -6), (106, -6), (88, 44), (50, 40)]), 'mid', 'f', ln=True),
             L(outline([(58, -4), (104, -4), (88, 42), (64, 40)]), 'shade', 'f', False),
             L(outline([(30, 86), (6, 82), (10, 100), (28, 94)]), 'bow', 'f', ln=True), L(outline([(70, 86), (94, 82), (90, 100), (72, 94)]), 'bow', 'f', ln=True),
             L(ell(34, 88, 3.4, 3.4), 'knot', 'f', ln=True), L(ell(46, 90, 3.4, 3.4), 'knot', 'f', ln=True), L(ell(54, 90, 3.4, 3.4), 'knot', 'f', ln=True),
             L(ell(66, 88, 3.4, 3.4), 'knot', 'f', ln=True)],
}

# Tyrah: melena azul marino oscuro con dos alas de murciélago a los lados de la cabeza y mechones largos que caen por
# delante; tres puntos en la frente, ojos rojos y mejillas sonrosadas
CHARS['tyrah'] = {
    'body': 'chica', 'pal': pal('#1e2448', '#fcd8b0', iris='#c81e24', blush='#f4a8a0'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 70), (8, 40), (0, 24), (-22, 26), (-4, 16), (-24, -2, 1), (6, 4), (24, -6), (36, -16, 1), (50, -2), (64, -16, 1), (76, -6), (94, 4),
                         (124, -2, 1), (104, 16), (122, 26), (100, 24), (92, 40), (86, 70)])),
              L(outline([(60, 0), (90, 10), (110, 18), (90, 34), (90, 66), (80, 40)]), 'shade', 'b', False),
              fringe([(12, 62), (14, 38), (28, 18), (50, 10), (72, 18), (86, 38), (88, 62), (80, 52), (78, 64), (74, 76), (70, 50), (58, 38), (50, 30), (42, 38), (30, 50),
                      (26, 76), (22, 64), (20, 52)]),
              L(outline([(16, 66), (12, 96), (14, 118, 1), (22, 96), (24, 70)]), 'mid', 'f'), L(outline([(84, 66), (88, 96), (86, 118, 1), (78, 96), (76, 70)]), 'mid', 'f'),
              L(ell(50, 56, 2, 2), OUTC, 'f', False), L(ell(44, 60, 1.6, 1.6), OUTC, 'f', False), L(ell(56, 60, 1.6, 1.6), OUTC, 'f', False),
              L(ell(30, 88, 4.4, 2.4), 'blush', 'f', False), L(ell(70, 88, 4.4, 2.4), 'blush', 'f', False)],
    'side': [L(outline([(54, 62), (60, 48), (80, 46), (92, 32), (86, 10), (70, -2), (60, -24, 1), (50, -4), (30, 0), (12, 14), (-14, 16), (4, 30), (2, 60), (6, 100),
                        (12, 120, 1), (20, 96), (30, 76), (44, 72)])),
             L(outline([(4, 34), (26, 40), (28, 80), (10, 90)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 16), (94, 40), (90, 64), (84, 110, 1), (80, 70), (76, 40)])],
    'back': [L(outline([(14, 70), (8, 40), (0, 24), (-22, 26), (-4, 16), (-24, -2, 1), (6, 4), (24, -6), (36, -16, 1), (50, -2), (64, -16, 1), (76, -6), (94, 4),
                        (124, -2, 1), (104, 16), (122, 26), (100, 24), (92, 40), (86, 70), (84, 100), (78, 120, 1), (72, 96), (28, 96), (22, 120, 1), (16, 100)])),
             L(outline([(56, 0), (92, 10), (110, 18), (92, 34), (88, 100), (70, 96)]), 'shade', 'b', False),
             strand([(50, 4), (50, 90)], 'deep', 'b', 1.0)],
}

# Catvari: grandullón gordo de cara ancha y orejas puntiagudas; pelo verde oscuro grisáceo peinado hacia atrás que le cae
# en una mata por la nuca, una cicatriz roja en círculo en la cara, un ojo amarillo y dientes afilados
CHARS['catvari'] = {
    'body': 'corpulento', 'pal': pal('#2e4440', '#f4dcc0', iris='#e8c01e', scar='#a82a1e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 102, 'hairline': False, 'big_ears': 3, 'ear_out': 10,
             'face_front': blob([(4, 50), (50, 40), (96, 50), (104, 80), (96, 108), (70, 120), (30, 120), (4, 108), (-4, 80)])},
    'front': [L(outline([(10, 56), (14, 28), (30, 14), (50, 10), (70, 14), (86, 28), (90, 56), (70, 44), (50, 48), (30, 44)])),
              strand([(30, 20), (36, 40)], 'deep', 'b', 1.0), strand([(50, 14), (50, 40)], 'deep', 'b', 1.0), strand([(70, 20), (64, 40)], 'deep', 'b', 1.0),
              L(ell(50, 92, 22, 16) + [ell(50, 92, 22, 16)[0]], 'scar', 'f', False, False, 2.0)],
    'side': [L(outline([(58, 40), (50, 20), (30, 12), (6, 20), (-10, 40), (-16, 70), (-22, 96), (0, 100), (20, 90), (30, 60), (50, 50)])),
             L(outline([(-10, 50), (14, 54), (16, 90), (-14, 94)]), 'shade', 'b', False),
             L([(78, 70), (84, 86), (76, 100)], 'scar', 'f', False, False, 2.0)],
    'back': [L(outline([(-4, 100), (-10, 70), (0, 40), (14, 20), (50, 10), (86, 20), (100, 40), (110, 70), (104, 100), (50, 108)])),
             L(outline([(56, 12), (88, 22), (106, 60), (100, 100), (64, 104)]), 'shade', 'b', False),
             strand([(20, 40), (14, 96)], 'deep', 'b', 1.0), strand([(50, 14), (50, 100)], 'deep', 'b', 1.0), strand([(80, 40), (86, 96)], 'deep', 'b', 1.0)],
}

# Panca: pelo azul en ondas gruesas que caen por un lado y se rizan por detrás, y un casco gris de máquina con tres lentes
# negras de rayas rojas que le tapa la cara
CHARS['panca'] = {
    'body': 'normal', 'pal': pal('#4a5cb8', '#f2c8a0', iris='#1e1414', helm='#5a5a60', helm_d='#3a3a40', lens='#1a1a1e', red='#e01e24'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': [L(outline([(6, 40), (14, 10), (40, -10), (70, -6), (92, 6), (100, 30), (104, 64), (112, 96), (96, 104), (90, 80), (86, 52), (60, 34), (40, 30)])),
              L(outline([(64, -2), (92, 10), (102, 50), (108, 90), (94, 92)]), 'shade', 'b', False),
              L(outline([(10, 44), (30, 36), (86, 40), (90, 100), (70, 110), (30, 110), (10, 100)]), 'helm', 'f', ln=True),
              L(outline([(60, 40), (86, 42), (88, 98), (70, 106)]), 'helm_d', 'f', False),
              L(ell(50, 58, 10, 10), 'lens', 'f', ln=True), L(ell(32, 88, 10, 10), 'lens', 'f', ln=True), L(ell(68, 88, 10, 10), 'lens', 'f', ln=True),
              L([(42, 58), (58, 58)], 'red', 'f', False, False, 2.0), L([(24, 88), (40, 88)], 'red', 'f', False, False, 2.0),
              L([(60, 88), (76, 88)], 'red', 'f', False, False, 2.0),
              L(outline([(62, 8), (80, 18), (86, 46), (76, 70), (84, 100), (72, 104), (66, 70), (70, 40), (56, 22)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(60, 40), (50, 0), (30, -12), (60, -14), (80, -6), (82, 20), (70, 10), (60, 40)])),
             L(outline([(46, 30), (20, 10), (0, 30), (-6, 70), (-10, 100), (6, 114), (16, 100), (14, 70), (28, 50)])),
             L(outline([(-6, 50), (10, 56), (12, 96), (-6, 98)]), 'shade', 'b', False),
             L(outline([(40, 40), (94, 40), (100, 70), (94, 104), (40, 100)]), 'helm', 'f', ln=True),
             L(ell(64, 70, 12, 12), 'red', 'f', ln=True), L(ell(64, 70, 7, 7), 'lens', 'f', ln=True), L(ell(64, 70, 3, 3), 'red', 'f', False),
             L(outline([(86, 56), (100, 56), (100, 86), (86, 86)]), 'lens', 'f', ln=True)],
    'back': [L(outline([(0, 100), (-6, 60), (4, 24), (20, 2), (50, -10), (80, -6), (100, 10), (110, 40), (100, 70), (110, 100), (90, 116), (50, 110), (10, 116)])),
             L(outline([(56, -6), (96, 14), (104, 60), (100, 108), (64, 108)]), 'shade', 'b', False),
             L(outline([(86, 40), (100, 40), (102, 70), (88, 70)]), 'helm', 'f', ln=True),
             strand([(20, 30), (30, 60), (20, 100)], 'deep', 'b', 1.0), strand([(60, 20), (50, 60), (60, 100)], 'deep', 'b', 1.0)],
}

# Sas: melena larga verde muy oscuro con un flequillo espeso que le tapa los ojos, que cae lisa por los lados y se abre en
# puntas hacia fuera a la altura de los hombros
CHARS['sas'] = {
    'body': 'delgado', 'pal': pal('#163a34', '#f4d8bc', iris='#1e1414'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(12, 96), (-10, 112, 1), (2, 90), (4, 50), (14, 14), (50, 0), (86, 14), (96, 50), (98, 90), (110, 112, 1), (88, 96), (82, 70), (18, 70)])),
              L(outline([(60, 4), (86, 16), (96, 50), (96, 96), (84, 70)]), 'shade', 'b', False),
              fringe([(12, 80), (10, 44), (22, 16), (50, 6), (78, 16), (90, 44), (88, 80), (78, 80), (70, 84), (50, 86), (30, 84), (22, 80)]),
              L(outline([(56, 12), (78, 20), (86, 48), (80, 76), (70, 50)]), 'shade', 'f', False)],
    'side': [L(outline([(56, 70), (58, 52), (82, 52), (94, 34), (88, 12), (66, 0), (38, 0), (16, 12), (4, 40), (0, 80), (-8, 112, 1), (16, 100), (36, 100), (50, 90)])),
             L(outline([(4, 40), (28, 46), (34, 96), (6, 100)]), 'shade', 'b', False),
             fringe([(62, 2), (88, 14), (96, 40), (94, 84), (82, 84), (76, 40), (66, 26)])],
    'back': [L(outline([(12, 100), (-12, 114, 1), (2, 90), (4, 50), (14, 14), (50, 0), (86, 14), (96, 50), (98, 90), (112, 114, 1), (88, 100), (50, 106)])),
             L(outline([(56, 4), (86, 16), (96, 50), (98, 100), (64, 104)]), 'shade', 'b', False)],
}

# Sapta: pelo negro recogido en un moño alto del que salen tres mechones rizados como cuernos, sujetos con anillas
# doradas, y dos rizos finos que le caen junto a la cara; orejas de elfo y ojos verdes
CHARS['sapta'] = {
    'body': 'chica', 'pal': pal('#1a1a1e', '#fce4c8', iris='#2a9a9a', gold='#f2c41e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False, 'big_ears': 2, 'ear_out': 8},
    'front': [L(quad((36, 10), (20, -10), (4, -16)) + quad((4, -16), (10, -24), (18, -18))[1:], 'mid', 'b', False, False, 6.5),
              L(quad((50, 6), (50, -14), (44, -30)) + quad((44, -30), (52, -36), (58, -30))[1:], 'mid', 'b', False, False, 6.5),
              L(quad((64, 10), (80, -10), (96, -16)) + quad((96, -16), (90, -24), (82, -18))[1:], 'mid', 'b', False, False, 6.5),
              L(outline([(16, 64), (12, 36), (24, 12), (50, 4), (76, 12), (88, 36), (84, 64), (78, 46), (64, 40), (50, 50, 1), (36, 40), (22, 46)])),
              L(outline([(28, 8), (36, 2), (38, 10), (30, 14)]), 'gold', 'f', ln=True), L(outline([(46, 2), (54, 2), (54, 10), (46, 10)]), 'gold', 'f', ln=True),
              L(outline([(72, 8), (64, 2), (62, 10), (70, 14)]), 'gold', 'f', ln=True),
              L(quad((18, 60), (10, 80), (18, 100)), 'mid', 'f', False, False, 2.4), L(quad((82, 60), (90, 80), (82, 100)), 'mid', 'f', False, False, 2.4)],
    'side': [L(outline([(54, 58), (62, 46), (82, 44), (92, 30), (84, 10), (62, 0), (36, 2), (16, 16), (8, 40), (10, 70), (24, 86), (40, 80)])),
             L(quad((40, 4), (30, -24), (10, -30)), 'mid', 'b', False, False, 7.0), L(quad((10, -30), (2, -40), (12, -46)), 'mid', 'b', False, False, 6.5),
             L(quad((48, 2), (54, -24), (70, -34)), 'mid', 'b', False, False, 6.5),
             L(outline([(36, 0), (46, -4), (48, 8), (38, 10)]), 'gold', 'f', ln=True),
             L(quad((54, 60), (48, 84), (56, 98)), 'mid', 'f', False, False, 2.4)],
    'back': [L(quad((40, 14), (20, -10), (4, -16)), 'mid', 'b', False, False, 7.0), L(quad((50, 10), (50, -14), (44, -30)), 'mid', 'b', False, False, 7.0),
             L(quad((60, 14), (80, -10), (96, -16)), 'mid', 'b', False, False, 7.0),
             L(outline([(16, 80), (12, 36), (24, 12), (50, 4), (76, 12), (88, 36), (84, 80), (50, 88)])),
             L(outline([(56, 6), (82, 16), (90, 50), (84, 78), (62, 86)]), 'shade', 'b', False),
             L(outline([(40, 8), (60, 8), (58, 16), (42, 16)]), 'gold', 'f', ln=True),
             L(quad((18, 76), (12, 90), (18, 104)), 'mid', 'f', False, False, 2.4), L(quad((82, 76), (88, 90), (82, 104)), 'mid', 'f', False, False, 2.4)],
}

# Asta: pelo rubio dorado de pinchos que se echan hacia la derecha y atrás, con un rayo azul pintado en la cara sobre el
# ojo; piel morena clara, orejas grandes y sonrisa
CHARS['asta'] = {
    'body': 'bajito', 'pal': pal('#f2c030', '#e8b080', iris='#1e1414', bolt='#2a4a8a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': False, 'big_ears': 3, 'ear_out': 4},
    'front': [L(outline([(16, 64), (10, 36), (16, 12), (12, -12, 1), (32, 2), (50, -4), (66, -14, 1), (72, 4), (110, -6, 1), (90, 18), (118, 30, 1), (92, 36), (100, 52, 1),
                         (86, 54), (84, 64), (78, 50), (22, 50)])),
              L(outline([(60, 0), (90, 18), (94, 40), (86, 58), (78, 40)]), 'shade', 'b', False),
              fringe([(14, 60), (16, 38), (30, 22), (50, 16), (70, 22), (84, 38), (86, 60), (76, 50), (70, 56, 1), (64, 42), (54, 50, 1), (48, 38), (40, 50, 1), (32, 40),
                      (24, 52, 1)]),
              L(outline([(66, 54), (58, 72), (64, 72), (56, 92), (70, 68), (64, 68), (70, 54)]), 'bolt', 'f', ln=True)],
    'side': [L(outline([(54, 58), (62, 44), (82, 42), (92, 28), (86, 10), (96, -8, 1), (70, -2), (62, -20, 1), (46, -4), (20, -14, 1), (20, 6), (-12, 0, 1), (2, 22),
                        (-20, 30, 1), (0, 40), (-14, 56, 1), (6, 58), (2, 76, 1), (18, 70), (30, 80, 1), (40, 70)])),
             L(outline([(6, 32), (24, 40), (24, 64), (8, 58)]), 'shade', 'b', False),
             fringe([(66, 2), (88, 14), (94, 38), (90, 58, 1), (84, 44), (76, 32)])],
    'back': [L(outline([(16, 80), (6, 60), (-14, 54, 1), (4, 44), (-10, 26, 1), (12, 22), (12, -8, 1), (30, 4), (50, -4), (66, -14, 1), (72, 4), (110, -6, 1), (90, 18),
                        (118, 30, 1), (92, 38), (104, 56, 1), (90, 64), (84, 80), (50, 88)])),
             L(outline([(56, 2), (88, 18), (94, 50), (84, 78), (62, 86)]), 'shade', 'b', False),
             strand([(30, 20), (40, 50), (34, 76)], 'deep', 'b', 1.0), strand([(70, 20), (60, 50), (66, 76)], 'deep', 'b', 1.0)],
}

# Navan: pelo blanco rosado peinado en una llama alta y puntiaguda que sale hacia arriba, con mechones de puntas a los lados
# y en la nuca; cejas fruncidas
CHARS['navan'] = {
    'body': 'normal', 'pal': pal('#f2e2e4', '#fcd8b4', iris='#2a1e1a', shade='#d4b4b8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 90), (2, 96, 1), (6, 80), (-6, 70, 1), (6, 56), (8, 24), (24, 6), (36, -2), (40, -32), (56, -48, 1), (58, -20), (66, 2), (82, 10), (94, 30),
                         (94, 56), (106, 70, 1), (94, 80), (98, 96, 1), (86, 90), (82, 60), (18, 60)])),
              L(outline([(56, -40), (60, -10), (84, 12), (96, 40), (90, 84), (80, 50), (66, 20)]), 'shade', 'b', False),
              fringe([(14, 64), (16, 40), (30, 22), (50, 16), (70, 22), (84, 40), (86, 64), (78, 52), (70, 62, 1), (64, 46), (54, 56, 1), (50, 44), (44, 56, 1), (36, 46),
                      (28, 60, 1), (22, 50)])],
    'side': [L(outline([(56, 56), (64, 44), (82, 42), (94, 26), (86, 6), (70, -6), (50, -30), (20, -50, 1), (30, -24), (14, -10), (4, 14), (2, 40), (-6, 60, 1), (6, 66),
                        (0, 84, 1), (16, 80), (12, 98, 1), (28, 86), (36, 96, 1), (42, 80), (50, 70)])),
             L(outline([(2, 36), (24, 42), (26, 80), (6, 74)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 16), (96, 40), (92, 62, 1), (84, 46), (78, 34)])],
    'back': [L(outline([(14, 92), (2, 98, 1), (6, 82), (-6, 72, 1), (6, 56), (8, 24), (24, 6), (36, -2), (40, -32), (56, -48, 1), (58, -20), (66, 2), (82, 10), (94, 30),
                        (94, 56), (106, 72, 1), (94, 82), (98, 98, 1), (86, 92), (72, 100, 1), (62, 90), (50, 102, 1), (38, 90), (28, 100, 1)])),
             L(outline([(56, -40), (60, -6), (86, 14), (96, 50), (88, 90), (64, 92)]), 'shade', 'b', False)],
}

# Dasan: pelo morado peinado hacia un lado en un tupé que acaba en punta, con un mechón largo que le tapa el ojo derecho y
# cae hasta el hombro; orejas puntiagudas y mirada de soslayo
CHARS['dasan'] = {
    'body': 'normal', 'pal': pal('#5a3aa0', '#fcdcbc', iris='#1e1414'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': False, 'big_ears': 2, 'ear_out': 6},
    'front': [L(outline([(14, 64), (10, 36), (20, 12), (44, 0), (72, 0), (98, -14, 1), (88, 10), (100, 34, 1), (88, 40), (86, 64), (80, 52), (20, 52)])),
              L(outline([(60, 2), (88, 10), (92, 40), (86, 58), (78, 36)]), 'shade', 'b', False),
              fringe([(14, 56), (16, 34), (30, 16), (50, 10), (70, 14), (86, 30), (90, 52), (84, 80), (86, 120, 1), (74, 90), (70, 60), (60, 44), (46, 36), (32, 40),
                      (22, 52)]),
              L(outline([(60, 18), (80, 24), (88, 46), (80, 70), (72, 44)]), 'shade', 'f', False)],
    'side': [L(outline([(54, 56), (62, 44), (82, 42), (92, 26), (84, 6), (64, -4), (40, -2), (10, -6, 1), (20, 6), (6, 24), (4, 54), (16, 74), (32, 72), (46, 64)])),
             L(outline([(6, 32), (24, 38), (24, 64), (8, 58)]), 'shade', 'b', False),
             fringe([(66, 0), (90, 14), (96, 40), (92, 66), (82, 110, 1), (78, 70), (74, 40)])],
    'back': [L(outline([(14, 80), (10, 36), (20, 12), (44, 0), (72, 0), (98, -14, 1), (88, 10), (100, 34, 1), (90, 40), (86, 80), (50, 88)])),
             L(outline([(56, 2), (88, 10), (92, 50), (84, 78), (62, 86)]), 'shade', 'b', False),
             L(outline([(70, 70), (84, 76), (78, 112, 1), (68, 88)]), 'mid', 'f', ln=True),
             strand([(20, 20), (50, 30), (80, 20)], 'deep', 'b', 1.0)],
}

# Sata (portero): pelo verde oliva de pinchos hacia arriba y hacia la derecha, flequillo de puntas y una coleta fina que cae
# por la nuca; ojos rojos muy abiertos y sonrisa
CHARS['sata'] = {
    'body': 'normal', 'pal': pal('#4a5a2a', '#fcd8b4', iris='#c81e1e'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 66), (0, 60, 1), (12, 50), (6, 22), (16, 4), (34, -4), (44, -20, 1), (54, -6), (70, -18, 1), (74, 2), (96, -4, 1), (88, 20), (104, 32, 1),
                         (90, 40), (98, 60, 1), (84, 66), (82, 50), (18, 50)])),
              L(outline([(60, -2), (88, 12), (94, 40), (88, 60), (78, 40)]), 'shade', 'b', False),
              fringe([(14, 60), (16, 38), (30, 22), (50, 16), (70, 22), (84, 38), (86, 60), (78, 50), (72, 58, 1), (64, 44), (56, 56, 1), (50, 42), (42, 56, 1), (36, 44),
                      (26, 58, 1)])],
    'side': [L(outline([(54, 58), (62, 44), (82, 42), (92, 28), (84, 10), (94, -8, 1), (68, -2), (60, -22, 1), (44, -4), (22, 0), (6, 18), (2, 46), (10, 70), (26, 76),
                        (42, 68)])),
             L(outline([(16, 64), (6, 84), (-8, 104), (-14, 112, 1), (2, 104), (18, 86), (26, 70)]), 'mid', 'b', ln=True),
             L(outline([(6, 32), (24, 38), (24, 64), (8, 58)]), 'shade', 'b', False),
             fringe([(66, 2), (88, 14), (94, 38), (90, 58, 1), (84, 44), (76, 32)])],
    'back': [L(outline([(16, 80), (6, 22), (16, 4), (34, -4), (44, -20, 1), (54, -6), (70, -18, 1), (74, 2), (96, -4, 1), (88, 20), (104, 32, 1), (90, 40), (86, 80),
                        (50, 86)])),
             L(outline([(56, 0), (88, 14), (92, 50), (84, 78), (62, 84)]), 'shade', 'b', False),
             L(outline([(44, 76), (56, 76), (58, 100), (50, 116, 1), (44, 100)]), 'mid', 'f', ln=True)],
}

# Sahasra: media melena blanca crema en casco, con el flequillo recto en mechones y las puntas de los lados rizadas hacia
# fuera; piel morena, sombra morada en los ojos y media sonrisa
CHARS['sahasra'] = {
    'body': 'normal', 'pal': pal('#f4f0dc', '#b07c50', iris='#2a1a2a', shade='#d4c0b4'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 86), (2, 96, 1), (6, 80), (4, 40), (16, 12), (50, 0), (84, 12), (96, 40), (94, 80), (98, 96, 1), (86, 86), (82, 62), (18, 62)])),
              L(outline([(60, 4), (86, 16), (96, 44), (92, 82), (80, 50)]), 'shade', 'b', False),
              fringe([(12, 66), (12, 40), (26, 16), (50, 8), (74, 16), (88, 40), (88, 66), (80, 56), (74, 62, 1), (66, 50), (58, 58, 1), (50, 48), (42, 58, 1), (34, 50),
                      (26, 62, 1), (20, 56)])],
    'side': [L(outline([(54, 62), (58, 50), (80, 48), (92, 34), (88, 12), (66, 0), (38, 0), (16, 12), (6, 40), (4, 76), (-6, 90, 1), (12, 86), (20, 98, 1), (30, 86),
                        (44, 80)])),
             L(outline([(4, 36), (28, 40), (30, 80), (8, 80)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 14), (94, 40), (90, 62, 1), (84, 48), (78, 58, 1), (74, 40), (64, 30)])],
    'back': [L(outline([(14, 88), (0, 98, 1), (4, 78), (4, 40), (16, 12), (50, 0), (84, 12), (96, 40), (96, 78), (100, 98, 1), (86, 88), (64, 94), (50, 104, 1), (36, 94)])),
             L(outline([(56, 4), (86, 16), (96, 44), (94, 86), (64, 92)]), 'shade', 'b', False)],
}

# Ayuta: pelo azul en un casco redondo de seta que le baja hasta los ojos y se abre en dos picos a los lados, con un
# antifaz negro; sonrisa
CHARS['ayuta'] = {
    'body': 'bajito', 'pal': pal('#1e5a8a', '#fcd8b4', iris='#1e1414', mask='#1a1a1e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 66), (-6, 58, 1), (8, 52), (8, 22), (24, 4), (50, -2), (76, 4), (92, 22), (92, 52), (106, 58, 1), (86, 66), (80, 70), (50, 74), (20, 70)])),
              L(outline([(60, 2), (86, 14), (94, 40), (88, 60), (76, 40)]), 'shade', 'b', False),
              L(outline([(20, 66), (50, 70), (80, 66), (78, 80), (60, 82), (50, 78), (40, 82), (22, 80)]), 'mask', 'f', ln=True),
              L(ell(36, 74, 4, 2.6), WHITE, 'f', False), L(ell(64, 74, 4, 2.6), WHITE, 'f', False),
              L(ell(37, 74, 1.6, 1.6), OUTC, 'f', False), L(ell(65, 74, 1.6, 1.6), OUTC, 'f', False)],
    'side': [L(outline([(60, 66), (70, 62), (90, 60), (96, 40), (86, 12), (60, -2), (30, 0), (10, 16), (2, 46), (6, 76), (20, 84), (40, 76)])),
             L(outline([(4, 36), (26, 42), (28, 76), (8, 70)]), 'shade', 'b', False),
             L(outline([(72, 64), (96, 64), (96, 80), (74, 80)]), 'mask', 'f', ln=True), L(ell(88, 72, 3, 2.4), WHITE, 'f', False)],
    'back': [L(outline([(16, 84), (-6, 60, 1), (8, 52), (8, 22), (24, 4), (50, -2), (76, 4), (92, 22), (92, 52), (106, 60, 1), (84, 84), (50, 90)])),
             L(outline([(56, 2), (86, 14), (94, 44), (84, 82), (62, 88)]), 'shade', 'b', False)],
}

# Laksha: melena larga gris liliácea con un mechón ancho que le tapa el ojo derecho y puntas abiertas en capas a los lados;
# sonrisa torcida de dientes
CHARS['laksha'] = {
    'body': 'delgado', 'pal': pal('#9a8aa0', '#fce0c4', iris='#1e1414'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 110), (8, 84), (-12, 82, 1), (4, 70), (-12, 54, 1), (6, 44), (8, 18), (30, 2), (50, -2), (70, 2), (92, 18), (94, 44), (112, 54, 1), (96, 70),
                         (112, 82, 1), (92, 84), (86, 110), (82, 62), (18, 62)])),
              L(outline([(60, 2), (88, 16), (96, 50), (90, 104), (80, 60)]), 'shade', 'b', False),
              fringe([(12, 70), (12, 40), (26, 16), (50, 8), (74, 16), (88, 40), (88, 70), (82, 60), (80, 76, 1), (72, 56), (64, 40), (56, 50), (54, 70), (60, 104, 1),
                      (46, 90), (40, 64), (32, 52), (24, 66, 1)])],
    'side': [L(outline([(54, 62), (58, 50), (80, 48), (92, 34), (88, 12), (66, 0), (38, 0), (14, 12), (2, 40), (-14, 52, 1), (2, 60), (-12, 76, 1), (4, 84), (8, 110),
                        (20, 100), (34, 108, 1), (40, 84), (46, 74)])),
             L(outline([(4, 36), (28, 42), (32, 96), (8, 100)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 14), (94, 40), (90, 64, 1), (84, 48), (78, 60, 1), (74, 40), (64, 30)])],
    'back': [L(outline([(14, 112), (8, 86), (-12, 84, 1), (4, 72), (-12, 56, 1), (6, 44), (8, 18), (30, 2), (50, -2), (70, 2), (92, 18), (94, 44), (112, 56, 1), (96, 72),
                        (112, 84, 1), (92, 86), (86, 112), (50, 118)])),
             L(outline([(56, 2), (88, 16), (96, 56), (88, 110), (64, 114)]), 'shade', 'b', False),
             strand([(30, 30), (26, 110)], 'deep', 'b', 1.0), strand([(70, 30), (74, 110)], 'deep', 'b', 1.0)],
}

# Niyuta: pelo blanco rosado despeinado en mechones que le caen por la cara, con un parche negro con un ojo pintado sobre
# el ojo derecho; sonrisa de dientes
CHARS['niyuta'] = {
    'body': 'normal', 'pal': pal('#f2e4e0', '#fcdcbc', iris='#1e1414', shade='#d4b8b4', patch='#1a1a1e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 92), (2, 96, 1), (6, 76), (4, 40), (16, 12), (50, 0), (84, 12), (96, 40), (94, 76), (98, 96, 1), (86, 92), (82, 64), (18, 64)])),
              L(outline([(60, 4), (86, 16), (96, 44), (92, 86), (80, 50)]), 'shade', 'b', False),
              L(outline([(18, 64), (34, 60), (48, 66), (46, 86), (30, 88), (20, 80)]), 'patch', 'f', ln=True),
              L(ell(34, 74, 6, 6), WHITE, 'f', False), L(ell(34, 74, 2.6, 2.6), OUTC, 'f', False),
              L(ell(66, 76, 3.4, 4.4), WHITE, 'f', ln=True), L(ell(66, 76, 1.8, 2.4), OUTC, 'f', False),
              fringe([(12, 68), (12, 40), (26, 16), (50, 8), (74, 16), (88, 40), (88, 68), (80, 56), (76, 70, 1), (68, 50), (60, 62, 1), (56, 44), (48, 58), (42, 76, 1),
                      (34, 56), (24, 70, 1), (20, 58)])],
    'side': [L(outline([(54, 62), (58, 50), (80, 48), (92, 34), (88, 12), (66, 0), (38, 0), (16, 12), (6, 40), (4, 76), (10, 94, 1), (20, 84), (30, 96, 1), (36, 82),
                        (46, 76)])),
             L(outline([(4, 36), (28, 40), (30, 80), (8, 80)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 14), (94, 40), (90, 64, 1), (84, 48), (78, 60, 1), (74, 40), (64, 30)]),
             L(ell(86, 74, 3, 4.4), WHITE, 'f', ln=True), L(ell(87, 74, 1.4, 2), OUTC, 'f', False)],
    'back': [L(outline([(14, 92), (2, 98, 1), (6, 76), (4, 40), (16, 12), (50, 0), (84, 12), (96, 40), (94, 76), (98, 98, 1), (86, 92), (70, 98, 1), (60, 90), (50, 100, 1),
                        (40, 90), (30, 98, 1)])),
             L(outline([(56, 4), (86, 16), (96, 44), (94, 88), (64, 94)]), 'shade', 'b', False)],
}
