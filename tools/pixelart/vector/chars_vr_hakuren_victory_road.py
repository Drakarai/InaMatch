"""Instituto Alpino de Victory Road (vr-hakuren-victory-road): el Hakuren de Inazuma Eleven: Victory Road, con los modelos
3D de 'イナズマイレブン 英雄たちのヴィクトリーロード' de la enciclopedia (busto de frente, perfil y espalda). Cada uno tiene una
sola forma en Victory Road; ninguno coge por prefijo el dibujo de otro personaje."""
import math

from chars import CHARS, L, OUTC, blob, ell, hexc, outline, pal, rope, strand  # noqa: F401
from heads import quad  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (30, 28, 38, 255)
BLUSH = (246, 168, 160, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


def curls(cx, cy, r, n=8, a0=0.0, k2=0.8):
    """Contorno de nube (bultos redondos alrededor de un centro)."""
    pts = []
    for i in range(n * 2):
        a = a0 + math.pi * 2 * i / (n * 2)
        k = 1.0 if i % 2 == 0 else k2
        pts.append((cx + r[0] * k * math.cos(a), cy + r[1] * k * math.sin(a)))
    return blob(pts, 6)


def puff(cx, cy, rx, ry, n, rr, c='mid', z='b', a0=0.0, low=None, ln=False):
    """Nube esponjosa: una elipse rellena con bolas alrededor (las de abajo, del color low si se da)."""
    out = [L(ell(cx, cy, rx, ry), c, z)]
    for i in range(n):
        a = a0 + math.pi * 2 * i / n
        col = low if (low and math.sin(a) > 0.35) else c
        out.append(L(ell(cx + rx * math.cos(a), cy + ry * math.sin(a), rr, rr * 0.92), col, z, True, ln))
    return out


def bun(cx, cy, rx, ry, c='mid', sh='shade'):
    """Moño redondo con sombra abajo a la derecha."""
    return [L(ell(cx, cy, rx, ry), c), L(ell(cx + rx * 0.22, cy + ry * 0.22, rx * 0.78, ry * 0.78), sh, 'b', False),
            L(ell(cx - rx * 0.12, cy - ry * 0.14, rx * 0.74, ry * 0.7), c, 'b', False)]


def petal(c, ang, r0, r1, w0, w1):
    """Pétalo (o aleta) que sale del punto c hacia el ángulo ang (grados; 0 = arriba, positivo = derecha de la imagen)."""
    a = math.radians(ang)
    ux, uy = math.sin(a), -math.cos(a)
    px, py = -uy, ux
    p0 = (c[0] + ux * r0, c[1] + uy * r0)
    p1 = (c[0] + ux * r1, c[1] + uy * r1)
    tip = (c[0] + ux * (r1 + w1 * 0.25), c[1] + uy * (r1 + w1 * 0.25))
    return outline([(p0[0] - px * w0 / 2, p0[1] - py * w0 / 2), (p1[0] - px * w1 / 2, p1[1] - py * w1 / 2), tip,
                    (p1[0] + px * w1 / 2, p1[1] + py * w1 / 2), (p0[0] + px * w0 / 2, p0[1] + py * w0 / 2)], 4)


def blush(y=88, dx=19, r=(4.4, 2.4)):
    return [L(ell(50 - dx, y, *r), BLUSH, 'f', False), L(ell(50 + dx, y, *r), BLUSH, 'f', False)]


def freckles(y=86, dx=20):
    out = []
    for s in (-1, 1):
        for ox, oy in ((-3, 0), (0, 2), (3, 0), (1, -2)):
            out.append(L(ell(50 + s * dx + ox, y + oy, 0.7, 0.7), (170, 110, 80, 255), 'f', False))
    return out


# Gael Vehemaint (Mashuu Isshin, portero): pelo azul marino enorme de pinchos que salen en todas direcciones, con la parte
# de abajo negra que le tapa la frente hasta los ojos; ojos lilas en espiral con marcas azules debajo
SPIR, SPIR_D, NAVY = hexc('#a07ad8'), hexc('#5a3a9a'), hexc('#2a2a6a')


def spiral_eyes(y=79):
    out = []
    for cx in (36, 64):
        out += [L(ell(cx, y, 5.6, 5.6), OUTC, 'f', False), L(ell(cx, y, 4.6, 4.6), WHITE, 'f', False), L(ell(cx, y, 3.8, 3.8), SPIR, 'f', False),
                L(ell(cx, y, 2.7, 2.7), WHITE, 'f', False), L(ell(cx, y, 1.8, 1.8), SPIR_D, 'f', False)]
        s = -1 if cx < 50 else 1
        out.append(L(quad((cx - 6 * s, 84), (cx - 1 * s, 89), (cx + 4 * s, 86)), NAVY, 'f', False, False, 1.8))
    return out


CHARS['gael-vehemaint'] = {
    'body': 'normal', 'pal': pal('#1e3a7a', '#fcd8b8', iris='#a07ad8', light='#3a62b0', under='#1c1c2a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 96,
             'hairline': [(14, 78), (18, 68), (34, 70), (50, 69), (66, 70), (82, 68), (86, 78)]},
    'front': [L(outline([(18, 76), (16, 56), (30, 48), (70, 48), (84, 56), (82, 76), (70, 70), (50, 70), (30, 70)]), 'under'),
              L(outline([(18, 64), (8, 76, 1), (13, 58), (-4, 52, 1), (12, 44), (2, 28, 1), (20, 30), (18, 6, 1), (34, 20), (42, -4, 1), (50, 16), (62, 0, 1),
                         (64, 16), (84, 10, 1), (76, 26), (98, 32, 1), (84, 42), (94, 58, 1), (82, 56), (80, 64), (70, 54), (30, 54)])),
              L(outline([(62, 2), (64, 16), (84, 10), (76, 26), (98, 32), (84, 42), (94, 58), (80, 50), (66, 30)]), 'shade', 'b', False),
              L(outline([(26, 24), (40, 6), (46, 22), (32, 34)]), 'light', 'b', False),
              strand([(30, 34), (44, 46)], 'deep', 'b', 1.0), strand([(56, 24), (60, 44)], 'deep', 'b', 1.0),
              fringe([(38, 46), (58, 44), (58, 54), (52, 72, 1), (46, 56)]), *spiral_eyes()],
    'side': [L(outline([(12, 50), (40, 50), (62, 56), (82, 60), (84, 70), (70, 64), (54, 62), (40, 64), (34, 78), (20, 84), (10, 74), (6, 60)]), 'under'),
             L(outline([(78, 62), (94, 80, 1), (84, 54), (94, 42, 1), (78, 36), (86, 20, 1), (66, 24), (62, -2, 1), (52, 18), (38, 6, 1), (36, 24), (18, 20, 1),
                        (26, 34), (4, 40, 1), (16, 48), (-6, 60, 1), (14, 62), (6, 80, 1), (24, 66), (40, 56), (56, 54), (70, 56)])),
             L(outline([(4, 40), (16, 48), (-6, 60), (14, 62), (6, 80), (24, 66), (40, 56), (30, 44)]), 'shade', 'b', False),
             strand([(50, 20), (60, 40)], 'deep', 'b', 1.0), strand([(30, 30), (44, 46)], 'deep', 'b', 1.0),
             L(quad((76, 85), (80, 89), (85, 86)), NAVY, 'f', False, False, 1.8),
             L(ell(82, 79, 4, 5), OUTC, 'f', False), L(ell(82.6, 79, 3, 4), WHITE, 'f', False), L(ell(83, 79, 2.2, 3), SPIR, 'f', False),
             L(ell(83.2, 79, 1.1, 1.6), WHITE, 'f', False)],
    'back': [L(outline([(18, 50), (82, 50), (84, 70), (76, 86), (56, 90), (50, 98, 1), (44, 90), (24, 86), (16, 70)]), 'under'),
             L(outline([(20, 62), (-2, 52, 1), (16, 46), (2, 28, 1), (22, 32), (24, 8, 1), (40, 24), (46, -2, 1), (54, 20), (70, 4, 1), (68, 24), (96, 30, 1),
                        (80, 42), (98, 58, 1), (80, 58), (70, 56), (50, 58), (30, 58)])),
             L(outline([(54, 20), (70, 4), (68, 24), (96, 30), (80, 42), (98, 58), (80, 58), (60, 50)]), 'shade', 'b', False)],
}

# Targan Snowbringer (Fuuren Shiroya): melena gris clara enorme, ondulada y revuelta hasta los hombros, con mechones que le
# caen entre los ojos; la parte de abajo malva; ojos caídos medio cerrados, con cara de sueño
CHARS['targan-snowbringer'] = {
    'body': 'delgado', 'pal': pal('#c4c8d2', '#fcdcc4', iris='#5a6070', shade='#a0929c', deep='#7a6c78', light='#eaf2fa'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'line', 'mouth_y': 95, 'eye_y': 78, 'hairline': False, 'ears': False},
    'front': [L(outline([(24, 102), (14, 106), (16, 92), (4, 90), (12, 80), (2, 70), (12, 62), (2, 50), (14, 44), (6, 30), (20, 26), (20, 8),
                         (34, 14), (44, -2), (54, 10), (68, 0), (70, 14), (86, 10), (82, 26), (96, 30), (86, 42), (98, 50), (86, 58), (96, 70),
                         (86, 78), (96, 90), (84, 92), (86, 106), (76, 100), (72, 86), (28, 86)])),
              L(outline([(4, 70), (14, 66), (26, 86), (24, 102), (14, 106), (16, 92), (4, 90), (12, 80)]), 'shade', 'b', False),
              L(outline([(96, 70), (86, 66), (74, 86), (76, 100), (86, 106), (84, 92), (96, 90), (88, 80)]), 'shade', 'b', False),
              L(outline([(22, 30), (40, 14), (56, 18), (40, 30)]), 'light', 'b', False),
              *[L([(cx - 6.4, 73), (cx + 6.4, 73), (cx + 6.4, 77.5), (cx - 6.4, 77.5)], 'skin', 'f', False) for cx in (36, 64)],
              *[L([(cx - 6, 77.5), (cx + 6, 77.5)], OUTC, 'f', False, False, 2.2) for cx in (36, 64)],
              fringe([(18, 84), (14, 60), (24, 44), (50, 36), (76, 44), (86, 60), (82, 84), (76, 66), (68, 58), (64, 72), (58, 58), (48, 60), (42, 74),
                      (38, 60), (28, 62), (24, 76)]),
              strand([(30, 46), (36, 60)], 'deep', 'f', 1.0), strand([(66, 46), (62, 58)], 'deep', 'f', 1.0)],
    'side': [L(outline([(62, 96), (56, 108), (48, 96), (36, 108), (30, 96), (14, 104), (14, 92), (-2, 90), (4, 78), (-6, 64), (2, 56), (-4, 40),
                        (6, 34), (4, 18), (18, 18), (22, 2), (36, 8), (50, -2), (58, 8), (74, 6), (76, 18), (90, 24), (86, 34), (96, 44), (84, 48),
                        (88, 64), (78, 58), (70, 64), (66, 80)])),
             L(outline([(-4, 40), (40, 30), (66, 72), (62, 96), (56, 108), (48, 96), (36, 108), (30, 96), (14, 104), (14, 92), (-2, 90), (4, 78)]), 'shade', 'b', False),
             L(outline([(30, 20), (50, 8), (64, 16), (46, 30)]), 'light', 'b', False),
             L([(76, 73), (87, 73), (87, 77.5), (76, 77.5)], 'skin', 'f', False), L([(77, 77.5), (86, 77.5)], OUTC, 'f', False, False, 2.2)],
    'back': [L(outline([(14, 104), (4, 92), (10, 80), (0, 66), (8, 56), (0, 40), (10, 32), (8, 16), (24, 14), (30, 2), (44, 8), (56, 0), (64, 10),
                        (80, 8), (80, 22), (94, 28), (88, 40), (98, 54), (90, 62), (98, 76), (88, 82), (94, 96), (84, 98), (80, 108), (66, 100),
                        (50, 110), (36, 100), (22, 108)])),
             L(outline([(4, 36), (50, 28), (96, 36), (94, 96), (80, 108), (66, 100), (50, 110), (36, 100), (22, 108), (14, 104), (4, 92)]), 'shade', 'b', False),
             L(outline([(26, 20), (44, 10), (60, 14), (40, 28)]), 'light', 'b', False)],
}

# Berta Brunche (Kumamori Nenemi): grandullona de pelo gris caqui recogido en cuatro moños redondos enormes (dos arriba y dos
# a los lados), con coleteros blancos, y el flequillo abierto en dos que le tapa los lados de la cara; ojos cerrados de
# felicidad con pestañas y una boca grande abierta
CHARS['berta-brunche'] = {
    'body': 'corpulento', 'pal': pal('#b4ac94', '#fce4d4', shade='#9a8070', deep='#7a6458', light='#d4ccb4', lip='#e04a4a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'ears': False,
             'hairline': [(18, 82), (24, 64), (36, 56), (50, 54), (64, 56), (76, 64), (82, 82)]},
    'front': [*bun(11, 72, 11, 12), *bun(89, 72, 11, 12), *bun(31, 28, 18, 16), *bun(69, 28, 18, 16),
              L(ell(40, 44, 5, 3.4), WHITE, 'b', ln=True), L(ell(60, 44, 5, 3.4), WHITE, 'b', ln=True),
              L(ell(19, 64, 3, 4.4), WHITE, 'b', ln=True), L(ell(81, 64, 3, 4.4), WHITE, 'b', ln=True),
              L(outline([(20, 96), (16, 70), (20, 50), (34, 40), (50, 38), (66, 40), (80, 50), (84, 70), (80, 96), (70, 90), (30, 90)])),
              fringe([(17, 90), (16, 64), (24, 50), (40, 44), (50, 50), (60, 44), (76, 50), (84, 64), (83, 90), (78, 94, 1), (74, 74), (66, 62), (52, 56),
                      (50, 60), (48, 56), (34, 62), (26, 74), (22, 94, 1)]),
              L(outline([(60, 46), (76, 50), (84, 64), (83, 90), (78, 94), (74, 74), (66, 60)]), 'shade', 'f', False),
              *[L(quad((cx - 6, 80), (cx, 74), (cx + 6, 80)), OUTC, 'f', False, False, 2.2) for cx in (37, 63)],
              *[L([(cx + dx, 80), (cx + dx * 1.3, 83)], OUTC, 'f', False, False, 1.2) for cx in (37, 63) for dx in (-5, 0, 5)],
              L(quad((40, 91), (50, 90), (60, 91)) + quad((60, 91), (50, 103), (40, 91))[1:], 'lip', 'f', ln=True),
              *blush(88, 20)],
    'side': [*bun(8, 74, 11, 12), *bun(58, 16, 13, 12), *bun(34, 22, 19, 17),
             L(ell(18, 66, 3, 4.4), WHITE, 'b', ln=True), L(ell(46, 34, 5, 3.4), WHITE, 'b', ln=True),
             L(outline([(62, 100), (50, 94), (30, 92), (14, 82), (10, 62), (16, 42), (30, 32), (50, 28), (70, 34), (84, 48), (90, 62), (84, 66), (78, 58), (72, 66),
                        (74, 98)])),
             L(outline([(14, 70), (40, 70), (58, 96), (50, 94), (30, 92), (16, 84)]), 'shade', 'b', False),
             L(quad((76, 80), (80, 75), (85, 80)), OUTC, 'f', False, False, 2.0), L(ell(86, 92, 2.4, 2), 'lip', 'f', False),
             L(ell(82, 87, 3.6, 2.2), BLUSH, 'f', False)],
    'back': [*bun(10, 72, 11, 11), *bun(90, 72, 11, 11), *bun(31, 28, 18, 17), *bun(69, 28, 18, 17),
             L(ell(20, 66, 3, 4.4), WHITE, 'b', ln=True), L(ell(80, 66, 3, 4.4), WHITE, 'b', ln=True),
             L(outline([(24, 92), (18, 66), (26, 44), (50, 36), (74, 44), (82, 66), (76, 92), (50, 96)])),
             L(outline([(52, 40), (74, 44), (82, 66), (76, 92), (56, 94)]), 'shade', 'b', False)],
}

# Mateo Potensio (Maruma Roman): grandullón de cara redonda y mofletuda; pelo de lana de oveja gris claro que le tapa los ojos,
# con rizos en espiral en el flequillo; solo se le ven la nariz y una sonrisa ancha
SWIRL = (110, 90, 84, 255)


def swirl(cx, cy, s=1, r=4.0):
    pts = [(cx + s * r * (1 - t / 14) * math.cos(t * 0.6), cy + r * (1 - t / 14) * math.sin(t * 0.6)) for t in range(12)]
    return L(pts, SWIRL, 'f', False, False, 1.1)


CHARS['mateo-potensio'] = {
    'body': 'corpulento', 'pal': pal('#c8c0b0', '#fcdcc4', shade='#a88c80', deep='#86706a', light='#e2dccf'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'ears': False,
             'hairline': [(8, 92), (16, 80), (30, 78), (50, 80), (70, 78), (84, 80), (92, 92)],
             'face_front': blob([(14, 56), (50, 48), (86, 56), (92, 80), (84, 100), (64, 110), (50, 111), (36, 110), (16, 100), (8, 80)])},
    'front': [*puff(14, 82, 5, 10, 4, 8, low='shade'), *puff(86, 82, 5, 10, 4, 8, low='shade'), *puff(50, 44, 34, 28, 11, 11, low='shade', a0=0.3),
              L(ell(46, 22, 14, 7), 'light', 'b', False),
              swirl(30, 72, -1), swirl(70, 72, 1), swirl(44, 66, 1, 3.2), swirl(56, 66, -1, 3.2),
              L(ell(46.5, 85, 1.3, 1.1), SWIRL, 'f', False), L(ell(53.5, 85, 1.3, 1.1), SWIRL, 'f', False),
              L(quad((34, 90), (50, 99), (66, 90)), OUTC, 'f', False, False, 1.6), *blush(92, 24, (5, 2.6))],
    'side': [*puff(40, 76, 30, 10, 8, 10, 'shade'), *puff(42, 40, 34, 26, 10, 11, low='shade', a0=0.2),
             L(ell(40, 18, 14, 7), 'light', 'b', False), swirl(76, 66, 1),
             L(quad((80, 92), (85, 94), (89, 91)), OUTC, 'f', False, False, 1.4)],
    'back': [*puff(50, 80, 38, 10, 9, 10, 'shade'), *puff(50, 42, 36, 28, 11, 11, low='shade', a0=0.3)],
}

# Ivar Trialton (Tobou Hatsuyuki): gorro de lana gris azulado con un pegote de nieve y el borde de canalé, y unas gafas de
# esquí enormes de cristal naranja que le tapan los ojos; mechones castaños de pinchos asoman por los lados y uno cae por la
# frente sobre las gafas; sonríe
CAPC, CAPD, FRAME, LENS, LENS_L, LENS_D = hexc('#7a82b4'), hexc('#5c6496'), hexc('#2c4648'), hexc('#f07a1e'), hexc('#ffd04a'), hexc('#b03a12')


def ribs(x0, x1, y0, y1, n=7):
    return [L([(x0 + (x1 - x0) * i / n, y0), (x0 + (x1 - x0) * i / n, y1)], OUTC, 'f', False, False, 0.7) for i in range(1, n)]


CHARS['ivar-trialton'] = {
    'body': 'normal', 'pal': pal('#6a4036', '#f8c8a8', shade='#4e2e28'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'ears': False, 'hairline': False},
    'front': [L(outline([(20, 96), (6, 94, 1), (16, 86), (2, 76, 1), (16, 70), (14, 50), (86, 50), (84, 70), (98, 76, 1), (84, 86), (94, 94, 1), (80, 96), (80, 80),
                         (20, 80)])),
              L(outline([(12, 52), (10, 30), (16, 10), (30, -2), (50, -8), (70, -2), (84, 10), (90, 30), (88, 52)]), CAPC, 'f'),
              L(outline([(56, -4), (76, 4), (86, 22), (88, 34), (70, 30)]), CAPD, 'f', False),
              L(outline([(10, 32), (50, 28), (90, 32), (89, 52), (50, 50), (11, 52)]), CAPD, 'f', ln=True), *ribs(10, 90, 31, 51, 9),
              L(blob([(56, -10), (66, -14), (76, -10), (74, -3), (60, -3)], 6), WHITE, 'f', ln=True), L(ell(46, -4, 2.6, 1.8), WHITE, 'f', ln=True),
              L(outline([(4, 56), (96, 56), (96, 64), (4, 64)]), FRAME, 'f'),
              L(outline([(10, 52), (50, 50), (90, 52), (92, 66), (88, 82), (66, 82), (50, 76), (34, 82), (12, 82), (8, 66)]), FRAME, 'f'),
              L(outline([(15, 56), (50, 54), (85, 56), (86, 66), (83, 78), (66, 78), (50, 72), (34, 78), (17, 78), (14, 66)]), LENS, 'f', False),
              L([(22, 57), (30, 57), (26, 77), (19, 77)], LENS_L, 'f', False), L([(68, 56), (76, 56), (74, 77), (66, 77)], LENS_L, 'f', False),
              L([(36, 56), (40, 56), (38, 77), (34, 77)], LENS_D, 'f', False), L([(80, 57), (84, 57), (83, 74), (79, 76)], LENS_D, 'f', False),
              fringe([(34, 46), (40, 36), (54, 36), (64, 44), (54, 46), (44, 68, 1), (42, 50)])],
    'side': [L(outline([(54, 82), (40, 92, 1), (36, 78), (20, 86, 1), (22, 72), (6, 72, 1), (12, 58), (60, 58), (64, 72)])),
             L(outline([(8, 58), (4, 34), (12, 10), (34, -6), (60, -6), (80, 6), (90, 28), (92, 52), (50, 56)]), CAPC),
             L(outline([(5, 36), (48, 40), (92, 32), (92, 52), (50, 56), (8, 58)]), CAPD, 'b', ln=True), *ribs(8, 90, 37, 55, 8),
             L(blob([(40, -8), (50, -12), (58, -8), (52, -2)], 6), WHITE, 'b', ln=True),
             L(outline([(70, 46), (82, 42), (88, 48), (94, 36, 1), (92, 50), (80, 52)])),
             L(outline([(6, 54), (78, 52), (78, 64), (8, 66)]), FRAME),
             L(outline([(72, 48), (97, 46), (99, 80), (74, 80)]), FRAME), L(outline([(78, 52), (96, 50), (96, 76), (80, 76)]), LENS, 'b', False),
             L([(84, 51), (89, 51), (89, 76), (84, 76)], LENS_L, 'b', False)],
    'back': [L(outline([(20, 90), (6, 92, 1), (14, 82), (0, 76, 1), (14, 70), (16, 56), (84, 56), (86, 70), (100, 76, 1), (86, 82), (94, 92, 1), (80, 90), (66, 96, 1),
                        (58, 88), (50, 98, 1), (42, 88), (34, 96, 1)])),
             L(outline([(12, 60), (8, 34), (16, 10), (30, -4), (50, -10), (70, -4), (84, 10), (92, 34), (88, 60), (50, 62)]), CAPC),
             L(outline([(58, -6), (80, 6), (90, 30), (70, 30)]), CAPD, 'b', False),
             L(outline([(9, 38), (50, 36), (91, 38), (89, 58), (50, 60), (11, 58)]), CAPD, 'b', ln=True), *ribs(10, 90, 37, 59, 9),
             L(outline([(10, 58), (90, 58), (88, 66), (12, 66)]), FRAME)],
}

# Anastasia Mingler (Shumari Horoka): melena crema enorme y redonda, como un champiñón, con un flequillo más claro que le
# enmarca la cara y la parte de abajo rosada; cascos negros con la diadema por encima; ojos grandes negros y coloretes
CHARS['anastasia-mingler'] = {
    'body': 'chica', 'pal': pal('#f6eedc', '#fde4d4', iris='#26222e', shade='#e2b8aa', deep='#c89a8c', light='#fffaf0'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'ears': False,
             'hairline': [(20, 84), (22, 64), (34, 60), (42, 66), (50, 58), (58, 66), (66, 60), (78, 64), (80, 84)]},
    'front': [L(outline([(-2, 98), (-6, 70), (0, 42), (18, 20), (50, 10), (82, 20), (100, 42), (106, 70), (102, 98), (80, 104), (50, 106), (20, 104)])),
              L(outline([(-4, 74), (20, 84), (50, 92), (80, 84), (104, 74), (102, 98), (80, 104), (50, 106), (20, 104), (-2, 98)]), 'shade', 'b', False),
              L(outline([(20, 96), (16, 70), (20, 46), (34, 32), (50, 28), (66, 32), (80, 46), (84, 70), (80, 96)]), 'light'),
              L(quad((15, 78), (50, 4), (85, 78)), BLACK, 'f', False, False, 3.6),
              L(ell(16, 80, 5, 9.6), BLACK, 'f'), L(ell(84, 80, 5, 9.6), BLACK, 'f'),
              *blush(88, 18)],
    'side': [L(outline([(14, 84), (-6, 104, 1), (2, 96), (-6, 112, 1), (22, 90)])),
             L(outline([(10, 82), (0, 56), (4, 30), (20, 10), (46, 4), (70, 10), (86, 28), (90, 46), (84, 58), (78, 48), (70, 52), (62, 66), (54, 86), (30, 88)])),
             L(outline([(2, 50), (32, 46), (44, 72), (32, 88), (10, 82)]), 'shade', 'b', False),
             L(outline([(60, 12), (84, 26), (90, 46), (84, 58), (78, 48), (70, 50), (66, 30)]), 'light', 'b', False),
             L(quad((54, 6), (52, 30), (48, 64)), BLACK, 'b', False, False, 3.6), L(ell(47, 70, 6, 9), BLACK, 'b'),
             L(ell(82, 88, 3.6, 2.2), BLUSH, 'f', False)],
    'back': [L(outline([(36, 100), (34, 110, 1), (44, 102)]), 'light'), L(outline([(64, 100), (66, 110, 1), (56, 102)]), 'light'),
             L(outline([(0, 92), (-4, 64), (4, 36), (24, 16), (50, 10), (76, 16), (96, 36), (104, 64), (100, 92), (80, 100), (50, 102), (20, 100)])),
             L(outline([(-2, 62), (30, 52), (70, 46), (102, 56), (100, 92), (80, 100), (50, 102), (20, 100), (0, 92)]), 'shade', 'b', False)],
}

# Hail Homestead (Murazumi Hakka): pelo azul lavanda en media melena con flequillo recto y mechones hasta la barbilla, y por
# detrás una flor enorme de siete pétalos de pelo (oscuros por dentro); ojos redondos verdes, dos puntitos en la frente y
# coloretes
PETAL_D = hexc('#5c5a7c')
_hc = (50, 46)
CHARS['hail-homestead'] = {
    'body': 'chica', 'pal': pal('#8c9ad2', '#fde4d4', iris='#6a8a5a', shade='#6c78b0', deep='#545c94', light='#aab6e4'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'none', 'ears': False, 'eye_y': 77,
             'hairline': [(18, 84), (20, 60), (50, 59), (80, 60), (82, 84)]},
    'front': [*[L(petal(_hc, a, 16, 46, 16, 32)) for a in (-104, -52, 0, 52, 104)],
              *[L(petal(_hc, a, 30, 46, 20, 28), 'shade', 'b', False) for a in (-104, 104)],
              L(outline([(20, 100), (16, 70), (18, 46), (32, 32), (50, 28), (68, 32), (82, 46), (84, 70), (80, 100), (72, 100), (72, 80), (28, 80), (28, 100)])),
              fringe([(17, 100), (16, 64), (22, 54), (30, 56), (28, 96), (24, 102, 1)]), fringe([(83, 100), (84, 64), (78, 54), (70, 56), (72, 96), (76, 102, 1)]),
              L(ell(47, 66, 0.9, 0.9), OUTC, 'f', False), L(ell(53, 66, 0.9, 0.9), OUTC, 'f', False),
              L(ell(50, 94, 2, 1.6), (220, 70, 70, 255), 'f', False), *blush(87, 18)],
    'side': [*[L(petal((40, 44), a, 14, 48, 16, 32)) for a in (-110, -60, -10)],
             L(petal((40, 44), -60, 34, 52, 16, 22), PETAL_D, 'b', False),
             L(outline([(58, 100), (50, 94), (30, 90), (14, 80), (10, 60), (16, 40), (30, 30), (52, 28), (72, 34), (86, 48), (90, 60), (80, 60), (70, 66), (72, 100)])),
             L(outline([(14, 66), (40, 66), (56, 96), (30, 90), (16, 82)]), 'shade', 'b', False),
             L(ell(84, 86, 3.6, 2.2), BLUSH, 'f', False)],
    'back': [L(outline([(36, 92), (34, 104, 1), (44, 94)])), L(outline([(64, 92), (66, 104, 1), (56, 94)])),
             L(outline([(22, 92), (18, 68), (26, 50), (50, 44), (74, 50), (82, 68), (78, 92), (50, 96)])),
             *[L(petal((50, 52), a, 4, 46, 6, 34)) for a in (-104, -52, 0, 52, 104)],
             *[L(petal((50, 52), a, 6, 42, 5, 27), PETAL_D, 'b', False) for a in (-104, -52, 0, 52, 104)]],
}

# Fergat Silverpine (Matsuka Motomichi): pelo rubio casi blanco, como un casco con las puntas de los lados hacia fuera, y en el
# flequillo un mechón verde con forma de pino que le cae sobre un ojo; pecas y ojos grises
GREEN = hexc('#1e8a7a')
CHARS['fergat-silverpine'] = {
    'body': 'normal', 'pal': pal('#ece6ce', '#f6d0b0', iris='#7a6e5e', shade='#c8b8a4', deep='#a89884', light='#fffbec'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(18, 84), (20, 66), (26, 72), (30, 62), (36, 70), (42, 62), (50, 68), (58, 60), (64, 70), (70, 60), (76, 70), (80, 62), (82, 84)]},
    'front': [L(outline([(22, 92), (18, 74), (4, 64, 1), (16, 58), (16, 40), (26, 24), (42, 12), (58, 12), (74, 22), (84, 40), (84, 56), (98, 62, 1), (84, 66),
                         (80, 92), (70, 84), (30, 84)])),
              L(outline([(58, 14), (76, 24), (84, 44), (84, 60), (74, 44)]), 'shade', 'b', False),
              strand([(30, 30), (26, 50)], 'deep', 'b', 1.0), strand([(68, 30), (72, 50)], 'deep', 'b', 1.0),
              L(outline([(32, 82, 1), (36, 70), (27, 72, 1), (37, 60), (29, 58, 1), (41, 50), (35, 45, 1), (46, 38), (42, 28, 1), (54, 28), (58, 36, 1), (56, 44),
                         (63, 46, 1), (56, 52), (65, 56, 1), (56, 60), (58, 70, 1), (50, 66), (45, 76, 1)]), GREEN, 'f'),
              *freckles(86, 21)],
    'side': [L(outline([(56, 64), (64, 58), (80, 62), (88, 56), (90, 40), (84, 26), (70, 14), (50, 8), (30, 10), (14, 22), (6, 40), (6, 60), (12, 76), (24, 84),
                        (34, 74), (40, 62), (48, 60)])),
             L(outline([(6, 44), (30, 50), (36, 72), (24, 84), (12, 76)]), 'shade', 'b', False),
             L(outline([(74, 28), (86, 34), (92, 48), (90, 64), (84, 76, 1), (80, 62), (74, 52)]), GREEN),
             strand([(40, 16), (50, 34)], 'deep', 'b', 1.0)],
    'back': [L(outline([(20, 90), (16, 66), (2, 60, 1), (16, 56), (16, 40), (26, 22), (50, 12), (74, 22), (84, 40), (84, 56), (98, 60, 1), (84, 66), (80, 90),
                        (50, 94)])),
             L(outline([(56, 14), (76, 24), (86, 46), (80, 90), (58, 92)]), 'shade', 'b', False),
             strand([(36, 20), (30, 60)], 'deep', 'b', 1.0), strand([(64, 20), (70, 60)], 'deep', 'b', 1.0), strand([(48, 14), (46, 50)], 'deep', 'b', 1.0)],
}

