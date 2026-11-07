"""Earth Eleven (gx-earth-eleven): sus modelos 3D de Inazuma Eleven GO Galaxy como referencia (busto de frente, perfil y espalda).

Versiones según la tabla de miembros de Galaxy de la wiki ("Earth Eleven") y los sprites "(EE) ... sprite":
- Tenma, Shindou, Tsurugi y Shinsuke tienen en Galaxy el mismo peinado que en GO: usan los dibujos del Raimon de GO.
- Kusaka (buddy-fury) con su gorro de lana; su variante buddy-fury-gx-kusaka-b es la forma Berserker (sin gorro, melena
  erizada y ojos rojos; sprite "(EE) Kusaka Ryuuji sprite (berserk)").
- Matatagi: la base es la forma Dark Side (mechones azules) y falco-flashman-gx-matatagi-p, la Pleasing (sin mechones).
- zack-avalon es Ichikawa Zanakurou (no Zanark): su modelo de Galaxy.
- maneuver-gibbs juega en el equipo disfrazado de Tsurugi (el falso Tsurugi de la wiki, "FakeTsurugi"): orejas de elfo,
  ojos morados y una coleta larga detrás.
"""
import copy

from chars import CHARS, L, OUTC, bumpy, ell, messy, outline, pal, strand  # noqa: F401
from heads import quad  # noqa: F401

T = 'gx-earth-eleven'
WHITE = (250, 250, 250, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Ibuki Munemasa (portero): pelo blanco de pinchos revueltos que le cae hasta la mandíbula, una cinta negra en la frente bajo
# el flequillo y ojos morados afilados
CHARS['terry-archibald'] = {
    'body': 'normal', 'pal': pal('#e6e2e8', '#f8c89a', iris='#7a4a8a', shade='#b4a0ac', deep='#94808c', band='#1e1c22'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 96), (4, 84, 1), (8, 70), (-10, 58, 1), (4, 50), (-8, 30, 1), (8, 26), (2, 6, 1), (20, 10), (24, -14, 1), (36, 0), (48, -22, 1),
                         (56, -2), (70, -18, 1), (74, 2), (92, -4, 1), (90, 18), (108, 22, 1), (96, 36), (110, 52, 1), (96, 58), (104, 78, 1), (90, 80), (88, 96, 1),
                         (82, 70), (18, 70)])),
              L(outline([(60, 2), (86, 10), (100, 36), (94, 72), (82, 46)]), 'shade', 'b', False),
              L(outline([(-6, 30), (8, 26), (14, 50), (4, 50)]), 'shade', 'b', False), L(outline([(24, -12), (36, 0), (30, 12), (22, 8)]), 'shade', 'b', False),
              L(outline([(14, 62), (14, 52), (50, 48), (86, 52), (86, 62), (50, 58)]), 'band', 'f', ln=True),
              fringe([(12, 54), (16, 30), (30, 16), (50, 12), (70, 16), (86, 30), (88, 54), (80, 48), (72, 62, 1), (64, 48), (54, 48), (44, 66, 1), (38, 48),
                      (28, 50), (22, 62, 1), (18, 50)]),
              strand([(36, 20), (30, 40)], 'shade', 'f', 1.0), strand([(62, 18), (68, 40)], 'shade', 'f', 1.0),
              L(outline([(14, 60), (10, 84), (16, 96, 1), (20, 80), (22, 64)]), 'mid', 'f'), L(outline([(86, 60), (90, 84), (84, 96, 1), (80, 80), (78, 64)]), 'mid', 'f')],
    'side': [L(outline([(56, 60), (62, 48), (80, 46), (94, 36), (92, 16), (100, 4, 1), (80, 2), (74, -18, 1), (58, -4), (40, -22, 1), (32, 0), (8, -6, 1), (14, 14),
                        (-12, 22, 1), (4, 36), (-14, 52, 1), (4, 58), (-8, 76, 1), (10, 76), (2, 96, 1), (20, 88), (24, 104, 1), (34, 88), (46, 78)])),
             L(outline([(4, 36), (26, 42), (30, 86), (10, 84)]), 'shade', 'b', False),
             L(outline([(60, 54), (92, 54), (94, 62), (60, 62)]), 'band', 'f', ln=True),
             fringe([(64, 2), (90, 16), (98, 40), (96, 70, 1), (88, 54), (82, 66, 1), (76, 44), (64, 30)])],
    'back': [L(outline([(14, 96), (2, 86, 1), (6, 70), (-10, 58, 1), (4, 48), (-8, 30, 1), (8, 26), (2, 6, 1), (20, 10), (24, -14, 1), (36, 0), (48, -22, 1),
                        (56, -2), (70, -18, 1), (74, 2), (92, -4, 1), (90, 18), (108, 22, 1), (96, 36), (110, 52, 1), (96, 58), (104, 82, 1), (88, 96), (74, 104, 1),
                        (62, 94), (50, 106, 1), (38, 94), (26, 104, 1)])),
             L(outline([(56, 2), (86, 10), (100, 40), (94, 90), (66, 98), (70, 50)]), 'shade', 'b', False),
             strand([(30, 20), (24, 60), (30, 92)], 'deep', 'b', 1.0), strand([(70, 20), (76, 60), (70, 92)], 'deep', 'b', 1.0)],
}

