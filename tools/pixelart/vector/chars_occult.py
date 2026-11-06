"""Occult (IE1): un equipo de monstruos. Pelo, máscaras y disfraces de cada jugador, con sus modelos 3D como referencia."""
import math

from chars import CHARS, L, OUTC, blob, bumpy, caps, dread, ell, fat, outline, pal, rope, sheen, spk, strand
from heads import FACE_FRONT, FACE_SIDE, quad

DARK = (30, 22, 24, 255)
WHITE = (255, 255, 255, 255)


def ring(cx, cy, rx, ry, n=24):
    return [(cx + rx * math.cos(i / n * 6.283), cy + ry * math.sin(i / n * 6.283)) for i in range(n + 1)]


def inside(poly, x, y):
    n, r = len(poly), False
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            r = not r
    return r


def clip(poly, p0, p1, margin=2.5):
    """El tramo de la recta p0-p1 que queda dentro de la forma (menos un margen en los extremos)."""
    pts = [(p0[0] + (p1[0] - p0[0]) * t / 200, p0[1] + (p1[1] - p0[1]) * t / 200) for t in range(201)]
    ins = [p for p in pts if inside(poly, *p)]
    if len(ins) < 2:
        return None
    a, b = ins[0], ins[-1]
    dx, dy = b[0] - a[0], b[1] - a[1]
    ln = math.hypot(dx, dy) or 1
    m = min(margin, ln / 3)
    return [(a[0] + dx / ln * m, a[1] + dy / ln * m), (b[0] - dx / ln * m, b[1] - dy / ln * m)]


def stitches(p0, p1, n=4, c=OUTC):
    """Cicatriz cosida: una línea con puntadas cruzadas."""
    out = [L([p0, p1], c, 'f', False, False, 1.0)]
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    ln = math.hypot(dx, dy) or 1
    nx, ny = -dy / ln * 2.4, dx / ln * 2.4
    for i in range(1, n + 1):
        t = i / (n + 1)
        x, y = p0[0] + dx * t, p0[1] + dy * t
        out.append(L([(x - nx, y - ny), (x + nx, y + ny)], c, 'f', False, False, 0.9))
    return out


# ------------------------------------------------------------------ Nathan Jones (portero): máscara de hockey blanca con dos
# agujeros negros y una raja, sujeta con una correa azul; pelo castaño en trenzas pegadas hacia atrás que acaban en moño
MASK = blob([(20, 50), (34, 42), (50, 40), (66, 42), (80, 50), (82, 76), (74, 94), (50, 102), (26, 94), (18, 76)])
CHARS['nathan-jones'] = {
    'body': 'normal', 'pal': pal('#7a4a2a', '#f2c8a0', mask='#e6ddd0', mask_d='#c8bcac', strap='#2a4060'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False},
    'front': [L(blob([(14, 70), (12, 40), (24, 16), (50, 8), (76, 16), (88, 40), (86, 70)]))]
             + [strand([(x, 12 + abs(x - 50) * 0.2), (x * 0.9 + 5, 50)], 'deep', 'b', 1.2) for x in (26, 38, 50, 62, 74)]
             + [L([(14, 62), (86, 62)], 'strap', 'f', False, False, 2.6),
                L(MASK, 'mask', 'f', ln=True), L(blob([(60, 46), (78, 54), (78, 80), (66, 92)], 6), 'mask_d', 'f', False),
                L([(50, 42), (50, 4)], 'strap', 'f', False, False, 3.0), L(ell(50, 44, 3, 3), 'strap', 'f', ln=True),
                L(ell(36, 70, 7, 6), DARK, 'f', False), L(ell(64, 70, 7, 6), DARK, 'f', False),
                L([(46, 56), (26, 86)], DARK, 'f', False, False, 2.0)],
    'side': [L(bumpy(12, 46, 14, 14, 8, 0.08)),
             L(blob([(46, 90), (24, 86), (14, 64), (16, 38), (32, 18), (58, 12), (80, 22), (88, 40), (74, 46)]))]
            + [strand([(70 - k * 10, 18 + k * 2), (24 - k * 2, 42 + k * 6)], 'deep', 'b', 1.2) for k in range(4)]
            + [L([(20, 60), (76, 56)], 'strap', 'f', False, False, 2.6), L(quad((80, 42), (60, 8), (30, 16)), 'strap', 'f', False, False, 3.0),
               L(blob([(74, 42), (90, 48), (92, 76), (86, 98), (74, 100), (72, 70)]), 'mask', 'f', ln=True),
               L(ell(86, 70, 3.6, 5.6), DARK, 'f', False)],
    'back': [L(blob([(14, 70), (12, 40), (24, 16), (50, 8), (76, 16), (88, 40), (86, 70), (70, 88), (30, 88)]))]
            + [strand([(x, 14), (x + (50 - x) * 0.3, 74)], 'deep', 'b', 1.2) for x in (26, 38, 50, 62, 74)]
            + [L(bumpy(50, 70, 14, 12, 8, 0.08), 'mid', 'f', ln=True), L([(12, 58), (88, 58)], 'strap', 'f', False, False, 2.6),
               L([(50, 4), (50, 58)], 'strap', 'f', False, False, 3.0)],
}

