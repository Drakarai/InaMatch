"""Knights of Queen (IE3, Inglaterra): gorros de la guardia, yelmos, cascos de boxeo, crestas y melenas, con sus modelos 3D
como referencia (contornos calcados sobre una rejilla de unidades de cabeza)."""
from chars import CHARS, L, OUTC, blob, ell, messy, outline, pal, rope, spk, strand
from chars_alius import LONG_FACE, SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE
from chars_bigwaves import bald, rect_glasses, side_eye, white_eyes
from chars_firedragon import bowl
from heads import quad

WHITE = (250, 250, 250, 255)


def mohawk(view, c='mid', h=-22, w=10, back_to=96):
    if view == 'front':
        return [L(outline([(50 - w, 22), (44, 0), (50, h, 1), (56, 0), (50 + w, 22), (50, 26)]), c, 'f', ln=True)]
    if view == 'side':
        return [L(outline([(18, 30), (20, 10), (40, h + 6), (66, h + 2), (84, h + 10, 1), (76, 6), (80, 20), (58, 14), (36, 20), (24, 40)]), c, 'f', ln=True)]
    return [L(outline([(50 - w, 6), (50, h, 1), (50 + w, 6), (50 + w * 0.6, back_to), (50, back_to + 4, 1), (50 - w * 0.6, back_to)]), c, 'f', ln=True)]


