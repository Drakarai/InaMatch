"""Ojeadores de Victory Road (scouts-vr), tanda 03: dibujados a partir de su retrato; claves 'scouts-vr:<id>'.

Casi todos salen solo del retrato (frente) y el perfil y la espalda se deducen del peinado. Donnie Summerfield, Eamon
Cattrall y Eshin tienen modelo 3D y es el suyo. Las masas de pelo son dome()/hl()/face() de la tanda 09 de IE1."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars_scouts_ie1_09 import dome, face, face_side, hl, mark
from chars_scouts_ie2_03 import round_glasses, teeth_grin  # noqa: F401
from chars_scouts_ie3_02 import bowl3
from chars_scouts_ie3_05 import headphones
from heads import FACE_FRONT, quad  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)


def _c(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5)) + (255,)


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


def S(pid, body, palette, f, fx=(), sx=(), bx=(), **dk):
    """Jugador con la misma masa de pelo (dome) en las tres vistas y capas extra por vista."""
    C(pid, body, palette, f, dome('front', **dk) + list(fx), dome('side', **dk) + list(sx), dome('back', **dk) + list(bx))


def fr(pts, c='mid'):
    """Mechón de delante (por encima de la cara)."""
    return L(outline(pts), c, 'f')


def shades(view, c=BLACK):
    """Gafas de sol negras."""
    if view == 'front':
        return [L(blob([(24, 70), (46, 70), (44, 82), (28, 82)], 4), c, 'f'), L(blob([(54, 70), (76, 70), (72, 82), (56, 82)], 4), c, 'f'),
                L([(44, 72), (56, 72)], c, 'f', False, False, 2.0)]
    return [L(blob([(74, 70), (88, 70), (86, 81), (76, 81)], 4), c, 'f'), L([(74, 72), (50, 68)], c, 'f', False, False, 2.0)]


def mic(view, c=BLACK):
    if view == 'front':
        return [L(quad((88, 76), (84, 96), (60, 96)), c, 'f', False, False, 1.6), L(ell(58, 96, 3, 2.4), c, 'f')]
    return [L(quad((48, 76), (66, 98), (86, 96)), c, 'f', False, False, 1.6), L(ell(87, 96, 3, 2.4), c, 'f')]


def blush(y=86, c='#f0a0a0', dx=20):
    k = _c(c)
    return [L(ell(50 - dx, y, 5, 2.6), k, 'f', False), L(ell(50 + dx, y, 5, 2.6), k, 'f', False)]


def blush_side(y=86, c='#f0a0a0'):
    return [L(ell(76, y, 4, 2.4), _c(c), 'f', False)]


def nose(y=86):
    return [L(quad((49, y - 4), (52, y), (49, y + 1)), _c('#c08060'), 'f', False, False, 1.0)]


# ------------------------------------------------------------------ jugadores

# Corwin Lockhart: pelo gris azulado oscuro revuelto con dos picos arriba como orejas de gato y un flequillo largo que le
# tapa un ojo; piel clara, ojos amarillos y boca seria
C('corwin-lockhart', 'normal', P('#3a4656', '#f6d6c0', iris='#d8c840', shade='#2a323e'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=93, hairline=hl(5, 66, 46, 60, jit=2, seed=1)),
  dome('front', top=-2, w=48, cy=44, n=6, amp=9, seed=31, sb=78) +
  [fr([(14, -4), (8, -18, 1), (24, 4)]), fr([(86, -4), (92, -18, 1), (76, 4)]),
   fr([(38, 30), (56, 28), (66, 52), (60, 84, 1), (52, 62), (44, 50)])],
  dome('side', top=-2, w=48, cy=44, n=6, amp=9, seed=31, nape=88, fr=52) + [fr([(72, 30), (90, 36), (92, 60), (86, 82, 1), (80, 56)])],
  dome('back', top=-2, w=48, cy=44, n=6, amp=9, seed=31, nape=90) + [fr([(14, -4), (8, -18, 1), (24, 4)]), fr([(86, -4), (92, -18, 1), (76, 4)])])

# Cosette Lyricotte: media melena castaño claro con las puntas hacia fuera y un rizo grande al lado izquierdo, una raya
# en medio con un mechón; ojos verdes, rubor y sonrisa
S('cosette-lyricotte', 'chica', P('#b0763c', '#f8dcc4', iris='#4a9a7a', shade='#8a5a2a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=[(6, 66), (20, 48), (40, 44), (50, 40), (60, 44), (80, 48), (94, 66)]),
  blush(87, '#f0a878') + [fr([(44, 30), (52, 26), (56, 52), (50, 70, 1), (46, 52)]), fr([(6, 78), (-6, 72, 1), (6, 66)])],
  blush_side(87, '#f0a878'), (),
  top=0, w=48, cy=44, n=5, amp=6, soft=True, seed=32, long=90, flare=10, ends=4)

# Cosmo Starward: pelo castaño oscuro corto con un tupé en punta arriba, piel morena y gafas de sol negras
S('cosmo-starward', 'normal', P('#5a4c40', '#a86a44', iris='#1e1a1a', shade='#3e342c'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=94, ear_out=2, hairline=[(8, 62), (18, 46), (36, 40), (50, 44), (64, 40), (82, 46), (92, 62)]),
  shades('front') + [fr([(44, 14), (48, -12, 1), (54, 0), (60, -10, 1), (58, 18)])],
  shades('side') + [fr([(60, 6), (66, -12, 1), (74, 4)])], [fr([(44, 14), (48, -12, 1), (56, 14)])],
  top=4, w=46, cy=46, n=0, sb=60, nape=80, fr=42)

# Crag Bolderin: afro castaño oscuro rizado, piel morena, cara ancha, ojos azules, cejas gruesas fruncidas y boca torcida
S('crag-bolderin', 'corpulento', P('#4a3a2c', '#b0784e', iris='#4a8ad0', shade='#33281e'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, face_front=face(w=5, chin=104, jaw=4), ear_out=4, nose=(50, 86, 2.6),
    hairline=[(6, 62), (16, 50), (34, 44), (50, 46), (66, 44), (84, 50), (94, 62)]),
  (), (), (),
  top=-6, w=54, cy=40, n=12, amp=6, soft=True, seed=33, sb=60, nape=82, fr=44)

# Credence Throwe: rizos rosa intenso en una mata alta, piel morena clara, ojos verde azulado y sonrisa de dientes
S('credence-throwe', 'normal', P('#e04a8a', '#c08a5e', iris='#3aa0a8', shade='#b02a68'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, hairline=hl(6, 62, 46, 54, jit=2, seed=4)),
  (), (), (),
  top=-10, w=48, cy=38, n=11, amp=8, soft=True, seed=34, sb=58, nape=78, fr=42)

# Crest Vertall: melena azul marino con la raya en medio y dos mechones celestes, hasta la mandíbula; cejas gruesas
# oscuras, cara larga y gesto serio
S('crest-vertall', 'delgado', P('#1e2a4a', '#e8c0a0', iris='#2a2a3a', shade='#141c34', light='#6a9ae0'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=97, face_front=face(chin=106), hairline=[(8, 70), (20, 46), (40, 34), (50, 30), (60, 34), (80, 46), (92, 70)]),
  [L([(44, 6), (28, 28), (14, 60), (10, 86)], 'light', 'f', False, False, 1.6), L([(56, 6), (72, 28), (86, 60), (90, 86)], 'light', 'f', False, False, 1.6)],
  [L([(60, 10), (76, 30), (82, 56)], 'light', 'f', False, False, 1.6)], (),
  top=0, w=46, cy=44, n=0, long=92, flare=4, fr=40, ends=3)

# Cristensen Blance: pelo negro revuelto hasta la nuca con un mechón verde menta a la derecha y otro que le cruza la cara;
# un ojo guiñado, rubor y boca abierta riendo
MINT = _c('#80d0b0')
S('cristensen-blance', 'normal', P('#2a2420', '#f8dcc4', iris='#2a2020', shade='#1a1614'),
  F(eyes='closed', brows=False, mouth='grin', mouth_y=94, hairline=hl(5, 66, 46, 58, lean=-2, jit=3, seed=5)),
  blush(87) + [fr([(70, 10), (84, 4), (92, 30), (88, 56, 1), (80, 34)], MINT), fr([(30, 30), (48, 30), (44, 60), (36, 76, 1), (34, 54)])],
  blush_side(87) + [fr([(64, 4), (82, 8), (86, 30), (80, 50, 1), (72, 26)], MINT)], [fr([(14, 10), (6, 4), (4, 30), (10, 50, 1), (18, 26)], MINT)],
  top=-2, w=48, cy=44, n=7, amp=9, seed=35, long=96, flare=8, fr=50)

# Culinaro Brons: melena larga gris hasta los hombros, piel morena, gafas plateadas, cejas grises fruncidas y boca seria
S('culinaro-brons', 'delgado', P('#8a8282', '#b07a50', iris='#3a6aa8', shade='#6a6262', brow='#5a5454'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, glasses=_c('#c8ccd0'), face_front=face(chin=104),
    hairline=[(6, 70), (18, 46), (38, 38), (50, 40), (62, 38), (82, 46), (94, 70)]),
  (), (), (),
  top=0, w=48, cy=44, n=6, amp=8, soft=True, seed=36, long=112, flare=10, fr=46, ends=5)

# Curia Caldwell: media melena en casco morada que se vuelve rosa en las puntas, flequillo con picos; cejas de corazón,
# ojos morados, rubor y sonrisa
PINK = _c('#f0a8d0')
C('curia-caldwell', 'chica', P('#8a4a8a', '#f8dcc8', iris='#5a2a5a', shade='#6a346a'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=[(8, 60), (20, 54), (32, 58), (42, 52), (50, 56), (58, 52), (68, 58), (80, 54), (92, 60)]),
  bowl3('front', top=4, side=84, fringe=58) + [L(blob([(8, 70), (20, 66), (18, 86), (8, 84)], 4), PINK, 'f'), L(blob([(92, 70), (80, 66), (82, 86), (92, 84)], 4), PINK, 'f')] +
  blush(86) + [L(quad((30, 64), (36, 58), (42, 64)), OUTC, 'f', False, False, 1.6), L(quad((58, 64), (64, 58), (70, 64)), OUTC, 'f', False, False, 1.6)],
  bowl3('side', top=4, nape=88, fringe=58) + [L(blob([(4, 72), (20, 74), (26, 88), (8, 86)], 4), PINK, 'f')] + blush_side(86),
  bowl3('back', top=4, nape=88) + [L(blob([(6, 72), (94, 72), (92, 88), (50, 92), (8, 88)], 4), PINK, 'f')])

# Curven Rallye: pelo gris verdoso con un mechón verde azulado, un ahoge arriba y un flequillo largo que tapa un ojo;
# piel morena clara, ojo verde y media sonrisa
TEAL = _c('#40a0a0')
S('curven-rallye', 'normal', P('#5a6a64', '#c8946a', iris='#8ac040', shade='#44524c'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=94, hairline=hl(4, 64, 46, 58, lean=4, jit=2, seed=6)),
  [fr([(46, 2), (40, -18, 1), (54, -2)]), fr([(70, 26), (40, 24), (18, 46), (14, 70), (24, 88, 1), (50, 82), (54, 56), (56, 44)]),
   L([(50, 28), (28, 44), (18, 72)], TEAL, 'f', False, False, 3.0)],
  [fr([(50, 0), (44, -18, 1), (58, -2)]), L([(60, 20), (80, 36), (88, 58)], TEAL, 'f', False, False, 3.0)], [fr([(46, 2), (40, -18, 1), (54, -2)])],
  top=0, w=46, cy=44, n=6, amp=9, sweep=0.6, seed=37, sb=72, nape=86, fr=48)

# Cuthbert Obelidge: cabeza de huevo con el pelo gris crema muy corto, cara ancha y mofletuda, ojos apretados, rubor y
# boca de enfado
C('cuthbert-obelidge', 'corpulento', P('#d8d4c0', '#f6d0b8', iris='#2a2020', shade='#b8b4a0'),
  F(eyes='closed', brows='angry', mouth='frown', mouth_y=98, face_front=face(w=8, chin=106, jaw=6, top=20), face_side=face_side(chin=6, jaw=6), ears=False,
    hairline=[(10, 56), (20, 40), (36, 30), (50, 28), (64, 30), (80, 40), (90, 56)]),
  dome('front', top=-12, w=40, cy=40, n=0, sb=54, shade=False) + blush(90, dx=24),
  dome('side', top=-12, w=40, cy=40, n=0, nape=78, fr=34, shade=False, side_burn=False) + blush_side(90),
  dome('back', top=-12, w=40, cy=40, n=0, nape=80, shade=False))

# Cyrus Veil: nube de pelo amarillo verdoso abultada, cejas amarillas, piel morena clara, ojos amarillos y boca seria
S('cyrus-veil', 'normal', P('#c8c830', '#d0a078', iris='#b0a020', shade='#9a9a20'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(8, 62), (14, 50), (26, 56), (36, 48), (50, 54), (64, 48), (74, 56), (86, 50), (92, 62)]),
  (), (), (),
  top=-10, w=52, cy=38, n=9, amp=8, soft=True, seed=38, sb=60, nape=78, fr=44)

# Damian Stonewell: pelo verde azulado en pinchos con flequillo de mechones hasta los ojos y patillas largas; ojos claros
S('damian-stonewell', 'normal', P('#30b0a0', '#f2cfb0', iris='#8aa0a8', shade='#20887a'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=94, hairline=hl(6, 70, 46, 64, jit=3, seed=7)),
  [fr([(14, 60), (10, 84, 1), (22, 66)]), fr([(86, 60), (90, 84, 1), (78, 66)])], [fr([(56, 58), (60, 84, 1), (66, 60)])], (),
  top=0, w=48, cy=44, n=8, amp=9, seed=39, sb=74, nape=88, fr=56)

# Damion Duform: pelo gris azulado en casco con el flequillo recto, cejas azules gruesas, ojos rojos y piel morena
C('damion-duform', 'normal', P('#506068', '#b07a50', iris='#c02a2a', shade='#3a4850', brow='#2a4a8a'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=94, hairline=[(8, 58), (92, 58)]),
  bowl3('front', top=0, side=62, fringe=56) + [L([(26, 62), (44, 66)], _c('#2a4a8a'), 'f', False, False, 3.4), L([(74, 62), (56, 66)], _c('#2a4a8a'), 'f', False, False, 3.4)],
  bowl3('side', top=0, nape=80, fringe=56),
  bowl3('back', top=0, nape=82))

# Danica Wynn: pelo rojo con picos a los lados y por delante, y un pañuelo negro atado en la frente; ojos negros afilados
S('danica-wynn', 'chica', P('#d02a2a', '#f8dcc4', iris='#2a1a1a', shade='#a01a1a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=hl(4, 64, 50, 62, jit=3, seed=8)),
  [L(outline([(10, 54), (12, 24), (50, 18), (88, 24), (90, 54), (50, 48)]), BLACK, 'f'), fr([(4, 70), (-8, 62, 1), (12, 56)]), fr([(96, 70), (108, 62, 1), (88, 56)]),
   fr([(40, 2), (34, -14, 1), (48, -4)]), fr([(60, 2), (68, -14, 1), (56, -4)])],
  [L(outline([(40, 54), (36, 22), (60, 14), (88, 24), (88, 50), (60, 48)]), BLACK, 'f'), fr([(4, 70), (-8, 60, 1), (12, 56)])],
  [L(outline([(10, 54), (12, 24), (50, 18), (88, 24), (90, 54), (50, 48)]), BLACK, 'f')],
  top=0, w=48, cy=46, n=7, amp=10, seed=40, sb=72, nape=86, fr=50)

# Darrell Dignard: moño de sumo rojo arriba sobre un casquete de pelo rojo, cara redonda y ancha, ojos cerrados contentos
# y sonrisa
C('darrell-dignard', 'corpulento', P('#c83a30', '#e8b088', iris='#2a2020', shade='#a02a24'),
  F(eyes='closed', brows=False, mouth='smile', mouth_y=96, face_front=face(w=8, chin=106, jaw=6), face_side=face_side(chin=6, jaw=6), ear_out=6, nose=(50, 86, 2.4),
    hairline=[(8, 62), (18, 54), (36, 52), (50, 52), (64, 52), (82, 54), (92, 62)]),
  dome('front', top=10, w=46, cy=48, n=0, sb=62, shade=False) + [L(ell(50, 4, 10, 8), 'mid', 'f'), L(outline([(44, 12), (56, 12), (56, 16), (44, 16)]), WHITE, 'f')],
  dome('side', top=10, w=46, cy=48, n=0, nape=82, fr=50, shade=False) + [L(ell(46, 6, 9, 8), 'mid', 'f'), L(outline([(40, 13), (52, 13), (52, 17), (40, 17)]), WHITE, 'f')],
  dome('back', top=10, w=46, cy=48, n=0, nape=82, shade=False) + [L(ell(50, 4, 10, 8), 'mid', 'f'), L(outline([(44, 12), (56, 12), (56, 16), (44, 16)]), WHITE, 'f')])

# Dasher Ballard: melena rubia clara en casco redondo con un mechón blanco en media luna, que le tapa un ojo; ojo azul
C('dasher-ballard', 'normal', P('#f0e070', '#f2cfb0', iris='#5a9ac0', shade='#d0c050'),
  F(eyes='normal', brows=False, mouth='line', mouth_y=94, hairline=[(8, 60), (92, 60)]),
  bowl3('front', top=-4, side=86, fringe=60, w=4) + [fr([(84, 40), (60, 30), (34, 34), (16, 56), (22, 88, 1), (50, 84), (52, 56)]),
                                                     L(quad((62, 6), (40, 30), (52, 54)), WHITE, 'f', False, False, 4.0)],
  bowl3('side', top=-4, nape=90, fringe=60, w=4) + [L(quad((60, 4), (48, 26), (58, 46)), WHITE, 'f', False, False, 4.0)],
  bowl3('back', top=-4, nape=92, w=4))

# Dashiell Fass: pelo rubio con un mechón gris oscuro ancho que le cae en diagonal por la cara y le tapa un ojo; piel
# morena clara y sonrisa de dientes
GRY = _c('#3a4248')
S('dashiell-fass', 'normal', P('#e8c840', '#c8946a', iris='#2a2020', shade='#c0a020'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, hairline=hl(4, 66, 46, 58, lean=3, jit=2, seed=9)),
  [fr([(36, 6), (54, 2), (68, 40), (74, 70), (70, 90, 1), (60, 66), (48, 40)], GRY)],
  [fr([(56, 2), (74, 8), (88, 40), (86, 66, 1), (76, 40)], GRY)], [fr([(40, 4), (60, 2), (64, 40), (54, 60, 1), (46, 36)], GRY)],
  top=-2, w=46, cy=44, n=5, amp=8, sweep=0.6, seed=41, sb=74, nape=86, fr=48)

# Davey Lockers: pelo morado corto y rizado, piel morena oscura, marcas rojas a los lados de la cara, ojos rojos
# entornados y sonrisa de dientes de tiburón
REDM = _c('#d03a3a')
S('davey-lockers', 'normal', P('#7060b0', '#9a5a3a', iris='#c02a2a', shade='#544890'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=95, ear_out=3, hairline=[(10, 62), (18, 48), (34, 42), (50, 44), (66, 42), (82, 48), (90, 62)]),
  [L([(16, 70), (22, 74)], REDM, 'f', False, False, 2.4), L([(84, 70), (78, 74)], REDM, 'f', False, False, 2.4),
   L([(44, 93), (46, 96), (48, 93), (50, 96), (52, 93), (54, 96), (56, 93)], OUTC, 'f', False, False, 0.9)],
  [L([(60, 70), (66, 74)], REDM, 'f', False, False, 2.4)], (),
  top=-4, w=46, cy=42, n=10, amp=6, soft=True, seed=42, sb=58, nape=78, fr=42)

# Davis Tarvish: pelo naranja dorado en ondas echado a un lado con un tupé que vuela hacia la derecha; piel morena, ojos
# verde azulado y sonrisa
S('davis-tarvish', 'normal', P('#f0a030', '#c87a40', iris='#3a9aa0', shade='#c87a1a', light='#f8d070'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=94, hairline=[(8, 62), (18, 48), (34, 40), (54, 44), (72, 40), (84, 48), (92, 62)]),
  [fr([(40, 10), (70, 2), (96, 16), (100, 36, 1), (82, 24), (64, 28)], 'light'), fr([(20, 36), (44, 30), (40, 54, 1), (30, 44)])],
  [fr([(60, 4), (90, 10), (102, 30, 1), (84, 24)], 'light')], (),
  top=-2, w=48, cy=44, n=5, amp=9, sweep=0.8, soft=True, seed=43, sb=66, nape=84, fr=46)

# Dazziel Spinwick: casi calvo con un tupé pequeño morado rosado, cara ancha y mofletuda, cejas gruesas, rubor y sonrisa
C('dazziel-spinwick', 'corpulento', P('#a07090', '#f2cfb0', iris='#4a3a3a', shade='#805470', brow='#a07090'),
  F(eyes='closed', brows=True, mouth='grin', mouth_y=96, face_front=face(w=8, chin=106, jaw=6), face_side=face_side(chin=6, jaw=6), big_ears=2, ear_out=6,
    hairline=[(10, 56), (20, 46), (36, 42), (50, 40), (64, 42), (80, 46), (90, 56)]),
  dome('front', top=12, w=40, cy=46, n=0, sb=56, shade=False) + [fr([(40, 20), (46, 2, 1), (52, 14), (58, 0, 1), (62, 22)])] + blush(88, dx=24) +
  [L([(26, 64), (40, 62)], _c('#a07090'), 'f', False, False, 4.0), L([(74, 64), (60, 62)], _c('#a07090'), 'f', False, False, 4.0)],
  dome('side', top=12, w=40, cy=46, n=0, nape=76, fr=40, shade=False, side_burn=False) + [fr([(60, 18), (66, 0, 1), (74, 18)])] + blush_side(88),
  dome('back', top=12, w=40, cy=46, n=0, nape=76, shade=False) + [fr([(42, 20), (48, 4, 1), (58, 20)])])

# Diana Whispervelt: melena rubia lisa y larga con flequillo recto, raya en medio y dos mechones largos a los lados de la
# cara; ojos azules
S('diana-whispervelt', 'chica', P('#e8c878', '#f8e0cc', iris='#3a6ab0', shade='#c8a050'),
  F(eyes='big', brows=False, mouth='line', mouth_y=93, hairline=[(8, 60), (20, 62), (36, 60), (50, 62), (64, 60), (80, 62), (92, 60)]),
  [fr([(12, 56), (10, 110), (20, 112), (22, 56)]), fr([(88, 56), (90, 110), (80, 112), (78, 56)]), L([(50, 4), (50, 30)], 'shade', 'f', False, False, 1.4)],
  [fr([(54, 56), (52, 110), (62, 112), (62, 56)])], (),
  top=0, w=46, cy=44, n=0, long=110, flare=4, fr=60, ends=3)

# Didar Valmont: piel muy oscura, lados rapados y arriba el pelo gris beige peinado hacia atrás; ojos lila y sonrisa
C('didar-valmont', 'normal', P('#a89a88', '#5a3020', iris='#9a7ad0', shade='#887a68'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=94, ear_out=2, hairline=[(14, 54), (22, 40), (38, 30), (50, 28), (62, 30), (78, 40), (86, 54)]),
  [L(outline([(16, 64), (12, 40), (22, 18), (50, 8), (78, 18), (88, 40), (84, 64), (80, 50), (20, 50)]), 'skin_d'),
   L(outline([(28, 44), (26, 14), (50, 0), (74, 14), (72, 44), (50, 36)]))],
  [L(outline([(52, 60), (40, 70), (14, 60), (6, 36), (20, 12), (50, 4), (76, 12), (84, 30), (70, 34)]), 'skin_d'),
   L(outline([(84, 30), (80, 8), (50, -2), (20, 8), (16, 24), (40, 20), (62, 24)]))],
  [L(outline([(16, 74), (12, 40), (22, 18), (50, 8), (78, 18), (88, 40), (84, 74), (50, 80)]), 'skin_d'),
   L(outline([(30, 50), (28, 14), (50, 2), (72, 14), (70, 50), (50, 56)]))])

# Dina Faith Kingston: media melena verde crema pálido con las puntas vueltas hacia fuera y un mechón sobre la frente;
# ojos amarillos afilados con delineado negro
S('dina-faith-kingston', 'chica', P('#d0d0a0', '#d8a880', iris='#d0a020', shade='#a8a878'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 66), (18, 50), (34, 44), (50, 48), (66, 44), (82, 50), (94, 66)]),
  [fr([(40, 28), (60, 26), (58, 52), (50, 70, 1), (46, 50)]), fr([(4, 92), (-10, 84, 1), (8, 76)]), fr([(96, 92), (110, 84, 1), (92, 76)])],
  [fr([(4, 92), (-10, 82, 1), (10, 76)])], (),
  top=0, w=48, cy=44, n=4, amp=7, soft=True, seed=44, long=94, flare=10, fr=50, ends=4)

# Divar Deepwell: piel oscura, pelo negro de puntas abiertas a los lados y una cresta verde agua en forma de hoja arriba;
# ojos verde azulado
AQ = _c('#40c8a8')
S('divar-deepwell', 'normal', P('#1e1a1e', '#4a3028', iris='#3aa8a8', shade='#121012'),
  F(eyes='big', brows='angry', mouth='frown', mouth_y=94, hairline=hl(5, 64, 48, 58, jit=3, seed=10)),
  [fr([(28, 30), (20, 4, 1), (36, 14), (44, -16, 1), (50, 4), (56, -16, 1), (64, 14), (80, 4, 1), (72, 30), (50, 36)], AQ),
   fr([(12, 72), (4, 86, 1), (16, 62)], AQ), fr([(88, 72), (96, 86, 1), (84, 62)], AQ)],
  [fr([(40, 24), (44, -12, 1), (56, 4), (68, -10, 1), (72, 14), (84, 6, 1), (78, 28)], AQ)],
  [fr([(28, 30), (20, 4, 1), (36, 14), (44, -16, 1), (50, 4), (56, -16, 1), (64, 14), (80, 4, 1), (72, 30), (50, 36)], AQ)],
  top=0, w=50, cy=46, n=9, amp=10, seed=45, sb=70, nape=86, fr=50)

# Dizzy Fumbleton (portera): pelo castaño recogido atrás en una coleta, con dos rizos sueltos junto a las orejas; ojos
# grandes, rubor y sonrisa
C('dizzy-fumbleton', 'chica', P('#6a5448', '#d8a888', iris='#2a2020', shade='#4e3c32'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=[(14, 60), (20, 44), (36, 34), (50, 32), (64, 34), (80, 44), (86, 60)]),
  dome('front', top=2, w=42, cy=44, n=0, sb=60) + blush(87) +
  [L(quad((14, 66), (2, 84), (12, 96)), 'mid', 'f', False, False, 3.0), L(quad((86, 66), (98, 84), (88, 96)), 'mid', 'f', False, False, 3.0)],
  dome('side', top=2, w=42, cy=44, n=0, nape=76, fr=36) + [L(blob([(8, 50), (-6, 64), (-2, 90), (8, 78)], 4), 'mid', 'b')] + blush_side(87),
  dome('back', top=2, w=42, cy=44, n=0, nape=76) + [L(blob([(44, 56), (56, 56), (58, 96), (50, 104), (42, 96)], 4), 'mid', 'f')])

# Domino Guerrera: pelo en cepillo plano negro con los lados gris verdoso, cara grande de mandíbula ancha y ojos de
# párpado caído
C('domino-guerrera', 'corpulento', P('#2a3430', '#f0c8a8', iris='#2a2a2a', shade='#1a221e', light='#8aa098'),
  F(eyes='dot', brows='angry', mouth='line', mouth_y=98, face_front=face(w=8, chin=108, jaw=8), face_side=face_side(chin=8, jaw=8), ear_out=6,
    hairline=[(8, 58), (14, 46), (30, 42), (70, 42), (86, 46), (92, 58)]),
  [L(outline([(12, 60), (10, 42), (90, 42), (88, 60), (84, 50), (16, 50)]), 'light'), L(outline([(14, 46), (16, 24), (84, 24), (86, 46)]))],
  [L(outline([(52, 56), (40, 64), (14, 58), (10, 40), (84, 38), (82, 46), (62, 46)]), 'light'), L(outline([(10, 40), (12, 22), (84, 22), (86, 40)]))],
  [L(outline([(10, 70), (8, 42), (92, 42), (90, 70), (50, 76)]), 'light'), L(outline([(14, 46), (16, 24), (84, 24), (86, 46)]))])

# Donnie Summerfield (comentarista, con modelo 3D): pelo castaño liso con flequillo, unos cascos negros con micrófono;
# ojos castaños y sonrisa
S('donnie-summerfield', 'normal', P('#7a4a30', '#f6d0b0', iris='#7a4a2a', shade='#5a3420'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=94, hairline=hl(5, 66, 48, 60, lean=-1, jit=2, seed=11)),
  headphones('front', BLACK) + mic('front'), headphones('side', BLACK) + mic('side'), headphones('back', BLACK),
  top=0, w=46, cy=44, n=6, amp=6, soft=True, seed=46, sb=70, nape=86, fr=52)

# Donovan Brasswagon: melena rubia dorada en tirabuzones grandes que le enmarcan la cara, piel clara, ojos amarillos y
# boca recta
S('donovan-brasswagon', 'delgado', P('#e8b030', '#fbe4d8', iris='#c0b030', shade='#c08a1a'),
  F(eyes='big', brows=False, mouth='line', mouth_y=94, face_front=face(chin=104), hairline=[(8, 66), (20, 46), (36, 40), (50, 50), (64, 40), (80, 46), (92, 66)]),
  [L(ell(10, 96, 7, 6), 'mid', 'f'), L(ell(90, 96, 7, 6), 'mid', 'f'), fr([(36, 30), (50, 46), (64, 30), (56, 22), (44, 22)], 'shade')],
  [L(ell(30, 98, 7, 6), 'mid', 'f')], [L(ell(30, 98, 7, 6), 'mid', 'f'), L(ell(70, 98, 7, 6), 'mid', 'f')],
  top=0, w=48, cy=44, n=8, amp=6, soft=True, seed=47, long=94, flare=8, fr=50, ends=4)

# Douglass Serve: melena larga oscura en ondas hasta los hombros, piel morena, cicatrices en la cara, ojos verdes y ceño
S('douglass-serve', 'normal', P('#3a2a3a', '#9a6040', iris='#7aa040', shade='#241a24'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=hl(5, 68, 46, 60, jit=3, seed=12)),
  [L([(30, 80), (44, 66)], _c('#5a3020'), 'f', False, False, 1.6), L([(32, 86), (42, 76)], _c('#5a3020'), 'f', False, False, 1.4)],
  [], (),
  top=-2, w=52, cy=44, n=9, amp=6, soft=True, seed=48, long=104, flare=12, fr=52, ends=5)

# Draven Savager: pelo morado echado hacia atrás con mechones sueltos sobre la frente, piel morena, cejas moradas gruesas
# y fruncidas, ojos castaños
S('draven-savager', 'normal', P('#5040a0', '#b07a50', iris='#8a4a2a', shade='#3a2e7a', brow='#3a2e7a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=[(10, 60), (20, 44), (36, 36), (50, 34), (64, 36), (80, 44), (90, 60)]),
  [fr([(36, 26), (48, 20), (44, 44, 1)]), fr([(60, 24), (70, 28), (66, 48, 1)])], (), (),
  top=-2, w=46, cy=44, n=6, amp=8, sweep=-0.6, seed=49, sb=62, nape=84, fr=42)

# Dreamer Havenridge: media melena negra lisa con un flequillo largo que le tapa un ojo, piel clara y media sonrisa
S('dreamer-havenridge', 'normal', P('#1e2422', '#f8dcc8', iris='#8a9aa8', shade='#121614'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=94, hairline=[(8, 66), (20, 50), (40, 44), (60, 46), (80, 50), (92, 66)]),
  [fr([(80, 30), (54, 24), (24, 40), (16, 66), (24, 88, 1), (50, 84), (54, 58), (64, 48)])], [fr([(70, 30), (90, 38), (92, 60), (86, 80, 1), (78, 54)])], (),
  top=0, w=46, cy=44, n=0, long=96, flare=4, fr=50, ends=3)

# Drewey Fournell: pelo castaño en seta abombada, cejas negras gruesas, ojos de punto, rubor redondo
S('drewey-fournell', 'normal', P('#7a5848', '#f8d8c0', iris='#1e1a1a', shade='#5a3e32'),
  F(eyes='dot', brows=True, mouth='line', mouth_y=94, hairline=[(8, 58), (92, 58)]),
  blush(86, '#f09090', 22) + [L(quad((28, 64), (36, 60), (44, 64)), OUTC, 'f', False, False, 3.0), L(quad((56, 64), (64, 60), (72, 64)), OUTC, 'f', False, False, 3.0)],
  blush_side(86, '#f09090'), (),
  top=-8, w=54, cy=38, n=0, sb=58, nape=78, fr=56)

# Duarte Wilde: pelo azul morado en pinchos echados hacia atrás, con las puntas de los lados rosa fucsia; piel morena,
# ojos azules y ceño fruncido
FUC = _c('#e04060')
S('duarte-wilde', 'normal', P('#4a4a8a', '#9a5a3a', iris='#3a6ac0', shade='#34346a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=hl(5, 64, 46, 56, jit=3, seed=13)),
  [fr([(12, 56), (4, 82, 1), (18, 66)], FUC), fr([(88, 56), (96, 82, 1), (82, 66)], FUC)], [fr([(30, 70), (24, 90, 1), (40, 76)], FUC)],
  [fr([(12, 56), (4, 82, 1), (18, 66)], FUC), fr([(88, 56), (96, 82, 1), (82, 66)], FUC)],
  top=-4, w=48, cy=44, n=9, amp=11, sweep=-0.3, seed=50, sb=66, nape=86, fr=48)

# Dunk Highfield: pelo dorado oliva revuelto en rizos con dos horquillas verde agua; ojos amarillos y ceño fruncido
S('dunk-highfield', 'normal', P('#a88a20', '#f2cfb0', iris='#c8a020', shade='#806814'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=hl(5, 64, 46, 58, jit=3, seed=14)),
  [L([(64, 34), (74, 26)], AQ, 'f', False, False, 2.2), L([(68, 38), (78, 30)], AQ, 'f', False, False, 2.2)], [L([(74, 32), (84, 24)], AQ, 'f', False, False, 2.2)], (),
  top=-6, w=50, cy=42, n=10, amp=8, soft=True, seed=51, sb=66, nape=84, fr=48)

# Dyne Amic: nube de pelo celeste claro, dos puntos celestes en la frente, ojos oscuros grandes y boca pequeña
S('dyne-amic', 'normal', P('#a8e0e8', '#f8dcc4', iris='#2a3a5a', shade='#80c0c8'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=94, hairline=[(8, 62), (16, 50), (30, 54), (40, 46), (50, 52), (60, 46), (70, 54), (84, 50), (92, 62)]),
  [L(ell(44, 58, 2.6, 2.6), 'mid', 'f'), L(ell(56, 58, 2.6, 2.6), 'mid', 'f')], (), (),
  top=-8, w=50, cy=40, n=9, amp=8, soft=True, seed=52, sb=62, nape=80, fr=46)

# Eamon Cattrall (con modelo 3D): pelo verde oscuro revuelto en mechones largos que se abren a los lados; ojos amarillos
# de párpado caído y media sonrisa
S('eamon-cattrall', 'normal', P('#3a4a3a', '#e8c4a0', iris='#c8b040', shade='#283428'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=94, hairline=hl(5, 64, 46, 58, lean=2, jit=3, seed=15)),
  [fr([(8, 50), (-8, 54, 1), (10, 40)]), fr([(92, 50), (108, 54, 1), (90, 40)])], [fr([(10, 50), (-8, 50, 1), (12, 38)])],
  [fr([(8, 50), (-8, 54, 1), (10, 40)]), fr([(92, 50), (108, 54, 1), (90, 40)])],
  top=-4, w=48, cy=44, n=8, amp=10, sweep=0.4, seed=53, sb=66, nape=86, fr=48)

# Ecole Linwood: pelo verde con dos coletas bajas recogidas con lazos morados y un mechón en la frente; ojos cerrados
# contentos, rubor y sonrisa
BOW = _c('#a868a0')
S('ecole-linwood', 'chica', P('#4a8a6a', '#f8dcc4', iris='#2a2020', shade='#346a50'),
  F(eyes='closed', brows=True, mouth='smile', mouth_y=93, hairline=[(8, 62), (20, 48), (40, 42), (50, 48), (60, 42), (80, 48), (92, 62)]),
  blush(87) + [L(ell(4, 96, 10, 9), 'mid', 'f'), L(ell(96, 96, 10, 9), 'mid', 'f'), L(blob([(4, 80), (14, 74), (18, 86), (8, 88)], 4), BOW, 'f'),
               L(blob([(96, 80), (86, 74), (82, 86), (92, 88)], 4), BOW, 'f'), fr([(44, 30), (54, 28), (52, 50, 1)])],
  blush_side(87) + [L(ell(22, 98, 10, 9), 'mid', 'f'), L(blob([(20, 80), (32, 76), (34, 88), (22, 90)], 4), BOW, 'f')],
  [L(ell(8, 96, 10, 9), 'mid', 'f'), L(ell(92, 96, 10, 9), 'mid', 'f'), L(blob([(8, 80), (18, 74), (22, 86), (12, 88)], 4), BOW, 'f'),
   L(blob([(92, 80), (82, 74), (78, 86), (88, 88)], 4), BOW, 'f')],
  top=0, w=48, cy=44, n=0, sb=74, nape=86, fr=48)

# Eden Snowbell: pelo blanco plateado recogido en una trenza gruesa que le cae por un lado, con horquillas de colores;
# ojos claros con pestañas y boca pequeña
S('eden-snowbell', 'chica', P('#e0dcd8', '#f6dcc8', iris='#9aa0b0', shade='#c0bab4'),
  F(eyes='big', brows=False, mouth='line', mouth_y=93, hairline=[(14, 60), (20, 44), (36, 34), (50, 36), (64, 34), (80, 44), (86, 60)]),
  [L(ell(14, 100, 8, 7), 'mid', 'f'), L(ell(8, 112, 7, 6), 'mid', 'f'), L(ell(12, 122, 6, 5), 'mid', 'f'),
   L([(62, 26), (70, 22)], _c('#f0a0c0'), 'f', False, False, 2.2), L([(64, 30), (72, 26)], _c('#f0e080'), 'f', False, False, 2.2)],
  [L(ell(30, 96, 8, 7), 'mid', 'f')], [L(ell(30, 96, 8, 7), 'mid', 'f'), L(ell(26, 108, 7, 6), 'mid', 'f'), L(ell(28, 118, 6, 5), 'mid', 'f')],
  top=2, w=44, cy=44, n=0, sb=60, nape=86, fr=38)

# Edith Endenwald (portera): pelo crema con dos coletas abultadas como nubes a los lados; ojos naranja grandes con
# pestañas y sonrisa
S('edith-endenwald', 'chica', P('#f0e0c8', '#f2cfb0', iris='#e08020', shade='#d8c4a8'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=[(8, 62), (16, 50), (30, 54), (40, 46), (50, 52), (60, 46), (70, 54), (84, 50), (92, 62)]),
  [L(blob([(-2, 64), (4, 56), (-10, 76), (0, 92), (12, 84), (14, 70)], 6), 'mid', 'f'), L(blob([(102, 64), (96, 56), (110, 76), (100, 92), (88, 84), (86, 70)], 6), 'mid', 'f')],
  [L(blob([(10, 60), (-4, 66), (-6, 86), (8, 90), (18, 74)], 6), 'mid', 'f')],
  [L(blob([(-2, 64), (4, 56), (-10, 76), (0, 92), (12, 84), (14, 70)], 6), 'mid', 'f'), L(blob([(102, 64), (96, 56), (110, 76), (100, 92), (88, 84), (86, 70)], 6), 'mid', 'f')],
  top=-4, w=46, cy=42, n=8, amp=7, soft=True, seed=54, sb=64, nape=82, fr=46)

# Edmin Streator: rizos morado oscuro en mata alta, gafas redondas de cristal con espirales y sonrisa de dientes
def _swirls():
    out = []
    for cx in (36, 64):
        out.append(L(ell(cx, 76, 9, 8), WHITE, 'f', False))
        out.append(L(ell(cx, 76, 6, 5) + [ell(cx, 76, 6, 5)[0]], _c('#4a8ab0'), 'f', False, False, 1.4))
        out.append(L(ell(cx, 76, 2.6, 2.2) + [ell(cx, 76, 2.6, 2.2)[0]], _c('#4a8ab0'), 'f', False, False, 1.2))
    return out + round_glasses('front', _c('#c8ccd0'), y=76, sep=14, r=9, w=1.8)
S('edmin-streator', 'normal', P('#4a3a5a', '#f2cfb0', iris='#2a2020', shade='#342844'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=94, hairline=hl(6, 62, 48, 58, jit=3, seed=16)),
  _swirls(), round_glasses('side', _c('#c8ccd0'), y=76, r=9, lens=WHITE), (),
  top=-10, w=50, cy=38, n=12, amp=7, soft=True, seed=55, sb=62, nape=80, fr=50)

# Edmund Boon (portero): pelo morado en casco con el flequillo recto y un mechón partido, ojos rosas grandes y pecas
C('edmund-boon', 'normal', P('#9a4aa0', '#f6d4b8', iris='#d060b0', shade='#7a347e'),
  F(eyes='big', brows=False, mouth='line', mouth_y=94, hairline=[(8, 62), (92, 62)]),
  bowl3('front', top=-2, side=66, fringe=62, w=6) + [L(ell(c, 86, 0.9, 0.9), _c('#c88a6a'), 'f', False) for c in (34, 38, 62, 66)],
  bowl3('side', top=-2, nape=82, fringe=62, w=6),
  bowl3('back', top=-2, nape=84, w=6))

# Edton Prentt: pelo verde oliva en casco echado a un lado con un mechón naranja ancho a la izquierda; ojos azules
ORG = _c('#e06a20')
C('edton-prentt', 'normal', P('#6a6a2a', '#f6d4b8', iris='#3a5ab0', shade='#4e4e1c'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=94, hairline=[(8, 66), (18, 58), (30, 52), (50, 48), (70, 50), (92, 64)]),
  bowl3('front', top=-4, side=78, fringe=52, w=4) + [fr([(6, 50), (12, 30), (30, 26), (26, 50), (16, 74, 1)], ORG)],
  bowl3('side', top=-4, nape=84, fringe=52, w=4),
  bowl3('back', top=-4, nape=86, w=4) + [fr([(94, 40), (90, 24), (76, 24), (80, 50), (90, 70, 1)], ORG)])

# Eilidh Innes: melena larga ondulada rosa crema pálido con un moño arriba, un mechón que le tapa un ojo; ojo ámbar y
# labios rojos
S('eilidh-innes', 'chica', P('#e8d0c8', '#f6dcc8', iris='#d09020', shade='#c8b0a8'),
  F(eyes='sharp', brows=False, mouth='lips', mouth_y=94, mouth_w=5, hairline=hl(4, 68, 46, 60, lean=-3, jit=2, seed=17)),
  [L(ell(50, -4, 14, 10), 'mid', 'f'), fr([(14, 26), (46, 22), (52, 50), (50, 88, 1), (26, 80), (16, 56)])],
  [L(ell(46, -4, 12, 10), 'mid', 'f')], [L(ell(50, -4, 14, 10), 'mid', 'f')],
  top=2, w=48, cy=44, n=7, amp=6, soft=True, seed=56, long=110, flare=12, fr=50, ends=5)

# Eldon Compayne: pelo gris plata con dos picos hacia arriba y hacia fuera como cuernos y la capa de debajo negra; piel
# morena, ojos azules
S('eldon-compayne', 'normal', P('#909090', '#b07a50', iris='#3a6ac0', shade='#707070', low='#1e1a1e'),
  F(eyes='big', brows='angry', mouth='frown', mouth_y=94, hairline=[(12, 58), (22, 40), (36, 52), (50, 40), (64, 52), (78, 40), (88, 58)]),
  [fr([(14, 30), (2, -10, 1), (32, 12)]), fr([(86, 30), (98, -10, 1), (68, 12)]), L(outline([(16, 56), (20, 36), (34, 50), (24, 58)]), 'low', 'f'),
   L(outline([(84, 56), (80, 36), (66, 50), (76, 58)]), 'low', 'f')],
  [fr([(70, 20), (92, -8, 1), (82, 24)])], [fr([(14, 30), (2, -10, 1), (32, 12)]), fr([(86, 30), (98, -10, 1), (68, 12)])],
  top=4, w=44, cy=44, n=0, sb=60, nape=84, fr=46)

# Eli Hoopsen: afro castaño muy oscuro, piel clara, cara larga, cejas gruesas y boca seria
S('eli-hoopsen', 'normal', P('#3a3230', '#f6d8b8', iris='#5a4a8a', shade='#262020'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=97, face_front=face(chin=106), nose=(50, 86, 2.2), hairline=[(10, 66), (16, 50), (34, 46), (50, 48), (66, 46), (84, 50), (90, 66)]),
  [], (), (),
  top=-10, w=50, cy=38, n=13, amp=6, soft=True, seed=57, sb=74, nape=82, fr=46)

# Elian Kitronic: pelo gris oscuro en pinchos con una melena hasta la nuca, ojos amarillos y sonrisa de dientes
S('elian-kitronic', 'normal', P('#4a4a52', '#f6d4b8', iris='#d0c040', shade='#34343a'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, hairline=hl(5, 66, 46, 58, jit=3, seed=18)),
  (), (), (),
  top=-4, w=50, cy=44, n=9, amp=10, seed=58, sb=72, nape=88, fr=50)

# Ellie Fumble: melena larga negra hasta la cintura, cascos con micrófono y dos antenas verdes; ojos verdes entornados y
# sonrisa
GRN = _c('#40c040')
S('ellie-fumble', 'chica', P('#2a2a26', '#f6dcc8', iris='#40b040', shade='#1a1a18'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=93, hairline=[(8, 60), (18, 46), (36, 40), (50, 44), (64, 40), (82, 46), (92, 60)]),
  headphones('front', BLACK) + mic('front') + [L([(66, 20), (70, 8)], GRN, 'f', False, False, 1.4), L(ell(70, 7, 2.2, 2.2), GRN, 'f'),
                                               L([(74, 24), (80, 14)], GRN, 'f', False, False, 1.4), L(ell(80, 13, 2.2, 2.2), GRN, 'f')],
  headphones('side', BLACK) + mic('side') + [L([(70, 18), (76, 6)], GRN, 'f', False, False, 1.4), L(ell(76, 5, 2.2, 2.2), GRN, 'f')], headphones('back', BLACK),
  top=0, w=48, cy=44, n=0, long=120, flare=6, fr=48, ends=4)

# Elmer Trommel: cresta rosa fucsia alta con los lados rapados granate, una cinta blanca gruesa en la frente; piel
# morena y ojos amarillos afilados
C('elmer-trommel', 'normal', P('#d04a80', '#b07a50', iris='#d0a020', shade='#a02a60', low='#7a3a50'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=[(12, 64), (14, 56), (86, 56), (88, 64)]),
  [L(outline([(16, 64), (12, 40), (22, 20), (50, 12), (78, 20), (88, 40), (84, 64), (80, 50), (20, 50)]), 'low'),
   L(outline([(38, 40), (44, 10), (54, -18, 1), (62, 10), (62, 40)])), L(outline([(10, 62), (10, 50), (90, 50), (90, 62), (50, 66)]), WHITE, 'f')],
  [L(outline([(54, 62), (40, 70), (14, 60), (6, 36), (20, 14), (50, 6), (76, 12), (84, 30), (70, 36)]), 'low'),
   L(outline([(30, 30), (50, -10, 1), (70, 10), (66, 30)])), L(outline([(10, 52), (88, 46), (88, 58), (10, 62)]), WHITE, 'f')],
  [L(outline([(16, 74), (12, 40), (22, 18), (50, 8), (78, 18), (88, 40), (84, 74), (50, 80)]), 'low'),
   L(outline([(40, 70), (40, 10), (50, -14, 1), (60, 10), (60, 70)])), L(outline([(10, 62), (10, 50), (90, 50), (90, 62), (50, 66)]), WHITE, 'f')])

# Emery Hillmere: pelo verde oscuro corto en pinchos revueltos, piel morena, ojos verdes y sonrisa de dientes
S('emery-hillmere', 'normal', P('#4a5a44', '#a86a44', iris='#7a9a5a', shade='#34422e'),
  F(eyes='big', brows='angry', mouth='grin', mouth_y=94, hairline=hl(6, 62, 46, 54, jit=3, seed=19)),
  (), (), (),
  top=-4, w=48, cy=44, n=9, amp=8, seed=59, sb=62, nape=82, fr=44)

# Emi Blanchett: melena larga castaño claro hasta la cintura, con un mechón largo que le cae por delante de un hombro;
# ojos azul grisáceo grandes y sonrisa
S('emi-blanchett', 'chica', P('#b89a80', '#f8e0cc', iris='#5a6a8a', shade='#987a62'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=[(8, 62), (18, 48), (34, 42), (50, 46), (66, 42), (82, 48), (92, 62)]),
  [fr([(10, 60), (4, 110), (14, 124, 1), (20, 100), (22, 62)])], [fr([(56, 60), (58, 110), (66, 122, 1), (68, 64)])], (),
  top=0, w=48, cy=44, n=4, amp=6, soft=True, seed=60, long=118, flare=6, fr=52, ends=4)

# Emil Tait: pelo rojo en casco con el flequillo recto de mechones, ojos azules grandes y cejas finas
C('emil-tait', 'normal', P('#e83a2a', '#f8dcc4', iris='#3a6aa0', shade='#b82a1a'),
  F(eyes='big', brows=True, mouth='frown', mouth_y=94, hairline=[(8, 60), (20, 62), (34, 58), (50, 62), (66, 58), (80, 62), (92, 60)]),
  bowl3('front', top=-2, side=78, fringe=60, w=4), bowl3('side', top=-2, nape=86, fringe=60, w=4), bowl3('back', top=-2, nape=88, w=4))

# Enna Flashette (portera): pelo verde oscuro con dos trenzas que le salen a los lados, cara redonda, rubor y boca seria
S('enna-flashette', 'chica', P('#4a604a', '#f6d4b8', iris='#4a4aa0', shade='#344634'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=94, hairline=[(8, 60), (20, 58), (40, 52), (50, 56), (60, 52), (80, 58), (92, 60)]),
  blush(88, '#f0a090', 22) + [L(ell(x, y, 5, 4), 'mid', 'f') for x, y in ((8, 84), (0, 88), (-6, 92))] + [L(ell(x, y, 5, 4), 'mid', 'f') for x, y in ((92, 84), (100, 88), (106, 92))],
  blush_side(88, '#f0a090') + [L(ell(x, y, 5, 4), 'mid', 'f') for x, y in ((24, 84), (16, 88), (10, 92))],
  [L(ell(x, y, 5, 4), 'mid', 'f') for x, y in ((8, 84), (0, 88), (-6, 92))] + [L(ell(x, y, 5, 4), 'mid', 'f') for x, y in ((92, 84), (100, 88), (106, 92))],
  top=0, w=48, cy=44, n=5, amp=5, soft=True, seed=61, sb=70, nape=84, fr=56)

# Erina Haberdash: media melena azul violeta lisa con un mechón sobre la frente; ojos castaños afilados y sonrisa leve
S('erina-haberdash', 'chica', P('#5050b0', '#f8e0cc', iris='#7a5a3a', shade='#3a3a8a'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=93, hairline=[(8, 62), (18, 46), (40, 40), (60, 44), (80, 48), (92, 62)]),
  [fr([(46, 22), (66, 26), (58, 50, 1), (54, 34)]), fr([(4, 90), (-8, 86, 1), (8, 78)]), fr([(96, 90), (108, 86, 1), (92, 78)])],
  [fr([(6, 90), (-6, 84, 1), (10, 78)])], (),
  top=0, w=46, cy=44, n=0, long=92, flare=8, fr=48, ends=3)

# Eshin (con modelo 3D): pelo negro azulado corto y redondo, cara ancha, cejas gruesas y sonrisa
S('eshin', 'corpulento', P('#1e2a3a', '#f6d4b8', iris='#6a6aa0', shade='#121c28'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=96, face_front=face(w=8, chin=106, jaw=6), face_side=face_side(chin=6, jaw=6), ear_out=6,
    hairline=hl(5, 60, 46, 54, jit=2, seed=20)),
  (), (), (),
  top=0, w=52, cy=44, n=8, amp=5, soft=True, seed=62, sb=60, nape=80, fr=44)

# Evander Greenvale: rizos verde oliva abultados, cejas verdes gruesas, piel morena, ojos rojos y sonrisa de dientes
S('evander-greenvale', 'normal', P('#8a9a3a', '#a86a44', iris='#c02a2a', shade='#6a7a24', brow='#6a7a24'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, hairline=[(10, 60), (16, 50), (30, 54), (40, 46), (50, 52), (60, 46), (70, 54), (84, 50), (90, 60)]),
  (), (), (),
  top=-10, w=50, cy=38, n=11, amp=8, soft=True, seed=63, sb=58, nape=78, fr=46)

# Eviden Tracer: pelo negro revuelto con pinchos y un ahoge, con un flequillo largo que le tapa un ojo; ojo amarillo
S('eviden-tracer', 'normal', P('#141414', '#f8dcc4', iris='#e0c020', shade='#0a0a0a'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=94, hairline=hl(4, 66, 46, 58, lean=-3, jit=3, seed=21)),
  [fr([(46, 2), (54, -24, 1), (60, 0)]), fr([(14, 30), (48, 26), (52, 52), (50, 88, 1), (24, 80), (16, 56)])],
  [fr([(50, 0), (60, -24, 1), (66, 0)]), fr([(72, 30), (92, 36), (92, 60), (86, 80, 1), (80, 56)])], [fr([(46, 2), (54, -24, 1), (60, 0)])],
  top=-2, w=50, cy=44, n=8, amp=12, seed=64, long=96, flare=10, fr=52, ends=4)

# Evon Newground: pelo rosa claro hasta el cuello con las puntas hacia fuera y una estrella en lo alto; ojos naranja
S('evon-newground', 'normal', P('#f0c8d8', '#f6d8c0', iris='#e08a20', shade='#d0a0b8'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=hl(5, 66, 46, 60, jit=3, seed=22)),
  [fr([(46, 10), (50, 2, 1), (54, 10)], 'shade'), fr([(4, 80), (-10, 70, 1), (8, 62)]), fr([(96, 80), (110, 70, 1), (92, 62)])],
  [fr([(6, 80), (-8, 70, 1), (10, 62)])], (),
  top=0, w=48, cy=44, n=6, amp=7, soft=True, seed=65, long=96, flare=8, fr=52, ends=4)

# Ezekiel Gravendirge: pelo azul revuelto con dos picos arriba y un flequillo espeso que le tapa los dos ojos
S('ezekiel-gravendirge', 'normal', P('#3a68a8', '#f6d8c0', iris='#2a2020', shade='#284c80'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=94, hairline=[(6, 82), (20, 82), (36, 80), (50, 84), (64, 80), (80, 82), (94, 82)]),
  [fr([(30, 10), (24, -18, 1), (44, 4)]), fr([(70, 10), (76, -18, 1), (56, 4)])],
  [fr([(60, 6), (66, -18, 1), (76, 6)]), fr([(64, 30), (92, 40), (94, 66), (88, 86, 1), (80, 60)])],
  [fr([(30, 10), (24, -18, 1), (44, 4)]), fr([(70, 10), (76, -18, 1), (56, 4)])],
  top=-2, w=52, cy=46, n=10, amp=10, seed=66, sb=86, nape=90, fr=60)

# Ezra Bachmann: pelo rubio en casco con rizos hacia fuera a los lados, gafas redondas negras gruesas y sonrisa
C('ezra-bachmann', 'normal', P('#e8d098', '#f6d4b8', iris='#3a3a3a', shade='#c8b078'),
  F(eyes='dot', brows=False, mouth='smile', mouth_y=94, hairline=[(8, 58), (92, 58)]),
  bowl3('front', top=2, side=70, fringe=58) + [fr([(8, 56), (-6, 50, 1), (6, 66)]), fr([(92, 56), (106, 50, 1), (94, 66)])] +
  round_glasses('front', BLACK, y=76, sep=14, r=8, w=2.6),
  bowl3('side', top=2, nape=84, fringe=58) + round_glasses('side', BLACK, y=76, r=8, w=2.6),
  bowl3('back', top=2, nape=86) + [fr([(8, 56), (-6, 50, 1), (6, 66)]), fr([(92, 56), (106, 50, 1), (94, 66)])])

# Ezrail Corbell: pelo verde muy oscuro en pinchos altos echados hacia atrás, con un pico negro arriba y un pico de
# viuda en la frente; patillas en pico, ojos rojos y sonrisa de dientes
S('ezrail-corbell', 'normal', P('#2a4a3a', '#f6dcc8', iris='#c02a2a', shade='#1a3428'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, hairline=[(14, 62), (18, 44), (34, 40), (50, 60), (66, 40), (82, 44), (86, 62)]),
  [fr([(30, 20), (40, -24, 1), (56, -10), (70, -20, 1), (66, 20)], BLACK), fr([(12, 64), (6, 86, 1), (20, 70)]), fr([(88, 64), (94, 86, 1), (80, 70)])],
  [fr([(30, 10), (56, -26, 1), (66, 10)], BLACK)], [fr([(30, 20), (40, -24, 1), (56, -10), (70, -20, 1), (66, 20)], BLACK)],
  top=-6, w=48, cy=44, n=8, amp=13, sweep=-0.4, seed=67, sb=66, nape=84, fr=44)
