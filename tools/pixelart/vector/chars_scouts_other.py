"""Ojeadores de Ares y Orion (scouts-ares, scouts-orion): claves 'scouts-ares:<id>' y 'scouts-orion:<id>'.

Los ocho tienen modelo 3D en la enciclopedia (de Ares o de Orion) y se han calcado de él sobre la rejilla."""
import copy

from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import quad  # noqa: F401

WHITE = (248, 248, 248, 255)
PEARL = (240, 232, 236, 255)


def curls(cx, cy, r, n=8, a0=0.0, k=0.8):
    """Contorno de nube de rizos alrededor de un centro."""
    import math
    pts = []
    for i in range(n * 2):
        a = a0 + math.pi * 2 * i / (n * 2)
        f = 1.0 if i % 2 == 0 else k
        pts.append((cx + r[0] * f * math.cos(a), cy + r[1] * f * math.sin(a)))
    return blob(pts, 6)


# Massimo Donati (Goujin Masatatsu, el padre de Goujin en Ares): adulto grandullón de piel morena; pelo negro rizado y
# abultado arriba con los lados cortos, una cinta blanca (hachimaki) atada detrás con el nudo y las puntas colgando;
# ojos redondos y saltones, bigotillo y barba de pocos días
CHARS['scouts-ares:massimo-donati'] = {
    'body': 'corpulento', 'pal': pal('#2a2626', '#9a6440', iris='#1e1a1a', shade='#1a1818', band='#f4f2ee', band_d='#d8cccc', stub='#5e3e2c'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 96, 'hairline': [(14, 64), (18, 50), (30, 46), (50, 46), (70, 46), (82, 50), (86, 64)]},
    'front': [L(curls(50, 20, (36, 20), 9, 0.3)), L(outline([(14, 66), (14, 40), (86, 40), (86, 66), (78, 52), (22, 52)])),
              L(curls(60, 16, (20, 10), 5, 0.6), 'shade', 'b', False),
              L(outline([(12, 32), (50, 30), (88, 32), (88, 46), (50, 46), (12, 46)]), 'band', 'f'),
              L(outline([(12, 42), (50, 41), (88, 42), (88, 46), (50, 46), (12, 46)]), 'band_d', 'f', False),
              L(quad((38, 92), (44, 89), (49, 91)), 'stub', 'f', False, False, 1.6), L(quad((51, 91), (56, 89), (62, 92)), 'stub', 'f', False, False, 1.6),
              L([(34, 99), (36, 103)], 'stub', 'f', False, False, 1.0), L([(66, 99), (64, 103)], 'stub', 'f', False, False, 1.0)],
    'side': [L(curls(42, 20, (40, 20), 9, 0.2)), L(outline([(4, 30), (60, 26), (62, 50), (40, 56), (30, 76), (12, 78), (4, 56)])),
             L(outline([(4, 46), (30, 50), (28, 76), (12, 78), (4, 60)]), 'shade', 'b', False),
             L(outline([(2, 32), (50, 28), (88, 34), (88, 48), (50, 44), (2, 46)]), 'band', 'f'),
             L(outline([(4, 40), (-10, 50), (-14, 70, 1), (-2, 56), (6, 46)]), 'band', 'f'),
             L(outline([(4, 40), (-4, 44), (-2, 74, 1), (6, 52)]), 'band_d', 'f'),
             L(quad((82, 92), (88, 89), (90, 92)), 'stub', 'f', False, False, 1.6)],
    'back': [L(curls(50, 20, (36, 20), 9, 0.3)), L(outline([(14, 70), (12, 36), (88, 36), (86, 70), (64, 88), (36, 88)])),
             L(outline([(52, 40), (86, 40), (86, 70), (64, 86)]), 'shade', 'b', False),
             L(outline([(12, 32), (50, 30), (88, 32), (88, 46), (50, 46), (12, 46)]), 'band', 'f'),
             L(outline([(50, 38), (34, 46), (30, 62, 1), (44, 52), (50, 44), (56, 52), (70, 62, 1), (66, 46)]), 'band', 'f'),
             L(ell(50, 40, 5, 5), 'band_d', 'f')],
}

