"""Inazuma Japón (IE3): los nuevos de la selección y el aspecto que tienen en IE3 los que ya estaban dibujados, con sus
modelos 3D como referencia (contornos calcados sobre una rejilla de unidades de cabeza). Jude lleva sus gafas de siempre. Las versiones de temporada van
con la clave 'ie3:<jugador>' y valen para todos los equipos de IE3."""
import copy

from chars import CHARS, L, OUTC, blob, ell, outline, pal, spk, strand
from chars_alius import SIDE_SKULL, SKULL_B, SKULL_F
from heads import quad

WHITE = (250, 250, 250, 255)

# Caleb Stonewall en IE3: el mismo peinado, pero ya sin el rayo rojo pintado en la sien
_caleb = copy.deepcopy(CHARS['caleb-stonewall'])
for _v in ('front', 'side', 'back'):
    _caleb[_v] = [l for it in _caleb[_v] for l in (it if isinstance(it, list) else [it]) if l['c'] != 'paint']
CHARS['ie3:caleb-stonewall'] = _caleb

# Xavier Foster en IE3 (humano, ya no Gran): media melena roja a capas, con mechones que le caen por la frente y uno entre
# los ojos, las puntas abiertas hacia fuera por encima de las orejas y la nuca; ojos verdes y media sonrisa
CHARS['ie3:xavier-foster'] = {
    'body': 'normal', 'pal': pal('#e0281a', '#fcdcc0', iris='#2a9a7a', shade='#b01a14', light='#ff6a50'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(8, 74), (-4, 66, 1), (6, 56), (2, 34), (14, 10), (36, -2), (60, -2), (82, 8), (96, 30), (96, 54), (106, 64, 1), (92, 72), (88, 66),
                         (14, 66)])),
              L(outline([(62, 2), (84, 12), (94, 34), (94, 56), (86, 60), (80, 32)]), 'shade', 'b', False),
              L(outline([(12, 70, 1), (14, 40), (26, 24), (46, 16), (66, 20), (82, 32), (88, 50), (88, 70, 1), (80, 56), (72, 64, 1), (66, 48), (56, 58), (50, 82, 1),
                         (44, 54), (38, 66, 1), (32, 52), (22, 64, 1), (18, 54)]), 'mid', 'f'),
              L(outline([(56, 22), (78, 30), (86, 48), (80, 54), (68, 38)]), 'shade', 'f', False),
              L(outline([(30, 26), (46, 20), (38, 30)]), 'light', 'f', False),
              strand([(52, 22), (50, 50), (50, 78)], 'shade', 'f', 1.0)],
    'side': [L(outline([(44, 94), (34, 98, 1), (22, 88), (6, 84, 1), (10, 70), (-2, 62, 1), (8, 52), (6, 30), (20, 10), (46, -2), (70, 0), (88, 14), (96, 34), (94, 52),
                        (86, 66, 1), (80, 50), (66, 46), (54, 60), (50, 80)])),
             L(outline([(10, 40), (34, 40), (46, 70), (40, 92), (20, 86), (10, 66)]), 'shade', 'b', False),
             spk((64, 26), (90, 34), (92, 62), 5, z='f', light_left=False)],
    'back': [L(outline([(-6, 70, 1), (6, 62), (4, 34), (16, 10), (40, -2), (64, -2), (86, 10), (96, 34), (94, 62), (106, 70, 1), (90, 80), (84, 94, 1), (70, 88),
                        (60, 98, 1), (50, 88), (40, 98, 1), (30, 88), (16, 94, 1), (10, 80)])),
             L(outline([(56, 2), (84, 14), (96, 40), (92, 80), (70, 90), (62, 50)]), 'shade', 'b', False)],
}

