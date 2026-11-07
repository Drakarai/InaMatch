"""Instituto Colina Verde (ares-midorigaoka, Midorigaoka en Ares): sus modelos 3D de Inazuma Eleven Ares como referencia
(busto de frente, perfil y espalda, con la rejilla de unidades de cabeza). Todos con un toque de bicho: cuernos, antenas,
casco de saltamontes, boina de mariquita, ojos en espiral..."""
from chars import CHARS, L, OUTC, ell, longhair, outline, pal, rope, strand
from chars_alius import WIDE_FACE
from chars_bigwaves import side_eye, white_eyes
from heads import quad

WHITE = (250, 250, 250, 255)
BLACK = (28, 26, 28, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


def antenna(p0, c, p1, col='mid', w=3.0, z='b'):
    return L(quad(p0, c, p1), col, z, False, False, w)


def blush(y=86, sep=22, rx=5, ry=2.6):
    return [L(ell(50 - sep, y, rx, ry), 'blush', 'f', False), L(ell(50 + sep, y, rx, ry), 'blush', 'f', False)]


# ------------------------------------------------------------------ Wryn Twincrest (Futakado Nirou, portero)
# Grandullón de cara redonda y mofletes rosados; pelo castaño oscuro corto en casco con pico en la frente y dos mechones
# enormes curvados hacia arriba como cuernos; ojos redondos pequeños, nariz de botón y sonrisa ancha
_horn_l = [(22, 46), (12, 30), (14, 14), (24, 2, 1), (24, 16), (30, 30), (38, 40)]
_horn_r = [(100 - p[0], p[1]) + tuple(p[2:]) for p in _horn_l]
CHARS['wryn-twincrest'] = {
    'body': 'corpulento', 'pal': pal('#4a3426', '#f6c8a0', blush='#f4a8a0'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'eye_y': 72, 'eye_sep': 16, 'face_front': WIDE_FACE,
             'nose': (50, 80, 4), 'hairline': False, 'big_ears': 2, 'ear_out': 5},
    'front': [L(outline(_horn_l)), L(outline(_horn_r)),
              fringe([(10, 62), (12, 44), (26, 34), (50, 30), (74, 34), (88, 44), (90, 62), (80, 50), (62, 44), (50, 54, 1), (38, 44), (20, 50)]),
              L(outline([(56, 32), (78, 36), (88, 50), (76, 46)]), 'shade', 'f', False)] + blush(88, 25, 6, 3.4),
    'side': [L(outline([(54, 50), (70, 42), (84, 40), (84, 28), (70, 16), (48, 10), (26, 14), (10, 30), (6, 56), (10, 84), (22, 92), (36, 84), (40, 62)])),
             L(outline([(26, 22), (30, 4), (40, -8, 1), (44, 8), (48, 20)])),
             L(outline([(8, 46), (24, 50), (28, 80), (12, 80)]), 'shade', 'b', False), L(ell(82, 86, 5, 3), 'blush', 'f', False)],
    'back': [L(outline([(12, 90), (8, 58), (14, 40), (30, 30), (50, 28), (70, 30), (86, 40), (92, 58), (88, 90), (68, 98), (50, 100), (32, 98)])),
             L(outline(_horn_l)), L(outline(_horn_r)),
             L(outline([(54, 30), (86, 42), (90, 86), (64, 96)]), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Garvin Cliffmarch (Tonobata Gakuto)
# Casco de saltamontes verde claro con una franja amarilla en medio, dos ojos compuestos oscuros enormes a los lados, dos
# antenas largas y un antifaz amarillo con los ojos rosados de sueño; por debajo asoma el pelo largo oscuro
_gc_ant = [antenna((38, 4), (30, -18), (12, -36), 'ant', 3.0), antenna((62, 4), (70, -18), (88, -36), 'ant', 3.0)]
CHARS['garvin-cliffmarch'] = {
    'body': 'normal', 'pal': pal('#3a3a34', '#f2c49a', iris='#c04a7a', helm='#8cbc5a', helm_d='#6a6034', stripe='#e8d860', ceye='#4a4a3a',
                                 ant='#c8b08a', gold='#e8c848'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 96, 'eye_y': 66, 'eye_sep': 14, 'hairline': False},
    'front': _gc_ant + [
        L(outline([(14, 62), (8, 100), (14, 96), (18, 106, 1), (24, 92), (24, 64)])), L(outline([(86, 62), (92, 100), (86, 96), (82, 106, 1), (76, 92), (76, 64)])),
        L(outline([(12, 64), (8, 32), (20, 8), (50, -2), (80, 8), (92, 32), (88, 64), (78, 64), (76, 56), (24, 56), (22, 64)]), 'helm', 'f', ln=True),
        L(outline([(40, 0), (60, 0), (62, 56), (38, 56)]), 'stripe', 'f', False),
        L(ell(22, 38, 8, 11), 'ceye', 'f', ln=True), L(ell(78, 38, 8, 11), 'ceye', 'f', ln=True),
        L(ell(20, 33, 2.4, 3.2), WHITE, 'f', False), L(ell(80, 33, 2.4, 3.2), WHITE, 'f', False),
        L(outline([(24, 58), (46, 58), (48, 66), (46, 74), (24, 74), (22, 66)]) + [(24, 58)], 'stripe', 'f', False, False, 2.4),
        L(outline([(76, 58), (54, 58), (52, 66), (54, 74), (76, 74), (78, 66)]) + [(76, 58)], 'stripe', 'f', False, False, 2.4)],
    'side': [antenna((60, 4), (60, -20), (54, -40), 'ant', 3.0),
             L(outline([(18, 50), (-2, 84), (2, 104, 1), (12, 90), (16, 102, 1), (26, 80), (34, 60)])),
             L(outline([(14, 60), (10, 28), (26, 6), (56, -2), (80, 8), (94, 30), (96, 64), (88, 70), (84, 56), (60, 50), (40, 54), (24, 64)]), 'helm', 'f', ln=True),
             L(outline([(12, 58), (12, 38), (40, 40), (60, 48), (40, 54), (24, 64)]), 'helm_d', 'f', False),
             L(ell(70, 28, 9, 12), 'ceye', 'f', ln=True), L(ell(68, 23, 2.4, 3), WHITE, 'f', False),
             L(outline([(84, 58), (96, 58), (98, 72), (86, 74)]), 'stripe', 'f', ln=True)],
    'back': _gc_ant + [
        L(outline([(14, 60), (8, 96), (16, 92), (22, 104, 1), (32, 92), (40, 104, 1), (50, 94), (60, 104, 1), (68, 92), (78, 104, 1), (84, 92), (92, 96), (86, 60)])),
        L(outline([(12, 64), (8, 32), (20, 8), (50, -2), (80, 8), (92, 32), (88, 64), (50, 68)]), 'helm', 'f', ln=True),
        L(outline([(10, 40), (50, 30), (90, 40), (88, 64), (50, 68), (12, 64)]), 'helm_d', 'f', False)],
}

# ------------------------------------------------------------------ Therion Daywick (Kooro Norihiko)
# Piel morena, pelo negro en un tupé plano altísimo como un cubo, con una franja gris rapada en la base, gafas de sol de
# cristales a rayas de colores, y rastas negras largas que le caen por la nuca
_td_glass = [L(outline([(14, 70), (50, 66), (86, 70), (84, 84), (60, 86), (50, 80), (40, 86), (16, 84)]), BLACK, 'f', ln=True),
             L(outline([(20, 72), (44, 70), (46, 82), (22, 82)]), 'lens1', 'f', False),
             L(outline([(54, 70), (80, 72), (78, 82), (54, 82)]), 'lens1', 'f', False),
             L(outline([(28, 71), (34, 71), (32, 82), (26, 82)]), 'lens2', 'f', False), L(outline([(64, 71), (70, 71), (68, 82), (62, 82)]), 'lens2', 'f', False),
             L(outline([(36, 70), (42, 70), (40, 82), (34, 82)]), 'lens3', 'f', False), L(outline([(72, 71), (78, 72), (76, 82), (70, 82)]), 'lens3', 'f', False)]
CHARS['therion-daywick'] = {
    'body': 'normal', 'pal': pal('#2a2828', '#a8704a', band='#6a6464', lens1='#f0c020', lens2='#4060c8', lens3='#e03070'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(12, 86), (6, 112), (14, 104), (16, 116, 1), (22, 96)])), L(outline([(88, 86), (94, 112), (86, 104), (84, 116, 1), (78, 96)])),
              L(outline([(18, 56), (18, -30), (82, -30), (82, 56), (60, 50), (50, 58, 1), (40, 50)]), 'mid', 'f', ln=True),
              L(outline([(18, 40), (30, 42), (30, 50), (18, 56)]), 'band', 'f', False), L(outline([(82, 40), (70, 42), (70, 50), (82, 56)]), 'band', 'f', False),
              L(outline([(60, -30), (82, -30), (82, 40), (64, 44)]), 'shade', 'f', False)] + _td_glass,
    'side': [L(rope((24, 54), (4, 70), (-6, 104), 5)), L(rope((30, 56), (12, 78), (6, 108), 5)), L(rope((20, 50), (-8, 62), (-14, 90), 4)),
             L(outline([(24, 64), (20, -30), (84, -30), (88, 44), (74, 50), (52, 52), (34, 62)]), 'mid', 'f', ln=True),
             L(outline([(22, 40), (86, 34), (88, 44), (74, 50), (52, 52), (34, 62), (24, 64)]), 'band', 'f', False),
             L(outline([(74, 66), (96, 64), (96, 78), (78, 80)]), BLACK, 'f', ln=True), L(outline([(80, 68), (94, 67), (93, 76), (81, 77)]), 'lens2', 'f', False)],
    'back': [L(outline([(16, 84), (8, 112), (24, 104), (30, 118, 1), (40, 104), (50, 118, 1), (60, 104), (70, 118, 1), (76, 104), (92, 112), (84, 84)])),
             L(outline([(18, 86), (18, -30), (82, -30), (82, 86), (74, 80), (66, 88), (58, 80), (50, 88), (42, 80), (34, 88), (26, 80)]), 'mid', 'f', ln=True),
             L(outline([(18, 40), (82, 40), (82, 86), (74, 80), (66, 88), (58, 80), (50, 88), (42, 80), (34, 88), (26, 80), (18, 86)]), 'band', 'f', False)],
}

# ------------------------------------------------------------------ Sylvar Verdis (Kanafumi Rokuri)
# Melena verde lisa cortada en recto a la altura de la barbilla, flequillo en pico entre los ojos y dos brotes de antena en lo
# alto; ojos negros de mirada seria
_sv_ant = [antenna((38, -2), (34, -12), (28, -18), 'mid', 3.2), antenna((62, -2), (66, -12), (72, -18), 'mid', 3.2),
           L(ell(28, -18, 3, 2.4), 'mid', 'b', False), L(ell(72, -18, 3, 2.4), 'mid', 'b', False)]
CHARS['sylvar-verdis'] = {
    'body': 'normal', 'pal': pal('#5a8a48', '#fcd0a8', iris='#1e1414', shade='#3e6a34'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': _sv_ant + [
        L(outline([(10, 104), (6, 40), (18, 6), (50, -6), (82, 6), (94, 40), (90, 104), (80, 106), (80, 64), (20, 64), (20, 106)])),
        L(outline([(60, -2), (84, 8), (94, 44), (90, 100), (82, 102), (80, 50)]), 'shade', 'b', False),
        fringe([(12, 62), (14, 30), (30, 10), (50, 4), (70, 10), (86, 30), (88, 62), (80, 54), (72, 60, 1), (64, 48), (56, 56), (50, 66, 1), (44, 56),
                (36, 48), (28, 60, 1), (20, 54)]),
        strand([(30, 14), (26, 50)], 'shade', 'f', 1.0), strand([(70, 14), (74, 50)], 'shade', 'f', 1.0)],
    'side': [antenna((48, -4), (50, -14), (46, -22), 'mid', 3.2), L(ell(46, -22, 3, 2.4), 'mid', 'b', False)] + longhair('side', length=104, flare=2, top=-6)
            + [fringe([(62, 0), (86, 14), (94, 40), (92, 60, 1), (84, 48), (76, 40)])],
    'back': _sv_ant + longhair('back', length=104, flare=2, top=-6, ends=7),
}

# ------------------------------------------------------------------ Orphion Ordain (Tendou Nanase)
# Boina roja enorme de mariquita con lunares negros, que le cubre la cabeza; melena castaña corta por debajo con flequillo;
# ojos negros grandes y ovalados, dos lunares en la frente y sonrisa
_oo_spots_f = [L(ell(-2, 16, 6, 9), BLACK, 'f', False), L(ell(96, -8, 7, 6), BLACK, 'f', False), L(ell(40, -24, 5, 3), BLACK, 'f', False)]
CHARS['orphion-ordain'] = {
    'body': 'bajito', 'pal': pal('#6a4a30', '#fcd8b4', beret='#d8303a', beret_d='#a81e28', blush='#f0a0a8'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    'front': [L(outline([(10, 84), (6, 40), (20, 20), (80, 20), (94, 40), (90, 84), (80, 80), (80, 60), (20, 60), (20, 80)])),
              fringe([(14, 60), (16, 32), (30, 26), (50, 24), (70, 26), (84, 32), (86, 60), (76, 50), (66, 54, 1), (60, 40), (50, 50), (40, 40), (34, 54, 1),
                      (24, 50)]),
              L(outline([(-6, 30), (-4, 4), (10, -20), (40, -32), (70, -30), (96, -18), (106, 6), (104, 30), (90, 40), (50, 30), (10, 40)]), 'beret', 'f', ln=True),
              L(outline([(60, -28), (96, -16), (104, 28), (90, 38), (74, 34)]), 'beret_d', 'f', False)] + _oo_spots_f + [
              L(ell(34, 72, 5, 7.4), BLACK, 'f', False), L(ell(66, 72, 5, 7.4), BLACK, 'f', False),
              L(ell(32.4, 69, 1.6, 2.2), WHITE, 'f', False), L(ell(64.4, 69, 1.6, 2.2), WHITE, 'f', False),
              L(ell(42, 52, 2.2, 2.4), BLACK, 'f', False), L(ell(58, 52, 2.2, 2.4), BLACK, 'f', False)] + blush(80, 26, 3, 2),
    'side': [L(outline([(54, 62), (60, 50), (80, 50), (90, 40), (40, 30), (8, 40), (4, 66), (14, 86), (34, 84), (46, 74)])),
             L(outline([(-8, 50), (-12, 20), (4, -10), (36, -24), (70, -20), (94, -4), (100, 20), (92, 36), (60, 38), (20, 52)]), 'beret', 'f', ln=True),
             L(outline([(-10, 30), (-4, 46), (20, 52), (60, 38), (40, 34)]), 'beret_d', 'f', False),
             L(ell(30, 6, 10, 12), BLACK, 'f', False), L(ell(80, 74, 3, 6), BLACK, 'f', False), L(ell(80, 84, 3, 2), 'blush', 'f', False)],
    'back': [L(outline([(10, 82), (8, 50), (92, 50), (90, 82), (70, 90), (30, 90)])),
             L(outline([(-6, 50), (-6, 16), (10, -14), (50, -26), (90, -14), (106, 16), (106, 50), (90, 62), (50, 66), (10, 62)]), 'beret', 'f', ln=True),
             L(outline([(54, -24), (90, -12), (104, 20), (104, 50), (88, 60), (66, 60)]), 'beret_d', 'f', False),
             L(ell(50, -8, 9, 7), BLACK, 'f', False), L(ell(30, 52, 8, 6), BLACK, 'f', False), L(ell(104, 14, 3, 9), BLACK, 'f', False)],
}

# ------------------------------------------------------------------ Corwin Lumen (Tamamushi Mitsuki)
# Pelo verde revuelto con un mechón amarillo que le cruza el flequillo, dos antenas de pelo que se curvan hacia fuera y
# ojos naranjas en espiral; coloretes y sonrisa
_cl_eye = []
for _cx in (34, 66):
    _cl_eye += [L(ell(_cx, 74, 7.2, 7.6), WHITE, 'f', ln=True), L(ell(_cx, 74, 5.6, 6), 'ring', 'f', False),
                L(ell(_cx, 74, 3.6, 4) + [ell(_cx, 74, 3.6, 4)[0]], OUTC, 'f', False, False, 1.0), L(ell(_cx, 74, 1.4, 2.4), OUTC, 'f', False)]
_cl_ant = [antenna((22, 10), (4, 0), (-10, 12), 'mid', 3.6), antenna((78, 10), (96, 0), (110, 12), 'mid', 3.6)]
CHARS['corwin-lumen'] = {
    'body': 'bajito', 'pal': pal('#4e9a5a', '#fcd8b4', shade='#357a44', streak='#d8d070', ring='#e07a1e', blush='#f4a0a0'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': _cl_ant + [
        L(outline([(14, 104), (4, 70), (6, 30), (20, 6), (50, -4), (80, 6), (94, 30), (96, 70), (86, 104), (82, 96), (80, 64), (20, 64), (18, 96)])),
        L(outline([(60, 0), (84, 10), (96, 40), (92, 90), (82, 60)]), 'shade', 'b', False),
        fringe([(12, 64), (14, 32), (28, 12), (50, 6), (72, 12), (86, 32), (88, 64), (80, 56), (74, 64, 1), (68, 52), (60, 60, 1), (56, 50), (50, 62, 1),
                (44, 50), (38, 60, 1), (32, 50), (24, 62, 1), (18, 54)]),
        L(outline([(46, 2), (54, 0), (50, 34), (44, 60, 1), (42, 30)]), 'streak', 'f', ln=True)] + _cl_eye + blush(86, 24, 4.4, 2.6),
    'side': [antenna((24, 14), (8, 2), (-8, 12), 'mid', 3.6),
             L(outline([(54, 64), (58, 50), (80, 50), (94, 36), (90, 12), (68, -4), (40, -6), (14, 8), (2, 34), (0, 70), (8, 96), (20, 86), (26, 100, 1), (36, 84),
                        (46, 76)])),
             L(outline([(4, 40), (26, 46), (30, 84), (10, 82)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 16), (96, 42), (94, 66, 1), (86, 52), (80, 62, 1), (76, 42), (64, 30)]),
             L(ell(86, 76, 4, 6), WHITE, 'f', ln=True), L(ell(87, 76, 2.6, 4.4), 'ring', 'f', False), L(ell(87, 76, 1, 1.8), OUTC, 'f', False),
             L(ell(82, 86, 4, 2.4), 'blush', 'f', False)],
    'back': _cl_ant + [
        L(outline([(12, 98), (4, 64), (8, 30), (22, 6), (50, -4), (78, 6), (92, 30), (96, 64), (88, 98), (76, 92), (64, 102, 1), (50, 94), (36, 102, 1), (24, 92)])),
        L(outline([(56, 0), (82, 10), (96, 44), (90, 92), (66, 96)]), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Aurel Ashdown (Higurashi Yuuhi)
# Piel morena, pelo verde muy oscuro en casco redondeado que cae en puntas hasta la barbilla, una cinta blanca fina en la
# frente y un mechón de punta en lo alto; ojos cerrados de felicidad y coloretes
CHARS['aurel-ashdown'] = {
    'body': 'normal', 'pal': pal('#2e4a3a', '#a06a44', shade='#20382c', band='#ece2e2', blush='#e0a080'),
    'face': {'eyes': 'closed', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(48, -6), (52, -32, 1), (60, -8)])),
              L(outline([(12, 100), (2, 76, 1), (10, 64), (6, 30), (20, 4), (50, -8), (80, 4), (94, 30), (90, 64), (98, 76, 1), (88, 100), (82, 66), (18, 66)])),
              L(outline([(58, -4), (84, 8), (94, 40), (88, 90), (80, 56)]), 'shade', 'b', False),
              fringe([(12, 60), (14, 30), (30, 14), (50, 8), (70, 14), (86, 30), (88, 60), (80, 46), (70, 40), (50, 38), (30, 40), (20, 46)]),
              L(quad((10, 34), (50, 24), (90, 34)), 'band', 'f', False, False, 3.0)] + blush(84, 24, 5, 2.6),
    'side': [L(outline([(36, -4), (34, -34, 1), (48, -8)])),
             L(outline([(54, 62), (58, 48), (80, 46), (92, 32), (88, 8), (66, -8), (36, -8), (12, 6), (2, 34), (-2, 70), (2, 100, 1), (16, 84), (24, 98, 1),
                        (34, 82), (46, 74)])),
             L(outline([(2, 40), (24, 44), (28, 84), (8, 86)]), 'shade', 'b', False), L(quad((4, 30), (50, 22), (92, 30)), 'band', 'f', False, False, 3.0),
             L(ell(84, 84, 4, 2.6), 'blush', 'f', False)],
    'back': [L(outline([(48, -6), (52, -32, 1), (60, -8)])),
             L(outline([(12, 96), (2, 74, 1), (8, 60), (6, 30), (20, 4), (50, -8), (80, 4), (94, 30), (92, 60), (98, 74, 1), (88, 96), (72, 90), (64, 100, 1), (54, 90),
                        (46, 100, 1), (36, 90), (26, 98, 1)])),
             L(outline([(56, -4), (84, 8), (94, 44), (88, 92), (64, 92)]), 'shade', 'b', False), L(quad((6, 34), (50, 26), (94, 34)), 'band', 'f', False, False, 3.0)],
}

# ------------------------------------------------------------------ Aveline Morrin (Miyama Ageha)
# Melena negra larguísima y lisa con flequillo recto de raya en medio, mechones largos junto a la cara y dos mechones sueltos
# que se abren hacia fuera a la altura del pecho; ojos rosados grandes
CHARS['aveline-morrin'] = {
    'body': 'chica', 'pal': pal('#2a2a2e', '#fce4cc', iris='#d0607a', shade='#1c1c22'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(8, 120), (0, 60), (6, 20), (22, -4), (50, -10), (78, -4), (94, 20), (100, 60), (92, 120), (82, 120), (80, 64), (20, 64), (18, 120)])),
              L(outline([(4, 70), (-14, 92), (-16, 104, 1), (-4, 92), (8, 84)])), L(outline([(96, 70), (114, 92), (116, 104, 1), (104, 92), (92, 84)])),
              L(outline([(58, -6), (84, 2), (98, 40), (92, 116), (82, 116), (80, 50)]), 'shade', 'b', False),
              fringe([(12, 100), (12, 30), (24, 6), (48, 0), (50, 8), (52, 0), (76, 6), (88, 30), (88, 100), (80, 92), (80, 56), (70, 56), (64, 50), (50, 50),
                      (36, 50), (30, 56), (20, 56), (20, 92)])],
    'side': longhair('side', length=124, flare=4, top=-10) + [fringe([(60, -4), (86, 10), (94, 40), (92, 60), (84, 58), (82, 96), (76, 96), (76, 52), (68, 40)])],
    'back': longhair('back', length=124, flare=6, top=-10, ends=6) + [L(outline([(4, 70), (-14, 92), (-16, 104, 1), (-4, 92), (8, 84)]), 'mid', 'b'),
                                                                      L(outline([(96, 70), (114, 92), (116, 104, 1), (104, 92), (92, 84)]), 'mid', 'b')],
}