# Chesney Horse (Kakuma Kanemasa, el padre de Kakuma en Ares): adulto con el pelo castaño muy oscuro en un tupé plano
# altísimo (flat-top) de lados rectos, rapado a los lados y la nuca; gafas rectangulares de pasta azul, cejas gruesas
# fruncidas y sonrisa pequeña
CHARS['scouts-ares:chesney-horse'] = {
    'body': 'normal', 'pal': pal('#3a2a20', '#f4b67a', iris='#1e1a1a', shade='#5a4a3c', fade='#8a6e52', blue='#3a64b0', lens='#d8ecf4'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': [(14, 60), (20, 54), (38, 54), (44, 62), (50, 52), (56, 62), (62, 54), (80, 54), (86, 60)]},
    'front': [L(outline([(12, 6), (88, 6), (86, 18), (84, 44), (16, 44), (14, 18)])),
              L(outline([(14, 18), (86, 18), (85, 28), (15, 28)]), 'shade', 'f', False),
              L(outline([(16, 44), (84, 44), (86, 62), (80, 56), (20, 56), (14, 62)]), 'fade'),
              L(outline([(22, 70), (46, 70), (46, 82), (24, 82)]), 'lens', 'f', False),
              L(outline([(78, 70), (54, 70), (54, 82), (76, 82)]), 'lens', 'f', False),
              L(outline([(22, 70), (46, 70), (46, 82), (24, 82)]) + [(22, 70)], 'blue', 'f', False, False, 2.0),
              L(outline([(78, 70), (54, 70), (54, 82), (76, 82)]) + [(78, 70)], 'blue', 'f', False, False, 2.0),
              L([(46, 74), (54, 74)], 'blue', 'f', False, False, 1.6), L([(22, 72), (16, 72)], 'blue', 'f', False, False, 1.6),
              L([(78, 72), (84, 72)], 'blue', 'f', False, False, 1.6)],
    'side': [L(outline([(12, 6), (88, 4), (86, 16), (78, 40), (62, 44), (40, 52), (8, 50)])),
             L(outline([(12, 16), (86, 14), (84, 24), (12, 26)]), 'shade', 'f', False),
             L(outline([(8, 46), (40, 50), (56, 46), (60, 58), (40, 64), (30, 84), (14, 82), (6, 64)]), 'fade'),
             L(outline([(80, 70), (90, 70), (90, 82), (80, 82)]), 'lens', 'f', False),
             L(outline([(80, 70), (90, 70), (90, 82), (80, 82)]) + [(80, 70)], 'blue', 'f', False, False, 2.0),
             L([(50, 72), (80, 72)], 'blue', 'f', False, False, 1.8)],
    'back': [L(outline([(12, 6), (88, 6), (86, 18), (84, 44), (16, 44), (14, 18)])),
             L(outline([(14, 18), (86, 18), (85, 28), (15, 28)]), 'shade', 'f', False),
             L(outline([(16, 44), (84, 44), (86, 70), (68, 86), (32, 86), (14, 70)]), 'fade'),
             L(outline([(52, 46), (84, 46), (84, 70), (66, 84)]), 'shade', 'b', False)],
}

# Faith Winter (Miyano Akane, la mánager del Raimon de Ares): chica de pelo negro azulado liso con un flequillo de mechones
# largos que le cae sobre los ojos (uno por en medio de la cara), recogido en dos coletas bajas a los lados que caen hasta
# el pecho; ojos verdes grandes y sonrisa
CHARS['scouts-ares:faith-winter'] = {
    'body': 'chica', 'pal': pal('#2c2a3e', '#fce4d4', iris='#2a8a5a', shade='#1c1a2a', light='#4a4862'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(6, 108), (0, 70), (6, 30), (24, 6), (50, -2), (76, 6), (94, 30), (100, 70), (94, 108), (84, 98), (86, 60), (80, 56), (20, 56),
                         (14, 60), (16, 98)])),
              L(outline([(60, 0), (84, 10), (96, 40), (98, 80), (92, 104), (86, 70)]), 'shade', 'b', False),
              L(outline([(16, 64), (18, 40), (30, 22), (50, 16), (70, 22), (82, 40), (84, 64), (76, 52), (68, 66, 1), (62, 48), (54, 50), (48, 78, 1),
                         (42, 50), (34, 52), (28, 66, 1), (24, 52)]), 'mid', 'f'),
              strand([(34, 20), (30, 40)], 'light', 'f', 1.0), strand([(66, 20), (70, 40)], 'light', 'f', 1.0)],
    'side': [L(outline([(56, 56), (62, 44), (80, 42), (92, 30), (86, 10), (62, -2), (34, 0), (12, 14), (2, 40), (4, 70), (14, 84), (30, 76), (44, 66),
                        (52, 60)])),
             L(outline([(40, 60), (34, 74), (32, 104), (40, 114, 1), (50, 100), (52, 72), (48, 62)])),
             L(outline([(4, 30), (36, 34), (40, 62), (16, 80), (4, 64)]), 'shade', 'b', False),
             L(outline([(70, 6), (90, 22), (94, 46), (88, 62, 1), (84, 44), (76, 34)]), 'mid', 'f')],
    'back': [L(outline([(10, 80), (4, 44), (14, 16), (50, 2), (86, 16), (96, 44), (90, 80), (70, 86), (50, 84), (30, 86)])),
             L(outline([(14, 70), (6, 82), (8, 110, 1), (20, 100), (24, 76)])), L(outline([(86, 70), (94, 82), (92, 110, 1), (80, 100), (76, 76)])),
             L(outline([(56, 6), (86, 18), (94, 50), (88, 78), (64, 84)]), 'shade', 'b', False),
             strand([(50, 4), (50, 80)], 'shade', 'b', 1.0)],
}

