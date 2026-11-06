"""Inazuma Eleven (IE1): los veteranos del equipo original; barbas, bigotes, gorros y caras de adulto, con sus modelos 3D
como referencia."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, pal, sheen, spk, strand
from chars_otaku import back_hair, glasses, side_glass
from chars_sallys import beard, mustache
from chars_umbrella import BOB_B, BOB_F, BOB_S, bob_shade
from heads import quad

WHITE = (255, 255, 255, 255)
DARK = (24, 20, 24, 255)
SIDE_SKULL = [(44, 92), (22, 88), (12, 64), (14, 36), (30, 16), (56, 10), (78, 18), (88, 36), (76, 44), (60, 48), (52, 62), (50, 80)]
SKULL_F = [(16, 64), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 64)]
SKULL_B = [(16, 70), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 70), (66, 86), (34, 86)]
# cara alargada de adulto (mentón largo)
LONG_FACE = quad((20, 52), (18, 104), (50, 114)) + quad((50, 114), (82, 104), (80, 52))[1:] + quad((80, 52), (50, 26), (20, 52))[1:-1]
WIDE_FACE = blob([(12, 54), (50, 46), (88, 54), (92, 76), (86, 96), (66, 106), (50, 108), (34, 106), (14, 96), (8, 76)])


def stubble(y0=84, c='stub'):
    return [L(ell(x, y, 0.8, 0.8), c, 'f', False) for x, y in ((30, y0 + 4), (36, y0 + 8), (64, y0 + 8), (70, y0 + 4), (42, y0 + 14), (58, y0 + 14),
                                                               (50, y0 + 18), (34, y0 + 12), (66, y0 + 12))]


def sunglasses(y=76, r=6.5):
    return [L(ell(36, y, r, r * 0.9), DARK, 'f', ln=True), L(ell(64, y, r, r * 0.9), DARK, 'f', ln=True),
            L([(42, y - 1), (58, y - 1)], DARK, 'f', False, False, 1.4),
            L(ell(33, y - 2, 1.8, 1.4), (120, 120, 140, 255), 'f', False), L(ell(61, y - 2, 1.8, 1.4), (120, 120, 140, 255), 'f', False)]


# ------------------------------------------------------------------ Seymour Hillman (portero): corpulento; pañuelo morado atado a
# la cabeza con las puntas en la nuca, gafas de sol redondas negras, y una barba y bigote blancos abundantes; patillas canosas
CHARS['seymour-hillman'] = {
    'body': 'corpulento', 'pal': pal('#e8dcc4', '#d89a5a', wrap='#3a2a4e', wrap_d='#281c38'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'nose': (50, 80, 3.4), 'nose_side': (92, 78, 3.2), 'big_ears': 1, 'hairline': False},
    'front': [L(blob([(14, 62), (12, 34), (24, 12), (50, 4), (76, 12), (88, 34), (86, 62), (50, 58)]), 'wrap', 'f', ln=True),
              L(blob([(60, 8), (88, 32), (86, 60), (70, 58)], 6), 'wrap_d', 'f', False)] + sunglasses(70)
             + [beard(), L(blob([(26, 86), (40, 82), (50, 86), (60, 82), (74, 86), (66, 94), (50, 92), (34, 94)], 5), 'mid', 'f', ln=True),
                L(blob([(36, 98), (50, 96), (64, 98), (60, 112), (50, 118), (40, 112)], 5), 'shade', 'f', ln=True)],
    'side': [L(blob(SIDE_SKULL)),
             L(blob([(12, 62), (10, 30), (26, 8), (54, 2), (80, 10), (92, 30), (92, 56), (50, 54)]), 'wrap', 'f', ln=True),
             L(blob([(14, 50), (2, 46), (-12, 56), (0, 60), (16, 58)], 4), 'wrap', 'f', ln=True), L(blob([(14, 56), (2, 62), (-8, 74), (6, 70)], 4), 'wrap_d', 'f', ln=True),
             L(ell(86, 70, 5, 5.6), DARK, 'f', ln=True), L([(80, 69), (54, 66)], DARK, 'f', False, False, 1.4),
             L(blob([(50, 66), (60, 66), (66, 86), (80, 100), (94, 96), (92, 112), (76, 118), (56, 104)]), 'mid', 'f', ln=True)],
    'back': [L(blob(SKULL_B), 'skin'), L(blob([(12, 66), (20, 62), (22, 86), (14, 84)]), 'mid', 'b', False), L(blob([(88, 66), (80, 62), (78, 86), (86, 84)]), 'mid', 'b', False),
             L(blob([(14, 62), (12, 34), (24, 12), (50, 4), (76, 12), (88, 34), (86, 62), (50, 66)]), 'wrap', 'f', ln=True),
             L(blob([(58, 8), (88, 32), (86, 60), (66, 64)], 6), 'wrap_d', 'f', False),
             L(blob([(50, 62), (36, 70), (30, 84), (44, 76)], 4), 'wrap', 'f', ln=True), L(blob([(50, 62), (64, 70), (70, 84), (56, 76)], 4), 'wrap', 'f', ln=True)],
}

# ------------------------------------------------------------------ Charles Island: melena rubia sucia larga y lisa que le tapa
# los ojos por completo (flequillo hasta la nariz) y barba de pocos días
CHARS['charles-island'] = {
    'body': 'normal', 'pal': pal('#b0a878', '#f6c08e', stub='#8a6a4a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 96, 'face_front': LONG_FACE, 'hairline': False},
    'front': [L(blob([(10, 112), (6, 60), (14, 18), (50, 4), (86, 18), (94, 60), (90, 112), (78, 108), (80, 70), (20, 70), (22, 108)])),
              L(blob([(62, 12), (92, 50), (88, 108), (80, 106)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
              L(blob([(14, 40), (34, 24), (50, 22), (70, 24), (86, 40), (84, 86), (66, 90), (50, 84), (34, 90), (16, 86)]), 'mid', 'f', ln=True),
              L(blob([(56, 26), (82, 40), (82, 84), (64, 86)], 6), 'shade', 'f', False),
              strand([(50, 22), (50, 82)], 'deep', 'f', 1.1), strand([(34, 28), (28, 86)], 'shade', 'f', 1.0), strand([(66, 28), (72, 86)], 'shade', 'f', 1.0),
              L(blob([(32, 96), (68, 96), (62, 112), (50, 116), (38, 112)], 5), 'stub', 'f', False)],
    'side': [L(blob([(56, 110), (16, 112), (4, 70), (6, 30), (26, 8), (56, 4), (82, 14), (96, 36), (96, 80), (82, 72), (64, 62), (60, 86)])),
             L(blob([(6, 50), (8, 104), (46, 108), (26, 74)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             strand([(24, 30), (18, 106)], 'shade', 'b', 1.0), strand([(42, 26), (40, 108)], 'shade', 'b', 1.0),
             L(blob([(76, 94), (90, 94), (90, 108), (80, 110)], 4), 'stub', 'f', False)],
    'back': [L(blob([(10, 112), (6, 60), (14, 18), (50, 4), (86, 18), (94, 60), (90, 112), (50, 116)])),
             L(blob([(58, 12), (92, 50), (88, 110), (66, 114)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3)]
            + [strand([(x, 20), (x + (x - 50) * 0.12, 108)], 'shade', 'b', 1.0) for x in (26, 40, 50, 60, 74)],
}

# ------------------------------------------------------------------ Garret Hairtown: pelo castaño claro despeinado con mechones
# hacia los lados, ojos redondos, un bigote castaño grande y un diente
CHARS['garret-hairtown'] = {
    'body': 'normal', 'pal': pal('#9a6a54', '#f6c08e'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'buck', 'mouth_y': 94, 'big_ears': 1, 'hairline': (56, 46)},
    'front': [L(blob([(8, 64), (4, 40), (16, 14), (50, 4), (84, 14), (96, 40), (92, 64), (80, 56), (20, 56)])),
              spk((6, 48), (12, 60), (0, 64), 3), spk((88, 60), (94, 48), (100, 64), 3, light_left=False),
              L(blob([(62, 10), (94, 38), (90, 62), (80, 58)], 6), 'shade', 'b', False), sheen(22, 48, 14, 3),
              spk((22, 30), (52, 22), (14, 56), 6, z='f'), spk((50, 22), (74, 28), (86, 52), 5, z='f', light_left=False),
              mustache(87, 13)],
    'side': [L(blob([(46, 84), (20, 80), (8, 56), (10, 28), (28, 6), (58, 2), (84, 12), (96, 30), (92, 46), (74, 42), (60, 46), (52, 62)])),
             spk((8, 48), (12, 64), (-8, 64), 4), L(blob([(12, 42), (16, 74), (38, 80), (26, 58)], 6), 'shade', 'b', False), sheen(30, 64, 10, 3),
             spk((56, 26), (88, 34), (94, 54), 5, z='f', light_left=False),
             L(blob([(82, 86), (94, 84), (96, 92), (86, 92)], 4), 'mid', 'f', ln=True)],
    'back': [L(blob([(8, 70), (4, 40), (16, 14), (50, 4), (84, 14), (96, 40), (92, 70), (66, 84), (34, 84)])),
             spk((6, 48), (12, 60), (0, 64), 3), spk((88, 60), (94, 48), (100, 64), 3, light_left=False)] + back_hair(),
}

# ------------------------------------------------------------------ Arthur Sweet: corpulento, gorro de lana oliva calado hasta las
# orejas, patillas oscuras, gafas redondas pequeñas, bigote y sonrisa
CHARS['arthur-sweet'] = {
    'body': 'corpulento', 'pal': pal('#2a2420', '#f6b878', hat='#6a5a1e', hat_d='#4a3e12'),
    'face': {'eyes': 'dot', 'brows': True, 'mouth': 'smile', 'mouth_y': 95, 'mouth_w': 12, 'face_front': WIDE_FACE, 'hairline': False},
    'front': [L(blob([(10, 60), (22, 60), (24, 86), (14, 84)])), L(blob([(90, 60), (78, 60), (76, 86), (86, 84)])),
              L(blob([(10, 64), (8, 32), (22, 10), (50, 2), (78, 10), (92, 32), (90, 64), (50, 60)]), 'hat', 'f', ln=True),
              L(blob([(60, 6), (90, 30), (90, 62), (72, 60)], 6), 'hat_d', 'f', False)]
             + [strand([(x, 8 + abs(x - 50) * 0.3), (x, 50)], 'hat_d', 'f', 0.9) for x in (26, 38, 50, 62, 74)]
             + [L(quad((8, 50), (50, 44), (92, 50)) + quad((92, 64), (50, 58), (8, 64)), 'hat_d', 'f', ln=True)]
             + glasses(76, 6, 5, (90, 90, 96, 255)) + [mustache(87, 11)],
    'side': [L(blob(SIDE_SKULL)), L(blob([(40, 58), (52, 58), (54, 86), (44, 84)])),
             L(blob([(12, 64), (10, 30), (26, 8), (54, 2), (80, 10), (92, 30), (92, 60), (50, 60)]), 'hat', 'f', ln=True),
             L(quad((10, 48), (50, 44), (94, 48)) + quad((94, 62), (50, 58), (10, 62)), 'hat_d', 'f', ln=True)] + side_glass(76, (90, 90, 96, 255))
            + [L(blob([(82, 86), (94, 84), (94, 90), (84, 91)], 4), 'mid', 'f', ln=True)],
    'back': [L(blob(SKULL_B)), L(blob([(10, 66), (8, 32), (22, 10), (50, 2), (78, 10), (92, 32), (90, 66), (50, 70)]), 'hat', 'f', ln=True),
             L(blob([(58, 6), (90, 30), (90, 64), (66, 68)], 6), 'hat_d', 'f', False),
             L(quad((8, 54), (50, 48), (92, 54)) + quad((92, 68), (50, 62), (8, 68)), 'hat_d', 'f', ln=True)],
}

# ------------------------------------------------------------------ Slot Machines: corpulento, cabeza calva grande con una cresta
# corta castaña en lo alto, ojos cerrados con fuerza, barba de pocos días y boca torcida
CHARS['slot-machines'] = {
    'body': 'corpulento', 'pal': pal('#7a5a40', '#e0a050', stub='#8a5a2a'),
    'face': {'eyes': 'closed', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'face_front': WIDE_FACE, 'big_ears': 1.5, 'ear_out': 4,
             'nose': (50, 84, 3), 'hairline': False},
    'front': [L(blob([(12, 66), (10, 36), (22, 12), (50, 4), (78, 12), (90, 36), (88, 66)]), 'skin'),
              L(blob([(62, 10), (90, 34), (88, 64), (76, 60)], 6), 'skin_d', 'b', False),
              L(blob([(40, 14), (42, 0), (52, -8), (60, 0), (58, 14)]), 'mid', 'b', ln=True), strand([(48, -4), (48, 12)], 'deep', 'b', 1.0)] + stubble(86),
    'side': [L(blob([(44, 96), (18, 92), (6, 64), (10, 32), (28, 10), (56, 4), (80, 12), (94, 34), (96, 64), (92, 90), (70, 104), (54, 104)]), 'skin'),
             L(blob([(36, 10), (50, -6), (68, -6), (70, 6), (54, 8)]), 'mid', 'b', ln=True)]
            + [L(ell(x, y, 0.8, 0.8), 'stub', 'f', False) for x, y in ((80, 92), (86, 96), (78, 98), (88, 102))],
    'back': [L(blob([(12, 72), (10, 36), (22, 12), (50, 4), (78, 12), (90, 36), (88, 72), (68, 90), (32, 90)]), 'skin'),
             L(blob([(58, 10), (90, 36), (88, 70), (66, 88)], 6), 'skin_d', 'b', False),
             L(blob([(40, 14), (42, 0), (52, -8), (60, 0), (58, 14)]), 'mid', 'b', ln=True)],
}

# ------------------------------------------------------------------ Bill Steakspear: corpulento, sombrero vaquero marrón claro de
# ala ancha con cinta, pelo castaño rojizo que asoma por los lados, gafas redondas y bigote fino
COWBOY_BRIM = blob([(-16, 50), (0, 40), (50, 34), (100, 40), (116, 50), (100, 56), (50, 54), (0, 56)], 6)
CHARS['bill-steakspear'] = {
    'body': 'corpulento', 'pal': pal('#6a3a24', '#f6b878', hat='#8a6a4a', hat_d='#6a4e34', band='#c89a40', crown='#c8b088'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'face_front': WIDE_FACE, 'glasses': (70, 60, 50, 255), 'hairline': False},
    'front': [L(blob([(10, 54), (22, 54), (24, 84), (12, 80)])), L(blob([(90, 54), (78, 54), (76, 84), (88, 80)])),
              L(blob([(22, 46), (20, 20), (32, 4), (44, 10), (50, 2), (56, 10), (68, 4), (80, 20), (78, 46)]), 'hat', 'f', ln=True),
              L(blob([(26, 22), (34, 8), (46, 14), (40, 34)], 5), 'crown', 'f', False),
              L(quad((20, 36), (50, 30), (80, 36)) + quad((80, 44), (50, 38), (20, 44)), 'band', 'f', ln=True),
              L(COWBOY_BRIM, 'hat', 'f', ln=True), L(blob([(50, 46), (100, 42), (112, 50), (100, 54), (50, 52)], 5), 'hat_d', 'f', False),
              L([(-14, 50), (-18, 40), (-8, 44)], 'hat', 'f', ln=True), L([(114, 50), (118, 40), (108, 44)], 'hat', 'f', ln=True),
              mustache(88, 10)],
    'side': [L(blob(SIDE_SKULL)), L(blob([(40, 54), (54, 56), (56, 84), (44, 80)])),
             L(blob([(22, 48), (20, 20), (36, 4), (66, 2), (82, 18), (82, 48)]), 'hat', 'f', ln=True),
             L(quad((20, 36), (50, 30), (82, 36)) + quad((82, 44), (50, 38), (20, 44)), 'band', 'f', ln=True),
             L(blob([(-14, 44), (-20, 36), (20, 46), (60, 42), (110, 36), (118, 44), (86, 54), (50, 54), (10, 52)], 6), 'hat', 'f', ln=True),
             L(ell(84, 76, 5.4, 5.6), (70, 60, 50, 255), 'f', False), L(ell(84, 76, 4, 4.2), WHITE, 'f', False), L(ell(85, 76, 1.6, 1.8), OUTC, 'f', False),
             L(blob([(82, 87), (94, 86), (94, 91), (84, 91)], 4), 'mid', 'f', ln=True)],
    'back': [L(blob(SKULL_B)), L(blob([(16, 60), (84, 60), (80, 80), (20, 80)])),
             L(blob([(22, 46), (20, 20), (32, 4), (50, 8), (68, 4), (80, 20), (78, 46)]), 'hat', 'f', ln=True),
             L(quad((20, 36), (50, 30), (80, 36)) + quad((80, 44), (50, 38), (20, 44)), 'band', 'f', ln=True),
             L(COWBOY_BRIM, 'hat', 'f', ln=True), L(blob([(50, 46), (100, 42), (112, 50), (100, 54), (50, 52)], 5), 'hat_d', 'f', False)],
}

# ------------------------------------------------------------------ Peter Mildred: delgado, cara muy alargada, pelo castaño con
# raya en medio y un mechón levantado; ojos entornados y una sonrisa enorme
CHARS['peter-mildred'] = {
    'body': 'delgado', 'pal': pal('#8a5a44', '#f6c08e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98, 'face_front': LONG_FACE, 'nose': (50, 86, 2.6), 'big_ears': 1,
             'hairline': [(14, 62), (28, 48), (42, 40), (50, 46), (58, 40), (72, 48), (86, 62)]},
    'front': [spk((44, 8), (52, 6), (40, -10), 3),
              L(blob([(14, 66), (12, 34), (24, 10), (50, 2), (76, 10), (88, 34), (86, 66)])),
              L(blob([(62, 10), (88, 32), (86, 62), (74, 58)], 6), 'shade', 'b', False), sheen(24, 48, 12, 3),
              strand([(50, 4), (50, 42)], 'deep', 'b', 1.1)],
    'side': [spk((46, 6), (56, 4), (50, -10), 3),
             L(blob([(44, 78), (20, 74), (10, 50), (14, 24), (32, 4), (60, 0), (82, 10), (92, 28), (80, 36), (62, 38), (52, 52)])),
             L(blob([(14, 40), (18, 68), (38, 74), (28, 52)], 6), 'shade', 'b', False), sheen(32, 64, 10, 3)],
    'back': [spk((44, 8), (52, 6), (40, -10), 3), L(blob(SKULL_B))] + back_hair() + [strand([(50, 8), (50, 80)], 'deep', 'b', 1.0)],
}

# ------------------------------------------------------------------ Josh Nathaniel: pelo verde muy oscuro peinado hacia atrás con
# volumen y un mechón suelto; ojos redondos, nariz y sonrisa
CHARS['josh-nathaniel'] = {
    'body': 'normal', 'pal': pal('#24302a', '#fcc080', nose='#c87a4a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'face_front': LONG_FACE, 'nose': (50, 84, 2.8), 'big_ears': 1.5,
             'hairline': (52, 40)},
    'front': [spk((50, 6), (60, 6), (64, -10), 3, light_left=False),
              L(blob([(14, 60), (10, 30), (24, 6), (50, -2), (78, 6), (92, 28), (88, 60)])),
              L(blob([(62, 6), (90, 28), (88, 58), (74, 54)], 6), 'shade', 'b', False), sheen(26, 50, 8, 3),
              strand([(40, 4), (30, 40)], 'deep', 'b', 1.0), strand([(60, 4), (70, 40)], 'deep', 'b', 1.0)],
    'side': [L(blob([(44, 70), (20, 68), (10, 46), (14, 20), (32, 0), (62, -4), (86, 6), (96, 22), (84, 30), (62, 34), (52, 48)])),
             L(blob([(14, 36), (18, 62), (38, 68), (28, 48)], 6), 'shade', 'b', False), sheen(32, 66, 6, 3),
             strand([(90, 14), (56, 6), (24, 28)], 'deep', 'b', 1.0)],
    'back': [spk((50, 6), (60, 6), (64, -10), 3, light_left=False), L(blob(SKULL_B))] + back_hair(),
}

# ------------------------------------------------------------------ Edward Gladstone: calvo con una cresta corta de pelo negro
# verdoso en lo alto y patillas oscuras; cara alargada, nariz roja, cejas furiosas y boca cerrada
CHARS['edward-gladstone'] = {
    'body': 'delgado', 'pal': pal('#24343a', '#f6b878', nose='#d0603a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 98, 'face_front': LONG_FACE, 'nose': (50, 86, 3.6), 'nose_side': (92, 84, 3.4),
             'big_ears': 1, 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin'), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'skin_d', 'b', False),
              L(blob([(44, 12), (40, -6), (46, -22), (54, -24), (58, -6), (56, 12)]), 'mid', 'b', ln=True),
              L(blob([(50, -20), (56, -16), (56, 8)], 4), 'shade', 'b', False),
              L(blob([(14, 44), (20, 44), (22, 66), (16, 66)]), 'mid', 'f'), L(blob([(86, 44), (80, 44), (78, 66), (84, 66)]), 'mid', 'f'),
              L([(42, 92), (44, 104)], 'skin_d', 'f', False, False, 1.0), L([(58, 92), (56, 104)], 'skin_d', 'f', False, False, 1.0)],
    'side': [L(blob(SIDE_SKULL), 'skin'),
             L(blob([(30, 18), (34, 0), (46, -16), (56, -16), (52, 2), (44, 18)]), 'mid', 'b', ln=True),
             L(blob([(18, 46), (32, 40), (40, 44), (34, 60), (22, 64)]), 'mid', 'b', ln=True)],
    'back': [L(blob(SKULL_B), 'skin'), L(blob([(58, 12), (86, 36), (84, 68), (66, 84)], 6), 'skin_d', 'b', False),
             L(blob([(18, 46), (82, 46), (80, 70), (66, 84), (34, 84), (20, 70)]), 'mid', 'b', ln=True),
             L(blob([(44, 12), (40, -6), (46, -22), (54, -24), (58, -6), (56, 12)]), 'mid', 'b', ln=True)],
}

# ------------------------------------------------------------------ Joseph Yosemite: media melena castaña clara con una cinta
# granate atada en la frente, gafas de sol redondas negras, bigote y barba de pocos días
CHARS['joseph-yosemite'] = {
    'body': 'normal', 'pal': pal('#9a7464', '#f6c08e', band='#7a2a2a', stub='#8a5a3a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'face_front': LONG_FACE, 'hairline': (56, 48)},
    'front': [L(blob([(6, 96), (2, 54), (12, 18), (50, 4), (88, 18), (98, 54), (94, 96), (82, 92), (82, 64), (18, 64), (18, 92)])),
              spk((2, 80), (10, 94), (-8, 100), 4), spk((90, 94), (98, 80), (108, 100), 4, light_left=False),
              L(blob([(62, 12), (96, 46), (92, 92), (84, 90)], 6), 'shade', 'b', False), sheen(22, 46, 18, 3),
              strand([(50, 6), (50, 44)], 'deep', 'b', 1.1),
              L(quad((6, 54), (50, 44), (94, 54)) + quad((94, 60), (50, 50), (6, 60)), 'band', 'f', ln=True),
              spk((8, 58), (22, 60), (14, 92), 4, z='f'), spk((78, 60), (92, 58), (86, 92), 4, z='f', light_left=False)]
             + sunglasses(76) + [mustache(88, 10, 'shade')] + stubble(90),
    'side': [L(blob([(50, 98), (12, 98), (0, 62), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (92, 58), (76, 56), (62, 58), (58, 74), (56, 94)])),
             spk((2, 80), (14, 94), (-8, 102), 4),
             L(blob([(6, 50), (8, 92), (40, 96), (24, 66)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             L(quad((2, 50), (50, 40), (94, 46)) + quad((94, 52), (50, 46), (2, 56)), 'band', 'f', ln=True),
             spk((58, 48), (72, 50), (66, 84), 4, z='f'),
             L(ell(85, 76, 5, 5.6), DARK, 'f', ln=True), L([(80, 75), (64, 72)], DARK, 'f', False, False, 1.4),
             L(blob([(82, 88), (94, 86), (94, 92), (84, 92)], 4), 'shade', 'f', ln=True)],
    'back': [L(blob([(6, 96), (2, 54), (12, 18), (50, 4), (88, 18), (98, 54), (94, 96), (50, 102)])),
             spk((2, 80), (10, 94), (-8, 100), 4), spk((90, 94), (98, 80), (108, 100), 4, light_left=False),
             L(blob([(58, 12), (96, 46), (92, 94), (66, 100)], 6), 'shade', 'b', False), sheen(22, 46, 18, 3),
             L(quad((2, 48), (50, 38), (98, 48)) + quad((98, 54), (50, 44), (2, 54)), 'band', 'f', ln=True)],
}

# ------------------------------------------------------------------ Constant Builder: corpulento, piel morena, pelo gris corto con
# unas gafas de sol subidas a la cabeza, barba de pocos días, cicatriz en la mejilla y sonrisa torcida
CHARS['constant-builder'] = {
    'body': 'corpulento', 'pal': pal('#9a9284', '#b07040', stub='#4a3020', scar='#6a3a1e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 94, 'face_front': LONG_FACE, 'hairline': (54, 44)},
    'front': [L(blob([(14, 62), (12, 34), (24, 12), (50, 6), (76, 12), (88, 34), (86, 62)])),
              L(blob([(62, 12), (88, 34), (86, 60), (74, 56)], 6), 'shade', 'b', False), sheen(26, 50, 14, 3),
              L(ell(36, 26, 8, 5), DARK, 'f', ln=True), L(ell(64, 26, 8, 5), DARK, 'f', ln=True), L([(44, 25), (56, 25)], DARK, 'f', False, False, 1.4),
              L([(64, 84), (70, 94)], 'scar', 'f', False, False, 1.2)] + stubble(90),
    'side': [L(blob([(44, 74), (20, 72), (10, 50), (14, 26), (30, 10), (58, 4), (82, 14), (92, 30), (78, 38), (62, 40), (52, 54)])),
             L(blob([(14, 40), (18, 66), (38, 72), (28, 50)], 6), 'shade', 'b', False), sheen(32, 62, 12, 3),
             L(ell(76, 16, 6, 4.4), DARK, 'f', ln=True), L([(70, 18), (44, 24)], DARK, 'f', False, False, 1.4),
             L([(70, 86), (78, 94)], 'scar', 'f', False, False, 1.2)],
    'back': [L(blob(SKULL_B))] + back_hair(),
}

# ------------------------------------------------------------------ Tyler Thomas: cara alargada con una nariz larguísima, pelo
# negro peinado a raya con flequillo de lado, bigote retorcido en espiral y sonrisa
CHARS['tyler-thomas'] = {
    'body': 'delgado', 'pal': pal('#1e2014', '#e8b878', nose='#e0a068'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 99, 'face_front': LONG_FACE, 'big_ears': 1.5, 'ear_out': 3,
             'nose': (50, 86, 4.6), 'nose_side': (96, 84, 5), 'hairline': [(14, 60), (30, 44), (50, 40), (64, 50), (78, 56), (86, 62)]},
    'front': [L(blob([(14, 64), (12, 34), (24, 10), (50, 2), (76, 10), (88, 34), (86, 64)])),
              L(blob([(62, 10), (88, 32), (86, 62), (74, 58)], 6), 'shade', 'b', False), sheen(24, 48, 12, 3),
              L([(56, 62), (50, 74), (46, 86), (54, 86)], 'skin_d', 'f', False),
              L(quad((50, 93), (36, 90), (30, 96)) + quad((30, 96), (26, 101), (33, 100))[1:], OUTC, 'f', False, False, 2.2),
              L(quad((50, 93), (64, 90), (70, 96)) + quad((70, 96), (74, 101), (67, 100))[1:], OUTC, 'f', False, False, 2.2)],
    'side': [L(blob([(44, 78), (20, 74), (10, 50), (14, 24), (32, 4), (60, 0), (82, 10), (90, 28), (76, 34), (60, 38), (52, 52)])),
             L(blob([(14, 40), (18, 68), (38, 74), (28, 52)], 6), 'shade', 'b', False), sheen(32, 64, 10, 3),
             L(quad((90, 92), (82, 92), (78, 98)), OUTC, 'f', False, False, 1.4)],
    'back': [L(blob(SKULL_B))] + back_hair(),
}

# ------------------------------------------------------------------ Ian Suffolk: pelo castaño claro canoso peinado hacia atrás
# con raya marcada, gafas rectangulares y una sonrisa con los labios gruesos
CHARS['ian-suffolk'] = {
    'body': 'delgado', 'pal': pal('#a08a70', '#d8a060'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'lips', 'mouth_y': 96, 'mouth_w': 10, 'face_front': LONG_FACE, 'big_ears': 1,
             'glasses': (60, 70, 80, 255), 'glasses_rect': True, 'hairline': (52, 40)},
    'front': [L(blob([(14, 60), (12, 30), (24, 6), (50, -2), (76, 6), (88, 30), (86, 60)])),
              L(blob([(62, 6), (88, 28), (86, 58), (74, 54)], 6), 'shade', 'b', False)]
             + [strand([(x, 2 + abs(x - 50) * 0.3), (x + (x - 50) * 0.2, 40)], 'shade', 'b', 1.0) for x in (30, 40, 50, 60, 70)],
    'side': [L(blob([(44, 72), (20, 70), (10, 46), (14, 20), (32, 0), (60, -4), (84, 6), (92, 24), (78, 32), (62, 36), (52, 50)])),
             L(blob([(14, 36), (18, 64), (38, 70), (28, 48)], 6), 'shade', 'b', False)]
            + [strand([(90, 12 + k * 6), (56, 2 + k * 6), (24, 26 + k * 10)], 'shade', 'b', 1.0) for k in range(3)],
    'back': [L(blob(SKULL_B))] + back_hair() + [strand([(x, 10), (x, 80)], 'shade', 'b', 1.0) for x in (36, 50, 64)],
}

# ------------------------------------------------------------------ Ted Poe: pelo castaño abultado y despeinado, barba y bigote
# castaños que le enmarcan la cara y ojos entornados
CHARS['ted-poe'] = {
    'body': 'normal', 'pal': pal('#6a4834', '#e8a868'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'none', 'mouth_y': 96, 'hairline': (56, 46)},
    'front': [L(bumpy(50, 32, 46, 30, 14, 0.08)), spk((4, 50), (10, 64), (-10, 62), 4), spk((90, 64), (96, 50), (110, 62), 4, light_left=False),
              L(blob([(8, 66), (6, 40), (94, 40), (92, 66), (80, 58), (20, 58)])),
              L(bumpy(68, 34, 22, 20, 8, 0.08), 'shade', 'b', False), L(ell(30, 14, 10, 4), 'light', 'b', False),
              beard(), L(blob([(26, 86), (40, 82), (50, 86), (60, 82), (74, 86), (66, 94), (50, 92), (34, 94)], 5), 'mid', 'f', ln=True),
              L(quad((42, 98), (50, 102), (58, 98)), (130, 70, 50, 255), 'f', False, False, 1.4)],
    'side': [L(bumpy(42, 34, 46, 30, 14, 0.08)), L(blob(SIDE_SKULL)), L(bumpy(24, 46, 18, 22, 8, 0.08), 'shade', 'b', False),
             L(blob([(50, 62), (60, 62), (64, 84), (78, 100), (92, 98), (90, 108), (72, 114), (56, 100)]), 'mid', 'f', ln=True)],
    'back': [L(bumpy(50, 36, 46, 34, 14, 0.08)), L(blob([(8, 70), (6, 40), (94, 40), (92, 70), (70, 86), (30, 86)])),
             L(bumpy(66, 50, 22, 26, 8, 0.08), 'shade', 'b', False), L(ell(30, 16, 10, 4), 'light', 'b', False)],
}

# ------------------------------------------------------------------ Marshall Heart: cara muy alargada, melena lisa castaña hasta
# los hombros con raya en medio, coronilla rubia, arrugas y ceño serio
CHARS['marshall-heart'] = {
    'body': 'delgado', 'pal': pal('#7a5a44', '#f6b878', top='#b0a070'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 100, 'face_front': LONG_FACE, 'nose': (50, 86, 2.6),
             'hairline': [(14, 70), (26, 52), (40, 42), (50, 48), (60, 42), (74, 52), (86, 70)]},
    'front': [L(blob([(8, 112), (4, 60), (12, 18), (50, 4), (88, 18), (96, 60), (92, 112), (80, 108), (80, 70), (20, 70), (20, 108)])),
              L(blob([(62, 14), (94, 50), (90, 108), (82, 106)], 6), 'shade', 'b', False),
              L(blob([(20, 22), (50, 4), (80, 22), (70, 30), (50, 24), (30, 30)]), 'top', 'b', False),
              strand([(50, 6), (50, 46)], 'deep', 'b', 1.1),
              L(blob([(10, 56), (22, 58), (24, 100), (14, 112), (8, 90)]), 'mid', 'f'), L(blob([(90, 56), (78, 58), (76, 100), (86, 112), (92, 90)]), 'mid', 'f'),
              strand([(22, 60), (24, 100), (16, 110)], OUTC, 'f', 1.0), strand([(78, 60), (76, 100), (84, 110)], OUTC, 'f', 1.0),
              L(quad((26, 84), (30, 90), (32, 96)), 'skin_d', 'f', False, False, 1.0), L(quad((74, 84), (70, 90), (68, 96)), 'skin_d', 'f', False, False, 1.0)],
    'side': [L(blob([(56, 108), (14, 110), (2, 70), (6, 30), (26, 8), (56, 4), (82, 14), (94, 34), (92, 56), (76, 54), (64, 58), (60, 80), (60, 100)])),
             L(blob([(6, 50), (8, 102), (46, 106), (26, 74)], 6), 'shade', 'b', False),
             L(blob([(30, 10), (60, 4), (84, 14), (70, 20), (44, 18)]), 'top', 'b', False),
             strand([(22, 30), (16, 104)], 'shade', 'b', 1.0), strand([(40, 24), (36, 106)], 'shade', 'b', 1.0),
             spk((56, 30), (88, 40), (92, 64), 5, z='f', light_left=False)],
    'back': [L(blob([(8, 112), (4, 60), (12, 18), (50, 4), (88, 18), (96, 60), (92, 112), (76, 118), (64, 110), (50, 118), (36, 110), (24, 118)])),
             L(blob([(58, 14), (94, 50), (90, 110), (66, 114)], 6), 'shade', 'b', False),
             L(blob([(20, 24), (50, 4), (80, 24), (70, 34), (50, 30), (30, 34)]), 'top', 'b', False)]
            + [strand([(x, 30), (x + (x - 50) * 0.1, 110)], 'shade', 'b', 1.0) for x in (26, 40, 50, 60, 74)],
}

# ------------------------------------------------------------------ Dom Foreman: corpulento, piel morena, pañuelo blanco rosado
# atado a la cabeza con el nudo detrás, melena negra lisa que cae por los lados y la nuca; ojos redondos y cara larga
CHARS['dom-foreman'] = {
    'body': 'corpulento', 'pal': pal('#1e1610', '#c08a4a', wrap='#e8dcd0', wrap_d='#c0a8a0'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'face_front': LONG_FACE, 'nose': (50, 86, 3), 'hairline': False},
    'front': [L(blob([(10, 100), (8, 50), (92, 50), (90, 100), (80, 96), (80, 60), (20, 60), (20, 96)])),
              L(blob([(80, 56), (90, 60), (88, 96), (80, 94)], 5), 'shade', 'b', False),
              L(blob([(10, 58), (8, 30), (22, 8), (50, 0), (78, 8), (92, 30), (90, 58), (50, 54)]), 'wrap', 'f', ln=True),
              L(blob([(60, 4), (90, 28), (90, 56), (70, 54)], 6), 'wrap_d', 'f', False),
              L(blob([(12, 56), (24, 58), (24, 96), (14, 98)]), 'mid', 'f'), L(blob([(88, 56), (76, 58), (76, 96), (86, 98)]), 'mid', 'f')],
    'side': [L(blob([(50, 100), (14, 100), (6, 60), (40, 56), (60, 60), (58, 80)])),
             L(blob(SIDE_SKULL), 'skin'),
             L(blob([(50, 100), (16, 100), (8, 60), (40, 56), (56, 62), (54, 86)])),
             L(blob([(12, 60), (10, 28), (26, 6), (56, 0), (82, 8), (94, 30), (92, 54), (50, 56)]), 'wrap', 'f', ln=True),
             L(blob([(12, 40), (24, 12), (30, 54), (16, 58)], 6), 'wrap_d', 'f', False),
             L(blob([(12, 44), (0, 38), (-12, 46), (2, 52), (14, 52)], 4), 'wrap', 'f', ln=True), L(blob([(12, 50), (0, 58), (-6, 70), (8, 62)], 4), 'wrap_d', 'f', ln=True)],
    'back': [L(blob([(10, 102), (8, 50), (92, 50), (90, 102), (50, 106)])),
             L(blob([(58, 54), (90, 56), (88, 100), (66, 104)], 6), 'shade', 'b', False),
             L(blob([(10, 60), (8, 30), (22, 8), (50, 0), (78, 8), (92, 30), (90, 60), (50, 62)]), 'wrap', 'f', ln=True),
             L(blob([(56, 4), (90, 28), (90, 58), (64, 60)], 6), 'wrap_d', 'f', False),
             L(blob([(50, 58), (30, 52), (20, 62), (36, 66)], 4), 'wrap', 'f', ln=True), L(blob([(50, 58), (70, 52), (80, 62), (64, 66)], 4), 'wrap', 'f', ln=True),
             L(ell(50, 60, 5, 4), 'wrap_d', 'f', ln=True)],
}
