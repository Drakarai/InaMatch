"""Colegio Ultramegahiedra (go-aoba-gakuen): sus modelos 3D de Inazuma Eleven GO como referencia (busto de frente, perfil y
espalda); los que no tienen modelo, por su retrato."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from chars_bigwaves import rect_glasses, white_eyes
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


def panda(y=76, sep=15, rx=9, ry=7):
    """Manchas negras alrededor de los ojos (maquillaje de ojeras)."""
    return [L(ell(50 - sep, y, rx, ry), OUTC, 'f', False), L(ell(50 + sep, y, rx, ry), OUTC, 'f', False)]


# Clem Attish (portero): pelo rojo rosado alto que sube recto y se dobla en dos mechones largos que caen como lazos hacia
# los lados; gafas redondas grandes de montura blanca, nariz puntiaguda naranja y cejas de enfado
CHARS['clem-attish'] = {
    'body': 'delgado', 'pal': pal('#d83c56', '#e8a868', shade='#a8283e', nose='#e07a3a', lens='#2a3a50'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 102, 'hairline': False,
             'face_front': blob([(16, 50), (50, 44), (84, 50), (86, 84), (80, 108), (62, 118), (38, 118), (20, 108), (14, 84)])},
    'front': [L(outline([(24, 52), (22, 20), (30, -10), (40, -30), (56, -34), (64, -20), (66, 0), (76, -14), (96, -6), (110, 10), (104, 30, 1), (96, 12), (80, 8),
                         (74, 24), (76, 52), (50, 48)])),
              L(outline([(34, -26), (24, -40), (6, -30), (-4, -10, 1), (14, -24), (30, -12)])),
              L(outline([(56, -30), (64, -20), (66, 0), (60, 20), (56, 48), (74, 50), (74, 20), (68, -6)]), 'shade', 'b', False),
              L(ell(34, 74, 11, 10), WHITE, 'f', ln=True), L(ell(66, 74, 11, 10), WHITE, 'f', ln=True),
              L(ell(34, 74, 7.6, 7), 'lens', 'f', False), L(ell(66, 74, 7.6, 7), 'lens', 'f', False),
              L(ell(32, 72, 2, 1.6), WHITE, 'f', False), L(ell(64, 72, 2, 1.6), WHITE, 'f', False),
              L([(45, 74), (55, 74)], WHITE, 'f', False, False, 2.4),
              L(outline([(46, 82), (54, 82), (50, 94, 1)]), 'nose', 'f', ln=True)],
    'side': [L(outline([(46, 92), (30, 92), (18, 70), (14, 40), (18, 10), (30, -14), (14, -24), (-6, -16), (-14, 2, 1), (-4, -30), (20, -38), (40, -30), (50, -12),
                        (64, -24), (80, -24), (84, -4, 1), (70, -14), (60, 0), (62, 30), (56, 50), (48, 70)])),
             L(outline([(16, 30), (30, 40), (34, 80), (20, 76)]), 'shade', 'b', False),
             L(ell(84, 74, 6, 8), WHITE, 'f', ln=True), L(ell(85, 74, 3.6, 5.4), 'lens', 'f', False), L([(78, 72), (50, 68)], WHITE, 'f', False, False, 2.2),
             L(outline([(92, 82), (108, 96, 1), (94, 92)]), 'nose', 'f', ln=True)],
    'back': [L(outline([(24, 90), (20, 52), (22, 20), (30, -10), (40, -30), (56, -34), (64, -20), (66, 0), (76, -14), (96, -6), (110, 10), (104, 30, 1), (96, 12),
                        (80, 8), (78, 52), (76, 90), (50, 96)])),
             L(outline([(34, -26), (24, -40), (6, -30), (-4, -10, 1), (14, -24), (30, -12)])),
             L(outline([(54, 20), (78, 20), (78, 88), (60, 94)]), 'shade', 'b', False)],
}

# Pike Pollack: pelo azul grisáceo peinado hacia atrás con raya en medio, liso y pegado, recogido en una coleta larga que cae
# por la espalda; ojeras negras pintadas, cejas finas y boca abierta de labios gruesos
CHARS['pike-pollack'] = {
    'body': 'normal', 'pal': pal('#5a7aa8', '#f6c494', iris='#1e1414', shade='#3e5a84'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'lips', 'mouth_y': 102, 'mouth_w': 7, 'hairline': False},
    'front': [L(outline([(16, 72), (10, 40), (22, 14), (40, 2), (50, -4), (60, 2), (78, 14), (90, 40), (84, 72), (70, 52), (56, 44), (50, 52, 1), (44, 44),
                         (30, 52)])),
              L(outline([(50, -2), (58, 6), (54, 44), (50, 50)]), 'shade', 'b', False),
              strand([(30, 14), (22, 40), (20, 64)], 'shade', 'b', 1.0), strand([(70, 14), (78, 40), (80, 64)], 'shade', 'b', 1.0),
              strand([(42, 4), (36, 30)], 'shade', 'b', 1.0), strand([(58, 4), (64, 30)], 'shade', 'b', 1.0)]
             + panda(78, 15, 10, 6) + white_eyes(78, 15, 5, 3.6, 1.6)
             + [L([(26, 64), (42, 68)], OUTC, 'f', False, False, 1.2), L([(74, 64), (58, 68)], OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(54, 60), (56, 44), (76, 38), (90, 30), (84, 10), (60, -2), (34, 0), (14, 14), (4, 36), (6, 60), (22, 70), (40, 66)])),
             L(outline([(14, 26), (4, 30), (-6, 46), (-14, 80), (-20, 112, 1), (-8, 90), (-6, 108, 1), (2, 80), (8, 50), (20, 36)])),
             L(outline([(8, 22), (16, 24), (14, 34), (6, 32)]), 'shade', 'f', ln=True),
             strand([(70, 8), (40, 6), (20, 20)], 'shade', 'b', 1.0), strand([(60, 30), (34, 30), (14, 40)], 'shade', 'b', 1.0),
             L(ell(84, 77, 6, 4), OUTC, 'f', False), L(ell(85, 77, 2.6, 2.4), WHITE, 'f', False)],
    'back': [L(outline([(16, 84), (10, 40), (22, 14), (40, 2), (50, -4), (60, 2), (78, 14), (90, 40), (84, 84), (50, 90)])),
             L(outline([(56, 2), (80, 16), (90, 46), (84, 80), (62, 86)]), 'shade', 'b', False),
             L(outline([(42, 20), (58, 20), (64, 70), (60, 116, 1), (50, 96), (40, 116, 1), (36, 70)]), 'mid', 'f', ln=True),
             strand([(50, 24), (50, 100)], 'shade', 'f', 1.0)],
}

# Martin Blando: piel morena, pelo morado oscuro de pinchos hacia arriba y hacia los lados, con un flequillo espeso que
# le cae por la frente y deja la cara en sombra (no se le ven los ojos)
CHARS['martin-blando'] = {
    'body': 'normal', 'pal': pal('#3a2a6a', '#a87048', shade='#261a4a', skin_d='#7a4e30'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(16, 74), (2, 80, 1), (8, 62), (-10, 56, 1), (6, 44), (-4, 26, 1), (14, 22), (14, 0, 1), (30, 8), (40, -18, 1), (52, 2), (66, -14, 1),
                         (68, 6), (88, 0, 1), (84, 22), (104, 26, 1), (92, 44), (108, 56, 1), (92, 62), (98, 80, 1), (84, 74), (82, 60), (18, 60)])),
              L(outline([(60, 2), (84, 14), (96, 44), (88, 70), (78, 40)]), 'shade', 'b', False),
              fringe([(14, 72), (16, 42), (30, 24), (50, 18), (70, 24), (84, 42), (86, 72), (78, 62), (70, 80, 1), (64, 64), (56, 84, 1), (50, 68), (44, 84, 1),
                      (36, 66), (30, 80, 1), (22, 64)]),
              L(outline([(16, 76), (84, 76), (84, 86), (16, 86)]), 'skin_d', 'b', False)],
    'side': [L(outline([(56, 62), (64, 50), (82, 52), (94, 66, 1), (92, 44), (100, 24, 1), (86, 16), (88, -4, 1), (68, 2), (58, -20, 1), (44, 0), (20, -14, 1),
                        (22, 10), (-6, 14, 1), (10, 30), (-12, 44, 1), (6, 54), (-6, 72, 1), (12, 72), (12, 90, 1), (28, 78), (44, 74)])),
             L(outline([(4, 34), (24, 40), (26, 70), (8, 64)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 84), (0, 86, 1), (8, 68), (-10, 58, 1), (6, 46), (-6, 28, 1), (14, 22), (12, 0, 1), (30, 8), (40, -18, 1), (52, 2), (66, -14, 1),
                        (68, 6), (90, 0, 1), (84, 22), (106, 28, 1), (92, 46), (110, 58, 1), (92, 68), (100, 86, 1), (84, 84), (66, 96, 1), (58, 86), (50, 98, 1),
                        (42, 86), (34, 96, 1)])),
             L(outline([(56, 4), (84, 14), (96, 46), (88, 82), (62, 88)]), 'shade', 'b', False)],
}

# Keane Gardner (sin modelo 3D; por su retrato): pelo crema corto y mullido, abierto en mechones a los lados, con las puntas
# de abajo verde azulado; ojos azules serios
CHARS['keane-gardner'] = {
    'body': 'normal', 'pal': pal('#f4f0d8', '#fcdcbc', iris='#3a5a9a', shade='#d8d0b0', tip='#4e6058'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 70), (-6, 66, 1), (4, 54), (2, 30), (16, 8), (38, -4), (62, -4), (84, 8), (98, 30), (96, 54), (106, 66, 1), (88, 70), (84, 56),
                         (16, 56)])),
              L(outline([(-4, 64), (8, 54), (20, 60), (14, 70)]), 'tip', 'f', ln=True), L(outline([(104, 64), (92, 54), (80, 60), (86, 70)]), 'tip', 'f', ln=True),
              fringe([(12, 62), (14, 38), (28, 18), (50, 10), (72, 18), (86, 38), (88, 62), (80, 54), (72, 64, 1), (64, 48), (54, 60, 1), (48, 46), (38, 60, 1),
                      (32, 48), (22, 62, 1)]),
              L(outline([(60, 18), (78, 26), (84, 46), (70, 38)]), 'shade', 'f', False)],
    'side': [L(outline([(52, 58), (40, 56), (24, 84), (10, 80), (-6, 60), (2, 44), (40, 44)]), 'tip'),
             L(outline([(54, 50), (82, 48), (94, 34), (88, 12), (66, -2), (38, -4), (16, 8), (2, 30), (-10, 50, 1), (8, 46), (20, 54), (36, 46)])),
             L(outline([(6, 32), (24, 38), (28, 64), (10, 60)]), 'shade', 'b', False),
             fringe([(66, 2), (88, 14), (94, 36), (90, 52, 1), (82, 42), (74, 32)])],
    'back': [L(outline([(12, 80), (-4, 74, 1), (4, 58), (2, 30), (16, 8), (38, -4), (62, -4), (84, 8), (98, 30), (96, 58), (104, 74, 1), (88, 80), (50, 86)])),
             L(outline([(10, 70), (90, 70), (88, 82), (66, 90), (50, 84), (34, 90), (12, 82)]), 'tip', 'b', ln=True),
             L(outline([(56, 0), (84, 12), (96, 44), (88, 66), (64, 66)]), 'shade', 'b', False)],
}

# Tyrian Purpel: pelo castaño oscuro pegado y rapado a los lados, con una cresta de pinchos verde azulado encima que baja
# por la nuca; nariz larga marcada y cara de enfado
CHARS['tyrian-purpel'] = {
    'body': 'normal', 'pal': pal('#4a2e22', '#f6c08a', iris='#1e1414', crest='#3a8a9a', crest_d='#24606e', nose='#e0985a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 102, 'hairline': [(10, 70), (18, 40), (40, 30), (50, 46), (60, 30), (82, 40), (90, 70)]},
    'front': [L(outline([(12, 76), (10, 40), (20, 14), (50, 4), (80, 14), (90, 40), (88, 76)])),
              L(outline([(28, 10), (20, -6, 1), (36, 0), (38, -18, 1), (48, -4), (56, -22, 1), (62, -4), (76, -14, 1), (74, 4), (84, 6, 1), (72, 16), (50, 12)]),
                'crest', 'f', ln=True),
              L(outline([(50, -8), (62, -4), (74, 4), (70, 14), (52, 12)]), 'crest_d', 'f', False),
              L(outline([(46, 70), (54, 70), (58, 94), (50, 98), (42, 94)]), 'nose', 'f', ln=True)],
    'side': [L(outline([(48, 70), (58, 40), (76, 28), (80, 12), (60, 0), (32, 2), (12, 18), (6, 46), (12, 76), (28, 92), (40, 86)])),
             L(outline([(76, 8), (84, -6, 1), (66, 0), (66, -18, 1), (54, -4), (48, -20, 1), (38, -4), (28, -16, 1), (24, 2), (10, -4, 1), (14, 12), (0, 16, 1), (14, 24),
                        (40, 10), (70, 14)]), 'crest', 'f', ln=True)],
    'back': [L(outline([(12, 80), (10, 40), (20, 14), (50, 4), (80, 14), (90, 40), (88, 80), (50, 92)])),
             L(outline([(56, 8), (80, 18), (88, 50), (84, 78), (62, 86)]), 'shade', 'b', False),
             L(outline([(40, 4), (30, -8, 1), (44, -4), (50, -20, 1), (56, -4), (70, -8, 1), (60, 10), (62, 30, 1), (56, 34), (58, 54, 1), (50, 72, 1), (42, 54, 1),
                        (44, 34), (38, 30, 1), (40, 10)]), 'crest', 'f', ln=True)],
}

# Shaun Bonce: pelo castaño muy oscuro enorme y esponjoso de mechones cuadrados en punta en todas direcciones, con un
# pico que baja por la frente; cara redonda pálida de ojos blancos de susto
CHARS['shaun-bonce'] = {
    'body': 'bajito', 'pal': pal('#3a2a26', '#fce8c8', shade='#2a1e1c'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 92), (-6, 98, 1), (0, 80), (-16, 70, 1), (-2, 60), (-14, 44, 1), (2, 36), (-6, 14, 1), (14, 16), (12, -6, 1), (30, 2), (38, -20, 1),
                         (52, -4), (66, -18, 1), (68, 2), (88, -6, 1), (86, 16), (106, 14, 1), (98, 36), (114, 44, 1), (102, 60), (116, 70, 1), (100, 80), (106, 98, 1),
                         (86, 92), (84, 64), (16, 64)])),
              L(outline([(60, 0), (88, 12), (104, 50), (98, 86), (82, 50)]), 'shade', 'b', False),
              fringe([(14, 70), (16, 44), (30, 28), (42, 26), (50, 52, 1), (58, 26), (70, 28), (84, 44), (86, 70), (78, 56), (66, 46), (50, 56), (34, 46), (22, 56)])]
             + white_eyes(78, 14, 6.6, 6.4, 1.8),
    'side': [L(outline([(54, 64), (62, 52), (82, 52), (90, 38), (100, 22, 1), (84, 18), (86, -2, 1), (66, 4), (60, -18, 1), (44, 0), (22, -10, 1), (22, 10), (-4, 8, 1),
                        (8, 26), (-16, 34, 1), (2, 46), (-16, 60, 1), (2, 66), (-8, 84, 1), (12, 84), (14, 100, 1), (28, 86), (44, 80)])),
             L(outline([(2, 36), (24, 42), (28, 76), (8, 70)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 96), (-6, 98, 1), (0, 80), (-16, 70, 1), (-2, 60), (-14, 44, 1), (2, 36), (-6, 14, 1), (14, 16), (12, -6, 1), (30, 2), (38, -20, 1),
                        (52, -4), (66, -18, 1), (68, 2), (88, -6, 1), (86, 16), (106, 14, 1), (98, 36), (114, 44, 1), (102, 60), (116, 70, 1), (100, 80), (106, 98, 1),
                        (86, 96), (70, 104, 1), (60, 94), (50, 104, 1), (40, 94), (30, 104, 1)])),
             L(outline([(56, 0), (88, 12), (104, 50), (98, 94), (64, 98)]), 'shade', 'b', False)],
}

# Penn Minim: pelo blanco liso con un mechón azul marino grueso que le cruza la cara y le tapa un ojo, dos moños redondos
# azul marino muy separados a los lados; ojeras negras y sonrisa de pillo
CHARS['penn-minim'] = {
    'body': 'bajito', 'pal': pal('#eceaf0', '#f6c890', iris='#1e1414', shade='#b8a8a8', bun='#1e2e66', bun_d='#141e48'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(ell(-10, 24, 16, 15), 'bun', 'b', True, True), L(ell(110, 24, 16, 15), 'bun', 'b', True, True),
              strand([(-20, 20), (-4, 28)], 'bun_d', 'b', 1.0), strand([(100, 28), (118, 20)], 'bun_d', 'b', 1.0),
              L(outline([(14, 96), (10, 60), (6, 34), (0, 24, 1), (14, 22), (24, 6), (50, -2), (76, 6), (86, 22), (100, 24, 1), (94, 34), (90, 60), (86, 96), (80, 66),
                         (20, 66)])),
              fringe([(12, 70), (14, 40), (26, 20), (50, 12), (74, 20), (86, 40), (88, 70), (80, 54), (72, 60), (64, 46), (36, 46), (28, 60), (20, 54)])]
             + panda(76, 14, 10, 7) + white_eyes(77, 14, 5, 3.4, 1.6)
             + [L(outline([(52, 6), (64, 12), (64, 40), (54, 70), (40, 98), (34, 94, 1), (44, 64), (50, 36)]), 'bun', 'f', ln=True)],
    'side': [L(ell(10, -2, 15, 15), 'bun', 'b', True, True), strand([(0, -6), (18, 4)], 'bun_d', 'b', 1.0),
             L(outline([(54, 60), (58, 48), (80, 46), (92, 34), (88, 14), (66, 0), (36, -2), (16, 10), (6, 34), (6, 62), (18, 84), (34, 84), (46, 72)]), 'shade'),
             L(outline([(16, 10), (36, -2), (66, 0), (88, 14), (92, 34), (60, 34), (30, 30)]), 'mid', 'b', False),
             L(outline([(80, 0), (90, 10), (96, 50), (92, 80, 1), (86, 50), (82, 30)]), 'bun', 'f', ln=True)],
    'back': [L(ell(-10, 24, 16, 15), 'bun', 'b', True, True), L(ell(110, 24, 16, 15), 'bun', 'b', True, True),
             strand([(-20, 20), (-4, 28)], 'bun_d', 'b', 1.0), strand([(100, 28), (118, 20)], 'bun_d', 'b', 1.0),
             L(outline([(14, 96), (10, 60), (6, 34), (0, 24, 1), (14, 22), (24, 6), (50, -2), (76, 6), (86, 22), (100, 24, 1), (94, 34), (90, 60), (86, 96),
                        (50, 88)]), 'shade'),
             L(outline([(6, 30), (24, 6), (50, -2), (76, 6), (94, 30), (70, 28), (50, 36), (30, 28)]), 'mid', 'b', False),
             strand([(50, 4), (50, 84)], 'deep', 'b', 1.2)],
}

# Joshua Bleak: pelo lila grisáceo liso en forma de campana, que cae recto desde la coronilla y se abre en puntas a la
# altura de la mandíbula, con flequillo largo; ojos blancos de pupila pequeña y ojeras
CHARS['joshua-bleak'] = {
    'body': 'normal', 'pal': pal('#a89ab4', '#fcd8b4', shade='#7a6a86'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(16, 64), (12, 30), (24, 6), (50, -2), (76, 6), (88, 30), (104, 70), (114, 96, 1), (100, 90), (96, 100, 1), (88, 84), (84, 60), (16, 60),
                         (12, 84), (4, 100, 1), (0, 90), (-14, 96, 1), (-4, 70)])),
              L(outline([(60, 2), (86, 18), (104, 70), (110, 90), (90, 80), (80, 40)]), 'shade', 'b', False),
              fringe([(12, 66), (14, 38), (28, 18), (50, 10), (72, 18), (86, 38), (88, 66), (80, 54), (72, 62, 1), (64, 48), (54, 58, 1), (48, 46), (38, 58, 1),
                      (30, 48), (22, 62, 1)])]
             + white_eyes(78, 14, 6.4, 5.6, 1.8)
             + [L(quad((26, 72), (36, 66), (46, 72)), OUTC, 'f', False, False, 2.2), L(quad((54, 72), (64, 66), (74, 72)), OUTC, 'f', False, False, 2.2)],
    'side': [L(outline([(60, 50), (78, 44), (94, 32), (88, 10), (64, -4), (34, -2), (14, 12), (0, 40), (-14, 76), (-26, 106, 1), (-6, 96), (4, 108, 1), (16, 96),
                        (30, 106, 1), (40, 90), (50, 76)])),
             L(outline([(0, 50), (30, 50), (44, 92), (14, 98)]), 'shade', 'b', False),
             fringe([(66, 0), (90, 14), (96, 40), (92, 56, 1), (84, 46), (74, 34)])],
    'back': [L(outline([(16, 40), (24, 6), (50, -2), (76, 6), (84, 40), (104, 70), (116, 98, 1), (100, 90), (96, 100, 1), (84, 92), (72, 98, 1), (62, 90), (50, 100, 1),
                        (38, 90), (28, 98, 1), (16, 92), (4, 100, 1), (0, 90), (-16, 98, 1), (-4, 70)])),
             L(outline([(56, 2), (84, 18), (104, 70), (110, 94), (70, 92), (70, 40)]), 'shade', 'b', False)],
}

# Hayden Whyrl: piel morena, pelo rosa blanquecino de pinchos que salen en todas direcciones y caen hasta los hombros, con un
# antifaz azul marino de ojos blancos y un pico hacia arriba
CHARS['hayden-whyrl'] = {
    'body': 'normal', 'pal': pal('#f6dcd2', '#9a6a44', shade='#c8a090', mask='#2a3060', tape='#c8e8d8'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(14, 100), (-6, 96, 1), (4, 82), (-12, 70, 1), (2, 60), (-10, 40, 1), (8, 36), (2, 12, 1), (20, 18), (24, -6, 1), (38, 6), (48, -16, 1),
                         (56, 4), (62, -30, 1), (66, 4), (84, -4, 1), (82, 18), (104, 20, 1), (94, 38), (110, 48, 1), (96, 60), (108, 76, 1), (94, 82), (102, 98, 1),
                         (86, 98), (84, 66), (16, 66)])),
              L(outline([(60, 4), (86, 16), (100, 50), (94, 90), (80, 50)]), 'shade', 'b', False),
              fringe([(14, 70), (16, 42), (28, 24), (50, 18), (72, 24), (84, 42), (86, 70), (78, 56), (72, 66, 1), (64, 50), (56, 62, 1), (50, 48), (42, 62, 1),
                      (34, 50), (26, 66, 1), (20, 56)]),
              L(outline([(14, 70), (30, 64), (46, 70), (54, 70), (70, 64), (86, 70), (84, 84), (68, 90), (54, 82), (46, 82), (32, 90), (16, 84)]), 'mask', 'f', ln=True),
              L(ell(32, 77, 6, 4.6), WHITE, 'f', False), L(ell(68, 77, 6, 4.6), WHITE, 'f', False),
              L(ell(33, 78, 1.8, 2.2), OUTC, 'f', False), L(ell(67, 78, 1.8, 2.2), OUTC, 'f', False),
              L(outline([(46, 72), (54, 72), (54, 80), (46, 80)]), 'tape', 'f', ln=True)],
    'side': [L(outline([(56, 60), (64, 48), (82, 50), (94, 36), (100, 20, 1), (82, 14), (84, -10, 1), (64, 0), (56, -28, 1), (42, -2), (18, -10, 1), (20, 10), (-6, 12, 1),
                        (8, 28), (-14, 40, 1), (4, 50), (-10, 66, 1), (6, 70), (-2, 90, 1), (14, 84), (16, 102, 1), (30, 86), (44, 76)])),
             L(outline([(4, 36), (24, 42), (28, 76), (8, 70)]), 'shade', 'b', False),
             L(outline([(70, 70), (92, 68), (94, 84), (72, 86)]), 'mask', 'f', ln=True), L(ell(85, 77, 4, 4.4), WHITE, 'f', False),
             L(ell(86, 78, 1.6, 2), OUTC, 'f', False)],
    'back': [L(outline([(14, 100), (-6, 96, 1), (4, 82), (-12, 70, 1), (2, 60), (-10, 40, 1), (8, 36), (2, 12, 1), (20, 18), (24, -6, 1), (38, 6), (48, -16, 1),
                        (56, 4), (62, -30, 1), (66, 4), (84, -4, 1), (82, 18), (104, 20, 1), (94, 38), (110, 48, 1), (96, 60), (108, 76, 1), (94, 82), (102, 98, 1),
                        (86, 100), (70, 108, 1), (60, 98), (50, 108, 1), (40, 98), (30, 108, 1)]), 'shade'),
             L(ell(30, 40, 6, 4), 'mid', 'b', False), L(ell(66, 32, 6, 4), 'mid', 'b', False), L(ell(50, 64, 6, 4), 'mid', 'b', False),
             L(ell(24, 76, 5, 3), 'mid', 'b', False), L(ell(76, 70, 5, 3), 'mid', 'b', False)],
}

# Tarquin Orchards: pelo azul petróleo liso de mechones cortos, con un mechón blanco grande en la frente, la nuca en punta y
# una coleta corta en la nuca; ojos negros serios
CHARS['tarquin-orchards'] = {
    'body': 'normal', 'pal': pal('#1e5470', '#fcd8b4', iris='#1e1414', shade='#163e56'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 70), (2, 56, 1), (10, 44), (10, 22), (26, 4), (50, -2), (74, 4), (90, 22), (90, 44), (98, 56, 1), (86, 70), (84, 56), (16, 56)])),
              L(outline([(60, 2), (86, 16), (92, 46), (86, 64), (78, 40)]), 'shade', 'b', False),
              fringe([(12, 62), (14, 38), (26, 20), (50, 12), (74, 20), (86, 38), (88, 62), (82, 52), (76, 58, 1), (68, 44), (58, 54, 1), (52, 42), (44, 54, 1),
                      (36, 44), (26, 56, 1), (18, 50)]),
              L(outline([(40, 14), (56, 10), (58, 22), (50, 40), (44, 54, 1), (40, 36), (34, 24)]), WHITE, 'f', ln=True)],
    'side': [L(outline([(54, 60), (60, 48), (82, 48), (94, 34), (88, 12), (66, 0), (38, -2), (16, 10), (6, 32), (8, 56), (-2, 72), (2, 80, 1), (18, 70), (26, 84, 1),
                        (36, 72), (46, 70)])),
             L(outline([(18, 64), (2, 64), (-12, 72), (-16, 84, 1), (-2, 80), (-6, 92, 1), (8, 82), (22, 74)])),
             L(outline([(6, 34), (24, 40), (28, 64), (10, 60)]), 'shade', 'b', False),
             fringe([(66, 2), (88, 14), (94, 36), (90, 52, 1), (82, 42), (74, 32)]),
             L(outline([(76, 6), (88, 12), (92, 24), (84, 30)]), WHITE, 'f', ln=True)],
    'back': [L(outline([(14, 76), (2, 60, 1), (10, 46), (10, 22), (26, 4), (50, -2), (74, 4), (90, 22), (90, 46), (98, 60, 1), (86, 76), (66, 82), (58, 92, 1),
                        (50, 82), (42, 92, 1), (34, 82)])),
             L(outline([(56, 2), (86, 16), (92, 50), (84, 74), (62, 80)]), 'shade', 'b', False),
             L(outline([(36, 80), (64, 80), (72, 96), (66, 104, 1), (58, 96), (50, 106, 1), (42, 96), (34, 104, 1), (28, 96)]))],
}

# Skylar Lepton (sin modelo 3D; por su retrato): pelo morado oscuro liso con raya al lado y un flequillo largo que le tapa el
# ojo derecho, recogido detrás en una coleta baja; ojo grande de mirada fija
CHARS['skylar-lepton'] = {
    'body': 'delgado', 'pal': pal('#5a3a7a', '#fcd8b4', iris='#1e1414', shade='#3e2858'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(14, 80), (8, 46), (12, 18), (30, 2), (54, -2), (78, 6), (92, 24), (94, 50), (88, 80), (82, 60), (18, 60)])),
              L(outline([(60, 2), (86, 16), (94, 46), (88, 74), (78, 40)]), 'shade', 'b', False),
              fringe([(90, 90), (92, 50), (84, 22), (60, 8), (32, 10), (14, 26), (10, 54), (18, 46), (30, 40), (42, 46), (48, 60), (48, 90, 1), (60, 84), (76, 92, 1),
                      (82, 80)])],
    'side': [L(outline([(54, 60), (58, 48), (80, 46), (92, 32), (86, 12), (64, -2), (36, -2), (14, 10), (4, 34), (6, 60), (18, 76), (34, 76), (46, 70)])),
             L(outline([(18, 60), (6, 72), (0, 100), (-4, 116, 1), (8, 104), (14, 80), (24, 68)])),
             L(outline([(6, 34), (26, 40), (30, 66), (10, 62)]), 'shade', 'b', False),
             fringe([(64, 0), (88, 14), (96, 40), (92, 70, 1), (84, 54), (76, 36)])],
    'back': [L(outline([(14, 84), (8, 46), (12, 18), (30, 2), (54, -2), (78, 6), (92, 24), (94, 50), (88, 84), (50, 92)])),
             L(outline([(56, 2), (86, 16), (94, 50), (86, 80), (62, 88)]), 'shade', 'b', False),
             L(outline([(42, 80), (58, 80), (58, 110), (50, 124, 1), (42, 110)]), 'mid', 'f', ln=True)],
}

# Brook Bold: pelo rubio claro peinado hacia atrás en un tupé redondo, recogido en una coleta alta que se levanta por detrás,
# con mechones ondulados que caen a los lados de la cara; ojos azules y media sonrisa
CHARS['brook-bold'] = {
    'body': 'normal', 'pal': pal('#f2e2a0', '#f8c890', iris='#4a5aa8', shade='#d0b874'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': [(14, 80), (16, 46), (34, 36), (50, 40), (66, 36), (84, 46), (86, 80)]},
    'front': [L(outline([(10, 100), (0, 92), (4, 76), (-2, 62), (8, 44), (6, 26), (18, 6), (34, -4), (40, -16), (60, -16), (66, -4), (82, 6), (94, 26), (92, 44),
                         (102, 62), (96, 76), (100, 92), (90, 100), (84, 70), (16, 70)])),
              L(outline([(60, -12), (84, 8), (96, 40), (96, 92), (86, 80), (80, 30)]), 'shade', 'b', False),
              strand([(30, 0), (24, 30)], 'shade', 'b', 1.0), strand([(50, -10), (50, 30)], 'shade', 'b', 1.0), strand([(70, 0), (76, 30)], 'shade', 'b', 1.0),
              strand([(4, 62), (12, 72)], 'shade', 'b', 1.0), strand([(96, 62), (88, 72)], 'shade', 'b', 1.0)],
    'side': [L(outline([(56, 58), (60, 44), (80, 40), (94, 26), (86, 6), (62, -6), (40, -6), (30, -20), (20, -28), (6, -24), (-4, -2), (-10, 30), (-4, 50), (2, 70),
                        (-4, 92), (10, 100), (28, 92), (40, 80), (48, 70)])),
             L(outline([(6, -20), (20, -26), (30, -14), (24, 30), (6, 60), (-6, 40)]), 'shade', 'b', False),
             strand([(60, 0), (40, 4), (24, 20)], 'shade', 'b', 1.0), strand([(70, 24), (44, 26), (28, 40)], 'shade', 'b', 1.0)],
    'back': [L(outline([(8, 100), (-2, 90), (2, 74), (-4, 60), (6, 44), (6, 26), (18, 6), (34, -4), (40, -16), (60, -16), (66, -4), (82, 6), (94, 26), (94, 44),
                        (104, 60), (98, 74), (102, 90), (92, 100), (72, 96), (62, 108, 1), (50, 96), (38, 108, 1), (28, 96)])),
             L(outline([(56, -12), (84, 8), (96, 40), (98, 96), (70, 96), (70, 30)]), 'shade', 'b', False),
             strand([(50, -10), (50, 96)], 'shade', 'b', 1.0)],
}

# Francis Tuffnot (sin modelo 3D; por su retrato): pelo azul marino liso hasta los hombros con raya al lado y un mechón
# largo que le tapa un ojo; ojo morado y un pendiente de pluma blanca
CHARS['francis-tuffnot'] = {
    'body': 'delgado', 'pal': pal('#24306a', '#fcd8b4', iris='#8a3aa8', shade='#18204a', feather='#f0f0f4'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 104), (6, 70), (8, 36), (20, 10), (44, -2), (70, 2), (88, 18), (94, 46), (94, 80), (90, 104), (84, 86), (82, 60), (18, 60), (18, 92)])),
              L(outline([(60, 2), (86, 16), (94, 46), (92, 100), (84, 80), (80, 40)]), 'shade', 'b', False),
              fringe([(8, 96), (6, 56), (14, 26), (40, 8), (66, 10), (84, 26), (88, 56), (76, 44), (60, 46), (52, 60), (50, 92, 1), (40, 76), (24, 98, 1), (16, 80)]),
              L(outline([(84, 84), (88, 84), (90, 104), (86, 112, 1), (82, 104)]), 'feather', 'f', ln=True)],
    'side': [L(outline([(56, 58), (60, 46), (80, 44), (92, 30), (86, 10), (62, -2), (34, 0), (14, 12), (4, 40), (2, 80), (6, 104), (22, 104), (34, 92), (46, 80)])),
             L(outline([(4, 40), (26, 46), (32, 96), (8, 100)]), 'shade', 'b', False),
             fringe([(64, 0), (88, 14), (96, 40), (92, 64, 1), (84, 52), (76, 36)]),
             L(outline([(46, 80), (50, 80), (52, 100), (48, 108, 1), (44, 100)]), 'feather', 'f', ln=True)],
    'back': [L(outline([(8, 104), (4, 70), (8, 36), (20, 10), (44, -2), (70, 2), (88, 18), (96, 46), (96, 80), (92, 104), (50, 110)])),
             L(outline([(56, 2), (86, 16), (96, 50), (92, 102), (64, 106)]), 'shade', 'b', False)],
}

# Matt Durer (portero suplente): piel morena, pelo azul petróleo oscuro de pinchos cortos arriba, los lados rapados oscuros con
# una franja verde a cada lado, un mechón rubio en la nuca; nariz redonda y labios gruesos
CHARS['matt-durer'] = {
    'body': 'normal', 'pal': pal('#1e3a50', '#a06a40', iris='#1e1414', buzz='#2e2a2a', band='#4a8a5a', blond='#e8d84a', nose='#6a3a1e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'lips', 'mouth_y': 102, 'mouth_w': 8, 'hairline': (60, 36), 'nose': (50, 86, 4)},
    'front': [L(outline([(14, 78), (12, 30), (88, 30), (86, 78), (80, 70), (20, 70)]), 'buzz'),
              L(outline([(14, 50), (20, 44), (24, 84), (18, 86)]), 'band', 'f', ln=True), L(outline([(86, 50), (80, 44), (76, 84), (82, 86)]), 'band', 'f', ln=True),
              L(outline([(10, 36), (4, 20, 1), (14, 18), (16, 0, 1), (30, 6), (40, -14, 1), (50, 2), (62, -14, 1), (66, 4), (84, -2, 1), (82, 14), (98, 20, 1), (90, 34),
                         (76, 30), (66, 40), (54, 34), (40, 44, 1), (34, 32), (20, 40)]), 'mid', 'f'),
              L(outline([(-2, 88), (10, 82), (20, 92), (6, 98)]), 'blond', 'b'), L(outline([(102, 88), (90, 82), (80, 92), (94, 98)]), 'blond', 'b')],
    'side': [L(outline([(52, 40), (56, 70), (46, 90), (26, 94), (10, 80), (8, 50), (12, 36)]), 'buzz'),
             L(outline([(54, 56), (60, 54), (62, 82), (56, 84)]), 'band', 'f', ln=True),
             L(outline([(4, 44), (0, 26, 1), (12, 22), (14, 2, 1), (30, 8), (40, -12, 1), (52, 4), (66, -10, 1), (68, 8), (86, 6, 1), (80, 22), (94, 30, 1), (78, 36),
                        (60, 40), (36, 38), (16, 46)]), 'mid', 'f'),
             L(outline([(4, 84), (24, 88), (36, 100), (16, 106, 1), (10, 98), (-6, 100, 1)]), 'blond', 'f', ln=True)],
    'back': [L(outline([(14, 86), (12, 36), (88, 36), (86, 86), (50, 94)]), 'buzz'),
             L(outline([(8, 40), (2, 20, 1), (14, 18), (16, 0, 1), (30, 6), (40, -14, 1), (50, 2), (62, -14, 1), (66, 4), (84, -2, 1), (82, 14), (98, 20, 1), (92, 40),
                        (50, 46)]), 'mid', 'f'),
             L(outline([(14, 82), (50, 90), (86, 82), (96, 98, 1), (76, 96), (66, 108, 1), (56, 98), (44, 108, 1), (36, 98), (20, 104, 1), (6, 96, 1)]), 'blond', 'f', ln=True)],
}

# Nixon Earlnight: pelo gris plata liso peinado de lado con mechones largos que caen por la frente y a los lados; gafas finas
# de montura dorada y ojos naranjas
CHARS['nixon-earlnight'] = {
    'body': 'delgado', 'pal': pal('#d4d0c4', '#fcdcbc', iris='#d87a1e', shade='#a8988c'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': False, 'glasses': (200, 170, 90, 255), 'glasses_rect': True},
    'front': [L(outline([(12, 90), (8, 54), (12, 24), (28, 6), (50, 0), (72, 6), (88, 24), (92, 54), (88, 90), (82, 66), (18, 66)])),
              L(outline([(60, 4), (84, 16), (92, 50), (86, 84), (80, 50)]), 'shade', 'b', False),
              fringe([(10, 78), (12, 42), (26, 18), (50, 8), (74, 18), (88, 42), (90, 78), (82, 60), (74, 44), (68, 58, 1), (60, 30), (54, 44), (48, 28), (40, 60, 1),
                      (34, 36), (24, 64, 1), (18, 54)]),
              strand([(50, 10), (46, 26)], 'shade', 'f', 1.2), strand([(58, 12), (64, 30)], 'shade', 'f', 1.0)],
    'side': [L(outline([(54, 62), (58, 48), (80, 46), (92, 32), (86, 12), (64, -2), (36, -2), (14, 10), (4, 34), (6, 62), (16, 86), (30, 92), (42, 80)]), 'shade'),
             L(outline([(14, 10), (36, -2), (64, -2), (86, 12), (92, 32), (60, 30), (30, 40), (8, 46)]), 'mid', 'b', False),
             fringe([(64, 0), (86, 12), (96, 30), (100, 70, 1), (88, 56), (82, 64, 1), (78, 40), (66, 28)])],
    'back': [L(outline([(12, 88), (8, 54), (12, 24), (28, 6), (50, 0), (72, 6), (88, 24), (92, 54), (88, 88), (66, 94), (50, 100, 1), (34, 94)]), 'shade'),
             L(outline([(10, 44), (12, 24), (28, 6), (50, 0), (72, 6), (88, 24), (90, 44), (70, 36), (50, 40), (30, 36)]), 'mid', 'b', False)],
}

# Jack Balance: un casco de pelo en forma de champiñón enorme que le tapa los ojos, mitad crema y mitad verde, con el borde
# de abajo más oscuro; solo se le ven la nariz y la sonrisa
CHARS['jack-balance'] = {
    'body': 'bajito', 'pal': pal('#f6eec4', '#fcdcbc', shade='#c8ae84', green='#2a8a3a', green_d='#1e6a2a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(-10, 76), (-12, 50), (0, 20), (20, 0), (50, -8), (80, 0), (100, 20), (112, 50), (110, 76), (50, 82)])),
              L(outline([(40, -6), (50, -8), (80, 0), (100, 20), (112, 50), (110, 76), (70, 80), (60, 50), (50, 20)]), 'green'),
              L(outline([(-11, 64), (50, 70), (111, 64), (110, 78), (50, 84), (-10, 78)]), 'shade', 'b', False),
              L(outline([(70, 68), (111, 64), (110, 78), (70, 82)]), 'green_d', 'b', False),
              strand([(4, 70), (6, 80)], OUTC, 'b', 0.8), strand([(30, 72), (30, 82)], OUTC, 'b', 0.8), strand([(70, 72), (70, 82)], OUTC, 'b', 0.8),
              strand([(96, 70), (94, 80)], OUTC, 'b', 0.8),
              L(ell(50, 88, 3, 2.4), 'skin_d', 'f', False)],
    'side': [L(outline([(-10, 80), (-12, 50), (0, 20), (20, 0), (50, -8), (80, 0), (100, 20), (108, 50), (106, 78), (50, 84)])),
             L(outline([(80, 0), (100, 20), (108, 50), (106, 78), (96, 80), (94, 40)]), 'green'),
             L(outline([(-11, 66), (50, 72), (107, 66), (106, 80), (50, 86), (-10, 80)]), 'shade', 'b', False)],
    'back': [L(outline([(-10, 80), (-12, 50), (0, 20), (20, 0), (50, -8), (80, 0), (100, 20), (112, 50), (110, 80), (50, 86)])),
             L(outline([(20, 0), (50, -8), (56, 20), (40, 60), (34, 84), (-10, 80), (-12, 50), (0, 20)]), 'green'),
             L(outline([(-11, 66), (50, 72), (111, 66), (110, 80), (50, 86), (-10, 80)]), 'shade', 'b', False)],
}
