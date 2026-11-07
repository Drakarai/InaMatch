"""Secundaria Northbright (vr-hokuyou-gakuen): el Hokuyou de Inazuma Eleven: Victory Road, con los modelos 3D de
'イナズマイレブン 英雄たちのヴィクトリーロード' de la enciclopedia (busto de frente, perfil y espalda). Cada uno tiene una sola
forma en Victory Road; ninguno coge por prefijo el dibujo de otro personaje. El perfil de Milo Rankin viene mal encuadrado
en la enciclopedia: dibujado a partir del frente y la espalda."""
from chars import CHARS, L, OUTC, ell, hexc, outline, pal, rope, strand  # noqa: F401
from heads import quad  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (30, 28, 34, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


def mirror(pts):
    return [(100 - p[0], p[1]) + tuple(p[2:]) for p in pts]


def lids(cx_list=(36, 64), y=75, c='skin'):
    """Párpados caídos: tapan la mitad de arriba del ojo con una raya gruesa."""
    out = []
    for cx in cx_list:
        out += [L([(cx - 6.6, y - 8), (cx + 6.6, y - 8), (cx + 6.6, y - 1), (cx - 6.6, y - 1)], c, 'f', False),
                L([(cx - 6.2, y - 1), (cx + 6.2, y - 1)], OUTC, 'f', False, False, 2.4)]
    return out


# Milo Rankin (Jinnai Gohei, portero): pelo negro peinado hacia atrás hasta un moño alto abierto en abanico, con los lados
# en trenzas pegadas (rayas grises) y una melena negra que le cae por la espalda; ceño fruncido y ojos amarillentos
GREYS = hexc('#7a6c72')
_mr_side = [(18, 76), (12, 96), (16, 110, 1), (24, 96), (24, 82)]
CHARS['milo-rankin'] = {
    'body': 'corpulento', 'pal': pal('#24222a', '#d8a078', iris='#c8b46a', shade='#3a3640', deep='#141218'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 97,
             'hairline': [(16, 72), (20, 56), (36, 52), (50, 58), (64, 52), (80, 56), (84, 72)]},
    'front': [L(outline(_mr_side)), L(outline(mirror(_mr_side))),
              L(outline([(16, 70), (14, 44), (24, 24), (40, 14), (60, 14), (76, 24), (86, 44), (84, 70), (78, 56), (22, 56)])),
              *[L(quad(p0, c, p1), GREYS, 'b', False, False, 2.2) for p0, c, p1 in
                (((17, 66), (18, 42), (32, 24)), ((23, 60), (24, 42), (36, 28)), ((83, 66), (82, 42), (68, 24)), ((77, 60), (76, 42), (64, 28)))],
              L(outline([(37, 40), (36, 14), (26, 4), (16, -10, 1), (34, -4), (40, -16, 1), (50, -6), (60, -16, 1), (66, -4), (84, -10, 1), (74, 4), (64, 14),
                         (63, 40), (50, 56, 1)])),
              strand([(44, 20), (46, 44)], 'shade', 'b', 1.0), strand([(56, 20), (54, 44)], 'shade', 'b', 1.0),
              L([(40, 64), (42, 72)], OUTC, 'f', False, False, 0.9), L([(60, 64), (58, 72)], OUTC, 'f', False, False, 0.9),
              L([(30, 86), (33, 90)], OUTC, 'f', False, False, 0.9), L([(70, 86), (67, 90)], OUTC, 'f', False, False, 0.9)],
    'side': [L(outline([(14, 60), (2, 92), (6, 114, 1), (18, 102), (26, 82), (26, 64)])),
             L(outline([(58, 58), (70, 50), (84, 44), (86, 30), (76, 16), (56, 8), (30, 10), (14, 24), (8, 44), (10, 64), (20, 76), (34, 72), (42, 62)])),
             *[L(quad(p0, c, p1), GREYS, 'b', False, False, 2.2) for p0, c, p1 in
               (((14, 60), (24, 36), (60, 22)), ((20, 70), (34, 46), (72, 32)), ((30, 72), (44, 54), (80, 40)))],
             L(outline([(30, 14), (18, -10, 1), (34, -4), (42, -18, 1), (52, -4), (66, -10, 1), (58, 10)]))],
    'back': [L(outline([(16, 60), (8, 90), (10, 112), (30, 116), (50, 112), (70, 116), (90, 112), (92, 90), (84, 60)])),
             L(outline([(16, 70), (14, 40), (24, 22), (50, 14), (76, 22), (86, 40), (84, 70), (50, 76)])),
             *[L([(x, 28), (x + (x - 50) * 0.15, 110)], GREYS, 'b', False, False, 2.2) for x in (20, 28, 72, 80)],
             L(outline([(36, 26), (24, 6), (8, -10, 1), (34, -6), (42, -16, 1), (50, -8), (58, -16, 1), (66, -6), (92, -10, 1), (76, 6), (64, 26)]))],
}

# Peake Fletcher (Yagura Takajin): pelo verde de pinchos de punta hacia arriba con un pico en medio de la frente; ojos lilas
# con raya gruesa y cejas finas arqueadas, sonrisa de dientes
CHARS['peake-fletcher'] = {
    'body': 'delgado', 'pal': pal('#7aa83a', '#f8d4b4', iris='#8a78a8', shade='#5a7e2a', deep='#3a561a', light='#9ac85a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 95,
             'hairline': [(16, 70), (20, 56), (30, 50), (42, 56), (50, 64), (58, 56), (70, 50), (80, 56), (84, 70)]},
    'front': [L(outline([(18, 66), (14, 40), (12, 8, 1), (26, 20), (34, -2, 1), (42, 16), (50, -6, 1), (58, 16), (66, -2, 1), (74, 20), (88, 8, 1), (86, 40),
                         (82, 66), (76, 56), (24, 56)])),
              L(outline([(58, 16), (66, -2), (74, 20), (88, 8), (86, 40), (82, 60), (72, 36)]), 'shade', 'b', False),
              strand([(22, 34), (30, 26), (36, 34), (44, 24), (50, 32), (56, 24), (64, 34), (70, 26), (78, 34)], 'deep', 'b', 1.1),
              L(quad((26, 68), (35, 61), (45, 67)), 'deep', 'f', False, False, 2.0), L(quad((74, 68), (65, 61), (55, 67)), 'deep', 'f', False, False, 2.0)],
    'side': [L(outline([(60, 56), (70, 50), (84, 50), (92, 30), (100, 12, 1), (84, 18), (82, -6, 1), (68, 8), (56, -10, 1), (46, 8), (30, 0, 1), (28, 14), (12, 14, 1),
                        (14, 30), (8, 50), (16, 66), (30, 62), (46, 56)])),
             L(outline([(8, 50), (14, 30), (40, 36), (46, 56), (30, 62), (16, 66)]), 'shade', 'b', False),
             L(quad((72, 66), (78, 61), (86, 64)), 'deep', 'f', False, False, 2.0)],
    'back': [L(outline([(18, 82), (14, 50), (12, 8, 1), (26, 20), (34, -2, 1), (42, 16), (50, -6, 1), (58, 16), (66, -2, 1), (74, 20), (88, 8, 1), (86, 50), (82, 82),
                        (50, 86)])),
             L(outline([(42, 20), (50, 12), (58, 20), (50, 30)]), 'deep', 'b', False),
             L(outline([(58, 20), (74, 22), (86, 50), (82, 80), (60, 84)]), 'shade', 'b', False)],
}

# Sentry Scarborough (Jouhekidou Sanpei): grandullón calvo de piel oscura, con una cresta negra que sale de lo alto de la
# cabeza y se curva hacia delante en un gancho; cejas rectas gruesas, párpados caídos y dientes de conejo
CHARS['sentry-scarborough'] = {
    'body': 'corpulento', 'pal': pal('#2a2020', '#a86a50', iris='#7a9a6a', shade='#1a1414'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'buck', 'mouth_y': 97, 'hairline': False, 'big_ears': 1, 'ear_out': 3,
             'face_front': outline([(14, 52), (30, 34), (50, 30), (70, 34), (86, 52), (90, 76), (84, 98), (66, 108), (50, 110), (34, 108), (16, 98), (10, 76)])},
    'front': [L(outline([(12, 72), (12, 42), (24, 18), (50, 8), (76, 18), (88, 42), (88, 72), (50, 76)]), 'skin'),
              L(outline([(60, 12), (78, 20), (88, 44), (86, 64), (76, 40)]), 'skin_d', 'b', False),
              L(outline([(38, 34), (40, 8), (46, -8), (62, -6), (64, 0), (58, 22), (55, 40), (46, 42)])),
              L(outline([(56, -6), (62, -6), (64, 0), (58, 22), (55, 40), (52, 40)]), 'shade', 'b', False),
              *lids(y=77), L([(27, 65), (44, 64)], OUTC, 'f', False, False, 3.4), L([(73, 65), (56, 64)], OUTC, 'f', False, False, 3.4),
              L([(46, 84), (54, 84)], OUTC, 'f', False, False, 1.0), L(quad((24, 86), (30, 92), (32, 98)), OUTC, 'f', False, False, 0.9),
              L(quad((76, 86), (70, 92), (68, 98)), OUTC, 'f', False, False, 0.9)],
    'side': [L(outline([(16, 58), (22, 30), (46, 20), (40, 44), (46, 74), (30, 84)]), 'skin_d', 'b', False),
             L(outline([(36, 22), (40, -4), (72, -8), (90, -2), (98, 14, 1), (86, 10), (72, 6), (56, 8), (50, 22)])),
             L([(74, 74), (88, 75)], 'skin', 'f', False, False, 3.0), L([(75, 76), (87, 76)], OUTC, 'f', False, False, 2.0),
             L([(72, 64), (86, 65)], OUTC, 'f', False, False, 3.2)],
    'back': [L(outline([(56, 30), (80, 40), (80, 80), (62, 94), (40, 60)]), 'skin_d', 'b', False),
             L(outline([(42, 34), (44, 2), (56, 0), (60, 8), (58, 34), (50, 38)]))],
}

# Autry Rogers (Yarisaki Yuuji): piel morena; pelo azul marino ondulado y abultado, con un cordón negro fino por encima y un
# ricito en medio de la frente; ojos verdes
CHARS['autry-rogers'] = {
    'body': 'normal', 'pal': pal('#1e4a7c', '#c48a62', iris='#2aa07a', shade='#163a62', deep='#0e2a4a', light='#3a6aa4'),
    'face': {'eyes': 'normal', 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(16, 84), (20, 64), (30, 58), (40, 62), (46, 70), (50, 62), (54, 70), (60, 62), (70, 58), (80, 64), (84, 84)]},
    'front': [L(outline([(16, 96), (6, 92), (4, 78), (-2, 66), (6, 56), (2, 42), (14, 32), (14, 16), (30, 12), (40, 2), (56, 4), (66, 10), (82, 12), (86, 26), (98, 36),
                         (94, 52), (102, 62), (96, 76), (96, 90), (84, 96), (80, 80), (20, 80)])),
              L(outline([(-2, 66), (6, 56), (16, 64), (20, 84), (16, 96), (6, 92), (4, 78)]), 'shade', 'b', False),
              L(outline([(102, 62), (94, 52), (84, 64), (80, 84), (84, 96), (96, 90), (96, 76)]), 'shade', 'b', False),
              L(outline([(30, 22), (44, 12), (52, 16), (36, 30)]), 'light', 'b', False),
              L(quad((10, 62), (50, 2), (90, 62)), BLACK, 'b', False, False, 1.1),
              strand([(30, 40), (36, 56)], 'deep', 'b', 1.0), strand([(70, 40), (64, 56)], 'deep', 'b', 1.0)],
    'side': [L(outline([(60, 62), (66, 54), (80, 54), (90, 44), (98, 32), (88, 22), (84, 8), (66, 4), (50, -2), (32, 4), (16, 8), (8, 22), (-2, 32), (4, 46), (-6, 60),
                        (2, 72), (0, 88), (14, 92), (26, 98), (40, 92), (52, 96), (56, 80)])),
             L(outline([(-6, 60), (40, 58), (56, 80), (52, 96), (40, 92), (26, 98), (14, 92), (0, 88), (2, 72)]), 'shade', 'b', False),
             L(quad((44, 2), (60, 30), (60, 64)), BLACK, 'b', False, False, 1.1)],
    'back': [L(outline([(10, 98), (2, 86), (4, 72), (-4, 58), (6, 46), (2, 32), (14, 22), (20, 8), (38, 6), (50, 0), (62, 6), (80, 8), (86, 22), (98, 32), (94, 46),
                        (104, 58), (96, 72), (98, 86), (90, 98), (74, 94), (60, 100), (50, 94), (40, 100), (26, 94)])),
             L(outline([(4, 64), (50, 56), (96, 64), (96, 86), (90, 98), (74, 94), (60, 100), (50, 94), (40, 100), (26, 94), (10, 98), (2, 86)]), 'shade', 'b', False)],
}

