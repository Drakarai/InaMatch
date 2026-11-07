"""Ojeadores de IE1 (scouts-ie1), tanda 11: dibujados a partir de su retrato de Victory Road; claves 'scouts-ie1:<id>'.
Casi ninguno tiene modelo 3D: del retrato salen el peinado, los colores y la cara; el perfil y la espalda, deducidos."""
from chars import CHARS, L, OUTC, blob, ell, longhair, messy, outline, pal, rope, strand  # noqa: F401
from chars_vr_nikogawa import blush, brow_side, brows, crop, ring_glasses
from heads import fat, mirror, quad  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (40, 34, 36, 255)
LIP = (150, 80, 66, 255)
# pieles (los retratos de VR salen muy saturados: tonos algo más suaves, como los de los equipos)
SK_P, SK_L, SK_T, SK_O, SK_D = '#fcdcbc', '#f8c89a', '#d8a06a', '#c8925e', '#a87448'


def K(pid):
    return f'scouts-ie1:{pid}'


def add(pid, body, p, face, front, side, back, **extra):
    CHARS[K(pid)] = dict(body=body, pal=p, face=face, front=front, side=side, back=back, **extra)


def views(fn, **kw):
    """Las tres vistas de un peinado hecho con una función fn(view, ...)."""
    return {v: fn(v, **kw) for v in ('front', 'side', 'back')}


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


def fang(x=56, y=93):
    return L([(x - 1.6, y - 0.5), (x + 1.6, y - 0.5), (x, y + 3.4)], WHITE, 'f', ln=True)


def nose(x=50, y=86, w=4, c=None):
    """Nariz grande de trazo (los adultos y los narizotas de IE1)."""
    return L(quad((x - w * 0.4, y - 8), (x - w, y + 1), (x - w * 0.2, y + 2)) + quad((x - w * 0.2, y + 2), (x + w * 0.6, y + 3), (x + w, y)), c or LIP, 'f',
             False, False, 1.2)


def cheek_lines(y=84, c=LIP):
    return [L([(24, y), (28, y - 2)], c, 'f', False, False, 1.0), L([(25, y + 3), (29, y + 1)], c, 'f', False, False, 1.0),
            L([(76, y), (72, y - 2)], c, 'f', False, False, 1.0), L([(75, y + 3), (71, y + 1)], c, 'f', False, False, 1.0)]


def earring(view, c=(230, 190, 60, 255), y=82):
    if view == 'front':
        return [L(ell(15, y, 1.6, 1.8), c, 'f'), L(ell(85, y, 1.6, 1.8), c, 'f')]
    if view == 'side':
        return [L(ell(46, y, 1.6, 1.8), c, 'f')]
    return [L(ell(15, y - 2, 1.6, 1.8), c, 'f'), L(ell(85, y - 2, 1.6, 1.8), c, 'f')]


def scalp(view):
    """Cráneo de piel (calvos y rapados): de frente la cara sola acaba en la frente."""
    if view == 'front':
        return L(outline([(17, 66), (14, 40), (24, 18), (50, 8), (76, 18), (86, 40), (83, 66), (50, 60)]), 'skin')
    if view == 'side':
        return L(outline([(54, 60), (60, 40), (80, 30), (84, 18), (62, 6), (34, 6), (12, 20), (4, 46), (10, 72), (30, 80), (48, 70)]), 'skin')
    return L(outline([(17, 70), (14, 40), (24, 18), (50, 8), (76, 18), (86, 40), (83, 70), (50, 80)]), 'skin')


# ------------------------------------------------------------------ hoja 0

# Sean Trawler: piel tostada, pelo crema corto en cepillo plano con el flequillo levantado en puntitas; ceño y media sonrisa
v = views(crop, top=2, side=54, nape=80, flat=8)
add('sean-trawler', 'normal', pal('#e2d6bc', SK_T, iris='#2a2224'),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'hairline': [(14, 54), (20, 44), (34, 40), (50, 42), (66, 40), (80, 44), (86, 54)]},
    v['front'] + [fringe([(24, 30), (28, 10), (34, 18), (40, 4, 1), (46, 16), (54, 2, 1), (60, 14), (68, 4, 1), (72, 18), (78, 30), (64, 26), (40, 26)])],
    v['side'] + [L(outline([(60, 10), (70, 0, 1), (74, 10), (84, 6, 1), (86, 20), (70, 22)]))],
    v['back'])

# Seymour Senary: pelo turquesa pálido peinado hacia arriba en mechones altos; corona marrón con dos cuernos curvos sobre la
# frente; cejas turquesa, colmillo
TEAL = '#a8cccc'
CROWN = (122, 66, 22, 255)
add('seymour-senary', 'normal', pal(TEAL, SK_T, iris='#2a2224', crown=CROWN, crown_d=(90, 46, 14, 255)),
    {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'hairline': False},
    [L(outline([(22, 50), (18, 22), (24, -4), (28, -26, 1), (36, -6), (42, -32, 1), (50, -10), (58, -32, 1), (64, -8), (72, -26, 1), (78, -4), (82, 22), (78, 50)])),
     L(outline([(58, -30), (64, -8), (72, -26), (78, -4), (82, 22), (78, 46), (68, 20)]), 'shade', 'b', False),
     strand([(36, 30), (34, 0)], 'shade', 'b', 1.0), strand([(50, 30), (50, -6)], 'shade', 'b', 1.0), strand([(64, 30), (66, 0)], 'shade', 'b', 1.0),
     L(outline([(12, 58), (14, 42), (30, 36), (50, 34), (70, 36), (86, 42), (88, 58), (70, 52), (50, 50), (30, 52)]), 'crown', 'f'),
     L(fat((14, 50), (24, 40), (2, 18, 1), 4), 'crown_d', 'f'), L(fat((86, 50), (76, 40), (98, 18, 1), -4), 'crown_d', 'f'),
     L(ell(50, 42, 3, 3), 'crown_d', 'f', False)]
    + brows(64, 'mid', 3.6, tilt=0.8) + [fang()],
    [L(outline([(70, 46), (80, 30), (84, 8), (78, -18, 1), (68, -4), (60, -30, 1), (50, -6), (40, -28, 1), (32, -4), (18, 8), (6, 30), (6, 56), (18, 72), (34, 70),
                (44, 56), (58, 50)])),
     L(outline([(6, 34), (30, 40), (42, 56), (34, 70), (18, 72), (6, 56)]), 'shade', 'b', False),
     L(outline([(30, 44), (40, 34), (66, 30), (90, 36), (92, 50), (66, 46), (42, 50)]), 'crown', 'f'),
     L(fat((70, 40), (80, 34), (66, 10, 1), 4), 'crown_d', 'f')] + brow_side(64, 'mid', 3.6, 0.8),
    [L(outline([(16, 76), (10, 44), (18, 14), (26, -10, 1), (36, 4), (44, -24, 1), (52, 0), (60, -24, 1), (66, 4), (76, -10, 1), (84, 14), (90, 44), (84, 76), (50, 82)])),
     L(outline([(58, 0), (76, -10), (84, 14), (90, 44), (84, 76), (64, 80)]), 'shade', 'b', False),
     L(outline([(10, 52), (12, 40), (50, 34), (88, 40), (90, 52), (50, 48)]), 'crown', 'f'),
     L(fat((14, 46), (24, 40), (4, 18, 1), 4), 'crown_d', 'f'), L(fat((86, 46), (76, 40), (96, 18, 1), -4), 'crown_d', 'f')])

# Sham Spike: hombre de cara larga y piel oscura; pelo gris claro muy corto peinado hacia atrás, y una coleta negra finísima que
# sale de la coronilla, sube y cae en látigo por la derecha; labios gruesos y nariz grande
v = views(crop, top=10, side=46, nape=78)
whip_f = [L(quad((58, 6), (62, -16), (76, -12)) + quad((76, -12), (88, -8), (80, 14)) + quad((80, 14), (74, 30), (82, 44)), BLACK, 'b', False, False, 2.6)]
add('sham-spike', 'delgado', pal('#d6c6ae', SK_D, iris='#2a2224'),
    {'eyes': 'round', 'brows': 'angry', 'mouth': 'lips', 'mouth_y': 94, 'mouth_w': 8, 'hairline': (48, 30)},
    whip_f + v['front'] + [strand([(30, 20), (34, 40)], 'shade', 'b', 1.0), strand([(70, 20), (66, 40)], 'shade', 'b', 1.0), nose(50, 86, 5)],
    v['side'] + [L(quad((40, 4), (30, -14), (14, -8)) + quad((14, -8), (0, -2), (4, 22)) + quad((4, 22), (8, 40), (-2, 56)), BLACK, 'b', False, False, 2.6)],
    v['back'] + [L(quad((50, 6), (54, -14), (66, -10)) + quad((66, -10), (80, -4), (72, 20)) + quad((72, 20), (66, 40), (74, 60)), BLACK, 'f', False, False, 2.6)])

# Sharkey Gobble: grandullón de pelo rosa rojizo revuelto y abultado, con una venda blanca atada en la frente, nariz gorda y
# boca torcida
BAND = (236, 222, 196, 255)
mf = messy('front', amp=14, n=9, seed=4, rx=50, ry=44, cy=44, lo=86)
add('sharkey-gobble', 'corpulento', pal('#c87068', SK_L, iris='#2a2224', band=BAND, band_d=(206, 190, 160, 255)),
    {'eyes': 'sharp', 'brows': False, 'mouth': 'line', 'mouth_y': 96, 'hairline': (62, 52)},
    mf + [L(outline([(8, 62), (10, 50), (50, 46), (90, 50), (92, 62), (50, 60)]), 'band', 'f'), strand([(14, 56), (86, 56)], 'band_d', 'f', 1.0),
          L(quad((40, 95), (52, 97), (62, 93)), LIP, 'f', False, False, 1.6), nose(50, 88, 6)],
    messy('side', amp=14, n=9, seed=4, rx=50, ry=44, cy=44, nape=96) + [L(outline([(4, 54), (10, 46), (60, 46), (90, 54), (90, 62), (60, 58), (8, 62)]), 'band', 'f')],
    messy('back', amp=14, n=9, seed=4, rx=50, ry=44, cy=44, nape=96) + [L(outline([(8, 60), (10, 50), (50, 46), (90, 50), (92, 60), (50, 58)]), 'band', 'f'),
                                                                       L(outline([(46, 56), (40, 72), (46, 70), (50, 58), (54, 70), (60, 72), (54, 56)]), 'band', 'f')])

# Shaun Imago: pelo lila grisáceo en pinchos con mechones sobre la frente y dos antenas finas marrones; ojos gris azulado
ANT = (120, 92, 70, 255)
add('shaun-imago', 'normal', pal('#7e7280', SK_T, iris='#6a8c8c'),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'hairline': False},
    [L(quad((32, 14), (24, -6), (22, -22)), ANT, 'b', False, False, 2.0), L(quad((68, 14), (76, -6), (78, -22)), ANT, 'b', False, False, 2.0)]
    + messy('front', amp=12, n=10, seed=7, rx=48, ry=40, cy=42, lo=74)
    + [fringe([(14, 66, 1), (16, 46), (30, 32), (50, 28), (70, 32), (84, 46), (86, 66, 1), (78, 54), (70, 62, 1), (64, 48), (54, 66, 1), (48, 50), (38, 64, 1), (34, 50),
               (24, 60)])],
    [L(quad((40, 12), (36, -8), (44, -22)), ANT, 'b', False, False, 2.0)] + messy('side', amp=12, n=10, seed=7, rx=48, ry=40, cy=42, nape=90)
    + [fringe([(66, 20), (86, 30), (92, 54, 1), (82, 46), (76, 56, 1), (70, 40)])],
    [L(quad((32, 14), (24, -6), (22, -22)), ANT, 'b', False, False, 2.0), L(quad((68, 14), (76, -6), (78, -22)), ANT, 'b', False, False, 2.0)]
    + messy('back', amp=12, n=10, seed=7, rx=48, ry=40, cy=42, nape=90))

