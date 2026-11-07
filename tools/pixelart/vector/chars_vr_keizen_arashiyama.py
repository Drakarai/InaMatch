"""Secundaria Stormridge (vr-keizen-arashiyama, Keizen Arashiyama): sus modelos 3D de Inazuma Eleven: Victory Road
(英雄たちのヴィクトリーロード) como referencia (busto de frente, perfil y espalda). Cada uno tiene un solo modelo; ningún id
coge por prefijo el dibujo de otro personaje. Aquí están también las ayudas que usan los otros equipos de VR de este lote
(Meiran, Nagumohara y sus Vendedores)."""
import math

from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import quad  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)


def fr(pts, c='mid'):
    """Mechones de delante de la cara (encima de los ojos)."""
    return L(outline(pts), c, 'f')


def cloud(cx, cy, rx, ry, n=8, a0=0.0, k=0.82):
    """Contorno de nube de rizos (bultos redondos alrededor de un centro)."""
    pts = []
    for i in range(n * 2):
        a = a0 + math.pi * 2 * i / (n * 2)
        f = 1.0 if i % 2 == 0 else k
        pts.append((cx + rx * f * math.cos(a), cy + ry * f * math.sin(a)))
    return blob(pts, 6)


def lashes(ey=75, sep=14, dx=7, n=1):
    """Pestañas: una o dos rayitas en el rabillo de fuera de cada ojo."""
    out = []
    for cx, s in ((50 - sep, -1), (50 + sep, 1)):
        x = cx + s * dx
        out.append(L([(x, ey - 3), (x + s * 4, ey - 6)], OUTC, 'f', False, False, 1.4))
        if n > 1:
            out.append(L([(x - s * 1, ey - 5), (x + s * 2, ey - 9)], OUTC, 'f', False, False, 1.2))
    return out


def lash_side(ey=75, x=84):
    return [L([(x - 2, ey - 3), (x - 6, ey - 7)], OUTC, 'f', False, False, 1.4)]


# Kiona Blackwell (Niikuro Konami, portera): pelo azul marino recogido en una coleta alta en lo alto de la cabeza (dos
# lazadas de pelo arriba y una goma gris) que cae larga por detrás y se aclara a lila en las puntas; dos mechones largos a
# los lados de la cara y uno fino que le cae por el medio de la frente hasta la nariz; ojos ámbar afilados con pestañas
CHARS['kiona-blackwell'] = {
    'body': 'chica', 'pal': pal('#2e3a60', '#fcd8b8', iris='#b8862a', shade='#222b48', deep='#161c30', tip='#7c7ad8', band='#b8b8c0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 94,
             'hairline': [(12, 74), (16, 60), (28, 50), (42, 46), (50, 46), (58, 46), (72, 50), (84, 60), (88, 74)]},
    'front': [L(outline([(16, 64), (8, 96), (2, 116, 1), (14, 110), (20, 92)]), 'mid', 'b'),
              L(outline([(84, 64), (92, 96), (98, 116, 1), (86, 110), (80, 92)]), 'mid', 'b'),
              L(outline([(6, 104), (2, 116, 1), (12, 112)]), 'tip', 'b', False), L(outline([(94, 104), (98, 116, 1), (88, 112)]), 'tip', 'b', False),
              L(outline([(14, 80), (10, 44), (20, 22), (38, 12), (62, 12), (80, 22), (90, 44), (86, 80), (80, 62), (20, 62)])),
              L(outline([(58, 14), (80, 24), (90, 46), (86, 72), (76, 44)]), 'shade', 'b', False),
              L(outline([(48, 14), (32, 0), (30, -12), (40, -14), (52, 4)])), L(outline([(50, 12), (56, -16), (66, -20), (70, -10), (62, 12)])),
              L(outline([(60, -14), (66, -18), (68, -10), (62, 6)]), 'shade', 'b', False),
              L(ell(50, 13, 9, 3.2), 'band', 'b', ln=True),
              strand([(48, 46), (42, 58), (48, 70), (44, 84)], 'deep', 'f', 1.2)],
    'side': [L(outline([(36, 10), (20, 20), (6, 40), (-2, 70), (-6, 100), (0, 120, 1), (10, 100), (18, 72), (30, 40), (44, 20)])),
             L(outline([(4, 84), (-6, 100), (0, 120, 1), (8, 104), (12, 88)]), 'tip', 'b', False),
             L(outline([(54, 62), (58, 50), (78, 44), (90, 32), (86, 14), (66, 4), (40, 4), (20, 14), (8, 34), (8, 58), (16, 78), (30, 84), (42, 78), (48, 70)])),
             L(outline([(10, 38), (30, 42), (34, 76), (16, 74)]), 'shade', 'b', False),
             L(outline([(40, 8), (30, -10), (38, -18), (50, 0)])), L(outline([(46, 6), (52, -18), (62, -16), (58, 6)])),
             L(ell(44, 8, 3.4, 7), 'band', 'b', ln=True),
             L(outline([(60, 50), (66, 70), (66, 94, 1), (60, 74)]), 'mid', 'f')] + lash_side(),
    'back': [L(outline([(14, 86), (10, 44), (20, 20), (38, 10), (62, 10), (80, 20), (90, 44), (86, 86), (68, 96), (32, 96)])),
             L(outline([(58, 12), (80, 22), (90, 46), (86, 84), (66, 92)]), 'shade', 'b', False),
             L(outline([(40, 14), (30, 40), (32, 80), (36, 110), (50, 124, 1), (64, 110), (68, 80), (70, 40), (60, 14)])),
             L(outline([(34, 96), (36, 110), (50, 124, 1), (64, 110), (66, 96)]), 'tip', 'b', False),
             strand([(40, 18), (34, 60), (38, 100)], 'deep', 'b', 1.2), strand([(60, 18), (66, 60), (62, 100)], 'deep', 'b', 1.2),
             L(outline([(44, 14), (30, 0), (30, -12), (40, -14), (52, 4)])), L(outline([(50, 12), (58, -16), (68, -18), (70, -8), (62, 12)])),
             L(ell(50, 14, 9, 3.2), 'band', 'b', ln=True)],
}

