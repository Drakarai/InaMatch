"""Ojeadores de Victory Road (scouts-vr), tanda 07: dibujados a partir de su retrato; claves 'scouts-vr:<id>'.

Ninguno de la tanda tiene modelo 3D propio salvo Nerida Neuland y Olive Mapleton (scratchpad/ref/scouts-vr/): el
frente sale del retrato y el perfil y la espalda se deducen de cómo cae ese peinado. El sexo, de su ficha de la wiki.
Usa las ayudas de la tanda 09 de IE1 (dome, hl, face) y algunas de otras tandas, sin editarlas."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars_scouts_ie1_03 import blush, freckles, rect_specs, round_specs, thick_brows, side_brow  # noqa: F401
from chars_scouts_ie1_09 import _c, dome, face, face_side, hl, mark  # noqa: F401
from chars_scouts_ie2_03 import curls, ears_pointy, round_glasses  # noqa: F401
from chars_scouts_ie3_02 import bowl3, hood, scarf  # noqa: F401
from chars_vr_nikogawa import brow_side, brows, crop, ring_glasses  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401

K = 'scouts-vr:'
WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)
TEAR = (150, 200, 240, 255)


def F(**k):
    d = {'eyes': 'normal', 'mouth': 'line'}
    d.update(k)
    return d


def P(hair, skin, iris='#302232', **k):
    return pal(hair, skin, iris, **k)


def C(pid, body, palette, f, front, side, back):
    """Como en las tandas anteriores: el nacimiento del pelo baja por el borde de la cara para que su raya no cruce el pelo."""
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[K + pid] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def arc_hl(side=64, top=42, x0=14, x1=86):
    """Nacimiento del pelo en arco liso (frente despejada)."""
    return [(x0 - 8, side), (x0 + 4, top + 10), (30, top + 2), (50, top), (70, top + 2), (x1 - 4, top + 10), (x1 + 8, side)]


def fringe_hl(y=58, side=66, n=6, tip=4, x0=16, x1=84, lean=0.0):
    """Flequillo de mechones a la altura y (puntas tip más abajo)."""
    return hl(n, side, y - tip, y, x0, x1, lean)


def puff(cx, cy, rx, ry, c='mid', z='b'):
    return L(blob(ell(cx, cy, rx, ry), 6), c, z)


def bun(cx, cy, r, c='mid', z='b'):
    return L(ell(cx, cy, r, r), c, z)


# ------------------------------------------------------------------ jugadores

# Mirko Harding (portero): melena corta muy rizada rosa fresa que abulta a los lados hasta las mejillas, frente despejada
# con un rizo en medio; cara redonda y clara con rubor, ojos azules grandes y boca pequeña
C('mirko-harding', 'normal', P('#ea5a7a', '#fbe0d4', '#5a9ad0', shade='#c63e60'),
  F(eyes='big', brows=True, mouth='line', mouth_y=92, hairline=arc_hl(66, 40)),
  dome('front', top=2, w=50, cy=46, n=9, amp=4, soft=True, sb=84, seed=3) + blush(88, 22),
  dome('side', top=2, w=48, cy=46, n=9, amp=4, soft=True, nape=90, fr=44, seed=3),
  dome('back', top=2, w=50, cy=46, n=9, amp=4, soft=True, nape=90, seed=3))

# Misia Cheveuse: pelo corto castaño claro con las puntas más oscuras, abierto en mechones de punta hacia los lados y
# flequillo barrido hacia arriba; ojos azules con pestañas, rubor y sonrisa
C('misia-cheveuse', 'chica', P('#bea47a', '#f8d4b0', '#4a7ab8', shade='#8a6e4a', low='#6a5034'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=fringe_hl(52, 64, 5, 6, lean=3)),
  dome('front', top=2, w=48, cy=44, n=7, amp=6, sb=70, seed=11, sweep=0.2) +
  [L(outline([(4, 64), (-6, 70, 1), (8, 56)]), 'low', 'f'), L(outline([(96, 64), (106, 70, 1), (92, 56)]), 'low', 'f')] + blush(87, 22),
  dome('side', top=2, w=46, cy=44, n=7, amp=6, nape=84, fr=48, seed=11),
  dome('back', top=2, w=48, cy=44, n=7, amp=6, nape=82, seed=11))

# Monica Kinbird: melena blanquísima con dos rulos enormes que se abren hacia los lados a la altura de las mejillas;
# ojos cerrados con lágrimas y boquita triste
C('monica-kinbird', 'chica', P('#f4f2f6', '#fbe4dc', shade='#cfcbd8'),
  F(eyes='closed', brows=True, mouth='frown', mouth_y=93, hairline=[(8, 66), (20, 52), (34, 44), (50, 42), (66, 44), (80, 52), (92, 66)]),
  [puff(4, 74, 22, 14), puff(96, 74, 22, 14), puff(-14, 70, 8, 9, 'shade'), puff(114, 70, 8, 9, 'shade')] +
  dome('front', top=0, w=46, cy=44, sb=78, seed=1) +
  [mark([(30, 80), (33, 80), (34, 88), (30, 88)], TEAR), mark([(67, 80), (70, 80), (70, 88), (66, 88)], TEAR)],
  dome('side', top=0, w=46, cy=44, nape=84, fr=46, seed=1) + [puff(22, 74, 22, 14), puff(6, 72, 8, 9, 'shade')],
  [puff(4, 74, 22, 14), puff(96, 74, 22, 14)] + dome('back', top=0, w=46, cy=44, nape=86, seed=1))

# Montgomery Marchand (portero): pelo negro corto en pinchos que asoman a los lados bajo una cinta blanca en la frente;
# piel morena, cara ancha de mandíbula fuerte, cejas gruesas fruncidas y ojos azules afilados
C('montgomery-marchand', 'corpulento', P('#1e2422', '#b07a52', '#4a8ac8', shade='#0e1210'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, face_front=face(4, 104, 4), hairline=[(8, 62), (20, 46), (50, 42), (80, 46), (92, 62)]),
  dome('front', top=8, w=46, cy=48, n=7, amp=5, sb=72, seed=5) +
  [L(blob([(8, 44), (30, 36), (50, 34), (70, 36), (92, 44), (92, 54), (70, 46), (50, 44), (30, 46), (8, 54)], 6), WHITE, 'f')] +
  thick_brows(64, 'deep', 4.2, tilt=1.2),
  dome('side', top=8, w=44, cy=48, n=7, amp=5, nape=86, fr=50, seed=5) +
  [L(blob([(4, 36), (40, 34), (86, 38), (88, 48), (40, 44), (4, 46)], 6), WHITE, 'f')],
  dome('back', top=8, w=46, cy=48, n=7, amp=5, nape=86, seed=5) +
  [L(blob([(4, 40), (50, 36), (96, 40), (96, 50), (50, 46), (4, 50)], 6), WHITE, 'f')])

# Montoodle Wixley: melena morada en casco con el flequillo recto que le tapa hasta los ojos; piel tostada con pecas,
# ojos entornados bajo el flequillo y una sonrisa de dientes
C('montoodle-wixley', 'normal', P('#9a5a92', '#d8a272', shade='#74406e'),
  F(eyes='closed', brows=False, mouth='grin', mouth_y=94, eye_y=80, hairline=[(8, 74), (92, 74)]),
  bowl3('front', top=10, side=92, w=2, fringe=74) + freckles(86, 24),
  bowl3('side', top=10, nape=96, w=2, fringe=72),
  bowl3('back', top=10, nape=96, w=2))

# Mora Grimmoir: melena larga naranja con las puntas vueltas hacia fuera y un flequillo espeso que le tapa los ojos;
# sonrisa suave
C('mora-grimmoir', 'chica', P('#e2602a', '#f8d6b8', shade='#b4441c'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=93, hairline=False),
  dome('front', top=0, w=48, cy=44, long=118, flare=10, seed=2) +
  [L(outline([(14, 82), (12, 50), (28, 34), (50, 30), (72, 34), (88, 50), (86, 82), (76, 78), (62, 80), (50, 78), (38, 80), (24, 78)]), 'mid', 'f')],
  dome('side', top=0, w=46, cy=44, long=118, flare=10, fr=80, seed=2),
  dome('back', top=0, w=48, cy=44, long=118, flare=10, ends=5, seed=2))

# Morrigan Shutterly: afro enorme morado muy oscuro, de bultos redondos, con mechones que le caen sobre la frente; ojos en
# espiral (gafas de cristal gris) y una sonrisa leve
C('morrigan-shutterly', 'chica', P('#3e2440', '#f8e0c0', shade='#28162a'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=93, hairline=fringe_hl(60, 70, 5, 8)),
  dome('front', top=-12, w=62, cy=44, n=12, amp=7, soft=True, sb=84, seed=7) +
  round_glasses('front', OUTC, 77, 14, 7.2, lens=(196, 190, 186, 255), w=1.6) +
  [L(ell(36, 77, 3.4, 3.4) + [ell(36, 77, 3.4, 3.4)[0]], (110, 100, 96, 255), 'f', False, False, 1.0),
   L(ell(64, 77, 3.4, 3.4) + [ell(64, 77, 3.4, 3.4)[0]], (110, 100, 96, 255), 'f', False, False, 1.0)],
  dome('side', top=-12, w=60, cy=44, n=12, amp=7, soft=True, nape=96, fr=58, seed=7) + round_glasses('side', OUTC, 77, r=7.2, lens=(196, 190, 186, 255), w=1.6),
  dome('back', top=-12, w=62, cy=44, n=12, amp=7, soft=True, nape=96, seed=7))

# Murray Hollowpot: pelo verde oscuro enorme y abultado como una seta, que cae en bucles gruesos por los lados hasta la
# mandíbula; ojos naranjas de párpado caído y boca seria
C('murray-hollowpot', 'normal', P('#2e5446', '#f6d4b6', '#e07a2a', shade='#1e3a30'),
  F(eyes='sharp', brows=True, mouth='line', mouth_y=94, hairline=fringe_hl(56, 66, 5, 6, lean=-2)),
  dome('front', top=-8, w=56, cy=40, n=10, amp=6, soft=True, sb=96, seed=9) + [puff(10, 90, 10, 12), puff(90, 90, 10, 12)],
  dome('side', top=-8, w=54, cy=40, n=10, amp=6, soft=True, nape=98, fr=52, seed=9),
  dome('back', top=-8, w=56, cy=40, n=10, amp=6, soft=True, nape=98, seed=9))

# Nadia Watershed: melena corta castaño rojizo, abombada, hasta la mandíbula, con la raya en medio y el flequillo abierto
# en dos; ojos grises oscuros y sonrisa
C('nadia-watershed', 'chica', P('#b8583a', '#fbe2d0', '#4a4a64', shade='#8e3e26'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=92, hairline=[(8, 70), (18, 60), (34, 54), (48, 44), (52, 44), (66, 54), (82, 60), (92, 70)]),
  bowl3('front', top=2, side=90, w=6, fringe=64) + [L([(50, 6), (50, 44)], 'shade', 'f', False, False, 1.4)],
  bowl3('side', top=2, nape=94, w=6, fringe=58),
  bowl3('back', top=2, nape=94, w=6))

# Nance Meridian: melena larga y ondulada gris parduzco hasta los hombros, con la raya en medio y una diadema amarilla;
# gafas redondas finas, ojos grises y sonrisa abierta
YEL = _c('#e0c050')
C('nance-meridian', 'chica', P('#9a8a7c', '#e8b892', '#6a6a6a', shade='#74665a'),
  F(eyes='normal', brows=True, mouth='grin', mouth_y=94, hairline=[(8, 66), (20, 52), (36, 46), (50, 40), (64, 46), (80, 52), (92, 66)]),
  dome('front', top=0, w=50, cy=44, n=9, amp=4, soft=True, long=114, flare=14, seed=4) +
  [L(quad((18, 30), (50, 4), (82, 30)), YEL, 'f', False, False, 3.0)] + round_glasses('front', OUTC, 76, 14, 8.5, w=1.3),
  dome('side', top=0, w=48, cy=44, n=9, amp=4, soft=True, long=114, flare=14, fr=46, seed=4) +
  [L(quad((50, 2), (70, 4), (82, 24)), YEL, 'f', False, False, 3.0)] + round_glasses('side', OUTC, 76, r=8.5, w=1.3),
  dome('back', top=0, w=50, cy=44, n=9, amp=4, soft=True, long=114, flare=14, ends=5, seed=4))

# Nasser Pryce: melena lisa naranja hasta los hombros, con la frente despejada en pico y dos coletitas en lo alto atadas
# con gomas negras; cejas naranjas levantadas, ojos verdes con lágrimas y sonrisa
C('nasser-pryce', 'normal', P('#ec6a2a', '#fbd8bc', '#9ac83a', shade='#c24c18'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=[(8, 70), (18, 50), (32, 44), (50, 56), (68, 44), (82, 50), (92, 70)]),
  [puff(20, 2, 10, 12), puff(80, 2, 10, 12), L(ell(24, -6, 3, 3), BLACK, 'b'), L(ell(76, -6, 3, 3), BLACK, 'b')] +
  dome('front', top=2, w=48, cy=44, long=104, flare=4, seed=6) +
  [mark([(30, 82), (34, 82), (33, 89), (29, 88)], TEAR), mark([(66, 82), (70, 82), (71, 88), (67, 89)], TEAR)],
  [puff(46, 0, 12, 12)] + dome('side', top=2, w=46, cy=44, long=104, flare=4, fr=46, seed=6),
  [puff(20, 2, 10, 12), puff(80, 2, 10, 12)] + dome('back', top=2, w=48, cy=44, long=104, flare=4, ends=4, seed=6))

# Naya Prism: melena larga verde azulado muy ondulada y abultada, echada hacia un lado; piel morena, cejas gruesas del color
# del pelo fruncidas, ojos verde grisáceo y boca seria
C('naya-prism', 'chica', P('#3e8a72', '#9a6442', '#9aa880', shade='#2a6654'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=94, hairline=[(8, 66), (16, 48), (32, 40), (50, 38), (66, 42), (84, 50), (92, 66)]),
  dome('front', top=-4, w=56, cy=42, n=9, amp=6, soft=True, long=112, flare=12, sweep=-0.3, seed=12) + brows(64, 'mid', 4.0, tilt=1.4),
  dome('side', top=-4, w=54, cy=42, n=9, amp=6, soft=True, long=112, flare=12, fr=44, seed=12) + brow_side(64, 'mid', 4.0, 1.0),
  dome('back', top=-4, w=56, cy=42, n=9, amp=6, soft=True, long=112, flare=12, ends=5, seed=12))

# Nerida Neuland: pelo negro corto pegado y peinado hacia atrás con la raya en medio y la frente despejada (adulta); ojos
# gris azulado y una sonrisa leve
C('nerida-neuland', 'chica', P('#24262e', '#fbe2d0', '#46566e', shade='#14161c'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=93, hairline=[(10, 66), (16, 46), (32, 36), (50, 34), (68, 36), (84, 46), (90, 66)]),
  crop('front', top=0, side=72, w=4),
  crop('side', top=0, nape=88, w=4) + [bun(8, 60, 9)],
  crop('back', top=0, nape=88, w=4) + [bun(50, 64, 10)])

# Neve Paisley: melena corta ondulada rosa melocotón hasta la mandíbula con la raya en medio; cejas gruesas rosadas, ojos
# rosas con pestañas y sonrisa
C('neve-paisley', 'chica', P('#e8a28a', '#fbe4d8', '#c86a8a', shade='#c47e68'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=[(8, 66), (20, 50), (36, 42), (50, 38), (64, 42), (80, 50), (92, 66)]),
  dome('front', top=2, w=50, cy=46, n=9, amp=4, soft=True, sb=94, seed=8) + brows(63, 'shade', 3.4) +
  [L([(50, 6), (50, 38)], 'shade', 'f', False, False, 1.2)],
  dome('side', top=2, w=48, cy=46, n=9, amp=4, soft=True, nape=96, fr=44, seed=8) + brow_side(63, 'shade', 3.4),
  dome('back', top=2, w=50, cy=46, n=9, amp=4, soft=True, nape=96, seed=8))

# Nico Kensee: melena malva lisa con flequillo de mechones finos y dos mechones largos a los lados hasta la barbilla; ojos
# gris azulado y boca neutra
C('nico-kensee', 'normal', P('#c2708a', '#fbe2d4', '#4a5a7a', shade='#94506a'),
  F(eyes='normal', brows=True, mouth='line', mouth_y=93, hairline=fringe_hl(64, 72, 6, 8, lean=-2)),
  dome('front', top=2, w=48, cy=44, long=100, flare=2, seed=10),
  dome('side', top=2, w=46, cy=44, nape=90, fr=60, seed=10),
  dome('back', top=2, w=48, cy=44, nape=92, seed=10))

# Nicolas Pirrant: un afro enorme y alto verde oscuro, de bultos redondos; piel morena, ojos redondos azules y boca
# pequeña
C('nicolas-pirrant', 'normal', P('#2e5a32', '#8e5a3a', '#3a5a9a', shade='#1e3e22'),
  F(eyes='round', brows=True, mouth='line', mouth_y=93, hairline=fringe_hl(60, 66, 6, 4)),
  dome('front', top=-24, w=58, cy=30, n=13, amp=6, soft=True, sb=70, seed=13),
  dome('side', top=-24, w=56, cy=30, n=13, amp=6, soft=True, nape=78, fr=54, seed=13),
  dome('back', top=-24, w=58, cy=30, n=13, amp=6, soft=True, nape=78, seed=13))

# Niles Gawkerson: pelo azul revuelto con mechones sobre la frente y las puntas rizadas amarillo anaranjado a los lados;
# unas gafas de visera rosa enormes con montura negra le tapan los ojos; piel morena y sonrisa abierta
PINK, GOLD = _c('#f04aa0'), _c('#f2b030')


def _visor(view):
    if view == 'front':
        return [L(blob([(10, 70), (30, 66), (50, 70), (70, 66), (90, 70), (92, 82), (70, 86), (50, 82), (30, 86), (8, 82)], 4), BLACK, 'f'),
                L(blob([(16, 72), (32, 69), (50, 73), (68, 69), (84, 72), (84, 80), (68, 83), (50, 80), (32, 83), (16, 80)], 4), PINK, 'f', False)]
    if view == 'side':
        return [L(blob([(40, 70), (88, 66), (92, 82), (40, 82)], 4), BLACK, 'f'), L(blob([(66, 70), (88, 69), (89, 80), (66, 80)], 4), PINK, 'f', False)]
    return [L([(6, 74), (50, 72), (94, 74)], BLACK, 'f', False, False, 3.0)]


C('niles-gawkerson', 'normal', P('#2a6ab8', '#9a6444', shade='#1c4a8a', light='#f2b030'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=94, hairline=fringe_hl(58, 66, 5, 8, lean=4)),
  [puff(8, 82, 11, 10, 'light'), puff(92, 82, 11, 10, 'light')] + dome('front', top=0, w=48, cy=44, n=8, amp=6, sb=74, seed=14) + _visor('front'),
  [puff(20, 84, 13, 10, 'light')] + dome('side', top=0, w=46, cy=44, n=8, amp=6, nape=84, fr=54, seed=14) + _visor('side'),
  [puff(14, 84, 13, 10, 'light'), puff(86, 84, 13, 10, 'light')] + dome('back', top=0, w=48, cy=44, n=8, amp=6, nape=84, seed=14) + _visor('back'))

# Niro Vannaburg: cabeza grande y redonda con el pelo gris rapado casi al cero; piel tostada, orejas grandes, ojos redondos
# y una sonrisa de oreja a oreja
C('niro-vannaburg', 'corpulento', P('#8a8a8c', '#eeaa7c', shade='#6a6a6e'),
  F(eyes='round', brows=True, mouth='smile', mouth_w=12, mouth_y=92, big_ears=2, face_front=face(4, 104, 2), hairline=arc_hl(56, 34, 16, 84)),
  crop('front', top=2, side=60, w=0),
  crop('side', top=2, nape=78, w=0),
  crop('back', top=2, nape=80, w=0))

# Nivea Etoile: pelo gris claro recogido en una trenza que le rodea toda la cabeza como una corona, con unos mechones
# sueltos sobre la frente; ojos gris azulado claro, piel muy clara, rubor y boca seria
C('nivea-etoile', 'chica', P('#c4c4c8', '#fbe8e0', '#9aa6be', shade='#9a9aa2'),
  F(eyes='big', brows=True, mouth='line', mouth_y=93, hairline=[(10, 66), (18, 48), (32, 40), (50, 40), (68, 40), (82, 48), (90, 66)]),
  dome('front', top=-2, w=46, cy=46, sb=74, seed=15) +
  [L(blob([(8, 50), (20, 14), (50, 0), (80, 14), (92, 50), (84, 52), (76, 22), (50, 10), (24, 22), (16, 52)], 6), 'shade', 'f', False)] +
  [L([(50, 2), (50, 40)], 'shade', 'f', False, False, 1.2), strand([(40, 40), (36, 52)], 'mid', 'f', 2.0), strand([(62, 40), (66, 52)], 'mid', 'f', 2.0)] + blush(87, 22),
  dome('side', top=-2, w=44, cy=46, nape=86, fr=46, seed=15) + [L(blob([(10, 60), (8, 24), (40, 4), (76, 12), (70, 20), (40, 14), (18, 30), (20, 62)], 6), 'shade', 'f', False)],
  dome('back', top=-2, w=46, cy=46, nape=86, seed=15) + [L(blob([(8, 54), (20, 16), (50, 2), (80, 16), (92, 54), (80, 70), (50, 78), (20, 70)], 6), 'shade', 'f', False)])

# Noelle Harmon: dos coletas enormes y esponjosas castaño claro que le abultan a los lados casi tanto como la cabeza, con un
# rizo de antena arriba y flequillo en pico; tres lunares en la frente sobre cada ojo, ojos cerrados y mucho rubor
DOT = _c('#8a5a3e')
C('noelle-harmon', 'chica', P('#c4a490', '#fbe0d0', shade='#9a7a66'),
  F(eyes='closed', brows=False, mouth='line', mouth_y=93, hairline=[(8, 66), (20, 52), (36, 46), (50, 56), (64, 46), (80, 52), (92, 66)]),
  [puff(-6, 70, 22, 32), puff(106, 70, 22, 32), puff(-10, 82, 14, 18, 'shade'), puff(110, 82, 14, 18, 'shade')] +
  dome('front', top=2, w=46, cy=44, sb=72, seed=16) + [L(quad((52, 4), (60, -14), (66, -6)), 'mid', 'f', False, False, 3.0)] +
  [L(ell(x, y, 2.2, 2.2), DOT, 'f', False) for x, y in ((28, 64), (34, 61), (40, 64), (60, 64), (66, 61), (72, 64))] + blush(86, 22, 5.5),
  [puff(14, 72, 24, 32)] + dome('side', top=2, w=44, cy=44, nape=84, fr=50, seed=16) + [L(quad((48, 2), (54, -16), (62, -8)), 'mid', 'f', False, False, 3.0)],
  [puff(-6, 70, 22, 32), puff(106, 70, 22, 32)] + dome('back', top=2, w=46, cy=44, nape=84, seed=16))

# Nolan Ashby: melena negra azulada lisa y larga hasta los hombros, abombada arriba con el flequillo echado hacia los
# lados; ojos cerrados bajo cejas gruesas y boca seria
C('nolan-ashby', 'normal', P('#1c2234', '#f6cfa8', shade='#0e1220'),
  F(eyes='closed', brows='angry', mouth='frown', mouth_y=94, hairline=[(10, 66), (18, 54), (32, 52), (44, 46), (56, 46), (68, 52), (82, 54), (90, 66)]),
  dome('front', top=-2, w=48, cy=44, long=112, flare=4, seed=17),
  dome('side', top=-2, w=46, cy=44, long=112, flare=4, fr=56, seed=17),
  dome('back', top=-2, w=48, cy=44, long=112, flare=4, ends=3, seed=17))

# Norah Noshawn: melena corta añil oscuro con el flequillo recto de mechones que le llega a las cejas y las puntas hacia
# dentro; ojos azules y boca seria
C('norah-noshawn', 'chica', P('#2e2a5e', '#fbe4d8', '#3a5a9a', shade='#1e1a40'),
  F(eyes='big', brows=False, mouth='line', mouth_y=93, hairline=fringe_hl(66, 74, 7, 6)),
  bowl3('front', top=2, side=94, w=6, fringe=66),
  bowl3('side', top=2, nape=94, w=6, fringe=64),
  bowl3('back', top=2, nape=94, w=6))

# Norma Paranon: pelo granate con el flequillo echado de lado y dos coletas en tirabuzón muy gruesas a los lados, atadas
# con gomas rojas; ojos rosas con pestañas y la boca abierta en una sonrisa
RED = _c('#d02838')
C('norma-paranon', 'chica', P('#7a3654', '#fbe0d0', '#e0408a', shade='#5a2440'),
  F(eyes='big', brows=True, mouth='grin', mouth_y=94, hairline=[(8, 66), (18, 52), (30, 50), (46, 62), (60, 46), (76, 46), (92, 66)]),
  [puff(-2, 66, 12, 12), puff(-4, 84, 12, 11), puff(-2, 100, 10, 9), puff(102, 66, 12, 12), puff(104, 84, 12, 11), puff(102, 100, 10, 9),
   L(ell(8, 52, 4, 4), RED, 'b'), L(ell(92, 52, 4, 4), RED, 'b')] +
  dome('front', top=0, w=46, cy=44, sb=72, seed=18, sweep=0.2),
  [puff(20, 70, 12, 12), puff(18, 88, 12, 11), puff(20, 104, 10, 9)] + dome('side', top=0, w=44, cy=44, nape=84, fr=52, seed=18),
  [puff(-2, 66, 12, 12), puff(-4, 84, 12, 11), puff(-2, 100, 10, 9), puff(102, 66, 12, 12), puff(104, 84, 12, 11), puff(102, 100, 10, 9)] +
  dome('back', top=0, w=46, cy=44, nape=84, seed=18))

# Nova Holloway (portera): melena gris en casco con flequillo recto de mechones y las puntas abiertas hacia fuera a la
# altura de la barbilla; gafas negras rectangulares y boca seria
C('nova-holloway', 'chica', P('#a2a2a4', '#f8d8c0', '#4a4a4a', shade='#7e7e82'),
  F(eyes='normal', brows=False, mouth='frown', mouth_y=94, hairline=fringe_hl(62, 70, 7, 6)),
  bowl3('front', top=0, side=94, w=8, fringe=62) + [L(outline([(2, 92), (-8, 98, 1), (10, 84)]), 'mid', 'b'), L(outline([(98, 92), (108, 98, 1), (90, 84)]), 'mid', 'b')] +
  rect_specs('front', BLACK, 76, 14, 2.4),
  bowl3('side', top=0, nape=96, w=8, fringe=60) + rect_specs('side', BLACK, 76, w=2.4),
  bowl3('back', top=0, nape=96, w=8))

# Octavia Carroll: melena larga y ondulada castaño grisáceo hasta la cintura, con la frente despejada en pico y dos
# horquillas verdes; ojos ámbar con lágrimas y sonrisa
GREEN = _c('#3ab040')
C('octavia-carroll', 'chica', P('#5e544e', '#fbe2d4', '#b8902a', shade='#433b36'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=[(8, 70), (18, 50), (34, 42), (50, 50), (64, 42), (82, 50), (92, 70)]),
  dome('front', top=-2, w=50, cy=44, n=8, amp=3, soft=True, long=124, flare=12, seed=19) +
  [L(blob([(10, 40), (18, 36), (16, 46)], 3), GREEN, 'f'), L(blob([(90, 40), (82, 36), (84, 46)], 3), GREEN, 'f'),
   mark([(32, 82), (35, 82), (35, 89), (31, 89)], TEAR), mark([(65, 82), (68, 82), (69, 89), (65, 89)], TEAR)],
  dome('side', top=-2, w=48, cy=44, n=8, amp=3, soft=True, long=124, flare=12, fr=46, seed=19),
  dome('back', top=-2, w=50, cy=44, n=8, amp=3, soft=True, long=124, flare=12, ends=5, seed=19))

# Octavian da Lua: gorro de punto marrón con manchas claras calado hasta la frente y una melena lisa roja que le cae hasta
# el pecho y le tapa un ojo; se le ve un solo ojo cansado y la boca seria
BROWNH, PATCH = _c('#8a6a44'), _c('#c4a886')


def _beanie_ol(view):
    if view == 'front':
        return [L(outline([(10, 60), (8, 30), (24, 6), (50, -4), (76, 6), (92, 30), (90, 60), (70, 56), (50, 58), (30, 56)]), BROWNH, 'f'),
                L(blob([(12, 50), (30, 48), (50, 52), (70, 48), (88, 50), (88, 58), (50, 60), (12, 58)], 4), PATCH, 'f', False)]
    if view == 'side':
        return [L(outline([(86, 58), (90, 30), (74, 4), (46, -6), (18, 6), (2, 32), (4, 62), (40, 58)]), BROWNH, 'f'),
                L(blob([(6, 52), (46, 50), (88, 50), (88, 58), (6, 60)], 4), PATCH, 'f', False)]
    return [L(outline([(8, 62), (6, 30), (24, 6), (50, -4), (76, 6), (94, 30), (92, 62), (50, 66)]), BROWNH, 'f'),
            L(blob([(8, 52), (50, 56), (92, 52), (92, 62), (50, 66), (8, 62)], 4), PATCH, 'f', False)]


C('octavian-da-lua', 'normal', P('#b83030', '#f2c8a2', '#4a4a6a', shade='#8a2020'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=95, hairline=False),
  dome('front', top=2, w=46, cy=44, long=122, flare=4, seed=20) +
  [L(outline([(48, 56), (88, 56), (92, 80), (90, 116), (76, 120, 1), (66, 104), (58, 84)]), 'mid', 'f')] + _beanie_ol('front') +
  [L(ell(36, 76, 5, 4.4), WHITE, 'f', False), L(ell(37, 77, 3, 3), (60, 60, 90, 255), 'f', False), L([(30, 72), (42, 72)], OUTC, 'f', False, False, 2.2)],
  dome('side', top=2, w=44, cy=44, long=122, flare=4, fr=60, seed=20) + _beanie_ol('side'),
  dome('back', top=2, w=46, cy=44, long=122, flare=4, ends=4, seed=20) + _beanie_ol('back'))

# Olan Ackroyd: pelo rojo peinado hacia atrás con pinchos hacia fuera a los lados de la cabeza; piel morena rojiza, unas
# marcas rojas sobre los ojos, ojos ámbar afilados y sonrisa torcida
REDM = _c('#d83a3a')
C('olan-ackroyd', 'normal', P('#d83444', '#8e4c3c', '#e0a020', shade='#a82030'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=95, face_front=face(2, 102, 2), hairline=[(8, 62), (16, 44), (32, 34), (50, 40), (68, 34), (84, 44), (92, 62)]),
  dome('front', top=2, w=46, cy=44, sb=66, seed=21) +
  [L(outline([(6, 56), (-10, 60, 1), (4, 48), (-8, 46, 1), (8, 40)]), 'mid', 'b'), L(outline([(94, 56), (110, 60, 1), (96, 48), (108, 46, 1), (92, 40)]), 'mid', 'b'),
   mark([(26, 64), (40, 66), (40, 69), (26, 67)], REDM), mark([(74, 64), (60, 66), (60, 69), (74, 67)], REDM)],
  dome('side', top=2, w=44, cy=44, nape=84, fr=40, seed=21) + [L(outline([(10, 60), (-8, 66, 1), (4, 50), (-6, 46, 1), (12, 44)]), 'mid', 'b')],
  dome('back', top=2, w=46, cy=44, nape=84, seed=21) +
  [L(outline([(6, 60), (-10, 64, 1), (4, 50), (-8, 48, 1), (8, 42)]), 'mid', 'b'), L(outline([(94, 60), (110, 64, 1), (96, 50), (108, 48, 1), (92, 42)]), 'mid', 'b')])

# Olive Mapleton: tupé alto rosa salmón, un lado de la cabeza rapado gris y por el otro un mechón ondulado verde menta que le
# cae hasta la mandíbula (modelo 3D); ojos verde grisáceo y sonrisa pícara
SAL, MINT, SHAV = _c('#ee7a6e'), _c('#6ae0a0'), _c('#a0a0a4')
C('olive-mapleton', 'chica', P('#ee7a6e', '#f6c8a0', '#7a9a6a', shade='#c85a50'),
  F(eyes='big', brows='angry', mouth='smile', mouth_y=93, hairline=[(8, 62), (18, 46), (34, 40), (50, 40), (66, 40), (82, 46), (92, 62)]),
  [L(outline([(80, 64), (88, 40), (82, 20), (70, 20), (72, 50)]), SHAV, 'b')] +
  [L(outline([(16, 40), (22, 8), (44, -6), (72, -2), (88, 14), (84, 30), (60, 30), (34, 34)]), SAL, 'f'),
   L(outline([(30, 30), (12, 34), (2, 50), (6, 70), (2, 86), (14, 94), (26, 84), (24, 66), (30, 52), (40, 42)]), MINT, 'f')],
  [L(outline([(4, 40), (20, 10), (50, -6), (82, 2), (90, 20), (60, 30), (30, 30)]), SAL, 'f'),
   L(outline([(4, 34), (40, 30), (54, 46), (52, 70), (44, 86), (24, 92), (8, 80), (0, 58)]), MINT, 'f')],
  [L(outline([(10, 70), (8, 40), (20, 20), (50, 18), (80, 20), (92, 40), (90, 70), (50, 84)]), SHAV, 'b'),
   L(outline([(20, 30), (24, 4), (50, -6), (76, 4), (80, 30), (50, 40)]), SAL, 'f'),
   L(outline([(80, 30), (98, 40), (100, 60), (94, 80), (84, 70), (82, 50)]), MINT, 'f')])

# Olivier Gourmand: corte de tazón ciruela muy oscuro, abombado como una seta, con el flequillo recto sobre las cejas; cejas
# gruesas, ojos celeste claro y boca pequeña
C('olivier-gourmand', 'normal', P('#3a2838', '#f8dcc4', '#8ac8e0', shade='#24161f'),
  F(eyes='big', brows=False, mouth='line', mouth_y=93, hairline=[(8, 64), (92, 64)]),
  bowl3('front', top=-2, side=74, w=10, fringe=64) + thick_brows(64, 'deep', 3.4),
  bowl3('side', top=-2, nape=86, w=10, fringe=62),
  bowl3('back', top=-2, nape=86, w=10))

# Oralyn Everfable: pelo añil hasta los hombros con mechones de punta vueltos hacia fuera y la frente despejada con la raya
# en medio; ojos grises grandes con pestañas, rubor y labios oscuros
C('oralyn-everfable', 'chica', P('#3a3a8c', '#fbe2d6', '#6a6a72', shade='#26266a'),
  F(eyes='big', brows='angry', mouth='lips', mouth_w=6, mouth_y=94, hairline=[(8, 66), (18, 46), (34, 40), (50, 46), (66, 40), (82, 46), (92, 66)]),
  dome('front', top=0, w=46, cy=44, long=104, flare=12, seed=22) + blush(87, 22),
  dome('side', top=0, w=44, cy=44, long=104, flare=12, fr=46, seed=22),
  dome('back', top=0, w=46, cy=44, long=104, flare=12, ends=3, seed=22))

# Ordin Scriben: pelo gris verdoso corto y bien peinado, abultado arriba; piel tostada, gafas redondas negras, cejas
# fruncidas y boca seria
C('ordin-scriben', 'normal', P('#5a6a66', '#cc946c', '#3a3030', shade='#3e4c48'),
  F(eyes='normal', brows='angry', mouth='frown', mouth_y=94, hairline=[(10, 64), (18, 46), (34, 40), (50, 40), (66, 40), (82, 46), (90, 64)]),
  dome('front', top=-4, w=48, cy=42, sb=68, seed=23) + ring_glasses('front', 76, OUTC, 2.4),
  dome('side', top=-4, w=46, cy=42, nape=84, fr=42, seed=23) + ring_glasses('side', 76, OUTC, 2.4),
  dome('back', top=-4, w=48, cy=42, nape=84, seed=23))

# Orlando Sterlight (portero): pelo azul marino corto con mechas rosas, un mechón grande que se enrosca hacia arriba en lo
# alto y el flequillo sobre la frente; ojos redondos con aros blancos y sonrisa
PNK = _c('#f08aa8')
C('orlando-sterlight', 'normal', P('#22224a', '#fbe0d0', '#2a2a3a', shade='#14142e'),
  F(eyes='round', brows=True, mouth='smile', mouth_y=93, hairline=fringe_hl(60, 66, 5, 6, lean=-3)),
  dome('front', top=4, w=46, cy=44, sb=70, seed=24) +
  [L(quad((60, 6), (90, -14), (100, -2)), 'mid', 'f', False, False, 6.0), strand([(30, 10), (24, 40), (22, 66)], PNK, 'f', 3.0),
   strand([(70, 12), (78, 40), (80, 60)], PNK, 'f', 3.0)],
  dome('side', top=4, w=44, cy=44, nape=84, fr=56, seed=24) + [L(quad((60, 4), (84, -14), (94, -4)), 'mid', 'f', False, False, 6.0),
                                                              strand([(40, 14), (30, 40), (34, 66)], PNK, 'f', 3.0)],
  dome('back', top=4, w=46, cy=44, nape=84, seed=24) + [strand([(30, 14), (24, 50)], PNK, 'f', 3.0), strand([(70, 14), (76, 50)], PNK, 'f', 3.0)])

# Ottis Quisley (portero): melena corta ondulada beige hasta la mandíbula con dos mechones grises caídos como orejas de
# perro a los lados; ojos ámbar grandes y sonrisa
GREY = _c('#8a8a8a')
C('ottis-quisley', 'normal', P('#d8c8a0', '#f8d0a8', '#c07a2a', shade='#b0a07a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=fringe_hl(58, 66, 6, 6)),
  dome('front', top=2, w=50, cy=46, n=8, amp=3, soft=True, sb=96, seed=25) +
  [L(blob([(4, 54), (-4, 66), (0, 84), (8, 76), (10, 58)], 5), GREY, 'f'), L(blob([(96, 54), (104, 66), (100, 84), (92, 76), (90, 58)], 5), GREY, 'f')],
  dome('side', top=2, w=48, cy=46, n=8, amp=3, soft=True, nape=96, fr=50, seed=25) + [L(blob([(40, 50), (30, 62), (34, 82), (44, 72), (48, 56)], 5), GREY, 'f')],
  dome('back', top=2, w=50, cy=46, n=8, amp=3, soft=True, nape=96, seed=25) +
  [L(blob([(10, 52), (2, 64), (6, 82), (14, 74), (18, 58)], 5), GREY, 'f'), L(blob([(90, 52), (98, 64), (94, 82), (86, 74), (82, 58)], 5), GREY, 'f')])

# Ouijane Boarden: melena negra larguísima y ondulada con un lazo negro enorme en lo alto y una cinta blanca y rosa;
# flequillo recto, ojos morados con pestañas, piel muy clara y sonrisa de dientes
PALEPINK = _c('#e8b8c8')
C('ouijane-boarden', 'chica', P('#1e1e24', '#fbe8e2', '#7a5a9a', shade='#0e0e12'),
  F(eyes='big', brows=True, mouth='grin', mouth_y=94, hairline=fringe_hl(60, 70, 7, 4)),
  [puff(26, -8, 18, 12), puff(74, -8, 18, 12)] + dome('front', top=2, w=50, cy=44, n=9, amp=4, soft=True, long=126, flare=14, seed=26) +
  [L(quad((12, 32), (50, 4), (88, 32)), WHITE, 'f', False, False, 3.0), L(quad((14, 36), (50, 9), (86, 36)), PALEPINK, 'f', False, False, 2.0), L(ell(50, -6, 6, 6), 'mid', 'f')],
  [puff(46, -10, 18, 12)] + dome('side', top=2, w=48, cy=44, n=9, amp=4, soft=True, long=126, flare=14, fr=58, seed=26) +
  [L(quad((50, 2), (70, 6), (84, 30)), WHITE, 'f', False, False, 3.0)],
  [puff(26, -8, 18, 12), puff(74, -8, 18, 12)] + dome('back', top=2, w=50, cy=44, n=9, amp=4, soft=True, long=126, flare=14, ends=5, seed=26) + [L(ell(50, -6, 6, 6), 'mid', 'f')])

# Papilla Revert: pelo azul celeste muy claro con flequillo de mechones y unos tirabuzones ondulados que se abren hacia los
# lados por debajo de las orejas; ojos marrones, rubor y boca seria
C('papilla-revert', 'chica', P('#c8e4ee', '#fbe0cc', '#5a3a2a', shade='#9ab8c8'),
  F(eyes='big', brows=True, mouth='frown', mouth_y=94, hairline=fringe_hl(60, 68, 6, 8, lean=2)),
  [puff(4, 82, 16, 12), puff(96, 82, 16, 12), puff(-6, 90, 10, 9, 'shade'), puff(106, 90, 10, 9, 'shade')] +
  dome('front', top=0, w=48, cy=44, sb=82, seed=27) + blush(87, 22),
  [puff(20, 84, 18, 12)] + dome('side', top=0, w=46, cy=44, nape=86, fr=56, seed=27),
  [puff(4, 82, 16, 12), puff(96, 82, 16, 12)] + dome('back', top=0, w=48, cy=44, nape=86, seed=27))

# Patrice Kampanee: una nube de pelo rosa claro enorme y esponjosa encima de la cabeza, con un rizo en espiral; flequillo
# hasta las cejas, ojos azules y sonrisa
C('patrice-kampanee', 'normal', P('#e4aab2', '#fbe0cc', '#3a5aa8', shade='#c0848e'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=93, hairline=fringe_hl(62, 68, 6, 4)),
  dome('front', top=-16, w=58, cy=34, n=9, amp=7, soft=True, sb=66, seed=28) + [L(quad((52, -6), (68, -12), (64, 4)), 'shade', 'f', False, False, 3.0)],
  dome('side', top=-16, w=56, cy=34, n=9, amp=7, soft=True, nape=76, fr=56, seed=28),
  dome('back', top=-16, w=58, cy=34, n=9, amp=7, soft=True, nape=76, seed=28))

# Paxton Plumfield: pelo gris pizarra muy oscuro, corto a los lados y levantado arriba en un tupé hacia atrás; pecas,
# ojos marrones de párpado afilado y sonrisa
C('paxton-plumfield', 'normal', P('#3e3e48', '#f6cfae', '#4a3020', shade='#26262e'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=93, hairline=[(12, 64), (18, 46), (32, 40), (50, 42), (68, 40), (82, 46), (88, 64)]),
  crop('front', top=4, side=68, w=2) + [L(outline([(18, 30), (20, 2), (40, -14), (68, -12), (84, 4), (82, 30), (60, 26), (40, 28)]), 'mid', 'f')] + freckles(85, 22),
  crop('side', top=4, nape=86, w=2) + [L(outline([(24, 12), (36, -12), (66, -16), (90, 6), (86, 24), (60, 18)]), 'mid', 'f')],
  crop('back', top=4, nape=86, w=2) + [L(outline([(20, 24), (24, 0), (50, -14), (76, 0), (80, 24), (50, 30)]), 'mid', 'f')])

# Penelope Mozartin: melena naranja en casco hasta la barbilla con el flequillo recto y los lados en rulos horizontales
# apilados; ojos verdes con lágrimas, cejas finas y rubor
C('penelope-mozartin', 'chica', P('#f0962e', '#fbe2d0', '#5aa070', shade='#c8761c'),
  F(eyes='big', brows=True, mouth='line', mouth_y=93, hairline=[(8, 62), (92, 62)]),
  bowl3('front', top=4, side=96, w=8, fringe=62) +
  [L([(9, y), (17, y + 1)], 'shade', 'f', False, False, 1.6) for y in (70, 78, 86)] +
  [L([(91, y), (83, y + 1)], 'shade', 'f', False, False, 1.6) for y in (70, 78, 86)] +
  [mark([(32, 82), (35, 82), (35, 89), (31, 89)], TEAR), mark([(65, 82), (68, 82), (69, 89), (65, 89)], TEAR)] + blush(87, 22),
  bowl3('side', top=4, nape=96, w=8, fringe=60) + [L([(8, y), (40, y + 1)], 'shade', 'f', False, False, 1.6) for y in (70, 80, 90)],
  bowl3('back', top=4, nape=96, w=8) + [L([(8, y), (92, y)], 'shade', 'f', False, False, 1.6) for y in (72, 82, 92)])

# Pennie Pound: melena negra en casco abombada con el flequillo echado de lado; ojos rojos con grandes ojeras oscuras y
# una sonrisa de oreja a oreja
DARKC = _c('#6a4a3a')
C('pennie-pound', 'chica', P('#1c1c22', '#fbe2d0', '#c03030', shade='#0c0c10'),
  F(eyes='round', brows='angry', mouth='smile', mouth_w=14, mouth_y=94, hairline=[(8, 66), (18, 54), (30, 56), (44, 64), (56, 50), (72, 46), (92, 64)]),
  bowl3('front', top=-2, side=88, w=12, fringe=60) + [mark([(28, 80), (42, 80), (40, 86), (30, 86)], DARKC), mark([(58, 80), (72, 80), (70, 86), (60, 86)], DARKC)],
  bowl3('side', top=-2, nape=92, w=12, fringe=56),
  bowl3('back', top=-2, nape=92, w=12))

# Petra Cornerstone (portera): melena larga gris oscuro que le tapa un ojo y cae ondulada hasta la cintura, con una
# horquilla verde; piel morena, un ojo verde y boca de gato
C('petra-cornerstone', 'chica', P('#5a5654', '#b47c58', '#4ab090', shade='#3e3a38'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, hairline=False),
  dome('front', top=0, w=48, cy=44, n=7, amp=3, soft=True, long=124, flare=12, seed=29) +
  [L(outline([(12, 96), (10, 52), (24, 34), (50, 30), (72, 34), (82, 48), (62, 50), (58, 70), (56, 88), (44, 118, 1), (26, 108)]), 'mid', 'f'),
   L(blob([(66, 34), (78, 30), (76, 40)], 3), GREEN, 'f'),
   L(ell(66, 77, 5, 4.6), WHITE, 'f', False), L(ell(66, 78, 3, 3.2), _c('#4ab090'), 'f', False), L(quad((58, 70), (66, 66), (74, 70)), OUTC, 'f', False, False, 2.2)],
  dome('side', top=0, w=46, cy=44, n=7, amp=3, soft=True, long=124, flare=12, fr=50, seed=29),
  dome('back', top=0, w=48, cy=44, n=7, amp=3, soft=True, long=124, flare=12, ends=5, seed=29))

# Phoebe "Phibs" Soarsky: pelo blanco crema con un moño rosado en lo alto, flequillo recto de mechones y las puntas a la
# altura de la mandíbula abiertas hacia fuera; ojos azules, rubor y sonrisa
ROSE = _c('#e8bab4')
C('phoebe-phibs-soarsky', 'chica', P('#f6eee4', '#fbe2d4', '#3a4a7a', shade='#d8ccc2'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=fringe_hl(62, 70, 7, 6)),
  [bun(50, -10, 12, ROSE)] + dome('front', top=2, w=46, cy=44, sb=84, seed=30) +
  [L(outline([(6, 80), (-10, 88, 1), (14, 70)]), 'mid', 'f'), L(outline([(94, 80), (110, 88, 1), (86, 70)]), 'mid', 'f')] + blush(87, 22),
  [bun(44, -12, 12, ROSE)] + dome('side', top=2, w=44, cy=44, nape=86, fr=56, seed=30),
  [bun(50, -10, 12, ROSE)] + dome('back', top=2, w=46, cy=44, nape=86, seed=30))

# Pierce Castleton: cara enorme y ancha con el pelo castaño oscuro corto en pinchos y un pico en la frente; piel tostada,
# cejas fruncidas, ojos pequeños y la boca torcida hacia abajo
C('pierce-castleton', 'corpulento', P('#5a4e44', '#eeaa72', '#3a4a6a', shade='#3e342c'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_w=12, mouth_y=96, face_front=face(6, 104, 6), hairline=[(4, 60), (16, 46), (34, 44), (50, 56), (66, 44), (84, 46), (96, 60)]),
  dome('front', top=6, w=50, cy=46, n=8, amp=5, sb=62, seed=31),
  dome('side', top=6, w=48, cy=46, n=8, amp=5, nape=82, fr=46, seed=31),
  dome('back', top=6, w=50, cy=46, n=8, amp=5, nape=82, seed=31))

# Pietro Olley: gorro de lana rojo calado hasta las cejas; cejas negras muy gruesas, cara redonda con rubor, ojos pequeños y
# boca seria
REDB = _c('#c44a40')


def _beanie_red(view):
    if view == 'front':
        return [L(outline([(8, 66), (6, 34), (22, 8), (50, -2), (78, 8), (94, 34), (92, 66), (50, 62)]), REDB, 'f'),
                L(blob([(8, 54), (50, 50), (92, 54), (92, 66), (50, 62), (8, 66)], 4), _c('#a83a32'), 'f', False)] + \
               [L([(x, 6), (x * 0.9 + 5, 52)], _c('#a83a32'), 'f', False, False, 1.2) for x in (30, 50, 70)]
    if view == 'side':
        return [L(outline([(88, 62), (90, 32), (72, 4), (46, -6), (16, 8), (2, 36), (4, 66), (44, 62)]), REDB, 'f'),
                L(blob([(4, 56), (46, 52), (88, 52), (88, 62), (4, 66)], 4), _c('#a83a32'), 'f', False)]
    return [L(outline([(6, 68), (4, 34), (22, 8), (50, -2), (78, 8), (96, 34), (94, 68), (50, 72)]), REDB, 'f'),
            L(blob([(6, 58), (50, 62), (94, 58), (94, 68), (50, 72), (6, 68)], 4), _c('#a83a32'), 'f', False)]


C('pietro-olley', 'corpulento', P('#1e1a18', '#e8a87a', '#2a2020', shade='#0e0c0a'),
  F(eyes='dot', brows=False, mouth='frown', mouth_y=94, face_front=face(4, 102, 2), hairline=False),
  _beanie_red('front') + thick_brows(68, 'mid', 5.0, w=14) + blush(84, 26),
  _beanie_red('side') + side_brow(68, 'mid', 5.0),
  _beanie_red('back'))

# Pillan Hallstead (portero): tupé naranja tostado alto y abultado; cara larga y pálida, cejas negras muy gruesas y
# arqueadas, ojos violeta claro afilados y sonrisa confiada
C('pillan-hallstead', 'delgado', P('#d08a2a', '#fbe4d4', '#8a7ab0', shade='#a86818'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_w=12, mouth_y=96, face_front=face(0, 106, 0), hairline=[(12, 60), (18, 42), (34, 32), (50, 34), (66, 32), (82, 42), (88, 60)]),
  dome('front', top=-12, w=46, cy=34, n=8, amp=4, soft=True, sb=62, seed=32) + thick_brows(64, BLACK, 4.6, tilt=1.6, w=14),
  dome('side', top=-12, w=44, cy=34, n=8, amp=4, soft=True, nape=80, fr=34, seed=32) + side_brow(64, BLACK, 4.6, 1.0),
  dome('back', top=-12, w=46, cy=34, n=8, amp=4, soft=True, nape=80, seed=32))

# Pina Propp: melena castaña en forma de seta que le tapa las orejas, con el flequillo hasta las cejas; piel tostada, ojos
# verdes grandes, nariz roja y boca pequeña
C('pina-propp', 'chica', P('#7a4a2a', '#e8a87a', '#3aa060', shade='#5a321a'),
  F(eyes='big', brows=True, mouth='line', mouth_y=94, hairline=fringe_hl(62, 70, 6, 6), nose=(50, 84, 3.6)),
  bowl3('front', top=0, side=92, w=12, fringe=62) + [L(ell(50, 84, 3.4, 3.0), _c('#e06a4a'), 'f', False)],
  bowl3('side', top=0, nape=94, w=12, fringe=60),
  bowl3('back', top=0, nape=94, w=12))

# Pinn Persica: una mata de pelo rosa chicle esponjosa que le cae sobre un ojo, con los lados rapados plateados; cara
# arrugada, ojos entornados y sonrisa torcida
PINKC, SILV = _c('#f290c0'), _c('#c8c8cc')
C('pinn-persica', 'delgado', P('#f290c0', '#f6d8c0', '#4a5a6a', shade='#c86a98'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=95, face_front=face(0, 104, 0), hairline=False),
  [L(outline([(16, 66), (12, 40), (22, 22), (78, 22), (88, 40), (84, 66), (80, 50), (20, 50)]), SILV, 'b')] +
  [L(blob([(14, 34), (18, 6), (40, -10), (66, -8), (84, 8), (82, 30), (74, 52), (66, 66), (58, 62), (52, 44), (38, 40), (22, 44)], 6), 'mid', 'f'),
   L(quad((44, 6), (60, 0), (68, 20)), 'shade', 'f', False, False, 2.0)],
  [L(outline([(8, 30), (40, 20), (70, 30), (56, 60), (20, 70), (6, 56)]), SILV, 'b'),
   L(blob([(20, 20), (40, -8), (70, -8), (92, 14), (90, 40), (74, 50), (60, 30), (34, 30)], 6), 'mid', 'f')],
  [L(outline([(12, 70), (10, 40), (22, 22), (78, 22), (90, 40), (88, 70), (50, 80)]), SILV, 'b'),
   L(blob([(16, 30), (24, 2), (50, -10), (76, 2), (84, 30), (50, 40)], 6), 'mid', 'f')])

# Ponny Grace: melena larga y ondulada azul con reflejos más oscuros por dentro y la raya en medio; piel tostada, cara
# ancha, ojos pequeños con pestañas y sonrisa
C('ponny-grace', 'chica', P('#3e6c9a', '#e2a272', '#3a3a5a', shade='#24486e'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=94, face_front=face(4, 102, 2), hairline=[(6, 66), (18, 52), (34, 46), (50, 50), (66, 46), (82, 52), (94, 66)]),
  dome('front', top=-2, w=52, cy=44, n=9, amp=4, soft=True, long=116, flare=16, seed=33),
  dome('side', top=-2, w=50, cy=44, n=9, amp=4, soft=True, long=116, flare=16, fr=48, seed=33),
  dome('back', top=-2, w=52, cy=44, n=9, amp=4, soft=True, long=116, flare=16, ends=5, seed=33))

# Praiseton Strongshout (portero): pelo rojo coral en mechones que le caen en pico sobre la frente, con una capa de pinchos
# castaño oscuro por encima; ojos rojos afilados y sonrisa confiada
DARKB = _c('#5a3428')
C('praiseton-strongshout', 'normal', P('#d85a5a', '#fbe4d8', '#c03838', shade='#b03e40'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_w=12, mouth_y=95, hairline=[(8, 62), (18, 50), (32, 46), (50, 60), (68, 46), (82, 50), (92, 62)]),
  [L(outline([(8, 30), (4, 6, 1), (18, 12), (26, -12, 1), (40, 2), (50, -16, 1), (60, 2), (74, -12, 1), (82, 12), (96, 6, 1), (92, 30), (50, 20)]), DARKB, 'b')] +
  dome('front', top=2, w=46, cy=44, sb=70, seed=34),
  [L(outline([(10, 34), (6, 8, 1), (24, 10), (34, -14, 1), (50, 0), (66, -14, 1), (74, 6), (90, 2, 1), (86, 26), (50, 24)]), DARKB, 'b')] +
  dome('side', top=2, w=44, cy=44, nape=84, fr=56, seed=34),
  [L(outline([(8, 34), (4, 6, 1), (18, 12), (26, -12, 1), (40, 2), (50, -16, 1), (60, 2), (74, -12, 1), (82, 12), (96, 6, 1), (92, 34), (50, 28)]), DARKB, 'f')] +
  dome('back', top=2, w=46, cy=44, nape=84, seed=34))

# Pristin Florynce: pelo rubio corto y bien peinado con la raya a un lado; cara redonda y mofletuda con rubor, ojos naranjas
# y una sonrisa enorme con la boca abierta
C('pristin-florynce', 'corpulento', P('#e8c640', '#fbe2cc', '#e0861e', shade='#c09a22'),
  F(eyes='big', brows=True, mouth='grin', mouth_y=94, face_front=face(4, 102, 2), hairline=[(10, 62), (18, 46), (34, 42), (44, 48), (60, 40), (82, 46), (90, 62)]),
  dome('front', top=0, w=48, cy=44, sb=66, seed=35) + blush(88, 24, 5.5),
  dome('side', top=0, w=46, cy=44, nape=84, fr=44, seed=35),
  dome('back', top=0, w=48, cy=44, nape=84, seed=35))

# Proteus Flavout (portero): pelo blanco azulado rizado y abultado, de señor mayor; cejas blancas pobladas, cara larga,
# ojos verde amarillento y sonrisa de lado
C('proteus-flavout', 'delgado', P('#d6e6ee', '#f6c8a8', '#a8b040', shade='#a8bcc8'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_w=12, mouth_y=96, face_front=face(0, 106, 0), hairline=[(12, 62), (18, 46), (34, 38), (50, 40), (66, 38), (82, 46), (88, 62)]),
  dome('front', top=-4, w=50, cy=42, n=10, amp=5, soft=True, sb=70, seed=36) + thick_brows(64, 'mid', 4.4, w=14),
  dome('side', top=-4, w=48, cy=42, n=10, amp=5, soft=True, nape=86, fr=40, seed=36) + side_brow(64, 'mid', 4.4),
  dome('back', top=-4, w=50, cy=42, n=10, amp=5, soft=True, nape=86, seed=36))

# Puerita Cakeley: melena corta castaño salmón hasta la mandíbula con un mechón rubio cruzado sobre la frente y un
# copete arriba; cejas pequeñas fruncidas, ojos oscuros, mofletes con rubor y sonrisa
BLOND = _c('#f0d080')
C('puerita-cakeley', 'chica', P('#c46a4c', '#fbe2d4', '#2a2020', shade='#9c4e36'),
  F(eyes='round', brows='angry', mouth='smile', mouth_y=93, face_front=face(2, 100, 2), hairline=[(8, 66), (18, 54), (30, 50), (42, 58), (58, 46), (76, 46), (92, 66)]),
  [L(blob([(42, 2), (50, -8), (58, 2)], 3), 'mid', 'b')] + dome('front', top=2, w=48, cy=44, sb=92, seed=37) +
  [L(blob([(56, 10), (44, 22), (32, 40), (24, 62), (30, 64), (40, 44), (52, 26), (62, 14)], 4), BLOND, 'f')] + blush(87, 24),
  [L(blob([(44, 0), (52, -10), (58, 0)], 3), 'mid', 'b')] + dome('side', top=2, w=46, cy=44, nape=92, fr=52, seed=37),
  dome('back', top=2, w=48, cy=44, nape=92, seed=37))

# Puffet Vearn: un afro enorme granate muy oscuro; piel morena clara, ojos marrones y sonrisa amable
C('puffet-vearn', 'normal', P('#6a1e26', '#cc947c', '#4a3020', shade='#4a1218'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=93, hairline=arc_hl(60, 48)),
  dome('front', top=-24, w=62, cy=30, n=13, amp=5, soft=True, sb=62, seed=38),
  dome('side', top=-24, w=60, cy=30, n=13, amp=5, soft=True, nape=74, fr=48, seed=38),
  dome('back', top=-24, w=62, cy=30, n=13, amp=5, soft=True, nape=74, seed=38))

# Rafton Calmers: pelo azul marino muy revuelto, en pinchos que le caen sobre la frente y los ojos; piel morena, ojos verde
# agua brillantes y una sonrisa de dientes
C('rafton-calmers', 'normal', P('#1e2a4a', '#8e5a3e', '#5ac8c0', shade='#121a30'),
  F(eyes='sharp', brows=False, mouth='grin', mouth_y=95, hairline=fringe_hl(66, 74, 6, 10, lean=2)),
  dome('front', top=0, w=52, cy=42, n=10, amp=10, sb=86, seed=39, sweep=0.1),
  dome('side', top=0, w=50, cy=42, n=10, amp=10, nape=90, fr=66, seed=39),
  dome('back', top=0, w=52, cy=42, n=10, amp=10, nape=90, seed=39))

# Ralya Chersey: melena larga y lisa rubio dorado con dos mechones finos y tiesos que salen como antenas a los lados y un
# rizo de antena arriba; ojos rojos y sonrisa
C('ralya-chersey', 'chica', P('#e8b250', '#fbe2d0', '#b02a2a', shade='#c08a30'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=fringe_hl(60, 68, 6, 8)),
  dome('front', top=2, w=46, cy=44, long=120, flare=2, seed=40) +
  [L(quad((10, 40), (-6, 56), (-10, 80)), 'mid', 'f', False, False, 2.4), L(quad((90, 40), (106, 56), (110, 80)), 'mid', 'f', False, False, 2.4),
   L(quad((50, 2), (44, -18), (56, -24)), 'mid', 'f', False, False, 2.4)],
  dome('side', top=2, w=44, cy=44, long=120, flare=2, fr=56, seed=40) + [L(quad((48, 0), (42, -20), (54, -26)), 'mid', 'f', False, False, 2.4)],
  dome('back', top=2, w=46, cy=44, long=120, flare=2, ends=4, seed=40) +
  [L(quad((10, 40), (-6, 56), (-10, 80)), 'mid', 'f', False, False, 2.4), L(quad((90, 40), (106, 56), (110, 80)), 'mid', 'f', False, False, 2.4)])

# Randy Teastock: pelo verde oliva en forma de hoja grande, con mechones anchos que se curvan en punta hacia los lados y uno
# enroscado arriba; ojos verde agua y sonrisa
C('randy-teastock', 'normal', P('#8a9a4a', '#fbe0cc', '#3aa0a0', shade='#66762e'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=fringe_hl(56, 64, 4, 10, lean=-4)),
  dome('front', top=-2, w=50, cy=42, n=6, amp=8, sb=70, seed=41) +
  [L(outline([(88, 50), (110, 46, 1), (96, 60)]), 'mid', 'f'), L(outline([(12, 56), (-6, 70, 1), (8, 66)]), 'mid', 'f'),
   L(quad((30, 8), (20, -8), (32, -12)), 'mid', 'f', False, False, 3.0), L(quad((50, 0), (60, 20), (56, 50)), 'shade', 'f', False, False, 1.6)],
  dome('side', top=-2, w=48, cy=42, n=6, amp=8, nape=84, fr=56, seed=41),
  dome('back', top=-2, w=50, cy=42, n=6, amp=8, nape=84, seed=41))

# Ravyn Grooves: pelo verde intenso muy revuelto en mechones de punta que le caen sobre la cara y abultan a los lados; piel
# morena, ojos verde agua y boca seria
C('ravyn-grooves', 'normal', P('#6ae072', '#8e5a3e', '#3ab0a0', shade='#3ab04a'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=94, hairline=fringe_hl(64, 72, 6, 10)),
  dome('front', top=-2, w=56, cy=44, n=11, amp=10, sb=96, seed=42),
  dome('side', top=-2, w=54, cy=44, n=11, amp=10, nape=96, fr=66, seed=42),
  dome('back', top=-2, w=56, cy=44, n=11, amp=10, nape=96, seed=42))

# Raya Sixstring: melena larga castaño claro con el flequillo recto y las puntas onduladas por debajo de los hombros; piel
# muy clara, ojos verde agua grandes y boca seria
C('raya-sixstring', 'chica', P('#b29a72', '#fbe8e0', '#5ab0b0', shade='#8a7450'),
  F(eyes='big', brows=True, mouth='line', mouth_y=93, hairline=fringe_hl(62, 70, 7, 4)),
  dome('front', top=-2, w=48, cy=44, n=8, amp=3, soft=True, long=122, flare=10, seed=43),
  dome('side', top=-2, w=46, cy=44, n=8, amp=3, soft=True, long=122, flare=10, fr=58, seed=43),
  dome('back', top=-2, w=48, cy=44, n=8, amp=3, soft=True, long=122, flare=10, ends=5, seed=43))

# Raymond Galak: pelo negro azulado con un tupé grande y redondeado echado hacia un lado y un rizo sobre la frente; ojos
# morados con pestañas marcadas y sonrisa
C('raymond-galak', 'normal', P('#16263c', '#fbdcc4', '#4a3a7a', shade='#0c1626'),
  F(eyes='big', brows='angry', mouth='smile', mouth_w=12, mouth_y=94, hairline=[(12, 62), (18, 46), (30, 44), (42, 56), (52, 46), (68, 42), (82, 46), (88, 62)]),
  crop('front', top=2, side=68, w=2) + [L(blob([(14, 40), (12, 10), (34, -10), (66, -12), (94, 2), (98, 26), (84, 40), (60, 34), (40, 40)], 6), 'mid', 'f'),
                                        L(quad((44, 38), (38, 50), (48, 54)), 'mid', 'f', False, False, 3.0)],
  crop('side', top=2, nape=86, w=2) + [L(blob([(14, 26), (24, -6), (60, -16), (96, -2), (96, 24), (70, 30), (40, 30)], 6), 'mid', 'f')],
  crop('back', top=2, nape=86, w=2) + [L(blob([(10, 34), (14, 4), (40, -10), (70, -12), (94, 6), (92, 32), (50, 40)], 6), 'mid', 'f')])

# Readon Booke: melena gris oscuro en casco con el flequillo recto hasta las cejas y las puntas en pico hacia dentro;
# gafas de pasta naranja, ojos morados y boca seria
ORG = _c('#d8742a')
C('readon-booke', 'delgado', P('#4a4e52', '#fbe2d0', '#7a5aa0', shade='#2e3236'),
  F(eyes='normal', brows=False, mouth='frown', mouth_y=95, face_front=face(0, 104, 0), hairline=fringe_hl(64, 72, 7, 4)),
  bowl3('front', top=-2, side=96, w=8, fringe=64) + rect_specs('front', ORG, 77, 14, 2.0),
  bowl3('side', top=-2, nape=96, w=8, fringe=62) + rect_specs('side', ORG, 77, w=2.0),
  bowl3('back', top=-2, nape=96, w=8))

# Regis Tunesmith: pelo rubio arena corto y peinado con un mechón que le cae sobre la frente; cejas rubias pobladas, cara
# redonda con rubor, gafas redondas de montura azul y boca apretada
BLUEG = _c('#7a9ac8')
C('regis-tunesmith', 'corpulento', P('#c8b072', '#fbe4dc', '#2a2a3a', shade='#a08a4e'),
  F(eyes='dot', brows=False, mouth='frown', mouth_y=95, face_front=face(4, 102, 2), hairline=[(10, 62), (18, 44), (34, 38), (50, 40), (66, 38), (82, 44), (90, 62)]),
  dome('front', top=-2, w=46, cy=42, sb=66, seed=44) + thick_brows(64, 'mid', 4.6, w=14) +
  [L(quad((52, 30), (44, 40), (50, 50)), 'shade', 'f', False, False, 2.4)] + round_glasses('front', BLUEG, 77, 14, 8.0, lens=(240, 244, 250, 255), w=1.8) + blush(88, 26, 5.5),
  dome('side', top=-2, w=44, cy=42, nape=84, fr=42, seed=44) + side_brow(64, 'mid', 4.6) + round_glasses('side', BLUEG, 77, r=8.0, lens=(240, 244, 250, 255), w=1.8),
  dome('back', top=-2, w=46, cy=42, nape=84, seed=44))

# Renee Sirensong: melena larga castaño claro que se abre mucho hacia los lados en mechones lisos, con un rizo de antena
# arriba; cejas fruncidas, ojos azules, un moflete hinchado y boca de enfado
C('renee-sirensong', 'chica', P('#b0905e', '#fbdcc8', '#4a7ab8', shade='#8a6c40'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(8, 64), (18, 50), (30, 44), (46, 52), (60, 42), (80, 46), (92, 64)]),
  [L(outline([(10, 50), (-24, 66, 1), (-12, 70), (-30, 88, 1), (4, 82), (12, 70)]), 'mid', 'b'),
   L(outline([(90, 50), (124, 66, 1), (112, 70), (130, 88, 1), (96, 82), (88, 70)]), 'mid', 'b')] +
  dome('front', top=0, w=48, cy=44, long=112, flare=6, seed=45) + [L(quad((44, 2), (40, -18), (54, -20)), 'mid', 'f', False, False, 2.6)] + blush(88, 22),
  dome('side', top=0, w=46, cy=44, long=112, flare=14, fr=50, seed=45) + [L(quad((44, 0), (40, -18), (54, -22)), 'mid', 'f', False, False, 2.6)],
  [L(outline([(10, 50), (-24, 66, 1), (-12, 70), (-30, 88, 1), (4, 82), (12, 70)]), 'mid', 'b'),
   L(outline([(90, 50), (124, 66, 1), (112, 70), (130, 88, 1), (96, 82), (88, 70)]), 'mid', 'b')] +
  dome('back', top=0, w=48, cy=44, long=112, flare=6, ends=4, seed=45))
