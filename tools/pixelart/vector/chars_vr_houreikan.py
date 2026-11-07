"""Instituto Lawcrest (vr-houreikan): el Houreikan de Inazuma Eleven: Victory Road, con los modelos 3D de
'イナズマイレブン 英雄たちのヴィクトリーロード' de la enciclopedia (busto de frente, perfil y espalda). Cada uno tiene una sola
forma en Victory Road; ninguno coge por prefijo el dibujo de otro personaje."""
from chars import CHARS, L, OUTC, ell, hexc, outline, pal, rope, strand  # noqa: F401
from heads import quad  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (30, 28, 34, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


def mirror(pts):
    return [(100 - p[0], p[1]) + tuple(p[2:]) for p in pts]


def both(pts, c='mid', z='b', sil=True, ln=False):
    return [L(outline(pts), c, z, sil, ln), L(outline(mirror(pts)), c, z, sil, ln)]


def brows(c, w=3.4, y=66):
    return [L(quad((26, y + 2), (36, y - 4), (46, y + 2)), c, 'f', False, False, w), L(quad((74, y + 2), (64, y - 4), (54, y + 2)), c, 'f', False, False, w)]


# Rufery Faire (Inazumi Sekirou, portero): pelo azul marino enorme de pinchos, con el flequillo de mechones rojo rosado en
# llamas; ojos grises y media sonrisa
PINK = hexc('#d24a5c')
CHARS['rufery-faire'] = {
    'body': 'normal', 'pal': pal('#1e2646', '#f8d4b4', iris='#6a7080', shade='#141a34', deep='#0c1022', light='#34406a'),
    'face': {'eyes': 'sharp', 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(16, 72), (20, 60), (30, 58), (42, 62), (56, 54), (70, 54), (82, 60), (84, 72)]},
    'front': [L(outline([(18, 70), (8, 60, 1), (14, 48), (2, 36, 1), (14, 28), (10, 6, 1), (26, 16), (32, -8, 1), (42, 8), (52, -12, 1), (58, 6), (70, -6, 1), (72, 12),
                         (88, 4, 1), (84, 24), (98, 32, 1), (86, 44), (94, 58, 1), (82, 70), (78, 56), (22, 56)])),
              L(outline([(58, 6), (70, -6), (72, 12), (88, 4), (84, 24), (98, 32), (86, 44), (94, 58), (82, 60), (74, 34)]), 'shade', 'b', False),
              fringe([(20, 66), (22, 50), (30, 40), (26, 28, 1), (38, 36), (44, 24, 1), (50, 36), (60, 32), (72, 38), (82, 50), (72, 48), (64, 60, 1), (56, 48), (48, 50),
                      (42, 64, 1), (38, 52), (30, 58)], PINK)],
    'side': [L(outline([(58, 58), (70, 50), (84, 48), (94, 38), (100, 22, 1), (86, 22), (84, 2, 1), (68, 8), (60, -10, 1), (48, 6), (30, -6, 1), (28, 10), (10, 6, 1), (14, 24),
                        (-2, 32, 1), (10, 42), (0, 56, 1), (12, 60), (16, 78), (30, 76), (40, 64), (50, 60)])),
             L(outline([(-2, 32), (10, 42), (0, 56), (12, 60), (16, 78), (30, 76), (40, 64), (34, 44)]), 'shade', 'b', False),
             fringe([(70, 34), (86, 30), (98, 34, 1), (92, 42), (100, 52, 1), (88, 52), (90, 62, 1), (78, 54), (70, 50)], PINK)],
    'back': [L(outline([(20, 74), (6, 62, 1), (14, 50), (0, 36, 1), (14, 28), (10, 6, 1), (26, 16), (32, -8, 1), (42, 8), (52, -12, 1), (58, 6), (70, -6, 1), (72, 12),
                        (90, 4, 1), (86, 28), (100, 36, 1), (86, 50), (94, 62, 1), (80, 74), (62, 82), (50, 94, 1), (38, 82)])),
             L(outline([(58, 6), (90, 4), (100, 36), (94, 62), (80, 74), (62, 82), (66, 40)]), 'shade', 'b', False)],
}

