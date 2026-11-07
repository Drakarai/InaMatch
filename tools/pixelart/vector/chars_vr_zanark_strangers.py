"""Zanark Outsiders (vr-zanark-strangers): equipo de Victory Road (modo Crónica) que Zanark monta con los jugadores que se
encuentra por las rutas de la Crónica. Todos juegan en su forma Mixi Max (Module:PlayerData/VR: '<x>_MM'): piel morena,
ojos rojos y casi todos con el pelo verde azulado de Zanark. Modelos 3D de 英雄たちのヴィクトリーロード; todos van como
'vr:<id>' (sus dibujos de IE/GO/CS se quedan para sus equipos). Desarm (dave-quagmire) es su modelo de Desarm (デザーム), no
el de Saginuma; Venom (ベノム・ブラグ) y Li Hao tienen modelo con otro nombre."""
import math

from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import quad  # noqa: F401

SKIN = '#a8603e'
RED = '#d0202c'
WHITE = (248, 248, 248, 255)
BLACK = (26, 20, 24, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


def liner(cx, s, y=75, w=2.0):
    """Raya negra bajo el ojo y su rabillo hacia fuera (los Mixi Max de Zanark llevan los ojos muy marcados)."""
    return L(quad((cx - 7 * s, y + 2), (cx, y + 6.5), (cx + 6 * s, y + 4.5)), OUTC, 'f', False, False, w)


# Desarm (Saginuma Osamu, forma Mixi Max): pelo rubio pajizo enorme y ahuecado, con una cresta que sube en el centro y
# mechones que salen en abanico a los lados; una bufanda gorda del mismo color le tapa el cuello y la barbilla. Ojos rojos
# con raya negra y una media sonrisa
CHARS['vr:dave-quagmire'] = {
    'body': 'normal', 'pal': pal('#ece2a0', SKIN, iris=RED, shade='#cdb47a', deep='#a88a5a', scarf='#e6d68a', scarf_d='#c2a868'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 90, 'hairline': [(16, 66), (22, 52), (34, 44), (46, 50), (52, 36), (60, 46), (72, 42), (82, 52), (86, 66)]},
    'front': [L(outline([(16, 76), (8, 66), (10, 58), (-2, 50, 1), (6, 40), (4, 30), (16, 24), (22, 12), (38, 6), (50, -4, 1), (62, 4), (80, 8), (88, 20), (100, 28, 1),
                         (94, 38), (104, 50, 1), (96, 58), (96, 68), (86, 74), (82, 56), (20, 56)])),
              L(outline([(56, 4), (80, 10), (86, 24), (98, 28), (90, 38), (100, 50), (90, 56), (80, 46), (66, 22)]), 'shade', 'b', False),
              strand([(30, 22), (40, 36)], 'deep', 'b', 1.0), strand([(70, 18), (64, 34)], 'deep', 'b', 1.0), strand([(50, 4), (48, 22)], 'deep', 'b', 1.0),
              fringe([(30, 40), (44, 30), (52, 28), (62, 34), (70, 40), (62, 40), (56, 36), (52, 54, 1), (48, 38), (40, 42), (34, 52, 1), (34, 42)]),
              liner(36, 1), liner(64, -1),
              L(outline([(4, 92), (16, 84), (32, 92), (50, 96), (68, 92), (84, 84), (96, 92), (100, 106), (90, 118), (70, 122), (50, 120), (30, 122), (10, 118), (0, 106)]),
                'scarf', 'f'),
              L(outline([(10, 104), (30, 108), (50, 106), (70, 108), (92, 104), (88, 114), (70, 118), (50, 116), (30, 118), (12, 114)]), 'scarf_d', 'f', False),
              strand([(24, 96), (44, 102)], 'scarf_d', 'f', 1.0), strand([(76, 96), (58, 102)], 'scarf_d', 'f', 1.0)],
    'side': [L(outline([(70, 52), (78, 40), (90, 34), (88, 18), (96, 6, 1), (80, 6), (70, -4, 1), (56, 4), (40, -2, 1), (30, 8), (10, 10, 1), (12, 22), (-4, 32, 1), (6, 42),
                        (-8, 56, 1), (6, 62), (2, 76, 1), (20, 76), (38, 66), (44, 56), (58, 54)])),
             L(outline([(-2, 34), (30, 40), (40, 56), (26, 70), (6, 66)]), 'shade', 'b', False),
             strand([(30, 14), (60, 22)], 'deep', 'b', 1.0), strand([(14, 36), (40, 44)], 'deep', 'b', 1.0),
             L(outline([(14, 82), (34, 78), (56, 88), (76, 94), (92, 92), (96, 106), (88, 120), (60, 124), (30, 120), (12, 108)]), 'scarf', 'f'),
             L(outline([(18, 104), (50, 110), (90, 108), (86, 118), (56, 120), (24, 116)]), 'scarf_d', 'f', False)],
    'back': [L(outline([(10, 84), (6, 68), (0, 50, 1), (6, 36), (18, 22), (36, 10), (50, 2, 1), (64, 10), (82, 22), (94, 36), (100, 50, 1), (94, 68), (90, 84), (50, 90)])),
             L(outline([(6, 46), (50, 52), (94, 46), (96, 56), (50, 62), (4, 56)]), 'shade', 'b', False),
             L(outline([(6, 70), (50, 76), (94, 70), (94, 80), (50, 86), (6, 80)]), 'shade', 'b', False),
             L(outline([(4, 92), (50, 88), (96, 92), (100, 106), (92, 120), (50, 124), (8, 120), (0, 106)]), 'scarf', 'f'),
             L(outline([(4, 104), (50, 102), (96, 104), (94, 112), (50, 112), (6, 112)]), 'scarf_d', 'f', False)],
}

# Cao Cao (forma Mixi Max): melena blanca verdosa enorme peinada hacia atrás, con un tupé que se levanta y acaba en punta a su
# izquierda (derecha de la imagen) y mechones largos que le caen por los lados de la cara hasta los hombros; piel morena,
# arrugas marcadas en la frente y entre los ojos, ojos rojos y bigote fino que baja en perilla
CHARS['vr:cao-cao'] = {
    'body': 'normal', 'pal': pal('#d8f0e6', SKIN, iris=RED, shade='#9e948c', deep='#7a706a', light='#f4fffa'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'hairline': [(16, 60), (24, 50), (36, 46), (46, 52), (52, 40), (58, 52), (66, 46), (78, 50), (86, 60)]},
    'front': [L(outline([(2, 124, 1), (2, 98), (8, 72), (8, 50), (0, 32, 1), (14, 28), (18, 10), (32, -2), (48, -8), (64, -6), (80, -2), (98, -8, 1), (92, 6), (110, 12, 1),
                         (94, 24), (92, 48), (92, 72), (98, 98), (98, 124, 1), (90, 114), (84, 124, 1), (82, 92), (80, 66), (20, 66), (18, 92), (16, 124, 1), (10, 114)])),
              L(outline([(4, 100), (10, 70), (12, 50), (18, 70), (18, 96), (20, 118), (8, 120)]), 'shade', 'b', False),
              L(outline([(96, 100), (90, 72), (88, 50), (82, 70), (82, 96), (80, 118), (92, 120)]), 'shade', 'b', False),
              strand([(30, 10), (40, 30)], 'shade', 'b', 1.2), strand([(60, 4), (64, 26)], 'shade', 'b', 1.2), strand([(82, 10), (74, 30)], 'shade', 'b', 1.2),
              fringe([(26, 46), (40, 36), (50, 34), (62, 38), (74, 46), (62, 44), (54, 66, 1), (50, 44), (44, 46), (40, 60, 1), (38, 46)]),
              L([(36, 56), (44, 62)], OUTC, 'f', False, False, 1.0), L([(64, 56), (56, 62)], OUTC, 'f', False, False, 1.0),
              L([(44, 66), (48, 70)], OUTC, 'f', False, False, 1.0), L([(56, 66), (52, 70)], OUTC, 'f', False, False, 1.0),
              liner(36, 1, w=1.6), liner(64, -1, w=1.6),
              L([(50, 82), (48, 88)], OUTC, 'f', False, False, 1.0),
              L(quad((38, 96), (50, 90), (62, 96)), OUTC, 'f', False, False, 2.0),
              L([(38, 96), (36, 104)], OUTC, 'f', False, False, 1.6), L([(62, 96), (64, 104)], OUTC, 'f', False, False, 1.6),
              L([(50, 98), (50, 104)], OUTC, 'f', False, False, 1.6)],
    'side': [L(outline([(78, 50), (84, 40), (96, 30), (112, 18, 1), (94, 14), (84, 0), (64, -8), (40, -6), (16, 2), (2, -6, 1), (2, 16), (-10, 40), (-14, 70), (-16, 100),
                        (-8, 124), (6, 132, 1), (18, 118), (30, 130, 1), (32, 104), (34, 82), (42, 62), (56, 56), (68, 56)])),
             L(outline([(-10, 40), (20, 46), (32, 84), (28, 124), (8, 126), (-12, 100)]), 'shade', 'b', False),
             strand([(60, 6), (34, 18), (14, 40)], 'shade', 'b', 1.2), strand([(80, 18), (50, 22), (24, 50)], 'shade', 'b', 1.2),
             L(outline([(78, 60), (86, 66), (88, 90), (84, 112), (80, 92), (80, 74)]), 'mid', 'f')],
    'back': [L(outline([(6, 120), (4, 90), (8, 60), (8, 36), (-14, 8, 1), (10, 16), (20, 6), (40, -4), (60, -4), (80, 4), (92, 14), (112, 2, 1), (94, 30), (92, 60),
                        (96, 90), (94, 120), (50, 126)])),
             L(outline([(8, 34), (30, 26), (50, 30), (70, 26), (92, 34), (94, 120), (50, 126), (6, 120)]), 'shade', 'b', False),
             L(outline([(30, 60), (44, 56), (46, 70), (34, 74)]), 'mid', 'b', False), L(outline([(60, 96), (76, 92), (78, 108), (62, 110)]), 'mid', 'b', False),
             strand([(50, 50), (50, 120)], 'deep', 'b', 1.0), strand([(28, 52), (22, 116)], 'deep', 'b', 1.0), strand([(74, 52), (80, 116)], 'deep', 'b', 1.0)],
}

# Gale (Kujirai Takanori, forma Mixi Max): pelo verde agua con una coleta altísima atada arriba con un lazo rojo que sube y
# cae en arco por su derecha (izquierda de la imagen); mechones largos a los lados de la cara hasta la barbilla y flequillo
# en puntas; piel morena, orejas puntiagudas, ojos rojos y sonrisa con dientes
CHARS['vr:gail-baker'] = {
    'body': 'normal', 'pal': pal('#9ad8d2', SKIN, iris=RED, shade='#78b2ae', deep='#5a8e8a', tie='#d83040'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 92, 'big_ears': 1, 'hairline': [(16, 62), (22, 50), (32, 56), (40, 44), (50, 54), (60, 44), (68, 56), (78, 50), (84, 62)]},
    'front': [L(outline([(30, 14), (22, -14), (30, -34), (44, -40), (52, -32), (44, -26), (38, -12), (42, 8)])),
              L(outline([(28, 12), (14, 16), (4, 36), (-2, 70), (-6, 104), (0, 112, 1), (10, 96), (16, 74), (18, 60)])),
              L(outline([(14, 66), (12, 42), (22, 18), (38, 6), (50, 4), (64, 6), (80, 16), (88, 38), (88, 64), (92, 100), (86, 112, 1), (80, 90), (82, 64), (80, 52),
                         (20, 52), (20, 80), (18, 102), (12, 112, 1), (10, 90)])),
              L(outline([(56, 6), (78, 14), (88, 38), (86, 64), (76, 40)]), 'shade', 'b', False),
              L(outline([(0, 70), (10, 40), (14, 60), (8, 90), (2, 106)]), 'shade', 'b', False),
              L(ell(36, 10, 6, 5), 'tie', 'f', False), L(outline([(31, 7), (41, 7), (42, 13), (30, 13)]), 'tie', 'f', ln=True),
              strand([(30, 20), (36, 40)], 'deep', 'b', 1.0), strand([(50, 10), (50, 36)], 'deep', 'b', 1.0), strand([(70, 20), (64, 40)], 'deep', 'b', 1.0),
              liner(36, 1, w=1.6), liner(64, -1, w=1.6)],
    'side': [L(outline([(42, 10), (30, -10), (8, -30), (-12, -20), (-20, 8), (-16, 40), (-8, 64), (-2, 84), (-12, 96, 1), (6, 88), (8, 62), (4, 36), (8, 14), (24, 4)])),
             L(outline([(76, 54), (82, 44), (90, 32), (84, 14), (64, 4), (40, 6), (18, 18), (6, 40), (8, 62), (22, 72), (34, 66), (46, 58), (60, 56)])),
             L(outline([(76, 58), (82, 70), (84, 98), (78, 104, 1), (76, 80), (72, 64)]), 'mid', 'f'),
             L(outline([(8, 40), (30, 44), (36, 62), (22, 70), (8, 62)]), 'shade', 'b', False),
             L(outline([(-12, -16), (-18, 10), (-10, 50), (-6, 30), (-4, 0)]), 'shade', 'b', False),
             L(ell(34, 4, 5, 6), 'tie', 'f', ln=True)],
    'back': [L(outline([(64, 12), (78, -14), (96, -30), (112, -12), (114, 30), (108, 70), (104, 100), (112, 112, 1), (96, 100), (98, 70), (102, 30), (98, 0), (86, -12),
                        (76, 4)])),
             L(outline([(16, 76), (12, 46), (20, 20), (38, 6), (62, 6), (80, 20), (88, 46), (84, 76), (50, 82)])),
             L(outline([(12, 72), (8, 94), (12, 104, 1), (18, 92), (20, 76)]), 'mid', 'b'), L(outline([(88, 72), (92, 94), (88, 104, 1), (82, 92), (80, 76)]), 'mid', 'b'),
             L(outline([(56, 8), (80, 22), (88, 46), (84, 74), (64, 80)]), 'shade', 'b', False),
             strand([(36, 14), (34, 74)], 'deep', 'b', 1.0), strand([(50, 10), (50, 78)], 'deep', 'b', 1.0), strand([(64, 14), (66, 74)], 'deep', 'b', 1.0),
             L(ell(64, 10, 6, 5), 'tie', 'f', ln=True)],
}

# Kabata Taruhiko (forma Mixi Max): el pelo verde azulado oscuro es un casco liso que le baja en pico hasta la nariz, con dos
# cuernos enormes que salen de los lados y se curvan hacia arriba; orejas grandes, piel morena, ojos rojos y una sonrisa
# enorme de dientes afilados
CHARS['vr:baron-oxford'] = {
    'body': 'corpulento', 'pal': pal('#1e8486', SKIN, iris=RED, shade='#156264', deep='#0e4a4c'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'big_ears': 3, 'ear_out': 4, 'eye_y': 80, 'hairline': False,
             'face_front': blob([(16, 50), (50, 40), (84, 50), (88, 76), (84, 100), (66, 112), (50, 114), (34, 112), (16, 100), (12, 76)])},
    'front': [L(outline([(12, 40), (-2, 34), (-14, 22), (-20, 4), (-18, -16, 1), (-8, 0), (2, 14), (18, 22), (30, 8), (50, 4), (70, 8), (82, 22), (98, 14), (108, 0), (118, -16, 1),
                         (120, 4), (114, 22), (102, 34), (88, 40), (88, 60), (82, 70), (66, 56), (52, 80, 1), (48, 80), (34, 56), (18, 70), (12, 60)])),
              L(outline([(12, 40), (-2, 34), (-14, 22), (-20, 4), (-18, -16, 1), (-8, 0), (2, 14), (18, 22), (30, 8), (50, 4), (70, 8), (82, 22), (98, 14), (108, 0), (118, -16, 1),
                         (120, 4), (114, 22), (102, 34), (88, 40), (88, 60), (82, 70), (66, 56), (52, 80, 1), (48, 80), (34, 56), (18, 70), (12, 60)]), 'mid', 'f', False, ln=True),
              L(outline([(60, 8), (80, 20), (88, 44), (84, 64), (70, 40)]), 'shade', 'f', False),
              L(outline([(100, 16), (110, 2), (117, -12), (118, 6), (112, 22), (100, 32)]), 'shade', 'f', False),
              L([(26, 70), (40, 76)], OUTC, 'f', False, False, 3.0), L([(74, 70), (60, 76)], OUTC, 'f', False, False, 3.0),
              L(outline([(44, 72), (50, 70), (56, 72), (58, 90), (50, 94), (42, 90)]), 'skin_d', 'f', False),
              L(quad((44, 90), (50, 94), (56, 90)), OUTC, 'f', False, False, 1.2),
              L(outline([(28, 96), (72, 96), (66, 108), (50, 112), (34, 108)]), WHITE, 'f', False),
              L([(28, 96), (72, 96), (66, 108), (50, 112), (34, 108), (28, 96)], OUTC, 'f', False, False, 1.6),
              L([(34, 96), (37, 102), (40, 96), (43, 104), (46, 96), (50, 106), (54, 96), (57, 104), (60, 96), (63, 102), (66, 96)], OUTC, 'f', False, False, 1.0),
              L([(32, 102), (68, 102)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(80, 70), (84, 56), (90, 40), (84, 20), (68, 4), (44, 0), (22, 8), (8, 28), (4, 52), (10, 74), (22, 86), (34, 80), (40, 62), (56, 56), (70, 62)])),
             L(outline([(52, 6), (60, -16), (54, -34, 1), (72, -16), (70, 6)])),
             L(outline([(4, 40), (24, 46), (34, 74), (22, 84), (8, 70)]), 'shade', 'b', False),
             L(outline([(54, -28), (68, -14), (66, 4), (58, 4)]), 'shade', 'b', False),
             L(outline([(78, 92), (88, 92), (86, 100), (78, 100)]), WHITE, 'f', ln=True)],
    'back': [L(outline([(10, 70), (8, 44), (-2, 36), (-14, 22), (-20, 4), (-18, -16, 1), (-8, 0), (4, 14), (24, 8), (50, 4), (76, 8), (96, 14), (108, 0), (118, -16, 1), (120, 4),
                        (114, 22), (102, 36), (92, 44), (90, 70), (50, 76)])),
             L(outline([(56, 8), (78, 14), (90, 44), (88, 68), (62, 74)]), 'shade', 'b', False),
             L(outline([(100, 16), (110, 2), (117, -12), (118, 6), (112, 22), (100, 32)]), 'shade', 'b', False)],
}

