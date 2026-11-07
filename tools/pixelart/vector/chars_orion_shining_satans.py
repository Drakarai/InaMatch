"""Demonios Brillantes (orion-shining-satans): Australia de Orion (シャイニングサタンズ), con sus modelos 3D de Inazuma Eleven
Orion no Kokuin (オリオンの刻印) en la enciclopedia. Todos van como 'orion-shining-satans:<id>': 'aster-roth' cogía por prefijo
el dibujo de 'aster' (otro personaje).

Satan Gaul (beryl) tiene tres caras: el modelo 3D es la primera (cuello a la izquierda: pinchos naranjas y mechones salmón).
La plantilla lo trae dos veces; la segunda ficha (beryl-ok-satan-mc) lleva su tercera cara del anime (cuello recto: pelo rojo
aún más erizado, ojos redondos enormes y la boca abierta), para que no sean iguales. Diabo Los (grant-grimoire) y Simon
Azazel (baz-azel) son el entrenador y su ayudante: su modelo va de traje, pero aquí juegan con la equipación."""
import math

from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars_ares_barcelona_orb import curls
from heads import quad  # noqa: F401

T = 'orion-shining-satans:'
WHITE = (248, 248, 248, 255)
PUPIL = (24, 18, 22, 255)


def mirror_x(pts):
    return [(100 - p[0], p[1]) + tuple(p[2:]) for p in pts][::-1]


def sharp_eye(cx, s, ey, iris):
    """El ojo 'sharp' de heads.py como capa de delante (para pintarlo encima de pinturas de guerra)."""
    eye = [(cx - 8 * s, ey - 4), (cx + 7 * s, ey - 1.5), (cx + 5.5 * s, ey + 5), (cx - 6 * s, ey + 3.5)]
    return [L(eye, WHITE, 'f', False), L(ell(cx + s, ey + 1, 3.6, 4.4), iris, 'f', False), L(ell(cx + s * 2, ey - 0.8, 1.2, 1.2), WHITE, 'f', False),
            L([eye[0], eye[1]], OUTC, 'f', False, False, 3.0)]


def sharp_eye_side(ey, iris):
    eye = [(74, ey - 3.5), (85, ey - 2), (84.5, ey + 5.5), (75, ey + 4.5)]
    return [L(eye, WHITE, 'f', False), L(ell(82.2, ey + 1.7, 3.2, 4.2), iris, 'f', False), L([eye[0], eye[1]], OUTC, 'f', False, False, 3.0)]


def radial(cx, cy, r_out, r_in, a0, a1, n, jit=0.0, seed=1):
    """Corona de pinchos alrededor de (cx, cy) entre los ángulos a0 y a1 (grados, 0 = derecha, 90 = arriba)."""
    import random
    rnd = random.Random(seed)
    pts = []
    for i in range(2 * n + 1):
        a = math.radians(a0 + (a1 - a0) * i / (2 * n))
        k = 1 + rnd.uniform(-jit, jit)
        if i % 2:
            pts.append((cx + r_out[0] * k * math.cos(a), cy - r_out[1] * k * math.sin(a), 1))
        else:
            pts.append((cx + r_in[0] * math.cos(a), cy - r_in[1] * math.sin(a)))
    return pts


# Pazuzu Zaham (Pazuza Ross, portero): moreno, pelo gris beige revuelto con dos mechones de punta arriba como orejas de
# lobo, flequillo hasta los ojos, dos mechones con rayas oscuras a los lados de la cara y coleta baja con una anilla dorada;
# una franja oscura le cruza los ojos
BAND = (70, 60, 60, 255)
STRIPE = (110, 80, 60, 255)
GOLD = (214, 172, 70, 255)
PZ_IRIS = (120, 50, 40, 255)


def _dread(x0, x1, y0, y1):
    out = [L(outline([(x0, y0), (x1, y0), (x1, y1), ((x0 + x1) / 2, y1 + 4, 1), (x0, y1)]), 'mid', 'f', ln=True)]
    for y in range(int(y0) + 10, int(y1), 8):
        out.append(L([(x0 + 0.5, y), (x1 - 0.5, y)], STRIPE, 'f', False, False, 2.2))
    return out


CHARS[T + 'pazuza-ross'] = {
    'body': 'delgado', 'pal': pal('#bcb4a6', '#8a5a3a', iris='#784032', shade='#988f82', deep='#766e62'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 78), (2, 60), (-8, 52, 1), (4, 44), (4, 26), (12, 10), (20, -18, 1), (34, 4), (50, 0), (64, 4), (78, -18, 1), (86, 10), (94, 26), (96, 44),
                         (108, 52, 1), (98, 60), (90, 78), (84, 60), (16, 60)])),
              L(outline([(60, 2), (78, -18), (86, 10), (94, 26), (96, 44), (108, 52), (98, 60), (90, 74), (82, 40)]), 'shade', 'b', False),
              L(blob([(16, 70), (50, 68), (84, 70), (84, 80), (50, 80), (16, 80)]), BAND, 'f', False)]
             + sharp_eye(36, 1, 75, PZ_IRIS) + sharp_eye(64, -1, 75, PZ_IRIS)
             + [L(outline([(12, 64), (12, 40), (24, 24), (50, 18), (76, 24), (88, 40), (88, 64), (80, 54), (74, 70, 1), (68, 52), (58, 60), (54, 46), (48, 66, 1), (44, 48),
                           (34, 56), (28, 46), (22, 68, 1), (18, 54)]), 'mid', 'f'),
                L(outline([(58, 20), (76, 24), (88, 40), (88, 62), (80, 54), (74, 68), (68, 50)]), 'shade', 'f', False)]
             + _dread(14, 22, 56, 100) + _dread(78, 86, 56, 100),
    'side': [L(outline([(80, 64), (88, 50), (92, 30), (84, 10), (70, -2), (60, -20, 1), (48, -2), (30, -2), (14, 8), (2, 30), (-6, 50, 1), (4, 56), (2, 74), (14, 86), (30, 84),
                        (40, 72), (44, 58), (56, 54), (70, 56)])),
             L(outline([(4, 30), (30, 34), (44, 58), (30, 84), (14, 84), (4, 60)]), 'shade', 'b', False),
             L(outline([(30, 80), (38, 84), (24, 112), (16, 116, 1), (20, 100)]), 'mid', 'b', ln=True),
             L([(28, 84), (36, 88)], GOLD, 'b', False, False, 3.0),
             L(blob([(70, 70), (88, 70), (88, 80), (70, 80)]), BAND, 'f', False)]
            + sharp_eye_side(75, PZ_IRIS)
            + [L(outline([(70, 6), (88, 18), (94, 40), (90, 62, 1), (84, 46), (76, 30)]), 'mid', 'f')]
            + _dread(62, 70, 56, 100),
    'back': [L(outline([(12, 84), (-6, 70, 1), (6, 62), (-4, 44, 1), (8, 36), (8, 20), (20, -18, 1), (36, 6), (50, 2), (64, 6), (80, -18, 1), (92, 20), (92, 36), (104, 44, 1),
                        (94, 62), (106, 70, 1), (88, 84), (70, 80), (60, 90, 1), (50, 80), (40, 90, 1), (30, 80)])),
             L(outline([(58, 4), (80, -18), (92, 20), (92, 36), (104, 44), (94, 62), (106, 70), (88, 82), (66, 80), (66, 30)]), 'shade', 'b', False),
             L(outline([(44, 80), (56, 80), (58, 112), (50, 118, 1), (42, 112)]), 'mid', 'f', ln=True), L([(44, 84), (56, 84)], GOLD, 'f', False, False, 3.2)]
            + _dread(12, 20, 60, 100) + _dread(80, 88, 60, 100),
}