# Archer Hawkins: tupé enorme castaño rojizo en forma de abanico, plano por arriba y abierto en dos alas de pinchos a los
# lados de la cabeza, con un mechón que le cruza la frente; por detrás el pelo le cae hasta la nuca en punta y un mechón
# largo baja por el lado; ojos blancos redondos muy marcados de pupila pequeña
CHARS['archer-hawkins'] = {
    'body': 'normal', 'pal': pal('#7a3e4a', '#f8c088', shade='#5e2c38', light='#9a5a64'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': [L(ell(35, 75, 7.6, 7), WHITE, 'f', ln=True), L(ell(65, 75, 7.6, 7), WHITE, 'f', ln=True),
              L(ell(35, 75, 7.6, 7) + [ell(35, 75, 7.6, 7)[0]], OUTC, 'f', False, False, 2.2), L(ell(65, 75, 7.6, 7) + [ell(65, 75, 7.6, 7)[0]], OUTC, 'f', False, False, 2.2),
              L(ell(36, 76, 2.2, 2.4), OUTC, 'f', False), L(ell(64, 76, 2.2, 2.4), OUTC, 'f', False),
              L([(26, 64), (42, 66)], OUTC, 'f', False, False, 2.2), L([(74, 64), (58, 66)], OUTC, 'f', False, False, 2.2),
              L(outline([(16, 66), (12, 44), (4, 30), (-12, 30, 1), (-4, 20), (-14, 6, 1), (2, 8), (-2, -14, 1), (14, -4), (20, -18, 1), (32, -2), (50, -6),
                         (68, -2), (80, -18, 1), (86, -4), (102, -14, 1), (98, 8), (114, 6, 1), (104, 20), (112, 30, 1), (96, 30), (88, 44), (84, 66)])),
              L(outline([(60, -2), (80, -16, 1), (86, -2), (100, -12, 1), (96, 10), (110, 8, 1), (100, 22), (88, 40), (78, 20)]), 'shade', 'b', False),
              L(outline([(16, 66), (10, 80), (4, 108, 1), (18, 92), (22, 74)]), 'mid', 'b', ln=True),
              L(outline([(16, 60), (18, 40), (32, 28), (50, 24), (68, 28), (82, 40), (84, 60), (74, 46), (60, 44), (46, 64, 1), (40, 46), (28, 48)]), 'mid', 'f'),
              L(outline([(56, 28), (76, 34), (84, 54), (72, 44)]), 'shade', 'f', False),
              strand([(30, 4), (40, 20)], 'shade', 'f', 1.0), strand([(70, 4), (60, 20)], 'shade', 'f', 1.0)],
    'side': [L(outline([(44, 92), (22, 88), (14, 70), (6, 96), (2, 112, 1), (2, 84), (8, 56), (-4, 46, 1), (8, 40), (4, 22), (-8, 14, 1), (8, 10), (10, -8, 1), (26, 2),
                        (34, -16, 1), (44, 0), (66, -6), (86, 4), (100, 14), (106, 26), (104, 40), (98, 52, 1), (96, 36), (86, 30), (74, 40), (60, 46), (52, 62),
                        (50, 80)])),
             L(outline([(10, 44), (32, 48), (44, 80), (26, 88), (12, 70)]), 'shade', 'b', False),
             L(outline([(60, 2), (84, 4), (100, 16), (90, 22), (70, 14)]), 'light', 'b', False),
             L(ell(84, 75, 4.4, 6.4), WHITE, 'f', ln=True), L(ell(86, 76, 1.6, 2.2), OUTC, 'f', False), L([(76, 64), (88, 66)], OUTC, 'f', False, False, 2.2)],
    'back': [L(outline([(16, 70), (12, 44), (4, 30), (-12, 30, 1), (-4, 20), (-14, 6, 1), (2, 8), (-2, -14, 1), (14, -4), (20, -18, 1), (32, -2), (50, -6), (68, -2),
                        (80, -18, 1), (86, -4), (102, -14, 1), (98, 8), (114, 6, 1), (104, 20), (112, 30, 1), (96, 30), (88, 44), (84, 70), (70, 84), (56, 108, 1),
                        (50, 92), (44, 108, 1), (30, 84)])),
             L(outline([(58, 0), (86, 0), (100, 20), (86, 50), (80, 80), (60, 100)]), 'shade', 'b', False),
             strand([(50, 10), (50, 80)], 'deep', 'b', 1.0)],
}