# Lennox Portsman (Suzumori Saiya): grandullón de piel morena oscura; pelo azul petróleo en rizos gordos: dos rollos encima
# de la frente y una masa enorme de rizos por detrás que le llega a los hombros; cejas gruesas del color del pelo y una
# marca azul bajo cada ojo; ojos pequeños y la boca seria
CHARS['lennox-portsman'] = {
    'body': 'corpulento', 'pal': pal('#4a7a98', '#9a6448', iris='#2a2a3a', shade='#3a6280', deep='#2a4a62'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'line', 'mouth_y': 94, 'nose': (50, 84, 3),
             'hairline': [(12, 76), (16, 60), (22, 50), (50, 46), (78, 50), (84, 60), (88, 76)]},
    'front': [L(cloud(50, 72, 64, 44, 9, 0.2)), L(outline([(2, 96), (-14, 112), (114, 112), (98, 96)])),
              L(outline([(16, 76), (14, 52), (24, 38), (50, 34), (76, 38), (86, 52), (84, 76), (78, 60), (22, 60)])),
              L(cloud(32, 30, 20, 13, 5, 0.3), 'mid', 'f'), L(cloud(68, 30, 20, 13, 5, 0.6), 'mid', 'f'),
              L(cloud(24, 54, 12, 12, 4), 'shade', 'b', False), L(cloud(76, 54, 12, 12, 4, 0.4), 'shade', 'b', False),
              L(outline([(26, 62), (32, 58), (44, 60), (44, 66), (32, 64)]), 'mid', 'f', ln=True),
              L(outline([(74, 62), (68, 58), (56, 60), (56, 66), (68, 64)]), 'mid', 'f', ln=True),
              L(quad((30, 86), (36, 89), (42, 86)), 'mid', 'f', False, False, 1.8), L(quad((58, 86), (64, 89), (70, 86)), 'mid', 'f', False, False, 1.8)],
    'side': [L(cloud(18, 70, 34, 42, 8, 0.1)), L(outline([(-14, 96), (-20, 116), (40, 116), (36, 96)])),
             L(outline([(54, 64), (58, 50), (80, 44), (86, 30), (70, 16), (40, 14), (16, 24), (6, 50), (20, 80), (40, 82), (48, 74)])),
             L(cloud(62, 22, 26, 13, 6, 0.3), 'mid', 'f'),
             L(cloud(2, 80, 18, 20, 5), 'shade', 'b', False),
             L(outline([(74, 62), (84, 58), (88, 64), (76, 66)]), 'mid', 'f', ln=True)],
    'back': [L(cloud(50, 76, 64, 42, 10, 0.2)), L(outline([(-6, 100), (-14, 116), (114, 116), (106, 100)])),
             L(cloud(50, 32, 28, 16, 6, 0.3)),
             L(cloud(30, 90, 18, 14, 5), 'shade', 'b', False), L(cloud(70, 90, 18, 14, 5, 0.5), 'shade', 'b', False)],
}

# Kaz Bloomfield (Hanamaruya Kazu): pelo rojo cereza muy abultado y alto, en una cúpula que le tapa el ojo izquierdo (la
# derecha de la imagen) y se riza hacia fuera en la punta; por debajo, mechones negros que le asoman por la nuca y los
# lados; ojo grande gris oscuro con ojeras
CHARS['kaz-bloomfield'] = {
    'body': 'delgado', 'pal': pal('#b83248', '#fcdcc4', iris='#3a3a46', shade='#962438', deep='#6e1a2a', black='#24222a'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'line', 'mouth_y': 94,
             'hairline': [(12, 70), (16, 56), (30, 50), (50, 48), (70, 48), (84, 56), (88, 70)]},
    'front': [L(outline([(16, 80), (10, 104), (18, 112, 1), (24, 96)]), 'black', 'b'), L(outline([(84, 80), (90, 104), (82, 112, 1), (76, 96)]), 'black', 'b'),
              L(outline([(12, 82), (4, 50), (8, 20), (24, -2), (46, -12), (70, -8), (88, 10), (96, 38), (94, 70), (98, 96, 1), (88, 84), (84, 64), (18, 64)])),
              L(outline([(62, -6), (86, 10), (96, 40), (92, 72), (82, 46)]), 'shade', 'b', False),
              strand([(30, 4), (24, 30)], 'deep', 'b', 1.0), strand([(50, -6), (50, 18)], 'deep', 'b', 1.0),
              fr([(40, 46), (54, 44), (72, 48), (86, 56), (90, 76), (86, 96, 1), (80, 82), (70, 92, 1), (62, 76), (54, 64)]),
              L(outline([(44, 50), (50, 52), (56, 62), (52, 58)]), 'black', 'f', False),
              L(quad((29, 82), (36, 86), (43, 82)), (150, 110, 110, 255), 'f', False, False, 1.4)],
    'side': [L(outline([(56, 60), (60, 48), (82, 44), (92, 30), (92, 6), (80, -12), (56, -20), (30, -16), (10, 0), (2, 30), (4, 60), (12, 82), (30, 90), (44, 84), (50, 72)])),
             L(outline([(4, 34), (26, 40), (30, 80), (10, 80)]), 'shade', 'b', False),
             L(outline([(14, 82), (20, 98), (14, 106, 1), (28, 102), (34, 90)]), 'black', 'b'),
             L(outline([(70, 44), (86, 52), (88, 70, 1), (78, 60)]), 'mid', 'f')],
    'back': [L(outline([(14, 86), (6, 50), (10, 20), (26, -2), (50, -10), (74, -4), (90, 16), (96, 48), (90, 84), (70, 92), (30, 92)])),
             L(outline([(58, -6), (86, 12), (96, 48), (90, 82), (66, 90)]), 'shade', 'b', False),
             L(outline([(24, 90), (20, 106), (30, 100), (36, 110), (42, 98), (50, 108), (58, 98), (64, 110), (70, 100), (80, 106), (76, 90)]), 'black', 'b')],
}