# Agalia Rept (Carlam Buer): grandullón moreno de cara enorme y marcada; pelo negro peinado hacia atrás que se abre en
# punta por abajo, con dos cuernos dorado oliva en las sienes y un mechón del mismo color que le cruza la cara; ojos
# amarillos, cicatrices y boca torcida
HORN = (170, 160, 80, 255)
HORN_D = (128, 118, 56, 255)
SCAR = (150, 96, 60, 255)
CHARS[T + 'carlam-buer'] = {
    'body': 'corpulento', 'pal': pal('#1e1a1e', '#c08a5a', iris='#f0d020', shade='#141114', deep='#0c0a0c'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 101, 'eye_y': 76,
             'hairline': [(14, 60), (20, 46), (34, 36), (50, 32), (66, 36), (80, 46), (86, 60)],
             'face_front': blob([(16, 52), (50, 42), (84, 52), (90, 78), (84, 102), (66, 112), (50, 114), (34, 112), (16, 102), (10, 78)])},
    'front': [L(outline([(14, 70), (4, 86), (-10, 100, 1), (10, 98), (20, 86)])), L(outline(mirror_x([(14, 70), (4, 86), (-10, 100, 1), (10, 98), (20, 86)]))),
              L(outline([(14, 72), (10, 40), (20, 14), (36, 2), (50, 0), (64, 2), (80, 14), (90, 40), (86, 72), (80, 50), (20, 50)])),
              strand([(50, 2), (50, 30)], 'deep', 'b', 1.0), strand([(32, 8), (26, 40)], 'deep', 'b', 1.0), strand([(68, 8), (74, 40)], 'deep', 'b', 1.0),
              L(outline([(20, 46), (6, 38), (-4, 20), (0, 2, 1), (6, 22), (16, 32), (26, 38)]), HORN, 'f', ln=True),
              L(outline(mirror_x([(20, 46), (6, 38), (-4, 20), (0, 2, 1), (6, 22), (16, 32), (26, 38)])), HORN, 'f', ln=True),
              L(outline([(48, 22), (60, 26), (46, 58), (34, 86, 1), (38, 58)]), HORN, 'f', ln=True),
              L(outline([(54, 26), (60, 26), (46, 58), (40, 72)]), HORN_D, 'f', False),
              L([(70, 82), (76, 92)], SCAR, 'f', False, False, 1.2), L([(66, 84), (70, 94)], SCAR, 'f', False, False, 1.2),
              L(quad((44, 80), (40, 90), (46, 92)), OUTC, 'f', False, False, 1.2), L(quad((56, 80), (60, 90), (54, 92)), OUTC, 'f', False, False, 1.2),
              L(quad((40, 104), (50, 106), (60, 104)), (150, 96, 60, 255), 'f', False, False, 1.0)],
    'side': [L(outline([(74, 30), (76, 20), (64, 4), (44, 0), (24, 6), (10, 22), (4, 44), (4, 72), (-12, 90, 1), (10, 88), (24, 84), (36, 72), (42, 60), (56, 44), (68, 36)])),
             strand([(60, 6), (30, 30)], 'deep', 'b', 1.0),
             L(outline([(40, 22), (60, 20), (84, 28), (100, 46, 1), (84, 36), (60, 30), (42, 30)]), HORN, 'f', ln=True),
             L(outline([(72, 34), (84, 40), (80, 60, 1), (76, 44)]), HORN, 'f', ln=True),
             L([(78, 86), (82, 94)], SCAR, 'f', False, False, 1.2)],
    'back': [L(outline([(14, 42), (4, 30), (0, 10), (4, 0, 1), (10, 18), (22, 32)]), HORN), L(outline(mirror_x([(14, 42), (4, 30), (0, 10), (4, 0, 1), (10, 18), (22, 32)])), HORN),
             L(outline([(-10, 98, 1), (8, 82), (12, 50), (16, 24), (30, 8), (50, 2), (70, 8), (84, 24), (88, 50), (92, 82), (110, 98, 1), (80, 94), (50, 98), (20, 94)])),
             strand([(50, 4), (50, 90)], 'deep', 'b', 1.0)],
}

# Demogorgon Anno (Damon Gorgon): grandullón moreno de cara redonda; pelo turquesa estirado con un moño en palmera arriba y
# dos moños de pompón a los lados, atados con gomas naranjas; ojillos redondos, nariz gorda marrón, dos dientes de conejo
# y rayitas amarillas en las mejillas
TIE = (226, 96, 40, 255)
NOSE = (110, 74, 62, 255)
MARK = (232, 196, 60, 255)
CHARS[T + 'damon-gorgon'] = {
    'body': 'corpulento', 'pal': pal('#2aa09a', '#a87850', iris='#2a2222', shade='#1e7e7a', deep='#145c58'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'none', 'eye_y': 76, 'hairline': [(16, 56), (22, 44), (50, 40), (78, 44), (84, 56)],
             'face_front': blob([(16, 52), (50, 42), (84, 52), (92, 78), (86, 102), (66, 112), (50, 114), (34, 112), (14, 102), (8, 78)])},
    'front': [L(outline([(30, -12), (34, -28, 1), (42, -20), (50, -32, 1), (58, -20), (66, -28, 1), (70, -12), (60, -4), (40, -4)])),
              L(outline([(30, -12), (70, -12), (60, -4), (40, -4)]), 'shade', 'b', False),
              L(outline([(44, 8), (45, -5), (55, -5), (56, 8)])),
              L(outline([(16, 58), (14, 34), (24, 14), (50, 6), (76, 14), (86, 34), (84, 58), (80, 46), (20, 46)])),
              L(outline([(60, 8), (76, 14), (86, 34), (84, 54), (76, 34)]), 'shade', 'b', False),
              strand([(50, 8), (50, 40)], 'deep', 'b', 1.0), strand([(34, 12), (28, 42)], 'deep', 'b', 1.0), strand([(66, 12), (72, 42)], 'deep', 'b', 1.0),
              L([(44, -4), (56, -4)], TIE, 'f', False, False, 2.6),
              L(curls(8, 68, (13, 15), 5, 0.2), 'mid', 'f'), L(curls(92, 68, (13, 15), 5, 0.5), 'mid', 'f'),
              L([(18, 60), (20, 66)], TIE, 'f', False, False, 2.6), L([(82, 60), (80, 66)], TIE, 'f', False, False, 2.6),
              L(ell(50, 86, 6.4, 5.4), NOSE, 'f', ln=True),
              L(quad((32, 95), (50, 99), (68, 94)), OUTC, 'f', False, False, 1.4),
              L([(45.5, 97.5), (54.5, 97.5), (54.5, 104), (45.5, 104)], WHITE, 'f', False), L([(45.5, 98), (45.5, 104), (54.5, 104), (54.5, 98)], OUTC, 'f', False, False, 1.0),
              L([(50, 98), (50, 104)], OUTC, 'f', False, False, 0.8),
              L([(24, 84), (28, 88)], MARK, 'f', False, False, 1.4), L([(28, 82), (31, 86)], MARK, 'f', False, False, 1.4),
              L([(76, 84), (72, 88)], MARK, 'f', False, False, 1.4), L([(72, 82), (69, 86)], MARK, 'f', False, False, 1.4)],
    'side': [L(outline([(20, -12), (24, -28, 1), (32, -20), (40, -32, 1), (48, -20), (56, -28, 1), (60, -12), (50, -4), (30, -4)])),
             L(outline([(34, 8), (35, -5), (45, -5), (46, 8)])),
             L(outline([(76, 44), (80, 30), (68, 12), (44, 4), (22, 10), (8, 28), (6, 52), (14, 64), (32, 64), (42, 56), (56, 48), (68, 46)])),
             L(outline([(8, 30), (30, 34), (42, 56), (14, 62)]), 'shade', 'b', False),
             L([(34, -4), (46, -4)], TIE, 'f', False, False, 2.6),
             L(curls(14, 70, (14, 15), 5, 0.3), 'mid', 'f'), L([(26, 62), (28, 70)], TIE, 'f', False, False, 2.6),
             L(ell(90, 86, 4.4, 4.8), NOSE, 'f', ln=True), L(quad((78, 95), (84, 97), (90, 95)), OUTC, 'f', False, False, 1.3),
             L([(84, 97), (88, 97), (88, 102), (84, 102)], WHITE, 'f', False)],
    'back': [L(outline([(30, -12), (34, -28, 1), (42, -20), (50, -32, 1), (58, -20), (66, -28, 1), (70, -12), (60, -4), (40, -4)])),
             L(outline([(44, 8), (45, -5), (55, -5), (56, 8)])),
             L(outline([(16, 66), (12, 36), (24, 14), (50, 6), (76, 14), (88, 36), (84, 66), (50, 72)])),
             L(outline([(56, 8), (76, 14), (88, 36), (84, 64), (64, 70)]), 'shade', 'b', False),
             L([(44, -4), (56, -4)], TIE, 'f', False, False, 2.6),
             L(curls(6, 74, (14, 15), 5, 0.2), 'mid', 'f'), L(curls(94, 74, (14, 15), 5, 0.5), 'mid', 'f'),
             L([(18, 66), (20, 72)], TIE, 'f', False, False, 2.6), L([(82, 66), (80, 72)], TIE, 'f', False, False, 2.6)],
}