# Austin Hobbes: pelo gris pizarra muy oscuro de pinchos largos que suben hacia arriba y hacia atrás, con un pico en medio de
# la frente; ojos verdes grandes y sonrisa
CHARS['austin-hobbes'] = {
    'body': 'delgado', 'pal': pal('#2e3a44', '#fcc890', iris='#1e7a5a', shade='#222a32', light='#4a5a66'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 94,
             'hairline': [(14, 66), (16, 48), (30, 42), (42, 46), (50, 58), (58, 46), (70, 42), (84, 48), (86, 66)]},
    'front': [L(outline([(12, 70), (8, 48), (-2, 40, 1), (8, 32), (2, 14, 1), (16, 14), (12, -8, 1), (26, 2), (28, -20, 1), (40, -4), (46, -26, 1), (54, -6),
                         (64, -22, 1), (68, -2), (82, -14, 1), (82, 6), (98, 4, 1), (90, 20), (104, 26, 1), (92, 36), (100, 46, 1), (90, 50), (88, 70), (82, 64),
                         (18, 64)])),
              L(outline([(58, -4), (64, -20, 1), (70, 0), (82, -12, 1), (84, 8), (96, 6, 1), (90, 22), (100, 28, 1), (90, 40), (86, 60), (76, 30)]), 'shade', 'b', False),
              L(outline([(26, 2), (28, -18, 1), (38, -2), (30, 14)]), 'light', 'b', False)],
    'side': [L(outline([(44, 92), (22, 88), (12, 66), (-4, 66, 1), (8, 54), (-8, 46, 1), (8, 38), (-2, 22, 1), (14, 22), (8, 2, 1), (24, 10), (24, -12, 1), (38, 4),
                        (44, -18, 1), (54, 2), (64, -12, 1), (68, 8), (82, 2, 1), (82, 18), (94, 22, 1), (88, 34), (76, 44), (60, 48), (52, 62), (50, 80)])),
             L(outline([(10, 44), (34, 44), (44, 78), (24, 88), (12, 66)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 76), (8, 48), (-2, 40, 1), (8, 32), (2, 14, 1), (16, 14), (12, -8, 1), (26, 2), (28, -20, 1), (40, -4), (46, -26, 1), (54, -6),
                        (64, -22, 1), (68, -2), (82, -14, 1), (82, 6), (98, 4, 1), (90, 20), (104, 26, 1), (92, 36), (100, 46, 1), (90, 50), (86, 76), (66, 88),
                        (50, 100, 1), (34, 88)])),
             L(outline([(58, -2), (84, 8), (94, 40), (86, 76), (64, 88)]), 'shade', 'b', False),
             L(outline([(36, 20), (44, 12), (50, 24), (42, 30)]), 'deep', 'b', False), L(outline([(58, 30), (66, 22), (70, 36), (62, 40)]), 'deep', 'b', False)],
}

