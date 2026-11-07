"""Instituto Visión Noble (vr-ijinmei-bundou): el Ijinmei Bundou de Inazuma Eleven: Victory Road, con los modelos 3D de
'イナズマイレブン 英雄たちのヴィクトリーロード' de la enciclopedia (busto de frente, perfil y espalda). Cada uno tiene una sola
forma en Victory Road; ninguno coge por prefijo el dibujo de otro personaje."""
from chars import CHARS, L, OUTC, ell, hexc, outline, pal, rope, strand  # noqa: F401
from heads import quad  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (30, 28, 34, 255)
BLUSH = (246, 160, 150, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


def mirror(pts):
    return [(100 - p[0], p[1]) + tuple(p[2:]) for p in pts]


def both(pts, c='mid', z='b', sil=True, ln=False):
    return [L(outline(pts), c, z, sil, ln), L(outline(mirror(pts)), c, z, sil, ln)]


def brows(c, w=3.4, y=66):
    return [L(quad((26, y + 2), (36, y - 4), (46, y + 2)), c, 'f', False, False, w), L(quad((74, y + 2), (64, y - 4), (54, y + 2)), c, 'f', False, False, w)]


def ring(cx, cy, rx, ry, c, w):
    e = ell(cx, cy, rx, ry)
    return L(e + [e[0]], c, 'f', False, False, w)


def dots(y=86, dx=(16, 20), c=(170, 110, 80, 255), r=0.7):
    out = []
    for s in (-1, 1):
        for i, x in enumerate(dx):
            out.append(L(ell(50 + s * x, y + (i % 2) * 1.6, r, r), c, 'f', False))
    return out


# Chat Baltauk (Nitobe Denzou, portero): grandullón con el pelo azul peinado hacia atrás en surcos, cejas azules gruesas,
# gafas redondas de cristal blanco que le tapan los ojos y una sonrisa ancha
LENSW = (230, 236, 242, 255)
CHARS['chat-baltauk'] = {
    'body': 'corpulento', 'pal': pal('#3a8ac2', '#f8d0b0', shade='#2c6c9a', deep='#1e4e72', light='#5aa8dc'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'big_ears': 1,
             'hairline': [(16, 64), (20, 50), (34, 46), (50, 48), (66, 46), (80, 50), (84, 64)]},
    'front': [L(outline([(16, 62), (14, 34), (18, 14), (30, 4), (50, 0), (70, 4), (82, 14), (86, 34), (84, 62), (78, 48), (22, 48)])),
              L(outline([(60, 2), (80, 12), (86, 36), (84, 58), (76, 30)]), 'shade', 'b', False),
              *[strand([(x, 4), (x + (x - 50) * 0.2, 44)], 'deep', 'b', 1.0) for x in (30, 40, 50, 60, 70)],
              *[L(outline(p, 4), 'deep', 'f') for p in ([(26, 66), (30, 58), (38, 58), (44, 62), (46, 66), (40, 63), (32, 64)],
                                                        mirror([(26, 66), (30, 58), (38, 58), (44, 62), (46, 66), (40, 63), (32, 64)]))],
              L(ell(35, 77, 9, 8), LENSW, 'f'), L(ell(65, 77, 9, 8), LENSW, 'f'), ring(35, 77, 9, 8, BLACK, 1.6), ring(65, 77, 9, 8, BLACK, 1.6),
              L([(44, 76), (56, 76)], BLACK, 'f', False, False, 1.4), L([(26, 76), (18, 74)], BLACK, 'f', False, False, 1.4), L([(74, 76), (82, 74)], BLACK, 'f', False, False, 1.4),
              L(quad((32, 91), (50, 101), (68, 91)), OUTC, 'f', False, False, 1.8)],
    'side': [L(outline([(58, 50), (70, 44), (86, 40), (94, 30), (90, 16), (70, 6), (40, 4), (16, 12), (6, 30), (8, 52), (18, 70), (32, 66), (44, 52)])),
             L(outline([(6, 34), (30, 36), (32, 66), (18, 70), (8, 52)]), 'shade', 'b', False),
             *[strand(p, 'deep', 'b', 1.0) for p in ([(88, 18), (50, 10), (14, 24)], [(92, 30), (50, 22), (8, 40)])],
             L(outline([(72, 66), (78, 60), (86, 60), (86, 66), (78, 64)], 4), 'deep', 'f'),
             L(ell(82, 77, 5.4, 7.6), LENSW, 'f'), ring(82, 77, 5.4, 7.6, BLACK, 1.6), L([(76, 76), (50, 70)], BLACK, 'f', False, False, 1.4),
             L(quad((80, 92), (85, 95), (89, 91)), OUTC, 'f', False, False, 1.4)],
    'back': [L(outline([(16, 80), (12, 50), (16, 22), (32, 8), (50, 4), (68, 8), (84, 22), (88, 50), (84, 80), (50, 82)])),
             L(outline([(56, 8), (80, 18), (88, 50), (84, 80), (62, 82)]), 'shade', 'b', False),
             L(quad((14, 36), (50, 28), (86, 36)), 'deep', 'b', False, False, 1.2), strand([(30, 50), (50, 52), (70, 50)], 'deep', 'b', 1.0)],
}

# Elric Spiech (Fukuzawa Doukichi): piel tostada; pelo castaño muy oscuro corto, ondulado y abultado arriba; cejas gruesas
# oscuras, ojos verde azulado y la boca apretada
CHARS['elric-spiech'] = {
    'body': 'normal', 'pal': pal('#3a1e1c', '#c48c64', iris='#4a8a9a', shade='#2a1412', deep='#1c0c0a', light='#5a3632'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 97,
             'hairline': [(16, 70), (20, 56), (36, 52), (50, 54), (64, 52), (80, 56), (84, 70)]},
    'front': [L(outline([(16, 66), (10, 50), (8, 34), (18, 20), (34, 10), (50, 12), (66, 8), (84, 18), (92, 34), (90, 50), (84, 66), (78, 54), (22, 54)])),
              L(outline([(60, 10), (84, 20), (92, 40), (86, 60), (76, 36)]), 'shade', 'b', False),
              strand([(34, 16), (30, 34)], 'deep', 'b', 1.0), strand([(62, 14), (68, 32)], 'deep', 'b', 1.0),
              L(quad((26, 66), (36, 61), (46, 65)), BLACK, 'f', False, False, 3.6), L(quad((74, 66), (64, 61), (54, 65)), BLACK, 'f', False, False, 3.6)],
    'side': [L(outline([(58, 56), (68, 50), (84, 50), (90, 38), (86, 22), (66, 10), (40, 8), (18, 14), (6, 30), (6, 52), (14, 70), (28, 74), (40, 62), (48, 56)])),
             L(outline([(6, 40), (30, 44), (40, 62), (28, 74), (14, 70)]), 'shade', 'b', False),
             L(quad((72, 65), (78, 61), (86, 64)), BLACK, 'f', False, False, 3.4)],
    'back': [L(outline([(18, 76), (8, 54), (8, 32), (20, 16), (50, 8), (80, 16), (92, 32), (92, 54), (82, 76), (50, 86)])),
             L(outline([(4, 50), (50, 58), (96, 50), (82, 76), (50, 86), (18, 76)]), 'shade', 'b', False)],
}

# Habib Liomont (Kitazato Gakusaburou): pelo gris oscuro revuelto en pinchos, con dos cuernos grandes de pelo arriba a los
# lados y mechones por la frente hasta los ojos; gafas redondas doradas y ojos ámbar
CHARS['habib-liomont'] = {
    'body': 'normal', 'pal': pal('#4a4442', '#f6d2b2', iris='#c09040', shade='#363230', deep='#242120', light='#6a6462'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'glasses': hexc('#b8902a'),
             'hairline': [(16, 78), (20, 62), (50, 58), (80, 62), (84, 78)]},
    'front': [L(outline([(16, 76), (4, 72, 1), (12, 60), (2, 50, 1), (12, 42), (4, 16), (0, -8, 1), (20, 10), (32, 4), (40, -2, 1), (48, 6), (62, 0, 1), (70, 8), (84, 10),
                         (100, -8, 1), (96, 16), (88, 42), (98, 50, 1), (88, 60), (96, 72, 1), (84, 76), (80, 62), (20, 62)])),
              L(outline([(62, 2), (84, 10), (100, -8), (96, 16), (88, 42), (98, 50), (88, 60), (80, 46)]), 'shade', 'b', False),
              fringe([(20, 66), (24, 50), (36, 42), (50, 40), (66, 44), (78, 52), (80, 66), (72, 58), (64, 70, 1), (58, 56), (50, 60), (44, 72, 1), (40, 58), (30, 62),
                      (26, 74, 1)])],
    'side': [L(outline([(58, 60), (68, 52), (82, 50), (92, 54, 1), (88, 42), (96, 30, 1), (84, 26), (86, 10), (72, 10), (64, -12, 1), (54, 6), (34, 2), (16, 10),
                        (4, 26), (-6, 36, 1), (6, 44), (-4, 58, 1), (8, 62), (12, 80), (28, 78), (40, 66), (50, 62)])),
             L(outline([(-6, 36), (34, 40), (40, 66), (28, 78), (12, 80), (8, 62), (-4, 58), (6, 44)]), 'shade', 'b', False)],
    'back': [L(outline([(18, 82), (4, 76, 1), (12, 62), (2, 50, 1), (12, 42), (4, 16), (0, -8, 1), (20, 8), (50, 2), (80, 8), (100, -8, 1), (96, 16), (88, 42),
                        (98, 50, 1), (88, 62), (96, 76, 1), (82, 82), (64, 84), (56, 92, 1), (44, 84), (36, 90, 1)])),
             L(outline([(56, 4), (80, 8), (100, -8), (96, 16), (88, 42), (98, 50), (88, 62), (96, 76), (82, 82), (64, 84)]), 'shade', 'b', False)],
}

# Histrion Etcher (Fujino Kamatari): pelo rojo peinado hacia atrás hasta una coleta alta con goma dorada, con mechones finos
# largos a los lados de la cara; cejas rojas gruesas, ojos de pupila negra y ceño fruncido
GOLD = hexc('#d8a83a')
CHARS['histrion-etcher'] = {
    'body': 'normal', 'pal': pal('#d03c30', '#f8d0b0', iris='#1e1e1e', shade='#a82c22', deep='#801e16', light='#e8604e'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'frown', 'mouth_y': 97,
             'hairline': [(16, 70), (20, 52), (36, 48), (46, 52), (50, 60), (54, 52), (64, 48), (80, 52), (84, 70)]},
    'front': [L(outline([(40, 16), (40, -8), (60, -8), (60, 16)])), L([(40, -4), (60, -4), (60, 0), (40, 0)], GOLD, 'b', False),
              L(outline([(16, 66), (14, 38), (24, 18), (40, 10), (60, 10), (76, 18), (86, 38), (84, 66), (78, 52), (22, 52)])),
              L(outline([(58, 12), (78, 20), (86, 42), (84, 62), (76, 36)]), 'shade', 'b', False),
              *[strand([(x, 14), (x + (x - 50) * 0.3, 46)], 'deep', 'b', 1.0) for x in (36, 50, 64)],
              *both([(18, 58), (25, 58), (25, 108), (21, 114, 1), (17, 104)], 'mid', 'f'),
              *brows('mid', 4.2, 67)],
    'side': [L(outline([(34, 10), (24, -10), (40, -14), (40, 8)])), L([(30, -6), (38, -8), (40, -4), (32, -2)], GOLD, 'b', False),
             L(outline([(24, -8), (8, 10), (0, 50), (2, 90), (8, 112, 1), (14, 92), (14, 50), (22, 16)])),
             L(outline([(58, 56), (68, 50), (82, 48), (88, 36), (82, 20), (64, 10), (40, 8), (20, 16), (8, 34), (8, 56), (20, 70), (34, 66), (46, 58)])),
             L(outline([(8, 40), (30, 44), (34, 66), (20, 70), (8, 56)]), 'shade', 'b', False),
             fringe([(56, 54), (63, 54), (63, 106), (59, 114, 1), (55, 100)]),
             L(quad((72, 66), (78, 61), (86, 64)), 'mid', 'f', False, False, 4.0)],
    'back': [L(outline([(16, 70), (14, 40), (24, 18), (40, 10), (60, 10), (76, 18), (86, 40), (84, 70), (50, 76)])),
             L(outline([(56, 12), (78, 20), (86, 44), (84, 70), (62, 74)]), 'shade', 'b', False),
             L(outline([(42, 4), (36, 40), (34, 90), (40, 114, 1), (50, 100), (60, 114, 1), (66, 90), (64, 40), (58, 4)])),
             L([(40, 8), (60, 8), (60, 13), (40, 13)], GOLD, 'b', False),
             *[strand([(x, 20), (x, 100)], 'deep', 'b', 0.9) for x in (44, 50, 56)]],
}

# Nelvin Dustrie (Shibusawa Eikou): pelo castaño liso arriba y muy abierto abajo en ondas, con la frente despejada; cara
# redonda, ojos grandes verdes, pecas y morritos
CHARS['nelvin-dustrie'] = {
    'body': 'bajito', 'pal': pal('#7a4a3a', '#fde0cc', iris='#2a8a4a', shade='#5e362a', deep='#44241c', light='#9a6a5a'),
    'face': {'eyes': 'big', 'mouth': 'frown', 'mouth_y': 96,
             'hairline': [(16, 80), (20, 56), (36, 42), (50, 38), (64, 42), (80, 56), (84, 80)]},
    'front': [L(outline([(14, 60), (16, 36), (30, 18), (50, 12), (70, 18), (84, 36), (86, 60), (100, 68), (106, 82), (98, 92), (90, 86), (82, 92), (80, 74), (20, 74), (18, 92),
                         (10, 86), (2, 92), (-6, 82), (0, 68)])),
              L(outline([(0, 70), (16, 66), (22, 92), (10, 86), (2, 92), (-6, 82)]), 'shade', 'b', False),
              L(outline([(100, 70), (84, 66), (78, 92), (90, 86), (98, 92), (106, 82)]), 'shade', 'b', False),
              *dots(87, (14, 17, 20))],
    'side': [L(outline([(60, 56), (64, 44), (76, 36), (84, 24), (70, 12), (44, 8), (20, 16), (8, 36), (6, 58), (-6, 70), (-8, 86), (4, 94), (16, 88), (28, 96), (42, 88), (52, 92),
                        (58, 78)])),
             L(outline([(4, 62), (40, 66), (58, 78), (52, 92), (42, 88), (28, 96), (16, 88), (4, 94), (-8, 86), (-6, 70)]), 'shade', 'b', False)],
    'back': [L(outline([(-4, 86), (0, 70), (14, 60), (16, 34), (30, 16), (50, 10), (70, 16), (84, 34), (86, 60), (100, 70), (104, 86), (90, 94), (76, 88), (62, 96), (50, 88),
                        (38, 96), (24, 88), (10, 94)])),
             L(outline([(54, 12), (76, 22), (86, 60), (100, 70), (104, 86), (90, 94), (76, 88), (62, 96), (50, 88), (56, 50)]), 'shade', 'b', False)],
}

# Keepie Upshire (Futatsumiya Kinjirou): piel tostada; pelo negro con un moñito arriba, un mechón de lado por la frente y una
# punta que sale hacia fuera por un lado; ojos grandes grises y sonrisa
CHARS['keepie-upshire'] = {
    'body': 'bajito', 'pal': pal('#1e1e30', '#b47c54', iris='#4a4a5a', shade='#141422', deep='#0a0a14', light='#3a3a54'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(16, 74), (20, 58), (50, 54), (80, 58), (84, 74)]},
    'front': [L(ell(50, -2, 7, 8)),
              L(outline([(16, 72), (12, 44), (22, 22), (40, 10), (60, 10), (78, 22), (88, 44), (86, 62), (96, 72), (106, 80, 1), (90, 82), (82, 72), (78, 58), (22, 58)])),
              L(outline([(58, 12), (78, 22), (88, 44), (86, 62), (76, 40)]), 'shade', 'b', False),
              fringe([(18, 62), (22, 46), (36, 36), (56, 34), (70, 40), (76, 52), (80, 70), (72, 60), (62, 50), (50, 46), (36, 50), (26, 58)]),
              *brows(BLACK, 3.2, 67)],
    'side': [L(ell(44, -2, 7, 8)), L(outline([(20, 10), (4, 4), (-6, 14, 1), (6, 16), (18, 22)])),
             L(outline([(58, 58), (68, 52), (84, 52), (90, 40), (84, 22), (64, 10), (40, 8), (20, 16), (8, 34), (8, 58), (18, 72), (34, 68), (46, 60)])),
             L(outline([(8, 40), (30, 44), (34, 68), (18, 72), (8, 58)]), 'shade', 'b', False),
             fringe([(66, 20), (86, 30), (92, 48), (90, 66, 1), (82, 52), (74, 46)])],
    'back': [L(ell(50, -2, 7, 8)),
             L(outline([(16, 70), (12, 44), (22, 22), (40, 10), (60, 10), (78, 22), (88, 44), (84, 62), (94, 72), (104, 80, 1), (88, 80), (80, 76), (50, 82), (20, 76)])),
             L(outline([(56, 12), (78, 22), (88, 46), (84, 72), (62, 80)]), 'shade', 'b', False)],
}