# Morimura Konoha: bajita, de carita redonda con coloretes; pelo verde oscuro con raya en medio, liso sobre la frente y
# recogido a los lados en dos moños enormes y esponjosos como nubes
_puffs = lambda z='b': [L(bumpy(0, 72, 26, 30, 9, 0.08), 'mid', z), L(bumpy(100, 72, 26, 30, 9, 0.08), 'mid', z),
                        L(outline([(98, 44), (118, 52), (124, 80), (110, 96), (100, 70)]), 'shade', z, False),
                        L(outline([(-2, 44), (-20, 56), (-22, 76), (-12, 92), (-6, 66)]), 'light', z, False)]
CHARS['trina-verdure'] = {
    'body': 'bajito', 'pal': pal('#2e5a2a', '#f8d0a8', iris='#1e1414', shade='#1e3e1c', light='#4a7a42', blush='#f4a0a0'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': _puffs() + [L(outline([(14, 66), (12, 36), (24, 16), (50, 8), (76, 16), (88, 36), (86, 66), (80, 52), (20, 52)])),
                         fringe([(14, 56), (16, 34), (30, 18), (50, 12), (70, 18), (84, 34), (86, 56), (74, 46), (60, 42), (50, 34), (40, 42), (26, 46)]),
                         strand([(50, 14), (50, 34)], 'shade', 'f', 1.2),
                         L(ell(30, 90, 5, 2.6), 'blush', 'f', False), L(ell(70, 90, 5, 2.6), 'blush', 'f', False)],
    'side': [L(outline([(28, 52), (14, 40), (-4, 44), (-16, 60), (-14, 82), (-2, 96), (16, 98), (30, 88), (34, 70)]), 'mid', 'b'),
             L(outline([(54, 60), (58, 48), (80, 46), (92, 32), (86, 12), (64, 0), (36, 0), (14, 12), (4, 34), (8, 60), (20, 72), (36, 72), (46, 66)])),
             L(outline([(-4, 50), (-14, 64), (-10, 86), (4, 94), (2, 70)]), 'shade', 'b', False),
             fringe([(64, 4), (88, 16), (94, 38), (90, 50, 1), (80, 42), (70, 34)]),
             L(ell(86, 90, 4, 2.4), 'blush', 'f', False)],
    'back': [L(outline([(14, 74), (10, 36), (22, 14), (50, 6), (78, 14), (90, 36), (86, 74), (50, 80)])),
             L(outline([(56, 8), (84, 18), (90, 50), (84, 72), (62, 78)]), 'shade', 'b', False),
             strand([(50, 8), (50, 76)], 'deep', 'b', 1.2)] + _puffs('f'),
}

