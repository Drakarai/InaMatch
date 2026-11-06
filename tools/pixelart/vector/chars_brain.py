"""Mikage Sennou / Instituto Brain (IE1): todos llevan electrodos en las sienes con cables negros que bajan hasta la
nuca; cada peinado con su modelo 3D como referencia."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, pal, sheen, spk, strand
from chars_otaku import back_hair
from chars_sengoku import wavy
from heads import quad

WHITE = (255, 255, 255, 255)
WIRE = (24, 22, 26, 255)
PAD = (236, 226, 206, 255)
SIDE_SKULL = [(44, 92), (22, 88), (12, 64), (14, 36), (30, 16), (56, 10), (78, 18), (88, 36), (76, 44), (60, 48), (52, 62), (50, 80)]
SKULL_F = [(16, 64), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 64)]
SKULL_B = [(16, 70), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 70), (66, 86), (34, 86)]


def wires(view, y=64, out=22, pads=True, r=3.2, x=16):
    """Electrodos en las sienes y sus cables, que dan un rodeo hacia fuera y bajan por detrás hasta el cuello."""
    out_l = []
    if view == 'side':
        out_l.append(L(quad((54, y), (10, y + 4), (30, 106)), WIRE, 'f', False, False, 2.0))
        if pads:
            out_l.append(L(ell(56, y, r * 0.8, r), PAD, 'f', ln=True))
        return out_l
    for sx, s in ((x, 1), (100 - x, -1)):
        out_l.append(L(quad((sx, y), (sx - s * out, y + 22), (50 - s * 26, 106)), WIRE, 'f', False, False, 2.0))
        if pads and view == 'front':
            out_l.append(L(ell(sx, y, r, r), PAD, 'f', ln=True))
    return out_l


# ------------------------------------------------------------------ Thomas Feldt (portero): delgado, calvo y pálido, con conos
# morados clavados en la cabeza (uno alto en lo alto y otros alrededor); cara alargada y mirada furiosa
CONE = '#5a4a7a'


def cone(base, tip, w=5):
    return [L([(base[0] - w, base[1]), tip, (base[0] + w, base[1] + 1)], 'cone', 'f', ln=True),
            L([base, tip, (base[0] + w, base[1] + 1)], 'cone_d', 'f', False)]


CHARS['thomas-feldt'] = {
    'body': 'delgado', 'pal': pal('#5a4a7a', '#f6dcc0', cone=CONE, cone_d='#3e3258'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'nose': (50, 84, 3), 'nose_side': (91, 82, 3), 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin'), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'skin_d', 'b', False)]
             + cone((50, 10), (50, -16), 6) + cone((24, 22), (12, 6), 5) + cone((76, 22), (90, 6), 5) + cone((38, 30), (36, 18), 4) + cone((62, 30), (64, 18), 4)
             + wires('front', 66),
    'side': [L(blob(SIDE_SKULL), 'skin')]
            + cone((50, 10), (52, -16), 6) + cone((28, 18), (14, 2), 5) + cone((70, 18), (86, 4), 5) + cone((18, 40), (0, 32), 5) + cone((30, 62), (12, 62), 5)
            + cone((44, 34), (40, 20), 4) + wires('side', 64),
    'back': [L(blob(SKULL_B), 'skin'), L(blob([(58, 12), (86, 36), (84, 68), (66, 84)], 6), 'skin_d', 'b', False)]
            + cone((50, 10), (50, -16), 6) + cone((24, 22), (12, 6), 5) + cone((76, 22), (90, 6), 5) + cone((32, 46), (24, 34), 5)
            + cone((68, 46), (76, 34), 5) + cone((50, 56), (50, 44), 5) + wires('back', 66),
}

# ------------------------------------------------------------------ Harry Leading: pelo castaño muy abierto hacia los lados
# (como alas) con un mechón que se riza sobre la frente; dos cables le salen por encima de la cabeza como antenas
CHARS['harry-leading'] = {
    'body': 'normal', 'pal': pal('#6a5040', '#fcd2a0'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (58, 48)},
    'front': [L(quad((24, 12), (24, -12), (42, -8)), WIRE, 'b', False, False, 2.0), L(quad((76, 12), (76, -12), (58, -8)), WIRE, 'b', False, False, 2.0),
              L(blob([(2, 50), (-6, 30), (10, 26), (24, 12), (50, 6), (76, 12), (90, 26), (106, 30), (98, 50), (84, 64), (16, 64)])),
              L(blob([(62, 12), (100, 32), (90, 54), (80, 52)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
              L(blob([(46, 10), (60, 18), (58, 36), (50, 52), (46, 40), (52, 26)]), 'mid', 'f', ln=True),
              L(blob([(54, 18), (60, 22), (54, 46), (52, 30)], 4), 'shade', 'f', False)],
    'side': [L(quad((40, 12), (30, -12), (60, -10)), WIRE, 'b', False, False, 2.0),
             L(blob([(46, 92), (20, 88), (8, 62), (8, 32), (24, 12), (54, 6), (80, 14), (94, 30), (90, 48), (74, 44), (60, 48), (52, 64), (50, 82)])),
             L(blob([(12, 46), (16, 78), (38, 88), (26, 60)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             spk((60, 26), (92, 34), (98, 54), 5, z='f', light_left=False)],
    'back': [L(quad((24, 12), (24, -12), (42, -8)), WIRE, 'b', False, False, 2.0), L(quad((76, 12), (76, -12), (58, -8)), WIRE, 'b', False, False, 2.0),
             L(blob([(2, 44), (-8, 26), (10, 24), (24, 10), (50, 6), (76, 10), (90, 24), (108, 26), (98, 44), (84, 70), (64, 88), (36, 88), (16, 70)])),
             L(blob([(58, 12), (100, 28), (84, 68), (64, 86)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3)],
}

# ------------------------------------------------------------------ Terry Stronger: pelo castaño rojizo oscuro de pinchos, una
# venda blanca atada en diagonal sobre la frente y una tirita en la mejilla
CHARS['terry-stronger'] = {
    'body': 'normal', 'pal': pal('#5a1a10', '#f6c08e', wrap='#f2ece4', wrap_d='#c8b8b0', aid='#e08a4a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (58, 48)},
    'front': [spk((8, 60), (12, 44), (-12, 58), 5), spk((10, 44), (20, 26), (-12, 26), 7), spk((22, 22), (40, 12), (24, -14), 7),
              spk((40, 12), (58, 10), (56, -18), 7, light_left=False), spk((58, 12), (76, 18), (88, -6), 7, light_left=False),
              spk((78, 24), (90, 42), (112, 30), 6, light_left=False), spk((88, 46), (92, 62), (106, 66), 4, light_left=False),
              L(blob([(10, 72), (8, 40), (20, 16), (50, 8), (80, 16), (92, 40), (90, 72), (80, 66), (20, 66)])),
              L(blob([(62, 14), (90, 38), (88, 68), (78, 64)], 6), 'shade', 'b', False),
              spk((12, 50), (28, 46), (16, 76), 4, z='f'), spk((72, 46), (88, 50), (86, 76), 4, z='f', light_left=False),
              L(quad((8, 50), (50, 28), (92, 34)) + quad((92, 46), (50, 40), (8, 62)), 'wrap', 'f', ln=True),
              L(quad((8, 58), (50, 38), (92, 44)) + quad((92, 46), (50, 40), (8, 62)), 'wrap_d', 'f', False),
              spk((30, 52), (44, 50), (36, 70), 3, z='f'), spk((52, 48), (66, 48), (60, 68), 3, z='f', light_left=False),
              L([(64, 82), (72, 78), (76, 84), (68, 88)], 'aid', 'f', ln=True)],
    'side': [spk((16, 40), (24, 24), (-16, 22), 7), spk((24, 26), (40, 14), (6, -12), 7), spk((40, 14), (60, 8), (54, -18), 7),
             spk((14, 56), (16, 40), (-14, 54), 6), spk((18, 72), (22, 58), (-8, 80), 5),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((60, 14), (80, 22), (98, 4), 6, light_left=False),
             L(quad((10, 50), (50, 36), (92, 40)) + quad((92, 52), (50, 48), (10, 62)), 'wrap', 'f', ln=True),
             spk((60, 52), (84, 52), (88, 72), 4, z='f', light_left=False),
             L([(80, 80), (88, 78), (88, 86), (80, 86)], 'aid', 'f', ln=True)],
    'back': [spk((8, 60), (12, 44), (-12, 58), 5), spk((10, 44), (20, 26), (-12, 26), 7), spk((22, 22), (40, 12), (24, -14), 7),
             spk((40, 12), (58, 10), (56, -18), 7, light_left=False), spk((58, 12), (76, 18), (88, -6), 7, light_left=False),
             spk((78, 24), (90, 42), (112, 30), 6, light_left=False), spk((88, 46), (92, 62), (106, 66), 4, light_left=False),
             L(blob([(10, 72), (8, 40), (20, 16), (50, 8), (80, 16), (92, 40), (90, 72), (66, 86), (34, 86)])),
             spk((14, 72), (32, 82), (10, 94), 4), spk((32, 82), (50, 86), (40, 100), 4), spk((50, 86), (68, 82), (62, 100), 4, light_left=False),
             spk((68, 82), (86, 72), (90, 94), 4, light_left=False),
             L(blob([(58, 14), (90, 38), (88, 70), (66, 84)], 6), 'shade', 'b', False),
             L(quad((8, 36), (50, 42), (92, 54)) + quad((92, 64), (50, 54), (8, 48)), 'wrap', 'f', ln=True)],
}

# ------------------------------------------------------------------ Philip Marvel: corpulento, piel morena, pelo verde azulado de
# pinchos hacia arriba, electrodos grandes en las sienes, ojos redondos de enfado y dientes apretados
CHARS['philip-marvel'] = {
    'body': 'corpulento', 'pal': pal('#4a8a7a', '#a8683a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 92, 'hairline': (56, 48)},
    'front': [spk((10, 50), (18, 32), (-10, 30), 7), spk((20, 28), (38, 14), (20, -14), 8), spk((38, 14), (56, 10), (46, -22), 8),
              spk((54, 10), (72, 16), (78, -16), 8, light_left=False), spk((70, 18), (86, 32), (110, 22), 7, light_left=False),
              L(blob([(14, 64), (12, 38), (24, 18), (50, 10), (76, 18), (88, 38), (86, 64)])),
              L(blob([(62, 14), (88, 36), (86, 62), (74, 58)], 6), 'shade', 'b', False),
              spk((20, 44), (40, 40), (28, 62), 4, z='f'), spk((60, 40), (80, 44), (74, 62), 4, z='f', light_left=False)]
             + wires('front', 64, r=4.6),
    'side': [spk((18, 38), (28, 22), (-12, 14), 8), spk((30, 20), (48, 10), (24, -16), 8), spk((48, 10), (66, 10), (66, -18), 7, light_left=False),
             spk((14, 56), (16, 40), (-12, 48), 6),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((62, 16), (82, 26), (100, 8), 6, light_left=False)] + wires('side', 62, r=4.6),
    'back': [spk((10, 50), (18, 32), (-10, 30), 7), spk((20, 28), (38, 14), (20, -14), 8), spk((38, 14), (56, 10), (46, -22), 8),
             spk((54, 10), (72, 16), (78, -16), 8, light_left=False), spk((70, 18), (86, 32), (110, 22), 7, light_left=False),
             L(blob([(14, 72), (12, 38), (24, 18), (50, 10), (76, 18), (88, 38), (86, 72), (66, 86), (34, 86)])),
             spk((16, 70), (34, 82), (12, 92), 4), spk((66, 82), (84, 70), (88, 92), 4, light_left=False)] + back_hair() + wires('back', 64),
}

# ------------------------------------------------------------------ Noel Good: corpulento, pelo castaño muy oscuro en casco con
# un pico sobre la frente, rayas negras junto a los ojos, nariz roja y electrodos en las sienes
CHARS['noel-good'] = {
    'body': 'corpulento', 'pal': pal('#3a2a20', '#fbc49a', nose='#e0603a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'nose': (50, 84, 2.8), 'nose_side': (91, 82, 2.6),
             'hairline': [(10, 62), (20, 52), (36, 50), (50, 60), (64, 50), (80, 52), (90, 62)]},
    'front': [L(blob([(14, 64), (12, 36), (24, 14), (50, 8), (76, 14), (88, 36), (86, 64)])),
              L(blob([(62, 14), (88, 36), (86, 62), (74, 58)], 6), 'shade', 'b', False), sheen(26, 50, 18, 3),
              L([(16, 70), (28, 78)], OUTC, 'f', False, False, 3.0), L([(84, 70), (72, 78)], OUTC, 'f', False, False, 3.0)] + wires('front', 64),
    'side': [L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False), sheen(32, 62, 16, 3),
             L([(70, 76), (76, 78)], OUTC, 'f', False, False, 2.2)] + wires('side', 60),
    'back': [L(blob(SKULL_B))] + back_hair() + wires('back', 64),
}

# ------------------------------------------------------------------ Tyron Rock: media melena verde oliva con raya al lado que le
# tapa las orejas, dos puntos en la frente, ojos rasgados y cables en grandes bucles a los lados
CHARS['tyron-rock'] = {
    'body': 'normal', 'pal': pal('#6a6a30', '#fcd6ae'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'ears': False, 'hairline': (60, 48)},
    'front': [L(blob([(10, 92), (6, 50), (16, 18), (50, 6), (84, 18), (94, 50), (90, 92), (80, 90), (80, 62), (20, 62), (20, 90)])),
              L(blob([(62, 14), (92, 46), (90, 88), (82, 86)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
              strand([(62, 8), (50, 50)], 'deep', 'b', 1.0),
              L(blob([(64, 12), (86, 30), (86, 62), (72, 54), (58, 44)]), 'mid', 'f'), strand([(58, 44), (72, 54), (86, 62)], OUTC, 'f', 1.0),
              L(ell(44, 60, 1.8, 1.8), OUTC, 'f', False), L(ell(56, 60, 1.8, 1.8), OUTC, 'f', False)]
             + [L(quad((14, 70), (-24, 76), (20, 104)), WIRE, 'f', False, False, 2.0), L(quad((86, 70), (124, 76), (80, 104)), WIRE, 'f', False, False, 2.0)],
    'side': [L(blob([(46, 94), (14, 92), (2, 62), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (92, 58), (76, 56), (62, 58), (58, 74), (56, 92)])),
             L(blob([(6, 50), (8, 88), (40, 92), (24, 64)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             spk((56, 30), (88, 40), (92, 70), 6, z='f', light_left=False),
             L(quad((60, 46), (20, 60), (24, 104)), WIRE, 'f', False, False, 2.0)],
    'back': [L(blob([(10, 92), (6, 50), (16, 18), (50, 6), (84, 18), (94, 50), (90, 92), (50, 98)])),
             L(blob([(58, 14), (92, 46), (90, 90), (66, 96)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
             strand([(50, 8), (48, 92)], 'deep', 'b', 1.0)]
            + [L(quad((14, 70), (-24, 76), (36, 100)), WIRE, 'f', False, False, 2.0), L(quad((86, 70), (124, 76), (64, 100)), WIRE, 'f', False, False, 2.0)],
}

# ------------------------------------------------------------------ Francis Tell: melena morada lisa con mechones largos y en
# punta que le caen sobre la cara hasta la barbilla; ojos azul verdoso afilados
CHARS['francis-tell'] = {
    'body': 'normal', 'pal': pal('#4a3a5e', '#fbe0c4', iris='#3a8a8a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 93, 'hairline': (60, 50)},
    'front': [L(blob([(10, 86), (6, 48), (16, 16), (50, 4), (84, 16), (94, 48), (90, 86), (80, 82), (80, 60), (20, 60), (20, 82)])),
              L(blob([(62, 12), (92, 46), (90, 84), (82, 82)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
              spk((10, 44), (26, 40), (20, 102), 4, z='f'), spk((74, 40), (90, 44), (80, 102), 4, z='f', light_left=False),
              spk((24, 38), (44, 34), (40, 74), 5, z='f'), spk((44, 34), (60, 36), (54, 80), 4, z='f', light_left=False),
              spk((58, 36), (76, 40), (68, 70), 4, z='f', light_left=False)]
             + wires('front', 68, pads=False, out=30),
    'side': [L(blob([(46, 94), (14, 92), (2, 62), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (92, 58), (76, 56), (62, 58), (56, 74), (52, 90)])),
             L(blob([(6, 50), (8, 88), (40, 92), (24, 64)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             spk((56, 30), (90, 40), (92, 86), 6, z='f', light_left=False), spk((50, 54), (62, 54), (56, 100), 3, z='f')] + wires('side', 64, pads=False),
    'back': [L(blob([(10, 88), (6, 48), (16, 16), (50, 4), (84, 16), (94, 48), (90, 88), (50, 96)])),
             spk((16, 84), (34, 90), (24, 104), 4), spk((34, 90), (50, 94), (44, 108), 4), spk((50, 94), (66, 90), (56, 108), 4, light_left=False),
             spk((66, 90), (84, 84), (76, 104), 4, light_left=False),
             L(blob([(58, 12), (92, 46), (90, 86), (66, 92)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3)] + wires('back', 66, pads=False, out=30),
}

# ------------------------------------------------------------------ Samuel Buster: piel morena, pelo gris malva de pinchos altos,
# electrodos en las sienes y mirada furiosa
CHARS['samuel-buster'] = {
    'body': 'normal', 'pal': pal('#6a5a6e', '#c08a40'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (58, 50)},
    'front': [spk((8, 62), (14, 42), (-10, 52), 5), spk((14, 40), (28, 20), (2, 4), 7), spk((28, 20), (46, 10), (30, -20), 8),
              spk((44, 10), (62, 12), (60, -18), 7, light_left=False), spk((62, 16), (80, 26), (96, 2), 7, light_left=False),
              spk((82, 32), (90, 50), (108, 40), 5, light_left=False),
              L(blob([(10, 70), (8, 40), (20, 16), (50, 8), (80, 16), (92, 40), (90, 70), (80, 64), (20, 64)])),
              L(blob([(62, 14), (90, 38), (88, 66), (78, 62)], 6), 'shade', 'b', False),
              spk((14, 46), (34, 40), (20, 72), 5, z='f'), spk((66, 40), (86, 46), (84, 72), 5, z='f', light_left=False)] + wires('front', 66),
    'side': [spk((16, 40), (24, 22), (-16, 16), 8), spk((24, 24), (42, 12), (14, -20), 8), spk((42, 12), (62, 8), (54, -22), 7),
             spk((14, 58), (16, 40), (-16, 50), 6), spk((18, 76), (22, 60), (-6, 84), 5),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((60, 14), (80, 22), (96, 0), 6, light_left=False), spk((56, 30), (86, 40), (90, 66), 5, z='f', light_left=False)] + wires('side', 64),
    'back': [spk((8, 62), (14, 42), (-10, 52), 5), spk((14, 40), (28, 20), (2, 4), 7), spk((28, 20), (46, 10), (30, -20), 8),
             spk((44, 10), (62, 12), (60, -18), 7, light_left=False), spk((62, 16), (80, 26), (96, 2), 7, light_left=False),
             spk((82, 32), (90, 50), (108, 40), 5, light_left=False),
             L(blob([(10, 72), (8, 40), (20, 16), (50, 8), (80, 16), (92, 40), (90, 72), (66, 86), (34, 86)])),
             spk((14, 72), (32, 84), (10, 96), 4), spk((32, 84), (50, 88), (40, 104), 4), spk((50, 88), (68, 84), (62, 104), 4, light_left=False),
             spk((68, 84), (86, 72), (90, 96), 4, light_left=False),
             L(blob([(58, 14), (90, 38), (88, 70), (66, 84)], 6), 'shade', 'b', False)] + wires('back', 66),
}

# ------------------------------------------------------------------ Victor Kind: pelo castaño de pinchos despeinados, gafas de
# cristal blanco opaco con montura roja y cables a los lados
CHARS['victor-kind'] = {
    'body': 'normal', 'pal': pal('#7a4a30', '#f6c08e', lens='#f4f4f4', frame='#b04a3a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 92, 'hairline': (60, 50)},
    'front': [spk((8, 60), (12, 42), (-12, 50), 6), spk((12, 42), (24, 22), (-6, 14), 7), spk((24, 22), (42, 12), (20, -16), 7),
              spk((42, 12), (60, 10), (60, -18), 7, light_left=False), spk((60, 12), (78, 20), (94, -6), 7, light_left=False),
              spk((80, 28), (90, 46), (110, 36), 6, light_left=False),
              L(blob([(10, 74), (8, 40), (20, 16), (50, 8), (80, 16), (92, 40), (90, 74), (80, 66), (20, 66)])),
              L(blob([(62, 14), (90, 38), (88, 70), (78, 66)], 6), 'shade', 'b', False),
              spk((12, 46), (30, 40), (18, 76), 5, z='f'), spk((28, 40), (46, 36), (36, 66), 4, z='f'),
              spk((54, 36), (72, 40), (64, 66), 4, z='f', light_left=False), spk((70, 40), (88, 46), (84, 76), 5, z='f', light_left=False)]
             + [L([(24, 70), (46, 70), (45, 80), (26, 80)], 'lens', 'f', ln=True), L([(54, 70), (76, 70), (74, 80), (55, 80)], 'lens', 'f', ln=True),
                L([(24, 70), (46, 70)], 'frame', 'f', False, False, 1.8), L([(54, 70), (76, 70)], 'frame', 'f', False, False, 1.8),
                L([(46, 72), (54, 72)], 'frame', 'f', False, False, 1.6)]
             + [L(quad((14, 72), (-20, 80), (20, 104)), WIRE, 'f', False, False, 2.0), L(quad((86, 72), (120, 80), (80, 104)), WIRE, 'f', False, False, 2.0)],
    'side': [spk((16, 40), (24, 24), (-18, 20), 7), spk((24, 26), (40, 14), (6, -14), 7), spk((40, 14), (60, 8), (54, -20), 7),
             spk((14, 56), (16, 40), (-16, 50), 6), spk((18, 72), (22, 58), (-8, 80), 5),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((60, 14), (80, 22), (98, 2), 6, light_left=False), spk((56, 30), (88, 40), (92, 70), 6, z='f', light_left=False),
             L([(78, 70), (92, 70), (91, 80), (80, 80)], 'lens', 'f', ln=True), L([(78, 70), (54, 68)], 'frame', 'f', False, False, 1.6),
             L(quad((52, 70), (10, 80), (30, 106)), WIRE, 'f', False, False, 2.0)],
    'back': [spk((8, 60), (12, 42), (-12, 50), 6), spk((12, 42), (24, 22), (-6, 14), 7), spk((24, 22), (42, 12), (20, -16), 7),
             spk((42, 12), (60, 10), (60, -18), 7, light_left=False), spk((60, 12), (78, 20), (94, -6), 7, light_left=False),
             spk((80, 28), (90, 46), (110, 36), 6, light_left=False),
             L(blob([(10, 74), (8, 40), (20, 16), (50, 8), (80, 16), (92, 40), (90, 74), (66, 86), (34, 86)])),
             spk((14, 74), (32, 84), (10, 96), 4), spk((32, 84), (50, 88), (40, 104), 4), spk((50, 88), (68, 84), (62, 104), 4, light_left=False),
             spk((68, 84), (86, 74), (90, 96), 4, light_left=False),
             L(blob([(58, 14), (90, 38), (88, 72), (66, 84)], 6), 'shade', 'b', False)]
            + [L(quad((14, 72), (-20, 80), (36, 100)), WIRE, 'f', False, False, 2.0), L(quad((86, 72), (120, 80), (64, 100)), WIRE, 'f', False, False, 2.0)],
}

# ------------------------------------------------------------------ Jonathan Seller: pelo blanco rosado ondulado, peinado hacia
# atrás con volumen y recogido en una coleta ondulada; ojos afilados
CHARS['jonathan-seller'] = {
    'body': 'normal', 'pal': pal('#d8b4b4', '#fbd0a4'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (54, 42)},
    'front': [L(blob([(12, 66), (10, 36), (22, 12), (50, 4), (78, 10), (96, 26), (102, 50), (94, 66), (86, 58), (14, 58)])),
              L(bumpy(90, 44, 14, 16, 6, 0.1)), L(bumpy(92, 60, 10, 10, 6, 0.1)),
              L(blob([(60, 8), (100, 34), (98, 64), (84, 56)], 6), 'shade', 'b', False), sheen(22, 46, 16, 3),
              strand([(30, 30), (54, 12), (80, 20)], 'shade', 'b', 1.1), strand([(34, 40), (60, 22), (88, 34)], 'shade', 'b', 1.1),
              spk((12, 50), (22, 46), (16, 66), 3, z='f')]
             + [L(quad((14, 64), (-14, 74), (20, 104)), WIRE, 'f', False, False, 2.0)],
    'side': wavy((14, 56), (26, 62), (-12, 94), 8) + wavy((14, 66), (24, 66), (2, 100), -6)
            + [L(blob([(46, 90), (20, 86), (8, 60), (10, 28), (28, 8), (60, 2), (86, 12), (100, 30), (96, 44), (78, 40), (62, 44), (54, 62), (50, 80)])),
               L(blob([(12, 44), (16, 76), (38, 86), (26, 60)], 6), 'shade', 'b', False), sheen(32, 66, 12, 3),
               strand([(94, 22), (60, 12), (26, 40)], 'shade', 'b', 1.1), strand([(96, 36), (62, 26), (30, 56)], 'shade', 'b', 1.1),
               L(ell(20, 60, 4, 4), 'deep', 'b', ln=True)] + wires('side', 66, pads=False),
    'back': [L(blob([(12, 70), (10, 36), (22, 12), (50, 4), (78, 12), (90, 36), (88, 70), (66, 84), (34, 84)])),
             L(blob([(58, 12), (88, 36), (86, 68), (66, 82)], 6), 'shade', 'b', False), sheen(22, 46, 16, 3),
             strand([(50, 6), (50, 70)], 'shade', 'b', 1.1)]
            + wavy((42, 70), (58, 70), (44, 112), 8, z='f') + [L(ell(50, 72, 6, 4), 'deep', 'f', ln=True)]
            + [L(quad((14, 66), (-14, 74), (36, 100)), WIRE, 'f', False, False, 2.0)],
}

# ------------------------------------------------------------------ Neil Turner: melena corta rojo salmón con flequillo recto y
# las puntas abiertas hacia fuera a la altura de la barbilla; un cable le rodea la cabeza como un aro
CHARS['neil-turner'] = {
    'body': 'normal', 'pal': pal('#c86a5a', '#fcdcc0', iris='#6a8a7a'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': (60, 54)},
    'front': [L(blob([(8, 92), (4, 50), (14, 16), (50, 6), (86, 16), (96, 50), (92, 92), (80, 88), (80, 64), (20, 64), (20, 88)])),
              spk((4, 80), (14, 94), (-10, 98), 4), spk((86, 94), (96, 80), (110, 98), 4, light_left=False),
              L(blob([(62, 14), (94, 46), (92, 90), (84, 88)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
              strand([(30, 22), (28, 58)], 'shade', 'b', 1.0), strand([(50, 18), (50, 58)], 'shade', 'b', 1.0), strand([(70, 22), (72, 58)], 'shade', 'b', 1.0),
              L(quad((10, 62), (-10, 66), (6, 74)) + quad((6, 74), (50, 80), (94, 74))[1:] + quad((94, 74), (110, 66), (90, 62))[1:], WIRE, 'f', False, False, 2.0)],
    'side': [L(blob([(46, 94), (14, 94), (2, 62), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (92, 58), (76, 56), (62, 58), (58, 74), (56, 92)])),
             spk((0, 82), (16, 96), (-14, 100), 4),
             L(blob([(6, 50), (8, 88), (40, 92), (24, 64)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             spk((56, 30), (90, 40), (92, 72), 6, z='f', light_left=False),
             L([(-6, 66), (40, 70), (96, 60)], WIRE, 'f', False, False, 2.0)],
    'back': [L(blob([(8, 92), (4, 50), (14, 16), (50, 6), (86, 16), (96, 50), (92, 92), (50, 98)])),
             spk((4, 80), (14, 94), (-10, 98), 4), spk((86, 94), (96, 80), (110, 98), 4, light_left=False),
             spk((14, 90), (32, 96), (18, 106), 4), spk((68, 96), (86, 90), (82, 106), 4, light_left=False),
             L(blob([(58, 14), (94, 46), (92, 90), (66, 96)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
             L(quad((10, 62), (-10, 66), (6, 74)) + quad((6, 74), (50, 80), (94, 74))[1:] + quad((94, 74), (110, 66), (90, 62))[1:], WIRE, 'f', False, False, 2.0)],
}

# ------------------------------------------------------------------ Reg Underwood (portero suplente): pelo malva de pinchos
# barridos hacia arriba y a un lado, una visera verde azulada con electrodos que le rodea la frente
VISOR = '#4a6a64'
CHARS['reg-underwood'] = {
    'body': 'normal', 'pal': pal('#8a6a74', '#d8a068', visor=VISOR, visor_d='#34504a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (54, 46)},
    'front': [spk((40, 14), (60, 12), (70, -16), 8, light_left=False), spk((58, 14), (78, 22), (104, 4), 8, light_left=False),
              spk((76, 26), (88, 40), (112, 30), 6, light_left=False), spk((20, 22), (40, 14), (30, -8), 7),
              L(blob([(12, 64), (10, 38), (22, 16), (50, 8), (78, 16), (90, 38), (88, 64)])),
              L(blob([(62, 14), (88, 36), (86, 62), (74, 58)], 6), 'shade', 'b', False),
              spk((14, 60), (24, 60), (16, 80), 3, z='f'), spk((76, 60), (86, 60), (84, 80), 3, z='f', light_left=False),
              L(quad((10, 44), (50, 32), (90, 44)) + quad((90, 62), (50, 52), (10, 62)), 'visor', 'f', ln=True),
              L(quad((10, 56), (50, 46), (90, 56)) + quad((90, 62), (50, 52), (10, 62)), 'visor_d', 'f', False),
              L(ell(16, 52, 3, 3), PAD, 'f', ln=True), L(ell(84, 52, 3, 3), PAD, 'f', ln=True)]
             + [L(quad((14, 96), (50, 104), (86, 96)), WIRE, 'f', False, False, 2.0), L(quad((16, 54), (6, 80), (16, 96)), WIRE, 'f', False, False, 2.0),
                L(quad((84, 54), (94, 80), (84, 96)), WIRE, 'f', False, False, 2.0)],
    'side': [spk((20, 30), (40, 14), (0, -6), 7), spk((40, 14), (60, 8), (52, -16), 7),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((60, 14), (80, 22), (100, 0), 7, light_left=False),
             L(quad((10, 44), (50, 34), (94, 42)) + quad((94, 60), (50, 54), (10, 60)), 'visor', 'f', ln=True),
             L(ell(54, 50, 3, 3.4), PAD, 'f', ln=True), L(ell(70, 50, 3, 3.4), PAD, 'f', ln=True),
             L(quad((54, 52), (40, 90), (16, 96)), WIRE, 'f', False, False, 2.0)],
    'back': [spk((40, 12), (60, 14), (30, -16), 8), spk((22, 22), (42, 14), (-4, 4), 8), spk((12, 40), (24, 26), (-12, 30), 6),
             spk((60, 14), (80, 22), (70, -8), 7, light_left=False),
             L(blob([(12, 70), (10, 38), (22, 16), (50, 8), (78, 16), (90, 38), (88, 70), (66, 84), (34, 84)])),
             L(blob([(58, 14), (88, 36), (86, 68), (66, 82)], 6), 'shade', 'b', False),
             L(quad((10, 52), (50, 46), (90, 52)) + quad((90, 68), (50, 62), (10, 68)), 'visor', 'f', ln=True),
             L(quad((16, 90), (50, 98), (84, 90)), WIRE, 'f', False, False, 2.0)],
}

# ------------------------------------------------------------------ Patrick Stiller: media melena verde oliva con un mechón
# verde azulado por el centro y un electrodo como un monóculo sobre un ojo, con su cable
CHARS['patrick-stiller'] = {
    'body': 'normal', 'pal': pal('#5a5a2a', '#f6bc80', iris='#3a8a8a', streak='#3a8a8a', mono='#8a8a90'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'frown', 'mouth_y': 93, 'hairline': (60, 50)},
    'front': [L(blob([(10, 86), (6, 48), (16, 16), (50, 4), (84, 16), (94, 48), (90, 86), (80, 82), (80, 60), (20, 60), (20, 82)])),
              L(blob([(62, 12), (92, 46), (90, 84), (82, 82)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
              spk((12, 44), (30, 38), (18, 72), 5, z='f'), spk((28, 38), (46, 34), (38, 64), 4, z='f'),
              spk((54, 34), (72, 38), (64, 64), 4, z='f', light_left=False), spk((70, 40), (88, 44), (86, 72), 5, z='f', light_left=False),
              L(blob([(50, 6), (58, 10), (56, 40), (54, 70), (50, 62), (50, 36)], 5), 'streak', 'f', ln=True),
              L(ell(36, 75, 8.6, 8.6), 'mono', 'f', ln=True), L(ell(36, 75, 6, 6), (190, 220, 220, 255), 'f', False),
              L(ell(36, 75, 2.6, 3), OUTC, 'f', False),
              L(quad((28, 76), (8, 78), (14, 100)), WIRE, 'f', False, False, 2.0)],
    'side': [L(blob([(46, 94), (14, 92), (2, 62), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (92, 58), (76, 56), (62, 58), (56, 74), (52, 90)])),
             L(blob([(6, 50), (8, 88), (40, 92), (24, 64)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             spk((56, 30), (88, 40), (92, 70), 6, z='f', light_left=False),
             L(ell(86, 75, 4.6, 8), 'mono', 'f', ln=True), L(quad((84, 80), (60, 96), (30, 104)), WIRE, 'f', False, False, 2.0)],
    'back': [L(blob([(10, 88), (6, 48), (16, 16), (50, 4), (84, 16), (94, 48), (90, 88), (50, 94)])),
             spk((16, 84), (34, 90), (24, 104), 4), spk((34, 90), (50, 94), (44, 106), 4), spk((50, 94), (66, 90), (56, 106), 4, light_left=False),
             spk((66, 90), (84, 84), (76, 104), 4, light_left=False),
             L(blob([(58, 12), (92, 46), (90, 86), (66, 92)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
             strand([(50, 6), (50, 60)], 'streak', 'b', 2.0)],
}

# ------------------------------------------------------------------ Charles Oughtry: piel morena, pelo azul marino muy oscuro
# despeinado que le cae por la frente, electrodos blancos en las sienes y cara de enfado
CHARS['charles-oughtry'] = {
    'body': 'normal', 'pal': pal('#2a3a5a', '#b08040'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (60, 50)},
    'front': [L(blob([(10, 80), (6, 46), (16, 16), (50, 6), (84, 16), (94, 46), (90, 80), (80, 74), (80, 60), (20, 60), (20, 74)])),
              L(blob([(62, 14), (92, 44), (90, 78), (82, 76)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
              spk((12, 44), (30, 38), (18, 72), 5, z='f'), spk((28, 38), (46, 34), (38, 66), 5, z='f'),
              spk((50, 34), (68, 36), (62, 66), 5, z='f', light_left=False), spk((66, 38), (88, 44), (86, 74), 5, z='f', light_left=False)]
             + wires('front', 70, x=14),
    'side': [L(blob([(46, 94), (14, 92), (2, 62), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (92, 58), (76, 56), (62, 58), (56, 74), (52, 90)])),
             spk((4, 56), (8, 70), (-12, 70), 4),
             L(blob([(6, 50), (8, 88), (40, 92), (24, 64)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             spk((56, 30), (90, 40), (92, 72), 6, z='f', light_left=False)] + wires('side', 66),
    'back': [L(blob([(10, 82), (6, 46), (16, 16), (50, 6), (84, 16), (94, 46), (90, 82), (50, 88)])),
             spk((14, 80), (32, 86), (16, 98), 4), spk((32, 86), (50, 88), (40, 100), 4), spk((50, 88), (68, 86), (60, 100), 4, light_left=False),
             spk((68, 86), (86, 80), (84, 98), 4, light_left=False),
             L(blob([(58, 14), (92, 44), (90, 80), (66, 86)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3)] + wires('back', 70, x=14),
}

# ------------------------------------------------------------------ Clive Mooney: pelo castaño verdoso con raya y un mechón
# claro largo que le cae por delante de un ojo; electrodos en las sienes y gesto de enfado
CHARS['clive-mooney'] = {
    'body': 'normal', 'pal': pal('#5a4a28', '#f6bc80', streak='#a8a060', streak_d='#888040'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'lips', 'mouth_y': 94, 'mouth_w': 7, 'hairline': (56, 46)},
    'front': [L(blob([(12, 70), (10, 38), (22, 14), (50, 6), (78, 14), (90, 38), (88, 70)])),
              L(blob([(62, 14), (88, 36), (86, 66), (76, 62)], 6), 'shade', 'b', False), sheen(22, 46, 16, 3),
              strand([(44, 8), (30, 48)], 'deep', 'b', 1.0),
              L(blob([(44, 8), (58, 10), (68, 40), (72, 80), (66, 84), (60, 50), (50, 30)]), 'streak', 'f', ln=True),
              L(blob([(56, 12), (68, 42), (70, 78), (64, 50)], 5), 'streak_d', 'f', False)] + wires('front', 66, out=28),
    'side': [L(blob([(46, 92), (20, 88), (8, 62), (10, 30), (28, 10), (56, 4), (80, 14), (92, 32), (90, 52), (76, 48), (62, 52), (54, 66), (50, 84)])),
             L(blob([(12, 46), (16, 80), (38, 88), (26, 62)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             strand([(80, 16), (50, 10), (22, 36)], 'deep', 'b', 1.0),
             L(blob([(64, 18), (86, 28), (92, 60), (88, 76), (82, 56)], 5), 'streak', 'f', ln=True)] + wires('side', 62),
    'back': [L(blob([(12, 72), (10, 38), (22, 14), (50, 6), (78, 14), (90, 38), (88, 72), (66, 90), (34, 90)])),
             L(blob([(58, 14), (88, 36), (86, 70), (66, 88)], 6), 'shade', 'b', False), sheen(22, 46, 16, 3),
             strand([(50, 8), (50, 86)], 'deep', 'b', 1.0)] + wires('back', 66, out=28),
}

# ------------------------------------------------------------------ Neil Waters: corpulento, media melena castaña rojiza en forma
# de seta con un pelillo de punta; ojos afilados con sonrisa pícara y un cable que le cruza la cara
CHARS['neil-waters'] = {
    'body': 'corpulento', 'pal': pal('#8a4a40', '#fcc89a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': (62, 54)},
    'front': [spk((46, 10), (54, 10), (48, -6), 2.5),
              L(blob([(4, 70), (0, 44), (12, 16), (50, 6), (88, 16), (100, 44), (96, 70), (82, 66), (82, 60), (18, 60), (18, 66)])),
              L(blob([(62, 12), (98, 42), (94, 68), (84, 66)], 6), 'shade', 'b', False), sheen(18, 44, 18, 3),
              strand([(30, 20), (24, 58)], 'shade', 'b', 1.0), strand([(50, 16), (50, 58)], 'shade', 'b', 1.0), strand([(70, 20), (76, 58)], 'shade', 'b', 1.0),
              L([(10, 68), (30, 78), (70, 78), (90, 68)], WIRE, 'f', False, False, 2.0)],
    'side': [spk((44, 6), (52, 6), (50, -8), 2.5),
             L(blob([(46, 78), (10, 76), (0, 52), (6, 22), (28, 6), (60, 2), (86, 12), (100, 32), (96, 52), (78, 48), (60, 52), (52, 64)])),
             L(blob([(6, 44), (10, 72), (40, 76), (24, 56)], 6), 'shade', 'b', False), sheen(30, 64, 12, 3),
             L([(4, 70), (40, 80), (84, 82)], WIRE, 'f', False, False, 2.0)],
    'back': [spk((46, 10), (54, 10), (52, -6), 2.5, light_left=False),
             L(blob([(4, 72), (0, 44), (12, 16), (50, 6), (88, 16), (100, 44), (96, 72), (50, 80)])),
             L(blob([(58, 12), (98, 42), (94, 70), (66, 78)], 6), 'shade', 'b', False), sheen(18, 44, 18, 3),
             L([(10, 70), (30, 80), (70, 80), (90, 70)], WIRE, 'f', False, False, 2.0)],
}


# Nathan Swift con los Emperadores Oscuros: la coleta alta se le abre en una melena suelta de mechones ondulados que le
# caen por los lados y la espalda hasta los hombros
def _nathan_de():
    import copy
    from chars_sengoku import wavy
    base = copy.deepcopy(CHARS['nathan-swift'])
    locks_f = (wavy((6, 58), (16, 60), (-14, 110), -8) + wavy((-2, 50), (8, 52), (-24, 98), 8) + wavy((84, 60), (94, 58), (112, 110), 8, light_left=False)
               + wavy((92, 52), (102, 50), (124, 98), -8, light_left=False))
    base['front'] = locks_f + base['front']
    base['side'] = (wavy((-2, 60), (10, 62), (-20, 112), 8) + wavy((6, 70), (18, 72), (2, 120), -8) + wavy((-6, 46), (4, 48), (-30, 92), 8)) + base['side']
    base['back'] = (locks_f + wavy((24, 86), (36, 90), (18, 128), 8) + wavy((64, 90), (76, 86), (82, 128), -8, light_left=False)) + base['back']
    return base


CHARS['ie2-dark-emperors:nathan-swift'] = _nathan_de()