# Shaun Staid (portero): pelo naranja ondulado hasta el cuello, con raya a un lado y un mechón que le cae sobre la frente; piel
# clara, ceño serio y un pendiente
add('shaun-staid', 'normal', pal('#d26a22', SK_P, iris='#3a2a22'),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': [(14, 70), (18, 48), (30, 42), (44, 52), (58, 36), (74, 42), (86, 50), (88, 70)]},
    longhair('front', length=104, flare=4, top=0) + [strand([(14, 70), (10, 84), (16, 96)], 'shade', 'b', 1.2), strand([(86, 70), (90, 84), (84, 96)], 'shade', 'b', 1.2),
                                                     fringe([(20, 46), (30, 26), (50, 18), (62, 30), (56, 40), (44, 56, 1), (40, 42), (30, 52, 1)]),
                                                     strand([(58, 6), (62, 24)], 'deep', 'b', 1.2)] + earring('front', (220, 220, 230, 255)),
    longhair('side', length=104, flare=4) + [strand([(10, 50), (6, 76), (12, 96)], 'shade', 'b', 1.2)],
    longhair('back', length=104, flare=4, ends=4) + [strand([(36, 30), (30, 70), (36, 96)], 'shade', 'b', 1.2), strand([(64, 30), (70, 70), (64, 96)], 'shade', 'b', 1.2)])

# Shawn Broker (portero): bajito y de cara redonda; casco de pelo morado oscuro con las puntas vueltas hacia fuera a la altura
# de las orejas; ojos caídos con ojeras y boca torcida
add('shawn-broker', 'bajito', pal('#5a4e68', SK_L, iris='#2a2224'),
    {'eyes': 'normal', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'hairline': [(14, 70), (16, 50), (34, 40), (60, 36), (86, 48), (88, 70)],
     'face_front': blob([(14, 56), (50, 40), (86, 56), (90, 80), (80, 100), (50, 108), (20, 100), (10, 80)])},
    [L(outline([(16, 80), (4, 84, 1), (10, 70), (8, 44), (18, 18), (50, 6), (82, 18), (92, 44), (90, 70), (96, 84, 1), (84, 80), (82, 60), (18, 60)])),
     L(outline([(60, 8), (84, 20), (92, 46), (88, 72), (80, 50)]), 'shade', 'b', False),
     fringe([(14, 56), (18, 38), (36, 26), (62, 24), (82, 34), (86, 52), (72, 42), (50, 38, 1), (54, 44), (30, 44), (22, 56)]),
     L([(28, 82), (40, 82)], (190, 130, 100, 255), 'f', False, False, 1.0), L([(60, 82), (72, 82)], (190, 130, 100, 255), 'f', False, False, 1.0)],
    [L(outline([(60, 54), (66, 42), (84, 38), (90, 22), (76, 6), (50, 0), (24, 6), (8, 26), (4, 52), (8, 74), (-2, 80, 1), (14, 82), (30, 80), (40, 66), (48, 56)])),
     L(outline([(4, 40), (30, 44), (40, 64), (30, 80), (10, 76)]), 'shade', 'b', False)],
    [L(outline([(14, 78), (2, 84, 1), (10, 66), (8, 42), (18, 16), (50, 4), (82, 16), (92, 42), (90, 66), (98, 84, 1), (86, 78), (50, 86)])),
     L(outline([(58, 6), (82, 18), (92, 44), (90, 70), (86, 78), (62, 84)]), 'shade', 'b', False)])

# Shay Chez: calvo de piel morena y cuello largo, con un moño claro en llama en lo alto de la cabeza; ojos pequeños y sonrisa
add('shay-chez', 'delgado', pal('#f0d2aa', '#b08c68', iris='#2a2224', scalp='#a07c5a'),
    {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': False, 'big_ears': 2},
    [scalp('front'), L(outline([(38, 14), (36, 0), (40, -14), (46, -8), (48, -26, 1), (54, -12), (60, -22, 1), (62, -4), (64, 14)])),
     L(outline([(54, -12), (60, -22), (62, -4), (64, 14), (54, 10)]), 'shade', 'b', False),
     L(outline([(36, 16), (40, 10), (60, 10), (64, 16), (60, 20), (40, 20)]), BLACK, 'f', False)] + cheek_lines(84),
    [L(outline([(28, 12), (24, -4), (30, -16), (36, -10), (40, -26, 1), (44, -10), (52, -18, 1), (52, 2), (50, 14)])),
     L(outline([(24, 14), (28, 8), (50, 8), (54, 14), (50, 18), (28, 18)]), BLACK, 'b', False)],
    [L(outline([(38, 14), (36, 0), (40, -14), (46, -8), (48, -26, 1), (54, -12), (60, -22, 1), (62, -4), (64, 14)])),
     L(outline([(36, 16), (40, 10), (60, 10), (64, 16), (60, 20), (40, 20)]), BLACK, 'f', False)])


def spiky(view, seed, amp=12, n=10, rx=48, ry=40, cy=42, lo=70, nape=90, sweep=0.0, shade=True):
    return messy(view, amp=amp, n=n, seed=seed, rx=rx, ry=ry, cy=cy, lo=lo, nape=nape, sweep=sweep, shade=shade)


def tall(view, tips, base=44, w=0, c='mid'):
    """Pelo de punta hacia arriba (cepillo alto o llamas): tips, las puntas de izquierda a derecha (x, y)."""
    if view == 'front':
        pts = [(18 - w, base + 8), (14 - w, 30)]
        for i, (x, y) in enumerate(tips):
            pts += [(x, y, 1)] + ([((x + tips[i + 1][0]) / 2, min(base - 18, (y + tips[i + 1][1]) / 2 + 22))] if i + 1 < len(tips) else [])
        pts += [(86 + w, 30), (82 + w, base + 8), (50, base)]
        return [L(outline(pts), c), L(outline([(62, 10), (84 + w, 26), (82 + w, base + 6), (70, base - 2)]), 'shade', 'b', False)]
    if view == 'side':
        pts = [(66, 48), (82, 40), (88, 26)]
        for i, (x, y) in enumerate(reversed(tips)):
            xx = 90 - (i + 0.5) * 80 / len(tips)
            pts += [(xx + 6, y + 4, 1), (xx - 2, min(30, y + 26))]
        pts += [(4, 30), (2, 56), (12, 76), (30, 80), (40, 66), (48, 54)]
        return [L(outline(pts), c), L(outline([(4, 40), (30, 44), (40, 64), (30, 80), (12, 76)]), 'shade', 'b', False)]
    pts = [(16 - w, 76), (12 - w, 30)]
    for i, (x, y) in enumerate(tips):
        pts += [(x, y + 4, 1)] + ([((x + tips[i + 1][0]) / 2, min(26, (y + tips[i + 1][1]) / 2 + 24))] if i + 1 < len(tips) else [])
    pts += [(88 + w, 30), (84 + w, 76), (50, 84)]
    return [L(outline(pts), c), L(outline([(60, 10), (86 + w, 28), (84 + w, 76), (64, 82)]), 'shade', 'b', False)]


def bob(view, lo=86, top=4, flare=4, c='mid', ends=0):
    """Melena corta redonda (casco) que cubre las orejas hasta lo."""
    if view == 'front':
        pts = [(16, lo), (10 - flare, lo + 2, 1), (8, 56), (10, 32), (22, 12 + top), (50, top), (78, 12 + top), (90, 32), (92, 56), (90 + flare, lo + 2, 1), (84, lo),
               (82, 60), (18, 60)]
        return [L(outline(pts), c), L(outline([(60, top + 4), (82, 16 + top), (92, 40), (90, lo - 4), (82, 56)]), 'shade', 'b', False)]
    if view == 'side':
        pts = [(58, 56), (66, 44), (84, 40), (90, 22), (74, 4 + top), (46, -2 + top), (20, 6 + top), (6, 26), (2, 56), (4, lo - 4), (0 - flare, lo + 2, 1), (20, lo),
               (34, lo - 6), (40, 70), (48, 60)]
        return [L(outline(pts), c), L(outline([(3, 40), (30, 46), (40, 66), (34, lo - 6), (14, lo - 2)]), 'shade', 'b', False)]
    pts = [(14, lo), (8 - flare, lo + 2, 1), (8, 56), (10, 32), (22, 12 + top), (50, top), (78, 12 + top), (90, 32), (92, 56), (92 + flare, lo + 2, 1), (86, lo)]
    for i in range(ends):
        x = 86 - (i + 1) * 72 / (ends + 1)
        pts += [(x + 6, lo - 6), (x, lo + 4, 1)]
    pts.append((50, lo + 2))
    return [L(outline(pts), c), L(outline([(58, top + 4), (82, 16 + top), (92, 44), (92, lo), (64, lo + 2)]), 'shade', 'b', False)]


def curls(cx, cy, rx, ry, n=9, a0=0.0, k=0.84):
    """Nube de rizos: bultos redondos alrededor del centro."""
    import math
    pts = []
    for i in range(n * 2):
        a = a0 + math.pi * 2 * i / (n * 2)
        f = 1.0 if i % 2 == 0 else k
        pts.append((cx + rx * f * math.cos(a), cy + ry * f * math.sin(a)))
    return blob(pts, 6)


# ------------------------------------------------------------------ hoja 1

# Shem Bassey: casco de pelo verde musgo con las puntas en picos abiertos hacia fuera a la altura de las orejas y flequillo hasta
# los ojos; piel morena y ceño
add('shem-bassey', 'normal', pal('#729642', SK_O, iris='#3a3048'),
    {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 94, 'hairline': False},
    [L(outline([(20, 78), (-6, 66, 1), (8, 60), (6, 36), (20, 12), (50, 2), (80, 12), (94, 36), (92, 60), (106, 66, 1), (80, 78), (80, 62), (20, 62)])),
     L(outline([(60, 6), (82, 16), (94, 40), (92, 60), (82, 62), (76, 40)]), 'shade', 'b', False),
     fringe([(14, 66), (16, 44), (30, 28), (50, 24), (70, 28), (84, 44), (86, 66, 1), (76, 60), (70, 68, 1), (62, 60), (54, 70, 1), (46, 60), (38, 70, 1), (32, 60),
             (24, 68, 1)]),
     strand([(36, 30), (40, 56)], 'shade', 'f', 1.0), strand([(62, 30), (60, 56)], 'shade', 'f', 1.0)],
    [L(outline([(62, 60), (70, 48), (88, 46), (94, 28), (78, 6), (50, -2), (22, 6), (6, 30), (2, 56), (-14, 70, 1), (10, 74), (26, 84, 1), (36, 72), (46, 64)])),
     L(outline([(4, 40), (30, 46), (40, 64), (26, 84), (10, 74)]), 'shade', 'b', False), fringe([(70, 20), (90, 34), (94, 64, 1), (84, 56), (78, 64, 1), (72, 48)])],
    [L(outline([(16, 80), (-6, 68, 1), (8, 60), (6, 36), (20, 12), (50, 2), (80, 12), (94, 36), (92, 60), (106, 68, 1), (84, 80), (70, 76), (60, 88, 1), (50, 78), (40, 88, 1),
                (30, 76)])),
     L(outline([(58, 6), (82, 16), (94, 40), (92, 62), (84, 80), (64, 80)]), 'shade', 'b', False)])

# Shemmy Ramis: bajito con una nube enorme de rizos crema amarillenta en espirales; cejas claras, ojos redondos muy abiertos y
# una boca naranja enorme de sonrisa
ORANGE_MOUTH = (226, 126, 60, 255)
add('shemmy-ramis', 'bajito', pal('#d6d49a', SK_L, iris='#2a2224'),
    {'eyes': 'round', 'brows': False, 'mouth': 'none', 'hairline': False, 'eye_sep': 15},
    [L(curls(50, 34, 52, 40, 10, 0.3)), L(curls(62, 30, 30, 26, 6, 0.6), 'shade', 'b', False),
     L(curls(50, 40, 38, 18, 8, 0.2), 'mid', 'f'),
     L(curls(66, 30, 9, 8, 4), 'shade', 'f', ln=True), L(curls(34, 34, 8, 7, 4), 'shade', 'f', ln=True),
     L(blob([(38, 92), (50, 90), (62, 92), (60, 99), (50, 102), (40, 99)], 6), ORANGE_MOUTH, 'f', ln=True),
     L(quad((38, 94), (50, 97), (62, 94)), OUTC, 'f', False, False, 1.0),
     L(ell(36, 63, 5, 1.6), (230, 226, 170, 255), 'f', ln=True), L(ell(64, 63, 5, 1.6), (230, 226, 170, 255), 'f', ln=True)],
    [L(curls(42, 38, 48, 40, 10, 0.3)), L(curls(24, 46, 22, 26, 6), 'shade', 'b', False),
     L(blob([(80, 92), (88, 90), (90, 98), (82, 100)], 6), ORANGE_MOUTH, 'f', ln=True)],
    [L(curls(50, 40, 52, 44, 10, 0.3)), L(curls(64, 44, 28, 34, 6, 0.4), 'shade', 'b', False)])

# Shep Shank: hombre de cara larga y barbilla grande; melena castaño rojizo ondulada hasta los hombros con raya en medio; un
# ojo guiñado y sonrisa torcida
add('shep-shank', 'delgado', pal('#a8460c', SK_P, iris='#2a2224'),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': [(14, 66), (18, 44), (32, 36), (50, 40), (68, 36), (82, 44), (86, 66)],
     'face_front': blob([(18, 52), (50, 36), (82, 52), (84, 80), (74, 102), (50, 110), (26, 102), (16, 80)])},
    longhair('front', length=112, flare=6, top=0, part=True)
    + [strand([(12, 60), (6, 80), (12, 100)], 'shade', 'b', 1.2), strand([(88, 60), (94, 80), (88, 100)], 'shade', 'b', 1.2), nose(52, 86, 4)],
    longhair('side', length=112, flare=6) + [strand([(14, 44), (6, 74), (14, 100)], 'shade', 'b', 1.2)],
    longhair('back', length=112, flare=6, ends=5, part=True) + [strand([(30, 30), (24, 70), (30, 104)], 'shade', 'b', 1.2),
                                                               strand([(70, 30), (76, 70), (70, 104)], 'shade', 'b', 1.2)])