# ------------------------------------------------------------------ Russell Walk: pelo gris pegado con una diadema metálica que
# baja en pico sobre la frente, y un mechón largo que cae por un lado; mirada afilada
CHARS['russell-walk'] = {
    'body': 'normal', 'pal': pal('#76808c', '#f6dcc4', metal='#c8ccd4', metal_d='#8a909a'),
    'face': {'eyes': 'sharp', 'mouth': 'smile', 'hairline': (62, 54)},
    'front': [L(blob([(14, 66), (12, 40), (24, 18), (50, 10), (76, 18), (88, 40), (86, 66)])),
              L(blob([(60, 16), (86, 36), (86, 64), (72, 58)], 6), 'shade', 'b', False), sheen(24, 48, 20, 3),
              spk((74, 52), (88, 56), (90, 106), 4, light_left=False), spk((80, 60), (90, 62), (84, 108), 3, light_left=False),
              L(quad((14, 54), (50, 40), (86, 54)) + quad((86, 59), (50, 45), (14, 59)), 'metal_d', 'f', False),
              L([(50, 16), (64, 52), (36, 52)], 'metal', 'f', ln=True)],
    'side': [L(blob([(44, 92), (22, 88), (12, 64), (14, 36), (30, 16), (56, 10), (78, 18), (88, 36), (76, 44), (60, 48), (52, 62), (50, 80)])),
             L(blob([(16, 48), (20, 74), (38, 86), (28, 60)], 6), 'shade', 'b', False), sheen(32, 62, 14, 3),
             L(quad((14, 50), (50, 40), (90, 52)) + quad((90, 57), (50, 45), (14, 55)), 'metal_d', 'f', False),
             L([(70, 16), (90, 50), (76, 50)], 'metal', 'f', ln=True)],
    'back': [L(blob([(14, 66), (12, 40), (24, 18), (50, 10), (76, 18), (88, 40), (86, 66), (72, 86), (50, 92), (28, 86)])),
             L(blob([(58, 16), (86, 38), (84, 66), (68, 84)], 6), 'shade', 'b', False), sheen(26, 52, 20, 3),
             spk((14, 56), (26, 60), (12, 104), 4), spk((10, 62), (20, 64), (16, 108), 3),
             L(quad((14, 54), (50, 46), (86, 54)) + quad((86, 59), (50, 51), (14, 59)), 'metal_d', 'f', False)],
}

# ------------------------------------------------------------------ Jason Jones: pelo verde oscuro corto y revuelto, gafas
# redondas finas, cara de preocupación y mejillas redondas
CHARS['jason-jones'] = {
    'body': 'normal', 'pal': pal('#3e5e50', '#f8dcb8'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'hairline': (60, 52)},
    'front': [L(blob([(14, 64), (10, 40), (22, 18), (50, 10), (78, 18), (90, 40), (86, 64)])),
              L(blob([(60, 16), (88, 36), (88, 62), (72, 58)], 6), 'shade', 'b', False), sheen(22, 46, 18, 3),
              spk((20, 46), (36, 42), (26, 62), 3, z='f'), spk((34, 42), (52, 40), (42, 60), 3, z='f'),
              spk((50, 40), (66, 42), (60, 60), 3, z='f', light_left=False), spk((64, 44), (82, 48), (78, 62), 3, z='f', light_left=False)] + [L(ell(cx, 75, 6.4, 6.4), WHITE, 'f', ln=True) for cx in (36, 64)] + [L(ell(cx, 75, 2.2, 2.2), DARK, 'f', False) for cx in (36, 64)] + [
              L([(29, 75), (25, 72), (22, 76), (18, 72)], OUTC, 'f', False, False, 1.2), L([(71, 75), (75, 72), (78, 76), (82, 72)], OUTC, 'f', False, False, 1.2),
              L(quad((30, 64), (36, 61), (42, 64)), OUTC, 'f', False, False, 1.4), L(quad((58, 64), (64, 61), (70, 64)), OUTC, 'f', False, False, 1.4)],
    'side': [L(blob([(44, 92), (22, 88), (10, 64), (12, 36), (28, 14), (56, 8), (80, 16), (90, 36), (76, 44), (60, 48), (52, 62), (50, 80)])),
             L(blob([(16, 48), (18, 76), (38, 88), (28, 60)], 6), 'shade', 'b', False),
             L(ell(83, 75, 4.6, 6.4), WHITE, 'f', ln=True), L(ell(84, 75, 1.8, 2.2), DARK, 'f', False),
             spk((54, 26), (84, 38), (90, 62), 5, z='f', light_left=False)],
    'back': [L(blob([(14, 66), (10, 40), (22, 18), (50, 10), (78, 18), (90, 40), (86, 66), (72, 86), (50, 92), (28, 86)])),
             L(blob([(58, 16), (88, 38), (86, 66), (68, 86)], 6), 'shade', 'b', False), sheen(24, 50, 20, 3)],
}

# ------------------------------------------------------------------ Ken Furan: corpulento, piel morena, pelo negro corto en
# cepillo con unas antenas rizadas en la coronilla (como cables) y una sonrisa enorme
def antennas(xs, base_y):
    out = []
    for x in xs:
        pts = [(x, base_y), (x - 3, base_y - 6), (x + 3, base_y - 10), (x - 2, base_y - 15), (x + 2, base_y - 19)]
        out.append(L(pts, (30, 26, 30, 255), 'b', False, False, 1.6))
        out.append(L(ring(x + 2, base_y - 21, 2.4, 2.4, 10), (30, 26, 30, 255), 'b', False, False, 1.4))
    return out


CHARS['ken-furan'] = {
    'body': 'corpulento', 'pal': pal('#24201e', '#b06a38'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'hairline': (56, 52)},
    'front': antennas((34, 46, 58, 70), 22) + [L(blob([(18, 60), (16, 34), (26, 22), (50, 20), (74, 22), (84, 34), (82, 60)])),
                                               L(blob([(60, 22), (82, 34), (82, 58), (72, 54)], 6), 'shade', 'b', False)],
    'side': antennas((40, 54, 66), 20) + [L(blob([(44, 88), (24, 84), (16, 60), (18, 32), (30, 20), (60, 18), (80, 24), (84, 40), (70, 46), (58, 50), (52, 64), (50, 80)])),
                                          L(blob([(20, 50), (22, 74), (38, 84), (28, 60)], 6), 'shade', 'b', False)],
    'back': antennas((34, 46, 58, 70), 22) + [L(blob([(18, 66), (16, 34), (26, 22), (50, 20), (74, 22), (84, 34), (82, 66), (64, 82), (36, 82)])),
                                              L(blob([(58, 22), (82, 36), (82, 64), (64, 80)], 6), 'shade', 'b', False)],
}