# Thor Stoutberg: grandullón moreno de melena castaña oscura y lisa que le cae por los lados y la espalda hasta los
# hombros, con un mechón naranja en forma de llama de pie sobre la frente; patillas, perilla, cejas gruesas y una sonrisa
# enorme de dientes. Juega con la camiseta sin mangas
CHARS['thor-stoutberg'] = {
    'body': 'corpulento', 'sleeveless': True,
    'pal': pal('#4a2a20', '#c88a4a', skin_d='#a86e38', flame='#f08a20', flame_d='#c86010', iris='#1e1814'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 93, 'hairline': False, 'ears': False},
    'front': [L(outline([(16, 56), (12, 30), (24, 12), (50, 6), (76, 12), (88, 30), (84, 56), (90, 80), (104, 108, 1), (92, 104), (96, 118, 1), (84, 108), (80, 86),
                         (80, 64), (66, 50), (50, 58, 1), (34, 50), (20, 64), (20, 86), (16, 108), (4, 118, 1), (8, 104), (-4, 108, 1), (10, 80)])),
              L(outline([(60, 10), (82, 24), (88, 60), (96, 100), (84, 100), (80, 64), (72, 40)]), 'shade', 'b', False),
              L(outline([(36, 22), (34, 8), (40, -6, 1), (46, 4), (54, -30, 1), (60, -8), (74, -22, 1), (70, 2), (82, -2, 1), (64, 22)]), 'flame', 'f', ln=True),
              L(outline([(50, 18), (54, -4), (62, 0), (66, 6), (60, 18)]), 'flame_d', 'f', False),
              L(outline([(20, 64), (26, 70), (26, 88), (20, 84)]), 'mid', 'f'), L(outline([(80, 64), (74, 70), (74, 88), (80, 84)]), 'mid', 'f'),
              L(outline([(46, 100), (54, 100), (50, 108, 1)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(44, 92), (40, 104), (24, 110, 1), (24, 98), (8, 108, 1), (8, 92), (-4, 94, 1), (2, 70), (2, 40), (16, 16), (44, 4), (72, 6), (88, 22), (90, 40),
                        (78, 44), (62, 46), (54, 62), (52, 80)])),
             L(outline([(6, 40), (30, 40), (44, 74), (40, 100), (14, 104), (4, 80)]), 'shade', 'b', False),
             L(outline([(54, 10), (50, -14, 1), (62, -4), (70, -24, 1), (74, -2), (84, -10, 1), (80, 10), (70, 16)]), 'flame', 'f', ln=True),
             L(outline([(66, 60), (74, 64), (78, 84), (70, 82)]), 'mid', 'f'), L(outline([(84, 98), (90, 98), (88, 106, 1)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(2, 56), (6, 28), (22, 8), (50, 2), (78, 8), (94, 28), (98, 56), (100, 90), (110, 110, 1), (92, 104), (86, 118, 1), (72, 104), (60, 116, 1),
                        (50, 104), (40, 116, 1), (28, 104), (14, 118, 1), (8, 104), (-10, 110, 1), (0, 90)])),
             L(outline([(56, 6), (86, 18), (98, 60), (100, 96), (80, 104), (66, 70)]), 'shade', 'b', False),
             strand([(26, 40), (20, 100)], 'deep', 'b', 1.0), strand([(50, 30), (50, 104)], 'deep', 'b', 1.0), strand([(74, 40), (80, 100)], 'deep', 'b', 1.0),
             L(outline([(36, 12), (30, -10, 1), (42, 0), (48, -22, 1), (56, -2), (68, -14, 1), (64, 10)]), 'flame_d', 'f', ln=True)],
}

# Jordan Greenway en IE3: el pelo verde claro recogido atrás en una coleta alta que cae gruesa hasta la espalda, con dos
# mechones largos que le enmarcan la cara y un flequillo en pico
CHARS['ie3:jordan-greenway'] = {
    'body': 'normal', 'pal': pal('#a8b850', '#fcc490', iris='#1e1a1a', shade='#86924a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(14, 66), (10, 36), (22, 12), (50, 2), (78, 12), (90, 36), (86, 66)])),
              L(outline([(60, 6), (82, 18), (90, 44), (84, 62), (76, 36)]), 'shade', 'b', False),
              L(outline([(12, 60), (14, 38), (28, 24), (50, 20), (72, 24), (86, 38), (88, 60), (76, 46), (60, 44), (50, 62, 1), (40, 44), (24, 46)]), 'mid', 'f'),
              L(outline([(56, 24), (76, 30), (86, 48), (74, 44)]), 'shade', 'f', False),
              L(outline([(14, 56), (22, 58), (20, 84), (16, 104, 1), (12, 82)]), 'mid', 'f', ln=True),
              L(outline([(86, 56), (78, 58), (80, 84), (84, 104, 1), (88, 82)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(26, 20), (10, 30), (-4, 60), (-8, 100), (-6, 124, 1), (4, 98), (10, 66), (24, 40)]), 'shade', 'b', ln=True),
             L(outline([(44, 92), (22, 88), (12, 64), (12, 36), (24, 14), (52, 4), (76, 10), (90, 28), (88, 44), (74, 46), (60, 48), (52, 62), (50, 80)])),
             L(outline([(14, 40), (34, 44), (42, 80), (22, 86), (12, 64)]), 'shade', 'b', False),
             L(ell(24, 22, 5, 5), 'shade', 'b', ln=True),
             L(outline([(62, 30), (88, 38), (90, 64), (88, 100, 1), (80, 70), (70, 48)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(12, 82), (10, 36), (22, 12), (50, 2), (78, 12), (90, 36), (88, 82), (50, 88)])),
             L(outline([(58, 6), (86, 26), (90, 60), (84, 80), (66, 84)]), 'shade', 'b', False),
             strand([(30, 10), (40, 30)], 'shade', 'b', 1.0), strand([(70, 10), (60, 30)], 'shade', 'b', 1.0),
             L(outline([(40, 26), (60, 26), (64, 60), (62, 100), (54, 126, 1), (46, 104), (38, 64)]), 'mid', 'f', ln=True),
             L(outline([(52, 30), (60, 30), (62, 70), (56, 110), (52, 70)]), 'shade', 'f', False),
             L(ell(50, 28, 7, 3), 'shade', 'f', ln=True)],
}