# Jorna Privinski (Shikino Murasaki): melena azul pizarra oscura con raya en medio, larga y abierta en capas por los hombros;
# cejas de puntito redondas, ojos grandes verdes y sonrisa
CHARS['jorna-privinski'] = {
    'body': 'chica', 'pal': pal('#2c3c4c', '#fde4d4', iris='#2a9a8a', shade='#1e2c3a', deep='#141e28', light='#4a5e70'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(18, 86), (20, 60), (30, 46), (50, 36), (70, 46), (80, 60), (82, 86)]},
    'front': [L(outline([(-2, 102), (2, 86), (12, 72), (14, 40), (28, 16), (50, 8), (72, 16), (86, 40), (88, 72), (98, 86), (102, 102), (86, 98), (84, 104), (78, 86), (22, 86),
                         (16, 104), (14, 98)])),
              L(outline([(-2, 102), (2, 86), (12, 76), (22, 88), (16, 104), (14, 98)]), 'shade', 'b', False),
              L(outline([(102, 102), (98, 86), (88, 76), (78, 88), (84, 104), (86, 98)]), 'shade', 'b', False),
              strand([(50, 8), (50, 30)], 'deep', 'b', 1.0),
              L(ell(40, 60, 4, 3), BLACK, 'f'), L(ell(60, 60, 4, 3), BLACK, 'f'),
              L(ell(30, 86, 0.9, 0.9), OUTC, 'f', False), L(ell(70, 86, 0.9, 0.9), OUTC, 'f', False)],
    'side': [L(outline([(60, 66), (68, 58), (82, 56), (88, 42), (82, 22), (62, 8), (36, 8), (16, 18), (6, 40), (4, 70), (-6, 92), (-4, 106, 1), (8, 98), (14, 110, 1), (24, 98),
                        (34, 106, 1), (40, 92), (56, 84)])),
             L(outline([(4, 60), (36, 62), (56, 84), (40, 92), (34, 106), (24, 98), (14, 110), (8, 98), (-4, 106), (-6, 92)]), 'shade', 'b', False)],
    'back': [L(outline([(0, 100), (4, 84), (12, 70), (14, 40), (28, 16), (50, 8), (72, 16), (86, 40), (88, 70), (96, 84), (100, 100), (84, 104), (70, 100), (50, 106), (30, 100),
                        (16, 104)])),
             L(outline([(54, 10), (74, 18), (88, 70), (96, 84), (100, 100), (84, 104), (70, 100), (60, 60)]), 'shade', 'b', False)],
}