# ------------------------------------------------------------------ Jerry Fulton: corpulento, pelo rubio despeinado de puntas
# cortas y sin orden que le tapa la frente hasta las cejas, cara redonda y labios morados
CHARS['jerry-fulton'] = {
    'body': 'corpulento', 'pal': pal('#e2c46c', '#f0c09a', lip='#7a4a8a', shade='#c09a50'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'hairline': False},
    'front': [L(outline([(10, 66), (6, 50), (-4, 42, 1), (8, 36), (4, 20), (18, 8), (14, -2, 1), (28, 4), (36, -6, 1), (46, 2), (56, -6, 1), (62, 4),
                         (78, 2, 1), (80, 12), (92, 22), (96, 36), (106, 44, 1), (92, 50), (90, 66)])),
              L(outline([(60, 6), (80, 14), (92, 30), (92, 52), (80, 44)]), 'shade', 'b', False),
              L(outline([(14, 62), (16, 40), (30, 26), (50, 22), (70, 26), (86, 40), (90, 62, 1), (80, 54), (74, 62, 1), (66, 52), (58, 64, 1), (52, 52),
                         (42, 62, 1), (36, 50), (26, 66, 1), (22, 54)]), 'mid', 'f'),
              L(outline([(56, 26), (76, 30), (86, 44), (82, 54), (70, 44)]), 'shade', 'f', False),
              strand([(36, 28), (40, 48)], 'shade', 'f', 1.0), strand([(62, 28), (60, 46)], 'shade', 'f', 1.0),
              L(ell(50, 92, 7, 3.4), 'lip', 'f', ln=True)],
    'side': [L(outline([(44, 92), (22, 88), (10, 70), (-4, 66, 1), (8, 58), (-6, 46, 1), (8, 40), (-2, 26, 1), (14, 22), (10, 8, 1), (28, 10), (34, -4, 1),
                        (46, 6), (56, -4, 1), (62, 8), (78, 6, 1), (80, 16), (90, 30), (94, 50, 1), (80, 44), (62, 48), (52, 62), (50, 80)])),
             L(outline([(14, 40), (24, 60), (38, 86), (20, 84), (8, 64)]), 'shade', 'b', False),
             strand([(30, 14), (20, 40)], 'shade', 'b', 1.0), strand([(56, 12), (46, 40)], 'shade', 'b', 1.0),
             L(ell(84, 92, 4, 3), 'lip', 'f', ln=True)],
    'back': [L(outline([(10, 66), (6, 50), (-4, 42, 1), (8, 36), (4, 20), (18, 8), (14, -2, 1), (28, 4), (36, -6, 1), (46, 2), (56, -6, 1), (62, 4),
                        (78, 2, 1), (80, 12), (92, 22), (96, 36), (106, 44, 1), (92, 50), (90, 66), (84, 86), (74, 94, 1), (66, 86), (56, 98, 1), (48, 88),
                        (38, 98, 1), (30, 86), (18, 92, 1), (16, 80)])),
             L(outline([(58, 10), (88, 30), (90, 66), (74, 90), (64, 60)]), 'shade', 'b', False),
             strand([(30, 10), (34, 40), (30, 70)], 'shade', 'b', 1.0), strand([(50, 4), (50, 50)], 'shade', 'b', 1.0)],
}

# ------------------------------------------------------------------ Ray Mannings: un jiangshi bajito: gorro chino azul con borde
# rojo y pompón rojo, un talismán amarillo pegado en la cara, coloretes y una trenza larga por detrás
HAT = blob([(8, 52), (16, 30), (34, 18), (50, 16), (66, 18), (84, 30), (92, 52), (50, 50)])
CHARS['ray-mannings'] = {
    'body': 'bajito', 'pal': pal('#2c2c26', '#f2d0a8', hat='#22406a', hat_d='#182c4a', rim='#c03030', pom='#e03030', tag='#f0c830', ink='#c03030', blush='#e88a6a'),
    'face': {'eyes': 'sharp', 'eye_sep': 18, 'eye_y': 72, 'brows': 'angry', 'mouth': 'none', 'hairline': False},
    'front': [L(blob([(14, 66), (12, 46), (86, 46), (86, 66)])),
              # sonrisa malvada de oreja a oreja con dientes (asoma a los lados del talismán)
              L(quad((26, 86), (50, 104), (74, 86)) + quad((74, 86), (50, 92), (26, 86))[1:], (120, 36, 36, 255), 'f', ln=True),
              L(quad((28, 87), (50, 99), (72, 87)) + quad((72, 87), (50, 93), (28, 87))[1:], WHITE, 'f', False),
              L(HAT, 'hat', 'f', ln=True), L(blob([(60, 20), (86, 32), (90, 50), (70, 50)], 6), 'hat_d', 'f', False),
              L(quad((8, 50), (50, 40), (92, 50)) + quad((92, 56), (50, 46), (8, 56)), 'rim', 'f', ln=True),
              L(ell(50, 12, 7, 7), 'pom', 'f', ln=True),
              L(ell(28, 80, 6, 4), 'blush', 'f', False), L(ell(72, 80, 6, 4), 'blush', 'f', False),
              L([(42, 54), (58, 54), (58, 100), (42, 100)], 'tag', 'f', ln=True),
              L([(45, 60), (55, 60)], 'ink', 'f', False, False, 1.2), L([(50, 58), (50, 96)], 'ink', 'f', False, False, 1.2),
              L([(45, 70), (55, 70)], 'ink', 'f', False, False, 1.2), L([(45, 80), (55, 80)], 'ink', 'f', False, False, 1.2)],
    'side': [L(blob([(30, 70), (16, 80), (6, 100), (0, 118)]), 'mid', 'b', False, False, 0)] + dread((24, 68), (6, 112), 4.4) + [
             L(blob([(44, 92), (22, 88), (14, 66), (16, 46), (80, 46), (74, 56), (54, 62), (50, 80)])),
             L(blob([(10, 54), (22, 32), (40, 20), (60, 18), (80, 24), (94, 40), (96, 52), (50, 52)]), 'hat', 'f', ln=True),
             L(quad((10, 50), (50, 44), (96, 50)) + quad((96, 56), (50, 50), (10, 56)), 'rim', 'f', ln=True),
             L(ell(56, 12, 7, 7), 'pom', 'f', ln=True),
             L([(86, 54), (94, 56), (94, 96), (86, 96)], 'tag', 'f', ln=True), L(ell(76, 82, 5, 3.4), 'blush', 'f', False)],
    'back': [L(blob([(16, 66), (12, 46), (88, 46), (84, 66), (70, 86), (30, 86)]))] + dread((50, 80), (50, 126), 5) + [
             L(HAT, 'hat', 'f', ln=True), L(blob([(56, 20), (86, 32), (90, 50), (66, 50)], 6), 'hat_d', 'f', False),
             L(quad((8, 50), (50, 44), (92, 50)) + quad((92, 56), (50, 50), (8, 56)), 'rim', 'f', ln=True), L(ell(50, 12, 7, 7), 'pom', 'f', ln=True)],
}