# Engil (forma Mixi Max): no se le ve la cara: lleva una máscara gris de robot, como una caja redondeada, con tres lentes
# negras redondas (una arriba en el centro y dos abajo) cruzadas por una raya roja, y unas piezas rojas a los lados; encima,
# una melena verde agua enorme y ondulada que le cae por su izquierda (derecha de la imagen) y en dos colas por detrás
GREY = (104, 104, 112, 255)
GREY_D = (74, 74, 82, 255)
LENS = (30, 28, 34, 255)
LRED = (214, 34, 44, 255)


def _lens(cx, cy, r=8.5):
    return [L(ell(cx, cy, r, r), LENS, 'f', False), L([(cx - r + 2, cy), (cx + r - 2, cy)], LRED, 'f', False, False, 2.2)]


CHARS['vr:panca'] = {
    'body': 'normal', 'pal': pal('#8ed8c8', SKIN, shade='#62a898', deep='#4a8274', light='#c4f4ea'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'ears': False, 'hairline': False},
    'front': [L(outline([(80, 30), (96, 46), (104, 70), (98, 92), (108, 110), (96, 120, 1), (90, 104), (84, 86), (88, 66), (80, 52)])),
              L(outline([(4, 54), (-4, 36), (6, 20), (2, 6, 1), (18, 4), (26, -12), (44, -16), (54, -4), (60, -18), (76, -18), (92, -6), (104, 12), (108, 30), (100, 44),
                         (88, 40), (70, 34), (50, 32), (30, 34), (14, 44)])),
              L(outline([(60, -14), (76, -14), (92, -4), (102, 12), (106, 30), (98, 40), (84, 30), (72, 14)]), 'shade', 'b', False),
              L(outline([(88, 50), (100, 70), (94, 92), (102, 108), (96, 114), (88, 98), (84, 76)]), 'shade', 'b', False),
              strand([(20, 14), (34, 26)], 'deep', 'b', 1.0), strand([(44, -6), (50, 20)], 'deep', 'b', 1.0), strand([(70, -6), (80, 20)], 'deep', 'b', 1.0),
              L(blob([(14, 50), (50, 44), (84, 50), (88, 80), (84, 108), (50, 114), (16, 108), (12, 80)], 6), GREY, 'f'),
              L(blob([(62, 48), (84, 50), (88, 80), (84, 108), (66, 112), (74, 80)], 6), GREY_D, 'f', False),
              L(outline([(8, 64), (14, 62), (14, 96), (8, 94)]), LRED, 'f', ln=True), L(outline([(86, 62), (92, 64), (92, 94), (86, 96)]), LRED, 'f', ln=True),
              _lens(50, 62), _lens(34, 90), _lens(66, 90),
              L(outline([(44, 34), (60, 30), (74, 38), (84, 54), (90, 72), (82, 66), (72, 50), (58, 42)]), 'mid', 'f')],
    'side': [L(outline([(30, 30), (10, 40), (-6, 58), (-2, 80), (-12, 100), (-4, 118, 1), (4, 102), (12, 86), (8, 66), (22, 54)])),
             L(outline([(40, 40), (34, 60), (30, 84), (24, 104), (30, 124, 1), (36, 104), (42, 84), (46, 60)])),
             L(outline([(28, 46), (14, 30), (16, 8), (32, -8), (56, -12), (78, -4), (92, 12), (94, 34), (84, 44), (60, 40), (40, 44)])),
             L(outline([(16, 20), (36, 26), (50, 40), (34, 50), (14, 40)]), 'shade', 'b', False),
             L(outline([(38, 42), (60, 40), (84, 44), (94, 60), (92, 96), (82, 110), (56, 112), (42, 100), (36, 70)]), GREY, 'f'),
             L(outline([(36, 70), (60, 72), (92, 70), (92, 96), (82, 110), (56, 112), (42, 100)]), GREY_D, 'f', False),
             L(ell(52, 74, 10, 10), LRED, 'f', ln=True), L(ell(52, 74, 6, 6), LENS, 'f', False), L(ell(52, 74, 3, 3), LRED, 'f', False),
             L(outline([(86, 64), (95, 62), (95, 92), (86, 94)]), LENS, 'f', False),
             L(outline([(40, 40), (60, 34), (82, 38), (92, 46), (70, 48), (50, 50)]), 'mid', 'f')],
    'back': [L(outline([(10, 90), (2, 70), (-6, 50), (-2, 26), (10, 6), (30, -10), (52, -16), (74, -12), (92, 0), (104, 20), (104, 50), (98, 76), (90, 96), (74, 110),
                        (60, 100), (50, 112), (36, 100), (22, 106)])),
             L(outline([(52, -12), (80, -4), (100, 20), (100, 56), (92, 80), (74, 96), (60, 70), (70, 30)]), 'shade', 'b', False),
             L(outline([(16, 30), (30, 24), (34, 40), (20, 44)]), 'light', 'b', False),
             strand([(30, 40), (26, 90)], 'deep', 'b', 1.0), strand([(50, 30), (52, 96)], 'deep', 'b', 1.0), strand([(70, 40), (76, 90)], 'deep', 'b', 1.0)],
}