# Marcelline Memoir (Higuchi Takeha): pelo melocotón abultado con puntas hacia fuera a los lados y un flequillo de rizos
# hasta las cejas; ojos grandes lilas
CHARS['marcelline-memoir'] = {
    'body': 'chica', 'pal': pal('#f4a878', '#fde4d4', iris='#7a5ab0', shade='#d8885a', deep='#b46a40', light='#fcc89e'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 96,
             'hairline': [(18, 84), (20, 64), (50, 62), (80, 64), (82, 84)]},
    'front': [L(outline([(16, 80), (6, 76), (-8, 70, 1), (10, 62), (8, 40), (20, 20), (40, 12), (50, 16), (60, 12), (80, 20), (92, 40), (90, 62), (108, 70, 1), (94, 76),
                         (84, 80), (80, 64), (20, 64)])),
              L(outline([(60, 14), (80, 22), (92, 42), (90, 62), (80, 44)]), 'shade', 'b', False),
              L(outline([(26, 24), (44, 16), (50, 20), (32, 30)]), 'light', 'b', False),
              fringe([(18, 72), (22, 56), (30, 50), (40, 52), (46, 46), (56, 48), (64, 52), (74, 50), (82, 60), (82, 76), (74, 66), (66, 70, 1), (60, 60), (52, 66, 1),
                      (44, 58), (36, 66, 1), (28, 62), (22, 74, 1)])],
    'side': [L(outline([(58, 66), (66, 58), (82, 58), (90, 46), (86, 26), (66, 12), (40, 8), (18, 18), (6, 40), (6, 62), (-10, 70, 1), (8, 74), (20, 80), (36, 76), (48, 68)])),
             L(outline([(6, 50), (34, 54), (48, 68), (36, 76), (20, 80), (8, 74), (-10, 70)]), 'shade', 'b', False),
             fringe([(66, 26), (86, 34), (92, 52), (88, 68, 1), (82, 56), (74, 50)])],
    'back': [L(outline([(16, 82), (6, 78), (-10, 70, 1), (10, 60), (8, 38), (20, 18), (50, 10), (80, 18), (92, 38), (90, 60), (110, 70, 1), (94, 78), (84, 82), (50, 88)])),
             L(outline([(54, 12), (80, 20), (92, 40), (90, 60), (110, 70), (94, 78), (84, 82), (60, 86)]), 'shade', 'b', False)],
}

