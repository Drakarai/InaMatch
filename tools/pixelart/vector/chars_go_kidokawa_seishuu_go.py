"""Instituto Kirkwood (GO) (go-kidokawa-seishuu-go): sus modelos 3D de Inazuma Eleven GO como referencia (busto de frente,
perfil y espalda); Flynt Pine y Calder Elm, que no tienen modelo, de sus retratos."""
from chars import CHARS, L, OUTC, ell, outline, pal, strand
from chars_bigwaves import bald
from heads import quad

WHITE = (250, 250, 250, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Strom Boojum (portero): melena verde oliva larga y lisa que le cae por los lados hasta el pecho, con una cresta de tres
# mechones gruesos en punta en lo alto; ojos rojos de loco y una sonrisa enorme de dientes
CHARS['strom-boojum'] = {
    'body': 'normal', 'pal': pal('#6a7020', '#f6c898', iris='#a01e2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 100, 'hairline': False, 'big_ears': 2},
    'front': [L(outline([(8, 124), (0, 70), (4, 34), (16, 10), (50, 0), (84, 10), (96, 34), (100, 70), (92, 124), (82, 124), (82, 66), (18, 66), (18, 124)])),
              L(outline([(62, 2), (88, 14), (98, 60), (90, 120), (82, 120), (82, 50)]), 'shade', 'b', False),
              fringe([(26, 52), (22, 20), (30, -10, 1), (38, 10), (50, -24, 1), (62, 10), (70, -10, 1), (78, 20), (74, 52), (60, 44), (50, 62, 1), (40, 44)]),
              L(outline([(44, 0), (50, -14), (56, 0), (52, 30)]), 'light', 'f', False),
              strand([(36, 12), (40, 44)], 'shade', 'f', 1.0), strand([(64, 12), (60, 44)], 'shade', 'f', 1.0)],
    'side': [L(outline([(56, 56), (66, 46), (84, 44), (92, 28), (84, 8), (90, -14, 1), (66, -4), (40, -2), (16, 10), (2, 40), (-6, 90), (-16, 124, 1), (10, 112),
                        (30, 124, 1), (40, 96), (48, 76)])),
             L(outline([(-4, 50), (18, 50), (28, 116), (-10, 118)]), 'shade', 'b', False),
             fringe([(68, 6), (90, 20), (96, 42), (92, 60, 1), (84, 46), (76, 36)])],
    'back': [L(outline([(6, 124), (-2, 70), (2, 34), (16, 10), (34, 2), (34, -14, 1), (44, 0), (50, -20, 1), (56, 0), (66, -14, 1), (66, 2), (84, 10), (98, 34),
                        (102, 70), (94, 124)])),
             L(outline([(56, 2), (88, 14), (100, 60), (94, 120), (64, 120)]), 'shade', 'b', False)],
}

# Dock Hickory: pelo castaño con un tupé altísimo que sube en punta desde la frente y mechones en punta a los lados y la
# nuca; ojos redondos de pasmo
CHARS['dock-hickory'] = {
    'body': 'delgado', 'pal': pal('#9a5a24', '#fcd8b4', iris='#1e1414'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 76), (2, 66, 1), (10, 52), (6, 30), (18, 12), (40, 4), (44, -34, 1), (60, 0), (82, 10), (94, 30), (90, 52), (98, 66, 1), (86, 76),
                         (82, 58), (18, 58)])),
              L(outline([(54, -4), (80, 10), (92, 40), (86, 66), (78, 40)]), 'shade', 'b', False),
              L(outline([(44, -26), (48, 2), (40, 4)]), 'light', 'b', False),
              fringe([(14, 62), (16, 38), (30, 22), (50, 18), (70, 22), (84, 38), (86, 62), (78, 50), (70, 58, 1), (62, 46), (52, 56, 1), (46, 44), (36, 54, 1),
                      (24, 48)])],
    'side': [L(outline([(54, 60), (60, 48), (82, 46), (92, 30), (84, 8), (96, -24, 1), (66, -8), (54, 0), (30, 0), (12, 10), (2, 34), (-8, 48, 1), (4, 54), (0, 76, 1),
                        (14, 72), (22, 84, 1), (30, 72), (46, 70)])),
             L(outline([(2, 34), (24, 40), (26, 68), (8, 62)]), 'shade', 'b', False),
             fringe([(64, 4), (88, 16), (94, 40), (90, 56, 1), (84, 42), (76, 32)])],
    'back': [L(outline([(14, 80), (0, 70, 1), (10, 54), (6, 30), (18, 12), (40, 4), (46, -30, 1), (60, 0), (82, 10), (94, 30), (90, 54), (100, 70, 1), (86, 80),
                        (50, 88)])),
             L(outline([(56, 0), (82, 12), (94, 40), (86, 76), (62, 84)]), 'shade', 'b', False)],
}

