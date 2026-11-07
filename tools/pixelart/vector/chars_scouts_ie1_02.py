"""Ojeadores de IE1 (scouts-ie1), tanda 02: dibujados a partir de su retrato de Victory Road (ninguno de esta tanda tiene
modelo 3D en la enciclopedia); claves 'scouts-ie1:<id>'. Los colores de piel del retrato (más cálidos) se pasan a los tonos
de los modelos 3D. El perfil y la espalda están deducidos del peinado del retrato."""
from chars import CHARS, L, OUTC, blob, ell, messy, outline, pal, rope, strand  # noqa: F401
from chars_sengoku import band
from chars_vr_nikogawa import WIDE, blush, brow_side, brows, crop, ring_glasses, wide_smile  # noqa: F401
from chars_bigwaves import rect_glasses  # noqa: F401
from heads import mirror, quad  # noqa: F401

K = 'scouts-ie1:'
WHITE = (248, 248, 248, 255)
FRECKLE = (196, 120, 84, 255)
BALD = blob([(16, 62), (15, 36), (28, 14), (50, 6), (72, 14), (85, 36), (84, 62), (83, 92), (66, 104), (50, 106), (34, 104), (17, 92)])
SQUARE = blob([(12, 48), (50, 40), (88, 48), (92, 76), (88, 98), (70, 108), (50, 110), (30, 108), (12, 98), (8, 76)])
CHUBBY = blob([(12, 50), (50, 40), (88, 50), (94, 76), (88, 100), (66, 110), (50, 112), (34, 110), (12, 100), (6, 76)])
# tonos de piel: el retrato es más cálido que los modelos 3D
SK_L, SK_LL, SK_T, SK_D, SK_DD = '#fcd4b0', '#fde4c8', '#d6a070', '#b07c50', '#8a5a3a'


def mir(pts):
    """Puntos de un contorno reflejados (izquierda <-> derecha), con las puntas (x, y, 1) incluidas."""
    return [(100 - p[0],) + tuple(p[1:]) for p in pts][::-1]


def band_side(y0, y1, c='band'):
    """Cinta alrededor de la cabeza, de perfil."""
    return L(outline([(4, y0 + 6), (50, y0 + 1), (90, y0 - 3), (91, y1 - 3), (50, y1 + 1), (4, y1 + 6)]), c, 'f', ln=True)


def band_back(y0, y1, c='band'):
    return L(quad((8, y0), (50, y0 - 4), (92, y0)) + quad((92, y1), (50, y1 - 4), (8, y1)), c, 'f', ln=True)


def angled_eyes(y=76, c=OUTC, w=2.4):
    """Ojos apretados en forma de > <."""
    return [L([(29, y - 4), (40, y), (29, y + 4)], c, 'f', False, False, w), L([(71, y - 4), (60, y), (71, y + 4)], c, 'f', False, False, w)]


def freckles(y=86, c=FRECKLE):
    out = []
    for cx in (27, 73):
        for dx, dy in ((-4, 0), (0, -2), (4, 0), (-2, 3), (2, 3)):
            out.append(L(ell(cx + dx, y + dy, 0.9, 0.9), c, 'f', False))
    return out


def wave_mouth(y=96, x0=36, x1=64, c=(130, 70, 50, 255), w=1.6):
    m = (x0 + x1) / 2
    return [L(quad((x0, y - 2), ((x0 + m) / 2, y + 3), (m, y)) + quad((m, y), ((m + x1) / 2, y + 3), (x1, y - 2))[1:], c, 'f', False, False, w)]


# Bear Turnbull: grandote de cara mofletuda y piel tostada; pelo rubio dorado en pinchos altos de cepillo encima, con los
# lados rapados más oscuros; ojillos pequeños, cejas finas y una sonrisa de dientes de conejo
CHARS[K + 'bear-turnbull'] = {
    'body': 'corpulento', 'pal': pal('#e0b020', SK_T, iris='#2a2020', shade='#b88a14', deep='#8a6410'),
    'face': {'eyes': 'dot', 'brows': True, 'mouth': 'buck', 'mouth_y': 93, 'face_front': CHUBBY,
             'hairline': [(14, 64), (17, 48), (30, 42), (50, 40), (70, 42), (83, 48), (86, 64)]},
    'front': [L(outline([(16, 66), (12, 46), (18, 30), (82, 30), (88, 46), (84, 66), (80, 48), (20, 48)]), 'shade'),
              L(outline([(22, 42), (18, 24), (8, 10, 1), (24, 8), (20, -6, 1), (34, 2), (38, -14, 1), (48, 0), (58, -12, 1), (62, 2), (76, -6, 1), (74, 8),
                         (92, 8, 1), (82, 24), (78, 42), (50, 44)])),
              L(outline([(60, 2), (76, -6), (74, 8), (92, 8), (82, 24), (78, 40), (66, 26)]), 'shade', 'b', False),
              strand([(36, 6), (40, 30)], 'deep', 'b', 1.0), strand([(56, 4), (52, 30)], 'deep', 'b', 1.0)]
             + [strand([(x, 50), (x + 1, 64)], 'deep', 'b', 0.8) for x in (17, 83)],
    'side': crop('side', top=12, nape=84, c='shade', shade=False)
            + [L(outline([(78, 42), (84, 30), (98, 22, 1), (84, 16), (90, 2, 1), (74, 4), (70, -12, 1), (58, 0), (46, -14, 1), (40, 2), (26, -6, 1), (24, 10),
                          (8, 14, 1), (14, 28), (22, 40), (50, 42)])),
               L(outline([(10, 16), (24, 12), (30, 30), (22, 40), (14, 28)]), 'shade', 'b', False)],
    'back': crop('back', top=12, nape=84, c='shade', shade=False)
            + [L(outline([(20, 44), (16, 26), (6, 12, 1), (22, 10), (20, -6, 1), (34, 2), (40, -14, 1), (50, 0), (60, -12, 1), (64, 2), (78, -6, 1), (76, 10),
                          (94, 12, 1), (84, 26), (80, 44), (50, 48)])),
               L(outline([(60, 4), (78, -6), (76, 10), (94, 12), (84, 26), (80, 42), (64, 30)]), 'shade', 'b', False)],
}

# Beau Fort: pelo verde azulado en pinchos de punta por encima de una cinta blanca anudada (hachimaki), con las colas que
# le cuelgan por el lado derecho de la imagen y el flequillo en mechones por delante de la cinta; ojos ámbar afilados
CHARS[K + 'beau-fort'] = {
    'body': 'normal', 'pal': pal('#5f9a8c', SK_L, iris='#d0a020', shade='#47786c', deep='#33584e', band='#ece2d2', band_d='#c8b8a4'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': False},
    'front': [L(outline([(14, 66), (10, 44), (14, 24), (6, 10, 1), (22, 12), (18, -4, 1), (34, 4), (40, -16, 1), (50, 2), (60, -14, 1), (66, 4), (84, -4, 1),
                         (80, 14), (94, 14, 1), (88, 30), (90, 46), (86, 66), (80, 50), (20, 50)])),
              L(outline([(62, 2), (84, -4), (80, 14), (94, 14), (88, 30), (90, 46), (86, 62), (76, 36)]), 'shade', 'b', False),
              strand([(30, 8), (36, 30)], 'deep', 'b', 1.0), strand([(50, 4), (50, 30)], 'deep', 'b', 1.0), strand([(68, 8), (64, 30)], 'deep', 'b', 1.0),
              band(44, 55, 'band', 'f', 8),
              L(outline([(84, 50), (100, 58), (104, 92, 1), (94, 68), (88, 94, 1), (84, 62)]), 'band', 'f', ln=True),
              strand([(90, 60), (95, 80)], 'band_d', 'f', 1.0),
              L(outline([(24, 50), (28, 70, 1), (35, 54), (43, 72, 1), (50, 54), (58, 70, 1), (64, 54), (71, 66, 1), (76, 50)]), 'mid', 'f')],
    'side': [L(outline([(78, 50), (86, 40), (98, 34, 1), (88, 26), (96, 10, 1), (78, 10), (72, -10, 1), (60, 2), (46, -14, 1), (38, 4), (22, -6, 1), (20, 12),
                        (4, 16, 1), (8, 32), (2, 54), (8, 72), (20, 84), (34, 82), (38, 66), (46, 58), (62, 54)])),
             L(outline([(4, 40), (28, 44), (40, 58), (34, 82), (20, 84), (8, 72)]), 'shade', 'b', False),
             band_side(44, 55),
             L(outline([(8, 50), (-8, 66), (-14, 96, 1), (-2, 74), (2, 98, 1), (10, 62)]), 'band', 'f', ln=True),
             L(outline([(78, 54), (90, 52), (92, 70, 1), (84, 60)]), 'mid', 'f')],
    'back': [L(outline([(14, 78), (10, 44), (14, 24), (6, 10, 1), (22, 12), (18, -4, 1), (34, 4), (40, -16, 1), (50, 2), (60, -14, 1), (66, 4), (84, -4, 1),
                        (80, 14), (94, 14, 1), (88, 30), (90, 46), (86, 78), (66, 88), (50, 90), (34, 88)])),
             L(outline([(62, 4), (84, -4), (80, 14), (94, 14), (88, 30), (90, 46), (86, 78), (66, 86), (70, 40)]), 'shade', 'b', False),
             band_back(46, 57),
             L(outline([(12, 52), (-4, 62), (-8, 94, 1), (4, 70), (8, 96, 1), (14, 60)]), 'band', 'f', ln=True)],
}

# Beau Painton: pelo rubio muy pálido, peinado hacia atrás y recogido en lo alto en un moñito de pinchos, con un mechón
# largo que le cae en curva por el lado izquierdo de la imagen hasta la mejilla; ojos negros pequeños y boca seria
CHARS[K + 'beau-painton'] = {
    'body': 'normal', 'pal': pal('#f6dcb0', SK_L, iris='#2a2226', shade='#dcbc8c', deep='#b89a6c', tie='#c8a8c8'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93,
             'hairline': [(14, 60), (18, 46), (34, 40), (50, 39), (66, 40), (82, 46), (86, 60)]},
    'front': [L(outline([(54, 12), (52, -6, 1), (60, 0), (66, -16, 1), (70, -1), (82, -8, 1), (76, 8), (70, 16)])),
              L(outline([(16, 62), (14, 36), (26, 16), (50, 8), (74, 16), (86, 36), (84, 62), (78, 46), (22, 46)])),
              L(outline([(60, 12), (78, 20), (86, 38), (84, 58), (76, 36)]), 'shade', 'b', False),
              L(ell(62, 12, 4.4, 3), 'tie', 'b', ln=True),
              strand([(38, 40), (44, 16)], 'shade', 'b', 1.0), strand([(62, 40), (58, 18)], 'shade', 'b', 1.0),
              L(outline([(50, 10), (30, 18), (14, 42), (8, 78), (14, 104, 1), (19, 74), (25, 50), (40, 28), (58, 18)]), 'mid', 'f', ln=True),
              strand([(36, 24), (20, 48), (14, 80)], 'shade', 'f', 1.0)],
    'side': [L(outline([(52, 6), (56, -12, 1), (62, 0), (72, -10, 1), (70, 6), (60, 14)])),
             L(outline([(76, 44), (82, 30), (76, 12), (56, 4), (30, 8), (10, 22), (4, 46), (8, 70), (20, 84), (34, 82), (38, 64), (48, 56), (62, 50)])),
             L(outline([(4, 42), (30, 46), (40, 60), (34, 82), (20, 84), (8, 70)]), 'shade', 'b', False),
             L(ell(58, 8, 3, 4), 'tie', 'b', ln=True),
             strand([(74, 30), (50, 12)], 'shade', 'b', 1.0), strand([(70, 42), (30, 20)], 'shade', 'b', 1.0)],
    'back': [L(outline([(42, 12), (40, -8, 1), (48, 0), (54, -16, 1), (60, -1), (70, -8, 1), (64, 8), (58, 16)])),
             L(outline([(16, 74), (12, 40), (22, 16), (50, 6), (78, 16), (88, 40), (84, 74), (66, 86), (50, 88), (34, 86)])),
             L(outline([(58, 10), (78, 18), (88, 42), (84, 74), (66, 84), (64, 40)]), 'shade', 'b', False),
             L(ell(50, 10, 4.4, 3), 'tie', 'b', ln=True),
             L(outline([(16, 40), (6, 70), (8, 100, 1), (14, 74), (20, 48)]), 'mid', 'b', ln=True)]
            + [strand([(x, 14), (x, 84)], 'shade', 'b', 1.0) for x in (36, 50, 64)],
}

# Ben Curd: grandullón de cara cuadrada y mandíbula ancha; pelo castaño muy oscuro corto y plano arriba, con dos picos en las
# esquinas como cuernos y patillas largas hasta la mandíbula; cejas gruesas enfadadas, ojos pequeños y sonrisa torcida
CHARS[K + 'ben-curd'] = {
    'body': 'corpulento', 'pal': pal('#3a2c1e', SK_L, iris='#2a2020', shade='#2a2016', deep='#1c140e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'face_front': SQUARE, 'nose': (50, 86, 3.4), 'ear_out': 4,
             'hairline': [(10, 94), (16, 94), (18, 52), (30, 45), (50, 45), (70, 45), (82, 52), (84, 94), (90, 94)]},
    'front': [L(outline([(10, 92), (6, 50), (8, 20), (4, -2, 1), (24, 12), (50, 14), (76, 12), (96, -2, 1), (92, 20), (94, 50), (90, 92), (84, 94), (82, 56),
                         (78, 46), (22, 46), (18, 56), (16, 94)])),
              L(outline([(60, 14), (78, 12), (96, -2), (92, 22), (94, 50), (90, 90), (84, 90), (84, 40)]), 'shade', 'b', False)]
             + brows(66, 'deep', 5.5, 15, 1.4, 15)
             + [L(quad((30, 95), (50, 104), (70, 90)), (130, 70, 50, 255), 'f', False, False, 1.8)],
    'side': [L(outline([(74, 48), (84, 40), (90, 24), (98, 6, 1), (80, 8), (54, 6), (26, 8), (8, -2, 1), (8, 22), (4, 48), (8, 72), (20, 84), (36, 82),
                        (40, 66), (48, 60), (60, 56)])),
             L(outline([(52, 54), (62, 54), (64, 92), (56, 96)])),
             L(outline([(4, 44), (30, 46), (42, 60), (36, 82), (20, 84), (8, 72)]), 'shade', 'b', False)]
            + brow_side(66, 'deep', 5.5, 1.4),
    'back': [L(outline([(12, 86), (8, 50), (6, 20), (4, -2, 1), (24, 10), (50, 8), (76, 10), (96, -2, 1), (94, 20), (92, 50), (88, 86), (66, 90), (50, 92),
                        (34, 90)])),
             L(outline([(60, 10), (76, 10), (96, -2), (94, 22), (92, 52), (88, 86), (66, 90), (66, 40)]), 'shade', 'b', False)],
}

# Ben Delimms (portero): piel morena y pelo rubio muy pálido peinado hacia atrás, con las puntas en pico detrás de las
# orejas; ojos redondos lilas muy abiertos, cejas enfadadas y boca apretada
CHARS[K + 'ben-delimms'] = {
    'body': 'normal', 'pal': pal('#f6dcb4', SK_D, iris='#b898b8', shade='#dcbc90', deep='#b8966c'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94,
             'hairline': [(14, 58), (18, 46), (34, 38), (50, 36), (66, 38), (82, 46), (86, 58)]},
    'front': [L(outline([(15, 50), (3, 68, 1), (14, 64), (18, 58)])), L(outline(mir([(15, 50), (3, 68, 1), (14, 64), (18, 58)]))),
              L(outline([(16, 58), (11, 40), (18, 14), (50, 0), (82, 14), (89, 40), (84, 58), (80, 50), (20, 50)])),
              L(outline([(58, 2), (82, 14), (90, 40), (86, 64), (78, 36)]), 'shade', 'b', False)]
             + [strand([(x, 40), (x * 0.9 + 5, 8)], 'shade', 'b', 1.0) for x in (30, 42, 56, 70)],
    'side': [L(outline([(80, 46), (86, 30), (80, 12), (56, 0), (28, 4), (8, 20), (0, 44), (-8, 64, 1), (8, 62), (16, 80), (32, 84), (38, 64), (48, 56), (64, 50)])),
             L(outline([(2, 44), (30, 48), (40, 62), (32, 84), (16, 80)]), 'shade', 'b', False),
             strand([(80, 36), (40, 8)], 'shade', 'b', 1.0), strand([(74, 46), (20, 20)], 'shade', 'b', 1.0)],
    'back': [L(outline([(14, 76), (2, 82, 1), (10, 60), (10, 40), (18, 14), (50, 2), (82, 14), (90, 40), (90, 60), (98, 82, 1), (86, 76), (66, 86), (50, 88),
                        (34, 86)])),
             L(outline([(58, 6), (82, 14), (90, 42), (86, 76), (66, 84), (66, 40)]), 'shade', 'b', False)]
            + [strand([(x, 6), (x, 84)], 'shade', 'b', 1.0) for x in (36, 50, 64)],
}

# Ben Evolent: piel tostada; pelo morado oscuro revuelto en pinchos por todas partes, con una cinta roja en la frente y el
# flequillo en mechones que le tapa un ojo; ojos grandes oscuros y sonrisa
CHARS[K + 'ben-evolent'] = {
    'body': 'normal', 'pal': pal('#4a3e5c', SK_T, iris='#2a2028', shade='#3a3048', deep='#282034', band='#c85c5c', band_d='#a04444'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(12, 70), (2, 52, 1), (12, 46), (2, 30, 1), (14, 24), (8, 6, 1), (24, 10), (26, -8, 1), (38, 4), (48, -14, 1), (56, 4), (70, -8, 1),
                         (72, 8), (90, 4, 1), (84, 20), (100, 28, 1), (88, 36), (98, 54, 1), (88, 56), (88, 70), (80, 52), (20, 52)])),
              L(outline([(62, 4), (90, 4), (84, 20), (100, 28), (88, 36), (98, 54), (88, 66), (80, 36)]), 'shade', 'b', False),
              band(42, 54, 'band', 'f', 8), strand([(14, 46), (50, 39), (86, 46)], 'band_d', 'f', 1.2),
              L(outline([(20, 52), (24, 86, 1), (33, 58), (40, 70, 1), (46, 55), (56, 64, 1), (60, 54), (70, 62, 1), (78, 52)]), 'mid', 'f'),
              strand([(28, 56), (25, 80)], 'deep', 'f', 1.0)],
    'side': [L(outline([(80, 48), (86, 40), (100, 38, 1), (88, 28), (98, 12, 1), (80, 12), (78, -8, 1), (62, 2), (52, -14, 1), (40, 2), (24, -10, 1), (20, 10),
                        (0, 10, 1), (8, 28), (-6, 40, 1), (6, 48), (-2, 66, 1), (10, 68), (18, 86, 1), (28, 78), (38, 66), (46, 58), (62, 54)])),
             L(outline([(4, 42), (28, 46), (40, 60), (28, 78), (12, 70)]), 'shade', 'b', False),
             band_side(42, 53),
             L(outline([(78, 52), (92, 52), (96, 74, 1), (86, 60)]), 'mid', 'f')],
    'back': [L(outline([(12, 78), (2, 60, 1), (12, 52), (2, 30, 1), (14, 24), (8, 6, 1), (24, 10), (26, -8, 1), (38, 4), (48, -14, 1), (56, 4), (70, -8, 1),
                        (72, 8), (90, 4, 1), (84, 20), (100, 28, 1), (88, 36), (98, 60, 1), (88, 78), (76, 90, 1), (66, 82), (56, 94, 1), (48, 82), (36, 94, 1),
                        (30, 82), (20, 90, 1)])),
             L(outline([(62, 6), (90, 4), (84, 20), (100, 28), (88, 36), (98, 60), (88, 78), (68, 82), (70, 40)]), 'shade', 'b', False),
             band_back(44, 55)],
}

# Benedict Eggers: chicarrón mofletudo; pelo rubio dorado en una nube abombada de rizos que le hace visera sobre la frente;
# ojos apretados en > <, cejas gruesas doradas y una boca ondulada de esfuerzo
CHARS[K + 'benedict-eggers'] = {
    'body': 'corpulento', 'pal': pal('#e0b420', SK_L, shade='#b88c14', deep='#8a6810', brow='#c89818'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': CHUBBY, 'nose': (50, 86, 3.6),
             'hairline': [(8, 72), (14, 56), (22, 50), (30, 54), (38, 48), (46, 52), (54, 48), (62, 52), (70, 48), (78, 54), (86, 56), (92, 72)]},
    'front': [L(outline([(8, 74), (0, 54), (4, 34), (12, 16), (28, 2), (50, -6), (72, 2), (88, 14), (98, 34), (100, 56), (92, 74), (84, 64), (80, 60), (20, 60),
                         (16, 64)])),
              L(outline([(62, -2), (88, 14), (98, 36), (98, 56), (90, 70), (84, 46), (76, 24)]), 'shade', 'b', False),
              strand([(24, 14), (30, 26), (24, 38)], 'deep', 'b', 1.0), strand([(48, 2), (54, 16), (48, 30)], 'deep', 'b', 1.0),
              strand([(72, 10), (78, 24), (72, 38)], 'deep', 'b', 1.0)]
             + angled_eyes(77) + brows(66, 'brow', 5.0, 15, 1.6, 14) + wave_mouth(97),
    'side': [L(outline([(80, 50), (90, 44), (98, 30), (92, 12), (74, -2), (48, -6), (24, 0), (6, 16), (-2, 38), (0, 60), (10, 78), (24, 86), (36, 80), (40, 66),
                        (48, 58), (64, 54)])),
             L(outline([(0, 42), (28, 44), (40, 60), (34, 80), (20, 84), (6, 68)]), 'shade', 'b', False),
             strand([(70, 6), (76, 20), (70, 32)], 'deep', 'b', 1.0), strand([(40, 4), (46, 18), (40, 32)], 'deep', 'b', 1.0),
             L([(78, 72), (86, 76), (78, 80)], OUTC, 'f', False, False, 2.4)] + brow_side(66, 'brow', 5.0, 1.6),
    'back': [L(outline([(10, 80), (0, 56), (4, 32), (14, 12), (32, 0), (50, -4), (68, 0), (86, 12), (96, 32), (100, 56), (90, 80), (74, 88), (62, 84), (50, 90),
                        (38, 84), (26, 88)])),
             L(outline([(60, 0), (86, 12), (96, 34), (100, 56), (90, 80), (74, 86), (70, 40)]), 'shade', 'b', False),
             strand([(30, 20), (36, 34), (30, 48)], 'deep', 'b', 1.0), strand([(54, 30), (60, 44), (54, 58)], 'deep', 'b', 1.0)],
}