# Minaho Kazuto: pelo naranja de pinchos largos que se abren hacia los lados y hacia arriba, con flequillo de mechones
# entre los ojos; ojos grandes verdes y cara seria
CHARS['keenan-sharpe'] = {
    'body': 'normal', 'pal': pal('#f2901e', '#fcdcc0', iris='#2a8a6a', shade='#b85a14', deep='#8a4010'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 66), (10, 50), (-12, 22, 1), (8, 30), (0, 4, 1), (16, 12), (14, -14, 1), (30, 2), (50, -6), (70, 0), (92, -14, 1), (88, 8), (106, 2, 1),
                         (94, 26), (112, 20, 1), (92, 46), (86, 66), (80, 52), (20, 52)])),
              L(outline([(60, -2), (84, 4), (96, 26), (88, 58), (78, 36)]), 'shade', 'b', False),
              fringe([(12, 62), (14, 38), (28, 18), (50, 10), (72, 18), (86, 38), (88, 62), (80, 50), (74, 60, 1), (68, 44), (58, 56, 1), (54, 42), (48, 68, 1),
                      (42, 44), (34, 58, 1), (28, 46), (20, 62, 1)]),
              L(outline([(56, 14), (76, 22), (84, 40), (72, 36)]), 'shade', 'f', False)],
    'side': [L(outline([(54, 62), (58, 50), (80, 48), (92, 34), (90, 14), (74, -2), (62, -6), (54, -30, 1), (42, -8), (30, -26, 1), (24, 0), (12, 10), (4, 30),
                        (-14, 46, 1), (8, 54), (14, 76), (30, 82), (46, 74)])),
             L(outline([(8, 30), (28, 38), (30, 70), (12, 60)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 18), (94, 42), (92, 64, 1), (84, 48), (78, 58, 1), (74, 40), (66, 30)])],
    'back': [L(outline([(16, 74), (12, 50), (-14, 30, 1), (10, 36), (-6, 6, 1), (16, 14), (12, -14, 1), (32, 2), (50, -4), (68, 2), (88, -14, 1), (84, 14), (106, 6, 1),
                        (90, 36), (114, 30, 1), (88, 50), (84, 74), (66, 84), (50, 94, 1), (34, 84)])),
             L(outline([(56, 0), (84, 10), (92, 40), (84, 72), (62, 82)]), 'shade', 'b', False)],
}

# Manabe Jinichirou: melena corta lila rosada en casco, abultada arriba, con las puntas de los lados vueltas hacia fuera a la
# altura de los ojos y de la boca; gafas finas rectangulares
CHARS['zippy-lerner'] = {
    'body': 'normal', 'pal': pal('#c8a0b4', '#fcdcc0', iris='#6a5a5a', shade='#9a7086', deep='#7a5468'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False, 'glasses': OUTC, 'glasses_rect': True},
    'front': [L(outline([(14, 96), (2, 92, 1), (10, 84), (8, 64), (-6, 58, 1), (6, 50), (4, 24), (20, 2), (50, -10), (80, 2), (96, 24), (94, 50), (106, 58, 1), (92, 64),
                         (90, 84), (98, 92, 1), (86, 96), (82, 66), (18, 66)])),
              L(outline([(60, -6), (84, 4), (96, 30), (92, 80), (82, 50)]), 'shade', 'b', False),
              fringe([(10, 66), (10, 40), (22, 18), (50, 8), (78, 18), (90, 40), (90, 66), (82, 54), (76, 64, 1), (70, 46), (60, 58, 1), (56, 42), (48, 62, 1),
                      (42, 44), (34, 60, 1), (28, 46), (18, 62, 1)]),
              L(outline([(28, 14), (44, 10), (38, 20)]), 'light', 'f', False)],
    'side': [L(outline([(54, 62), (58, 50), (80, 48), (94, 34), (88, 8), (64, -8), (34, -8), (12, 6), (0, 32), (-2, 60), (-10, 66, 1), (2, 74), (4, 96), (-6, 102, 1),
                        (14, 104), (30, 96), (42, 100, 1), (46, 82)])),
             L(outline([(0, 40), (24, 44), (32, 92), (8, 92)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 42), (94, 64, 1), (86, 50), (80, 60, 1), (76, 42), (64, 30)])],
    'back': [L(outline([(12, 96), (2, 98, 1), (6, 80), (2, 62), (-10, 56, 1), (4, 50), (4, 24), (20, 2), (50, -10), (80, 2), (96, 24), (96, 50), (110, 56, 1), (98, 62),
                        (94, 80), (98, 98, 1), (86, 96), (72, 104, 1), (60, 96), (50, 104, 1), (40, 96), (28, 104, 1)])),
             L(outline([(56, -6), (84, 4), (98, 40), (94, 94), (68, 100), (70, 50)]), 'shade', 'b', False)],
}

