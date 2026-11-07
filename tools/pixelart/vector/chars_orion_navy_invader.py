"""Navy Invader (orion-navy-invader): Estados Unidos (la marina) en Inazuma Eleven Orion no Kokuin, con sus modelos 3D de
'イナズマイレブン オリオンの刻印' (cada uno tiene una sola forma; ninguno coge por prefijo el dibujo de otro). Algunos modelos
de la enciclopedia salen mal encuadrados de perfil o de espaldas (Mop, Hellion, Howler): se completan con las otras vistas."""
import math

from chars import CHARS, L, OUTC, blob, bumpy, ell, outline, pal, rope, strand  # noqa: F401
from heads import quad  # noqa: F401

WHITE = (250, 248, 240, 255)
BLUSH = (240, 140, 140, 255)


def ring(pts):
    return pts + [pts[0]]


def star(cx, cy, rx, ry, n, amp=0.28, a0=0.0, seed=1):
    """Melena de pinchos alrededor de un centro (puntas afiladas alternas)."""
    import random
    r = random.Random(seed)
    pts = []
    for i in range(n * 2):
        a = a0 + math.pi * 2 * i / (n * 2)
        k = 1.0 + amp * (0.6 + 0.4 * r.random()) if i % 2 == 0 else 1.0 - amp * 0.3
        pts.append((cx + rx * k * math.cos(a), cy + ry * k * math.sin(a)) + ((1,) if i % 2 == 0 else ()))
    return outline(pts)


def eye_ring(cx, cy, rx, ry, pupil, pr=1.8):
    """Ojo redondo blanco con borde negro grueso y pupila pequeña (Hunter, Switch)."""
    return [L(ell(cx, cy, rx, ry), WHITE, 'f', False), L(ring(ell(cx, cy, rx, ry)), OUTC, 'f', False, False, 2.2),
            L(ell(cx, cy + 0.5, pr, pr), pupil, 'f', False)]