# Bennett Byers (portero): pelo verde ondulado por la mandíbula, con las puntas en bucles hacia fuera, y una cinta gris
# azulada en la frente; pecas, cejas verdes enfadadas, ojos amarillos y media sonrisa
CHARS[K + 'bennett-byers'] = {
    'body': 'normal', 'pal': pal('#4f8a5c', SK_L, iris='#c8b04c', shade='#3c6c48', deep='#2c5236', band='#6e9c9c', band_d='#527a7a'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(10, 98, 1), (2, 80), (4, 46), (14, 20), (34, 4), (50, 0), (66, 4), (86, 20), (96, 46), (98, 80), (90, 98, 1), (86, 88), (82, 60), (18, 60),
                         (14, 88)])),
              L(outline([(62, 4), (86, 20), (96, 46), (98, 80), (90, 96), (84, 70), (80, 30)]), 'shade', 'b', False),
              strand([(30, 10), (24, 30)], 'deep', 'b', 1.0), strand([(70, 10), (76, 30)], 'deep', 'b', 1.0),
              strand([(8, 70), (10, 90)], 'deep', 'b', 1.0), strand([(92, 70), (90, 90)], 'deep', 'b', 1.0),
              band(44, 56, 'band', 'f', 8), strand([(14, 50), (50, 43), (86, 50)], 'band_d', 'f', 1.0),
              L(outline([(18, 54), (22, 66, 1), (30, 56), (70, 56), (78, 66, 1), (82, 54)]), 'mid', 'f')]
             + brows(65, 'deep', 3.6, 14, 1.4, 11) + freckles(86),
    'side': [L(outline([(80, 50), (88, 40), (88, 22), (72, 4), (48, -2), (24, 4), (6, 22), (-2, 50), (0, 80), (8, 98, 1), (20, 90), (30, 100, 1), (38, 84), (40, 66),
                        (48, 58), (64, 54)])),
             L(outline([(0, 46), (30, 48), (40, 64), (36, 86), (20, 92), (6, 84)]), 'shade', 'b', False),
             band_side(44, 55)] + brow_side(65, 'deep', 3.6, 1.4),
    'back': [L(outline([(10, 98, 1), (2, 80), (4, 46), (14, 20), (34, 4), (50, 0), (66, 4), (86, 20), (96, 46), (98, 80), (90, 98, 1), (76, 92), (64, 100, 1),
                        (50, 92), (36, 100, 1), (24, 92)])),
             L(outline([(60, 4), (86, 20), (96, 46), (98, 80), (90, 96), (74, 92), (70, 40)]), 'shade', 'b', False),
             band_back(46, 57)]
            + [strand([(x, 60), (x, 92)], 'deep', 'b', 1.0) for x in (30, 50, 70)],
}

# Benny Factor (portero): gorra de visera plana gris oliva, abombada, con un botón arriba y la banda de abajo cosida, de la
# que asoman mechones rubios de punta sobre la frente; ojazos negros, cejas enfadadas, bigotitos de gato y sonrisa
CHARS[K + 'benny-factor'] = {
    'body': 'normal', 'pal': pal('#e8c030', SK_L, iris='#1e1a1c', shade='#c09820', deep='#8a6c14', cap='#8c8672', cap_d='#6c6656', cap_b='#5c5648'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(16, 64), (14, 50), (24, 50), (20, 64)])), L(outline(mir([(16, 64), (14, 50), (24, 50), (20, 64)]))),
              L(outline([(20, 50), (24, 66, 1), (30, 54), (36, 68, 1), (42, 54), (58, 54), (64, 68, 1), (70, 54), (76, 66, 1), (80, 50)]), 'mid', 'f'),
              L(ell(50, -10, 6, 5), 'cap', 'f', ln=True),
              L(outline([(4, 48), (2, 28), (12, 8), (30, -6), (50, -8), (70, -6), (88, 8), (98, 28), (96, 48), (80, 54), (50, 55), (20, 54)]), 'cap', 'f', ln=True),
              L(outline([(60, -6), (88, 8), (98, 30), (96, 48), (82, 50), (80, 20)]), 'cap_d', 'f', False),
              L(quad((10, 44), (50, 36), (90, 44)) + quad((90, 54), (50, 46), (10, 54)), 'cap_b', 'f', ln=True)]
             + [L([(x, 42 - abs(x - 50) * 0.08), (x + 2, 47 - abs(x - 50) * 0.08)], 'cap_d', 'f', False, False, 1.0) for x in range(16, 86, 6)]
             + [L([(14, 84), (22, 86)], OUTC, 'f', False, False, 1.0), L([(14, 89), (22, 89)], OUTC, 'f', False, False, 1.0),
                L([(86, 84), (78, 86)], OUTC, 'f', False, False, 1.0), L([(86, 89), (78, 89)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(8, 50), (6, 70), (20, 84), (36, 82), (40, 62), (30, 50)])),
             L(outline([(82, 52), (92, 50), (94, 68, 1), (86, 60)]), 'mid', 'f'),
             L(ell(48, -10, 5, 5), 'cap', 'f', ln=True),
             L(outline([(98, 46), (100, 30), (86, 8), (58, -6), (28, -4), (8, 12), (0, 32), (2, 50), (50, 54), (92, 52)]), 'cap', 'f', ln=True),
             L(outline([(2, 34), (40, 34), (60, 52), (2, 50)]), 'cap_d', 'f', False),
             L(outline([(2, 42), (50, 46), (98, 40), (98, 50), (50, 56), (2, 52)]), 'cap_b', 'f', ln=True)],
    'back': [L(outline([(16, 52), (14, 74), (34, 86), (50, 88), (66, 86), (86, 74), (84, 52)])),
             L(ell(50, -10, 6, 5), 'cap', 'f', ln=True),
             L(outline([(4, 50), (2, 28), (12, 8), (30, -6), (50, -8), (70, -6), (88, 8), (98, 28), (96, 50), (50, 56)]), 'cap', 'f', ln=True),
             L(outline([(60, -6), (88, 8), (98, 30), (96, 50), (64, 54)]), 'cap_d', 'f', False),
             L(quad((4, 44), (50, 38), (96, 44)) + quad((96, 54), (50, 48), (4, 54)), 'cap_b', 'f', ln=True)],
}

# Bert Neptune: melena rubia ceniza por la mandíbula con las puntas en pico y un flequillo largo de lado que le tapa el ojo
# izquierdo; gafas finas sin montura de abajo, ojos gris azulado y boca seria
CHARS[K + 'bert-neptune'] = {
    'body': 'normal', 'pal': pal('#d8cc9c', SK_L, iris='#7896b0', shade='#b4a878', deep='#8c8058', frame='#a09478'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(10, 98, 1), (6, 70), (6, 40), (16, 16), (36, 2), (50, 0), (66, 2), (86, 14), (96, 40), (94, 70), (92, 98, 1), (84, 84), (82, 60), (18, 60),
                         (16, 84)])),
              L(outline([(60, 2), (86, 14), (96, 40), (94, 70), (92, 96), (84, 70), (80, 30)]), 'shade', 'b', False)]
             + rect_glasses('front', 77, (150, 138, 110, 255))
             + [L(outline([(16, 62), (18, 40), (30, 24), (50, 18), (72, 24), (86, 42), (90, 72, 1), (82, 60), (76, 82, 1), (68, 62), (60, 70, 1), (52, 56), (42, 62, 1),
                           (36, 50), (26, 58, 1)]), 'mid', 'f'),
                strand([(56, 24), (70, 50), (76, 76)], 'shade', 'f', 1.0), strand([(40, 24), (48, 44)], 'shade', 'f', 1.0)],
    'side': [L(outline([(80, 48), (88, 40), (90, 24), (76, 6), (50, -2), (24, 4), (6, 22), (0, 50), (2, 80), (8, 98, 1), (18, 88), (28, 98, 1), (34, 80), (38, 66),
                        (48, 58), (64, 54)])),
             L(outline([(2, 46), (30, 50), (38, 66), (32, 86), (18, 90), (6, 84)]), 'shade', 'b', False),
             L(outline([(78, 46), (92, 48), (94, 72, 1), (84, 58)]), 'mid', 'f')]
            + rect_glasses('side', 77, (150, 138, 110, 255)),
    'back': [L(outline([(10, 98, 1), (6, 70), (6, 40), (16, 16), (36, 2), (50, 0), (66, 2), (86, 14), (96, 40), (94, 70), (92, 98, 1), (78, 90), (66, 98, 1),
                        (54, 90), (44, 98, 1), (32, 90), (22, 98, 1)])),
             L(outline([(60, 2), (86, 14), (96, 40), (94, 70), (92, 96), (76, 90), (70, 40)]), 'shade', 'b', False)]
            + [strand([(x, 8), (x, 90)], 'shade', 'b', 1.0) for x in (34, 50, 66)],
}

# Berty Adman (portero): cara alargada; pelo castaño malva en un tupé redondo y abultado que le hace visera, con las
# patillas en rizos por las orejas; ojillos de punto, nariz redonda y sonrisita
CHARS[K + 'berty-adman'] = {
    'body': 'normal', 'pal': pal('#a07870', SK_L, iris='#2a2020', shade='#80605a', deep='#604440'),
    'face': {'eyes': 'dot', 'brows': True, 'mouth': 'smile', 'mouth_y': 95, 'nose': (50, 86, 2.6),
             'hairline': [(12, 76), (16, 54), (26, 48), (50, 46), (74, 48), (84, 54), (88, 76)]},
    'front': [L(outline([(12, 78), (8, 64), (10, 50), (6, 30), (14, 8), (36, -6), (62, -6), (84, 4), (94, 24), (90, 50), (92, 64), (88, 78), (82, 64), (80, 56),
                         (20, 56), (18, 64)])),
              L(outline([(60, -4), (84, 4), (94, 26), (90, 50), (92, 64), (86, 74), (82, 40)]), 'shade', 'b', False),
              strand([(26, 10), (40, 6), (54, 14)], 'deep', 'b', 1.0), strand([(30, 28), (50, 20), (70, 28)], 'deep', 'b', 1.0),
              strand([(12, 60), (16, 66), (12, 72)], 'deep', 'b', 1.0), strand([(88, 60), (84, 66), (88, 72)], 'deep', 'b', 1.0)],
    'side': [L(outline([(82, 50), (94, 40), (96, 24), (82, 4), (56, -6), (28, -2), (8, 14), (0, 40), (4, 66), (16, 82), (32, 84), (36, 70), (42, 60), (40, 50), (60, 52)])),
             L(outline([(36, 56), (48, 56), (52, 78), (44, 86), (38, 78)])),
             L(outline([(0, 40), (28, 44), (36, 70), (32, 84), (16, 82), (4, 66)]), 'shade', 'b', False),
             strand([(90, 30), (70, 12), (40, 6)], 'deep', 'b', 1.0)],
    'back': [L(outline([(12, 80), (8, 50), (6, 28), (16, 6), (38, -6), (62, -6), (84, 6), (94, 28), (92, 50), (88, 80), (66, 90), (50, 92), (34, 90)])),
             L(outline([(58, -4), (84, 6), (94, 30), (92, 50), (88, 80), (66, 88), (70, 40)]), 'shade', 'b', False),
             strand([(30, 20), (50, 14), (70, 20)], 'deep', 'b', 1.0)],
}

# Biff Beeston (portero): cabeza rapada con una sombra de pelo naranja de puntas cortas y una cresta tiesa en el centro;
# ojos negros rasgados y enfadados, una tirita en la mejilla, boca de morros y una perilla naranja en anillo
CHARS[K + 'biff-beeston'] = {
    'body': 'normal', 'pal': pal('#e88a30', SK_L, iris='#1e1a1c', shade='#c06c20', deep='#94501a', tape='#f2e6d8'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'none', 'mouth_y': 95,
             'hairline': [(14, 56), (18, 46), (24, 42), (30, 44), (36, 38), (42, 41), (50, 36), (58, 41), (64, 38), (70, 44), (76, 42), (82, 46), (86, 56)]},
    'front': [L(outline([(16, 58), (12, 40), (20, 20), (50, 12), (80, 20), (88, 40), (84, 58), (80, 48), (20, 48)])),
              L(outline([(43, 18), (45, -4), (50, -26, 1), (56, -4), (57, 18)])),
              L(outline([(51, -20), (56, -4), (57, 16), (52, 14)]), 'shade', 'b', False),
              L(outline([(62, 82), (74, 76), (78, 84), (66, 90)]), 'tape', 'f', ln=True),
              L(quad((38, 95), (50, 89), (62, 95)) + quad((62, 95), (50, 99), (38, 95))[1:], (196, 110, 90, 255), 'f', ln=True),
              L(quad((42, 100), (50, 110), (58, 100)), 'mid', 'f', False, False, 2.6)],
    'side': crop('side', top=12, nape=82, shade=False)
            + [L(outline([(36, 14), (42, -6), (54, -24, 1), (60, -6), (68, 10), (50, 16)]))],
    'back': crop('back', top=12, nape=82, shade=False)
            + [L(outline([(44, 16), (45, -4), (50, -22, 1), (55, -4), (56, 16), (54, 60), (50, 70), (46, 60)]))],
}

# Bill Aegis: mandíbula cuadrada; pelo castaño rojizo corto y plano arriba, con dos picos de punta en las esquinas; ojos
# afilados enfadados, nariz grande y la boca en una raya recta
CHARS[K + 'bill-aegis'] = {
    'body': 'normal', 'pal': pal('#b04a1c', SK_L, iris='#1e1a1c', shade='#8a3814', deep='#64280e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'face_front': SQUARE, 'nose': (50, 86, 3.2),
             'hairline': [(14, 58), (18, 48), (34, 46), (50, 46), (66, 46), (82, 48), (86, 58)]},
    'front': [L(outline([(16, 60), (12, 30), (8, 6, 1), (26, 14), (50, 16), (74, 14), (92, 6, 1), (88, 30), (84, 60), (80, 50), (20, 50)])),
              L(outline([(60, 16), (74, 14), (92, 6), (88, 30), (84, 58), (78, 34)]), 'shade', 'b', False),
              L([(32, 97), (68, 97)], OUTC, 'f', False, False, 1.6)],
    'side': [L(outline([(74, 48), (84, 42), (88, 24), (96, 8, 1), (78, 10), (54, 10), (26, 10), (8, 2, 1), (8, 24), (4, 48), (8, 70), (20, 82), (34, 80), (38, 64),
                        (46, 56), (60, 52)])),
             L(outline([(4, 44), (28, 46), (38, 62), (34, 80), (20, 82), (8, 70)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 78), (12, 30), (8, 6, 1), (26, 12), (50, 12), (74, 12), (92, 6, 1), (88, 30), (84, 78), (66, 86), (50, 88), (34, 86)])),
             L(outline([(60, 14), (74, 12), (92, 6), (88, 30), (84, 78), (66, 84), (66, 40)]), 'shade', 'b', False)],
}

# Bill Dozer (portero): pelo rosa rojizo en pinchos echados hacia la derecha de la imagen, con mechones que le caen por la
# frente; gafas de sol marrones rectangulares y sonrisa de lado
CHARS[K + 'bill-dozer'] = {
    'body': 'normal', 'pal': pal('#d0606c', SK_L, iris='#2a2020', shade='#a84a56', deep='#80343e', lens='#6a5232'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(16, 64), (12, 40), (16, 18), (10, 4, 1), (28, 8), (30, -10, 1), (44, 2), (56, -14, 1), (62, 2), (80, -4, 1), (76, 12), (98, 14, 1), (86, 28),
                         (100, 44, 1), (86, 48), (84, 64), (78, 52), (20, 52)])),
              L(outline([(60, 2), (80, -4), (76, 12), (98, 14), (86, 28), (100, 44), (86, 48), (84, 62), (78, 34)]), 'shade', 'b', False),
              L(outline([(18, 56), (22, 44), (36, 36), (50, 34), (66, 36), (80, 44), (84, 56), (78, 52), (74, 68, 1), (68, 50), (60, 62, 1), (54, 48), (44, 58, 1),
                         (40, 48), (28, 54, 1), (24, 48)]), 'mid', 'f'),
              L(outline([(20, 70), (46, 70), (44, 81), (25, 81)]), 'lens', 'f', ln=True), L(outline(mir([(20, 70), (46, 70), (44, 81), (25, 81)])), 'lens', 'f', ln=True),
              L([(46, 72), (54, 72)], OUTC, 'f', False, False, 1.6), L([(20, 71), (14, 70)], OUTC, 'f', False, False, 1.6),
              L([(80, 71), (86, 70)], OUTC, 'f', False, False, 1.6)],
    'side': [L(outline([(80, 50), (88, 42), (102, 40, 1), (90, 32), (100, 18, 1), (82, 16), (82, -2, 1), (66, 6), (56, -14, 1), (44, 4), (26, -6, 1), (24, 12),
                        (6, 16, 1), (10, 30), (2, 50), (8, 72), (20, 84), (34, 82), (38, 66), (46, 58), (62, 54)])),
             L(outline([(4, 44), (28, 46), (40, 60), (34, 82), (20, 84), (8, 72)]), 'shade', 'b', False),
             L(outline([(78, 70), (90, 70), (89, 81), (79, 81)]), 'lens', 'f', ln=True), L([(50, 72), (78, 72)], OUTC, 'f', False, False, 1.6)],
    'back': [L(outline([(16, 78), (12, 40), (16, 18), (10, 4, 1), (28, 8), (30, -10, 1), (44, 2), (56, -14, 1), (62, 2), (80, -4, 1), (76, 12), (98, 14, 1), (86, 28),
                        (100, 44, 1), (86, 50), (84, 78), (66, 88), (50, 90), (34, 88)])),
             L(outline([(60, 4), (80, -4), (76, 12), (98, 14), (86, 28), (100, 44), (86, 50), (84, 78), (66, 86), (70, 40)]), 'shade', 'b', False),
             L([(14, 72), (20, 74)], OUTC, 'f', False, False, 1.6), L([(86, 72), (80, 74)], OUTC, 'f', False, False, 1.6)],
}

# Bill Looney: calvo, con una cicatriz en zigzag como un rayo que le baja por la frente y el ojo derecho; ojos blancos sin
# pupila y enfadados, nariz grande y sonrisa torcida
CHARS[K + 'bill-looney'] = {
    'body': 'normal', 'pal': pal('#f0c8a0', SK_L, iris='#f4f4f4', bolt='#c8985a', bolt_d='#a07440'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'hairline': False, 'nose': (50, 86, 3.4), 'face_front': BALD},
    'front': [L(outline([(38, 44), (28, 62), (36, 62), (26, 84, 1), (44, 59), (35, 59), (44, 44)]), 'bolt', 'f', ln=True),
              L(quad((36, 95), (52, 100), (66, 92)), (130, 70, 50, 255), 'f', False, False, 1.6)],
    'side': [],
    'back': [],
}

# Bill Moony: cabeza rapada con una sombra de pelo gris lila y una coleta negra larguísima, como un látigo, que le sale de
# la coronilla, se levanta en curva y le cae por detrás; ojos afilados con raya roja y media sonrisa; cara alargada
CHARS[K + 'bill-moony'] = {
    'body': 'delgado', 'pal': pal('#b8a2b2', SK_L, iris='#2a2020', shade='#988292', deep='#786270', queue='#22202a', queue_d='#3a3644'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(14, 60), (18, 46), (34, 40), (50, 38), (66, 40), (82, 46), (86, 60)]},
    'front': [L(outline([(16, 62), (12, 40), (20, 18), (50, 8), (80, 18), (88, 40), (84, 62), (80, 48), (20, 48)])),
              L(rope((60, 12), (84, -40), (88, 10), 5), 'queue', 'b'), L(rope((88, 10), (100, 40), (88, 74), 4.4), 'queue', 'b'),
              L([(24, 70), (42, 74)], (200, 50, 50, 255), 'f', False, False, 1.2), L([(76, 70), (58, 74)], (200, 50, 50, 255), 'f', False, False, 1.2)]
             + [strand([(x, 14 + abs(x - 50) * 0.3), (x, 40)], 'shade', 'b', 0.8) for x in (30, 40, 50, 60, 70)],
    'side': crop('side', top=6, nape=84, shade=False)
            + [L(rope((44, 4), (60, -40), (20, -20), 5), 'queue', 'b'), L(rope((20, -20), (-10, 10), (0, 60), 4.4), 'queue', 'b')],
    'back': crop('back', top=6, nape=84, shade=False)
            + [L(rope((50, 6), (40, -40), (20, 0), 5), 'queue', 'b'), L(rope((20, 0), (6, 40), (24, 80), 4.4), 'queue', 'f')],
}