# Ivan Allegrov (Bernard Girikanan, el entrenador de Rusia en Orion): joven de pelo blanco lavanda liso con flequillo recto
# de mechones y dos mechones largos delante de las orejas, recogido detrás en una coleta baja larguísima; ojos azul claro,
# un lunar bajo el ojo izquierdo y media sonrisa
CHARS['scouts-orion:ivan-allegrov'] = {
    'body': 'delgado', 'pal': pal('#eef0f8', '#fce8d6', iris='#5aa4d8', shade='#c4b8cc', deep='#a898b4', mole='#3a2a2a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 100), (10, 60), (14, 24), (30, 8), (50, 4), (70, 8), (86, 24), (90, 60), (88, 100), (82, 80), (82, 60), (78, 56), (22, 56),
                         (18, 60), (18, 80)])),
              L(outline([(60, 6), (82, 18), (90, 50), (88, 96), (82, 64)]), 'shade', 'b', False),
              L(outline([(16, 62), (16, 38), (28, 20), (50, 14), (72, 20), (84, 38), (84, 62), (78, 60), (72, 66, 1), (64, 58), (56, 66, 1), (50, 58),
                         (42, 66, 1), (36, 58), (28, 66, 1), (22, 60)]), 'mid', 'f'),
              strand([(30, 22), (30, 56)], 'deep', 'f', 0.9), strand([(50, 16), (50, 56)], 'deep', 'f', 0.9), strand([(70, 22), (70, 56)], 'deep', 'f', 0.9),
              L(ell(66, 84, 1.2, 1.2), 'mole', 'f', False)],
    'side': [L(outline([(60, 56), (66, 46), (82, 44), (94, 34), (92, 14), (72, 2), (44, 2), (20, 12), (8, 34), (8, 58), (16, 70), (34, 66), (48, 62),
                        (56, 60)])),
             L(outline([(14, 60), (0, 70), (-22, 98), (-32, 112, 1), (-10, 100), (8, 82), (22, 70)])),
             L(outline([(74, 50), (78, 70), (76, 96, 1), (70, 72), (68, 54)])),
             L(outline([(8, 34), (40, 32), (50, 50), (34, 66), (14, 68)]), 'shade', 'b', False),
             L(outline([(70, 6), (92, 18), (96, 40), (90, 56, 1), (84, 42), (76, 30)]), 'mid', 'f')],
    'back': [L(outline([(12, 70), (10, 36), (24, 12), (50, 4), (76, 12), (90, 36), (88, 70), (70, 80), (50, 82), (30, 80)])),
             L(outline([(42, 74), (50, 70), (58, 74), (64, 100), (56, 116, 1), (50, 104), (44, 116, 1), (36, 100)])),
             L(outline([(56, 8), (82, 18), (90, 44), (86, 70), (62, 80)]), 'shade', 'b', False),
             L(ell(50, 74, 5, 3), 'deep', 'f'),
             strand([(30, 20), (44, 72)], 'deep', 'b', 0.9), strand([(70, 20), (56, 72)], 'deep', 'b', 0.9)],
}