# Govin Castlehoven (Yashiro Suberu): pelo gris muy oscuro largo y lacio que le cae por delante y por detrás, con mechones
# que salen hacia los lados y se enroscan en la punta, y una antena curva en lo alto; ojos morados en espiral con ojeras
CHARS['govin-castlehoven'] = {
    'body': 'delgado', 'pal': pal('#3e4248', '#f2c8a4', iris='#9a4ac0', shade='#2e3236', deep='#1e2024'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'frown', 'mouth_y': 95,
             'hairline': [(12, 76), (18, 56), (32, 46), (46, 50), (50, 40), (54, 50), (68, 46), (82, 56), (88, 76)]},
    'front': [L(outline([(14, 60), (0, 100), (-4, 130, 1), (14, 118), (24, 96)])), L(outline([(86, 60), (100, 100), (104, 130, 1), (86, 118), (76, 96)])),
              L(rope((12, 66), (-10, 70), (-18, 58), 5)), L(rope((88, 66), (110, 70), (118, 58), 5)),
              L(rope((12, 88), (-8, 92), (-14, 82), 4)), L(rope((88, 90), (106, 96), (112, 86), 4)),
              L(outline([(12, 80), (8, 44), (18, 20), (38, 8), (62, 8), (82, 20), (92, 44), (88, 80), (82, 62), (18, 62)])),
              L(outline([(58, 10), (82, 22), (92, 46), (88, 74), (78, 44)]), 'shade', 'b', False),
              L(rope((50, 10), (44, -10), (60, -14), 3.6)),
              fr([(18, 56), (34, 46), (44, 48), (32, 70), (26, 108, 1), (20, 76)]), fr([(82, 56), (66, 46), (56, 48), (68, 70), (74, 108, 1), (80, 76)]),
              L(ell(36, 80, 6.4, 2.2), (150, 110, 120, 255), 'b', False), L(ell(64, 80, 6.4, 2.2), (150, 110, 120, 255), 'b', False)],
    'side': [L(outline([(54, 62), (58, 50), (80, 44), (90, 30), (86, 12), (66, 2), (40, 2), (18, 12), (4, 36), (0, 70), (-4, 104), (2, 126, 1), (14, 106), (24, 90),
                        (40, 86), (48, 74)])),
             L(rope((20, 30), (-14, 30), (-30, 18), 5)), L(rope((40, 4), (40, -14), (58, -16), 3.6)),
             L(outline([(4, 40), (26, 46), (30, 84), (8, 92)]), 'shade', 'b', False),
             L(outline([(76, 46), (88, 60), (86, 92, 1), (80, 70)]), 'mid', 'f')],
    'back': [L(outline([(12, 80), (8, 42), (18, 18), (38, 6), (62, 6), (82, 18), (92, 42), (88, 80), (92, 110), (80, 124, 1), (70, 110), (60, 124, 1), (50, 112),
                        (40, 124, 1), (30, 110), (20, 124, 1), (8, 110)])),
             L(rope((12, 70), (-10, 74), (-18, 62), 5)), L(rope((88, 70), (110, 74), (118, 62), 5)),
             L(rope((12, 94), (-6, 98), (-12, 88), 4)), L(rope((88, 94), (106, 98), (112, 88), 4)),
             L(rope((50, 8), (52, -10), (36, -14), 3.6)),
             L(outline([(58, 8), (82, 20), (92, 46), (88, 104), (64, 110)]), 'shade', 'b', False)],
}

# Floramira Pagotta (Gojuudera Manaka): melena corta ondulada morada casi negra, a la altura de la mandíbula, con las puntas
# hacia fuera y un mechón lila claro que le cruza la cabeza; flequillo apartado a un lado que deja la frente; ojos grises con
# mucho delineado y una sonrisa tranquila
CHARS['floramira-pagotta'] = {
    'body': 'chica', 'pal': pal('#3a2a42', '#fcdcc4', iris='#7a8a8a', shade='#2a1e30', deep='#1c1420', lilac='#a8a4d4'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 93,
             'hairline': [(12, 70), (16, 56), (26, 46), (40, 42), (56, 40), (70, 46), (82, 56), (88, 70)]},
    'front': [L(outline([(16, 64), (4, 82), (2, 98, 1), (14, 92), (22, 98, 1), (24, 84)])), L(outline([(84, 64), (96, 82), (98, 98, 1), (86, 92), (78, 98, 1), (76, 84)])),
              L(outline([(12, 76), (8, 42), (18, 18), (40, 6), (62, 6), (82, 18), (92, 42), (88, 76), (82, 60), (18, 60)])),
              L(outline([(58, 8), (82, 20), (92, 46), (88, 70), (78, 44)]), 'shade', 'b', False),
              L(outline([(14, 50), (18, 26), (34, 12), (54, 8), (58, 14), (40, 18), (26, 32), (20, 52)]), 'lilac', 'b', False),
              fr([(56, 40), (70, 42), (84, 52), (90, 70), (86, 86, 1), (80, 66), (68, 50)]),
              L([(68, 86), (69, 88)], OUTC, 'f', False, False, 1.6)] + lashes(n=2),
    'side': [L(outline([(54, 62), (58, 50), (80, 44), (90, 30), (86, 12), (66, 2), (40, 2), (18, 12), (4, 36), (2, 64), (-2, 84), (2, 98, 1), (14, 90), (24, 98, 1),
                        (30, 88), (44, 82), (50, 72)])),
             L(outline([(26, 6), (48, 2), (70, 8), (68, 14), (48, 10), (30, 14)]), 'lilac', 'b', False),
             L(outline([(4, 40), (26, 46), (30, 82), (8, 86)]), 'shade', 'b', False)] + lash_side(),
    'back': [L(outline([(10, 80), (8, 42), (18, 18), (40, 6), (62, 6), (82, 18), (92, 42), (90, 80), (96, 96, 1), (80, 92), (66, 98, 1), (56, 90), (44, 98, 1), (34, 90),
                        (20, 98, 1), (4, 96, 1)])),
             L(outline([(18, 30), (34, 12), (56, 6), (58, 14), (38, 20), (24, 34)]), 'lilac', 'b', False),
             L(outline([(58, 8), (82, 20), (92, 46), (88, 84), (66, 90)]), 'shade', 'b', False)],
}

# Alistar Montero (Renzan Hamato): piel tostada; pelo largo malva oscuro con raya en medio, liso, que le cae por los lados
# de la cara hasta el pecho, con mechones finos sueltos delante; ojos morados y media sonrisa
CHARS['alistar-montero'] = {
    'body': 'normal', 'pal': pal('#8a4a5c', '#dca07c', iris='#6a4ab8', shade='#6e3a4a', deep='#522a36'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 94,
             'hairline': [(12, 80), (16, 56), (24, 44), (40, 38), (50, 30), (60, 38), (76, 44), (84, 56), (88, 80)]},
    'front': [L(outline([(16, 64), (6, 96), (4, 124, 1), (16, 114), (22, 96)])), L(outline([(84, 64), (94, 96), (96, 124, 1), (84, 114), (78, 96)])),
              L(outline([(12, 84), (8, 44), (18, 18), (40, 4), (60, 4), (82, 18), (92, 44), (88, 84), (82, 62), (18, 62)])),
              L(outline([(58, 6), (82, 20), (92, 46), (88, 80), (78, 44)]), 'shade', 'b', False),
              strand([(50, 4), (50, 30)], 'deep', 'b', 1.2),
              L(quad((20, 80), (16, 100), (12, 118)), 'mid', 'f', False, False, 1.8), L(quad((80, 80), (84, 100), (88, 118)), 'mid', 'f', False, False, 1.8)],
    'side': [L(outline([(54, 62), (58, 50), (80, 42), (90, 28), (86, 12), (66, 0), (40, 0), (18, 10), (4, 36), (0, 80), (-2, 112), (4, 128, 1), (16, 110), (30, 96),
                        (44, 86), (50, 74)])),
             L(outline([(4, 40), (28, 44), (34, 90), (8, 104)]), 'shade', 'b', False)],
    'back': [L(outline([(10, 84), (8, 42), (18, 16), (40, 2), (60, 2), (82, 16), (92, 42), (90, 84), (94, 118), (82, 126, 1), (66, 118), (50, 128, 1), (34, 118),
                        (18, 126, 1), (6, 118)])),
             L(outline([(58, 4), (84, 18), (94, 50), (92, 116), (64, 120)]), 'shade', 'b', False),
             strand([(50, 4), (50, 60)], 'deep', 'b', 1.0)],
}