# Tetsukado Shin: piel morena y rastas granates con franjas turquesa recogidas sobre la cabeza, que le caen por los lados
# hasta la mandíbula; una rasta enroscada como una antena en lo alto; ojos azules y cejas fruncidas
_dread = lambda p0, c, p1, w=6: L(quad(p0, c, p1), 'mid', 'b', False, False, w)
CHARS['frank-foreman'] = {
    'body': 'normal', 'pal': pal('#7a262c', '#b4744c', iris='#2a7ab8', shade='#5a1a20', teal='#3a8a9a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [_dread((20, 40), (10, 70), (14, 100)), _dread((30, 30), (16, 64), (22, 96)), _dread((80, 40), (90, 70), (86, 100)), _dread((70, 30), (84, 64), (78, 96)),
              L(outline([(16, 52), (14, 30), (26, 10), (42, 0), (58, 0), (74, 10), (86, 30), (84, 52), (66, 34), (50, 60, 1), (34, 34)])),
              L(outline([(36, 8), (44, 2), (46, 40), (40, 40)]), 'teal', 'f', False), L(outline([(64, 8), (56, 2), (54, 40), (60, 40)]), 'teal', 'f', False),
              strand([(26, 16), (30, 40)], 'shade', 'f', 1.4), strand([(74, 16), (70, 40)], 'shade', 'f', 1.4),
              L(quad((48, 2), (36, -20), (50, -30)), 'mid', 'b', False, False, 4.0), L(quad((50, -30), (64, -24), (54, -12)), 'mid', 'b', False, False, 4.0),
              L(quad((52, 2), (58, -10), (54, -12)), 'mid', 'b', False, False, 4.0)],
    'side': [_dread((30, 40), (14, 70), (16, 100)), _dread((40, 30), (24, 66), (28, 96)), _dread((20, 50), (4, 80), (6, 104)),
             L(outline([(56, 52), (64, 40), (84, 36), (88, 20), (72, 4), (48, -2), (24, 6), (10, 24), (8, 50), (20, 62), (40, 56)])),
             L(outline([(30, 6), (60, 2), (62, 10), (32, 14)]), 'teal', 'f', False),
             L(quad((44, 0), (34, -22), (48, -32)), 'mid', 'b', False, False, 4.0), L(quad((48, -32), (62, -26), (52, -14)), 'mid', 'b', False, False, 4.0)],
    'back': [_dread((16, 40), (6, 70), (12, 100)), _dread((30, 50), (24, 80), (30, 104)), _dread((50, 56), (48, 84), (52, 106)), _dread((70, 50), (76, 80), (70, 104)),
             _dread((84, 40), (94, 70), (88, 100)),
             L(outline([(14, 60), (12, 30), (26, 8), (50, 0), (74, 8), (88, 30), (86, 60), (70, 76), (50, 80), (30, 76)]), 'teal'),
             L(outline([(56, 4), (82, 14), (88, 46), (76, 70), (60, 76)]), (40, 110, 124, 255), 'b', False),
             L(quad((48, 2), (36, -20), (50, -30)), 'mid', 'b', False, False, 4.0), L(quad((50, -30), (64, -24), (54, -12)), 'mid', 'b', False, False, 4.0)],
}

# Kusaka Ryuuji: grandullón de piel morena con un gorro de lana marrón oscuro calado hasta las cejas y una melena larga y
# ondulada castaña clara que le cae hasta los hombros en rizos gruesos; ojos cerrados de sonrisa
_kus_hair_f = [L(outline([(12, 60), (2, 80), (-10, 96), (-14, 112, 1), (2, 108), (6, 120, 1), (18, 106), (24, 86), (22, 64)])),
               L(outline([(88, 60), (98, 80), (110, 96), (114, 112, 1), (98, 108), (94, 120, 1), (82, 106), (76, 86), (78, 64)])),
               L(outline([(98, 84), (112, 100), (100, 106), (88, 96)]), 'shade', 'b', False), L(outline([(2, 84), (-12, 100), (0, 106), (12, 96)]), 'shade', 'b', False)]