# Willard Headdon (Kendou Yajirou): grandullón de cara ancha; pelo verde azulado oscuro corto que baja por la frente como un
# antifaz alrededor de los ojos, con un dibujo de corazón claro en medio y un rizo hacia delante; ojos azules enfadados
BEIGE = hexc('#c8b090')
CHARS['willard-headdon'] = {
    'body': 'corpulento', 'pal': pal('#1e4a52', '#f8c8a0', iris='#3a7ab0', shade='#163a40', deep='#0e2a2e', light='#2e6a72'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 99, 'nose': (50, 86, 2.4),
             'hairline': [(12, 80), (16, 66), (24, 72), (30, 64), (40, 66), (46, 64), (50, 70), (54, 64), (60, 66), (70, 64), (76, 72), (84, 66), (88, 80)],
             'face_front': outline([(12, 52), (30, 34), (50, 30), (70, 34), (88, 52), (92, 76), (86, 98), (66, 110), (50, 112), (34, 110), (14, 98), (8, 76)])},
    'front': [L(outline([(12, 74), (10, 44), (14, 24), (10, 14, 1), (22, 18), (30, 12), (50, 8), (70, 12), (78, 18), (90, 14, 1), (86, 24), (90, 44), (88, 74), (80, 60),
                         (20, 60)])),
              L(outline([(60, 10), (78, 18), (88, 40), (86, 66), (78, 44)]), 'shade', 'b', False),
              L(outline([(50, 62), (42, 54), (36, 44), (40, 38), (46, 40), (50, 48), (54, 40), (60, 38), (64, 44), (58, 54)]), BEIGE, 'b', False),
              *brows('mid', 3.8, 68)],
    'side': [L(outline([(60, 62), (70, 58), (84, 58), (88, 44), (82, 26), (66, 12), (40, 8), (18, 14), (8, 30), (6, 56), (10, 80), (26, 84), (36, 72), (44, 62)])),
             L(outline([(6, 40), (30, 44), (36, 72), (26, 84), (10, 80)]), 'shade', 'b', False),
             L(outline([(78, 22), (90, 14), (100, 20), (98, 36), (92, 28), (86, 26)])),
             L(quad((72, 70), (78, 65), (86, 68)), 'mid', 'f', False, False, 3.6)],
    'back': [L(outline([(14, 84), (12, 44), (18, 24), (15, 17, 1), (26, 18), (36, 12), (64, 12), (74, 18), (85, 17, 1), (82, 24), (88, 44), (86, 84), (50, 88)])),
             L(outline([(56, 14), (78, 22), (88, 46), (86, 84), (62, 86)]), 'shade', 'b', False)],
}

# Eames Rapport (Daitou Ryouya): tupé gris oscuro peinado hacia atrás en una ola grande; cejas gruesas onduladas, gafas negras
# redondas de pasta y ojos lilas; nariz marcada
CHARS['eames-rapport'] = {
    'body': 'delgado', 'pal': pal('#4a4a5e', '#f8d4b0', iris='#6a6a9a', shade='#363648', deep='#24242e', light='#6a6a82'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'line', 'mouth_y': 96, 'nose': (50, 87, 2.6), 'nose_side': (89, 86, 2.4),
             'hairline': [(16, 66), (20, 52), (50, 48), (80, 52), (84, 66)]},
    'front': [L(outline([(16, 62), (12, 40), (4, 22), (10, 4), (30, -6), (56, -6), (76, 2), (86, 16), (88, 36), (84, 62), (78, 50), (22, 50)])),
              L(outline([(4, 22), (10, 4), (30, -6), (52, -4), (36, 6), (20, 20), (14, 36)]), 'light', 'b', False),
              L(outline([(60, -4), (80, 6), (88, 30), (84, 56), (76, 30)]), 'shade', 'b', False),
              strand([(14, 30), (30, 10), (60, 0)], 'deep', 'b', 1.0), strand([(24, 40), (40, 20), (70, 8)], 'deep', 'b', 1.0),
              *[L(outline(p, 4), BLACK, 'f') for p in ([(24, 66), (28, 59), (36, 58), (44, 62), (46, 66), (38, 64), (30, 66)],
                                                       mirror([(24, 66), (28, 59), (36, 58), (44, 62), (46, 66), (38, 64), (30, 66)]))],
              *[L(ell(cx, 76, 8.6, 8) + [ell(cx, 76, 8.6, 8)[0]], BLACK, 'f', False, False, 2.6) for cx in (35, 65)],
              L([(43.5, 75), (56.5, 75)], BLACK, 'f', False, False, 1.6)],
    'side': [L(outline([(58, 56), (68, 50), (80, 48), (86, 34), (96, 20), (92, 4), (70, -6), (40, -6), (20, 4), (8, 22), (6, 44), (10, 62), (20, 72), (34, 66), (44, 56)])),
             L(outline([(6, 44), (30, 46), (34, 66), (20, 72), (10, 62)]), 'shade', 'b', False),
             strand([(90, 10), (60, 2), (20, 14)], 'deep', 'b', 1.0), strand([(84, 30), (50, 18), (14, 34)], 'deep', 'b', 1.0),
             L(outline([(72, 64), (78, 59), (86, 60), (86, 64), (78, 64)], 4), BLACK, 'f'),
             L(ell(82, 76, 5.6, 7.4) + [ell(82, 76, 5.6, 7.4)[0]], BLACK, 'f', False, False, 2.4), L([(76, 74), (52, 70)], BLACK, 'f', False, False, 1.8)],
    'back': [L(outline([(18, 80), (14, 50), (16, 26), (28, 10), (50, 2), (72, 8), (86, 20), (92, 18), (92, 30), (86, 50), (82, 80), (50, 86)])),
             L(outline([(56, 6), (80, 14), (88, 46), (82, 80), (62, 84)]), 'shade', 'b', False),
             strand([(30, 14), (50, 10), (80, 16)], 'deep', 'b', 1.0)],
}