# Bigman (portero): bajito; pelo verde enorme y revuelto de pinchos hacia arriba; ojos azules grandes con raya negra gruesa
# y una sonrisa enseñando los dientes
CHARS['bigman'] = {
    'body': 'bajito', 'pal': pal('#3ca86c', '#f6c8a0', iris='#2a8ad0', shade='#2c8454', deep='#1e5c3a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 94, 'hairline': [(14, 62), (18, 50), (30, 48), (44, 54), (50, 48), (56, 54), (70, 48), (82, 50), (86, 62)]},
    'front': [L(outline([(16, 62), (6, 54, 1), (12, 44), (2, 30, 1), (12, 24), (4, 4, 1), (18, 4), (14, -16, 1), (30, -8), (32, -28, 1), (46, -14), (56, -30, 1), (62, -12),
                         (78, -22, 1), (78, -4), (94, -4, 1), (86, 12), (100, 22, 1), (88, 30), (98, 44, 1), (86, 48), (90, 60, 1), (82, 62), (80, 50), (20, 50)])),
              L(outline([(62, -12), (78, -22), (78, -4), (94, -4), (86, 12), (100, 22), (88, 30), (98, 44), (86, 48), (90, 60), (82, 60), (78, 30), (66, 10)]), 'shade', 'b', False),
              strand([(30, 0), (36, 30)], 'deep', 'b', 1.0), strand([(50, -10), (50, 24)], 'deep', 'b', 1.0), strand([(68, 0), (62, 30)], 'deep', 'b', 1.0),
              L(outline([(40, 40), (50, 36), (52, 42), (46, 58, 1)]), 'mid', 'f'),
              L(quad((27, 82), (36, 85), (45, 80)), OUTC, 'f', False, False, 2.6), L(quad((73, 82), (64, 85), (55, 80)), OUTC, 'f', False, False, 2.6),
              L([(24, 70), (29, 72)], OUTC, 'f', False, False, 2.4), L([(76, 70), (71, 72)], OUTC, 'f', False, False, 2.4)],
    'side': [L(outline([(60, 54), (68, 44), (84, 40), (98, 30, 1), (88, 22), (96, 6, 1), (80, 4), (86, -14, 1), (66, -6), (64, -28, 1), (48, -10), (34, -30, 1), (28, -8),
                        (8, -16, 1), (12, 6), (-8, 10, 1), (4, 26), (-14, 38, 1), (2, 46), (-8, 62, 1), (8, 66), (4, 80, 1), (20, 76), (32, 68), (42, 60), (52, 56)])),
             L(outline([(2, 46), (20, 34), (40, 60), (20, 76), (8, 66)]), 'shade', 'b', False),
             strand([(20, 0), (40, 20)], 'deep', 'b', 1.0), strand([(50, -6), (60, 20)], 'deep', 'b', 1.0)],
    'back': [L(outline([(18, 84), (12, 70, 1), (14, 60), (-2, 50, 1), (10, 42), (-4, 26, 1), (12, 22), (6, 2, 1), (22, 6), (20, -16, 1), (34, -4), (40, -24, 1), (50, -8),
                        (62, -26, 1), (66, -6), (82, -16, 1), (80, 4), (98, 4, 1), (88, 20), (104, 30, 1), (88, 40), (100, 54, 1), (86, 60), (88, 72, 1), (82, 84),
                        (50, 88)])),
             L(outline([(14, 50), (40, 40), (60, 44), (88, 40), (86, 82), (50, 88), (18, 82)]), 'shade', 'b', False)],
}

# Charmer (Gentleman): tupé engominado castaño oliva peinado hacia arriba y atrás, los lados cortos; ojos azules y sonrisa
# tranquila de galán
CHARS['charmer'] = {
    'body': 'normal', 'pal': pal('#8a8656', '#f8d4ac', iris='#3a5aa0', shade='#6c6840', deep='#4e4a2c', light='#aeaa7a'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 93, 'hairline': [(16, 58), (20, 38), (50, 34), (80, 38), (84, 58)]},
    'front': [L(outline([(16, 60), (14, 36), (14, 12), (22, -4), (40, -12), (62, -10), (80, -4), (90, 8), (88, 22), (82, 28), (82, 40), (84, 60), (80, 50), (20, 50)])),
              L(outline([(20, 12), (40, 6), (60, 8), (84, 14), (88, 22), (82, 28), (60, 24), (40, 24), (20, 28)]), 'shade', 'b', False),
              L(outline([(28, -4), (44, -10), (52, -4), (36, 2)]), 'light', 'b', False),
              strand([(30, -6), (34, 20)], 'deep', 'b', 0.9), strand([(50, -10), (54, 18)], 'deep', 'b', 0.9), strand([(68, -6), (72, 18)], 'deep', 'b', 0.9)],
    'side': [L(outline([(60, 46), (68, 36), (86, 32), (96, 18), (92, 2), (72, -10), (44, -12), (20, -2), (6, 22), (4, 48), (10, 64), (24, 68), (34, 58), (44, 50)])),
             L(outline([(4, 40), (40, 30), (60, 36), (34, 58), (24, 68), (10, 64)]), 'shade', 'b', False),
             strand([(20, 10), (60, 0), (90, 6)], 'deep', 'b', 0.9), strand([(14, 26), (50, 16), (86, 22)], 'deep', 'b', 0.9),
             L(outline([(40, -8), (70, -8), (60, -2)]), 'light', 'b', False)],
    'back': [L(outline([(18, 70), (14, 40), (16, 12), (30, -6), (50, -12), (72, -6), (86, 10), (86, 40), (82, 70), (50, 86, 1)])),
             L(outline([(16, 30), (50, 26), (86, 30), (82, 70), (50, 86), (18, 70)]), 'shade', 'b', False),
             strand([(30, 0), (44, 60)], 'deep', 'b', 0.9), strand([(70, 0), (56, 60)], 'deep', 'b', 0.9)],
}

# Scuba (Diver): pelo negro alborotado de mechones de punta; un pañuelo de rayas roja, amarilla y verde le rodea la frente y
# la cara hasta la mandíbula, con el lazo arriba; ojos gris azulado y ceño fruncido
RED, YEL, GRN = (196, 52, 48, 255), (236, 196, 72, 255), (42, 112, 64, 255)
CHARS['scuba'] = {
    'body': 'normal', 'pal': pal('#1c1a1c', '#f8d4ac', iris='#6a8ab4', shade='#121012', deep='#060506', light='#3a383c'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'ears': False, 'hairline': False},
    'front': [L(outline([(16, 82), (6, 60), (-2, 36, 1), (8, 30), (2, 10, 1), (10, 4), (8, -20, 1), (22, -12), (28, -30, 1), (40, -16), (50, -34, 1), (58, -16),
                         (70, -30, 1), (76, -12), (92, -20, 1), (92, 0), (104, 6, 1), (94, 18), (102, 34, 1), (92, 40), (94, 60), (84, 82)])),
              L(outline([(58, -16), (70, -30), (76, -12), (92, -20), (92, 0), (104, 6), (94, 18), (102, 34), (92, 40), (80, 20)]), 'light', 'b', False),
              L(rope((16, 88), (50, -26), (84, 88), 7), RED, 'f'), L(rope((20, 88), (50, -16), (80, 88), 6), YEL, 'f', False),
              L(rope((23, 88), (50, -6), (77, 88), 5), GRN, 'f', False),
              L(outline([(50, 30), (36, 14), (30, 22), (44, 34)]), YEL, 'f', True, True), L(outline([(50, 30), (64, 14), (70, 22), (56, 34)]), GRN, 'f', True, True),
              L(ell(50, 30, 4, 3.4), RED, 'f', False, True)],
    'side': [L(outline([(70, 44), (86, 30), (92, 14), (82, -6), (86, -22, 1), (68, -14), (62, -32, 1), (48, -14), (30, -28, 1), (24, -8), (4, -14, 1), (8, 6), (-12, 14, 1),
                        (2, 26), (-14, 40, 1), (4, 48), (-6, 64, 1), (12, 66), (14, 82), (32, 78), (44, 64)])),
             L(outline([(4, 48), (24, 40), (40, 64), (14, 82), (12, 66)]), 'light', 'b', False),
             L(rope((94, 28), (54, 50), (18, 90), 7), RED, 'f'), L(rope((92, 36), (56, 58), (22, 96), 6), YEL, 'f', False),
             L(rope((90, 44), (58, 66), (26, 100), 5), GRN, 'f', False),
             L(outline([(88, 26), (98, 12), (100, 22), (92, 32)]), YEL, 'f', True, True)],
    'back': [L(outline([(16, 84), (4, 64), (-4, 40, 1), (6, 34), (0, 12, 1), (10, 6), (8, -18, 1), (22, -10), (28, -30, 1), (40, -14), (50, -32, 1), (58, -14),
                        (70, -28, 1), (76, -10), (92, -18, 1), (92, 2), (104, 10, 1), (94, 22), (104, 38, 1), (94, 44), (96, 64), (84, 84), (50, 88)])),
             L(outline([(56, -12), (70, -28), (76, -10), (92, -18), (92, 2), (104, 10), (94, 22), (104, 38), (94, 44), (96, 64), (84, 84), (66, 60)]), 'light', 'b', False),
             L(quad((10, 70), (50, 80), (90, 70)) + quad((90, 78), (50, 88), (10, 78)), RED, 'b'),
             L(quad((12, 77), (50, 87), (88, 77)) + quad((88, 83), (50, 93), (12, 83)), YEL, 'b', False),
             L(quad((14, 83), (50, 93), (86, 83)) + quad((86, 88), (50, 98), (14, 88)), GRN, 'b', False)],
}

# Smokestack (Smokey): piel oscura; un afro grande castaño oliva, más oscuro por abajo, que le baja hasta las cejas; un globo
# de chicle rosa en la boca, ojos color ámbar y pendientes rojos
GUM = (246, 196, 196, 255)
CHARS['smokestack'] = {
    'body': 'normal', 'pal': pal('#76723a', '#8a5a3a', iris='#b0701e', shade='#4e4428', deep='#3a3020', light='#96925a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'hairline': [(14, 78), (20, 66), (32, 62), (44, 66), (50, 60), (56, 66), (68, 62), (80, 66), (86, 78)]},
    'front': [L(bumpy(50, 32, 52, 44, 13, 0.07)), L(outline([(0, 46), (30, 52), (50, 50), (70, 52), (100, 46), (98, 70), (86, 80), (14, 80), (2, 70)]), 'shade', 'b', False),
              L(outline([(60, -8), (90, 8), (100, 30), (90, 40), (78, 20)]), 'light', 'b', False),
              L(outline([(36, 58), (44, 56), (50, 62), (46, 70, 1), (42, 62)]), 'shade', 'f'),
              L(ell(50, 98, 7, 6.4), GUM, 'f', True, True), L(ell(47, 95, 2, 1.6), WHITE, 'f', False),
              L(ell(15, 82, 1.8, 2.2), (196, 40, 40, 255), 'f', False), L(ell(85, 82, 1.8, 2.2), (196, 40, 40, 255), 'f', False)],
    'side': [L(bumpy(42, 30, 54, 44, 13, 0.07)), L(outline([(-10, 40), (30, 50), (60, 54), (92, 44), (90, 66), (60, 74), (30, 80), (-6, 66)]), 'shade', 'b', False),
             L(ell(90, 97, 6, 6), GUM, 'f', True, True), L(ell(46, 86, 1.8, 2.2), (196, 40, 40, 255), 'f', False)],
    'back': [L(bumpy(50, 34, 52, 46, 13, 0.07)), L(outline([(0, 46), (50, 54), (100, 46), (98, 70), (86, 82), (50, 86), (14, 82), (2, 70)]), 'shade', 'b', False),
             L(outline([(60, -8), (90, 8), (100, 30), (90, 40), (78, 20)]), 'light', 'b', False)],
}

# Judge: melena negra larguísima y abultada que le envuelve la cabeza como una capucha hasta los hombros, con un mechón gris
# claro que le tapa un ojo y una cinta rosa que la cruza; gafas redondas negras, el ojo que se ve rojo, nariz larga y sonrisa
PINK = (226, 186, 192, 255)
CHARS['judge'] = {
    'body': 'delgado', 'pal': pal('#3a302e', '#f8d4b0', iris='#c42222', shade='#2a2220', deep='#1a1412', lock='#d8d4d8', lock_d='#aaa4ac'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'ears': False,
             'hairline': [(22, 104), (22, 62), (28, 44), (40, 36), (50, 34), (60, 36), (72, 44), (78, 62), (78, 104)]},
    'front': [L(outline([(4, 126), (0, 84), (2, 44), (10, 14), (28, -4), (50, -10), (72, -4), (90, 14), (98, 44), (100, 84), (96, 126)])),
              L(outline([(62, -6), (90, 14), (98, 44), (100, 84), (96, 124), (84, 120), (86, 60)]), 'shade', 'b', False),
              strand([(16, 30), (12, 110)], 'deep', 'b', 1.0), strand([(84, 30), (88, 110)], 'deep', 'b', 1.0),
              L(quad((8, 20), (50, -10), (92, 20)), PINK, 'b', False, False, 2.4),
              L(outline([(54, 32), (64, 30), (76, 42), (80, 70), (76, 104), (68, 100), (70, 70), (62, 46)]), 'lock', 'f'),
              L(outline([(70, 40), (78, 50), (80, 70), (76, 100), (74, 70)]), 'lock_d', 'f', False),
              L(ring(ell(36, 75, 8.4, 8.4)), OUTC, 'f', False, False, 2.2), L(ring(ell(64, 75, 8.4, 8.4)), OUTC, 'f', False, False, 2.2),
              L([(44, 74), (56, 74)], OUTC, 'f', False, False, 1.8),
              L([(50, 74), (46, 88), (52, 90)], OUTC, 'f', False, False, 1.1)],
    'side': [L(outline([(70, 40), (84, 30), (92, 16), (80, -2), (56, -10), (30, -6), (10, 10), (0, 40), (-4, 80), (-8, 124), (40, 124), (44, 100), (52, 70), (62, 50)])),
             L(outline([(-4, 60), (20, 50), (40, 90), (40, 124), (-8, 124)]), 'shade', 'b', False),
             L([(8, 14), (40, 30), (66, 40)], PINK, 'b', False, False, 2.4), L([(40, 30), (34, 80), (30, 124)], PINK, 'b', False, False, 2.4),
             L(outline([(64, 46), (72, 42), (74, 90), (68, 104), (62, 80)]), 'lock', 'f'),
             L(ring(ell(82, 75, 5, 8)), OUTC, 'f', False, False, 2.2), L([(78, 74), (60, 70)], OUTC, 'f', False, False, 1.6)],
    'back': [L(outline([(4, 126), (0, 84), (2, 44), (10, 14), (28, -4), (50, -10), (72, -4), (90, 14), (98, 44), (100, 84), (96, 126)])),
             L(outline([(56, -8), (90, 14), (98, 44), (100, 84), (96, 124), (62, 124)]), 'shade', 'b', False),
             L(quad((6, 34), (50, 18), (94, 34)), PINK, 'b', False, False, 2.4), L([(36, -6), (40, 26)], PINK, 'b', False, False, 2.4),
             L([(64, -6), (60, 26)], PINK, 'b', False, False, 2.4)],
}

# Hunter: pelo rubio pálido muy corto en punta, con el nacimiento en M que deja una frente alta; un tatuaje de rayas rojas en
# la frente, ojos blancos de pupila diminuta con borde negro grueso y una mueca apretando los dientes
CHARS['hunter'] = {
    'body': 'normal', 'pal': pal('#f2eab2', '#fcd8b0', iris='#1e1a1c', shade='#d4ca8c', deep='#b0a66a'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 95, 'hairline': [(14, 62), (18, 46), (28, 44), (32, 28), (50, 22), (68, 28), (72, 44), (82, 46), (86, 62)]},
    'front': [L(outline([(16, 64), (13, 40), (16, 16), (26, 0), (36, -6), (40, -14, 1), (46, -6), (62, -8), (70, -14, 1), (72, -4), (84, 10), (88, 30), (86, 64),
                         (80, 50), (20, 50)])),
              L(outline([(62, -8), (70, -14), (72, -4), (84, 10), (88, 30), (86, 62), (80, 40), (72, 16)]), 'shade', 'b', False),
              strand([(30, 6), (34, 12)], 'deep', 'b', 0.9), strand([(66, 4), (62, 10)], 'deep', 'b', 0.9),
              L([(40, 32), (50, 40), (60, 32)], (140, 54, 44, 255), 'f', False, False, 2.2), L([(43, 28), (50, 34), (57, 28)], (140, 54, 44, 255), 'f', False, False, 1.8),
              L([(50, 40), (50, 46)], (140, 54, 44, 255), 'f', False, False, 1.6),
              *eye_ring(36, 76, 6.4, 4.6, OUTC, 1.4), *eye_ring(64, 76, 6.4, 4.6, OUTC, 1.4),
              L([(50, 76), (48, 86), (52, 88)], (190, 140, 110, 255), 'f', False, False, 1.0)],
    'side': [L(outline([(58, 56), (64, 46), (74, 44), (78, 28), (86, 26), (84, 8), (66, -6), (54, -12, 1), (48, -6), (28, -4), (12, 8), (4, 30), (4, 56), (12, 70),
                        (24, 72), (34, 62), (46, 58)])),
             L(outline([(4, 30), (30, 26), (40, 50), (34, 62), (24, 72), (12, 70), (4, 56)]), 'shade', 'b', False),
             strand([(30, 4), (34, 10)], 'deep', 'b', 0.9),
             L(ell(80, 76, 4, 4.6), WHITE, 'f', False), L(ring(ell(80, 76, 4, 4.6)), OUTC, 'f', False, False, 2.2), L(ell(82, 76.5, 1.2, 1.2), OUTC, 'f', False)],
    'back': [L(outline([(16, 80), (12, 50), (16, 24), (30, 6), (40, -2), (46, -6, 1), (50, -2), (66, 0), (70, -4, 1), (76, 6), (86, 24), (88, 50), (84, 80), (50, 84)])),
             L(outline([(18, 56), (40, 44), (70, 34), (88, 40), (84, 78), (50, 84), (18, 78)]), 'shade', 'b', False),
             strand([(30, 20), (36, 24)], 'deep', 'b', 0.9), strand([(70, 30), (66, 36)], 'deep', 'b', 0.9)],
}

# Cobra: media melena castaña en forma de casco que le enmarca la cara hasta la mandíbula, con el flequillo en pinchos; ojos de
# serpiente grandes con sombra rosa, coloretes y una sonrisa abierta con colmillos y la lengua roja
CHARS['cobra'] = {
    'body': 'delgado', 'pal': pal('#8a5a36', '#fcdcc0', iris='#1e1a1c', shade='#6a4428', deep='#4c301c'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'none', 'hairline': [(14, 80), (20, 56), (34, 44), (50, 40), (66, 44), (80, 56), (86, 80)]},
    'front': [L(outline([(8, 98, 1), (8, 72), (2, 50), (6, 24), (20, 4), (40, -6), (60, -6), (80, 4), (94, 24), (98, 50), (92, 72), (92, 98, 1), (86, 86), (82, 70),
                         (78, 56), (22, 56), (18, 70), (14, 86)])),
              L(outline([(60, -6), (80, 4), (94, 24), (98, 50), (92, 72), (92, 96), (84, 70), (82, 36)]), 'shade', 'b', False),
              strand([(30, 0), (16, 50)], 'deep', 'b', 0.9), strand([(70, 0), (84, 50)], 'deep', 'b', 0.9),
              L(outline([(24, 48), (30, 34), (40, 30), (50, 28), (60, 30), (72, 34), (76, 48), (66, 42), (60, 52, 1), (56, 40), (50, 58, 1), (46, 40), (40, 52, 1), (34, 42)]),
                'mid', 'f'),
              L(quad((28, 70), (36, 66), (44, 70)), (226, 120, 136, 255), 'f', False, False, 2.0), L(quad((72, 70), (64, 66), (56, 70)), (226, 120, 136, 255), 'f', False, False, 2.0),
              L(ell(26, 86, 4, 2.6), BLUSH, 'f', False), L(ell(74, 86, 4, 2.6), BLUSH, 'f', False),
              L(ell(47.5, 86, 0.8, 0.8), OUTC, 'f', False), L(ell(52.5, 86, 0.8, 0.8), OUTC, 'f', False),
              L(quad((38, 90), (50, 106), (62, 90)) + [(50, 92)], (150, 40, 40, 255), 'f', False), L(ell(50, 100, 3, 2.4), (220, 90, 90, 255), 'f', False),
              L(quad((36, 89), (50, 93), (64, 89)), OUTC, 'f', False, False, 1.3),
              L([(43, 91), (45, 96), (47, 91.6)], WHITE, 'f', False), L([(53, 91.6), (55, 96), (57, 91)], WHITE, 'f', False)],
    'side': [L(outline([(60, 60), (70, 46), (86, 40), (92, 20), (78, 2), (52, -6), (26, -2), (8, 14), (0, 40), (2, 66), (12, 84), (16, 100, 1), (24, 86), (34, 74), (44, 64)])),
             L(outline([(0, 40), (20, 30), (40, 64), (24, 86), (12, 84), (2, 66)]), 'shade', 'b', False),
             L(outline([(80, 40), (92, 36), (96, 52, 1), (86, 48)]), 'mid', 'f'), L(ell(78, 86, 4, 2.6), BLUSH, 'f', False)],
    'back': [L(outline([(10, 100, 1), (10, 76), (2, 50), (6, 24), (20, 4), (40, -6), (60, -6), (80, 4), (94, 24), (98, 50), (90, 76), (90, 100, 1), (80, 84), (50, 88),
                        (20, 84)])),
             L(outline([(4, 46), (30, 54), (50, 56), (70, 54), (96, 46), (90, 76), (80, 84), (50, 88), (20, 84), (10, 76)]), 'shade', 'b', False),
             *[strand([(x, 4 + abs(x - 50) * 0.2), (x + (x - 50) * 0.2, 60)], 'deep', 'b', 0.9) for x in (30, 50, 70)]],
}

# Yoga: pelo largo ondulado castaño dorado con mechones sueltos que salen hacia los lados y dos que le caen por delante de la
# cara; cejas gruesas, ojos verdes grandes y sonrisa enseñando los dientes
CHARS['yoga'] = {
    'body': 'normal', 'pal': pal('#a68c2c', '#f8cca4', iris='#3a9a6a', shade='#846e1e', deep='#5e4e14'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 95, 'hairline': [(14, 70), (20, 52), (32, 44), (50, 40), (68, 44), (80, 52), (86, 70)]},
    'front': [L(rope((18, 14), (-16, 20), (-8, 50), 4)), L(rope((14, 46), (-10, 60), (4, 84), 4)), L(rope((20, 64), (6, 96), (24, 108), 4)),
              L(rope((82, 14), (116, 20), (108, 50), 4)), L(rope((86, 46), (110, 60), (96, 84), 4)), L(rope((80, 64), (94, 96), (76, 108), 4)),
              L(outline([(16, 72), (12, 40), (16, 14), (30, -2), (50, -6), (70, -2), (84, 14), (88, 40), (84, 72), (80, 56), (20, 56)])),
              L(outline([(62, -4), (84, 14), (88, 40), (84, 70), (80, 40), (72, 14)]), 'shade', 'b', False),
              strand([(36, 0), (30, 36)], 'deep', 'b', 1.0), strand([(64, 0), (70, 36)], 'deep', 'b', 1.0),
              L(rope((34, 44), (20, 76), (30, 106), 5), 'mid', 'f'), L(rope((66, 44), (80, 76), (70, 106), 5), 'shade', 'f')],
    'side': [L(rope((14, 30), (-18, 40), (-10, 70), 4)), L(rope((10, 56), (-12, 80), (6, 100), 4)), L(rope((24, 70), (12, 100), (30, 112), 4)),
             L(outline([(60, 56), (68, 44), (84, 40), (90, 22), (80, 4), (56, -6), (30, -4), (12, 8), (4, 30), (4, 56), (14, 72), (28, 72), (38, 62), (50, 58)])),
             L(outline([(4, 30), (18, 20), (34, 50), (28, 72), (14, 72), (4, 56)]), 'shade', 'b', False),
             L(rope((82, 40), (98, 70), (86, 106), 5), 'mid', 'f')],
    'back': [L(rope((20, 14), (-16, 22), (-8, 54), 4)), L(rope((80, 14), (116, 22), (108, 54), 4)), L(rope((20, 60), (0, 90), (16, 110), 4)),
             L(rope((80, 60), (100, 90), (84, 110), 4)),
             L(outline([(16, 86), (12, 50), (16, 18), (30, 0), (50, -6), (70, 0), (84, 18), (88, 50), (84, 86), (66, 80), (50, 92), (34, 80)])),
             L(outline([(56, -4), (84, 18), (88, 50), (84, 84), (60, 84)]), 'shade', 'b', False),
             strand([(40, 10), (36, 70)], 'deep', 'b', 1.0), strand([(60, 10), (64, 70)], 'deep', 'b', 1.0)],
}

# Mop (Shakey): pelo rubio con un moño arriba sujeto con una pinza verde, y una melena en forma de cuenco con un flequillo que le
# tapa los ojos del todo; coloretes enormes y boquita
CLIP = (140, 190, 70, 255)
CHARS['mop'] = {
    'body': 'bajito', 'pal': pal('#f2cc6a', '#fcdcc4', iris='#2a1e1a', shade='#cc9c44', deep='#a8782c', back='#b67c46'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 97, 'ears': False, 'hairline': False},
    'front': [L(ell(50, 4, 13, 14)), L(outline([(54, -6), (62, 4), (56, 14), (52, 4)]), 'shade', 'b', False),
              L(outline([(12, 88), (6, 70), (14, 48), (28, 30), (50, 24), (72, 30), (86, 48), (94, 70), (88, 88), (70, 90), (50, 92), (30, 90)]), 'mid', 'f'),
              L(outline([(66, 30), (86, 48), (94, 70), (88, 88), (76, 88), (80, 60)]), 'shade', 'f', False),
              *[L([(x, 62 + abs(x - 50) * 0.05), (x, 90)], 'deep', 'f', False, False, 0.9) for x in (30, 40, 50, 60, 70)],
              L(outline([(26, 22), (74, 22), (76, 27), (24, 27)]), CLIP, 'f', True, True), L([(20, 24), (32, 24)], CLIP, 'f', False, False, 2.2),
              L([(68, 24), (80, 24)], CLIP, 'f', False, False, 2.2),
              L(ell(28, 96, 6.4, 5.4), BLUSH, 'f', False), L(ell(72, 96, 6.4, 5.4), BLUSH, 'f', False)],
    'side': [L(ell(48, 2, 13, 14)),
             L(outline([(4, 88), (0, 62), (10, 38), (34, 24), (62, 26), (84, 40), (94, 66), (94, 90), (60, 92), (30, 92)]), 'mid', 'f'),
             L(outline([(0, 62), (14, 44), (30, 70), (30, 92), (4, 88)]), 'shade', 'f', False),
             L(outline([(28, 22), (68, 22), (70, 27), (26, 27)]), CLIP, 'f', True, True), L([(66, 24), (84, 20)], CLIP, 'f', False, False, 2.2),
             L(ell(84, 96, 5, 5), BLUSH, 'f', False)],
    'back': [L(ell(50, 4, 13, 14)), L(outline([(16, 58), (20, 36), (36, 26), (50, 24), (64, 26), (80, 36), (84, 58)])),
             L(outline([(4, 62), (-4, 56), (20, 50), (50, 56), (80, 50), (104, 56), (96, 62), (90, 86), (50, 92), (10, 86)]), 'back'),
             L(outline([(56, 54), (80, 50), (104, 56), (96, 62), (90, 86), (60, 92)]), 'deep', 'b', False),
             L(outline([(26, 22), (74, 22), (76, 27), (24, 27)]), CLIP, 'b', True, True), L([(20, 24), (32, 24)], CLIP, 'b', False, False, 2.2),
             L([(68, 24), (80, 24)], CLIP, 'b', False, False, 2.2)],
}

# Moai (Convoy): cara cuadrada como una estatua moái; pelo castaño rojizo en bloque, plano arriba con un adorno morado, que le
# cuelga a los lados en mechones gruesos hasta el cuello; ojos azul hielo rasgados, cejas rectas, nariz cuadrada y boca seria
CYAN = (184, 232, 236, 255)
PURP = (90, 70, 140, 255)
CHARS['moai'] = {
    'body': 'corpulento', 'pal': pal('#9c5c46', '#7c5238', iris='#2a1e1a', shade='#7c4634', deep='#5c3224', light='#e8b494'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': [(14, 92), (20, 60), (26, 50), (40, 46), (60, 46), (74, 50), (80, 60), (86, 92)],
             'face_front': blob([(16, 50), (50, 44), (84, 50), (88, 76), (84, 98), (66, 106), (50, 108), (34, 106), (16, 98), (12, 76)])},
    'front': [L(outline([(10, 106), (4, 96), (12, 90), (8, 70), (14, 50), (22, 40), (20, 26), (26, 14), (74, 14), (80, 26), (78, 40), (86, 50), (92, 70), (88, 90),
                         (96, 96), (90, 106), (84, 98), (80, 80), (80, 60), (20, 60), (20, 80), (16, 98)])),
              L(outline([(26, 14), (74, 14), (78, 36), (50, 40), (22, 36)]), 'light', 'b', False),
              L(outline([(80, 26), (78, 40), (86, 50), (92, 70), (88, 90), (96, 96), (90, 106), (84, 98), (84, 60)]), 'shade', 'b', False),
              strand([(12, 80), (10, 102)], 'deep', 'b', 1.0), strand([(88, 80), (90, 102)], 'deep', 'b', 1.0),
              L(quad((38, 16), (50, 32), (62, 16)), PURP, 'b', False, False, 3.0),
              L([(24, 70), (46, 72)], OUTC, 'f', False, False, 2.8), L([(76, 70), (54, 72)], OUTC, 'f', False, False, 2.8),
              L(outline([(26, 75), (44, 76), (42, 80), (28, 80)]), CYAN, 'f', False), L(ring([(26, 75), (44, 76), (42, 80), (28, 80)]), OUTC, 'f', False, False, 1.4),
              L(outline([(74, 75), (56, 76), (58, 80), (72, 80)]), CYAN, 'f', False), L(ring([(74, 75), (56, 76), (58, 80), (72, 80)]), OUTC, 'f', False, False, 1.4),
              L([(46, 80), (46, 88), (40, 88), (40, 92), (60, 92), (60, 88), (54, 88), (54, 80)], OUTC, 'f', False, False, 1.1),
              L(quad((38, 100), (50, 97), (62, 100)), OUTC, 'f', False, False, 1.8)],
    'side': [L(outline([(56, 58), (66, 52), (82, 48), (86, 30), (80, 12), (56, 8), (30, 10), (14, 18), (8, 40), (6, 66), (-8, 90), (-6, 104), (14, 100), (30, 104),
                        (40, 94), (40, 72), (48, 62)])),
             L(outline([(14, 18), (30, 10), (56, 8), (80, 12), (84, 24), (50, 24), (20, 28)]), 'light', 'b', False),
             L(outline([(6, 66), (20, 56), (36, 80), (30, 104), (14, 100), (-6, 104), (-8, 90)]), 'shade', 'b', False),
             L([(16, 14), (12, 40)], PURP, 'b', False, False, 3.0),
             L([(72, 70), (86, 72)], OUTC, 'f', False, False, 2.8), L(outline([(76, 75), (86, 76), (86, 80), (78, 80)]), CYAN, 'f', False)],
    'back': [L(outline([(12, 106), (8, 70), (14, 40), (20, 20), (30, 12), (70, 12), (80, 20), (86, 40), (92, 70), (88, 106), (76, 98), (64, 106), (50, 98), (36, 106),
                        (24, 98)])),
             L(outline([(24, 20), (76, 20), (80, 46), (50, 52), (20, 46)]), 'light', 'b', False),
             L(outline([(56, 52), (80, 46), (88, 70), (88, 106), (64, 106)]), 'shade', 'b', False),
             *[L(ell(x, 82, 2.6, 8), 'light', 'b', False) for x in (28, 40, 52, 64, 76)],
             L(outline([(38, 8), (44, 8), (46, 36, 1)]), PURP, 'b', False), L(outline([(56, 8), (62, 8), (54, 36, 1)]), PURP, 'b', False)],
}

# Hellion (Lion): una melena de león enorme de pinchos, dorada por fuera y castaña por dentro, con un mechón en pico que le baja
# por la frente hasta la nariz; ojos verde azulado, nariz ancha y ceño fruncido
CHARS['hellion'] = {
    'body': 'normal', 'pal': pal('#eab84a', '#e8b080', iris='#3a8a9a', shade='#c88c36', deep='#9a6230', inner='#a8643c', streak='#7a3420'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'nose': (50, 86, 3.6), 'ears': False, 'hairline': False},
    'front': [L(star(50, 56, 50, 58, 13, 0.24, -math.pi / 2, 3)),
              L(blob([(12, 60), (20, 20), (50, 10), (80, 20), (88, 60), (88, 92), (70, 94), (50, 90), (30, 94), (12, 92)], 6), 'inner', 'b', False),
              L(outline([(42, 30), (50, 14), (58, 30), (55, 50), (51, 80, 1), (49, 80, 1), (45, 50)]), 'inner', 'f'),
              L(outline([(46, 30), (50, 20), (54, 30), (52, 70, 1), (48, 70, 1)]), 'streak', 'f', False)],
    'side': [L(star(40, 54, 56, 60, 12, 0.24, 0.3, 4)),
             L(outline([(4, 40), (30, 30), (44, 60), (30, 96), (6, 80)]), 'inner', 'b', False),
             L(outline([(76, 34), (90, 30), (92, 60, 1), (82, 50)]), 'inner', 'f')],
    'back': [L(star(50, 56, 50, 58, 13, 0.24, -math.pi / 2, 5)),
             L(blob([(20, 40), (50, 26), (80, 40), (84, 80), (50, 100), (16, 80)], 6), 'inner', 'b', False)],
}

# Howler (Horn, portero): cara grande y ancha; melena verde larga y revuelta que se vuelve amarillenta en las puntas, con el
# flequillo en pinchos; ojos cerrados de felicidad y una sonrisa enorme enseñando todos los dientes
CHARS['howler'] = {
    'body': 'corpulento', 'pal': pal('#2e6c4c', '#fcd8b8', iris='#2a1e1a', shade='#225438', deep='#163c28', tip='#c4c066'),
    'face': {'eyes': 'closed', 'brows': True, 'mouth': 'none', 'hairline': [(14, 70), (20, 52), (32, 44), (50, 42), (68, 44), (80, 52), (86, 70)],
             'face_front': blob([(14, 52), (50, 44), (86, 52), (92, 76), (86, 100), (66, 110), (50, 112), (34, 110), (14, 100), (8, 76)])},
    'front': [L(outline([(8, 122), (-2, 98, 1), (8, 88), (-6, 72, 1), (8, 62), (2, 42, 1), (14, 34), (14, 14), (26, 2), (50, -4), (74, 2), (86, 14), (86, 34), (98, 42, 1),
                         (92, 62), (106, 72, 1), (92, 88), (102, 98, 1), (92, 122), (80, 110), (80, 70), (20, 70), (20, 110)])),
              L(outline([(-2, 98), (8, 88), (14, 90), (20, 110), (8, 122)]), 'tip', 'b', False), L(outline([(102, 98), (92, 88), (86, 90), (80, 110), (92, 122)]), 'tip', 'b', False),
              L(outline([(62, 0), (86, 14), (86, 34), (98, 42), (92, 62), (84, 50), (78, 20)]), 'shade', 'b', False),
              L(outline([(22, 52), (28, 38), (50, 32), (72, 38), (78, 52), (70, 46), (64, 56, 1), (58, 46), (50, 58, 1), (42, 46), (36, 56, 1), (30, 46)]), 'mid', 'f'),
              L(quad((26, 86), (50, 112), (74, 86)) + [(50, 88)], WHITE, 'f', False),
              L(ring(quad((26, 86), (50, 112), (74, 86)) + [(50, 88)]), OUTC, 'f', False, False, 1.6),
              L(quad((30, 92), (50, 98), (70, 92)), OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(60, 56), (68, 44), (84, 40), (90, 22), (80, 4), (56, -6), (30, -4), (12, 8), (4, 30), (-6, 50, 1), (2, 60), (-14, 80, 1), (0, 88), (-8, 112, 1),
                        (14, 106), (20, 122, 1), (30, 100), (40, 76), (50, 62)])),
             L(outline([(-14, 80), (0, 88), (-8, 112), (14, 106), (20, 122), (30, 100), (24, 92), (4, 84)]), 'tip', 'b', False),
             L(outline([(4, 30), (20, 26), (34, 60), (24, 90), (2, 60)]), 'shade', 'b', False),
             L(quad((78, 88), (86, 104), (90, 92)), OUTC, 'f', False, False, 1.6)],
    'back': [L(outline([(6, 122), (-4, 96, 1), (6, 86), (-6, 68, 1), (8, 58), (2, 38, 1), (14, 30), (16, 12), (30, 0), (50, -4), (70, 0), (84, 12), (86, 30), (98, 38, 1),
                        (92, 58), (106, 68, 1), (94, 86), (104, 96, 1), (94, 122), (76, 112), (62, 124, 1), (50, 110), (38, 124, 1), (24, 112)])),
             L(outline([(-4, 96), (6, 86), (30, 92), (50, 88), (70, 92), (94, 86), (104, 96), (94, 122), (76, 112), (62, 124), (50, 110), (38, 124), (24, 112), (6, 122)]),
               'tip', 'b', False),
             L(outline([(56, -2), (84, 12), (86, 30), (98, 38), (92, 58), (94, 84), (66, 86)]), 'shade', 'b', False)],
}

