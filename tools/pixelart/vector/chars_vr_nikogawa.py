"""Instituto Twinford (vr-nikogawa): el Nikogawa de Victory Road (英雄たちのヴィクトリーロード), con sus modelos 3D de la
enciclopedia. Son todos personajes nuevos de VR, con una sola forma. Ojo: en la wiki Shizukawa Kazuo (asher-norwood) tiene
copiado el nombre japonés de Gou Toshio; su modelo es el de 静河和男.
Aquí van también las ayudas de pelo corto que usan los demás equipos de VR de este lote (Nishinomiya, Plathos, Rojiura)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars_bigwaves import rect_glasses
from heads import quad  # noqa: F401

WHITE = (248, 248, 248, 255)
BROWN_LINE = (130, 70, 50, 255)


def crop(view, top=2, side=66, nape=86, w=0, c='mid', shade=True, flat=0):
    """Pelo corto pegado a la cabeza (casquete): top, altura de la coronilla; side, hasta dónde bajan los lados de delante;
    nape, la nuca; w, cuánto abulta a los lados; flat, coronilla más plana (cabeza cuadrada)."""
    if view == 'front':
        out = [L(outline([(17, side), (12 - w, 42), (20 - w * 0.6, 16 + flat * 0.4), (50, top), (80 + w * 0.6, 16 + flat * 0.4), (88 + w, 42), (83, side),
                          (80, 50), (20, 50)]), c)]
        if shade:
            out.append(L(outline([(60, top + 4), (82 + w * 0.6, 18 + flat * 0.4), (88 + w, 42), (84, side - 4), (78, 40)]), 'shade', 'b', False))
        return out
    if view == 'side':
        out = [L(outline([(70, 48), (80, 42), (86, 26), (78, 8 + flat * 0.3), (54, top - 2), (28, top + 4), (8, 22), (2 - w, 46), (8, 70), (20, nape),
                          (34, nape - 2), (38, 66), (44, 58), (58, 54)]), c)]
        if shade:
            out.append(L(outline([(3 - w, 44), (30, 46), (42, 58), (36, 66), (34, nape - 2), (20, nape), (8, 70)]), 'shade', 'b', False))
        return out
    out = [L(outline([(17, 74), (12 - w, 44), (20 - w * 0.6, 18 + flat * 0.4), (50, top + 2), (80 + w * 0.6, 18 + flat * 0.4), (88 + w, 44), (83, 74),
                      (66, nape - 2), (50, nape), (34, nape - 2)]), c)]
    if shade:
        out.append(L(outline([(58, top + 6), (80 + w * 0.6, 20 + flat * 0.4), (88 + w, 46), (83, 74), (66, nape - 2), (60, 50)]), 'shade', 'b', False))
    return out


def brows(y=64, c='deep', h=4.0, sep=14, tilt=0.0, w=11):
    """Cejas gruesas (de bloque) de color propio: y, altura; h, grosor; tilt > 0 las baja hacia dentro (enfadado)."""
    out = []
    for cx, s in ((50 - sep, 1), (50 + sep, -1)):
        x0, x1 = cx - s * w * 0.55, cx + s * w * 0.5
        pts = [(x0, y + 1 - tilt * 2), (cx, y - h * 0.6), (x1, y + tilt * 2), (x1, y + h * 0.7 + tilt * 2), (cx, y + h * 0.5), (x0, y + h * 0.6 - tilt * 2)]
        out.append(L(blob(pts, 6), c, 'f', False))
    return out


def brow_side(y=64, c='deep', h=4.0, tilt=0.0):
    return [L(blob([(72, y + 1 - tilt), (78, y - h * 0.6), (86, y + tilt), (86, y + h * 0.7 + tilt), (78, y + h * 0.5), (72, y + h * 0.6)], 6), c, 'f', False)]


def ring_glasses(view, y=76, c=OUTC, w=2.6, rx=9.5, ry=7.5, sep=14):
    if view == 'front':
        out = []
        for cx in (50 - sep, 50 + sep):
            e = ell(cx, y, rx, ry)
            out.append(L(e + [e[0]], c, 'f', False, False, w))
        out.append(L([(50 - sep + rx - 1, y - 1), (50 + sep - rx + 1, y - 1)], c, 'f', False, False, w * 0.7))
        return out
    if view == 'side':
        e = ell(82, y, 5, ry)
        return [L(e + [e[0]], c, 'f', False, False, w), L([(77, y - 1), (50, y - 4)], c, 'f', False, False, w * 0.7)]
    return []


def cat_mouth(y=94, c=OUTC, w=1.4):
    return [L(quad((42, y - 1), (46, y + 3), (50, y)) + quad((50, y), (54, y + 3), (58, y - 1))[1:], c, 'f', False, False, w)]


def wide_smile(y=94, x0=34, x1=66, d=5, c=BROWN_LINE, w=1.6):
    return [L(quad((x0, y - 2), (50, y + d), (x1, y - 2)), c, 'f', False, False, w)]


def blush(y=86, c=(240, 150, 140, 255), dx=23, r=4.5):
    return [L(ell(50 - dx, y, r, r * 0.6), c, 'f', False), L(ell(50 + dx, y, r, r * 0.6), c, 'f', False)]


def leaf(x, y, a=0, s=1.0, c=(58, 120, 54, 255)):
    import math
    ca, sa = math.cos(a), math.sin(a)
    pts = [(-5, 0), (0, -3), (5, 0), (0, 2.6)]
    return L(blob([(x + (px * ca - py * sa) * s, y + (px * sa + py * ca) * s) for px, py in pts], 5), c, 'f', ln=True)


WIDE = blob([(15, 50), (50, 30), (85, 50), (90, 76), (85, 96), (66, 107), (50, 109), (34, 107), (15, 96), (10, 76)])


# Hobie Chartwood (Oyobe Masao, portero): un grandullón con cara de señor mayor: pelo muy corto gris pardo, cejas enormes de
# bloque marrón oscuro, gafitas redondas de alambre con cordón, nariz redonda, sonrisa ancha y un lápiz verde en la oreja
CHARS['hobie-chartwood'] = {
    'body': 'corpulento', 'pal': pal('#8c7c6c', '#f6b48c', iris='#7a8a7a', shade='#6e5e52', deep='#4a3028', pencil='#4a6a2a'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'none', 'eye_y': 77, 'nose': (50, 87, 4.2), 'face_front': WIDE, 'ear_out': 3,
             'hairline': [(14, 60), (17, 46), (30, 40), (50, 38), (70, 40), (83, 46), (86, 60)]},
    'front': crop('front', top=8, side=62, w=1, flat=6)
             + brows(64, 'deep', 7.0, 15, 0.0, 17)
             + ring_glasses('front', 77, (60, 50, 40, 255), 1.3, 7, 6, 14)
             + [L([(29, 79), (12, 86)], (60, 50, 40, 255), 'f', False, False, 0.9), L([(71, 79), (88, 86)], (60, 50, 40, 255), 'f', False, False, 0.9)]
             + wide_smile(95, 30, 70, 6)
             + [L([(14, 58), (9, 76)], 'pencil', 'f', False, False, 3.0), L([(14, 58), (15.5, 54)], (240, 200, 150, 255), 'f', False, False, 2.0)],
    'side': crop('side', top=6, nape=82, flat=6) + brow_side(64, 'deep', 7.0)
            + ring_glasses('side', 77, (60, 50, 40, 255), 1.3, 5, 6)
            + [L([(34, 76), (66, 52)], 'pencil', 'f', False, False, 3.0), L([(66, 52), (70, 49)], (240, 200, 150, 255), 'f', False, False, 2.0)],
    'back': crop('back', top=8, nape=82, flat=6) + [L([(87, 60), (89, 80)], 'pencil', 'f', False, False, 3.0)],
}

# Lila Glosswood (Makita Kazuko): melena de champiñón castaño oscuro, redonda y muy ancha, con flequillo recto sobre las
# cejas y la nuca rapada; ojos grandes casi negros, colorete y una sonrisa de dientes
CHARS['lila-glosswood'] = {
    'body': 'normal', 'pal': pal('#4c3834', '#fcd4b0', iris='#3a3a46', shade='#3a2a28', deep='#2a1e1c'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'grin', 'mouth_y': 93, 'hairline': False},
    'front': [L(outline([(2, 64), (-2, 38), (8, 10), (28, -8), (50, -12), (72, -8), (92, 10), (102, 38), (98, 64), (84, 66), (78, 50), (22, 50), (16, 66)])),
              L(outline([(62, -8), (90, 8), (102, 38), (98, 62), (86, 62), (84, 30)]), 'shade', 'b', False)]
             + [strand([(x, 12 if abs(x - 50) < 30 else 20), (x * 1.02 - 1, 46 if abs(x - 50) < 30 else 60)], 'deep', 'b', 1.0) for x in (8, 18, 30, 42, 58, 70, 82, 92)]
             + [L(outline([(16, 64), (16, 36), (26, 18), (50, 12), (74, 18), (84, 36), (84, 64), (78, 64), (76, 48), (24, 48), (22, 64)]), 'mid', 'f'),
                strand([(36, 22), (36, 46)], 'deep', 'f', 1.0), strand([(50, 16), (50, 46)], 'deep', 'f', 1.0), strand([(64, 22), (64, 46)], 'deep', 'f', 1.0)]
             + blush(86),
    'side': [L(outline([(92, 46), (96, 30), (86, 4), (60, -12), (30, -10), (6, 6), (-4, 34), (-2, 62), (30, 64), (58, 62), (88, 60), (90, 50)])),
             L(outline([(-2, 40), (40, 40), (60, 62), (-2, 62)]), 'shade', 'b', False),
             L(outline([(16, 64), (40, 64), (40, 82), (30, 92)]), (150, 110, 104, 255), 'b', False)]
            + [strand([(x, 12), (x - 2, 60)], 'deep', 'b', 1.0) for x in (14, 34, 56, 76)],
    'back': [L(outline([(-2, 62), (0, 30), (14, 4), (50, -10), (86, 4), (100, 30), (102, 62), (50, 64)])),
             L(outline([(58, -6), (86, 6), (100, 32), (102, 62), (60, 64)]), 'shade', 'b', False),
             L(outline([(28, 64), (72, 64), (66, 84), (50, 90), (34, 84)]), (150, 110, 104, 255), 'b', False)]
            + [strand([(x, 4 if abs(x - 50) < 30 else 18), (x, 62)], 'deep', 'b', 1.0) for x in (10, 24, 38, 50, 62, 76, 90)],
}

# Rowland Brightwood (Mondo Kanta): pelo corto castaño oscuro y redondo; cejas gruesas como orugas y unas gafas redondas
# negras de pasta gruesa; ojos negros y sonrisa suave
CHARS['rowland-brightwood'] = {
    'body': 'normal', 'pal': pal('#4a443a', '#fcccA4', iris='#2a2626', shade='#3a342c', deep='#2a2622'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 93,
             'hairline': [(15, 66), (18, 50), (34, 46), (50, 50), (66, 46), (82, 50), (85, 66)]},
    'front': crop('front', top=2, side=68, w=2) + brows(63, 'deep', 5.0, 14, 0.0, 12) + ring_glasses('front', 77, (24, 22, 22, 255), 2.8, 10, 8, 15),
    'side': crop('side', top=0, nape=88, w=2) + brow_side(63, 'deep', 5.0) + ring_glasses('side', 77, (24, 22, 22, 255), 2.8, 5, 8),
    'back': crop('back', top=2, nape=88, w=2) + [L([(14, 74), (19, 76)], (24, 22, 22, 255), 'f', False, False, 2.4), L([(86, 74), (81, 76)], (24, 22, 22, 255), 'f', False, False, 2.4)],
}

# Tristan Brookwood (Yamame Yukio): piel morena; pelo corto azul marino muy oscuro, redondo y abultado, con el borde de la
# frente en picos cortos y patillas; ojazos azules, cejas enfadadas y sonrisa de dientes
CHARS['tristan-brookwood'] = {
    'body': 'normal', 'pal': pal('#2a2e44', '#a8704a', iris='#3a78c8', shade='#20233a', deep='#161828'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 94,
             'hairline': [(15, 66), (18, 54), (22, 50), (28, 46), (34, 48), (40, 44), (46, 47), (52, 44), (58, 47), (64, 44), (70, 48), (76, 46), (82, 52), (85, 66)]},
    'front': crop('front', top=0, side=68, w=3),
    'side': [L(outline([(66, 54), (74, 46), (84, 42), (88, 24), (78, 6), (54, -2), (28, 2), (8, 20), (0, 46), (6, 70), (20, 88), (34, 86), (38, 66), (46, 60),
                        (54, 72, 1), (58, 58)])),
             L(outline([(2, 44), (30, 46), (42, 60), (36, 66), (34, 86), (20, 88), (6, 70)]), 'shade', 'b', False)],
    'back': crop('back', top=0, nape=86, w=3),
}

# Lachlan Hartwood (Kabamoto Yasunobu): rechoncho de cara muy ancha y mofletes; pelo negro corto en casquete de coronilla
# plana; cejas negras gruesas en arco, ojillos pequeños, nariz grande redonda y sonrisa ancha
CHARS['lachlan-hartwood'] = {
    'body': 'corpulento', 'pal': pal('#2e2e2e', '#fcd8b8', iris='#2a2a2a', shade='#222222', deep='#161616'),
    'face': {'eyes': 'dot', 'brows': False, 'mouth': 'none', 'eye_y': 78, 'nose': (50, 86, 4.6), 'face_front': WIDE, 'ear_out': 3,
             'hairline': [(14, 64), (16, 52), (30, 50), (50, 52), (70, 50), (84, 52), (86, 64)]},
    'front': crop('front', top=6, side=64, w=2, flat=8)
             + [L(quad((24, 72), (32, 62), (44, 68)), OUTC, 'f', False, False, 3.4), L(quad((76, 72), (68, 62), (56, 68)), OUTC, 'f', False, False, 3.4)]
             + wide_smile(95, 32, 68, 6),
    'side': crop('side', top=4, nape=84, w=2, flat=8) + [L(quad((72, 70), (78, 62), (86, 66)), OUTC, 'f', False, False, 3.4)],
    'back': crop('back', top=6, nape=84, w=2, flat=8),
}

# Nathaniel Whitewood (Koba Emiko): pelo corto castaño grisáceo en casquete con entradas en las sienes; ojos verdes,
# cejas castañas gruesas, colorete y sonrisa
CHARS['nathaniel-whitewood'] = {
    'body': 'normal', 'pal': pal('#6e6252', '#fcd4b0', iris='#4a8a7a', shade='#564a3e', deep='#3e342c'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 93,
             'hairline': [(15, 64), (18, 46), (24, 42), (28, 34), (50, 32), (72, 34), (76, 42), (82, 46), (85, 64)]},
    'front': crop('front', top=0, side=66, w=2) + brows(63, 'shade', 3.4, 14, 0.0, 13) + blush(86),
    'side': crop('side', top=-2, nape=86, w=2) + brow_side(63, 'shade', 3.4),
    'back': crop('back', top=0, nape=86, w=2),
}

# Orin Wildwood (Ino Yatarou): piel morena; pelo corto verde azulado oscuro con el nacimiento en picos (la frente en forma de
# estrella); ojos azules grandes, cejas verdes gruesas y sonrisa
CHARS['orin-wildwood'] = {
    'body': 'normal', 'pal': pal('#1e5a5a', '#b07a54', iris='#3a8ac8', shade='#184848', deep='#103434'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 93,
             'hairline': [(15, 64), (18, 50), (26, 48), (28, 38), (38, 48), (50, 44), (62, 48), (72, 38), (74, 48), (82, 50), (85, 64)]},
    'front': crop('front', top=0, side=66, w=2) + brows(63, 'mid', 4.0, 14, 0.4, 12)
             + [strand([(30, 16), (32, 20)], 'deep', 'b', 1.4), strand([(60, 10), (63, 13)], 'deep', 'b', 1.4), strand([(76, 24), (78, 28)], 'deep', 'b', 1.4)],
    'side': crop('side', top=-2, nape=86, w=2) + brow_side(63, 'mid', 4.0) + [strand([(50, 14), (54, 18)], 'deep', 'b', 1.4)],
    'back': crop('back', top=0, nape=86, w=2) + [strand([(46, 8), (50, 6), (54, 8)], 'deep', 'b', 1.2)],
}

# Calvin Sixwood (Mutsumi Hideo): pelo gris muy oscuro corto, con pico en la frente y entradas; los lados y la nuca rapados
# más claros; ojos negros entornados, arrugas de ceño y sonrisa de lado
CHARS['calvin-sixwood'] = {
    'body': 'delgado', 'pal': pal('#3a3844', '#fcd4b4', iris='#2a2a2a', shade='#2c2a34', deep='#201e26', buzz='#6e5a54'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 95,
             'hairline': [(15, 64), (18, 46), (28, 40), (40, 36), (50, 44), (60, 36), (72, 40), (82, 46), (85, 64)]},
    'front': [L(outline([(17, 66), (12, 42), (20, 16), (50, 0), (80, 16), (88, 42), (83, 66), (80, 50), (20, 50)]), 'buzz'),
              L(outline([(16, 34), (20, 14), (50, 0), (80, 14), (84, 34), (70, 38), (50, 40), (30, 38)])),
              L(outline([(60, 4), (82, 16), (84, 34), (74, 34)]), 'shade', 'b', False),
              L([(26, 62), (40, 66)], OUTC, 'f', False, False, 1.8), L([(74, 62), (60, 66)], OUTC, 'f', False, False, 1.8),
              L([(28, 58), (40, 62)], (200, 140, 120, 255), 'f', False, False, 0.9), L([(72, 58), (60, 62)], (200, 140, 120, 255), 'f', False, False, 0.9),
              L([(48, 84), (50, 87), (53, 85)], (200, 140, 120, 255), 'f', False, False, 1.0)],
    'side': [L(outline([(70, 48), (80, 42), (86, 26), (78, 8), (54, -2), (28, 4), (8, 22), (2, 46), (8, 70), (20, 86), (34, 84), (38, 66), (44, 58), (58, 54)]), 'buzz'),
             L(outline([(76, 32), (86, 24), (78, 8), (54, -2), (28, 4), (8, 22), (2, 40), (30, 36), (56, 36)])),
             L([(74, 62), (86, 64)], OUTC, 'f', False, False, 1.8)],
    'back': [L(outline([(17, 74), (12, 44), (20, 18), (50, 2), (80, 18), (88, 44), (83, 74), (66, 84), (50, 86), (34, 84)]), 'buzz'),
             L(outline([(14, 42), (20, 16), (50, 2), (80, 16), (86, 42), (66, 48), (34, 48)])),
             L(outline([(58, 6), (80, 18), (86, 40), (66, 46)]), 'shade', 'b', False)],
}

# Iris Nightwood (Uwa Taeko): melena lisa morada muy larga (hasta la cintura), con flequillo recto que le tapa las cejas y los
# lados cayendo junto a la cara; cara pálida, ojos negros redondos y boquita de gato
CHARS['iris-nightwood'] = {
    'body': 'chica', 'pal': pal('#6a5a8a', '#fcecd8', iris='#1e1a22', shade='#544870', deep='#3e3454'),
    'face': {'eyes': 'round', 'brows': False, 'mouth': 'none', 'hairline': False, 'eye_y': 74},
    'front': [L(outline([(8, 118, 1), (10, 40), (18, 10), (50, 0), (82, 10), (90, 40), (92, 118, 1), (80, 116), (80, 58), (20, 58), (20, 116)])),
              L(outline([(60, 4), (84, 14), (90, 44), (92, 116), (82, 114), (82, 50)]), 'shade', 'b', False),
              L(outline([(18, 64), (16, 30), (28, 12), (50, 8), (72, 12), (84, 30), (82, 64), (80, 56), (66, 56), (50, 56), (34, 56), (20, 56)]), 'mid', 'f'),
              L(outline([(16, 60), (20, 28), (24, 28), (22, 110)]), 'shade', 'f', False), L(outline([(84, 60), (80, 28), (76, 28), (78, 110)]), 'shade', 'f', False),
              L(quad((32, 22), (50, 16), (68, 22)), 'light', 'f', False, False, 1.4)]
             + cat_mouth(90, BROWN_LINE, 1.3),
    'side': [L(outline([(86, 64), (90, 40), (82, 10), (56, -2), (28, 2), (10, 20), (2, 50), (-4, 122, 1), (24, 120), (44, 118), (50, 92), (62, 60), (74, 60), (78, 64)])),
             L(outline([(2, 50), (30, 40), (52, 64), (46, 116), (-4, 120)]), 'shade', 'b', False),
             L(outline([(72, 62), (90, 64), (90, 40), (80, 30)]), 'mid', 'f')],
    'back': [L(outline([(6, 120, 1), (8, 40), (18, 10), (50, 0), (82, 10), (92, 40), (94, 120, 1), (50, 122)])),
             L(outline([(58, 4), (84, 14), (92, 44), (94, 120), (60, 122), (54, 60)]), 'shade', 'b', False),
             L(quad((26, 16), (50, 8), (74, 16)), 'light', 'b', False, False, 1.4)],
}

# Ronan Strongwood (Gou Toshio): un señor mayor curtido: pelo muy corto gris beige que baja en patillas largas y cuadradas
# junto a la cara hasta la mandíbula; frente con arrugas, ceño fruncido, ojos amarillentos y boca recta y ancha
RONAN = {
    'body': 'normal', 'pal': pal('#b2ae98', '#fcd2ae', iris='#8a8a2a', shade='#8c8070', deep='#6e6458'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'none', 'big_ears': 1,
             'hairline': [(19, 100), (19, 50), (30, 46), (46, 42), (50, 48), (54, 42), (70, 46), (81, 50), (81, 100)]},
    'front': [L(outline([(13, 100), (11, 44), (20, 14), (50, 2), (80, 14), (89, 44), (87, 100), (82, 100), (82, 52), (18, 52), (18, 100)])),
              L(outline([(60, 6), (82, 18), (89, 44), (87, 98), (82, 96), (80, 40)]), 'shade', 'b', False),
              L(quad((30, 52), (40, 50), (46, 54)), (200, 140, 116, 255), 'f', False, False, 0.9),
              L(quad((54, 54), (60, 50), (70, 52)), (200, 140, 116, 255), 'f', False, False, 0.9),
              L([(34, 64), (44, 69)], OUTC, 'f', False, False, 2.2), L([(66, 64), (56, 69)], OUTC, 'f', False, False, 2.2),
              L([(46, 64), (48, 70)], (200, 140, 116, 255), 'f', False, False, 0.9), L([(54, 64), (52, 70)], (200, 140, 116, 255), 'f', False, False, 0.9),
              L(quad((40, 84), (46, 80), (50, 86)), (200, 140, 116, 255), 'f', False, False, 1.0),
              L(quad((60, 84), (54, 80), (50, 86)), (200, 140, 116, 255), 'f', False, False, 1.0),
              L(quad((36, 94), (50, 96), (64, 94)), BROWN_LINE, 'f', False, False, 1.6)],
    'side': [L(outline([(84, 30), (80, 10), (56, 0), (28, 4), (10, 22), (4, 48), (10, 74), (26, 84), (36, 80), (40, 64), (48, 58), (56, 58), (56, 82), (64, 92),
                        (70, 88), (66, 58), (72, 46), (80, 40)])),
             L(outline([(4, 44), (32, 44), (42, 62), (36, 80), (26, 84), (10, 74)]), 'shade', 'b', False),
             L([(70, 64), (84, 67)], OUTC, 'f', False, False, 2.2)],
    'back': [L(outline([(19, 70), (14, 40), (22, 14), (50, 2), (78, 14), (86, 40), (81, 70), (70, 76), (64, 90), (36, 90), (30, 76)])),
             L(outline([(58, 6), (78, 16), (86, 40), (81, 70), (70, 76), (64, 90), (56, 90), (60, 50)]), 'shade', 'b', False),
             L(outline([(36, 80), (64, 80), (62, 90), (38, 90)]), 'deep', 'b', False)],
}
CHARS['ronan-strongwood'] = RONAN

# Vearn Dashwood (Yomogi Kenta): pelo corto verde hoja con una calva-cúpula verde oscura en lo alto de la frente y hojitas
# verdes pegadas por el pelo; ojos grandes verde agua con ojeras verdes, cejas gruesas y sonrisa
CHARS['vearn-dashwood'] = {
    'body': 'bajito', 'pal': pal('#8ab05a', '#fcd0a8', iris='#4aa8a0', shade='#6a8a44', deep='#3e5a2a'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 93,
             'hairline': [(15, 66), (18, 50), (22, 42), (36, 42), (38, 40), (62, 40), (64, 42), (78, 42), (82, 50), (85, 66)]},
    'front': crop('front', top=0, side=68, w=2)
             + [L(outline([(36, 42), (36, 26), (42, 16), (50, 14), (58, 16), (64, 26), (64, 42)]), 'deep', 'b', False),
                leaf(14, 26, -0.4, 1.4), leaf(88, 38, 0.6, 1.2), leaf(76, 8, 0.3, 1.0)]
             + brows(64, 'deep', 4.4, 14, 0.0, 12),
    'side': crop('side', top=-2, nape=86, w=2) + brow_side(64, 'deep', 4.4) + [leaf(22, 30, 1.2, 1.4), leaf(58, 12, -0.4, 1.2), leaf(80, 40, 0.8, 1.0)],
    'back': crop('back', top=0, nape=86, w=2) + [leaf(36, 4, -0.3, 1.2), leaf(84, 24, 1.0, 1.1), leaf(20, 30, -1.0, 1.0)],
}

# Asher Norwood (Shizukawa Kazuo): piel morena; pelo azul marino casi negro arriba, con los lados y la nuca rapados gris
# azulado, y un mechón suelto que le cae en curva por el centro de la frente; ojazos azules, cejas gruesas y sonrisa
CHARS['asher-norwood'] = {
    'body': 'normal', 'pal': pal('#1a2238', '#a8704a', iris='#3a5aa8', shade='#121828', deep='#0c101c', buzz='#5a6a84'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'grin', 'mouth_y': 94,
             'hairline': [(15, 62), (18, 44), (30, 38), (50, 36), (70, 38), (82, 44), (85, 62)]},
    'front': [L(outline([(17, 64), (12, 42), (20, 16), (50, 0), (80, 16), (88, 42), (83, 64), (80, 50), (20, 50)]), 'buzz'),
              L(outline([(14, 34), (20, 12), (50, -2), (80, 12), (86, 34), (70, 32), (50, 34), (30, 32)])),
              L(outline([(60, 2), (82, 14), (86, 32), (72, 30)]), 'shade', 'b', False),
              L(rope((52, 30), (40, 38), (44, 54), 5), 'mid', 'f')]
             + brows(63, 'mid', 4.6, 14, 0.5, 12),
    'side': [L(outline([(70, 48), (80, 42), (86, 26), (78, 8), (54, -2), (28, 4), (8, 22), (2, 46), (8, 70), (20, 86), (34, 84), (38, 66), (44, 58), (58, 54)]), 'buzz'),
             L(outline([(84, 30), (86, 24), (78, 6), (54, -4), (28, 2), (8, 20), (2, 34), (30, 30), (60, 32)])),
             L(rope((84, 28), (94, 34), (92, 52), 5), 'mid', 'f')] + brow_side(63, 'mid', 4.6, 0.6),
    'back': [L(outline([(17, 74), (12, 44), (20, 18), (50, 2), (80, 18), (88, 44), (83, 74), (66, 84), (50, 86), (34, 84)]), 'buzz'),
             L(outline([(14, 36), (20, 14), (50, 0), (80, 14), (86, 36), (66, 40), (34, 40)])),
             L(outline([(58, 4), (80, 16), (86, 34), (66, 38)]), 'shade', 'b', False)],
}

# Emory Plainwood (Naoie Masaya): pelo corto verde petróleo con patillas cuadradas; gafas naranjas rectangulares de pasta,
# ojos granate, cejas gruesas en arco y sonrisa de dientes
ORANGE = (214, 112, 52, 255)
CHARS['emory-plainwood'] = {
    'body': 'normal', 'pal': pal('#3e6a5e', '#fcd4b0', iris='#a04a3a', shade='#30544a', deep='#223c34'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'grin', 'mouth_y': 94,
             'hairline': [(15, 66), (21, 64), (23, 46), (77, 46), (79, 64), (85, 66)]},
    'front': crop('front', top=0, side=68, w=2) + brows(63, 'deep', 4.0, 14, 0.6, 12)
             + [L(outline([(22, 70), (46, 70), (46, 82), (24, 82)]) + [(22, 70)], ORANGE, 'f', False, False, 2.4),
                L(outline([(78, 70), (54, 70), (54, 82), (76, 82)]) + [(78, 70)], ORANGE, 'f', False, False, 2.4),
                L([(46, 73), (54, 73)], ORANGE, 'f', False, False, 1.8), L([(22, 72), (16, 72)], ORANGE, 'f', False, False, 1.8),
                L([(78, 72), (84, 72)], ORANGE, 'f', False, False, 1.8)],
    'side': crop('side', top=-2, nape=86, w=2) + brow_side(63, 'deep', 4.0, 0.6)
            + [L([(78, 70), (90, 70), (90, 82), (79, 82), (78, 70)], ORANGE, 'f', False, False, 2.4), L([(50, 70), (78, 72)], ORANGE, 'f', False, False, 1.8)],
    'back': crop('back', top=0, nape=86, w=2) + [L([(14, 72), (19, 72)], ORANGE, 'f', False, False, 2.2), L([(86, 72), (81, 72)], ORANGE, 'f', False, False, 2.2)],
}

# Maris Hollowwood (Omotedani Sonoko): pelo corto malva oscuro en casquete con la frente alta y redonda; cara muy pálida,
# ojos granate con raya azul marcada, cejas cortas gruesas y sonrisa de dientes
CHARS['maris-hollowwood'] = {
    'body': 'normal', 'pal': pal('#7a5058', '#fce8dc', iris='#7a3a4a', shade='#623e46', deep='#4a2c34'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 94,
             'hairline': [(15, 64), (18, 44), (26, 36), (50, 32), (74, 36), (82, 44), (85, 64)]},
    'front': crop('front', top=0, side=66, w=2) + brows(60, 'mid', 4.6, 14, -0.3, 10)
             + [L([(28, 77), (31, 80)], (50, 60, 140, 255), 'f', False, False, 1.6), L([(72, 77), (69, 80)], (50, 60, 140, 255), 'f', False, False, 1.6)],
    'side': crop('side', top=-2, nape=86, w=2) + brow_side(60, 'mid', 4.6),
    'back': crop('back', top=0, nape=86, w=2),
}

# Lydia Trailwood (Yoyobi Yae): melena corta desfilada verde oliva con las puntas tostadas, dos mechones que se levantan a los
# lados como orejas de perro, flequillo en picos y una diadema negra; ojos verdes grandes y sonrisa de dientes
TAN = (164, 120, 74, 255)
CHARS['lydia-trailwood'] = {
    'body': 'chica', 'pal': pal('#6a6448', '#fcd8bc', iris='#3a9a7a', shade='#54503a', deep='#3e3a2a'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'grin', 'mouth_y': 93, 'hairline': False},
    'front': [L(outline([(14, 34), (-6, 54, 1), (-2, 60), (12, 50)]), TAN), L(outline([(86, 34), (106, 54, 1), (102, 60), (88, 50)]), TAN),
              L(outline([(6, 102, 1), (4, 72), (2, 50), (12, 20), (30, 6), (50, 2), (70, 6), (88, 20), (98, 50), (96, 72), (94, 102, 1), (86, 92), (84, 102, 1),
                         (80, 82), (20, 82), (16, 102, 1), (14, 92)])),
              L(outline([(60, 6), (86, 20), (98, 50), (94, 100), (86, 90), (84, 60)]), 'shade', 'b', False),
              L(outline([(6, 100), (10, 88), (16, 100)]), TAN, 'b', False), L(outline([(94, 100), (90, 88), (84, 100)]), TAN, 'b', False),
              L(quad((14, 40), (50, 26), (86, 40)), OUTC, 'f', False, False, 2.2),
              L(outline([(14, 74, 1), (18, 46), (30, 34), (50, 30), (70, 34), (82, 46), (86, 74, 1), (78, 62), (68, 70, 1), (60, 58), (52, 78, 1), (46, 58), (36, 70, 1),
                         (28, 58), (22, 64)]), 'mid', 'f'),
              strand([(50, 34), (50, 66)], 'deep', 'f', 1.0)] + blush(87),
    'side': [L(outline([(84, 44), (88, 62), (84, 80), (78, 94, 1), (70, 82), (60, 92), (52, 100, 1), (44, 88), (30, 98, 1), (22, 88), (6, 102, 1), (6, 82), (-6, 62),
                        (-4, 30), (12, 8), (40, -4), (70, 2), (86, 20)])),
             L(outline([(-4, 50), (30, 50), (44, 86), (30, 96), (6, 100)]), 'shade', 'b', False),
             L(outline([(26, 22), (44, 44, 1), (38, 46), (20, 32)]), TAN, 'b'),
             L(outline([(70, 30), (90, 40), (92, 62), (86, 74, 1), (82, 60), (76, 48)]), 'mid', 'f')],
    'back': [L(outline([(14, 34), (-6, 54, 1), (-2, 60), (12, 50)]), TAN), L(outline([(86, 34), (106, 54, 1), (102, 60), (88, 50)]), TAN),
             L(outline([(6, 104, 1), (2, 72), (2, 48), (12, 20), (30, 6), (50, 2), (70, 6), (88, 20), (98, 48), (98, 72), (94, 104, 1), (82, 96), (72, 106, 1), (62, 96),
                        (50, 108, 1), (38, 96), (28, 106, 1), (18, 96)])),
             L(outline([(56, 6), (86, 20), (98, 48), (98, 72), (94, 104), (72, 104), (60, 60)]), 'shade', 'b', False)],
}

# Alden Songwood (Kubashira Kensuke, portero): cabeza ancha; pelo corto gris azulado de coronilla plana con la frente recta y
# patillas; cejas gruesas oscuras enfadadas, ojos marrones, boca de gato y corazoncitos rosas en las mejillas
CHARS['alden-songwood'] = {
    'body': 'normal', 'pal': pal('#7a8c94', '#fcd4ac', iris='#6a3a2a', shade='#5e6e76', deep='#3a464c'),
    'face': {'eyes': 'normal', 'brows': False, 'mouth': 'none', 'face_front': WIDE, 'ear_out': 3,
             'hairline': [(14, 68), (19, 66), (22, 50), (30, 46), (70, 46), (78, 50), (81, 66), (86, 68)]},
    'front': crop('front', top=8, side=70, w=4, flat=10) + brows(64, (40, 54, 60, 255), 5.0, 14, 0.8, 13) + cat_mouth(95)
             + blush(87, (244, 170, 160, 255), 22, 3.6),
    'side': crop('side', top=6, nape=86, w=4, flat=10) + brow_side(64, (40, 54, 60, 255), 5.0, 0.8),
    'back': crop('back', top=8, nape=86, w=4, flat=10),
}

# la camiseta lleva el hombro izquierdo y el pecho en marrón, cruzado en diagonal (la del portero, en azul claro)
for _pid in ('lila-glosswood', 'rowland-brightwood', 'tristan-brookwood', 'lachlan-hartwood', 'nathaniel-whitewood', 'orin-wildwood', 'calvin-sixwood',
             'iris-nightwood', 'ronan-strongwood', 'vearn-dashwood', 'asher-norwood', 'emory-plainwood', 'maris-hollowwood', 'lydia-trailwood'):
    CHARS[_pid]['sash'] = '#6a4632'
for _pid in ('hobie-chartwood', 'alden-songwood'):
    CHARS[_pid]['sash'] = '#a8c8e0'