# Elijah Singleton (Ikue Magoichi, capitán): casco de pelo castaño en forma de seta con el flequillo recto hasta las gafas
# y un moño arriba del que salen dos palitos oscuros en V; gafas redondas rojas y los ojos cerrados de sonrisa; dos
# mechones finos le cuelgan junto a las orejas
CHARS['elijah-singleton'] = {
    'body': 'normal', 'pal': pal('#80643e', '#fcdcc4', shade='#64502e', deep='#4a3a20', stick='#3a2a1e'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'line', 'mouth_y': 94, 'glasses': (190, 52, 60, 255), 'hairline': False},
    'front': [L(rope((44, 12), (36, 0), (26, -18), 3.0), 'stick', 'b'), L(rope((56, 12), (64, 0), (74, -18), 3.0), 'stick', 'b'),
              L(outline([(16, 78), (12, 98, 1), (22, 86)]), 'deep', 'b'), L(outline([(84, 78), (88, 98, 1), (78, 86)]), 'deep', 'b'),
              L(cloud(50, 10, 14, 11, 4, 0.3)), L(ell(50, 18, 13, 3), 'deep', 'b', False),
              L(outline([(4, 64), (6, 40), (20, 22), (50, 16), (80, 22), (94, 40), (96, 64), (82, 66), (66, 64), (50, 66), (34, 64), (18, 66)]), 'mid', 'f'),
              L(outline([(58, 18), (82, 26), (94, 44), (94, 60), (80, 44)]), 'shade', 'f', False),
              strand([(30, 50), (30, 64)], 'deep', 'f', 1.0), strand([(50, 50), (50, 64)], 'deep', 'f', 1.0), strand([(70, 50), (70, 64)], 'deep', 'f', 1.0)],
    'side': [L(rope((50, 6), (44, -6), (36, -20), 3.0), 'stick', 'b'),
             L(cloud(52, 4, 13, 11, 4, 0.3)), L(ell(52, 12, 12, 3), 'deep', 'b', False),
             L(outline([(20, 82), (14, 98, 1), (30, 90)]), 'deep', 'b'),
             L(outline([(52, 70), (60, 64), (92, 64), (94, 48), (84, 28), (60, 14), (34, 16), (12, 30), (2, 52), (8, 76), (24, 86), (40, 80)])),
             L(outline([(4, 50), (30, 52), (34, 78), (12, 76)]), 'shade', 'b', False)],
    'back': [L(rope((44, 8), (36, -4), (26, -20), 3.0), 'stick', 'b'), L(rope((56, 8), (64, -4), (74, -20), 3.0), 'stick', 'b'),
             L(cloud(50, 8, 14, 11, 4, 0.3)), L(ell(50, 16, 13, 3), 'deep', 'b', False),
             L(outline([(18, 82), (14, 100, 1), (26, 88)]), 'deep', 'b'), L(outline([(82, 82), (86, 100, 1), (74, 88)]), 'deep', 'b'),
             L(outline([(16, 80), (6, 58), (8, 38), (24, 20), (50, 14), (76, 20), (92, 38), (94, 58), (84, 80), (50, 86)])),
             L(outline([(58, 16), (82, 26), (94, 50), (86, 78), (64, 84)]), 'shade', 'b', False)],
}

# Rohan Snatchett (Ujiie Touichi): pelo naranja rojizo con dos moños pequeños a los lados de la cabeza, mechones largos que
# le enmarcan la cara hasta la barbilla y un flequillo grueso que le cae de su derecha a su izquierda; ojos azules caídos
CHARS['rohan-snatchett'] = {
    'body': 'normal', 'pal': pal('#e2561e', '#fcdcc4', iris='#4a8ac8', shade='#bc4214', deep='#8e300e'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'line', 'mouth_y': 95,
             'hairline': [(12, 76), (16, 58), (26, 48), (40, 44), (56, 42), (72, 46), (84, 56), (88, 76)]},
    'front': [L(cloud(8, 40, 10, 10, 4, 0.3)), L(cloud(92, 40, 10, 10, 4, 0.6)),
              L(outline([(16, 62), (8, 90), (10, 110, 1), (20, 96), (24, 80)])), L(outline([(84, 62), (92, 90), (90, 110, 1), (80, 96), (76, 80)])),
              L(outline([(12, 80), (8, 44), (18, 18), (40, 4), (62, 4), (82, 18), (92, 44), (88, 80), (82, 60), (18, 60)])),
              L(outline([(58, 6), (82, 20), (92, 46), (88, 74), (78, 44)]), 'shade', 'b', False),
              strand([(50, 6), (50, 24)], 'deep', 'b', 1.0),
              fr([(14, 60), (16, 40), (30, 30), (50, 30), (66, 40), (60, 60, 1), (52, 48), (40, 44), (28, 48), (20, 62, 1)])],
    'side': [L(cloud(10, 28, 10, 10, 4, 0.3)),
             L(outline([(54, 62), (58, 50), (80, 42), (90, 28), (86, 12), (66, 0), (40, 0), (18, 10), (4, 36), (4, 66), (14, 84), (28, 90), (42, 84), (48, 72)])),
             L(outline([(4, 40), (26, 46), (30, 82), (10, 80)]), 'shade', 'b', False),
             L(outline([(58, 46), (68, 56), (68, 98, 1), (60, 76)]), 'mid', 'f')],
    'back': [L(cloud(8, 42, 10, 10, 4, 0.3)), L(cloud(92, 42, 10, 10, 4, 0.6)),
             L(outline([(12, 84), (8, 42), (18, 16), (40, 2), (60, 2), (82, 16), (92, 42), (88, 84), (70, 94), (50, 90), (30, 94)])),
             L(outline([(58, 4), (84, 18), (94, 50), (88, 82), (66, 92)]), 'shade', 'b', False),
             strand([(50, 4), (50, 86)], 'deep', 'b', 1.0)],
}

