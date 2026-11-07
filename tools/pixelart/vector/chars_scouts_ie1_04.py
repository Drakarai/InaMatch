"""Ojeadores de IE1 (scouts-ie1), tanda 04: dibujados a partir de su retrato de Victory Road; claves 'scouts-ie1:<id>'.
Ninguno tiene modelo 3D: perfil y espalda deducidos del peinado del retrato."""
from chars import CHARS, L, OUTC, blob, ell, longhair, messy, outline, pal, rope, strand  # noqa: F401
from chars_vr_nikogawa import blush, brow_side, brows, crop, ring_glasses, wide_smile  # noqa: F401
from heads import quad  # noqa: F401

T = 'scouts-ie1:'
WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 28, 255)
LIP = (150, 80, 60, 255)


def fr(pts, c='mid'):
    """Flequillo o mechón por delante de la cara."""
    return L(outline(pts), c, 'f')


def back_of(front_pts_top, nape=86, c='mid'):
    """Espalda sencilla de un casquete: la misma curva de arriba que el frente, cerrada en la nuca."""
    return [L(outline(front_pts_top + [(84, 76), (66, nape - 2), (50, nape), (34, nape - 2), (16, 76)]), c),
            L(outline([(58, 6), (84, 22), (90, 46), (84, 76), (66, nape - 2), (60, 50)]), 'shade', 'b', False)]


def side_cap(top=2, nape=86, front=(84, 44), w=0, c='mid'):
    """Perfil de un casquete que llega a la frente en front=(x, y)."""
    fx, fy = front
    return [L(outline([(fx - 14, fy + 6), (fx - 4, fy), (fx + 2, fy - 16), (78, 8), (54, top - 2), (28, top + 4), (8, 22), (2 - w, 46), (8, 70), (20, nape),
                       (34, nape - 2), (38, 66), (44, 58), (58, fy + 8)]), c),
            L(outline([(3 - w, 44), (30, 46), (42, 58), (36, 66), (34, nape - 2), (20, nape), (8, 70)]), 'shade', 'b', False)]


def nose_tri(x=50, y=86, w=4, h=7, c=(232, 120, 40, 255)):
    return L([(x - w, y - h * 0.3), (x + w, y - h * 0.3), (x, y + h * 0.7)], c, 'f', ln=True)


def star4(x, y, r=4, c=(110, 60, 40, 255)):
    k = r * 0.28
    return L([(x, y - r), (x + k, y - k), (x + r, y), (x + k, y + k), (x, y + r), (x - k, y + k), (x - r, y), (x - k, y - k)], c, 'f', False)


# Dan Vega: turbante crema enorme enrollado que le tapa todo el pelo y una venda que le tapa de la nariz a la barbilla;
# cejas naranjas gruesas y ojos redondos negros
_TUR = (252, 226, 182, 255)
CHARS[T + 'dan-vega'] = {
    'body': 'normal', 'pal': pal('#fce1b5', '#ebb778', iris='#1e1a1a', shade='#e0c08e', deep='#bc9b7d', brow='#d07a2a'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'none', 'hairline': False, 'eye_y': 74},
    'front': [L(outline([(10, 66), (2, 40), (12, 10), (34, -6), (60, -8), (84, 2), (98, 26), (96, 54), (88, 66), (80, 56), (20, 56)])),
              L(outline([(60, -6), (84, 4), (98, 28), (94, 54), (84, 50), (76, 20)]), 'shade', 'b', False),
              strand([(12, 40), (40, 8), (80, 0)], 'deep', 'b', 1.2), strand([(14, 54), (50, 22), (94, 24)], 'deep', 'b', 1.2),
              strand([(30, 56), (62, 30), (96, 44)], 'deep', 'b', 1.0)]
             + brows(64, 'brow', 4.0, 14, 0.2, 12)
             + [L(outline([(17, 80), (30, 79), (50, 82), (70, 79), (83, 80), (80, 92), (64, 99), (50, 102), (36, 99), (20, 92)]), _TUR, 'f', ln=True),
                strand([(22, 86), (50, 92), (78, 86)], 'deep', 'f', 1.0), strand([(30, 95), (50, 98), (70, 95)], 'deep', 'f', 1.0)],
    'side': [L(outline([(86, 58), (92, 40), (88, 14), (68, -4), (40, -6), (14, 6), (0, 30), (2, 58), (14, 72), (30, 74), (44, 62), (60, 56)])),
             L(outline([(2, 40), (30, 44), (40, 62), (28, 74), (12, 70)]), 'shade', 'b', False),
             strand([(10, 20), (50, -2), (86, 20)], 'deep', 'b', 1.2), strand([(4, 44), (46, 22), (90, 40)], 'deep', 'b', 1.2)]
            + brow_side(64, 'brow', 4.0, 0.2)
            + [L(outline([(70, 80), (87, 80), (86, 92), (80, 100), (66, 102), (56, 100), (54, 88)]), _TUR, 'f', ln=True)],
    'back': [L(outline([(10, 72), (2, 44), (12, 12), (34, -4), (66, -4), (88, 12), (98, 44), (90, 72), (50, 80)])),
             L(outline([(60, -2), (86, 12), (98, 44), (90, 70), (64, 76)]), 'shade', 'b', False),
             strand([(8, 40), (50, 20), (94, 40)], 'deep', 'b', 1.2), strand([(10, 60), (50, 42), (96, 60)], 'deep', 'b', 1.2),
             L(blob([(38, 74), (50, 66), (62, 74), (58, 86), (42, 86)], 6), 'shade', 'b', ln=True)],
}

# Darrel Jeeling (portero): media melena rosa con flequillo recto y un rollo enroscado a cada lado de la cara, y una corona
# dorada con un gorrito rojo y verde encima; ojos verde azulado, cejas enfadadas y media sonrisa
_GOLD = (232, 190, 70, 255)
_GOLD_D = (190, 140, 40, 255)


def _crown(cx=50, y=6, w=24, h=12, view='front'):
    if view == 'side':
        return [L(outline([(cx - 20, y + 4), (cx - 16, y - h - 8), (cx, y - h - 14), (cx + 14, y - h - 6), (cx + 18, y + 2)]), (200, 50, 40, 255), 'f'),
                L(outline([(cx - 4, y - h - 14), (cx + 14, y - h - 6), (cx + 16, y - 4), (cx + 2, y - 4)]), (60, 150, 70, 255), 'f', False),
                L([(cx - 22, y + 6), (cx - 24, y - h), (cx - 12, y - 4), (cx, y - h - 2), (cx + 10, y - 4), (cx + 20, y - h), (cx + 20, y + 6)], _GOLD, 'f', ln=True)]
    return [L(outline([(cx - w + 6, y), (cx - w + 4, y - h - 6), (cx, y - h - 14), (cx + w - 4, y - h - 6), (cx + w - 6, y)]), (200, 50, 40, 255), 'f'),
            L(outline([(cx - 8, y - h - 12), (cx + 8, y - h - 12), (cx + 10, y - 2), (cx - 10, y - 2)]), (60, 150, 70, 255), 'f', False),
            L([(cx - w, y + 6), (cx - w - 2, y - h), (cx - w / 2, y - 3), (cx, y - h - 2), (cx + w / 2, y - 3), (cx + w + 2, y - h), (cx + w, y + 6)],
              _GOLD, 'f', ln=True),
            L([(cx - w, y + 2), (cx + w, y + 2), (cx + w, y + 6), (cx - w, y + 6)], _GOLD_D, 'f', False)]


def _roll(cx, cy, r):
    return [L(ell(cx, cy, r, r * 1.05), 'mid', 'f', ln=True), L(ell(cx, cy, r * 0.55, r * 0.6), 'shade', 'f', ln=True), L(ell(cx, cy, r * 0.2, r * 0.22), 'deep', 'f', False)]


CHARS[T + 'darrel-jeeling'] = {
    'body': 'normal', 'pal': pal('#ca8776', '#edb870', iris='#5aa8a0', shade='#a0624c', deep='#84341a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'ears': False,
             'hairline': [(16, 74), (18, 58), (82, 58), (84, 74)]},
    'front': [L(outline([(10, 82), (8, 46), (16, 16), (50, 6), (84, 16), (92, 46), (90, 82), (80, 70), (80, 58), (20, 58), (20, 70)])),
              L(outline([(60, 8), (84, 18), (92, 46), (90, 78), (82, 60)]), 'shade', 'b', False)]
             + [strand([(x, 20), (x, 56)], 'deep', 'b', 0.9) for x in (30, 42, 58, 70)]
             + _roll(10, 76, 11) + _roll(90, 76, 11) + _crown(50, 8),
    'side': [L(outline([(80, 58), (86, 40), (78, 12), (54, 2), (26, 6), (8, 24), (2, 52), (6, 78), (22, 88), (38, 86), (50, 64), (64, 58)])),
             L(outline([(3, 46), (28, 48), (40, 62), (36, 84), (22, 88), (8, 76)]), 'shade', 'b', False)]
            + _roll(46, 76, 12) + _crown(52, 6, view='side'),
    'back': [L(outline([(10, 82), (8, 44), (16, 16), (50, 6), (84, 16), (92, 44), (90, 82), (50, 88)])),
             L(outline([(58, 8), (84, 18), (92, 46), (90, 80), (62, 86)]), 'shade', 'b', False)]
            + [strand([(x, 18), (x, 84)], 'deep', 'b', 0.9) for x in (30, 50, 70)]
            + _roll(10, 76, 11) + _roll(90, 76, 11) + _crown(50, 8),
}

# Dash Dotter: piel morena y pelo liso azul verdoso claro, con flequillo de lado y dos mechones largos y afilados que le bajan
# por delante de las orejas hasta la barbilla; ojos verdes, cejas enfadadas y boca abierta de mueca
CHARS[T + 'dash-dotter'] = {
    'body': 'normal', 'pal': pal('#9bc5c1', '#c5985b', iris='#4a9a3a', shade='#7d9e9a', deep='#5e7a78'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 93,
             'hairline': [(16, 68), (18, 54), (30, 50), (42, 56), (54, 46), (68, 50), (80, 50), (84, 66)]},
    'front': [L(outline([(14, 108, 1), (11, 80), (9, 46), (18, 16), (50, 2), (82, 16), (91, 46), (89, 80), (86, 108, 1), (80, 82), (80, 56), (20, 56), (20, 82)])),
              L(outline([(60, 4), (84, 18), (91, 46), (88, 84), (84, 100), (82, 60)]), 'shade', 'b', False),
              strand([(44, 8), (36, 48)], 'deep', 'b', 1.0), strand([(64, 10), (74, 44)], 'deep', 'b', 1.0)],
    'side': [L(outline([(80, 52), (88, 36), (82, 12), (56, 0), (28, 4), (8, 22), (2, 50), (6, 80), (14, 96), (26, 92), (34, 74), (42, 60), (56, 56), (66, 54)])),
             L(outline([(3, 46), (30, 48), (40, 60), (30, 80), (16, 94), (6, 78)]), 'shade', 'b', False),
             fr([(56, 60), (62, 58), (60, 84), (56, 106, 1), (52, 84)])],
    'back': longhair('back', length=92, flare=2, top=2, ends=4),
}

# Dave Altair: rubio peinado hacia atrás y aplastado, con un mechón que le cae por la frente a un lado y las puntas de
# los lados abiertas en pico; una marca de estrella oscura en la frente, párpados caídos y sonrisa
CHARS[T + 'dave-altair'] = {
    'body': 'normal', 'pal': pal('#d9b961', '#f0b770', iris='#2a2020', shade='#b8963e', deep='#8e6535'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 92,
             'hairline': [(16, 66), (18, 50), (30, 44), (50, 42), (70, 44), (82, 50), (84, 66)]},
    'front': [L(outline([(8, 80, 1), (12, 66), (10, 40), (18, 14), (50, 2), (82, 14), (90, 40), (88, 66), (92, 80, 1), (82, 72), (80, 48), (20, 48), (18, 72)])),
              L(outline([(60, 4), (84, 16), (90, 40), (88, 64), (82, 56), (76, 26)]), 'shade', 'b', False)]
             + [strand([(x, 8), (x * 1.0, 42)], 'deep', 'b', 1.0) for x in (34, 46, 58, 70)]
             + [fr([(26, 44), (34, 40), (28, 58), (24, 70, 1), (22, 56)]), star4(50, 56, 5)],
    'side': side_cap(top=2, nape=84, front=(84, 44))
            + [strand([(30, 10), (60, 6), (82, 20)], 'deep', 'b', 1.0), strand([(14, 30), (50, 20), (84, 34)], 'deep', 'b', 1.0),
               L(outline([(8, 70), (2, 86, 1), (14, 80), (18, 92, 1), (24, 82)]), 'mid', 'b')],
    'back': [L(outline([(8, 82, 1), (14, 70), (12, 40), (20, 14), (50, 2), (80, 14), (88, 40), (86, 70), (92, 82, 1), (76, 80), (66, 90, 1), (58, 82), (50, 92, 1),
                        (42, 82), (34, 90, 1), (24, 80)])),
             L(outline([(58, 4), (82, 16), (88, 44), (88, 76), (64, 84)]), 'shade', 'b', False)]
            + [strand([(x, 6), (x, 76)], 'deep', 'b', 1.0) for x in (34, 50, 66)],
}

