"""Big Bang (gx-big-bang): equipo de elfos de Galaxy (la ruta de la versión Big Bang). Referencias: sus modelos 3D de Inazuma
Eleven GO Galaxy en la enciclopedia (cada jugador tiene uno solo; todos llevan las orejas largas de elfo hacia los lados)."""
from chars import CHARS, L, OUTC, ell, mirror, outline, pal, rope, strand  # noqa: F401
from chars_bigwaves import white_eyes
from heads import quad

WHITE = (248, 248, 248, 255)


def elf(view, length=40, up=8, lo=82, z=None):
    """Orejas largas de elfo hacia los lados (frente y espalda) o hacia atrás (perfil), un poco hacia arriba."""
    tip = 19 - length
    if view == 'side':
        ear = [(54, 64), (54 - length * 0.8, 60 - up, 1), (52, lo)]
        inner = [(51, 68), (54 - length * 0.8 + 8, 63 - up, 1), (50, lo - 5)]
        return [L(outline(ear, 4), 'skin', z or 'f', ln=True), L(outline(inner, 4), 'skin_d', z or 'f', False)]
    ear = [(20, 62), (tip, 62 - up, 1), (20, lo)]
    inner = [(18, 66), (tip + 9, 64 - up, 1), (18, lo - 5)]
    out = [L(outline(ear, 4), 'skin', z or 'b', ln=True), L(outline(inner, 4), 'skin_d', z or 'b', False)]
    out += [L(mirror(outline(ear, 4)), 'skin', z or 'b', ln=True), L(mirror(outline(inner, 4)), 'skin_d', z or 'b', False)]
    return out


def ball(x, y, r=6, c='mid'):
    return L(ell(x, y, r, r * 0.92), c, 'f', ln=True)


NOEARS = {'ears': False}