# Gusto Reitonly (Tadamichi Fuuki): pelo verde oliva con un flequillo grande de lado, puntas abiertas hacia fuera abajo y un
# mechón rubio debajo del flequillo; orejas, ojos verdes grisáceos y sonrisa
BLOND = hexc('#e8e4a0')
CHARS['gusto-reitonly'] = {
    'body': 'normal', 'pal': pal('#4a5a22', '#fde0cc', iris='#7a9a5a', shade='#36441a', deep='#243010', light='#6a7a3a'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(16, 84), (20, 62), (50, 58), (80, 62), (84, 84)]},
    'front': [L(outline([(16, 84), (2, 82, 1), (10, 60), (14, 36), (28, 18), (50, 10), (72, 18), (86, 36), (90, 60), (98, 82, 1), (84, 84), (80, 64), (20, 64)])),
              L(outline([(60, 12), (80, 24), (88, 50), (96, 80), (84, 72), (80, 44)]), 'shade', 'b', False),
              L(outline([(54, 40), (66, 44), (68, 64), (58, 62)]), BLOND, 'f'),
              fringe([(18, 72), (20, 50), (32, 36), (50, 30), (70, 34), (82, 46), (84, 66), (76, 56), (64, 48), (56, 62, 1), (50, 50), (40, 56), (30, 68, 1), (26, 58)]),
              *brows('mid', 2.6, 68)],
    'side': [L(outline([(58, 64), (66, 56), (82, 58), (88, 46), (84, 26), (66, 12), (40, 8), (18, 16), (6, 36), (4, 60), (-6, 82, 1), (12, 76), (26, 82), (36, 72),
                        (46, 64)])),
             L(outline([(4, 50), (30, 52), (36, 72), (26, 82), (12, 76), (-6, 82)]), 'shade', 'b', False),
             L(outline([(70, 50), (84, 50), (86, 64), (76, 62)]), BLOND, 'b'),
             fringe([(64, 20), (84, 28), (92, 44), (90, 58, 1), (82, 48), (72, 44)])],
    'back': [L(outline([(16, 86), (2, 84, 1), (10, 62), (14, 36), (28, 16), (50, 10), (72, 16), (86, 36), (90, 62), (98, 84, 1), (84, 86), (62, 82), (50, 90, 1),
                        (38, 82)])),
             L(outline([(54, 12), (78, 22), (90, 62), (98, 84), (84, 86), (62, 82)]), 'shade', 'b', False)],
}

# Normon Peeveton (Igari Tetsuta): cresta de pinchos gris lavanda sobre los lados morado oscuro; orejas grandes, ojos azules
# enfadados, nariz grande y los dientes apretados
DARKP = hexc('#3a3048')
CHARS['normon-peeveton'] = {
    'body': 'bajito', 'pal': pal('#b8b0cc', '#f8d0a8', iris='#5a5ab0', shade='#948aa8', deep='#706888', light='#d6d0e4'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'big_ears': 2, 'nose': (50, 86, 3.0),
             'hairline': [(14, 74), (18, 58), (30, 56), (44, 54), (50, 62), (56, 54), (70, 56), (82, 58), (86, 74)]},
    'front': [L(outline([(16, 72), (6, 62, 1), (14, 52), (14, 30), (86, 30), (86, 52), (94, 62, 1), (84, 72), (80, 58), (20, 58)]), DARKP),
              L(outline([(26, 56), (22, 30), (26, 4, 1), (36, 18), (44, -2, 1), (52, 14), (62, -4, 1), (66, 16), (76, 6, 1), (76, 32), (72, 56), (56, 52), (50, 62, 1),
                         (44, 52)])),
              L(outline([(52, 14), (62, -4), (66, 16), (76, 6), (76, 32), (72, 54), (62, 40)]), 'shade', 'b', False),
              L(outline([(46, 46), (54, 46), (50, 52)]), hexc('#a87a6a'), 'b', False)],
    'side': [L(outline([(14, 40), (42, 46), (50, 58), (40, 78), (20, 84), (8, 66)]), DARKP),
             L(outline([(56, 54), (68, 48), (82, 48), (90, 36), (96, 18, 1), (82, 20), (78, 2, 1), (64, 12), (56, -4, 1), (46, 12), (30, 16), (18, 26), (14, 42), (30, 46),
                        (46, 50)])),
             L(outline([(14, 42), (18, 26), (36, 28), (46, 50), (30, 46)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 70), (4, 60, 1), (14, 50), (14, 30), (30, 16), (70, 16), (86, 30), (86, 50), (96, 60, 1), (86, 70), (70, 86), (50, 90), (30, 86)]), DARKP),
             L(outline([(26, 34), (30, 10), (40, 18), (50, 0, 1), (60, 18), (70, 10), (74, 34), (50, 52)])),
             L(outline([(40, 32), (50, 22), (60, 32), (50, 44)]), 'deep', 'b', False)],
}

