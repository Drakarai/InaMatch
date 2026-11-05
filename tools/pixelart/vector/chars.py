"""Personajes dibujados en vectores: colores, tipo de cuerpo y el pelo en tres vistas (frente, perfil, espalda).

Referencia: los modelos 3D de la enciclopedia oficial (zukan.inazuma.jp/chara_model_view). Coordenadas como en
heads.py (la cabeza mide 100 de ancho; de perfil mira a la derecha).
"""
import math

from heads import L, blob, ell, fat, mirror, spk, strand


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
    # coleta alta (asoma por detrás de la cabeza), mechones largos a los lados y flequillo que le tapa el ojo derecho
    'front': [L(blob([(20, 34), (6, 30), (0, 52), (8, 70), (18, 54)])), L(blob([(80, 34), (94, 30), (100, 52), (92, 70), (82, 54)])),
              L(blob([(12, 70), (10, 44), (20, 22), (44, 12), (66, 14), (84, 26), (90, 46), (88, 70)])),
              spk((10, 56), (24, 52), (14, 98), 3), spk((76, 52), (90, 56), (86, 98), 3, light_left=False),
              spk((12, 42), (56, 34), (34, 96), 8, z='f'), spk((50, 36), (70, 38), (60, 62), 3, z='f', light_left=False),
              spk((66, 40), (88, 48), (82, 70), 3, z='f', light_left=False),
              strand([(26, 24), (44, 16), (64, 18)], 'shade', 'b', 1.2)],
    'side': [L(blob([(28, 24), (14, 10), (0, 18), (-4, 44), (-2, 74), (4, 96), (12, 82), (14, 58), (20, 40)])),
             spk((-2, 70), (8, 72), (-6, 96), 3), spk((6, 76), (14, 72), (10, 98), 3, light_left=False),
             strand([(4, 22), (0, 50), (2, 80)], 'shade', 'b', 1.4),
             L(blob([(40, 96), (20, 90), (12, 68), (14, 42), (28, 20), (54, 12), (78, 20), (88, 40), (74, 46), (60, 50), (52, 64), (50, 84)])),
             L(ell(26, 24, 4.5, 5.5), 'tie'),
             spk((54, 28), (84, 42), (88, 78), 5, z='f', light_left=False), spk((46, 52), (58, 52), (54, 96), 2, z='f'),
             strand([(30, 28), (46, 18), (64, 16)], 'shade', 'b', 1.2)],
    'back': [L(blob([(12, 70), (10, 44), (20, 22), (44, 12), (66, 14), (84, 26), (90, 46), (88, 70), (80, 92), (50, 98), (20, 92)])),
             L(blob([(44, 20), (56, 20), (66, 44), (64, 80), (56, 104), (44, 104), (36, 80), (34, 44)]), 'mid', 'f', ln=True),
             L(blob([(52, 26), (64, 46), (62, 80), (56, 100), (54, 60)], 6), 'shade', 'f', False),
             spk((34, 84), (48, 90), (34, 112), 3, z='f'), spk((44, 92), (56, 92), (50, 116), 3, z='f'),
             spk((52, 90), (66, 84), (66, 112), 3, z='f', light_left=False),
             strand([(50, 26), (48, 60), (50, 96)], 'shade', 'f', 1.4), strand([(42, 30), (38, 70)], 'shade', 'f', 1.0),
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
    # melena lisa hasta los hombros, con raya en medio y el flequillo tapándole los ojos
    'front': [L(blob([(8, 120), (6, 60), (14, 26), (36, 12), (64, 12), (86, 26), (94, 60), (92, 120), (78, 120), (74, 84), (26, 84), (22, 120)])),
              L(blob([(84, 40), (92, 70), (90, 118), (80, 118), (82, 70)], 6), 'shade', 'b', False),
              L(blob([(16, 46), (34, 30), (50, 28), (66, 30), (84, 46), (84, 82), (70, 88), (60, 84), (50, 88), (40, 84), (30, 88), (16, 82)]), 'mid', 'f'),
              L(blob([(52, 30), (68, 32), (82, 48), (82, 80), (70, 84), (62, 60)], 6), 'shade', 'f', False),
              L(blob([(24, 40), (34, 34), (30, 60), (24, 72)], 6), 'light', 'f', False),
              strand([(50, 28), (48, 60), (50, 86)], 'deep', 'f', 1.2), strand([(36, 40), (32, 84)], 'shade', 'f', 1.0),
              strand([(66, 40), (70, 84)], 'deep', 'f', 1.0)],
    'side': [L(blob([(48, 30), (20, 30), (8, 70), (8, 124), (30, 124), (44, 96)])),
             L(blob([(40, 96), (20, 90), (12, 68), (14, 42), (28, 20), (54, 12), (78, 20), (88, 40), (74, 46), (60, 50), (52, 64), (50, 84)])),
             L(blob([(14, 60), (12, 100), (16, 122), (26, 122), (22, 96)], 6), 'shade', 'b', False),
             spk((52, 26), (86, 42), (88, 90), 4, z='f', light_left=False), spk((44, 50), (60, 50), (50, 112), 3, z='f'),
             strand([(26, 30), (16, 70), (18, 118)], 'shade', 'b', 1.2)],
    'back': [L(blob([(8, 124), (6, 60), (14, 26), (36, 12), (64, 12), (86, 26), (94, 60), (92, 124), (50, 128)])),
             L(blob([(54, 20), (80, 30), (90, 80), (88, 122), (64, 126), (72, 70)], 6), 'shade', 'b', False),
             L(blob([(24, 30), (36, 18), (40, 40), (32, 90), (24, 70)], 6), 'light', 'b', False),
             strand([(50, 14), (48, 70), (50, 124)], 'deep', 'b', 1.2), strand([(30, 30), (24, 120)], 'shade', 'b', 1.0)],
}