# Paul Peabody: pelo verde musgo despeinado y abultado, con mechones en punta que le caen por la frente, las sienes y la
# nuca, y dos pelos de punta arriba; ojos negros enormes y redondos, coloretes y sonrisa
CHARS['paul-peabody'] = {
    'body': 'bajito', 'pal': pal('#5e7a3a', '#fcc890', shade='#465e2a', blush='#f0a080'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(8, 76, 1), (6, 56), (-6, 46, 1), (4, 34), (12, 14), (30, 2), (36, -10, 1), (44, 0), (56, -2), (66, -12, 1), (68, 2), (84, 10), (94, 32),
                         (106, 44, 1), (94, 54), (92, 76, 1), (84, 64), (16, 64)])),
              L(outline([(60, 2), (84, 12), (94, 36), (90, 64), (78, 40)]), 'shade', 'b', False),
              L(outline([(12, 70, 1), (14, 42), (28, 26), (50, 20), (72, 26), (86, 42), (88, 70, 1), (80, 54), (72, 64, 1), (64, 48), (56, 60, 1), (50, 46), (42, 60, 1),
                         (36, 48), (26, 64, 1), (20, 54)]), 'mid', 'f'),
              L(outline([(56, 24), (78, 32), (86, 52), (76, 50), (68, 38)]), 'shade', 'f', False),
              L(ell(35, 76, 6.2, 6.6), WHITE, 'f', ln=True), L(ell(65, 76, 6.2, 6.6), WHITE, 'f', ln=True),
              L(ell(35, 76, 4.6, 5), OUTC, 'f', False), L(ell(65, 76, 4.6, 5), OUTC, 'f', False),
              L(ell(33.6, 74.4, 1.4, 1.4), WHITE, 'f', False), L(ell(63.6, 74.4, 1.4, 1.4), WHITE, 'f', False),
              L(ell(24, 86, 4, 2.4), 'blush', 'f', False), L(ell(76, 86, 4, 2.4), 'blush', 'f', False)],
    'side': [L(outline([(44, 94), (30, 98, 1), (20, 88), (-2, 88, 1), (6, 70), (-6, 60, 1), (6, 50), (4, 28), (18, 8), (40, -2), (48, -14, 1), (54, 0), (72, 4), (88, 18),
                        (94, 40, 1), (80, 40), (64, 46), (54, 62), (50, 80)])),
             L(outline([(8, 46), (32, 48), (40, 84), (20, 86), (8, 66)]), 'shade', 'b', False),
             L(ell(84, 76, 3.6, 6), WHITE, 'f', ln=True), L(ell(85, 76, 2.6, 4.6), OUTC, 'f', False),
             spk((60, 30), (88, 40), (92, 66), 4, z='f', light_left=False)],
    'back': [L(outline([(-4, 72, 1), (6, 60), (4, 32), (16, 10), (36, 0), (44, -12, 1), (52, 0), (64, -8, 1), (68, 4), (84, 12), (96, 32), (94, 60), (104, 72, 1),
                        (86, 80), (70, 76), (50, 84), (30, 76), (14, 80)])),
             L(outline([(8, 50), (50, 40), (92, 50), (100, 70), (80, 78), (50, 82), (20, 78), (0, 70)]), 'shade', 'b', False)],
}