# Prudence Witt (Kureno Hanka): melena granate oscura, larga y lisa hasta los hombros, con raya al lado y dos horquillas
# blancas; ojos verdes con pestañas
CHARS['prudence-witt'] = {
    'body': 'chica', 'pal': pal('#8a1626', '#fde4d4', iris='#2a9a8a', shade='#6a0e1c', deep='#4e0814', light='#aa2a3a'),
    'face': {'eyes': 'normal', 'mouth': 'line', 'mouth_y': 96,
             'hairline': [(18, 92), (20, 58), (36, 50), (50, 44), (62, 50), (76, 58), (82, 92)]},
    'front': [L(outline([(12, 112), (8, 70), (14, 36), (28, 16), (50, 10), (72, 16), (86, 36), (92, 70), (88, 112), (76, 110), (74, 76), (26, 76), (24, 110)])),
              L(outline([(56, 12), (78, 22), (90, 60), (88, 110), (78, 108), (80, 60)]), 'shade', 'b', False),
              strand([(44, 12), (30, 30)], 'deep', 'b', 0.9),
              L([(25, 60), (34, 55)], WHITE, 'f', False, False, 1.6), L([(75, 60), (66, 55)], WHITE, 'f', False, False, 1.6)],
    'side': [L(outline([(56, 104), (62, 80), (70, 60), (82, 54), (88, 40), (82, 22), (64, 10), (40, 8), (18, 18), (6, 40), (4, 70), (0, 96), (-8, 110, 1), (20, 108),
                        (40, 106)])),
             L(outline([(4, 50), (34, 54), (50, 100), (40, 106), (20, 108), (-8, 110), (0, 96)]), 'shade', 'b', False),
             L([(70, 58), (78, 54)], WHITE, 'f', False, False, 1.6)],
    'back': [L(outline([(10, 112), (8, 70), (14, 36), (28, 16), (50, 10), (72, 16), (86, 36), (92, 70), (90, 112), (50, 114)])),
             L(outline([(56, 12), (78, 22), (92, 70), (90, 112), (62, 114)]), 'shade', 'b', False), strand([(50, 12), (50, 112)], 'deep', 'b', 0.8)],
}

# Dion Arbiter (Okitehara Zan): melena negra hasta los hombros con las puntas abiertas, dos mechones plateados que le enmarcan
# la cara y dos rizos negros arriba como cuernos; ojos azul grisáceo afilados
SILVER = hexc('#c8d2da')
_da_lock = [(48, 46), (36, 52), (26, 64), (22, 92), (30, 82), (32, 64), (44, 58)]
_da_horn = [(28, 14), (24, 0), (14, -6, 1), (30, -2), (36, 10)]
CHARS['dion-arbiter'] = {
    'body': 'delgado', 'pal': pal('#1e1e2a', '#fde0cc', iris='#6a8aa0', shade='#14141e', deep='#0a0a12', light='#3a3a4e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 96,
             'hairline': [(16, 80), (20, 58), (36, 50), (50, 48), (64, 50), (80, 58), (84, 80)]},
    'front': [L(outline([(14, 64), (2, 100, 1), (14, 96), (8, 112, 1), (24, 98), (30, 80), (70, 80), (76, 98), (92, 112, 1), (86, 96), (98, 100, 1), (86, 64)])),
              L(outline([(14, 70), (12, 40), (20, 20), (36, 10), (50, 8), (64, 10), (80, 20), (88, 40), (86, 70), (78, 56), (22, 56)])),
              *both(_da_horn), *both(_da_lock, SILVER, 'f'), L(outline([(46, 44), (54, 44), (50, 52, 1)]), 'mid', 'f')],
    'side': [L(outline([(26, 60), (2, 96, 1), (14, 94), (6, 112, 1), (26, 98), (34, 108, 1), (40, 86), (50, 70)])),
             L(outline([(56, 58), (66, 50), (82, 50), (88, 36), (82, 20), (62, 8), (36, 8), (16, 18), (6, 38), (8, 62), (30, 64), (46, 58)])),
             L(outline([(30, 12), (22, -2), (12, -6, 1), (28, -2), (36, 10)])),
             fringe([(66, 50), (78, 50), (76, 70), (68, 98, 1), (64, 72)], SILVER)],
    'back': [L(outline([(14, 50), (4, 100, 1), (16, 98), (10, 112, 1), (30, 104), (40, 112, 1), (50, 104), (60, 112, 1), (70, 104), (90, 112, 1), (84, 98), (96, 100, 1),
                        (86, 50)])),
             L(outline([(14, 60), (12, 40), (20, 20), (36, 10), (64, 10), (80, 20), (88, 40), (86, 60), (50, 66)])),
             *both(_da_horn), L(outline([(56, 12), (80, 22), (88, 50), (86, 98), (62, 104)]), 'shade', 'b', False)],
}