# Bill Mumm: pelo rosa granate ondulado por la mandíbula, con raya al lado, el flequillo echado hacia la derecha de la imagen
# y las puntas hacia fuera; gafas redondas de pasta marrón y sonrisa
CHARS[K + 'bill-mumm'] = {
    'body': 'normal', 'pal': pal('#c06470', SK_L, iris='#2a2020', shade='#9a4c58', deep='#743842'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(8, 94, 1), (4, 72), (6, 40), (16, 16), (36, 2), (50, 0), (66, 2), (86, 16), (96, 40), (96, 72), (94, 94, 1), (84, 82), (82, 60), (18, 60),
                         (16, 82)])),
              L(outline([(62, 2), (86, 16), (96, 40), (96, 72), (92, 92), (84, 70), (80, 30)]), 'shade', 'b', False),
              strand([(8, 70), (12, 86)], 'deep', 'b', 1.0), strand([(92, 70), (88, 86)], 'deep', 'b', 1.0)]
             + ring_glasses('front', 77, (90, 56, 34, 255), 2.2, 9.5, 7.5, 14)
             + [L(outline([(16, 62), (18, 40), (32, 26), (52, 20), (74, 26), (86, 44), (86, 64, 1), (78, 52), (66, 46), (50, 44), (36, 48), (26, 56, 1), (22, 48)]), 'mid', 'f'),
                strand([(40, 26), (60, 34), (76, 50)], 'shade', 'f', 1.0)],
    'side': [L(outline([(80, 48), (88, 40), (90, 24), (76, 6), (50, -2), (24, 4), (6, 22), (0, 50), (2, 80), (6, 96, 1), (16, 86), (28, 96, 1), (34, 80), (38, 66),
                        (48, 58), (64, 54)])),
             L(outline([(2, 46), (30, 50), (38, 66), (32, 86), (16, 88), (6, 84)]), 'shade', 'b', False)]
            + ring_glasses('side', 77, (90, 56, 34, 255), 2.2, 5, 7.5),
    'back': [L(outline([(8, 94, 1), (4, 72), (6, 40), (16, 16), (36, 2), (50, 0), (66, 2), (86, 16), (96, 40), (96, 72), (94, 94, 1), (78, 88), (64, 94, 1),
                        (50, 88), (36, 94, 1), (22, 88)])),
             L(outline([(60, 2), (86, 16), (96, 40), (96, 72), (92, 92), (76, 88), (70, 40)]), 'shade', 'b', False)]
            + [strand([(x, 10), (x + 2, 86)], 'deep', 'b', 1.0) for x in (30, 50, 70)],
}

# Bill Phee (portero): pelo verde azulado liso, plano y peinado hacia atrás arriba, con dos cortinas largas que le caen
# rectas por detrás de las orejas hasta los hombros; frente alta, mejillas hundidas, párpados caídos y sonrisa
CHARS[K + 'bill-phee'] = {
    'body': 'delgado', 'pal': pal('#4f8a80', SK_L, iris='#1e1a1c', shade='#3c6c64', deep='#2c524c'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'nose': (50, 85, 2.6),
             'hairline': [(10, 112), (19, 112), (20, 44), (50, 40), (80, 44), (81, 112), (90, 112)]},
    'front': [L(outline([(12, 112), (10, 60), (12, 22), (12, 4), (50, 6), (88, 2), (88, 22), (90, 60), (88, 112), (80, 112), (80, 56), (78, 42), (22, 42),
                         (20, 56), (20, 112)])),
              L(outline([(60, 6), (92, -2), (88, 22), (90, 60), (88, 110), (82, 110), (82, 40)]), 'shade', 'b', False),
              strand([(16, 50), (16, 108)], 'deep', 'b', 1.0), strand([(84, 50), (84, 108)], 'deep', 'b', 1.0),
              L([(28, 72), (44, 72)], OUTC, 'f', False, False, 2.0), L([(56, 72), (72, 72)], OUTC, 'f', False, False, 2.0),
              L(quad((24, 84), (28, 92), (26, 98)), (190, 130, 90, 255), 'f', False, False, 1.0),
              L(quad((76, 84), (72, 92), (74, 98)), (190, 130, 90, 255), 'f', False, False, 1.0)],
    'side': [L(outline([(78, 42), (86, 30), (82, 10), (90, -2, 1), (56, 2), (26, 6), (8, 20), (2, 50), (4, 90), (8, 116), (34, 116), (34, 64), (44, 56), (62, 48)])),
             L(outline([(4, 50), (30, 52), (32, 114), (8, 114)]), 'shade', 'b', False),
             strand([(80, 24), (40, 10)], 'deep', 'b', 1.0), L([(76, 72), (85, 72)], OUTC, 'f', False, False, 2.0)],
    'back': [L(outline([(12, 116), (10, 60), (12, 22), (8, 0, 1), (50, 4), (92, -2, 1), (88, 22), (90, 60), (88, 116), (50, 118)])),
             L(outline([(60, 4), (92, -2), (88, 22), (90, 60), (88, 114), (64, 116)]), 'shade', 'b', False)]
            + [strand([(x, 10), (x, 112)], 'deep', 'b', 1.0) for x in (34, 50, 66)],
}

# Bill Tardy (portero): piel tostada; pelo salmón corto de cepillo, plano arriba y con un pico delante, y cejas del mismo
# color; párpados caídos, nariz grande y una sonrisa de raya larga; barbilla alargada
CHARS[K + 'bill-tardy'] = {
    'body': 'normal', 'pal': pal('#d06c66', SK_T, iris='#1e1a1c', shade='#a8524e', deep='#7c3c38'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'none', 'nose': (50, 86, 4.0),
             'hairline': [(14, 58), (18, 46), (34, 42), (50, 42), (66, 42), (82, 46), (86, 58)]},
    'front': [L(outline([(16, 60), (12, 32), (14, 14), (8, 4, 1), (30, 10), (70, 8), (86, 12), (88, 32), (84, 60), (80, 48), (20, 48)])),
              L(outline([(60, 9), (86, 12), (88, 32), (84, 58), (78, 34)]), 'shade', 'b', False),
              strand([(30, 8), (32, 30)], 'deep', 'b', 1.0), strand([(50, 6), (50, 30)], 'deep', 'b', 1.0), strand([(70, 6), (68, 30)], 'deep', 'b', 1.0),
              L([(28, 72), (44, 72)], OUTC, 'f', False, False, 2.0), L([(56, 72), (72, 72)], OUTC, 'f', False, False, 2.0),
              L(quad((34, 96), (50, 99), (66, 95)), (130, 70, 50, 255), 'f', False, False, 1.6)]
             + brows(63, 'mid', 3.2, 14, 0.0, 11),
    'side': [L(outline([(74, 46), (84, 40), (88, 20), (98, 4, 1), (74, 6), (50, 4), (26, 6), (10, 16), (4, 44), (8, 70), (20, 82), (34, 80), (38, 64), (46, 56), (60, 50)])),
             L(outline([(4, 42), (28, 44), (38, 62), (34, 80), (20, 82), (8, 70)]), 'shade', 'b', False),
             L([(76, 72), (85, 72)], OUTC, 'f', False, False, 2.0)] + brow_side(63, 'mid', 3.2),
    'back': [L(outline([(16, 78), (12, 32), (14, 14), (50, 10), (86, 12), (88, 32), (84, 78), (66, 86), (50, 88), (34, 86)])),
             L(outline([(60, 6), (88, 6), (88, 30), (84, 78), (66, 84), (66, 40)]), 'shade', 'b', False)],
}

# Bill Teller: pelo gris violáceo con raya en medio, en mechones largos que le caen hasta la mandíbula con las puntas
# hacia fuera; ojos marrones afilados, cejas enfadadas y boca seria
CHARS[K + 'bill-teller'] = {
    'body': 'normal', 'pal': pal('#7c6c86', SK_L, iris='#8a6020', shade='#5e5068', deep='#443a4c'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(6, 94, 1), (6, 70), (8, 40), (18, 16), (36, 4), (50, 6), (64, 4), (82, 16), (92, 40), (94, 70), (94, 94, 1), (84, 80), (82, 58), (18, 58),
                         (16, 80)])),
              L(outline([(60, 4), (82, 16), (92, 40), (94, 70), (92, 92), (84, 70), (80, 30)]), 'shade', 'b', False),
              L(outline([(16, 60), (18, 40), (30, 28), (48, 22), (50, 30), (52, 22), (70, 28), (82, 40), (84, 60), (78, 48), (70, 58, 1), (64, 44), (56, 52, 1), (50, 36),
                         (44, 52, 1), (36, 44), (30, 58, 1), (22, 48)]), 'mid', 'f'),
              strand([(50, 8), (50, 30)], 'deep', 'f', 1.0)],
    'side': [L(outline([(80, 50), (88, 40), (90, 24), (76, 6), (50, -2), (24, 4), (6, 22), (0, 50), (2, 80), (6, 96, 1), (16, 84), (26, 96, 1), (34, 80), (38, 66),
                        (48, 58), (64, 54)])),
             L(outline([(2, 46), (30, 50), (38, 66), (32, 86), (16, 86), (6, 84)]), 'shade', 'b', False),
             L(outline([(78, 48), (92, 50), (94, 68, 1), (84, 58)]), 'mid', 'f')],
    'back': [L(outline([(6, 94, 1), (6, 70), (8, 40), (18, 16), (36, 4), (50, 2), (64, 4), (82, 16), (92, 40), (94, 70), (94, 94, 1), (78, 86), (64, 96, 1),
                        (50, 86), (36, 96, 1), (22, 86)])),
             L(outline([(60, 4), (82, 16), (92, 40), (94, 70), (92, 92), (76, 86), (70, 40)]), 'shade', 'b', False)]
            + [strand([(x, 8), (x, 84)], 'deep', 'b', 1.0) for x in (34, 50, 66)],
}

# Bill Wordsworthy: melena naranja en forma de seta, con flequillo de mechones y las puntas que se abren en picos a la
# altura de las orejas; gafas redondas negras y sonrisa
CHARS[K + 'bill-wordsy-wordsworthy'] = {
    'body': 'normal', 'pal': pal('#d87428', SK_L, iris='#2a2020', shade='#b05a1c', deep='#844214'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(0, 76, 1), (8, 58), (8, 34), (18, 12), (38, 0), (62, 0), (82, 12), (92, 34), (92, 58), (100, 76, 1), (86, 68), (84, 62), (16, 62), (14, 68)])),
              L(outline([(60, 2), (82, 12), (92, 36), (92, 58), (98, 74), (86, 66), (80, 30)]), 'shade', 'b', False)]
             + ring_glasses('front', 77, (30, 26, 26, 255), 2.6, 9.5, 7.5, 14)
             + [L(outline([(16, 64), (16, 40), (28, 26), (50, 20), (72, 26), (84, 40), (84, 64), (76, 58), (70, 64, 1), (62, 54), (50, 62, 1), (40, 54), (30, 64, 1), (24, 56)]),
                  'mid', 'f'),
                strand([(36, 26), (40, 50)], 'shade', 'f', 1.0), strand([(62, 26), (60, 50)], 'shade', 'f', 1.0)],
    'side': [L(outline([(80, 52), (88, 42), (90, 26), (76, 6), (50, -2), (24, 4), (6, 22), (2, 50), (-4, 74, 1), (10, 68), (20, 80, 1), (30, 70), (38, 66), (48, 60),
                        (64, 56)])),
             L(outline([(2, 46), (30, 50), (38, 64), (20, 78), (8, 68)]), 'shade', 'b', False),
             L(outline([(78, 50), (92, 52), (92, 66, 1), (84, 60)]), 'mid', 'f')]
            + ring_glasses('side', 77, (30, 26, 26, 255), 2.6, 5, 7.5),
    'back': [L(outline([(0, 76, 1), (8, 58), (8, 34), (18, 12), (38, 0), (62, 0), (82, 12), (92, 34), (92, 58), (100, 76, 1), (80, 74), (66, 82, 1), (50, 76),
                        (34, 82, 1), (20, 74)])),
             L(outline([(60, 2), (82, 12), (92, 36), (92, 58), (98, 74), (78, 74), (70, 40)]), 'shade', 'b', False)]
            + [strand([(x, 6), (x, 74)], 'deep', 'b', 1.0) for x in (34, 50, 66)],
}

# Bill Yards (portero): melena verde lisa por la mandíbula con raya en medio, en cortinas que le enmarcan la frente;
# cejas verdes gruesas y enfadadas, ojos negros y media sonrisa
CHARS[K + 'bill-yards'] = {
    'body': 'normal', 'pal': pal('#3e9a5c', SK_L, iris='#1e1a1c', shade='#2e7646', deep='#1e5432'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(8, 102, 1), (6, 60), (12, 24), (30, 6), (50, 2), (70, 6), (88, 24), (94, 60), (92, 102, 1), (84, 96), (82, 64), (18, 64), (16, 96)])),
              L(outline([(60, 4), (88, 24), (94, 60), (92, 100), (84, 80), (80, 30)]), 'shade', 'b', False),
              L(outline([(18, 66), (20, 40), (36, 28), (50, 26), (64, 28), (80, 40), (82, 66), (74, 50), (50, 44), (26, 50)]), 'mid', 'f'),
              L(outline([(42, 28), (50, 26), (58, 28), (54, 44), (46, 44)]), 'deep', 'f', False),
              strand([(30, 34), (24, 56)], 'shade', 'f', 1.0), strand([(70, 34), (76, 56)], 'shade', 'f', 1.0)]
             + brows(66, 'deep', 4.0, 14, 1.2, 12),
    'side': [L(outline([(80, 50), (88, 40), (90, 24), (76, 6), (50, -2), (24, 4), (6, 22), (0, 50), (2, 84), (8, 104, 1), (34, 98), (36, 70), (44, 60), (64, 54)])),
             L(outline([(2, 46), (30, 50), (34, 96), (10, 100)]), 'shade', 'b', False),
             L(outline([(76, 48), (90, 52), (88, 70, 1), (80, 58)]), 'mid', 'f')] + brow_side(66, 'deep', 4.0, 1.2),
    'back': [L(outline([(8, 102, 1), (6, 60), (12, 24), (30, 6), (50, 2), (70, 6), (88, 24), (94, 60), (92, 102, 1), (50, 98)])),
             L(outline([(60, 4), (88, 24), (94, 60), (92, 100), (64, 98)]), 'shade', 'b', False),
             strand([(50, 4), (50, 96)], 'deep', 'b', 1.0)],
}

# Billy Blanc: pelo rosa en forma de casco redondo con un flequillo largo y abombado echado hacia la derecha de la imagen;
# gafas finas doradas, ojos gris azulado y sonrisa de dientes
CHARS[K + 'billy-blanc'] = {
    'body': 'normal', 'pal': pal('#c86872', SK_L, iris='#7a9cb0', shade='#a04e5a', deep='#783a44'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'grin', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(10, 82), (6, 50), (12, 22), (32, 4), (50, 0), (68, 4), (88, 22), (94, 50), (90, 82), (84, 76), (82, 60), (18, 60), (16, 76)])),
              L(outline([(60, 2), (88, 22), (94, 50), (90, 80), (84, 70), (80, 30)]), 'shade', 'b', False)]
             + rect_glasses('front', 77, (176, 150, 90, 255))
             + [L(outline([(16, 64), (16, 40), (28, 22), (50, 16), (72, 22), (86, 40), (88, 68, 1), (80, 62), (70, 60), (56, 54), (40, 56), (28, 60), (20, 62)]), 'mid', 'f'),
                L(outline([(56, 20), (76, 26), (86, 44), (86, 62), (74, 56), (68, 40)]), 'shade', 'f', False),
                strand([(32, 30), (50, 40), (64, 54)], 'shade', 'f', 1.0)],
    'side': [L(outline([(82, 54), (92, 46), (94, 28), (78, 6), (50, -2), (24, 4), (6, 22), (2, 50), (6, 76), (18, 86), (34, 84), (38, 68), (48, 60), (66, 58)])),
             L(outline([(4, 46), (30, 50), (38, 66), (34, 84), (18, 86), (6, 76)]), 'shade', 'b', False)]
            + rect_glasses('side', 77, (176, 150, 90, 255)),
    'back': [L(outline([(10, 82), (6, 50), (12, 22), (32, 4), (50, 0), (68, 4), (88, 22), (94, 50), (90, 82), (66, 90), (50, 92), (34, 90)])),
             L(outline([(60, 2), (88, 22), (94, 50), (90, 82), (66, 88), (70, 40)]), 'shade', 'b', False)]
            + [strand([(x, 8), (x, 88)], 'deep', 'b', 1.0) for x in (36, 50, 64)],
}

# Billy Nomates (portero): pelo azul marino casi negro, una mata enorme de pinchos que salen hacia todos lados, con el
# flequillo en picos sobre la frente; ojos afilados enfadados y boca seria
CHARS[K + 'billy-nomates'] = {
    'body': 'normal', 'pal': pal('#2e2a48', SK_L, iris='#1e1a1c', shade='#221f38', deep='#16142a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(16, 70), (-6, 66, 1), (8, 56), (-8, 40, 1), (8, 34), (-2, 16, 1), (16, 16), (12, -2, 1), (28, 6), (32, -12, 1), (44, 2), (54, -14, 1),
                         (60, 2), (74, -8, 1), (74, 8), (92, 2, 1), (86, 18), (104, 22, 1), (92, 34), (108, 44, 1), (92, 54), (106, 68, 1), (84, 70), (82, 60),
                         (18, 60)])),
              L(outline([(60, 2), (74, -8), (74, 8), (92, 2), (86, 18), (104, 22), (92, 34), (108, 44), (92, 54), (104, 66), (84, 64), (80, 30)]), 'shade', 'b', False),
              L(outline([(16, 62), (20, 44), (34, 34), (50, 30), (66, 34), (80, 44), (84, 62), (74, 52), (68, 62, 1), (60, 50), (50, 60, 1), (40, 50), (32, 62, 1),
                         (26, 52)]), 'mid', 'f')],
    'side': [L(outline([(80, 50), (88, 42), (102, 40, 1), (90, 30), (100, 14, 1), (82, 14), (80, -6, 1), (64, 4), (52, -14, 1), (40, 2), (22, -10, 1), (20, 10),
                        (0, 6, 1), (8, 26), (-12, 34, 1), (4, 46), (-8, 62, 1), (8, 64), (6, 84, 1), (22, 76), (28, 92, 1), (36, 72), (46, 60), (62, 54)])),
             L(outline([(4, 44), (28, 46), (38, 62), (24, 80), (8, 70)]), 'shade', 'b', False),
             L(outline([(78, 50), (92, 52), (94, 68, 1), (84, 60)]), 'mid', 'f')],
    'back': [L(outline([(16, 82), (-6, 72, 1), (8, 60), (-8, 40, 1), (8, 34), (-2, 16, 1), (16, 16), (12, -2, 1), (28, 6), (32, -12, 1), (44, 2), (54, -14, 1),
                        (60, 2), (74, -8, 1), (74, 8), (92, 2, 1), (86, 18), (104, 22, 1), (92, 34), (108, 44, 1), (92, 60), (106, 74, 1), (84, 82), (72, 94, 1),
                        (64, 84), (52, 96, 1), (44, 84), (32, 94, 1), (28, 84)])),
             L(outline([(60, 4), (74, -8), (74, 8), (92, 2), (86, 18), (104, 22), (92, 34), (108, 44), (92, 60), (104, 72), (84, 80), (70, 40)]), 'shade', 'b', False)],
}