# Bodhi Field (Tonda Mannen): calvo de piel tostada, con unas cejas enormes onduladas castaño oscuro, ojos grandes verdes y
# orejas grandes
BROWC = hexc('#3a2418')
_bf_brow = [(23, 66), (27, 58), (35, 56), (40, 54), (46, 60), (46, 66), (40, 62), (33, 62)]
CHARS['bodhi-field'] = {
    'body': 'normal', 'pal': pal('#c08262', '#c08262', iris='#2a6a4a'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'line', 'mouth_y': 96, 'hairline': False, 'big_ears': 2, 'ear_out': 2,
             'face_front': outline([(18, 52), (30, 36), (50, 32), (70, 36), (82, 52), (82, 80), (74, 94), (50, 104), (26, 94), (18, 80)])},
    'front': [L(outline([(16, 72), (14, 42), (26, 18), (50, 10), (74, 18), (86, 42), (84, 72), (50, 76)]), 'skin'),
              L(outline([(60, 14), (78, 22), (86, 44), (84, 64), (74, 40)]), 'skin_d', 'b', False),
              L(ell(42, 20, 8, 4), (232, 170, 140, 255), 'b', False),
              L(outline(_bf_brow, 4), BROWC, 'f'), L(outline(mirror(_bf_brow), 4), BROWC, 'f'),
              L([(48, 84), (51, 86)], OUTC, 'f', False, False, 0.9)],
    'side': [L(outline([(16, 58), (22, 28), (44, 20), (38, 48), (46, 76), (30, 86)]), 'skin_d', 'b', False),
             L(ell(56, 24, 7, 3.4), (232, 170, 140, 255), 'b', False),
             L(outline([(70, 64), (74, 57), (80, 56), (84, 54), (86, 60), (80, 61), (76, 62)], 4), BROWC, 'f')],
    'back': [L(outline([(54, 22), (80, 34), (82, 80), (62, 96), (52, 60)]), 'skin_d', 'b', False), L(ell(40, 26, 7, 3.4), (232, 170, 140, 255), 'b', False)],
}

