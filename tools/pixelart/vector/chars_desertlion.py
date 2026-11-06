"""Desert Lion / Leones del Desierto (IE3, Qatar): pañuelos anudados, rizos, barbas y máscaras, con sus modelos 3D como
referencia (contornos calcados sobre una rejilla de unidades de cabeza)."""
from chars import CHARS, L, OUTC, blob, ell, messy, outline, pal, rope, spk, strand
from chars_alius import LONG_FACE, SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE
from chars_bigwaves import side_eye, white_eyes
from heads import quad

WHITE = (250, 250, 250, 255)


def bald(view):
    if view == 'front':
        return [L(blob(SKULL_F), 'skin'), L(blob([(62, 12), (86, 34), (84, 62), (72, 58)], 6), 'skin_d', 'b', False)]
    if view == 'side':
        return [L(blob(SIDE_SKULL), 'skin')]
    return [L(blob(SKULL_B), 'skin'), L(blob([(58, 12), (86, 36), (84, 68), (66, 84)], 6), 'skin_d', 'b', False)]


def bandana(view, c='cloth', cd='cloth_d', low=58, tails=True, tail_side=1):
    """Pañuelo anudado que cubre la cabeza hasta la frente, con el nudo y dos puntas detrás."""
    if view == 'front':
        out = [L(outline([(10, low + 2), (8, 26), (20, 6), (50, -2), (80, 6), (92, 26), (90, low + 2), (50, low - 4)]), c, 'f', ln=True),
               L(outline([(60, 2), (82, 10), (92, 32), (90, low), (72, low - 4), (70, 26)]), cd, 'f', False),
               L(quad((12, low - 8), (50, low - 14), (88, low - 8)), cd, 'f', False, False, 1.4)]
        if tails:
            x = 92 if tail_side > 0 else 8
            out.append(L(outline([(x, low - 4), (x + 10 * tail_side, low + 20), (x + 6 * tail_side, low + 34, 1), (x - 2 * tail_side, low + 12)]), c, 'f', ln=True))
        return out
    if view == 'side':
        out = [L(outline([(4, low + 4), (4, 22), (20, 4), (50, -4), (78, 4), (92, 22), (92, low - 2), (60, low - 6), (30, low)]), c, 'f', ln=True),
               L(outline([(6, 30), (30, 30), (34, low - 2), (6, low + 2)]), cd, 'f', False)]
        if tails:
            out += [L(outline([(10, low - 8), (-8, low + 10), (-12, low + 30, 1), (0, low + 12), (12, low)]), c, 'f', ln=True),
                    L(ell(8, low - 6, 6, 5), cd, 'f', ln=True)]
        return out
    out = [L(outline([(6, low + 4), (6, 24), (20, 4), (50, -4), (80, 4), (94, 24), (94, low + 4), (50, low)]), c, 'f', ln=True),
           L(outline([(56, 0), (84, 10), (94, 34), (94, low), (66, low)]), cd, 'f', False)]
    if tails:
        out += [L(outline([(46, low - 2), (28, low + 18), (32, low + 34, 1), (44, low + 14), (50, low)]), c, 'f', ln=True),
                L(outline([(54, low - 2), (72, low + 18), (68, low + 34, 1), (56, low + 14), (50, low)]), c, 'f', ln=True),
                L(ell(50, low - 2, 6, 5), cd, 'f', ln=True)]
    return out


def side_puffs(view, y=72, c='mid', back_low=86):
    """Mechones rizados que salen por los lados bajo un pañuelo (zack, rajab)."""
    if view == 'front':
        return [L(outline([(16, y - 18), (-4, y - 16), (-14, y - 4, 1), (-4, y + 6), (-12, y + 16, 1), (6, y + 16), (18, y + 6)]), c, 'b', ln=True),
                L(outline([(84, y - 18), (104, y - 16), (114, y - 4, 1), (104, y + 6), (112, y + 16, 1), (94, y + 16), (82, y + 6)]), c, 'b', ln=True)]
    if view == 'side':
        return [L(outline([(36, y - 20), (14, y - 22), (-2, y - 10, 1), (6, y), (-4, y + 10, 1), (14, y + 14), (34, y + 6)]), c, 'b', ln=True)]
    return [L(outline([(16, y - 20), (-6, y - 16), (-16, y - 2, 1), (-6, y + 8), (-12, y + 18, 1), (8, y + 18), (30, y + 10), (50, y + 14), (70, y + 10), (92, y + 18),
                       (112, y + 18, 1), (106, y + 8), (116, y - 2, 1), (106, y - 16), (84, y - 20)]), c, 'b', ln=True)]


def beard(view, c='mid', chin=118, top=64, inner=None):
    """Barba que sale de las patillas y rodea la mandíbula (inner: hueco de la boca)."""
    if view == 'front':
        return [L(outline([(10, top), (18, top), (22, 96), (34, 108), (50, 110), (66, 108), (78, 96), (82, top), (90, top), (90, 100), (76, 116), (60, chin), (50, chin + 4, 1),
                           (40, chin), (24, 116), (10, 100)]), c, 'f', ln=True)]
    if view == 'side':
        return [L(outline([(50, top), (58, top), (64, 98), (78, 108), (90, 104), (92, 112), (80, chin), (62, chin + 2), (52, 104)]), c, 'f', ln=True)]
    return []