# Umbren Lightwood (Kurashiki Akari): pelo azul violeta muy abultado en mechones gruesos que salen hacia los lados como
# pétalos, con un flequillo recto que le llega a los ojos; ojos oscuros entornados con la raya marcada
CHARS['umbren-lightwood'] = {
    'body': 'normal', 'pal': pal('#4a52a2', '#fcdcc4', iris='#2a2a40', shade='#3a4080', deep='#2a2e60'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(14, 96), (2, 100, 1), (8, 86), (-6, 78, 1), (6, 66), (-10, 46, 1), (8, 40), (0, 16, 1), (22, 14), (34, -6, 1), (50, 6), (62, -6, 1), (76, 10),
                         (98, 10, 1), (92, 30), (110, 40, 1), (94, 56), (106, 74, 1), (92, 80), (98, 96, 1), (86, 96), (82, 64), (18, 64)])),
              L(outline([(60, 0), (84, 12), (100, 40), (94, 80), (82, 54)]), 'shade', 'b', False),
              fr([(12, 66), (12, 44), (24, 30), (50, 26), (76, 30), (88, 44), (88, 66), (80, 68, 1), (74, 62), (64, 68, 1), (58, 62), (50, 68, 1), (42, 62), (36, 68, 1),
                  (26, 62), (20, 68, 1)])],
    'side': [L(outline([(54, 64), (58, 52), (80, 46), (92, 34), (92, 14), (104, 4, 1), (80, 0), (74, -16, 1), (56, -6), (36, -10, 1), (24, 4), (-2, 6, 1), (6, 26),
                        (-12, 40, 1), (2, 54), (-8, 74, 1), (8, 76), (6, 96, 1), (20, 88), (30, 98, 1), (40, 86), (48, 76)])),
             L(outline([(2, 42), (26, 48), (30, 84), (8, 84)]), 'shade', 'b', False),
             fr([(74, 30), (92, 34), (96, 52), (92, 68, 1), (84, 56), (80, 66, 1), (76, 50)])],
    'back': [L(outline([(14, 96), (0, 98, 1), (8, 86), (-8, 76, 1), (6, 66), (-10, 46, 1), (8, 40), (0, 16, 1), (22, 14), (34, -6, 1), (50, 6), (62, -6, 1), (76, 10),
                        (100, 10, 1), (92, 30), (110, 42, 1), (94, 58), (108, 76, 1), (92, 84), (100, 98, 1), (82, 98), (70, 104, 1), (60, 96), (46, 106, 1), (36, 96),
                        (24, 106, 1)])),
             L(outline([(58, 2), (84, 12), (100, 42), (94, 92), (64, 96)]), 'shade', 'b', False)],
}

# Blaine Westbrook (Saijou Lill): casco de pelo lila grisáceo, con el flequillo en picos irregulares y los lados hasta la
# mandíbula, más oscuros por abajo; ojos muy abiertos de pupila pequeña verde oliva y una sonrisa pícara
CHARS['blaine-westbrook'] = {
    'body': 'normal', 'pal': pal('#aaa6d0', '#fcdcc4', iris='#6a6a3e', shade='#8a7ea8', deep='#6a5a80'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 94,
             'hairline': [(10, 82), (14, 62), (20, 56), (24, 62), (30, 52), (38, 58), (44, 48), (50, 56), (56, 46), (62, 56), (70, 50), (76, 60), (82, 54), (86, 62), (90, 82)]},
    'front': [L(outline([(10, 92), (4, 60), (8, 30), (24, 10), (50, 2), (76, 10), (92, 30), (96, 60), (90, 92), (84, 82), (82, 64), (18, 64), (16, 82)])),
              L(outline([(4, 64), (10, 92), (16, 82), (18, 64)]), 'shade', 'b', False), L(outline([(96, 64), (90, 92), (84, 82), (82, 64)]), 'shade', 'b', False),
              L(outline([(60, 4), (84, 16), (96, 44), (92, 64), (80, 40)]), 'shade', 'b', False)],
    'side': [L(outline([(54, 66), (58, 54), (72, 52), (78, 60), (82, 50), (90, 46), (92, 26), (78, 6), (50, -2), (22, 6), (4, 30), (2, 62), (8, 88), (26, 96), (40, 90),
                        (48, 80)])),
             L(outline([(2, 56), (30, 60), (40, 90), (26, 96), (8, 88)]), 'shade', 'b', False)],
    'back': [L(outline([(8, 92), (4, 60), (8, 30), (24, 10), (50, 2), (76, 10), (92, 30), (96, 60), (92, 92), (80, 98, 1), (72, 90), (62, 98, 1), (50, 90), (38, 98, 1),
                        (28, 90), (20, 98, 1)])),
             L(outline([(4, 56), (30, 62), (50, 56), (70, 62), (96, 56), (92, 92), (50, 96), (8, 92)]), 'shade', 'b', False)],
}