CHARS['buddy-fury'] = {
    'body': 'delgado', 'pal': pal('#b08e68', '#c8986a', iris='#1e1414', shade='#8a6a4a', hat='#3e2a1e', hat_d='#2a1c14'),
    'face': {'eyes': 'closed', 'brows': True, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': _kus_hair_f + [L(outline([(12, 58), (12, 30), (24, 10), (50, 2), (76, 10), (88, 30), (88, 58), (50, 54)]), 'hat', 'f', ln=True),
                            L(outline([(60, 6), (80, 16), (88, 40), (86, 56), (72, 54)]), 'hat_d', 'f', False),
                            strand([(18, 50), (50, 46), (82, 50)], 'hat_d', 'f', 1.4)],
    'side': [L(outline([(40, 56), (20, 62), (0, 74), (-14, 96), (-12, 116, 1), (2, 106), (8, 120, 1), (20, 106), (30, 96), (40, 84), (46, 66)])),
             L(outline([(-4, 84), (-12, 104), (2, 104), (14, 92)]), 'shade', 'b', False),
             L(outline([(96, 50), (94, 28), (78, 8), (50, 0), (24, 6), (8, 24), (4, 48), (14, 58), (50, 56)]), 'hat', 'f', ln=True),
             L(outline([(14, 38), (-8, 34), (-12, 46, 1), (6, 50)]), 'hat', 'f', ln=True)],
    'back': [L(outline([(12, 56), (0, 74), (-12, 92), (-16, 112, 1), (2, 106), (8, 120, 1), (22, 110), (36, 118, 1), (50, 108), (64, 118, 1), (78, 110), (92, 120, 1),
                        (98, 106), (116, 112, 1), (112, 92), (100, 74), (88, 56)])),
             L(outline([(56, 60), (88, 60), (104, 84), (110, 108), (80, 110), (70, 80)]), 'shade', 'b', False),
             L(outline([(12, 62), (12, 30), (24, 10), (50, 2), (76, 10), (88, 30), (88, 62), (50, 66)]), 'hat', 'f', ln=True),
             L(outline([(60, 6), (80, 16), (88, 40), (88, 62), (66, 64)]), 'hat_d', 'f', False)],
}

# Kusaka en forma Berserker: sin gorro, la melena clara se le eriza en mechones salvajes por todas partes hasta los hombros;
# ojos rojos y gesto de rabia
CHARS[f'{T}:buddy-fury-gx-kusaka-b'] = {
    'body': 'delgado', 'pal': pal('#d8c8ae', '#c8986a', iris='#c81e1e', shade='#a8967e', deep='#86766a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 100), (-8, 112, 1), (2, 92), (-16, 80, 1), (0, 70), (-14, 52, 1), (2, 46), (-6, 24, 1), (12, 22), (12, -2, 1), (28, 8), (36, -16, 1),
                         (48, 2), (62, -18, 1), (68, 2), (88, -6, 1), (88, 18), (108, 22, 1), (98, 42), (116, 52, 1), (100, 66), (116, 80, 1), (98, 90), (108, 112, 1),
                         (86, 100), (82, 66), (18, 66)])),
              L(outline([(60, 2), (88, 14), (106, 50), (104, 96), (84, 70)]), 'shade', 'b', False),
              fringe([(12, 64), (14, 38), (28, 18), (50, 12), (72, 18), (86, 38), (88, 64), (80, 50), (74, 62, 1), (66, 44), (58, 58, 1), (54, 42), (48, 70, 1),
                      (42, 44), (34, 60, 1), (28, 46), (20, 64, 1)]),
              strand([(30, 22), (22, 50)], 'shade', 'f', 1.0), strand([(70, 22), (78, 50)], 'shade', 'f', 1.0)],
    'side': [L(outline([(54, 62), (58, 50), (80, 48), (94, 34), (92, 14), (102, 0, 1), (80, 2), (72, -18, 1), (56, -2), (36, -18, 1), (28, 2), (4, -4, 1), (10, 16),
                        (-14, 24, 1), (2, 40), (-18, 54, 1), (0, 62), (-16, 82, 1), (4, 84), (-4, 104, 1), (14, 96), (18, 114, 1), (30, 98), (40, 104, 1), (46, 82)])),
             L(outline([(0, 40), (24, 46), (32, 94), (8, 92)]), 'shade', 'b', False),
             fringe([(64, 4), (90, 18), (96, 42), (94, 66, 1), (86, 50), (80, 62, 1), (76, 42), (64, 30)])],
    'back': [L(outline([(14, 104), (-8, 112, 1), (0, 92), (-18, 80, 1), (-2, 68), (-16, 50, 1), (2, 44), (-6, 22, 1), (12, 20), (12, -2, 1), (28, 8), (36, -16, 1),
                        (48, 2), (62, -18, 1), (68, 2), (88, -6, 1), (88, 18), (108, 22, 1), (98, 44), (118, 50, 1), (102, 68), (118, 80, 1), (100, 92), (108, 112, 1),
                        (86, 104), (72, 118, 1), (60, 104), (48, 120, 1), (36, 104), (26, 116, 1)])),
             L(outline([(56, 2), (88, 14), (106, 50), (104, 100), (70, 108), (72, 50)]), 'shade', 'b', False),
             strand([(28, 20), (20, 60), (26, 100)], 'deep', 'b', 1.0), strand([(72, 20), (80, 60), (74, 100)], 'deep', 'b', 1.0)],
}