# Strem Gooser (portero): rechoncho; pelo malva en casco con raya, un moño redondo arriba atado con un cordón rojo y dos
# mechones a los lados de la cara que acaban en bolitas a la altura de la barbilla; ojos azules achinados y sonrisa con
# colmillos
CHARS['strem-goozer'] = {
    'body': 'corpulento', 'pal': pal('#c48ca2', '#fae2c4', iris='#6a7aa8', cord='#c02a24'),
    'face': {**NOEARS, 'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 94, 'hairline': (64, 54)},
    'front': elf('front', 36, 6)
             + [L(ell(50, -20, 10, 9)), L(outline([(45, -12), (55, -12), (56, 8), (44, 8)]), 'cord', 'b', ln=True),
                strand([(45, -4), (55, -4)], OUTC, 'b', 0.8), strand([(45, 2), (55, 2)], OUTC, 'b', 0.8),
                L(outline([(12, 74), (10, 38), (24, 12), (50, 2), (76, 12), (90, 38), (88, 74), (80, 62), (66, 56), (56, 60), (50, 54), (44, 60), (34, 56), (20, 62)])),
                L(outline([(58, 8), (80, 18), (88, 40), (84, 60), (74, 42)]), 'shade', 'b', False),
                strand([(50, 6), (50, 38)], 'deep', 'b', 1.0),
                L(outline([(14, 56), (22, 60), (26, 90), (22, 100), (16, 96)]), 'mid', 'f', ln=True),
                L(outline([(86, 56), (78, 60), (74, 90), (78, 100), (84, 96)]), 'mid', 'f', ln=True),
                ball(20, 104, 6), ball(80, 104, 6)],
    'side': [L(ell(44, -20, 10, 9)), L(outline([(39, -12), (49, -12), (50, 6), (38, 6)]), 'cord', 'b', ln=True),
             L(outline([(54, 58), (60, 44), (80, 40), (90, 26), (80, 8), (54, -2), (28, 4), (12, 22), (6, 50), (10, 76), (24, 88), (40, 84), (48, 70)])),
             L(outline([(10, 40), (30, 44), (34, 80), (14, 74)]), 'shade', 'b', False),
             L(outline([(62, 50), (72, 56), (76, 88), (70, 100), (64, 90)]), 'mid', 'f', ln=True), ball(70, 104, 6)]
            + elf('side', 34, 6),
    'back': elf('back' if False else 'front', 36, 6)
            + [L(ell(50, -20, 10, 9)), L(outline([(45, -12), (55, -12), (56, 8), (44, 8)]), 'cord', 'b', ln=True),
               L(outline([(14, 76), (12, 38), (24, 14), (50, 4), (76, 14), (88, 38), (86, 76), (66, 88), (34, 88)])),
               L(outline([(56, 8), (80, 18), (88, 44), (84, 74), (62, 86)]), 'shade', 'b', False),
               ball(22, 98, 6), ball(78, 98, 6)],
}

# Fou Tudus: pelo celeste peinado hacia atrás con la frente despejada y un pico en medio; encima, una diadema de dos arcos
# grises que salen de una pinza negra en lo alto y acaban en tres bolas grises por lado; ojos verdes y boca abierta
_fou_arc = [L(rope((46, 2), (14, -4), (-14, 30), 7), 'band'), L(rope((54, 2), (86, -4), (114, 30), 7), 'band'),
            ball(-16, 36, 10, 'band'), ball(2, 14, 10, 'band'), ball(24, 2, 9, 'band'),
            ball(116, 36, 10, 'band'), ball(98, 14, 10, 'band'), ball(76, 2, 9, 'band'),
            L(outline([(44, -10), (56, -10), (56, 2), (44, 2)]), OUTC, 'f', False)]
CHARS['fow-tudas'] = {
    'body': 'normal', 'pal': pal('#a8dcdc', '#fce4c4', iris='#3aa84a', band='#8a8488', band_d='#6a6468'),
    'face': {**NOEARS, 'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 94,
             'hairline': [(14, 66), (20, 50), (34, 44), (46, 50), (50, 58), (54, 50), (66, 44), (80, 50), (86, 66)]},
    'front': elf('front', 42, 8)
             + [L(outline([(16, 66), (14, 38), (26, 16), (50, 8), (74, 16), (86, 38), (84, 66), (76, 50), (62, 44), (54, 50), (50, 60, 1), (46, 50), (38, 44), (24, 50)])),
                L(outline([(58, 12), (80, 22), (86, 44), (82, 60), (74, 44)]), 'shade', 'b', False),
                strand([(34, 20), (30, 40)], 'shade', 'b', 1.0), strand([(66, 20), (70, 40)], 'shade', 'b', 1.0)]
             + _fou_arc,
    'side': [L(outline([(56, 58), (62, 46), (80, 44), (92, 30), (86, 12), (62, 0), (34, 2), (14, 16), (6, 40), (8, 66), (22, 82), (38, 80), (48, 70)]), 'band'),
             L(outline([(62, 4), (86, 14), (92, 32), (78, 34), (60, 22), (40, 18), (26, 26)]), 'mid', 'b'),
             L(rope((52, 0), (20, -12), (-18, 16), 7), 'band'), ball(-22, 20, 9, 'band'), ball(-2, -2, 9, 'band'), ball(20, -10, 8, 'band'),
             L(outline([(46, -8), (56, -8), (56, 4), (46, 4)]), OUTC, 'f', False)]
            + elf('side', 38, 8),
    'back': elf('front', 42, 8)
            + [L(outline([(16, 76), (14, 38), (26, 16), (50, 8), (74, 16), (86, 38), (84, 76), (66, 88), (34, 88)]), 'band'),
               L(outline([(30, 12), (50, 8), (70, 12), (64, 40), (50, 48), (36, 40)]), 'mid', 'b', False),
               L(outline([(58, 12), (80, 22), (86, 50), (82, 74), (62, 86)]), 'band_d', 'b', False)]
            + _fou_arc,
}

# Cherio Pardon: pelo verde oliva en casco con raya en medio y dos cortinas que bajan hasta la mandíbula; por detrás le
# caen cinco mechones finos que acaban en bolitas sobre los hombros; ojos achinados y cejas fruncidas
CHARS['cherio-pardon'] = {
    'body': 'delgado', 'pal': pal('#a8b07a', '#fce2c4', iris='#2a2420', shade='#86845a'),
    'face': {**NOEARS, 'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 94, 'hairline': False},
    'front': elf('front', 44, 6)
             + [L(outline([(14, 84), (12, 40), (24, 14), (50, 4), (76, 14), (88, 40), (86, 84), (80, 66), (64, 54), (54, 46), (50, 38, 1), (46, 46), (36, 54), (20, 66)])),
                L(outline([(56, 10), (78, 20), (88, 44), (86, 78), (78, 56), (60, 44)]), 'shade', 'b', False),
                L(outline([(14, 62), (22, 66), (24, 100), (18, 104)]), 'mid', 'f', ln=True), L(outline([(86, 62), (78, 66), (76, 100), (82, 104)]), 'mid', 'f', ln=True),
                ball(20, 110, 5), ball(80, 110, 5)],
    'side': [L(outline([(54, 62), (58, 48), (80, 46), (92, 30), (84, 10), (60, -2), (32, 2), (12, 18), (4, 44), (6, 72), (18, 88), (36, 86), (46, 74)])),
             L(outline([(6, 38), (30, 42), (34, 82), (12, 80)]), 'shade', 'b', False),
             L(rope((20, 84), (12, 96), (4, 108), 4)), ball(2, 112, 5), L(rope((34, 86), (30, 98), (24, 110), 4)), ball(22, 114, 5),
             L(outline([(62, 4), (86, 16), (92, 36), (90, 54, 1), (82, 42), (72, 34)]), 'mid', 'f')]
            + elf('side', 40, 6),
    'back': elf('front', 44, 6)
            + [L(outline([(14, 84), (12, 40), (24, 14), (50, 4), (76, 14), (88, 40), (86, 84), (64, 92), (36, 92)])),
               L(outline([(56, 8), (80, 20), (88, 48), (86, 82), (60, 92)]), 'shade', 'b', False)]
            + [L(rope((x, 86), (x + (x - 50) * 0.1, 98), (x + (x - 50) * 0.2, 108), 4)) for x in (22, 36, 50, 64, 78)]
            + [ball(x + (x - 50) * 0.2, 112, 5) for x in (22, 36, 50, 64, 78)],
}

# Bambaros Tower: melena lila grisácea salvaje, de pinchos gruesos (dos como orejas de lobo arriba) y patillas espesas
# que le tapan las mejillas; un tatuaje azul en zigzag sobre cada ojo y la boca cosida con una cruz; orejas pequeñas
CHARS['bambaros-tower'] = {
    'body': 'normal', 'pal': pal('#9a96ba', '#e8c8a8', iris='#1e1e24', shade='#76708e', tat='#3a5ab0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'hairline': False, 'ear_out': 2},
    'front': [L(outline([(12, 94), (4, 76), (-4, 60, 1), (6, 54), (2, 34), (-2, 2, 1), (20, 16), (36, 10), (44, 2, 1), (54, 10), (64, 4, 1), (72, 12), (102, 2, 1),
                         (98, 34), (94, 54), (104, 60, 1), (96, 76), (90, 94), (82, 68), (66, 56), (50, 52), (34, 56), (18, 68)])),
              L(outline([(58, 8), (80, 14), (92, 46), (88, 86), (80, 60)]), 'shade', 'b', False),
              L(outline([(14, 60), (24, 64), (26, 86), (30, 98, 1), (18, 92)]), 'mid', 'f', ln=True),
              L(outline([(86, 60), (76, 64), (74, 86), (70, 98, 1), (82, 92)]), 'mid', 'f', ln=True),
              L(outline([(16, 52), (24, 40), (36, 34), (50, 38), (64, 34), (76, 40), (84, 52), (72, 50), (64, 58, 1), (58, 48), (50, 54, 1), (42, 48), (36, 58, 1), (28, 50)]), 'mid', 'f'),
              L([(30, 62), (36, 66), (32, 68), (40, 70)], 'tat', 'f', False, False, 1.8), L([(70, 62), (64, 66), (68, 68), (60, 70)], 'tat', 'f', False, False, 1.8),
              L([(45, 89), (55, 97)], OUTC, 'f', False, False, 1.6), L([(55, 89), (45, 97)], OUTC, 'f', False, False, 1.6),
              L([(42, 93), (58, 93)], OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(54, 62), (60, 48), (80, 46), (90, 32), (82, 16), (86, -6, 1), (66, 4), (56, -18, 1), (44, 2), (22, -4, 1), (22, 14), (2, 16, 1), (10, 30),
                        (-12, 40, 1), (6, 48), (-8, 64, 1), (8, 70), (2, 90, 1), (18, 86), (24, 100, 1), (36, 86), (46, 76)])),
             L(outline([(4, 40), (26, 46), (28, 84), (8, 78)]), 'shade', 'b', False),
             L(outline([(58, 58), (70, 60), (70, 86), (64, 96, 1), (58, 84)]), 'mid', 'f', ln=True),
             L([(82, 64), (88, 68), (84, 70)], 'tat', 'f', False, False, 1.8), L([(80, 90), (88, 96)], OUTC, 'f', False, False, 1.4)],
    'back': [L(outline([(12, 96), (-2, 84, 1), (4, 64), (-10, 50, 1), (6, 42), (-4, 18, 1), (14, 24), (16, 0, 1), (32, 12), (44, -6, 1), (54, 10), (68, -2, 1), (74, 14),
                        (94, 6, 1), (88, 28), (108, 36, 1), (94, 52), (106, 70, 1), (96, 84), (100, 98, 1), (82, 96), (70, 104, 1), (60, 96), (50, 106, 1), (40, 96),
                        (28, 104, 1)])),
             L(outline([(56, 6), (82, 14), (94, 48), (90, 92), (64, 98)]), 'shade', 'b', False)],
}

# Zahtan Worlder: melena larga ondulada castaño grisácea hasta los hombros (y por detrás hasta media espalda), con raya y
# mechones sobre la frente; ojos blancos enormes de pupila pequeña, sonrisa ancha y dos rayas negras bajo los ojos
CHARS['zartan-walder'] = {
    'body': 'delgado', 'pal': pal('#7c6c60', '#fce4c8', shade='#5e5048', light='#9a9a88'),
    'face': {**NOEARS, 'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': elf('front', 30, 6)
             + [L(outline([(18, 112), (-2, 118, 1), (2, 106), (-18, 110, 1), (-8, 96), (-20, 88, 1), (-4, 78), (0, 52), (4, 28), (18, 6), (50, -4), (82, 6), (96, 28),
                           (100, 52), (104, 78), (120, 88, 1), (108, 96), (118, 110, 1), (98, 106), (102, 118, 1), (82, 112), (82, 70), (18, 70)])),
                L(outline([(58, 4), (84, 14), (98, 44), (98, 104), (84, 114), (82, 60)]), 'shade', 'b', False),
                L(outline([(12, 84), (8, 46), (22, 20), (44, 10), (50, 20), (56, 10), (78, 20), (92, 46), (88, 84), (82, 62), (72, 48), (60, 40), (52, 28), (50, 24),
                           (48, 28), (40, 40), (28, 48), (18, 62)]), 'mid', 'f'),
                L(outline([(60, 18), (78, 28), (86, 48), (74, 44)]), 'shade', 'f', False), L(outline([(26, 24), (40, 18), (34, 30)]), 'light', 'f', False)]
             + white_eyes(76, 14, 7, 5.6, 1.8)
             + [L([(30, 84), (34, 96)], OUTC, 'f', False, False, 1.8), L([(70, 84), (66, 96)], OUTC, 'f', False, False, 1.8),
                L(quad((36, 92), (50, 100), (64, 92)), OUTC, 'f', False, False, 1.6)],
    'side': [L(outline([(52, 66), (56, 54), (80, 50), (94, 36), (90, 14), (98, 0, 1), (70, 0), (40, -6), (14, 6), (0, 30), (-12, 60), (-24, 100), (-34, 126, 1), (-10, 116),
                        (-2, 130, 1), (12, 110), (26, 104), (40, 96), (46, 82)])),
             L(outline([(0, 40), (24, 48), (30, 96), (4, 104), (-16, 108)]), 'shade', 'b', False),
             L(outline([(64, 4), (90, 18), (96, 42), (94, 70, 1), (86, 54), (80, 66, 1), (76, 44), (64, 30)]), 'mid', 'f'),
             L(ell(84, 76, 4, 5), WHITE, 'f', ln=True), L(ell(85, 76.5, 1.4, 1.6), OUTC, 'f', False)]
            + elf('side', 28, 6),
    'back': elf('front', 30, 6)
            + [L(outline([(10, 120), (-8, 116, 1), (-2, 92), (-8, 60), (2, 30), (18, 8), (50, -2), (82, 8), (98, 30), (108, 60), (102, 92), (108, 116, 1), (90, 120),
                          (76, 132, 1), (62, 120), (50, 134, 1), (38, 120), (24, 132, 1)])),
               L(outline([(56, 2), (84, 12), (100, 46), (102, 112), (70, 122), (72, 50)]), 'shade', 'b', False),
               L(outline([(28, 30), (40, 60), (32, 90), (24, 60)]), 'light', 'b', False), strand([(50, 4), (50, 120)], 'deep', 'b', 1.0)],
}

# Zain Hanging: pelo gris azulado peinado hacia atrás con trenzas alrededor de la cabeza; un mechón con anillas metálicas le
# baja desde la frente por encima de la nariz hasta la barbilla y le cuelgan dos bolas a cada lado junto a las orejas
_zain_rings = [L(outline([(45, y), (55, y), (55, y + 4), (45, y + 4)]), 'ring', 'f', ln=True) for y in (62, 70, 78, 86, 94)]
CHARS['zyne-hanging'] = {
    'body': 'normal', 'pal': pal('#9cb0c0', '#f2cfa6', iris='#1e1e24', shade='#7a8ea0', ring='#d8ccc0', deep='#5a6a7c'),
    'face': {**NOEARS, 'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': (58, 36)},
    'front': elf('front', 42, 10)
             + [L(outline([(16, 64), (14, 34), (26, 12), (50, 4), (74, 12), (86, 34), (84, 64), (76, 48), (60, 38), (50, 36), (40, 38), (24, 48)])),
                L(outline([(58, 8), (80, 18), (86, 40), (82, 58), (74, 42)]), 'shade', 'b', False),
                L(quad((16, 40), (50, 16), (84, 40)), 'deep', 'b', False, False, 2.4), L(quad((18, 48), (50, 26), (82, 48)), 'deep', 'b', False, False, 1.4),
                L(outline([(44, 36), (56, 36), (56, 104), (50, 110, 1), (44, 104)]), 'mid', 'f', ln=True)] + _zain_rings
             + [L(rope((16, 52), (12, 70), (14, 86), 5)), ball(12, 90, 6), ball(22, 100, 6), L(rope((84, 52), (88, 70), (86, 86), 5)), ball(88, 90, 6), ball(78, 100, 6)],
    'side': [L(outline([(56, 56), (62, 44), (80, 40), (90, 26), (82, 8), (58, -2), (30, 2), (12, 18), (6, 44), (10, 70), (24, 82), (40, 80), (48, 70)])),
             L(outline([(8, 40), (30, 44), (32, 76), (14, 72)]), 'shade', 'b', False),
             L(quad((86, 24), (50, 6), (14, 30)), 'deep', 'b', False, False, 2.4),
             L(rope((22, 72), (16, 86), (14, 96), 5)), ball(12, 100, 6), ball(28, 102, 6)]
            + elf('side', 38, 10),
    'back': elf('front', 42, 10)
            + [L(outline([(14, 78), (12, 36), (24, 12), (50, 4), (76, 12), (88, 36), (86, 78), (64, 88), (36, 88)])),
               L(outline([(56, 8), (80, 18), (88, 46), (84, 76), (62, 86)]), 'shade', 'b', False),
               L(quad((12, 36), (50, 20), (88, 36)), 'deep', 'b', False, False, 2.4), L(outline([(46, 24), (54, 24), (54, 44), (46, 44)]), 'ring', 'b', ln=True),
               ball(50, 50, 7), ball(18, 96, 6), ball(34, 102, 6), ball(66, 102, 6), ball(82, 96, 6)],
}

# Madison Ballada: cresta de pelo verde menta muy alta, de puntas hacia arriba y atrás, sobre una melena lisa verde oliva
# oscuro que le cae por los lados y la espalda; diadema dorada fina con una joya roja en la frente; sonrisa enorme
_mad_crest_f = [(22, 40), (24, 18), (30, 2), (24, -16, 1), (40, -2), (44, -28, 1), (54, -4), (66, -22, 1), (66, 0), (78, 10), (82, 36), (66, 30), (50, 32), (34, 30)]
CHARS['madison-barada'] = {
    'body': 'normal', 'pal': pal('#8edcbc', '#fce2c4', iris='#2a8a7a', shade='#5ea88a', long='#7c7a62', long_d='#5c5a46', gold='#d8a840', gem='#c02a2a'),
    'face': {**NOEARS, 'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 94, 'hairline': False},
    'front': elf('front', 40, 6)
             + [L(outline([(18, 108), (10, 90), (8, 50), (14, 36), (86, 36), (92, 50), (90, 90), (82, 108), (80, 66), (20, 66)]), 'long'),
                L(outline([(14, 52), (16, 40), (84, 40), (86, 52), (70, 46), (50, 44), (30, 46)]), 'long'),
                L(outline(_mad_crest_f)), L(outline([(54, -4), (66, -22), (66, 0), (78, 10), (82, 36), (66, 30)]), 'shade', 'b', False),
                L(quad((14, 46), (50, 34), (86, 46)), 'gold', 'f', False, False, 2.2), L(ell(50, 37, 3, 3), 'gem', 'f', ln=True)],
    'side': [L(outline([(54, 62), (58, 48), (80, 46), (92, 32), (86, 14), (64, 4), (40, 4), (18, 14), (4, 40), (-10, 80), (-20, 118), (-8, 122, 1), (10, 104), (30, 92),
                        (46, 76)]), 'long'),
             L(outline([(20, 26), (16, 6), (2, -10, 1), (24, -2), (32, -20, 1), (42, -4), (58, -16, 1), (60, 4), (82, 12), (90, 30), (60, 26), (40, 30)])),
             L(quad((88, 40), (50, 28), (16, 40)), 'gold', 'f', False, False, 2.2)]
            + elf('side', 36, 6),
    'back': elf('front', 40, 6)
            + [L(outline([(10, 110), (4, 60), (12, 26), (50, 12), (88, 26), (96, 60), (90, 110), (70, 124, 1), (50, 116), (30, 124, 1)]), 'long'),
               L(outline([(56, 14), (88, 28), (96, 64), (90, 108), (66, 118)]), 'long_d', 'b', False),
               L(outline([(26, 34), (28, 10), (40, -8, 1), (46, 6), (54, -14, 1), (58, 6), (68, -6, 1), (72, 14), (76, 34), (50, 44)])),
               L(quad((10, 40), (50, 28), (90, 40)), 'gold', 'f', False, False, 2.2)],
}

# Bind Hermit: melena rosa pálido lisa y larga que le cubre toda la cabeza como un velo y cae por delante de los hombros;
# lleva los ojos tapados con una venda negra ancha
CHARS['bindal-hermit'] = {
    'body': 'normal', 'pal': pal('#e4bcc4', '#f8dcc4', shade='#c4949e', mask='#3a3a42', mask_d='#26262c'),
    'face': {**NOEARS, 'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 96, 'hairline': False},
    'front': elf('front', 40, 6)
             + [L(outline([(16, 128), (6, 100), (4, 44), (14, 14), (50, 0), (86, 14), (96, 44), (94, 100), (84, 128), (80, 72), (20, 72)])),
                L(outline([(58, 4), (84, 16), (96, 48), (94, 110), (84, 122), (82, 66)]), 'shade', 'b', False),
                L(outline([(16, 76), (14, 40), (26, 18), (50, 10), (74, 18), (86, 40), (84, 76), (78, 62), (22, 62)]), 'mid', 'f'),
                strand([(50, 12), (50, 60)], 'shade', 'f', 1.2),
                L(outline([(16, 62), (84, 62), (86, 84), (50, 86), (14, 84)]), 'mask', 'f', ln=True),
                L(outline([(56, 64), (84, 64), (85, 82), (60, 84)]), 'mask_d', 'f', False)],
    'side': [L(outline([(54, 66), (58, 52), (80, 48), (92, 34), (86, 12), (62, -2), (34, 0), (12, 14), (2, 40), (-4, 80), (-10, 120), (4, 128, 1), (18, 108), (34, 96), (46, 80)])),
             L(outline([(2, 40), (26, 46), (30, 96), (0, 110)]), 'shade', 'b', False),
             L(outline([(70, 60), (92, 60), (94, 82), (72, 84)]), 'mask', 'f', ln=True),
             L(outline([(66, 4), (90, 18), (96, 42), (94, 62), (86, 60), (80, 40), (68, 30)]), 'mid', 'f')]
            + elf('side', 36, 6),
    'back': elf('front', 40, 6)
            + [L(outline([(12, 126), (4, 90), (4, 44), (14, 14), (50, 0), (86, 14), (96, 44), (96, 90), (88, 126), (50, 132)])),
               L(outline([(56, 4), (84, 16), (96, 50), (96, 120), (66, 128), (70, 50)]), 'shade', 'b', False),
               L(outline([(28, 30), (40, 70), (34, 116), (24, 80)]), 'light', 'b', False)],
}

# Astra Justin: pelo amarillo pálido de pinchos largos hacia arriba y a los lados (más tostado por detrás), con un mechón
# en pico sobre la frente; ojos grandes enfadados y boca apretada
CHARS['astro-justin'] = {
    'body': 'normal', 'pal': pal('#f2eab4', '#fce4c4', iris='#1e1e24', shade='#c8a884', deep='#a88866'),
    'face': {**NOEARS, 'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': elf('front', 30, 6)
             + [L(outline([(14, 70), (8, 52), (-6, 40, 1), (8, 32), (2, 6, 1), (20, 16), (22, -16, 1), (36, 2), (46, -26, 1), (56, -2), (70, -18, 1), (72, 6), (92, 0, 1),
                           (86, 24), (104, 30, 1), (90, 44), (86, 70), (80, 56), (20, 56)])),
                L(outline([(58, -2), (72, -14), (72, 6), (90, 2), (86, 26), (92, 48), (80, 40)]), 'shade', 'b', False),
                L(outline([(14, 62), (16, 42), (30, 28), (50, 22), (70, 28), (84, 42), (86, 62), (78, 52), (70, 60, 1), (62, 46), (54, 54), (48, 66, 1), (42, 50), (32, 58, 1), (24, 48)]), 'mid', 'f'),
                L(outline([(38, 4), (46, -20), (50, 4), (44, 20)]), 'light', 'b', False)],
    'side': [L(outline([(54, 58), (60, 46), (78, 44), (90, 30), (98, 10, 1), (78, 10), (74, -14, 1), (58, 0), (44, -24, 1), (32, 2), (8, -14, 1), (12, 14), (-14, 22, 1), (4, 36),
                        (-12, 54, 1), (8, 58), (4, 78, 1), (20, 72), (28, 86, 1), (38, 72), (46, 66)]), 'shade'),
             L(outline([(58, 0), (74, -14), (78, 10), (98, 10), (90, 30), (78, 44), (66, 30)]), 'mid', 'b', False),
             L(outline([(66, 4), (90, 18), (94, 40), (90, 56, 1), (84, 42), (74, 32)]), 'mid', 'f')]
            + elf('side', 28, 6),
    'back': elf('front', 30, 6)
            + [L(outline([(14, 82), (2, 72, 1), (8, 56), (-8, 42, 1), (8, 32), (2, 6, 1), (20, 16), (22, -16, 1), (36, 2), (46, -26, 1), (56, -2), (70, -18, 1), (72, 6),
                          (92, 0, 1), (86, 24), (106, 34, 1), (92, 48), (100, 70, 1), (86, 82), (66, 92, 1), (56, 82), (44, 92, 1), (34, 82)]), 'shade'),
               L(outline([(36, 2), (46, -26), (56, -2), (50, 20)]), 'light', 'b', False),
               strand([(30, 20), (40, 50), (36, 76)], 'deep', 'b', 1.0), strand([(70, 20), (60, 50), (64, 76)], 'deep', 'b', 1.0)],
}

# Joss Fool: pelo beige grisáceo revuelto, con mechones finísimos que salen disparados hacia los lados como antenas y dos
# coletas cortas junto a las orejas que acaban en bolas con anillas doradas; una grieta pálida le cruza media cara
CHARS['joss-fool'] = {
    'body': 'normal', 'pal': pal('#bca492', '#f6d6b6', iris='#4a7ab8', shade='#9a7a6a', pale='#fbf2ea', gold='#d8a840'),
    'face': {**NOEARS, 'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': (58, 44)},
    'front': elf('front', 34, 6)
             + [L(quad((26, 18), (0, 8), (-22, 14)), 'shade', 'b', False, False, 2.4), L(quad((74, 18), (100, 8), (122, 14)), 'shade', 'b', False, False, 2.4),
                L(quad((20, 34), (-4, 34), (-24, 44)), 'shade', 'b', False, False, 2.2), L(quad((80, 34), (104, 34), (124, 44)), 'shade', 'b', False, False, 2.2),
                L(quad((44, 8), (40, -10), (30, -20)), 'shade', 'b', False, False, 2.2), L(quad((60, 8), (66, -8), (78, -16)), 'shade', 'b', False, False, 2.2),
                L(outline([(14, 74), (8, 52), (4, 30), (18, 10), (34, 2), (50, 8), (66, 0), (84, 10), (96, 30), (92, 52), (86, 74), (80, 58), (64, 48), (50, 46), (36, 48), (20, 58)])),
                L(outline([(58, 6), (82, 14), (94, 40), (88, 66), (78, 46)]), 'shade', 'b', False),
                L(outline([(14, 60), (24, 64), (26, 88), (18, 92)]), 'mid', 'f', ln=True), L(outline([(86, 60), (76, 64), (74, 88), (82, 92)]), 'mid', 'f', ln=True),
                L(outline([(16, 90), (24, 90), (24, 94), (16, 94)]), 'gold', 'f', ln=True), L(outline([(76, 90), (84, 90), (84, 94), (76, 94)]), 'gold', 'f', ln=True),
                ball(18, 100, 6), ball(82, 100, 6),
                L(outline([(34, 48), (50, 46), (46, 56), (52, 62), (42, 66), (30, 64)]), 'pale', 'f', False),
                L([(50, 46), (46, 56), (52, 62), (42, 66)], OUTC, 'f', False, False, 1.0)],
    'side': [L(quad((40, 6), (20, -12), (-4, -16)), 'shade', 'b', False, False, 2.4), L(quad((20, 24), (-4, 20), (-24, 30)), 'shade', 'b', False, False, 2.2),
             L(outline([(54, 62), (60, 48), (80, 46), (92, 30), (82, 8), (56, -2), (28, 2), (8, 20), (2, 48), (8, 74), (22, 84), (38, 82), (48, 72)])),
             L(outline([(4, 40), (26, 44), (30, 78), (10, 74)]), 'shade', 'b', False),
             L(outline([(60, 58), (70, 60), (70, 86), (62, 90)]), 'mid', 'f', ln=True), ball(66, 96, 6),
             L(outline([(64, 6), (90, 18), (94, 40), (90, 58, 1), (82, 44), (74, 34)]), 'mid', 'f')]
            + elf('side', 32, 6),
    'back': elf('front', 34, 6)
            + [L(quad((26, 18), (0, 8), (-22, 14)), 'shade', 'b', False, False, 2.4), L(quad((74, 18), (100, 8), (122, 14)), 'shade', 'b', False, False, 2.4),
               L(quad((20, 34), (-4, 34), (-24, 44)), 'shade', 'b', False, False, 2.2), L(quad((80, 34), (104, 34), (124, 44)), 'shade', 'b', False, False, 2.2),
               L(outline([(12, 84), (6, 52), (4, 30), (18, 10), (34, 2), (50, 8), (66, 0), (84, 10), (96, 30), (94, 52), (88, 84), (64, 94), (36, 94)])),
               L(outline([(56, 6), (82, 14), (96, 44), (90, 82), (62, 92)]), 'shade', 'b', False),
               ball(16, 98, 6), ball(84, 98, 6)],
}

# Sarjes Luhg: media melena rubia dorada ondulada y en capas, con las puntas abiertas hacia fuera y un flequillo largo
# que le tapa un ojo; más oscura por detrás; ojos verde azulado y boca seria
CHARS['circulus'] = {
    'body': 'normal', 'pal': pal('#f2c274', '#fce4c4', iris='#2a8a8a', shade='#d89a5e', light='#fae0a8'),
    'face': {**NOEARS, 'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': elf('front', 30, 6)
             + [L(outline([(14, 96), (-2, 88, 1), (6, 74), (-6, 60, 1), (4, 52), (2, 26), (18, 6), (50, -4), (82, 6), (98, 26), (96, 52), (106, 60, 1), (94, 74),
                           (102, 88, 1), (86, 96), (82, 66), (18, 66)])),
                L(outline([(58, 2), (84, 12), (98, 40), (94, 84), (82, 56)]), 'shade', 'b', False),
                L(outline([(12, 78), (10, 46), (22, 22), (48, 12), (72, 18), (88, 38), (90, 76), (84, 60), (78, 70, 1), (72, 50), (60, 58), (56, 92, 1), (48, 76),
                           (40, 96, 1), (34, 76), (26, 84, 1), (20, 64)]), 'mid', 'f'),
                L(outline([(30, 22), (48, 16), (40, 30)]), 'light', 'f', False), L(outline([(60, 22), (80, 30), (86, 50), (72, 44)]), 'shade', 'f', False)],
    'side': [L(outline([(54, 64), (58, 50), (80, 48), (94, 34), (90, 12), (66, -4), (36, -4), (12, 10), (0, 34), (-8, 50, 1), (2, 58), (-6, 76, 1), (8, 76), (4, 96, 1),
                        (20, 88), (28, 102, 1), (36, 88), (46, 80)]), 'shade'),
             L(outline([(36, -4), (66, -4), (90, 12), (94, 34), (70, 30), (46, 22), (24, 20), (12, 10)]), 'mid', 'b', False),
             L(outline([(64, 4), (90, 18), (96, 42), (96, 74, 1), (86, 56), (80, 70, 1), (76, 44), (64, 30)]), 'mid', 'f')]
            + elf('side', 28, 6),
    'back': elf('front', 30, 6)
            + [L(outline([(12, 96), (-4, 86, 1), (4, 70), (-8, 56, 1), (4, 48), (2, 26), (18, 6), (50, -4), (82, 6), (98, 26), (96, 48), (108, 56, 1), (96, 70), (104, 86, 1),
                          (88, 96), (72, 106, 1), (62, 96), (50, 108, 1), (38, 96), (28, 106, 1)]), 'shade'),
               L(outline([(20, 8), (50, -4), (80, 8), (90, 30), (50, 40), (10, 30)]), 'mid', 'b', False),
               strand([(30, 30), (24, 60), (30, 96)], 'deep', 'b', 1.0), strand([(70, 30), (76, 60), (70, 96)], 'deep', 'b', 1.0)],
}