# Staton Folhard (Ito Hiroyasu): pelo azul petróleo oscuro en mechones retorcidos que se enroscan hacia arriba y hacia fuera,
# con uno que le cruza la frente; ojos lilas afilados y sonrisa de lado
CHARS['staton-folhard'] = {
    'body': 'delgado', 'pal': pal('#1e3e50', '#f8d4b4', iris='#5a5ab2', shade='#162e3c', deep='#0e1e28', light='#345e74'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(16, 72), (20, 58), (36, 52), (50, 50), (66, 52), (80, 56), (84, 72)]},
    'front': [L(outline([(18, 70), (14, 50), (0, 46, 1), (10, 36), (-6, 26, 1), (8, 24), (14, 16), (24, 14), (22, -4), (30, -10, 1), (30, 2), (36, 8), (50, 4), (54, -8),
                         (62, -14, 1), (62, 2), (74, 8), (84, 16), (100, 22, 1), (88, 32), (88, 50), (84, 70), (78, 56), (22, 56)])),
              L(outline([(62, 2), (74, 8), (84, 16), (100, 22), (88, 32), (88, 50), (80, 40)]), 'shade', 'b', False),
              fringe([(86, 40), (70, 36), (50, 40), (34, 50), (24, 66), (30, 72, 1), (36, 58), (50, 50), (66, 48), (80, 52)])],
    'side': [L(outline([(58, 58), (68, 50), (84, 48), (92, 36), (88, 22), (98, 14, 1), (80, 12), (70, -2), (62, -14, 1), (56, 4), (36, 2), (24, -8), (14, -12, 1), (20, 8),
                        (6, 20), (-8, 18, 1), (2, 32), (4, 54), (16, 72), (30, 70), (42, 62), (50, 58)])),
             L(outline([(4, 40), (34, 46), (42, 62), (30, 70), (16, 72)]), 'shade', 'b', False),
             fringe([(64, 30), (86, 32), (96, 44), (92, 58, 1), (84, 46), (72, 42)])],
    'back': [L(outline([(18, 76), (12, 50), (0, 44, 1), (10, 34), (-6, 24, 1), (10, 20), (22, 12), (20, -6), (30, -12, 1), (32, 4), (50, 2), (56, -10), (64, -16, 1), (64, 2),
                        (80, 8), (98, 4, 1), (106, 16), (92, 24), (90, 50), (84, 76), (50, 84)])),
             L(outline([(56, 4), (80, 8), (98, 4), (106, 16), (92, 24), (90, 50), (84, 76), (62, 82)]), 'shade', 'b', False)],
}

