"""Secundaria Internacional Eastwind (vr-toufuu-ikokukan, 東風異国館): personajes propios de Victory Road, con sus modelos 3D
de 英雄たちのヴィクトリーロード en la enciclopedia. Cada uno tiene una sola forma; van como 'vr:<id>' para que ningún id
coja por prefijo el dibujo de otro."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, outline, pal, rope, strand  # noqa: F401
from heads import quad  # noqa: F401

V = 'vr'
WHITE = (248, 248, 248, 255)
FRECKLE = (196, 120, 96, 255)


def fr(pts, c='mid'):
    return L(outline(pts), c, 'f')


def fre(pts, k, c='mid', w=1.1):
    """Flequillo con la línea de las puntas (pts[k:]) marcada: si no, sobre piel clara no se distinguen los mechones."""
    return [fr(pts, c), L([p[:2] for p in pts[k:]], OUTC, 'f', False, False, w)]


def dots(pts, c=FRECKLE, r=0.9):
    return [L(ell(x, y, r, r), c, 'f', False) for x, y in pts]


# Martino Leone (portero): rubio pálido con un remolino en la coronilla; flequillo largo en puntas que le cae entre los ojos,
# dos pinchos de lado a la altura de las sienes y una melena que por detrás le baja en punta hasta la nuca; ojos turquesa
CHARS[f'{V}:martino-leone'] = {
    'body': 'normal', 'pal': pal('#ece0b4', '#fce2cc', iris='#3a9aa0', shade='#cfc092', deep='#a89870'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(20, 94), (14, 72), (12, 62), (-4, 58, 1), (10, 50), (12, 34), (22, 14), (40, 2), (50, 0), (62, 2), (80, 12), (90, 32), (90, 48), (104, 50, 1),
                         (90, 58), (88, 72), (82, 94), (78, 70), (22, 70)])),
              L(outline([(60, 4), (82, 14), (92, 36), (90, 70), (84, 92), (78, 56)]), 'shade', 'b', False),
              L(outline([(44, 6), (48, -4, 1), (54, 6)]), 'deep', 'b', False),
              fre([(14, 76), (14, 46), (26, 22), (50, 14), (74, 22), (86, 46), (86, 76), (80, 60), (74, 66, 1), (68, 54), (56, 60), (50, 86, 1), (46, 58), (34, 54),
                  (28, 66, 1), (22, 58), (18, 82, 1)], 7),
              strand([(36, 22), (40, 44)], 'deep', 'f', 1.0), strand([(62, 22), (58, 44)], 'deep', 'f', 1.0)],
    'side': [L(outline([(62, 84), (58, 60), (72, 54), (84, 52), (96, 50, 1), (90, 40), (86, 22), (70, 6), (50, 0), (28, 4), (12, 18), (4, 40), (4, 66), (10, 92),
                        (22, 108, 1), (30, 90), (36, 74), (44, 62)])),
             L(outline([(4, 44), (26, 50), (36, 74), (30, 90), (22, 106), (10, 92), (4, 66)]), 'shade', 'b', False),
             L(outline([(70, 52), (78, 46), (74, 62), (66, 80, 1), (64, 58)]), 'mid', 'f')],
    'back': [L(outline([(22, 86), (16, 66), (14, 60), (-2, 58, 1), (14, 52), (14, 30), (28, 10), (50, 2), (72, 10), (86, 30), (86, 52), (102, 58, 1), (86, 62), (84, 80),
                        (68, 96), (56, 112, 1), (50, 100), (42, 110, 1), (32, 94)])),
             L(outline([(54, 6), (76, 14), (88, 40), (84, 80), (60, 106), (64, 50)]), 'shade', 'b', False),
             strand([(40, 30), (44, 70), (46, 96)], 'deep', 'b', 1.0)],
}

# Jenny Okutba: media melena lila azulada en casco con la raya en medio y un remolino arriba; el flequillo se abre en V
# sobre la frente, las puntas se abren hacia fuera con el envés gris y dos rizos le enmarcan la barbilla; dos lunares bajo
# los ojos turquesa y sonrisa pícara
CHARS[f'{V}:jenny-okutba'] = {
    'body': 'chica', 'pal': pal('#6a68b8', '#fde6d6', iris='#4aa0a8', shade='#52509a', deep='#3c3a7a', under='#b4b4c0'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(22, 100), (16, 92), (14, 86), (0, 90, 1), (-4, 82, 1), (8, 74), (10, 58), (12, 34), (24, 12), (50, 2), (76, 12), (88, 34), (90, 58), (92, 74),
                         (104, 82, 1), (100, 90, 1), (86, 86), (84, 92), (78, 100), (70, 78), (30, 78)])),
              L(outline([(0, 90), (6, 80), (16, 84), (14, 90)]), 'under', 'b', False), L(outline([(100, 90), (94, 80), (84, 84), (86, 90)]), 'under', 'b', False),
              L(outline([(60, 6), (82, 18), (90, 50), (88, 80), (78, 56)]), 'shade', 'b', False),
              fre([(14, 88), (12, 58), (22, 30), (46, 12), (50, 18), (54, 12), (78, 30), (88, 58), (86, 88), (80, 76), (74, 62), (62, 54), (50, 60, 1), (38, 54), (26, 62),
                  (20, 76)], 9),
              fr([(18, 74), (26, 80), (28, 96), (36, 102), (28, 106), (20, 96)]), fr([(82, 74), (74, 80), (72, 96), (64, 102), (72, 106), (80, 96)]),
              strand([(48, 14), (50, 6), (52, 14)], 'deep', 'f', 1.0)] + dots([(33, 86), (67, 86)], OUTC, 1.0),
    'side': [L(outline([(64, 92), (60, 66), (74, 58), (86, 52), (92, 38), (84, 16), (60, 2), (34, 4), (14, 16), (6, 40), (6, 56), (-6, 64, 1), (2, 72), (18, 74),
                        (30, 86), (40, 82), (46, 62)])),
             L(outline([(-6, 64), (2, 58), (14, 64), (16, 72), (2, 72)]), 'under', 'b', False),
             L(outline([(6, 40), (30, 46), (40, 80), (30, 86), (18, 74), (6, 58)]), 'shade', 'b', False),
             fr([(72, 58), (84, 56), (86, 74), (82, 94), (88, 100), (78, 100), (74, 80)])],
    'back': [L(outline([(12, 96), (6, 90), (-4, 96, 1), (6, 80), (8, 50), (16, 20), (50, 4), (84, 20), (92, 50), (94, 80), (104, 96, 1), (94, 90), (88, 96), (50, 100)])),
             L(outline([(-4, 96), (6, 84), (16, 92), (12, 98)]), 'under', 'b', False), L(outline([(104, 96), (94, 84), (84, 92), (88, 98)]), 'under', 'b', False),
             L(outline([(56, 6), (84, 22), (92, 56), (88, 94), (66, 98), (70, 50)]), 'shade', 'b', False),
             strand([(50, 6), (50, 16)], 'deep', 'b', 1.0)],
}

# Gigy Maharaja: grandullón moreno de cara redonda y ceño de enfado; trenzas pegadas al cráneo arriba (rayas claras) y
# detrás una nube enorme de rizos granates, con mechones gruesos que le salen de lado a la altura de los hombros
_gigy_puff = bumpy(50, 40, 60, 52, n=14, amp=0.07)
CHARS[f'{V}:gigy-maharaja'] = {
    'body': 'corpulento', 'pal': pal('#6a2a48', '#a8704c', iris='#2a1e1a', shade='#52203a', deep='#3a142a', row='#b07a7a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False,
             'face_front': blob([(14, 52), (50, 34), (86, 52), (92, 76), (86, 100), (66, 110), (50, 112), (34, 110), (14, 100), (8, 76)])},
    'front': [L(_gigy_puff), L(rope((14, 92), (0, 98), (-18, 98), 7)), L(rope((86, 92), (100, 98), (118, 98), 7)),
              L(outline([(56, -8), (96, 16), (108, 50), (96, 84), (80, 50)]), 'shade', 'b', False),
              L(outline([(16, 62), (16, 40), (28, 24), (50, 18), (72, 24), (84, 40), (84, 62), (76, 52), (50, 48), (24, 52)]), 'mid', 'f'),
              strand([(30, 54), (32, 26)], 'row', 'f', 1.2), strand([(42, 50), (44, 20)], 'row', 'f', 1.2), strand([(58, 50), (56, 20)], 'row', 'f', 1.2),
              strand([(70, 54), (68, 26)], 'row', 'f', 1.2)],
    'side': [L(bumpy(30, 36, 44, 50, n=12, amp=0.08)), L(rope((20, 70), (0, 90), (-20, 100), 8)), L(rope((30, 76), (14, 96), (-2, 108), 7)),
             L(outline([(4, 50), (30, 70), (20, 86), (-6, 80)]), 'shade', 'b', False),
             L(outline([(50, 60), (52, 30), (64, 20), (82, 26), (90, 44), (80, 54), (66, 56)]), 'mid', 'f'),
             strand([(60, 54), (66, 24)], 'row', 'f', 1.2), strand([(72, 52), (78, 26)], 'row', 'f', 1.2)],
    'back': [L(bumpy(50, 40, 60, 54, n=14, amp=0.07)), L(rope((16, 92), (0, 98), (-18, 98), 7)), L(rope((84, 92), (100, 98), (118, 98), 7)),
             L(rope((36, 92), (30, 100), (24, 108), 7)), L(rope((64, 92), (70, 100), (76, 108), 7)),
             L(outline([(54, -10), (96, 14), (110, 52), (96, 90), (70, 80)]), 'shade', 'b', False)],
}

# Judie Cassios: chica morena de pelo rizado morado oscuro: una cúpula de rizos arriba con una diadema blanca y dos
# moños de rizos grandes abajo a los lados; cejas marcadas, ojos verdes y una sonrisa enseñando los dientes
CHARS[f'{V}:judie-cassios'] = {
    'body': 'chica', 'pal': pal('#3a1e3e', '#6e4434', iris='#3aa08a', shade='#2a1430', deep='#1e0e22', band='#f0f0f2'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'grin', 'mouth_y': 97, 'hairline': [(16, 66), (22, 54), (36, 48), (50, 46), (64, 48), (78, 54), (84, 66)]},
    'front': [L(bumpy(50, 26, 44, 32, n=12, amp=0.08)), L(bumpy(8, 84, 16, 16, n=8, amp=0.1)), L(bumpy(92, 84, 16, 16, n=8, amp=0.1)),
              L(outline([(16, 70), (14, 40), (86, 40), (84, 70), (50, 60)])),
              L(outline([(58, -6), (88, 12), (94, 40), (86, 64), (76, 30)]), 'shade', 'b', False),
              L(quad((16, 58), (50, -12), (84, 58)), 'band', 'f', False, False, 3.6)],
    'side': [L(bumpy(46, 24, 44, 30, n=12, amp=0.08)), L(bumpy(10, 78, 20, 18, n=8, amp=0.1)),
             L(outline([(54, 62), (60, 46), (80, 44), (88, 30), (60, 20), (20, 30), (10, 60), (24, 70), (44, 60)])),
             L(outline([(0, 70), (20, 64), (28, 86), (8, 94)]), 'shade', 'b', False),
             L(quad((60, 56), (66, 18), (86, 14)), 'band', 'f', False, False, 3.6)],
    'back': [L(bumpy(50, 26, 46, 34, n=12, amp=0.08)), L(bumpy(50, 78, 50, 24, n=12, amp=0.08)),
             L(outline([(58, -6), (92, 16), (98, 70), (90, 98), (70, 60)]), 'shade', 'b', False)],
}

# Robart Anderson: moreno con una mata de rizos verde petróleo muy oscuro arriba, en forma de seta, y los lados y la
# nuca rapados en degradado; cejas verdes, ojos color oliva y sonrisa tranquila
CHARS[f'{V}:robart-anderson'] = {
    'body': 'normal', 'pal': pal('#1e3c40', '#8a5634', iris='#8a8a4a', shade='#142c30', deep='#0e2024', shave='#4e4448', shave_d='#2e3e40'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': [(16, 60), (24, 52), (50, 50), (76, 52), (84, 60)]},
    'front': [L(outline([(16, 66), (16, 40), (84, 40), (84, 66), (50, 56)]), 'shave', 'b'),
              L(bumpy(50, 22, 48, 26, n=14, amp=0.07)),
              L(outline([(58, -2), (90, 10), (98, 30), (88, 44), (70, 30)]), 'shade', 'b', False),
              L(outline([(18, 56), (16, 44), (24, 44), (22, 56)]), 'shave_d', 'f', False), L(outline([(82, 56), (84, 44), (76, 44), (78, 56)]), 'shave_d', 'f', False)],
    'side': [L(outline([(50, 60), (52, 40), (20, 36), (10, 60), (20, 80), (40, 74)]), 'shave', 'b'),
             L(outline([(12, 66), (20, 50), (50, 50), (40, 70), (22, 80)]), 'shave_d', 'b', False),
             strand([(14, 62), (44, 60)], 'shave', 'b', 0.8), strand([(18, 70), (40, 68)], 'shave', 'b', 0.8),
             L(bumpy(46, 18, 48, 26, n=14, amp=0.07)),
             L(outline([(4, 20), (30, 30), (60, 34), (40, 44), (10, 38)]), 'shade', 'b', False)],
    'back': [L(outline([(18, 80), (14, 40), (86, 40), (82, 80), (50, 86)]), 'shave', 'b'),
             L(outline([(16, 46), (84, 46), (84, 66), (50, 72), (16, 66)]), 'shave_d', 'b', False),
             strand([(18, 58), (50, 64), (82, 58)], 'shave', 'b', 0.8),
             L(bumpy(50, 20, 50, 28, n=14, amp=0.07)),
             L(outline([(56, -4), (92, 10), (100, 34), (80, 44), (66, 24)]), 'shade', 'b', False)],
}

# Maribelle Flanmir: chica de piel oscura con una melena naranja enorme y esponjosa, con dos puntas que le salen arriba a
# los lados como orejas de gato; flequillo de lado con un mechón que baja sobre un ojo; ojos azules grandes, boca pequeña
CHARS[f'{V}:maribelle-flanmir'] = {
    'body': 'chica', 'pal': pal('#e8783e', '#5a3a2c', iris='#3a9ad0', shade='#c85e2a', deep='#a0461c'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 97, 'hairline': False},
    'front': [L(outline([(12, 98), (4, 84), (8, 74), (2, 50), (2, 30), (-10, 6, 1), (10, 18), (22, 4), (50, -4), (78, 4), (90, 18), (110, 6, 1), (98, 30), (98, 50),
                         (92, 74), (96, 84), (88, 98), (80, 76), (20, 76)])),
              L(outline([(58, -2), (86, 10), (98, 40), (94, 86), (82, 60)]), 'shade', 'b', False),
              fr([(10, 84), (10, 44), (24, 22), (50, 14), (76, 22), (90, 44), (90, 84), (84, 68), (80, 54), (64, 50), (50, 56), (42, 78, 1), (38, 58), (28, 60),
                  (18, 74)]),
              strand([(30, 24), (36, 46)], 'deep', 'f', 1.0), strand([(62, 22), (60, 44)], 'deep', 'f', 1.0)],
    'side': [L(outline([(62, 90), (58, 62), (74, 56), (88, 48), (92, 30), (80, 10), (60, 0), (40, 2), (30, -14, 1), (24, 6), (8, 18), (0, 42), (2, 72), (8, 94),
                        (24, 100), (40, 90), (46, 66)])),
             L(outline([(0, 44), (24, 50), (40, 88), (24, 98), (6, 90)]), 'shade', 'b', False),
             fr([(70, 54), (88, 46), (90, 62), (80, 70)])],
    'back': [L(outline([(10, 98), (2, 72), (4, 40), (-10, 8, 1), (12, 22), (30, 6), (50, 2), (70, 6), (88, 22), (110, 8, 1), (96, 40), (98, 72), (90, 98), (70, 102),
                        (50, 98), (30, 102)])),
             L(outline([(56, 4), (86, 22), (98, 60), (90, 98), (66, 100), (70, 50)]), 'shade', 'b', False)],
}

# Toyo Yamanouchi: pálido y pecoso, con un afro negro violáceo enorme y erizado en puntas pequeñas que le tapa la frente en
# línea recta; cejas negras gruesas y ojos verdes serios
_afro = [(-14, 84), (-8, 74, 1), (-18, 60), (-8, 52, 1), (-16, 36), (-4, 30, 1), (-10, 14), (4, 12, 1), (2, -4), (16, -2, 1), (22, -16), (34, -8, 1),
         (44, -20), (54, -10, 1), (64, -20), (72, -8, 1), (84, -14), (88, 0, 1), (100, -2), (98, 14, 1), (112, 18), (104, 32, 1), (116, 40), (106, 52, 1),
         (118, 62), (108, 74, 1), (114, 86), (98, 86, 1), (86, 92), (84, 70), (16, 70), (14, 92), (2, 86, 1)]
CHARS[f'{V}:toyo-yamanouchi'] = {
    'body': 'normal', 'pal': pal('#2e1e30', '#fde8dc', iris='#6a8a3a', shade='#1e1220', deep='#140a16'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 96,
             'hairline': [(14, 66), (20, 58), (28, 62), (36, 56), (44, 61), (52, 56), (60, 61), (68, 56), (76, 62), (82, 58), (86, 66)]},
    'front': [L(outline(_afro)),
              L(outline([(58, -10), (96, 4), (110, 40), (104, 80), (86, 60)]), 'shade', 'b', False)] + dots([(30, 86), (34, 88), (38, 86), (62, 86), (66, 88), (70, 86), (50, 84)]),
    'side': [L(outline([(60, 62), (64, 52), (86, 50), (96, 40), (104, 30, 1), (98, 16), (104, 4, 1), (90, -2), (90, -16, 1), (74, -10), (66, -22, 1), (54, -10), (40, -22, 1),
                        (30, -8), (14, -12, 1), (10, 4), (-6, 4, 1), (-2, 20), (-16, 28, 1), (-6, 40), (-18, 52, 1), (-6, 60), (-14, 76, 1), (2, 78), (0, 92, 1),
                        (16, 86), (22, 98, 1), (30, 84), (44, 72)])),
             L(outline([(-6, 40), (26, 46), (32, 84), (2, 80)]), 'shade', 'b', False)],
    'back': [L(outline([p[:2] if len(p) == 2 else p for p in _afro[:-4]] + [(86, 96), (70, 104, 1), (60, 94), (50, 104, 1), (40, 94), (30, 104, 1), (16, 96)])),
             L(outline([(56, -10), (98, 4), (112, 50), (104, 92), (70, 96), (74, 40)]), 'shade', 'b', False)],
}

# Ming Chow: pelo granate corto con tres pinchos arriba y una fila de rizos en forma de coma por todo el nacimiento del
# pelo; ojos gris azulado con sombra morada oscura alrededor y cejas finas
MK = (112, 66, 120, 255)
CHARS[f'{V}:ming-chow'] = {
    'body': 'normal', 'pal': pal('#8a2e3a', '#fcdcc4', iris='#6a7a9c', shade='#6e222c', deep='#521820'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'line', 'mouth_y': 96,
             'hairline': [(16, 68), (20, 58), (28, 62), (32, 52), (42, 56), (50, 50), (58, 56), (68, 52), (72, 62), (80, 58), (84, 68)]},
    'front': [L(outline([(16, 82), (12, 60), (12, 36), (22, 18), (30, 8), (34, -4, 1), (42, 6), (50, -10, 1), (58, 4), (66, -4, 1), (72, 8), (82, 20), (90, 36), (90, 60),
                         (84, 82), (80, 66), (20, 66)])),
              L(outline([(58, 2), (68, -10), (72, 8), (82, 20), (90, 40), (86, 80), (76, 50)]), 'shade', 'b', False),
              strand([(24, 60), (22, 54), (28, 52)], 'deep', 'b', 1.0), strand([(40, 54), (38, 48), (44, 46)], 'deep', 'b', 1.0),
              strand([(60, 54), (62, 48), (56, 46)], 'deep', 'b', 1.0), strand([(76, 60), (78, 54), (72, 52)], 'deep', 'b', 1.0),
              L(quad((27, 72), (36, 66), (44, 70)), MK, 'f', False, False, 1.6), L(quad((73, 72), (64, 66), (56, 70)), MK, 'f', False, False, 1.6)],
    'side': [L(outline([(58, 62), (62, 50), (82, 46), (90, 34), (86, 16), (90, 2, 1), (72, 4), (66, -6, 1), (54, 0), (42, -6, 1), (32, 2), (12, 10), (4, 30), (4, 56),
                        (12, 80), (28, 82), (40, 70), (50, 60)])),
             L(outline([(4, 34), (28, 40), (36, 74), (14, 78)]), 'shade', 'b', False),
             strand([(72, 50), (76, 44), (82, 48)], 'deep', 'b', 1.0)],
    'back': [L(outline([(14, 82), (10, 60), (10, 36), (22, 16), (32, 8), (36, -4, 1), (44, 6), (52, -8, 1), (60, 4), (66, -2, 1), (72, 8), (82, 18), (90, 36), (90, 60),
                        (84, 82), (66, 90), (50, 86), (34, 90)])),
             L(outline([(58, 4), (82, 20), (90, 50), (84, 82), (64, 88), (70, 40)]), 'shade', 'b', False)],
}

# Joey Beat: piel muy oscura, lados y nuca rapados en gris y un tupé negro brillante peinado hacia su izquierda que acaba en
# mechones largos y finos que le cuelgan por un lado de la cara; ojos verdes afilados y media sonrisa
CHARS[f'{V}:joey-beat'] = {
    'body': 'normal', 'pal': pal('#16161a', '#4a3028', iris='#5ab08a', shade='#0c0c10', light='#5a5a66', shave='#7a7a7e', shave_d='#5e5e64'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': [(14, 70), (18, 52), (32, 46), (50, 44), (68, 46), (82, 52), (86, 70)]},
    'front': [L(outline([(14, 76), (12, 46), (20, 24), (50, 14), (80, 24), (88, 46), (86, 76), (50, 64)]), 'shave', 'b'),
              L(outline([(14, 50), (16, 22), (34, 2), (60, -6), (84, 2), (96, 22), (98, 50), (104, 76, 1), (94, 64), (98, 100, 1), (88, 76), (86, 52), (76, 34), (52, 30),
                         (30, 34), (22, 46)]), 'mid', 'f'),
              L(outline([(70, 2), (90, 14), (96, 34), (90, 50), (84, 30)]), 'shade', 'f', False),
              strand([(30, 14), (60, 4), (84, 12)], 'light', 'f', 1.4)],
    'side': [L(outline([(56, 62), (60, 50), (80, 46), (88, 30), (60, 18), (20, 24), (8, 50), (14, 80), (34, 86), (44, 72)]), 'shave', 'b'),
             L(outline([(10, 54), (30, 50), (44, 74), (34, 86), (14, 80)]), 'shave_d', 'b', False),
             L(outline([(14, 30), (26, 10), (50, 0), (80, -2), (100, 8), (104, 20, 1), (88, 16), (70, 20), (44, 22), (24, 34)]), 'mid', 'f'),
             strand([(30, 14), (60, 4), (90, 6)], 'light', 'f', 1.4)],
    'back': [L(outline([(16, 84), (12, 46), (22, 20), (50, 12), (78, 20), (88, 46), (84, 84), (50, 92)]), 'shave', 'b'),
             L(outline([(30, 74), (26, 30), (36, 8), (64, 8), (74, 30), (70, 74), (50, 80)]), 'mid', 'f'),
             L(outline([(80, 30), (92, 40), (100, 80, 1), (90, 66), (86, 90, 1), (80, 60)]), 'mid', 'f'),
             strand([(42, 14), (40, 50)], 'light', 'f', 1.2)],
}

# Kai Yoshizaki: aire de mayor, cara ancha; pelo gris pardo erizado arriba con mechones de lado sobre la frente y una
# melena larga detrás (mullet) que le cae hasta los hombros; ojos rojos con sombra rosa y una sonrisa ancha
CHARS[f'{V}:kai-yoshizaki'] = {
    'body': 'normal', 'pal': pal('#8a8680', '#fcdcc8', iris='#c83a4a', shade='#6a6660', deep='#4e4a46'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False,
             'face_front': blob([(16, 52), (50, 36), (84, 52), (88, 76), (84, 96), (64, 106), (50, 108), (36, 106), (16, 96), (12, 76)])},
    'front': [L(outline([(8, 106), (2, 94), (14, 84), (12, 50), (6, 30), (-2, 14, 1), (16, 16), (20, -2), (34, 4), (40, -12, 1), (52, 0), (64, -10, 1), (72, 6), (88, 4, 1),
                         (86, 20), (98, 30, 1), (88, 46), (86, 84), (98, 94), (92, 106), (80, 84), (20, 84)])),
              L(outline([(60, -2), (86, 8), (94, 40), (90, 100), (80, 60)]), 'shade', 'b', False),
              fre([(16, 66), (16, 42), (30, 26), (50, 22), (72, 26), (84, 40), (84, 66), (78, 52), (66, 46), (60, 62, 1), (54, 46), (40, 46), (28, 52), (22, 66, 1)], 7),
              L(quad((28, 70), (36, 67), (44, 70)), (220, 120, 140, 255), 'f', False, False, 1.4),
              L(quad((72, 70), (64, 67), (56, 70)), (220, 120, 140, 255), 'f', False, False, 1.4)],
    'side': [L(outline([(60, 60), (62, 48), (82, 44), (94, 32), (100, 16, 1), (86, 14), (88, -4, 1), (70, 2), (62, -14, 1), (50, 0), (34, -8, 1), (26, 8), (10, 16), (2, 40),
                        (-2, 70), (-10, 98, 1), (6, 92), (8, 108, 1), (22, 92), (34, 80), (44, 64)])),
             L(outline([(2, 44), (26, 50), (34, 80), (14, 100), (-2, 80)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 98), (8, 70), (10, 40), (0, 20, 1), (16, 18), (22, -2), (36, 4), (42, -12, 1), (52, 0), (64, -10, 1), (72, 6), (88, 4, 1), (86, 20), (100, 22, 1),
                        (90, 40), (92, 70), (86, 98), (74, 112, 1), (64, 100), (50, 114, 1), (36, 100), (26, 112, 1)])),
             L(outline([(56, -2), (86, 10), (94, 60), (86, 98), (64, 104), (70, 50)]), 'shade', 'b', False),
             strand([(32, 40), (34, 80), (30, 104)], 'deep', 'b', 1.0), strand([(66, 40), (64, 80), (68, 104)], 'deep', 'b', 1.0)],
}

# Sikuvot Shivan: rubio con el pelo en capas de mechones que salen de lado como alas, y un dibujo dorado oscuro en el
# flequillo (como una estrella con rayas que bajan hacia las cejas); ojos azul grisáceo grandes y sonrisa
CHARS[f'{V}:sikuvot-shivan'] = {
    'body': 'normal', 'pal': pal('#f0d888', '#fde2cc', iris='#8aa0d0', shade='#d0b46a', deep='#b0944c', gold='#c8a040'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 72), (14, 58), (-6, 54, 1), (10, 46), (-8, 32, 1), (14, 26), (4, 10, 1), (26, 8), (40, -2), (60, -2), (74, 8), (96, 10, 1), (86, 26),
                         (108, 32, 1), (90, 46), (106, 54, 1), (86, 58), (84, 72), (78, 58), (22, 58)])),
              L(outline([(60, 0), (76, 10), (94, 12), (88, 26), (104, 34), (90, 46), (84, 64), (76, 40)]), 'shade', 'b', False),
              fre([(14, 64), (16, 44), (30, 28), (50, 24), (70, 28), (84, 44), (86, 64), (78, 56), (72, 62, 1), (64, 54), (58, 62, 1), (50, 54), (42, 62, 1), (36, 54),
                  (28, 62, 1), (22, 56)], 7),
              L(outline([(50, 30), (56, 42), (72, 40), (58, 48), (60, 62, 1), (50, 52), (40, 62, 1), (42, 48), (28, 40), (44, 42)]), 'gold', 'f', False)],
    'side': [L(outline([(58, 62), (62, 50), (84, 46), (94, 30), (90, 12), (70, 0), (44, -2), (22, 6), (-4, 4, 1), (10, 18), (-8, 28, 1), (8, 36), (-8, 48, 1), (8, 52),
                        (6, 66, 1), (20, 64), (36, 60), (48, 58)])),
             L(outline([(-8, 28), (30, 30), (60, 44), (40, 56), (8, 52)]), 'shade', 'b', False),
             strand([(10, 18), (50, 22), (84, 34)], 'deep', 'b', 1.0)],
    'back': [L(outline([(18, 70), (14, 58), (-8, 52, 1), (10, 44), (-8, 30, 1), (12, 24), (6, 8, 1), (26, 8), (40, -2), (60, -2), (74, 8), (94, 8, 1), (88, 24), (108, 30, 1),
                        (90, 44), (108, 52, 1), (86, 58), (82, 70), (72, 64, 1), (62, 72), (50, 64, 1), (38, 72), (28, 64, 1)])),
             L(outline([(4, 36), (20, 30), (30, 40, 1), (40, 30), (50, 40, 1), (60, 30), (70, 40, 1), (80, 30), (96, 36), (90, 46), (10, 46)]), 'shade', 'b', False),
             L(outline([(10, 14), (24, 12), (34, 22, 1), (44, 12), (50, 20, 1), (56, 12), (66, 22, 1), (76, 12), (90, 14), (86, 22), (14, 22)]), 'light', 'b', False)],
}

# Olson Carchis: pelo color caqui ondulado y abultado, con rizos en S que le enmarcan la cara hasta las mejillas y un
# flequillo ondulado; ojos turquesa con sombra rosa y sonrisa
CHARS[f'{V}:olson-carchis'] = {
    'body': 'normal', 'pal': pal('#a49c6c', '#fcdcc8', iris='#4aa0a0', shade='#857e52', deep='#66603c'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(14, 98), (4, 84), (12, 70), (2, 54), (6, 30), (22, 10), (40, 2), (50, 6), (60, 0), (80, 8), (96, 28), (98, 54), (90, 70), (98, 84), (86, 98),
                         (80, 76), (20, 76)])),
              L(outline([(60, 2), (84, 12), (98, 50), (92, 94), (80, 60)]), 'shade', 'b', False),
              fre([(12, 72), (12, 46), (26, 26), (50, 20), (74, 26), (88, 46), (88, 72), (82, 58), (72, 54), (64, 62, 1), (60, 52), (46, 52), (38, 60, 1), (32, 54), (24, 58),
                  (18, 72)], 7),
              fr([(14, 66), (22, 70), (18, 82), (24, 92), (16, 96), (10, 84)]), fr([(86, 66), (78, 70), (82, 82), (76, 92), (84, 96), (90, 84)]),
              strand([(44, 8), (50, 16), (56, 8)], 'deep', 'f', 1.0)],
    'side': [L(outline([(60, 66), (62, 52), (82, 48), (94, 34), (92, 14), (74, 0), (46, -2), (22, 6), (6, 24), (0, 50), (4, 74), (0, 90), (14, 96), (24, 88), (36, 90),
                        (40, 74), (48, 64)])),
             L(outline([(2, 46), (26, 50), (38, 74), (24, 88), (6, 84)]), 'shade', 'b', False),
             fr([(72, 50), (86, 48), (82, 64), (86, 76), (78, 80), (74, 64)])],
    'back': [L(outline([(12, 96), (4, 80), (8, 60), (4, 34), (20, 10), (50, 2), (80, 10), (96, 34), (92, 60), (96, 80), (88, 96), (74, 100), (66, 92), (50, 98), (34, 92),
                        (26, 100)])),
             L(outline([(56, 4), (84, 16), (96, 50), (90, 94), (66, 96), (72, 50)]), 'shade', 'b', False),
             strand([(30, 30), (36, 50), (30, 70)], 'deep', 'b', 1.0), strand([(70, 30), (64, 50), (70, 70)], 'deep', 'b', 1.0)],
}

# Mengmeng Wang: chica de pelo rojo muy abultado y ondulado, recogido en una trenza gruesa que le cae por delante por un lado
# con una goma azul; ojos ámbar grandes, pecas rojas en las mejillas y sonrisa
CHARS[f'{V}:mengmeng-wang'] = {
    'body': 'chica', 'pal': pal('#c83a2a', '#fde2cc', iris='#c8783a', shade='#a42c20', deep='#801e16', tie='#6a8ad0'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 90), (6, 60), (8, 30), (20, 6), (40, -6), (60, -6), (80, 6), (94, 30), (96, 60), (90, 88), (82, 70), (18, 70)])),
              L(outline([(60, -4), (84, 8), (96, 40), (92, 84), (80, 54)]), 'shade', 'b', False),
              fre([(12, 74), (10, 44), (24, 20), (48, 12), (72, 18), (88, 38), (90, 74), (82, 58), (74, 50), (62, 46), (54, 58), (46, 46), (36, 50), (26, 58), (18, 74)], 7),
              strand([(30, 20), (40, 34)], 'deep', 'f', 1.0), strand([(64, 16), (70, 30)], 'deep', 'f', 1.0),
              L(rope((16, 82), (6, 98), (14, 116), 8), 'mid', 'f'), L(ell(9, 102, 4.6, 2.6), 'tie', 'f'),
              L(outline([(12, 104), (18, 108), (16, 118), (8, 114)]), 'shade', 'f', False)] + dots([(30, 86), (34, 88), (66, 88), (70, 86)], (220, 80, 70, 255), 1.1),
    'side': [L(outline([(62, 62), (64, 50), (84, 46), (94, 30), (88, 8), (64, -6), (36, -6), (14, 6), (2, 30), (2, 60), (12, 80), (32, 82), (44, 72), (52, 62)])),
             L(outline([(4, 34), (28, 40), (40, 74), (16, 78)]), 'shade', 'b', False),
             L(rope((40, 76), (42, 96), (50, 112), 7), 'mid', 'f'), L(ell(42, 98, 3.6, 2.4), 'tie', 'f')],
    'back': [L(outline([(12, 88), (6, 60), (8, 30), (20, 6), (40, -6), (60, -6), (80, 6), (94, 30), (96, 60), (88, 88), (70, 96), (50, 92), (30, 96)])),
             L(outline([(56, -4), (84, 10), (96, 50), (88, 88), (66, 92), (72, 40)]), 'shade', 'b', False),
             strand([(30, 20), (40, 50), (34, 80)], 'deep', 'b', 1.0), strand([(64, 16), (60, 50), (66, 80)], 'deep', 'b', 1.0)],
}

# Kain Vijet: tupé castaño claro peinado hacia arriba y atrás con un mechón en punta en el centro y pico en la frente; la
# nuca más corta con dos mechas rojas; cejas gruesas, ojos grises con ojeras y sonrisa
CHARS[f'{V}:kain-vijet'] = {
    'body': 'normal', 'pal': pal('#a47c5c', '#fde2cc', iris='#6a6a66', shade='#866044', deep='#664630', red='#c8282a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96,
             'hairline': [(16, 68), (20, 54), (34, 48), (44, 50), (50, 60), (56, 50), (66, 48), (80, 54), (84, 68)]},
    'front': [L(outline([(16, 76), (12, 52), (12, 30), (22, 8), (36, -4), (50, -10), (64, -4), (78, 8), (88, 30), (88, 52), (84, 76), (78, 56), (22, 56)])),
              L(outline([(60, -4), (80, 8), (90, 34), (86, 70), (76, 40)]), 'shade', 'b', False),
              L(outline([(44, 50), (46, 30), (50, 16), (54, 30), (56, 50), (50, 58)]), 'deep', 'b', False),
              strand([(30, 50), (32, 16)], 'deep', 'b', 1.0), strand([(70, 50), (68, 16)], 'deep', 'b', 1.0)],
    'side': [L(outline([(58, 60), (60, 48), (80, 44), (92, 32), (106, 32, 1), (94, 20), (90, 4), (70, -10), (40, -10), (20, -2), (8, 16), (4, 44), (8, 66), (14, 80, 1),
                        (22, 70), (28, 82, 1), (34, 68), (44, 60)])),
             L(outline([(4, 30), (40, 34), (60, 44), (36, 60), (8, 60)]), 'shade', 'b', False),
             strand([(30, -4), (60, 10), (86, 24)], 'deep', 'b', 1.0),
             L(outline([(22, 72), (26, 64), (28, 80, 1)]), 'red', 'f', False), L(outline([(30, 70), (34, 62), (34, 78, 1)]), 'red', 'f', False)],
    'back': [L(outline([(16, 80), (12, 52), (12, 30), (22, 10), (36, 0), (50, -10, 1), (64, 0), (78, 10), (88, 30), (88, 52), (84, 80), (76, 88, 1), (68, 82), (60, 90, 1),
                        (50, 82), (40, 90, 1), (32, 82), (24, 88, 1)])),
             L(outline([(56, 0), (80, 12), (90, 40), (84, 80), (64, 86), (70, 40)]), 'shade', 'b', False),
             L(quad((14, 50), (50, 66), (86, 50)), 'deep', 'b', False, False, 1.2),
             L(outline([(26, 70), (30, 62), (32, 88, 1)]), 'red', 'f', False), L(outline([(74, 70), (70, 62), (68, 88, 1)]), 'red', 'f', False)],
}

# Kaos Dao (portero): grandullón moreno con una capucha de tela blanca que le cubre la cabeza y le cae por detrás, de la
# que salen rastas negras: dos le enmarcan la cara y dos más se curvan arriba como antenas; pintura blanca en las mejillas
# y ojos pequeños de enfado
HOOD = (236, 238, 240, 255)
HOOD_D = (196, 186, 192, 255)
DREAD = (26, 24, 28, 255)
CHARS[f'{V}:kaos-dao'] = {
    'body': 'corpulento', 'pal': pal('#eceef0', '#9a6a4a', iris='#2a2440', shade='#c8bcc4', deep='#a898a4'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 98, 'hairline': [(14, 70), (22, 54), (50, 48), (78, 54), (86, 70)],
             'face_front': blob([(14, 52), (50, 36), (86, 52), (92, 76), (86, 100), (66, 110), (50, 112), (34, 110), (14, 100), (8, 76)])},
    'front': [L(outline([(4, 104), (-2, 60), (8, 26), (26, 6), (50, 0), (74, 6), (92, 26), (102, 60), (96, 104), (84, 72), (16, 72)]), HOOD, 'b'),
              L(outline([(60, 2), (90, 20), (102, 60), (96, 100), (82, 56)]), HOOD_D, 'b', False),
              L(rope((44, 8), (20, 36), (16, 100), 4), DREAD, 'f'), L(rope((48, 8), (30, 28), (28, 62), 3.4), DREAD, 'f'),
              L(rope((54, 8), (76, 30), (82, 60), 3.4), DREAD, 'f'),
              L(rope((56, 6), (90, -8), (110, 14), 3.0), DREAD, 'f'), L(rope((60, 10), (92, 6), (104, 28), 3.0), DREAD, 'f'),
              L(outline([(16, 84), (30, 80), (28, 86), (18, 90)]), WHITE, 'f', False), L(outline([(84, 84), (70, 80), (72, 86), (82, 90)]), WHITE, 'f', False)],
    'side': [L(outline([(60, 70), (58, 50), (80, 44), (90, 26), (70, 4), (40, 0), (14, 10), (-6, 30), (-24, 56), (-30, 76, 1), (-14, 70), (4, 64), (10, 90), (30, 96),
                        (44, 80)]), HOOD, 'b'),
             L(outline([(-24, 56), (4, 40), (20, 70), (10, 90), (-14, 70)]), HOOD_D, 'b', False),
             L(rope((70, 8), (96, 0), (100, 24), 3.0), DREAD, 'f'), L(rope((72, 14), (100, 14), (100, 40), 3.0), DREAD, 'f'),
             L(rope((62, 50), (56, 76), (60, 100), 3.4), DREAD, 'f'),
             L(outline([(76, 84), (86, 80), (86, 88), (78, 90)]), WHITE, 'f', False)],
    'back': [L(outline([(4, 106), (-4, 60), (6, 24), (26, 4), (50, -2), (74, 4), (94, 24), (104, 60), (96, 106), (70, 112), (50, 108), (30, 112)]), HOOD, 'b'),
             L(outline([(56, 0), (90, 20), (104, 64), (94, 104), (66, 106), (70, 50)]), HOOD_D, 'b', False),
             L(rope((90, 24), (100, 10), (112, 20), 3.0), DREAD, 'f'), L(rope((86, 30), (100, 30), (110, 44), 3.0), DREAD, 'f')],
}

# Edmond Pias: pelo negro azulado largo, peinado hacia atrás, que le cae en una melena en punta hasta la espalda, con un
# mechón suelto sobre un lado de la frente; ojos gris azulado con sombra oscura y gesto serio
CHARS[f'{V}:edmond-pias'] = {
    'body': 'normal', 'pal': pal('#1e2c38', '#fde4d4', iris='#7aa0b8', shade='#141e28', deep='#0c141c', light='#4a6070'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'line', 'mouth_y': 96,
             'hairline': [(16, 68), (18, 50), (32, 42), (50, 46), (68, 42), (82, 50), (84, 68)]},
    'front': [L(outline([(14, 98), (10, 60), (12, 30), (26, 8), (50, 0), (74, 8), (88, 30), (90, 60), (86, 98), (80, 68), (20, 68)])),
              L(outline([(60, 2), (84, 14), (92, 46), (88, 94), (80, 60)]), 'shade', 'b', False),
              strand([(36, 40), (40, 10)], 'light', 'b', 1.2), strand([(64, 40), (60, 10)], 'light', 'b', 1.2),
              fr([(24, 46), (36, 42), (30, 62), (22, 84, 1), (20, 60)])],
    'side': [L(outline([(58, 60), (62, 48), (82, 44), (92, 30), (86, 10), (64, -2), (36, 0), (14, 12), (4, 36), (4, 70), (10, 96), (20, 114, 1), (30, 94), (38, 74),
                        (48, 62)])),
             L(outline([(4, 40), (28, 46), (36, 74), (22, 110), (8, 90)]), 'shade', 'b', False),
             strand([(40, 4), (60, 20), (84, 30)], 'light', 'b', 1.2)],
    'back': [L(outline([(16, 90), (10, 60), (12, 30), (26, 8), (50, 0), (74, 8), (88, 30), (90, 60), (84, 90), (66, 104), (52, 118, 1), (46, 104), (34, 100)])),
             L(outline([(56, 2), (84, 16), (92, 50), (84, 90), (58, 110), (66, 50)]), 'shade', 'b', False),
             strand([(40, 10), (44, 60), (48, 100)], 'light', 'b', 1.2), strand([(60, 10), (58, 60), (52, 104)], 'deep', 'b', 1.0)],
}