# Gustav (Gustav Nikolsky, el director de Rusia en Orion): anciano de cara alargada y arrugada con un gorro negro plano y
# redondo; pelo gris pegado a los lados, cejas gruesas grises fruncidas, nariz larga y una barba y bigote grises muy
# largos en dos mechones; capa negra de cuello alto rojo
CHARS['scouts-orion:gustav'] = {
    'body': 'delgado', 'cape': '#cc1e24', 'pal': pal('#c8c8cc', '#f8dcc0', iris='#3a4a6a', shade='#9a9aa0', hat='#222024', hat_l='#3a383e',
                                                      wrinkle='#c8a488'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'hairline': False,
             'face_front': blob([(22, 46), (50, 40), (78, 46), (80, 76), (74, 100), (62, 110), (50, 112), (38, 110), (26, 100), (20, 76)])},
    'front': [L(outline([(18, 76), (16, 44), (22, 30), (78, 30), (84, 44), (82, 76), (76, 60), (24, 60)])),
              L(outline([(18, 26), (22, 14), (50, 10), (78, 14), (82, 26), (78, 34), (22, 34)]), 'hat'),
              L(outline([(24, 16), (50, 12), (76, 16), (74, 22), (26, 22)]), 'hat_l', 'f', False),
              L(outline([(26, 82), (40, 84), (50, 90), (60, 84), (74, 82), (78, 100), (70, 124), (60, 146, 1), (52, 128), (48, 128), (40, 146, 1), (30, 124), (22, 100)]), 'mid', 'f'),
              L([(50, 70), (48, 84), (52, 86)], 'wrinkle', 'f', False, False, 1.2),
              L(outline([(38, 90), (50, 94), (62, 90), (60, 100), (50, 98), (40, 100)]), 'shade', 'f', False),
              strand([(44, 96), (40, 136)], 'shade', 'f', 0.9), strand([(56, 96), (60, 136)], 'shade', 'f', 0.9),
              L([(36, 64), (44, 66)], 'wrinkle', 'f', False, False, 1.0), L([(64, 64), (56, 66)], 'wrinkle', 'f', False, False, 1.0),
              L([(42, 58), (58, 58)], 'wrinkle', 'f', False, False, 1.0)],
    'side': [L(outline([(14, 34), (64, 32), (62, 50), (46, 58), (36, 74), (20, 80), (10, 60)])),
             L(outline([(14, 28), (20, 14), (60, 10), (88, 16), (88, 28), (60, 34), (14, 34)]), 'hat'),
             L(outline([(72, 82), (90, 84), (96, 104), (90, 130), (82, 144, 1), (76, 118), (66, 96)]), 'mid', 'f'),
             L(outline([(86, 70), (96, 80), (90, 84)]), 'skin', 'f')],
    'back': [L(outline([(18, 78), (16, 40), (84, 40), (82, 78), (66, 90), (34, 90)])),
             L(outline([(56, 40), (84, 40), (82, 76), (64, 88)]), 'shade', 'b', False),
             L(outline([(18, 26), (22, 14), (50, 10), (78, 14), (82, 26), (78, 36), (22, 36)]), 'hat')],
}

# Philip Star (Ichihoshi Mitsuru, el hermano de Hikaru, en Orion): el mismo modelo que su dibujo del Inazuma Japón de
# Orion ('orion:lucas-star'): melena corta azul marino en capas de puntas, ojos azules afilados y ceño fruncido
CHARS['scouts-orion:philip-star'] = copy.deepcopy(CHARS['orion:lucas-star'])

# Yekaterina (Irina Stronov, la dama de Rusia en Orion): mujer de pelo azul muy claro enorme y ondulado, en volutas que
# le abultan arriba y a los lados hasta los hombros; ojos lilas, labios finos, pendientes y collar de perlas
CHARS['scouts-orion:yekaterina'] = {
    'body': 'chica', 'pal': pal('#c8d8f0', '#fcecdc', iris='#8a6ac8', shade='#9a96b4', deep='#7a7698', pearl='#f0e8ec'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 96, 'hairline': [(14, 70), (16, 50), (24, 34), (40, 28), (48, 32), (52, 26),
                                                                                         (64, 28), (78, 36), (84, 50), (86, 70)]},
    'front': [L(curls(50, 18, (42, 22), 8, 0.4)), L(curls(12, 66, (13, 26), 6, 0.2)), L(curls(88, 66, (13, 26), 6, 0.9)),
              L(outline([(12, 88), (6, 60), (10, 34), (30, 16), (70, 16), (90, 34), (94, 60), (88, 88), (82, 70), (18, 70)])),
              L(curls(64, 6, (24, 14), 5, 0.6), 'shade', 'b', False), L(curls(92, 66, (10, 22), 5, 0.3), 'shade', 'b', False),
              strand([(30, 14), (40, 26), (54, 26)], 'deep', 'b', 1.0), strand([(70, 18), (80, 30)], 'deep', 'b', 1.0),
              L(ell(17, 82, 1.8, 1.8), 'pearl', 'f'), L(ell(83, 82, 1.8, 1.8), 'pearl', 'f')],
    'side': [L(curls(44, 14, (48, 28), 8, 0.2)), L(curls(20, 62, (28, 32), 7, 0.5)),
             L(outline([(60, 50), (66, 38), (86, 34), (92, 20), (80, 30), (60, 30)])),
             L(curls(16, 66, (12, 16), 5, 0.1), 'shade', 'b', False),
             L(ell(48, 80, 1.8, 1.8), 'pearl', 'f')],
    'back': [L(curls(50, 14, (46, 26), 8, 0.4)), L(curls(50, 60, (46, 32), 9, 0.2)),
             L(curls(66, 50, (26, 30), 6, 0.6), 'shade', 'b', False),
             strand([(30, 30), (40, 60)], 'deep', 'b', 1.0), strand([(70, 30), (60, 64)], 'deep', 'b', 1.0)],
}

