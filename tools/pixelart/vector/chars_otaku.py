"""Shuuyou Meito / Instituto Otaku (IE1): pelo, gafas, cascos y disfraces de cada jugador, con sus modelos 3D como
referencia (Marcus Train no tiene modelo: su retrato de la wiki)."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, fat, pal, sheen, spk, strand
from heads import quad

DARK = (30, 22, 24, 255)
WHITE = (255, 255, 255, 255)
SIDE_SKULL = [(44, 92), (22, 88), (12, 64), (14, 36), (30, 16), (56, 10), (78, 18), (88, 36), (76, 44), (60, 48), (52, 62), (50, 80)]


def glasses(y=75, rx=9, ry=7, c=(60, 50, 40, 255), lens=None):
    out = []
    for cx in (36, 64):
        if lens:
            out.append(L(ell(cx, y, rx, ry), lens, 'f', False))
        pts = ell(cx, y, rx, ry)
        out.append(L(pts + [pts[0]], c, 'f', False, False, 1.5))
    out.append(L([(36 + rx, y - 1), (64 - rx, y - 1)], c, 'f', False, False, 1.3))
    return out


def side_glass(y=75, c=(60, 50, 40, 255), lens=None):
    pts = ell(84, y, 5.4, 7)
    out = [L(pts, lens, 'f', False)] if lens else []
    return out + [L(pts + [pts[0]], c, 'f', False, False, 1.5), L([(78, y - 1), (52, y - 4)], c, 'f', False, False, 1.3)]


def back_hair(c='shade'):
    return [L(blob([(58, 16), (88, 38), (86, 68), (68, 86)], 6), c, 'b', False), sheen(26, 52, 20, 3)]


# ------------------------------------------------------------------ Sam Idol (portero): corpulento, pelo oscuro rizado y alto,
# gafas redondas, nariz roja y ojos cerrados de felicidad con una sonrisa enorme
CHARS['sam-idol'] = {
    'body': 'corpulento', 'pal': pal('#2e3644', '#f2c49a', nose='#e0503a'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'grin', 'mouth_y': 90, 'nose': (50, 80, 4), 'nose_side': (90, 79, 3.6), 'hairline': (58, 50)},
    'front': [L(bumpy(50, 34, 46, 32, 14, 0.08)), L(bumpy(66, 40, 22, 20, 8, 0.08), 'shade', 'b', False), L(ell(32, 18, 10, 4), 'light', 'b', False),
              L(blob([(10, 66), (8, 44), (92, 44), (90, 66), (78, 58), (22, 58)]))] + glasses(74, 9, 7.5),
    'side': [L(bumpy(44, 34, 44, 32, 14, 0.08)), L(bumpy(26, 46, 20, 22, 8, 0.08), 'shade', 'b', False),
             L(blob(SIDE_SKULL))] + side_glass(74),
    'back': [L(bumpy(50, 40, 46, 38, 14, 0.08)), L(bumpy(68, 50, 22, 24, 8, 0.08), 'shade', 'b', False), L(ell(32, 22, 10, 4), 'light', 'b', False),
             L(blob([(14, 60), (86, 60), (80, 84), (50, 92), (20, 84)]))],
}

# ------------------------------------------------------------------ Marcus Train: melena castaña revuelta con una cinta roja en la
# frente, cejas caídas y cara de cansancio
CHARS['marcus-train'] = {
    'body': 'normal', 'pal': pal('#5a3a22', '#e8b07a', band='#b82a2a', band_d='#8a1e1e'),
    'face': {'eyes': 'dot', 'brows': True, 'mouth': 'frown', 'hairline': (58, 52)},
    'front': [L(blob([(8, 70), (2, 44), (14, 18), (50, 8), (86, 18), (98, 44), (92, 70)])),
              spk((4, 50), (12, 66), (-10, 70), 5), spk((88, 66), (96, 50), (110, 70), 5, light_left=False),
              spk((30, 14), (44, 10), (26, 2), 4), spk((44, 10), (56, 10), (50, 0), 3), spk((56, 10), (70, 14), (74, 2), 4, light_left=False),
              L(blob([(60, 14), (92, 36), (92, 66), (76, 62)], 6), 'shade', 'b', False), sheen(22, 46, 18, 3),
              L(quad((14, 46), (50, 38), (86, 46)) + quad((86, 56), (50, 48), (14, 56)), 'band', 'f', ln=True),
              L(quad((14, 52), (50, 44), (86, 52)) + quad((86, 56), (50, 48), (14, 56)), 'band_d', 'f', False),
              spk((18, 56), (34, 54), (22, 68), 3, z='f'), spk((66, 54), (82, 56), (78, 68), 3, z='f', light_left=False)],
    'side': [L(blob([(46, 92), (20, 88), (6, 62), (8, 34), (24, 12), (54, 6), (80, 16), (92, 36), (76, 44), (60, 48), (54, 62), (52, 82)])),
             spk((10, 44), (20, 28), (-12, 28), 6), spk((8, 64), (16, 48), (-14, 56), 5), spk((12, 80), (24, 90), (-6, 98), 5),
             L(blob([(12, 48), (14, 84), (40, 92), (26, 62)], 6), 'shade', 'b', False),
             L(quad((12, 44), (50, 36), (90, 46)) + quad((90, 56), (50, 46), (12, 54)), 'band', 'f', ln=True),
             spk((60, 54), (86, 56), (90, 70), 3, z='f', light_left=False)],
    'back': [L(blob([(8, 70), (2, 44), (14, 18), (50, 8), (86, 18), (98, 44), (92, 70), (76, 90), (50, 96), (24, 90)])),
             spk((4, 50), (12, 66), (-10, 70), 5), spk((88, 66), (96, 50), (110, 70), 5, light_left=False),
             spk((14, 78), (32, 90), (6, 104), 5), spk((32, 92), (52, 96), (38, 110), 5), spk((52, 96), (72, 92), (68, 110), 5, light_left=False),
             spk((70, 90), (88, 78), (96, 104), 5, light_left=False)] + back_hair() + [
             L(quad((10, 46), (50, 40), (90, 46)) + quad((90, 56), (50, 50), (10, 56)), 'band', 'f', ln=True)],
}

# ------------------------------------------------------------------ Spencer Gates: corpulento, pelo verde oliva con orejas de gato
# rosas encima, ojos grandes, nariz de gato y mejillas sonrosadas
CHARS['spencer-gates'] = {
    'body': 'corpulento', 'pal': pal('#6a6a30', '#f2c8a0', cat='#e8b8a8', cat_d='#a07060', nose='#d06a3a', blush='#f0a080'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'nose': (50, 82, 3.6), 'nose_side': (89, 80, 3.2), 'hairline': (60, 52)},
    'front': [L(fat((8, 40), (24, 22), (2, 0), 4), 'cat', 'b', True, True), L(fat((76, 22), (92, 40), (98, 0), 4), 'cat', 'b', True, True),
              L(fat((12, 32), (20, 24), (8, 10), 2), 'cat_d', 'b', False), L(fat((80, 24), (88, 32), (92, 10), 2), 'cat_d', 'b', False),
              L(blob([(12, 66), (10, 40), (22, 18), (50, 10), (78, 18), (90, 40), (88, 66)])),
              L(blob([(60, 14), (88, 34), (88, 62), (72, 58)], 6), 'shade', 'b', False), sheen(26, 50, 20, 3),
              spk((18, 46), (40, 42), (26, 66), 4, z='f'), spk((38, 42), (62, 42), (50, 62), 4, z='f'), spk((60, 42), (82, 46), (74, 66), 4, z='f', light_left=False),
              L(ell(28, 86, 5, 3), 'blush', 'f', False), L(ell(72, 86, 5, 3), 'blush', 'f', False)],
    'side': [L(fat((40, 20), (58, 16), (52, -6), 4), 'cat', 'b', True, True),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((54, 26), (84, 36), (90, 64), 6, z='f', light_left=False), L(ell(78, 88, 4, 2.6), 'blush', 'f', False)],
    'back': [L(fat((8, 40), (24, 22), (2, 0), 4), 'cat', 'b', True, True), L(fat((76, 22), (92, 40), (98, 0), 4), 'cat', 'b', True, True),
             L(blob([(12, 66), (10, 40), (22, 18), (50, 10), (78, 18), (90, 40), (88, 66), (72, 84), (50, 88), (28, 84)]))] + back_hair(),
}

# ------------------------------------------------------------------ Light Nobel: corpulento, pelo verde oscuro alborotado hacia
# arriba, gafas redondas pequeñas y cara redonda de bonachón
CHARS['light-nobel'] = {
    'body': 'corpulento', 'pal': pal('#2c5a3e', '#f6d29a'),
    'face': {'eyes': 'dot', 'brows': True, 'mouth': 'smile', 'hairline': (56, 50)},
    'front': [L(blob([(16, 58), (12, 34), (24, 12), (50, 4), (76, 12), (88, 34), (84, 58)])),
              spk((10, 44), (18, 30), (-4, 34), 5), spk((82, 30), (90, 44), (104, 34), 5, light_left=False),
              spk((28, 12), (46, 6), (34, -4), 5), spk((46, 6), (60, 6), (54, -6), 4), spk((58, 6), (74, 12), (70, -4), 5, light_left=False),
              L(blob([(60, 10), (86, 32), (84, 56), (70, 52)], 6), 'shade', 'b', False), sheen(28, 52, 14, 3),
              spk((26, 44), (44, 42), (34, 56), 3, z='f'), spk((56, 42), (74, 44), (68, 56), 3, z='f', light_left=False)] + glasses(74, 7, 6),
    'side': [L(blob([(44, 86), (24, 82), (16, 58), (18, 30), (34, 10), (60, 4), (82, 14), (90, 34), (76, 42), (60, 46), (52, 60), (50, 76)])),
             spk((18, 30), (32, 14), (-6, 4), 7), spk((40, 8), (58, 4), (44, -12), 5),
             L(blob([(20, 44), (22, 70), (38, 82), (30, 58)], 6), 'shade', 'b', False)] + side_glass(74),
    'back': [L(blob([(16, 64), (12, 34), (24, 12), (50, 4), (76, 12), (88, 34), (84, 64), (68, 80), (32, 80)])),
             spk((10, 44), (18, 30), (-4, 34), 5), spk((82, 30), (90, 44), (104, 34), 5, light_left=False),
             spk((28, 12), (46, 6), (34, -4), 5), spk((46, 6), (60, 6), (54, -6), 4), spk((58, 6), (74, 12), (70, -4), 5, light_left=False)] + back_hair(),
}

# ------------------------------------------------------------------ Walter Valiant: pelo castaño despeinado con dos antenas finas
# que se curvan, cara alargada con gesto de enfado y pañuelo rojo al cuello
CHARS['walter-valiant'] = {
    'body': 'delgado', 'pal': pal('#4a3a20', '#f2c69c', scarf='#c83a20', scarf_d='#8a2414'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'hairline': (60, 52)},
    'front': [L(quad((40, 14), (24, -6), (10, 6)), 'mid', 'b', False, False, 1.6), L(quad((60, 14), (76, -6), (90, 6)), 'mid', 'b', False, False, 1.6),
              L(blob([(12, 70), (8, 40), (20, 16), (50, 8), (80, 16), (92, 40), (88, 70)])),
              spk((8, 52), (16, 66), (-6, 70), 4), spk((84, 66), (92, 52), (106, 70), 4, light_left=False),
              L(blob([(60, 14), (90, 36), (90, 66), (74, 62)], 6), 'shade', 'b', False), sheen(22, 46, 18, 3),
              spk((14, 46), (34, 42), (20, 72), 5, z='f'), spk((32, 42), (52, 40), (42, 66), 5, z='f'),
              spk((50, 40), (68, 42), (62, 62), 4, z='f', light_left=False), spk((66, 44), (88, 48), (84, 72), 5, z='f', light_left=False),
              L(blob([(20, 100), (50, 106), (80, 100), (82, 112), (50, 116), (18, 112)], 5), 'scarf', 'f', ln=True),
              L(blob([(76, 104), (100, 94), (104, 108), (84, 114)], 4), 'scarf_d', 'f', ln=True)],
    'side': [L(quad((44, 12), (54, -10), (70, -4)), 'mid', 'b', False, False, 1.6),
             L(blob(SIDE_SKULL)), spk((12, 62), (22, 46), (-10, 52), 5), spk((14, 80), (28, 88), (0, 96), 4),
             L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((54, 26), (86, 36), (92, 70), 6, z='f', light_left=False),
             L(blob([(46, 98), (84, 100), (84, 110), (46, 112)], 5), 'scarf', 'f', ln=True),
             L(blob([(46, 104), (22, 96), (10, 108), (22, 116), (44, 112)], 4), 'scarf_d', 'f', ln=True)],
    'back': [L(quad((40, 14), (24, -6), (10, 6)), 'mid', 'b', False, False, 1.6), L(quad((60, 14), (76, -6), (90, 6)), 'mid', 'b', False, False, 1.6),
             L(blob([(12, 70), (8, 40), (20, 16), (50, 8), (80, 16), (92, 40), (88, 70), (74, 90), (50, 96), (26, 90)])),
             spk((14, 78), (32, 90), (8, 102), 4), spk((32, 92), (52, 96), (38, 110), 4), spk((52, 96), (72, 92), (68, 110), 4, light_left=False),
             spk((70, 90), (88, 78), (94, 102), 4, light_left=False)] + back_hair() + [
             L(blob([(18, 100), (82, 100), (82, 112), (18, 112)], 5), 'scarf', 'f', ln=True),
             L(blob([(14, 104), (-6, 98), (-8, 114), (10, 114)], 4), 'scarf_d', 'f', ln=True)],
}

# ------------------------------------------------------------------ A. Woodbridge: pelo rosa con un pelo de antena, cinta de pelo
# morada oscura en la frente y gafas redondas blancas con espirales (no se le ven los ojos)
CHARS['a-woodbridge'] = {
    'body': 'normal', 'pal': pal('#d87070', '#f6d2b0', band='#3a2a40', lens=(250, 250, 250, 255)),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'hairline': (58, 50)},
    'front': [L(quad((50, 14), (56, -6), (64, -2)), 'mid', 'b', False, False, 1.8),
              L(blob([(10, 80), (6, 44), (16, 18), (50, 10), (84, 18), (94, 44), (90, 80), (80, 76), (80, 60), (20, 60), (20, 76)])),
              L(blob([(60, 14), (92, 38), (90, 76), (80, 72)], 6), 'shade', 'b', False), sheen(22, 46, 18, 3),
              L(quad((10, 38), (50, 28), (90, 38)) + quad((90, 50), (50, 40), (10, 50)), 'band', 'f', ln=True),
              spk((14, 50), (32, 48), (18, 80), 4, z='f'), spk((68, 48), (86, 50), (84, 80), 4, z='f', light_left=False),
              spk((32, 50), (46, 50), (38, 62), 2, z='f'), spk((54, 50), (68, 50), (62, 62), 2, z='f', light_left=False)]
             + glasses(73, 10, 8, (90, 90, 100, 255), 'lens')
             + [L(quad((30, 73), (36, 68), (42, 74)), (140, 140, 150, 255), 'f', False, False, 1.0), L(quad((58, 73), (64, 68), (70, 74)), (140, 140, 150, 255), 'f', False, False, 1.0)],
    'side': [L(quad((54, 12), (66, -8), (76, -2)), 'mid', 'b', False, False, 1.8),
             L(blob([(46, 94), (20, 90), (6, 64), (8, 34), (24, 12), (54, 6), (80, 16), (92, 36), (76, 44), (60, 48), (54, 62), (52, 84)])),
             L(blob([(12, 48), (14, 84), (40, 92), (26, 64)], 6), 'shade', 'b', False),
             L(quad((10, 36), (50, 26), (92, 40)) + quad((92, 52), (50, 38), (10, 48)), 'band', 'f', ln=True),
             spk((58, 50), (86, 54), (90, 74), 3, z='f', light_left=False)] + side_glass(73, (90, 90, 100, 255), 'lens'),
    'back': [L(quad((50, 14), (56, -6), (64, -2)), 'mid', 'b', False, False, 1.8),
             L(blob([(10, 80), (6, 44), (16, 18), (50, 10), (84, 18), (94, 44), (90, 80), (50, 88)]))] + back_hair() + [
             L(quad((8, 38), (50, 30), (92, 38)) + quad((92, 50), (50, 42), (8, 50)), 'band', 'f', ln=True)],
}

# ------------------------------------------------------------------ Josh Spear: melena lisa castaña con raya en medio y flequillo
# largo que le tapa un ojo, coleta baja; orejas grandes
CHARS['josh-spear'] = {
    'body': 'delgado', 'pal': pal('#6a3e30', '#f2c49c'),
    'face': {'eyes': 'sharp', 'mouth': 'line', 'big_ears': 2, 'ear_out': 4, 'ears_front': True, 'hairline': (62, 46)},
    'front': [L(blob([(14, 92), (10, 44), (20, 16), (50, 8), (80, 16), (90, 44), (86, 92), (78, 90), (80, 60), (20, 60), (22, 90)])),
              L(blob([(60, 14), (86, 36), (86, 88), (78, 86)], 6), 'shade', 'b', False), sheen(24, 46, 16, 3),
              strand([(50, 10), (50, 40)], 'deep', 'b', 1.2),
              L(blob([(50, 14), (70, 22), (82, 46), (80, 90), (70, 92), (66, 64), (56, 50)]), 'mid', 'f', ln=True),
              L(blob([(50, 14), (32, 22), (20, 46), (20, 88), (28, 88), (30, 60), (44, 50)]), 'mid', 'f', ln=True)],
    'side': [L(blob([(30, 52), (16, 56), (4, 80), (2, 104), (10, 106), (18, 82), (32, 64)])),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((54, 24), (86, 34), (86, 88), 5, z='f', light_left=False)],
    'back': [L(blob([(14, 92), (10, 44), (20, 16), (50, 8), (80, 16), (90, 44), (86, 92), (50, 96)]))] + back_hair() + [
             L(blob([(42, 56), (58, 56), (60, 92), (54, 116), (46, 116), (40, 92)]), 'mid', 'f', ln=True), strand([(50, 60), (50, 112)], 'shade', 'f', 1.0)],
}

# ------------------------------------------------------------------ Gaby Farmer: pelo azul grisáceo corto con flequillo de lado y
# gafas redondas finas; piel morena y mirada seria
CHARS['gaby-farmer'] = {
    'body': 'normal', 'pal': pal('#4a7a8a', '#d8a070'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'hairline': (60, 52)},
    'front': [L(blob([(12, 76), (8, 42), (20, 16), (50, 8), (80, 16), (92, 42), (88, 76), (80, 72), (80, 60), (20, 60), (20, 72)])),
              L(blob([(60, 14), (90, 36), (88, 72), (78, 70)], 6), 'shade', 'b', False), sheen(22, 46, 18, 3),
              spk((60, 24), (80, 36), (16, 66), 7, z='f'), spk((54, 38), (74, 42), (36, 66), 4, z='f'),
              spk((70, 42), (88, 50), (84, 72), 4, z='f', light_left=False)] + glasses(76, 9, 7),
    'side': [L(blob([(46, 92), (20, 88), (8, 64), (10, 36), (26, 14), (54, 8), (80, 16), (90, 36), (76, 44), (60, 48), (54, 62), (52, 82)])),
             L(blob([(12, 48), (14, 84), (40, 92), (26, 64)], 6), 'shade', 'b', False),
             spk((54, 24), (86, 34), (90, 70), 6, z='f', light_left=False)] + side_glass(76),
    'back': [L(blob([(12, 76), (8, 42), (20, 16), (50, 8), (80, 16), (92, 42), (88, 76), (72, 90), (50, 94), (28, 90)]))] + back_hair(),
}

# ------------------------------------------------------------------ Gus Gamer: melena castaña rojiza rizada hasta los hombros, con
# una cinta blanca y rosa en la frente y cejas pobladas
CHARS['gus-gamer'] = {
    'body': 'normal', 'pal': pal('#8a3a1e', '#f2c098', band='#f0e0e4', band_d='#d89aa8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'hairline': (58, 50)},
    'front': [L(bumpy(50, 56, 50, 52, 16, 0.07)), L(blob([(64, 20), (94, 50), (90, 96), (78, 96)], 6), 'shade', 'b', False),
              L(blob([(18, 64), (82, 64), (82, 100), (18, 100)]), 'skin', 'b', False),
              L(quad((10, 46), (50, 38), (90, 46)) + quad((90, 56), (50, 48), (10, 56)), 'band', 'f', ln=True),
              L(quad((10, 52), (50, 44), (90, 52)) + quad((90, 56), (50, 48), (10, 56)), 'band_d', 'f', False),
              spk((10, 56), (24, 58), (10, 96), 4, z='f'), spk((76, 58), (90, 56), (90, 96), 4, z='f', light_left=False)],
    'side': [L(bumpy(40, 56, 42, 48, 14, 0.07)), L(blob([(12, 50), (12, 92), (40, 98), (26, 66)], 6), 'shade', 'b', False),
             L(quad((10, 44), (50, 36), (90, 46)) + quad((90, 56), (50, 46), (10, 54)), 'band', 'f', ln=True),
             spk((58, 54), (86, 56), (90, 72), 3, z='f', light_left=False)],
    'back': [L(bumpy(50, 58, 50, 54, 16, 0.07)), L(blob([(58, 18), (94, 46), (90, 96), (66, 104)], 6), 'shade', 'b', False),
             L(quad((8, 46), (50, 40), (92, 46)) + quad((92, 56), (50, 50), (8, 56)), 'band', 'f', ln=True)],
}

# ------------------------------------------------------------------ Mark Gambling: pelo rubio con flequillo largo de lado que le
# tapa un ojo, moño alto con dos lápices clavados y una boina rosa ladeada; gafas
CHARS['mark-gambling'] = {
    'body': 'normal', 'pal': pal('#d8b05a', '#f6d6b8', beret='#d07070', beret_d='#a04a4a', pencil='#e8e0d0', lead='#4a6a9a'),
    'face': {'eyes': 'normal', 'mouth': 'line', 'hairline': (60, 52), 'glasses': (70, 70, 80, 255)},
    'front': [L(fat((30, 18), (36, 14), (16, -10), 1.5), 'pencil', 'b', True, True), L(fat((64, 14), (70, 18), (88, -8), 1.5), 'pencil', 'b', True, True),
              L(bumpy(50, 16, 16, 12, 8, 0.08)),
              L(blob([(12, 82), (8, 42), (20, 16), (50, 8), (80, 16), (92, 42), (88, 82), (80, 78), (80, 60), (20, 60), (20, 78)])),
              L(blob([(60, 14), (90, 36), (88, 78), (78, 76)], 6), 'shade', 'b', False), sheen(22, 46, 18, 3),
              L(ell(64, 20, 16, 8), 'beret', 'b', True, True), L(ell(68, 22, 9, 4), 'beret_d', 'b', False),
              L(blob([(54, 22), (32, 34), (18, 54), (22, 86), (34, 90), (40, 64), (50, 48), (68, 40)]), 'mid', 'f', ln=True),
              spk((62, 40), (86, 48), (84, 76), 4, z='f', light_left=False)],
    'side': [L(fat((38, 12), (44, 10), (30, -14), 1.5), 'pencil', 'b', True, True), L(bumpy(40, 14, 16, 12, 8, 0.08)),
             L(blob([(46, 94), (20, 90), (8, 64), (10, 36), (26, 14), (54, 8), (80, 16), (90, 36), (76, 44), (60, 48), (54, 62), (52, 84)])),
             L(blob([(12, 48), (14, 84), (40, 92), (26, 64)], 6), 'shade', 'b', False), L(ell(64, 18, 14, 7), 'beret', 'b', True, True),
             spk((54, 24), (86, 34), (90, 80), 6, z='f', light_left=False)],
    'back': [L(fat((30, 18), (36, 14), (16, -10), 1.5), 'pencil', 'b', True, True), L(fat((64, 14), (70, 18), (88, -8), 1.5), 'pencil', 'b', True, True),
             L(bumpy(50, 16, 16, 12, 8, 0.08)),
             L(blob([(12, 82), (8, 42), (20, 16), (50, 8), (80, 16), (92, 42), (88, 82), (50, 90)]))] + back_hair() + [L(ell(36, 20, 16, 8), 'beret', 'b', True, True)],
}

# ------------------------------------------------------------------ Theodore Master: gorro de aviador gris verdoso con unas
# gafas rojas grandes encima, pelo azul claro que asoma y una tirita en la mejilla
CHARS['theodore-master'] = {
    'body': 'normal', 'pal': pal('#6aa8a8', '#f2c8a0', cap='#4a5a58', cap_d='#36423f', gog='#b02020', lens='#e8e8e0', plaster='#f0e0c8'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'frown', 'hairline': (60, 52)},
    'front': [L(blob([(8, 72), (4, 40), (16, 14), (50, 6), (84, 14), (96, 40), (92, 72), (80, 66), (20, 66)]), 'cap', 'f', ln=True),
              L(blob([(60, 10), (94, 38), (92, 68), (78, 64)], 6), 'cap_d', 'f', False),
              spk((20, 52), (36, 50), (26, 66), 3, z='f'), spk((36, 50), (52, 50), (44, 66), 3, z='f'), spk((52, 50), (68, 50), (60, 64), 3, z='f', light_left=False),
              L(quad((8, 40), (50, 32), (92, 40)) + quad((92, 52), (50, 44), (8, 52)), 'gog', 'f', ln=True),
              L(ell(34, 36, 13, 11), 'gog', 'f', ln=True), L(ell(66, 36, 13, 11), 'gog', 'f', ln=True),
              L(ell(34, 36, 9, 7.6), 'lens', 'f', False), L(ell(66, 36, 9, 7.6), 'lens', 'f', False),
              L([(28, 32), (34, 40), (40, 32)], OUTC, 'f', False, False, 1.4), L([(60, 32), (66, 40), (72, 32)], OUTC, 'f', False, False, 1.4),
              L([(58, 82), (70, 82), (70, 88), (58, 88)], 'plaster', 'f', ln=True)],
    'side': [L(blob([(48, 96), (16, 92), (4, 62), (8, 30), (26, 8), (58, 4), (84, 16), (94, 40), (90, 64), (66, 62), (56, 78), (58, 96)]), 'cap', 'f', ln=True),
             L(blob([(8, 36), (26, 12), (30, 60), (22, 90)], 6), 'cap_d', 'f', False),
             L(quad((10, 40), (50, 32), (94, 40)) + quad((94, 52), (50, 44), (10, 52)), 'gog', 'f', ln=True),
             L(ell(82, 38, 9, 11), 'gog', 'f', ln=True), L(ell(84, 38, 5.6, 7), 'lens', 'f', False),
             spk((64, 58), (86, 58), (88, 72), 3, z='f', light_left=False)],
    'back': [L(blob([(8, 76), (4, 40), (16, 14), (50, 6), (84, 14), (96, 40), (92, 76), (74, 92), (50, 98), (26, 92)]), 'cap', 'f', ln=True),
             L(blob([(56, 10), (94, 38), (92, 76), (70, 92)], 6), 'cap_d', 'f', False),
             L(quad((6, 42), (50, 36), (94, 42)) + quad((94, 52), (50, 46), (6, 52)), 'gog', 'f', ln=True)],
}

# ------------------------------------------------------------------ Ham Signalman: pañuelo de rayas verdes y oscuras atado en la
# cabeza (nudo detrás), pelo castaño que asoma por debajo y cara sonriente
def striped(shape_pts, rows, c1='band', c2='band_d'):
    out = [L(shape_pts, c1, 'f', ln=True)]
    for y in rows:
        out.append(L([(0, y), (100, y - 4)], c2, 'f', False, False, 3.4))
    return out


CHARS['ham-signalman'] = {
    'body': 'normal', 'pal': pal('#4a2c1e', '#f2c49a', band='#6a7a3a', band_d='#3e4a26'),
    'face': {'eyes': 'big', 'mouth': 'smile', 'hairline': (60, 54)},
    'front': [L(blob([(10, 84), (8, 56), (92, 56), (90, 84), (80, 80), (20, 80)])),
              spk((10, 62), (22, 66), (8, 90), 3), spk((78, 66), (90, 62), (92, 90), 3, light_left=False)]
             + [L(blob([(10, 60), (8, 34), (20, 12), (50, 6), (80, 12), (92, 34), (90, 60), (50, 52)]), 'band', 'f', ln=True)]
             + [L([(14 + k * 2, 20 + k * 10), (88 - k * 2, 14 + k * 10)], 'band_d', 'f', False, False, 3.2) for k in range(4)]
             + [spk((22, 54), (38, 54), (28, 66), 2, z='f'), spk((38, 54), (52, 54), (46, 66), 2, z='f'), spk((62, 54), (78, 54), (72, 66), 2, z='f', light_left=False)],
    'side': [L(blob(SIDE_SKULL)), spk((14, 66), (24, 76), (6, 90), 3),
             L(blob([(12, 62), (10, 32), (26, 10), (54, 4), (80, 12), (92, 32), (90, 56), (50, 56)]), 'band', 'f', ln=True)]
            + [L([(14, 22 + k * 10), (90, 16 + k * 10)], 'band_d', 'f', False, False, 3.2) for k in range(4)]
            + [L(blob([(12, 50), (-4, 46), (-6, 62), (8, 62)], 4), 'band', 'f', ln=True)],
    'back': [L(blob([(14, 70), (12, 56), (88, 56), (86, 70), (68, 88), (32, 88)])),
             L(blob([(10, 64), (8, 34), (20, 12), (50, 6), (80, 12), (92, 34), (90, 64), (50, 66)]), 'band', 'f', ln=True)]
            + [L([(12, 20 + k * 10), (88, 16 + k * 10)], 'band_d', 'f', False, False, 3.2) for k in range(5)]
            + [L(blob([(40, 58), (24, 50), (20, 66), (38, 70)], 4), 'band', 'f', ln=True), L(blob([(60, 58), (76, 50), (80, 66), (62, 70)], 4), 'band', 'f', ln=True),
               L(ell(50, 62, 7, 6), 'band_d', 'f', ln=True)],
}

# ------------------------------------------------------------------ Bill Formby: corpulento, piel morena, melena castaña lisa con
# raya en medio recogida en una coleta baja
CHARS['bill-formby'] = {
    'body': 'corpulento', 'pal': pal('#5e4a2a', '#c08a5a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'hairline': (62, 46)},
    'front': [L(blob([(14, 86), (10, 44), (20, 16), (50, 8), (80, 16), (90, 44), (86, 86), (78, 84), (80, 60), (20, 60), (22, 84)])),
              L(blob([(60, 14), (86, 36), (86, 84), (78, 82)], 6), 'shade', 'b', False), sheen(24, 46, 16, 3),
              strand([(50, 10), (50, 44)], 'deep', 'b', 1.2)],
    'side': [L(blob([(28, 56), (14, 62), (2, 86), (-6, 112), (4, 114), (16, 90), (30, 70)])),
             L(blob(SIDE_SKULL)), L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             strand([(70, 22), (40, 22), (20, 44)], 'shade', 'b', 1.0), strand([(74, 32), (44, 32), (24, 60)], 'shade', 'b', 1.0)],
    'back': [L(blob([(14, 86), (10, 44), (20, 16), (50, 8), (80, 16), (90, 44), (86, 86), (50, 92)]))] + back_hair() + [
             L(blob([(42, 70), (58, 70), (58, 100), (52, 122), (48, 122), (42, 100)]), 'mid', 'f', ln=True), strand([(50, 12), (50, 70)], 'deep', 'b', 1.2)],
}

# ------------------------------------------------------------------ Grant Eldorado (portero suplente): máscara de luchador
# negra con rayas doradas y cuernos dorados; pelo morado que asoma por la nuca
CHARS['grant-eldorado'] = {
    'body': 'normal', 'pal': pal('#5a3a5a', '#e8c09a', mask='#3e3828', mask_d='#2a2618', gold='#d8b050', gold_d='#a8862e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 92, 'hairline': False, 'ears': False},
    'front': [spk((10, 66), (22, 70), (6, 92), 4), spk((78, 70), (90, 66), (94, 92), 4, light_left=False),
              L(fat((10, 40), (22, 30), (-4, 4), 4), 'gold', 'f', True, True), L(fat((78, 30), (90, 40), (104, 4), 4), 'gold', 'f', True, True),
              L(blob([(12, 84), (8, 44), (18, 18), (50, 8), (82, 18), (92, 44), (88, 84), (70, 86), (60, 80), (50, 82), (40, 80), (30, 86)]), 'mask', 'f', ln=True),
              L(fat((42, 12), (58, 12), (50, 66), 2), 'gold', 'f', False), L(fat((22, 22), (34, 16), (26, 60), 2), 'gold_d', 'f', False),
              L(fat((66, 16), (78, 22), (74, 60), 2), 'gold_d', 'f', False),
              L(blob([(20, 64), (44, 68), (44, 82), (24, 80)], 4), 'gold', 'f', ln=True), L(blob([(80, 64), (56, 68), (56, 82), (76, 80)], 4), 'gold', 'f', ln=True),
              L(ell(34, 74, 6, 4.6), WHITE, 'f', False), L(ell(66, 74, 6, 4.6), WHITE, 'f', False),
              L(ell(34, 74, 3, 3), (140, 120, 170, 255), 'f', False), L(ell(66, 74, 3, 3), (140, 120, 170, 255), 'f', False)],
    'side': [spk((14, 72), (26, 80), (2, 96), 5), L(fat((60, 26), (72, 22), (84, 0), 4), 'gold', 'f', True, True),
             L(blob([(48, 92), (20, 88), (8, 60), (10, 32), (26, 12), (56, 6), (80, 16), (92, 40), (92, 70), (80, 88)]), 'mask', 'f', ln=True),
             L(quad((22, 14), (50, 6), (84, 20)) + quad((84, 28), (50, 14), (22, 22)), 'gold', 'f', False),
             L(blob([(70, 64), (90, 66), (88, 80), (72, 78)], 4), 'gold', 'f', ln=True), L(ell(82, 72, 4, 4.4), WHITE, 'f', False)],
    'back': [spk((14, 76), (32, 88), (8, 102), 5), spk((32, 90), (52, 94), (38, 110), 5), spk((52, 94), (72, 90), (66, 110), 5, light_left=False),
             spk((70, 88), (88, 76), (94, 102), 5, light_left=False),
             L(fat((10, 40), (22, 30), (-4, 4), 4), 'gold', 'f', True, True), L(fat((78, 30), (90, 40), (104, 4), 4), 'gold', 'f', True, True),
             L(blob([(12, 80), (8, 44), (18, 18), (50, 8), (82, 18), (92, 44), (88, 80), (50, 86)]), 'mask', 'f', ln=True),
             L(fat((42, 10), (58, 10), (50, 84), 2), 'gold', 'f', False), L(fat((22, 22), (32, 18), (24, 76), 2), 'gold_d', 'f', False),
             L(fat((68, 18), (78, 22), (76, 76), 2), 'gold_d', 'f', False)],
}

# ------------------------------------------------------------------ Mike Vox: pelo verde oscuro en forma de casco con flequillo
# recto y dos pelillos arriba; ojos cerrados y coloretes
CHARS['mike-vox'] = {
    'body': 'normal', 'pal': pal('#2c4a36', '#f8e0c4', blush='#f0a888'),
    'face': {'eyes': 'closed', 'brows': True, 'mouth': 'line', 'hairline': False},
    'front': [L(fat((46, 12), (52, 10), (42, -4), 2)), L(fat((50, 10), (56, 12), (60, -4), 2)),
              L(blob([(6, 76), (4, 44), (14, 16), (50, 8), (86, 16), (96, 44), (94, 76), (84, 72), (84, 60), (16, 60), (16, 72)])),
              L(blob([(60, 12), (94, 40), (92, 74), (84, 72)], 6), 'shade', 'b', False), sheen(22, 48, 18, 3),
              L(blob([(14, 44), (86, 44), (86, 60), (66, 62), (50, 60), (34, 62), (14, 60)]), 'mid', 'f', ln=True),
              L(ell(28, 86, 5, 3), 'blush', 'f', False), L(ell(72, 86, 5, 3), 'blush', 'f', False)],
    'side': [L(fat((44, 10), (50, 8), (40, -6), 2)),
             L(blob([(48, 90), (16, 88), (4, 62), (6, 32), (24, 10), (54, 6), (80, 16), (92, 36), (90, 60), (66, 60), (56, 70), (54, 86)])),
             L(blob([(10, 46), (12, 82), (40, 88), (26, 62)], 6), 'shade', 'b', False),
             L(ell(80, 86, 4, 2.6), 'blush', 'f', False)],
    'back': [L(fat((46, 12), (52, 10), (42, -4), 2)), L(fat((50, 10), (56, 12), (60, -4), 2)),
             L(blob([(6, 76), (4, 44), (14, 16), (50, 8), (86, 16), (96, 44), (94, 76), (76, 84), (50, 88), (24, 84)]))] + back_hair(),
}

# ------------------------------------------------------------------ Ollie Webb: pelo castaño rojizo de pinchos que se abren a
# los lados, gafas de piloto en la frente, pecas y cejas pobladas
CHARS['ollie-webb'] = {
    'body': 'normal', 'pal': pal('#9a3a1e', '#f2c49a', gog='#5a5a5a', lens='#f0e8d0', freckle='#c8805a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'hairline': (60, 52)},
    'front': [L(blob([(12, 66), (8, 40), (20, 16), (50, 8), (80, 16), (92, 40), (88, 66)])),
              spk((8, 44), (18, 30), (-12, 24), 6), spk((82, 30), (92, 44), (112, 24), 6, light_left=False),
              spk((6, 58), (14, 70), (-10, 74), 5), spk((86, 70), (94, 58), (110, 74), 5, light_left=False),
              spk((26, 16), (44, 10), (24, -8), 5), spk((56, 10), (74, 16), (76, -8), 5, light_left=False),
              L(blob([(60, 14), (88, 34), (88, 62), (72, 58)], 6), 'shade', 'b', False),
              L(blob([(16, 36), (84, 36), (84, 44), (16, 44)], 3), 'gog', 'f'),
              L(ell(36, 40, 10, 7), 'gog', 'f', ln=True), L(ell(64, 40, 10, 7), 'gog', 'f', ln=True),
              L(ell(36, 40, 7, 4.6), 'lens', 'f', False), L(ell(64, 40, 7, 4.6), 'lens', 'f', False),
              spk((18, 50), (36, 46), (24, 68), 4, z='f'), spk((36, 46), (54, 46), (44, 62), 4, z='f'),
              spk((54, 46), (70, 48), (64, 62), 4, z='f', light_left=False), spk((68, 50), (86, 52), (82, 68), 4, z='f', light_left=False)]
             + [L(ell(x, y, 1.1, 1.1), 'freckle', 'f', False) for x, y in ((26, 84), (30, 86), (28, 88), (74, 84), (70, 86), (72, 88))],
    'side': [L(blob(SIDE_SKULL)), spk((14, 40), (28, 24), (-10, 16), 6), spk((12, 62), (22, 46), (-12, 52), 6), spk((40, 12), (58, 8), (44, -10), 5),
             L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             spk((54, 26), (84, 36), (92, 66), 6, z='f', light_left=False),
             L(blob([(40, 34), (90, 36), (90, 44), (40, 42)], 3), 'gog', 'f'), L(ell(82, 40, 7, 7), 'gog', 'f', ln=True), L(ell(83, 40, 4.4, 4.6), 'lens', 'f', False)],
    'back': [L(blob([(12, 66), (8, 40), (20, 16), (50, 8), (80, 16), (92, 40), (88, 66), (74, 86), (50, 92), (26, 86)])),
             spk((8, 44), (18, 30), (-12, 24), 6), spk((82, 30), (92, 44), (112, 24), 6, light_left=False),
             spk((6, 58), (14, 70), (-10, 74), 5), spk((86, 70), (94, 58), (110, 74), 5, light_left=False),
             spk((26, 16), (44, 10), (24, -8), 5), spk((56, 10), (74, 16), (76, -8), 5, light_left=False),
             spk((16, 76), (34, 88), (10, 102), 5), spk((34, 90), (54, 94), (40, 108), 5), spk((54, 94), (72, 90), (68, 108), 5, light_left=False),
             spk((70, 88), (86, 76), (94, 102), 5, light_left=False)] + back_hair() + [
             L(blob([(10, 36), (90, 36), (90, 43), (10, 43)], 3), 'gog', 'f')],
}