# Marinus Courier (Uchinari Kaiji): piel morena oscura; pelo granate en pinchos grandes hacia arriba y hacia fuera; cejas
# gruesas granates, una franja de barba negra que baja por cada lado de la mandíbula; ojos grandes y sonrisa de dientes
CHARS['marinus-courier'] = {
    'body': 'normal', 'pal': pal('#8e1e22', '#7a4a30', iris='#1e1414', shade='#6e1418', deep='#4e0e10', beard='#1c1416'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 94,
             'hairline': [(12, 66), (20, 54), (34, 50), (50, 52), (66, 50), (80, 54), (88, 66)]},
    'front': [L(outline([(14, 66), (-4, 64, 1), (8, 50), (-10, 34, 1), (12, 30), (8, 6, 1), (26, 14), (30, -10, 1), (44, 8), (54, -14, 1), (60, 8), (82, -6, 1), (76, 16),
                         (104, 22, 1), (90, 34), (108, 48, 1), (90, 54), (100, 66, 1), (86, 66), (82, 58), (18, 58)])),
              L(outline([(58, 0), (80, -4), (78, 16), (96, 30), (92, 56), (80, 40)]), 'shade', 'b', False),
              L(outline([(18, 70), (24, 70), (28, 96), (40, 104), (50, 106), (30, 104), (20, 92)]), 'beard', 'f', False),
              L(outline([(82, 70), (76, 70), (72, 96), (60, 104), (50, 106), (70, 104), (80, 92)]), 'beard', 'f', False)],
    'side': [L(outline([(54, 60), (58, 50), (80, 44), (92, 32), (110, 26, 1), (92, 16), (100, 0, 1), (80, 4), (78, -16, 1), (62, 0), (44, -16, 1), (36, 4), (12, -2, 1),
                        (14, 20), (-8, 26, 1), (6, 40), (-6, 56, 1), (8, 62), (8, 80), (24, 88), (40, 82), (48, 70)])),
             L(outline([(4, 40), (26, 46), (30, 80), (10, 78)]), 'shade', 'b', False),
             L(outline([(50, 76), (56, 76), (66, 96), (78, 102), (70, 104), (56, 96)]), 'beard', 'f', False)],
    'back': [L(outline([(14, 82), (-4, 76, 1), (8, 62), (-10, 44, 1), (10, 36), (8, 8, 1), (26, 14), (30, -10, 1), (44, 6), (54, -14, 1), (62, 6), (82, -6, 1), (78, 16),
                        (106, 22, 1), (92, 36), (110, 50, 1), (92, 60), (102, 76, 1), (86, 82), (50, 86)])),
             L(outline([(56, 0), (80, -4), (80, 16), (98, 34), (92, 80), (62, 84)]), 'shade', 'b', False)],
}

# Drexel Kixley (Masakari Kitaru): grandullón; pelo naranja corto y revuelto arriba sobre los lados y la nuca rapados en
# gris; orejas grandes, mofletes sonrosados, ojos estrechos y la boca abierta de burla
CHARS['drexel-kixley'] = {
    'body': 'corpulento', 'pal': pal('#e8842a', '#fcd2b0', iris='#a88a3a', shade='#c46a1c', deep='#9a5012', gray='#8a8682', gray_d='#6a6662'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'big_ears': 3, 'ear_out': 4, 'nose': (50, 86, 4),
             'hairline': [(12, 66), (16, 52), (26, 44), (38, 52), (50, 42), (62, 52), (74, 44), (84, 52), (88, 66)]},
    'front': [L(outline([(14, 70), (12, 40), (22, 22), (78, 22), (88, 40), (86, 70), (80, 56), (20, 56)]), 'gray'),
              L(outline([(18, 44), (14, 30), (8, 18, 1), (22, 16), (24, 2, 1), (36, 8), (44, -6, 1), (52, 6), (62, -6, 1), (66, 8), (80, 2, 1), (78, 16), (92, 20, 1),
                         (84, 30), (82, 46), (74, 38), (62, 50, 1), (56, 38), (48, 50, 1), (42, 38), (30, 50, 1), (24, 38)])),
              L(outline([(56, 4), (66, 6), (80, 2), (78, 16), (88, 22), (84, 40), (74, 30)]), 'shade', 'b', False),
              L(ell(26, 90, 5, 3), (240, 150, 140, 255), 'f', False), L(ell(74, 90, 5, 3), (240, 150, 140, 255), 'f', False)],
    'side': [L(outline([(54, 62), (60, 48), (82, 40), (88, 26), (70, 12), (40, 10), (18, 18), (6, 40), (6, 66), (20, 84), (36, 84), (46, 72)]), 'gray'),
             L(outline([(4, 54), (30, 58), (46, 72), (36, 84), (20, 84), (8, 70)]), 'gray_d', 'b', False),
             L(outline([(12, 30), (8, 18, 1), (22, 14), (28, -2, 1), (40, 8), (52, -6, 1), (60, 6), (74, -4, 1), (76, 10), (94, 14, 1), (86, 24), (90, 40, 1), (78, 36),
                        (66, 42, 1), (58, 32), (44, 40, 1), (36, 30), (20, 38, 1)]))],
    'back': [L(outline([(14, 80), (10, 40), (22, 18), (78, 18), (90, 40), (86, 80), (50, 88)]), 'gray'),
             L(outline([(12, 56), (50, 62), (88, 56), (86, 80), (50, 88), (14, 80)]), 'gray_d', 'b', False),
             L(outline([(14, 36), (8, 18, 1), (22, 14), (26, 0, 1), (38, 8), (46, -6, 1), (54, 6), (64, -6, 1), (68, 8), (80, 2, 1), (78, 16), (94, 20, 1), (86, 34),
                        (76, 44, 1), (66, 34), (54, 44, 1), (46, 34), (34, 44, 1), (26, 34)]))],
}

