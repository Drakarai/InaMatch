"""Personajes dibujados en vectores: colores, tipo de cuerpo y el pelo en tres vistas (frente, perfil, espalda).

Referencia: los modelos 3D de la enciclopedia oficial (zukan.inazuma.jp/chara_model_view). Coordenadas como en
heads.py (la cabeza mide 100 de ancho; de perfil mira a la derecha).
"""
import math

from heads import L, blob, ell, fat, mirror, spk


def hexc(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5)) + (255,)


def tone(c, f):
    return tuple(max(0, min(255, int(v * f))) for v in c[:3]) + (255,)


def mix(c, d, t):
    return tuple(int(c[i] + (d[i] - c[i]) * t) for i in range(3)) + (255,)


def pal(hair, skin, iris='#302232', **extra):
    h, s = hexc(hair), hexc(skin)
    out = {'mid': h, 'shade': tone(h, 0.78), 'deep': tone(h, 0.6), 'light': mix(h, (255, 255, 255), 0.38),
           'skin': s, 'skin_d': tone(s, 0.86), 'iris': hexc(iris)}
    for k, v in extra.items():
        out[k] = hexc(v) if isinstance(v, str) else v
    return out


def bumpy(cx, cy, rx, ry, n=16, amp=0.07, a0=0.0):
    """Contorno de rizos: elipse con bultos."""
    pts = []
    for i in range(n * 2):
        a = a0 + math.pi * 2 * i / (n * 2)
        r = 1 + (amp if i % 2 == 0 else -amp * 0.6)
        pts.append((cx + rx * r * math.cos(a), cy + ry * r * math.sin(a)))
    return blob(pts, 8)


def M(layers):
    """Refleja una lista de capas (izquierda <-> derecha) para no dibujar dos veces lo simétrico."""
    out = []
    for l in layers:
        out.append(dict(l, s=mirror(l['s'])))
    return out


DOME = blob([(16, 64), (13, 42), (22, 24), (50, 16), (78, 24), (87, 42), (84, 64)])
SIDE_SKULL = blob([(44, 90), (22, 92), (14, 66), (16, 38), (34, 20), (60, 18), (80, 28), (86, 50), (64, 54)])
BACK_SKULL = blob([(16, 66), (14, 40), (24, 22), (50, 16), (76, 22), (86, 40), (84, 66), (70, 90), (50, 96), (30, 90)])

CHARS = {}

# ------------------------------------------------------------------ Mark Evans: cinta naranja y dos mechones de punta
band_front = blob([(10, 44), (30, 36), (50, 33), (70, 36), (90, 44), (91, 58), (70, 53), (50, 51), (30, 53), (9, 58)], 6)
CHARS['mark-evans'] = {
    'body': 'normal', 'pal': pal('#5a3a26', '#fcbc87', band='#ee6418', band_d='#b8400c', band_l='#ff9a4a'),
    'face': {'eyes': 'big', 'mouth': 'smile'},
    'front': [L(DOME), spk((12, 44), (30, 30), (8, 8), 5), spk((70, 30), (88, 44), (92, 8), 5, light_left=False),
              L(band_front, 'band', 'f'), L(blob([(12, 52), (50, 47), (90, 52), (90, 58), (50, 52), (10, 58)], 4), 'band_d', 'f', False),
              L(blob([(16, 42), (40, 36), (60, 36), (72, 38), (50, 38)], 4), 'band_l', 'f', False),
              spk((40, 30), (60, 30), (50, 52), 2, z='f', ln=True),
              spk((14, 56), (26, 56), (19, 74), 2, z='f'), spk((74, 56), (86, 56), (81, 74), 2, z='f', light_left=False)],
    'side': [L(SIDE_SKULL), spk((14, 54), (30, 30), (2, 16), 7), spk((54, 26), (72, 32), (76, 6), 5, light_left=False),
             L(blob([(13, 52), (30, 38), (50, 32), (70, 34), (88, 44), (88, 60), (70, 54), (50, 54), (30, 60), (14, 66)], 6), 'band', 'f'),
             L(blob([(14, 60), (40, 55), (70, 52), (88, 56), (88, 60), (60, 56), (30, 62), (14, 66)], 4), 'band_d', 'f', False),
             spk((52, 60), (60, 60), (56, 78), 1, z='f')],
    'back': [L(BACK_SKULL), spk((12, 44), (30, 30), (8, 8), 5), spk((70, 30), (88, 44), (92, 8), 5, light_left=False),
             L(band_front, 'band', 'f'), L(blob([(12, 52), (50, 47), (90, 52), (90, 58), (50, 52), (10, 58)], 4), 'band_d', 'f', False)],
}