# Cordelia Collison (Ritsunomori Komachi): pelo caqui enorme en champiñón con raya en medio y flequillo recto, y dos coletas
# bajas atadas con gomas negras; cejas claras gruesas y ojos oscuros de pestañas largas
_cc_tail = [(19, 102), (28, 102), (30, 114), (24, 120, 1), (18, 114)]
CHARS['cordelia-collison'] = {
    'body': 'chica', 'pal': pal('#c2a272', '#fde4d4', iris='#4a3020', shade='#9a7a52', deep='#7a5c3a', light='#dcc092'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'line', 'mouth_y': 96, 'ears': False, 'nose': (50, 86, 1.8),
             'hairline': [(18, 82), (20, 64), (50, 62), (80, 64), (82, 82)]},
    'front': [L(outline([(0, 90), (-2, 70), (6, 46), (20, 24), (50, 14), (80, 24), (94, 46), (102, 70), (100, 90), (82, 90), (80, 72), (20, 72), (18, 90)])),
              L(outline([(-2, 74), (18, 80), (18, 90), (0, 90)]), 'shade', 'b', False), L(outline([(102, 74), (82, 80), (82, 90), (100, 90)]), 'shade', 'b', False),
              strand([(50, 14), (50, 36)], 'deep', 'b', 1.0),
              *both(_cc_tail, 'mid', 'f'), L(ell(24, 100, 4.4, 3), BLACK, 'f'), L(ell(76, 100, 4.4, 3), BLACK, 'f'),
              *brows('light', 3.2, 67)],
    'side': [L(outline([(36, 98), (46, 98), (48, 112), (42, 118, 1), (36, 110)])), L(ell(42, 96, 4.4, 3), BLACK, 'b'),
             L(outline([(62, 76), (68, 64), (84, 62), (92, 48), (86, 26), (66, 10), (40, 6), (16, 16), (2, 40), (-4, 70), (0, 86), (24, 92), (50, 92), (58, 84)])),
             L(outline([(0, 60), (40, 70), (58, 84), (50, 92), (24, 92), (0, 86)]), 'shade', 'b', False),
             L(quad((72, 66), (78, 62), (86, 64)), 'light', 'f', False, False, 3.0)],
    'back': [*both([(30, 92), (38, 92), (38, 108), (34, 116, 1), (28, 108)]), L(ell(34, 92, 4.4, 3), BLACK, 'b'), L(ell(66, 92, 4.4, 3), BLACK, 'b'),
             L(outline([(0, 88), (-2, 68), (6, 44), (20, 22), (50, 12), (80, 22), (94, 44), (102, 68), (100, 88), (70, 92), (50, 96), (30, 92)])),
             L(outline([(0, 64), (50, 56), (100, 64), (100, 88), (70, 92), (50, 96), (30, 92), (0, 88)]), 'shade', 'b', False),
             strand([(50, 12), (50, 94)], 'deep', 'b', 1.0)],
}

# Norwin Naeve (Koute Norimitsu): pelo castaño grisáceo como un casco, con flequillo recto hasta las cejas, dos picos hacia
# arriba a los lados de la cabeza y pinchitos junto a las orejas; orejas grandes y ojos verde azulado
CHARS['norwin-naeve'] = {
    'body': 'normal', 'pal': pal('#8a7462', '#fde0cc', iris='#2a9a9a', shade='#6a5848', deep='#4e4034', light='#a89282'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'big_ears': 2, 'ear_out': 1,
             'hairline': [(16, 76), (18, 66), (50, 68), (82, 66), (84, 76)]},
    'front': [L(outline([(16, 80), (8, 88, 1), (14, 72), (10, 50), (4, 28), (-6, 4, 1), (16, 18), (50, 10), (84, 18), (106, 4, 1), (96, 28), (90, 50), (86, 72),
                         (92, 88, 1), (84, 80), (80, 66), (20, 66)])),
              L(outline([(60, 12), (84, 18), (106, 4), (96, 28), (90, 50), (86, 66), (78, 40)]), 'shade', 'b', False),
              *[strand([(x, 50), (x, 66)], 'deep', 'b', 0.8) for x in (30, 42, 58, 70)]],
    'side': [L(outline([(58, 66), (66, 58), (84, 58), (92, 64, 1), (90, 46), (84, 26), (66, 12), (40, 8), (16, 12), (-6, 0, 1), (8, 22), (4, 44), (6, 64), (14, 80),
                        (8, 90, 1), (24, 84), (36, 74), (46, 66)])),
             L(outline([(4, 44), (30, 48), (36, 74), (24, 84), (14, 80)]), 'shade', 'b', False)],
    'back': [L(outline([(18, 80), (12, 54), (6, 30), (-8, 4, 1), (16, 16), (50, 10), (84, 16), (108, 4, 1), (94, 30), (88, 54), (82, 80), (66, 88), (60, 96, 1), (50, 88),
                        (40, 96, 1), (34, 88)])),
             L(outline([(56, 12), (84, 16), (108, 4), (94, 30), (88, 54), (82, 80), (62, 86)]), 'shade', 'b', False)],
}

