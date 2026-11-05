"""Nose / Instituto Wild (IE1): un equipo de chicos salvajes con aspecto de animal; pelo y rasgos de cada jugador, con sus
modelos 3D como referencia."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, fat, pal, sheen, spk, strand
from heads import quad

DARK = (30, 22, 24, 255)
WHITE = (255, 255, 255, 255)

SIDE_SKULL = [(44, 92), (22, 88), (12, 64), (14, 36), (30, 16), (56, 10), (78, 18), (88, 36), (76, 44), (60, 48), (52, 62), (50, 80)]


def mustache(y=84, w=12, c='mid'):
    return L(blob([(50 - w, y + 3), (44, y - 1), (50, y + 1), (56, y - 1), (50 + w, y + 3), (52, y + 4), (48, y + 4)], 5), c, 'f')


def eyes_white(y=74, sep=14, r=6, pupil=2.2):
    """Ojos redondos grandes y blancos con pupila pequeña (los de expresión de sorpresa)."""
    return [L(ell(50 - sep, y, r, r), WHITE, 'f', ln=True), L(ell(50 + sep, y, r, r), WHITE, 'f', ln=True),
            L(ell(50 - sep, y, pupil, pupil), DARK, 'f', False), L(ell(50 + sep, y, pupil, pupil), DARK, 'f', False)]


# ------------------------------------------------------------------ Charlie Boardfield (portero): corpulento, melena oscura de
# pinchos revueltos, nariz ancha de jabalí con dos colmillos, cejas pobladas
CHARS['charlie-boardfield'] = {
    'body': 'corpulento', 'pal': pal('#3e3a22', '#e2a070', nose='#8a5a3a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 92, 'nose': (50, 82, 6), 'nose_side': (90, 80, 5), 'hairline': (60, 52)},
    'front': [L(blob([(8, 70), (4, 40), (16, 16), (50, 6), (84, 16), (96, 40), (92, 70)])),
              spk((6, 40), (18, 26), (-14, 20), 6), spk((18, 24), (36, 14), (10, -6), 6), spk((40, 12), (58, 10), (48, -10), 6),
              spk((62, 12), (80, 22), (88, -4), 6, light_left=False), spk((82, 26), (94, 40), (114, 20), 6, light_left=False),
              spk((4, 56), (12, 70), (-10, 76), 5), spk((88, 70), (96, 56), (110, 76), 5, light_left=False),
              L(blob([(60, 14), (92, 34), (92, 66), (76, 60)], 6), 'shade', 'b', False),
              spk((16, 48), (36, 42), (22, 66), 4, z='f'), spk((34, 42), (54, 40), (44, 62), 4, z='f'),
              spk((52, 40), (70, 42), (64, 60), 4, z='f', light_left=False), spk((66, 44), (86, 50), (84, 66), 4, z='f', light_left=False),
              L(fat((40, 90), (44, 90), (40, 98), 0), WHITE, 'f', ln=True), L(fat((56, 90), (60, 90), (60, 98), 0), WHITE, 'f', ln=True)],
    'side': [L(blob([(44, 94), (20, 90), (6, 64), (6, 32), (24, 8), (56, 2), (82, 14), (92, 36), (76, 44), (60, 48), (52, 62), (50, 80)])),
             spk((14, 30), (30, 14), (-12, 6), 7), spk((8, 52), (16, 36), (-16, 40), 6), spk((10, 76), (22, 88), (-10, 96), 5),
             spk((40, 6), (58, 2), (42, -14), 6), L(blob([(14, 46), (16, 80), (38, 90), (28, 62)], 6), 'shade', 'b', False),
             spk((54, 24), (86, 36), (92, 66), 6, z='f', light_left=False)],
    'back': [L(blob([(8, 70), (4, 40), (16, 16), (50, 6), (84, 16), (96, 40), (92, 70), (76, 92), (50, 98), (24, 92)])),
             spk((6, 40), (18, 26), (-14, 20), 6), spk((18, 24), (36, 14), (10, -6), 6), spk((40, 12), (58, 10), (48, -10), 6),
             spk((62, 12), (80, 22), (88, -4), 6, light_left=False), spk((82, 26), (94, 40), (114, 20), 6, light_left=False),
             spk((10, 76), (28, 88), (4, 102), 5), spk((28, 90), (48, 94), (34, 110), 5), spk((50, 94), (70, 90), (66, 110), 5, light_left=False),
             spk((70, 88), (88, 76), (96, 102), 5, light_left=False),
             L(blob([(58, 14), (92, 36), (90, 70), (70, 90)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Wilson Fishman: pelo azul grisáceo corto con una cresta como
# aleta; aletas de pez blancas en lugar de orejas, ojos blancos grandes y labios gruesos
FIN = '#d8c8c4'
CHARS['wilson-fishman'] = {
    'body': 'normal', 'pal': pal('#5a7a8a', '#f2b884', fin=FIN, fin_d='#a89090'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'lips', 'mouth_y': 90, 'mouth_w': 8, 'ears': False, 'hairline': (58, 52)},
    'front': [L(fat((44, 20), (56, 20), (52, -4), 3)),
              L(blob([(16, 62), (14, 36), (26, 18), (50, 12), (74, 18), (86, 36), (84, 62), (50, 52)])),
              L(blob([(60, 16), (86, 34), (84, 60), (70, 54)], 6), 'shade', 'b', False), sheen(26, 50, 20, 3),
              L(blob([(16, 62), (2, 52), (-4, 64), (2, 80), (16, 78)]), 'fin', 'f', ln=True), L(blob([(84, 62), (98, 52), (104, 64), (98, 80), (84, 78)]), 'fin', 'f', ln=True),
              strand([(4, 60), (12, 70)], 'fin_d', 'f', 1.1), strand([(2, 70), (12, 74)], 'fin_d', 'f', 1.1),
              strand([(96, 60), (88, 70)], 'fin_d', 'f', 1.1), strand([(98, 70), (88, 74)], 'fin_d', 'f', 1.1)] + eyes_white(72),
    'side': [L(fat((56, 14), (66, 18), (88, -4), 4)), L(fat((40, 14), (54, 12), (30, -2), 3)),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             L(blob([(48, 62), (30, 50), (22, 64), (28, 80), (46, 80)]), 'fin', 'f', ln=True),
             strand([(30, 58), (42, 66)], 'fin_d', 'f', 1.1), strand([(28, 70), (42, 72)], 'fin_d', 'f', 1.1),
             L(ell(82, 72, 5, 6), WHITE, 'f', ln=True), L(ell(84, 72, 2, 2), DARK, 'f', False)],
    'back': [L(fat((44, 18), (56, 18), (50, -4), 3)),
             L(blob([(16, 66), (14, 36), (26, 18), (50, 12), (74, 18), (86, 36), (84, 66), (70, 86), (50, 90), (30, 86)])),
             L(blob([(58, 18), (86, 38), (84, 66), (66, 84)], 6), 'shade', 'b', False), strand([(50, 16), (50, 70)], 'deep', 'b', 1.4),
             L(blob([(16, 62), (2, 52), (-4, 64), (2, 80), (16, 78)]), 'fin', 'f', ln=True), L(blob([(84, 62), (98, 52), (104, 64), (98, 80), (84, 78)]), 'fin', 'f', ln=True)],
}

# ------------------------------------------------------------------ Peter Johnson: pelo verde oliva recogido en un moño alto en
# punta que se curva a un lado, ojos amarillos rasgados
CHARS['peter-johnson'] = {
    'body': 'delgado', 'pal': pal('#6c7a2a', '#f4c48c', iris='#c8b830'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'hairline': (60, 50)},
    'front': [L(blob([(36, 30), (30, 12), (36, -6), (46, -18), (58, -26), (70, -24), (60, -14), (62, 4), (66, 26)])),
              L(blob([(52, -16), (64, -22), (58, -8), (60, 14), (54, 26)], 6), 'shade', 'b', False),
              L(blob([(16, 62), (14, 38), (26, 20), (50, 14), (74, 20), (86, 38), (84, 62), (50, 52)])),
              L(blob([(60, 18), (86, 38), (84, 60), (70, 54)], 6), 'shade', 'b', False), sheen(26, 48, 22, 3),
              strand([(34, 22), (40, 46)], 'shade', 'b', 1.0), strand([(64, 22), (60, 46)], 'shade', 'b', 1.0)],
    'side': [L(blob([(30, 26), (24, 8), (30, -10), (40, -22), (54, -28), (64, -24), (52, -14), (50, 2), (54, 22)])),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             strand([(70, 24), (40, 22), (20, 44)], 'shade', 'b', 1.0)],
    'back': [L(blob([(36, 30), (30, 12), (36, -6), (46, -18), (58, -26), (70, -24), (60, -14), (62, 4), (66, 26)])),
             L(blob([(16, 66), (14, 38), (26, 20), (50, 14), (74, 20), (86, 38), (84, 66), (70, 86), (50, 90), (30, 86)])),
             L(blob([(58, 18), (86, 38), (84, 66), (66, 84)], 6), 'shade', 'b', False),
             strand([(36, 26), (40, 80)], 'shade', 'b', 1.0), strand([(64, 26), (60, 80)], 'deep', 'b', 1.0)],
}

# ------------------------------------------------------------------ Leonard O'Shea: corpulento, melena castaña de león revuelta
# alrededor de la cara, ojos pequeños y enfadados, nariz chata
LEO_MANE = [spk((14, 50), (22, 34), (-10, 30), 7), spk((20, 32), (36, 20), (4, 4), 7), spk((36, 20), (56, 16), (40, -8), 7),
            spk((56, 16), (74, 22), (76, -6), 7, light_left=False), spk((72, 26), (86, 38), (106, 18), 7, light_left=False),
            spk((80, 46), (88, 60), (110, 56), 6, light_left=False), spk((12, 60), (20, 72), (-10, 74), 6)]
CHARS['leonard-o-shea'] = {
    'body': 'corpulento', 'pal': pal('#9a5422', '#e8b080', nose='#c88a5a'),
    # melena castaña de león: mechones grandes alrededor de la cara; ojos pequeños y enfadados, nariz chata
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'frown', 'nose': (50, 80, 4.4), 'nose_side': (90, 80, 4), 'hairline': (60, 52)},
    'front': LEO_MANE + [L(blob([(10, 72), (6, 42), (18, 18), (50, 10), (82, 18), (94, 42), (90, 72)])),
              L(blob([(60, 14), (90, 36), (90, 70), (76, 64)], 6), 'shade', 'b', False), sheen(24, 48, 18, 3),
              spk((14, 44), (34, 40), (20, 68), 5, z='f'), spk((32, 40), (52, 38), (42, 62), 5, z='f'),
              spk((50, 38), (68, 40), (62, 60), 5, z='f', light_left=False), spk((66, 42), (88, 46), (84, 68), 5, z='f', light_left=False),
              spk((10, 64), (20, 70), (10, 98), 4, z='f'), spk((80, 70), (90, 64), (90, 98), 4, z='f', light_left=False)],
    'side': [spk((14, 34), (28, 18), (-10, 10), 7), spk((8, 56), (16, 38), (-16, 42), 7), spk((10, 78), (22, 90), (-10, 98), 6),
             spk((34, 12), (54, 8), (40, -12), 6), spk((56, 10), (72, 16), (78, -6), 6, light_left=False),
             L(blob([(46, 94), (20, 90), (6, 62), (8, 32), (24, 10), (54, 4), (80, 14), (92, 36), (76, 44), (60, 48), (54, 62), (52, 82)])),
             L(blob([(12, 46), (14, 84), (40, 92), (26, 62)], 6), 'shade', 'b', False),
             spk((54, 24), (86, 34), (94, 68), 7, z='f', light_left=False), spk((52, 54), (62, 54), (58, 86), 3, z='f')],
    'back': LEO_MANE + [L(blob([(10, 72), (6, 42), (18, 18), (50, 10), (82, 18), (94, 42), (90, 72), (74, 92), (50, 98), (26, 92)])),
             spk((12, 80), (30, 92), (4, 106), 6), spk((30, 94), (50, 98), (36, 114), 6), spk((50, 98), (70, 94), (66, 114), 6, light_left=False),
             spk((70, 92), (88, 80), (96, 106), 6, light_left=False),
             L(blob([(58, 14), (92, 38), (90, 72), (70, 92)], 6), 'shade', 'b', False), sheen(26, 50, 18, 3)],
}

# ------------------------------------------------------------------ Hugo Tallgeese: bajito, cabeza calva con una cresta roja de
# pinchos largos que sale hacia arriba desde la frente; orejas grandes y cara de enfado
CHARS['hugo-tallgeese'] = {
    'body': 'bajito', 'pal': pal('#8a2a12', '#f2c098'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'big_ears': 2, 'ear_out': 4, 'hairline': False},
    'front': [L(blob([(16, 66), (14, 36), (26, 16), (50, 10), (74, 16), (86, 36), (84, 66)]), 'skin'),
              L(blob([(62, 16), (84, 36), (82, 62), (72, 58)], 6), 'skin_d', 'b', False),
              spk((38, 46), (48, 36), (24, 2), 5, z='f'), spk((44, 40), (54, 36), (38, -10), 5, z='f'),
              spk((48, 36), (58, 40), (60, -14), 5, z='f', light_left=False), spk((54, 40), (62, 48), (78, 4), 5, z='f', light_left=False),
              spk((44, 52), (56, 52), (48, 66), 2, z='f')],
    'side': [L(blob([(44, 92), (22, 88), (14, 64), (16, 36), (30, 16), (56, 10), (78, 18), (88, 40), (88, 62), (64, 56)]), 'skin'),
             spk((56, 34), (70, 30), (30, -6), 6, z='f'), spk((64, 30), (76, 36), (58, -14), 5, z='f'), spk((70, 36), (80, 44), (88, 4), 4, z='f', light_left=False)],
    'back': [L(blob([(16, 70), (14, 36), (26, 16), (50, 10), (74, 16), (86, 36), (84, 70), (66, 88), (34, 88)]), 'skin'),
             L(blob([(58, 14), (84, 36), (82, 68), (66, 86)], 6), 'skin_d', 'b', False),
             spk((40, 30), (50, 24), (30, -6), 5, z='f'), spk((48, 24), (56, 26), (54, -14), 5, z='f'), spk((54, 26), (62, 32), (74, -4), 5, z='f', light_left=False)],
}

# ------------------------------------------------------------------ Cham Lion: pelo verde lima largo y liso con un flequillo que
# le tapa media cara, dos moños a los lados (con forma de concha) y una coleta trenzada
CHARS['cham-lion'] = {
    'body': 'normal', 'pal': pal('#8ab83c', '#e8b080', bun='#6a7a4a'),
    'face': {'eyes': 'sharp', 'mouth': 'smile', 'hairline': (62, 52)},
    'front': [L(ell(8, 32, 11, 11), 'bun', 'b'), L(ell(92, 32, 11, 11), 'bun', 'b'), L(ell(4, 30, 5, 5), 'deep', 'b', False, False, 1.0), L(ell(96, 30, 5, 5), 'deep', 'b', False, False, 1.0),
              L(blob([(8, 100), (6, 50), (16, 20), (50, 10), (84, 20), (94, 50), (92, 100), (80, 98), (82, 62), (18, 62), (20, 98)])),
              L(blob([(70, 20), (92, 50), (90, 96), (80, 94)], 6), 'shade', 'b', False), sheen(22, 48, 20, 3),
              spk((14, 44), (36, 40), (22, 74), 5, z='f'), spk((34, 40), (56, 38), (46, 70), 5, z='f'),
              spk((54, 40), (74, 42), (66, 66), 4, z='f', light_left=False), spk((70, 44), (88, 50), (84, 74), 4, z='f', light_left=False)],
    'side': [L(blob([(20, 80), (12, 96), (16, 116), (24, 112), (26, 90)]), 'bun', 'b', True, True),
             L(blob([(46, 96), (22, 92), (8, 66), (10, 36), (26, 14), (54, 8), (78, 16), (90, 36), (76, 44), (60, 48), (54, 62), (52, 84)])),
             L(blob([(14, 50), (16, 86), (40, 94), (26, 66)], 6), 'shade', 'b', False),
             L(ell(34, 34, 11, 11), 'bun', 'f', True, True), L(ell(34, 34, 6, 6), 'deep', 'f', False, False, 1.0), L(ell(34, 34, 2, 2), 'deep', 'f', False),
             spk((54, 26), (86, 36), (92, 70), 6, z='f', light_left=False)],
    'back': [L(ell(8, 32, 11, 11), 'bun', 'b'), L(ell(92, 32, 11, 11), 'bun', 'b'), L(ell(4, 30, 5, 5), 'deep', 'b', False, False, 1.0), L(ell(96, 30, 5, 5), 'deep', 'b', False, False, 1.0),
             L(blob([(8, 100), (6, 50), (16, 20), (50, 10), (84, 20), (94, 50), (92, 100), (50, 106)])),
             L(blob([(58, 16), (90, 40), (90, 98), (66, 104)], 6), 'shade', 'b', False), sheen(26, 52, 20, 3),
             L(blob([(42, 90), (58, 90), (56, 124), (44, 124)]), 'bun', 'f', True, True)],
}

# ------------------------------------------------------------------ Steve Eagle: gorro blanco de aviador que le cubre la cabeza y
# baja como una bufanda, con gafas de piloto en la frente y plumas negras a un lado; piel oscura y ojos amarillos
CHARS['steve-eagle'] = {
    'body': 'delgado', 'pal': pal('#2a2420', '#a06a3e', iris='#d8c030', hood='#ece4d0', hood_d='#c8b8a0', gog='#8a7a5a', lens='#d8d0b0', feather='#2a2a30'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'hairline': False, 'ears': False},
    'front': [L(fat((84, 52), (90, 60), (116, 34), 3), 'feather', 'b', True, True), L(fat((86, 60), (90, 68), (118, 58), 3), 'feather', 'b', True, True),
              L(blob([(6, 108), (4, 60), (12, 24), (34, 6), (66, 6), (88, 24), (96, 60), (94, 108), (78, 104), (80, 70), (20, 70), (22, 104)]), 'hood', 'f', ln=True),
              L(blob([(60, 10), (92, 40), (92, 104), (80, 102)], 6), 'hood_d', 'f', False),
              L(blob([(20, 60), (50, 52), (80, 60), (80, 66), (50, 58), (20, 66)], 4), 'hood_d', 'f', False),
              spk((30, 58), (44, 58), (36, 70), 2, z='f'),
              L(ell(34, 30, 11, 9), 'gog', 'f', ln=True), L(ell(66, 30, 11, 9), 'gog', 'f', ln=True),
              L(ell(34, 30, 7.4, 5.8), 'lens', 'f', False), L(ell(66, 30, 7.4, 5.8), 'lens', 'f', False)],
    'side': [L(fat((20, 52), (30, 58), (-12, 40), 3), 'feather', 'b', True, True),
             L(blob([(50, 110), (14, 104), (4, 64), (10, 26), (32, 6), (62, 4), (84, 16), (94, 40), (90, 62), (66, 62), (56, 80), (60, 104)]), 'hood', 'f', ln=True),
             L(blob([(10, 40), (30, 12), (34, 70), (22, 100)], 6), 'hood_d', 'f', False),
             L(ell(76, 30, 9, 9), 'gog', 'f', ln=True), L(ell(78, 30, 5.4, 6), 'lens', 'f', False)],
    'back': [L(fat((70, 60), (80, 66), (114, 50), 3), 'feather', 'b', True, True), L(fat((72, 66), (82, 72), (112, 74), 3), 'feather', 'b', True, True),
             L(blob([(6, 110), (4, 60), (12, 24), (34, 6), (66, 6), (88, 24), (96, 60), (94, 110), (50, 116)]), 'hood', 'f', ln=True),
             L(blob([(56, 10), (92, 40), (92, 106), (66, 112)], 6), 'hood_d', 'f', False),
             L([(6, 48), (50, 42), (94, 48)], 'gog', 'f', False, False, 2.4)],
}

# ------------------------------------------------------------------ Bruce Monkey: pañuelo naranja atado en la cabeza (con el nudo
# a un lado), pelo castaño que asoma por debajo, piel morena y colmillos
CHARS['bruce-monkey'] = {
    'body': 'normal', 'pal': pal('#5a3a22', '#a0683c', cloth='#eca018', cloth_d='#c07810'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'hairline': (60, 54)},
    'front': [L(blob([(10, 84), (8, 56), (92, 56), (90, 84), (80, 80), (20, 80)])),
              spk((10, 60), (22, 64), (8, 90), 3), spk((78, 64), (90, 60), (92, 90), 3, light_left=False),
              L(blob([(10, 60), (8, 34), (20, 14), (50, 6), (80, 14), (92, 34), (90, 60), (50, 54)]), 'cloth', 'f', ln=True),
              L(blob([(60, 10), (90, 32), (90, 58), (74, 56)], 6), 'cloth_d', 'f', False),
              strand([(20, 40), (50, 34), (80, 40)], 'cloth_d', 'f', 1.0), strand([(14, 50), (50, 46), (86, 50)], 'cloth_d', 'f', 1.0),
              L(blob([(88, 34), (102, 26), (104, 44), (92, 46)], 4), 'cloth', 'f', ln=True), L(blob([(90, 44), (104, 48), (100, 60), (90, 52)], 4), 'cloth_d', 'f', ln=True),
              spk((24, 54), (40, 54), (30, 66), 2, z='f'), spk((60, 54), (76, 54), (70, 66), 2, z='f', light_left=False)],
    'side': [L(blob(SIDE_SKULL)), spk((14, 66), (24, 76), (6, 90), 3), spk((24, 80), (36, 86), (22, 98), 3),
             L(blob([(12, 60), (10, 32), (26, 10), (54, 4), (80, 12), (92, 32), (90, 56), (50, 56)]), 'cloth', 'f', ln=True),
             L(blob([(12, 40), (26, 14), (30, 56)], 6), 'cloth_d', 'f', False),
             L(blob([(12, 40), (-4, 34), (-6, 52), (8, 54)], 4), 'cloth', 'f', ln=True), L(blob([(10, 50), (-6, 60), (0, 70), (14, 58)], 4), 'cloth_d', 'f', ln=True)],
    'back': [L(blob([(14, 70), (12, 56), (88, 56), (86, 70), (68, 88), (32, 88)])),
             L(blob([(10, 64), (8, 34), (20, 14), (50, 6), (80, 14), (92, 34), (90, 64), (50, 66)]), 'cloth', 'f', ln=True),
             L(blob([(56, 10), (90, 32), (90, 62), (70, 64)], 6), 'cloth_d', 'f', False),
             L(blob([(40, 52), (24, 44), (20, 60), (38, 64)], 4), 'cloth', 'f', ln=True), L(blob([(60, 52), (76, 44), (80, 60), (62, 64)], 4), 'cloth', 'f', ln=True),
             L(ell(50, 58, 7, 6), 'cloth_d', 'f', ln=True)],
}

# ------------------------------------------------------------------ Gary Lancaster: corpulento, piel anaranjada de oso, pelo azul
# oscuro peinado en una tupé, ceja gruesa y una cicatriz en el ojo
CHARS['gary-lancaster'] = {
    'body': 'corpulento', 'pal': pal('#2c3e5c', '#c0702c', nose='#5a2a1a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 91, 'nose': (50, 80, 4.4), 'nose_side': (90, 79, 4), 'big_ears': 1, 'hairline': (56, 46)},
    'front': [L(blob([(18, 56), (16, 30), (28, 12), (50, 4), (72, 12), (84, 30), (82, 56), (50, 46)])),
              L(blob([(58, 8), (84, 30), (82, 54), (68, 50)], 6), 'shade', 'b', False), sheen(30, 54, 12, 3),
              # cejas gruesas muy inclinadas y sombra bajo ellas: mirada amenazante
              L(blob([(22, 62), (46, 70), (46, 74), (24, 68)], 3), OUTC, 'f'), L(blob([(78, 62), (54, 70), (54, 74), (76, 68)], 3), OUTC, 'f'),
              L(blob([(24, 68), (46, 74), (44, 78), (26, 74)], 3), 'skin_d', 'f', False), L(blob([(76, 68), (54, 74), (56, 78), (74, 74)], 3), 'skin_d', 'f', False),
              L([(58, 66), (70, 86)], OUTC, 'f', False, False, 1.4), L([(62, 64), (74, 84)], OUTC, 'f', False, False, 1.0)],
    'side': [L(blob([(48, 66), (30, 72), (16, 56), (16, 30), (30, 8), (56, 0), (80, 10), (92, 30), (84, 44), (64, 46)])),
             L(blob([(18, 40), (30, 12), (36, 60)], 6), 'shade', 'b', False), strand([(80, 20), (50, 14), (24, 36)], 'shade', 'b', 1.1)],
    'back': [L(blob([(18, 66), (16, 30), (28, 12), (50, 4), (72, 12), (84, 30), (82, 66), (50, 72)])),
             L(blob([(58, 8), (84, 30), (82, 64), (66, 70)], 6), 'shade', 'b', False), strand([(50, 6), (50, 60)], 'deep', 'b', 1.2)],
}

# ------------------------------------------------------------------ Harry Snake: melena morada ondulada hasta la mandíbula, piel
# verdosa de serpiente, ojos amarillos rasgados y sonrisa
CHARS['harry-snake'] = {
    'body': 'delgado', 'pal': pal('#6c5a7c', '#c8d090', iris='#c8b020'),
    'face': {'eyes': 'sharp', 'mouth': 'smile', 'hairline': (62, 52)},
    'front': [L(blob([(8, 96), (4, 50), (14, 18), (50, 8), (86, 18), (96, 50), (92, 96), (80, 92), (82, 62), (18, 62), (20, 92)])),
              L(blob([(70, 20), (94, 50), (90, 92), (80, 90)], 6), 'shade', 'b', False), sheen(22, 48, 20, 3),
              spk((14, 44), (36, 40), (20, 72), 5, z='f'), spk((34, 40), (52, 38), (40, 64), 4, z='f'),
              spk((50, 38), (68, 40), (62, 62), 4, z='f', light_left=False), spk((66, 42), (88, 48), (84, 72), 5, z='f', light_left=False)],
    'side': [L(blob([(48, 96), (20, 94), (6, 66), (8, 34), (24, 12), (54, 6), (78, 14), (90, 34), (76, 44), (60, 48), (54, 62), (52, 84)])),
             L(blob([(12, 50), (14, 88), (40, 94), (26, 66)], 6), 'shade', 'b', False), sheen(32, 62, 14, 3),
             spk((54, 24), (86, 34), (90, 76), 6, z='f', light_left=False)],
    'back': [L(blob([(8, 96), (4, 50), (14, 18), (50, 8), (86, 18), (96, 50), (92, 96), (50, 102)])),
             L(blob([(58, 14), (92, 40), (90, 94), (66, 100)], 6), 'shade', 'b', False), sheen(26, 52, 20, 3),
             strand([(34, 40), (30, 96)], 'shade', 'b', 1.0), strand([(64, 40), (68, 96)], 'deep', 'b', 1.0)],
}

# ------------------------------------------------------------------ Adrian Speed: guepardo: pelo rubio de puntas con mechones
# castaños a los lados como orejas, marcas oscuras bajo los ojos y un pañuelo de leopardo al cuello
CHARS['adrian-speed'] = {
    'body': 'normal', 'pal': pal('#d8b048', '#f2c08e', ear='#8a5a2a', scarf='#c88a4a', spot='#3a2a1a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'hairline': (60, 52)},
    'front': [L(fat((10, 46), (24, 30), (-2, 18), 5), 'ear', 'b', True, True), L(fat((76, 30), (90, 46), (102, 18), 5), 'ear', 'b', True, True),
              L(blob([(14, 64), (12, 40), (24, 18), (50, 10), (76, 18), (88, 40), (86, 64)])),
              spk((26, 18), (42, 12), (24, -6), 5), spk((42, 12), (58, 10), (48, -10), 5), spk((58, 12), (74, 18), (76, -6), 5, light_left=False),
              L(blob([(60, 16), (86, 36), (86, 62), (72, 58)], 6), 'shade', 'b', False),
              spk((16, 46), (34, 42), (20, 70), 4, z='f'), spk((32, 42), (50, 40), (40, 64), 4, z='f'),
              spk((50, 40), (68, 42), (62, 62), 4, z='f', light_left=False), spk((66, 44), (86, 48), (82, 70), 4, z='f', light_left=False),
              L([(30, 80), (26, 90)], 'spot', 'f', False, False, 1.4), L([(70, 80), (74, 90)], 'spot', 'f', False, False, 1.4),
              L(blob([(22, 100), (50, 108), (78, 100), (74, 112), (50, 118), (26, 112)], 5), 'scarf', 'f', ln=True),
              L(ell(36, 106, 1.6, 1.6), 'spot', 'f', False), L(ell(50, 112, 1.6, 1.6), 'spot', 'f', False), L(ell(64, 106, 1.6, 1.6), 'spot', 'f', False)],
    'side': [L(fat((30, 30), (44, 22), (12, 8), 5), 'ear', 'b', True, True),
             L(blob(SIDE_SKULL)), spk((18, 40), (32, 22), (-4, 14), 6), spk((32, 22), (50, 14), (24, -8), 5), spk((50, 14), (66, 16), (58, -8), 5),
             L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((54, 26), (86, 36), (92, 66), 6, z='f', light_left=False),
             L(blob([(44, 98), (84, 100), (84, 110), (44, 110)], 5), 'scarf', 'f', ln=True), L(blob([(46, 104), (26, 110), (18, 124), (30, 122), (44, 112)], 4), 'scarf', 'f', ln=True)],
    'back': [L(fat((10, 46), (24, 30), (-2, 18), 5), 'ear', 'b', True, True), L(fat((76, 30), (90, 46), (102, 18), 5), 'ear', 'b', True, True),
             L(blob([(14, 66), (12, 40), (24, 18), (50, 10), (76, 18), (88, 40), (86, 66), (72, 86), (50, 92), (28, 86)]), 'ear'),
             spk((26, 18), (42, 12), (24, -6), 5, light_left=True), spk((42, 12), (58, 10), (48, -10), 5), spk((58, 12), (74, 18), (76, -6), 5, light_left=False),
             spk((16, 74), (34, 86), (10, 100), 5), spk((34, 88), (54, 92), (40, 108), 5), spk((54, 92), (72, 88), (68, 108), 5, light_left=False),
             spk((70, 86), (86, 74), (94, 100), 5, light_left=False),
             L(blob([(20, 100), (80, 100), (80, 110), (20, 110)], 5), 'scarf', 'f', ln=True), L(blob([(44, 106), (56, 106), (62, 124), (40, 124)], 4), 'scarf', 'f', ln=True)],
}

# ------------------------------------------------------------------ Alan Coe: bajito y regordete, pelo corto castaño claro con un
# pelillo arriba, orejas grandes de mono, nariz roja, coloretes y ojos pequeños
CHARS['alan-coe'] = {
    'body': 'bajito', 'pal': pal('#9a7258', '#f6b46c', nose='#e05a3a', blush='#f08a6a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'nose': (50, 80, 3.6), 'nose_side': (89, 79, 3.4),
             'big_ears': 4, 'ear_out': 8, 'ears_front': True, 'hairline': (58, 50)},
    'front': [L(fat((48, 14), (54, 14), (44, 0), 2)), L(fat((52, 14), (58, 14), (60, 0), 2)),
              L(blob([(16, 62), (14, 38), (26, 18), (50, 12), (74, 18), (86, 38), (84, 62), (50, 52)])),
              L(blob([(60, 16), (86, 36), (84, 60), (70, 54)], 6), 'shade', 'b', False), sheen(28, 52, 20, 3),
              spk((22, 48), (40, 44), (28, 60), 2, z='f'), spk((40, 44), (60, 44), (52, 58), 2, z='f'), spk((60, 44), (78, 48), (72, 60), 2, z='f', light_left=False),
              L(ell(28, 84, 6, 3.6), 'blush', 'f', False), L(ell(72, 84, 6, 3.6), 'blush', 'f', False)],
    'side': [L(fat((48, 12), (56, 12), (44, -4), 2)),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((56, 28), (84, 38), (88, 56), 4, z='f', light_left=False), L(ell(78, 86, 5, 3), 'blush', 'f', False)],
    'back': [L(fat((48, 14), (54, 14), (44, 0), 2)), L(fat((52, 14), (58, 14), (60, 0), 2)),
             L(blob([(16, 66), (14, 38), (26, 18), (50, 12), (74, 18), (86, 38), (84, 66), (70, 86), (50, 90), (30, 86)])),
             L(blob([(58, 18), (86, 38), (84, 66), (66, 84)], 6), 'shade', 'b', False), sheen(28, 54, 20, 3)],
}

# ------------------------------------------------------------------ Philip Anders: panda: melena azul marino muy oscura con dos
# moños redondos como orejas de panda, piel blanca y manchas negras alrededor de los ojos
CHARS['philip-anders'] = {
    'body': 'normal', 'pal': pal('#24324a', '#f8ecdc'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'hairline': (58, 50), 'ears': False},
    'front': [L(bumpy(18, 18, 11, 11, 8, 0.08)), L(bumpy(82, 18, 11, 11, 8, 0.08)),
              L(blob([(8, 88), (4, 46), (14, 18), (50, 8), (86, 18), (96, 46), (92, 88), (80, 84), (82, 62), (18, 62), (20, 84)])),
              L(blob([(70, 20), (94, 50), (90, 84), (80, 82)], 6), 'shade', 'b', False), sheen(24, 50, 20, 3),
              spk((22, 46), (50, 38), (34, 64), 6, z='f'), spk((50, 38), (78, 46), (66, 64), 6, z='f', light_left=False),
              L(ell(34, 76, 10, 8), DARK, 'f', False), L(ell(66, 76, 10, 8), DARK, 'f', False),
              L(ell(34, 76, 5, 5), WHITE, 'f', False), L(ell(66, 76, 5, 5), WHITE, 'f', False),
              L(ell(34, 76, 2.4, 2.4), DARK, 'f', False), L(ell(66, 76, 2.4, 2.4), DARK, 'f', False)],
    'side': [L(bumpy(40, 16, 11, 11, 8, 0.08)),
             L(blob([(48, 92), (20, 90), (6, 62), (8, 32), (24, 10), (54, 6), (80, 16), (90, 36), (76, 44), (60, 48), (54, 62), (52, 82)])),
             L(blob([(12, 48), (14, 84), (40, 92), (26, 64)], 6), 'shade', 'b', False),
             spk((54, 26), (86, 36), (90, 66), 6, z='f', light_left=False),
             L(ell(82, 76, 6, 8), DARK, 'f', False), L(ell(83, 76, 3, 4), WHITE, 'f', False), L(ell(84, 76, 1.6, 2), DARK, 'f', False)],
    'back': [L(bumpy(18, 18, 11, 11, 8, 0.08)), L(bumpy(82, 18, 11, 11, 8, 0.08)),
             L(blob([(8, 88), (4, 46), (14, 18), (50, 8), (86, 18), (96, 46), (92, 88), (50, 96)])),
             L(blob([(58, 14), (92, 40), (90, 86), (66, 94)], 6), 'shade', 'b', False), sheen(26, 52, 20, 3)],
}

# ------------------------------------------------------------------ Rocky Rackham: corpulento, melena oscura de oso con dos
# orejitas redondas arriba, cara redonda con manchas oscuras alrededor de los ojos
CHARS['rocky-rackham'] = {
    'body': 'corpulento', 'pal': pal('#2c2a18', '#e2a676', patch='#7a5236'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'smile', 'hairline': (60, 50)},
    'front': [L(bumpy(22, 16, 10, 10, 8, 0.08)), L(bumpy(78, 16, 10, 10, 8, 0.08)),
              L(blob([(10, 80), (6, 44), (16, 18), (50, 8), (84, 18), (94, 44), (90, 80), (80, 76), (80, 60), (20, 60), (20, 76)])),
              L(blob([(60, 14), (90, 36), (88, 76), (78, 74)], 6), 'shade', 'b', False),
              spk((18, 44), (40, 40), (26, 64), 5, z='f'), spk((38, 40), (62, 40), (50, 62), 5, z='f'), spk((60, 40), (82, 44), (74, 64), 5, z='f', light_left=False),
              L(ell(36, 74, 8, 5), 'patch', 'f', False), L(ell(64, 74, 8, 5), 'patch', 'f', False)],
    'side': [L(bumpy(40, 14, 10, 10, 8, 0.08)),
             L(blob([(46, 92), (20, 90), (6, 62), (8, 32), (24, 10), (54, 6), (80, 16), (90, 36), (76, 44), (60, 48), (54, 62), (52, 82)])),
             L(blob([(12, 48), (14, 84), (40, 92), (26, 64)], 6), 'shade', 'b', False),
             spk((54, 26), (86, 36), (90, 64), 6, z='f', light_left=False), L(ell(82, 74, 6, 5), 'patch', 'f', False)],
    'back': [L(bumpy(22, 16, 10, 10, 8, 0.08)), L(bumpy(78, 16, 10, 10, 8, 0.08)),
             L(blob([(10, 80), (6, 44), (16, 18), (50, 8), (84, 18), (94, 44), (90, 80), (50, 88)])),
             L(blob([(58, 14), (90, 38), (88, 78), (66, 86)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Matt Mouseman: ratón: pelo castaño rojizo despeinado de
# puntas, bigotes de ratón, dientes de conejo y ojos pequeños
CHARS['matt-mouseman'] = {
    'body': 'normal', 'pal': pal('#b07058', '#f6c48e'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'buck', 'mouth_y': 88, 'hairline': (60, 52)},
    'front': [L(blob([(12, 64), (8, 40), (20, 16), (50, 8), (80, 16), (92, 40), (88, 64)])),
              spk((8, 52), (16, 64), (-6, 66), 4), spk((84, 64), (92, 52), (106, 66), 4, light_left=False),
              spk((36, 12), (50, 10), (42, -2), 4), spk((50, 10), (64, 12), (60, -2), 4, light_left=False),
              L(blob([(60, 14), (88, 34), (88, 62), (72, 58)], 6), 'shade', 'b', False), sheen(22, 46, 18, 3),
              spk((16, 46), (34, 42), (22, 68), 4, z='f'), spk((32, 42), (50, 40), (40, 64), 4, z='f'),
              spk((50, 40), (68, 42), (62, 62), 4, z='f', light_left=False), spk((66, 44), (86, 48), (82, 68), 4, z='f', light_left=False),
              L([(30, 84), (18, 82)], OUTC, 'f', False, False, 0.9), L([(30, 87), (18, 88)], OUTC, 'f', False, False, 0.9),
              L([(70, 84), (82, 82)], OUTC, 'f', False, False, 0.9), L([(70, 87), (82, 88)], OUTC, 'f', False, False, 0.9)],
    'side': [L(blob(SIDE_SKULL)), spk((14, 40), (28, 24), (-8, 16), 6), spk((12, 62), (22, 46), (-10, 52), 5), spk((40, 12), (56, 8), (40, -10), 5),
             L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((54, 26), (84, 36), (92, 66), 6, z='f', light_left=False), L([(84, 84), (96, 82)], OUTC, 'f', False, False, 0.9)],
    'back': [L(blob([(12, 66), (8, 40), (20, 16), (50, 8), (80, 16), (92, 40), (88, 66), (74, 86), (50, 92), (26, 86)])),
             spk((8, 52), (16, 64), (-6, 66), 4), spk((84, 64), (92, 52), (106, 66), 4, light_left=False),
             spk((36, 12), (50, 10), (42, -2), 4), spk((50, 10), (64, 12), (60, -2), 4, light_left=False),
             spk((18, 76), (36, 86), (12, 100), 4), spk((36, 88), (54, 92), (42, 106), 4), spk((54, 92), (72, 88), (68, 106), 4, light_left=False),
             spk((70, 86), (86, 76), (94, 100), 4, light_left=False),
             L(blob([(58, 14), (88, 36), (86, 68), (68, 86)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Chad Bullford: corpulento, pelo verde azulado revuelto con dos
# cuernos de toro blancos, nariz ancha; portero suplente
CHARS['chad-bullford'] = {
    'body': 'corpulento', 'pal': pal('#2a7a74', '#e8a46a', horn='#ece4d4', nose='#c88a5a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'nose': (50, 80, 5), 'nose_side': (90, 79, 4.4), 'hairline': (60, 52)},
    'front': [L(blob([(12, 66), (8, 40), (20, 16), (50, 8), (80, 16), (92, 40), (88, 66)])),
              spk((20, 20), (36, 12), (16, -4), 5), spk((40, 10), (58, 8), (48, -10), 5), spk((62, 10), (78, 18), (82, -4), 5, light_left=False),
              L(blob([(60, 14), (88, 34), (88, 62), (72, 58)], 6), 'shade', 'b', False),
              spk((16, 46), (34, 42), (22, 66), 4, z='f'), spk((32, 42), (50, 40), (40, 62), 4, z='f'),
              spk((50, 40), (68, 42), (62, 60), 4, z='f', light_left=False), spk((66, 44), (86, 48), (82, 66), 4, z='f', light_left=False),
              L(fat((12, 52), (20, 44), (-6, 34), 4), 'horn', 'f', True, True), L(fat((80, 44), (88, 52), (106, 34), 4), 'horn', 'f', True, True)],
    'side': [
             L(blob(SIDE_SKULL)), spk((18, 36), (32, 20), (-6, 10), 6), spk((12, 60), (22, 44), (-10, 50), 5), spk((40, 12), (58, 8), (44, -10), 5),
             L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((54, 26), (84, 36), (92, 66), 6, z='f', light_left=False), L(fat((58, 46), (68, 40), (76, 22), 4), 'horn', 'f', True, True)],
    'back': [L(fat((12, 52), (20, 44), (-6, 34), 4), 'horn', 'b', True, True), L(fat((80, 44), (88, 52), (106, 34), 4), 'horn', 'b', True, True),
             L(blob([(12, 66), (8, 40), (20, 16), (50, 8), (80, 16), (92, 40), (88, 66), (74, 86), (50, 92), (26, 86)])),
             spk((20, 20), (36, 12), (16, -4), 5), spk((40, 10), (58, 8), (48, -10), 5), spk((62, 10), (78, 18), (82, -4), 5, light_left=False),
             spk((18, 76), (36, 86), (12, 100), 4), spk((36, 88), (54, 92), (42, 106), 4), spk((54, 92), (72, 88), (68, 106), 4, light_left=False),
             L(blob([(58, 14), (88, 36), (86, 68), (68, 86)], 6), 'shade', 'b', False)],
}