# ------------------------------------------------------------------ Robert Mayer: una momia: toda la cabeza vendada, con un ojo
# que asoma entre las vendas
def wraps(head, rows, tilt=7):
    """Vendas anchas: tiras inclinadas alternas (claras y en sombra) con su borde, recortadas a la cabeza."""
    out = []
    for i, y in enumerate(rows):
        t = tilt if i % 2 else -tilt
        seg = clip(head, (-20, y + t), (120, y - t), 1.5)
        if not seg:
            continue
        out.append(L(seg, 'band_l' if i % 3 == 0 else 'band', 'f', False, False, 5.2))
        lo = clip(head, (-20, y + t + 4.2), (120, y - t + 4.2), 2.5)
        if lo:
            out.append(L(lo, 'band_d', 'f', False, False, 1.0))
    return out


ROB_HEAD_F = blob([(14, 70), (12, 40), (24, 14), (50, 6), (76, 14), (88, 40), (88, 76), (78, 96), (50, 104), (22, 96), (12, 76)])
ROB_HEAD_S = blob([(44, 98), (20, 90), (10, 62), (12, 32), (30, 10), (60, 6), (82, 20), (90, 46), (90, 80), (80, 98)])
ROB_HEAD_B = blob([(14, 70), (12, 40), (24, 14), (50, 6), (76, 14), (88, 40), (88, 76), (74, 94), (50, 100), (26, 94), (12, 76)])
CHARS['robert-mayer'] = {
    'body': 'normal', 'pal': pal('#d8b89a', '#d8b89a', band='#e6d4b4', band_l='#f4e8d0', band_d='#a89070'),
    # momia: toda la cabeza envuelta en vendas anchas cruzadas; un ojo asoma por una rendija
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False, 'ears': False},
    'front': [L(ROB_HEAD_F, 'band', 'f', ln=True)] + wraps(ROB_HEAD_F, range(14, 104, 8)) + [
              L(blob([(62, 16), (86, 36), (88, 74), (76, 94), (76, 60)], 6), (168, 146, 112, 90), 'f', False),
              L(blob([(54, 70), (74, 66), (74, 76), (54, 80)], 3), DARK, 'f', False), L(ell(64, 73, 2.6, 2.6), (220, 210, 190, 255), 'f', False)],
    'side': [L(ROB_HEAD_S, 'band', 'f', ln=True)] + wraps(ROB_HEAD_S, range(12, 102, 8), 9) + [
             L(blob([(76, 70), (90, 68), (90, 76), (78, 78)], 3), DARK, 'f', False)],
    'back': [L(ROB_HEAD_B, 'band', 'f', ln=True)] + wraps(ROB_HEAD_B, range(14, 100, 8), -7),
}

# ------------------------------------------------------------------ Alexander Brave: melena negra larga y ondulada, una venda
# gris tapándole los ojos y unas orejas de zorro naranjas con huesos sobre la cabeza
def candle(x, y_top, y_bot, w=5):
    """Vela atada a la cabeza: cilindro blanco rosado con su llama naranja y roja."""
    return [L([(x - w, y_top), (x + w, y_top), (x + w, y_bot), (x - w, y_bot)], 'wax', 'b', True, True),
            L([(x + w * 0.2, y_top + 1), (x + w - 0.8, y_top + 1), (x + w - 0.8, y_bot - 1), (x + w * 0.2, y_bot - 1)], 'wax_d', 'b', False),
            L(ell(x, y_top, w, 2), 'wax_l', 'b', False),
            L(fat((x - w + 1, y_top - 1), (x + w - 1, y_top - 1), (x + 1, y_top - 18), 4), 'flame', 'b', True, True),
            L(fat((x - w * 0.4, y_top - 1), (x + w * 0.4, y_top - 1), (x + 0.6, y_top - 10), 2), 'flame_l', 'b', False)]


