"""Brockenborg / Brocken Brigade (IE3, Alemania): máscara de gas, casco de pincho, parche, cintas y trenzas, con sus
modelos 3D como referencia (contornos calcados sobre una rejilla de unidades de cabeza)."""
from chars import CHARS, L, OUTC, blob, ell, longhair, messy, outline, pal, rope, spk, strand
from chars_alius import LONG_FACE, SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE
from chars_bigwaves import bald, rect_glasses, side_eye, white_eyes
from chars_orpheus import headband
from chars_unicorn import buzz
from heads import quad

WHITE = (250, 250, 250, 255)


def round_glasses(view, y=76, c=(30, 30, 30, 255), r=7.5):
    if view == 'front':
        return [L(ell(34, y, r, r * 0.9) + [ell(34, y, r, r * 0.9)[0]], c, 'f', False, False, 1.6), L(ell(66, y, r, r * 0.9) + [ell(66, y, r, r * 0.9)[0]], c, 'f', False, False, 1.6),
                L([(41, y - 1), (59, y - 1)], c, 'f', False, False, 1.4)]
    if view == 'side':
        return [L(ell(86, y, 3.4, r * 0.9) + [ell(86, y, 3.4, r * 0.9)[0]], c, 'f', False, False, 1.6), L([(50, y - 2), (82, y - 1)], c, 'f', False, False, 1.4)]
    return []