# Shirley Ladyman (chica): pelo granate oscuro recogido en una coleta alta de puntas, con flequillo en estrella; ojos con brillos
add('shirley-ladyman', 'chica', pal('#74424e', SK_L, iris='#2a2a3a'),
    {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    [L(outline([(40, 8), (34, -6), (30, -22, 1), (40, -14), (44, -28, 1), (50, -14), (58, -28, 1), (60, -12), (70, -20, 1), (64, -4), (60, 8)])),
     L(ell(50, 6, 8, 4), (230, 214, 170, 255), 'b'),
     L(outline([(16, 66), (12, 40), (22, 16), (50, 8), (78, 16), (88, 40), (84, 66), (80, 50), (20, 50)])),
     L(outline([(60, 10), (80, 18), (88, 40), (84, 62), (78, 40)]), 'shade', 'b', False),
     fringe([(16, 56), (18, 40), (30, 28), (50, 22), (70, 28), (82, 40), (84, 56), (74, 50), (66, 60, 1), (60, 46), (50, 58, 1), (40, 46), (34, 60, 1), (26, 50)])],
    [L(outline([(26, 10), (14, -6), (10, -22, 1), (22, -12), (24, -26, 1), (32, -12), (40, -20, 1), (40, -2), (38, 8)])),
     L(outline([(62, 56), (68, 44), (84, 40), (90, 24), (74, 8), (48, 2), (22, 10), (8, 30), (6, 56), (16, 74), (32, 76), (40, 64), (50, 56)])),
     L(outline([(6, 40), (30, 44), (40, 64), (32, 76), (16, 74)]), 'shade', 'b', False), fringe([(70, 16), (90, 30), (90, 54, 1), (80, 42), (74, 52, 1), (70, 36)])],
    [L(outline([(16, 76), (12, 40), (22, 16), (50, 8), (78, 16), (88, 40), (84, 76), (50, 84)])),
     L(outline([(58, 10), (80, 18), (88, 44), (84, 76), (62, 82)]), 'shade', 'b', False),
     strand([(50, 12), (40, 40), (36, 70)], 'shade', 'b', 1.0), strand([(50, 12), (60, 40), (64, 70)], 'shade', 'b', 1.0),
     L(ell(50, 8, 8, 4), (230, 214, 170, 255), 'f'),
     L(outline([(40, 6), (34, -8), (30, -22, 1), (40, -14), (44, -28, 1), (50, -14), (58, -28, 1), (60, -12), (70, -20, 1), (64, -6), (60, 6)]), 'mid', 'f')])

# Shylock Watson: pelo melocotón muy claro en casco de tazón con flequillo recto en mechones; ojos redondos verde oliva
add('shylock-watson', 'normal', pal('#f6dcc0', SK_P, iris='#7a7a5a', shade='#e8b896', deep='#c8946e'),
    {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'hairline': False},
    bob('front', lo=76, top=2, flare=0) + [L(outline([(12, 66), (12, 40), (24, 18), (50, 10), (76, 18), (88, 40), (88, 66), (50, 64)]), 'mid', 'f'),
                                           L(outline([(14, 50), (50, 44), (86, 50), (88, 66), (50, 64), (12, 66)]), 'shade', 'f', False)]
    + [strand([(x, 50), (x, 64)], 'deep', 'f', 0.9) for x in (24, 34, 44, 56, 66, 76)],
    bob('side', lo=76, top=2, flare=0) + [fringe([(66, 16), (86, 26), (92, 46), (90, 62), (76, 58), (70, 40)])],
    bob('back', lo=80, top=2, flare=0))

# Sid Parting: pelo azul marino con un flequillo enorme peinado de lado que sale en punta hacia la izquierda, nuca corta y un
# pelillo de punta arriba
add('sid-parting', 'normal', pal('#364e68', SK_L, iris='#2a2224'),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': [(14, 64), (20, 50), (40, 52), (60, 44), (80, 46), (86, 64)]},
    crop('front', top=2, side=64, w=2) + [fringe([(-12, 46, 1), (8, 38), (22, 20), (44, 10), (66, 12), (84, 26), (88, 44), (70, 40), (56, 46), (40, 50), (22, 50), (14, 48)]),
                                          L(quad((70, 12), (76, -4), (82, -6)), 'mid', 'b', False, False, 2.4),
                                          strand([(30, 26), (6, 42)], 'deep', 'f', 1.0)],
    crop('side', top=2, w=2) + [fringe([(60, 6), (86, 18), (100, 40, 1), (84, 36), (70, 30)]), L(quad((54, 2), (56, -12), (62, -14)), 'mid', 'b', False, False, 2.4)],
    crop('back', top=2, w=2) + [L(quad((68, 14), (74, -2), (80, -4)), 'mid', 'b', False, False, 2.4)])

# Silas Scrooge: hombre de nariz grande y melena lisa naranja hasta el pecho, con raya a un lado que le despeja la frente
add('silas-scrooge', 'delgado', pal('#d2721e', SK_P, iris='#2a2224'),
    {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': [(14, 70), (18, 48), (26, 34), (44, 30), (60, 34), (76, 42), (86, 58), (88, 70)]},
    longhair('front', length=122, flare=4, top=0) + [strand([(42, 2), (24, 30), (16, 70)], 'shade', 'b', 1.2), strand([(56, 4), (80, 30), (86, 70)], 'shade', 'b', 1.2),
                                                     nose(52, 86, 5)],
    longhair('side', length=122, flare=4) + [strand([(30, 4), (10, 60), (14, 110)], 'shade', 'b', 1.2)],
    longhair('back', length=122, flare=4, ends=5, part=True))

# Silver Platt: pelo amarillo peinado hacia atrás con mechones que le caen por la frente y la nuca larga; ceño y media sonrisa
add('silver-platt', 'normal', pal('#d6bc1e', SK_L, iris='#5a5230'),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': [(14, 66), (20, 46), (36, 40), (50, 44), (64, 38), (80, 44), (86, 66)]},
    crop('front', top=2, side=68, w=2) + [strand([(50, 4), (30, 30), (24, 56)], 'shade', 'b', 1.2), strand([(50, 4), (70, 30), (78, 56)], 'shade', 'b', 1.2),
                                          strand([(50, 4), (46, 30), (40, 58)], 'deep', 'f', 1.0), strand([(50, 4), (58, 32), (62, 56)], 'deep', 'f', 1.0)],
    crop('side', top=2, nape=96, w=2) + [strand([(80, 14), (40, 10), (10, 40)], 'shade', 'b', 1.2)],
    crop('back', top=2, nape=96, w=2) + [strand([(50, 6), (40, 50), (44, 92)], 'shade', 'b', 1.2), strand([(50, 6), (62, 50), (58, 92)], 'shade', 'b', 1.2)])


# ------------------------------------------------------------------ hoja 2

# Sim Cope: melena ondulada y abultada malva grisáceo que le tapa las orejas; ojos cerrados de risa y sonrisa
add('sim-cope', 'normal', pal('#bca4a4', SK_P, iris='#2a2224'),
    {'eyes': 'closed', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': [(14, 66), (20, 46), (32, 40), (50, 34), (66, 30), (80, 40), (86, 66)]},
    [L(curls(14, 70, 12, 20, 5, 0.3)), L(curls(86, 70, 12, 20, 5, 0.6)), L(curls(50, 34, 50, 36, 10, 0.2)),
     L(curls(72, 26, 16, 16, 5), 'shade', 'b', False), strand([(30, 20), (50, 30), (70, 18)], 'deep', 'b', 1.0)],
    [L(curls(24, 70, 22, 22, 6)), L(curls(44, 34, 48, 36, 10, 0.2)), L(curls(18, 62, 10, 14, 5), 'shade', 'b', False)],
    [L(curls(50, 66, 42, 28, 8, 0.3)), L(curls(50, 36, 50, 38, 10, 0.2)), L(curls(72, 56, 14, 18, 5), 'shade', 'b', False)])

# Sim Pathy: frente despejada con pico en medio y melena morada oscura en rulos gruesos hasta los hombros; ojos rojos afilados
DRK = '#665a74'
rolls_f = [L(rope((16, 56), (8, 76), (14, 100), 11)), L(rope((26, 54), (20, 80), (24, 104), 10)), L(rope((84, 56), (92, 76), (86, 100), 11)),
           L(rope((74, 54), (80, 80), (76, 104), 10))]
add('sim-pathy', 'normal', pal(DRK, SK_L, iris='#b03a3a'),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'hairline': [(14, 64), (20, 44), (34, 34), (44, 30), (50, 40), (56, 30), (66, 34), (80, 44), (86, 64)]},
    rolls_f + crop('front', top=0, side=64, w=4),
    crop('side', top=0, nape=94, w=4) + [L(rope((10, 50), (0, 80), (8, 106), 12)), L(rope((26, 60), (20, 84), (28, 104), 11)), L(rope((40, 60), (38, 84), (44, 100), 10))],
    crop('back', top=0, nape=90, w=4) + [L(rope((x, 50), (x + (x - 50) * 0.15, 80), (x, 104), 11), 'mid', 'f') for x in (14, 30, 50, 70, 86)]
    + [strand([(x, 56), (x, 96)], 'shade', 'f', 1.0) for x in (14, 30, 50, 70, 86)])

# Simon Stryker (portero): hombre de mandíbula marcada; pelo castaño oliva con raya en medio en dos cortinas y un moñito arriba;
# ojos verdosos y sonrisa de dientes
add('simon-stryker', 'delgado', pal('#5a4e22', SK_L, iris='#6a7a5a'),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 95, 'hairline': [(14, 62), (20, 46), (36, 42), (48, 50), (52, 50), (64, 42), (80, 46), (86, 62)]},
    [L(outline([(42, 8), (40, -6), (48, -14), (56, -10), (58, 0), (56, 8)])), strand([(44, 6), (56, 6)], 'deep', 'b', 1.4)] + crop('front', top=4, side=64)
    + [strand([(50, 6), (36, 30), (24, 50)], 'deep', 'b', 1.0), strand([(50, 6), (64, 30), (76, 50)], 'deep', 'b', 1.0)],
    [L(outline([(36, 6), (34, -8), (42, -16), (50, -12), (52, -2), (50, 6)]))] + crop('side', top=4),
    [L(outline([(42, 8), (40, -6), (48, -14), (56, -10), (58, 0), (56, 8)]))] + crop('back', top=4))

# Skip Rooter: hombre de cara arrugada; pelo rubio oscuro en pinchos peinados hacia atrás con pico en la frente y puntas a los
# lados; un ojo guiñado
add('skip-rooter', 'delgado', pal('#c8a45c', SK_L, iris='#2a2224'),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': [(14, 60), (22, 44), (36, 38), (50, 50), (64, 38), (78, 44), (86, 60)]},
    spiky('front', 11, amp=12, n=9, lo=64, sweep=0.2) + [nose(50, 86, 4)] + cheek_lines(88),
    spiky('side', 11, amp=14, n=9, sweep=-0.3),
    spiky('back', 11, amp=12, n=9))

# Skip Sofrenic: grandullón de cabeza redonda y piel pálida, casi calvo, con un mechón azul marino de punta arriba; cejas gruesas,
# nariz de oso marrón y morros
NAVY = '#364e68'
add('skip-sofrenic', 'corpulento', pal(NAVY, '#e8d6c0', iris='#2a2224', nose=(150, 96, 70, 255)),
    {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 97, 'hairline': False, 'nose': (50, 86, 4.4),
     'face_front': blob([(14, 54), (50, 40), (86, 54), (92, 78), (82, 102), (50, 110), (18, 102), (8, 78)])},
    [scalp('front'), L(outline([(36, 22), (30, 8), (36, 2), (38, -10, 1), (46, 0), (52, -14, 1), (56, 0), (64, -8, 1), (64, 6), (70, 12), (64, 22), (50, 18)])),
     L(outline([(52, 0), (64, -8), (64, 6), (70, 12), (64, 22), (56, 18)]), 'shade', 'b', False)] + brows(64, 'mid', 4.4, tilt=1.0),
    [L(outline([(30, 18), (26, 6), (34, -6, 1), (40, 2), (50, -10, 1), (54, 4), (62, 8), (58, 18)]))] + brow_side(64, 'mid', 4.4, 1.0),
    [L(outline([(36, 22), (30, 8), (36, 2), (38, -10, 1), (46, 0), (52, -14, 1), (56, 0), (64, -8, 1), (64, 6), (70, 12), (64, 22), (50, 18)]))])

# Slim Lanky (portero): flaco de cara alargada y pómulos marcados; pelo gris verdoso en pinchos muy altos hacia arriba
add('slim-lanky', 'delgado', pal('#7e8a7e', '#e8b884', iris='#2a2224'),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98, 'hairline': [(14, 56), (24, 46), (38, 42), (50, 46), (62, 42), (76, 46), (86, 56)],
     'face_front': blob([(20, 52), (50, 42), (80, 52), (82, 78), (68, 102), (50, 110), (32, 102), (18, 78)])},
    tall('front', [(4, 10), (18, -14), (34, -30), (50, -34), (66, -30), (82, -14), (96, 10)], base=48)
    + [L([(30, 84), (36, 96)], LIP, 'f', False, False, 1.0), L([(70, 84), (64, 96)], LIP, 'f', False, False, 1.0), nose(50, 88, 3)],
    tall('side', [(6, -4), (20, -24), (40, -30), (60, -26), (80, -12)]),
    tall('back', [(6, 10), (20, -12), (36, -26), (50, -30), (64, -26), (80, -12), (94, 10)]))

