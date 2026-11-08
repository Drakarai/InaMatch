"""Ojeadores de Victory Road (scouts-vr), tanda 02: dibujados a partir de su retrato; claves 'scouts-vr:<id>'.

Ninguno de la tanda tiene modelo 3D propio salvo Caelum Wade: el frente sale del retrato y el perfil y la espalda se
deducen de cómo cae el peinado. El sexo (cuerpo 'chica') viene de su ficha de la wiki. Usa dome/hl/face de la tanda 09
de IE1 para la masa de pelo y añade moños, trenzas, coletas, rubor y pecas."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars_scouts_ie1_09 import BLACK, WHITE, _c, dome, face, face_side, hl, mark  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401

PINK = _c('#f08c96')
FRECK = _c('#c8785a')


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


def blush(y=86, dx=18, side=False):
    if side:
        return [L(ell(74, y, 4.4, 2.6), PINK, 'f', False)]
    return [L(ell(50 - dx, y, 4.6, 2.8), PINK, 'f', False), L(ell(50 + dx, y, 4.6, 2.8), PINK, 'f', False)]


def freckles(y=84, dx=17, side=False):
    pts = [(-4, 0), (0, 2), (4, 0), (1, -2)]
    if side:
        return [L(ell(74 + px * 0.8, y + py, 0.9, 0.9), FRECK, 'f', False) for px, py in pts]
    return [L(ell(50 + s * dx + px, y + py, 0.9, 0.9), FRECK, 'f', False) for s in (-1, 1) for px, py in pts]


def bun(x, y, r, c='mid', tie=None, ty=0, tx=0):
    out = [L(ell(x, y, r, r * 0.92), c)]
    if tie:
        out.append(L(ell(x + tx, y + ty, r * 0.42, r * 0.42), tie, 'b', True))
    return out


def braid(x, y, n=4, dy=10, r=5.5, c='mid', dx=0.0, tie=None):
    out = [L(ell(x + dx * i, y + dy * i, r, dy * 0.62), c, 'b', True, True) for i in range(n)]
    if tie:
        out.append(L(ell(x + dx * n, y + dy * n - dy * 0.3, r * 0.7, 2.4), tie))
    return out


def lock(pts, c='mid', z='f'):
    """Mechón suelto (contorno con puntas)."""
    return L(outline(pts), c, z)


def eyeshadow(y=73, c=PINK):
    return [L(quad((26, y - 3), (36, y - 8), (46, y - 3)), c, 'f', False, False, 2.4),
            L(quad((54, y - 3), (64, y - 8), (74, y - 3)), c, 'f', False, False, 2.4)]


# ------------------------------------------------------------------ jugadores

# Bernadine Banquet: pelo castaño claro rosado esponjoso en ondas, con una trenza larga que le cae por un lado; ojos
# cerrados de felicidad, sonrisa y un bigotito pintado en las mejillas
BR = _c('#8a5e52')
C('bernadine-banquet', 'chica', P('#a87868', '#fbdcd0'),
  F(eyes='closed', mouth='smile', mouth_y=92, hairline=hl(6, 66, 48, 54, jit=2, seed=2)),
  dome('front', top=0, w=50, cy=44, n=12, amp=6, soft=True, sb=70, seed=3) + braid(18, 84, 4, 10, 5.5, dx=-0.6) +
  [L(quad((36, 88), (40, 86), (44, 88)), BR, 'f', False, False, 1.2), L(quad((56, 88), (60, 86), (64, 88)), BR, 'f', False, False, 1.2)],
  dome('side', top=0, w=48, cy=44, n=12, amp=6, soft=True, nape=88, fr=48, seed=3),
  dome('back', top=0, w=50, cy=44, n=12, amp=6, soft=True, nape=88, seed=3) + braid(80, 82, 4, 10, 5.5, dx=0.6))

# Biijiro Onoda: pelo granate oscuro abombado con el flequillo en puntas sobre los ojos; pecas, ojos verdosos, ceño serio
C('biijiro-onoda', 'normal', P('#6a1a24', '#f8cdb4', iris='#7a8058'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=hl(5, 66, 50, 64, jit=2, seed=4)),
  dome('front', top=0, w=50, cy=44, n=6, amp=5, soft=True, sb=68, seed=4) + freckles(),
  dome('side', top=0, w=48, cy=44, n=6, amp=5, soft=True, nape=88, fr=54, seed=4) + freckles(side=True),
  dome('back', top=0, w=50, cy=44, n=6, amp=5, soft=True, nape=88, seed=4))

# Blendon Frugel: pelo castaño oscuro en ondas revueltas con una horquilla en X turquesa; cejas gruesas curvas y ojos
# entornados granates
CY = _c('#58d0d8')
C('blendon-frugel', 'normal', P('#5a4848', '#f8e6d6', iris='#a02a5a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=hl(6, 66, 48, 58, lean=-1, jit=3, seed=5)),
  dome('front', top=-2, w=50, cy=44, n=10, amp=8, soft=True, sb=70, seed=5) +
  [L([(18, 34), (30, 46)], CY, 'f', False, False, 2.6), L([(30, 34), (18, 46)], CY, 'f', False, False, 2.6),
   L([(26, 63), (44, 66)], OUTC, 'f', False, False, 3.6), L([(74, 63), (56, 66)], OUTC, 'f', False, False, 3.6)],
  dome('side', top=-2, w=48, cy=44, n=10, amp=8, soft=True, nape=88, fr=50, seed=5),
  dome('back', top=-2, w=50, cy=44, n=10, amp=8, soft=True, nape=88, seed=5) +
  [L([(76, 34), (88, 46)], CY, 'b', False, False, 2.6), L([(88, 34), (76, 46)], CY, 'b', False, False, 2.6)])

# Blossom Laine: pelo azul petróleo con flequillo y dos moños a los lados atados con cintas rojas, de los que caen dos
# mechones; ojos grandes naranjas, rubor y sonrisa
RED = _c('#d02a3a')
C('blossom-laine', 'chica', P('#1e7a98', '#fbdcc8', iris='#c8661e'),
  F(eyes='normal', brows='angry', mouth='smile', mouth_y=92, hairline=hl(5, 64, 50, 58, seed=6)),
  bun(8, 44, 10, tie=RED, tx=6) + bun(92, 44, 10, tie=RED, tx=-6) +
  [lock([(4, 54), (12, 52), (14, 78), (8, 84, 1)], 'mid', 'b'), lock([(96, 54), (88, 52), (86, 78), (92, 84, 1)], 'mid', 'b')] +
  dome('front', top=2, w=46, cy=44, sb=66) + blush(),
  bun(30, 42, 11, tie=RED, tx=6) + dome('side', top=2, w=46, cy=44, nape=84, fr=52) + blush(side=True),
  bun(8, 44, 10, tie=RED, tx=6) + bun(92, 44, 10, tie=RED, tx=-6) + dome('back', top=2, w=46, cy=44, nape=84))

# Blue Cleverley (portero): media melena castaño claro en casco con la raya al medio y el flequillo hasta las cejas; ojos
# redondos grandes azulados, cejas gruesas y sonrisa
C('blue-cleverley', 'normal', P('#b8966e', '#fbdac8', iris='#5a6ab0'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93,
    hairline=[(6, 72), (14, 58), (30, 58), (46, 52), (50, 46), (54, 52), (70, 58), (86, 58), (94, 72)]),
  dome('front', top=2, w=50, cy=46, sb=76) + [L([(50, 6), (50, 44)], 'shade', 'f', False, False, 1.2)],
  dome('side', top=2, w=48, cy=46, nape=90, fr=58),
  dome('back', top=2, w=50, cy=46, nape=90) + [L([(50, 6), (50, 60)], 'shade', 'b', False, False, 1.2)])

# Bowen Fleurmett: pelo naranja con raya a un lado, echado y cayendo por la sien hasta la mejilla; ojos grises, cejas
# fruncidas y boca pequeña
C('bowen-fleurmett', 'normal', P('#e0662a', '#fbdcc8', iris='#6a6a8a'),
  F(eyes='normal', brows='angry', mouth='line', mouth_y=93,
    hairline=[(6, 64), (14, 46), (28, 42), (44, 40), (60, 44), (74, 54), (82, 70), (90, 84), (94, 70)]),
  dome('front', top=0, w=48, cy=44, sweep=0.6, sb=68) + [lock([(56, 30), (80, 40), (88, 64), (90, 86, 1), (80, 66), (68, 50)])],
  dome('side', top=0, w=46, cy=44, nape=86, fr=46),
  dome('back', top=0, w=48, cy=44, nape=86))

# Bowie Buffoon (portero): un afro enorme morado oscuro que le llega a las mejillas; cara ancha, cejas negras curvas y
# muy gruesas, ojos entornados y sonrisa de pillo
C('bowie-buffoon', 'corpulento', P('#3e1a2c', '#fad8c0', iris='#2a2a3a'),
  F(eyes='closed', brows=False, mouth='smile', mouth_y=94, face_front=face(w=4, chin=102, jaw=2), ears=False,
    hairline=[(6, 66), (14, 54), (30, 50), (50, 50), (70, 50), (86, 54), (94, 66)]),
  dome('front', top=-6, w=62, cy=50, n=16, amp=5, soft=True, long=100, flare=4, seed=7) +
  [L(quad((26, 70), (34, 58), (46, 68)), OUTC, 'f', False, False, 3.4), L(quad((74, 70), (66, 58), (54, 68)), OUTC, 'f', False, False, 3.4)],
  dome('side', top=-6, w=58, cy=50, n=16, amp=5, soft=True, long=100, flare=4, fr=52, seed=7),
  dome('back', top=-6, w=62, cy=50, n=16, amp=5, soft=True, long=100, flare=4, ends=5, seed=7))

# Bracker Grippe: pelo celeste grisáceo peinado hacia atrás y recogido en un moño arriba, con un rizo que le cae por un
# lado; piel morena, ojos celestes afilados y media sonrisa
C('bracker-grippe', 'normal', P('#a8ccd4', '#c89a7a', iris='#6a9ab8'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=[(6, 62), (16, 44), (34, 36), (50, 34), (66, 36), (84, 44), (94, 62)]),
  [L(ell(50, 0, 11, 9))] + dome('front', top=4, w=46, cy=44, sb=62) +
  [lock([(66, 38), (84, 44), (90, 60), (84, 74, 1), (80, 58), (72, 48)])],
  [L(ell(38, 2, 11, 9))] + dome('side', top=4, w=46, cy=44, nape=84, fr=40) + [lock([(84, 40), (94, 48), (92, 66, 1), (88, 52)])],
  [L(ell(50, 0, 11, 9))] + dome('back', top=4, w=46, cy=44, nape=84))

# Brandan Broomdorf (portero): una melena roja lisa que le tapa la cabeza como un casco y le cae hasta los hombros; cara
# blanca de kabuki con los ojos pintados de rojo y cejas negras gruesas fruncidas
KR = _c('#c8242a')
C('brandan-broomdorf', 'corpulento', P('#c02a2a', '#f8f0ee', iris='#3a4a7a'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=94, face_front=face(w=4, chin=102, jaw=2), ears=False,
    hairline=[(6, 60), (16, 58), (50, 56), (84, 58), (94, 60)]),
  dome('front', top=-2, w=54, cy=46, long=124, flare=8, ends=3) +
  [L([(24, 66), (34, 62), (44, 68)], OUTC, 'f', False, False, 4.0), L([(76, 66), (66, 62), (56, 68)], OUTC, 'f', False, False, 4.0),
   L(quad((24, 74), (32, 82), (44, 80)), KR, 'f', False, False, 1.6), L(quad((76, 74), (68, 82), (56, 80)), KR, 'f', False, False, 1.6)],
  dome('side', top=-2, w=52, cy=46, long=124, flare=8, fr=56),
  dome('back', top=-2, w=54, cy=46, long=124, flare=8, ends=3))

# Brannon Chalant: media melena gris lisa con la raya al medio hasta la mandíbula; ojos entornados, ceño y boca torcida
C('brannon-chalant', 'normal', P('#6e6e6a', '#fbe4c0', iris='#3a3a4a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94,
    hairline=[(6, 70), (16, 50), (34, 40), (50, 34), (66, 40), (84, 50), (94, 70)]),
  dome('front', top=0, w=48, cy=44, long=96, flare=2) + [L([(50, 4), (50, 34)], 'shade', 'f', False, False, 1.2)],
  dome('side', top=0, w=46, cy=44, long=96, flare=2, fr=40),
  dome('back', top=0, w=48, cy=44, long=96, flare=2))

# Brenae Ackermann: melena larga lisa azul grisácea hasta el pecho con un mechón que le cruza la cara; unas gafas de
# buceo subidas a la frente, ojos en espiral celestes y sonrisa nerviosa
GOG = _c('#e8f0ee')
C('brenae-ackermann', 'chica', P('#3a4a5e', '#fbe2d8', iris='#58a8c8'),
  F(eyes='round', brows=True, mouth='smile', mouth_y=93, hairline=[(6, 70), (16, 52), (34, 44), (50, 40), (66, 44), (84, 52), (94, 70)]),
  dome('front', top=0, w=48, cy=44, long=132, flare=4) +
  [L(blob([(32, 44), (68, 44), (68, 56), (32, 56)], 3), GOG, 'f', True, True), lock([(50, 32), (56, 34), (56, 80), (52, 104, 1), (50, 70)])],
  dome('side', top=0, w=46, cy=44, long=132, flare=4, fr=44) + [L(blob([(72, 44), (90, 44), (90, 56), (72, 56)], 3), GOG, 'f', True, True)],
  dome('back', top=0, w=48, cy=44, long=132, flare=4, ends=4) + [L([(6, 50), (94, 50)], _c('#5a6a7a'), 'b', False, False, 2.4)])

# Brianna Summing: media melena corta ondulada castaño oliva, piel tostada con pecas, ojos azules afilados y sonrisa
C('brianna-summing', 'chica', P('#5a4a20', '#eca478', iris='#3a4ab0'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 66), (14, 52), (30, 44), (44, 48), (56, 44), (72, 46), (86, 52), (94, 66)]),
  dome('front', top=0, w=52, cy=44, n=8, amp=5, soft=True, long=88, flare=6, seed=9) + freckles(),
  dome('side', top=0, w=50, cy=44, n=8, amp=5, soft=True, long=88, flare=6, fr=48, seed=9) + freckles(side=True),
  dome('back', top=0, w=52, cy=44, n=8, amp=5, soft=True, long=88, flare=6, seed=9))

# Bridget Steepen: una nube enorme de pelo rosa en dos pisos, más ancha que la cabeza; piel oscura, ojos grandes y
# redondos rojizos y sonrisa
C('bridget-steepen', 'chica', P('#d0687a', '#5a3224', iris='#a02a2a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 64), (16, 56), (34, 54), (50, 52), (66, 54), (84, 56), (94, 64)]),
  [L(blob([(-14, 30), (0, 14), (20, 22), (50, 16), (80, 22), (100, 14), (114, 30), (104, 44), (80, 40), (50, 44), (20, 40), (-4, 44)], 6))] +
  dome('front', top=-12, w=40, cy=34, n=10, amp=6, soft=True, sb=60, seed=10, shade=False) +
  [L(blob([(10, 44), (90, 44), (88, 58), (12, 58)], 4))],
  [L(blob([(0, 30), (20, 14), (60, 12), (96, 26), (92, 46), (50, 50), (8, 48)], 6))] +
  dome('side', top=-12, w=40, cy=34, n=10, amp=6, soft=True, nape=80, fr=54, seed=10, shade=False),
  [L(blob([(-14, 30), (0, 14), (20, 22), (50, 16), (80, 22), (100, 14), (114, 30), (104, 44), (80, 40), (50, 44), (20, 40), (-4, 44)], 6))] +
  dome('back', top=-12, w=40, cy=34, n=10, amp=6, soft=True, nape=80, seed=10, shade=False) +
  [L(blob([(10, 44), (90, 44), (88, 76), (50, 82), (12, 76)], 4))])

# Britson Farago: pelo rubio corto en pinchos hacia arriba, ojos afilados ámbar, cejas fruncidas y sonrisa de dientes
C('britson-farago', 'normal', P('#e8c040', '#f8c8a0', iris='#a07a2a'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, hairline=hl(5, 62, 46, 56, jit=3, seed=11)),
  dome('front', top=-4, w=46, cy=42, n=7, amp=12, seed=11, sb=64),
  dome('side', top=-4, w=46, cy=42, n=7, amp=12, seed=11, nape=82, fr=46),
  dome('back', top=-4, w=46, cy=42, n=7, amp=12, seed=11, nape=82))

# Brooke Reedman: media melena negra con un mechón azul que le cae por el centro de la cara y las puntas azules; ojos rojos
# y gesto triste
BL = _c('#3a7ad8')
C('brooke-reedman', 'normal', P('#1c2030', '#fbe0d0', iris='#c02a3a'),
  F(eyes='normal', brows=True, mouth='frown', mouth_y=94, hairline=[(6, 70), (16, 54), (34, 50), (48, 58), (60, 50), (84, 54), (94, 70)]),
  dome('front', top=0, w=50, cy=44, n=7, amp=5, soft=True, long=96, flare=4, seed=12) +
  [lock([(42, 32), (50, 30), (52, 66), (48, 88, 1), (44, 64)], BL), L(blob([(14, 92), (22, 90), (22, 98), (14, 98)], 3), BL, 'b', False),
   L(blob([(78, 90), (86, 92), (86, 98), (78, 98)], 3), BL, 'b', False)],
  dome('side', top=0, w=48, cy=44, n=7, amp=5, soft=True, long=96, flare=4, fr=50, seed=12),
  dome('back', top=0, w=50, cy=44, n=7, amp=5, soft=True, long=96, flare=4, seed=12) +
  [L(blob([(8, 88), (92, 88), (92, 98), (8, 98)], 3), BL, 'b', False)])

# Bunette Volane (portera): pelo blanco rosado en melenita con flequillo recto y dos grandes rodetes redondos arriba a los
# lados, como orejas; ojos rojos y boca pequeña
C('bunette-volane', 'chica', P('#f4e4e6', '#fbe4dc', iris='#c02a3a', shade='#e4c8cc'),
  F(eyes='sharp', brows=True, mouth='frown', mouth_y=93, hairline=[(6, 68), (14, 60), (50, 60), (86, 60), (94, 68)]),
  bun(12, 14, 16) + bun(88, 14, 16) + dome('front', top=4, w=48, cy=46, long=92, flare=2) +
  [L([(16, 8), (12, 26)], 'shade', 'f', False, False, 1.0), L([(84, 8), (88, 26)], 'shade', 'f', False, False, 1.0)],
  bun(36, 10, 16) + dome('side', top=4, w=46, cy=46, long=92, flare=2, fr=60),
  bun(12, 14, 16) + bun(88, 14, 16) + dome('back', top=4, w=48, cy=46, long=92, flare=2))

# Burley Billabong (portero): pelo negro rapado en un casquete corto, cara ancha morena, cejas negras muy gruesas en arco,
# nariz ancha y ceño
C('burley-billabong', 'corpulento', P('#2a2a2c', '#b07a4c', iris='#2a2020'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=95, face_front=face(w=8, chin=104, jaw=5), face_side=face_side(chin=4, jaw=6),
    big_ears=2, ear_out=6, nose=(50, 85, 4), hairline=[(6, 54), (16, 40), (34, 32), (50, 30), (66, 32), (84, 40), (94, 54)]),
  dome('front', top=10, w=44, cy=46, sb=54, shade=False) +
  [L(quad((24, 70), (34, 58), (46, 66)), OUTC, 'f', False, False, 4.4), L(quad((76, 70), (66, 58), (54, 66)), OUTC, 'f', False, False, 4.4)],
  dome('side', top=10, w=42, cy=46, nape=72, fr=36, shade=False),
  dome('back', top=10, w=44, cy=46, nape=72, shade=False))

# Caddy Chamomile: melena rosa abombada hasta la barbilla con un moño recogido verde oliva encima, de mechones; ojos
# grandes rosas con pestañas y bigotito
OL = _c('#8a8a3a')
C('caddy-chamomile', 'chica', P('#f0a8c0', '#fbe0d4', iris='#d0507a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=[(6, 70), (14, 54), (30, 48), (50, 50), (70, 48), (86, 54), (94, 70)]),
  [L(blob([(30, 30), (36, 0), (50, -14), (64, 0), (70, 30), (50, 36)], 6), OL)] +
  dome('front', top=4, w=56, cy=48, long=96, flare=6, shade=True) +
  [L([(50, -10), (50, 30)], _c('#6a6a2a'), 'f', False, False, 1.2), L(blob([(40, 26), (60, 26), (62, 40), (38, 40)], 4), OL, 'f', True, False)],
  [L(blob([(26, 30), (30, 0), (44, -12), (58, 2), (60, 30), (44, 36)], 6), OL)] + dome('side', top=4, w=52, cy=48, long=96, flare=6, fr=50),
  [L(blob([(30, 30), (36, 0), (50, -14), (64, 0), (70, 30), (50, 36)], 6), OL)] + dome('back', top=4, w=56, cy=48, long=96, flare=6))

# Caellum Orison: pelo verde abombado y revuelto con un pelo de punta arriba; marcas verde claro alrededor de los ojos,
# ojos redondos y ceño
MK = _c('#a8e0b0')
C('caellum-orison', 'normal', P('#3a8a6a', '#fbdac8', iris='#2a6a5a'),
  F(eyes='round', brows=True, mouth='frown', mouth_y=93, hairline=hl(5, 66, 50, 58, lean=2, jit=2, seed=13)),
  dome('front', top=2, w=48, cy=44, n=7, amp=6, soft=True, sweep=0.4, sb=66, seed=13) +
  [lock([(44, 6), (40, -10), (48, -6), (52, -16, 1), (54, 4)]),
   L([(26, 70), (24, 80)], MK, 'f', False, False, 2.4), L([(74, 70), (76, 80)], MK, 'f', False, False, 2.4)],
  dome('side', top=2, w=46, cy=44, n=7, amp=6, soft=True, nape=84, fr=52, seed=13) + [lock([(48, 6), (46, -12), (56, -14, 1), (56, 4)])],
  dome('back', top=2, w=48, cy=44, n=7, amp=6, soft=True, nape=84, seed=13) + [lock([(48, 6), (46, -12), (56, -14, 1), (54, 4)])])

# Caelum Wade (con modelo 3D): gorra azul marino con la visera hacia delante y un logo claro, pelo granate asomando por
# los lados y la nuca; gafas negras gruesas rectangulares y sonrisa
NV, NVD = _c('#1e2e5a'), _c('#142040')
C('caelum-wade', 'normal', P('#a03a2a', '#f8d0b0', iris='#2a2020'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=93, glasses=_c('#1a1a1e'), glasses_rect=True, hairline=False),
  [lock([(6, 56), (14, 52), (16, 78), (8, 72)], 'mid', 'b'), lock([(94, 56), (86, 52), (84, 78), (92, 72)], 'mid', 'b'),
   L(blob([(6, 54), (8, 24), (24, 4), (50, -2), (76, 4), (92, 24), (94, 54), (50, 50)], 6), NV),
   L(blob([(14, 52), (50, 46), (86, 52), (84, 62), (50, 58), (16, 62)], 3), NVD, 'f'),
   L(quad((42, 26), (50, 20), (58, 26)), _c('#c8d0e0'), 'f', False, False, 1.8), L(quad((42, 32), (50, 26), (58, 32)), _c('#c8d0e0'), 'f', False, False, 1.8)],
  [lock([(14, 60), (40, 58), (44, 74), (24, 82)], 'mid', 'b'),
   L(blob([(4, 60), (2, 30), (20, 6), (48, -2), (76, 6), (90, 26), (92, 50), (50, 56), (20, 62)], 6), NV),
   L(blob([(80, 46), (108, 50), (108, 56), (80, 56)], 3), NVD, 'f')],
  [lock([(14, 60), (86, 60), (84, 80), (16, 80)], 'mid', 'b'),
   L(blob([(6, 62), (8, 28), (24, 6), (50, -2), (76, 6), (92, 28), (94, 62), (50, 58)], 6), NV),
   L(blob([(38, 50), (62, 50), (62, 58), (38, 58)], 3), _c('#e8e8ee'), 'f', False)])

# Calem Backstrom: pelo gris azulado oscuro en mechones echados hacia los lados, piel morena con pecas, ojos verdes
# grandes y sonrisa
C('calem-backstrom', 'normal', P('#3a4250', '#8a5a3a', iris='#2a8a6a'),
  F(eyes='big', brows='angry', mouth='smile', mouth_y=93, hairline=hl(5, 64, 48, 58, lean=-2, jit=3, seed=14)),
  dome('front', top=2, w=50, cy=44, n=7, amp=9, sweep=-0.3, sb=68, seed=14) + freckles(),
  dome('side', top=2, w=48, cy=44, n=7, amp=9, sweep=-0.3, nape=84, fr=50, seed=14) + freckles(side=True),
  dome('back', top=2, w=50, cy=44, n=7, amp=9, sweep=-0.3, nape=84, seed=14))

# Calina Breezer: pelo lila corto en ondas suaves, ojos cerrados tranquilos con cejas lilas y boca pequeña
C('calina-breezer', 'chica', P('#b89ab0', '#fbe4dc', iris='#6a4a7a'),
  F(eyes='closed', brows=True, mouth='line', mouth_y=93, hairline=[(6, 64), (14, 52), (30, 46), (44, 50), (56, 46), (72, 48), (86, 52), (94, 64)]),
  dome('front', top=4, w=46, cy=44, n=9, amp=4, soft=True, long=84, flare=2, seed=15),
  dome('side', top=4, w=44, cy=44, n=9, amp=4, soft=True, long=84, flare=2, fr=48, seed=15),
  dome('back', top=4, w=46, cy=44, n=9, amp=4, soft=True, long=84, flare=2, seed=15))

# Calix Virtus (portero): pelo verde muy oscuro peinado hacia atrás con dos picos como cuernos arriba; cara grande y
# pálida, ojos morados redondos, boca en ceño grande
C('calix-virtus', 'corpulento', P('#26342a', '#fbe4b4', iris='#7a3a8a'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=95, face_front=face(w=8, chin=104, jaw=6), face_side=face_side(chin=4, jaw=5),
    nose=(50, 86, 3), hairline=[(6, 60), (18, 44), (34, 38), (50, 44), (66, 38), (82, 44), (94, 60)]),
  dome('front', top=6, w=46, cy=46, sb=62) + [lock([(34, 14), (40, -14, 1), (48, 10)]), lock([(52, 10), (60, -14, 1), (66, 14)])] +
  [L(quad((40, 98), (50, 90), (60, 98)), OUTC, 'f', False, False, 1.6)],
  dome('side', top=6, w=44, cy=46, nape=82, fr=44) + [lock([(40, 12), (46, -14, 1), (56, 10)])],
  dome('back', top=6, w=46, cy=46, nape=82) + [lock([(34, 14), (40, -14, 1), (48, 10)]), lock([(52, 10), (60, -14, 1), (66, 14)])])

# Callista Norton: melena larga blanca lila con flequillo; dos colas a los lados que caen hasta el pecho y se abren en
# pinzas, con lazos negros; ojos rojos y media sonrisa
BK = _c('#2a2228')
C('callista-norton', 'chica', P('#e8e4f0', '#fbe0d4', iris='#b0283a', shade='#c8c0d8'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 68), (14, 58), (30, 56), (50, 54), (70, 56), (86, 58), (94, 68)]),
  [lock([(6, 56), (16, 54), (14, 104), (2, 118, 1), (-10, 110, 1), (2, 104)], 'mid', 'b'),
   lock([(94, 56), (84, 54), (86, 104), (98, 118, 1), (110, 110, 1), (98, 104)], 'mid', 'b'),
   L(ell(6, 50, 6, 8), BK, 'f'), L(ell(94, 50, 6, 8), BK, 'f')] + dome('front', top=0, w=50, cy=44, long=104, flare=2),
  [lock([(30, 56), (42, 56), (40, 104), (28, 118, 1), (16, 110, 1), (28, 104)], 'mid', 'b'), L(ell(32, 50, 6, 8), BK)] +
  dome('side', top=0, w=48, cy=44, long=104, flare=2, fr=54),
  [lock([(6, 56), (16, 54), (14, 104), (2, 118, 1), (-10, 110, 1), (2, 104)], 'mid', 'b'),
   lock([(94, 56), (84, 54), (86, 104), (98, 118, 1), (110, 110, 1), (98, 104)], 'mid', 'b'),
   L(ell(6, 50, 6, 8), BK), L(ell(94, 50, 6, 8), BK)] + dome('back', top=0, w=50, cy=44, long=104, flare=2))

# Candace Mardipanz: pelo verde azulado con flequillo recto y dos moños enormes arriba atados con gomas rojas; cara
# redonda, pecas, ojos entornados y sonrisa de pilla
C('candace-mardipanz', 'chica', P('#4a9a8a', '#fbc8a4', iris='#3a5a9a'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=92, face_front=face(w=4, chin=100, jaw=3), ear_out=4,
    hairline=[(6, 62), (14, 58), (50, 56), (86, 58), (94, 62)]),
  bun(4, 10, 17, tie=RED, tx=10, ty=10) + bun(96, 10, 17, tie=RED, tx=-10, ty=10) + dome('front', top=4, w=46, cy=44, sb=60) + freckles(86, 20),
  bun(36, 6, 17, tie=RED, tx=6, ty=12) + dome('side', top=4, w=44, cy=44, nape=80, fr=56) + freckles(side=True),
  bun(4, 10, 17, tie=RED, tx=10, ty=10) + bun(96, 10, 17, tie=RED, tx=-10, ty=10) + dome('back', top=4, w=46, cy=44, nape=80))

# Cane Fangley: pelo rosa salmón alborotado con dos mechones marrón oscuro a los lados; piel morena con una mancha negra
# en forma de V alrededor de los ojos, como un antifaz, y ceño
DB = _c('#3a2a24')
C('cane-fangley', 'normal', P('#f0b0a0', '#8a5a40', iris='#c8a07a'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=94, hairline=hl(5, 66, 48, 60, jit=3, seed=16)),
  dome('front', top=0, w=50, cy=44, n=8, amp=8, soft=True, long=92, flare=4, seed=16) +
  [lock([(10, 40), (20, 36), (22, 70), (14, 84, 1)], DB, 'b'), lock([(90, 40), (80, 36), (78, 70), (86, 84, 1)], DB, 'b'),
   L(outline([(22, 68), (40, 70), (50, 60, 1), (60, 70), (78, 68), (76, 82), (60, 82), (50, 76), (40, 82), (24, 82)]), DB, 'f', False),
   L(ell(36, 76, 5, 4), WHITE, 'f', False), L(ell(64, 76, 5, 4), WHITE, 'f', False),
   L(ell(36, 76, 2.6, 2.8), _c('#c8a07a'), 'f', False), L(ell(64, 76, 2.6, 2.8), _c('#c8a07a'), 'f', False)],
  dome('side', top=0, w=48, cy=44, n=8, amp=8, soft=True, long=92, flare=4, fr=50, seed=16) +
  [L(outline([(70, 68), (88, 64), (88, 82), (72, 82)]), DB, 'f', False), L(ell(80, 75, 3.4, 3.4), WHITE, 'f', False)],
  dome('back', top=0, w=50, cy=44, n=8, amp=8, soft=True, long=92, flare=4, seed=16) +
  [lock([(10, 40), (20, 36), (22, 76), (14, 88, 1)], DB, 'b'), lock([(90, 40), (80, 36), (78, 76), (86, 88, 1)], DB, 'b')])

# Capricia Saiz: media melena granate oscuro con la raya a un lado y un mechón que le cae por la frente; piel tostada, ojos
# grandes morados y gesto serio
C('capricia-saiz', 'chica', P('#6a1e24', '#c88a5e', iris='#4a3a7a'),
  F(eyes='big', brows=True, mouth='line', mouth_y=93, hairline=[(6, 66), (14, 50), (30, 44), (46, 46), (60, 42), (76, 48), (88, 56), (94, 66)]),
  dome('front', top=0, w=50, cy=44, sweep=-0.4, long=90, flare=2) + [lock([(4, 52), (10, 46), (12, 60), (0, 64, 1)], 'mid', 'b')],
  dome('side', top=0, w=48, cy=44, long=90, flare=2, fr=48),
  dome('back', top=0, w=50, cy=44, long=90, flare=2))

# Carlisle Laimlight: media melena lisa color crema con las puntas rosadas y una trenza larga a un lado; ojos verdes con
# un toque amarillo y gesto serio
PKT = _c('#e0b8b0')
C('carlisle-laimlight', 'normal', P('#e4dcc8', '#fbe4d4', iris='#5a7a3a'),
  F(eyes='normal', brows=True, mouth='line', mouth_y=93, hairline=[(6, 68), (14, 54), (30, 56), (44, 50), (56, 54), (72, 52), (86, 54), (94, 68)]),
  dome('front', top=0, w=50, cy=44, long=88, flare=4) + braid(16, 92, 4, 9, 5, dx=-0.4) +
  [L(blob([(2, 82), (14, 80), (14, 90), (2, 90)], 3), PKT, 'b', False), L(blob([(86, 80), (98, 82), (98, 90), (86, 90)], 3), PKT, 'b', False)],
  dome('side', top=0, w=48, cy=44, long=88, flare=4, fr=52),
  dome('back', top=0, w=50, cy=44, long=88, flare=4) + braid(84, 90, 4, 9, 5, dx=0.4) +
  [L(blob([(4, 80), (96, 80), (96, 90), (4, 90)], 3), PKT, 'b', False)])

# Carly Veneer (portera): melena larga rosa pálido ondulada hasta el pecho, con la frente despejada; ojos cerrados de
# felicidad, cejas finas, rubor y sonrisa
C('carly-veneer', 'chica', P('#f0d0d0', '#fbe4dc', iris='#8a5a6a', shade='#dcb0b4'),
  F(eyes='closed', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 68), (16, 52), (32, 42), (50, 38), (68, 42), (84, 52), (94, 68)]),
  dome('front', top=0, w=50, cy=44, n=8, amp=4, soft=True, long=120, flare=8, seed=17) + blush(),
  dome('side', top=0, w=48, cy=44, n=8, amp=4, soft=True, long=120, flare=8, fr=42, seed=17) + blush(side=True),
  dome('back', top=0, w=50, cy=44, n=8, amp=4, soft=True, long=120, flare=8, seed=17))

# Carole Meine: pelo gris claro con dos coletas abultadas a los lados, un tirabuzón en la frente y mechones rosas junto
# a las sienes; sombra rosa sobre los ojos amarillos y sonrisa
PKS = _c('#e080b0')
C('carole-meine', 'chica', P('#c4c4c8', '#fbe8e0', iris='#c8b040'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=92, hairline=[(6, 62), (16, 46), (34, 40), (50, 44), (66, 40), (84, 46), (94, 62)]),
  [L(blob([(0, 40), (-14, 60), (-12, 86), (6, 92), (12, 70), (10, 46)], 6)), L(blob([(100, 40), (114, 60), (112, 86), (94, 92), (88, 70), (90, 46)], 6))] +
  dome('front', top=2, w=48, cy=44, sb=60) +
  [lock([(46, 30), (58, 32), (60, 48), (50, 56), (46, 48), (52, 44)]), L([(18, 52), (22, 60)], PKS, 'f', False, False, 3),
   L([(82, 52), (78, 60)], PKS, 'f', False, False, 3)] + eyeshadow(),
  [L(blob([(24, 40), (6, 58), (8, 88), (24, 92), (30, 70), (32, 46)], 6))] + dome('side', top=2, w=46, cy=44, nape=82, fr=44),
  [L(blob([(0, 40), (-14, 60), (-12, 86), (6, 92), (12, 70), (10, 46)], 6)), L(blob([(100, 40), (114, 60), (112, 86), (94, 92), (88, 70), (90, 46)], 6))] +
  dome('back', top=2, w=48, cy=44, nape=82))

# Casper Forman: una melena enorme de rizos rojo anaranjado con la raya al medio que le llega a los hombros; ojos grises
# afilados con dos marcas bajo los ojos y gesto serio
C('casper-forman', 'normal', P('#f0502e', '#fbd8c0', iris='#5a6a7a'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=93,
    hairline=[(6, 66), (16, 50), (34, 42), (48, 36), (52, 36), (66, 42), (84, 50), (94, 66)]),
  dome('front', top=-4, w=58, cy=46, n=16, amp=6, soft=True, long=104, flare=6, seed=18) +
  [L([(32, 82), (32, 88)], OUTC, 'f', False, False, 1.0), L([(68, 82), (68, 88)], OUTC, 'f', False, False, 1.0)],
  dome('side', top=-4, w=56, cy=46, n=16, amp=6, soft=True, long=104, flare=6, fr=40, seed=18),
  dome('back', top=-4, w=58, cy=46, n=16, amp=6, soft=True, long=104, flare=6, ends=5, seed=18))

# Caspian Hearken: melena larga negra lisa con la raya al medio hasta los hombros y una trenza baja a un lado con una
# goma; piel tostada, ojos oliva con un trazo naranja y gesto tranquilo
ORG = _c('#e0902a')
C('caspian-hearken', 'normal', P('#1e1a1a', '#c08a60', iris='#7a7a3a'),
  F(eyes='sharp', brows=True, mouth='line', mouth_y=93, hairline=[(6, 70), (16, 52), (34, 42), (50, 36), (66, 42), (84, 52), (94, 70)]),
  dome('front', top=0, w=48, cy=44, long=108, flare=4) + braid(86, 104, 3, 9, 4.5, dx=0.4, tie=_c('#a0602a')) +
  [L([(30, 82), (34, 86)], ORG, 'f', False, False, 1.6), L([(70, 82), (66, 86)], ORG, 'f', False, False, 1.6)],
  dome('side', top=0, w=46, cy=44, long=108, flare=4, fr=40),
  dome('back', top=0, w=48, cy=44, long=108, flare=4) + braid(14, 104, 3, 9, 4.5, dx=-0.4, tie=_c('#a0602a')))

# Cassia Bladecroft: pelo gris en mechones de punta hasta la mandíbula, con un mechón amarillo grande en un lado del
# flequillo; piel morena, ojos azules afilados y ceño
YL = _c('#f0c040')
C('cassia-bladecroft', 'chica', P('#7a7a7a', '#a8724e', iris='#3a6ac8'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=93, hairline=hl(5, 68, 50, 62, lean=-2, jit=3, seed=19)),
  dome('front', top=0, w=50, cy=44, n=9, amp=7, sweep=-0.3, long=90, flare=4, seed=19) +
  [lock([(26, 22), (40, 18), (40, 44), (32, 66), (24, 82, 1), (22, 56)], YL)],
  dome('side', top=0, w=48, cy=44, n=9, amp=7, sweep=-0.3, long=90, flare=4, fr=50, seed=19),
  dome('back', top=0, w=50, cy=44, n=9, amp=7, sweep=-0.3, long=90, flare=4, seed=19) + [lock([(66, 22), (78, 20), (80, 60), (72, 86, 1)], YL, 'b')])

# Cassiel Longstaff: un tupé enorme gris claro como una nube encima, con los lados oscuros cortos; piel morena, cejas
# negras fruncidas, ojos azules y boca seria
DK = _c('#2a2020')
C('cassiel-longstaff', 'normal', P('#c4c0bc', '#a0643e', iris='#3a6aa8', low='#2a2020'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 64), (16, 46), (34, 38), (50, 36), (66, 38), (84, 46), (94, 64)]),
  [L(outline([(10, 70), (8, 44), (20, 28), (80, 28), (92, 44), (90, 70), (80, 56), (20, 56)]), 'low')] +
  [L(blob([(6, 24), (12, 0), (30, -14), (50, -18), (72, -14), (90, 0), (96, 24), (80, 38), (50, 34), (20, 38)], 6))] +
  [L(blob([(56, -10), (84, -4), (94, 20), (78, 32)], 5), 'shade', 'b', False)],
  [L(outline([(8, 72), (4, 46), (20, 30), (60, 30), (60, 58), (50, 74), (26, 84)]), 'low'),
   L(blob([(0, 26), (8, 0), (34, -16), (64, -14), (86, 2), (90, 26), (64, 36), (20, 38)], 6))],
  [L(outline([(10, 76), (8, 44), (20, 28), (80, 28), (92, 44), (90, 76), (50, 84)]), 'low'),
   L(blob([(6, 24), (12, 0), (30, -14), (50, -18), (72, -14), (90, 0), (96, 24), (80, 38), (50, 34), (20, 38)], 6))])

# Castor Fatica: pelo morado alborotado en mechones con un pelo de punta arriba y una horquilla; flequillo largo hasta los
# ojos, ojos grandes turquesa y gesto preocupado
C('castor-fatica', 'normal', P('#7a4a7a', '#fbdcc4', iris='#3ab0b8'),
  F(eyes='big', brows=True, mouth='frown', mouth_y=93, hairline=hl(6, 70, 52, 66, jit=3, seed=20)),
  dome('front', top=0, w=52, cy=44, n=10, amp=7, soft=True, long=88, flare=6, seed=20) +
  [lock([(46, 4), (44, -14, 1), (54, 2)]), L([(28, 50), (34, 54)], _c('#c8c8d0'), 'f', False, False, 2.4)],
  dome('side', top=0, w=50, cy=44, n=10, amp=7, soft=True, long=88, flare=6, fr=56, seed=20) + [lock([(48, 4), (46, -14, 1), (56, 2)])],
  dome('back', top=0, w=52, cy=44, n=10, amp=7, soft=True, long=88, flare=6, seed=20) + [lock([(46, 4), (44, -14, 1), (54, 2)])])

# Cecilia Alabaster (portera): melena castaño claro ondulada hasta los hombros, con la frente despejada; ojos turquesa
# grandes y sonrisa
C('cecilia-alabaster', 'chica', P('#a08a7a', '#fbdcc4', iris='#3ab0c0'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 68), (16, 52), (32, 42), (50, 38), (68, 42), (84, 52), (94, 68)]),
  dome('front', top=0, w=52, cy=44, n=8, amp=6, soft=True, long=100, flare=10, seed=21),
  dome('side', top=0, w=50, cy=44, n=8, amp=6, soft=True, long=100, flare=10, fr=42, seed=21),
  dome('back', top=0, w=52, cy=44, n=8, amp=6, soft=True, long=100, flare=10, seed=21))

# Charlet Namora: melena larga lisa verde oscuro con flequillo recto que le tapa las cejas; gafas finas marrones, labios
# gruesos fruncidos
C('charlet-namora', 'chica', P('#3a5a4a', '#fbe4d4', iris='#2a2a2a'),
  F(eyes='sharp', brows=False, mouth='lips', mouth_y=94, mouth_w=6, glasses=_c('#8a6a3a'), glasses_rect=True,
    hairline=[(6, 70), (14, 66), (50, 66), (86, 66), (94, 70)]),
  dome('front', top=0, w=48, cy=44, long=124, flare=2),
  dome('side', top=0, w=46, cy=44, long=124, flare=2, fr=66),
  dome('back', top=0, w=48, cy=44, long=124, flare=2))

# Charlotte Graceslowe: un gorro de punto azul marino encasquetado hasta las cejas, melenita azul oscura debajo y unas
# gafas redondas blancas enormes; gesto de morritos
NB = _c('#1e3a6e')
C('charlotte-graceslowe', 'chica', P('#1e3a80', '#fbe0d0', iris='#4a2a6a'),
  F(eyes='normal', brows=False, mouth='frown', mouth_y=94, glasses=_c('#f0f0f4'), hairline=[(6, 64), (14, 62), (50, 62), (86, 62), (94, 64)]),
  dome('front', top=10, w=50, cy=50, long=90, flare=2, shade=False) +
  [L(blob([(4, 60), (6, 26), (22, 4), (50, -2), (78, 4), (94, 26), (96, 60), (50, 58)], 6), NB, 'f'),
   L(blob([(4, 50), (50, 46), (96, 50), (96, 62), (50, 58), (4, 62)], 3), _c('#162c56'), 'f', False)],
  dome('side', top=10, w=48, cy=50, long=90, flare=2, fr=62, shade=False) +
  [L(blob([(2, 62), (2, 28), (20, 4), (50, -2), (78, 6), (94, 30), (94, 58), (50, 60)], 6), NB, 'f')],
  dome('back', top=10, w=50, cy=50, long=90, flare=2, shade=False) +
  [L(blob([(4, 62), (6, 26), (22, 4), (50, -2), (78, 4), (94, 26), (96, 62), (50, 60)], 6), NB, 'f')])

# Chaunce Gambell: casi calvo, con el pelo rosado grisáceo rapado al cero; cara redonda, gafas redondas granates, ojos
# cerrados y ceño
C('chaunce-gambell', 'normal', P('#c8a8b0', '#fbd4b4', iris='#2a2020'),
  F(eyes='closed', brows='angry', mouth='frown', mouth_y=95, glasses=_c('#8a2a24'), face_front=face(w=4, chin=102, jaw=3),
    hairline=[(6, 56), (16, 42), (34, 34), (50, 32), (66, 34), (84, 42), (94, 56)]),
  dome('front', top=10, w=44, cy=46, sb=56, shade=False),
  dome('side', top=10, w=42, cy=46, nape=70, fr=36, shade=False),
  dome('back', top=10, w=44, cy=46, nape=70, shade=False))

# Cheery Allende: pelo celeste recogido en un moño alto con flequillo recto, mechones largos a los lados y un tirabuzón
# grande que le cae por un lado; ojos rosas y gesto tranquilo
C('cheery-allende', 'chica', P('#a8d0dc', '#fbe4d8', iris='#c8708a'),
  F(eyes='normal', brows=True, mouth='line', mouth_y=93, hairline=[(6, 70), (14, 62), (50, 60), (86, 62), (94, 70)]),
  [L(ell(50, -2, 16, 12)), L(blob([(8, 70), (-10, 78), (-14, 98), (0, 108), (10, 96), (2, 86), (14, 80)], 6))] +
  dome('front', top=2, w=48, cy=44, sb=60) +
  [lock([(10, 54), (18, 52), (20, 96), (14, 104, 1)], 'mid', 'b'), lock([(90, 54), (82, 52), (80, 96), (86, 104, 1)], 'mid', 'b')],
  [L(ell(42, -2, 15, 12))] + dome('side', top=2, w=46, cy=44, nape=84, fr=60),
  [L(ell(50, -2, 16, 12)), L(blob([(92, 70), (110, 78), (114, 98), (100, 108), (90, 96), (98, 86), (86, 80)], 6))] +
  dome('back', top=2, w=48, cy=44, nape=84))

# Chiana Fielder: melena verde menta salvaje en mechones ondulados de punta, con una coleta alta despeinada; ojos
# amarillos grandes y boca abierta de alegría
C('chiana-fielder', 'chica', P('#30c090', '#fbdcc8', iris='#e0a020'),
  F(eyes='big', brows=True, mouth='grin', mouth_y=93, hairline=hl(6, 70, 50, 64, jit=4, seed=22)),
  [L(outline([(36, 8), (28, -10, 1), (40, -8), (42, -26, 1), (52, -10), (62, -22, 1), (64, -4), (74, -8, 1), (66, 10)]))] +
  dome('front', top=0, w=56, cy=46, n=12, amp=9, soft=True, long=96, flare=10, seed=22),
  [L(outline([(30, 10), (20, -8, 1), (34, -6), (40, -24, 1), (50, -8), (56, -18, 1), (58, 6)]))] +
  dome('side', top=0, w=54, cy=46, n=12, amp=9, soft=True, long=96, flare=10, fr=56, seed=22),
  [L(outline([(36, 8), (28, -10, 1), (40, -8), (42, -26, 1), (52, -10), (62, -22, 1), (64, -4), (74, -8, 1), (66, 10)]))] +
  dome('back', top=0, w=56, cy=46, n=12, amp=9, soft=True, long=96, flare=10, ends=5, seed=22))

# Choco Racketfeld: pelo castaño rosado recogido en un moño alto, con flequillo y dos mechones finos a los lados; ojos
# azules grandes y gesto serio
C('choco-racketfeld', 'chica', P('#b89890', '#fbe0d4', iris='#4a7ab0'),
  F(eyes='big', brows=True, mouth='frown', mouth_y=93, hairline=hl(4, 66, 54, 62, seed=23)),
  [L(ell(50, -6, 13, 11))] + dome('front', top=2, w=46, cy=44, sb=60) +
  [lock([(16, 56), (20, 54), (22, 90), (18, 96, 1)], 'mid', 'b'), lock([(84, 56), (80, 54), (78, 90), (82, 96, 1)], 'mid', 'b')],
  [L(ell(40, -6, 12, 11))] + dome('side', top=2, w=44, cy=44, nape=82, fr=58),
  [L(ell(50, -6, 13, 11))] + dome('back', top=2, w=46, cy=44, nape=82))

# Cid Drewend: pelo azul corto peinado hacia atrás con pico en la frente; cejas azules, ojos entornados, media sonrisa
# torcida y piel tostada
C('cid-drewend', 'normal', P('#2a4ab0', '#e0a87a', iris='#2a3a6a', brow='#2a4ab0'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=94, hairline=[(6, 60), (16, 44), (34, 40), (50, 48), (66, 40), (84, 44), (94, 60)]),
  dome('front', top=6, w=44, cy=46, sb=60),
  dome('side', top=6, w=42, cy=46, nape=78, fr=44),
  dome('back', top=6, w=44, cy=46, nape=78))

# Circe Roundella: media melena malva en rizos abombados con un remolino en espiral arriba; ojos tristones con pestañas y
# boca pequeña
C('circe-roundella', 'chica', P('#a87080', '#fbdcd0', iris='#3a3a5a'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=93, hairline=[(6, 68), (14, 56), (30, 50), (50, 54), (70, 50), (86, 56), (94, 68)]),
  dome('front', top=0, w=54, cy=46, n=10, amp=6, soft=True, long=92, flare=8, seed=24) +
  [L(quad((44, 30), (54, 18), (62, 30)) + quad((62, 30), (52, 38), (48, 28))[1:], 'shade', 'f', False, False, 1.6)] + eyeshadow(72, _c('#a85080')),
  dome('side', top=0, w=52, cy=46, n=10, amp=6, soft=True, long=92, flare=8, fr=52, seed=24),
  dome('back', top=0, w=54, cy=46, n=10, amp=6, soft=True, long=92, flare=8, seed=24))

# Clarissa Gimmich: media melena lila plateada en ondas con un mechón que le tapa un ojo; ojos verdes afilados y gesto
# serio
C('clarissa-gimmich', 'chica', P('#c8c8d8', '#fbdcc4', iris='#3a9a7a'),
  F(eyes='sharp', brows=True, mouth='line', mouth_y=93, hairline=[(6, 66), (16, 50), (34, 42), (50, 44), (62, 48), (74, 54), (86, 56), (94, 66)]),
  dome('front', top=0, w=54, cy=46, n=10, amp=6, soft=True, long=94, flare=10, seed=25) +
  [lock([(48, 34), (64, 40), (66, 66), (60, 82, 1), (56, 62)])],
  dome('side', top=0, w=52, cy=46, n=10, amp=6, soft=True, long=94, flare=10, fr=48, seed=25),
  dome('back', top=0, w=54, cy=46, n=10, amp=6, soft=True, long=94, flare=10, seed=25))

# Claudette Clackenoff: melenita castaño claro con flequillo y dos mechones laterales que se abren como orejas de perro,
# con un lazo azul y rojo arriba; ojos grandes con estrellas y boca de gato
BLB = _c('#5a8ad8')
C('claudette-clackenoff', 'chica', P('#d4a080', '#fbdccc', iris='#3a3a6a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=hl(5, 66, 52, 62, seed=26)),
  [lock([(42, 6), (22, -16), (30, -2), (46, 4)], BLB), lock([(58, 6), (78, -16), (70, -2), (54, 4)], RED)] +
  dome('front', top=2, w=48, cy=44, sb=64) +
  [lock([(8, 52), (16, 56), (2, 90), (-12, 96, 1), (-4, 80)], 'mid', 'b'), lock([(92, 52), (84, 56), (98, 90), (112, 96, 1), (104, 80)], 'mid', 'b')],
  [lock([(44, 6), (30, -16), (34, -2), (50, 4)], BLB)] + dome('side', top=2, w=46, cy=44, nape=84, fr=60) +
  [lock([(30, 52), (40, 56), (28, 90), (16, 96, 1), (22, 80)], 'mid', 'b')],
  [lock([(42, 6), (22, -16), (30, -2), (46, 4)], BLB), lock([(58, 6), (78, -16), (70, -2), (54, 4)], RED)] +
  dome('back', top=2, w=48, cy=44, nape=84) +
  [lock([(8, 52), (16, 56), (2, 90), (-12, 96, 1), (-4, 80)], 'mid', 'b'), lock([(92, 52), (84, 56), (98, 90), (112, 96, 1), (104, 80)], 'mid', 'b')])

# Cleara Sounds: melena larga granate oscuro con flequillo y dos mechones de punta como cuernos, rizada en las puntas;
# auriculares rosas, ojos grandes rosas y sonrisa
HP = _c('#e0408a')
C('cleara-sounds', 'chica', P('#5a2234', '#fbe4dc', iris='#c0507a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 68), (14, 58), (30, 60), (40, 52), (50, 58), (60, 52), (70, 60), (86, 58), (94, 68)]),
  dome('front', top=2, w=50, cy=44, long=112, flare=6) +
  [L(ell(8, 112, 6, 7)), L(ell(92, 112, 6, 7)),
   L(quad((10, 50), (50, -6), (90, 50)), HP, 'f', False, False, 3.2), L(blob([(4, 60), (14, 60), (14, 80), (4, 80)], 3), HP, 'f'),
   L(blob([(86, 60), (96, 60), (96, 80), (86, 80)], 3), HP, 'f')],
  dome('side', top=2, w=48, cy=44, long=112, flare=6, fr=58) + [L(ell(44, 68, 9, 10), HP, 'f'), L(quad((44, 58), (40, 10), (60, -2)), HP, 'f', False, False, 3.2)],
  dome('back', top=2, w=50, cy=44, long=112, flare=6) + [L(quad((10, 50), (50, -6), (90, 50)), HP, 'b', False, False, 3.2)])

# Cleon Balogh: melena castaña ondulada con la raya al medio hasta los hombros, cejas gruesas muy fruncidas, ojos grises
# y boca en ceño
C('cleon-balogh', 'normal', P('#7a6248', '#fbdcc0', iris='#5a6a8a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95,
    hairline=[(6, 66), (16, 50), (34, 40), (48, 36), (52, 36), (66, 40), (84, 50), (94, 66)]),
  dome('front', top=0, w=50, cy=44, n=6, amp=5, soft=True, long=100, flare=12, seed=27) +
  [L([(26, 62), (44, 66)], OUTC, 'f', False, False, 3.6), L([(74, 62), (56, 66)], OUTC, 'f', False, False, 3.6)],
  dome('side', top=0, w=48, cy=44, n=6, amp=5, soft=True, long=100, flare=12, fr=40, seed=27),
  dome('back', top=0, w=50, cy=44, n=6, amp=5, soft=True, long=100, flare=12, seed=27))

# Clyde Dalen: media melena en casco con la raya al medio, castaña arriba y amarilla en las puntas que le enmarcan la cara;
# ojos amarillos afilados y gesto serio
YE = _c('#f0b030')
C('clyde-dalen', 'normal', P('#a06a3a', '#fbe4d0', iris='#c8901e'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93,
    hairline=[(6, 70), (16, 60), (30, 56), (44, 46), (50, 40), (56, 46), (70, 56), (84, 60), (94, 70)]),
  dome('front', top=0, w=50, cy=44, long=86, flare=4) +
  [L(blob([(4, 60), (22, 56), (34, 66), (26, 78), (8, 84)], 4), YE, 'b', False), L(blob([(96, 60), (78, 56), (66, 66), (74, 78), (92, 84)], 4), YE, 'b', False),
   lock([(20, 44), (36, 50), (40, 64, 1), (28, 58)], YE), lock([(80, 44), (64, 50), (60, 64, 1), (72, 58)], YE)],
  dome('side', top=0, w=48, cy=44, long=86, flare=4, fr=46) + [L(blob([(10, 66), (50, 64), (50, 82), (10, 82)], 4), YE, 'b', False)],
  dome('back', top=0, w=50, cy=44, long=86, flare=4) + [L(blob([(8, 68), (92, 68), (90, 82), (10, 82)], 4), YE, 'b', False)])

# Coby Cogsworth: pelo verde lima echado hacia delante sobre una base celeste clara que asoma por los lados; ojos
# turquesa afilados y gesto serio
LB = _c('#b0e0e8')
C('coby-cogsworth', 'normal', P('#c8e050', '#fbe0d0', iris='#2ab0b8'),
  F(eyes='sharp', brows=True, mouth='frown', mouth_y=93, hairline=hl(5, 64, 52, 66, jit=3, seed=28)),
  [L(blob([(2, 64), (2, 30), (20, 10), (50, 6), (80, 10), (98, 30), (98, 64), (80, 54), (20, 54)], 6), LB)] +
  dome('front', top=-2, w=42, cy=40, n=6, amp=6, soft=True, sb=60, seed=28) + [lock([(42, 30), (56, 30), (54, 60), (48, 72, 1)])],
  [L(blob([(2, 70), (0, 32), (20, 8), (60, 6), (88, 24), (92, 48), (60, 56), (30, 80)], 6), LB)] +
  dome('side', top=-2, w=40, cy=40, n=6, amp=6, soft=True, nape=70, fr=56, seed=28),
  [L(blob([(2, 70), (2, 30), (20, 10), (50, 6), (80, 10), (98, 30), (98, 70), (50, 86)], 6), LB)] +
  dome('back', top=-2, w=42, cy=40, n=6, amp=6, soft=True, nape=70, seed=28))

# Coco Lajoie: melenita negra morada con flequillo y una horquilla clara; cara redonda y ancha, nariz de cerdito rosa,
# rubor y una sonrisa grande
C('coco-lajoie', 'chica', P('#2a2238', '#fbd8c0', iris='#2a8a6a', nose='#f0a0a0'),
  F(eyes='dot', brows=True, mouth='smile', mouth_y=95, mouth_w=10, face_front=face(w=8, chin=102, jaw=6), face_side=face_side(chin=2, jaw=4),
    nose=(50, 86, 5), hairline=[(6, 66), (14, 60), (50, 58), (86, 60), (94, 66)]),
  dome('front', top=6, w=52, cy=48, long=92, flare=6) + blush(88, 24) +
  [L([(70, 50), (74, 60)], _c('#f0e8d0'), 'f', False, False, 2.4), L(quad((38, 94), (50, 102), (62, 94)), OUTC, 'f', False, False, 1.6)],
  dome('side', top=6, w=50, cy=48, long=92, flare=6, fr=58) + blush(side=True),
  dome('back', top=6, w=52, cy=48, long=92, flare=6))

# Cocoa Bounce: pelo beige en forma de seta con flequillo recto; piel morena, ojos verdes azulados grandes, rubor, nariz
# roja y sonrisa pequeña
C('cocoa-bounce', 'chica', P('#d4ccb0', '#a8704a', iris='#3a8a8a', nose='#e05a5a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, nose=(50, 84, 2.4), hairline=[(6, 64), (14, 60), (50, 58), (86, 60), (94, 64)]),
  dome('front', top=0, w=54, cy=46, sb=60) + [L(blob([(-6, 58), (10, 50), (14, 64), (0, 70)], 4)), L(blob([(106, 58), (90, 50), (86, 64), (100, 70)], 4))] + blush(),
  dome('side', top=0, w=52, cy=46, nape=74, fr=58) + [L(blob([(2, 60), (20, 52), (24, 66), (6, 72)], 4))] + blush(side=True),
  dome('back', top=0, w=54, cy=46, nape=74) + [L(blob([(-6, 58), (10, 50), (14, 64), (0, 70)], 4)), L(blob([(106, 58), (90, 50), (86, 64), (100, 70)], 4))])

# Codey Presto: pelo oliva corto peinado hacia arriba, cejas gruesas, unas gafas redondas negras muy gruesas y boca en
# ceño
C('codey-presto', 'normal', P('#6a6a40', '#fbdcc4', iris='#4a4a8a'),
  F(eyes='round', brows=True, mouth='frown', mouth_y=95, glasses=_c('#1a1a1e'), nose=(50, 84, 2.4),
    hairline=[(6, 60), (16, 44), (34, 40), (50, 42), (66, 40), (84, 44), (94, 60)]),
  dome('front', top=0, w=44, cy=44, n=5, amp=6, sweep=0.4, sb=60, seed=29) +
  [L(ell(36, 75, 10, 8) + [ell(36, 75, 10, 8)[0]], _c('#1a1a1e'), 'f', False, False, 2.6),
   L(ell(64, 75, 10, 8) + [ell(64, 75, 10, 8)[0]], _c('#1a1a1e'), 'f', False, False, 2.6)],
  dome('side', top=0, w=42, cy=44, n=5, amp=6, sweep=0.4, nape=78, fr=44, seed=29),
  dome('back', top=0, w=44, cy=44, n=5, amp=6, sweep=0.4, nape=78, seed=29))

# Colette Brushmont: media melena negra hasta los hombros con flequillo recto y las puntas abiertas hacia fuera; ojos
# grises y gesto serio
C('colette-brushmont', 'chica', P('#1e1a2a', '#fbe4d8', iris='#4a5a6a'),
  F(eyes='normal', brows=True, mouth='line', mouth_y=93, hairline=[(6, 66), (14, 60), (50, 62), (86, 60), (94, 66)]),
  dome('front', top=0, w=50, cy=44, long=100, flare=12, ends=4),
  dome('side', top=0, w=48, cy=44, long=100, flare=12, fr=60),
  dome('back', top=0, w=50, cy=44, long=100, flare=12, ends=4))

# Colleen Evenholm: pelo negro peinado hacia atrás con la frente despejada y dos mechones largos a los lados hasta la
# barbilla; gafas rectangulares azules y sonrisa
C('colleen-evenholm', 'chica', P('#1e1a2a', '#fbe4d4', iris='#3a6a6a'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=92, glasses=_c('#1e3aa0'), glasses_rect=True,
    hairline=[(6, 62), (16, 46), (34, 38), (50, 36), (66, 38), (84, 46), (94, 62)]),
  dome('front', top=2, w=48, cy=44, sb=62) +
  [lock([(12, 48), (22, 44), (24, 76), (18, 100, 1), (12, 80)], 'mid', 'b'), lock([(88, 48), (78, 44), (76, 76), (82, 100, 1), (88, 80)], 'mid', 'b')],
  dome('side', top=2, w=46, cy=44, nape=86, fr=40),
  dome('back', top=2, w=48, cy=44, nape=86))

# Colm Dawdlin: melena morada grisácea oscura lisa con un flequillo largo que le tapa un ojo; gafas rectangulares
# opacas blancas y media sonrisa
WG = _c('#f4f4f6')
C('colm-dawdlin', 'normal', P('#4a4458', '#e8b890', iris='#2a2a2a'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=93, hairline=[(6, 66), (14, 52), (30, 46), (44, 44), (58, 60), (66, 76), (76, 60), (88, 54), (94, 66)]),
  dome('front', top=0, w=50, cy=44, long=94, flare=2) +
  [L(blob([(26, 70), (46, 70), (46, 80), (26, 80)], 2), WG, 'f', True), L(blob([(54, 70), (74, 70), (74, 80), (54, 80)], 2), WG, 'f', True),
   lock([(40, 30), (60, 36), (66, 62), (64, 86, 1), (56, 66), (46, 48)])],
  dome('side', top=0, w=48, cy=44, long=94, flare=2, fr=50) + [L(blob([(72, 70), (88, 70), (88, 80), (72, 80)], 2), WG, 'f', True)],
  dome('back', top=0, w=50, cy=44, long=94, flare=2))

# Colter Fairburn: un tupé alto granate oscuro revuelto con los lados rapados y la nuca rubia; ojos afilados grises y ceño
C('colter-fairburn', 'normal', P('#6a2a2a', '#fbd8c0', iris='#5a6a9a', low='#c8a050'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 62), (16, 50), (30, 46), (50, 44), (70, 46), (84, 50), (94, 62)]),
  [L(outline([(10, 66), (8, 44), (20, 38), (80, 38), (92, 44), (90, 66), (80, 54), (20, 54)]), 'low')] +
  dome('front', top=-14, w=40, cy=26, n=10, amp=6, soft=True, sb=46, seed=30),
  [L(outline([(6, 70), (6, 44), (24, 38), (60, 40), (60, 56), (50, 70), (26, 80)]), 'low')] +
  dome('side', top=-14, w=40, cy=26, n=10, amp=6, soft=True, nape=48, fr=42, seed=30),
  [L(outline([(10, 74), (8, 44), (20, 38), (80, 38), (92, 44), (90, 74), (50, 82)]), 'low')] +
  dome('back', top=-14, w=40, cy=26, n=10, amp=6, soft=True, nape=48, seed=30))

# Cora Inkton: melenita malva rosada con flequillo recto y las puntas abiertas hacia fuera; pecas, ojos verdosos y boca
# de gato
C('cora-inkton', 'chica', P('#b88a98', '#fbe0d4', iris='#3a7a6a'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 66), (14, 62), (50, 62), (86, 62), (94, 66)]),
  dome('front', top=2, w=48, cy=44, long=88, flare=16, ends=3) + freckles(84, 18),
  dome('side', top=2, w=46, cy=44, long=88, flare=16, fr=62) + freckles(side=True),
  dome('back', top=2, w=48, cy=44, long=88, flare=16, ends=3))

# Coraline Quisittor: pelo gris pardo muy corto pegado a la cabeza, gafas negras rectangulares y gesto neutro
C('coraline-quisittor', 'chica', P('#7a6a64', '#fbe4d4', iris='#3a2a2a'),
  F(eyes='normal', brows=True, mouth='line', mouth_y=93, glasses=_c('#1a1a1e'), glasses_rect=True,
    hairline=[(6, 60), (16, 44), (34, 38), (50, 36), (66, 38), (84, 44), (94, 60)]),
  dome('front', top=4, w=46, cy=46, sb=64),
  dome('side', top=4, w=44, cy=46, nape=82, fr=40),
  dome('back', top=4, w=46, cy=46, nape=82))

# Corday Dremin: pelo verde azulado revuelto en mechones con el flequillo sobre los ojos; ojos entornados de sueño y boca
# en ceño
C('corday-dremin', 'normal', P('#2a9a9a', '#fbdcc0', iris='#2a5a5a'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=93, hairline=hl(6, 68, 54, 66, jit=3, seed=31)),
  dome('front', top=2, w=50, cy=44, n=8, amp=8, soft=True, long=84, flare=8, seed=31) +
  [L([(26, 72), (44, 74)], OUTC, 'f', False, False, 2.0), L([(74, 72), (56, 74)], OUTC, 'f', False, False, 2.0)],
  dome('side', top=2, w=48, cy=44, n=8, amp=8, soft=True, long=84, flare=8, fr=58, seed=31),
  dome('back', top=2, w=48, cy=44, n=8, amp=8, soft=True, long=84, flare=8, seed=31))

# Cornelia Hoopett: melenita verde menta con el flequillo partido y dos grandes rodetes enrollados como caracolas a los
# lados de la cara, con un agujero en el centro; ojos grises y boca pequeña
MD = _c('#4a8a6a')
def _shell(x, y, s=1):
    return [L(ell(x, y, 13, 11), 'mid'), L(ell(x + s * 2, y + 1, 4, 3.4), MD, 'b', True)]
C('cornelia-hoopett', 'chica', P('#80c0a0', '#fbe4d8', iris='#4a4a4a'),
  F(eyes='big', brows=True, mouth='frown', mouth_y=93, hairline=[(6, 66), (14, 56), (30, 52), (44, 58), (54, 50), (70, 54), (86, 56), (94, 66)]),
  dome('front', top=2, w=48, cy=44, sb=70) + [x for p in (_shell(6, 86, 1), _shell(94, 86, -1), _shell(14, 104, 1), _shell(86, 104, -1)) for x in p],
  dome('side', top=2, w=46, cy=44, nape=84, fr=52) + _shell(36, 88, 1) + _shell(44, 104, 1),
  dome('back', top=2, w=48, cy=44, nape=84) + [x for p in (_shell(6, 86, -1), _shell(94, 86, 1), _shell(14, 104, -1), _shell(86, 104, 1)) for x in p])