# Nozaki Sakura: pelo rosa trenzado alrededor de la cabeza con un moño en forma de flor de cerezo en lo alto y dos mechones
# finos junto a las orejas; ojos grandes azules y coloretes
CHARS['cerise-blossom'] = {
    'body': 'chica', 'pal': pal('#ec8c9c', '#fce0c8', iris='#3a8ac0', shade='#c46a7c', light='#f8b8c4', blush='#f8a8a8'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(36, 6), (30, -10), (40, -8), (44, -24, 1), (50, -10), (60, -22, 1), (62, -8), (74, -10), (66, 4), (50, 10)])),
              L(outline([(44, -6), (50, -18), (56, -6)]), 'light', 'b', False),
              L(outline([(14, 66), (12, 34), (26, 12), (50, 4), (74, 12), (88, 34), (86, 66), (80, 52), (20, 52)])),
              L(outline([(60, 6), (82, 16), (88, 40), (84, 60), (76, 36)]), 'shade', 'b', False),
              fringe([(12, 58), (14, 36), (28, 18), (50, 12), (72, 18), (86, 36), (88, 58), (80, 48), (70, 44), (60, 48), (54, 36), (46, 36), (40, 48), (30, 44),
                      (20, 48)]),
              strand([(18, 40), (30, 24), (50, 18), (70, 24), (82, 40)], 'shade', 'f', 1.3),
              L(quad((14, 62), (10, 80), (16, 92)), 'mid', 'f', False, False, 2.4), L(quad((86, 62), (90, 80), (84, 92)), 'mid', 'f', False, False, 2.4),
              L(ell(30, 90, 5, 2.6), 'blush', 'f', False), L(ell(70, 90, 5, 2.6), 'blush', 'f', False)],
    'side': [L(outline([(30, 6), (20, -10), (30, -8), (34, -26, 1), (44, -10), (54, -14), (48, 2)])),
             L(outline([(54, 60), (58, 48), (80, 46), (92, 32), (86, 10), (64, -2), (36, -2), (14, 10), (4, 34), (6, 62), (18, 80), (34, 82), (46, 72)])),
             L(outline([(6, 34), (28, 40), (30, 76), (12, 70)]), 'shade', 'b', False),
             strand([(70, 4), (40, 14), (16, 34), (14, 60)], 'shade', 'f', 1.3),
             L(quad((56, 62), (60, 80), (56, 92)), 'mid', 'f', False, False, 2.4), L(ell(86, 90, 4, 2.4), 'blush', 'f', False)],
    'back': [L(outline([(36, 6), (28, -10), (40, -8), (44, -24, 1), (50, -10), (60, -22, 1), (62, -8), (74, -10), (66, 6), (50, 12)])),
             L(outline([(14, 76), (10, 36), (22, 12), (50, 4), (78, 12), (90, 36), (86, 76), (64, 86), (36, 86)])),
             L(outline([(56, 8), (84, 18), (90, 50), (84, 74), (60, 84)]), 'shade', 'b', False),
             strand([(50, 12), (50, 84)], 'shade', 'b', 1.2)],
}

# Ichikawa Zanakurou: piel morena y pelo verde azulado muy oscuro en pinchos enormes por todas partes, con un pico entre los
# ojos; ojos rojos afilados y dos pendientes redondos gruesos bajo las orejas
_zk_beads = [L(ell(14, 104, 7, 6), 'bead', 'f', ln=True), L(ell(86, 104, 7, 6), 'bead', 'f', ln=True),
             L([(9, 96), (19, 96)], 'gold', 'f', False, False, 1.6), L([(81, 96), (91, 96)], 'gold', 'f', False, False, 1.6)]