# Sly O'Hands (portero): pelo verde menta casi blanco revuelto con un pelillo de punta arriba; gafas negras rectangulares y sonrisa
add('sly-o-hands', 'normal', pal('#d4eedc', SK_L, iris='#2a2224', shade='#a8c4b4', deep='#7a948a'),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False, 'glasses': OUTC, 'glasses_rect': True},
    spiky('front', 21, amp=10, n=10, lo=70) + [L(quad((50, 6), (44, -12), (54, -22)), 'mid', 'b', False, False, 2.4),
                                               fringe([(14, 70, 1), (16, 46), (30, 32), (50, 28), (70, 32), (84, 46), (86, 70, 1), (78, 56), (68, 64, 1), (62, 50),
                                                       (50, 62, 1), (42, 50), (32, 64, 1), (26, 52)])],
    spiky('side', 21, amp=10, n=10) + [L(quad((50, 4), (46, -14), (58, -22)), 'mid', 'b', False, False, 2.4)],
    spiky('back', 21, amp=10, n=10) + [L(quad((50, 6), (44, -12), (54, -22)), 'mid', 'b', False, False, 2.4)])

# Sly Winker: casco de motorista azul verdoso con una franja crema ancha y el borde azul marino alrededor de la cara; piel tostada
# y ojos redondos
HEL, HEL_D, HEL_B, RIM = (108, 154, 154, 255), (78, 120, 124, 255), (224, 220, 162, 255), (54, 78, 114, 255)
add('sly-winker', 'normal', pal('#364e72', SK_T, iris='#2a2224'),
    {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'hairline': False},
    [L(outline([(10, 80), (4, 50), (12, 18), (50, -4), (88, 18), (96, 50), (90, 80), (80, 82), (82, 62), (50, 54), (18, 62), (20, 82)]), HEL),
     L(outline([(8, 36), (16, 18), (50, 6), (84, 18), (92, 36), (50, 26)]), HEL_B, 'b', False),
     L(outline([(14, 10), (50, -4), (86, 10), (70, 4), (50, 0), (30, 4)]), HEL, 'b', False),
     L(outline([(60, -2), (88, 18), (96, 50), (90, 78), (84, 56)]), HEL_D, 'b', False),
     L(outline([(14, 84), (12, 60), (24, 50), (50, 46), (76, 50), (88, 60), (86, 84), (80, 84), (78, 62), (50, 56), (22, 62), (20, 84)]), RIM, 'f')]
    + cheek_lines(86),
    [L(outline([(70, 60), (74, 42), (92, 36), (94, 16), (70, -2), (40, -6), (14, 6), (0, 32), (0, 64), (10, 84), (34, 86), (50, 74), (60, 62)]), HEL),
     L(outline([(4, 22), (30, 4), (74, 6), (92, 24), (92, 34), (70, 22), (30, 20), (2, 40)]), HEL_B, 'b', False),
     L(outline([(70, 64), (74, 44), (90, 38), (94, 42), (80, 50), (76, 66)]), RIM, 'f')],
    [L(outline([(10, 84), (4, 50), (12, 18), (50, -4), (88, 18), (96, 50), (90, 84), (50, 92)]), HEL),
     L(outline([(6, 40), (14, 20), (50, 8), (86, 20), (94, 40), (50, 30)]), HEL_B, 'b', False),
     L(outline([(60, -2), (88, 18), (96, 50), (90, 84), (64, 90)]), HEL_D, 'b', False),
     L(outline([(10, 84), (50, 92), (90, 84), (90, 90), (50, 98), (10, 90)]), RIM, 'f')])


# ------------------------------------------------------------------ hoja 3

# Sol Crater: cara ancha de párpados caídos; pelo verde oliva oscuro rapado con una cresta corta de pinchos arriba; una marca de
# arcoíris en la mejilla
add('sol-crater', 'corpulento', pal('#5a5a2c', SK_L, iris='#2a2224'),
    {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': (50, 34),
     'face_front': blob([(14, 54), (50, 40), (86, 54), (92, 80), (80, 102), (50, 108), (20, 102), (8, 80)])},
    crop('front', top=12, side=48, w=-2) + [L(outline([(36, 18), (30, 2, 1), (40, 8), (44, -14, 1), (50, 4), (56, -18, 1), (60, 4), (70, -6, 1), (66, 10), (64, 20)])),
                                            L(quad((66, 80), (76, 84), (74, 100)), (86, 160, 90, 255), 'f', False, False, 2.0),
                                            L(quad((70, 78), (80, 82), (78, 100)), (226, 150, 70, 255), 'f', False, False, 1.6),
                                            L([(28, 72), (44, 72)], OUTC, 'f', False, False, 1.4), L([(56, 72), (72, 72)], OUTC, 'f', False, False, 1.4)],
    crop('side', top=12, w=-2) + [L(outline([(40, 12), (38, -6, 1), (48, 2), (56, -16, 1), (60, 4), (70, -6, 1), (70, 12)]))],
    crop('back', top=12, w=-2) + [L(outline([(36, 18), (32, 2, 1), (42, 8), (46, -12, 1), (52, 4), (58, -16, 1), (62, 4), (70, -4, 1), (66, 18)]))])

# Sol Stiss: trenzas pegadas castaño oliva que acaban en seis moños alrededor de la cabeza; gafas de sol amarillas octogonales
GOLD = (226, 196, 40, 255)
LENS = (120, 96, 50, 255)
buns_f = [L(curls(x, y, 8, 8, 5, 0.4)) for x, y in ((14, 40), (24, 14), (42, 0), (58, 0), (76, 14), (86, 40))]
add('sol-stiss', 'normal', pal('#968044', SK_T, iris='#2a2224'),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': (52, 38)},
    buns_f + crop('front', top=4, side=52) + [strand([(x, 10), (x + (x - 50) * 0.3, 42)], 'shade', 'b', 1.0) for x in (30, 40, 50, 60, 70)]
    + [L(outline([(cx - 10, 70, 1), (cx - 6, 66, 1), (cx + 6, 66, 1), (cx + 10, 70, 1), (cx + 10, 78, 1), (cx + 6, 82, 1), (cx - 6, 82, 1), (cx - 10, 78, 1)]), LENS, 'f')
       for cx in (36, 64)]
    + [L([(cx - 10, 70), (cx - 6, 66), (cx + 6, 66), (cx + 10, 70), (cx + 10, 78), (cx + 6, 82), (cx - 6, 82), (cx - 10, 78), (cx - 10, 70)], GOLD, 'f', False, False, 2.0)
       for cx in (36, 64)] + [L([(46, 72), (54, 72)], GOLD, 'f', False, False, 1.6)],
    [L(curls(x, y, 8, 8, 5, 0.4)) for x, y in ((10, 50), (16, 22), (36, 4), (60, 2))] + crop('side', top=4)
    + [L([(74, 68), (86, 68), (88, 80), (76, 80), (74, 68)], GOLD, 'f', False, False, 2.0), L([(74, 70), (50, 66)], GOLD, 'f', False, False, 1.6)],
    [L(curls(x, y, 8, 8, 5, 0.4)) for x, y in ((14, 44), (24, 16), (42, 2), (58, 2), (76, 16), (86, 44), (50, 70))] + crop('back', top=4)
    + [strand([(x, 10), (x + (x - 50) * 0.2, 70)], 'shade', 'b', 1.0) for x in (30, 40, 50, 60, 70)])

# Solomon Justice: hombre de mandíbula ancha; pelo caoba peinado de lado en una onda grande que cae hacia la derecha
add('solomon-justice', 'delgado', pal('#ae4410', SK_L, iris='#2a2224'),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': [(14, 60), (20, 44), (34, 38), (46, 44), (60, 36), (78, 40), (86, 60)]},
    crop('front', top=2, side=62, w=2) + [fringe([(30, 40), (36, 20), (54, 10), (76, 14), (92, 32), (96, 48, 1), (84, 42), (72, 36), (56, 40), (44, 46)]),
                                          strand([(46, 12), (60, 34)], 'shade', 'f', 1.0), nose(51, 86, 4)],
    crop('side', top=2, w=2) + [fringe([(60, 4), (86, 16), (98, 36, 1), (84, 34), (70, 28)])],
    crop('back', top=2, w=2))

# Solomon Osaka: cara ancha; pelo verde azulado peinado hacia atrás en ondas, con patillas largas; cejas negras muy gruesas
add('solomon-osaka', 'normal', pal('#5a8a7e', SK_L, iris='#2a2224'),
    {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 95, 'hairline': [(14, 80), (16, 52), (28, 42), (50, 40), (72, 42), (84, 52), (86, 80)],
     'face_front': blob([(14, 54), (50, 42), (86, 54), (90, 80), (78, 102), (50, 108), (22, 102), (10, 80)])},
    crop('front', top=4, side=82, w=3) + [strand([(24, 30), (40, 20), (60, 22), (78, 32)], 'deep', 'b', 1.2), strand([(20, 44), (40, 34), (62, 36), (82, 46)], 'deep', 'b', 1.2)]
    + brows(64, BLACK, 5.0, tilt=1.2, w=13),
    crop('side', top=4, w=3) + [strand([(80, 24), (50, 16), (20, 30)], 'deep', 'b', 1.2)] + brow_side(64, BLACK, 5.0, 1.2),
    crop('back', top=4, w=3) + [strand([(20, 40), (50, 50), (80, 40)], 'deep', 'b', 1.2), strand([(20, 60), (50, 70), (80, 60)], 'deep', 'b', 1.2)])

# Sonny East (portero): piel oscura y pelo verde oscuro rapado; una tirita en la nariz, ojos redondos y ceño
add('sonny-east', 'normal', pal('#2c5a44', '#b07848', iris='#2a2224'),
    {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'hairline': (54, 40)},
    crop('front', top=6, side=54, w=-1) + [L(blob([(44, 78), (56, 78), (57, 82), (43, 82)], 4), (236, 220, 200, 255), 'f', ln=True)],
    crop('side', top=6, w=-1), crop('back', top=6, w=-1))