CHARS['alexander-brave'] = {
    'body': 'normal', 'pal': pal('#2a2430', '#f6d6b4', band='#c8d4d0', band_d='#9aa8a4', wax='#e8c8b8', wax_d='#c89c8c', wax_l='#f8e8e0',
                                 flame='#d0602a', flame_l='#f0a050'),
    # tres velas atadas a la cabeza con una venda que le tapa los ojos; melena negra larga y ondulada
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'hairline': (66, 56), 'ears': False},
    'front': [
              L(blob([(8, 112), (2, 70), (10, 30), (34, 14), (66, 14), (90, 30), (98, 70), (92, 112), (80, 108), (82, 70), (18, 70), (20, 108)])),
              L(blob([(72, 24), (94, 60), (90, 108), (82, 104)], 6), 'shade', 'b', False)]
             + candle(34, 2, 30) + candle(50, -6, 26) + candle(66, 2, 30) + [
              L(quad((10, 58), (50, 52), (90, 58)) + quad((90, 74), (50, 68), (10, 74)), 'band', 'f', ln=True),
              L(quad((10, 68), (50, 62), (90, 68)) + quad((90, 74), (50, 68), (10, 74)), 'band_d', 'f', False),
              spk((16, 44), (36, 40), (22, 60), 3, z='f'), spk((60, 40), (84, 44), (78, 60), 3, z='f', light_left=False)],
    'side': [
             L(blob([(52, 50), (40, 56), (32, 80), (26, 112), (6, 110), (4, 70), (12, 30), (34, 12), (64, 12), (84, 26), (86, 44)])),
             L(blob([(10, 50), (8, 104), (22, 106), (22, 70)], 6), 'shade', 'b', False)]
            + candle(40, 2, 26) + candle(56, -4, 22) + [
             L(quad((16, 56), (60, 52), (92, 62)) + quad((92, 74), (60, 64), (16, 70)), 'band', 'f', ln=True)],
    'back': [L(bumpy(50, 72, 46, 52, 14, 0.06)), L(bumpy(66, 84, 22, 30, 8), 'shade', 'b', False)]
            + candle(34, 2, 30) + candle(50, -6, 26) + candle(66, 2, 30) + [
             L(quad((8, 58), (50, 52), (92, 58)) + quad((92, 72), (50, 66), (8, 72)), 'band', 'f', ln=True)],
}

# ------------------------------------------------------------------ Troy Moon: hombre lobo: melena morada larga y de puntas
# que le tapa media cara, ojos amarillos, piel morena con bigotes de lobo marcados
CHARS['troy-moon'] = {
    'body': 'normal', 'pal': pal('#4c3a6c', '#c49048', iris='#e8c020', mark='#5a3a20'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'hairline': (62, 54)},
    'front': [L(blob([(8, 100), (4, 50), (14, 18), (40, 6), (60, 6), (86, 18), (96, 50), (92, 100), (80, 96), (82, 62), (18, 62), (20, 96)])),
              spk((36, 10), (54, 8), (40, -10), 5), spk((52, 8), (68, 12), (70, -8), 5, light_left=False),
              L(blob([(64, 14), (94, 46), (90, 96), (80, 92)], 6), 'shade', 'b', False), sheen(22, 46, 18, 3),
              spk((14, 46), (40, 40), (24, 90), 6, z='f'), spk((36, 40), (56, 40), (46, 70), 4, z='f'),
              spk((54, 40), (74, 42), (66, 68), 4, z='f', light_left=False), spk((70, 44), (88, 50), (84, 96), 5, z='f', light_left=False),
              L([(26, 84), (36, 86)], 'mark', 'f', False, False, 1.2), L([(64, 86), (74, 84)], 'mark', 'f', False, False, 1.2),
              L([(26, 88), (36, 88)], 'mark', 'f', False, False, 1.2), L([(64, 88), (74, 88)], 'mark', 'f', False, False, 1.2)],
    'side': [L(blob([(46, 96), (22, 94), (8, 66), (8, 34), (24, 10), (50, 2), (72, 8), (88, 26), (78, 44), (62, 48), (54, 62), (52, 84)])),
             spk((30, 8), (48, 4), (34, -12), 5), spk((14, 60), (22, 42), (-12, 50), 6), spk((12, 80), (24, 92), (-4, 100), 5),
             L(blob([(14, 50), (16, 86), (40, 94), (26, 66)], 6), 'shade', 'b', False),
             spk((54, 24), (86, 34), (92, 82), 6, z='f', light_left=False)],
    'back': [L(blob([(8, 100), (4, 50), (14, 18), (40, 6), (60, 6), (86, 18), (96, 50), (92, 100), (50, 104)])),
             spk((36, 10), (54, 8), (40, -10), 5), spk((52, 8), (68, 12), (70, -8), 5, light_left=False),
             spk((14, 88), (34, 96), (18, 112), 4), spk((34, 98), (54, 100), (42, 116), 4), spk((54, 100), (74, 96), (68, 114), 4, light_left=False),
             spk((70, 94), (88, 86), (86, 110), 4, light_left=False),
             L(blob([(58, 14), (92, 44), (90, 96), (66, 100)], 6), 'shade', 'b', False), sheen(24, 50, 18, 3)],
}

# ------------------------------------------------------------------ Burt Wolf: vampiro: pelo rubio oscuro peinado hacia atrás con
# pico en la frente, orejas puntiagudas, ojos rojos y piel pálida
CHARS['burt-wolf'] = {
    'body': 'normal', 'pal': pal('#9a8a5a', '#f8e8dc', iris='#b02020'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'big_ears': 1, 'ear_out': 4,
             'hairline': [(8, 64), (18, 64), (22, 50), (34, 46), (44, 50), (50, 58), (56, 50), (66, 46), (78, 50), (82, 64), (92, 64)]},
    'front': [L(blob([(16, 66), (14, 38), (26, 16), (50, 10), (74, 16), (86, 38), (84, 66)])),
              L(blob([(60, 16), (86, 36), (84, 64), (72, 58)], 6), 'shade', 'b', False), sheen(28, 52, 18, 3),
              strand([(36, 20), (40, 46)], 'shade', 'b', 1.0), strand([(64, 20), (60, 46)], 'shade', 'b', 1.0),
              L(fat((10, 66), (16, 80), (-4, 64), 2), 'skin', 'f', ln=True), L(fat((84, 80), (90, 66), (104, 64), 2), 'skin', 'f', ln=True)],
    'side': [L(blob([(44, 92), (22, 88), (12, 64), (14, 36), (30, 16), (56, 10), (78, 18), (84, 34), (70, 40), (58, 46), (52, 62), (50, 80)])),
             L(blob([(16, 48), (20, 74), (38, 86), (28, 60)], 6), 'shade', 'b', False), sheen(32, 60, 14, 3),
             strand([(70, 22), (40, 22), (20, 44)], 'shade', 'b', 1.0), strand([(74, 32), (44, 32), (24, 60)], 'shade', 'b', 1.0)],
    'back': [L(blob([(16, 66), (14, 38), (26, 16), (50, 10), (74, 16), (86, 38), (84, 66), (70, 86), (50, 92), (30, 86)])),
             L(blob([(58, 16), (86, 38), (84, 66), (66, 86)], 6), 'shade', 'b', False), sheen(28, 54, 18, 3),
             strand([(40, 20), (42, 86)], 'shade', 'b', 1.0), strand([(60, 20), (58, 86)], 'deep', 'b', 1.0),
             L(fat((10, 66), (16, 80), (-4, 64), 2), 'skin', 'f', ln=True), L(fat((84, 80), (90, 66), (104, 64), 2), 'skin', 'f', ln=True)],
}

