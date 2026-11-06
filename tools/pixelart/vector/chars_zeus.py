"""Zeus (IE1): los "dioses" del Instituto Zeus: casco griego, máscara, maquillaje de payaso, rastas, melenas largas y
cintas en la frente, con sus modelos 3D como referencia (Ned Yousef no tiene modelo: su retrato)."""
from chars import CHARS, L, OUTC, blob, bumpy, dread, ell, pal, sheen, spk, strand
from chars_otaku import back_hair
from chars_sengoku import wavy
from heads import quad

WHITE = (255, 255, 255, 255)
SIDE_SKULL = [(44, 92), (22, 88), (12, 64), (14, 36), (30, 16), (56, 10), (78, 18), (88, 36), (76, 44), (60, 48), (52, 62), (50, 80)]
SKULL_F = [(16, 64), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 64)]
SKULL_B = [(16, 70), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 70), (66, 86), (34, 86)]


def bald(view):
    if view == 'front':
        return [L(blob(SKULL_F), 'skin'), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'skin_d', 'b', False)]
    if view == 'side':
        return [L(blob(SIDE_SKULL), 'skin')]
    return [L(blob(SKULL_B), 'skin'), L(blob([(58, 12), (86, 36), (84, 68), (66, 84)], 6), 'skin_d', 'b', False)]


# ------------------------------------------------------------------ Paul Siddon (portero): corpulento, cabeza rapada con una
# corona de rastas cortas verde azulado que salen de la coronilla y caen alrededor como serpientes; ceño y muecas
def paul_dreads(view):
    if view == 'side':
        ends = [((40, 14), (8, 34)), ((36, 18), (-4, 56)), ((32, 22), (2, 80)), ((44, 12), (24, 2)), ((52, 12), (72, 8)), ((38, 20), (16, 70))]
    elif view == 'front':
        ends = [((24, 26), (2, 40)), ((20, 36), (-2, 56)), ((22, 48), (4, 68)), ((76, 26), (98, 40)), ((80, 36), (102, 56)), ((78, 48), (96, 68)),
                ((42, 12), (30, 2)), ((58, 12), (70, 2))]
    else:
        ends = [((24, 26), (2, 40)), ((20, 36), (-2, 56)), ((22, 48), (4, 68)), ((76, 26), (98, 40)), ((80, 36), (102, 56)), ((78, 48), (96, 68)),
                ((40, 20), (32, 60)), ((50, 20), (50, 64)), ((60, 20), (68, 60))]
    return [x for p0, p1 in ends for x in dread(p0, p1, 3.6)]


CHARS['paul-siddon'] = {
    'body': 'corpulento', 'pal': pal('#4a8a7a', '#f0b068', crown='#7a8a80'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 92, 'big_ears': 1, 'ear_out': 3, 'hairline': False},
    'front': bald('front') + [L(ell(50, 14, 12, 6), 'crown', 'b', ln=True)] + paul_dreads('front'),
    'side': bald('side') + [L(ell(44, 14, 10, 6), 'crown', 'b', ln=True)] + paul_dreads('side'),
    'back': bald('back') + [L(ell(50, 14, 12, 6), 'crown', 'b', ln=True)] + paul_dreads('back'),
}

# ------------------------------------------------------------------ Apollo Light: pelo verde oliva rizado y despeinado con una
# cinta blanca en lo alto de la cabeza; cicatriz en la mejilla y sonrisa
CHARS['apollo-light'] = {
    'body': 'normal', 'pal': pal('#6a7030', '#fcd2a6', band='#f4f4f4', band_d='#c8c8cc', scar='#c07a5a'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 92, 'hairline': (60, 50)},
    'front': [L(bumpy(50, 38, 46, 34, 14, 0.07)), L(bumpy(10, 62, 10, 12, 6, 0.1)), L(bumpy(90, 62, 10, 12, 6, 0.1)),
              L(bumpy(68, 42, 22, 24, 8, 0.07), 'shade', 'b', False), L(ell(30, 18, 10, 4), 'light', 'b', False),
              L(quad((10, 30), (50, 12), (90, 30)) + quad((90, 38), (50, 20), (10, 38)), 'band', 'f', ln=True),
              spk((12, 46), (30, 40), (18, 70), 5, z='f'), spk((30, 40), (48, 38), (40, 62), 5, z='f'),
              spk((52, 38), (70, 40), (60, 62), 5, z='f', light_left=False), spk((70, 42), (88, 46), (84, 70), 5, z='f', light_left=False),
              L([(66, 84), (72, 80)], 'scar', 'f', False, False, 1.2), L([(66, 80), (70, 86)], 'scar', 'f', False, False, 1.0)],
    'side': [L(bumpy(44, 40, 44, 34, 14, 0.07)), L(bumpy(12, 64, 12, 14, 6, 0.1)),
             L(bumpy(28, 50, 20, 22, 8, 0.07), 'shade', 'b', False),
             L(quad((22, 22), (50, 8), (80, 18)) + quad((80, 26), (50, 16), (22, 30)), 'band', 'f', ln=True),
             spk((56, 30), (88, 40), (92, 68), 6, z='f', light_left=False)],
    'back': [L(bumpy(50, 42, 46, 38, 14, 0.07)), L(bumpy(10, 64, 10, 12, 6, 0.1)), L(bumpy(90, 64, 10, 12, 6, 0.1)),
             spk((20, 76), (38, 86), (24, 98), 4), spk((38, 86), (56, 88), (46, 100), 4), spk((56, 88), (74, 84), (70, 98), 4, light_left=False),
             L(bumpy(66, 52, 22, 26, 8, 0.07), 'shade', 'b', False), L(ell(30, 20, 10, 4), 'light', 'b', False),
             L(quad((10, 30), (50, 12), (90, 30)) + quad((90, 38), (50, 20), (10, 38)), 'band', 'f', ln=True)],
}

