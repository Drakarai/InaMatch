"""Chispas Perfectas (orion-perfect-spark): Rusia en Inazuma Eleven Orion no Kokuin, con sus modelos 3D de
'イナズマイレブン オリオンの刻印' (cada uno tiene una sola forma). Yuri (Yuri Rodina) no es el Yuri de Storm Wolf: va como
'orion-perfect-spark:yuri'. Martemeli Prestov sale dos veces en la plantilla (Lus Kasim): el mismo dibujo."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, outline, pal, rope, strand  # noqa: F401
from heads import quad  # noqa: F401

WHITE = (250, 248, 240, 255)
BLUSH = (246, 150, 130, 255)


def oct_ring(cx, cy, r):
    """Montura octogonal (gafas de Marat)."""
    import math
    pts = [(cx + r * 1.08 * math.cos(math.pi / 8 + k * math.pi / 4), cy + r * 0.92 * math.sin(math.pi / 8 + k * math.pi / 4)) for k in range(8)]
    return pts + [pts[0]]


# Gregory Fortin (Goran Vecilia, portero): pañuelo verde azulado oscuro atado a la cabeza que le baja en pico hasta entre los
# ojos, con el nudo y las puntas a su derecha (izquierda de la imagen); por debajo, el pelo largo y liso rosa pálido hasta los
# hombros; piel morena, ojos gris azulado y ceño serio
CHARS['gregory-fortin'] = {
    'body': 'corpulento', 'pal': pal('#f0d4cc', '#a87650', iris='#6a8a9a', shade='#d4b0a8', deep='#b08c86', band='#2e4a4e', band_d='#203638'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'ears': False, 'hairline': False, 'nose': (50, 86, 3.4)},
    'front': [L(outline([(12, 62), (22, 62), (26, 92), (26, 120), (12, 120), (10, 92)]), 'mid', 'f'),
              L(outline([(88, 62), (78, 62), (74, 92), (74, 120), (88, 120), (90, 92)]), 'mid', 'f'),
              L(outline([(84, 64), (88, 92), (88, 120), (80, 120), (80, 90)]), 'shade', 'f', False),
              strand([(18, 70), (18, 116)], 'deep', 'f', 0.8), strand([(82, 70), (82, 116)], 'deep', 'f', 0.8),
              L(outline([(14, 64), (12, 40), (20, 16), (36, 4), (50, 2), (64, 4), (80, 16), (88, 40), (86, 64), (66, 62), (50, 74, 1), (34, 62)]), 'band', 'f'),
              L(outline([(60, 4), (80, 16), (88, 40), (86, 62), (70, 60), (76, 34)]), 'band_d', 'f', False),
              L(outline([(14, 30), (2, 22, 1), (8, 38), (2, 50, 1), (14, 44)]), 'band', 'f'),
              L(quad((18, 56), (50, 50), (82, 56)), 'band_d', 'f', False, False, 1.0)],
    'side': [L(outline([(26, 60), (8, 80), (-16, 116), (-2, 122), (20, 98), (40, 74)])), strand([(14, 78), (-6, 114)], 'deep', 'b', 0.8),
             L(outline([(58, 62), (66, 64), (70, 110, 1), (60, 100)]), 'mid', 'f'),
             L(outline([(8, 62), (4, 34), (16, 10), (40, 0), (66, 4), (84, 18), (90, 40), (90, 60), (80, 62), (60, 56), (40, 62)]), 'band', 'f'),
             L(outline([(8, 62), (4, 34), (16, 10), (30, 6), (24, 40), (18, 62)]), 'band_d', 'f', False),
             L(outline([(10, 30), (-8, 16, 1), (-2, 32), (-10, 48, 1), (8, 44)]), 'band', 'f'),
             L(quad((10, 52), (50, 48), (90, 54)), 'band_d', 'f', False, False, 1.0)],
    'back': [L(outline([(14, 66), (8, 96), (2, 124), (98, 124), (92, 96), (86, 66), (50, 74)])),
             L(outline([(56, 70), (86, 66), (92, 96), (98, 124), (64, 124)]), 'shade', 'b', False),
             *[strand([(x, 80), (x + (x - 50) * 0.15, 120)], 'deep', 'b', 0.8) for x in (26, 40, 60, 74)],
             L(outline([(14, 70), (12, 40), (20, 16), (36, 4), (50, 2), (64, 4), (80, 16), (88, 40), (86, 70), (50, 76)]), 'band'),
             L(outline([(56, 4), (80, 16), (88, 40), (86, 68), (62, 72)]), 'band_d', 'b', False),
             L(outline([(84, 34), (100, 18, 1), (96, 36), (104, 50, 1), (86, 48)]), 'band')],
}

# Leonid Largov (Alexei Trepov): melena morada larga y ondulada hasta los hombros, la frente despejada con dos mechones oscuros
# de punta encima; ojos morados afilados y sonrisa de listillo
CHARS['leonid-largov'] = {
    'body': 'delgado', 'pal': pal('#5c5498', '#f6d4a8', iris='#7a3a9a', shade='#463e7c', deep='#2e2a56'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': [(14, 70), (18, 50), (24, 44), (76, 44), (82, 50), (86, 70)]},
    'front': [L(outline([(14, 122), (6, 98), (12, 82), (2, 62), (10, 42), (12, 18), (22, 2), (36, -6), (50, -2), (64, -6), (78, 2), (88, 18), (90, 42), (98, 62),
                         (88, 82), (94, 98), (86, 122), (76, 112), (80, 92), (78, 60), (76, 44), (24, 44), (22, 60), (20, 92), (24, 112)])),
              L(outline([(64, -4), (78, 2), (88, 18), (90, 42), (98, 62), (88, 82), (94, 98), (86, 120), (80, 92), (82, 50)]), 'shade', 'b', False),
              *[strand([(x, 8), (x + d, 36)], 'deep', 'b', 1.4) for x, d in ((30, -2), (36, 0), (42, 2), (58, -2), (64, 0), (70, 2))],
              strand([(8, 70), (14, 100)], 'deep', 'b', 0.9), strand([(92, 70), (86, 100)], 'deep', 'b', 0.9)],
    'side': [L(outline([(60, 56), (70, 44), (84, 40), (90, 24), (82, 6), (60, -6), (36, -4), (16, 8), (6, 30), (4, 56), (-4, 80), (-14, 104, 1), (6, 96), (20, 110),
                        (24, 92), (36, 80), (40, 64), (50, 58)])),
             L(outline([(4, 56), (16, 40), (36, 64), (24, 92), (6, 96)]), 'shade', 'b', False),
             strand([(16, 20), (40, 6), (70, 4)], 'deep', 'b', 1.0), strand([(10, 70), (0, 96)], 'deep', 'b', 0.9)],
    'back': [L(outline([(12, 70), (-4, 96), (-6, 124), (106, 124), (104, 96), (88, 70), (50, 74)])),
             L(outline([(12, 62), (10, 36), (20, 12), (36, 0), (50, -2), (64, 0), (80, 12), (90, 36), (88, 62), (50, 70)])),
             L(outline([(56, 0), (80, 12), (90, 36), (104, 96), (106, 122), (66, 124), (60, 70)]), 'shade', 'b', False),
             *[strand([(50, 60), (x, y)], 'deep', 'b', 0.9) for x, y in ((20, 24), (34, 6), (50, 0), (66, 6), (80, 24))],
             strand([(10, 90), (8, 120)], 'deep', 'b', 0.9), strand([(90, 90), (92, 120)], 'deep', 'b', 0.9)],
}

# Boris Kaprichyov (Rabi Eremenko): gordito de cara redonda y coloretes; pelo negro corto y revuelto; ojillos azules redondos
# con tres rayitas encima por cejas, boquita y un collar de cuentas blancas grandes
BEAD = (244, 232, 222, 255)
CHARS['boris-kaprichyov'] = {
    'body': 'corpulento', 'pal': pal('#2e2a22', '#fbdcb0', iris='#2a8ac8', shade='#221e18', light='#4e4838'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'line', 'mouth_y': 94, 'hairline': [(12, 70), (18, 58), (50, 56), (82, 58), (88, 70)],
             'face_front': blob([(14, 52), (50, 44), (86, 52), (90, 76), (84, 96), (66, 106), (50, 108), (34, 106), (16, 96), (10, 76)])},
    'front': [L(outline([(12, 72), (8, 52), (14, 32), (24, 22), (36, 20), (48, 12), (56, 6), (62, 14), (76, 16), (88, 30), (92, 50), (88, 72), (82, 60), (18, 60)])),
              L(outline([(62, 14), (76, 16), (88, 30), (92, 50), (88, 70), (80, 44), (70, 26)]), 'shade', 'b', False),
              L(outline([(36, 22), (44, 18), (48, 26), (40, 30)]), 'light', 'b', False),
              *[L([(29, y), (37, y + 0.4)], OUTC, 'f', False, False, 1.0) for y in (62, 64.6, 67.2)],
              *[L([(63, y + 0.4), (71, y)], OUTC, 'f', False, False, 1.0) for y in (62, 64.6, 67.2)],
              L(ell(26, 86, 5, 3.4), BLUSH, 'f', False), L(ell(74, 86, 5, 3.4), BLUSH, 'f', False),
              *[L(ell(x, 112 - abs(x - 50) * 0.18, 6, 5), BEAD, 'f', True, True) for x in (14, 28, 42, 58, 72, 86)]],
    'side': [L(outline([(62, 56), (70, 46), (84, 44), (88, 28), (78, 12), (56, 4), (34, 6), (14, 14), (4, 34), (4, 60), (12, 74), (24, 76), (34, 66), (44, 60), (54, 58)])),
             L(outline([(4, 34), (14, 16), (28, 30), (34, 66), (24, 76), (12, 74), (4, 60)]), 'shade', 'b', False),
             L(ell(78, 86, 4, 3), BLUSH, 'f', False),
             *[L(ell(x, y, 6, 5), BEAD, 'f', True, True) for x, y in ((16, 108), (30, 112), (46, 114), (62, 114), (76, 112))]],
    'back': [L(outline([(14, 84), (10, 56), (14, 32), (26, 18), (40, 14), (50, 8), (60, 14), (76, 18), (88, 32), (90, 56), (86, 84), (50, 88)])),
             L(outline([(58, 12), (76, 18), (88, 32), (90, 56), (86, 82), (62, 86)]), 'shade', 'b', False),
             *[L(ell(x, 108 + abs(x - 50) * 0.05, 6, 5), BEAD, 'f', True, True) for x in (14, 28, 42, 58, 72, 86)]],
}

# Nikolai Glisanderov (Gwennady Zakharov): pelo rubio pálido muy corto, rapado, con el nacimiento del pelo en ángulo; mirada
# fría de ojos grises, ceño serio y aritos negros en las orejas
CHARS['nikolai-glisanderov'] = {
    'body': 'normal', 'pal': pal('#f2e2b6', '#f8d8b0', iris='#4a5a8a', shade='#d8c696', deep='#b8a676'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'frown', 'mouth_y': 95, 'hairline': [(16, 62), (20, 46), (34, 38), (50, 44), (66, 38), (80, 46), (84, 62)]},
    'front': [L(outline([(16, 64), (13, 40), (18, 18), (32, 4), (50, 0), (68, 4), (82, 18), (87, 40), (84, 64), (80, 46), (20, 46)])),
              L(outline([(60, 2), (80, 14), (87, 40), (84, 62), (78, 38)]), 'shade', 'b', False),
              L(ell(16, 82, 2.6, 2.6) + [ell(16, 82, 2.6, 2.6)[0]], OUTC, 'f', False, False, 1.2), L(ell(84, 82, 2.6, 2.6) + [ell(84, 82, 2.6, 2.6)[0]], OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(58, 56), (64, 46), (78, 40), (88, 28), (80, 10), (56, 0), (32, 2), (14, 12), (4, 32), (4, 56), (12, 70), (24, 72), (34, 62), (44, 58)])),
             L(outline([(4, 32), (14, 14), (26, 30), (34, 62), (24, 72), (12, 70), (4, 56)]), 'shade', 'b', False),
             L(ell(46, 82, 2.6, 2.6) + [ell(46, 82, 2.6, 2.6)[0]], OUTC, 'f', False, False, 1.2)],
    'back': [L(outline([(16, 78), (12, 50), (16, 26), (30, 8), (50, 2), (70, 8), (84, 26), (88, 50), (84, 78), (50, 84)])),
             L(outline([(56, 4), (76, 12), (88, 40), (84, 76), (60, 82)]), 'shade', 'b', False),
             L(ell(14, 82, 2.6, 2.6) + [ell(14, 82, 2.6, 2.6)[0]], OUTC, 'f', False, False, 1.2), L(ell(86, 82, 2.6, 2.6) + [ell(86, 82, 2.6, 2.6)[0]], OUTC, 'f', False, False, 1.2)],
}

# Igor Pitsikatov (Simon Zhitova): pelo azul marino recogido en dos moños redondos arriba con cintas amarillas y un pincho en
# medio, una coleta que sale por detrás atada con naranja y una trenza por la nuca; visera de gafas verde lima sobre los ojos y
# sonrisa enseñando los dientes
LIME = (214, 234, 112, 255)
CHARS['igor-pitsikatov'] = {
    'body': 'bajito', 'pal': pal('#2c4a68', '#fbdcb6', iris='#4a9a2a', shade='#1e3650', deep='#142438', yel='#f2c63a', tie='#e8902a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 95, 'hairline': [(14, 60), (20, 48), (80, 48), (86, 60)]},
    'front': [L(outline([(16, 62), (12, 40), (8, 22), (12, 6), (24, -4), (36, -4), (44, 2), (50, -12, 1), (56, 2), (64, -4), (76, -4), (88, 6), (92, 22), (88, 40),
                         (84, 62), (80, 48), (20, 48)])),
              L(outline([(56, -2), (66, -2), (82, 4), (90, 20), (88, 40), (84, 60), (76, 30)]), 'shade', 'b', False),
              strand([(34, 0), (32, 44)], 'deep', 'b', 1.0), strand([(66, 0), (68, 44)], 'deep', 'b', 1.0), strand([(50, 0), (50, 44)], 'deep', 'b', 0.8),
              L(outline([(10, 22), (16, 4), (22, 6), (18, 22), (14, 36)]), 'yel', 'b', False), L(outline([(90, 22), (84, 4), (78, 6), (82, 22), (86, 36)]), 'yel', 'b', False),
              L(outline([(18, 70), (30, 64), (46, 68), (50, 72), (54, 68), (70, 64), (82, 70), (80, 82), (66, 88), (54, 84), (50, 80), (46, 84), (34, 88), (20, 82)]), LIME, 'f', True, True),
              L([(28, 70), (42, 76)], (60, 140, 40, 255), 'f', False, False, 2.0), L([(72, 70), (58, 76)], (60, 140, 40, 255), 'f', False, False, 2.0),
              L([(33, 76), (38, 82)], (60, 140, 40, 255), 'f', False, False, 1.4), L([(67, 76), (62, 82)], (60, 140, 40, 255), 'f', False, False, 1.4)],
    'side': [L(rope((14, 34), (-8, 60), (2, 98), 9), 'mid'), *[L(ell(-4 + k, 46 + k * 11, 5, 5.6), 'mid', 'b', True, True) for k in range(5)],
             L(outline([(18, 20), (0, -4), (-8, -26, 1), (10, -14), (28, 10)])), L(outline([(10, 18), (20, 12), (24, 22), (14, 28)]), 'tie', 'b', False),
             L(outline([(60, 54), (68, 44), (84, 40), (90, 22), (82, 4), (62, -4), (40, -2), (20, 8), (8, 28), (6, 52), (14, 66), (26, 66), (36, 58), (48, 54)])),
             L(outline([(70, 0), (82, 4), (90, 20), (88, 34), (78, 20)]), 'yel', 'b', False),
             L(outline([(6, 34), (18, 16), (30, 34), (26, 64), (12, 64)]), 'shade', 'b', False),
             L(outline([(72, 66), (90, 64), (90, 84), (74, 84)]), LIME, 'f', True, True), L([(78, 70), (88, 74)], (60, 140, 40, 255), 'f', False, False, 1.8)],
    'back': [L(outline([(16, 76), (12, 50), (10, 24), (20, 6), (36, 0), (64, 0), (80, 6), (90, 24), (88, 50), (84, 76), (50, 82)])),
             L(outline([(56, 2), (80, 6), (90, 24), (88, 50), (84, 74), (60, 80)]), 'shade', 'b', False),
             L(outline([(12, 22), (18, 8), (24, 20), (18, 36)]), 'yel', 'b', False), L(outline([(88, 22), (82, 8), (76, 20), (82, 36)]), 'yel', 'b', False),
             L(outline([(42, 14), (40, -6), (48, -28, 1), (56, -10), (62, -16, 1), (60, 6), (58, 16)])),
             L(outline([(44, 20), (56, 20), (54, 28), (46, 28)]), 'tie', 'b', False),
             *[L(ell(50, 34 + k * 12, 6 - k * 0.5, 6.4), 'mid', 'b', True, True) for k in range(6)]],
}

# Michael Vivacer (Karl Senirov): rastas largas rojo oscuro que le caen hasta los hombros y abren a los lados, con una cinta
# verde oliva en la frente con un zigzag azul claro; piel oscura, ojos azules y cejas fruncidas
CHARS['michael-vivacer'] = {
    'body': 'normal', 'pal': pal('#5e1612', '#8a5a3c', iris='#3a8ac8', shade='#46100e', deep='#2e0a08', band='#7a7a3c', zz='#a8d4e0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': [(14, 72), (20, 62), (50, 60), (80, 62), (86, 72)]},
    'front': [L(outline([(2, 104), (-6, 76, 1), (0, 66), (-8, 50, 1), (2, 40), (10, 16), (26, 2), (50, -2), (74, 2), (90, 16), (98, 40), (108, 50, 1), (100, 66),
                         (106, 76, 1), (98, 104), (86, 104), (82, 80), (78, 60), (22, 60), (18, 80), (14, 104)])),
              L(outline([(62, 0), (90, 16), (98, 40), (108, 50), (100, 66), (106, 76), (98, 104), (86, 104), (84, 60)]), 'shade', 'b', False),
              *[strand([(x, 20), (x + (x - 50) * 0.3, 100)], 'deep', 'b', 1.0) for x in (8, 18, 30, 70, 82, 92)],
              L(outline([(22, 70), (26, 56), (30, 58), (30, 84, 1)]), 'mid', 'f'), L(outline([(78, 70), (74, 56), (70, 58), (70, 84, 1)]), 'mid', 'f'),
              L(outline([(26, 48), (50, 44), (74, 48), (74, 60), (50, 58), (26, 60)]), 'band', 'f'),
              L([(30, 56), (36, 50), (42, 56), (48, 50), (54, 56), (60, 50), (66, 56), (70, 52)], 'zz', 'f', False, False, 1.4)],
    'side': [L(outline([(64, 54), (72, 46), (86, 42), (90, 24), (80, 6), (56, -4), (30, -2), (10, 12), (0, 34), (-8, 62), (-8, 92), (0, 104, 1), (10, 96), (22, 104, 1),
                        (30, 92), (40, 98, 1), (44, 80), (40, 64), (52, 58)])),
             L(outline([(0, 34), (16, 20), (40, 64), (30, 92), (10, 96), (-8, 92), (-8, 62)]), 'shade', 'b', False),
             *[strand([(x, 10), (x - 10, 94)], 'deep', 'b', 1.0) for x in (16, 30, 46)],
             L(outline([(76, 48), (90, 44), (92, 56), (78, 60)]), 'band', 'f')],
    'back': [L(outline([(-2, 104), (-8, 76, 1), (-2, 64), (-8, 48, 1), (2, 38), (10, 16), (26, 2), (50, -2), (74, 2), (90, 16), (98, 38), (108, 48, 1), (102, 64),
                        (108, 76, 1), (102, 104), (86, 98), (70, 102), (50, 98), (30, 102), (14, 98)])),
             L(outline([(56, 0), (90, 16), (98, 38), (102, 104), (70, 102)]), 'shade', 'b', False),
             *[strand([(x, 12), (x + (x - 50) * 0.3, 98)], 'deep', 'b', 1.0) for x in (10, 22, 36, 50, 64, 78, 90)]],
}

# Konstantin Furyozov (Shamil Trubetskoy): pelo naranja largo peinado hacia atrás, liso y pegado, con rayas de peine, que le
# cae por la espalda; orejas muy grandes de soplillo; cejas naranjas gruesas fruncidas, ojos verdes y cara larga
CHARS['konstantin-furyozov'] = {
    'body': 'delgado', 'pal': pal('#e2924c', '#fcdcb4', iris='#3aa03a', shade='#c0743a', deep='#9a5a2a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'big_ears': 3, 'ear_out': 5, 'ears_front': True,
             'hairline': [(14, 70), (18, 46), (30, 38), (50, 46), (70, 38), (82, 46), (86, 70)]},
    'front': [L(outline([(14, 120), (12, 70), (14, 40), (22, 16), (36, 4), (50, 2), (64, 4), (78, 16), (86, 40), (88, 70), (86, 120), (80, 118), (80, 60), (20, 60),
                         (20, 118)])),
              L(outline([(64, 4), (78, 16), (86, 40), (88, 70), (86, 118), (80, 90), (82, 40)]), 'shade', 'b', False),
              strand([(50, 4), (50, 44)], 'deep', 'b', 1.0), strand([(38, 6), (32, 38)], 'deep', 'b', 0.9), strand([(62, 6), (68, 38)], 'deep', 'b', 0.9),
              strand([(28, 12), (20, 40)], 'light', 'b', 1.2), strand([(72, 12), (80, 40)], 'light', 'b', 1.2),
              L(outline([(24, 62), (36, 64), (46, 70), (44, 74), (34, 70), (26, 68)]), 'shade', 'f', True, True),
              L(outline([(76, 62), (64, 64), (54, 70), (56, 74), (66, 70), (74, 68)]), 'shade', 'f', True, True),
              L([(50, 76), (50, 88)], (200, 150, 120, 255), 'f', False, False, 1.0)],
    'side': [L(outline([(56, 52), (62, 42), (76, 38), (86, 28), (80, 8), (58, -2), (34, 0), (16, 10), (6, 32), (2, 62), (-6, 96), (-16, 122), (6, 120), (16, 92),
                        (26, 72), (36, 60), (46, 56)])),
             L(outline([(2, 62), (14, 40), (30, 66), (16, 92), (6, 118), (-6, 96)]), 'shade', 'b', False),
             strand([(30, 4), (60, 6), (82, 18)], 'deep', 'b', 1.0), strand([(14, 20), (50, 16)], 'light', 'b', 1.2),
             L(outline([(70, 60), (82, 62), (86, 68), (74, 68)]), 'shade', 'f', True, True)],
    'back': [L(outline([(14, 122), (12, 70), (14, 40), (22, 16), (36, 4), (50, 2), (64, 4), (78, 16), (86, 40), (88, 70), (86, 122), (50, 126)])),
             L(outline([(56, 4), (78, 16), (86, 40), (88, 70), (86, 120), (60, 124), (58, 60)]), 'shade', 'b', False),
             L(outline([(30, 12), (40, 8), (42, 18), (32, 20)]), 'light', 'b', False)],
}

# Dmitri (Viktor Sedova): pelo morado oscuro en pinchos hacia arriba con un mechón claro en medio de la frente, que baja por los
# lados de la cara y se abre en dos puntas a la altura de la barbilla; por detrás, una coleta horizontal; orejas grandes, ojos
# azules con raya marcada y media sonrisa
CHARS['dmitri'] = {
    'body': 'delgado', 'pal': pal('#4e3264', '#fcdcb4', iris='#3aa8c8', shade='#3a244c', deep='#281836', light='#e8d4e0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'big_ears': 1, 'ear_out': 4, 'ears_front': True,
             'hairline': [(16, 80), (20, 50), (32, 42), (42, 44), (46, 52), (52, 42), (70, 40), (80, 50), (84, 80)]},
    'front': [L(outline([(20, 96), (2, 106, 1), (14, 92), (16, 70), (12, 46), (14, 20), (18, 0), (24, -16, 1), (32, 0), (40, -20, 1), (50, -2), (58, -18, 1), (64, 0),
                         (76, -12, 1), (82, 14), (88, 46), (84, 70), (86, 92), (98, 106, 1), (80, 96), (80, 60), (20, 60)])),
              L(outline([(58, -18), (64, 0), (76, -12), (82, 14), (88, 46), (84, 70), (86, 92), (80, 80), (80, 40), (70, 14)]), 'shade', 'b', False),
              L(outline([(44, 4), (52, 0), (50, 30), (46, 52, 1), (44, 30)]), 'light', 'b', False),
              strand([(30, 4), (28, 40)], 'deep', 'b', 1.0), strand([(64, 4), (68, 40)], 'deep', 'b', 1.0)],
    'side': [L(outline([(62, 54), (70, 44), (84, 40), (90, 26), (84, 4), (80, -14, 1), (66, -4), (56, -20, 1), (44, -6), (24, -12, 1), (20, 6), (8, 24), (4, 50), (8, 66),
                        (-18, 80), (-28, 102, 1), (-6, 92), (10, 92), (24, 80), (36, 62), (48, 56)])),
             L(outline([(4, 50), (14, 30), (30, 50), (24, 80), (10, 92), (-6, 92), (-18, 80), (8, 66)]), 'shade', 'b', False),
             L(outline([(66, -4), (80, -14), (84, 4), (74, 14)]), 'light', 'b', False),
             L(outline([(60, 56), (66, 58), (68, 90), (74, 100, 1), (62, 92)]), 'mid', 'f')],
    'back': [L(outline([(22, 106), (6, 114, 1), (18, 96), (16, 70), (12, 46), (14, 20), (20, 0), (26, -14, 1), (34, 0), (42, -18, 1), (50, -2), (58, -16, 1), (64, 0),
                        (76, -10, 1), (82, 16), (88, 46), (84, 70), (82, 96), (94, 114, 1), (78, 106), (50, 102)])),
             L(outline([(56, -4), (64, 0), (76, -10), (82, 16), (88, 46), (84, 70), (82, 96), (78, 104), (60, 100)]), 'shade', 'b', False)],
}

# Alexander Allegrov (Froy Girikanan): pelo blanco en pinchos revueltos con sombras lila y un mechón azul a su derecha (la
# izquierda de la imagen); flequillo de pinchos que le cae por la frente; ojos
# azules y sonrisa tranquila
CHARS['alexander-allegrov'] = {
    'body': 'normal', 'pal': pal('#eef2fa', '#fcd8b4', iris='#3a9ad0', shade='#c8bcd4', deep='#9a8cac', streak='#7a92e0'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 93, 'hairline': [(14, 72), (18, 54), (30, 50), (44, 56), (50, 60), (56, 54), (70, 50), (82, 54), (86, 72)]},
    'front': [L(outline([(16, 76), (8, 68, 1), (14, 58), (0, 48, 1), (12, 40), (-4, 26, 1), (14, 20), (8, 4, 1), (24, 6), (28, -14, 1), (40, 0), (52, -20, 1), (58, -2),
                         (72, -10, 1), (76, 6), (94, 8, 1), (86, 22), (102, 32, 1), (88, 40), (98, 52, 1), (86, 58), (90, 70, 1), (84, 76), (80, 60), (20, 60)])),
              L(outline([(58, -2), (72, -10), (76, 6), (94, 8), (86, 22), (102, 32), (88, 40), (98, 52), (86, 58), (90, 70), (84, 74), (80, 40), (68, 20)]), 'shade', 'b', False),
              L(outline([(14, 58), (0, 48), (12, 40), (24, 50), (20, 70), (16, 76), (8, 68)]), 'shade', 'b', False),
              L(outline([(22, 44), (28, 60, 1), (34, 48), (42, 64, 1), (48, 48), (52, 66, 1), (58, 48), (66, 62, 1), (72, 46), (80, 58, 1), (82, 40), (66, 32), (48, 32), (32, 34)]),
                'mid', 'f'),
              L(outline([(66, 48), (72, 46), (80, 58), (82, 42)]), 'shade', 'f', False),
              L(outline([(24, -10), (32, -8), (36, 20), (38, 42), (32, 36), (28, 14)]), 'streak', 'f')],
    'side': [L(outline([(62, 56), (70, 46), (86, 44), (92, 30), (98, 14, 1), (86, 14), (92, -4, 1), (74, 4), (72, -16, 1), (58, -2), (40, -14, 1), (34, 2), (14, -4, 1),
                        (16, 12), (-4, 16, 1), (8, 28), (-10, 40, 1), (6, 48), (-6, 62, 1), (8, 66), (2, 82, 1), (16, 78), (20, 92, 1), (28, 78), (40, 64), (52, 58)])),
             L(outline([(6, 48), (24, 40), (40, 64), (28, 78), (16, 78), (8, 66)]), 'shade', 'b', False),
             L(outline([(28, 22), (60, 20), (44, 36)]), 'shade', 'b', False),
             L(outline([(84, 14), (92, -4), (96, -24, 1), (98, -2), (92, 16)]), 'streak', 'b'),
             L(outline([(78, 46), (88, 44), (94, 58, 1), (82, 54)]), 'mid', 'f')],
    'back': [L(outline([(24, 98), (16, 86, 1), (16, 74), (4, 66, 1), (10, 56), (-6, 46, 1), (8, 38), (-2, 22, 1), (16, 18), (14, 2, 1), (30, 6), (40, -14, 1), (50, 2),
                        (64, -10, 1), (68, 6), (86, 2, 1), (84, 18), (104, 26, 1), (90, 38), (106, 50, 1), (90, 58), (98, 70, 1), (84, 76), (86, 90, 1), (74, 92),
                        (64, 100, 1), (56, 94), (48, 102, 1), (40, 94), (32, 102, 1)])),
             L(outline([(16, 40), (30, 26), (50, 30), (70, 22), (90, 36), (88, 80), (70, 90), (50, 96), (30, 92), (14, 76)]), 'shade', 'b', False),
             L(outline([(40, 34), (50, 30), (52, 40), (42, 42)]), 'mid', 'b', False)],
}

# Anton Kolosalyov (Zaur Salenko): grandullón de mandíbula cuadrada; los lados rapados castaño claro y arriba un mechón revuelto
# blanco crema que baja por la nuca en una trenza; una cicatriz de dos tajos en la frente; ojos hundidos con sombra oscura y
# pupilas azules, nariz cuadrada y boca recta
DARKEYE = (70, 44, 46, 255)
CHARS['anton-kolosalyov'] = {
    'body': 'corpulento', 'pal': pal('#f4ece0', '#fbdcb0', iris='#3a5aa8', shade='#dcc4c0', deep='#b49a98', shave='#ae9070', shave_d='#8c7258'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': [(14, 66), (20, 40), (30, 28), (70, 28), (80, 40), (86, 66)],
             'face_front': blob([(14, 50), (50, 40), (86, 50), (90, 76), (86, 100), (70, 110), (50, 112), (30, 110), (14, 100), (10, 76)])},
    'front': [L(outline([(14, 66), (12, 34), (20, 18), (80, 18), (88, 34), (86, 66), (80, 40), (20, 40)]), 'shave'),
              L(outline([(62, 18), (80, 18), (88, 34), (86, 64), (80, 38)]), 'shave_d', 'b', False),
              L(outline([(30, 22), (32, 8), (38, -6, 1), (44, 4), (50, -14, 1), (56, 2), (64, -8, 1), (66, 8), (70, 22), (50, 26)])),
              L(outline([(54, 0), (64, -8), (66, 8), (70, 20), (58, 22)]), 'shade', 'b', False),
              L([(36, 48), (54, 34)], (80, 50, 44, 255), 'f', False, False, 2.4), L([(42, 52), (60, 38)], (80, 50, 44, 255), 'f', False, False, 2.4),
              L([(22, 68), (46, 70)], OUTC, 'f', False, False, 2.6), L([(78, 68), (54, 70)], OUTC, 'f', False, False, 2.6),
              L(outline([(24, 72), (44, 72), (42, 79), (28, 79)]), DARKEYE, 'f', False), L(outline([(76, 72), (56, 72), (58, 79), (72, 79)]), DARKEYE, 'f', False),
              L(ell(36, 75.5, 1.6, 1.8), (110, 140, 230, 255), 'f', False), L(ell(64, 75.5, 1.6, 1.8), (110, 140, 230, 255), 'f', False),
              L([(46, 78), (46, 86), (42, 90), (58, 90), (54, 86), (54, 78)], OUTC, 'f', False, False, 1.1),
              L([(36, 100), (64, 100)], OUTC, 'f', False, False, 1.8)],
    'side': [L(rope((10, 20), (-10, 50), (-4, 84), 8), 'mid'), *[L(ell(-6 + k * 0.6, 34 + k * 11, 5, 5.6), 'mid', 'b', True, True) for k in range(5)],
             L(outline([(60, 56), (66, 44), (80, 40), (88, 28), (84, 12), (60, 4), (34, 6), (14, 14), (4, 34), (4, 58), (12, 72), (26, 74), (36, 62), (48, 58)]), 'shave'),
             L(outline([(4, 34), (14, 14), (28, 28), (34, 62), (26, 72), (12, 72), (4, 58)]), 'shave_d', 'b', False),
             L(outline([(20, 12), (24, -2, 1), (34, 4), (44, -14, 1), (52, 2), (64, -8, 1), (70, 6), (80, 0, 1), (82, 14), (50, 12)])),
             L([(70, 68), (86, 70)], OUTC, 'f', False, False, 2.6), L(outline([(74, 72), (86, 72), (86, 79), (76, 79)]), DARKEYE, 'f', False),
             L(ell(82, 75.5, 1.4, 1.8), (110, 140, 230, 255), 'f', False)],
    'back': [L(outline([(16, 80), (12, 50), (16, 24), (30, 10), (50, 6), (70, 10), (84, 24), (88, 50), (84, 80), (50, 84)]), 'shave'),
             L(outline([(58, 8), (76, 14), (88, 40), (84, 78), (62, 82)]), 'shave_d', 'b', False),
             L(outline([(38, 12), (40, -2, 1), (46, 4), (50, -14, 1), (56, 2), (62, -4, 1), (64, 12), (50, 16)])),
             *[L(ell(50, 18 + k * 12, 7 - k * 0.6, 6.6), 'mid', 'b', True, True) for k in range(6)],
             L(outline([(46, 88), (54, 88), (52, 104, 1), (48, 104, 1)]), 'mid', 'b', True, True)],
}

# Yuri (Yuri Rodina): pelo rubio largo con dos mechones lisos que le caen por delante hasta el pecho y una coleta baja atada
# con una goma azul; flequillo de lado con un rizo en la frente; ojos azul verdoso grandes y pendientes azules
TEAL = (52, 160, 176, 255)
CHARS['orion-perfect-spark:yuri'] = {
    'body': 'delgado', 'pal': pal('#f4cc90', '#fcdcbc', iris='#2a9ab0', shade='#dcae70', deep='#bc8e56'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': [(14, 80), (20, 56), (32, 44), (50, 40), (68, 44), (80, 56), (86, 80)]},
    'front': [L(outline([(12, 120), (10, 70), (14, 32), (26, 10), (50, 2), (74, 10), (86, 32), (90, 70), (88, 120), (78, 120), (78, 70), (22, 70), (22, 120)])),
              L(outline([(64, 6), (80, 14), (88, 36), (90, 70), (88, 118), (82, 90), (82, 44)]), 'shade', 'b', False),
              L(outline([(14, 60), (22, 60), (24, 120), (13, 120)]), 'mid', 'f'), L(outline([(86, 60), (78, 60), (76, 120), (87, 120)]), 'mid', 'f'),
              L(outline([(80, 64), (86, 64), (87, 120), (80, 120)]), 'shade', 'f', False),
              L(outline([(22, 52), (30, 36), (46, 28), (60, 30), (72, 40), (78, 54), (66, 44), (58, 52), (56, 62, 1), (52, 48), (44, 44), (32, 50), (26, 60)]), 'mid', 'f'),
              L(outline([(56, 34), (66, 40), (60, 46)]), 'shade', 'f', False),
              L(outline([(14, 84), (17, 86), (17, 92), (14, 94), (11, 92), (11, 86)]), TEAL, 'f', False, True),
              L(outline([(86, 84), (89, 86), (89, 92), (86, 94), (83, 92), (83, 86)]), TEAL, 'f', False, True)],
    'side': [L(outline([(16, 70), (4, 96), (-4, 112, 1), (10, 104), (20, 116, 1), (22, 92), (26, 76)])),
             L(outline([(62, 54), (70, 44), (84, 40), (90, 22), (80, 6), (56, -2), (32, 0), (14, 12), (4, 34), (4, 58), (12, 74), (26, 76), (36, 64), (48, 58)])),
             L(outline([(4, 34), (14, 16), (28, 30), (34, 62), (26, 74), (12, 72), (4, 58)]), 'shade', 'b', False),
             L(outline([(12, 70), (26, 72), (24, 80), (12, 78)]), TEAL, 'b', False),
             L(outline([(62, 56), (70, 58), (72, 118), (64, 118)]), 'mid', 'f'),
             L(outline([(46, 84), (49, 86), (49, 92), (46, 94), (43, 92), (43, 86)]), TEAL, 'f', False, True)],
    'back': [L(outline([(40, 90), (60, 90), (62, 110), (56, 124, 1), (44, 124, 1), (38, 110)])),
             L(outline([(16, 88), (12, 60), (14, 32), (26, 10), (50, 2), (74, 10), (86, 32), (88, 60), (84, 88), (62, 94), (50, 96), (38, 94)])),
             L(outline([(56, 4), (76, 12), (88, 40), (84, 86), (60, 92)]), 'shade', 'b', False), strand([(50, 4), (50, 30)], 'deep', 'b', 0.9),
             L(outline([(42, 92), (58, 92), (58, 98), (42, 98)]), TEAL, 'b', False, True),
             L(outline([(12, 80), (20, 84), (20, 118), (12, 116)])), L(outline([(88, 80), (80, 84), (80, 118), (88, 116)]))],
}

# Molev Misterioski (Lasker Vagner): piel oscura; pelo blanco crema enorme en capas como tejas, que le tapa toda la frente y los
# ojos, con mechones largos a los lados hasta el cuello; solo se le ve la boca
CHARS['molev-misterioski'] = {
    'body': 'normal', 'pal': pal('#eee4dc', '#6a4232', iris='#2a1e1a', shade='#cbb6b4', deep='#a08886'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 95, 'ears': False, 'hairline': False},
    'front': [L(outline([(10, 80), (18, 86), (18, 112, 1), (8, 100)]), 'mid', 'f'), L(outline([(90, 80), (82, 86), (82, 112, 1), (92, 100)]), 'mid', 'f'),
              L(outline([(4, 90), (-2, 70), (2, 48), (10, 32), (28, 22), (44, 18), (50, 8), (56, 18), (72, 22), (90, 32), (98, 48), (102, 70), (96, 90), (88, 86),
                         (86, 84), (66, 86), (50, 88), (34, 86), (14, 84), (12, 86)]), 'mid', 'f'),
              L(outline([(60, 20), (90, 32), (98, 48), (102, 70), (96, 88), (88, 84), (84, 60), (72, 40)]), 'shade', 'f', False),
              L(quad((2, 50), (50, 36), (98, 50)), 'deep', 'f', False, False, 1.0), L(quad((0, 70), (50, 58), (100, 70)), 'deep', 'f', False, False, 1.0),
              *[L([(x, 70 - abs(x - 50) * 0.1), (x, 86)], 'deep', 'f', False, False, 1.0) for x in (26, 38, 50, 62, 74)],
              *[L([(x, 38 - abs(x - 50) * 0.12), (x + (x - 50) * 0.1, 56)], 'deep', 'f', False, False, 0.9) for x in (20, 36, 64, 80)]],
    'side': [L(outline([(70, 84), (78, 90), (76, 110, 1), (66, 96)]), 'mid', 'f'),
             L(outline([(92, 84), (98, 66), (94, 48), (82, 30), (56, 18), (30, 22), (10, 34), (-2, 54), (2, 76), (20, 86), (40, 80), (60, 86)]), 'mid', 'f'),
             L(outline([(-2, 54), (10, 40), (30, 60), (20, 86), (2, 76)]), 'shade', 'f', False),
             L(quad((4, 48), (50, 30), (94, 50)), 'deep', 'f', False, False, 1.0), L(quad((0, 70), (50, 56), (98, 68)), 'deep', 'f', False, False, 1.0)],
    'back': [L(outline([(10, 82), (18, 90), (18, 112, 1), (8, 100)])), L(outline([(90, 82), (82, 90), (82, 112, 1), (92, 100)])),
             L(outline([(6, 88), (-2, 70), (2, 48), (10, 32), (28, 22), (44, 18), (50, 8), (56, 18), (72, 22), (90, 32), (98, 48), (102, 70), (94, 88), (50, 90)])),
             L(outline([(58, 20), (90, 32), (98, 48), (102, 70), (94, 86), (60, 88)]), 'shade', 'b', False),
             L(quad((2, 50), (50, 40), (98, 50)), 'deep', 'b', False, False, 1.0), L(quad((0, 70), (50, 62), (100, 70)), 'deep', 'b', False, False, 1.0),
             *[L([(x, 40), (x, 56)], 'deep', 'b', False, False, 0.9) for x in (30, 50, 70)]],
}

# Marat Stakatov (Marl Marat, "Bellota"): el pelo como el sombrerete de una bellota, un casquete marrón granate con rayas que
# acaba en el borde de la frente y un rizo arriba; por debajo, la nuca rapada; gafas verdes octogonales, cejas fruncidas,
# coloretes y una sonrisa pícara enseñando los dientes
GREEN = (72, 150, 88, 255)
CHARS['marat-stakatov'] = {
    'body': 'bajito', 'pal': pal('#603c44', '#fcdcbc', iris='#2a1e1a', shade='#4a2c34', deep='#341e24', nape='#7a5444'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 94, 'hairline': [(10, 58), (50, 58), (90, 58)]},
    'front': [L(outline([(10, 56), (8, 34), (14, 14), (30, 2), (50, -2), (70, 2), (86, 14), (92, 34), (90, 56), (50, 60)])),
              L(outline([(62, 0), (86, 14), (92, 34), (90, 54), (76, 56), (78, 24)]), 'shade', 'b', False),
              L(outline([(10, 44), (50, 48), (90, 44), (90, 56), (50, 60), (10, 56)]), 'shade', 'b', False),
              *[strand([(x, 4 + abs(x - 50) * 0.2), (x + (x - 50) * 0.1, 56)], 'deep', 'b', 1.0) for x in (24, 38, 50, 62, 76)],
              L(outline([(46, 0), (44, -10), (50, -20, 1), (50, -10), (54, 0)])),
              L(oct_ring(36, 75, 9), GREEN, 'f', False, False, 2.4), L(oct_ring(64, 75, 9), GREEN, 'f', False, False, 2.4),
              L([(45, 74), (55, 74)], GREEN, 'f', False, False, 1.8),
              L(ell(26, 88, 4, 2.6), BLUSH, 'f', False), L(ell(74, 88, 4, 2.6), BLUSH, 'f', False)],
    'side': [L(outline([(10, 56), (14, 80), (26, 88), (38, 76), (44, 60)]), 'nape'),
             L(outline([(2, 58), (2, 36), (12, 14), (34, 0), (60, -2), (82, 8), (94, 28), (96, 56), (50, 62)])),
             L(outline([(2, 46), (50, 50), (96, 46), (96, 56), (50, 62), (2, 58)]), 'shade', 'b', False),
             *[strand([(x, 4), (x, 56)], 'deep', 'b', 1.0) for x in (24, 44, 64, 82)],
             L(outline([(46, 0), (40, -10), (46, -20, 1), (48, -8), (54, -2)])),
             L(ell(88, 75, 2.6, 7) + [ell(88, 75, 2.6, 7)[0]], GREEN, 'f', False, False, 2.4), L([(86, 72), (54, 70)], GREEN, 'f', False, False, 1.6),
             L(ell(78, 88, 4, 2.6), BLUSH, 'f', False)],
    'back': [L(outline([(18, 58), (18, 86), (50, 92), (82, 86), (82, 58)]), 'nape'),
             L(outline([(10, 58), (8, 36), (14, 14), (30, 2), (50, -2), (70, 2), (86, 14), (92, 36), (90, 58), (50, 62)])),
             L(outline([(10, 46), (50, 50), (90, 46), (90, 58), (50, 62), (10, 58)]), 'shade', 'b', False),
             *[strand([(x, 4 + abs(x - 50) * 0.2), (x, 58)], 'deep', 'b', 1.0) for x in (24, 38, 50, 62, 76)],
             L(outline([(46, 0), (44, -10), (50, -20, 1), (50, -10), (54, 0)]))],
}

# Martemeli Prestov (Lus Kasim): pelo beis claro en pinchos, uno alto arriba y dos que salen de lado sobre las orejas, con el
# flequillo echado a la derecha de la imagen; ojos azules afilados y ceño fruncido
CHARS['martemeli-prestov'] = {
    'body': 'bajito', 'pal': pal('#e6dec6', '#fcdcbc', iris='#3a6ac0', shade='#c4b49c', deep='#9e8c76'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': [(14, 72), (18, 56), (30, 50), (46, 56), (60, 50), (74, 54), (84, 60), (86, 72)]},
    'front': [L(outline([(16, 76), (12, 64), (-6, 58, 1), (12, 50), (12, 32), (-2, 24, 1), (16, 22), (26, 10), (34, -12, 1), (42, 4), (56, 2), (74, 8), (86, 22),
                         (100, 26, 1), (90, 32), (90, 52), (106, 60, 1), (88, 64), (86, 76), (80, 60), (20, 60)])),
              L(outline([(56, 2), (74, 8), (86, 22), (100, 26), (90, 32), (90, 52), (106, 60), (88, 64), (86, 74), (80, 44), (70, 22)]), 'shade', 'b', False),
              L(outline([(20, 52), (26, 38), (44, 30), (64, 32), (80, 42), (86, 62), (76, 54), (72, 68, 1), (66, 52), (56, 64, 1), (52, 50), (40, 60, 1), (36, 48),
                         (26, 60, 1)]), 'mid', 'f'),
              L(outline([(44, 34), (64, 36), (80, 46), (72, 50), (60, 42)]), 'shade', 'f', False),
              strand([(30, 40), (40, 50)], 'deep', 'f', 0.8)],
    'side': [L(outline([(62, 56), (70, 46), (84, 44), (90, 26), (80, 8), (62, 0), (56, -14, 1), (48, 0), (26, 6), (10, 20), (4, 40), (6, 60), (-4, 70, 1), (14, 70),
                        (26, 76), (36, 64), (48, 58)])),
             L(outline([(4, 40), (14, 22), (30, 36), (36, 64), (26, 76), (14, 70), (6, 60)]), 'shade', 'b', False),
             L(outline([(46, 12), (58, 4), (60, 22), (50, 26)]), 'shade', 'b', False),
             L(outline([(76, 46), (86, 44), (92, 60, 1), (82, 56)]), 'mid', 'f')],
    'back': [L(outline([(18, 86), (12, 70), (-6, 64, 1), (12, 56), (12, 34), (2, 22, 1), (18, 22), (30, 8), (50, 2), (54, -12, 1), (60, 4), (76, 10), (88, 24),
                        (100, 26, 1), (90, 36), (90, 56), (106, 64, 1), (88, 70), (82, 86), (70, 82), (62, 90, 1), (54, 82), (46, 90, 1), (38, 82), (30, 90, 1)])),
             L(outline([(20, 50), (40, 40), (60, 36), (88, 40), (88, 72), (70, 82), (50, 86), (30, 84), (16, 72)]), 'shade', 'b', False)],
}
CHARS['martemeli-prestov-ok-lus'] = CHARS['martemeli-prestov']

# Oleg Animatov (Malik Kuabel): melena naranja en forma de champiñón con la raya en medio, que le tapa las orejas y cae en
# mechones a los lados de la cara hasta los ojos; ojos azules grandes y sonrisa confiada
CHARS['oleg-animatov'] = {
    'body': 'normal', 'pal': pal('#ea8c5a', '#fcdcbc', iris='#3a8ac8', shade='#c86e42', deep='#a0522e'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 93, 'ears': False,
             'hairline': [(16, 80), (22, 56), (34, 42), (46, 38), (50, 42), (54, 38), (66, 42), (78, 56), (84, 80)]},
    'front': [L(outline([(14, 82), (4, 62), (4, 36), (14, 12), (32, 0), (50, -4), (68, 0), (86, 12), (96, 36), (96, 62), (86, 82), (80, 70), (20, 70)])),
              L(outline([(62, 0), (86, 12), (96, 36), (96, 62), (86, 80), (82, 56), (76, 30)]), 'shade', 'b', False),
              strand([(50, -2), (50, 40)], 'deep', 'b', 1.0), strand([(36, 2), (26, 50)], 'deep', 'b', 0.9), strand([(64, 2), (74, 50)], 'deep', 'b', 0.9),
              strand([(18, 20), (10, 60)], 'deep', 'b', 0.9), strand([(82, 20), (90, 60)], 'deep', 'b', 0.9),
              L(outline([(22, 52), (30, 46), (32, 76, 1), (24, 68)]), 'mid', 'f'), L(outline([(78, 52), (70, 46), (68, 76, 1), (76, 68)]), 'shade', 'f')],
    'side': [L(outline([(66, 66), (84, 58), (94, 36), (84, 10), (60, -6), (34, -6), (12, 6), (0, 30), (0, 58), (8, 74), (30, 78), (40, 70), (48, 64), (58, 66)])),
             L(outline([(0, 40), (16, 24), (40, 50), (30, 78), (8, 74), (0, 58)]), 'shade', 'b', False),
             *[strand([(x, 0), (x - 6, 70)], 'deep', 'b', 1.0) for x in (24, 46, 66)]],
    'back': [L(outline([(14, 82), (4, 62), (4, 36), (14, 12), (32, 0), (50, -4), (68, 0), (86, 12), (96, 36), (96, 62), (86, 82), (66, 86), (50, 88), (34, 86)])),
             L(outline([(54, -2), (86, 12), (96, 36), (96, 62), (86, 82), (60, 86)]), 'shade', 'b', False),
             *[strand([(x, 4 + abs(x - 50) * 0.2), (x + (x - 50) * 0.15, 84)], 'deep', 'b', 1.0) for x in (22, 36, 50, 64, 78)]],
}