# Truman Newton (Shinjou Takuma, entrenador del Japón de Orion): adulto de piel tostada con el pelo negro peinado hacia
# atrás en mechones pegados, con dos picos arriba, dos mechones largos que le salen de las sienes y se curvan hacia
# fuera, y una coleta baja corta; ojos rojizos afilados bajo cejas negras fruncidas y boca seria
CHARS['scouts-orion:truman-newton'] = {
    'body': 'delgado', 'pal': pal('#2a2626', '#e0a274', iris='#8a2a2a', shade='#1a1818', light='#4a4446'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98,
             'hairline': [(16, 66), (18, 46), (28, 34), (40, 30), (50, 36), (60, 30), (72, 34), (82, 46), (84, 66)]},
    'front': [L(outline([(16, 70), (12, 40), (20, 20), (34, 8), (40, 2, 1), (46, 8), (54, 8), (60, 2, 1), (66, 8), (80, 20), (88, 40), (84, 70),
                         (78, 52), (22, 52)])),
              L(outline([(58, 8), (80, 20), (88, 42), (84, 64), (76, 44)]), 'shade', 'b', False),
              strand([(40, 10), (44, 30), (50, 36)], 'light', 'f', 0.9), strand([(60, 10), (56, 30), (50, 36)], 'light', 'f', 0.9),
              strand([(28, 18), (30, 34)], 'light', 'f', 0.9), strand([(72, 18), (70, 34)], 'light', 'f', 0.9),
              L(outline([(16, 52), (8, 56), (-4, 66), (-6, 76, 1), (4, 66), (16, 62)])), L(outline([(84, 52), (92, 56), (104, 66), (106, 76, 1), (96, 66), (84, 62)]))],
    'side': [L(outline([(70, 46), (74, 34), (90, 30), (92, 16), (80, 4), (60, 0), (40, 2), (20, 10), (8, 26), (6, 50), (14, 64), (26, 66), (40, 58),
                        (56, 52), (64, 50)])),
             L(outline([(14, 54), (0, 62), (-6, 82, 1), (6, 72), (12, 92, 1), (20, 70), (26, 60)])),
             L(outline([(46, 50), (34, 54), (24, 64), (22, 74, 1), (32, 64), (44, 60)])),
             L(outline([(6, 30), (34, 28), (48, 44), (30, 62), (12, 62)]), 'shade', 'b', False),
             strand([(88, 18), (60, 10), (30, 18)], 'light', 'f', 0.9), strand([(90, 28), (60, 24), (34, 34)], 'light', 'f', 0.9)],
    'back': [L(outline([(16, 66), (12, 36), (24, 14), (50, 4), (76, 14), (88, 36), (84, 66), (64, 76), (36, 76)])),
             L(outline([(40, 70), (50, 66), (60, 70), (62, 88), (54, 102, 1), (50, 90), (46, 102, 1), (38, 88)])),
             L(outline([(16, 52), (8, 56), (-4, 66), (-6, 76, 1), (4, 66), (16, 62)])), L(outline([(84, 52), (92, 56), (104, 66), (106, 76, 1), (96, 66), (84, 62)])),
             L(outline([(56, 8), (82, 18), (88, 42), (82, 64), (60, 74)]), 'shade', 'b', False),
             strand([(50, 6), (50, 66)], 'light', 'b', 0.9), strand([(30, 16), (42, 68)], 'light', 'b', 0.9), strand([(70, 16), (58, 68)], 'light', 'b', 0.9)],
}