# Chase Winthrop (Hohira Ayumu): pelo azul marino violáceo en tazón, con el flequillo en picos cortos; ojos grandes grises y
# sonrisa
CHARS['chase-winthrop'] = {
    'body': 'bajito', 'pal': pal('#3a3a7a', '#f8d4b4', iris='#5a5a6a', shade='#2a2a5e', deep='#1c1c44', light='#5a5aa0'),
    'face': {'eyes': 'big', 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(16, 84), (18, 64), (26, 62), (30, 68), (36, 60), (44, 64), (50, 58), (56, 64), (64, 60), (70, 66), (76, 62), (82, 64), (84, 84)]},
    'front': [L(outline([(16, 86), (12, 60), (16, 36), (30, 18), (50, 12), (70, 18), (84, 36), (88, 60), (84, 86), (78, 70), (22, 70)])),
              L(outline([(60, 14), (80, 26), (88, 50), (86, 80), (78, 50)]), 'shade', 'b', False),
              L(outline([(28, 24), (50, 16), (54, 20), (32, 30)]), 'light', 'b', False)],
    'side': [L(outline([(58, 62), (64, 56), (80, 60), (86, 52), (88, 36), (80, 20), (60, 10), (36, 10), (16, 20), (6, 40), (6, 64), (14, 82), (28, 88), (36, 76), (44, 64)])),
             L(outline([(6, 44), (30, 46), (36, 74), (28, 88), (14, 82)]), 'shade', 'b', False),
             L(outline([(40, 14), (64, 14), (66, 20), (42, 20)]), 'light', 'b', False)],
    'back': [L(outline([(16, 84), (12, 58), (16, 34), (30, 16), (50, 10), (70, 16), (84, 34), (88, 58), (84, 84), (50, 90)])),
             L(outline([(56, 14), (78, 24), (88, 56), (82, 84), (60, 88)]), 'shade', 'b', False)],
}