# Dave Chaucer: pelo naranja en pinchos hacia arriba y flequillo de puntas sobre los ojos; gafas redondas negras y sonrisa
CHARS[T + 'dave-chaucer'] = {
    'body': 'bajito', 'pal': pal('#cc6c1e', '#eeb571', iris='#2a2020', shade='#a14f1c', deep='#7e3d16'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    'front': messy('front', amp=16, n=10, seed=4, lo=64, sweep=-0.2)
             + [fr([(16, 64), (14, 44), (30, 30), (50, 26), (70, 30), (86, 44), (84, 64), (80, 56), (74, 66, 1), (68, 54), (60, 62, 1), (54, 52), (46, 64, 1), (40, 52),
                    (32, 64, 1), (26, 54), (20, 66, 1)])]
             + ring_glasses('front', 76, BLACK, 2.2, 8.5, 7.5, 14),
    'side': messy('side', amp=16, n=10, seed=4, nape=88, sweep=0.3) + [fr([(74, 44), (90, 46), (88, 58), (84, 66, 1), (80, 56)])]
            + ring_glasses('side', 76, BLACK, 2.2, 5, 7.5),
    'back': messy('back', amp=16, n=10, seed=4, nape=88),
}

# Dave O'Resis: grandullón de cara larga y piel tostada; casco de pelo amarillo con flequillo de puntas, cejas amarillas
# gruesas y unos labios enormes
CHARS[T + 'dave-o-resis'] = {
    'body': 'corpulento', 'pal': pal('#d7b41c', '#cc924a', iris='#2a2020', shade='#b08e14', deep='#8a6a10'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'none', 'hairline': False, 'eye_y': 76,
             'face_front': blob([(18, 52), (50, 30), (82, 52), (84, 78), (78, 100), (62, 110), (50, 112), (38, 110), (22, 100), (16, 78)])},
    'front': [L(outline([(12, 70), (8, 40), (18, 12), (50, 0), (82, 12), (92, 40), (88, 70), (80, 62), (20, 62)])),
              L(outline([(60, 2), (84, 14), (92, 40), (88, 66), (82, 48)]), 'shade', 'b', False),
              fr([(16, 64), (14, 40), (30, 24), (50, 20), (70, 24), (86, 40), (86, 64), (80, 56), (72, 64, 1), (64, 54), (56, 62, 1), (48, 52), (40, 62, 1), (32, 54),
                  (24, 62, 1), (20, 56)])]
             + brows(66, 'mid', 4.5, 14, 0.1, 13)
             + [L(blob([(36, 96), (44, 92), (50, 93), (56, 92), (64, 96), (60, 103), (50, 106), (40, 103)], 6), (150, 82, 52, 255), 'f', ln=True),
                L(quad((38, 97), (50, 100), (62, 97)), OUTC, 'f', False, False, 1.2)],
    'side': side_cap(top=0, nape=84, front=(86, 50))
            + [fr([(70, 48), (90, 44), (88, 58), (84, 64, 1), (78, 56)])] + brow_side(66, 'mid', 4.5)
            + [L(blob([(80, 94), (88, 93), (90, 99), (86, 104), (80, 102)], 5), (150, 82, 52, 255), 'f', ln=True)],
    'back': back_of([(16, 76), (10, 44), (18, 14), (50, 0), (82, 14), (90, 44)], 86),
}

# David Burnum: pinchos verde grisáceo oscuro de punta hacia arriba; ojos entornados de pillo, sonrisa torcida
CHARS[T + 'david-burnum'] = {
    'body': 'normal', 'pal': pal('#5d7262', '#f8d5a0', iris='#2a2020', shade='#46493e', deep='#37342c'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 93, 'hairline': (60, 48)},
    'front': messy('front', amp=22, n=11, seed=7, lo=66, sweep=0.0),
    'side': messy('side', amp=22, n=11, seed=7, nape=88, sweep=0.2),
    'back': messy('back', amp=22, n=11, seed=7, nape=88),
}

# Davy Johns: cabeza redonda y grande, pelo rapado crema muy claro con pico en la frente; piel tostada, ojos redondos,
# cejas enfadadas y una nariz naranja de zanahoria
CHARS[T + 'davy-johns'] = {
    'body': 'corpulento', 'pal': pal('#fce0b4', '#cc914f', iris='#2a2020', shade='#e8c690', deep='#c8a070'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 95,
             'hairline': [(16, 60), (20, 46), (36, 40), (50, 46), (64, 40), (80, 46), (84, 60)],
             'face_front': blob([(16, 52), (50, 30), (84, 52), (88, 78), (80, 98), (50, 106), (20, 98), (12, 78)])},
    'front': crop('front', top=14, side=60, w=1, flat=4) + [nose_tri(50, 86, 4.5, 8)],
    'side': crop('side', top=12, nape=82, flat=4) + [L([(86, 82), (96, 86), (86, 90)], (232, 120, 40, 255), 'f', ln=True)],
    'back': crop('back', top=14, nape=82, flat=4),
}

# Daz Tighthead (portero): grandote de mandíbula ancha; pelo corto pardo oliva con una mancha más oscura en forma de
# estrella a un lado; cejas gruesas del mismo color, enfadado y con la boca torcida hacia abajo
CHARS[T + 'daz-tighthead'] = {
    'body': 'corpulento', 'pal': pal('#94804a', '#efb46d', iris='#2a2020', shade='#755f30', deep='#5a4824'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 95, 'nose': (50, 86, 3.2),
             'hairline': [(16, 60), (20, 46), (36, 40), (50, 40), (64, 40), (80, 46), (84, 60)],
             'face_front': blob([(16, 52), (50, 30), (84, 52), (88, 78), (82, 98), (64, 108), (50, 110), (36, 108), (18, 98), (12, 78)])},
    'front': crop('front', top=8, side=60, w=1, flat=6) + brows(64, 'mid', 6.0, 15, 0.6, 14)
             + [L(blob([(70, 18), (76, 26), (84, 24), (80, 32), (84, 40), (76, 36), (70, 42), (70, 32), (62, 28), (70, 26)], 3), 'deep', 'b', False)],
    'side': crop('side', top=6, nape=82, flat=6) + brow_side(64, 'mid', 6.0, 0.6),
    'back': crop('back', top=8, nape=82, flat=6),
}

# Dec O'Rator: cara ancha de mofletes; pelo verde de pinchos altos que sube recto como un cepillo; cejas verdes rizadas,
# ojos redondos grandes, nariz de bola y una sonrisa enorme
CHARS[T + 'dec-o-rator'] = {
    'body': 'corpulento', 'pal': pal('#768e49', '#efb46e', iris='#1e1a1a', shade='#5f5e34', deep='#47472e', nose='#e0a060'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'none', 'eye_y': 76, 'nose': (50, 86, 6.5), 'hairline': (56, 46),
             'face_front': blob([(16, 52), (50, 36), (84, 52), (90, 80), (82, 100), (64, 110), (50, 112), (36, 110), (18, 100), (10, 80)])},
    'front': [L(outline([(16, 62), (12, 30), (6, 0, 1), (18, 8), (20, -22, 1), (32, -4), (38, -30, 1), (48, -8), (56, -32, 1), (62, -8), (74, -26, 1), (78, -2),
                         (92, -12, 1), (88, 26), (84, 62), (78, 48), (22, 48)])),
              L(outline([(62, -8), (74, -26), (78, -2), (92, -12), (88, 26), (84, 56), (76, 30)]), 'shade', 'b', False)]
             + [strand([(x, 0), (x + 2, 40)], 'deep', 'b', 1.0) for x in (26, 40, 54, 68)]
             + [L(quad((28, 66), (36, 58), (44, 64)), 'mid', 'f', False, False, 3.0), L(quad((56, 64), (64, 58), (72, 66)), 'mid', 'f', False, False, 3.0)]
             + wide_smile(96, 30, 70, 8, OUTC, 2.0),
    'side': [L(outline([(70, 50), (80, 44), (88, 26), (96, 6, 1), (82, 8), (84, -20, 1), (68, -4), (62, -30, 1), (50, -6), (40, -26, 1), (32, 0), (14, -10, 1),
                        (16, 14), (4, 30), (4, 54), (12, 74), (24, 82), (36, 80), (40, 64), (48, 56), (60, 54)])),
             L(outline([(5, 36), (30, 40), (40, 60), (34, 78), (22, 80), (10, 70)]), 'shade', 'b', False),
             L(quad((72, 64), (78, 58), (86, 64)), 'mid', 'f', False, False, 3.0)],
    'back': [L(outline([(16, 80), (12, 30), (6, 0, 1), (18, 8), (20, -22, 1), (32, -4), (38, -30, 1), (48, -8), (56, -32, 1), (62, -8), (74, -26, 1), (78, -2),
                        (92, -12, 1), (88, 30), (84, 80), (50, 86)])),
             L(outline([(62, -8), (74, -26), (78, -2), (92, -12), (88, 30), (84, 78), (64, 82)]), 'shade', 'b', False)]
            + [strand([(x, 0), (x, 70)], 'deep', 'b', 1.0) for x in (30, 50, 70)],
}

# Dec Orum: cresta en abanico gris lila muy alta en lo alto de la cabeza, con los lados rapados morado oscuro; ojos afilados,
# cejas enfadadas y media sonrisa
_CREST = (184, 157, 158, 255)
_CREST_D = (150, 124, 128, 255)
CHARS[T + 'dec-orum'] = {
    'body': 'normal', 'pal': pal('#5e4e5d', '#f0b56f', iris='#2a2020', shade='#4a3c4a', deep='#3a2e3a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92,
             'hairline': [(16, 62), (20, 48), (34, 40), (50, 36), (66, 40), (80, 48), (84, 62)]},
    'front': crop('front', top=6, side=62, w=-1)
             + [L(outline([(42, 26), (36, 0), (22, -22, 1), (36, -18), (50, -24, 1), (64, -18), (78, -22, 1), (64, 0), (58, 26)]), _CREST, 'f'),
                L(outline([(50, -20), (64, -18), (78, -22), (64, 0), (58, 24), (52, 4)]), _CREST_D, 'f', False),
                strand([(44, 20), (40, -8)], _CREST_D, 'f', 1.0)],
    'side': crop('side', top=4, nape=84, w=-1)
            + [L(outline([(80, 14), (90, -10, 1), (70, -14), (48, -20, 1), (30, -12), (10, -2, 1), (20, 14), (40, 6), (60, 6)]), _CREST, 'f'),
               L(outline([(20, 14), (10, -2), (30, -12), (40, 4)]), _CREST_D, 'f', False)],
    'back': crop('back', top=6, nape=84, w=-1)
            + [L(outline([(42, 30), (36, 2), (24, -20, 1), (38, -16), (50, -22, 1), (62, -16), (76, -20, 1), (64, 2), (58, 30)]), _CREST, 'f'),
               L(outline([(50, -18), (62, -16), (76, -20), (64, 2), (58, 28), (52, 4)]), _CREST_D, 'f', False)],
}

# Del Iverryboy (portero): tupé naranja alto que se levanta hacia un lado en una ola, con los lados cortos; piel clara,
# ojos redondos con pestañas, cejas enfadadas y sonrisa
CHARS[T + 'del-iverryboy'] = {
    'body': 'normal', 'pal': pal('#cd6d1f', '#f7d69f', iris='#1e1a1a', shade='#a6541a', deep='#91451a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'nose': (50, 85, 2.4),
             'hairline': [(16, 66), (18, 52), (30, 46), (44, 50), (56, 44), (70, 46), (82, 52), (84, 66)]},
    'front': [L(outline([(16, 66), (12, 40), (14, 16), (28, -6), (50, -12), (70, -10), (86, 4), (90, 30), (88, 56), (84, 66), (80, 50), (20, 50)])),
              L(outline([(56, -10), (78, -6), (88, 14), (90, 40), (84, 58), (76, 30), (64, 10)]), 'shade', 'b', False),
              strand([(30, 0), (44, 20), (46, 46)], 'deep', 'b', 1.2), strand([(56, -4), (70, 20), (72, 44)], 'deep', 'b', 1.0)],
    'side': [L(outline([(72, 52), (84, 48), (92, 30), (92, 6), (76, -10), (50, -14), (28, -6), (10, 12), (2, 40), (6, 66), (18, 82), (32, 80), (40, 64), (52, 56)])),
             L(outline([(3, 42), (30, 44), (40, 60), (32, 80), (18, 82), (8, 68)]), 'shade', 'b', False),
             strand([(30, -4), (60, 0), (88, 14)], 'deep', 'b', 1.2)],
    'back': [L(outline([(16, 80), (12, 44), (14, 16), (28, -6), (50, -12), (72, -6), (86, 16), (88, 44), (84, 80), (66, 86), (50, 88), (34, 86)])),
             L(outline([(58, -8), (80, 4), (88, 40), (84, 78), (62, 86)]), 'shade', 'b', False),
             strand([(30, 0), (40, 40), (36, 78)], 'deep', 'b', 1.0)],
}

# Den Hidden (portero): grandote de cara redonda y piel tostada; pelo granate en casco con un flequillo espeso que le baja
# hasta los ojos, orejas grandes; ojos achinados y ceño
CHARS[T + 'den-hidden'] = {
    'body': 'corpulento', 'pal': pal('#61210d', '#c5985b', iris='#2a2020', shade='#4b1c0c', deep='#36140a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'big_ears': 2, 'ear_out': 4, 'nose': (50, 86, 3.6), 'eye_y': 78, 'hairline': False,
             'face_front': blob([(14, 52), (50, 34), (86, 52), (92, 80), (84, 100), (64, 110), (50, 112), (36, 110), (16, 100), (8, 80)])},
    'front': [L(outline([(12, 74), (8, 44), (18, 16), (50, 4), (82, 16), (92, 44), (88, 74), (80, 64), (20, 64)])),
              L(outline([(60, 6), (84, 18), (92, 44), (88, 70), (82, 50)]), 'shade', 'b', False),
              fr([(14, 72), (14, 44), (28, 26), (50, 20), (72, 26), (86, 44), (86, 72), (78, 60), (66, 70, 1), (60, 56), (50, 66, 1), (42, 54), (34, 68, 1), (26, 58),
                  (20, 72, 1)]),
              L(quad((24, 68), (32, 62), (42, 68)), OUTC, 'f', False, False, 1.8), L(quad((58, 68), (68, 62), (76, 68)), OUTC, 'f', False, False, 1.8)],
    'side': side_cap(top=2, nape=84, front=(88, 54), w=2) + [fr([(70, 50), (92, 48), (90, 62), (86, 70, 1), (78, 60)])],
    'back': back_of([(14, 76), (8, 44), (18, 14), (50, 2), (82, 14), (92, 44)], 86),
}

# Den Taligene: pelo castaño con un flequillo largo y liso que le cruza la frente en diagonal y tapa un ojo a medias, y los
# lados hasta la mandíbula; ojos afilados y sonrisa con un colmillo
CHARS[T + 'den-taligene'] = {
    'body': 'delgado', 'pal': pal('#79470c', '#efb46c', iris='#2a2020', shade='#5e360a', deep='#442606'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'nose': (50, 85, 3.0),
             'hairline': [(16, 74), (18, 52), (30, 40), (50, 36), (82, 52), (84, 74)]},
    'front': [L(outline([(14, 92, 1), (10, 60), (12, 28), (24, 6), (50, -2), (76, 6), (90, 30), (90, 60), (86, 92, 1), (80, 72), (80, 52), (20, 52), (20, 72)])),
              L(outline([(60, 0), (82, 12), (90, 34), (88, 70), (82, 52)]), 'shade', 'b', False),
              fr([(24, 30), (40, 18), (62, 20), (80, 30), (86, 46), (84, 64), (80, 82, 1), (74, 64), (66, 56), (56, 50), (40, 44), (28, 44)]),
              strand([(40, 24), (66, 40), (78, 64)], 'deep', 'f', 1.0),
              L([(55, 92), (57, 97), (59, 92)], WHITE, 'f', ln=True)],
    'side': [L(outline([(78, 52), (88, 40), (86, 14), (64, 0), (34, 0), (12, 14), (2, 42), (4, 72), (12, 92), (24, 90), (32, 72), (40, 60), (56, 56)])),
             L(outline([(3, 44), (30, 46), (40, 60), (30, 74), (22, 90), (8, 78)]), 'shade', 'b', False),
             fr([(66, 40), (90, 40), (92, 56), (88, 66, 1), (80, 54)])],
    'back': longhair('back', length=86, flare=2, top=-2, ends=4),
}

# Derek Longhand: señor de cara marcada y nariz grande; pelo corto castaño rosado recogido en un moñito en lo alto con una
# goma azul; ojos afilados, cejas gruesas y sonrisa
CHARS[T + 'derek-longhand'] = {
    'body': 'normal', 'pal': pal('#b88267', '#f0b56f', iris='#2a2020', shade='#8f5d45', deep='#6b3b22', band='#5a8ab0'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'nose': (50, 86, 5.0),
             'hairline': [(16, 62), (20, 48), (34, 42), (50, 40), (66, 42), (80, 48), (84, 62)]},
    'front': crop('front', top=4, side=62, w=1)
             + [L(ell(50, -2, 10, 7), 'mid', 'b', ln=True), L(outline([(44, -8), (40, -16, 1), (48, -10), (52, -18, 1), (56, -10), (62, -14, 1), (58, -4)]), 'mid', 'b'),
                L([(40, 4), (60, 4), (58, 8), (42, 8)], 'band', 'b', False)]
             + [strand([(x, 8), (x * 1.0, 40)], 'deep', 'b', 1.0) for x in (30, 42, 58, 70)]
             + brows(64, 'deep', 4.0, 14, 0.3, 13)
             + [L(quad((30, 84), (34, 88), (38, 86)), OUTC, 'f', False, False, 0.9), L(quad((62, 86), (66, 88), (70, 84)), OUTC, 'f', False, False, 0.9)],
    'side': crop('side', top=2, nape=84, w=1)
            + [L(ell(46, -2, 9, 7), 'mid', 'b', ln=True), L(outline([(40, -8), (34, -16, 1), (44, -10), (50, -18, 1), (54, -6)]), 'mid', 'b')]
            + brow_side(64, 'deep', 4.0, 0.3),
    'back': crop('back', top=4, nape=84, w=1)
            + [L(ell(50, -2, 10, 7), 'mid', 'b', ln=True), L(outline([(44, -8), (40, -16, 1), (48, -10), (52, -18, 1), (56, -10), (62, -14, 1), (58, -4)]), 'mid', 'b'),
               L([(40, 4), (60, 4), (58, 8), (42, 8)], 'band', 'b', False)],
}

# Derek Terr: casco azul verdoso con dos antenas que le tapa toda la cabeza menos la cara, con un mechón rubio que asoma
# por la frente y un antifaz rojo oscuro alrededor de los ojos; sonrisa
_HELM = (158, 200, 197, 255)
_HELM_D = (120, 150, 146, 255)
_MASK = (170, 66, 30, 255)
CHARS[T + 'derek-terr'] = {
    'body': 'normal', 'pal': pal('#f2e2a0', '#f6d69d', iris='#1e1a1a', shade='#d8c070', deep='#b09a50'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'ears': False, 'hairline': False},
    'front': [L(outline([(12, 96), (6, 60), (10, 24), (28, 2), (50, -4), (72, 2), (90, 24), (94, 60), (88, 96), (80, 96), (82, 60), (76, 44), (50, 40), (24, 44), (18, 60),
                         (20, 96)]), _HELM),
              L(outline([(60, -2), (84, 12), (94, 50), (90, 92), (82, 92), (84, 56)]), _HELM_D, 'b', False),
              L([(44, -2), (56, -2), (56, 38), (44, 38)], _HELM_D, 'b', False),
              L(outline([(26, 2), (20, -34, 1), (30, -4)]), _HELM, 'b'), L(outline([(70, -4), (80, -34, 1), (74, 2)]), _HELM, 'b'),
              fr([(52, 42), (62, 40), (68, 50), (62, 66, 1), (60, 52), (54, 50)], 'mid'),
              L(outline([(22, 70), (36, 66), (46, 72), (50, 76), (54, 72), (64, 66), (78, 70), (74, 82), (62, 82), (50, 80), (38, 82), (26, 82)]), _MASK, 'f', ln=True)]
             + [L(ell(cx, 75, r, r * 1.05), c, 'f', False) for cx in (36, 64) for r, c in ((4.4, OUTC), (3.3, WHITE), (2.4, BLACK))],
    'side': [L(outline([(70, 46), (84, 40), (92, 22), (80, 2), (54, -6), (28, -2), (8, 16), (0, 46), (4, 80), (12, 100), (30, 100), (40, 80), (50, 60), (58, 52)]), _HELM),
             L(outline([(2, 46), (30, 48), (42, 66), (32, 98), (12, 98), (4, 78)]), _HELM_D, 'b', False),
             L(outline([(40, -2), (36, -34, 1), (48, -4)]), _HELM, 'b'),
             L(outline([(72, 68), (86, 66), (88, 80), (74, 80)]), _MASK, 'f', ln=True),
             L(ell(82, 75, 3.6, 4.4), OUTC, 'f', False), L(ell(82.4, 75, 2.6, 3.3), WHITE, 'f', False), L(ell(83.2, 75, 1.8, 2.4), BLACK, 'f', False)],
    'back': [L(outline([(12, 96), (6, 60), (10, 24), (28, 2), (50, -4), (72, 2), (90, 24), (94, 60), (88, 96), (50, 100)]), _HELM),
             L(outline([(60, -2), (84, 12), (94, 50), (88, 94), (62, 98)]), _HELM_D, 'b', False),
             L(outline([(26, 2), (20, -34, 1), (30, -4)]), _HELM, 'b'), L(outline([(70, -4), (80, -34, 1), (74, 2)]), _HELM, 'b'),
             L([(44, -2), (56, -2), (56, 98), (44, 98)], _HELM_D, 'b', False)],
}

# Des Ainer: pañuelo verde oliva con lunares crema atado a la cabeza, del que salen mechones rubio pálido despeinados por
# los lados y la frente; ojos entornados con pestañas y sonrisa pícara
_BAND = (161, 163, 72, 255)
_BAND_D = (127, 128, 52, 255)
_DOT = (224, 219, 165, 255)


def _dots(pts, r=4.0):
    return [L(ell(x, y, r, r * 0.8), _DOT, 'f', False) for x, y in pts]


CHARS[T + 'des-ainer'] = {
    'body': 'normal', 'pal': pal('#ece2a4', '#eeb46f', iris='#2a2020', shade='#cfc27e', deep='#a89a5a'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 93, 'nose': (50, 86, 2.4), 'hairline': False},
    'front': [L(outline([(10, 92, 1), (14, 74), (6, 70, 1), (14, 56), (14, 30), (50, 14), (86, 30), (86, 56), (94, 70, 1), (86, 74), (90, 92, 1), (80, 76), (80, 56), (20, 56),
                         (20, 76)])),
              fr([(18, 56), (24, 46), (40, 44), (56, 44), (72, 46), (82, 56), (78, 66, 1), (70, 56), (62, 70, 1), (56, 54), (46, 68, 1), (40, 54), (30, 66, 1), (24, 58)]),
              L(outline([(12, 50), (12, 26), (26, 6), (50, -2), (74, 6), (88, 26), (88, 50), (70, 46), (50, 44), (30, 46)]), _BAND, 'f'),
              L(outline([(60, 0), (76, 8), (88, 26), (88, 48), (78, 46), (72, 20)]), _BAND_D, 'f', False)]
             + _dots([(30, 14), (50, 6), (70, 14), (22, 34), (42, 28), (60, 28), (78, 34), (34, 42), (66, 42)]),
    'side': [L(outline([(70, 56), (80, 50), (74, 64, 1), (66, 60), (54, 58), (44, 64), (38, 82, 1), (30, 70), (16, 86, 1), (16, 66), (4, 68, 1), (8, 50), (20, 46), (50, 46)])),
             L(outline([(84, 50), (90, 28), (76, 6), (50, -4), (24, 2), (6, 20), (0, 44), (10, 54), (40, 48), (60, 48)]), _BAND, 'f'),
             L(outline([(4, 30), (0, 44), (10, 54), (30, 50), (20, 32)]), _BAND_D, 'f', False)]
            + _dots([(30, 10), (54, 6), (74, 14), (20, 30), (42, 26), (64, 28), (82, 34), (34, 44)]),
    'back': [L(outline([(10, 92, 1), (14, 74), (6, 70, 1), (14, 56), (16, 40), (84, 40), (86, 56), (94, 70, 1), (86, 74), (90, 92, 1), (72, 84), (62, 94, 1), (54, 84), (44, 94, 1),
                        (36, 84), (24, 92, 1)])),
             L(outline([(12, 56), (12, 26), (26, 6), (50, -2), (74, 6), (88, 26), (88, 56), (50, 60)]), _BAND, 'f'),
             L(outline([(44, 56), (50, 52), (56, 56), (60, 72, 1), (50, 64), (40, 72, 1)]), _BAND_D, 'f', ln=True)]
            + _dots([(30, 14), (50, 6), (70, 14), (22, 34), (42, 28), (60, 28), (78, 34), (34, 46), (66, 46)]),
}

# Des Count: grandullón de cara alargada y barbilla enorme; pelo azul marino peinado hacia atrás con pico en la frente y
# patillas largas; ojos redondos pequeños, nariz grande y boca ondulada
CHARS[T + 'des-count'] = {
    'body': 'corpulento', 'pal': pal('#3e4f62', '#efb46e', iris='#1e1a1a', shade='#2e3b4a', deep='#1e2834', nose='#e0a060'),
    'face': {'eyes': 'round', 'brows': True, 'mouth': 'none', 'eye_y': 74, 'nose': (50, 85, 5.5),
             'hairline': [(16, 76), (18, 54), (30, 46), (42, 48), (50, 56), (58, 48), (70, 46), (82, 54), (84, 76)],
             'face_front': blob([(18, 52), (50, 32), (82, 52), (86, 80), (84, 100), (70, 112), (50, 116), (30, 112), (16, 100), (14, 80)])},
    'front': [L(outline([(16, 78), (12, 46), (18, 18), (50, 4), (82, 18), (88, 46), (84, 78), (80, 56), (20, 56)])),
              L(outline([(60, 6), (82, 18), (88, 46), (84, 74), (78, 40)]), 'shade', 'b', False),
              strand([(36, 14), (40, 46)], 'deep', 'b', 1.0), strand([(64, 14), (60, 46)], 'deep', 'b', 1.0),
              L(quad((40, 98), (45, 95), (50, 98)) + quad((50, 98), (55, 101), (60, 98))[1:], OUTC, 'f', False, False, 1.6)],
    'side': side_cap(top=2, nape=84, front=(84, 48)) + [fr([(66, 52), (72, 50), (72, 76), (66, 72)])],
    'back': back_of([(16, 76), (10, 44), (18, 16), (50, 2), (82, 16), (90, 44)], 84),
}

# Des Tiny: chica de pelo gris pardo con raya en medio, una cinta blanca y turquesa en la frente y dos trenzas que le caen por
# delante de los hombros con gomas azules; ojos turquesa grandes y sonrisa
_BAND2 = (250, 250, 248, 255)
_TEAL = (96, 150, 156, 255)


def _braid(x, y0, y1, w=6, c='mid'):
    out = []
    n = 4
    for i in range(n):
        ya, yb = y0 + (y1 - y0) * i / n, y0 + (y1 - y0) * (i + 1) / n
        out.append(L(blob([(x - w / 2, ya), (x + w / 2, ya), (x + w / 2 + 1, (ya + yb) / 2), (x, yb), (x - w / 2 - 1, (ya + yb) / 2)], 4), c, 'f', ln=True))
    return out


CHARS[T + 'des-tiny'] = {
    'body': 'chica', 'pal': pal('#998869', '#f7b16c', iris='#4a8a90', shade='#715c4a', deep='#544334', tie='#7ab0c8'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': (58, 46)},
    'front': [L(outline([(12, 84), (8, 46), (16, 14), (50, 0), (84, 14), (92, 46), (88, 84), (80, 70), (80, 52), (20, 52), (20, 70)])),
              L(outline([(56, 2), (82, 14), (92, 46), (88, 80), (82, 56)]), 'shade', 'b', False),
              strand([(50, 2), (48, 44)], 'deep', 'b', 1.2),
              L(quad((14, 54), (50, 42), (86, 54)) + quad((86, 60), (50, 48), (14, 60)), _BAND2, 'f', ln=True),
              L(quad((15, 56.5), (50, 45), (85, 56.5)), _TEAL, 'f', False, False, 2.2)]
             + _braid(14, 82, 112) + _braid(86, 82, 112)
             + [L(ell(14, 84, 4.5, 2.6), 'tie', 'f', ln=True), L(ell(86, 84, 4.5, 2.6), 'tie', 'f', ln=True)],
    'side': [L(outline([(78, 54), (88, 40), (82, 12), (56, 0), (28, 4), (8, 22), (2, 50), (6, 78), (20, 88), (34, 86), (42, 64), (58, 56)])),
             L(outline([(3, 46), (30, 48), (40, 62), (34, 84), (20, 88), (6, 76)]), 'shade', 'b', False),
             L(quad((86, 50), (60, 38), (40, 60)) + quad((40, 66), (60, 44), (86, 56)), _BAND2, 'f', ln=True)]
            + _braid(50, 82, 112) + [L(ell(50, 84, 4.5, 2.6), 'tie', 'f', ln=True)],
    'back': [L(outline([(12, 84), (8, 46), (16, 14), (50, 0), (84, 14), (92, 46), (88, 84), (50, 90)])),
             L(outline([(56, 2), (82, 14), (92, 46), (88, 80), (62, 88)]), 'shade', 'b', False),
             strand([(50, 2), (50, 86)], 'deep', 'b', 1.2),
             L(quad((10, 54), (50, 44), (90, 54)) + quad((90, 60), (50, 50), (10, 60)), _BAND2, 'f', ln=True)]
            + _braid(16, 82, 110) + _braid(84, 82, 110),
}

# Dex Territy (portero): pelo rapado gris beige claro, redondo; enfurruñado: ojos redondos verde oliva, cejas enfadadas
# y boca torcida
CHARS[T + 'dex-territy'] = {
    'body': 'normal', 'pal': pal('#cebda5', '#f8b068', iris='#5a5a30', shade='#b0a088', deep='#8c7e6a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94,
             'hairline': [(16, 60), (20, 44), (36, 36), (50, 34), (64, 36), (80, 44), (84, 60)]},
    'front': crop('front', top=6, side=60, w=1, flat=2),
    'side': crop('side', top=4, nape=82, flat=2),
    'back': crop('back', top=6, nape=82, flat=2),
}

# Dexter Ambie: pelo granate anaranjado peinado hacia atrás, liso por arriba y con las puntas abiertas hacia fuera en dos
# alas a la altura de las orejas; ojos afilados grises, ceño fruncido y bigotillos de gato en las mejillas
CHARS[T + 'dexter-ambie'] = {
    'body': 'normal', 'pal': pal('#a33e0b', '#f0b46e', iris='#8a8a6a', shade='#84300a', deep='#6d2b11'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94,
             'hairline': [(16, 66), (18, 50), (30, 42), (50, 38), (70, 42), (82, 50), (84, 66)]},
    'front': [L(outline([(16, 72), (4, 84, 1), (10, 74), (10, 42), (18, 14), (50, 2), (82, 14), (90, 42), (90, 74), (96, 84, 1), (84, 72), (80, 50), (20, 50)])),
              L(outline([(60, 4), (82, 16), (90, 42), (88, 70), (82, 52)]), 'shade', 'b', False)]
             + [strand([(x, 6), (x, 40)], 'deep', 'b', 1.0) for x in (32, 44, 56, 68)]
             + [L([(26, 86), (34, 85)], OUTC, 'f', False, False, 0.9), L([(26, 89), (34, 88)], OUTC, 'f', False, False, 0.9),
                L([(66, 85), (74, 86)], OUTC, 'f', False, False, 0.9), L([(66, 88), (74, 89)], OUTC, 'f', False, False, 0.9)],
    'side': side_cap(top=2, nape=82, front=(84, 44)) + [L(outline([(10, 72), (-2, 86, 1), (16, 80), (28, 84, 1), (24, 74)]), 'mid', 'b'),
                                                       strand([(20, 12), (56, 4), (84, 22)], 'deep', 'b', 1.0)],
    'back': [L(outline([(10, 78), (2, 88, 1), (14, 82), (50, 86), (86, 82), (98, 88, 1), (90, 78), (90, 42), (82, 14), (50, 2), (18, 14), (10, 42)])),
             L(outline([(58, 4), (82, 16), (90, 44), (88, 78), (62, 84)]), 'shade', 'b', False)]
            + [strand([(x, 6), (x, 76)], 'deep', 'b', 1.0) for x in (32, 50, 68)],
}

# Dexter Raleigh: cara alargada y barbilla larga; pelo castaño grisáceo con mechones largos de flequillo que le caen por el
# medio de la cara y los lados abiertos en alas; ojos afilados y media sonrisa
CHARS[T + 'dexter-raleigh'] = {
    'body': 'delgado', 'pal': pal('#b4996d', '#f0b570', iris='#2a2020', shade='#846448', deep='#664932'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False,
             'face_front': blob([(19, 52), (50, 32), (81, 52), (82, 80), (76, 100), (62, 112), (50, 116), (38, 112), (24, 100), (18, 80)])},
    'front': [L(outline([(16, 64), (0, 70, 1), (10, 52), (12, 28), (26, 6), (50, -2), (74, 6), (88, 28), (90, 52), (100, 70, 1), (84, 64), (80, 52), (20, 52)])),
              L(outline([(60, 0), (82, 12), (90, 36), (96, 64), (84, 60), (80, 40)]), 'shade', 'b', False),
              fr([(18, 56), (22, 36), (36, 24), (50, 22), (64, 24), (78, 36), (82, 56), (72, 48), (62, 52), (56, 86, 1), (50, 56), (44, 76, 1), (40, 50), (30, 50)]),
              strand([(50, 26), (54, 60)], 'deep', 'f', 1.0)],
    'side': [L(outline([(76, 52), (88, 42), (86, 16), (64, 0), (34, 0), (12, 14), (2, 40), (-6, 62, 1), (10, 60), (16, 80), (30, 82), (40, 66), (54, 56)])),
             L(outline([(3, 42), (30, 46), (40, 62), (30, 80), (16, 80), (6, 60)]), 'shade', 'b', False),
             fr([(70, 40), (92, 44), (94, 60), (90, 74, 1), (82, 58), (76, 52)])],
    'back': [L(outline([(16, 70), (-2, 74, 1), (10, 54), (12, 28), (26, 6), (50, -2), (74, 6), (88, 28), (90, 54), (102, 74, 1), (84, 72), (76, 84, 1), (64, 78), (50, 86, 1),
                        (36, 78), (24, 84, 1)])),
             L(outline([(58, 0), (82, 12), (90, 40), (98, 70), (64, 80)]), 'shade', 'b', False)],
}

# Dick Turbin: pelo rojo peinado hacia atrás desde la frente, que por detrás de las orejas le baja liso hasta el cuello;
# ojos afilados claros, ceño y boca apretada
CHARS[T + 'dick-turbin'] = {
    'body': 'normal', 'pal': pal('#a82403', '#f0b46e', iris='#b0a070', shade='#812309', deep='#571d0b'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94,
             'hairline': [(16, 70), (18, 52), (30, 44), (50, 40), (70, 44), (82, 52), (84, 70)]},
    'front': [L(outline([(10, 100, 1), (8, 70), (10, 40), (18, 14), (50, 2), (82, 14), (90, 40), (92, 70), (90, 100, 1), (82, 84), (80, 52), (20, 52), (18, 84)])),
              L(outline([(60, 4), (82, 16), (90, 42), (90, 90), (84, 70), (80, 40)]), 'shade', 'b', False)]
             + [strand([(x, 6), (x, 42)], 'deep', 'b', 1.0) for x in (34, 46, 56, 68)],
    'side': [L(outline([(78, 50), (88, 40), (84, 14), (60, 0), (30, 2), (10, 16), (2, 44), (2, 80), (10, 100, 1), (22, 90), (32, 96, 1), (36, 74), (42, 60), (56, 54)])),
             L(outline([(3, 44), (30, 46), (40, 60), (34, 90), (12, 96), (4, 76)]), 'shade', 'b', False),
             strand([(28, 8), (60, 6), (84, 22)], 'deep', 'b', 1.0)],
    'back': [L(outline([(10, 100, 1), (8, 70), (10, 40), (18, 14), (50, 2), (82, 14), (90, 40), (92, 70), (90, 100, 1), (76, 92), (64, 100, 1), (56, 92), (44, 100, 1), (36, 92),
                        (24, 98, 1)])),
             L(outline([(58, 4), (82, 16), (90, 44), (90, 94), (62, 94)]), 'shade', 'b', False)]
            + [strand([(x, 6), (x, 90)], 'deep', 'b', 1.0) for x in (32, 50, 68)],
}

# Django Keyes (portero): pelo crema clarísimo echado todo hacia un lado en un gran tupé que le tapa media frente, con el
# envés pardo rosado; ojos lila, cejas enfadadas y sonrisa
CHARS[T + 'django-keyes'] = {
    'body': 'normal', 'pal': pal('#f4e6c1', '#f0b56f', iris='#a88aa0', shade='#d8c8a0', deep='#917464', under='#9a7a6a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93,
             'hairline': [(16, 72), (18, 52), (28, 44), (44, 40), (58, 46), (70, 50), (82, 50), (84, 64)]},
    'front': [L(outline([(10, 84, 1), (8, 56), (8, 30), (22, 4), (50, -6), (78, 0), (96, 18), (98, 46), (88, 62), (84, 62), (80, 50), (20, 54), (18, 70)])),
              L(outline([(40, 0), (56, 6), (64, 30), (58, 50), (50, 30)]), 'under', 'b', False),
              L(outline([(62, 2), (88, 10), (98, 30), (96, 48), (86, 58), (78, 38)]), 'shade', 'b', False),
              fr([(10, 64), (14, 30), (30, 10), (46, 8), (60, 26), (52, 44), (40, 52), (28, 62), (18, 78, 1)])],
    'side': [L(outline([(80, 54), (94, 46), (98, 24), (82, 2), (54, -8), (26, -2), (8, 16), (2, 44), (4, 72), (14, 88), (28, 86), (38, 66), (54, 56)])),
             L(outline([(3, 44), (30, 46), (40, 62), (28, 86), (14, 86), (6, 70)]), 'deep', 'b', False),
             strand([(30, 0), (70, 6), (94, 30)], 'shade', 'b', 1.2)],
    'back': [L(outline([(10, 84, 1), (8, 56), (8, 30), (22, 4), (50, -6), (78, 0), (96, 18), (96, 46), (90, 84), (50, 90)])),
             L(outline([(60, -2), (84, 8), (96, 24), (94, 50), (88, 82), (62, 88)]), 'shade', 'b', False),
             strand([(30, 4), (60, 10), (90, 30)], 'shade', 'b', 1.2)],
}

# Dom Anding: piel tostada y pelo naranja desgreñado de mechones en punta que le cubren la frente y las orejas; cejas
# naranjas, ojos grandes y labios gruesos
CHARS[T + 'dom-anding'] = {
    'body': 'normal', 'pal': pal('#cd6e20', '#cc914c', iris='#1e1a1a', shade='#a85a1c', deep='#7b380e'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'none', 'nose': (50, 86, 2.6), 'hairline': False},
    'front': [L(outline([(8, 78, 1), (12, 62), (4, 54, 1), (12, 40), (16, 16), (50, 2), (84, 16), (90, 40), (98, 52, 1), (88, 60), (92, 78, 1), (80, 66), (80, 56), (20, 56),
                         (20, 66)])),
              L(outline([(60, 4), (84, 18), (90, 40), (92, 72), (82, 56)]), 'shade', 'b', False),
              fr([(18, 58), (18, 40), (32, 26), (50, 22), (68, 26), (82, 40), (82, 60), (76, 52), (70, 60, 1), (62, 48), (54, 58, 1), (46, 46), (38, 58, 1), (32, 48),
                  (24, 60, 1)]),
              strand([(36, 30), (44, 48)], 'deep', 'f', 1.0), strand([(62, 30), (58, 48)], 'deep', 'f', 1.0)]
             + brows(66, 'mid', 3.0, 14, 0.0, 12)
             + [L(blob([(40, 95), (46, 92), (50, 93), (54, 92), (60, 95), (56, 100), (50, 101), (44, 100)], 5), (159, 90, 40, 255), 'f', ln=True),
                L([(41, 95.5), (59, 95.5)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(76, 54), (90, 52), (84, 62, 1), (92, 40), (84, 14), (60, 0), (30, 2), (10, 18), (2, 46), (6, 74), (12, 86, 1), (22, 78), (30, 88, 1), (34, 72),
                        (42, 60), (56, 56)])),
             L(outline([(3, 44), (30, 46), (40, 60), (32, 80), (14, 84), (6, 70)]), 'shade', 'b', False)]
            + brow_side(66, 'mid', 3.0),
    'back': [L(outline([(8, 80, 1), (12, 62), (4, 54, 1), (12, 40), (16, 16), (50, 2), (84, 16), (90, 40), (98, 52, 1), (88, 62), (92, 80, 1), (76, 82), (66, 92, 1), (58, 82),
                        (50, 92, 1), (42, 82), (34, 92, 1), (24, 82)])),
             L(outline([(58, 4), (84, 18), (90, 44), (90, 78), (62, 84)]), 'shade', 'b', False)],
}

# Dom Ittory (portero): una lámina de pelo rosa rojizo echada por encima de la cabeza hacia un lado, que cae en punta junto
# a la oreja, y debajo pelo castaño oscuro largo que se abre en puntas a la altura del cuello; ojos cerrados de felicidad
# y sonrisa
CHARS[T + 'dom-ittory'] = {
    'body': 'normal', 'pal': pal('#c47163', '#f0b56e', iris='#2a2020', shade='#9e564a', deep='#7a3e34', dark='#443122', dark_d='#2e2016'),
    'face': {'eyes': 'closed', 'brows': True, 'mouth': 'smile', 'mouth_y': 93, 'nose': (50, 86, 2.4),
             'hairline': [(16, 76), (18, 54), (30, 46), (50, 40), (70, 40), (82, 50), (84, 70)]},
    'front': [L(outline([(16, 74), (-2, 96, 1), (8, 74), (10, 42), (20, 20), (80, 20), (90, 42), (92, 74), (102, 96, 1), (84, 80), (80, 56), (20, 56)]), 'dark'),
              L(outline([(20, 50), (22, 24), (40, 4), (64, 0), (84, 8), (94, 26), (98, 54), (102, 72, 1), (88, 58), (84, 44), (70, 40), (50, 40), (30, 46)])),
              L(outline([(64, 2), (86, 10), (96, 32), (100, 68), (88, 52), (84, 32)]), 'shade', 'b', False),
              strand([(30, 30), (60, 14), (92, 30)], 'deep', 'b', 1.0)],
    'side': [L(outline([(36, 66), (24, 86), (14, 100, 1), (8, 80), (2, 50), (10, 24), (30, 14), (50, 30), (44, 54)]), 'dark'),
             L(outline([(76, 46), (90, 40), (92, 16), (72, 0), (40, -2), (16, 10), (4, 34), (14, 40), (34, 40), (50, 46), (58, 50)])),
             strand([(16, 16), (50, 4), (88, 22)], 'deep', 'b', 1.0)],
    'back': [L(outline([(10, 74), (-2, 96, 1), (12, 84), (30, 90), (50, 86), (70, 90), (88, 84), (102, 96, 1), (90, 74), (90, 40), (80, 20), (20, 20), (10, 40)]), 'dark'),
             L(outline([(14, 50), (16, 24), (36, 4), (64, 0), (86, 10), (96, 30), (98, 56), (84, 54), (50, 52)])),
             L(outline([(60, 2), (86, 12), (96, 32), (96, 54), (70, 52)]), 'shade', 'b', False)],
}

# Don Keys: melena corta lila grisácea en forma de casco, con flequillo recto que le llega a las cejas; ojos cerrados
# apretados y boca seria
CHARS[T + 'don-keys'] = {
    'body': 'normal', 'pal': pal('#7f7183', '#efb46e', iris='#2a2020', shade='#6d5d67', deep='#59454b'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'frown', 'mouth_y': 94, 'hairline': False, 'ears': False},
    'front': [L(outline([(8, 92), (6, 50), (14, 16), (50, 2), (86, 16), (94, 50), (92, 92), (80, 92), (80, 64), (20, 64), (20, 92)])),
              L(outline([(60, 4), (84, 16), (94, 50), (92, 90), (82, 88), (84, 50)]), 'shade', 'b', False),
              fr([(16, 66), (16, 40), (30, 24), (50, 20), (70, 24), (84, 40), (84, 66)]),
              strand([(32, 30), (32, 64)], 'deep', 'f', 0.9), strand([(50, 24), (50, 64)], 'deep', 'f', 0.9), strand([(68, 30), (68, 64)], 'deep', 'f', 0.9),
              L([(30, 74), (40, 77), (30, 80)], OUTC, 'f', False, False, 2.0), L([(70, 74), (60, 77), (70, 80)], OUTC, 'f', False, False, 2.0)],
    'side': [L(outline([(88, 62), (92, 40), (84, 12), (58, 0), (28, 4), (8, 22), (2, 50), (4, 90), (40, 94), (54, 92), (54, 66), (70, 62)])),
             L(outline([(3, 46), (34, 48), (46, 66), (46, 92), (6, 90)]), 'shade', 'b', False),
             L([(84, 74), (78, 77), (84, 80)], OUTC, 'f', False, False, 2.0)],
    'back': [L(outline([(8, 92), (6, 50), (14, 16), (50, 2), (86, 16), (94, 50), (92, 92), (50, 96)])),
             L(outline([(58, 4), (84, 16), (94, 50), (92, 90), (62, 94)]), 'shade', 'b', False)],
}

# Don Paolo: un mafioso adulto con sombrero de ala ancha marrón oscuro, gafas redondas, bigote y perilla oscuros
_HAT = (59, 42, 29, 255)
_HAT_D = (40, 28, 20, 255)
_HATBAND = (100, 40, 28, 255)
CHARS[T + 'don-paolo'] = {
    'body': 'normal', 'pal': pal('#3b2a1d', '#d8ae88', iris='#2a2020', shade='#2a1e14', deep='#1e140e'),
    'face': {'eyes': 'dot', 'brows': True, 'mouth': 'none', 'nose': (50, 86, 3.6), 'hairline': False, 'glasses': (40, 30, 26, 255)},
    'front': [L(outline([(16, 70), (14, 52), (86, 52), (84, 70), (80, 60), (20, 60)])),
              L(outline([(-12, 52), (-4, 42), (20, 40), (24, 14), (38, 0), (62, 0), (76, 14), (80, 40), (104, 42), (112, 52), (86, 54), (50, 56), (14, 54)]), _HAT, 'f'),
              L(outline([(56, 2), (74, 14), (78, 40), (60, 40)]), _HAT_D, 'f', False),
              L([(21, 32), (79, 32), (80, 40), (20, 40)], _HATBAND, 'f', False),
              L(blob([(36, 92), (44, 89), (50, 91), (56, 89), (64, 92), (58, 94), (50, 93), (42, 94)], 5), 'mid', 'f', False),
              L(blob([(44, 99), (56, 99), (54, 108), (50, 110), (46, 108)], 5), 'mid', 'f', False)],
    'side': [L(outline([(56, 58), (60, 50), (8, 50), (2, 70), (12, 82), (30, 80), (40, 66)])),
             L(outline([(-6, 50), (4, 40), (16, 38), (20, 12), (40, -2), (66, 0), (80, 14), (82, 38), (100, 40), (108, 50), (86, 54), (50, 54), (14, 54)]), _HAT, 'f'),
             L([(18, 30), (82, 30), (82, 38), (16, 38)], _HATBAND, 'f', False),
             L(blob([(80, 91), (90, 89), (90, 94), (82, 94)], 4), 'mid', 'f', False), L(blob([(78, 99), (88, 99), (86, 108), (80, 108)], 4), 'mid', 'f', False)],
    'back': [L(outline([(16, 84), (12, 54), (88, 54), (84, 84), (50, 90)])),
             L(outline([(-12, 52), (-4, 42), (20, 40), (24, 14), (38, 0), (62, 0), (76, 14), (80, 40), (104, 42), (112, 52), (86, 56), (50, 58), (14, 56)]), _HAT, 'f'),
             L([(21, 32), (79, 32), (80, 40), (20, 40)], _HATBAND, 'f', False)],
}

# Don Ringo (portero): pelo verde crema pálido, despeinado y de mechones largos que le tapan la frente y bajan por los lados;
# ojos entornados y media sonrisa
CHARS[T + 'don-ringo'] = {
    'body': 'normal', 'pal': pal('#dbdda7', '#f0c08a', iris='#4a4030', shade='#b8ba86', deep='#909068'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 93, 'hairline': False},
    'front': [L(outline([(8, 90, 1), (10, 64), (2, 50, 1), (12, 40), (14, 14), (32, 0), (50, 4), (70, -2), (88, 14), (90, 40), (100, 50, 1), (90, 62), (92, 90, 1), (80, 72),
                         (80, 56), (20, 56), (20, 72)])),
              L(outline([(60, 2), (84, 14), (90, 40), (92, 84), (82, 60)]), 'shade', 'b', False),
              fr([(16, 64), (16, 40), (30, 24), (50, 20), (70, 24), (84, 40), (84, 64), (76, 54), (68, 66, 1), (62, 50), (52, 70, 1), (48, 48), (38, 64, 1), (32, 50),
                  (24, 62, 1)]),
              strand([(44, 24), (48, 58)], 'deep', 'f', 1.0), strand([(64, 28), (62, 52)], 'deep', 'f', 1.0)],
    'side': [L(outline([(76, 54), (92, 52), (86, 64, 1), (94, 40), (84, 12), (58, -2), (28, 2), (8, 20), (0, 48), (4, 78), (10, 92, 1), (20, 82), (30, 92, 1), (34, 72),
                        (42, 60), (56, 56)])),
             L(outline([(3, 46), (30, 48), (40, 62), (30, 84), (12, 88), (6, 72)]), 'shade', 'b', False)],
    'back': [L(outline([(8, 90, 1), (10, 64), (2, 50, 1), (12, 40), (14, 14), (32, 0), (50, 4), (70, -2), (88, 14), (90, 40), (100, 50, 1), (90, 62), (92, 90, 1), (76, 84),
                        (66, 94, 1), (58, 84), (50, 94, 1), (42, 84), (34, 94, 1), (24, 84)])),
             L(outline([(58, 2), (84, 14), (90, 44), (92, 84), (62, 86)]), 'shade', 'b', False)],
}

# Don Snow (portero): calvo de piel tostada con un mechón verde plano en lo alto como una magdalena y una estrella amarilla
# pintada en la frente; cejas verdes gruesas y sonrisa
_STAR = (238, 196, 40, 255)


def _star5(x, y, r):
    import math
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((x + rr * math.cos(a), y + rr * math.sin(a)))
    return pts


CHARS[T + 'don-snow'] = {
    'body': 'normal', 'pal': pal('#98b95e', '#ce9346', iris='#2a2020', shade='#7a9648', deep='#5a6e34'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'nose': (50, 86, 3.4), 'hairline': False},
    'front': [L(outline([(19, 62), (16, 36), (28, 14), (50, 8), (72, 14), (84, 36), (81, 62)]), 'skin'),
              L(outline([(34, 14), (30, -6), (36, -16), (50, -18), (64, -16), (70, -6), (66, 14), (50, 18)])),
              L(outline([(54, -16), (64, -16), (70, -6), (66, 14), (56, 16)]), 'shade', 'b', False)]
             + [strand([(x, -14), (x, 14)], 'deep', 'b', 0.9) for x in (40, 50, 60)]
             + [L(_star5(50, 48, 9), _STAR, 'f', ln=True)] + brows(64, 'mid', 4.5, 14, 0.2, 12),
    'side': [L(outline([(54, 30), (50, 8), (56, -4), (70, -6), (82, -2), (84, 10), (76, 30), (64, 32)])),
             L(outline([(70, -6), (82, -2), (84, 10), (76, 30), (70, 30)]), 'shade', 'b', False)]
            + brow_side(64, 'mid', 4.5, 0.2),
    'back': [L(outline([(34, 22), (30, 0), (36, -12), (50, -14), (64, -12), (70, 0), (66, 22), (50, 26)])),
             L(outline([(54, -12), (64, -12), (70, 0), (66, 22), (56, 24)]), 'shade', 'b', False)],
}

# Doug Leepearson-Gaze: grandote de cara redonda; pelo azul marino pegado hacia atrás con los lados rapados y una coleta
# trenzada que le sale hacia un lado; ojos blancos de enfado y dientes apretados
CHARS[T + 'doug-leepearson-gaze'] = {
    'body': 'corpulento', 'pal': pal('#394e64', '#efb56e', iris='#f2f2f2', shade='#2a3a4c', deep='#1e2a38', shaved='#b8906a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98, 'eye_y': 78, 'nose': (50, 88, 2.8),
             'hairline': [(14, 62), (18, 44), (34, 36), (50, 34), (66, 36), (82, 44), (86, 62)],
             'face_front': blob([(14, 52), (50, 34), (86, 52), (92, 80), (84, 102), (64, 112), (50, 114), (36, 112), (16, 102), (8, 80)])},
    'front': [L(outline([(15, 62), (14, 40), (24, 18), (50, 10), (76, 18), (86, 40), (85, 62), (80, 50), (20, 50)]), 'shaved'),
              L(outline([(26, 40), (28, 18), (50, 8), (72, 18), (74, 40), (60, 34), (40, 34)])),
              L(outline([(56, 10), (72, 18), (74, 40), (62, 34)]), 'shade', 'b', False),
              L(outline([(78, 28), (92, 30), (104, 40), (100, 46), (90, 38)]), 'mid', 'b'),
              L(ell(102, 46, 4, 4), 'mid', 'f', ln=True), L(ell(104, 53, 3.5, 3.5), 'mid', 'f', ln=True),
              L(ell(106, 60, 3, 3), 'mid', 'f', ln=True), L(ell(106, 64, 2, 1.4), (230, 200, 60, 255), 'f', False)],
    'side': [L(outline([(76, 46), (86, 40), (86, 18), (64, 4), (34, 4), (12, 18), (4, 42), (8, 66), (20, 80), (36, 78), (42, 60), (58, 50)]), 'shaved'),
             L(outline([(84, 26), (70, 6), (40, 2), (16, 14), (10, 30), (30, 24), (60, 22)])),
             L(ell(10, 34, 5, 5), 'mid', 'f', ln=True), L(ell(4, 42, 4.5, 4.5), 'mid', 'f', ln=True), L(ell(0, 50, 4, 4), 'mid', 'f', ln=True),
             L(ell(-2, 57, 3.5, 3.5), 'mid', 'f', ln=True)],
    'back': [L(outline([(15, 80), (12, 44), (22, 18), (50, 10), (78, 18), (88, 44), (85, 80), (50, 86)]), 'shaved'),
             L(outline([(26, 50), (28, 20), (50, 8), (72, 20), (74, 50), (50, 56)])),
             L(outline([(56, 10), (72, 20), (74, 50), (60, 54)]), 'shade', 'b', False),
             L(ell(50, 58, 5, 5), 'mid', 'f', ln=True), L(ell(56, 66, 4.5, 4.5), 'mid', 'f', ln=True), L(ell(64, 72, 4, 4), 'mid', 'f', ln=True),
             L(ell(72, 76, 3.5, 3.5), 'mid', 'f', ln=True), L(ell(77, 78, 2, 1.4), (230, 200, 60, 255), 'f', False)],
}

# Doug Outon: casco de pelo naranja con un flequillo largo de mechones que le cruza la cara y le tapa medio ojo; ceño
# fruncido y boca apretada
CHARS[T + 'doug-outon'] = {
    'body': 'normal', 'pal': pal('#d5751a', '#efb470', iris='#2a2020', shade='#a55017', deep='#7a3813'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': False},
    'front': [L(outline([(12, 80), (8, 46), (16, 14), (50, 0), (84, 14), (92, 46), (88, 80), (80, 66), (80, 56), (20, 56), (20, 66)])),
              L(outline([(60, 2), (84, 14), (92, 46), (88, 76), (82, 56)]), 'shade', 'b', False),
              fr([(16, 66), (16, 40), (30, 22), (50, 18), (70, 22), (84, 40), (84, 66), (78, 54), (70, 64, 1), (64, 52), (54, 84, 1), (48, 56), (40, 62, 1), (34, 52),
                  (24, 62, 1)]),
              strand([(42, 24), (54, 76)], 'deep', 'f', 1.0), strand([(60, 26), (66, 56)], 'deep', 'f', 1.0)],
    'side': [L(outline([(76, 54), (92, 48), (90, 64, 1), (92, 36), (84, 12), (58, -2), (28, 2), (8, 20), (2, 48), (6, 74), (18, 86), (32, 84), (40, 64), (56, 56)])),
             L(outline([(3, 46), (30, 48), (40, 62), (32, 84), (18, 86), (6, 72)]), 'shade', 'b', False)],
    'back': back_of([(12, 76), (8, 44), (16, 14), (50, 0), (84, 14), (92, 44)], 86),
}


def skull(view='front'):
    """Cabeza calva más alta que la cara (para los rapados y los que solo tienen pelo en los lados)."""
    if view == 'side':
        return [L(outline([(58, 54), (86, 44), (88, 22), (70, 6), (44, 4), (20, 14), (8, 34), (6, 60), (20, 80), (40, 76)]), 'skin')]
    return [L(outline([(19, 62), (16, 36), (28, 14), (50, 8), (72, 14), (84, 36), (81, 62)]), 'skin')]


# Doug Walker (portero): grandote de cara ancha y frente despejada, con el pelo lila grisáceo rapado solo en lo alto y los
# lados; párpados caídos de ojos morados y sonrisa tranquila
CHARS[T + 'doug-walker'] = {
    'body': 'corpulento', 'pal': pal('#a898b0', '#f0b268', iris='#6a5a8a', shade='#887890', deep='#685870'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 96,
             'hairline': [(16, 52), (20, 34), (32, 26), (50, 28), (68, 26), (80, 34), (84, 52)],
             'face_front': blob([(16, 50), (50, 30), (84, 50), (90, 78), (84, 100), (64, 110), (50, 112), (36, 110), (16, 100), (10, 78)])},
    'front': crop('front', top=14, side=52, w=0, flat=4),
    'side': crop('side', top=12, nape=80, flat=4),
    'back': crop('back', top=14, nape=80, flat=4),
}

# Dougie McFlea: pelo verde azulado de pinchos afilados que salen hacia arriba y los lados; cara flaca de nariz larga, ojos
# afilados y sonrisa torcida
CHARS[T + 'dougie-mcflea'] = {
    'body': 'delgado', 'pal': pal('#5b877d', '#efb570', iris='#2a2020', shade='#4a6e66', deep='#3a524c'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': [(16, 66), (20, 50), (32, 44), (42, 52), (50, 40), (60, 50), (70, 44), (82, 50), (84, 66)]},
    'front': messy('front', amp=24, n=9, seed=12, lo=64, sweep=0.15)
             + [L([(50, 80), (46, 90), (52, 91)], OUTC, 'f', False, False, 1.0)],
    'side': messy('side', amp=24, n=9, seed=12, nape=86, sweep=0.3),
    'back': messy('back', amp=24, n=9, seed=12, nape=86),
}

# Drew Crenshaw: calvo por arriba, con el pelo verde azulado solo en los lados y la nuca y una mancha en zigzag en la
# coronilla; gafas redondas negras, cejas de preocupación y boca triste
CHARS[T + 'drew-crenshaw'] = {
    'body': 'normal', 'pal': pal('#58877e', '#efb46f', iris='#2a2020', shade='#466c64', deep='#34504a', lens='#f2e8d0'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'frown', 'mouth_y': 95, 'hairline': False},
    'front': skull()
             + [L(outline([(19, 66), (15, 44), (20, 26), (30, 20), (28, 44), (24, 66)])), L(outline([(81, 66), (85, 44), (80, 26), (70, 20), (72, 44), (76, 66)])),
                L(outline([(56, 10), (64, 16), (60, 22), (70, 24), (72, 30), (64, 30), (62, 22), (54, 18)])),
                L(ell(36, 76, 7.5, 7.0), 'lens', 'f', False), L(ell(64, 76, 7.5, 7.0), 'lens', 'f', False)]
             + ring_glasses('front', 76, BLACK, 2.0, 7.5, 7.0, 14)
             + [L(ell(36, 76, 2.4, 2.6), BLACK, 'f', False), L(ell(64, 76, 2.4, 2.6), BLACK, 'f', False),
                L([(28, 64), (40, 62)], 'mid', 'f', False, False, 2.4), L([(60, 62), (72, 64)], 'mid', 'f', False, False, 2.4)],
    'side': skull('side')
            + [L(outline([(40, 60), (24, 70), (12, 76), (4, 56), (8, 32), (20, 20), (34, 28), (40, 46)])),
               L(ell(82, 76, 4.5, 6.5), 'lens', 'f', False)]
            + ring_glasses('side', 76, BLACK, 2.0, 4.5, 6.5) + [L(ell(83, 76, 1.8, 2.4), BLACK, 'f', False)],
    'back': [L(outline([(16, 80), (12, 50), (20, 28), (30, 22), (50, 30), (70, 22), (80, 28), (88, 50), (84, 80), (50, 86)])),
             L(outline([(60, 28), (80, 30), (88, 52), (84, 78), (62, 84)]), 'shade', 'b', False),
             L(outline([(40, 30), (34, 14), (50, 8), (66, 14), (60, 30), (50, 34)]), 'skin', 'b', False),
             L(outline([(44, 16), (52, 20), (48, 26), (58, 28), (60, 32), (52, 32), (50, 26), (42, 22)]))],
}

# Drew Faxon: pelo naranja salvaje de pinchos en todas direcciones; nariz redonda naranja, ojos afilados y sonrisa
CHARS[T + 'drew-faxon'] = {
    'body': 'normal', 'pal': pal('#d67717', '#f0b56f', iris='#2a2020', shade='#ad5e16', deep='#8a4a12', nose='#e8783a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'nose': (50, 86, 3.6),
             'hairline': [(16, 64), (20, 50), (30, 44), (40, 52), (50, 42), (60, 52), (70, 44), (80, 50), (84, 64)]},
    'front': messy('front', amp=20, n=12, seed=21, lo=66, sweep=-0.1),
    'side': messy('side', amp=20, n=12, seed=21, nape=88, sweep=0.25),
    'back': messy('back', amp=20, n=12, seed=21, nape=88),
}

# Drew Reiner: pelo amarillo ondulado y abultado que se hincha a los lados; cejas enfadadas y sonrisa
CHARS[T + 'drew-reiner'] = {
    'body': 'normal', 'pal': pal('#dfbd17', '#f0b56f', iris='#2a2020', shade='#b8961a', deep='#96671a'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93,
             'hairline': [(16, 66), (20, 52), (34, 46), (48, 54), (60, 44), (74, 48), (82, 54), (84, 66)]},
    'front': [L(outline([(14, 68), (4, 56), (8, 36), (6, 20), (22, 6), (40, 0), (56, 4), (74, -2), (90, 10), (94, 30), (98, 50), (88, 68), (80, 54), (20, 54)])),
              L(outline([(60, 2), (80, 0), (92, 14), (96, 46), (88, 64), (80, 40), (72, 18)]), 'shade', 'b', False),
              strand([(24, 22), (34, 12), (48, 14)], 'deep', 'b', 1.0), strand([(56, 18), (70, 10), (84, 18)], 'deep', 'b', 1.0),
              strand([(14, 44), (24, 38), (32, 42)], 'deep', 'b', 1.0), strand([(70, 38), (80, 34), (88, 40)], 'deep', 'b', 1.0)],
    'side': [L(outline([(76, 54), (88, 50), (94, 34), (88, 14), (64, -2), (36, 0), (12, 12), (0, 34), (2, 60), (10, 78), (24, 84), (36, 78), (42, 62), (58, 56)])),
             L(outline([(2, 44), (30, 48), (40, 62), (34, 78), (22, 84), (8, 72)]), 'shade', 'b', False),
             strand([(20, 14), (40, 8), (56, 14)], 'deep', 'b', 1.0), strand([(60, 10), (76, 8), (88, 20)], 'deep', 'b', 1.0)],
    'back': [L(outline([(12, 80), (4, 60), (8, 36), (6, 20), (22, 6), (40, 0), (56, 4), (74, -2), (90, 10), (94, 30), (98, 54), (88, 80), (50, 86)])),
             L(outline([(58, 2), (80, 0), (92, 14), (96, 50), (88, 78), (62, 84)]), 'shade', 'b', False),
             strand([(24, 30), (40, 24), (56, 30)], 'deep', 'b', 1.0), strand([(30, 56), (50, 50), (70, 56)], 'deep', 'b', 1.0)],
}

# Drew Strait-Straitedge (portero): adulto de cara larga y nariz grande; pelo verde salvia corto peinado hacia atrás con un
# rizo en lo alto y dos picos como cuernos a los lados; ojos de párpado caído y boca recta
_HORN = (196, 150, 110, 255)
CHARS[T + 'drew-strait-straitedge'] = {
    'body': 'normal', 'pal': pal('#b0b47a', '#fab068', iris='#2a2020', shade='#8e925e', deep='#6e7046'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'line', 'mouth_y': 98, 'nose': (50, 88, 4.4), 'hairline': [(17, 66), (19, 44), (34, 36), (50, 34), (66, 36), (81, 44), (83, 66)],
             'face_front': blob([(18, 50), (50, 30), (82, 50), (84, 80), (80, 100), (64, 114), (50, 117), (36, 114), (20, 100), (16, 80)])},
    'front': crop('front', top=6, side=66, w=0)
             + [L(outline([(22, 20), (14, 0, 1), (28, 14)]), _HORN, 'b'), L(outline([(78, 20), (86, 0, 1), (72, 14)]), _HORN, 'b'),
                L(outline([(14, 50), (6, 46, 1), (14, 40)]), 'mid', 'b'), L(outline([(86, 50), (94, 46, 1), (86, 40)]), 'mid', 'b'),
                L(quad((42, 10), (52, -2), (60, 10)) + quad((60, 10), (54, 14), (48, 10))[1:], 'mid', 'b', ln=True),
                strand([(46, 12), (50, 30)], 'deep', 'b', 1.0)],
    'side': crop('side', top=4, nape=84) + [L(outline([(48, 10), (44, -10, 1), (56, 4)]), _HORN, 'b'),
                                          L(quad((50, 8), (62, -4), (72, 10)), 'mid', 'b', False, False, 3.0)],
    'back': crop('back', top=6, nape=84) + [L(outline([(22, 22), (14, 2, 1), (28, 16)]), _HORN, 'b'), L(outline([(78, 22), (86, 2, 1), (72, 16)]), _HORN, 'b')],
}

# Drew Straws: piel tostada; pelo azul marino en una llama de pinchos que sube muy alta, y cejas gruesas azules en punta;
# ojos afilados y media sonrisa
CHARS[T + 'drew-straws'] = {
    'body': 'normal', 'pal': pal('#3b5065', '#cc914b', iris='#2a2020', shade='#2e3e50', deep='#222e3c'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'nose': (50, 86, 3.4),
             'hairline': [(16, 66), (18, 50), (30, 42), (50, 38), (70, 42), (82, 50), (84, 66)]},
    'front': [L(outline([(16, 66), (10, 40), (12, 14), (20, -14, 1), (28, 0), (34, -30, 1), (44, -6), (50, -36, 1), (56, -6), (66, -30, 1), (72, 0), (80, -14, 1), (88, 14),
                         (90, 40), (84, 66), (80, 50), (20, 50)])),
              L(outline([(56, -6), (66, -30), (72, 0), (80, -14), (88, 14), (90, 40), (84, 60), (76, 30)]), 'shade', 'b', False)]
             + [strand([(x, -10), (x, 36)], 'deep', 'b', 1.0) for x in (30, 42, 58, 70)]
             + [L(outline([(24, 66), (30, 62), (42, 62), (46, 66), (40, 68), (34, 66), (28, 70, 1)]), 'mid', 'f', False),
                L(outline([(76, 66), (70, 62), (58, 62), (54, 66), (60, 68), (66, 66), (72, 70, 1)]), 'mid', 'f', False)],
    'side': [L(outline([(76, 50), (86, 44), (90, 22), (98, 4, 1), (82, 6), (86, -18, 1), (68, -6), (66, -34, 1), (52, -8), (40, -30, 1), (32, -2), (14, -14, 1), (16, 12),
                        (4, 34), (4, 62), (16, 80), (32, 80), (40, 64), (54, 54)])),
             L(outline([(5, 40), (30, 44), (40, 62), (32, 78), (16, 80), (8, 66)]), 'shade', 'b', False),
             L(outline([(72, 64), (78, 61), (88, 63), (84, 67), (76, 68, 1)]), 'mid', 'f', False)],
    'back': [L(outline([(16, 80), (10, 40), (12, 14), (20, -14, 1), (28, 0), (34, -30, 1), (44, -6), (50, -36, 1), (56, -6), (66, -30, 1), (72, 0), (80, -14, 1), (88, 14),
                        (90, 40), (84, 80), (50, 86)])),
             L(outline([(56, -6), (66, -30), (72, 0), (80, -14), (88, 14), (90, 40), (84, 78), (62, 84)]), 'shade', 'b', False)]
            + [strand([(x, -10), (x, 70)], 'deep', 'b', 1.0) for x in (32, 50, 68)],
}

# Duncan Jump: grandote de cara ancha y nariz grande; pelo morado oscuro corto peinado hacia atrás con las patillas en
# punta hacia fuera; ojos amarillentos afilados y media sonrisa
CHARS[T + 'duncan-jump'] = {
    'body': 'corpulento', 'pal': pal('#594a5f', '#f0b56e', iris='#c8b850', shade='#42353c', deep='#362622'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 97, 'nose': (50, 87, 4.4),
             'hairline': [(16, 66), (18, 50), (30, 42), (50, 38), (70, 42), (82, 50), (84, 66)],
             'face_front': blob([(16, 50), (50, 30), (84, 50), (90, 78), (84, 100), (64, 110), (50, 112), (36, 110), (16, 100), (10, 78)])},
    'front': crop('front', top=6, side=66, w=1)
             + [L(outline([(17, 62), (8, 72, 1), (16, 72)]), 'mid', 'b'), L(outline([(83, 62), (92, 72, 1), (84, 72)]), 'mid', 'b')],
    'side': crop('side', top=4, nape=84, w=1) + [L(outline([(62, 56), (60, 74, 1), (66, 60)]), 'mid', 'f')],
    'back': crop('back', top=6, nape=84, w=1),
}

# Dusky Sunfield: piel oscura; pelo morado oscuro muy corto con un pico que asoma a un lado; párpados caídos de ojos
# morados y labios gruesos oscuros
CHARS[T + 'dusky-sunfield'] = {
    'body': 'normal', 'pal': pal('#5d4d63', '#bb7b43', iris='#5a4a7a', shade='#4a3c50', deep='#382c3e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'nose': (50, 86, 3.0),
             'hairline': [(16, 62), (20, 46), (34, 40), (50, 38), (66, 40), (80, 46), (84, 62)]},
    'front': crop('front', top=4, side=62, w=0) + [L(outline([(66, 16), (72, 0, 1), (74, 18)]), 'mid', 'b'),
                                                L(blob([(40, 95), (50, 93), (60, 95), (56, 99), (44, 99)], 5), (110, 60, 40, 255), 'f', ln=True)],
    'side': crop('side', top=2, nape=84) + [L(outline([(70, 10), (80, -4, 1), (78, 14)]), 'mid', 'b'),
                                          L(blob([(82, 94), (88, 93), (88, 98), (82, 98)], 4), (110, 60, 40, 255), 'f', False)],
    'back': crop('back', top=4, nape=84) + [L(outline([(28, 16), (22, 0, 1), (34, 14)]), 'mid', 'b')],
}

# Dustin Westend: pelo de dos colores: los lados y la nuca verde muy oscuro rapados, y por arriba un tupé granate pardo
# peinado hacia un lado que acaba en una punta levantada; piel clara, ojos azul grisáceo y sonrisa
CHARS[T + 'dustin-westend'] = {
    'body': 'normal', 'pal': pal('#6b4c4f', '#f8d5a0', iris='#6a7a90', shade='#543235', deep='#402628', side='#27382e'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92,
             'hairline': [(16, 64), (18, 48), (30, 42), (50, 40), (70, 42), (82, 48), (84, 64)]},
    'front': crop('front', top=6, side=64, c='side', shade=False)
             + [L(outline([(24, 30), (26, 10), (44, -2), (70, -2), (90, 6), (104, 0, 1), (96, 16), (86, 26), (66, 32), (44, 36)])),
                L(outline([(60, 0), (90, 8), (102, 2), (94, 18), (80, 28), (66, 24)]), 'shade', 'b', False),
                strand([(34, 14), (60, 6), (88, 14)], 'deep', 'b', 1.0)],
    'side': crop('side', top=4, nape=84, c='side', shade=False)
            + [L(outline([(28, 22), (34, 4), (56, -6), (80, -2), (98, 2), (106, -6, 1), (100, 12), (88, 26), (64, 26), (44, 28)])),
               strand([(40, 10), (70, 4), (96, 10)], 'deep', 'b', 1.0)],
    'back': crop('back', top=6, nape=84, c='side', shade=False)
            + [L(outline([(26, 34), (24, 12), (44, -2), (70, -2), (86, 8), (90, 30), (70, 38), (44, 38)])),
               L(outline([(60, 0), (84, 10), (90, 30), (72, 36)]), 'shade', 'b', False)],
}

# Dusty Rellicks: capucha amarilla que le envuelve la cabeza, con el pelo amarillo pegado asomando en franjas por la frente;
# ojos de punto, cejas enfadadas, boca torcida y una cicatriz en cruz en la mejilla
_HOOD = (217, 182, 27, 255)
_HOOD_D = (164, 115, 25, 255)
CHARS[T + 'dusty-rellicks'] = {
    'body': 'normal', 'pal': pal('#c8a020', '#f0b56e', iris='#2a2020', shade='#a47319', deep='#7c5013'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'ears': False, 'hairline': False},
    'front': [L(outline([(8, 104), (4, 60), (10, 24), (28, 2), (50, -4), (72, 2), (90, 24), (96, 60), (92, 104), (82, 104), (84, 70), (80, 52), (20, 52), (16, 70),
                         (18, 104)]), _HOOD),
              L(outline([(60, -2), (84, 12), (96, 50), (92, 100), (84, 100), (86, 60)]), _HOOD_D, 'b', False),
              fr([(18, 62), (20, 44), (34, 36), (50, 34), (66, 36), (80, 44), (82, 62), (66, 56), (50, 56), (34, 56)]),
              strand([(24, 48), (50, 42), (76, 48)], 'deep', 'f', 1.2),
              L([(64, 86), (74, 94)], OUTC, 'f', False, False, 1.2), L([(64, 94), (73, 85)], OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(80, 50), (88, 38), (84, 12), (60, -6), (30, -4), (8, 14), (0, 50), (4, 90), (16, 108), (40, 108), (52, 90), (56, 66), (66, 54)]), _HOOD),
             L(outline([(2, 50), (30, 52), (44, 70), (40, 104), (14, 104), (4, 80)]), _HOOD_D, 'b', False),
             fr([(68, 56), (86, 44), (90, 56), (86, 62), (74, 62)])],
    'back': [L(outline([(8, 104), (4, 60), (10, 24), (28, 2), (50, -4), (72, 2), (90, 24), (96, 60), (92, 104), (50, 108)]), _HOOD),
             L(outline([(60, -2), (84, 12), (96, 50), (92, 102), (62, 106)]), _HOOD_D, 'b', False),
             strand([(50, 0), (50, 104)], _HOOD_D, 'b', 1.0)],
}

# Dwayne Woo: cara pálida como de payaso, con rayas moradas bajo los ojos; pelo rojo anaranjado recogido en una coleta alta
# que sale de lo alto de la cabeza y cae curvada hacia un lado; ojos blancos entornados y sonrisa torcida
CHARS[T + 'dwayne-woo'] = {
    'body': 'delgado', 'pal': pal('#a8410b', '#e4d4be', iris='#f2f2f2', shade='#7b2c09', deep='#5a2008', paint='#7a5a8a', tie='#e8c040'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'nose': (50, 86, 2.8),
             'hairline': [(16, 60), (20, 44), (34, 34), (50, 30), (66, 34), (80, 44), (84, 60)]},
    'front': crop('front', top=6, side=60)
             + [L(outline([(44, 8), (40, -14), (30, -24, 1), (46, -20), (54, -30, 1), (60, -18), (80, -10), (94, 6), (100, 30), (102, 64, 1), (92, 34), (82, 14), (60, 2)])),
                L(outline([(80, -8), (94, 6), (100, 30), (102, 62), (90, 30)]), 'shade', 'b', False),
                L(ell(52, 4, 4, 3), 'tie', 'f', ln=True),
                L([(34, 80), (32, 92)], 'paint', 'f', False, False, 1.4), L([(38, 80), (37, 90)], 'paint', 'f', False, False, 1.2),
                L([(66, 80), (68, 92)], 'paint', 'f', False, False, 1.4), L([(62, 80), (63, 90)], 'paint', 'f', False, False, 1.2)],
    'side': crop('side', top=4, nape=82)
            + [L(outline([(52, 6), (56, -16), (48, -30, 1), (64, -20), (70, -32, 1), (72, -16), (60, 4)])),
               L(outline([(52, -10), (36, -14), (14, -4), (0, 20), (-6, 54), (-4, 80, 1), (6, 54), (16, 24), (34, 6), (52, 2)])),
               L(ell(56, 2, 3.5, 3), 'tie', 'f', ln=True), L([(82, 80), (82, 92)], 'paint', 'f', False, False, 1.4)],
    'back': crop('back', top=6, nape=82)
            + [L(outline([(44, 10), (40, -14), (30, -24, 1), (46, -20), (54, -30, 1), (60, -18), (66, 0), (70, 30), (76, 70), (72, 92, 1), (62, 64), (56, 30), (54, 12)])),
               L(outline([(60, -16), (66, 0), (70, 30), (76, 68), (66, 40)]), 'shade', 'b', False),
               L(ell(52, 6, 4, 3), 'tie', 'f', ln=True)],
}

# Dwight Self: piel tostada; pelo crema clarísimo peinado hacia atrás en una ola que se levanta por detrás, con mechones
# largos que le caen por los lados de la cara; ojos amarillos afilados, ceño y bigotillos en las mejillas
CHARS[T + 'dwight-self'] = {
    'body': 'normal', 'pal': pal('#efebd1', '#c59859', iris='#c8b040', shade='#d3c6a5', deep='#a89a80', pink='#d8a8a0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95,
             'hairline': [(16, 62), (18, 40), (30, 30), (50, 26), (70, 30), (82, 40), (84, 62)]},
    'front': [L(outline([(16, 60), (12, 32), (20, 8), (44, -4), (68, -2), (90, 10), (98, 30), (104, 40, 1), (90, 40), (84, 60), (80, 40), (20, 40)])),
              L(outline([(60, -2), (88, 12), (98, 34), (100, 42), (86, 42), (80, 20)]), 'shade', 'b', False)]
             + [strand([(x, 4), (x + 6, 30)], 'deep', 'b', 1.0) for x in (28, 40, 54, 68)]
             + [fr([(18, 50), (24, 48), (22, 70), (16, 96, 1), (14, 70)]), fr([(82, 50), (76, 48), (78, 70), (84, 92, 1), (86, 70)]),
                L([(26, 86), (34, 85)], OUTC, 'f', False, False, 0.9), L([(66, 85), (74, 86)], OUTC, 'f', False, False, 0.9)],
    'side': [L(outline([(78, 46), (88, 40), (86, 16), (62, 0), (32, -2), (8, 8), (-8, 20, 1), (4, 26), (0, 50), (8, 72), (20, 82), (34, 78), (40, 62), (54, 54)])),
             L(outline([(2, 40), (30, 44), (40, 60), (32, 78), (20, 82), (8, 70)]), 'shade', 'b', False),
             strand([(30, 4), (60, 4), (86, 20)], 'deep', 'b', 1.0), fr([(62, 54), (68, 52), (68, 76), (62, 96, 1), (58, 76)])],
    'back': [L(outline([(16, 80), (10, 46), (14, 18), (34, 2), (60, -2), (84, 8), (100, 24), (108, 40, 1), (92, 40), (88, 60), (84, 80), (50, 86)])),
             L(outline([(58, 0), (84, 10), (98, 26), (92, 42), (86, 78), (62, 84)]), 'shade', 'b', False)]
            + [strand([(x, 6), (x, 76)], 'deep', 'b', 1.0) for x in (32, 50, 68)],
}

# Dylan Magpie (portero): media melena amarilla en forma de casco con raya en medio y flequillo de mechones; cejas negras
# gruesas, ojos grandes negros y sonrisa
CHARS[T + 'dylan-magpie'] = {
    'body': 'normal', 'pal': pal('#d9b51b', '#efb570', iris='#1e1a1a', shade='#a7771a', deep='#7c4f15'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'hairline': False},
    'front': [L(outline([(10, 80), (6, 46), (14, 14), (50, 0), (86, 14), (94, 46), (90, 80), (80, 66), (80, 58), (20, 58), (20, 66)])),
              L(outline([(56, 2), (84, 14), (94, 46), (90, 76), (82, 56)]), 'shade', 'b', False),
              fr([(16, 64), (16, 40), (30, 22), (50, 10), (70, 22), (84, 40), (84, 64), (78, 56), (70, 64, 1), (64, 50), (56, 62, 1), (50, 40), (44, 62, 1), (36, 50),
                  (30, 64, 1), (22, 56)]),
              strand([(50, 4), (50, 34)], 'deep', 'f', 1.2)]
             + brows(66, BLACK, 4.2, 14, 0.2, 13),
    'side': side_cap(top=0, nape=86, front=(86, 50)) + [fr([(70, 50), (90, 46), (90, 60), (86, 66, 1), (78, 58)])] + brow_side(66, BLACK, 4.2, 0.2),
    'back': back_of([(10, 76), (6, 44), (14, 14), (50, 0), (86, 14), (94, 44)], 86) + [strand([(50, 2), (50, 84)], 'deep', 'b', 1.0)],
}

# Dylan Swan: grandote de cara ancha y orejas grandes; pelo rosa rojizo cortado al cepillo, plano por arriba; ojos de
# párpado caído, cejas enfadadas y boca torcida hacia abajo
CHARS[T + 'dylan-swan'] = {
    'body': 'corpulento', 'pal': pal('#c46e68', '#f0b568', iris='#2a2020', shade='#a05650', deep='#723b26'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 97, 'big_ears': 2, 'ear_out': 3, 'nose': (50, 87, 4.0),
             'hairline': [(16, 60), (18, 42), (30, 36), (50, 36), (70, 36), (82, 42), (84, 60)],
             'face_front': blob([(16, 50), (50, 30), (84, 50), (90, 78), (84, 100), (64, 110), (50, 112), (36, 110), (16, 100), (10, 78)])},
    'front': crop('front', top=4, side=60, w=1, flat=14),
    'side': crop('side', top=2, nape=82, flat=14),
    'back': crop('back', top=4, nape=82, flat=14),
}

# Earl Grayson: cara flaca y huesuda; pelo castaño grisáceo de pinchos cortos que salen en corona, con un pico en la frente;
# cejas gruesas, ojos pequeños y boca abierta
CHARS[T + 'earl-grayson'] = {
    'body': 'delgado', 'pal': pal('#9b7c71', '#f0b56f', iris='#2a2020', shade='#7a5944', deep='#523c34'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'none', 'nose': (50, 86, 3.0),
             'hairline': [(16, 62), (20, 46), (34, 40), (44, 44), (50, 54), (56, 44), (66, 40), (80, 46), (84, 62)],
             'face_front': blob([(19, 52), (50, 32), (81, 52), (82, 80), (76, 100), (62, 112), (50, 114), (38, 112), (24, 100), (18, 80)])},
    'front': messy('front', amp=18, n=9, seed=33, lo=62, sweep=0.0) + brows(66, 'deep', 4.0, 14, 0.2, 12)
             + [L(ell(50, 98, 5, 3.5), (120, 50, 40, 255), 'f', ln=True)],
    'side': messy('side', amp=18, n=9, seed=33, nape=84) + brow_side(66, 'deep', 4.0, 0.2),
    'back': messy('back', amp=18, n=9, seed=33, nape=84),
}

# Eathan Ringer: grandote calvo por arriba, con el pelo verde oliva oscuro solo por detrás y los lados, que se abre en picos
# junto a las orejas; ojos cerrados, cejas oliva, nariz redonda naranja, sonrisa y bigotillos en las mejillas
CHARS[T + 'eathan-ringer'] = {
    'body': 'corpulento', 'pal': pal('#58502c', '#f0b46e', iris='#2a2020', shade='#453e22', deep='#322c18', nose='#e8803a'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'nose': (50, 87, 4.6), 'hairline': False,
             'face_front': blob([(16, 50), (50, 30), (84, 50), (90, 78), (84, 100), (64, 110), (50, 112), (36, 110), (16, 100), (10, 78)])},
    'front': skull()
             + [L(outline([(20, 62), (6, 70, 1), (14, 60), (4, 54, 1), (16, 50), (16, 32), (28, 16), (36, 14), (24, 30), (22, 50)])),
                L(outline([(80, 62), (94, 70, 1), (86, 60), (96, 54, 1), (84, 50), (84, 32), (72, 16), (64, 14), (76, 30), (78, 50)])),
                L(outline([(36, 14), (50, 10), (64, 14), (62, 18), (50, 15), (38, 18)]))]
             + brows(66, 'mid', 4.0, 14, -0.3, 12)
             + [L([(24, 86), (32, 87)], OUTC, 'f', False, False, 0.9), L([(68, 87), (76, 86)], OUTC, 'f', False, False, 0.9)],
    'side': skull('side')
            + [L(outline([(42, 64), (24, 80), (10, 84, 1), (14, 74), (2, 72, 1), (8, 56), (6, 32), (18, 16), (32, 14), (40, 34), (44, 52)]))]
            + brow_side(66, 'mid', 4.0, -0.3),
    'back': [L(outline([(14, 80), (0, 76, 1), (10, 66), (6, 46), (16, 22), (50, 10), (84, 22), (94, 46), (90, 66), (100, 76, 1), (86, 80), (50, 86)])),
             L(outline([(58, 12), (84, 24), (94, 48), (88, 78), (62, 84)]), 'shade', 'b', False),
             L(outline([(36, 14), (50, 6), (64, 14), (60, 26), (50, 28), (40, 26)]), 'skin', 'b', False)],
}

# Eaton Rampage: un gorro de cerdito rosa con hocico y orejas, sobre un casco verde que le tapa los lados de la cabeza; un
# mechón rubio en la frente, cejas amarillas, ojos grandes y una sonrisa ancha y ondulada
_PIG = (214, 130, 120, 255)
_PIG_D = (165, 93, 75, 255)
_HEL2 = (90, 126, 108, 255)
_HEL2_D = (64, 96, 80, 255)
CHARS[T + 'eaton-rampage'] = {
    'body': 'corpulento', 'pal': pal('#e8c040', '#f8d69e', iris='#1e1a1a', shade='#c8a028', deep='#a07a18', brow='#e0d040'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'none', 'nose': (50, 87, 3.0), 'ears': False, 'hairline': False,
             'face_front': blob([(16, 52), (50, 36), (84, 52), (90, 80), (82, 100), (64, 110), (50, 112), (36, 110), (18, 100), (10, 80)])},
    'front': [L(outline([(8, 86), (4, 54), (14, 26), (50, 14), (86, 26), (96, 54), (92, 86), (84, 86), (84, 60), (16, 60), (16, 86)]), _HEL2),
              L(outline([(70, 20), (88, 30), (96, 56), (92, 84), (86, 80), (86, 50)]), _HEL2_D, 'b', False),
              fr([(40, 46), (50, 40), (64, 44), (62, 52), (52, 48), (44, 54, 1)]),
              L(outline([(2, 34), (8, 12), (30, -2), (50, -6), (70, -2), (92, 12), (98, 34), (80, 40), (50, 42), (20, 40)]), _PIG, 'f'),
              L(outline([(4, 20), (-8, 4, 1), (16, 6)]), _PIG, 'f'), L(outline([(96, 20), (108, 4, 1), (84, 6)]), _PIG, 'f'),
              L(outline([(36, 22), (40, 12), (60, 12), (64, 22), (60, 30), (40, 30)]), _PIG, 'f', ln=True),
              L(ell(45, 21, 1.8, 2.2), _PIG_D, 'f', False), L(ell(55, 21, 1.8, 2.2), _PIG_D, 'f', False),
              L(ell(28, 26, 1.8, 1.8), BLACK, 'f', False), L(ell(72, 26, 1.8, 1.8), BLACK, 'f', False)]
             + brows(64, 'brow', 3.6, 14, -0.2, 12)
             + [L(quad((34, 96), (42, 101), (50, 97)) + quad((50, 97), (58, 101), (66, 96))[1:], OUTC, 'f', False, False, 1.8)],
    'side': [L(outline([(70, 50), (84, 40), (84, 22), (60, 10), (30, 12), (10, 26), (4, 54), (8, 84), (36, 88), (48, 74), (56, 58)]), _HEL2),
             L(outline([(4, 40), (30, 44), (44, 60), (36, 86), (8, 84)]), _HEL2_D, 'b', False),
             L(outline([(0, 36), (6, 12), (30, -4), (60, -4), (86, 8), (96, 26), (100, 38), (80, 40), (50, 40), (20, 42)]), _PIG, 'f'),
             L(outline([(26, 4), (16, -12, 1), (40, -4)]), _PIG, 'f'),
             L(outline([(94, 24), (104, 22), (106, 34), (96, 36)]), _PIG, 'f', ln=True)]
            + brow_side(64, 'brow', 3.6, -0.2),
    'back': [L(outline([(8, 86), (4, 54), (14, 26), (50, 14), (86, 26), (96, 54), (92, 86), (50, 92)]), _HEL2),
             L(outline([(66, 20), (88, 30), (96, 56), (92, 84), (66, 90)]), _HEL2_D, 'b', False),
             L(outline([(2, 34), (8, 12), (30, -2), (50, -6), (70, -2), (92, 12), (98, 34), (80, 44), (50, 46), (20, 44)]), _PIG, 'f'),
             L(outline([(4, 20), (-8, 4, 1), (16, 6)]), _PIG, 'f'), L(outline([(96, 20), (108, 4, 1), (84, 6)]), _PIG, 'f'),
             L(quad((46, 40), (52, 34), (56, 40)) + quad((56, 40), (50, 44), (48, 38))[1:], _PIG_D, 'f', False, False, 1.4)],
}

# Ebenezer Marner: piel tostada; pelo rojo peinado hacia arriba y atrás en una gran ola que acaba en punta por encima de la
# cabeza, y que por detrás se riza hacia fuera en la nuca; ojos redondos, ceño y boca seria
CHARS[T + 'ebenezer-marner'] = {
    'body': 'normal', 'pal': pal('#a12403', '#cd924b', iris='#1e1a1a', shade='#82200a', deep='#662309'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'nose': (50, 86, 2.6),
             'hairline': [(16, 64), (18, 50), (30, 44), (50, 42), (70, 44), (82, 50), (84, 64)]},
    'front': [L(outline([(16, 66), (12, 40), (18, 14), (34, -2), (56, -8), (72, -22), (80, -30, 1), (78, -10), (88, 8), (90, 38), (84, 66), (80, 50), (20, 50)])),
              L(outline([(60, -6), (78, -12), (88, 8), (90, 38), (84, 60), (76, 26)]), 'shade', 'b', False)]
             + [strand([(x, 4 - (x - 30) * 0.2), (x - 2, 46)], 'deep', 'b', 1.0) for x in (30, 44, 58, 70)],
    'side': [L(outline([(78, 50), (88, 40), (88, 16), (78, -2), (88, -20, 1), (64, -10), (40, -8), (16, 4), (4, 30), (2, 56), (8, 72), (-6, 86, 1), (16, 80), (30, 80),
                        (40, 64), (56, 54)])),
             L(outline([(3, 40), (30, 44), (40, 60), (30, 80), (14, 80), (6, 64)]), 'shade', 'b', False),
             strand([(20, 8), (54, -4), (84, -14)], 'deep', 'b', 1.0)],
    'back': [L(outline([(16, 80), (0, 92, 1), (10, 76), (8, 44), (16, 14), (40, 0), (60, -8), (76, -24), (80, -30, 1), (80, -6), (88, 14), (92, 44), (90, 76), (100, 92, 1),
                        (84, 80), (50, 86)])),
             L(outline([(58, -4), (80, -8), (90, 20), (92, 50), (88, 78), (62, 84)]), 'shade', 'b', False)],
}

# Ed Dupee: pelo verde oliva despeinado en pinchos, con un mechón largo que le cae por la cara y le tapa medio ojo; ojos gris
# azulado y sonrisa
CHARS[T + 'ed-dupee'] = {
    'body': 'normal', 'pal': pal('#726b2f', '#eeb572', iris='#5a7a80', shade='#574824', deep='#413110'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 93, 'hairline': False},
    'front': messy('front', amp=16, n=10, seed=44, lo=66, sweep=-0.1)
             + [fr([(16, 62), (16, 42), (30, 28), (50, 24), (70, 28), (84, 42), (84, 62), (78, 52), (70, 60, 1), (64, 48), (58, 84, 1), (52, 52), (44, 60, 1), (36, 50),
                    (28, 60, 1), (22, 52)]),
                strand([(50, 30), (58, 76)], 'deep', 'f', 1.0)],
    'side': messy('side', amp=16, n=10, seed=44, nape=88, sweep=0.2) + [fr([(72, 44), (92, 46), (92, 60), (88, 72, 1), (82, 58), (76, 52)])],
    'back': messy('back', amp=16, n=10, seed=44, nape=88),
}

# Ed Halley: media melena gris azulada que se abre en dos alas a los lados de la cara, con una cinta roja ancha en la cabeza;
# ojos claros afilados y sonrisa
_RED = (160, 40, 20, 255)
CHARS[T + 'ed-halley'] = {
    'body': 'normal', 'pal': pal('#719197', '#f0b56e', iris='#8aa0b0', shade='#565a5a', deep='#40444a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': (60, 48)},
    'front': [L(outline([(14, 68), (-6, 84, 1), (6, 62), (8, 36), (18, 12), (50, 2), (82, 12), (92, 36), (94, 62), (106, 84, 1), (86, 68), (80, 52), (20, 52)])),
              L(outline([(58, 4), (82, 14), (92, 38), (100, 76), (86, 62), (82, 40)]), 'shade', 'b', False)]
             + [strand([(x, 8), (x, 46)], 'deep', 'b', 0.9) for x in (30, 42, 58, 70)]
             + [L(quad((12, 40), (50, 8), (88, 40)) + quad((90, 30), (50, -4), (10, 30)), _RED, 'f', ln=True)],
    'side': [L(outline([(78, 50), (88, 40), (84, 14), (60, 0), (30, 2), (10, 16), (2, 44), (6, 66), (-8, 84, 1), (16, 78), (30, 80), (40, 64), (56, 54)])),
             L(outline([(3, 44), (30, 46), (40, 60), (30, 80), (10, 80), (4, 64)]), 'shade', 'b', False),
             L(quad((86, 30), (50, 6), (10, 26)) + quad((8, 36), (50, 16), (88, 40)), _RED, 'f', ln=True)],
    'back': [L(outline([(14, 74), (-6, 86, 1), (6, 64), (8, 36), (18, 12), (50, 2), (82, 12), (92, 36), (94, 64), (106, 86, 1), (86, 74), (50, 82)])),
             L(outline([(58, 4), (82, 14), (92, 38), (100, 80), (86, 72), (62, 80)]), 'shade', 'b', False),
             L(quad((10, 36), (50, 10), (90, 36)) + quad((90, 46), (50, 20), (10, 46)), _RED, 'f', ln=True)],
}

# Ed Ripp: hombretón de cara curtida; pelo corto gris verdoso claro con unas patillas grises enormes que le bajan por las
# mejillas; ceño fruncido y boca ondulada
CHARS[T + 'ed-ripp'] = {
    'body': 'corpulento', 'pal': pal('#9cc5c1', '#efb46f', iris='#2a2020', shade='#7ea6a2', deep='#5e7e7a', burn='#6e6a62'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'nose': (50, 87, 4.0),
             'hairline': [(16, 62), (20, 46), (34, 40), (50, 40), (66, 40), (80, 46), (84, 62)],
             'face_front': blob([(16, 52), (50, 32), (84, 52), (88, 80), (82, 100), (64, 110), (50, 112), (36, 110), (18, 100), (12, 80)])},
    'front': crop('front', top=4, side=62, w=2)
             + [L(outline([(16, 62), (24, 64), (26, 84), (34, 98), (24, 100), (14, 86)]), 'burn', 'f'),
                L(outline([(84, 62), (76, 64), (74, 84), (66, 98), (76, 100), (86, 86)]), 'burn', 'f'),
                L(quad((38, 97), (44, 94), (50, 97)) + quad((50, 97), (56, 100), (62, 97))[1:], OUTC, 'f', False, False, 1.6)],
    'side': crop('side', top=2, nape=82, w=2) + [L(outline([(56, 58), (66, 60), (70, 84), (64, 100), (54, 92)]), 'burn', 'f')],
    'back': crop('back', top=4, nape=82, w=2),
}

# Edward Albion (portero): pelo azul petróleo muy oscuro de pinchos que salen hacia arriba y los lados; ojos negros grandes,
# cejas enfadadas y sonrisa
CHARS[T + 'edward-albion'] = {
    'body': 'normal', 'pal': pal('#16404a', '#f7b56e', iris='#1e1a1a', shade='#132f36', deep='#0e2226'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93,
             'hairline': [(16, 64), (20, 50), (30, 44), (40, 54), (50, 44), (60, 54), (70, 44), (80, 50), (84, 64)]},
    'front': messy('front', amp=20, n=10, seed=55, lo=66, sweep=0.1),
    'side': messy('side', amp=20, n=10, seed=55, nape=88, sweep=0.3),
    'back': messy('back', amp=20, n=10, seed=55, nape=88),
}

# Eggbert Heading: flequillo de tazón azul marino cortado recto muy alto, con un pico de pelo en lo alto; gafas redondas
# enormes de montura cobre y cristales blancos; piel pálida, cejas de preocupación y boca triste abierta
_COPPER = (200, 120, 60, 255)
CHARS[T + 'eggbert-heading'] = {
    'body': 'delgado', 'pal': pal('#394f65', '#f7d6a0', iris='#2a2020', shade='#2e3e50', deep='#222e3c', lens='#f4f2e4'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'nose': (50, 88, 2.6), 'hairline': False},
    'front': [L(outline([(16, 58), (12, 30), (20, 8), (44, 0), (50, -8, 1), (56, 0), (80, 8), (88, 30), (84, 58), (80, 48), (20, 48)])),
              L(outline([(60, 2), (80, 10), (88, 32), (84, 54), (76, 30)]), 'shade', 'b', False),
              fr([(14, 56), (14, 36), (28, 24), (50, 20), (72, 24), (86, 36), (86, 56)]),
              strand([(30, 30), (30, 56)], 'deep', 'f', 0.9), strand([(50, 24), (50, 56)], 'deep', 'f', 0.9), strand([(70, 30), (70, 56)], 'deep', 'f', 0.9),
              L(ell(36, 76, 10, 9), 'lens', 'f', False), L(ell(64, 76, 10, 9), 'lens', 'f', False)]
             + ring_glasses('front', 76, _COPPER, 2.8, 10, 9, 14)
             + [L([(26, 66), (36, 62)], OUTC, 'f', False, False, 2.0), L([(64, 62), (74, 66)], OUTC, 'f', False, False, 2.0),
                L(ell(50, 95, 5, 3), (120, 50, 40, 255), 'f', ln=True)],
    'side': [L(outline([(74, 50), (88, 46), (88, 24), (76, 6), (56, -2), (60, -12, 1), (46, -2), (26, 2), (8, 18), (2, 44), (6, 66), (20, 80), (34, 78), (42, 60), (58, 52)])),
             L(outline([(3, 40), (30, 44), (40, 60), (32, 78), (20, 80), (8, 66)]), 'shade', 'b', False),
             L(ell(84, 76, 5.5, 9), 'lens', 'f', False)]
            + ring_glasses('side', 76, _COPPER, 2.8, 5.5, 9),
    'back': back_of([(14, 76), (12, 30), (20, 8), (44, 0), (50, -8, 1), (56, 0), (80, 8), (88, 30)], 84),
}

# Ei King: pelo gris azulado de pinchos peinados hacia arriba y a un lado, con un mechón largo que le cae junto a la cara;
# cara seria con sombra de barba, ceño y boca apretada
CHARS[T + 'ei-king'] = {
    'body': 'normal', 'pal': pal('#5a7988', '#f9c37a', iris='#2a2020', shade='#3d5967', deep='#2c4250', stubble='#d8a868'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'nose': (50, 86, 2.8),
             'hairline': [(16, 66), (18, 50), (28, 42), (40, 48), (52, 38), (66, 42), (80, 48), (84, 62)]},
    'front': [L(outline([(16, 66), (10, 40), (14, 16), (28, 4), (36, -12, 1), (46, 0), (62, -24, 1), (64, -4), (86, -16, 1), (82, 6), (98, 0, 1), (90, 24), (90, 44),
                         (84, 62), (80, 50), (20, 50)])),
              L(outline([(64, -4), (86, -16), (82, 6), (98, 0), (90, 24), (90, 44), (84, 56), (76, 26)]), 'shade', 'b', False),
              strand([(30, 16), (50, 2), (70, -8)], 'deep', 'b', 1.0), strand([(36, 34), (60, 16), (84, 8)], 'deep', 'b', 1.0),
              fr([(16, 52), (24, 46), (24, 70), (20, 92, 1), (16, 70)])],
    'side': [L(outline([(78, 50), (90, 42), (92, 24), (106, 14, 1), (88, 8), (96, -8, 1), (74, -2), (70, -20, 1), (56, -4), (34, -2), (12, 12), (2, 40), (6, 66), (18, 80),
                        (34, 78), (40, 62), (56, 54)])),
             L(outline([(3, 40), (30, 44), (40, 60), (32, 78), (18, 80), (8, 64)]), 'shade', 'b', False),
             strand([(20, 10), (54, 0), (90, 6)], 'deep', 'b', 1.0)],
    'back': [L(outline([(16, 80), (10, 44), (14, 16), (28, 4), (36, -12, 1), (46, 0), (62, -24, 1), (64, -4), (86, -16, 1), (82, 6), (98, 0, 1), (90, 24), (90, 44),
                        (84, 80), (50, 86)])),
             L(outline([(64, -4), (86, -16), (82, 6), (98, 0), (90, 24), (90, 44), (84, 78), (62, 84)]), 'shade', 'b', False)],
}

# Equin Knocks: piel tostada, cara larguísima; pelo corto rojizo con la frente muy alta; ojos caídos de cansancio, cejas
# arqueadas y unos labios enormes
CHARS[T + 'equin-knocks'] = {
    'body': 'corpulento', 'pal': pal('#a84209', '#cd914b', iris='#2a2020', shade='#863608', deep='#7c3f10'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'none', 'nose': (50, 86, 4.4), 'eye_y': 76,
             'hairline': [(17, 56), (20, 36), (32, 26), (50, 24), (68, 26), (80, 36), (83, 56)],
             'face_front': blob([(19, 50), (50, 30), (81, 50), (84, 80), (80, 102), (66, 116), (50, 119), (34, 116), (20, 102), (16, 80)])},
    'front': crop('front', top=6, side=56, w=0, flat=8)
             + [L(blob([(36, 98), (44, 94), (50, 95), (56, 94), (64, 98), (60, 105), (50, 108), (40, 105)], 6), (150, 82, 50, 255), 'f', ln=True),
                L(quad((38, 99), (50, 102), (62, 99)), OUTC, 'f', False, False, 1.2)],
    'side': crop('side', top=4, nape=82, flat=8) + [L(blob([(80, 96), (88, 95), (90, 101), (86, 106), (80, 104)], 5), (150, 82, 50, 255), 'f', ln=True)],
    'back': crop('back', top=6, nape=82, flat=8),
}

# Erhard Blower: pelo rojo en llamas de pinchos alborotados hacia arriba y los lados; ojos verde azulado, ceño y sonrisa
CHARS[T + 'erhard-blower'] = {
    'body': 'normal', 'pal': pal('#b02a08', '#f0b46f', iris='#4aa0a8', shade='#832107', deep='#551a0a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93,
             'hairline': [(16, 64), (20, 50), (30, 44), (40, 54), (50, 44), (60, 52), (70, 44), (80, 50), (84, 64)]},
    'front': messy('front', amp=22, n=11, seed=66, lo=66, sweep=0.2)
             + [L([(26, 86), (33, 85)], OUTC, 'f', False, False, 0.9), L([(67, 85), (74, 86)], OUTC, 'f', False, False, 0.9)],
    'side': messy('side', amp=22, n=11, seed=66, nape=88, sweep=0.35),
    'back': messy('back', amp=22, n=11, seed=66, nape=88),
}

# Ernest Byer: piel tostada; rastas gruesas color crema rosado que caen hasta los hombros, con cuentas azul marino y verdes;
# gafas de sol amarillas de cristales oscuros y sonrisa
_BEAD1 = (40, 48, 80, 255)
_BEAD2 = (110, 150, 70, 255)
_FRAME = (230, 200, 40, 255)
_SHADES = (100, 72, 40, 255)


def _dreads(tips, top=(50, 6)):
    out = []
    for (x0, y0), (x1, y1) in tips:
        out.append(L(rope((x0, y0), ((x0 + x1) / 2 + (x1 - x0) * 0.1, (y0 + y1) / 2), (x1, y1), 9), 'mid', 'b', ln=True))
    return out


CHARS[T + 'ernest-byer'] = {
    'body': 'normal', 'pal': pal('#eee4ca', '#cd9448', iris='#2a2020', shade='#c19c82', deep='#977261'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 94, 'hairline': [(16, 60), (20, 44), (34, 36), (50, 34), (66, 36), (80, 44), (84, 60)]},
    'front': crop('front', top=4, side=60, c='shade', shade=False)
             + _dreads([((24, 14), (8, 104)), ((36, 8), (18, 108)), ((64, 8), (82, 108)), ((76, 14), (92, 104)), ((16, 30), (2, 92)), ((84, 30), (98, 92))])
             + [strand([(36, 10), (40, 36)], 'deep', 'b', 1.0), strand([(64, 10), (60, 36)], 'deep', 'b', 1.0), strand([(50, 4), (50, 36)], 'deep', 'b', 1.0)]
             + [L(ell(x, y, 4.5, 3.6), c, 'f', ln=True) for x, y, c in ((12, 74, _BEAD1), (88, 74, _BEAD1), (6, 92, _BEAD2), (94, 92, _BEAD2), (18, 98, _BEAD1),
                                                                         (82, 98, _BEAD1))]
             + [L(outline([(22, 70), (34, 68), (46, 72), (54, 72), (66, 68), (78, 70), (76, 82), (62, 84), (54, 78), (46, 78), (38, 84), (24, 82)]), _SHADES, 'f', False),
                L(outline([(20, 68), (34, 66), (46, 70), (54, 70), (66, 66), (80, 68), (80, 72), (66, 70), (54, 74), (46, 74), (34, 70), (20, 72)]), _FRAME, 'f', ln=True)],
    'side': crop('side', top=2, nape=84, c='shade', shade=False)
            + _dreads([((30, 6), (8, 104)), ((44, 4), (26, 106)), ((14, 20), (-6, 92)), ((22, 10), (2, 100))])
            + [L(ell(x, y, 4.5, 3.6), c, 'f', ln=True) for x, y, c in ((4, 80, _BEAD1), (16, 92, _BEAD2), (36, 96, _BEAD1))]
            + [L(outline([(74, 70), (88, 68), (88, 80), (76, 82)]), _SHADES, 'f', False), L([(52, 66), (88, 66), (88, 70), (52, 70)], _FRAME, 'f', ln=True)],
    'back': crop('back', top=4, nape=84, c='shade', shade=False)
            + _dreads([((20, 18), (8, 106)), ((34, 10), (24, 110)), ((50, 8), (44, 112)), ((50, 8), (58, 112)), ((66, 10), (76, 110)), ((80, 18), (92, 106))])
            + [L(ell(x, y, 4.5, 3.6), c, 'f', ln=True) for x, y, c in ((12, 80, _BEAD1), (88, 80, _BEAD1), (30, 96, _BEAD2), (70, 96, _BEAD2), (50, 104, _BEAD1))],
}

# Ernie Riddell: piel oscura; pelo azul marino muy corto con las entradas en ángulo; ojos amarillos redondos grandes, cejas
# gruesas azul marino y labios gruesos
CHARS[T + 'ernie-riddell'] = {
    'body': 'normal', 'pal': pal('#3a4e66', '#c69a58', iris='#e0c020', shade='#2e3e52', deep='#22303e'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'none', 'nose': (50, 86, 2.6),
             'hairline': [(16, 62), (18, 46), (28, 44), (34, 36), (50, 34), (66, 36), (72, 44), (82, 46), (84, 62)]},
    'front': crop('front', top=4, side=62, w=1) + brows(65, 'mid', 4.0, 14, 0.3, 13)
             + [L(blob([(40, 95), (50, 93), (60, 95), (56, 100), (44, 100)], 5), (150, 82, 50, 255), 'f', ln=True)],
    'side': crop('side', top=2, nape=84, w=1) + brow_side(65, 'mid', 4.0, 0.3),
    'back': crop('back', top=4, nape=84, w=1),
}

# Errol Lorre: gorro azul marino que le cubre la cabeza con dos bolas como orejas de ratón y un flequillo a rayas crema que
# asoma; cara de señor arrugada, párpados caídos y sonrisa cansada
_CAP = (58, 79, 101, 255)
_CAP_D = (40, 56, 74, 255)
CHARS[T + 'errol-lorre'] = {
    'body': 'delgado', 'pal': pal('#e6e2c5', '#eeb46e', iris='#2a2020', shade='#bb9d82', deep='#8a7464'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 98, 'nose': (50, 88, 3.4), 'ears': False, 'hairline': False,
             'face_front': blob([(19, 52), (50, 34), (81, 52), (82, 80), (76, 102), (62, 114), (50, 116), (38, 114), (24, 102), (18, 80)])},
    'front': [L(outline([(10, 96), (6, 56), (12, 22), (30, 4), (50, 0), (70, 4), (88, 22), (94, 56), (90, 96), (82, 96), (82, 60), (76, 50), (24, 50), (18, 60), (18, 96)]), _CAP),
              L(outline([(60, 2), (84, 14), (94, 50), (90, 92), (84, 90), (86, 56)]), _CAP_D, 'b', False),
              L(ell(18, 4, 10, 10), _CAP, 'b', ln=True), L(ell(82, 4, 10, 10), _CAP, 'b', ln=True),
              fr([(22, 58), (24, 40), (36, 32), (50, 30), (64, 32), (76, 40), (78, 58), (50, 56)])]
             + [strand([(x, 33), (x, 56)], 'shade', 'f', 1.4) for x in (32, 42, 52, 62, 70)]
             + [L(quad((28, 84), (32, 92), (36, 96)), OUTC, 'f', False, False, 0.9), L(quad((72, 84), (68, 92), (64, 96)), OUTC, 'f', False, False, 0.9),
                L(quad((36, 64), (50, 62), (64, 64)), OUTC, 'f', False, False, 0.8)],
    'side': [L(outline([(76, 50), (86, 42), (86, 18), (66, 2), (38, 0), (14, 12), (2, 40), (2, 80), (12, 100), (34, 102), (44, 82), (52, 60), (62, 52)]), _CAP),
             L(outline([(2, 44), (30, 48), (44, 62), (34, 100), (12, 98), (4, 78)]), _CAP_D, 'b', False),
             L(ell(42, 0, 10, 10), _CAP, 'b', ln=True),
             fr([(70, 50), (84, 44), (90, 52), (86, 58), (74, 58)])],
    'back': [L(outline([(10, 96), (6, 56), (12, 22), (30, 4), (50, 0), (70, 4), (88, 22), (94, 56), (90, 96), (50, 100)]), _CAP),
             L(outline([(60, 2), (84, 14), (94, 50), (90, 94), (62, 98)]), _CAP_D, 'b', False),
             L(ell(18, 4, 10, 10), _CAP, 'b', ln=True), L(ell(82, 4, 10, 10), _CAP, 'b', ln=True)],
}

# Esau Fagus: cara pálida con sombra de ojos; media melena naranja rojiza echada a un lado en una gran capa que le tapa
# media frente; ojos afilados y sonrisa de colmillos
CHARS[T + 'esau-fagus'] = {
    'body': 'delgado', 'pal': pal('#a7400a', '#e3d2bc', iris='#4a4040', shade='#843208', deep='#5b2412', shadow='#a08aa0'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'nose': (50, 86, 2.8),
             'hairline': [(16, 72), (18, 52), (30, 42), (50, 38), (64, 46), (76, 54), (84, 66)]},
    'front': [L(outline([(10, 88, 1), (6, 56), (10, 26), (26, 4), (46, -6), (70, -2), (88, 12), (94, 36), (92, 60), (86, 64), (80, 52), (20, 52), (16, 70)])),
              L(outline([(56, -4), (80, 4), (92, 24), (94, 50), (86, 60), (80, 36)]), 'shade', 'b', False),
              fr([(10, 70), (12, 36), (28, 14), (50, 8), (66, 22), (60, 40), (44, 46), (28, 56), (18, 76, 1)]),
              strand([(30, 20), (50, 14), (60, 28)], 'deep', 'f', 1.0),
              L(quad((28, 72), (36, 69), (44, 72)), 'shadow', 'f', False, False, 1.6), L(quad((56, 72), (64, 69), (72, 72)), 'shadow', 'f', False, False, 1.6),
              L([(55, 95), (57, 99), (59, 95)], WHITE, 'f', ln=True), L([(41, 95), (43, 99), (45, 95)], WHITE, 'f', ln=True)],
    'side': [L(outline([(78, 52), (90, 46), (92, 22), (74, 0), (44, -6), (18, 4), (4, 30), (0, 60), (6, 86, 1), (20, 82), (34, 80), (40, 64), (56, 56)])),
             L(outline([(2, 44), (30, 46), (40, 60), (32, 80), (12, 82), (4, 64)]), 'shade', 'b', False),
             strand([(20, 6), (56, -2), (88, 22)], 'deep', 'b', 1.0)],
    'back': [L(outline([(10, 88, 1), (6, 56), (10, 26), (26, 4), (46, -6), (70, -2), (88, 12), (94, 36), (94, 64), (88, 80), (50, 86), (24, 84)])),
             L(outline([(56, -4), (80, 4), (92, 24), (94, 60), (86, 78), (62, 84)]), 'shade', 'b', False)],
}

# Euan Stamper: pelo verde grisáceo de pinchos revueltos; ojos afilados, cejas enfadadas y media sonrisa
CHARS[T + 'euan-stamper'] = {
    'body': 'normal', 'pal': pal('#5b7262', '#eeb571', iris='#2a2020', shade='#4a5c4e', deep='#39372d'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93,
             'hairline': [(16, 64), (20, 50), (30, 46), (40, 54), (50, 44), (60, 52), (70, 46), (80, 50), (84, 64)]},
    'front': messy('front', amp=18, n=12, seed=77, lo=66, sweep=-0.1),
    'side': messy('side', amp=18, n=12, seed=77, nape=88, sweep=0.2),
    'back': messy('back', amp=18, n=12, seed=77, nape=88),
}

# Evan Yielding: pelo verde oliva muy oscuro, liso hasta la mandíbula y abierto en puntas a los lados, con raya y flequillo
# de lado; dos rayas pintadas oscuras en cada mejilla; ceño y boca seria
CHARS[T + 'evan-yielding'] = {
    'body': 'normal', 'pal': pal('#433e20', '#efb570', iris='#2a2020', shade='#372f1b', deep='#2a2216'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94,
             'hairline': [(16, 70), (18, 52), (30, 44), (44, 50), (56, 40), (70, 44), (82, 52), (84, 70)]},
    'front': [L(outline([(10, 96, 1), (8, 64), (8, 34), (20, 10), (50, 0), (80, 10), (92, 34), (92, 64), (90, 96, 1), (82, 78), (80, 56), (20, 56), (18, 78)])),
              L(outline([(60, 2), (82, 12), (92, 36), (92, 84), (84, 66), (80, 40)]), 'shade', 'b', False),
              fr([(18, 58), (20, 36), (34, 22), (54, 18), (72, 24), (84, 40), (84, 58), (70, 48), (56, 44), (40, 52), (28, 60, 1)]),
              strand([(50, 20), (34, 46)], 'deep', 'f', 1.0)]
             + [L([(x0, 82), (x1, 92)], 'mid', 'f', False, False, 2.0) for x0, x1 in ((26, 22), (32, 28), (74, 78), (68, 72))],
    'side': [L(outline([(78, 50), (88, 40), (84, 14), (60, 0), (30, 2), (10, 16), (2, 44), (4, 74), (12, 98, 1), (24, 86), (34, 96, 1), (38, 74), (44, 60), (58, 54)])),
             L(outline([(3, 44), (30, 46), (40, 60), (34, 90), (14, 94), (4, 72)]), 'shade', 'b', False),
             L([(78, 82), (82, 92)], 'mid', 'f', False, False, 2.0)],
    'back': longhair('back', length=94, flare=2, top=0, ends=4),
}

# Ewan Liner (portero): piel tostada; rastas gruesas amarillas enroscadas que se levantan en lo alto de la cabeza, sobre una
# cinta verde azulada ancha; cejas amarillas, párpados caídos y labios gruesos
_TEAL2 = (96, 150, 150, 255)
CHARS[T + 'ewan-liner'] = {
    'body': 'normal', 'pal': pal('#d6b421', '#cb934c', iris='#2a2020', shade='#a67722', deep='#895417', under='#c4502a'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'none', 'nose': (50, 86, 4.0), 'hairline': False},
    'front': [L(outline([(16, 62), (14, 40), (84, 40), (86, 62), (80, 54), (20, 54)]), 'under')]
             + [L(rope((x, 42), (x + dx * 0.8, 20), (x + dx, 6), 15), 'mid', 'b', ln=True) for x, dx in ((14, -10), (28, -6), (42, -2), (58, 2), (72, 6), (86, 10))]
             + [L(rope((x, 30), (x + dx * 0.8, 10), (x + dx, -4), 14), 'mid', 'b', ln=True) for x, dx in ((36, -4), (50, 0), (64, 4))]
             + [L(quad((12, 54), (50, 38), (88, 54)) + quad((88, 44), (50, 28), (12, 44)), _TEAL2, 'f', ln=True)]
             + brows(64, 'mid', 3.6, 14, -0.2, 12)
             + [L(blob([(36, 95), (44, 92), (50, 93), (56, 92), (64, 95), (60, 101), (50, 103), (40, 101)], 6), (150, 82, 50, 255), 'f', ln=True),
                L(quad((38, 96), (50, 98), (62, 96)), OUTC, 'f', False, False, 1.2)],
    'side': [L(outline([(70, 50), (86, 44), (84, 30), (14, 30), (8, 50), (30, 56)]), 'under')]
            + [L(rope((x, 38), (x + dx * 0.8, 18), (x + dx, 2), 15), 'mid', 'b', ln=True) for x, dx in ((14, -12), (30, -6), (48, 0), (64, 6), (80, 12))]
            + [L(quad((86, 48), (50, 36), (8, 50)) + quad((8, 40), (50, 26), (88, 38)), _TEAL2, 'f', ln=True)]
            + brow_side(64, 'mid', 3.6, -0.2),
    'back': [L(outline([(14, 80), (12, 40), (88, 40), (86, 80), (50, 84)]), 'shade')]
            + [L(rope((x, 44), (x + dx * 0.8, 22), (x + dx, 6), 15), 'mid', 'b', ln=True) for x, dx in ((14, -10), (28, -6), (42, -2), (58, 2), (72, 6), (86, 10))]
            + [L(quad((10, 56), (50, 44), (90, 56)) + quad((90, 46), (50, 34), (10, 46)), _TEAL2, 'f', ln=True)],
}

# Fane Club (portero): niño pequeño con el pelo rosa rojizo en tres pinchos altísimos hacia arriba y los lados, y un
# flequillo de punta; ojos verdes grandes, ceño y boca enfurruñada
CHARS[T + 'fane-club'] = {
    'body': 'bajito', 'pal': pal('#c76f69', '#eeaa65', iris='#6a8a50', shade='#a8564f', deep='#8f443d'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 93,
             'hairline': [(16, 62), (20, 50), (32, 44), (44, 54), (54, 44), (66, 46), (80, 50), (84, 62)]},
    'front': [L(outline([(16, 62), (12, 40), (4, 4, 1), (22, 18), (28, -26, 1), (42, 6), (54, 2), (64, -30, 1), (70, 6), (100, -10, 1), (88, 26), (90, 46), (84, 62), (80, 50),
                         (20, 50)])),
              L(outline([(54, 2), (64, -30), (70, 6), (100, -10), (88, 26), (90, 44), (84, 56), (74, 26)]), 'shade', 'b', False),
              fr([(18, 50), (30, 38), (50, 36), (70, 38), (82, 48), (66, 46), (50, 46), (42, 58, 1), (36, 46), (26, 52)]),
              strand([(30, 4), (36, 36)], 'deep', 'b', 1.0), strand([(64, -16), (60, 34)], 'deep', 'b', 1.0)],
    'side': [L(outline([(76, 50), (88, 42), (92, 22), (110, 2, 1), (84, 6), (82, -28, 1), (62, -2), (40, -24, 1), (34, 2), (14, 10), (4, 34), (4, 60), (14, 78), (30, 80),
                        (40, 62), (56, 54)])),
             L(outline([(5, 40), (30, 44), (40, 60), (30, 80), (14, 78), (6, 62)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 80), (12, 40), (4, 4, 1), (22, 18), (28, -26, 1), (42, 6), (54, 2), (64, -30, 1), (70, 6), (100, -10, 1), (88, 26), (90, 46), (84, 80), (50, 86)])),
             L(outline([(54, 2), (64, -30), (70, 6), (100, -10), (88, 26), (90, 46), (84, 78), (62, 84)]), 'shade', 'b', False)],
}