# Aurelio Auditus (Hijiri Tokutarou): pelo morado grisáceo oscuro estirado hasta un moño alto, con dos trencitas finas que
# bajan desde detrás de las orejas y se unen en un lazo; orejas grandes y ojos amarillos de párpados caídos
CHARS['aurelio-auditus'] = {
    'body': 'delgado', 'pal': pal('#3e3a4e', '#f8d4b4', iris='#d8c070', shade='#2e2a3a', deep='#1e1c28', light='#5a566e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 96, 'big_ears': 2, 'ear_out': 2,
             'hairline': [(16, 66), (20, 52), (36, 46), (46, 50), (50, 56), (54, 50), (64, 46), (80, 52), (84, 66)]},
    'front': [L(ell(50, -4, 9, 9)), L(quad((16, 76), (8, 98), (24, 108)), 'mid', 'b', True, False, 3.4), L(quad((84, 76), (92, 98), (76, 108)), 'mid', 'b', True, False, 3.4),
              L(outline([(18, 64), (14, 40), (22, 20), (38, 10), (62, 10), (78, 20), (86, 40), (82, 64), (76, 50), (24, 50)])),
              L(outline([(58, 12), (78, 22), (86, 42), (82, 60), (74, 36)]), 'shade', 'b', False),
              *[L([(cx - 7, 72), (cx + 7, 72)], OUTC, 'f', False, False, 2.4) for cx in (36, 64)],
              *brows(BLACK, 2.0, 64)],
    'side': [L(ell(36, -2, 9, 9)), L(quad((40, 74), (20, 92), (6, 114)), 'mid', 'b', True, False, 3.4),
             L(outline([(58, 54), (68, 48), (84, 48), (88, 36), (82, 20), (62, 8), (38, 8), (18, 16), (8, 34), (8, 56), (20, 70), (34, 66), (46, 56)])),
             L(outline([(8, 40), (30, 44), (34, 66), (20, 70), (8, 56)]), 'shade', 'b', False)],
    'back': [L(ell(50, -4, 9, 9)), L(quad((22, 74), (50, 116), (78, 74)), 'mid', 'b', True, False, 3.4),
             L(outline([(18, 70), (14, 40), (22, 20), (38, 10), (62, 10), (78, 20), (86, 40), (82, 70), (50, 80)])),
             L(outline([(56, 12), (78, 22), (86, 44), (82, 70), (62, 78)]), 'shade', 'b', False),
             strand([(50, 6), (50, 76)], 'deep', 'b', 0.9)],
}