# ------------------------------------------------------------------ Johan Tassman: pelo rosado de punta hacia arriba y una venda
# gris sobre los ojos con un gran ojo rojo dibujado; nudo detrás
EYE_BAND = quad((8, 40), (50, 30), (92, 40)) + quad((92, 82), (50, 74), (8, 82))
CHARS['johan-tassman'] = {
    'body': 'normal', 'pal': pal('#c8a0a8', '#f6d6b4', band='#6a6670', band_d='#4a4650', eye_y='#e8c060', eye_r='#c02020'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'hairline': False},
    'front': [L(blob([(14, 66), (12, 40), (24, 18), (50, 10), (76, 18), (88, 40), (86, 66)])),
              spk((14, 40), (30, 26), (8, 2), 6), spk((28, 24), (46, 16), (30, -10), 6), spk((44, 16), (60, 16), (52, -14), 6),
              spk((58, 18), (74, 26), (74, -8), 6, light_left=False), spk((70, 28), (86, 40), (94, 4), 6, light_left=False),
              L(blob([(60, 18), (86, 38), (86, 64), (72, 58)], 6), 'shade', 'b', False),
              spk((10, 64), (20, 66), (8, 92), 3), spk((80, 66), (90, 64), (92, 92), 3, light_left=False),
              L(EYE_BAND, 'band', 'f', ln=True),
              L([(20, 58), (34, 46), (50, 42), (66, 46), (80, 58), (66, 70), (50, 74), (34, 70)], 'eye_y', 'f', ln=True),
              L(ell(50, 58, 13, 13), (255, 240, 220, 255), 'f', ln=True), L(ell(50, 58, 10, 10), 'eye_r', 'f', False),
              L(ell(50, 58, 6, 6), (40, 10, 10, 255), 'f', False), L(ell(50, 58, 2.6, 2.6), 'eye_r', 'f', False)],
    'side': [L(blob([(44, 92), (22, 88), (12, 64), (14, 36), (30, 16), (56, 10), (78, 18), (88, 36), (76, 44), (60, 48), (52, 62), (50, 80)])),
             spk((16, 42), (30, 24), (-4, 10), 6), spk((28, 24), (48, 16), (24, -12), 6), spk((46, 16), (64, 16), (54, -14), 5),
             L(blob([(16, 48), (20, 74), (38, 86), (28, 60)], 6), 'shade', 'b', False),
             L(quad((14, 40), (50, 30), (92, 44)) + quad((92, 82), (50, 76), (14, 80)), 'band', 'f', ln=True),
             L([(80, 52), (90, 48), (92, 66), (82, 66)], 'eye_y', 'f', ln=True),
             L(blob([(14, 66), (2, 72), (0, 92), (10, 88), (16, 76)], 5), 'band_d', 'f', ln=True)],
    'back': [L(blob([(14, 66), (12, 40), (24, 18), (50, 10), (76, 18), (88, 40), (86, 66), (72, 86), (50, 92), (28, 86)])),
             spk((14, 40), (30, 26), (8, 2), 6), spk((28, 24), (46, 16), (30, -10), 6), spk((44, 16), (60, 16), (52, -14), 6),
             spk((58, 18), (74, 26), (74, -8), 6, light_left=False), spk((70, 28), (86, 40), (94, 4), 6, light_left=False),
             L(blob([(58, 18), (86, 40), (84, 66), (68, 84)], 6), 'shade', 'b', False),
             L(EYE_BAND, 'band', 'f', ln=True), L(ell(50, 62, 7, 7), 'band_d', 'f', ln=True),
             L(blob([(46, 66), (34, 88), (44, 96), (50, 72)], 4), 'band_d', 'f', ln=True), L(blob([(54, 66), (66, 88), (56, 96), (50, 72)], 4), 'band_d', 'f', ln=True)],
}

# ------------------------------------------------------------------ Rob Crombie: Frankenstein: corpulento, cabeza calva alta y
# cuadrada de piel amarillenta, cicatrices cosidas en la frente y la mejilla, boca abierta con dientes
ROB_FACE = blob([(18, 30), (30, 14), (50, 10), (70, 14), (82, 30), (84, 70), (78, 94), (62, 102), (38, 102), (22, 94), (16, 70)])
CHARS['rob-crombie'] = {
    'body': 'corpulento', 'pal': pal('#c8b080', '#d8c08a', scar='#6a5030'),
    'face': {'eyes': 'dot', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 92, 'face_front': ROB_FACE, 'hairline': False},
    'front': [L(blob([(36, 26), (64, 26), (60, 30), (40, 30)], 3), 'skin_d', 'f', False)]
             + stitches((24, 36), (76, 32), 6, (106, 80, 48, 255)) + stitches((64, 82), (78, 92), 2, (106, 80, 48, 255)),
    'side': [L(blob([(48, 102), (22, 94), (14, 66), (16, 30), (32, 12), (60, 8), (80, 18), (88, 40), (90, 80), (82, 100)]), 'skin')]
            + stitches((24, 30), (70, 22), 5, (106, 80, 48, 255)) + stitches((72, 86), (82, 94), 2, (106, 80, 48, 255)),
    'back': [L(blob([(18, 70), (16, 30), (30, 14), (50, 10), (70, 14), (84, 30), (82, 70), (68, 90), (32, 90)]), 'skin'),
             L(blob([(58, 14), (82, 32), (82, 68), (66, 88)], 6), 'skin_d', 'b', False)] + stitches((26, 36), (74, 30), 6, (106, 80, 48, 255)),
}

