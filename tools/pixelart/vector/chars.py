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


def sheen(x0, x1, y, h=4, c='light', z='b'):
    """Brillo del pelo: una media luna fina sobre la parte iluminada."""
    return L(quad_band(x0, x1, y, h), c, z, False)


def quad_band(x0, x1, y, h):
    from heads import quad
    mid = (x0 + x1) / 2
    return quad((x0, y + h), (mid, y - h * 1.6), (x1, y + h)) + quad((x1, y + h), (mid, y - h * 0.2), (x0, y + h))[1:]


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

# ------------------------------------------------------------------ Mark Evans: cinta naranja ancha, dos mechones de punta
# arriba, un mechón en V que cae sobre la cinta, patillas bajo la cinta y, de perfil, un mechón que se curva hacia atrás
MARK_BAND = blob([(12, 42), (30, 35), (50, 33), (70, 35), (88, 42), (88, 54), (70, 51), (50, 50), (30, 51), (12, 54)], 6)
MARK_BAND_D = blob([(13, 51), (50, 46), (87, 51), (87, 55), (50, 51), (13, 55)], 4)
CHARS['mark-evans'] = {
    'body': 'normal', 'pal': pal('#5a3a26', '#fcbc87', band='#ee6418', band_d='#b8400c', band_l='#ff9a4a'),
    'face': {'eyes': 'big', 'mouth': 'smile', 'hairline': (60, 56)},
    'front': [L(blob([(14, 66), (12, 42), (24, 22), (50, 16), (76, 22), (88, 42), (86, 66), (76, 58), (24, 58)])),
              spk((12, 40), (30, 30), (8, 6), 5), spk((70, 30), (88, 40), (92, 6), 5, light_left=False),
              sheen(30, 62, 24, 3),
              L(MARK_BAND, 'band', 'f'), L(MARK_BAND_D, 'band_d', 'f', False), L(quad_band(24, 58, 38, 2), 'band_l', 'f', False),
              spk((40, 30), (60, 30), (50, 58), 2, z='f', ln=True),
              spk((14, 50), (28, 50), (19, 76), 2, z='f'), spk((72, 50), (86, 50), (81, 76), 2, z='f', light_left=False),
              spk((26, 50), (36, 50), (30, 62), 1.5, z='f'), spk((64, 50), (74, 50), (70, 62), 1.5, z='f', light_left=False)],
    'side': [L(blob([(48, 92), (26, 88), (14, 66), (14, 40), (28, 22), (52, 16), (74, 22), (86, 38), (84, 52), (66, 54), (56, 60), (52, 76)])),
             spk((18, 42), (38, 28), (-2, 22), 9),
             spk((46, 26), (62, 24), (58, 8), 3, light_left=False),
             spk((20, 80), (34, 88), (24, 98), 2), spk((34, 88), (46, 92), (40, 100), 2),
             L(blob([(13, 40), (40, 33), (70, 33), (87, 40), (87, 54), (70, 51), (40, 51), (14, 55)], 6), 'band', 'f'),
             L(blob([(14, 50), (50, 47), (88, 50), (88, 55), (50, 52), (14, 55)], 4), 'band_d', 'f', False),
             spk((54, 52), (64, 52), (58, 74), 1.5, z='f'),
             L(blob([(18, 56), (20, 80), (40, 88), (30, 66)], 6), 'shade', 'b', False)],
    'back': [L(blob([(16, 66), (12, 42), (24, 22), (50, 16), (76, 22), (88, 42), (84, 66), (72, 86), (60, 94), (40, 94), (28, 86)])),
             spk((12, 40), (30, 30), (8, 6), 5), spk((70, 30), (88, 40), (92, 6), 5, light_left=False),
             L(blob([(58, 54), (82, 58), (76, 84), (60, 92)], 6), 'shade', 'b', False),
             spk((36, 86), (50, 88), (42, 100), 2), spk((50, 88), (64, 86), (58, 100), 2, light_left=False),
             L(MARK_BAND, 'band', 'f'), L(MARK_BAND_D, 'band_d', 'f', False)],
}

# ------------------------------------------------------------------ Nathan Swift: coleta alta y flequillo que tapa un ojo
CHARS['nathan-swift'] = {
    'body': 'delgado', 'pal': pal('#679499', '#fac698', iris='#7a3a24', tie='#c84a2a'),
    'face': {'eyes': 'normal', 'mouth': 'smile', 'hairline': (64, 50)},
    # coleta alta en la coronilla (asoma por arriba a la derecha), mechones largos a los lados hasta la barbilla y un
    # mechón grande que baja en diagonal y le tapa el ojo izquierdo
    'front': [L(blob([(54, 18), (66, 2), (84, 0), (94, 14), (90, 34), (76, 26)])),
              L(blob([(12, 70), (10, 44), (20, 22), (44, 12), (66, 14), (84, 26), (90, 46), (88, 70)])),
              spk((8, 48), (22, 52), (12, 100), 3), spk((78, 52), (92, 48), (88, 100), 3, light_left=False),
              L(blob([(70, 6), (88, 6), (90, 26), (78, 22)], 6), 'shade', 'b', False),
              sheen(22, 48, 26, 3),
              spk((16, 46), (36, 42), (24, 68), 3, z='f'),
              L(blob([(26, 42), (52, 34), (74, 40), (82, 62), (80, 94), (72, 100), (64, 84), (54, 64), (40, 50)]), 'mid', 'f', ln=True),
              L(blob([(60, 44), (76, 52), (78, 90), (70, 94), (66, 70)], 6), 'shade', 'f', False),
              L(blob([(34, 42), (50, 38), (44, 46)], 4), 'light', 'f', False),
              strand([(44, 44), (60, 62), (70, 90)], 'shade', 'f', 1.1)],
    'side': [L(blob([(34, 22), (22, 12), (8, 18), (0, 40), (-4, 72), (0, 106), (8, 112), (14, 88), (16, 60), (22, 38)])),
             spk((-4, 80), (6, 82), (-6, 110), 3), spk((6, 84), (14, 80), (12, 112), 3, light_left=False),
             strand([(10, 24), (4, 56), (4, 96)], 'shade', 'b', 1.4),
             L(blob([(46, 92), (24, 88), (14, 66), (14, 40), (28, 20), (54, 12), (78, 20), (88, 40), (74, 46), (60, 50), (52, 64), (50, 84)])),
             L(blob([(20, 50), (20, 74), (40, 88), (30, 64)], 6), 'shade', 'b', False),
             L(ell(30, 22, 4.5, 5.5), 'tie'), sheen(36, 62, 22, 3),
             spk((54, 28), (84, 40), (90, 86), 6, z='f', light_left=False), spk((46, 52), (58, 52), (52, 98), 2, z='f')],
    'back': [L(blob([(12, 70), (10, 44), (20, 22), (44, 12), (66, 14), (84, 26), (90, 46), (88, 70), (80, 92), (50, 98), (20, 92)])),
             L(blob([(58, 18), (84, 36), (86, 70), (70, 90)], 6), 'shade', 'b', False),
             L(blob([(44, 16), (56, 16), (70, 44), (72, 84), (64, 116), (36, 116), (28, 84), (30, 44)]), 'mid', 'f', ln=True),
             L(blob([(52, 24), (68, 46), (68, 86), (60, 112), (54, 70)], 6), 'shade', 'f', False),
             spk((28, 96), (42, 100), (30, 124), 3, z='f'), spk((40, 102), (60, 102), (50, 128), 3, z='f'),
             spk((58, 100), (72, 96), (70, 124), 3, z='f', light_left=False),
             strand([(46, 30), (40, 70), (42, 110)], 'shade', 'f', 1.1),
             L(ell(50, 18, 6, 5), 'tie', 'f')],
}