# Bourne Birch: grandullón con el pelo verde oscuro de mechones gruesos en punta levantados como una corona y patillas
# largas en punta; cejas enormes y pobladas y los dientes apretados
CHARS['bourne-birch'] = {
    'body': 'corpulento', 'pal': pal('#3e6020', '#f6c898', iris='#1e1414', brow='#3e6020'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 100, 'hairline': False, 'big_ears': 2},
    'front': [L(outline([(12, 96), (6, 84, 1), (14, 70), (8, 50), (-4, 40, 1), (10, 34), (4, 12, 1), (22, 18), (26, -6, 1), (40, 10), (50, -14, 1), (60, 10), (74, -6, 1),
                         (78, 18), (96, 12, 1), (90, 34), (104, 40, 1), (92, 50), (86, 70), (94, 84, 1), (88, 96), (82, 66), (18, 66)])),
              L(outline([(60, 4), (84, 16), (94, 42), (86, 84), (80, 50)]), 'shade', 'b', False),
              fringe([(16, 56), (20, 40), (34, 30), (50, 28), (66, 30), (80, 40), (84, 56), (72, 50), (64, 54, 1), (58, 46), (50, 54, 1), (42, 46), (36, 54, 1),
                      (28, 50)]),
              L(outline([(24, 66), (40, 62), (44, 70), (28, 72)]), 'brow', 'f', ln=True), L(outline([(76, 66), (60, 62), (56, 70), (72, 72)]), 'brow', 'f', ln=True)],
    'side': [L(outline([(56, 58), (62, 48), (84, 44), (96, 26), (100, 4, 1), (78, 10), (70, -10, 1), (54, 4), (34, 2), (14, 10), (4, 30), (6, 60), (20, 70), (40, 68)])),
             L(outline([(70, 52), (78, 52), (82, 86, 1), (72, 76)])),
             L(outline([(4, 30), (24, 36), (26, 64), (8, 58)]), 'shade', 'b', False),
             L(outline([(76, 62), (90, 62), (90, 70), (78, 70)]), 'brow', 'f', ln=True)],
    'back': [L(outline([(12, 96), (6, 84, 1), (14, 70), (8, 50), (-6, 40, 1), (10, 32), (4, 8, 1), (24, 14), (30, -8, 1), (42, 8), (50, -12, 1), (58, 8), (70, -8, 1),
                        (76, 14), (96, 8, 1), (90, 32), (106, 40, 1), (92, 50), (86, 70), (94, 84, 1), (88, 96), (76, 70), (50, 74), (24, 70)])),
             L(outline([(56, 6), (84, 16), (94, 44), (84, 70), (60, 72)]), 'shade', 'b', False)],
}

# Flynt Pine (sin modelo 3D; de su retrato): cabeza rapada con una cresta morada que sube en pico desde la frente; ceño
# fruncido
CHARS['flynt-pine'] = {
    'body': 'normal', 'pal': pal('#7a3a7a', '#fcd8b4', iris='#1e1414'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False, 'big_ears': 2},
    'front': bald('front') + [L(outline([(36, 40), (34, 10), (42, -10), (58, -26, 1), (62, 0), (64, 20), (62, 40), (50, 44)]), 'mid', 'f', ln=True),
                              L(outline([(50, 0), (58, -18), (60, 10), (56, 36)]), 'shade', 'f', False)],
    'side': bald('side') + [L(outline([(80, 40), (70, 8), (50, -6), (40, -24, 1), (34, -2), (14, 12), (6, 30), (24, 22), (48, 20), (68, 34)]), 'mid', 'f', ln=True)],
    'back': bald('back') + [L(outline([(42, 20), (40, -4), (50, -18, 1), (60, -4), (58, 20), (56, 60), (50, 70), (44, 60)]), 'mid', 'f', ln=True)],
}