# Isaac Glass: pelo castaño muy oscuro corto, con flequillo de mechones finos y las puntas abiertas por encima de las
# orejas; gafas de montura negra con la patilla verde y media sonrisa pícara
CHARS['isaac-glass'] = {
    'body': 'normal', 'pal': pal('#2e2018', '#fcc890', iris='#1e1814', rim='#1e1e1e', arm='#3a8a5a'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(12, 70), (8, 56), (-4, 50, 1), (8, 44), (8, 30), (20, 10), (50, 2), (80, 10), (92, 30), (92, 44), (104, 50, 1), (92, 56), (88, 70), (80, 64),
                         (20, 64)])),
              L(outline([(60, 6), (84, 16), (92, 40), (88, 62), (78, 36)]), 'shade', 'b', False),
              L(outline([(12, 64), (14, 40), (28, 26), (50, 20), (72, 26), (86, 40), (88, 64, 1), (80, 50), (68, 56, 1), (62, 44), (52, 52, 1), (44, 40), (34, 56, 1),
                         (30, 44), (20, 60, 1)]), 'mid', 'f'),
              L(outline([(56, 24), (78, 32), (86, 50), (74, 44)]), 'shade', 'f', False),
              L(outline([(22, 68), (46, 68), (46, 82), (24, 82)]) + [outline([(22, 68), (46, 68), (46, 82), (24, 82)])[0]], 'rim', 'f', False, False, 2.0),
              L(outline([(78, 68), (54, 68), (54, 82), (76, 82)]) + [outline([(78, 68), (54, 68), (54, 82), (76, 82)])[0]], 'rim', 'f', False, False, 2.0),
              L([(46, 72), (54, 72)], 'arm', 'f', False, False, 1.6), L([(14, 72), (22, 72)], 'arm', 'f', False, False, 1.6),
              L([(78, 72), (86, 72)], 'arm', 'f', False, False, 1.6)],
    'side': [L(outline([(44, 92), (22, 88), (12, 66), (0, 58, 1), (12, 54), (12, 30), (26, 10), (54, 2), (78, 10), (92, 30), (90, 46), (76, 46), (62, 48), (52, 62),
                        (50, 80)])),
             L(outline([(14, 40), (36, 44), (42, 80), (22, 86), (12, 66)]), 'shade', 'b', False),
             L(outline([(76, 68), (92, 68), (92, 82), (78, 82)]) + [outline([(76, 68), (92, 68), (92, 82), (78, 82)])[0]], 'rim', 'f', False, False, 2.0),
             L([(50, 72), (76, 72)], 'arm', 'f', False, False, 1.8),
             spk((60, 28), (88, 38), (90, 60), 4, z='f', light_left=False)],
    'back': [L(outline([(12, 80), (8, 56), (-4, 50, 1), (8, 44), (8, 30), (20, 10), (50, 2), (80, 10), (92, 30), (92, 44), (104, 50, 1), (92, 56), (88, 80), (50, 88)])),
             L(outline([(58, 6), (86, 22), (92, 50), (86, 78), (64, 86)]), 'shade', 'b', False),
             L([(14, 72), (86, 72)], 'arm', 'f', False, False, 1.4)],
}