# Faust Fennrick (Fushimi Shishi): tupé morado oscuro abultado, con un rizo en la frente y patillas largas curvas que le tapan
# las orejas; ojos amarillos con raya y sonrisa pícara de dientes
CHARS['faust-fennrick'] = {
    'body': 'delgado', 'pal': pal('#3e3462', '#fde0cc', iris='#d8a020', shade='#2c2448', deep='#1c1632', light='#5a4e84'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'ears': False,
             'hairline': [(18, 86), (20, 62), (30, 56), (40, 60), (50, 56), (60, 58), (70, 56), (80, 62), (82, 86)]},
    'front': [L(outline([(18, 92), (10, 70), (6, 40), (16, 18), (36, 8), (50, 12), (64, 6), (84, 16), (94, 40), (90, 70), (82, 92), (78, 74), (22, 74)])),
              L(outline([(60, 8), (84, 18), (94, 42), (88, 70), (80, 44)]), 'shade', 'b', False),
              L(outline([(20, 30), (36, 14), (48, 16), (30, 30)]), 'light', 'b', False),
              fringe([(30, 58), (34, 66, 1), (38, 60), (36, 56)]),
              fringe([(18, 66), (24, 62), (26, 86), (22, 94, 1), (18, 86)]), fringe([(82, 66), (76, 62), (74, 86), (78, 94, 1), (82, 86)])],
    'side': [L(outline([(58, 60), (66, 54), (82, 54), (92, 44), (96, 28), (88, 12), (66, 2), (40, 4), (18, 14), (6, 34), (8, 60), (20, 76), (36, 72), (46, 62)])),
             L(outline([(6, 40), (30, 44), (36, 72), (20, 76), (8, 60)]), 'shade', 'b', False),
             fringe([(52, 60), (62, 60), (62, 84), (58, 94, 1), (52, 80)])],
    'back': [L(outline([(20, 82), (10, 60), (8, 36), (20, 16), (50, 8), (80, 16), (92, 36), (90, 60), (80, 82), (50, 86)])),
             L(outline([(56, 10), (80, 18), (92, 40), (86, 70), (80, 82), (62, 84), (60, 50)]), 'shade', 'b', False)],
}

# Adamas Quarell (Shimozuma Norimasa): pelo granate oscuro de pinchos revueltos; cejas rojas gruesas, ojos azules y ceño serio
CHARS['adamas-quarell'] = {
    'body': 'normal', 'pal': pal('#7a1c18', '#fcd8b4', iris='#3a4a9a', shade='#5e1410', deep='#420c08', light='#9a3028'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'frown', 'mouth_y': 96,
             'hairline': [(16, 74), (20, 58), (36, 54), (50, 56), (64, 54), (80, 58), (84, 74)]},
    'front': [L(outline([(16, 70), (6, 62, 1), (12, 50), (2, 38, 1), (14, 30), (10, 12, 1), (26, 18), (32, 0, 1), (44, 12), (54, -4, 1), (62, 10), (74, 2, 1), (78, 18),
                         (92, 12, 1), (88, 30), (98, 38, 1), (88, 50), (94, 62, 1), (84, 70), (80, 56), (20, 56)])),
              L(outline([(62, 10), (74, 2), (78, 18), (92, 12), (88, 30), (98, 38), (88, 50), (94, 62), (82, 60), (74, 34)]), 'shade', 'b', False),
              strand([(30, 24), (36, 44)], 'deep', 'b', 1.0), strand([(56, 16), (56, 44)], 'deep', 'b', 1.0),
              *brows('mid', 4.4, 67)],
    'side': [L(outline([(58, 58), (70, 52), (84, 50), (94, 40), (100, 26, 1), (86, 24), (88, 6, 1), (70, 10), (66, -6, 1), (52, 6), (34, -4, 1), (30, 12), (10, 8, 1),
                        (14, 26), (-2, 34, 1), (10, 44), (2, 58, 1), (12, 62), (16, 80), (30, 78), (40, 66), (50, 60)])),
             L(outline([(-2, 34), (10, 44), (2, 58), (12, 62), (16, 80), (30, 78), (40, 66), (34, 44)]), 'shade', 'b', False),
             L(quad((72, 68), (78, 63), (86, 66)), 'mid', 'f', False, False, 4.0)],
    'back': [L(outline([(16, 80), (4, 66, 1), (12, 52), (0, 40, 1), (14, 30), (10, 10, 1), (26, 18), (32, 0, 1), (44, 12), (54, -4, 1), (62, 10), (74, 2, 1), (78, 18),
                        (92, 10, 1), (88, 30), (100, 40, 1), (88, 52), (96, 66, 1), (84, 80), (50, 86)])),
             L(outline([(58, 8), (92, 10), (100, 40), (96, 66), (84, 80), (62, 84)]), 'shade', 'b', False)],
}