# Hawky Savard (Kishibe Towa): melena azul grisácea abierta como un champiñón, con un mechón que le cae entre los ojos y una
# trenza baja por detrás; ojos azules con tres puntitos debajo de cada uno
CHARS['hawky-savard'] = {
    'body': 'chica', 'pal': pal('#5a84aa', '#fde4d4', iris='#3a6a9a', shade='#44688c', deep='#30506e', light='#7aa0c4'),
    'face': {'eyes': 'normal', 'mouth': 'smile', 'mouth_y': 95, 'ears': False,
             'hairline': [(20, 86), (22, 60), (34, 58), (46, 62), (54, 74), (60, 62), (72, 60), (80, 64), (82, 86)]},
    'front': [L(outline([(-4, 96), (0, 84), (10, 70), (14, 46), (26, 22), (50, 12), (74, 22), (86, 46), (90, 70), (100, 84), (104, 96), (84, 98), (80, 86), (20, 86),
                         (16, 98)])),
              L(outline([(-4, 96), (0, 84), (10, 74), (22, 86), (16, 98)]), 'shade', 'b', False), L(outline([(104, 96), (100, 84), (90, 74), (78, 86), (84, 98)]), 'shade', 'b', False),
              L(outline([(28, 26), (48, 16), (52, 20), (32, 32)]), 'light', 'b', False),
              *[L(ell(50 + s * dx, 84 + dy, 0.8, 0.8), OUTC, 'f', False) for s in (-1, 1) for dx, dy in ((10, 0), (14, 1.5), (18, 0))]],
    'side': [L(outline([(20, 86), (12, 100), (16, 114, 1), (24, 104), (30, 90)]), 'mid', 'b', False, True),
             L(outline([(60, 66), (66, 58), (82, 58), (88, 46), (84, 24), (66, 10), (40, 6), (18, 14), (6, 36), (2, 60), (-6, 80), (-4, 94), (20, 92), (40, 96), (54, 90),
                        (58, 80)])),
             L(outline([(2, 60), (30, 62), (54, 90), (40, 96), (20, 92), (-4, 94), (-6, 80)]), 'shade', 'b', False)],
    'back': [L(outline([(44, 92), (44, 112), (50, 118, 1), (56, 112), (56, 92)]), 'mid', 'b', True, True), L(ell(50, 96, 5, 3), 'deep', 'b', ln=True),
             L(outline([(-4, 92), (2, 78), (12, 64), (16, 40), (30, 18), (50, 10), (70, 18), (84, 40), (88, 64), (98, 78), (104, 92), (80, 96), (50, 92), (20, 96)])),
             L(outline([(0, 84), (50, 72), (100, 84), (104, 92), (80, 96), (50, 92), (20, 96), (-4, 92)]), 'shade', 'b', False)],
}

# Taliesin Greenhunt (Shinkari Eito): piel oscura; pelo castaño muy oscuro rizado y abultado, con rizos que le caen por la
# frente; ojos amarillos con raya negra gruesa y sonrisa de lado
CHARS['taliesin-greenhunt'] = {
    'body': 'normal', 'pal': pal('#3a2620', '#8a5a3e', iris='#e2c840', shade='#2a1a16', deep='#1c100c', light='#5a3a30'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(16, 82), (20, 62), (28, 64), (34, 56), (42, 62), (50, 56), (58, 62), (66, 56), (72, 64), (80, 62), (84, 82)]},
    'front': [L(outline([(18, 98), (6, 96), (8, 84), (-2, 76), (6, 66), (0, 52), (10, 44), (8, 28), (22, 22), (26, 8), (42, 8), (50, 2), (62, 8), (76, 10), (80, 22), (94, 30),
                         (92, 44), (102, 54), (94, 66), (100, 78), (90, 86), (92, 98), (82, 96), (80, 80), (20, 80)])),
              L(outline([(60, 8), (80, 22), (94, 30), (92, 44), (80, 40), (70, 24)]), 'light', 'b', False),
              strand([(28, 36), (34, 50)], 'deep', 'b', 1.0), strand([(72, 36), (66, 50)], 'deep', 'b', 1.0),
              *[L(quad((cx - 7, 72), (cx, 70), (cx + 7, 73)), OUTC, 'f', False, False, 2.0) for cx in (36, 64)]],
    'side': [L(outline([(60, 62), (66, 54), (80, 54), (88, 44), (96, 34), (86, 24), (84, 10), (66, 6), (52, -2), (34, 4), (18, 8), (10, 22), (-2, 32), (4, 46), (-6, 58),
                        (2, 70), (-4, 84), (10, 90), (20, 100), (34, 92), (46, 98), (54, 84)])),
             L(outline([(-6, 58), (36, 56), (54, 84), (46, 98), (34, 92), (20, 100), (10, 90), (-4, 84), (2, 70)]), 'shade', 'b', False)],
    'back': [L(outline([(12, 96), (4, 86), (6, 74), (-4, 62), (6, 50), (2, 34), (16, 24), (22, 8), (40, 6), (50, 0), (62, 6), (80, 8), (86, 24), (98, 34), (94, 50),
                        (104, 62), (94, 74), (96, 86), (88, 96), (74, 92), (60, 100), (50, 92), (40, 100), (26, 92)])),
             L(outline([(4, 66), (50, 60), (96, 66), (96, 86), (88, 96), (74, 92), (60, 100), (50, 92), (40, 100), (26, 92), (12, 96), (4, 86)]), 'shade', 'b', False)],
}