# Belphegor Inos (Mortam Malius): pelo carmesí en pinchos con la raya en medio y un mechón largo a un lado de la cara; orejas
# de punta, una trenza que le cae por delante, ojos amarillos afilados, rayas rojizas en las mejillas y sonrisa con colmillo
CHEEK = (176, 80, 60, 255)
CHARS[T + 'mortam-malius'] = {
    'body': 'normal', 'pal': pal('#b02a3a', '#fcdcc0', iris='#d8b020', shade='#8a1e2c', deep='#64141e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(14, 70), (2, 60, 1), (12, 76)]), 'skin', 'b', ln=True), L(outline([(86, 70), (98, 60, 1), (88, 76)]), 'skin', 'b', ln=True),
              L(outline([(14, 66), (10, 46), (-2, 40, 1), (8, 32), (2, 14, 1), (18, 16), (18, -4, 1), (32, 8), (40, -12, 1), (50, 4), (62, -10, 1), (66, 8), (82, 0, 1), (80, 18),
                         (98, 22, 1), (88, 34), (100, 44, 1), (88, 48), (86, 66), (80, 52), (20, 52)])),
              L(outline([(62, -10), (66, 8), (82, 0), (80, 18), (98, 22), (88, 34), (100, 44), (88, 48), (86, 62), (76, 30)]), 'shade', 'b', False),
              L(outline([(14, 62), (16, 40), (30, 26), (48, 22), (50, 36), (52, 22), (70, 26), (84, 40), (86, 60), (80, 50), (68, 40), (58, 40), (52, 48, 1), (46, 40), (34, 40),
                         (24, 50), (18, 66, 1)]), 'mid', 'f'),
              L(outline([(16, 44), (24, 48), (20, 80), (14, 96, 1), (14, 70)]), 'mid', 'f'),
              L(outline([(54, 24), (70, 26), (84, 40), (86, 58), (80, 50), (68, 40)]), 'shade', 'f', False),
              L(outline([(22, 92), (30, 94), (34, 112), (28, 118, 1), (22, 106)]), 'mid', 'f', ln=True),
              L([(24, 100), (32, 101)], 'deep', 'f', False, False, 0.9), L([(25, 108), (33, 109)], 'deep', 'f', False, False, 0.9),
              L([(28, 84), (34, 88)], CHEEK, 'f', False, False, 1.4), L([(28, 88), (34, 92)], CHEEK, 'f', False, False, 1.4),
              L([(72, 84), (66, 88)], CHEEK, 'f', False, False, 1.4), L([(72, 88), (66, 92)], CHEEK, 'f', False, False, 1.4),
              L([(54, 96), (55, 99), (56, 96)], WHITE, 'f', False)],
    'side': [L(outline([(76, 56), (84, 46), (94, 40, 1), (86, 32), (100, 22, 1), (84, 18), (88, 2, 1), (70, 8), (64, -12, 1), (52, 4), (32, -8, 1), (30, 10), (10, 6, 1), (14, 22),
                        (-4, 30, 1), (10, 40), (2, 56, 1), (14, 60), (18, 76, 1), (30, 70), (40, 60), (50, 54), (66, 52)])),
             L(outline([(4, 30), (30, 34), (44, 56), (30, 70), (14, 60)]), 'shade', 'b', False),
             L(outline([(42, 64), (34, 50, 1), (50, 62)]), 'skin', 'f', ln=True),
             L(outline([(30, 74), (38, 76), (40, 106), (34, 114, 1), (30, 100)]), 'mid', 'f', ln=True),
             L([(80, 86), (86, 90)], CHEEK, 'f', False, False, 1.4)],
    'back': [L(outline([(14, 70), (2, 60, 1), (12, 76)]), 'skin', 'b', ln=True), L(outline([(86, 70), (98, 60, 1), (88, 76)]), 'skin', 'b', ln=True),
             L(outline([(14, 80), (8, 60), (-4, 50, 1), (8, 44), (0, 28, 1), (14, 24), (12, 6, 1), (28, 12), (34, -8, 1), (46, 6), (58, -10, 1), (62, 8), (80, 2, 1), (80, 20),
                        (98, 26, 1), (90, 40), (100, 52, 1), (90, 60), (86, 80), (70, 76), (60, 88, 1), (50, 78), (40, 88, 1), (30, 76)])),
             L(outline([(58, -10), (62, 8), (80, 2), (80, 20), (98, 26), (90, 40), (100, 52), (90, 60), (86, 78), (66, 76), (66, 20)]), 'shade', 'b', False),
             L(outline([(44, 76), (56, 76), (58, 108), (50, 116, 1), (42, 108)]), 'mid', 'f', ln=True)],
}

# Amdu Scias (Dante Dusias): pelo blanco en media melena con flequillo de mechones hasta los ojos y las puntas abiertas a
# los lados; dos mechones finísimos le cuelgan de las sienes hasta el pecho; un ojo rojo y otro amarillo, sonrisa
YELLOW = (232, 200, 40, 255)


def _thin(pts, c):
    return [L(pts, OUTC, 'f', False, False, 2.4), L(pts, c, 'f', False, False, 1.2)]


