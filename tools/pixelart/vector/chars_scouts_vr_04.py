"""Ojeadores de Victory Road (scouts-vr), tanda 04: dibujados a partir de su retrato; claves 'scouts-vr:<id>'.

Solo Flynn Duval tiene modelo 3D (el mismo personaje): el resto sale del retrato, con el perfil y la espalda deducidos.
Reutiliza dome/hl/face de la tanda 09 de IE1, bowl3/skull3 de la 02 de IE3, cap/band de la 06 de IE3 y gafas de IE1/IE2."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401
from chars_scouts_ie1_09 import dome, hl, face, face_side, mark, _c
from chars_scouts_ie1_03 import rect_specs, freckles, blush
from chars_scouts_ie2_03 import round_glasses
from chars_scouts_ie3_02 import bowl3, skull3
from chars_scouts_ie3_06 import cap, band

WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)


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


def D(**k):
    """El mismo pelo (dome) en las tres vistas; nape y fr solo cuentan de perfil y de espaldas."""
    fk = {a: b for a, b in k.items() if a not in ('nape', 'fr', 'back_n')}
    sk = {a: b for a, b in k.items() if a not in ('sb', 'flare', 'back_n', 'ends')}
    bk = {a: b for a, b in k.items() if a not in ('sb', 'fr')}
    return dome('front', **fk), dome('side', **sk), dome('back', **bk)


def fr(pts, c='mid'):
    """Mechón por delante de la cara."""
    return L(outline(pts), c, 'f')


def tri(pts, c, z='f'):
    return L(outline(pts), c, z)


def lid_line(y=74, c=OUTC, w=2.4):
    """Ojos cerrados de felicidad (arcos ^) dibujados a mano."""
    return [L(quad((cx - 6, y + 2), (cx, y - 3), (cx + 6, y + 2)), c, 'f', False, False, w) for cx in (36, 64)]


def side_lid(y=74, c=OUTC):
    return [L(quad((76, y + 2), (81, y - 3), (86, y + 2)), c, 'f', False, False, 2.4)]


def tie_tail(view, x, y, c, ln=-30):
    """Coleta larga que cae por detrás (de perfil hacia atrás y de espaldas por el centro)."""
    if view == 'side':
        return [L(outline([(x, y - 4), (x - 14, y + 6), (x - 22, y + 30), (x - 16, y + 58, 1), (x - 8, y + 30), (x + 4, y + 6)]), c)]
    return [L(outline([(x - 6, y), (x + 6, y), (x + 8, y + 30), (x, y + 60, 1), (x - 8, y + 30)]), c)]


# ------------------------------------------------------------------ jugadores

# Fang Arzola: calvo, una franja corta azul marino en pico en lo alto de la cabeza; piel tostada, mandíbula ancha y
# sonrisa de satisfacción con los ojos entrecerrados
NV = _c('#2c3a6a')
C('fang-arzola', 'corpulento', P('#2c3a6a', '#f0c48c', iris='#4a5a8a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=False, face_front=face(w=4, chin=104, jaw=4), face_side=face_side(chin=3, jaw=3)),
  skull3('front') + [tri([(38, 10), (50, 4), (62, 10), (56, 22), (50, 34, 1), (44, 22)], NV)],
  skull3('side') + [tri([(28, 6), (48, 0), (70, 6), (64, 16), (36, 16)], NV)],
  skull3('back') + [tri([(40, 8), (50, 4), (60, 8), (58, 30), (42, 30)], NV)])

# Farah Tigressa: melena corta verde en casco, con raya al medio y dos franjas amarillo pálido en onda como rayas de
# tigre; ojos grises serios
YP = _c('#e4e09a')
f_, s_, b_ = bowl3('front', top=0, side=94, nape=96, w=2, fringe=56), bowl3('side', top=0, nape=96, w=2, fringe=56), bowl3('back', top=0, nape=96, w=2)
C('farah-tigressa', 'chica', P('#3a9a62', '#f8d4b8', iris='#5a6478', shade='#2a7a4a'),
  F(eyes='normal', brows=True, mouth='frown', mouth_y=92, hairline=[(8, 58), (30, 54), (48, 44), (50, 40), (52, 44), (70, 54), (92, 58)]),
  f_ + [L(quad((14, 40), (24, 50), (32, 40)) + quad((32, 40), (40, 50), (46, 40))[1:], YP, 'f', False, False, 2.6),
        L(quad((54, 40), (60, 50), (68, 40)) + quad((68, 40), (76, 50), (86, 40))[1:], YP, 'f', False, False, 2.6),
        L([(50, 4), (50, 42)], 'shade', 'f', False, False, 1.2)],
  s_ + [L(quad((30, 30), (46, 40), (62, 30)) + quad((62, 30), (72, 40), (82, 32))[1:], YP, 'f', False, False, 2.6)],
  b_ + [L(quad((14, 44), (32, 52), (50, 44)) + quad((50, 44), (68, 52), (86, 44))[1:], YP, 'f', False, False, 2.6)])

# Faris Creed: tazón negro de flequillo recto hasta las cejas y unas gafas redondas enormes de montura negra gruesa
C('faris-creed', 'normal', P('#1c1c22', '#f4c8a0', iris='#606870'),
  F(eyes='normal', brows=False, mouth='frown', mouth_y=93, hairline=[(8, 62), (92, 62)]),
  bowl3('front', top=4, side=70, fringe=62, w=1) + round_glasses('front', BLACK, y=77, r=9, w=3.4),
  bowl3('side', top=4, nape=86, fringe=62, w=1) + round_glasses('side', BLACK, y=77, r=9, w=3.4),
  bowl3('back', top=4, nape=86, w=1))

# Farran Corsa: melena verde azulado muy oscuro en seta, que se abre hacia fuera por abajo y le enmarca la cara;
# ojos cerrados con sombra amarilla y sonrisa
YL = _c('#e0b830')
C('farran-corsa', 'normal', P('#22465a', '#f6d0b8', shade='#183444'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=92, hairline=[(8, 60), (24, 54), (50, 50), (76, 54), (92, 60)]),
  [L(outline([(-6, 96), (6, 70), (8, 30), (28, 6), (50, 0), (72, 6), (92, 30), (94, 70), (106, 96), (82, 84), (80, 56), (20, 56), (18, 84)])),
   L(outline([(60, 4), (88, 26), (94, 70), (104, 94), (84, 82), (80, 50)]), 'shade', 'b', False)] +
  [L(quad((30, 76), (36, 72), (42, 76)), YL, 'f', False, False, 2.4), L(quad((58, 76), (64, 72), (70, 76)), YL, 'f', False, False, 2.4)] + lid_line(76),
  [L(outline([(84, 54), (88, 34), (74, 8), (46, 0), (20, 8), (4, 32), (0, 70), (-8, 100), (18, 94), (40, 88), (54, 80), (60, 58), (70, 54)]))] + side_lid(76),
  [L(outline([(-6, 98), (6, 70), (8, 30), (28, 6), (50, 0), (72, 6), (92, 30), (94, 70), (106, 98), (70, 94), (50, 96), (30, 94)])),
   L(outline([(60, 6), (88, 28), (94, 70), (104, 96), (70, 92), (64, 40)]), 'shade', 'b', False)])

# Felicia Felton: melena larga castaña lisa con flequillo recto y dos horquillas blancas a cada lado; ojos castaños grandes
fF, sF, bF = D(top=2, w=46, cy=44, long=120, flare=4, fr=58, seed=3)
C('felicia-felton', 'chica', P('#9a7048', '#f8d6bc', iris='#7a5232'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=[(8, 62), (92, 62)]),
  fF + [L([(28, 60), (34, 60)], WHITE, 'f', False, False, 2.6), L([(66, 60), (72, 60)], WHITE, 'f', False, False, 2.6)],
  sF + [L([(68, 58), (74, 60)], WHITE, 'f', False, False, 2.6)],
  bF)

# Fenric Wulfgang: melena enorme celeste pálido en pinchos que salen hacia los lados, con mechones azul oscuro que le caen
# por el centro de la cara; marcas de pintura en las mejillas y ojos amarillos de mirada torva
DK = _c('#3a5068')
fW, sW, bW = D(top=-4, w=52, cy=46, n=12, amp=12, seed=8, sb=78, nape=92, fr=50)
C('fenric-wulfgang', 'normal', P('#bcdcdc', '#e8c8a8', iris='#b8a040', shade='#94bcbc'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=94, hairline=[(8, 66), (30, 54), (50, 50), (70, 54), (92, 66)]),
  fW + [fr([(40, 30), (52, 24), (62, 36), (58, 62), (54, 80, 1), (50, 60), (44, 66, 1), (42, 48)], DK),
        L(quad((26, 82), (32, 86), (38, 82)), DK, 'f', False, False, 1.6), L(quad((62, 82), (68, 86), (74, 82)), DK, 'f', False, False, 1.6)],
  sW + [fr([(66, 34), (86, 40), (88, 62), (84, 74, 1), (78, 56)], DK)],
  bW)

# Feodor Wayte: pelo rojo largo echado todo a un lado en un tupé ladeado, con el otro lado rapado gris; rayas rojas
# bajo los ojos azules y ceño de enfado
GR = _c('#7a7e88')
C('feodor-wayte', 'normal', P('#c8382a', '#e8a070', iris='#3a6ad0', shade='#a02a20'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(8, 60), (20, 52), (40, 48), (60, 46), (80, 50), (92, 60)]),
  [L(outline([(14, 60), (12, 34), (26, 16), (40, 14), (40, 50), (22, 56)]), GR),
   L(outline([(30, 52), (32, 14), (52, 2), (76, 4), (94, 22), (98, 50), (96, 86, 1), (86, 64), (80, 46), (60, 40), (44, 46)])),
   L(outline([(62, 6), (90, 22), (96, 60), (94, 84), (82, 50)]), 'shade', 'b', False),
   L([(24, 84), (40, 82)], _c('#c8302a'), 'f', False, False, 1.6), L([(60, 82), (76, 84)], _c('#c8302a'), 'f', False, False, 1.6)],
  [L(outline([(52, 62), (54, 40), (70, 30), (90, 30), (94, 14), (76, 2), (48, 0), (24, 6), (8, 24), (14, 40), (40, 44), (48, 60)])),
   L(outline([(8, 30), (40, 40), (44, 62), (30, 76), (8, 64)]), GR)],
  [L(outline([(10, 82), (8, 40), (20, 16), (50, 4), (80, 16), (94, 40), (96, 90, 1), (70, 80), (50, 82), (30, 80)])),
   L(outline([(10, 40), (36, 30), (40, 82), (12, 80)]), GR)])

# Ferdy Fenwick: pelo blanco con un mechón largo que le tapa un ojo y la parte de abajo de un lado teñida de rojo;
# ojos de párpado caído
RD = _c('#d03a48')
fD, sD, bD = D(top=2, w=46, cy=44, n=4, amp=6, sweep=-0.3, seed=11, sb=84, nape=88, fr=52, soft=True)
C('ferdy-fenwick', 'normal', P('#eceaf0', '#f6d6c4', iris='#3a4a3a', shade='#c4c4d0'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=93, hairline=[(8, 62), (30, 56), (60, 54), (92, 62)]),
  [L(outline([(6, 90), (8, 60), (18, 60), (22, 92, 1)]), RD)] + fD + [fr([(36, 40), (70, 34), (84, 52), (72, 78, 1), (62, 58), (50, 52)])],
  sD + [L(outline([(10, 70), (30, 64), (40, 90), (16, 92)]), RD)],
  bD + [L(outline([(70, 60), (92, 60), (94, 88), (72, 86)]), RD)])

# Fergus Lougdon: calvo y grandote, con un único mechón azul marino que le sale de un lado y se riza hacia arriba;
# nariz rosada, ceño de enfado y morros
C('fergus-lougdon', 'corpulento', P('#22285a', '#f4d4c4', iris='#4a5a6a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, hairline=False, nose=(50, 86, 3.6), face_front=face(w=5, chin=106, jaw=3), face_side=face_side(chin=4)),
  skull3('front') + [tri([(56, 22), (62, 6), (78, 2), (86, 14, 1), (74, 12), (70, 40), (66, 56, 1), (60, 34)], 'mid')],
  skull3('side') + [tri([(40, 10), (54, -2), (70, 0), (78, 10, 1), (60, 8), (50, 24)], 'mid')],
  skull3('back') + [tri([(30, 18), (38, 4), (24, 0), (16, 10, 1)], 'mid')])

# Fermin Dealitz: pelo corto azul marino pegado, cara ancha y mofletuda, gafas de montura fina gris y gesto serio
fM, sM, bM = D(top=6, w=44, cy=42, sb=60, nape=82, fr=50)
C('fermin-dealitz', 'corpulento', P('#20244a', '#f8e0d6', iris='#3a3a4a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, hairline=[(8, 58), (30, 50), (50, 52), (70, 50), (92, 58)], face_front=face(w=6, chin=104, jaw=4)),
  fM + rect_specs('front', _c('#8a96a8'), y=77, w=1.6), sM + rect_specs('side', _c('#8a96a8'), y=77, w=1.6), bM)

# Ferron Rockfort: piel oscura, pelo azul marino en pinchos de punta hacia arriba y patillas; ojos cerrados y gran sonrisa
fR, sR, bR = D(top=-10, w=42, cy=40, n=7, amp=14, seed=13, sb=72, nape=82, fr=48)
C('ferron-rockfort', 'normal', P('#2e3450', '#8a5a3a', shade='#20263e'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=94, hairline=[(8, 66), (24, 52), (50, 44), (76, 52), (92, 66)], face_front=face(chin=104, jaw=2)),
  fR + lid_line(76), sR + side_lid(76), bR)

# Figgo Balpark: tupé abombado verde oliva oscuro con una media luna crema en lo alto, cejas gruesas y sonrisa abierta
CR = _c('#e4c88a')
fG, sG, bG = D(top=-6, w=48, cy=40, sb=62, nape=82, fr=46)
C('figgo-balpark', 'normal', P('#44463a', '#f6caa0', iris='#7a6a2a'),
  F(eyes='normal', brows=False, mouth='grin', mouth_y=94, hairline=[(8, 60), (30, 50), (50, 46), (70, 50), (92, 60)]),
  fG + [L(outline([(30, 0), (40, -2), (52, 4), (44, 6), (40, 24), (46, 36), (34, 30)]), CR, 'f'),
        L(blob([(26, 62), (40, 58), (44, 64), (28, 66)], 4), 'mid', 'f', False), L(blob([(56, 64), (60, 58), (74, 62), (72, 66)], 4), 'mid', 'f', False)],
  sG + [L(outline([(40, -4), (60, -2), (62, 8), (44, 8)]), CR, 'f')],
  bG + [L(outline([(36, 0), (54, -2), (60, 10), (40, 14)]), CR, 'f')])

# Finck Zaplan: pelo corto gris azulado, cara redonda de mofletes, cejas tristes y ojos llorosos
fZ, sZ, bZ = D(top=6, w=46, cy=42, n=6, amp=4, soft=True, seed=15, sb=60, nape=84, fr=50)
C('finck-zaplan', 'normal', P('#4a5a70', '#f8dcc8', iris='#8a9aa0'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=94, hairline=[(8, 58), (30, 52), (50, 50), (70, 52), (92, 58)], face_front=face(w=4, chin=102)),
  fZ + [L([(28, 66), (42, 61)], 'deep', 'f', False, False, 2.6), L([(72, 66), (58, 61)], 'deep', 'f', False, False, 2.6),
        L(ell(30, 84, 2, 3), _c('#a8d8f0'), 'f', False), L(ell(70, 84, 2, 3), _c('#a8d8f0'), 'f', False)],
  sZ, bZ)

# Finley Brooks: señor moreno con el pelo gris en un tupé alto en ola hacia atrás, patillas que se juntan con la barba
fB, sB, bB = D(top=4, w=44, cy=42, sb=70, nape=82, fr=48)
SW = [(30, 14), (44, -4), (66, -14), (88, -8, 1), (70, -2), (64, 20)]
C('finley-brooks', 'normal', P('#8a8a90', '#b88660', iris='#3a3a4a'),
  F(eyes='normal', brows='angry', mouth='frown', mouth_y=96, hairline=[(8, 66), (24, 54), (50, 46), (76, 54), (92, 66)], face_front=face(chin=104, jaw=3)),
  fB + [tri(SW, 'mid', 'b'), L(outline([(16, 66), (21, 66), (26, 92), (34, 100), (24, 100), (16, 88)]), 'mid', 'f'),
        L(outline([(84, 66), (79, 66), (74, 92), (66, 100), (76, 100), (84, 88)]), 'mid', 'f')],
  sB + [tri([(30, 10), (50, -6), (74, -12), (96, 0, 1), (76, 2), (66, 18)], 'mid', 'b'), L(outline([(54, 64), (60, 66), (64, 92), (74, 102), (62, 102), (54, 86)]), 'mid', 'f')],
  bB + [tri(SW, 'mid', 'b')])

# Finnard Grit: pelo morado oscuro alto y abultado con un gran mechón rosa que le cruza la frente
PK = _c('#e88ab8')
fN, sN, bN = D(top=-12, w=48, cy=40, n=6, amp=6, soft=True, seed=17, sb=62, nape=84, fr=48)
C('finnard-grit', 'normal', P('#3a2a5a', '#f8dcb0', iris='#4a5a7a'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, hairline=[(8, 62), (30, 52), (50, 50), (70, 52), (92, 62)]),
  fN + [fr([(30, 30), (54, 22), (72, 32), (70, 54), (60, 64, 1), (56, 48), (44, 52, 1), (40, 42)], PK)],
  sN + [fr([(60, 28), (84, 34), (90, 52), (80, 58, 1), (72, 44)], PK)], bN)

# Finnes Grapplefeld: grandullón de cara redonda, pelo castaño rojizo corto con un mechón tieso hacia arriba; gafas
# pequeñas redondas, cejas fruncidas y colorete
fK, sK, bK = D(top=12, w=44, cy=44, sb=58, nape=82, fr=52)
C('finnes-grapplefeld', 'corpulento', P('#6a2e22', '#f8dcd0', iris='#3a2a2a'),
  F(eyes='dot', brows='angry', mouth='frown', mouth_y=96, hairline=[(8, 58), (50, 54), (92, 58)], face_front=face(w=7, chin=104, jaw=4)),
  fK + [tri([(44, 14), (36, -10), (52, -20, 1), (48, -4), (56, 12)], 'mid')] + round_glasses('front', _c('#9aa0a8'), y=76, r=6, w=1.4) + blush(86, 26),
  sK + [tri([(40, 14), (28, -8), (44, -18, 1), (42, -2), (52, 10)], 'mid')] + round_glasses('side', _c('#9aa0a8'), y=76, r=6, w=1.4),
  bK + [tri([(44, 16), (38, -8), (54, -18, 1), (50, -2), (56, 14)], 'mid')])

# Fiona Leroux: pelo granate con flequillo y dos picos en lo alto como orejas de gato; ojos rosas y colorete
fL, sL, bL = D(top=2, w=44, cy=42, sb=92, nape=88, fr=56, n=5, amp=5, soft=True, seed=18)
C('fiona-leroux', 'chica', P('#8a4a4a', '#f8dcd0', iris='#e05a7a'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, hairline=hl(6, 70, 54, 60, seed=4)),
  fL + [tri([(14, 22), (14, -14, 1), (36, 10)], 'mid'), tri([(86, 22), (86, -14, 1), (64, 10)], 'mid')] + blush(86, 24),
  sL + [tri([(32, 10), (40, -18, 1), (56, 4)], 'mid')],
  bL + [tri([(14, 22), (14, -14, 1), (36, 10)], 'mid'), tri([(86, 22), (86, -14, 1), (64, 10)], 'mid')])

# Fitzbon Vivant: señor de pelo gris escaso, calvo por arriba, piel tostada clara, gafas negras rectangulares y ojos
# cerrados de sonrisa
GG = _c('#8a8a8e')
C('fitzbon-vivant', 'normal', P('#8a8a8e', '#f0c890', iris='#3a3a3a'),
  F(eyes='none', brows=True, mouth='smile', mouth_y=94, hairline=False),
  skull3('front') + [L(outline([(14, 70), (12, 40), (24, 18), (38, 12), (30, 30), (24, 66)]), GG), L(outline([(86, 70), (88, 40), (76, 18), (62, 12), (70, 30), (76, 66)]), GG)] +
  rect_specs('front', BLACK, y=76, w=2.6) + lid_line(76),
  skull3('side') + [L(outline([(8, 32), (30, 20), (44, 40), (40, 66), (14, 66)]), GG)] + rect_specs('side', BLACK, y=76, w=2.6) + side_lid(76),
  skull3('back') + [L(outline([(14, 74), (12, 40), (88, 40), (86, 74), (50, 82)]), GG)])

# Fizz Kablooey: melena de rizos verde oscuro hasta la nuca con raya al medio y ojos verdes
fX, sX, bX = D(top=0, w=48, cy=44, n=14, amp=5, soft=True, seed=19, long=96, flare=4, fr=50)
C('fizz-kablooey', 'normal', P('#2e3a2a', '#f8dccc', iris='#5a9a4a'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=93, hairline=[(8, 66), (30, 52), (48, 40), (50, 36), (52, 40), (70, 52), (92, 66)]),
  fX + [strand([(30, 20), (26, 40)], 'deep', 'b', 1.0), strand([(70, 20), (74, 40)], 'deep', 'b', 1.0)], sX, bX)

# Flash Lighton: piel oscura, melena morada esponjosa y abultada a los lados, ojos naranjas y sonrisa de dientes
fH, sH, bH = D(top=0, w=52, cy=44, n=10, amp=7, soft=True, seed=20, sb=86, nape=90, fr=50, flare=8)
C('flash-lighton', 'normal', P('#4a3a9a', '#8a5a40', iris='#e07a2a'),
  F(eyes='big', brows=False, mouth='grin', mouth_y=94, hairline=hl(5, 66, 52, 60, seed=5)),
  fH, sH, bH)

# Flaurine Woodwind: pelo azul con flequillo de lado y dos rollos grandes a los lados que acaban en bolas abajo
fO, sO, bO = bowl3('front', top=4, side=74, fringe=60, w=0), bowl3('side', top=4, nape=86, fringe=60), bowl3('back', top=4, nape=86)
C('flaurine-woodwind', 'chica', P('#2a6aa8', '#fae0d2', iris='#a03028'),
  F(eyes='big', brows=True, mouth='frown', mouth_y=92, hairline=[(8, 60), (40, 56), (70, 60), (92, 62)]),
  fO + [L(ell(4, 72, 12, 8)), L(ell(96, 72, 12, 8)), L(ell(6, 100, 13, 9)), L(ell(94, 100, 13, 9)), fr([(60, 56), (80, 44), (86, 64), (76, 62)])] + blush(86, 24),
  sO + [L(ell(30, 98, 12, 9))], bO + [L(ell(10, 96, 13, 9)), L(ell(90, 96, 13, 9))])

# Floyn Circuits: tupé alto morado en bloque plano, maquillaje morado alrededor de los ojos y sonrisa de dientes
PU = _c('#9a5ac8')
C('floyn-circuits', 'normal', P('#a86ac8', '#f6c8a0', iris='#5a5ab0', shade='#8a4aa8'),
  F(eyes='sharp', brows=False, mouth='grin', mouth_y=94, hairline=[(8, 58), (22, 46), (50, 42), (78, 46), (92, 58)]),
  [L(outline([(14, 60), (12, 20), (18, -16), (50, -22), (82, -16), (88, 20), (86, 60), (80, 46), (20, 46)])),
   L(outline([(60, -18), (82, -14), (88, 22), (84, 56), (76, 30)]), 'shade', 'b', False),
   L(quad((22, 76), (30, 62), (44, 68)), PU, 'f', False, False, 3.2), L(quad((78, 76), (70, 62), (56, 68)), PU, 'f', False, False, 3.2)],
  [L(outline([(56, 54), (58, 40), (82, 40), (88, -12), (60, -22), (24, -18), (8, 10), (8, 44), (30, 60), (48, 58)]))],
  [L(outline([(12, 76), (10, 20), (18, -16), (50, -22), (82, -16), (90, 20), (88, 76), (50, 82)]))])

# Flynn Duval (modelo 3D): pelo castaño oscuro alborotado con un mechón de antena enroscado arriba y mechones por la
# frente; piel morena y ojos redondos muy abiertos
fY, sY, bY = D(top=-2, w=48, cy=44, n=9, amp=9, sweep=0.2, seed=21, sb=88, nape=90, fr=52)
C('flynn-duval', 'normal', P('#3a2018', '#b07848', iris='#2a2020'),
  F(eyes='round', brows='angry', mouth='line', mouth_y=94, hairline=hl(5, 70, 52, 62, lean=-2, seed=6)),
  fY + [L(quad((54, 2), (72, -26), (60, -16)) + [(56, -6)], 'mid', 'b', False, False, 3.2)],
  sY + [L(quad((48, 0), (54, -26), (40, -18)), 'mid', 'b', False, False, 3.2)],
  bY + [L(quad((54, 4), (72, -24), (60, -14)), 'mid', 'b', False, False, 3.2)])

# Focas Quayle: pelo verde menta con un mechón largo que le tapa un ojo y una coletilla atrás; ojos morados serios
fQ, sQ, bQ = D(top=0, w=48, cy=44, n=6, amp=8, sweep=-0.4, seed=22, sb=84, nape=90, fr=52)
C('focas-quayle', 'normal', P('#9ae0c0', '#f2c49a', iris='#9a3ab0', shade='#6ab89a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=hl(5, 66, 52, 60, lean=3, seed=7)),
  fQ + [fr([(46, 40), (78, 36), (90, 58), (84, 84, 1), (74, 64), (62, 54)])],
  sQ + tie_tail('side', 14, 70, 'mid'), bQ + tie_tail('back', 50, 78, 'mid'))

# Foster Bracewell (portero): pelo azul marino corto con raya, gafas de montura fina y sonrisa amable
fS, sS, bS = D(top=4, w=46, cy=42, sb=62, nape=82, fr=50)
C('foster-bracewell', 'normal', P('#22264a', '#f6d0b0', iris='#5a6a7a'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=94, hairline=[(8, 60), (30, 52), (44, 46), (70, 54), (92, 60)], face_front=face(chin=104)),
  fS + round_glasses('front', _c('#3a3a3a'), y=76, r=7.5, w=1.4), sS + round_glasses('side', _c('#3a3a3a'), y=76, r=7.5, w=1.4), bS)

# Fouad Togenick: tupé rubio altísimo en bloque plano, con un remolino en la frente; cara ancha y cuadrada y gran sonrisa
fT = [L(outline([(10, 62), (6, 20), (-6, -12), (50, -22), (106, -12), (94, 20), (90, 62), (80, 48), (20, 48)])),
      L(outline([(60, -18), (104, -10), (92, 22), (88, 58), (76, 30)]), 'shade', 'b', False)]
C('fouad-togenick', 'corpulento', P('#e0d482', '#f6c49c', iris='#7a6a2a', shade='#c0b460'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=96, hairline=[(8, 60), (30, 50), (50, 48), (70, 50), (92, 60)], face_front=face(w=8, chin=104, jaw=6)),
  fT + [L(quad((40, 60), (50, 44), (58, 56)) + quad((58, 56), (52, 64), (46, 56))[1:], 'shade', 'f', False, False, 2.4),
        L([(26, 64), (40, 64)], 'shade', 'f', False, False, 2.6), L([(60, 64), (74, 64)], 'shade', 'f', False, False, 2.6)],
  [L(outline([(54, 56), (60, 44), (86, 42), (100, -14), (60, -22), (14, -14), (4, 12), (8, 46), (30, 60)]))],
  [L(outline([(10, 76), (6, 20), (-6, -12), (50, -22), (106, -12), (94, 20), (90, 76), (50, 82)]))])

# Francesca Fintootle: pelo morado con dos picos como cuernos arriba y melena ondulada hasta los hombros; cejas
# arqueadas de enfado, sombra lila y ojos verdes
fE, sE, bE = D(top=2, w=46, cy=44, n=6, amp=5, soft=True, seed=24, long=100, flare=4, fr=54)
C('francesca-fintootle', 'chica', P('#6a4aa0', '#f8d6c4', iris='#7ac03a', shade='#50388a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=[(8, 62), (30, 52), (50, 48), (70, 52), (92, 62)]),
  fE + [tri([(20, 20), (16, -16, 1), (36, 8)], 'mid'), tri([(80, 20), (84, -16, 1), (64, 8)], 'mid')],
  sE + [tri([(34, 8), (40, -18, 1), (56, 4)], 'mid')],
  bE + [tri([(20, 20), (16, -16, 1), (36, 8)], 'mid'), tri([(80, 20), (84, -16, 1), (64, 8)], 'mid')])

# Frey Granzburn: piel muy oscura y pelo blanco abundante que se abre hacia los lados como alas; mirada seria
C('frey-granzburn', 'normal', P('#f2eef0', '#5a3a30', iris='#a0b4c0', shade='#d0c8d0'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(8, 62), (30, 54), (50, 50), (70, 54), (92, 62)]),
  [L(outline([(16, 82), (-12, 90, 1), (0, 70), (-6, 58, 1), (6, 48), (8, 24), (28, 8), (50, 4), (72, 8), (92, 24), (94, 48), (106, 58, 1), (100, 70), (112, 90, 1), (84, 82), (80, 52), (20, 52)])),
   L(outline([(60, 8), (90, 24), (96, 50), (110, 88), (84, 80), (78, 40)]), 'shade', 'b', False)],
  [L(outline([(56, 56), (60, 42), (84, 40), (90, 22), (66, 4), (34, 4), (10, 20), (-8, 66, 1), (20, 58), (40, 60)]))],
  [L(outline([(16, 76), (-14, 70, 1), (6, 50), (8, 24), (28, 8), (50, 4), (72, 8), (92, 24), (94, 50), (114, 70, 1), (84, 76), (50, 82)])),
   L(outline([(60, 8), (90, 24), (94, 50), (110, 68), (82, 74), (78, 40)]), 'shade', 'b', False)])

# Fuyo Catcher: un gorro enorme blanco en forma de medusa que le tapa la cabeza hasta la nariz, con dos círculos
# naranjas como ojos; se le ve solo la boca
WG, WGD, OR = _c('#e8eaea'), _c('#b8c0c0'), _c('#f0a030')
C('fuyo-catcher', 'normal', P('#c8cccc', '#f4caa8'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, hairline=False),
  [L(outline([(-14, 88), (0, 70), (14, 30), (36, 6), (64, 6), (86, 30), (100, 70), (114, 88), (84, 84), (50, 86), (16, 84)]), WG, 'f'),
   L(outline([(-14, 88), (2, 62), (98, 62), (114, 88), (84, 84), (50, 86), (16, 84)]), WGD, 'f', False),
   L(ell(30, 46, 10, 8), WHITE, 'f'), L(ell(70, 46, 10, 8), WHITE, 'f'), L(ell(30, 46, 7, 6), OR, 'f', False), L(ell(70, 46, 7, 6), OR, 'f', False)],
  [L(outline([(-10, 90), (2, 64), (12, 26), (40, 4), (70, 10), (92, 36), (104, 72), (112, 88), (60, 86), (20, 90)]), WG, 'f'),
   L(outline([(-10, 90), (4, 64), (104, 64), (112, 88), (60, 86)]), WGD, 'f', False), L(ell(80, 44, 6, 7), OR, 'f')],
  [L(outline([(-14, 90), (0, 70), (14, 30), (36, 6), (64, 6), (86, 30), (100, 70), (114, 90), (50, 94)]), WG, 'f'),
   L(outline([(-14, 90), (2, 64), (98, 64), (114, 90), (50, 94)]), WGD, 'f', False)])

# Galina Chilvers: piel morena, pelo lila rizado y abultado con unas gafas de natación azules en lo alto; ojos azules
BLG = _c('#3a7ac8')
fA, sA, bA = D(top=-2, w=50, cy=44, n=12, amp=6, soft=True, seed=25, sb=84, nape=90, fr=52, flare=6)
C('galina-chilvers', 'chica', P('#b8b8ec', '#c8946a', iris='#2a5ab0', shade='#9898d0'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=hl(6, 66, 52, 60, seed=8)),
  fA + [band('front', BLG, 30, 6, w=46), L(ell(36, 34, 8, 6), WHITE, 'f'), L(ell(64, 34, 8, 6), WHITE, 'f'), L(ell(36, 34, 5, 4), BLG, 'f', False), L(ell(64, 34, 5, 4), BLG, 'f', False)],
  sA + [band('side', BLG, 22, 6), L(ell(80, 22, 6, 6), BLG, 'f')], bA + [band('back', BLG, 34, 6, w=48)])

# Gavin Mallory: pelo azul marino en casco redondo con flequillo en mechones; ojos grandes azules y sonrisa traviesa
C('gavin-mallory', 'normal', P('#2a2a5a', '#f6caa4', iris='#3a3ab0'),
  F(eyes='big', brows=False, mouth='grin', mouth_y=93, hairline=hl(6, 66, 54, 64, seed=9)),
  bowl3('front', top=-2, side=70, fringe=58, w=4), bowl3('side', top=-2, nape=88, fringe=58, w=4), bowl3('back', top=-2, nape=88, w=4))

# Gemma Coombs: melena larga morada oscura con raya al medio, gafas redondas grandes doradas y ojos de sueño
fC, sC, bC = D(top=2, w=46, cy=44, long=118, flare=6, fr=56, seed=26)
GD = _c('#d09a30')
C('gemma-coombs', 'chica', P('#3a2a5a', '#f8e2d6', iris='#3a3a6a'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=93, hairline=[(8, 64), (30, 50), (48, 40), (50, 36), (52, 40), (70, 50), (92, 64)]),
  fC + round_glasses('front', GD, y=76, r=10, w=2.6), sC + round_glasses('side', GD, y=76, r=10, w=2.6), bC)

# Gentino Sorella: piel oscura, pelo corto verde azulado con un rizo celeste que le baja por la frente; cejas celestes
CY = _c('#7ad8d8')
fI, sI, bI = D(top=4, w=46, cy=42, sb=60, nape=82, fr=48)
C('gentino-sorella', 'normal', P('#2a8a8a', '#8a5a38', iris='#6a5a7a'),
  F(eyes='normal', brows=False, mouth='line', mouth_y=94, hairline=[(8, 58), (30, 46), (50, 44), (70, 46), (92, 58)]),
  fI + [fr([(46, 22), (58, 30), (54, 46), (50, 66, 1), (46, 48), (50, 36)], CY),
        L(quad((26, 64), (34, 60), (42, 64)), CY, 'f', False, False, 2.4), L(quad((58, 64), (66, 60), (74, 64)), CY, 'f', False, False, 2.4)],
  sI + [fr([(70, 30), (84, 40), (82, 54), (76, 44)], CY)], bI)

# Geri Spears: pelo gris claro corto en pinchos revueltos con un mechón blanco; ojos grises y sonrisa
fP, sP, bP = D(top=-6, w=44, cy=42, n=9, amp=10, seed=27, sb=70, nape=84, fr=50)
C('geri-spears', 'chica', P('#b8b4ac', '#f8d6bc', iris='#5a7a8a', shade='#948e86'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=hl(5, 64, 50, 58, seed=10)),
  fP + [fr([(54, 6), (64, 4), (66, 36), (60, 54, 1), (56, 34)], WHITE)], sP, bP)

# Gilbert Kraft: piel oscura, pelo morado al rape, cejas gruesas y sonrisa de dientes
fJ, sJ, bJ = D(top=8, w=44, cy=42, sb=56, nape=80, fr=48)
C('gilbert-kraft', 'normal', P('#7a6a98', '#8a5634', iris='#3a3a8a'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=95, hairline=[(8, 56), (30, 46), (50, 44), (70, 46), (92, 56)], face_front=face(w=3, chin=104, jaw=3)),
  fJ, sJ, bJ)

# Gildred Gainstead: pelo rubio claro alborotado y esponjoso que le tapa la frente y los ojos a medias; ojos verdes
fV, sV, bV = D(top=0, w=52, cy=46, n=10, amp=8, soft=True, seed=28, sb=84, nape=90, fr=58, flare=8)
C('gildred-gainstead', 'normal', P('#ecd49a', '#f6caa4', iris='#2a8a7a', shade='#cab070'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=hl(6, 72, 60, 70, seed=11)),
  fV, sV, bV)

# Giovanni Buston: melena morada ondulada hasta la mandíbula, más clara en las puntas de los lados; ojos en espiral
LV = _c('#9a8ac8')
fU, sU, bU = D(top=0, w=50, cy=44, n=8, amp=5, soft=True, seed=29, long=98, flare=6, fr=56)
C('giovanni-buston', 'normal', P('#4a3a60', '#f8dccc', iris='#6a6a8a'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=93, hairline=hl(6, 66, 54, 62, seed=12)),
  fU + [L(blob([(2, 80), (14, 78), (16, 98), (4, 100)], 4), LV, 'b', False), L(blob([(98, 80), (86, 78), (84, 98), (96, 100)], 4), LV, 'b', False)],
  sU + [L(blob([(10, 80), (30, 82), (28, 98), (6, 98)], 4), LV, 'b', False)], bU)

# Gloria Somdenn: melena larga azul con una antena en lo alto, flequillo y dos mechones que se abren a los lados como
# alas; colorete, ceño fruncido y morros
fW2, sW2, bW2 = D(top=0, w=48, cy=44, long=124, flare=6, fr=56, seed=30)
C('gloria-somdenn', 'chica', P('#3a5aa8', '#f8d8c8', iris='#3a8ac8', shade='#2a4488'),
  F(eyes='big', brows='angry', mouth='frown', mouth_y=93, hairline=hl(5, 66, 54, 62, seed=13)),
  fW2 + [tri([(16, 52), (-14, 70, 1), (14, 70)], 'mid'), tri([(84, 52), (114, 70, 1), (86, 70)], 'mid'),
         L(quad((46, 4), (44, -16), (56, -14)), 'mid', 'b', False, False, 3.2)] + blush(86, 24),
  sW2 + [L(quad((42, 2), (40, -18), (52, -16)), 'mid', 'b', False, False, 3.2)],
  bW2 + [L(quad((46, 4), (44, -16), (56, -14)), 'mid', 'b', False, False, 3.2)])

# Glorian Flaunt: señor de pelo oliva oscuro peinado a un lado con tupé, gafas redondas pequeñas y bigote de puntas
# enroscadas
fF2, sF2, bF2 = D(top=2, w=44, cy=42, sb=64, nape=82, fr=48)
fF2 += [tri([(34, 14), (50, -4), (70, -6), (86, 6, 1), (70, 6), (64, 20)], 'mid', 'b')]
C('glorian-flaunt', 'delgado', P('#3a3a30', '#f6caa4', iris='#3a8a8a'),
  F(eyes='normal', brows='angry', mouth='smile', mouth_y=96, hairline=[(8, 60), (26, 50), (40, 44), (70, 50), (92, 60)], face_front=face(chin=106)),
  fF2 + round_glasses('front', BLACK, y=77, r=6.5, w=1.6) +
  [L(quad((50, 90), (36, 88), (32, 82)) + [(30, 78)], 'mid', 'f', False, False, 2.0), L(quad((50, 90), (64, 88), (68, 82)) + [(70, 78)], 'mid', 'f', False, False, 2.0)],
  sF2 + round_glasses('side', BLACK, y=77, r=6.5, w=1.6) + [L(quad((86, 90), (80, 88), (76, 82)), 'mid', 'f', False, False, 2.0)], bF2)

# Godfrey Shahmann: pelo castaño peinado todo hacia atrás en una coleta larga que le cae por un hombro; piel tostada y
# ojos redondos
fH2, sH2, bH2 = D(top=0, w=46, cy=42, sb=60, nape=80, fr=44)
C('godfrey-shahmann', 'normal', P('#7a6a40', '#d8a878', iris='#2a2a2a'),
  F(eyes='round', brows=True, mouth='line', mouth_y=94, hairline=[(8, 60), (30, 44), (48, 38), (50, 34), (52, 38), (70, 44), (92, 60)], nose=(50, 85, 2.4)),
  fH2 + [L(outline([(84, 70), (94, 76), (100, 104), (94, 124, 1), (88, 100), (84, 84)]))],
  sH2 + tie_tail('side', 14, 64, 'mid'), bH2 + tie_tail('back', 50, 74, 'mid'))

# Gon Vyrall: pelo rojo asomando bajo una gorra de béisbol blanca y amarilla con la visera ladeada; ojos verdes
CPW, CPY = _c('#f4f4f4'), _c('#f4d432')
C('gon-vyrall', 'bajito', P('#e0503a', '#f4a87a', iris='#2ac0a0'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, hairline=hl(5, 68, 54, 62, seed=14)),
  dome('front', top=10, w=48, cy=46, n=8, amp=6, seed=32, sb=76) +
  [cap('front', CPW, top=-4, rim=46, w=48, z='f', ln=True), L(outline([(50, -4), (80, 6), (96, 30), (98, 44), (50, 44)]), CPY, 'f', True, True),
   L(outline([(70, 40), (112, 40), (118, 50), (80, 52)]), CPY, 'f', True, True)],
  dome('side', top=10, w=46, cy=46, n=8, amp=6, seed=32, nape=86, fr=52) + [cap('side', CPW, top=-4, rim=44, w=46, z='f', ln=True)],
  dome('back', top=10, w=48, cy=46, n=8, amp=6, seed=32, nape=86) + [cap('back', CPY, top=-4, rim=44, w=48, z='f', ln=True)])

# Grace Starlet: melena larga negra azulada que se vuelve morada en las puntas, flequillo partido y pestañas marcadas
fG2, sG2, bG2 = D(top=0, w=48, cy=44, long=126, flare=6, fr=56, seed=33)
PR = _c('#8a5aa8')
C('grace-starlet', 'chica', P('#24223e', '#f8dccc', iris='#7a7aa0'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=93, hairline=[(8, 64), (30, 52), (46, 42), (50, 46), (54, 42), (70, 52), (92, 64)]),
  fG2 + [L(outline([(-2, 104), (2, 120), (10, 126, 1), (16, 108)]), PR, 'f', False)],
  sG2 + [L(outline([(-2, 110), (6, 128, 1), (20, 118), (14, 102)]), PR, 'f', False)],
  bG2 + [L(outline([(-2, 104), (98, 104), (102, 124), (50, 128), (-2, 124)]), PR, 'f', False)])

# Graye Earlnest: melena plateada en casco con un mechón morado oscuro en el centro que le baja hasta la nariz; ojos ámbar
fE2, sE2, bE2 = bowl3('front', top=0, side=88, fringe=62, w=2), bowl3('side', top=0, nape=94, fringe=62, w=2), bowl3('back', top=0, nape=94, w=2)
C('graye-earlnest', 'normal', P('#c8ccd8', '#f8dccc', iris='#d0a030', shade='#a8acbc'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=93, hairline=[(8, 62), (92, 62)]),
  fE2 + [fr([(44, 30), (56, 30), (54, 66), (50, 86, 1), (46, 66)], _c('#3a2a5a'))], sE2, bE2)

# Grayson Tiltwood: pelo verde azulado abombado y peinado a un lado, con un mechón largo junto a la cara; ojos celestes
fT2, sT2, bT2 = D(top=-2, w=48, cy=42, n=3, amp=8, sweep=0.5, seed=34, sb=86, nape=88, fr=50, soft=True)
C('grayson-tiltwood', 'normal', P('#4a8a9a', '#f8dccc', iris='#3ab0c8', shade='#346a78'),
  F(eyes='big', brows=True, mouth='frown', mouth_y=93, hairline=[(8, 62), (30, 54), (46, 52), (70, 48), (92, 62)]),
  fT2 + [fr([(20, 50), (28, 54), (26, 84, 1), (18, 70)])], sT2, bT2)

# Greef Lonbrusch: melena corta naranja hasta la mandíbula, ojos verdes de párpado caído, pecas y gesto triste
fR2, sR2, bR2 = D(top=0, w=48, cy=44, n=6, amp=5, soft=True, seed=35, long=96, flare=4, fr=54)
C('greef-lonbrusch', 'normal', P('#e88a4a', '#f8dccc', iris='#4a8a4a', shade='#c86a30'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=93, hairline=hl(5, 66, 54, 62, seed=15)),
  fR2 + freckles(84, 22), sR2, bR2)

# Griffin Fastwell: pelo gris oscuro peinado en una gran ola hacia un lado con un mechón que cae sobre la frente;
# gafas de montura fina y ojos verdes serios
fF3, sF3, bF3 = D(top=2, w=46, cy=42, sb=72, nape=84, fr=46)
fF3 += [tri([(66, 14), (52, -4), (30, -10), (6, 4, 1), (26, 6), (36, 20)], 'mid', 'b')]
sF3 += [tri([(60, 12), (44, -6), (20, -8), (0, 8, 1), (22, 8), (30, 22)], 'mid', 'b')]
C('griffin-fastwell', 'delgado', P('#5a5a60', '#f6dcd0', iris='#3a9a6a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=[(8, 62), (26, 52), (60, 48), (92, 62)], face_front=face(chin=106)),
  fF3 + [fr([(10, 30), (30, 26), (36, 50), (26, 70, 1), (20, 50)])] + rect_specs('front', _c('#9aa0a8'), y=78, w=1.4),
  sF3 + rect_specs('side', _c('#9aa0a8'), y=78, w=1.4), bF3)

# Gusmin Strelbard: piel tostada, pelo verde muy oscuro recogido en una coleta altísima con goma roja que acaba en una
# punta larga enroscada; ojos entornados con lágrimas
fM2, sM2, bM2 = D(top=2, w=46, cy=42, n=5, amp=5, soft=True, seed=37, sb=72, nape=82, fr=50)
RG = _c('#d02a2a')
C('gusmin-strelbard', 'normal', P('#262e22', '#c88a5a', iris='#3a3a3a'),
  F(eyes='closed', brows='angry', mouth='frown', mouth_y=95, hairline=hl(6, 66, 52, 60, seed=16)),
  fM2 + [L(outline([(44, 4), (40, -20), (50, -34), (60, -20), (56, 4)])), L(ell(50, -2, 6, 3), RG, 'b'),
         L(quad((44, -30), (10, -30), (4, 0)), 'mid', 'b', False, False, 5.0), L(quad((60, -10), (100, 10), (108, 40)), 'mid', 'b', False, False, 5.0)],
  sM2 + [L(outline([(36, 4), (30, -20), (40, -32), (50, -18), (48, 4)])), L(ell(42, -2, 6, 3), RG, 'b'), L(quad((34, -24), (0, -10), (-6, 30)), 'mid', 'b', False, False, 5.0)],
  bM2 + [L(outline([(44, 4), (40, -20), (50, -34), (60, -20), (56, 4)])), L(ell(50, -2, 6, 3), RG, 'b'), L(quad((50, -28), (80, 20), (60, 70)), 'mid', 'b', False, False, 5.0)])

# Hanah Keller: piel morena, pelo rojo anaranjado revuelto con una diadema azul marino y un mechón tieso arriba;
# ojos ámbar
NVB = _c('#283454')
fK2, sK2, bK2 = D(top=-2, w=48, cy=44, n=8, amp=8, seed=38, sb=82, nape=88, fr=52)
C('hanah-keller', 'chica', P('#d24a2a', '#b07848', iris='#c08a2a', shade='#a83420'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, hairline=hl(5, 68, 54, 62, seed=17)),
  fK2 + [band('front', NVB, 40, 6, w=46), tri([(50, 4), (54, -18, 1), (62, 4)], 'mid')],
  sK2 + [band('side', NVB, 32, 6)], bK2 + [band('back', NVB, 42, 6, w=48)])

# Hanz Boll (portero): piel tostada, pelo castaño anaranjado en cepillo con las sienes rapadas en pico; cejas muy
# gruesas y sonrisa de lado
fB2, sB2, bB2 = D(top=-6, w=40, cy=40, sb=54, nape=78, fr=46)
C('hanz-boll', 'normal', P('#b0602a', '#c08a5a', iris='#3a6a7a'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=94, hairline=[(10, 54), (26, 46), (50, 44), (74, 46), (90, 54)], face_front=face(chin=104, jaw=2)),
  fB2 + [L(blob([(24, 64), (30, 58), (44, 62), (42, 68), (26, 68)], 4), 'deep', 'f', False), L(blob([(76, 64), (70, 58), (56, 62), (58, 68), (74, 68)], 4), 'deep', 'f', False)],
  sB2 + [L(blob([(72, 62), (86, 60), (86, 66), (72, 66)], 4), 'deep', 'f', False)], bB2)

# Hapleigh Mistakian: pelo naranja en llamaradas hacia arriba y una máscara pintada naranja y roja alrededor de los ojos
ORM, RDM = _c('#e88a2a'), _c('#c83a2a')
fP2, sP2, bP2 = D(top=-14, w=44, cy=40, n=7, amp=16, seed=39, sb=66, nape=82, fr=48)
C('hapleigh-mistakian', 'normal', P('#e06a2a', '#f8dccc', iris='#6a6aa0', shade='#b84a1a'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=94, hairline=hl(5, 62, 48, 56, seed=18)),
  fP2 + [L([(18, 64), (34, 62), (46, 70)], RDM, 'f', False, False, 3.4), L([(82, 64), (66, 62), (54, 70)], RDM, 'f', False, False, 3.4),
         L(quad((22, 76), (30, 86), (44, 82)), ORM, 'f', False, False, 3.0), L(quad((78, 76), (70, 86), (56, 82)), ORM, 'f', False, False, 3.0)],
  sP2 + [L(blob([(68, 68), (88, 64), (90, 82), (72, 82)], 4), ORM, 'b', False)], bP2)

# Hardan Kempton: melena larga castaña oscura y despeinada con pelos sueltos arriba, gafas negras rectangulares y ojos
# cerrados
fN2, sN2, bN2 = D(top=2, w=50, cy=44, n=10, amp=8, seed=40, long=112, flare=10, fr=56, ends=5)
C('hardan-kempton', 'delgado', P('#4a3e3a', '#f8dccc', iris='#3a3a3a'),
  F(eyes='none', brows=True, mouth='frown', mouth_y=95, hairline=[(8, 64), (30, 50), (50, 46), (70, 50), (92, 64)], face_front=face(chin=106)),
  fN2 + rect_specs('front', BLACK, y=76, w=2.6) + lid_line(76) +
  [L(quad((30, 8), (6, -12), (-6, 0)), 'deep', 'b', False, False, 1.0), L(quad((70, 8), (94, -12), (106, 0)), 'deep', 'b', False, False, 1.0)],
  sN2 + rect_specs('side', BLACK, y=76, w=2.6) + side_lid(76), bN2)

# Harolde Narcissus: afro rubio enorme y esponjoso en bultos redondos; ojos dorados brillantes
fA2, sA2, bA2 = D(top=-14, w=52, cy=38, n=12, amp=6, soft=True, seed=41, sb=62, nape=84, fr=48)
C('harolde-narcissus', 'normal', P('#f0d880', '#f8e2d6', iris='#c09a2a', shade='#d0b860'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=hl(6, 62, 54, 60, seed=19)),
  fA2, sA2, bA2)

# Harrey Tagebard: abuelito de pelo corto gris azulado, frente con arrugas, ojos cerrados sonrientes y colorete
fT3, sT3, bT3 = D(top=6, w=46, cy=42, sb=62, nape=82, fr=48)
C('harrey-tagebard', 'bajito', P('#7a90b0', '#f8dccc', iris='#3a3a3a'),
  F(eyes='none', brows=True, mouth='smile', mouth_y=94, hairline=[(8, 58), (30, 44), (50, 42), (70, 44), (92, 58)]),
  fT3 + lid_line(76) + blush(86, 24) + [L([(34, 52), (66, 52)], 'skin_d', 'f', False, False, 1.2), L([(36, 57), (64, 57)], 'skin_d', 'f', False, False, 1.2)],
  sT3 + side_lid(76), bT3)

# Harris Gridley: pelo negro rizado muy abultado con un rizo que le cae por la frente; mirada intensa y nariz rojiza
fG3, sG3, bG3 = D(top=-6, w=54, cy=44, n=14, amp=7, soft=True, seed=42, sb=90, nape=92, fr=52, flare=8)
C('harris-gridley', 'normal', P('#2a2626', '#e8b894', iris='#4a8a8a'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=95, hairline=hl(6, 66, 52, 58, seed=20)),
  fG3 + [fr([(44, 40), (56, 40), (58, 52), (50, 60), (44, 54), (50, 50)]), L(blob([(44, 78), (56, 78), (54, 88), (46, 88)], 4), _c('#d07a70'), 'b', False)],
  sG3, bG3)

# Hazel Woodrow (portera): pelo verde oscuro con flequillo largo en mechones y melena hasta los hombros; mirada afilada
fW3, sW3, bW3 = D(top=0, w=46, cy=44, long=104, flare=4, fr=56, seed=43)
C('hazel-woodrow', 'chica', P('#384a32', '#f8e2d6', iris='#8ab040'),
  F(eyes='sharp', brows=True, mouth='frown', mouth_y=93, hairline=hl(4, 70, 54, 66, seed=21)),
  fW3, sW3, bW3)

# Hazlo Prophyle: piel oscura y un afro gris oscuro enorme que le tapa la frente hasta los ojos
fZ2, sZ2, bZ2 = D(top=-14, w=58, cy=40, n=14, amp=7, soft=True, seed=44, sb=80, nape=90, fr=60, flare=8)
C('hazlo-prophyle', 'normal', P('#4a5058', '#9a6a4a', iris='#4a5a8a'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=95, hairline=[(8, 70), (30, 68), (50, 66), (70, 68), (92, 70)]),
  fZ2, sZ2, bZ2)

# Healan Masson: pelo azul marino en pinchos revueltos hacia arriba, cejas fruncidas y morros
fH3, sH3, bH3 = D(top=-14, w=46, cy=40, n=10, amp=12, seed=45, sb=64, nape=84, fr=48)
C('healan-masson', 'normal', P('#34508a', '#f8dccc', iris='#4a6ab0'),
  F(eyes='normal', brows='angry', mouth='frown', mouth_y=94, hairline=hl(5, 62, 50, 58, seed=22)),
  fH3, sH3, bH3)

# Heathcliff Humbold: piel morena, melena negra larga y salvaje con dos picos como cuernos y un mechón blanco que le cae
# por un lado; ojos amarillos
fC2, sC2, bC2 = D(top=-2, w=52, cy=44, n=12, amp=10, seed=46, long=116, flare=10, fr=56, ends=5)
C('heathcliff-humbold', 'normal', P('#262426', '#8a5a3a', iris='#c0a030'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=hl(6, 70, 56, 66, seed=23)),
  fC2 + [tri([(16, 14), (-6, -12, 1), (26, 0)], 'mid'), tri([(84, 14), (106, -12, 1), (74, 0)], 'mid'),
         fr([(62, 30), (78, 28), (82, 70), (78, 104, 1), (70, 70)], WHITE), L(quad((18, 12), (2, -8), (-4, -10)), WHITE, 'f', False, False, 3.0)],
  sC2 + [tri([(40, 6), (24, -16, 1), (54, 0)], 'mid'), fr([(70, 30), (84, 36), (82, 74), (76, 92, 1), (72, 60)], WHITE)],
  bC2 + [tri([(16, 14), (-6, -12, 1), (26, 0)], 'mid'), tri([(84, 14), (106, -12, 1), (74, 0)], 'mid'), L(outline([(62, 30), (80, 30), (84, 110), (66, 104)]), WHITE, 'f', False)])

# Heather Lovella: pelo negro con flequillo recto y una coleta baja a un lado que cae por delante del hombro
fL2, sL2, bL2 = bowl3('front', top=2, side=82, fringe=60, w=0), bowl3('side', top=2, nape=88, fringe=60), bowl3('back', top=2, nape=88)
C('heather-lovella', 'chica', P('#24202e', '#f8e2d6', iris='#5a4a4a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(8, 60), (92, 60)]),
  fL2 + [L(outline([(4, 80), (12, 80), (18, 110), (10, 128, 1), (2, 108)]))],
  sL2 + tie_tail('side', 30, 82, 'mid'), bL2 + [L(outline([(2, 84), (14, 84), (16, 116), (6, 130, 1)]))])

# Hedrick Wilspin (portero): gorro de punto morado calado, piel tostada, cejas pintadas y arrugas de enfado
PBN = _c('#5a4ab0')
C('hedrick-wilspin', 'normal', P('#2a2a30', '#d09060', iris='#a03028'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=False, face_front=face(chin=104, jaw=2)),
  [cap('front', PBN, top=0, rim=54, w=47, z='f', ln=True)] + [L([(30 + i * 8, 10), (30 + i * 8, 50)], _c('#4a3a98'), 'f', False, False, 1.0) for i in range(6)] +
  [L([(40, 66), (46, 70)], 'skin_d', 'f', False, False, 1.2), L([(60, 66), (54, 70)], 'skin_d', 'f', False, False, 1.2)],
  [cap('side', PBN, top=0, rim=52, w=46, z='f', ln=True)],
  [cap('back', PBN, top=0, rim=52, w=47, z='f', ln=True)])

# Helen Deavor: melena azul marino ondulada hasta los hombros, que se abre por abajo, con dos horquillas blancas; ojos
# verdes y cejas marcadas
fD2, sD2, bD2 = D(top=0, w=48, cy=44, n=6, amp=5, soft=True, seed=47, long=100, flare=10, fr=54)
C('helen-deavor', 'chica', P('#24284a', '#f8dccc', iris='#4ab04a'),
  F(eyes='big', brows=True, mouth='line', mouth_y=93, hairline=[(8, 64), (30, 52), (48, 44), (50, 40), (52, 44), (70, 52), (92, 64)]),
  fD2 + [L([(26, 38), (42, 32)], WHITE, 'f', False, False, 2.0), L([(28, 43), (44, 37)], WHITE, 'f', False, False, 2.0)],
  sD2 + [L([(60, 36), (72, 30)], WHITE, 'f', False, False, 2.0)], bD2)