# Ivan Mercer (Shinano Masashi): pelo azul de pinchos altos hacia arriba con un pico en la frente, y los lados y la nuca rapados
# en rojo granate; ojos verdes con sombra roja y sonrisa
REDS = hexc('#a01e32')
CHARS['ivan-mercer'] = {
    'body': 'normal', 'pal': pal('#1e64aa', '#f8d4b4', iris='#2aa070', shade='#164a82', deep='#0e3460', light='#3a8ad2'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(16, 64), (22, 52), (34, 54), (42, 58), (50, 66), (58, 58), (66, 54), (78, 52), (84, 64)]},
    'front': [L(outline([(18, 62), (14, 36), (10, 8, 1), (24, 18), (28, -8, 1), (38, 10), (46, -14, 1), (54, 6), (62, -12, 1), (68, 10), (80, -4, 1), (80, 18), (92, 10, 1),
                         (86, 36), (82, 62), (70, 52), (30, 52)])),
              L(outline([(54, 6), (62, -12), (68, 10), (80, -4), (80, 18), (92, 10), (86, 36), (82, 58), (72, 34)]), 'shade', 'b', False),
              strand([(30, 20), (36, 40)], 'deep', 'b', 1.0), strand([(50, 14), (50, 40)], 'deep', 'b', 1.0), strand([(70, 20), (64, 40)], 'deep', 'b', 1.0),
              L(outline([(18, 58), (24, 56), (22, 72), (18, 70)]), REDS, 'f', False), L(outline([(82, 58), (76, 56), (78, 72), (82, 70)]), REDS, 'f', False),
              L(quad((27, 68), (36, 64), (45, 70)), REDS, 'f', False, False, 2.0), L(quad((73, 68), (64, 64), (55, 70)), REDS, 'f', False, False, 2.0)],
    'side': [L(outline([(12, 46), (42, 52), (50, 62), (40, 80), (22, 86), (10, 72)]), REDS),
             L(outline([(58, 56), (70, 50), (84, 48), (92, 30), (98, 10, 1), (84, 14), (80, -8, 1), (68, 4), (56, -14, 1), (48, 4), (32, -6, 1), (28, 12), (14, 10, 1),
                        (14, 30), (10, 48), (30, 50), (46, 54)])),
             L(outline([(10, 48), (14, 30), (40, 34), (46, 54), (30, 50)]), 'shade', 'b', False),
             L(quad((72, 68), (78, 64), (86, 68)), REDS, 'f', False, False, 2.0)],
    'back': [L(outline([(18, 46), (82, 46), (84, 70), (72, 84), (50, 88), (28, 84), (16, 70)]), REDS),
             L(outline([(16, 60), (14, 36), (10, 8, 1), (24, 18), (28, -8, 1), (38, 10), (46, -14, 1), (54, 6), (62, -12, 1), (68, 10), (80, -4, 1), (80, 18), (92, 10, 1),
                        (86, 36), (84, 60), (50, 62)])),
             L(outline([(56, 6), (80, 0), (90, 14), (86, 58), (60, 60)]), 'shade', 'b', False)],
}