# Arlo Galbrash (Sagae Kokichi): gorro de lana amarillo con pompón crema y orejeras que bajan hasta unas trencitas crema; ojos
# grandes verde azulado y morritos
HAT, HAT_D, CREAM = hexc('#e6d672'), hexc('#c8ac5c'), hexc('#f2e8cc')


def braid(x, y0, s=1):
    return [L(ell(x, y0 + i * 7, 5.4 - i * 0.6, 4.2), CREAM, 'f', ln=True) for i in range(3)]


CHARS['arlo-galbrash'] = {
    'body': 'bajito', 'pal': pal('#3a2a26', '#fde0c8', iris='#3a9aa8'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 95, 'ears': False,
             'hairline': [(16, 82), (24, 62), (50, 60), (76, 62), (84, 82)]},
    'front': [L(curls(50, -6, (12, 9), 6), CREAM),
              L(outline([(14, 92), (10, 60), (14, 30), (30, 8), (50, 2), (70, 8), (86, 30), (90, 60), (86, 92), (76, 96), (74, 64), (26, 64), (24, 96)]), HAT),
              L(outline([(60, 6), (80, 18), (90, 50), (86, 70), (76, 40)]), HAT_D, 'b', False),
              L(outline([(14, 90), (24, 92), (24, 66), (16, 70)]), HAT_D, 'f', False), L(outline([(86, 90), (76, 92), (76, 66), (84, 70)]), HAT_D, 'f', False),
              *braid(19, 98), *braid(81, 98)],
    'side': [
             L(outline([(12, 80), (6, 52), (12, 26), (30, 8), (54, 4), (74, 12), (88, 30), (90, 50), (80, 56), (66, 58), (60, 94), (46, 96), (40, 78)]), HAT),
             L(outline([(8, 54), (40, 60), (42, 80), (14, 82)]), HAT_D, 'b', False),
             L(curls(22, 2, (12, 9), 6, 0.4), CREAM), *braid(52, 100)],
    'back': [L(outline([(26, 80), (74, 80), (70, 94), (30, 94)]), 'mid'),
             L(outline([(12, 88), (8, 56), (14, 28), (30, 8), (50, 2), (70, 8), (86, 28), (92, 56), (88, 88), (50, 84)]), HAT),
             L(outline([(10, 70), (50, 66), (90, 70), (88, 88), (50, 84), (12, 88)]), CREAM, 'b', ln=True),
             L(outline([(34, 50), (66, 50), (60, 58), (40, 58)]), HAT_D, 'b', False),
             L(curls(50, -6, (12, 9), 6), CREAM), *braid(14, 96), *braid(86, 96)],
}