# ------------------------------------------------------------------ Tod Ironside: casquete en punta, nuca rapada y orejas grandes
CHARS['tod-ironside'] = {
    'body': 'bajito', 'pal': pal('#934814', '#ffbe8d', stub='#b98a5a'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'grin', 'big_ears': 2},
    # pelo en forma de bellota: punta arriba y casquete que baja por los lados hasta las orejas
    'front': [L(blob([(14, 74), (13, 40), (28, 18), (50, 2), (72, 18), (87, 40), (86, 74), (80, 66), (74, 56), (50, 58), (26, 56), (20, 66)])),
              L(blob([(26, 24), (44, 10), (50, 6), (40, 26), (28, 40)], 6), 'light', 'b', False),
              L(blob([(62, 16), (84, 36), (85, 70), (72, 56)], 6), 'shade', 'b', False)],
    'side': [L(blob([(40, 96), (22, 90), (16, 74), (30, 76), (44, 84)]), 'stub'),
             L(blob([(28, 78), (16, 58), (20, 30), (44, 4), (66, 14), (82, 30), (86, 48), (70, 50), (58, 52), (52, 64), (44, 78)])),
             L(blob([(36, 14), (50, 8), (48, 20), (32, 34)], 6), 'light', 'b', False),
             L(blob([(18, 54), (22, 74), (34, 78), (26, 62)], 6), 'shade', 'b', False)],
    'back': [L(blob([(16, 72), (84, 72), (76, 92), (50, 98), (24, 92)]), 'stub'),
             L(blob([(14, 74), (13, 40), (28, 18), (50, 2), (72, 18), (87, 40), (86, 74), (50, 78)])),
             L(blob([(56, 12), (84, 38), (84, 70), (64, 74)], 6), 'shade', 'b', False),
             L(blob([(30, 24), (44, 10), (40, 28)], 4), 'light', 'b', False)],
}

# ------------------------------------------------------------------ Steve Grim: pelo corto despeinado con un pelo de punta
steve_bangs = [spk((22, 46), (40, 44), (30, 70), 3, z='f'), spk((38, 44), (56, 44), (46, 68), 3, z='f'),
               spk((54, 44), (72, 44), (66, 70), 3, z='f', light_left=False), spk((70, 46), (86, 50), (82, 72), 3, z='f', light_left=False)]
steve_bangs = [spk((22, 46), (40, 44), (30, 70), 3, z='f'), spk((38, 44), (56, 44), (46, 68), 3, z='f'),
               spk((54, 44), (72, 44), (66, 70), 3, z='f', light_left=False), spk((70, 46), (86, 50), (82, 72), 3, z='f', light_left=False)]
