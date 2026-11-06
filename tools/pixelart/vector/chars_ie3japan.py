"""Inazuma Japón (IE3): los nuevos de la selección y el aspecto que tienen en IE3 los que ya estaban dibujados, con sus
modelos 3D como referencia (contornos calcados sobre una rejilla de unidades de cabeza). Las versiones de temporada van
con la clave 'ie3:<jugador>' y valen para todos los equipos de IE3."""
import copy

from chars import CHARS, L, OUTC, blob, ell, outline, pal, spk, strand
from chars_alius import SIDE_SKULL, SKULL_B, SKULL_F
from heads import quad

WHITE = (250, 250, 250, 255)

# Jude Sharp en IE3: el mismo peinado de rastas, pero sin las gafas (el modelo de IE3 no las lleva): ojos rojos, cejas
# marcadas y media sonrisa; la capa roja sigue
_jude = copy.deepcopy(CHARS['jude-sharp'])
for _v in ('front', 'side', 'back'):
    _flat = [l for it in _jude[_v] for l in (it if isinstance(it, list) else [it])]
    _jude[_v] = [l for l in _flat if l['c'] not in ('strap', 'rim', 'lens', 'lens_l')]
# por delante el modelo de IE3 deja la frente al aire: fuera la fila de rastas que bajaba hasta los ojos
_jude['front'] = [l for l in _jude['front'] if not (min(y for _, y in l['s']) >= 50 and 22 < sum(x for x, _ in l['s']) / len(l['s']) < 78)]
_jude['pal'] = dict(_jude['pal'], iris=(176, 30, 40, 255))
_jude['face'] = {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 94, 'hairline': (58, 50)}
CHARS['ie3:jude-sharp'] = _jude

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