# Erdem Barath (Tomobe Jin): pelo rojo anaranjado revuelto en pinchos, con el flequillo de lado y dos mechones finos largos a
# los lados de la cara; gafas rectangulares granate y ojos castaños
CHARS['erdem-barath'] = {
    'body': 'normal', 'pal': pal('#c8481e', '#f8d4b4', iris='#5a3020', shade='#9a3616', deep='#70240e', light='#e46a3a'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'glasses': hexc('#9a1e32'), 'glasses_rect': True,
             'hairline': [(16, 76), (20, 60), (30, 56), (50, 52), (70, 52), (82, 58), (84, 76)]},
    'front': [L(outline([(16, 72), (4, 64, 1), (12, 52), (2, 40, 1), (14, 32), (12, 12, 1), (28, 20), (36, -2, 1), (44, 16), (60, 2), (76, 8), (90, 22), (106, 28, 1),
                         (90, 44), (98, 58, 1), (84, 62), (80, 56), (20, 56)])),
              L(outline([(60, 2), (76, 8), (90, 22), (106, 28), (90, 44), (98, 58), (84, 60), (76, 36)]), 'shade', 'b', False),
              fringe([(20, 60), (24, 44), (40, 32), (60, 32), (80, 40), (88, 56), (78, 52), (64, 46), (48, 46), (36, 52), (28, 64)]),
              fringe([(20, 64), (27, 64), (26, 100), (22, 110, 1), (18, 92)]), fringe([(80, 64), (73, 64), (74, 100), (78, 110, 1), (82, 92)])],
    'side': [L(outline([(58, 58), (70, 50), (84, 48), (94, 38), (98, 24, 1), (84, 22), (80, 4), (64, 4), (60, -10, 1), (48, 4), (30, 4), (14, 14), (2, 26, 1), (10, 34),
                        (2, 48, 1), (10, 54), (8, 70, 1), (22, 66), (24, 82, 1), (36, 70), (48, 60)])),
             L(outline([(2, 48), (34, 50), (36, 70), (24, 82), (22, 66), (8, 70), (10, 54)]), 'shade', 'b', False),
             fringe([(58, 56), (66, 58), (64, 100), (60, 110, 1), (56, 92)])],
    'back': [L(outline([(16, 84), (14, 70), (2, 64, 1), (12, 54), (0, 42, 1), (14, 34), (12, 12, 1), (28, 20), (36, -2, 1), (44, 16), (60, 2), (76, 8), (90, 22),
                        (106, 30, 1), (90, 42), (100, 56, 1), (86, 64), (84, 84), (60, 80), (50, 92, 1), (40, 80)])),
             L(outline([(58, 4), (90, 22), (100, 56), (86, 64), (84, 84), (60, 80)]), 'shade', 'b', False),
             L(outline([(18, 80), (24, 80), (24, 104), (20, 110, 1), (16, 96)])), L(outline([(82, 80), (76, 80), (76, 104), (80, 110, 1), (84, 96)]))],
}

# Nikas Himmelstein (Soramiya Sei): piel tostada; pelo caqui verdoso con una estrella negra en lo alto, flequillo en picos y
# la capa de debajo negra, abierta en alas hacia los lados y por detrás; ojos azules
CHARS['nikas-himmelstein'] = {
    'body': 'normal', 'pal': pal('#b4b07a', '#c48c66', iris='#3a6ab0', shade='#8e7c56', deep='#6a5a3e', light='#cecc98', under='#1e1e20'),
    'face': {'eyes': 'normal', 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(16, 76), (20, 62), (28, 68), (34, 58), (42, 66), (50, 58), (58, 66), (66, 58), (72, 68), (80, 62), (84, 76)]},
    'front': [L(outline([(16, 76), (-6, 58, 1), (10, 52), (90, 52), (106, 58, 1), (84, 76)]), 'under'),
              L(outline([(16, 66), (0, 52, 1), (12, 46), (10, 28), (24, 12), (50, 6), (76, 12), (90, 28), (88, 46), (100, 52, 1), (84, 66), (80, 58), (20, 58)])),
              L(outline([(60, 10), (80, 18), (90, 34), (88, 50), (76, 34)]), 'shade', 'b', False),
              L(outline([(50, 8), (54, 15), (64, 14), (56, 20), (58, 28), (50, 22), (42, 28), (44, 20), (36, 14), (46, 15)], 2), 'under', 'b', False)],
    'side': [L(outline([(14, 44), (40, 52), (46, 66), (34, 82), (20, 90), (-6, 70, 1), (8, 62)]), 'under'),
             L(outline([(58, 58), (68, 50), (84, 52), (90, 40), (88, 24), (74, 12), (52, 6), (30, 10), (14, 22), (4, 40), (-4, 48, 1), (12, 50), (30, 50), (46, 56)])),
             L(outline([(60, 6), (66, 10), (58, 14)], 2), 'under', 'b', False)],
    'back': [L(outline([(16, 46), (-10, 44, 1), (10, 58), (30, 74), (50, 90), (70, 74), (90, 58), (110, 44, 1), (84, 46)]), 'under'),
             L(outline([(14, 50), (0, 44, 1), (12, 38), (16, 22), (30, 10), (50, 6), (70, 10), (84, 22), (88, 38), (100, 44, 1), (86, 50), (70, 56), (60, 50), (50, 58),
                        (40, 50), (30, 56)])),
             L(outline([(52, 10), (78, 16), (88, 38), (80, 48), (60, 46)]), 'shade', 'b', False)],
}