CHARS[T + 'dante-dusias'] = {
    'body': 'normal', 'pal': pal('#eeeee6', '#fcdcc4', iris='#d03020', shade='#c8c4b8', deep='#a8a498'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(10, 88), (6, 60), (-4, 72, 1), (8, 30), (18, 10), (50, 0), (82, 10), (92, 30), (104, 72, 1), (94, 60), (90, 88), (84, 76), (84, 60), (16, 60), (16, 76)])),
              L(outline([(60, 2), (82, 10), (92, 30), (104, 72), (94, 60), (90, 84), (84, 60), (80, 30)]), 'shade', 'b', False),
              L(outline([(12, 64), (12, 40), (24, 20), (50, 14), (76, 20), (88, 40), (88, 64), (82, 56), (76, 70, 1), (70, 52), (62, 62), (58, 46), (52, 68, 1), (48, 48), (40, 60),
                         (34, 46), (28, 66, 1), (20, 54)]), 'mid', 'f'),
              L(outline([(58, 16), (76, 20), (88, 40), (88, 62), (82, 56), (76, 68), (70, 46)]), 'shade', 'f', False),
              L(ell(65, 76, 3.4, 4.2), YELLOW, 'f', False), L(ell(63, 74.4, 1.1, 1.1), WHITE, 'f', False)]
             + _thin([(22, 56), (20, 84), (22, 118)], (238, 238, 230, 255)) + _thin([(78, 56), (80, 84), (78, 118)], (238, 238, 230, 255)),
    'side': [L(outline([(78, 66), (88, 50), (92, 30), (82, 10), (60, -2), (36, -2), (14, 8), (2, 30), (0, 56), (-6, 74, 1), (8, 74), (14, 88), (30, 86), (40, 72), (44, 58), (56, 54),
                        (70, 56)])),
             L(outline([(2, 30), (30, 34), (44, 58), (30, 86), (14, 86), (4, 60)]), 'shade', 'b', False),
             L(outline([(70, 8), (88, 22), (92, 44), (90, 66, 1), (84, 50), (78, 34)]), 'mid', 'f')]
            + _thin([(72, 58), (74, 84), (72, 118)], (238, 238, 230, 255)),
    'back': [L(outline([(10, 88), (-4, 74, 1), (6, 60), (8, 30), (18, 10), (50, 0), (82, 10), (92, 30), (94, 60), (104, 74, 1), (90, 88), (78, 82), (70, 94, 1), (60, 84),
                        (50, 96, 1), (40, 84), (30, 94, 1), (22, 82)])),
             L(outline([(56, 2), (82, 10), (92, 30), (94, 60), (104, 74), (90, 86), (68, 86), (68, 30)]), 'shade', 'b', False)],
}

# Beelze Bub (Beel Zebub): media melena lisa partida en dos colores, rosa a un lado y negra al otro, con flequillo recto
# hasta las cejas; ojos amarillos con raya rosa encima y boca seria
PINK = (224, 80, 122, 255)
PINK_D = (184, 58, 96, 255)
BLK = (42, 32, 38, 255)
BLK_D = (28, 22, 26, 255)
CHARS[T + 'beel-zebub'] = {
    'body': 'normal', 'pal': pal('#e0507a', '#fcdcc4', iris='#d8d020', shade='#b83a60', deep='#8a2a48'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(50, -4), (26, 2), (12, 18), (6, 44), (8, 92, 1), (18, 88), (18, 60), (50, 60)]), PINK),
              L(outline(mirror_x([(50, -4), (26, 2), (12, 18), (6, 44), (8, 92, 1), (18, 88), (18, 60), (50, 60)])), BLK),
              L([(50, 14), (32, 18), (18, 30), (12, 46), (12, 64), (50, 64)], PINK, 'f', False),
              L([(50, 14), (68, 18), (82, 30), (88, 46), (88, 64), (50, 64)], BLK, 'f', False),
              L(outline([(12, 64), (12, 46), (18, 28), (32, 18), (50, 14), (68, 18), (82, 28), (88, 46), (88, 64)], 2) + [(50, 64)], OUTC, 'f', False, False, 1.4),
              L([(12, 64), (88, 64)], OUTC, 'f', False, False, 1.6),
              strand([(30, 22), (26, 62)], PINK_D, 'f', 1.0), strand([(40, 18), (40, 62)], PINK_D, 'f', 1.0), strand([(62, 18), (62, 62)], BLK_D, 'f', 1.0),
              strand([(72, 22), (76, 62)], BLK_D, 'f', 1.0),
              L(quad((27, 69), (35, 67), (43, 70)), PINK, 'f', False, False, 1.8), L(quad((73, 69), (65, 67), (57, 70)), PINK, 'f', False, False, 1.8)],
    'side': [L(outline([(84, 64), (90, 40), (84, 14), (62, 0), (36, -2), (14, 8), (2, 30), (0, 60), (4, 92, 1), (14, 86), (26, 90, 1), (36, 80), (42, 64), (56, 62), (74, 62)]), PINK),
             L(outline([(2, 34), (30, 40), (42, 64), (26, 90), (4, 90)]), PINK_D, 'b', False),
             L(outline([(76, 38), (88, 38), (92, 64), (78, 64)]), PINK, 'f'),
             L(quad((76, 67), (80, 66), (85, 67)), PINK, 'f', False, False, 1.6)],
    'back': [L(outline([(50, -4), (26, 2), (12, 18), (6, 44), (8, 92, 1), (20, 86), (30, 94, 1), (40, 86), (50, 94)]), BLK),
             L(outline(mirror_x([(50, -4), (26, 2), (12, 18), (6, 44), (8, 92, 1), (20, 86), (30, 94, 1), (40, 86), (50, 94)])), PINK)],
}

# Belial Noze (Malik Sinn): bajito y moreno; pelo morado con raya en medio y dos coletas largas que salen de lo alto con
# gomas verde lima, con mechones rosas por dentro; un mechón rosa le cruza la frente; ojos rosas enfadados y rubor
LIME = (168, 200, 58, 255)
PINKS = (224, 80, 122, 255)
BLUSH = (236, 150, 130, 255)
CHARS[T + 'malik-sinn'] = {
    'body': 'bajito', 'pal': pal('#7a5ab8', '#c88a5a', iris='#c83a6a', shade='#604696', deep='#463270'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95,
             'hairline': [(14, 62), (18, 46), (30, 36), (46, 30), (50, 34), (54, 30), (70, 36), (82, 46), (86, 62)]},
    'front': [L(outline([(20, 22), (2, 34), (-8, 60), (-10, 104, 1), (2, 90), (6, 60), (16, 40)])), L(outline(mirror_x([(20, 22), (2, 34), (-8, 60), (-10, 104, 1), (2, 90), (6, 60), (16, 40)]))),
              L(quad((10, 34), (-2, 60), (-4, 96)), PINKS, 'b', False, False, 2.4), L(quad((90, 34), (102, 60), (104, 96)), PINKS, 'b', False, False, 2.4),
              L(outline([(14, 62), (10, 40), (18, 16), (36, 4), (50, 2), (64, 4), (82, 16), (90, 40), (86, 62), (80, 46), (20, 46)])),
              L(outline([(56, 4), (82, 16), (90, 40), (86, 58), (76, 34)]), 'shade', 'b', False),
              strand([(50, 4), (50, 32)], 'deep', 'b', 1.0),
              L(quad((50, 6), (44, 30), (34, 48)), PINKS, 'f', False, False, 2.6),
              L(ell(18, 22, 5, 4.4), LIME, 'f', ln=True), L(ell(82, 22, 5, 4.4), LIME, 'f', ln=True),
              L(ell(28, 86, 3.6, 2.2), BLUSH, 'f', False), L(ell(72, 86, 3.6, 2.2), BLUSH, 'f', False)],
    'side': [L(outline([(44, 12), (30, 20), (18, 50), (12, 104, 1), (24, 86), (28, 56), (40, 30)])),
             L(quad((32, 26), (22, 56), (20, 96)), PINKS, 'b', False, False, 2.4),
             L(outline([(76, 46), (80, 34), (70, 14), (50, 4), (28, 8), (12, 24), (6, 46), (10, 66), (24, 74), (38, 68), (44, 56), (58, 48), (70, 46)])),
             L(outline([(8, 30), (30, 34), (44, 56), (24, 72), (10, 64)]), 'shade', 'b', False),
             L(ell(44, 12, 5, 4.4), LIME, 'f', ln=True),
             L(quad((60, 8), (76, 24), (82, 44)), PINKS, 'f', False, False, 2.2),
             L(ell(80, 86, 3, 2), BLUSH, 'f', False)],
    'back': [L(outline([(22, 20), (4, 30), (-8, 60), (-10, 104, 1), (2, 90), (8, 60), (18, 36)])), L(outline(mirror_x([(22, 20), (4, 30), (-8, 60), (-10, 104, 1), (2, 90), (8, 60), (18, 36)]))),
             L(quad((10, 32), (-2, 60), (-4, 96)), PINKS, 'b', False, False, 2.4), L(quad((90, 32), (102, 60), (104, 96)), PINKS, 'b', False, False, 2.4),
             L(outline([(16, 72), (12, 40), (20, 16), (50, 4), (80, 16), (88, 40), (84, 72), (50, 78)])),
             L(outline([(56, 6), (80, 16), (88, 40), (84, 70), (62, 76)]), 'shade', 'b', False),
             strand([(50, 6), (50, 76)], 'deep', 'b', 1.0),
             L(ell(20, 20, 5, 4.4), LIME, 'f', ln=True), L(ell(80, 20, 5, 4.4), LIME, 'f', ln=True)],
}

