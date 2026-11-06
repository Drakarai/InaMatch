"""Ichibangai Sally's (IE1): el equipo de los vecinos del barrio comercial; pelo, bigotes, gorros y gafas de cada uno, con sus
modelos 3D como referencia."""
from chars import CHARS, L, OUTC, blob, bumpy, dread, ell, fat, pal, sheen, spk, strand
from chars_otaku import back_hair, glasses, side_glass
from heads import quad

DARK = (30, 22, 24, 255)
WHITE = (255, 255, 255, 255)
SIDE_SKULL = [(44, 92), (22, 88), (12, 64), (14, 36), (30, 16), (56, 10), (78, 18), (88, 36), (76, 44), (60, 48), (52, 62), (50, 80)]


def mustache(y=86, w=12, c='mid', z='f'):
    return L(blob([(50 - w, y + 3), (44, y - 1.5), (50, y + 0.5), (56, y - 1.5), (50 + w, y + 3), (52, y + 4), (48, y + 4)], 5), c, z, ln=True)


def beard(c='mid'):
    """Barba que enmarca la cara de patilla a patilla."""
    return L(blob([(14, 62), (22, 62), (24, 84), (36, 96), (50, 100), (64, 96), (76, 84), (78, 62), (86, 62), (84, 92), (70, 106), (50, 112), (30, 106), (16, 92)]), c, 'f', ln=True)


# ------------------------------------------------------------------ Suzanne Yuma (portera): corpulenta, melena morada abombada y
# ondulada, ojos pequeños y labios rojos; cuello de camisa blanco
CHARS['suzanne-yuma'] = {
    'body': 'corpulento', 'pal': pal('#4a2a4a', '#f2b48c'),
    'face': {'eyes': 'dot', 'brows': True, 'mouth': 'smile', 'hairline': (56, 48)},
    'front': [L(bumpy(50, 40, 54, 36, 14, 0.08)), L(bumpy(70, 46, 22, 22, 8, 0.08), 'shade', 'b', False), L(ell(30, 20, 10, 4), 'light', 'b', False),
              L(blob([(6, 66), (4, 46), (96, 46), (94, 66), (80, 60), (20, 60)])),
              spk((20, 46), (40, 42), (28, 58), 4, z='f'), spk((40, 42), (60, 42), (50, 56), 4, z='f'), spk((60, 42), (80, 46), (72, 58), 4, z='f', light_left=False),
              L(ell(50, 92, 5, 2.6), (200, 50, 50, 255), 'f', ln=True)],
    'side': [L(bumpy(40, 40, 50, 36, 14, 0.08)), L(bumpy(22, 52, 22, 24, 8, 0.08), 'shade', 'b', False),
             L(blob(SIDE_SKULL)), spk((56, 30), (86, 40), (90, 60), 5, z='f', light_left=False)],
    'back': [L(bumpy(50, 44, 54, 40, 14, 0.08)), L(bumpy(70, 52, 22, 24, 8, 0.08), 'shade', 'b', False), L(ell(30, 22, 10, 4), 'light', 'b', False)],
}

# ------------------------------------------------------------------ T. Fielding: melena castaña clara, ancha y abombada hasta los
# hombros con puntas hacia fuera; nariz grande y sonrisa
CHARS['t-fielding'] = {
    'body': 'normal', 'pal': pal('#9a7462', '#f2c08e', nose='#d89a6a'),
    'face': {'eyes': 'sharp', 'mouth': 'smile', 'nose': (50, 82, 4.6), 'nose_side': (90, 80, 4.2), 'hairline': (62, 52)},
    'front': [L(blob([(0, 92), (-6, 60), (8, 22), (50, 8), (92, 22), (106, 60), (100, 92), (82, 86), (82, 62), (18, 62), (18, 86)])),
              spk((-4, 70), (8, 80), (-16, 94), 4), spk((92, 80), (104, 70), (116, 94), 4, light_left=False),
              L(blob([(62, 14), (98, 40), (98, 86), (84, 84)], 6), 'shade', 'b', False), sheen(22, 48, 20, 3),
              spk((14, 46), (36, 40), (22, 70), 5, z='f'), spk((34, 40), (56, 38), (46, 64), 5, z='f'),
              spk((54, 40), (74, 42), (66, 64), 4, z='f', light_left=False), spk((70, 44), (90, 50), (84, 72), 4, z='f', light_left=False)],
    'side': [L(blob([(48, 96), (12, 96), (-4, 62), (2, 30), (24, 8), (56, 4), (82, 16), (92, 36), (78, 46), (62, 50), (54, 64), (52, 86)])),
             L(blob([(4, 46), (6, 90), (38, 96), (22, 64)], 6), 'shade', 'b', False), spk((0, 80), (14, 92), (-10, 104), 4),
             spk((54, 24), (88, 36), (92, 74), 6, z='f', light_left=False)],
    'back': [L(blob([(0, 92), (-6, 60), (8, 22), (50, 8), (92, 22), (106, 60), (100, 92), (50, 100)])),
             spk((-4, 70), (8, 80), (-16, 94), 4), spk((92, 80), (104, 70), (116, 94), 4, light_left=False),
             L(blob([(58, 14), (98, 40), (98, 90), (66, 98)], 6), 'shade', 'b', False), sheen(22, 50, 20, 3)],
}