# Lev Langvil (Kitahira Uryuu): pelo verde azulado oscuro enorme de pinchos revueltos, con dos mechones largos a los lados de
# la cara que bajan hasta la barbilla y se curvan hacia fuera; cejas gruesas, ojos claros caídos con raya verde y pecas
CHARS['lev-langvil'] = {
    'body': 'normal', 'pal': pal('#1e5a6a', '#f6d2b4', iris='#a8c4d4', shade='#174652', deep='#10343e', light='#3a8494'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(16, 84), (20, 62), (28, 68), (34, 58), (42, 66), (50, 56), (58, 66), (66, 58), (72, 68), (80, 62), (84, 84)]},
    'front': [L(outline([(22, 80), (16, 96), (4, 100, 1), (12, 84), (-2, 80, 1), (12, 70), (0, 56, 1), (14, 50), (4, 36, 1), (18, 32), (14, 18, 1), (26, 16),
                         (36, 6), (50, 2), (64, 6), (74, 14), (86, 16, 1), (82, 30), (98, 34, 1), (86, 46), (100, 58, 1), (88, 68),
                         (100, 82, 1), (86, 84), (96, 100, 1), (84, 96), (78, 80)])),
              L(outline([(60, 6), (70, 18), (86, 12), (82, 30), (98, 34), (86, 46), (100, 58), (88, 68), (80, 56), (70, 30)]), 'shade', 'b', False),
              L(outline([(28, 24), (42, 14), (44, 30), (32, 36)]), 'light', 'b', False),
              fringe([(18, 64), (24, 64), (26, 92), (32, 104), (22, 110, 1), (22, 100), (16, 82)]),
              fringe([(82, 64), (76, 64), (74, 92), (68, 104), (78, 110, 1), (78, 100), (84, 82)]),
              L([(28, 66), (44, 63)], 'deep', 'f', False, False, 3.2), L([(72, 66), (56, 63)], 'deep', 'f', False, False, 3.2),
              *[L(quad((cx - 6, 81), (cx, 83), (cx + 6, 81)), 'mid', 'f', False, False, 1.0) for cx in (36, 64)],
              *freckles(86, 20)],
    'side': [L(outline([(62, 62), (74, 56), (86, 58), (96, 48, 1), (86, 40), (96, 28, 1), (80, 22), (84, 6, 1), (66, 10), (62, -4, 1), (48, 8), (30, 0, 1), (28, 14),
                        (8, 12, 1), (14, 28), (-6, 36, 1), (8, 46), (-8, 60, 1), (8, 66), (-2, 82, 1), (14, 80), (10, 96, 1), (26, 86), (32, 98, 1), (40, 80), (50, 64)])),
             L(outline([(-6, 36), (40, 46), (50, 64), (40, 80), (32, 98), (26, 86), (10, 96), (14, 80), (-2, 82), (8, 66), (-8, 60), (8, 46)]), 'shade', 'b', False),
             fringe([(56, 60), (66, 62), (66, 92), (74, 104), (64, 108, 1), (58, 94)]),
             L([(72, 64), (84, 66)], 'deep', 'f', False, False, 3.0)],
    'back': [L(outline([(16, 96), (2, 100, 1), (10, 84), (-4, 78, 1), (10, 68), (-2, 54, 1), (12, 48), (2, 34, 1), (16, 30), (12, 12, 1), (30, 18), (32, 0, 1),
                        (44, 12), (52, -4, 1), (58, 10), (70, 0, 1), (70, 16), (88, 12, 1), (84, 30), (100, 34, 1), (88, 48), (102, 56, 1), (90, 68), (104, 80, 1),
                        (90, 84), (98, 100, 1), (82, 94), (70, 100, 1), (62, 90), (50, 102, 1), (40, 90), (30, 100, 1)])),
             L(outline([(4, 60), (50, 54), (96, 60), (90, 84), (98, 100), (82, 94), (70, 100), (62, 90), (50, 102), (40, 90), (30, 100), (16, 96), (2, 100), (10, 84)]),
               'shade', 'b', False)],
}