# Asmo Deus (Ian Qubus): pelo morado peinado de lado que le tapa un ojo, con las puntas turquesa; por detrás, una melena
# negra enorme y salvaje en pinchos que le llega a los hombros; un ojo azul a la vista y sonrisa
MANE = (26, 20, 30, 255)
TEAL = (90, 176, 192, 255)
CHARS[T + 'ian-qubus'] = {
    'body': 'normal', 'pal': pal('#6a5aa8', '#fcdcc8', iris='#3a8ac8', shade='#52468a', deep='#3c3266'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(16, 60), (20, 44), (40, 32), (60, 30), (78, 38), (84, 50), (86, 62)]},
    'front': [L(outline([(18, 80), (-6, 96), (-28, 110, 1), (-8, 86), (-26, 70, 1), (-6, 60), (-20, 40, 1), (0, 36), (-6, 10, 1), (14, 14), (20, -10, 1), (36, 4), (50, -6),
                         (64, 4), (80, -10, 1), (86, 14), (106, 10, 1), (100, 36), (120, 40, 1), (106, 60), (126, 70, 1), (108, 86), (128, 110, 1), (106, 96), (82, 80)]), MANE),
              L(outline([(16, 62), (12, 36), (22, 14), (40, 4), (60, 4), (78, 14), (88, 36), (86, 62), (80, 46), (20, 46)])),
              L(outline([(60, 4), (78, 14), (88, 36), (86, 58), (78, 34)]), 'shade', 'b', False),
              L(outline([(10, 40), (24, 18), (46, 10), (70, 14), (86, 30), (80, 34), (64, 30), (54, 40), (48, 64), (42, 86, 1), (30, 78), (20, 64), (14, 52)]), 'mid', 'f'),
              L(outline([(16, 60), (30, 72), (42, 86), (46, 66), (32, 60), (18, 54)]), TEAL, 'f', False),
              L(outline([(46, 12), (70, 14), (86, 30), (80, 34), (64, 30), (54, 40), (40, 26)]), 'light', 'f', False)],
    'side': [L(outline([(40, 70), (20, 90), (2, 118, 1), (4, 92), (-16, 96, 1), (-6, 76), (-24, 62, 1), (-6, 50), (-20, 30, 1), (0, 24), (-6, 2, 1), (14, 8), (20, -12, 1), (36, 0),
                        (56, -4), (60, 20), (46, 50)]), MANE),
             L(outline([(76, 40), (80, 26), (70, 8), (50, 0), (30, 4), (16, 20), (14, 44), (24, 60), (36, 64), (42, 56), (56, 46), (68, 42)])),
             L(outline([(66, 10), (86, 22), (94, 44), (90, 66, 1), (82, 52), (76, 36)]), 'mid', 'f'),
             L(outline([(84, 50), (92, 54), (90, 66), (84, 58)]), TEAL, 'f', False)],
    'back': [L(outline([(18, 80), (-6, 100), (-28, 114, 1), (-8, 86), (-26, 70, 1), (-6, 60), (-20, 40, 1), (0, 36), (-6, 10, 1), (14, 14), (20, -10, 1), (36, 4), (50, -8),
                        (64, 4), (80, -10, 1), (86, 14), (106, 10, 1), (100, 36), (120, 40, 1), (106, 60), (126, 70, 1), (108, 86), (128, 114, 1), (106, 100), (82, 80),
                        (70, 110, 1), (60, 90), (50, 112, 1), (40, 90), (30, 110, 1)]), MANE)],
}


# Satan Gaul (Beryl): melena enorme de pinchos naranja rojizo en todas direcciones; por delante, dos mechones salmón que le
# salen de la raya y se abren hacia los lados, y mechones salmón junto a la cara; ojos turquesa con raya negra marcada,
# cejas rojizas muy fruncidas
def satan(outer, inner, inner_d, front_extra, side_extra, face):
    oc, ic, idc = outer, inner, inner_d
    return {
        'body': 'normal', 'pal': pal(ic, '#fce0cc', iris='#2a8a9a', shade=idc, deep=oc),
        'face': face,
        'front': [L(outline(radial(50, 40, (66, 62), (40, 36), 196, -16, 9, 0.12, 3) + [(88, 96, 1), (78, 100), (50, 98), (22, 100), (12, 96, 1)]), oc),
                  L(outline([(16, 92), (10, 60), (12, 30), (24, 12), (50, 4), (76, 12), (88, 30), (90, 60), (84, 92), (80, 62), (20, 62)])),
                  L(outline([(60, 6), (76, 12), (88, 30), (90, 60), (84, 90), (80, 50)]), 'shade', 'b', False),
                  L(outline([(50, 8), (36, 12), (16, 20), (-6, 30, 1), (14, 32), (30, 30), (46, 22)]), 'mid', 'f', ln=True),
                  L(outline(mirror_x([(50, 8), (36, 12), (16, 20), (-6, 30, 1), (14, 32), (30, 30), (46, 22)])), 'mid', 'f', ln=True),
                  L(outline([(17, 42), (12, 70), (14, 98, 1), (22, 70), (24, 46)]), 'mid', 'f'), L(outline(mirror_x([(17, 42), (12, 70), (14, 98, 1), (22, 70), (24, 46)])), 'mid', 'f'),
                  L([(46, 8), (50, 14), (47, 18), (53, 24)], OUTC, 'f', False, False, 1.2)] + front_extra,
        'side': [L(outline(radial(40, 42, (64, 62), (40, 38), 96, 262, 9, 0.12, 5) + [(40, 92), (62, 70), (76, 40), (64, 4)]), oc),
                 L(outline([(76, 44), (80, 28), (70, 10), (50, 2), (30, 6), (16, 20), (12, 44), (20, 62), (36, 66), (42, 56), (56, 48), (68, 44)])),
                 L(outline([(64, 6), (86, 10), (104, 24, 1), (86, 22), (74, 24)]), 'mid', 'f', ln=True),
                 L(outline([(70, 30), (84, 34), (88, 66), (84, 96, 1), (78, 62)]), 'mid', 'f')] + side_extra,
        'back': [L(outline(radial(50, 44, (66, 66), (42, 42), -62, 242, 12, 0.12, 7) + [(34, 96), (50, 100), (66, 96)]), oc),
                                  strand([(50, 10), (50, 70)], (150, 40, 20, 255), 'b', 1.0)],
    }