# ------------------------------------------------------------------ Nathan Swift: coleta alta y flequillo que tapa un ojo
CHARS['nathan-swift'] = {
    'body': 'delgado', 'pal': pal('#679499', '#fac698', iris='#7a3a24', tie='#c84a2a'),
    'face': {'eyes': 'normal', 'mouth': 'line'},
    'front': [L(blob([(10, 100), (6, 60), (14, 30), (36, 14), (64, 14), (86, 30), (94, 60), (90, 104), (80, 96), (74, 70), (26, 70), (20, 96)])),
              spk((72, 24), (90, 38), (104, 6), 6, light_left=False),
              L(blob([(14, 52), (18, 28), (40, 14), (64, 14), (84, 28), (86, 52)]), 'mid', 'f', False),
              spk((12, 44), (54, 40), (30, 98), 9, z='f'),
              spk((46, 42), (68, 42), (60, 66), 3, z='f', light_left=False),
              spk((64, 44), (86, 48), (82, 74), 3, z='f', light_left=False)],
    'side': [L(SIDE_SKULL),
             L(blob([(18, 26), (6, 30), (-6, 56), (-8, 90), (0, 108), (8, 92), (10, 60), (22, 40)])),
             L(blob([(-4, 60), (-6, 90), (0, 104), (4, 84), (4, 62)], 6), 'shade', 'b', False),
             L(ell(18, 30, 5, 6), 'tie', 'b'),
             spk((54, 30), (80, 40), (86, 78), 5, z='f', light_left=False),
             spk((44, 54), (60, 54), (52, 98), 3, z='f')],
    'back': [L(blob([(8, 100), (6, 60), (14, 30), (36, 14), (64, 14), (86, 30), (94, 60), (92, 100), (70, 96), (50, 92), (30, 96)])),
             L(blob([(40, 22), (60, 22), (68, 60), (62, 104), (50, 126), (38, 104), (32, 60)]), 'mid', 'f'),
             L(blob([(52, 30), (62, 60), (58, 100), (50, 120), (54, 70)], 6), 'shade', 'f', False),
             L(ell(50, 22, 6, 5), 'tie', 'f')],
}