# Wren Habilton (Hieizaka Ganto): pelo verde azulado en cepillo, alto y recto como una columna con las puntas de arriba en
# zigzag, y los lados de la cabeza rapados (verde menta); orejas grandes, ojos grises con párpados caídos y ceño fruncido
MINT, KHAKI = hexc('#c4e0a4'), hexc('#a8a07a')
CHARS['wren-habilton'] = {
    'body': 'normal', 'pal': pal('#4ab8c8', '#f8c8a4', iris='#6a7a80', shade='#2e8494', deep='#1e6270', light='#7ad4dc'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'big_ears': 2,
             'hairline': [(14, 52), (30, 46), (44, 48), (50, 54), (56, 48), (70, 46), (86, 52)]},
    'front': [L(outline([(16, 56), (15, 20), (17, -20), (24, -15, 1), (31, -22), (38, -15, 1), (46, -22), (54, -15, 1), (62, -22), (70, -15, 1), (78, -22),
                         (84, -18, 1), (84, 20), (84, 56), (70, 50), (50, 50), (30, 50)])),
              L(outline([(40, 26), (50, 14), (60, 26), (56, 44), (50, 54, 1), (44, 44)]), 'shade', 'b', False),
              L(outline([(70, -16), (84, -18), (84, 50), (72, 46)]), 'shade', 'b', False),
              *[strand([(x, -14), (x, 40)], 'deep', 'b', 1.0) for x in (26, 38, 62, 74)],
              L(outline([(18, 52), (28, 50), (26, 60), (20, 68)]), MINT, 'f', False), L(outline([(82, 52), (72, 50), (74, 60), (80, 68)]), MINT, 'f', False)],
    'side': [L(outline([(14, 40), (40, 44), (60, 46), (66, 58), (54, 66), (40, 72), (20, 80), (12, 60)]), MINT),
             L(outline([(20, 50), (40, 52), (36, 66), (22, 72)]), KHAKI, 'b', False),
             L(outline([(60, 48), (72, 38), (86, 32), (92, -4), (86, -20, 1), (74, -14), (62, -22, 1), (50, -14), (38, -20, 1), (26, -12), (18, 20), (14, 42), (30, 46),
                        (48, 46)])),
             L(outline([(20, 0), (40, -6), (40, 44), (16, 42)]), 'shade', 'b', False)],
    'back': [L(outline([(18, 46), (82, 46), (82, 70), (70, 84), (50, 88), (30, 84), (18, 70)]), MINT),
             L(outline([(24, 54), (76, 54), (72, 74), (50, 84), (28, 74)]), KHAKI, 'b', False),
             L(outline([(16, 52), (15, 20), (17, -20), (24, -15, 1), (31, -22), (38, -15, 1), (46, -22), (54, -15, 1), (62, -22), (70, -15, 1), (78, -22),
                        (84, -18, 1), (84, 20), (84, 52), (50, 54)])),
             L(outline([(30, 10), (50, 0), (70, 10), (60, 36), (50, 46), (40, 36)]), 'shade', 'b', False)],
}