# Biron Pendexter: pelo castaño oliva recogido en lo alto en un moño revuelto con goma verde, y un flequillo rubio claro en
# forma de estrella sobre la frente; ojazos negros redondos y sonrisa
CHARS[K + 'biron-pendexter'] = {
    'body': 'bajito', 'pal': pal('#8c7838', SK_L, iris='#1e1a1c', shade='#6c5c2a', deep='#4c401c', tie='#7ab04a', blond='#ecd488', blond_d='#c8ac5c'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': [(14, 62), (18, 46), (34, 40), (50, 38), (66, 40), (82, 46), (86, 62)]},
    'front': [L(outline([(38, 10), (30, -8, 1), (42, -4), (46, -20, 1), (54, -6), (66, -16, 1), (64, -2), (76, -6, 1), (66, 10)])),
              L(ell(52, 8, 8, 3.4), 'tie', 'b', ln=True),
              L(outline([(16, 64), (12, 40), (20, 18), (50, 8), (80, 18), (88, 40), (84, 64), (80, 50), (20, 50)])),
              L(outline([(60, 10), (80, 18), (88, 40), (84, 62), (76, 36)]), 'shade', 'b', False),
              L(outline([(50, 26), (54, 38), (68, 34, 1), (58, 44), (64, 56, 1), (52, 48), (44, 60, 1), (44, 46), (30, 48, 1), (40, 38), (32, 28, 1), (46, 34)]), 'blond', 'f',
                ln=True),
              L([(20, 86), (24, 85)], (190, 120, 90, 255), 'f', False, False, 1.0), L([(20, 89), (24, 88)], (190, 120, 90, 255), 'f', False, False, 1.0)],
    'side': [L(outline([(40, 8), (36, -10, 1), (46, -4), (52, -18, 1), (58, -2), (66, -10, 1), (62, 8)])),
             L(ell(50, 6, 6, 3.4), 'tie', 'b', ln=True),
             L(outline([(76, 46), (84, 32), (80, 14), (56, 4), (30, 8), (10, 22), (4, 46), (8, 70), (20, 84), (34, 82), (38, 64), (48, 56), (62, 50)])),
             L(outline([(4, 42), (30, 46), (40, 60), (34, 82), (20, 84), (8, 70)]), 'shade', 'b', False),
             L(outline([(76, 40), (88, 44), (92, 56, 1), (82, 52)]), 'blond', 'f', ln=True)],
    'back': [L(outline([(38, 10), (30, -8, 1), (42, -4), (46, -20, 1), (54, -6), (66, -16, 1), (64, -2), (76, -6, 1), (66, 10)])),
             L(ell(52, 8, 8, 3.4), 'tie', 'b', ln=True),
             L(outline([(16, 74), (12, 40), (20, 18), (50, 8), (80, 18), (88, 40), (84, 74), (66, 86), (50, 88), (34, 86)])),
             L(outline([(58, 12), (80, 18), (88, 42), (84, 74), (66, 84), (64, 40)]), 'shade', 'b', False)]
            + [strand([(x, 80), (50, 14)], 'shade', 'b', 1.0) for x in (30, 50, 70)],
}

# Bo Ling: pelo castaño en capas por la mandíbula, con un flequillo largo de lado que le tapa el ojo izquierdo; ojos
# afilados y sonrisa de lado
CHARS[K + 'bo-ling'] = {
    'body': 'normal', 'pal': pal('#8a6c3c', SK_L, iris='#2a2020', shade='#6c522c', deep='#4c3a1e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(10, 94, 1), (6, 70), (6, 40), (16, 14), (36, 2), (50, 0), (66, 2), (86, 14), (96, 40), (96, 70), (96, 94, 1), (86, 84), (82, 60), (18, 60),
                         (16, 84)])),
              L(outline([(60, 2), (86, 14), (96, 40), (96, 70), (94, 92), (84, 70), (80, 30)]), 'shade', 'b', False),
              L(outline([(16, 60), (18, 40), (32, 24), (52, 18), (74, 24), (88, 42), (90, 76, 1), (82, 64), (74, 82, 1), (66, 62), (58, 68, 1), (52, 54), (40, 56), (28, 58),
                         (22, 50)]), 'mid', 'f'),
              strand([(46, 22), (62, 40), (72, 70)], 'shade', 'f', 1.0), strand([(30, 30), (36, 48)], 'shade', 'f', 1.0)],
    'side': [L(outline([(80, 48), (88, 40), (90, 24), (76, 6), (50, -2), (24, 4), (6, 22), (0, 50), (2, 80), (6, 96, 1), (16, 86), (26, 96, 1), (34, 80), (38, 66),
                        (48, 58), (64, 54)])),
             L(outline([(2, 46), (30, 50), (38, 66), (32, 86), (16, 88), (6, 84)]), 'shade', 'b', False),
             L(outline([(76, 46), (92, 48), (94, 72, 1), (84, 58)]), 'mid', 'f')],
    'back': [L(outline([(10, 94, 1), (6, 70), (6, 40), (16, 14), (36, 2), (50, 0), (66, 2), (86, 14), (96, 40), (96, 70), (96, 94, 1), (80, 88), (66, 96, 1),
                        (52, 88), (38, 96, 1), (24, 88)])),
             L(outline([(60, 2), (86, 14), (96, 40), (96, 70), (94, 92), (78, 88), (70, 40)]), 'shade', 'b', False)]
            + [strand([(x, 8), (x, 86)], 'deep', 'b', 1.0) for x in (34, 50, 66)],
}

# Bo Luger: grandote calvo de piel tostada, con un mechón amarillo en forma de flor de pétalos en punta en la coronilla;
# dos manchas verde azulado alrededor de los ojos, orejas grandes y unos morros gruesos
CHARS[K + 'bo-luger'] = {
    'body': 'corpulento', 'pal': pal('#e8c020', SK_T, iris='#1e1a1c', shade='#c09c14', deep='#8a700e', patch='#5e8c84', lip='#c86a48'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'none', 'hairline': False, 'face_front': blob([(14, 60), (15, 34), (28, 14), (50, 6), (72, 14), (85, 34), (88, 62),
                                                                                                      (88, 92), (68, 108), (50, 110), (32, 108), (12, 92)]),
             'big_ears': 3, 'ear_out': 3},
    'front': [L(ell(37, 76, 9, 7.5), 'patch', 'f', ln=True), L(ell(63, 76, 9, 7.5), 'patch', 'f', ln=True),
              L(ell(37, 76, 2.4, 2.8), OUTC, 'f', False), L(ell(63, 76, 2.4, 2.8), OUTC, 'f', False),
              L([(30, 71), (44, 71)], OUTC, 'f', False, False, 1.6), L([(56, 71), (70, 71)], OUTC, 'f', False, False, 1.6),
              L(rope((38, 95), (50, 99), (62, 95), 6), 'lip', 'f', ln=True),
              L(outline([(50, 28), (44, 16), (36, 20, 1), (42, 10), (36, 0, 1), (46, 4), (50, -6, 1), (54, 4), (64, 0, 1), (58, 10), (64, 20, 1), (56, 16)]), 'mid',
                'f', ln=True),
              L(outline([(48, 28), (50, 44, 1), (53, 28)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(52, 28), (46, 16), (38, 18, 1), (44, 10), (40, 0, 1), (50, 6), (56, -4, 1), (58, 8), (66, 6, 1), (60, 16), (62, 26, 1)]), 'mid', 'f', ln=True),
             L(ell(82, 76, 5, 7), 'patch', 'f', ln=True), L(ell(83, 76, 1.8, 2.6), OUTC, 'f', False),
             L(rope((80, 96), (86, 98), (90, 95), 5), 'lip', 'f', ln=True)],
    'back': [L(outline([(50, 28), (44, 16), (36, 20, 1), (42, 10), (36, 0, 1), (46, 4), (50, -6, 1), (54, 4), (64, 0, 1), (58, 10), (64, 20, 1), (56, 16)]), 'mid',
               'f', ln=True)],
}

# Bob Baggum (portero): piel tostada; rastas gruesas verde oliva oscuro que se levantan en rollos hacia arriba y a los
# lados, sujetas con una cinta blanca en la frente; cejas gruesas, nariz grande con pecas y sonrisa ancha
CHARS[K + 'bob-baggum'] = {
    'body': 'corpulento', 'pal': pal('#5a5a2c', SK_T, iris='#1e1a1c', shade='#44441e', deep='#303014', band='#ece4d2'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'none', 'hairline': False, 'face_front': CHUBBY, 'nose': (50, 86, 4.6)},
    'front': [L(outline([(14, 54), (12, 36), (24, 18), (50, 12), (76, 18), (88, 36), (86, 54)]))]
             + [L(rope(a, c, b, 9), 'mid', 'b', ln=True) for a, c, b in (((20, 30), (2, 26), (-2, 44)), ((26, 20), (10, 4), (4, 16)), ((36, 14), (28, -8), (20, -6)),
                                                                          ((50, 12), (50, -12), (40, -16)), ((62, 14), (70, -8), (78, -6)), ((74, 20), (90, 4), (96, 16)),
                                                                          ((80, 30), (98, 26), (102, 44)))]
             + [band(42, 52, 'band', 'f', 6)] + brows(64, 'deep', 4.6, 15, 0.6, 13)
             + [L(quad((28, 94), (50, 104), (72, 94)), (130, 70, 50, 255), 'f', False, False, 1.8)]
             + [L(ell(x, y, 0.9, 0.9), FRECKLE, 'f', False) for x, y in ((42, 90), (45, 93), (55, 93), (58, 90))],
    'side': [L(outline([(80, 48), (84, 30), (70, 14), (40, 10), (14, 22), (6, 46), (10, 70), (24, 80), (38, 70), (46, 56), (62, 50)]))]
            + [L(rope(a, c, b, 9), 'mid', 'b', ln=True) for a, c, b in (((70, 24), (90, 14), (100, 26)), ((56, 14), (64, -8), (76, -10)), ((40, 12), (36, -12), (24, -12)),
                                                                         ((24, 18), (6, 0), (-4, 8)), ((14, 34), (-4, 30), (-8, 48)), ((14, 52), (-2, 60), (0, 76)))]
            + [band_side(42, 51)] + brow_side(64, 'deep', 4.6, 0.6),
    'back': [L(outline([(14, 70), (12, 36), (24, 18), (50, 12), (76, 18), (88, 36), (86, 70), (50, 76)]))]
            + [L(rope(a, c, b, 9), 'mid', 'b', ln=True) for a, c, b in (((20, 30), (2, 26), (-2, 44)), ((26, 20), (10, 4), (4, 16)), ((36, 14), (28, -8), (20, -6)),
                                                                         ((50, 12), (50, -12), (60, -16)), ((62, 14), (70, -8), (78, -6)), ((74, 20), (90, 4), (96, 16)),
                                                                         ((80, 30), (98, 26), (102, 44)), ((22, 50), (6, 60), (8, 76)), ((78, 50), (94, 60), (92, 76)),
                                                                         ((40, 50), (36, 70), (42, 84)), ((60, 50), (64, 70), (58, 84)))]
            + [band_back(44, 53)],
}

# Bob Dingnagian: chicarrón de cara redonda; pelo gris pardo peinado hacia atrás, con un rizo suelto que le cae por la
# frente; cejas gruesas grises, ojillos de punto, nariz redonda y una sonrisa larga
CHARS[K + 'bob-dingy-dingnagian'] = {
    'body': 'corpulento', 'pal': pal('#9a8c74', SK_L, iris='#1e1a1c', shade='#7a6e5a', deep='#5a5042', brow='#8a8270'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'none', 'face_front': CHUBBY, 'nose': (50, 85, 3.0),
             'hairline': [(10, 62), (14, 48), (30, 42), (50, 40), (70, 42), (86, 48), (90, 62)]},
    'front': [L(outline([(10, 64), (8, 40), (18, 16), (50, 4), (82, 16), (92, 40), (90, 64), (84, 50), (16, 50)])),
              L(outline([(60, 6), (82, 16), (92, 40), (90, 62), (80, 34)]), 'shade', 'b', False)]
             + [strand([(x, 42), (x * 0.9 + 5, 10)], 'deep', 'b', 1.0) for x in (26, 40, 54, 68, 80)]
             + [L(rope((30, 42), (16, 46), (24, 56), 5), 'mid', 'f', ln=True)]
             + brows(64, 'brow', 5.0, 15, 0.4, 14)
             + [L(quad((28, 95), (50, 103), (72, 93)), (130, 70, 50, 255), 'f', False, False, 1.8), L([(16, 82), (21, 82)], OUTC, 'f', False, False, 1.0),
                L([(16, 85), (21, 85)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(80, 46), (86, 32), (80, 12), (56, 2), (28, 6), (8, 22), (2, 46), (8, 70), (20, 82), (34, 80), (38, 64), (48, 56), (64, 50)])),
             L(outline([(2, 44), (30, 48), (40, 62), (34, 80), (20, 82), (8, 70)]), 'shade', 'b', False),
             strand([(82, 36), (40, 10)], 'deep', 'b', 1.0), strand([(74, 46), (20, 24)], 'deep', 'b', 1.0)] + brow_side(64, 'brow', 5.0, 0.4),
    'back': [L(outline([(10, 76), (8, 40), (18, 16), (50, 4), (82, 16), (92, 40), (90, 76), (66, 86), (50, 88), (34, 86)])),
             L(outline([(58, 8), (82, 16), (92, 42), (90, 76), (66, 84), (66, 40)]), 'shade', 'b', False)]
            + [strand([(x, 8), (x, 84)], 'deep', 'b', 1.0) for x in (34, 50, 66)],
}

# Bob Lioteck (portero): piel tostada y cara redonda; melena rubio platino lisa por la mandíbula, con un flequillo largo
# echado de lado que le tapa media frente y las puntas hacia fuera; ojos gris azulado afilados y sonrisa
CHARS[K + 'bob-lioteck'] = {
    'body': 'corpulento', 'pal': pal('#ecd8a8', SK_T, iris='#7a9aa8', shade='#cab688', deep='#a8946a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False, 'face_front': CHUBBY},
    'front': [L(outline([(6, 96, 1), (4, 70), (6, 40), (16, 14), (36, 2), (50, 0), (66, 2), (86, 14), (96, 40), (98, 70), (100, 96, 1), (88, 84), (84, 60), (16, 60),
                         (14, 84)])),
              L(outline([(60, 2), (86, 14), (96, 40), (98, 70), (98, 94), (86, 70), (80, 30)]), 'shade', 'b', False),
              L(outline([(14, 74, 1), (14, 40), (28, 22), (52, 16), (74, 22), (86, 38), (86, 62), (78, 52), (66, 50), (52, 54), (40, 60), (30, 66), (22, 68)]), 'mid', 'f'),
              strand([(30, 30), (24, 60)], 'shade', 'f', 1.0), strand([(50, 22), (60, 46)], 'shade', 'f', 1.0)],
    'side': [L(outline([(80, 48), (88, 40), (90, 24), (76, 6), (50, -2), (24, 4), (6, 22), (0, 50), (2, 80), (8, 98, 1), (18, 88), (28, 98, 1), (34, 80), (38, 66),
                        (48, 58), (64, 54)])),
             L(outline([(2, 46), (30, 50), (38, 66), (32, 86), (18, 90), (6, 84)]), 'shade', 'b', False),
             L(outline([(76, 46), (92, 48), (92, 64, 1), (84, 56)]), 'mid', 'f')],
    'back': [L(outline([(6, 96, 1), (4, 70), (6, 40), (16, 14), (36, 2), (50, 0), (66, 2), (86, 14), (96, 40), (98, 70), (100, 96, 1), (80, 90), (66, 98, 1),
                        (52, 90), (38, 98, 1), (22, 90)])),
             L(outline([(60, 2), (86, 14), (96, 40), (98, 70), (98, 94), (78, 90), (70, 40)]), 'shade', 'b', False)]
            + [strand([(x, 8), (x, 88)], 'deep', 'b', 1.0) for x in (34, 50, 66)],
}

# Bob Shishker: cabeza rapada con un moñito marrón redondo y tieso en lo alto, como un cepillo; una sola ceja enorme y
# gruesa verde oliva, ojos caídos, orejas grandes y boca de enfado
CHARS[K + 'bob-shishker'] = {
    'body': 'normal', 'pal': pal('#9c7a42', SK_L, iris='#1e1a1c', shade='#7a5e30', deep='#5a4422', brow='#7a7442', brow_d='#5a5630'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'frown', 'mouth_y': 95, 'hairline': False, 'face_front': BALD, 'big_ears': 2, 'nose': (50, 86, 3.0)},
    'front': [L(outline([(34, 22), (32, 8), (40, -4), (50, -8), (60, -4), (68, 8), (66, 22), (50, 26)]), 'mid', 'f', ln=True),
              L(outline([(56, -4), (68, 8), (66, 22), (56, 24)]), 'shade', 'f', False),
              strand([(42, 2), (44, 18)], 'deep', 'f', 1.0), strand([(56, 2), (54, 18)], 'deep', 'f', 1.0),
              L(outline([(22, 66), (50, 60), (78, 66), (78, 72), (50, 67), (22, 72)]), 'brow', 'f', ln=True),
              L([(30, 79), (44, 79)], OUTC, 'f', False, False, 1.6), L([(56, 79), (70, 79)], OUTC, 'f', False, False, 1.6)],
    'side': [L(outline([(38, 20), (36, 6), (46, -6), (58, -4), (66, 8), (64, 22), (50, 24)]), 'mid', 'f', ln=True),
             L(outline([(70, 64), (86, 64), (86, 70), (70, 70)]), 'brow', 'f', ln=True)],
    'back': [L(outline([(34, 22), (32, 8), (40, -4), (50, -8), (60, -4), (68, 8), (66, 22), (50, 26)]), 'mid', 'f', ln=True),
             L(outline([(56, -4), (68, 8), (66, 22), (56, 24)]), 'shade', 'f', False)],
}

# Bob Stretcher: pelo verde muy oscuro en pinchos cortos de punta, con el flequillo en picos y patillas en punta; ojos
# azules afilados y enfadados, nariz naranja redonda y sonrisa
CHARS[K + 'bob-stretcher'] = {
    'body': 'normal', 'pal': pal('#24543c', SK_L, iris='#7aa8c0', shade='#1a3e2c', deep='#102a1e', nose='#e8803a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False, 'nose': (50, 86, 3.4)},
    'front': [L(outline([(16, 66), (12, 44), (4, 34, 1), (14, 26), (8, 10, 1), (24, 12), (24, -4, 1), (36, 6), (46, -10, 1), (54, 4), (66, -8, 1), (68, 8), (84, 0, 1),
                         (80, 16), (96, 18, 1), (86, 30), (98, 40, 1), (88, 46), (84, 66), (80, 52), (20, 52)])),
              L(outline([(60, 4), (84, 0), (80, 16), (96, 18), (86, 30), (98, 40), (88, 46), (84, 62), (76, 34)]), 'shade', 'b', False),
              L(outline([(14, 82, 1), (16, 66), (20, 66)]), 'mid', 'f'), L(outline(mir([(14, 82, 1), (16, 66), (20, 66)])), 'mid', 'f'),
              L(outline([(16, 60), (20, 44), (34, 34), (50, 30), (66, 34), (80, 44), (84, 60), (76, 52), (70, 62, 1), (62, 50), (52, 60, 1), (44, 50), (34, 62, 1),
                         (28, 52)]), 'mid', 'f')],
    'side': [L(outline([(80, 50), (86, 42), (100, 38, 1), (88, 30), (98, 16, 1), (80, 16), (80, -2, 1), (64, 6), (54, -10, 1), (42, 4), (24, -6, 1), (22, 12),
                        (4, 14, 1), (10, 30), (0, 44, 1), (8, 52), (6, 72), (20, 84), (34, 82), (38, 66), (46, 58), (62, 54)])),
             L(outline([(4, 44), (28, 46), (40, 60), (34, 82), (20, 84), (8, 72)]), 'shade', 'b', False),
             L(outline([(54, 56), (64, 58), (60, 82, 1)]), 'mid', 'b'),
             L(outline([(78, 50), (92, 52), (94, 66, 1), (84, 60)]), 'mid', 'f')],
    'back': [L(outline([(16, 78), (12, 44), (4, 34, 1), (14, 26), (8, 10, 1), (24, 12), (24, -4, 1), (36, 6), (46, -10, 1), (54, 4), (66, -8, 1), (68, 8), (84, 0, 1),
                        (80, 16), (96, 18, 1), (86, 30), (98, 40, 1), (88, 46), (84, 78), (66, 88), (50, 90), (34, 88)])),
             L(outline([(60, 6), (84, 0), (80, 16), (96, 18), (86, 30), (98, 40), (88, 46), (84, 78), (66, 86), (70, 40)]), 'shade', 'b', False)],
}

# Bob Whittle: casco de aviador verde oliva con ribete crema, unas gafas de piloto grises subidas a la frente y orejeras
# redondas grises; flequillo naranja rojizo por debajo; ojazos negros, pecas y boca de enfado
CHARS[K + 'bob-whittle'] = {
    'body': 'normal', 'pal': pal('#d8561e', SK_L, iris='#1e1a1c', shade='#b04416', deep='#843210', helm='#6c7a3a', helm_d='#525e2a', rim='#e8dcc0', goggle='#8a8a8a',
                                 lens='#5a5248', ear='#9a9a9e'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(20, 60), (22, 46), (36, 40), (50, 38), (64, 40), (78, 46), (80, 60), (72, 52), (66, 62, 1), (58, 50), (50, 60, 1), (42, 50), (34, 62, 1),
                         (28, 52)]), 'mid', 'f'),
              L(outline([(8, 76), (6, 40), (16, 14), (50, 0), (84, 14), (94, 40), (92, 76), (82, 66), (80, 50), (66, 42), (50, 40), (34, 42), (20, 50), (18, 66)]), 'helm', 'f',
                ln=True),
              L(outline([(60, 2), (84, 14), (94, 40), (92, 74), (84, 64), (82, 40)]), 'helm_d', 'f', False),
              L(quad((20, 50), (50, 34), (80, 50)), 'rim', 'f', False, False, 2.6),
              L(ell(10, 74, 7, 9), 'ear', 'f', ln=True), L(ell(90, 74, 7, 9), 'ear', 'f', ln=True),
              L(ell(10, 74, 3.4, 4.6), 'goggle', 'f', ln=True), L(ell(90, 74, 3.4, 4.6), 'goggle', 'f', ln=True),
              L(outline([(18, 30), (20, 14), (46, 12), (48, 30)]), 'goggle', 'f', ln=True), L(outline(mir([(18, 30), (20, 14), (46, 12), (48, 30)])), 'goggle', 'f', ln=True),
              L(outline([(23, 27), (24, 17), (43, 16), (44, 27)]), 'lens', 'f', False), L(outline(mir([(23, 27), (24, 17), (43, 16), (44, 27)])), 'lens', 'f', False)]
             + freckles(86),
    'side': [L(outline([(78, 52), (92, 54), (92, 68, 1), (84, 60)]), 'mid', 'f'),
             L(outline([(78, 50), (86, 34), (78, 12), (54, 0), (26, 4), (8, 20), (2, 48), (8, 76), (26, 84), (40, 78), (42, 60), (60, 52)]), 'helm', 'f', ln=True),
             L(outline([(4, 46), (40, 50), (40, 78), (26, 84), (8, 76)]), 'helm_d', 'f', False),
             L(ell(46, 72, 7, 9), 'ear', 'f', ln=True), L(ell(46, 72, 3.4, 4.6), 'goggle', 'f', ln=True),
             L(outline([(62, 26), (64, 10), (86, 14), (88, 30)]), 'goggle', 'f', ln=True), L(outline([(67, 24), (68, 15), (83, 18), (84, 26)]), 'lens', 'f', False),
             L(quad((48, 22), (56, 12), (64, 14)), 'goggle', 'f', False, False, 2.4)],
    'back': [L(outline([(8, 80), (6, 40), (16, 14), (50, 0), (84, 14), (94, 40), (92, 80), (66, 90), (50, 92), (34, 90)]), 'helm', 'f', ln=True),
             L(outline([(60, 2), (84, 14), (94, 40), (92, 80), (66, 88), (66, 40)]), 'helm_d', 'f', False),
             L(quad((8, 80), (50, 96), (92, 80)), 'rim', 'f', False, False, 2.6),
             L(ell(8, 72, 6, 9), 'ear', 'f', ln=True), L(ell(92, 72, 6, 9), 'ear', 'f', ln=True),
             L(quad((10, 26), (50, 14), (90, 26)), 'goggle', 'f', False, False, 3.0)],
}