# ------------------------------------------------------------------ Chuck Dollman: un muñeco: pelo naranja de mechones gruesos
# como cuerdas de lana con las puntas redondas, que caen desde la coronilla hacia fuera y por delante hasta las cejas;
# cara pálida con costuras en la frente, la mejilla y la boca
CHUCK_TOP = [rope((40, 8), (20, 6), (0, 22), 15), rope((56, 6), (78, 4), (98, 22), 15), rope((48, 8), (36, -4), (22, -8), 14),
             rope((52, 8), (66, -4), (80, -6), 14), rope((30, 14), (8, 26), (-6, 46), 15), rope((70, 14), (92, 26), (106, 46), 15)]
CHARS['chuck-dollman'] = {
    'body': 'normal', 'pal': pal('#d8781e', '#ece0c8', shade='#b85a14'),
    'face': {'eyes': 'normal', 'brows': 'angry', 'mouth': 'none', 'hairline': False},
    'front': [L(blob([(10, 64), (4, 38), (16, 14), (50, 4), (84, 14), (96, 38), (90, 64)]))]
             + [L(s, 'mid', 'b', ln=True) for s in CHUCK_TOP]
             + [L(rope((22, 30), (6, 50), (2, 74), 15), 'mid', 'b', ln=True), L(rope((78, 30), (94, 50), (98, 74), 15), 'mid', 'b', ln=True)]
             + [L(rope((30, 30), (22, 48), (18, 68), 16), 'mid', 'f', ln=True), L(rope((44, 28), (40, 46), (34, 64), 16), 'mid', 'f', ln=True),
                L(rope((58, 28), (62, 46), (66, 66), 16), 'mid', 'f', ln=True), L(rope((70, 30), (78, 48), (82, 70), 16), 'mid', 'f', ln=True),
                L(rope((50, 24), (52, 40), (52, 56), 15), 'shade', 'f', ln=True)]
             + stitches((40, 92), (60, 92), 4) + stitches((22, 66), (30, 84), 2),
    'side': [L(blob([(44, 92), (20, 88), (6, 62), (6, 34), (24, 8), (56, 2), (82, 14), (92, 36), (76, 44), (60, 48), (52, 62), (50, 80)])),
             L(rope((50, 4), (30, -6), (6, 2), 15), 'mid', 'b', ln=True), L(rope((40, 10), (14, 14), (-4, 36), 15), 'mid', 'b', ln=True),
             L(rope((26, 30), (6, 50), (0, 72), 15), 'mid', 'b', ln=True), L(rope((26, 52), (14, 70), (12, 90), 15), 'mid', 'b', ln=True),
             L(rope((60, 4), (80, 0), (96, 16), 15), 'mid', 'b', ln=True), L(rope((44, 12), (36, 40), (34, 70), 16), 'shade', 'b', ln=True),
             L(rope((66, 14), (84, 30), (90, 62), 16), 'mid', 'f', ln=True), L(rope((56, 20), (64, 40), (70, 60), 15), 'mid', 'f', ln=True)]
            + stitches((80, 92), (88, 92), 2),
    'back': [L(blob([(10, 64), (4, 38), (16, 14), (50, 4), (84, 14), (96, 38), (90, 64), (76, 88), (50, 94), (24, 88)]))]
            + [L(s, 'mid', 'b', ln=True) for s in CHUCK_TOP]
            + [L(rope((22, 30), (6, 50), (2, 74), 15), 'mid', 'b', ln=True), L(rope((78, 30), (94, 50), (98, 74), 15), 'mid', 'b', ln=True),
               L(rope((30, 40), (24, 64), (22, 88), 16), 'mid', 'b', ln=True), L(rope((44, 40), (42, 66), (40, 92), 16), 'shade', 'b', ln=True),
               L(rope((58, 40), (60, 66), (60, 92), 16), 'mid', 'b', ln=True), L(rope((72, 40), (78, 64), (80, 88), 16), 'shade', 'b', ln=True)],
}

# ------------------------------------------------------------------ Uxley Allen: un alienígena: cabeza calva naranja alargada con
# rayas oscuras, orejas puntiagudas, ojos blancos rasgados y boca seria
UX_HEAD = blob([(18, 66), (16, 36), (28, 14), (50, 2), (72, 14), (84, 36), (82, 66)])
CHARS['uxley-allen'] = {
    'body': 'normal', 'pal': pal('#2a1a10', '#e09a48', iris='#f4f0e8'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'hairline': False},
    'front': [L(UX_HEAD, 'skin'), L(blob([(62, 14), (84, 36), (82, 64), (72, 58)], 6), 'skin_d', 'b', False),
              L(fat((44, 10), (56, 10), (50, 40), 1), 'mid', 'b', False), L(fat((24, 30), (34, 22), (34, 46), 2), 'mid', 'b', False),
              L(fat((66, 22), (76, 30), (66, 46), 2), 'mid', 'b', False)],
    'side': [L(blob([(48, 96), (22, 90), (14, 66), (16, 36), (32, 12), (56, 2), (78, 14), (88, 36), (88, 80), (80, 96)]), 'skin'),
             L(quad((30, 14), (52, 6), (80, 22)) + quad((80, 30), (52, 14), (30, 22)), 'mid', 'b', False),
             L(fat((20, 30), (30, 26), (34, 48), 2), 'mid', 'b', False)],
    'back': [L(blob([(18, 70), (16, 36), (28, 14), (50, 2), (72, 14), (84, 36), (82, 70), (66, 90), (34, 90)]), 'skin'),
             L(blob([(58, 12), (84, 36), (82, 68), (66, 88)], 6), 'skin_d', 'b', False),
             L(fat((44, 6), (56, 6), (50, 70), 2), 'mid', 'b', False), L(fat((24, 30), (34, 22), (32, 60), 2), 'mid', 'b', False),
             L(fat((66, 22), (76, 30), (68, 60), 2), 'mid', 'b', False)],
}

