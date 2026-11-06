"""Kidokawa Seishuu / Instituto Kirkwood (IE1): rastas con pañuelo, tupés, crestas de los trillizos Murdock con sus gafas
de sol y demás peinados, con sus modelos 3D como referencia."""
from chars import CHARS, L, OUTC, blob, bumpy, dread, ell, pal, sheen, spk, strand
from chars_otaku import back_hair
from chars_sengoku import wavy
from heads import quad

WHITE = (255, 255, 255, 255)
SIDE_SKULL = [(44, 92), (22, 88), (12, 64), (14, 36), (30, 16), (56, 10), (78, 18), (88, 36), (76, 44), (60, 48), (52, 62), (50, 80)]
SKULL_F = [(16, 64), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 64)]
SKULL_B = [(16, 70), (14, 36), (26, 14), (50, 6), (74, 14), (86, 36), (84, 70), (66, 86), (34, 86)]


def zigzag(y=92, x0=42, x1=58, n=6, h=1.6):
    """Boca temblorosa en zigzag."""
    pts = [(x0 + (x1 - x0) * i / n, y + (h if i % 2 else -h) * 0.5) for i in range(n + 1)]
    return L(pts, (130, 70, 50, 255), 'f', False, False, 1.3)


def shades(lens, frame, y=76):
    """Gafas de sol de los Murdock: dos cristales anchos e inclinados con la montura gruesa."""
    left = [(20, y - 6), (45, y - 3), (44, y + 5), (24, y + 6)]
    right = [(100 - x, yy) for x, yy in left][::-1]
    out = []
    for g in (left, right):
        out += [L(g, frame, 'f', True), L(blob(g, 4), lens, 'f', False), L(g + [g[0]], frame, 'f', False, False, 1.8)]
    return out + [L([(45, y - 2), (55, y - 2)], frame, 'f', False, False, 1.8), L([(20, y - 5), (14, y - 6)], frame, 'f', False, False, 1.8),
                  L([(80, y - 5), (86, y - 6)], frame, 'f', False, False, 1.8)]


def side_shades(lens, frame, y=76):
    g = [(78, y - 5), (92, y - 4), (91, y + 5), (80, y + 6)]
    return [L(g, lens, 'f', True), L(g + [g[0]], frame, 'f', False, False, 1.8), L([(78, y - 4), (50, y - 6)], frame, 'f', False, False, 1.8)]


def bald(f='front'):
    """Cabeza rapada de los trillizos: el cráneo es piel."""
    if f == 'front':
        return [L(blob(SKULL_F), 'skin'), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'skin_d', 'b', False)]
    if f == 'side':
        return [L(blob(SIDE_SKULL), 'skin')]
    return [L(blob(SKULL_B), 'skin'), L(blob([(58, 12), (86, 36), (84, 68), (66, 84)], 6), 'skin_d', 'b', False)]


