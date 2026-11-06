"""IE2: jugadores sueltos de equipos que ya tenían casi todos dibujados (Emperadores Oscuros, Jóvenes Inazuma)."""
from chars import CHARS, L, OUTC, blob, ell, pal, sheen, spk, strand
from chars_otaku import back_hair
from chars_sallys import mustache
from heads import quad

SIDE_SKULL = [(44, 92), (22, 88), (12, 64), (14, 36), (30, 16), (56, 10), (78, 18), (88, 36), (76, 44), (60, 48), (52, 62), (50, 80)]
SKULL_B = [(16, 70), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 70), (66, 86), (34, 86)]
LONG_FACE = quad((20, 52), (18, 104), (50, 114)) + quad((50, 114), (82, 104), (80, 52))[1:] + quad((80, 52), (50, 26), (20, 52))[1:-1]

# ------------------------------------------------------------------ Shadow Cimmerian: piel morena, pelo gris plateado muy despeinado
# de pinchos que le caen sobre los ojos, ojeras oscuras y mirada sombría
SHADOW_TOP = [spk((8, 56), (12, 40), (-14, 50), 4), spk((22, 22), (42, 10), (14, -10), 5),
              spk((44, 8), (62, 10), (70, -18), 5, light_left=False), spk((76, 24), (90, 42), (110, 30), 4, light_left=False)]