# ------------------------------------------------------------------ Phil Noir: capucha morada con el borde amarillo almenado; la
# cara queda en sombra y solo se ven unos mechones naranjas y la boca
HOOD = blob([(4, 104), (4, 60), (12, 26), (34, 6), (60, 2), (82, 16), (96, 50), (96, 104), (84, 100), (82, 70), (18, 70), (16, 100)])
CHARS['phil-noir'] = {
    'body': 'normal', 'pal': pal('#c86a2a', '#f2b884', hood='#4e3e62', hood_d='#382a48', trim='#c8b850', shadow='#3a2a2a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': False, 'ears': False},
    'front': [L(blob([(18, 56), (82, 56), (80, 84), (50, 88), (20, 84)]), 'shadow', 'f'),
              spk((26, 52), (40, 52), (32, 80), 2, z='f'), spk((44, 52), (56, 52), (50, 84), 2, z='f'), spk((60, 52), (74, 52), (68, 80), 2, z='f', light_left=False),
              L(HOOD, 'hood', 'f', ln=True), L(blob([(60, 6), (94, 46), (94, 100), (84, 98)], 6), 'hood_d', 'f', False),
              L([(12, 70), (18, 52), (24, 56), (30, 44), (38, 48), (44, 40), (56, 40), (62, 48), (70, 44), (76, 56), (82, 52), (88, 70),
                 (82, 72), (76, 64), (70, 56), (62, 58), (56, 50), (44, 50), (38, 58), (30, 56), (24, 66), (18, 72)], 'trim', 'f', ln=True)],
    'side': [L(blob([(2, 106), (0, 60), (8, 24), (30, 4), (60, 0), (84, 12), (96, 40), (94, 70), (78, 62), (60, 62), (52, 80), (54, 104)]), 'hood', 'f', ln=True),
             L(blob([(4, 60), (10, 26), (26, 12), (30, 60), (24, 100)], 6), 'hood_d', 'f', False),
             L(blob([(60, 60), (90, 58), (88, 86), (66, 84)], 5), 'shadow', 'f'),
             L(blob([(64, 84), (82, 84), (84, 100), (70, 102), (62, 94)], 5), 'skin', 'f'),
             L([(78, 62), (84, 50), (88, 54), (94, 44), (96, 60), (92, 72), (84, 70)], 'trim', 'f', ln=True)],
    'back': [L(blob([(4, 106), (4, 60), (12, 26), (34, 4), (60, 0), (84, 14), (96, 50), (96, 106), (50, 112)]), 'hood', 'f', ln=True),
             L(blob([(58, 6), (94, 46), (94, 104), (66, 110)], 6), 'hood_d', 'f', False)],
}

# ------------------------------------------------------------------ Mick Askley: un espantapájaros: la cabeza es un saco de tela
# con parches cosidos, ojos negros y boca cosida pintados, y dos cuernos naranjas
SACK = blob([(14, 104), (10, 60), (16, 24), (34, 8), (50, 4), (66, 8), (84, 24), (90, 60), (86, 104), (70, 110), (50, 104), (30, 110)])
CHARS['mick-askley'] = {
    'body': 'normal', 'pal': pal('#c86a2a', '#e6d6bc', sack='#e6d6bc', sack_d='#c8b498', patch='#c88a4a', horn='#d06a20'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False, 'ears': False},
    'front': [L(fat((14, 30), (24, 20), (-6, 4), 4), 'horn', 'b', True, True), L(fat((76, 20), (86, 30), (106, 4), 4), 'horn', 'b', True, True),
              L(SACK, 'sack', 'f', ln=True), L(blob([(62, 10), (86, 30), (88, 100), (74, 106)], 6), 'sack_d', 'f', False),
              L([(18, 26), (34, 22), (32, 36), (20, 38)], 'patch', 'f', ln=True), L([(64, 24), (80, 28), (78, 40), (64, 38)], 'patch', 'f', ln=True),
              L(ell(36, 66, 6, 5), DARK, 'f', False), L(ell(64, 66, 6, 5), DARK, 'f', False),
              L([(32, 74), (40, 74)], DARK, 'f', False, False, 1.2), L([(60, 74), (68, 74)], DARK, 'f', False, False, 1.2)]
             + stitches((34, 88), (66, 88), 6, DARK),
    'side': [L(fat((40, 16), (54, 12), (40, -10), 4), 'horn', 'b', True, True),
             L(blob([(18, 106), (8, 60), (14, 24), (34, 8), (60, 6), (82, 18), (92, 50), (92, 96), (80, 108), (50, 112)]), 'sack', 'f', ln=True),
             L(blob([(10, 60), (16, 26), (30, 16), (30, 60), (22, 102)], 6), 'sack_d', 'f', False),
             L([(36, 40), (52, 36), (54, 52), (38, 56)], 'patch', 'f', ln=True), L(ell(84, 66, 3.6, 5), DARK, 'f', False)]
            + stitches((78, 88), (90, 88), 2, DARK),
    'back': [L(fat((14, 30), (24, 20), (-6, 4), 4), 'horn', 'b', True, True), L(fat((76, 20), (86, 30), (106, 4), 4), 'horn', 'b', True, True),
             L(SACK, 'sack', 'f', ln=True), L(blob([(58, 10), (86, 30), (88, 100), (70, 108)], 6), 'sack_d', 'f', False),
             L([(42, 40), (60, 38), (60, 56), (44, 58)], 'patch', 'f', ln=True)],
}