# Thorsten Welger (portero): una máscara de gas negra con un gran visor redondo verde y el filtro gris, y por encima el pelo
# castaño claro de pinchos que se abre a los lados
CHARS['thorsten-welger'] = {
    'body': 'normal', 'pal': pal('#9a7a50', '#f0b880', shade='#7a5c3a', gas='#2e2e2a', rim='#8a8a80', lens='#4a7a2a', filt='#a0a094'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False, 'ears': False},
    'front': [L(outline([(10, 54), (-8, 40, 1), (4, 26), (-2, 6, 1), (20, 8), (36, -4), (50, 4), (64, -4), (80, 8), (102, 6, 1), (96, 26), (108, 40, 1), (90, 54)])),
              L(outline([(8, 104), (6, 50), (18, 30), (50, 22), (82, 30), (94, 50), (92, 104), (70, 116), (30, 116)]), 'gas', 'f', ln=True),
              L(ell(50, 70, 26, 24), 'rim', 'f', ln=True), L(ell(50, 70, 21, 19), 'lens', 'f', False), L(ell(42, 62, 6, 3), (120, 170, 80, 255), 'f', False),
              L(outline([(34, 98), (66, 98), (64, 116), (36, 116)]), 'filt', 'f', ln=True), L([(36, 104), (64, 104)], 'gas', 'f', False, False, 1.2),
              L([(36, 110), (64, 110)], 'gas', 'f', False, False, 1.2),
              L(outline([(2, 64), (10, 60), (10, 84), (2, 82)]), 'gas', 'f', ln=True), L(outline([(98, 64), (90, 60), (90, 84), (98, 82)]), 'gas', 'f', ln=True)],
    'side': [L(outline([(30, 30), (16, 10), (24, -6, 1), (40, 6), (56, -4), (70, 4), (84, -2, 1), (82, 14), (70, 20)])),
             L(outline([(12, 96), (8, 40), (24, 16), (54, 8), (80, 16), (92, 40), (94, 100), (60, 104)]), 'gas', 'f', ln=True),
             L(outline([(84, 52), (100, 54), (102, 84), (86, 86)]), 'rim', 'f', ln=True), L(outline([(88, 56), (98, 58), (98, 82), (88, 82)]), 'lens', 'f', False),
             L(outline([(80, 94), (104, 96), (106, 112), (82, 112)]), 'filt', 'f', ln=True), L(ell(38, 64, 8, 8), 'filt', 'f', ln=True)],
    'back': [L(outline([(8, 70), (-6, 40, 1), (4, 26), (-2, 6, 1), (20, 8), (36, -4), (50, 4), (64, -4), (80, 8), (102, 6, 1), (96, 26), (106, 40, 1), (92, 70), (50, 80)])),
             L(outline([(56, 4), (82, 10), (98, 30), (92, 66), (66, 76)]), 'shade', 'b', False),
             L(outline([(44, 0), (56, 0), (56, 84), (44, 84)]), 'gas', 'f', ln=True), L(quad((4, 70), (50, 82), (96, 70)), 'gas', 'f', False, False, 4),
             L(outline([(40, 70), (60, 70), (60, 80), (40, 80)]), 'rim', 'f', ln=True)],
}
# Alexander Hausen: pelo rubio verdoso de mechones largos y despeinados, con un flequillo que le cae por la frente y dos
# mechones gruesos que le bajan por delante de las orejas hasta el cuello; ojos azules de enfado
CHARS['alexander-hausen'] = {
    'body': 'normal', 'pal': pal('#a8a048', '#fcd0a8', iris='#2a6ac8', shade='#86802e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': messy('front', 6, 10, seed=1401, rx=52, ry=44, cy=40, lo=70)
             + [L(outline([(10, 70, 1), (14, 42), (30, 24), (54, 18), (76, 24), (90, 40), (104, 34, 1), (92, 54), (86, 62), (74, 48), (60, 46), (50, 58), (40, 72, 1), (34, 54), (22, 60)]), 'mid', 'f', ln=True),
                L(rope((16, 66), (8, 90), (18, 110), 10), 'mid', 'f', ln=True), L(rope((84, 66), (92, 90), (82, 110), 10), 'mid', 'f', ln=True)],
    'side': messy('side', 7, 9, seed=1401, rx=48, ry=44, cy=40, nape=94, sweep=-0.2) + [L(rope((58, 60), (66, 90), (58, 110), 10), 'mid', 'f', ln=True)],
    'back': messy('back', 6, 10, seed=1401, rx=52, ry=44, cy=40, nape=96),
}
# Heinrich Farber: cabeza alta y alargada, rapada con el pelo rubio ceniza muy corto; cejas rubias rectas, ojos azules de
# sueño, nariz larga y la boca en una raya
CHARS['heinrich-farber'] = {
    'body': 'corpulento', 'pal': pal('#c0b888', '#f8c09a', iris='#3a8ab8', shade='#9a926a', nose='#e8a888'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 104, 'face_front': LONG_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 7},
    'front': bald('front') + [L(outline([(16, 76), (14, 20), (26, 2), (50, -4), (74, 2), (86, 20), (84, 76), (78, 50), (78, 20), (22, 20), (22, 50)]), 'mid', 'f')]
             + [L(outline([(22, 66), (44, 66), (44, 70), (22, 70)]), 'mid', 'f', ln=True), L(outline([(78, 66), (56, 66), (56, 70), (78, 70)]), 'mid', 'f', ln=True)]
             + white_eyes(76, 16, 6, 4.6, 2.6, lid=2) + [L(outline([(44, 74), (56, 74), (56, 96), (44, 96)]), 'nose', 'f', ln=True)],
    'side': bald('side') + buzz('side') + side_eye(76, lid=2) + [L(outline([(86, 74), (98, 90), (88, 94)]), 'nose', 'f', ln=True)],
    'back': bald('back') + buzz('back', nape=76),
}
# Kurt Zawel: gordo de cara enorme y pálida; pelo castaño oliva despeinado de mechones con barba de pocos días; ojos de
# enfado, nariz redonda naranja y los dientes apretados
CHARS['kurt-zawel'] = {
    'body': 'corpulento', 'pal': pal('#8a6a2e', '#fce0b0', shade='#6a4e1e', nose='#f0a060', stubble='#c0a068'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 9},
    'front': messy('front', 4, 13, seed=1402, rx=54, ry=44, cy=38, lo=62)
             + [L(outline([(10, 62, 1), (14, 40), (30, 24), (50, 20), (70, 24), (86, 40), (90, 62, 1), (78, 50), (68, 56, 1), (60, 46), (50, 54, 1), (40, 46), (32, 56, 1), (22, 50)]), 'mid', 'f'),
                L(outline([(10, 80), (20, 104), (40, 118), (60, 118), (80, 104), (90, 80), (82, 100), (60, 110), (40, 110), (18, 100)]), 'stubble', 'f', False),
                L(outline([(22, 70), (40, 72), (38, 78), (26, 76)]), WHITE, 'f', ln=True), L(outline([(78, 70), (60, 72), (62, 78), (74, 76)]), WHITE, 'f', ln=True),
                L([(22, 68), (42, 72)], OUTC, 'f', False, False, 2.4), L([(78, 68), (58, 72)], OUTC, 'f', False, False, 2.4),
                L(ell(50, 84, 7, 5), 'nose', 'f', ln=True),
                L(outline([(30, 98), (70, 98), (66, 106), (34, 106)]), WHITE, 'f', ln=True), L([(32, 102), (68, 102)], OUTC, 'f', False, False, 1.0)],
    'side': messy('side', 5, 11, seed=1402, rx=50, ry=44, cy=38, nape=88) + side_eye(74) + [L(ell(94, 84, 6, 5), 'nose', 'f', ln=True)],
    'back': messy('back', 4, 13, seed=1402, rx=54, ry=44, cy=38, nape=90),
}
# Lukas Schmidt: un casco prusiano plateado con un pincho en lo alto y dos franjas en la frente, calado hasta los ojos; por
# los lados asoma el pelo rubio; ojos azules de enfado
CHARS['lukas-schmidt'] = {
    'body': 'normal', 'pal': pal('#e0c070', '#fcd8b8', iris='#3a7ab8', helm='#d8d4e0', helm_d='#a89eb0'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin'), L(outline([(14, 62), (20, 62), (22, 86), (16, 88)]), 'mid', 'b', ln=True), L(outline([(86, 62), (80, 62), (78, 86), (84, 88)]), 'mid', 'b', ln=True),
              L(outline([(46, -4), (50, -24, 1), (54, -4)]), 'helm', 'f', ln=True),
              L(outline([(4, 66), (8, 58), (10, 26), (24, 4), (50, -4), (76, 4), (90, 26), (92, 58), (96, 66), (50, 62)]), 'helm', 'f', ln=True),
              L(outline([(60, 0), (82, 12), (90, 36), (90, 58), (74, 56)]), 'helm_d', 'f', False),
              L(quad((10, 42), (50, 32), (90, 42)), 'helm_d', 'f', False, False, 1.6), L(quad((10, 50), (50, 40), (90, 50)), 'helm_d', 'f', False, False, 1.6)],
    'side': [L(blob(SIDE_SKULL), 'skin'),
             L(outline([(48, -6), (54, -26, 1), (60, -6)]), 'helm', 'f', ln=True),
             L(outline([(2, 70), (8, 60), (8, 26), (24, 2), (54, -6), (80, 2), (96, 24), (98, 52), (116, 64, 1), (90, 62), (40, 64)]), 'helm', 'f', ln=True),
             L(outline([(80, 50), (104, 60), (96, 64), (80, 60)]), 'helm_d', 'f', False)],
    'back': [L(blob(SKULL_B), 'skin'), L(outline([(16, 70), (84, 70), (80, 84), (50, 88), (20, 84)]), 'mid', 'b', ln=True),
             L(outline([(46, -4), (50, -24, 1), (54, -4)]), 'helm', 'f', ln=True),
             L(outline([(0, 72), (8, 62), (10, 26), (24, 4), (50, -4), (76, 4), (90, 26), (92, 62), (100, 72), (50, 74)]), 'helm', 'f', ln=True),
             L(outline([(56, 0), (82, 12), (92, 40), (92, 70), (64, 72)]), 'helm_d', 'f', False)],
}
# Theodor Ulrich: pelo castaño oliva peinado hacia atrás en un tupé con un mechón largo que se curva hacia arriba y atrás
# como una antena; ojos azules de enfado y la boca seria
CHARS['theodor-ulrich'] = {
    'body': 'normal', 'pal': pal('#6a5a34', '#f8c090', iris='#3a7ab8', shade='#4e4224'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'face_front': LONG_FACE, 'hairline': [(16, 66), (18, 40), (36, 32), (50, 40), (64, 32), (82, 40), (84, 66)]},
    'front': [L(rope((50, 6), (70, -26), (90, -10), 7), 'mid', 'b', ln=True),
              L(outline([(14, 70), (10, 30), (22, 6), (50, -2), (78, 6), (90, 30), (86, 70), (82, 62), (18, 62)])),
              L(outline([(60, 2), (82, 12), (90, 36), (86, 66), (76, 36)]), 'shade', 'b', False),
              strand([(40, 6), (36, 36)], 'shade', 'b', 1.0), strand([(56, 2), (60, 36)], 'shade', 'b', 1.0)],
    'side': [L(rope((60, 4), (40, -30), (10, -20), 7), 'mid', 'b', ln=True),
             L(outline([(44, 92), (22, 88), (12, 64), (10, 30), (24, 6), (54, -2), (80, 6), (92, 24), (88, 40), (74, 42), (60, 48), (52, 64), (50, 80)])),
             L(outline([(12, 40), (34, 40), (42, 80), (22, 88)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 86), (10, 30), (22, 6), (50, -2), (78, 6), (90, 30), (86, 86), (50, 92)])), L(rope((50, 4), (30, -26), (10, -10), 7), 'mid', 'f', ln=True),
             L(outline([(56, 2), (82, 12), (90, 40), (86, 84), (64, 90)]), 'shade', 'b', False)],
}
# Jan Oster: cara larguísima y estrecha; pelo castaño corto peinado hacia atrás en un tupé; gafas redondas de alambre, una
# nariz enorme en punta y los dientes asomando
CHARS['jan-oster'] = {
    'body': 'delgado', 'pal': pal('#5a3e2a', '#f8b880', shade='#42281a', nose='#e8a070'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': LONG_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 6},
    'front': bald('front') + [L(outline([(16, 46), (14, 24), (2, 14), (20, 2), (50, -4), (80, 0), (98, 8), (88, 22), (84, 46), (72, 32), (50, 30), (30, 36)]), 'mid', 'f', ln=True),
                              L([(24, 66), (40, 62)], OUTC, 'f', False, False, 1.8), L([(76, 66), (60, 62)], OUTC, 'f', False, False, 1.8)]
             + white_eyes(74, 16, 5, 5, 1.8) + round_glasses('front', 74)
             + [L(outline([(46, 70), (54, 70), (58, 106), (50, 110, 1), (42, 106)]), 'nose', 'f', ln=True),
                L(outline([(44, 112), (56, 112), (54, 116), (46, 116)]), WHITE, 'f', ln=True)],
    'side': bald('side') + [L(outline([(14, 60), (12, 26), (28, 6), (60, -4), (90, 4), (98, 18), (80, 20), (56, 22), (36, 40), (24, 64)]), 'mid', 'f', ln=True)]
            + side_eye(74) + round_glasses('side', 74) + [L(outline([(84, 76), (110, 108, 1), (88, 104)]), 'nose', 'f', ln=True)],
    'back': bald('back') + buzz('back', nape=80) + [L(outline([(70, 14), (100, 0, 1), (86, 20)]), 'mid', 'f', ln=True)],
}
# Niklas Kuster: pelo rubio ceniza de mechones barridos hacia un lado en un flequillo que le tapa la frente; gafas
# rectangulares de montura fina, ojos azules y los dientes apretados
CHARS['niklas-kuster'] = {
    'body': 'normal', 'pal': pal('#d0c8a8', '#fcdcc0', iris='#3a7ab8', shade='#a8a080'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 70), (8, 36), (20, 10), (50, 0), (80, 8), (94, 26), (106, 30, 1), (94, 42), (88, 70), (80, 62), (20, 62)])),
              L(outline([(60, 4), (86, 16), (98, 32), (88, 62), (78, 36)]), 'shade', 'b', False),
              L(outline([(10, 68), (12, 40), (26, 22), (50, 14), (74, 18), (90, 30), (88, 44), (74, 40), (58, 42), (44, 48), (34, 60), (28, 70, 1), (20, 58)]), 'mid', 'f', ln=True)]
             + [strand([(30 + k * 12, 18), (20 + k * 12, 50)], 'shade', 'f', 1.0) for k in range(4)] + rect_glasses('front', 76, (120, 110, 90, 255)),
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (10, 30), (22, 8), (52, 0), (80, 6), (96, 18), (104, 30, 1), (90, 34), (74, 40), (60, 48), (52, 64), (50, 80)])),
             L(outline([(12, 40), (34, 40), (42, 80), (22, 88)]), 'shade', 'b', False)] + rect_glasses('side', 76, (120, 110, 90, 255)),
    'back': [L(outline([(12, 84), (8, 36), (20, 10), (50, 0), (80, 10), (92, 36), (100, 40, 1), (88, 50), (88, 84), (50, 90)])),
             L(outline([(56, 4), (84, 16), (94, 44), (88, 82), (64, 88)]), 'shade', 'b', False)],
}
# Jonas Polk: la cabeza cubierta por un pañuelo negro azulado enrollado en diagonal, que deja ver a un lado el pelo blanco;
# un parche redondo gris sobre un ojo, sujeto con una correa; el otro ojo de sueño
CHARS['jonas-polk'] = {
    'body': 'normal', 'pal': pal('#ece8e0', '#fcd0a8', iris='#1e1e1e', cloth='#1e2e38', cloth_d='#141e26', strap='#8a7a5a', patch='#8a8a74'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin'),
              L(outline([(14, 62), (12, 28), (24, 8), (50, 0), (76, 8), (88, 28), (86, 50), (60, 30), (40, 30), (24, 44), (20, 64)])),
              L(outline([(8, 30), (30, 6), (60, 0), (80, 8), (92, 30), (94, 66), (70, 66), (46, 42), (24, 26), (12, 40)]), 'cloth', 'f', ln=True),
              L(outline([(60, 4), (80, 10), (92, 32), (92, 62), (74, 60)]), 'cloth_d', 'f', False),
              L([(8, 40), (40, 52), (70, 66), (94, 80)], 'strap', 'f', False, False, 1.6), L([(30, 20), (94, 50)], 'strap', 'f', False, False, 1.2),
              L(ell(66, 76, 9, 8.6), 'patch', 'f', ln=True), L(ell(64, 74, 3, 2.4), (180, 180, 160, 255), 'f', False)],
    'side': [L(blob(SIDE_SKULL), 'skin'),
             L(outline([(8, 66), (6, 28), (22, 4), (52, -4), (80, 4), (94, 24), (92, 52), (60, 50), (30, 60)]), 'cloth', 'f', ln=True),
             L(outline([(44, 50), (60, 50), (66, 66), (54, 70)]), 'mid', 'f', ln=True), L([(10, 44), (94, 36)], 'strap', 'f', False, False, 1.4)],
    'back': [L(blob(SKULL_B), 'skin'),
             L(outline([(14, 74), (12, 28), (24, 8), (50, 0), (76, 8), (88, 28), (86, 74), (50, 80)])),
             L(outline([(30, 4), (60, 0), (82, 12), (92, 34), (90, 60), (66, 76), (40, 76), (60, 40)]), 'cloth', 'f', ln=True),
             L([(6, 40), (94, 52)], 'strap', 'f', False, False, 1.6)],
}
# Maximilian Müller: pelo castaño de pinchos que salen hacia arriba y a los lados, con una cinta roja ancha en la frente; las
# patillas largas en punta, pinturas naranjas bajo los ojos y una sonrisa
CHARS['maximilian-m-ller'] = {
    'body': 'normal', 'pal': pal('#8a5a2a', '#fcd0a0', iris='#2a9aa0', shade='#6a421a', band='#b02a2a', band_d='#8a1e1e', paint='#e0801e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': messy('front', 12, 8, seed=1403, rx=52, ry=44, cy=36, lo=96)
             + [L(outline([(8, 60), (8, 42), (50, 36), (92, 42), (92, 60), (50, 54)]), 'band', 'f', ln=True), L(outline([(56, 40), (92, 44), (92, 58), (60, 54)]), 'band_d', 'f', False),
                L([(24, 82), (32, 86), (28, 92)], 'paint', 'f', False, False, 1.6), L([(76, 82), (68, 86), (72, 92)], 'paint', 'f', False, False, 1.6)],
    'side': messy('side', 18, 8, seed=1403, rx=48, ry=44, cy=36, nape=100, sweep=-0.4) + [L(outline([(6, 56), (6, 40), (94, 38), (94, 54)]), 'band', 'f', ln=True)],
    'back': messy('back', 16, 9, seed=1403, rx=52, ry=44, cy=36, nape=104) + [L(outline([(6, 60), (6, 42), (50, 38), (94, 42), (94, 60), (50, 56)]), 'band', 'f', ln=True)],
}
# Peter Naumann: pelo gris claro peinado hacia atrás en surcos, corto; un ojo cerrado por una cicatriz que le cruza la
# cara en diagonal y el otro de enfado
CHARS['peter-naumann'] = {
    'body': 'normal', 'pal': pal('#b8b4b0', '#fcd8b0', iris='#3a4a6a', shade='#8a8684', scar='#e0a080'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': (52, 40)},
    'front': [L(outline([(12, 68), (8, 34), (20, 8), (50, 0), (80, 8), (92, 34), (88, 68), (80, 58), (20, 58)])),
              L(outline([(60, 4), (84, 16), (92, 40), (86, 64), (76, 36)]), 'shade', 'b', False)]
             + [strand([(x, 4 + abs(x - 50) * 0.2), (x + (x - 50) * 0.2, 40)], 'shade', 'b', 1.2) for x in (26, 40, 54, 68)]
             + [L(ell(34, 76, 6, 5), WHITE, 'f', ln=True), L(ell(35, 77, 2.4, 2.6), 'iris', 'f', False), L([(26, 68), (42, 70)], OUTC, 'f', False, False, 2.2),
                L(quad((58, 76), (66, 79), (74, 76)), OUTC, 'f', False, False, 2.0), L([(56, 60), (80, 96)], 'scar', 'f', False, False, 1.8)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (8, 34), (22, 8), (52, 0), (80, 8), (94, 24), (90, 40), (74, 42), (60, 48), (52, 64), (50, 80)])),
             L(outline([(12, 40), (34, 40), (42, 80), (22, 88)]), 'shade', 'b', False)] + side_eye(76),
    'back': [L(outline([(12, 84), (8, 34), (20, 8), (50, 0), (80, 8), (92, 34), (88, 84), (50, 90)])),
             L(outline([(56, 4), (84, 16), (92, 44), (88, 82), (64, 88)]), 'shade', 'b', False)],
}
# Gerhard Enders (portero suplente): calvo de cara alargada con dos cicatrices cosidas que le cruzan la cabeza y una pintura
# azul en forma de ola que le baja por la frente y la nariz; ojos amarillos de enfado y los dientes apretados
CHARS['gerhard-enders'] = {
    'body': 'corpulento', 'pal': pal('#2a2a2a', '#d8945a', paint='#1e4a8a', stitch='#4a3020'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': LONG_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 6},
    'front': bald('front') + [L(outline([(60, 0), (78, 10), (70, 30), (52, 56), (44, 80), (40, 100), (34, 96), (36, 72), (44, 48), (62, 20)]), 'paint', 'f', ln=True),
                              L([(14, 50), (86, 50)], 'stitch', 'f', False, False, 1.4), L([(16, 88), (84, 88)], 'stitch', 'f', False, False, 1.4)]
             + [L([(x, 46), (x, 54)], 'stitch', 'f', False, False, 1.0) for x in (20, 32, 44, 56, 68, 80)]
             + [L(outline([(22, 72), (40, 70), (38, 76), (26, 78)]), WHITE, 'f', ln=True), L(outline([(78, 72), (60, 70), (62, 76), (74, 78)]), WHITE, 'f', ln=True),
                L(ell(32, 74, 1.8, 2), (200, 160, 30, 255), 'f', False), L(ell(68, 74, 1.8, 2), (200, 160, 30, 255), 'f', False),
                L([(22, 68), (42, 72)], OUTC, 'f', False, False, 2.4), L([(78, 68), (58, 72)], OUTC, 'f', False, False, 2.4),
                L(outline([(32, 102), (68, 102), (64, 110), (36, 110)]), WHITE, 'f', ln=True)],
    'side': bald('side') + [L(outline([(70, 10), (86, 30), (94, 56), (90, 80), (82, 60), (74, 30)]), 'paint', 'f', ln=True), L([(12, 50), (90, 50)], 'stitch', 'f', False, False, 1.4)]
            + side_eye(74),
    'back': bald('back') + [L([(14, 50), (86, 50)], 'stitch', 'f', False, False, 1.4), L([(16, 80), (84, 80)], 'stitch', 'f', False, False, 1.4)],
}
# Erwin Völz: melena rubia verdosa con raya en medio, lisa arriba y ondulada en mechones largos que le caen por los lados
# hasta el cuello; ojos marrones de enfado y la boca seria
CHARS['erwin-v-lz'] = {
    'body': 'normal', 'pal': pal('#b8b070', '#fcd0a8', iris='#8a4a1e', shade='#8e8650'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': [(16, 72), (18, 44), (32, 36), (50, 34), (68, 36), (82, 44), (84, 72)]},
    'front': longhair('front', 104, 8, part=True)
             + [L(rope((16, 60), (10, 86), (16, 108), 7), 'mid', 'f', ln=True), L(rope((84, 60), (90, 86), (84, 108), 7), 'mid', 'f', ln=True)],
    'side': longhair('side', 98, 8),
    'back': longhair('back', 98, 8, part=True, ends=3),
}
# Jens Hoffman: pelo azul morado liso cortado en tazón con el flequillo recto hasta los ojos y las puntas abiertas a los
# lados a la altura de la barbilla; ojos negros de enfado
CHARS['jens-hoffman'] = {
    'body': 'normal', 'pal': pal('#4a4aa8', '#fcd0a8', shade='#36368a'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(-6, 92, 1), (6, 76), (2, 40), (16, 10), (50, -2), (84, 10), (98, 40), (94, 76), (106, 92, 1), (84, 86), (82, 64), (18, 64), (16, 86)])),
              L(outline([(60, 2), (86, 16), (98, 44), (94, 84), (84, 84), (80, 50)]), 'shade', 'b', False),
              L(outline([(12, 66), (14, 40), (30, 22), (50, 18), (70, 22), (86, 40), (88, 66), (78, 62), (70, 68, 1), (62, 62), (54, 68, 1), (46, 62), (38, 68, 1), (30, 62), (22, 66, 1)]), 'mid', 'f')],
    'side': [L(outline([(56, 70), (52, 96), (40, 100), (22, 110, 1), (8, 92), (2, 40), (18, 10), (50, -2), (78, 6), (94, 26), (94, 50), (80, 48), (66, 52)])),
             L(outline([(4, 44), (34, 44), (46, 86), (24, 102), (8, 90)]), 'shade', 'b', False)],
    'back': [L(outline([(-6, 92, 1), (6, 76), (2, 40), (16, 10), (50, -2), (84, 10), (98, 40), (94, 76), (106, 92, 1), (70, 88), (50, 92), (30, 88)])),
             L(outline([(56, 2), (86, 16), (98, 44), (98, 88), (64, 90)]), 'shade', 'b', False)],
}
# Ernst Fliedner: pelo rubio en un tupé abultado sobre la frente, las sienes de un rubio más oscuro rapadas con dos rayas
# afeitadas en aspa; ojos negros grandes de enfado y orejas grandes
CHARS['ernst-fliedner'] = {
    'body': 'bajito', 'pal': pal('#e8d888', '#fcd0a8', shade='#b8a858', shave='#a89a3a', line='#e0a080'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False, 'big_ears': 4, 'ear_out': 8},
    'front': bald('front') + buzz('front', 'shave', front_y=40)
             + [L(outline([(26, 46), (22, 20), (32, 0), (50, -8), (66, 0), (76, 18), (70, 40), (58, 48), (44, 42), (36, 54, 1)]), 'mid', 'f', ln=True),
                L(outline([(40, 4), (56, 0), (60, 12), (46, 18)]), 'shade', 'f', False)],
    'side': bald('side') + buzz('side', 'shave') + [L(outline([(40, 22), (44, 0), (66, -8), (90, 0), (96, 16), (80, 24), (60, 20)]), 'mid', 'f', ln=True),
                                                    L([(20, 40), (60, 18)], 'line', 'f', False, False, 1.6)],
    'back': bald('back') + buzz('back', 'shave', nape=86) + [L(outline([(36, 22), (40, 0), (50, -8), (62, 0), (66, 22), (50, 30)]), 'mid', 'f', ln=True),
                                                             L([(26, 30), (74, 76)], 'line', 'f', False, False, 1.8), L([(74, 30), (26, 76)], 'line', 'f', False, False, 1.8)],
}
# Emmanuel Ewerz: calvo de cara ancha con dos trenzas naranjas gruesas que le salen de la coronilla y le caen por detrás; ojos
# blancos medio cerrados, nariz enorme y una sonrisa de dientes
CHARS['emmanuel-ewerz'] = {
    'body': 'corpulento', 'pal': pal('#e0702a', '#fcd0b0', shade='#b0541a', nose='#c8805a', tie='#2a3aa8'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 8},
    'front': [L(rope((14, 40), (0, 70), (4, 106), 10), 'mid', 'b', ln=True), L(rope((86, 40), (100, 70), (96, 106), 10), 'mid', 'b', ln=True)]
             + bald('front') + [L(outline([(16, 46), (16, 20), (30, 6), (50, 2), (70, 6), (84, 20), (84, 46), (70, 26), (50, 22), (30, 26)]), 'mid', 'f', ln=True)]
             + [strand([(30, 8), (22, 40)], 'shade', 'f', 1.2), strand([(70, 8), (78, 40)], 'shade', 'f', 1.2)]
             + white_eyes(72, 16, 5.4, 4.4, 1.6, lid=1.5)
             + [L(outline([(42, 74), (58, 74), (64, 92), (36, 92)]), 'nose', 'f', ln=True),
                L(outline([(28, 98), (50, 102), (72, 98), (66, 108), (34, 108)]), WHITE, 'f', ln=True)],
    'side': bald('side') + [L(outline([(14, 64), (12, 28), (28, 6), (56, 0), (80, 8), (88, 22), (60, 20), (40, 30), (26, 60)]), 'mid', 'f', ln=True),
                            L(rope((16, 40), (-10, 64), (-16, 100), 10), 'mid', 'f', ln=True), L(ell(4, 50, 4, 4), 'tie', 'f', ln=True)] + side_eye(72, lid=1.5),
    'back': bald('back') + [L(outline([(16, 60), (14, 22), (28, 6), (50, 2), (72, 6), (86, 22), (84, 60), (50, 66)]), 'mid', 'f', ln=True),
                            L(rope((40, 50), (24, 76), (30, 110), 10), 'mid', 'f', ln=True), L(rope((60, 50), (76, 76), (70, 110), 10), 'mid', 'f', ln=True)],
}