# Fifi Frostkin (Tsumimori Umari, portera): pelo crema enorme y esponjoso en dos pisos, con una cinta azul de gafas de nieve
# (cristal verde azulado) entre los dos y un mechón que le cae por la frente; ojos grandes azules y sonrisa de dientes
GBAND, GLENS, GLENS_L = hexc('#2a6aa8'), hexc('#2a8a90'), hexc('#8ad8c0')
CHARS['fifi-frostkin'] = {
    'body': 'chica', 'pal': pal('#ece6cc', '#f8d4b8', iris='#3a5a9a', shade='#c0a898', deep='#a08c80', light='#fffbec'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'grin', 'mouth_y': 95, 'ears': False,
             'hairline': [(14, 88), (20, 66), (40, 62), (50, 66), (60, 62), (80, 66), (86, 88)]},
    'front': [*puff(50, 74, 48, 14, 12, 12, low='shade'), *puff(50, 20, 32, 16, 9, 13, low='shade', a0=0.2),
              L(outline([(8, 40), (92, 40), (92, 54), (8, 54)]), GBAND, 'b'),
              L(outline([(26, 32), (74, 32), (78, 52), (22, 52)]), BLACK, 'b'), L(outline([(29, 35), (71, 35), (74, 49), (26, 49)]), GLENS, 'b', False),
              L([(36, 36), (42, 36), (36, 48), (30, 48)], GLENS_L, 'b', False),
              fringe([(38, 50), (62, 50), (58, 62), (50, 74, 1), (44, 62)]),
              L(quad((30, 84), (36, 87), (42, 84)), OUTC, 'f', False, False, 1.2), L(quad((58, 84), (64, 87), (70, 84)), OUTC, 'f', False, False, 1.2)],
    'side': [*puff(36, 72, 40, 14, 10, 12, low='shade'), *puff(44, 26, 30, 14, 9, 11, low='shade', a0=0.2),
             L(outline([(4, 44), (84, 38), (86, 52), (6, 56)]), GBAND),
             L(outline([(74, 30), (92, 30), (94, 50), (76, 52)]), BLACK), L(outline([(77, 33), (90, 33), (91, 47), (79, 49)]), GLENS, 'b', False)],
    'back': [*puff(50, 76, 50, 14, 12, 12, low='shade'), *puff(50, 24, 30, 14, 9, 11, low='shade', a0=0.2),
             L(outline([(10, 42), (90, 42), (90, 56), (10, 56)]), GBAND)],
}

