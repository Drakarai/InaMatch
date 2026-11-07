"""Ragnah (cs-the-lagoon): sus modelos 3D de Inazuma Eleven GO 2: Chrono Stone como referencia (busto de frente, perfil y espalda).
Mehr y Ghiris también juegan en Gir: están dibujados en chars_cs_giru.py."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)


def fringe(pts, c='mid'):
    """Flequillo por delante de la cara (las puntas, con un tercer valor, afiladas)."""
    return L(outline(pts), c, 'f')


def braid(x0, y0, x1, y1, n=5, w=7, c='mid'):
    """Trenza: una fila de eslabones de x0,y0 a x1,y1."""
    out = []
    for i in range(n):
        t = (i + 0.5) / n
        out.append(L(ell(x0 + (x1 - x0) * t, y0 + (y1 - y0) * t, w * 0.62, (abs(y1 - y0) + abs(x1 - x0)) / n * 0.62), c, 'f', ln=True))
    return out


# Hippos Kohlt (portero): piel oscura, pelo gris claro en forma de seta ancha con dos puntas hacia los lados y un mechón
# que le cae sobre un ojo; una protección blanca le baja por los lados de la cara
CHARS['hippos-kohlt'] = {
    'body': 'normal', 'pal': pal('#c8bcc4', '#9a5a34', iris='#1e1414', guard='#f2eeee'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 70), (16, 74), (20, 104), (30, 112), (14, 108), (8, 90)]), 'guard', 'f', ln=True),
              L(outline([(90, 70), (84, 74), (80, 104), (70, 112), (86, 108), (92, 90)]), 'guard', 'f', ln=True),
              L(outline([(14, 58), (-14, 22, 1), (10, 30), (24, 12), (50, 6), (76, 12), (90, 30), (114, 22, 1), (86, 58), (68, 52), (50, 56), (32, 52)]), 'mid', 'f'),
              L(outline([(60, 10), (86, 20), (108, 26), (84, 54), (74, 34)]), 'shade', 'f', False),
              L(outline([(46, 40), (60, 44), (66, 64), (64, 92, 1), (56, 66), (46, 52)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(30, 30), (16, 52), (14, 82), (30, 96), (50, 92), (48, 60)]), 'guard', 'b', ln=True),
             L(outline([(74, 72), (80, 70), (84, 100), (76, 104)]), 'guard', 'f', ln=True),
             L(outline([(4, 46), (-20, 4, 1), (12, 16), (36, 4), (64, 2), (84, 10), (96, 24), (94, 52), (78, 46), (60, 50), (40, 44), (20, 50)]), 'mid', 'f'),
             L(outline([(84, 30), (98, 44), (96, 80, 1), (88, 52)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(14, 52), (12, 90), (34, 100), (66, 100), (88, 90), (86, 52)]), 'guard', 'b', ln=True),
             L(outline([(12, 62), (-16, 18, 1), (12, 26), (28, 8), (50, 4), (72, 8), (88, 26), (116, 18, 1), (88, 62), (70, 54), (50, 64), (30, 54)]), 'mid', 'f'),
             L(outline([(56, 8), (86, 22), (110, 22), (86, 60), (66, 40)]), 'shade', 'f', False)],
}

# Anas Eidah: grandullón de pelo verde menta recogido en una coleta alta con goma amarilla, dos picos que salen hacia
# arriba a los lados y trenzas gordas que le cuelgan por los lados y la nuca
CHARS['anas-eidah'] = {
    'body': 'corpulento', 'pal': pal('#b8e4dc', '#f8d4b0', iris='#b81e1e', shade='#9aa4a0', deep='#7a8480', tie='#e8d040'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(12, 70), (8, 40), (14, 22), (10, -16, 1), (28, 12), (50, 2), (72, 12), (90, -16, 1), (86, 22), (92, 40), (88, 70), (80, 58), (20, 58)])),
              L(outline([(36, 6), (40, -10), (50, -14), (60, -10), (64, 6), (50, 8)])),
              L(ell(50, 0, 8, 3), 'tie', 'f', ln=True)]
             + braid(6, 30, 2, 110, 6, 9, 'shade') + braid(94, 30, 98, 110, 6, 9, 'shade')
             + [fringe([(12, 64), (14, 40), (28, 22), (50, 16), (72, 22), (86, 40), (88, 64), (78, 52), (70, 62, 1), (62, 48), (54, 62, 1), (50, 50), (46, 62, 1),
                        (38, 48), (30, 62, 1), (22, 52)])],
    'side': [L(outline([(54, 64), (58, 50), (80, 48), (94, 34), (88, 12), (90, -14, 1), (70, 4), (50, -4), (30, -6), (12, 10), (4, 36), (8, 64), (22, 80), (40, 78)])),
             L(outline([(30, -4), (20, -16), (8, -14), (4, 0), (16, 6)]), 'shade', 'b', ln=True), L(ell(26, -6, 4, 4), 'tie', 'f', ln=True)]
             + braid(14, -10, -16, 90, 6, 9, 'shade') + braid(22, 30, 6, 110, 6, 9, 'shade')
             + [L(outline([(4, 36), (26, 42), (28, 68), (10, 62)]), 'shade', 'b', False)],
    'back': [L(outline([(12, 74), (8, 40), (14, 22), (10, -16, 1), (28, 12), (50, 2), (72, 12), (90, -16, 1), (86, 22), (92, 40), (88, 74), (50, 82)]), 'shade'),
             L(outline([(36, 6), (40, -10), (50, -14), (60, -10), (64, 6), (50, 8)]), 'shade'), L(ell(50, 0, 8, 3), 'tie', 'f', ln=True)]
             + braid(50, 4, 50, 112, 7, 10, 'shade') + braid(6, 30, -2, 110, 6, 9, 'shade') + braid(94, 30, 102, 110, 6, 9, 'shade'),
}

# Djung Hamstah: piel morena, pelo lila de pinchos de punta hacia arriba y un flequillo liso en pico hasta la nariz; ojos
# rojos
CHARS['djung-hamstah'] = {
    'body': 'normal', 'pal': pal('#c8b8e0', '#c8885a', iris='#b81e1e', shade='#a090b0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 70), (10, 40), (12, 14), (8, -6, 1), (24, 6), (30, -24, 1), (40, 0), (50, -32, 1), (60, 0), (72, -24, 1), (76, 6), (92, -6, 1), (88, 14),
                         (90, 40), (84, 70), (80, 56), (20, 56)])),
              L(outline([(60, 0), (84, 12), (90, 40), (86, 64), (78, 40)]), 'shade', 'b', False),
              fringe([(12, 70), (14, 40), (28, 22), (50, 16), (72, 22), (86, 40), (88, 70), (80, 58), (70, 66, 1), (64, 48), (56, 60), (50, 86, 1), (44, 60),
                      (36, 48), (30, 66, 1), (20, 58)])],
    'side': [L(outline([(54, 60), (58, 48), (80, 46), (92, 32), (86, 10), (92, -16, 1), (70, -2), (66, -28, 1), (50, -6), (30, -22, 1), (28, 0), (2, -4, 1), (12, 16),
                        (4, 40), (8, 66), (22, 82), (40, 78)])),
             L(outline([(6, 36), (26, 42), (28, 70), (10, 64)]), 'shade', 'b', False),
             strand([(10, 50), (40, 52)], 'deep', 'b', 1.0), strand([(12, 62), (40, 64)], 'deep', 'b', 1.0),
             fringe([(64, 2), (88, 16), (94, 40), (92, 64, 1), (84, 48), (76, 32)])],
    'back': [L(outline([(14, 82), (10, 40), (12, 14), (8, -6, 1), (24, 6), (30, -24, 1), (40, 0), (50, -32, 1), (60, 0), (72, -24, 1), (76, 6), (92, -6, 1), (88, 14),
                        (90, 40), (86, 82), (50, 90)])),
             L(outline([(56, 0), (84, 12), (90, 46), (84, 80), (62, 88)]), 'shade', 'b', False),
             strand([(12, 56), (50, 60), (88, 56)], 'deep', 'b', 1.0), strand([(14, 70), (50, 74), (86, 70)], 'deep', 'b', 1.0)],
}

# Ewa Mouton: chica de pelo rosa claro en forma de seta grande que le hace de sombrero, con dos bolas de pelo rosa intenso
# a los lados de la espalda sujetas con brazaletes grises
CHARS['ewa-mouton'] = {
    'body': 'chica', 'pal': pal('#f2c0cc', '#fce4cc', iris='#2a1a1a', puff='#e880a8', puff_d='#c86088', cuff='#6a6a70'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(blob([(-10, 80), (-24, 104), (-8, 126), (16, 120), (20, 96)], 8), 'puff'), L(blob([(110, 80), (124, 104), (108, 126), (84, 120), (80, 96)], 8), 'puff'),
              L(outline([(10, 72), (14, 76), (22, 76), (22, 60), (16, 60)]), 'cuff', 'b', ln=True), L(outline([(90, 72), (86, 76), (78, 76), (78, 60), (84, 60)]), 'cuff', 'b', ln=True),
              L(outline([(16, 72), (14, 50), (86, 50), (84, 72), (50, 66)])),
              L(outline([(-4, 46), (-6, 30), (8, 8), (30, -6), (50, -10), (70, -6), (92, 8), (106, 30), (104, 46), (86, 54), (66, 48), (50, 54), (34, 48), (14, 54)]), 'mid', 'f'),
              L(outline([(60, -6), (90, 8), (104, 30), (102, 44), (86, 48), (78, 20)]), 'shade', 'f', False),
              strand([(20, 20), (40, 8)], 'deep', 'f', 1.0), strand([(60, 8), (80, 20)], 'deep', 'f', 1.0)],
    'side': [L(blob([(-4, 70), (-30, 92), (-20, 124), (10, 120), (14, 92)], 8), 'puff'),
             L(outline([(30, 64), (40, 66), (40, 94), (30, 92)]), 'cuff', 'b', ln=True),
             L(outline([(-6, 50), (-8, 30), (6, 6), (30, -8), (60, -10), (84, 0), (100, 20), (102, 40), (84, 48), (60, 42), (40, 48), (14, 54)]), 'mid', 'f'),
             L(outline([(-4, 30), (6, 40), (20, 50), (-4, 50)]), 'shade', 'f', False)],
    'back': [L(blob([(-10, 80), (-24, 104), (-8, 126), (16, 120), (20, 96)], 8), 'puff'), L(blob([(110, 80), (124, 104), (108, 126), (84, 120), (80, 96)], 8), 'puff'),
             L(outline([(16, 90), (14, 50), (86, 50), (84, 90), (50, 96)]), 'puff_d'),
             L(outline([(12, 76), (24, 76), (24, 98), (12, 98)]), 'cuff', 'f', ln=True), L(outline([(88, 76), (76, 76), (76, 98), (88, 98)]), 'cuff', 'f', ln=True),
             L(outline([(-4, 50), (-6, 30), (8, 8), (30, -6), (50, -10), (70, -6), (92, 8), (106, 30), (104, 50), (50, 60)]), 'mid', 'f'),
             L(outline([(56, -6), (90, 8), (104, 30), (102, 48), (60, 56)]), 'shade', 'f', False), strand([(50, -8), (50, 58)], 'deep', 'f', 1.0)],
}

# Katya Felis: chica de pelo naranja salmón ondulado hasta la mandíbula, con una trenza que le rodea la cabeza como una
# diadema y un mechón que le cae entre los ojos; ojos violeta
CHARS['katya-felis'] = {
    'body': 'chica', 'pal': pal('#f0905a', '#fce8d0', iris='#6a5aa8', shade='#c86a3a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 96), (-4, 92, 1), (0, 70), (-6, 44), (6, 16), (30, 2), (50, 0), (70, 2), (94, 16), (106, 44), (100, 70), (104, 92, 1), (90, 96), (84, 64),
                         (16, 64)])),
              L(outline([(60, 2), (90, 16), (104, 44), (98, 90), (84, 56)]), 'shade', 'b', False)]
             + braid(14, 18, 50, 2, 4, 9, 'shade') + braid(50, 2, 86, 18, 4, 9, 'shade')
             + [fringe([(10, 72), (12, 40), (26, 22), (50, 16), (74, 22), (88, 40), (90, 72), (82, 58), (74, 66, 1), (66, 46), (56, 54), (50, 84, 1), (46, 54), (36, 48),
                        (28, 66, 1), (18, 58)])],
    'side': [L(outline([(52, 70), (56, 56), (80, 50), (94, 36), (88, 12), (64, -2), (34, 0), (12, 14), (-2, 40), (-6, 70), (2, 96, 1), (16, 86), (26, 100, 1), (36, 86),
                        (46, 90, 1), (44, 78)])),
             L(outline([(-2, 40), (24, 46), (32, 92), (6, 92)]), 'shade', 'b', False)]
             + braid(66, 4, 86, 22, 3, 9, 'shade')
             + [fringe([(64, 2), (88, 16), (94, 40), (92, 64, 1), (84, 48), (76, 32)])],
    'back': [L(outline([(8, 96), (-4, 92, 1), (0, 70), (-6, 44), (6, 16), (30, 2), (50, 0), (70, 2), (94, 16), (106, 44), (100, 70), (104, 92, 1), (92, 96), (72, 104, 1),
                        (62, 94), (50, 106, 1), (38, 94), (28, 104, 1)])),
             L(outline([(56, 2), (90, 16), (104, 44), (100, 96), (66, 100)]), 'shade', 'b', False),
             strand([(26, 40), (20, 80)], 'deep', 'b', 1.0), strand([(74, 40), (80, 80)], 'deep', 'b', 1.0)],
}

# Macah Psitta: piel oscura y pelo blanco de pinchos en todas direcciones, con un mechón azul celeste que sale hacia arriba
# a la derecha; ojos negros enfadados
CHARS['macah-psitta'] = {
    'body': 'normal', 'pal': pal('#f2eeee', '#9a6038', iris='#1e1414', shade='#c8b8bc', deep='#a8989c', blue='#8ac8f0', blue_d='#5aa0d0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 86), (2, 92, 1), (6, 70), (-12, 60, 1), (4, 50), (-10, 30, 1), (10, 26), (8, 2, 1), (28, 10), (40, -16, 1), (54, 4), (70, -12, 1),
                         (76, 8), (100, 0, 1), (92, 24), (110, 34, 1), (94, 48), (108, 64, 1), (92, 70), (98, 90, 1), (84, 84), (84, 60), (16, 60)])),
              L(outline([(60, 4), (86, 16), (96, 46), (90, 80), (80, 50)]), 'shade', 'b', False),
              L(outline([(64, 20), (78, -10), (92, -16, 1), (86, 6), (96, 24, 1), (80, 30)]), 'blue', 'f', ln=True),
              fringe([(14, 66), (16, 40), (30, 22), (50, 16), (70, 22), (86, 40), (86, 66), (78, 54), (70, 64, 1), (62, 46), (54, 76, 1), (48, 46), (40, 62, 1),
                      (32, 48), (22, 64, 1)])],
    'side': [L(outline([(54, 62), (62, 48), (84, 46), (96, 30), (86, 10), (98, -6, 1), (70, 0), (60, -20, 1), (44, 0), (16, -10, 1), (16, 12), (-14, 18, 1), (4, 34),
                        (-18, 50, 1), (4, 56), (-10, 76, 1), (10, 76), (6, 96, 1), (24, 86), (32, 100, 1), (40, 82)])),
             L(outline([(4, 34), (24, 40), (28, 76), (8, 70)]), 'shade', 'b', False),
             L(outline([(50, 6), (66, -14), (82, -18, 1), (72, 2), (80, 14, 1), (62, 16)]), 'blue', 'f', ln=True),
             fringe([(66, 4), (90, 18), (94, 40), (92, 58, 1), (84, 44), (76, 32)])],
    'back': [L(outline([(16, 92), (0, 100, 1), (6, 72), (-14, 62, 1), (4, 50), (-12, 30, 1), (10, 26), (8, 0, 1), (28, 10), (40, -16, 1), (54, 4), (70, -12, 1), (76, 8),
                        (102, 0, 1), (92, 24), (112, 34, 1), (94, 50), (110, 66, 1), (92, 74), (100, 96, 1), (84, 92), (70, 104, 1), (60, 92), (48, 106, 1), (38, 92),
                        (28, 104, 1)])),
             L(outline([(56, 4), (86, 16), (98, 50), (92, 92), (64, 96)]), 'shade', 'b', False),
             L(outline([(36, 20), (22, -10), (8, -16, 1), (14, 6), (4, 24, 1), (20, 30)]), 'blue', 'f', ln=True)],
}

# Folie Vora: chica de piel morena y pelo blanco recogido en un moño con dos puntas largas como cuernos hacia arriba, flequillo
# de mechones y dos colitas a los lados de la nuca; ojos rosas
CHARS['folie-vora'] = {
    'body': 'chica', 'pal': pal('#f2ecec', '#a87050', iris='#c84aa8', shade='#c8b4b8', deep='#a8949a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(22, 10), (14, -30, 1), (30, -4)])), L(outline([(78, 10), (86, -30, 1), (70, -4)])),
              L(outline([(28, 10), (34, -10), (50, -16), (66, -10), (72, 10), (50, 8)])),
              L(outline([(12, 70), (2, 96), (6, 110, 1), (16, 96), (20, 74)])), L(outline([(88, 70), (98, 96), (94, 110, 1), (84, 96), (80, 74)])),
              L(outline([(14, 74), (8, 40), (18, 12), (50, 2), (82, 12), (92, 40), (86, 74), (80, 60), (20, 60)])),
              L(outline([(60, 4), (84, 16), (92, 44), (86, 66), (78, 40)]), 'shade', 'b', False),
              fringe([(12, 70), (14, 40), (28, 20), (50, 14), (72, 20), (86, 40), (88, 70), (80, 60), (76, 74, 1), (68, 52), (58, 62, 1), (54, 46), (46, 60, 1),
                      (40, 46), (30, 62, 1), (24, 50), (22, 74, 1), (16, 60)])],
    'side': [L(outline([(28, 4), (-4, -22, 1), (10, 10)])), L(outline([(26, 4), (30, -12), (46, -16), (58, -8), (56, 6)])),
             L(outline([(54, 66), (58, 52), (80, 48), (92, 34), (86, 12), (64, -2), (34, 0), (12, 14), (4, 40), (6, 66), (20, 80), (40, 78)])),
             L(outline([(16, 76), (10, 100), (14, 112, 1), (24, 96), (26, 78)])),
             L(outline([(4, 36), (26, 42), (30, 70), (10, 66)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 16), (94, 40), (92, 62, 1), (84, 46), (76, 32)])],
    'back': [L(outline([(22, 10), (14, -30, 1), (30, -4)])), L(outline([(78, 10), (86, -30, 1), (70, -4)])),
             L(outline([(28, 10), (34, -10), (50, -16), (66, -10), (72, 10), (50, 8)])),
             L(outline([(14, 76), (8, 40), (18, 12), (50, 2), (82, 12), (92, 40), (86, 76), (50, 84)])),
             L(outline([(56, 4), (84, 16), (92, 46), (86, 74), (62, 82)]), 'shade', 'b', False),
             L(outline([(14, 72), (4, 98), (8, 110, 1), (18, 98), (22, 76)]), 'mid', 'f', ln=True),
             L(outline([(86, 72), (96, 98), (92, 110, 1), (82, 98), (78, 76)]), 'mid', 'f', ln=True),
             strand([(50, 8), (50, 80)], 'deep', 'b', 1.0)],
}

# Simeon Ayp: pelo blanco de pinchos largos hacia arriba y a los lados, con unas gafas de aviador negras sobre la frente;
# ojos negros y sonrisa
CHARS['simeon-ayp'] = {
    'body': 'normal', 'pal': pal('#f4f0f0', '#f8cca0', iris='#1e1414', shade='#c8bcc0', deep='#a89ca0', gog='#1e1e22', lens='#b8a888'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 80), (0, 76, 1), (8, 62), (-8, 46, 1), (8, 36), (4, 10, 1), (24, 16), (30, -12, 1), (42, 4), (50, -24, 1), (58, 4), (70, -12, 1), (76, 16),
                         (96, 10, 1), (92, 36), (108, 46, 1), (92, 62), (100, 76, 1), (84, 80), (84, 60), (16, 60)])),
              L(outline([(60, 4), (86, 16), (96, 44), (90, 74), (80, 46)]), 'shade', 'b', False),
              fringe([(14, 70), (16, 42), (30, 26), (50, 20), (70, 26), (86, 42), (86, 70), (78, 58), (70, 68, 1), (62, 52), (54, 78, 1), (48, 50), (40, 66, 1),
                      (32, 52), (22, 68, 1)]),
              L(outline([(10, 44), (20, 34), (44, 36), (50, 40), (56, 36), (80, 34), (90, 44), (82, 54), (60, 52), (50, 46), (40, 52), (18, 54)]), 'gog', 'f', ln=True),
              L(ell(30, 44, 8, 5), 'lens', 'f', ln=True), L(ell(70, 44, 8, 5), 'lens', 'f', ln=True)],
    'side': [L(outline([(54, 64), (62, 50), (84, 46), (96, 32), (86, 12), (98, -2, 1), (70, 4), (62, -18, 1), (46, 2), (20, -10, 1), (20, 12), (-12, 20, 1), (4, 36),
                        (-16, 52, 1), (4, 58), (-8, 78, 1), (12, 76), (14, 94, 1), (28, 80), (44, 74)])),
             L(outline([(4, 36), (24, 42), (28, 74), (8, 68)]), 'shade', 'b', False),
             L(outline([(70, 30), (88, 28), (92, 42), (74, 46)]), 'gog', 'f', ln=True), L([(70, 38), (40, 44)], 'gog', 'f', False, False, 3.0),
             fringe([(66, 4), (90, 18), (94, 40), (92, 60, 1), (84, 46), (76, 34)])],
    'back': [L(outline([(16, 86), (-2, 82, 1), (8, 64), (-10, 46, 1), (8, 36), (4, 10, 1), (24, 16), (30, -12, 1), (42, 4), (50, -24, 1), (58, 4), (70, -12, 1), (76, 16),
                        (98, 10, 1), (92, 36), (110, 46, 1), (92, 64), (102, 82, 1), (84, 86), (70, 98, 1), (60, 88), (50, 100, 1), (40, 88), (30, 98, 1)])),
             L(outline([(56, 4), (86, 16), (98, 50), (92, 84), (64, 92)]), 'shade', 'b', False),
             L(quad((8, 50), (50, 58), (92, 50)), 'gog', 'f', False, False, 3.0)],
}

# Kyon Canis: pelo azul lavanda largo y liso, peinado hacia un lado, con mechones largos que le enmarcan la cara y caen por
# delante de los hombros; ojos celestes fríos
CHARS['kyon-canis'] = {
    'body': 'normal', 'pal': pal('#a8b8f0', '#fcecd8', iris='#3ac8d8', shade='#8a90c8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(8, 120), (-6, 126, 1), (-2, 80), (-4, 40), (8, 12), (30, -6), (60, -8), (84, 4), (98, 30), (104, 70), (110, 116, 1), (94, 106), (86, 70),
                         (16, 70)])),
              L(outline([(60, -4), (86, 8), (100, 40), (104, 106), (86, 70)]), 'shade', 'b', False),
              fringe([(10, 80), (10, 40), (22, 14), (46, 2), (70, 4), (86, 20), (92, 50), (88, 80), (80, 60), (72, 44), (62, 40), (46, 40), (30, 50), (22, 74, 1),
                      (16, 66)]),
              L(outline([(10, 66), (4, 100), (8, 122, 1), (16, 104), (20, 72)]), 'mid', 'f', ln=True),
              L(outline([(88, 66), (96, 100), (94, 122, 1), (86, 104), (82, 72)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(52, 70), (56, 56), (80, 50), (94, 36), (90, 12), (70, -6), (36, -6), (12, 10), (0, 40), (-4, 80), (2, 120, 1), (20, 110), (40, 110), (46, 88)])),
             L(outline([(0, 40), (24, 46), (36, 104), (6, 110)]), 'shade', 'b', False),
             fringe([(64, -2), (90, 14), (96, 40), (94, 70, 1), (86, 52), (80, 64, 1), (76, 44), (66, 32)])],
    'back': [L(outline([(8, 116), (-6, 124, 1), (-2, 80), (-4, 40), (8, 12), (30, -6), (60, -8), (84, 4), (98, 30), (104, 70), (110, 116, 1), (94, 112), (70, 120),
                        (50, 112), (30, 120)])),
             L(outline([(56, -4), (86, 8), (100, 40), (104, 112), (70, 116)]), 'shade', 'b', False),
             strand([(40, 10), (30, 60), (34, 110)], 'deep', 'b', 1.0)],
}

# Sus Swihn: pelo verde agua con una cresta en punta hacia arriba y una franja blanca en V desde la frente, el resto
# pegado a la cabeza, y dos trenzas finas por detrás de las orejas; marquitas en la frente
CHARS['sus-swihn'] = {
    'body': 'normal', 'pal': pal('#88d8d0', '#fce4c8', iris='#1e1414', shade='#6aa8a4', stripe='#f2ecec'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': (40, 30)},
    'front': [L(outline([(14, 74), (12, 40), (22, 14), (42, 2), (50, -16, 1), (58, 2), (78, 14), (88, 40), (86, 74), (80, 60), (20, 60)])),
              L(outline([(60, 4), (82, 16), (88, 44), (84, 66), (78, 40)]), 'shade', 'b', False),
              L(outline([(28, 10), (36, 6), (50, 34), (64, 6), (72, 10), (50, 46)]), 'stripe', 'b', False)]
             + [L(ell(14 - 2 * i, 84 + 8 * i, 3.4, 4.4), 'shade', 'f', ln=True) for i in range(4)]
             + [L(ell(86 + 2 * i, 84 + 8 * i, 3.4, 4.4), 'shade', 'f', ln=True) for i in range(4)]
             + [L(outline([(42, 52), (46, 46), (48, 54)]), 'shade', 'f', False), L(outline([(58, 52), (54, 46), (52, 54)]), 'shade', 'f', False)],
    'side': [L(outline([(54, 50), (66, 40), (72, 14), (82, -10, 1), (56, -4), (30, 2), (12, 18), (4, 42), (6, 70), (18, 86), (34, 84), (46, 70)])),
             L(outline([(70, 8), (60, 2), (30, 10), (16, 30), (24, 30), (36, 18), (60, 12), (72, 18)]), 'stripe', 'b', False),
             L(outline([(4, 40), (24, 46), (26, 72), (8, 66)]), 'shade', 'b', False)]
             + [L(ell(40 - 3 * i, 82 + 8 * i, 3.4, 4.4), 'shade', 'f', ln=True) for i in range(4)],
    'back': [L(outline([(14, 78), (12, 40), (22, 14), (42, 2), (50, -16, 1), (58, 2), (78, 14), (88, 40), (86, 78), (50, 86)])),
             L(outline([(56, 4), (82, 16), (88, 46), (84, 76), (62, 84)]), 'shade', 'b', False),
             L(outline([(30, 6), (40, 4), (50, 50), (60, 4), (70, 6), (54, 76), (46, 76)]), 'stripe', 'b', False)]
             + [L(ell(18 - 2 * i, 84 + 8 * i, 3.4, 4.4), 'shade', 'f', ln=True) for i in range(4)]
             + [L(ell(82 + 2 * i, 84 + 8 * i, 3.4, 4.4), 'shade', 'f', ln=True) for i in range(4)],
}

# Siid Sinapis (portero): pelo morado abultado como una boina que le tapa la frente hasta las gafas y cae largo por la
# espalda; gafas de montura negra y ojos grises de mirada dura
CHARS['siid-sinapis'] = {
    'body': 'normal', 'pal': pal('#b880d0', '#fce4cc', iris='#6a6a70', shade='#8a5aa8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False, 'glasses': (30, 30, 34, 255), 'glasses_rect': True},
    'front': [L(outline([(4, 120), (-8, 90), (-4, 70), (10, 70), (16, 100), (84, 100), (90, 70), (104, 70), (108, 90), (96, 120)]), 'shade'),
              L(outline([(14, 74), (10, 50), (86, 50), (90, 74), (50, 70)])),
              L(outline([(-4, 50), (-6, 26), (10, 6), (34, -6), (66, -6), (90, 6), (106, 26), (104, 50), (90, 64), (70, 58), (50, 64), (30, 58), (10, 64)]), 'mid', 'f'),
              L(outline([(60, -4), (90, 8), (104, 28), (102, 48), (86, 58), (76, 20)]), 'shade', 'f', False),
              strand([(20, 30), (40, 20)], 'deep', 'f', 1.0), strand([(60, 22), (82, 30)], 'deep', 'f', 1.0)],
    'side': [L(outline([(40, 40), (30, 70), (10, 110), (-30, 130), (-10, 96), (-4, 60), (0, 36)]), 'shade'),
             L(outline([(-6, 50), (-8, 26), (6, 4), (34, -8), (66, -8), (90, 4), (104, 24), (102, 50), (84, 58), (64, 54), (40, 60), (14, 58)]), 'mid', 'f'),
             L(outline([(-6, 30), (10, 40), (20, 56), (-4, 52)]), 'shade', 'f', False)],
    'back': [L(outline([(6, 120), (-8, 80), (-4, 50), (104, 50), (108, 80), (94, 120), (50, 126)]), 'shade'),
             L(outline([(-4, 54), (-6, 26), (10, 6), (34, -6), (66, -6), (90, 6), (106, 26), (104, 54), (50, 62)]), 'mid', 'f'),
             L(outline([(56, -4), (90, 8), (104, 28), (102, 52), (60, 58)]), 'shade', 'f', False)],
}

# Pelta Chincha: piel morena, pelo lavanda azulado en media melena acampanada que se abre en puntas a la altura de las
# orejas, y unas gafas de nadar rosas sobre los ojos
CHARS['pelta-chincha'] = {
    'body': 'normal', 'pal': pal('#9aa0e0', '#d89a60', iris='#c83a3a', shade='#7a7ab8', gog='#f2e8e8', lens='#e89aa0'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(8, 64), (-14, 72, 1), (-2, 50), (6, 20), (30, 2), (50, -2), (70, 2), (94, 20), (102, 50), (114, 72, 1), (92, 64), (86, 70), (76, 62, 1),
                         (66, 70), (56, 62, 1), (44, 70), (34, 62, 1), (24, 70), (14, 62, 1)])),
              L(outline([(60, 2), (90, 18), (102, 48), (110, 68), (86, 62), (80, 30)]), 'shade', 'b', False),
              L(outline([(12, 76), (24, 70), (46, 74), (54, 74), (76, 70), (88, 76), (82, 88), (60, 86), (50, 80), (40, 86), (18, 88)]), 'gog', 'f', ln=True),
              L(ell(30, 79, 8, 5), 'lens', 'f', ln=True), L(ell(70, 79, 8, 5), 'lens', 'f', ln=True),
              L(ell(30, 79, 2, 2), OUTC, 'f', False), L(ell(70, 79, 2, 2), OUTC, 'f', False)],
    'side': [L(outline([(60, 60), (66, 70, 1), (54, 66), (40, 74, 1), (30, 64), (16, 74, 1), (6, 62), (-14, 72, 1), (-4, 48), (4, 20), (28, 2), (60, -2), (84, 8), (98, 28),
                        (102, 52), (110, 66, 1), (84, 62)])),
             L(outline([(-4, 48), (20, 46), (30, 64), (6, 62)]), 'shade', 'b', False),
             L(outline([(74, 72), (96, 72), (98, 86), (76, 86)]), 'gog', 'f', ln=True), L(ell(88, 79, 4, 5), 'lens', 'f', ln=True)],
    'back': [L(outline([(8, 64), (-14, 72, 1), (-2, 50), (6, 20), (30, 2), (50, -2), (70, 2), (94, 20), (102, 50), (114, 72, 1), (92, 66), (82, 74, 1), (70, 66),
                        (58, 76, 1), (46, 66), (34, 76, 1), (22, 66)])),
             L(outline([(56, 2), (90, 18), (102, 48), (110, 70), (80, 66)]), 'shade', 'b', False),
             L(quad((10, 80), (50, 86), (90, 80)), 'gog', 'f', False, False, 3.0)],
}

# Lieva Snoshu: chica de pelo rubio dorado con dos moños redondos arriba, flequillo de lado y grandes tirabuzones en espiral
# a los lados y en la nuca; ojos turquesa grandes y coloretes
CHARS['lieva-snoshu'] = {
    'body': 'chica', 'pal': pal('#f2d080', '#fcecdc', iris='#3ab8b0', shade='#d8a860', blush='#f4b0a8'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(ell(18, 6, 14, 12)), L(ell(82, 6, 14, 12)),
              L(outline([(10, 80), (6, 40), (18, 12), (50, 2), (82, 12), (94, 40), (90, 80), (80, 60), (20, 60)])),
              L(outline([(60, 4), (86, 16), (94, 44), (88, 70), (78, 40)]), 'shade', 'b', False),
              L(blob(quad((0, 86), (-8, 72), (6, 64)) + [(22, 70), (24, 92), (10, 102), (-2, 98)], 6), 'shade', 'f', ln=True),
              L(blob(quad((100, 86), (108, 72), (94, 64)) + [(78, 70), (76, 92), (90, 102), (102, 98)], 6), 'shade', 'f', ln=True),
              L(ell(10, 86, 4, 4) + [ell(10, 86, 4, 4)[0]], 'deep', 'f', False, False, 1.4), L(ell(90, 86, 4, 4) + [ell(90, 86, 4, 4)[0]], 'deep', 'f', False, False, 1.4),
              fringe([(12, 68), (12, 40), (26, 18), (50, 10), (74, 18), (88, 40), (88, 64), (76, 54), (64, 42), (50, 36), (40, 44), (30, 58), (20, 70, 1)]),
              L(ell(30, 88, 4.4, 2.4), 'blush', 'f', False), L(ell(70, 88, 4.4, 2.4), 'blush', 'f', False)],
    'side': [L(ell(40, -2, 14, 12)),
             L(outline([(54, 66), (58, 52), (80, 48), (92, 34), (86, 12), (64, -2), (34, 0), (12, 14), (4, 40), (6, 66), (20, 80), (40, 78)])),
             L(blob([(10, 64), (-14, 70), (-20, 92), (2, 100), (22, 90), (24, 74)], 6), 'shade', 'f', ln=True),
             L(ell(2, 84, 5, 5) + [ell(2, 84, 5, 5)[0]], 'deep', 'f', False, False, 1.4),
             L(outline([(4, 36), (26, 42), (30, 70), (10, 66)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 16), (94, 40), (92, 60, 1), (84, 46), (76, 32)]), L(ell(86, 88, 4, 2.4), 'blush', 'f', False)],
    'back': [L(ell(18, 6, 14, 12)), L(ell(82, 6, 14, 12)),
             L(outline([(8, 90), (4, 40), (18, 12), (50, 2), (82, 12), (96, 40), (92, 90), (50, 96)])),
             L(outline([(56, 4), (86, 16), (96, 46), (92, 88), (62, 94)]), 'shade', 'b', False)]
             + [L(ell(x, 96, 9, 9), 'shade', 'f', ln=True) for x in (6, 28, 50, 72, 94)]
             + [L(ell(x, 96, 3.4, 3.4) + [ell(x, 96, 3.4, 3.4)[0]], 'deep', 'f', False, False, 1.2) for x in (6, 28, 50, 72, 94)],
}

# Russo Rosmarus: grandullón calvo con la cabeza rapada clara por arriba y una banda más oscura por detrás, un punto en la
# frente, orejas grandes y un antifaz azul oscuro sobre los ojos
CHARS['russo-rosmarus'] = {
    'body': 'corpulento', 'pal': pal('#c8d8f0', '#ecd0a8', iris='#1e1414', skin_d='#c8ac88', shade='#a898a8', mask='#2a2e5a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': False, 'big_ears': 3, 'ear_out': 4},
    'front': [L(outline([(16, 60), (14, 30), (26, 10), (50, 2), (74, 10), (86, 30), (84, 60), (50, 50)])),
              L(ell(50, 50, 3, 3), 'shade', 'f', ln=True),
              L(outline([(18, 76), (30, 66), (46, 72), (50, 80), (54, 72), (70, 66), (82, 76), (74, 90), (58, 88), (50, 84), (42, 88), (26, 90)]), 'mask', 'f', ln=True),
              L(ell(32, 80, 3, 3), WHITE, 'f', False), L(ell(68, 80, 3, 3), WHITE, 'f', False),
              L([(36, 64), (44, 70)], OUTC, 'f', False, False, 2.4), L([(64, 64), (56, 70)], OUTC, 'f', False, False, 2.4)],
    'side': [L(outline([(70, 30), (60, 46), (40, 48), (20, 58), (8, 50), (10, 24), (30, 6), (56, 2), (76, 10), (86, 24)])),
             L(outline([(8, 50), (22, 58), (40, 50), (40, 70), (18, 86), (8, 70)]), 'shade'),
             L(outline([(76, 70), (94, 66), (96, 82), (80, 84)]), 'mask', 'f', ln=True), L(ell(88, 75, 2.4, 2.4), WHITE, 'f', False)],
    'back': [L(outline([(16, 56), (14, 30), (26, 10), (50, 2), (74, 10), (86, 30), (84, 56), (50, 62)])),
             L(outline([(14, 56), (50, 62), (86, 56), (86, 80), (70, 92), (30, 92), (14, 80)]), 'shade'),
             L(quad((10, 66), (50, 72), (90, 66)), 'mask', 'f', False, False, 2.4)],
}
