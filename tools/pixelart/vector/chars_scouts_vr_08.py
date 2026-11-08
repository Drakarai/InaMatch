"""Ojeadores de Victory Road (scouts-vr), tanda 08: dibujados a partir de su retrato (con el modelo 3D para perfil y
espalda cuando es del mismo personaje); claves 'scouts-vr:<id>'. El sexo, de la ficha de la wiki."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401
from chars_scouts_ie1_09 import dome, hl, face, face_side, mark, _c  # noqa: F401
from chars_scouts_ie1_03 import bowl, round_specs, shades, blush, thick_brows, side_brow  # noqa: F401
from chars_scouts_ie3_02 import bowl3, side_lock  # noqa: F401

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


def fr(pts, c='mid'):
    return L(outline(pts), c, 'f')


def bun(cx, cy, r, c='mid', z='b'):
    """Moño o coleta enroscada redonda."""
    return L(blob([(cx + r * a, cy + r * b) for a, b in ((0, -1), (0.8, -0.6), (1, 0.1), (0.7, 0.8), (0, 1), (-0.7, 0.8), (-1, 0.1), (-0.8, -0.6))], 4), c, z)


def tail(x0, y0, x1, y1, w=10, c='mid', z='b', bend=0):
    """Coleta larga que cae de (x0,y0) a la punta (x1,y1)."""
    mx, my = (x0 + x1) / 2 + bend, (y0 + y1) / 2
    return L(outline([(x0 - w / 2, y0), (x0 + w / 2, y0), (mx + w / 2, my), (x1 + w / 4, y1 - 8), (x1, y1, 1), (x1 - w / 3, y1 - 8), (mx - w / 2, my)]), c, z)


def earring(x, y, c=WHITE, r=1.8):
    return L(ell(x, y, r, r), c, 'f', False)


def eyes_arc(ey=75, sep=14, w=6):
    """Ojos cerrados de felicidad (arco hacia arriba)."""
    return [L(quad((50 - sep - w, ey + 2), (50 - sep, ey - 4), (50 - sep + w, ey + 2)), OUTC, 'f', False, False, 2.2),
            L(quad((50 + sep - w, ey + 2), (50 + sep, ey - 4), (50 + sep + w, ey + 2)), OUTC, 'f', False, False, 2.2)]


# ------------------------------------------------------------------ jugadores

# Rhianna Wardholdt: pelo negro con flequillo abierto en el centro y mechones finos en la frente; dos coletas bajas
# enroscadas en bola junto al cuello; ojos grandes oscuros y sonrisa
C('rhianna-wardholdt', 'chica', P('#1e2226', '#fce6d4', iris='#2a2a34', shade='#121518'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, hairline=[(6, 70), (18, 52), (30, 48), (44, 56), (50, 50), (56, 56), (70, 48), (82, 52), (94, 70)]),
  [bun(12, 96, 11), bun(88, 96, 11)] + dome('front', top=2, w=46, cy=46, sb=82) +
  [fr([(36, 42), (46, 46), (48, 66, 1), (42, 52)]), fr([(64, 42), (54, 46), (52, 66, 1), (58, 52)])],
  [bun(36, 98, 11)] + dome('side', top=2, w=46, cy=46, nape=88, fr=52),
  [bun(16, 96, 11), bun(84, 96, 11)] + dome('back', top=2, w=46, cy=46, nape=90))

# Ricemond Chowen: grandullón de cara redondísima; pelo castaño rojizo peinado hacia atrás con la frente despejada, que le cae
# por detrás de las orejas hasta los hombros; cejas enormes en arco, ojos cerrados, coloretes y morritos
RED = _c('#e08a7a')
C('ricemond-chowen', 'corpulento', P('#a8665a', '#fccdab', shade='#7a4038'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=98, nose=(50, 88, 3), ear_out=6,
    face_front=face(w=8, chin=112, jaw=8, top=30), face_side=face_side(chin=8, jaw=6), hairline=False),
  [L(outline([(2, 112), (0, 60), (8, 30), (24, 14), (50, 8), (76, 14), (92, 30), (100, 60), (98, 112), (88, 108), (86, 58), (14, 58), (12, 108)])),
   L(blob([(14, 56), (20, 34), (36, 22), (50, 20), (64, 22), (80, 34), (86, 56), (70, 50), (50, 48), (30, 50)], 6), 'skin', 'b', False),
   L(quad((20, 72), (32, 58), (44, 70)), OUTC, 'f', False, False, 3.0), L(quad((56, 70), (68, 58), (80, 72)), OUTC, 'f', False, False, 3.0),
   L(quad((26, 80), (32, 76), (40, 80)), OUTC, 'f', False, False, 1.8), L(quad((60, 80), (68, 76), (74, 80)), OUTC, 'f', False, False, 1.8),
   L(ell(22, 90, 6, 4), RED, 'f', False), L(ell(78, 90, 6, 4), RED, 'f', False)],
  [L(outline([(60, 30), (40, 14), (20, 18), (6, 40), (2, 80), (4, 112), (24, 112), (30, 80), (40, 60), (54, 52), (64, 40)])),
   L(quad((72, 72), (80, 62), (88, 70)), OUTC, 'f', False, False, 3.0), L(quad((76, 80), (80, 77), (86, 79)), OUTC, 'f', False, False, 1.8),
   L(ell(80, 90, 5, 4), RED, 'f', False)],
  dome('back', top=8, w=48, cy=50, long=112, flare=2, ends=3))

# Richter Poole: melena lisa morada hasta los hombros con flequillo recto; ojos afilados naranjas y sonrisa de dientes
C('richter-poole', 'delgado', P('#8a6ea8', '#f9e4d7', iris='#d8602a', shade='#644a80'),
  F(eyes='sharp', brows=False, mouth='grin', mouth_y=96, face_front=face(chin=106), face_side=face_side(chin=5),
    hairline=[(6, 70), (14, 58), (86, 58), (94, 70)]),
  dome('front', top=0, w=47, cy=46, long=102, flare=4, ends=4) + [fr([(16, 40), (30, 28), (50, 26), (70, 28), (84, 40), (86, 62), (14, 62)])] +
  [L(outline([(18, 62), (12, 104, 1), (24, 80), (24, 62)]), 'mid', 'f'), L(outline([(82, 62), (88, 104, 1), (76, 80), (76, 62)]), 'mid', 'f')],
  dome('side', top=0, w=47, cy=46, long=102, flare=4, fr=62),
  dome('back', top=0, w=47, cy=46, long=102, flare=4, ends=4))

# Rico Falsettis: pelo castaño grisáceo en casco corto con flequillo; ojos azul grisáceo y boca pequeña
C('rico-falsettis', 'bajito', P('#8a7470', '#fbe2cf', iris='#5a6a88', shade='#6a5654'),
  F(eyes='normal', brows=False, mouth='line', mouth_y=92, hairline=[(8, 64), (16, 56), (30, 58), (44, 54), (60, 58), (74, 54), (84, 56), (92, 64)]),
  bowl3('front', top=2, side=74, nape=88, fringe=60),
  bowl3('side', top=2, side=74, nape=88, fringe=58),
  bowl3('back', top=2, side=74, nape=88, fringe=60))

# Rina Eastvale: dos coletas largas naranjas que caen hasta la cintura, flequillo con mechones; ojos azules, sonrisa y
# pendientes de perla (modelo 3D para la espalda)
C('rina-eastvale', 'chica', P('#e3874a', '#fbdaba', iris='#3a5aa8', shade='#b35838'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, hairline=[(6, 70), (16, 52), (30, 58), (40, 48), (50, 60), (60, 48), (70, 58), (84, 52), (94, 70)]),
  [tail(10, 50, 4, 128, 14), tail(90, 50, 96, 128, 14)] + dome('front', top=0, w=46, cy=46, sb=80) +
  [L(ell(11, 48, 4, 4), _c('#f0e0a0'), 'f'), L(ell(89, 48, 4, 4), _c('#f0e0a0'), 'f'), earring(13, 82), earring(87, 82)],
  [tail(40, 40, 24, 128, 14, bend=-6)] + dome('side', top=0, w=46, cy=46, nape=86, fr=56) + [L(ell(40, 40, 4, 4), _c('#f0e0a0'), 'f')],
  [tail(16, 48, 10, 128, 14), tail(84, 48, 90, 128, 14)] + dome('back', top=0, w=46, cy=46, nape=88))

# Ripley Swaydon: pelo crema abombado en ondas como una nube, con un mechón claro que cae por el centro de la cara; piel
# morena, ojos verdes y boca recta
C('ripley-swaydon', 'normal', P('#e7dcc1', '#bf8f7d', iris='#4ab04a', shade='#c0a888', light='#f6f0e2'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=93, hairline=[(6, 70), (18, 54), (34, 48), (50, 52), (66, 48), (82, 54), (94, 70)]),
  dome('front', top=-6, w=54, cy=48, n=9, amp=6, soft=True, sb=86, seed=8) +
  [fr([(46, 40), (54, 40), (56, 66), (52, 86, 1), (48, 66)], 'light')],
  dome('side', top=-6, w=54, cy=48, n=9, amp=6, soft=True, nape=90, fr=56, seed=8),
  dome('back', top=-6, w=54, cy=48, n=9, amp=6, soft=True, nape=92, seed=8))

# Rockin Sunshaide: pelo rubio oscuro revuelto en mechones de punta, piel tostada; gafas de natación verdes de cristal oscuro y
# una sonrisa enorme de dientes; cejas gruesas
C('rockin-sunshaide', 'normal', P('#c0aa76', '#dcae8c', shade='#967555'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=96, hairline=hl(6, 64, 50, 58, jit=2, seed=5)),
  dome('front', top=-2, w=48, cy=44, n=8, amp=8, sweep=0.3, seed=5, sb=64) +
  [L(blob([(24, 74), (46, 74), (45, 84), (26, 84)], 4), _c('#2a2c2c'), 'f', True), L(blob([(76, 74), (54, 74), (55, 84), (74, 84)], 4), _c('#2a2c2c'), 'f', True),
   L([(22, 76), (24, 76)], _c('#3ac850'), 'f', False, False, 2), L([(46, 78), (54, 78)], _c('#3ac850'), 'f', False, False, 2.4),
   L(quad((24, 64), (34, 58), (44, 64)), 'shade', 'f', False, False, 3.2), L(quad((56, 64), (66, 58), (76, 64)), 'shade', 'f', False, False, 3.2)],
  dome('side', top=-2, w=48, cy=44, n=8, amp=8, sweep=0.3, seed=5, nape=84, fr=50) +
  [L(blob([(74, 74), (88, 74), (88, 84), (75, 84)], 4), _c('#2a2c2c'), 'f', True), L([(74, 78), (48, 76)], _c('#3ac850'), 'f', False, False, 2)],
  dome('back', top=-2, w=48, cy=44, n=8, amp=8, sweep=0.3, seed=5, nape=86) + [L([(8, 78), (92, 78)], _c('#3ac850'), 'f', False, False, 2.4)])

# Rockson Grohl: pelo negro morado revuelto en pinchos largos que se abren hacia fuera y mechones sobre la frente; ojos
# grises entornados y boca torcida
C('rockson-grohl', 'normal', P('#382e43', '#f8d2b8', iris='#6a6070', shade='#261f2c'),
  F(eyes='sharp', brows=True, mouth='frown', mouth_y=94, hairline=hl(6, 70, 50, 62, lean=-3, jit=3, seed=9)),
  dome('front', top=-10, w=52, cy=46, n=10, amp=14, sweep=-0.2, seed=9, sb=90),
  dome('side', top=-10, w=52, cy=46, n=10, amp=14, sweep=-0.2, seed=9, nape=94, fr=56),
  dome('back', top=-10, w=52, cy=46, n=10, amp=14, sweep=-0.2, seed=9, nape=96))

# Roderick Sawsbury (portero): pelo lila muy claro, desgreñado y en capas, con mechones sobre la frente y las puntas grises
# a los lados; ojos azules y sonrisa
GRY = _c('#5a5458')
C('roderick-sawsbury', 'normal', P('#e4d6e7', '#f8c5a6', iris='#4a5aa0', shade='#bca8c0'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=92, hairline=hl(7, 68, 50, 66, lean=-2, jit=3, seed=12)),
  [L(outline([(4, 80), (-2, 92, 1), (12, 86)]), GRY), L(outline([(96, 80), (102, 92, 1), (88, 86)]), GRY)] +
  dome('front', top=0, w=48, cy=46, n=9, amp=6, sweep=-0.2, seed=12, sb=86),
  dome('side', top=0, w=48, cy=46, n=9, amp=6, sweep=-0.2, seed=12, nape=88, fr=62) + [L(outline([(28, 88), (22, 98, 1), (40, 90)]), GRY)],
  dome('back', top=0, w=48, cy=46, n=9, amp=6, sweep=-0.2, seed=12, nape=90) + [L(outline([(10, 84), (6, 96, 1), (24, 88)]), GRY), L(outline([(90, 84), (94, 96, 1), (76, 88)]), GRY)])

# Romain Romanze: melena rosa larga y ondulada, peinada hacia un lado, que le cae por un hombro; ojos tristes grises con
# pestañas, cejas caídas y boca pequeña
C('romain-romanze', 'delgado', P('#f6c8c8', '#fee8de', iris='#6a6070', shade='#c58c8c', light='#fde2e2'),
  F(eyes='normal', brows=False, mouth='frown', mouth_y=94, face_front=face(chin=104), hairline=[(6, 70), (14, 56), (30, 44), (52, 40), (70, 50), (84, 56), (94, 70)]),
  dome('front', top=-2, w=48, cy=46, n=6, amp=5, soft=True, seed=14, long=114, flare=8, ends=3) +
  [fr([(14, 50), (30, 30), (56, 26), (72, 34), (60, 40), (42, 46), (30, 56), (22, 74), (14, 64)]),
   L(outline([(82, 60), (96, 92), (90, 120, 1), (84, 96), (76, 70)]), 'mid', 'f'),
   L([(26, 66), (42, 62)], OUTC, 'f', False, False, 2.0), L([(74, 66), (58, 62)], OUTC, 'f', False, False, 2.0)],
  dome('side', top=-2, w=48, cy=46, n=6, amp=5, soft=True, seed=14, long=114, flare=8, fr=54) + [L([(72, 66), (84, 62)], OUTC, 'f', False, False, 2.0)],
  dome('back', top=-2, w=48, cy=46, n=6, amp=5, soft=True, seed=14, long=114, flare=8, ends=3))

# Romica Glimmerly: melena larga rosa muy clara con flequillo recto y tirabuzones gruesos a los lados; ojos grandes rojizos
# con pestañas y sonrisa
def _ringlets(xs, y0=80, y1=126):
    out = []
    for x in xs:
        for i, y in enumerate(range(y0, y1, 12)):
            out.append(L(ell(x + (2 if i % 2 else -2), y, 7, 7), 'mid', 'b'))
    return out
C('romica-glimmerly', 'chica', P('#ebd5dd', '#fee2d1', iris='#b04a5a', shade='#c8a8b2', light='#f8eef2'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, hairline=[(6, 70), (12, 60), (88, 60), (94, 70)]),
  _ringlets([6, 94]) + dome('front', top=-2, w=48, cy=46, long=96, flare=4, ends=4) +
  [fr([(14, 42), (30, 26), (50, 24), (70, 26), (86, 42), (88, 64), (12, 64)]), L([(18, 64), (82, 64)], 'shade', 'f', False, False, 1.0)],
  _ringlets([26]) + dome('side', top=-2, w=48, cy=46, long=96, flare=4, fr=64),
  _ringlets([12, 50, 88]) + dome('back', top=-2, w=48, cy=46, long=96, flare=4, ends=4))

# Rondo Harmond (portero): pelo verde oliva en seta corta y redonda; cejas claras gruesas, ojos entornados de pillo,
# coloretes y sonrisa
C('rondo-harmond', 'normal', P('#c8b868', '#fad1b1', iris='#3a3020', shade='#9a8848', light='#e0d490'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, ear_out=2, face_front=face(w=4, chin=104, jaw=3), hairline=False),
  [L(blob([(2, 56), (6, 30), (24, 12), (50, 6), (76, 12), (94, 30), (98, 56), (80, 60), (50, 58), (20, 60)], 6)),
   L(blob([(56, 10), (80, 16), (96, 40), (96, 56), (80, 54), (70, 30)], 6), 'shade', 'b', False),
   L(quad((22, 68), (32, 62), (44, 68)), 'light', 'f', False, False, 3.6), L(quad((56, 68), (68, 62), (78, 68)), 'light', 'f', False, False, 3.6),
   L([(26, 78), (42, 78)], OUTC, 'f', False, False, 2.6), L([(58, 78), (74, 78)], OUTC, 'f', False, False, 2.6),
   L(quad((30, 78), (34, 82), (38, 78)), OUTC, 'f', False, False, 1.6), L(quad((62, 78), (66, 82), (70, 78)), OUTC, 'f', False, False, 1.6),
   L(ell(22, 88, 5, 3), RED, 'f', False), L(ell(78, 88, 5, 3), RED, 'f', False)],
  [L(blob([(92, 54), (90, 30), (70, 10), (44, 4), (20, 12), (4, 34), (2, 64), (14, 76), (30, 68), (50, 60), (70, 58)], 6)),
   L(quad((70, 68), (78, 62), (88, 66)), 'light', 'f', False, False, 3.6), L([(76, 78), (86, 78)], OUTC, 'f', False, False, 2.6)],
  [L(blob([(2, 64), (6, 30), (24, 12), (50, 6), (76, 12), (94, 30), (98, 64), (80, 76), (50, 80), (20, 76)], 6)),
   L(blob([(56, 10), (80, 16), (96, 40), (96, 64), (80, 72), (70, 30)], 6), 'shade', 'b', False)])

# Roxy Roarke: pelo azul con dos mechones enroscados hacia arriba como cuernos y rizos que se curvan hacia fuera por los
# lados, con mechas celestes; pintura azul alrededor de los ojos, coloretes y boca enfurruñada
SKY, PAINT = _c('#c8e0f2'), _c('#3a78c0')
def _roxy(view):
    if view == 'front':
        return [L(outline([(16, 30), (2, 14), (-4, 22, 1), (4, 24), (16, 40)])), L(outline([(84, 30), (98, 14), (104, 22, 1), (96, 24), (84, 40)])),
                L(outline([(8, 76), (-4, 70), (-6, 80, 1), (2, 84), (8, 90)])), L(outline([(92, 76), (104, 70), (106, 80, 1), (98, 84), (92, 90)]))]
    if view == 'side':
        return [L(outline([(40, 8), (30, -8), (22, -6, 1), (30, 0), (34, 14)])), L(outline([(26, 82), (14, 80), (10, 90, 1), (20, 90), (26, 96)]))]
    return [L(outline([(16, 30), (2, 14), (-4, 22, 1), (4, 24), (16, 40)])), L(outline([(84, 30), (98, 14), (104, 22, 1), (96, 24), (84, 40)])),
            L(outline([(8, 80), (-4, 74), (-6, 84, 1), (2, 88), (8, 94)])), L(outline([(92, 80), (104, 74), (106, 84, 1), (98, 88), (92, 94)]))]
C('roxy-roarke', 'chica', P('#4e81b4', '#f8c7a4', iris='#2a3a6a', shade='#3a6290'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=93, hairline=[(6, 70), (16, 52), (30, 58), (42, 50), (50, 58), (58, 50), (70, 58), (84, 52), (94, 70)]),
  _roxy('front') + dome('front', top=4, w=46, cy=46, sb=92) +
  [strand([(30, 20), (24, 50)], SKY, 'b', 2.0), strand([(70, 20), (76, 50)], SKY, 'b', 2.0),
   L(ell(36, 75, 8, 8) + [ell(36, 75, 8, 8)[0]], PAINT, 'f', False, False, 3.0), L(ell(64, 75, 8, 8) + [ell(64, 75, 8, 8)[0]], PAINT, 'f', False, False, 3.0),
   L(ell(22, 88, 5, 4), RED, 'f', False), L(ell(78, 88, 5, 4), RED, 'f', False)],
  _roxy('side') + dome('side', top=4, w=46, cy=46, nape=92, fr=56) + [L(ell(80, 88, 5, 4), RED, 'f', False)],
  _roxy('back') + dome('back', top=4, w=46, cy=46, nape=94) + [strand([(40, 20), (34, 70)], SKY, 'b', 2.0)])

# Ruckus Dinglestar: grandullón moreno de cara redonda; tupé castaño oscuro enorme con un mechón naranja que le baja por la
# sien; cejas gruesas enfadadas, ojos pequeños y boca torcida
ORA = _c('#e8a838')
C('ruckus-dinglestar', 'corpulento', P('#3b322f', '#d79276', iris='#2a1e18', shade='#2a2522'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=98, ear_out=5, face_front=face(w=6, chin=108, jaw=6, top=30), face_side=face_side(chin=6, jaw=5),
    hairline=[(8, 66), (14, 50), (40, 42), (70, 42), (88, 50), (92, 66)]),
  [L(outline([(10, 66), (8, 36), (20, 16), (40, 6), (54, -12, 1), (60, -4), (78, -6), (74, 6), (90, 24), (92, 48), (90, 66), (80, 50), (20, 50)])),
   L(outline([(12, 44), (24, 40), (22, 60), (14, 74), (10, 60)]), ORA, 'f'), *thick_brows(64, BLACK, 5.0, 15, 2.0, 14)],
  [L(outline([(84, 50), (88, 32), (80, 10), (62, -10, 1), (50, 0), (30, 2), (10, 16), (2, 42), (6, 70), (24, 78), (40, 66), (52, 58), (70, 54)])),
   L(outline([(70, 40), (80, 42), (78, 62), (72, 60)]), ORA, 'f'), side_brow(64, BLACK, 5.0, 2.0)],
  [L(outline([(10, 72), (8, 36), (20, 16), (40, 6), (54, -12, 1), (60, -4), (78, -6), (74, 6), (90, 24), (92, 48), (90, 72), (50, 80)]))])

# Rudgar Dennings: grandullón de cara ancha con un afro enorme azul marino; cejas pobladas enfadadas, ojos pequeños y boca
# apretada
C('rudgar-dennings', 'corpulento', P('#2c2a4e', '#cd9987', iris='#1e1a20', shade='#1e1c34'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=98, ear_out=6, face_front=face(w=8, chin=108, jaw=8, top=34), face_side=face_side(chin=6, jaw=6),
    hairline=[(6, 66), (16, 52), (34, 46), (50, 50), (66, 46), (84, 52), (94, 66)], nose=(50, 88, 4)),
  dome('front', top=-12, w=62, cy=48, n=14, amp=6, soft=True, seed=16, sb=84, flare=4),
  dome('side', top=-12, w=58, cy=48, n=14, amp=6, soft=True, seed=16, nape=90, fr=54),
  dome('back', top=-12, w=62, cy=48, n=14, amp=6, soft=True, seed=16, nape=92))

# Russ Radcliff: pelo naranja de pinchos revueltos en todas direcciones con mechones sobre los ojos; piel morena, ojos oscuros
# y boca seria
C('russ-radcliff', 'normal', P('#fca36b', '#c58c77', iris='#2a1e18', shade='#ca6f4c'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=94, hairline=hl(7, 70, 50, 66, jit=3, seed=18)),
  dome('front', top=-12, w=52, cy=44, n=13, amp=14, seed=18, sb=78),
  dome('side', top=-12, w=52, cy=44, n=13, amp=14, seed=18, nape=88, fr=60),
  dome('back', top=-12, w=52, cy=44, n=13, amp=14, seed=18, nape=90))

# Ruy Roosalot: pelo azul oscuro recogido en un moño alto, con un mechón largo que le tapa el ojo derecho y le cae hasta el
# pecho; ojo afilado y media sonrisa
C('ruy-roosalot', 'delgado', P('#2e4a90', '#fbe4d6', iris='#2a2830', shade='#223670', light='#4a6ab0'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=93, face_front=face(chin=104), hairline=[(6, 66), (16, 50), (40, 40), (64, 44), (84, 52), (94, 66)]),
  [bun(50, -2, 12)] + dome('front', top=2, w=45, cy=46, sb=70) +
  [fr([(18, 42), (36, 30), (50, 34), (48, 60), (40, 88), (34, 120, 1), (28, 90), (22, 66), (16, 56)]),
   strand([(36, 40), (36, 70), (32, 100)], 'light', 'f', 1.2)],
  [bun(40, -2, 12)] + dome('side', top=2, w=45, cy=46, nape=80, fr=52),
  [bun(50, -2, 12)] + dome('back', top=2, w=45, cy=46, nape=82))

# Ryden Waverley: pelo gris pizarra peinado hacia atrás que cae ondulado hasta el cuello; piel muy morena, ojos afilados
# claros y sonrisa de dientes
C('ryden-waverley', 'normal', P('#5a7484', '#8a5a40', iris='#c8b880', shade='#44606e'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=96, face_front=face(chin=104, jaw=2), hairline=[(6, 66), (16, 48), (32, 40), (50, 38), (68, 40), (84, 48), (94, 66)]),
  dome('front', top=-2, w=48, cy=46, n=5, amp=5, soft=True, seed=21, long=104, flare=6, ends=3) + [strand([(50, 10), (50, 30)], 'shade', 'b', 1.2)],
  dome('side', top=-2, w=48, cy=46, n=5, amp=5, soft=True, seed=21, long=104, flare=6, fr=44),
  dome('back', top=-2, w=48, cy=46, n=5, amp=5, soft=True, seed=21, long=104, flare=6, ends=3))

# Ryker Strive: pelo azul marino corto y revuelto con dos mechones de punta arriba como cuernos; orejas grandes, ojos grandes
# azules y sonrisa
C('ryker-strive', 'bajito', P('#3a3a62', '#fbd8bc', iris='#4a78b0', shade='#2a2a4a'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, big_ears=2, ear_out=2, hairline=hl(6, 62, 48, 56, jit=2, seed=23)),
  dome('front', top=-2, w=46, cy=42, n=7, amp=8, seed=23, sb=60) + [L(outline([(20, 18), (12, -4, 1), (30, 10)])), L(outline([(80, 18), (88, -4, 1), (70, 10)]))],
  dome('side', top=-2, w=46, cy=42, n=7, amp=8, seed=23, nape=78, fr=50) + [L(outline([(50, 4), (46, -12, 1), (62, 4)]))],
  dome('back', top=-2, w=46, cy=42, n=7, amp=8, seed=23, nape=80) + [L(outline([(20, 18), (12, -4, 1), (30, 10)])), L(outline([(80, 18), (88, -4, 1), (70, 10)]))])

# Rylan Spiker: pelo rojo de pinchos grandes echados hacia atrás y a los lados; ojos afilados verde agua con raya roja
# alrededor y sonrisa ladeada
CRIM = _c('#c8202a')
C('rylan-spiker', 'normal', P('#d8283a', '#fbd2b4', iris='#2ab0a0', shade='#a01828'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=hl(6, 64, 48, 58, lean=2, jit=2, seed=25)),
  dome('front', top=-14, w=50, cy=42, n=8, amp=16, sweep=0.5, seed=25, sb=66) +
  [L([(22, 70), (28, 76), (24, 82)], CRIM, 'f', False, False, 1.6), L([(78, 70), (72, 76), (76, 82)], CRIM, 'f', False, False, 1.6)],
  dome('side', top=-14, w=50, cy=42, n=8, amp=16, sweep=0.5, seed=25, nape=84, fr=50),
  dome('back', top=-14, w=50, cy=42, n=8, amp=16, sweep=0.5, seed=25, nape=86))

# Rynor Rushenfort: grandullón moreno con una melena melocotón enorme y abultada que le rodea la cara como una crin y forma
# dos cejas enormes sobre los ojos; ojos pequeños azules y morros enfadados
PEA = _c('#f6cfa2')
C('rynor-rushenfort', 'corpulento', P('#f6cfa2', '#b07a58', iris='#4a8ab0', shade='#d8aa80'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=98, ear_out=6, face_front=face(w=6, chin=106, jaw=6, top=40), hairline=False),
  dome('front', top=-8, w=56, cy=50, n=7, amp=8, soft=True, seed=27, long=106, flare=6, ends=3) +
  [L(blob([(14, 60), (26, 52), (46, 60), (44, 68), (26, 64), (16, 70)], 6), 'mid', 'f'), L(blob([(86, 60), (74, 52), (54, 60), (56, 68), (74, 64), (84, 70)], 6), 'mid', 'f')],
  dome('side', top=-8, w=54, cy=50, n=7, amp=8, soft=True, seed=27, long=106, flare=6, fr=60) + [L(blob([(66, 60), (84, 54), (90, 62), (80, 68)], 6), 'mid', 'f')],
  dome('back', top=-8, w=56, cy=50, n=7, amp=8, soft=True, seed=27, long=106, flare=6, ends=3))

# Sabine Jellis: pelo granate oscuro corto con un tupé redondo hacia un lado; ojos grandes magenta y boca abierta sonriente
C('sabine-jellis', 'chica', P('#4a1418', '#fbe2d4', iris='#b02a6a', shade='#300c10', light='#6a2428'),
  F(eyes='big', brows=True, mouth='grin', mouth_y=92, hairline=[(6, 64), (14, 52), (24, 42), (40, 50), (62, 46), (80, 52), (94, 64)]),
  bowl('front', top=-4, side=78, nape=84) + [fr([(16, 40), (24, 18), (50, 8), (76, 14), (74, 28), (54, 30), (34, 38), (22, 52)]),
                                               strand([(30, 22), (60, 16)], 'light', 'f', 1.2)],
  bowl('side', top=-4, side=78, nape=84),
  bowl('back', top=-4, side=78, nape=84))

# Sadley Lonsom: pelo negro en casco con mechas verde agua y un flequillo recto largo que le tapa los ojos; asoman los ojos
# azules por debajo; sonrisa
TEAL = _c('#2aa0a0')
C('sadley-lonsom', 'normal', P('#1a2428', '#fbe4d4', iris='#3a6ac0', shade='#10181a'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=92, eye_y=78, hairline=[(6, 70), (12, 72), (88, 72), (94, 70)]),
  bowl3('front', top=-2, side=84, nape=90, fringe=72) + [strand([(24, 50), (20, 80)], TEAL, 'f', 2.0), strand([(76, 50), (80, 80)], TEAL, 'f', 2.0),
                                                       strand([(40, 52), (38, 70)], TEAL, 'f', 1.6)],
  bowl3('side', top=-2, side=84, nape=90, fringe=70) + [strand([(70, 56), (76, 70)], TEAL, 'f', 1.6)],
  bowl3('back', top=-2, side=84, nape=90, fringe=72))

# Safine Papillonia: melena larga ondulada castaña que se aclara a rubio en las puntas, con un mechón que le tapa el ojo
# izquierdo; ojos naranjas con pestañas y sonrisa
BLD = _c('#f0d8a8')
C('safine-papillonia', 'chica', P('#9a7a58', '#fcdcc4', iris='#e07a20', shade='#7a5c40'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=[(6, 70), (16, 50), (30, 44), (50, 42), (70, 46), (84, 52), (94, 70)]),
  [L(outline([(0, 92), (-6, 120), (6, 132, 1), (20, 122), (12, 100)]), BLD, 'b'), L(outline([(100, 92), (106, 120), (94, 132, 1), (80, 122), (88, 100)]), BLD, 'b')] +
  dome('front', top=-2, w=48, cy=46, n=5, amp=5, soft=True, seed=29, long=110, flare=6, ends=3) +
  [L(blob([(-2, 92), (24, 90), (26, 112), (-2, 114)], 6), BLD, 'b', False), L(blob([(102, 92), (76, 90), (74, 112), (102, 114)], 6), BLD, 'b', False),
   fr([(46, 36), (66, 30), (84, 44), (86, 64), (80, 84, 1), (72, 68), (62, 58), (50, 50)]), strand([(18, 60), (10, 100)], BLD, 'b', 3.0)],
  dome('side', top=-2, w=48, cy=46, n=5, amp=5, soft=True, seed=29, long=110, flare=6, fr=56) + [L(outline([(4, 96), (0, 120), (14, 130, 1), (26, 116)]), BLD, 'b')],
  dome('back', top=-2, w=48, cy=46, n=5, amp=5, soft=True, seed=29, long=110, flare=6, ends=3) +
  [L(blob([(4, 90), (96, 90), (96, 112), (50, 116), (4, 112)], 6), BLD, 'b', False)])

# Sahl Saltzman: grandullón de cara anchísima; pelo morado corto y rizado; cejas negras gruesas enfadadas, ojos azules y boca
# apretada con la barbilla marcada
C('sahl-saltzman', 'corpulento', P('#5a2a62', '#f6c09a', iris='#3a7ab0', shade='#401c48'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=98, ear_out=8, face_front=face(w=12, chin=110, jaw=10, top=34), face_side=face_side(chin=6, jaw=8),
    hairline=[(4, 62), (14, 50), (30, 46), (50, 48), (70, 46), (86, 50), (96, 62)], nose=(50, 88, 3)),
  dome('front', top=4, w=54, cy=46, n=10, amp=5, soft=True, seed=31, sb=68) + thick_brows(66, BLACK, 5.0, 16, 1.6, 15) +
  [L(quad((44, 104), (50, 106), (56, 104)), OUTC, 'f', False, False, 1.2)],
  dome('side', top=4, w=52, cy=46, n=10, amp=5, soft=True, seed=31, nape=80, fr=52) + side_brow(66, BLACK, 5.0, 1.6),
  dome('back', top=4, w=54, cy=46, n=10, amp=5, soft=True, seed=31, nape=82))

# Salpida Longwheel: pelo verde menta abombado en rizos grandes con un moño en espiral arriba; ojos entornados con pestañas
# menta y sonrisa suave
MINT = _c('#a8d8b8')
def _swirl(x, y):
    return [bun(x, y, 9), L(outline([(x + 4, y - 8), (x + 10, y - 22), (x + 2, y - 30), (x - 6, y - 26, 1), (x + 2, y - 24), (x + 4, y - 16)]))]
C('salpida-longwheel', 'chica', P('#c4e2cc', '#fde4d4', iris='#4a8a60', shade='#98c0a4', light='#e0f2e4'),
  F(eyes='closed', brows=False, mouth='smile', mouth_y=92, hairline=[(6, 66), (16, 54), (30, 48), (50, 50), (70, 48), (84, 54), (94, 66)]),
  _swirl(50, 2) + dome('front', top=0, w=54, cy=48, n=7, amp=7, soft=True, seed=33, sb=92) +
  [L(quad((26, 72), (36, 68), (46, 72)), MINT, 'f', False, False, 2.0), L(quad((54, 72), (64, 68), (74, 72)), MINT, 'f', False, False, 2.0)],
  _swirl(44, 2) + dome('side', top=0, w=52, cy=48, n=7, amp=7, soft=True, seed=33, nape=94, fr=54),
  _swirl(50, 2) + dome('back', top=0, w=54, cy=48, n=7, amp=7, soft=True, seed=33, nape=96))

# Sami Wampovich (portera): pelo castaño oscuro corto con mechones por la frente y una coleta baja que cae por detrás de un
# hombro; ojos cerrados de risa, coloretes y sonrisa de dientes
C('sami-wampovich', 'chica', P('#3a2a24', '#fbdcc4', shade='#2a1e1a'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=92, hairline=hl(6, 66, 50, 60, jit=2, seed=35)),
  [tail(14, 86, 4, 128, 12)] + dome('front', top=0, w=48, cy=46, sb=80) + eyes_arc(76) +
  [L(ell(22, 86, 5, 3), RED, 'f', False), L(ell(78, 86, 5, 3), RED, 'f', False)],
  [tail(24, 80, 14, 126, 12)] + dome('side', top=0, w=48, cy=46, nape=86, fr=58) +
  [L(quad((74, 78), (80, 72), (86, 78)), OUTC, 'f', False, False, 2.2)],
  [tail(30, 84, 22, 128, 12)] + dome('back', top=0, w=48, cy=46, nape=88))

# Santi Lite: calvo; gafas enormes de cristal verde oscuro en forma de alas de insecto; cejas gruesas en arco y sonrisa de
# dientes
DKG = _c('#1e3a28')
C('santi-lite', 'normal', P('#c89a88', '#e8b8a0', shade='#b08878'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=96, hairline=False, ear_out=2),
  [L(blob([(18, 56), (16, 30), (28, 12), (50, 4), (72, 12), (84, 30), (82, 56)], 8), 'skin'),
   L(outline([(16, 66), (28, 64), (46, 72), (44, 86), (32, 90), (20, 82)]), DKG, 'f'), L(outline([(84, 66), (72, 64), (54, 72), (56, 86), (68, 90), (80, 82)]), DKG, 'f'),
   L(ell(36, 78, 4, 3), _c('#5a8a64'), 'f', False), L(ell(64, 78, 4, 3), _c('#5a8a64'), 'f', False),
   L(quad((20, 60), (30, 52), (42, 60)), OUTC, 'f', False, False, 2.6), L(quad((58, 60), (70, 52), (80, 60)), OUTC, 'f', False, False, 2.6)],
  [L(outline([(72, 66), (90, 68), (88, 86), (74, 88)]), DKG, 'f'), L(quad((72, 60), (80, 54), (88, 58)), OUTC, 'f', False, False, 2.6)],
  [L(blob([(18, 64), (16, 30), (28, 12), (50, 4), (72, 12), (84, 30), (82, 64), (50, 70)], 8), 'skin'), L([(14, 78), (86, 78)], OUTC, 'f', False, False, 1.6)])

# Sara Lyle: pelo gris con un moño en forma de concha arriba sujeto con una goma amarilla y dos rodetes oscuros a los lados;
# ojos de espiral amarillos, ceño fruncido, coloretes y boca enfurruñada
DKB, YELL = _c('#3a3434'), _c('#f0d040')
def _shell(x):
    return [L(blob([(x - 16, 0), (x - 10, -14), (x, -18), (x + 10, -14), (x + 16, 0), (x, 4)], 4)),
            L([(x, -16), (x, 2)], 'shade', 'b', False, False, 1.0), L([(x - 8, -12), (x - 4, 2)], 'shade', 'b', False, False, 1.0),
            L([(x + 8, -12), (x + 4, 2)], 'shade', 'b', False, False, 1.0), L(ell(x, 4, 7, 3), YELL, 'b')]
C('sara-lyle', 'chica', P('#a8a098', '#fde8dc', shade='#8a8278'),
  F(eyes='none', brows='angry', mouth='frown', mouth_y=93, hairline=[(6, 70), (16, 54), (30, 50), (42, 58), (50, 52), (58, 58), (70, 50), (84, 54), (94, 70)]),
  [bun(8, 60, 8, DKB), bun(92, 60, 8, DKB), bun(8, 92, 8, DKB), bun(92, 92, 8, DKB)] + _shell(50) + dome('front', top=4, w=46, cy=46, long=96, flare=2, ends=3) +
  [L(ell(36, 76, 6, 6), YELL, 'f'), L(ell(64, 76, 6, 6), YELL, 'f'), L(ell(36, 76, 3, 3) + [ell(36, 76, 3, 3)[0]], OUTC, 'f', False, False, 1.2),
   L(ell(64, 76, 3, 3) + [ell(64, 76, 3, 3)[0]], OUTC, 'f', False, False, 1.2), L(ell(22, 88, 5, 4), RED, 'f', False), L(ell(78, 88, 5, 4), RED, 'f', False)],
  [bun(30, 60, 8, DKB), bun(30, 92, 8, DKB)] + _shell(44) + dome('side', top=4, w=46, cy=46, long=96, flare=2, fr=56) +
  [L(ell(82, 76, 4, 6), YELL, 'f'), L(ell(80, 88, 5, 4), RED, 'f', False)],
  [bun(8, 60, 8, DKB), bun(92, 60, 8, DKB), bun(8, 92, 8, DKB), bun(92, 92, 8, DKB)] + _shell(50) + dome('back', top=4, w=46, cy=46, long=96, flare=2, ends=3))

# Selen Dippity: pelo rojo anaranjado en mechones ondulados como llamas que se curvan hacia fuera; ojos afilados rojos de
# enfado y boca apretada
C('selen-dippity', 'chica', P('#e8582a', '#fbd6be', iris='#a82020', shade='#c03a1a', light='#f08a4a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=hl(7, 70, 50, 64, lean=1, jit=3, seed=37)),
  dome('front', top=-10, w=52, cy=46, n=10, amp=10, sweep=0.2, seed=37, sb=86) +
  [L(outline([(6, 70), (-6, 78), (-2, 90, 1), (8, 84)])), L(outline([(94, 70), (106, 78), (102, 90, 1), (92, 84)]))],
  dome('side', top=-10, w=50, cy=46, n=10, amp=10, sweep=0.2, seed=37, nape=90, fr=58),
  dome('back', top=-10, w=52, cy=46, n=10, amp=10, sweep=0.2, seed=37, nape=92))

# Selena Sopralis: melena larga y lisa blanca con flequillo recto y mechas azules a los lados y en las puntas; ojos rojos y
# boca pequeña
BLU = _c('#2a8ac8')
C('selena-sopralis', 'chica', P('#eef2f4', '#fbe2d4', iris='#a82a3a', shade='#c8d0d8'),
  F(eyes='normal', brows=False, mouth='line', mouth_y=92, hairline=[(6, 70), (12, 62), (88, 62), (94, 70)]),
  dome('front', top=-2, w=47, cy=46, long=110, flare=2, ends=4) + [fr([(14, 42), (30, 26), (50, 24), (70, 26), (86, 42), (88, 66), (12, 66)]),
                                                                  strand([(30, 40), (30, 66)], BLU, 'f', 2.4), strand([(66, 40), (66, 66)], BLU, 'f', 2.4),
                                                                  strand([(10, 70), (12, 108)], BLU, 'b', 3.0), strand([(90, 70), (88, 108)], BLU, 'b', 3.0)],
  dome('side', top=-2, w=47, cy=46, long=110, flare=2, fr=66) + [strand([(30, 70), (26, 106)], BLU, 'b', 3.0)],
  dome('back', top=-2, w=47, cy=46, long=110, flare=2, ends=4) + [strand([(20, 80), (18, 108)], BLU, 'b', 3.0), strand([(80, 80), (82, 108)], BLU, 'b', 3.0)])

# Selina Goldpyre: media melena lila muy clara con flequillo recto y dos mechones azul marino grandes que caen a los lados
# como orejas de perro; gafas redondas negras y sonrisa
NAV = _c('#1e2442')
C('selina-goldpyre', 'chica', P('#e4e0ee', '#fbe4d4', iris='#6a6a70', shade='#c0b8cc'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=92, hairline=[(6, 70), (12, 62), (88, 62), (94, 70)]),
  [L(outline([(16, 30), (-10, 52), (-8, 64, 1), (6, 60), (10, 96, 1), (20, 70)]), NAV, 'b'), L(outline([(84, 30), (110, 52), (108, 64, 1), (94, 60), (90, 96, 1), (80, 70)]), NAV, 'b')] +
  bowl3('front', top=-2, side=94, nape=94, fringe=62) + round_specs('front', OUTC, 77, 14, 9, 7, 2.0),
  [L(outline([(30, 20), (6, 44), (8, 58, 1), (20, 52), (22, 94, 1), (34, 64)]), NAV, 'b')] + bowl3('side', top=-2, side=94, nape=94, fringe=60) +
  round_specs('side', OUTC, 77, 14, 9, 7, 2.0),
  [L(outline([(16, 30), (-10, 52), (-8, 64, 1), (6, 60), (10, 96, 1), (20, 70)]), NAV, 'b'), L(outline([(84, 30), (110, 52), (108, 64, 1), (94, 60), (90, 96, 1), (80, 70)]), NAV, 'b')] +
  bowl3('back', top=-2, side=94, nape=94, fringe=62))

# Seph T. Forst: pelo gris oscuro en cepillo plano con dos picos arriba; dos rizos de pintura verde en las patillas; cejas
# gruesas enfadadas, mandíbula cuadrada y boca torcida
GRN = _c('#78d8a0')
C('seph-t-forst', 'normal', P('#3e3e4a', '#f8d4a8', iris='#5a6a90', shade='#2c2c36'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=98, face_front=face(w=4, chin=106, jaw=6), face_side=face_side(chin=6, jaw=6),
    hairline=[(10, 60), (16, 50), (84, 50), (90, 60)]),
  [L(outline([(14, 60), (12, 34), (16, 14), (20, -2, 1), (34, 10), (66, 10), (80, -2, 1), (84, 14), (88, 34), (86, 60), (80, 50), (20, 50)])),
   L(blob([(14, 62), (22, 64), (24, 76), (16, 82), (12, 72)], 4), GRN, 'f', False), L(blob([(86, 62), (78, 64), (76, 76), (84, 82), (88, 72)], 4), GRN, 'f', False),
   *thick_brows(66, BLACK, 5.0, 14, 1.8, 13)],
  [L(outline([(62, 50), (82, 46), (86, 24), (82, 10), (72, -4, 1), (60, 8), (34, 8), (14, 16), (6, 36), (8, 64), (24, 72), (40, 62), (50, 54)])),
   L(blob([(70, 62), (78, 64), (78, 78), (70, 80)], 4), GRN, 'f', False), side_brow(66, BLACK, 5.0, 1.8)],
  [L(outline([(12, 70), (10, 34), (16, 14), (20, -2, 1), (34, 10), (66, 10), (80, -2, 1), (84, 14), (90, 34), (88, 70), (50, 76)]))])

# Serene Goldwell: melena rubia dorada ondulada con tirabuzones gruesos a los lados; ojos naranjas con sombra morada y
# pestañas de puntitos; boca abierta
PURP = _c('#7a4a9a')
C('serene-goldwell', 'chica', P('#d8c070', '#fde4d4', iris='#e07a20', shade='#b09a50', light='#ead890'),
  F(eyes='big', brows=False, mouth='grin', mouth_y=94, hairline=[(6, 70), (16, 52), (30, 46), (44, 56), (50, 48), (60, 56), (72, 46), (84, 52), (94, 70)]),
  _ringlets([4, 96], 76, 112) + dome('front', top=-6, w=50, cy=46, n=7, amp=5, soft=True, seed=39, sb=90) +
  [L(quad((26, 68), (36, 62), (46, 68)), PURP, 'f', False, False, 2.4), L(quad((54, 68), (64, 62), (74, 68)), PURP, 'f', False, False, 2.4)],
  _ringlets([24], 76, 112) + dome('side', top=-6, w=50, cy=46, n=7, amp=5, soft=True, seed=39, nape=92, fr=54),
  _ringlets([8, 50, 92], 76, 112) + dome('back', top=-6, w=50, cy=46, n=7, amp=5, soft=True, seed=39, nape=94))

# Serina Shelby (portera): pelo verde azulado oscuro con dos lazadas de pelo arriba como orejitas y flequillo recto; mechones
# largos a los lados y una coleta baja ancha que se aclaran a castaño en las puntas (modelo 3D); ojos afilados verdes
BRN = _c('#8a5a3a')
def _loops(x, y):
    return [L(outline([(x - 4, y + 4), (x - 14, y - 10), (x - 8, y - 16), (x - 2, y - 6)])), L(outline([(x + 4, y + 4), (x + 14, y - 10), (x + 8, y - 16), (x + 2, y - 6)]))]
C('serina-shelby', 'chica', P('#1e4a5a', '#fbd8c0', iris='#2a9a8a', shade='#143440'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=[(6, 70), (12, 60), (88, 60), (94, 70)]),
  _loops(50, 6) + dome('front', top=2, w=46, cy=46, sb=70) + [fr([(16, 42), (30, 28), (50, 26), (70, 28), (84, 42), (86, 62), (14, 62)]),
                                                             L(outline([(12, 60), (6, 96), (10, 110, 1), (18, 92), (20, 62)]), 'mid', 'f'),
                                                             L(outline([(88, 60), (94, 96), (90, 110, 1), (82, 92), (80, 62)]), 'mid', 'f'),
                                                             L(outline([(8, 92), (10, 110, 1), (17, 94)]), BRN, 'f'), L(outline([(92, 92), (90, 110, 1), (83, 94)]), BRN, 'f')],
  _loops(46, 6) + [tail(30, 70, 14, 118, 16), L(outline([(20, 100), (14, 118, 1), (26, 104)]), BRN, 'b')] + dome('side', top=2, w=46, cy=46, nape=78, fr=60),
  _loops(50, 6) + [L(outline([(30, 66), (70, 66), (78, 104), (66, 116, 1), (56, 108), (50, 118, 1), (44, 108), (34, 116, 1), (22, 104)])),
                   L(blob([(24, 98), (76, 98), (70, 114), (30, 114)], 4), BRN, 'b', False)] + dome('back', top=2, w=46, cy=46, nape=76))

# Shawl Creedstern (portero): pelo azul marino muy oscuro en pinchos hacia arriba con mechas doradas y mechones largos que le
# caen a los lados de la cara; piel morena, ojos afilados y boca seria
GOLD = _c('#b09a3a')
C('shawl-creedstern', 'normal', P('#22224a', '#c08a68', iris='#4a2a1a', shade='#161634'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, face_front=face(chin=104), hairline=hl(6, 66, 48, 64, lean=1, jit=3, seed=41)),
  dome('front', top=-16, w=48, cy=44, n=8, amp=14, sweep=0.2, seed=41, sb=70) +
  [strand([(36, 10), (30, 34)], GOLD, 'b', 2.4), strand([(66, 8), (70, 30)], GOLD, 'b', 2.4),
   L(outline([(14, 60), (10, 96), (16, 108, 1), (20, 88), (22, 62)]), 'mid', 'f'), L(outline([(86, 60), (90, 96), (84, 108, 1), (80, 88), (78, 62)]), 'mid', 'f')],
  dome('side', top=-16, w=48, cy=44, n=8, amp=14, sweep=0.2, seed=41, nape=86, fr=56) + [strand([(40, 6), (36, 30)], GOLD, 'b', 2.4)],
  dome('back', top=-16, w=48, cy=44, n=8, amp=14, sweep=0.2, seed=41, nape=88) + [strand([(40, 6), (34, 36)], GOLD, 'b', 2.4), strand([(64, 6), (68, 34)], GOLD, 'b', 2.4)])

# Shena Ennigans: media melena ondulada verde azulado oscuro con la raya a un lado; gafas grandes cuadradas color caramelo,
# ojos azules con pestañas y sonrisa
CAR = _c('#c87a2a')
C('shena-ennigans', 'chica', P('#1e4a5a', '#fbe0cc', iris='#2a4aa8', shade='#143440'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=[(6, 70), (16, 50), (30, 44), (54, 40), (70, 48), (84, 54), (94, 70)]),
  dome('front', top=-2, w=48, cy=46, n=6, amp=5, soft=True, seed=43, long=102, flare=8, ends=3) +
  [fr([(16, 48), (30, 30), (56, 26), (64, 34), (44, 44), (30, 56), (20, 70)]),
   L(blob([(22, 68), (46, 68), (46, 84), (22, 84)], 3) + [(22, 68)], CAR, 'f', False, False, 2.6),
   L(blob([(54, 68), (78, 68), (78, 84), (54, 84)], 3) + [(54, 68)], CAR, 'f', False, False, 2.6), L([(46, 74), (54, 74)], CAR, 'f', False, False, 2.2)],
  dome('side', top=-2, w=48, cy=46, n=6, amp=5, soft=True, seed=43, long=102, flare=8, fr=54) +
  [L([(74, 68), (88, 68), (88, 84), (74, 84), (74, 68)], CAR, 'f', False, False, 2.6), L([(74, 74), (52, 70)], CAR, 'f', False, False, 2.0)],
  dome('back', top=-2, w=48, cy=46, n=6, amp=5, soft=True, seed=43, long=102, flare=8, ends=3))

# Shiryu Hanabusa (portero): pelo rosa abombado en rizos esponjosos; ojos grandes verde agua, boca de gato y coloretes
def _catmouth(y=93):
    return [L(quad((44, y), (47, y + 3), (50, y)) + quad((50, y), (53, y + 3), (56, y))[1:], OUTC, 'f', False, False, 1.4)]
C('shiryu-hanabusa', 'bajito', P('#f6b8c0', '#fde0cc', iris='#2ab0b0', shade='#d890a0', light='#fcd8de'),
  F(eyes='big', brows=False, mouth='none', hairline=[(6, 70), (16, 58), (30, 62), (40, 54), (52, 62), (64, 54), (76, 62), (86, 58), (94, 70)]),
  dome('front', top=-8, w=52, cy=46, n=11, amp=7, soft=True, seed=45, sb=80) + _catmouth() +
  [L(ell(22, 86, 6, 4), RED, 'f', False), L(ell(78, 86, 6, 4), RED, 'f', False)],
  dome('side', top=-8, w=50, cy=46, n=11, amp=7, soft=True, seed=45, nape=84, fr=60) + [L(ell(80, 86, 5, 4), RED, 'f', False)],
  dome('back', top=-8, w=52, cy=46, n=11, amp=7, soft=True, seed=45, nape=86))

# Sienna Fairborn: dos coletas largas color malva grisáceo atadas con lazos negros y flequillo recto; ojos lilas con pestañas
# y sonrisa
C('sienna-fairborn', 'chica', P('#8a7a88', '#fde4d8', iris='#a87ac8', shade='#6a5a68'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=[(6, 70), (12, 62), (88, 62), (94, 70)]),
  [tail(10, 40, 2, 128, 16), tail(90, 40, 98, 128, 16)] + dome('front', top=0, w=46, cy=46, sb=82) +
  [fr([(16, 42), (30, 28), (50, 26), (70, 28), (84, 42), (86, 64), (14, 64)]), L(ell(10, 38, 6, 4), BLACK, 'f'), L(ell(90, 38, 6, 4), BLACK, 'f')],
  [tail(38, 30, 20, 128, 16, bend=-6)] + dome('side', top=0, w=46, cy=46, nape=86, fr=62) + [L(ell(38, 30, 5, 5), BLACK, 'f')],
  [tail(14, 38, 6, 128, 16), tail(86, 38, 94, 128, 16)] + dome('back', top=0, w=46, cy=46, nape=88) + [L(ell(14, 38, 6, 4), BLACK, 'f'), L(ell(86, 38, 6, 4), BLACK, 'f')])

# Silky Fersken: media melena roja coral lisa con la raya en medio; ojos entornados verde agua y boca pequeña
C('silky-fersken', 'chica', P('#e85a6a', '#fde4d8', iris='#2a9a8a', shade='#c03a4a'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=93, hairline=[(6, 70), (16, 54), (34, 44), (50, 40), (66, 44), (84, 54), (94, 70)]),
  dome('front', top=0, w=48, cy=46, long=98, flare=6, ends=4) + [strand([(50, 4), (50, 40)], 'shade', 'b', 1.2)],
  dome('side', top=0, w=48, cy=46, long=98, flare=6, fr=52),
  dome('back', top=0, w=48, cy=46, long=98, flare=6, ends=4))

# Slater Verbenbaum: pelo castaño claro en cepillo de pinchos con las puntas rubias; piel muy clara, cejas rubias, ojos
# lilas con raya negra marcada y boca enfurruñada
BLO = _c('#f0e4a0')
C('slater-verbenbaum', 'normal', P('#a8885a', '#fde6d8', iris='#a888c8', shade='#86683e'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=94, hairline=[(10, 62), (16, 50), (84, 50), (90, 62)]),
  [L(outline([(14, 62), (12, 34), (4, 10, 1), (18, 16), (20, -4, 1), (32, 8), (42, -8, 1), (52, 6), (62, -8, 1), (70, 8), (82, -4, 1), (84, 16), (98, 10, 1),
              (88, 34), (86, 62), (80, 50), (20, 50)])),
   L(outline([(4, 10), (18, 16), (20, -4), (32, 8), (42, -8), (52, 6), (62, -8), (70, 8), (82, -4), (84, 16), (98, 10), (90, 20), (10, 20)]), BLO, 'b', False),
   L(quad((26, 64), (34, 60), (44, 64)), BLO, 'f', False, False, 3.0), L(quad((56, 64), (66, 60), (74, 64)), BLO, 'f', False, False, 3.0),
   L([(22, 72), (28, 71)], OUTC, 'f', False, False, 2.4), L([(78, 72), (72, 71)], OUTC, 'f', False, False, 2.4)],
  [L(outline([(66, 50), (84, 46), (90, 26), (98, 10, 1), (82, 12), (80, -6, 1), (64, 6), (48, -8, 1), (36, 6), (16, 4, 1), (20, 18), (6, 30), (6, 60), (22, 70), (40, 62), (54, 54)])),
   L(outline([(98, 10), (82, 12), (80, -6), (64, 6), (48, -8), (36, 6), (16, 4), (20, 18), (40, 16), (90, 20)]), BLO, 'b', False)],
  [L(outline([(12, 72), (10, 34), (4, 10, 1), (18, 16), (20, -4, 1), (32, 8), (42, -8, 1), (52, 6), (62, -8, 1), (70, 8), (82, -4, 1), (84, 16), (98, 10, 1),
              (90, 34), (88, 72), (50, 78)])),
   L(outline([(4, 10), (18, 16), (20, -4), (32, 8), (42, -8), (52, 6), (62, -8), (70, 8), (82, -4), (84, 16), (98, 10), (90, 20), (10, 20)]), BLO, 'b', False)])

# Smiles Thrussell: cara ancha; pelo castaño oscuro corto con un pico en el centro; gafas rectangulares grises, cejas de
# enfado y una sonrisa de suficiencia
GRAY = _c('#a8a8a8')
C('smiles-thrussell', 'corpulento', P('#4a3a30', '#fde2cc', iris='#2a2a30', shade='#342820'),
  F(eyes='dot', brows='angry', mouth='smile', mouth_y=96, ear_out=6, face_front=face(w=8, chin=106, jaw=8), face_side=face_side(chin=4, jaw=5),
    hairline=[(6, 62), (14, 48), (36, 42), (50, 46), (64, 42), (86, 48), (94, 62)]),
  [L(outline([(10, 62), (8, 34), (22, 14), (40, 6), (50, -6, 1), (60, 6), (78, 14), (92, 34), (90, 62), (82, 48), (18, 48)])),
   L(blob([(22, 70), (46, 70), (46, 82), (22, 82)], 2) + [(22, 70)], GRAY, 'f', False, False, 3.0),
   L(blob([(54, 70), (78, 70), (78, 82), (54, 82)], 2) + [(54, 70)], GRAY, 'f', False, False, 3.0), L([(46, 74), (54, 74)], GRAY, 'f', False, False, 2.4),
   L([(14, 74), (22, 74)], GRAY, 'f', False, False, 2.4), L([(86, 74), (78, 74)], GRAY, 'f', False, False, 2.4)],
  [L(outline([(62, 48), (80, 44), (84, 26), (70, 6), (54, -6, 1), (44, 4), (24, 8), (8, 26), (4, 56), (16, 72), (36, 66), (52, 54)])),
   L([(74, 70), (88, 70), (88, 82), (74, 82), (74, 70)], GRAY, 'f', False, False, 3.0), L([(74, 74), (48, 72)], GRAY, 'f', False, False, 2.4)],
  [L(outline([(10, 72), (8, 34), (22, 14), (40, 6), (50, -6, 1), (60, 6), (78, 14), (92, 34), (90, 72), (50, 78)]))])

# Somnal Brightmore: pelo azul marino muy rizado con una cinta roja ancha en la cabeza; piel morena, ojos verde agua de
# enfado y boca seria
C('somnal-brightmore', 'normal', P('#22264a', '#9a6a48', iris='#2ab0b0', shade='#161834'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=94, hairline=[(6, 70), (14, 56), (30, 50), (50, 52), (70, 50), (86, 56), (94, 70)]),
  dome('front', top=-8, w=52, cy=46, n=13, amp=6, soft=True, seed=47, sb=86) +
  [L(quad((8, 50), (50, 14), (92, 50)) + quad((92, 42), (50, 4), (8, 42)), CRIM, 'f')],
  dome('side', top=-8, w=50, cy=46, n=13, amp=6, soft=True, seed=47, nape=88, fr=58) + [L(quad((84, 50), (50, 8), (14, 26)) + quad((10, 18), (50, -2), (86, 42)), CRIM, 'f')],
  dome('back', top=-8, w=52, cy=46, n=13, amp=6, soft=True, seed=47, nape=90) + [L(quad((6, 44), (50, 10), (94, 44)) + quad((94, 36), (50, 0), (6, 36)), CRIM, 'f')])

# Sona Sondheim: pelo rubio ceniza peinado hacia atrás con una diadema azul y dos trenzas largas que caen por delante;
# cejas claras, ojos azules y boca pequeña
def _braid(x0, y0, x1, y1, n=5):
    out = []
    for i in range(n):
        t = i / (n - 1)
        out.append(L(ell(x0 + (x1 - x0) * t + (2 if i % 2 else -2), y0 + (y1 - y0) * t, 6, 6), 'mid', 'f'))
    return out
C('sona-sondheim', 'chica', P('#d0c8b0', '#fbe8dc', iris='#3a6ac8', shade='#a8a088'),
  F(eyes='normal', brows=False, mouth='line', mouth_y=93, hairline=[(6, 66), (16, 50), (34, 40), (50, 38), (66, 40), (84, 50), (94, 66)]),
  dome('front', top=0, w=46, cy=46, sb=84) + _braid(12, 86, 10, 128) + _braid(88, 86, 90, 128) +
  [L(quad((8, 46), (50, 2), (92, 46)), BLU, 'f', False, False, 3.6), L(quad((26, 64), (34, 60), (44, 64)), 'shade', 'f', False, False, 2.4),
   L(quad((56, 64), (66, 60), (74, 64)), 'shade', 'f', False, False, 2.4)],
  dome('side', top=0, w=46, cy=46, nape=84, fr=46) + _braid(46, 86, 50, 128) + [L(quad((84, 44), (60, 0), (30, 6)), BLU, 'f', False, False, 3.6)],
  dome('back', top=0, w=46, cy=46, nape=86) + [L(quad((6, 46), (50, 4), (94, 46)), BLU, 'f', False, False, 3.6)])

# Sonata Cherub: pelo blanco abombado como una nube que se vuelve rosado por abajo y se abre en mechones a los lados;
# ojos grandes verdes, coloretes y sonrisa
PNK = _c('#d0a8b0')
C('sonata-cherub', 'chica', P('#f0ecf4', '#fde4d8', iris='#8aa880', shade='#d0c8d8'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, hairline=hl(6, 70, 52, 62, jit=3, seed=49)),
  [L(outline([(6, 70), (-14, 92), (4, 100, 1), (14, 84)]), PNK, 'b'), L(outline([(94, 70), (114, 92), (96, 100, 1), (86, 84)]), PNK, 'b')] +
  dome('front', top=-10, w=56, cy=46, n=10, amp=8, soft=True, seed=49, sb=84) +
  [L(blob([(-4, 64), (18, 62), (20, 84), (0, 84)], 6), PNK, 'b', False), L(blob([(104, 64), (82, 62), (80, 84), (100, 84)], 6), PNK, 'b', False),
   L(ell(22, 86, 6, 4), RED, 'f', False), L(ell(78, 86, 6, 4), RED, 'f', False)],
  dome('side', top=-10, w=54, cy=46, n=10, amp=8, soft=True, seed=49, nape=88, fr=60) + [L(blob([(0, 60), (40, 62), (44, 86), (4, 88)], 6), PNK, 'b', False)],
  dome('back', top=-10, w=56, cy=46, n=10, amp=8, soft=True, seed=49, nape=90) + [L(blob([(-4, 60), (104, 60), (100, 88), (0, 88)], 6), PNK, 'b', False)])

# Sophia Goston: media melena negra lisa con flequillo recto muy bajo y una cofia blanca de volantes; ojos grandes negros
def _frill(view):
    if view == 'side':
        return [L(ell(26 + i * 10, 8 - i * 2 + (i * i) * 0.6, 4.5, 4.5), WHITE, 'f') for i in range(6)]
    return [L(ell(50 + 44 * __import__('math').cos(a), 46 - 44 * __import__('math').sin(a), 4.5, 4.5), WHITE, 'f') for a in [0.25 + k * 0.33 for k in range(9)]]
C('sophia-goston', 'chica', P('#141418', '#fde6d8', iris='#141418', shade='#0a0a0c'),
  F(eyes='big', brows=False, mouth='none', hairline=[(6, 70), (12, 66), (88, 66), (94, 70)]),
  bowl3('front', top=2, side=90, nape=92, fringe=66) + _frill('front'),
  bowl3('side', top=2, side=90, nape=92, fringe=64) + _frill('side'),
  bowl3('back', top=2, side=90, nape=92, fringe=66) + _frill('back'))

# Soria Bordeau: pelo castaño rojizo en seta redonda con un mechón de antena arriba y un pico de flequillo en el centro;
# ojos verdes con pestañas y coloretes
C('soria-bordeau', 'chica', P('#8a4a48', '#fde4d4', iris='#5aa860', shade='#6a3432'),
  F(eyes='normal', brows=False, mouth='none', hairline=[(6, 66), (12, 58), (42, 58), (50, 68), (58, 58), (88, 58), (94, 66)]),
  bowl3('front', top=6, side=74, nape=82, w=6, fringe=58) + [L(quad((50, 8), (40, -14), (54, -16)) + [(56, -8), (52, 8)]),
                                                             L(ell(22, 86, 5, 3), RED, 'f', False), L(ell(78, 86, 5, 3), RED, 'f', False)],
  bowl3('side', top=6, side=74, nape=82, w=6, fringe=56) + [L(quad((48, 6), (38, -16), (52, -18)) + [(54, -10), (50, 6)])],
  bowl3('back', top=6, side=74, nape=82, w=6, fringe=58) + [L(quad((50, 8), (40, -14), (54, -16)) + [(56, -8), (52, 8)])])

# Starry Durant: pelo morado oscuro en dos moños enormes a los lados; gafas cuadradas de píxeles azules con dos antenas y una
# sonrisa enorme
def _pixglasses(view):
    if view == 'side':
        return [L([(72, 68), (90, 68), (90, 84), (72, 84), (72, 68)], GRAY, 'f', False, False, 2.4), L(blob([(73, 69), (89, 69), (89, 83), (73, 83)], 2), _c('#2a6ac8'), 'f', False),
                L([(72, 74), (40, 70)], GRAY, 'f', False, False, 2.4), L([(78, 68), (78, 46)], GRAY, 'f', False, False, 2.0), L(ell(78, 44, 3, 3), GRAY, 'f')]
    out = []
    for x0 in (20, 54):
        out += [L(blob([(x0, 68), (x0 + 26, 68), (x0 + 26, 86), (x0, 86)], 2), _c('#1a3a9a'), 'f'),
                L(blob([(x0 + 2, 70), (x0 + 13, 70), (x0 + 13, 77), (x0 + 2, 77)], 1), _c('#4ab0f0'), 'f', False),
                L(blob([(x0 + 13, 77), (x0 + 24, 77), (x0 + 24, 84), (x0 + 13, 84)], 1), _c('#4ab0f0'), 'f', False),
                L([(x0 + 2, 68), (x0 + 2, 46)], GRAY, 'f', False, False, 2.0), L(ell(x0 + 2, 44, 3, 3), GRAY, 'f')]
    return out + [L([(46, 74), (54, 74)], GRAY, 'f', False, False, 2.4)]
C('starry-durant', 'normal', P('#3a2a5a', '#fcd8b8', shade='#281c40', light='#5a4a7a'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=97, hairline=[(6, 62), (14, 52), (86, 52), (94, 62)]),
  [bun(4, 42, 18), bun(96, 42, 18)] + dome('front', top=0, w=48, cy=46, sb=64) + _pixglasses('front'),
  dome('side', top=0, w=48, cy=46, nape=80, fr=52) + [bun(18, 34, 18, 'mid', 'f')] + _pixglasses('side'),
  [bun(4, 42, 18), bun(96, 42, 18)] + dome('back', top=0, w=48, cy=46, nape=82))

# Stellan Checkman: gorro de lana gris oscuro con pompón crema calado hasta las cejas y mechones rubios desgreñados que
# asoman por los lados y la frente; ojos afilados y mueca de dientes
BEA, POM = _c('#4a4a52'), _c('#e0d8c0')
def _beanie2(view):
    if view == 'side':
        return [L(outline([(86, 46), (88, 26), (74, 6), (48, 0), (22, 6), (6, 26), (4, 50), (30, 54), (60, 50)]), BEA), L(blob([(4, 44), (88, 38), (88, 50), (4, 56)], 4), BEA),
                L(ell(42, -2, 9, 7), POM)]
    return [L(outline([(8, 50), (10, 24), (28, 6), (50, 0), (72, 6), (90, 24), (92, 50), (50, 48)]), BEA),
            L(blob([(6, 42), (50, 38), (94, 42), (94, 54), (50, 50), (6, 54)], 4), BEA), L(ell(50, -4, 10, 7), POM)] + \
           [L([(x, 8 if abs(x - 50) < 30 else 16), (x, 40)], _c('#3a3a40'), 'b', False, False, 1.0) for x in (24, 36, 50, 64, 76)]
C('stellan-checkman', 'normal', P('#d8c068', '#fde6d4', iris='#3a3020', shade='#b09a48'),
  F(eyes='sharp', brows=False, mouth='grin', mouth_y=95, hairline=[(6, 70), (14, 56), (30, 60), (40, 54), (50, 70), (58, 54), (70, 62), (86, 56), (94, 70)]),
  dome('front', top=10, w=48, cy=50, n=8, amp=8, sweep=-0.3, seed=51, sb=92) + [fr([(34, 50), (52, 50), (50, 72, 1), (44, 60), (38, 74, 1)])] + _beanie2('front'),
  dome('side', top=10, w=48, cy=50, n=8, amp=8, sweep=-0.3, seed=51, nape=94, fr=64) + _beanie2('side'),
  dome('back', top=10, w=48, cy=50, n=8, amp=8, sweep=-0.3, seed=51, nape=94) + _beanie2('back'))

# Sten Fanborough: pelo castaño rojizo corto y abultado; piel tostada con pecas, cejas gruesas enfadadas, ojos verdes y boca
# apretada
C('sten-fanborough', 'normal', P('#7a2a1e', '#e8a878', iris='#6a8a3a', shade='#5a1e14'),
  F(eyes='normal', brows=False, mouth='frown', mouth_y=95, ear_out=2, hairline=[(6, 62), (14, 52), (30, 46), (50, 48), (70, 46), (86, 52), (94, 62)]),
  dome('front', top=-4, w=48, cy=44, n=8, amp=5, soft=True, seed=53, sb=62) + thick_brows(64, _c('#5a1e14'), 4.6, 14, 1.6, 13) +
  [L(ell(x, 86, 0.9, 0.9), _c('#b06a40'), 'f', False) for x in (26, 30, 34, 66, 70, 74)],
  dome('side', top=-4, w=48, cy=44, n=8, amp=5, soft=True, seed=53, nape=80, fr=50) + side_brow(64, _c('#5a1e14'), 4.6, 1.6),
  dome('back', top=-4, w=48, cy=44, n=8, amp=5, soft=True, seed=53, nape=82))

# Stouton Savant (portero): grandullón de cara ancha con el pelo negro recogido en un moño de luchador de sumo; ojos
# apretados de esfuerzo y boca apretada
C('stouton-savant', 'corpulento', P('#1e1a1e', '#fce0cc', shade='#100e10'),
  F(eyes='none', brows='angry', mouth='frown', mouth_y=98, ear_out=8, face_front=face(w=10, chin=108, jaw=10, top=32), face_side=face_side(chin=6, jaw=8),
    hairline=[(4, 62), (16, 48), (34, 44), (50, 50), (66, 44), (84, 48), (96, 62)]),
  [L(outline([(6, 66), (6, 36), (20, 16), (50, 8), (80, 16), (94, 36), (94, 66), (82, 50), (18, 50)])), bun(50, 6, 9), L(ell(50, 14, 6, 3), 'shade', 'b'),
   L([(28, 72), (38, 76), (28, 80)], OUTC, 'f', False, False, 2.4), L([(72, 72), (62, 76), (72, 80)], OUTC, 'f', False, False, 2.4)],
  [L(outline([(60, 48), (76, 42), (70, 16), (48, 6), (22, 12), (6, 34), (6, 64), (24, 72), (42, 62)])), bun(40, 4, 9),
   L([(84, 72), (76, 76), (84, 80)], OUTC, 'f', False, False, 2.4)],
  [L(outline([(6, 74), (6, 36), (20, 16), (50, 8), (80, 16), (94, 36), (94, 74), (50, 80)])), bun(50, 6, 9)])

# Stran Linemont: pelo celeste peinado hacia arriba y atrás en ondas con un mechón negro en medio; piel muy clara, ojos
# lilas con sombra morada, coloretes y boca pequeña
CYAN = _c('#6ad0e0')
C('stran-linemont', 'normal', P('#6ad0e0', '#fde6dc', iris='#a080c8', shade='#4aa8c0'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=93, hairline=[(6, 62), (14, 50), (30, 44), (50, 40), (70, 44), (86, 50), (94, 62)]),
  dome('front', top=-10, w=52, cy=42, n=7, amp=9, sweep=0.5, seed=55, sb=60) +
  [L(outline([(36, 44), (40, 24), (52, 8, 1), (52, 26), (46, 44)]), BLACK, 'b'), L(quad((26, 68), (36, 64), (46, 68)), PURP, 'f', False, False, 2.4),
   L(quad((54, 68), (64, 64), (74, 68)), PURP, 'f', False, False, 2.4), L(ell(22, 86, 5, 3), RED, 'f', False), L(ell(78, 86, 5, 3), RED, 'f', False)],
  dome('side', top=-10, w=50, cy=42, n=7, amp=9, sweep=0.5, seed=55, nape=78, fr=46) + [L(outline([(60, 14), (40, 2, 1), (50, 18)]), BLACK, 'b')],
  dome('back', top=-10, w=52, cy=42, n=7, amp=9, sweep=0.5, seed=55, nape=80))

# Stratos Merrill: pelo azul corto con la raya a un lado; cejas gruesas, gafas de sol grises de cristal claro y una sonrisa
# enorme de dientes
C('stratos-merrill', 'normal', P('#3a68a8', '#fbcca8', shade='#2a4e80'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=96, hairline=[(6, 62), (14, 50), (30, 44), (60, 40), (72, 46), (86, 50), (94, 62)]),
  dome('front', top=0, w=48, cy=44, sb=64) + shades('front', 76, _c('#a8c0d0')) + thick_brows(64, BLACK, 3.6, 14, -0.8, 13) +
  [L(quad((46, 96), (50, 102), (54, 96)), OUTC, 'f', False, False, 1.0)],
  dome('side', top=0, w=48, cy=44, nape=80, fr=48) + shades('side', 76, _c('#a8c0d0')),
  dome('back', top=0, w=48, cy=44, nape=82))

# Sylas Saxton: cara alargada; pelo azul pizarra peinado hacia atrás con mechones largos que le caen por delante de las
# orejas; gafas finas sin montura, cejas en arco enfadadas, ojos azules afilados y boca de dientes apretados
C('sylas-saxton', 'delgado', P('#4a5a88', '#fbe4c8', iris='#2a3a8a', shade='#36446a'),
  F(eyes='sharp', brows=False, mouth='grin', mouth_y=98, face_front=face(chin=110), face_side=face_side(chin=8),
    hairline=[(10, 64), (16, 46), (30, 34), (50, 30), (70, 34), (84, 46), (90, 64)]),
  dome('front', top=-2, w=46, cy=44, sb=72) +
  [L(outline([(14, 50), (10, 90, 1), (20, 72), (22, 50)]), 'mid', 'f'), L(outline([(86, 50), (90, 90, 1), (80, 72), (78, 50)]), 'mid', 'f'),
   L(quad((24, 66), (34, 58), (44, 68)), OUTC, 'f', False, False, 2.4), L(quad((56, 68), (66, 58), (76, 66)), OUTC, 'f', False, False, 2.4),
   L(blob([(24, 72), (44, 72), (44, 82), (24, 82)], 3) + [(24, 72)], GRAY, 'f', False, False, 1.2),
   L(blob([(56, 72), (76, 72), (76, 82), (56, 82)], 3) + [(56, 72)], GRAY, 'f', False, False, 1.2)],
  dome('side', top=-2, w=46, cy=44, nape=82, fr=40) + [L([(74, 72), (88, 72), (88, 82), (74, 82), (74, 72)], GRAY, 'f', False, False, 1.2)],
  dome('back', top=-2, w=46, cy=44, nape=84))

# Talken Bigby: pelo rubio oscuro revuelto con una estrella negra dibujada y un mechón que le tapa un ojo; cara ancha morena y
# sonrisa de pillo
C('talken-bigby', 'normal', P('#a8944a', '#c08860', iris='#2a2020', shade='#867432'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=96, ear_out=4, face_front=face(w=6, chin=104, jaw=6), face_side=face_side(chin=4, jaw=5),
    hairline=[(6, 68), (14, 54), (30, 48), (50, 50), (70, 48), (86, 54), (94, 68)]),
  dome('front', top=-6, w=52, cy=46, n=8, amp=10, sweep=0.3, seed=57, sb=84) +
  [fr([(20, 46), (40, 40), (48, 50), (44, 70), (36, 84, 1), (30, 68), (20, 60)]),
   L(outline([(66, 18), (70, 8, 1), (73, 18), (82, 20, 1), (74, 24), (76, 34, 1), (69, 27), (61, 32, 1), (64, 24), (56, 20, 1)]), BLACK, 'b')],
  dome('side', top=-6, w=50, cy=46, n=8, amp=10, sweep=0.3, seed=57, nape=86, fr=56),
  dome('back', top=-6, w=52, cy=46, n=8, amp=10, sweep=0.3, seed=57, nape=88))

# Tally McIntosh: media melena lila azulado en casco con flequillo recto; gafas protectoras transparentes sobre los ojos
# naranjas con pestañas
CLR = (220, 230, 236, 140)
C('tally-mcintosh', 'chica', P('#8a98d0', '#fde6d8', iris='#e0902a', shade='#6a78b0'),
  F(eyes='big', brows=False, mouth='line', mouth_y=94, hairline=[(6, 70), (12, 62), (88, 62), (94, 70)]),
  bowl3('front', top=-2, side=96, nape=96, w=4, fringe=62) +
  [L(blob([(18, 66), (82, 66), (82, 86), (60, 88), (50, 82), (40, 88), (18, 86)], 4) + [(18, 66)], _c('#d0d8e0'), 'f', False, False, 2.0)],
  bowl3('side', top=-2, side=96, nape=96, w=4, fringe=60) + [L([(72, 66), (90, 66), (90, 86), (72, 86), (72, 66)], _c('#d0d8e0'), 'f', False, False, 2.0)],
  bowl3('back', top=-2, side=96, nape=96, w=4, fringe=62))

# Taxter Coilschmidt: pelo azul marino en seta redonda con rayas de peine; cejas azules gruesas, ojos verdes, coloretes y
# boca pequeña
C('taxter-coilschmidt', 'bajito', P('#3a4a78', '#fbd4b4', iris='#4a8a5a', shade='#2a365a'),
  F(eyes='normal', brows=False, mouth='frown', mouth_y=92, hairline=[(6, 62), (12, 56), (88, 56), (94, 62)]),
  bowl3('front', top=0, side=60, nape=74, w=4, fringe=56) + [L([(x, 12 if abs(x - 50) < 20 else 22), (x, 54)], 'shade', 'b', False, False, 1.0) for x in (24, 36, 50, 64, 76)] +
  thick_brows(64, _c('#2a3a8a'), 4.0, 14, 0.6, 12) + [L(ell(22, 86, 5, 3), RED, 'f', False), L(ell(78, 86, 5, 3), RED, 'f', False)],
  bowl3('side', top=0, side=60, nape=74, w=4, fringe=54) + side_brow(64, _c('#2a3a8a'), 4.0, 0.6),
  bowl3('back', top=0, side=60, nape=74, w=4, fringe=56))

# Teagan Leafhart: grandullón de cara ancha con el pelo naranja rizado y abultado; cejas naranjas gruesas, ojos amarillos
# entornados y una sonrisa ondulada como un bigote
C('teagan-leafhart', 'corpulento', P('#f0902a', '#f8b888', iris='#c8a82a', shade='#c86a1a'),
  F(eyes='sharp', brows=False, mouth='none', ear_out=8, face_front=face(w=10, chin=106, jaw=10, top=34), face_side=face_side(chin=4, jaw=8),
    hairline=[(4, 62), (14, 50), (30, 46), (50, 48), (70, 46), (86, 50), (96, 62)]),
  dome('front', top=0, w=58, cy=48, n=12, amp=7, soft=True, seed=59, sb=78) + thick_brows(66, 'mid', 5.0, 15, 0.8, 15) +
  [L(quad((36, 94), (43, 98), (50, 94)) + quad((50, 94), (57, 98), (64, 94))[1:], OUTC, 'f', False, False, 1.6)],
  dome('side', top=0, w=54, cy=48, n=12, amp=7, soft=True, seed=59, nape=84, fr=54) + side_brow(66, 'mid', 5.0, 0.8),
  dome('back', top=0, w=58, cy=48, n=12, amp=7, soft=True, seed=59, nape=86))

# Tempest Liebkind: pelo azul celeste desgreñado en capas que le tapa la frente, con un mechoncito arriba; ojos pequeños de
# sueño y boca de gato
C('tempest-liebkind', 'chica', P('#a0bcd8', '#fbe0cc', iris='#2a2a30', shade='#7a98b8', light='#c4d8ec'),
  F(eyes='dot', brows=False, mouth='none', eye_y=78, hairline=hl(7, 72, 56, 66, jit=3, seed=61)),
  [bun(50, -2, 6)] + dome('front', top=-2, w=54, cy=48, n=9, amp=7, soft=True, seed=61, long=98, flare=8, ends=4) + _catmouth(93),
  [bun(46, -2, 6)] + dome('side', top=-2, w=52, cy=48, n=9, amp=7, soft=True, seed=61, long=98, flare=8, fr=64),
  [bun(50, -2, 6)] + dome('back', top=-2, w=54, cy=48, n=9, amp=7, soft=True, seed=61, long=98, flare=8, ends=4))

# Tendance Chausefutt: pelo verde oliva claro en pinchos revueltos con una cinta negra fina; piel clara, ojos afilados de
# enfado con marcas en las mejillas y boca apretada
C('tendance-chausefutt', 'normal', P('#c0b04a', '#fde0c4', iris='#4a4a58', shade='#9a8a32'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=[(6, 62), (14, 50), (30, 44), (50, 42), (70, 44), (86, 50), (94, 62)]),
  dome('front', top=-12, w=52, cy=44, n=11, amp=10, seed=63, sb=62) +
  [L(quad((10, 40), (50, 4), (90, 40)), BLACK, 'f', False, False, 2.4), L([(22, 82), (28, 86)], OUTC, 'f', False, False, 1.2), L([(78, 82), (72, 86)], OUTC, 'f', False, False, 1.2)],
  dome('side', top=-12, w=50, cy=44, n=11, amp=10, seed=63, nape=80, fr=48) + [L(quad((84, 40), (60, 0), (20, 14)), BLACK, 'f', False, False, 2.4)],
  dome('back', top=-12, w=52, cy=44, n=11, amp=10, seed=63, nape=82) + [L(quad((8, 42), (50, 6), (92, 42)), BLACK, 'f', False, False, 2.4)])

# Tenison Onsera: pelo gris corto con la frente muy despejada; gafas redondas enormes, ojos muy abiertos de susto con la
# pupila pequeña, cejas grises y boca abierta con los dientes de delante
C('tenison-onsera', 'normal', P('#8a8a8a', '#fbd8c4', iris='#4a9ab0', shade='#6a6a6a'),
  F(eyes='round', brows=False, mouth='buck', mouth_y=96, ear_out=2, hairline=[(8, 58), (14, 40), (30, 28), (50, 24), (70, 28), (86, 40), (92, 58)]),
  dome('front', top=2, w=46, cy=44, n=5, amp=4, soft=True, seed=65, sb=70) + round_specs('front', BLACK, 76, 16, 12, 11, 2.6) +
  [L(quad((26, 62), (34, 58), (42, 62)), 'mid', 'f', False, False, 2.6), L(quad((58, 62), (66, 58), (74, 62)), 'mid', 'f', False, False, 2.6)],
  dome('side', top=2, w=46, cy=44, n=5, amp=4, soft=True, seed=65, nape=80, fr=30) + round_specs('side', BLACK, 76, 16, 12, 11, 2.6),
  dome('back', top=2, w=46, cy=44, n=5, amp=4, soft=True, seed=65, nape=82))
