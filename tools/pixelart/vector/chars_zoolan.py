"""Team Garshield / Zoolan Team (IE3): turbantes y pañuelos granates, bufanda granate al cuello y pelos de todos los
colores, con sus modelos 3D como referencia (contornos calcados sobre una rejilla de unidades de cabeza)."""
from chars import CHARS, L, OUTC, blob, ell, longhair, messy, outline, pal, rope, spk, strand
from chars_alius import LONG_FACE, SIDE_SKULL, SKULL_B, SKULL_F, WIDE_FACE
from chars_bigwaves import bald, side_eye, white_eyes
from chars_desertlion import bandana
from chars_unicorn import buzz
from heads import quad

WHITE = (250, 250, 250, 255)
WINE = '#8a1e34'
WINE_D = '#681428'


def scarf(view, top=98, up=False):
    """La bufanda granate del equipo enrollada al cuello (up: subida hasta la nariz)."""
    t = 84 if up else top
    if view == 'front':
        return [L(outline([(18, t), (50, t + 4), (82, t), (86, 112), (50, 118), (14, 112)]), 'scarf', 'f', ln=True),
                L(outline([(56, t + 4), (82, t + 2), (84, 110), (60, 114)]), 'scarf_d', 'f', False)]
    if view == 'side':
        return [L(outline([(30, top + 4), (60, t + 2), (92, t), (94, 110), (60, 116), (32, 114)]), 'scarf', 'f', ln=True)]
    return [L(outline([(16, top + 4), (50, top), (84, top + 4), (86, 114), (50, 118), (14, 114)]), 'scarf', 'f', ln=True)]


def turban(view, low=60, c='scarf', cd='scarf_d', tail=None):
    """Turbante de tela granate enrollado (tail: punta que cae por un lado, 1 a la derecha de la imagen, -1 a la izquierda)."""
    out = bandana(view, c, cd, low=low, tails=False)
    if view == 'front':
        out += [L(quad((10, low - 12), (50, low - 20), (90, low - 12)), cd, 'f', False, False, 1.4), L(quad((10, low - 24), (50, low - 30), (90, low - 24)), cd, 'f', False, False, 1.4)]
        if tail:
            x = 50 + tail * 38
            out.append(L(outline([(x - 8, low - 30), (x + 8, low - 30), (x + 10, low + 30), (x - 4, low + 34)]), c, 'f', ln=True))
    return out


def P(*a, **k):
    return pal(*a, scarf=WINE, scarf_d=WINE_D, **k)