# ------------------------------------------------------------------ A. Lovely: media melena castaña rojiza abombada con flequillo
# recto, pecas y sonrisa
CHARS['a-lovely'] = {
    'body': 'chica', 'pal': pal('#7a3414', '#f6c88e', freckle='#c88a5a'),
    'face': {'eyes': 'big', 'mouth': 'smile', 'hairline': (60, 50)},
    'front': [L(blob([(4, 92), (0, 54), (12, 18), (50, 6), (88, 18), (100, 54), (96, 92), (82, 88), (82, 60), (18, 60), (18, 88)])),
              L(blob([(62, 12), (96, 44), (94, 88), (84, 86)], 6), 'shade', 'b', False), sheen(22, 46, 18, 3),
              L(blob([(14, 44), (30, 26), (50, 20), (70, 26), (86, 44), (86, 60), (14, 60)]), 'mid', 'f', ln=True),
              strand([(36, 40), (34, 58)], 'shade', 'f', 1.0), strand([(50, 38), (50, 58)], 'shade', 'f', 1.0), strand([(64, 40), (66, 58)], 'shade', 'f', 1.0)]
             + [L(ell(x, y, 1.1, 1.1), 'freckle', 'f', False) for x, y in ((26, 86), (30, 88), (74, 86), (70, 88))],
    'side': [L(blob([(48, 96), (12, 94), (0, 62), (4, 28), (24, 8), (56, 4), (82, 16), (92, 36), (90, 56), (66, 58), (56, 66), (54, 86)])),
             L(blob([(6, 46), (8, 88), (38, 94), (22, 64)], 6), 'shade', 'b', False),
             L(ell(76, 88, 1.1, 1.1), 'freckle', 'f', False)],
    'back': [L(blob([(4, 92), (0, 54), (12, 18), (50, 6), (88, 18), (100, 54), (96, 92), (50, 100)])),
             L(blob([(58, 12), (96, 44), (94, 90), (66, 98)], 6), 'shade', 'b', False), sheen(24, 50, 20, 3)],
}