def rect_shades(view, y=76, c='lens'):
    if view == 'front':
        return [L(outline([(14, y - 6), (46, y - 6), (44, y + 6), (20, y + 8), (14, y + 2)]), c, 'f', ln=True),
                L(outline([(86, y - 6), (54, y - 6), (56, y + 6), (80, y + 8), (86, y + 2)]), c, 'f', ln=True),
                L([(46, y - 3), (54, y - 3)], c, 'f', False, False, 1.6)]
    if view == 'side':
        return [L(outline([(76, y - 6), (94, y - 6), (94, y + 6), (78, y + 6)]), c, 'f', ln=True), L([(50, y - 3), (76, y - 3)], c, 'f', False, False, 1.6)]
    return []


# Nasir Mustafa (portero): piel morena; pelo castaño muy oscuro en mechones de rizos en punta que se abren hacia fuera en
# todas direcciones y le bajan en patillas; perilla, ojos dorados rasgados y media sonrisa
CHARS['nasir-mustafa'] = {
    'body': 'normal', 'pal': pal('#3a1e1e', '#a86a3a', iris='#d0a020', shade='#2a1414'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': [(12, 70), (16, 46), (28, 40), (40, 48), (50, 42), (60, 48), (72, 40), (84, 46), (88, 70)]},
    'front': messy('front', 18, 10, seed=401, rx=54, ry=44, cy=40, lo=72)
             + [L(outline([(12, 66), (20, 66), (24, 86), (18, 90)]), 'mid', 'f'), L(outline([(88, 66), (80, 66), (76, 86), (82, 90)]), 'mid', 'f'),
                L(outline([(40, 104), (50, 100), (60, 104), (54, 112), (50, 116, 1), (46, 112)]), 'mid', 'f', ln=True)],
    'side': messy('side', 20, 9, seed=401, rx=50, ry=44, cy=40, nape=96, sweep=-0.3)
            + [L(outline([(50, 62), (58, 62), (62, 90), (56, 96)]), 'mid', 'f'), L(outline([(82, 102), (90, 102), (86, 112, 1)]), 'mid', 'f', ln=True)],
    'back': messy('back', 18, 10, seed=401, rx=54, ry=44, cy=40, nape=96),
}
# Faraz Farooq: gordo de cara redonda y enorme; un pañuelo verde oscuro anudado con las puntas a los lados, un antifaz de
# cejas negras pobladas con ojos blancos redondos, la nariz naranja de bola y un bigote espeso
FARAZ_FACE = blob([(10, 50), (50, 42), (90, 50), (100, 80), (94, 108), (72, 122), (28, 122), (6, 108), (0, 80)])
CHARS['faraz-farooq'] = {
    'body': 'corpulento', 'pal': pal('#3a2018', '#c8844a', cloth='#2e5a3e', cloth_d='#1e4430', nose='#e87a4a', brow='#1e1414'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': FARAZ_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 9},
    'front': [L(blob(SKULL_F), 'skin')] + bandana('front', low=52, tails=False)
             + [L(outline([(10, 48), (-6, 52), (-2, 62, 1), (12, 56)]), 'cloth', 'f', ln=True), L(outline([(90, 48), (106, 52), (102, 62, 1), (88, 56)]), 'cloth', 'f', ln=True),
                L(outline([(18, 68), (32, 60), (46, 66), (50, 72), (54, 66), (68, 60), (82, 68), (78, 82), (60, 80), (50, 76), (40, 80), (22, 82)]), 'brow', 'f', ln=True),
                L(ell(34, 73, 6, 5.6), WHITE, 'f', False), L(ell(66, 73, 6, 5.6), WHITE, 'f', False),
                L(ell(34, 73, 2.2, 2.2), OUTC, 'f', False), L(ell(66, 73, 2.2, 2.2), OUTC, 'f', False),
                L(outline([(30, 104), (40, 94), (50, 96), (60, 94), (70, 104), (60, 100), (50, 102), (40, 100)]), 'mid', 'f', ln=True),
                L(ell(50, 88, 7, 5.6), 'nose', 'f', ln=True),
                L(quad((34, 110), (50, 116), (66, 110)), OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(28, 110), (10, 80), (12, 30), (40, 10), (70, 14), (92, 36), (100, 70), (100, 104), (82, 122), (50, 124)]), 'skin')] + bandana('side', low=48)
             + [L(outline([(76, 66), (96, 66), (96, 80), (80, 80)]), 'brow', 'f', ln=True), L(ell(88, 73, 3.4, 4.6), WHITE, 'f', False), L(ell(89, 73, 1.4, 1.8), OUTC, 'f', False),
                L(ell(102, 88, 5, 5), 'nose', 'f', ln=True), L(outline([(88, 96), (104, 96), (100, 104), (88, 104)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(10, 96), (8, 30), (30, 10), (70, 10), (92, 30), (92, 96), (50, 106)]), 'skin'),
             L(outline([(56, 14), (88, 30), (92, 90), (60, 100)]), 'skin_d', 'b', False),
             L(outline([(14, 70), (50, 62), (86, 70), (86, 90), (50, 94), (14, 90)]), 'mid', 'b', False)]
            + bandana('back', low=50, tails=False)
            + [L(outline([(48, 44), (6, 30), (-24, 40), (-10, 52), (40, 52)]), 'cloth', 'f', ln=True),
               L(outline([(52, 44), (94, 30), (124, 40), (110, 52), (60, 52)]), 'cloth', 'f', ln=True), L(ell(50, 48, 7, 6), 'cloth_d', 'f', ln=True)],
}
# Bilal Kalil: piel morena; melena verde azulado larga y ondulada hasta los hombros, con mechones sueltos que le caen por la
# cara y le tapan el ojo derecho; el otro, verde, y la boca seria
CHARS['bilal-kalil'] = {
    'body': 'normal', 'pal': pal('#1e7470', '#9a6438', iris='#8ab04a', shade='#145452'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False, 'ears': False},
    'front': [L(outline([(-10, 110, 1), (-2, 90), (-12, 78, 1), (-2, 66), (-6, 40), (10, 12), (40, -4), (66, 0), (90, 14), (104, 40), (100, 66), (110, 80, 1), (98, 90),
                         (106, 110, 1), (88, 102), (84, 66), (16, 66), (12, 102)])),
              L(outline([(60, 2), (90, 18), (104, 50), (98, 96), (88, 100), (80, 50)]), 'shade', 'b', False),
              L(outline([(10, 74, 1), (12, 44), (28, 24), (50, 16), (72, 22), (88, 40), (92, 72, 1), (82, 58), (74, 76, 1), (68, 62), (58, 92, 1), (50, 62), (42, 76, 1),
                         (36, 54), (26, 66, 1), (18, 54)]), 'mid', 'f'),
              L(outline([(54, 20), (76, 28), (88, 48), (80, 60), (66, 44)]), 'shade', 'f', False),
              strand([(30, 26), (36, 48), (32, 64)], 'shade', 'f', 1.0)],
    'side': [L(outline([(56, 70), (54, 100), (44, 112, 1), (34, 98), (24, 116, 1), (16, 100), (0, 110, 1), (0, 84), (-10, 70, 1), (0, 56), (2, 30), (18, 8), (48, -4), (76, 4),
                        (94, 24), (96, 50), (92, 70, 1), (84, 52), (70, 50), (62, 54)])),
             L(outline([(4, 40), (30, 40), (46, 80), (40, 104), (16, 104), (4, 82)]), 'shade', 'b', False)],
    'back': [L(outline([(-10, 110, 1), (-2, 90), (-12, 78, 1), (-2, 66), (-6, 40), (10, 12), (40, -4), (66, 0), (90, 14), (104, 40), (100, 66), (110, 80, 1), (98, 90),
                        (106, 110, 1), (84, 104), (72, 118, 1), (60, 104), (48, 118, 1), (38, 104), (24, 114, 1), (12, 102)])),
             L(outline([(58, 2), (90, 18), (104, 50), (98, 100), (72, 112), (64, 50)]), 'shade', 'b', False)],
}
# Jamila Wali: pelo castaño rojizo de rizos que le caen en tirabuzones a los lados, con un rizo en espiral en lo alto, una
# cinta dorada fina en la frente y dos orejas de camello marrones; ojos entornados con pestañas y boca de gato
CHARS['jamila-wali'] = {
    'body': 'chica', 'pal': pal('#8a3a20', '#fcc880', iris='#8a2a1a', shade='#6a2a16', band='#d8a040', ear='#9a6a40', ear_d='#6a4428'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False, 'ears': False},
    'front': [L(outline([(16, 22), (4, 4), (-2, -6, 1), (10, 2), (24, 14)]), 'ear', 'b', ln=True), L(outline([(84, 22), (96, 4), (102, -6, 1), (90, 2), (76, 14)]), 'ear', 'b', ln=True),
              L(outline([(14, 18), (8, 6), (18, 10)]), 'ear_d', 'b', False), L(outline([(86, 18), (92, 6), (82, 10)]), 'ear_d', 'b', False),
              L(outline([(16, 60), (12, 30), (24, 10), (50, 2), (76, 10), (88, 30), (84, 60)])),
              L(outline([(60, 6), (84, 20), (88, 46), (80, 56), (74, 30)]), 'shade', 'b', False),
              L(ell(48, -6, 6, 6), 'mid', 'b', ln=True), L(ell(48, -6, 2.6, 2.6), 'shade', 'b', False),
              L(quad((16, 46), (50, 36), (84, 46)), 'band', 'f', False, False, 2.4)]
             + [L(ell(x, y, 8, 7), 'mid', 'f', ln=True) for x, y in ((12, 70), (6, 86), (14, 100), (88, 70), (94, 86), (86, 100))]
             + [L(ell(x, y, 3, 2.6), 'shade', 'f', False) for x, y in ((12, 70), (6, 86), (14, 100), (88, 70), (94, 86), (86, 100))]
             + [L(outline([(16, 52), (30, 40), (44, 46), (34, 54), (24, 60)]), 'mid', 'f', ln=True), L(outline([(84, 52), (70, 40), (56, 46), (66, 54), (76, 60)]), 'mid', 'f', ln=True),
                L(ell(34, 76, 6.4, 5.4), WHITE, 'f', ln=True), L(ell(66, 76, 6.4, 5.4), WHITE, 'f', ln=True),
                L(ell(34, 77, 3, 3), 'iris', 'f', False), L(ell(66, 77, 3, 3), 'iris', 'f', False),
                L(outline([(27, 73), (41, 73), (41, 70), (27, 70)]), 'skin', 'f', False), L(outline([(59, 73), (73, 73), (73, 70), (59, 70)]), 'skin', 'f', False),
                L([(27, 73), (41, 73)], OUTC, 'f', False, False, 1.8), L([(59, 73), (73, 73)], OUTC, 'f', False, False, 1.8),
                L([(44, 92), (47, 95), (50, 92), (53, 95), (56, 92)], OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(48, 30), (40, 8), (34, -6, 1), (50, 2), (58, 24)]), 'ear', 'b', ln=True),
             L(outline([(44, 92), (14, 94), (-6, 70), (-2, 40), (14, 14), (46, 2), (76, 8), (92, 26), (92, 46), (78, 44), (64, 50), (54, 64), (50, 80)])),
             L(outline([(0, 50), (30, 46), (46, 80), (16, 94)]), 'shade', 'b', False),
             L(ell(40, -4, 6, 6), 'mid', 'b', ln=True),
             L(quad((10, 40), (50, 30), (92, 40)), 'band', 'f', False, False, 2.4),
             L(ell(52, 82, 8, 7), 'mid', 'f', ln=True), L(ell(46, 98, 7, 6), 'mid', 'f', ln=True),
             L(ell(84, 76, 3.4, 4.6), WHITE, 'f', ln=True), L([(80, 73), (88, 73)], OUTC, 'f', False, False, 1.8)],
    'back': [L(outline([(16, 22), (4, 4), (-2, -6, 1), (10, 2), (24, 14)]), 'ear', 'b', ln=True), L(outline([(84, 22), (96, 4), (102, -6, 1), (90, 2), (76, 14)]), 'ear', 'b', ln=True),
             L(outline([(-6, 86), (-4, 50), (10, 14), (50, 2), (90, 14), (104, 50), (106, 86), (90, 104), (50, 108), (10, 104)])),
             L(outline([(56, 6), (90, 20), (104, 60), (100, 100), (70, 104)]), 'shade', 'b', False),
             L(ell(48, -6, 6, 6), 'mid', 'b', ln=True),
             L(quad((4, 40), (50, 30), (96, 40)), 'band', 'f', False, False, 2.4)]
            + [L(ell(x, 104, 7, 6), 'mid', 'f', ln=True) for x in (6, 28, 50, 72, 94)],
}
# Musa Sylla: grandullón de cara alargada con una melena castaña rojiza que le baja en patillas enormes hasta una barba
# cerrada, y arriba un tupé corto de pinchos gruesos; ojos blancos furiosos, nariz gorda naranja y los dientes apretados
MUSA_FACE = blob([(14, 30), (50, 24), (86, 30), (90, 70), (86, 104), (66, 118), (34, 118), (14, 104), (10, 70)])
CHARS['musa-sylla'] = {
    'body': 'corpulento', 'pal': pal('#6a2a1e', '#c87e48', nose='#e08848', shade='#4e1e14'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': MUSA_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 8},
    'front': [L(outline([(12, 60), (12, 14), (20, 2), (22, -14, 1), (30, 0), (36, -16, 1), (44, -2), (50, -18, 1), (56, -2), (64, -16, 1), (70, 0), (78, -14, 1),
                         (80, 2), (88, 14), (88, 60), (76, 44), (60, 40), (50, 48), (40, 40), (24, 44)])),
              L(outline([(60, 0), (80, 4), (88, 30), (84, 50), (72, 30)]), 'shade', 'b', False),
              L(outline([(26, 50), (40, 46), (50, 54), (60, 46), (74, 50), (66, 56), (50, 60), (34, 56)]), 'shade', 'f', False)]
             + beard('front', chin=120, top=52)
             + [L(outline([(24, 70), (40, 66), (42, 74), (28, 78)]), WHITE, 'f', ln=True), L(outline([(76, 70), (60, 66), (58, 74), (72, 78)]), WHITE, 'f', ln=True),
                L([(22, 64), (42, 70)], OUTC, 'f', False, False, 2.6), L([(78, 64), (58, 70)], OUTC, 'f', False, False, 2.6),
                L(outline([(42, 76), (58, 76), (64, 90), (56, 96), (44, 96), (36, 90)]), 'nose', 'f', ln=True),
                L(outline([(32, 100), (68, 100), (66, 110), (34, 110)]), WHITE, 'f', ln=True), L([(34, 105), (66, 105)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(36, 112), (16, 104), (10, 60), (10, 10), (30, -4), (34, -16, 1), (44, -4), (54, -14, 1), (60, 0), (82, 6), (92, 24), (92, 50), (94, 100), (80, 118),
                        (60, 120)]), 'skin'),
             L(outline([(10, 70), (10, 10), (30, -4), (60, 0), (82, 6), (70, 14), (44, 20), (34, 50), (32, 80), (44, 110), (20, 106)])),
             L(outline([(4, 40), (-12, 34), (-10, 46), (4, 50)]), 'mid', 'b', ln=True)]
            + beard('side', chin=124, top=50)
            + [L(outline([(78, 70), (92, 68), (92, 76), (80, 78)]), WHITE, 'f', ln=True), L([(76, 66), (92, 70)], OUTC, 'f', False, False, 2.4),
               L(outline([(90, 78), (104, 86), (98, 96), (88, 94)]), 'nose', 'f', ln=True), L(outline([(84, 100), (94, 100), (94, 108), (86, 108)]), WHITE, 'f', ln=True)],
    'back': [L(outline([(12, 100), (12, 14), (20, 2), (22, -14, 1), (30, 0), (36, -16, 1), (44, -2), (50, -18, 1), (56, -2), (64, -16, 1), (70, 0), (78, -14, 1), (80, 2),
                        (88, 14), (88, 100), (70, 88), (50, 96, 1), (30, 88)])),
             L(outline([(56, 0), (82, 6), (88, 40), (86, 96), (70, 86)]), 'shade', 'b', False)],
}
# Yusuf Massoud: un pañuelo azul grisáceo y crema anudado con dos puntas largas que le cuelgan a los lados; pelo morado
# oscuro con pico en la frente y patillas en punta; cejas gruesas moradas, ojos cerrados con pestañas y bigote fino
CHARS['yusuf-massoud'] = {
    'body': 'normal', 'pal': pal('#3a2a6a', '#e8b88a', cloth='#5a6a8a', cloth_d='#e8dcc0', iris='#3a2a2a'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'line', 'mouth_y': 98, 'face_front': LONG_FACE, 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin'),
              L(outline([(14, 66), (14, 50), (36, 46), (50, 60, 1), (64, 46), (86, 50), (86, 66), (80, 56), (60, 54), (50, 64), (40, 54), (20, 56)]), 'mid', 'f'),
              L(outline([(14, 60), (2, 66, 1), (14, 70)]), 'mid', 'f', ln=True), L(outline([(86, 60), (98, 66, 1), (86, 70)]), 'mid', 'f', ln=True)]
             + bandana('front', 'cloth', 'cloth_d', low=48, tails=False)
             + [L(outline([(12, 44), (-6, 70), (-10, 100, 1), (6, 76), (18, 52)]), 'cloth', 'f', ln=True),
                L(outline([(88, 44), (106, 70), (110, 100, 1), (94, 76), (82, 52)]), 'cloth_d', 'f', ln=True),
                L(outline([(24, 66), (34, 62), (44, 68), (34, 68)]), 'mid', 'f', False), L(outline([(76, 66), (66, 62), (56, 68), (66, 68)]), 'mid', 'f', False),
                L(outline([(34, 92), (44, 88), (50, 90), (56, 88), (66, 92), (56, 92), (50, 94), (44, 92)]), 'mid', 'f', ln=True)],
    'side': [L(blob(SIDE_SKULL), 'skin'),
             L(outline([(14, 64), (12, 40), (40, 44), (60, 54), (64, 62), (40, 60), (26, 70)]), 'mid', 'f')]
            + bandana('side', 'cloth', 'cloth_d', low=44)
            + [L(outline([(76, 92), (90, 90), (94, 94), (80, 96)]), 'mid', 'f', ln=True)],
    'back': [L(blob(SKULL_B), 'skin'), L(outline([(16, 84), (14, 50), (86, 50), (84, 84), (50, 90)]), 'mid', 'b')]
            + bandana('back', 'cloth', 'cloth_d', low=48)
            + [L(outline([(10, 46), (-6, 70), (-10, 100, 1), (6, 76), (16, 54)]), 'cloth_d', 'f', ln=True),
               L(outline([(90, 46), (106, 70), (110, 100, 1), (94, 76), (84, 54)]), 'cloth', 'f', ln=True)],
}
# Sulayk Sulaiman: pelo amarillo verdoso abultado y despeinado, con flequillo de mechones en punta hasta los ojos; una
# mascarilla negra que le tapa la nariz y la boca, atada detrás; ojos verdes de enfado
CHARS['sulayk-sulaiman'] = {
    'body': 'normal', 'pal': pal('#c8c040', '#a87040', iris='#2a8a7a', shade='#9a9028', mask='#24262a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'hairline': False},
    'front': messy('front', 6, 12, seed=402, rx=56, ry=46, cy=38, lo=70)
             + [L(outline([(10, 68, 1), (14, 40), (28, 24), (50, 18), (72, 24), (86, 40), (90, 68, 1), (80, 54), (72, 64, 1), (64, 50), (56, 62, 1), (50, 50), (44, 62, 1),
                           (36, 50), (28, 64, 1), (20, 54)]), 'mid', 'f'),
                L(outline([(56, 22), (78, 30), (88, 50), (78, 54), (70, 40)]), 'shade', 'f', False),
                L(outline([(14, 84), (50, 80), (86, 84), (84, 104), (64, 114), (36, 114), (16, 104)]), 'mask', 'f', ln=True)],
    'side': messy('side', 7, 10, seed=402, rx=52, ry=46, cy=38, nape=94, sweep=-0.2)
            + [L(outline([(48, 82), (98, 84), (96, 106), (74, 116), (52, 108)]), 'mask', 'f', ln=True),
               L(outline([(40, 84), (26, 96), (22, 110, 1), (32, 98), (42, 92)]), 'mask', 'f', ln=True)],
    'back': messy('back', 6, 12, seed=402, rx=56, ry=46, cy=38, nape=96)
            + [L(ell(50, 92, 5, 4), 'mask', 'f', ln=True), L(outline([(48, 94), (42, 112, 1), (50, 100), (58, 112, 1), (52, 94)]), 'mask', 'f', ln=True)],
}
# Sayid Armand: piel morena; pelo verde azulado oscuro en mechones gruesos y abultados como nubes, y una barba del mismo
# color que le rodea la cara; ojos de sueño con pupilas arriba y labios gruesos
CHARS['sayid-armand'] = {
    'body': 'normal', 'pal': pal('#1e5458', '#a86a3a', shade='#143c40', lip='#c88a5a'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'none', 'hairline': False},
    'front': [L(outline([(12, 60), (8, 40), (-8, 30), (-6, 14), (8, 10), (14, 0), (30, 2), (40, -10), (60, -10), (70, 2), (86, 0), (92, 10), (106, 14), (108, 30), (92, 40),
                         (88, 60), (80, 50), (20, 50)])),
              L(outline([(60, -6), (84, 4), (104, 18), (100, 32), (86, 48), (78, 24)]), 'shade', 'b', False),
              L(outline([(14, 52), (30, 44), (50, 48), (70, 44), (86, 52), (70, 54), (50, 52), (30, 54)]), 'mid', 'f')]
             + beard('front', chin=118, top=58)
             + [L(outline([(36, 102), (50, 98), (64, 102), (58, 108), (42, 108)]), 'lip', 'f', ln=True)]
             + [L(ell(35, 76, 6, 5.4), WHITE, 'f', ln=True), L(ell(65, 76, 6, 5.4), WHITE, 'f', ln=True),
                L(ell(35, 73, 2, 2), OUTC, 'f', False), L(ell(65, 73, 2, 2), OUTC, 'f', False)],
    'side': [L(outline([(44, 92), (22, 88), (10, 64), (6, 30), (14, 4), (40, -8), (70, -6), (88, 8), (94, 28), (88, 42), (70, 44), (56, 52), (52, 66), (50, 80)])),
             L(outline([(8, 40), (34, 44), (42, 80), (22, 88), (10, 64)]), 'shade', 'b', False)]
            + beard('side', chin=122, top=56) + side_eye(76),
    'back': [L(outline([(10, 80), (6, 40), (-8, 30), (-6, 14), (8, 10), (14, 0), (30, 2), (40, -10), (60, -10), (70, 2), (86, 0), (92, 10), (106, 14), (108, 30), (94, 40),
                        (90, 80), (50, 88)])),
             L(outline([(56, -6), (84, 4), (104, 18), (100, 32), (90, 78), (64, 86)]), 'shade', 'b', False)],
}
# Mansur Jasim: cara larguísima y estrecha con la barbilla en punta; la cabeza rapada en verde grisáceo con una cresta
# verde oscuro peinada hacia atrás y atada en un moño en la nuca; un antifaz negro alrededor de los ojos blancos y la nariz
# larga; la boca, un círculo
MANSUR_FACE = blob([(16, 30), (50, 24), (84, 30), (84, 70), (72, 110), (50, 128), (28, 110), (16, 70)])
CHARS['mansur-jasim'] = {
    'body': 'delgado', 'pal': pal('#1e4434', '#b8783e', shave='#6a9a80', shave_d='#4e7a62', mask='#1e1e1e', nose='#7a3a1e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': MANSUR_FACE, 'hairline': False},
    'front': [L(outline([(16, 64), (14, 20), (26, 4), (50, -2), (74, 4), (86, 20), (84, 64)]), 'shave'),
              L(outline([(62, 4), (84, 18), (84, 60), (74, 40)]), 'shave_d', 'b', False),
              L(outline([(38, 30), (40, 4), (50, -2), (60, 4), (62, 30), (50, 26)]), 'mid', 'f', ln=True),
              L(outline([(16, 64), (30, 60), (50, 64), (70, 60), (84, 64), (84, 82), (64, 86), (50, 80), (36, 86), (16, 82)]), 'mask', 'f', ln=True),
              L(outline([(26, 70), (42, 68), (40, 76), (28, 76)]), WHITE, 'f', False), L(outline([(74, 70), (58, 68), (60, 76), (72, 76)]), WHITE, 'f', False),
              L(ell(34, 72, 1.8, 2), OUTC, 'f', False), L(ell(66, 72, 1.8, 2), OUTC, 'f', False),
              L(outline([(46, 62), (54, 62), (56, 96), (50, 100), (44, 96)]), 'nose', 'f', ln=True),
              L(ell(50, 116, 4.6, 4.2), (90, 40, 30, 255), 'f', ln=True)],
    'side': [L(outline([(40, 100), (14, 84), (10, 30), (26, 4), (56, 0), (80, 10), (88, 40), (84, 80), (72, 116), (56, 128), (44, 120)]), 'skin'),
             L(outline([(10, 70), (10, 30), (26, 4), (56, 0), (80, 10), (82, 30), (60, 40), (40, 60), (30, 80)]), 'shave'),
             L(outline([(70, 4), (40, -4), (14, 6), (0, 18), (-8, 30, 1), (8, 26), (30, 20), (60, 18)]), 'mid', 'f', ln=True),
             L(outline([(60, 64), (90, 64), (90, 80), (64, 80)]), 'mask', 'f', ln=True), L(outline([(80, 68), (88, 68), (88, 74), (80, 74)]), WHITE, 'f', False),
             L(outline([(86, 70), (100, 94), (90, 98)]), 'nose', 'f', ln=True)],
    'back': [L(outline([(16, 92), (14, 20), (26, 4), (50, -2), (74, 4), (86, 20), (84, 92), (50, 100)]), 'shave'),
             L(outline([(56, 2), (84, 18), (84, 88), (62, 96)]), 'shave_d', 'b', False),
             L(outline([(38, 30), (40, 4), (50, -2), (60, 4), (62, 30), (50, 40)]), 'mid', 'f', ln=True), L(ell(50, 40, 9, 9), 'mid', 'f', ln=True),
             L(ell(48, 38, 3, 3), 'shade', 'f', False)],
}
# Zack Abdulla: un pañuelo azul añil cubriéndole la cabeza, anudado con una punta que le cae por la derecha; por debajo
# asoman dos matas de rizos castaños a los lados; ojos castaños y sonrisa
CHARS['zack-abdulla'] = {
    'body': 'normal', 'pal': pal('#5a3a26', '#c8844a', iris='#8a4a1a', cloth='#4a52a8', cloth_d='#363e88'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': side_puffs('front', 66) + [L(blob(SKULL_F), 'skin')]
             + [L(outline([(36, 58), (44, 56), (46, 68), (38, 64)]), 'mid', 'f')] + bandana('front', 'cloth', 'cloth_d', low=56, tail_side=1),
    'side': side_puffs('side', 66) + [L(blob(SIDE_SKULL), 'skin')] + bandana('side', 'cloth', 'cloth_d', low=52, tails=False),
    'back': side_puffs('back', 66) + [L(blob(SKULL_B), 'skin'), L(ell(50, 74, 8, 7), 'mid', 'b', ln=True)] + bandana('back', 'cloth', 'cloth_d', low=56, tails=False),
}
# Majdi Ismail: pelo corto de puntas, mitad castaño oscuro y mitad crema en dos manchas que se separan en zigzag; cejas
# gruesas en punta, ojos negros redondos y una sonrisa enorme de dientes
CHARS['majdi-ismail'] = {
    'body': 'normal', 'pal': pal('#6a2a14', '#b87240', shade='#4e1e0e', cream='#f8d8b8'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 95, 'hairline': [(12, 64), (16, 46), (26, 52), (32, 40), (42, 50), (50, 38), (58, 50), (68, 40),
                                                                                            (74, 52), (84, 46), (88, 64)]},
    'front': messy('front', 7, 12, seed=403, rx=46, ry=40, cy=42, lo=66)
             + [L(outline([(50, 2), (64, 2), (82, 14), (94, 34), (94, 52), (86, 54), (76, 40), (70, 46), (64, 30), (56, 34), (52, 16)]), 'cream', 'b', False)],
    'side': messy('side', 8, 10, seed=403, rx=44, ry=40, cy=42, nape=92, sweep=-0.2),
    'back': messy('back', 7, 12, seed=403, rx=46, ry=40, cy=42, nape=94)
            + [L(outline([(6, 40), (14, 12), (40, 2), (46, 20), (40, 34), (48, 50), (40, 66), (46, 80), (20, 84), (6, 66)]), 'cream', 'b', False)],
}
# Talal Hamad (portero suplente): pelo gris azulado abultado y ondulado en mechones hacia arriba y a los lados, con una
# cinta naranja ancha en la frente; ojos verdes de enfado y la boca seria
CHARS['talal-hamad'] = {
    'body': 'normal', 'pal': pal('#4a6070', '#c88a54', iris='#2a7a6a', shade='#36485a', band='#d8601a', band_d='#a8460e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'face_front': LONG_FACE, 'hairline': False},
    'front': messy('front', 7, 12, seed=404, rx=56, ry=44, cy=38, lo=70)
             + [L(outline([(16, 48), (50, 42), (84, 48), (84, 60), (50, 54), (16, 60)]), 'band', 'f', ln=True),
                L(outline([(60, 44), (84, 48), (84, 60), (62, 56)]), 'band_d', 'f', False)],
    'side': messy('side', 8, 10, seed=404, rx=52, ry=44, cy=38, nape=94, sweep=-0.2)
            + [L(outline([(40, 44), (88, 46), (88, 58), (40, 56)]), 'band', 'f', ln=True)],
    'back': messy('back', 7, 12, seed=404, rx=56, ry=44, cy=38, nape=96)
            + [L(outline([(14, 44), (50, 38), (86, 44), (86, 56), (50, 50), (14, 56)]), 'band', 'f', ln=True)],
}
# Hasan Ahmed: pelo castaño con raya en medio, pegado y peinado hacia atrás, con las puntas abiertas en las patillas y la
# nuca; una cinta crema fina en la frente; ojos castaños de enfado
CHARS['hasan-ahmed'] = {
    'body': 'normal', 'pal': pal('#5a3420', '#b87a44', iris='#8a3a1a', shade='#42261a', band='#e8c890'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 96, 'hairline': [(14, 64), (16, 46), (30, 44), (50, 46), (70, 44), (84, 46), (86, 64)]},
    'front': [L(outline([(12, 70), (2, 80, 1), (10, 62), (8, 34), (20, 10), (50, 2), (80, 10), (92, 34), (90, 62), (98, 80, 1), (88, 70), (82, 64), (18, 64)])),
              L(outline([(60, 6), (84, 18), (92, 40), (88, 64), (78, 36)]), 'shade', 'b', False),
              strand([(50, 4), (50, 44)], 'deep', 'b', 1.2), L(quad((10, 42), (50, 32), (90, 42)), 'band', 'f', False, False, 2.4)],
    'side': [L(outline([(44, 92), (32, 102, 1), (24, 88), (10, 96, 1), (10, 70), (8, 34), (22, 10), (52, 2), (78, 8), (92, 28), (90, 44), (76, 46), (60, 50), (52, 64),
                        (50, 80)])),
             L(outline([(10, 40), (34, 44), (42, 84), (22, 90), (10, 70)]), 'shade', 'b', False),
             L(quad((8, 40), (50, 30), (92, 38)), 'band', 'f', False, False, 2.4)],
    'back': [L(outline([(12, 84), (8, 34), (20, 10), (50, 2), (80, 10), (92, 34), (88, 84), (76, 94, 1), (66, 86), (58, 98, 1), (50, 86), (42, 98, 1), (34, 86), (24, 94, 1)])),
             L(outline([(56, 4), (84, 18), (92, 48), (86, 82), (64, 88)]), 'shade', 'b', False),
             strand([(50, 4), (50, 88)], 'deep', 'b', 1.2), L(quad((8, 42), (50, 36), (92, 42)), 'band', 'f', False, False, 2.4)],
}
# Khalfan Jibril: cara muy alargada y huesuda, con mejillas marcadas; pelo castaño rojizo corto y rizado con un pico en la
# frente; ojos blancos de sueño, nariz larga recta, perilla y la boca en una raya
CHARS['khalfan-jibril'] = {
    'body': 'delgado', 'pal': pal('#8a3a1a', '#e8b878', shade='#6a2a12', skin_d='#c89458'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 102, 'face_front': LONG_FACE, 'hairline': False},
    'front': [L(outline([(12, 66), (6, 40), (14, 16), (36, 2), (64, 2), (86, 16), (94, 40), (88, 66), (80, 50), (64, 42), (50, 52, 1), (36, 42), (20, 50)])),
              L(outline([(60, 4), (84, 16), (92, 40), (86, 60), (74, 36)]), 'shade', 'b', False),
              L(outline([(14, 22), (30, 8), (40, 18), (24, 26)]), 'shade', 'b', False), L(outline([(56, 10), (72, 8), (76, 20), (62, 22)]), 'shade', 'b', False),
              L([(46, 64), (46, 92), (52, 94)], 'skin_d', 'f', False, False, 1.6), L([(28, 90), (34, 104)], 'skin_d', 'f', False, False, 1.2),
              L([(72, 90), (66, 104)], 'skin_d', 'f', False, False, 1.2),
              L(outline([(44, 108), (56, 108), (50, 120, 1)]), 'mid', 'f', ln=True),
              L(outline([(22, 68), (44, 68), (44, 72), (22, 72)]), OUTC, 'f', False), L(outline([(78, 68), (56, 68), (56, 72), (78, 72)]), OUTC, 'f', False),
              L(ell(34, 74, 6, 3), WHITE, 'f', False), L(ell(66, 74, 6, 3), WHITE, 'f', False), L(ell(34, 74.5, 1.4, 1.4), OUTC, 'f', False),
              L(ell(66, 74.5, 1.4, 1.4), OUTC, 'f', False)],
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (8, 36), (20, 10), (48, -2), (76, 4), (92, 22), (92, 40), (78, 44), (64, 48), (54, 62), (50, 80)])),
             L(outline([(10, 40), (36, 44), (42, 84), (22, 88), (12, 64)]), 'shade', 'b', False),
             L(outline([(78, 106), (90, 108), (86, 118, 1)]), 'mid', 'f', ln=True), L([(78, 70), (90, 70)], OUTC, 'f', False, False, 2.4)],
    'back': [L(outline([(12, 82), (6, 40), (14, 16), (36, 2), (64, 2), (86, 16), (94, 40), (88, 82), (50, 92)])),
             L(outline([(56, 4), (84, 16), (94, 44), (86, 80), (64, 88)]), 'shade', 'b', False)],
}
# Rajab Ismail: un pañuelo rosa anudado detrás con dos puntas largas que le caen por la espalda; por debajo, matas de rizos
# castaños a los lados; ojos negros redondos de pasmo y la boca seria
CHARS['rajab-ismail'] = {
    'body': 'normal', 'pal': pal('#4a2a1a', '#c8844a', cloth='#e8a8b0', cloth_d='#c88890'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': side_puffs('front', 66) + [L(blob(SKULL_F), 'skin'),
                                        L(outline([(16, 62), (24, 52), (40, 54), (50, 50), (60, 54), (76, 52), (84, 62), (70, 60), (50, 58), (30, 60)]), 'mid', 'f')]
             + bandana('front', 'cloth', 'cloth_d', low=52, tails=False) + white_eyes(76, 15, 6.4, 6.4, 3.2),
    'side': side_puffs('side', 66) + [L(blob(SIDE_SKULL), 'skin')] + bandana('side', 'cloth', 'cloth_d', low=48) + side_eye(76),
    'back': side_puffs('back', 66) + [L(blob(SKULL_B), 'skin')] + bandana('back', 'cloth', 'cloth_d', low=50)
            + [L(outline([(44, 56), (38, 100), (44, 120, 1), (50, 96)]), 'cloth', 'f', ln=True), L(outline([(56, 56), (62, 100), (56, 120, 1), (50, 96)]), 'cloth_d', 'f', ln=True)],
}
# Adel Siddique: piel morena; pelo verde azulado muy corto pegado al cráneo con un pico de puntas en la frente; gafas de
# sol azules en forma de corazón, cejas en punta y los labios gruesos en morro
CHARS['adel-siddique'] = {
    'body': 'normal', 'pal': pal('#3a7070', '#a8703e', shade='#285656', lens='#3a5ab0', lip='#c8946a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False, 'big_ears': 2, 'ear_out': 4},
    'front': [L(blob(SKULL_F), 'skin'),
              L(outline([(14, 58), (12, 30), (24, 10), (50, 2), (76, 10), (88, 30), (86, 58), (76, 40), (68, 52, 1), (62, 40), (56, 52, 1), (50, 40), (44, 52, 1), (38, 40),
                         (32, 52, 1), (24, 40)]), 'mid', 'f'),
              L(outline([(60, 6), (82, 18), (86, 46), (76, 36)]), 'shade', 'f', False),
              L(outline([(22, 66), (36, 62), (40, 68), (28, 70)]), 'shade', 'f', False), L(outline([(78, 66), (64, 62), (60, 68), (72, 70)]), 'shade', 'f', False),
              L(outline([(14, 70), (30, 68), (46, 72), (44, 84), (32, 88), (18, 82)]), 'lens', 'f', ln=True),
              L(outline([(86, 70), (70, 68), (54, 72), (56, 84), (68, 88), (82, 82)]), 'lens', 'f', ln=True),
              L([(46, 74), (54, 74)], 'lens', 'f', False, False, 1.6),
              L(outline([(40, 98), (50, 94), (60, 98), (56, 106), (44, 106)]), 'lip', 'f', ln=True)],
    'side': [L(blob(SIDE_SKULL), 'skin'),
             L(outline([(14, 66), (12, 34), (26, 10), (52, 2), (76, 8), (88, 26), (86, 40), (74, 36), (70, 46, 1), (62, 36), (44, 44), (30, 56), (22, 70)]), 'mid'),
             L(outline([(76, 68), (94, 66), (94, 82), (80, 84)]), 'lens', 'f', ln=True), L([(50, 70), (76, 70)], 'lens', 'f', False, False, 1.6),
             L(outline([(86, 96), (96, 96), (96, 104), (86, 104)]), 'lip', 'f', ln=True)],
    'back': [L(blob(SKULL_B), 'skin'),
             L(outline([(14, 74), (12, 30), (24, 10), (50, 2), (76, 10), (88, 30), (86, 74), (50, 80)])),
             L(outline([(56, 4), (82, 16), (88, 50), (84, 72), (60, 78)]), 'shade', 'b', False)],
}
