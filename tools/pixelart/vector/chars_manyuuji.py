"""Manyuuji / Instituto Claustro Sagrado (IE2): los monjes; cabezas rapadas, una cesta en la cabeza, moños, caras
pintadas y máscaras, con sus modelos 3D como referencia."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, pal, sheen, spk, strand
from chars_alius import SIDE_SKULL, SKULL_B, SKULL_F, LONG_FACE, spiky, spiky_face
from chars_otaku import back_hair, glasses, side_glass
from chars_sengoku import wavy
from chars_umbrella import BOB_B, BOB_F, BOB_S, bob_shade, fringe
from heads import quad

DARK = (24, 20, 24, 255)


def bald(view):
    if view == 'front':
        return [L(blob(SKULL_F), 'skin'), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'skin_d', 'b', False)]
    if view == 'side':
        return [L(blob(SIDE_SKULL), 'skin')]
    return [L(blob(SKULL_B), 'skin'), L(blob([(58, 12), (86, 36), (84, 68), (66, 84)], 6), 'skin_d', 'b', False)]


def same(f, s, b):
    return {'front': f, 'side': s, 'back': b}


# Crane Kik (portero): cara alargada de adulto, pañuelo naranja atado a la cabeza con el nudo detrás, ojos entornados
CHARS['crane-kik'] = {
    'body': 'normal', 'pal': pal('#2a2a2a', '#c8905a', wrap='#d8701a', wrap_d='#a8500e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'face_front': LONG_FACE, 'big_ears': 1, 'nose': (50, 86, 3), 'hairline': False},
    'front': bald('front') + [L(blob([(12, 50), (10, 26), (24, 8), (50, 2), (76, 8), (90, 26), (88, 50), (50, 46)]), 'wrap', 'f', ln=True),
                              L(blob([(60, 6), (88, 26), (88, 48), (70, 46)], 6), 'wrap_d', 'f', False)],
    'side': bald('side') + [L(blob([(12, 52), (10, 24), (28, 6), (56, 0), (82, 10), (92, 30), (92, 48), (50, 46)]), 'wrap', 'f', ln=True),
                            L(blob([(14, 40), (0, 34), (-8, 48), (6, 50)], 4), 'wrap', 'f', ln=True)],
    'back': bald('back') + [L(blob([(12, 54), (10, 26), (24, 8), (50, 2), (76, 8), (90, 26), (88, 54), (50, 58)]), 'wrap', 'f', ln=True),
                            L(blob([(50, 54), (32, 48), (26, 60), (40, 62)], 4), 'wrap_d', 'f', ln=True), L(blob([(50, 54), (68, 48), (74, 60), (60, 62)], 4), 'wrap_d', 'f', ln=True)],
}
# Parry Waxon: rapado, una diadema fina con una joya roja en la frente y ojos cerrados
CHARS['parry-waxon'] = {
    'body': 'normal', 'pal': pal('#2a2a2a', '#fce4b8', gem='#c0302a', band='#8a7060'),
    'face': {'eyes': 'closed', 'brows': True, 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    'front': bald('front') + [L(quad((14, 46), (50, 36), (86, 46)), 'band', 'f', False, False, 1.6), L(ell(50, 42, 3, 3.6), 'gem', 'f', ln=True)],
    'side': bald('side') + [L(quad((14, 48), (50, 36), (90, 42)), 'band', 'f', False, False, 1.6)],
    'back': bald('back') + [L(quad((14, 50), (50, 44), (86, 50)), 'band', 'f', False, False, 1.6)],
}
# Bri Spark: rapado, coloretes y ceño
CHARS['bri-spark'] = {
    'body': 'normal', 'pal': pal('#2a2a2a', '#fce4b8', blush='#f0a070'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': False},
    'front': bald('front') + [L(ell(24, 84, 4, 2.6), 'blush', 'f', False), L(ell(76, 84, 4, 2.6), 'blush', 'f', False)],
    'side': bald('side') + [L(ell(80, 84, 3.6, 2.4), 'blush', 'f', False)], 'back': bald('back'),
}
# Max Fortune: rapado con una cicatriz grande en la frente, orejas enormes y ceño
CHARS['max-fortune'] = {
    'body': 'normal', 'pal': pal('#2a2a2a', '#f8c8a0', scar='#b06a3a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'big_ears': 3, 'ear_out': 4, 'hairline': False},
    'front': bald('front') + [L([(30, 30), (40, 36), (36, 44), (48, 50), (44, 58)], 'scar', 'f', False, False, 1.6)],
    'side': bald('side') + [L([(70, 30), (78, 38), (76, 46)], 'scar', 'f', False, False, 1.6)],
    'back': bald('back') + [L([(30, 30), (40, 36), (36, 44)], 'scar', 'f', False, False, 1.6)],
}
# Brendan Water: piel tostada, gorro de tela crema calado y una venda negra sobre los ojos con unas gafitas pequeñas
CHARS['brendan-water'] = {
    'body': 'normal', 'pal': pal('#2a2a2a', '#f0c070', hat='#e4dcc4', hat_d='#b8ae98'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 94, 'face_front': LONG_FACE, 'hairline': False},
    'front': bald('front') + [L(blob([(14, 52), (12, 26), (26, 8), (50, 2), (74, 8), (88, 26), (86, 52), (50, 50)]), 'hat', 'f', ln=True),
                              L(blob([(60, 6), (86, 26), (86, 50), (70, 48)], 6), 'hat_d', 'f', False),
                              L(quad((14, 66), (50, 62), (86, 66)) + quad((86, 78), (50, 74), (14, 78)), DARK, 'f', ln=True)] + glasses(70, 4, 3, (200, 200, 200, 255)),
    'side': bald('side') + [L(blob([(12, 54), (10, 26), (28, 6), (56, 0), (82, 10), (92, 30), (92, 50), (50, 50)]), 'hat', 'f', ln=True),
                            L(quad((14, 66), (50, 62), (96, 66)) + quad((96, 78), (50, 74), (14, 78)), DARK, 'f', ln=True)],
    'back': bald('back') + [L(blob([(14, 56), (12, 26), (26, 8), (50, 2), (74, 8), (88, 26), (86, 56), (50, 58)]), 'hat', 'f', ln=True),
                            L(quad((14, 70), (50, 66), (86, 70)) + quad((86, 80), (50, 76), (14, 80)), DARK, 'f', ln=True)],
}
# Junior Fardream: la cabeza metida en una cesta de mimbre (komusō) con una rendija para ver
BASKET = [(4, 96), (2, 20), (12, 0), (50, -6), (88, 0), (98, 20), (96, 96), (50, 102)]
CHARS['junior-fardream'] = {
    'body': 'normal', 'pal': pal('#2a2a2a', '#f6c08e', wick='#d8a040', wick_d='#a07020'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'ears': False, 'hairline': False},
    'front': [L(blob(BASKET, 6), 'wick', 'f', ln=True), L(blob([(62, -2), (96, 20), (94, 94), (74, 98)], 6), 'wick_d', 'f', False)]
             + [L(quad((4, y), (50, y + 4), (96, y)), 'wick_d', 'f', False, False, 1.2) for y in (10, 26, 42, 58, 74, 90)]
             + [L([(x, 0), (x, 98)], 'wick_d', 'f', False, False, 0.8) for x in (20, 35, 50, 65, 80)]
             + [L([(30, 54), (70, 54), (70, 66), (30, 66)], DARK, 'f', False)],
    'side': [L(blob([(8, 96), (0, 20), (16, -2), (60, -6), (92, 4), (104, 24), (100, 96), (54, 102)], 6), 'wick', 'f', ln=True)]
            + [L(quad((2, y), (50, y + 4), (102, y)), 'wick_d', 'f', False, False, 1.2) for y in (10, 26, 42, 58, 74, 90)]
            + [L([(84, 54), (100, 54), (100, 66), (84, 66)], DARK, 'f', False)],
    'back': [L(blob(BASKET, 6), 'wick', 'f', ln=True), L(blob([(58, -2), (96, 20), (94, 94), (66, 100)], 6), 'wick_d', 'f', False)]
            + [L(quad((4, y), (50, y + 4), (96, y)), 'wick_d', 'f', False, False, 1.2) for y in (10, 26, 42, 58, 74, 90)],
}
# Ian Telektual: piel amarilla, pelo gris verdoso corto con un moño negro despeinado en lo alto, gafas y nariz larga
CHARS['ian-telektual'] = {
    'body': 'delgado', 'pal': pal('#3e5a54', '#f0c860', knot='#24242a', nose='#e0b050'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 98, 'face_front': LONG_FACE, 'big_ears': 1, 'nose': (50, 86, 4), 'nose_side': (94, 84, 4.4),
             'glasses': (200, 200, 200, 255), 'hairline': (52, 42)},
    'front': wavy((40, 6), (50, 4), (4, -10), -6) + wavy((50, 4), (60, 6), (96, -10), 6, light_left=False)
             + [L(ell(50, 4, 8, 6), 'knot', 'b', ln=True), L(blob(SKULL_F)), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'shade', 'b', False)],
    'side': wavy((40, 6), (52, 4), (8, -6), -6) + [L(ell(46, 4, 8, 6), 'knot', 'b', ln=True), L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False)],
    'back': wavy((40, 6), (50, 4), (4, -10), -6) + wavy((50, 4), (60, 6), (96, -10), 6, light_left=False) + [L(ell(50, 4, 8, 6), 'knot', 'b', ln=True), L(blob(SKULL_B))] + back_hair(),
}
# Lee Dinglite: pelo negro verdoso despeinado que cae a los lados, cara alargada pintada (rayas rojas en los párpados)
CHARS['lee-dinglite'] = {
    'body': 'normal', 'pal': pal('#1e2a1e', '#d8a060', paint='#c03a2a'),
    'face': {'eyes': 'closed', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 98, 'face_front': LONG_FACE, 'hairline': (60, 50)},
    'front': [L(blob(BOB_F))] + bob_shade('front') + fringe(4, 36, 62)
             + [spk((2, 52), (10, 40), (-12, 42), 4), spk((90, 40), (98, 52), (112, 42), 4, light_left=False),
                L(quad((26, 74), (36, 70), (44, 74)), 'paint', 'f', False, False, 1.6), L(quad((56, 74), (64, 70), (74, 74)), 'paint', 'f', False, False, 1.6)],
    'side': [L(blob(BOB_S))] + bob_shade('side') + [spk((56, 30), (88, 40), (92, 70), 6, z='f', light_left=False), spk((14, 30), (22, 14), (2, 0), 5)],
    'back': [L(blob(BOB_B))] + bob_shade('back') + [spk((14, 84), (32, 90), (16, 100), 4), spk((68, 90), (86, 84), (84, 100), 4, light_left=False)],
}
# Marshall Artz: rapado con un moño castaño de punta en lo alto, máscara roja sobre la boca, espirales pintadas en la frente y dos
# trenzas finas detrás de las orejas
CHARS['marshall-artz'] = {
    'body': 'normal', 'pal': pal('#6a3420', '#f6c890', mask='#c03a40', paint='#c87a2a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': [spk((40, 10), (60, 10), (40, -24), 7)] + bald('front')
             + [L(blob([(16, 52), (14, 36), (50, 26), (86, 36), (84, 52), (50, 46)]), 'mid', 'f', ln=True),
                L(blob([(26, 82), (50, 78), (74, 82), (70, 100), (50, 104), (30, 100)]), 'mask', 'f', ln=True),
                L(blob([(36, 56), (42, 52), (46, 58), (40, 62), (38, 58)], 5), 'paint', 'f', False, False, 1.4),
                L(blob([(64, 56), (58, 52), (54, 58), (60, 62), (62, 58)], 5), 'paint', 'f', False, False, 1.4),
                L(quad((14, 66), (8, 86), (12, 104)), 'mid', 'f', False, False, 2.4), L(quad((86, 66), (92, 86), (88, 104)), 'mid', 'f', False, False, 2.4)],
    'side': [spk((34, 10), (54, 6), (30, -24), 7)] + bald('side') + [L(blob([(14, 50), (16, 30), (50, 20), (86, 30), (88, 44), (50, 40)]), 'mid', 'f', ln=True),
             L(blob([(76, 82), (96, 84), (96, 100), (80, 102)]), 'mask', 'f', ln=True), L(quad((40, 66), (36, 86), (40, 104)), 'mid', 'f', False, False, 2.4)],
    'back': [spk((40, 10), (60, 10), (40, -24), 7)] + bald('back') + [L(blob([(16, 52), (14, 34), (50, 24), (86, 34), (84, 52), (50, 48)]), 'mid', 'f', ln=True),
             L(quad((24, 66), (20, 86), (24, 104)), 'mid', 'f', False, False, 2.4), L(quad((76, 66), (80, 86), (76, 104)), 'mid', 'f', False, False, 2.4)],
}
# Tyke Wando: pelo verde oscuro en casco con un mechón alto curvado arriba, dos trenzas largas a los lados y un punto rojo en la frente
CHARS['tyke-wando'] = {
    'body': 'bajito', 'pal': pal('#2e4a2a', '#f8c48c', dot='#c0302a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (58, 50)},
    'front': wavy((44, 10), (56, 10), (74, -24), -8, light_left=False) + [L(blob(SKULL_F)), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'shade', 'b', False),
             L(quad((16, 62), (4, 80), (-4, 100)), 'mid', 'f', False, False, 3), L(quad((84, 62), (96, 80), (104, 100)), 'mid', 'f', False, False, 3),
             L(ell(50, 56, 2, 2), 'dot', 'f', False)] + fringe(4, 34, 52),
    'side': wavy((40, 8), (52, 6), (72, -24), -8, light_left=False) + [L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             L(quad((30, 64), (16, 82), (6, 100)), 'mid', 'f', False, False, 3)],
    'back': wavy((44, 10), (56, 10), (74, -24), -8, light_left=False) + [L(blob(SKULL_B))] + back_hair()
            + [L(quad((20, 62), (6, 80), (-2, 100)), 'mid', 'f', False, False, 3), L(quad((80, 62), (94, 80), (102, 100)), 'mid', 'f', False, False, 3)],
}
# Dirk Artz: rapado con una coleta negra alta y mechones largos a los lados, máscara azul sobre la boca y espirales pintadas
CHARS['dirk-artz'] = {
    'body': 'normal', 'pal': pal('#1e2a3a', '#fce4b8', mask='#2a5aa0', paint='#2a2a2a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': wavy((44, 10), (56, 10), (88, -16), -6, light_left=False) + bald('front')
             + [L(blob([(14, 50), (14, 34), (50, 26), (86, 34), (86, 50), (50, 46)]), 'mid', 'f', ln=True),
                L(blob([(12, 50), (20, 50), (22, 100), (12, 100)]), 'mid', 'f', ln=True), L(blob([(88, 50), (80, 50), (78, 100), (88, 100)]), 'mid', 'f', ln=True),
                L(blob([(26, 82), (50, 78), (74, 82), (70, 100), (50, 104), (30, 100)]), 'mask', 'f', ln=True),
                L(blob([(36, 56), (42, 52), (46, 58), (40, 62), (38, 58)], 5), 'paint', 'f', False, False, 1.2),
                L(blob([(64, 56), (58, 52), (54, 58), (60, 62), (62, 58)], 5), 'paint', 'f', False, False, 1.2)],
    'side': wavy((36, 10), (50, 6), (6, -14), 8) + bald('side') + [L(blob([(14, 50), (16, 30), (50, 20), (86, 30), (88, 44), (50, 40)]), 'mid', 'f', ln=True),
             L(blob([(36, 50), (46, 50), (48, 100), (38, 100)]), 'mid', 'f', ln=True), L(blob([(76, 82), (96, 84), (96, 100), (80, 102)]), 'mask', 'f', ln=True)],
    'back': wavy((44, 10), (56, 10), (88, -16), -6, light_left=False) + bald('back')
            + [L(blob([(14, 56), (14, 32), (50, 24), (86, 32), (86, 56), (50, 52)]), 'mid', 'f', ln=True),
               L(blob([(12, 56), (22, 56), (22, 100), (12, 100)]), 'mid', 'f', ln=True), L(blob([(88, 56), (78, 56), (78, 100), (88, 100)]), 'mid', 'f', ln=True)],
}
# Earnest Bookworm: piel tostada, pelo muy corto (sombra de rapado) con un punto en la frente y ojos cerrados sonrientes
CHARS['earnest-bookworm'] = {
    'body': 'normal', 'pal': pal('#6a5040', '#d8a068'),
    'face': {'eyes': 'closed', 'brows': True, 'mouth': 'smile', 'mouth_y': 94, 'face_front': LONG_FACE, 'big_ears': 1, 'hairline': (48, 40)},
    'front': [L(blob(SKULL_F)), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'shade', 'b', False), L(ell(50, 56, 1.6, 1.6), DARK, 'f', False)],
    'side': [L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False)],
    'back': [L(blob(SKULL_B))] + back_hair(),
}
# Ollie Gami: rapado con una cresta corta naranja en lo alto, nariz larga y ceño
CHARS['ollie-gami'] = {
    'body': 'normal', 'pal': pal('#e07a2a', '#e0a070', nose='#c88050'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'nose': (50, 84, 3.4), 'nose_side': (92, 82, 3.6), 'hairline': False},
    'front': bald('front') + [L(blob([(42, 10), (44, -2), (50, -6), (56, -2), (58, 10), (56, 40), (44, 40)]), 'mid', 'b', ln=True)],
    'side': bald('side') + [L(blob([(24, 30), (30, 10), (50, 0), (74, 4), (70, 10), (48, 10), (32, 30)]), 'mid', 'b', ln=True)],
    'back': bald('back') + [L(blob([(42, 10), (44, -2), (50, -6), (56, -2), (58, 10), (56, 60), (44, 60)]), 'mid', 'b', ln=True)],
}
# Roman Kandel: piel morena, rapado con un moño blanco en espiral de punta en lo alto, ojos redondos
CHARS['roman-kandel'] = {
    'body': 'normal', 'pal': pal('#e8dcd0', '#b0703e', shade='#b8a8a0'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'big_ears': 1, 'ear_out': 3, 'hairline': False},
    'front': [L(blob([(34, 14), (40, -4), (50, -22), (60, -4), (66, 14)]), 'mid', 'b', ln=True),
              L(quad((38, 4), (50, -2), (62, 4)), 'shade', 'b', False, False, 1.2), L(quad((42, -6), (50, -10), (58, -6)), 'shade', 'b', False, False, 1.2)] + bald('front'),
    'side': [L(blob([(30, 14), (36, -4), (48, -22), (60, -4), (62, 14)]), 'mid', 'b', ln=True)] + bald('side'),
    'back': [L(blob([(34, 14), (40, -4), (50, -22), (60, -4), (66, 14)]), 'mid', 'b', ln=True)] + bald('back'),
}
# Don Ation: corte de tazón castaño oscuro con flequillo recto, ojos redondos y ceño
CHARS['don-ation'] = {
    'body': 'normal', 'pal': pal('#3a2a20', '#f8c08a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': False},
    'front': [L(blob(BOB_F))] + bob_shade('front')
             + [L(blob([(12, 60), (10, 40), (24, 22), (50, 16), (76, 22), (90, 40), (88, 60), (50, 58)]), 'mid', 'f', ln=True),
                L(blob([(60, 22), (86, 40), (86, 58), (70, 58)], 6), 'shade', 'f', False)]
             + [strand([(x, 30 + abs(x - 50) * 0.2), (x, 58)], 'deep', 'f', 0.9) for x in (28, 40, 52, 64, 76)],
    'side': [L(blob(BOB_S))] + bob_shade('side') + [strand([(70, 40), (70, 58)], 'deep', 'b', 1.0)],
    'back': [L(blob(BOB_B))] + bob_shade('back') + [strand([(x, 50), (x, 86)], 'deep', 'b', 1.0) for x in (24, 37, 50, 63, 76)],
}