# Bobby Constable: piel morena y cara alargada; cresta morada que le sale en pico desde la frente, con los lados rapados;
# párpados caídos, nariz grande y sonrisa de lado
CHARS[K + 'bobby-constable'] = {
    'body': 'delgado', 'pal': pal('#5a4872', SK_D, iris='#1e1a1c', shade='#44365a', deep='#302640'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'none', 'nose': (50, 85, 3.2),
             'hairline': [(14, 60), (18, 46), (24, 42), (36, 42), (40, 36), (46, 44), (50, 48), (54, 44), (60, 36), (64, 42), (76, 42), (82, 46), (86, 60)]},
    'front': [L(outline([(16, 62), (12, 40), (20, 20), (40, 12), (44, -10), (50, -30, 1), (56, -10), (60, 12), (80, 20), (88, 40), (84, 62), (80, 48), (20, 48)])),
              L(outline([(52, -24), (56, -10), (60, 12), (80, 20), (88, 40), (84, 60), (74, 32), (54, 18)]), 'shade', 'b', False),
              L([(28, 72), (44, 72)], OUTC, 'f', False, False, 2.0), L([(56, 72), (72, 72)], OUTC, 'f', False, False, 2.0),
              L(quad((34, 96), (54, 100), (68, 92)), (110, 60, 40, 255), 'f', False, False, 1.6)],
    'side': [L(outline([(74, 46), (82, 36), (90, 20), (98, 4, 1), (80, 4), (64, -10), (44, -18, 1), (36, -2), (16, 10), (4, 34), (4, 58), (14, 78), (30, 82), (38, 64),
                        (48, 56), (62, 50)])),
             L(outline([(4, 40), (30, 44), (40, 60), (30, 82), (14, 78)]), 'shade', 'b', False),
             L([(76, 72), (85, 72)], OUTC, 'f', False, False, 2.0)],
    'back': [L(outline([(16, 76), (12, 40), (20, 20), (40, 10), (44, -10), (50, -30, 1), (56, -10), (60, 10), (80, 20), (88, 40), (84, 76), (66, 86), (50, 88),
                        (34, 86)])),
             L(outline([(52, -24), (56, -10), (60, 12), (80, 20), (88, 40), (84, 76), (66, 84), (60, 30)]), 'shade', 'b', False)],
}

# Bobby Peel: pelo azul verdoso con mechas oscuras, un flequillo de mechones sobre la frente y un mechón largo que le sale
# del lado derecho de la imagen como un ala; ojazos marrones, cejas enfadadas y boca seria
CHARS[K + 'bobby-peel'] = {
    'body': 'normal', 'pal': pal('#5c9aa8', SK_L, iris='#6a5030', shade='#467884', deep='#2e5460'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(12, 90, 1), (8, 66), (8, 38), (18, 14), (38, 2), (60, 2), (80, 10), (92, 30), (94, 54), (110, 46, 1), (96, 70), (90, 90, 1), (84, 78),
                         (82, 60), (18, 60), (16, 78)])),
              L(outline([(60, 4), (80, 10), (92, 30), (94, 54), (108, 48), (96, 68), (88, 86), (82, 40)]), 'shade', 'b', False),
              L(outline([(16, 62), (18, 40), (30, 24), (50, 18), (70, 24), (84, 40), (84, 62), (76, 50), (70, 60, 1), (62, 46), (54, 58, 1), (48, 44), (38, 56, 1), (32, 44),
                         (24, 58, 1)]), 'mid', 'f'),
              strand([(40, 22), (52, 50)], 'deep', 'f', 1.4), strand([(62, 22), (66, 48)], 'deep', 'f', 1.4), strand([(30, 30), (30, 52)], 'deep', 'f', 1.0)],
    'side': [L(outline([(80, 50), (88, 40), (90, 24), (76, 6), (50, -2), (24, 4), (6, 22), (0, 50), (-14, 56, 1), (2, 70), (6, 90, 1), (18, 84), (34, 80), (38, 66),
                        (48, 58), (64, 54)])),
             L(outline([(2, 46), (30, 50), (38, 66), (32, 82), (16, 86), (4, 70)]), 'shade', 'b', False),
             strand([(60, 2), (40, 30), (30, 60)], 'deep', 'b', 1.4),
             L(outline([(76, 46), (92, 50), (94, 68, 1), (84, 58)]), 'mid', 'f')],
    'back': [L(outline([(12, 90, 1), (8, 66), (8, 38), (18, 14), (38, 2), (60, 2), (80, 10), (92, 30), (94, 54), (110, 46, 1), (96, 70), (90, 90, 1), (72, 84),
                        (50, 88), (30, 84)])),
             L(outline([(60, 4), (80, 10), (92, 30), (94, 54), (108, 48), (96, 68), (88, 86), (70, 40)]), 'shade', 'b', False),
             strand([(36, 6), (32, 80)], 'deep', 'b', 1.4), strand([(60, 6), (64, 80)], 'deep', 'b', 1.4)],
}

# Bobby Yellow (portero): pelo rubio arena en casquete con el flequillo echado de lado; ojos enormes redondos y blancos
# con la pupila diminuta, del susto, y la boca apretada enseñando los dientes
CHARS[K + 'bobby-yeller-yellow'] = {
    'body': 'bajito', 'pal': pal('#c8a862', SK_L, iris='#1e1a1c', shade='#a4884a', deep='#806834'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(10, 80), (6, 48), (12, 20), (32, 4), (50, 0), (68, 4), (88, 20), (94, 48), (90, 80), (84, 74), (82, 58), (18, 58), (16, 74)])),
              L(outline([(60, 2), (88, 20), (94, 48), (90, 78), (84, 68), (80, 30)]), 'shade', 'b', False),
              L(outline([(16, 62), (16, 40), (28, 22), (50, 16), (72, 22), (86, 40), (86, 60), (76, 52), (62, 48), (46, 50), (32, 56), (22, 60)]), 'mid', 'f'),
              strand([(40, 22), (60, 34), (72, 50)], 'shade', 'f', 1.0)]
             + [L(ell(cx, 77, 8.4, 9), OUTC, 'f', False) for cx in (35, 65)] + [L(ell(cx, 77, 7, 7.6), WHITE, 'f', False) for cx in (35, 65)]
             + [L(ell(cx, 77, 2.2, 2.4), OUTC, 'f', False) for cx in (35, 65)],
    'side': [L(outline([(82, 54), (92, 46), (94, 28), (78, 6), (50, -2), (24, 4), (6, 22), (2, 50), (6, 76), (18, 86), (34, 84), (38, 68), (48, 60), (66, 58)])),
             L(outline([(4, 46), (30, 50), (38, 66), (34, 84), (18, 86), (6, 76)]), 'shade', 'b', False),
             L(ell(82, 77, 5.6, 9), OUTC, 'f', False), L(ell(82, 77, 4.4, 7.6), WHITE, 'f', False), L(ell(84, 77, 1.8, 2.4), OUTC, 'f', False)],
    'back': [L(outline([(10, 82), (6, 48), (12, 20), (32, 4), (50, 0), (68, 4), (88, 20), (94, 48), (90, 82), (66, 90), (50, 92), (34, 90)])),
             L(outline([(60, 2), (88, 20), (94, 48), (90, 82), (66, 88), (70, 40)]), 'shade', 'b', False)]
            + [strand([(x, 8), (x, 88)], 'deep', 'b', 1.0) for x in (36, 50, 64)],
}

# Boe Tyer (portero): pelo naranja óxido revuelto en pinchos que le caen por la frente y salen por los lados; cejas
# naranjas, ojillos con pestañas y sonrisa
CHARS[K + 'boe-tyer'] = {
    'body': 'normal', 'pal': pal('#c25620', SK_L, iris='#1e1a1c', shade='#9a4218', deep='#702e10'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    'front': messy('front', amp=16, n=11, seed=7, rx=46, ry=40, cy=40, lo=66)
             + [L(outline([(14, 66), (18, 44), (34, 32), (50, 28), (66, 32), (82, 44), (88, 68, 1), (78, 56), (72, 66, 1), (64, 52), (56, 62, 1), (48, 48), (40, 60, 1),
                           (34, 50), (26, 64, 1), (22, 54)]), 'mid', 'f')]
             + brows(66, 'mid', 3.4, 14, 0.4, 11)
             + [L([(25, 74), (29, 76)], OUTC, 'f', False, False, 1.2), L([(75, 74), (71, 76)], OUTC, 'f', False, False, 1.2)],
    'side': messy('side', amp=16, n=11, seed=7, rx=46, ry=40, cy=40) + [L(outline([(78, 50), (92, 52), (94, 68, 1), (84, 60)]), 'mid', 'f')]
            + brow_side(66, 'mid', 3.4, 0.4),
    'back': messy('back', amp=16, n=11, seed=7, rx=46, ry=40, cy=40),
}

# Bones Size: piel tostada; pelo verde muy oscuro recogido en lo alto en una coleta de pinchos con una goma clara, y dos
# mechones largos que le caen por los lados de la cara; cejas verdes gruesas, ojos afilados y sonrisa con colmillo
CHARS[K + 'bones-size'] = {
    'body': 'normal', 'pal': pal('#24543c', SK_T, iris='#1e1a1c', shade='#1a3e2c', deep='#102a1e', tie='#ece0b8'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': [(14, 60), (18, 46), (34, 40), (50, 38), (66, 40), (82, 46), (86, 60)]},
    'front': [L(outline([(40, 12), (24, 6, 1), (36, 0), (30, -14, 1), (44, -8), (48, -24, 1), (54, -8), (70, -14, 1), (64, 0), (78, 6, 1), (60, 12)])),
              L(ell(50, 8, 8, 3.4), 'tie', 'b', ln=True),
              L(outline([(16, 62), (12, 40), (20, 18), (50, 8), (80, 18), (88, 40), (84, 62), (80, 48), (20, 48)])),
              L(outline([(60, 10), (80, 18), (88, 40), (84, 60), (76, 36)]), 'shade', 'b', False),
              L(outline([(28, 40), (20, 60), (18, 92, 1), (26, 66), (34, 46)]), 'mid', 'f', ln=True),
              L(outline(mir([(28, 40), (20, 60), (18, 92, 1), (26, 66), (34, 46)])), 'mid', 'f', ln=True),
              L(outline([(56, 96), (58, 101, 1), (60, 96)]), WHITE, 'f', ln=True)]
             + brows(66, 'deep', 4.0, 14, 1.4, 12),
    'side': [L(outline([(42, 10), (36, -10, 1), (48, -4), (54, -22, 1), (60, -4), (74, -10, 1), (66, 8)])),
             L(ell(54, 6, 5, 3.4), 'tie', 'b', ln=True),
             L(outline([(76, 46), (84, 32), (80, 14), (56, 4), (30, 8), (10, 22), (4, 46), (8, 70), (20, 84), (34, 82), (38, 64), (48, 56), (62, 50)])),
             L(outline([(4, 42), (30, 46), (40, 60), (34, 82), (20, 84), (8, 70)]), 'shade', 'b', False),
             L(outline([(72, 44), (80, 46), (82, 92, 1), (74, 64)]), 'mid', 'f', ln=True)] + brow_side(66, 'deep', 4.0, 1.4),
    'back': [L(outline([(40, 12), (24, 6, 1), (36, 0), (30, -14, 1), (44, -8), (48, -24, 1), (54, -8), (70, -14, 1), (64, 0), (78, 6, 1), (60, 12)])),
             L(ell(50, 8, 8, 3.4), 'tie', 'b', ln=True),
             L(outline([(16, 74), (12, 40), (20, 18), (50, 8), (80, 18), (88, 40), (84, 74), (66, 86), (50, 88), (34, 86)])),
             L(outline([(58, 12), (80, 18), (88, 42), (84, 74), (66, 84), (64, 40)]), 'shade', 'b', False)]
            + [strand([(x, 80), (50, 14)], 'shade', 'b', 1.0) for x in (30, 50, 70)],
}

# Bos Horne: piel tostada; pelo gris morado corto con pico en la frente y dos cuernos grandes y curvos que le salen de los
# lados de la cabeza; cejas negras gruesas, párpados caídos y sonrisa de lado
CHARS[K + 'bos-horne'] = {
    'body': 'normal', 'pal': pal('#7a6a82', SK_T, iris='#1e1a1c', shade='#5e5066', deep='#443a4a'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'none', 'nose': (50, 86, 3.4),
             'hairline': [(14, 60), (18, 48), (30, 44), (42, 46), (50, 54), (58, 46), (70, 44), (82, 48), (86, 60)]},
    'front': [L(outline([(16, 40), (6, 28), (2, 6), (8, -16, 1), (12, 8), (20, 22), (24, 30)])), L(outline(mir([(16, 40), (6, 28), (2, 6), (8, -16, 1), (12, 8), (20, 22),
                                                                                                             (24, 30)]))),
              L(outline([(16, 62), (12, 40), (20, 18), (50, 10), (80, 18), (88, 40), (84, 62), (80, 50), (20, 50)])),
              L(outline([(60, 12), (80, 18), (88, 40), (84, 60), (76, 36)]), 'shade', 'b', False),
              L([(28, 72), (44, 72)], OUTC, 'f', False, False, 2.0), L([(56, 72), (72, 72)], OUTC, 'f', False, False, 2.0),
              L(quad((34, 96), (52, 99), (66, 93)), (110, 60, 40, 255), 'f', False, False, 1.6)]
             + brows(64, (30, 26, 28, 255), 5.0, 15, 1.2, 14),
    'side': [L(outline([(40, 26), (34, 8), (40, -12), (52, -22, 1), (48, -6), (48, 14), (52, 26)])),
             L(outline([(76, 46), (84, 32), (80, 14), (56, 6), (30, 8), (10, 22), (4, 46), (8, 70), (20, 84), (34, 82), (38, 64), (48, 56), (62, 50)])),
             L(outline([(4, 42), (30, 46), (40, 60), (34, 82), (20, 84), (8, 70)]), 'shade', 'b', False),
             L(outline([(40, 26), (34, 8), (40, -12), (52, -22, 1), (48, -6), (48, 14), (52, 26)]), 'mid', 'f', ln=True),
             L([(76, 72), (85, 72)], OUTC, 'f', False, False, 2.0)] + brow_side(64, (30, 26, 28, 255), 5.0, 1.2),
    'back': [L(outline([(16, 40), (6, 28), (2, 6), (8, -16, 1), (12, 8), (20, 22), (24, 30)])), L(outline(mir([(16, 40), (6, 28), (2, 6), (8, -16, 1), (12, 8), (20, 22),
                                                                                                            (24, 30)]))),
             L(outline([(16, 76), (12, 40), (20, 18), (50, 10), (80, 18), (88, 40), (84, 76), (66, 86), (50, 88), (34, 86)])),
             L(outline([(58, 12), (80, 18), (88, 42), (84, 76), (66, 84), (64, 40)]), 'shade', 'b', False)],
}

# Braden Bakewell: pelo castaño con raya al lado y un tupé que cae en curva hacia la derecha de la imagen, con las puntas
# hacia fuera por encima de las orejas; ojos violeta, nariz larga y sonrisa; cara alargada
CHARS[K + 'braden-bakewell'] = {
    'body': 'delgado', 'pal': pal('#8a6c3e', SK_L, iris='#8a80b0', shade='#6c532e', deep='#4c3a20'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'nose': (50, 85, 2.6),
             'hairline': [(10, 66), (14, 56), (26, 48), (40, 44), (50, 46), (62, 52), (74, 58), (84, 60), (90, 66)]},
    'front': [L(outline([(4, 74, 1), (12, 62), (10, 40), (18, 16), (38, 2), (60, 2), (80, 12), (92, 34), (92, 60), (100, 74, 1), (86, 70), (82, 64), (18, 64), (14, 70)])),
              L(outline([(60, 4), (80, 12), (92, 36), (92, 58), (98, 72), (86, 66), (80, 30)]), 'shade', 'b', False),
              L(outline([(34, 44), (50, 30), (70, 34), (86, 50), (88, 66, 1), (76, 58), (62, 52), (48, 46)]), 'mid', 'f', ln=True),
              strand([(30, 40), (34, 14)], 'deep', 'b', 1.0), strand([(56, 34), (74, 46)], 'shade', 'f', 1.0)],
    'side': [L(outline([(84, 50), (94, 46), (94, 30), (78, 8), (50, -2), (24, 4), (6, 22), (2, 50), (-4, 72, 1), (12, 66), (24, 82), (36, 80), (38, 66), (48, 58),
                        (66, 54)])),
             L(outline([(2, 46), (30, 50), (38, 64), (24, 80), (10, 70)]), 'shade', 'b', False)],
    'back': [L(outline([(4, 78, 1), (12, 64), (10, 40), (18, 16), (38, 2), (60, 2), (80, 12), (92, 34), (92, 62), (100, 78, 1), (80, 80), (66, 88), (50, 90), (34, 88),
                        (20, 80)])),
             L(outline([(60, 4), (80, 12), (92, 36), (92, 62), (98, 76), (78, 80), (70, 40)]), 'shade', 'b', False)]
            + [strand([(x, 8), (x, 84)], 'deep', 'b', 1.0) for x in (34, 50, 66)],
}

# Bramley Cox: cara ancha pintada de blanco con dos coloretes naranjas; pelo verde oscuro liso en casco, con un flequillo
# recto abierto en el centro, un mechón largo que le cae por un lado y un moñito amarillo detrás; ojos afilados con
# pestañas y sonrisita
CHARS[K + 'bramley-cox'] = {
    'body': 'normal', 'pal': pal('#1e6a4a', '#ece2d4', iris='#1e1a1c', shade='#165238', deep='#0e3a28', bun='#e0b040', blush='#e0782a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False, 'face_front': WIDE, 'nose': (50, 86, 2.4)},
    'front': [L(ell(50, -4, 10, 6), 'bun', 'b', ln=True),
              L(outline([(8, 76), (4, 44), (12, 16), (32, 0), (50, -4), (68, 0), (88, 16), (96, 44), (92, 76), (84, 70), (82, 58), (18, 58), (16, 70)])),
              L(outline([(60, -2), (88, 16), (96, 44), (92, 74), (84, 64), (80, 30)]), 'shade', 'b', False),
              L(outline([(14, 62), (14, 38), (26, 20), (50, 14), (74, 20), (86, 38), (86, 62), (56, 56), (52, 64, 1), (48, 56), (14, 62)]), 'mid', 'f'),
              L(outline([(16, 58), (12, 90), (20, 106, 1), (22, 84), (24, 60)]), 'mid', 'f', ln=True)]
             + [strand([(x, 22 if abs(x - 50) < 24 else 30), (x, 56)], 'deep', 'f', 1.0) for x in (24, 34, 42, 58, 66, 76)]
             + [L(ell(24, 86, 3.4, 3.4), 'blush', 'f', False), L(ell(76, 86, 3.4, 3.4), 'blush', 'f', False),
                L([(24, 70), (20, 66)], OUTC, 'f', False, False, 1.0), L([(76, 70), (80, 66)], OUTC, 'f', False, False, 1.0)],
    'side': [L(ell(40, -4, 8, 6), 'bun', 'b', ln=True),
             L(outline([(84, 52), (94, 46), (94, 28), (78, 6), (50, -4), (24, 2), (6, 20), (0, 48), (4, 76), (18, 86), (34, 84), (38, 68), (48, 60), (66, 56)])),
             L(outline([(2, 46), (30, 50), (38, 66), (34, 84), (18, 86), (4, 76)]), 'shade', 'b', False),
             L(outline([(80, 50), (94, 52), (94, 64), (84, 62)]), 'mid', 'f')],
    'back': [L(ell(50, -4, 10, 6), 'bun', 'b', ln=True),
             L(outline([(8, 80), (4, 44), (12, 16), (32, 0), (50, -4), (68, 0), (88, 16), (96, 44), (92, 80), (66, 88), (50, 90), (34, 88)])),
             L(outline([(60, -2), (88, 16), (96, 44), (92, 80), (66, 86), (70, 40)]), 'shade', 'b', False),
             L(outline([(10, 70), (6, 96), (12, 106, 1), (16, 84), (18, 72)]), 'mid', 'b', ln=True)]
            + [strand([(x, 8), (x, 86)], 'deep', 'b', 1.0) for x in (30, 42, 58, 70)],
}

# Brendan Branch (portero): piel tostada y cabeza rapada, con una cresta amarillo verdoso pálido que le nace en pico en la
# frente y va hacia atrás; cejas del mismo color, ojazos negros y sonrisa
CHARS[K + 'brendan-branch'] = {
    'body': 'normal', 'pal': pal('#cccc8a', SK_T, iris='#1e1a1c', shade='#a8a86a', deep='#86864e'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False, 'face_front': BALD, 'nose': (50, 86, 2.2)},
    'front': [L(outline([(44, 20), (42, 0), (46, -14), (52, -22, 1), (56, -10), (58, 6), (56, 22), (52, 56, 1), (48, 26)]), 'mid', 'f', ln=True),
              L(outline([(53, -16), (56, -10), (58, 6), (56, 22), (52, 50)]), 'shade', 'f', False)]
             + brows(64, 'mid', 3.6, 14, 0.2, 11),
    'side': [L(outline([(76, 34), (72, 14), (62, 0), (58, -14, 1), (44, -6), (24, 2), (10, 18), (4, 38), (12, 40), (24, 22), (44, 12), (62, 20)]), 'mid', 'f', ln=True)]
            + brow_side(64, 'mid', 3.6, 0.2),
    'back': [L(outline([(44, 8), (46, -8), (52, -14), (56, -6), (56, 10), (54, 60), (50, 70), (46, 60)]), 'mid', 'f', ln=True)],
}

# Brent Cross: piel tostada y mofletes; pelo castaño oscuro en pinchos revueltos, con un mechón largo amarillo verdoso
# pálido que le cae por la frente hasta el ojo; ojazos gris violeta y sonrisa de dientes
CHARS[K + 'brent-cross'] = {
    'body': 'normal', 'pal': pal('#4a3a1e', SK_T, iris='#9a8aa0', shade='#382c16', deep='#261e0e', lock='#ccd092', lock_d='#a8aa6e'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 95, 'hairline': False, 'face_front': CHUBBY},
    'front': [L(outline([(14, 66), (10, 44), (-2, 36, 1), (12, 26), (8, 10, 1), (24, 12), (26, -6, 1), (38, 4), (50, -14, 1), (56, 2), (70, -8, 1), (72, 8), (88, 4, 1),
                         (84, 20), (98, 26, 1), (88, 36), (90, 66), (84, 54), (16, 54)])),
              L(outline([(60, 2), (88, 4), (84, 20), (98, 26), (88, 36), (88, 62), (80, 34)]), 'shade', 'b', False),
              L(outline([(16, 58), (20, 44), (34, 34), (50, 30), (66, 34), (82, 44), (86, 58), (78, 52), (72, 60, 1), (64, 48), (50, 56, 1), (42, 48), (32, 58, 1), (26, 50)]),
                'mid', 'f'),
              L(outline([(50, 30), (62, 32), (70, 46), (72, 76, 1), (62, 56), (52, 42)]), 'lock', 'f', ln=True),
              strand([(58, 34), (66, 60)], 'lock_d', 'f', 1.0)],
    'side': [L(outline([(80, 50), (86, 42), (100, 38, 1), (88, 30), (98, 14, 1), (80, 14), (80, -6, 1), (64, 4), (54, -12, 1), (42, 2), (24, -8, 1), (22, 10),
                        (4, 12, 1), (10, 28), (2, 50), (8, 72), (20, 84), (34, 82), (38, 66), (46, 58), (62, 54)])),
             L(outline([(4, 44), (28, 46), (40, 60), (34, 82), (20, 84), (8, 72)]), 'shade', 'b', False),
             L(outline([(76, 40), (90, 44), (94, 72, 1), (82, 54)]), 'lock', 'f', ln=True)],
    'back': [L(outline([(14, 78), (10, 44), (-2, 36, 1), (12, 26), (8, 10, 1), (24, 12), (26, -6, 1), (38, 4), (50, -14, 1), (56, 2), (70, -8, 1), (72, 8), (88, 4, 1),
                        (84, 20), (98, 26, 1), (88, 36), (90, 78), (66, 88), (50, 90), (34, 88)])),
             L(outline([(60, 4), (88, 4), (84, 20), (98, 26), (88, 36), (90, 78), (66, 86), (70, 40)]), 'shade', 'b', False)],
}

# Brian Presser: bajito; pelo verde oliva oscuro en casco redondo con un flequillo largo que le tapa un ojo entero; el otro
# ojo verde y una sonrisita
CHARS[K + 'brian-presser'] = {
    'body': 'bajito', 'pal': pal('#4a5422', SK_L, iris='#6a7a3a', shade='#384018', deep='#262c10'),
    'face': {'eyes': 'normal', 'brows': True, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(12, 80), (8, 48), (14, 20), (32, 4), (50, 0), (68, 4), (86, 20), (92, 48), (88, 80), (82, 74), (82, 58), (18, 58), (18, 74)])),
              L(outline([(60, 2), (86, 20), (92, 48), (88, 78), (82, 68), (80, 30)]), 'shade', 'b', False),
              L(outline([(14, 70), (14, 40), (26, 22), (50, 16), (72, 22), (84, 38), (84, 58), (70, 54), (56, 58), (52, 86, 1), (44, 82), (30, 86), (20, 80)]), 'mid', 'f'),
              strand([(30, 26), (36, 70)], 'deep', 'f', 1.0), strand([(46, 22), (48, 78)], 'deep', 'f', 1.0)],
    'side': [L(outline([(82, 54), (92, 46), (94, 28), (78, 6), (50, -2), (24, 4), (6, 22), (2, 50), (6, 76), (18, 86), (34, 84), (38, 68), (48, 60), (66, 58)])),
             L(outline([(4, 46), (30, 50), (38, 66), (34, 84), (18, 86), (6, 76)]), 'shade', 'b', False)],
    'back': [L(outline([(12, 82), (8, 48), (14, 20), (32, 4), (50, 0), (68, 4), (86, 20), (92, 48), (88, 82), (66, 90), (50, 92), (34, 90)])),
             L(outline([(60, 2), (86, 20), (92, 48), (88, 82), (66, 88), (70, 40)]), 'shade', 'b', False)]
            + [strand([(x, 8), (x, 88)], 'deep', 'b', 1.0) for x in (36, 50, 64)],
}