# Hugh Pronghorn (Yasha Mitsutoshi): pelo verde menta peinado hacia atrás con raya en medio, mechones largos a los lados de la
# cara y una coleta baja por detrás; ojos azul oscuro y ceño serio
CHARS['hugh-pronghorn'] = {
    'body': 'delgado', 'pal': pal('#7ab0a0', '#fde0cc', iris='#2a3a6a', shade='#5a8a7c', deep='#3e6a5e', light='#9ccabc'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96,
             'hairline': [(16, 84), (20, 56), (34, 48), (50, 44), (66, 48), (80, 56), (84, 84)]},
    'front': [L(outline([(16, 96), (12, 60), (16, 30), (30, 14), (50, 8), (70, 14), (84, 30), (88, 60), (84, 96), (78, 70), (22, 70)])),
              L(outline([(56, 10), (76, 20), (88, 50), (84, 80), (74, 46)]), 'shade', 'b', False),
              strand([(50, 10), (50, 40)], 'deep', 'b', 1.0), strand([(40, 14), (32, 40)], 'deep', 'b', 0.8), strand([(60, 14), (68, 40)], 'deep', 'b', 0.8),
              fringe([(16, 54), (26, 52), (28, 70), (22, 102), (14, 94)]), fringe([(84, 54), (74, 52), (72, 70), (78, 102), (86, 94)])],
    'side': [L(outline([(18, 62), (4, 90), (0, 110, 1), (12, 100), (24, 76)])),
             L(outline([(58, 56), (66, 50), (82, 48), (88, 36), (82, 20), (62, 8), (36, 8), (16, 18), (6, 38), (8, 60), (18, 70), (34, 64), (46, 56)])),
             L(outline([(6, 40), (30, 44), (34, 62), (18, 70), (8, 60)]), 'shade', 'b', False),
             strand([(70, 16), (40, 24), (14, 40)], 'deep', 'b', 0.9),
             fringe([(58, 52), (66, 52), (66, 70), (60, 98), (54, 90)])],
    'back': [L(outline([(44, 80), (40, 104), (50, 116, 1), (60, 104), (56, 80)])), L(ell(50, 82, 5, 3), 'deep', 'b', ln=True),
             L(outline([(16, 72), (12, 50), (18, 28), (32, 14), (50, 8), (68, 14), (82, 28), (88, 50), (84, 72), (50, 84)])),
             L(outline([(54, 12), (76, 22), (88, 50), (82, 72), (58, 80)]), 'shade', 'b', False), strand([(50, 10), (50, 78)], 'deep', 'b', 0.9)],
}

# Everett Shipman (Sensha Susumu): pelo verde oscuro en una cúpula con un pico arriba y dos pinchos horizontales largos a los
# lados de la cabeza; cara redonda, ojos grandes castaños, cejas gruesas y morritos
CHARS['everett-shipman'] = {
    'body': 'corpulento', 'pal': pal('#1e4a40', '#f8d4b4', iris='#6a5030', shade='#163a32', deep='#0e2a24', light='#2e6a5c'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'frown', 'mouth_y': 97, 'big_ears': 1,
             'hairline': [(16, 74), (20, 60), (30, 54), (50, 52), (70, 54), (80, 60), (84, 74)],
             'face_front': outline([(16, 52), (30, 36), (50, 32), (70, 36), (84, 52), (88, 76), (80, 98), (64, 108), (50, 110), (36, 108), (20, 98), (12, 76)])},
    'front': [L(outline([(16, 74), (8, 80, 1), (12, 66), (-12, 60, 1), (12, 54), (14, 36), (28, 18), (44, 8), (50, -6, 1), (58, 8), (74, 18), (86, 36), (88, 54),
                         (112, 60, 1), (88, 66), (92, 80, 1), (84, 74), (80, 58), (20, 58)])),
              L(outline([(58, 8), (74, 18), (86, 36), (88, 54), (112, 60), (88, 66), (80, 50), (70, 28)]), 'shade', 'b', False),
              L(outline([(26, 26), (44, 14), (48, 20), (30, 32)]), 'light', 'b', False),
              L([(28, 64), (42, 63)], 'mid', 'f', False, False, 3.0), L([(72, 64), (58, 63)], 'mid', 'f', False, False, 3.0)],
    'side': [L(outline([(58, 58), (68, 52), (82, 52), (88, 40), (82, 22), (64, 10), (58, -6, 1), (46, 8), (26, 12), (12, 26), (6, 44), (-14, 50, 1), (6, 56), (8, 66),
                        (-2, 76, 1), (14, 72), (24, 80), (36, 70), (46, 60)])),
             L(outline([(6, 44), (30, 48), (36, 70), (24, 80), (14, 72), (8, 66)]), 'shade', 'b', False),
             L([(72, 64), (84, 64)], 'mid', 'f', False, False, 3.0)],
    'back': [L(outline([(16, 76), (6, 84, 1), (12, 68), (-14, 60, 1), (12, 52), (14, 34), (28, 16), (44, 8), (50, -6, 1), (56, 8), (72, 16), (86, 34), (88, 52),
                        (114, 60, 1), (88, 68), (94, 84, 1), (84, 76), (50, 84)])),
             L(outline([(56, 8), (72, 16), (86, 34), (88, 52), (114, 60), (88, 68), (94, 84), (84, 76), (62, 80)]), 'shade', 'b', False)],
}