# Brie Brillante (Makabe Shiro, portera): pelo crema con un moño alto atado con una goma oscura, flequillo de lado y dos
# mechones largos que se abren hacia fuera a los lados de la cara; sombra verde en los ojos y puntitos debajo
GREENE = hexc('#2a8a5a')
_bb_lock = [(16, 56), (6, 78), (0, 98, 1), (14, 86), (24, 64)]
CHARS['brie-brillante'] = {
    'body': 'chica', 'pal': pal('#e8e2cc', '#fde4d4', iris='#4a4a6a', shade='#c4bca4', deep='#a49c84', light='#fffbec'),
    'face': {'eyes': 'normal', 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(16, 76), (20, 60), (30, 56), (40, 62), (50, 54), (58, 62), (66, 56), (80, 60), (84, 76)]},
    'front': [L(ell(50, -6, 11, 10)), L(ell(57, -15, 7, 6)), L(ell(50, 4, 8, 2.6), BLACK, 'b', False),
              *both(_bb_lock),
              L(outline([(16, 70), (12, 40), (24, 18), (50, 10), (76, 18), (88, 40), (84, 70), (78, 58), (22, 58)])),
              L(outline([(58, 12), (78, 22), (88, 44), (84, 64), (76, 40)]), 'shade', 'b', False),
              *[L(quad((cx - 7, 71), (cx, 66), (cx + 7, 71)), GREENE, 'f', False, False, 2.0) for cx in (36, 64)],
              *[L(ell(50 + s * dx, 85, 0.8, 0.8), GREENE, 'f', False) for s in (-1, 1) for dx in (12, 16)]],
    'side': [L(outline([(30, 4), (14, 30), (2, 64), (0, 92, 1), (12, 70), (22, 40), (36, 14)])),
             L(ell(36, -4, 11, 10)), L(ell(28, -12, 7, 6)), L(ell(38, 6, 3, 7), BLACK, 'b', False),
             L(outline([(58, 58), (66, 50), (82, 50), (88, 36), (82, 20), (62, 8), (36, 8), (16, 18), (6, 38), (8, 60), (30, 62), (46, 58)])),
             fringe([(60, 52), (70, 52), (72, 70), (68, 96, 1), (62, 72)]),
             L(quad((74, 71), (79, 67), (86, 70)), GREENE, 'f', False, False, 2.0)],
    'back': [*both([(30, 20), (16, 50), (8, 84), (10, 100, 1), (20, 80), (30, 50), (40, 24)]),
             L(outline([(16, 70), (12, 40), (24, 18), (50, 10), (76, 18), (88, 40), (84, 70), (50, 80)])),
             L(outline([(56, 14), (78, 22), (88, 46), (84, 70), (60, 78)]), 'shade', 'b', False),
             L(ell(50, -6, 11, 10)), L(ell(57, -15, 7, 6)), L(ell(50, 4, 8, 2.6), BLACK, 'b', False)],
}

# Kieran Knavenly (Kiriki Sousui): media melena castaño violáceo ondulada hasta la mandíbula, con raya en medio y flequillo en
# picos cortos; ojos grises afilados con puntitos debajo y media sonrisa
CHARS['kieran-knavenly'] = {
    'body': 'delgado', 'pal': pal('#5a3a42', '#fde0cc', iris='#7a7a8a', shade='#442a32', deep='#301c22', light='#7a5a62'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(18, 86), (20, 62), (28, 66), (34, 60), (40, 66), (46, 60), (54, 66), (60, 60), (66, 66), (72, 60), (80, 62), (82, 86)]},
    'front': [L(outline([(10, 98), (6, 84), (12, 76), (8, 60), (16, 34), (30, 16), (50, 10), (70, 16), (84, 34), (92, 60), (88, 76), (94, 84), (90, 98), (80, 96), (78, 74),
                         (22, 74), (20, 96)])),
              L(outline([(56, 12), (78, 22), (92, 60), (88, 76), (94, 84), (90, 98), (80, 96), (80, 60)]), 'shade', 'b', False),
              strand([(50, 10), (50, 30)], 'deep', 'b', 1.0),
              *[L(ell(50 + s * dx, 85, 0.7, 0.7), OUTC, 'f', False) for s in (-1, 1) for dx in (11, 14, 17)]],
    'side': [L(outline([(58, 64), (66, 56), (82, 56), (88, 42), (82, 22), (62, 8), (36, 8), (16, 18), (6, 40), (8, 60), (0, 74), (6, 92), (20, 96), (34, 90), (46, 96),
                        (50, 80)])),
             L(outline([(8, 56), (36, 60), (50, 80), (46, 96), (34, 90), (20, 96), (6, 92), (0, 74)]), 'shade', 'b', False)],
    'back': [L(outline([(8, 96), (4, 82), (10, 72), (8, 56), (16, 32), (30, 14), (50, 8), (70, 14), (84, 32), (92, 56), (90, 72), (96, 82), (92, 96), (76, 92), (62, 98),
                        (50, 92), (38, 98), (24, 92)])),
             L(outline([(6, 70), (50, 62), (94, 70), (96, 82), (92, 96), (76, 92), (62, 98), (50, 92), (38, 98), (24, 92), (8, 96), (4, 82)]), 'shade', 'b', False)],
}

# Alzen Wasruff (Nigoriya Naki): media melena rubia redonda con un flequillo largo que le tapa un ojo; el otro, rojo
CHARS['alzen-wasruff'] = {
    'body': 'delgado', 'pal': pal('#e2c696', '#fde4d4', iris='#c02424', shade='#c09a70', deep='#9a7a54', light='#f8e2b8'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'ears': False,
             'hairline': [(18, 84), (20, 60), (50, 54), (80, 60), (82, 84)]},
    'front': [L(outline([(8, 96), (6, 70), (12, 40), (26, 18), (50, 10), (74, 18), (88, 40), (94, 70), (92, 96), (80, 92), (78, 76), (22, 76), (20, 92)])),
              L(outline([(4, 76), (20, 80), (20, 92), (8, 96)]), 'shade', 'b', False), L(outline([(96, 76), (80, 80), (80, 92), (92, 96)]), 'shade', 'b', False),
              fringe([(16, 88), (16, 56), (30, 36), (50, 30), (70, 36), (82, 50), (84, 64), (72, 56), (62, 52), (56, 68), (50, 86), (40, 92), (26, 92)]),
              strand([(40, 40), (34, 70)], 'shade', 'f', 1.0), strand([(56, 40), (48, 70)], 'shade', 'f', 1.0)],
    'side': [L(outline([(60, 64), (70, 56), (84, 56), (90, 42), (84, 22), (64, 8), (38, 6), (16, 16), (4, 40), (2, 66), (6, 90), (24, 96), (44, 94), (56, 86)])),
             L(outline([(2, 60), (30, 62), (56, 86), (44, 94), (24, 96), (6, 90)]), 'shade', 'b', False),
             fringe([(66, 20), (86, 30), (94, 48), (92, 70, 1), (84, 56), (74, 48)])],
    'back': [L(outline([(6, 92), (4, 66), (12, 38), (26, 16), (50, 8), (74, 16), (88, 38), (96, 66), (94, 92), (70, 98), (50, 100), (30, 98)])),
             L(outline([(4, 60), (40, 50), (96, 56), (94, 92), (70, 98), (50, 100), (30, 98), (6, 92)]), 'shade', 'b', False)],
}