# Trent Poplar: media melena castaño dorado lisa en forma de casco, con flequillo de mechones sobre los ojos y las puntas
# hacia dentro a la altura de la mandíbula; ojos apretados y los dientes al aire
CHARS['trent-poplar'] = {
    'body': 'normal', 'pal': pal('#a07a10', '#fcd8b4', iris='#1e1414'),
    'face': {'eyes': 'closed', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(14, 100), (4, 92), (0, 60), (6, 26), (24, 6), (50, 0), (76, 6), (94, 26), (100, 60), (96, 92), (86, 100), (84, 66), (16, 66)])),
              L(outline([(60, 4), (86, 16), (98, 56), (92, 94), (84, 60)]), 'shade', 'b', False),
              fringe([(12, 72), (12, 40), (26, 20), (50, 12), (74, 20), (88, 40), (88, 72), (82, 62), (76, 70, 1), (68, 50), (60, 62, 1), (54, 44), (48, 72, 1),
                      (42, 46), (34, 62, 1), (28, 50), (20, 66, 1)])],
    'side': [L(outline([(54, 62), (60, 50), (82, 50), (94, 34), (90, 12), (68, -2), (40, -4), (16, 6), (2, 32), (0, 70), (8, 96), (24, 104), (40, 98), (48, 78)])),
             L(outline([(2, 40), (24, 44), (32, 96), (8, 92)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 16), (96, 42), (94, 64, 1), (86, 50), (80, 40)])],
    'back': [L(outline([(10, 98), (0, 60), (6, 26), (24, 6), (50, 0), (76, 6), (94, 26), (100, 60), (90, 98), (76, 104), (50, 100), (24, 104)])),
             L(outline([(14, 50), (50, 30), (86, 50), (90, 80), (50, 70), (10, 80)]), 'shade', 'b', False)],
}

# River Willows: pelo rubio ahuecado como una nube encima de una cinta azul marino ancha en la frente; sonrisa de pillo
# con los dientes
CHARS['river-willows'] = {
    'body': 'normal', 'pal': pal('#f0d478', '#f8c898', iris='#1e1414', band='#2a3c6a', band_d='#1c2a4e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 70), (0, 44), (2, 18), (16, 2), (34, -6), (54, -4), (72, -6), (90, 2), (102, 20), (100, 44), (90, 70), (84, 60), (16, 60)])),
              L(outline([(60, -2), (88, 6), (100, 30), (94, 56), (80, 40)]), 'shade', 'b', False),
              strand([(20, 14), (34, 8), (44, 16)], 'shade', 'b', 1.0), strand([(56, 8), (70, 4), (82, 12)], 'shade', 'b', 1.0),
              L(outline([(10, 62), (10, 42), (50, 36), (90, 42), (90, 62), (50, 58)]), 'band', 'f', ln=True),
              L(outline([(60, 38), (90, 42), (90, 62), (62, 58)]), 'band_d', 'f', False)],
    'side': [L(outline([(54, 56), (64, 46), (90, 44), (102, 26), (96, 6), (76, -6), (50, -8), (22, -4), (2, 12), (-6, 34), (0, 60), (16, 72), (40, 64)])),
             L(outline([(-4, 30), (18, 38), (22, 64), (2, 58)]), 'shade', 'b', False),
             L(outline([(14, 66), (12, 48), (50, 42), (90, 46), (90, 62), (50, 60)]), 'band', 'f', ln=True)],
    'back': [L(outline([(10, 66), (0, 40), (2, 16), (16, 0), (34, -8), (54, -6), (72, -8), (90, 0), (102, 18), (100, 40), (90, 66), (50, 72)])),
             L(outline([(56, -6), (90, 2), (102, 34), (92, 62), (66, 66)]), 'shade', 'b', False),
             L(outline([(12, 82), (12, 62), (50, 66), (88, 62), (88, 82), (50, 86)]), 'band', 'f', ln=True)],
}