EYELINE = (30, 30, 40, 255)
CHARS[T + 'beryl'] = satan((240, 74, 26, 255), '#f49a80', '#d8786a',
                           [L(quad((26, 70), (36, 67), (46, 71)), EYELINE, 'f', False, False, 2.0), L(quad((74, 70), (64, 67), (54, 71)), EYELINE, 'f', False, False, 2.0),
                            L([(28, 64), (44, 68)], (150, 50, 30, 255), 'f', False, False, 3.0), L([(72, 64), (56, 68)], (150, 50, 30, 255), 'f', False, False, 3.0),
                            L([(44, 60), (46, 66)], (150, 50, 30, 255), 'f', False, False, 1.4), L([(56, 60), (54, 66)], (150, 50, 30, 255), 'f', False, False, 1.4)],
                           [L([(70, 64), (84, 68)], (150, 50, 30, 255), 'f', False, False, 3.0)],
                           {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 95,
                            'hairline': [(16, 62), (20, 44), (34, 36), (50, 30), (66, 36), (80, 44), (84, 62)]})

# Satan Gaul, tercera cara (beryl-ok-satan-mc): con el cuello recto, el pelo rojo intenso aún más erizado, los ojos redondos
# enormes de blanco grisáceo con el iris turquesa pequeño, cejas afiladas y la boca abierta de par en par gritando
GREYW = (226, 228, 230, 255)
CHARS[T + 'beryl-ok-satan-mc'] = satan((200, 20, 46, 255), '#e83a52', '#c02a40',
                                       [L(ell(36, 76, 7.4, 7.6), OUTC, 'f', False), L(ell(36, 76, 6.2, 6.4), GREYW, 'f', False), L(ell(36, 76, 2.6, 2.8), (42, 138, 154, 255), 'f', False),
                                        L(ell(36, 76, 1.1, 1.2), PUPIL, 'f', False),
                                        L(ell(64, 76, 7.4, 7.6), OUTC, 'f', False), L(ell(64, 76, 6.2, 6.4), GREYW, 'f', False), L(ell(64, 76, 2.6, 2.8), (42, 138, 154, 255), 'f', False),
                                        L(ell(64, 76, 1.1, 1.2), PUPIL, 'f', False),
                                        L([(26, 62), (44, 68)], OUTC, 'f', False, False, 2.6), L([(74, 62), (56, 68)], OUTC, 'f', False, False, 2.6),
                                        L(quad((40, 90), (50, 86), (60, 90)) + quad((60, 90), (58, 102), (50, 104))[1:] + quad((50, 104), (42, 102), (40, 90))[1:], (120, 30, 40, 255), 'f', ln=True),
                                        L(quad((42, 91), (50, 88), (58, 91)), WHITE, 'f', False, False, 1.6)],
                                       [L([(70, 62), (84, 66)], OUTC, 'f', False, False, 2.6)],
                                       {'eyes': 'round', 'brows': False, 'mouth': 'grin', 'mouth_y': 96,
                                        'hairline': [(16, 62), (20, 44), (34, 36), (50, 30), (66, 36), (80, 44), (84, 62)]})

# Sar Gatanas (Serge): cara alargada; melena lisa gris pizarra hasta el pecho que le tapa un ojo, con mechones finos azul
# claro a los lados; un ojo cerrado dibujado en la frente; el otro ojo amarillo entornado y sonrisa
LBLUE = (168, 208, 232, 255)
MARKB = (130, 96, 60, 255)
CHARS[T + 'serge'] = {
    'body': 'delgado', 'pal': pal('#3a4a58', '#fcdcc0', iris='#d8c020', shade='#2c3a46', deep='#202a34'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 97, 'eye_y': 76,
             'hairline': [(14, 60), (18, 36), (30, 22), (44, 14), (60, 14), (80, 30), (86, 60)],
             'face_front': blob([(18, 46), (50, 36), (82, 46), (84, 76), (80, 100), (64, 110), (50, 112), (36, 110), (20, 100), (16, 76)])},
    'front': [L(outline([(8, 112, 1), (6, 70), (8, 30), (20, 8), (46, 0), (76, 6), (90, 24), (94, 60), (94, 112, 1), (84, 106), (82, 60), (18, 60), (18, 106)])),
              L(outline([(60, 2), (76, 6), (90, 24), (94, 60), (94, 110), (86, 104), (84, 40)]), 'shade', 'b', False),
              L(outline([(40, 8), (64, 6), (84, 20), (90, 44), (88, 90), (80, 106, 1), (66, 90), (56, 70), (52, 50), (48, 26)]), 'mid', 'f'),
              L(outline([(64, 8), (84, 20), (90, 44), (88, 88), (82, 100), (78, 60)]), 'shade', 'f', False),
              L(outline([(16, 34), (22, 40), (20, 106, 1), (14, 80)]), 'mid', 'f'),
              L(quad((34, 40), (40, 44), (48, 40)), MARKB, 'f', False, False, 1.6),
              L([(36, 42), (35, 45)], MARKB, 'f', False, False, 1.0), L([(41, 43.5), (41, 47)], MARKB, 'f', False, False, 1.0), L([(46, 42), (47, 45)], MARKB, 'f', False, False, 1.0),
              L(quad((16, 40), (12, 80), (14, 112)), LBLUE, 'f', False, False, 1.4), L(quad((86, 40), (90, 80), (88, 112)), LBLUE, 'f', False, False, 1.4)],
    'side': [L(outline([(74, 30), (78, 18), (66, 4), (44, -2), (22, 4), (8, 22), (2, 50), (0, 90), (4, 120, 1), (18, 116), (28, 96), (36, 76), (42, 60), (56, 44), (66, 36)])),
             L(outline([(4, 40), (30, 46), (40, 66), (28, 96), (6, 116)]), 'shade', 'b', False),
             L(quad((60, 4), (48, 50), (52, 118)), LBLUE, 'f', False, False, 1.4),
             L(outline([(70, 20), (86, 32), (90, 60), (86, 100, 1), (78, 64)]), 'mid', 'f')],
    'back': [L(outline([(8, 112, 1), (6, 40), (14, 14), (30, 2), (50, -2), (70, 2), (86, 14), (94, 40), (94, 112, 1), (70, 108), (56, 112, 1), (50, 96), (44, 112, 1), (30, 108)])),
             L(outline([(56, 0), (86, 14), (94, 40), (94, 110), (70, 106), (66, 40)]), 'shade', 'b', False),
             strand([(50, 2), (50, 96)], 'deep', 'b', 1.0),
             L(quad((14, 40), (10, 80), (12, 112)), LBLUE, 'f', False, False, 1.4), L(quad((86, 40), (90, 80), (88, 112)), LBLUE, 'f', False, False, 1.4)],
}

