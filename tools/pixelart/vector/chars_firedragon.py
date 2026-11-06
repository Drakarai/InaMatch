"""Fire Dragon / Dragones de Fuego (IE3, Corea): con sus modelos 3D como referencia (contornos calcados sobre una rejilla
de unidades de cabeza). Claude, Bryce y Byron ya están dibujados."""
from chars import CHARS, L, OUTC, blob, ell, messy, outline, pal, spk, strand
from chars_alius import LONG_FACE, SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE
from chars_bigwaves import bald, rect_glasses, side_eye, white_eyes
from heads import quad

WHITE = (250, 250, 250, 255)


def bowl(view, low=58, fringe_y=56, nape=86, ears=True):
    """Pelo cortado en tazón: casco liso con el flequillo recto."""
    if view == 'front':
        return [L(outline([(12, fringe_y + 10), (8, 34), (20, 8), (50, 0), (80, 8), (92, 34), (88, fringe_y + 10), (80, fringe_y + 4), (50, fringe_y), (20, fringe_y + 4)])),
                L(outline([(60, 4), (84, 16), (92, 40), (88, fringe_y + 8), (78, 34)]), 'shade', 'b', False)]
    if view == 'side':
        return [L(outline([(44, 92), (24, 88), (14, 70), (8, 36), (22, 10), (52, 0), (78, 8), (92, 28), (94, 46), (80, 46), (64, 48), (54, 62), (50, 80)])),
                L(outline([(10, 40), (34, 44), (42, 82), (24, 88), (12, 68)]), 'shade', 'b', False)]
    return [L(outline([(12, nape - 4), (8, 34), (20, 8), (50, 0), (80, 8), (92, 34), (88, nape - 4), (50, nape)])),
            L(outline([(56, 4), (84, 16), (92, 44), (88, nape - 6), (64, nape - 2)]), 'shade', 'b', False)]