CHARS['zack-avalon'] = {
    'body': 'normal', 'pal': pal('#1e4a54', '#a8683e', iris='#c81e2a', shade='#12343c', deep='#0c2228', bead='#1e4a54', gold='#c89a4a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 90), (2, 80, 1), (8, 66), (-8, 52, 1), (6, 46), (-6, 24, 1), (12, 24), (8, 0, 1), (24, 8), (30, -18, 1), (42, -2), (52, -26, 1), (60, -4),
                         (74, -16, 1), (76, 6), (94, 0, 1), (90, 22), (108, 24, 1), (96, 44), (108, 54, 1), (94, 64), (100, 82, 1), (86, 90), (82, 66), (18, 66)])),
              L(outline([(60, -2), (86, 8), (100, 36), (94, 80), (82, 50)]), 'shade', 'b', False),
              fringe([(12, 66), (14, 40), (28, 22), (50, 16), (72, 22), (86, 40), (88, 66), (80, 52), (76, 64, 1), (68, 48), (60, 58, 1), (54, 44), (50, 66, 1),
                      (46, 44), (40, 58, 1), (32, 48), (24, 64, 1), (18, 52)])] + _zk_beads,
    'side': [L(outline([(54, 62), (58, 50), (80, 48), (92, 34), (92, 14), (102, 2, 1), (80, 2), (74, -20, 1), (58, -4), (40, -24, 1), (32, 0), (8, -10, 1), (12, 12),
                        (-12, 20, 1), (4, 34), (-16, 48, 1), (2, 56), (-12, 74, 1), (6, 76), (0, 96, 1), (18, 90), (24, 106, 1), (34, 90), (46, 76)])),
             L(outline([(2, 36), (24, 42), (30, 88), (10, 86)]), 'shade', 'b', False),
             fringe([(66, 4), (90, 18), (96, 42), (94, 64, 1), (86, 50), (80, 60, 1), (76, 42), (66, 30)]),
             L(ell(52, 104, 7, 6), 'bead', 'f', ln=True), L([(47, 96), (57, 96)], 'gold', 'f', False, False, 1.6)],
    'back': [L(outline([(14, 94), (0, 82, 1), (6, 66), (-10, 52, 1), (4, 44), (-6, 22, 1), (12, 22), (8, -2, 1), (24, 6), (30, -18, 1), (42, -2), (52, -26, 1), (60, -4),
                        (74, -16, 1), (76, 6), (94, -2, 1), (90, 22), (108, 22, 1), (96, 44), (110, 52, 1), (96, 66), (102, 84, 1), (86, 94), (72, 104, 1), (60, 94),
                        (50, 104, 1), (40, 94), (28, 104, 1)])),
             L(outline([(56, -2), (86, 8), (100, 40), (94, 88), (66, 98), (70, 50)]), 'shade', 'b', False)] + _zk_beads,
}

# Matatagi Hayato (forma Pleasing): pelo gris pardo muy oscuro de pinchos grandes hacia arriba y hacia los lados, con
# mechones que le caen por la frente; piel bronceada, ojos oscuros y una sonrisa amable
_mat_front = [L(outline([(14, 94), (0, 82, 1), (6, 68), (-12, 56, 1), (4, 48), (-8, 28, 1), (10, 26), (6, 2, 1), (22, 10), (28, -16, 1), (40, 0), (52, -26, 1),
                         (58, -2), (74, -16, 1), (76, 4), (94, 0, 1), (90, 22), (108, 24, 1), (96, 42), (110, 54, 1), (96, 62), (102, 80, 1), (88, 88), (84, 94, 1),
                         (82, 66), (18, 66)])),
              L(outline([(60, -2), (86, 8), (100, 36), (96, 76), (82, 50)]), 'shade', 'b', False),
              fringe([(12, 62), (14, 38), (28, 20), (50, 14), (72, 20), (86, 38), (88, 62), (80, 50), (74, 60, 1), (68, 46), (60, 56, 1), (56, 42), (50, 64, 1),
                      (44, 42), (36, 58, 1), (30, 46), (22, 62, 1)])]