# Cyril Fox (portero): melena blanca lisa y recta hasta los hombros que le tapa un ojo; piel morena, el otro ojo cerrado
CHARS['cyril-fox'] = {
    'body': 'normal', 'pal': P('#f0ece4', '#a8703e', shade='#c8bcb0'),
    'face': {'eyes': 'closed', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': longhair('front', 106, 0, top=-2)
             + [L(outline([(12, 66), (14, 40), (30, 22), (52, 16), (74, 22), (88, 40), (88, 64), (78, 56), (66, 56), (58, 70), (52, 96, 1), (46, 70), (36, 62), (22, 68)]), 'mid', 'f', ln=True)]
             + [strand([(x, 14), (x - 6, 100)], 'shade', 'b', 1.0) for x in (16, 84)] + scarf('front'),
    'side': longhair('side', 106, 0, top=-2) + scarf('side'),
    'back': longhair('back', 106, 0, top=-2, ends=0) + [strand([(x, 2), (x, 104)], 'shade', 'b', 1.0) for x in (24, 40, 60, 76)] + scarf('back'),
}
# Jacques Allemand: pelo azul grisáceo despeinado de puntas que asoman bajo un turbante granate enrollado, con mechones que le
# caen por las sienes; ojos dorados de pillo y una sonrisa de dientes
CHARS['jacques-allemand'] = {
    'body': 'normal', 'pal': P('#6a8aa0', '#d8944a', iris='#c89a1e', shade='#4e6a80'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'hairline': False},
    'front': messy('front', 12, 9, seed=1601, rx=52, ry=40, cy=40, lo=74) + turban('front', 52)
             + [L(outline([(16, 52), (4, 60, 1), (18, 64), (30, 70, 1), (24, 56)]), 'mid', 'f', ln=True), L(outline([(84, 52), (96, 60, 1), (82, 64), (70, 70, 1), (76, 56)]), 'mid', 'f', ln=True)]
             + scarf('front'),
    'side': messy('side', 13, 8, seed=1601, rx=48, ry=40, cy=40, nape=96) + turban('side', 48) + scarf('side'),
    'back': messy('back', 12, 9, seed=1601, rx=52, ry=40, cy=40, nape=98) + turban('back', 52) + scarf('back'),
}
# Phil A. Minion: gordo de cabeza calva y redonda naranja con un rizo verde oliva en lo alto; ojos verdes ovalados de
# sueño y una sonrisa
CHARS['phil-a-minion'] = {
    'body': 'corpulento', 'pal': P('#5a6a2a', '#f0a050', iris='#5a6a2a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 2, 'ear_out': 6},
    'front': bald('front') + [L(outline([(46, 8), (42, -6), (48, -18), (60, -16), (52, -10), (54, 8)]), 'mid', 'f', ln=True),
                              L(ell(34, 72, 4.4, 3.4), 'iris', 'f', ln=True), L(ell(66, 72, 4.4, 3.4), 'iris', 'f', ln=True),
                              L([(24, 76), (32, 80)], OUTC, 'f', False, False, 1.2), L([(76, 76), (68, 80)], OUTC, 'f', False, False, 1.2)] + scarf('front'),
    'side': bald('side') + [L(outline([(46, 8), (44, -8), (54, -18), (62, -12), (54, -8), (54, 8)]), 'mid', 'f', ln=True), L(ell(84, 72, 3, 3.4), 'iris', 'f', ln=True)] + scarf('side'),
    'back': bald('back') + [L(outline([(46, 8), (44, -8), (54, -18), (62, -12), (54, -8), (54, 8)]), 'mid', 'f', ln=True)] + scarf('back'),
}
# Buddy Plains: pelo azul marino de pinchos grandes hacia arriba con una cinta granate atada sobre los ojos (que brillan
# amarillos por debajo); patillas en punta y los dientes apretados
CHARS['buddy-plains'] = {
    'body': 'corpulento', 'pal': P('#24345a', '#c88a40', shade='#182440'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': [L(outline([(12, 70), (4, 50), (-10, 54, 1), (6, 40), (4, 24), (14, -2, 1), (28, 12), (36, -14, 1), (46, 6), (54, -16, 1), (62, 6), (72, -10, 1), (78, 12), (90, -2, 1),
                         (94, 24), (94, 40), (110, 54, 1), (96, 50), (88, 70), (80, 62), (20, 62)])),
              L(outline([(56, 4), (72, -6, 1), (78, 14), (92, 4, 1), (92, 40), (86, 60), (76, 30)]), 'shade', 'b', False),
              L(outline([(10, 74), (16, 64), (24, 66), (20, 92, 1)]), 'mid', 'f', ln=True), L(outline([(90, 74), (84, 64), (76, 66), (80, 92, 1)]), 'mid', 'f', ln=True),
              L(outline([(8, 60), (50, 54), (92, 60), (92, 76), (50, 70), (8, 76)]), 'scarf', 'f', ln=True),
              L(outline([(24, 78), (42, 80), (38, 86), (26, 84)]), OUTC, 'f', False), L(outline([(76, 78), (58, 80), (62, 86), (74, 84)]), OUTC, 'f', False),
              L(ell(32, 82, 2.4, 1.6), (240, 220, 60, 255), 'f', False), L(ell(68, 82, 2.4, 1.6), (240, 220, 60, 255), 'f', False),
              L(outline([(32, 96), (68, 96), (64, 104), (36, 104)]), WHITE, 'f', ln=True)] + scarf('front'),
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (-6, 62, 1), (8, 50), (-8, 36, 1), (10, 30), (4, 10, 1), (24, 14), (26, -10, 1), (40, 6), (50, -16, 1), (60, 4), (76, -6, 1),
                        (80, 14), (92, 30), (82, 42), (64, 46), (54, 62), (50, 80)])),
             L(outline([(6, 56), (92, 54), (94, 70), (8, 72)]), 'scarf', 'f', ln=True), L(outline([(64, 70), (76, 64), (76, 100, 1)]), 'mid', 'f', ln=True)] + scarf('side'),
    'back': [L(outline([(12, 84), (4, 50), (-10, 54, 1), (6, 40), (4, 24), (14, -2, 1), (28, 12), (36, -14, 1), (46, 6), (54, -16, 1), (62, 6), (72, -10, 1), (78, 12), (90, -2, 1),
                        (94, 24), (94, 40), (110, 54, 1), (96, 50), (88, 84), (50, 90)])),
             L(outline([(6, 60), (50, 56), (94, 60), (94, 76), (50, 72), (6, 76)]), 'scarf', 'f', ln=True)] + scarf('back'),
}
# Dean Goddard: pelo gris claro de puntas con un mechón negro a un lado, y un pañuelo granate atado en la frente con dos
# puntas largas que le caen por un lado; una cicatriz bajo un ojo y la boca seria
CHARS['dean-goddard'] = {
    'body': 'normal', 'pal': P('#c8d0c0', '#c88a50', iris='#2a6a9a', shade='#a0a898', dark='#24282e', scar='#e0b080'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': messy('front', 9, 9, seed=1602, rx=50, ry=42, cy=40, lo=72)
             + [L(outline([(60, 4), (74, -6, 1), (78, 14), (92, 6, 1), (90, 30), (80, 30)]), 'dark', 'f', ln=True)]
             + [L(outline([(10, 66), (10, 48), (50, 40), (90, 48), (90, 66), (50, 58)]), 'scarf', 'f', ln=True),
                L(outline([(4, 50), (12, 50), (14, 92), (2, 96)]), 'scarf', 'f', ln=True), L(outline([(8, 52), (18, 52), (22, 88), (12, 90)]), 'scarf_d', 'f', ln=True),
                L([(60, 82), (66, 92)], 'scar', 'f', False, False, 1.6)] + scarf('front'),
    'side': messy('side', 10, 8, seed=1602, rx=48, ry=42, cy=40, nape=94) + [L(outline([(6, 62), (6, 44), (92, 44), (92, 60)]), 'scarf', 'f', ln=True),
                                                                             L(outline([(30, 50), (40, 50), (42, 92), (28, 94)]), 'scarf', 'f', ln=True)] + scarf('side'),
    'back': messy('back', 9, 9, seed=1602, rx=50, ry=42, cy=40, nape=94) + [L(outline([(6, 64), (6, 46), (50, 40), (94, 46), (94, 64), (50, 58)]), 'scarf', 'f', ln=True),
                                                                            L(outline([(76, 50), (92, 50), (96, 96), (80, 98)]), 'scarf', 'f', ln=True)] + scarf('back'),
}
# Cecil Crowley: pelo gris azulado peinado hacia arriba en punta y una cinta granate atada sobre los ojos; por debajo asoma
# el pelo a los lados; la boca en una raya
CHARS['cecil-crowley'] = {
    'body': 'normal', 'pal': P('#3a4a50', '#fcd0a0', shade='#283438'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 70), (10, 40), (22, 10), (40, -8), (50, -20, 1), (60, -8), (78, 10), (90, 40), (86, 70), (80, 62), (20, 62)])),
              L(outline([(56, -8), (78, 10), (90, 40), (86, 66), (74, 36)]), 'shade', 'b', False),
              L(outline([(12, 74), (18, 64), (24, 66), (20, 90, 1)]), 'mid', 'f', ln=True), L(outline([(88, 74), (82, 64), (76, 66), (80, 90, 1)]), 'mid', 'f', ln=True),
              L(outline([(8, 58), (50, 52), (92, 58), (92, 80), (50, 76), (8, 80)]), 'scarf', 'f', ln=True), L(quad((10, 68), (50, 62), (90, 68)), 'scarf_d', 'f', False, False, 1.4)]
             + scarf('front'),
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (10, 34), (22, 10), (40, -6), (34, -20, 1), (56, -6), (78, 4), (92, 24), (88, 40), (74, 44), (60, 48), (52, 64), (50, 80)])),
             L(outline([(6, 56), (94, 54), (96, 76), (8, 78)]), 'scarf', 'f', ln=True), L(outline([(12, 60), (0, 72, 1), (6, 84), (18, 72)]), 'scarf', 'f', ln=True)] + scarf('side'),
    'back': [L(outline([(14, 84), (10, 40), (22, 10), (40, -8), (50, -20, 1), (60, -8), (78, 10), (90, 40), (86, 84), (50, 90)])),
             L(outline([(6, 60), (50, 54), (94, 60), (94, 80), (50, 76), (6, 80)]), 'scarf', 'f', ln=True),
             L(outline([(42, 66), (36, 92), (46, 96), (50, 72), (54, 96), (64, 92), (58, 66)]), 'scarf_d', 'f', ln=True)] + scarf('back'),
}
# Seth Hedges: pelo rubio verdoso liso peinado a un lado en un flequillo enorme que le tapa un ojo; el otro ojo rojizo y la
# boca seria
CHARS['seth-hedges'] = {
    'body': 'normal', 'pal': P('#c8c840', '#fcdcc0', iris='#8a2a4a', shade='#9a9a28'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 70), (8, 34), (20, 8), (50, 0), (80, 8), (92, 34), (88, 70), (80, 62), (20, 62)])),
              L(outline([(60, 4), (84, 16), (92, 40), (88, 66), (78, 40)]), 'shade', 'b', False),
              L(outline([(20, 50), (24, 26), (44, 12), (70, 12), (88, 26), (94, 50), (92, 78), (82, 90, 1), (78, 66), (66, 52), (50, 46), (32, 50)]), 'mid', 'f', ln=True)]
             + [strand([(36 + k * 12, 16), (50 + k * 10, 40), (70 + k * 6, 66)], 'shade', 'f', 1.0) for k in range(3)] + scarf('front'),
    'side': [L(outline([(44, 92), (22, 88), (12, 64), (8, 32), (22, 8), (52, -2), (80, 6), (96, 24), (98, 50), (88, 54), (70, 48), (58, 52), (52, 64), (50, 80)])),
             L(outline([(10, 40), (34, 40), (42, 80), (22, 88)]), 'shade', 'b', False)] + scarf('side'),
    'back': [L(outline([(12, 84), (8, 34), (20, 8), (50, 0), (80, 8), (92, 34), (88, 84), (50, 90)])),
             L(outline([(20, 50), (50, 40), (90, 44), (88, 82), (50, 90), (14, 84)]), 'shade', 'b', False)] + scarf('back'),
}
# Niccolo Mantegna: melena verde menta lisa y abombada como un casco con un flequillo que le tapa un ojo; la bufanda
# granate le tapa la boca
CHARS['niccolo-mantegna'] = {
    'body': 'normal', 'pal': P('#5ab070', '#e0a060', iris='#3a3a3a', shade='#428a54'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': longhair('front', 98, 0, top=-6)
             + [L(outline([(12, 70), (14, 40), (30, 18), (52, 12), (74, 18), (88, 40), (90, 70), (80, 72), (72, 58), (60, 52), (50, 52), (40, 70), (34, 84, 1), (28, 64), (20, 70)]), 'mid', 'f', ln=True)]
             + scarf('front', up=True),
    'side': longhair('side', 98, 0, top=-6) + scarf('side', up=True),
    'back': longhair('back', 98, 0, top=-6, ends=0) + scarf('back'),
}
# Damien Crawford: un turbante granate enrollado que le tapa un ojo, con un mechón morado que sale en punta por arriba y a
# un lado; el otro ojo blanco de enfado
CHARS['damien-crawford'] = {
    'body': 'normal', 'pal': P('#5a4aa0', '#c88a50', shade='#40347a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin'),
              L(outline([(40, 10), (60, -6), (90, -4), (104, 20, 1), (90, 14), (70, 14)]), 'mid', 'b', ln=True)]
             + turban('front', 66)
             + [L(outline([(60, 2), (82, 8), (92, 30), (90, 92), (76, 94), (62, 60)]), 'scarf', 'f', ln=True)]
             + [L(quad((64, 20 + k * 14), (78, 24 + k * 14), (90, 20 + k * 14)), 'scarf_d', 'f', False, False, 1.2) for k in range(5)]
             + white_eyes(76, 16, 5.4, 6, 2)[:2] + [L([(22, 70), (40, 72)], OUTC, 'f', False, False, 2.2)] + scarf('front'),
    'side': [L(blob(SIDE_SKULL), 'skin'), L(outline([(10, 20), (20, -10), (50, -16), (70, -6), (80, 10, 1), (60, 4), (36, 6)]), 'mid', 'f', ln=True)]
            + turban('side', 62) + side_eye(78) + scarf('side'),
    'back': [L(blob(SKULL_B), 'skin'), L(outline([(10, 20), (6, -6, 1), (30, -10), (60, -14), (90, -10), (96, 10, 1), (80, 6)]), 'mid', 'f', ln=True)]
            + turban('back', 66) + scarf('back'),
}
# Avinash Chowdhury: melena gris lila lisa peinada hacia atrás, larga por los lados; una joya roja en la frente, cejas gris
# claro, ojos amarillos y la bufanda subida hasta la nariz
CHARS['avinash-chowdhury'] = {
    'body': 'normal', 'pal': P('#c0c4d8', '#a8703e', iris='#c8b820', shade='#9a9eb4', gem='#c81e2a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'hairline': [(14, 80), (16, 50), (30, 36), (50, 34), (70, 36), (84, 50), (86, 80)]},
    'front': longhair('front', 118, 4, part=True) + [L(ell(50, 50, 3.4, 3.8), 'gem', 'f', ln=True),
                                                     L(outline([(24, 64), (40, 62), (42, 66), (26, 68)]), 'mid', 'f', ln=True), L(outline([(76, 64), (60, 62), (58, 66), (74, 68)]), 'mid', 'f', ln=True)]
             + scarf('front', up=True),
    'side': longhair('side', 118, 4) + scarf('side', up=True),
    'back': longhair('back', 110, 4, part=True, ends=0) + scarf('back'),
}
# Sedgley Scofield: un gorro de tela verde agua abombado y arrugado, con un pañuelo granate enrollado por debajo que le cae por
# un lado, y la bufanda subida hasta la nariz; ojos azules de enfado y cejas verdes
CHARS['sedgley-scofield'] = {
    'body': 'normal', 'pal': P('#a8e0c8', '#c88a50', iris='#2a8ab0', shade='#80b8a0'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin'),
              L(outline([(-2, 54), (-6, 34), (6, 10), (30, -4), (54, -6), (78, 0), (96, 14), (104, 36), (98, 54), (50, 46)]), 'mid', 'f', ln=True),
              L(outline([(60, -2), (92, 12), (102, 38), (96, 52), (76, 46)]), 'shade', 'f', False)]
             + turban('front', 64, tail=1)[:3]
             + [L(outline([(80, 34), (92, 36), (94, 92), (82, 96)]), 'scarf', 'f', ln=True),
                L(outline([(22, 66), (38, 62), (42, 68), (26, 70)]), 'mid', 'f', ln=True), L(outline([(78, 66), (62, 62), (58, 68), (74, 70)]), 'mid', 'f', ln=True)]
             + scarf('front', up=True),
    'side': [L(blob(SIDE_SKULL), 'skin'),
             L(outline([(-6, 60), (-10, 30), (6, 4), (40, -10), (76, -6), (100, 14), (108, 38), (96, 52), (60, 46), (20, 54)]), 'mid', 'f', ln=True)]
            + turban('side', 60)[:1] + scarf('side', up=True),
    'back': [L(blob(SKULL_B), 'skin'),
             L(outline([(-6, 70), (-8, 34), (6, 8), (30, -6), (70, -6), (94, 8), (108, 34), (106, 70), (50, 76)]), 'mid', 'f', ln=True),
             L(outline([(56, -4), (94, 10), (106, 40), (104, 68), (64, 72)]), 'shade', 'f', False)] + scarf('back'),
}
# Grizzler Bruin (portero suplente): grandullón de cabeza redonda morena con un pañuelo granate atado en lo alto, y una
# banda verde azulada alrededor de la cabeza a la altura de la frente; gafas de sol negras y una sonrisa de dientes
CHARS['grizzler-bruin'] = {
    'body': 'corpulento', 'pal': P('#3a7a6a', '#c8843e', shade='#2a5a4e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 9},
    'front': bald('front') + [L(outline([(6, 74), (6, 46), (94, 46), (94, 74), (82, 92), (80, 64), (20, 64), (18, 92)]), 'mid', 'f', ln=True)]
             + bandana('front', 'scarf', 'scarf_d', low=46, tails=False)
             + [L(outline([(24, 70), (42, 70), (40, 76), (26, 76)]), OUTC, 'f', False), L(outline([(76, 70), (58, 70), (60, 76), (74, 76)]), OUTC, 'f', False),
                L(outline([(44, 74), (56, 74), (58, 90), (42, 90)]), 'skin_d', 'f', ln=True),
                L(outline([(28, 94), (50, 96), (72, 94), (66, 108), (34, 108)]), WHITE, 'f', ln=True)]
             + [L([(x, 95), (x, 107)], OUTC, 'f', False, False, 0.8) for x in (36, 44, 52, 60)] + scarf('front'),
    'side': bald('side') + [L(outline([(10, 70), (10, 46), (90, 50), (90, 64), (60, 68), (40, 80), (24, 82)]), 'mid', 'f', ln=True)]
            + bandana('side', 'scarf', 'scarf_d', low=42, tails=False) + scarf('side'),
    'back': bald('back') + [L(outline([(6, 76), (6, 50), (94, 50), (94, 76), (50, 80)]), 'mid', 'f', ln=True)]
            + bandana('back', 'scarf', 'scarf_d', low=48, tails=False)
            + [L(outline([(40, 54), (50, 50), (60, 54), (56, 64), (50, 58), (44, 64)]), 'scarf', 'f', ln=True)] + scarf('back'),
}
# Ian C. Wincy: pelo verde oliva de puntas cortas que asoma bajo un turbante granate enrollado del que cae una punta por un
# lado; flequillo de mechones verdes, ojos verdes y una sonrisa
CHARS['ian-c-wincy'] = {
    'body': 'normal', 'pal': P('#6a8a2a', '#fcd0a0', iris='#2a7a4a', shade='#4e6a1e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': messy('front', 9, 10, seed=1603, rx=48, ry=40, cy=36, lo=70)
             + turban('front', 52, tail=1)
             + [L(outline([(16, 50), (24, 50), (36, 52), (46, 50), (54, 54), (50, 66, 1), (42, 58), (34, 64, 1), (28, 58), (20, 66, 1)]), 'mid', 'f', ln=True)] + scarf('front'),
    'side': messy('side', 10, 8, seed=1603, rx=46, ry=40, cy=36, nape=90) + turban('side', 48) + scarf('side'),
    'back': messy('back', 9, 10, seed=1603, rx=48, ry=40, cy=36, nape=90) + turban('back', 52)
            + [L(outline([(70, 30), (84, 30), (88, 80), (76, 84)]), 'scarf', 'f', ln=True)] + scarf('back'),
}
# Bandy Horsman: cara larguísima con barba rubia hasta el pecho; un pañuelo granate atado en la cabeza con una tira que le
# cruza la cara; ojos de enfado y una nariz enorme
CHARS['bandy-horsman'] = {
    'body': 'normal', 'pal': P('#e8c060', '#a87048', shade='#c09a40', nose='#e0905a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'face_front': LONG_FACE, 'hairline': False, 'big_ears': 3, 'ear_out': 7},
    'front': bald('front') + bandana('front', 'scarf', 'scarf_d', low=50, tails=False)
             + [L(outline([(18, 70), (24, 72), (26, 100), (38, 116), (50, 120), (62, 116), (74, 100), (76, 72), (82, 70), (82, 108), (68, 128), (50, 136, 1), (32, 128), (18, 108)]), 'mid', 'f', ln=True),
                L(outline([(44, 74), (56, 74), (64, 102), (50, 108), (36, 102)]), 'nose', 'f', ln=True)] + scarf('front', top=104),
    'side': bald('side') + bandana('side', 'scarf', 'scarf_d', low=46, tails=False)
            + [L(outline([(56, 70), (62, 70), (68, 104), (82, 118), (92, 116), (90, 128), (70, 134), (56, 110)]), 'mid', 'f', ln=True),
               L(outline([(86, 74), (106, 100), (88, 104)]), 'nose', 'f', ln=True), L([(10, 46), (40, 96)], 'scarf_d', 'f', False, False, 1.4)] + scarf('side', top=104),
    'back': bald('back') + bandana('back', 'scarf', 'scarf_d', low=50, tails=False) + [L([(60, 46), (80, 96)], 'scarf_d', 'f', False, False, 1.4)] + scarf('back', top=104),
}
# Ali Caiman: un turbante granate enorme enrollado alrededor de la cabeza que le tapa un ojo, con pinchos de pelo negro
# verdoso asomando por arriba y por los lados; una pintura negra bajo el ojo visible, que es amarillo
CHARS['ali-caiman'] = {
    'body': 'normal', 'pal': P('#2a3a34', '#c88a50', shade='#1e2a26', paint='#1e1e1e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 100, 'hairline': False},
    'front': [L(blob(SKULL_F), 'skin'),
              L(outline([(16, 10), (14, -8, 1), (30, 0), (40, -14, 1), (50, 0), (64, -12, 1), (70, 2), (86, -4, 1), (84, 12)]), 'mid', 'b', ln=True),
              L(outline([(14, 84), (4, 92, 1), (20, 96)]), 'mid', 'f', ln=True), L(outline([(86, 84), (96, 92, 1), (80, 96)]), 'mid', 'f', ln=True)]
             + bandana('front', 'scarf', 'scarf_d', low=72, tails=False)
             + [L(quad((10, 40), (50, 30), (90, 40)), 'scarf_d', 'f', False, False, 1.4), L(quad((10, 58), (50, 48), (90, 58)), 'scarf_d', 'f', False, False, 1.4),
                L(ell(36, 80, 6, 6), WHITE, 'f', ln=True), L(ell(36, 80, 3, 3), (220, 200, 40, 255), 'f', False), L(ell(36, 80, 1.4, 1.4), OUTC, 'f', False),
                L(outline([(34, 86), (40, 86), (40, 100), (36, 106, 1)]), 'paint', 'f', False)] + scarf('front'),
    'side': [L(blob(SIDE_SKULL), 'skin'), L(outline([(30, 10), (34, -10, 1), (46, 0), (56, -12, 1), (62, 4)]), 'mid', 'b', ln=True)]
            + bandana('side', 'scarf', 'scarf_d', low=68, tails=False) + scarf('side'),
    'back': [L(blob(SKULL_B), 'skin'), L(outline([(16, 10), (14, -8, 1), (30, 0), (40, -14, 1), (50, 0), (64, -12, 1), (70, 2), (86, -4, 1), (84, 12)]), 'mid', 'b', ln=True),
             L(outline([(14, 84), (86, 84), (80, 96), (50, 100), (20, 96)]), 'mid', 'b', ln=True)]
            + bandana('back', 'scarf', 'scarf_d', low=72, tails=False) + scarf('back'),
}
# Chris Ellis: piel morena; pelo negro liso cortado en casco con las puntas abiertas a los lados y una cinta granate ancha
# en la frente; ojos azules grandes y la boca seria
CHARS['chris-ellis'] = {
    'body': 'normal', 'pal': P('#1e2228', '#a8703e', iris='#2a7ab0', shade='#141618'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': longhair('front', 92, 22, top=-4)
             + [L(outline([(16, 50), (16, 22), (30, 6), (50, 2), (70, 6), (84, 22), (84, 50), (50, 44)]), 'scarf', 'f', ln=True)] + scarf('front'),
    'side': longhair('side', 92, 20, top=-4) + [L(outline([(40, 46), (40, 20), (56, 4), (80, 6), (90, 24), (88, 44)]), 'scarf', 'f', ln=True)] + scarf('side'),
    'back': longhair('back', 92, 22, top=-4, ends=0) + scarf('back'),
}
