"""Jóvenes Inazuma (IE2): los veteranos del Inazuma Eleven cuando eran niños, hace 40 años, con sus modelos 3D de IE2.
Se guardan como '<equipo>:<jugador>' para no pisar a los veteranos (los mismos jugadores en el Inazuma Eleven)."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, pal, sheen, spk, strand
from chars_otaku import back_hair, glasses, side_glass
from chars_sengoku import wavy
from chars_umbrella import BOB_B, BOB_F, BOB_S, bob_shade
from heads import quad

T = 'ie2-young-inazuma:'
WHITE = (255, 255, 255, 255)
DARK = (24, 20, 24, 255)
SIDE_SKULL = [(44, 92), (22, 88), (12, 64), (14, 36), (30, 16), (56, 10), (78, 18), (88, 36), (76, 44), (60, 48), (52, 62), (50, 80)]
SKULL_F = [(16, 64), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 64)]
SKULL_B = [(16, 70), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 70), (66, 86), (34, 86)]
LONG_FACE = quad((20, 52), (18, 104), (50, 112)) + quad((50, 112), (82, 104), (80, 52))[1:] + quad((80, 52), (50, 26), (20, 52))[1:-1]
WIDE_FACE = blob([(12, 54), (50, 46), (88, 54), (92, 76), (86, 96), (66, 106), (50, 108), (34, 106), (14, 96), (8, 76)])

# ------------------------------------------------------------------ Seymour (portero): corpulento, piel morena, pañuelo morado atado
# a la cabeza con las puntas detrás, patillas oscuras, ojos pequeños y dientes apretados (aún sin barba)
CHARS[T + 'seymour-hillman'] = {
    'body': 'corpulento', 'pal': pal('#3a2a20', '#b8784a', wrap='#3a2a4e', wrap_d='#281c38'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 94, 'face_front': WIDE_FACE, 'big_ears': 1, 'nose': (50, 82, 3.4),
             'nose_side': (92, 80, 3.2), 'hairline': False},
    'front': [L(blob([(14, 58), (22, 58), (24, 80), (16, 78)])), L(blob([(86, 58), (78, 58), (76, 80), (84, 78)])),
              L(blob([(14, 60), (12, 32), (24, 12), (50, 4), (76, 12), (88, 32), (86, 60), (50, 56)]), 'wrap', 'f', ln=True),
              L(blob([(60, 8), (88, 30), (86, 58), (70, 56)], 6), 'wrap_d', 'f', False)],
    'side': [L(blob(SIDE_SKULL)), L(blob([(40, 58), (52, 58), (54, 80), (44, 78)])),
             L(blob([(12, 60), (10, 30), (26, 8), (54, 2), (80, 10), (92, 30), (92, 54), (50, 54)]), 'wrap', 'f', ln=True),
             L(blob([(14, 48), (2, 44), (-12, 54), (0, 58), (16, 56)], 4), 'wrap', 'f', ln=True), L(blob([(14, 54), (2, 60), (-8, 72), (6, 68)], 4), 'wrap_d', 'f', ln=True)],
    'back': [L(blob(SKULL_B), 'mid'),
             L(blob([(14, 62), (12, 34), (24, 12), (50, 4), (76, 12), (88, 34), (86, 62), (50, 66)]), 'wrap', 'f', ln=True),
             L(blob([(58, 8), (88, 32), (86, 60), (66, 64)], 6), 'wrap_d', 'f', False),
             L(blob([(50, 62), (36, 70), (30, 84), (44, 76)], 4), 'wrap', 'f', ln=True), L(blob([(50, 62), (64, 70), (70, 84), (56, 76)], 4), 'wrap', 'f', ln=True)],
}

# ------------------------------------------------------------------ Charles: media melena castaño oliva con un flequillo largo que
# le tapa un ojo; el otro azul y grande
CHARS[T + 'charles-island'] = {
    'body': 'normal', 'pal': pal('#4a4430', '#fce0c0', iris='#2a8aa8'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'line', 'mouth_y': 93, 'hairline': (60, 52)},
    'front': [L(blob(BOB_F))] + bob_shade('front') + [
              L(blob([(30, 26), (56, 22), (74, 30), (80, 60), (78, 92), (70, 96), (62, 76), (52, 58), (40, 44)]), 'mid', 'f'),
              L(blob([(60, 30), (76, 40), (76, 86), (70, 90), (64, 62)], 5), 'shade', 'f', False),
              strand([(40, 44), (54, 60), (64, 80), (70, 96)], OUTC, 'f', 1.0),
              spk((12, 44), (30, 36), (18, 74), 5, z='f'),
              spk((4, 70), (14, 80), (0, 94), 3), spk((86, 80), (96, 70), (100, 94), 3, light_left=False)],
    'side': [L(blob(BOB_S))] + bob_shade('side') + [spk((56, 30), (90, 40), (92, 84), 6, z='f', light_left=False),
             spk((4, 76), (16, 88), (-4, 96), 3)],
    'back': [L(blob(BOB_B))] + bob_shade('back') + [
             spk((12, 84), (30, 90), (14, 102), 4), spk((30, 90), (50, 92), (40, 104), 4), spk((50, 92), (70, 90), (60, 104), 4, light_left=False),
             spk((70, 90), (88, 84), (86, 102), 4, light_left=False)],
}

# ------------------------------------------------------------------ Garret: pelo castaño oscuro ondulado y abultado con mechones
# hacia los lados y un rizo arriba; ojos redondos y sonrisa con un diente
CHARS[T + 'garret-hairtown'] = {
    'body': 'normal', 'pal': pal('#4a3428', '#fcc490', nose='#e07a5a'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'buck', 'mouth_y': 92, 'nose': (50, 84, 2.4), 'big_ears': 1, 'hairline': (56, 48)},
    'front': wavy((6, 50), (12, 34), (-16, 30), 6) + wavy((88, 34), (94, 50), (116, 30), -6, light_left=False) + wavy((40, 10), (54, 8), (60, -12), -5)
             + [L(blob([(8, 64), (4, 40), (16, 14), (50, 4), (84, 14), (96, 40), (92, 64), (80, 56), (20, 56)])),
                L(blob([(62, 10), (94, 38), (90, 62), (80, 58)], 6), 'shade', 'b', False), sheen(22, 48, 14, 3)]
             + wavy((14, 42), (40, 30), (12, 60), 6, z='f') + wavy((40, 30), (64, 30), (48, 52), -5, z='f') + wavy((62, 32), (86, 40), (90, 58), -5, z='f', light_left=False),
    'side': wavy((20, 26), (40, 12), (-8, 8), 7) + wavy((40, 12), (60, 8), (52, -14), -5) + wavy((12, 52), (16, 34), (-14, 44), 6)
            + [L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False)]
            + wavy((56, 28), (86, 38), (94, 56), -5, z='f', light_left=False),
    'back': wavy((6, 50), (12, 34), (-16, 30), 6) + wavy((88, 34), (94, 50), (116, 30), -6, light_left=False) + wavy((40, 10), (54, 8), (60, -12), -5)
            + [L(blob([(8, 70), (4, 40), (16, 14), (50, 4), (84, 14), (96, 40), (92, 70), (66, 86), (34, 86)])),
               L(blob([(58, 10), (94, 38), (90, 68), (66, 84)], 6), 'shade', 'b', False)]
            + wavy((14, 70), (34, 84), (10, 92), 5) + wavy((66, 84), (86, 70), (90, 92), -5, light_left=False),
}

# ------------------------------------------------------------------ Arthur: corpulento y bajito, gorra verde azulado con un 4
# amarillo, patillas oscuras, gafas redondas pequeñas y boca seria
CHARS[T + 'arthur-sweet'] = {
    'body': 'corpulento', 'pal': pal('#2a2420', '#fcc08a', hat='#5a9690', hat_d='#3e726c', num='#f0c020'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'frown', 'mouth_y': 94, 'face_front': WIDE_FACE, 'hairline': False},
    'front': [L(blob([(10, 58), (22, 58), (24, 86), (14, 84)])), L(blob([(90, 58), (78, 58), (76, 86), (86, 84)])),
              L(blob([(10, 62), (8, 30), (22, 8), (50, 0), (78, 8), (92, 30), (90, 62), (50, 58)]), 'hat', 'f', ln=True),
              L(blob([(60, 4), (90, 28), (90, 60), (72, 58)], 6), 'hat_d', 'f', False),
              L([(14, 12), (10, 4), (22, 6)], 'hat', 'f', ln=True), L([(86, 12), (90, 4), (78, 6)], 'hat', 'f', ln=True),
              L([(44, 16), (52, 16), (48, 26), (56, 26), (56, 30), (52, 30), (52, 38), (48, 38), (48, 30), (40, 30)], 'num', 'f', ln=True),
              L(quad((8, 52), (50, 46), (92, 52)) + quad((92, 62), (50, 58), (8, 62)), 'hat_d', 'f', ln=True)]
             + glasses(74, 6, 5, (110, 110, 116, 255)),
    'side': [L(blob(SIDE_SKULL)), L(blob([(40, 56), (52, 56), (54, 86), (44, 84)])),
             L(blob([(12, 62), (10, 30), (26, 8), (54, 0), (80, 8), (92, 28), (92, 58), (50, 58)]), 'hat', 'f', ln=True),
             L(quad((10, 50), (50, 46), (94, 48)) + quad((94, 60), (50, 56), (10, 60)), 'hat_d', 'f', ln=True)] + side_glass(74, (110, 110, 116, 255)),
    'back': [L(blob(SKULL_B)), L(blob([(10, 64), (8, 30), (22, 8), (50, 0), (78, 8), (92, 30), (90, 64), (50, 68)]), 'hat', 'f', ln=True),
             L(blob([(58, 4), (90, 28), (90, 62), (66, 66)], 6), 'hat_d', 'f', False),
             L([(14, 12), (10, 4), (22, 6)], 'hat', 'f', ln=True), L([(86, 12), (90, 4), (78, 6)], 'hat', 'f', ln=True),
             L(quad((8, 54), (50, 48), (92, 54)) + quad((92, 66), (50, 60), (8, 66)), 'hat_d', 'f', ln=True)],
}

# ------------------------------------------------------------------ Tyler: cara alargada y pálida con la nariz muy larga, pelo negro
# con raya y un mechón de lado; ceño fruncido (aún sin bigote)
CHARS[T + 'tyler-thomas'] = {
    'body': 'normal', 'pal': pal('#24281a', '#fcecc4', nose='#e8c8a0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'face_front': LONG_FACE, 'big_ears': 1.5, 'ear_out': 3,
             'nose': (50, 86, 4.4), 'nose_side': (96, 84, 5), 'hairline': [(14, 60), (30, 44), (50, 40), (64, 50), (78, 56), (86, 62)]},
    'front': [L(blob([(14, 62), (12, 32), (24, 10), (50, 2), (76, 10), (88, 32), (86, 62)])),
              L(blob([(62, 10), (88, 32), (86, 60), (74, 56)], 6), 'shade', 'b', False), sheen(24, 48, 12, 3),
              spk((40, 10), (66, 10), (90, 30), 6, light_left=False),
              L([(56, 62), (50, 74), (46, 86), (54, 86)], 'skin_d', 'f', False)],
    'side': [L(blob([(44, 76), (20, 72), (10, 50), (14, 24), (32, 4), (60, 0), (82, 10), (90, 28), (76, 34), (60, 38), (52, 52)])),
             L(blob([(14, 40), (18, 66), (38, 72), (28, 52)], 6), 'shade', 'b', False), sheen(32, 64, 10, 3),
             spk((56, 6), (72, 10), (86, -4), 4, light_left=False)],
    'back': [L(blob(SKULL_B))] + back_hair(),
}

# ------------------------------------------------------------------ Ian: piel morena, pelo negro corto, gafas de sol rectangulares
# oscuras con montura roja y labios gruesos de enfado
CHARS[T + 'ian-suffolk'] = {
    'body': 'normal', 'pal': pal('#22221a', '#a8683a', lip='#c87060'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'lips', 'mouth_y': 94, 'mouth_w': 9, 'face_front': LONG_FACE, 'hairline': (54, 44)},
    'front': [L(blob([(16, 60), (14, 32), (26, 12), (50, 4), (74, 12), (86, 32), (84, 60)])),
              L(blob([(62, 10), (86, 32), (84, 58), (72, 54)], 6), 'shade', 'b', False), sheen(28, 52, 14, 3),
              L([(16, 68), (46, 70), (46, 80), (20, 80)], (40, 14, 14, 255), 'f', ln=True), L([(84, 68), (54, 70), (54, 80), (80, 80)], (40, 14, 14, 255), 'f', ln=True),
              L([(46, 72), (54, 72)], (120, 30, 30, 255), 'f', False, False, 1.8)],
    'side': [L(blob([(44, 70), (20, 68), (10, 46), (14, 22), (32, 6), (60, 2), (82, 12), (90, 30), (76, 36), (60, 38), (52, 50)])),
             L(blob([(14, 38), (18, 62), (38, 68), (28, 48)], 6), 'shade', 'b', False), sheen(32, 62, 10, 3),
             L([(74, 68), (92, 69), (91, 80), (76, 80)], (40, 14, 14, 255), 'f', ln=True), L([(74, 72), (50, 70)], (120, 30, 30, 255), 'f', False, False, 1.6)],
    'back': [L(blob(SKULL_B))] + back_hair(),
}

# ------------------------------------------------------------------ Peter: cara alargada, pelo castaño con raya en medio, mechones
# que caen por los lados y uno levantado arriba; ojos furiosos y dientes apretados
CHARS[T + 'peter-mildred'] = {
    'body': 'delgado', 'pal': pal('#6a4030', '#fcc8a0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'face_front': LONG_FACE, 'big_ears': 1,
             'hairline': [(14, 66), (28, 50), (42, 40), (50, 46), (58, 40), (72, 50), (86, 66)]},
    'front': [spk((44, 8), (52, 6), (40, -10), 3),
              L(blob([(12, 76), (10, 36), (22, 10), (50, 2), (78, 10), (90, 36), (88, 76), (80, 70), (80, 60), (20, 60), (20, 70)])),
              L(blob([(62, 10), (88, 34), (86, 72), (80, 70)], 6), 'shade', 'b', False), sheen(24, 48, 12, 3),
              strand([(50, 4), (50, 44)], 'deep', 'b', 1.1)],
    'side': [spk((46, 6), (56, 4), (50, -10), 3),
             L(blob([(46, 84), (20, 80), (10, 54), (14, 24), (32, 4), (60, 0), (82, 10), (92, 28), (80, 36), (62, 38), (54, 54), (50, 72)])),
             L(blob([(14, 40), (18, 74), (38, 80), (28, 54)], 6), 'shade', 'b', False), sheen(32, 64, 10, 3)],
    'back': [spk((44, 8), (52, 6), (40, -10), 3), L(blob([(12, 78), (10, 36), (22, 10), (50, 2), (78, 10), (90, 36), (88, 78), (50, 88)]))]
            + back_hair() + [strand([(50, 6), (50, 84)], 'deep', 'b', 1.0),
                             spk((30, 80), (50, 84), (38, 96), 3), spk((50, 84), (70, 80), (62, 96), 3, light_left=False)],
}

# ------------------------------------------------------------------ Josh: pelo verde muy oscuro peinado hacia atrás con volumen y
# un mechón suelto; ojos redondos, nariz y sonrisa
CHARS[T + 'josh-nathaniel'] = {
    'body': 'normal', 'pal': pal('#1e2a26', '#fcc070', nose='#a8603a'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'smile', 'mouth_y': 93, 'nose': (50, 83, 2.6), 'big_ears': 1.5, 'hairline': (52, 42)},
    'front': [spk((50, 6), (60, 6), (66, -10), 3, light_left=False),
              L(blob([(14, 62), (10, 30), (24, 6), (50, -2), (78, 6), (94, 28), (90, 62)])),
              spk((86, 40), (96, 30), (108, 40), 4, light_left=False),
              L(blob([(62, 6), (92, 28), (88, 60), (74, 56)], 6), 'shade', 'b', False), sheen(26, 50, 8, 3)],
    'side': [L(blob([(44, 70), (20, 68), (10, 46), (14, 20), (32, 0), (62, -4), (86, 6), (98, 22), (84, 30), (62, 34), (52, 48)])),
             L(blob([(14, 36), (18, 62), (38, 68), (28, 48)], 6), 'shade', 'b', False), sheen(32, 66, 6, 3),
             strand([(90, 14), (56, 6), (24, 28)], 'deep', 'b', 1.0)],
    'back': [spk((50, 6), (60, 6), (64, -10), 3, light_left=False), L(blob(SKULL_B))] + back_hair(),
}

# ------------------------------------------------------------------ Edward: pelo negro azulado corto con una cresta alta que acaba
# en punta gris, nariz roja, cejas furiosas y dientes apretados
CHARS[T + 'edward-gladstone'] = {
    'body': 'normal', 'pal': pal('#1e2638', '#fcc888', tip='#7a8090', nose='#e0603a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'face_front': LONG_FACE, 'nose': (50, 84, 3.6), 'nose_side': (92, 82, 3.4),
             'big_ears': 1, 'hairline': (52, 40)},
    'front': [L(blob([(42, 14), (40, -8), (46, -26), (56, -28), (58, -8), (58, 14)])), L(blob([(44, -12), (46, -26), (56, -28), (57, -14)], 4), 'tip', 'b', False),
              L(blob([(16, 58), (14, 32), (26, 12), (50, 6), (74, 12), (86, 32), (84, 58)])),
              L(blob([(62, 12), (86, 32), (84, 56), (72, 52)], 6), 'shade', 'b', False)],
    'side': [L(blob([(30, 16), (34, -4), (48, -22), (60, -22), (54, 0), (46, 16)])), L(blob([(44, -10), (50, -22), (60, -22), (54, -8)], 4), 'tip', 'b', False),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False)],
    'back': [L(blob([(42, 14), (40, -8), (46, -26), (56, -28), (58, -8), (58, 14)])), L(blob([(44, -12), (46, -26), (56, -28), (57, -14)], 4), 'tip', 'b', False),
             L(blob([(16, 72), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 72), (66, 90), (34, 90)]))] + back_hair(),
}

# ------------------------------------------------------------------ Joseph: media melena castaña abultada hasta los hombros con una
# cinta rosa fina en la frente y gafas finas; sonrisa
CHARS[T + 'joseph-yosemite'] = {
    'body': 'normal', 'pal': pal('#7a5444', '#fcc8a0', band='#d07a7a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'glasses': (40, 30, 30, 255), 'glasses_rect': True, 'hairline': (58, 48)},
    'front': [L(blob([(4, 96), (0, 54), (12, 18), (50, 6), (88, 18), (100, 54), (96, 96), (82, 92), (82, 64), (18, 64), (18, 92)])),
              L(blob([(62, 12), (98, 48), (94, 92), (84, 90)], 6), 'shade', 'b', False), sheen(22, 46, 18, 3),
              strand([(50, 8), (50, 46)], 'deep', 'b', 1.1),
              L(quad((6, 52), (50, 42), (94, 52)), 'band', 'f', False, False, 2.2),
              spk((10, 56), (24, 58), (16, 92), 4, z='f'), spk((76, 58), (90, 56), (84, 92), 4, z='f', light_left=False)],
    'side': [L(blob([(50, 98), (12, 98), (0, 62), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (92, 56), (76, 54), (62, 56), (58, 74), (56, 94)])),
             L(blob([(6, 50), (8, 92), (40, 96), (24, 66)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             L(quad((2, 46), (50, 36), (94, 42)), 'band', 'f', False, False, 2.2), spk((58, 48), (72, 50), (66, 84), 4, z='f')],
    'back': [L(blob([(4, 96), (0, 54), (12, 18), (50, 6), (88, 18), (100, 54), (96, 96), (50, 102)])),
             L(blob([(58, 12), (98, 48), (94, 94), (66, 100)], 6), 'shade', 'b', False), sheen(22, 46, 18, 3),
             spk((14, 92), (32, 98), (16, 108), 4), spk((32, 98), (50, 100), (40, 112), 4), spk((50, 100), (68, 98), (60, 112), 4, light_left=False),
             spk((68, 98), (86, 92), (84, 108), 4, light_left=False),
             L(quad((2, 48), (50, 38), (98, 48)), 'band', 'f', False, False, 2.2)],
}

# ------------------------------------------------------------------ Constant: corpulento, piel morena, pelo castaño oscuro corto
# con unas gafas de sol subidas a la cabeza y sonrisa pícara con dientes
CHARS[T + 'constant-builder'] = {
    'body': 'corpulento', 'pal': pal('#3a2a20', '#a8683a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 94, 'face_front': LONG_FACE, 'hairline': (54, 44)},
    'front': [L(blob([(14, 62), (12, 34), (24, 12), (50, 6), (76, 12), (88, 34), (86, 62)])),
              L(blob([(62, 12), (88, 34), (86, 60), (74, 56)], 6), 'shade', 'b', False), sheen(26, 50, 14, 3),
              L(ell(36, 24, 8, 5), DARK, 'f', ln=True), L(ell(64, 24, 8, 5), DARK, 'f', ln=True), L([(44, 23), (56, 23)], DARK, 'f', False, False, 1.4)],
    'side': [L(blob([(44, 74), (20, 72), (10, 50), (14, 26), (30, 10), (58, 4), (82, 14), (92, 30), (78, 38), (62, 40), (52, 54)])),
             L(blob([(14, 40), (18, 66), (38, 72), (28, 50)], 6), 'shade', 'b', False), sheen(32, 62, 12, 3),
             L(ell(76, 14, 6, 4.4), DARK, 'f', ln=True), L([(70, 16), (44, 22)], DARK, 'f', False, False, 1.4)],
    'back': [L(blob(SKULL_B))] + back_hair(),
}