# Freddy McQueen (portero): cabeza ancha de mandíbula enorme y orejas grandes; pelo castaño corto en un cepillo plano arriba,
# las sienes rapadas con una raya clara afeitada que da la vuelta a la cabeza; cejas negras gruesas y nariz larga
FREDDY_FACE = blob([(12, 40), (50, 34), (88, 40), (94, 76), (90, 108), (70, 122), (30, 122), (10, 108), (6, 76)])
CHARS['freddy-mcqueen'] = {
    'body': 'corpulento', 'pal': pal('#5a3a20', '#fce4b8', skin_d='#e8c49a', nose='#f0b090'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 104, 'face_front': FREDDY_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 9},
    'front': [L(outline([(18, 44), (16, 6), (50, 0), (84, 6), (82, 44)]), 'skin'),
              L(outline([(20, 18), (24, 2), (50, -4), (76, 2), (80, 18), (50, 14)]), 'mid', 'f', ln=True),
              L(outline([(16, 20), (24, 22), (24, 50), (18, 50)]), 'mid', 'f'), L(outline([(84, 20), (76, 22), (76, 50), (82, 50)]), 'mid', 'f'),
              L(outline([(22, 70), (32, 64), (44, 72), (42, 76), (32, 72), (24, 76)]), OUTC, 'f', False),
              L(outline([(78, 70), (68, 64), (56, 72), (58, 76), (68, 72), (76, 76)]), OUTC, 'f', False),
              L(outline([(44, 72), (56, 72), (60, 94), (50, 98), (40, 94)]), 'nose', 'f', ln=True)],
    'side': [L(outline([(36, 112), (14, 104), (10, 60), (12, 8), (50, -2), (80, 6), (92, 30), (96, 70), (94, 104), (80, 120), (56, 122)]), 'skin'),
             L(outline([(12, 64), (12, 8), (50, -2), (82, 4), (84, 16), (60, 14), (40, 30), (30, 60)]), 'mid'),
             L(outline([(14, 28), (60, 18), (84, 22), (84, 28), (60, 26), (20, 36)]), 'skin', 'f', False),
             L(outline([(86, 70), (106, 88), (92, 96)]), 'nose', 'f', ln=True), L([(76, 66), (92, 72)], OUTC, 'f', False, False, 3)],
    'back': [L(outline([(16, 90), (14, 6), (50, 0), (86, 6), (84, 90), (50, 96)]), 'mid'),
             L(outline([(14, 26), (50, 20), (86, 26), (86, 34), (50, 28), (14, 34)]), 'skin', 'f', False),
             L(outline([(56, 36), (86, 36), (84, 88), (62, 94)]), 'shade', 'b', False)],
}
# Jonny Gascoigne: calvo de piel morena clara con un tatuaje negro de llamas en espiral en lo alto de la cabeza; orejas
# grandes, ojos blancos redondos y una sonrisa enorme de boca morada
CHARS['jonny-gascoigne'] = {
    'body': 'delgado', 'pal': pal('#1e1e1e', '#d8b080', skin_d='#b88e60', mouth='#7a5ab0'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': LONG_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 6},
    'front': bald('front') + [L(outline([(26, 34), (24, 18), (34, 6), (46, 4), (36, 12), (34, 24), (40, 22), (36, 34)]), 'mid', 'f'),
                              L(ell(32, 36, 4, 4) + [ell(32, 36, 4, 4)[0]], 'mid', 'f', False, False, 1.6),
                              L(outline([(38, 10), (54, 0), (48, 14), (42, 24)]), 'mid', 'f')]
             + white_eyes(78, 14, 5.6, 5, 2)
             + [L(outline([(30, 96), (50, 100), (70, 94), (62, 108), (50, 112), (38, 108)]), 'mouth', 'f', ln=True), L(quad((30, 96), (50, 102), (70, 94)), WHITE, 'f', False, False, 2)],
    'side': bald('side') + [L(outline([(62, 14), (74, 12), (84, 24), (74, 22), (70, 30), (80, 36), (70, 40)]), 'mid', 'f'), L(ell(74, 40, 3.6, 3.6) + [ell(74, 40, 3.6, 3.6)[0]], 'mid', 'f', False, False, 1.6)]
            + side_eye(78) + [L(outline([(80, 96), (96, 92), (92, 106), (82, 104)]), 'mouth', 'f', ln=True)],
    'back': bald('back'),
}
# David Buckingham: el gorro de piel negro altísimo de la guardia real, con un penacho rojo a un lado, que le tapa hasta la
# nariz; por debajo asoma el pelo rubio oscuro en la nuca y lleva el barboquejo dorado bajo la barbilla
CHARS['david-buckingham'] = {
    'body': 'normal', 'pal': pal('#b88a40', '#f8c890', hat='#2e2c2e', hat_d='#1e1c1e', plume='#c81e1e', strap='#c8b060'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 100, 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin'),
              L(outline([(16, 84), (22, 96), (40, 110), (60, 110), (78, 96), (84, 84)]) + [(16, 84)], 'strap', 'f', False, False, 2.2),
              L(outline([(4, 80), (2, -36), (10, -48), (50, -52), (90, -48), (98, -36), (96, 80), (50, 82)]), 'hat', 'f', ln=True),
              L(outline([(60, -48), (90, -46), (96, -30), (94, 78), (70, 80), (66, 0)]), 'hat_d', 'f', False),
              L(outline([(96, 0), (104, 2), (104, 30), (96, 30)]), 'plume', 'f', ln=True),
              L(outline([(44, 80), (56, 80), (56, 90), (44, 90)]), 'skin_d', 'f', False)],
    'side': [L(blob(SIDE_SKULL), 'skin'), L(outline([(22, 82), (40, 84), (44, 96), (26, 96)]), 'mid', 'b'),
             L(quad((40, 80), (70, 110), (92, 96)), 'strap', 'f', False, False, 2.2),
             L(outline([(-2, 80), (-4, -36), (6, -48), (50, -52), (88, -48), (98, -36), (98, 76), (50, 82)]), 'hat', 'f', ln=True),
             L(outline([(-6, 0), (2, 2), (2, 30), (-6, 30)]), 'plume', 'f', ln=True)],
    'back': [L(blob(SKULL_B), 'skin'), L(outline([(14, 80), (86, 80), (84, 94), (50, 98), (16, 94)]), 'mid', 'b', ln=True),
             L(outline([(4, 82), (2, -36), (10, -48), (50, -52), (90, -48), (98, -36), (96, 82), (50, 84)]), 'hat', 'f', ln=True),
             L(outline([(-4, 0), (4, 2), (4, 30), (-4, 30)]), 'plume', 'f', ln=True)],
}
# Lance Rawton: un yelmo de caballero gris verdoso con la visera cerrada (solo una rendija negra a la altura de los ojos),
# una gorguera remachada y un penacho de plumas crema que cae hacia atrás
CHARS['lance-rawton'] = {
    'body': 'normal', 'pal': pal('#e8dcc0', '#fcd8b0', helm='#a8aa98', helm_d='#7e8070', slit='#1e1e1e', feather='#e8dcc0', feather_d='#c0b498'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False, 'ears': False},
    'front': [L(rope((52, 0), (60, -30), (40, -44), 7), 'feather', 'b', ln=True), L(rope((54, 0), (76, -30), (104, -40), 7), 'feather', 'b', ln=True),
              L(rope((54, 0), (80, -16), (112, -18), 6), 'feather_d', 'b', ln=True), L(rope((52, 0), (70, -40), (92, -52), 6), 'feather', 'b', ln=True),
              L(outline([(10, 100), (8, 30), (22, 6), (50, -2), (78, 6), (92, 30), (90, 100), (70, 108), (30, 108)]), 'helm', 'f', ln=True),
              L(outline([(60, 2), (82, 14), (92, 40), (90, 98), (70, 106), (70, 50)]), 'helm_d', 'f', False),
              L([(50, 0), (50, 60)], 'helm_d', 'f', False, False, 1.4),
              L(outline([(14, 62), (50, 56), (86, 62), (84, 80), (50, 74), (16, 80)]), 'slit', 'f', ln=True),
              L(outline([(4, 102), (50, 96), (96, 102), (98, 116), (50, 112), (2, 116)]), 'helm', 'f', ln=True)]
             + [L(ell(x, 108, 1.4, 1.4), 'helm_d', 'f', False) for x in (14, 30, 50, 70, 86)],
    'side': [L(rope((50, 2), (30, -30), (0, -40), 7), 'feather', 'b', ln=True), L(rope((50, 2), (20, -14), (-14, -18), 7), 'feather_d', 'b', ln=True),
             L(rope((50, 2), (40, -36), (20, -54), 6), 'feather', 'b', ln=True),
             L(outline([(14, 96), (8, 30), (24, 6), (52, -2), (78, 6), (94, 30), (98, 70), (92, 98), (60, 104)]), 'helm', 'f', ln=True),
             L(ell(52, 60, 7, 7), 'helm_d', 'f', ln=True),
             L(outline([(72, 60), (98, 60), (98, 76), (74, 76)]), 'slit', 'f', ln=True),
             L(outline([(14, 98), (96, 98), (98, 112), (12, 112)]), 'helm', 'f', ln=True)],
    'back': [L(outline([(10, 100), (8, 30), (22, 6), (50, -2), (78, 6), (92, 30), (90, 100), (50, 106)]), 'helm', 'f', ln=True),
             L(outline([(56, 2), (82, 14), (92, 40), (90, 98), (60, 104)]), 'helm_d', 'f', False),
             L(rope((50, 6), (20, -24), (-14, -34), 7), 'feather', 'f', ln=True), L(rope((50, 6), (30, -6), (-6, -4), 7), 'feather_d', 'f', ln=True),
             L(rope((50, 6), (60, -30), (84, -40), 6), 'feather', 'f', ln=True),
             L(outline([(4, 102), (50, 98), (96, 102), (98, 116), (50, 112), (2, 116)]), 'helm', 'f', ln=True)],
}
# Edge Ripper: piel pálida cosida, con cicatrices en la cara; melena gris verdosa lisa y larga con raya a un lado, que le cae
# por los lados hasta los hombros; ojos rojizos de pupila pequeña y la boca en una raya cosida
CHARS['edge-ripper'] = {
    'body': 'delgado', 'pal': pal('#a8c0b8', '#fcecd0', shade='#7e968e', stitch='#5a4a3a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': LONG_FACE, 'hairline': False, 'ears': False},
    'front': [L(outline([(-8, 116, 1), (2, 80), (4, 30), (18, 6), (44, -2), (76, 6), (94, 28), (98, 80), (110, 116, 1), (86, 104), (84, 60), (60, 26), (40, 30), (20, 60),
                         (16, 104)])),
              L(outline([(58, 4), (86, 18), (96, 50), (98, 100), (86, 100), (80, 60), (60, 28)]), 'shade', 'b', False),
              L(outline([(40, 4), (30, 30), (22, 70), (14, 100), (26, 70), (40, 30)]), 'shade', 'f', False),
              L(ell(34, 78, 6, 4.4), WHITE, 'f', ln=True), L(ell(66, 78, 6, 4.4), WHITE, 'f', ln=True),
              L(ell(34, 78, 2.2, 2.2), (150, 70, 40, 255), 'f', False), L(ell(66, 78, 2.2, 2.2), (150, 70, 40, 255), 'f', False),
              L([(26, 74), (42, 72)], OUTC, 'f', False, False, 1.6), L([(74, 74), (58, 72)], OUTC, 'f', False, False, 1.6),
              L([(30, 84), (24, 98)], 'stitch', 'f', False, False, 1.2), L([(62, 60), (70, 50)], 'stitch', 'f', False, False, 1.2),
              L([(34, 102), (66, 102)], 'stitch', 'f', False, False, 1.4)] + [L([(x, 99), (x, 105)], 'stitch', 'f', False, False, 1.0) for x in (38, 46, 54, 62)],
    'side': [L(outline([(56, 70), (54, 110), (40, 104), (26, 118, 1), (16, 100), (2, 106, 1), (4, 70), (4, 30), (18, 6), (48, -2), (76, 6), (92, 26), (92, 44), (78, 40),
                        (64, 50)])),
             L(outline([(6, 40), (34, 44), (48, 90), (40, 106), (16, 100), (6, 76)]), 'shade', 'b', False)] + side_eye(78),
    'back': [L(outline([(-8, 116, 1), (2, 80), (4, 30), (18, 6), (50, -2), (82, 6), (96, 30), (98, 80), (110, 116, 1), (80, 112), (50, 118), (20, 112)])),
             L(outline([(56, 4), (86, 18), (98, 60), (104, 110), (70, 112), (64, 50)]), 'shade', 'b', False),
             strand([(50, 0), (50, 116)], 'deep', 'b', 1.0)],
}
# Peter Cole: pelo granate muy abultado en forma de corazón invertido, con dos alas anchas a los lados y un pico en la
# frente; gafas cuadradas de montura blanca y cristales azul oscuro y la boca seria
CHARS['peter-cole'] = {
    'body': 'normal', 'pal': pal('#6a1e1e', '#fcc890', shade='#4e1414', light='#9a4a4a', frame='#ece4d0', lens='#3a4a6a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin'),
              L(outline([(14, 72), (0, 50), (-4, 18), (2, -6, 1), (24, 0), (50, 4), (76, 0), (98, -6, 1), (104, 18), (100, 50), (86, 72), (80, 60), (66, 52), (50, 60, 1),
                         (34, 52), (20, 60)]), 'mid', 'f'),
              L(outline([(60, 4), (94, 0), (100, 30), (90, 62), (76, 40)]), 'shade', 'f', False),
              L(ell(20, 8, 6, 3.6), 'light', 'f', False),
              L(outline([(16, 68), (46, 68), (46, 84), (18, 84)]), 'lens', 'f', ln=True), L(outline([(84, 68), (54, 68), (54, 84), (82, 84)]), 'lens', 'f', ln=True),
              L(outline([(16, 68), (46, 68), (46, 84), (18, 84)]) + [(16, 68)], 'frame', 'f', False, False, 2.4),
              L(outline([(84, 68), (54, 68), (54, 84), (82, 84)]) + [(84, 68)], 'frame', 'f', False, False, 2.4), L([(46, 72), (54, 72)], 'frame', 'f', False, False, 2.2)],
    'side': [L(blob(SIDE_SKULL), 'skin'),
             L(outline([(18, 80), (4, 50), (0, 20), (14, 0), (46, -10), (80, -2), (96, 16), (98, 38), (84, 54), (72, 46), (56, 54), (44, 70), (30, 84)]), 'mid'),
             L(outline([(4, 40), (30, 40), (40, 70), (24, 82)]), 'shade', 'b', False),
             L(outline([(76, 68), (94, 68), (94, 84), (78, 84)]), 'lens', 'f', ln=True), L([(46, 72), (76, 72)], 'frame', 'f', False, False, 2.2)],
    'back': [L(outline([(14, 80), (-4, 50), (-6, 14), (2, -6, 1), (24, 0), (50, 4), (76, 0), (98, -6, 1), (106, 14), (104, 50), (86, 80), (60, 86), (50, 100, 1), (40, 86)])),
             L(outline([(56, 4), (96, 0), (104, 40), (86, 78), (60, 84)]), 'shade', 'b', False)],
}
# Gary Mane: la cabeza rapada con el pelo rosa claro muy corto y una cresta rosa fuerte que nace en la frente, sube y cae
# en un mechón largo por delante de la cara hasta la barbilla; orejas grandes y ojos verdes de enfado
CHARS['gary-mane'] = {
    'body': 'normal', 'pal': pal('#c85a90', '#f8b880', iris='#3a7a5a', shave='#e8b0d0', shade='#a04070'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False, 'big_ears': 2, 'ear_out': 5},
    'front': [L(outline([(16, 58), (14, 30), (26, 10), (50, 4), (74, 10), (86, 30), (84, 58), (72, 48), (28, 48)]), 'shave'),
              L(outline([(40, 12), (44, -4), (56, -8), (62, 10), (60, 40), (56, 70), (50, 92, 1), (46, 62), (40, 40)]), 'mid', 'f', ln=True),
              L(outline([(52, -4), (60, 10), (58, 40), (54, 66)]), 'shade', 'f', False)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (12, 30), (26, 10), (52, 4), (78, 10), (90, 28), (84, 40), (66, 42), (56, 52), (52, 66), (50, 80)]), 'shave'),
             L(outline([(20, 30), (24, 6), (50, -10), (78, -6), (96, 14), (100, 40), (96, 64, 1), (90, 40), (78, 20), (54, 10), (34, 20)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(16, 84), (14, 30), (26, 10), (50, 4), (74, 10), (86, 30), (84, 84), (50, 90)]), 'shave'),
             L(outline([(58, 8), (82, 22), (86, 60), (82, 82), (64, 88)]), (200, 140, 170, 255), 'b', False),
             L(outline([(42, 8), (46, -8), (56, -8), (58, 8), (54, 30), (46, 30)]), 'mid', 'f', ln=True)],
}
# Paul Appleton: pelo rubio oscuro en tazón con el flequillo recto en mechones finos hasta las cejas; ojos verdes de
# enfado y la boca seria
CHARS['paul-appleton'] = {
    'body': 'normal', 'pal': pal('#c0a060', '#f8c088', iris='#2a8a6a', shade='#9a7e44'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': bowl('front', fringe_y=56)
             + [L(outline([(12, 64), (14, 42), (30, 26), (50, 22), (70, 26), (86, 42), (88, 64), (78, 60), (70, 64, 1), (64, 58), (56, 62, 1), (50, 58), (44, 62, 1),
                           (38, 58), (30, 64, 1), (22, 60)]), 'mid', 'f')],
    'side': bowl('side'),
    'back': bowl('back', nape=90),
}
# Eric Purpleton: pelo castaño oscuro liso peinado hacia atrás y suelto hasta los hombros, con una cinta crema fina en la
# frente; cejas gruesas, ojos de sueño y la boca torcida
CHARS['eric-purpleton'] = {
    'body': 'normal', 'pal': pal('#5a4630', '#fcd8a8', iris='#5a8ab0', shade='#42321e', band='#e8d8a0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': [(16, 64), (18, 46), (30, 38), (50, 36), (70, 38), (82, 46), (84, 64)]},
    'front': [L(outline([(2, 108, 1), (6, 80), (4, 36), (18, 10), (50, 0), (82, 10), (96, 36), (94, 80), (98, 108, 1), (84, 96), (82, 62), (18, 62), (16, 96)])),
              L(outline([(60, 4), (86, 16), (96, 44), (94, 100), (84, 92), (80, 50)]), 'shade', 'b', False),
              strand([(50, 4), (50, 30)], 'deep', 'b', 1.0), strand([(36, 8), (28, 30)], 'deep', 'b', 1.0), strand([(64, 8), (72, 30)], 'deep', 'b', 1.0),
              L(quad((8, 40), (50, 30), (92, 40)), 'band', 'f', False, False, 2.4)],
    'side': [L(outline([(54, 70), (52, 96), (34, 104), (16, 112, 1), (10, 92), (4, 36), (18, 10), (50, 0), (78, 8), (92, 28), (90, 46), (76, 46), (62, 52)])),
             L(outline([(8, 40), (32, 40), (46, 80), (40, 100), (16, 106), (8, 80)]), 'shade', 'b', False),
             L(quad((6, 40), (50, 30), (92, 38)), 'band', 'f', False, False, 2.4)],
    'back': [L(outline([(2, 108, 1), (6, 80), (4, 36), (18, 10), (50, 0), (82, 10), (96, 36), (94, 80), (98, 108, 1), (70, 104), (50, 110), (30, 104)])),
             L(outline([(56, 4), (86, 16), (96, 44), (96, 104), (66, 106)]), 'shade', 'b', False),
             L(quad((4, 42), (50, 36), (96, 42)), 'band', 'f', False, False, 2.4)],
}
# Edgar Partinus: melena azul grisáceo que le envuelve la cabeza en mechones anchos barridos hacia un lado, tapándole el
# ojo derecho, y que se recoge atrás en una coleta baja con una goma roja; ojo azul y una sonrisa tranquila
CHARS['edgar-partinus'] = {
    'body': 'normal', 'pal': pal('#6a86a8', '#fcd8b8', iris='#2a7a9a', shade='#4e6a8a', tie='#c8202a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(2, 100), (-2, 40), (12, 10), (46, -4), (80, 4), (98, 30), (100, 70), (94, 96), (84, 90), (84, 62), (16, 62), (14, 94)])),
              L(outline([(60, 2), (88, 14), (100, 44), (96, 94), (84, 88), (80, 40)]), 'shade', 'b', False),
              L(outline([(10, 74), (8, 44), (24, 24), (50, 14), (74, 20), (90, 36), (94, 50), (82, 46), (66, 44), (54, 50), (46, 62), (44, 84, 1), (36, 66), (24, 66)]), 'mid', 'f', ln=True),
              L(outline([(80, 50), (88, 54), (86, 90), (82, 100, 1), (78, 80)]), 'mid', 'f', ln=True),
              strand([(30, 20), (24, 50)], 'shade', 'f', 1.0), strand([(60, 16), (40, 40)], 'shade', 'f', 1.0)],
    'side': [L(outline([(44, 92), (22, 88), (10, 70), (0, 40), (14, 12), (46, -4), (78, 4), (96, 24), (98, 50), (86, 50), (70, 50), (58, 56), (52, 70), (50, 80)])),
             L(outline([(4, 40), (34, 40), (44, 80), (24, 88), (8, 70)]), 'shade', 'b', False),
             L(outline([(14, 70), (2, 86), (-4, 100, 1), (10, 90), (20, 78)]), 'mid', 'b', ln=True), L(ell(12, 74, 4, 3.6), 'tie', 'b', ln=True)],
    'back': [L(outline([(4, 90), (-2, 40), (12, 10), (50, -4), (88, 10), (102, 40), (96, 90), (60, 80), (50, 82), (40, 80)])),
             L(outline([(56, 0), (88, 12), (100, 44), (96, 86), (62, 78)]), 'shade', 'b', False),
             L(outline([(42, 78), (58, 78), (60, 100), (50, 112, 1), (40, 100)]), 'mid', 'f', ln=True), L(outline([(42, 80), (58, 80), (58, 86), (42, 86)]), 'tie', 'f', ln=True)],
}
# Phillip Owen: pelo gris verdoso de pinchos largos hacia arriba y hacia atrás; ojos grises de enfado y los dientes apretados
CHARS['phillip-owen'] = {
    'body': 'normal', 'pal': pal('#9a9a80', '#fcc890', iris='#5a6a6a', shade='#7a6a54'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'hairline': (56, 50)},
    'front': messy('front', 18, 9, seed=601, rx=50, ry=42, lo=66),
    'side': messy('side', 22, 8, seed=601, rx=48, ry=42, nape=92, sweep=-0.6) + [spk((58, 30), (88, 40), (92, 60), 4, z='f', light_left=False)],
    'back': messy('back', 18, 9, seed=601, rx=50, ry=42, nape=94),
}
# Servilius Jeeves (portero suplente): pelo rubio liso en casco con un flequillo en pico que le cae en mechones hasta los
# ojos; ojos turquesa y la boca seria
CHARS['servilius-jeeves'] = {
    'body': 'normal', 'pal': pal('#d8c070', '#fce0b8', iris='#2a9aa0', shade='#b09a50'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': bowl('front', fringe_y=58)
             + [L(outline([(12, 70, 1), (14, 42), (30, 26), (50, 22), (70, 26), (86, 42), (88, 70, 1), (78, 56), (66, 52), (56, 58), (50, 86, 1), (44, 58), (34, 52), (22, 56)]), 'mid', 'f'),
                L(outline([(56, 26), (78, 32), (86, 54), (76, 52), (66, 40)]), 'shade', 'f', False)],
    'side': bowl('side') + [spk((60, 30), (88, 40), (92, 64), 4, z='f', light_left=False)],
    'back': bowl('back', nape=88),
}
# Martin Squall: calvo con una cresta roja peinada hacia atrás en lo alto; una mascarilla gris azulada con un filtro crema en
# forma de rueda, sujeta con una correa; ojos blancos de enfado
CHARS['martin-squall'] = {
    'body': 'corpulento', 'pal': pal('#b8301e', '#f8c078', skin_d='#e0a060', mask='#7a90a8', filt='#e8dcc0', strap='#e8dcc0'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 8},
    'front': bald('front') + mohawk('front', h=-26, w=8)
             + [L(outline([(22, 70), (36, 70), (34, 76), (26, 76)]), WHITE, 'f', ln=True), L(outline([(78, 70), (64, 70), (66, 76), (74, 76)]), WHITE, 'f', ln=True),
                L(quad((8, 92), (50, 88), (92, 92)), 'strap', 'f', False, False, 2.4),
                L(outline([(30, 84), (50, 80), (70, 84), (72, 102), (60, 112), (40, 112), (28, 102)]), 'mask', 'f', ln=True),
                L(ell(50, 97, 11, 9), 'filt', 'f', ln=True), L([(50, 88), (50, 97), (42, 104)], 'mask', 'f', False, False, 1.4), L([(50, 97), (58, 104)], 'mask', 'f', False, False, 1.4)],
    'side': bald('side') + mohawk('side', h=-22) + side_eye(72)
            + [L(quad((10, 82), (50, 86), (88, 90)), 'strap', 'f', False, False, 2.4), L(outline([(80, 84), (98, 84), (100, 104), (84, 108)]), 'mask', 'f', ln=True)],
    'back': bald('back') + mohawk('back', h=-24, back_to=78) + [L(quad((6, 84), (50, 92), (94, 84)), 'strap', 'f', False, False, 2.4)],
}
# Nick Woodgate: la cabeza con el pelo castaño oliva muy corto peinado hacia atrás y una crestita en punta en lo alto;
# orejas grandes, ojos negros y una sonrisa
CHARS['nick-woodgate'] = {
    'body': 'normal', 'pal': pal('#8a7230', '#fcc8a0', shade='#5a4a20'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 94, 'hairline': [(16, 56), (20, 36), (40, 30), (50, 34), (60, 30), (80, 36), (84, 56)], 'big_ears': 3,
             'ear_out': 6},
    'front': [L(outline([(16, 60), (14, 30), (26, 10), (50, 4), (74, 10), (86, 30), (84, 60), (80, 50), (20, 50)])),
              L(outline([(60, 6), (82, 20), (86, 50), (76, 30)]), 'shade', 'b', False)] + mohawk('front', h=-18, w=6),
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (12, 30), (26, 10), (52, 2), (80, 6), (94, 22), (92, 36), (74, 38), (60, 44), (52, 62), (50, 80)])),
             L(outline([(12, 40), (34, 44), (42, 84), (22, 88), (12, 64)]), 'shade', 'b', False)] + mohawk('side', h=-16),
    'back': [L(outline([(16, 84), (14, 30), (26, 10), (50, 4), (74, 10), (86, 30), (84, 84), (50, 90)])),
             L(outline([(36, 10), (50, 4), (64, 10), (58, 86), (50, 92, 1), (42, 86)]), 'shade', 'b', False)] + mohawk('back', h=-18, w=6, back_to=40),
}
# Mikey Richards: pelo rubio oscuro peinado todo hacia atrás, liso y largo hasta la nuca, que le baja en patillas finas;
# cara alargada pálida, ojos de enfado y la boca seria
CHARS['mikey-richards'] = {
    'body': 'normal', 'pal': pal('#c0a868', '#fce8c0', shade='#9a8448'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'face_front': LONG_FACE, 'hairline': [(16, 66), (18, 40), (36, 32), (50, 34), (64, 32), (82, 40), (84, 66)]},
    'front': [L(outline([(14, 74), (10, 30), (22, 6), (50, -4), (78, 6), (90, 30), (86, 74), (82, 66), (18, 66)])),
              L(outline([(60, 0), (82, 12), (90, 40), (84, 70), (78, 40)]), 'shade', 'b', False),
              strand([(30, 4), (36, 34)], 'shade', 'b', 1.0), strand([(50, -2), (50, 34)], 'shade', 'b', 1.0), strand([(70, 4), (64, 34)], 'shade', 'b', 1.0),
              L(outline([(14, 64), (20, 66), (22, 92), (16, 96, 1)]), 'mid', 'f'), L(outline([(86, 64), (80, 66), (78, 92), (84, 96, 1)]), 'mid', 'f')],
    'side': [L(outline([(44, 92), (40, 104), (24, 104, 1), (12, 80), (8, 30), (22, 6), (52, -4), (80, 4), (94, 24), (90, 40), (74, 40), (60, 46), (52, 62), (50, 80)])),
             L(outline([(10, 40), (36, 40), (44, 84), (26, 100), (12, 80)]), 'shade', 'b', False),
             L(outline([(52, 60), (58, 62), (60, 90), (54, 96, 1)]), 'mid', 'f')],
    'back': [L(outline([(14, 92), (10, 30), (22, 6), (50, -4), (78, 6), (90, 30), (86, 92), (74, 100, 1), (60, 92), (50, 98), (40, 92), (26, 100, 1)])),
             L(outline([(56, 0), (82, 12), (90, 44), (86, 90), (60, 94)]), 'shade', 'b', False), strand([(50, 0), (50, 94)], 'deep', 'b', 1.0)],
}
# Sirius Pounding: un casco de boxeo rojo que le tapa la cabeza, las orejas y la frente, con una franja blanca arriba; por
# encima asoma el pelo verde oliva; nariz naranja y la boca de enfado
CHARS['sirius-pounding'] = {
    'body': 'normal', 'pal': pal('#6a6a2a', '#fcc890', helm='#d02a1e', helm_d='#a01e14', nose='#e8963a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False, 'ears': False},
    'front': [L(outline([(30, 2), (50, -4), (70, 2), (62, 8), (38, 8)]), 'mid', 'b', ln=True),
              L(outline([(4, 106), (0, 40), (14, 8), (50, -2), (86, 8), (100, 40), (96, 106), (84, 104), (82, 70), (70, 64), (50, 66), (30, 64), (18, 70), (16, 104)]), 'helm', 'f', ln=True),
              L(outline([(60, 4), (86, 14), (98, 44), (94, 104), (84, 100), (82, 66), (70, 40)]), 'helm_d', 'f', False),
              L(outline([(38, 14), (62, 14), (62, 22), (38, 22)]), WHITE, 'f', ln=True),
              L(ell(50, 84, 5, 4), 'nose', 'f', ln=True)],
    'side': [L(blob(SIDE_SKULL), 'skin'),
             L(outline([(8, 100), (2, 40), (16, 8), (50, -4), (80, 4), (96, 24), (98, 60), (86, 70), (70, 60), (60, 70), (52, 104), (30, 106)]), 'helm', 'f', ln=True),
             L(outline([(26, 50), (44, 50), (46, 96), (28, 96)]), 'helm_d', 'f', ln=True), L(ell(92, 82, 4, 4), 'nose', 'f', ln=True)],
    'back': [L(outline([(4, 106), (0, 40), (14, 8), (50, -2), (86, 8), (100, 40), (96, 106), (50, 102)]), 'helm', 'f', ln=True),
             L(outline([(56, 2), (86, 14), (98, 44), (96, 104), (60, 100)]), 'helm_d', 'f', False),
             L(outline([(40, 0), (60, 0), (58, 8), (42, 8)]), 'mid', 'f', ln=True)],
}