# Volk Lorius (Dentouda Tokinosuke): lleva una máscara blanca de zorro (kitsune) que le tapa toda la cara, con las orejas
# moradas por dentro, rayas negras de bigote, un ojo cerrado pintado y por el otro hueco se le ve el ojo naranja; pelo
# naranja en media melena con las puntas hacia fuera; cordones morados con borlas a los lados y el lazo atado por detrás
_MASK = outline([(22, 44), (16, 20, 1), (32, 36), (50, 32), (68, 36), (84, 20, 1), (78, 44), (84, 70), (72, 92), (54, 108, 1), (46, 108, 1), (28, 92), (16, 70)])
CHARS['volk-lorius'] = {
    'body': 'normal', 'pal': pal('#e87a1e', '#fcdcc4', iris='#d0601c', shade='#c4600e', deep='#9a480a', mask=WHITE, ear='#8a48b8', cord='#6a2a9a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': [L(outline([(16, 54), (2, 70), (-6, 82, 1), (10, 78), (20, 86)])), L(outline([(84, 54), (98, 70), (106, 82, 1), (90, 78), (80, 86)])),
              L(outline([(12, 74), (8, 42), (18, 18), (40, 6), (62, 6), (82, 18), (92, 42), (88, 74), (82, 60), (18, 60)])),
              L(outline([(58, 8), (82, 20), (92, 46), (88, 70), (78, 44)]), 'shade', 'b', False),
              L(_MASK, 'mask', 'f', ln=True),
              L(outline([(22, 40), (20, 26, 1), (30, 36)]), 'ear', 'f', False), L(outline([(78, 40), (80, 26, 1), (70, 36)]), 'ear', 'f', False),
              L(quad((30, 70), (36, 74), (42, 70)), OUTC, 'f', False, False, 1.8),
              L(outline([(58, 70), (66, 66), (72, 70), (66, 76)]), WHITE, 'f', False),
              L(ell(65, 71, 2.6, 2.8), 'iris', 'f', False),
              L([(56, 68), (62, 64)], OUTC, 'f', False, False, 1.4), L([(36, 56), (40, 62)], OUTC, 'f', False, False, 1.0), L([(64, 56), (60, 62)], OUTC, 'f', False, False, 1.0),
              L([(48, 104), (52, 104)], OUTC, 'f', False, False, 1.6),
              L(rope((14, 64), (10, 80), (12, 96), 2.4), 'cord', 'f'), L(ell(12, 100, 3, 5), 'cord', 'f', ln=True),
              L(rope((86, 64), (90, 80), (88, 96), 2.4), 'cord', 'f'), L(ell(88, 100, 3, 5), 'cord', 'f', ln=True)],
    'side': [L(outline([(54, 62), (58, 50), (80, 42), (90, 28), (86, 12), (66, 0), (40, 0), (18, 10), (4, 36), (4, 62), (-4, 76, 1), (14, 78), (28, 86), (42, 82),
                        (48, 70)])),
             L(outline([(4, 40), (26, 46), (30, 80), (10, 76)]), 'shade', 'b', False),
             L(outline([(70, 30), (76, 12, 1), (82, 34), (92, 50), (96, 76), (112, 94, 1), (96, 96), (86, 104), (74, 96), (72, 70)]), 'mask', 'f', ln=True),
             L(outline([(76, 30), (77, 18, 1), (80, 32)]), 'ear', 'f', False),
             L(quad((84, 72), (88, 74), (92, 72)), OUTC, 'f', False, False, 1.6),
             L(rope((60, 60), (46, 66), (40, 92), 2.4), 'cord', 'f'), L(ell(40, 96, 3, 5), 'cord', 'f', ln=True)],
    'back': [L(outline([(12, 80), (8, 42), (18, 16), (40, 2), (60, 2), (82, 16), (92, 42), (88, 70), (104, 80, 1), (86, 84), (70, 90), (50, 86), (30, 90), (14, 84),
                        (-4, 80, 1)])),
             L(outline([(58, 4), (84, 18), (94, 50), (88, 80), (66, 88)]), 'shade', 'b', False),
             L(quad((10, 52), (50, 58), (90, 52)), 'cord', 'f', False, False, 2.4),
             L(outline([(50, 56), (38, 50), (36, 62)]), 'cord', 'f', ln=True), L(outline([(50, 56), (62, 50), (64, 62)]), 'cord', 'f', ln=True),
             L(rope((48, 58), (44, 80), (42, 104), 2.4), 'cord', 'f'), L(rope((52, 58), (56, 80), (58, 104), 2.4), 'cord', 'f'),
             L(ell(86, 96, 3, 5), 'cord', 'f', ln=True)],
}

# Dawsey Geistfeld (Kamata Mudou): pelo gris claro ondulado, peinado de lado sobre la frente, con un mechón en forma de lazo
# levantado arriba a su izquierda y ondas que le caen a los lados hasta la mandíbula; ojos grises en espiral con rayas negras
# de payaso debajo, un corazoncito rosa en la nariz y una sonrisa
CHARS['dawsey-geistfeld'] = {
    'body': 'delgado', 'pal': pal('#bcbcbc', '#fce4d8', iris='#8a8a92', shade='#9a9a9c', deep='#7a7a7c', pink='#e886a0'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(12, 76), (14, 60), (22, 50), (36, 44), (50, 48), (60, 56), (66, 46), (78, 50), (86, 60), (88, 76)]},
    'front': [L(outline([(16, 62), (4, 78), (10, 92), (2, 104, 1), (16, 100), (22, 86)])), L(outline([(84, 62), (96, 78), (90, 92), (98, 104, 1), (84, 100), (78, 86)])),
              L(outline([(12, 76), (8, 42), (18, 18), (40, 6), (62, 6), (82, 18), (92, 42), (88, 76), (82, 60), (18, 60)])),
              L(outline([(60, 12), (64, -6, 1), (74, 4), (84, -6, 1), (86, 8), (98, 12, 1), (84, 20), (70, 20)])),
              L(outline([(58, 8), (82, 20), (92, 46), (88, 70), (78, 44)]), 'shade', 'b', False),
              fr([(14, 60), (16, 40), (30, 28), (50, 24), (58, 30), (54, 44), (60, 58), (52, 66, 1), (46, 52), (36, 46), (24, 50)]),
              L([(30, 84), (32, 89)], OUTC, 'f', False, False, 1.2), L([(36, 84), (36, 90)], OUTC, 'f', False, False, 1.2), L([(42, 84), (40, 89)], OUTC, 'f', False, False, 1.2),
              L([(58, 84), (60, 89)], OUTC, 'f', False, False, 1.2), L([(64, 84), (64, 90)], OUTC, 'f', False, False, 1.2), L([(70, 84), (68, 89)], OUTC, 'f', False, False, 1.2),
              L(ell(50, 85, 2.0, 1.6), 'pink', 'f', False)],
    'side': [L(outline([(54, 62), (58, 50), (80, 42), (90, 28), (86, 12), (66, 0), (40, 0), (18, 10), (4, 36), (4, 62), (-2, 80), (6, 98, 1), (14, 84), (28, 90), (42, 82),
                        (48, 70)])),
             L(outline([(30, 6), (20, -10, 1), (34, -4), (40, -16, 1), (44, 2), (50, 4)])),
             L(outline([(4, 40), (26, 46), (30, 82), (10, 80)]), 'shade', 'b', False),
             L(outline([(74, 40), (90, 46), (96, 64), (88, 80, 1), (86, 62)]), 'mid', 'f')],
    'back': [L(outline([(12, 80), (8, 42), (18, 16), (40, 2), (60, 2), (82, 16), (92, 42), (88, 80), (94, 96, 1), (78, 92), (60, 96), (40, 92), (22, 96), (6, 96, 1)])),
             L(outline([(22, 10), (10, -8, 1), (24, -6), (26, -20, 1), (36, -6), (40, 4)])),
             L(outline([(58, 4), (84, 18), (94, 50), (88, 84), (66, 92)]), 'shade', 'b', False)],
}

