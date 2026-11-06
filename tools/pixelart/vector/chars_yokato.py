"""Yokato / Instituto Fauxshore (IE2): el equipo de los apostadores; pelos de pinchos, tupés, rastas, pañuelos y cintas
de festival, con sus modelos 3D como referencia (contornos calcados sobre una rejilla de unidades de cabeza)."""
from chars import CHARS, L, OUTC, blob, ell, messy, outline, pal, rope, spk, strand
from chars_alius import SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE, LONG_FACE
from heads import quad

DARK = (24, 22, 28, 255)
WHITE = (250, 250, 250, 255)


def bald(view):
    if view == 'front':
        return [L(blob(SKULL_F), 'skin'), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'skin_d', 'b', False)]
    if view == 'side':
        return [L(blob(SIDE_SKULL), 'skin')]
    return [L(blob(SKULL_B), 'skin'), L(blob([(58, 12), (86, 36), (84, 68), (66, 84)], 6), 'skin_d', 'b', False)]


def band(view, y0, y1, c='band', stripes=None, n=6):
    """Cinta alrededor de la cabeza entre las alturas y0 (arriba) e y1, curvada como la frente; con franjas verticales de
    otro color (de arriba abajo) si se piden."""
    x0, x1, bow = {'front': (8, 92, 6), 'side': (6, 94, 3), 'back': (6, 94, 4)}[view]
    sag = -bow if view == 'front' else bow * 0.5

    def y_at(y, x):
        t = (x - x0) / (x1 - x0)
        return y + sag * 4 * t * (1 - t)
    xs = [x0 + (x1 - x0) * k / 24 for k in range(25)]
    shape = [(x, y_at(y0, x)) for x in xs] + [(x, y_at(y1, x)) for x in xs[::-1]]
    out = [L(shape, c, 'f', ln=True)]
    if stripes:
        w = (x1 - x0) / (2 * n - 1)
        for k in range(n - 1):
            a, b = x0 + w * (2 * k + 1), x0 + w * (2 * k + 2)
            out.append(L([(a, y_at(y0, a)), (b, y_at(y0, b)), (b, y_at(y1, b)), (a, y_at(y1, a))], stripes, 'f', False))
        out.append(L(shape, OUTC, 'f', False, False, 1.0))
    return out


