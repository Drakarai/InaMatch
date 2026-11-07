"""Solaria-Zeus de Victory Road (vr-tenshou-zeus, 天翔ゼウス): sus modelos 3D de Inazuma Eleven: Victory Road
(英雄たちのヴィクトリーロード) en la enciclopedia. Personajes nuevos de Victory Road con un solo modelo cada uno (en la
wiki llevan alias de dioses: スサノオ, パーン, エロース...). Ningún id coge por prefijo el dibujo de otro."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars_vr_ouja_raimon import puff
from heads import quad  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (24, 22, 26, 255)


def fr(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Susano Ouji (Garci Stormdale, portero): pelo verde azulado muy oscuro con dos pinchos como cuernos arriba y dos
# pinchos largos hacia los lados, melena por detrás hasta los hombros y una coleta baja; patillas en punta; ojos rojos
# con la raya amarilla y cara seria
CHARS['garci-stormdale'] = {
    'body': 'normal', 'pal': pal('#163e46', '#d8a07a', iris='#c82a2a', shade='#0e2c32', deep='#0a2026', liner='#d8c84a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 100), (6, 64), (-16, 50, 1), (8, 40), (14, 18), (24, 4), (26, -14, 1), (36, 0), (50, -4), (64, 0), (74, -14, 1), (76, 4), (86, 18), (92, 40),
                         (116, 50, 1), (94, 64), (90, 100), (82, 66), (18, 66)])),
              L(outline([(64, 0), (74, -14), (76, 4), (86, 18), (92, 40), (116, 50), (94, 64), (90, 96), (84, 50)]), 'shade', 'b', False),
              fr([(16, 90, 1), (12, 56), (18, 34), (32, 24), (40, 40), (44, 30), (50, 46, 1), (56, 30), (60, 40), (68, 24), (82, 34), (88, 56), (84, 90, 1), (80, 66),
                  (74, 56), (68, 60), (58, 46), (42, 46), (32, 60), (26, 56), (20, 66)]),
              L(quad((25, 72), (36, 78), (45, 74)), 'liner', 'f', False, False, 1.0), L(quad((75, 72), (64, 78), (55, 74)), 'liner', 'f', False, False, 1.0)],
    'side': [L(rope((24, 80), (14, 100), (20, 116), 5), 'mid', 'b'),
             L(outline([(62, 62), (66, 50), (84, 48), (94, 32), (88, 12), (78, 4), (80, -16, 1), (62, -2), (36, -4), (14, 8), (2, 34), (-20, 46, 1), (2, 52), (0, 80),
                        (10, 98), (30, 100), (44, 86), (50, 72)])),
             L(outline([(2, 52), (28, 56), (44, 86), (30, 100), (10, 98)]), 'shade', 'b', False),
             fr([(66, 8), (90, 20), (96, 46), (92, 64, 1), (86, 56), (82, 74, 1), (76, 46)])],
    'back': [L(rope((50, 90), (48, 106), (54, 118), 5), 'mid', 'b'),
             L(outline([(10, 100), (6, 64), (-16, 50, 1), (8, 40), (14, 18), (24, 4), (26, -14, 1), (36, 0), (50, -4), (64, 0), (74, -14, 1), (76, 4), (86, 18), (92, 40),
                        (116, 50, 1), (94, 64), (90, 100), (70, 104), (50, 100), (30, 104)])),
             L(outline([(56, 0), (86, 18), (96, 50), (90, 96), (64, 100), (70, 50)]), 'shade', 'b', False)],
}

# Patry Ambrosia (Patrie Ambrosia): niña bajita de pelo lavanda azulado en una nube enorme de rizos como lana de oveja,
# con bucles grandes a los lados que le llegan a los hombros y un flequillo de rizos sobre los ojos; ojos naranja de
# gato y sonrisa con un colmillo
CHARS['patrie-ambrosia'] = {
    'body': 'chica', 'pal': pal('#9eaaf0', '#fce8dc', iris='#e09a1e', shade='#7a84c8', deep='#5e66a8'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(puff(4, 70, 16, 24, 5, 0.3)), L(puff(96, 70, 16, 24, 5, 0.6)), L(puff(8, 100, 12, 14, 4, 0.2)), L(puff(92, 100, 12, 14, 4, 0.6)),
              L(puff(50, 24, 56, 38, 9, 0.15)),
              L(puff(66, 14, 26, 20, 5, 0.3), 'shade', 'b', False),
              fr([(14, 70), (12, 50), (20, 36), (32, 42), (40, 34), (50, 44), (60, 34), (68, 42), (80, 36), (88, 50), (86, 70), (80, 62), (70, 66), (62, 58), (50, 66),
                  (38, 58), (30, 66), (20, 62)]),
              L(puff(12, 80, 9, 14, 4, 0.2), 'mid', 'f'), L(puff(88, 80, 9, 14, 4, 0.6), 'mid', 'f'),
              L([(53, 96), (54, 99)], WHITE, 'f', False, False, 1.2)],
    'side': [L(puff(40, 26, 52, 36, 9, 0.2)), L(puff(14, 76, 22, 28, 6, 0.3)), L(puff(30, 104, 14, 12, 4, 0.1)),
             L(outline([(0, 40), (30, 50), (40, 96), (16, 104), (-6, 80)]), 'shade', 'b', False),
             L(puff(54, 20, 16, 14, 4, 0.4), 'shade', 'b', False),
             L(puff(76, 36, 16, 12, 5, 0.3), 'mid', 'f')],
    'back': [L(puff(50, 30, 58, 40, 9, 0.15)), L(puff(6, 76, 18, 26, 5, 0.3)), L(puff(94, 76, 18, 26, 5, 0.6)), L(puff(50, 76, 40, 24, 7, 0.2)),
             L(outline([(20, 40), (60, 30), (96, 50), (80, 70), (40, 64)]), 'shade', 'b', False)],
}

# Enoguchi Aijirou (Garrick Loventhal): melena larga rosa salmón ondulada hasta los hombros, con raya en medio y las
# puntas abiertas en ondas; perilla gris azulada, cejas gruesas del mismo color, ojos azules y sonrisa de galán
CHARS['garrick-loventhal'] = {
    'body': 'delgado', 'pal': pal('#eea898', '#fbe6dc', iris='#4a6ab8', shade='#d0867a', deep='#b06a60', beard='#5a7a8a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(10, 104), (-8, 100, 1), (0, 84), (-10, 70, 1), (2, 60), (2, 30), (16, 8), (40, -4), (60, -4), (84, 8), (98, 30), (98, 60), (110, 70, 1), (100, 84),
                         (108, 100, 1), (90, 104), (84, 66), (16, 66)])),
              L(outline([(60, -2), (84, 10), (98, 40), (98, 96), (84, 60)]), 'shade', 'b', False),
              fr([(10, 92), (8, 50), (18, 24), (40, 12), (50, 20), (60, 12), (82, 24), (92, 50), (90, 92, 1), (82, 72), (76, 52), (64, 40), (52, 34), (48, 34), (36, 40),
                  (24, 52), (18, 72)]),
              strand([(50, 20), (36, 40), (24, 60)], 'deep', 'f', 1.0), strand([(50, 20), (64, 40), (76, 60)], 'deep', 'f', 1.0),
              L(outline([(28, 66), (36, 62), (44, 66), (42, 69), (30, 69)]), 'beard', 'f', False), L(outline([(72, 66), (64, 62), (56, 66), (58, 69), (70, 69)]), 'beard', 'f', False),
              L(outline([(46, 98), (54, 98), (52, 106), (48, 106)]), 'beard', 'f', False)],
    'side': [L(outline([(62, 66), (66, 52), (84, 48), (96, 32), (88, 8), (62, -4), (32, -2), (10, 12), (-2, 40), (-10, 70, 1), (0, 76), (-8, 96, 1), (12, 92), (6, 110, 1),
                        (28, 100), (36, 112, 1), (44, 94), (52, 78)])),
             L(outline([(-2, 44), (30, 50), (44, 94), (28, 100), (12, 92), (-8, 96), (0, 76)]), 'shade', 'b', False),
             fr([(68, 8), (90, 20), (98, 46), (94, 72, 1), (86, 56), (78, 42)]),
             L(outline([(80, 98), (86, 98), (84, 106), (80, 104)]), 'beard', 'f', False)],
    'back': [L(outline([(10, 108), (-10, 104, 1), (0, 86), (-10, 72, 1), (2, 62), (2, 30), (16, 8), (40, -4), (60, -4), (84, 8), (98, 30), (98, 62), (110, 72, 1), (100, 86),
                        (110, 104, 1), (90, 108), (74, 116, 1), (62, 104), (50, 116, 1), (38, 104), (26, 116, 1)])),
             L(ell(62, 50, 30, 28), 'shade', 'b', False)],
}

# Haie Kuon (Sampa Eonius): piel muy oscura; pelo verde menta peinado hacia atrás en franjas trenzadas pegadas a la cabeza,
# con dos cuentas moradas en la de en medio, y dos trenzas finas a los lados que acaban en punta; cejas gruesas menta y
# ojos amarillos caídos
CHARS['sampa-eonius'] = {
    'body': 'normal', 'pal': pal('#b4e0a8', '#5a3a2a', iris='#e0c84a', shade='#8aaa7a', deep='#6a8a5e', bead='#4a3a8a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 74), (10, 40), (20, 14), (50, 2), (80, 14), (90, 40), (84, 74), (78, 50), (22, 50)])),
              L(outline([(60, 4), (80, 14), (90, 40), (86, 66), (80, 44)]), 'shade', 'b', False),
              L(outline([(14, 56), (18, 34), (34, 20), (50, 16), (66, 20), (82, 34), (86, 56), (76, 48), (64, 40), (50, 38), (36, 40), (24, 48)]), 'mid', 'f'),
              strand([(34, 20), (40, 42)], 'deep', 'f', 1.0), strand([(66, 20), (60, 42)], 'deep', 'f', 1.0),
              L(rope((14, 60), (8, 90), (12, 110), 3.4), 'mid', 'f'), L(rope((86, 60), (92, 90), (88, 110), 3.4), 'mid', 'f'),
              L(outline([(26, 64), (36, 58), (46, 62), (44, 66), (34, 64), (28, 68)]), 'mid', 'f', ln=True),
              L(outline([(74, 64), (64, 58), (54, 62), (56, 66), (66, 64), (72, 68)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(64, 50), (72, 40), (88, 38), (92, 22), (74, 6), (46, 2), (22, 10), (8, 34), (8, 62), (20, 76), (36, 70), (48, 56)])),
             L(outline([(8, 40), (32, 44), (36, 70), (18, 74)]), 'shade', 'b', False),
             strand([(88, 24), (50, 12), (14, 30)], 'deep', 'b', 1.0), strand([(88, 34), (50, 26), (10, 46)], 'deep', 'b', 1.0),
             L(ell(30, 14, 2.6, 2.6), 'bead', 'f', ln=True), L(ell(18, 28, 2.6, 2.6), 'bead', 'f', ln=True),
             L(rope((60, 60), (64, 90), (60, 112), 3.4), 'mid', 'f')],
    'back': [L(outline([(16, 80), (10, 40), (20, 14), (50, 2), (80, 14), (90, 40), (84, 80), (50, 88)])),
             L(outline([(56, 4), (80, 14), (90, 40), (84, 76), (60, 60)]), 'shade', 'b', False),
             strand([(14, 40), (50, 54), (86, 40)], 'deep', 'b', 1.0), strand([(16, 60), (50, 72), (84, 60)], 'deep', 'b', 1.0),
             L(ell(50, 20, 3, 3), 'bead', 'f', ln=True), L(ell(50, 44, 3, 3), 'bead', 'f', ln=True),
             L(rope((50, 84), (48, 100), (50, 114), 3.4), 'mid', 'f'),
             L(rope((14, 70), (4, 88), (10, 104), 3.0), 'mid', 'b'), L(rope((86, 70), (96, 88), (90, 104), 3.0), 'mid', 'b')],
}

# Yamatsumi Kenou (Kenard Montemar): melena enorme morada oscura en ondas que se abre a los lados en bucles, con un pelo
# de antena curvado arriba y una cinta rosa y dorada alrededor de la cabeza; dos mechones largos por delante hasta el
# pecho; ojos rosados enfadados y dientes apretados
CHARS['kenard-montemar'] = {
    'body': 'normal', 'pal': pal('#3e1a54', '#fce4d4', iris='#c87a8a', shade='#2c1240', deep='#1e0c2e', band='#d8b45a', band2='#c83a6a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'hairline': False},
    'front': [L(puff(0, 80, 16, 24, 5, 0.3)), L(puff(100, 80, 16, 24, 5, 0.6)),
              L(outline([(10, 100), (4, 60), (6, 30), (20, 8), (44, -2), (56, -2), (80, 8), (94, 30), (96, 60), (90, 100), (82, 66), (18, 66)])),
              L(rope((48, -2), (44, -28), (62, -26), 2.8), 'mid', 'b'),
              L(outline([(60, 0), (82, 10), (94, 40), (94, 90), (82, 56)]), 'shade', 'b', False),
              fr([(14, 86), (10, 50), (20, 26), (40, 14), (50, 22), (60, 14), (80, 26), (90, 50), (86, 86), (80, 66), (74, 50), (60, 40), (52, 36), (48, 36), (40, 40),
                  (26, 50), (20, 66)]),
              L(rope((18, 60), (14, 90), (18, 122), 3.0), 'mid', 'f'), L(rope((82, 60), (86, 90), (82, 122), 3.0), 'mid', 'f'),
              L(quad((8, 40), (50, 10), (92, 40)), 'band', 'f', False, False, 3.4),
              L([(26, 22), (30, 20)], 'band2', 'f', False, False, 3.4), L([(70, 20), (74, 22)], 'band2', 'f', False, False, 3.4)],
    'side': [L(puff(14, 66, 26, 28, 6, 0.3)), L(puff(30, 96, 16, 14, 4, 0.2)),
             L(outline([(62, 62), (66, 50), (84, 46), (94, 30), (88, 8), (62, -4), (32, -2), (10, 14), (2, 40), (8, 70), (30, 84), (46, 76)])),
             L(rope((52, -2), (46, -28), (66, -26), 2.8), 'mid', 'b'),
             L(outline([(0, 44), (30, 50), (40, 80), (10, 90)]), 'shade', 'b', False),
             L(quad((86, 30), (50, 0), (10, 30)), 'band', 'f', False, False, 3.4),
             L(rope((68, 56), (76, 90), (80, 118), 2.8), 'mid', 'f')],
    'back': [L(puff(50, 74, 52, 34, 8, 0.2)),
             L(outline([(10, 90), (4, 60), (6, 30), (20, 8), (44, -2), (56, -2), (80, 8), (94, 30), (96, 60), (90, 90), (50, 96)])),
             L(rope((48, -2), (44, -28), (62, -26), 2.8), 'mid', 'b'),
             L(outline([(4, 60), (50, 70), (96, 60), (100, 90), (50, 106), (0, 90)]), 'shade', 'b', False),
             L(quad((6, 34), (50, 18), (94, 34)), 'band', 'f', False, False, 3.4)],
}

# Atora Suuri (Atol Lasalle): pelo azul celeste revuelto y abundante con un pelo de antena arriba, mechones que le caen
# sobre la cara y se ensombrecen a gris por debajo, con puntas curvadas a los lados; ojos azul grisáceo grandes y sonrisa
CHARS['atol-lasalle'] = {
    'body': 'bajito', 'pal': pal('#9accde', '#fce0d0', iris='#5a7a9a', shade='#8a9098', deep='#6a7078'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(12, 96), (-6, 90, 1), (2, 76), (0, 40), (12, 12), (30, -2), (40, -6), (40, -26, 1), (60, -14), (52, -4), (76, 4), (92, 18), (100, 40), (98, 76),
                         (108, 90, 1), (88, 96), (82, 64), (18, 64)])),
              L(outline([(0, 60), (12, 96), (-6, 90), (2, 76)]), 'shade', 'b', False), L(outline([(100, 60), (88, 96), (108, 90), (98, 76)]), 'shade', 'b', False),
              fr([(10, 80), (8, 50), (16, 28), (38, 14), (64, 14), (86, 26), (96, 48), (94, 80, 1), (86, 64), (76, 56), (66, 64), (60, 50), (52, 66), (46, 92, 1), (42, 64),
                  (34, 56), (24, 66), (16, 80, 1)]),
              strand([(30, 20), (48, 40)], 'deep', 'f', 1.0), strand([(60, 20), (80, 40)], 'deep', 'f', 1.0),
              L(rope((16, 76), (8, 90), (14, 100), 2.4), 'shade', 'f'), L(rope((84, 76), (92, 90), (86, 100), 2.4), 'shade', 'f')],
    'side': [L(outline([(62, 60), (66, 48), (84, 46), (96, 32), (90, 10), (66, -4), (60, -26, 1), (46, -8), (30, -4), (10, 10), (-2, 40), (-10, 56, 1), (4, 62), (2, 84),
                        (16, 100, 1), (22, 84), (36, 80), (46, 70)])),
             L(outline([(-2, 44), (30, 50), (36, 80), (22, 84), (16, 100), (2, 84), (4, 62)]), 'shade', 'b', False),
             fr([(68, 8), (90, 20), (98, 46), (94, 70, 1), (86, 56), (78, 42)])],
    'back': [L(outline([(12, 96), (-6, 92, 1), (2, 76), (0, 40), (12, 12), (30, -2), (40, -6), (40, -26, 1), (60, -14), (52, -4), (76, 4), (92, 18), (100, 40), (98, 76),
                        (108, 92, 1), (88, 96), (70, 102), (50, 98), (30, 102)])),
             L(outline([(0, 40), (30, 30), (60, 40), (100, 36), (98, 76), (88, 96), (70, 102), (50, 98), (30, 102), (12, 96), (2, 76)]), 'shade', 'b', False)],
}

# Uzukami Uzume (Revea Ristair): niña de piel morena; pelo azul marino en una melena hueca enorme con dos mechones de punta
# arriba como orejas, flequillo redondo y dos aros de pelo colgando a los lados por detrás; ojos amarillos redondos con
# sombra naranja y boca abierta de alegría
CHARS['revea-ristair'] = {
    'body': 'chica', 'pal': pal('#1c2668', '#9a643e', iris='#e8d83a', shade='#141c4e', deep='#0e1438', ring='#e07a2a'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'grin', 'mouth_y': 95, 'hairline': False},
    'front': [L(rope((8, 90), (-14, 100), (-6, 118), 4), 'mid', 'b'), L(rope((92, 90), (114, 100), (106, 118), 4), 'mid', 'b'),
              L(outline([(10, 92), (-2, 60), (2, 30), (16, 8), (30, 2), (32, -18, 1), (42, -2), (58, -2), (68, -18, 1), (70, 2), (84, 8), (98, 30), (102, 60), (90, 92),
                         (82, 66), (18, 66)])),
              L(outline([(60, 0), (84, 10), (98, 40), (98, 80), (84, 56)]), 'shade', 'b', False),
              fr([(14, 74), (10, 46), (22, 24), (50, 16), (78, 24), (90, 46), (86, 74), (80, 62), (66, 60), (50, 64), (34, 60), (20, 62)]),
              L(ell(36, 76, 7, 6.4), 'ring', 'f', False), L(ell(64, 76, 7, 6.4), 'ring', 'f', False),
              L(ell(36, 76, 4.4, 4.6), WHITE, 'f', False), L(ell(64, 76, 4.4, 4.6), WHITE, 'f', False),
              L(ell(36, 76, 3, 3.2), 'iris', 'f', False), L(ell(64, 76, 3, 3.2), 'iris', 'f', False),
              L(ell(36, 76, 1.2, 1.6), BLACK, 'f', False), L(ell(64, 76, 1.2, 1.6), BLACK, 'f', False)],
    'side': [L(rope((20, 82), (-4, 92), (2, 112), 4), 'mid', 'b'),
             L(outline([(62, 62), (66, 50), (84, 46), (94, 30), (86, 8), (62, -4), (52, -18, 1), (44, -4), (30, -2), (8, 14), (-2, 44), (2, 74), (20, 86), (40, 80), (50, 70)])),
             L(outline([(0, 44), (28, 50), (40, 80), (20, 86), (2, 74)]), 'shade', 'b', False),
             fr([(66, 6), (88, 18), (96, 42), (92, 62, 1), (84, 58), (78, 42)])],
    'back': [L(rope((14, 84), (-10, 96), (-2, 116), 4), 'mid', 'b'), L(rope((86, 84), (110, 96), (102, 116), 4), 'mid', 'b'),
             L(outline([(10, 92), (-2, 60), (2, 30), (16, 8), (30, 2), (32, -18, 1), (42, -2), (58, -2), (68, -18, 1), (70, 2), (84, 8), (98, 30), (102, 60), (90, 92),
                        (70, 98), (50, 94), (30, 98)])),
             L(outline([(4, 60), (50, 70), (96, 60), (90, 92), (70, 98), (50, 94), (30, 98), (10, 92)]), 'shade', 'b', False)],
}

# Harutani Moa (Harald Monet): melena larga lila pálido, lisa, con raya en medio, que le enmarca la cara y le cae hasta el
# pecho, y dos mechones que se curvan hacia fuera a los lados; ojos cerrados tranquilos
CHARS['harald-monet'] = {
    'body': 'delgado', 'pal': pal('#e0c8e8', '#fce8dc', iris='#6a5a8a', shade='#bca4c8', deep='#9a84a8'),
    'face': {'eyes': 'closed', 'brows': True, 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(8, 120), (2, 80), (4, 40), (14, 14), (36, -2), (50, 4), (64, -2), (86, 14), (96, 40), (98, 80), (92, 120), (82, 118), (82, 64), (18, 64),
                         (18, 118)])),
              L(rope((8, 70), (-12, 64), (-20, 84), 3.6), 'mid', 'b'), L(rope((92, 70), (112, 64), (120, 84), 3.6), 'mid', 'b'),
              L(outline([(60, 0), (86, 14), (96, 44), (96, 116), (84, 64)]), 'shade', 'b', False),
              fr([(12, 116), (10, 56), (16, 30), (34, 14), (50, 22), (66, 14), (84, 30), (90, 56), (88, 116), (80, 116), (80, 64), (72, 42), (58, 32), (50, 28), (42, 32),
                  (28, 42), (20, 64), (20, 116)]),
              strand([(50, 6), (50, 22)], 'deep', 'f', 1.2)],
    'side': [L(outline([(62, 66), (66, 52), (84, 48), (94, 30), (86, 8), (60, -4), (32, -2), (10, 12), (0, 40), (-2, 80), (2, 118), (24, 124), (40, 104), (50, 82)])),
             L(rope((10, 64), (-10, 58), (-18, 78), 3.6), 'mid', 'b'),
             L(outline([(-2, 50), (28, 56), (40, 104), (24, 124), (2, 118)]), 'shade', 'b', False),
             fr([(66, 6), (90, 18), (98, 44), (96, 84, 1), (86, 62), (78, 42)])],
    'back': [L(rope((8, 70), (-12, 64), (-20, 84), 3.6), 'mid', 'b'), L(rope((92, 70), (112, 64), (120, 84), 3.6), 'mid', 'b'),
             L(outline([(8, 112), (2, 80), (4, 40), (14, 14), (36, -2), (64, -2), (86, 14), (96, 40), (98, 80), (92, 112), (70, 118), (50, 114), (30, 118)])),
             L(outline([(56, 0), (86, 14), (98, 44), (94, 110), (64, 110), (70, 50)]), 'shade', 'b', False)],
}

# Zerosu Retsushi (Ciro Zealon): pelo blanco recogido arriba en una coleta con goma negra que se abre en una nube enorme
# de bultos, que pasa de blanco a granate y acaba en puntas fucsia por abajo; flequillo blanco ondulado; ojos lila
CHARS['ciro-zealon'] = {
    'body': 'bajito', 'pal': pal('#eef4f4', '#fce4d4', iris='#a88ac8', shade='#c8c4c8', deep='#a8a0a8', low='#b42446', tip='#f0306a', tie='#3a3a3e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(puff(4, 74, 20, 26, 5, 0.3), 'low'), L(puff(96, 74, 20, 26, 5, 0.6), 'low'),
              L(puff(8, 96, 14, 10, 4, 0.2), 'tip'), L(puff(92, 96, 14, 10, 4, 0.6), 'tip'),
              L(puff(50, -8, 40, 22, 7, 0.2)),
              L(outline([(12, 80), (6, 40), (18, 14), (50, 6), (82, 14), (94, 40), (88, 80), (82, 62), (18, 62)])),
              L(quad((40, 10), (50, 7), (60, 10)), 'tie', 'f', False, False, 3.0),
              fr([(16, 76), (12, 48), (22, 26), (42, 16), (60, 18), (78, 26), (88, 48), (84, 70, 1), (76, 58), (64, 54), (56, 62), (50, 56), (40, 60), (30, 56), (24, 66)]),
              strand([(40, 20), (34, 40)], 'shade', 'f', 1.0), strand([(60, 20), (66, 40)], 'shade', 'f', 1.0)],
    'side': [L(puff(16, 50, 32, 30, 7, 0.3), 'low'), L(puff(26, 82, 22, 16, 5, 0.2), 'tip'),
             L(puff(40, -6, 26, 20, 6, 0.4)), L(quad((46, 6), (52, 10), (58, 12)), 'tie', 'f', False, False, 3.0),
             L(outline([(60, 60), (66, 48), (84, 46), (94, 32), (86, 10), (60, 4), (34, 10), (20, 30), (24, 56), (40, 64), (50, 62)])),
             fr([(66, 10), (90, 20), (96, 44), (92, 62, 1), (84, 56), (76, 42)])],
    'back': [L(puff(50, 70, 52, 32, 8, 0.2), 'low'), L(puff(50, 92, 40, 12, 6, 0.4), 'tip'),
             L(puff(50, 26, 50, 30, 8, 0.1)), L(puff(50, -8, 40, 22, 7, 0.2)),
             L(quad((40, 10), (50, 7), (60, 10)), 'tie', 'f', False, False, 3.0)],
}

# Teita Tanji (Thaddeus Bellefax, 'アフロディ帝'): melena rubia pálida enorme en pinchos largos hacia arriba y hacia los
# lados, con un pincho en el centro de la frente; por detrás el pelo se ensombrece a castaño; ojos de distinto color
# (rosa y azul) y sonrisa
CHARS['thaddeus-bellefax'] = {
    'body': 'normal', 'pal': pal('#ead292', '#fce4d4', iris='#d0508a', shade='#c4a86a', deep='#a0804a', back='#a07a50', iris2='#3a7ad0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(14, 100), (-14, 104, 1), (-2, 88), (-20, 74, 1), (0, 66), (-12, 46, 1), (4, 40), (0, 20, 1), (18, 18), (20, -2, 1), (36, 6), (50, -22, 1), (64, 6),
                         (80, -2, 1), (82, 18), (100, 20, 1), (96, 40), (112, 46, 1), (100, 66), (120, 74, 1), (102, 88), (114, 104, 1), (86, 100), (82, 66), (18, 66)])),
              L(outline([(64, 6), (80, -2), (82, 18), (100, 20), (96, 40), (112, 46), (100, 66), (120, 74), (102, 88), (94, 70), (84, 40)]), 'shade', 'b', False),
              fr([(14, 84, 1), (10, 52), (20, 30), (38, 20), (50, 8, 1), (62, 20), (80, 30), (90, 52), (86, 84, 1), (78, 64), (72, 54), (60, 50), (52, 70, 1), (48, 50),
                  (40, 50), (28, 56), (22, 66)]),
              L(outline([(40, 22), (50, 12), (60, 22), (54, 40), (46, 40)]), 'light', 'f', False),
              L(ell(65, 77, 3.4, 4.2), 'iris2', 'f', False)],
    'side': [L(outline([(62, 62), (66, 50), (84, 46), (96, 34), (90, 16), (100, 2, 1), (80, 4), (76, -18, 1), (60, -2), (40, -14, 1), (34, 4), (10, 0, 1), (16, 18), (-10, 26, 1),
                        (6, 38), (-16, 54, 1), (4, 58), (-10, 80, 1), (10, 78), (6, 100, 1), (24, 88), (30, 104, 1), (40, 84), (50, 72)])),
             L(outline([(4, 38), (28, 44), (40, 84), (24, 88), (10, 78)]), 'back', 'b', False),
             fr([(66, 8), (90, 20), (98, 46), (94, 74, 1), (86, 58), (78, 42)])],
    'back': [L(outline([(14, 104), (-14, 108, 1), (-2, 90), (-20, 76, 1), (0, 66), (-12, 46, 1), (4, 40), (0, 20, 1), (18, 18), (20, -2, 1), (36, 6), (50, -22, 1), (64, 6),
                        (80, -2, 1), (82, 18), (100, 20, 1), (96, 40), (112, 46, 1), (100, 66), (120, 76, 1), (102, 90), (114, 108, 1), (86, 104), (60, 96), (50, 106, 1),
                        (40, 96)]), 'back'),
             L(outline([(-14, 108), (-2, 90), (-20, 76), (0, 66), (-12, 46), (4, 40), (14, 60), (14, 96)]), 'mid', 'b', False),
             L(outline([(114, 108), (102, 90), (120, 76), (100, 66), (112, 46), (96, 40), (86, 60), (86, 96)]), 'mid', 'b', False)],
}

# Izana Giyuu (Riza Nagivar): pelo azul petróleo voluminoso peinado hacia atrás en dos grandes ondas a los lados, con un
# pico en la frente, y una melena larga que le cae por la espalda; ojos violeta afilados y sonrisa altiva
CHARS['riza-nagivar'] = {
    'body': 'delgado', 'pal': pal('#2a6a8e', '#fce4d4', iris='#7a6ac8', shade='#1e5070', deep='#143a54'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(6, 120), (-10, 100), (-6, 70), (-8, 40), (6, 12), (30, -4), (50, 0), (70, -4), (94, 12), (108, 40), (106, 70), (110, 100), (94, 120), (84, 66),
                         (16, 66)])),
              L(outline([(60, -2), (94, 14), (106, 44), (106, 110), (84, 60)]), 'shade', 'b', False),
              fr([(14, 84), (2, 70), (0, 44), (14, 22), (36, 14), (50, 20), (64, 14), (86, 22), (100, 44), (98, 70), (86, 84), (82, 62), (70, 54), (58, 50), (50, 64, 1),
                  (42, 50), (30, 54), (18, 62)]),
              L(outline([(4, 44), (16, 30), (30, 34), (24, 46), (12, 52)]), 'shade', 'f', False), L(outline([(96, 44), (84, 30), (70, 34), (76, 46), (88, 52)]), 'shade', 'f', False)],
    'side': [L(outline([(62, 60), (66, 48), (84, 46), (96, 32), (88, 8), (62, -6), (32, -4), (10, 12), (-6, 40), (-16, 80), (-30, 116, 1), (-6, 108), (6, 120, 1), (22, 100),
                        (40, 80), (50, 70)])),
             L(outline([(-6, 50), (24, 56), (40, 80), (6, 120), (-6, 108), (-30, 116), (-16, 80)]), 'shade', 'b', False),
             L(puff(60, 22, 26, 18, 5, 0.3), 'mid', 'f'), strand([(44, 22), (62, 14), (80, 26)], 'deep', 'f', 1.0)],
    'back': [L(outline([(4, 116), (-10, 100), (-6, 70), (-8, 40), (6, 12), (30, -4), (50, 0), (70, -4), (94, 12), (108, 40), (106, 70), (110, 100), (96, 116), (72, 124),
                        (50, 118), (28, 124)])),
             L(outline([(20, 30), (34, 10), (40, 40)]), 'shade', 'b', False), L(outline([(80, 30), (66, 10), (60, 40)]), 'shade', 'b', False),
             L(outline([(40, 40), (60, 40), (72, 120), (50, 118), (28, 120)]), 'shade', 'b', False)],
}

# Hekate Meika (Cate Heckel): niña de piel morena con una melena enorme rosa claro, ondulada y salvaje, en mechones que le
# caen hasta la cintura; ojos rojos con la raya roja y pestañas negras marcadas
CHARS['cate-heckel'] = {
    'body': 'chica', 'pal': pal('#f4b4b0', '#c8865a', iris='#c82a2a', shade='#d48e8a', deep='#b4706c', liner='#e83a3a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(8, 120), (-16, 118, 1), (-6, 100), (-20, 84, 1), (-6, 74), (-14, 52, 1), (0, 44), (-2, 20, 1), (16, 14), (26, -6), (40, -2), (50, -20, 1), (62, -4),
                         (80, -4), (86, 14), (104, 20, 1), (100, 44), (114, 52, 1), (106, 74), (120, 84, 1), (106, 100), (116, 118, 1), (92, 120), (84, 66), (16, 66)])),
              L(outline([(62, -4), (80, -4), (86, 14), (104, 20), (100, 44), (114, 52), (106, 74), (120, 84), (106, 100), (116, 118), (92, 116), (84, 60)]), 'shade', 'b', False),
              fr([(12, 92, 1), (8, 52), (18, 28), (40, 16), (60, 16), (82, 28), (92, 52), (88, 92, 1), (80, 66), (72, 54), (60, 50), (52, 60), (46, 50), (34, 54), (24, 66)]),
              L(rope((14, 80), (4, 100), (12, 118), 4), 'mid', 'f'), L(rope((86, 80), (96, 100), (88, 118), 4), 'mid', 'f'),
              L([(24, 70), (30, 66)], OUTC, 'f', False, False, 1.4), L([(76, 70), (70, 66)], OUTC, 'f', False, False, 1.4),
              L(quad((27, 80), (36, 84), (44, 80)), 'liner', 'f', False, False, 1.2), L(quad((73, 80), (64, 84), (56, 80)), 'liner', 'f', False, False, 1.2)],
    'side': [L(outline([(62, 64), (66, 50), (84, 46), (96, 30), (88, 6), (62, -6), (32, -4), (10, 10), (-6, 40), (-20, 64, 1), (-6, 70), (-22, 96, 1), (-2, 96), (-10, 120, 1),
                        (12, 108), (16, 124, 1), (30, 104), (44, 84)])),
             L(outline([(-6, 46), (24, 52), (44, 84), (16, 124), (12, 108), (-10, 120), (-2, 96), (-22, 96), (-6, 70)]), 'shade', 'b', False),
             fr([(66, 6), (90, 18), (98, 44), (94, 72, 1), (86, 58), (78, 42)])],
    'back': [L(outline([(8, 122), (-16, 120, 1), (-6, 100), (-20, 84, 1), (-6, 74), (-14, 52, 1), (0, 44), (-2, 20, 1), (16, 14), (26, -6), (40, -2), (50, -20, 1), (62, -4),
                        (80, -4), (86, 14), (104, 20, 1), (100, 44), (114, 52, 1), (106, 74), (120, 84, 1), (106, 100), (116, 120, 1), (92, 122), (72, 130, 1), (60, 118),
                        (50, 128, 1), (40, 118), (28, 130, 1)])),
             L(outline([(50, 0), (80, 20), (90, 70), (70, 120), (50, 118), (60, 60)]), 'shade', 'b', False)]}

# Otaruda Rousuke (Iskandar Tarusian, portero): grandullón de piel morena oscura y cara ancha con pintura blanca en rayas
# por la frente y las mejillas; una mata enorme de pelo crema recogido en un moño alto con una goma dorada y trenzas
# gruesas por los lados y la espalda; ojos amarillos y sonrisa enseñando los dientes
_isk_face = blob([(10, 50), (50, 40), (90, 50), (98, 80), (92, 104), (72, 116), (50, 118), (28, 116), (8, 104), (2, 80)])
CHARS['iskandar-tarusian'] = {
    'body': 'corpulento', 'pal': pal('#e2c8b4', '#8a5034', iris='#e8b42a', shade='#c4a490', deep='#a48672', gold='#d8a43a', paint='#efe6d8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 100, 'hairline': False, 'face_front': _isk_face, 'ear_out': 6},
    'front': [L(rope((8, 70), (-6, 96), (2, 118), 7), 'mid', 'b'), L(ell(-2, 104, 6, 2.6), 'gold', 'b'),
              L(puff(56, -10, 34, 22, 6, 0.3)),
              L(outline([(10, 70), (6, 40), (18, 14), (50, 4), (82, 14), (94, 40), (90, 70), (82, 56), (18, 56)])),
              L(outline([(60, -28), (88, -10), (92, 20), (80, 10)]), 'shade', 'b', False),
              L(quad((36, 8), (50, 2), (64, 8)), 'gold', 'f', False, False, 3.0),
              L(outline([(10, 60), (16, 38), (34, 26), (50, 30), (66, 26), (84, 38), (90, 60), (80, 50), (50, 44), (20, 50)]), 'mid', 'f'),
              L([(42, 50), (40, 64)], 'paint', 'f', False, False, 2.4), L([(58, 50), (60, 64)], 'paint', 'f', False, False, 2.4),
              L([(18, 80), (30, 86)], 'paint', 'f', False, False, 2.2), L([(82, 80), (70, 86)], 'paint', 'f', False, False, 2.2),
              L([(16, 88), (26, 92)], 'paint', 'f', False, False, 1.8), L([(84, 88), (74, 92)], 'paint', 'f', False, False, 1.8)],
    'side': [L(puff(30, 0, 34, 24, 6, 0.3)),
             L(outline([(66, 52), (80, 46), (88, 30), (70, 10), (40, 6), (14, 18), (2, 44), (0, 76), (14, 96), (34, 90), (46, 70), (56, 56)])),
             L(rope((20, 80), (34, 104), (60, 110), 7), 'mid', 'f'), L(ell(40, 106, 3, 6), 'gold', 'f'),
             strand([(10, 30), (40, 40), (60, 50)], 'deep', 'b', 1.0), strand([(4, 56), (30, 64), (46, 70)], 'deep', 'b', 1.0),
             L([(80, 80), (88, 84)], 'paint', 'f', False, False, 2.2)],
    'back': [L(puff(50, -6, 38, 24, 6, 0.3)),
             L(outline([(8, 100), (2, 60), (8, 26), (30, 6), (50, 2), (70, 6), (92, 26), (98, 60), (92, 100), (70, 110), (50, 106), (30, 110)])),
             strand([(10, 40), (50, 60), (90, 40)], 'deep', 'b', 1.2), strand([(6, 66), (50, 86), (94, 66)], 'deep', 'b', 1.2),
             strand([(20, 20), (60, 30), (90, 24)], 'deep', 'b', 1.2)],
}

# Izana Mitsuji (Orisa Namir): pelo verde oscuro en mechones de punta revueltos hacia arriba, con un mechón que le cae
# por la frente, y una coleta trenzada larga que sale de la nuca; ojos verdes afilados con la raya marcada
CHARS['orisa-namir'] = {
    'body': 'normal', 'pal': pal('#1e5a50', '#fce4d4', iris='#3aa86a', shade='#144238', deep='#0e3028', tie='#8a8a92'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(rope((80, 70), (96, 92), (90, 116), 5), 'mid', 'b'),
              L(outline([(14, 76), (-4, 66, 1), (6, 54), (-6, 38, 1), (8, 32), (6, 10, 1), (22, 10), (26, -8, 1), (40, 2), (52, -12, 1), (62, 2), (80, -4, 1), (80, 12),
                         (98, 18, 1), (92, 34), (106, 42, 1), (94, 54), (102, 68, 1), (86, 76), (82, 60), (18, 60)])),
              L(outline([(62, 2), (80, -4), (80, 12), (98, 18), (92, 34), (106, 42), (94, 54), (88, 44), (76, 24)]), 'shade', 'b', False),
              fr([(14, 70, 1), (12, 46), (22, 28), (42, 18), (62, 20), (80, 28), (88, 46), (86, 70, 1), (78, 56), (68, 50), (60, 58), (54, 80, 1), (50, 56), (40, 52),
                  (30, 56), (22, 64)]),
              strand([(34, 24), (40, 42)], 'deep', 'f', 1.0), strand([(64, 24), (60, 42)], 'deep', 'f', 1.0)],
    'side': [L(rope((18, 60), (-4, 84), (-6, 118), 6), 'mid', 'b'), L(ell(14, 62, 4, 4), 'tie', 'b'),
             L(outline([(62, 58), (66, 48), (84, 46), (96, 34), (92, 16), (100, 4, 1), (80, 6), (76, -14, 1), (60, 0), (40, -12, 1), (34, 4), (14, 2, 1), (16, 18), (2, 30),
                        (4, 54), (18, 66), (34, 64), (46, 58)])),
             L(outline([(2, 34), (26, 40), (34, 64), (18, 66), (4, 54)]), 'shade', 'b', False),
             fr([(66, 10), (90, 22), (96, 46, 1), (86, 42), (84, 60, 1), (78, 44), (70, 36)])],
    'back': [L(outline([(14, 80), (-4, 70, 1), (6, 56), (-6, 40, 1), (8, 32), (6, 10, 1), (22, 10), (26, -8, 1), (40, 2), (52, -12, 1), (62, 2), (80, -4, 1), (80, 12),
                        (98, 18, 1), (92, 34), (106, 44, 1), (94, 56), (102, 70, 1), (86, 80), (50, 86)])),
             L(outline([(56, 2), (82, 10), (98, 40), (86, 76), (60, 70)]), 'shade', 'b', False),
             strand([(20, 20), (50, 70)], 'deep', 'b', 1.0), strand([(80, 20), (50, 70)], 'deep', 'b', 1.0),
             L(rope((50, 72), (56, 96), (50, 124), 6), 'mid', 'f'), L(ell(50, 74, 4.4, 3.4), 'tie', 'f', ln=True)],
}

# Tajikarao Iwafumi (Burke Forzane): bajito de cara redonda; pelo azul marino en forma de casco abombado que le tapa la
# frente, con mechones naranja en punta por debajo y rayas naranja en el flequillo; ojos naranja redondos y brillantes,
# coloretes y boca de gato
CHARS['burke-forzane'] = {
    'body': 'bajito', 'pal': pal('#1e3e66', '#fce0cc', iris='#d0601e', shade='#142c4c', deep='#0e2038', orange='#d0581e', blush='#f0a090'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'none', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(6, 92), (-8, 82, 1), (4, 76), (2, 40), (14, 12), (36, -2), (64, -2), (86, 12), (98, 40), (96, 76), (108, 82, 1), (94, 92), (82, 66), (18, 66)])),
              L(outline([(-8, 82), (4, 76), (16, 84), (6, 92)]), 'orange', 'f', False), L(outline([(108, 82), (96, 76), (84, 84), (94, 92)]), 'orange', 'f', False),
              L(outline([(60, 0), (86, 14), (98, 44), (96, 74), (84, 50)]), 'shade', 'b', False),
              fr([(10, 74), (6, 46), (16, 24), (40, 12), (60, 12), (84, 24), (94, 46), (90, 74), (84, 66), (70, 64), (60, 68, 1), (56, 62), (44, 62), (40, 68, 1), (30, 64),
                  (16, 66)]),
              L(quad((38, 66), (34, 40), (44, 30)), 'orange', 'f', False, False, 2.4), L(quad((62, 66), (66, 40), (56, 30)), 'orange', 'f', False, False, 2.4),
              L(ell(26, 88, 5, 2.6), 'blush', 'f', False), L(ell(74, 88, 5, 2.6), 'blush', 'f', False),
              L(quad((44, 95), (47, 98), (50, 95)) + quad((50, 95), (53, 98), (56, 95))[1:], OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(62, 62), (66, 50), (84, 46), (96, 30), (88, 6), (62, -6), (32, -4), (10, 10), (-2, 40), (0, 76), (-10, 86, 1), (12, 92), (30, 90, 1), (40, 78),
                        (50, 70)])),
             L(outline([(-10, 86), (0, 76), (20, 82), (30, 90), (12, 92)]), 'orange', 'b', False),
             L(outline([(10, 6), (20, -6, 1), (24, 10)]), 'orange', 'f', False), L(outline([(0, 30), (-8, 20, 1), (8, 24)]), 'orange', 'f', False),
             L(outline([(0, 40), (28, 46), (40, 78), (12, 80)]), 'shade', 'b', False),
             fr([(66, 6), (90, 18), (98, 44), (94, 64, 1), (86, 56), (78, 42)]),
             L(ell(78, 88, 4, 2.4), 'blush', 'f', False)],
    'back': [L(outline([(6, 94), (-8, 84, 1), (4, 76), (2, 40), (14, 12), (36, -2), (64, -2), (86, 12), (98, 40), (96, 76), (108, 84, 1), (94, 94), (72, 100), (50, 96),
                        (28, 100)])),
             L(outline([(-8, 84), (4, 76), (50, 84), (96, 76), (108, 84), (94, 94), (72, 100), (50, 96), (28, 100), (6, 94)]), 'orange', 'b', False),
             L(outline([(56, 0), (86, 14), (98, 44), (94, 76), (60, 76)]), 'shade', 'b', False)],
}

# Mikazuchi Jinya (Kazimir Stormblade): bajito; pelo azul marino peinado hacia arriba y hacia su izquierda (la derecha de
# la imagen) en una gran onda que acaba en punta, con una franja turquesa por encima; dos mechones finos por delante de
# las orejas; ojos azules y boca de gato pícara
CHARS['kazimir-stormblade'] = {
    'body': 'bajito', 'pal': pal('#1e2c48', '#fce4d4', iris='#5a6ad8', shade='#141e34', deep='#0e1626', cyan='#6ae0d6'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'none', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 72), (10, 40), (6, 16), (20, 6), (40, -6), (64, -10), (90, -20, 1), (84, -4), (104, 4, 1), (94, 14), (98, 40), (94, 60), (84, 72), (82, 60),
                         (18, 60)])),
              L(outline([(64, -10), (90, -20), (84, -4), (104, 4), (94, 14), (98, 40), (90, 50), (80, 20)]), 'shade', 'b', False),
              L(outline([(4, 20), (20, 4), (44, -4), (66, -8), (50, 2), (28, 10), (10, 26)]), 'cyan', 'f', ln=True),
              fr([(14, 64), (12, 40), (24, 22), (46, 14), (70, 14), (88, 26), (94, 46), (90, 66, 1), (82, 54), (70, 48), (56, 50), (46, 56), (40, 50), (28, 54), (20, 60)]),
              L(rope((18, 62), (14, 86), (18, 98), 2.4), 'mid', 'f'), L(rope((82, 62), (86, 86), (82, 98), 2.4), 'mid', 'f'),
              L(quad((44, 95), (47, 98), (50, 95)) + quad((50, 95), (53, 98), (56, 95))[1:], OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(62, 56), (66, 46), (84, 44), (96, 30), (92, 10), (100, -6, 1), (80, -2), (64, -12), (40, -22, 1), (36, -4), (12, 4), (-14, 4, 1), (0, 16), (2, 40),
                        (6, 58), (20, 66), (36, 62), (48, 58)])),
             L(outline([(64, -12), (80, -2), (100, -6), (92, 6), (70, 2)]), 'cyan', 'f', ln=True),
             L(outline([(2, 30), (26, 36), (34, 62), (20, 66), (6, 58)]), 'shade', 'b', False),
             L(rope((60, 58), (62, 84), (58, 98), 2.4), 'mid', 'f')],
    'back': [L(outline([(16, 76), (10, 40), (6, 16), (20, 6), (40, -6), (64, -10), (90, -20, 1), (84, -4), (104, 4, 1), (94, 14), (98, 40), (94, 60), (84, 76), (50, 82)])),
             L(outline([(56, -6), (90, -18), (98, 40), (84, 72), (60, 64)]), 'shade', 'b', False),
             L(rope((26, 70), (22, 90), (26, 100), 2.4), 'mid', 'b'), L(rope((74, 70), (78, 90), (74, 100), 2.4), 'mid', 'b')],
}
