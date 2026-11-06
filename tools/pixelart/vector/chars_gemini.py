"""Tormenta de Géminis (IE2): los alienígenas de la Academia Alius; caras pintadas, casco, máscara y peinados extraños.
Casi ninguno tiene modelo 3D: sus retratos (Grant y Jordan, con modelo)."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, pal, sheen, spk, strand
from chars_otaku import back_hair
from chars_sengoku import wavy
from heads import quad

WHITE = (255, 255, 255, 255)
SIDE_SKULL = [(44, 92), (22, 88), (12, 64), (14, 36), (30, 16), (56, 10), (78, 18), (88, 36), (76, 44), (60, 48), (52, 62), (50, 80)]
SKULL_F = [(16, 64), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 64)]
SKULL_B = [(16, 70), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 70), (66, 86), (34, 86)]
WIDE_FACE = blob([(12, 54), (50, 46), (88, 54), (92, 76), (86, 96), (66, 106), (50, 108), (34, 106), (14, 96), (8, 76)])


def bald(view, c='skin', cd='skin_d'):
    if view == 'front':
        return [L(blob(SKULL_F), c), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), cd, 'b', False)]
    if view == 'side':
        return [L(blob(SIDE_SKULL), c)]
    return [L(blob(SKULL_B), c), L(blob([(58, 12), (86, 36), (84, 68), (66, 84)], 6), cd, 'b', False)]


# ------------------------------------------------------------------ Gordon Star (portero): corpulento, pelo verde azulado en
# llamas onduladas hacia arriba y a los lados, cara ancha, nariz marcada y dientes apretados
CHARS['gordon-star'] = {
    'body': 'corpulento', 'pal': pal('#2a8a9a', '#f8dcc0', nose='#6a5a4a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 94, 'face_front': WIDE_FACE, 'nose': (50, 82, 3), 'hairline': (56, 48)},
    'front': wavy((10, 40), (24, 22), (-14, 4), 8) + wavy((76, 22), (90, 40), (112, 6), -8, light_left=False) + wavy((30, 16), (50, 8), (24, -20), 8)
             + wavy((50, 8), (70, 14), (78, -18), -8, light_left=False) + wavy((4, 60), (10, 44), (-18, 48), 6) + wavy((90, 44), (96, 60), (118, 50), -6, light_left=False)
             + [L(blob([(10, 64), (8, 36), (20, 14), (50, 6), (80, 14), (92, 36), (90, 64)])),
                L(blob([(62, 12), (90, 34), (88, 62), (76, 58)], 6), 'shade', 'b', False), sheen(24, 48, 14, 3)]
             + wavy((20, 42), (40, 36), (14, 60), 5, z='f') + wavy((60, 36), (80, 42), (86, 60), -5, z='f', light_left=False),
    'side': wavy((20, 26), (40, 12), (-6, 0), 8) + wavy((40, 12), (62, 6), (44, -22), 8) + wavy((14, 50), (18, 30), (-18, 36), 7) + wavy((16, 70), (18, 52), (-14, 70), 6)
            + [L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False)]
            + wavy((56, 28), (86, 36), (96, 56), -5, z='f', light_left=False),
    'back': wavy((10, 40), (24, 22), (-14, 4), 8) + wavy((76, 22), (90, 40), (112, 6), -8, light_left=False) + wavy((30, 16), (50, 8), (24, -20), 8)
            + wavy((50, 8), (70, 14), (78, -18), -8, light_left=False) + wavy((4, 60), (10, 44), (-18, 48), 6) + wavy((90, 44), (96, 60), (118, 50), -6, light_left=False)
            + [L(blob(SKULL_B))] + back_hair(),
}

# ------------------------------------------------------------------ Connor Shuttle: piel verde de alienígena, pelo azul marino en
# tentáculos curvados hacia arriba y a los lados, orejas puntiagudas y ojos blancos sin pupila
CHARS['connor-shuttle'] = {
    'body': 'normal', 'pal': pal('#2a4a8a', '#5aa880'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 92, 'big_ears': 1, 'ear_out': 4, 'hairline': (52, 44)},
    'front': wavy((20, 22), (30, 16), (8, -18), 6) + wavy((70, 16), (80, 22), (92, -18), -6, light_left=False)
             + wavy((36, 12), (46, 8), (34, -22), 5) + wavy((54, 8), (64, 12), (66, -22), -5, light_left=False)
             + wavy((10, 52), (16, 42), (-16, 50), 6) + wavy((84, 42), (90, 52), (116, 50), -6, light_left=False)
             + [L(blob([(12, 60), (10, 34), (22, 14), (50, 6), (78, 14), (90, 34), (88, 60)])),
                L(blob([(62, 12), (88, 34), (86, 58), (74, 54)], 6), 'shade', 'b', False),
                L(blob([(28, 72), (44, 70), (42, 79), (30, 79)], 4), WHITE, 'f', ln=True), L(blob([(72, 72), (56, 70), (58, 79), (70, 79)], 4), WHITE, 'f', ln=True)],
    'side': wavy((24, 18), (40, 10), (10, -14), 6) + wavy((40, 10), (58, 8), (52, -20), 5) + wavy((14, 50), (18, 36), (-16, 40), 6)
            + [L(blob(SIDE_SKULL)), L(blob([(78, 72), (90, 71), (89, 79), (80, 79)], 4), WHITE, 'f', ln=True)],
    'back': wavy((20, 22), (30, 16), (8, -18), 6) + wavy((70, 16), (80, 22), (92, -18), -6, light_left=False)
            + wavy((36, 12), (46, 8), (34, -22), 5) + wavy((54, 8), (64, 12), (66, -22), -5, light_left=False)
            + wavy((10, 52), (16, 42), (-16, 50), 6) + wavy((84, 42), (90, 52), (116, 50), -6, light_left=False)
            + [L(blob(SKULL_B))] + back_hair(),
}

# ------------------------------------------------------------------ Jim Landing: corpulento, piel rosada, calvo con una cresta roja
# corta, ojos pequeños y furiosos y dientes apretados
CHARS['jim-landing'] = {
    'body': 'corpulento', 'pal': pal('#c02a1a', '#ec9a84', iris='#e0a020'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 94, 'face_front': WIDE_FACE, 'big_ears': 1, 'hairline': False},
    'front': bald('front') + spk((40, 10), (58, 8), (44, -16), 6) + spk((52, 8), (62, 12), (66, -8), 4, light_left=False),
    'side': bald('side') + spk((34, 12), (54, 6), (30, -14), 6) + spk((50, 8), (66, 10), (58, -12), 5, light_left=False),
    'back': bald('back') + spk((40, 10), (58, 8), (44, -16), 6),
}

# ------------------------------------------------------------------ Charles Riverboat: piel morena, melena gris azulado enorme y
# ondulada hasta los hombros, un parche en un ojo y una sonrisa enorme
CHARS['charles-riverboat'] = {
    'body': 'normal', 'pal': pal('#4e5c66', '#c09068'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 92, 'hairline': (56, 46)},
    'front': [L(bumpy(50, 50, 52, 50, 16, 0.07)), L(bumpy(70, 54, 24, 38, 8, 0.07), 'shade', 'b', False), L(ell(30, 16, 10, 4), 'light', 'b', False),
              L(blob([(14, 50), (20, 40), (50, 34), (80, 40), (86, 50), (60, 46), (40, 46)]), 'mid', 'f'),
              L(ell(64, 75, 8, 6.4), (24, 20, 24, 255), 'f', ln=True), L([(56, 72), (88, 60)], (24, 20, 24, 255), 'f', False, False, 1.2)],
    'side': [L(bumpy(40, 50, 50, 50, 16, 0.07)), L(blob(SIDE_SKULL)), L(bumpy(24, 56, 20, 36, 8, 0.07), 'shade', 'b', False),
             spk((56, 30), (86, 40), (92, 64), 5, z='f', light_left=False)],
    'back': [L(bumpy(50, 52, 52, 52, 16, 0.07)), L(bumpy(68, 58, 24, 40, 8, 0.07), 'shade', 'b', False), L(ell(30, 16, 10, 4), 'light', 'b', False)],
}

# ------------------------------------------------------------------ Jordan Greenway (Reize): pelo verde claro con flequillo de
# mechones y una coleta alta larga que cae por detrás
CHARS['jordan-greenway'] = {
    'body': 'normal', 'pal': pal('#a8b850', '#fcc490', iris='#3a2a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': (60, 50)},
    'front': wavy((52, 10), (66, 8), (90, -14), -6, light_left=False)
             + [L(blob([(10, 80), (6, 44), (16, 14), (50, 4), (84, 14), (94, 44), (90, 80), (80, 74), (80, 60), (20, 60), (20, 74)])),
              L(blob([(62, 12), (92, 42), (88, 78), (82, 76)], 6), 'shade', 'b', False), sheen(22, 48, 14, 3),
              spk((12, 44), (30, 36), (18, 82), 4, z='f'), spk((30, 36), (50, 30), (40, 62), 5, z='f'),
              spk((50, 30), (70, 36), (60, 62), 5, z='f', light_left=False), spk((70, 36), (88, 44), (82, 82), 4, z='f', light_left=False)],
    'side': wavy((24, 18), (30, 30), (-14, 104), 8)
            + [L(blob([(48, 92), (16, 88), (6, 60), (10, 28), (28, 8), (58, 4), (82, 14), (94, 34), (92, 56), (76, 54), (62, 56), (56, 72), (52, 88)])),
               L(blob([(10, 50), (12, 84), (40, 88), (26, 64)], 6), 'shade', 'b', False), sheen(30, 62, 12, 3),
               spk((56, 30), (88, 40), (92, 76), 6, z='f', light_left=False)],
    'back': [L(blob([(10, 82), (6, 44), (16, 14), (50, 4), (84, 14), (94, 44), (90, 82), (50, 88)])),
             L(blob([(58, 12), (92, 42), (88, 80), (66, 86)], 6), 'shade', 'b', False), sheen(22, 48, 14, 3)]
            + wavy((40, 20), (60, 20), (44, 122), -8, z='f'),
}

# ------------------------------------------------------------------ Pat Box: chica de piel muy pálida, pelo morado oscuro recogido
# en un moño alto con mechones que caen junto a la cara, un adorno en la frente y rayas rojas en las mejillas
CHARS['pat-box'] = {
    'body': 'chica', 'pal': pal('#3a2440', '#f6ece4', iris='#2a8a6a', mark='#c03a2a', gem='#a8c8d8'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 92, 'big_ears': 1, 'ear_out': 3, 'hairline': (60, 46)},
    'front': [L(bumpy(50, 2, 14, 12, 8, 0.08)),
              L(blob([(14, 64), (12, 36), (24, 14), (50, 6), (76, 14), (88, 36), (86, 64)])),
              L(blob([(60, 12), (86, 34), (84, 62), (72, 58)], 6), 'shade', 'b', False), sheen(28, 52, 14, 3),
              L(quad((18, 56), (14, 80), (22, 100)), 'mid', 'f', False, False, 2.4), L(quad((82, 56), (86, 80), (78, 100)), 'mid', 'f', False, False, 2.4),
              L(ell(50, 58, 2.6, 2.6), 'gem', 'f', ln=True),
              L([(24, 84), (32, 82)], 'mark', 'f', False, False, 1.4), L([(24, 88), (32, 86)], 'mark', 'f', False, False, 1.4),
              L([(76, 84), (68, 82)], 'mark', 'f', False, False, 1.4), L([(76, 88), (68, 86)], 'mark', 'f', False, False, 1.4)],
    'side': [L(bumpy(40, 0, 14, 12, 8, 0.08)), L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             L(quad((56, 56), (52, 78), (60, 100)), 'mid', 'f', False, False, 2.4), L([(78, 84), (84, 82)], 'mark', 'f', False, False, 1.4)],
    'back': [L(bumpy(50, 4, 14, 12, 8, 0.08)), L(blob(SKULL_B))] + back_hair(),
}

# ------------------------------------------------------------------ Gregory Saturn: un casco de astronauta blanco con la visera
# verde enorme, en la que brilla una cara maligna de ojos y sonrisa blancos
CHARS['gregory-saturn'] = {
    'body': 'normal', 'pal': pal('#2a2a2a', '#f6c08e', helm='#e8e8ec', helm_d='#a8a8b4', visor='#8ac820', visor_d='#5a9a10'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'ears': False, 'hairline': False},
    'front': [L(blob([(2, 100), (0, 50), (12, 14), (50, 0), (88, 14), (100, 50), (98, 100), (50, 110)]), 'helm', 'f', ln=True),
              L(blob([(64, 6), (98, 50), (96, 98), (78, 104)], 6), 'helm_d', 'f', False),
              L(blob([(10, 60), (14, 30), (50, 16), (86, 30), (90, 60), (80, 92), (50, 100), (20, 92)]), 'visor', 'f', ln=True),
              L(blob([(60, 22), (86, 34), (88, 62), (72, 86)], 6), 'visor_d', 'f', False),
              L([(26, 48), (44, 56), (30, 60)], WHITE, 'f', False), L([(74, 48), (56, 56), (70, 60)], WHITE, 'f', False),
              L(quad((26, 70), (50, 90), (74, 70)) + quad((74, 70), (50, 80), (26, 70))[1:], WHITE, 'f', False),
              L([(-4, 60), (4, 56), (6, 76), (-2, 78)], 'helm_d', 'f', ln=True), L([(104, 60), (96, 56), (94, 76), (102, 78)], 'helm_d', 'f', ln=True)],
    'side': [L(blob([(10, 104), (0, 60), (6, 20), (34, 0), (66, 0), (92, 16), (102, 50), (100, 96), (60, 112)]), 'helm', 'f', ln=True),
             L(blob([(60, 22), (92, 30), (100, 60), (90, 90), (64, 96), (56, 60)]), 'visor', 'f', ln=True),
             L([(80, 48), (94, 54), (84, 58)], WHITE, 'f', False), L(quad((72, 72), (88, 86), (98, 72)), WHITE, 'f', False, False, 1.6),
             L([(24, 56), (34, 54), (34, 76), (24, 78)], 'helm_d', 'f', ln=True)],
    'back': [L(blob([(2, 100), (0, 50), (12, 14), (50, 0), (88, 14), (100, 50), (98, 100), (50, 110)]), 'helm', 'f', ln=True),
             L(blob([(58, 6), (98, 50), (96, 98), (70, 106)], 6), 'helm_d', 'f', False)],
}

# ------------------------------------------------------------------ Izzy Jupiter: máscara blanca con unas gafas redondas de bronce
# y una sonrisa pintada; pelo naranja de pinchos en todas direcciones alrededor de la máscara
IZZY_TOP = [spk((4, 58), (10, 40), (-18, 40), 7), spk((12, 36), (26, 18), (-4, -2), 7), spk((28, 16), (46, 8), (30, -18), 7),
            spk((46, 8), (62, 10), (64, -18), 7, light_left=False), spk((64, 14), (80, 24), (102, 2), 7, light_left=False),
            spk((84, 30), (94, 48), (118, 38), 7, light_left=False), spk((92, 54), (96, 72), (116, 74), 5, light_left=False),
            spk((4, 72), (8, 56), (-14, 74), 5)]
CHARS['izzy-jupiter'] = {
    'body': 'normal', 'pal': pal('#d8601a', '#f6c08e', mask='#ece4d4', mask_d='#c0b4a0', rim='#8a7a3a', lens='#c8b880'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'ears': False, 'hairline': False},
    'front': IZZY_TOP + [L(blob([(10, 70), (8, 38), (20, 14), (50, 6), (80, 14), (92, 38), (90, 70)])),
                         L(blob([(62, 12), (90, 36), (88, 66), (78, 62)], 6), 'shade', 'b', False),
                         L(blob([(20, 40), (50, 30), (80, 40), (84, 70), (72, 96), (50, 104), (28, 96), (16, 70)]), 'mask', 'f', ln=True),
                         L(blob([(56, 34), (80, 42), (82, 70), (66, 96)], 6), 'mask_d', 'f', False),
                         L(ell(36, 62, 9, 8), 'rim', 'f', ln=True), L(ell(64, 62, 9, 8), 'rim', 'f', ln=True),
                         L(ell(36, 62, 6, 5.4), 'lens', 'f', False), L(ell(64, 62, 6, 5.4), 'lens', 'f', False),
                         L(quad((32, 84), (50, 94), (68, 84)), OUTC, 'f', False, False, 1.6)],
    'side': [spk((16, 40), (24, 22), (-20, 14), 8), spk((24, 24), (42, 12), (8, -20), 8), spk((42, 12), (62, 6), (58, -24), 8),
             spk((14, 58), (16, 40), (-20, 50), 7), spk((18, 76), (22, 58), (-14, 82), 6),
             L(blob(SIDE_SKULL)), L(blob([(62, 36), (92, 44), (96, 74), (86, 100), (66, 102), (60, 70)]), 'mask', 'f', ln=True),
             L(ell(88, 62, 5, 7), 'rim', 'f', ln=True), L(quad((80, 86), (90, 92), (96, 84)), OUTC, 'f', False, False, 1.4)],
    'back': IZZY_TOP + [L(blob(SKULL_B), 'mid'), L(blob([(58, 12), (86, 36), (84, 68), (66, 84)], 6), 'shade', 'b', False)]
            + [spk((14, 72), (32, 84), (10, 96), 5), spk((32, 84), (50, 88), (40, 104), 5), spk((50, 88), (68, 84), (60, 104), 5, light_left=False),
               spk((68, 84), (86, 72), (90, 96), 5, light_left=False)],
}

# ------------------------------------------------------------------ Rhona Countdown: piel morena, melena rosa salmón que le tapa
# medio rostro con una antena de pelo en forma de cuerno de ciervo, ojo izquierdo pintado de negro
CHARS['rhona-countdown'] = {
    'body': 'chica', 'pal': pal('#e88a7a', '#b07a54', iris='#2a2a2a', paint='#1e1a1e'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'line', 'mouth_y': 92, 'hairline': (60, 52)},
    'front': [spk((40, 10), (48, 8), (20, -22), 3), spk((28, -2), (32, -6), (16, -14), 2.5), spk((34, 4), (38, 0), (40, -16), 2.5),
              L(blob([(8, 90), (4, 50), (14, 16), (50, 6), (86, 16), (96, 50), (92, 90), (80, 86), (80, 62), (20, 62), (20, 86)])),
              L(blob([(62, 12), (94, 46), (90, 88), (82, 86)], 6), 'shade', 'b', False), sheen(22, 48, 16, 3),
              L(ell(64, 75, 8, 7), 'paint', 'f', False),
              L(blob([(10, 40), (36, 28), (54, 32), (50, 70), (42, 92), (30, 96), (26, 72), (14, 58)]), 'mid', 'f'),
              L(blob([(36, 34), (50, 36), (44, 76), (36, 90), (34, 60)], 5), 'shade', 'f', False),
              strand([(52, 34), (48, 70), (38, 94)], OUTC, 'f', 1.0), spk((60, 36), (84, 42), (84, 70), 5, z='f', light_left=False)],
    'side': [spk((34, 8), (42, 6), (18, -20), 3),
             L(blob([(48, 94), (14, 92), (2, 62), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (92, 56), (76, 54), (62, 56), (56, 72), (52, 90)])),
             L(blob([(6, 50), (8, 88), (40, 92), (24, 64)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             spk((56, 30), (90, 40), (92, 80), 6, z='f', light_left=False)],
    'back': [spk((40, 10), (48, 8), (20, -22), 3),
             L(blob([(8, 92), (4, 50), (14, 16), (50, 6), (86, 16), (96, 50), (92, 92), (50, 98)])),
             L(blob([(58, 12), (94, 46), (90, 90), (66, 96)], 6), 'shade', 'b', False), sheen(22, 48, 16, 3)],
}

# ------------------------------------------------------------------ Dylan Bluemoon (Diam): pelo castaño con dos alas puntiagudas
# muy grandes a los lados y flequillo partido; ojos verde azulado y ceño
CHARS['dylan-bluemoon'] = {
    'body': 'normal', 'pal': pal('#6a4628', '#fce8c4', iris='#3a8a8a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 92, 'hairline': (60, 50)},
    'front': [spk((8, 50), (16, 34), (-20, 22), 6), spk((84, 34), (92, 50), (120, 22), 6, light_left=False),
              spk((10, 74), (14, 58), (-14, 80), 5), spk((86, 58), (90, 74), (114, 80), 5, light_left=False),
              L(blob([(10, 84), (6, 44), (18, 12), (50, 2), (82, 12), (94, 44), (90, 84), (80, 80), (80, 60), (20, 60), (20, 80)])),
              L(blob([(62, 10), (92, 42), (88, 82), (80, 80)], 6), 'shade', 'b', False), sheen(22, 48, 12, 3),
              spk((14, 44), (34, 34), (24, 72), 5, z='f'), spk((34, 32), (50, 28), (44, 58), 4, z='f'),
              spk((50, 28), (66, 32), (56, 58), 4, z='f', light_left=False), spk((66, 34), (86, 44), (76, 72), 5, z='f', light_left=False)],
    'side': [spk((16, 40), (22, 24), (-20, 14), 7), spk((14, 66), (18, 50), (-16, 70), 6),
             L(blob([(48, 92), (16, 88), (6, 60), (10, 28), (28, 6), (58, 2), (82, 12), (94, 34), (92, 56), (76, 54), (62, 56), (56, 72), (52, 88)])),
             L(blob([(10, 50), (12, 84), (40, 88), (26, 64)], 6), 'shade', 'b', False), sheen(30, 62, 10, 3),
             spk((56, 30), (88, 40), (90, 72), 6, z='f', light_left=False)],
    'back': [spk((8, 50), (16, 34), (-20, 22), 6), spk((84, 34), (92, 50), (120, 22), 6, light_left=False),
             spk((10, 74), (14, 58), (-14, 80), 5), spk((86, 58), (90, 74), (114, 80), 5, light_left=False),
             L(blob([(10, 86), (6, 44), (18, 12), (50, 2), (82, 12), (94, 44), (90, 86), (50, 92)])),
             L(blob([(58, 10), (92, 42), (88, 84), (66, 90)], 6), 'shade', 'b', False), sheen(22, 48, 12, 3)],
}

# ------------------------------------------------------------------ Grant Icewater: piel morena, pelo verde oscuro con dos cuernos
# de punta hacia arriba y mechones a los lados, ojos redondos blancos sin pupila, orejas grandes y un colmillo
CHARS['grant-icewater'] = {
    'body': 'corpulento', 'pal': pal('#3a6a3a', '#a07858'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'buck', 'mouth_y': 94, 'big_ears': 1.5, 'ear_out': 3, 'nose': (50, 82, 3), 'hairline': (54, 44)},
    'front': [spk((22, 22), (34, 16), (26, -22), 3.5), spk((66, 16), (78, 22), (76, -22), 3.5, light_left=False),
              spk((8, 46), (14, 34), (-6, 28), 4), spk((86, 34), (92, 46), (106, 28), 4, light_left=False),
              L(blob([(10, 60), (8, 34), (22, 14), (50, 8), (78, 14), (92, 34), (90, 60)])),
              L(blob([(62, 14), (90, 34), (88, 58), (76, 54)], 6), 'shade', 'b', False),
              spk((10, 56), (20, 56), (12, 82), 4, z='f'), spk((80, 56), (90, 56), (88, 82), 4, z='f', light_left=False),
              L(ell(36, 74, 5.4, 5), WHITE, 'f', ln=True), L(ell(64, 74, 5.4, 5), WHITE, 'f', ln=True)],
    'side': [spk((34, 14), (52, 8), (46, -20), 5), L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((14, 56), (24, 56), (16, 84), 4), L(ell(84, 74, 3.6, 5), WHITE, 'f', ln=True)],
    'back': [spk((22, 22), (34, 16), (26, -22), 3.5), spk((66, 16), (78, 22), (76, -22), 3.5, light_left=False), L(blob(SKULL_B))] + back_hair(),
}