# Nishiki Ryouma (forma Mixi Max con Zanark): pelo verde agua por su derecha y gris por su izquierda, con flequillo de
# puntas sobre la frente; una coleta larguísima atada en lo alto con un lazo rosa sube y cae en arco por su izquierda
# (derecha de la imagen) hasta el pecho; piel morena, ojos rojos y media sonrisa
CHARS['vr:ryoma-nishiki'] = {
    'body': 'normal', 'pal': pal('#b4dcd2', SKIN, iris=RED, shade='#8a9a96', deep='#6a7876', tie='#e84478'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92,
             'hairline': [(16, 64), (22, 50), (28, 58), (34, 44), (40, 58), (46, 44), (52, 58), (58, 44), (64, 58), (70, 46), (76, 58), (80, 50), (84, 64)]},
    'front': [L(outline([(54, 8), (66, -18), (90, -16), (110, 6), (118, 40), (114, 80), (104, 108), (96, 104, 1), (104, 76), (106, 40), (98, 14), (84, 2), (70, 4), (62, 14)])),
              L(outline([(16, 68), (12, 42), (22, 18), (38, 8), (50, 6), (64, 8), (80, 18), (88, 42), (84, 68), (80, 52), (20, 52)])),
              L(outline([(50, 6), (64, 8), (80, 18), (88, 42), (84, 66), (78, 44), (62, 26), (50, 22)]), 'shade', 'b', False),
              L(outline([(100, 14), (110, 40), (108, 80), (100, 100), (104, 70), (104, 40)]), 'shade', 'b', False),
              L(outline([(44, 4), (52, -6), (60, -4), (58, 10)]), 'tie', 'f', ln=True),
              strand([(30, 20), (34, 40)], 'deep', 'b', 1.0), strand([(70, 20), (66, 40)], 'deep', 'b', 1.0),
              liner(36, 1, w=1.4), liner(64, -1, w=1.4)],
    'side': [L(outline([(48, 4), (60, -18), (40, -38), (10, -40), (-14, -24), (-26, 4), (-28, 40), (-22, 76), (-12, 104), (-4, 96, 1), (-14, 72), (-18, 40), (-12, 10),
                        (2, -14), (22, -24), (40, -18)])),
             L(outline([(76, 54), (82, 46), (92, 44, 1), (86, 36), (96, 30, 1), (86, 22), (84, 10), (66, 0), (44, 2), (22, 12), (8, 32), (6, 56), (18, 68), (34, 64), (44, 56),
                        (60, 54)])),
             L(outline([(8, 30), (30, 36), (40, 58), (24, 66), (8, 56)]), 'shade', 'b', False),
             L(outline([(-18, 10), (-24, 40), (-18, 76), (-8, 96), (-14, 60), (-12, 20)]), 'shade', 'b', False),
             L(outline([(40, -4), (52, -12), (58, -2), (48, 6)]), 'tie', 'f', ln=True)],
    'back': [L(outline([(44, 6), (30, -18), (8, -22), (-12, -6), (-22, 26), (-22, 66), (-14, 102), (-6, 96, 1), (-12, 64), (-12, 28), (-4, 2), (12, -8), (28, -4)])),
             L(outline([(16, 74), (12, 46), (20, 20), (38, 6), (62, 6), (80, 20), (88, 46), (84, 74), (50, 80)])),
             L(outline([(50, 6), (62, 6), (80, 20), (88, 46), (84, 72), (60, 78), (56, 40)]), 'shade', 'b', False),
             L(outline([(-14, 0), (-20, 30), (-18, 70), (-10, 96), (-14, 60), (-12, 20)]), 'shade', 'b', False),
             L(outline([(42, 2), (54, -4), (58, 6), (46, 10)]), 'tie', 'f', ln=True)],
}