# Brock Twigg: pelo azul claro grisáceo en melena corta con flequillo recto y las puntas abiertas hacia fuera por la
# mandíbula; cejas azules, ojos redondos, nariz larga y sonrisa; cara alargada
CHARS[K + 'brock-twigg'] = {
    'body': 'delgado', 'pal': pal('#90c0c8', SK_LL, iris='#1e1a1c', shade='#709ca4', deep='#507880'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False, 'nose': (50, 84, 2.4)},
    'front': [L(outline([(0, 84, 1), (8, 70), (8, 40), (18, 14), (38, 0), (50, -2), (62, 0), (82, 14), (92, 40), (92, 70), (100, 84, 1), (86, 80), (82, 62), (18, 62),
                         (14, 80)])),
              L(outline([(60, 2), (82, 14), (92, 40), (92, 70), (98, 82), (86, 76), (80, 30)]), 'shade', 'b', False),
              L(outline([(16, 64), (16, 38), (28, 20), (50, 14), (72, 20), (84, 38), (84, 64), (76, 56), (70, 62, 1), (62, 54), (54, 60, 1), (46, 54), (38, 60, 1), (30, 54),
                         (22, 62, 1)]), 'mid', 'f')]
             + brows(66, 'shade', 3.4, 14, 1.0, 11),
    'side': [L(outline([(80, 50), (88, 40), (90, 24), (76, 6), (50, -2), (24, 4), (6, 22), (2, 50), (2, 70), (-6, 86, 1), (12, 80), (28, 88, 1), (34, 76), (38, 64),
                        (48, 58), (64, 54)])),
             L(outline([(2, 46), (30, 50), (36, 64), (26, 84), (8, 80)]), 'shade', 'b', False),
             L(outline([(78, 48), (92, 52), (92, 64, 1), (84, 58)]), 'mid', 'f')] + brow_side(66, 'shade', 3.4, 1.0),
    'back': [L(outline([(0, 86, 1), (8, 70), (8, 40), (18, 14), (38, 0), (50, -2), (62, 0), (82, 14), (92, 40), (92, 70), (100, 86, 1), (78, 84), (64, 92, 1),
                        (50, 84), (36, 92, 1), (22, 84)])),
             L(outline([(60, 2), (82, 14), (92, 40), (92, 70), (98, 84), (76, 84), (70, 40)]), 'shade', 'b', False)]
            + [strand([(x, 6), (x, 84)], 'deep', 'b', 1.0) for x in (34, 50, 66)],
}

# Brook Atwater: piel tostada y cara alargada; melena castaña oscura ondulada hasta los hombros, peinada hacia atrás con un
# pico en la frente; gafas de sol naranjas rectangulares y sonrisa
CHARS[K + 'brook-atwater'] = {
    'body': 'delgado', 'pal': pal('#4a3a1e', SK_T, iris='#1e1a1c', shade='#382c16', deep='#261e0e', lens='#c87a52'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 96,
             'hairline': [(12, 112), (20, 112), (20, 46), (34, 42), (44, 44), (50, 56), (56, 44), (66, 42), (80, 46), (80, 112), (88, 112)]},
    'front': [L(outline([(12, 112), (2, 100, 1), (8, 86), (2, 70, 1), (10, 60), (8, 34), (18, 12), (50, 2), (82, 12), (92, 34), (90, 60), (98, 70, 1), (92, 86),
                         (98, 100, 1), (88, 112), (80, 112), (80, 54), (78, 44), (22, 44), (20, 54), (20, 112)])),
              L(outline([(60, 4), (82, 12), (92, 34), (90, 60), (96, 70), (90, 86), (96, 100), (86, 108), (84, 40)]), 'shade', 'b', False),
              strand([(36, 40), (34, 12)], 'deep', 'b', 1.0), strand([(64, 40), (66, 12)], 'deep', 'b', 1.0),
              L(outline([(20, 70), (46, 72), (44, 82), (24, 81)]), 'lens', 'f', ln=True), L(outline(mir([(20, 70), (46, 72), (44, 82), (24, 81)])), 'lens', 'f', ln=True),
              L([(46, 74), (54, 74)], OUTC, 'f', False, False, 1.6)],
    'side': [L(outline([(78, 44), (86, 30), (80, 10), (56, 0), (28, 4), (8, 20), (0, 46), (-8, 62, 1), (2, 72), (-4, 90, 1), (6, 98), (4, 114, 1), (20, 106),
                        (34, 114, 1), (36, 90), (36, 66), (46, 56), (62, 48)])),
             L(outline([(2, 46), (30, 50), (34, 104), (8, 100)]), 'shade', 'b', False),
             strand([(80, 34), (40, 8)], 'deep', 'b', 1.0),
             L(outline([(76, 70), (90, 71), (89, 82), (77, 81)]), 'lens', 'f', ln=True), L([(50, 72), (76, 72)], OUTC, 'f', False, False, 1.6)],
    'back': [L(outline([(12, 116), (2, 104, 1), (8, 88), (2, 72, 1), (10, 60), (8, 34), (18, 12), (50, 2), (82, 12), (92, 34), (90, 60), (98, 72, 1), (92, 88),
                        (98, 104, 1), (88, 116), (70, 110), (50, 118, 1), (30, 110)])),
             L(outline([(60, 4), (82, 12), (92, 34), (90, 60), (96, 72), (90, 88), (96, 104), (86, 112), (66, 110), (66, 40)]), 'shade', 'b', False)]
            + [strand([(x, 8), (x + 2, 108)], 'deep', 'b', 1.0) for x in (30, 50, 70)],
}

# Bryce Bergman: un tupé altísimo crema blanquecino con una mecha marrón rosada, peinado hacia atrás y hacia un lado, con
# los lados cortos; ojos oliva afilados, sonrisa de lado y barbilla larga
CHARS[K + 'bryce-bergman'] = {
    'body': 'delgado', 'pal': pal('#e8dcc0', SK_L, iris='#8a8040', shade='#c8bc9c', deep='#a49878', streak='#b08a82', streak_d='#8c6a64'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'nose': (50, 86, 2.4),
             'hairline': [(14, 58), (18, 46), (34, 42), (50, 40), (66, 42), (82, 46), (86, 58)]},
    'front': [L(outline([(16, 58), (14, 44), (20, 40), (22, 54)]), 'shade'), L(outline(mir([(16, 58), (14, 44), (20, 40), (22, 54)])), 'shade'),
              L(outline([(18, 46), (16, 22), (24, 0), (36, -16), (54, -26), (70, -24, 1), (64, -14), (78, -2), (84, 20), (82, 46), (50, 48)])),
              L(outline([(48, -22), (62, -18), (70, 0), (68, 30), (62, 56, 1), (56, 30), (54, 6)]), 'streak', 'b', ln=True),
              strand([(30, 40), (32, 0), (48, -18)], 'deep', 'b', 1.0)],
    'side': crop('side', top=16, nape=84, c='shade', shade=False)
            + [L(outline([(78, 40), (88, 26), (92, 6), (84, -14), (66, -24), (80, -32, 1), (56, -28), (34, -18), (18, -4), (12, 14), (20, 34), (40, 40)])),
               L(outline([(56, -26), (76, -20), (86, -4), (84, 16), (70, 0), (60, -12)]), 'streak', 'b', False)],
    'back': crop('back', top=16, nape=84, c='shade', shade=False)
            + [L(outline([(24, 40), (20, 20), (26, 0), (40, -16), (54, -24), (66, -16), (78, -2), (80, 20), (76, 40), (50, 44)])),
               L(outline([(48, -20), (62, -16), (70, 0), (68, 30), (58, 40)]), 'streak', 'b', False)],
}

# Buck Teachey: piel tostada; pelo crema blanquecino en ondas por encima de las orejas, con un pañuelo de cuadros verdes y
# azules atado en la frente; ojos rojizos y sonrisa
CHARS[K + 'buck-teachey'] = {
    'body': 'normal', 'pal': pal('#f0e4c2', SK_T, iris='#c86a60', shade='#d0c29c', deep='#ac9e7a', band='#3a8a5a', band_d='#2a5a8a'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(6, 80, 1), (4, 60), (6, 38), (16, 14), (36, 2), (50, 0), (64, 2), (84, 14), (94, 38), (96, 60), (94, 80, 1), (84, 74), (82, 60), (18, 60),
                         (16, 74)])),
              L(outline([(60, 2), (84, 14), (94, 38), (96, 60), (92, 78), (84, 66), (80, 30)]), 'shade', 'b', False)]
             + [strand([(x, 60), (x - 4, 70), (x, 78)], 'shade', 'b', 1.0) for x in (10, 90)]
             + [L(outline([(14, 62), (18, 54), (30, 58, 1), (26, 50), (16, 48)]), 'mid', 'f')]
             + [band(36, 56, 'band', 'f', 8)]
             + [L([(x, 38 + abs(x - 50) * 0.16), (x, 54 + abs(x - 50) * 0.16)], 'band_d', 'f', False, False, 1.2) for x in (24, 36, 50, 64, 76)]
             + [strand([(14, 46), (50, 40), (86, 46)], 'band_d', 'f', 1.6)],
    'side': [L(outline([(80, 50), (88, 40), (90, 24), (76, 6), (50, -2), (24, 4), (6, 22), (0, 50), (2, 70), (8, 84, 1), (20, 76), (34, 80), (38, 66), (48, 58), (64, 54)])),
             L(outline([(2, 46), (30, 50), (36, 64), (32, 78), (12, 80)]), 'shade', 'b', False),
             band_side(36, 54), L([(30, 38), (30, 54)], 'band_d', 'f', False, False, 2.0), L([(60, 36), (60, 52)], 'band_d', 'f', False, False, 2.0)],
    'back': [L(outline([(6, 82, 1), (4, 60), (6, 38), (16, 14), (36, 2), (50, 0), (64, 2), (84, 14), (94, 38), (96, 60), (94, 82, 1), (76, 80), (62, 88, 1), (50, 80),
                        (38, 88, 1), (24, 80)])),
             L(outline([(60, 2), (84, 14), (94, 38), (96, 60), (92, 80), (76, 80), (70, 40)]), 'shade', 'b', False),
             band_back(38, 56), L(outline([(46, 48), (40, 66, 1), (50, 56), (60, 66, 1), (54, 48)]), 'band', 'f', ln=True)],
}

# Bud Dahman: grandote de piel morena; pelo amarillo pálido en pinchos revueltos arriba, con los lados lisos y largos que
# le caen por detrás de las orejas hasta la mandíbula; ojos afilados y sonrisa ancha
CHARS[K + 'bud-dahman'] = {
    'body': 'corpulento', 'pal': pal('#ecdc9c', SK_D, iris='#1e1a1c', shade='#c8b878', deep='#a49458'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'face_front': CHUBBY,
             'hairline': [(8, 100), (16, 100), (18, 50), (30, 44), (50, 42), (70, 44), (82, 50), (84, 100), (92, 100)]},
    'front': [L(outline([(8, 100), (6, 60), (8, 36), (4, 20, 1), (18, 18), (14, 2, 1), (30, 6), (32, -12, 1), (44, 0), (52, -16, 1), (58, 0), (72, -10, 1), (72, 6),
                         (90, 4, 1), (84, 20), (98, 26, 1), (90, 38), (92, 60), (92, 100), (84, 100), (84, 54), (78, 46), (22, 46), (16, 54), (16, 100)])),
              L(outline([(60, 2), (90, 4), (84, 20), (98, 26), (90, 38), (92, 60), (90, 98), (84, 96), (84, 40)]), 'shade', 'b', False),
              strand([(12, 56), (12, 96)], 'shade', 'b', 1.0), strand([(88, 56), (88, 96)], 'shade', 'b', 1.0),
              L(quad((32, 94), (50, 104), (68, 94)), (100, 50, 30, 255), 'f', False, False, 1.8)],
    'side': [L(outline([(78, 46), (86, 36), (100, 30, 1), (88, 24), (96, 8, 1), (78, 10), (76, -8, 1), (60, 2), (50, -14, 1), (40, 2), (22, -8, 1), (20, 10),
                        (2, 14, 1), (8, 30), (0, 50), (2, 80), (6, 102), (34, 102), (34, 66), (44, 56), (62, 50)])),
             L(outline([(2, 46), (30, 50), (32, 100), (6, 100)]), 'shade', 'b', False)],
    'back': [L(outline([(8, 104), (6, 60), (8, 36), (4, 20, 1), (18, 18), (14, 2, 1), (30, 6), (32, -12, 1), (44, 0), (52, -16, 1), (58, 0), (72, -10, 1), (72, 6),
                        (90, 4, 1), (84, 20), (98, 26, 1), (90, 38), (92, 60), (92, 104), (50, 106)])),
             L(outline([(60, 4), (90, 4), (84, 20), (98, 26), (90, 38), (92, 60), (92, 102), (66, 104), (66, 40)]), 'shade', 'b', False)]
            + [strand([(x, 30), (x, 102)], 'shade', 'b', 1.0) for x in (30, 50, 70)],
}

# Bud Hunter (portero): pelo rosa malva en una nube de rizos en espiral muy abultada, con una trenza gruesa que le cae por
# un lado; ojos afilados con mucho blanco, cejas enfadadas y boca de gato
CHARS[K + 'bud-hunter'] = {
    'body': 'normal', 'pal': pal('#c09ca4', SK_L, iris='#1e1a1c', shade='#9c7a84', deep='#7a5a64'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'hairline': [(10, 70), (16, 52), (26, 46), (36, 50), (46, 44), (56, 48), (66, 44), (76, 50), (84, 52),
                                                                               (90, 70)]},
    'front': [L(outline([(10, 72), (0, 50), (4, 28), (14, 10), (32, -4), (50, -8), (68, -4), (86, 10), (96, 28), (100, 50), (92, 72), (84, 64), (80, 58), (20, 58),
                         (16, 64)])),
              L(outline([(62, -4), (86, 10), (96, 30), (98, 50), (90, 70), (84, 46), (76, 24)]), 'shade', 'b', False)]
             + [L(quad((cx - 6, cy + 4), (cx, cy - 8), (cx + 6, cy)) + quad((cx + 6, cy), (cx + 2, cy + 6), (cx - 1, cy + 2))[1:], 'deep', 'b', False, False, 1.2)
                for cx, cy in ((22, 24), (40, 10), (60, 12), (78, 26), (14, 46), (86, 48), (50, 30))]
             + [L(rope((84, 70), (100, 86), (90, 104), 9), 'mid', 'f', ln=True), L(rope((90, 104), (86, 112), (92, 120), 6), 'mid', 'f', ln=True)]
             + [L(quad((42, 94), (46, 98), (50, 95)) + quad((50, 95), (54, 98), (58, 94))[1:], (130, 70, 50, 255), 'f', False, False, 1.4)],
    'side': [L(outline([(80, 52), (90, 44), (98, 28), (88, 8), (66, -6), (40, -8), (16, 2), (0, 22), (-4, 46), (2, 70), (16, 84), (34, 82), (40, 66), (48, 58), (64, 54)])),
             L(outline([(-2, 44), (30, 48), (40, 64), (34, 82), (16, 84), (2, 70)]), 'shade', 'b', False),
             L(rope((20, 80), (6, 100), (16, 118), 8), 'mid', 'b', ln=True)]
            + [L(quad((cx - 6, cy + 4), (cx, cy - 8), (cx + 6, cy)), 'deep', 'b', False, False, 1.2) for cx, cy in ((24, 20), (50, 8), (74, 18), (16, 44))],
    'back': [L(outline([(10, 82), (0, 56), (4, 30), (14, 10), (32, -4), (50, -8), (68, -4), (86, 10), (96, 30), (100, 56), (90, 82), (66, 90), (50, 92), (34, 90)])),
             L(outline([(62, -4), (86, 10), (96, 32), (100, 56), (90, 82), (66, 88), (70, 40)]), 'shade', 'b', False),
             L(rope((20, 82), (6, 100), (14, 118), 8), 'mid', 'f', ln=True)]
            + [L(quad((cx - 6, cy + 4), (cx, cy - 8), (cx + 6, cy)), 'deep', 'b', False, False, 1.2) for cx, cy in ((26, 20), (50, 30), (74, 22), (40, 56), (64, 60))],
}