# ------------------------------------------------------------------ Jeff Iron: piel morena, melena azul marino ondulada hasta
# los hombros con una cinta dorada fina en la frente; ojos verdes afilados
CHARS['jeff-iron'] = {
    'body': 'normal', 'pal': pal('#2e3466', '#a86a3a', iris='#7aa86a', gold='#d8b860'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 92, 'hairline': (58, 50)},
    'front': [L(blob([(4, 100), (-2, 60), (8, 22), (50, 6), (92, 22), (102, 60), (96, 100), (82, 96), (82, 62), (18, 62), (18, 96)])),
              L(bumpy(2, 84, 10, 14, 6, 0.1)), L(bumpy(98, 84, 10, 14, 6, 0.1)), L(bumpy(4, 64, 8, 10, 6, 0.1)), L(bumpy(96, 64, 8, 10, 6, 0.1)),
              L(blob([(62, 12), (98, 46), (96, 96), (84, 94)], 6), 'shade', 'b', False), sheen(22, 48, 20, 3),
              L(quad((14, 54), (50, 46), (86, 54)), 'gold', 'f', False, False, 1.8),
              wavy((14, 42), (30, 36), (18, 70), -4, z='f'), wavy((70, 36), (86, 42), (84, 70), 4, z='f', light_left=False),
              L(blob([(34, 34), (66, 34), (60, 42), (50, 46), (40, 42)], 5), 'mid', 'f')],
    'side': [L(blob([(48, 100), (10, 102), (-4, 62), (2, 28), (24, 8), (56, 4), (82, 14), (94, 34), (92, 58), (76, 56), (62, 58), (58, 74), (56, 96)])),
             L(bumpy(2, 86, 10, 14, 6, 0.1)), L(bumpy(20, 98, 12, 10, 6, 0.1)),
             L(blob([(4, 50), (6, 92), (40, 98), (24, 66)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             L(quad((10, 44), (50, 40), (92, 48)), 'gold', 'f', False, False, 1.8),
             wavy((56, 30), (90, 40), (92, 72), 6, z='f', light_left=False)],
    'back': [L(blob([(4, 100), (-2, 60), (8, 22), (50, 6), (92, 22), (102, 60), (96, 100), (50, 106)])),
             L(bumpy(10, 100, 12, 10, 6, 0.1)), L(bumpy(50, 104, 14, 10, 6, 0.1)), L(bumpy(90, 100, 12, 10, 6, 0.1)),
             L(blob([(58, 12), (98, 46), (96, 98), (66, 104)], 6), 'shade', 'b', False), sheen(22, 48, 20, 3),
             L(quad((4, 46), (50, 38), (96, 46)), 'gold', 'f', False, False, 1.8)],
}

# ------------------------------------------------------------------ Lane War: melena roja con un flequillo grande que le tapa un
# ojo y una trenza gruesa atada que le cae por delante del hombro
CHARS['lane-war'] = {
    'body': 'normal', 'pal': pal('#b02a10', '#f2b884'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 93, 'hairline': (60, 50)},
    'front': [L(blob([(10, 84), (6, 46), (16, 14), (50, 4), (84, 14), (94, 46), (90, 84), (80, 80), (80, 60), (20, 60), (20, 80)])),
              L(blob([(62, 12), (92, 46), (90, 82), (82, 80)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
              strand([(58, 6), (40, 46)], 'deep', 'b', 1.0),
              L(blob([(16, 36), (40, 26), (58, 30), (54, 60), (44, 86), (34, 90), (30, 70), (20, 56)]), 'mid', 'f'),
              L(blob([(40, 32), (54, 34), (48, 72), (40, 86), (38, 60)], 5), 'shade', 'f', False),
              strand([(56, 32), (52, 62), (42, 88)], OUTC, 'f', 1.0),
              L(bumpy(80, 92, 7, 6, 6, 0.1), 'mid', 'f', ln=True), L(bumpy(80, 104, 7, 6, 6, 0.1), 'mid', 'f', ln=True),
              L(blob([(76, 108), (86, 108), (84, 124), (78, 128)]), 'mid', 'f', ln=True)],
    'side': [L(blob([(46, 92), (14, 90), (2, 60), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (92, 58), (76, 56), (62, 58), (56, 74), (52, 88)])),
             L(blob([(6, 50), (8, 86), (40, 90), (24, 64)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             L(bumpy(6, 70, 8, 7, 6, 0.1), 'mid', 'b', ln=True), L(bumpy(-2, 78, 7, 6, 6, 0.1), 'mid', 'b', ln=True),
             wavy((56, 30), (92, 40), (92, 80), 8, z='f', light_left=False)],
    'back': [L(blob([(10, 86), (6, 46), (16, 14), (50, 4), (84, 14), (94, 46), (90, 86), (50, 92)])),
             L(blob([(58, 12), (92, 46), (90, 84), (66, 90)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
             strand([(50, 6), (50, 70)], 'deep', 'b', 1.0),
             L(bumpy(22, 86, 8, 7, 6, 0.1), 'mid', 'f', ln=True), L(bumpy(18, 98, 7, 6, 6, 0.1), 'mid', 'f', ln=True)],
}

# ------------------------------------------------------------------ Danny Wood: corpulento, piel tostada, trenzas pegadas al cráneo
# de delante atrás (cresta castaña) con los lados rapados; rayas de pintura de guerra en las mejillas y sonrisa con dientes
CHARS['danny-wood'] = {
    'body': 'corpulento', 'pal': pal('#4a3020', '#e0a050', paint='#5a3a20'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 92, 'hairline': [(10, 50), (30, 48), (32, 40), (68, 40), (70, 48), (90, 50)]},
    'front': bald('front') + [L(blob([(30, 46), (28, 20), (36, 6), (50, 2), (64, 6), (72, 20), (70, 46), (50, 42)]))]
             + [strand([(x, 6 + abs(x - 50) * 0.3), (x + (x - 50) * 0.1, 44)], 'deep', 'b', 1.2) for x in (36, 43, 50, 57, 64)]
             + [L([(22, 82), (34, 82)], 'paint', 'f', False, False, 1.8), L([(24, 87), (34, 87)], 'paint', 'f', False, False, 1.8),
                L([(78, 82), (66, 82)], 'paint', 'f', False, False, 1.8), L([(76, 87), (66, 87)], 'paint', 'f', False, False, 1.8)],
    'side': bald('side') + [L(blob([(30, 60), (18, 40), (24, 16), (44, 4), (66, 4), (84, 14), (90, 30), (70, 26), (48, 26), (34, 44)]))]
            + [strand([(84, 18 + k * 3), (50, 10 + k * 5), (26, 30 + k * 8)], 'deep', 'b', 1.2) for k in range(3)]
            + [L([(76, 82), (86, 82)], 'paint', 'f', False, False, 1.8), L([(78, 87), (86, 87)], 'paint', 'f', False, False, 1.8)],
    'back': bald('back') + [L(blob([(30, 82), (28, 20), (36, 6), (50, 2), (64, 6), (72, 20), (70, 82), (50, 86)]))]
            + [strand([(x, 6 + abs(x - 50) * 0.3), (x, 82)], 'deep', 'b', 1.2) for x in (36, 43, 50, 57, 64)],
}

# ------------------------------------------------------------------ Artie Mishman: pelo verde grisáceo con las puntas hacia fuera
# y la cara tapada por una máscara blanca con ojos cerrados pintados
ARTIE_MASK = blob([(18, 54), (50, 46), (82, 54), (84, 78), (76, 96), (50, 104), (24, 96), (16, 78)])
CHARS['artie-mishman'] = {
    'body': 'normal', 'pal': pal('#4a6a50', '#f6c08e', mask='#ece8e0', mask_d='#c8c4bc'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': (60, 50)},
    'front': [L(blob([(6, 70), (2, 44), (14, 16), (50, 6), (86, 16), (98, 44), (94, 70), (82, 64), (18, 64)])),
              spk((4, 58), (12, 68), (0, 76), 3), spk((88, 68), (96, 58), (100, 76), 3, light_left=False),
              L(blob([(62, 12), (96, 44), (92, 68), (84, 66)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
              L(ARTIE_MASK, 'mask', 'f', ln=True), L(blob([(62, 52), (82, 56), (82, 80), (72, 96), (64, 80)], 6), 'mask_d', 'f', False),
              L(quad((28, 72), (36, 66), (44, 72)), OUTC, 'f', False, False, 1.4), L(quad((56, 72), (64, 66), (72, 72)), OUTC, 'f', False, False, 1.4),
              L(quad((28, 72), (36, 78), (44, 72)), OUTC, 'f', False, False, 1.2), L(quad((56, 72), (64, 78), (72, 72)), OUTC, 'f', False, False, 1.2),
              L([(46, 92), (54, 92)], OUTC, 'f', False, False, 1.2), L([(48, 82), (50, 86)], 'mask_d', 'f', False, False, 1.2),
              spk((14, 40), (34, 34), (20, 58), 5, z='f'), spk((34, 34), (52, 32), (44, 54), 5, z='f'),
              spk((50, 32), (68, 34), (60, 54), 5, z='f', light_left=False), spk((66, 36), (86, 40), (82, 58), 5, z='f', light_left=False)],
    'side': [L(blob([(46, 92), (14, 90), (2, 60), (6, 28), (26, 8), (56, 4), (82, 14), (96, 34), (92, 54), (76, 52), (62, 56), (56, 72), (52, 88)])),
             spk((4, 62), (12, 72), (0, 80), 3),
             L(blob([(6, 50), (8, 86), (40, 90), (24, 64)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             L(blob([(66, 50), (92, 54), (94, 80), (88, 98), (72, 104), (66, 80)]), 'mask', 'f', ln=True),
             L(quad((80, 72), (85, 68), (90, 72)), OUTC, 'f', False, False, 1.4),
             spk((56, 30), (92, 40), (94, 56), 5, z='f', light_left=False)],
    'back': [L(blob([(6, 72), (2, 44), (14, 16), (50, 6), (86, 16), (98, 44), (94, 72), (50, 80)])),
             spk((4, 58), (12, 68), (0, 76), 3), spk((88, 68), (96, 58), (100, 76), 3, light_left=False),
             spk((14, 70), (32, 80), (14, 92), 4), spk((32, 80), (50, 82), (40, 96), 4), spk((50, 82), (68, 80), (60, 96), 4, light_left=False),
             spk((68, 80), (86, 70), (86, 92), 4, light_left=False),
             L(blob([(58, 12), (96, 44), (92, 70), (66, 80)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3)],
}

# ------------------------------------------------------------------ Arion Matlock: calvo y muy pálido, con un símbolo azul
# grisáceo en la cabeza, maquillaje de payaso (nariz roja, ojos y boca enormes pintados) y una bufanda gris enorme
ARION_SCARF_F = blob([(4, 96), (20, 92), (50, 104), (80, 92), (96, 96), (100, 112), (80, 118), (50, 122), (20, 118), (0, 112)])
CHARS['arion-matlock'] = {
    'body': 'normal', 'pal': pal('#5a8a8a', '#fce0b8', paint='#8a3a2a', lip='#c03a2a', nose='#c03a2a', scarf='#9a9ea2', scarf_d='#74787c'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'none', 'big_ears': 1.5, 'ear_out': 3, 'nose': (50, 82, 3.4), 'nose_side': (91, 80, 3.2),
             'hairline': False},
    'front': bald('front') + [L([(40, 22), (56, 16), (60, 22), (52, 24), (50, 36), (44, 34), (48, 26), (42, 28)], 'mid', 'b', ln=True),
                              L(ell(36, 75, 7, 6.4), 'paint', 'f', False), L(ell(64, 75, 7, 6.4), 'paint', 'f', False),
                              L(quad((32, 88), (50, 84), (68, 88)) + quad((68, 88), (50, 102), (32, 88))[1:], 'lip', 'f', ln=True),
                              L(quad((38, 90), (50, 88), (62, 90)) + quad((62, 90), (50, 96), (38, 90))[1:], (90, 20, 20, 255), 'f', False),
                              L(ARION_SCARF_F, 'scarf', 'f', ln=True), L(blob([(54, 106), (80, 94), (98, 98), (98, 110), (80, 116), (56, 118)], 6), 'scarf_d', 'f', False),
                              L(blob([(70, 108), (96, 104), (106, 128), (94, 132), (78, 120)]), 'scarf', 'f', ln=True)],
    'side': bald('side') + [L(blob([(40, 12), (56, 8), (60, 14), (50, 16), (48, 26), (42, 24)], 6), 'mid', 'b', ln=True),
                            L(ell(83, 75, 5, 6.4), 'paint', 'f', False), L(blob([(80, 88), (92, 86), (92, 96), (82, 96)], 4), 'lip', 'f', ln=True),
                            L(blob([(30, 94), (60, 92), (86, 100), (88, 114), (60, 118), (30, 114)]), 'scarf', 'f', ln=True),
                            L(blob([(20, 98), (34, 96), (26, 124), (12, 128), (8, 114)]), 'scarf', 'f', ln=True)],
    'back': bald('back') + [L(blob([(4, 94), (20, 88), (50, 90), (80, 88), (96, 94), (100, 112), (50, 118), (0, 112)]), 'scarf', 'f', ln=True),
                            L(blob([(54, 92), (96, 96), (98, 110), (56, 116)], 6), 'scarf_d', 'f', False)],
}

# ------------------------------------------------------------------ Wesley Knox: coleta rubia altísima que sale de la coronilla
# y cae hacia atrás, lados rapados (pardo grisáceo), una cicatriz roja en la mejilla y sonrisa de lado
CHARS['wesley-knox'] = {
    'body': 'normal', 'pal': pal('#d8c890', '#fcd2a6', shave='#7a6a5a', tie='#2a3a6a', scar='#d05a4a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': (54, 46)},
    'front': [L(blob(SKULL_F), 'shave'),
              L(blob([(44, 12), (40, -10), (50, -24), (60, -18), (58, -2), (56, 12)]), 'mid', 'b', ln=True),
              L(blob([(54, -16), (60, -18), (58, 8)], 4), 'shade', 'b', False),
              L(blob([(44, 2), (56, 2), (56, -6), (44, -6)], 3), 'tie', 'b', ln=True),
              L(blob([(30, 26), (50, 10), (70, 26), (66, 48), (54, 62), (50, 52), (40, 58), (34, 44)]), 'mid', 'b', False),
              L(blob([(54, 16), (70, 28), (64, 50), (56, 58)], 5), 'shade', 'b', False),
              L([(64, 82), (70, 78)], 'scar', 'f', False, False, 1.4), L([(66, 86), (72, 80)], 'scar', 'f', False, False, 1.2)],
    'side': [L(blob(SIDE_SKULL), 'shave'),
             L(blob([(40, 14), (30, -10), (14, -26), (2, -30), (-8, -10), (-14, 30), (-12, 70), (-6, 40), (0, 0), (14, -12), (28, 0), (32, 16)]), 'mid', 'b', ln=True),
             L(blob([(-10, 0), (-12, 40), (-8, 64), (-6, 20)], 6), 'shade', 'b', False),
             L(ell(32, 6, 4.6, 6), 'tie', 'b', ln=True),
             L(blob([(36, 16), (60, 10), (82, 18), (92, 34), (80, 40), (60, 34)]), 'mid', 'b', False),
             L([(80, 82), (84, 78)], 'scar', 'f', False, False, 1.4)],
    'back': [L(blob(SKULL_B), 'shave'), L(blob([(58, 30), (86, 40), (84, 68), (66, 84)], 6), tuple(int(v * 0.85) for v in (122, 106, 90)) + (255,), 'b', False),
             L(blob([(36, 14), (50, 8), (64, 14), (60, 28), (40, 28)]), 'mid', 'b', False)]
            + wavy((42, 10), (58, 10), (52, 104), -6, z='f') + [L(ell(50, 8, 7, 4), 'tie', 'f', ln=True),
                                                               L(blob([(44, 4), (56, 4), (60, -16), (50, -22), (42, -14)]), 'mid', 'b', ln=True)],
}

# ------------------------------------------------------------------ Byron Love (Afrodita): melena rubia muy clara, lisa y larga
# hasta más abajo de los hombros, con raya en medio y mechones a los lados de la cara; ojos rojos grandes
CHARS['byron-love'] = {
    'body': 'normal', 'pal': pal('#e2de9c', '#fce0c4', iris='#b0201a'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': (58, 50)},
    'front': [L(blob([(2, 128), (-4, 64), (8, 20), (50, 6), (92, 20), (104, 64), (98, 128), (82, 124), (82, 66), (18, 66), (18, 124)])),
              L(blob([(62, 12), (100, 50), (96, 124), (86, 122)], 6), 'shade', 'b', False), sheen(22, 48, 20, 3),
              strand([(50, 8), (50, 40)], 'shade', 'b', 1.2),
              L(quad((48, 16), (50, 20), (52, 16)), 'shade', 'b', False, False, 1.0),
              spk((12, 42), (32, 34), (18, 92), 5, z='f'), spk((28, 36), (48, 30), (40, 66), 5, z='f'),
              spk((52, 30), (72, 36), (62, 66), 5, z='f', light_left=False), spk((68, 34), (88, 42), (82, 92), 5, z='f', light_left=False),
              L(blob([(10, 60), (20, 62), (22, 110), (14, 126), (8, 100)]), 'mid', 'f'), L(blob([(90, 60), (80, 62), (78, 110), (86, 126), (92, 100)]), 'mid', 'f'),
              strand([(20, 64), (20, 112), (14, 124)], OUTC, 'f', 1.0), strand([(80, 64), (80, 112), (86, 124)], OUTC, 'f', 1.0)],
    'side': [L(blob([(56, 128), (14, 130), (-2, 80), (2, 30), (24, 8), (56, 4), (82, 14), (94, 34), (92, 58), (76, 56), (62, 58), (58, 76), (58, 110)])),
             L(blob([(4, 50), (8, 120), (46, 126), (26, 80)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             strand([(20, 40), (14, 124)], 'shade', 'b', 1.0), strand([(40, 30), (36, 126)], 'shade', 'b', 1.0),
             spk((56, 30), (92, 40), (92, 84), 6, z='f', light_left=False)],
    'back': [L(blob([(2, 128), (-4, 64), (8, 20), (50, 6), (92, 20), (104, 64), (98, 128), (50, 134)])),
             L(blob([(58, 12), (100, 50), (96, 126), (66, 132)], 6), 'shade', 'b', False), sheen(22, 48, 20, 3)]
            + [strand([(x, 30), (x + (x - 50) * 0.15, 128)], 'shade', 'b', 1.0) for x in (24, 38, 50, 62, 76)],
}

# ------------------------------------------------------------------ Jonas Demetrius: casco griego de metal con la cresta roja de
# delante atrás, carrilleras y una abertura en T para los ojos; asoma pelo castaño en la nuca
HELM_F = blob([(10, 98), (8, 50), (14, 22), (34, 8), (50, 6), (66, 8), (86, 22), (92, 50), (90, 98), (72, 100), (66, 84), (60, 64), (40, 64),
               (34, 84), (28, 100)], 8)
CHARS['jonas-demetrius'] = {
    'body': 'normal', 'pal': pal('#5a3a2a', '#f6c08e', helm='#a0a0a8', helm_d='#6e6e78', helm_l='#d0d0d8', crest='#b02a10', crest_d='#801a08'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 93, 'ears': False, 'hairline': False},
    'front': [L(blob([(44, 8), (44, -14), (50, -18), (56, -14), (56, 8)], 6), 'crest', 'b', ln=True),
              L(HELM_F, 'helm', 'f', ln=True), L(blob([(62, 10), (88, 30), (90, 96), (74, 98), (68, 70)], 6), 'helm_d', 'f', False),
              L(blob([(20, 30), (34, 16), (44, 14), (32, 28)], 4), 'helm_l', 'f', False),
              L([(40, 66), (60, 66)], 'helm_d', 'f', False, False, 1.4),
              L(blob([(44, 30), (50, 26), (56, 30), (54, 44), (50, 50), (46, 44)], 4), 'helm_d', 'f', ln=True),
              L(quad((14, 54), (50, 46), (86, 54)), 'helm_d', 'f', False, False, 1.4)],
    'side': [L(blob([(24, 20), (40, -4), (66, -12), (96, -6), (86, 2), (64, 0), (42, 10)]), 'crest', 'b', ln=True),
             L(blob([(26, 4), (50, -6), (80, -6), (60, 2), (40, 10)], 5), 'crest_d', 'b', False),
             L(blob([(12, 84), (8, 50), (14, 22), (36, 6), (64, 6), (84, 18), (94, 40), (92, 58), (78, 58), (74, 74), (80, 98), (64, 102), (56, 84),
                     (40, 90), (24, 96)]), 'helm', 'f', ln=True),
             L(blob([(12, 50), (18, 24), (34, 14), (32, 60), (22, 90)], 6), 'helm_d', 'f', False),
             L(blob([(40, 14), (64, 10), (80, 18), (60, 18)], 4), 'helm_l', 'f', False),
             L(quad((14, 54), (50, 50), (92, 52)), 'helm_d', 'f', False, False, 1.4)],
    'back': [L(blob([(44, 10), (44, -14), (50, -18), (56, -14), (56, 10)], 6), 'crest', 'b', ln=True),
             L(blob([(24, 88), (30, 70), (70, 70), (76, 88), (50, 96)]), 'mid', 'b', ln=True),
             L(blob([(10, 78), (8, 46), (14, 22), (34, 8), (50, 6), (66, 8), (86, 22), (92, 46), (90, 78), (50, 72)]), 'helm', 'f', ln=True),
             L(blob([(58, 10), (88, 30), (90, 76), (64, 74)], 6), 'helm_d', 'f', False),
             L(quad((10, 56), (50, 50), (90, 56)), 'helm_d', 'f', False, False, 1.4)],
}

# ------------------------------------------------------------------ Gus Heeley: piel tostada, pelo castaño de pinchos en todas
# direcciones; sonrisa pícara y mirada afilada
GUS_TOP = [spk((6, 62), (10, 44), (-14, 56), 6), spk((10, 44), (20, 26), (-14, 22), 7), spk((20, 26), (38, 12), (16, -16), 7),
           spk((38, 12), (58, 8), (48, -26), 8), spk((58, 10), (76, 18), (84, -12), 7, light_left=False),
           spk((76, 22), (88, 38), (114, 24), 7, light_left=False), spk((88, 42), (94, 62), (114, 60), 6, light_left=False)]
CHARS['gus-heeley'] = {
    'body': 'normal', 'pal': pal('#5a3a30', '#e0a040'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': (60, 50)},
    'front': GUS_TOP + [L(blob([(8, 74), (6, 40), (18, 16), (50, 6), (82, 16), (94, 40), (92, 74), (80, 66), (20, 66)])),
                        spk((6, 70), (14, 80), (-8, 88), 4), spk((86, 80), (94, 70), (108, 88), 4, light_left=False),
                        L(blob([(62, 12), (92, 38), (90, 70), (78, 66)], 6), 'shade', 'b', False),
                        spk((12, 46), (30, 40), (18, 72), 5, z='f'), spk((30, 40), (48, 36), (38, 62), 5, z='f'),
                        spk((52, 36), (70, 40), (62, 62), 5, z='f', light_left=False), spk((70, 40), (88, 46), (84, 72), 5, z='f', light_left=False)],
    'side': [spk((16, 40), (24, 22), (-18, 18), 8), spk((24, 24), (42, 12), (8, -16), 8), spk((42, 12), (62, 6), (54, -24), 8),
             spk((14, 58), (16, 40), (-18, 52), 7), spk((18, 74), (22, 58), (-10, 82), 6), spk((26, 86), (30, 74), (8, 98), 5),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((62, 12), (82, 22), (100, 0), 7, light_left=False), spk((56, 30), (88, 40), (92, 70), 6, z='f', light_left=False)],
    'back': GUS_TOP + [L(blob([(8, 76), (6, 40), (18, 16), (50, 6), (82, 16), (94, 40), (92, 76), (66, 88), (34, 88)])),
                       spk((12, 74), (30, 86), (6, 98), 5), spk((30, 88), (50, 90), (40, 108), 5), spk((50, 90), (70, 88), (62, 108), 5, light_left=False),
                       spk((70, 86), (88, 74), (94, 98), 5, light_left=False),
                       L(blob([(58, 12), (92, 38), (90, 74), (66, 86)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Henry House: melena castaña lisa hasta los hombros con raya
# en medio y una cinta fina blanca en la frente; mirada seria
CHARS['henry-house'] = {
    'body': 'normal', 'pal': pal('#8a4a2a', '#fcd8b4', band='#ece4dc'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'frown', 'mouth_y': 93, 'hairline': [(10, 66), (24, 54), (40, 48), (50, 52), (60, 48), (76, 54), (90, 66)]},
    'front': [L(blob([(6, 108), (2, 60), (10, 20), (50, 6), (90, 20), (98, 60), (94, 108), (82, 104), (82, 66), (18, 66), (18, 104)])),
              L(blob([(62, 12), (96, 48), (92, 104), (84, 102)], 6), 'shade', 'b', False), sheen(22, 48, 20, 3),
              strand([(50, 8), (50, 50)], 'deep', 'b', 1.2), strand([(40, 12), (24, 50)], 'shade', 'b', 1.0), strand([(60, 12), (76, 50)], 'shade', 'b', 1.0),
              L(quad((10, 52), (50, 44), (90, 52)), 'band', 'f', False, False, 2.0),
              L(blob([(10, 58), (20, 60), (24, 96), (16, 108), (8, 90)]), 'mid', 'f'), L(blob([(90, 58), (80, 60), (76, 96), (84, 108), (92, 90)]), 'mid', 'f'),
              strand([(20, 62), (22, 96), (16, 106)], OUTC, 'f', 1.0), strand([(80, 62), (78, 96), (84, 106)], OUTC, 'f', 1.0)],
    'side': [L(blob([(54, 108), (14, 110), (0, 70), (4, 30), (24, 8), (56, 4), (82, 14), (94, 34), (92, 56), (76, 54), (62, 58), (58, 76), (58, 100)])),
             L(blob([(4, 50), (8, 102), (46, 106), (26, 74)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             strand([(20, 36), (14, 104)], 'shade', 'b', 1.0), strand([(38, 30), (34, 106)], 'shade', 'b', 1.0),
             L(quad((6, 46), (50, 40), (92, 46)), 'band', 'f', False, False, 2.0),
             spk((56, 30), (90, 40), (92, 64), 5, z='f', light_left=False)],
    'back': [L(blob([(6, 108), (2, 60), (10, 20), (50, 6), (90, 20), (98, 60), (94, 108), (50, 112)])),
             L(blob([(58, 12), (96, 48), (92, 106), (66, 110)], 6), 'shade', 'b', False), sheen(22, 48, 20, 3),
             L(quad((2, 46), (50, 38), (98, 46)), 'band', 'f', False, False, 2.0)]
            + [strand([(x, 50), (x + (x - 50) * 0.1, 108)], 'shade', 'b', 1.0) for x in (26, 40, 50, 60, 74)],
}

# ------------------------------------------------------------------ Iggy Russ (portero suplente): pelo verde azulado con un
# flequillo largo que le tapa un ojo, un pañuelo de rayas moradas atado a la cabeza y puntas oscuras en la nuca
CHARS['iggy-russ'] = {
    'body': 'normal', 'pal': pal('#5a9a9a', '#f2b884', dark='#4a5458', band='#8a5a6a', band_l='#c8a0a8', band_d='#5a3a44'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': (60, 52)},
    'front': [spk((10, 66), (20, 66), (8, 80), 3), spk((80, 66), (90, 66), (92, 80), 3, light_left=False),
              L(blob([(12, 70), (10, 40), (22, 14), (50, 6), (78, 14), (90, 40), (88, 70)])),
              L(blob([(62, 12), (88, 36), (86, 66), (74, 62)], 6), 'shade', 'b', False),
              L(quad((10, 40), (50, 28), (90, 40)) + quad((90, 58), (50, 48), (10, 58)), 'band', 'f', ln=True)]
             + [L(quad((10 + k * 16, 40 - 4), (14 + k * 16, 48), (12 + k * 16, 58)), 'band_l', 'f', False, False, 2.2) for k in range(5)]
             + [L(blob([(36, 6), (60, 8), (86, 26), (80, 60), (66, 80), (58, 84), (60, 60), (50, 40), (30, 30)]), 'mid', 'f', ln=True),
                L(blob([(64, 20), (84, 30), (76, 64), (62, 80)], 5), 'shade', 'f', False)],
    'side': [spk((12, 66), (22, 64), (2, 78), 4), spk((20, 76), (30, 74), (12, 88), 4),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             L(quad((10, 40), (50, 30), (92, 38)) + quad((92, 56), (50, 48), (10, 58)), 'band', 'f', ln=True),
             L(blob([(40, 8), (66, 6), (88, 18), (96, 40), (90, 64), (82, 48), (70, 30)]), 'mid', 'f', ln=True)],
    'back': [L(blob(SKULL_B), 'dark')]
            + [x for k in range(5) for x in spk((14 + k * 15, 74 + abs(k - 2) * -2), (28 + k * 15, 76), (18 + k * 15, 94), 4)]
            + [L(blob([(10, 66), (8, 38), (20, 14), (50, 6), (80, 14), (92, 38), (90, 66), (50, 70)])),
               L(quad((8, 44), (50, 36), (92, 44)) + quad((92, 66), (50, 58), (8, 66)), 'band', 'f', ln=True)]
            + [L([(14 + k * 18, 44), (16 + k * 18, 64)], 'band_l', 'f', False, False, 2.2) for k in range(5)],
}

# ------------------------------------------------------------------ Harry Closs: corpulento, piel morena, tupé morado muy oscuro
# de pinchos echado hacia arriba y atrás, orejas puntiagudas y cara ancha de enfado
CHARS['harry-closs'] = {
    'body': 'corpulento', 'pal': pal('#2a2440', '#a0683a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 92, 'big_ears': 1, 'hairline': (56, 46)},
    'front': [spk((18, 28), (36, 14), (6, -6), 7), spk((34, 14), (52, 8), (36, -16), 7), spk((50, 8), (68, 14), (70, -14), 7, light_left=False),
              spk((66, 16), (82, 28), (98, 4), 7, light_left=False),
              L(blob([(12, 64), (10, 36), (22, 14), (50, 8), (78, 14), (90, 36), (88, 64)])),
              spk((8, 50), (14, 64), (-6, 64), 4), spk((86, 64), (92, 50), (106, 64), 4, light_left=False),
              L(blob([(62, 12), (88, 34), (86, 62), (74, 58)], 6), 'shade', 'b', False)],
    'side': [spk((20, 30), (36, 12), (-4, 0), 8), spk((36, 12), (56, 4), (24, -18), 8), spk((56, 6), (76, 10), (66, -16), 7, light_left=False),
             spk((76, 14), (90, 26), (104, 10), 6, light_left=False), spk((14, 52), (18, 34), (-12, 40), 7),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False)],
    'back': [spk((18, 28), (36, 14), (6, -6), 7), spk((34, 14), (52, 8), (36, -16), 7), spk((50, 8), (68, 14), (70, -14), 7, light_left=False),
             spk((66, 16), (82, 28), (98, 4), 7, light_left=False),
             L(blob([(12, 70), (10, 36), (22, 14), (50, 8), (78, 14), (90, 36), (88, 70), (66, 82), (34, 82)])),
             spk((8, 50), (14, 64), (-6, 64), 4), spk((86, 64), (92, 50), (106, 64), 4, light_left=False),
             spk((20, 74), (38, 82), (24, 94), 4), spk((62, 82), (80, 74), (76, 94), 4, light_left=False)] + back_hair(),
}

# ------------------------------------------------------------------ Andy Chronic: calvo, con una cicatriz cosida en la cabeza y
# moratones verdosos en las mejillas; ojos redondos de enfado, nariz grande y orejas grandes
CHARS['andy-chronic'] = {
    'body': 'normal', 'pal': pal('#6a4a2a', '#f0b468', scar='#7a4a2a', bruise='#7a8a5a', nose='#e0a058'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'big_ears': 1.5, 'ear_out': 3, 'nose': (50, 83, 4.6),
             'nose_side': (91, 81, 4.2), 'hairline': False},
    'front': bald('front') + [L(quad((24, 34), (40, 24), (58, 26)), 'scar', 'b', False, False, 1.6)]
             + [L([(30 + k * 6, 26 - k * 0.4 + 0), (32 + k * 6, 33 - k * 0.4)], 'scar', 'b', False, False, 1.2) for k in range(5)]
             + [L(blob([(24, 88), (30, 86), (30, 94), (25, 94)], 4), 'bruise', 'f', False), L(blob([(76, 88), (70, 86), (70, 94), (75, 94)], 4), 'bruise', 'f', False)],
    'side': bald('side') + [L(quad((40, 18), (62, 14), (82, 26)), 'scar', 'b', False, False, 1.6)]
            + [L([(46 + k * 7, 13 + k * 1.2), (48 + k * 7, 20 + k * 1.2)], 'scar', 'b', False, False, 1.2) for k in range(5)]
            + [L(blob([(76, 86), (84, 84), (84, 96), (78, 96)], 4), 'bruise', 'f', False)],
    'back': bald('back'),
}

# ------------------------------------------------------------------ Ned Yousef (sin modelo 3D; su retrato): pelo verde oliva con
# raya en medio y gruesos mechones horizontales que salen hacia los lados; dos puntos en la frente y sonrisa
def ned_locks(view):
    out = []
    for i, y in enumerate((30, 44, 58)):
        ln = 16 - i * 3
        lock = [(16, y - 7), (2 - ln * 0.4, y - 8), (-ln, y - 3), (-ln - 2, y + 6), (-ln + 4, y + 9), (0, y + 5), (16, y + 7)]
        sides = [lock] if view == 'side' else [lock, [(100 - x, yy) for x, yy in lock]]
        for sd in sides:
            out += [L(blob(sd, 6), 'mid', 'b', ln=True), L(blob([(p[0], p[1] + 3) for p in sd[3:6]] + [sd[3]], 4), 'shade', 'b', False)]
    return out


CHARS['ned-yousef'] = {
    'body': 'normal', 'pal': pal('#7a7440', '#f6b878'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': [(10, 62), (30, 54), (40, 50), (50, 56), (60, 50), (70, 54), (90, 62)]},
    'front': ned_locks('front') + [L(blob([(12, 66), (10, 38), (22, 14), (50, 6), (78, 14), (90, 38), (88, 66)])),
                                   L(blob([(62, 12), (88, 36), (86, 64), (74, 60)], 6), 'shade', 'b', False),
                                   strand([(50, 8), (50, 54)], 'deep', 'b', 1.2),
                                   L(ell(44, 62, 1.8, 1.8), OUTC, 'f', False), L(ell(56, 62, 1.8, 1.8), OUTC, 'f', False)],
    'side': ned_locks('side') + [L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
                                 spk((56, 30), (88, 40), (92, 60), 5, z='f', light_left=False)],
    'back': ned_locks('back') + [L(blob(SKULL_B))] + back_hair() + [strand([(50, 8), (50, 84)], 'deep', 'b', 1.2)],
}