CHARS['steve-grim'] = {
    'body': 'normal', 'pal': pal('#4a3316', '#fac286'),
    'face': {'eyes': 'normal', 'mouth': 'line'},
    # pelo despeinado que cae en mechones hasta la nuca, con un pelo de punta arriba
    'front': [L(fat((46, 18), (54, 18), (58, -2), 2)), L(DOME), spk((10, 56), (24, 48), (12, 86), 3),
              spk((76, 48), (90, 56), (88, 86), 3, light_left=False)] + steve_bangs,
    'side': [L(fat((50, 20), (56, 18), (60, -2), 2)),
             L(blob([(40, 96), (20, 92), (10, 70), (12, 44), (26, 20), (54, 12), (78, 20), (88, 40), (74, 46), (60, 52), (52, 64), (50, 82)])),
             spk((10, 76), (22, 84), (8, 100), 3), spk((24, 88), (38, 94), (24, 106), 3), spk((40, 92), (50, 88), (46, 104), 2),
             spk((54, 30), (84, 42), (88, 72), 5, z='f', light_left=False), spk((50, 54), (60, 54), (56, 80), 2, z='f'),
             strand([(20, 34), (36, 22), (56, 18)], 'shade', 'b', 1.2)],
    'back': [L(fat((46, 18), (54, 18), (58, -2), 2)), L(BACK_SKULL), spk((18, 82), (38, 84), (26, 102), 3),
             spk((38, 86), (62, 86), (50, 104), 3), spk((62, 84), (82, 82), (74, 102), 3, light_left=False),
             L(blob([(58, 20), (84, 40), (84, 70), (66, 86)], 6), 'shade', 'b', False)],
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
    # melena de rizos que le tapa los ojos: masa de bultos con sombras en los rizos de abajo y de la derecha
    'front': [L(bumpy(50, 48, 50, 42)), L(bumpy(70, 58, 22, 24, 10), 'shade', 'b', False),
              L(bumpy(50, 64, 40, 24, 10), 'mid', 'f'), L(bumpy(66, 74, 18, 12, 6), 'shade', 'f', False),
              L(ell(34, 26, 8, 4), 'light', 'b', False), L(ell(30, 66, 6, 3), 'light', 'f', False),
              strand([(30, 44), (40, 40), (50, 44)], 'shade', 'b', 1.2), strand([(58, 34), (68, 30), (76, 36)], 'shade', 'b', 1.2)],
    'side': [L(bumpy(46, 46, 44, 42)), L(bumpy(28, 60, 20, 24, 10), 'shade', 'b', False),
             L(bumpy(72, 66, 16, 16, 8), 'mid', 'f'), L(ell(46, 22, 8, 4), 'light', 'b', False),
             strand([(30, 36), (42, 30), (54, 34)], 'shade', 'b', 1.2)],
    'back': [L(bumpy(50, 54, 50, 48)), L(bumpy(68, 66, 24, 30, 10), 'shade', 'b', False), L(ell(34, 28, 8, 4), 'light', 'b', False),
             strand([(28, 50), (40, 44), (52, 50)], 'shade', 'b', 1.2), strand([(40, 74), (52, 70), (64, 76)], 'shade', 'b', 1.2)],
}

# ------------------------------------------------------------------ Jude Sharp: rastas recogidas, gafas y capa
def dread_ridges(x0, x1, ys, z='b'):
    """Rastas: crestas horizontales en la masa de pelo."""
    return [strand([(x0 + 4 * (i % 2), y), ((x0 + x1) / 2, y - 3), (x1 - 4 * (i % 2), y)], 'deep', z, 1.1) for i, y in enumerate(ys)]


