"""Plathos (vr-platos): el equipo de Victory Road (英雄たちのヴィクトリーロード), con sus modelos 3D de la enciclopedia.
Son todos personajes nuevos de VR, con una sola forma (Victorio Arno sale en la enciclopedia con ropa negra: se dibuja la
cabeza y lleva la equipación del equipo)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars_vr_nikogawa import BROWN_LINE, blush, brow_side, brows, crop  # noqa: F401
from heads import quad  # noqa: F401

WHITE = (248, 248, 248, 255)


# Ash Barnes (portero): pelo verde azulado que se abre a los lados en dos picos como orejas de gato, con un rizo de antena,
# mechones por la frente y una diadema verde lima; ojos verdes grandes y sonrisa
LIME = (200, 224, 64, 255)
CHARS['ash-barnes'] = {
    'body': 'normal', 'pal': pal('#2a8a8a', '#fcd2b0', iris='#3aa88a', shade='#206c6c', deep='#165050'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'hairline': False},
    'front': [L(outline([(16, 86), (14, 64), (8, 52), (-4, 44, 1), (8, 36), (14, 18), (30, 4), (50, 0), (70, 4), (86, 18), (92, 36), (104, 44, 1), (92, 52), (86, 64),
                         (84, 86), (80, 64), (20, 64)])),
              L(outline([(60, 2), (84, 16), (92, 38), (100, 44), (90, 52), (84, 80), (78, 40)]), 'shade', 'b', False),
              L(quad((40, 2), (36, -14), (48, -16)) + quad((48, -16), (42, -8), (46, 2))[1:], 'mid', 'b'),
              L(quad((16, 40), (50, 26), (84, 40)), LIME, 'b', False, False, 2.4),
              L(outline([(14, 66), (16, 44), (30, 36), (50, 34), (70, 36), (84, 44), (86, 66), (78, 54), (70, 64, 1), (62, 50), (54, 74, 1), (50, 48), (46, 74, 1),
                         (38, 50), (30, 64, 1), (22, 54)]), 'mid', 'f'),
              strand([(50, 38), (50, 70)], 'deep', 'f', 1.0)],
    'side': [L(outline([(76, 52), (88, 46), (94, 30), (86, 10), (64, 0), (40, 0), (20, 8), (6, 30), (-10, 42, 1), (4, 50), (-8, 58, 1), (8, 62), (14, 80), (18, 98, 1),
                        (26, 84), (36, 80), (40, 64), (48, 58), (60, 56), (70, 70, 1)])),
             L(outline([(4, 40), (30, 46), (44, 60), (36, 80), (24, 84), (12, 72)]), 'shade', 'b', False),
             L(quad((56, 2), (54, -16), (66, -14)) + quad((66, -14), (60, -6), (62, 2))[1:], 'mid', 'b'),
             L(quad((42, 72), (60, 30), (90, 30)), LIME, 'f', False, False, 2.2),
             L(outline([(76, 26), (92, 36), (94, 56), (88, 66, 1), (84, 52), (76, 42)]), 'mid', 'f')],
    'back': [L(outline([(18, 80), (12, 54), (-4, 44, 1), (8, 36), (14, 18), (30, 4), (50, 0), (70, 4), (86, 18), (92, 36), (104, 44, 1), (88, 54), (82, 80), (66, 88),
                        (52, 98, 1), (46, 88), (34, 88)])),
             L(outline([(56, 2), (84, 16), (92, 38), (102, 44), (88, 54), (82, 80), (66, 88), (60, 40)]), 'shade', 'b', False),
             L(quad((44, 2), (42, -14), (54, -16)) + quad((54, -16), (48, -8), (52, 2))[1:], 'mid', 'b')],
}

# Miles Euclid: melena lisa rubio lima hasta la mandíbula con las puntas abiertas, más clara delante, y un flequillo largo
# que le tapa el ojo derecho; ojos azules y sonrisa
CREAM = (248, 248, 208, 255)
CHARS['miles-euclid'] = {
    'body': 'normal', 'pal': pal('#dcee8c', '#fcd8bc', iris='#3a7ad0', shade='#bccc6c', deep='#9aa850'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'hairline': False},
    'front': [L(outline([(2, 102, 1), (10, 90), (8, 60), (10, 30), (22, 8), (50, 0), (78, 8), (90, 30), (92, 60), (90, 90), (98, 102, 1), (84, 96), (80, 64), (20, 64), (16, 96)])),
              L(outline([(60, 4), (84, 14), (92, 40), (90, 92), (84, 92), (82, 50)]), 'shade', 'b', False),
              L(outline([(14, 66), (16, 40), (28, 24), (46, 18), (56, 22), (52, 50), (50, 92, 1), (44, 68), (34, 62, 1), (22, 60)]), CREAM, 'f'),
              L(outline([(56, 22), (72, 24), (84, 38), (86, 66), (78, 54), (68, 50), (60, 54)]), 'mid', 'f'),
              strand([(40, 24), (44, 50), (48, 80)], 'shade', 'f', 1.0), strand([(28, 32), (30, 56)], 'shade', 'f', 1.0)],
    'side': [L(outline([(78, 54), (90, 46), (94, 26), (84, 6), (60, -2), (34, 0), (14, 12), (4, 36), (4, 70), (12, 96), (26, 104, 1), (36, 96), (50, 98, 1), (54, 80),
                        (56, 62), (66, 58)])),
             L(outline([(4, 40), (36, 40), (52, 64), (48, 96), (26, 100), (10, 90)]), 'shade', 'b', False),
             L(outline([(72, 6), (90, 24), (94, 50), (88, 80, 1), (82, 54), (76, 36)]), CREAM, 'f'),
             strand([(30, 8), (36, 40), (40, 90)], 'deep', 'b', 1.0)],
    'back': [L(outline([(0, 102, 1), (8, 88), (6, 60), (8, 30), (20, 8), (50, 0), (80, 8), (92, 30), (94, 60), (92, 88), (100, 102, 1), (70, 98), (50, 100), (30, 98)])),
             L(outline([(56, 4), (82, 12), (92, 34), (94, 88), (98, 100), (66, 98), (60, 50)]), 'shade', 'b', False)]
            + [strand([(x, 20), (x, 96)], 'deep', 'b', 1.0) for x in (24, 40, 60, 76)],
}

# Hector Thareos (Hicks Fraile): pelo morado oscuro en pinchos de punta hacia arriba, con un pico en la frente y dos mechones
# largos que bajan por las mejillas y se rizan hacia fuera en la mandíbula; ojos granate, cejas gruesas y sonrisa
CHARS['hector-thareos'] = {
    'body': 'normal', 'pal': pal('#4a3a7a', '#fcd2b0', iris='#a03a2a', shade='#3a2e62', deep='#2a2048'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(15, 70), (18, 50), (30, 46), (42, 42), (50, 48), (58, 42), (70, 46), (82, 50), (85, 70)]},
    'front': [L(outline([(16, 72), (12, 50), (2, 46, 1), (10, 36), (2, 22, 1), (14, 18), (12, 2, 1), (26, 6), (30, -12, 1), (40, -2), (50, -18, 1), (58, -2), (70, -12, 1),
                         (74, 6), (88, 2, 1), (86, 18), (98, 22, 1), (90, 36), (98, 46, 1), (88, 50), (84, 72), (80, 54), (20, 54)])),
              L(outline([(56, -4), (70, -10), (74, 8), (86, 4), (86, 20), (96, 24), (90, 38), (96, 46), (86, 52), (78, 30)]), 'shade', 'b', False),
              L(quad((18, 60), (16, 84), (10, 92)) + quad((10, 92), (4, 96), (2, 104))[1:], 'mid', 'f', False, False, 3.0),
              L(quad((82, 60), (84, 84), (90, 92)) + quad((90, 92), (96, 96), (98, 104))[1:], 'mid', 'f', False, False, 3.0)]
             + brows(64, 'mid', 4.6, 14, 0.6, 12),
    'side': [L(outline([(70, 52), (82, 46), (92, 30), (102, 20, 1), (88, 14), (96, 0, 1), (78, 2), (80, -16, 1), (62, -4), (54, -20, 1), (44, -4), (30, -14, 1), (26, 4),
                        (8, 2, 1), (12, 18), (-4, 26, 1), (6, 36), (0, 52, 1), (8, 60), (12, 78), (24, 92), (36, 86), (38, 66), (46, 58), (58, 56)])),
             L(outline([(4, 38), (32, 44), (44, 58), (36, 66), (36, 86), (24, 92), (10, 74)]), 'shade', 'b', False),
             L(quad((62, 60), (60, 84), (56, 92)) + quad((56, 92), (50, 96), (48, 104))[1:], 'mid', 'f', False, False, 3.0)]
            + brow_side(64, 'mid', 4.6, 0.6),
    'back': [L(outline([(18, 84), (12, 52), (0, 44, 1), (10, 36), (2, 20, 1), (14, 16), (12, 0, 1), (26, 4), (30, -14, 1), (40, -2), (50, -20, 1), (60, -2), (70, -14, 1),
                        (74, 4), (88, 0, 1), (86, 16), (98, 20, 1), (90, 36), (100, 44, 1), (88, 52), (82, 84), (66, 88), (50, 96, 1), (34, 88)])),
             L(outline([(56, -2), (70, -12), (74, 6), (86, 2), (86, 18), (96, 22), (90, 38), (98, 46), (88, 54), (82, 84), (66, 88), (60, 40)]), 'shade', 'b', False),
             L(quad((16, 70), (14, 86), (8, 92)) + quad((8, 92), (2, 96), (0, 104))[1:], 'mid', 'b', False, False, 3.0),
             L(quad((84, 70), (86, 86), (92, 92)) + quad((92, 92), (98, 96), (100, 104))[1:], 'mid', 'b', False, False, 3.0)],
}

# Rhea Loriandrin (Romi Rhomin): pelo naranja con flequillo de lado y dos trenzas gruesas y cortas que salen hacia fuera y
# abajo a la altura de la mandíbula, atadas con gomas; ojos azules grandes y sonrisa
def _braid(x0, y0, x1, y1, w=11, c='mid'):
    import math
    dx, dy = x1 - x0, y1 - y0
    n = math.hypot(dx, dy) or 1
    px, py = -dy / n * w / 2, dx / n * w / 2
    out = [L([(x0 + px, y0 + py), (x1 + px, y1 + py), (x1 - px, y1 - py), (x0 - px, y0 - py)], c)]
    for t in (0.33, 0.66):
        mx, my = x0 + dx * t, y0 + dy * t
        out.append(L([(mx + px, my + py), (mx - px, my - py)], 'deep', 'b', False, False, 1.0))
    return out


CHARS['rhea-loriandrin'] = {
    'body': 'chica', 'pal': pal('#f07a3a', '#fcd8bc', iris='#3a4ad0', shade='#d0602a', deep='#a8481e'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 93, 'hairline': False},
    'front': _braid(14, 76, -6, 96) + _braid(86, 76, 106, 96)
             + [L(outline([(16, 80), (10, 56), (8, 30), (20, 6), (50, -4), (80, 6), (92, 30), (90, 56), (84, 80), (80, 60), (20, 60)])),
                L(outline([(60, 0), (84, 10), (92, 34), (88, 60), (84, 76), (80, 40)]), 'shade', 'b', False),
                L(outline([(14, 66), (16, 40), (30, 24), (50, 18), (72, 24), (86, 40), (86, 66), (80, 54), (72, 46), (60, 44), (48, 48), (40, 58, 1), (36, 48), (24, 58)]), 'mid', 'f'),
                strand([(64, 22), (52, 34), (40, 50)], 'deep', 'f', 1.0), strand([(78, 30), (66, 40)], 'deep', 'f', 1.0)],
    'side': _braid(24, 74, -6, 96, 12)
            + [L(outline([(72, 52), (84, 46), (92, 28), (84, 6), (60, -6), (34, -4), (14, 8), (2, 30), (2, 54), (10, 72), (24, 80), (36, 76), (40, 64), (48, 58), (60, 56)])),
               L(outline([(2, 40), (30, 44), (44, 58), (36, 76), (12, 70)]), 'shade', 'b', False),
               L(outline([(70, 20), (90, 30), (92, 50), (86, 60, 1), (80, 44)]), 'mid', 'f')],
    'back': _braid(18, 76, -4, 96) + _braid(82, 76, 104, 96)
            + [L(outline([(16, 78), (8, 52), (8, 28), (20, 6), (50, -4), (80, 6), (92, 28), (92, 52), (84, 78), (66, 86), (50, 88), (34, 86)])),
               L(outline([(56, 0), (82, 8), (92, 30), (92, 52), (84, 78), (60, 86), (54, 40)]), 'shade', 'b', False),
               strand([(50, -2), (50, 86)], 'deep', 'b', 1.0)],
}

# Saros Algebra (Serpo Alegre): rechoncho; pelo azul pizarra oscuro, alto, con un tupé de mechones gordos hacia arriba; un
# visor naranja que le tapa los ojos, sujeto con una banda blanca y verde; sonrisa ancha
VISOR = (240, 160, 32, 255)
BAND = (236, 220, 220, 255)
GREEN = (40, 170, 110, 255)
CHARS['saros-algebra'] = {
    'body': 'corpulento', 'pal': pal('#2e4658', '#fcd2b0', iris='#2a2a2a', shade='#243848', deep='#1a2834'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': blob([(15, 50), (50, 30), (85, 50), (90, 76), (85, 96), (66, 107), (50, 109), (34, 107), (15, 96), (10, 76)]),
             'hairline': [(14, 64), (18, 48), (30, 44), (50, 46), (70, 44), (82, 48), (86, 64)]},
    'front': [L(outline([(16, 66), (12, 44), (14, 20), (22, 2), (18, -14), (26, -22), (34, -16), (36, -30), (46, -32), (50, -20), (58, -32), (68, -28), (66, -14),
                         (76, -18), (82, -8), (78, 4), (86, 18), (88, 44), (84, 66), (80, 50), (20, 50)])),
              L(outline([(56, -14), (62, -32), (66, -12), (76, -20), (78, 0), (86, 20), (88, 44), (82, 60), (76, 30)]), 'shade', 'b', False),
              strand([(36, -10), (40, 10)], 'deep', 'b', 1.2), strand([(60, -10), (58, 12)], 'deep', 'b', 1.2),
              L(quad((40, 64), (44, 61), (48, 64)), OUTC, 'f', False, False, 1.6),
              L([(6, 68), (94, 68), (94, 84), (6, 84)], BAND, 'f', ln=True),
              L([(14, 70), (86, 70), (86, 82), (14, 82)], VISOR, 'f', ln=True),
              L([(18, 74), (82, 74)], (252, 210, 120, 255), 'f', False, False, 1.4)]
             + [L(quad((32, 94), (50, 102), (68, 94)), BROWN_LINE, 'f', False, False, 1.6)],
    'side': [L(outline([(70, 50), (80, 44), (88, 24), (84, 0), (78, -26, 1), (66, -12), (56, -36, 1), (46, -14), (30, -28, 1), (24, -6), (8, 10), (2, 40), (8, 66), (22, 82),
                        (34, 80), (38, 64), (46, 56), (58, 52)])),
             L(outline([(2, 40), (30, 44), (44, 56), (36, 66), (34, 80), (22, 82), (8, 66)]), 'shade', 'b', False),
             L([(20, 66), (60, 66), (62, 80), (20, 82)], BAND, 'f', ln=True),
             L([(28, 69), (46, 69), (46, 77), (28, 77)], GREEN, 'f', False),
             L([(62, 66), (92, 66), (94, 80), (62, 80)], VISOR, 'f', ln=True)],
    'back': [L(outline([(18, 76), (12, 44), (14, 20), (22, 0), (22, -20, 1), (34, -14), (40, -34, 1), (50, -18), (60, -36, 1), (64, -14), (76, -24, 1), (78, -2), (86, 18),
                        (88, 44), (82, 76), (66, 86), (50, 88), (34, 86)])),
             L(outline([(56, -14), (62, -32), (66, -12), (76, -20), (78, 0), (86, 20), (88, 44), (82, 76), (66, 86), (60, 40)]), 'shade', 'b', False),
             L([(6, 68), (94, 68), (94, 84), (6, 84)], BAND, 'f', ln=True),
             L([(14, 74), (86, 74), (86, 78), (14, 78)], GREEN, 'f', False)],
}

# Eosram Reeves (Eosin Reese): piel morena; melena corta gris verdosa hasta la barbilla con raya en medio, de puntas hacia
# dentro; dos cintas rojas largas que le cuelgan por detrás desde la nuca; ojos verde azulado y sonrisa
RED = (196, 74, 72, 255)
CHARS['eosram-reeves'] = {
    'body': 'normal', 'pal': pal('#6a7a76', '#c08a62', iris='#3a8a8a', shade='#56645f', deep='#424e4a'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 94,
             'hairline': [(19, 96), (19, 50), (30, 40), (44, 34), (50, 30), (56, 34), (70, 40), (81, 50), (81, 96)]},
    'front': [L([(20, 92), (16, 118)], RED, 'b', False, False, 4.0), L([(80, 92), (84, 118)], RED, 'b', False, False, 4.0),
              L(outline([(10, 92), (4, 70), (6, 36), (18, 10), (50, 0), (82, 10), (94, 36), (96, 70), (90, 92), (82, 96), (82, 52), (18, 52), (18, 96)])),
              L(outline([(60, 2), (84, 12), (94, 38), (94, 72), (88, 90), (82, 60)]), 'shade', 'b', False),
              strand([(50, 2), (50, 30)], 'deep', 'b', 1.2)]
             + [strand([(x, 40), (x + (2 if x > 50 else -2), 90)], 'deep', 'b', 1.0) for x in (10, 90)],
    'side': [L(quad((30, 70), (16, 96), (4, 130)), RED, 'b', False, False, 4.0), L(quad((36, 72), (28, 96), (22, 126)), RED, 'b', False, False, 4.0),
             L(outline([(76, 52), (88, 44), (92, 26), (82, 6), (58, -2), (32, 0), (12, 12), (2, 40), (2, 70), (10, 90), (26, 92), (40, 88), (52, 90), (56, 70), (60, 56),
                        (70, 54)])),
             L(outline([(2, 46), (30, 46), (54, 64), (50, 88), (26, 92), (8, 86)]), 'shade', 'b', False)],
    'back': [L(outline([(8, 90), (4, 68), (6, 36), (18, 10), (50, 0), (82, 10), (94, 36), (96, 68), (92, 90), (70, 92), (50, 94), (30, 92)])),
             L(outline([(56, 2), (82, 10), (94, 36), (96, 68), (92, 90), (60, 92), (56, 50)]), 'shade', 'b', False),
             L([(44, 90), (40, 124)], RED, 'f', False, False, 5.0), L([(56, 90), (60, 124)], RED, 'f', False, False, 5.0),
             L([(42, 90), (58, 90)], RED, 'f', False, False, 4.0)]
            + [strand([(x, 30), (x, 90)], 'deep', 'b', 1.0) for x in (24, 40, 60, 76)],
}

# Eon McKeane (Aeon McKean): melena roja larga recogida por detrás en una cola baja que cae hasta la espalda, con volumen a
# los lados, y una diadema azul marino con una raya gris; ojos grises y sonrisa
NAVY = (42, 42, 90, 255)
CHARS['eon-mckeane'] = {
    'body': 'normal', 'pal': pal('#b8402c', '#fcd8bc', iris='#5a5a6a', shade='#9a3424', deep='#7a281c'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 94,
             'hairline': [(17, 70), (19, 48), (30, 40), (50, 36), (70, 40), (81, 48), (83, 70)]},
    'front': [L(outline([(8, 112, 1), (4, 92), (8, 64), (6, 34), (18, 6), (50, -6), (82, 6), (94, 34), (92, 64), (96, 92), (92, 112, 1), (84, 100), (82, 52), (18, 52), (16, 100)])),
              L(outline([(60, -2), (84, 8), (94, 36), (92, 66), (94, 104), (84, 96), (82, 50)]), 'shade', 'b', False),
              L(quad((14, 46), (50, 18), (86, 46)), NAVY, 'f', False, False, 4.0), L(quad((16, 44), (50, 16), (84, 44)), (150, 150, 160, 255), 'f', False, False, 1.0)],
    'side': [L(outline([(76, 50), (86, 40), (88, 20), (78, 0), (52, -8), (26, -4), (8, 14), (0, 44), (-2, 72), (-18, 106), (-26, 120, 1), (-6, 112), (10, 96), (24, 84), (36, 80),
                        (40, 64), (48, 56), (62, 52)])),
             L(outline([(0, 46), (30, 46), (44, 60), (36, 80), (10, 96), (-20, 116)]), 'shade', 'b', False),
             L(quad((44, 70), (60, 20), (86, 16)), NAVY, 'f', False, False, 4.0)],
    'back': [L(outline([(8, 112, 1), (4, 64), (6, 34), (18, 6), (50, -6), (82, 6), (94, 34), (96, 64), (92, 112, 1), (70, 106), (50, 114), (30, 106)])),
             L(outline([(56, -2), (82, 6), (94, 34), (96, 64), (92, 110), (64, 108), (56, 50)]), 'shade', 'b', False),
             L(quad((14, 46), (50, 30), (86, 46)), NAVY, 'b', False, False, 3.0)],
}

# Dariusius Henletos (Derios Henletti): pelo rubio dorado redondo, más oscuro por debajo, con el flequillo en mechones que
# se abren desde el centro de la frente y una coletita baja atada en la nuca; ojos azules, cejas fruncidas y sonrisa
CHARS['dariusius-henletos'] = {
    'body': 'normal', 'pal': pal('#e8c870', '#fcd8bc', iris='#3a4aa8', shade='#c4a052', deep='#9a7c3a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(16, 84), (8, 60), (8, 30), (20, 6), (50, -4), (80, 6), (92, 30), (92, 60), (84, 84), (80, 62), (20, 62)])),
              L(outline([(60, 0), (84, 10), (92, 34), (90, 62), (84, 80), (80, 40)]), 'shade', 'b', False),
              L(outline([(14, 66), (16, 40), (28, 22), (44, 18), (50, 30), (56, 18), (72, 22), (86, 40), (86, 66), (78, 52), (66, 44), (58, 52, 1), (54, 38), (50, 46),
                         (46, 38), (42, 52, 1), (34, 44), (22, 52)]), 'mid', 'f'),
              strand([(46, 22), (36, 30), (30, 50)], 'deep', 'f', 1.0), strand([(54, 22), (64, 30), (70, 50)], 'deep', 'f', 1.0)],
    'side': [L(outline([(16, 84), (6, 92), (2, 100, 1), (14, 98), (24, 90)]), 'shade'),
             L(outline([(74, 54), (86, 46), (92, 28), (84, 8), (60, -4), (34, -2), (14, 10), (4, 32), (4, 60), (12, 80), (26, 88), (36, 84), (40, 66), (48, 58), (62, 56)])),
             L(outline([(4, 46), (32, 48), (46, 60), (38, 84), (12, 80)]), 'shade', 'b', False),
             L(outline([(70, 10), (90, 28), (92, 54), (86, 64, 1), (80, 44)]), 'mid', 'f'),
             L([(20, 84), (26, 88)], OUTC, 'f', False, False, 2.4)],
    'back': [L(outline([(16, 82), (8, 58), (8, 30), (20, 6), (50, -4), (80, 6), (92, 30), (92, 58), (84, 82), (66, 88), (50, 90), (34, 88)])),
             L(outline([(56, 0), (82, 8), (92, 32), (92, 58), (84, 82), (60, 88), (54, 40)]), 'shade', 'b', False),
             L(outline([(46, 88), (40, 104, 1), (52, 96), (64, 102, 1), (56, 88)]), 'shade'),
             L([(46, 90), (56, 90)], OUTC, 'f', False, False, 2.4)],
}

# Torin Sandels (Torin Sanders): piel oscura; una mata grande de rizos gordos azul marino que le tapa el ojo derecho y se
# abulta hacia atrás y a su izquierda; ojo azul y sonrisa
def _curl_mass(pts, c='mid'):
    return L(blob(pts, 8), c)


CHARS['torin-sandels'] = {
    'body': 'normal', 'pal': pal('#2a3a9a', '#7a4a30', iris='#4a8ad0', shade='#20307e', deep='#162262'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [_curl_mass([(-14, 66), (-6, 48), (-12, 32), (2, 16), (10, -2), (30, -8), (46, -4), (64, -8), (84, 2), (94, 22), (92, 46), (86, 60), (84, 50), (60, 48),
                          (54, 58), (56, 80), (46, 96), (32, 100), (20, 94), (2, 92), (-12, 80)]),
              L(blob([(54, -4), (80, 2), (94, 24), (90, 48), (80, 46), (74, 20)], 6), 'shade', 'b', False),
              L(blob([(-10, 66), (6, 60), (20, 76), (12, 94), (-6, 88)], 6), 'shade', 'b', False),
              L(blob([(22, 58), (38, 52), (52, 60), (50, 78), (38, 88), (24, 84), (18, 72)], 6), 'mid', 'f', ln=True),
              L(blob([(16, 30), (34, 22), (50, 28), (46, 44), (26, 46)], 6), 'shade', 'f', False),
              L(quad((60, 64), (68, 60), (76, 64)), OUTC, 'f', False, False, 1.6)],
    'side': [_curl_mass([(70, 50), (86, 44), (94, 24), (84, 4), (60, -6), (34, -6), (14, 4), (2, 22), (-10, 30), (-16, 52), (-10, 74), (4, 88), (22, 96), (40, 96), (50, 86),
                         (54, 70), (60, 56)]),
             L(blob([(-14, 50), (10, 46), (34, 60), (40, 90), (16, 94), (-6, 80)], 6), 'shade', 'b', False),
             L(blob([(64, 0), (84, 8), (92, 26), (80, 30), (70, 18)], 6), 'shade', 'b', False)],
    'back': [_curl_mass([(4, 78), (-8, 60), (-2, 40), (8, 18), (26, 2), (50, -6), (74, 0), (92, 14), (104, 34), (110, 56), (104, 76), (92, 90), (80, 84), (66, 88), (50, 90),
                         (32, 88), (16, 86)]),
             L(blob([(58, -2), (88, 12), (104, 36), (108, 60), (96, 86), (72, 80), (64, 40)], 6), 'shade', 'b', False),
             L(blob([(24, 30), (44, 24), (50, 44), (30, 50)], 6), 'shade', 'f', False)],
}

# Orpheus Clayridge (Ortopi Clade): melena lisa blanca lavanda hasta los hombros, con un pico en el centro de la frente y
# los lados enmarcando la cara; ojos naranjas afilados, cejas finas y boca seria
CHARS['orpheus-clayridge'] = {
    'body': 'delgado', 'pal': pal('#ece4f2', '#fcd4b4', iris='#d07a2a', shade='#c8bcd4', deep='#a498b4'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'line', 'mouth_y': 95,
             'hairline': [(19, 110), (19, 50), (30, 42), (44, 38), (50, 44), (56, 38), (70, 42), (81, 50), (81, 110)]},
    'front': [L(outline([(2, 114, 1), (6, 80), (6, 40), (16, 12), (50, 0), (84, 12), (94, 40), (94, 80), (98, 114, 1), (82, 112), (82, 52), (18, 52), (18, 112)])),
              L(outline([(60, 2), (84, 12), (94, 40), (94, 80), (96, 112), (84, 110), (82, 50)]), 'shade', 'b', False),
              strand([(30, 10), (24, 50), (14, 100)], 'deep', 'b', 1.0), strand([(70, 10), (76, 50), (86, 100)], 'deep', 'b', 1.0)],
    'side': [L(outline([(76, 52), (88, 44), (92, 26), (82, 6), (58, -2), (32, 0), (12, 12), (2, 40), (-2, 80), (-6, 118, 1), (20, 112), (40, 116, 1), (50, 96), (56, 70),
                        (60, 56), (70, 54)])),
             L(outline([(2, 44), (32, 44), (54, 64), (46, 110), (20, 110), (0, 112)]), 'shade', 'b', False),
             L(outline([(72, 30), (90, 40), (90, 60), (80, 90, 1), (78, 56)]), 'mid', 'f'),
             strand([(30, 4), (24, 60), (20, 110)], 'deep', 'b', 1.0)],
    'back': [L(outline([(0, 116, 1), (4, 80), (4, 40), (16, 12), (50, 0), (84, 12), (96, 40), (96, 80), (100, 116, 1), (70, 112), (50, 116), (30, 112)])),
             L(outline([(56, 2), (84, 12), (96, 40), (96, 80), (98, 114), (64, 112), (58, 50)]), 'shade', 'b', False)]
            + [strand([(x, 10), (x, 110)], 'deep', 'b', 1.0) for x in (26, 44, 62, 78)],
}

# Victorio Arno ("Vee"): bajito; pelo esponjoso rubio amarillo arriba y castaño claro por debajo, abultado a los lados, con
# flequillo en mechones; ojos verdes grandes y sonrisa
TAWNY = (196, 150, 72, 255)
CHARS['victorio-cryptix'] = {
    'body': 'bajito', 'pal': pal('#f2e048', '#fcd8bc', iris='#3ab04a', shade='#d4c234', deep='#a89a28'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'hairline': False},
    'front': [L(outline([(10, 86, 1), (6, 66), (0, 52), (8, 26), (24, 4), (34, 0), (38, -8, 1), (46, -2), (56, -8, 1), (62, 0), (80, 6), (94, 26), (100, 52), (94, 66),
                         (90, 86, 1), (82, 72), (18, 72)]), TAWNY),
              L(outline([(4, 56), (8, 26), (24, 4), (34, 0), (38, -8, 1), (46, -2), (56, -8, 1), (62, 0), (80, 6), (94, 26), (96, 56), (80, 50), (50, 52), (20, 50)])),
              L(outline([(60, 2), (82, 10), (94, 30), (94, 54), (80, 48), (76, 24)]), 'shade', 'b', False),
              L(outline([(14, 68), (16, 46), (30, 36), (50, 32), (70, 36), (84, 46), (86, 68), (78, 58), (70, 64, 1), (62, 54), (54, 66, 1), (48, 54), (38, 66, 1), (32, 54),
                         (22, 62, 1)]), TAWNY, 'f')],
    'side': [L(outline([(74, 56), (86, 50), (94, 32), (86, 10), (62, -2), (52, -10, 1), (44, -2), (24, 2), (8, 20), (-4, 50), (4, 72), (16, 90, 1), (26, 80), (38, 84, 1),
                        (40, 66), (48, 58), (62, 58)]), TAWNY),
             L(outline([(86, 34), (86, 10), (62, -2), (52, -10, 1), (44, -2), (24, 2), (8, 20), (-2, 46), (30, 46), (60, 40)])),
             L(outline([(74, 30), (92, 40), (94, 60), (86, 70, 1), (80, 50)]), TAWNY, 'f')],
    'back': [L(outline([(10, 86, 1), (4, 66), (0, 50), (8, 24), (24, 4), (40, -2), (48, -10, 1), (56, -2), (76, 4), (92, 24), (100, 50), (96, 66), (90, 86, 1), (74, 82),
                        (62, 90, 1), (50, 82), (38, 90, 1), (26, 82)]), TAWNY),
             L(outline([(2, 54), (8, 24), (24, 4), (40, -2), (48, -10, 1), (56, -2), (76, 4), (92, 24), (98, 54), (70, 60), (50, 54), (30, 60)])),
             L(outline([(56, 0), (80, 8), (94, 28), (96, 54), (70, 58), (60, 30)]), 'shade', 'b', False)],
}

# Niana Cooke (Niana Cook): piel tostada; pelo castaño con un mechón blanco en el flequillo y coletas de pinchos que salen
# disparadas: una a su derecha, a la altura de la sien, y otra en lo alto a su izquierda, con gomas azules; ojos verdes
# enormes con raya azul y sonrisa
BLUE_TIE = (40, 110, 200, 255)
CHARS['niana-cooke'] = {
    'body': 'chica', 'pal': pal('#7a4a3a', '#d89068', iris='#2ab07a', shade='#623a2e', deep='#4a2c22'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 94,
             'hairline': [(15, 62), (18, 46), (30, 40), (50, 38), (70, 40), (82, 46), (85, 62)]},
    'front': [L(outline([(14, 44), (-6, 36, 1), (0, 50), (-8, 62, 1), (2, 66), (-2, 82, 1), (14, 64)])),
              L(outline([(70, 8), (70, -18, 1), (80, -10), (90, -26, 1), (90, -6), (104, -6, 1), (92, 8), (100, 22, 1), (82, 18)])),
              L(ell(14, 54, 2.6, 4), BLUE_TIE, 'f', False), L(ell(78, 12, 4, 2.6), BLUE_TIE, 'f', False)]
             + crop('front', top=0, side=64, w=2)
             + [L(outline([(26, 26), (40, 18), (56, 22), (60, 34), (48, 34), (34, 40)]), WHITE, 'f', ln=True)]
             + brows(64, 'mid', 4.0, 14, 0.2, 11)
             + [L([(24, 76), (28, 80)], BLUE_TIE, 'f', False, False, 1.4), L([(76, 76), (72, 80)], BLUE_TIE, 'f', False, False, 1.4)] + blush(87, (220, 120, 100, 255)),
    'side': [L(outline([(28, 46), (4, 34, 1), (10, 50), (-2, 58, 1), (8, 66), (4, 82, 1), (26, 64)])),
             L(outline([(32, 12), (22, -20, 1), (36, -10), (44, -26, 1), (46, -6), (58, -8, 1), (48, 10)]))]
            + crop('side', top=-2, nape=86, w=2)
            + [L(outline([(76, 20), (88, 22), (92, 34), (82, 34)]), WHITE, 'f', ln=True)] + brow_side(64, 'mid', 4.0),
    'back': [L(outline([(86, 44), (106, 36, 1), (100, 50), (108, 62, 1), (98, 66), (102, 82, 1), (86, 64)])),
             L(outline([(30, 8), (30, -18, 1), (20, -10), (10, -26, 1), (10, -6), (-4, -6, 1), (8, 8), (0, 22, 1), (18, 18)])),
             L(ell(86, 54, 2.6, 4), BLUE_TIE, 'f', False), L(ell(22, 12, 4, 2.6), BLUE_TIE, 'f', False)]
            + crop('back', top=0, nape=86, w=2) + [strand([(50, 4), (46, 30), (54, 50), (48, 80)], 'deep', 'b', 1.0)],
}

# Gilia Dandrel (Gilia Dandelio): melena magenta hasta la mandíbula con un gran flequillo de lado hacia su izquierda y las
# puntas abiertas, recogida por detrás en una coletita; ojos morados, boca seria
CHARS['gilia-dandrel'] = {
    'body': 'chica', 'pal': pal('#a252aa', '#fcdcc8', iris='#6a4a8a', shade='#863e8e', deep='#682c70'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'line', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(2, 96, 1), (6, 70), (4, 36), (16, 8), (40, -6), (64, -4), (84, 8), (94, 30), (104, 34, 1), (94, 40), (94, 70), (98, 96, 1), (84, 86), (80, 60),
                         (20, 60), (16, 86)])),
              L(outline([(60, -2), (84, 8), (94, 32), (92, 70), (88, 88), (82, 50)]), 'shade', 'b', False),
              L(outline([(14, 66), (14, 40), (26, 22), (44, 14), (66, 16), (86, 28), (104, 32, 1), (84, 38), (66, 34), (46, 38), (30, 50), (20, 62)]), 'mid', 'f'),
              strand([(28, 24), (50, 22), (80, 30)], 'deep', 'f', 1.0)],
    'side': [L(outline([(76, 52), (88, 44), (96, 24), (86, 2), (60, -6), (34, -4), (14, 10), (4, 36), (2, 66), (8, 88), (20, 98), (28, 112, 1), (34, 96), (48, 92), (54, 74),
                        (60, 58), (70, 56)])),
             L(outline([(2, 44), (32, 44), (54, 64), (46, 92), (20, 96), (8, 86)]), 'shade', 'b', False),
             L(outline([(70, 6), (94, 22), (98, 34), (88, 46, 1), (82, 32), (74, 22)]), 'mid', 'f')],
    'back': [L(outline([(4, 96, 1), (6, 70), (4, 36), (16, 8), (50, -6), (84, 8), (96, 36), (94, 70), (96, 96, 1), (76, 90), (58, 92), (54, 108, 1), (46, 92), (24, 90)])),
             L(outline([(56, -2), (84, 8), (96, 36), (94, 70), (94, 94), (60, 92), (56, 40)]), 'shade', 'b', False),
             strand([(20, 20), (40, 50), (50, 90)], 'deep', 'b', 1.0)],
}

# Nikolaos Menandros (Nicole Menon): pelo castaño rojizo con raya y flequillo de lado, dos mechones blancos por dentro que le
# enmarcan la cara hasta el cuello, y una coleta larga por detrás; ojos azules y sonrisa
CHARS['nikolaos-menandros'] = {
    'body': 'normal', 'pal': pal('#a85a5a', '#fcd8bc', iris='#3a8ab0', shade='#8c4848', deep='#6e3636'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(10, 100, 1), (8, 70), (8, 34), (20, 8), (50, -4), (80, 8), (92, 34), (92, 70), (90, 100, 1), (82, 92), (80, 60), (20, 60), (18, 92)])),
              L(outline([(60, 0), (84, 10), (92, 36), (90, 70), (88, 94), (82, 50)]), 'shade', 'b', False),
              L(outline([(14, 54), (12, 80), (18, 112, 1), (22, 80), (22, 52)]), WHITE, 'f', ln=True),
              L(outline([(86, 54), (88, 80), (82, 112, 1), (78, 80), (78, 52)]), WHITE, 'f', ln=True),
              L(outline([(14, 60), (16, 36), (30, 20), (50, 14), (72, 20), (86, 36), (86, 60), (80, 50), (66, 44), (54, 46), (46, 64, 1), (42, 46), (30, 50), (20, 58)]), 'mid', 'f'),
              strand([(60, 18), (50, 30), (44, 56)], 'deep', 'f', 1.0)],
    'side': [L(outline([(28, 70), (12, 96), (-6, 124, 1), (8, 112), (24, 96), (36, 80)])),
             L(outline([(76, 52), (88, 44), (92, 26), (82, 6), (58, -4), (32, -2), (12, 10), (2, 36), (2, 62), (10, 80), (24, 86), (36, 80), (40, 64), (48, 58), (62, 56)])),
             L(outline([(2, 44), (30, 46), (44, 60), (36, 80), (10, 78)]), 'shade', 'b', False),
             L(outline([(78, 40), (84, 70), (90, 104, 1), (78, 76), (72, 50)]), WHITE, 'f', ln=True),
             L(outline([(70, 10), (90, 26), (92, 50), (84, 58, 1), (78, 40)]), 'mid', 'f')],
    'back': [L(outline([(16, 84), (8, 56), (8, 30), (20, 6), (50, -4), (80, 6), (92, 30), (92, 56), (84, 84), (60, 90), (56, 122, 1), (50, 110), (44, 122, 1), (40, 90)])),
             L(outline([(56, 0), (82, 8), (92, 30), (92, 56), (84, 84), (60, 90), (54, 40)]), 'shade', 'b', False),
             L(outline([(42, 30), (38, 70), (50, 110, 1), (62, 70), (58, 30)]), 'deep', 'b', False)],
}

# Hugo Severian (Hugo Svate): pelo gris plateado en casco redondo, más oscuro (gris pardo) por debajo, con un flequillo que le
# tapa el ojo derecho; el ojo que se ve, naranja; sonrisa
HUGO_D = (122, 106, 106, 255)
CHARS['hugo-severian'] = {
    'body': 'normal', 'pal': pal('#cacaca', '#fcd8bc', iris='#e08a2a', shade='#a8a8a8', deep='#868686'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(12, 90), (6, 64), (6, 34), (18, 8), (50, -4), (82, 8), (94, 34), (94, 64), (88, 90), (82, 70), (18, 70)]), HUGO_D),
              L(outline([(6, 56), (6, 34), (18, 8), (50, -4), (82, 8), (94, 34), (94, 56), (76, 48), (50, 46), (24, 48)])),
              L(outline([(60, 0), (84, 10), (94, 34), (94, 54), (80, 48)]), 'shade', 'b', False),
              L(outline([(14, 70), (16, 42), (30, 28), (50, 24), (66, 30), (64, 52), (58, 74), (52, 90, 1), (46, 74), (36, 84, 1), (30, 70), (22, 76, 1)]), 'mid', 'f'),
              L(outline([(14, 70), (30, 60), (46, 72), (52, 90), (36, 84), (22, 76)]), HUGO_D, 'f', False),
              L(quad((30, 34), (44, 28), (58, 32)), WHITE, 'f', False, False, 1.4)],
    'side': [L(outline([(74, 56), (86, 50), (92, 30), (84, 8), (60, -4), (34, -4), (14, 8), (2, 34), (2, 64), (10, 86), (26, 92), (36, 86), (38, 66), (46, 58), (60, 56),
                        (66, 76, 1), (70, 60)]), HUGO_D),
             L(outline([(92, 30), (84, 8), (60, -4), (34, -4), (14, 8), (2, 34), (2, 46), (30, 40), (60, 44), (86, 46)])),
             L(outline([(74, 22), (92, 34), (92, 52), (86, 70, 1), (80, 50)]), 'mid', 'f')],
    'back': [L(outline([(14, 84), (6, 60), (6, 32), (18, 8), (50, -4), (82, 8), (94, 32), (94, 60), (86, 84), (66, 90), (50, 92), (34, 90)]), HUGO_D),
             L(outline([(6, 54), (6, 32), (18, 8), (50, -4), (82, 8), (94, 32), (94, 54), (70, 56), (50, 50), (30, 56)])),
             L(quad((26, 18), (50, 10), (74, 18)), WHITE, 'b', False, False, 1.4)],
}

# Pharos Radris (Fado Lado, portero): piel morena; una mata grande de rastas gruesas gris oscuro que salen en todas
# direcciones y le caen por la frente, con la nuca rapada verde oliva; ojos verdes afilados y boca seria
OLIVE = (106, 106, 48, 255)


def _dreads(view):
    out = []

    def rope(a, b, c, w):  # rastas cortas y gordas: el mismo trazo recortado hacia la raíz
        from chars import rope as _r
        b2 = (a[0] + (b[0] - a[0]) * 0.8, a[1] + (b[1] - a[1]) * 0.8)
        c2 = (b2[0] + (c[0] - b[0]) * 0.4, b2[1] + (c[1] - b[1]) * 0.4)
        return _r(a, b2, c2, w + 3)
    if view == 'front':
        locks = [((14, 40), (2, 46), (-4, 62)), ((10, 24), (-4, 22), (-10, 30)), ((20, 8), (8, -6), (0, -10)), ((36, 0), (32, -16), (24, -22)), ((52, -2), (54, -18), (48, -26)),
                 ((68, 0), (76, -14), (74, -24)), ((82, 8), (96, 0), (102, 2)), ((88, 24), (104, 22), (108, 30)), ((86, 40), (98, 46), (102, 60))]
        for a, b, c in locks:
            out.append(L(rope(a, b, c, 9), 'mid'))
        for a, b, c in [((26, 20), (22, 40), (18, 66)), ((40, 22), (38, 46), (34, 60)), ((54, 22), (56, 44), (52, 56)), ((68, 20), (70, 40), (72, 62)), ((82, 26), (84, 44), (82, 64))]:
            out.append(L(rope(a, b, c, 9), 'mid', 'f', ln=True))
        return out
    if view == 'side':
        locks = [((60, 10), (80, 2), (96, 6)), ((70, 24), (90, 22), (100, 30)), ((40, 0), (44, -16), (40, -26)), ((22, 6), (14, -8), (4, -12)), ((8, 22), (-6, 18), (-14, 24)),
                 ((4, 40), (-10, 46), (-14, 58)), ((14, 56), (6, 70), (4, 80))]
        for a, b, c in locks:
            out.append(L(rope(a, b, c, 9), 'mid'))
        out.append(L(rope((76, 36), (86, 46), (88, 60), 8), 'mid', 'f', ln=True))
        return out
    locks = [((14, 40), (0, 46), (-6, 62)), ((10, 24), (-6, 22), (-10, 30)), ((20, 8), (8, -6), (0, -10)), ((36, 0), (32, -16), (26, -24)), ((52, -2), (54, -18), (48, -26)),
             ((68, 0), (76, -14), (74, -24)), ((82, 8), (96, 0), (102, 2)), ((88, 24), (104, 22), (108, 30)), ((86, 40), (100, 46), (104, 60))]
    for a, b, c in locks:
        out.append(L(rope(a, b, c, 9), 'mid'))
    for x in (26, 40, 56, 70):
        out.append(L(rope((x, 16), (x, 34), (x + 2, 52), 9), 'mid', 'f', ln=True))
    return out


def _mop(cx, cy, rx, ry, n=10, a0=0.0):
    import math
    pts = []
    for i in range(n * 2):
        a = a0 + math.pi * 2 * i / (n * 2)
        k = 1.0 if i % 2 == 0 else 0.84
        pts.append((cx + rx * k * math.cos(a), cy + ry * k * math.sin(a)))
    return blob(pts, 6)


_LOCKS_F = [((24, 24), (20, 44), (16, 62)), ((38, 22), (36, 44), (32, 58)), ((54, 22), (56, 42), (52, 56)), ((68, 22), (70, 42), (72, 60)), ((82, 28), (84, 46), (84, 62))]
CHARS['pharos-radris'] = {
    'body': 'normal', 'pal': pal('#6a6460', '#b07a4a', iris='#8ac040', shade='#54504c', deep='#3e3a38'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': [L(_mop(50, 18, 58, 38, 9, 0.2)), L(outline([(60, -14), (90, -2), (106, 22), (96, 48), (80, 40)]), 'shade', 'b', False),
              L(rope((14, 40), (6, 56), (8, 70), 10)), L(rope((86, 40), (94, 56), (92, 70), 10))]
             + [L(rope(a, b, c, 10), 'mid', 'f', ln=True) for a, b, c in _LOCKS_F]
             + [strand([(30, -6), (36, 10)], 'deep', 'b', 1.4), strand([(60, -8), (64, 8)], 'deep', 'b', 1.4)],
    'side': [L(outline([(10, 50), (40, 46), (46, 60), (38, 76), (20, 82), (8, 70)]), OLIVE),
             L(_mop(46, 20, 56, 38, 9, 0.4)), L(outline([(-8, 20), (30, 30), (40, 50), (6, 54)]), 'shade', 'b', False),
             L(rope((8, 40), (0, 58), (4, 74), 10)), L(rope((78, 30), (88, 46), (90, 62), 10), 'mid', 'f', ln=True)],
    'back': [L(outline([(18, 76), (14, 50), (86, 50), (82, 76), (66, 84), (50, 86), (34, 84)]), OLIVE),
             L(_mop(50, 20, 58, 40, 9, 0.2)), L(outline([(56, -16), (90, -2), (106, 24), (96, 52), (64, 56)]), 'shade', 'b', False)]
            + [L(rope((x, 30), (x + 2, 46), (x, 62), 10), 'mid', 'b', ln=True) for x in (20, 36, 52, 68, 82)],
}