# Fabricius Cator (Asagi Aruto): pelo verde azulado en tazón con flequillo recto, un mechón de punta arriba y dos mechones
# largos finos junto a la cara; cejas gruesas, ojos azules y sonrisa
CHARS['fabricius-cator'] = {
    'body': 'bajito', 'pal': pal('#3a7a9a', '#fde0cc', iris='#3a5a9a', shade='#2c6078', deep='#1e4458', light='#5a9aba'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(16, 84), (18, 62), (30, 62), (36, 66), (42, 60), (56, 60), (62, 66), (70, 62), (82, 62), (84, 84)]},
    'front': [L(outline([(14, 90), (10, 60), (16, 34), (30, 16), (46, 10), (50, 6, 1), (54, 10), (70, 16), (84, 34), (90, 60), (86, 90), (78, 74), (22, 74)])),
              L(outline([(58, 12), (80, 24), (90, 56), (86, 86), (80, 56)]), 'shade', 'b', False),
              *both([(18, 60), (26, 62), (24, 96), (20, 110, 1), (16, 94)], 'mid', 'f'),
              *brows('mid', 3.4, 67)],
    'side': [L(outline([(58, 64), (66, 56), (82, 56), (88, 42), (82, 22), (62, 8), (36, 8), (14, 16), (2, 38), (0, 62), (6, 80), (22, 86), (40, 82), (50, 70)])),
             L(outline([(2, 50), (30, 54), (50, 70), (40, 82), (22, 86), (6, 80)]), 'shade', 'b', False),
             fringe([(56, 58), (64, 58), (64, 96), (60, 108, 1), (56, 90)])],
    'back': [*both([(18, 70), (24, 70), (24, 100), (20, 110, 1), (16, 96)]),
             L(outline([(12, 80), (6, 56), (14, 30), (30, 14), (50, 8), (70, 14), (86, 30), (94, 56), (88, 80), (60, 84), (50, 92, 1), (40, 84)])),
             L(outline([(56, 10), (78, 20), (94, 56), (88, 80), (60, 84)]), 'shade', 'b', False), strand([(50, 10), (50, 90)], 'deep', 'b', 1.0)],
}

# Recco Rectenwald (Tadashiki Hanamaru): piel tostada; pelo azul marino abultado en tres bollos (arriba y a los dos lados) y
# flequillo corto en picos; ojos grandes y sonrisa
CHARS['recco-rectenwald'] = {
    'body': 'normal', 'pal': pal('#1e3a6c', '#dc9c6c', iris='#3a4a7a', shade='#162c54', deep='#0e1e3c', light='#34568e'),
    'face': {'eyes': 'big', 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(14, 72), (18, 60), (30, 56), (40, 62), (50, 56), (60, 62), (70, 56), (82, 60), (86, 72)]},
    'front': [L(ell(16, 46, 15, 20)), L(ell(84, 46, 15, 20)), L(ell(50, 28, 32, 24)),
              L(outline([(16, 64), (14, 40), (86, 40), (84, 64), (50, 60)])),
              L(ell(88, 48, 10, 15), 'shade', 'b', False), L(ell(60, 30, 18, 14), 'shade', 'b', False), L(ell(44, 18, 16, 9), 'mid', 'b', False),
              L(ell(38, 14, 8, 4), 'light', 'b', False)],
    'side': [L(ell(30, 44, 26, 26)), L(ell(56, 28, 30, 22)),
             L(outline([(58, 60), (68, 52), (84, 52), (92, 44), (90, 30), (70, 20), (40, 24), (14, 40), (8, 60), (20, 72), (40, 64)])),
             L(ell(24, 52, 18, 16), 'shade', 'b', False)],
    'back': [L(ell(18, 48, 16, 20)), L(ell(82, 48, 16, 20)), L(ell(50, 30, 34, 26)),
             L(outline([(16, 66), (16, 44), (84, 44), (84, 66), (70, 80), (50, 84), (30, 80)])),
             L(outline([(14, 56), (86, 56), (84, 66), (70, 80), (50, 84), (30, 80), (16, 66)]), 'shade', 'b', False)],
}
