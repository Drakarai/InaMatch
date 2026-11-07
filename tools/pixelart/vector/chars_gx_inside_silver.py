"""Inside Silver (gx-inside-silver): los alienígenas plateados que se hacían pasar por Storm Wolf. Los once (Gin1-Gin11) son
el mismo modelo 3D en Inazuma Eleven GO Galaxy (y en la wiki, un único uniforme para todos, portero incluido): cabeza gris
en forma de bombilla, orejas puntiagudas, ojos enormes azules almendrados y dos franjas azules que le recorren el cráneo
de la frente a la nuca. Un solo dibujo para todos, con clave de equipo."""
from chars import CHARS, L, OUTC, ell, outline, pal  # noqa: F401
from heads import quad

T = 'gx-inside-silver'
DARK = (20, 44, 80, 255)

GIN_FRONT = outline([(50, -2), (74, 4), (88, 22), (90, 46), (84, 66), (72, 86), (60, 100), (50, 106, 1), (40, 100), (28, 86), (16, 66), (10, 46), (12, 22),
                     (26, 4)])
GIN_SIDE = outline([(46, -2), (72, 4), (90, 22), (96, 46), (94, 66), (90, 84), (82, 98), (72, 106, 1), (60, 100), (46, 96), (28, 86), (10, 68), (2, 44), (12, 16)])


def _eye(cx, flip=False):
    """Ojo almendrado inclinado (la esquina de fuera más alta), con el contorno oscuro, el iris azul y un brillo."""
    s = -1 if flip else 1
    P = lambda pts: [(cx + s * (p[0] - 34), p[1]) + tuple(p[2:]) for p in pts]
    return [L(outline(P([(16, 70), (26, 64), (40, 68), (47, 80), (47, 95, 1), (34, 92), (21, 84)])), DARK, 'f', ln=True),
            L(outline(P([(20, 72), (28, 67), (39, 71), (44, 81), (44, 91), (34, 89), (24, 82)])), 'iris', 'f', False),
            L(ell(cx - s * 4, 75, 4.4, 3.2), 'eye_l', 'f', False), L(ell(cx + s * 4, 85, 1.8, 1.6), 'eye_l', 'f', False)]


def _band_front(x0):
    """Franja azul del cráneo, de la frente hacia arriba (vista de frente)."""
    s = 1 if x0 < 50 else -1
    pts = [(x0, 58), (x0 - s * 4, 40), (x0 - s * 2, 18), (x0 + s * 4, 4), (x0 + s * 10, 6), (x0 + s * 6, 18), (x0 + s * 5, 40), (x0 + s * 8, 58)]
    return L(outline(pts), 'band', 'f', ln=True)


_gin = {
    'body': 'normal', 'pal': pal('#3a7ab8', '#a8acb4', iris='#2a6ab0', skin_d='#7e6a6a', band='#3a7ab8', band_d='#24508a', eye_l='#8ac4ee',
                                 dome='#c4c8ce', brow='#d4d6da'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 98, 'hairline': False, 'ears': False, 'face_front': GIN_FRONT, 'face_side': GIN_SIDE},
    'front': [L(outline([(16, 52), (-12, 40, 1), (8, 62), (18, 76)]), 'skin', 'b', ln=True),
              L(outline([(84, 52), (112, 40, 1), (92, 62), (82, 76)]), 'skin', 'b', ln=True),
              L(outline([(14, 54), (0, 46), (12, 62)]), 'skin_d', 'b', False), L(outline([(86, 54), (100, 46), (88, 62)]), 'skin_d', 'b', False),
              L(ell(42, 22, 13, 9), 'dome', 'f', False), L(ell(64, 26, 4, 5), 'dome', 'f', False),
              _band_front(30), _band_front(70)]
             + _eye(34) + _eye(66, True)
             + [L(quad((22, 62), (30, 58), (40, 61)), 'brow', 'f', False, False, 2.4), L(quad((78, 62), (70, 58), (60, 61)), 'brow', 'f', False, False, 2.4),
                L([(46, 62), (50, 67), (54, 62)], OUTC, 'f', False, False, 1.2), L([(46, 103), (54, 103)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(4, 46), (12, 16), (30, 8), (44, 40), (56, 84), (40, 96), (24, 88), (10, 70)]), 'skin_d', 'b', False),
             L(outline([(4, 44), (12, 16), (40, 4), (40, 12), (18, 24), (12, 52)]), 'skin_d', 'f', False),
             L(outline([(10, 46), (24, 14), (52, 2), (80, 10), (92, 34), (86, 36), (76, 18), (52, 10), (28, 20), (16, 48)]), 'band', 'f', ln=True),
             L(outline([(14, 40), (26, 16), (50, 8), (52, 12), (30, 22), (18, 44)]), 'band_d', 'f', False),
             L(outline([(38, 68), (54, 62), (28, 30, 1)]), 'skin', 'f', ln=True), L(outline([(41, 64), (33, 40), (48, 62)]), 'skin_d', 'f', False),
             L(outline([(80, 64), (92, 62), (96, 74), (92, 86), (84, 82)]), DARK, 'f', ln=True), L(outline([(84, 66), (92, 65), (94, 74), (90, 82), (86, 78)]), 'iris', 'f', False),
             L(ell(89, 70, 2, 2), 'eye_l', 'f', False)],
    'back': [L(outline([(50, -2), (76, 6), (90, 26), (92, 52), (84, 76), (66, 90), (50, 94), (34, 90), (16, 76), (8, 52), (10, 26), (24, 6)]), 'skin'),
             L(outline([(56, 2), (78, 8), (90, 30), (88, 62), (72, 84), (60, 60)]), 'skin_d', 'b', False),
             L(outline([(14, 52), (-12, 40, 1), (10, 64)]), 'skin', 'f', ln=True), L(outline([(86, 52), (112, 40, 1), (90, 64)]), 'skin', 'f', ln=True),
             L(outline([(26, 4), (36, 0), (38, 30), (42, 52), (58, 52), (62, 30), (64, 0), (74, 4), (72, 34), (70, 62), (30, 62), (28, 34)]), 'band', 'f', ln=True),
             L(outline([(62, 4), (72, 6), (70, 40), (68, 60), (60, 58), (62, 30)]), 'band_d', 'f', False)],
}

for _pid in ('ezra-gin', 'silva-gin', 'argus-gin', 'micah-gin', 'maxter-gin', 'casey-gin', 'consy-gin', 'shari-gin', 'colin-gin', 'nathas-gin', 'zane-gin'):
    CHARS[f'{T}:{_pid}'] = _gin