# Wizard (Magician): pelo rubio pálido largo y liso con la raya en medio, hasta más abajo de los hombros, y un mechón fino que le
# sale volando por un lado; antifaz azul con puntas a los lados, ojos castaños y una sonrisa tranquila
MASK = (58, 60, 170, 255)
CHARS['wizard'] = {
    'body': 'delgado', 'pal': pal('#f2eab8', '#fcd8b8', iris='#8a4a2a', shade='#d6ca90', deep='#b0a46a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'ears': False,
             'hairline': [(22, 100), (22, 60), (30, 42), (44, 36), (50, 40), (56, 36), (70, 42), (78, 60), (78, 100)]},
    'front': [L(rope((18, 40), (-16, 70), (-12, 112), 3.4)),
              L(outline([(14, 124), (12, 70), (14, 30), (26, 8), (42, -4), (50, -8), (58, -4), (74, 8), (86, 30), (88, 70), (86, 124), (78, 124), (78, 70), (22, 70),
                         (22, 124)])),
              L(outline([(60, -4), (74, 8), (86, 30), (88, 70), (86, 122), (80, 90), (82, 40)]), 'shade', 'b', False),
              strand([(50, -6), (50, 38)], 'deep', 'b', 1.0), strand([(36, 4), (24, 50)], 'deep', 'b', 0.9), strand([(64, 4), (76, 50)], 'deep', 'b', 0.9),
              L(outline([(14, 66), (22, 64), (36, 66), (50, 70), (64, 66), (78, 64), (86, 66), (92, 58, 1), (88, 76), (70, 84), (56, 82), (50, 78), (44, 82), (30, 84),
                         (12, 76), (8, 58, 1)]), MASK, 'f', True, True),
              *[L(outline([(cx - 6, 74), (cx + 6, 74), (cx + 5, 79), (cx - 5, 79)]), WHITE, 'f', False) for cx in (36, 64)],
              *[L(ell(cx, 76.5, 2.4, 2.6), (138, 74, 42, 255), 'f', False) for cx in (36, 64)],
              *[L([(cx - 6.4, 74), (cx + 6.4, 73.6)], OUTC, 'f', False, False, 1.8) for cx in (36, 64)]],
    'side': [L(outline([(70, 44), (84, 34), (88, 18), (76, 2), (54, -8), (30, -4), (12, 10), (2, 36), (-2, 70), (-10, 124), (40, 124), (36, 96), (44, 72), (58, 54)])),
             L(outline([(-2, 60), (16, 40), (34, 80), (36, 124), (-10, 124)]), 'shade', 'b', False),
             strand([(20, 6), (6, 60), (0, 110)], 'deep', 'b', 0.9), strand([(40, 0), (24, 60), (20, 110)], 'deep', 'b', 0.9),
             L(outline([(68, 64), (80, 64), (92, 66), (90, 82), (78, 82), (68, 76)]), MASK, 'f', True, True),
             L(outline([(76, 74), (86, 74), (86, 79), (78, 79)]), WHITE, 'f', False), L(ell(83, 76.5, 2, 2.6), (138, 74, 42, 255), 'f', False)],
    'back': [L(rope((82, 40), (116, 70), (112, 112), 3.4)),
             L(outline([(12, 126), (10, 70), (14, 30), (26, 8), (42, -4), (50, -8), (58, -4), (74, 8), (86, 30), (90, 70), (88, 126), (50, 128)])),
             L(outline([(56, -6), (74, 8), (86, 30), (90, 70), (88, 124), (60, 126)]), 'shade', 'b', False)],
}