# Sonny Rentman: melena verde lisa hasta los hombros con un flequillo de mechones que le tapa media cara; piel tostada
add('sonny-rentman', 'normal', pal('#4e9660', SK_T, iris='#2a2224'),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    longhair('front', length=106, flare=6, top=0) + [fringe([(12, 62), (16, 40), (30, 26), (50, 22), (70, 26), (84, 40), (88, 62), (78, 54), (70, 64, 1), (64, 52),
                                                             (54, 74, 1), (48, 54), (40, 66, 1), (34, 52), (24, 62, 1)])] + cheek_lines(86),
    longhair('side', length=106, flare=6) + [fringe([(66, 14), (88, 28), (92, 56, 1), (82, 46), (76, 58, 1), (70, 38)])],
    longhair('back', length=106, flare=6, ends=5))

# Sonny Welkin: cara ancha; pelo rojo corto con dos mechones enormes curvados hacia arriba como cuernos a los lados
add('sonny-welkin', 'normal', pal('#a82c08', SK_O, iris='#4a6a3a'),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 96, 'hairline': [(14, 60), (20, 46), (36, 40), (50, 48), (64, 40), (80, 46), (86, 60)],
     'face_front': blob([(14, 54), (50, 42), (86, 54), (90, 80), (78, 102), (50, 108), (22, 102), (10, 80)])},
    [L(outline([(16, 46), (2, 30), (-2, 6), (6, -14, 1), (8, 10), (20, 26), (28, 34)])), L(outline([(84, 46), (98, 30), (102, 6), (94, -14, 1), (92, 10), (80, 26), (72, 34)]))]
    + crop('front', top=4, side=60),
    [L(outline([(60, 30), (70, 14), (70, -6), (64, -20, 1), (60, 0), (50, 14), (46, 24)]))] + crop('side', top=4),
    [L(outline([(16, 46), (2, 30), (-2, 6), (6, -14, 1), (8, 10), (20, 26), (28, 34)])), L(outline([(84, 46), (98, 30), (102, 6), (94, -14, 1), (92, 10), (80, 26), (72, 34)]))]
    + crop('back', top=4))

