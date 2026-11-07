"""Unlimited Shining (go-unlimited-shining): sus modelos 3D de Inazuma Eleven GO como referencia (busto de frente, perfil y
espalda). Albion, Candido, Dwight, Beamer, Dawntavius y Bailong juegan también en el Equipo Zero y están en chars_go_zero."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Chandler Blanc: pelo gris pardo en una cúpula terminada en pico, con un ala ancha que se abre por detrás y a los lados como
# un sombrero, y la frente al descubierto en forma de U partida por un mechón; cara alargada y pálida
CHARS['chandler-blanc'] = {
    'body': 'delgado', 'pal': pal('#8a7a6a', '#f8e8c8', iris='#2a1e1a', shade='#6a5a4e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 60), (-36, 70), (-44, 80, 1), (14, 82), (86, 82), (144, 80, 1), (136, 70), (88, 60)]), 'shade', 'b'),
              L(outline([(12, 80), (8, 44), (18, 14), (36, -6), (50, -20, 1), (64, -6), (82, 14), (92, 44), (88, 80), (80, 60), (20, 60)])),
              L(outline([(56, -10), (80, 12), (90, 46), (84, 74), (76, 40)]), 'shade', 'b', False),
              L(outline([(30, 64), (28, 42), (34, 26), (42, 22), (46, 34), (48, 52), (52, 52), (54, 34), (58, 22), (66, 26), (72, 42), (70, 64)]), 'skin', 'f', ln=True)],
    'side': [L(outline([(54, 60), (60, 40), (78, 30), (82, 10), (68, -8), (40, -10), (18, 2), (6, 26), (-4, 52), (-36, 64), (-44, 74, 1), (2, 74), (22, 82), (40, 74)])),
             L(outline([(4, 34), (24, 40), (26, 74), (-10, 70)]), 'shade', 'b', False),
             L(outline([(60, 0), (72, 2), (78, 24), (70, 18)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 64), (-36, 72), (-44, 82, 1), (14, 86), (86, 86), (144, 82, 1), (136, 72), (86, 64)]), 'shade', 'b'),
             L(outline([(14, 80), (8, 44), (18, 14), (36, -6), (50, -20, 1), (64, -6), (82, 14), (92, 44), (86, 80), (50, 86)])),
             L(outline([(56, -10), (82, 14), (92, 50), (86, 80), (62, 84)]), 'shade', 'b', False)],
}

# Beacon Noor: piel morena, pelo verde azulado en casco liso con flequillo y dos mechones largos y finos que le caen delante
# de las orejas hasta el pecho; cejas gruesas verdes y ojos grandes
CHARS['beacon-noor'] = {
    'body': 'bajito', 'pal': pal('#1e8a74', '#a87048', iris='#1e1414', shade='#146a58'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 70), (6, 40), (16, 14), (50, 2), (84, 14), (94, 40), (90, 70), (82, 56), (18, 56)])),
              L(outline([(60, 4), (86, 16), (94, 44), (88, 64), (78, 40)]), 'shade', 'b', False),
              fringe([(8, 62), (12, 34), (28, 16), (50, 10), (72, 16), (88, 34), (92, 62), (84, 52), (78, 44), (72, 54, 1), (64, 42), (50, 50), (36, 42), (28, 54, 1),
                      (22, 44), (16, 52)]),
              L(outline([(10, 50), (18, 50), (18, 130), (10, 134, 1), (8, 100)]), 'mid', 'f', ln=True),
              L(outline([(90, 50), (82, 50), (82, 130), (90, 134, 1), (92, 100)]), 'mid', 'f', ln=True),
              L(outline([(24, 60), (42, 58), (42, 64), (26, 66)]), 'mid', 'f', ln=True), L(outline([(76, 60), (58, 58), (58, 64), (74, 66)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(52, 60), (58, 48), (80, 48), (92, 34), (88, 12), (66, 0), (38, 0), (14, 12), (4, 40), (8, 66), (20, 80), (36, 80), (46, 68)])),
             L(outline([(4, 40), (24, 42), (28, 74), (10, 70)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 40), (92, 50, 1), (84, 42), (74, 34)]),
             L(outline([(58, 48), (66, 48), (66, 130), (58, 134, 1)]), 'mid', 'f', ln=True),
             L(outline([(74, 60), (88, 60), (88, 64), (76, 66)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(10, 74), (6, 40), (16, 14), (50, 2), (84, 14), (94, 40), (90, 74), (70, 88), (30, 88)])),
             L(outline([(56, 4), (86, 16), (94, 48), (88, 74), (62, 86)]), 'shade', 'b', False),
             L(outline([(10, 66), (18, 66), (18, 130), (10, 134, 1), (8, 100)]), 'mid', 'f', ln=True),
             L(outline([(90, 66), (82, 66), (82, 130), (90, 134, 1), (92, 100)]), 'mid', 'f', ln=True)],
}

# Brighton Spark: pelo castaño claro en media melena acampanada que se abre hacia fuera a la altura de la mandíbula, con un
# mechón rizado en la frente y una antena por detrás; ojos azul grisáceo de ceño fruncido
CHARS['brighton-spark'] = {
    'body': 'normal', 'pal': pal('#9a7448', '#fcdcc0', iris='#5a6a98', shade='#7a5634'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(18, 82), (-8, 96, 1), (-2, 80), (4, 50), (10, 18), (30, 2), (50, -2), (70, 2), (90, 18), (96, 50), (102, 80), (108, 96, 1), (82, 82), (80, 60),
                         (20, 60)])),
              L(outline([(60, 2), (88, 16), (98, 50), (100, 86), (86, 78), (80, 44)]), 'shade', 'b', False),
              fringe([(12, 64), (14, 38), (28, 18), (50, 12), (72, 18), (86, 38), (88, 64), (78, 52), (66, 58, 1), (58, 44), (48, 54, 1), (40, 42), (30, 58, 1),
                      (22, 48)]),
              L(outline([(56, 22), (66, 14), (74, 20), (68, 30), (62, 26)]), 'shade', 'f', ln=True)],
    'side': [L(outline([(52, 64), (56, 52), (80, 48), (92, 34), (88, 12), (66, -2), (36, 0), (14, 14), (4, 40), (-6, 70), (-20, 84, 1), (10, 82), (34, 84), (46, 74)])),
             L(outline([(-6, 66), (6, 40), (28, 44), (34, 80), (-14, 82)]), 'shade', 'b', False),
             L(quad((70, 0), (80, -12), (94, -8)), 'mid', 'b', False, False, 2.4),
             fringe([(64, 2), (90, 16), (96, 42), (92, 58, 1), (84, 46), (76, 34)])],
    'back': [L(outline([(14, 70), (-14, 84, 1), (-6, 70), (4, 50), (10, 18), (30, 2), (50, -2), (70, 2), (90, 18), (96, 50), (106, 70), (114, 84, 1), (86, 76), (50, 82)])),
             L(outline([(56, 2), (88, 16), (98, 50), (106, 78), (60, 80)]), 'shade', 'b', False)],
}

# Laban Lux: pelo celeste claro en media melena recta con flequillo cortado, dos pequeñas puntas arriba como orejas de gato y
# dos adornos redondos en la frente; ojos ámbar con raya negra
CHARS['laban-lux'] = {
    'body': 'normal', 'pal': pal('#a8e0ea', '#fcdcc0', iris='#c8941e', shade='#8a8e94', dot='#a8e0ea'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 96), (4, 70), (6, 30), (10, 4), (-2, -14, 1), (24, -2), (50, -6), (76, -2), (102, -14, 1), (90, 4), (94, 30), (96, 70), (88, 96), (82, 66),
                         (18, 66)])),
              L(outline([(60, -2), (88, 10), (96, 50), (90, 90), (80, 50)]), 'shade', 'b', False),
              fringe([(8, 84), (8, 40), (20, 14), (50, 6), (80, 14), (92, 40), (92, 84), (84, 70), (82, 54), (72, 56), (60, 54), (50, 56), (40, 54), (28, 56), (18, 54),
                      (16, 70)]),
              L(ell(42, 62, 3.4, 3.4), 'dot', 'f', ln=True), L(ell(58, 62, 3.4, 3.4), 'dot', 'f', ln=True)],
    'side': [L(outline([(54, 66), (58, 56), (80, 54), (92, 40), (90, 12), (96, -6, 1), (74, 0), (44, -4), (18, 8), (6, 34), (2, 70), (6, 94, 1), (20, 86), (30, 96, 1),
                        (40, 84)]), 'shade'),
             L(outline([(18, 8), (44, -4), (74, 0), (96, -6, 1), (90, 12), (92, 40), (80, 54), (60, 46), (40, 30)]), 'mid', 'b', False),
             fringe([(66, 4), (90, 16), (96, 42), (94, 72), (86, 62), (82, 50), (74, 40)])],
    'back': [L(outline([(10, 92), (4, 70), (6, 30), (10, 4), (-2, -14, 1), (24, -2), (50, -6), (76, -2), (102, -14, 1), (90, 4), (94, 30), (96, 70), (90, 92), (76, 86),
                        (68, 96, 1), (60, 86), (40, 86), (32, 96, 1), (24, 86)]), 'shade'),
             L(outline([(10, 4), (-2, -14, 1), (24, -2), (50, -6), (76, -2), (102, -14, 1), (90, 4), (94, 30), (70, 26), (50, 30), (30, 26), (6, 30)]), 'mid', 'b', False)],
}

# Filbert Weissman: piel morena, pelo rubio echado hacia atrás en puntas con una cinta morada ancha en la frente, un mechón
# rizado que le cae por delante de un ojo y una melena larga que baja por la espalda; mirada de párpados caídos
CHARS['filbert-weissman'] = {
    'body': 'normal', 'pal': pal('#f0d070', '#8a5a30', iris='#1e1414', shade='#c8a050', band='#6a2a7a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 72), (10, 40), (0, 30), (-14, 10, 1), (8, 14), (14, -10, 1), (30, 6), (40, -26, 1), (52, 0), (70, -20, 1), (72, 4), (92, -6, 1), (88, 20),
                         (96, 40), (90, 72), (82, 54), (18, 54)])),
              L(outline([(56, 2), (84, 10), (94, 44), (86, 66), (78, 40)]), 'shade', 'b', False),
              L(outline([(8, 50), (10, 32), (50, 22), (90, 32), (92, 50), (50, 42)]), 'band', 'f', ln=True),
              L(outline([(30, 44), (36, 64), (44, 84), (40, 100), (30, 92), (34, 80), (26, 62)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(54, 56), (60, 44), (82, 44), (90, 26), (98, 4, 1), (78, 6), (74, -20, 1), (58, -2), (34, -10), (14, 2), (2, 24), (-10, 60), (-20, 104), (-8, 122, 1),
                        (-2, 100), (10, 72), (26, 60), (40, 64)])),
             L(outline([(-4, 50), (12, 48), (4, 90), (-14, 104)]), 'shade', 'b', False),
             L(outline([(4, 40), (8, 20), (50, 10), (92, 20), (92, 40), (50, 32)]), 'band', 'f', ln=True),
             L(outline([(76, 40), (86, 60), (84, 78), (78, 70), (80, 56)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(14, 70), (8, 40), (-6, 30), (-14, 10, 1), (10, 12), (14, -10, 1), (30, 6), (40, -26, 1), (52, 0), (70, -20, 1), (72, 4), (94, -6, 1), (88, 20),
                        (98, 40), (92, 70), (80, 100), (64, 120, 1), (56, 96), (44, 96), (36, 120, 1), (20, 100)])),
             L(outline([(56, 2), (86, 12), (96, 50), (84, 96), (60, 100)]), 'shade', 'b', False),
             L(outline([(6, 52), (8, 32), (50, 24), (92, 32), (94, 52), (50, 46)]), 'band', 'f', ln=True)],
}