# Beck Heath: pelo lila corto y despeinado con dos mechones que salen en punta a los lados como alas, un pelo tieso en lo
# alto y flequillo sobre los ojos; mirada triste
CHARS['beck-heath'] = {
    'body': 'normal', 'pal': pal('#c8b0c4', '#fcd8b4', iris='#4a7a7a', shade='#a08aa0'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(quad((50, 4), (40, -20), (56, -34)), 'mid', 'b', False, False, 3.0),
              L(outline([(16, 92), (6, 84, 1), (12, 66), (6, 44), (-18, 34, 1), (10, 24), (24, 8), (50, 2), (76, 8), (90, 24), (118, 34, 1), (94, 44), (88, 66),
                         (94, 84, 1), (84, 92), (82, 62), (18, 62)])),
              L(outline([(60, 6), (86, 18), (94, 50), (86, 84), (80, 50)]), 'shade', 'b', False),
              fringe([(12, 66), (14, 40), (28, 22), (50, 16), (72, 22), (86, 40), (88, 66), (80, 56), (74, 66, 1), (66, 48), (58, 60, 1), (52, 46), (48, 74, 1),
                      (42, 48), (34, 62, 1), (28, 50), (20, 64, 1)])],
    'side': [L(quad((44, 2), (40, -20), (56, -32)), 'mid', 'b', False, False, 3.0),
             L(outline([(54, 62), (60, 50), (82, 48), (94, 34), (100, 18, 1), (84, 14), (68, 0), (42, -2), (18, 8), (2, 32), (2, 62), (-8, 76, 1), (10, 76), (8, 92, 1),
                        (24, 84), (38, 90), (46, 76)])),
             L(outline([(2, 36), (24, 42), (26, 78), (6, 72)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 16), (94, 40), (92, 62, 1), (84, 48), (76, 36)])],
    'back': [L(quad((50, 4), (44, -20), (58, -32)), 'mid', 'b', False, False, 3.0),
             L(outline([(14, 88), (4, 80, 1), (10, 64), (6, 44), (-20, 34, 1), (10, 22), (24, 8), (50, 2), (76, 8), (90, 22), (120, 34, 1), (94, 44), (90, 64),
                        (96, 80, 1), (86, 88), (50, 94)])),
             L(outline([(56, 4), (86, 18), (96, 50), (88, 84), (62, 90)]), 'shade', 'b', False)],
}

# Brook Linden: pelo blanco liso peinado hacia un lado, con un mechón grande que le cruza la frente y cae junto a la oreja;
# por detrás es castaño claro; piel morena y ojos azules
CHARS['brook-linden'] = {
    'body': 'normal', 'pal': pal('#f4f0e0', '#b07a4a', iris='#4a90d0', shade='#b89a8a', deep='#8a6a5a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 96), (4, 60), (8, 24), (24, 6), (50, 0), (76, 6), (92, 24), (96, 60), (92, 92), (84, 66), (16, 66)])),
              L(outline([(60, 4), (86, 16), (96, 56), (90, 88), (82, 56)]), 'shade', 'b', False),
              fringe([(10, 80), (10, 40), (22, 18), (46, 8), (72, 14), (88, 30), (90, 54), (82, 46), (70, 36), (50, 40), (34, 50), (22, 66), (16, 96, 1)])],
    'side': [L(outline([(54, 62), (60, 50), (82, 50), (94, 36), (90, 12), (68, -2), (40, -4), (16, 6), (2, 32), (2, 70), (10, 92), (26, 98), (40, 90), (48, 76)]), 'shade'),
             L(outline([(14, 4), (40, -4), (68, -2), (90, 12), (94, 36), (84, 40), (60, 22), (40, 18), (16, 26)]), 'mid', 'b', False),
             fringe([(66, 2), (90, 16), (96, 42), (94, 64, 1), (86, 50), (80, 40)])],
    'back': [L(outline([(10, 92), (2, 60), (8, 24), (24, 6), (50, 0), (76, 6), (92, 24), (98, 60), (90, 92), (70, 98), (50, 94), (30, 98)]), 'shade'),
             L(outline([(8, 30), (24, 6), (50, 0), (76, 6), (92, 30), (70, 26), (50, 34), (30, 26)]), 'mid', 'b', False),
             strand([(40, 60), (44, 68), (48, 60)], 'deep', 'b', 1.0), strand([(58, 64), (62, 72), (66, 64)], 'deep', 'b', 1.0)],
}