# Yetzy Klaus (Namihara Yoruna): melena azul marino casi negra, ondulada y abierta hacia abajo como una campana, con el forro
# azul celeste junto a la cara y el flequillo de lado; ojos grandes con el iris pequeño, coloretes y sonrisa
LINING = hexc('#a6d4e2')
CHARS['yetzy-klaus'] = {
    'body': 'chica', 'pal': pal('#1e2644', '#fde0cc', iris='#2a3a5e', shade='#141a32', deep='#0c1022', light='#3a4a7a'),
    'face': {'eyes': 'normal', 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(18, 82), (20, 56), (28, 48), (42, 48), (56, 54), (68, 62), (78, 70), (82, 84)]},
    'front': [L(outline([(2, 98), (6, 80), (12, 60), (16, 40), (30, 20), (50, 12), (72, 18), (86, 36), (90, 58), (98, 80), (100, 98), (88, 92), (80, 98), (76, 84),
                         (24, 84), (20, 98), (10, 92)])),
              L(outline([(8, 92), (14, 66), (20, 60), (26, 92), (18, 98)]), LINING, 'b', False),
              L(outline([(92, 92), (86, 66), (80, 60), (74, 92), (82, 98)]), LINING, 'b', False),
              L(outline([(60, 16), (80, 26), (88, 50), (82, 60), (70, 36)]), 'light', 'b', False),
              *blush(88, 18)],
    'side': [L(outline([(60, 66), (66, 56), (82, 54), (88, 40), (82, 22), (64, 8), (40, 4), (18, 12), (6, 32), (2, 60), (-4, 86), (2, 98), (14, 90), (24, 98), (36, 90),
                        (48, 96), (56, 86)])),
             L(outline([(62, 60), (74, 58), (70, 88), (64, 98), (58, 86)]), LINING, 'b', False),
             L(outline([(70, 14), (84, 28), (86, 44), (78, 50), (72, 30)]), 'light', 'b', False),
             L(ell(84, 86, 3.6, 2.2), BLUSH, 'f', False)],
    'back': [L(outline([(0, 96), (6, 76), (12, 52), (16, 32), (32, 14), (50, 10), (68, 14), (84, 32), (88, 52), (94, 76), (100, 96), (88, 92), (80, 100), (68, 92),
                        (58, 100), (50, 94), (42, 100), (32, 92), (20, 100), (12, 92)])),
             L(outline([(4, 76), (50, 66), (96, 76), (100, 96), (88, 92), (80, 100), (68, 92), (58, 100), (50, 94), (42, 100), (32, 92), (20, 100), (12, 92), (0, 96)]),
               'shade', 'b', False)],
}