# Wilhelmina Goforth (Umezu Yamako): pelo fucsia peinado hacia atrás hasta un moño bajo enorme que asoma por los dos lados de
# la cabeza; cejas fucsia gruesas, ojos grandes rosados y labios pintados
CHARS['wilhelmina-goforth'] = {
    'body': 'chica', 'pal': pal('#d02a5c', '#fde4d4', iris='#c05a7a', shade='#a81e48', deep='#801436', light='#e8507a'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'lips', 'mouth_y': 94, 'mouth_w': 5,
             'hairline': [(16, 70), (20, 52), (36, 46), (50, 44), (64, 46), (80, 52), (84, 70)]},
    'front': [L(ell(50, 78, 46, 22), 'shade'),
              L(outline([(16, 66), (14, 38), (24, 16), (50, 8), (76, 16), (86, 38), (84, 66), (78, 52), (22, 52)])),
              L(outline([(58, 10), (78, 20), (86, 42), (84, 62), (76, 36)]), 'shade', 'b', False),
              *[strand([(x, 10), (x + (x - 50) * 0.3, 46)], 'deep', 'b', 0.9) for x in (40, 60)],
              *brows('mid', 3.4, 66)],
    'side': [L(ell(8, 66, 22, 20)), L(ell(4, 70, 16, 14), 'shade', 'b', False),
             L(outline([(58, 54), (68, 48), (84, 48), (88, 36), (82, 20), (62, 8), (38, 8), (18, 16), (10, 34), (14, 54), (24, 66), (36, 64), (46, 56)])),
             strand([(70, 14), (40, 18), (16, 40)], 'deep', 'b', 0.9),
             L(quad((72, 66), (78, 61), (86, 64)), 'mid', 'f', False, False, 3.2)],
    'back': [L(outline([(16, 60), (14, 36), (24, 16), (50, 8), (76, 16), (86, 36), (84, 60), (50, 56)])),
             L(ell(50, 76, 42, 24)), L(outline([(10, 80), (50, 92), (90, 80), (88, 90), (50, 100), (12, 90)]), 'shade', 'b', False),
             strand([(50, 54), (50, 98)], 'deep', 'b', 1.0), strand([(30, 60), (26, 94)], 'deep', 'b', 0.9), strand([(70, 60), (74, 94)], 'deep', 'b', 0.9)],
}

# Basil Wanderbilt (Iwakura Tomotsugu): pelo verde azulado oscuro ondulado y abultado hasta los hombros, con un mechón en
# medio de la frente; cejas gruesas, ojos lilas y ceño serio
CHARS['basil-wanderbilt'] = {
    'body': 'normal', 'pal': pal('#1e5a62', '#fde0cc', iris='#8a7ab0', shade='#16464c', deep='#0e3238', light='#2e7a84'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'frown', 'mouth_y': 96,
             'hairline': [(16, 86), (20, 60), (30, 54), (40, 58), (50, 50), (60, 58), (70, 54), (80, 60), (84, 86)]},
    'front': [L(outline([(14, 104), (4, 100), (6, 86), (-2, 78), (8, 66), (8, 44), (18, 24), (34, 12), (50, 10), (66, 12), (82, 24), (92, 44), (92, 66), (102, 78), (94, 86),
                         (96, 100), (86, 104), (80, 82), (20, 82)])),
              L(outline([(-2, 78), (8, 66), (18, 84), (14, 104), (4, 100), (6, 86)]), 'shade', 'b', False),
              L(outline([(102, 78), (92, 66), (82, 84), (86, 104), (96, 100), (94, 86)]), 'shade', 'b', False),
              strand([(36, 22), (30, 44)], 'deep', 'b', 1.0), strand([(64, 22), (70, 44)], 'deep', 'b', 1.0),
              L(quad((26, 68), (36, 62), (46, 67)), 'deep', 'f', False, False, 3.6), L(quad((74, 68), (64, 62), (54, 67)), 'deep', 'f', False, False, 3.6)],
    'side': [L(outline([(60, 64), (66, 56), (82, 56), (88, 42), (82, 22), (62, 8), (36, 8), (16, 18), (6, 40), (4, 64), (-6, 78), (-2, 94), (10, 100), (20, 108), (34, 100),
                        (46, 104), (56, 88)])),
             L(outline([(4, 58), (36, 62), (56, 88), (46, 104), (34, 100), (20, 108), (10, 100), (-2, 94), (-6, 78)]), 'shade', 'b', False),
             L(quad((72, 67), (78, 62), (86, 65)), 'deep', 'f', False, False, 3.4)],
    'back': [L(outline([(8, 102), (0, 90), (2, 76), (-4, 64), (8, 52), (8, 36), (20, 18), (50, 8), (80, 18), (92, 36), (92, 52), (104, 64), (98, 76), (100, 90), (92, 102),
                        (76, 98), (62, 106), (50, 98), (38, 106), (24, 98)])),
             L(outline([(2, 70), (50, 62), (98, 70), (100, 90), (92, 102), (76, 98), (62, 106), (50, 98), (38, 106), (24, 98), (8, 102), (0, 90)]), 'shade', 'b', False)],
}

# Odell Farley (Wakeno Seima): pelo azul pizarra enorme de pinchos, con un mechón verde menta cruzándole la frente y las puntas
# de las patillas también menta; ojos grises en espiral y boca apretada
MINT = hexc('#9ae0d0')


def spiral(y=78):
    out = []
    for cx in (36, 64):
        out += [L(ell(cx, y, 5.6, 5.6), OUTC, 'f', False), L(ell(cx, y, 4.6, 4.6), WHITE, 'f', False), ring(cx, y, 3.4, 3.4, (110, 110, 130, 255), 1.0),
                ring(cx, y, 1.8, 1.8, (110, 110, 130, 255), 1.0), L(ell(cx, y, 0.8, 0.8), OUTC, 'f', False)]
    return out