# Langford Ash: melena castaña larga peinada hacia un lado con un mechón ancho que le cae sobre un ojo, dos mechones en
# punta en lo alto como cuernos y una coleta baja que le cae por la espalda
CHARS['langford-ash'] = {
    'body': 'normal', 'pal': pal('#8a5a34', '#fcd8b4', iris='#1e1414'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(12, 100), (6, 60), (8, 26), (4, -6, 1), (22, 10), (50, 2), (78, 10), (96, -6, 1), (92, 26), (94, 60), (88, 100), (84, 66), (16, 66)])),
              L(outline([(60, 4), (84, 14), (94, 50), (88, 94), (82, 56)]), 'shade', 'b', False),
              fringe([(14, 62), (18, 34), (34, 16), (54, 12), (72, 18), (86, 36), (86, 62), (78, 50), (70, 60, 1), (64, 44), (56, 52), (50, 80, 1), (44, 54),
                      (34, 46), (26, 58, 1)]),
              L(outline([(56, 16), (74, 22), (84, 40), (72, 38)]), 'light', 'f', False)],
    'side': [L(outline([(54, 62), (60, 50), (82, 48), (92, 32), (86, 10), (82, -10, 1), (68, 2), (40, -2), (16, 8), (2, 32), (2, 64), (12, 90), (30, 100), (38, 120, 1),
                        (40, 96), (48, 76)])),
             L(outline([(4, 36), (24, 42), (30, 92), (12, 88)]), 'shade', 'b', False),
             fringe([(66, 4), (90, 18), (96, 42), (94, 66, 1), (86, 50), (80, 40)])],
    'back': [L(outline([(12, 96), (4, 60), (8, 26), (4, -6, 1), (22, 10), (50, 2), (78, 10), (96, -6, 1), (92, 26), (96, 60), (88, 96), (60, 104), (54, 120, 1),
                        (46, 104), (30, 100)])),
             L(outline([(56, 4), (86, 16), (96, 56), (88, 94), (60, 102)]), 'shade', 'b', False)],
}

# Escott Aspen: pelo verde azulado oscuro de pinchos hacia arriba, con mechones en punta que caen a los lados y la nuca y
# un flequillo de puntas; cejas fruncidas
CHARS['escott-aspen'] = {
    'body': 'normal', 'pal': pal('#2a4a50', '#fcd8b4', iris='#1e1414'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 92), (2, 92, 1), (10, 74), (6, 50), (-4, 40, 1), (10, 30), (16, 6, 1), (30, 14), (40, -4, 1), (50, 8), (60, -12, 1), (66, 8), (82, 4, 1),
                         (86, 24), (104, 40, 1), (94, 50), (90, 74), (98, 92, 1), (86, 92), (84, 64), (16, 64)])),
              L(outline([(60, 2), (84, 14), (94, 46), (88, 84), (80, 50)]), 'shade', 'b', False),
              fringe([(12, 66), (16, 40), (30, 24), (50, 18), (70, 24), (84, 40), (88, 66), (80, 54), (74, 64, 1), (66, 48), (58, 58, 1), (52, 44), (46, 66, 1),
                      (40, 46), (32, 58, 1), (26, 48), (20, 64, 1)])],
    'side': [L(outline([(54, 62), (60, 50), (82, 48), (92, 32), (88, 14), (98, 2, 1), (76, 2), (66, -14, 1), (52, 0), (28, -8, 1), (24, 8), (6, 20), (2, 50), (-10, 76, 1),
                        (10, 72), (8, 92, 1), (24, 82), (36, 86), (46, 74)])),
             L(outline([(4, 30), (24, 36), (26, 72), (8, 66)]), 'shade', 'b', False),
             fringe([(64, 4), (90, 18), (96, 42), (94, 66, 1), (86, 50), (80, 62, 1), (76, 42)])],
    'back': [L(outline([(14, 92), (-4, 88, 1), (8, 74), (4, 50), (-8, 40, 1), (10, 28), (16, 4, 1), (30, 12), (40, -6, 1), (50, 6), (60, -14, 1), (66, 6), (84, 2, 1),
                        (88, 22), (108, 40, 1), (96, 50), (92, 74), (104, 88, 1), (86, 92), (64, 96, 1), (50, 88), (36, 96, 1)])),
             L(outline([(56, 4), (86, 16), (98, 50), (88, 88), (62, 92)]), 'shade', 'b', False)],
}