# As Taroth (Aster Roth): grandullón moreno; melena lisa gris oscuro hasta los hombros con pico en la frente y dos mechones
# que se levantan a los lados como cuernos; mechones delante de las orejas con dos anillas doradas; ojos rojos y cejas
# negras gruesas y fruncidas
CHARS[T + 'aster-roth'] = {
    'body': 'corpulento', 'pal': pal('#4a3e44', '#8a5a3a', iris='#c02a3a', shade='#3a3036', deep='#2a2226'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 99, 'eye_y': 76,
             'hairline': [(16, 62), (18, 40), (30, 30), (42, 34), (50, 48), (58, 34), (70, 30), (82, 40), (84, 62)]},
    'front': [L(outline([(20, 20), (4, 22), (-14, 14, 1), (2, 30), (18, 34)])), L(outline(mirror_x([(20, 20), (4, 22), (-14, 14, 1), (2, 30), (18, 34)]))),
              L(outline([(10, 102), (8, 60), (10, 30), (20, 14), (36, 4), (50, 8), (64, 4), (80, 14), (90, 30), (92, 60), (90, 102), (84, 96), (82, 60), (18, 60), (16, 96)])),
              L(outline([(60, 6), (80, 14), (90, 30), (92, 60), (90, 100), (84, 94), (82, 40)]), 'shade', 'b', False),
              strand([(50, 10), (50, 44)], 'deep', 'b', 1.0), strand([(34, 8), (28, 36)], 'deep', 'b', 1.0), strand([(66, 8), (72, 36)], 'deep', 'b', 1.0),
              L(outline([(14, 44), (22, 46), (22, 102), (14, 106, 1)]), 'mid', 'f'), L(outline([(86, 44), (78, 46), (78, 102), (86, 106, 1)]), 'mid', 'f'),
              L([(13, 51), (23, 51)], GOLD, 'f', False, False, 2.6), L([(13, 57), (23, 57)], GOLD, 'f', False, False, 2.6),
              L([(77, 51), (87, 51)], GOLD, 'f', False, False, 2.6), L([(77, 57), (87, 57)], GOLD, 'f', False, False, 2.6),
              L([(50, 76), (47, 90), (53, 91)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(40, 16), (24, 4), (6, 2, 1), (20, 14), (30, 24)])),
             L(outline([(74, 30), (78, 18), (66, 4), (44, -2), (22, 4), (8, 22), (2, 50), (-4, 90), (-10, 116, 1), (10, 108), (24, 94), (34, 76), (42, 60), (56, 44), (66, 36)])),
             L(outline([(4, 40), (30, 46), (40, 66), (24, 94), (-6, 112)]), 'shade', 'b', False),
             L(outline([(62, 40), (70, 40), (72, 100), (66, 104, 1)]), 'mid', 'f'),
             L([(61, 50), (71, 50)], GOLD, 'f', False, False, 2.6), L([(61, 56), (71, 56)], GOLD, 'f', False, False, 2.6)],
    'back': [L(outline([(20, 22), (4, 22), (-14, 12, 1), (2, 32), (18, 36)])), L(outline(mirror_x([(20, 22), (4, 22), (-14, 12, 1), (2, 32), (18, 36)]))),
             L(outline([(8, 108, 1), (6, 50), (10, 26), (24, 8), (50, 0), (76, 8), (90, 26), (94, 50), (92, 108, 1), (70, 104), (50, 108), (30, 104)])),
             L(outline([(56, 2), (76, 8), (90, 26), (94, 50), (92, 106), (70, 104), (66, 40)]), 'shade', 'b', False),
             strand([(50, 2), (50, 104)], 'deep', 'b', 1.0)],
}

# Luci Fanos (Lu Jiver): bajito; pelo azul muy claro con un flequillo grande barrido de lado que sube en una onda arriba y
# puntas que se enroscan como ganchos junto a las mejillas; ojos rosas grandes y rayitas en las mejillas
CHARS[T + 'lu-jiver'] = {
    'body': 'bajito', 'pal': pal('#c4e2e2', '#fcdcc8', iris='#d04a7a', shade='#9cc0c2', deep='#7a9ea0'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'line', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(10, 86), (6, 56), (10, 30), (22, 10), (44, 2), (60, -4), (78, -18, 1), (80, 4), (90, 20), (94, 50), (92, 86), (84, 74), (84, 60), (16, 60), (16, 74)])),
              L(outline([(60, -2), (78, -18), (80, 4), (90, 20), (94, 50), (92, 84), (84, 60), (80, 26)]), 'shade', 'b', False),
              L(outline([(12, 62), (14, 40), (26, 22), (50, 16), (74, 20), (86, 34), (88, 56), (84, 66), (80, 58), (72, 48), (60, 44), (48, 46), (36, 56), (24, 70, 1)]), 'mid', 'f'),
              L(outline([(56, 18), (74, 20), (86, 34), (88, 54), (80, 56), (72, 46)]), 'shade', 'f', False),
              L(quad((86, 56), (96, 74), (84, 84)), 'mid', 'f', False, False, 2.6), L(quad((14, 62), (4, 78), (16, 86)), 'mid', 'f', False, False, 2.6),
              L([(26, 86), (32, 84)], (140, 190, 200, 255), 'f', False, False, 1.2), L([(74, 86), (68, 84)], (140, 190, 200, 255), 'f', False, False, 1.2)],
    'side': [L(outline([(80, 62), (88, 48), (92, 30), (86, 10), (90, -16, 1), (70, -2), (48, -4), (26, 2), (10, 18), (2, 44), (4, 70), (14, 86), (30, 84), (40, 70), (44, 58), (58, 54),
                        (70, 56)])),
             L(outline([(4, 30), (30, 34), (44, 58), (30, 84), (14, 84)]), 'shade', 'b', False),
             L(outline([(70, 8), (88, 22), (92, 46), (88, 62, 1), (82, 48), (76, 32)]), 'mid', 'f'),
             L(quad((86, 58), (96, 74), (86, 84)), 'mid', 'f', False, False, 2.6), L(quad((8, 70), (-4, 84), (8, 94)), 'mid', 'b', False, False, 2.6)],
    'back': [L(outline([(10, 86), (6, 56), (8, 30), (20, 10), (40, 2), (22, -18, 1), (56, -2), (78, 8), (90, 26), (94, 56), (90, 86), (70, 92), (50, 88), (30, 92)])),
             L(outline([(56, -2), (78, 8), (90, 26), (94, 56), (90, 84), (66, 88), (66, 30)]), 'shade', 'b', False),
             L(quad((10, 70), (-2, 84), (10, 94)), 'mid', 'f', False, False, 2.6), L(quad((90, 70), (102, 84), (90, 94)), 'mid', 'f', False, False, 2.6)],
}

# Gaap Redel (Zagan Barbatos): calvo con una cresta corta azul marino en el centro; la cara pintada de calavera (cuencas
# negras, nariz negra y la mandíbula verde grisácea con los dientes dibujados); trencitas oscuras con cuentas doradas y
# calaveritas blancas colgando a los lados
NAVY = (30, 34, 56, 255)
MASK = (64, 96, 88, 255)
TEETH = (196, 200, 196, 255)
BRAID = (40, 40, 50, 255)


def _skull(x, y):
    return [L(ell(x, y, 5.6, 5.0), (238, 232, 226, 255), 'f', ln=True), L(ell(x - 2, y - 1, 1.2, 1.4), OUTC, 'f', False), L(ell(x + 2, y - 1, 1.2, 1.4), OUTC, 'f', False),
            L([(x - 2.4, y + 2.4), (x + 2.4, y + 2.4)], OUTC, 'f', False, False, 0.8)]


def _braid(pts, beads):
    out = [L(pts, BRAID, 'f', False, False, 2.6)]
    for (x, y) in beads:
        out.append(L([(x, y - 1.6), (x, y + 1.6)], GOLD, 'f', False, False, 3.0))
    return out


