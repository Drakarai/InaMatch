"""Academia Alius (IE2): Polvo de Diamantes, Prominence, Caos (mezcla de los dos) y Génesis, con los modelos 3D de la
enciclopedia y de la wiki (versión alienígena) y, para los que no tienen, sus retratos."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, pal, sheen, spk, strand
from chars_otaku import back_hair, glasses
from chars_sengoku import wavy
from chars_umbrella import BOB_B, BOB_F, BOB_S, bob_shade, fringe
from heads import quad

WHITE = (255, 255, 255, 255)
DARK = (24, 20, 24, 255)
SIDE_SKULL = [(44, 92), (22, 88), (12, 64), (14, 36), (30, 16), (56, 10), (78, 18), (88, 36), (76, 44), (60, 48), (52, 62), (50, 80)]
SKULL_F = [(16, 64), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 64)]
SKULL_B = [(16, 70), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 70), (66, 86), (34, 86)]
CAP_F = [(10, 70), (8, 40), (20, 16), (50, 6), (80, 16), (92, 40), (90, 70), (80, 64), (20, 64)]
CAP_B = [(10, 74), (8, 40), (20, 16), (50, 6), (80, 16), (92, 40), (90, 74), (66, 88), (34, 88)]
WIDE_FACE = blob([(12, 54), (50, 46), (88, 54), (92, 76), (86, 96), (66, 106), (50, 108), (34, 106), (14, 96), (8, 76)])
LONG_FACE = quad((20, 52), (18, 104), (50, 114)) + quad((50, 114), (82, 104), (80, 52))[1:] + quad((80, 52), (50, 26), (20, 52))[1:-1]


def spiky(view, s=1.0, lower=True):
    """Pelo de pinchos en todas direcciones (s: largo)."""
    if view == 'side':
        out = [spk((16, 40), (24, 22), (16 - 34 * s, 22 - 8 * s), 7), spk((24, 24), (42, 12), (24 - 18 * s, 12 - 28 * s), 7),
               spk((42, 12), (62, 6), (52, 6 - 30 * s), 7), spk((14, 58), (16, 40), (14 - 32 * s, 50), 6)]
        if lower:
            out.append(spk((18, 76), (22, 58), (18 - 28 * s, 76 + 6 * s), 5))
        return out + [spk((62, 12), (82, 22), (82 + 16 * s, 22 - 22 * s), 6, light_left=False)]
    out = [spk((8, 58), (12, 40), (8 - 22 * s, 48), 6), spk((12, 40), (24, 22), (12 - 18 * s, 22 - 14 * s), 7),
           spk((24, 22), (42, 12), (30 - 6 * s, 12 - 26 * s), 7), spk((42, 12), (58, 10), (50, 10 - 32 * s), 7),
           spk((58, 12), (76, 20), (70 + 6 * s, 20 - 28 * s), 7, light_left=False), spk((76, 22), (88, 40), (88 + 18 * s, 22 - 12 * s), 7, light_left=False),
           spk((88, 42), (92, 60), (92 + 22 * s, 50), 6, light_left=False)]
    if view == 'back':
        out += [L(blob(CAP_B))] + [spk((12, 72), (30, 86), (12 - 6 * s, 86 + 10 * s), 5), spk((30, 88), (50, 92), (40, 92 + 14 * s), 5),
                                   spk((50, 92), (70, 88), (60, 92 + 14 * s), 5, light_left=False), spk((70, 86), (88, 72), (88 + 6 * s, 86 + 10 * s), 5, light_left=False),
                                   L(blob([(58, 12), (90, 38), (88, 72), (66, 86)], 6), 'shade', 'b', False)]
    return out


def spiky_face(view, fr=True):
    """Casco y flequillo del pelo de pinchos."""
    if view == 'front':
        out = [L(blob(CAP_F)), L(blob([(62, 12), (90, 38), (88, 66), (78, 62)], 6), 'shade', 'b', False)]
        if fr:
            out += [spk((12, 46), (30, 40), (18, 70), 5, z='f'), spk((30, 40), (48, 36), (38, 60), 5, z='f'),
                    spk((52, 36), (70, 40), (62, 60), 5, z='f', light_left=False), spk((70, 40), (88, 46), (84, 70), 5, z='f', light_left=False)]
        return out
    out = [L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False)]
    if fr:
        out.append(spk((56, 30), (88, 40), (92, 66), 6, z='f', light_left=False))
    return out


def full(spec_front, spec_side, spec_back):
    return {'front': spec_front, 'side': spec_side, 'back': spec_back}


# ================================================================== Polvo de Diamantes
# ------------------------------------------------------------------ Ben North / Beluga (portero): pelo negro con un tupé de punta
# hacia arriba y una máscara azul agrietada que le tapa la cara de la frente a la nariz; piel verdosa
CHARS['ben-north'] = {
    'body': 'normal', 'pal': pal('#2a2a2e', '#7aa890', mask='#2a7ac0', mask_d='#1a5a90'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 94, 'big_ears': 1, 'hairline': False},
    'front': [spk((30, 20), (70, 14), (34, -24), 8), L(blob(SKULL_F)), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'shade', 'b', False),
              L(blob([(16, 30), (50, 22), (84, 30), (86, 82), (50, 86), (14, 82)]), 'mask', 'f', ln=True),
              L(blob([(56, 24), (84, 32), (84, 80), (60, 84)], 6), 'mask_d', 'f', False),
              L([(54, 24), (48, 44), (58, 56), (50, 72)], WHITE, 'f', False, False, 1.4)],
    'side': [spk((30, 16), (60, 8), (20, -20), 8), L(blob(SIDE_SKULL)),
             L(blob([(50, 28), (90, 32), (94, 82), (58, 84)]), 'mask', 'f', ln=True)],
    'back': [spk((30, 20), (70, 14), (34, -24), 8), L(blob(SKULL_B))] + back_hair(),
}

# ------------------------------------------------------------------ Alan Downhill / IQ: pelo gris oscuro de pinchos, gafas
# rectangulares finas y mirada seria
CHARS['alan-downhill'] = {
    'body': 'normal', 'pal': pal('#3e4446', '#fcd4a8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'glasses': (30, 30, 34, 255), 'glasses_rect': True, 'hairline': (58, 50)},
    'front': spiky('front', 0.8) + spiky_face('front'), 'side': spiky('side', 0.8) + spiky_face('side'), 'back': spiky('back', 0.8),
}

# ------------------------------------------------------------------ Claire Lesnow / Clara: media melena azul marino recta con
# raya al lado y dos pasadores naranjas a los lados; mirada fría
CHARS['claire-lesnow'] = {
    'body': 'chica', 'pal': pal('#24447a', '#fcdcbc', iris='#3a6a6a', clip='#e8901a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 92, 'hairline': [(10, 70), (24, 54), (44, 42), (60, 48), (76, 56), (90, 70)]},
    'front': [L(blob(BOB_F))] + bob_shade('front') + [strand([(44, 8), (34, 48)], 'deep', 'b', 1.1),
              L([(8, 64), (20, 64), (20, 70), (8, 70)], 'clip', 'f', ln=True), L([(80, 64), (92, 64), (92, 70), (80, 70)], 'clip', 'f', ln=True)],
    'side': [L(blob(BOB_S))] + bob_shade('side') + [L([(48, 62), (60, 62), (60, 68), (48, 68)], 'clip', 'f', ln=True),
             spk((56, 30), (90, 40), (92, 74), 6, z='f', light_left=False)],
    'back': [L(blob(BOB_B))] + bob_shade('back'),
}

# ------------------------------------------------------------------ Albert Denver / Gokka: corpulento, piel tostada, pelo azul marino
# con un cuerno central alto y dos alas puntiagudas a los lados; ojos amarillos y dientes apretados
CHARS['albert-denver'] = {
    'body': 'corpulento', 'pal': pal('#1e2a5a', '#b88a50', iris='#e0b020'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 94, 'face_front': WIDE_FACE, 'hairline': (54, 46)},
    'front': [spk((38, 14), (62, 14), (50, -24), 7), spk((0, 46), (16, 26), (-24, 14), 6), spk((84, 26), (100, 46), (124, 14), 6, light_left=False),
              L(blob([(12, 60), (10, 32), (24, 14), (50, 8), (76, 14), (90, 32), (88, 60)])), L(blob([(62, 14), (88, 34), (86, 58), (74, 54)], 6), 'shade', 'b', False)],
    'side': [spk((32, 14), (54, 8), (40, -24), 7), spk((14, 40), (26, 22), (-18, 10), 6),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False)],
    'back': [spk((38, 14), (62, 14), (50, -24), 7), spk((0, 46), (16, 26), (-24, 14), 6), spk((84, 26), (100, 46), (124, 14), 6, light_left=False),
             L(blob(SKULL_B))] + back_hair(),
}

# ------------------------------------------------------------------ Ving Rice / Frost: piel pálida, cara pintada con un triángulo
# verde azulado en la frente y ojos negros, pelo naranja recogido en un moño alto con mechones largos que caen a los lados
CHARS['ving-rice'] = {
    'body': 'chica', 'pal': pal('#e8602a', '#f4ece4', paint='#2a9a9a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 94, 'hairline': (62, 50)},
    'front': [L(blob([(30, 20), (28, -6), (50, -18), (72, -6), (70, 20)])), L(blob([(54, -14), (70, -6), (68, 18)], 4), 'shade', 'b', False),
              L(blob(SKULL_F)), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'shade', 'b', False),
              wavy((14, 40), (24, 36), (-12, 84), 7), wavy((76, 36), (86, 40), (112, 84), -7, light_left=False),
              L([(36, 56), (64, 56), (50, 74)], 'paint', 'f', ln=True),
              L(blob([(28, 72), (42, 70), (40, 80), (30, 80)], 4), DARK, 'f'), L(blob([(72, 72), (58, 70), (60, 80), (70, 80)], 4), DARK, 'f')],
    'side': [L(blob([(30, 16), (26, -10), (48, -20), (64, -8), (56, 16)])), L(blob(SIDE_SKULL)),
             L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False)] + wavy((20, 40), (30, 36), (-6, 86), 7)
            + [L(blob([(78, 72), (90, 71), (89, 80), (80, 80)], 4), DARK, 'f')],
    'back': [L(blob([(30, 20), (28, -6), (50, -18), (72, -6), (70, 20)])), L(blob(SKULL_B))] + back_hair()
            + wavy((14, 40), (24, 36), (-12, 84), 7) + wavy((76, 36), (86, 40), (112, 84), -7, light_left=False),
}

# ------------------------------------------------------------------ Denzel Freezer / Gazel no: Droll... piel verdosa clara, pelo
# verde azulado de pinchos altos hacia arriba, ojos rasgados y ceño
CHARS['denzel-freezer'] = {
    'body': 'normal', 'pal': pal('#1e7a7a', '#dccca8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (56, 50)},
    'front': [spk((14, 34), (30, 14), (16, -26), 7), spk((30, 14), (50, 8), (40, -32), 7), spk((50, 8), (70, 14), (60, -32), 7, light_left=False),
              spk((70, 14), (86, 34), (84, -26), 7, light_left=False), spk((6, 66), (14, 52), (-8, 72), 4), spk((86, 52), (94, 66), (108, 72), 4, light_left=False)]
             + spiky_face('front'),
    'side': [spk((20, 30), (36, 12), (6, -24), 8), spk((36, 12), (58, 6), (42, -32), 8), spk((14, 58), (18, 40), (-12, 56), 5)] + spiky_face('side'),
    'back': [spk((14, 34), (30, 14), (16, -26), 7), spk((30, 14), (50, 8), (40, -32), 7), spk((50, 8), (70, 14), (60, -32), 7, light_left=False),
             spk((70, 14), (86, 34), (84, -26), 7, light_left=False), L(blob(CAP_B)), L(blob([(58, 12), (90, 38), (88, 72), (66, 86)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Lucy Hailstone / IC: melena granate lisa y larga hasta el pecho
# con raya al medio, ojos rojos afilados
CHARS['lucy-hailstone'] = {
    'body': 'chica', 'pal': pal('#8a3a5a', '#fcd4a8', iris='#c02a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 92, 'hairline': [(14, 70), (26, 52), (42, 42), (50, 48), (58, 42), (74, 52), (86, 70)]},
    'front': [L(blob([(6, 118), (2, 60), (12, 18), (50, 4), (88, 18), (98, 60), (94, 118), (82, 112), (82, 66), (18, 66), (18, 112)])),
              L(blob([(62, 12), (96, 50), (92, 112), (84, 110)], 6), 'shade', 'b', False), sheen(22, 46, 18, 3),
              strand([(50, 6), (50, 46)], 'deep', 'b', 1.2),
              L(blob([(10, 56), (22, 58), (24, 104), (14, 116), (6, 90)]), 'mid', 'f'), L(blob([(90, 56), (78, 58), (76, 104), (86, 116), (94, 90)]), 'mid', 'f'),
              strand([(22, 60), (23, 104), (16, 114)], OUTC, 'f', 1.0), strand([(78, 60), (77, 104), (84, 114)], OUTC, 'f', 1.0)],
    'side': [L(blob([(56, 116), (14, 118), (0, 66), (4, 28), (24, 8), (56, 4), (82, 14), (94, 34), (92, 56), (76, 54), (62, 58), (58, 78), (60, 104)])),
             L(blob([(4, 50), (8, 108), (46, 112), (24, 74)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             spk((56, 30), (90, 40), (92, 70), 5, z='f', light_left=False)],
    'back': [L(blob([(6, 118), (2, 60), (12, 18), (50, 4), (88, 18), (98, 60), (94, 118), (50, 124)])),
             L(blob([(58, 12), (96, 50), (92, 116), (66, 122)], 6), 'shade', 'b', False), sheen(22, 46, 18, 3),
             strand([(50, 8), (50, 118)], 'deep', 'b', 1.2)],
}

# ------------------------------------------------------------------ Brad Coldwater / Droll... piel tostada, pelo castaño oscuro de
# pinchos hacia atrás, rayas rojas en las mejillas y una mascarilla blanca con costuras
CHARS['brad-coldwater'] = {
    'body': 'normal', 'pal': pal('#3a2420', '#d8a070', mask='#ece4dc', mask_d='#b8aca0', paint='#c03a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'hairline': (56, 48)},
    'front': spiky('front', 0.9) + spiky_face('front')
             + [L([(22, 74), (30, 80)], 'paint', 'f', False, False, 1.6), L([(78, 74), (70, 80)], 'paint', 'f', False, False, 1.6),
                L(blob([(36, 84), (50, 80), (64, 84), (60, 98), (50, 102), (40, 98)]), 'mask', 'f', ln=True), L([(50, 80), (50, 102)], 'mask_d', 'f', False, False, 1.0)],
    'side': spiky('side', 0.9) + spiky_face('side') + [L(blob([(78, 82), (94, 84), (92, 100), (80, 100)]), 'mask', 'f', ln=True)],
    'back': spiky('back', 0.9),
}

# ------------------------------------------------------------------ Dawson Foxx / Blow: pelo verde muy oscuro peinado hacia un lado
# en una gran ola y gafas de visera verde azulado translúcida sobre los ojos
CHARS['dawson-foxx'] = {
    'body': 'normal', 'pal': pal('#1a3a34', '#b88858', lens=(80, 200, 210, 180)),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (58, 50)},
    'front': [L(blob(SKULL_F)), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'shade', 'b', False)]
             + wavy((14, 40), (50, 14), (110, 10), -10, z='f') + wavy((40, 26), (70, 26), (106, 30), -6, z='f', light_left=False)
             + [L(blob([(16, 66), (50, 62), (84, 66), (82, 82), (50, 80), (18, 82)]), 'lens', 'f', ln=True)],
    'side': [L(blob(SIDE_SKULL))] + wavy((20, 36), (52, 12), (110, 8), -10) + wavy((40, 26), (70, 24), (104, 28), -6)
            + [L(blob([(64, 66), (94, 66), (94, 82), (66, 82)]), 'lens', 'f', ln=True)],
    'back': [L(blob(SKULL_B))] + back_hair() + wavy((86, 40), (50, 14), (-10, 10), 10, z='f'),
}

# ------------------------------------------------------------------ Bernie White / Lionne... pelo castaño rojizo corto de pinchos
# hacia arriba, ojos rojos y ceño
CHARS['bernie-white'] = {
    'body': 'normal', 'pal': pal('#8a3a20', '#fcc8a0', iris='#c02a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (56, 50)},
    'front': [spk((22, 22), (40, 12), (26, -16), 6), spk((40, 12), (58, 10), (50, -22), 6), spk((58, 12), (76, 20), (74, -16), 6, light_left=False),
              spk((10, 44), (20, 26), (2, 8), 5), spk((80, 26), (90, 44), (98, 8), 5, light_left=False)] + spiky_face('front'),
    'side': [spk((22, 28), (40, 12), (14, -14), 6), spk((40, 12), (60, 8), (52, -20), 6)] + spiky_face('side'),
    'back': [spk((22, 22), (40, 12), (26, -16), 6), spk((40, 12), (58, 10), (50, -22), 6), spk((58, 12), (76, 20), (74, -16), 6, light_left=False),
             L(blob(SKULL_B))] + back_hair(),
}

# ------------------------------------------------------------------ Bryce Whitingale / Gazel (capitán): pelo blanco plateado muy
# abultado, una nube de mechones gruesos que se curvan hacia fuera en todas direcciones; ojos verde azulado
GAZEL_F = [spk((2, 60), (8, 36), (-24, 48), 10), spk((8, 34), (24, 12), (-18, 2), 10), spk((26, 10), (48, 0), (22, -24), 10),
           spk((50, 0), (72, 8), (78, -24), 10, light_left=False), spk((74, 12), (92, 34), (118, 2), 10, light_left=False),
           spk((92, 36), (98, 60), (124, 48), 10, light_left=False), spk((4, 74), (12, 58), (-16, 80), 7), spk((88, 58), (96, 74), (116, 80), 7, light_left=False)]
CHARS['bryce-whitingale'] = {
    'body': 'normal', 'pal': pal('#dcdcdc', '#fcd0a4', iris='#3a7a7a', shade='#b8aeb0'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 93, 'hairline': (58, 50)},
    'front': GAZEL_F + [L(bumpy(50, 30, 48, 30, 10, 0.1)), L(bumpy(70, 34, 22, 22, 6, 0.1), 'shade', 'b', False)]
             + [spk((10, 44), (30, 36), (6, 74), 8, z='f'), spk((30, 36), (50, 32), (34, 66), 8, z='f'),
                spk((50, 32), (70, 36), (66, 66), 8, z='f', light_left=False), spk((70, 36), (90, 44), (94, 74), 8, z='f', light_left=False)],
    'side': [spk((16, 40), (24, 18), (-24, 20), 11), spk((24, 20), (46, 6), (8, -24), 11), spk((46, 6), (66, 6), (64, -26), 10, light_left=False),
             spk((12, 60), (16, 38), (-26, 60), 10), spk((18, 80), (22, 58), (-16, 90), 8),
             L(bumpy(44, 32, 44, 30, 10, 0.1))] + [L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False)]
            + [spk((54, 26), (86, 34), (100, 66), 9, z='f', light_left=False)],
    'back': GAZEL_F + [L(bumpy(50, 36, 48, 36, 10, 0.1)), L(bumpy(68, 44, 22, 26, 6, 0.1), 'shade', 'b', False),
                       spk((10, 72), (30, 84), (2, 104), 8), spk((30, 86), (50, 90), (36, 112), 8), spk((50, 90), (70, 86), (66, 112), 8, light_left=False),
                       spk((70, 84), (90, 72), (98, 104), 8, light_left=False)],
}

# ================================================================== Prominence
# ------------------------------------------------------------------ Grant Cook / Grent (portero): piel morena, pelo gris como rocas
# con una trenza gruesa que cae a un lado, una mascarilla blanca redonda con un agujero negro y ojos pintados de negro
CHARS['grant-cook'] = {
    'body': 'corpulento', 'pal': pal('#9a9a9e', '#c0805a', mask='#f0eae4', mask_d='#c0b4ac'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'none', 'hairline': False},
    'front': [L(blob(SKULL_F)), L(bumpy(70, 20, 22, 18, 6, 0.12)), L(bumpy(40, 14, 18, 14, 6, 0.12)), L(bumpy(70, 20, 12, 10, 6, 0.12), 'shade', 'b', False),
              L(bumpy(14, 56, 7, 7, 6, 0.12)), L(bumpy(10, 70, 7, 7, 6, 0.12)), L(bumpy(8, 84, 7, 7, 6, 0.12)), L(bumpy(8, 98, 6, 6, 6, 0.12)),
              L(blob([(26, 70), (44, 66), (42, 76), (28, 78)], 4), DARK, 'f'), L(blob([(74, 70), (56, 66), (58, 76), (72, 78)], 4), DARK, 'f'),
              L(ell(50, 92, 14, 12), 'mask', 'f', ln=True), L(ell(50, 92, 6, 6), DARK, 'f', False)],
    'side': [L(blob(SIDE_SKULL)), L(bumpy(40, 18, 30, 18, 8, 0.12)), L(bumpy(20, 60, 8, 8, 6, 0.12)), L(bumpy(16, 76, 8, 8, 6, 0.12)), L(bumpy(16, 92, 7, 7, 6, 0.12)),
             L(blob([(76, 70), (90, 68), (90, 76), (78, 78)], 4), DARK, 'f'), L(ell(86, 92, 8, 11), 'mask', 'f', ln=True), L(ell(90, 92, 3, 4), DARK, 'f', False)],
    'back': [L(blob(SKULL_B)), L(bumpy(50, 24, 40, 22, 10, 0.12)), L(bumpy(66, 28, 18, 12, 6, 0.12), 'shade', 'b', False),
             L(bumpy(20, 60, 8, 8, 6, 0.12)), L(bumpy(18, 76, 8, 8, 6, 0.12)), L(bumpy(16, 92, 7, 7, 6, 0.12))],
}

# ------------------------------------------------------------------ Bonnie Sparks / Barra: melena morada larga con las puntas
# abiertas, un gran lazo verde azulado en lo alto y gafas de aviador verdes sobre los ojos
CHARS['bonnie-sparks'] = {
    'body': 'chica', 'pal': pal('#6a3a7a', '#fcd4b0', bow='#3aa0a0', bow_d='#2a7878', rim='#4aa0a0', lens='#e8e0d0'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'hairline': (60, 50)},
    'front': [L(blob([(8, 70), (2, 96), (-14, 112), (8, 112), (20, 96), (20, 64)])), L(blob([(92, 70), (98, 96), (114, 112), (92, 112), (80, 96), (80, 64)])),
              L(blob(CAP_F)), L(blob([(62, 12), (90, 38), (88, 66), (78, 62)], 6), 'shade', 'b', False), sheen(22, 48, 14, 3),
              L(blob([(30, 6), (18, -10), (24, -18), (46, -2), (54, -2), (76, -18), (82, -10), (70, 6), (50, 4)]), 'bow', 'f', ln=True),
              L(ell(50, 0, 6, 5), 'bow_d', 'f', ln=True),
              L(ell(34, 72, 11, 9), 'rim', 'f', ln=True), L(ell(66, 72, 11, 9), 'rim', 'f', ln=True),
              L(ell(34, 72, 7.4, 6), 'lens', 'f', False), L(ell(66, 72, 7.4, 6), 'lens', 'f', False)],
    'side': [L(blob([(20, 60), (6, 90), (-10, 110), (12, 110), (30, 80)])),
             L(blob(SIDE_SKULL), 'mid'), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             L(blob([(34, 6), (22, -10), (30, -16), (48, -2), (44, 8)]), 'bow', 'f', ln=True),
             L(ell(84, 72, 7, 9), 'rim', 'f', ln=True), L(ell(85, 72, 4, 6), 'lens', 'f', False)],
    'back': [L(blob([(6, 100), (0, 60), (10, 20), (50, 6), (90, 20), (100, 60), (94, 100), (110, 116), (50, 104), (-10, 116)])),
             L(blob([(58, 12), (96, 56), (100, 112), (66, 104)], 6), 'shade', 'b', False),
             L(blob([(30, 6), (18, -10), (24, -18), (46, -2), (54, -2), (76, -18), (82, -10), (70, 6), (50, 4)]), 'bow', 'f', ln=True)],
}

# ------------------------------------------------------------------ Val Flamewood / Torch... piel morena, pelo castaño muy oscuro de
# pinchos y gafas de sol naranjas grandes; sonrisa con dientes
CHARS['val-flamewood'] = {
    'body': 'normal', 'pal': pal('#2e2016', '#b8804a', lens='#d88a1a', rim='#e8c080'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 92, 'hairline': (56, 50)},
    'front': spiky('front', 0.8) + spiky_face('front')
             + [L([(14, 66), (46, 66), (44, 80), (18, 80)], 'lens', 'f', ln=True), L([(86, 66), (54, 66), (56, 80), (82, 80)], 'lens', 'f', ln=True),
                L([(46, 68), (54, 68)], 'rim', 'f', False, False, 1.8)],
    'side': spiky('side', 0.8) + spiky_face('side') + [L([(72, 66), (94, 66), (92, 80), (74, 80)], 'lens', 'f', ln=True)],
    'back': spiky('back', 0.8),
}

# ------------------------------------------------------------------ Sean Ashford: pelo gris lila corto con dos picos a los lados,
# mirada afilada y sonrisa de lado
CHARS['sean-ashford'] = {
    'body': 'normal', 'pal': pal('#7a7290', '#fcd0a4'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': [(14, 62), (30, 48), (44, 44), (50, 50), (56, 44), (70, 48), (86, 62)]},
    'front': [spk((14, 30), (30, 14), (16, -10), 5), spk((70, 14), (86, 30), (84, -10), 5, light_left=False),
              L(blob(SKULL_F)), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'shade', 'b', False), sheen(28, 52, 14, 3)],
    'side': [spk((28, 20), (44, 10), (24, -12), 5), L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False)],
    'back': [spk((14, 30), (30, 14), (16, -10), 5), spk((70, 14), (86, 30), (84, -10), 5, light_left=False), L(blob(SKULL_B))] + back_hair(),
}

# ------------------------------------------------------------------ Nigel August / Nepper: pelo castaño oliva despeinado hacia atrás,
# una cinta roja y blanca muy ancha en la frente y ojos pintados de negro
CHARS['nigel-august'] = {
    'body': 'normal', 'pal': pal('#6a5a1a', '#fcd0a4', band='#d02a1a', band_l='#f0e8e0'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 93, 'eye_y': 78, 'hairline': False},
    'front': wavy((60, 12), (80, 18), (110, 0), -8, light_left=False) + wavy((80, 26), (90, 40), (116, 34), -6, light_left=False) + wavy((10, 50), (16, 36), (-8, 40), 5)
             + [L(blob(CAP_F)), L(blob([(62, 12), (90, 38), (88, 66), (78, 62)], 6), 'shade', 'b', False),
                L(blob([(8, 64), (8, 48), (50, 40), (92, 48), (92, 64), (50, 60)]), 'band', 'f', ln=True),
                L(blob([(30, 46), (50, 42), (66, 50), (54, 56), (40, 52)]), 'band_l', 'f', False),
                L(blob([(26, 72), (46, 70), (46, 84), (28, 84)], 4), DARK, 'f'), L(blob([(74, 72), (54, 70), (54, 84), (72, 84)], 4), DARK, 'f')],
    'side': wavy((30, 14), (60, 8), (100, 0), -8) + wavy((16, 40), (26, 20), (-16, 10), 7) + wavy((14, 60), (18, 42), (-16, 54), 6)
            + spiky_face('side', False)
            + [L(quad((10, 50), (50, 40), (94, 46)) + quad((94, 62), (50, 58), (10, 64)), 'band', 'f', ln=True),
               L(blob([(74, 72), (92, 70), (92, 84), (76, 84)], 4), DARK, 'f')],
    'back': wavy((60, 12), (80, 18), (110, 0), -8, light_left=False) + [L(blob(CAP_B))]
            + wavy((10, 70), (30, 84), (2, 96), 6) + wavy((30, 86), (50, 90), (40, 106), 6) + wavy((50, 90), (70, 86), (66, 106), -6, light_left=False)
            + [L(blob(SKULL_B), 'shade'), L(quad((8, 56), (50, 48), (92, 56)) + quad((92, 70), (50, 64), (8, 70)), 'band', 'f', ln=True)],
}

# ------------------------------------------------------------------ Sam Bournes: chica, melena verde azulado oscura con ondas que
# salen a los lados, gafas finas y ceño
CHARS['sam-bournes'] = {
    'body': 'chica', 'pal': pal('#1e5a5a', '#fcd0a4'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 92, 'glasses': (40, 30, 40, 255), 'glasses_rect': True, 'hairline': (60, 50)},
    'front': wavy((4, 60), (12, 70), (-24, 76), 7) + wavy((88, 70), (96, 60), (124, 76), -7, light_left=False) + wavy((8, 74), (16, 82), (-16, 98), -6)
             + wavy((84, 82), (92, 74), (116, 98), 6, light_left=False) + wavy((60, 6), (78, 10), (100, -10), -6, light_left=False)
             + [L(blob(BOB_F))] + bob_shade('front') + fringe(4, 36, 62),
    'side': wavy((6, 60), (12, 74), (-24, 78), 7) + wavy((12, 76), (20, 86), (-14, 100), -6) + [L(blob(BOB_S))] + bob_shade('side')
            + [spk((56, 30), (90, 40), (92, 66), 5, z='f', light_left=False)],
    'back': wavy((4, 60), (12, 70), (-24, 76), 7) + wavy((88, 70), (96, 60), (124, 76), -7, light_left=False) + [L(blob(BOB_B))] + bob_shade('back'),
}

# ------------------------------------------------------------------ Ben Blowton / Bomba: corpulento, pelo rubio anaranjado enorme y
# despeinado que cae hasta los hombros, una cinta azul fina en la frente y antifaz negro
CHARS['ben-blowton'] = {
    'body': 'corpulento', 'pal': pal('#e0a028', '#e8a878', band='#2a6ab0'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'eye_y': 76, 'hairline': False},
    'front': [L(blob([(0, 90), (-12, 54), (2, 20), (50, 0), (98, 20), (112, 54), (100, 90), (84, 78), (82, 60), (18, 60), (16, 78)])),
              spk((-10, 70), (0, 86), (-26, 100), 6), spk((100, 86), (110, 70), (126, 100), 6, light_left=False),
              spk((40, 4), (56, 2), (52, -16), 4),
              L(blob([(60, 6), (106, 50), (100, 86), (86, 76)], 6), 'shade', 'b', False), sheen(22, 46, 14, 3),
              L(quad((14, 48), (50, 38), (86, 48)), 'band', 'f', False, False, 2.6),
              L(blob([(20, 70), (50, 68), (80, 70), (78, 84), (56, 84), (50, 78), (44, 84), (22, 84)], 4), DARK, 'f'),
              spk((14, 44), (34, 38), (24, 74), 5, z='f'), spk((34, 36), (50, 32), (44, 62), 4, z='f'),
              spk((50, 32), (66, 36), (58, 62), 4, z='f', light_left=False), spk((66, 38), (86, 44), (78, 74), 5, z='f', light_left=False)],
    'side': [L(blob([(48, 90), (0, 96), (-16, 60), (-6, 24), (24, 2), (60, -2), (86, 12), (96, 34), (92, 56), (76, 54), (62, 56), (56, 72)])),
             spk((-6, 70), (4, 90), (-26, 104), 6), L(blob([(-6, 50), (0, 90), (36, 90), (16, 64)], 6), 'shade', 'b', False),
             L(quad((10, 44), (50, 34), (92, 42)), 'band', 'f', False, False, 2.6), L(blob([(70, 70), (94, 70), (92, 84), (72, 84)], 4), DARK, 'f'),
             spk((56, 30), (90, 40), (94, 72), 6, z='f', light_left=False)],
    'back': [L(blob([(0, 94), (-12, 54), (2, 20), (50, 0), (98, 20), (112, 54), (100, 94), (50, 100)])),
             spk((-10, 70), (0, 86), (-26, 100), 6), spk((100, 86), (110, 70), (126, 100), 6, light_left=False),
             L(blob([(58, 6), (106, 50), (100, 92), (66, 98)], 6), 'shade', 'b', False), L(quad((2, 50), (50, 40), (98, 50)), 'band', 'f', False, False, 2.6)],
}

# ------------------------------------------------------------------ Ethan Whitering / Heat: pelo rubio ceniza muy claro de pinchos
# grandes en todas direcciones, ojos verde azulado y pecas
CHARS['ethan-whitering'] = {
    'body': 'normal', 'pal': pal('#ece0c8', '#fcd8b8', iris='#2a8a8a', shade='#c8b8a0', freckle='#e0a080'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (58, 50)},
    'front': spiky('front', 1.1) + spiky_face('front') + [L(ell(x, y, 1.1, 1.1), 'freckle', 'f', False) for x, y in ((26, 86), (30, 88), (74, 86), (70, 88))],
    'side': spiky('side', 1.1) + spiky_face('side'),
    'back': spiky('back', 1.1),
}

# ------------------------------------------------------------------ Brenda Firequest: chica, pelo naranja con un rizo en espiral en
# lo alto y media melena con las puntas hacia dentro; ojos verde azulado
CHARS['brenda-firequest'] = {
    'body': 'chica', 'pal': pal('#e0702a', '#fcd8b8', iris='#2a8a9a'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 92, 'hairline': (60, 52)},
    'front': [L(blob(BOB_F))] + bob_shade('front')
             + [L(blob([(70, 10), (86, 2), (94, 14), (84, 22), (78, 14), (86, 10)], 6), 'mid', 'f', ln=True)] + fringe(4, 36, 62),
    'side': [L(blob(BOB_S))] + bob_shade('side') + [L(blob([(60, 6), (76, -2), (84, 10), (74, 18), (68, 10), (76, 6)], 6), 'mid', 'f', ln=True),
             spk((56, 30), (90, 40), (92, 66), 5, z='f', light_left=False)],
    'back': [L(blob(BOB_B))] + bob_shade('back'),
}

# ------------------------------------------------------------------ Jim Flareson / Siden: piel morena, pelo gris enorme de pinchos
# hacia arriba y a los lados con dos trenzas grises, ojos amarillos con antifaz negro
CHARS['jim-flareson'] = {
    'body': 'normal', 'pal': pal('#6e6c70', '#9a6a44', iris='#e0b020'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 94, 'eye_y': 76, 'face_front': WIDE_FACE, 'hairline': (54, 46)},
    'front': [spk((-2, 40), (10, 22), (-28, 12), 7), spk((10, 20), (30, 6), (-4, -18), 7), spk((30, 6), (50, 2), (34, -28), 7),
              spk((50, 2), (70, 6), (66, -28), 7, light_left=False), spk((70, 6), (90, 20), (104, -18), 7, light_left=False),
              spk((90, 22), (102, 40), (128, 12), 7, light_left=False),
              L(blob([(6, 60), (4, 30), (20, 10), (50, 4), (80, 10), (96, 30), (94, 60), (80, 54), (20, 54)])),
              L(blob([(62, 10), (94, 32), (92, 58), (78, 54)], 6), 'shade', 'b', False),
              L(blob([(10, 60), (20, 60), (20, 104), (10, 104)]), 'mid', 'f', ln=True), L(blob([(80, 60), (90, 60), (90, 104), (80, 104)]), 'mid', 'f', ln=True),
              L(blob([(20, 68), (50, 66), (80, 68), (78, 82), (56, 82), (50, 76), (44, 82), (22, 82)], 4), DARK, 'f')],
    'side': [spk((16, 30), (30, 10), (-16, -8), 8), spk((30, 10), (52, 4), (32, -28), 8), spk((52, 4), (72, 10), (76, -22), 7, light_left=False),
             spk((8, 50), (14, 30), (-24, 32), 7), L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             L(blob([(26, 60), (36, 60), (36, 104), (26, 104)]), 'mid', 'f', ln=True), L(blob([(70, 68), (94, 68), (92, 82), (72, 82)], 4), DARK, 'f')],
    'back': [spk((-2, 40), (10, 22), (-28, 12), 7), spk((10, 20), (30, 6), (-4, -18), 7), spk((30, 6), (50, 2), (34, -28), 7),
             spk((50, 2), (70, 6), (66, -28), 7, light_left=False), spk((70, 6), (90, 20), (104, -18), 7, light_left=False),
             spk((90, 22), (102, 40), (128, 12), 7, light_left=False), L(blob(SKULL_B), 'mid'), L(blob([(58, 12), (86, 36), (84, 68), (66, 84)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Claude Beacons / Burn (capitán): pelo rojo intenso en llamas
# gruesas que suben hacia arriba y se abren a los lados, ojos dorados
BURN_F = [spk((0, 56), (8, 34), (-22, 26), 9), spk((10, 30), (28, 10), (-6, -18), 9), spk((28, 10), (50, 2), (34, -32), 9),
          spk((50, 2), (72, 10), (70, -32), 9, light_left=False), spk((72, 10), (90, 30), (108, -18), 9, light_left=False),
          spk((92, 34), (100, 56), (122, 26), 9, light_left=False), spk((4, 70), (12, 56), (-14, 76), 6), spk((88, 56), (96, 70), (114, 76), 6, light_left=False)]
CHARS['claude-beacons'] = {
    'body': 'normal', 'pal': pal('#c8101a', '#fcd0a4', iris='#c8a020'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': (58, 50)},
    'front': BURN_F + [L(bumpy(50, 30, 44, 28, 10, 0.1)), L(bumpy(70, 34, 20, 20, 6, 0.1), 'shade', 'b', False)]
             + [spk((12, 46), (30, 38), (14, 72), 7, z='f'), spk((30, 38), (50, 34), (38, 64), 7, z='f'),
                spk((50, 34), (70, 38), (62, 64), 7, z='f', light_left=False), spk((70, 38), (88, 46), (86, 72), 7, z='f', light_left=False)],
    'side': [spk((16, 40), (24, 18), (-22, 10), 10), spk((24, 20), (46, 6), (14, -30), 10), spk((46, 6), (66, 6), (64, -32), 9, light_left=False),
             spk((12, 60), (16, 38), (-24, 50), 9), spk((18, 80), (22, 58), (-12, 88), 7),
             L(bumpy(44, 32, 42, 28, 10, 0.1)), L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((54, 28), (86, 36), (96, 64), 8, z='f', light_left=False)],
    'back': BURN_F + [L(bumpy(50, 36, 46, 34, 10, 0.1)), L(bumpy(68, 44, 20, 24, 6, 0.1), 'shade', 'b', False),
                      spk((10, 72), (30, 84), (4, 102), 8), spk((30, 86), (50, 90), (38, 110), 8), spk((50, 90), (70, 86), (64, 110), 8, light_left=False),
                      spk((70, 84), (90, 72), (96, 102), 8, light_left=False)],
}

# ================================================================== Génesis
# ------------------------------------------------------------------ Nelson Rockwell / Nero (portero): pelo verde de pinchos cortos
# en todas direcciones, ojos rojos con ojeras y pendientes morados
CHARS['nelson-rockwell'] = {
    'body': 'normal', 'pal': pal('#3a8a2a', '#f8ecd8', iris='#c01a1a', ear='#8a3aa0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (56, 50)},
    'front': spiky('front', 0.7) + spiky_face('front') + [L(ell(16, 84, 2.4, 3.4), 'ear', 'f', ln=True), L(ell(84, 84, 2.4, 3.4), 'ear', 'f', ln=True)],
    'side': spiky('side', 0.7) + spiky_face('side'), 'back': spiky('back', 0.7),
}

# ------------------------------------------------------------------ Gail Baker / Coyote: pelo castaño recogido en una coleta alta
# muy larga con mechones a los lados, ojos amarillos y sonrisa con colmillos
CHARS['gail-baker'] = {
    'body': 'normal', 'pal': pal('#6a4a34', '#e8c09a', iris='#e0c020'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 94, 'big_ears': 1, 'hairline': (54, 44)},
    'front': wavy((52, 6), (60, 4), (68, -26), -6, light_left=False)
             + [L(blob(SKULL_F)), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'shade', 'b', False), sheen(28, 52, 14, 3)]
             + wavy((12, 44), (24, 44), (2, 104), 6, z='f') + wavy((76, 44), (88, 44), (98, 104), -6, z='f', light_left=False),
    'side': wavy((40, 8), (50, 4), (-6, 100), 10) + [L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False)]
            + wavy((54, 50), (64, 50), (60, 100), -4, z='f'),
    'back': [L(blob(SKULL_B))] + back_hair() + wavy((44, 6), (56, 6), (46, 120), -8, z='f') + [L(ell(50, 8, 6, 4), (200, 120, 40, 255), 'f', ln=True)],
}

# ------------------------------------------------------------------ Kim Powell / Gale... melena granate ondulada y abultada hasta
# los hombros, ojos azules afilados y labios marcados
CHARS['kim-powell'] = {
    'body': 'chica', 'pal': pal('#a82a4a', '#d89a6a', iris='#2a5aa8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': (58, 48)},
    'front': [L(bumpy(50, 54, 50, 46, 16, 0.06)), L(bumpy(70, 60, 22, 34, 8, 0.06), 'shade', 'b', False), L(ell(30, 18, 10, 4), 'light', 'b', False),
              wavy((14, 42), (34, 34), (16, 66), -5, z='f'), wavy((66, 34), (86, 42), (84, 66), 5, z='f', light_left=False)],
    'side': [L(bumpy(40, 54, 46, 46, 16, 0.06)), L(blob(SIDE_SKULL)), L(bumpy(22, 60, 18, 32, 8, 0.06), 'shade', 'b', False),
             spk((56, 30), (88, 40), (92, 64), 5, z='f', light_left=False)],
    'back': [L(bumpy(50, 56, 50, 48, 16, 0.06)), L(bumpy(68, 62, 22, 36, 8, 0.06), 'shade', 'b', False), L(ell(30, 18, 10, 4), 'light', 'b', False)],
}

# ------------------------------------------------------------------ Zack Cummings / Gojou... corpulento, piel morena, pelo naranja
# corto con una coleta pequeña atada detrás, ojos rojos y una mascarilla negra con rejilla sobre la boca
CHARS['zack-cummings'] = {
    'body': 'corpulento', 'pal': pal('#e08a2a', '#9a6a4a', iris='#c01a1a', mask='#3a3438', mask_d='#24202a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'face_front': WIDE_FACE, 'big_ears': 1, 'hairline': (54, 46)},
    'front': [L(blob(SKULL_F)), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'shade', 'b', False), sheen(28, 52, 14, 3),
              L(blob([(24, 80), (50, 76), (76, 80), (72, 100), (50, 106), (28, 100)]), 'mask', 'f', ln=True),
              L([(36, 88), (64, 88)], 'mask_d', 'f', False, False, 1.4), L([(38, 94), (62, 94)], 'mask_d', 'f', False, False, 1.4)],
    'side': [L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             L(blob([(18, 46), (6, 50), (-4, 74), (6, 74), (16, 58)]), 'mid', 'b', ln=True),
             L(blob([(70, 78), (98, 82), (98, 98), (80, 104), (66, 96)]), 'mask', 'f', ln=True)],
    'back': [L(blob(SKULL_B))] + back_hair() + [L(blob([(44, 70), (56, 70), (54, 96), (46, 96)]), 'mid', 'f', ln=True), L(ell(50, 70, 5, 3), (180, 30, 30, 255), 'f', ln=True)],
}

# ------------------------------------------------------------------ Hunt Mercer / Gocchi... corpulento, piel rosada, cara de cerdo
# con la nariz chata y morros, pelo castaño oscuro con un tupé en lo alto
CHARS['hunt-mercer'] = {
    'body': 'corpulento', 'pal': pal('#5a3020', '#e89080', nose='#d06a60'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'lips', 'mouth_y': 96, 'mouth_w': 10, 'face_front': WIDE_FACE, 'big_ears': 2, 'ear_out': 4,
             'nose': (50, 84, 5.6), 'nose_side': (94, 82, 5), 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin'), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'skin_d', 'b', False),
              L(blob([(26, 30), (40, 10), (60, 4), (78, 14), (70, 26), (56, 18), (44, 28)]), 'mid', 'b', ln=True),
              L(ell(47, 84, 1.2, 1.6), OUTC, 'f', False), L(ell(53, 84, 1.2, 1.6), OUTC, 'f', False)],
    'side': [L(blob(SIDE_SKULL), 'skin'), L(blob([(26, 24), (44, 4), (70, 2), (84, 14), (66, 18), (46, 22)]), 'mid', 'b', ln=True)],
    'back': [L(blob(SKULL_B), 'skin'), L(blob([(58, 12), (86, 36), (84, 68), (66, 84)], 6), 'skin_d', 'b', False),
             L(blob([(26, 30), (40, 10), (60, 4), (78, 14), (70, 26), (56, 18), (44, 28)]), 'mid', 'b', ln=True)],
}

# ------------------------------------------------------------------ Isabelle Trick / Ulvida: melena azul lisa muy larga con raya al
# lado y dos mechones blancos junto a la cara; ojos verde azulado
CHARS['isabelle-trick'] = {
    'body': 'chica', 'pal': pal('#2a7ab8', '#fcdcc0', iris='#2a8a8a', white='#ece8e4'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': [(10, 70), (24, 54), (44, 42), (60, 48), (76, 56), (90, 70)]},
    'front': [L(blob([(6, 124), (2, 60), (12, 18), (50, 4), (88, 18), (98, 60), (94, 124), (82, 118), (82, 66), (18, 66), (18, 118)])),
              L(blob([(62, 12), (96, 50), (92, 118), (84, 116)], 6), 'shade', 'b', False), sheen(22, 46, 18, 3),
              strand([(44, 8), (30, 48)], 'deep', 'b', 1.1),
              L(blob([(12, 56), (22, 58), (24, 104), (16, 118), (10, 90)]), 'white', 'f'), L(blob([(88, 56), (78, 58), (76, 104), (84, 118), (90, 90)]), 'white', 'f'),
              strand([(22, 60), (23, 104), (16, 116)], OUTC, 'f', 1.0), strand([(78, 60), (77, 104), (84, 116)], OUTC, 'f', 1.0),
              spk((10, 44), (30, 34), (16, 76), 5, z='f')],
    'side': [L(blob([(56, 122), (14, 124), (0, 66), (4, 28), (24, 8), (56, 4), (82, 14), (94, 34), (92, 56), (76, 54), (62, 58), (58, 78), (60, 110)])),
             L(blob([(4, 50), (8, 114), (46, 118), (24, 74)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             L(blob([(56, 56), (64, 58), (64, 104), (58, 112)]), 'white', 'f', ln=True), spk((56, 30), (90, 40), (92, 70), 5, z='f', light_left=False)],
    'back': [L(blob([(6, 124), (2, 60), (12, 18), (50, 4), (88, 18), (98, 60), (94, 124), (50, 130)])),
             L(blob([(58, 12), (96, 50), (92, 122), (66, 128)], 6), 'shade', 'b', False), sheen(22, 46, 18, 3)]
            + [strand([(x, 24), (x + (x - 50) * 0.1, 122)], 'deep', 'b', 1.0) for x in (30, 44, 56, 70)],
}

# ------------------------------------------------------------------ Connor Murray / Wheeze no: Gale... pelo castaño oliva liso hasta
# la mandíbula con las puntas claras, flequillo y ojos cerrados de concentración
CHARS['connor-murray'] = {
    'body': 'normal', 'pal': pal('#6a6420', '#fcd0a4', tips='#e8d880'),
    'face': {'eyes': 'closed', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (60, 52)},
    'front': [L(blob(BOB_F))] + bob_shade('front') + fringe(5, 36, 64)
             + [L(blob([(6, 70), (18, 70), (20, 84), (10, 84)]), 'tips', 'f', False), L(blob([(94, 70), (82, 70), (80, 84), (90, 84)]), 'tips', 'f', False),
                spk((4, 54), (12, 64), (-14, 58), 4), spk((88, 64), (96, 54), (114, 58), 4, light_left=False)],
    'side': [L(blob(BOB_S))] + bob_shade('side') + [spk((56, 30), (90, 40), (92, 70), 6, z='f', light_left=False)],
    'back': [L(blob(BOB_B))] + bob_shade('back'),
}

# ------------------------------------------------------------------ Katie Brown / Kii... pelo morado con dos moños redondos enormes
# a los lados, un dibujo rojo en la frente y coloretes; ojos redondos
CHARS['katie-brown'] = {
    'body': 'chica', 'pal': pal('#8a4a8a', '#fce4cc', iris='#c02a2a', paint='#c02a2a', blush='#f0a0a0'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'frown', 'mouth_y': 92, 'hairline': (60, 50)},
    'front': [L(bumpy(10, 18, 18, 16, 8, 0.06)), L(bumpy(90, 18, 18, 16, 8, 0.06)),
              L(bumpy(14, 14, 8, 6, 6, 0.06), 'light', 'b', False), L(bumpy(86, 14, 8, 6, 6, 0.06), 'light', 'b', False),
              L(blob(CAP_F)), L(blob([(62, 12), (90, 38), (88, 66), (78, 62)], 6), 'shade', 'b', False)] + fringe(4, 36, 58)
             + [L(quad((40, 62), (50, 56), (60, 62)), 'paint', 'f', False, False, 1.6), L([(50, 58), (50, 66)], 'paint', 'f', False, False, 1.4),
                L(ell(26, 86, 5, 3), 'blush', 'f', False), L(ell(74, 86, 5, 3), 'blush', 'f', False)],
    'side': [L(bumpy(36, 8, 18, 16, 8, 0.06))] + spiky_face('side', False) + [spk((56, 30), (88, 40), (92, 62), 5, z='f', light_left=False)],
    'back': [L(bumpy(10, 20, 18, 16, 8, 0.06)), L(bumpy(90, 20, 18, 16, 8, 0.06)), L(blob(SKULL_B))] + back_hair(),
}

# ------------------------------------------------------------------ Ashton Malone / Quill... casco blanco de auriculares, un visor
# rojo sobre los ojos y un mechón gris largo que le cae sobre la cara
CHARS['ashton-malone'] = {
    'body': 'normal', 'pal': pal('#b8b8bc', '#f6c08e', helm='#e8e4dc', helm_d='#a8a49c', visor='#c81a1a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 93, 'ears': False, 'hairline': False},
    'front': [L(blob([(8, 70), (6, 36), (20, 10), (50, 2), (80, 10), (94, 36), (92, 70), (80, 60), (20, 60)]), 'helm', 'f', ln=True),
              L(blob([(62, 8), (92, 34), (90, 66), (80, 60)], 6), 'helm_d', 'f', False),
              L(ell(10, 70, 8, 12), 'helm_d', 'f', ln=True), L(ell(90, 70, 8, 12), 'helm_d', 'f', ln=True),
              L(blob([(14, 66), (50, 60), (86, 66), (84, 80), (50, 78), (16, 80)]), 'visor', 'f', ln=True)]
             + wavy((60, 10), (72, 14), (16, 70), 10, z='f'),
    'side': [L(blob(SIDE_SKULL)), L(blob([(12, 68), (10, 32), (26, 8), (54, 2), (80, 10), (94, 32), (92, 60), (50, 60)]), 'helm', 'f', ln=True),
             L(ell(44, 70, 10, 13), 'helm_d', 'f', ln=True), L(blob([(70, 64), (96, 64), (96, 80), (72, 80)]), 'visor', 'f', ln=True)],
    'back': [L(blob([(8, 74), (6, 36), (20, 10), (50, 2), (80, 10), (94, 36), (92, 74), (50, 80)]), 'helm', 'f', ln=True),
             L(blob([(58, 8), (92, 34), (90, 72), (66, 78)], 6), 'helm_d', 'f', False),
             L(ell(10, 70, 8, 12), 'helm_d', 'f', ln=True), L(ell(90, 70, 8, 12), 'helm_d', 'f', ln=True)],
}

# ------------------------------------------------------------------ Wilbur Watkins / Wheeze: piel morena, pelo blanco azulado
# enorme de pinchos hacia atrás y a los lados, rayas blancas en la cara y ojos rojos
CHARS['wilbur-watkins'] = {
    'body': 'normal', 'pal': pal('#d8ecf4', '#9a6a44', iris='#c02a2a', shade='#a8c0cc', paint='#ece8e4'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (56, 48)},
    'front': spiky('front', 1.2) + spiky_face('front')
             + [L([(22, 82), (30, 88)], 'paint', 'f', False, False, 1.6), L([(78, 82), (70, 88)], 'paint', 'f', False, False, 1.6),
                spk((4, 58), (12, 74), (-12, 92), 4), spk((88, 74), (96, 58), (112, 92), 4, light_left=False)],
    'side': spiky('side', 1.3) + spiky_face('side') + [L([(78, 82), (86, 88)], 'paint', 'f', False, False, 1.6)],
    'back': spiky('back', 1.2),
}

# ------------------------------------------------------------------ Xavier Foster / Gran (capitán): pelo rojo con mucho volumen en
# lo alto (mechones gruesos que se curvan hacia arriba y atrás) y mechones que le caen sobre la cara; ojos verdes
GRAN_F = [spk((6, 50), (12, 28), (-14, 12), 9), spk((14, 22), (34, 4), (8, -24), 10), spk((34, 4), (56, -2), (40, -34), 10),
          spk((54, -2), (76, 6), (78, -30), 10, light_left=False), spk((76, 10), (92, 30), (112, 0), 9, light_left=False),
          spk((90, 34), (96, 54), (116, 42), 7, light_left=False)]
CHARS['xavier-foster'] = {
    'body': 'normal', 'pal': pal('#d8181a', '#f6dcc4', iris='#2a9a6a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'hairline': (60, 52)},
    'front': GRAN_F + [L(bumpy(50, 24, 42, 30, 10, 0.1)), L(blob(CAP_F)), L(bumpy(70, 30, 18, 22, 6, 0.1), 'shade', 'b', False),
                       L(blob([(62, 12), (90, 38), (88, 66), (78, 62)], 6), 'shade', 'b', False)]
             + [spk((12, 44), (32, 36), (18, 76), 7, z='f'), spk((32, 36), (52, 32), (46, 72), 7, z='f'),
                spk((52, 32), (72, 36), (62, 66), 7, z='f', light_left=False), spk((72, 38), (90, 46), (86, 74), 6, z='f', light_left=False)],
    'side': [spk((20, 30), (38, 10), (-4, -14), 10), spk((38, 8), (60, 2), (44, -32), 10), spk((60, 4), (78, 12), (88, -20), 9, light_left=False),
             spk((14, 52), (18, 30), (-18, 30), 9), L(bumpy(44, 26, 40, 28, 10, 0.1)),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((56, 30), (88, 40), (94, 70), 7, z='f', light_left=False)],
    'back': GRAN_F + [L(bumpy(50, 30, 42, 34, 10, 0.1)), L(blob(CAP_B)), L(blob([(58, 12), (90, 38), (88, 72), (66, 86)], 6), 'shade', 'b', False),
                      spk((14, 74), (32, 86), (10, 100), 7), spk((32, 88), (52, 92), (42, 106), 7), spk((52, 92), (72, 88), (64, 106), 7, light_left=False),
                      spk((72, 86), (88, 74), (92, 100), 7, light_left=False)],
}