# Bradford Ash: pelo castaño con dos mechones gruesos que se alzan en punta a los lados de la cabeza como cuernos y uno
# ancho que baja por la frente hasta la nariz; ojos verdes grandes
CHARS['bradford-ash'] = {
    'body': 'bajito', 'pal': pal('#6a4224', '#fcd8b4', iris='#5a7a3a'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(14, 90), (8, 60), (8, 30), (-6, -10, 1), (20, 14), (50, 6), (70, 10), (86, -8, 1), (94, 24), (92, 60), (86, 90), (82, 62), (18, 62)])),
              L(outline([(60, 8), (84, 14), (94, 46), (88, 84), (80, 50)]), 'shade', 'b', False),
              fringe([(30, 20), (50, 14), (66, 22), (72, 40), (60, 54), (50, 82, 1), (44, 50), (34, 40)]),
              L(outline([(48, 22), (60, 26), (58, 44)]), 'light', 'f', False)],
    'side': [L(outline([(54, 60), (60, 50), (84, 46), (94, 30), (100, 8, 1), (78, 14), (72, -10, 1), (56, 6), (34, 4), (18, -14, 1), (14, 12), (4, 34), (4, 66), (16, 90),
                        (34, 92), (46, 76)])),
             L(outline([(4, 36), (24, 42), (28, 86), (10, 80)]), 'shade', 'b', False),
             fringe([(70, 14), (92, 28), (94, 52, 1), (84, 40)])],
    'back': [L(outline([(14, 86), (8, 60), (8, 30), (-4, -10, 1), (20, 16), (50, 8), (66, 12), (90, -10, 1), (94, 26), (92, 60), (86, 86), (50, 94)])),
             L(outline([(14, 50), (50, 36), (86, 50), (88, 80), (50, 74), (12, 80)]), 'shade', 'b', False)],
}

# Bay Laurel: pelo azul morado espeso que se abre en punta a la altura de las orejas, con un lazo de dos mechones en lo
# alto; ojos azules
CHARS['bay-laurel'] = {
    'body': 'delgado', 'pal': pal('#3e3e86', '#fcd8b4', iris='#2a8ab8'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(44, 4), (30, -18, 1), (46, -8), (50, 2)])), L(outline([(56, 4), (72, -14, 1), (58, -6), (52, 2)])),
              L(outline([(14, 96), (4, 76), (-12, 64, 1), (6, 56), (6, 26), (24, 6), (50, 0), (76, 6), (94, 26), (94, 56), (112, 64, 1), (96, 76), (86, 96), (84, 66),
                         (16, 66)])),
              L(outline([(60, 4), (86, 16), (96, 52), (90, 90), (82, 56)]), 'shade', 'b', False),
              fringe([(12, 68), (14, 40), (28, 22), (50, 16), (72, 22), (86, 40), (88, 68), (80, 56), (72, 66, 1), (66, 48), (56, 60, 1), (50, 44), (44, 60, 1),
                      (36, 48), (28, 64, 1), (20, 54)])],
    'side': [L(outline([(40, 4), (30, -18, 1), (44, -8), (48, 2)])), L(outline([(50, 4), (66, -16, 1), (54, -6), (46, 0)])),
             L(outline([(54, 62), (60, 50), (82, 48), (92, 32), (88, 12), (68, 0), (40, -2), (16, 8), (2, 34), (-6, 56), (-20, 66, 1), (0, 68), (8, 92), (24, 98),
                        (40, 90), (48, 76)])),
             L(outline([(2, 40), (24, 44), (30, 90), (8, 86)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 42), (94, 64, 1), (86, 50), (80, 40)])],
    'back': [L(outline([(44, 4), (30, -18, 1), (46, -8), (50, 2)])), L(outline([(56, 4), (72, -14, 1), (58, -6), (52, 2)])),
             L(outline([(14, 96), (4, 76), (-14, 60, 1), (4, 52), (6, 26), (24, 6), (50, 0), (76, 6), (94, 26), (96, 52), (114, 60, 1), (96, 76), (86, 96), (50, 102)])),
             L(outline([(56, 4), (86, 16), (98, 52), (88, 92), (62, 98)]), 'shade', 'b', False)],
}

