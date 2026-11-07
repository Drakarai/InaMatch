"""Nosfanáticos (cs-vamptym): el equipo de monstruos (vampiros, momia, Frankenstein...); sus modelos 3D de Chrono Stone como
referencia (busto de frente, perfil y espalda). desmodus-drakul-cs-vamp-mm tiene el mismo modelo que Desmodus y usa su dibujo."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from chars_alius import SKULL_F
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Vince Sizor (portero, Frankenstein): casco gris de una pieza que le cubre la cabeza hasta las cejas, con un tornillo
# grande atravesado arriba; un pañuelo rojo le tapa la boca y la nariz; piel morena y ojos amarillos
CHARS['vince-sizor'] = {
    'body': 'corpulento', 'pal': pal('#8a8a90', '#b88458', iris='#e0b020', shade='#6a6a70', light='#b4b4ba', bolt='#d8d4d4', bolt_d='#a8a4a4', scarf='#c81e24',
                          scarf_d='#981418'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': [L(outline([(46, 10), (46, -14), (54, -14), (54, 10)]), 'bolt_d', 'b'),
              L(outline([(14, -22), (86, -22), (86, -10), (14, -10)]), 'bolt', 'b'), L(outline([(4, -26), (14, -26), (14, -6), (4, -6)]), 'bolt', 'b'),
              L(outline([(86, -26), (96, -26), (96, -6), (86, -6)]), 'bolt', 'b'), L(ell(50, -16, 10, 9), 'mid', 'b'),
              L(outline([(10, 92), (8, 50), (16, 20), (36, 4), (64, 4), (84, 20), (92, 50), (90, 92), (80, 80), (78, 64), (60, 52), (50, 66, 1), (40, 52), (22, 64),
                         (20, 80)]), 'mid', 'f'),
              L(outline([(60, 8), (82, 22), (90, 56), (86, 86), (78, 60)]), 'shade', 'f', False), L(outline([(24, 20), (40, 10), (34, 26)]), 'light', 'f', False),
              L(outline([(8, 80), (26, 82), (50, 88), (74, 82), (92, 80), (94, 104), (74, 116), (26, 116), (6, 104)]), 'scarf', 'f', ln=True),
              L(outline([(56, 88), (92, 82), (92, 104), (70, 112)]), 'scarf_d', 'f', False)],
    'side': [L(outline([(44, 10), (44, -14), (56, -14), (56, 10)]), 'bolt_d', 'b'), L(ell(50, -18, 10, 10), 'bolt', 'b', ln=True),
             L(outline([(54, 54), (62, 46), (80, 44), (90, 30), (84, 10), (64, 2), (36, 2), (14, 16), (4, 40), (6, 70), (16, 92), (36, 96), (50, 82)]), 'mid'),
             L(outline([(4, 40), (26, 46), (30, 90), (12, 86)]), 'shade', 'b', False),
             L(outline([(30, 76), (60, 72), (96, 78), (98, 96), (60, 102), (30, 96)]), 'scarf', 'f', ln=True)],
    'back': [L(outline([(46, 10), (46, -14), (54, -14), (54, 10)]), 'bolt_d', 'b'),
             L(outline([(14, -22), (86, -22), (86, -10), (14, -10)]), 'bolt', 'b'), L(outline([(4, -26), (14, -26), (14, -6), (4, -6)]), 'bolt', 'b'),
             L(outline([(86, -26), (96, -26), (96, -6), (86, -6)]), 'bolt', 'b'), L(ell(50, -16, 10, 9), 'mid', 'b'),
             L(outline([(10, 92), (8, 50), (16, 20), (36, 4), (64, 4), (84, 20), (92, 50), (90, 92), (50, 98)]), 'mid'),
             L(outline([(56, 8), (84, 22), (92, 56), (88, 90), (64, 96)]), 'shade', 'b', False),
             L(outline([(8, 78), (50, 84), (92, 78), (94, 94), (50, 100), (6, 94)]), 'scarf', 'f', ln=True)],
}

# Ron Innwater: pelo blanco rosado peinado hacia atrás muy pegado, con dos cuernos de pelo a los lados de la frente y dos
# trenzas largas de cuentas que le caen junto a la cara; piel morena, ojos rojos y marcas negras bajo los ojos
CHARS['ron-innwater'] = {
    'body': 'normal', 'pal': pal('#e8d0e4', '#a87048', iris='#c81e4a', shade='#b89ab8', mark='#1e1a1e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': [(14, 60), (24, 40), (40, 30), (50, 28), (60, 30), (76, 40), (86, 60)]},
    'front': [L(outline([(16, 76), (10, 44), (-8, 30, 1), (14, 26), (26, 8), (50, 0), (74, 8), (86, 26), (108, 30, 1), (90, 44), (84, 76), (80, 60), (20, 60)])),
              L(outline([(60, 4), (82, 18), (90, 46), (84, 66), (76, 40)]), 'shade', 'b', False),
              strand([(36, 6), (30, 36)], 'shade', 'b', 1.0), strand([(50, 2), (50, 30)], 'shade', 'b', 1.0), strand([(64, 6), (70, 36)], 'shade', 'b', 1.0)]
             + [L(ell(x, y, 5, 5), 'mid', 'f', ln=True) for x in (12, 88) for y in (70, 80, 90, 100, 110)]
             + [L(outline([(28, 80), (36, 84), (30, 96), (26, 92)]), 'mark', 'f', False), L(outline([(72, 80), (64, 84), (70, 96), (74, 92)]), 'mark', 'f', False)],
    'side': [L(outline([(54, 62), (58, 50), (78, 42), (90, 28), (84, 10), (64, 0), (38, 0), (16, 12), (6, 36), (6, 70), (18, 88), (34, 86), (46, 76)])),
             L(outline([(76, 28), (92, 14, 1), (90, 34)]), 'mid', 'f', ln=True),
             L(outline([(4, 36), (26, 42), (30, 82), (10, 78)]), 'shade', 'b', False),
             strand([(70, 10), (30, 20), (12, 50)], 'shade', 'b', 1.0)]
            + [L(ell(x, y, 5, 5), 'mid', 'f', ln=True) for x, y in ((56, 66), (52, 76), (46, 86), (40, 96), (34, 106))]
            + [L(outline([(76, 80), (84, 82), (80, 94)]), 'mark', 'f', False)],
    'back': [L(outline([(16, 86), (10, 44), (-8, 30, 1), (14, 26), (26, 8), (50, 0), (74, 8), (86, 26), (108, 30, 1), (90, 44), (84, 86), (50, 92)])),
             L(outline([(56, 4), (84, 18), (92, 50), (86, 82), (64, 88)]), 'shade', 'b', False),
             strand([(36, 6), (34, 84)], 'shade', 'b', 1.0), strand([(50, 2), (50, 88)], 'shade', 'b', 1.0), strand([(64, 6), (66, 84)], 'shade', 'b', 1.0)]
            + [L(ell(x, y, 5, 5), 'mid', 'f', ln=True) for x in (10, 90) for y in (70, 80, 90, 100, 110)],
}

# Holly Waters: gordita de cara redonda y pálida; media melena rosa en casco que le cae en diagonal sobre un ojo; sombra
# de ojos morada y labios morados
CHARS['holly-waters'] = {
    'body': 'corpulento', 'pal': pal('#e8b4cc', '#fcecd4', iris='#3aa8a8', shade='#c88aa8', lid='#6a4a8a', mouth='#6a4a8a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'lips', 'mouth_y': 100, 'mouth_w': 5, 'face_front': blob([(12, 56), (50, 48), (88, 56), (96, 84), (88, 108),
                                                                                                            (66, 118), (34, 118), (12, 108), (4, 84)]),
             'hairline': False},
    'front': [L(outline([(10, 84), (4, 50), (12, 20), (34, 4), (62, 2), (84, 14), (96, 44), (96, 84), (86, 92), (84, 66), (16, 66)])),
              L(outline([(60, 6), (84, 18), (94, 50), (90, 84), (80, 50)]), 'shade', 'b', False),
              L(ell(64, 76, 9, 6), 'lid', 'b', False),
              fringe([(8, 72), (8, 40), (22, 16), (50, 8), (76, 16), (90, 40), (92, 72), (86, 64), (78, 52), (62, 50), (50, 56), (40, 68), (32, 90), (20, 92), (12, 84)]),
              strand([(30, 20), (24, 60)], 'shade', 'f', 1.0), strand([(50, 14), (46, 50)], 'shade', 'f', 1.0), strand([(70, 18), (74, 48)], 'shade', 'f', 1.0)],
    'side': [L(outline([(56, 66), (60, 54), (84, 50), (94, 32), (88, 10), (64, -2), (36, 0), (14, 14), (4, 40), (6, 72), (18, 84), (40, 84)])),
             L(outline([(4, 40), (28, 44), (32, 80), (10, 78)]), 'shade', 'b', False),
             strand([(20, 20), (14, 70)], 'shade', 'b', 1.0), strand([(40, 6), (36, 70)], 'shade', 'b', 1.0),
             fringe([(64, 2), (88, 14), (96, 40), (94, 60, 1), (86, 48), (74, 40)])],
    'back': [L(outline([(10, 84), (4, 50), (12, 20), (34, 4), (62, 2), (84, 14), (96, 44), (96, 84), (70, 90), (30, 90)])),
             L(outline([(56, 4), (84, 18), (96, 50), (92, 84), (64, 90)]), 'shade', 'b', False),
             strand([(26, 16), (20, 84)], 'shade', 'b', 1.0), strand([(50, 4), (50, 88)], 'shade', 'b', 1.0), strand([(74, 16), (80, 84)], 'shade', 'b', 1.0)],
}

# Turner Fogg (el alienígena): cabeza calva crema muy grande en forma de huevo, orejas pequeñas y dos enormes manchas negras
# alrededor de los ojos rojos; sonrisa pequeña
_EGG_F = [(14, 70), (8, 40), (14, 10), (30, -10), (50, -16), (70, -10), (86, 10), (92, 40), (86, 70)]
CHARS['turner-fogg'] = {
    'body': 'normal', 'pal': pal('#f2e4c0', '#f8eccc', iris='#c81e1e', shade='#e0c8a8', socket='#2a1e2e', socket_l='#5a3a5a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline(_EGG_F), 'skin'), L(outline([(62, -6), (84, 10), (90, 40), (84, 64), (76, 30)]), 'shade', 'b', False),
              L(outline([(18, 70), (24, 60), (38, 62), (46, 74), (42, 88), (30, 92), (20, 84)]), 'socket', 'f', ln=True),
              L(outline([(82, 70), (76, 60), (62, 62), (54, 74), (58, 88), (70, 92), (80, 84)]), 'socket', 'f', ln=True),
              L(ell(34, 78, 5, 3), 'iris', 'f', False), L(ell(66, 78, 5, 3), 'iris', 'f', False),
              L([(22, 58), (16, 50)], 'socket', 'f', False, False, 1.6), L([(78, 58), (84, 50)], 'socket', 'f', False, False, 1.6)],
    'side': [L(outline([(50, 70), (40, 80), (20, 74), (6, 50), (8, 20), (24, -4), (50, -14), (74, -6), (88, 14), (92, 40), (90, 60)]), 'skin'),
             L(outline([(8, 30), (30, 26), (40, 60), (18, 70)]), 'shade', 'b', False),
             L(outline([(72, 64), (86, 62), (92, 74), (86, 88), (74, 84)]), 'socket', 'f', ln=True), L(ell(84, 76, 3, 2.6), 'iris', 'f', False)],
    'back': [L(outline(_EGG_F + [(70, 90), (30, 90)]), 'skin'), L(outline([(56, -10), (84, 10), (90, 50), (80, 84), (60, 90)]), 'shade', 'b', False)],
}

# Sid Viper: melena lisa rubio oscuro hasta la barbilla con raya en medio, dos mechones blancos en forma de colmillo
# bajando por la frente y otros dos junto a la boca; ojos rojos y una sonrisa ancha
CHARS['sid-viper'] = {
    'body': 'delgado', 'pal': pal('#c8b46a', '#f8dcb4', iris='#c81e1e', shade='#9a8648'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 104), (6, 70), (6, 30), (20, 8), (50, 0), (80, 8), (94, 30), (94, 70), (88, 104), (80, 100), (80, 64), (20, 64), (20, 100)])),
              L(outline([(60, 4), (86, 18), (94, 50), (90, 100), (82, 64)]), 'shade', 'b', False),
              fringe([(10, 74), (12, 36), (26, 14), (50, 6), (74, 14), (88, 36), (90, 74), (80, 64), (70, 48), (56, 44), (50, 56), (44, 44), (30, 48), (20, 64)]),
              L(outline([(30, 18), (24, 34), (32, 56), (36, 40)]), WHITE, 'f', ln=True), L(outline([(70, 18), (76, 34), (68, 56), (64, 40)]), WHITE, 'f', ln=True),
              L(outline([(22, 92), (28, 100), (30, 112)]), WHITE, 'f', ln=True), L(outline([(78, 92), (72, 100), (70, 112)]), WHITE, 'f', ln=True)],
    'side': [L(outline([(54, 76), (56, 56), (80, 48), (92, 30), (86, 10), (62, -2), (36, 0), (14, 14), (4, 40), (2, 80), (8, 104), (40, 104), (52, 96)])),
             L(outline([(4, 40), (28, 46), (36, 100), (10, 100)]), 'shade', 'b', False),
             fringe([(62, 2), (88, 14), (96, 40), (92, 60, 1), (84, 46), (72, 38)]),
             L(outline([(80, 20), (86, 34), (82, 52), (78, 36)]), WHITE, 'f', ln=True)],
    'back': [L(outline([(10, 104), (4, 70), (6, 30), (20, 8), (50, 0), (80, 8), (94, 30), (96, 70), (90, 104), (50, 108)])),
             L(outline([(56, 4), (86, 18), (96, 60), (92, 102), (64, 106)]), 'shade', 'b', False), strand([(50, 4), (50, 104)], 'shade', 'b', 1.0)],
}

# Dave Walker (fantasma): pelo blanco azulado muy claro que se arremolina como humo, con mechones ondulados que salen a los
# lados y un flequillo que le tapa los ojos menos un ojo rojo; piel morena
CHARS['dave-walker'] = {
    'body': 'normal', 'pal': pal('#d4ecf0', '#a87850', iris='#c81e1e', shade='#a8b4c0'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 80), (0, 76), (-14, 92, 1), (-8, 66), (2, 54), (-12, 50, 1), (6, 40), (10, 16), (30, 0), (46, -4), (54, -24, 1), (60, -4), (78, 2),
                         (94, 20), (98, 42), (114, 48, 1), (100, 58), (110, 82, 1), (92, 72), (84, 80), (82, 62), (18, 62)])),
              L(outline([(60, 0), (84, 12), (98, 40), (92, 70), (80, 40)]), 'shade', 'b', False),
              fringe([(12, 70), (14, 40), (30, 20), (50, 14), (70, 20), (86, 38), (88, 70), (78, 60), (72, 82, 1), (66, 62), (58, 84, 1), (52, 66), (42, 86, 1),
                      (36, 66), (26, 82, 1), (20, 66)]),
              L(ell(60, 78, 3, 2.4), 'iris', 'f', False)],
    'side': [L(outline([(56, 60), (62, 48), (80, 44), (92, 28), (84, 6), (62, -4), (54, -24, 1), (42, -2), (20, 4), (6, 22), (-12, 22, 1), (2, 40), (-14, 60, 1),
                        (2, 62), (-6, 82, 1), (14, 76), (16, 92, 1), (30, 78), (44, 72)])),
             L(outline([(4, 30), (26, 40), (28, 70), (8, 62)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 16), (96, 40), (96, 70, 1), (86, 54), (84, 76, 1), (76, 50), (66, 34)])],
    'back': [L(outline([(16, 84), (-2, 82), (-14, 96, 1), (-8, 70), (2, 56), (-12, 50, 1), (6, 40), (10, 16), (30, 0), (46, -4), (54, -24, 1), (60, -4), (78, 2),
                        (94, 20), (98, 42), (114, 48, 1), (100, 58), (112, 84, 1), (92, 80), (84, 88), (50, 94)])),
             L(outline([(56, 0), (84, 12), (100, 44), (94, 80), (64, 90)]), 'shade', 'b', False),
             strand([(30, 20), (50, 40), (40, 70)], 'shade', 'b', 1.2), strand([(70, 20), (60, 50), (70, 80)], 'shade', 'b', 1.2)],
}

# Porphyria Filia: pelo lila que le envuelve la cabeza como una capucha, con una trenza larga que cae por delante del
# hombro; cara pálida de ojos rasgados con sombra verde y labios verdes, un lunar en la frente
CHARS['porphyria-filia'] = {
    'body': 'chica', 'pal': pal('#c0b0dc', '#fcecc0', iris='#3a3a6a', shade='#9a8ab8', lid='#2a8a7a', mouth='#2a8a7a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'lips', 'mouth_y': 100, 'mouth_w': 5, 'hairline': False},
    'front': [L(outline([(10, 100), (2, 60), (8, 24), (28, 4), (50, -2), (72, 4), (92, 24), (98, 60), (90, 100), (80, 112), (60, 118), (40, 118), (20, 112)])),
              L(outline([(60, 2), (86, 18), (96, 56), (88, 100), (80, 50)]), 'shade', 'b', False),
              fringe([(14, 80), (16, 44), (30, 26), (44, 20), (50, 34), (56, 20), (70, 26), (84, 44), (86, 80), (80, 100), (66, 112), (60, 108), (78, 92), (80, 60),
                      (70, 40), (50, 46), (30, 40), (20, 60), (22, 92), (40, 108), (34, 112), (20, 100)]),
              L(ell(50, 60, 1.6, 1.6), OUTC, 'f', False), L(ell(38, 76, 7, 4), 'lid', 'b', False), L(ell(62, 76, 7, 4), 'lid', 'b', False)],
    'side': [L(outline([(54, 76), (58, 56), (80, 50), (94, 30), (86, 8), (62, -4), (34, -2), (12, 14), (2, 44), (4, 80), (20, 98), (44, 96)])),
             L(outline([(4, 44), (28, 48), (34, 92), (12, 90)]), 'shade', 'b', False),
             L(outline([(54, 92), (62, 100), (58, 110), (66, 118), (60, 128), (66, 136, 1), (52, 128), (54, 116), (48, 106), (50, 96)]), 'mid', 'f', ln=True),
             fringe([(62, 2), (88, 14), (96, 40), (94, 70, 1), (86, 52), (74, 40)])],
    'back': [L(outline([(10, 100), (2, 60), (8, 24), (28, 4), (50, -2), (72, 4), (92, 24), (98, 60), (90, 100), (70, 110), (50, 104, 1), (30, 110)])),
             L(outline([(56, 2), (86, 18), (98, 60), (90, 100), (64, 106)]), 'shade', 'b', False),
             strand([(30, 10), (22, 90)], 'shade', 'b', 1.0), strand([(50, 0), (50, 100)], 'shade', 'b', 1.0), strand([(70, 10), (78, 90)], 'shade', 'b', 1.0)],
}

# Hugh Mumford (la momia): la cabeza entera envuelta en vendas pardas que le tapan hasta la nariz, y por arriba asoma un
# pelo rubio crema peinado hacia atrás; boca apretada
CHARS['hugh-mumford'] = {
    'body': 'normal', 'pal': pal('#f0e4b4', '#d8946a', iris='#2a1e1a', shade='#c8b88a', band='#b8a888', band_d='#8a7a5a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(10, 70), (6, 40), (14, 14), (32, 0), (50, -4), (68, 0), (86, 14), (94, 40), (90, 70)])),
              L(outline([(10, 84), (8, 40), (24, 34), (50, 30), (76, 34), (92, 40), (92, 84), (70, 90), (50, 86), (30, 90)]), 'band', 'f', ln=True),
              L(outline([(12, 36), (30, 20), (40, 34), (34, 50), (20, 54)]), 'mid', 'f'), L(outline([(88, 36), (70, 20), (60, 34), (66, 50), (80, 54)]), 'mid', 'f'),
              L(outline([(30, 20), (50, 12), (70, 20), (60, 34), (50, 26), (40, 34)]), 'mid', 'f'),
              strand([(10, 50), (90, 60)], 'band_d', 'f', 1.0), strand([(10, 64), (90, 54)], 'band_d', 'f', 1.0), strand([(10, 76), (90, 74)], 'band_d', 'f', 1.0),
              strand([(30, 40), (70, 84)], 'band_d', 'f', 1.0)],
    'side': [L(outline([(52, 72), (56, 56), (80, 48), (92, 30), (84, 8), (62, -4), (36, 0), (14, 14), (4, 40), (6, 70), (18, 90), (40, 90)]), 'band'),
             L(outline([(8, 30), (20, 6), (50, -6), (80, 2), (92, 20), (70, 20), (50, 26), (24, 30)]), 'mid', 'f', ln=True),
             L(outline([(40, 30), (54, 22), (60, 34), (48, 40)]), 'mid', 'f'),
             strand([(4, 50), (90, 46)], 'band_d', 'f', 1.0), strand([(6, 66), (88, 64)], 'band_d', 'f', 1.0), strand([(10, 80), (60, 76)], 'band_d', 'f', 1.0)],
    'back': [L(outline([(10, 84), (6, 40), (14, 14), (32, 0), (50, -4), (68, 0), (86, 14), (94, 40), (90, 84), (70, 92), (30, 92)]), 'band'),
             L(outline([(10, 34), (18, 12), (36, 0), (50, -4), (64, 0), (82, 12), (90, 34), (70, 28), (50, 32), (30, 28)]), 'mid', 'f', ln=True),
             strand([(8, 50), (92, 60)], 'band_d', 'f', 1.0), strand([(8, 66), (92, 54)], 'band_d', 'f', 1.0), strand([(10, 80), (90, 76)], 'band_d', 'f', 1.0)],
}

# Desmodus Drakul: melena larga lisa gris verdoso muy claro que le cae hasta el pecho con mechones ondulados, raya a un
# lado con un zigzag; ojos verdes afilados de pestaña larga
CHARS['desmodus-drakul'] = {
    'body': 'delgado', 'pal': pal('#c8d4cc', '#fce4cc', iris='#5aa87a', shade='#9aaaa0'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 126), (2, 110), (4, 80), (0, 50), (8, 20), (28, 2), (50, -4), (72, 2), (92, 20), (100, 50), (96, 80), (98, 110), (88, 126), (82, 100),
                         (82, 64), (18, 64), (18, 100)])),
              L(outline([(60, 2), (86, 16), (98, 50), (94, 112), (84, 110), (80, 50)]), 'shade', 'b', False),
              fringe([(10, 80), (10, 44), (24, 20), (44, 10), (60, 12), (76, 20), (90, 40), (90, 80), (84, 70), (80, 52), (70, 40), (60, 42), (48, 52), (36, 58),
                      (26, 72), (18, 96)]),
              L(quad((62, 14), (68, 22), (64, 30)) + quad((64, 30), (70, 36), (66, 44))[1:], OUTC, 'f', False, False, 1.0),
              L(outline([(14, 70), (4, 96), (6, 126, 1), (18, 108), (24, 128, 1), (26, 96), (24, 74)]), 'mid', 'f', ln=True),
              L(outline([(86, 70), (96, 96), (94, 126, 1), (82, 108), (76, 128, 1), (74, 96), (76, 74)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(54, 76), (58, 56), (80, 48), (92, 30), (86, 8), (62, -4), (34, -2), (12, 14), (2, 44), (-2, 90), (4, 128, 1), (20, 116), (34, 128, 1),
                        (44, 108), (52, 92)])),
             L(outline([(2, 44), (26, 48), (34, 110), (8, 114)]), 'shade', 'b', False),
             strand([(14, 40), (10, 120)], 'shade', 'b', 1.0), strand([(30, 30), (34, 112)], 'shade', 'b', 1.0),
             fringe([(62, 2), (88, 14), (96, 40), (92, 64, 1), (84, 48), (72, 38)])],
    'back': [L(outline([(12, 128), (2, 110), (4, 80), (0, 50), (8, 20), (28, 2), (50, -4), (72, 2), (92, 20), (100, 50), (96, 80), (98, 110), (88, 128), (70, 134),
                        (50, 128), (30, 134)])),
             L(outline([(56, 2), (86, 16), (100, 60), (96, 124), (66, 130), (68, 50)]), 'shade', 'b', False),
             strand([(30, 20), (22, 124)], 'shade', 'b', 1.0), strand([(50, 4), (50, 128)], 'shade', 'b', 1.0), strand([(70, 20), (78, 124)], 'shade', 'b', 1.0)],
}

# Woodrow Stake: pelo rubio verdoso ondulado peinado hacia un lado, con un mechón que le tapa el ojo derecho y puntas
# rizadas hacia fuera a los lados y en la nuca; ojo verde azulado
CHARS['woodrow-stake'] = {
    'body': 'normal', 'pal': pal('#d8d0a0', '#fce4c4', iris='#3a8a9a', shade='#a8a07a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 90), (-2, 84, 1), (6, 70), (-6, 58, 1), (6, 50), (4, 24), (22, 4), (50, -4), (74, 4), (94, 20), (98, 44), (108, 56, 1), (96, 62),
                         (104, 80, 1), (88, 82), (84, 64), (18, 64)])),
              L(outline([(60, 2), (86, 14), (98, 44), (92, 78), (80, 50)]), 'shade', 'b', False),
              fringe([(12, 70), (12, 40), (24, 18), (46, 8), (70, 12), (88, 30), (90, 60), (82, 50), (74, 42), (64, 48), (56, 54), (48, 64), (44, 88), (36, 102, 1),
                      (28, 92), (18, 82)]),
              strand([(30, 20), (60, 14)], 'shade', 'f', 1.0), strand([(24, 40), (56, 30)], 'shade', 'f', 1.0)],
    'side': [L(outline([(54, 62), (58, 50), (80, 46), (92, 30), (86, 8), (62, -4), (34, -2), (12, 12), (2, 36), (-8, 50, 1), (4, 56), (-2, 76, 1), (12, 76), (14, 92, 1),
                        (26, 82), (40, 86, 1), (44, 72)])),
             L(outline([(4, 34), (26, 40), (30, 76), (10, 72)]), 'shade', 'b', False),
             fringe([(62, 2), (88, 14), (96, 40), (92, 60, 1), (84, 46), (72, 36)])],
    'back': [L(outline([(14, 88), (-4, 84, 1), (6, 70), (-6, 58, 1), (6, 50), (4, 24), (22, 4), (50, -4), (78, 4), (96, 24), (96, 50), (108, 58, 1), (96, 70),
                        (104, 84, 1), (86, 88), (70, 94), (60, 88), (50, 96, 1), (40, 88), (30, 94)])),
             L(outline([(56, 2), (86, 16), (98, 50), (92, 84), (64, 90)]), 'shade', 'b', False),
             strand([(50, 4), (40, 40), (50, 80)], 'shade', 'b', 1.0)],
}

# Nora Flexion: pelo rubio claro con dos coletas altas tiesas como orejas de conejo, una diadema negra ancha con triángulos
# blancos en lo alto y mechones largos junto a la cara; ojos verdes grandes
CHARS['nora-flexion'] = {
    'body': 'chica', 'pal': pal('#f4e8b8', '#fce8cc', iris='#3a9a5a', shade='#d8c48a', band='#1e1e22', tie='#3a7a3a'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(22, 26), (6, 10), (-12, -18), (-6, -26), (14, -18), (30, 8)])), L(outline([(78, 26), (94, 10), (112, -18), (106, -26), (86, -18), (70, 8)])),
              L(outline([(0, -14), (12, -16), (20, 4), (10, 4)]), 'shade', 'b', False), L(outline([(100, -14), (88, -16), (80, 4), (90, 4)]), 'shade', 'b', False),
              L(outline([(12, 76), (8, 44), (14, 20), (32, 6), (50, 2), (68, 6), (86, 20), (92, 44), (88, 76), (82, 60), (18, 60)])),
              L(outline([(14, 60), (10, 80), (12, 100, 1), (22, 84), (22, 64)]), 'mid', 'f', ln=True),
              L(outline([(86, 60), (90, 80), (88, 100, 1), (78, 84), (78, 64)]), 'mid', 'f', ln=True),
              fringe([(14, 64), (16, 44), (30, 36), (50, 34), (70, 36), (84, 44), (86, 64), (78, 56), (70, 66, 1), (64, 52), (56, 72, 1), (50, 50), (44, 70, 1), (38, 50),
                      (30, 64, 1), (22, 54)]),
              L(outline([(10, 42), (14, 18), (32, 6), (50, 2), (68, 6), (86, 18), (90, 42), (70, 34), (50, 32), (30, 34)]), 'band', 'f', ln=True),
              L(outline([(26, 32), (34, 14), (42, 30)]), WHITE, 'f', False), L(outline([(42, 30), (50, 10), (58, 30)]), WHITE, 'f', False),
              L(outline([(58, 30), (66, 14), (74, 32)]), WHITE, 'f', False)],
    'side': [L(outline([(36, 14), (20, -10), (4, -32), (14, -34), (34, -14), (46, 8)])),
             L(outline([(54, 62), (58, 50), (80, 46), (92, 30), (86, 10), (64, -2), (36, 0), (14, 14), (6, 38), (8, 64), (20, 78), (40, 76)])),
             L(outline([(4, 34), (26, 40), (30, 70), (10, 66)]), 'shade', 'b', False),
             L(outline([(40, 10), (48, 4), (52, 14), (44, 18)]), 'tie', 'f', ln=True),
             L(outline([(54, 6), (72, 2), (90, 20), (96, 40), (84, 36), (72, 22), (58, 18)]), 'band', 'f', ln=True),
             L(outline([(66, 8), (78, 12), (72, 22)]), WHITE, 'f', False),
             L(outline([(86, 40), (92, 60), (88, 80, 1), (82, 60)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(22, 30), (6, 12), (-12, -18), (-6, -26), (14, -18), (30, 10)])), L(outline([(78, 30), (94, 12), (112, -18), (106, -26), (86, -18), (70, 10)])),
             L(outline([(20, 28), (16, 18), (28, 12), (30, 22)]), 'tie', 'f', ln=True), L(outline([(80, 28), (84, 18), (72, 12), (70, 22)]), 'tie', 'f', ln=True),
             L(outline([(12, 80), (8, 44), (14, 20), (32, 6), (50, 2), (68, 6), (86, 20), (92, 44), (88, 80), (70, 88), (30, 88)])),
             L(outline([(56, 4), (86, 18), (92, 50), (86, 80), (64, 86)]), 'shade', 'b', False),
             L(outline([(14, 70), (10, 90), (12, 104, 1), (20, 88), (22, 74)]), 'mid', 'f', ln=True),
             L(outline([(86, 70), (90, 90), (88, 104, 1), (80, 88), (78, 74)]), 'mid', 'f', ln=True)],
}