# ------------------------------------------------------------------ Jack Wallside: casco de pelo verde muy bajo (le llega a las
# cejas), cara ancha y corta, nariz redonda, labios gruesos y patillas que bajan por las mejillas hasta una perilla
JACK_FACE = blob([(12, 58), (88, 58), (90, 74), (82, 90), (64, 98), (50, 99), (36, 98), (18, 90), (10, 74)])
CHARS['jack-wallside'] = {
    'body': 'corpulento', 'pal': pal('#2f6447', '#c98d70', nose='#d8704a'),
    'face': {'eyes': 'round', 'eye_y': 67, 'eye_sep': 13, 'brows': False, 'mouth': 'lips', 'mouth_y': 86, 'ears': True,
             'face_front': JACK_FACE, 'nose': (50, 76, 5), 'ear_out': 8, 'mouth_w': 14, 'nose_side': (90, 76, 4.5), 'hairline': False},
    'front': [L(blob([(4, 66), (2, 40), (16, 16), (50, 6), (84, 16), (98, 40), (96, 66), (84, 62), (50, 60), (16, 62)])),
              L(blob([(18, 26), (38, 14), (52, 12), (40, 24), (24, 36)], 6), 'light', 'b', False),
              L(blob([(70, 20), (92, 40), (94, 62), (84, 60), (82, 40)], 6), 'shade', 'b', False),
              # patillas por las mejillas y perilla
              L(blob([(12, 60), (20, 60), (24, 84), (36, 96), (28, 96), (14, 84)]), 'mid', 'f'),
              L(blob([(88, 60), (80, 60), (76, 84), (64, 96), (72, 96), (86, 84)]), 'mid', 'f'),
              L(blob([(42, 93), (58, 93), (54, 100), (46, 100)]), 'mid', 'f')],
    'side': [L(blob([(8, 86), (0, 50), (12, 18), (46, 4), (80, 12), (98, 38), (96, 62), (80, 64), (64, 66), (52, 86), (34, 96)])),
             L(blob([(22, 22), (44, 10), (62, 10), (44, 22), (28, 32)], 6), 'light', 'b', False),
             L(blob([(4, 56), (10, 82), (34, 94), (20, 66)], 6), 'shade', 'b', False),
             L(blob([(66, 66), (72, 66), (74, 86), (82, 98), (74, 98), (66, 86)]), 'mid', 'f')],
    'back': [L(blob([(4, 80), (0, 44), (14, 16), (50, 4), (86, 16), (100, 44), (96, 80), (74, 96), (26, 96)])),
             L(blob([(18, 24), (40, 12), (58, 12), (40, 24), (24, 34)], 6), 'light', 'b', False),
             L(blob([(60, 30), (94, 44), (94, 78), (70, 94), (78, 60)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Jim Wraith: melena lisa que le tapa los ojos
CHARS['jim-wraith'] = {
    'body': 'delgado', 'pal': pal('#c99598', '#fcc48d'),
    'face': {'eyes': 'none', 'mouth': 'line', 'ears': False, 'hairline': False},
    # melena lisa con raya en medio que cae recta por delante de la cara (le tapa los ojos, se le ve de la nariz
    # para abajo) y por la espalda hasta los omóplatos
    'front': [L(blob([(12, 122), (10, 50), (16, 22), (34, 10), (66, 10), (84, 22), (90, 50), (88, 122), (78, 124), (74, 90), (26, 90), (22, 124)])),
              L(blob([(80, 30), (90, 60), (88, 120), (80, 120), (82, 70)], 6), 'shade', 'b', False),
              L(blob([(50, 14), (34, 18), (22, 34), (18, 60), (20, 100), (28, 118), (34, 100), (36, 82), (44, 80), (49, 66)]), 'mid', 'f'),
              L(blob([(50, 14), (66, 18), (78, 34), (82, 60), (80, 100), (72, 118), (66, 100), (64, 82), (56, 80), (51, 66)]), 'mid', 'f'),
              L(blob([(54, 22), (70, 30), (76, 60), (72, 100), (66, 80), (60, 60)], 6), 'shade', 'f', False),
              L(blob([(30, 26), (40, 20), (34, 44), (28, 70), (26, 48)], 6), 'light', 'f', False),
              strand([(50, 14), (50, 64)], 'deep', 'f', 1.2), strand([(36, 40), (30, 100)], 'shade', 'f', 1.0),
              strand([(64, 40), (70, 100)], 'deep', 'f', 1.0)],
    'side': [L(blob([(58, 20), (32, 14), (14, 32), (8, 70), (8, 126), (32, 128), (40, 98), (44, 82), (40, 58), (54, 46), (74, 44), (86, 46), (84, 30), (70, 18)])),
             L(blob([(14, 50), (12, 100), (16, 124), (28, 124), (24, 96)], 6), 'shade', 'b', False),
             L(blob([(36, 18), (54, 18), (40, 30), (24, 44)], 6), 'light', 'b', False),
             strand([(28, 28), (16, 70), (16, 120)], 'shade', 'b', 1.2), strand([(40, 40), (30, 80), (32, 122)], 'deep', 'b', 1.0),
             L(blob([(48, 30), (70, 30), (86, 40), (90, 62), (88, 80), (80, 82), (72, 66), (60, 62), (50, 70), (46, 52)]), 'mid', 'f', ln=True),
             L(blob([(66, 40), (84, 48), (86, 76), (80, 78), (74, 58)], 6), 'shade', 'f', False)],
    'back': [L(blob([(10, 128), (8, 60), (14, 26), (36, 12), (64, 12), (86, 26), (92, 60), (90, 128), (70, 132), (50, 128), (30, 132)])),
             L(blob([(54, 20), (80, 30), (88, 80), (86, 126), (64, 128), (72, 70)], 6), 'shade', 'b', False),
             L(blob([(24, 30), (36, 18), (40, 40), (32, 90), (24, 70)], 6), 'light', 'b', False),
             strand([(50, 14), (48, 70), (50, 128)], 'deep', 'b', 1.2), strand([(30, 30), (24, 124)], 'shade', 'b', 1.0),
             strand([(70, 30), (76, 124)], 'deep', 'b', 1.0)],
}

# ------------------------------------------------------------------ Tod Ironside: casquete en punta, nuca rapada y orejas grandes
CHARS['tod-ironside'] = {
    'body': 'bajito', 'pal': pal('#934814', '#ffbe8d', stub='#a9805a', plaster='#c8a070'),
    # cara de mono enfadado: ojos redondos pequeños, cejas en V, tirita en la nariz, dientes de conejo y orejas grandes
    'face': {'eyes': 'round', 'eye_y': 74, 'eye_sep': 13, 'brows': 'angry', 'mouth': 'buck', 'mouth_y': 90, 'big_ears': 2,
             'ear_out': 5, 'ears_front': True, 'hairline': [(6, 88), (21, 88), (22, 66), (25, 54), (32, 50), (40, 54), (46, 62), (50, 68), (54, 62), (60, 54), (68, 50), (75, 54), (78, 66), (79, 88), (94, 88)]},
    # pelo en forma de bellota que acaba en punta y enmarca la cara hasta la mandíbula, con pico en la frente
    'front': [L(blob([(14, 84), (10, 54), (18, 26), (36, 10), (50, -2), (64, 10), (82, 26), (90, 54), (86, 84), (78, 80), (22, 80)])),
              L(blob([(26, 22), (42, 8), (50, 2), (40, 26), (28, 40)], 6), 'light', 'b', False),
              L(blob([(62, 14), (84, 34), (86, 70), (72, 56)], 6), 'shade', 'b', False),
              L(blob([(42, 79), (58, 79), (58, 84), (42, 84)], 2), 'plaster', 'f', ln=True)],
    'side': [L(blob([(42, 96), (22, 90), (16, 72), (30, 74), (44, 84)]), 'stub'),
             L(blob([(26, 76), (16, 56), (20, 30), (44, 2), (66, 14), (82, 30), (88, 50), (74, 52), (62, 54), (58, 74), (50, 76), (40, 70)])),
             L(blob([(36, 14), (50, 8), (48, 20), (32, 34)], 6), 'light', 'b', False),
             L(blob([(18, 52), (24, 70), (36, 72), (28, 58)], 6), 'shade', 'b', False),
             L(blob([(54, 52), (62, 52), (60, 80), (54, 82)]), 'mid', 'f'),
             L(blob([(84, 78), (92, 78), (92, 83), (84, 83)], 2), 'plaster', 'f', ln=True)],
    'back': [L(blob([(14, 70), (86, 70), (78, 92), (50, 98), (22, 92)]), 'stub'),
             L(blob([(12, 72), (10, 44), (24, 20), (50, -2), (76, 20), (90, 44), (88, 72), (50, 74)])),
             L(blob([(56, 12), (84, 38), (86, 68), (64, 72)], 6), 'shade', 'b', False),
             L(blob([(30, 24), (44, 8), (40, 28)], 4), 'light', 'b', False)],
}

# ------------------------------------------------------------------ Steve Grim: pelo corto despeinado con un pelo de punta
# Steve Grim: pelo castaño despeinado y con volumen; dos pelillos de punta arriba, mechones en punta por los lados hasta
# la mandíbula y flequillo en puntas hasta los ojos, con un mechón más largo entre ellos
STEVE_MASS = blob([(14, 70), (11, 46), (20, 28), (36, 18), (54, 16), (72, 20), (85, 32), (89, 50), (86, 70), (76, 60), (24, 60)])
CHARS['steve-grim'] = {
    'body': 'normal', 'pal': pal('#4a3316', '#fac286'),
    'face': {'eyes': 'normal', 'mouth': 'smile', 'hairline': (66, 52)},
    'front': [L(fat((44, 20), (50, 18), (40, 4), 2)), L(fat((52, 18), (58, 20), (62, 6), 2)), L(STEVE_MASS),
              # puntas de los lados, por delante de las orejas, hasta la mandíbula
              spk((10, 52), (22, 56), (12, 90), 3), spk((18, 58), (26, 62), (22, 86), 2),
              spk((78, 56), (90, 52), (88, 90), 3, light_left=False), spk((74, 62), (82, 58), (78, 86), 2, light_left=False),
              # flequillo en puntas
              spk((20, 52), (36, 48), (26, 70), 3, z='f'), spk((32, 48), (48, 46), (40, 72), 3, z='f'),
              spk((44, 46), (56, 46), (50, 80), 2, z='f'), spk((52, 46), (68, 48), (60, 72), 3, z='f', light_left=False),
              spk((64, 48), (80, 52), (74, 70), 3, z='f', light_left=False),
              L(blob([(56, 14), (84, 30), (88, 52), (76, 56)], 6), 'shade', 'b', False),
              sheen(24, 50, 26, 3), strand([(30, 42), (46, 36), (66, 38)], 'shade', 'b', 1.1)],
    'side': [L(fat((40, 16), (46, 14), (34, -2), 2)), L(fat((48, 14), (54, 14), (56, -2), 2)),
             L(blob([(46, 90), (24, 86), (12, 66), (12, 40), (26, 18), (50, 10), (74, 16), (88, 34), (88, 50), (74, 50), (62, 54), (54, 66), (54, 80)])),
             # puntas de la nuca y de detrás de la oreja
             spk((12, 70), (24, 78), (6, 96), 3), spk((22, 80), (34, 86), (22, 102), 3), spk((34, 86), (46, 90), (38, 104), 3),
             # flequillo hacia delante y mechón por delante de la oreja
             spk((58, 30), (88, 40), (90, 66), 5, z='f', light_left=False), spk((70, 40), (86, 48), (82, 74), 3, z='f', light_left=False),
             spk((52, 54), (62, 54), (56, 84), 2, z='f'),
             L(blob([(16, 50), (18, 74), (40, 86), (30, 62)], 6), 'shade', 'b', False),
             sheen(24, 50, 26, 3), strand([(20, 52), (34, 38), (52, 32)], 'shade', 'b', 1.1)],
    'back': [L(fat((44, 16), (50, 14), (40, -2), 2)), L(fat((52, 14), (58, 16), (62, 0), 2)),
             L(blob([(14, 70), (10, 44), (20, 22), (40, 12), (60, 12), (80, 22), (90, 44), (86, 70), (72, 86), (50, 90), (28, 86)])),
             spk((14, 70), (28, 80), (12, 98), 3), spk((26, 82), (40, 86), (30, 104), 3), spk((40, 86), (54, 86), (46, 106), 3),
             spk((54, 86), (68, 84), (64, 104), 3, light_left=False), spk((68, 80), (86, 70), (86, 98), 3, light_left=False),
             L(blob([(58, 16), (86, 40), (86, 70), (66, 84)], 6), 'shade', 'b', False),
             sheen(24, 50, 26, 3), strand([(30, 52), (50, 46), (70, 52)], 'shade', 'b', 1.1)],
}

# ------------------------------------------------------------------ Tim Saunders: calvo, un mechón en la frente y coleta enorme
# Tim Saunders: cabeza calva y alta en forma de huevo, un mechón rizado en la frente, ojos cerrados y una coleta enorme
# atada en la coronilla que le cae por la espalda hasta la cintura
TIM_SKULL = blob([(19, 66), (14, 38), (24, 14), (50, 4), (76, 14), (86, 38), (81, 66)])
TIM_LOCK = blob([(50, 16), (57, 28), (56, 42), (50, 52), (44, 50), (48, 42), (45, 30)])
CHARS['tim-saunders'] = {
    'body': 'bajito', 'pal': pal('#814407', '#fcbc7a', tie='#c03a2a'),
    'face': {'eyes': 'closed', 'mouth': 'smile', 'hairline': False},
    'front': [L(blob([(56, 6), (66, -4), (80, 6), (96, 40), (108, 84), (106, 120), (94, 110), (86, 76), (76, 40), (60, 14)])),
              L(blob([(94, 50), (104, 88), (102, 112), (94, 96), (88, 66)], 6), 'shade', 'b', False),
              L(TIM_SKULL, 'skin'), L(blob([(28, 18), (40, 12), (34, 24)], 4), (255, 226, 190, 255), 'b', False),
              L(TIM_LOCK, 'mid', 'f', ln=True), L(blob([(52, 22), (56, 32), (52, 46), (50, 34)], 4), 'shade', 'f', False),
              L(ell(54, 6, 6, 4), 'tie', 'b')],
    'side': [L(blob([(32, 8), (40, -4), (28, -10), (8, -2), (-10, 30), (-16, 84), (-6, 116), (4, 88), (6, 50), (16, 20)])),
             L(blob([(-6, 40), (-10, 88), (-4, 106), (0, 80)], 6), 'shade', 'b', False),
             L(ell(32, 6, 5, 6), 'tie'),
             L(blob([(44, 92), (22, 90), (14, 66), (14, 36), (28, 14), (54, 6), (78, 16), (88, 40), (88, 62), (64, 56)]), 'skin'),
             L(blob([(66, 18), (74, 26), (76, 40), (70, 48), (66, 40), (68, 30)]), 'mid', 'f', ln=True)],
    'back': [L(BACK_SKULL, 'skin'),
             L(blob([(40, 10), (60, 10), (72, 50), (70, 104), (50, 132), (30, 104), (28, 50)]), 'mid', 'f', ln=True),
             L(blob([(54, 18), (68, 50), (66, 100), (50, 124), (58, 70)], 6), 'shade', 'f', False),
             strand([(44, 30), (40, 70), (44, 116)], 'shade', 'f', 1.1),
             L(ell(50, 12, 7, 5), 'tie', 'f')],
}

# ------------------------------------------------------------------ Sam Kincaid: rizos naranjas que le tapan los ojos
def clumps(pts, r, c='shade', z='b'):
    """Rizos: bolas de pelo con su sombra (pts: centros)."""
    return [L(bumpy(x, y, r, r * 0.8, 7, 0.08), c, z, False) for x, y in pts]


CHARS['sam-kincaid'] = {
    'body': 'normal', 'pal': pal('#d4671a', '#ffcda3', nose='#e8806a', freckle='#d89070'),
    # melena afro de rizos, más ancha que alta, que le tapa los ojos; se le ve la nariz redonda, las pecas y la sonrisa
    'face': {'eyes': 'none', 'mouth': 'smile', 'mouth_y': 90, 'ears': False, 'hairline': (72, 58), 'nose': (50, 79, 3.6)},
    'front': [L(bumpy(50, 44, 54, 40, 18, 0.06))] + clumps([(12, 56), (88, 56), (20, 72), (80, 72)], 12) + [
              L(ell(30, 20, 10, 4), 'light', 'b', False), L(ell(64, 16, 8, 3), 'light', 'b', False),
              strand([(26, 36), (38, 30), (50, 34)], 'shade', 'b', 1.2), strand([(56, 28), (68, 24), (78, 30)], 'shade', 'b', 1.2),
              L(bumpy(50, 60, 38, 15, 12, 0.08), 'mid', 'f'), L(bumpy(64, 66, 16, 8, 6), 'shade', 'f', False),
              L(ell(34, 58, 8, 3), 'light', 'f', False),
              L(ell(38, 82, 1.2, 1.2), 'freckle', 'f', False), L(ell(42, 84, 1.2, 1.2), 'freckle', 'f', False),
              L(ell(58, 84, 1.2, 1.2), 'freckle', 'f', False), L(ell(62, 82, 1.2, 1.2), 'freckle', 'f', False)],
    'side': [L(bumpy(44, 44, 48, 40, 16, 0.06))] + clumps([(10, 58), (22, 74), (40, 80)], 12) + [
             L(ell(44, 18, 9, 4), 'light', 'b', False), strand([(28, 34), (42, 28), (56, 32)], 'shade', 'b', 1.2),
             L(bumpy(70, 56, 20, 18, 8), 'mid', 'f'), L(ell(68, 48, 6, 3), 'light', 'f', False)],
    'back': [L(bumpy(50, 50, 54, 46, 18, 0.06))] + clumps([(14, 62), (86, 62), (28, 82), (50, 88), (72, 82)], 13) + [
             L(ell(32, 22, 10, 4), 'light', 'b', False), L(ell(66, 20, 8, 3), 'light', 'b', False),
             strand([(26, 42), (40, 36), (54, 42)], 'shade', 'b', 1.2), strand([(50, 54), (64, 48), (78, 54)], 'shade', 'b', 1.2)],
}

# ------------------------------------------------------------------ Jude Sharp: rastas recogidas, gafas y capa
OUTC = (60, 24, 16, 255)


def caps(p0, p1, r, n=10):
    """Cápsula (rasta): segmento con los extremos redondos."""
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    Ln = math.hypot(dx, dy) or 1
    a0 = math.atan2(dx / Ln, -dy / Ln)
    pts = [(p0[0] + r * math.cos(a0 + math.pi * k / n), p0[1] + r * math.sin(a0 + math.pi * k / n)) for k in range(n + 1)]
    pts += [(p1[0] + r * math.cos(a0 + math.pi + math.pi * k / n), p1[1] + r * math.sin(a0 + math.pi + math.pi * k / n)) for k in range(n + 1)]
    return pts


def dread(p0, p1, r, z='b', sil=True):
    """Rasta: cápsula con tono medio, lado en sombra y rayas de trenzado."""
    out = [L(caps(p0, p1, r), 'mid', z, sil, False)]
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    Ln = math.hypot(dx, dy) or 1
    nx, ny = -dy / Ln, dx / Ln
    out.append(L(caps((p0[0] + nx * r * 0.45, p0[1] + ny * r * 0.45), (p1[0] + nx * r * 0.45, p1[1] + ny * r * 0.45), r * 0.5), 'shade', z, False))
    # borde oscuro en el extremo de abajo (separa cada rasta de la que tiene debajo)
    ang = math.atan2(dy, dx)
    arc = [(p0[0] + r * math.cos(ang + math.pi / 2 + math.pi * k / 8), p0[1] + r * math.sin(ang + math.pi / 2 + math.pi * k / 8)) for k in range(9)]
    out.append(L(arc, OUTC, z, False, False, 1.3))
    steps = max(2, int(Ln / 7))
    for i in range(1, steps):
        t = i / steps
        cx, cy = p0[0] + dx * t, p0[1] + dy * t
        out.append(strand([(cx - nx * r * 0.8, cy - ny * r * 0.8 + 1.5), (cx, cy - 1), (cx + nx * r * 0.8, cy + ny * r * 0.8 + 1.5)], 'deep', z, 0.9))
    return out


# Jude Sharp: rastas gruesas que salen de la frente hacia arriba y hacia atrás (de perfil se ve el mazo recogido detrás),
# rastas cortas a los lados hasta las orejas, gafas de natación con cristales verdes y capa roja
def dread_rows(rows, r=6.2, z='b'):
    """Rastas en filas (de arriba abajo; las de abajo tapan a las de arriba): cada fila (y, [x...], largo)."""
    out = []
    for y, xs, ln in rows:
        for x in xs:
            tilt = (x - 50) * 0.18
            out += dread((x, y), (x + tilt, y - ln), r, z, sil=True)
    return out


JUDE_ROWS = [(16, [36, 50, 64], 14), (29, [26, 40, 54, 68], 14), (43, [20, 34, 48, 62, 76], 14), (58, [18, 32, 46, 60, 74, 84], 13)]
CHARS['jude-sharp'] = {
    'body': 'normal', 'cape': '#c8201c', 'pal': pal('#94793d', '#f0c393', strap='#2a3a52', lens='#4a8a3a', lens_l='#a8e0a0', rim='#3a5a7a'),
    'face': {'eyes': 'none', 'mouth': 'smile', 'hairline': (68, 66)},
    'front': [L(blob([(14, 66), (12, 40), (22, 14), (40, 0), (60, 0), (78, 14), (88, 40), (86, 66)])),
              L(blob([(58, 4), (80, 22), (86, 56), (70, 50)], 6), 'shade', 'b', False)]
             + dread_rows(JUDE_ROWS)
             + dread((14, 60), (12, 82), 6) + dread((86, 60), (88, 82), 6)
             + [L(blob([(18, 70), (82, 70), (82, 78), (18, 78)], 3), 'strap', 'f'),
                L(ell(36, 75, 11, 9), 'rim', 'f'), L(ell(64, 75, 11, 9), 'rim', 'f'),
                L(ell(36, 75, 7.5, 6), 'lens', 'f', False), L(ell(64, 75, 7.5, 6), 'lens', 'f', False),
                L(ell(33, 72, 2.6, 1.8), 'lens_l', 'f', False), L(ell(61, 72, 2.6, 1.8), 'lens_l', 'f', False)],
    'side': [L(bumpy(10, 36, 22, 26, 9, 0.09))] + [x for p0, p1 in (((26, 30), (-4, 18)), ((24, 44), (-8, 44)), ((28, 56), (0, 66)))
                                                   for x in dread(p0, p1, 7)]
            + [L(blob([(44, 92), (24, 88), (16, 66), (18, 40), (32, 22), (56, 16), (78, 24), (88, 42), (74, 48), (58, 52), (52, 66), (50, 82)]))]
            + [x for p0, p1 in (((60, 46), (30, 22)), ((74, 46), (52, 18)), ((52, 58), (24, 44)))
               for x in dread(p0, p1, 6.5)]
            + dread((48, 62), (46, 84), 5.5)
            + [L(blob([(44, 70), (88, 70), (88, 78), (44, 78)], 3), 'strap', 'f'),
               L(ell(84, 75, 7, 8.5), 'rim', 'f'), L(ell(85, 75, 4.5, 6), 'lens', 'f', False)],
    'back': [L(blob([(10, 70), (8, 40), (20, 14), (40, 0), (60, 0), (80, 14), (92, 40), (90, 70), (70, 84), (30, 84)]))]
            + dread_rows([(10, [38, 52, 66], 12), (24, [26, 40, 54, 68, 80], 12), (40, [16, 30, 44, 58, 72, 86], 13),
                          (58, [14, 28, 42, 56, 70, 86], 13), (78, [26, 40, 54, 68], 13)], 6.6)
            + [L(blob([(10, 70), (90, 70), (90, 77), (10, 77)], 3), 'strap', 'f')],
}

# ------------------------------------------------------------------ Maxwell Carson: gorro de rayas con punta y trenzas
# Maxwell Carson: gorro de lana rosa con dos franjas verdes, la parte de arriba plana con dos picos en las esquinas y
# orejeras con cordones trenzados y borlas; flequillo naranja que asoma bajo el gorro y mechones largos por detrás
MAX_HAT = blob([(10, 64), (8, 30), (10, 6), (16, -4), (26, 4), (50, 2), (74, 4), (84, -4), (90, 6), (92, 30), (90, 64), (50, 62)])
MAX_FLAP_L = blob([(10, 54), (26, 56), (24, 84), (18, 96), (12, 88)])
MAX_FLAP_R = mirror(MAX_FLAP_L)


def stripe_band(y0, y1, x0=8.6, x1=91.4):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


def cord(x, y0, y1):
    """Cordón trenzado con borlas: rombos alternos rosa y verde."""
    out = [strand([(x, y0), (x, y1)], 'stripe', 'f', 1.0)]
    for i, y in enumerate(range(int(y0) + 3, int(y1), 5)):
        out.append(L(ell(x, y, 2.2, 2.6), 'hat' if i % 2 else 'stripe', 'f', False))
    out.append(L(ell(x, y1 + 2, 3, 3), 'bead', 'f', False))
    return out


CHARS['maxwell-carson'] = {
    'body': 'normal', 'pal': pal('#c4561e', '#f2b48c', iris='#3a2a2a', hat='#e08478', hat_d='#b8645a', stripe='#7c9a96', bead='#e05a6a'),
    'face': {'eyes': 'big', 'eye_y': 74, 'mouth': 'smile', 'hairline': False, 'ears': False},
    'front': [spk((24, 60), (40, 58), (30, 74), 2), spk((60, 58), (76, 60), (70, 74), 2, light_left=False),
              spk((40, 58), (54, 58), (46, 70), 2, z='f'),
              L(MAX_HAT, 'hat', 'f'), L(blob([(64, 6), (86, 2), (92, 30), (90, 62), (74, 60)], 6), 'hat_d', 'f', False),
              L(stripe_band(18, 28), 'stripe', 'f', False), L(stripe_band(40, 50), 'stripe', 'f', False),
              L(MAX_FLAP_L, 'hat', 'f'), L(MAX_FLAP_R, 'hat', 'f')]
             + cord(17, 96, 116) + cord(83, 96, 116),
    'side': [L(blob([(14, 58), (40, 60), (42, 76), (28, 96), (10, 104), (6, 84)])),
             spk((10, 64), (30, 66), (0, 108), 6), spk((22, 70), (40, 72), (20, 110), 5), spk((52, 60), (62, 60), (58, 78), 2, z='f'),
             L(blob([(10, 66), (8, 34), (16, 12), (30, -2), (48, 4), (70, 6), (86, 22), (92, 46), (90, 64), (50, 62)]), 'hat', 'f'),
             L(blob([(10, 64), (8, 34), (16, 12), (30, 0), (28, 30), (24, 62)], 6), 'hat_d', 'f', False),
             L([(10, 20), (88, 22), (90, 32), (9, 30)], 'stripe', 'f', False), L([(9, 42), (90, 44), (90, 54), (10, 52)], 'stripe', 'f', False),
             L(blob([(40, 56), (56, 58), (54, 86), (48, 96), (42, 86)]), 'hat', 'f')] + cord(48, 96, 116),
    'back': [L(blob([(20, 60), (80, 60), (78, 84), (66, 104), (50, 110), (34, 104), (22, 84)])),
             spk((22, 70), (40, 72), (28, 108), 6), spk((38, 74), (60, 74), (48, 116), 6), spk((58, 72), (78, 70), (70, 106), 6, light_left=False),
             strand([(40, 66), (38, 96)], 'shade', 'b', 1.0), strand([(60, 66), (62, 96)], 'shade', 'b', 1.0),
             L(MAX_HAT, 'hat', 'f'), L(blob([(56, 6), (84, -2), (92, 30), (90, 62), (70, 60)], 6), 'hat_d', 'f', False),
             L(stripe_band(18, 28), 'stripe', 'f', False), L(stripe_band(40, 50), 'stripe', 'f', False),
             L(MAX_FLAP_L, 'hat', 'f'), L(MAX_FLAP_R, 'hat', 'f')] + cord(17, 96, 116) + cord(83, 96, 116),
}

# ------------------------------------------------------------------ Kevin Dragonfly: rapado rosa y cara de enfado
CHARS['kevin-dragonfly'] = {
    'body': 'normal', 'pal': pal('#c66c66', '#cf9667'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown',
             'hairline': [(8, 68), (17, 68), (20, 54), (24, 42), (32, 40), (40, 46), (50, 52), (60, 46), (68, 40), (76, 42), (80, 54), (83, 68), (92, 68)]},
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
    'face': {'eyes': 'sharp', 'mouth': 'smile', 'glasses': (40, 70, 50, 255), 'glasses_rect': True},
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
# Bobby Shearer: pelo gris verdoso corto y despeinado, de punta hacia arriba con mechones desiguales que se abren a los
# lados; cara alargada, ojos redondos pequeños
BOBBY_TOP = [spk((14, 46), (36, 26), (14, 8), 8), spk((30, 28), (54, 20), (38, -4), 8), spk((48, 20), (70, 24), (64, -2), 7, light_left=False),
             spk((64, 26), (86, 44), (88, 12), 8, light_left=False), spk((40, 22), (58, 22), (52, 4), 4)]
CHARS['bobby-shearer'] = {
    'body': 'delgado', 'pal': pal('#8eaa9a', '#c99860'),
    'face': {'eyes': 'round', 'eye_y': 74, 'eye_sep': 14, 'mouth': 'line', 'mouth_y': 92,
             'hairline': [(8, 66), (16, 64), (20, 52), (30, 48), (42, 50), (50, 46), (58, 50), (70, 48), (80, 52), (84, 64), (92, 66)]},
    'front': BOBBY_TOP + [L(blob([(16, 62), (14, 40), (26, 26), (50, 20), (74, 26), (86, 40), (84, 62), (50, 56)])),
                          L(blob([(62, 26), (84, 40), (84, 60), (70, 54)], 6), 'shade', 'b', False),
                          spk((36, 44), (50, 42), (42, 56), 2, z='f'), spk((54, 42), (66, 44), (62, 56), 2, z='f', light_left=False)],
    'side': [spk((16, 50), (28, 34), (2, 30), 5), spk((24, 36), (40, 24), (12, 8), 5), spk((38, 26), (54, 20), (34, 0), 5),
             spk((52, 20), (66, 22), (58, 0), 4, light_left=False), spk((64, 24), (78, 32), (78, 10), 4, light_left=False),
             L(blob([(42, 92), (22, 86), (14, 64), (16, 40), (30, 24), (56, 20), (78, 28), (84, 42), (70, 46), (58, 50), (52, 64), (50, 80)])),
             L(blob([(18, 56), (22, 78), (38, 86), (28, 66)], 6), 'shade', 'b', False),
             spk((68, 34), (86, 42), (90, 58), 3, z='f', light_left=False)],
    'back': BOBBY_TOP + [
             L(blob([(16, 70), (14, 40), (26, 26), (50, 20), (74, 26), (86, 40), (84, 70), (66, 86), (34, 86)])),
             L(blob([(58, 26), (84, 42), (84, 68), (66, 84)], 6), 'shade', 'b', False),
             strand([(30, 40), (40, 60), (42, 80)], 'shade', 'b', 1.0), strand([(56, 36), (60, 60), (58, 82)], 'deep', 'b', 1.0)],
}

# ------------------------------------------------------------------ Erik Eagle: flequillo en ola y puntas hacia fuera
CHARS['erik-eagle'] = {
    'body': 'normal', 'pal': pal('#5a3a26', '#fcbb7a'),
    'face': {'eyes': 'big', 'mouth': 'smile', 'hairline': (62, 52)},
    # pelo con mucho volumen y raya a un lado: el flequillo barre de derecha a izquierda en mechones grandes y las puntas
    # de los lados se abren hacia fuera a la altura de las orejas; por detrás, puntas abiertas en la nuca
    'front': [L(blob([(12, 70), (8, 42), (18, 18), (44, 6), (70, 8), (88, 24), (94, 46), (90, 70), (80, 62), (20, 62)])),
              spk((10, 52), (22, 66), (-2, 74), 6), spk((78, 66), (90, 52), (102, 74), 6, light_left=False),
              L(blob([(60, 12), (86, 26), (92, 50), (80, 58)], 6), 'shade', 'b', False),
              sheen(22, 50, 22, 3),
              # raya a la derecha y flequillo barrido hacia la izquierda
              L(blob([(60, 18), (80, 32), (70, 44), (50, 52), (32, 62), (14, 70), (16, 56), (30, 36)]), 'mid', 'f', ln=True),
              spk((56, 36), (74, 42), (34, 68), 5, z='f'),
              spk((70, 36), (86, 46), (62, 66), 4, z='f', light_left=False),
              spk((80, 44), (90, 54), (84, 70), 3, z='f', light_left=False),
              strand([(66, 26), (44, 44), (26, 60)], 'shade', 'f', 1.1)],
    'side': [L(blob([(42, 94), (22, 90), (10, 70), (10, 44), (22, 20), (50, 8), (76, 14), (90, 32), (86, 46), (70, 48), (58, 52), (52, 66), (50, 84)])),
             spk((14, 48), (26, 30), (-10, 26), 6), spk((22, 32), (40, 18), (8, 4), 6), spk((10, 66), (18, 52), (-8, 58), 5),
             spk((14, 82), (28, 90), (2, 98), 4),
             L(blob([(16, 56), (18, 80), (38, 90), (28, 66)], 6), 'shade', 'b', False), sheen(34, 64, 14, 3),
             spk((50, 22), (80, 30), (92, 64), 6, z='f', light_left=False), spk((50, 52), (60, 52), (56, 78), 2, z='f')],
    'back': [L(blob([(12, 66), (8, 40), (20, 16), (50, 8), (80, 16), (92, 40), (88, 66), (78, 86), (50, 94), (22, 86)])),
             spk((12, 50), (22, 62), (-6, 74), 4), spk((78, 62), (88, 50), (106, 72), 4, light_left=False),
             spk((14, 78), (30, 88), (4, 98), 4), spk((30, 88), (46, 92), (30, 106), 4), spk((46, 92), (60, 92), (54, 108), 4),
             spk((58, 90), (74, 86), (74, 104), 4, light_left=False), spk((70, 86), (86, 76), (96, 96), 4, light_left=False),
             L(blob([(58, 16), (88, 40), (86, 68), (70, 86)], 6), 'shade', 'b', False), sheen(26, 54, 22, 3)],
}


# ------------------------------------------------------------------ Axel Blaze: los pinchos que diste por buenos (head_axel.py
# y el perfil de body.py), ahora sobre la base común para que la cara tenga las mismas proporciones que el resto
def _axel():
    import head_axel as A
    from heads import lerp
    hair = '#f6d8b0'
    front = [L(A.CAP)]
    for bl, br, tp, bd, ll in A.SPIKES:
        front += [L(A.spike(bl, br, tp, bd), 'mid'),
                  L(A.spike(lerp(bl, br, 0.55), br, tp, bd) if ll else A.spike(bl, lerp(bl, br, 0.45), tp, bd), 'shade', 'b', False)]
        a_, b_ = (lerp(bl, br, 0.14), lerp(bl, br, 0.36)) if ll else (lerp(bl, br, 0.64), lerp(bl, br, 0.86))
        front.append(L(A.spike(lerp(a_, tp, 0.14), lerp(b_, tp, 0.14), lerp(lerp(a_, b_, 0.5), tp, 0.6), (bd[0] * 0.6, bd[1] * 0.6)), 'light', 'b', False))
    for bl, br, tp, bd in A.BANGS:
        ll = tp[0] < 50
        front += [L(A.spike(bl, br, tp, bd), 'mid', 'f'),
                  L(A.spike(lerp(bl, br, 0.55), br, tp, bd) if ll else A.spike(bl, lerp(bl, br, 0.45), tp, bd), 'shade', 'f', False)]
    side_sp = [((24, 84), (10, 46), (-8, 50)), ((14, 62), (34, 34), (2, 6)), ((26, 40), (52, 28), (24, -10)),
               ((46, 30), (70, 34), (54, -12)), ((62, 36), (80, 48), (82, 4))]
    side = [L(blob([(44, 90), (24, 92), (16, 70), (12, 26), (52, 24), (84, 26), (84, 62), (64, 56)]), 'shade')]
    for a_, b_, tp in side_sp:
        side += [L(fat(a_, b_, tp, 7), 'mid'), L(fat(a_, lerp(a_, b_, 0.5), tp, 4), 'shade', 'b', False),
                 L(fat(lerp(lerp(a_, b_, 0.62), tp, 0.12), lerp(lerp(a_, b_, 0.88), tp, 0.12), lerp(lerp(a_, b_, 0.75), tp, 0.62), 2.5), 'light', 'b', False)]
    for lo, hi, tp in (((40, 62), (58, 46), (22, 18)), ((56, 50), (70, 36), (44, 4))):
        side += [L(fat(lo, hi, tp, 6), 'mid', 'b', False, True), L(fat(lo, lerp(lo, hi, 0.45), tp, 3), 'shade', 'b', False),
                 L(fat(lerp(lo, hi, 0.68), hi, lerp(lerp(lo, hi, 0.85), tp, 0.62), 2), 'light', 'b', False)]
    side += [spk((60, 42), (78, 44), (84, 62), 3, z='f', light_left=False), spk((52, 54), (62, 54), (56, 76), 1.5, z='f')]
    back = [L(A.CAP, 'shade'), L(blob([(16, 56), (84, 56), (80, 80), (64, 94), (36, 94), (20, 80)])),
            L(blob([(54, 58), (82, 60), (76, 84), (60, 92)], 6), 'shade', 'b', False)]
    for bl, br, tp, bd, ll in A.SPIKES:
        back += [L(A.spike(bl, br, tp, bd), 'mid'),
                 L(A.spike(lerp(bl, br, 0.55), br, tp, bd) if ll else A.spike(bl, lerp(bl, br, 0.45), tp, bd), 'shade', 'b', False)]
    back += [strand([(36, 66), (34, 90)], 'shade', 'b', 1.0), strand([(50, 64), (50, 92)], 'shade', 'b', 1.0), strand([(64, 66), (66, 90)], 'shade', 'b', 1.0)]
    return {
        'body': 'normal', 'pal': dict(pal(hair, '#eeb07c', iris='#302232'), mid=(246, 216, 176, 255), shade=(214, 160, 128, 255),
                                      deep=(160, 110, 82, 255), light=(255, 246, 226, 255)),
        'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'hairline': (66, 58)},
        'front': front, 'side': side, 'back': back,
    }


CHARS['axel-blaze'] = _axel()


# equipos en sus propios archivos (registran sus personajes en CHARS)
import chars_teikoku  # noqa: E402,F401
import chars_occult  # noqa: E402,F401
import chars_wild  # noqa: E402,F401
import chars_otaku  # noqa: E402,F401
import chars_sallys  # noqa: E402,F401
import chars_sengoku  # noqa: E402,F401
import chars_kirkwood  # noqa: E402,F401
import chars_brain  # noqa: E402,F401
import chars_zeus  # noqa: E402,F401
import chars_farm  # noqa: E402,F401
import chars_umbrella  # noqa: E402,F401
import chars_kfc  # noqa: E402,F401
import chars_ob  # noqa: E402,F401
import chars_raimon2  # noqa: E402,F401
import chars_ie2misc  # noqa: E402,F401
import chars_gemini  # noqa: E402,F401
import chars_young  # noqa: E402,F401
import chars_epsilon  # noqa: E402,F401
import chars_alius  # noqa: E402,F401
import chars_alpino  # noqa: E402,F401
import chars_jukai  # noqa: E402,F401
import chars_manyuuji  # noqa: E402,F401
import chars_robots  # noqa: E402,F401