# Buddy Goodman: cara alargada de señor; pelo azul marino casi negro rapado al cepillo y alto arriba, con las orejas
# grandes; ojillos de punto, cejas enfadadas, nariz en punta y una sonrisa de raya
CHARS[K + 'buddy-goodman'] = {
    'body': 'normal', 'pal': pal('#2e2642', SK_L, iris='#1e1a1c', shade='#221c32', deep='#161222'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'none', 'big_ears': 2, 'nose': (50, 85, 2.8),
             'hairline': [(16, 54), (20, 42), (34, 38), (50, 37), (66, 38), (80, 42), (84, 54)]},
    'front': [L(outline([(18, 56), (16, 30), (22, 8), (50, 0), (78, 8), (84, 30), (82, 56), (78, 44), (22, 44)])),
              L(outline([(60, 2), (78, 8), (84, 30), (82, 54), (76, 30)]), 'shade', 'b', False),
              strand([(50, 2), (50, 36)], 'deep', 'b', 1.0),
              L([(34, 96), (66, 96)], (130, 70, 50, 255), 'f', False, False, 1.6)],
    'side': [L(outline([(70, 42), (80, 34), (82, 16), (68, 2), (44, -2), (22, 4), (10, 22), (6, 46), (12, 64), (26, 72), (36, 66), (40, 56), (54, 48)]))],
    'back': [L(outline([(18, 70), (16, 30), (22, 8), (50, 0), (78, 8), (84, 30), (82, 70), (66, 78), (50, 80), (34, 78)])),
             L(outline([(58, 2), (78, 8), (84, 30), (82, 70), (66, 76), (66, 40)]), 'shade', 'b', False)],
}

# Bully Thrower: pelo gris lila corto en mechones, con una antena larga y fina que se levanta en arco desde la coronilla;
# ojos verdes, cejas enfadadas y sonrisa de lado con colmillo
CHARS[K + 'bully-thrower'] = {
    'body': 'normal', 'pal': pal('#b8a4b6', SK_L, iris='#6a9a8a', shade='#968296', deep='#746274'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(14, 74), (8, 50), (12, 24), (30, 6), (50, 2), (70, 6), (88, 24), (92, 50), (86, 74), (82, 62), (18, 62)])),
              L(outline([(60, 4), (88, 24), (92, 50), (86, 72), (80, 34)]), 'shade', 'b', False),
              L(rope((46, 6), (50, -36), (96, -20), 4), 'mid', 'b', ln=True),
              L(outline([(16, 64), (16, 40), (28, 24), (50, 18), (72, 24), (84, 40), (84, 64), (76, 52), (70, 62, 1), (64, 48), (56, 60, 1), (50, 46), (42, 58, 1), (36, 48),
                         (26, 60, 1), (22, 50)]), 'mid', 'f'),
              L(outline([(58, 95), (60, 100, 1), (62, 95)]), WHITE, 'f', ln=True)],
    'side': [L(outline([(80, 50), (88, 40), (90, 24), (76, 6), (50, -2), (24, 4), (6, 22), (2, 50), (6, 74), (18, 84), (32, 82), (38, 66), (48, 58), (64, 54)])),
             L(outline([(4, 46), (30, 50), (38, 64), (32, 82), (18, 84), (6, 74)]), 'shade', 'b', False),
             L(rope((44, 0), (60, -40), (100, -26), 4), 'mid', 'b', ln=True),
             L(outline([(78, 48), (92, 52), (92, 66, 1), (84, 58)]), 'mid', 'f')],
    'back': [L(outline([(14, 78), (8, 50), (12, 24), (30, 6), (50, 2), (70, 6), (88, 24), (92, 50), (86, 78), (66, 88), (50, 90), (34, 88)])),
             L(outline([(60, 4), (88, 24), (92, 50), (86, 78), (66, 86), (70, 40)]), 'shade', 'b', False),
             L(rope((50, 6), (50, -36), (4, -22), 4), 'mid', 'b', ln=True)],
}

# Burt Mocking: payaso grandote de cara blanquecina; dos matas enormes de pelo rojo que le salen a los lados de un gorro
# crema ajustado, con mechones rosa claro sobre la frente; nariz de payaso roja y redonda, párpados caídos y sonrisa
CHARS[K + 'burt-mocking'] = {
    'body': 'corpulento', 'pal': pal('#a82412', '#fce6c4', iris='#1e1a1c', shade='#84180c', deep='#5e1008', cap='#f2e6c2', cap_d='#d8c89e', pink='#e8a2b4',
                                     nose='#c01e14'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 99, 'hairline': False, 'face_front': CHUBBY},
    'front': [L(outline([(16, 74), (-14, 70), (-18, 50), (-4, 34), (16, 32)])), L(outline(mir([(16, 74), (-14, 70), (-18, 50), (-4, 34), (16, 32)]))),
              L(outline([(-14, 66), (-16, 52), (-4, 38), (8, 62)]), 'shade', 'b', False),
              L(outline([(18, 64), (24, 52), (34, 62, 1), (30, 50), (44, 54), (40, 46), (60, 48), (20, 48)]), 'pink', 'f', ln=True),
              L(outline([(10, 52), (8, 30), (20, 10), (50, 2), (80, 10), (92, 30), (90, 52), (70, 46), (50, 44), (30, 46)]), 'cap', 'f', ln=True),
              L(outline([(60, 4), (80, 10), (92, 30), (90, 52), (76, 48), (78, 24)]), 'cap_d', 'f', False),
              L([(28, 74), (44, 74)], OUTC, 'f', False, False, 2.0), L([(56, 74), (72, 74)], OUTC, 'f', False, False, 2.0),
              L(ell(50, 87, 12, 10), 'nose', 'f', ln=True), L(ell(46, 83, 3, 2.2), (236, 120, 110, 255), 'f', False)],
    'side': [L(outline([(20, 70), (-10, 66), (-14, 46), (0, 30), (24, 30)])),
             L(outline([(86, 46), (94, 30), (80, 10), (52, 2), (24, 6), (8, 22), (6, 46), (40, 48), (60, 48)]), 'cap', 'f', ln=True),
             L(outline([(82, 46), (92, 50), (92, 62, 1)]), 'pink', 'f', ln=True),
             L([(76, 74), (85, 74)], OUTC, 'f', False, False, 2.0), L(ell(90, 87, 6, 7), 'nose', 'f', ln=True)],
    'back': [L(outline([(16, 74), (-14, 70), (-18, 50), (-4, 34), (16, 32)])), L(outline(mir([(16, 74), (-14, 70), (-18, 50), (-4, 34), (16, 32)]))),
             L(outline([(10, 60), (8, 30), (20, 10), (50, 2), (80, 10), (92, 30), (90, 60), (50, 64)]), 'cap', 'f', ln=True),
             L(outline([(60, 4), (80, 10), (92, 30), (90, 60), (66, 62)]), 'cap_d', 'f', False)],
}

# Buster Chopps (portero): gorro de lana verde azulado con una estrella y puntitos, con un rulo trenzado crema alrededor y
# el pelo oscuro asomando por los lados; ojos afilados, ceño fruncido y sonrisita
CHARS[K + 'buster-chopps'] = {
    'body': 'normal', 'pal': pal('#3a3a3e', SK_L, iris='#1e1a1c', shade='#2a2a2e', deep='#1c1c20', hat='#6c9c92', hat_d='#527a72', roll='#ece4c4', roll_d='#c8bea0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(16, 76), (12, 52), (22, 48), (22, 70)])), L(outline(mir([(16, 76), (12, 52), (22, 48), (22, 70)]))),
              L(outline([(12, 48), (12, 26), (24, 6), (50, -2), (76, 6), (88, 26), (88, 48), (50, 44)]), 'hat', 'f', ln=True),
              L(outline([(60, 0), (76, 6), (88, 26), (88, 46), (78, 44), (78, 20)]), 'hat_d', 'f', False),
              L(outline([(30, 14), (33, 22), (42, 22), (35, 27), (38, 35), (30, 30), (22, 35), (25, 27), (18, 22), (27, 22)]), 'hat_d', 'f', False)]
             + [L(ell(x, y, 0.9, 0.9), 'hat_d', 'f', False) for x, y in ((50, 10), (60, 18), (68, 28), (46, 26), (56, 34), (72, 14), (40, 6))]
             + [L(rope((8, 50), (50, 32), (92, 50), 10), 'roll', 'f', ln=True)]
             + [L([(x, 40 + abs(x - 50) * 0.18), (x + 4, 48 + abs(x - 50) * 0.18)], 'roll_d', 'f', False, False, 1.2) for x in range(14, 88, 8)],
    'side': [L(outline([(36, 50), (40, 76), (24, 82), (10, 70), (8, 50)])),
             L(outline([(90, 46), (92, 28), (78, 8), (50, -2), (24, 4), (8, 22), (4, 48), (50, 48)]), 'hat', 'f', ln=True),
             L(outline([(4, 30), (30, 30), (40, 46), (4, 48)]), 'hat_d', 'f', False),
             L(rope((2, 50), (50, 42), (94, 46), 10), 'roll', 'f', ln=True)],
    'back': [L(outline([(14, 50), (14, 74), (34, 86), (50, 88), (66, 86), (86, 74), (86, 50)])),
             L(outline([(10, 52), (10, 26), (24, 6), (50, -2), (76, 6), (90, 26), (90, 52), (50, 56)]), 'hat', 'f', ln=True),
             L(outline([(60, 0), (76, 6), (90, 26), (90, 52), (64, 54)]), 'hat_d', 'f', False),
             L(rope((8, 52), (50, 62), (92, 52), 10), 'roll', 'f', ln=True)],
}

# Buster Clout: grandullón con cara de bulldog: casco verde de fútbol americano con una estrella amarilla grande arriba y
# una franja crema en el centro; nariz chata enorme, párpados caídos y sonrisa de lado
CHARS[K + 'buster-clout'] = {
    'body': 'corpulento', 'pal': pal('#3a3a3e', SK_T, iris='#1e1a1c', helm='#3a8a4c', helm_d='#2a6a38', star='#e8c830', stripe='#ece2c0'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'none', 'hairline': False, 'face_front': SQUARE, 'ears': False},
    'front': [L(outline([(4, 100), (0, 50), (6, 20), (24, 0), (50, -8), (76, 0), (94, 20), (100, 50), (96, 100), (86, 100), (86, 66), (80, 52), (50, 48), (20, 52),
                         (14, 66), (14, 100)]), 'helm', 'f', ln=True),
              L(outline([(62, -4), (76, 0), (94, 20), (100, 50), (96, 98), (88, 98), (88, 40)]), 'helm_d', 'f', False),
              L(outline([(42, 48), (42, 20), (58, 20), (58, 48)]), 'stripe', 'f', False),
              L(outline([(50, -6), (56, 8), (72, 8), (60, 18), (66, 34), (50, 24), (34, 34), (40, 18), (28, 8), (44, 8)]), 'star', 'f', ln=True),
              L(quad((14, 60), (50, 46), (86, 60)), 'helm_d', 'f', False, False, 2.0),
              L(ell(50, 86, 8, 6), 'skin_d', 'f', ln=True), L(ell(46, 87, 1.6, 1.4), OUTC, 'f', False), L(ell(54, 87, 1.6, 1.4), OUTC, 'f', False),
              L([(28, 72), (44, 72)], OUTC, 'f', False, False, 2.0), L([(56, 72), (72, 72)], OUTC, 'f', False, False, 2.0),
              L(quad((34, 98), (52, 100), (64, 94)), (110, 60, 40, 255), 'f', False, False, 1.6)],
    'side': [L(outline([(80, 50), (90, 40), (94, 20), (78, 2), (50, -8), (22, -2), (4, 16), (-2, 46), (2, 84), (14, 100), (56, 100), (58, 64), (70, 54)]), 'helm', 'f',
               ln=True),
             L(outline([(0, 46), (30, 46), (50, 64), (50, 98), (14, 98), (2, 84)]), 'helm_d', 'f', False),
             L(outline([(44, -6), (60, -4), (80, 8), (74, 18), (52, 8), (38, 6)]), 'star', 'f', ln=True),
             L(ell(32, 72, 6, 7), 'helm_d', 'f', ln=True), L(ell(88, 86, 5, 6), 'skin_d', 'f', ln=True),
             L([(76, 72), (85, 72)], OUTC, 'f', False, False, 2.0)],
    'back': [L(outline([(4, 100), (0, 50), (6, 20), (24, 0), (50, -8), (76, 0), (94, 20), (100, 50), (96, 100), (50, 104)]), 'helm', 'f', ln=True),
             L(outline([(62, -4), (76, 0), (94, 20), (100, 50), (96, 98), (70, 100)]), 'helm_d', 'f', False),
             L(outline([(42, 100), (42, 10), (58, 10), (58, 100)]), 'stripe', 'f', False),
             L(outline([(50, -6), (56, 8), (72, 8), (60, 18), (66, 34), (50, 24), (34, 34), (40, 18), (28, 8), (44, 8)]), 'star', 'f', ln=True)],
}

# Buster Locke: pelo rojo con dos picos en las esquinas como orejas de gato y patillas largas en punta; cara cuadrada, ojos
# enfadados, nariz naranja y boca de morros
CHARS[K + 'buster-locke'] = {
    'body': 'normal', 'pal': pal('#b02c12', SK_L, iris='#1e1a1c', shade='#8a200c', deep='#641608', nose='#e8803a'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 97, 'face_front': SQUARE, 'nose': (50, 86, 3.0),
             'hairline': [(10, 96), (16, 96), (18, 50), (30, 44), (40, 50), (50, 46), (60, 50), (70, 44), (82, 50), (84, 96), (90, 96)]},
    'front': [L(outline([(10, 96), (6, 50), (8, 20), (2, -6, 1), (24, 10), (50, 14), (76, 10), (98, -6, 1), (92, 20), (94, 50), (90, 96), (84, 96), (82, 56), (78, 50),
                         (22, 50), (18, 56), (16, 96)])),
              L(outline([(60, 14), (76, 10), (98, -6), (92, 22), (94, 50), (90, 92), (84, 92), (84, 40)]), 'shade', 'b', False),
              strand([(12, 56), (14, 90)], 'deep', 'b', 1.0), strand([(88, 56), (86, 90)], 'deep', 'b', 1.0)],
    'side': [L(outline([(74, 48), (84, 40), (90, 22), (98, 4, 1), (78, 8), (54, 8), (26, 8), (6, -4, 1), (8, 22), (4, 48), (8, 72), (20, 84), (36, 82), (40, 66),
                        (48, 60), (60, 56)])),
             L(outline([(52, 54), (62, 54), (62, 96, 1), (56, 80)])),
             L(outline([(4, 44), (30, 46), (42, 60), (36, 82), (20, 84), (8, 72)]), 'shade', 'b', False)],
    'back': [L(outline([(12, 86), (8, 50), (6, 20), (2, -6, 1), (24, 10), (50, 10), (76, 10), (98, -6, 1), (94, 20), (92, 50), (88, 86), (66, 90), (50, 92),
                        (34, 90)])),
             L(outline([(60, 12), (76, 10), (98, -6), (94, 22), (92, 52), (88, 86), (66, 90), (66, 40)]), 'shade', 'b', False)],
}

# Butch Pythons (portero): grandote de mandíbula ancha; pelo rubio en pinchos tiesos hacia arriba, con los lados cortos;
# ojos gris verdoso afilados, cejas rubias enfadadas, nariz grande y boca de enfado
CHARS[K + 'butch-pythons'] = {
    'body': 'corpulento', 'pal': pal('#dcc070', SK_T, iris='#5a9a9a', shade='#b89c50', deep='#8c7438'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 97, 'face_front': SQUARE, 'nose': (50, 86, 3.6),
             'hairline': [(12, 60), (16, 48), (30, 44), (40, 48), (50, 42), (60, 48), (70, 44), (84, 48), (88, 60)]},
    'front': [L(outline([(14, 62), (10, 40), (12, 20), (6, -2, 1), (24, 10), (26, -12, 1), (38, 4), (46, -18, 1), (54, 2), (64, -14, 1), (68, 6), (82, -6, 1), (84, 16),
                         (94, 10, 1), (90, 40), (86, 62), (80, 52), (20, 52)])),
              L(outline([(60, 4), (82, -6), (84, 16), (94, 10), (90, 40), (86, 60), (76, 36)]), 'shade', 'b', False),
              strand([(30, 10), (34, 40)], 'deep', 'b', 1.0), strand([(50, 4), (50, 40)], 'deep', 'b', 1.0), strand([(68, 10), (66, 40)], 'deep', 'b', 1.0)]
             + brows(66, 'shade', 4.2, 15, 1.6, 13),
    'side': [L(outline([(76, 46), (84, 36), (98, 20, 1), (82, 18), (88, 2, 1), (70, 6), (66, -12, 1), (54, 2), (40, -14, 1), (34, 4), (16, -4, 1), (18, 14), (6, 26),
                        (2, 48), (8, 72), (20, 84), (34, 82), (38, 66), (46, 58), (62, 50)])),
             L(outline([(4, 44), (28, 46), (40, 60), (34, 82), (20, 84), (8, 72)]), 'shade', 'b', False)] + brow_side(66, 'shade', 4.2, 1.6),
    'back': [L(outline([(14, 78), (10, 40), (12, 20), (6, -2, 1), (24, 10), (26, -12, 1), (38, 4), (46, -18, 1), (54, 2), (64, -14, 1), (68, 6), (82, -6, 1), (84, 16),
                        (94, 10, 1), (90, 40), (86, 78), (66, 88), (50, 90), (34, 88)])),
             L(outline([(60, 6), (82, -6), (84, 16), (94, 10), (90, 40), (86, 78), (66, 86), (68, 40)]), 'shade', 'b', False)],
}

# Butler Chambers: cara alargada de señor, con arrugas en las mejillas; un gorro abombado crema con una franja verde en el
# centro y el borde verde, que le tapa toda la cabeza; párpados caídos, nariz larga y sonrisa
CHARS[K + 'butler-chambers'] = {
    'body': 'delgado', 'pal': pal('#3a3a3e', SK_L, iris='#1e1a1c', hat='#f2e2c0', hat_d='#d8c49c', green='#5a9040', green_d='#44702e'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 97, 'hairline': False, 'nose': (50, 86, 2.6)},
    'front': [L(outline([(8, 76), (4, 40), (14, 12), (32, -4), (50, -8), (68, -4), (86, 12), (96, 40), (92, 76), (84, 70), (82, 58), (50, 54), (18, 58), (16, 70)]), 'hat',
                'f', ln=True),
              L(outline([(60, -4), (86, 12), (96, 40), (92, 74), (84, 66), (80, 30)]), 'hat_d', 'f', False),
              L(outline([(40, -6), (60, -6), (62, 56), (38, 56)]), 'green', 'f', False),
              L(outline([(8, 76), (6, 64), (18, 56), (50, 52), (82, 56), (94, 64), (92, 76), (84, 70), (82, 62), (50, 58), (18, 62), (16, 70)]), 'green', 'f', ln=True),
              L([(28, 72), (44, 72)], OUTC, 'f', False, False, 2.0), L([(56, 72), (72, 72)], OUTC, 'f', False, False, 2.0),
              L(quad((22, 82), (28, 90), (24, 98)), (190, 130, 90, 255), 'f', False, False, 1.0),
              L(quad((78, 82), (72, 90), (76, 98)), (190, 130, 90, 255), 'f', False, False, 1.0)],
    'side': [L(outline([(84, 52), (94, 44), (94, 26), (78, 4), (50, -8), (24, -2), (6, 16), (0, 44), (2, 76), (16, 86), (34, 82), (40, 64), (52, 56), (68, 54)]), 'hat',
               'f', ln=True),
             L(outline([(2, 44), (30, 48), (38, 62), (34, 82), (16, 86), (2, 76)]), 'hat_d', 'f', False),
             L(quad((30, 0), (60, 16), (88, 48)) + quad((92, 42), (62, 8), (40, -6)), 'green', 'f', False),
             L(outline([(2, 70), (20, 80), (36, 76), (42, 60), (54, 54), (86, 52), (88, 58), (56, 62), (46, 68), (40, 84), (16, 88), (2, 78)]), 'green', 'f', ln=True),
             L([(76, 72), (85, 72)], OUTC, 'f', False, False, 2.0)],
    'back': [L(outline([(8, 80), (4, 40), (14, 12), (32, -4), (50, -8), (68, -4), (86, 12), (96, 40), (92, 80), (66, 90), (50, 92), (34, 90)]), 'hat', 'f', ln=True),
             L(outline([(60, -4), (86, 12), (96, 40), (92, 80), (66, 88), (70, 40)]), 'hat_d', 'f', False),
             L(outline([(40, -6), (60, -6), (60, 90), (40, 90)]), 'green', 'f', False),
             L(outline([(8, 80), (8, 68), (34, 80), (50, 82), (66, 80), (92, 68), (92, 80), (66, 92), (50, 94), (34, 92)]), 'green', 'f', ln=True)],
}

