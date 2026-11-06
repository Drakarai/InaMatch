"""Hakuren / Instituto Alpino (IE2): el equipo de la nieve de Shawn; gorros, orejeras, capuchas, bufandas y gafas de
esquí, con sus modelos 3D como referencia."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, pal, sheen, spk, strand
from chars_alius import CAP_B, CAP_F, SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE, LONG_FACE, spiky, spiky_face
from chars_otaku import back_hair
from chars_umbrella import BOB_B, BOB_F, BOB_S, bob_shade, fringe
from heads import quad

WHITE = (255, 255, 255, 255)
DARK = (24, 20, 24, 255)


def beanie(view, c='hat', cd='hat_d', y=58, top=-2):
    """Gorro de lana calado hasta y, con su vuelta."""
    if view == 'side':
        return [L(blob([(10, y + 2), (8, 26), (26, top + 4), (56, top), (82, top + 8), (94, 28), (94, y), (50, y - 2)]), c, 'f', ln=True),
                L(quad((10, y - 10), (50, y - 14), (94, y - 10)) + quad((94, y), (50, y - 4), (10, y + 2)), cd, 'f', ln=True)]
    return [L(blob([(8, y + 2), (6, 28), (20, top + 6), (50, top), (80, top + 6), (94, 28), (92, y + 2), (50, y - 2)]), c, 'f', ln=True),
            L(blob([(60, top + 4), (92, 26), (92, y), (72, y - 2)], 6), cd, 'f', False),
            L(quad((8, y - 10), (50, y - 16), (92, y - 10)) + quad((92, y + 2), (50, y - 4), (8, y + 2)), cd, 'f', ln=True)]


# ------------------------------------------------------------------ Adam Ropes (portero): corpulento, gorro verde oliva con la vuelta
# blanca, patillas oscuras, cara alargada y boca torcida
CHARS['adam-ropes'] = {
    'body': 'corpulento', 'pal': pal('#3a2a20', '#f0b060', hat='#4e5a1e', hat_d='#e8e4dc'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'face_front': LONG_FACE, 'nose': (50, 84, 2.6), 'hairline': False},
    'front': [L(blob([(12, 58), (22, 58), (24, 86), (14, 84)])), L(blob([(88, 58), (78, 58), (76, 86), (86, 84)]))] + beanie('front', y=56),
    'side': [L(blob(SIDE_SKULL)), L(blob([(40, 56), (52, 56), (54, 84), (44, 82)]))] + beanie('side', y=56),
    'back': [L(blob(SKULL_B))] + back_hair() + beanie('back', y=62),
}

# ------------------------------------------------------------------ Joaquine Downtown: gorro blanco de pelo abultado (como de piel)
# con una cola a un lado, flequillo rubio verdoso y coloretes
CHARS['joaquine-downtown'] = {
    'body': 'normal', 'pal': pal('#8a8a30', '#fcdcc4', hat='#ece8e4', hat_d='#c0b4b4', blush='#e8a0a0'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    'front': [L(blob([(10, 80), (8, 56), (92, 56), (90, 80), (80, 76), (20, 76)])),
              spk((12, 56), (28, 56), (18, 76), 4, z='f'), spk((28, 56), (44, 56), (36, 70), 4, z='f'),
              spk((56, 56), (72, 56), (64, 70), 4, z='f', light_left=False), spk((72, 56), (88, 56), (84, 76), 4, z='f', light_left=False),
              L(bumpy(46, 28, 42, 26, 12, 0.07), 'hat', 'f', ln=True), L(bumpy(62, 32, 22, 18, 8, 0.07), 'hat_d', 'f', False),
              L(blob([(80, 30), (100, 40), (104, 70), (92, 74), (86, 50)]), 'hat', 'f', ln=True), L(blob([(94, 56), (104, 70), (92, 74)], 4), (40, 30, 30, 255), 'f', False),
              L(ell(26, 86, 5, 3), 'blush', 'f', False), L(ell(74, 86, 5, 3), 'blush', 'f', False)],
    'side': [L(blob(BOB_S))] + bob_shade('side') + [L(bumpy(46, 28, 44, 26, 12, 0.07), 'hat', 'f', ln=True),
             L(blob([(10, 30), (-6, 44), (-8, 70), (4, 70), (12, 50)]), 'hat', 'f', ln=True)],
    'back': [L(blob([(10, 86), (8, 56), (92, 56), (90, 86), (50, 92)])), spk((14, 82), (32, 88), (16, 98), 4), spk((32, 88), (50, 90), (40, 100), 4),
             spk((50, 90), (68, 88), (60, 100), 4, light_left=False), spk((68, 88), (86, 82), (84, 98), 4, light_left=False),
             L(bumpy(50, 30, 44, 28, 12, 0.07), 'hat', 'f', ln=True), L(blob([(4, 30), (-12, 44), (-14, 72), (-2, 74), (6, 50)]), 'hat', 'f', ln=True)],
}

# ------------------------------------------------------------------ Milton Bindings: gorro naranja enorme con orejeras crema y
# pompones colgando, flequillo verde oscuro, ojos redondos y nariz roja de frío
CHARS['milton-bindings'] = {
    'body': 'normal', 'pal': pal('#1e4a3a', '#fcd0a8', hat='#e8800a', hat_d='#c0600a', flap='#e8dcc4', flap_d='#c0b49c', nose='#e07a5a'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'line', 'mouth_y': 93, 'ears': False, 'nose': (50, 82, 3), 'hairline': False},
    'front': [L(bumpy(50, 22, 54, 26, 12, 0.05), 'hat', 'f', ln=True), L(bumpy(70, 26, 26, 18, 8, 0.05), 'hat_d', 'f', False),
              L(blob([(14, 46), (24, 24), (50, 18), (76, 24), (86, 46), (90, 90), (80, 92), (78, 60), (22, 60), (20, 92), (10, 90)]), 'flap', 'f', ln=True),
              L(blob([(40, 6), (60, 6), (58, 26), (42, 26)]), 'flap', 'f', False),
              L(blob([(22, 46), (40, 40), (60, 40), (78, 46), (78, 60), (22, 60)]), 'mid', 'f', ln=True),
              L(ell(16, 100, 6, 6), 'flap_d', 'f', ln=True), L(ell(84, 100, 6, 6), 'flap_d', 'f', ln=True)],
    'side': [L(blob(SIDE_SKULL)), L(bumpy(42, 24, 50, 26, 12, 0.05), 'hat', 'f', ln=True),
             L(blob([(14, 46), (30, 26), (60, 22), (88, 40), (92, 58), (66, 56), (56, 92), (46, 94), (40, 60), (16, 60)]), 'flap', 'f', ln=True),
             L(ell(50, 100, 6, 6), 'flap_d', 'f', ln=True), spk((68, 44), (92, 48), (92, 62), 3, z='f', light_left=False)],
    'back': [L(blob(SKULL_B)), L(bumpy(50, 24, 54, 28, 12, 0.05), 'hat', 'f', ln=True), L(bumpy(68, 30, 26, 20, 8, 0.05), 'hat_d', 'f', False),
             L(blob([(14, 46), (24, 24), (50, 18), (76, 24), (86, 46), (86, 70), (14, 70)]), 'flap', 'f', ln=True),
             L(blob([(42, 10), (58, 10), (56, 70), (44, 70)]), 'flap_d', 'f', False),
             L(quad((20, 70), (16, 86), (16, 96)), 'flap_d', 'f', False, False, 1.6), L(quad((80, 70), (84, 86), (84, 96)), 'flap_d', 'f', False, False, 1.6)],
}

# ------------------------------------------------------------------ Spike Gleeson: gorro de lana gris con pompón colgando, pelo
# castaño rojizo de puntas hacia fuera y una franja oscura sobre los ojos (gafas)
CHARS['spike-gleeson'] = {
    'body': 'normal', 'pal': pal('#6a3428', '#fcc890', hat='#c8c8d0', hat_d='#9a9aa4'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    'front': [L(blob([(10, 80), (8, 54), (92, 54), (90, 80), (80, 72), (20, 72)])),
              spk((2, 60), (12, 76), (-14, 76), 5), spk((88, 76), (98, 60), (114, 76), 5, light_left=False),
              L(quad((14, 70), (50, 66), (86, 70)) + quad((86, 80), (50, 76), (14, 80)), DARK, 'f', ln=True),
              L(quad((40, -2), (60, -20), (80, -14)), 'hat_d', 'f', False, False, 1.6), L(ell(84, -12, 7, 6), 'hat', 'f', ln=True)]
             + beanie('front', y=62, top=-4),
    'side': [L(blob(BOB_S)), spk((2, 64), (10, 82), (-14, 82), 5)] + bob_shade('side') + beanie('side', y=62, top=-4)
            + [L(quad((40, -2), (20, -20), (2, -12)), 'hat_d', 'f', False, False, 1.6), L(ell(0, -10, 7, 6), 'hat', 'f', ln=True),
               L([(64, 70), (96, 70), (96, 80), (66, 80)], DARK, 'f', ln=True)],
    'back': [L(blob(BOB_B)), spk((2, 60), (12, 76), (-14, 76), 5), spk((88, 76), (98, 60), (114, 76), 5, light_left=False),
             spk((14, 84), (32, 90), (16, 100), 4), spk((68, 90), (86, 84), (84, 100), 4, light_left=False)] + beanie('back', y=64, top=-4)
            + [L(quad((40, -2), (20, -20), (6, -14)), 'hat_d', 'f', False, False, 1.6), L(ell(6, -12, 7, 6), 'hat', 'f', ln=True)],
}

# ------------------------------------------------------------------ Martin Ursus: piel tostada, pelo verde oliva en un tupé alto y
# plano como un bloque, patillas largas, cara alargada y gesto furioso
CHARS['martin-ursus'] = {
    'body': 'normal', 'pal': pal('#3e4224', '#c88a54'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'face_front': LONG_FACE, 'big_ears': 1, 'nose': (50, 86, 3), 'hairline': (50, 44)},
    'front': [L(blob([(14, 62), (12, 20), (20, -6), (50, -12), (80, -6), (88, 20), (86, 62)])),
              L(blob([(62, -8), (86, 18), (84, 60), (72, 56)], 6), 'shade', 'b', False), L(ell(46, -2, 6, 4), 'shade', 'b', ln=True),
              L(blob([(12, 56), (20, 56), (22, 96), (14, 96)]), 'mid', 'f'), L(blob([(88, 56), (80, 56), (78, 96), (86, 96)]), 'mid', 'f')],
    'side': [L(blob([(44, 70), (20, 68), (10, 40), (14, 4), (36, -12), (66, -10), (88, 0), (92, 22), (78, 32), (60, 36), (52, 50)])),
             L(blob([(14, 30), (20, 64), (38, 68), (28, 44)], 6), 'shade', 'b', False), L(blob([(40, 56), (50, 56), (52, 96), (44, 96)]), 'mid', 'f')],
    'back': [L(blob([(14, 74), (12, 20), (20, -6), (50, -12), (80, -6), (88, 20), (86, 74), (66, 86), (34, 86)])),
             L(blob([(58, -8), (86, 18), (84, 72), (66, 84)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Gem Strata: corpulento, piel morena, pelo azul grisáceo oscuro
# con dos bultos a los lados (como un yunque), bigote y una banda de tela sobre la boca
CHARS['gem-strata'] = {
    'body': 'corpulento', 'pal': pal('#2e3a44', '#a87040', cloth='#6a4a30'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'face_front': WIDE_FACE, 'hairline': (52, 44)},
    'front': [L(blob([(0, 40), (-6, 20), (14, 10), (30, 2), (50, 0), (70, 2), (86, 10), (106, 20), (100, 40), (86, 34), (86, 58), (14, 58), (14, 34)])),
              L(blob([(60, 4), (100, 22), (96, 38), (84, 32), (84, 56), (72, 54)], 6), 'shade', 'b', False),
              L(blob([(20, 86), (50, 84), (80, 86), (80, 98), (50, 100), (20, 98)]), 'cloth', 'f', ln=True)],
    'side': [L(blob([(44, 74), (20, 72), (8, 44), (8, 14), (30, -2), (64, -2), (86, 10), (90, 30), (76, 38), (60, 40), (52, 54)])),
             L(blob([(12, 30), (18, 66), (38, 72), (26, 44)], 6), 'shade', 'b', False),
             L(blob([(70, 84), (98, 86), (98, 100), (72, 100)]), 'cloth', 'f', ln=True)],
    'back': [L(blob([(0, 40), (-6, 20), (14, 10), (30, 2), (50, 0), (70, 2), (86, 10), (106, 20), (100, 40), (86, 34), (86, 70), (66, 82), (34, 82), (14, 70), (14, 34)])),
             L(blob([(58, 4), (100, 22), (96, 38), (84, 32), (84, 68), (66, 80)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Sean Snowfield: corpulento, capucha roja que le cubre la cabeza
# entera y una bufanda roja; cara redonda con coloretes y ojos cerrados
CHARS['sean-snowfield'] = {
    'body': 'corpulento', 'pal': pal('#c84a4a', '#fcc490', hood='#d05a5a', hood_d='#a03a3a', blush='#f0904a'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'line', 'mouth_y': 92, 'face_front': WIDE_FACE, 'ears': False, 'hairline': False},
    'front': [L(blob([(4, 100), (2, 50), (12, 14), (50, 0), (88, 14), (98, 50), (96, 100), (84, 90), (84, 56), (16, 56), (16, 90)]), 'hood', 'f', ln=True),
              L(blob([(62, 6), (96, 46), (94, 96), (86, 88)], 6), 'hood_d', 'f', False),
              L(blob([(10, 96), (50, 104), (90, 96), (92, 112), (50, 118), (8, 112)]), 'hood_d', 'f', ln=True),
              L(ell(26, 84, 6, 4), 'blush', 'f', False), L(ell(74, 84, 6, 4), 'blush', 'f', False)],
    'side': [L(blob(SIDE_SKULL)), L(blob([(6, 104), (0, 56), (8, 20), (34, 0), (66, 0), (88, 14), (96, 50), (84, 58), (66, 56), (58, 76), (60, 100)]), 'hood', 'f', ln=True),
             L(blob([(30, 98), (92, 100), (92, 114), (28, 112)]), 'hood_d', 'f', ln=True), L(ell(82, 84, 5, 4), 'blush', 'f', False)],
    'back': [L(blob([(4, 104), (2, 50), (12, 14), (50, 0), (88, 14), (98, 50), (96, 104), (50, 110)]), 'hood', 'f', ln=True),
             L(blob([(58, 6), (96, 46), (94, 100), (66, 106)], 6), 'hood_d', 'f', False)],
}

# ------------------------------------------------------------------ Kerry Bootgaiter: sombrero de paja de ala muy caída a los lados
# (como un tejado) sobre una media melena granate oscura; coloretes y ojos grandes
CHARS['kerry-bootgaiter'] = {
    'body': 'normal', 'pal': pal('#4a1e1e', '#fcd8bc', straw='#b07a30', straw_d='#80541e', blush='#f0a0a0'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 92, 'hairline': False},
    'front': [L(blob(BOB_F))] + fringe(4, 50, 66)
             + [L(blob([(34, 14), (34, -4), (66, -4), (66, 14)]), 'straw', 'f', ln=True), L(quad((34, 2), (50, 0), (66, 2)), 'straw_d', 'f', False, False, 2.4),
                L(blob([(-14, 72), (6, 30), (30, 14), (70, 14), (94, 30), (114, 72), (94, 70), (78, 46), (22, 46), (6, 70)]), 'straw', 'f', ln=True),
                L(blob([(64, 16), (94, 32), (110, 68), (94, 66)], 5), 'straw_d', 'f', False),
                L(ell(26, 86, 4, 2.6), 'blush', 'f', False), L(ell(74, 86, 4, 2.6), 'blush', 'f', False)],
    'side': [L(blob(BOB_S))] + bob_shade('side')
             + [L(blob([(36, 14), (40, -6), (66, -4), (64, 16)]), 'straw', 'f', ln=True),
                L(blob([(-14, 64), (10, 24), (40, 12), (74, 14), (100, 30), (106, 46), (72, 34), (40, 34), (18, 50), (0, 70)]), 'straw', 'f', ln=True)],
    'back': [L(blob(BOB_B))] + bob_shade('back')
            + [L(blob([(34, 14), (34, -4), (66, -4), (66, 14)]), 'straw', 'f', ln=True),
               L(blob([(-14, 76), (6, 30), (30, 14), (70, 14), (94, 30), (114, 76), (50, 80)]), 'straw_d', 'f', ln=True)],
}

# ------------------------------------------------------------------ Maddox Rock: pelo castaño con flequillo, unos cascos crema en
# las orejas y gafas de esquí naranjas; sonrisa
CHARS['maddox-rock'] = {
    'body': 'normal', 'pal': pal('#6a3424', '#fcc890', muff='#e8dcc4', muff_d='#4a4a50', lens='#f0a020', rim='#a8a0a0'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'ears': False, 'hairline': (60, 52)},
    'front': [L(blob(BOB_F))] + bob_shade('front') + fringe(4, 36, 62)
             + [L(ell(8, 70, 9, 14), 'muff', 'f', ln=True), L(ell(92, 70, 9, 14), 'muff', 'f', ln=True),
                L(ell(34, 74, 13, 9), 'rim', 'f', ln=True), L(ell(66, 74, 13, 9), 'rim', 'f', ln=True),
                L(ell(34, 74, 10, 6.6), 'lens', 'f', False), L(ell(66, 74, 10, 6.6), 'lens', 'f', False),
                L([(26, 74), (42, 74)], (120, 60, 10, 255), 'f', False, False, 1.4), L([(58, 74), (74, 74)], (120, 60, 10, 255), 'f', False, False, 1.4)],
    'side': [L(blob(BOB_S))] + bob_shade('side')
            + [L(ell(42, 70, 12, 15), 'muff', 'f', ln=True), L(ell(42, 70, 7, 10), 'muff_d', 'f', False),
               L(ell(88, 74, 7, 9), 'rim', 'f', ln=True), L(ell(89, 74, 4.4, 6), 'lens', 'f', False)],
    'back': [L(blob(BOB_B))] + bob_shade('back') + [L(ell(8, 70, 9, 14), 'muff', 'f', ln=True), L(ell(92, 70, 9, 14), 'muff', 'f', ln=True)],
}

# ------------------------------------------------------------------ Roland Climbstein: pelo verde azulado de mechones en punta con
# un pelillo arriba y unas gafas de esquí moradas sobre la frente (con nieve encima)
CHARS['roland-climbstein'] = {
    'body': 'normal', 'pal': pal('#2a7a74', '#fcd8b4', rim='#3a3a4a', lens='#6a5a8a', snow='#f4f4f8'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': (60, 52)},
    'front': [spk((44, 10), (52, 8), (52, -14), 3, light_left=False)] + [L(blob(BOB_F))] + bob_shade('front')
             + [spk((12, 44), (28, 40), (16, 80), 4, z='f'), spk((28, 40), (44, 38), (36, 66), 4, z='f'),
                spk((56, 38), (72, 40), (64, 66), 4, z='f', light_left=False), spk((72, 40), (88, 44), (84, 80), 4, z='f', light_left=False),
                L(quad((8, 36), (50, 26), (92, 36)), 'rim', 'f', False, False, 3),
                L(blob([(20, 26), (48, 22), (80, 26), (82, 42), (50, 44), (18, 42)]), 'rim', 'f', ln=True),
                L(blob([(24, 28), (48, 25), (76, 28), (78, 40), (50, 41), (22, 40)]), 'lens', 'f', False),
                L(bumpy(28, 20, 8, 4, 6, 0.1), 'snow', 'f', ln=True), L(bumpy(70, 20, 8, 4, 6, 0.1), 'snow', 'f', ln=True)],
    'side': [spk((40, 8), (48, 6), (48, -14), 3, light_left=False), L(blob(BOB_S))] + bob_shade('side')
            + [spk((56, 30), (88, 40), (92, 72), 5, z='f', light_left=False),
               L(quad((10, 40), (50, 26), (92, 30)), 'rim', 'f', False, False, 3), L(ell(84, 32, 7, 8), 'lens', 'f', ln=True)],
    'back': [spk((44, 10), (52, 8), (52, -14), 3, light_left=False), L(blob(BOB_B))] + bob_shade('back')
            + [spk((14, 84), (32, 90), (16, 100), 4), spk((32, 90), (50, 92), (40, 102), 4), spk((50, 92), (68, 90), (60, 102), 4, light_left=False),
               spk((68, 90), (86, 84), (84, 100), 4, light_left=False), L(quad((6, 42), (50, 34), (94, 42)), 'rim', 'f', False, False, 3)],
}

# ------------------------------------------------------------------ Robert Skipolson: media melena gris morada que le tapa un ojo,
# una diadema verde y orejeras crema; mirada tímida
CHARS['robert-skipolson'] = {
    'body': 'normal', 'pal': pal('#4a4050', '#fcd8b8', band='#7a8a2a', muff='#ece0c8'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 92, 'ears': False, 'hairline': (60, 52)},
    'front': [L(blob(BOB_F))] + bob_shade('front')
             + [L(blob([(14, 40), (40, 28), (64, 32), (62, 60), (54, 84), (44, 86), (40, 66), (22, 56)]), 'mid', 'f'),
                strand([(62, 34), (60, 60), (50, 86)], OUTC, 'f', 1.0), spk((64, 38), (88, 44), (84, 70), 5, z='f', light_left=False),
                L(quad((12, 36), (50, 18), (88, 36)), 'band', 'f', False, False, 3), L(ell(6, 70, 8, 12), 'muff', 'f', ln=True), L(ell(94, 70, 8, 12), 'muff', 'f', ln=True)],
    'side': [L(blob(BOB_S))] + bob_shade('side') + [L(quad((14, 40), (50, 20), (84, 24)), 'band', 'f', False, False, 3),
             L(ell(42, 68, 12, 15), 'muff', 'f', ln=True), spk((56, 30), (90, 40), (92, 76), 6, z='f', light_left=False)],
    'back': [L(blob(BOB_B))] + bob_shade('back') + [L(quad((10, 38), (50, 24), (90, 38)), 'band', 'f', False, False, 3),
             L(ell(6, 70, 8, 12), 'muff', 'f', ln=True), L(ell(94, 70, 8, 12), 'muff', 'f', ln=True)],
}

# ------------------------------------------------------------------ Quentin Rackner: pelo gris azulado liso en casco con flequillo
# y una bufanda verde oliva que le tapa la boca y cae por la espalda; ojos verde azulado
CHARS['quentin-rackner'] = {
    'body': 'normal', 'pal': pal('#4a5560', '#fcd8b8', iris='#3a8a8a', scarf='#5a6a3a', scarf_d='#3e4a28'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'none', 'hairline': (60, 52)},
    'front': [L(blob(BOB_F))] + bob_shade('front') + fringe(4, 36, 66)
             + [L(blob([(10, 86), (50, 90), (90, 86), (92, 108), (50, 114), (8, 108)]), 'scarf', 'f', ln=True),
                L(blob([(56, 90), (90, 86), (92, 106), (56, 112)], 5), 'scarf_d', 'f', False)],
    'side': [L(blob(BOB_S))] + bob_shade('side') + [spk((56, 30), (90, 40), (92, 72), 6, z='f', light_left=False),
             L(blob([(30, 86), (96, 88), (96, 106), (30, 108)]), 'scarf', 'f', ln=True), L(blob([(30, 96), (16, 100), (10, 128), (24, 128), (32, 108)]), 'scarf_d', 'f', ln=True)],
    'back': [L(blob(BOB_B))] + bob_shade('back') + [L(blob([(8, 92), (50, 96), (92, 92), (92, 108), (50, 112), (8, 108)]), 'scarf', 'f', ln=True),
             L(blob([(30, 100), (44, 100), (44, 140), (30, 140)]), 'scarf_d', 'f', ln=True)],
}

# ------------------------------------------------------------------ Trent Peggs (portero suplente): pelo granate de pinchos hacia
# arriba, cara redonda con ojos redondos muy abiertos y orejas grandes
CHARS['trent-peggs'] = {
    'body': 'normal', 'pal': pal('#5a1a2a', '#fcc070'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'face_front': WIDE_FACE, 'big_ears': 2, 'ear_out': 4, 'hairline': (50, 42)},
    'front': [spk((26, 18), (44, 10), (24, -14), 6), spk((44, 10), (60, 10), (54, -18), 6), spk((58, 12), (76, 20), (80, -12), 6, light_left=False),
              L(blob(SKULL_F)), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'shade', 'b', False)],
    'side': [spk((22, 26), (40, 12), (10, -12), 7), spk((40, 12), (60, 8), (52, -18), 6), L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False)],
    'back': [spk((26, 18), (44, 10), (24, -14), 6), spk((44, 10), (60, 10), (54, -18), 6), spk((58, 12), (76, 20), (80, -12), 6, light_left=False),
             L(blob(SKULL_B))] + back_hair(),
}

# ------------------------------------------------------------------ Pete Bogg: pelo granate muy oscuro de pinchos grandes en todas
# direcciones, ojos grandes y ceño
CHARS['pete-bogg'] = {
    'body': 'normal', 'pal': pal('#3a1414', '#fcc890'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (58, 50)},
    'front': spiky('front', 1.3) + spiky_face('front'), 'side': spiky('side', 1.3) + spiky_face('side'), 'back': spiky('back', 1.3),
}

# ------------------------------------------------------------------ Horace Onlign: pelo negro azulado de pinchos hacia arriba y a
# los lados, ojos afilados y ceño
CHARS['horace-onlign'] = {
    'body': 'normal', 'pal': pal('#1e2632', '#fcc890'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (56, 48)},
    'front': spiky('front', 0.9) + spiky_face('front'), 'side': spiky('side', 0.9) + spiky_face('side'), 'back': spiky('back', 0.9),
}
