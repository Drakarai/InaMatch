"""Colmillos del Norte (go-northern-fang): sus modelos 3D de Inazuma Eleven GO como referencia (busto de frente, perfil y espalda)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from heads import quad  # noqa: F401
from chars_go_raimon import fringe

WHITE = (250, 250, 250, 255)

# Los demás jugadores están en chars_go_demon_s_horn.py (Cuerno Demoníaco junta a los de Garras del Sur y Colmillos del Norte).

# Jude Osbourne: piel morena, pelo azul petróleo en forma de casco con dos grandes puntas hacia arriba y a los lados, como una
# cola de pez, y una máscara blanca con pico que le tapa los ojos; boca torcida
CHARS['jude-osbourne'] = {
    'body': 'normal', 'pal': pal('#2e5a7a', '#a8704a', iris='#1e1414', mask='#eef0f6', mask_d='#a8b0c8'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 102, 'hairline': False},
    'front': [L(outline([(14, 70), (10, 40), (0, 20), (-14, -16, 1), (20, 4), (50, 10), (80, 4), (114, -16, 1), (100, 20), (90, 40), (86, 70), (80, 56), (20, 56)])),
              L(outline([(60, 8), (100, -6), (90, 30), (86, 64), (78, 30)]), 'shade', 'b', False),
              L(outline([(18, 50), (20, 34), (50, 30), (80, 34), (82, 50), (72, 76), (58, 70), (50, 92, 1), (42, 70), (28, 76)]), 'mask', 'f', ln=True),
              L(outline([(50, 70), (58, 70), (54, 90), (50, 92)]), 'mask_d', 'f', False),
              L(quad((30, 56), (36, 62), (34, 72)), OUTC, 'f', False, False, 1.6), L(quad((70, 56), (64, 62), (66, 72)), OUTC, 'f', False, False, 1.6)],
    'side': [L(outline([(56, 56), (64, 44), (84, 40), (90, 20), (76, 2), (60, -20, 1), (40, 0), (14, 8), (2, 30), (4, 60), (16, 80), (34, 80), (46, 68)])),
             L(outline([(6, 36), (24, 40), (26, 72), (10, 66)]), 'shade', 'b', False),
             L(outline([(70, 46), (92, 40), (112, 76, 1), (96, 78), (82, 76), (72, 66)]), 'mask', 'f', ln=True),
             L(outline([(90, 64), (112, 76, 1), (94, 76)]), 'mask_d', 'f', False)],
    'back': [L(outline([(14, 70), (10, 40), (0, 20), (-14, -16, 1), (20, 4), (50, 10), (80, 4), (114, -16, 1), (100, 20), (90, 40), (86, 70), (66, 88), (50, 104, 1),
                        (34, 88)])),
             L(outline([(52, 10), (100, -6), (90, 40), (84, 72), (56, 96)]), 'shade', 'b', False)],
}

# Bill Froger: carita redonda morena con manchas oscuras alrededor de los ojos y nariz naranja; el pelo blanco en casco
# pegado a la cabeza con dos cuernos enormes curvados hacia arriba (blancos por fuera, oscuros por dentro); dientes de conejo
CHARS['bill-froger'] = {
    'body': 'bajito', 'pal': pal('#f2ecda', '#9a6440', iris='#1e1414', shade='#c8a89a', inner='#24323a', patch='#4a2a1e', nose='#e8742a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'buck', 'mouth_y': 102, 'hairline': False, 'nose': (50, 90, 2.4)},
    'front': [L(outline([(16, 40), (6, 20), (-14, 10), (-20, -10), (-12, -40, 1), (-4, -14), (14, 0), (30, 4)]), 'mid', 'b'),
              L(outline([(84, 40), (94, 20), (114, 10), (120, -10), (112, -40, 1), (104, -14), (86, 0), (70, 4)]), 'mid', 'b'),
              L(outline([(-12, -36, 1), (-8, -16), (4, -4), (-2, -14)]), 'inner', 'b', False), L(outline([(112, -36, 1), (108, -16), (96, -4), (102, -14)]), 'inner', 'b', False),
              L(outline([(16, 66), (12, 40), (22, 14), (50, 6), (78, 14), (88, 40), (84, 66), (78, 54), (62, 52), (50, 64, 1), (38, 52), (22, 54)]), 'mid', 'f'),
              L(outline([(60, 10), (82, 22), (88, 46), (80, 56), (74, 30)]), 'shade', 'f', False),
              L(ell(36, 76, 10, 8), 'patch', 'f', False), L(ell(64, 76, 10, 8), 'patch', 'f', False),
              L(ell(37, 77, 3, 2.4), WHITE, 'f', False), L(ell(63, 77, 3, 2.4), WHITE, 'f', False),
              L(ell(38, 77, 1.2, 1.6), OUTC, 'f', False), L(ell(62, 77, 1.2, 1.6), OUTC, 'f', False)],
    'side': [L(outline([(40, 20), (20, 4), (6, -14), (14, -40, 1), (22, -14), (36, 0), (56, 10)]), 'mid', 'b'),
             L(outline([(14, -36, 1), (18, -16), (28, -6), (20, -14)]), 'inner', 'b', False),
             L(outline([(56, 56), (64, 46), (84, 42), (90, 24), (76, 6), (50, 0), (24, 8), (10, 28), (8, 56), (18, 76), (34, 78), (46, 68)]), 'mid', 'f'),
             L(ell(82, 76, 6, 7), 'patch', 'f', False), L(ell(84, 76, 1.4, 1.8), WHITE, 'f', False)],
    'back': [L(outline([(16, 40), (6, 20), (-14, 10), (-20, -10), (-12, -40, 1), (-4, -14), (14, 0), (30, 4)]), 'mid', 'b'),
             L(outline([(84, 40), (94, 20), (114, 10), (120, -10), (112, -40, 1), (104, -14), (86, 0), (70, 4)]), 'mid', 'b'),
             L(outline([(16, 70), (12, 40), (22, 14), (50, 6), (78, 14), (88, 40), (84, 70), (66, 82), (34, 82)])),
             L(outline([(56, 10), (82, 22), (88, 50), (80, 72), (60, 80)]), 'shade', 'b', False)],
}

# Caesar Lionheart: pálido, pelo morado largo hasta la espalda con dos mechones enroscados hacia arriba a los lados de la
# cabeza como cuernos y un flequillo en pico sobre la frente; ojos ámbar adormilados y boca entreabierta
CHARS['caesar-lionheart'] = {
    'body': 'delgado', 'pal': pal('#4e2e6a', '#fcecdc', iris='#d8941e', light='#7a5a9a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(14, 70), (2, 40), (-10, 20), (-14, -6, 1), (8, 10), (30, 2), (50, 0), (70, 2), (92, 10), (114, -6, 1), (110, 20), (98, 40), (92, 80), (98, 110),
                         (80, 104), (80, 64), (20, 64), (20, 104), (2, 110), (8, 80)])),
              L(outline([(60, 2), (86, 12), (96, 50), (94, 100), (84, 90), (80, 40)]), 'shade', 'b', False),
              fringe([(12, 66), (14, 40), (26, 20), (50, 12), (74, 20), (86, 40), (88, 66), (80, 54), (66, 46), (56, 54), (50, 76, 1), (44, 54), (34, 46), (20, 54)]),
              L(outline([(40, 8), (54, 6), (48, 20), (36, 20)]), 'light', 'f', False)],
    'side': [L(outline([(56, 62), (60, 50), (82, 50), (94, 34), (88, 12), (66, -2), (36, -2), (14, 10), (2, 36), (-6, 70), (-8, 100), (6, 116), (24, 110), (36, 96), (48, 76)])),
             L(outline([(44, 20), (40, 0), (50, -14, 1), (56, 6), (54, 22)]), 'mid', 'f', ln=True),
             L(outline([(0, 50), (24, 50), (30, 100), (6, 108)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 40), (92, 58, 1), (84, 44), (74, 34)])],
    'back': [L(outline([(14, 70), (2, 40), (-10, 20), (-14, -6, 1), (8, 10), (30, 2), (50, 0), (70, 2), (92, 10), (114, -6, 1), (110, 20), (98, 40), (96, 80), (100, 120),
                        (70, 130), (50, 124), (30, 130), (0, 120), (4, 80)])),
             L(outline([(56, 2), (90, 12), (98, 50), (100, 116), (70, 126), (70, 40)]), 'shade', 'b', False),
             strand([(30, 40), (24, 120)], 'deep', 'b', 1.0), strand([(70, 40), (76, 120)], 'deep', 'b', 1.0)],
}

# Stan Roller: piel morena, melena azul marino oscuro enorme y salvaje de pinchos en todas direcciones, con una cinta roja en la
# frente; gesto furioso con la boca abierta
CHARS['stan-roller'] = {
    'body': 'corpulento', 'pal': pal('#24244e', '#b07448', iris='#1e1414', band='#c82a2a', mouth='#7a1e1e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(14, 76), (-6, 80, 1), (4, 64), (-16, 54, 1), (0, 44), (-12, 26, 1), (8, 22), (4, 0, 1), (22, 6), (28, -18, 1), (42, -2), (54, -24, 1), (62, -2),
                         (80, -16, 1), (80, 4), (100, 0, 1), (94, 22), (114, 26, 1), (100, 44), (116, 54, 1), (96, 64), (106, 80, 1), (86, 76), (84, 56), (16, 56)])),
              L(outline([(60, -4), (86, 8), (100, 44), (92, 70), (80, 40)]), 'shade', 'b', False),
              fringe([(14, 64), (16, 44), (30, 34), (50, 30), (70, 34), (84, 44), (86, 64), (76, 56), (68, 62, 1), (60, 52), (50, 60, 1), (40, 52), (32, 62, 1), (24, 56)]),
              L(outline([(14, 52), (30, 46), (50, 44), (70, 46), (86, 52), (84, 59), (70, 53), (50, 51), (30, 53), (16, 59)]), 'band', 'f', ln=True)],
    'side': [L(outline([(58, 58), (64, 46), (84, 46), (92, 30), (86, 12), (100, -4, 1), (76, 0), (70, -20, 1), (54, -4), (36, -18, 1), (28, 2), (0, -6, 1), (10, 16),
                        (-18, 24, 1), (2, 38), (-20, 50, 1), (2, 58), (-14, 76, 1), (8, 76), (0, 96, 1), (20, 86), (24, 102, 1), (36, 84), (48, 70)])),
             L(outline([(0, 40), (22, 46), (26, 84), (6, 80)]), 'shade', 'b', False),
             L(outline([(54, 44), (70, 38), (90, 38), (92, 46), (72, 46), (56, 52)]), 'band', 'f', ln=True)],
    'back': [L(outline([(10, 92), (-12, 96, 1), (0, 78), (-20, 66, 1), (-2, 56), (-16, 38, 1), (4, 32), (-2, 8, 1), (18, 12), (24, -14, 1), (40, 0), (52, -22, 1), (60, 0),
                        (80, -14, 1), (80, 6), (102, 4, 1), (96, 28), (118, 34, 1), (102, 52), (120, 64, 1), (102, 76), (112, 96, 1), (90, 92), (78, 110, 1), (64, 96),
                        (50, 112, 1), (36, 96), (22, 110, 1)])),
             L(outline([(56, 0), (88, 10), (104, 54), (100, 96), (70, 98), (74, 40)]), 'shade', 'b', False),
             L(outline([(4, 46), (50, 40), (96, 46), (96, 54), (50, 48), (4, 54)]), 'band', 'f', ln=True)],
}