# Darren LaChance (portero): pelo castaño oliva despeinado y abultado de puntas cortas, con un flequillo de mechones que le
# cae hasta las cejas; ojos grandes grises y sonrisa
CHARS['darren-lachance'] = {
    'body': 'normal', 'pal': pal('#6a5a24', '#f8c088', iris='#4a4e5a'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': messy('front', 9, 11, seed=201, rx=52, ry=44, lo=70)
             + [L(outline([(12, 66, 1), (14, 40), (30, 26), (50, 22), (70, 26), (86, 40), (88, 66, 1), (80, 54), (72, 62, 1), (64, 52), (56, 62, 1), (50, 52),
                           (42, 62, 1), (36, 52), (28, 62, 1), (20, 54)]), 'mid', 'f'),
                L(outline([(58, 26), (80, 34), (88, 52), (80, 54), (70, 40)]), 'shade', 'f', False),
                L(ell(28, 86, 1, 1), 'skin_d', 'f', False), L(ell(72, 86, 1, 1), 'skin_d', 'f', False)],
    'side': messy('side', 10, 9, seed=201, rx=48, ry=44, nape=94, sweep=-0.2) + [spk((58, 30), (88, 40), (90, 62), 5, z='f', light_left=False)],
    'back': messy('back', 9, 11, seed=201, rx=52, ry=44, nape=96),
}
# Drancis Fake: media melena verde oliva clara en forma de casco con flequillo recto, y una cinta azul y rosa a rayas
# retorcida en la frente cuyo extremo sube enroscado por su izquierda; ojos rasgados negros y la boca seria
CHARS['drancis-fake'] = {
    'body': 'normal', 'pal': pal('#b8c078', '#fce4d0', iris='#141418', band='#2a6a9a', stripe='#f0c8c8'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(6, 98, 1), (10, 80), (8, 40), (20, 16), (50, 6), (80, 16), (92, 40), (90, 80), (94, 98, 1), (82, 86), (82, 64), (18, 64), (18, 86)])),
              L(outline([(60, 10), (86, 28), (92, 60), (90, 92), (82, 80), (80, 44)]), 'shade', 'b', False)]
             + band('front', 48, 58, stripes='stripe', n=7)
             + [L(outline([(14, 64), (16, 56), (84, 56), (86, 64), (78, 62), (76, 66, 1), (68, 62), (60, 66, 1), (52, 62), (44, 66, 1), (36, 62), (28, 66, 1), (20, 62)]), 'mid', 'f'),
                L(rope((88, 52), (100, 30), (94, 8), 7), 'band', 'f', ln=True), L(rope((90, 44), (98, 30), (94, 20), 3), 'stripe', 'f')],
    'side': [L(outline([(52, 94, 1), (44, 86), (20, 88), (8, 66), (8, 38), (22, 14), (50, 4), (78, 10), (92, 30), (92, 56), (78, 58), (60, 60), (54, 70)])),
             L(outline([(12, 44), (40, 52), (48, 84), (20, 86), (8, 64)]), 'shade', 'b', False)]
            + band('side', 44, 54, stripes='stripe'),
    'back': [L(outline([(12, 96), (6, 40), (20, 14), (50, 4), (80, 14), (94, 40), (88, 96), (50, 100)])),
             L(outline([(58, 8), (86, 28), (94, 60), (88, 94), (66, 98)]), 'shade', 'b', False),
             strand([(30, 58), (28, 96)], 'deep', 'b', 1.0), strand([(50, 58), (50, 100)], 'deep', 'b', 1.0), strand([(70, 58), (72, 96)], 'deep', 'b', 1.0)]
            + band('back', 40, 52, stripes='stripe', n=7) + [L(rope((10, 46), (0, 26), (6, 6), 7), 'band', 'f', ln=True)],
}
# Mick Mishap: piel morena y una mata enorme de pelo rubio de pinchos que se abren en todas direcciones, con mechones en
# punta sobre la frente; ojos medio cerrados de desgana
CHARS['mick-mishap'] = {
    'body': 'normal', 'pal': pal('#f4d880', '#9a7458', shade='#d8b860'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': messy('front', 22, 11, seed=202, rx=56, ry=46, lo=86)
             + [L(outline([(10, 70, 1), (14, 40), (30, 26), (50, 22), (70, 26), (86, 40), (90, 70, 1), (82, 56), (76, 64, 1), (66, 50), (58, 60, 1), (50, 48),
                           (42, 60, 1), (34, 50), (24, 64, 1), (18, 56)]), 'mid', 'f'),
                L(outline([(56, 28), (80, 36), (88, 54), (78, 54), (70, 40)]), 'shade', 'f', False)],
    'side': messy('side', 24, 9, seed=202, rx=52, ry=46, nape=96, sweep=-0.3) + [spk((58, 30), (90, 40), (96, 70), 5, z='f', light_left=False)],
    'back': messy('back', 22, 11, seed=202, rx=56, ry=46, nape=104),
}
# Louis Leave: piel tostada; pelo verde muy oscuro en un tupé plano y alto con pico en medio de la frente y las sienes
# rectas; cejas gruesas negras de enfado, orejas grandes y una sonrisa pícara
CHARS['louis-leave'] = {
    'body': 'normal', 'pal': pal('#163a1e', '#e0a050'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'big_ears': 2, 'ear_out': 4,
             'hairline': [(12, 66), (14, 40), (36, 40), (50, 52), (64, 40), (86, 40), (88, 66)]},
    'front': [L(outline([(12, 70), (10, 6), (24, -6), (76, -6), (90, 6), (88, 70), (82, 66), (18, 66)])),
              L(outline([(60, -4), (78, -4), (88, 10), (86, 62), (78, 40)]), 'shade', 'b', False)],
    'side': [L(outline([(44, 92), (22, 88), (10, 64), (10, 4), (24, -6), (80, -6), (94, 6), (88, 36), (76, 44), (64, 46), (54, 62), (50, 80)])),
             L(outline([(12, 30), (40, 40), (40, 86), (22, 86), (10, 60)]), 'shade', 'b', False)],
    'back': [L(outline([(12, 84), (10, 6), (24, -6), (76, -6), (90, 6), (88, 84), (50, 90)])),
             L(outline([(58, -4), (80, -4), (90, 10), (88, 80), (66, 86)]), 'shade', 'b', False)],
}
# Maurice Badgame: cara ancha y redonda morena, la cabeza rapada a los lados (gris) con una gorra plana azul marino arriba;
# ojos entornados, la boca enorme y marrón en forma de U y la nariz pequeña naranja
MAURICE_FACE = blob([(10, 40), (50, 34), (90, 40), (98, 74), (92, 104), (70, 116), (30, 116), (8, 104), (2, 74)])
CHARS['maurice-badgame'] = {
    'body': 'corpulento', 'pal': pal('#7a7672', '#a07a5a', cap='#1e2e5a', cap_d='#142046', mouth='#7a4a2a', nose='#e08a40'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': MAURICE_FACE, 'nose': (50, 78, 3), 'hairline': False, 'big_ears': 3, 'ear_out': 8},
    'front': [L(outline([(12, 42), (14, 10), (50, 4), (86, 10), (88, 42)]), 'mid', 'b'),
              L(outline([(14, 14), (50, 6), (86, 14), (86, 0), (50, -6), (14, 0)]), 'cap', 'f', ln=True),
              L(outline([(60, -4), (86, 0), (86, 12), (62, 8)]), 'cap_d', 'f', False),
              L([(24, 68), (42, 70)], OUTC, 'f', False, False, 2.6), L([(76, 68), (58, 70)], OUTC, 'f', False, False, 2.6),
              L([(30, 64), (40, 62)], OUTC, 'f', False, False, 1.4), L([(70, 64), (60, 62)], OUTC, 'f', False, False, 1.4),
              L(outline([(22, 86), (50, 82), (78, 86), (80, 104), (64, 114), (36, 114), (20, 104)]), 'mouth', 'f', ln=True),
              L([(36, 104), (64, 104)], OUTC, 'f', False, False, 1.4)],
    'side': [L(outline([(20, 100), (8, 70), (10, 10), (50, 2), (80, 8), (94, 44), (98, 80), (92, 108), (60, 116), (36, 112)]), 'skin'),
             L(outline([(10, 14), (48, 8), (80, 10), (84, 40), (56, 44), (30, 60), (10, 62)]), 'mid', 'b'),
             L(outline([(12, 40), (40, 50), (48, 96), (28, 108), (10, 80)]), 'skin_d', 'b', False),
             L(outline([(10, 14), (50, 6), (82, 12), (82, 0), (50, -6), (10, 0)]), 'cap', 'f', ln=True),
             L(outline([(82, 84), (98, 84), (96, 106), (84, 108)]), 'mouth', 'f', ln=True), L([(78, 68), (90, 70)], OUTC, 'f', False, False, 2.4)],
    'back': [L(outline([(10, 96), (8, 10), (50, 4), (92, 10), (90, 96), (50, 104)]), 'mid'),
             L(outline([(54, 30), (90, 30), (90, 92), (60, 100)]), (90, 72, 64, 255), 'b', False),
             L(outline([(10, 14), (50, 6), (90, 14), (90, 0), (50, -6), (10, 0)]), 'cap', 'f', ln=True)],
}
# Dany Destiny: calvo y de piel morena clara, con una cinta crema gruesa y retorcida como una cuerda alrededor de la cabeza,
# anudada arriba a su izquierda; ojos de sueño y la boca en una raya
CHARS['dany-destiny'] = {
    'body': 'normal', 'pal': pal('#e8dcc0', '#d8a070', shade='#c0aa8a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': bald('front')
             + [L(quad((6, 36), (50, 22), (94, 36)) + quad((94, 36), (50, 26), (6, 36))[1:], 'shade', 'f', False, False, 13)]
             + [L(ell(12 + k * 12.6, 35 - 9 * (1 - ((12 + k * 12.6 - 50) / 44) ** 2), 7.6, 5.6), 'mid', 'f') for k in range(7)]
             + [L(outline([(70, 26), (78, 10), (90, 6, 1), (88, 18), (96, 22, 1), (84, 30)]), 'mid', 'f', ln=True)],
    'side': bald('side') + [L([(8, 36), (90, 26)], 'shade', 'f', False, False, 13)] + [L(ell(12 + k * 15.6, 35 - k * 1.8, 8, 5.6), 'mid', 'f') for k in range(6)],
    'back': bald('back') + [L(quad((6, 36), (50, 28), (94, 36)), 'shade', 'f', False, False, 13)]
            + [L(ell(10 + k * 13.3, 35 - 5 * (1 - ((10 + k * 13.3 - 50) / 44) ** 2), 7.6, 5.6), 'mid', 'f') for k in range(7)]
            + [L(outline([(26, 26), (18, 10), (6, 6, 1), (10, 18), (2, 22, 1), (14, 30)]), 'mid', 'f', ln=True)],
}
# Cannon Random: tupé rojo enorme y redondo que tapa toda la cabeza y se alarga muy hacia atrás como un casco; ojos de
# enfado y orejas grandes
CHARS['cannon-random'] = {
    'body': 'normal', 'pal': pal('#c8201a', '#fcc890'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'big_ears': 2, 'ear_out': 4, 'hairline': (62, 60)},
    'front': [L(outline([(10, 68), (6, 30), (16, 6), (50, -4), (84, 6), (94, 30), (90, 68), (80, 62), (20, 62)])),
              L(outline([(60, -2), (86, 8), (94, 34), (88, 62), (78, 40)]), 'shade', 'b', False),
              strand([(26, 12), (24, 52)], 'shade', 'b', 1.0), strand([(74, 12), (76, 52)], 'deep', 'b', 1.0), strand([(28, 12), (72, 12)], 'shade', 'b', 1.0)],
    'side': [L(outline([(44, 92), (22, 88), (10, 66), (8, 30), (-6, 20), (-18, 8), (-16, -8), (0, -12), (40, -6), (70, 0), (90, 16), (96, 40), (86, 56),
                        (66, 56), (54, 64), (50, 80)])),
             L(outline([(-14, 0), (10, 10), (30, 30), (40, 60), (20, 80), (8, 50)]), 'shade', 'b', False),
             strand([(40, -4), (44, 50)], 'deep', 'b', 1.2)],
    'back': [L(outline([(10, 76), (6, 30), (16, 6), (50, -4), (84, 6), (94, 30), (90, 76), (50, 84)])),
             L(outline([(36, 50), (64, 50), (68, 78), (32, 78)]), 'deep', 'b', False),
             L(outline([(60, -2), (86, 8), (94, 34), (88, 74), (70, 80)]), 'shade', 'b', False)],
}
# Ulric Richmen: piel morena, rastas negras gruesas que salen de la coronilla y caen hacia fuera hasta la barbilla; unas
# gafas de sol negras envolventes con el borde amarillo, nariz larga y labios gruesos
DREADS_F = [((22, 30), (4, 50), (-8, 70)), ((18, 46), (0, 70), (-6, 90)), ((26, 20), (8, 30), (-10, 40)), ((78, 30), (96, 50), (108, 70)),
            ((82, 46), (100, 70), (106, 90)), ((74, 20), (92, 30), (110, 40))]
CHARS['ulric-richmen'] = {
    'body': 'normal', 'pal': pal('#1e1a1a', '#8a5a3a', lens='#141414', rim='#e8d020', lip='#5a3020'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': LONG_FACE, 'hairline': (50, 44)},
    'front': [L(rope(a, c, b, 9), 'mid', 'b', ln=True) for a, c, b in DREADS_F]
             + [L(outline([(16, 54), (14, 28), (30, 10), (50, 6), (70, 10), (86, 28), (84, 54), (50, 46)])),
                L(outline([(10, 70), (50, 66), (90, 70), (88, 80), (58, 82), (50, 76), (42, 82), (12, 80)]), 'lens', 'f', ln=True),
                L(quad((12, 70), (50, 64), (88, 70)), 'rim', 'f', False, False, 1.4), L([(44, 72), (50, 68), (56, 72)], 'rim', 'f', False, False, 1.2),
                L([(50, 80), (50, 92)], 'skin_d', 'f', False, False, 1.6),
                L(outline([(40, 100), (50, 96), (60, 100), (56, 106), (44, 106)]), 'lip', 'f', ln=True)],
    'side': [L(outline([(44, 94), (22, 90), (10, 66), (12, 36), (28, 14), (54, 6), (78, 14), (88, 32), (74, 40), (60, 44), (52, 62), (50, 80)]), 'skin'),
             L(outline([(14, 36), (28, 12), (54, 4), (76, 10), (84, 26), (60, 30), (40, 40), (20, 56)]))]
            + [L(rope((x, 24), (x - 18, 50 + k * 4), (x - 22, 80 + k * 6), 9), 'mid', 'b', ln=True) for k, x in enumerate((30, 44, 58))]
            + [L(outline([(70, 66), (94, 66), (94, 78), (72, 78)]), 'lens', 'f', ln=True), L([(48, 70), (70, 70)], 'lens', 'f', False, False, 1.6),
               L(outline([(86, 98), (96, 98), (96, 106), (86, 106)]), 'lip', 'f', ln=True)],
    'back': [L(outline([(16, 60), (14, 28), (30, 10), (50, 6), (70, 10), (86, 28), (84, 60), (50, 66)]))]
            + [L(rope((x, 20 + abs(x - 50) * 0.2), (x + (x - 50) * 0.5, 56), (x + (x - 50) * 0.8, 92 - abs(x - 50) * 0.3), 9), 'mid', 'b', ln=True)
               for x in (16, 30, 44, 56, 70, 84)],
}
# Spencer Duskplay: un pañuelo azul marino enrollado muy alto como un cubo que le tapa la frente hasta las cejas, con las
# puntas rubias de pinchos asomando por arriba; piel morena, ojos rojos y la boca seria
CHARS['spencer-duskplay'] = {
    'body': 'normal', 'pal': pal('#f0dca0', '#a07050', iris='#c82a1a', cloth='#1e3a5a', cloth_d='#142a44'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(20, 6), (24, -16, 1), (32, -4), (40, -22, 1), (48, -6), (56, -24, 1), (62, -6), (70, -18, 1), (76, 6)])),
              L(outline([(10, 66), (8, 10), (50, 2), (92, 10), (90, 66), (50, 62)]), 'cloth', 'f', ln=True),
              L(outline([(58, 4), (92, 10), (90, 64), (70, 62), (66, 30)]), 'cloth_d', 'f', False),
              L(quad((10, 56), (50, 52), (90, 56)), 'cloth_d', 'f', False, False, 1.4), L(quad((10, 60), (50, 56), (90, 60)), 'cloth_d', 'f', False, False, 1.0)],
    'side': [L(blob(SIDE_SKULL), 'skin'),
             L(outline([(20, 4), (24, -16, 1), (34, -4), (44, -20, 1), (52, -4), (62, -18, 1), (70, 2)])),
             L(outline([(4, 64), (2, 8), (50, 0), (94, 6), (94, 58), (60, 60)]), 'cloth', 'f', ln=True),
             L(outline([(4, 20), (30, 30), (30, 62), (4, 64)]), 'cloth_d', 'f', False)],
    'back': [L(blob(SKULL_B), 'skin'), L(blob([(58, 12), (86, 36), (84, 68), (66, 84)], 6), 'skin_d', 'b', False),
             L(outline([(22, 6), (26, -14, 1), (34, -2), (44, -20, 1), (52, -4), (60, -18, 1), (68, -2), (76, -12, 1), (80, 6)])),
             L(outline([(8, 66), (8, 10), (50, 2), (92, 10), (92, 66), (50, 62)]), 'cloth', 'f', ln=True),
             L(outline([(56, 4), (92, 10), (92, 64), (64, 62)]), 'cloth_d', 'f', False)],
}
# Dave Fate: cara redonda y ancha; el pelo gris rapado muy corto en forma de casquete, con una cinta roja y blanca retorcida
# anudada a un lado; ojos de enfado, nariz chata y la boca abierta gritando
CHARS['dave-fate'] = {
    'body': 'corpulento', 'pal': pal('#a8aab4', '#fcc070', band='#d02a2a', stripe='#f0e8d8', nose='#f4b060', tongue='#f08080'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'none', 'face_front': WIDE_FACE, 'nose': (50, 80, 3.6), 'hairline': False, 'big_ears': 3, 'ear_out': 8},
    'front': [L(outline([(12, 50), (12, 22), (26, 4), (50, -2), (74, 4), (88, 22), (88, 50)]), 'mid', 'b'),
              L(outline([(60, 0), (82, 12), (88, 40), (76, 36)]), 'shade', 'b', False)]
             + band('front', 44, 52, stripes='stripe', n=7)
             + [L(rope((84, 44), (92, 34), (88, 22), 5), 'band', 'f', ln=True), L(rope((86, 46), (98, 40), (98, 26), 5), 'stripe', 'f', ln=True),
                L(outline([(34, 92), (50, 88), (66, 92), (64, 104), (50, 108), (36, 104)]), (120, 30, 30, 255), 'f', ln=True),
                L(outline([(36, 92), (50, 89), (64, 92), (62, 96), (38, 96)]), WHITE, 'f', False),
                L(outline([(40, 102), (50, 100), (60, 102), (50, 106)]), 'tongue', 'f', False)],
    'side': [L(outline([(10, 56), (8, 22), (24, 4), (52, -2), (76, 6), (88, 24), (88, 44), (60, 50), (30, 60)]), 'mid', 'b')]
            + band('side', 40, 48, stripes='stripe')
            + [L(outline([(84, 90), (96, 88), (96, 100), (86, 102)]), (120, 30, 30, 255), 'f', ln=True)],
    'back': [L(outline([(10, 74), (10, 22), (24, 4), (50, -2), (76, 4), (90, 22), (90, 74), (50, 80)]), 'mid'),
             L(outline([(58, 0), (84, 14), (90, 40), (90, 72), (70, 76)]), 'shade', 'b', False)]
            + [L(ell(x, y, 0.8, 0.8), 'shade', 'b', False) for x, y in ((30, 20), (40, 12), (60, 14), (70, 22), (50, 28))]
            + band('back', 42, 50, stripes='stripe', n=7)
            + [L(rope((14, 44), (6, 32), (12, 20), 5), 'band', 'f', ln=True), L(rope((12, 46), (0, 40), (2, 26), 5), 'stripe', 'f', ln=True)],
}
# Jonathan Luckyman: un pañuelo morado oscuro que le cubre toda la cabeza, anudado en la nuca con dos puntas que caen; por
# debajo asoma el pelo verde azulado en las patillas y la nuca; ojos marrones y la boca seria
CHARS['jonathan-luckyman'] = {
    'body': 'normal', 'pal': pal('#1e6a6a', '#fcd0a0', iris='#8a5a1e', cloth='#4a323e', cloth_d='#36242e'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 80), (10, 50), (90, 50), (88, 80), (80, 72), (20, 72)])),
              L(outline([(10, 80), (2, 90), (8, 96), (20, 86)]), 'cloth', 'b', ln=True), L(outline([(90, 80), (98, 90), (92, 96), (80, 86)]), 'cloth', 'b', ln=True),
              L(outline([(10, 62), (8, 30), (20, 10), (50, 2), (80, 10), (92, 30), (90, 62), (70, 56), (50, 58), (30, 56)]), 'cloth', 'f', ln=True),
              L(outline([(60, 6), (82, 16), (92, 40), (88, 60), (74, 54)]), 'cloth_d', 'f', False),
              L(quad((14, 40), (50, 30), (86, 40)), 'cloth_d', 'f', False, False, 1.4)],
    'side': [L(outline([(44, 92), (22, 88), (12, 66), (14, 50), (50, 50), (52, 62), (50, 80)])),
             L(outline([(4, 58), (6, 24), (24, 6), (54, 0), (78, 8), (92, 28), (90, 50), (60, 50), (40, 58), (20, 64)]), 'cloth', 'f', ln=True),
             L(outline([(14, 50), (2, 74), (6, 94, 1), (16, 74), (24, 56)]), 'cloth', 'f', ln=True)],
    'back': [L(outline([(12, 84), (10, 56), (90, 56), (88, 84), (50, 90)])),
             L(outline([(8, 66), (8, 30), (20, 8), (50, 0), (80, 8), (92, 30), (92, 66), (50, 62)]), 'cloth', 'f', ln=True),
             L(outline([(58, 4), (84, 16), (92, 40), (92, 64), (66, 62)]), 'cloth_d', 'f', False),
             L(ell(50, 66, 8, 6), 'cloth', 'f', ln=True),
             L(outline([(44, 68), (30, 86), (34, 100, 1), (46, 84), (50, 72)]), 'cloth', 'f', ln=True),
             L(outline([(56, 68), (70, 86), (66, 100, 1), (54, 84), (50, 72)]), 'cloth', 'f', ln=True)],
}
# Joe Poker: pelo verde oliva de pinchos grandes en todas direcciones, con un lazo rosado palo atado en la frente; ojos
# naranjas de pillo y una sonrisa de dientes
CHARS['joe-poker'] = {
    'body': 'normal', 'pal': pal('#5a5a1e', '#fcc080', iris='#d0601a', bow='#d8b0a8', bow_d='#b08a80'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'grin', 'mouth_y': 95, 'hairline': False},
    'front': messy('front', 24, 10, seed=203, rx=54, ry=46, lo=78)
             + [L(outline([(10, 70, 1), (14, 44), (30, 30), (50, 26), (70, 30), (86, 44), (90, 70, 1), (82, 58), (18, 58)]), 'mid', 'f'),
                L(outline([(14, 58), (50, 52), (86, 58), (86, 66), (50, 60), (14, 66)]), 'bow', 'f', ln=True),
                L(outline([(50, 54), (36, 42), (34, 54), (40, 62)]), 'bow', 'f', ln=True), L(outline([(50, 54), (64, 42), (66, 54), (60, 62)]), 'bow', 'f', ln=True),
                L(ell(50, 56, 4, 4), 'bow_d', 'f', ln=True)],
    'side': messy('side', 26, 9, seed=203, rx=50, ry=46, nape=100, sweep=-0.4)
            + [L(outline([(60, 50), (92, 54), (92, 62), (60, 58)]), 'bow', 'f', ln=True), L(outline([(66, 52), (56, 40), (54, 50)]), 'bow', 'f', ln=True)],
    'back': messy('back', 24, 10, seed=203, rx=54, ry=46, nape=102),
}
# Wiley Cracker (portero): pelo corto gris oliva, peinado en un casquete; cara alargada, ojos redondos de enfado, nariz
# larga y una sonrisa de medio lado
CHARS['wiley-cracker'] = {
    'body': 'normal', 'pal': pal('#8a8a6a', '#f8c088'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'face_front': LONG_FACE, 'nose': (50, 86, 3),
             'hairline': (52, 44), 'big_ears': 1, 'ear_out': 3},
    'front': [L(outline([(16, 58), (14, 26), (28, 6), (50, 0), (72, 6), (86, 26), (84, 58), (70, 46), (30, 46)])),
              L(outline([(60, 4), (80, 14), (86, 40), (78, 50), (72, 30)]), 'shade', 'b', False)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (12, 30), (26, 8), (54, 0), (78, 8), (88, 26), (80, 36), (62, 40), (52, 60), (50, 80)])),
             L(outline([(14, 40), (30, 30), (44, 60), (40, 86), (22, 86), (12, 64)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 84), (12, 30), (26, 6), (50, 0), (74, 6), (88, 30), (84, 84), (60, 90), (50, 80), (40, 90)])),
             L(outline([(56, 4), (82, 18), (88, 50), (84, 82), (62, 88)]), 'shade', 'b', False)],
}
# Mark Failing: pelo castaño rojizo con raya en medio, liso y pegado, que se abre en dos puntas hacia fuera a la altura de la
# barbilla y le baja en patillas gruesas hasta las mejillas; cejas gruesas de enfado
CHARS['mark-failing'] = {
    'body': 'normal', 'pal': pal('#8a3a14', '#fcc8a0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': [(16, 70), (18, 46), (30, 38), (50, 36), (70, 38), (82, 46), (84, 70)]},
    'front': [L(outline([(-8, 100, 1), (8, 84), (8, 40), (20, 14), (50, 4), (80, 14), (92, 40), (92, 84), (108, 100, 1), (84, 96), (80, 66), (20, 66), (16, 96)])),
              L(outline([(60, 8), (86, 26), (92, 60), (92, 90), (84, 92), (80, 50)]), 'shade', 'b', False),
              strand([(50, 6), (50, 36)], 'deep', 'b', 1.2), strand([(38, 10), (28, 36)], 'deep', 'b', 1.0), strand([(62, 10), (72, 36)], 'deep', 'b', 1.0),
              L(outline([(17, 62), (23, 64), (24, 80), (30, 88, 1), (20, 86), (17, 74)]), 'mid', 'f'),
              L(outline([(83, 62), (77, 64), (76, 80), (70, 88, 1), (80, 86), (83, 74)]), 'mid', 'f')],
    'side': [L(outline([(54, 70), (52, 92), (40, 98), (22, 104, 1), (16, 96), (6, 76), (6, 40), (20, 14), (50, 2), (76, 8), (90, 26), (86, 40), (74, 44), (62, 48)])),
             L(outline([(10, 50), (30, 50), (44, 76), (40, 96), (20, 100), (8, 84)]), 'shade', 'b', False),
             L(outline([(62, 60), (74, 62), (80, 86), (72, 92), (64, 80)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(-8, 104, 1), (8, 86), (8, 40), (20, 14), (50, 4), (80, 14), (92, 40), (92, 86), (108, 104, 1), (80, 98), (50, 100), (20, 98)])),
             L(outline([(58, 8), (88, 30), (94, 80), (96, 98), (70, 96), (66, 60)]), 'shade', 'b', False)],
}
# Alton Cotts: pelo azul marino en un tupé altísimo y plano por arriba, con un pico muy marcado en la frente y patillas en
# punta; cejas gruesas azul marino de enfado y la boca seria
CHARS['alton-cotts'] = {
    'body': 'normal', 'pal': pal('#2a3a6a', '#f8b880'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 98, 'face_front': LONG_FACE, 'nose': (50, 88, 2.6),
             'hairline': [(12, 74), (14, 50), (30, 52), (50, 70), (70, 52), (86, 50), (88, 74)]},
    'front': [L(outline([(12, 80), (4, 30), (2, -18), (50, -24), (98, -18), (96, 30), (88, 80), (82, 74), (18, 74)])),
              L(outline([(62, -22), (98, -18), (96, 30), (86, 74), (78, 30)]), 'shade', 'b', False),
              strand([(40, -20), (44, 30)], 'deep', 'b', 1.0), strand([(60, -20), (58, 30)], 'deep', 'b', 1.0),
              L(outline([(20, 72), (30, 66), (44, 74), (44, 78), (30, 74), (22, 76)]), 'mid', 'f', ln=True),
              L(outline([(80, 72), (70, 66), (56, 74), (56, 78), (70, 74), (78, 76)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(44, 92), (22, 88), (10, 64), (8, -16), (60, -22), (96, -18), (92, 30), (80, 44), (64, 50), (54, 62), (50, 80)])),
             L(outline([(10, 20), (40, 30), (44, 86), (22, 86), (10, 60)]), 'shade', 'b', False),
             L(outline([(70, 66), (84, 64), (86, 70), (72, 72)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(12, 86), (4, 30), (2, -18), (50, -24), (98, -18), (96, 30), (88, 86), (50, 92)])),
             L(outline([(60, -22), (98, -18), (96, 30), (88, 84), (64, 90)]), 'shade', 'b', False)],
}
# Mike Passing: pelo gris arena en forma de casco con un flequillo de mechones en punta hasta las cejas y las puntas
# abiertas en las patillas; cara de enfado
CHARS['mike-passing'] = {
    'body': 'normal', 'pal': pal('#c8c0a0', '#e8a868', shade='#a0927a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 70), (6, 36), (18, 12), (50, 2), (82, 12), (94, 36), (90, 70), (80, 64), (20, 64)])),
              L(outline([(60, 6), (86, 22), (94, 50), (88, 66), (78, 40)]), 'shade', 'b', False),
              L(outline([(10, 70, 1), (14, 40), (30, 26), (50, 22), (70, 26), (86, 40), (90, 70, 1), (80, 58), (72, 66, 1), (62, 54), (54, 64, 1), (48, 54),
                         (40, 66, 1), (32, 54), (22, 68, 1), (18, 58)]), 'mid', 'f'),
              L(outline([(54, 26), (78, 32), (88, 50), (80, 58), (68, 40)]), 'shade', 'f', False)],
    'side': [L(outline([(44, 92), (22, 90), (8, 66), (8, 34), (22, 10), (52, 2), (78, 10), (92, 30), (92, 48), (78, 46), (64, 48), (54, 62), (50, 80)])),
             L(outline([(10, 40), (36, 40), (44, 80), (24, 88), (8, 66)]), 'shade', 'b', False),
             spk((60, 28), (90, 40), (92, 66), 5, z='f', light_left=False)],
    'back': [L(outline([(10, 84), (6, 36), (18, 12), (50, 2), (82, 12), (94, 36), (90, 84), (50, 90)])),
             L(outline([(20, 50), (40, 40), (60, 44), (80, 40), (90, 60), (88, 84), (50, 90), (12, 84)]), 'shade', 'b', False)],
}
# Knowle Bathers (portero suplente): pelo castaño anaranjado de pinchos altos hacia arriba y una cinta ancha a rayas azul
# marino y blanco en la frente; ojos de enfado y la boca seria
CHARS['knowle-bathers'] = {
    'body': 'normal', 'pal': pal('#c06a1a', '#f8c088', band='#1e4a8a', stripe='#f0ece0'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(12, 66), (8, 36), (2, 22, 1), (14, 20), (12, 0, 1), (26, 8), (28, -14, 1), (40, 0), (48, -24, 1), (56, -2), (68, -16, 1), (70, 4),
                         (88, -2, 1), (84, 16), (98, 20, 1), (90, 36), (88, 66)])),
              L(outline([(56, -2), (68, -16, 1), (70, 4), (88, -2, 1), (84, 16), (90, 40), (86, 60), (74, 30)]), 'shade', 'b', False),
              strand([(36, 10), (40, 44)], 'deep', 'b', 1.0), strand([(56, 4), (58, 44)], 'deep', 'b', 1.0)]
             + band('front', 46, 66, stripes='stripe', n=5),
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (12, 36), (4, 22, 1), (18, 22), (16, 2, 1), (32, 10), (38, -14, 1), (50, 4), (64, -12, 1), (68, 8),
                        (84, 6, 1), (82, 22), (90, 34), (76, 42), (60, 46), (52, 62), (50, 80)])),
             L(outline([(14, 46), (20, 76), (38, 88), (28, 60)]), 'shade', 'b', False)]
            + band('side', 42, 62, stripes='stripe', n=5),
    'back': [L(outline([(12, 82), (8, 36), (2, 22, 1), (14, 20), (12, 0, 1), (26, 8), (30, -12, 1), (42, 2), (50, -22, 1), (58, 0), (70, -14, 1), (72, 6),
                        (88, 0, 1), (84, 18), (98, 22, 1), (90, 36), (88, 82), (50, 88)])),
             L(outline([(58, 0), (84, 18), (90, 50), (86, 80), (64, 86)]), 'shade', 'b', False)]
            + band('back', 44, 64, stripes='stripe', n=5),
}