# René Gadé (Bahart Descom, el mánager): gorra blanca de oficial de marina con cordón dorado y visera negra; el pelo rubio solo
# asoma en la nuca y las patillas; ojos rojos de mirada furiosa y un bigote amarillo en pico bajo la nariz
CAP, CAP_D, VISOR = (246, 244, 240, 255), (220, 196, 200, 255), (24, 22, 26, 255)
GOLD = (232, 182, 72, 255)
CHARS['ren-gad'] = {
    'body': 'normal', 'pal': pal('#e8a650', '#f8d4b0', iris='#c42222', shade='#c68434', deep='#9a6224'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 101, 'hairline': False},
    'front': [L(outline([(16, 52), (20, 52), (22, 70), (17, 70)]), 'mid', 'f', True, True), L(outline([(84, 52), (80, 52), (78, 70), (83, 70)]), 'mid', 'f', True, True),
              L(outline([(4, 30), (12, 14), (30, 6), (50, 4), (70, 6), (88, 14), (96, 30), (84, 44), (16, 44)]), CAP, 'f'),
              L(outline([(14, 26), (50, 20), (86, 26), (84, 40), (16, 40)]), CAP_D, 'f', False),
              L(outline([(16, 44), (84, 44), (86, 56), (70, 60), (50, 62), (30, 60), (14, 56)]), VISOR, 'f'),
              *[L(outline([(x - 3.6, 44), (x, 41.6), (x + 3.6, 44), (x, 46.4)]), GOLD, 'f', False, True) for x in range(20, 84, 7)],
              L(outline([(36, 90), (50, 83), (64, 90), (50, 98)]), (240, 200, 92, 255), 'f', True, True),
              L([(50, 76), (47, 84)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(28, 54), (46, 54), (46, 78), (30, 78)]), 'mid', 'b'),
             L(outline([(2, 22), (10, 8), (40, 2), (80, 2), (100, 10), (94, 28), (80, 40), (20, 40)]), CAP, 'f'),
             L(outline([(8, 22), (50, 18), (96, 20), (90, 34), (20, 36)]), CAP_D, 'f', False),
             L(outline([(70, 40), (86, 42), (108, 52), (88, 56), (72, 50)]), VISOR, 'f'),
             *[L(outline([(x - 3.6, 40), (x, 37.6), (x + 3.6, 40), (x, 42.4)]), GOLD, 'f', False, True) for x in range(18, 80, 7)],
             L(outline([(84, 86), (96, 90), (86, 96)]), (240, 200, 92, 255), 'f', True, True)],
    'back': [L(outline([(22, 50), (78, 50), (78, 76), (22, 76)]), 'mid'), L(outline([(54, 50), (78, 50), (78, 76), (60, 76)]), 'shade', 'b', False),
             L(outline([(4, 30), (12, 14), (30, 6), (50, 4), (70, 6), (88, 14), (96, 30), (84, 48), (16, 48)]), CAP, 'f'),
             L(outline([(12, 22), (50, 16), (88, 22), (84, 40), (16, 40)]), CAP_D, 'f', False),
             *[L(outline([(x - 3.6, 46), (x, 43.6), (x + 3.6, 46), (x, 48.4)]), GOLD, 'f', False, True) for x in range(20, 84, 7)]],
}