# Armin Marshall (Mutou Gunpei, portero): piel morena; pelo rubio claro corto de punta hacia arriba, con mechones que le caen
# por la frente y la nuca rapada; ojos rojizos, ceño fruncido y nariz grande
CHARS['armin-marshall'] = {
    'body': 'corpulento', 'pal': pal('#f0dcae', '#a8704e', iris='#a05050', shade='#d0b884', deep='#a8905e', light='#fff4d8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'nose': (50, 86, 3.6), 'nose_side': (89, 85, 2.8),
             'hairline': [(16, 62), (22, 50), (50, 48), (78, 50), (84, 62)]},
    'front': [L(outline([(16, 60), (14, 36), (18, 14), (30, 0, 1), (36, 12), (46, -6, 1), (52, 10), (60, -4, 1), (66, 12), (76, 4, 1), (80, 20), (86, 36), (84, 60),
                         (76, 48), (24, 48)])),
              L(outline([(60, -2), (66, 12), (76, 4), (80, 20), (86, 36), (84, 56), (74, 34)]), 'shade', 'b', False),
              fringe([(28, 54), (34, 44), (50, 40), (66, 44), (72, 54), (62, 50), (56, 62, 1), (50, 50), (44, 62, 1), (40, 50)])],
    'side': [L(outline([(60, 52), (72, 46), (86, 46), (92, 30), (90, 16), (80, 4), (72, -2, 1), (62, 6), (52, -6, 1), (44, 8), (30, 6), (20, 16), (16, 30), (30, 36),
                        (46, 44)])),
             L(outline([(16, 30), (30, 20), (40, 36), (30, 36)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 44), (16, 26), (26, 8), (34, -2, 1), (42, 8), (50, -6, 1), (58, 8), (66, -2, 1), (74, 8), (84, 26), (84, 44), (70, 50), (50, 46), (30, 50)])),
             L(outline([(56, 6), (74, 10), (84, 30), (82, 44), (66, 46)]), 'shade', 'b', False),
             L(outline([(20, 56), (50, 52), (80, 56), (80, 76), (62, 92), (38, 92), (20, 76)]), 'skin_d', 'b', False)],
}

# Conley Quiver (Sanbonya Motonari): pelo azul marino casi negro en champiñón, con el flequillo en picos y el borde de abajo
# recto por encima de las orejas; ojos grises y sonrisa
CHARS['conley-quiver'] = {
    'body': 'normal', 'pal': pal('#1e2452', '#f8d4b4', iris='#6a6478', shade='#161a3e', deep='#0e122c', light='#3a4278'),
    'face': {'eyes': 'big', 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(16, 80), (18, 62), (26, 60), (30, 66), (36, 58), (44, 64), (50, 56), (56, 64), (64, 58), (70, 66), (74, 60), (82, 62), (84, 80)]},
    'front': [L(outline([(4, 82), (6, 64), (14, 40), (28, 20), (50, 12), (72, 20), (86, 40), (94, 64), (96, 82), (84, 84), (80, 74), (20, 74), (16, 84)])),
              L(outline([(60, 14), (80, 26), (92, 56), (94, 80), (84, 82), (82, 56)]), 'shade', 'b', False),
              L(outline([(26, 26), (50, 16), (54, 20), (30, 32)]), 'light', 'b', False)],
    'side': [
             L(outline([(60, 60), (68, 54), (86, 58), (94, 44), (86, 22), (64, 8), (36, 8), (14, 20), (2, 42), (-4, 66), (0, 76), (20, 74), (36, 72), (46, 66)])),
             L(outline([(2, 46), (30, 50), (36, 72), (20, 74), (0, 76)]), 'shade', 'b', False)],
    'back': [L(outline([(30, 76), (34, 94), (50, 98), (66, 94), (70, 76)])),
             L(outline([(2, 80), (6, 60), (14, 36), (28, 16), (50, 8), (72, 16), (86, 36), (94, 60), (98, 80), (70, 78), (50, 80), (30, 78)])),
             L(outline([(56, 10), (80, 22), (94, 56), (98, 80), (72, 78)]), 'shade', 'b', False)],
}

# Denzel Harvest (Taihou Ryuusuke): pelo morado largo y liso hasta los hombros, con un flequillo espeso que le tapa los ojos;
# solo se le ve la sonrisa
CHARS['denzel-harvest'] = {
    'body': 'delgado', 'pal': pal('#6a3a8c', '#f8d4b4', shade='#4e2a6c', deep='#381c50', light='#8a5aac'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'ears': False,
             'hairline': [(16, 92), (18, 84), (50, 86), (82, 84), (84, 92)]},
    'front': [L(outline([(14, 110), (10, 70), (14, 36), (28, 16), (50, 10), (72, 16), (86, 36), (90, 70), (86, 110), (76, 106), (72, 80), (28, 80), (24, 106)])),
              L(outline([(58, 12), (78, 22), (90, 60), (86, 108), (76, 104), (78, 60)]), 'shade', 'b', False),
              *[strand([(x, 20), (x + (x - 50) * 0.1, 80)], 'deep', 'b', 0.9) for x in (30, 42, 58, 70)]],
    'side': [L(outline([(54, 104), (60, 86), (70, 86), (80, 88), (88, 84), (90, 60), (86, 30), (68, 12), (40, 8), (18, 18), (6, 40), (4, 70), (8, 100), (22, 108), (40, 104)])),
             L(outline([(6, 50), (34, 54), (50, 100), (40, 104), (22, 108), (8, 100)]), 'shade', 'b', False),
             *[strand(p, 'deep', 'b', 0.9) for p in ([(40, 14), (30, 60), (28, 100)], [(62, 14), (56, 60), (52, 100)])]],
    'back': [L(outline([(10, 104), (8, 70), (14, 36), (28, 16), (50, 10), (72, 16), (86, 36), (92, 70), (90, 104), (70, 108), (50, 100), (30, 108)])),
             L(outline([(56, 14), (78, 24), (90, 60), (90, 104), (70, 108), (60, 60)]), 'shade', 'b', False),
             *[strand([(x, 24), (x + (x - 50) * 0.1, 102)], 'deep', 'b', 0.9) for x in (28, 40, 60, 72)]],
}