CHARS['jude-sharp'] = {
    'body': 'normal', 'cape': '#c8201c', 'pal': pal('#94793d', '#f0c393', strap='#2a3a52', lens='#4a9a4a', lens_l='#a8e0a0'),
    'face': {'eyes': 'none', 'mouth': 'line'},
    # rastas recogidas hacia atrás (de frente se ve una masa con crestas), rastas a los lados y gafas de natación
    'front': [L(blob([(12, 68), (10, 40), (18, 18), (36, 6), (50, 4), (64, 6), (82, 18), (90, 40), (88, 68), (80, 56), (50, 50), (20, 56)])),
              L(blob([(60, 10), (84, 30), (88, 62), (74, 54)], 6), 'shade', 'b', False)] + dread_ridges(22, 78, [18, 28, 38, 48]) + [
              spk((8, 58), (20, 52), (10, 90), 3), spk((80, 52), (92, 58), (90, 90), 3, light_left=False),
              L(blob([(18, 77), (82, 77), (82, 85), (18, 85)], 3), 'strap', 'f'),
              L(ell(36, 81, 10, 7.5), 'strap', 'f'), L(ell(64, 81, 10, 7.5), 'strap', 'f'),
              L(ell(36, 81, 7.5, 5.5), 'lens', 'f', False), L(ell(64, 81, 7.5, 5.5), 'lens', 'f', False),
              L(ell(33, 79, 2.5, 1.8), 'lens_l', 'f', False), L(ell(61, 79, 2.5, 1.8), 'lens_l', 'f', False)],
    'side': [L(bumpy(10, 38, 20, 24, 8, 0.08)), L(bumpy(4, 44, 10, 14, 6), 'shade', 'b', False),
             L(blob([(40, 96), (20, 90), (12, 68), (14, 42), (28, 18), (54, 10), (78, 18), (88, 40), (74, 46), (60, 50), (52, 64), (50, 84)]))] + [
             strand([(24 + 6 * i, 22 + 2 * i), (14 + 6 * i, 40 + 6 * i)], 'deep', 'b', 1.1) for i in range(5)] + [
             L(blob([(44, 78), (88, 76), (88, 86), (44, 86)], 3), 'strap', 'f'),
             L(ell(82, 81, 7, 7.5), 'strap', 'f'), L(ell(82, 81, 5, 5.5), 'lens', 'f', False)],
    'back': [L(bumpy(50, 50, 44, 44, 12, 0.08)), L(bumpy(66, 62, 22, 26, 8), 'shade', 'b', False)] + dread_ridges(16, 84, [28, 40, 52, 64, 76]) + [
             L(blob([(12, 76), (88, 76), (88, 83), (12, 83)], 3), 'strap', 'f')],
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
              L(blob([(72, 20), (88, 40), (90, 62), (80, 62)], 6), 'hat_d', 'f', False)],
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
    # rapado: casquete pegado a la cabeza con entradas en la frente
    'front': [L(blob([(17, 66), (15, 40), (26, 22), (50, 16), (74, 22), (85, 40), (83, 66), (78, 58), (66, 52), (58, 56), (50, 54), (42, 56), (34, 52), (22, 58)])),
              L(blob([(62, 20), (82, 36), (83, 60), (72, 52)], 6), 'shade', 'b', False),
              L(blob([(30, 24), (44, 19), (36, 30)], 4), 'light', 'b', False)],
    'side': [L(blob([(42, 92), (24, 86), (16, 62), (20, 34), (38, 18), (62, 18), (80, 30), (84, 46), (68, 48), (56, 54), (50, 66), (52, 80)])),
             L(blob([(22, 62), (26, 84), (40, 90), (30, 72)], 6), 'shade', 'b', False),
             L(blob([(40, 24), (58, 20), (46, 30)], 4), 'light', 'b', False)],
    'back': [L(blob([(16, 74), (14, 40), (26, 20), (50, 14), (74, 20), (86, 40), (84, 74), (70, 90), (50, 94), (30, 90)])),
             L(blob([(58, 20), (84, 40), (84, 72), (64, 88)], 6), 'shade', 'b', False),
             L(blob([(30, 26), (46, 18), (36, 34)], 4), 'light', 'b', False)],
}