# Cal Cooler: pelo gris pardo en rizos apretados, alto y redondo arriba y con los lados rizados hasta la mandíbula; cejas
# grises, ojos redondos, orejas grandes y una sonrisa con hoyuelo
CHARS[K + 'cal-cooler'] = {
    'body': 'normal', 'pal': pal('#8c8470', SK_L, iris='#1e1a1c', shade='#6e6856', deep='#504c3e'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'big_ears': 2, 'ear_out': 3,
             'hairline': [(8, 96), (16, 96), (18, 52), (30, 44), (40, 48), (50, 42), (60, 48), (70, 44), (82, 52), (84, 96), (92, 96)]},
    'front': [L(outline([(8, 98), (2, 84), (6, 70), (2, 54), (8, 38), (6, 20), (18, 4), (34, -8), (50, -12), (66, -8), (82, 4), (94, 20), (92, 38), (98, 54), (94, 70),
                         (98, 84), (92, 98), (84, 98), (84, 56), (78, 46), (22, 46), (16, 56), (16, 98)])),
              L(outline([(62, -8), (82, 4), (94, 22), (92, 38), (98, 54), (94, 70), (96, 84), (90, 96), (84, 92), (84, 40)]), 'shade', 'b', False)]
             + [L(quad((x - 5, y + 3), (x, y - 5), (x + 5, y + 2)), 'deep', 'b', False, False, 1.2)
                for x, y in ((26, 14), (44, 2), (62, 4), (78, 16), (36, 28), (56, 24), (10, 60), (90, 60), (10, 82), (90, 82))]
             + brows(66, 'shade', 3.4, 14, 0.0, 12)
             + [L([(50, 90), (50, 94)], (130, 70, 50, 255), 'f', False, False, 1.2)],
    'side': [L(outline([(78, 46), (88, 36), (90, 20), (78, 0), (54, -10), (28, -6), (8, 10), (0, 34), (-2, 60), (2, 86), (10, 100), (34, 98), (34, 70), (44, 56),
                        (62, 50)])),
             L(outline([(2, 46), (30, 50), (32, 96), (8, 96)]), 'shade', 'b', False)]
            + [L(quad((x - 5, y + 3), (x, y - 5), (x + 5, y + 2)), 'deep', 'b', False, False, 1.2) for x, y in ((30, 8), (56, 2), (72, 16), (16, 40), (20, 70))]
            + brow_side(66, 'shade', 3.4, 0.0),
    'back': [L(outline([(8, 100), (2, 84), (6, 70), (2, 54), (8, 38), (6, 20), (18, 4), (34, -8), (50, -12), (66, -8), (82, 4), (94, 20), (92, 38), (98, 54), (94, 70),
                        (98, 84), (92, 100), (50, 104)])),
             L(outline([(62, -8), (82, 4), (94, 22), (92, 38), (98, 54), (94, 70), (96, 84), (90, 98), (66, 100), (66, 40)]), 'shade', 'b', False)]
            + [L(quad((x - 5, y + 3), (x, y - 5), (x + 5, y + 2)), 'deep', 'b', False, False, 1.2)
               for x, y in ((26, 14), (50, 4), (74, 14), (30, 40), (56, 36), (40, 66), (64, 70), (20, 86), (80, 86))],
}

# Cal Emarry (portero): pelo castaño malva revuelto en mechones de punta, con una cinta rosada muy baja, justo sobre las
# cejas; párpados caídos, nariz grande y una boca de morros entreabierta
CHARS[K + 'cal-emarry'] = {
    'body': 'normal', 'pal': pal('#a06a62', SK_L, iris='#1e1a1c', shade='#80524c', deep='#603c36', band='#c8907e', band_d='#a8705e', lip='#b06a50'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'none', 'hairline': False, 'nose': (50, 86, 3.4)},
    'front': [L(outline([(14, 66), (6, 54, 1), (10, 40), (2, 26, 1), (16, 20), (12, 4, 1), (28, 8), (32, -8, 1), (44, 2), (56, -10, 1), (62, 4), (78, -2, 1), (78, 12),
                         (94, 16, 1), (88, 30), (98, 42, 1), (88, 50), (86, 66), (80, 58), (20, 58)])),
              L(outline([(60, 4), (78, -2), (78, 12), (94, 16), (88, 30), (98, 42), (88, 50), (86, 62), (78, 34)]), 'shade', 'b', False),
              L(outline([(14, 60), (18, 42), (34, 32), (50, 28), (66, 32), (82, 42), (86, 60)]), 'mid', 'f'),
              band(60, 70, 'band', 'f', 8),
              L([(28, 76), (44, 76)], OUTC, 'f', False, False, 2.0), L([(56, 76), (72, 76)], OUTC, 'f', False, False, 2.0),
              L(rope((40, 97), (50, 92), (60, 97), 5), 'lip', 'f', ln=True), L([(43, 97), (57, 97)], OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(80, 50), (86, 42), (100, 38, 1), (88, 30), (98, 14, 1), (80, 14), (80, -4, 1), (64, 4), (54, -12, 1), (42, 2), (24, -8, 1), (22, 10),
                        (4, 12, 1), (10, 28), (2, 50), (8, 72), (20, 84), (34, 82), (38, 66), (46, 58), (62, 54)])),
             L(outline([(4, 44), (28, 46), (40, 60), (34, 82), (20, 84), (8, 72)]), 'shade', 'b', False),
             band_side(60, 69), L([(76, 76), (85, 76)], OUTC, 'f', False, False, 2.0)],
    'back': [L(outline([(14, 78), (6, 58, 1), (10, 40), (2, 26, 1), (16, 20), (12, 4, 1), (28, 8), (32, -8, 1), (44, 2), (56, -10, 1), (62, 4), (78, -2, 1), (78, 12),
                        (94, 16, 1), (88, 30), (98, 42, 1), (88, 56), (86, 78), (66, 88), (50, 90), (34, 88)])),
             L(outline([(60, 6), (78, -2), (78, 12), (94, 16), (88, 30), (98, 42), (88, 56), (86, 78), (66, 86), (70, 40)]), 'shade', 'b', False),
             band_back(60, 70)],
}

# Cal O'Rees: pelo verde azulado corto peinado hacia atrás, con mechones de punta detrás de las orejas; una cicatriz naranja
# en forma de estrella en la frente; ojazos enfadados y boca seria
CHARS[K + 'cal-o-rees'] = {
    'body': 'normal', 'pal': pal('#4f8a86', SK_L, iris='#1e1a1c', shade='#3c6c68', deep='#2c4e4c', scar='#e0a040'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95,
             'hairline': [(14, 60), (18, 46), (34, 40), (50, 38), (66, 40), (82, 46), (86, 60)]},
    'front': [L(outline([(16, 62), (2, 76, 1), (12, 70), (10, 40), (18, 14), (50, 2), (82, 14), (90, 40), (88, 70), (98, 76, 1), (84, 62), (80, 48), (20, 48)])),
              L(outline([(60, 4), (82, 14), (90, 40), (88, 68), (96, 74), (84, 60), (78, 34)]), 'shade', 'b', False),
              strand([(30, 40), (34, 12)], 'deep', 'b', 1.0), strand([(66, 40), (64, 10)], 'deep', 'b', 1.0),
              L(outline([(60, 46), (63, 52), (70, 52), (64, 56), (68, 64), (60, 58), (52, 62), (56, 55), (50, 50), (58, 51)]), 'scar', 'f', ln=True)],
    'side': [L(outline([(78, 44), (86, 30), (80, 12), (56, 2), (28, 6), (8, 20), (2, 46), (0, 64), (-8, 82, 1), (12, 76), (18, 88, 1), (28, 80), (38, 66), (48, 56),
                        (64, 50)])),
             L(outline([(4, 44), (30, 48), (38, 64), (26, 82), (10, 76)]), 'shade', 'b', False),
             strand([(80, 34), (40, 10)], 'deep', 'b', 1.0)],
    'back': [L(outline([(16, 76), (2, 84, 1), (12, 66), (10, 40), (18, 14), (50, 2), (82, 14), (90, 40), (88, 66), (98, 84, 1), (84, 76), (70, 84), (64, 94, 1),
                        (56, 84), (44, 94, 1), (36, 84)])),
             L(outline([(58, 6), (82, 14), (90, 42), (88, 66), (96, 82), (84, 76), (66, 84), (66, 40)]), 'shade', 'b', False)],
}

# Callan Trens: pelo rosa salmón en casco corto con flequillo de mechones; ojazos amarillos, cejas enfadadas y sonrisa
CHARS[K + 'callan-trens'] = {
    'body': 'normal', 'pal': pal('#d47a74', SK_L, iris='#d8c040', shade='#b05e5a', deep='#8a4642'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(12, 80), (8, 48), (14, 20), (32, 4), (50, 0), (68, 4), (86, 20), (92, 48), (88, 80), (82, 74), (82, 58), (18, 58), (18, 74)])),
              L(outline([(60, 2), (86, 20), (92, 48), (88, 78), (82, 68), (80, 30)]), 'shade', 'b', False),
              L(outline([(16, 62), (16, 40), (28, 22), (50, 16), (72, 22), (84, 40), (84, 62), (76, 54), (70, 62, 1), (62, 52), (54, 60, 1), (48, 50), (40, 60, 1), (34, 52),
                         (26, 60, 1), (22, 54)]), 'mid', 'f'),
              strand([(50, 4), (48, 18)], 'deep', 'f', 1.0)],
    'side': [L(outline([(82, 54), (92, 46), (94, 28), (78, 6), (50, -2), (24, 4), (6, 22), (2, 50), (6, 76), (18, 86), (34, 84), (38, 68), (48, 60), (66, 58)])),
             L(outline([(4, 46), (30, 50), (38, 66), (34, 84), (18, 86), (6, 76)]), 'shade', 'b', False),
             L(outline([(80, 52), (92, 54), (92, 66, 1), (84, 60)]), 'mid', 'f')],
    'back': [L(outline([(12, 82), (8, 48), (14, 20), (32, 4), (50, 0), (68, 4), (86, 20), (92, 48), (88, 82), (66, 90), (50, 92), (34, 90)])),
             L(outline([(60, 2), (86, 20), (92, 48), (88, 82), (66, 88), (70, 40)]), 'shade', 'b', False)]
            + [strand([(x, 8), (x, 88)], 'deep', 'b', 1.0) for x in (36, 50, 64)],
}

# Cam Broadsheet: mofletudo; pelo azul marino en pinchos revueltos, con una cinta ancha verde con rombos amarillos en la
# frente y el flequillo cayendo por delante; ojos negros rasgados y sonrisa
CHARS[K + 'cam-agent-broadsheet'] = {
    'body': 'corpulento', 'pal': pal('#2c3a6a', SK_L, iris='#1e1a1c', shade='#202c52', deep='#161e3a', band='#2a7a3a', band_y='#e0c020'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 97, 'hairline': False, 'face_front': CHUBBY},
    'front': [L(outline([(10, 74), (-4, 64, 1), (6, 52), (-2, 34, 1), (12, 28), (8, 8, 1), (26, 12), (30, -8, 1), (44, 4), (54, -12, 1), (60, 4), (76, -6, 1), (76, 10),
                         (94, 8, 1), (88, 26), (104, 34, 1), (92, 46), (104, 62, 1), (90, 74), (84, 62), (16, 62)])),
              L(outline([(60, 4), (76, -6), (76, 10), (94, 8), (88, 26), (104, 34), (92, 46), (102, 60), (88, 70), (80, 34)]), 'shade', 'b', False),
              band(34, 56, 'band', 'f', 8)]
             + [L(outline([(x, 30 + abs(x - 50) * 0.16), (x + 7, 39 + abs(x - 50) * 0.16), (x, 48 + abs(x - 50) * 0.16), (x - 7, 39 + abs(x - 50) * 0.16)]), 'band_y',
                  'f', ln=True) for x in (22, 36, 50, 64, 78)]
             + [L(outline([(16, 54), (22, 74, 1), (30, 56), (38, 72, 1), (44, 56), (56, 56), (62, 72, 1), (70, 56), (78, 74, 1), (84, 54)]), 'mid', 'f'),
                L(outline([(28, 76), (44, 80), (42, 84), (30, 80)]), OUTC, 'f', False), L(outline(mir([(28, 76), (44, 80), (42, 84), (30, 80)])), OUTC, 'f', False)],
    'side': [L(outline([(80, 50), (86, 42), (100, 38, 1), (88, 30), (98, 14, 1), (80, 14), (80, -6, 1), (64, 4), (54, -12, 1), (42, 2), (24, -8, 1), (22, 10),
                        (2, 8, 1), (8, 28), (-8, 38, 1), (4, 48), (-6, 64, 1), (8, 66), (10, 86, 1), (24, 76), (36, 72), (46, 60), (62, 54)])),
             L(outline([(4, 44), (28, 46), (38, 62), (24, 78), (10, 70)]), 'shade', 'b', False),
             band_side(34, 54),
             L(outline([(78, 52), (92, 54), (94, 70, 1), (84, 62)]), 'mid', 'f'),
             L(outline([(78, 77), (88, 79), (86, 83), (78, 81)]), OUTC, 'f', False)],
    'back': [L(outline([(10, 80), (-4, 70, 1), (6, 58), (-2, 34, 1), (12, 28), (8, 8, 1), (26, 12), (30, -8, 1), (44, 4), (54, -12, 1), (60, 4), (76, -6, 1), (76, 10),
                        (94, 8, 1), (88, 26), (104, 34, 1), (92, 46), (104, 68, 1), (90, 80), (74, 92, 1), (66, 84), (54, 94, 1), (46, 84), (34, 92, 1), (28, 84)])),
             L(outline([(60, 6), (76, -6), (76, 10), (94, 8), (88, 26), (104, 34), (92, 46), (102, 66), (88, 78), (70, 40)]), 'shade', 'b', False),
             band_back(36, 56), L(outline([(46, 50), (38, 70, 1), (50, 58), (62, 70, 1), (54, 50)]), 'band', 'f', ln=True)],
}

# Cam Lensman: pelo azul acero en pinchos revueltos que salen hacia los lados; cejas azules gruesas y enfadadas, ojillos
# redondos y boca seria
CHARS[K + 'cam-lensman'] = {
    'body': 'normal', 'pal': pal('#5a8c9c', SK_L, iris='#1e1a1c', shade='#46707e', deep='#32525c'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': False},
    'front': messy('front', amp=14, n=12, seed=11, rx=46, ry=38, cy=42, lo=64)
             + [L(outline([(14, 66), (18, 44), (34, 34), (50, 30), (66, 34), (82, 44), (86, 66, 1), (76, 54), (70, 62, 1), (62, 50), (54, 58, 1), (48, 46), (40, 58, 1),
                           (34, 50), (24, 62, 1), (22, 52)]), 'mid', 'f')]
             + brows(66, 'deep', 4.4, 14, 1.6, 12),
    'side': messy('side', amp=14, n=12, seed=11, rx=46, ry=38, cy=42) + [L(outline([(78, 50), (92, 52), (94, 68, 1), (84, 60)]), 'mid', 'f')]
            + brow_side(66, 'deep', 4.4, 1.6),
    'back': messy('back', amp=14, n=12, seed=11, rx=46, ry=38, cy=42),
}

# Cam O'Miles (portero): pelo amarillo verdoso pálido en casco de seta con mechones marcados, una antena de dos pelos en la
# coronilla y las puntas abiertas por encima de las orejas; ojos afilados y sonrisa de lado
CHARS[K + 'cam-o-miles'] = {
    'body': 'normal', 'pal': pal('#d4d092', SK_L, iris='#1e1a1c', shade='#b0ac70', deep='#8a8852'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False, 'nose': (50, 86, 2.6)},
    'front': [L(outline([(0, 72, 1), (8, 62), (8, 34), (18, 12), (38, 2), (62, 2), (82, 12), (92, 34), (92, 62), (100, 72, 1), (86, 68), (84, 60), (16, 60), (14, 68)])),
              L(rope((48, 4), (40, -12), (54, -14), 3), 'mid', 'b', ln=True), L(rope((52, 4), (60, -12), (70, -6), 3), 'mid', 'b', ln=True),
              L(outline([(60, 4), (82, 12), (92, 36), (92, 60), (98, 70), (86, 64), (80, 30)]), 'shade', 'b', False),
              L(outline([(14, 62), (14, 40), (26, 24), (50, 18), (74, 24), (86, 40), (86, 62), (72, 56), (50, 54), (28, 56)]), 'mid', 'f')]
             + [strand([(x, 20 + abs(x - 50) * 0.2), (x, 56)], 'shade', 'f', 1.0) for x in (22, 32, 42, 58, 68, 78)],
    'side': [L(outline([(82, 54), (92, 46), (94, 28), (78, 6), (50, -2), (24, 4), (6, 22), (2, 50), (-6, 70, 1), (10, 66), (24, 80), (36, 78), (38, 66), (48, 60),
                        (66, 58)])),
             L(rope((50, 0), (44, -16), (58, -18), 3), 'mid', 'b', ln=True),
             L(outline([(4, 46), (30, 50), (38, 64), (24, 78), (10, 70)]), 'shade', 'b', False)]
            + [strand([(x, 4), (x - 6, 56)], 'shade', 'b', 1.0) for x in (40, 60, 76)],
    'back': [L(outline([(0, 74, 1), (8, 64), (8, 34), (18, 12), (38, 2), (62, 2), (82, 12), (92, 34), (92, 64), (100, 74, 1), (78, 76), (64, 84), (50, 86), (36, 84),
                        (22, 76)])),
             L(rope((50, 4), (44, -12), (34, -10), 3), 'mid', 'b', ln=True),
             L(outline([(60, 4), (82, 12), (92, 36), (92, 64), (98, 72), (78, 76), (70, 40)]), 'shade', 'b', False)]
            + [strand([(x, 6), (x, 80)], 'shade', 'b', 1.0) for x in (24, 36, 50, 64, 76)],
}

# Cam Vass (portero): pelo verde oliva en mechones largos de punta que caen por la frente y salen por los lados; ojos
# redondos blancos con la pupila pequeña, cejas negras gruesas y enfadadas, bigotitos y sonrisa
CHARS[K + 'cam-vass'] = {
    'body': 'normal', 'pal': pal('#8a9042', SK_L, iris='#1e1a1c', shade='#6c7030', deep='#4e5222'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False, 'nose': (50, 86, 2.2)},
    'front': [L(outline([(16, 74), (-6, 62, 1), (8, 52), (6, 30), (18, 10), (38, 0), (62, 0), (82, 10), (94, 30), (92, 52), (106, 62, 1), (84, 74), (82, 62), (18, 62)])),
              L(outline([(60, 2), (82, 10), (94, 30), (92, 52), (104, 62), (86, 70), (80, 30)]), 'shade', 'b', False),
              L(outline([(14, 66), (16, 40), (28, 22), (50, 16), (72, 22), (84, 40), (86, 66), (78, 56), (72, 66, 1), (64, 52), (56, 64, 1), (50, 50), (44, 64, 1), (36, 52),
                         (28, 66, 1), (22, 56)]), 'mid', 'f'),
              strand([(38, 22), (42, 54)], 'shade', 'f', 1.0), strand([(62, 22), (58, 54)], 'shade', 'f', 1.0)]
             + brows(64, (30, 26, 28, 255), 4.6, 15, 1.6, 13)
             + [L([(12, 84), (22, 86)], OUTC, 'f', False, False, 1.0), L([(12, 89), (22, 89)], OUTC, 'f', False, False, 1.0),
                L([(88, 84), (78, 86)], OUTC, 'f', False, False, 1.0), L([(88, 89), (78, 89)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(80, 50), (88, 40), (90, 24), (76, 6), (50, -2), (24, 4), (6, 22), (2, 48), (-10, 64, 1), (8, 64), (8, 84, 1), (24, 76), (34, 80), (38, 66),
                        (48, 58), (64, 54)])),
             L(outline([(4, 44), (30, 48), (38, 64), (24, 78), (10, 66)]), 'shade', 'b', False),
             L(outline([(78, 48), (92, 52), (94, 70, 1), (84, 60)]), 'mid', 'f')] + brow_side(64, (30, 26, 28, 255), 4.6, 1.6),
    'back': [L(outline([(16, 80), (-6, 66, 1), (8, 54), (6, 30), (18, 10), (38, 0), (62, 0), (82, 10), (94, 30), (92, 54), (106, 66, 1), (84, 80), (72, 90, 1), (62, 82),
                        (50, 92, 1), (38, 82), (28, 90, 1)])),
             L(outline([(60, 2), (82, 10), (94, 30), (92, 54), (104, 66), (84, 78), (70, 40)]), 'shade', 'b', False)],
}

# Cameron Hameha: melena castaña lisa por la mandíbula, con flequillo de mechones largos en punta que le cae entre los ojos;
# ojazos negros, bigotitos y sonrisa
CHARS[K + 'cameron-hameha'] = {
    'body': 'normal', 'pal': pal('#7a4a16', SK_L, iris='#1e1a1c', shade='#5e3810', deep='#42260a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    'front': [L(outline([(10, 100, 1), (6, 70), (6, 40), (16, 14), (36, 2), (50, 0), (66, 2), (86, 14), (96, 40), (96, 70), (92, 100, 1), (84, 90), (82, 60), (18, 60),
                         (16, 90)])),
              L(outline([(60, 2), (86, 14), (96, 40), (96, 70), (92, 98), (84, 76), (80, 30)]), 'shade', 'b', False),
              L(outline([(16, 64), (16, 40), (28, 22), (50, 16), (72, 22), (84, 40), (84, 66), (74, 54), (66, 66, 1), (60, 50), (52, 70, 1), (46, 50), (36, 64, 1), (30, 50),
                         (22, 62, 1)]), 'mid', 'f'),
              strand([(40, 22), (46, 50)], 'deep', 'f', 1.0), strand([(62, 22), (58, 50)], 'deep', 'f', 1.0)]
             + [L([(16, 84), (22, 85)], OUTC, 'f', False, False, 1.0), L([(16, 88), (22, 88)], OUTC, 'f', False, False, 1.0),
                L([(84, 84), (78, 85)], OUTC, 'f', False, False, 1.0), L([(84, 88), (78, 88)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(80, 48), (88, 40), (90, 24), (76, 6), (50, -2), (24, 4), (6, 22), (0, 50), (2, 84), (8, 102, 1), (34, 96), (36, 70), (44, 60), (64, 54)])),
             L(outline([(2, 46), (30, 50), (34, 94), (10, 98)]), 'shade', 'b', False),
             L(outline([(76, 46), (92, 50), (92, 70, 1), (82, 58)]), 'mid', 'f')],
    'back': [L(outline([(10, 102, 1), (6, 70), (6, 40), (16, 14), (36, 2), (50, 0), (66, 2), (86, 14), (96, 40), (96, 70), (92, 102, 1), (50, 98)])),
             L(outline([(60, 2), (86, 14), (96, 40), (96, 70), (92, 100), (64, 98)]), 'shade', 'b', False)]
            + [strand([(x, 8), (x, 96)], 'deep', 'b', 1.0) for x in (34, 50, 66)],
}