CHARS['shadow-cimmerian'] = {
    'body': 'normal', 'pal': pal('#c8c4c4', '#b88a6a', shade='#9a8a8c', bag='#5a3a3a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 93, 'eye_y': 77, 'hairline': (62, 56)},
    'front': SHADOW_TOP + [L(blob([(8, 76), (6, 40), (18, 14), (50, 6), (82, 14), (94, 40), (92, 76), (80, 66), (20, 66)])),
                           L(blob([(62, 12), (92, 38), (90, 72), (80, 68)], 6), 'shade', 'b', False),
                           spk((10, 44), (28, 38), (16, 78), 5, z='f'), spk((26, 38), (44, 34), (36, 76), 5, z='f'),
                           spk((44, 34), (60, 34), (54, 74), 5, z='f'), spk((58, 36), (76, 40), (68, 76), 5, z='f', light_left=False),
                           spk((74, 42), (90, 46), (86, 78), 5, z='f', light_left=False),
                           L(quad((28, 84), (36, 87), (44, 84)), 'bag', 'f', False, False, 1.4), L(quad((56, 84), (64, 87), (72, 84)), 'bag', 'f', False, False, 1.4)],
    'side': [spk((16, 40), (24, 22), (-18, 16), 7), spk((24, 24), (42, 12), (8, -14), 7), spk((42, 12), (62, 6), (58, -18), 7),
             spk((14, 58), (16, 40), (-16, 50), 6), spk((18, 76), (22, 58), (-10, 82), 6),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((56, 30), (88, 40), (94, 78), 6, z='f', light_left=False)],
    'back': SHADOW_TOP + [L(blob([(8, 78), (6, 40), (18, 14), (50, 6), (82, 14), (94, 40), (92, 78), (66, 90), (34, 90)])),
                          spk((12, 76), (30, 88), (8, 100), 6), spk((30, 90), (50, 94), (38, 110), 6), spk((50, 94), (70, 90), (64, 110), 6, light_left=False),
                          spk((70, 88), (88, 76), (94, 100), 6, light_left=False),
                          L(blob([(58, 12), (92, 38), (90, 76), (66, 88)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Godric Wyles: adulto de cara muy alargada y pálida, melena verde
# azulado oscura ondulada con volumen que le enmarca la cara, ojos entornados y boca seria
CHARS['godric-wyles'] = {
    'body': 'delgado', 'pal': pal('#1e4a4a', '#e8d4a4'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 100, 'face_front': LONG_FACE, 'eye_y': 74,
             'hairline': [(14, 66), (26, 50), (40, 42), (58, 44), (74, 52), (86, 66)]},
    'front': [L(blob([(4, 92), (0, 50), (12, 14), (50, 2), (88, 14), (100, 50), (96, 92), (82, 88), (82, 64), (18, 64), (18, 88)])),
              L(blob([(62, 10), (98, 46), (94, 88), (84, 86)], 6), 'shade', 'b', False), sheen(22, 46, 14, 3),
              strand([(30, 16), (56, 10), (80, 28)], 'deep', 'b', 1.0), strand([(20, 40), (40, 24), (66, 26)], 'deep', 'b', 1.0),
              L(blob([(8, 56), (20, 56), (22, 86), (12, 92), (4, 76)]), 'mid', 'f'), L(blob([(92, 56), (80, 56), (78, 86), (88, 92), (96, 76)]), 'mid', 'f'),
              strand([(20, 58), (21, 86)], OUTC, 'f', 1.0), strand([(80, 58), (79, 86)], OUTC, 'f', 1.0)],
    'side': [L(blob([(54, 96), (14, 98), (0, 62), (4, 26), (26, 4), (58, 0), (84, 12), (96, 32), (92, 50), (76, 48), (62, 52), (58, 72), (58, 90)])),
             L(blob([(4, 46), (8, 90), (44, 94), (24, 66)], 6), 'shade', 'b', False), sheen(30, 62, 10, 3),
             strand([(88, 20), (54, 8), (20, 34), (14, 88)], 'deep', 'b', 1.0), spk((56, 28), (90, 36), (92, 58), 5, z='f', light_left=False)],
    'back': [L(blob([(4, 94), (0, 50), (12, 14), (50, 2), (88, 14), (100, 50), (96, 94), (50, 100)])),
             L(blob([(58, 10), (98, 46), (94, 92), (66, 98)], 6), 'shade', 'b', False), sheen(22, 46, 14, 3),
             strand([(36, 10), (30, 90)], 'deep', 'b', 1.0), strand([(64, 10), (70, 90)], 'deep', 'b', 1.0)],
}

# ------------------------------------------------------------------ David Evans (portero, el abuelo de Mark): adulto, pelo castaño
# oscuro recogido en una coleta, la cinta naranja de portero en la frente y bigote
CHARS['david-evans'] = {
    'body': 'normal', 'pal': pal('#4a2e1e', '#d8a060', band='#e8501a', band_d='#b0360a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'none', 'face_front': LONG_FACE, 'hairline': (54, 46)},
    'front': [L(blob([(14, 62), (12, 34), (24, 12), (50, 4), (76, 12), (88, 34), (86, 62)])),
              L(blob([(62, 12), (88, 34), (86, 60), (74, 56)], 6), 'shade', 'b', False), sheen(26, 50, 12, 3),
              L(blob([(34, 18), (50, 8), (66, 14), (54, 22)], 4), 'deep', 'b', False),
              L(blob([(10, 56), (8, 36), (22, 22), (50, 16), (78, 22), (92, 36), (90, 56), (50, 52)]), 'band', 'f', ln=True),
              L(quad((10, 50), (50, 42), (90, 50)) + quad((90, 56), (50, 52), (10, 56)), 'band_d', 'f', False),
              L(blob([(50, 18), (70, 22), (60, 34), (46, 30)], 4), 'band_d', 'f', False), mustache(90, 11)],
    'side': [L(blob([(40, 20), (52, 6), (66, 8), (60, 16), (50, 24)]), 'mid', 'b', ln=True),
             L(blob([(46, 74), (20, 72), (10, 50), (14, 26), (30, 10), (58, 4), (82, 14), (92, 32), (78, 38), (62, 40), (52, 54)])),
             L(blob([(14, 40), (18, 66), (38, 72), (28, 50)], 6), 'shade', 'b', False),
             L(blob([(10, 58), (10, 36), (26, 20), (56, 14), (82, 22), (94, 38), (92, 56), (50, 52)]), 'band', 'f', ln=True),
             L(blob([(82, 89), (94, 88), (94, 93), (84, 94)], 4), 'mid', 'f', ln=True)],
    'back': [L(blob(SKULL_B))] + back_hair() + [
             L(blob([(10, 60), (8, 36), (22, 22), (50, 16), (78, 22), (92, 36), (90, 60), (50, 62)]), 'band', 'f', ln=True),
             L(ell(50, 66, 6, 4), 'deep', 'f', ln=True)],
}
