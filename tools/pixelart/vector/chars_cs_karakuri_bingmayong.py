"""Ejército de Terracota (cs-karakuri-bingmayong): los guerreros de terracota (todos con el mismo modelo 3D de Chrono Stone)
y los generales Guan Yu y Zhang Fei (sin modelo 3D: dibujados a partir de su retrato)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from heads import quad  # noqa: F401


def rect(x0, y0, x1, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


# Guerrero de terracota: cara de barro beige como una máscara, con rendijas negras rectangulares en los ojos y la boca
# abierta, dos líneas de juntura que bajan por las mejillas y la nariz recta; pelo castaño en casquete con un moño alto.
# 'terracotta-warrior' sirve para todos (terracotta-warrior-1 ... -11) por el prefijo.
_mask = [L(rect(26, 70, 44, 80), OUTC, 'f', False), L(rect(30, 73, 40, 77), 'skin', 'f', False),
         L(rect(56, 70, 74, 80), OUTC, 'f', False), L(rect(60, 73, 70, 77), 'skin', 'f', False),
         L(rect(40, 90, 60, 97), OUTC, 'f', False),
         L(outline([(46, 74), (54, 74), (56, 86), (44, 86)]), 'skin_d', 'f', ln=True),
         L([(26, 52), (28, 96)], OUTC, 'f', False, False, 1.0), L([(74, 52), (72, 96)], OUTC, 'f', False, False, 1.0)]
CHARS['terracotta-warrior'] = {
    'body': 'normal', 'pal': pal('#6a5038', '#e8d2aa', iris='#1e1414', skin_d='#c8b088', shade='#54402c'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False, 'big_ears': 1},
    'front': [L(outline([(38, 14), (38, -12), (44, -20), (56, -20), (62, -12), (62, 14)])),
              L(outline([(14, 58), (12, 30), (24, 12), (50, 6), (76, 12), (88, 30), (86, 58), (74, 48), (26, 48)]), 'mid', 'f'),
              L(outline([(60, 10), (80, 18), (88, 40), (84, 56), (74, 46)]), 'shade', 'f', False),
              L(outline([(44, -14), (50, -16), (48, 4)]), 'light', 'b', False)] + _mask,
    'side': [L(outline([(28, 12), (28, -12), (34, -20), (46, -20), (52, -12), (52, 10)])),
             L(outline([(74, 50), (84, 32), (74, 10), (50, 4), (24, 8), (10, 30), (8, 62), (14, 88), (30, 96), (42, 82), (50, 60), (60, 52)]), 'mid', 'f'),
             L(outline([(10, 40), (26, 46), (30, 84), (14, 82)]), 'shade', 'f', False),
             L(rect(78, 70, 88, 80), OUTC, 'f', False), L(rect(80, 73, 86, 77), 'skin', 'f', False),
             L(rect(84, 90, 92, 96), OUTC, 'f', False), L([(64, 54), (66, 96)], OUTC, 'f', False, False, 1.0)],
    'back': [L(outline([(38, 14), (38, -12), (44, -20), (56, -20), (62, -12), (62, 14)])),
             L(outline([(14, 70), (12, 30), (24, 12), (50, 6), (76, 12), (88, 30), (86, 70), (70, 88), (30, 88)])),
             L(outline([(56, -18), (62, -12), (62, 12), (80, 18), (88, 40), (86, 70), (64, 86)]), 'shade', 'b', False)],
}

# Guan Yu: general de piel tostada con la cara roja de guerrero, cejas gruesas y una barba negra larguísima que le cae
# hasta el pecho; gorro azul marino con un adorno dorado de nubes y una bola dorada arriba
CHARS['guan-yu'] = {
    'body': 'corpulento', 'pal': pal('#1a1a22', '#d8946a', iris='#1e1414', cap='#22306a', cap_d='#16204a', gold='#e8b830', nose='#c03424'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'hairline': False, 'nose': (50, 84, 3.4)},
    'front': [L(outline([(12, 56), (10, 26), (24, 6), (50, -2), (76, 6), (90, 26), (88, 56), (50, 48)]), 'cap', 'f'),
              L(outline([(60, 2), (82, 12), (90, 32), (88, 54), (70, 50)]), 'cap_d', 'f', False),
              L(ell(50, 26, 16, 9), 'gold', 'f', ln=True), L(ell(44, 26, 5, 4), 'cap', 'f', False), L(ell(56, 26, 5, 4), 'cap', 'f', False),
              L(ell(50, -8, 7, 7), 'gold', 'f', ln=True),
              L(outline([(14, 74), (20, 96), (32, 108), (40, 128), (50, 150, 1), (60, 128), (68, 108), (80, 96), (86, 74), (82, 100), (64, 112), (36, 112), (18, 100)]),
                'mid', 'f'),
              L(outline([(30, 98), (42, 92), (50, 96), (58, 92), (70, 98), (62, 102), (50, 100), (38, 102)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(70, 52), (86, 40), (84, 16), (64, 2), (36, 0), (14, 12), (6, 36), (8, 56), (40, 52)]), 'cap', 'f'),
             L(ell(52, 22, 10, 7), 'gold', 'f', ln=True), L(ell(44, -8, 7, 7), 'gold', 'f', ln=True),
             L(outline([(10, 56), (6, 80), (16, 94), (30, 90), (34, 70)])),
             L(outline([(62, 82), (74, 96), (84, 104), (84, 126), (76, 150, 1), (66, 124), (56, 106), (50, 96)]), 'mid', 'f')],
    'back': [L(outline([(14, 84), (10, 56), (90, 56), (86, 84), (50, 92)])),
             L(outline([(12, 58), (10, 26), (24, 6), (50, -2), (76, 6), (90, 26), (88, 58), (50, 62)]), 'cap', 'f'),
             L(outline([(60, 2), (82, 12), (90, 32), (88, 58), (66, 60)]), 'cap_d', 'f', False),
             L(ell(50, -8, 7, 7), 'gold', 'f', ln=True)],
}

# Zhang Fei: general de pelo castaño enmarañado de pinchos, una diadema dorada con espirales en la frente y una barba poblada
# que le rodea toda la cara; ojos verdes y dientes apretados de rabia
CHARS['zhang-fei'] = {
    'body': 'corpulento', 'pal': pal('#8a5a3a', '#f0b890', iris='#2a8a3a', gold='#e8b830'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 66), (-4, 58, 1), (6, 46), (-6, 30, 1), (12, 24), (10, 2, 1), (28, 10), (32, -14, 1), (44, 4), (52, -18, 1), (60, 4), (72, -12, 1),
                         (74, 10), (92, 4, 1), (88, 24), (106, 30, 1), (94, 46), (104, 58, 1), (90, 66), (84, 52), (16, 52)])),
              L(outline([(58, 0), (84, 12), (96, 40), (90, 62), (80, 40)]), 'shade', 'b', False),
              L(outline([(14, 50), (16, 38), (50, 32), (84, 38), (86, 50), (50, 44)]), 'gold', 'f', ln=True),
              L(ell(42, 41, 4, 3) + [ell(42, 41, 4, 3)[0]], 'shade', 'f', False, False, 1.4), L(ell(58, 41, 4, 3) + [ell(58, 41, 4, 3)[0]], 'shade', 'f', False, False, 1.4),
              L(outline([(10, 64), (4, 88), (14, 110), (30, 124), (50, 130, 1), (70, 124), (86, 110), (96, 88), (90, 64), (84, 86), (72, 106), (50, 110), (28, 106),
                         (16, 86)]), 'mid', 'f'),
              L(outline([(30, 90), (42, 86), (50, 90), (58, 86), (70, 90), (62, 94), (50, 92), (38, 94)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(56, 54), (64, 42), (84, 40), (90, 26), (82, 8), (92, -4, 1), (70, 0), (60, -18, 1), (46, 0), (26, -12, 1), (22, 8), (-2, 6, 1), (8, 24),
                        (-14, 34, 1), (4, 44), (-10, 60, 1), (8, 62), (4, 80, 1), (20, 76), (36, 74), (48, 64)])),
             L(outline([(52, 48), (92, 40), (94, 48), (54, 56)]), 'gold', 'f', ln=True),
             L(outline([(50, 72), (60, 98), (76, 116), (94, 120), (96, 104), (90, 92), (78, 102), (64, 90), (58, 70)]), 'mid', 'f')],
    'back': [L(outline([(14, 84), (2, 70, 1), (8, 58), (-6, 42, 1), (10, 34), (8, 8, 1), (26, 14), (32, -12, 1), (44, 6), (52, -16, 1), (60, 6), (72, -10, 1),
                        (76, 14), (94, 8, 1), (90, 34), (106, 42, 1), (92, 58), (98, 70, 1), (86, 84), (66, 92), (50, 102, 1), (34, 92)])),
             L(outline([(56, 2), (84, 14), (94, 46), (88, 80), (64, 88)]), 'shade', 'b', False),
             L([(8, 46), (50, 40), (92, 46)], 'gold', 'b', False, False, 4.0)],
}