# ------------------------------------------------------------------ William Glass: pelo con puntas abiertas y gafas
CHARS['william-glass'] = {
    'body': 'bajito', 'pal': pal('#412d1b', '#f1b46c'),
    'face': {'eyes': 'normal', 'mouth': 'smile', 'glasses': (40, 70, 50, 255)},
    # pelo ancho y liso, con las puntas de los lados hacia fuera a la altura de las orejas
    'front': [L(blob([(14, 66), (10, 40), (22, 18), (50, 10), (78, 18), (90, 40), (86, 66), (82, 60), (18, 60)])),
              spk((10, 44), (20, 60), (-4, 64), 4), spk((80, 60), (90, 44), (104, 64), 4, light_left=False),
              spk((16, 42), (38, 36), (22, 64), 4, z='f'), spk((34, 36), (52, 34), (42, 62), 4, z='f'),
              spk((48, 34), (66, 36), (58, 62), 4, z='f', light_left=False), spk((62, 36), (84, 42), (78, 64), 4, z='f', light_left=False),
              L(blob([(58, 16), (86, 38), (86, 60), (70, 54)], 6), 'shade', 'b', False)],
    'side': [L(blob([(40, 94), (20, 90), (10, 68), (12, 42), (26, 18), (54, 10), (78, 18), (88, 40), (74, 46), (60, 50), (52, 64), (50, 82)])),
             spk((8, 66), (18, 78), (-2, 84), 3),
             spk((54, 26), (86, 40), (90, 64), 5, z='f', light_left=False),
             L(blob([(14, 50), (16, 76), (36, 90), (26, 66)], 6), 'shade', 'b', False)],
    'back': [L(blob([(12, 66), (10, 40), (22, 18), (50, 10), (78, 18), (90, 40), (88, 66), (78, 88), (50, 94), (22, 88)])),
             spk((10, 44), (20, 60), (-4, 64), 4), spk((80, 60), (90, 44), (104, 64), 4, light_left=False),
             L(blob([(56, 18), (86, 40), (86, 66), (70, 86)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Bobby Shearer: pelo corto en punta, gris verdoso
bobby_top = [spk((18, 40), (30, 30), (16, 14), 3), spk((28, 30), (40, 24), (30, 6), 3), spk((38, 24), (52, 22), (44, 2), 3),
             spk((50, 22), (62, 24), (60, 2), 3, light_left=False), spk((60, 24), (72, 30), (72, 6), 3, light_left=False),
             spk((70, 30), (82, 40), (84, 14), 3, light_left=False)]
CHARS['bobby-shearer'] = {
    'body': 'delgado', 'pal': pal('#88a494', '#cf9d65'),
    'face': {'eyes': 'normal', 'mouth': 'line'},
    # pelo corto de punta hacia arriba, pegado por los lados
    'front': bobby_top + [L(blob([(17, 60), (15, 40), (26, 26), (50, 22), (74, 26), (85, 40), (83, 60), (72, 52), (50, 50), (28, 52)])),
                          L(blob([(62, 26), (84, 40), (83, 58), (72, 52)], 6), 'shade', 'b', False)],
    'side': [spk((18, 46), (28, 32), (6, 22), 3), spk((26, 32), (40, 24), (20, 6), 3), spk((38, 24), (52, 20), (40, 0), 3),
             spk((50, 20), (64, 22), (60, 0), 3, light_left=False), spk((62, 22), (76, 30), (78, 8), 3, light_left=False),
             L(blob([(40, 92), (22, 88), (14, 64), (16, 40), (30, 24), (56, 20), (78, 28), (84, 42), (70, 46), (58, 50), (52, 64), (50, 82)])),
             L(blob([(18, 58), (22, 80), (38, 88), (28, 68)], 6), 'shade', 'b', False)],
    'back': bobby_top + [L(blob([(16, 70), (14, 40), (26, 26), (50, 22), (74, 26), (86, 40), (84, 70), (66, 86), (34, 86)])),
                         L(blob([(58, 26), (84, 42), (84, 68), (66, 84)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Erik Eagle: flequillo en ola y puntas hacia fuera
CHARS['erik-eagle'] = {
    'body': 'normal', 'pal': pal('#5a3a26', '#fcbb7a'),
    'face': {'eyes': 'big', 'mouth': 'smile'},
    # pelo voluminoso peinado hacia un lado, con las puntas de abajo abiertas hacia fuera junto a las orejas
    'front': [L(blob([(12, 66), (10, 40), (22, 18), (50, 10), (78, 16), (92, 36), (90, 62), (84, 70), (80, 60), (20, 60), (16, 70)])),
              spk((10, 46), (20, 62), (-2, 70), 4), spk((80, 62), (90, 46), (102, 70), 4, light_left=False),
              spk((14, 42), (36, 34), (18, 68), 4, z='f'), spk((30, 36), (52, 32), (36, 66), 4, z='f'),
              spk((48, 32), (68, 34), (58, 62), 4, z='f', light_left=False), spk((64, 36), (88, 44), (82, 68), 4, z='f', light_left=False),
              strand([(30, 22), (44, 18), (60, 20)], 'shade', 'b', 1.2)],
    'side': [L(blob([(40, 94), (20, 90), (10, 70), (12, 44), (26, 20), (54, 12), (78, 20), (88, 40), (74, 46), (60, 52), (52, 64), (50, 82)])),
             spk((14, 84), (26, 88), (4, 98), 3), spk((30, 92), (42, 94), (24, 104), 3),
             spk((54, 26), (86, 40), (90, 68), 5, z='f', light_left=False),
             strand([(22, 30), (40, 20), (60, 18)], 'shade', 'b', 1.2), strand([(16, 56), (24, 40), (36, 30)], 'shade', 'b', 1.2)],
    'back': [L(blob([(12, 66), (10, 40), (22, 18), (50, 10), (78, 18), (90, 40), (88, 66), (78, 88), (50, 96), (22, 88)])),
             spk((16, 82), (34, 88), (14, 102), 4), spk((34, 90), (50, 92), (38, 106), 4), spk((50, 92), (66, 90), (62, 106), 4, light_left=False),
             spk((66, 88), (84, 82), (86, 102), 4, light_left=False),
             L(blob([(58, 18), (86, 38), (86, 66), (70, 84)], 6), 'shade', 'b', False),
             strand([(30, 24), (46, 16), (62, 18)], 'shade', 'b', 1.2)],
}