# ------------------------------------------------------------------ Louis Hillside: corpulento, pelo verde muy oscuro peinado con
# raya y largo por detrás, bigote fino y perilla
CHARS['louis-hillside'] = {
    'body': 'corpulento', 'pal': pal('#24302a', '#b0703e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'hairline': (60, 46)},
    'front': [L(blob([(12, 72), (8, 40), (20, 14), (50, 6), (80, 14), (92, 40), (88, 72)])),
              L(blob([(60, 12), (90, 36), (88, 70), (74, 66)], 6), 'shade', 'b', False), sheen(28, 54, 14, 3),
              strand([(46, 8), (36, 44)], 'deep', 'b', 1.2),
              mustache(86, 10), L(blob([(46, 96), (54, 96), (52, 104), (48, 104)]), 'mid', 'f')],
    'side': [L(blob([(46, 96), (20, 96), (8, 66), (8, 34), (24, 10), (54, 4), (80, 14), (90, 34), (76, 40), (60, 44), (52, 60), (52, 80)])),
             L(blob([(12, 48), (14, 90), (40, 96), (26, 64)], 6), 'shade', 'b', False),
             L(blob([(82, 86), (92, 84), (92, 89), (84, 90)], 3), 'mid', 'f')],
    'back': [L(blob([(12, 72), (8, 40), (20, 14), (50, 6), (80, 14), (92, 40), (88, 72), (74, 86), (26, 86)]))] + back_hair(),
}

# ------------------------------------------------------------------ Ness Sheldon: corpulento, pelo morado oscuro de pinchos
# cortos y barba que le enmarca la cara; labios gruesos
CHARS['ness-sheldon'] = {
    'body': 'corpulento', 'pal': pal('#3a3240', '#c0844e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'lips', 'mouth_y': 92, 'mouth_w': 8, 'hairline': (58, 50)},
    'front': [L(blob([(16, 62), (14, 34), (26, 14), (50, 6), (74, 14), (86, 34), (84, 62)])),
              L(blob([(20, 20), (24, 2), (76, 2), (80, 20), (50, 14)])),
              L(blob([(60, 12), (86, 34), (84, 60), (70, 56)], 6), 'shade', 'b', False), beard()],
    'side': [L(blob([(46, 96), (22, 94), (12, 64), (16, 30), (30, 10), (56, 4), (80, 14), (88, 34), (76, 40), (60, 44), (54, 60), (54, 84)])),
             L(blob([(26, 18), (30, 0), (70, 0), (76, 16), (50, 12)])),
             L(blob([(54, 64), (62, 64), (64, 84), (78, 100), (92, 98), (90, 108), (72, 112), (56, 100)]), 'mid', 'f', ln=True)],
    'back': [L(blob([(16, 68), (14, 34), (26, 14), (50, 6), (74, 14), (86, 34), (84, 68), (66, 84), (34, 84)])),
             L(blob([(20, 20), (24, 2), (76, 2), (80, 20), (50, 14)]))] + back_hair(),
}

# ------------------------------------------------------------------ Ian Stager: gorro de lana marrón calado hasta las cejas, pelo
# negro de puntas que asoma por los lados, gafas redondas pequeñas y nariz larga
CHARS['ian-stager'] = {
    'body': 'normal', 'pal': pal('#2a2420', '#f6d2a6', hat='#6a5432', hat_d='#4a3a20'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'line', 'hairline': False},
    'front': [spk((8, 60), (18, 58), (0, 70), 3), spk((10, 66), (18, 68), (4, 80), 3), spk((82, 58), (92, 60), (100, 70), 3, light_left=False),
              spk((82, 68), (90, 66), (96, 80), 3, light_left=False),
              L(blob([(10, 62), (8, 32), (20, 12), (50, 4), (80, 12), (92, 32), (90, 62), (50, 58)]), 'hat', 'f', ln=True),
              L(blob([(60, 8), (90, 30), (90, 60), (74, 58)], 6), 'hat_d', 'f', False)]
             + [strand([(x, 10 + abs(x - 50) * 0.3), (x, 52)], 'hat_d', 'f', 0.9) for x in (26, 38, 50, 62, 74)]
             + [L(quad((10, 50), (50, 44), (90, 50)) + quad((90, 62), (50, 58), (10, 62)), 'hat_d', 'f', ln=True)] + glasses(74, 6, 5),
    'side': [spk((12, 62), (22, 60), (2, 70), 3), spk((14, 70), (24, 72), (6, 84), 3),
             L(blob(SIDE_SKULL)), L(blob([(12, 60), (10, 30), (26, 10), (54, 4), (80, 12), (92, 32), (90, 58), (50, 58)]), 'hat', 'f', ln=True),
             L(quad((12, 48), (50, 44), (92, 50)) + quad((92, 60), (50, 56), (12, 60)), 'hat_d', 'f', ln=True)] + side_glass(74),
    'back': [spk((8, 60), (18, 58), (0, 70), 3), spk((82, 58), (92, 60), (100, 70), 3, light_left=False),
             spk((14, 72), (32, 80), (8, 92), 4), spk((32, 80), (50, 82), (36, 96), 4), spk((50, 82), (68, 80), (64, 96), 4, light_left=False),
             spk((68, 80), (86, 72), (92, 92), 4, light_left=False),
             L(blob([(10, 66), (8, 32), (20, 12), (50, 4), (80, 12), (92, 32), (90, 66), (50, 72)]), 'hat', 'f', ln=True),
             L(quad((8, 54), (50, 50), (92, 54)) + quad((92, 66), (50, 62), (8, 66)), 'hat_d', 'f', ln=True)],
}

# ------------------------------------------------------------------ Lizzy Squirrel: moño alto castaño con mechones que caen junto
# a la cara, gafas finas y cara de enfado
CHARS['lizzy-squirrel'] = {
    'body': 'chica', 'pal': pal('#6e5244', '#f2c49a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'hairline': (62, 44), 'glasses': (90, 40, 40, 255)},
    'front': [L(bumpy(50, 8, 14, 10, 8, 0.08)),
              L(blob([(14, 66), (10, 40), (20, 16), (50, 8), (80, 16), (90, 40), (86, 66)])),
              L(blob([(60, 14), (88, 36), (86, 64), (72, 60)], 6), 'shade', 'b', False), sheen(28, 54, 16, 3),
              strand([(50, 10), (30, 40)], 'shade', 'b', 1.0), strand([(50, 10), (70, 40)], 'shade', 'b', 1.0),
              L(quad((18, 56), (14, 76), (22, 96)), 'mid', 'f', False, False, 2.4), L(quad((82, 56), (86, 76), (78, 96)), 'mid', 'f', False, False, 2.4)],
    'side': [L(bumpy(34, 6, 14, 10, 8, 0.08)),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             strand([(70, 20), (40, 18), (22, 40)], 'shade', 'b', 1.0), L(quad((56, 56), (52, 76), (60, 96)), 'mid', 'f', False, False, 2.4)],
    'back': [L(bumpy(50, 8, 14, 10, 8, 0.08)),
             L(blob([(14, 70), (10, 40), (20, 16), (50, 8), (80, 16), (90, 40), (86, 70), (66, 86), (34, 86)]))] + back_hair() + [
             strand([(50, 14), (40, 70)], 'shade', 'b', 1.0), strand([(50, 14), (60, 70)], 'shade', 'b', 1.0)],
}

# ------------------------------------------------------------------ Kippy Jones: anciano, pelo blanco grisáceo peinado hacia atrás
# con una onda, ojos cerrados con manchas oscuras, mentón largo
CHARS['kippy-jones'] = {
    'body': 'delgado', 'pal': pal('#d0c8c0', '#f6c69a'),
    'face': {'eyes': 'closed', 'brows': True, 'mouth': 'smile', 'mouth_y': 94, 'hairline': (56, 40)},
    'front': [L(blob([(16, 62), (14, 34), (26, 14), (50, 6), (74, 14), (86, 34), (84, 62)])),
              L(blob([(60, 12), (86, 34), (84, 60), (70, 56)], 6), 'shade', 'b', False),
              strand([(28, 34), (50, 22), (72, 34)], 'shade', 'b', 1.2), strand([(30, 26), (50, 16), (70, 26)], 'shade', 'b', 1.0),
              L(ell(36, 76, 7, 4), (60, 40, 40, 160), 'f', False), L(ell(64, 76, 7, 4), (60, 40, 40, 160), 'f', False)],
    'side': [L(blob([(44, 90), (22, 84), (14, 60), (16, 32), (30, 12), (56, 4), (80, 12), (88, 30), (74, 36), (60, 40), (52, 56), (50, 76)])),
             L(blob([(18, 46), (20, 72), (38, 84), (28, 58)], 6), 'shade', 'b', False),
             strand([(80, 16), (50, 10), (24, 30)], 'shade', 'b', 1.2), strand([(82, 24), (50, 20), (26, 46)], 'shade', 'b', 1.0)],
    'back': [L(blob([(16, 66), (14, 34), (26, 14), (50, 6), (74, 14), (86, 34), (84, 66), (66, 82), (34, 82)]))] + back_hair() + [
             strand([(40, 10), (38, 76)], 'shade', 'b', 1.0), strand([(60, 10), (62, 76)], 'shade', 'b', 1.0)],
}

# ------------------------------------------------------------------ F. Riversong: rastas castañas que salen hacia los lados y hacia
# atrás, gafas de sol redondas negras y bigote
CHARS['f-riversong'] = {
    'body': 'delgado', 'pal': pal('#5e3424', '#f2b07a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': (58, 50)},
    'front': [x for p0, p1 in (((22, 60), (-2, 64)), ((22, 70), (0, 80)), ((78, 60), (102, 64)), ((78, 70), (100, 80))) for x in dread(p0, p1, 4.4)]
             + [L(blob([(14, 64), (10, 38), (20, 14), (50, 4), (80, 14), (90, 38), (86, 64)])),
                L(blob([(60, 10), (88, 34), (86, 62), (72, 58)], 6), 'shade', 'b', False)]
             + [strand([(x, 8 + abs(x - 50) * 0.3), (x, 56)], 'deep', 'b', 1.1) for x in (26, 36, 46, 56, 66, 76)]
             + [L(ell(36, 74, 6, 5), DARK, 'f', ln=True), L(ell(64, 74, 6, 5), DARK, 'f', ln=True), L([(42, 73), (58, 73)], DARK, 'f', False, False, 1.4),
                L(ell(34, 72, 1.6, 1.2), (120, 120, 130, 255), 'f', False), L(ell(62, 72, 1.6, 1.2), (120, 120, 130, 255), 'f', False),
                mustache(88, 12)],
    'side': [x for p0, p1 in (((20, 40), (-8, 36)), ((18, 54), (-10, 58)), ((20, 68), (-6, 80)), ((30, 80), (6, 96))) for x in dread(p0, p1, 4.4)]
            + [L(blob(SIDE_SKULL))] + [strand([(70 - k * 10, 14 + k * 2), (30 - k * 4, 30 + k * 10)], 'deep', 'b', 1.1) for k in range(4)]
            + [L(ell(84, 74, 4, 5), DARK, 'f', ln=True), L([(80, 73), (54, 70)], DARK, 'f', False, False, 1.2),
               L(blob([(80, 86), (92, 84), (92, 90), (82, 90)], 3), 'mid', 'f')],
    'back': [L(blob([(12, 50), (88, 50), (96, 92), (50, 98), (4, 92)]), 'deep', 'b', False)]
            + [x for k in range(8) for x in dread((16 + k * 10, 50), (8 + k * 12, 92), 4.6)]
            + [L(blob([(14, 64), (10, 38), (20, 14), (50, 4), (80, 14), (90, 38), (86, 64), (50, 68)]))]
            + [strand([(x, 8), (x + (x - 50) * 0.2, 60)], 'deep', 'b', 1.1) for x in (26, 38, 50, 62, 74)],
}

# ------------------------------------------------------------------ Samantha Moonlight: melena verde oscura muy larga con rizos en
# las puntas y una diadema rosa; ojos grandes
CHARS['samantha-moonlight'] = {
    'body': 'chica', 'pal': pal('#2c4a36', '#f2c49a', band='#e8b0b0'),
    'face': {'eyes': 'big', 'mouth': 'smile', 'hairline': (62, 50)},
    'front': [L(blob([(2, 104), (-4, 60), (10, 20), (50, 8), (90, 20), (104, 60), (98, 104), (82, 98), (82, 62), (18, 62), (18, 98)])),
              L(bumpy(4, 96, 10, 10, 6, 0.1)), L(bumpy(96, 96, 10, 10, 6, 0.1)), L(bumpy(-2, 78, 9, 9, 6, 0.1)), L(bumpy(102, 78, 9, 9, 6, 0.1)),
              L(blob([(62, 14), (98, 44), (96, 96), (84, 94)], 6), 'shade', 'b', False), sheen(22, 46, 18, 3),
              L(quad((14, 30), (50, 12), (86, 30)) + quad((86, 36), (50, 18), (14, 36)), 'band', 'f', ln=True),
              spk((14, 46), (36, 40), (22, 68), 5, z='f'), spk((34, 40), (56, 38), (46, 62), 5, z='f'),
              spk((54, 40), (74, 42), (66, 62), 4, z='f', light_left=False), spk((70, 44), (90, 50), (86, 70), 4, z='f', light_left=False)],
    'side': [L(blob([(48, 100), (10, 104), (-6, 66), (0, 30), (22, 8), (56, 4), (82, 16), (92, 36), (78, 46), (62, 50), (54, 64), (52, 88)])),
             L(bumpy(6, 98, 11, 10, 6, 0.1)), L(bumpy(-4, 76, 9, 9, 6, 0.1)),
             L(blob([(4, 46), (6, 92), (38, 100), (22, 64)], 6), 'shade', 'b', False),
             L(quad((26, 12), (50, 4), (78, 14)) + quad((78, 20), (50, 10), (26, 18)), 'band', 'f', ln=True),
             spk((54, 24), (86, 34), (90, 72), 6, z='f', light_left=False)],
    'back': [L(blob([(2, 104), (-4, 60), (10, 20), (50, 8), (90, 20), (104, 60), (98, 104), (50, 112)])),
             L(bumpy(10, 104, 12, 10, 6, 0.1)), L(bumpy(50, 110, 14, 10, 6, 0.1)), L(bumpy(90, 104, 12, 10, 6, 0.1)),
             L(blob([(58, 14), (98, 44), (96, 100), (66, 108)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
             L(quad((12, 32), (50, 16), (88, 32)) + quad((88, 38), (50, 22), (12, 38)), 'band', 'f', ln=True)],
}

# ------------------------------------------------------------------ Eddie Prentice: tupé azul oscuro muy alto peinado hacia atrás,
# gafas de sol negras y barbilla larga
CHARS['eddie-prentice'] = {
    'body': 'delgado', 'pal': pal('#2e3a54', '#f2b884'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 94, 'hairline': (56, 44)},
    'front': [L(blob([(16, 60), (14, 30), (26, 4), (50, -10), (74, 4), (86, 30), (84, 60)])),
              L(blob([(60, 0), (86, 28), (84, 58), (70, 54)], 6), 'shade', 'b', False), sheen(30, 50, 2, 3),
              strand([(36, 4), (40, 44)], 'shade', 'b', 1.0), strand([(64, 4), (60, 44)], 'shade', 'b', 1.0),
              L(blob([(18, 70), (46, 70), (50, 74), (54, 70), (82, 70), (80, 80), (58, 82), (50, 78), (42, 82), (20, 80)], 4), DARK, 'f'),
              L(blob([(24, 72), (36, 71), (30, 75)], 3), (90, 90, 110, 255), 'f', False), L(blob([(64, 71), (76, 72), (70, 75)], 3), (90, 90, 110, 255), 'f', False)],
    'side': [L(blob([(46, 66), (30, 72), (16, 56), (16, 30), (30, 8), (60, -6), (92, 0), (104, 14), (90, 30), (72, 36), (62, 46)])),
             L(blob([(18, 40), (30, 12), (36, 60)], 6), 'shade', 'b', False), strand([(98, 8), (60, 4), (26, 28)], 'shade', 'b', 1.2),
             L(blob([(66, 70), (88, 70), (87, 79), (68, 78)], 4), DARK, 'f'), L([(66, 72), (50, 70)], DARK, 'f', False, False, 1.4)],
    'back': [L(blob([(16, 66), (14, 30), (26, 4), (50, -10), (74, 4), (86, 30), (84, 66), (50, 76)])),
             L(blob([(58, 0), (86, 28), (84, 64), (66, 74)], 6), 'shade', 'b', False), strand([(50, -6), (50, 60)], 'deep', 'b', 1.2),
             spk((34, 70), (50, 76), (40, 90), 3), spk((50, 76), (66, 70), (60, 90), 3, light_left=False)],
}

# ------------------------------------------------------------------ Mitch Sandstone: casi calvo, con un pañuelo claro atado en la
# frente (nudo y puntas a un lado), cejas pobladas, nariz grande y perilla
CHARS['mitch-sandstone'] = {
    'body': 'normal', 'pal': pal('#6a5a3a', '#f0b480', cloth='#e8d8c8', cloth_d='#b89a8a', nose='#d8946a'),
    'face': {'eyes': 'dot', 'brows': True, 'mouth': 'smile', 'nose': (50, 80, 5.6), 'nose_side': (91, 79, 5), 'hairline': False},
    'front': [L(blob([(16, 66), (14, 36), (26, 14), (50, 8), (74, 14), (86, 36), (84, 66)]), 'skin'),
              L(blob([(62, 14), (86, 36), (84, 64), (72, 60)], 6), 'skin_d', 'b', False),
              L(quad((12, 42), (50, 32), (88, 42)) + quad((88, 54), (50, 44), (12, 54)), 'cloth', 'f', ln=True),
              L(blob([(10, 44), (-4, 38), (-6, 52), (8, 54)], 4), 'cloth', 'f', ln=True), L(blob([(8, 50), (-4, 60), (2, 68), (12, 56)], 4), 'cloth_d', 'f', ln=True),
              L(blob([(44, 96), (56, 96), (54, 104), (46, 104)]), 'mid', 'f')],
    'side': [L(blob([(44, 92), (22, 88), (14, 64), (16, 36), (30, 16), (56, 10), (78, 18), (88, 40), (88, 62), (64, 56)]), 'skin'),
             L(quad((14, 40), (50, 30), (90, 42)) + quad((90, 54), (50, 42), (14, 52)), 'cloth', 'f', ln=True),
             L(blob([(16, 42), (0, 34), (-4, 50), (12, 52)], 4), 'cloth', 'f', ln=True),
             L(blob([(84, 96), (92, 96), (90, 102), (84, 102)]), 'mid', 'f')],
    'back': [L(blob([(16, 70), (14, 36), (26, 14), (50, 8), (74, 14), (86, 36), (84, 70), (66, 88), (34, 88)]), 'skin'),
             L(blob([(58, 14), (86, 36), (84, 68), (66, 86)], 6), 'skin_d', 'b', False),
             L(quad((10, 44), (50, 36), (90, 44)) + quad((90, 56), (50, 48), (10, 56)), 'cloth', 'f', ln=True),
             L(blob([(88, 44), (104, 38), (106, 52), (92, 54)], 4), 'cloth', 'f', ln=True), L(blob([(90, 50), (102, 60), (96, 68), (88, 56)], 4), 'cloth_d', 'f', ln=True)],
}

# ------------------------------------------------------------------ Alf Holmes (portero suplente): pelo castaño corto con raya a
# un lado, gafas rectangulares y cara seria
CHARS['alf-holmes'] = {
    'body': 'normal', 'pal': pal('#5a3a2a', '#f2c69c'),
    'face': {'eyes': 'sharp', 'mouth': 'frown', 'hairline': (60, 50), 'glasses': (30, 30, 40, 255), 'glasses_rect': True},
    'front': [L(blob([(14, 66), (10, 40), (20, 16), (50, 8), (80, 16), (90, 40), (86, 66)])),
              L(blob([(60, 14), (88, 36), (86, 64), (72, 60)], 6), 'shade', 'b', False), sheen(22, 46, 18, 3),
              spk((58, 22), (80, 36), (20, 62), 6, z='f'), spk((70, 40), (88, 48), (84, 66), 3, z='f', light_left=False)],
    'side': [L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((54, 26), (84, 36), (90, 60), 5, z='f', light_left=False)] + side_glass(75, (30, 30, 40, 255)),
    'back': [L(blob([(14, 70), (10, 40), (20, 16), (50, 8), (80, 16), (90, 40), (86, 70), (66, 86), (34, 86)]))] + back_hair(),
}

# ------------------------------------------------------------------ Fred Crumb: gorro de cocinero blanco, pelo castaño oscuro que
# asoma en puntas a los lados, ojos redondos y coloretes
CHARS['fred-crumb'] = {
    'body': 'normal', 'pal': pal('#3e3a22', '#f6c8a0', hat='#ece8e4', hat_d='#c8b8b0', blush='#f08a6a'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'frown', 'hairline': False},
    'front': [spk((8, 56), (20, 54), (2, 66), 4), spk((10, 64), (20, 66), (4, 78), 4), spk((80, 54), (92, 56), (98, 66), 4, light_left=False),
              spk((80, 66), (90, 64), (96, 78), 4, light_left=False),
              L(blob([(16, 58), (14, 30), (18, 4), (50, -6), (82, 4), (86, 30), (84, 58), (50, 54)]), 'hat', 'f', ln=True),
              L(blob([(60, 0), (84, 20), (84, 56), (70, 54)], 6), 'hat_d', 'f', False),
              L(quad((14, 46), (50, 40), (86, 46)) + quad((86, 58), (50, 52), (14, 58)), 'hat_d', 'f', ln=True),
              L(ell(28, 86, 5, 3), 'blush', 'f', False), L(ell(72, 86, 5, 3), 'blush', 'f', False)],
    'side': [spk((12, 60), (22, 58), (2, 68), 4), spk((14, 68), (24, 70), (6, 82), 4),
             L(blob(SIDE_SKULL)), L(blob([(16, 58), (14, 28), (22, 2), (54, -8), (82, 4), (88, 28), (86, 56), (50, 56)]), 'hat', 'f', ln=True),
             L(quad((14, 46), (50, 40), (88, 48)) + quad((88, 58), (50, 52), (14, 58)), 'hat_d', 'f', ln=True),
             L(ell(80, 86, 4, 2.6), 'blush', 'f', False)],
    'back': [spk((8, 60), (20, 58), (2, 70), 4), spk((80, 58), (92, 60), (98, 70), 4, light_left=False),
             spk((16, 70), (34, 80), (10, 90), 5), spk((34, 80), (50, 82), (40, 96), 5), spk((50, 82), (66, 80), (60, 96), 5, light_left=False),
             spk((66, 80), (84, 70), (90, 90), 5, light_left=False),
             L(blob([(16, 62), (14, 30), (18, 4), (50, -6), (82, 4), (86, 30), (84, 62), (50, 66)]), 'hat', 'f', ln=True),
             L(quad((14, 50), (50, 46), (86, 50)) + quad((86, 62), (50, 58), (14, 62)), 'hat_d', 'f', ln=True)],
}

# ------------------------------------------------------------------ Doug Baughan: anciano, pelo canoso peinado hacia atrás, arrugas
# en la frente, ojos pequeños y sonrisa amable
CHARS['doug-baughan'] = {
    'body': 'normal', 'pal': pal('#b8a090', '#f2b884'),
    'face': {'eyes': 'dot', 'brows': True, 'mouth': 'smile', 'hairline': (50, 34)},
    'front': [L(blob([(16, 60), (14, 32), (26, 12), (50, 6), (74, 12), (86, 32), (84, 60)])),
              L(blob([(60, 10), (86, 32), (84, 58), (70, 54)], 6), 'shade', 'b', False),
              strand([(36, 10), (34, 34)], 'shade', 'b', 1.0), strand([(50, 8), (50, 32)], 'shade', 'b', 1.0), strand([(64, 10), (66, 34)], 'shade', 'b', 1.0),
              L(quad((36, 46), (50, 43), (64, 46)), 'skin_d', 'f', False, False, 1.0), L(quad((38, 51), (50, 48), (62, 51)), 'skin_d', 'f', False, False, 1.0)],
    'side': [L(blob([(44, 90), (22, 84), (14, 60), (16, 32), (30, 12), (56, 4), (78, 10), (84, 24), (70, 30), (58, 34), (52, 50), (50, 76)])),
             L(blob([(18, 44), (20, 72), (38, 84), (28, 56)], 6), 'shade', 'b', False),
             strand([(76, 12), (50, 8), (24, 30)], 'shade', 'b', 1.0), strand([(78, 20), (50, 18), (26, 46)], 'shade', 'b', 1.0)],
    'back': [L(blob([(16, 66), (14, 32), (26, 12), (50, 6), (74, 12), (86, 32), (84, 66), (66, 84), (34, 84)]))] + back_hair() + [
             strand([(40, 10), (38, 76)], 'shade', 'b', 1.0), strand([(60, 10), (62, 76)], 'shade', 'b', 1.0)],
}

# ------------------------------------------------------------------ Pip Daltry: pelo malva recogido en una coleta lateral, con un
# mechón que cae junto a la cara; ojos grandes
CHARS['pip-daltry'] = {
    'body': 'chica', 'pal': pal('#9a7484', '#f6d0ac'),
    'face': {'eyes': 'big', 'mouth': 'smile', 'hairline': (62, 52)},
    'front': [L(blob([(82, 60), (98, 66), (98, 96), (90, 110), (84, 96)])),
              L(blob([(12, 70), (8, 42), (20, 16), (50, 8), (80, 16), (92, 42), (88, 70)])),
              L(blob([(60, 14), (90, 38), (88, 68), (74, 64)], 6), 'shade', 'b', False), sheen(22, 46, 18, 3),
              spk((14, 46), (36, 40), (20, 70), 5, z='f'), spk((34, 40), (56, 38), (44, 62), 5, z='f'),
              spk((54, 40), (72, 42), (64, 62), 4, z='f', light_left=False), spk((70, 44), (88, 50), (84, 74), 4, z='f', light_left=False)],
    'side': [L(blob([(30, 50), (14, 50), (4, 70), (6, 98), (16, 104), (18, 78), (30, 64)])),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             L([(26, 52), (30, 62)], (180, 80, 80, 255), 'b', False, False, 1.6),
             spk((54, 26), (84, 36), (90, 70), 6, z='f', light_left=False)],
    'back': [L(blob([(12, 76), (8, 42), (20, 16), (50, 8), (80, 16), (92, 42), (88, 76), (50, 84)]))] + back_hair() + [
             L(blob([(20, 66), (32, 66), (30, 96), (22, 110), (16, 96)]), 'mid', 'f', ln=True)],
}