_mat_side = [L(outline([(54, 62), (58, 50), (80, 48), (92, 34), (92, 14), (104, 4, 1), (82, 2), (78, -22, 1), (60, -4), (40, -26, 1), (32, -2), (6, -8, 1), (12, 12),
                        (-14, 20, 1), (4, 34), (-16, 48, 1), (2, 56), (-12, 72, 1), (6, 74), (0, 92, 1), (18, 86), (22, 102, 1), (32, 88), (46, 76)])),
             L(outline([(2, 36), (24, 42), (30, 84), (10, 82)]), 'shade', 'b', False),
             fringe([(66, 4), (90, 18), (96, 42), (94, 64, 1), (86, 50), (80, 60, 1), (76, 42), (66, 30)])]
_mat_back = [L(outline([(14, 94), (0, 84, 1), (6, 68), (-12, 56, 1), (4, 46), (-8, 26, 1), (10, 24), (6, 2, 1), (22, 10), (28, -16, 1), (40, 0), (52, -26, 1),
                        (58, -2), (74, -16, 1), (76, 4), (94, 0, 1), (90, 22), (110, 26, 1), (96, 44), (112, 56, 1), (96, 66), (104, 84, 1), (86, 94), (72, 104, 1),
                        (62, 94), (50, 106, 1), (38, 94), (26, 104, 1)])),
             L(outline([(56, -2), (86, 8), (102, 40), (96, 88), (66, 98), (70, 50)]), 'shade', 'b', False)]
_mat_pal = dict(iris='#2a1e1a', shade='#3e3632', deep='#2a2420', blue='#1e5a9a', blue_d='#143e6a')
CHARS[f'{T}:falco-flashman-gx-matatagi-p'] = {
    'body': 'normal', 'pal': pal('#5a5048', '#eaa874', **_mat_pal),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': _mat_front, 'side': _mat_side, 'back': _mat_back,
}
# Matatagi en forma Dark Side (Matatagi_DS en la wiki; no juega en el equipo, se guarda para cuando salga): el mismo pelo con mechones azules en las puntas del lado izquierdo y
# por detrás, y la mirada afilada
_blue_f = [L(outline([(-12, 56), (4, 48), (-8, 28), (10, 26), (6, 2), (22, 10), (16, 20), (14, 40), (10, 58)]), 'blue', 'b'),
           L(outline([(-8, 28), (6, 34), (0, 46), (-12, 56, 1)]), 'blue_d', 'b', False)]
CHARS['gx:falco-flashman-dark'] = {
    'body': 'normal', 'pal': pal('#5a5048', '#eaa874', **_mat_pal),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': _mat_front[:1] + _blue_f + _mat_front[1:],
    'side': _mat_side[:1] + [L(outline([(60, -4), (40, -26), (32, -2), (50, 6), (70, 14), (92, 14), (104, 4), (82, 2), (78, -22)]), 'blue', 'b'),
                             L(outline([(72, 16), (92, 16), (92, 30), (76, 26)]), 'blue_d', 'b', False)] + _mat_side[1:],
    'back': _mat_back[:1] + [L(outline([(8, 2), (22, 10), (28, -16), (40, 0), (34, 20), (14, 40), (4, 46), (-8, 26), (10, 24)]), 'blue', 'b')] + _mat_back[1:],
}

# Maneuver Gibbs juega disfrazado de Tsurugi (el falso Tsurugi): el peinado de Tsurugi, más tieso, con una coleta larga
# hacia atrás, orejas puntiagudas, ojos morados y los rizos en espiral junto a las orejas
_fake = copy.deepcopy(CHARS['victor-blade'])
_fake['pal'] = {**_fake['pal'], 'iris': (150, 60, 190, 255)}
_fake['face'] = {**_fake['face'], 'ears': False}
_elf = [L(outline([(16, 64), (2, 52, 1), (12, 80)]), 'skin', 'b', ln=True), L(outline([(84, 64), (98, 52, 1), (88, 80)]), 'skin', 'b', ln=True)]
_fake['front'] = _elf + _fake['front']
_fake['back'] = _elf + _fake['back']
_fake['side'] = _fake['side'] + [L(outline([(48, 64), (36, 50, 1), (54, 74)]), 'skin', 'f', ln=True)]
CHARS[f'{T}:maneuver-gibbs'] = _fake
# el Matatagi base del equipo es también la forma Pleasing (Matatagi en la wiki: "Pleasing form - story")
CHARS['falco-flashman'] = CHARS[f'{T}:falco-flashman-gx-matatagi-p']