CHARS['odell-farley'] = {
    'body': 'bajito', 'pal': pal('#3a4a6c', '#fde0cc', shade='#2c3a56', deep='#1e283e', light='#56688e'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'eye_y': 78,
             'hairline': [(16, 84), (20, 62), (34, 58), (50, 56), (66, 58), (80, 62), (84, 84)]},
    'front': [L(outline([(18, 96), (6, 94, 1), (12, 82), (-6, 74, 1), (8, 66), (-6, 50, 1), (8, 44), (0, 24, 1), (16, 22), (16, 2, 1), (32, 12), (40, -8, 1), (50, 8),
                         (64, -6, 1), (66, 12), (86, 4, 1), (84, 22), (102, 26, 1), (92, 42), (106, 52, 1), (92, 64), (106, 76, 1), (90, 82), (94, 96, 1), (82, 96),
                         (80, 76), (20, 76)])),
              L(outline([(64, -6), (66, 12), (86, 4), (84, 22), (102, 26), (92, 42), (106, 52), (92, 64), (82, 52), (74, 30)]), 'shade', 'b', False),
              L(outline([(14, 92), (22, 86), (26, 98), (18, 102)]), MINT, 'b', False), L(outline([(86, 92), (78, 86), (74, 98), (82, 102)]), MINT, 'b', False),
              fringe([(26, 60), (36, 50), (52, 46), (64, 40), (74, 44), (68, 50), (72, 56), (58, 54), (42, 58), (32, 64)], MINT), *spiral()],
    'side': [L(outline([(60, 62), (70, 54), (84, 54), (92, 42), (100, 30, 1), (86, 26), (90, 8, 1), (72, 12), (66, -8, 1), (54, 8), (34, -4, 1), (30, 12), (10, 8, 1), (14, 26),
                        (-6, 32, 1), (6, 44), (-8, 58, 1), (6, 62), (-2, 80, 1), (14, 78), (12, 94, 1), (26, 84), (34, 96, 1), (42, 78), (52, 66)])),
             L(outline([(-6, 32), (40, 46), (52, 66), (42, 78), (34, 96), (26, 84), (12, 94), (14, 78), (-2, 80), (6, 62), (-8, 58), (6, 44)]), 'shade', 'b', False),
             fringe([(74, 42), (90, 40), (94, 48), (84, 52)], MINT),
             L(ell(82, 78, 4, 5), OUTC, 'f', False), L(ell(82.6, 78, 3, 4), WHITE, 'f', False), ring(83, 78, 1.8, 2.4, (110, 110, 130, 255), 0.9)],
    'back': [L(outline([(16, 96), (2, 96, 1), (10, 82), (-8, 74, 1), (8, 64), (-6, 48, 1), (8, 42), (0, 22, 1), (16, 20), (16, 0, 1), (32, 10), (40, -10, 1), (50, 6),
                        (64, -8, 1), (66, 10), (86, 2, 1), (84, 20), (104, 24, 1), (92, 42), (108, 50, 1), (92, 64), (108, 76, 1), (90, 84), (98, 98, 1), (80, 94),
                        (66, 100, 1), (60, 90), (50, 102, 1), (40, 90), (32, 100, 1)])),
             L(outline([(4, 64), (50, 58), (96, 64), (108, 76), (90, 84), (98, 98), (80, 94), (66, 100), (60, 90), (50, 102), (40, 90), (32, 100), (16, 96), (2, 96), (10, 82),
                        (-8, 74)]), 'shade', 'b', False)],
}

# Viki Devine (Jinguu Kougetsu): media melena verde azulada oscura con una cinta dorada en la cabeza, flequillo recto, dos
# mechones a los lados acabados en bola y una coleta baja; ojos grandes azul lavanda
_vd_tail = [(17, 66), (24, 66), (20, 96), (16, 98)]
CHARS['viki-devine'] = {
    'body': 'chica', 'pal': pal('#1e4a4e', '#fde4d4', iris='#7a8ad8', shade='#16383c', deep='#0e2a2c', light='#2e6a70'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'line', 'mouth_y': 96,
             'hairline': [(16, 84), (18, 62), (50, 64), (82, 62), (84, 84)]},
    'front': [L(outline([(14, 96), (10, 64), (16, 36), (30, 18), (50, 10), (70, 18), (84, 36), (90, 64), (86, 96), (78, 80), (22, 80)])),
              L(outline([(58, 12), (78, 22), (90, 60), (86, 92), (80, 60)]), 'shade', 'b', False),
              L(quad((12, 46), (50, 22), (88, 46)), GOLD, 'b', False, False, 2.4),
              *[strand([(x, 50), (x, 64)], 'deep', 'b', 0.8) for x in (32, 44, 56, 68)],
              *both(_vd_tail, 'mid', 'f'), L(ell(16, 102, 5, 7), 'mid', 'f'), L(ell(84, 102, 5, 7), 'mid', 'f'),
              *brows('mid', 3.2, 67)],
    'side': [L(outline([(24, 80), (16, 100), (12, 116, 1), (22, 104), (30, 86)])), L(ell(26, 82, 3.4, 3), GOLD, 'b', ln=True),
             L(outline([(58, 62), (66, 56), (82, 56), (88, 42), (82, 22), (62, 8), (36, 8), (16, 18), (6, 40), (6, 64), (14, 80), (30, 84), (44, 76), (50, 66)])),
             L(outline([(6, 44), (30, 48), (44, 76), (30, 84), (14, 80)]), 'shade', 'b', False),
             L(quad((6, 42), (40, 10), (88, 30)), GOLD, 'b', False, False, 2.4),
             fringe([(54, 66), (62, 66), (60, 96), (54, 98)]), L(ell(56, 102, 5, 7), 'mid', 'f')],
    'back': [L(outline([(44, 86), (40, 106), (50, 118, 1), (60, 106), (56, 86)])), L(ell(50, 88, 5, 3), GOLD, 'b', ln=True),
             L(ell(14, 100, 6, 8)), L(ell(86, 100, 6, 8)),
             L(outline([(12, 92), (8, 62), (14, 34), (30, 16), (50, 10), (70, 16), (86, 34), (92, 62), (88, 92), (50, 88)])),
             L(outline([(56, 12), (78, 22), (92, 62), (88, 92), (60, 88)]), 'shade', 'b', False),
             L(quad((10, 50), (50, 40), (90, 50)), GOLD, 'b', False, False, 2.4)],
}

