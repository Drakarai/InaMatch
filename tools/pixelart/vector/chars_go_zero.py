"""Equipo Zero (go-zero): sus modelos 3D de Inazuma Eleven GO como referencia (busto de frente, perfil y espalda).
Los que juegan también en Unlimited Shining (Albion, Candido, Dwight, Beamer, Dawntavius y Bailong) se dibujan aquí; los de
la Oscuridad Ancestral, en chars_go_ancient_dark."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Albion Lumina (portero): capucha verde agua que baja en pico hasta el entrecejo, con dos cuernos lilas que suben en
# diagonal y, por detrás, una capa larga con franjas lilas sobre los hombros; piel muy pálida, orejas de punta, ojos
# amarillos y marcas negras en la cara
CHARS['albion-lumina'] = {
    'body': 'delgado', 'pal': pal('#5aa890', '#f8ecd4', iris='#d8c01e', shade='#3e7a68', deep='#2a5a4c', horn='#c8a8e0', stripe='#c8a8e0'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False, 'ears': False},
    'front': [L(outline([(-4, 112), (-20, 120), (0, 96), (10, 70), (90, 70), (100, 96), (120, 120), (104, 112)]), 'mid', 'b'),
              L(outline([(-12, 116), (2, 100), (98, 100), (112, 116), (98, 108), (2, 108)]), 'stripe', 'b', False),
              L(outline([(8, 100), (6, 60), (12, 30), (30, 8), (50, -2), (70, 8), (88, 30), (94, 60), (92, 100), (82, 76), (76, 48), (50, 66, 1), (24, 48), (18, 76)])),
              L(outline([(16, 52), (8, 46, 1), (18, 72)]), 'skin', 'f', ln=True), L(outline([(84, 52), (92, 46, 1), (82, 72)]), 'skin', 'f', ln=True),
              L(outline([(56, 4), (80, 16), (92, 50), (88, 92), (80, 60)]), 'shade', 'b', False),
              L(outline([(14, 52), (20, 30), (26, 48), (22, 80)]), 'deep', 'f', False), L(outline([(86, 52), (80, 30), (74, 48), (78, 80)]), 'deep', 'f', False),
              L(outline([(20, 44), (30, 36), (50, 64, 1), (70, 36), (80, 44), (74, 26), (26, 26)]), 'mid', 'f'),
              L(outline([(34, 36), (18, 10), (2, -14, 1), (24, 4), (42, 30)]), 'horn', 'f', ln=True),
              L(outline([(66, 36), (82, 10), (98, -14, 1), (76, 4), (58, 30)]), 'horn', 'f', ln=True),
              L(quad((30, 86), (36, 96), (34, 108)), OUTC, 'f', False, False, 1.2), L(quad((70, 86), (64, 96), (66, 108)), OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(60, 60), (74, 40), (70, 14), (50, 0), (26, 4), (10, 22), (2, 60), (-10, 110), (-30, 150, 1), (6, 124), (26, 100), (40, 76)])),
             L(outline([(2, 80), (14, 90), (-8, 134), (-18, 128)]), 'stripe', 'b', False),
             L(outline([(52, 30), (60, 10), (52, -14, 1), (68, 6), (64, 36)]), 'horn', 'f', ln=True),
             L(outline([(14, 30), (34, 34), (40, 70), (18, 80)]), 'shade', 'b', False)],
    'back': [L(outline([(34, 34), (18, 8), (2, -14, 1), (24, 2), (42, 30)]), 'horn', 'b', ln=True),
             L(outline([(66, 34), (82, 8), (98, -14, 1), (76, 2), (58, 30)]), 'horn', 'b', ln=True),
             L(outline([(-24, 124), (0, 96), (8, 56), (14, 26), (32, 6), (50, -2), (68, 6), (86, 26), (92, 56), (100, 96), (124, 124)])),
             L(outline([(-22, 112), (122, 112), (124, 120), (-24, 120)]), 'stripe', 'b', False),
             L(outline([(50, 0), (70, 6), (86, 26), (92, 60), (100, 100), (60, 104), (56, 40)]), 'shade', 'b', False)],
}

# Dwight Whittaker: melena naranja salvaje de puntas en todas direcciones con un mechón amarillo que sube en curva; cara de
# hombre mayor con patillas y barba naranja que le enmarcan la cara, ojos pequeños y ceño fruncido
CHARS['dwight-whittaker'] = {
    'body': 'corpulento', 'pal': pal('#e07a1e', '#f8c890', iris='#1e1414', streak='#f0d040', shade='#b85a14'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 100, 'hairline': (56, 46)},
    'front': [L(outline([(14, 74), (-10, 74, 1), (4, 58), (-18, 44, 1), (6, 34), (-2, 10, 1), (20, 12), (18, -14, 1), (36, 2), (46, -24, 1), (56, 0), (76, -14, 1),
                         (76, 8), (100, 4, 1), (92, 26), (116, 34, 1), (98, 48), (114, 66, 1), (92, 70), (100, 86, 1), (84, 78), (84, 56), (16, 56)])),
              L(outline([(60, 2), (86, 14), (100, 44), (90, 72), (78, 40)]), 'shade', 'b', False),
              L(outline([(40, 46), (34, 20), (40, -6), (52, -36, 1), (50, -4), (48, 24), (50, 46)]), 'streak', 'b', ln=True),
              fringe([(14, 60), (18, 38), (32, 26), (50, 22), (68, 26), (82, 38), (86, 60), (76, 48), (68, 58, 1), (60, 44), (50, 54, 1), (42, 44), (32, 58, 1),
                      (24, 48)]),
              L(outline([(16, 64), (21, 64), (24, 96), (34, 110), (40, 112), (32, 116), (18, 102)]), 'mid', 'f', ln=True),
              L(outline([(84, 64), (79, 64), (76, 96), (66, 110), (60, 112), (68, 116), (82, 102)]), 'mid', 'f', ln=True),
              L(outline([(42, 110), (58, 110), (50, 122, 1)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(56, 60), (62, 48), (80, 46), (90, 30), (102, 14, 1), (82, 12), (80, -12, 1), (64, 2), (54, -28, 1), (44, 0), (20, -10, 1), (22, 14), (-6, 14, 1),
                        (8, 32), (-18, 42, 1), (4, 52), (-12, 70, 1), (8, 70), (2, 90, 1), (22, 80), (40, 76)])),
             L(outline([(70, 46), (64, 18), (72, -8), (82, -36, 1), (80, -6), (78, 20), (78, 44)]), 'streak', 'b', ln=True),
             L(outline([(2, 36), (22, 42), (24, 74), (6, 66)]), 'shade', 'b', False),
             L(outline([(54, 64), (60, 66), (66, 100), (80, 112), (88, 110), (84, 120), (66, 120), (56, 100)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(18, 90), (-2, 92, 1), (8, 72), (-16, 62, 1), (4, 50), (-12, 32, 1), (8, 28), (2, 4, 1), (22, 10), (22, -14, 1), (38, 2), (50, -22, 1),
                        (60, 0), (80, -12, 1), (78, 10), (102, 8, 1), (92, 28), (114, 36, 1), (96, 50), (110, 66, 1), (94, 72), (100, 92, 1), (82, 88), (66, 98, 1),
                        (50, 88), (34, 98, 1)])),
             L(outline([(56, 4), (84, 12), (98, 50), (90, 86), (62, 90)]), 'shade', 'b', False),
             L(outline([(54, 30), (60, 0), (52, -26, 1), (48, 0), (46, 30)]), 'streak', 'b', ln=True)],
}

# Candido Glow: pelo castaño con un tupé altísimo en forma de llama que sube recto desde la frente, con rayas, y los lados
# cortos en puntas; ceño fruncido
CHARS['candido-glow'] = {
    'body': 'normal', 'pal': pal('#8a5038', '#f6c494', iris='#1e1414', shade='#6a3828'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 68), (2, 60, 1), (14, 48), (0, 34, 1), (16, 30), (84, 30), (100, 34, 1), (86, 48), (98, 60, 1), (84, 68), (80, 52), (20, 52)])),
              L(outline([(24, 44), (20, 10), (26, -26), (40, -56), (52, -64), (62, -54), (72, -20), (78, 14), (76, 44), (50, 50)]), 'mid', 'f'),
              L(outline([(56, -56), (68, -30), (76, 10), (74, 40), (62, 42), (64, 0)]), 'shade', 'f', False),
              strand([(36, 40), (34, 0), (42, -40)], 'deep', 'f', 1.0), strand([(50, 44), (50, 0), (50, -50)], 'deep', 'f', 1.0),
              strand([(64, 40), (64, 0), (58, -40)], 'deep', 'f', 1.0)],
    'side': [L(outline([(54, 58), (62, 46), (82, 44), (88, 26), (70, 16), (40, 20), (16, 26), (-4, 30, 1), (10, 42), (-6, 56, 1), (12, 58), (4, 76, 1), (22, 72), (38, 70)])),
             L(outline([(30, 30), (18, -2), (24, -40), (48, -68), (72, -60), (84, -30), (86, 6), (80, 30), (56, 26)]), 'mid', 'f'),
             L(outline([(22, -10), (30, -40), (50, -62), (40, -30), (36, 10), (28, 24)]), 'shade', 'f', False),
             strand([(46, 24), (48, -20), (62, -56)], 'deep', 'f', 1.0)],
    'back': [L(outline([(18, 82), (4, 74, 1), (12, 60), (-2, 46, 1), (12, 40), (4, 24, 1), (20, 24), (80, 24), (96, 24, 1), (88, 40), (102, 46, 1), (88, 60), (96, 74, 1),
                        (82, 82), (50, 90)])),
             L(outline([(56, 26), (86, 30), (88, 70), (64, 86)]), 'shade', 'b', False),
             L(outline([(26, 40), (20, 6), (26, -28), (40, -56), (52, -64), (62, -54), (72, -22), (78, 10), (74, 40), (50, 46)]), 'mid', 'f'),
             L(outline([(56, -56), (68, -30), (76, 10), (72, 38), (60, 40), (62, 0)]), 'shade', 'f', False)],
}


def _cone(base, tip, w=9):
    """Moño cónico (un mechón atado y enrollado) de la base a la punta, con sus vueltas."""
    import math
    dx, dy = tip[0] - base[0], tip[1] - base[1]
    d = math.hypot(dx, dy) or 1
    nx, ny = -dy / d * w, dx / d * w
    a, b = (base[0] + nx, base[1] + ny), (base[0] - nx, base[1] - ny)
    mid = (base[0] + dx * 0.45, base[1] + dy * 0.45)
    shape = outline([a, (mid[0] + nx * 1.15, mid[1] + ny * 1.15), (tip[0], tip[1], 1), (mid[0] - nx * 1.15, mid[1] - ny * 1.15), b])
    rings = [L([(base[0] + dx * t + nx * 0.9, base[1] + dy * t + ny * 0.9), (base[0] + dx * (t + 0.08) - nx * 0.9, base[1] + dy * (t + 0.08) - ny * 0.9)],
               'deep', 'b', False, False, 1.0) for t in (0.3, 0.55)]
    return [L(shape, 'mid', 'b', ln=True)] + rings


# Beamer Daye: chica de pelo corto rojo coral con cinco moños en forma de cono que salen hacia fuera (uno arriba y dos a
# cada lado); ojos verde agua y sonrisa pícara de dientes
CHARS['beamer-daye'] = {
    'body': 'chica', 'pal': pal('#e0604a', '#fcdcc0', iris='#2ab0a0', shade='#b8443a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': _cone((50, 10), (50, -40)) + _cone((24, 20), (-6, -12)) + _cone((76, 20), (106, -12)) + _cone((14, 52), (-26, 44)) + _cone((86, 52), (126, 44))
             + [L(outline([(14, 76), (8, 46), (16, 20), (50, 6), (84, 20), (92, 46), (86, 76), (80, 60), (20, 60)])),
                L(outline([(60, 8), (84, 20), (92, 50), (86, 70), (78, 44)]), 'shade', 'b', False),
                fringe([(12, 62), (14, 40), (28, 22), (50, 16), (72, 22), (86, 40), (88, 62), (80, 54), (72, 62, 1), (66, 48), (58, 58, 1), (52, 46), (44, 58, 1),
                        (38, 46), (30, 60, 1), (22, 50)])],
    'side': _cone((40, 6), (40, -44)) + _cone((24, 20), (-4, -20)) + _cone((16, 50), (-24, 50))
            + [L(outline([(54, 60), (60, 48), (82, 48), (92, 34), (86, 12), (64, 2), (38, 2), (16, 14), (6, 40), (8, 66), (22, 80), (36, 78), (46, 68)])),
               L(outline([(6, 40), (24, 44), (26, 72), (10, 66)]), 'shade', 'b', False),
               fringe([(66, 4), (90, 18), (94, 40), (90, 54, 1), (82, 42), (74, 30)])],
    'back': _cone((50, 10), (50, -40)) + _cone((24, 20), (-6, -12)) + _cone((76, 20), (106, -12)) + _cone((14, 52), (-26, 44)) + _cone((86, 52), (126, 44))
            + [L(outline([(14, 76), (8, 46), (16, 20), (50, 6), (84, 20), (92, 46), (86, 76), (66, 86), (34, 86)])),
               L(outline([(56, 8), (84, 20), (92, 50), (86, 74), (62, 84)]), 'shade', 'b', False)],
}

# Bailong: pelo blanco de pinchos hacia arriba y a los lados, con dos mechones gris lila que se abren como alas a la altura
# de las orejas y una coleta baja atada con un lazo blanco en la nuca; ojos rojizos afilados
CHARS['bailong'] = {
    'body': 'normal', 'pal': pal('#f4f0ee', '#fcdcc0', iris='#9a3a2a', shade='#d0c0c8', deep='#a898a8', wing='#c8b4c8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(14, 70), (-14, 76, 1), (2, 62), (-10, 56, 1), (8, 52), (18, 60)]), 'wing', 'b', ln=True),
              L(outline([(86, 70), (114, 76, 1), (98, 62), (110, 56, 1), (92, 52), (82, 60)]), 'wing', 'b', ln=True),
              L(outline([(16, 64), (2, 52, 1), (12, 42), (-2, 28, 1), (14, 22), (10, 2, 1), (26, 10), (30, -14, 1), (42, 2), (50, -26, 1), (58, 0), (72, -12, 1), (74, 10),
                         (92, 4, 1), (88, 22), (102, 28, 1), (88, 42), (98, 52, 1), (84, 64), (80, 52), (20, 52)])),
              L(outline([(60, 0), (84, 12), (92, 40), (86, 58), (76, 38)]), 'shade', 'b', False),
              fringe([(14, 60), (16, 38), (30, 24), (50, 18), (70, 24), (84, 38), (86, 60), (78, 50), (72, 60, 1), (64, 46), (56, 58, 1), (50, 44), (44, 64, 1),
                      (38, 46), (30, 58, 1), (22, 50)]),
              strand([(36, 30), (40, 46)], 'deep', 'f', 1.0), strand([(62, 30), (60, 46)], 'deep', 'f', 1.0)],
    'side': [L(outline([(30, 76), (14, 86), (-6, 104, 1), (8, 100), (-2, 116, 1), (20, 100), (34, 86)]), 'wing', 'b', ln=True),
             L(outline([(54, 58), (62, 46), (82, 46), (90, 30), (98, 12, 1), (78, 12), (76, -12, 1), (62, 2), (50, -24, 1), (40, 2), (14, -6, 1), (18, 14), (-8, 18, 1),
                        (8, 32), (-14, 44, 1), (8, 50), (2, 66, 1), (20, 64), (36, 66)])),
             L(outline([(30, 54), (10, 50), (-16, 62, 1), (8, 60), (-6, 72, 1), (16, 68), (34, 64)]), 'wing', 'f', ln=True),
             L(outline([(4, 32), (22, 38), (24, 62), (8, 54)]), 'shade', 'b', False),
             L(ell(30, 78, 5, 4), WHITE, 'f', ln=True),
             fringe([(66, 4), (90, 18), (94, 40), (90, 54, 1), (82, 40), (74, 30)])],
    'back': [L(outline([(10, 64), (-14, 70, 1), (0, 56), (-12, 48, 1), (8, 46), (92, 46), (112, 48, 1), (100, 56), (114, 70, 1), (90, 64), (70, 72), (50, 66), (30, 72)]),
               'wing', 'b', ln=True),
             L(outline([(16, 70), (2, 54, 1), (12, 44), (-2, 30, 1), (14, 22), (10, 2, 1), (26, 10), (30, -14, 1), (42, 2), (50, -26, 1), (58, 0), (72, -12, 1), (74, 10),
                        (92, 4, 1), (88, 22), (102, 30, 1), (88, 44), (98, 54, 1), (84, 70), (50, 80)])),
             L(outline([(56, 2), (84, 12), (92, 44), (84, 66), (62, 76)]), 'shade', 'b', False),
             L(outline([(44, 76), (56, 76), (58, 110, 1), (50, 100), (42, 110, 1)]), 'mid', 'f', ln=True),
             L(outline([(40, 78), (50, 72), (60, 78), (56, 86), (44, 86)]), WHITE, 'f', ln=True)],
}

# Glaucous Gull: grandullón de piel morena y cara redonda, con una melena morada oscura enorme de rizos en bultos que le cae
# hasta los hombros abriéndose a los lados y una corona de pinchos encima; ojillos de ceño fruncido y bigote fino
CHARS['glaucous-gull'] = {
    'body': 'corpulento', 'pal': pal('#4a3e6e', '#a86a40', iris='#2a2a3a', shade='#342a52'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': (58, 40)},
    'front': [L(outline([(14, 70), (-10, 76), (-26, 92), (-34, 110, 1), (-12, 108), (0, 118), (14, 110), (20, 96), (14, 78)])),
              L(outline([(86, 70), (110, 76), (126, 92), (134, 110, 1), (112, 108), (100, 118), (86, 110), (80, 96), (86, 78)])),
              L(outline([(14, 74), (-6, 66), (-10, 46), (4, 30), (10, 8), (22, 4), (24, -14, 1), (36, -2), (44, -22, 1), (54, -4), (66, -18, 1), (70, 2), (82, -8, 1), (84, 10),
                         (96, 22), (110, 46), (106, 66), (86, 74), (82, 52), (18, 52)])),
              L(outline([(60, 0), (90, 18), (106, 50), (100, 68), (80, 40)]), 'shade', 'b', False),
              strand([(-6, 56), (8, 60), (14, 74)], 'shade', 'b', 1.2), strand([(106, 56), (92, 60), (86, 74)], 'shade', 'b', 1.2),
              L(quad((38, 100), (50, 92), (62, 100)), OUTC, 'f', False, False, 1.8), L(quad((36, 112), (50, 118), (64, 112)), OUTC, 'f', False, False, 1.4)],
    'side': [L(outline([(54, 50), (66, 36), (64, 16), (82, -2, 1), (56, 4), (52, -18, 1), (38, 2), (20, 4), (6, 18), (-16, 28), (-34, 46), (-46, 70), (-44, 96),
                        (-26, 112), (-4, 108), (16, 112), (26, 96), (40, 72)])),
             L(outline([(-20, 50), (2, 54), (14, 96), (-14, 102)]), 'shade', 'b', False),
             strand([(-30, 70), (-10, 74)], 'shade', 'b', 1.2), strand([(-22, 94), (0, 92)], 'shade', 'b', 1.2)],
    'back': [L(outline([(10, 8), (22, 4), (24, -14, 1), (36, -2), (44, -22, 1), (54, -4), (66, -18, 1), (70, 2), (82, -8, 1), (84, 10), (96, 22), (112, 44), (128, 66),
                        (134, 96), (120, 110), (100, 104), (84, 116), (64, 104), (50, 116), (36, 104), (16, 116), (0, 104), (-20, 110), (-34, 96), (-28, 66), (-12, 44),
                        (4, 22)])),
             L(outline([(56, 2), (96, 24), (128, 70), (130, 100), (90, 104), (70, 40)]), 'shade', 'b', False),
             strand([(-10, 70), (10, 74), (28, 66)], 'shade', 'b', 1.2), strand([(72, 66), (90, 74), (110, 70)], 'shade', 'b', 1.2)],
}

# Dawntavius Spectrum: melena lisa roja hasta los hombros, con raya al lado y un mechón que le tapa un ojo; las puntas se
# abren hacia fuera; sonrisa tranquila
CHARS['dawntavius-spectrum'] = {
    'body': 'normal', 'pal': pal('#c81e14', '#fcdcc0', iris='#9a3a2a', shade='#981410', light='#e85a4a'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 116), (-8, 124, 1), (2, 104), (2, 60), (8, 24), (28, 4), (50, -2), (72, 4), (92, 24), (98, 60), (98, 104), (108, 124, 1), (88, 116),
                         (84, 70), (16, 70)])),
              L(outline([(60, 2), (88, 16), (98, 50), (98, 110), (86, 100), (84, 50)]), 'shade', 'b', False),
              fringe([(8, 100), (6, 50), (18, 20), (42, 8), (66, 10), (86, 26), (94, 56), (90, 80), (84, 62), (72, 52), (66, 48), (58, 54), (52, 74), (44, 100),
                      (34, 112, 1), (32, 92), (24, 108, 1), (18, 92), (12, 112, 1)]),
              L(outline([(30, 14), (52, 8), (40, 24)]), 'light', 'f', False), L(ell(66, 12, 6, 3), 'light', 'f', False)],
    'side': [L(outline([(54, 70), (58, 56), (80, 50), (92, 36), (88, 14), (66, 0), (36, 0), (14, 14), (4, 40), (0, 80), (-4, 112), (-16, 124, 1), (8, 116), (20, 124, 1),
                        (32, 110), (46, 122, 1), (48, 96)])),
             L(outline([(4, 40), (28, 44), (36, 100), (6, 106)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 42), (94, 64, 1), (86, 50), (78, 38)])],
    'back': [L(outline([(2, 112), (-8, 122, 1), (2, 104), (0, 60), (8, 24), (28, 4), (50, -2), (72, 4), (92, 24), (100, 60), (98, 104), (108, 122, 1), (96, 114),
                        (80, 120, 1), (66, 110), (50, 120, 1), (34, 110), (20, 120, 1)])),
             L(outline([(56, 2), (88, 16), (100, 50), (98, 112), (66, 112), (66, 50)]), 'shade', 'b', False),
             L(ell(50, 10, 10, 4), 'light', 'b', False)],
}

# Ashley Silverwood: pelo castaño en casco liso con flequillo de mechones peinado de lado; ojos entornados grises y un cuello
# alto de bufanda morada
CHARS['ashley-silverwood'] = {
    'body': 'normal', 'pal': pal('#9a5a1e', '#fcdcc0', iris='#5a5a5a', shade='#7a4414', scarf='#4a3a6a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 86), (6, 50), (12, 20), (30, 4), (50, 0), (70, 4), (88, 20), (94, 50), (86, 86), (80, 64), (20, 64)])),
              L(outline([(60, 4), (86, 18), (94, 50), (88, 80), (80, 50)]), 'shade', 'b', False),
              fringe([(10, 76), (10, 44), (22, 20), (44, 10), (70, 14), (88, 34), (90, 66), (84, 54), (78, 44), (72, 56, 1), (64, 40), (54, 56, 1), (50, 40),
                      (40, 58, 1), (34, 42), (24, 60, 1), (18, 54), (16, 76)]),
              L(outline([(24, 112), (50, 118), (76, 112), (80, 124), (50, 130), (20, 124)]), 'scarf', 'f', ln=True)],
    'side': [L(outline([(52, 70), (56, 56), (78, 50), (92, 36), (88, 14), (68, 0), (40, -2), (16, 10), (4, 36), (4, 70), (12, 90), (30, 96), (44, 86)])),
             L(outline([(4, 40), (26, 42), (32, 88), (10, 86)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 42), (92, 58, 1), (84, 46), (76, 34)]),
             L(outline([(46, 100), (78, 106), (80, 122), (44, 120)]), 'scarf', 'f', ln=True)],
    'back': [L(outline([(12, 84), (6, 50), (12, 20), (30, 4), (50, 0), (70, 4), (88, 20), (94, 50), (88, 84), (64, 92), (50, 104, 1), (36, 92)])),
             L(outline([(56, 4), (86, 18), (94, 50), (88, 84), (60, 92)]), 'shade', 'b', False),
             L(outline([(24, 104), (50, 108), (76, 104), (80, 120), (50, 124), (20, 120)]), 'scarf', 'f', ln=True)],
}

# Pinkus Mountbatten: hombre hecho y derecho, con el pelo castaño oscuro en un tupé plano echado hacia delante y de puntas a
# la derecha, los lados cortos y unas patillas que bajan hasta un bigotazo; ceño duro
CHARS['pinkus-mountbatten'] = {
    'body': 'delgado', 'pal': pal('#3e2e26', '#f8d4b0', iris='#1e1414', shade='#2a1e18'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 112, 'hairline': (40, 30)},
    'front': [L(outline([(16, 74), (14, 40), (20, 30), (80, 30), (86, 40), (84, 74), (78, 60), (22, 60)])),
              L(outline([(14, 34), (2, 22), (-12, 6, 1), (8, 6), (10, -4), (40, -8), (70, -6), (90, -2), (110, -10, 1), (100, 6), (114, 8, 1), (94, 16), (88, 34),
                         (50, 30)]), 'mid', 'f'),
              L(outline([(58, -10), (90, -4), (90, 14), (70, 22)]), 'shade', 'f', False),
              L(outline([(16, 72), (22, 72), (26, 100), (20, 104), (16, 96)]), 'mid', 'f', ln=True),
              L(outline([(84, 72), (78, 72), (74, 100), (80, 104), (84, 96)]), 'mid', 'f', ln=True),
              L(outline([(22, 108), (34, 98), (50, 98), (66, 98), (78, 108), (74, 112), (62, 106), (50, 106), (38, 106), (26, 112)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(56, 70), (60, 40), (40, 30), (14, 40), (8, 70), (18, 90), (34, 92), (48, 84)])),
             L(outline([(14, 40), (8, 20), (0, 8), (24, 0), (50, -6), (80, -6), (100, -2), (112, -16, 1), (104, 6), (94, 18), (70, 18), (40, 28)]), 'mid', 'f'),
             L(outline([(50, 70), (58, 72), (64, 100), (76, 110), (92, 104), (98, 108), (84, 118), (64, 114), (54, 96)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(14, 84), (14, 40), (20, 26), (80, 26), (86, 40), (86, 84), (50, 90)])),
             L(outline([(56, 26), (84, 30), (86, 80), (64, 88)]), 'shade', 'b', False),
             L(outline([(12, 34), (6, 10), (24, -6), (50, -10), (76, -6), (96, -2), (112, -14, 1), (106, 2), (120, 6, 1), (98, 14), (90, 34), (50, 30)]), 'mid', 'f')],
}

# Flint Charcoal: hombre de pelo largo liso gris verdoso hasta los hombros, con el flequillo de puntas echado a la derecha;
# sonrisa ancha de dientes y mirada de pillo
CHARS['flint-charcoal'] = {
    'body': 'delgado', 'pal': pal('#6a6a5a', '#fcdcc0', iris='#2a1e1a', shade='#4e4e42'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(10, 120), (4, 70), (8, 30), (24, 8), (50, -2), (76, 8), (92, 30), (96, 70), (92, 120), (82, 120), (80, 70), (20, 70), (20, 120)])),
              L(outline([(60, 2), (86, 16), (96, 50), (92, 116), (84, 100), (80, 50)]), 'shade', 'b', False),
              fringe([(10, 80), (8, 44), (20, 18), (44, 6), (70, 8), (86, 18), (98, 26, 1), (92, 34), (110, 44, 1), (90, 48), (86, 54), (70, 46), (56, 52), (40, 46),
                      (24, 56), (18, 76)])],
    'side': [L(outline([(52, 60), (58, 48), (82, 44), (94, 30), (100, 10, 1), (84, 8), (66, -6), (40, -4), (16, 10), (6, 40), (4, 80), (2, 120), (30, 118), (40, 84)])),
             L(outline([(8, 50), (28, 50), (34, 110), (8, 112)]), 'shade', 'b', False),
             ],
    'back': [L(outline([(4, 120), (4, 70), (8, 30), (24, 8), (50, -2), (76, 8), (92, 30), (98, 70), (98, 120), (50, 124)])),
             L(outline([(56, 4), (88, 18), (98, 60), (96, 118), (66, 120)]), 'shade', 'b', False),
             L(outline([(16, 16), (-6, 10, 1), (8, 30)]), 'mid', 'b', ln=True),
             L(ell(66, 40, 6, 8), 'deep', 'b', False)],
}

# Gus Martin en GO: ya mayor, con media melena castaña lisa hasta los hombros y un tupé que se enrosca en un rizo sobre la
# frente; gafas redondas de cristal rosado, nariz larga y puntiaguda y una sonrisa torcida
CHARS['go:gus-martin'] = {
    'body': 'delgado', 'pal': pal('#5a3820', '#fcdcc0', iris='#2a1e1a', shade='#402614', lens='#f4dce4'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 104, 'hairline': (60, 40)},
    'front': [L(outline([(10, 120), (4, 70), (8, 30), (24, 6), (50, -2), (76, 6), (92, 30), (96, 70), (92, 120), (82, 120), (80, 70), (20, 70), (20, 120)])),
              L(outline([(60, 2), (86, 16), (96, 50), (92, 116), (84, 100), (80, 50)]), 'shade', 'b', False),
              L(outline([(40, 40), (36, 18), (50, 4), (72, 8), (84, 26), (82, 50), (76, 60), (68, 52), (70, 36), (60, 26), (50, 30), (52, 42)]), 'mid', 'f', ln=True),
              L(outline([(52, 14), (72, 16), (76, 36), (68, 30)]), 'shade', 'f', False),
              L(ell(36, 76, 9, 7), 'lens', 'f', ln=True), L(ell(64, 76, 9, 7), 'lens', 'f', ln=True), L([(45, 75), (55, 75)], OUTC, 'f', False, False, 1.4),
              L(ell(36, 77, 2, 2), OUTC, 'f', False), L(ell(64, 77, 2, 2), OUTC, 'f', False),
              L(outline([(47, 80), (53, 80), (56, 98, 1), (44, 98, 1)]), 'skin', 'f', ln=True)],
    'side': [L(outline([(54, 56), (58, 44), (76, 40), (90, 26), (82, 4), (60, -6), (34, -4), (14, 10), (4, 40), (2, 80), (4, 120), (34, 118), (40, 84), (46, 66)])),
             L(outline([(4, 46), (26, 48), (32, 110), (6, 112)]), 'shade', 'b', False),
             L(outline([(70, 40), (76, 16), (90, 6), (100, 18), (94, 34), (86, 26), (82, 40)]), 'mid', 'f', ln=True),
             L(ell(86, 74, 5, 6), 'lens', 'f', ln=True), L([(80, 72), (54, 68)], OUTC, 'f', False, False, 1.2),
             L(outline([(88, 80), (112, 100, 1), (90, 96)]), 'skin', 'f', ln=True)],
    'back': [L(outline([(4, 120), (4, 70), (8, 30), (24, 6), (50, -2), (76, 6), (92, 30), (98, 70), (98, 120), (50, 124)])),
             L(outline([(56, 4), (88, 18), (98, 60), (96, 118), (66, 120)]), 'shade', 'b', False)],
}