# Elon Entremet (Kanbashi Suezou): pañuelo beige en la cabeza, moño verde oscuro arriba, melena verde oscura larga y abierta en
# puntas por detrás y dos mechones finos que le caen por delante hasta el pecho; un ricito en la frente; sonrisa grande
BAND, BAND_D = hexc('#c8c4ae'), hexc('#a6a28c')
CHARS['elon-entremet'] = {
    'body': 'delgado', 'pal': pal('#1c4a3a', '#f6d0b0', iris='#3a3040', shade='#14382c', deep='#0c2a20', light='#2e6a54'),
    'face': {'eyes': 'normal', 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(14, 70), (22, 54), (50, 52), (78, 54), (86, 70)]},
    'front': [L(outline([(16, 64), (-10, 96, 1), (8, 92), (-6, 112, 1), (16, 102), (22, 84), (78, 84), (84, 102), (106, 112, 1), (92, 92), (110, 96, 1), (84, 64)])),
              L(ell(50, -2, 10, 9)), L(ell(50, -12, 6, 5)),
              L(outline([(14, 60), (14, 34), (24, 16), (50, 8), (76, 16), (86, 34), (86, 60), (70, 52), (50, 50), (30, 52)]), BAND, 'b', ln=True),
              L(outline([(62, 12), (80, 22), (86, 40), (86, 58), (74, 40)]), BAND_D, 'b', False),
              fringe([(22, 56), (30, 58), (28, 108), (31, 118), (24, 118, 1), (22, 100)]), fringe([(78, 56), (70, 58), (72, 108), (69, 118), (76, 118, 1), (78, 100)]),
              L(curls(50, 56, (4, 3.4), 4), 'mid', 'f')],
    'side': [L(outline([(30, 54), (-6, 80, 1), (8, 82), (-8, 100, 1), (12, 96), (6, 112, 1), (26, 100), (34, 110, 1), (40, 88), (50, 64)])),
             L(ell(40, -2, 10, 9)), L(ell(36, -12, 6, 5)),
             L(outline([(8, 56), (6, 32), (18, 12), (44, 4), (70, 10), (86, 26), (90, 46), (70, 50), (50, 54)]), BAND, 'b', ln=True),
             fringe([(56, 54), (62, 56), (62, 106), (66, 118), (58, 116, 1), (56, 96)])],
    'back': [L(outline([(16, 50), (-10, 96, 1), (8, 92), (-6, 112, 1), (16, 104), (30, 112, 1), (40, 102), (50, 114, 1), (60, 102), (70, 112, 1), (84, 104),
                        (106, 112, 1), (92, 92), (110, 96, 1), (84, 50)])),
             L(outline([(14, 80), (86, 80), (84, 104), (50, 114), (16, 104)]), 'shade', 'b', False),
             L(outline([(12, 56), (12, 32), (24, 14), (50, 6), (76, 14), (88, 32), (88, 56), (50, 62)]), BAND, 'b', ln=True),
             L(ell(50, -2, 10, 9)), L(ell(50, -12, 6, 5))],
}

