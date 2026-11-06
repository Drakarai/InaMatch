"""Unicorn (IE3, Estados Unidos): sombrero vaquero, pañuelos, gafas, tocado de plumas y pelos de todo tipo, con sus
modelos 3D como referencia (contornos calcados sobre una rejilla de unidades de cabeza). Bobby y Erik ya están dibujados."""
from chars import CHARS, L, OUTC, blob, ell, messy, outline, pal, spk, strand
from chars_alius import LONG_FACE, SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE
from chars_bigwaves import bald, rect_glasses, side_eye, white_eyes
from chars_firedragon import bowl
from heads import quad

WHITE = (250, 250, 250, 255)


def buzz(view, c='mid', front_y=34, peak=None, nape=86):
    """Pelo rapado muy corto pegado al cráneo (peak: pico en la frente)."""
    if view == 'front':
        line = [(16, 58), (16, front_y + 6)] + ([(36, front_y), (peak[0], peak[1]), (64, front_y)] if peak else [(50, front_y - 4)]) + [(84, front_y + 6), (84, 58)]
        return [L(outline([(14, 60), (14, 30), (26, 10), (50, 4), (74, 10), (86, 30), (86, 60)] + line[::-1][1:-1]), c, 'f'),
                L(outline([(60, 8), (82, 20), (86, 46), (74, 34)]), 'shade', 'f', False)]
    if view == 'side':
        return [L(outline([(44, 90), (22, 86), (12, 64), (12, 30), (26, 10), (52, 2), (78, 8), (90, 24), (88, 34), (70, 34), (58, 42), (50, 62), (48, 80)]), c, 'f'),
                L(outline([(12, 40), (34, 40), (42, 80), (22, 86), (12, 64)]), 'shade', 'f', False)]
    return [L(outline([(14, nape - 6), (12, 30), (24, 10), (50, 4), (76, 10), (88, 30), (86, nape - 6), (50, nape)]), c, 'f'),
            L(outline([(56, 6), (82, 18), (88, 46), (86, nape - 8), (62, nape - 4)]), 'shade', 'f', False)]


