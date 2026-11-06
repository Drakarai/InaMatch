"""Shin Teikoku Gakuen / Royal Academy Redux (IE2): el equipo de Ray Dark; máscaras, gafas, gorros y caras pintadas, con
sus modelos 3D como referencia (Rowan Beltzer, con su retrato)."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, outline, pal, sheen, spk, strand
from chars_alius import SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE, LONG_FACE, spiky, spiky_face
from chars_ccc import cap_hair
from chars_otaku import back_hair
from chars_sengoku import wavy
from chars_umbrella import BOB_B, BOB_F, BOB_S, bob_shade, fringe
from heads import quad

DARK = (24, 20, 24, 255)
WHITE = (250, 250, 250, 255)


def bald(view):
    if view == 'front':
        return [L(blob(SKULL_F), 'skin'), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'skin_d', 'b', False)]
    if view == 'side':
        return [L(blob(SIDE_SKULL), 'skin')]
    return [L(blob(SKULL_B), 'skin'), L(blob([(58, 12), (86, 36), (84, 68), (66, 84)], 6), 'skin_d', 'b', False)]


# Rowan Beltzer: piel tostada, pelo gris azulado en surcos gruesos pegados al cráneo, ojos pequeños de enfado y labios enormes
CHARS['rowan-beltzer'] = {
    'body': 'corpulento', 'pal': pal('#4a5464', '#c89a50', lip='#a05a3a'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'none', 'face_front': WIDE_FACE, 'big_ears': 2, 'ear_out': 4, 'hairline': (52, 44)},
    'front': cap_hair('front') + [strand([(x, 10 + abs(x - 50) * 0.3), (x + (x - 50) * 0.2, 46)], 'deep', 'b', 2) for x in (26, 38, 50, 62, 74)]
             + [L(blob([(30, 88), (50, 84), (70, 88), (66, 98), (50, 100), (34, 98)]), 'lip', 'f', ln=True)],
    'side': cap_hair('side') + [L(blob([(80, 86), (96, 86), (96, 98), (82, 98)]), 'lip', 'f', ln=True)],
    'back': cap_hair('back') + [strand([(x, 10), (x, 80)], 'deep', 'b', 2) for x in (30, 42, 54, 66)],
}
BH_FRONT = [(2, 72, 1), (2, 58), (-14, 66, 1), (-2, 46), (-18, 40, 1), (0, 30), (-6, 14, 1), (14, 12), (22, 0), (50, -2), (78, 0), (86, 12),
            (106, 12, 1), (100, 28), (118, 40, 1), (102, 48), (114, 66, 1), (98, 60), (98, 72, 1), (86, 62), (14, 62)]
CHARS['blade-healen'] = {
    'body': 'normal', 'pal': pal('#6a6650', '#f8b060', iris='#d0501a', band='#7a4a7a', tie=WHITE, camo='#54483a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin'),
              L(outline(BH_FRONT)),
              L(outline([(46, 8), (40, 0), (28, -6), (12, -10, 1), (22, -16), (8, -26, 1), (30, -30), (50, -30), (60, -24), (63, -10), (56, 6)]), 'mid', 'b', ln=True),
              L(outline([(44, 4), (38, -4), (28, -10), (40, -16), (54, -18), (56, -6)]), 'camo', 'b', False),
              L(ell(50, 6, 6, 2.6), 'tie', 'b', ln=True),
              L(outline([(26, 4), (40, 10), (36, 18), (22, 14)]), 'camo', 'b', False), L(outline([(68, 6), (90, 18), (96, 36), (76, 24)]), 'camo', 'b', False),
              L(quad((14, 62), (50, 56), (86, 62)) + quad((86, 72), (50, 66), (14, 72)), 'band', 'f', ln=True),
              L(outline([(12, 66, 1), (14, 40), (30, 24), (50, 20), (70, 24), (86, 40), (88, 66, 1), (80, 60), (72, 66, 1), (64, 58), (56, 64, 1),
                         (50, 56), (42, 64, 1), (34, 58), (26, 66, 1), (20, 60)]), 'mid', 'f'),
              L(outline([(54, 26), (80, 34), (86, 52), (70, 48)]), 'camo', 'f', False),
              ]
             + spk((10, 62), (20, 64), (14, 94), 3, z='f') + spk((80, 64), (90, 62), (86, 94), 3, z='f', light_left=False)
             + [L([(54, 96), (56, 100), (58, 96)], WHITE, 'f', False)],
    'side': [L(outline([(14, 86), (20, 100, 1), (2, 86), (-8, 96, 1), (-4, 74), (-22, 66, 1), (-2, 54), (-20, 40, 1), (0, 34), (-12, 16, 1), (10, 12),
                        (30, 0), (60, 2), (84, 14), (96, 36), (94, 62, 1), (84, 54), (70, 50), (56, 60), (46, 76), (32, 88)])),
             L(outline([(36, 6), (34, -8), (40, -24), (54, -32), (66, -26), (72, -14, 1), (62, -18), (56, -8), (52, 4)]), 'mid', 'b', ln=True),
             L(outline([(40, 4), (40, -12), (50, -24), (56, -14), (50, 0)]), 'camo', 'b', False),
             L(ell(44, 6, 6, 2.6), 'tie', 'b', ln=True),
             L(outline([(18, 26), (36, 18), (40, 36), (24, 44)]), 'camo', 'b', False), L(outline([(60, 12), (82, 20), (84, 36), (66, 30)]), 'camo', 'b', False),
             L(outline([(-4, 60), (14, 56), (24, 76), (10, 84)]), 'camo', 'b', False),
             L(quad((70, 60), (84, 56), (96, 60)) + quad((96, 68), (84, 64), (72, 70)), 'band', 'f', ln=True)]
            + spk((76, 18), (94, 30), (94, 86), 4, z='f', light_left=False),
    'back': [L(outline([(-6, 14, 1), (14, 12), (22, 0), (50, -2), (78, 0), (86, 12), (106, 14, 1), (100, 28), (118, 40, 1), (102, 50), (116, 70, 1),
                        (98, 70), (92, 92, 1), (76, 88), (64, 104, 1), (52, 92), (40, 106, 1), (28, 90), (10, 94, 1), (2, 72), (-16, 70, 1), (-2, 50),
                        (-18, 40, 1), (0, 30)])),
             L(outline([(40, 6), (36, -6), (24, -12, 1), (36, -16), (42, -26), (60, -30), (86, -30, 1), (70, -22), (78, -14, 1), (60, -10), (58, 6)]), 'mid', 'b', ln=True),
             L(outline([(44, 4), (42, -14), (56, -22), (60, -12), (54, 4)]), 'camo', 'b', False),
             L(ell(50, 6, 7, 2.6), 'tie', 'b', ln=True),
             L(outline([(60, 4), (94, 26), (100, 64), (84, 84), (66, 60)]), 'shade', 'b', False),
             L(outline([(26, 24), (46, 20), (44, 40), (28, 44)]), 'camo', 'b', False), L(outline([(56, 52), (76, 46), (78, 64), (60, 68)]), 'camo', 'b', False)],
}
ARGIE_FACE = blob([(18, 50), (30, 38), (50, 34), (70, 38), (82, 50), (92, 76), (96, 98), (86, 112), (50, 118), (14, 112), (4, 98), (8, 76)])
CHARS['argie-bargie'] = {
    'body': 'corpulento', 'pal': pal('#4a2a3a', '#a88068', skin_d='#8a6450', teeth=(250, 250, 244, 255)),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': ARGIE_FACE, 'nose': (50, 78, 4.6), 'hairline': False,
             'big_ears': 2, 'ear_out': 6},
    'front': [L(blob(SKULL_F), 'skin'),
              L(blob([(14, 56), (16, 30), (30, 12), (50, 6), (70, 12), (84, 30), (86, 56), (70, 52), (56, 58), (50, 68), (44, 58), (30, 52)]), 'mid', 'f'),
              L(blob([(58, 14), (82, 30), (84, 52), (66, 48)], 5), 'shade', 'f', False)]
             + spk((36, 12), (50, 6), (34, -14), 4, z='f') + spk((44, 8), (58, 8), (50, -20), 5, z='f') + spk((52, 6), (66, 12), (68, -12), 4, z='f', light_left=False)
             + spk((10, 50), (16, 64), (-4, 52), 3, z='f') + spk((12, 60), (16, 72), (-2, 70), 3, z='f')
             + spk((84, 64), (90, 50), (104, 52), 3, z='f', light_left=False) + spk((84, 72), (88, 60), (102, 70), 3, z='f', light_left=False)
             + [L([(22, 64), (40, 72)], OUTC, 'f', False, False, 2.6), L([(78, 64), (60, 72)], OUTC, 'f', False, False, 2.6),
                L([(26, 68), (40, 74), (36, 79), (28, 76)], WHITE, 'f', ln=True), L([(74, 68), (60, 74), (64, 79), (72, 76)], WHITE, 'f', ln=True),
                L(ell(35, 75, 1.6, 1.8), OUTC, 'f', False), L(ell(65, 75, 1.6, 1.8), OUTC, 'f', False),
                L(blob([(18, 84), (34, 80), (50, 84), (66, 80), (82, 84), (80, 94), (50, 98), (20, 94)], 6), 'teeth', 'f', ln=True),
                L([(20, 89), (50, 91), (80, 89)], OUTC, 'f', False, False, 0.9)]
             + [L([(x, 82 + abs(x - 50) * 0.02), (x, 96 - abs(x - 50) * 0.06)], OUTC, 'f', False, False, 0.7) for x in (30, 40, 50, 60, 70)]
             + [L(quad((38, 106), (50, 104), (62, 107)), OUTC, 'f', False, False, 1.2)],
    'side': [L(blob([(20, 40), (40, 30), (64, 34), (80, 48), (94, 70), (96, 98), (82, 112), (56, 114), (34, 100), (20, 74)]), 'skin'),
             L(blob([(30, 60), (40, 100), (56, 114), (34, 104), (20, 80)], 6), 'skin_d', 'b', False),
             L(blob([(40, 10), (62, 4), (80, 12), (88, 30), (86, 46), (74, 36), (58, 38), (42, 48), (26, 60), (8, 68), (-12, 70), (2, 58), (-10, 54),
                     (6, 46), (-6, 38), (14, 28)])),
             L(blob([(40, 40), (20, 50), (6, 62), (0, 56), (24, 38)], 5), 'shade', 'b', False)]
            + spk((50, 6), (66, 4), (56, -16), 4) + spk((64, 4), (80, 12), (82, -10), 4, light_left=False) + spk((32, 14), (48, 8), (24, -6), 4)
            + [L([(70, 66), (86, 72)], OUTC, 'f', False, False, 2.4), L([(76, 72), (88, 74), (86, 80), (78, 78)], WHITE, 'f', ln=True),
               L(ell(98, 78, 4, 4), 'skin_d', 'f', ln=True),
               L(blob([(80, 86), (96, 86), (96, 98), (82, 98)], 4), 'teeth', 'f', ln=True), L(quad((84, 106), (90, 108), (94, 106)), OUTC, 'f', False, False, 1.0)],
    'back': [L(blob(SKULL_B), 'skin'), L(blob([(58, 12), (86, 36), (84, 68), (66, 84)], 6), 'skin_d', 'b', False),
             L(blob([(36, 6), (50, 0), (64, 6), (80, 40), (90, 76), (84, 90), (50, 94), (16, 90), (10, 76), (20, 40)])),
             L(blob([(56, 6), (78, 40), (88, 76), (70, 88), (62, 50)], 6), 'shade', 'b', False)]
            + spk((24, 30), (30, 18), (6, 4), 3) + spk((76, 30), (70, 18), (94, 4), 3, light_left=False)
            + spk((12, 62), (16, 50), (-8, 52), 3) + spk((88, 62), (84, 50), (108, 52), 3, light_left=False),
}
# Lee Bamboo: piel amarilla y cara alargada de mandíbula ancha; pelo morado pegado en forma de gorro con pico hasta el
# entrecejo y dos puntas horizontales a los lados de arriba; orejas de elfo puntiagudas, ojos blancos de enfado y una
# sonrisa ancha de oreja a oreja
CHARS['lee-bamboo'] = {
    'body': 'normal', 'pal': pal('#4a3a6a', '#d8a850', skin_d='#c08a3a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': LONG_FACE, 'hairline': False, 'ears': False},
    'front': [L(outline([(18, 58), (-2, 44, 1), (6, 64), (16, 82)]), 'skin', 'b', ln=True), L(outline([(82, 58), (102, 44, 1), (94, 64), (84, 82)]), 'skin', 'b', ln=True),
              L(blob(SKULL_F), 'skin'),
              L(outline([(16, 52), (16, 24), (30, 10), (50, 6), (70, 10), (84, 24), (84, 52), (76, 46), (64, 46), (50, 62, 1), (36, 46), (24, 46)]), 'mid', 'f'),
              L(outline([(60, 10), (82, 24), (84, 48), (70, 44)]), 'shade', 'f', False),
              L(outline([(20, 12), (-12, 8, 1), (18, 26)]), 'mid', 'f'), L(outline([(80, 12), (112, 8, 1), (82, 26)]), 'mid', 'f'),
              L(outline([(24, 70), (40, 74, 1), (36, 78), (28, 77)]), WHITE, 'f', ln=True), L(outline([(76, 70), (60, 74, 1), (64, 78), (72, 77)]), WHITE, 'f', ln=True),
              L(ell(33, 75, 1.4, 1.6), OUTC, 'f', False), L(ell(67, 75, 1.4, 1.6), OUTC, 'f', False),
              L([(22, 66), (40, 72)], OUTC, 'f', False, False, 1.8), L([(78, 66), (60, 72)], OUTC, 'f', False, False, 1.8),
              L(quad((24, 90), (50, 104), (76, 90)), OUTC, 'f', False, False, 1.4)],
    'side': [L(outline([(10, 62), (10, 30), (28, 10), (56, 4), (78, 12), (88, 30), (84, 44), (76, 38), (70, 50), (60, 44), (48, 54), (42, 74), (38, 90),
                        (20, 88)])),
             L(outline([(14, 50), (20, 80), (36, 88), (26, 62)]), 'shade', 'b', False),
             L(outline([(42, 76), (34, 50, 1), (50, 62), (50, 80)]), 'skin', 'f', ln=True),
             L(quad((76, 92), (82, 97), (88, 92)), OUTC, 'f', False, False, 1.4)],
    'back': [L(outline([(18, 58), (-4, 42, 1), (6, 66), (18, 82)]), 'skin', 'b', ln=True), L(outline([(82, 58), (104, 42, 1), (94, 66), (82, 82)]), 'skin', 'b', ln=True),
             L(outline([(14, 82), (12, 40), (16, 28), (-14, 10, 1), (20, 8), (50, 6), (80, 8), (114, 10, 1), (84, 28), (88, 40), (86, 82), (50, 86)])),
             L(outline([(60, 10), (86, 36), (84, 80), (64, 84)]), 'shade', 'b', False)],
}
from heads import fat
fat_streak = fat((40, 30), (60, 30), (50, -18), 5)
# Dawson Little: pelo blanco de pinchos con una estrella de pinchos azul en medio de la frente; una cinta negra ancha le
# rodea la cabeza sobre las cejas (los ojos, azules, quedan a la vista); piel morena
CHARS['dawson-little'] = {
    'body': 'normal', 'pal': pal('#ece8e4', '#c8885a', shade='#c8bcbc', streak='#3a6aa8', streak_d='#284e80', band='#2a2020'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': False, 'iris': None},
    'front': [L(outline([(10, 62), (4, 48), (-10, 44, 1), (4, 34), (-6, 18, 1), (14, 16), (10, -2, 1), (28, 6), (30, -14, 1), (42, 2), (52, -18, 1),
                         (58, 0), (72, -8, 1), (72, 8), (92, 4, 1), (84, 20), (104, 24, 1), (90, 36), (102, 48, 1), (90, 56), (90, 62)])),
              L(outline([(60, 4), (90, 24), (92, 52), (74, 40)]), 'shade', 'b', False),
              L(outline([(12, 62), (16, 40), (30, 28), (50, 24), (70, 28), (84, 40), (88, 62)]), 'mid', 'f'),
              L(outline([(12, 58), (50, 54), (88, 58), (88, 68), (50, 64), (12, 68)]), 'band', 'f', ln=True),
              L(outline([(50, 12, 1), (56, 28), (72, 20, 1), (62, 34), (78, 40, 1), (62, 44), (64, 60, 1), (52, 48), (42, 60, 1), (40, 44), (24, 42, 1),
                         (38, 34), (32, 20, 1), (44, 28)]), 'streak', 'f', ln=True),
              L(outline([(52, 26), (58, 34), (56, 46), (50, 40)]), 'streak_d', 'f', False)]
             + spk((10, 58), (20, 60), (12, 74), 2, z='f') + spk((80, 60), (90, 58), (88, 74), 2, z='f', light_left=False),
    'side': [L(outline([(14, 82), (4, 66), (-14, 60, 1), (2, 50), (-12, 36, 1), (6, 30), (-4, 14, 1), (16, 14), (14, -4, 1), (32, 6), (40, -14, 1),
                        (50, 4), (64, -8, 1), (66, 10), (84, 8, 1), (80, 22), (94, 30), (96, 52), (84, 58), (60, 58), (42, 62), (30, 82)])),
             L(outline([(4, 60), (20, 62), (30, 80), (14, 80)]), 'shade', 'b', False),
             L(outline([(84, 20), (98, 8, 1), (96, 26), (106, 38, 1), (94, 42), (90, 30)]), 'streak', 'b', ln=True),
             L(outline([(2, 52), (96, 56), (96, 68), (4, 64)]), 'band', 'f', ln=True)],
    'back': [L(outline([(8, 84), (4, 48), (-10, 44, 1), (4, 34), (-6, 18, 1), (14, 16), (10, -2, 1), (28, 6), (30, -14, 1), (42, 2), (52, -18, 1),
                        (58, 0), (72, -8, 1), (72, 8), (92, 4, 1), (84, 20), (104, 24, 1), (90, 36), (102, 48, 1), (94, 56), (92, 84), (50, 90)])),
             L(outline([(60, 4), (92, 30), (94, 84), (66, 88)]), 'shade', 'b', False),
             L(outline([(4, 52), (50, 50), (96, 52), (96, 66), (50, 64), (4, 66)]), 'band', 'b', ln=True)],
}
# Eton Messer: pelo rubio en pinchos desordenados que acaba recto sobre la frente; una banda verde oliva y otra azul
# petróleo le rodean la cabeza, y delante lleva un gran visor verde de un solo ojo con la lente azul en el centro de la
# cara; una bufanda crema gruesa le tapa hasta la nariz
CHARS['eton-messer'] = {
    'body': 'normal', 'pal': pal('#e0b020', '#f0c080', scarf='#e8dcc8', scarf_d='#b8a890', rim='#3a6a3a', rim_d='#2a4a2a', lens='#2a7ab0',
                                 olive='#8a8030', strap='#1e3a4a', ring='#e8e0c8'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin'),
              L(outline([(10, 36), (2, 22, 1), (14, 18), (8, 2, 1), (22, 8), (22, -10, 1), (34, 4), (42, -14, 1), (50, 2), (60, -14, 1), (64, 4), (76, -8, 1),
                         (78, 8), (94, 0, 1), (86, 18), (100, 22, 1), (90, 36), (50, 34)]), 'mid', 'f'),
              L(outline([(56, 6), (66, -4, 1), (72, 12), (88, 6, 1), (84, 22), (92, 32), (60, 30)]), 'shade', 'f', False),
              strand([(30, 30), (26, 10)], 'shade', 'f', 1.0), strand([(46, 30), (44, 6)], 'shade', 'f', 1.0),
              L(outline([(10, 36), (18, 36), (20, 66), (12, 66)]), 'olive', 'f', ln=True), L(outline([(90, 36), (82, 36), (80, 66), (88, 66)]), 'olive', 'f', ln=True),
              L(outline([(10, 64), (90, 64), (90, 72), (10, 72)]), 'strap', 'f', ln=True),
              L(outline([(32, 54), (68, 54), (80, 64), (80, 84), (68, 94), (32, 94), (20, 84), (20, 64)]), 'rim', 'f', ln=True),
              L(outline([(60, 56), (68, 56), (78, 66), (78, 84), (68, 92), (62, 90)]), 'rim_d', 'f', False),
              L(ell(50, 74, 13.5, 12.5), 'ring', 'f', ln=True), L(ell(50, 74, 10.5, 9.8), 'lens', 'f', False), L(ell(46, 70, 3, 2.4), WHITE, 'f', False),
              L(blob([(6, 88), (50, 90), (94, 88), (98, 114), (50, 122), (2, 114)]), 'scarf', 'f', ln=True),
              L(blob([(58, 86), (94, 84), (96, 110), (60, 116)], 5), 'scarf_d', 'f', False)],
    'side': [L(blob(SIDE_SKULL), 'skin'),
             L(outline([(14, 40), (2, 30, 1), (14, 24), (6, 8, 1), (22, 12), (22, -6, 1), (36, 6), (44, -10, 1), (54, 6), (62, -8, 1), (68, 8), (82, 2, 1),
                        (80, 18), (92, 22, 1), (86, 34), (50, 32)]), 'mid', 'b'),
             L(outline([(12, 32), (88, 34), (88, 46), (14, 46)]), 'olive', 'b', ln=True),
             L(outline([(14, 46), (88, 50), (88, 56), (16, 54)]), 'strap', 'b', ln=True),
             L(outline([(80, 54), (94, 54), (98, 62), (96, 72), (80, 72)]), 'rim', 'f', ln=True), L(ell(96, 63, 2.6, 6), 'lens', 'f', ln=True),
             L(blob([(26, 80), (96, 78), (100, 108), (30, 114)]), 'scarf', 'f', ln=True), L(blob([(30, 96), (60, 100), (90, 104), (40, 112)], 5), 'scarf_d', 'f', False)],
    'back': [L(outline([(10, 36), (2, 22, 1), (14, 18), (8, 2, 1), (22, 8), (22, -10, 1), (34, 4), (42, -14, 1), (50, 2), (60, -14, 1), (64, 4), (76, -8, 1),
                        (78, 8), (94, 0, 1), (86, 18), (100, 22, 1), (90, 36), (50, 34)])),
             L(outline([(56, 6), (66, -4, 1), (72, 12), (88, 6, 1), (84, 22), (92, 32), (60, 30)]), 'shade', 'b', False),
             L(outline([(8, 32), (50, 30), (92, 32), (92, 50), (50, 48), (8, 50)]), 'olive', 'b', ln=True),
             L(outline([(8, 50), (50, 48), (92, 50), (92, 58), (50, 56), (8, 58)]), 'strap', 'b', ln=True),
             L(blob([(6, 84), (50, 82), (94, 84), (96, 112), (50, 118), (4, 112)]), 'scarf', 'f', ln=True)],
}
# Jonah Spark: melena rubia ceniza hasta la barbilla que le tapa media cara (la derecha de la imagen), con dos coletas
# bajas atadas a los lados (goma naranja y goma gris azulada); la otra media cara, una máscara negra azulada con un ojo
# blanco redondo y una boca de una raya
CHARS['jonah-spark'] = {
    'body': 'normal', 'pal': pal('#e0d4b8', '#f8d8b8', shade='#c0b098', mask='#2a3a4a', tie='#d0782a', tie2='#7a8a98'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': (60, 50), 'ears': False},
    'front': [L(outline([(10, 108), (0, 70), (4, 30), (20, 6), (50, -2), (80, 6), (96, 30), (100, 70), (90, 108), (80, 100), (84, 62), (16, 62),
                         (20, 100)])),
              L(outline([(66, 6), (94, 30), (98, 70), (86, 66)]), 'shade', 'b', False),
              L(outline([(16, 58), (50, 54), (54, 108), (26, 104), (16, 84)]), 'mask', 'f', ln=True),
              L(ell(32, 76, 6.5, 6.5), WHITE, 'f', ln=True), L(quad((24, 94), (36, 98), (48, 94)), (120, 130, 140, 255), 'f', False, False, 1.0),
              L(outline([(14, 62), (16, 38), (30, 24), (50, 20), (70, 24), (86, 40), (92, 70), (90, 104), (74, 102), (62, 84), (54, 60), (40, 58), (24, 66)]), 'mid', 'f'),
              L(outline([(60, 30), (84, 42), (88, 96), (76, 92), (66, 60)]), 'shade', 'f', False),
              L(outline([(2, 98), (16, 98), (14, 112), (8, 128, 1), (2, 112)]), 'mid', 'f', ln=True), L(outline([(98, 98), (84, 98), (86, 112), (92, 128, 1), (98, 112)]), 'mid', 'f', ln=True),
              L(ell(9, 104, 6, 2.6), 'tie', 'f', ln=True), L(ell(91, 104, 6, 2.6), 'tie2', 'f', ln=True)],
    'side': [L(outline([(60, 70), (56, 100), (44, 112), (24, 112), (6, 102), (0, 76), (4, 40), (20, 12), (50, 0), (78, 8), (94, 30), (97, 60), (90, 66),
                        (84, 52), (72, 48)])),
             L(outline([(8, 40), (30, 30), (56, 50), (50, 100), (24, 108), (8, 96)]), 'shade', 'b', False),
             L(outline([(76, 50), (92, 56), (96, 80), (92, 100), (80, 104), (74, 80)]), 'mask', 'f', ln=True), L(ell(88, 74, 3.6, 6), WHITE, 'f', ln=True),
             L(outline([(30, 106), (44, 106), (40, 120), (34, 132, 1), (28, 120)]), 'mid', 'f', ln=True), L(ell(37, 110, 6, 2.6), 'tie', 'f', ln=True)],
    'back': [L(outline([(10, 108), (0, 70), (4, 30), (20, 6), (50, -2), (80, 6), (96, 30), (100, 70), (90, 108), (70, 96), (50, 92), (30, 96)])),
             L(outline([(0, 52), (30, 40), (50, 48), (70, 40), (100, 52), (98, 80), (86, 104), (70, 92), (50, 88), (30, 92), (12, 104), (2, 80)]), 'shade', 'b', False),
             L(outline([(2, 98), (16, 98), (14, 112), (8, 128, 1), (2, 112)]), 'mid', 'b', ln=True), L(outline([(98, 98), (84, 98), (86, 112), (92, 128, 1), (98, 112)]), 'mid', 'b', ln=True),
             L(ell(9, 104, 6, 2.6), 'tie2', 'b', ln=True), L(ell(91, 104, 6, 2.6), 'tie', 'b', ln=True)],
}
# Sue Sparrow: pelo coral en media melena que le tapa la frente y el ojo izquierdo, una mascarilla del mismo coral que le
# cruza la cara en diagonal tapando la nariz y la boca y, por su lado izquierdo, tres tirabuzones largos hasta los hombros
CHARS['sue-sparrow'] = {
    'body': 'chica', 'pal': pal('#e0786a', '#fcd8b8', mask='#d8705e', iris='#2a2a3a'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'none', 'hairline': (56, 48)},
    'front': [L(blob(BOB_F))] + bob_shade('front')
             + wavy((78, 40), (90, 40), (90, 92), 6, light_left=False) + wavy((84, 50), (98, 52), (104, 108), 6, light_left=False)
             + wavy((76, 66), (88, 66), (84, 112), -6, light_left=False)
             + [L(outline([(38, 30), (60, 22), (82, 34), (88, 64), (84, 84), (72, 74), (60, 60), (50, 44)]), 'mid', 'f'),
                L(outline([(4, 86), (40, 76), (70, 62), (86, 66), (82, 92), (58, 100), (26, 104), (10, 98)]), 'mask', 'f', ln=True),
                strand([(46, 34), (64, 50), (80, 70)], 'shade', 'f', 1.2)],
    'side': [L(blob(BOB_S))] + bob_shade('side')
             + wavy((66, 40), (78, 46), (78, 100), 6, z='f', light_left=False) + wavy((60, 56), (72, 60), (66, 112), -6, z='f')
             + [L(outline([(66, 80), (96, 74), (98, 98), (78, 104)]), 'mask', 'f', ln=True)],
    'back': [L(blob(BOB_B))] + bob_shade('back') + wavy((4, 46), (16, 46), (-2, 98), -6) + wavy((6, 60), (18, 62), (6, 112), 6) + wavy((-2, 54), (8, 56), (-10, 104), -6),
}
def horn(k, view='front'):
    """Cuerno de pelo grueso que sale del lado de la cabeza y se curva hacia arriba y hacia fuera (k = -1 izquierda, 1 derecha)."""
    pts = [(28, 26), (8, 26), (-12, 18), (-24, 2), (-22, -10), (-14, 4), (2, 12), (22, 12), (36, 18)]
    return L(blob([(50 + (x - 50) * 1 if k < 0 else 100 - x, y) for x, y in pts], 6), 'mid', 'b', ln=True)


# Riley Jamm: payaso. Cara pintada de blanco con una sonrisa enorme de dientes amarillos y comisuras rojas, un ojo guiñado
# y el otro con una espiral amarilla. Pelo verde azulado pegado en pico hasta la frente, con un cuerno largo que sube por
# su derecha y se enrosca por arriba (de perfil y de espaldas forma un gran aro) y otro cuerno corto a su izquierda
CHARS['riley-jamm'] = {
    'body': 'normal', 'pal': pal('#1e7a6a', '#f4f0e8', teeth='#e8d880', red='#c8202a', eye='#e8d040'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin'),
              L(outline([(16, 62), (-6, 34), (-4, 6), (10, -16), (30, -28, 1), (18, -12), (10, 8), (10, 30), (22, 50)]), 'mid', 'b', ln=True),
              L(outline([(84, 38), (100, 22), (112, 4, 1), (106, 28), (88, 56)]), 'mid', 'b', ln=True),
              L(outline([(14, 64), (14, 36), (26, 12), (44, -8), (52, -26, 1), (60, -8), (76, 12), (86, 36), (86, 64), (76, 52), (64, 40), (50, 58, 1),
                         (36, 40), (24, 52)]), 'mid', 'f'),
              L(outline([(56, -8), (76, 14), (84, 50), (68, 38)]), 'shade', 'f', False),
              L(quad((26, 66), (34, 62), (42, 66)), 'mid', 'f', False, False, 1.0), L(quad((58, 66), (66, 62), (74, 66)), 'mid', 'f', False, False, 1.0),
              L(quad((27, 75), (34, 70), (42, 75)), OUTC, 'f', False, False, 1.8),
              L(ell(65, 74, 6, 5.4), 'eye', 'f', ln=True), L(ell(65, 74, 3, 2.6), OUTC, 'f', False, False, 0.7),
              L(outline([(14, 80, 1), (50, 86), (86, 80, 1), (72, 98), (50, 104), (28, 98)]), 'red', 'f', ln=True),
              L(outline([(22, 84), (50, 88), (78, 84), (68, 96), (50, 100), (32, 96)]), 'teeth', 'f', False),
              L([(22, 88), (50, 92), (78, 88)], OUTC, 'f', False, False, 0.9)]
             + [L([(x, 86 + abs(x - 50) * -0.03), (x, 98 - abs(x - 50) * 0.08)], OUTC, 'f', False, False, 0.7) for x in (32, 41, 50, 59, 68)],
    'side': [L(outline([(52, 2), (30, -20), (0, -24), (-22, -8), (-30, 16), (-22, 38, 1), (-18, 14), (-6, -6), (16, -10), (40, 4)]), 'mid', 'b', ln=True),
             L(outline([(18, 86), (8, 62), (10, 30), (28, 8), (56, 0), (78, 8), (86, 24), (80, 40), (68, 36), (54, 56), (46, 86)])),
             L(outline([(12, 50), (20, 80), (40, 86), (28, 60)]), 'shade', 'b', False),
             L(outline([(80, 82, 1), (96, 84), (94, 98), (84, 102, 1)]), 'red', 'f', ln=True), L(outline([(84, 86), (95, 87), (93, 96), (86, 98)]), 'teeth', 'f', False),
             L(quad((76, 75), (81, 71), (86, 75)), OUTC, 'f', False, False, 1.8)],
    'back': [L(outline([(14, 82), (12, 40), (24, 14), (50, 2), (76, 14), (88, 40), (86, 82), (50, 86)])),
             L(outline([(60, 6), (86, 36), (84, 78), (64, 84)]), 'shade', 'b', False),
             L(outline([(30, 30), (4, 40), (-18, 32), (-28, 14, 1), (-8, 24), (20, 20)]), 'mid', 'b', ln=True),
             L(outline([(56, 24), (96, 28), (118, 16), (120, 0), (104, -12), (78, -12, 1), (104, -4), (110, 8), (94, 18), (64, 12)]), 'mid', 'b', ln=True)],
}
# Caleb Stonewall: medio cráneo rapado. Una cresta castaña oscura recorre la cabeza de la frente a la coronilla y por su
# derecha cae en una masa de pelo con un mechón sobre la frente hasta entre los ojos; la izquierda va rapada, con un rayo
# rojo pintado en la sien. De perfil y de espaldas solo se ve la cresta sobre la cabeza rapada. Contornos calcados del
# modelo 3D sobre una rejilla de unidades de cabeza.
CHARS['caleb-stonewall'] = {
    'body': 'normal', 'pal': pal('#4a3424', '#fad4a0', iris='#3a6a62', paint='#c42a14', light='#6a4c36'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': False, 'big_ears': 1, 'ear_out': 2},
    'front': [L(blob(SKULL_F), 'skin'),
              L([(71, 15), (77, 18), (72, 27), (78, 29), (80, 35), (76, 41), (68, 45), (73, 37), (74, 33), (67, 32)], 'paint', 'b', False),
              L([(69, 45), (76, 46), (66, 57)], 'paint', 'b', False),
              L(outline([(5, 52, 1), (14, 47), (18, 42), (17, 34), (16, 29), (9, 31, 1), (13, 14), (21, 1), (31, -9), (40, -11), (31, -17, 1), (41, -24),
                         (50, -26), (57, -21), (62, -15, 1), (67, -17), (77, -16, 1), (70, -14), (66, -9), (65, -3), (64, 5), (60, 12),
                         (59, 21), (61, 32), (60, 39), (57, 45), (53, 51), (51, 60), (53, 68, 1), (50, 67), (46, 79, 1), (43, 70),
                         (39, 63), (33, 58), (23, 54), (17, 55), (11, 55)]), 'mid', 'f'),
              # sombras: bajo la masa a la izquierda del mechón y la raya oscura bajo la cresta
              L(outline([(20, 50), (26, 40), (36, 36), (42, 44), (46, 56), (46, 79, 1), (43, 70), (39, 63), (33, 58), (23, 54)]), 'shade', 'f', False),
              L(outline([(50, 10), (55, 4), (59, 12), (58, 30), (55, 42, 1), (52, 26)]), 'shade', 'f', False),
              L(outline([(15, 14), (22, 10), (20, 22), (10, 30, 1), (15, 20)]), 'shade', 'f', False),
              strand([(28, 6), (36, 18), (42, 34), (46, 50)], 'deep', 'f', 1.0), strand([(42, -16), (46, -6), (48, 6)], 'deep', 'f', 1.0),
              L(outline([(26, 4), (34, -4), (42, -7), (34, 1), (28, 8)]), 'light', 'f', False)],
    'side': [L(blob(SIDE_SKULL), 'skin'),
             L(blob([(14, 44), (20, 26), (30, 30), (48, 40), (60, 56), (64, 76), (60, 92), (44, 92), (24, 82), (14, 64)], 6), 'skin_d', 'b', False),
             L(outline([(26, -19, 1), (36, -14), (44, -12), (51, -16), (59, -22), (69, -24), (76, -20, 1), (70, -14), (66, -9), (71, -10),
                        (80, -11), (92, -8), (97, 0), (100, 9), (99, 13, 1), (104, 21), (107, 32), (107, 43), (108, 49, 1), (100, 50),
                        (97, 56), (95, 66), (92, 76, 1), (89, 72), (87, 62), (86, 50), (83, 38), (79, 25), (71, 16), (62, 10), (52, 8),
                        (40, 8), (33, 10), (33, -6)]), 'mid', 'b'),
             L(outline([(36, 8), (37, -4), (44, -8), (54, -10), (60, -4), (64, 4), (68, 12), (60, 9), (50, 8)]), 'shade', 'b', False),
             L(outline([(80, -6), (92, -4), (98, 8), (96, 14), (102, 26), (98, 30), (90, 12)]), 'light', 'b', False),
             strand([(84, 0), (94, 20), (100, 40)], 'deep', 'b', 1.0), strand([(78, 10), (88, 30), (92, 52), (91, 70)], 'deep', 'b', 1.0)],
    'back': [L(blob(SKULL_B), 'skin'), L(blob([(58, 12), (86, 36), (84, 68), (66, 84)], 6), 'skin_d', 'b', False),
             L([(28, 20), (30, 18), (30, 26)], 'paint', 'b', False),
             L(outline([(21, -20, 1), (26, -21), (31, -18), (38, -14), (42, -12, 1), (46, -16), (52, -17), (58, -15), (66, -7, 1), (59, -6),
                        (55, -4), (57, -2), (65, 1), (73, 8), (79, 16), (83, 25), (84, 34, 1), (81, 28), (75, 22), (70, 16), (62, 12), (50, 12),
                        (42, 13), (37, 13), (36, -4), (33, -13), (28, -18)]), 'mid', 'b'),
             L(outline([(38, 12), (38, 0), (42, -6), (48, -2), (54, 6), (50, 12)]), 'shade', 'b', False),
             L(outline([(64, 4), (74, 10), (80, 20), (83, 30, 1), (76, 18)]), 'shade', 'b', False)],
}
# Jimbo Cellar (portero suplente): melena castaña lisa y larga con raya en medio, cara alargada pálida y ojos rasgados
CHARS['jimbo-cellar'] = {
    'body': 'delgado', 'pal': pal('#6a4830', '#fce4c8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 98, 'face_front': LONG_FACE, 'hairline': [(14, 70), (26, 52), (42, 42), (50, 48), (58, 42), (74, 52), (86, 70)]},
    'front': [L(blob([(6, 120), (2, 60), (12, 18), (50, 4), (88, 18), (98, 60), (94, 120), (82, 116), (82, 66), (18, 66), (18, 116)])),
              L(blob([(62, 14), (96, 50), (92, 116), (84, 114)], 6), 'shade', 'b', False), strand([(50, 6), (50, 46)], 'deep', 'b', 1.2)],
    'side': [L(blob([(56, 118), (14, 120), (2, 66), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (92, 56), (76, 54), (62, 58), (58, 78), (60, 106)]))] + bob_shade('side'),
    'back': [L(blob([(6, 120), (2, 60), (12, 18), (50, 4), (88, 18), (98, 60), (94, 120), (50, 126)])), L(blob([(58, 14), (96, 50), (92, 118), (66, 124)], 6), 'shade', 'b', False)],
}
# Zenn Wildhorse: gorro de lana verde con franjas amarillas y un mechón rojo que asoma por un lado; ojos cerrados y sonrisa
CHARS['zenn-wildhorse'] = {
    'body': 'normal', 'pal': pal('#c02a1a', '#fcc890', hat='#2a6a3a', hat_d='#1e4a2a', stripe='#e8b020'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    'front': bald('front') + [L(blob([(8, 60), (6, 28), (20, 6), (50, -2), (80, 6), (94, 28), (92, 60), (50, 56)]), 'hat', 'f', ln=True),
                              L(quad((8, 34), (50, 24), (92, 34)) + quad((92, 40), (50, 30), (8, 40)), 'stripe', 'f', False),
                              L(quad((8, 50), (50, 42), (92, 50)) + quad((92, 56), (50, 48), (8, 56)), 'stripe', 'f', False)]
             + [L(outline([(46, 2), (56, -6), (64, -6), (76, 2, 1), (70, 8), (82, 22, 1), (74, 26), (80, 40, 1), (72, 42), (68, 56), (58, 66, 1), (56, 48),
                           (50, 30), (46, 14)]), 'mid', 'f', ln=True),
                L(outline([(58, 0), (70, 10), (72, 30), (64, 50), (60, 30)]), 'shade', 'f', False)],
    'side': bald('side') + [L(blob([(10, 62), (8, 26), (26, 4), (56, -4), (84, 6), (96, 30), (96, 58), (50, 58)]), 'hat', 'f', ln=True),
                            L(quad((8, 34), (50, 24), (96, 34)) + quad((96, 40), (50, 30), (8, 40)), 'stripe', 'f', False),
                            L(outline([(46, -4), (70, -2), (86, 10), (94, 30), (96, 58, 1), (88, 40), (78, 22), (60, 8)]), 'mid', 'f', ln=True)],
    'back': bald('back') + [L(blob([(8, 64), (6, 28), (20, 6), (50, -2), (80, 6), (94, 28), (92, 64), (50, 68)]), 'hat', 'f', ln=True),
                            L(quad((8, 36), (50, 28), (92, 36)) + quad((92, 42), (50, 34), (8, 42)), 'stripe', 'f', False)]
            + [L(outline([(54, -4), (36, -2), (20, 8), (10, 26), (6, 50, 1), (14, 36), (26, 22), (40, 14), (56, 6)]), 'mid', 'f', ln=True)],
}
# Maston Color: un sombrero de bruja morado pequeño y caído sobre una cara ancha sin pelo a la vista; ojos y boca de fastidio
CHARS['maston-color'] = {
    'body': 'normal', 'pal': pal('#3a2a4a', '#f8dcc0', hat='#5a4a7a', hat_d='#3e325a'),
    'face': {'eyes': 'closed', 'brows': True, 'mouth': 'frown', 'mouth_y': 94, 'face_front': WIDE_FACE, 'hairline': False},
    'front': bald('front') + [L(blob([(0, 58), (20, 46), (34, 10), (50, -16), (60, -6), (66, 10), (80, 46), (100, 58), (50, 62)]), 'hat', 'f', ln=True),
                              L(blob([(54, -6), (66, 12), (80, 46), (98, 56), (60, 56)], 5), 'hat_d', 'f', False)],
    'side': bald('side') + [L(blob([(-8, 56), (20, 44), (40, 8), (60, -12), (70, -2), (72, 10), (84, 44), (104, 58), (50, 60)]), 'hat', 'f', ln=True)],
    'back': bald('back') + [L(blob([(0, 60), (20, 48), (34, 10), (50, -16), (60, -6), (66, 10), (80, 48), (100, 60), (50, 66)]), 'hat', 'f', ln=True)],
}
# Cosimo Beck (sin modelo 3D; su retrato): melena granate con flequillo sobre un ojo y puntas abiertas a la altura de la
# barbilla, gafas de sol rectangulares oscuras
CHARS['cosimo-beck'] = {
    'body': 'normal', 'pal': pal('#8a1a2a', '#e8b880', lens='#24302a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'hairline': (60, 50)},
    'front': [L(blob(BOB_F))] + bob_shade('front') + wavy((4, 74), (14, 84), (-8, 96), -5) + wavy((86, 84), (96, 74), (108, 96), 5, light_left=False)
             + [L(blob([(14, 40), (40, 26), (62, 30), (58, 56), (48, 70), (40, 70), (36, 56), (22, 52)]), 'mid', 'f'), strand([(60, 32), (56, 56), (46, 70)], OUTC, 'f', 1.0),
                L(blob([(18, 70), (46, 70), (46, 80), (20, 80)], 4), 'lens', 'f', ln=True), L(blob([(82, 70), (54, 70), (54, 80), (80, 80)], 4), 'lens', 'f', ln=True)],
    'side': [L(blob(BOB_S))] + bob_shade('side') + [L(blob([(68, 70), (96, 70), (94, 80), (70, 80)], 4), 'lens', 'f', ln=True)],
    'back': [L(blob(BOB_B))] + bob_shade('back') + wavy((6, 80), (24, 88), (2, 102), 5) + wavy((76, 88), (94, 80), (98, 102), -5, light_left=False),
}

JK_TOP = [(-6, -24, 1), (20, -10), (30, -32, 1), (44, -16), (60, -32, 1), (68, -14), (106, -26, 1), (94, -2), (126, 0, 1), (108, 18),
          (128, 34, 1), (114, 44), (128, 64, 1), (116, 74), (126, 98, 1)]
JK_LEFT = [(-30, 86, 1), (-20, 72), (-32, 54, 1), (-18, 44), (-30, 22, 1), (-12, 20), (-26, 0, 1), (0, 4)]
CHARS['ie2-shin-teikoku-gakuen:joseph-king'] = {
    'body': 'corpulento', 'pal': pal('#8a3a14', '#f8c890', paint='#d0702a', light='#b05a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': False, 'ears': False},
    'front': [L(outline([(18, 84), (10, 134, 1), (2, 108), (-14, 126, 1), (-12, 98)] + JK_LEFT + JK_TOP
                        + [(110, 98), (110, 126, 1), (96, 108), (90, 134, 1), (82, 104), (82, 84)])),
              L(outline([(66, -12), (100, -16, 1), (96, 4), (120, 6, 1), (106, 22), (120, 38, 1), (110, 50), (118, 66, 1), (108, 80), (112, 110, 1),
                         (94, 104), (84, 84), (82, 50), (76, 20)]), 'shade', 'b', False),
              L(outline([(-4, -16, 1), (20, -2), (28, -24, 1), (36, -8), (14, 8), (-18, 8, 1), (2, 2)]), 'light', 'b', False),
              strand([(-6, 30), (6, 60), (2, 100)], 'deep', 'b', 1.2), strand([(104, 30), (96, 60), (100, 100)], 'deep', 'b', 1.2)]
             + [L(outline([(12, 66), (12, 44), (24, 30), (50, 22), (76, 30), (88, 44), (88, 66), (80, 58, 1), (72, 66, 1), (64, 56), (56, 62, 1),
                           (52, 54), (47, 92, 1), (42, 56), (34, 66, 1), (28, 58), (20, 70, 1)]), 'mid', 'f'),
                L(outline([(56, 28), (80, 36), (88, 50), (86, 64), (80, 58, 1), (72, 66, 1), (66, 48)]), 'shade', 'f', False),
                strand([(44, 30), (46, 60), (47, 88)], 'deep', 'f', 1.0), strand([(30, 34), (28, 56)], 'deep', 'f', 1.0)]
             + spk((10, 58), (22, 66), (14, 106), 4, z='f') + spk((78, 66), (90, 58), (86, 106), 4, z='f', light_left=False)
             + [L([(24, 84), (34, 79)], 'paint', 'f', False, False, 1.6), L([(26, 90), (36, 85)], 'paint', 'f', False, False, 1.6),
                L([(76, 84), (66, 79)], 'paint', 'f', False, False, 1.6), L([(74, 90), (64, 85)], 'paint', 'f', False, False, 1.6)],
    'side': [L(outline([(60, 70), (56, 100), (46, 136, 1), (36, 118), (22, 138, 1), (16, 118), (-6, 128, 1), (-2, 104), (-24, 100, 1), (-12, 84),
                        (-30, 66, 1), (-14, 56), (-30, 36, 1), (-10, 30), (-24, 6, 1), (0, 4), (4, -22, 1), (24, -12), (36, -36, 1), (48, -18),
                        (66, -40, 1), (66, -16), (84, -12), (96, 4), (97, 30), (92, 60, 1), (84, 46), (78, 58, 1), (66, 52)])),
             L(outline([(-12, 40), (8, 50), (24, 80), (32, 112), (22, 136, 1), (14, 116), (-4, 124, 1), (-2, 102), (-20, 98, 1), (-10, 80),
                        (-24, 64, 1)]), 'shade', 'b', False),
             L(outline([(10, -6), (34, -28, 1), (40, -10), (64, -32, 1), (62, -10), (40, 2)]), 'light', 'b', False),
             strand([(30, 0), (20, 60), (30, 120)], 'deep', 'b', 1.2), strand([(60, 0), (50, 60), (44, 120)], 'deep', 'b', 1.2)]
            + spk((74, 6), (94, 14), (98, 66), 5, z='f', light_left=False) + spk((60, 50), (70, 54), (62, 100), 4, z='f'),
    'back': [L(outline(JK_LEFT + JK_TOP + [(112, 104), (114, 130, 1), (96, 120), (90, 144, 1), (76, 128), (64, 148, 1), (54, 130), (40, 148, 1),
                                         (30, 128), (12, 144, 1), (6, 120), (-12, 130, 1), (-10, 104)])),
             L(outline([(64, -12), (100, -16, 1), (96, 4), (120, 6, 1), (106, 22), (120, 38, 1), (110, 50), (118, 66, 1), (108, 80), (112, 112, 1),
                        (94, 116), (86, 136, 1), (74, 120), (66, 60)]), 'shade', 'b', False),
             L(outline([(-4, -16, 1), (20, -2), (28, -24, 1), (36, -8), (14, 8), (-18, 8, 1), (2, 2)]), 'light', 'b', False)]
            + [strand([(30, 0), (24, 50), (20, 120)], 'deep', 'b', 1.2), strand([(50, -6), (50, 60), (46, 130)], 'deep', 'b', 1.2),
               strand([(72, 0), (80, 50), (84, 124)], 'deep', 'b', 1.2), strand([(10, 20), (0, 60), (2, 110)], 'deep', 'b', 1.0)],
}
# David Samford en la Redux: melena verde menta lisa hasta los hombros que se vuelve gris en las puntas, flequillo con un
# mechón entre los ojos, un parche mecánico negro con un ojo blanco y rojo sobre su ojo derecho (izquierda de la imagen) y
# su correa marrón alrededor de la cabeza; piel morena y ojo naranja
CHARS['ie2-shin-teikoku-gakuen:david-samford'] = {
    'body': 'normal', 'pal': pal('#c8ece0', '#b8804a', iris='#c85a1a', shade='#a8ccc0', grey='#c0b8b4', grey_d='#9a9290', strap='#4a3a2a', patch='#2a2a2a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 94, 'hairline': False, 'ears': False},
    'front': [L(outline([(10, 112), (2, 70), (6, 30), (20, 6), (50, -2), (80, 6), (94, 30), (98, 70), (92, 112, 1), (84, 96), (84, 60), (16, 60),
                         (18, 96)])),
              L(outline([(4, 84), (16, 84), (18, 98), (10, 112, 1), (6, 100)]), 'grey', 'b', False),
              L(outline([(84, 84), (96, 84), (94, 100), (92, 112, 1), (84, 96)]), 'grey', 'b', False),
              L(outline([(64, 6), (92, 30), (96, 70), (86, 62)]), 'shade', 'b', False),
              L(quad((12, 62), (50, 56), (88, 62)), 'strap', 'b', False, False, 2.4),
              L(ell(34, 76, 9.5, 8.5), 'patch', 'f', ln=True), L(ell(34, 76, 5, 5), WHITE, 'f', False), L(ell(34, 76, 2.2, 2.2), (190, 40, 40, 255), 'f', False),
              L(outline([(12, 66, 1), (14, 40), (30, 24), (50, 20), (70, 24), (86, 40), (88, 66, 1), (80, 58), (74, 68, 1), (66, 56), (58, 64, 1), (54, 54),
                         (49, 86, 1), (44, 56), (38, 64, 1), (30, 56), (22, 68, 1), (18, 58)]), 'mid', 'f'),
              L(outline([(60, 26), (84, 40), (86, 60), (72, 52)]), 'shade', 'f', False)]
             + spk((10, 60), (22, 64), (14, 104), 4, z='f') + spk((78, 64), (90, 60), (86, 104), 4, z='f', light_left=False),
    'side': [L(outline([(62, 70), (58, 100), (50, 120, 1), (40, 106), (30, 124, 1), (22, 108), (8, 118, 1), (6, 100), (-4, 104, 1), (2, 80), (4, 50),
                        (12, 24), (30, 6), (56, 0), (78, 8), (92, 26), (96, 50), (92, 72, 1), (84, 56), (72, 54)])),
             L(outline([(2, 84), (60, 84), (58, 100), (50, 120, 1), (40, 106), (30, 124, 1), (22, 108), (8, 118, 1), (6, 100), (-4, 104, 1)]), 'grey', 'b', False),
             L(outline([(8, 40), (30, 50), (40, 80), (20, 84)]), 'shade', 'b', False),
             L(quad((4, 50), (40, 52), (84, 60)), 'strap', 'f', False, False, 2.4),
             L(outline([(76, 66), (88, 66), (92, 84), (78, 86)]), 'patch', 'f', ln=True)]
            + spk((70, 10), (92, 22), (94, 78), 5, z='f', light_left=False),
    'back': [L(outline([(2, 76), (6, 30), (20, 6), (50, -2), (80, 6), (94, 30), (98, 76), (100, 112), (90, 132, 1), (80, 116), (70, 136, 1), (60, 118),
                        (50, 138, 1), (40, 118), (30, 136, 1), (20, 116), (10, 132, 1), (0, 112)])),
             L(outline([(0, 78), (100, 78), (100, 112), (90, 132, 1), (80, 116), (70, 136, 1), (60, 118), (50, 138, 1), (40, 118), (30, 136, 1), (20, 116),
                        (10, 132, 1), (0, 112)]), 'grey', 'b', False),
             L(outline([(64, 10), (94, 34), (98, 76), (78, 70)]), 'shade', 'b', False),
             L(outline([(70, 80), (100, 80), (98, 112), (88, 126, 1), (80, 112), (72, 90)]), 'grey_d', 'b', False),
             L(quad((4, 54), (50, 50), (96, 54)), 'strap', 'b', False, False, 2.6)],
}