# ------------------------------------------------------------------ John Neville (portero): corpulento, pelo castaño tupido y
# abombado solo arriba (como una boina) con los lados rapados, ojos redondos de susto, boca temblorosa y coloretes naranjas
CHARS['john-neville'] = {
    'body': 'corpulento', 'pal': pal('#7a4220', '#f6b878', shave='#7a6656', blush='#f07a3a'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'none', 'big_ears': 1, 'ear_out': 2, 'hairline': (52, 44)},
    'front': [L(blob([(14, 64), (12, 40), (24, 22), (50, 16), (76, 22), (88, 40), (86, 64)]), 'shave'),
              L(bumpy(50, 22, 38, 15, 10, 0.08)), L(bumpy(62, 24, 20, 10, 6, 0.08), 'shade', 'b', False),
              strand([(30, 22), (44, 14)], 'deep', 'b', 1.0), strand([(52, 26), (68, 16)], 'deep', 'b', 1.0),
              zigzag(92), L([(24, 84), (30, 82)], 'blush', 'f', False, False, 1.4), L([(25, 87), (31, 85)], 'blush', 'f', False, False, 1.4),
              L([(76, 84), (70, 82)], 'blush', 'f', False, False, 1.4), L([(75, 87), (69, 85)], 'blush', 'f', False, False, 1.4)],
    'side': [L(blob(SIDE_SKULL), 'shave'),
             L(bumpy(46, 22, 42, 15, 10, 0.08)), L(bumpy(30, 26, 18, 10, 6, 0.08), 'shade', 'b', False),
             strand([(30, 20), (60, 14)], 'deep', 'b', 1.0),
             L([(80, 84), (85, 82)], 'blush', 'f', False, False, 1.4)],
    'back': [L(blob(SKULL_B), 'shave'), L(blob([(58, 30), (86, 40), (84, 68), (66, 84)], 6), tuple(int(v * 0.85) for v in (122, 102, 86)) + (255,), 'b', False),
             L(bumpy(50, 22, 38, 15, 10, 0.08)), L(bumpy(62, 24, 20, 10, 6, 0.08), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Malcolm Night: piel morena, rastas verde oliva que asoman
# por encima de un pañuelo gris azulado muy grueso, dos rastas a cada lado de la cara y el resto recogidas en una coleta
MAL_BAND_F = blob([(10, 58), (8, 38), (18, 26), (50, 22), (82, 26), (92, 38), (90, 58), (50, 54)])
CHARS['malcolm-night'] = {
    'body': 'normal', 'pal': pal('#7a8040', '#d8904a', band='#5e8c96', band_d='#3e6670', tie='#e8a0a0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': False},
    'front': [x for k in range(7) for x in dread((22 + k * 9.3, 30), (22 + k * 9.3, 10 + abs(k - 3) * 2), 4.6)]
             + [L(MAL_BAND_F, 'band', 'f', ln=True), L(blob([(54, 24), (82, 26), (92, 38), (90, 58), (60, 54)], 6), 'band_d', 'f', False),
                L(quad((14, 44), (40, 36), (60, 42)), 'band_d', 'f', False, False, 1.2), L(quad((40, 50), (66, 42), (86, 48)), 'band_d', 'f', False, False, 1.2)]
             + [x for p0, p1 in (((16, 56), (15, 94)), ((24, 58), (23, 90)), ((84, 56), (85, 94)), ((76, 58), (77, 90))) for x in dread(p0, p1, 3.8, 'f')],
    'side': [x for p0, p1 in (((22, 58), (2, 84)), ((18, 62), (-4, 92)), ((26, 62), (8, 96))) for x in dread(p0, p1, 4.4)]
            + [L(ell(18, 60, 4, 4), 'tie', 'b', ln=True), L(blob(SIDE_SKULL), 'shade')]
            + [x for k in range(6) for x in dread((26 + k * 10, 26), (24 + k * 10, 10 + abs(k - 2) * 2), 4.6)]
            + [L(blob([(10, 56), (8, 38), (20, 24), (54, 20), (84, 26), (94, 40), (92, 58), (50, 56)]), 'band', 'f', ln=True),
               L(blob([(10, 56), (8, 38), (20, 26), (30, 56)], 6), 'band_d', 'f', False)]
            + dread((58, 58), (58, 92), 3.8, 'f'),
    'back': [x for k in range(7) for x in dread((22 + k * 9.3, 30), (22 + k * 9.3, 10 + abs(k - 3) * 2), 4.6)]
            + [L(blob(SKULL_B), 'shade'), L(MAL_BAND_F, 'band', 'f', ln=True),
               L(blob([(54, 24), (82, 26), (92, 38), (90, 58), (60, 54)], 6), 'band_d', 'f', False)]
            + [x for p0, p1 in (((44, 64), (40, 106)), ((56, 64), (60, 106)), ((50, 64), (50, 110))) for x in dread(p0, p1, 4.0, 'f')]
            + [L(ell(50, 64, 7, 3.6), 'tie', 'f', ln=True)]
            + [x for p0, p1 in (((14, 56), (14, 90)), ((86, 56), (86, 90))) for x in dread(p0, p1, 3.8, 'f')],
}

# ------------------------------------------------------------------ Alfred Meenan: piel muy clara, media melena malva grisácea
# despeinada con mechones que le caen sobre un ojo; ojos grises con pestañas
CHARS['alfred-meenan'] = {
    'body': 'normal', 'pal': pal('#7a5a68', '#fbe4d4', iris='#8a7a84'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'line', 'mouth_y': 93, 'hairline': (60, 50)},
    'front': [L(blob([(8, 84), (4, 48), (14, 16), (50, 4), (86, 16), (96, 48), (92, 84), (82, 80), (82, 60), (18, 60), (18, 80)])),
              spk((4, 66), (12, 80), (-8, 86), 3), spk((88, 80), (96, 66), (108, 86), 3, light_left=False),
              L(blob([(62, 12), (94, 46), (92, 82), (84, 80)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
              strand([(50, 6), (44, 30)], 'deep', 'b', 1.0),
              spk((12, 44), (30, 36), (16, 74), 5, z='f'), spk((26, 38), (46, 34), (34, 70), 5, z='f'),
              spk((44, 34), (62, 36), (60, 82), 6, z='f', light_left=False), spk((66, 38), (88, 44), (86, 76), 5, z='f', light_left=False)],
    'side': [L(blob([(48, 94), (14, 92), (2, 62), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (92, 58), (76, 56), (62, 58), (56, 74), (52, 90)])),
             spk((6, 78), (18, 90), (0, 98), 3), spk((24, 90), (42, 94), (30, 104), 3),
             L(blob([(6, 50), (8, 88), (40, 92), (24, 64)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             spk((56, 30), (88, 40), (92, 82), 6, z='f', light_left=False), spk((50, 54), (62, 54), (56, 84), 3, z='f')],
    'back': [L(blob([(8, 84), (4, 48), (14, 16), (50, 4), (86, 16), (96, 48), (92, 84), (50, 90)])),
             spk((4, 66), (12, 80), (-8, 86), 3), spk((88, 80), (96, 66), (108, 86), 3, light_left=False),
             spk((14, 82), (32, 88), (14, 100), 4), spk((32, 88), (50, 90), (40, 102), 4), spk((50, 90), (68, 88), (60, 102), 4, light_left=False),
             spk((68, 88), (86, 82), (86, 100), 4, light_left=False),
             L(blob([(58, 12), (94, 46), (92, 82), (66, 88)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
             strand([(50, 8), (40, 50), (36, 84)], 'deep', 'b', 1.0)],
}

# ------------------------------------------------------------------ Dan Mirthful: corpulento, piel morena, pelo castaño verdoso
# como un casco con un pico sobre la frente y que sobresale por delante; mirada de enfado y marcas en las mejillas
CHARS['dan-mirthful'] = {
    'body': 'corpulento', 'pal': pal('#5a5432', '#b86a2a', mark='#5a2a10'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93, 'hairline': (58, 48)},
    'front': [L(blob([(10, 64), (8, 36), (20, 14), (50, 6), (80, 14), (92, 36), (90, 64), (80, 56), (20, 56)])),
              spk((6, 52), (14, 62), (-6, 66), 3), spk((86, 62), (94, 52), (106, 66), 3, light_left=False),
              L(blob([(62, 12), (90, 36), (88, 62), (76, 56)], 6), 'shade', 'b', False), sheen(24, 48, 16, 3),
              spk((36, 36), (64, 36), (50, 62), 5, z='f'), spk((14, 40), (34, 38), (20, 60), 4, z='f'),
              spk((66, 38), (86, 40), (82, 60), 4, z='f', light_left=False),
              L([(25, 84), (32, 86)], 'mark', 'f', False, False, 1.2), L([(26, 89), (32, 89)], 'mark', 'f', False, False, 1.2),
              L([(75, 84), (68, 86)], 'mark', 'f', False, False, 1.2), L([(74, 89), (68, 89)], 'mark', 'f', False, False, 1.2)],
    'side': [L(blob([(44, 86), (16, 80), (6, 56), (10, 26), (32, 6), (64, 4), (92, 14), (104, 34), (96, 44), (78, 42), (62, 46), (52, 62)])),
             L(blob([(8, 44), (12, 76), (36, 82), (22, 58)], 6), 'shade', 'b', False), sheen(30, 64, 12, 3),
             strand([(96, 22), (60, 14), (24, 34)], 'shade', 'b', 1.1),
             L([(78, 84), (84, 86)], 'mark', 'f', False, False, 1.2), L([(78, 89), (84, 89)], 'mark', 'f', False, False, 1.2)],
    'back': [L(blob([(10, 70), (8, 36), (20, 14), (50, 6), (80, 14), (92, 36), (90, 70), (70, 82), (30, 82)])),
             spk((6, 52), (14, 62), (-6, 66), 3), spk((86, 62), (94, 52), (106, 66), 3, light_left=False)] + back_hair(),
}

# ------------------------------------------------------------------ Ricky Clover: delgado, tupé azul marino altísimo y plano que
# sube recto desde la frente; ojos redondos de enfado, orejas grandes y un bigote enorme sobre la boca
RICKY_HAIR_F = blob([(26, 52), (24, 20), (26, -10), (30, -34), (50, -38), (70, -34), (74, -10), (76, 20), (74, 52), (50, 48)])
CHARS['ricky-clover'] = {
    'body': 'delgado', 'pal': pal('#2a4466', '#f0b070', stache='#9a5a3a', stache_d='#7a4228'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'big_ears': 1.5, 'ear_out': 2, 'hairline': (58, 48)},
    'front': [L(RICKY_HAIR_F), L(blob([(58, -32), (70, -32), (76, 20), (74, 50), (62, 48)], 6), 'shade', 'b', False),
              strand([(38, -32), (36, 40)], 'deep', 'b', 1.0), strand([(50, -36), (50, 40)], 'light', 'b', 1.2),
              L(blob([(32, 90), (40, 82), (50, 80), (60, 82), (68, 90), (50, 89)], 5), 'stache', 'f', ln=True),
              L(blob([(50, 81), (60, 83), (68, 90), (52, 89)], 4), 'stache_d', 'f', False)],
    'side': [L(blob([(28, 72), (10, 50), (6, 20), (12, -6), (24, -32), (46, -36), (62, -24), (80, 6), (90, 30), (80, 44), (60, 46), (52, 62), (48, 80)])),
             L(blob([(8, 20), (14, -10), (26, -30), (30, 30), (24, 66)], 6), 'shade', 'b', False),
             strand([(40, -30), (64, 20)], 'light', 'b', 1.2),
             L(blob([(82, 84), (94, 82), (98, 90), (86, 91)], 4), 'stache', 'f', ln=True)],
    'back': [L(blob([(28, 74), (24, 20), (26, -10), (30, -34), (50, -38), (70, -34), (74, -10), (76, 20), (72, 74), (50, 94)])),
             L(blob([(56, -32), (70, -32), (76, 20), (72, 72), (54, 90)], 6), 'shade', 'b', False),
             strand([(50, -34), (50, 90)], 'deep', 'b', 1.0)],
}

# ------------------------------------------------------------------ Toby Damian: piel tostada, lados rapados grises y por arriba
# pelo castaño oscuro de pinchos barridos hacia un lado que caen sobre la frente; ojos redondos y sonrisa
CHARS['toby-damian'] = {
    'body': 'normal', 'pal': pal('#3a3a26', '#d8a058', shave='#6a6a5e', mark='#7a4a20'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'smile', 'mouth_y': 92, 'hairline': (56, 48)},
    'front': [L(blob(SKULL_F), 'shave'),
              spk((34, 18), (56, 10), (74, -8), 7, light_left=False),
              spk((54, 12), (76, 20), (98, 8), 7, light_left=False), spk((70, 24), (86, 36), (104, 36), 6, light_left=False),
              L(blob([(20, 40), (30, 20), (50, 12), (74, 18), (86, 34), (84, 50), (60, 44), (40, 42)])),
              L(blob([(60, 18), (84, 32), (84, 50), (66, 44)], 6), 'shade', 'b', False),
              spk((52, 36), (76, 38), (82, 66), 6, z='f', light_left=False), spk((34, 40), (52, 38), (44, 56), 4, z='f'),
              L([(26, 84), (31, 86)], 'mark', 'f', False, False, 1.1), L([(74, 84), (69, 86)], 'mark', 'f', False, False, 1.1)],
    'side': [L(blob(SIDE_SKULL), 'shave'),
             spk((20, 24), (40, 10), (6, -10), 7), spk((40, 10), (62, 8), (56, -16), 7, light_left=False),
             L(blob([(18, 30), (34, 10), (60, 6), (82, 14), (92, 30), (80, 40), (50, 34), (30, 40)])),
             spk((60, 22), (86, 28), (96, 56), 6, z='f', light_left=False),
             L([(78, 84), (82, 86)], 'mark', 'f', False, False, 1.1)],
    'back': [L(blob(SKULL_B), 'shave'),
             spk((42, 10), (62, 16), (30, -10), 7), spk((24, 20), (44, 12), (8, 2), 7),
             L(blob([(80, 40), (70, 20), (50, 12), (26, 18), (14, 34), (16, 50), (40, 44), (60, 42)])),
             L(blob([(40, 18), (16, 32), (16, 50), (34, 44)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ York Nashmith: pelo verde oscuro de pinchos hacia arriba y
# hacia los lados, con mechones de punta sobre la frente; ojos redondos y boca temblorosa
CHARS['york-nashmith'] = {
    'body': 'normal', 'pal': pal('#3a5a1e', '#fcd8b4'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'none', 'hairline': (60, 50)},
    'front': [spk((10, 46), (18, 28), (-4, 22), 7), spk((22, 22), (40, 12), (24, -16), 7),
              spk((40, 12), (58, 10), (52, -22), 7), spk((58, 12), (76, 18), (80, -14), 7, light_left=False),
              spk((80, 26), (90, 46), (106, 20), 7, light_left=False), spk((8, 60), (12, 46), (-4, 62), 4), spk((88, 46), (92, 60), (104, 62), 4, light_left=False),
              L(blob([(10, 70), (8, 40), (20, 16), (50, 8), (80, 16), (92, 40), (90, 70), (80, 64), (20, 64)])),
              L(blob([(62, 14), (90, 38), (88, 66), (78, 62)], 6), 'shade', 'b', False),
              spk((12, 44), (30, 38), (18, 74), 5, z='f'), spk((28, 40), (46, 36), (36, 62), 4, z='f'),
              spk((54, 36), (72, 40), (64, 62), 4, z='f', light_left=False), spk((70, 38), (88, 44), (84, 74), 5, z='f', light_left=False),
              zigzag(92, 44, 56, 4)],
    'side': [spk((16, 40), (24, 24), (-16, 22), 7), spk((24, 26), (40, 14), (8, -12), 7), spk((40, 14), (60, 8), (52, -18), 7),
             spk((14, 56), (16, 40), (-14, 54), 6), spk((18, 70), (22, 58), (-6, 80), 5),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((60, 14), (80, 22), (98, 4), 6, light_left=False),
             spk((56, 30), (88, 40), (92, 72), 6, z='f', light_left=False), spk((50, 54), (60, 54), (56, 76), 2.5, z='f')],
    'back': [spk((10, 46), (18, 28), (-4, 22), 7), spk((22, 22), (40, 12), (24, -16), 7),
             spk((40, 12), (58, 10), (52, -22), 7), spk((58, 12), (76, 18), (80, -14), 7, light_left=False),
             spk((80, 26), (90, 46), (106, 20), 7, light_left=False), spk((8, 60), (12, 46), (-4, 62), 4), spk((88, 46), (92, 60), (104, 62), 4, light_left=False),
             L(blob([(10, 72), (8, 40), (20, 16), (50, 8), (80, 16), (92, 40), (90, 72), (66, 84), (34, 84)])),
             spk((14, 72), (32, 82), (10, 94), 4), spk((32, 82), (50, 86), (40, 100), 4), spk((50, 86), (68, 82), (62, 100), 4, light_left=False),
             spk((68, 82), (86, 72), (90, 94), 4, light_left=False),
             L(blob([(58, 14), (90, 38), (88, 70), (66, 82)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Zachary Moore: pelo castaño rojizo muy oscuro de pinchos
# finos en todas direcciones, como un erizo; ojos pequeños y cara tranquila
ZACH_TOP = [spk((6, 60), (10, 42), (-14, 54), 6), spk((10, 44), (20, 26), (-12, 24), 6), spk((18, 28), (32, 14), (4, -6), 6),
            spk((30, 14), (46, 8), (28, -18), 6), spk((44, 8), (58, 8), (50, -22), 6), spk((56, 8), (72, 14), (74, -18), 6, light_left=False),
            spk((70, 14), (84, 26), (98, -4), 6, light_left=False), spk((82, 28), (92, 44), (114, 26), 6, light_left=False),
            spk((90, 44), (94, 62), (114, 58), 5, light_left=False)]
CHARS['zachary-moore'] = {
    'body': 'normal', 'pal': pal('#5a1e14', '#f6bc80'),
    'face': {'eyes': 'dot', 'brows': True, 'mouth': 'line', 'mouth_y': 92, 'hairline': (60, 50)},
    'front': ZACH_TOP + [L(blob([(8, 70), (6, 40), (18, 16), (50, 6), (82, 16), (94, 40), (92, 70), (80, 64), (20, 64)])),
                         L(blob([(62, 12), (92, 38), (90, 66), (78, 62)], 6), 'shade', 'b', False),
                         spk((12, 44), (28, 36), (16, 70), 4, z='f'), spk((26, 36), (42, 32), (34, 60), 4, z='f'),
                         spk((40, 32), (56, 30), (50, 58), 4, z='f'), spk((56, 32), (72, 36), (66, 60), 4, z='f', light_left=False),
                         spk((72, 36), (88, 44), (84, 70), 4, z='f', light_left=False)],
    'side': [spk((16, 40), (24, 24), (-18, 22), 7), spk((24, 26), (40, 14), (6, -14), 7), spk((40, 14), (60, 8), (48, -20), 7),
             spk((14, 56), (16, 40), (-18, 52), 6), spk((16, 72), (20, 58), (-12, 80), 6), spk((24, 84), (26, 72), (4, 96), 5),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((60, 14), (80, 22), (96, 0), 6, light_left=False),
             spk((56, 30), (88, 40), (92, 66), 6, z='f', light_left=False)],
    'back': ZACH_TOP + [L(blob([(8, 72), (6, 40), (18, 16), (50, 6), (82, 16), (94, 40), (92, 72), (66, 86), (34, 86)])),
                        spk((12, 72), (30, 82), (6, 96), 5), spk((30, 84), (50, 88), (38, 104), 5), spk((50, 88), (70, 84), (64, 104), 5, light_left=False),
                        spk((70, 82), (88, 72), (94, 96), 5, light_left=False),
                        L(blob([(58, 12), (92, 38), (90, 70), (66, 84)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Los trillizos Murdock: cabeza rapada, labios gruesos, nariz
# redonda y gafas de sol de montura gruesa; cada uno con su cresta: Marvin, una cresta corta de púas moradas
MURDOCK = {'body': 'normal', 'face': {'eyes': 'none', 'brows': False, 'mouth': 'lips', 'mouth_y': 93, 'mouth_w': 7, 'nose': (50, 84, 4),
                                       'nose_side': (91, 82, 3.6), 'big_ears': 1, 'hairline': False}}
CHARS['marvin-murdock'] = dict(MURDOCK, **{
    'pal': pal('#5a4a5e', '#f0b070', nose='#c8804a', lens='#d07a1a', frame='#f2f2f2'),
    'front': [spk((36, 16), (44, 12), (34, -6), 3), spk((42, 12), (50, 10), (44, -10), 3), spk((48, 10), (56, 12), (56, -10), 3, light_left=False),
              spk((54, 12), (62, 16), (66, -6), 3, light_left=False)] + bald('front') + shades('lens', 'frame'),
    'side': [spk((50, 10), (60, 12), (64, -4), 3, light_left=False), spk((38, 10), (50, 8), (46, -10), 3), spk((26, 14), (38, 10), (26, -6), 3),
             spk((16, 22), (28, 14), (10, 2), 3)] + bald('side') + side_shades('lens', 'frame'),
    'back': [spk((36, 16), (44, 12), (34, -6), 3), spk((42, 12), (50, 10), (44, -10), 3), spk((48, 10), (56, 12), (56, -10), 3, light_left=False),
             spk((54, 12), (62, 16), (66, -6), 3, light_left=False), spk((42, 18), (58, 18), (50, 30), 3)] + bald('back'),
})

# ------------------------------------------------------------------ Thomas Murdock: pelo castaño rosado solo en lo alto, con raya
# en medio y dos mechones curvados hacia las sienes; gafas de cristal gris
THOMAS_TOP = blob([(16, 44), (18, 24), (34, 12), (50, 14), (66, 12), (82, 24), (84, 44), (72, 34), (54, 26), (46, 26), (28, 34)])
CHARS['thomas-murdock'] = dict(MURDOCK, **{
    'pal': pal('#8a5a50', '#f0b070', nose='#c8804a', lens='#9aa0a8', frame='#5a7480'),
    'front': bald('front') + [L(THOMAS_TOP, 'mid', 'f', ln=True), L(blob([(54, 16), (66, 14), (82, 24), (84, 42), (68, 30)], 6), 'shade', 'f', False),
                              strand([(26, 30), (40, 18)], 'deep', 'f', 1.0), strand([(74, 30), (60, 18)], 'deep', 'f', 1.0),
                              strand([(50, 14), (50, 26)], OUTC, 'f', 1.0)] + shades('lens', 'frame'),
    'side': bald('side') + [L(blob([(14, 40), (20, 20), (40, 8), (62, 8), (82, 16), (90, 30), (70, 26), (44, 26), (24, 40)]), 'mid', 'f', ln=True),
                            strand([(80, 18), (50, 14), (24, 30)], 'deep', 'f', 1.0)] + side_shades('lens', 'frame'),
    'back': bald('back') + [L(blob([(16, 40), (18, 22), (34, 10), (50, 12), (66, 10), (82, 22), (84, 40), (66, 30), (50, 32), (34, 30)]), 'mid', 'f', ln=True),
                            L(blob([(54, 14), (66, 12), (82, 22), (84, 38), (68, 28)], 6), 'shade', 'f', False)],
})

# ------------------------------------------------------------------ Tyler Murdock: una cresta verde oscura corta y puntiaguda en
# lo alto; gafas rosas
CHARS['tyler-murdock'] = dict(MURDOCK, **{
    'pal': pal('#24503a', '#f0b070', nose='#c8804a', lens='#a87a88', frame='#f0b0c4'),
    'front': spk((40, 16), (60, 16), (50, -10), 3) + bald('front') + shades('lens', 'frame'),
    'side': [L(blob([(14, 34), (24, 14), (46, 4), (70, 6), (86, 18), (62, 14), (40, 18), (22, 34)]), 'mid', 'b', ln=True),
             L(blob([(24, 22), (46, 8), (70, 8), (46, 14)], 4), 'light', 'b', False)] + bald('side')[:0]
            + [L(blob(SIDE_SKULL), 'skin'), L(blob([(16, 30), (30, 12), (54, 4), (78, 8), (88, 20), (60, 14), (36, 20), (20, 34)]), 'mid', 'f', ln=True)]
            + side_shades('lens', 'frame'),
    'back': spk((40, 16), (60, 16), (50, -10), 3) + bald('back'),
})

# ------------------------------------------------------------------ Simon Calier: pelo rubio dorado despeinado y muy ancho, con
# las puntas abiertas hacia los lados y un pelillo de antena; ojos afilados
CHARS['simon-calier'] = {
    'body': 'normal', 'pal': pal('#d8b048', '#f6c08e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': (60, 50)},
    'front': [spk((36, 8), (42, 6), (30, -8), 2),
              L(blob([(6, 70), (2, 44), (14, 16), (50, 6), (86, 16), (98, 44), (94, 70), (82, 66), (82, 60), (18, 60), (18, 66)])),
              *[wavy(a, b, t, bd) for a, b, t, bd in (((2, 50), (10, 66), (-22, 64), 4), ((6, 62), (16, 74), (-14, 82), -4))],
              *[wavy(a, b, t, bd, light_left=False) for a, b, t, bd in (((90, 66), (98, 50), (122, 64), -4), ((84, 74), (94, 62), (114, 82), 4))],
              L(blob([(62, 12), (96, 44), (94, 70), (84, 66)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
              spk((12, 44), (30, 38), (16, 72), 5, z='f'), spk((28, 38), (48, 34), (36, 64), 5, z='f'),
              spk((52, 34), (70, 38), (62, 64), 5, z='f', light_left=False), spk((70, 40), (88, 44), (86, 72), 5, z='f', light_left=False)],
    'side': [spk((34, 8), (40, 6), (36, -8), 2),
             L(blob([(48, 92), (14, 90), (2, 62), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (92, 58), (76, 56), (62, 58), (56, 74), (52, 90)])),
             *wavy((4, 50), (8, 66), (-24, 62), 4), *wavy((6, 66), (14, 80), (-18, 86), -4), *wavy((16, 82), (30, 90), (4, 100), -4),
             L(blob([(6, 50), (8, 86), (40, 90), (24, 64)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             spk((56, 30), (88, 40), (92, 72), 6, z='f', light_left=False), spk((50, 54), (62, 54), (56, 80), 3, z='f')],
    'back': [spk((58, 8), (64, 6), (70, -8), 2, light_left=False),
             L(blob([(6, 72), (2, 44), (14, 16), (50, 6), (86, 16), (98, 44), (94, 72), (50, 82)])),
             *wavy((2, 50), (10, 66), (-22, 64), 4), *wavy((6, 62), (16, 76), (-14, 84), -4),
             *wavy((90, 66), (98, 50), (122, 64), -4, light_left=False), *wavy((84, 76), (94, 62), (114, 84), 4, light_left=False),
             *wavy((18, 74), (40, 80), (24, 94), 4), *wavy((40, 80), (60, 80), (52, 96), -3), *wavy((60, 80), (82, 74), (78, 94), -4, light_left=False),
             L(blob([(58, 12), (96, 44), (94, 70), (66, 80)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3)],
}

# ------------------------------------------------------------------ Brody Gloom: corpulento, tupé gris con un rizo que se levanta
# sobre la frente; ojos pequeños, cejas tristes y boca hacia abajo
BRODY_QUIFF = blob([(30, 26), (34, 6), (50, -4), (66, 0), (72, 12), (62, 14), (56, 8), (50, 12), (52, 26)])
CHARS['brody-gloom'] = {
    'body': 'corpulento', 'pal': pal('#5e5e68', '#f6b878'),
    'face': {'eyes': 'dot', 'brows': True, 'mouth': 'frown', 'mouth_y': 93, 'hairline': (56, 44)},
    'front': [L(blob([(14, 64), (12, 36), (24, 14), (50, 8), (76, 14), (88, 36), (86, 64)])),
              L(blob([(60, 12), (88, 36), (86, 62), (72, 58)], 6), 'shade', 'b', False),
              strand([(30, 20), (24, 50)], 'deep', 'b', 1.0), strand([(70, 20), (76, 50)], 'deep', 'b', 1.0),
              L(BRODY_QUIFF, 'mid', 'b', ln=True), L(blob([(52, 0), (66, 2), (70, 12), (60, 10)], 4), 'light', 'b', False)],
    'side': [L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             L(blob([(50, 20), (60, 2), (78, -2), (92, 8), (94, 22), (84, 18), (76, 12), (70, 22), (80, 36), (62, 32)]), 'mid', 'b', ln=True),
             L(blob([(66, 2), (86, 2), (92, 14), (78, 8)], 4), 'light', 'b', False),
             strand([(70, 24), (40, 22), (20, 46)], 'light', 'b', 1.4), strand([(76, 34), (44, 32), (24, 60)], 'deep', 'b', 1.0)],
    'back': [L(blob(SKULL_B))] + back_hair() + [L(BRODY_QUIFF, 'mid', 'b', ln=True),
             strand([(40, 14), (36, 80)], 'deep', 'b', 1.0), strand([(60, 14), (64, 80)], 'deep', 'b', 1.0)],
}

# ------------------------------------------------------------------ Victor Talis: pelo gris verdoso de pinchos hacia arriba y a
# los lados; ojos redondos, nariz roja pequeña y sonrisa
CHARS['victor-talis'] = {
    'body': 'normal', 'pal': pal('#40584e', '#f6bc80', nose='#e05a3a'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'nose': (50, 83, 2.6), 'nose_side': (90, 81, 2.4), 'hairline': (58, 50)},
    'front': [spk((8, 60), (12, 42), (-14, 50), 6), spk((12, 42), (24, 24), (-6, 14), 7), spk((24, 24), (42, 12), (24, -16), 7),
              spk((40, 12), (60, 10), (52, -22), 7), spk((58, 12), (76, 18), (82, -14), 7, light_left=False),
              spk((74, 20), (88, 36), (110, 18), 7, light_left=False), spk((88, 40), (92, 60), (114, 52), 6, light_left=False),
              L(blob([(10, 70), (8, 40), (20, 16), (50, 8), (80, 16), (92, 40), (90, 70), (80, 64), (20, 64)])),
              L(blob([(62, 14), (90, 38), (88, 66), (78, 62)], 6), 'shade', 'b', False),
              spk((12, 46), (30, 40), (18, 70), 5, z='f'), spk((30, 40), (48, 36), (38, 60), 4, z='f'),
              spk((52, 36), (70, 40), (62, 60), 4, z='f', light_left=False), spk((70, 40), (88, 46), (84, 70), 5, z='f', light_left=False)],
    'side': [spk((16, 40), (24, 24), (-18, 20), 7), spk((24, 26), (40, 14), (6, -14), 7), spk((40, 14), (60, 8), (54, -20), 7),
             spk((14, 56), (16, 40), (-16, 50), 6), spk((18, 70), (22, 58), (-8, 80), 5),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((60, 14), (80, 22), (98, 2), 6, light_left=False),
             spk((56, 30), (88, 40), (92, 70), 6, z='f', light_left=False), spk((54, 52), (66, 52), (62, 84), 3, z='f')],
    'back': [spk((8, 60), (12, 42), (-14, 50), 6), spk((12, 42), (24, 24), (-6, 14), 7), spk((24, 24), (42, 12), (24, -16), 7),
             spk((40, 12), (60, 10), (52, -22), 7), spk((58, 12), (76, 18), (82, -14), 7, light_left=False),
             spk((74, 20), (88, 36), (110, 18), 7, light_left=False), spk((88, 40), (92, 60), (114, 52), 6, light_left=False),
             L(blob([(10, 72), (8, 40), (20, 16), (50, 8), (80, 16), (92, 40), (90, 72), (66, 86), (34, 86)])),
             spk((16, 74), (34, 84), (14, 96), 4), spk((34, 84), (50, 88), (42, 100), 4), spk((50, 88), (66, 84), (58, 100), 4, light_left=False),
             spk((66, 84), (84, 74), (86, 96), 4, light_left=False),
             L(blob([(58, 14), (90, 38), (88, 70), (66, 84)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Eren Middleton: delgado, piel tostada, cara alargada; media
# melena castaña rojiza con raya al medio que le cae por los lados hasta el cuello, arrugas rojas en la frente, ojos medio
# cerrados, nariz larga y labios gruesos
EREN_FACE = quad((20, 50), (17, 100), (50, 108)) + quad((50, 108), (83, 100), (80, 50))[1:] + quad((80, 50), (50, 26), (20, 50))[1:-1]
CHARS['eren-middleton'] = {
    'body': 'delgado', 'pal': pal('#6a2a1a', '#c89a5a', wrinkle='#b04a3a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'lips', 'mouth_y': 98, 'mouth_w': 7, 'eye_y': 74, 'face_front': EREN_FACE,
             'nose': (50, 86, 3.4), 'nose_side': (92, 84, 3.4), 'hairline': [(10, 70), (24, 50), (38, 44), (50, 50), (62, 44), (76, 50), (90, 70)]},
    'front': [L(blob([(6, 96), (2, 56), (10, 22), (50, 8), (90, 22), (98, 56), (94, 96), (82, 92), (82, 64), (18, 64), (18, 92)])),
              L(blob([(62, 14), (96, 48), (92, 92), (84, 90)], 6), 'shade', 'b', False), sheen(22, 48, 20, 3),
              strand([(50, 10), (50, 48)], 'deep', 'b', 1.2), strand([(40, 14), (26, 50)], 'deep', 'b', 1.0), strand([(60, 14), (74, 50)], 'deep', 'b', 1.0),
              L(quad((38, 54), (50, 51), (62, 54)), 'wrinkle', 'f', False, False, 1.2), L(quad((36, 59), (50, 56), (64, 59)), 'wrinkle', 'f', False, False, 1.2),
              L(quad((38, 64), (50, 61), (62, 64)), 'wrinkle', 'f', False, False, 1.2),
              L([(32, 70), (42, 72)], OUTC, 'f', False, False, 2.4), L([(68, 70), (58, 72)], OUTC, 'f', False, False, 2.4),
              L([(50, 74), (52, 86)], 'skin_d', 'f', False, False, 1.4)],
    'side': [L(blob([(48, 100), (14, 98), (2, 62), (6, 28), (26, 8), (56, 4), (82, 14), (94, 34), (90, 50), (76, 46), (62, 50), (56, 70), (54, 94)])),
             L(blob([(6, 50), (8, 92), (40, 98), (24, 66)], 6), 'shade', 'b', False), sheen(30, 62, 14, 3),
             spk((56, 30), (86, 38), (92, 52), 5, z='f', light_left=False), spk((52, 52), (62, 52), (58, 86), 3, z='f'),
             L(quad((84, 54), (88, 52), (92, 54)), 'wrinkle', 'f', False, False, 1.1), L(quad((84, 59), (88, 57), (92, 59)), 'wrinkle', 'f', False, False, 1.1)],
    'back': [L(blob([(6, 96), (2, 56), (10, 22), (50, 8), (90, 22), (98, 56), (94, 96), (50, 104)])),
             spk((12, 92), (30, 98), (16, 110), 4), spk((30, 98), (50, 102), (38, 114), 4), spk((50, 102), (70, 98), (62, 114), 4, light_left=False),
             spk((70, 98), (88, 92), (84, 110), 4, light_left=False),
             L(blob([(58, 12), (96, 48), (92, 94), (66, 100)], 6), 'shade', 'b', False), sheen(22, 48, 20, 3),
             spk((48, 8), (54, 8), (54, -6), 2, light_left=False)],
}