CHARS[T + 'zagan-barbatos'] = {
    'body': 'delgado', 'pal': pal('#1e2238', '#e8d4b0', iris='#2a2222', shade='#161a2c', deep='#10121e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': [L(outline([(18, 62), (16, 32), (26, 12), (50, 4), (74, 12), (84, 32), (82, 62)]), 'skin'),
              L(outline([(44, 2), (56, 2), (56, 30), (44, 30)]), NAVY, 'f'),
              L(blob([(20, 84), (50, 86), (80, 84), (82, 96), (66, 108), (50, 110), (34, 108), (18, 96)]), MASK, 'f', False),
              L([(32, 90), (68, 90), (66, 100), (34, 100)], TEETH, 'f', False), L([(32, 90), (68, 90), (66, 100), (34, 100), (32, 90)], OUTC, 'f', False, False, 1.2),
              L([(32, 95), (67, 95)], OUTC, 'f', False, False, 0.9)]
             + [L([(x, 90), (x, 100)], OUTC, 'f', False, False, 0.8) for x in (38, 44, 50, 56, 62)]
             + [L(ell(36, 75, 9, 9), OUTC, 'f', False), L(ell(36, 75, 4.4, 4.6), WHITE, 'f', False), L(ell(36, 75, 1.8, 1.8), (120, 110, 60, 255), 'f', False),
                L(ell(64, 75, 9, 9), OUTC, 'f', False), L(ell(64, 75, 4.4, 4.6), WHITE, 'f', False), L(ell(64, 75, 1.8, 1.8), (120, 110, 60, 255), 'f', False),
                L([(46, 80), (54, 80), (50, 88)], OUTC, 'f', False)]
             + _braid([(17, 44), (14, 70), (12, 96)], [(16, 56), (13, 84)]) + _braid([(83, 44), (86, 70), (88, 96)], [(84, 56), (87, 84)])
             + _skull(11, 104) + _skull(89, 104),
    'side': [L(outline([(74, 30), (66, 12), (44, 4), (22, 10), (8, 28), (6, 56), (14, 72), (36, 70), (44, 56), (60, 44)]), 'skin'),
             L(outline([(76, 26), (60, 4), (36, 0), (34, 8), (58, 10), (72, 30)]), NAVY, 'f'),
             L(blob([(64, 86), (88, 84), (90, 96), (80, 106), (66, 104)]), MASK, 'f', False),
             L([(78, 90), (90, 90), (89, 98), (78, 98)], TEETH, 'f', False), L([(78, 90), (90, 90), (89, 98), (78, 98), (78, 90)], OUTC, 'f', False, False, 1.0),
             L(ell(81, 75, 6.4, 8), OUTC, 'f', False), L(ell(82, 75, 3.2, 3.6), WHITE, 'f', False), L(ell(83, 75, 1.4, 1.4), (120, 110, 60, 255), 'f', False)]
            + _braid([(38, 52), (34, 80), (36, 104)], [(37, 62), (34, 90)]) + _skull(36, 110),
    'back': [L(outline([(18, 72), (14, 40), (24, 14), (50, 4), (76, 14), (86, 40), (82, 72), (50, 80)]), 'skin'),
             L(outline([(56, 6), (76, 14), (86, 40), (82, 70), (62, 76)]), 'skin_d', 'b', False),
             L(outline([(44, 2), (56, 2), (56, 30), (44, 30)]), NAVY, 'f')]
            + _braid([(17, 44), (14, 70), (12, 96)], [(16, 56), (13, 84)]) + _braid([(83, 44), (86, 70), (88, 96)], [(84, 56), (87, 84)])
            + _skull(11, 104) + _skull(89, 104),
}

# Diabo Los (Grant Grimoire, entrenador): pelo turquesa en una seta enorme y redonda con dos puntas finas que salen en
# horizontal a los lados; cejas turquesa gruesas y afiladas, bigote turquesa fino con las puntas caídas, ojos rosas y sonrisa
# de dientes
TEALB = (50, 120, 112, 255)
CHARS[T + 'grant-grimoire'] = {
    'body': 'normal', 'pal': pal('#2a7a72', '#fcd4b0', iris='#c04a6a', shade='#1f5e58', deep='#16443f'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 99, 'hairline': False},
    'front': [L(outline([(8, 64), (0, 46), (-4, 28), (-26, 24, 1), (-2, 18), (10, 6), (30, -4), (50, -6), (70, -4), (90, 6), (102, 18), (126, 24, 1), (104, 28), (100, 46),
                         (92, 64), (84, 58), (78, 64, 1), (70, 56), (60, 60, 1), (50, 56), (40, 60, 1), (30, 56), (22, 64, 1), (16, 58)]), 'mid', 'f'),
              L(outline([(62, -4), (90, 6), (102, 18), (104, 28), (100, 46), (92, 62), (84, 56), (80, 30)]), 'shade', 'f', False),
              strand([(30, 0), (24, 56)], 'deep', 'f', 1.0), strand([(42, -4), (40, 56)], 'deep', 'f', 1.0), strand([(58, -4), (60, 56)], 'deep', 'f', 1.0),
              strand([(70, 0), (76, 56)], 'deep', 'f', 1.0),
              L([(26, 64), (44, 70)], TEALB, 'f', False, False, 3.2), L([(74, 64), (56, 70)], TEALB, 'f', False, False, 3.2),
              L(quad((48, 92), (36, 92), (32, 104)), TEALB, 'f', False, False, 1.6), L(quad((52, 92), (64, 92), (68, 104)), TEALB, 'f', False, False, 1.6),
              L(quad((40, 82), (42, 76), (46, 72)), (200, 150, 120, 255), 'f', False, False, 0.9), L(quad((60, 82), (58, 76), (54, 72)), (200, 150, 120, 255), 'f', False, False, 0.9)],
    'side': [L(outline([(92, 58), (100, 40), (96, 18), (76, 2), (50, -4), (24, 0), (-2, 14), (-24, 16, 1), (0, 22), (0, 40), (4, 58), (30, 62), (50, 60), (70, 62)])),
             L(outline([(4, 34), (40, 40), (70, 44), (92, 50), (90, 58), (70, 62), (50, 60), (30, 62), (4, 58)]), 'shade', 'b', False),
             L([(72, 64), (84, 68)], TEALB, 'f', False, False, 3.0), L(quad((88, 93), (82, 96), (80, 104)), TEALB, 'f', False, False, 1.6)],
    'back': [L(outline([(8, 70), (0, 50), (-4, 30), (-26, 24, 1), (-2, 20), (10, 6), (30, -4), (50, -6), (70, -4), (90, 6), (102, 20), (126, 24, 1), (104, 30), (100, 50), (92, 70),
                        (50, 76)])),
             L(outline([(0, 46), (100, 46), (92, 70), (50, 76), (8, 70)]), 'shade', 'b', False)],
}

# Simon Azazel (Baz Azel, ayudante): delgado de cara alargada; pelo gris verdoso corto con un mechón de punta hacia arriba en
# el centro y entradas; orejas grandes, gafas redondas finas, nariz larga y un colmillo
CHARS[T + 'baz-azel'] = {
    'body': 'delgado', 'pal': pal('#4a5e50', '#f4c8a0', iris='#3a4ab0', shade='#3a4a40', deep='#2a3630'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'line', 'mouth_y': 98, 'big_ears': 2, 'ear_out': 3, 'glasses': (60, 56, 64, 255),
             'hairline': [(20, 56), (24, 40), (36, 32), (50, 34), (64, 32), (76, 40), (80, 56)]},
    'front': [L(outline([(20, 58), (18, 40), (26, 24), (38, 14), (42, -4, 1), (50, 8), (58, -8, 1), (62, 10), (74, 22), (82, 40), (80, 58), (76, 44), (24, 44)])),
              L(outline([(58, -8), (62, 10), (74, 22), (82, 40), (80, 54), (70, 30)]), 'shade', 'b', False),
              L([(50, 72), (46, 90), (52, 92)], OUTC, 'f', False, False, 1.2),
              L([(58, 98), (60, 102), (62, 98)], WHITE, 'f', False)],
    'side': [L(outline([(70, 40), (76, 28), (70, 8), (64, -14, 1), (54, 2), (36, 2), (16, 12), (8, 30), (8, 56), (18, 66), (34, 62), (42, 52), (56, 44)])),
             L(outline([(8, 32), (32, 38), (42, 52), (18, 64)]), 'shade', 'b', False),
             L(outline([(84, 72), (96, 92), (86, 92)]), 'skin', 'f', ln=True)],
    'back': [L(outline([(18, 70), (14, 44), (22, 22), (36, 10), (44, -6, 1), (52, 6), (60, -8, 1), (64, 10), (78, 22), (86, 44), (82, 70), (50, 76)])),
             L(outline([(58, -6), (64, 10), (78, 22), (86, 44), (82, 68), (62, 74)]), 'shade', 'b', False)],
}
