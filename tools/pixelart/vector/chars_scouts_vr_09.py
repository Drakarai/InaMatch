"""Ojeadores de Victory Road (scouts-vr), tanda 09: dibujados a partir de su retrato; claves 'scouts-vr:<id>'.

El frente sale del retrato y el perfil y la espalda se deducen de cómo cae ese peinado (Terrell Brightley, Verity Billows
y Zayn Pinegrove, con su modelo 3D). La masa de pelo es dome() de la tanda 09 de IE1; aquí van las coletas, moños,
cintas y gafas de esta tanda."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401
from chars_scouts_ie1_09 import _c, dome, face, face_side, hl, mark

WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)
LT, MD, TN, DK = '#f8dcc4', '#f4c8a4', '#d89c70', '#9a6440'  # pieles: clara, media, tostada, morena


def F(**k):
    d = {'eyes': 'normal', 'mouth': 'line'}
    d.update(k)
    return d


def P(hair, skin, iris='#302232', **k):
    return pal(hair, skin, iris, **k)


def C(pid, body, palette, f, front, side, back):
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        # el nacimiento del pelo baja por el borde de la cara: así su raya no cruza el pelo de los lados
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[f'scouts-vr:{pid}'] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def H(views=('front', 'side', 'back'), **k):
    """La masa de pelo en las tres vistas con los mismos parámetros."""
    return [dome(v, **k) for v in views]


def mid(side=62, top=46, dip=50, x0=16, x1=84):
    """Raya en medio: el pelo se abre en dos cortinas desde el centro."""
    return [(x0 - 10, side), (x0, side - 6), (34, top + 2), (50, dip), (66, top + 2), (x1, side - 6), (x1 + 10, side)]


def fringe(y=56, side=64):
    """Flequillo recto."""
    return [(6, side), (16, y), (84, y), (94, side)]


def swept(y0=48, y1=60, side=64, right=True):
    """Flequillo echado a un lado: alto en un lado y bajo en el otro."""
    a, b = (y0, y1) if right else (y1, y0)
    return [(6, side), (16, a), (50, (a + b) / 2), (84, b), (94, side)]


def tails(view, c='mid', y=40, low=104, w=11, out=12):
    """Dos coletas que cuelgan a los lados (de perfil, una detrás)."""
    if view == 'front':
        return [L(outline([(50 - 46, y), (50 - 46 - out, y + 14), (50 - 46 - out - 2, low - 10), (50 - 46 - out + w * 0.6, low, 1), (50 - 46 + w * 0.4, low - 16), (50 - 40, y + 20)]), c),
                L(outline([(50 + 46, y), (50 + 46 + out, y + 14), (50 + 46 + out + 2, low - 10), (50 + 46 + out - w * 0.6, low, 1), (50 + 46 - w * 0.4, low - 16), (50 + 40, y + 20)]), c)]
    if view == 'side':
        return [L(outline([(8, y), (-6, y + 16), (-8, low - 10), (0, low, 1), (6, low - 18), (16, y + 14)]), c)]
    return [L(outline([(6, y), (-8, y + 16), (-10, low - 10), (-2, low, 1), (4, low - 18), (14, y + 14)]), c),
            L(outline([(94, y), (108, y + 16), (110, low - 10), (102, low, 1), (96, low - 18), (86, y + 14)]), c)]


def tie(view, c, y=40):
    """Gomas de las coletas."""
    if view == 'front':
        return [L(ell(3, y + 4, 4.5, 4), c, 'f'), L(ell(97, y + 4, 4.5, 4), c, 'f')]
    if view == 'side':
        return [L(ell(8, y + 4, 4.5, 4), c, 'f')]
    return [L(ell(5, y + 4, 4.5, 4), c, 'f'), L(ell(95, y + 4, 4.5, 4), c, 'f')]


def pony(view, c='mid', y=10, low=96, w=12):
    """Coleta alta que cae por detrás (de frente apenas asoma por arriba)."""
    if view == 'front':
        return [L(outline([(42, 6), (50, -10), (58, 6)]), c)]
    if view == 'side':
        return [L(outline([(14, y - 4), (2, y + 8), (-4, low - 20), (2, low, 1), (10, low - 22), (18, y + 14)]), c)]
    return [L(outline([(50 - w / 2, y), (50 - w * 0.8, low - 20), (50, low, 1), (50 + w * 0.8, low - 20), (50 + w / 2, y)]), c, 'f')]


def bun(view, c='mid', y=-4, r=12):
    if view == 'side':
        return [L(ell(34, y + 4, r, r * 0.9), c)]
    return [L(ell(50, y, r, r * 0.9), c)]


def band(view, c, y=12, h=5, z='f'):
    """Cinta o diadema que pasa por encima de la cabeza."""
    if view == 'front':
        return [L(outline([(8, y + 30), (16, y + 6), (50, y - 4), (84, y + 6), (92, y + 30), (92 - h, y + 30), (82, y + 6 + h), (50, y - 4 + h), (18, y + 6 + h), (8 + h, y + 30)]), c, z, False)]
    if view == 'side':
        return [L(outline([(40, y - 4), (70, y + 8), (74, y + 32), (74 - h, y + 32), (66, y + 8 + h), (38, y - 4 + h)]), c, z, False)]
    return [L(outline([(6, y + 34), (10, y + 10), (90, y + 10), (94, y + 34), (94 - h, y + 34), (88, y + 10 + h), (12, y + 10 + h), (6 + h, y + 34)]), c, z, False)]


def specs(c, rect=False):
    return {'glasses': c, 'glasses_rect': rect}


def blush(y=86):
    return [mark([(26, y), (34, y), (34, y + 3), (26, y + 3)], _c('#f0a0a0')), mark([(66, y), (74, y), (74, y + 3), (66, y + 3)], _c('#f0a0a0'))]


def freckles(c='#c07850', y=86):
    k = _c(c)
    return [L(ell(x, y + dy, 0.9, 0.9), k, 'f', False) for x, dy in ((28, 0), (32, 2), (36, 0), (64, 0), (68, 2), (72, 0))]


def nose_tape(y=82):
    return [mark([(44, y), (56, y), (56, y + 5), (44, y + 5)], _c('#f4e0cc'))]


def tip(view, c, y0, y1, side='both'):
    """Puntas de otro color al final de una melena."""
    k = _c(c)
    if view == 'front':
        return [mark([(4, y0), (14, y0), (12, y1), (2, y1)], k, 'b'), mark([(86, y0), (96, y0), (98, y1), (88, y1)], k, 'b')]
    if view == 'side':
        return [mark([(4, y0), (22, y0 - 2), (22, y1 - 2), (6, y1)], k, 'b')]
    return [mark([(4, y0), (96, y0), (98, y1), (2, y1)], k)]


# ------------------------------------------------------------------ jugadores

# Terrell Brightley (adulto, modelo 3D): melena castaña oscura con raya en medio hasta los hombros y las puntas rojas;
# gafas finas grises, perilla y bigote
C('terrell-brightley', 'delgado', P('#4a3a38', MD, iris='#2a2020'),
  F(eyes='sharp', brows=True, mouth='line', mouth_y=92, hairline=mid(64, 44, 52), face_front=face(chin=104), face_side=face_side(chin=4),
    **specs((170, 170, 176, 255), rect=True)),
  dome('front', top=4, w=46, cy=46, long=100, flare=4) + tip('front', '#d84a2a', 92, 100) +
  [mark([(42, 96), (58, 96), (54, 104), (46, 104)], _c('#3a2a28')), mark([(40, 90), (60, 90), (58, 92), (42, 92)], _c('#3a2a28'))],
  dome('side', top=4, w=46, cy=46, long=96, fr=46) + tip('side', '#d84a2a', 88, 96) + [mark([(80, 96), (88, 96), (86, 104), (80, 104)], _c('#3a2a28'))],
  dome('back', top=4, w=46, cy=46, long=96, ends=3) + tip('back', '#d84a2a', 88, 96))

# Tessa Rapperton: pelo gris verdoso muy oscuro y revuelto en pinchos, coleta alta con un gran lazo azul; flequillo recto
BLU = _c('#3a7ad0')
C('tessa-rapperton', 'chica', P('#3c4446', LT, iris='#3a3a44'),
  F(eyes='normal', brows='angry', mouth='frown', mouth_y=92, hairline=fringe(58, 66)),
  dome('front', top=0, w=48, cy=44, n=9, amp=10, seed=3, sb=74) + pony('front') +
  [L(outline([(28, 6), (10, -6, 1), (18, 12)]), BLU, 'f'), L(outline([(28, 6), (34, -14, 1), (36, 6)]), BLU, 'f')],
  dome('side', top=0, w=46, cy=44, n=9, amp=10, seed=3, nape=80, fr=50) + pony('side', y=8, low=84) +
  [L(outline([(24, 2), (10, -12, 1), (30, 10)]), BLU, 'f')],
  dome('back', top=0, w=48, cy=44, n=9, amp=10, seed=3, nape=80) + pony('back', y=8, low=84) +
  [L(outline([(50, 8), (34, -6, 1), (46, 14)]), BLU, 'f'), L(outline([(50, 8), (66, -6, 1), (54, 14)]), BLU, 'f')])

# Thalia Petras: pelo negro con flequillo recto y dos coletas bajas largas; gafas grandes plateadas
C('thalia-petras', 'chica', P('#2e3038', LT, iris='#5a5a64'),
  F(eyes='normal', brows=True, mouth='frown', mouth_y=92, hairline=fringe(58, 66), **specs((190, 190, 196, 255))),
  dome('front', top=2, w=46, cy=44, sb=72) + tails('front', y=56, low=104, out=8),
  dome('side', top=2, w=46, cy=44, nape=84, fr=52) + tails('side', y=58, low=104),
  dome('back', top=2, w=46, cy=44, nape=84) + tails('back', y=58, low=104))

# Thompson Hummings: tupé blanco y gris echado hacia atrás sobre los lados rapados oscuros; cara ancha, pecas y párpados lilas
C('thompson-hummings', 'corpulento', P('#e8ecf0', MD, iris='#3a3040', low='#3a3434', grey='#9aa4b4'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=94, hairline=[(6, 62), (18, 48), (50, 40), (82, 48), (94, 62)], face_front=face(w=6, jaw=2)),
  [L(outline([(10, 62), (8, 40), (20, 30), (80, 30), (92, 40), (90, 62), (80, 50), (20, 50)]), 'low'),
   L(outline([(16, 40), (20, 14), (40, 0), (70, -6), (98, -4, 1), (84, 6), (90, 18), (76, 30), (40, 34)])),
   L(outline([(16, 40), (20, 14), (36, 4), (40, 30)]), 'grey', 'b', False)] + freckles(),
  [L(outline([(10, 66), (6, 40), (30, 34), (54, 40), (56, 62), (40, 70)]), 'low'),
   L(outline([(8, 38), (16, 14), (40, -2), (76, -4), (102, 0, 1), (84, 12), (88, 26), (60, 30), (30, 36)]))],
  [L(outline([(14, 72), (12, 44), (88, 44), (86, 72), (50, 80)]), 'low'),
   L(outline([(14, 44), (20, 14), (50, -4), (80, 14), (86, 44), (50, 40)])), L(outline([(14, 44), (20, 14), (40, 2), (40, 40)]), 'grey', 'b', False)])

# Tiffany Fencourt: melena azul marino hasta los hombros con raya en medio y una diadema roja con adorno dorado arriba
RED, GOLD = _c('#d03a2a'), _c('#e8b830')
C('tiffany-fencourt', 'chica', P('#1e3e78', LT, iris='#3a5a7a'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=92, hairline=mid(64, 46, 52)),
  dome('front', top=0, w=48, cy=46, long=92, flare=6) + band('front', RED, 4, 6) + [L(outline([(40, -2), (44, -12), (56, -12), (60, -2)]), GOLD, 'f')],
  dome('side', top=0, w=46, cy=46, long=90, fr=46) + band('side', RED, 4, 6),
  dome('back', top=0, w=48, cy=46, long=90, ends=4) + band('back', RED, 4, 6) + [L(outline([(40, 0), (44, -10), (56, -10), (60, 0)]), GOLD, 'f')])

# Timmit Bower: pelo castaño en casquete con un pelo de punta; gafas redondas finas y pecas
C('timmit-bower', 'normal', P('#5a4440', LT, iris='#8a3a5a'),
  F(eyes='normal', brows='angry', mouth='frown', mouth_y=92, hairline=[(6, 64), (16, 56), (40, 54), (60, 56), (84, 54), (94, 64)], **specs((200, 180, 170, 255))),
  dome('front', top=4, w=48, cy=46, sb=66) + [L([(50, 4), (46, -6), (54, -10)], 'mid', 'b', False, False, 2.4)] + freckles(),
  dome('side', top=4, w=46, cy=46, nape=84, fr=56) + [L([(44, 2), (40, -8), (48, -12)], 'mid', 'b', False, False, 2.4)],
  dome('back', top=4, w=48, cy=46, nape=84) + [L([(50, 4), (46, -6), (54, -10)], 'mid', 'b', False, False, 2.4)])

# Tina Hopkins: moño alto crema, cinta roja y blanca, piel tostada, cejas blancas gruesas, tirita en la nariz y ojos naranjas
C('tina-hopkins', 'chica', P('#f0e4cc', TN, iris='#d07020'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 62), (18, 50), (50, 44), (82, 50), (94, 62)]),
  dome('front', top=4, w=46, cy=44, sb=66) + bun('front', y=-2, r=13) + band('front', RED, 10, 7) + band('front', WHITE, 13, 2) + nose_tape(),
  dome('side', top=4, w=46, cy=44, nape=80, fr=48) + bun('side', y=-2) + band('side', RED, 10, 7),
  dome('back', top=4, w=46, cy=44, nape=80) + bun('back', y=-2, r=13) + band('back', RED, 10, 7))

# Tito de Core: melena corta partida en dos colores, azul a un lado y rosa fuerte al otro, que le tapa medio ojo
C('tito-de-core', 'normal', P('#4a6ad0', MD, iris='#3a3a5a', pink='#e8306a'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=92, hairline=swept(52, 70, 64)),
  dome('front', top=2, w=48, cy=46, sb=72) + [L(outline([(50, 0), (82, 10), (98, 40), (96, 72), (80, 70), (60, 74, 1), (50, 50)]), 'pink')],
  dome('side', top=2, w=46, cy=46, nape=84, fr=56) + [L(outline([(48, 0), (80, 10), (94, 40), (90, 60), (60, 56), (52, 30)]), 'pink')],
  dome('back', top=2, w=48, cy=46, nape=84) + [L(outline([(50, 0), (20, 10), (6, 40), (8, 76), (50, 84)]), 'pink')])

# Tobias Thumpern: pelo castaño claro muy rizado y abultado, piel tostada
C('tobias-thumpern', 'normal', P('#c08a6a', TN, iris='#6a3a20'),
  F(eyes='normal', brows=True, mouth='frown', mouth_y=92, hairline=[(6, 64), (14, 58), (30, 50), (50, 54), (70, 46), (86, 58), (94, 64)]),
  dome('front', top=-4, w=52, cy=44, n=10, amp=7, soft=True, sb=80, seed=5),
  dome('side', top=-4, w=50, cy=44, n=10, amp=7, soft=True, nape=88, fr=50, seed=5),
  dome('back', top=-4, w=52, cy=44, n=10, amp=7, soft=True, nape=88, seed=5))

# Tobin Tempelhof: pelo verde claro en casquete con mechones verde oscuro y gafas blancas grandes
C('tobin-tempelhof', 'normal', P('#8ac890', LT, iris='#4a8a6a'),
  F(eyes='normal', brows=True, mouth='frown', mouth_y=92, hairline=[(6, 62), (16, 54), (36, 58), (50, 52), (66, 58), (84, 54), (94, 62)], **specs(WHITE)),
  dome('front', top=0, w=48, cy=44, sb=64) + [strand([(34, 10), (38, 40)], 'deep', 'b', 2.4), strand([(60, 8), (58, 40)], 'deep', 'b', 2.4)],
  dome('side', top=0, w=46, cy=44, nape=82, fr=54) + [strand([(40, 6), (60, 36)], 'deep', 'b', 2.4)],
  dome('back', top=0, w=48, cy=44, nape=82))

# Torric Brawnstone: pelo naranja corto con los lados azul marino, piel morena, cara redonda y cejas naranjas gruesas
C('torric-brawnstone', 'corpulento', P('#f07828', DK, iris='#2a8a7a', low='#2a3050'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=94, hairline=[(6, 60), (16, 50), (50, 44), (84, 50), (94, 60)], face_front=face(w=8, jaw=3)),
  [L(outline([(6, 64), (6, 40), (94, 40), (94, 64), (80, 54), (20, 54)]), 'low')] + dome('front', top=6, w=42, cy=40, sb=50, n=5, amp=6, seed=2),
  [L(outline([(10, 66), (6, 40), (54, 40), (56, 66)]), 'low')] + dome('side', top=6, w=42, cy=40, nape=56, fr=44, n=5, amp=6, seed=2),
  [L(outline([(12, 76), (12, 44), (88, 44), (88, 76), (50, 82)]), 'low')] + dome('back', top=6, w=42, cy=40, nape=56, n=5, amp=6, seed=2))

# Torwyn Endeavor: pelo celeste peinado hacia arriba y atrás en una ola alta; ojos afilados
C('torwyn-endeavor', 'normal', P('#5ac0e0', LT, iris='#3a5a3a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=92, hairline=[(6, 62), (18, 48), (50, 42), (82, 48), (94, 62)]),
  [L(outline([(10, 62), (8, 34), (20, 8), (50, -6), (80, -14), (104, -16, 1), (90, -2), (94, 20), (92, 62), (80, 50), (20, 50)]))],
  [L(outline([(54, 60), (52, 44), (26, 40), (6, 50), (4, 24), (24, 0), (60, -12), (104, -14, 1), (88, 2), (86, 30), (66, 40)]))],
  [L(outline([(8, 80), (6, 34), (20, 6), (50, -8), (80, 6), (94, 34), (92, 80), (50, 88)]))])

# Trace Combe: melena castaño claro en casco con un flequillo que le tapa los ojos del todo; sonrisa
C('trace-combe', 'normal', P('#c08a6a', TN),
  F(eyes='none', brows=False, mouth='smile', mouth_y=92, hairline=False),
  dome('front', top=0, w=50, cy=46, sb=78) + [L(outline([(10, 48), (14, 66), (24, 80, 1), (34, 70), (44, 82, 1), (54, 70), (64, 82, 1), (74, 70), (84, 78, 1), (90, 48)]), 'mid', 'f', True, True),
                                              strand([(30, 56), (32, 72)], 'shade', 'f', 1.2), strand([(60, 56), (60, 72)], 'shade', 'f', 1.2)],
  dome('side', top=0, w=48, cy=46, nape=86, fr=80) + [L(outline([(60, 40), (88, 50), (92, 80, 1), (76, 72), (64, 78, 1)]), 'mid', 'f', True, True)],
  dome('back', top=0, w=50, cy=46, nape=88))

# Trad Askenburg: melena carmesí en casco hasta la barbilla, piel tostada y ojos lilas afilados
C('trad-askenburg', 'normal', P('#b81e2e', TN, iris='#6a5a9a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=92, hairline=swept(48, 58, 64)),
  dome('front', top=0, w=50, cy=46, long=90, flare=2),
  dome('side', top=0, w=48, cy=46, long=88, fr=50),
  dome('back', top=0, w=50, cy=46, long=88, ends=4))

# Trane Levitt (adulto): pelo gris verdoso peinado hacia atrás con mechones de punta a los lados; ojos naranjas
C('trane-levitt', 'delgado', P('#6a8a8a', MD, iris='#c05a2a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=[(6, 62), (16, 46), (50, 40), (84, 46), (94, 62)], face_front=face(chin=104)),
  dome('front', top=4, w=46, cy=44, n=6, amp=10, sweep=0.5, sb=72, seed=8),
  dome('side', top=4, w=46, cy=44, n=6, amp=10, sweep=0.5, nape=84, fr=44, seed=8),
  dome('back', top=4, w=46, cy=44, n=6, amp=10, sweep=0.5, nape=84, seed=8))

# Trebor Donders: pelo rosa en mechones de punta hacia arriba con un mechón negro detrás; piel pálida y marcas rojas en los ojos
PNK = _c('#e8306a')
C('trebor-donders', 'normal', P('#f0a0c8', '#f8e4b8', iris='#3a2a2a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 62), (18, 46), (34, 52), (50, 42), (66, 50), (82, 46), (94, 62)], face_front=face(chin=104)),
  [L(outline([(70, 10), (80, -10), (100, -4), (94, 20)]), BLACK)] + dome('front', top=-4, w=46, cy=44, n=7, amp=12, sweep=-0.4, seed=4, sb=70) +
  [mark([(26, 70), (42, 72), (40, 76), (24, 74)], PNK), mark([(58, 72), (74, 70), (76, 74), (60, 76)], PNK)],
  [L(outline([(10, 10), (0, -6), (16, -10), (20, 10)]), BLACK)] + dome('side', top=-4, w=46, cy=44, n=7, amp=12, sweep=-0.4, seed=4, nape=82, fr=46),
  [L(outline([(70, 10), (80, -8), (98, -2), (92, 20)]), BLACK)] + dome('back', top=-4, w=46, cy=44, n=7, amp=12, sweep=-0.4, seed=4, nape=82))

# Trew Talif: pelo rosa pálido muy rizado y esponjoso con manchas moradas, piel tostada y ojos verdes
PUR = _c('#5a3a6a')
C('trew-talif', 'normal', P('#f0d4dc', TN, iris='#5ab05a'),
  F(eyes='normal', brows='angry', mouth='frown', mouth_y=92, hairline=[(6, 64), (16, 54), (30, 48), (50, 56), (70, 48), (84, 54), (94, 64)]),
  dome('front', top=-4, w=54, cy=46, n=12, amp=7, soft=True, sb=82, seed=6) + [L(ell(18, 34, 7, 9), PUR, 'b', False), L(ell(82, 34, 7, 9), PUR, 'b', False), L(ell(40, 4, 8, 5), PUR, 'b', False), L(ell(64, 4, 8, 5), PUR, 'b', False)],
  dome('side', top=-4, w=52, cy=46, n=12, amp=7, soft=True, nape=88, fr=50, seed=6) + [L(ell(24, 30, 8, 9), PUR, 'b', False)],
  dome('back', top=-4, w=54, cy=46, n=12, amp=7, soft=True, nape=90, seed=6) + [L(ell(30, 30, 8, 9), PUR, 'b', False), L(ell(70, 30, 8, 9), PUR, 'b', False)])

# Trip Cresta: pelo granate largo recogido en una coleta altísima, mechones que caen por la cara; piel morena y pintura
# naranja de guerra alrededor de los ojos
ORA = _c('#e86a2a')
C('trip-cresta', 'normal', P('#6a1e1e', DK, iris='#3a8a7a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 64), (16, 50), (34, 44), (50, 54, ), (66, 44), (84, 50), (94, 64)]),
  [L(outline([(40, 4), (50, -14), (60, 4)]))] + dome('front', top=2, w=46, cy=44, sb=74) +
  [L(outline([(16, 50), (8, 90), (14, 100, 1), (20, 70)])), L(outline([(84, 50), (92, 90), (86, 100, 1), (80, 70)])),
   mark([(22, 66), (42, 72), (36, 82), (24, 76)], ORA), mark([(58, 72), (78, 66), (76, 76), (64, 82)], ORA)],
  dome('side', top=2, w=46, cy=44, nape=84, fr=50) + pony('side', y=0, low=100, w=14),
  dome('back', top=2, w=46, cy=44, nape=84) + pony('back', y=2, low=100, w=16))

# Tris Baylor: pelo gris rizado con una diadema negra, gafas redondas negras y sonrisa
C('tris-baylor', 'normal', P('#a4b4b4', MD, iris='#2a2a2a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=92, hairline=[(6, 64), (16, 54), (34, 48), (52, 56), (70, 48), (84, 54), (94, 64)], **specs(BLACK)),
  dome('front', top=-2, w=52, cy=46, n=11, amp=6, soft=True, sb=80, seed=9) + band('front', BLACK, 6, 3),
  dome('side', top=-2, w=50, cy=46, n=11, amp=6, soft=True, nape=86, fr=50, seed=9) + band('side', BLACK, 6, 3),
  dome('back', top=-2, w=52, cy=46, n=11, amp=6, soft=True, nape=86, seed=9) + band('back', BLACK, 6, 3))

# Trix Rosenblum: melena granate ondulada en casco hasta la barbilla
C('trix-rosenblum', 'normal', P('#7a1838', LT, iris='#3a2a3a'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=92, hairline=mid(64, 46, 50)),
  dome('front', top=-2, w=50, cy=46, long=86, flare=8, n=0),
  dome('side', top=-2, w=48, cy=46, long=84, fr=48),
  dome('back', top=-2, w=50, cy=46, long=84, ends=5))

# Tufton Frizzell: casco de rugby negro con dos cuernos celestes, piel tostada y cejas celestes
CEL = _c('#a8d8e8')
def _helmet(view):
    if view == 'front':
        return [L(outline([(14, 18), (2, 2, 1), (22, 10)]), CEL), L(outline([(86, 18), (98, 2, 1), (78, 10)]), CEL),
                L(outline([(8, 78), (6, 40), (20, 10), (50, 2), (80, 10), (94, 40), (92, 78), (82, 76), (82, 52), (18, 52), (18, 76)]), BLACK),
                L([(10, 36), (50, 30), (90, 36)], _c('#5a5050'), 'f', False, False, 1.4)]
    if view == 'side':
        return [L(outline([(60, 12), (60, -6, 1), (74, 10)]), CEL),
                L(outline([(10, 80), (4, 40), (20, 8), (56, 2), (84, 20), (88, 50), (60, 52), (50, 82)]), BLACK)]
    return [L(outline([(14, 18), (2, 2, 1), (22, 10)]), CEL), L(outline([(86, 18), (98, 2, 1), (78, 10)]), CEL),
            L(outline([(8, 82), (6, 40), (20, 10), (50, 2), (80, 10), (94, 40), (92, 82), (50, 88)]), BLACK)]
C('tufton-frizzell', 'corpulento', P('#202020', TN, iris='#5a8aa0', brow='#a8d8e8'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=94, hairline=False, face_front=face(w=6, jaw=2), ears=False,
    nose=(50, 84, 4)),
  _helmet('front') + [mark([(26, 62), (42, 62), (42, 66), (26, 66)], CEL), mark([(58, 62), (74, 62), (74, 66), (58, 66)], CEL)],
  _helmet('side'), _helmet('back'))

# Uriah Goldfield: pelo gris oscuro en seta, cara alargada con ojos pequeños de susto y la boca abierta
C('uriah-goldfield', 'normal', P('#5a5654', LT),
  F(eyes='dot', brows=True, mouth='none', hairline=[(6, 58), (16, 50), (84, 50), (94, 58)], face_front=face(chin=106)),
  dome('front', top=2, w=54, cy=42, sb=56) + [L(ell(50, 96, 6, 4.5), _c('#6a2a2a'), 'f', True), L(ell(50, 98, 3.5, 1.8), _c('#e07a7a'), 'f', False)],
  dome('side', top=2, w=52, cy=42, nape=72, fr=50),
  dome('back', top=2, w=54, cy=42, nape=74))

# Valentine Lovejoy: dos coletas rojas con gomas celestes y flequillo; ojos rojos
LBL = _c('#7ac8e8')
C('valentine-lovejoy', 'chica', P('#e83a3a', LT, iris='#c82a3a'),
  F(eyes='big', brows='angry', mouth='frown', mouth_y=92, hairline=[(6, 64), (16, 54), (30, 60), (42, 50), (56, 60), (70, 52), (84, 58), (94, 64)]),
  dome('front', top=2, w=48, cy=44, sb=70) + tails('front', y=20, low=96, out=12, w=13) + tie('front', LBL, 18),
  dome('side', top=2, w=46, cy=44, nape=82, fr=52) + tails('side', y=20, low=94) + tie('side', LBL, 18),
  dome('back', top=2, w=48, cy=44, nape=82) + tails('back', y=20, low=94) + tie('back', LBL, 18))

# Vane Nishmont: pelo negro corto en casquete con flequillo
C('vane-nishmont', 'normal', P('#202024', LT, iris='#4a4a5a'),
  F(eyes='normal', brows=True, mouth='line', mouth_y=92, hairline=[(6, 62), (16, 54), (40, 58), (60, 54), (84, 58), (94, 62)]),
  dome('front', top=2, w=48, cy=46, sb=66),
  dome('side', top=2, w=46, cy=46, nape=84, fr=56),
  dome('back', top=2, w=48, cy=46, nape=84))

# Verdy Golnuts: cabeza grande y redonda con el pelo celeste cortito y un pico en punta arriba; ojos entornados y sonrisa
C('verdy-golnuts', 'corpulento', P('#6aa8b4', LT, iris='#3a5a7a'),
  F(eyes='closed', brows=True, mouth='grin', mouth_y=92, hairline=[(6, 50), (20, 40), (50, 34), (80, 40), (94, 50)], face_front=face(w=8, jaw=3)),
  [L(outline([(14, 54), (16, 26), (40, 10), (50, -10, 1), (60, 10), (84, 26), (86, 54), (50, 40)]))] + blush(),
  [L(outline([(54, 46), (40, 36), (10, 44), (14, 20), (40, 8), (50, -10, 1), (62, 10), (80, 22), (70, 34)]))],
  [L(outline([(12, 64), (14, 26), (40, 10), (50, -10, 1), (60, 10), (86, 26), (88, 64), (50, 70)]))])

# Vergil Turnaraud: pelo gris en seta ondulada, cejas grises tristes, lágrimas y boca de pena
TEAR = _c('#6ab0e0')
C('vergil-turnaraud', 'normal', P('#7a7a7a', LT, iris='#2a3a5a'),
  F(eyes='normal', brows=True, mouth='frown', mouth_y=94, hairline=[(6, 58), (16, 52), (30, 56), (50, 52), (70, 56), (84, 52), (94, 58)]),
  dome('front', top=2, w=52, cy=42, n=10, amp=4, soft=True, sb=58, seed=2) + [mark([(36, 82), (40, 82), (40, 90), (36, 90)], TEAR), mark([(60, 82), (64, 82), (64, 90), (60, 90)], TEAR)],
  dome('side', top=2, w=50, cy=42, n=10, amp=4, soft=True, nape=74, fr=52, seed=2),
  dome('back', top=2, w=52, cy=42, n=10, amp=4, soft=True, nape=76, seed=2))

# Verica Nyman: pelo verde oliva oscuro recogido atrás con dos rizos pequeños que caen a los lados del cuello; ojos verdes
C('verica-nyman', 'chica', P('#4a4a30', MD, iris='#8aa020'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=92, hairline=mid(62, 40, 44)),
  dome('front', top=4, w=46, cy=44, sb=64) + [L(outline([(18, 70), (8, 84), (14, 96), (22, 86)])), L(outline([(82, 70), (92, 84), (86, 96), (78, 86)]))],
  dome('side', top=4, w=46, cy=44, nape=80, fr=46) + [L(ell(14, 74, 9, 8))],
  dome('back', top=4, w=46, cy=44, nape=80) + [L(ell(50, 76, 12, 10))])

# Verity Billows (adulta, modelo 3D): melena gris verdosa oscura ondulada y abombada hasta la barbilla, peinada a un lado
C('verity-billows', 'chica', P('#3a4a4a', MD, iris='#2a5a8a'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=92, hairline=swept(44, 54, 62), face_front=face(chin=102)),
  dome('front', top=0, w=52, cy=46, long=86, flare=8),
  dome('side', top=0, w=50, cy=46, long=84, fr=46),
  dome('back', top=0, w=52, cy=46, long=84, ends=4))

# Veronica Camry: pelo gris oscuro largo y liso con el flequillo echado a un lado
C('veronica-camry', 'chica', P('#4a4e58', LT, iris='#3a4a8a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=swept(48, 60, 64)),
  dome('front', top=2, w=48, cy=46, long=104, flare=2),
  dome('side', top=2, w=46, cy=46, long=104, fr=50),
  dome('back', top=2, w=48, cy=46, long=104, ends=4))

# Vicente Olsean: pelo negro ondulado y revuelto hasta el cuello, piel tostada clara
C('vicente-olsean', 'normal', P('#2a2626', MD, iris='#3a6a5a'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 62), (18, 48), (34, 44), (50, 54), (66, 44), (82, 48), (94, 62)]),
  dome('front', top=-2, w=52, cy=46, long=88, flare=8, n=8, amp=6, seed=3),
  dome('side', top=-2, w=50, cy=46, long=86, fr=48, n=8, amp=6, seed=3),
  dome('back', top=-2, w=52, cy=46, long=86, ends=5, n=8, amp=6, seed=3))

# Vincent Melodin: melena celeste larga y ondulada que le tapa un ojo
C('vincent-melodin', 'normal', P('#9ac4dc', LT, iris='#3a6a9a'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=92, hairline=swept(52, 80, 66)),
  dome('front', top=0, w=50, cy=46, long=104, flare=6) + [L(outline([(48, 40), (78, 46), (90, 66), (86, 90, 1), (72, 82), (58, 64)]), 'mid', 'f', True, True)],
  dome('side', top=0, w=48, cy=46, long=104, fr=54),
  dome('back', top=0, w=50, cy=46, long=104, ends=4))

# Vivi Dehues: pelo azul revuelto en mechones cortos y ojos grandes con aros blancos alrededor
C('vivi-dehues', 'chica', P('#2a6ad0', LT, iris='#3aa08a'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=92, hairline=[(6, 64), (18, 52), (30, 60), (44, 52), (58, 62), (72, 52), (84, 60), (94, 64)], **specs(WHITE)),
  dome('front', top=0, w=50, cy=46, n=10, amp=8, sb=80, seed=7),
  dome('side', top=0, w=48, cy=46, n=10, amp=8, nape=86, fr=52, seed=7),
  dome('back', top=0, w=50, cy=46, n=10, amp=8, nape=86, seed=7))

# Vivienne Starling: pelo morado largo y ondulado con flequillo recto y una coleta alta; ojos amarillos
C('vivienne-starling', 'chica', P('#6a4a7a', LT, iris='#d0a020'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=92, hairline=fringe(56, 64)),
  dome('front', top=4, w=46, cy=44, long=104, flare=8, n=6, amp=4, soft=True, seed=2) + pony('front'),
  dome('side', top=4, w=46, cy=44, long=104, fr=50) + pony('side', y=4, low=90),
  dome('back', top=4, w=46, cy=44, long=104, ends=4) + pony('back', y=4, low=90))

# Volbert Brackenbal (portero): pelo verde oscuro en seta con pinchos arriba, piel tostada y ojos granates
C('volbert-brackenbal', 'normal', P('#4a6a5a', TN, iris='#8a2a3a'),
  F(eyes='normal', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 58), (16, 52), (84, 52), (94, 58)]),
  dome('front', top=-2, w=54, cy=42, n=5, amp=6, sb=58, seed=4),
  dome('side', top=-2, w=52, cy=42, n=5, amp=6, nape=74, fr=52, seed=4),
  dome('back', top=-2, w=54, cy=42, n=5, amp=6, nape=76, seed=4))

# Wagner Waltz (portero): pelo rosa pálido corto con un rizo en la frente y el lado derecho rosa fuerte; piel morena
C('wagner-waltz', 'normal', P('#f0c4d4', DK, iris='#4a4a4a', pink='#f070a0'),
  F(eyes='sharp', brows=True, mouth='lips', mouth_y=94, hairline=[(6, 58), (16, 46), (30, 54), (50, 42), (84, 46), (94, 58)], face_front=face(chin=104)),
  dome('front', top=4, w=46, cy=42, sb=60) + [L(outline([(66, 6), (90, 20), (92, 50), (80, 44)]), 'pink')],
  dome('side', top=4, w=44, cy=42, nape=72, fr=44) + [L(outline([(60, 4), (84, 16), (86, 40), (70, 36)]), 'pink')],
  dome('back', top=4, w=46, cy=42, nape=72) + [L(outline([(14, 20), (30, 6), (34, 60), (14, 60)]), 'pink')])

# Wale Gambon: pelo verde azulado en seta ancha, cara muy redonda con papada
C('wale-gambon', 'corpulento', P('#1ea0a8', MD, iris='#5a8a6a'),
  F(eyes='normal', brows='angry', mouth='frown', mouth_y=94, hairline=[(4, 58), (14, 50), (50, 56), (86, 50), (96, 58)], face_front=face(w=10, jaw=4)),
  dome('front', top=4, w=58, cy=42, sb=56),
  dome('side', top=4, w=54, cy=42, nape=70, fr=52),
  dome('back', top=4, w=58, cy=42, nape=72))

# Wander Treeday: pelo rojo rosado largo peinado hacia atrás hasta los hombros, cejas gruesas y ojos amarillos
C('wander-treeday', 'delgado', P('#c04a68', LT, iris='#c09020'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 60), (16, 44), (50, 36), (84, 44), (94, 60)], face_front=face(chin=104)),
  dome('front', top=2, w=46, cy=42, long=100, flare=6),
  dome('side', top=2, w=46, cy=42, long=98, fr=40),
  dome('back', top=2, w=46, cy=42, long=98, ends=4))

# Watt Ownes: pelo castaño en pinchos revueltos, piel tostada y ojos celestes afilados
C('watt-ownes', 'normal', P('#8a4a1e', TN, iris='#3ab0d0'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, hairline=[(6, 62), (18, 48), (32, 56), (46, 46), (60, 56), (74, 46), (86, 54), (94, 62)]),
  dome('front', top=-6, w=50, cy=44, n=9, amp=14, seed=11, sb=70),
  dome('side', top=-6, w=48, cy=44, n=9, amp=14, seed=11, nape=84, fr=48),
  dome('back', top=-6, w=50, cy=44, n=9, amp=14, seed=11, nape=84))

# Wendy Stitchilton: pelo azul marino largo y liso con flequillo recto, un mechón morado y una trenza a un lado
C('wendy-stitchilton', 'chica', P('#3a3a8a', LT, iris='#2a8ab0', pur='#8a5ac8'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=92, hairline=fringe(56, 64)),
  dome('front', top=2, w=48, cy=46, long=106, flare=2) + [L(outline([(14, 50), (20, 50), (18, 100), (12, 100)]), 'pur', 'b', False),
                                                           L(outline([(4, 70), (12, 70), (12, 112), (8, 118, 1), (2, 112)]))],
  dome('side', top=2, w=46, cy=46, long=106, fr=50),
  dome('back', top=2, w=48, cy=46, long=106, ends=4))

# Wentworth Wiggins: melena rubia en campana ancha con un hueco de corazón sobre la frente; marcas doradas en los ojos
YW = _c('#e8c820')
C('wentworth-wiggins', 'normal', P('#f4e050', LT, iris='#c8a020'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=94, hairline=[(6, 58), (18, 50), (40, 50), (50, 58), (60, 50), (82, 50), (94, 58)]),
  [L(outline([(-6, 66, 1), (4, 40), (18, 14), (50, 4), (82, 14), (96, 40), (106, 66, 1), (80, 60), (20, 60)]))] +
  [mark([(22, 70), (40, 66), (42, 70), (24, 74)], YW), mark([(58, 70), (60, 66), (78, 70), (76, 74)], YW)],
  [L(outline([(54, 60), (40, 56), (0, 70, 1), (8, 34), (30, 8), (60, 4), (84, 20), (90, 46), (70, 50)]))],
  [L(outline([(-6, 70, 1), (4, 40), (18, 14), (50, 4), (82, 14), (96, 40), (106, 70, 1), (50, 76)]))])

# Wheyland Schultz: pelo verde azulado en pinchos de punta hacia arriba con un mechón negro; boca abierta de risa
C('wheyland-schultz', 'normal', P('#3ab4a0', MD, iris='#c07020'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, hairline=[(6, 62), (18, 46), (34, 52), (50, 42), (66, 52), (82, 46), (94, 62)]),
  dome('front', top=-8, w=46, cy=42, n=7, amp=14, sweep=0.4, seed=12, sb=72) + [strand([(30, 10), (38, 44)], BLACK, 'b', 3)],
  dome('side', top=-8, w=46, cy=42, n=7, amp=14, sweep=0.4, seed=12, nape=82, fr=46) + [strand([(30, 6), (50, 40)], BLACK, 'b', 3)],
  dome('back', top=-8, w=46, cy=42, n=7, amp=14, sweep=0.4, seed=12, nape=82))

# Whitney Blackrock: pelo lila con flequillo recto y dos trenzas en lazo a los lados, con gomas oscuras
C('whitney-blackrock', 'chica', P('#c080e0', LT, iris='#8a4a9a'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=92, hairline=fringe(58, 66)),
  dome('front', top=2, w=48, cy=44, sb=70) +
  [L(outline([(6, 34), (-8, 22), (-14, 50), (-12, 98), (-2, 104), (6, 84), (2, 56)])), L(outline([(94, 34), (108, 22), (114, 50), (112, 98), (102, 104), (94, 84), (98, 56)]))] + tie('front', _c('#4a2a5a'), 28),
  dome('side', top=2, w=46, cy=44, nape=82, fr=52) + [L(outline([(6, 30), (-10, 20), (-14, 60), (-4, 90), (10, 80)]))],
  dome('back', top=2, w=48, cy=44, nape=82) +
  [L(outline([(6, 34), (-10, 20), (-14, 50), (-8, 86), (6, 92), (8, 70)])), L(outline([(94, 34), (110, 20), (114, 50), (108, 86), (94, 92), (92, 70)]))])

# Willem Durrmore: pelo crema ondulado, piel morena, cara ancha, cejas blancas gruesas y una sonrisa enorme
C('willem-durrmore', 'corpulento', P('#f4e8c4', DK, iris='#6a8a2a'),
  F(eyes='sharp', brows=True, mouth='grin', mouth_y=94, hairline=[(4, 60), (14, 48), (32, 42), (50, 46), (68, 42), (86, 48), (96, 60)], face_front=face(w=10, jaw=4)),
  dome('front', top=4, w=54, cy=44, n=9, amp=4, soft=True, sb=76, seed=3),
  dome('side', top=4, w=52, cy=44, n=9, amp=4, soft=True, nape=84, fr=46, seed=3),
  dome('back', top=4, w=54, cy=44, n=9, amp=4, soft=True, nape=84, seed=3))

# Wily Wimpinberg: melena gris oscura ondulada y abultada hasta el cuello, ojos claros afilados y sonrisa pícara
C('wily-wimpinberg', 'delgado', P('#3e3e40', LT, iris='#a8b8c8'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=94, hairline=[(6, 60), (16, 46), (50, 38), (84, 46), (94, 60)], face_front=face(chin=104)),
  dome('front', top=-4, w=54, cy=44, long=90, flare=10, n=6, amp=6, soft=True, seed=5),
  dome('side', top=-4, w=52, cy=44, long=88, fr=40, n=6, amp=6, soft=True, seed=5),
  dome('back', top=-4, w=54, cy=44, long=88, ends=5, n=6, amp=6, soft=True, seed=5))

# Wing Hyland (portera): pelo rojo óxido revuelto en mechones de punta, piel morena, ojos rojos en espiral y tirita en la nariz
C('wing-hyland', 'chica', P('#a83a1e', DK, iris='#d03030'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=92, hairline=[(6, 64), (18, 54), (30, 66), (44, 54), (58, 66), (72, 54), (84, 62), (94, 64)]),
  dome('front', top=0, w=50, cy=46, n=10, amp=8, seed=13, sb=82) + nose_tape(80),
  dome('side', top=0, w=48, cy=46, n=10, amp=8, seed=13, nape=86, fr=60),
  dome('back', top=0, w=50, cy=46, n=10, amp=8, seed=13, nape=86))

# Winifred Wardrow: melena rubia larga y muy ondulada, peinada con raya a un lado
C('winifred-wardrow', 'chica', P('#f0c060', LT, iris='#3a6ab0'),
  F(eyes='normal', brows=True, mouth='frown', mouth_y=92, hairline=swept(44, 58, 64)),
  dome('front', top=0, w=52, cy=46, long=106, flare=10, n=8, amp=5, soft=True, seed=4),
  dome('side', top=0, w=50, cy=46, long=104, fr=48, n=8, amp=5, soft=True, seed=4),
  dome('back', top=0, w=52, cy=46, long=104, ends=5, n=8, amp=5, soft=True, seed=4))

# Wyatt Stockaway (portero): pelo verde oscuro corto en mechones de punta, pecas y ojos redondos
C('wyatt-stockaway', 'normal', P('#3a5a3a', LT, iris='#3a3a6a'),
  F(eyes='normal', brows=True, mouth='frown', mouth_y=92, hairline=[(6, 60), (18, 50), (40, 46), (50, 54), (60, 46), (82, 50), (94, 60)]),
  dome('front', top=0, w=52, cy=44, n=8, amp=10, sweep=0.3, seed=14, sb=72) + freckles('#d09070'),
  dome('side', top=0, w=50, cy=44, n=8, amp=10, sweep=0.3, seed=14, nape=82, fr=50),
  dome('back', top=0, w=50, cy=44, n=8, amp=10, sweep=0.3, seed=14, nape=82))

# Yarden Forsman: pelo verde pálido muy corto, piel morena y unas gafas de visera plateadas sobre los ojos
SIL = _c('#c8ccd0')
C('yarden-forsman', 'normal', P('#c8d8a8', DK, iris='#2a2a2a'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=94, hairline=[(6, 50), (18, 40), (50, 34), (82, 40), (94, 50)]),
  dome('front', top=8, w=44, cy=40, sb=52) + [L(outline([(10, 68), (20, 62), (50, 64), (80, 62), (90, 68), (84, 80), (56, 78), (50, 74), (44, 78), (16, 80)]), SIL, 'f'),
                                             L(outline([(24, 68), (44, 70), (42, 76), (22, 76)]), _c('#4a4a50'), 'f', False), L(outline([(56, 70), (76, 68), (78, 76), (58, 76)]), _c('#4a4a50'), 'f', False)],
  dome('side', top=8, w=42, cy=40, nape=60, fr=40) + [L(outline([(60, 66), (92, 64), (92, 78), (62, 78)]), SIL, 'f')],
  dome('back', top=8, w=44, cy=40, nape=60) + [L(outline([(17, 70), (83, 70), (83, 74), (17, 74)]), SIL, 'f', False)])

# Yohannes Drummand: pelo gris oscuro estirado hacia atrás con un moño arriba, diadema blanca y cejas curvas gruesas
C('yohannes-drummand', 'delgado', P('#4a4644', LT, iris='#2a2a2a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 60), (16, 44), (50, 36), (84, 44), (94, 60)], face_front=face(chin=104)),
  dome('front', top=4, w=46, cy=44, sb=70) + bun('front', y=-2, r=11) + band('front', WHITE, 10, 2),
  dome('side', top=4, w=46, cy=44, nape=82, fr=42) + bun('side', y=-2, r=11) + band('side', WHITE, 10, 2),
  dome('back', top=4, w=46, cy=44, nape=82) + bun('back', y=-2, r=11) + band('back', WHITE, 10, 2))

# Zacharias Klutchett: pelo rapado caqui con una cresta roja naranja en medio; sonrisa enorme
C('zacharias-klutchett', 'normal', P('#a89870', LT, iris='#4a4a6a', crest='#e85a3a'),
  F(eyes='normal', brows='angry', mouth='grin', mouth_y=94, hairline=[(6, 56), (18, 44), (50, 36), (82, 44), (94, 56)]),
  dome('front', top=8, w=44, cy=42, sb=60, shade=False) + [L(outline([(38, 30), (36, 0), (48, -22, 1), (52, -2), (60, -10, 1), (62, 30)]), 'crest')],
  dome('side', top=8, w=42, cy=42, nape=78, fr=40, shade=False) + [L(outline([(20, 20), (30, -4), (54, -20, 1), (62, -6), (78, -10, 1), (70, 20)]), 'crest')],
  dome('back', top=8, w=44, cy=42, nape=78, shade=False) + [L(outline([(42, 40), (40, 0), (50, -18, 1), (60, 0), (58, 40)]), 'crest')])

# Zackory Wart: pelo granate oscuro en tupé plano alto (flat-top), cejas gruesas, mandíbula grande y piel tostada
C('zackory-wart', 'normal', P('#6a2a1e', TN, iris='#3a3a3a'),
  F(eyes='normal', brows='angry', mouth='line', mouth_y=96, hairline=[(6, 56), (16, 44), (50, 40), (84, 44), (94, 56)], face_front=face(chin=106, jaw=4)),
  [L(outline([(10, 60), (10, -4), (90, -4), (90, 60), (80, 48), (20, 48)]))] + [strand([(40, 0), (44, 40)], 'deep', 'b', 2)],
  [L(outline([(54, 52), (40, 44), (10, 50), (10, -4), (86, -4), (86, 42), (70, 40)]))],
  [L(outline([(10, 70), (10, -4), (90, -4), (90, 70), (50, 76)]))])

# Zaydan Smythe: pelo lila en casco con mechones oscuros en forma de cuerno a los lados y ojos en espiral
DKP = _c('#3a2a3a')
C('zaydan-smythe', 'normal', P('#c4a0dc', MD, iris='#3a2a3a'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=94, hairline=fringe(58, 66)),
  dome('front', top=0, w=48, cy=46, long=90, flare=4) + [L(outline([(10, 30), (2, 60), (8, 84, 1), (16, 56)]), DKP, 'b', False), L(outline([(90, 30), (98, 60), (92, 84, 1), (84, 56)]), DKP, 'b', False)],
  dome('side', top=0, w=46, cy=46, long=88, fr=54) + [L(outline([(30, 30), (20, 60), (26, 84, 1), (36, 56)]), DKP, 'b', False)],
  dome('back', top=0, w=48, cy=46, long=88, ends=4))

# Zayn Pinegrove (modelo 3D): pelo gris pizarra oscuro peinado hacia atrás en una corona de puntas, pendientes; ojos verdosos
C('zayn-pinegrove', 'normal', P('#3e4a54', LT, iris='#7a8a5a'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=94, hairline=[(6, 60), (16, 46), (34, 40), (50, 50), (66, 40), (84, 46), (94, 60)]),
  dome('front', top=-6, w=48, cy=42, n=6, amp=12, seed=15, sb=76) + [L(ell(12, 82, 1.6, 1.6), BLACK, 'f', False), L(ell(88, 82, 1.6, 1.6), BLACK, 'f', False)],
  dome('side', top=-6, w=46, cy=42, n=6, amp=12, sweep=-0.6, seed=15, nape=82, fr=44) + [L(ell(46, 80, 1.6, 1.6), BLACK, 'f', False)],
  dome('back', top=-6, w=48, cy=42, n=6, amp=12, seed=15, nape=84))

# Zinnia Crylic: melena roja con flequillo recto y puntas rosas que salen a los lados como orejas, y una boina negra
C('zinnia-crylic', 'chica', P('#d82a2a', LT, iris='#c02a3a', pk='#f4a0b0'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=92, hairline=fringe(58, 66)),
  dome('front', top=2, w=48, cy=46, sb=78) + [L(outline([(10, 66), (-6, 82, 1), (12, 84)]), 'pk'), L(outline([(90, 66), (106, 82, 1), (88, 84)]), 'pk'),
                                              L(ell(70, 4, 16, 8), BLACK, 'f'), L(ell(70, -4, 3, 3), BLACK, 'f')],
  dome('side', top=2, w=46, cy=46, nape=86, fr=54) + [L(ell(56, 2, 18, 8), BLACK, 'f')],
  dome('back', top=2, w=48, cy=46, nape=86) + [L(ell(30, 4, 16, 8), BLACK, 'f')])

# Zoey Tippings: dos coletas largas castaño oscuro con gomas turquesa, piel tostada, ojos cerrados de risa y gran sonrisa
TQ = _c('#4ac8c8')
C('zoey-tippings', 'chica', P('#5a3a3a', TN, iris='#3a2a2a'),
  F(eyes='closed', brows=True, mouth='grin', mouth_y=92, hairline=mid(62, 44, 48)),
  dome('front', top=2, w=46, cy=44, sb=70) + tails('front', y=12, low=110, out=10, w=14) + tie('front', TQ, 10),
  dome('side', top=2, w=46, cy=44, nape=82, fr=46) + tails('side', y=12, low=110) + tie('side', TQ, 10),
  dome('back', top=2, w=46, cy=44, nape=82) + tails('back', y=12, low=110) + tie('back', TQ, 10))

# Zuna Yokochenko: melena castaño rojiza corta y ahuecada a los lados, cejas gruesas cortas y sonrisa de dientes
C('zuna-yokochenko', 'chica', P('#8a3e22', LT, iris='#3a4a6a'),
  F(eyes='sharp', brows=True, mouth='grin', mouth_y=92, hairline=[(6, 62), (16, 52), (40, 50), (50, 56), (60, 50), (84, 52), (94, 62)]),
  dome('front', top=4, w=46, cy=44, long=78, flare=14),
  dome('side', top=4, w=46, cy=44, long=76, fr=50),
  dome('back', top=4, w=46, cy=44, long=76, ends=3))