# Horatio Tickner (Inoguchi Hideyuki): pelo verde oscuro enorme y esponjoso, abierto a los lados como una nube, con el
# flequillo en pico; cejas verdes gruesas, ojos azules, coloretes y orejas grandes
CHARS['horatio-tickner'] = {
    'body': 'bajito', 'pal': pal('#1e6a58', '#fde0cc', iris='#3a6aa8', shade='#165244', deep='#0e3c32', light='#2e8a74'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'big_ears': 2, 'ear_out': 2,
             'hairline': [(16, 66), (20, 56), (34, 54), (44, 62), (50, 54), (60, 58), (70, 54), (80, 56), (84, 66)]},
    'front': [L(outline([(18, 64), (10, 56), (-6, 50, 1), (4, 40), (-2, 28), (12, 16), (30, 8), (50, 2), (70, 8), (88, 14), (104, 26), (96, 40), (108, 50, 1), (90, 56),
                         (82, 64), (76, 54), (24, 54)])),
              L(outline([(58, 6), (88, 14), (104, 26), (96, 40), (108, 50), (90, 56), (80, 40)]), 'shade', 'b', False),
              L(outline([(24, 18), (44, 8), (52, 12), (30, 24)]), 'light', 'b', False),
              L(quad((26, 68), (36, 62), (46, 67)), 'mid', 'f', False, False, 3.6), L(quad((74, 68), (64, 62), (54, 67)), 'mid', 'f', False, False, 3.6),
              L(ell(28, 88, 4.6, 2.6), BLUSH, 'f', False), L(ell(72, 88, 4.6, 2.6), BLUSH, 'f', False), L(ell(50, 86, 2.2, 1.8), BLUSH, 'f', False)],
    'side': [L(outline([(58, 58), (66, 50), (82, 48), (94, 40), (100, 26), (88, 14), (66, 4), (40, 2), (16, 10), (2, 24), (-6, 40), (2, 56), (16, 64), (34, 60), (48, 58)])),
             L(outline([(-6, 40), (30, 40), (48, 58), (34, 60), (16, 64), (2, 56)]), 'shade', 'b', False),
             L(quad((72, 67), (78, 62), (86, 65)), 'mid', 'f', False, False, 3.4), L(ell(84, 88, 3.4, 2.2), BLUSH, 'f', False)],
    'back': [L(outline([(18, 70), (8, 60), (-6, 52), (2, 40), (-4, 26), (12, 12), (30, 4), (50, 0), (70, 4), (88, 12), (104, 26), (98, 40), (108, 52), (92, 60), (82, 70),
                        (50, 76)])),
             L(outline([(4, 46), (50, 56), (96, 46), (108, 52), (92, 60), (82, 70), (50, 76), (18, 70), (8, 60), (-6, 52)]), 'shade', 'b', False)],
}

# Barney Snellman (Takabashi Korekiyo, portero): grandullón con el pelo gris muy corto y una barba gris que le rodea toda la
# cara; cejas grises, ojillos negros, una franja de rubor sobre la nariz y una sonrisa ancha
GREYB = hexc('#a8a090')
CHARS['barney-snellman'] = {
    'body': 'corpulento', 'pal': pal('#a8a090', '#fcd8c0', shade='#8a8272', deep='#6a6454'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'none', 'big_ears': 2, 'ear_out': 3, 'eye_y': 78,
             'hairline': [(12, 74), (16, 56), (50, 50), (84, 56), (88, 74)],
             'face_front': outline([(12, 52), (30, 36), (50, 32), (70, 36), (88, 52), (92, 76), (86, 98), (66, 110), (50, 112), (34, 110), (14, 98), (8, 76)])},
    'front': [L(outline([(12, 70), (10, 40), (22, 18), (50, 8), (78, 18), (90, 40), (88, 70), (80, 54), (20, 54)])),
              L(outline([(60, 10), (80, 20), (90, 44), (88, 64), (78, 40)]), 'shade', 'b', False),
              L(outline([(10, 66), (16, 86), (30, 98), (50, 102), (70, 98), (84, 86), (90, 66), (92, 86), (84, 102), (68, 112), (50, 116), (32, 112), (16, 102), (8, 86)]), GREYB, 'f'),
              L([(26, 80), (74, 80), (74, 85), (26, 85)], BLUSH, 'f', False),
              L(outline([(28, 70), (32, 65), (42, 65), (44, 70)], 4), GREYB, 'f', ln=True), L(outline(mirror([(28, 70), (32, 65), (42, 65), (44, 70)]), 4), GREYB, 'f', ln=True),
              L(quad((32, 90), (50, 99), (68, 90)), OUTC, 'f', False, False, 1.8)],
    'side': [L(outline([(16, 56), (24, 30), (46, 20), (40, 50), (46, 80), (30, 88)]), 'skin_d', 'b', False),
             L(outline([(58, 56), (70, 50), (84, 46), (86, 32), (76, 16), (52, 8), (28, 10), (12, 24), (6, 44), (10, 64), (24, 66), (40, 60)])),
             L(outline([(54, 76), (62, 90), (76, 98), (88, 96), (90, 104), (74, 110), (58, 104), (48, 90)]), GREYB, 'f'),
             L([(76, 82), (88, 82), (88, 86), (76, 86)], BLUSH, 'f', False),
             L(outline([(72, 70), (76, 66), (84, 66), (86, 70)], 4), GREYB, 'f', ln=True)],
    'back': [L(outline([(14, 64), (12, 40), (24, 18), (50, 8), (76, 18), (88, 40), (86, 64), (50, 60)])),
             L(outline([(56, 10), (78, 20), (88, 44), (86, 64), (62, 62)]), 'shade', 'b', False),
             L(outline([(20, 64), (50, 60), (80, 64), (78, 84), (60, 96), (40, 96), (22, 84)]), 'skin_d', 'b', False)],
}