# Dave Quagmire (humano, en Neo Japón): pelo negro azulado recogido en un moño alto y ancho como un abanico, con dos
# mechones largos que le caen por delante de las orejas hasta el cuello y se abren en punta; cara alargada pálida, ojos
# naranjas rasgados y media sonrisa
CHARS['ie3:dave-quagmire'] = {
    'body': 'normal', 'pal': pal('#24303a', '#fce8c8', iris='#d0601a', shade='#1a2228'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': [(16, 60), (20, 40), (36, 32), (50, 34), (64, 32), (80, 40), (84, 60)]},
    'front': [L(outline([(16, 64), (14, 30), (24, 16), (6, 6, 1), (26, 0), (40, -12), (60, -12), (74, 0), (94, 6, 1), (76, 16), (86, 30), (84, 64)])),
              L(outline([(60, -8), (76, 2), (90, 6, 1), (76, 16), (84, 34), (82, 60), (74, 30)]), 'shade', 'b', False),
              L(quad((24, 16), (50, 10), (76, 16)), 'shade', 'b', False, False, 1.4),
              L(outline([(14, 50), (22, 52), (24, 80), (20, 100), (26, 112, 1), (12, 104), (10, 80)]), 'mid', 'f', ln=True),
              L(outline([(86, 50), (78, 52), (76, 80), (80, 100), (74, 112, 1), (88, 104), (90, 80)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(44, 92), (22, 88), (14, 64), (8, 80), (-10, 104, 1), (-2, 80), (8, 54), (10, 30), (20, 12), (12, -12, 1), (32, 0), (50, -10), (66, -12, 1),
                        (70, 8), (86, 22), (88, 40), (76, 44), (62, 46), (54, 62), (50, 80)])),
             L(outline([(12, 40), (32, 44), (40, 84), (22, 88), (12, 64)]), 'shade', 'b', False),
             L(outline([(52, 54), (60, 56), (58, 96), (50, 108, 1), (48, 80)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(16, 84), (10, 40), (22, 18), (4, 8, 1), (24, 0), (40, -12), (60, -12), (76, 0), (96, 8, 1), (78, 18), (90, 40), (84, 84), (70, 92),
                        (62, 108, 1), (56, 92), (50, 104, 1), (44, 92), (38, 108, 1), (30, 92)])),
             L(outline([(56, -8), (78, 4), (92, 40), (84, 82), (66, 90), (62, 40)]), 'shade', 'b', False),
             L(outline([(36, 20), (50, 54, 1), (64, 20)]), 'shade', 'b', False)],
}
# Zeke Valanche (humano, en Neo Japón): piel morena; pelo blanco rosado peinado hacia atrás y a un lado, con un mechón en
# punta que se levanta por su izquierda y puntas cortas en la nuca; ojos naranjas de pillo y sonrisa de dientes
CHARS['ie3:zeke-valanche'] = {
    'body': 'normal', 'pal': pal('#f2e4e0', '#9a6440', iris='#d0601a', shade='#c8a8a8', light=WHITE),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(10, 74), (6, 40), (18, 14), (44, 2), (70, 4), (88, 14), (96, -8, 1), (92, 20), (104, 46, 1), (92, 50), (90, 74), (82, 64), (18, 64)])),
              L(outline([(62, 6), (86, 16), (94, -4, 1), (90, 24), (100, 44, 1), (88, 46), (78, 30)]), 'shade', 'b', False),
              L(outline([(12, 66, 1), (14, 40), (28, 22), (52, 14), (74, 20), (88, 38), (88, 60, 1), (78, 44), (62, 34), (44, 36), (30, 46), (22, 62, 1), (18, 50)]), 'mid', 'f'),
              L(outline([(30, 24), (52, 16), (68, 22), (48, 26)]), 'light', 'f', False),
              L(outline([(8, 66), (2, 86, 1), (14, 76)]), 'mid', 'f', ln=True), L(outline([(92, 66), (98, 86, 1), (86, 76)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(44, 92), (34, 100, 1), (24, 90), (10, 96, 1), (12, 80), (0, 76, 1), (8, 60), (6, 36), (20, 12), (48, 2), (74, 6), (90, 20), (94, 34), (86, 44),
                        (70, 44), (58, 50), (52, 64), (50, 80)])),
             L(outline([(8, 40), (40, 30), (54, 46), (46, 88), (26, 92), (10, 70)]), 'shade', 'b', False)],
    'back': [L(outline([(10, 84), (0, 92, 1), (8, 74), (6, 40), (18, 12), (50, 2), (82, 12), (96, -6, 1), (92, 22), (94, 40), (92, 74), (100, 92, 1), (88, 86), (76, 98, 1),
                        (64, 88), (50, 100, 1), (36, 88), (24, 98, 1)])),
             L(outline([(10, 50), (50, 30), (90, 46), (90, 80), (50, 96), (12, 82)]), 'shade', 'b', False)],
}

# En IE3 los del Zeus ya no llevan la tela cruzada de su equipo (Byron juega con los Dragones de Fuego)
for _k in [k for k, v in list(CHARS.items()) if ':' not in k and v.get('sash')]:
    CHARS['ie3:' + _k] = dict(CHARS[_k], sash=None)