# Maxwell Mahogany (portero suplente): melena morada lisa y larga, con un mechón que le tapa un ojo y las puntas por debajo
# de la mandíbula; cara seria
CHARS['maxwell-mahogany'] = {
    'body': 'normal', 'pal': pal('#7a2a62', '#f6c898', iris='#1e1414'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 118), (4, 60), (8, 24), (26, 4), (50, -2), (74, 4), (92, 24), (96, 60), (92, 118), (82, 116), (84, 66), (16, 66), (18, 116)])),
              L(outline([(60, 2), (86, 16), (96, 56), (90, 116), (82, 116), (82, 56)]), 'shade', 'b', False),
              fringe([(10, 80), (10, 40), (24, 16), (50, 8), (76, 16), (90, 40), (90, 76), (82, 58), (66, 48), (54, 62), (50, 96, 1), (40, 80), (30, 92, 1), (22, 74)]),
              L(outline([(56, 14), (78, 22), (86, 44), (72, 40)]), 'light', 'f', False)],
    'side': [L(outline([(54, 62), (60, 50), (82, 50), (94, 34), (90, 12), (68, -2), (40, -4), (16, 6), (2, 32), (0, 70), (6, 112), (26, 118), (40, 100), (48, 76)])),
             L(outline([(2, 40), (24, 44), (34, 112), (8, 110)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 42), (94, 74, 1), (86, 56), (80, 40)])],
    'back': [L(outline([(10, 116), (2, 60), (8, 24), (26, 4), (50, -2), (74, 4), (92, 24), (98, 60), (90, 116), (50, 122)])),
             L(outline([(56, 2), (88, 18), (98, 60), (90, 114), (60, 118)]), 'shade', 'b', False)],
}

# Calder Elm (sin modelo 3D; de su retrato): pelo negro a capas hasta la mandíbula, con mechones en punta sobre la frente y
# las orejas; mirada cansada
CHARS['calder-elm'] = {
    'body': 'normal', 'pal': pal('#2a2a30', '#fcd8b4', iris='#2a3a5a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 100), (-2, 98, 1), (6, 84), (2, 50), (10, 20), (28, 2), (50, -4), (72, 2), (90, 20), (98, 50), (94, 84), (102, 98, 1), (88, 100),
                         (84, 64), (16, 64)])),
              L(outline([(60, 2), (86, 16), (96, 52), (90, 92), (82, 56)]), 'shade', 'b', False),
              fringe([(10, 68), (12, 38), (26, 18), (50, 10), (74, 18), (88, 38), (90, 68), (82, 56), (76, 66, 1), (68, 48), (60, 60, 1), (54, 44), (46, 62, 1),
                      (40, 46), (30, 62, 1), (24, 50), (18, 66, 1)])],
    'side': [L(outline([(54, 62), (60, 50), (82, 50), (94, 34), (90, 12), (68, -2), (40, -4), (16, 6), (2, 32), (0, 66), (-10, 90, 1), (10, 84), (14, 100, 1), (26, 88),
                        (36, 98, 1), (44, 80)])),
             L(outline([(2, 40), (24, 44), (30, 88), (8, 84)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 42), (94, 64, 1), (86, 50), (80, 40)])],
    'back': [L(outline([(10, 98), (-4, 96, 1), (4, 82), (0, 50), (10, 20), (28, 2), (50, -4), (72, 2), (90, 20), (100, 50), (96, 82), (104, 96, 1), (88, 98),
                        (70, 106, 1), (60, 96), (50, 106, 1), (40, 96), (30, 106, 1)])),
             L(outline([(56, 2), (88, 18), (98, 52), (92, 94), (62, 98)]), 'shade', 'b', False)],
}