# Shinjami (forma Mixi Max): chica de pelo verde azulado oscuro recogido en tres moños en fila sobre la cabeza, atados con
# cintas rojas, de los que salen mechones larguísimos y retorcidos hacia arriba y afuera, como cuernos; tirabuzones finos
# junto a las mejillas, orejas de elfo muy puntiagudas, piel morena y ojos rojos
def _tendril(pts, w=5.0, c='mid', amp=4.0, waves=2.5):
    """Mechón retorcido: la curva pts ondulada (amp unidades a cada lado, waves ondas) y con la punta enroscada."""
    out = []
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        x0, y0 = pts[max(0, i - 1)]
        x1, y1 = pts[min(n - 1, i + 1)]
        dx, dy = x1 - x0, y1 - y0
        d = math.hypot(dx, dy) or 1
        k = amp * math.sin(i / (n - 1) * waves * 2 * math.pi) * (1 - 0.4 * i / n)
        out.append((x - dy / d * k, y + dx / d * k))
    tip = out[-1]
    curl = [(tip[0] + 4 * math.cos(a), tip[1] + 4 * math.sin(a)) for a in [i * 0.6 for i in range(10)]]
    pts = out + curl
    return [L(pts, OUTC, 'b', False, False, w + 2.4), L(pts, c, 'b', False, False, w)]


def _band(cx, cy, w=7, h=7):
    return [L(outline([(cx - w, cy - h), (cx + w, cy - h), (cx + w, cy + h), (cx - w, cy + h)]), 'tie', 'f', ln=True),
            L([(cx - w, cy), (cx + w, cy)], OUTC, 'f', False, False, 1.0)]