# Spike Clutcher: hombre de pelo verde azulado en pinchos revueltos y una cicatriz en la barbilla
add('spike-clutcher', 'delgado', pal('#5a8a7e', SK_L, iris='#7a7068'),
    {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': [(14, 58), (22, 44), (36, 40), (50, 44), (64, 38), (78, 44), (86, 58)]},
    spiky('front', 31, amp=12, n=11, lo=62) + [L(quad((60, 96), (56, 102), (62, 108)), OUTC, 'f', False, False, 1.0), nose(51, 86, 4)],
    spiky('side', 31, amp=12, n=11), spiky('back', 31, amp=12, n=11))


def topknot(x=50, y=-2, r=7, c='mid'):
    return [L(curls(x, y, r, r * 0.9, 5, 0.3), c), strand([(x - r * 0.7, y + r * 0.9), (x + r * 0.7, y + r * 0.9)], 'deep', 'b', 1.4)]


def freckles(y=86, c=(200, 110, 70, 255)):
    return [L(ell(x, y + (i % 2) * 2, 0.8, 0.8), c, 'f', False) for i, x in enumerate((24, 28, 32, 68, 72, 76))]


WIDE = blob([(14, 54), (50, 42), (86, 54), (90, 80), (78, 102), (50, 108), (22, 102), (10, 80)])

# ------------------------------------------------------------------ hoja 4

# Spike Coiffs: pelo verde oliva en pinchos enormes y revueltos con un mechón que le tapa un ojo; tirita en la mejilla, ojos de punto
add('spike-coiffs', 'normal', pal('#72722c', SK_L, iris='#2a2224'),
    {'eyes': 'dot', 'brows': False, 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    spiky('front', 41, amp=18, n=10, rx=50, ry=42, lo=72)
    + [fringe([(14, 64, 1), (16, 44), (30, 30), (50, 26), (70, 30), (84, 44), (86, 64, 1), (76, 54), (66, 66, 1), (60, 52), (50, 62, 1), (44, 50), (38, 84, 1), (32, 56),
               (24, 60)]),
       L(blob([(64, 84), (72, 82), (73, 88), (65, 90)], 4), (236, 220, 200, 255), 'f', ln=True)],
    spiky('side', 41, amp=18, n=10, rx=50, ry=42) + [fringe([(66, 16), (88, 28), (94, 56, 1), (82, 46), (76, 60, 1), (70, 38)])],
    spiky('back', 41, amp=18, n=10, rx=50, ry=42))

# Spike Needle (portero): pelo amarillo en un cepillo altísimo y recto hacia arriba; sombra de ojos morada y un colmillo
EYESH = (150, 120, 190, 255)
add('spike-needle', 'delgado', pal('#dcba22', SK_L, iris='#2a2224'),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': [(14, 56), (24, 46), (40, 44), (50, 50), (60, 44), (76, 46), (86, 56)]},
    tall('front', [(14, -34), (26, -40), (38, -42), (50, -42), (62, -42), (74, -40), (86, -34)], base=50)
    + [L(quad((28, 70), (36, 66), (44, 71)), EYESH, 'f', False, False, 2.2), L(quad((72, 70), (64, 66), (56, 71)), EYESH, 'f', False, False, 2.2), fang(55, 94)],
    tall('side', [(10, -30), (28, -40), (48, -42), (66, -40), (82, -32)]),
    tall('back', [(14, -34), (26, -40), (38, -42), (50, -42), (62, -42), (74, -40), (86, -34)]))

# Spike Pitt: pelo naranja corto y ondulado en bultos; pecas
add('spike-pitt', 'normal', pal('#d2721e', SK_L, iris='#2a2224'),
    {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': [(14, 60), (20, 44), (34, 40), (50, 42), (66, 38), (80, 44), (86, 60)]},
    [L(curls(50, 28, 44, 26, 8, 0.2))] + crop('front', top=6, side=62, w=2) + freckles(86),
    [L(curls(46, 26, 42, 24, 8, 0.2))] + crop('side', top=6, w=2),
    [L(curls(50, 28, 44, 26, 8, 0.2))] + crop('back', top=6, w=2))

# Spike Thorne: pelo naranja en llamas altas de punta hacia arriba y picos a los lados; ojos verdes
add('spike-thorne', 'normal', pal('#d4721e', SK_L, iris='#2e9a5a'),
    {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': [(14, 60), (22, 46), (36, 42), (50, 46), (64, 42), (78, 46), (86, 60)]},
    tall('front', [(4, 24), (14, -8), (28, -26), (44, -34), (58, -30), (72, -24), (86, -6), (96, 24)], base=48)
    + [L(outline([(16, 60), (2, 84, 1), (14, 72), (14, 50)])), L(outline([(84, 60), (98, 84, 1), (86, 72), (86, 50)]))],
    tall('side', [(8, -4), (24, -24), (42, -32), (62, -28), (82, -10)]),
    tall('back', [(4, 24), (14, -8), (28, -26), (44, -34), (58, -30), (72, -24), (86, -6), (96, 24)]))

# Stan Dupp: grandullón de cara redonda; pelo gris parduzco en pinchos con los lados trenzados; ojos cerrados de risa y labios gruesos
add('stan-dupp', 'corpulento', pal('#968a68', SK_O, iris='#2a2224'),
    {'eyes': 'closed', 'brows': False, 'mouth': 'lips', 'mouth_y': 96, 'mouth_w': 8, 'hairline': [(14, 58), (22, 44), (36, 40), (50, 44), (64, 40), (78, 44), (86, 58)],
     'face_front': WIDE, 'nose': (50, 86, 4.0)},
    spiky('front', 51, amp=12, n=10, lo=60) + [strand([(14, 50), (14, 70)], 'deep', 'f', 1.0), strand([(86, 50), (86, 70)], 'deep', 'f', 1.0)],
    spiky('side', 51, amp=12, n=10) + [strand([(30, 50), (34, 70)], 'deep', 'b', 1.0), strand([(36, 50), (40, 70)], 'deep', 'b', 1.0)],
    spiky('back', 51, amp=12, n=10))

# Stan Trum: cara ancha, pelo verde oliva oscuro rapado al cepillo; párpados caídos y boca torcida
add('stan-trum', 'normal', pal('#44441e', SK_L, iris='#2a2224'),
    {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 97, 'hairline': (46, 34), 'face_front': WIDE, 'nose': (50, 86, 3.4)},
    crop('front', top=8, side=46, w=0, flat=10) + [L([(28, 72), (44, 72)], OUTC, 'f', False, False, 1.4), L([(56, 72), (72, 72)], OUTC, 'f', False, False, 1.4)],
    crop('side', top=8, flat=10), crop('back', top=8, flat=10))

# Steve Pinner (portero): pelo rubio corto al cepillo; una marca naranja de rayo cruzándole un ojo
add('steve-pinner', 'normal', pal('#dcbc66', SK_L, iris='#3a8a7a'),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': (50, 38)},
    crop('front', top=4, side=50, flat=6) + [L(outline([(30, 18), (34, 4, 1), (40, 14), (48, 2, 1), (54, 14), (62, 4, 1), (66, 16), (70, 22)])),
                                             L([(30, 60), (38, 72), (32, 76), (40, 90)], (220, 120, 40, 255), 'f', False, False, 2.0)],
    crop('side', top=4, flat=6), crop('back', top=4, flat=6))

# Stu Born (portero): pelo rosa salmón en pinchos revueltos con mechones largos que le enmarcan la cara; ojos lila
add('stu-born', 'normal', pal('#d27e72', SK_L, iris='#7a70a8'),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 94, 'hairline': False},
    spiky('front', 61, amp=16, n=10, lo=70) + [fringe([(14, 66), (16, 44), (30, 30), (50, 26), (70, 30), (84, 44), (86, 66), (80, 52), (72, 60, 1), (64, 46), (52, 58, 1),
                                                       (46, 46), (36, 58, 1), (30, 50), (20, 56)]),
                                               L(outline([(16, 52), (10, 90, 1), (20, 70), (22, 54)]), 'mid', 'f'), L(outline([(84, 52), (90, 90, 1), (80, 70), (78, 54)]), 'mid', 'f')],
    spiky('side', 61, amp=16, n=10) + [fringe([(66, 16), (88, 28), (94, 56, 1), (82, 46), (78, 76, 1), (70, 38)])],
    spiky('back', 61, amp=16, n=10))

# ------------------------------------------------------------------ hoja 5

# Stu Dent (portero): pelo azul marino morado en pinchos altos abiertos en V hacia los lados; piel morena y ojos redondos
add('stu-dent', 'normal', pal('#42385c', SK_O, iris='#2a2224'),
    {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    [L(outline([(16, 62), (8, 40), (-6, 6, 1), (16, 22), (22, -14, 1), (36, 12), (50, -6, 1), (60, 12), (80, -14, 1), (82, 20), (104, 8, 1), (92, 40), (84, 62), (50, 50)])),
     L(outline([(60, 12), (80, -14), (82, 20), (104, 8), (92, 40), (84, 60), (74, 34)]), 'shade', 'b', False),
     fringe([(14, 60), (18, 42), (34, 30), (50, 28), (66, 30), (82, 42), (86, 60), (76, 50), (68, 58, 1), (60, 46), (48, 60, 1), (42, 46), (30, 56, 1), (24, 50)])],
    [L(outline([(60, 56), (68, 44), (86, 40), (96, 20, 1), (80, 18), (84, -8, 1), (64, 8), (52, -14, 1), (40, 6), (14, 0, 1), (16, 20), (4, 36), (6, 60), (20, 74), (36, 70),
                (44, 58)])),
     L(outline([(6, 40), (30, 44), (40, 62), (32, 72), (18, 72)]), 'shade', 'b', False)],
    [L(outline([(16, 76), (8, 40), (-6, 6, 1), (16, 22), (22, -14, 1), (36, 12), (50, -6, 1), (60, 12), (80, -14, 1), (82, 20), (104, 8, 1), (92, 40), (84, 76), (50, 84)])),
     L(outline([(60, 12), (80, -14), (82, 20), (104, 8), (92, 40), (84, 76), (64, 82)]), 'shade', 'b', False)])

# Stu Helmsley (portero): casco verde con tres franjas crema y el borde crema, una cinta azul grisácea en la frente; piel
# oscura, una cicatriz en zigzag en la mejilla y morros
HG, HG_D, CREAM, BAND2 = (42, 102, 66, 255), (30, 78, 50, 255), (234, 222, 162, 255), (78, 114, 126, 255)
add('stu-helmsley', 'normal', pal('#3a4a70', SK_D, iris='#2a2224'),
    {'eyes': 'round', 'brows': False, 'mouth': 'lips', 'mouth_y': 96, 'mouth_w': 7, 'hairline': False},
    [L(outline([(6, 92), (2, 60), (8, 22), (26, 2), (50, -4), (74, 2), (92, 22), (98, 60), (94, 92), (84, 92), (84, 62), (50, 56), (16, 62), (16, 92)]), HG),
     L(outline([(64, 0), (90, 20), (98, 60), (94, 90), (86, 60), (78, 30)]), HG_D, 'b', False),
     L(outline([(26, 46), (24, 14), (32, 12), (34, 46)]), CREAM, 'b', False), L(outline([(46, 44), (46, 6), (54, 6), (54, 44)]), CREAM, 'b', False),
     L(outline([(66, 46), (68, 14), (76, 16), (74, 46)]), CREAM, 'b', False),
     L(outline([(6, 92), (2, 64), (12, 50), (16, 64), (14, 92)]), CREAM, 'f'), L(outline([(94, 92), (98, 64), (88, 50), (84, 64), (86, 92)]), CREAM, 'f'),
     L(outline([(14, 66), (16, 54), (50, 50), (84, 54), (86, 66), (50, 62)]), BAND2, 'f'),
     L([(64, 82), (70, 86), (66, 90), (72, 94)], OUTC, 'f', False, False, 1.2)],
    [L(outline([(62, 60), (66, 46), (84, 42), (96, 26), (84, 4), (50, -6), (20, 2), (2, 26), (0, 66), (8, 92), (30, 92), (44, 74), (54, 62)]), HG),
     L(outline([(30, 4), (36, 2), (40, 50), (32, 52)]), CREAM, 'b', False),
     L(outline([(62, 60), (66, 46), (90, 44), (92, 52), (70, 54), (66, 62)]), BAND2, 'f')],
    [L(outline([(6, 92), (2, 60), (8, 22), (26, 2), (50, -4), (74, 2), (92, 22), (98, 60), (94, 92), (50, 98)]), HG),
     L(outline([(64, 0), (90, 20), (98, 60), (94, 90), (70, 96)]), HG_D, 'b', False),
     L(outline([(26, 70), (24, 14), (32, 12), (34, 70)]), CREAM, 'b', False), L(outline([(46, 72), (46, 6), (54, 6), (54, 72)]), CREAM, 'b', False),
     L(outline([(66, 70), (68, 14), (76, 16), (74, 70)]), CREAM, 'b', False),
     L(outline([(6, 92), (50, 98), (94, 92), (94, 98), (50, 104), (6, 98)]), CREAM, 'f')])

# Stu Lucky-Perstitious: rastas castaño oliva con cuentas naranjas y amarillas hasta los hombros; lágrimas pintadas turquesa y
# labios rojos
BEAD1, BEAD2, TEAR = (210, 90, 40, 255), (230, 190, 50, 255), (90, 200, 210, 255)
locks_f = []
for x0, x1, y1 in ((18, 10, 104), (12, 2, 92), (82, 90, 104), (88, 98, 92)):
    locks_f.append(L(rope((x0, 50), ((x0 + x1) / 2, 76), (x1, y1), 8)))
add('stu-lucky-perstitious', 'normal', pal('#5a4e2c', SK_T, iris='#2a2224', bead=BEAD1, bead2=BEAD2),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'lips', 'mouth_y': 96, 'mouth_w': 8, 'hairline': (54, 36)},
    locks_f + crop('front', top=2, side=56, w=2) + [strand([(x, 6), (x + (x - 50) * 0.4, 40)], 'deep', 'b', 1.0) for x in (36, 44, 56, 64)]
    + [L(ell(x, y, 2.6, 2.6), c, 'f') for x, y, c in ((14, 64, BEAD1), (8, 76, BEAD2), (86, 64, BEAD1), (92, 76, BEAD2), (12, 90, BEAD1), (88, 90, BEAD1))]
    + [L(blob([(30, 82), (34, 82), (32, 92)], 4), TEAR, 'f'), L(blob([(66, 82), (70, 82), (68, 92)], 4), TEAR, 'f')],
    crop('side', top=2, nape=90, w=2) + [L(rope((x, 50), (x - 4, 76), (x - 2, 100), 8)) for x in (10, 22, 34)]
    + [L(ell(x - 3, 72, 2.6, 2.6), BEAD1, 'f') for x in (10, 22, 34)],
    crop('back', top=2, nape=84, w=2) + [L(rope((x, 50), (x + (x - 50) * 0.1, 76), (x, 102), 8), 'mid', 'f') for x in (14, 30, 50, 70, 86)]
    + [L(ell(x, 74, 2.6, 2.6), BEAD1 if i % 2 else BEAD2, 'f') for i, x in enumerate((14, 30, 50, 70, 86))])

# Stu Shiner (portero): pelo caoba en casco con un flequillo largo abierto en medio que le tapa las cejas; ojos rosa
add('stu-shiner', 'normal', pal('#ae4410', SK_L, iris='#d88a8a'),
    {'eyes': 'normal', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'hairline': False},
    bob('front', lo=74, top=2, flare=2) + [fringe([(10, 70), (12, 40), (26, 18), (50, 10), (74, 18), (88, 40), (90, 70), (80, 62), (66, 66, 1), (58, 52), (52, 40), (48, 40),
                                                   (42, 52), (34, 66, 1), (20, 62)]),
                                           strand([(50, 10), (40, 40)], 'shade', 'f', 1.0), strand([(50, 10), (64, 44)], 'shade', 'f', 1.0)],
    bob('side', lo=74, top=2, flare=2) + [fringe([(66, 14), (88, 26), (94, 56, 1), (84, 52), (76, 40)])],
    bob('back', lo=80, top=2, flare=2))

# Stu Venier: pelo gris morado en trenzas pegadas enrolladas, con una trenza larga que le cuelga por un lado hasta el pecho
add('stu-venier', 'normal', pal('#7e7280', SK_L, iris='#2a2224'),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': (54, 34)},
    [L(rope((18, 60), (6, 90), (14, 124), 8))] + crop('front', top=0, side=56, w=2)
    + [strand([(16 + i * 9, 50 - abs(4 - i) * 2), (20 + i * 8, 6 + abs(4 - i) * 3)], 'deep', 'b', 1.0) for i in range(8)]
    + [strand([(10, 70 + i * 8), (16, 72 + i * 8)], 'deep', 'b', 1.0) for i in range(6)],
    crop('side', top=0, w=2) + [strand([(14 + i * 10, 74 - i * 6), (40 + i * 8, 6 + i * 4)], 'deep', 'b', 1.0) for i in range(5)],
    crop('back', top=0, w=2) + [strand([(14 + i * 10, 70), (20 + i * 9, 8)], 'deep', 'b', 1.0) for i in range(8)] + [L(rope((20, 60), (12, 90), (18, 124), 8), 'mid', 'f')])

# Sul Tarner: pinchos azul marino por detrás y un flequillo rosa malva peinado de lado por delante; nariz redonda
PINK = (188, 164, 164, 255)
add('sul-tarner', 'normal', pal('#364e68', SK_T, iris='#2a2224', pink=PINK, pink_d=(150, 126, 128, 255), nose=(220, 150, 110, 255)),
    {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False, 'nose': (50, 85, 4)},
    spiky('front', 71, amp=14, n=10, lo=72) + [fringe([(14, 60), (14, 40), (26, 24), (48, 16), (72, 20), (86, 36), (88, 56), (76, 46), (60, 42), (42, 44), (24, 52)], 'pink'),
                                               strand([(30, 30), (60, 26), (84, 40)], 'pink_d', 'f', 1.2)],
    spiky('side', 71, amp=14, n=10) + [fringe([(54, 6), (82, 16), (94, 40), (88, 50), (74, 36), (58, 28)], 'pink')],
    spiky('back', 71, amp=14, n=10))

# Sylver Stone: hombre de frente alta; pelo verde grisáceo en pinchos salvajes y abultados; cejas verdosas
add('sylver-stone', 'delgado', pal('#5c7268', SK_T, iris='#2a2224'),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': [(14, 54), (22, 40), (36, 34), (50, 38), (64, 34), (78, 40), (86, 54)]},
    spiky('front', 81, amp=20, n=12, rx=52, ry=42, lo=58) + [nose(50, 86, 4)],
    spiky('side', 81, amp=20, n=12, rx=52, ry=42), spiky('back', 81, amp=20, n=12, rx=52, ry=42))

# Tabor Drummond (portero): pelo rubio crema en cepillo plano con dos picos altos en las esquinas y los lados castaños rapados;
# dos círculos verdes pintados alrededor de los ojos y nariz naranja
GREEN_P = (110, 150, 70, 255)
add('tabor-drummond', 'normal', pal('#e8dca4', SK_L, iris='#2a2224', side='#ba8a66', nose=(226, 130, 60, 255)),
    {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 96, 'hairline': (52, 40), 'face_front': WIDE, 'nose': (50, 86, 3.6)},
    [L(outline([(16, 62), (12, 40), (16, 22), (84, 22), (88, 40), (84, 62), (50, 54)]), 'side'),
     L(outline([(16, 30), (10, -12, 1), (30, 10), (50, 14), (70, 10), (90, -12, 1), (84, 30), (50, 34)])),
     L(outline([(60, 12), (90, -12), (84, 30), (66, 32)]), 'shade', 'b', False),
     L(ell(36, 75, 10, 8.4), GREEN_P, 'f'), L(ell(64, 75, 10, 8.4), GREEN_P, 'f')]
    + [l for x in (36, 64) for l in (L(ell(x, 75, 4.4, 4.4), OUTC, 'f'), L(ell(x, 75.5, 3.4, 3.4), WHITE, 'f'), L(ell(x, 76, 2.4, 2.4), BLACK, 'f'),
                                     L([(x - 5, 72), (x + 5, 72)], OUTC, 'f', False, False, 1.6))],
    [L(outline([(60, 54), (66, 42), (84, 38), (86, 20), (40, 18), (8, 26), (4, 52), (14, 74), (32, 76), (44, 60)]), 'side'),
     L(outline([(84, 26), (90, -12, 1), (70, 12), (40, 12), (10, 4, 1), (10, 30), (50, 32)])), L(ell(80, 75, 7, 8.4), GREEN_P, 'f'), L(ell(82, 75.5, 3, 3.2), WHITE, 'f', ln=True), L(ell(83, 76, 2, 2.2), BLACK, 'f')],
    [L(outline([(16, 76), (12, 40), (16, 22), (84, 22), (88, 40), (84, 76), (50, 84)]), 'side'),
     L(outline([(16, 30), (10, -12, 1), (30, 10), (50, 14), (70, 10), (90, -12, 1), (84, 30), (50, 34)]))])


# ------------------------------------------------------------------ hoja 6

# Tad Trinket: pelo morado oscuro en pinchos grandes y revueltos, con picos en la nuca; ojos naranjas
add('tad-trinket', 'normal', pal('#5a4468', SK_L, iris='#d2782a'),
    {'eyes': 'normal', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': False},
    spiky('front', 91, amp=16, n=10, lo=70) + [fringe([(14, 64, 1), (16, 44), (30, 30), (50, 26), (70, 30), (84, 44), (86, 64, 1), (76, 54), (66, 64, 1), (60, 50),
                                                       (50, 62, 1), (44, 50), (34, 64, 1), (28, 52)]),
                                               L(outline([(16, 66), (8, 90, 1), (20, 74)]), 'mid', 'b'), L(outline([(84, 66), (92, 90, 1), (80, 74)]), 'mid', 'b')],
    spiky('side', 91, amp=16, n=10) + [fringe([(66, 16), (88, 28), (94, 56, 1), (82, 46), (76, 58, 1), (70, 38)])],
    spiky('back', 91, amp=16, n=10))

# Taka Tanaka: pelo castaño oliva rapado al cepillo con una estrella afeitada; párpados caídos y media sonrisa
add('taka-tanaka', 'normal', pal('#968044', SK_L, iris='#2a2224'),
    {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 93, 'hairline': (50, 38)},
    crop('front', top=4, side=50, flat=4) + [L(outline([(30, 16), (34, 22, 1), (42, 22, 1), (36, 27, 1), (38, 35, 1), (31, 30, 1), (24, 35, 1), (26, 27, 1), (20, 22, 1),
                                                        (28, 22, 1)]), 'deep', 'b', False)]
    + brows(64, 'shade', 3.6, tilt=-0.4),
    crop('side', top=4, flat=4) + brow_side(64, 'shade', 3.6), crop('back', top=4, flat=4))

# Teagen Brewer: cara ancha de piel morena y nariz grande; melena lisa blanca crema hasta la barbilla con flequillo en medio; sonrisa
add('teagen-brewer', 'normal', pal('#d6d4b2', SK_T, iris='#2a2224'),
    {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': False, 'face_front': WIDE},
    longhair('front', length=104, flare=2, top=0) + [fringe([(20, 56), (22, 36), (36, 24), (50, 22), (64, 24), (78, 36), (80, 56), (70, 46), (58, 50), (50, 60, 1), (42, 50),
                                                             (30, 46)]),
                                                     L(quad((38, 95), (50, 101), (62, 95)), OUTC, 'f', False, False, 1.4), nose(50, 86, 5)],
    longhair('side', length=104, flare=2) + [fringe([(66, 14), (88, 28), (90, 50, 1), (78, 44)])],
    longhair('back', length=104, flare=2, ends=5))

# Ted Fast (portero): trenzas pegadas azul marino que acaban en cinco moños por arriba y los lados; ojos turquesa y una boca
# naranja enorme
add('ted-fast', 'normal', pal('#364e68', SK_T, iris='#4aa0a0'),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'none', 'hairline': (56, 38)},
    [L(curls(x, y, 9, 9, 5, 0.4)) for x, y in ((12, 44), (22, 10), (50, -2), (78, 10), (88, 44))] + crop('front', top=4, side=58)
    + [strand([(x, 8), (x + (x - 50) * 0.4, 42)], 'deep', 'b', 1.0) for x in (32, 42, 50, 58, 68)]
    + [L(blob([(38, 92), (50, 89), (62, 92), (58, 98), (50, 99), (42, 98)], 6), ORANGE_MOUTH, 'f', ln=True), L(quad((40, 94), (50, 96), (60, 94)), OUTC, 'f', False, False, 1.0)],
    [L(curls(x, y, 9, 9, 5, 0.4)) for x, y in ((8, 50), (16, 18), (44, 0))] + crop('side', top=4),
    [L(curls(x, y, 9, 9, 5, 0.4)) for x, y in ((12, 46), (22, 12), (50, 0), (78, 12), (88, 46))] + crop('back', top=4)
    + [strand([(x, 8), (x + (x - 50) * 0.2, 76)], 'deep', 'b', 1.0) for x in (30, 40, 50, 60, 70)])

# Ted Larkin: flaco de piel pálida grisácea; melena lisa castaño malva que le tapa un ojo, ojo caído con ojeras
add('ted-larkin', 'delgado', pal('#a28074', '#e4d8c4', iris='#4a7a7a'),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False},
    longhair('front', length=104, flare=2, top=0) + [fringe([(10, 66), (12, 40), (24, 20), (48, 12), (62, 18), (60, 30), (56, 56), (52, 92, 1), (42, 70), (34, 60), (22, 60)]),
                                                     strand([(40, 16), (46, 60)], 'shade', 'f', 1.0), L(quad((56, 80), (64, 84), (72, 80)), (120, 140, 140, 255), 'f', False, False, 1.2)],
    longhair('side', length=104, flare=2) + [fringe([(60, 6), (86, 20), (92, 60, 1), (80, 50), (72, 30)])],
    longhair('back', length=104, flare=2, ends=4))

# Teddy Kodiak: grandullón de cara ancha; moño azul marino en lo alto y los lados rapados
add('teddy-kodiak', 'corpulento', pal('#364e68', SK_L, iris='#2a2224', scalp=(200, 168, 140, 255)),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 96, 'hairline': (46, 32), 'face_front': WIDE},
    [L(outline([(16, 52), (14, 34), (24, 18), (76, 18), (86, 34), (84, 52), (50, 46)]), 'scalp')]
    + [L(outline([(26, 26), (28, 10), (50, 4), (72, 10), (74, 26), (50, 22)]))] + topknot(52, -4, 8)
    + [L(outline([(44, -10), (56, -18, 1), (60, -6)]))],
    [L(outline([(60, 50), (66, 40), (84, 34), (84, 18), (40, 14), (10, 24), (4, 48), (12, 70), (30, 74), (44, 58)]), 'scalp'),
     L(outline([(40, 22), (44, 8), (70, 6), (76, 22), (58, 26)]))] + topknot(56, -4, 8),
    [L(outline([(16, 74), (14, 34), (24, 18), (76, 18), (86, 34), (84, 74), (50, 82)]), 'scalp'),
     L(outline([(26, 26), (28, 10), (50, 4), (72, 10), (74, 26), (50, 30)]))] + topknot(50, -4, 8))

# Tel Egram: pelo rosa malva en pinchos grandes que salen hacia los lados; ojos negros grandes y nariz redonda
add('tel-egram', 'normal', pal('#bca4a4', SK_L, iris='#1a1416'),
    {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': False, 'nose': (50, 86, 3.6), 'eye_sep': 15},
    [L(outline([(16, 60), (-8, 46, 1), (8, 30), (-6, 10, 1), (16, 12), (20, -12, 1), (36, 4), (54, -16, 1), (62, 4), (84, -8, 1), (84, 14), (106, 22, 1), (92, 36),
                (100, 54, 1), (84, 60), (50, 50)])),
     L(outline([(62, 4), (84, -8), (84, 14), (106, 22), (92, 36), (100, 54), (84, 58), (74, 30)]), 'shade', 'b', False),
     fringe([(14, 62), (18, 42), (34, 30), (50, 28), (66, 30), (82, 42), (86, 62), (76, 50), (66, 60, 1), (60, 46), (50, 58, 1), (44, 46), (32, 60, 1), (26, 50)]),
     L(outline([(16, 74), (2, 82, 1), (14, 66)]), 'mid', 'b'), L(outline([(84, 74), (98, 82, 1), (86, 66)]), 'mid', 'b')],
    [L(outline([(60, 54), (68, 44), (86, 40), (100, 24, 1), (84, 20), (86, -6, 1), (66, 6), (54, -16, 1), (40, 4), (14, -6, 1), (18, 16), (-6, 24, 1), (6, 40), (-2, 62, 1),
                (12, 66), (26, 82, 1), (34, 68), (46, 58)])),
     L(outline([(6, 40), (30, 44), (40, 62), (34, 68), (12, 66)]), 'shade', 'b', False)],
    [L(outline([(16, 76), (-8, 50, 1), (8, 34), (-6, 10, 1), (16, 12), (20, -12, 1), (36, 4), (54, -16, 1), (62, 4), (84, -8, 1), (84, 14), (106, 22, 1), (92, 38),
                (108, 52, 1), (84, 76), (50, 84)])),
     L(outline([(62, 4), (84, -8), (84, 14), (106, 22), (92, 38), (108, 52), (84, 76), (64, 82)]), 'shade', 'b', False)])

# Teller Scoap (portero): pelo rosa rojizo corto en pinchos; ojos redondos muy abiertos y rayitas en las mejillas
add('teller-scoap', 'normal', pal('#c87068', SK_T, iris='#2a2224'),
    {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 93, 'hairline': [(14, 58), (22, 44), (36, 40), (50, 44), (64, 40), (78, 44), (86, 58)],
     'nose': (50, 85, 2.6)},
    spiky('front', 101, amp=10, n=11, lo=62) + cheek_lines(86),
    spiky('side', 101, amp=10, n=11), spiky('back', 101, amp=10, n=11))


# ------------------------------------------------------------------ hoja 7

# Telly Fonbocks: una nube de pelo azul verdoso en bultos grandes que baja por los lados; dos triángulos amarillos en las mejillas
YEL = (226, 190, 50, 255)
add('telly-fonbocks', 'normal', pal('#669898', SK_L, iris='#2a2224'),
    {'eyes': 'round', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 95, 'hairline': [(14, 64), (20, 48), (36, 44), (50, 50), (64, 44), (80, 48), (86, 64)]},
    [L(curls(12, 72, 10, 14, 5, 0.3)), L(curls(88, 72, 10, 14, 5, 0.6)), L(curls(50, 28, 52, 34, 8, 0.2)),
     L(curls(74, 22, 10, 10, 5), 'shade', 'b', False), nose(50, 86, 4),
     L([(24, 82), (34, 82), (29, 90)], YEL, 'f', ln=True), L([(66, 82), (76, 82), (71, 90)], YEL, 'f', ln=True)],
    [L(curls(26, 70, 18, 18, 6)), L(curls(46, 28, 48, 32, 8, 0.2))],
    [L(curls(50, 66, 38, 22, 7, 0.3)), L(curls(50, 30, 52, 34, 8, 0.2)), L(curls(74, 50, 10, 12, 5), 'shade', 'b', False)])

# Terrence Anthem: gorra roja con la copa rosa y un corazón rojo, pelo morado por debajo; gafas redondas de cristal turquesa
CAPR, CAPP, HEART, LENS2 = (196, 52, 40, 255), (232, 160, 150, 255), (190, 36, 30, 255), (120, 170, 180, 255)
add('terrence-anthem', 'normal', pal('#7a6a96', SK_P, iris='#2a2224'),
    {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 95, 'hairline': False, 'nose': (50, 86, 3.4)},
    [L(outline([(16, 70), (8, 84, 1), (12, 60), (88, 60), (92, 84, 1), (84, 70), (50, 60)])),
     L(outline([(14, 52), (14, 30), (26, 6), (50, -4), (74, 6), (86, 30), (86, 52)]), CAPP),
     L(blob([(50, 30), (40, 16), (46, 12), (50, 18), (54, 12), (60, 16)], 6), HEART, 'b', False),
     L(outline([(4, 60), (6, 48), (50, 40), (94, 48), (96, 60), (50, 58)]), CAPR, 'f'),
     L(outline([(10, 52), (12, 40), (50, 32), (88, 40), (90, 52), (50, 46)]), CAPR, 'f')]
    + [L(ell(cx, 76, 9, 8), LENS2, 'f')for cx in (36, 64)] + ring_glasses('front', 76, (70, 110, 120, 255), 2.2, 9, 8),
    [L(outline([(10, 70), (2, 84, 1), (8, 56), (40, 56), (34, 72)])),
     L(outline([(10, 52), (16, 24), (40, 4), (66, 6), (84, 26), (84, 50)]), CAPP),
     L(outline([(4, 56), (8, 44), (60, 40), (104, 46), (106, 54), (60, 54)]), CAPR, 'f'), L(ell(82, 76, 5, 8), LENS2, 'f')] + ring_glasses('side', 76, (70, 110, 120, 255), 2.2, 9, 8),
    [L(outline([(14, 80), (8, 90, 1), (12, 60), (88, 60), (92, 90, 1), (86, 80), (50, 86)])),
     L(outline([(14, 54), (14, 30), (26, 6), (50, -4), (74, 6), (86, 30), (86, 54)]), CAPP),
     L(outline([(10, 62), (12, 48), (50, 42), (88, 48), (90, 62), (50, 56)]), CAPR, 'f'),
     L(outline([(40, 58), (60, 58), (58, 64), (42, 64)]), CAPP, 'f', False)])

# Terry Orr: grandullón de nariz de cerdo y un colmillo; pelo marrón en dos orejas largas que le caen a los lados y un tupé
# naranja de puntas arriba
FLAP = '#8a5a2c'
add('terry-orr', 'corpulento', pal('#ae4410', SK_O, iris='#2a2224', flap=FLAP, flap_d='#6a4220', nose=(140, 90, 60, 255)),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 97, 'hairline': (48, 36), 'face_front': WIDE, 'nose': (50, 86, 5)},
    [L(outline([(18, 34), (4, 50), (-2, 90), (10, 98), (22, 80), (26, 50)]), 'flap'), L(outline([(82, 34), (96, 50), (102, 90), (90, 98), (78, 80), (74, 50)]), 'flap'),
     L(outline([(18, 50), (14, 30), (24, 14), (50, 8), (76, 14), (86, 30), (82, 50), (50, 42)]), 'flap'),
     L(outline([(26, 30), (16, 18, 1), (32, 14), (30, 0, 1), (44, 8), (52, -6, 1), (58, 8), (72, 0, 1), (68, 14), (86, 18, 1), (74, 30), (50, 26)])),
     L(outline([(56, 8), (72, 0), (68, 14), (86, 18), (74, 30), (62, 26)]), 'shade', 'b', False),
     L([(60, 94), (63, 89), (65, 95)], WHITE, 'f', ln=True), L(quad((36, 96), (50, 98), (64, 95)), OUTC, 'f', False, False, 1.6)],
    [L(outline([(36, 34), (24, 50), (20, 92), (32, 98), (42, 80), (44, 50)]), 'flap'),
     L(outline([(60, 50), (66, 40), (84, 34), (84, 18), (50, 8), (14, 18), (4, 46), (14, 68), (30, 72), (44, 56)]), 'flap'),
     L(outline([(40, 22), (30, 4, 1), (48, 8), (56, -6, 1), (64, 8), (82, 4, 1), (78, 20), (60, 26)]))],
    [L(outline([(16, 34), (2, 50), (-2, 90), (10, 98), (22, 80), (26, 50)]), 'flap'), L(outline([(84, 34), (98, 50), (102, 90), (90, 98), (78, 80), (74, 50)]), 'flap'),
     L(outline([(16, 76), (14, 30), (24, 14), (50, 8), (76, 14), (86, 30), (84, 76), (50, 84)]), 'flap'),
     L(outline([(26, 30), (16, 18, 1), (32, 14), (30, 0, 1), (44, 8), (52, -6, 1), (58, 8), (72, 0, 1), (68, 14), (86, 18, 1), (74, 30), (50, 34)]))])

# Tex Curvator: grandullón de cara ancha; cresta alta gris parduzca sobre la cabeza rapada; cejas gruesas
add('tex-curvator', 'corpulento', pal('#968a72', SK_L, iris='#2a2224', scalp=(212, 176, 140, 255)),
    {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 96, 'hairline': (44, 30), 'face_front': WIDE, 'nose': (50, 85, 3)},
    [L(outline([(16, 54), (14, 34), (24, 18), (76, 18), (86, 34), (84, 54), (50, 46)]), 'scalp'),
     L(outline([(42, 30), (40, 4), (46, -16), (56, -28, 1), (58, -6), (58, 30)])), L(outline([(52, -20), (56, -28), (58, -6), (58, 28), (54, 20)]), 'shade', 'b', False)]
    + brows(64, 'mid', 4.6, tilt=1.2, w=13),
    [L(outline([(60, 50), (66, 40), (84, 34), (84, 18), (40, 12), (10, 24), (4, 48), (12, 70), (30, 74), (44, 58)]), 'scalp'),
     L(outline([(70, 18), (66, 2), (54, -10), (30, -14), (14, -26, 1), (20, -6), (10, 10), (14, 22), (40, 14)]))] + brow_side(64, 'mid', 4.6, 1.2),
    [L(outline([(16, 76), (14, 34), (24, 18), (76, 18), (86, 34), (84, 76), (50, 84)]), 'scalp'),
     L(outline([(42, 60), (40, 4), (46, -14), (56, -24, 1), (58, -6), (58, 60), (50, 66)]))])

# Tex Tingle (portero): pelo castaño malva en un tupé enorme peinado hacia la derecha; ojos verdes grandes
add('tex-tingle', 'normal', pal('#a28074', SK_L, iris='#3aa06a'),
    {'eyes': 'big', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 95, 'hairline': False},
    [L(outline([(16, 66), (10, 40), (4, 4), (30, -6), (70, -6), (100, 6, 1), (90, 26), (88, 50), (86, 66), (80, 50), (20, 50)])),
     L(outline([(60, -4), (100, 6), (90, 26), (88, 50), (84, 62), (78, 36)]), 'shade', 'b', False),
     fringe([(14, 56), (14, 36), (30, 20), (60, 14), (90, 20), (86, 40), (72, 34), (66, 52, 1), (60, 36), (46, 40), (40, 60, 1), (34, 42), (24, 46)]),
     strand([(20, 10), (60, 20), (88, 14)], 'shade', 'b', 1.2), L(outline([(84, 64), (94, 74, 1), (82, 70)]), 'mid', 'b')],
    [L(outline([(60, 54), (68, 44), (86, 40), (96, 28), (110, 8, 1), (84, 0), (50, -8), (20, 0), (6, 24), (4, 54), (16, 72), (32, 72), (44, 60)])),
     L(outline([(6, 40), (30, 44), (40, 62), (32, 72), (16, 72)]), 'shade', 'b', False)],
    [L(outline([(16, 76), (10, 40), (4, 4), (30, -6), (70, -6), (100, 6, 1), (90, 30), (86, 76), (50, 84)])),
     L(outline([(60, -4), (100, 6), (90, 30), (86, 76), (64, 82)]), 'shade', 'b', False)])

# Theo Bernoulli: piel morena y pelo amarillo pálido corto en mechones de punta, con un pelillo arriba
add('theo-bernoulli', 'normal', pal('#d6d49a', SK_T, iris='#2a2224'),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 94, 'hairline': False},
    crop('front', top=2, side=62, w=2) + [fringe([(14, 62), (16, 40), (30, 26), (50, 22), (70, 26), (84, 40), (86, 62), (78, 52), (70, 60, 1), (64, 48), (56, 58, 1),
                                                  (50, 46), (42, 58, 1), (36, 48), (28, 58, 1), (22, 50)]),
                                          L(quad((50, 4), (46, -8), (54, -12)), 'mid', 'b', False, False, 2.0)] + cheek_lines(84),
    crop('side', top=2, w=2) + [fringe([(66, 14), (88, 28), (92, 54, 1), (80, 44)])], crop('back', top=2, w=2))

# Theo Broma: hombre de cara larga y labios gruesos; gorro de lana alto a rayas verdes y amarillas (rasta); párpados caídos
RG, RY = (42, 102, 66, 255), (220, 190, 40, 255)
add('theo-broma', 'delgado', pal('#3a2a20', SK_T, iris='#2a2224'),
    {'eyes': 'round', 'brows': 'angry', 'mouth': 'lips', 'mouth_y': 98, 'mouth_w': 8, 'hairline': False,
     'face_front': blob([(18, 52), (50, 42), (82, 52), (84, 80), (72, 104), (50, 112), (28, 104), (16, 80)])},
    [L(outline([(8, 60), (4, 30), (14, 4), (50, -14), (86, 4), (96, 30), (92, 60), (50, 56)]), RG),
     L(outline([(6, 44), (8, 30), (50, 16), (92, 30), (94, 44), (50, 32)]), RY, 'b', False),
     L(outline([(16, 12), (50, 0), (84, 12), (70, 6), (50, 4), (30, 6)]), RY, 'b', False),
     L(outline([(10, 62), (10, 50), (50, 44), (90, 50), (90, 62), (50, 56)]), RG, 'f'), nose(50, 88, 5)],
    [L(outline([(60, 56), (64, 44), (86, 40), (92, 20), (70, 0), (40, -14), (10, -6), (-2, 24), (2, 56), (20, 66), (44, 60)]), RG),
     L(outline([(0, 36), (20, 16), (60, 14), (90, 26), (90, 34), (60, 26), (20, 30)]), RY, 'b', False)],
    [L(outline([(8, 64), (4, 30), (14, 4), (50, -14), (86, 4), (96, 30), (92, 64), (50, 72)]), RG),
     L(outline([(6, 46), (8, 32), (50, 18), (92, 32), (94, 46), (50, 36)]), RY, 'b', False),
     L(outline([(16, 12), (50, 0), (84, 12), (70, 6), (50, 4), (30, 6)]), RY, 'b', False)])

# Theo Riser: piel clara y pelo verde oscuro peinado hacia atrás con un rizo que sale por detrás; ojos pequeños con pestañas
add('theo-riser', 'normal', pal('#2c5a44', SK_L, iris='#2a2224'),
    {'eyes': 'round', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 96, 'hairline': [(14, 58), (20, 44), (34, 36), (50, 34), (66, 36), (80, 44), (86, 58)]},
    crop('front', top=0, side=60) + [strand([(30, 34), (40, 8)], 'deep', 'b', 1.0), strand([(50, 32), (50, 2)], 'deep', 'b', 1.0), strand([(70, 34), (62, 8)], 'deep', 'b', 1.0),
                                     L(outline([(80, 30), (94, 34), (100, 50, 1), (90, 44), (84, 40)]))],
    crop('side', top=0) + [L(outline([(10, 30), (-8, 36), (-14, 54, 1), (-4, 48), (6, 46)])), strand([(80, 30), (40, 14), (10, 30)], 'deep', 'b', 1.0)],
    crop('back', top=0) + [L(outline([(80, 30), (98, 32), (106, 50, 1), (94, 44), (86, 44)]))])


# ------------------------------------------------------------------ hoja 8

# Thomas Cott (portero): pelo azul marino recogido en un moño alto envuelto en una tela crema; ojos grandes
add('thomas-cott', 'normal', pal('#364e68', SK_T, iris='#1a1416', wrap=(234, 226, 172, 255), wrap_d=(206, 196, 140, 255)),
    {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 92, 'hairline': [(14, 60), (20, 44), (34, 36), (50, 40), (66, 36), (80, 44), (86, 60)]},
    [L(curls(50, -6, 14, 10, 6, 0.3), 'wrap'), L(outline([(32, 2), (36, -2), (64, -2), (68, 2), (64, 6), (36, 6)]), 'wrap_d')]
    + crop('front', top=2, side=62) + [strand([(50, 4), (36, 30)], 'deep', 'b', 1.0), strand([(50, 4), (64, 30)], 'deep', 'b', 1.0)] + cheek_lines(84),
    [L(curls(44, -6, 12, 10, 6, 0.3), 'wrap')] + crop('side', top=2),
    [L(curls(50, -6, 14, 10, 6, 0.3), 'wrap')] + crop('back', top=2))

# Thomas Ediston: cara ancha de piel morena y nariz gorda redonda; pelo castaño oliva en trenzas pegadas peinadas hacia atrás
add('thomas-ediston', 'normal', pal('#968044', SK_T, iris='#2a2224', nose=(170, 100, 60, 255)),
    {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 96, 'hairline': (60, 32), 'face_front': WIDE, 'nose': (50, 86, 5)},
    crop('front', top=4, side=64) + [strand([(x, 8), (x + (x - 50) * 0.5, 50)], 'deep', 'b', 1.0) for x in (30, 40, 50, 60, 70)],
    crop('side', top=4) + [strand([(80, 28), (50, 10), (16, 30)], 'deep', 'b', 1.0), strand([(70, 40), (40, 24), (10, 50)], 'deep', 'b', 1.0)],
    crop('back', top=4) + [strand([(x, 8), (x + (x - 50) * 0.3, 80)], 'deep', 'b', 1.0) for x in (30, 40, 50, 60, 70)])

# Thor Toise: gordo de cara redonda; pelo rubio estirado hacia atrás con un moñito arriba y puntas a los lados; sonrisa de dientes
add('thor-toise', 'corpulento', pal('#dcbc66', SK_L, iris='#2a2224'),
    {'eyes': 'closed', 'brows': False, 'mouth': 'grin', 'mouth_y': 95, 'hairline': (50, 34), 'face_front': WIDE},
    [L(outline([(42, 16), (40, 0), (48, -10), (54, -16, 1), (58, -4), (58, 16)]))]
    + crop('front', top=6, side=52, w=4) + [L(outline([(14, 50), (0, 40, 1), (12, 36)])), L(outline([(86, 50), (100, 40, 1), (88, 36)])),
                                             strand([(50, 8), (30, 30)], 'deep', 'b', 1.0), strand([(50, 8), (70, 30)], 'deep', 'b', 1.0)],
    [L(outline([(36, 14), (34, -2), (42, -12), (48, -18, 1), (52, -4), (52, 14)]))] + crop('side', top=6, w=4),
    [L(outline([(42, 16), (40, 0), (48, -10), (54, -16, 1), (58, -4), (58, 16)]))] + crop('back', top=6, w=4)
    + [L(outline([(14, 50), (0, 40, 1), (12, 36)])), L(outline([(86, 50), (100, 40, 1), (88, 36)]))])
