"""Épsilon y Épsilon Plus (IE2): la versión alienígena de la Academia Alius (Dvalin/Desarm, Zel, Metron...), con los
modelos 3D de la wiki (Desarm, Zel, Macure) y los retratos. Van por equipo ('<equipo>:<jugador>') porque Dave Quagmire,
Zeke Valanche y Ronny Metcalf salen también con su aspecto humano en otros equipos (Neo Japón, Academia Alia...)."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, pal, sheen, spk, strand
from chars_otaku import back_hair
from chars_sengoku import wavy
from heads import quad

WHITE = (255, 255, 255, 255)
SIDE_SKULL = [(44, 92), (22, 88), (12, 64), (14, 36), (30, 16), (56, 10), (78, 18), (88, 36), (76, 44), (60, 48), (52, 62), (50, 80)]
SKULL_F = [(16, 64), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 64)]
SKULL_B = [(16, 70), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 70), (66, 86), (34, 86)]
LONG_FACE = quad((20, 52), (18, 104), (50, 114)) + quad((50, 114), (82, 104), (80, 52))[1:] + quad((80, 52), (50, 26), (20, 52))[1:-1]
E = {}


def bald(view, c='skin', cd='skin_d'):
    if view == 'front':
        return [L(blob(SKULL_F), c), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), cd, 'b', False)]
    if view == 'side':
        return [L(blob(SIDE_SKULL), c)]
    return [L(blob(SKULL_B), c), L(blob([(58, 12), (86, 36), (84, 68), (66, 84)], 6), cd, 'b', False)]


# ------------------------------------------------------------------ Dvalin (Desarm, el capitán): melena azul marino oscura enorme de
# mechones en capas que sube hacia atrás como un cono, un cuello alto de tela oscura que le tapa la barbilla, piel pálida,
# ojos naranjas y sonrisa maligna
def jag(pts, depth=7, n=None):
    """Contorno de mechones en capas: entre cada par de puntos, una punta hacia fuera."""
    import math
    out = []
    for i in range(len(pts)):
        a, b = pts[i], pts[(i + 1) % len(pts)]
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        dx, dy = b[0] - a[0], b[1] - a[1]
        ln = math.hypot(dx, dy) or 1
        out += [a, (mx + dy / ln * depth, my - dx / ln * depth)]
    return out


# melena: un bloque alto de mechones en capas que sube hacia atrás
DES_MANE_F = [L(jag([(2, 86), (-2, 56), (2, 28), (14, 6), (32, -12), (50, -22), (68, -12), (86, 6), (98, 28), (102, 56), (98, 86)], 8)),
              L(blob([(60, -10), (94, 24), (98, 80), (84, 76)], 6), 'shade', 'b', False)] \
             + [strand([(10 + k * 3, 20 + k * 14), (50, 6 + k * 14), (90 - k * 3, 20 + k * 14)], 'deep', 'b', 1.2) for k in range(4)]
E['dave-quagmire'] = {
    'body': 'normal', 'pal': pal('#24303e', '#f4dca4', iris='#e05010', cowl='#2a323e', cowl_d='#1a2028'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 90, 'face_front': LONG_FACE, 'hairline': [(16, 72), (24, 54), (40, 40), (50, 48), (60, 40), (76, 54), (84, 72)]},
    'front': DES_MANE_F + [
                           spk((12, 46), (26, 40), (18, 84), 4, z='f'), spk((74, 40), (88, 46), (82, 84), 4, z='f', light_left=False),
                           spk((40, 34), (50, 30), (46, 54), 3, z='f'), spk((50, 30), (60, 34), (54, 54), 3, z='f', light_left=False),
                           L(blob([(6, 92), (14, 80), (28, 96), (50, 106), (72, 96), (86, 80), (94, 92), (90, 116), (50, 124), (10, 116)]), 'cowl', 'f', ln=True),
                           L(blob([(56, 104), (86, 84), (90, 114), (56, 120)], 5), 'cowl_d', 'f', False)],
    'side': [L(jag([(50, 92), (14, 92), (-6, 60), (-10, 24), (4, -6), (28, -24), (56, -20), (80, -2), (94, 26), (88, 46), (74, 44), (60, 50), (54, 70)], 8)),
             strand([(70, -6), (30, 0), (2, 30)], 'deep', 'b', 1.2), strand([(80, 14), (40, 18), (0, 54)], 'deep', 'b', 1.2),
             L(blob([(8, 46), (12, 84), (40, 88), (24, 60)], 6), 'shade', 'b', False),
             spk((58, 26), (88, 36), (92, 66), 5, z='f', light_left=False),
             L(blob([(30, 90), (60, 92), (90, 98), (92, 112), (60, 120), (26, 112)]), 'cowl', 'f', ln=True)],
    'back': [L(jag([(2, 84), (-2, 56), (2, 28), (14, 6), (32, -12), (50, -22), (68, -12), (86, 6), (98, 28), (102, 56), (98, 84), (50, 88)], 8)),
             L(blob([(58, -8), (96, 30), (96, 80), (66, 84)], 6), 'shade', 'b', False)]
            + [strand([(4 + k * 2, 10 + k * 16), (50, -4 + k * 16), (96 - k * 2, 10 + k * 16)], 'deep', 'b', 1.2) for k in range(4)] + [
                          L(blob([(8, 96), (50, 102), (92, 96), (90, 116), (50, 122), (10, 116)]), 'cowl', 'f', ln=True)],
}
E['dave-quagmire-desarm-cc'] = E['dave-quagmire']

# ------------------------------------------------------------------ Zel: piel morena, pelo blanco peinado hacia arriba y a un lado
# con un mechón en punta, ojos rojos y sonrisa con colmillos
E['zeke-valanche'] = {
    'body': 'normal', 'pal': pal('#ece4e0', '#a06a44', iris='#d0301a', shade='#c8b4b0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 92, 'hairline': (58, 50)},
    'front': [spk((52, 10), (70, 14), (92, -14), 6, light_left=False), spk((32, 12), (52, 8), (44, -10), 5),
              L(blob([(10, 74), (8, 40), (20, 14), (50, 6), (80, 14), (92, 40), (90, 74), (80, 66), (20, 66)])),
              spk((6, 60), (12, 74), (-6, 80), 4), spk((88, 74), (94, 60), (106, 80), 4, light_left=False),
              L(blob([(62, 12), (90, 38), (88, 70), (78, 66)], 6), 'shade', 'b', False),
              spk((12, 46), (30, 38), (18, 70), 5, z='f'), spk((30, 38), (50, 32), (40, 58), 5, z='f'),
              spk((50, 32), (70, 36), (62, 58), 5, z='f', light_left=False), spk((70, 38), (88, 46), (84, 70), 5, z='f', light_left=False)],
    'side': [spk((40, 10), (60, 6), (64, -20), 6, light_left=False), spk((18, 34), (30, 16), (-6, 10), 6),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((14, 60), (18, 44), (-8, 58), 5), spk((18, 76), (24, 62), (0, 86), 4),
             spk((56, 30), (88, 40), (92, 66), 5, z='f', light_left=False)],
    'back': [spk((52, 10), (70, 14), (92, -14), 6, light_left=False), spk((32, 12), (52, 8), (44, -10), 5),
             L(blob([(10, 76), (8, 40), (20, 14), (50, 6), (80, 14), (92, 40), (90, 76), (66, 88), (34, 88)])),
             spk((12, 74), (30, 86), (8, 98), 5), spk((30, 88), (50, 90), (40, 104), 5), spk((50, 90), (70, 88), (62, 104), 5, light_left=False),
             spk((70, 86), (88, 74), (92, 98), 5, light_left=False),
             L(blob([(58, 12), (90, 38), (88, 74), (66, 86)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Kenvil: piel tostada pálida, pelo granate de pinchos altos hacia
# arriba, orejas puntiagudas y una sonrisa enorme con dientes
E['craven-kenville'] = {
    'body': 'normal', 'pal': pal('#7a1428', '#d8c098'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 90, 'big_ears': 1, 'ear_out': 5, 'hairline': (56, 48)},
    'front': [spk((14, 40), (26, 22), (6, -6), 6), spk((26, 20), (44, 12), (30, -20), 6), spk((44, 12), (58, 12), (52, -26), 6),
              spk((58, 12), (74, 20), (76, -20), 6, light_left=False), spk((74, 22), (86, 40), (96, -4), 6, light_left=False),
              L(blob([(14, 62), (12, 36), (24, 14), (50, 8), (76, 14), (88, 36), (86, 62)])),
              L(blob([(62, 14), (88, 36), (86, 60), (74, 56)], 6), 'shade', 'b', False),
              spk((22, 44), (40, 40), (30, 58), 4, z='f'), spk((60, 40), (78, 44), (70, 58), 4, z='f', light_left=False)],
    'side': [spk((18, 36), (28, 18), (-6, 6), 7), spk((28, 18), (46, 10), (24, -20), 7), spk((46, 10), (64, 10), (56, -24), 6),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False)],
    'back': [spk((14, 40), (26, 22), (6, -6), 6), spk((26, 20), (44, 12), (30, -20), 6), spk((44, 12), (58, 12), (52, -26), 6),
             spk((58, 12), (74, 20), (76, -20), 6, light_left=False), spk((74, 22), (86, 40), (96, -4), 6, light_left=False),
             L(blob(SKULL_B))] + back_hair(),
}

# ------------------------------------------------------------------ Mole: una capucha roja con forma de corazón y dos alas en punta a
# los lados que le enmarca la cara, y una mascarilla gris con un tubo; ojos azules
E['anna-mole'] = {
    'body': 'chica', 'pal': pal('#a8243a', '#f6d4b8', iris='#3a5a9a', hood='#a8243a', hood_d='#7a1428', mask='#9a9aa4', mask_d='#6a6a74'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'none', 'ears': False, 'hairline': False},
    'front': [L(blob([(-14, 22), (10, 30), (30, 4), (50, 16), (70, 4), (90, 30), (114, 22), (96, 52), (90, 88), (80, 66), (20, 66), (10, 88), (4, 52)]), 'hood', 'f', ln=True),
              L(blob([(70, 8), (90, 30), (110, 24), (94, 50), (88, 82), (80, 62)], 6), 'hood_d', 'f', False),
              L(blob([(30, 82), (50, 78), (70, 82), (68, 96), (50, 102), (32, 96)]), 'mask', 'f', ln=True),
              L(quad((64, 94), (76, 104), (70, 116)), 'mask_d', 'f', False, False, 3.0)],
    'side': [L(blob(SIDE_SKULL)),
             L(blob([(8, 96), (0, 50), (10, 14), (36, -2), (66, 4), (88, 22), (96, 50), (84, 62), (66, 58), (56, 74), (54, 96)]), 'hood', 'f', ln=True),
             L(blob([(10, 30), (-10, 22), (2, 44)], 4), 'hood_d', 'f', ln=True),
             L(blob([(74, 80), (92, 82), (92, 96), (76, 98)]), 'mask', 'f', ln=True), L(quad((76, 96), (64, 104), (60, 116)), 'mask_d', 'f', False, False, 3.0)],
    'back': [L(blob([(-14, 22), (10, 30), (30, 4), (50, 16), (70, 4), (90, 30), (114, 22), (96, 52), (92, 96), (50, 104), (8, 96), (4, 52)]), 'hood', 'f', ln=True),
             L(blob([(56, 10), (90, 30), (108, 24), (94, 50), (90, 94), (60, 100)], 6), 'hood_d', 'f', False)],
}

# ------------------------------------------------------------------ Keison: un gorro negro redondo calado hasta los ojos con un
# mechón verde largo que le cae por delante de un ojo, piel pálida, barba oscura en la mandíbula y un ojo naranja
E['kayson-wattever'] = {
    'body': 'normal', 'pal': pal('#1e8a5a', '#f6dcb0', iris='#e07a10', hat='#26262c', hat_d='#141418', beard='#4a3a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'face_front': LONG_FACE, 'big_ears': 1, 'ear_out': 4, 'hairline': False},
    'front': [L(blob([(22, 92), (30, 86), (50, 90), (70, 86), (78, 92), (66, 110), (50, 116), (34, 110)]), 'beard', 'f', False),
              L(blob([(8, 56), (6, 30), (20, 6), (50, -2), (80, 6), (94, 30), (92, 56), (50, 52)]), 'hat', 'f', ln=True),
              L(blob([(62, 2), (92, 28), (92, 54), (72, 52)], 6), 'hat_d', 'f', False),
              L(blob([(30, 40), (46, 36), (44, 70), (34, 104), (24, 100), (30, 70)]), 'mid', 'f', ln=True),
              L(blob([(38, 42), (44, 40), (42, 70), (32, 100), (34, 70)], 5), 'shade', 'f', False)],
    'side': [L(blob(SIDE_SKULL)),
             L(blob([(10, 58), (8, 28), (24, 6), (54, -2), (82, 6), (96, 28), (96, 54), (50, 54)]), 'hat', 'f', ln=True),
             L(blob([(72, 84), (94, 86), (92, 104), (78, 110), (64, 96)]), 'beard', 'f', False),
             L(blob([(84, 44), (94, 46), (92, 76), (86, 100), (80, 76)]), 'mid', 'f', ln=True)],
    'back': [L(blob(SKULL_B), 'shade'), L(blob([(8, 64), (6, 30), (20, 6), (50, -2), (80, 6), (94, 30), (92, 64), (50, 68)]), 'hat', 'f', ln=True),
             L(blob([(58, 2), (92, 28), (92, 62), (66, 66)], 6), 'hat_d', 'f', False)],
}

# ------------------------------------------------------------------ Titan: corpulento, piel naranja, una visera gris que le cruza la
# cara con dos ojos rojos brillantes, antenas moradas en lo alto y una sonrisa de dientes apretados
E['mike-tytan'] = {
    'body': 'corpulento', 'pal': pal('#7a4a7a', '#f0a868', visor='#b8bcc4', visor_d='#888c94', glow='#e02010'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 92, 'ears': False, 'hairline': False},
    'front': bald('front') + [spk((40, 14), (48, 10), (32, -16), 3), spk((48, 10), (56, 10), (50, -20), 3), spk((56, 10), (64, 14), (70, -14), 3, light_left=False),
                              L(blob([(4, 64), (8, 56), (92, 56), (96, 64), (94, 80), (6, 80)], 4), 'visor', 'f', ln=True),
                              L([(20, 62), (80, 62), (78, 74), (22, 74)], (40, 30, 36, 255), 'f', False),
                              L(ell(36, 68, 4.4, 4), 'glow', 'f', False), L(ell(64, 68, 4.4, 4), 'glow', 'f', False)],
    'side': bald('side') + [spk((40, 10), (50, 8), (36, -18), 3), spk((50, 8), (58, 10), (56, -18), 3, light_left=False),
                            L(blob([(40, 56), (96, 58), (98, 78), (40, 80)], 4), 'visor', 'f', ln=True), L(ell(88, 68, 3.4, 4), 'glow', 'f', False)],
    'back': bald('back') + [spk((40, 14), (48, 10), (32, -16), 3), spk((56, 10), (64, 14), (70, -14), 3, light_left=False),
                            L(blob([(4, 64), (8, 56), (92, 56), (96, 64), (94, 80), (6, 80)], 4), 'visor', 'f', ln=True)],
}

# ------------------------------------------------------------------ Fadra: piel morena, cabeza calva en forma de cono con una franja
# de pelo azul claro en el centro, orejas puntiagudas, ojos rasgados y sonrisa enorme
FADRA_F = [(14, 66), (14, 40), (30, 10), (50, -14), (70, 10), (86, 40), (86, 66)]
E['mads-hatter'] = {
    'body': 'normal', 'pal': pal('#5a9ac0', '#8a5a3a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 90, 'big_ears': 1.5, 'ear_out': 6, 'hairline': False},
    'front': [L(blob(FADRA_F), 'skin'), L(blob([(62, 6), (86, 40), (84, 64), (72, 60)], 6), 'skin_d', 'b', False),
              L(blob([(44, 20), (48, 0), (50, -12), (52, 0), (56, 20), (50, 40)]), 'mid', 'b', ln=True)],
    'side': [L(blob([(44, 92), (22, 88), (12, 64), (14, 36), (34, 6), (56, -12), (70, 10), (88, 36), (76, 44), (60, 48), (52, 62), (50, 80)]), 'skin'),
             L(blob([(40, 6), (56, -10), (62, 4), (46, 20)]), 'mid', 'b', ln=True)],
    'back': [L(blob(FADRA_F + [(66, 86), (34, 86)]), 'skin'), L(blob([(58, 6), (86, 40), (84, 70), (66, 84)], 6), 'skin_d', 'b', False),
             L(blob([(44, 20), (48, 0), (50, -12), (52, 0), (56, 20), (50, 60)]), 'mid', 'b', ln=True)],
}

# ------------------------------------------------------------------ Krypto: melena rubia ceniza en grandes rizos enrollados que le
# enmarcan la cara y un turbante azul con una joya roja en lo alto; ojos rojos
E['karen-ripton'] = {
    'body': 'chica', 'pal': pal('#c8bc94', '#f6dcc0', iris='#c02a2a', band='#2a7aa8', band_d='#1e5a80', gem='#c82a2a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 92, 'ears': False, 'hairline': False},
    'front': [L(bumpy(12, 56, 14, 18, 8, 0.1)), L(bumpy(88, 56, 14, 18, 8, 0.1)), L(bumpy(14, 90, 14, 14, 8, 0.1)), L(bumpy(86, 90, 14, 14, 8, 0.1)),
              L(bumpy(20, 92, 6, 6, 6, 0.1), 'shade', 'b', False), L(bumpy(80, 92, 6, 6, 6, 0.1), 'shade', 'b', False),
              L(blob([(14, 56), (16, 24), (30, 4), (50, -2), (70, 4), (84, 24), (86, 56), (50, 50)]), 'band', 'f', ln=True),
              L(blob([(60, 4), (84, 24), (86, 54), (70, 52)], 6), 'band_d', 'f', False),
              L(ell(50, 4, 8, 5), 'gem', 'f', ln=True), L(ell(50, 4, 6, 3), 'mid', 'f', False),
              L(bumpy(24, 44, 16, 12, 7, 0.1), 'mid', 'f', ln=True), L(bumpy(76, 44, 16, 12, 7, 0.1), 'mid', 'f', ln=True),
              L(ell(26, 44, 6, 4), 'shade', 'f', False), L(ell(74, 44, 6, 4), 'shade', 'f', False)],
    'side': [L(bumpy(28, 60, 18, 22, 8, 0.1)), L(bumpy(30, 92, 16, 14, 8, 0.1)), L(blob(SIDE_SKULL)),
             L(blob([(14, 56), (14, 24), (32, 2), (60, -2), (82, 10), (92, 34), (90, 54), (50, 52)]), 'band', 'f', ln=True),
             L(ell(50, 0, 7, 5), 'gem', 'f', ln=True), L(bumpy(74, 48, 12, 8, 6, 0.1), 'mid', 'f', ln=True)],
    'back': [L(bumpy(50, 80, 42, 24, 12, 0.1)), L(bumpy(66, 84, 20, 14, 8, 0.1), 'shade', 'b', False),
             L(blob([(14, 62), (16, 24), (30, 4), (50, -2), (70, 4), (84, 24), (86, 62), (50, 66)]), 'band', 'f', ln=True),
             L(blob([(58, 4), (84, 24), (86, 60), (66, 64)], 6), 'band_d', 'f', False), L(ell(50, 4, 8, 5), 'gem', 'f', ln=True)],
}

# ------------------------------------------------------------------ Swarm: pelo verde oscuro en una mata de pinchos que le tapa los
# ojos y le cae a los lados; solo se le ve una sonrisa enorme de dientes
E['yakker-plantsworm'] = {
    'body': 'normal', 'pal': pal('#1e4a2a', '#f6b878'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 90, 'hairline': False},
    'front': [spk((-2, 54), (8, 34), (-22, 30), 7), spk((92, 34), (102, 54), (122, 30), 7, light_left=False),
              spk((10, 28), (30, 10), (0, -10), 7), spk((30, 10), (52, 4), (36, -18), 7), spk((52, 4), (72, 10), (72, -18), 7, light_left=False),
              spk((70, 10), (90, 28), (104, -6), 7, light_left=False),
              L(blob([(2, 72), (0, 40), (14, 12), (50, 2), (86, 12), (100, 40), (98, 72)])),
              L(blob([(62, 8), (98, 38), (96, 70), (84, 66)], 6), 'shade', 'b', False),
              L(blob([(6, 60), (8, 40), (24, 26), (50, 20), (76, 26), (92, 40), (94, 60), (80, 78), (66, 72), (50, 80), (34, 72), (20, 78)]), 'mid', 'f', ln=True),
              L(blob([(60, 26), (92, 42), (92, 60), (78, 74)], 6), 'shade', 'f', False),
              spk((14, 64), (28, 66), (18, 84), 4, z='f'), spk((72, 66), (86, 64), (82, 84), 4, z='f', light_left=False)],
    'side': [spk((18, 32), (30, 12), (-8, 4), 8), spk((30, 12), (52, 4), (36, -18), 7), spk((10, 54), (14, 34), (-20, 40), 8), spk((12, 74), (14, 56), (-14, 80), 6),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             L(blob([(50, 20), (80, 26), (98, 46), (94, 70), (82, 66), (70, 74), (60, 60)]), 'mid', 'f', ln=True)],
    'back': [spk((-2, 54), (8, 34), (-22, 30), 7), spk((92, 34), (102, 54), (122, 30), 7, light_left=False),
             spk((10, 28), (30, 10), (0, -10), 7), spk((30, 10), (52, 4), (36, -18), 7), spk((52, 4), (72, 10), (72, -18), 7, light_left=False),
             spk((70, 10), (90, 28), (104, -6), 7, light_left=False),
             L(blob([(2, 76), (0, 40), (14, 12), (50, 2), (86, 12), (100, 40), (98, 76), (50, 84)])),
             spk((6, 72), (26, 82), (4, 96), 6), spk((26, 84), (50, 88), (36, 102), 6), spk((50, 88), (74, 84), (66, 102), 6, light_left=False),
             spk((74, 82), (94, 72), (96, 96), 6, light_left=False),
             L(blob([(58, 8), (98, 38), (96, 74), (66, 82)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Metron: pelo morado de pinchos que le caen por los lados de la
# cara y una cinta oscura ancha en la frente; ojos castaños
E['ronny-metcalf'] = {
    'body': 'normal', 'pal': pal('#4a3a9a', '#f6c08e', iris='#8a4a1a', band='#2a2e3a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    'front': [L(blob([(8, 84), (4, 44), (16, 12), (50, 2), (84, 12), (96, 44), (92, 84), (80, 76), (80, 60), (20, 60), (20, 76)])),
              spk((4, 66), (12, 80), (-6, 92), 4), spk((88, 80), (96, 66), (106, 92), 4, light_left=False),
              L(blob([(62, 10), (94, 44), (90, 82), (82, 80)], 6), 'shade', 'b', False), sheen(22, 48, 14, 3),
              spk((10, 46), (22, 46), (16, 86), 4, z='f'), spk((78, 46), (90, 46), (84, 86), 4, z='f', light_left=False),
              L(blob([(16, 62), (16, 46), (50, 40), (84, 46), (84, 62), (50, 58)]), 'band', 'f', ln=True),
              spk((24, 36), (44, 30), (34, 50), 4, z='f'), spk((56, 30), (76, 36), (66, 50), 4, z='f', light_left=False)],
    'side': [L(blob([(48, 92), (16, 88), (4, 60), (8, 28), (28, 6), (58, 2), (84, 12), (96, 34), (94, 56), (76, 54), (62, 56), (56, 72), (52, 88)])),
             spk((6, 76), (16, 88), (-6, 96), 4), L(blob([(6, 50), (8, 86), (40, 90), (24, 64)], 6), 'shade', 'b', False),
             L(quad((14, 48), (50, 40), (94, 46)) + quad((94, 60), (50, 56), (14, 62)), 'band', 'f', ln=True),
             spk((52, 56), (64, 56), (60, 90), 3, z='f')],
    'back': [L(blob([(8, 86), (4, 44), (16, 12), (50, 2), (84, 12), (96, 44), (92, 86), (50, 92)])),
             spk((12, 82), (30, 88), (14, 100), 4), spk((30, 88), (50, 92), (40, 104), 4), spk((50, 92), (70, 88), (60, 104), 4, light_left=False),
             spk((70, 88), (88, 82), (86, 100), 4, light_left=False),
             L(blob([(58, 10), (94, 44), (90, 84), (66, 90)], 6), 'shade', 'b', False),
             L(quad((6, 50), (50, 42), (94, 50)) + quad((94, 64), (50, 56), (6, 64)), 'band', 'f', ln=True)],
}

# ------------------------------------------------------------------ Macure: pelo verde azulado corto con flequillo y dos moños
# metálicos enormes y redondos a los lados (con luces amarillas), de los que bajan dos cables junto a la cara
def bun(cx, cy, view='front'):
    return [L(ell(cx, cy, 15, 13), 'metal', 'f', ln=True), L(ell(cx, cy, 9, 8), 'mid', 'f', ln=True), L(ell(cx + (8 if cx > 50 else -8), cy - 4, 2.4, 2.4), 'light2', 'f', False)]


E['carrie-mccuring'] = {
    'body': 'chica', 'pal': pal('#2a9a9a', '#fce4c8', iris='#2a7a7a', metal='#c8ccd4', light2='#f0d020'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': (62, 52)},
    'front': [L(blob([(12, 70), (10, 40), (22, 14), (50, 6), (78, 14), (90, 40), (88, 70)])),
              L(blob([(62, 12), (88, 36), (86, 66), (74, 62)], 6), 'shade', 'b', False), sheen(24, 48, 14, 3),
              spk((14, 46), (32, 38), (20, 66), 5, z='f'), spk((32, 38), (50, 34), (42, 62), 5, z='f'),
              spk((50, 34), (68, 38), (58, 62), 5, z='f', light_left=False), spk((68, 40), (86, 46), (80, 66), 5, z='f', light_left=False),
              L(quad((14, 30), (8, 60), (18, 100)), (220, 220, 228, 255), 'f', False, False, 1.6), L(quad((86, 30), (92, 60), (82, 100)), (220, 220, 228, 255), 'f', False, False, 1.6)]
             + bun(6, 18) + bun(94, 18),
    'side': [L(blob([(46, 92), (20, 88), (8, 60), (10, 28), (28, 8), (58, 4), (82, 14), (94, 34), (92, 56), (76, 54), (62, 56), (56, 72), (52, 88)])),
             L(blob([(12, 50), (14, 84), (40, 88), (26, 64)], 6), 'shade', 'b', False),
             spk((56, 30), (88, 40), (92, 66), 5, z='f', light_left=False), L(quad((40, 30), (36, 60), (44, 100)), (220, 220, 228, 255), 'f', False, False, 1.6)]
            + bun(34, 14),
    'back': [L(blob([(12, 76), (10, 40), (22, 14), (50, 6), (78, 14), (90, 40), (88, 76), (50, 86)])),
             L(blob([(58, 12), (88, 36), (86, 74), (66, 84)], 6), 'shade', 'b', False)] + bun(6, 18) + bun(94, 18),
}

# Épsilon Plus (Épsilon Kai): misma gente, pero en su forma de Épsilon Kai (los sprites "(EK)" de la wiki) todos llevan los
# ojos rojos encendidos y el gesto más fiero (Zel y Metron enseñan los dientes, Desarm frunce el ceño)
import copy  # noqa: E402

RED_EYES = (232, 30, 34, 255)
EK_FACE = {'zeke-valanche': {'mouth': 'grin', 'brows': 'angry'}, 'ronny-metcalf': {'mouth': 'grin', 'brows': 'angry'},
           'dave-quagmire': {'brows': 'angry'}, 'carrie-mccuring': {'eyes': 'sharp'}, 'mads-hatter': {'mouth': 'grin'},
           'karen-ripton': {'eyes': 'sharp'}}
EK = {}
for _pid, _spec in E.items():
    _k = copy.deepcopy(_spec)
    _k['pal']['iris'] = RED_EYES
    if _k['face'].get('eyes') in ('big', 'normal'):
        _k['face']['eyes'] = 'sharp'
    _k['face'].update(EK_FACE.get(_pid.replace('-desarm-cc', ''), {}))
    EK[_pid] = _k

for _pid, _spec in E.items():
    CHARS[f'ie2-epsilon:{_pid}'] = _spec
for _pid, _spec in EK.items():
    CHARS[f'ie2-epsilon-kai:{_pid}'] = _spec