# Rael Abbeybogy (Teramae Reiru): grandote de cara muy redonda y mofletuda, piel tostada; casco de pelo morado oscuro
# grueso, con el borde recto sobre las cejas; tres rayas negras como bigotes en cada moflete, ojos pequeños y boca de enfado
_rael_face = outline([(12, 56), (50, 48), (88, 56), (100, 80), (92, 102), (70, 114), (50, 116), (30, 114), (8, 102), (0, 80)])
CHARS['rael-abbeybogy'] = {
    'body': 'corpulento', 'pal': pal('#4c2c5e', '#cc966c', iris='#2a2030', shade='#3a2048', deep='#281632'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'frown', 'mouth_y': 102, 'eye_y': 78, 'nose': (50, 90, 3.4), 'face_front': _rael_face, 'ear_out': 16,
             'hairline': False},
    'front': [L(outline([(2, 66), (2, 36), (16, 12), (50, 2), (84, 12), (98, 36), (98, 66), (84, 64), (66, 62), (50, 66), (34, 62), (16, 64)]), 'mid', 'f'),
              L(outline([(60, 6), (86, 16), (98, 40), (96, 62), (82, 40)]), 'shade', 'f', False),
              strand([(36, 46), (34, 62)], 'deep', 'f', 1.0), strand([(64, 46), (66, 62)], 'deep', 'f', 1.0),
              L([(14, 82), (28, 84)], OUTC, 'f', False, False, 1.4), L([(16, 90), (28, 88)], OUTC, 'f', False, False, 1.4), L([(20, 96), (30, 92)], OUTC, 'f', False, False, 1.4),
              L([(86, 82), (72, 84)], OUTC, 'f', False, False, 1.4), L([(84, 90), (72, 88)], OUTC, 'f', False, False, 1.4), L([(80, 96), (70, 92)], OUTC, 'f', False, False, 1.4)],
    'side': [L(outline([(48, 70), (56, 60), (94, 60), (92, 40), (78, 18), (50, 8), (22, 14), (4, 34), (2, 60), (14, 76), (30, 78)])),
             L(outline([(4, 50), (30, 52), (30, 76), (12, 72)]), 'shade', 'b', False),
             L([(76, 86), (88, 86)], OUTC, 'f', False, False, 1.4), L([(76, 92), (86, 90)], OUTC, 'f', False, False, 1.4)],
    'back': [L(outline([(8, 76), (2, 46), (14, 18), (50, 6), (86, 18), (98, 46), (92, 76), (50, 82)])),
             L(outline([(4, 54), (50, 60), (96, 54), (92, 76), (50, 82), (8, 76)]), 'shade', 'b', False)],
}

# Zelane Whitlow (Nanakaidou Haku, portero): piel morena; pelo blanco peinado hacia arriba en un moño alto, con mechones
# largos y puntiagudos que le enmarcan la cara y una trenza larga de cuentas (bultos) que le cae por un lado; cejas blancas
# gruesas, ojos verde oliva, marcas oscuras bajo los ojos y una sonrisa de dientes
CHARS['zelane-whitlow'] = {
    'body': 'normal', 'pal': pal('#ece8e2', '#7a4a32', iris='#8a8a3a', shade='#c8c0c0', deep='#a89a9e', tie='#3a3a3a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 94,
             'hairline': [(12, 70), (18, 52), (30, 40), (44, 42), (50, 30), (56, 42), (70, 40), (82, 52), (88, 70)]},
    'front': [L(outline([(16, 60), (10, 90), (14, 112, 1), (22, 92), (24, 74)])), L(outline([(84, 60), (90, 90), (86, 112, 1), (78, 92), (76, 74)])),
              L(ell(14, 86, 5, 6), 'mid', 'b', ln=True), L(ell(10, 98, 5, 6), 'mid', 'b', ln=True), L(ell(8, 110, 4.4, 5), 'mid', 'b', ln=True),
              L(outline([(12, 70), (10, 40), (20, 18), (40, 8), (60, 8), (80, 18), (90, 40), (88, 70), (82, 58), (18, 58)])),
              L(cloud(50, 2, 11, 10, 4, 0.3)), L(ell(50, 12, 9, 2.4), 'tie', 'b', False),
              L(outline([(58, 10), (80, 20), (90, 44), (86, 66), (78, 44)]), 'shade', 'b', False),
              L(outline([(26, 64), (40, 62), (44, 66), (28, 68)]), 'mid', 'f', ln=True), L(outline([(74, 64), (60, 62), (56, 66), (72, 68)]), 'mid', 'f', ln=True),
              L([(28, 82), (34, 86)], OUTC, 'f', False, False, 1.2), L([(72, 82), (66, 86)], OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(54, 62), (58, 50), (80, 44), (90, 30), (86, 14), (66, 4), (40, 4), (18, 14), (6, 36), (6, 60), (16, 76), (30, 82), (42, 78), (48, 70)])),
             L(cloud(48, -2, 11, 10, 4, 0.3)), L(ell(48, 8, 9, 2.4), 'tie', 'b', False),
             L(ell(30, 4, 6, 6), 'mid', 'b', ln=True), L(ell(18, 14, 6, 6.4), 'mid', 'b', ln=True), L(ell(6, 28, 6, 6.4), 'mid', 'b', ln=True),
             L(ell(-2, 44, 5.4, 6), 'mid', 'b', ln=True), L(ell(-6, 60, 5, 5.4), 'mid', 'b', ln=True), L(outline([(-8, 64), (-14, 82, 1), (-2, 66)])),
             L(outline([(6, 40), (28, 44), (32, 78), (14, 74)]), 'shade', 'b', False),
             L(outline([(74, 46), (86, 56), (84, 90, 1), (78, 70)]), 'mid', 'f')],
    'back': [L(outline([(14, 82), (10, 40), (20, 18), (40, 8), (60, 8), (80, 18), (90, 40), (86, 82), (50, 88)])),
             L(outline([(58, 10), (80, 20), (90, 44), (86, 80), (62, 86)]), 'shade', 'b', False),
             L(cloud(50, 0, 12, 11, 4, 0.3)), L(ell(50, 12, 9, 2.4), 'tie', 'b', False),
             L(ell(54, 22, 7, 6), 'mid', 'f', ln=True), L(ell(56, 36, 7, 6.4), 'mid', 'f', ln=True), L(ell(58, 52, 7, 6.4), 'mid', 'f', ln=True),
             L(ell(60, 68, 6.4, 6), 'mid', 'f', ln=True), L(ell(62, 84, 6, 6), 'mid', 'f', ln=True), L(ell(64, 98, 5.4, 5.4), 'mid', 'f', ln=True),
             L(outline([(60, 102), (64, 122, 1), (70, 102)]), 'mid', 'f', ln=True)],
}
