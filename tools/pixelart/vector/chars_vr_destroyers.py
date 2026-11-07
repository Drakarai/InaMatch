"""Destructores (vr-destroyers): equipo exclusivo del modo Crónica de Victory Road (Inazuma Eleven: Eiyuutachi no Victory
Road), con sus modelos 3D de la enciclopedia (英雄たちのヴィクトリーロード). Cada uno tiene una sola forma; ninguno coge por
prefijo el dibujo de otro personaje."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, longhair, outline, pal, rope, strand  # noqa: F401
from heads import mirror, quad  # noqa: F401

BLACK = (30, 28, 34, 255)
YELLOW = (232, 208, 30, 255)
WHITE = (246, 246, 246, 255)
BLUSH = (226, 120, 110, 255)


def tri(a, b, c):
    return [a, b, c]


# Galala (Garruk Vynce, portero): grandullón moreno de pelo castaño oscuro en trenzas pegadas que acaban en un mazo
# enorme y abultado detrás de la cabeza, con una cinta amarilla; ojos amarillos, marcas oscuras en las mejillas y perilla
CHARS['garruk-vynce'] = {
    'body': 'corpulento', 'pal': pal('#3a2c1e', '#a8724a', iris='#e8d02a', paint='#4a3020'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 89,
             'hairline': [(16, 66), (22, 56), (32, 54), (42, 58), (50, 64), (58, 58), (68, 54), (78, 56), (84, 66)]},
    'front': [L(bumpy(50, 40, 40, 34, 11, 0.08)), L(bumpy(15, 58, 14, 16, 5, 0.1)), L(bumpy(85, 58, 14, 16, 5, 0.1)),
              L(outline([(16, 70), (14, 44), (24, 22), (40, 12), (60, 12), (76, 22), (86, 44), (84, 70), (50, 66)]), 'mid', 'b', False),
              L(outline([(58, 14), (78, 24), (88, 46), (86, 66), (74, 46)]), 'shade', 'b', False),
              strand([(30, 56), (34, 34), (46, 16)], 'deep', 'b', 1.2), strand([(40, 58), (44, 36), (50, 16)], 'deep', 'b', 1.2),
              strand([(60, 58), (56, 36), (50, 16)], 'deep', 'b', 1.2), strand([(70, 56), (66, 34), (54, 16)], 'deep', 'b', 1.2),
              L(quad((38, 20), (50, 12), (62, 20)), YELLOW, 'b', False, False, 2.6),
              L(quad((18, 44), (20, 50), (26, 56)), YELLOW, 'f', False, False, 3.0), L(quad((82, 44), (80, 50), (74, 56)), YELLOW, 'f', False, False, 3.0),
              L(tri((18, 80), (30, 84), (22, 92)), 'paint', 'f', False), L(tri((82, 80), (70, 84), (78, 92)), 'paint', 'f', False),
              L(blob([(46, 92), (54, 92), (52, 99), (50, 101), (48, 99)], 4), 'paint', 'f', False)],
    'side': [L(bumpy(10, 46, 32, 40, 11, 0.08)),
             L(outline([(82, 50), (86, 36), (74, 18), (54, 12), (34, 18), (22, 36), (22, 60), (30, 74), (40, 72), (44, 60), (56, 56), (70, 52)])),
             L(outline([(-18, 50), (8, 40), (26, 70), (10, 84)]), 'shade', 'b', False),
             strand([(80, 40), (60, 24), (36, 26)], 'deep', 'b', 1.2), strand([(76, 48), (56, 36), (30, 40)], 'deep', 'b', 1.2),
             L([(56, 16), (84, 44)], YELLOW, 'f', False, False, 3.6),
             L(tri((70, 82), (80, 84), (72, 92)), 'paint', 'f', False),
             L(blob([(82, 92), (88, 92), (86, 100), (82, 99)], 4), 'paint', 'f', False)],
    'back': [L(bumpy(50, 46, 46, 44, 12, 0.08)), L(bumpy(14, 64, 14, 18, 5, 0.1)), L(bumpy(86, 64, 14, 18, 5, 0.1)),
             L(bumpy(50, 80, 30, 14, 7, 0.1)),
             L(outline([(56, 6), (86, 30), (94, 62), (80, 86), (66, 60)]), 'shade', 'b', False)],
}

# Xyon (Xyron Madric): grandullón curtido de pelo blanco rosado en pinchos, con un pañuelo negro atado a la frente cuyas
# puntas salen volando a los lados de la nuca; arrugas, ojos grises con sombra oscura y una trenza larga a la espalda
CHARS['xyron-madric'] = {
    'body': 'corpulento', 'pal': pal('#f0d6d4', '#d89a74', iris='#8a9ab8', shade='#d2b0b0', deep='#a88686', band='#1e1c22'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94,
             'hairline': [(12, 64), (16, 52), (30, 44), (50, 42), (70, 44), (84, 52), (88, 64)]},
    'front': [L(outline([(-4, 98, 1), (18, 84), (22, 92)]), 'band', 'b'), L(outline([(104, 98, 1), (82, 84), (78, 92)]), 'band', 'b'),
              L(outline([(14, 70), (4, 62, 1), (12, 54), (2, 42, 1), (12, 34), (8, 18, 1), (22, 18), (26, 2, 1), (38, 8), (50, -6, 1), (62, 8), (74, 2, 1),
                         (78, 18), (92, 18, 1), (88, 34), (98, 42, 1), (88, 54), (96, 62, 1), (86, 70), (50, 60)])),
              L(outline([(60, 4), (74, 4), (78, 20), (92, 20), (88, 36), (96, 44), (88, 56), (80, 40)]), 'shade', 'b', False),
              L(outline([(12, 58), (14, 36), (30, 20), (44, 16), (50, 8, 1), (56, 16), (70, 20), (86, 36), (88, 58), (80, 50), (72, 38), (50, 32), (28, 38), (20, 50)]), 'band', 'f'),
              strand([(30, 38), (34, 44)], 'deep', 'f', 1.0), strand([(42, 34), (44, 42)], 'deep', 'f', 1.0), strand([(58, 34), (56, 42)], 'deep', 'f', 1.0),
              strand([(70, 38), (66, 44)], 'deep', 'f', 1.0),
              L(quad((40, 52), (50, 56), (60, 52)), 'skin_d', 'f', False, False, 1.0), L(quad((38, 60), (50, 62), (62, 60)), 'skin_d', 'f', False, False, 1.0),
              L([(50, 80), (50, 88)], 'skin_d', 'f', False, False, 1.2),
              L(quad((26, 80), (36, 84), (44, 80)), (120, 50, 60, 255), 'f', False, False, 2.0), L(quad((74, 80), (64, 84), (56, 80)), (120, 50, 60, 255), 'f', False, False, 2.0)],
    'side': [L(outline([(36, 66), (6, 84, 1), (-26, 96, 1), (2, 88), (26, 78)]), 'band', 'b'),
             L(rope((22, 66), (10, 92), (4, 118), 7), 'mid'),
             L(outline([(70, 52), (78, 40), (88, 32), (82, 20), (90, 10, 1), (72, 8), (68, -8, 1), (54, 2), (40, -10, 1), (34, 6), (16, 4, 1), (16, 18), (2, 22, 1),
                        (8, 34), (-4, 44, 1), (8, 50), (0, 62, 1), (14, 64), (18, 76), (34, 70), (44, 60), (58, 56)])),
             L(outline([(4, 40), (28, 48), (36, 68), (16, 72)]), 'shade', 'b', False),
             L(outline([(88, 24), (92, 44), (70, 48), (50, 56), (38, 66), (28, 54), (44, 40), (66, 30)]), 'band', 'f'),
             L(quad((74, 82), (80, 84), (84, 82)), (120, 50, 60, 255), 'f', False, False, 1.6)],
    'back': [L(rope((44, 80), (40, 100), (42, 122), 6), 'mid'), L(rope((56, 80), (60, 100), (58, 122), 6), 'mid'),
             L(outline([(18, 84), (6, 74, 1), (14, 64), (2, 52, 1), (12, 42), (6, 28, 1), (20, 24), (22, 8, 1), (36, 12), (50, -2, 1), (64, 12), (78, 8, 1), (80, 24),
                        (94, 28, 1), (88, 42), (98, 52, 1), (86, 64), (94, 74, 1), (82, 84), (50, 90)])),
             L(outline([(56, 10), (78, 10), (82, 26), (94, 30), (88, 44), (96, 54), (86, 66), (90, 78), (70, 60)]), 'shade', 'b', False),
             L(outline([(-12, 84, 1), (20, 78), (50, 82), (80, 78), (112, 84, 1), (80, 90), (50, 90), (20, 90)]), 'band', 'f'),
             L(ell(50, 86, 5, 4), 'band', 'f')],
}

# Arden (Arden Drax): pelo gris verdoso con un flequillo en punta sobre la frente y un moño alto atado con una cinta
# amarilla del que salen dos mechones rizados como antenas; dos trenzas verde lima largas a los lados de la cara; sonrisa
BRAID = (184, 184, 48, 255)
CHARS['arden-drax'] = {
    'body': 'normal', 'pal': pal('#6a6e60', '#f6c8a0', iris='#3a2a3a', braid=BRAID),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 92,
             'hairline': [(14, 60), (18, 48), (30, 44), (42, 48), (50, 58), (58, 48), (70, 44), (82, 48), (86, 60)]},
    'front': [L(rope((44, 8), (6, -12), (8, 36), 7)),
              L(outline([(14, 62), (12, 36), (22, 16), (40, 6), (60, 6), (78, 16), (88, 36), (86, 62), (50, 56)])),
              L(outline([(58, 8), (78, 18), (88, 40), (86, 60), (74, 42)]), 'shade', 'b', False),
              strand([(32, 14), (40, 30), (48, 50)], 'deep', 'b', 1.0), strand([(68, 14), (60, 30), (52, 50)], 'deep', 'b', 1.0),
              L(rope((18, 46), (12, 76), (22, 106), 6), 'braid', 'f'), L(rope((84, 46), (90, 80), (82, 112), 6), 'braid', 'f'),
              L(quad((26, 76), (34, 80), (44, 78)), (170, 70, 80, 255), 'f', False, False, 1.6), L(quad((74, 76), (66, 80), (56, 78)), (170, 70, 80, 255), 'f', False, False, 1.6)],
    'side': [L(rope((24, 14), (10, -20), (-4, -8), 6)), L(rope((16, 24), (-12, 18), (-6, 44), 6)),
             L(outline([(58, 56), (66, 46), (82, 50, 1), (86, 36), (78, 18), (56, 8), (32, 12), (18, 28), (16, 50), (24, 66), (40, 62), (48, 54)])),
             L(outline([(18, 32), (40, 36), (44, 60), (26, 64)]), 'shade', 'b', False),
             L(ell(20, 20, 7, 6), BRAID, 'b'),
             L(rope((40, 42), (36, 80), (54, 112), 6), 'braid', 'f')],
    'back': [L(rope((54, 16), (70, -18), (88, -6), 6)), L(rope((58, 22), (104, 14), (100, 46), 6)),
             L(outline([(18, 74), (14, 44), (24, 20), (50, 10), (76, 20), (86, 44), (82, 74), (50, 80)])),
             L(outline([(56, 14), (76, 22), (86, 46), (80, 72), (64, 76)]), 'shade', 'b', False),
             L(ell(52, 22, 9, 7), 'mid'), L(ell(52, 26, 6, 4), BRAID, 'b'),
             L(rope((20, 50), (18, 80), (24, 104), 6), 'braid', 'f'), L(rope((80, 50), (84, 80), (76, 104), 6), 'braid', 'f')],
}

# Simi (Simen Thorne): piel morena y una melena negra azulada enorme y abultada, con raya en medio, que se ensancha hacia
# abajo como una campana; detrás le cuelgan trencitas con cuentas blancas; pendientes oscuros y mejillas sonrosadas
CHARS['simen-thorne'] = {
    'body': 'normal', 'pal': pal('#2c2c3e', '#b07a52', iris='#3a3a5a'),
    'face': {'eyes': 'normal', 'mouth': 'line', 'mouth_y': 92,
             'hairline': [(16, 72), (20, 54), (34, 44), (50, 46), (66, 44), (80, 54), (84, 72)]},
    'front': [L(bumpy(10, 74, 16, 20, 6, 0.1)), L(bumpy(90, 74, 16, 20, 6, 0.1)),
              L(outline([(14, 96), (2, 80), (6, 56), (14, 30), (32, 12), (50, 8), (68, 12), (86, 30), (94, 56), (98, 80), (86, 96), (80, 70), (20, 70)])),
              L(outline([(58, 10), (82, 26), (94, 58), (96, 82), (84, 76), (78, 44)]), 'shade', 'b', False),
              strand([(50, 10), (48, 30)], 'deep', 'b', 1.2), strand([(46, 30), (30, 40), (20, 56)], 'deep', 'b', 1.0), strand([(52, 30), (70, 40), (80, 56)], 'deep', 'b', 1.0),
              L(ell(16, 86, 2.2, 3.4), BLACK, 'f', False), L(ell(84, 86, 2.2, 3.4), BLACK, 'f', False),
              L(ell(32, 86, 4, 2.2), BLUSH, 'f', False), L(ell(68, 86, 4, 2.2), BLUSH, 'f', False)],
    'side': [L(rope((24, 88), (22, 100), (18, 110), 4)), L(rope((32, 88), (32, 100), (30, 112), 4)),
             L(ell(18, 108, 2.4, 2.4), WHITE, 'f', ln=True), L(ell(30, 110, 2.4, 2.4), WHITE, 'f', ln=True),
             L(bumpy(10, 62, 24, 28, 8, 0.1)),
             L(outline([(70, 52), (80, 46), (86, 32), (76, 14), (54, 6), (32, 10), (16, 24), (8, 46), (14, 70), (30, 88), (44, 82), (46, 62), (58, 56)])),
             L(outline([(-12, 50), (16, 44), (34, 70), (24, 86), (0, 80)]), 'shade', 'b', False),
             L(ell(46, 82, 2.0, 3.0), BLACK, 'f', False)],
    'back': [L(rope((36, 88), (34, 100), (32, 110), 4)), L(rope((50, 90), (50, 102), (50, 112), 4)), L(rope((64, 88), (66, 100), (68, 110), 4)),
             L(bumpy(8, 74, 18, 22, 6, 0.1)), L(bumpy(92, 74, 18, 22, 6, 0.1)),
             L(outline([(12, 96), (0, 78), (6, 52), (16, 26), (34, 10), (50, 6), (66, 10), (84, 26), (94, 52), (100, 78), (88, 96), (50, 92)])),
             L(outline([(58, 10), (84, 28), (96, 60), (96, 86), (70, 90)]), 'shade', 'b', False),
             L(ell(32, 110, 2.4, 2.4), WHITE, 'f', ln=True), L(ell(50, 112, 2.4, 2.4), WHITE, 'f', ln=True), L(ell(68, 110, 2.4, 2.4), WHITE, 'f', ln=True)],
}

# Denebola (Denowar Krell): pelo gris azulado en pinchos grandes que salen hacia arriba y a los lados (por debajo, gris
# oscuro), con un pico estrecho que le baja por la frente y patillas hasta la mandíbula; ojos verdes y media sonrisa
CHARS['denowar-krell'] = {
    'body': 'normal', 'pal': pal('#8aa4c8', '#f8ccaa', iris='#3a9a4a', shade='#6c7690', deep='#4c5468', light='#c4d4ec'),
    'face': {'eyes': 'sharp', 'mouth': 'smile', 'mouth_y': 92,
             'hairline': [(14, 82), (18, 60), (30, 50), (44, 52), (50, 64), (56, 52), (70, 50), (82, 60), (86, 82)]},
    'front': [L(outline([(16, 82), (8, 66), (-2, 58, 1), (8, 48), (-8, 38, 1), (6, 30), (-10, 12, 1), (10, 14), (4, -20, 1), (30, 0), (50, -4), (70, 0), (96, -20, 1),
                         (90, 14), (110, 12, 1), (94, 30), (108, 38, 1), (92, 48), (102, 58, 1), (92, 66), (84, 82), (82, 60), (18, 60)])),
              L(outline([(10, 48), (22, 52), (18, 80), (8, 66)]), 'shade', 'b', False), L(outline([(90, 48), (78, 52), (82, 80), (92, 66)]), 'shade', 'b', False),
              L(outline([(60, 2), (92, -14), (86, 16), (102, 18), (90, 32), (80, 40)]), 'shade', 'b', False),
              L(ell(34, 22, 9, 4), 'light', 'b', False), strand([(38, 14), (44, 12)], 'deep', 'b', 1.0), strand([(56, 12), (62, 14)], 'deep', 'b', 1.0)],
    'side': [L(outline([(72, 54), (82, 46), (90, 30), (86, 14), (66, 2), (48, -2), (24, -34, 1), (20, -2), (6, 4, 1), (12, 18), (-2, 26, 1), (12, 34), (2, 46, 1),
                        (14, 54), (20, 70), (30, 84, 1), (40, 76), (46, 60), (58, 58), (66, 66, 1)])),
             L(outline([(4, 30), (30, 36), (42, 60), (34, 80), (18, 66)]), 'shade', 'b', False),
             L(ell(66, 16, 10, 4), 'light', 'b', False)],
    'back': [L(outline([(26, 84), (14, 70), (4, 64, 1), (10, 56), (-6, 46, 1), (8, 40), (-10, 22, 1), (10, 20), (4, -22, 1), (30, 2), (50, 0), (70, 2), (96, -22, 1),
                        (90, 20), (110, 22, 1), (92, 40), (106, 46, 1), (90, 56), (96, 64, 1), (86, 70), (74, 84), (60, 86), (50, 96, 1), (40, 86)])),
             L(outline([(8, 44), (92, 44), (86, 70), (74, 84), (50, 94), (26, 84), (14, 70)]), 'shade', 'b', False)],
}

# Priss (Prisca Grav): piel morena, media melena morada con flequillo, dos moños enroscados como cuernos de carnero a los
# lados de la cabeza (con un cuernecillo blanco que asoma) y dos coletas cortas enroscadas abajo; ojos amarillos y sonrisa
HORN = (240, 236, 228, 255)
CHARS['prisca-grav'] = {
    'body': 'chica', 'pal': pal('#8a5ac8', '#a86c48', iris='#c8d030', shade='#6a44a0', deep='#4e3278'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 93,
             'hairline': [(16, 72), (20, 56), (30, 62), (36, 52), (44, 62), (50, 52), (58, 62), (66, 52), (74, 60), (80, 56), (84, 72)]},
    'front': [L(rope((24, 34), (-12, 0), (6, 44), 12)), L(rope((76, 34), (112, 0), (94, 44), 12)),
              L(rope((20, 84), (0, 92), (20, 104), 9)), L(rope((80, 84), (100, 92), (80, 104), 9)),
              L(outline([(16, 86), (10, 60), (14, 34), (30, 14), (50, 8), (70, 14), (86, 34), (90, 60), (84, 86), (80, 66), (20, 66)])),
              L(outline([(60, 10), (82, 26), (90, 56), (84, 82), (78, 50)]), 'shade', 'b', False),
              L(outline([(26, 26), (32, 14, 1), (36, 26)]), HORN, 'b', True), L(outline([(64, 26), (68, 14, 1), (74, 26)]), HORN, 'b', True),
              strand([(48, 14), (40, 40), (36, 52)], 'deep', 'b', 1.0), strand([(56, 18), (62, 40), (66, 52)], 'deep', 'b', 1.0)],
    'side': [L(rope((34, 82), (10, 88), (16, 108), 9)),
             L(outline([(62, 56), (72, 52), (84, 54), (88, 36), (78, 14), (56, 4), (32, 8), (14, 26), (10, 52), (20, 78), (34, 84), (44, 70), (46, 58)])),
             L(outline([(10, 34), (34, 36), (42, 66), (28, 80), (14, 64)]), 'shade', 'b', False),
             L(rope((50, 26), (64, -12), (78, 30), 12)), L(outline([(54, 20), (58, 6, 1), (64, 18)]), HORN, 'b', True)],
    'back': [L(rope((24, 30), (-12, -2), (6, 46), 12)), L(rope((76, 30), (112, -2), (94, 46), 12)),
             L(outline([(16, 84), (10, 56), (14, 30), (30, 12), (50, 6), (70, 12), (86, 30), (90, 56), (84, 84), (50, 90)])),
             L(outline([(56, 10), (82, 26), (90, 56), (84, 82), (62, 86)]), 'shade', 'b', False),
             strand([(50, 8), (50, 48)], OUTC, 'b', 1.0),
             L(rope((36, 80), (14, 84), (22, 104), 9)), L(rope((64, 80), (86, 84), (78, 104), 9))],
}

# Grenier (Grenadier Deton): melena corta hasta la mandíbula partida en dos colores: azul marino oscuro a un lado y blanco
# plateado al otro (el lado izquierdo de él, a la derecha de la imagen), con raya y un mechón blanco que cruza la frente
GHAIR_W = (228, 232, 238, 255)
GHAIR_WS = (190, 192, 204, 255)
CHARS['grenadier-deton'] = {
    'body': 'normal', 'pal': pal('#1c2c44', '#fad2b2', iris='#8a3a3a', shade='#14203a', deep='#0c1424'),
    'face': {'eyes': 'normal', 'mouth': 'line', 'mouth_y': 92,
             'hairline': [(16, 90), (20, 60), (30, 46), (42, 40), (54, 44), (66, 52), (78, 62), (84, 90)]},
    'front': [L(outline([(18, 98), (12, 80), (8, 54), (16, 26), (34, 6), (50, 2), (66, 6), (84, 24), (94, 50), (92, 78), (84, 92), (82, 62), (20, 62)])),
              L(outline([(44, 4), (50, 2), (66, 6), (84, 24), (94, 50), (92, 78), (84, 92), (80, 74), (74, 56), (60, 46), (46, 40), (40, 26)]), GHAIR_W, 'b', False),
              L(outline([(70, 30), (88, 40), (92, 70), (86, 88), (82, 66)]), GHAIR_WS, 'b', False),
              strand([(46, 6), (48, 28), (58, 44)], 'deep', 'b', 1.0)],
    'side': [L(outline([(58, 62), (66, 56), (80, 52), (90, 38), (86, 14), (66, 0), (40, -2), (16, 10), (2, 34), (2, 60), (12, 84), (32, 96), (46, 90), (50, 72)])),
             L(outline([(76, 2), (88, 14), (92, 38), (84, 52), (82, 30)]), GHAIR_W, 'b', False),
             L(outline([(4, 40), (30, 44), (44, 70), (40, 90), (16, 80)]), 'shade', 'b', False)],
    'back': [L(outline([(18, 96), (10, 74), (8, 48), (16, 22), (34, 4), (50, 0), (66, 4), (84, 22), (92, 48), (90, 74), (82, 96), (64, 90), (50, 88), (36, 90)])),
             L(outline([(8, 48), (16, 22), (22, 14), (16, 50), (14, 80), (18, 96), (10, 74)]), GHAIR_W, 'b', False),
             L(outline([(58, 6), (82, 22), (90, 50), (84, 90), (66, 88)]), 'shade', 'b', False)],
}

# Declan (Declan Jaxor): pelo castaño muy oscuro con un moño alto en punta, y un visor blanco que le rodea la cabeza y le
# tapa el ojo izquierdo con una lente azul; el otro ojo grande y oscuro, mejillas sonrosadas, cara seria
VISOR = (228, 228, 232, 255)
LENS = (40, 150, 230, 255)
CHARS['declan-jaxor'] = {
    'body': 'normal', 'pal': pal('#3a3236', '#fad2b2', iris='#2a2226', shade='#2c2428', deep='#1c1618'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'eye_y': 77,
             'hairline': [(16, 74), (20, 60), (32, 56), (42, 64), (50, 58), (60, 54), (72, 56), (82, 62), (84, 74)]},
    'front': [L(outline([(24, 22), (20, 0), (32, -14), (50, -16), (62, -30, 1), (70, -10), (76, 4), (76, 22)])),
              L(outline([(16, 78), (12, 54), (18, 30), (34, 14), (50, 10), (66, 14), (82, 30), (88, 54), (84, 78), (80, 62), (20, 62)])),
              L(outline([(60, 12), (82, 30), (88, 54), (82, 74), (76, 46)]), 'shade', 'b', False),
              L(outline([(14, 40), (24, 30), (40, 26), (30, 36), (18, 48)]), VISOR, 'f'),
              L(outline([(50, 66), (62, 64), (80, 68), (92, 70), (86, 82), (70, 86), (54, 84), (48, 76)]), VISOR, 'f'),
              L(ell(64, 76, 5, 5), LENS, 'f', ln=True), L(ell(62, 74, 1.6, 1.6), WHITE, 'f', False),
              L(ell(30, 86, 4, 2.2), BLUSH, 'f', False)],
    'side': [L(outline([(36, 20), (14, -16), (-12, -22, 1), (-6, -4), (12, 16), (24, 28)])),
             L(outline([(66, 58), (76, 52), (88, 50), (90, 30), (80, 12), (58, 4), (34, 8), (14, 24), (8, 50), (14, 74), (24, 90, 1), (36, 80), (46, 66), (56, 60)])),
             L(outline([(8, 40), (30, 44), (40, 66), (24, 84), (12, 66)]), 'shade', 'b', False),
             L(outline([(16, 28), (40, 16), (66, 22), (86, 40), (90, 74), (82, 80), (78, 56), (62, 38), (40, 32), (20, 40)]), VISOR, 'f'),
             L(strand([(30, 26), (52, 24)], OUTC, 'f', 2.0)['s'], OUTC, 'f', False, False, 2.0),
             L(ell(84, 88, 3.4, 2.0), BLUSH, 'f', False)],
    'back': [L(outline([(30, 30), (28, -14), (46, -24), (62, -20), (70, -32, 1), (72, -6), (70, 30)])),
             L(outline([(18, 80), (12, 54), (18, 28), (34, 14), (50, 10), (66, 14), (82, 28), (88, 54), (84, 80), (66, 90), (50, 92), (34, 90)])),
             L(outline([(60, 14), (82, 30), (88, 54), (82, 80), (66, 86)]), 'shade', 'b', False),
             L(outline([(12, 48), (30, 40), (50, 38), (70, 40), (90, 48), (90, 62), (70, 56), (50, 56), (30, 56), (12, 62)]), VISOR, 'f'),
             L(strand([(56, 46), (76, 44)], OUTC, 'f', 2.0)['s'], OUTC, 'f', False, False, 2.0)],
}

# Nebula (Nebula Raime): melena negra verdosa muy abultada hasta la mandíbula, con las puntas hacia fuera teñidas de
# magenta; flequillo largo en punta que le baja hasta entre los ojos (rosa magenta con el centro turquesa); sonrisa
MAGENTA = (168, 30, 120, 255)
CHARS['nebula-raime'] = {
    'body': 'chica', 'pal': pal('#1e3236', '#fcdcc8', iris='#b02a7a', shade='#152428', deep='#0a1416'),
    'face': {'eyes': 'big', 'mouth': 'smile', 'mouth_y': 92, 'ears': False,
             'hairline': [(14, 88), (18, 66), (26, 58), (38, 62), (50, 72), (60, 62), (72, 58), (82, 66), (86, 88)]},
    'front': [L(outline([(2, 98, 1), (14, 88), (24, 96), (20, 104)]), MAGENTA), L(outline([(98, 98, 1), (86, 88), (76, 96), (80, 104)]), MAGENTA),
              L(outline([(16, 92), (8, 70), (6, 40), (16, 14), (34, 0), (50, -4), (66, 0), (84, 14), (94, 40), (92, 70), (84, 92), (82, 66), (18, 66)])),
              L(outline([(60, 0), (84, 16), (94, 44), (90, 76), (82, 50)]), 'shade', 'b', False),
              strand([(36, 4), (30, 30), (22, 52)], 'deep', 'b', 1.0), strand([(52, 0), (48, 30), (50, 60)], 'deep', 'b', 1.0), strand([(64, 4), (72, 30), (78, 50)], 'deep', 'b', 1.0),
              L(ell(36, 76, 1.6, 2.6), (40, 190, 190, 255), 'f', False), L(ell(64, 76, 1.6, 2.6), (40, 190, 190, 255), 'f', False)],
    'side': [L(outline([(36, 92), (14, 102, 1), (20, 94), (34, 88)]), MAGENTA),
             L(outline([(64, 60), (74, 56), (88, 54), (92, 36), (84, 12), (62, -2), (36, -2), (14, 10), (2, 36), (2, 66), (10, 86), (26, 96), (40, 92), (46, 76), (52, 64)])),
             L(outline([(4, 40), (32, 44), (44, 74), (32, 92), (12, 82)]), 'shade', 'b', False),
             L(outline([(70, 56), (84, 54), (90, 64), (84, 70, 1), (76, 62)]), 'mid', 'f')],
    'back': [L(outline([(2, 96, 1), (14, 84), (26, 92), (20, 102)]), MAGENTA), L(outline([(98, 96, 1), (86, 84), (74, 92), (80, 102)]), MAGENTA),
             L(outline([(16, 90), (8, 68), (6, 40), (16, 14), (34, 0), (50, -4), (66, 0), (84, 14), (94, 40), (92, 68), (84, 90), (64, 96), (50, 106, 1), (36, 96)])),
             L(outline([(58, 0), (84, 16), (94, 44), (88, 86), (64, 92)]), 'shade', 'b', False)],
}

# Kinis (Keines Elvain, capitán): piel morena, pelo blanco que pasa a rosa en las puntas, peinado hacia arriba en una
# ola alta que acaba en punta y cae por un lado en un mechón curvo; por detrás una melena lisa hasta los hombros; ojos
# rojos afilados y media sonrisa
KPINK = (226, 160, 184, 255)
CHARS['keines-elvain'] = {
    'body': 'normal', 'pal': pal('#eceaf0', '#9a6a48', iris='#c02040', shade='#d0c4cc', deep='#a898a4'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'ear_out': 2,
             'hairline': [(14, 66), (18, 54), (30, 48), (50, 46), (70, 48), (82, 54), (86, 66)]},
    'front': [L(outline([(8, 118, 1), (6, 84), (12, 58), (20, 60), (22, 90), (20, 118, 1)]), KPINK), L(outline([(92, 118, 1), (94, 84), (88, 58), (80, 60), (78, 90), (80, 118, 1)]), KPINK),
              L(outline([(14, 62), (12, 44), (18, 24), (30, 10), (38, -8, 1), (46, 6), (62, 12), (80, 22), (92, 40), (94, 60), (88, 78, 1), (84, 58), (72, 42), (50, 50), (24, 52)])),
              L(outline([(46, 8), (64, 14), (82, 26), (92, 46), (88, 72), (82, 50), (66, 34)]), 'shade', 'b', False),
              strand([(36, 0), (36, 20), (30, 42)], 'deep', 'b', 1.0), strand([(50, 12), (66, 28), (84, 56)], 'deep', 'b', 1.0)],
    'side': [L(outline([(40, 72), (26, 120, 1), (8, 116), (0, 80), (6, 50)]), KPINK),
             L(outline([(54, 54), (62, 46), (74, 40), (86, 30), (88, 10), (76, -10, 1), (66, 6), (50, 2), (30, 8), (14, 24), (8, 50), (20, 64), (36, 56), (46, 52)])),
             L(outline([(70, 6), (78, -6), (86, 12), (84, 30), (74, 24)]), 'shade', 'b', False),
             L(outline([(10, 30), (34, 36), (40, 54), (16, 60)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 70), (10, 116, 1), (30, 106), (50, 118, 1), (70, 106), (90, 116, 1), (86, 70)]), KPINK),
             L(outline([(16, 80), (12, 50), (18, 24), (34, 10), (44, -6, 1), (52, 8), (70, 14), (84, 28), (88, 50), (84, 80), (50, 86)])),
             L(outline([(56, 10), (80, 24), (88, 50), (84, 80), (62, 84)]), 'shade', 'b', False)],
}

# Vector (Vector Vernam): pelo granate en pinchos revueltos solo arriba, con los lados y la nuca rapados en negro; un
# mechón rojo fino le baja por la frente hasta la ceja; cejas gruesas arqueadas, párpados caídos, ojos azul claro y
# sonrisa enorme enseñando los dientes
UNDER = (38, 34, 38, 255)
CHARS['vector-vernam'] = {
    'body': 'normal', 'pal': pal('#8a1a14', '#f8ccaa', iris='#9ac8e8', shade='#6a120e', deep='#4a0c0a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 93, 'big_ears': 1,
             'hairline': [(14, 66), (16, 46), (24, 36), (50, 34), (76, 36), (84, 46), (86, 66)]},
    'front': [L(outline([(16, 70), (14, 40), (24, 26), (76, 26), (86, 40), (84, 70), (78, 50), (22, 50)]), UNDER),
              L(outline([(14, 36), (0, 30, 1), (8, 20), (-4, 6, 1), (10, 4), (6, -14, 1), (22, -6), (28, -22, 1), (40, -10), (50, -24, 1), (60, -10), (72, -22, 1),
                         (78, -6), (94, -14, 1), (90, 4), (104, 6, 1), (92, 20), (100, 30, 1), (86, 36), (70, 30), (50, 34), (30, 30)])),
              L(outline([(56, -8), (72, -18), (78, -4), (92, -8), (88, 8), (98, 10), (88, 24), (78, 30)]), 'shade', 'b', False),
              L(quad((56, 30), (50, 50), (42, 66)), 'mid', 'f', False, False, 2.4),
              L(quad((24, 68), (34, 64), (44, 70)), 'skin_d', 'f', False, False, 1.6), L(quad((76, 68), (66, 64), (56, 70)), 'skin_d', 'f', False, False, 1.6)],
    'side': [L(outline([(70, 46), (74, 34), (60, 26), (30, 26), (14, 40), (12, 70), (30, 82), (40, 70), (44, 56), (56, 50)]), UNDER),
             L(outline([(84, 38), (98, 30, 1), (88, 22), (96, 8, 1), (84, 6), (86, -12, 1), (70, -6), (62, -22, 1), (52, -8), (36, -20, 1), (32, -4), (14, -12, 1),
                        (16, 6), (0, 10, 1), (8, 20), (-2, 30, 1), (12, 34), (34, 30), (60, 30), (74, 34)])),
             L(outline([(0, 20), (30, 26), (40, 30), (12, 34)]), 'shade', 'b', False),
             L(quad((86, 36), (90, 50), (86, 64)), 'mid', 'f', False, False, 2.0)],
    'back': [L(outline([(18, 76), (14, 44), (22, 26), (78, 26), (86, 44), (82, 76), (64, 88), (36, 88)]), UNDER),
             L(outline([(14, 40), (0, 32, 1), (8, 22), (-4, 8, 1), (10, 6), (6, -12, 1), (22, -4), (28, -20, 1), (40, -8), (50, -22, 1), (60, -8), (72, -20, 1),
                        (78, -4), (94, -12, 1), (90, 6), (104, 8, 1), (92, 22), (100, 32, 1), (86, 40), (70, 34), (50, 38), (30, 34)])),
             L(outline([(54, -6), (72, -16), (78, -2), (92, -6), (88, 10), (98, 12), (88, 26), (76, 32)]), 'shade', 'b', False)],
}

# Zippy (Zyphar Doar): pelo rosa en forma de casco (corte de tazón) con mechones rectos, flequillo recto y un mechón más
# largo que le tapa el ojo izquierdo (a la derecha de la imagen); ojo azul y cara seria
CHARS['zyphar-doar'] = {
    'body': 'normal', 'pal': pal('#f0a0a0', '#f2c49c', iris='#4a8ac8', shade='#d08080', deep='#9a5050'),
    'face': {'eyes': 'normal', 'mouth': 'frown', 'mouth_y': 94,
             'hairline': [(14, 84), (16, 64), (30, 64), (50, 64), (70, 64), (84, 64), (86, 84)]},
    'front': [L(outline([(12, 90), (4, 66), (6, 36), (20, 12), (40, 2), (60, 2), (80, 12), (94, 36), (96, 66), (88, 90), (84, 72), (16, 72)])),
              L(outline([(60, 4), (82, 16), (94, 40), (94, 66), (86, 86), (80, 60)]), 'shade', 'b', False),
              L(outline([(48, 60), (86, 60), (86, 90), (70, 96, 1), (52, 92), (50, 76)]), 'mid', 'f'),
              L(outline([(70, 64), (84, 62), (84, 88), (72, 92)]), 'shade', 'f', False),
              strand([(26, 20), (22, 62)], 'deep', 'b', 1.0), strand([(40, 12), (38, 62)], 'deep', 'b', 1.0), strand([(62, 12), (64, 90)], 'deep', 'f', 1.0),
              strand([(76, 20), (78, 88)], 'deep', 'f', 1.0)],
    'side': [L(outline([(66, 66), (78, 62), (90, 62), (92, 36), (80, 12), (56, 2), (30, 6), (12, 22), (2, 48), (4, 74), (14, 90), (30, 92), (40, 76), (48, 68)])),
             L(outline([(4, 50), (34, 54), (44, 70), (32, 90), (12, 84)]), 'shade', 'b', False),
             strand([(70, 10), (74, 62)], 'deep', 'b', 1.0), strand([(30, 12), (20, 88)], 'deep', 'b', 1.0), strand([(50, 6), (50, 60)], 'deep', 'b', 1.0)],
    'back': [L(outline([(12, 88), (4, 64), (6, 34), (20, 12), (40, 2), (60, 2), (80, 12), (94, 34), (96, 64), (88, 88), (70, 94), (50, 96), (30, 94)])),
             L(outline([(58, 4), (82, 16), (94, 40), (90, 86), (60, 92)]), 'shade', 'b', False),
             strand([(28, 18), (24, 90)], 'deep', 'b', 1.0), strand([(42, 8), (40, 94)], 'deep', 'b', 1.0), strand([(58, 8), (60, 94)], 'deep', 'b', 1.0),
             strand([(72, 18), (76, 90)], 'deep', 'b', 1.0)],
}

# Machina (Machina Dex): media melena castaño claro hasta la mandíbula con las puntas desfiladas; un mechón negro le cruza
# la frente en diagonal y le pasa bajo el ojo izquierdo, y dos horquillas plateadas a los lados; ojos verdes, serio
CLIP = (170, 190, 200, 255)
CHARS['machina-dex'] = {
    'body': 'normal', 'pal': pal('#b09a62', '#fad6b8', iris='#5a8a50', shade='#8a7448', deep='#5a4a2e'),
    'face': {'eyes': 'normal', 'mouth': 'line', 'mouth_y': 93, 'ears': False,
             'hairline': [(14, 92), (16, 70), (26, 66), (40, 64), (54, 66), (70, 64), (84, 70), (86, 92)]},
    'front': [L(outline([(18, 100, 1), (10, 82), (6, 56), (12, 30), (28, 10), (50, 4), (72, 10), (88, 30), (94, 56), (90, 82), (82, 100, 1), (82, 70), (18, 70)])),
              L(outline([(60, 6), (84, 24), (94, 56), (88, 90), (82, 64)]), 'shade', 'b', False),
              L(quad((40, 14), (64, 40), (80, 70)), BLACK, 'f', False, False, 4.6), L(quad((80, 70), (72, 84), (56, 82)), BLACK, 'f', False, False, 3.0),
              strand([(30, 16), (26, 40), (20, 64)], 'deep', 'b', 1.0), strand([(50, 6), (46, 34), (42, 64)], 'deep', 'b', 1.0),
              L(ell(20, 68, 2.6, 2.6), CLIP, 'f', ln=True), L(ell(80, 68, 2.6, 2.6), CLIP, 'f', ln=True)],
    'side': [L(outline([(60, 62), (70, 60), (84, 58), (90, 40), (82, 16), (60, 2), (34, 2), (12, 16), (2, 42), (4, 70), (16, 92), (30, 98, 1), (38, 84), (46, 76), (52, 66)])),
             L(outline([(4, 44), (32, 48), (40, 70), (26, 92), (10, 78)]), 'shade', 'b', False),
             L(quad((74, 6), (86, 22), (90, 40)), BLACK, 'b', False, False, 3.0),
             L(ell(62, 66, 2.6, 2.6), CLIP, 'f', ln=True)],
    'back': [L(outline([(18, 100, 1), (10, 80), (6, 54), (12, 28), (28, 8), (50, 2), (72, 8), (88, 28), (94, 54), (90, 80), (82, 100, 1), (72, 94), (64, 100, 1),
                        (56, 92), (44, 92), (36, 100, 1), (28, 94)])),
             L(outline([(56, 6), (82, 22), (92, 54), (86, 92), (62, 92)]), 'shade', 'b', False)],
}

# Luol (Rourik Bhatt): pelo morado arriba, peinado hacia atrás con dos picos, y lila por debajo; dos mechones lila curvos
# le caen desde el centro de la frente y le enmarcan los ojos hasta las mejillas; por detrás la nuca en pico; ojos grises
LILAC = (204, 150, 204, 255)
CHARS['rourik-bhatt'] = {
    'body': 'normal', 'pal': pal('#6a3a78', '#fad6b8', iris='#5a6488', shade='#52285e', deep='#3a1a44'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 94,
             'hairline': [(14, 66), (18, 52), (30, 46), (46, 44), (54, 44), (70, 46), (82, 52), (86, 66)]},
    'front': [L(outline([(16, 70), (8, 50), (14, 22), (30, 4), (40, -4, 1), (50, 6), (60, -4, 1), (70, 4), (86, 22), (92, 50), (84, 70), (50, 56)]), LILAC),
              L(outline([(10, 44), (14, 22), (30, 4), (40, -4, 1), (50, 6), (60, -4, 1), (70, 4), (86, 22), (90, 44), (70, 40), (50, 42), (30, 40)])),
              L(outline([(60, -2), (72, 6), (86, 24), (88, 42), (72, 36)]), 'shade', 'b', False),
              strand([(30, 8), (36, 26), (46, 40)], 'deep', 'b', 1.0), strand([(70, 8), (64, 26), (54, 40)], 'deep', 'b', 1.0),
              L(rope((46, 42), (26, 50), (28, 86), 5), LILAC, 'f'), L(rope((54, 42), (74, 50), (72, 86), 5), LILAC, 'f')],
    'side': [L(outline([(62, 54), (72, 50), (84, 46), (90, 30), (40, -26, 1), (20, -10), (6, 14), (4, 40), (12, 62), (28, 72), (40, 64), (52, 58)]), LILAC),
             L(outline([(90, 30), (40, -26, 1), (20, -10), (6, 14), (4, 36), (40, 30), (70, 34)])),
             L(outline([(20, -6), (40, -22), (60, 0), (40, 20), (10, 30)]), 'shade', 'b', False),
             L(rope((82, 40), (98, 60), (82, 82), 5), LILAC, 'f')],
    'back': [L(outline([(18, 70), (8, 46), (14, 20), (30, 2), (40, -6, 1), (50, 4), (60, -6, 1), (70, 2), (86, 20), (92, 46), (82, 70), (64, 82), (56, 96, 1), (50, 86),
                        (44, 96, 1), (36, 82)]), LILAC),
             L(outline([(8, 46), (14, 20), (30, 2), (40, -6, 1), (50, 4), (60, -6, 1), (70, 2), (86, 20), (92, 46), (70, 40), (50, 44), (30, 40)])),
             L(outline([(58, 0), (84, 20), (90, 44), (70, 38)]), 'shade', 'b', False)],
}

# Menos (Menox Kessler): pelo verde azulado oscuro en forma de casco, con un pico estrecho que baja por la frente y dos
# mechones amarillo verdoso curvos como cuernos que salen hacia los lados; bajo el casco, mechones negros con puntas
# amarillas junto a las mejillas; ojos amarillo verdoso afilados y cara seria
OLIVE = (196, 196, 70, 255)
CHARS['menox-kessler'] = {
    'body': 'normal', 'pal': pal('#3e5a5a', '#fad6b8', iris='#b8d040', shade='#2e4444', deep='#1e2c2c'),
    'face': {'eyes': 'sharp', 'mouth': 'frown', 'mouth_y': 94,
             'hairline': [(14, 80), (18, 62), (30, 52), (42, 50), (50, 64), (58, 50), (70, 52), (82, 62), (86, 80)]},
    'front': [L(rope((20, 70), (16, 86), (24, 100), 6), BLACK), L(rope((80, 70), (84, 86), (76, 100), 6), BLACK),
              L(quad((18, 88), (20, 96), (24, 100)), OLIVE, 'b', False, False, 3.0), L(quad((82, 88), (80, 96), (76, 100)), OLIVE, 'b', False, False, 3.0),
              L(outline([(16, 82), (10, 56), (14, 30), (30, 12), (50, 6), (70, 12), (86, 30), (90, 56), (84, 82), (80, 62), (20, 62)])),
              L(outline([(60, 8), (82, 24), (90, 54), (84, 78), (78, 50)]), 'shade', 'b', False),
              L(outline([(36, 22), (20, 30), (4, 50, 1), (18, 40), (36, 30)]), OLIVE, 'f'), L(outline([(64, 22), (80, 30), (96, 50, 1), (82, 40), (64, 30)]), OLIVE, 'f')],
    'side': [L(outline([(62, 60), (72, 56), (86, 54), (90, 36), (80, 14), (58, 4), (34, 6), (14, 20), (4, 46), (6, 72), (16, 90), (32, 96), (42, 82), (48, 66)])),
             L(outline([(6, 46), (32, 50), (42, 72), (30, 92), (14, 84)]), 'shade', 'b', False),
             L(outline([(56, 38), (74, 26), (86, 16, 1), (80, 30), (62, 44)]), OLIVE, 'f'),
             L(rope((50, 62), (46, 86), (54, 100), 5), OLIVE, 'f')],
    'back': [L(outline([(18, 50), (2, 46, 1), (18, 42)]), OLIVE), L(outline([(82, 50), (98, 46, 1), (82, 42)]), OLIVE),
             L(outline([(16, 84), (10, 56), (14, 30), (30, 12), (50, 6), (70, 12), (86, 30), (90, 56), (84, 84), (66, 92), (50, 94), (34, 92)])),
             L(outline([(58, 8), (82, 24), (90, 56), (84, 84), (60, 90)]), 'shade', 'b', False),
             L(quad((20, 86), (22, 96), (26, 100)), OLIVE, 'f', False, False, 2.6), L(quad((80, 86), (78, 96), (74, 100)), OLIVE, 'f', False, False, 2.6)],
}

# Crisis (Crysis Murdok, portero suplente): melena lisa malva muy larga que le cae por delante de los hombros, flequillo
# recto a la altura de los ojos con una franja central rojo coral; ojos amarillos con raya negra en punta
CORAL = (240, 106, 106, 255)
CHARS['crysis-murdok'] = {
    'body': 'normal', 'pal': pal('#c49aa0', '#fad6b8', iris='#d8c830', shade='#9e7a80', deep='#6e5054'),
    'face': {'eyes': 'sharp', 'mouth': 'line', 'mouth_y': 93, 'ears': False,
             'hairline': [(14, 100), (16, 64), (50, 64), (84, 64), (86, 100)]},
    'front': longhair('front', length=122, flare=2, top=4) + [
              L(outline([(14, 66), (12, 36), (24, 12), (50, 4), (76, 12), (88, 36), (86, 66), (50, 66)]), 'mid', 'f'),
              L(outline([(44, 6), (56, 6), (58, 66), (42, 66)]), CORAL, 'f', False),
              L(outline([(60, 8), (80, 18), (88, 40), (86, 64), (72, 64)]), 'shade', 'f', False),
              strand([(30, 12), (26, 66)], 'deep', 'f', 1.0), strand([(70, 12), (74, 66)], 'deep', 'f', 1.0),
              strand([(16, 70), (14, 118)], 'deep', 'f', 1.0), strand([(84, 70), (86, 118)], 'deep', 'f', 1.0),
              L([(26, 72), (20, 70)], BLACK, 'f', False, False, 2.4), L([(74, 72), (80, 70)], BLACK, 'f', False, False, 2.4)],
    'side': longhair('side', length=124, flare=2, top=4) + [
             L(outline([(88, 60), (92, 30), (84, 12), (90, 22), (94, 44)]), CORAL, 'b', False)],
    'back': longhair('back', length=124, flare=2, top=4, ends=3),
}