# ------------------------------------------------------------------ Jack Wallside: casco de pelo redondo
helmet = blob([(2, 72), (0, 44), (14, 18), (50, 6), (86, 18), (100, 44), (98, 72), (84, 66), (50, 62), (16, 66)])
CHARS['jack-wallside'] = {
    'body': 'corpulento', 'pal': pal('#2f6447', '#c98d70'),
    'face': {'eyes': 'dot', 'eye_y': 78, 'mouth': 'lips', 'ears': False},
    'front': [L(helmet), L(blob([(16, 26), (36, 14), (52, 12), (40, 24), (22, 36)], 6), 'light', 'b', False),
              L(blob([(70, 20), (92, 40), (96, 66), (84, 62), (82, 40)], 6), 'shade', 'b', False)],
    'side': [L(blob([(10, 82), (2, 50), (14, 18), (48, 4), (80, 14), (98, 40), (96, 64), (76, 62), (56, 64), (40, 82)])),
             L(blob([(22, 22), (44, 10), (62, 10), (44, 22), (28, 32)], 6), 'light', 'b', False),
             L(blob([(4, 56), (12, 78), (36, 82), (20, 64)], 6), 'shade', 'b', False)],
    'back': [L(blob([(4, 80), (0, 44), (14, 16), (50, 4), (86, 16), (100, 44), (96, 80), (70, 92), (30, 92)])),
             L(blob([(18, 24), (40, 12), (58, 12), (40, 24), (24, 34)], 6), 'light', 'b', False),
             L(blob([(60, 30), (94, 44), (94, 78), (70, 90), (78, 60)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Jim Wraith: melena lisa que le tapa los ojos
CHARS['jim-wraith'] = {
    'body': 'delgado', 'pal': pal('#c99598', '#fcc48d'),
    'face': {'eyes': 'none', 'mouth': 'line', 'ears': False},
    'front': [L(blob([(8, 120), (6, 60), (14, 26), (36, 12), (64, 12), (86, 26), (94, 60), (92, 120), (78, 120), (74, 84), (26, 84), (22, 120)])),
              L(blob([(84, 40), (92, 70), (90, 118), (80, 118), (82, 70)], 6), 'shade', 'b', False),
              spk((12, 40), (52, 30), (30, 94), 5, z='f'), spk((48, 30), (88, 40), (70, 94), 5, z='f', light_left=False)],
    'side': [L(blob([(46, 40), (18, 40), (8, 80), (10, 124), (30, 124), (42, 96)])),
             L(blob([(48, 64), (40, 32), (54, 14), (80, 22), (88, 46), (76, 50), (60, 50)])),
             L(blob([(14, 60), (12, 100), (16, 122), (26, 122), (22, 96)], 6), 'shade', 'b', False),
             spk((56, 34), (84, 44), (88, 92), 4, z='f', light_left=False),
             spk((44, 50), (60, 50), (50, 112), 3, z='f')],
    'back': [L(blob([(8, 124), (6, 60), (14, 26), (36, 12), (64, 12), (86, 26), (94, 60), (92, 124), (50, 128)])),
             L(blob([(54, 20), (80, 30), (90, 80), (88, 122), (64, 126), (72, 70)], 6), 'shade', 'b', False),
             L(blob([(24, 30), (36, 18), (40, 40), (32, 90), (24, 70)], 6), 'light', 'b', False)],
}

# ------------------------------------------------------------------ Tod Ironside: casquete en punta, nuca rapada y orejas grandes
CHARS['tod-ironside'] = {
    'body': 'bajito', 'pal': pal('#934814', '#ffbe8d', stub='#b98a5a'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'grin', 'big_ears': 2},
    'front': [L(blob([(14, 64), (13, 38), (28, 18), (50, 2), (72, 18), (87, 38), (86, 64), (70, 56), (50, 60), (30, 56)])),
              L(blob([(26, 24), (44, 10), (50, 6), (40, 26), (28, 40)], 6), 'light', 'b', False),
              L(blob([(62, 16), (84, 36), (84, 60), (70, 52)], 6), 'shade', 'b', False)],
    'side': [L(blob([(28, 90), (18, 70), (26, 72), (40, 84)]), 'stub'),
             L(blob([(30, 72), (16, 54), (20, 28), (44, 4), (66, 16), (82, 32), (86, 50), (70, 52), (56, 50), (46, 66)])),
             L(blob([(36, 14), (50, 8), (48, 20), (32, 34)], 6), 'light', 'b', False)],
    'back': [L(blob([(16, 72), (84, 72), (76, 92), (50, 98), (24, 92)]), 'stub'),
             L(blob([(14, 72), (13, 40), (28, 18), (50, 2), (72, 18), (87, 40), (86, 72), (50, 76)])),
             L(blob([(56, 12), (84, 38), (84, 70), (64, 72)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Steve Grim: pelo corto despeinado con un pelo de punta
steve_bangs = [spk((22, 46), (40, 44), (30, 70), 3, z='f'), spk((38, 44), (56, 44), (46, 68), 3, z='f'),
               spk((54, 44), (72, 44), (66, 70), 3, z='f', light_left=False), spk((70, 46), (86, 50), (82, 72), 3, z='f', light_left=False)]
CHARS['steve-grim'] = {
    'body': 'normal', 'pal': pal('#4a3316', '#fac286'),
    'face': {'eyes': 'normal', 'mouth': 'line'},
    'front': [L(fat((46, 18), (54, 18), (58, -2), 2)), L(DOME), spk((10, 56), (24, 48), (12, 86), 3),
              spk((76, 48), (90, 56), (88, 86), 3, light_left=False)] + steve_bangs,
    'side': [L(fat((52, 22), (58, 20), (60, 0), 2)), L(SIDE_SKULL), spk((16, 64), (26, 44), (4, 70), 4), spk((18, 44), (36, 26), (6, 30), 4),
             spk((54, 34), (80, 44), (86, 72), 4, z='f', light_left=False), spk((48, 54), (60, 54), (54, 84), 2, z='f')],
    'back': [L(fat((46, 18), (54, 18), (58, -2), 2)), L(BACK_SKULL), spk((18, 82), (38, 84), (26, 102), 3),
             spk((38, 86), (62, 86), (50, 104), 3), spk((62, 84), (82, 82), (74, 102), 3, light_left=False)],
}

# ------------------------------------------------------------------ Tim Saunders: calvo, un mechón en la frente y coleta enorme
tim_skull = blob([(16, 64), (14, 40), (26, 18), (50, 10), (74, 18), (86, 40), (84, 64)])
CHARS['tim-saunders'] = {
    'body': 'bajito', 'pal': pal('#814407', '#fcbc7a', tie='#c03a2a'),
    'face': {'eyes': 'dot', 'mouth': 'smile'},
    'front': [L(blob([(30, 30), (8, 44), (-8, 84), (-6, 116), (8, 104), (16, 72), (30, 52)])),
              L(blob([(2, 70), (-4, 100), (4, 108), (8, 80)], 6), 'shade', 'b', False),
              L(tim_skull, 'skin'), L(blob([(50, 20), (57, 36), (54, 50), (46, 50), (43, 36)]), 'mid', 'f')],
    'side': [L(blob([(26, 18), (34, 6), (24, -2), (6, 6), (-12, 40), (-16, 92), (-6, 114), (4, 84), (8, 44)])),
             L(blob([(-6, 50), (-10, 92), (-4, 106), (0, 80)], 6), 'shade', 'b', False),
             L(ell(26, 16, 5, 5), 'tie'),
             L(blob([(44, 90), (22, 92), (14, 66), (16, 38), (34, 20), (60, 18), (80, 28), (86, 50), (64, 54)]), 'skin'),
             L(blob([(66, 22), (74, 30), (74, 44), (68, 46), (64, 32)]), 'mid', 'f')],
    'back': [L(BACK_SKULL, 'skin'),
             L(blob([(40, 14), (60, 14), (72, 50), (68, 104), (50, 128), (32, 104), (28, 50)]), 'mid', 'f'),
             L(blob([(54, 22), (68, 50), (64, 100), (50, 120), (58, 70)], 6), 'shade', 'f', False),
             L(ell(50, 16, 7, 5), 'tie', 'f')],
}

# ------------------------------------------------------------------ Sam Kincaid: rizos naranjas que le tapan los ojos
CHARS['sam-kincaid'] = {
    'body': 'normal', 'pal': pal('#d4671a', '#ffcda3'),
    'face': {'eyes': 'none', 'mouth': 'smile', 'ears': False},
    'front': [L(bumpy(50, 50, 52, 44)), L(bumpy(66, 62, 26, 26), 'shade', 'b', False), L(bumpy(34, 34, 18, 14), 'light', 'b', False),
              L(bumpy(50, 70, 38, 18, 10), 'mid', 'f'), L(bumpy(40, 64, 16, 8, 6), 'light', 'f', False)],
    'side': [L(bumpy(44, 48, 46, 44)), L(bumpy(26, 62, 22, 24), 'shade', 'b', False), L(bumpy(46, 30, 18, 12), 'light', 'b', False),
             L(bumpy(70, 66, 18, 16, 8), 'mid', 'f')],
    'back': [L(bumpy(50, 54, 52, 50)), L(bumpy(66, 66, 26, 30), 'shade', 'b', False), L(bumpy(34, 36, 18, 14), 'light', 'b', False)],
}

# ------------------------------------------------------------------ Jude Sharp: rastas recogidas, gafas y capa
dreads_top = [spk((18, 40), (32, 28), (14, 6), 3), spk((30, 28), (46, 22), (34, 0), 3), spk((44, 22), (58, 22), (52, -4), 3),
              spk((56, 22), (70, 28), (68, 0), 3, light_left=False), spk((70, 30), (84, 40), (88, 6), 3, light_left=False)]
CHARS['jude-sharp'] = {
    'body': 'normal', 'cape': '#c8201c', 'pal': pal('#94793d', '#f0c393', strap='#2a3a52', lens='#4a9a4a', lens_l='#a8e0a0'),
    'face': {'eyes': 'none', 'mouth': 'line'},
    'front': dreads_top + [L(DOME), spk((10, 56), (22, 46), (8, 84), 3), spk((78, 46), (90, 56), (92, 84), 3, light_left=False),
                           L(blob([(10, 76), (90, 76), (90, 86), (10, 86)], 3), 'strap', 'f'),
                           L(ell(36, 81, 10, 7.5), 'strap', 'f'), L(ell(64, 81, 10, 7.5), 'strap', 'f'),
                           L(ell(36, 81, 7.5, 5.5), 'lens', 'f', False), L(ell(64, 81, 7.5, 5.5), 'lens', 'f', False),
                           L(ell(33, 79, 2.5, 1.8), 'lens_l', 'f', False), L(ell(61, 79, 2.5, 1.8), 'lens_l', 'f', False)],
    'side': [L(blob([(30, 34), (12, 18), (-8, 28), (-12, 56), (0, 74), (22, 62)])),
             spk((4, 40), (14, 30), (-14, 34), 3), spk((0, 60), (10, 50), (-16, 66), 3), L(SIDE_SKULL),
             spk((30, 26), (50, 20), (22, 6), 3), spk((50, 20), (70, 26), (58, 2), 3, light_left=False),
             L(blob([(42, 78), (90, 76), (90, 86), (42, 86)], 3), 'strap', 'f'),
             L(ell(82, 81, 7, 7.5), 'strap', 'f'), L(ell(82, 81, 5, 5.5), 'lens', 'f', False)],
    'back': [L(bumpy(50, 52, 46, 44, 12, 0.1)), L(bumpy(50, 30, 30, 18, 8, 0.12), 'light', 'b', False),
             L(bumpy(66, 66, 24, 24, 8, 0.1), 'shade', 'b', False),
             L(blob([(6, 76), (94, 76), (94, 84), (6, 84)], 3), 'strap', 'f')],
}

# ------------------------------------------------------------------ Maxwell Carson: gorro de rayas con punta y trenzas
hat_front = blob([(8, 64), (8, 40), (18, 18), (40, 6), (50, 0), (60, 6), (82, 18), (92, 40), (92, 64)])
CHARS['maxwell-carson'] = {
    'body': 'normal', 'pal': pal('#a8502a', '#f2b48c', hat='#dd8276', hat_d='#b55e54', stripe='#7c9a96', bead='#e05a6a'),
    'face': {'eyes': 'big', 'mouth': 'smile'},
    'front': [L(blob([(10, 60), (18, 60), (19, 104), (14, 110), (9, 104)]), 'mid', 'b'), L(blob([(82, 60), (90, 60), (91, 104), (86, 110), (81, 104)]), 'mid', 'b'),
              L(ell(14, 106, 3, 3), 'bead', 'b'), L(ell(86, 106, 3, 3), 'bead', 'b'),
              spk((26, 60), (44, 60), (34, 72), 2, z='f'), spk((56, 60), (74, 60), (66, 72), 2, z='f', light_left=False),
              L(hat_front, 'hat', 'f'), L(blob([(11, 36), (89, 36), (90, 47), (10, 47)], 3), 'stripe', 'f', False),
              L(blob([(56, 10), (90, 40), (92, 64), (72, 62)], 6), 'hat_d', 'f', False)],
    'side': [L(SIDE_SKULL), spk((16, 62), (36, 62), (6, 98), 4), L(blob([(52, 60), (58, 60), (59, 100), (55, 106), (51, 100)]), 'mid', 'f'),
             L(ell(55, 102, 3, 3), 'bead', 'f'),
             L(blob([(10, 72), (8, 40), (22, 14), (46, 2), (70, 8), (86, 26), (90, 58), (60, 60)]), 'hat', 'f'),
             L(blob([(11, 44), (86, 38), (89, 49), (10, 55)], 3), 'stripe', 'f', False)],
    'back': [L(blob([(18, 60), (82, 60), (76, 96), (50, 104), (24, 96)])), L(blob([(50, 64), (78, 64), (72, 94), (52, 100)], 6), 'shade', 'b', False),
             L(hat_front, 'hat', 'f'), L(blob([(11, 36), (89, 36), (90, 47), (10, 47)], 3), 'stripe', 'f', False)],
}

# ------------------------------------------------------------------ Kevin Dragonfly: rapado rosa y cara de enfado
CHARS['kevin-dragonfly'] = {
    'body': 'normal', 'pal': pal('#c66c66', '#cf9667'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown'},
    'front': [L(blob([(16, 62), (14, 38), (26, 20), (50, 14), (74, 20), (86, 38), (84, 62), (72, 54), (50, 50), (28, 54)])),
              L(blob([(60, 18), (84, 36), (84, 58), (70, 52)], 6), 'shade', 'b', False)],
    'side': [L(blob([(38, 72), (18, 62), (16, 34), (36, 16), (62, 16), (80, 30), (84, 48), (64, 46), (50, 54)])),
             L(blob([(20, 50), (22, 66), (36, 70)], 6), 'shade', 'b', False)],
    'back': [L(blob([(16, 74), (14, 38), (26, 20), (50, 14), (74, 20), (86, 38), (84, 74), (66, 88), (34, 88)])),
             L(blob([(56, 20), (84, 40), (84, 72), (62, 86)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ William Glass: pelo con puntas abiertas y gafas
CHARS['william-glass'] = {
    'body': 'bajito', 'pal': pal('#412d1b', '#f1b46c'),
    'face': {'eyes': 'normal', 'mouth': 'smile', 'glasses': (40, 70, 50, 255)},
    'front': [L(blob([(14, 62), (10, 40), (22, 20), (50, 12), (78, 20), (90, 40), (86, 62)])),
              spk((8, 46), (18, 62), (-4, 74), 4), spk((82, 62), (92, 46), (104, 74), 4, light_left=False),
              spk((20, 44), (50, 38), (28, 68), 5, z='f'), spk((50, 38), (80, 44), (72, 68), 5, z='f', light_left=False)],
    'side': [L(SIDE_SKULL), spk((14, 62), (24, 44), (0, 76), 5), spk((54, 34), (82, 46), (86, 70), 4, z='f', light_left=False)],
    'back': [L(BACK_SKULL), spk((8, 46), (18, 62), (-4, 74), 4), spk((82, 62), (92, 46), (104, 74), 4, light_left=False),
             L(blob([(56, 22), (84, 40), (84, 66), (66, 88)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Bobby Shearer: pelo corto en punta, gris verdoso
CHARS['bobby-shearer'] = {
    'body': 'delgado', 'pal': pal('#88a494', '#cf9d65'),
    'face': {'eyes': 'normal', 'mouth': 'line'},
    'front': [spk((14, 42), (30, 28), (8, 10), 4), spk((28, 28), (46, 22), (28, 4), 4), spk((42, 22), (60, 22), (52, 0), 4),
              spk((56, 22), (72, 28), (72, 4), 4, light_left=False), spk((70, 28), (86, 42), (92, 10), 4, light_left=False),
              L(blob([(16, 60), (14, 40), (26, 24), (50, 20), (74, 24), (86, 40), (84, 60), (70, 54), (50, 52), (30, 54)]))],
    'side': [L(SIDE_SKULL), spk((16, 56), (28, 36), (0, 30), 4), spk((24, 36), (44, 24), (14, 8), 4), spk((42, 24), (62, 22), (46, 2), 4),
             spk((60, 22), (76, 30), (78, 4), 4, light_left=False)],
    'back': [spk((14, 42), (30, 28), (8, 10), 4), spk((28, 28), (46, 22), (28, 4), 4), spk((42, 22), (60, 22), (52, 0), 4),
             spk((56, 22), (72, 28), (72, 4), 4, light_left=False), spk((70, 28), (86, 42), (92, 10), 4, light_left=False),
             L(blob([(16, 70), (14, 40), (26, 24), (50, 20), (74, 24), (86, 40), (84, 70), (64, 82), (36, 82)]))],
}

# ------------------------------------------------------------------ Erik Eagle: flequillo en ola y puntas hacia fuera
CHARS['erik-eagle'] = {
    'body': 'normal', 'pal': pal('#5a3a26', '#fcbb7a'),
    'face': {'eyes': 'big', 'mouth': 'smile'},
    'front': [L(DOME), spk((12, 62), (20, 48), (-2, 46), 5), spk((80, 48), (88, 62), (102, 46), 5, light_left=False),
              spk((14, 44), (52, 36), (22, 72), 7, z='f'), spk((46, 38), (78, 42), (66, 68), 5, z='f', light_left=False),
              spk((74, 46), (88, 54), (86, 74), 3, z='f', light_left=False)],
    'side': [L(SIDE_SKULL), spk((14, 60), (24, 42), (-4, 50), 6), spk((20, 40), (40, 24), (6, 18), 6),
             spk((54, 30), (82, 44), (88, 72), 5, z='f', light_left=False)],
    'back': [L(BACK_SKULL), spk((12, 62), (20, 48), (-2, 46), 5), spk((80, 48), (88, 62), (102, 46), 5, light_left=False),
             spk((18, 84), (40, 86), (24, 104), 4), spk((40, 88), (60, 88), (50, 106), 4), spk((60, 86), (82, 84), (76, 104), 4, light_left=False)],
}