# Jeongsu Cho (portero): calvo de cabeza pálida, con dos manchas rojas de pelo en lo alto que se abren hacia la frente;
# ojos blancos de enfado con párpados rojos y la boca en una raya
CHARS['jeongsu-cho'] = {
    'body': 'corpulento', 'pal': pal('#a81a0e', '#fcecd4', skin_d='#e8c8b0'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 98, 'hairline': False, 'big_ears': 2, 'ear_out': 4},
    'front': bald('front') + [L(outline([(26, 34), (22, 10), (36, 2), (42, 8), (38, 34)]), 'mid', 'f', ln=True),
                              L(outline([(74, 34), (78, 10), (64, 2), (58, 8), (62, 34)]), 'mid', 'f', ln=True),
                              L(outline([(22, 70), (44, 70), (42, 80), (24, 78)]), WHITE, 'f', ln=True), L(outline([(78, 70), (56, 70), (58, 80), (76, 78)]), WHITE, 'f', ln=True),
                              L([(22, 70), (44, 70)], 'mid', 'f', False, False, 2.4), L([(78, 70), (56, 70)], 'mid', 'f', False, False, 2.4),
                              L(ell(36, 75, 1.8, 1.8), OUTC, 'f', False), L(ell(64, 75, 1.8, 1.8), OUTC, 'f', False)],
    'side': bald('side') + [L(outline([(24, 20), (44, 8), (72, 8), (86, 26), (70, 20), (44, 18)]), 'mid', 'f', ln=True), L([(78, 70), (90, 72)], 'mid', 'f', False, False, 2.4)]
            + side_eye(75),
    'back': bald('back') + [L(outline([(22, 26), (30, 10), (50, 4), (70, 10), (78, 26), (50, 22)]), 'mid', 'f', ln=True)],
}
# Umi Hwang: pelo verde intenso cortado en tazón con un mechón que le cae en diagonal sobre el ojo derecho, cejas verdes y
# media cara en sombra; ojos morados rasgados y la boca seria
CHARS['umi-hwang'] = {
    'body': 'normal', 'pal': pal('#2e8a24', '#f8c890', iris='#4a3a8a', shade='#226a1a', light='#5aba4a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': bowl('front', fringe_y=54)
             + [L(outline([(12, 64), (14, 42), (30, 28), (50, 24), (70, 28), (86, 42), (88, 62), (78, 54), (60, 52), (46, 56), (34, 70), (26, 82, 1), (22, 66)]), 'mid', 'f', ln=True),
                L(outline([(30, 30), (50, 26), (44, 34)]), 'light', 'f', False),
                L([(22, 66), (40, 62)], 'mid', 'f', False, False, 2.4), L([(78, 66), (60, 62)], 'mid', 'f', False, False, 2.4)],
    'side': bowl('side') + [spk((60, 30), (90, 40), (92, 64), 4, z='f', light_left=False)],
    'back': bowl('back', nape=90),
}
# Dooyoon Hong: cara grande y redonda con orejas grandes; el pelo naranja corto en un flequillo recto sobre la frente y las
# sienes y la nuca de castaño oscuro rapado; ojos cerrados de llanto, coloretes y la boca torcida
CHARS['dooyoon-hong'] = {
    'body': 'bajito', 'pal': pal('#e08a2a', '#fce4cc', shade='#b86a18', dark='#3a2018', blush='#f0a090'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 8},
    'front': [L(outline([(12, 56), (12, 30), (26, 12), (50, 6), (74, 12), (88, 30), (88, 56), (80, 40), (20, 40)]), 'dark'),
              L(outline([(20, 40), (18, 22), (32, 8), (50, 4), (68, 8), (82, 22), (80, 40), (64, 36), (50, 38), (36, 36)]), 'mid', 'f', ln=True),
              L(outline([(58, 8), (78, 18), (80, 36), (66, 32)]), 'shade', 'f', False),
              strand([(36, 18), (38, 34)], 'shade', 'f', 1.0), strand([(50, 12), (50, 36)], 'shade', 'f', 1.0),
              L([(26, 70), (40, 74), (28, 78)], OUTC, 'f', False, False, 2.0), L([(74, 70), (60, 74), (72, 78)], OUTC, 'f', False, False, 2.0),
              L(ell(24, 88, 5, 3), 'blush', 'f', False), L(ell(76, 88, 5, 3), 'blush', 'f', False),
              L(outline([(40, 100), (50, 96), (60, 100), (56, 104), (44, 104)]), (220, 140, 140, 255), 'f', ln=True)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (10, 30), (24, 10), (52, 2), (78, 10), (90, 28), (86, 40), (68, 42), (56, 52), (52, 66), (50, 80)]), 'dark'),
             L(outline([(30, 18), (52, 4), (80, 8), (96, 22), (88, 30), (60, 24), (40, 28)]), 'mid', 'f', ln=True),
             L(ell(76, 86, 5, 3), 'blush', 'f', False), L([(78, 72), (88, 74)], OUTC, 'f', False, False, 2.0)],
    'back': [L(outline([(12, 84), (10, 30), (24, 10), (50, 4), (76, 10), (90, 30), (88, 84), (50, 90)]), 'dark'),
             L(outline([(26, 14), (50, 6), (74, 14), (62, 44), (60, 76), (40, 76), (38, 44)]), 'mid', 'f', ln=True),
             L([(40, 64), (60, 64)], 'shade', 'f', False, False, 1.4), L([(40, 70), (60, 70)], 'shade', 'f', False, False, 1.4)],
}
# Minho Cho: piel morena; la cabeza rapada con una mata de pinchos verdes en lo alto; orejas en punta, ojos blancos de
# enfado, mejillas marcadas, nariz ancha y labios gruesos morados
CHARS['minho-cho'] = {
    'body': 'normal', 'pal': pal('#7a9a2a', '#a8784e', skin_d='#8a5e38', shade='#5a7a1a', light='#a8c84a', lip='#7a4a6a', dark='#4a3020'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': LONG_FACE, 'hairline': False, 'big_ears': 2, 'ear_out': 4},
    'front': [L(outline([(16, 60), (14, 30), (26, 14), (50, 8), (74, 14), (86, 30), (84, 60), (70, 44), (30, 44)]), 'dark'),
              L(outline([(22, 20), (14, -4, 1), (28, 4), (32, -16, 1), (42, -2), (50, -20, 1), (58, -2), (68, -16, 1), (72, 4), (86, -4, 1), (78, 20)]), 'mid', 'f', ln=True),
              L(outline([(44, 0), (50, -16, 1), (56, 0), (52, 16)]), 'light', 'f', False),
              L(outline([(22, 70), (40, 70), (38, 78), (26, 78)]), WHITE, 'f', ln=True), L(outline([(78, 70), (60, 70), (62, 78), (74, 78)]), WHITE, 'f', ln=True),
              L([(20, 66), (42, 70)], OUTC, 'f', False, False, 2.4), L([(80, 66), (58, 70)], OUTC, 'f', False, False, 2.4),
              L(ell(33, 74, 1.6, 1.8), OUTC, 'f', False), L(ell(67, 74, 1.6, 1.8), OUTC, 'f', False),
              L(outline([(44, 80), (56, 80), (60, 94), (40, 94)]), 'skin_d', 'f', ln=True),
              L(outline([(32, 104), (50, 100), (68, 104), (62, 112), (38, 112)]), 'lip', 'f', ln=True)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (12, 30), (26, 10), (52, 4), (78, 10), (90, 28), (84, 40), (66, 42), (56, 52), (52, 66), (50, 80)]), 'dark'),
             L(outline([(20, 20), (12, 2, 1), (26, 8), (30, -10, 1), (42, 4), (52, -14, 1), (58, 4), (72, -10, 1), (74, 8), (88, 4, 1), (80, 22)]), 'mid', 'f', ln=True),
             L(outline([(86, 104), (96, 102), (94, 112), (86, 112)]), 'lip', 'f', ln=True)] + side_eye(74),
    'back': [L(outline([(14, 86), (12, 30), (26, 12), (50, 6), (74, 12), (88, 30), (86, 86), (50, 92)]), 'dark'),
             L(outline([(22, 22), (14, -2, 1), (28, 4), (32, -14, 1), (42, -2), (50, -18, 1), (58, -2), (68, -14, 1), (72, 4), (86, -2, 1), (78, 22)]), 'mid', 'f', ln=True)],
}
# Songhwan Ko: pelo azul marino en forma de casco con dos picos que suben arriba y patillas largas en punta; una nariz larga
# naranja, ojos blancos redondos de enfado y la barbilla cuadrada
CHARS['songhwan-ko'] = {
    'body': 'normal', 'pal': pal('#1e4a7a', '#e8b06a', shade='#163a62', nose='#e8963a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 104, 'face_front': LONG_FACE, 'hairline': False},
    'front': [L(outline([(12, 76), (8, 44), (-2, 36, 1), (12, 30), (20, 8), (30, -18, 1), (40, 2), (50, -2), (60, 2), (70, -18, 1), (80, 8), (88, 30), (102, 36, 1),
                         (92, 44), (88, 76), (84, 84, 1), (80, 62), (20, 62), (16, 84, 1)])),
              L(outline([(60, 2), (70, -14, 1), (78, 10), (88, 34), (86, 72), (78, 50)]), 'shade', 'b', False),
              L(outline([(16, 56), (30, 46), (44, 52), (50, 64), (56, 52), (70, 46), (84, 56), (70, 56), (50, 70, 1), (30, 56)]), 'mid', 'f')]
             + white_eyes(76, 14, 6.4, 6.4, 2.2)
             + [L([(24, 68), (42, 72)], OUTC, 'f', False, False, 2.2), L([(76, 68), (58, 72)], OUTC, 'f', False, False, 2.2),
                L(outline([(44, 78), (56, 78), (58, 100), (50, 104, 1), (42, 100)]), 'nose', 'f', ln=True)],
    'side': [L(outline([(44, 92), (40, 106, 1), (26, 88), (12, 64), (12, 30), (24, 6), (38, -18, 1), (50, 2), (66, 0), (84, 12), (94, 30), (90, 44), (74, 46), (60, 50),
                        (54, 64), (50, 80)])),
             L(outline([(12, 40), (34, 44), (42, 84), (24, 90), (12, 66)]), 'shade', 'b', False),
             L(outline([(84, 76), (110, 100, 1), (90, 96)]), 'nose', 'f', ln=True)] + side_eye(74),
    'back': [L(outline([(12, 84), (8, 44), (-2, 36, 1), (12, 30), (20, 8), (30, -18, 1), (40, 2), (50, -2), (60, 2), (70, -18, 1), (80, 8), (88, 30), (102, 36, 1),
                        (92, 44), (88, 84), (50, 92)])),
             L(outline([(56, 2), (70, -14, 1), (80, 10), (90, 40), (86, 82), (62, 90)]), 'shade', 'b', False)],
}
# Paekyeong Park: la cabeza rapada en marrón grisáceo, con un moño plano como un tapón en lo alto; una bufanda rosa enorme
# enrollada que le tapa hasta la nariz; cejas negras gruesas de enfado y los ojos cerrados
CHARS['paekyeong-park'] = {
    'body': 'normal', 'pal': pal('#3a2a1a', '#b88050', shave='#8a7a60', shave_d='#6a5c48', scarf='#f0a8b0', scarf_d='#d0808c'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin'),
              L(outline([(16, 60), (14, 30), (26, 10), (50, 4), (74, 10), (86, 30), (84, 60), (70, 46), (30, 46)]), 'shave', 'f'),
              L(outline([(60, 8), (82, 22), (84, 56), (72, 40)]), 'shave_d', 'f', False),
              L(outline([(30, 4), (32, -8), (50, -12), (68, -8), (70, 4), (50, 8)]), 'mid', 'f', ln=True),
              L(outline([(20, 64), (32, 60), (42, 70), (30, 72)]), OUTC, 'f', False), L(outline([(80, 64), (68, 60), (58, 70), (70, 72)]), OUTC, 'f', False),
              L(quad((24, 76), (32, 80), (40, 76)), OUTC, 'f', False, False, 1.8), L(quad((60, 76), (68, 80), (76, 76)), OUTC, 'f', False, False, 1.8),
              L(outline([(-4, 84), (50, 80), (104, 84), (106, 112), (92, 124), (50, 128), (8, 124), (-6, 112)]), 'scarf', 'f', ln=True),
              L(outline([(56, 82), (104, 86), (104, 110), (90, 122), (60, 124)]), 'scarf_d', 'f', False),
              strand([(4, 100), (50, 96), (96, 100)], 'scarf_d', 'f', 1.2)],
    'side': [L(blob(SIDE_SKULL), 'skin'),
             L(outline([(14, 64), (12, 30), (26, 8), (52, 2), (78, 10), (88, 30), (70, 40), (50, 40), (30, 56)]), 'shave', 'f'),
             L(outline([(30, 4), (32, -8), (54, -12), (72, -6), (72, 6), (50, 6)]), 'mid', 'f', ln=True),
             L(outline([(14, 84), (60, 80), (100, 80), (104, 106), (86, 122), (40, 124), (12, 110)]), 'scarf', 'f', ln=True),
             L(outline([(30, 112), (20, 124), (26, 130, 1), (36, 118)]), 'scarf_d', 'f', ln=True)],
    'back': [L(blob(SKULL_B), 'shave'), L(blob([(58, 12), (86, 36), (84, 68), (66, 84)], 6), 'shave_d', 'b', False),
             L(outline([(30, 4), (32, -8), (50, -12), (68, -8), (70, 4), (50, 8)]), 'mid', 'f', ln=True),
             L(outline([(-4, 86), (50, 82), (104, 86), (106, 112), (92, 124), (50, 128), (8, 124), (-6, 112)]), 'scarf', 'f', ln=True),
             L(outline([(54, 110), (66, 122), (62, 132, 1), (52, 120)]), 'scarf_d', 'f', ln=True)],
}
# Changsu Choi: pelo negro azulado rizado en una mata enorme y redonda que le cae por los lados en patillas largas, con dos
# gafas de buceo blancas encima; ojos cerrados y la boca seria
CHARS['changsu-choi'] = {
    'body': 'normal', 'pal': pal('#24303a', '#f8c890', shade='#18222a', ring='#ece4d0', lens='#2a4a4a'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'face_front': LONG_FACE, 'hairline': (50, 44)},
    'front': messy('front', 3, 16, seed=501, rx=56, ry=48, cy=38, lo=70)
             + [L(outline([(12, 56), (22, 58), (24, 90), (20, 100, 1), (12, 88)]), 'mid', 'f', ln=True),
                L(outline([(88, 56), (78, 58), (76, 90), (80, 100, 1), (88, 88)]), 'mid', 'f', ln=True),
                L(ell(34, 14, 10, 6.4), 'ring', 'f', ln=True), L(ell(66, 14, 10, 6.4), 'ring', 'f', ln=True),
                L(ell(34, 14, 6.4, 3.8), 'lens', 'f', False), L(ell(66, 14, 6.4, 3.8), 'lens', 'f', False)],
    'side': messy('side', 3.5, 14, seed=501, rx=52, ry=48, cy=38, nape=94, sweep=-0.1)
            + [L(outline([(50, 56), (58, 58), (58, 92), (52, 104, 1), (46, 90)]), 'mid', 'f', ln=True),
               L(ell(60, 10, 6, 6.4), 'ring', 'f', ln=True), L(ell(61, 10, 3.6, 3.8), 'lens', 'f', False)],
    'back': messy('back', 3, 16, seed=501, rx=56, ry=48, cy=38, nape=98),
}
# Eunyeong Kim: cabeza enorme de cara roja y ancha, con el pelo morado corto arriba que le baja en patillas gruesas hasta una
# barba que le rodea la mandíbula; cejas moradas pobladas, ojitos de enfado, nariz roja y la boca torcida de dientes
EUN_FACE = blob([(10, 40), (50, 32), (90, 40), (100, 76), (96, 108), (76, 124), (24, 124), (4, 108), (0, 76)])
CHARS['eunyeong-kim'] = {
    'body': 'corpulento', 'pal': pal('#5a4a8a', '#f0806a', skin_d='#d06a54', shade='#443870', nose='#c84a3a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': EUN_FACE, 'hairline': False, 'big_ears': 2, 'ear_out': 9},
    'front': [L(outline([(10, 56), (12, 22), (30, 4), (50, 0), (70, 4), (88, 22), (90, 56), (74, 40), (26, 40)])),
              L(outline([(60, 4), (82, 14), (90, 40), (78, 40)]), 'shade', 'b', False),
              L(outline([(4, 60), (14, 58), (18, 96), (32, 116), (50, 120), (68, 116), (82, 96), (86, 58), (96, 60), (96, 104), (78, 126), (50, 132), (22, 126), (4, 104)]), 'mid', 'f', ln=True),
              L(outline([(20, 58), (34, 52), (46, 60), (34, 64)]), 'mid', 'f', ln=True), L(outline([(80, 58), (66, 52), (54, 60), (66, 64)]), 'mid', 'f', ln=True),
              L(outline([(26, 66), (40, 66), (38, 72), (28, 72)]), WHITE, 'f', ln=True), L(outline([(74, 66), (60, 66), (62, 72), (72, 72)]), WHITE, 'f', ln=True),
              L(ell(33, 69, 1.4, 1.6), OUTC, 'f', False), L(ell(67, 69, 1.4, 1.6), OUTC, 'f', False),
              L(ell(50, 80, 5, 3.6), 'nose', 'f', ln=True),
              L(outline([(24, 98), (40, 90), (60, 92), (76, 100), (60, 104), (40, 104)]), WHITE, 'f', ln=True),
              L([(26, 98), (74, 100)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(28, 116), (6, 90), (6, 30), (24, 6), (54, -2), (80, 8), (94, 30), (100, 70), (98, 108), (80, 126), (50, 128)]), 'skin'),
             L(outline([(6, 80), (6, 30), (24, 6), (54, -2), (80, 8), (88, 26), (60, 22), (40, 40), (36, 80), (46, 116), (24, 112)])),
             L(outline([(46, 110), (70, 124), (90, 118), (98, 108), (80, 116), (60, 114)]), 'mid', 'f', ln=True),
             L(outline([(84, 96), (98, 96), (98, 104), (86, 104)]), WHITE, 'f', ln=True), L([(78, 64), (94, 66)], 'mid', 'f', False, False, 3.0)] + side_eye(70),
    'back': [L(outline([(6, 104), (6, 30), (24, 6), (50, 0), (76, 6), (94, 30), (94, 104), (50, 112)])),
             L(outline([(56, 2), (82, 12), (94, 44), (92, 100), (64, 110)]), 'shade', 'b', False)],
}
# Sung-jin Noh: pelo azul añil oscuro liso y abultado, peinado de lado con un flequillo largo que le cae en diagonal sobre la
# frente y puntas en la nuca; cejas gruesas de enfado, ojos rasgados y la boca seria
CHARS['sung-jin-noh'] = {
    'body': 'normal', 'pal': pal('#24244a', '#f8c080', iris='#1e1e1e', shade='#181838', light='#4a4a7a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 92, 1), (12, 66), (6, 36), (18, 10), (48, -2), (78, 6), (94, 28), (94, 60), (90, 92, 1), (84, 76), (84, 62), (16, 62), (16, 78)])),
              L(outline([(60, 2), (86, 14), (94, 40), (90, 86), (84, 74), (80, 40)]), 'shade', 'b', False),
              L(outline([(12, 70), (14, 42), (28, 24), (54, 16), (76, 22), (90, 40), (88, 62), (78, 48), (62, 42), (46, 46), (34, 56), (24, 72, 1)]), 'mid', 'f', ln=True),
              L(outline([(30, 26), (54, 18), (66, 22), (46, 28)]), 'light', 'f', False)],
    'side': [L(outline([(54, 70), (52, 92), (42, 98), (30, 108, 1), (22, 94), (10, 76), (8, 36), (22, 10), (52, -2), (80, 6), (96, 26), (96, 50), (86, 48), (70, 50), (60, 54)])),
             L(outline([(10, 44), (34, 44), (46, 80), (40, 96), (22, 94), (10, 76)]), 'shade', 'b', False)],
    'back': [L(outline([(10, 92, 1), (12, 66), (6, 36), (18, 10), (48, -2), (78, 6), (94, 28), (94, 66), (90, 92, 1), (66, 88), (50, 100, 1), (34, 88)])),
             L(outline([(56, 2), (86, 16), (94, 44), (90, 88), (64, 92)]), 'shade', 'b', False)],
}
# Chi-won Ho (portero suplente): un gorro de lana verde grisáceo con manchas pardas, muy hondo, que le tapa hasta las cejas;
# por debajo asoma el pelo negro azulado en las patillas; ojos negros grandes de enfado
CHARS['chi-won-ho'] = {
    'body': 'normal', 'pal': pal('#24303a', '#f8c080', hat='#9aaa78', hat_d='#7a6a4a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(14, 60), (20, 60), (22, 86), (16, 92, 1), (12, 80)]), 'mid', 'b', ln=True),
              L(outline([(86, 60), (80, 60), (78, 86), (84, 92, 1), (88, 80)]), 'mid', 'b', ln=True),
              L(blob(SKULL_F), 'skin'),
              L(outline([(8, 66), (6, 28), (18, 2), (50, -10), (82, 2), (94, 28), (92, 66), (50, 60)]), 'hat', 'f', ln=True),
              L(outline([(60, -4), (84, 8), (92, 40), (90, 62), (72, 60), (70, 20)]), 'hat_d', 'f', False),
              L(outline([(16, 30), (34, 22), (40, 34), (24, 40)]), 'hat_d', 'f', False)],
    'side': [L(blob(SIDE_SKULL), 'skin'), L(outline([(40, 60), (50, 62), (50, 90), (44, 96, 1)]), 'mid', 'b', ln=True),
             L(outline([(4, 76), (2, 30), (18, 2), (50, -10), (78, -2), (94, 22), (96, 60), (60, 58), (30, 66)]), 'hat', 'f', ln=True),
             L(outline([(4, 40), (34, 30), (50, 54), (30, 70), (4, 76)]), 'hat_d', 'f', False)],
    'back': [L(blob(SKULL_B), 'skin'), L(outline([(16, 78), (84, 78), (80, 92), (50, 96), (20, 92)]), 'mid', 'b', ln=True),
             L(outline([(6, 82), (4, 30), (18, 2), (50, -10), (82, 2), (96, 30), (94, 82), (50, 78)]), 'hat', 'f', ln=True),
             L(outline([(20, 30), (50, 20), (80, 30), (84, 60), (50, 54), (16, 60)]), 'hat_d', 'f', False)],
}
# Dong-hyun Seul: pelo castaño muy oscuro en tazón con el flequillo recto cortado en pico; barbilla larga y en punta,
# ojos blancos de enfado con cejas gruesas y la boca en una raya
CHARS['dong-hyun-seul'] = {
    'body': 'normal', 'pal': pal('#3a2a1e', '#f8c080', shade='#2a1e14'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 102, 'face_front': LONG_FACE, 'hairline': False, 'big_ears': 2, 'ear_out': 4},
    'front': bowl('front', fringe_y=50)
             + [L(outline([(14, 60), (16, 42), (30, 34), (50, 32), (70, 34), (84, 42), (86, 60), (78, 52), (60, 50), (50, 56, 1), (40, 50), (22, 52)]), 'mid', 'f')]
             + white_eyes(76, 14, 6, 4.6, 2) + [L([(22, 66), (42, 72)], OUTC, 'f', False, False, 2.8), L([(78, 66), (58, 72)], OUTC, 'f', False, False, 2.8)],
    'side': bowl('side') + side_eye(76) + [L([(76, 66), (90, 70)], OUTC, 'f', False, False, 2.6)],
    'back': bowl('back', nape=88),
}
# Jung-hoon Yi: pelo azul petróleo en tazón abombado como una seta, con el flequillo recto en mechones; ojos verdes
# grandes de enfado y la boca seria
CHARS['jung-hoon-yi'] = {
    'body': 'normal', 'pal': pal('#1e5a7a', '#f8c8a0', iris='#4a8a4a', shade='#164462'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(2, 70), (0, 40), (14, 10), (50, -2), (86, 10), (100, 40), (98, 70), (84, 66), (16, 66)])),
              L(outline([(60, 2), (88, 14), (100, 44), (96, 68), (84, 62), (80, 34)]), 'shade', 'b', False),
              L(outline([(4, 70), (6, 44), (24, 24), (50, 18), (76, 24), (94, 44), (96, 70), (82, 62), (76, 66, 1), (70, 58), (62, 62, 1), (56, 56), (50, 62, 1), (44, 56),
                         (38, 62, 1), (30, 58), (24, 66, 1), (18, 62)]), 'mid', 'f')],
    'side': [L(outline([(44, 92), (24, 88), (10, 76), (0, 72), (2, 40), (18, 10), (50, -2), (82, 8), (98, 28), (100, 54), (92, 60), (78, 54), (64, 54), (54, 64), (50, 80)])),
             L(outline([(4, 44), (34, 44), (42, 74), (6, 72)]), 'shade', 'b', False)],
    'back': [L(outline([(2, 74), (0, 40), (14, 10), (50, -2), (86, 10), (100, 40), (98, 74), (84, 80), (50, 82), (16, 80)])),
             L(outline([(56, 2), (88, 14), (100, 44), (96, 76), (66, 82)]), 'shade', 'b', False)],
}
# Joon-ho Ja: pelo verde muy oscuro con raya en medio, liso y abombado, que le cubre las sienes y la nuca; gafas de montura
# roja fina sobre unos ojos rasgados de enfado y la boca seria
CHARS['joon-ho-ja'] = {
    'body': 'normal', 'pal': pal('#2e3a2e', '#fcc890', iris='#1e1e1e', shade='#202a20', rim='#c02a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': [(14, 66), (16, 46), (30, 40), (50, 50), (70, 40), (84, 46), (86, 66)]},
    'front': [L(outline([(10, 74), (6, 40), (18, 12), (50, 2), (82, 12), (94, 40), (90, 74), (82, 66), (18, 66)])),
              L(outline([(60, 6), (84, 18), (94, 44), (88, 70), (78, 40)]), 'shade', 'b', False),
              strand([(50, 4), (50, 48)], 'deep', 'b', 1.2)] + rect_glasses('front', 76, (190, 40, 40, 255)),
    'side': [L(outline([(44, 92), (22, 88), (10, 64), (8, 36), (22, 10), (52, 2), (78, 10), (92, 28), (90, 44), (76, 46), (60, 50), (52, 64), (50, 80)])),
             L(outline([(10, 40), (34, 44), (42, 84), (22, 88), (10, 64)]), 'shade', 'b', False)] + rect_glasses('side', 76, (190, 40, 40, 255)),
    'back': [L(outline([(10, 84), (6, 40), (18, 12), (50, 2), (82, 12), (94, 40), (90, 84), (50, 92)])),
             L(outline([(56, 4), (84, 18), (94, 48), (88, 82), (64, 90)]), 'shade', 'b', False), strand([(50, 4), (50, 90)], 'deep', 'b', 1.2)],
}