CHARS['vr:sapta'] = {
    'body': 'chica', 'pal': pal('#185862', SKIN, iris=RED, shade='#124650', deep='#0c343c', tie='#e03a3e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 94, 'ears': False, 'hairline': (56, 46)},
    'front': [_tendril(quad((30, 12), (6, -16), (-14, -26)) + quad((-14, -26), (-22, -18), (-16, -6))[1:]),
              _tendril(quad((50, 6), (40, -30), (30, -50)) + quad((30, -50), (24, -44), (28, -36))[1:]),
              _tendril(quad((50, 6), (60, -30), (72, -48)) + quad((72, -48), (80, -44), (78, -34))[1:]),
              _tendril(quad((70, 12), (94, -16), (114, -26)) + quad((114, -26), (122, -18), (116, -6))[1:]),
              L(outline([(14, 44), (2, 36), (-10, 32, 1), (6, 50), (16, 58)]), 'skin'), L(outline([(86, 44), (98, 36), (110, 32, 1), (94, 50), (84, 58)]), 'skin'),
              L(outline([(14, 60), (12, 40), (20, 22), (36, 12), (50, 10), (64, 12), (80, 22), (88, 40), (86, 60), (78, 46), (22, 46)])),
              L(ell(30, 12, 10, 12), ln=True), L(ell(70, 12, 10, 12), ln=True), L(ell(50, 4, 10, 13), ln=True),
              _band(30, 18, 8, 3.5), _band(70, 18, 8, 3.5), _band(50, 12, 8, 3.5),
              L(outline([(56, 12), (78, 22), (88, 40), (84, 56), (72, 36)]), 'shade', 'b', False),
              [dict(l, z='f') for l in _tendril(quad((18, 50), (10, 72), (16, 94)), 3.0, amp=3.0, waves=2.0)],
              [dict(l, z='f') for l in _tendril(quad((82, 50), (90, 72), (84, 94)), 3.0, amp=3.0, waves=2.0)],
              liner(36, 1, w=1.4), liner(64, -1, w=1.4)],
    'side': [_tendril(quad((40, 10), (20, -24), (0, -36)) + quad((0, -36), (-8, -30), (-4, -20))[1:]),
             _tendril(quad((54, 4), (60, -30), (76, -44)) + quad((76, -44), (84, -40), (80, -30))[1:]),
             L(outline([(76, 52), (84, 44), (88, 30), (80, 12), (60, 2), (36, 4), (16, 16), (6, 36), (8, 60), (20, 72), (34, 66), (44, 56), (60, 52)])),
             L(outline([(8, 34), (30, 38), (40, 58), (24, 70), (8, 58)]), 'shade', 'b', False),
             L(ell(46, 8, 9, 9)), _band(46, 14, 7, 4),
             L(outline([(40, 62), (30, 46), (20, 36, 1), (42, 52), (50, 66)]), 'skin', 'f'),
             [dict(l, z='f') for l in _tendril(quad((78, 54), (86, 74), (80, 96)), 3.0, amp=3.0, waves=2.0)]],
    'back': [_tendril(quad((30, 12), (6, -16), (-14, -26)) + quad((-14, -26), (-22, -18), (-16, -6))[1:]),
             _tendril(quad((50, 6), (40, -30), (30, -50)) + quad((30, -50), (24, -44), (28, -36))[1:]),
             _tendril(quad((50, 6), (60, -30), (72, -48)) + quad((72, -48), (80, -44), (78, -34))[1:]),
             _tendril(quad((70, 12), (94, -16), (114, -26)) + quad((114, -26), (122, -18), (116, -6))[1:]),
             L(outline([(14, 44), (2, 36), (-10, 32, 1), (6, 50), (16, 58)]), 'skin'), L(outline([(86, 44), (98, 36), (110, 32, 1), (94, 50), (84, 58)]), 'skin'),
             L(outline([(16, 76), (12, 46), (20, 22), (36, 10), (64, 10), (80, 22), (88, 46), (84, 76), (50, 84)])),
             L(outline([(56, 10), (80, 22), (88, 46), (84, 74), (64, 82)]), 'shade', 'b', False),
             L(ell(30, 12, 10, 12), ln=True), L(ell(70, 12, 10, 12), ln=True), L(ell(50, 4, 10, 13), ln=True),
             _band(30, 18, 8, 3.5), _band(70, 18, 8, 3.5), _band(50, 12, 8, 3.5),
             _tendril(quad((22, 70), (16, 88), (22, 104)), 3.0, amp=3.0, waves=2.0), _tendril(quad((78, 70), (84, 88), (78, 104)), 3.0, amp=3.0, waves=2.0)],
}

# Fudou Akio (forma Mixi Max con Zanark): cresta de pelo verde azulado oscuro sobre la cabeza rapada, con las puntas hacia
# arriba y un mechón que le cae por la frente a su derecha (izquierda de la imagen) hasta el ojo; en la sien izquierda, unas
# marcas rojas como de llama; piel morena, ojos rojos y sonrisa de dientes
TATTOO = (196, 40, 44, 255)
CHARS['vr:caleb-stonewall'] = {
    'body': 'normal', 'pal': pal('#1e5c74', SKIN, iris=RED, shade='#164656', deep='#0e3240', scalp='#8e4e34'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 92, 'hairline': False},
    'front': [L(outline([(26, 40), (24, 20), (28, 4), (18, -14, 1), (36, -4), (44, -20, 1), (52, -2), (66, -12, 1), (64, 6), (76, 10), (70, 22), (66, 40)])),
              L(outline([(52, -2), (66, -10), (64, 6), (76, 10), (70, 22), (64, 36), (58, 20)]), 'shade', 'b', False),
              L(blob([(19, 52), (24, 34), (50, 22), (76, 34), (81, 52)], 6), 'scalp', 'f', False),
              L(outline([(28, 28), (36, 8), (52, 4), (66, 16), (62, 34), (52, 46), (44, 66), (38, 74, 1), (34, 60), (26, 70, 1), (24, 54), (18, 62, 1), (20, 44)]), 'mid', 'f'),
              L(outline([(48, 10), (62, 18), (58, 32), (50, 42)]), 'shade', 'f', False),
              L(outline([(64, 50), (74, 44), (76, 52), (70, 54), (76, 60), (66, 62), (70, 56)]), TATTOO, 'f', False),
              L([(72, 40), (78, 46)], TATTOO, 'f', False, False, 2.0),
              liner(36, 1, w=1.4), liner(64, -1, w=1.4)],
    'side': [L(outline([(70, 30), (84, 26), (90, 12, 1), (76, 8), (82, -10, 1), (62, -2), (60, -22, 1), (44, -6), (30, -16, 1), (28, 2), (12, 6, 1), (22, 16), (36, 30),
                        (54, 30)])),
             L(outline([(40, 10), (60, 4), (76, 8), (70, 26), (50, 28)]), 'shade', 'b', False),
             L(outline([(16, 40), (26, 26), (52, 22), (76, 30), (80, 40), (60, 36), (36, 40), (22, 60)]), 'scalp', 'f', False),
             L(outline([(74, 30), (88, 32), (92, 46), (86, 58, 1), (82, 44), (74, 40)]), 'mid', 'f')],
    'back': [L(outline([(36, 50), (32, 30), (34, 10), (26, -8, 1), (40, 0), (48, -16, 1), (54, 0), (68, -10, 1), (66, 10), (68, 30), (64, 50), (50, 56)])),
             L(outline([(54, 0), (68, -8), (66, 10), (68, 30), (64, 48), (56, 40)]), 'shade', 'b', False),
             L(blob([(20, 60), (22, 34), (50, 20), (78, 34), (80, 60), (74, 84), (50, 94), (26, 84)], 6), 'scalp', 'b', False),
             L(outline([(36, 50), (32, 30), (34, 10), (26, -8, 1), (40, 0), (48, -16, 1), (54, 0), (68, -10, 1), (66, 10), (68, 30), (64, 50), (50, 56)]), 'mid', 'f', False, ln=True),
             L(outline([(54, 0), (68, -8), (66, 10), (68, 30), (64, 48), (56, 40)]), 'shade', 'f', False)],
}

# Arachnes (forma Mixi Max): chica de melena corta verde azulada, lisa y abombada, con flequillo largo de raya en medio y
# dos rizos enormes a los lados de la cabeza que se enroscan hacia arriba como cuernos de carnero; labios negros, pestañas
# largas y ojos rojos
LIPS = (36, 26, 34, 255)


def _ram(s, z='b'):
    """Rizo grande de un lado (s=1 izquierda de la imagen, -1 derecha), que sale de la melena y se enrosca hacia arriba."""
    m = lambda pts: [(50 + (q[0] - 50) * s,) + tuple(q[1:]) for q in pts]  # noqa: E731
    return L(outline(m([(18, 70), (6, 72), (-6, 60), (-10, 40), (-8, 18), (0, 4), (10, 0, 1), (6, 12), (2, 26), (2, 44), (8, 56), (18, 54)])), 'mid', z)


CHARS['vr:arachne'] = {
    'body': 'chica', 'pal': pal('#2aa0ae', SKIN, iris=RED, shade='#1e7c88', deep='#145c66', light='#6cd0da'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'hairline': [(16, 66), (22, 54), (34, 48), (46, 54), (50, 46), (54, 54), (66, 48), (78, 54), (84, 66)]},
    'front': [_ram(1), _ram(-1),
              L(outline([(12, 86), (8, 60), (12, 34), (26, 14), (50, 6), (74, 14), (88, 34), (92, 60), (88, 86), (80, 90), (80, 60), (20, 60), (20, 90)])),
              L(outline([(56, 8), (76, 16), (88, 36), (90, 62), (86, 84), (80, 60), (72, 36)]), 'shade', 'b', False),
              L(outline([(-8, 22), (-4, 40), (2, 56), (2, 30)]), 'shade', 'b', False), L(outline([(108, 22), (104, 40), (98, 56), (98, 30)]), 'shade', 'b', False),
              L(outline([(28, 22), (40, 14), (44, 22), (32, 30)]), 'light', 'b', False),
              strand([(50, 8), (50, 40)], 'deep', 'b', 1.0),
              L([(26, 70), (22, 66)], OUTC, 'f', False, False, 1.4), L([(74, 70), (78, 66)], OUTC, 'f', False, False, 1.4),
              liner(36, 1, w=1.4), liner(64, -1, w=1.4),
              L(quad((44, 92), (50, 89), (56, 92)) + quad((56, 92), (50, 97), (44, 92))[1:], LIPS, 'f', False)],
    'side': [L(outline([(20, 50), (8, 40), (0, 22), (10, 6), (22, 2, 1), (16, 12), (14, 26), (22, 38)])),
             L(outline([(78, 56), (84, 42), (88, 26), (78, 10), (56, 2), (30, 6), (12, 22), (4, 46), (6, 70), (16, 90), (36, 92), (44, 80), (44, 62), (60, 56)])),
             L(outline([(6, 40), (30, 46), (40, 80), (30, 90), (12, 84)]), 'shade', 'b', False),
             L(outline([(78, 56), (86, 64), (88, 84), (82, 92), (78, 76)]), 'mid', 'f')],
    'back': [_ram(1), _ram(-1),
             L(outline([(10, 86), (8, 56), (14, 30), (28, 12), (50, 6), (72, 12), (86, 30), (92, 56), (90, 86), (70, 92), (50, 88), (30, 92)])),
             L(outline([(54, 8), (74, 14), (88, 34), (92, 60), (88, 86), (66, 90), (56, 40)]), 'shade', 'b', False),
             strand([(50, 30), (50, 88)], 'deep', 'b', 1.0)],
}

# Seki Ganjirou (Grizzly, forma Mixi Max): grandullón de cara redonda; melena de pinchos verde azulado muy oscuro que le
# rodea toda la cabeza, con unos pinchos más claros encima de la frente; ojos redondos pequeños, cejas gruesas fruncidas y
# los dientes apretados en una mueca
CHARS['vr:grisley-bear'] = {
    'body': 'corpulento', 'pal': pal('#163e4e', SKIN, iris='#1a1418', shade='#0e2e3a', deep='#08202a', front='#3a98a4', front_d='#2a7682'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'none', 'eye_y': 80, 'eye_sep': 15, 'ear_out': 4, 'hairline': False,
             'face_front': blob([(16, 50), (50, 40), (84, 50), (90, 76), (86, 100), (66, 112), (50, 114), (34, 112), (14, 100), (10, 76)])},
    'front': [L(outline([(14, 90), (0, 86, 1), (6, 74), (-10, 64, 1), (4, 54), (-8, 40, 1), (8, 34), (2, 18, 1), (18, 18), (16, 2, 1), (32, 8), (36, -10, 1), (48, 4),
                         (58, -12, 1), (64, 4), (80, 0, 1), (80, 14), (96, 14, 1), (92, 28), (108, 36, 1), (96, 46), (110, 60, 1), (96, 66), (104, 82, 1), (88, 88),
                         (84, 60), (16, 60)])),
              L(outline([(60, -8), (64, 4), (80, 2), (80, 16), (94, 16), (92, 30), (104, 38), (94, 48), (104, 60), (88, 62), (78, 40)]), 'shade', 'b', False),
              L(outline([(22, 56), (24, 38), (14, 30, 1), (30, 30), (32, 16, 1), (42, 26), (50, 10, 1), (56, 26), (68, 16, 1), (70, 30), (86, 30, 1), (76, 40), (78, 56),
                         (66, 48), (58, 58, 1), (50, 46), (42, 58, 1), (34, 48)]), 'front', 'f'),
              L(outline([(50, 12), (56, 26), (68, 18), (70, 30), (84, 32), (76, 40), (76, 52), (66, 46), (58, 54), (54, 40)]), 'front_d', 'f', False),
              L([(24, 66), (32, 64), (44, 70)], OUTC, 'f', False, False, 3.6), L([(76, 66), (68, 64), (56, 70)], OUTC, 'f', False, False, 3.6),
              L([(44, 74), (50, 78), (56, 74)], OUTC, 'f', False, False, 1.0),
              L(outline([(32, 96), (68, 96), (64, 104), (50, 106), (36, 104)]), WHITE, 'f', False),
              L([(30, 94), (40, 96), (60, 96), (70, 94), (64, 104), (50, 106), (36, 104), (30, 94)], OUTC, 'f', False, False, 1.6),
              L([(33, 100), (67, 100)], OUTC, 'f', False, False, 1.0),
              L([(42, 96), (42, 105)], OUTC, 'f', False, False, 0.8), L([(50, 96), (50, 106)], OUTC, 'f', False, False, 0.8), L([(58, 96), (58, 105)], OUTC, 'f', False, False, 0.8)],
    'side': [L(outline([(74, 50), (78, 38), (90, 30, 1), (80, 22), (88, 8, 1), (70, 8), (72, -10, 1), (56, 0), (46, -14, 1), (36, 4), (18, -2, 1), (20, 14), (0, 12, 1),
                        (8, 28), (-12, 34, 1), (2, 44), (-12, 58, 1), (4, 62), (-6, 80, 1), (10, 80), (6, 96, 1), (22, 88), (34, 96, 1), (38, 78), (44, 60), (60, 54)])),
             L(outline([(0, 40), (24, 46), (36, 76), (22, 88), (4, 76)]), 'shade', 'b', False),
             L(outline([(70, 52), (76, 38), (88, 34, 1), (80, 44), (92, 50, 1), (80, 54), (88, 64, 1), (76, 62)]), 'front', 'f'),
             L(outline([(80, 64), (88, 96), (78, 100)]), 'skin', 'f', False)],
    'back': [L(outline([(14, 96), (2, 90, 1), (6, 76), (-10, 66, 1), (4, 56), (-8, 42, 1), (8, 34), (2, 18, 1), (18, 18), (16, 2, 1), (32, 8), (38, -10, 1), (48, 4),
                        (58, -12, 1), (64, 4), (80, 0, 1), (80, 14), (96, 16, 1), (92, 30), (108, 38, 1), (96, 48), (110, 62, 1), (96, 70), (104, 86, 1), (88, 92), (74, 100, 1),
                        (64, 92), (50, 102, 1), (38, 92), (26, 102, 1)])),
             L(outline([(58, -8), (66, 6), (80, 4), (80, 18), (94, 18), (92, 32), (104, 40), (94, 50), (104, 64), (94, 72), (98, 84), (86, 90), (74, 96), (64, 88),
                        (60, 40)]), 'shade', 'b', False)],
}

# Zanark Avalonic (forma Mixi Max): pelo verde azulado de pinchos gruesos hacia arriba y a los lados, más largo y erizado
# que de normal, y mechones de punta sobre la frente; piel morena, ojos rojos con marcas verdes debajo y sonrisa de dientes;
# hombreras enormes del mismo verde (de la armadura del Mixi Max)
MARK = (40, 150, 150, 255)
CHARS['vr:zanark-avalonic'] = {
    'body': 'corpulento', 'pal': pal('#2c9a9c', SKIN, iris=RED, shade='#1f7678', deep='#165658', light='#6ad0cc'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 93,
             'hairline': [(16, 66), (20, 52), (28, 60), (34, 46), (42, 58), (50, 44), (58, 58), (66, 46), (72, 60), (80, 52), (84, 66)]},
    'front': [L(outline([(16, 70), (2, 66, 1), (10, 54), (-6, 40, 1), (10, 34), (4, 14, 1), (20, 16), (18, -8, 1), (34, 6), (40, -26, 1), (50, 0), (62, -22, 1), (64, 4),
                         (82, -6, 1), (80, 14), (98, 12, 1), (90, 32), (106, 40, 1), (92, 52), (100, 66, 1), (84, 70), (80, 54), (20, 54)])),
              L(outline([(56, -10), (62, -18), (64, 6), (80, -2), (80, 16), (94, 16), (88, 34), (100, 42), (88, 52), (78, 36), (66, 22)]), 'shade', 'b', False),
              L(outline([(36, 10), (42, -18), (48, 6), (44, 20)]), 'light', 'b', False),
              strand([(26, 30), (34, 44)], 'deep', 'b', 1.0), strand([(74, 30), (66, 44)], 'deep', 'b', 1.0),
              L([(28, 82), (34, 86)], MARK, 'f', False, False, 1.6), L([(72, 82), (66, 86)], MARK, 'f', False, False, 1.6),
              liner(36, 1, w=1.6), liner(64, -1, w=1.6)],
    'side': [L(outline([(76, 56), (82, 46), (96, 46, 1), (86, 36), (100, 26, 1), (86, 22), (94, 6, 1), (76, 6), (80, -14, 1), (62, -2), (56, -26, 1), (44, -4), (26, -20, 1),
                        (24, 2), (4, 0, 1), (12, 16), (-10, 22, 1), (4, 34), (-12, 46, 1), (4, 52), (-6, 66, 1), (12, 66), (24, 72), (36, 64), (46, 56), (62, 54)])),
             L(outline([(4, 30), (28, 36), (40, 58), (24, 70), (8, 60)]), 'shade', 'b', False),
             strand([(40, 4), (64, 22)], 'deep', 'b', 1.0), strand([(20, 20), (46, 34)], 'deep', 'b', 1.0)],
    'back': [L(outline([(16, 82), (4, 78, 1), (10, 64), (-6, 50, 1), (10, 40), (4, 18, 1), (20, 18), (18, -6, 1), (34, 6), (40, -26, 1), (50, 0), (62, -22, 1), (64, 4),
                        (82, -6, 1), (80, 16), (98, 16, 1), (90, 36), (106, 48, 1), (92, 60), (98, 78, 1), (84, 82), (66, 88, 1), (58, 80), (50, 90, 1), (42, 80), (32, 88, 1)])),
             L(outline([(56, -10), (62, -18), (64, 6), (80, -2), (80, 18), (94, 18), (88, 36), (100, 48), (90, 58), (94, 74), (82, 80), (64, 84), (60, 40)]), 'shade', 'b', False)],
}

# Baddap Sleed (forma Mixi Max): pelo verde agua de pinchos que se echan hacia atrás en lo alto y le cae largo y liso por
# los lados hasta los hombros; en la frente, un símbolo negro como un tercer ojo; piel morena, ojos rojos y gesto serio
CHARS['vr:bash-lancer'] = {
    'body': 'normal', 'pal': pal('#a4d8d2', SKIN, iris=RED, shade='#7cb0aa', deep='#5e8c88', light='#d4f4f0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94,
             'hairline': [(16, 64), (22, 50), (30, 58), (36, 46), (44, 56), (50, 48), (56, 56), (64, 46), (70, 58), (78, 50), (84, 64)]},
    'front': [L(outline([(10, 116, 1), (8, 90), (10, 64), (-2, 52, 1), (8, 42), (0, 26, 1), (16, 22), (12, 4, 1), (30, 8), (36, -12, 1), (48, 2), (60, -14, 1), (64, 4),
                         (86, -4, 1), (82, 14), (102, 20, 1), (90, 34), (100, 48, 1), (90, 56), (92, 84), (92, 116, 1), (84, 102), (78, 116, 1), (80, 86), (80, 54), (20, 54),
                         (20, 86), (22, 116, 1), (16, 102)])),
              L(outline([(58, -8), (64, 4), (84, 0), (82, 16), (98, 22), (88, 36), (96, 48), (88, 56), (90, 84), (90, 110), (82, 96), (82, 60), (74, 30)]), 'shade', 'b', False),
              L(outline([(10, 70), (16, 60), (18, 90), (14, 108), (10, 96)]), 'shade', 'b', False),
              strand([(30, 14), (40, 34)], 'deep', 'b', 1.0), strand([(70, 14), (62, 34)], 'deep', 'b', 1.0),
              L(ell(50, 58, 3.6, 3.6), OUTC, 'f', False), L([(44, 64), (56, 64)], OUTC, 'f', False, False, 1.4),
              liner(36, 1, w=1.4), liner(64, -1, w=1.4)],
    'side': [L(outline([(76, 54), (82, 46), (92, 42, 1), (84, 34), (94, 24, 1), (82, 20), (88, 4, 1), (70, 6), (70, -12, 1), (54, 0), (40, -14, 1), (34, 4), (14, 0, 1), (16, 16),
                        (2, 24, 1), (4, 46), (0, 80), (2, 112), (12, 122, 1), (20, 110), (30, 120, 1), (32, 96), (36, 74), (44, 60), (60, 54)])),
             L(outline([(4, 36), (28, 42), (36, 74), (30, 112), (14, 116), (4, 90)]), 'shade', 'b', False),
             strand([(36, 6), (60, 20)], 'deep', 'b', 1.0)],
    'back': [L(outline([(8, 116, 1), (6, 86), (8, 58), (-2, 46, 1), (8, 36), (2, 20, 1), (18, 18), (14, 2, 1), (32, 8), (38, -12, 1), (50, 2), (62, -14, 1), (66, 4),
                        (86, -2, 1), (84, 16), (102, 22, 1), (92, 38), (100, 50, 1), (92, 60), (94, 86), (92, 116, 1), (80, 106), (68, 120, 1), (58, 108), (50, 122, 1),
                        (42, 108), (32, 120, 1), (20, 106)])),
             L(outline([(58, -8), (66, 4), (84, 2), (84, 18), (98, 24), (90, 40), (96, 50), (90, 60), (92, 86), (90, 112), (78, 104), (66, 116), (58, 104), (60, 40)]),
               'shade', 'b', False),
             strand([(30, 30), (28, 104)], 'deep', 'b', 1.0), strand([(50, 30), (50, 112)], 'deep', 'b', 1.0), strand([(70, 30), (72, 104)], 'deep', 'b', 1.0)],
}

# Clara Jane (forma Mixi Max, 巨大台風クララジェーン): no se le ve la cabeza: va envuelta en un tifón, un cono en espiral de
# bandas verde agua y rojas que acaba en punta arriba, con una vuelta verde clarito abajo y un hueco azul oscuro en el sitio
# de la cara
TEAL = (64, 186, 196, 255)
TEAL_D = (40, 130, 140, 255)
CRIM = (214, 34, 72, 255)
MINT = (176, 236, 226, 255)
NAVY = (14, 44, 92, 255)


def _band_front(y, h, w0, w1, c, tilt=6):
    """Vuelta del tifón de frente: banda inclinada de alto h entre los anchos w0 (arriba) y w1 (abajo)."""
    return L(outline([(50 - w0, y + tilt), (50 + w0, y - tilt), (50 + w1, y + h - tilt), (50 - w1, y + h + tilt)]), c, 'f', False)


_CONE_F = outline([(50, -36, 1), (60, -12), (76, 6), (86, 26), (96, 50), (104, 76), (106, 100), (96, 118), (50, 122), (4, 118), (-6, 100), (-4, 76), (4, 50),
                   (14, 26), (24, 6), (40, -12)])
_CONE_S = outline([(50, -36, 1), (60, -12), (76, 6), (88, 26), (98, 50), (104, 76), (102, 100), (90, 118), (40, 122), (2, 116), (-4, 96), (0, 70), (8, 46),
                   (18, 24), (30, 4), (42, -14)])
CHARS['vr:hurricane-zeta'] = {
    'body': 'chica', 'pal': pal('#40bac4', SKIN, shade='#28828c', deep='#1c5c64'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'ears': False, 'hairline': False, 'no_head': True},
    'front': [L(_CONE_F, TEAL, 'b'), L(_CONE_F, TEAL, 'f', False),
              _band_front(-14, 12, 6, 14, CRIM, 4), _band_front(4, 14, 18, 27, CRIM), _band_front(28, 14, 29, 37, CRIM),
              _band_front(52, 12, 40, 46, CRIM), _band_front(20, 6, 24, 28, TEAL_D, 5), _band_front(44, 6, 35, 39, TEAL_D, 5),
              L(outline([(14, 70), (50, 62), (86, 72), (84, 96), (50, 100), (16, 94)]), NAVY, 'f', False),
              L(outline([(-6, 96), (20, 86), (50, 94), (80, 90), (106, 98), (100, 112), (70, 104), (50, 108), (24, 102), (2, 112)]), MINT, 'f', False),
              L(outline([(-4, 108), (30, 112), (70, 110), (104, 108), (96, 120), (50, 122), (4, 120)]), TEAL_D, 'f', False),
              L([(30, -2), (50, -10), (70, -16)], OUTC, 'f', False, False, 1.0), L([(62, -14), (84, -18)], OUTC, 'f', False, False, 1.4)],
    'side': [L(_CONE_S, TEAL, 'b'), L(_CONE_S, TEAL, 'f', False),
             _band_front(-14, 12, 6, 14, CRIM, 2), _band_front(4, 14, 18, 28, CRIM, 3), _band_front(30, 14, 31, 39, CRIM, 3),
             _band_front(80, 12, 46, 48, CRIM, 3),
             L(outline([(2, 64), (50, 56), (102, 60), (104, 74), (50, 72), (0, 80)]), MINT, 'f', False),
             L(outline([(86, 60), (104, 54), (100, 74)]), NAVY, 'f', False),
             L(outline([(90, 96), (114, 84), (100, 100)]), MINT, 'f', ln=True)],
    'back': [L(_CONE_F, TEAL, 'b'), L(_CONE_F, TEAL, 'f', False),
             _band_front(-14, 12, 6, 14, CRIM, -4), _band_front(6, 14, 18, 27, CRIM, -5), _band_front(30, 14, 29, 37, CRIM, -5),
             _band_front(56, 14, 41, 47, CRIM, -5), _band_front(80, 10, 48, 50, CRIM, -5),
             L(outline([(4, 98), (50, 90), (100, 96), (104, 110), (50, 106), (0, 112)]), MINT, 'f', False)],
}

# Desuta (forma Mixi Max): una melena enorme de pinchos verde azulado oscuro que le sale de la cabeza en todas direcciones,
# muy alta por arriba y abierta a los lados hasta los hombros; ojos rojos grandes y sonrisa tranquila
CHARS['vr:destra'] = {
    'body': 'normal', 'pal': pal('#1c5260', SKIN, iris=RED, shade='#143e4a', deep='#0c2c36', light='#3a8494'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92,
             'hairline': [(16, 64), (22, 50), (30, 58), (38, 44), (46, 58), (52, 46), (58, 58), (66, 44), (72, 58), (80, 50), (84, 64)]},
    'front': [L(outline([(16, 76), (0, 90, 1), (6, 72), (-14, 74, 1), (2, 60), (-12, 50, 1), (6, 44), (-4, 30, 1), (12, 28), (8, 8, 1), (22, 14), (20, -14, 1), (34, 2),
                         (36, -26, 1), (46, -2), (52, -30, 1), (58, -2), (68, -24, 1), (68, 4), (84, -10, 1), (80, 14), (98, 6, 1), (90, 28), (108, 30, 1), (94, 44),
                         (112, 50, 1), (96, 60), (114, 74, 1), (94, 74), (100, 90, 1), (84, 76), (80, 54), (20, 54)])),
              L(outline([(54, -24), (58, -2), (68, -20), (68, 4), (84, -6), (80, 14), (96, 8), (90, 28), (106, 32), (94, 44), (108, 52), (96, 60), (110, 72), (92, 72),
                         (82, 50), (72, 26)]), 'shade', 'b', False),
              L(outline([(24, 20), (34, 4), (38, 24)]), 'light', 'b', False), L(outline([(46, 4), (52, -20), (54, 10)]), 'light', 'b', False),
              strand([(30, 30), (36, 46)], 'deep', 'b', 1.0), strand([(70, 30), (64, 46)], 'deep', 'b', 1.0)],
    'side': [L(outline([(76, 56), (82, 46), (94, 44, 1), (86, 36), (98, 26, 1), (84, 22), (92, 4, 1), (74, 8), (76, -16, 1), (60, -2), (52, -28, 1), (42, -4), (24, -22, 1),
                        (22, 0), (0, -6, 1), (8, 14), (-14, 16, 1), (2, 30), (-18, 40, 1), (0, 48), (-16, 64, 1), (2, 66), (-10, 86, 1), (10, 80), (8, 100, 1), (22, 86),
                        (32, 102, 1), (36, 80), (44, 60), (60, 54)])),
             L(outline([(0, 34), (26, 40), (40, 64), (30, 88), (12, 84)]), 'shade', 'b', False),
             strand([(40, 0), (62, 20)], 'deep', 'b', 1.0), strand([(14, 20), (44, 36)], 'deep', 'b', 1.0)],
    'back': [L(outline([(20, 96), (0, 100, 1), (6, 80), (-14, 82, 1), (0, 66), (-14, 56, 1), (4, 46), (-6, 30, 1), (12, 28), (8, 6, 1), (22, 14), (22, -14, 1), (34, 2),
                        (38, -26, 1), (46, -2), (52, -30, 1), (58, -2), (68, -24, 1), (68, 4), (84, -10, 1), (80, 14), (96, 6, 1), (90, 28), (108, 30, 1), (96, 46),
                        (114, 56, 1), (96, 66), (114, 82, 1), (94, 80), (100, 100, 1), (80, 96), (64, 104, 1), (56, 94), (50, 106, 1), (42, 94), (34, 104, 1)])),
             L(outline([(54, -24), (58, -2), (68, -20), (68, 4), (84, -6), (80, 14), (96, 8), (90, 28), (106, 32), (96, 46), (110, 56), (96, 66), (110, 80), (94, 80),
                        (96, 96), (80, 92), (64, 100), (56, 90), (60, 40)]), 'shade', 'b', False)],
}

# Zagomel Zande (forma Mixi Max): cresta de pelo verde agua en pinchos hacia arriba, con los lados rapados; unas gafas de
# soldador de cristales verdes le tapan el ojo derecho, con la correa marrón cruzándole la cabeza en diagonal; colmillos
# blancos que le salen de la boca hacia arriba, dientes apretados, orejas grandes y ojo izquierdo enfadado
STRAP = (66, 40, 32, 255)
STRAP_E = (196, 102, 52, 255)
RIM = (150, 150, 90, 255)
GLASS = (110, 130, 40, 255)


def _goggle(cx, cy, r=7.5):
    return [L(ell(cx, cy, r + 2.6, r + 2.6), RIM, 'f', ln=True), L(ell(cx, cy, r, r), GLASS, 'f', False), L(ell(cx - 2, cy - 2, 2, 2), (190, 210, 110, 255), 'f', False)]


def _tusk(s):
    m = lambda pts: [(50 + (q[0] - 50) * s,) + tuple(q[1:]) for q in pts]  # noqa: E731
    return L(outline(m([(30, 100), (24, 96), (20, 86), (22, 76, 1), (26, 86), (32, 94)])), WHITE, 'f', ln=True)


CHARS['vr:lars-luceaf-r'] = {
    'body': 'corpulento', 'pal': pal('#a4d4ce', SKIN, iris='#1a1418', shade='#7caca6', deep='#5e8a84', scalp='#94543a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'big_ears': 3, 'ear_out': 4, 'hairline': False, 'eye_y': 80,
             'face_front': blob([(16, 50), (50, 40), (84, 50), (88, 76), (84, 100), (66, 112), (50, 114), (34, 112), (16, 100), (12, 76)])},
    'front': [L(outline([(30, 48), (28, 28), (24, 14, 1), (36, 20), (38, -8, 1), (48, 10), (58, -20, 1), (62, 6), (76, 0, 1), (70, 24), (72, 48)])),
              L(outline([(58, -16), (62, 6), (74, 4), (70, 24), (70, 44), (60, 30)]), 'shade', 'b', False),
              L(outline([(30, 50), (28, 30), (24, 14, 1), (36, 22), (38, -6, 1), (48, 12), (58, -18, 1), (62, 8), (76, 2, 1), (70, 26), (70, 50), (50, 56)]), 'mid', 'f', False, ln=True),
              L(outline([(58, -14), (62, 8), (74, 6), (70, 26), (68, 46), (60, 32)]), 'shade', 'f', False),
              L(outline([(14, 70), (78, 38), (88, 46), (20, 82)]), STRAP, 'f', ln=True),
              L([(15, 72), (79, 40)], STRAP_E, 'f', False, False, 1.4), L([(19, 80), (87, 48)], STRAP_E, 'f', False, False, 1.4),
              _goggle(52, 60), _goggle(34, 76),
              L(outline([(56, 78), (72, 74), (74, 82), (58, 84)]), WHITE, 'f', ln=True), L(ell(66, 79, 2.6, 2.6), OUTC, 'f', False),
              L([(54, 72), (76, 66)], OUTC, 'f', False, False, 3.2),
              L(outline([(44, 84), (50, 82), (56, 84), (56, 92), (44, 92)]), 'skin_d', 'f', False),
              L(outline([(30, 96), (70, 96), (70, 104), (30, 104)]), WHITE, 'f', False),
              L([(30, 96), (70, 96), (70, 104), (30, 104), (30, 96)], OUTC, 'f', False, False, 1.6), L([(30, 100), (70, 100)], OUTC, 'f', False, False, 1.0),
              _tusk(1), _tusk(-1)],
    'side': [L(outline([(70, 30), (82, 22), (92, 0, 1), (78, 8), (70, -18, 1), (58, 4), (44, -4, 1), (40, 8), (16, 8, 1), (28, 20), (40, 30), (56, 32)])),
             L(outline([(56, 4), (70, -14), (78, 10), (70, 28), (56, 28)]), 'shade', 'b', False),
             L(outline([(14, 50), (24, 32), (50, 26), (76, 32), (80, 40), (56, 38), (34, 44), (20, 62)]), 'scalp', 'f', False),
             L(outline([(4, 52), (40, 56), (86, 50), (88, 60), (40, 66), (6, 62)]), STRAP, 'f', ln=True),
             L([(4, 54), (40, 58), (86, 52)], STRAP_E, 'f', False, False, 1.2),
             L(outline([(82, 46), (94, 44), (96, 70), (84, 70)]), RIM, 'f', ln=True), L(outline([(88, 48), (94, 48), (94, 66), (88, 66)]), GLASS, 'f', False),
             L(outline([(76, 102), (82, 96), (84, 84, 1), (86, 96), (82, 104)]), WHITE, 'f', ln=True)],
    'back': [L(outline([(30, 50), (28, 28), (22, 12, 1), (36, 18), (36, -10, 1), (48, 8), (58, -20, 1), (62, 6), (78, -2, 1), (70, 24), (72, 50), (50, 56)])),
             L(outline([(58, -16), (62, 6), (76, 2), (70, 24), (70, 46), (60, 30)]), 'shade', 'b', False),
             L(blob([(16, 60), (22, 34), (50, 22), (78, 34), (84, 60), (78, 86), (50, 96), (22, 86)], 6), 'scalp', 'b', False),
             L(outline([(30, 50), (28, 28), (22, 12, 1), (36, 18), (36, -10, 1), (48, 8), (58, -20, 1), (62, 6), (78, -2, 1), (70, 24), (72, 50), (50, 56)]), 'mid', 'f', False, ln=True),
             L(outline([(58, -16), (62, 6), (76, 2), (70, 24), (70, 46), (60, 30)]), 'shade', 'f', False),
             L(outline([(18, 40), (28, 30), (84, 86), (76, 96)]), STRAP, 'f', ln=True),
             L([(20, 38), (82, 90)], STRAP_E, 'f', False, False, 1.2)],
}

# Venom (ベノム・ブラグ, forma Mixi Max): una melena enorme, rizada y despeinada de color verde grisáceo que le tapa la cabeza y
# le cae hasta los hombros; una visera granate de rayas le tapa los ojos, con dos tiras que le bajan por las mejillas; piel
# morena y bigote negro
VISOR = (140, 30, 48, 255)
VISOR_D = (92, 18, 30, 255)
CHARS['vr:venom-braggard'] = {
    'body': 'normal', 'pal': pal('#a8ccc4', SKIN, shade='#7e8e8a', deep='#5e6c6a', light='#c8ece4'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': [(16, 66), (24, 52), (36, 48), (46, 56), (54, 48), (64, 54), (76, 50), (84, 66)]},
    'front': [L(outline([(-2, 124), (-8, 108, 1), (0, 96), (-10, 82, 1), (2, 70), (-6, 54, 1), (6, 44), (0, 26, 1), (12, 18), (10, 2, 1), (24, 2), (28, -12, 1), (40, -6),
                         (50, -16, 1), (60, -6), (72, -12, 1), (78, 2), (92, 2, 1), (90, 18), (104, 26, 1), (96, 42), (108, 54, 1), (98, 68), (108, 82, 1), (98, 96),
                         (106, 110, 1), (100, 124), (82, 118), (80, 64), (20, 64), (18, 118)])),
              L(outline([(56, -6), (72, -8), (78, 4), (90, 6), (88, 20), (100, 28), (94, 42), (104, 54), (96, 68), (104, 82), (96, 96), (102, 110), (98, 120), (84, 114),
                         (82, 62), (74, 30)]), 'shade', 'b', False),
              L(outline([(4, 74), (14, 66), (16, 96), (10, 110), (2, 96)]), 'shade', 'b', False),
              L(outline([(20, 20), (30, 12), (36, 22), (26, 30)]), 'light', 'b', False), L(outline([(46, 6), (56, 2), (60, 14), (48, 16)]), 'light', 'b', False),
              L(outline([(16, 64), (84, 64), (84, 82), (16, 82)]), VISOR, 'f', ln=True),
              L([(16, 70), (84, 70)], VISOR_D, 'f', False, False, 1.6), L([(16, 76), (84, 76)], VISOR_D, 'f', False, False, 1.6),
              L(outline([(18, 82), (26, 82), (26, 116), (18, 116)]), VISOR, 'f', ln=True), L(outline([(74, 82), (82, 82), (82, 116), (74, 116)]), VISOR, 'f', ln=True),
              L(outline([(30, 46), (40, 42), (46, 54), (44, 70), (48, 80, 1), (40, 70), (36, 56)]), 'mid', 'f'),
              L(outline([(56, 46), (66, 44), (70, 56), (62, 64), (66, 80, 1), (58, 66)]), 'mid', 'f'),
              L(quad((40, 94), (50, 90), (60, 94)) + [(58, 96), (50, 93), (42, 96)], OUTC, 'f', False)],
    'side': [L(outline([(76, 54), (82, 44), (94, 36, 1), (88, 24), (96, 12, 1), (84, 6), (86, -10, 1), (70, -4), (60, -18, 1), (46, -6), (30, -14, 1), (24, 2), (6, 0, 1),
                        (10, 16), (-8, 24, 1), (2, 38), (-12, 52, 1), (0, 62), (-10, 80, 1), (0, 92), (-8, 108, 1), (2, 118), (12, 130, 1), (24, 118), (36, 128, 1), (40, 106),
                        (40, 82), (46, 62), (62, 56)])),
             L(outline([(0, 40), (26, 48), (36, 80), (32, 118), (8, 120), (-2, 90)]), 'shade', 'b', False),
             L(outline([(46, 64), (88, 62), (90, 80), (48, 82)]), VISOR, 'f', ln=True), L([(48, 70), (88, 69)], VISOR_D, 'f', False, False, 1.4),
             L(outline([(84, 80), (90, 80), (90, 114), (84, 114)]), VISOR, 'f', ln=True),
             L(outline([(76, 52), (86, 58), (84, 70), (78, 64)]), 'mid', 'f'),
             L([(84, 94), (90, 96)], OUTC, 'f', False, False, 2.0)],
    'back': [L(outline([(-4, 124), (-10, 108, 1), (-2, 96), (-12, 82, 1), (0, 70), (-8, 54, 1), (4, 44), (-2, 26, 1), (12, 18), (10, 2, 1), (24, 2), (28, -12, 1), (40, -6),
                        (50, -16, 1), (60, -6), (72, -12, 1), (78, 2), (92, 2, 1), (90, 18), (104, 26, 1), (98, 42), (110, 54, 1), (100, 68), (110, 82, 1), (100, 96),
                        (108, 110, 1), (104, 124), (80, 118), (64, 128, 1), (50, 118), (36, 128, 1), (20, 118)])),
             L(outline([(4, 60), (20, 44), (40, 52), (56, 40), (78, 48), (96, 40), (100, 70), (96, 100), (84, 116), (66, 106), (50, 116), (32, 104), (14, 114), (2, 96)]),
               'shade', 'b', False),
             strand([(26, 60), (20, 104)], 'deep', 'b', 1.0), strand([(50, 54), (50, 110)], 'deep', 'b', 1.0), strand([(74, 60), (80, 104)], 'deep', 'b', 1.0),
             L(outline([(30, 20), (44, 14), (48, 26), (34, 30)]), 'light', 'b', False)],
}