# Laike Alder: piel morena, pelo rosa muy claro que le envuelve la cabeza como una capucha, con dos mechones en punta en lo
# alto como orejas y una coleta que le cae por delante de un hombro; dos marcas blancas sobre los ojos rojizos
CHARS['laike-alder'] = {
    'body': 'normal', 'pal': pal('#f6dcdc', '#a8784a', iris='#8a2a3a', shade='#d8b0b0'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(26, 10), (24, -20, 1), (40, 2)])),
              L(outline([(12, 100), (4, 60), (8, 24), (24, 4), (50, -2), (76, 4), (92, 24), (96, 60), (90, 100), (84, 66), (16, 66)])),
              L(outline([(60, 4), (86, 16), (96, 56), (90, 96), (82, 56)]), 'shade', 'b', False),
              fringe([(12, 70), (12, 40), (24, 22), (50, 18), (76, 22), (88, 40), (88, 70), (80, 52), (66, 40), (50, 38), (34, 40), (20, 52)]),
              L(outline([(82, 84), (90, 100), (88, 118, 1), (80, 102)]), 'mid', 'f', ln=True),
              L([(34, 64), (40, 60)], WHITE, 'f', False, False, 1.4), L([(66, 64), (60, 60)], WHITE, 'f', False, False, 1.4)],
    'side': [L(outline([(36, 4), (30, -24, 1), (50, 0)])),
             L(outline([(54, 62), (60, 50), (82, 50), (94, 34), (90, 12), (68, -2), (40, -4), (16, 6), (2, 32), (2, 70), (10, 96), (26, 104), (40, 96), (48, 78)])),
             L(outline([(2, 40), (24, 44), (32, 96), (8, 92)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 16), (96, 42), (94, 56), (86, 50), (80, 40)])],
    'back': [L(outline([(70, 10), (74, -20, 1), (58, 2)])),
             L(outline([(12, 96), (2, 60), (8, 24), (24, 4), (50, -2), (76, 4), (92, 24), (98, 60), (90, 96), (50, 104)])),
             L(outline([(56, 2), (88, 18), (98, 56), (90, 94), (62, 100)]), 'shade', 'b', False)],
}

# Tahoma Sequoia: pelo verde oscuro en mechones gruesos y lisos que caen como un casco hasta debajo de las orejas, con las
# puntas sueltas; piel morena clara, sonrisa de dientes
CHARS['tahoma-sequoia'] = {
    'body': 'normal', 'pal': pal('#3e5a1e', '#f0b880', iris='#1e1414'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 100, 'hairline': (56, 44)},
    'front': [L(outline([(10, 100), (2, 92, 1), (4, 60), (6, 24), (24, 2), (50, -4), (76, 2), (94, 24), (96, 60), (98, 92, 1), (90, 100), (84, 70), (16, 70)])),
              L(outline([(60, 0), (86, 14), (96, 56), (92, 96), (82, 60)]), 'shade', 'b', False),
              strand([(22, 18), (14, 60)], 'deep', 'b', 1.0), strand([(78, 18), (86, 60)], 'deep', 'b', 1.0)],
    'side': [L(outline([(56, 54), (66, 46), (84, 44), (92, 28), (86, 8), (66, -4), (40, -4), (16, 6), (2, 32), (-2, 70), (2, 100), (20, 104), (36, 96), (48, 72)])),
             L(outline([(0, 40), (22, 44), (30, 96), (6, 96)]), 'shade', 'b', False),
             strand([(20, 20), (14, 90)], 'deep', 'b', 1.0), strand([(40, 8), (36, 80)], 'deep', 'b', 1.0)],
    'back': [L(outline([(6, 102), (0, 60), (6, 24), (24, 2), (50, -4), (76, 2), (94, 24), (100, 60), (94, 102), (78, 106), (64, 98), (50, 106), (36, 98), (22, 106)])),
             L(outline([(56, 0), (88, 16), (100, 60), (92, 100), (64, 100)]), 'shade', 'b', False),
             strand([(26, 20), (22, 96)], 'deep', 'b', 1.0), strand([(50, 10), (50, 100)], 'deep', 'b', 1.0), strand([(74, 20), (78, 96)], 'deep', 'b', 1.0)],
}