# ------------------------------------------------------------------ Corin Cainver (Kama Touya)
# Melena larga verde oliva con raya en medio y dos mechones peinados hacia atrás, que se abre por detrás en una capa de
# puntas hasta los hombros (por debajo, castaña); mirada chula y media sonrisa
CHARS['corin-cainver'] = {
    'body': 'normal', 'pal': pal('#9aa058', '#fcd0a8', iris='#1e1414', shade='#6a5a34'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(18, 60), (4, 80), (-22, 104, 1), (2, 98), (-14, 116, 1), (12, 106), (20, 90)]), 'shade', 'b'),
              L(outline([(82, 60), (96, 80), (122, 104, 1), (98, 98), (114, 116, 1), (88, 106), (80, 90)]), 'shade', 'b'),
              L(outline([(16, 90), (8, 40), (20, 8), (50, -2), (80, 8), (92, 40), (84, 90), (80, 60), (20, 60)])),
              fringe([(14, 70), (14, 34), (26, 12), (44, 4), (50, 10), (56, 4), (74, 12), (86, 34), (86, 70), (80, 58), (78, 34), (64, 20), (56, 30), (50, 20),
                      (44, 30), (36, 20), (22, 34), (20, 58)]),
              strand([(40, 10), (38, 40)], 'shade', 'f', 1.0), strand([(60, 10), (62, 40)], 'shade', 'f', 1.0)],
    'side': [L(outline([(54, 56), (62, 44), (82, 42), (92, 26), (86, -2), (96, -22, 1), (70, -14), (40, -4), (18, 12), (6, 40), (-16, 66), (-28, 80, 1), (-6, 80),
                        (-20, 98, 1), (6, 90), (24, 76), (40, 70)])),
             L(outline([(-6, 70), (14, 56), (30, 64), (12, 84)]), 'shade', 'b', False), fringe([(66, 2), (88, 14), (94, 36), (90, 50, 1), (82, 38)])],
    'back': [L(outline([(16, 10), (36, -2), (50, -4), (64, -2), (84, 10), (92, 50), (110, 82), (126, 104, 1), (100, 98), (110, 118, 1), (80, 108), (50, 120),
                        (20, 108), (-10, 118, 1), (0, 98), (-26, 104, 1), (-10, 82), (8, 50)])),
             L(outline([(14, 70), (50, 50), (86, 70), (100, 96), (60, 104), (40, 104), (0, 96)]), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Merrick Seawell (Hanmi Youta)
# Pelo gris beige recogido en un moño con forma de estrella de mar (cinco puntas que se abren por detrás y por arriba),
# mechones en punta a los lados de la cara y flequillo partido; ojos negros y sonrisa de pillo
_ms_star = [L(outline([(50, -22), (44, 4), (56, 4)])), L(outline([(14, 50), (-8, 44, 1), (16, 36)])), L(outline([(86, 50), (108, 44, 1), (84, 36)])),
            L(outline([(16, 92), (-6, 100, 1), (18, 82)])), L(outline([(84, 92), (106, 100, 1), (82, 82)]))]
CHARS['merrick-seawell'] = {
    'body': 'normal', 'pal': pal('#c8bca0', '#fcd0a8', iris='#1e1414', shade='#a89478'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': _ms_star + [
        L(outline([(16, 100), (6, 60), (10, 24), (24, 6), (50, 0), (76, 6), (90, 24), (94, 60), (84, 100), (80, 62), (20, 62)])),
        L(outline([(14, 18), (6, 6, 1), (24, 8)])), L(outline([(86, 18), (94, 6, 1), (76, 8)])),
        fringe([(14, 64), (14, 34), (28, 14), (48, 8), (50, 22), (52, 8), (72, 14), (86, 34), (86, 64), (78, 46), (64, 34), (54, 42), (50, 32), (46, 42), (36, 34),
                (22, 46)]),
        L(outline([(58, 10), (80, 18), (88, 40), (76, 36)]), 'shade', 'f', False)],
    'side': [L(outline([(30, 12), (24, -18, 1), (40, 4)])), L(outline([(18, 30), (-10, 22, 1), (10, 46)])), L(outline([(16, 60), (-14, 70, 1), (14, 72)])),
             L(outline([(54, 60), (58, 48), (80, 46), (92, 30), (86, 10), (66, -2), (40, 0), (18, 12), (8, 40), (6, 70), (12, 92), (28, 96), (40, 80)])),
             L(outline([(8, 40), (28, 46), (30, 80), (12, 80)]), 'shade', 'b', False), fringe([(64, 2), (88, 16), (94, 40), (90, 58, 1), (82, 44), (74, 34)])],
    'back': [L(outline([(16, 96), (8, 60), (12, 24), (26, 6), (50, 0), (74, 6), (88, 24), (92, 60), (84, 96), (50, 104)])),
             L(outline([(50, 34), (46, -20, 1), (54, 34)])), L(outline([(50, 34), (6, 20, 1), (50, 40)])), L(outline([(50, 34), (94, 20, 1), (50, 40)])),
             L(outline([(50, 36), (2, 52, 1), (48, 44)])), L(outline([(50, 36), (98, 52, 1), (52, 44)])),
             L(outline([(16, 92), (-6, 100, 1), (18, 82)])), L(outline([(84, 92), (106, 100, 1), (82, 82)])),
             L(outline([(56, 6), (86, 18), (92, 60), (84, 90), (62, 96)]), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Griffit Valiance (Ikkaku Ooji)
# Pelo castaño rojizo revuelto de pinchos con un mechón enorme en punta hacia arriba (el cuerno), mascarilla negra que le
# tapa media cara, cejas de punto y ojos verdes de sueño
CHARS['griffit-valiance'] = {
    'body': 'normal', 'pal': pal('#6a3e30', '#f6c8a0', iris='#5a8a4a', shade='#4e2c22', mask='#2c2c2e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'eye_y': 74, 'hairline': False},
    'front': [L(outline([(40, 0), (50, -40, 1), (58, -4)])),
              L(outline([(16, 76), (4, 70, 1), (10, 58), (-2, 40, 1), (10, 30), (4, 12, 1), (20, 12), (24, -4), (40, -8), (60, -6), (76, -14, 1), (78, 4), (98, 10, 1),
                         (88, 26), (100, 40, 1), (90, 50), (96, 66, 1), (84, 72), (82, 56), (18, 56)])),
              L(outline([(56, -6), (78, 4), (92, 40), (86, 64), (76, 40)]), 'shade', 'b', False),
              fringe([(14, 62), (16, 36), (28, 18), (50, 10), (72, 18), (84, 36), (86, 62), (78, 54), (72, 62, 1), (64, 46), (56, 58, 1), (50, 44), (42, 58, 1),
                      (34, 46), (28, 60, 1), (20, 52)]),
              L(ell(38, 58, 4, 2.4), 'shade', 'f', ln=True), L(ell(62, 58, 4, 2.4), 'shade', 'f', ln=True),
              L(outline([(18, 82), (50, 80), (82, 82), (78, 98), (60, 108), (50, 110, 1), (40, 108), (22, 98)]), 'mask', 'f', ln=True),
              L([(16, 82), (8, 74)], 'mask', 'f', False, False, 1.4), L([(84, 82), (92, 74)], 'mask', 'f', False, False, 1.4)],
    'side': [L(outline([(54, 58), (62, 46), (82, 46), (92, 30), (88, 10), (98, -6, 1), (78, -2), (80, -28, 1), (60, -12), (52, -36, 1), (40, -8), (14, -2, 1), (16, 14),
                        (-8, 22, 1), (6, 36), (-10, 52, 1), (8, 58), (2, 80, 1), (20, 74), (26, 92, 1), (38, 76), (48, 66)])),
             L(outline([(6, 34), (26, 40), (28, 70), (10, 64)]), 'shade', 'b', False),
             fringe([(66, 2), (88, 16), (94, 40), (90, 56, 1), (84, 42), (76, 32)]),
             L(outline([(70, 80), (96, 78), (98, 94), (84, 104), (70, 98)]), 'mask', 'f', ln=True), L([(70, 82), (48, 72)], 'mask', 'f', False, False, 1.4)],
    'back': [L(outline([(42, 0), (50, -40, 1), (60, -2)])),
             L(outline([(16, 86), (2, 80, 1), (8, 66), (-6, 50, 1), (8, 40), (0, 18, 1), (18, 16), (26, -6), (50, -10), (74, -6), (96, 14, 1), (90, 36), (106, 50, 1),
                        (92, 66), (98, 82, 1), (84, 86), (66, 98), (50, 94), (34, 98)])),
             L(outline([(56, -6), (80, 6), (94, 46), (86, 84), (64, 92)]), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Galad Worden (Gen Goroumaru)
# Melena castaña verdosa larga y ondulada hasta los hombros, con un flequillo largo que le tapa el ojo derecho; ojo verde
# de mirada tranquila y media sonrisa
CHARS['galad-worden'] = {
    'body': 'normal', 'pal': pal('#6a5a34', '#fcd8b4', iris='#6a8a4a', shade='#4e4226'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(8, 108), (-6, 90), (0, 50), (8, 16), (26, -6), (50, -12), (74, -6), (94, 16), (102, 50), (108, 90), (94, 108), (82, 100), (80, 60), (20, 60),
                         (18, 100)])),
              L(outline([(58, -8), (86, 6), (100, 50), (104, 96), (90, 104), (82, 60)]), 'shade', 'b', False),
              fringe([(12, 60), (12, 30), (26, 8), (50, 0), (72, 6), (88, 26), (92, 60), (94, 90), (82, 96), (80, 70), (66, 70), (56, 82, 1), (52, 66), (44, 52),
                      (36, 34), (28, 42), (20, 58)]),
              strand([(60, 10), (64, 50), (60, 76)], 'shade', 'f', 1.2), strand([(76, 20), (84, 60)], 'shade', 'f', 1.0)],
    'side': [L(outline([(54, 62), (60, 50), (80, 48), (94, 32), (90, 8), (68, -8), (36, -10), (10, 4), (-2, 40), (-6, 80), (0, 104), (20, 112), (40, 100), (46, 76)])),
             L(outline([(-2, 40), (22, 46), (34, 96), (6, 100)]), 'shade', 'b', False), strand([(10, 50), (16, 96)], 'deep', 'b', 1.0),
             fringe([(64, 0), (88, 14), (96, 40), (94, 66, 1), (86, 52), (78, 40)])],
    'back': [L(outline([(6, 104), (-6, 80), (0, 40), (12, 10), (30, -6), (50, -10), (70, -6), (88, 10), (100, 40), (106, 80), (96, 104), (70, 112), (50, 108), (30, 112)])),
             L(outline([(56, -6), (86, 8), (102, 50), (102, 98), (70, 108), (68, 50)]), 'shade', 'b', False),
             strand([(30, 20), (20, 70), (28, 104)], 'deep', 'b', 1.0), strand([(64, 20), (74, 70), (66, 104)], 'deep', 'b', 1.0)],
}

# ------------------------------------------------------------------ Alaric Durnham (Yasude Nagafumi)
# Melena granate enorme, revuelta y en capas de puntas que le abulta hasta la barbilla y por detrás; ojos blancos redondos
# como platos con la pupila pequeña, y boca pequeña enfadada
CHARS['alaric-durnham'] = {
    'body': 'bajito', 'pal': pal('#7a3a40', '#fcd8b4', shade='#5a2a30'),
    'face': {'eyes': 'none', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 104), (4, 96, 1), (8, 82), (-6, 74, 1), (4, 62), (-8, 50, 1), (4, 40), (0, 22), (12, 4), (28, -10), (50, -16), (66, -12), (74, -26, 1),
                         (78, -8), (90, 4), (100, 22), (98, 40), (108, 50, 1), (96, 62), (106, 74, 1), (92, 82), (96, 96, 1), (84, 104), (80, 64), (20, 64)])),
              L(outline([(58, -10), (86, 4), (100, 40), (92, 96), (82, 64)]), 'shade', 'b', False),
              fringe([(12, 68), (12, 36), (24, 14), (46, 4), (70, 8), (86, 26), (90, 64), (82, 56), (76, 66, 1), (70, 50), (62, 62, 1), (58, 46), (50, 60, 1),
                      (44, 44), (36, 58, 1), (30, 46), (22, 64, 1)]),
              strand([(30, 12), (24, 40)], 'shade', 'f', 1.0), strand([(56, 8), (66, 34)], 'shade', 'f', 1.0)] + white_eyes(76, 15, 7.4, 7, 2.2),
    'side': [L(outline([(54, 64), (60, 52), (80, 50), (94, 36), (96, 12), (82, -8), (56, -18), (28, -14), (6, 0), (-8, 24), (-12, 50), (-6, 76), (-14, 92, 1), (4, 92),
                        (2, 106, 1), (18, 98), (28, 110, 1), (36, 94), (46, 80)])),
             L(outline([(-8, 40), (16, 44), (26, 92), (2, 96)]), 'shade', 'b', False), strand([(4, 50), (10, 90)], 'deep', 'b', 1.0),
             fringe([(64, 0), (90, 14), (96, 42), (94, 68, 1), (86, 54), (80, 64, 1), (76, 44), (64, 32)])] + side_eye(76),
    'back': [L(outline([(10, 100), (-4, 92, 1), (2, 76), (-10, 62, 1), (0, 46), (-6, 28, 1), (8, 16), (20, 0), (40, -14), (60, -16), (80, -6), (96, 12), (106, 30, 1),
                        (100, 46), (110, 62, 1), (98, 76), (104, 92, 1), (90, 100), (76, 96), (66, 108, 1), (54, 96), (44, 108, 1), (34, 96), (22, 106, 1)])),
             L(outline([(58, -14), (86, 0), (102, 40), (96, 92), (66, 98)]), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Plumian Whitlock (Haneari Akiho)
# Pelo negro corto y redondeado como un casco con mechones en punta sobre la frente, atado en la nuca con una cinta negra
# de puntas sueltas; dos lunares en la frente, ojos negros y sonrisa
_pw_tie = [L(outline([(42, 94), (30, 108), (26, 104), (36, 92)]), 'mid', 'b', ln=True), L(outline([(58, 94), (70, 106), (74, 102), (64, 92)]), 'mid', 'b', ln=True)]
CHARS['plumian-whitlock'] = {
    'body': 'normal', 'pal': pal('#2a2a2e', '#fcd8b4', iris='#1e1414', shade='#1a1a1e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 74), (10, 40), (20, 12), (50, 0), (80, 12), (90, 40), (84, 74), (80, 60), (20, 60)])),
              L(outline([(58, 4), (82, 14), (90, 44), (84, 68), (78, 40)]), 'shade', 'b', False),
              fringe([(14, 62), (16, 34), (30, 16), (50, 10), (70, 16), (84, 34), (86, 62), (78, 50), (70, 44), (62, 56, 1), (56, 42), (46, 60, 1), (42, 42), (32, 54, 1),
                      (26, 44), (20, 56)]),
              L(ell(42, 60, 2.6, 2.2), BLACK, 'f', False), L(ell(56, 60, 2.6, 2.2), BLACK, 'f', False)],
    'side': [L(outline([(26, 92), (14, 104), (10, 98), (20, 86)]), 'mid', 'b', ln=True),
             L(outline([(54, 60), (60, 48), (80, 46), (90, 30), (84, 10), (62, -2), (34, 0), (12, 14), (4, 40), (6, 70), (14, 88), (30, 92), (42, 80), (50, 70)])),
             L(outline([(6, 40), (28, 44), (30, 80), (12, 80)]), 'shade', 'b', False), fringe([(64, 2), (88, 16), (94, 40), (90, 54, 1), (82, 42), (74, 34)])],
    'back': _pw_tie + [L(outline([(14, 84), (8, 44), (18, 14), (50, 0), (82, 14), (92, 44), (86, 84), (66, 94), (50, 96), (34, 94)])),
                       L(outline([(56, 4), (84, 16), (92, 50), (84, 80), (62, 90)]), 'shade', 'b', False),
                       strand([(50, 4), (50, 90)], 'deep', 'b', 1.0), L(ell(50, 92, 4, 3), 'mid', 'f', ln=True)],
}

# ------------------------------------------------------------------ Queintas Quillmere (Abu Bunsaku)
# Pelo castaño revuelto de puntas con dos mechones de punta en lo alto, una cinta ancha verde con hebilla gris alta en la
# frente, flequillo que le tapa el ojo izquierdo de la imagen y pecas; boca pequeña abierta
CHARS['queintas-quillmere'] = {
    'body': 'normal', 'pal': pal('#5a4030', '#fcd8b4', iris='#1e1414', shade='#3e2c20', band='#3a9a3a', band_d='#2a7a2a', buckle='#9a9aa0'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'line', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(36, -4), (30, -24, 1), (46, -10)])), L(outline([(56, -10), (66, -26, 1), (68, -4)])),
              L(outline([(16, 100), (4, 90, 1), (10, 76), (-2, 64, 1), (10, 54), (6, 24), (20, 2), (50, -8), (80, 2), (94, 24), (90, 54), (102, 64, 1), (90, 76),
                         (96, 90, 1), (84, 100), (80, 66), (20, 66)])),
              L(outline([(58, -4), (84, 8), (94, 40), (88, 90), (80, 56)]), 'shade', 'b', False),
              fringe([(12, 70), (14, 40), (30, 30), (50, 28), (70, 30), (86, 40), (88, 70), (80, 60), (72, 68, 1), (66, 56), (58, 62, 1), (54, 50), (46, 52), (40, 86, 1),
                      (34, 70), (26, 88, 1), (20, 66)]),
              L(outline([(8, 30), (8, 12), (50, 4), (92, 12), (92, 30), (50, 24)]), 'band', 'f', ln=True),
              L(outline([(56, 8), (92, 14), (92, 30), (60, 26)]), 'band_d', 'f', False),
              L(outline([(44, 4), (56, 4), (56, 25), (44, 25)]), 'buckle', 'f', ln=True)]
             + [L(ell(x, y, 0.9, 0.9), (120, 70, 50, 255), 'f', False) for x, y in ((26, 84), (30, 86), (28, 88), (70, 84), (74, 86), (72, 88))],
    'side': [L(outline([(40, -6), (36, -26, 1), (52, -8)])),
             L(outline([(54, 64), (58, 52), (80, 50), (94, 36), (90, 12), (70, -4), (42, -6), (16, 8), (4, 36), (-8, 50, 1), (4, 60), (-2, 86, 1), (14, 80), (14, 100, 1),
                        (28, 86), (40, 82), (48, 74)])),
             L(outline([(4, 40), (24, 46), (28, 80), (10, 78)]), 'shade', 'b', False),
             L(outline([(6, 30), (8, 10), (60, 2), (94, 12), (94, 32), (60, 24)]), 'band', 'f', ln=True), L(outline([(70, 8), (80, 8), (82, 28), (70, 26)]), 'buckle', 'f', ln=True),
             fringe([(66, 30), (90, 34), (96, 46), (94, 66, 1), (86, 52), (80, 62, 1), (76, 46)])],
    'back': [L(outline([(36, -4), (30, -24, 1), (46, -10)])), L(outline([(56, -10), (66, -26, 1), (68, -4)])),
             L(outline([(14, 94), (2, 86, 1), (8, 70), (-6, 56, 1), (8, 48), (6, 24), (20, 2), (50, -8), (80, 2), (94, 24), (92, 48), (106, 56, 1), (92, 70), (98, 86, 1),
                        (86, 94), (70, 100, 1), (60, 92), (50, 102, 1), (40, 92), (30, 100, 1)])),
             L(outline([(56, -4), (84, 8), (94, 44), (88, 90), (64, 94)]), 'shade', 'b', False),
             L(outline([(6, 32), (8, 14), (50, 8), (92, 14), (94, 32), (50, 28)]), 'buckle', 'f', ln=True)],
}

# ------------------------------------------------------------------ Tarvon Runnel (Mimizuki Kojirou)
# Pelo blanco en mechones largos y lisos como fideos que le caen por la cara y los lados hasta la barbilla (sombra rosada por
# detrás); dos marcas negras en forma de gota bajo los ojos grises
CHARS['tarvon-runnel'] = {
    'body': 'normal', 'pal': pal('#f0ece6', '#fcd8b4', iris='#7a7a7a', shade='#c8aaa8', deep='#9a8484'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'line', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(14, 98), (4, 60), (-6, 54, 1), (6, 40), (10, 14), (28, -4), (50, -8), (72, -4), (90, 14), (94, 40), (106, 54, 1), (96, 60), (86, 98),
                         (80, 64), (20, 64)])),
              L(outline([(58, -4), (84, 8), (94, 44), (88, 90), (80, 56)]), 'shade', 'b', False),
              fringe([(12, 72), (14, 34), (28, 12), (50, 4), (72, 12), (86, 34), (88, 72), (82, 64), (80, 92, 1), (76, 60), (70, 50), (64, 70, 1), (58, 50), (52, 84, 1),
                      (48, 54), (42, 46), (36, 70, 1), (30, 50), (24, 92, 1), (20, 64)]),
              strand([(30, 14), (26, 50)], 'shade', 'f', 1.0), strand([(70, 14), (74, 50)], 'shade', 'f', 1.0),
              L(outline([(34, 84), (36, 90), (34, 94), (32, 90)]), BLACK, 'f', False), L(outline([(66, 84), (68, 90), (66, 94), (64, 90)]), BLACK, 'f', False)],
    'side': [L(outline([(54, 62), (60, 50), (82, 48), (94, 32), (88, 8), (66, -6), (38, -8), (14, 6), (2, 34), (0, 70), (4, 96, 1), (14, 80), (18, 100, 1), (26, 82),
                        (34, 96, 1), (40, 78), (48, 72)])),
             L(outline([(2, 34), (30, 40), (40, 80), (10, 86)]), 'shade', 'b', False),
             fringe([(64, 2), (88, 16), (96, 40), (96, 76, 1), (88, 56), (82, 70, 1), (78, 44), (66, 30)]),
             L(outline([(82, 86), (84, 92), (82, 96), (80, 92)]), BLACK, 'f', False)],
    'back': [L(outline([(12, 98), (2, 60), (-6, 54, 1), (6, 40), (10, 14), (28, -4), (50, -8), (72, -4), (90, 14), (94, 40), (106, 54, 1), (98, 60), (88, 98), (76, 92),
                        (68, 104, 1), (58, 92), (50, 100, 1), (42, 92), (32, 104, 1), (24, 92)])),
             L(outline([(54, -4), (84, 8), (96, 44), (90, 92), (60, 96), (64, 40)]), 'shade', 'b', False),
             strand([(30, 10), (22, 60), (28, 96)], 'deep', 'b', 1.0), strand([(64, 10), (70, 60), (64, 96)], 'deep', 'b', 1.0)],
}