# Switch (Jack): una cresta de pinchos castaño oscuro hacia atrás, con un flequillo amarillo dorado echado a un lado en pinchos
# y los lados rapados gris; ojos blancos enormes de pupila roja diminuta y la boca abierta con los dientes
CHARS['switch'] = {
    'body': 'delgado', 'pal': pal('#5a3a24', '#fcd8b8', iris='#c42222', shade='#422a1a', deep='#2c1c10', grey='#b4ac94', fr='#c8a424', fr_d='#9a7c14'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'none', 'hairline': [(14, 64), (18, 46), (30, 40), (50, 40), (70, 40), (82, 46), (86, 64)]},
    'front': [L(outline([(16, 66), (12, 40), (16, 18), (84, 18), (88, 40), (84, 66), (80, 48), (20, 48)]), 'grey'),
              L(outline([(28, 22), (24, 4), (30, -24, 1), (40, -8), (48, -30, 1), (56, -10), (66, -28, 1), (70, -6), (72, 10), (70, 22)])),
              L(outline([(34, 16), (50, 6), (70, 4), (98, 0, 1), (84, 12), (106, 16, 1), (88, 24), (100, 32, 1), (84, 34), (90, 46, 1), (76, 42), (70, 58, 1), (64, 42),
                         (56, 54, 1), (52, 36), (44, 46, 1), (40, 30)]), 'fr', 'f'),
              L(outline([(70, 4), (98, 0), (84, 12), (106, 16), (88, 24), (100, 32), (84, 34), (90, 46), (76, 42), (80, 26)]), 'fr_d', 'f', False),
              *eye_ring(36, 76, 6.6, 6.2, (196, 34, 34, 255), 1.8), *eye_ring(64, 76, 6.6, 6.2, (196, 34, 34, 255), 1.8),
              L(outline([(43, 97), (57, 97), (55, 102), (45, 102)]), (50, 24, 22, 255), 'f', False),
              *[L(ell(x, 98.4, 0.9, 0.9), WHITE, 'f', False) for x in (46, 50, 54)]],
    'side': [L(outline([(60, 54), (68, 46), (82, 42), (86, 26), (76, 10), (54, 4), (30, 8), (12, 20), (4, 42), (6, 64), (16, 74), (28, 72), (36, 60), (48, 56)]), 'grey'),
             L(outline([(40, 4), (20, -8), (-6, -16, 1), (10, 0), (-16, 4, 1), (4, 14), (-12, 24, 1), (6, 30), (-4, 46, 1), (10, 46), (6, 66), (14, 84, 1), (20, 70),
                        (30, 40), (44, 20), (60, 10), (70, 0), (60, -20, 1), (52, -4), (42, -24, 1)])),
             L(outline([(70, 6), (88, 10), (100, 6, 1), (92, 20), (102, 28, 1), (88, 32), (94, 44, 1), (82, 40), (78, 24)]), 'fr', 'f')],
    'back': [L(outline([(16, 76), (12, 50), (16, 24), (30, 8), (50, 4), (70, 8), (84, 24), (88, 50), (84, 76), (60, 82), (50, 104, 1), (40, 82)]), 'grey'),
             L(outline([(30, 12), (26, -6), (32, -26, 1), (42, -10), (50, -30, 1), (58, -10), (68, -26, 1), (74, -6), (70, 12), (68, 40), (62, 70), (50, 104, 1),
                        (38, 70), (32, 40)])),
             L(outline([(52, -10), (68, -26), (74, -6), (70, 12), (66, 50), (54, 90)]), 'shade', 'b', False),
             L(outline([(18, 20), (2, 6, 1), (-8, 20, 1), (6, 24), (-6, 34, 1), (12, 34), (4, 46, 1), (18, 40)]), 'fr')],
}