# Zain Blizzard (Tsunozaki Akaba): piel morena; pelo gris pizarra en cuernos curvos enormes hacia arriba a los dos lados, con
# el centro gris claro de puntas blancas; cejas gruesas, ojos grandes lila grisáceo y la nariz naranja redonda
GREY, SNOW = hexc('#b4b4c4'), hexc('#f2f2f8')
CHARS['zain-blizzard'] = {
    'body': 'normal', 'pal': pal('#4a4a5c', '#a87656', iris='#8a88b2', shade='#363646', deep='#24242e', light='#6a6a80'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 96,
             'hairline': [(14, 70), (22, 58), (36, 62), (50, 56), (64, 62), (78, 58), (86, 70)]},
    'front': [L(outline([(16, 66), (4, 52), (6, 30), (12, 16, 1), (16, 38), (24, 46), (22, 24), (28, -2, 1), (36, 28), (42, 22), (50, 14), (58, 22), (64, 28),
                         (72, -2, 1), (78, 24), (76, 46), (84, 38), (88, 16, 1), (94, 30), (96, 52), (84, 66), (70, 58), (30, 58)])),
              L(outline([(32, 56), (36, 30), (44, 20), (50, 10), (56, 20), (64, 30), (68, 56), (50, 60)]), GREY),
              L(outline([(42, 22), (45, 4, 1), (50, 14), (55, 2, 1), (58, 22), (50, 26)]), SNOW, 'b', False),
              L(outline([(72, 0), (78, 24), (76, 46), (70, 40)]), 'shade', 'b', False), L(outline([(28, 0), (22, 24), (24, 46), (30, 40)]), 'light', 'b', False),
              L(ell(50, 87, 3.6, 3.2), hexc('#e8702e'), 'f', ln=True)],
    'side': [L(outline([(60, 58), (72, 50), (84, 52), (92, 40), (88, 22), (96, 0, 1), (78, 14), (66, 2), (60, -14, 1), (52, 6), (36, -6, 1), (32, 14), (14, 10, 1),
                        (14, 26), (0, 30, 1), (8, 44), (-4, 54, 1), (10, 60), (14, 78), (28, 76), (40, 64), (50, 60)])),
             L(outline([(54, 10), (66, 2), (78, 14), (86, 28), (76, 40), (60, 36)]), GREY),
             L(outline([(60, 6), (60, -10, 1), (66, 4)]), SNOW, 'b', False),
             L(ell(88, 86, 3.2, 3), hexc('#e8702e'), 'f', ln=True)],
    'back': [L(outline([(18, 80), (6, 52), (4, 30), (10, 14, 1), (16, 36), (22, 40), (22, 20), (28, -2, 1), (36, 24), (50, 14), (64, 24), (72, -2, 1), (78, 20),
                        (78, 40), (84, 36), (90, 14, 1), (96, 30), (94, 52), (82, 80), (50, 86)])),
             L(outline([(36, 26), (50, 16), (64, 26), (60, 50), (50, 58), (40, 50)]), GREY),
             L(outline([(56, 18), (78, 20), (94, 50), (82, 78), (60, 84)]), 'shade', 'b', False)],
}

# Bayard Boreas (Tenke Nomo): pelo beige claro esponjoso como un gorro, con dos picos de oreja de gato arriba y flequillo en
# zigzag; por debajo el pelo castaño oscuro de la nuca; cejas de óvalo claras, ojos grandes azul grisáceo y coloretes
DARKH = hexc('#3a2a26')
CHARS['bayard-boreas'] = {
    'body': 'bajito', 'pal': pal('#ecd4bc', '#fde0cc', iris='#6a7a90', shade='#c8a890', deep='#a88a74', light='#fff2e2'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'frown', 'mouth_y': 95,
             'hairline': [(14, 70), (18, 56), (26, 58), (32, 52), (42, 56), (50, 50), (58, 56), (68, 52), (74, 58), (82, 56), (86, 70)]},
    'front': [L(outline([(16, 80), (14, 56), (86, 56), (84, 80)]), DARKH),
              L(outline([(14, 62), (4, 58, 1), (10, 48), (2, 40, 1), (12, 32), (14, 8, 1), (30, 16), (50, 10), (70, 16), (86, 8, 1), (88, 32), (98, 40, 1), (90, 48),
                         (96, 58, 1), (86, 62), (80, 52), (20, 52)])),
              L(outline([(60, 14), (86, 10), (88, 32), (96, 40), (88, 50), (76, 34)]), 'shade', 'b', False),
              L(outline([(44, 16), (50, 22, 1), (46, 26), (54, 30, 1)]), 'deep', 'b', False, False, 0.9) if False else strand([(46, 16), (50, 22), (46, 26)], 'deep', 'b', 0.9),
              L(ell(41, 63, 4.6, 3), 'light', 'f', ln=True), L(ell(59, 63, 4.6, 3), 'light', 'f', ln=True),
              *blush(88, 19)],
    'side': [L(outline([(20, 50), (44, 54), (40, 76), (24, 88), (12, 80), (8, 60)]), DARKH),
             L(outline([(60, 56), (72, 50), (86, 54), (90, 40), (86, 24), (72, 12), (64, -4, 1), (52, 8), (32, 8), (14, 18), (4, 34), (-2, 44, 1), (6, 52), (20, 56),
                        (40, 52)])),
             L(outline([(4, 34), (30, 40), (40, 52), (20, 56), (6, 52)]), 'shade', 'b', False),
             L(ell(80, 63, 3.6, 2.8), 'light', 'f', ln=True), L(ell(84, 88, 3.4, 2.2), BLUSH, 'f', False)],
    'back': [L(outline([(18, 56), (82, 56), (82, 76), (70, 88), (50, 92), (30, 88), (18, 76)]), DARKH),
             L(outline([(14, 64), (4, 60, 1), (10, 50), (2, 42, 1), (12, 34), (14, 8, 1), (30, 16), (50, 10), (70, 16), (86, 8, 1), (88, 34), (98, 42, 1), (90, 50),
                        (96, 60, 1), (86, 64), (70, 70), (50, 66), (30, 70)])),
             L(outline([(56, 14), (86, 10), (90, 50), (86, 64), (70, 68), (62, 40)]), 'shade', 'b', False)],
}