# Billy Dash (portero): un sombrero vaquero azul marino de ala ancha calado hasta las cejas, un pañuelo rojo anudado al cuello
# y el pelo castaño que asoma en las patillas; ojos entornados de enfado
CHARS['billy-dash'] = {
    'body': 'normal', 'pal': pal('#6a4a2a', '#e8a868', hat='#2a3456', hat_d='#1c2440', scarf='#d8401e', scarf_d='#a82e14'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'eye_y': 76, 'face_front': LONG_FACE, 'hairline': False},
    'front': [L(outline([(14, 64), (20, 64), (22, 90), (16, 92)]), 'mid', 'b', ln=True), L(outline([(86, 64), (80, 64), (78, 90), (84, 92)]), 'mid', 'b', ln=True),
              L(outline([(-24, 62), (-10, 52), (20, 46), (50, 44), (80, 46), (110, 52), (124, 62), (108, 66), (80, 58), (50, 56), (20, 58), (-8, 66)]), 'hat', 'f', ln=True),
              L(outline([(16, 50), (14, 18), (26, -2), (50, -6), (74, -2), (86, 18), (84, 50), (50, 46)]), 'hat', 'f', ln=True),
              L(outline([(38, 4), (50, 10), (62, 4)]), 'hat_d', 'f', False, False, 2.2),
              L(outline([(60, -2), (78, 6), (84, 40), (70, 44)]), 'hat_d', 'f', False),
              L(outline([(4, 108), (30, 100), (50, 108), (70, 100), (96, 108), (100, 124), (60, 130), (50, 124, 1), (40, 130), (0, 124)]), 'scarf', 'f', ln=True),
              L(outline([(56, 108), (94, 108), (96, 122), (60, 126)]), 'scarf_d', 'f', False)],
    'side': [L(outline([(-20, 62), (0, 50), (40, 44), (90, 40), (120, 46), (106, 54), (70, 54), (30, 58), (-4, 66)]), 'hat', 'f', ln=True),
             L(outline([(10, 48), (12, 14), (30, -6), (60, -8), (80, 4), (86, 40), (50, 44)]), 'hat', 'f', ln=True),
             L(outline([(20, 106), (60, 100), (90, 104), (94, 118), (60, 124), (30, 120)]), 'scarf', 'f', ln=True),
             L(outline([(24, 104), (4, 96), (-2, 110, 1), (14, 112)]), 'scarf', 'f', ln=True)],
    'back': [L(blob(SKULL_B), 'skin'), L(outline([(16, 82), (14, 50), (86, 50), (84, 82), (50, 88)]), 'mid', 'b'),
             L(outline([(-24, 62), (-10, 52), (20, 46), (50, 44), (80, 46), (110, 52), (124, 62), (108, 66), (80, 60), (50, 58), (20, 60), (-8, 66)]), 'hat', 'f', ln=True),
             L(outline([(16, 50), (14, 18), (26, -2), (50, -6), (74, -2), (86, 18), (84, 50), (50, 48)]), 'hat', 'f', ln=True),
             L(outline([(4, 102), (50, 98), (96, 102), (100, 118), (50, 124), (0, 118)]), 'scarf', 'f', ln=True),
             L(outline([(40, 106), (30, 120), (40, 128, 1), (50, 114), (60, 128, 1), (70, 120), (60, 106)]), 'scarf_d', 'f', ln=True)],
}
# Ted Bryant: piel morena; pelo castaño corto con un pico en la frente y un mechón en punta a un lado; un pañuelo amarillo
# mostaza anudado detrás que le tapa la boca y la nariz; ojos negros grandes de enfado
CHARS['ted-bryant'] = {
    'body': 'normal', 'pal': pal('#4a2a14', '#9a643a', cloth='#e8b830', cloth_d='#b88a1e'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'none', 'hairline': False, 'big_ears': 3, 'ear_out': 6},
    'front': bald('front') + buzz('front', front_y=42, peak=(54, 54))
             + [L(outline([(64, 36), (70, 54, 1), (74, 34)]), 'mid', 'f', ln=True),
                L(outline([(14, 84), (50, 80), (86, 84), (82, 100), (64, 110), (50, 116, 1), (36, 110), (18, 100)]), 'cloth', 'f', ln=True),
                L(outline([(54, 84), (86, 86), (82, 100), (62, 110)]), 'cloth_d', 'f', False)],
    'side': bald('side') + buzz('side')
            + [L(outline([(36, 82), (96, 80), (98, 92), (80, 108), (50, 102)]), 'cloth', 'f', ln=True),
               L(outline([(34, 84), (16, 88), (10, 98, 1), (22, 96), (34, 94)]), 'cloth_d', 'f', ln=True)],
    'back': bald('back') + buzz('back')
            + [L(quad((6, 84), (50, 92), (94, 84)), 'cloth', 'f', False, False, 4),
               L(outline([(36, 86), (50, 82), (64, 86), (60, 96), (50, 92), (40, 96)]), 'cloth_d', 'f', ln=True)],
}
# Tony Strider: grandullón de cara cuadrada con orejas grandes; pelo rubio rapado muy corto con un tatuaje de estrella
# amarilla en la sien; ojos blancos redondos de pasmo y la boca torcida
CHARS['tony-strider'] = {
    'body': 'corpulento', 'pal': pal('#d8a840', '#f8c090', star='#f0c020', shade='#b08830'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 4, 'ear_out': 9},
    'front': bald('front') + buzz('front', front_y=34)
             + white_eyes(76, 16, 6.4, 6, 2.6)
             + [L(outline([(66, 44), (68, 38, 1), (70, 44), (76, 44, 1), (71, 48), (73, 54, 1), (68, 50), (63, 54, 1), (65, 48), (60, 44, 1)]), 'star', 'f', ln=True),
                L([(30, 54), (40, 58)], 'skin_d', 'f', False, False, 1.2), L([(60, 58), (70, 54)], 'skin_d', 'f', False, False, 1.2)],
    'side': bald('side') + buzz('side') + side_eye(76),
    'back': bald('back') + buzz('back'),
}
# Drake Dynamo: piel muy morena; pelo gris oscuro rapado con entradas marcadas; tres cicatrices en la frente, ojos blancos de
# furia, nariz ancha y los dientes apretados
CHARS['drake-dynamo'] = {
    'body': 'corpulento', 'pal': pal('#4a4440', '#6a3a24', skin_d='#4e2a18', scar='#e8a8a0', nose='#5a301c'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 8},
    'front': bald('front') + [L(outline([(14, 50), (14, 26), (26, 8), (50, 2), (74, 8), (86, 26), (86, 50), (76, 36), (62, 32), (50, 36), (38, 32), (24, 36)]), 'mid', 'f')]
             + [L([(26 + k * 4, 48), (34 + k * 4, 58)], 'scar', 'f', False, False, 1.8) for k in range(3)]
             + [L(outline([(22, 70), (40, 70), (38, 78), (26, 76)]), WHITE, 'f', ln=True), L(outline([(78, 70), (60, 70), (62, 78), (74, 76)]), WHITE, 'f', ln=True),
                L([(20, 64), (42, 70)], OUTC, 'f', False, False, 2.6), L([(80, 64), (58, 70)], OUTC, 'f', False, False, 2.6),
                L(outline([(38, 84), (62, 84), (64, 92), (36, 92)]), 'nose', 'f', ln=True),
                L(outline([(30, 100), (50, 96), (70, 100), (66, 108), (34, 108)]), WHITE, 'f', ln=True), L([(32, 104), (68, 104)], OUTC, 'f', False, False, 1.0)],
    'side': bald('side') + buzz('side') + [L([(70, 44), (78, 54)], 'scar', 'f', False, False, 1.8)] + side_eye(72),
    'back': bald('back') + buzz('back'),
}
# Steve Woodmark: piel morena; pelo castaño oscuro peinado hacia atrás en surcos que se recoge en dos rizos en la nuca; unas
# gafas de sol grises subidas en la frente; ojos negros de enfado
CHARS['steve-woodmark'] = {
    'body': 'normal', 'pal': pal('#4a2a18', '#b07a48', shade='#341e10', frame='#5a6068', lens='#7a8890'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': (56, 46)},
    'front': [L(outline([(12, 76), (8, 36), (20, 10), (50, 2), (80, 10), (92, 36), (88, 76), (84, 92, 1), (80, 66), (20, 66), (16, 92, 1)])),
              L(outline([(60, 6), (84, 18), (92, 44), (86, 84), (80, 50)]), 'shade', 'b', False)]
             + [strand([(x, 6 + abs(x - 50) * 0.2), (x + (x - 50) * 0.2, 44)], 'deep', 'b', 1.0) for x in (28, 40, 52, 64, 76)]
             + [L(outline([(14, 38), (46, 36), (46, 48), (18, 48)]), 'lens', 'f', ln=True), L(outline([(86, 38), (54, 36), (54, 48), (82, 48)]), 'lens', 'f', ln=True),
                L(quad((8, 42), (50, 34), (92, 42)), 'frame', 'f', False, False, 2.0)],
    'side': [L(outline([(44, 92), (40, 104, 1), (24, 92), (12, 66), (8, 36), (22, 10), (52, 2), (78, 8), (90, 24), (86, 36), (70, 40), (58, 46), (52, 62), (50, 80)])),
             L(outline([(10, 40), (34, 40), (42, 84), (22, 88), (12, 66)]), 'shade', 'b', False),
             L(outline([(70, 36), (92, 34), (92, 46), (72, 46)]), 'lens', 'f', ln=True), L([(40, 50), (70, 40)], 'frame', 'f', False, False, 2.0)],
    'back': [L(outline([(12, 84), (8, 36), (20, 10), (50, 2), (80, 10), (92, 36), (88, 84), (80, 98, 1), (64, 88), (50, 92), (36, 88), (20, 98, 1)])),
             L(outline([(56, 6), (84, 18), (92, 48), (88, 84), (64, 88)]), 'shade', 'b', False)]
            + [strand([(x, 4), (x + (x - 50) * 0.1, 84)], 'deep', 'b', 1.0) for x in (30, 44, 56, 70)],
}
# Shane Pierce: pelo rubio ceniza a capas con un mechón largo que le cruza la frente y sale en punta por un lado; gafas
# rectangulares finas, ojos turquesa y la boca seria
CHARS['shane-pierce'] = {
    'body': 'normal', 'pal': pal('#c8b870', '#fcd8b8', iris='#2a9aa0', shade='#a09050'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 80), (8, 40), (20, 12), (50, 2), (80, 12), (92, 40), (88, 80), (82, 74), (82, 62), (18, 62), (18, 74)])),
              L(outline([(60, 6), (84, 18), (92, 46), (86, 76), (80, 46)]), 'shade', 'b', False),
              L(outline([(-12, 38, 1), (14, 36), (34, 24), (56, 18), (76, 22), (88, 38), (90, 60), (80, 52), (62, 44), (46, 48), (36, 60), (30, 72, 1), (24, 54), (14, 46)]), 'mid', 'f', ln=True),
              L(outline([(14, 64), (20, 64), (22, 88), (16, 94, 1)]), 'mid', 'f'), L(outline([(86, 64), (80, 64), (78, 88), (84, 94, 1)]), 'mid', 'f')]
             + rect_glasses('front', 76),
    'side': [L(outline([(44, 92), (40, 102, 1), (26, 92), (12, 70), (8, 36), (22, 10), (52, 2), (78, 8), (92, 26), (94, 46), (82, 46), (66, 48), (56, 58), (52, 70), (50, 80)])),
             L(outline([(10, 40), (34, 40), (42, 84), (24, 90), (12, 70)]), 'shade', 'b', False)] + rect_glasses('side', 76),
    'back': [L(outline([(12, 84), (8, 40), (20, 12), (50, 2), (80, 12), (92, 40), (88, 84), (102, 80, 1), (86, 92), (50, 96), (14, 92)])),
             L(outline([(56, 6), (84, 18), (92, 48), (88, 84), (64, 90)]), 'shade', 'b', False)],
}
# Mark Krueger: pelo castaño claro abultado y despeinado en mechones en punta que se abren a los lados y le caen por la
# frente; ojos turquesa y media sonrisa confiada
CHARS['mark-krueger'] = {
    'body': 'normal', 'pal': pal('#b8862e', '#fcd8b8', iris='#2a9a9a', shade='#8a6420', light='#d8a84a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': messy('front', 14, 9, seed=701, rx=56, ry=44, cy=40, lo=78)
             + [L(outline([(10, 72, 1), (14, 44), (28, 28), (50, 22), (72, 28), (86, 44), (90, 72, 1), (80, 56), (72, 64, 1), (64, 50), (56, 60, 1), (50, 48), (44, 66, 1),
                           (38, 52), (28, 62, 1), (20, 54)]), 'mid', 'f'),
                L(outline([(30, 30), (52, 24), (44, 34)]), 'light', 'f', False)],
    'side': messy('side', 16, 8, seed=701, rx=52, ry=44, cy=40, nape=94, sweep=-0.4) + [spk((58, 30), (90, 40), (94, 66), 4, z='f', light_left=False)],
    'back': messy('back', 14, 9, seed=701, rx=56, ry=44, cy=40, nape=96),
}
# Dylan Keats: pelo rubio verdoso peinado hacia atrás que se recoge en una coleta corta y cae en mechones hasta el cuello;
# unas gafas de natación azules sobre los ojos y una sonrisa enorme de dientes
CHARS['dylan-keats'] = {
    'body': 'normal', 'pal': pal('#b8b878', '#fcd8b8', shade='#8e8e58', goggle='#2a7a9a', strap='#1e1e1e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 96, 'hairline': (56, 46)},
    'front': [L(outline([(8, 92, 1), (12, 70), (6, 40), (18, 12), (40, -4), (50, 6), (60, -4), (82, 12), (94, 40), (88, 70), (92, 92, 1), (82, 80), (82, 62), (18, 62), (18, 80)])),
              L(outline([(60, 0), (84, 16), (94, 44), (88, 84), (80, 46)]), 'shade', 'b', False),
              strand([(30, 6), (36, 40)], 'shade', 'b', 1.0), strand([(70, 6), (64, 40)], 'shade', 'b', 1.0),
              L(quad((10, 74), (50, 70), (90, 74)), 'strap', 'f', False, False, 1.8),
              L(outline([(18, 68), (46, 70), (50, 76), (54, 70), (82, 68), (82, 82), (60, 86), (50, 80), (40, 86), (18, 82)]), 'goggle', 'f', ln=True),
              L(outline([(22, 70), (34, 70), (24, 76)]), (140, 200, 220, 255), 'f', False)],
    'side': [L(outline([(44, 92), (22, 88), (12, 70), (8, 36), (22, 10), (52, 0), (78, 8), (90, 24), (88, 40), (72, 42), (58, 48), (52, 64), (50, 80)])),
             L(outline([(10, 40), (34, 40), (42, 84), (22, 88), (12, 68)]), 'shade', 'b', False),
             L(outline([(18, 44), (0, 50), (-6, 60, 1), (6, 56), (20, 52)]), 'mid', 'b', ln=True),
             L(quad((40, 76), (60, 72), (80, 74)), 'strap', 'f', False, False, 1.8), L(outline([(78, 68), (96, 68), (96, 82), (80, 82)]), 'goggle', 'f', ln=True)],
    'back': [L(outline([(8, 92, 1), (12, 70), (6, 40), (18, 12), (50, 2), (82, 12), (94, 40), (88, 70), (92, 92, 1), (70, 86), (50, 90), (30, 86)])),
             L(outline([(56, 6), (84, 18), (94, 48), (88, 84), (64, 88)]), 'shade', 'b', False),
             L(outline([(44, 40), (56, 40), (58, 66), (50, 76, 1), (42, 66)]), 'mid', 'f', ln=True),
             L(quad((6, 72), (50, 76), (94, 72)), 'strap', 'f', False, False, 1.8)],
}
# Gabriel Jax: piel morena; pelo castaño oscuro ondulado hasta la nuca, peinado hacia atrás con un mechón rizado en antena;
# ojos marrones de enfado y la boca abierta de dientes apretados
CHARS['gabriel-jax'] = {
    'body': 'normal', 'pal': pal('#5a2e2a', '#a8703e', iris='#6a3a20', shade='#42201c'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'hairline': [(14, 66), (16, 46), (30, 40), (44, 46), (56, 36), (70, 40), (84, 46), (86, 66)]},
    'front': [L(outline([(6, 90, 1), (10, 70), (4, 40), (18, 10), (50, 0), (82, 10), (96, 40), (90, 70), (94, 90, 1), (82, 80), (82, 62), (18, 62), (18, 80)])),
              L(outline([(60, 4), (84, 16), (94, 44), (90, 84), (80, 46)]), 'shade', 'b', False),
              strand([(50, 4), (56, 36)], 'deep', 'b', 1.0), strand([(30, 10), (26, 40)], 'deep', 'b', 1.0), strand([(70, 10), (74, 40)], 'deep', 'b', 1.0),
              L(outline([(54, 36), (48, 50), (56, 58), (52, 52)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(44, 92), (34, 102, 1), (24, 90), (10, 96, 1), (10, 70), (6, 36), (20, 10), (52, 0), (78, 6), (92, 24), (88, 40), (74, 42), (60, 48), (52, 64), (50, 80)])),
             L(outline([(8, 40), (34, 40), (42, 84), (24, 90), (10, 70)]), 'shade', 'b', False),
             L(outline([(76, 6), (92, 0), (100, 10), (94, 18), (98, 22, 1), (88, 14)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(6, 90, 1), (10, 70), (4, 40), (18, 10), (50, 0), (82, 10), (96, 40), (90, 70), (94, 90, 1), (76, 86), (64, 96, 1), (50, 86), (36, 96, 1), (24, 86)])),
             L(outline([(56, 4), (86, 18), (94, 48), (90, 84), (64, 88)]), 'shade', 'b', False)],
}
# Alex Hawke (portero suplente): un tocado de plumas blancas con las puntas rojas abiertas en abanico alrededor de la
# cabeza, sujeto con una cinta de rombos rojos y amarillos; por debajo, el pelo castaño; ojos negros y la boca seria
FEATHER_ANG = [-80, -55, -30, -5, 20, 45, 70, 95, 120, 145, 170, 195, 220, 245]
def _feathers(view):
    import math
    out = []
    for a in FEATHER_ANG:
        r = math.radians(a - 90)
        cx, cy = (50, 46) if view != 'side' else (44, 46)
        tip = (cx + 70 * math.cos(r), cy + 64 * math.sin(r))
        if view == 'front' and tip[1] > 70:
            continue
        if view == 'side' and (tip[0] > 56 or tip[1] > 100):
            continue
        base = (cx + 30 * math.cos(r), cy + 26 * math.sin(r))
        d = (-math.sin(r) * 7, math.cos(r) * 7)
        out.append(L(outline([(base[0] - d[0], base[1] - d[1]), (tip[0] - d[0] * 0.5, tip[1] - d[1] * 0.5), (tip[0], tip[1], 1), (tip[0] + d[0] * 0.5, tip[1] + d[1] * 0.5),
                              (base[0] + d[0], base[1] + d[1])]), 'feather', 'b', ln=True))
        out.append(L(outline([(tip[0] - d[0] * 0.5 - math.cos(r) * 8, tip[1] - d[1] * 0.5 - math.sin(r) * 8), (tip[0], tip[1], 1),
                              (tip[0] + d[0] * 0.5 - math.cos(r) * 8, tip[1] + d[1] * 0.5 - math.sin(r) * 8)]), 'feather_t', 'b', False))
    return out


def _diamond_band(view, y0=40, y1=56):
    x0, x1 = (8, 92) if view != 'side' else (10, 94)
    out = [L(outline([(x0, y1), (x0, y0), (50, y0 - 4), (x1, y0), (x1, y1), (50, y1 - 4)]), 'band', 'f', ln=True)]
    n = 5
    for k in range(n):
        a = x0 + (x1 - x0) * k / n
        b = x0 + (x1 - x0) * (k + 1) / n
        out.append(L([(a, y1 - 2), ((a + b) / 2, y0), (b, y1 - 2)], 'band_d', 'f', False))
    return out


CHARS['alex-hawke'] = {
    'body': 'normal', 'pal': pal('#5a3a20', '#f8c890', feather='#f4ecd8', feather_t='#d84a1e', band='#f0b020', band_d='#d03a1e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': _feathers('front') + [L(outline([(14, 70), (12, 40), (88, 40), (86, 70), (80, 64), (20, 64)]))] + _diamond_band('front'),
    'side': _feathers('side') + [L(outline([(44, 92), (22, 88), (12, 66), (12, 40), (88, 40), (88, 50), (70, 52), (56, 58), (52, 70), (50, 80)]))] + _diamond_band('side'),
    'back': [L(outline([(14, 84), (12, 40), (88, 40), (86, 84), (50, 90)]))] + _feathers('back') + [L(ell(50, 50, 20, 14), 'mid', 'f', ln=True)],
}
# Corey Washington: cabeza pequeña y ovalada con el pelo castaño rapado muy corto y una entrada en pico; pinturas de
# guerra rojas en la mejilla, ojos negros grandes y redondos, la nariz redonda y la boca abierta en una O
CHARS['corey-washington'] = {
    'body': 'normal', 'pal': pal('#5a4a3a', '#d8a060', paint='#c82a1a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': LONG_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 5},
    'front': bald('front') + buzz('front', front_y=40, peak=(50, 50))
             + white_eyes(74, 15, 6.4, 7, 3.6)
             + [L(ell(50, 86, 5, 4.4) + [ell(50, 86, 5, 4.4)[0]], OUTC, 'f', False, False, 1.2),
                L([(22, 88), (32, 82)], 'paint', 'f', False, False, 1.8), L([(22, 93), (32, 87)], 'paint', 'f', False, False, 1.8),
                L(ell(50, 100, 5, 4), WHITE, 'f', ln=True)],
    'side': bald('side') + buzz('side') + side_eye(74, None)
            + [L([(60, 86), (74, 84)], 'paint', 'f', False, False, 1.8), L([(60, 91), (74, 89)], 'paint', 'f', False, False, 1.8)],
    'back': bald('back') + buzz('back'),
}
# Bob Bobbins: gordito de cara redonda y coloretes naranjas; pelo verde oliva peinado en un tupé que le cae hacia un lado;
# ojos cerrados de risa, la nariz naranja de pato y una sonrisa enorme de dientes
CHARS['bob-bobbins'] = {
    'body': 'corpulento', 'pal': pal('#7a6a2a', '#fcc8a0', shade='#5a4c1e', nose='#f08a2a', blush='#f8a050'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 9},
    'front': [L(blob(SKULL_F), 'skin'),
              L(outline([(10, 62), (10, 30), (24, 8), (50, 0), (78, 4), (96, -6, 1), (90, 16), (92, 40), (90, 62), (80, 46), (60, 40), (40, 40), (20, 46)]), 'mid', 'f'),
              L(outline([(56, 4), (82, 6), (92, 30), (84, 46), (70, 30)]), 'shade', 'f', False),
              L([(24, 70), (38, 74), (26, 78)], OUTC, 'f', False, False, 2.0), L([(76, 70), (62, 74), (74, 78)], OUTC, 'f', False, False, 2.0),
              L(ell(22, 84, 5, 3), 'blush', 'f', False), L(ell(78, 84, 5, 3), 'blush', 'f', False),
              L(outline([(42, 82), (58, 82), (54, 90), (46, 90)]), 'nose', 'f', ln=True),
              L(outline([(20, 96), (50, 100), (80, 96), (70, 108), (50, 112), (30, 108)]), WHITE, 'f', ln=True), L([(24, 100), (76, 100)], OUTC, 'f', False, False, 1.0)],
    'side': [L(blob(SIDE_SKULL), 'skin'),
             L(outline([(12, 64), (12, 30), (26, 8), (54, 0), (80, 2), (96, 10), (92, 22), (80, 30), (60, 36), (40, 40), (24, 60)]), 'mid', 'f'),
             L(ell(76, 84, 5, 3), 'blush', 'f', False), L(outline([(88, 80), (100, 84), (90, 90)]), 'nose', 'f', ln=True),
             L(outline([(80, 98), (94, 98), (92, 106), (80, 106)]), WHITE, 'f', ln=True)],
    'back': [L(outline([(10, 84), (8, 30), (22, 8), (50, 0), (78, 6), (92, 30), (90, 84), (50, 90)])),
             L(outline([(56, 6), (84, 18), (92, 48), (88, 82), (64, 88)]), 'shade', 'b', False),
             L(outline([(12, 6), (4, -6, 1), (24, 2)]), 'mid', 'f', ln=True)],
}
# Petie Pooma: piel muy morena y cara redonda con orejas grandes; pelo castaño oscuro corto con un pico marcado en las
# sienes; ojos negros grandes y una sonrisa abierta
CHARS['petie-pooma'] = {
    'body': 'bajito', 'pal': pal('#3a2418', '#8a5a34', shade='#26160e'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'none', 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 4, 'ear_out': 9},
    'front': bald('front') + [L(outline([(14, 60), (14, 26), (26, 8), (50, 2), (74, 8), (86, 26), (86, 60), (78, 46), (70, 54, 1), (64, 42), (50, 40), (36, 42), (30, 54, 1),
                                         (22, 46)]), 'mid', 'f')]
             + white_eyes(76, 15, 6, 6.6, 3.4)
             + [L(outline([(36, 94), (64, 94), (60, 104), (50, 106), (40, 104)]), (120, 40, 40, 255), 'f', ln=True), L(outline([(38, 94), (62, 94), (60, 98), (40, 98)]), WHITE, 'f', False)],
    'side': bald('side') + buzz('side') + side_eye(76),
    'back': bald('back') + buzz('back'),
}
# Norbert Poindexter: pelo rubio dorado peinado hacia atrás en mechones de punta que se abren por detrás y a los lados,
# con un mechón de pico en la frente; cejas finas, ojos verdes y una sonrisa
CHARS['norbert-poindexter'] = {
    'body': 'normal', 'pal': pal('#d8b050', '#fce4c8', iris='#2a8a3a', shade='#b08a30'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 95, 'hairline': [(14, 64), (16, 44), (30, 36), (50, 34), (70, 36), (84, 44), (86, 64)]},
    'front': [L(outline([(12, 66), (8, 36), (20, 10), (50, 0), (80, 8), (96, 20), (106, 26, 1), (94, 34), (106, 46, 1), (92, 50), (88, 66), (82, 60), (18, 60)])),
              L(outline([(60, 4), (84, 14), (100, 26), (92, 46), (80, 34)]), 'shade', 'b', False),
              strand([(36, 6), (30, 36)], 'shade', 'b', 1.0), strand([(56, 2), (60, 34)], 'shade', 'b', 1.0)],
    'side': [L(outline([(44, 92), (22, 88), (12, 66), (-8, 64, 1), (6, 52), (-10, 40, 1), (8, 34), (-4, 20, 1), (16, 16), (12, 2, 1), (30, 8), (52, 0), (78, 4), (94, 16),
                        (92, 34), (76, 40), (60, 46), (52, 62), (50, 80)])),
             L(outline([(10, 40), (34, 40), (42, 84), (22, 88), (12, 66)]), 'shade', 'b', False)],
    'back': [L(outline([(12, 80), (8, 40), (-6, 30, 1), (10, 26), (4, 8, 1), (20, 10), (30, -4, 1), (42, 6), (54, -6, 1), (62, 6), (78, -2, 1), (80, 12), (98, 10, 1),
                        (90, 26), (104, 36, 1), (92, 44), (88, 80), (50, 88)])),
             L(outline([(56, 4), (84, 16), (94, 44), (88, 78), (64, 86)]), 'shade', 'b', False)],
}
