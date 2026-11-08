"""Ojeadores de GO (scouts-go), tanda 01: dibujados a partir de su retrato de Victory Road; claves 'scouts-go:<id>'.

Ninguno de la tanda tiene modelo 3D: el frente sale del retrato y el perfil y la espalda se deducen de cómo cae ese
peinado. El sexo (y con él el cuerpo 'chica') viene de su ficha de la wiki. Se usan las ayudas de los ojeadores de IE
(dome/hl/face de ie1_09, bowl3/hood/ring/skull3 de ie3_02, cap/band de ie3_06, round_glasses de ie2_03...)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401
from chars_scouts_ie1_09 import dome, face, face_side, hl, mark, side_x  # noqa: F401
from chars_scouts_ie1_03 import fr, thick_brows, side_brow, blush, big_grin, stache  # noqa: F401
from chars_scouts_ie3_02 import ring, skull3, hood, bowl3, scarf, side_lock  # noqa: F401
from chars_scouts_ie3_06 import arc, cap, band  # noqa: F401
from chars_scouts_ie2_03 import round_glasses, ears_pointy  # noqa: F401
from chars_scouts_ie1_10 import nose_tri, squint  # noqa: F401
from chars_scouts_ie2_04 import sharp_eyes, sharp_eye_side  # noqa: F401

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
        f['hairline'] = [(min(xs) + 0.6, 104)] + [p[:2] for p in hl_[1:-1]] + [(max(xs) - 0.6, 104)]
    CHARS[f'scouts-go:{pid}'] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def D(top=-2, w=46, cy=44, n=0, amp=10, sweep=0.0, seed=1, sb=64, nape=86, fr_=46, **k):
    """El mismo dome en las tres vistas."""
    return (dome('front', top=top, w=w, cy=cy, n=n, amp=amp, sweep=sweep, seed=seed, sb=sb, **k),
            dome('side', top=top, w=w, cy=cy, n=n, amp=amp, sweep=sweep, seed=seed, nape=nape, fr=fr_, **k),
            dome('back', top=top, w=w, cy=cy, n=n, amp=amp, sweep=sweep, seed=seed, nape=nape, **k))


def lid_eyes(ey=75, sep=14, c=BLACK):
    """Ojos de párpado caído (medio cerrados, aburridos)."""
    out = []
    for cx in (50 - sep, 50 + sep):
        out += [L(blob([(cx - 7, ey), (cx, ey - 2), (cx + 7, ey), (cx + 6, ey + 5), (cx, ey + 6), (cx - 6, ey + 5)], 4), WHITE, 'f', False),
                L(ell(cx, ey + 3, 2.6, 2.6), c, 'f', False), L([(cx - 8, ey), (cx, ey - 2.4), (cx + 8, ey)], c, 'f', False, False, 2.4)]
    return out


# ------------------------------------------------------------------ jugadores

# Aaron Newgate: pelo corto castaño oscuro en pinchos de punta revueltos; ojos redondos negros y sonrisa
f, s, b = D(top=-6, w=46, cy=44, n=9, amp=11, seed=3, sb=64, nape=84)
C('aaron-newgate', 'normal', P('#55513d', '#fcd08c'),
  F(eyes='round', brows=True, mouth='smile', mouth_y=93, hairline=hl(6, 64, 48, 56, jit=2, seed=4)), f, s, b)

# Abby de Valera: pelo gris azulado en pinchos largos hacia fuera, un mechón de punta que baja por el centro de la frente;
# ojos verdes afilados y ceño
f, s, b = D(top=-10, w=50, cy=46, n=9, amp=16, sweep=0.2, seed=5, sb=74, nape=88, flare=8)
C('abby-de-valera', 'chica', P('#4f7177', '#f4d6a0', iris='#3a8a50'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=hl(5, 66, 50, 58, jit=3, seed=2)),
  f + [fr([(44, 46), (56, 46), (52, 66), (49, 76, 1), (47, 64)])], s, b)

# Abel Bumpkin (portero): cara de mono morena con la boca ancha de dientes apretados y la nariz roja; casquete de pelo
# gris azulado oscuro con la frente al aire en forma de arco
C('abel-bumpkin', 'corpulento', P('#3a4850', '#b38864', iris='#5a7a7a', muzzle='#c8a07a'),
  F(eyes='sharp', brows=False, mouth='none', hairline=False, face_front=face(w=4, chin=104, jaw=2), nose=(50, 84, 5)),
  [L(outline([(12, 62), (8, 36), (24, 14), (50, 8), (76, 14), (92, 36), (88, 62), (80, 48), (66, 40), (50, 48), (34, 40), (20, 48)]), 'mid', 'f')] +
  [L(blob([(26, 84), (50, 80), (74, 84), (76, 100), (50, 108), (24, 100)], 6), 'muzzle', 'f', False),
   L(blob([(34, 90), (50, 88), (66, 90), (64, 100), (50, 102), (36, 100)], 6), WHITE, 'f', False),
   L([(36, 95), (64, 95)], OUTC, 'f', False, False, 1.2), L(ell(50, 84, 6, 4), _c('#d86a5a'), 'f', False)],
  [L(outline([(54, 56), (60, 42), (80, 38), (86, 24), (66, 8), (36, 6), (12, 20), (4, 44), (8, 64), (24, 72), (44, 64)]))],
  [L(outline([(10, 80), (8, 40), (24, 14), (50, 8), (76, 14), (92, 40), (90, 80), (50, 88)]))])

# Ada Vyper: melena azul marino ondulada con dos grandes asas enroscadas arriba y un mechón ondulado que cruza la cara
# hasta el hombro; ojos rojos grandes
NV = '#37446e'
def _loops(view):
    if view == 'front':
        return [L(outline([(30, 14), (14, -14), (-6, -8), (-4, 10), (12, 8), (18, -2), (26, 4)]), 'mid', 'b'),
                L(outline([(70, 14), (86, -14), (106, -8), (104, 10), (88, 8), (82, -2), (74, 4)]), 'mid', 'b')]
    if view == 'side':
        return [L(outline([(40, 8), (28, -16), (6, -12), (8, 6), (22, 4), (28, -4), (34, 4)]), 'mid', 'b')]
    return [L(outline([(30, 14), (14, -14), (-6, -8), (-4, 10), (12, 8), (18, -2), (26, 4)]), 'mid', 'b'),
            L(outline([(70, 14), (86, -14), (106, -8), (104, 10), (88, 8), (82, -2), (74, 4)]), 'mid', 'b')]
f, s, b = D(top=0, w=46, cy=46, sb=80, nape=96, long=104, flare=8, ends=4)
C('ada-vyper', 'chica', P(NV, '#f0caa9', iris='#c0303a'),
  F(eyes='big', brows=True, mouth='frown', mouth_y=95, hairline=[(8, 66), (20, 50), (36, 46), (50, 52), (64, 46), (80, 50), (92, 66)]),
  _loops('front') + f + [fr([(40, 46), (52, 48), (48, 64), (56, 80), (48, 96), (56, 112), (46, 118, 1), (40, 104), (46, 90), (38, 76), (42, 62)])],
  _loops('side') + s, _loops('back') + b)

# Adam Orable: pelo celeste muy claro echado a un lado en un flequillo largo que tapa un ojo, con mechones que caen por
# la nuca; ojos azul oscuro y media sonrisa
f, s, b = D(top=2, w=47, cy=46, n=6, amp=6, sweep=0.6, seed=8, sb=78, nape=94, soft=True)
C('adam-orable', 'normal', P('#c4f3fc', '#f8bc7d', iris='#3a4a8a'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=94, hairline=[(8, 66), (20, 50), (36, 46), (50, 50), (64, 46), (80, 50), (92, 66)]),
  f + [fr([(28, 44), (62, 42), (82, 52), (74, 58), (60, 54), (44, 70, 1), (40, 56), (26, 62, 1)])], s, b)

# Adi "Gecko" Sivfeet: cabeza de gecko naranja con dos ojos amarillos saltones a los lados como gafas, una franja verde por
# encima y ojos caídos de sueño; boca ancha
GK, GY = _c('#94af74'), _c('#dac63b')
def _gecko(view):
    if view == 'front':
        return [L(blob([(8, 64), (8, 40), (26, 22), (50, 18), (74, 22), (92, 40), (92, 64)], 6), 'skin', 'b'),
                L(quad((22, 34), (50, 18), (78, 34)) + quad((76, 42), (50, 28), (24, 42)), GK, 'f', True, True),
                L(ell(14, 54, 12, 11), GY, 'f'), L(ell(14, 54, 6, 6), _c('#2a3020'), 'f', False),
                L(ell(86, 54, 12, 11), GY, 'f'), L(ell(86, 54, 6, 6), _c('#2a3020'), 'f', False),
                strand([(30, 48), (34, 60), (30, 70)], GK, 'f', 2.6), strand([(70, 48), (66, 60), (70, 70)], GK, 'f', 2.6)]
    if view == 'side':
        return [L(blob([(10, 66), (6, 36), (26, 18), (60, 14), (86, 28), (90, 48), (60, 46), (40, 60)], 6), 'skin', 'b'),
                L(quad((20, 30), (50, 14), (84, 30)) + quad((82, 38), (50, 22), (22, 38)), GK, 'f', True, True),
                L(ell(66, 46, 11, 11), GY, 'f'), L(ell(68, 46, 5, 5), _c('#2a3020'), 'f', False)]
    return [L(blob([(8, 80), (8, 40), (26, 20), (50, 16), (74, 20), (92, 40), (92, 80), (50, 86)], 6), 'skin', 'b'),
            L(quad((22, 34), (50, 16), (78, 34)) + quad((76, 42), (50, 26), (24, 42)), GK, 'f', True, True),
            L(ell(10, 54, 10, 10), GY, 'f'), L(ell(90, 54, 10, 10), GY, 'f')]
C('adi-gecko-sivfeet', 'normal', P('#94af74', '#fbc271'),
  F(eyes='none', brows=False, mouth='line', mouth_y=96, mouth_w=14, hairline=False, ears=False),
  _gecko('front') + lid_eyes(76, 16) + [L([(32, 96), (68, 96)], OUTC, 'f', False, False, 1.6)], _gecko('side'), _gecko('back'))

# Al Overa: grandullón de cara redonda y pálida con pelo corto ondulado verde grisáceo, gafas redondas enormes de cristal
# claro, ojos cerrados y labios fruncidos
f, s, b = D(top=8, w=42, cy=44, n=8, amp=4, soft=True, seed=2, sb=58, nape=82)
C('al-overa', 'corpulento', P('#556e68', '#e1cbad'),
  F(eyes='closed', brows=False, mouth='none', hairline=[(10, 60), (22, 46), (36, 42), (50, 44), (64, 42), (78, 46), (90, 60)],
    face_front=face(w=5, chin=104, jaw=3), nose=(50, 86, 3)),
  f + round_glasses('front', _c('#e8e8e4'), y=76, sep=16, r=10, w=2.2) +
  [L(ell(50, 94, 4, 3), _c('#a87060'), 'f', False), L(quad((44, 102), (50, 106), (58, 101)), OUTC, 'f', False, False, 1.0)],
  s + round_glasses('side', _c('#e8e8e4'), y=76, r=10), b)

# Alan McCallum: pelo blanco lila corto y recto con flequillo en mechones; ojos afilados verdosos con ceño y boca recta
f, s, b = D(top=0, w=46, cy=46, n=7, amp=7, seed=6, sb=72, nape=88)
C('alan-mccallum', 'normal', P('#e8e2f0', '#f9bb7d', iris='#8a8a4a', shade='#bfc5cf'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=hl(7, 66, 50, 60, jit=2, seed=1)), f, s, b)

# Alben Moretti: gorro enorme amarillo de dos picos como orejas con una franja azul en el centro y el borde crema que le tapa
# los ojos; boca torcida
YL, BL, CRM = _c('#fbe349'), _c('#37497f'), _c('#e7ebd9')
def _hat(view):
    return [dict(l, z='f') for l in _hat0(view)]


def _hat0(view):
    if view == 'front':
        return [L(outline([(2, 60), (-4, 28), (-2, 0, 1), (24, 14), (50, 12), (76, 14), (102, 0, 1), (104, 28), (98, 60)]), YL),
                L(outline([(40, 13), (60, 13), (64, 58), (36, 58)]), BL, 'f', False),
                L(blob([(2, 56), (50, 60), (98, 56), (96, 72), (50, 78), (4, 72)], 6), CRM, 'f')]
    if view == 'side':
        return [L(outline([(6, 66), (0, 30), (8, -2, 1), (40, 10), (80, 14), (96, 40), (98, 62), (50, 64)]), YL),
                L(outline([(30, 12), (48, 12), (46, 64), (30, 64)]), BL, 'f', False),
                L(blob([(4, 62), (50, 62), (100, 58), (100, 74), (50, 78), (4, 76)], 6), CRM, 'f')]
    return [L(outline([(2, 64), (-4, 28), (-2, 0, 1), (24, 14), (50, 12), (76, 14), (102, 0, 1), (104, 28), (98, 64)]), YL),
            L(outline([(40, 13), (60, 13), (64, 62), (36, 62)]), BL, 'f', False),
            L(blob([(2, 60), (50, 64), (98, 60), (96, 76), (50, 80), (4, 76)], 6), CRM, 'f')]
C('alben-moretti', 'normal', P('#5a3a2a', '#f4bc7d'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, hairline=False, ears=False),
  _hat('front'), _hat('side'), _hat('back'))

# Alex "Prof" Gottlieb: pelo naranja rojizo en pinchos largos hacia fuera y una máscara gris con cuatro lentes naranjas
# redondas en la cara; sonrisa
GR_, ORL = _c('#706253'), _c('#e49242')
f, s, b = D(top=-12, w=50, cy=44, n=9, amp=16, seed=11, sb=70, nape=88)
C('alex-prof-gottlieb', 'normal', P('#b84110', '#e49242'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=96, hairline=hl(6, 62, 48, 56, jit=3, seed=3)),
  f + [L(blob([(14, 60), (50, 56), (86, 60), (88, 82), (66, 88), (50, 84), (34, 88), (12, 82)], 6), GR_, 'f'),
       L(ell(39, 64, 5, 5), ORL, 'f'), L(ell(61, 64, 5, 5), ORL, 'f'), L(ell(30, 77, 7.5, 7.5), ORL, 'f'), L(ell(70, 77, 7.5, 7.5), ORL, 'f')],
  s + [L(blob([(66, 58), (90, 60), (92, 84), (70, 86)], 6), GR_, 'f'), L(ell(84, 76, 5, 7), ORL, 'f')], b)

# Algo Rithm: cabeza entera cubierta por una capucha negra de tela ajustada, con unas gafas verdes de lentes rojas
DK, GG, RL = _c('#4e4d4b'), _c('#688f7f'), _c('#c05040')
def _algo(view):
    if view == 'front':
        return [L(blob([(14, 100), (10, 50), (20, 16), (50, 4), (80, 16), (90, 50), (86, 100), (50, 110)], 8), DK, 'f'),
                L(blob([(16, 66), (50, 62), (84, 66), (84, 84), (50, 80), (16, 84)], 6), GG, 'f'),
                L(ell(32, 74, 7, 6), RL, 'f'), L(ell(68, 74, 7, 6), RL, 'f'), L(ell(50, 96, 2, 1.4), _c('#1e1e1e'), 'f', False)]
    if view == 'side':
        return [L(blob([(30, 104), (10, 70), (8, 34), (28, 8), (60, 4), (84, 22), (90, 56), (90, 94), (70, 106)], 8), DK, 'f'),
                L(blob([(70, 66), (94, 64), (94, 84), (72, 84)], 6), GG, 'f'), L(ell(86, 74, 5, 6), RL, 'f')]
    return [L(blob([(14, 100), (10, 50), (20, 16), (50, 4), (80, 16), (90, 50), (86, 100), (50, 110)], 8), DK, 'f'),
            L([(6, 72), (94, 72), (94, 78), (6, 78)], GG, 'f', False)]
C('algo-rithm', 'normal', P('#4e4d4b', '#a25544'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False), _algo('front'), _algo('side'), _algo('back'))

# Alicia Odde: melena larga rubio ceniza lisa hasta el pecho con un lazo blanco enorme arriba y una horquilla rosa en forma
# de cruz; ojos grandes lilas y rubor
WB, PKX = _c('#fafafa'), _c('#f08a9a')
def _bow(y=-2):
    return [L(outline([(50, y + 10), (30, y - 4), (22, y + 4), (26, y + 18), (50, y + 12), (74, y + 18), (78, y + 4), (70, y - 4)]), WB, 'f'),
            L(ell(50, y + 10, 5, 5), WB, 'f')]
f, s, b = D(top=2, w=46, cy=46, sb=80, nape=96, long=112, flare=6, ends=5)
C('alicia-odde', 'chica', P('#d4bf94', '#fcedd3', iris='#7a5a7a'),
  F(eyes='big', brows=True, mouth='frown', mouth_y=95, hairline=[(8, 66), (18, 50), (34, 44), (50, 50), (66, 44), (82, 50), (92, 66)]),
  f + _bow(2) + blush(86, 22, 4) + [L(blob([(14, 52), (20, 46), (26, 52), (20, 58)], 4), PKX, 'f'), L(blob([(10, 56), (30, 50), (28, 56), (12, 60)], 4), PKX, 'f')],
  s + [L(outline([(40, 8), (24, -4), (14, 6), (22, 16), (44, 12)]), WB, 'f')], b + _bow(2))

# Alma Verchu: melena azul marino oscuro hasta los hombros con una diadema blanca y un mechón por la frente; ojos verdes
# grandes y sonrisa
f, s, b = D(top=2, w=46, cy=46, sb=82, nape=96, long=104, flare=6, ends=4)
C('alma-verchu', 'chica', P('#303062', '#fbeaba', iris='#3a9a5a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=94, hairline=[(8, 66), (18, 50), (34, 46), (44, 60), (52, 46), (66, 46), (82, 50), (92, 66)]),
  f + [band('front', WB, y=24, h=6, w=40, dip=10)], s + [band('side', WB, y=16, h=6)], b + [band('back', WB, y=22, h=6, w=40)])

# Amanda Jurr: melena granate en casco con flequillo recto que tapa las cejas y dos moños enroscados como cuernos; ojos
# azules redondos, pecas y boca en O
def _buns(view):
    if view == 'side':
        return [L(ell(40, 6, 12, 11), 'mid', 'b'), strand([(34, 4), (40, 0), (46, 6), (40, 12)], 'deep', 'b', 1.0)]
    out = []
    for cx in (24, 76):
        out += [L(ell(cx, 8, 13, 12), 'mid', 'b'), strand([(cx - 6, 6), (cx, 0), (cx + 6, 6), (cx, 12)], 'deep', 'b', 1.0)]
    return out
C('amanda-jurr', 'chica', P('#a32041', '#f4edcd', iris='#6aa0c8'),
  F(eyes='round', brows=False, mouth='none', hairline=[(8, 66), (92, 66)], eye_y=78, ears=False),
  _buns('front') + bowl3('front', top=6, side=104, fringe=66) +
  [L(ell(50, 96, 2.4, 3), _c('#7a3030'), 'f', False)] + [L(ell(x, 88, 0.9, 0.9), _c('#7a5040'), 'f', False) for x in (26, 30, 70, 74)],
  _buns('side') + bowl3('side', top=6, nape=100, fringe=64), _buns('back') + bowl3('back', top=6, nape=100))

# Ambrose "Amber" Ericson (portero): pelo naranja en llamas altísimas hacia arriba con franjas melocotón; cejas y ojos
# naranjas en V, nariz larga y boca torcida
f = [L(outline([(16, 60), (8, 30), (2, -16, 1), (20, 6), (30, -30, 1), (40, 4), (50, -36, 1), (60, 4), (70, -30, 1), (80, 6), (98, -16, 1), (92, 30), (84, 60),
                (78, 48), (22, 48)])),
     L(outline([(28, 0), (32, -22, 1), (38, 2)]), 'light', 'b', False), L(outline([(58, 0), (64, -22, 1), (68, 2)]), 'light', 'b', False)]
s = [L(outline([(56, 52), (64, 40), (82, 34), (92, 0, 1), (72, 14), (64, -30, 1), (50, 6), (34, -26, 1), (26, 8), (8, -8, 1), (8, 24), (4, 48), (20, 60), (44, 56)]))]
b = [L(outline([(14, 70), (8, 30), (2, -16, 1), (20, 6), (30, -30, 1), (40, 4), (50, -36, 1), (60, 4), (70, -30, 1), (80, 6), (98, -16, 1), (92, 30), (86, 70),
                (50, 76)]))]
C('ambrose-amber-ericson', 'normal', P('#f86c28', '#fccc95', iris='#c85a20', light='#fcc0a0'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=97, hairline=[(14, 58), (30, 50), (50, 54), (70, 50), (86, 58)], nose=(50, 86, 3),
    face_front=face(chin=104)), f, s, b)

# Amelio "Amethyst" Thyst: tupé morado alto y peinado a un lado con mechas rosas, cara larga pálida con unas florituras negras
# pintadas sobre los ojos; sonrisa
f, s, b = D(top=-12, w=40, cy=40, sb=58, nape=78, sweep=0.0)
C('amelio-amethyst-thyst', 'delgado', P('#955aa6', '#e3cbae', iris='#4a2a3a', light='#d070c8'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=98, hairline=[(14, 60), (24, 44), (40, 38), (60, 36), (76, 42), (86, 60)],
    face_front=face(chin=108), face_side=face_side(chin=6)),
  f + [L(outline([(30, -8), (50, -14), (72, -4), (78, 20), (60, 6), (44, 20)]), 'light', 'f', False),
       L(quad((26, 70), (34, 60), (42, 66)), OUTC, 'f', False, False, 1.8), L(quad((74, 70), (66, 60), (58, 66)), OUTC, 'f', False, False, 1.8)],
  s, b)

# Amy Sargent: media melena castaña con raya en medio, que cae lisa por los lados hasta la mandíbula; ojos castaños y
# sonrisa
f, s, b = D(top=2, w=46, cy=46, sb=92, nape=92)
C('amy-sargent', 'chica', P('#6c544e', '#f8bc7e', iris='#6a4a3a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=94, hairline=[(8, 66), (18, 52), (32, 46), (48, 48), (50, 52), (52, 48), (68, 46), (82, 52), (92, 66)]),
  f + [strand([(50, 8), (50, 40)], 'deep', 'b', 1.0)], s, b)

# Andy Kareem: cara cuadrada y ancha con un gorro como una maceta naranja del revés y la cinta gris; ojos turquesa con
# pestañas gruesas y boca enorme en arco hacia abajo
POT, PBD = _c('#d19435'), _c('#9a9088')
def _pot(view):
    if view == 'front':
        return [L([(14, 50), (20, -2), (80, -2), (86, 50)], POT, 'f'), L([(13, 50), (87, 50), (87, 58), (13, 58)], PBD, 'f'),
                L([(66, -1), (80, -2), (86, 50), (72, 50)], _c('#a8742a'), 'f', False)]
    if view == 'side':
        return [L([(10, 52), (20, 0), (78, 0), (90, 46)], POT, 'f'), L([(9, 52), (91, 46), (91, 54), (9, 60)], PBD, 'f')]
    return [L([(14, 52), (20, -2), (80, -2), (86, 52)], POT, 'f'), L([(13, 52), (87, 52), (87, 60), (13, 60)], PBD, 'f')]
C('andy-kareem', 'corpulento', P('#27221c', '#fdeab8', iris='#3a8a8a'),
  F(eyes='round', brows='angry', mouth='none', hairline=False, face_front=blob([(14, 50), (86, 50), (88, 92), (76, 106), (24, 106), (12, 92)], 6)),
  _pot('front') + [L(quad((36, 104), (50, 88), (64, 104)), OUTC, 'f', False, False, 2.2), L(quad((24, 72), (30, 66), (44, 70)), OUTC, 'f', False, False, 2.0),
                   L(quad((76, 72), (70, 66), (56, 70)), OUTC, 'f', False, False, 2.0)],
  _pot('side'), _pot('back'))

# Anne Sestral: media melena blanca azulada en casco, con flequillo recto que roza las cejas y las puntas abiertas; piel
# morena, ojos negros y sonrisa con la boca abierta
C('anne-sestral', 'chica', P('#dafafe', '#cd9569', iris='#2a2020', shade='#a9b6c0'),
  F(eyes='big', brows=False, mouth='grin', mouth_y=94, hairline=[(8, 62), (92, 62)], ears=False),
  bowl3('front', top=2, side=100, w=8, fringe=62), bowl3('side', top=2, nape=100, w=6, fringe=60), bowl3('back', top=2, nape=100, w=8))

# Anne Tenney: dos coletas largas azul marino a los lados con dos pinzas rosas arriba, flequillo en mechones; cara ancha
# muy pálida, ojos negros grandes y boca de gato con un colmillo
PNK = _c('#ce7e82')
def _tails(view):
    if view == 'side':
        return [L(outline([(20, 18), (6, 40), (2, 80), (10, 112), (16, 84), (22, 50), (30, 26)]), 'mid', 'b'),
                L(outline([(24, 6), (34, 12), (30, 24), (20, 18)]), PNK, 'f')]
    return [L(outline([(24, 14), (6, 30), (-2, 70), (4, 112, 1), (12, 80), (16, 44), (28, 26)]), 'mid', 'b'),
            L(outline([(76, 14), (94, 30), (102, 70), (96, 112, 1), (88, 80), (84, 44), (72, 26)]), 'mid', 'b'),
            L(outline([(24, 2), (34, 8), (30, 22), (20, 16)]), PNK, 'f'), L(outline([(76, 2), (66, 8), (70, 22), (80, 16)]), PNK, 'f')]
f, s, b = D(top=4, w=44, cy=46, n=6, amp=6, seed=3, sb=70, nape=86)
C('anne-tenney', 'chica', P('#3b4d64', '#f3edce', iris='#141416'),
  F(eyes='big', brows=True, mouth='none', hairline=hl(5, 64, 50, 60, seed=3), face_front=face(w=4, chin=102)),
  _tails('front') + f + [L(quad((40, 94), (45, 98), (50, 94)) + quad((50, 94), (55, 98), (60, 94))[1:], OUTC, 'f', False, False, 1.4),
                         L([(52, 96), (54, 100), (56, 96)], WHITE, 'f', False)],
  _tails('side') + s, _tails('back') + b)

# Anthea Tussore: melena rubia muy clara ondulada en bucles hasta la barbilla con un gran rizo encima de la frente y dos
# cuernos rojos de carnero a los lados; ojos granates grandes
HRN = _c('#c03a3a')
def _ram(view):
    if view == 'side':
        return [L(outline([(40, 74), (28, 60), (30, 44), (44, 44), (50, 60)]), HRN, 'f')]
    return [L(outline([(14, 56), (0, 42), (2, 26), (14, 26), (20, 40)]), HRN, 'f'), L(outline([(86, 56), (100, 42), (98, 26), (86, 26), (80, 40)]), HRN, 'f')]
f = dome('front', top=0, w=48, cy=46, n=10, amp=6, soft=True, seed=4, long=96, flare=8, ends=4)
s = dome('side', top=0, w=48, cy=46, n=10, amp=6, soft=True, seed=4, long=94, fr=46)
b = dome('back', top=0, w=48, cy=46, n=10, amp=6, soft=True, seed=4, long=96, flare=8)
C('anthea-tussore', 'chica', P('#f9ef9e', '#fdecb7', iris='#7a2a30', shade='#e0c070'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=96, hairline=[(8, 66), (20, 50), (34, 50), (44, 40), (60, 38), (74, 46), (86, 52), (92, 66)]),
  f + [L(ell(46, 28, 11, 10), 'mid', 'f'), strand([(40, 28), (46, 22), (52, 28), (46, 34)], 'shade', 'f', 1.4)] + _ram('front'),
  s + _ram('side'), b + _ram('back'))

# Apnus Braithwaite (portero): pelo verde oliva oscuro en dos bultos enormes redondos arriba y patillas anchas; cara
# morena ancha con una franja oscura sobre los ojos fruncidos y labios gruesos
f = [L(outline([(10, 74), (6, 40), (8, 18), (28, 4), (48, 14), (52, 14), (72, 4), (92, 18), (94, 40), (90, 74), (82, 74), (80, 48), (20, 48), (18, 74)])),
     L(outline([(62, 8), (84, 10), (92, 36), (88, 70), (80, 44)]), 'shade', 'b', False)]
s = [L(outline([(54, 56), (62, 44), (80, 40), (90, 24), (76, 6), (54, 8), (30, 2), (10, 14), (2, 40), (6, 64), (24, 76), (44, 66)]))]
b = [L(outline([(10, 82), (6, 40), (8, 18), (28, 4), (48, 14), (52, 14), (72, 4), (92, 18), (94, 40), (90, 82), (50, 88)]))]
C('apnus-braithwaite', 'corpulento', P('#4c4833', '#eca663', iris='#202020'),
  F(eyes='sharp', brows=False, mouth='lips', mouth_y=96, mouth_w=10, hairline=False, face_front=face(w=4, chin=104, jaw=3)),
  f + [L(blob([(22, 70), (50, 66), (78, 70), (78, 76), (50, 74), (22, 76)], 4), _c('#3d3227'), 'f', False)], s, b)

# Apra Chabel: pelo verde muy oscuro con un flequillo grande echado a un lado que le tapa un ojo y una coleta baja a un
# lado con una cuenta turquesa; piel morena, ojo turquesa y sonrisa
TQ = _c('#4ab0a8')
f, s, b = D(top=2, w=46, cy=46, sb=78, nape=88)
C('apra-chabel', 'chica', P('#384341', '#b29172', iris='#40b0b0'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=94, hairline=[(8, 66), (20, 50), (34, 46), (50, 46), (66, 46), (80, 50), (92, 66)]),
  f + [fr([(20, 50), (40, 38), (66, 40), (84, 52), (82, 84, 1), (70, 64), (58, 58), (52, 64)]),
       L(outline([(18, 80), (12, 92), (4, 108), (10, 116, 1), (16, 104), (20, 94)]), 'mid', 'b'), L(ell(16, 84, 4, 4), TQ, 'f')],
  s + [L(outline([(24, 78), (16, 92), (10, 108), (16, 114, 1), (22, 100), (30, 86)]), 'mid', 'f'), L(ell(26, 80, 4, 4), TQ, 'f')], b)

# Archie Valry: yelmo de caballero plateado que le tapa toda la cabeza, con la ranura del visor oscura y un penacho rojo
# curvo que cae por detrás
SLV, PLM = _c('#d9d4d2'), _c('#c54739')
def _helm(view):
    if view == 'front':
        return [L(outline([(70, 6), (84, -18), (96, -14), (90, 4), (98, 40), (94, 60), (102, 80), (96, 96, 1), (84, 70), (80, 30)]), PLM, 'b'),
                L(outline([(12, 104), (8, 56), (14, 24), (30, 4), (50, -4, 1), (70, 4), (86, 24), (92, 56), (88, 104), (50, 112)]), SLV, 'f'),
                L(outline([(40, 54), (50, 46), (60, 54), (56, 96), (50, 100), (44, 96)]), _c('#2a2424'), 'f', False),
                L(outline([(60, 6), (86, 26), (90, 60), (86, 100), (70, 104), (70, 50)]), _c('#a9a0a0'), 'f', False)]
    if view == 'side':
        return [L(outline([(50, -2), (30, -14), (10, -6), (-8, 30), (-4, 70), (6, 96, 1), (8, 64), (14, 30), (30, 8)]), PLM, 'b'),
                L(outline([(14, 104), (6, 60), (12, 24), (36, 2), (62, 0), (86, 18), (96, 50), (94, 86), (80, 106), (50, 112)]), SLV, 'f'),
                L(outline([(86, 56), (96, 56), (96, 70), (86, 70)]), _c('#2a2424'), 'f', False)]
    return [L(outline([(12, 104), (8, 56), (14, 24), (30, 4), (50, -4, 1), (70, 4), (86, 24), (92, 56), (88, 104), (50, 112)]), SLV, 'f'),
            L(outline([(46, -2), (54, -2), (60, 60), (50, 104, 1), (40, 60)]), PLM, 'f')]
C('archie-valry', 'normal', P('#c54739', '#9a6a44'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False), _helm('front'), _helm('side'), _helm('back'))

# Armand Sedate: cabeza redonda y mofletuda casi calva, con una franja corta de pelo gris verdoso encima; ojos de punto,
# cejas cortas y gruesas y boca abierta sonriente
f = [L(blob([(18, 46), (24, 22), (50, 12), (76, 22), (82, 46), (70, 36), (50, 30), (30, 36)], 6))]
s = [L(blob([(30, 44), (26, 20), (50, 10), (76, 20), (84, 36), (60, 30)], 6))]
b = [L(blob([(14, 50), (22, 22), (50, 12), (78, 22), (86, 50), (50, 44)], 6))]
C('armand-sedate', 'corpulento', P('#5e7a7a', '#fabc7a'),
  F(eyes='dot', brows=False, mouth='grin', mouth_y=94, hairline=False, face_front=face(w=7, chin=104, jaw=4, top=10)),
  skull3('front') + f + thick_brows(68, 'mid', 3.0, 16, 0, 9),
  skull3('side') + s + side_brow(68, 'mid', 3.0), skull3('back') + b)

# Art Izan: media melena lisa color crema hasta la barbilla con un flequillo largo que le tapa medio rostro; piel morena,
# un ojo cerrado y boca recta
f, s, b = D(top=2, w=46, cy=46, sb=98, nape=96, long=None)
C('art-izan', 'normal', P('#f9f3e0', '#cc9468', shade='#d8c8b0'),
  F(eyes='closed', brows=False, mouth='line', mouth_y=96, hairline=[(8, 66), (20, 50), (36, 46), (50, 46), (64, 46), (80, 50), (92, 66)]),
  f + [fr([(36, 40), (70, 40), (84, 56), (84, 96), (66, 106, 1), (64, 76), (54, 54), (46, 70, 1), (40, 52)])], s, b)

# Art Turner (portero): pelo azul grisáceo claro corto y peinado hacia atrás con pico en la frente; piel pálida, ojos grises
# con pestañas abajo y boca pequeña
f, s, b = D(top=0, w=44, cy=44, n=5, amp=4, soft=True, sweep=-0.3, seed=2, sb=66, nape=86)
C('art-turner', 'normal', P('#acd0d7', '#fceab8', iris='#7a8090'),
  F(eyes='big', brows=True, mouth='line', mouth_y=95, mouth_w=6, hairline=[(10, 64), (22, 48), (36, 40), (50, 50), (64, 40), (78, 48), (90, 64)]), f, s, b)

# Ash Cagger: hombre de piel rojiza con un moño de samurái verde oliva atado con un cordón blanco, cejas enormes oscuras,
# una franja blanca pintada bajo los ojos como un bigote al revés, perilla oliva y ceño
f = [L(outline([(16, 58), (16, 40), (30, 30), (50, 28), (70, 30), (84, 40), (84, 58), (70, 46), (30, 46)])), L(ell(50, 8, 9, 8)),
     L(outline([(46, 12), (54, 12), (55, 30), (45, 30)]), WHITE, 'f')]
s = [L(outline([(44, 58), (30, 60), (16, 46), (20, 32), (44, 26), (70, 28), (84, 40), (62, 40)])), L(ell(44, 10, 8, 8)),
     L(outline([(40, 14), (48, 14), (49, 28), (41, 28)]), WHITE, 'f')]
b = [L(outline([(14, 72), (14, 40), (30, 28), (50, 26), (70, 28), (86, 40), (86, 72), (50, 76)])), L(ell(50, 8, 9, 8)),
     L(outline([(46, 12), (54, 12), (55, 28), (45, 28)]), WHITE, 'f')]
C('ash-cagger', 'corpulento', P('#414428', '#ca7150', iris='#d8c030'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=96, hairline=False, face_front=face(w=4, chin=106, jaw=2)),
  skull3('front') + f + thick_brows(64, 'mid', 6, 16, -1, 14) +
  [L(blob([(14, 82), (34, 78), (50, 86), (66, 78), (86, 82), (80, 88), (50, 92), (20, 88)], 4), WHITE, 'f', False),
   L(outline([(44, 100), (56, 100), (50, 112, 1)]), 'mid', 'f')],
  skull3('side') + s + side_brow(64, 'mid', 6) + [L(outline([(78, 100), (86, 100), (80, 110, 1)]), 'mid', 'f')], skull3('back') + b)

# Askel Blays: pelo naranja en pinchos de llama hacia arriba, piel tostada con una cicatriz en X sobre la nariz y arañazos,
# ojos azules afilados y ceño
f, s, b = D(top=-12, w=46, cy=44, n=7, amp=16, sweep=0.1, seed=12, sb=68, nape=86)
C('askel-blays', 'normal', P('#fc9a3d', '#ad8761', iris='#3a6aa0', shade='#d8702a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, hairline=hl(6, 62, 48, 58, jit=2, seed=6)),
  f + [L([(42, 76), (58, 90)], OUTC, 'f', False, False, 1.4), L([(58, 76), (42, 90)], OUTC, 'f', False, False, 1.4),
       L([(24, 88), (30, 92)], OUTC, 'f', False, False, 1.0), L([(26, 92), (32, 96)], OUTC, 'f', False, False, 1.0)], s, b)

# Av Antguard: melena azul lavanda ondulada hasta los hombros con mechones que cruzan la cara; piel pálida, ojos caídos y
# dientes apretados
f, s, b = D(top=0, w=48, cy=46, n=8, amp=5, soft=True, seed=9, long=104, flare=8, ends=4, nape=96)
C('av-antguard', 'delgado', P('#7584a4', '#e5d0b5', iris='#3a3a50'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=97, hairline=[(8, 66), (20, 50), (34, 44), (44, 56), (52, 44), (68, 46), (82, 50), (92, 66)],
    face_front=face(chin=106), face_side=face_side(chin=5)),
  f + lid_eyes(76, 14) + [fr([(42, 44), (50, 46), (44, 70), (38, 92, 1), (36, 66)]), fr([(60, 44), (68, 48), (72, 80), (66, 96, 1), (62, 70)])], s, b)

# Avery Rarecard: pinchos rojos echados hacia un lado con las puntas de atrás negras, unas gafas de aviador con un rayo
# amarillo en cada lente sobre la frente; ojos verdes y sonrisa
GLD, GLN, BND = _c('#c8a030'), _c('#2a2a30'), _c('#2a5a8a')
f, s, b = D(top=-8, w=48, cy=44, n=8, amp=14, sweep=0.5, seed=14, sb=70, nape=88)
C('avery-rarecard', 'normal', P('#b3342e', '#f8b87b', iris='#2a9a7a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=hl(6, 64, 50, 60, lean=3, jit=2, seed=5)),
  [L(outline([(6, 60), (-6, 50, 1), (6, 40), (-8, 30, 1), (8, 26)]), _c('#1e1a1a')), L(outline([(94, 60), (106, 50, 1), (94, 40), (108, 30, 1), (92, 26)]), _c('#1e1a1a'))] +
  f + [band('front', BND, y=34, h=5, w=44, dip=8), L(ell(34, 34, 9, 8), GLD, 'f'), L(ell(34, 34, 6, 5), GLN, 'f', False),
       L(ell(66, 34, 9, 8), GLD, 'f'), L(ell(66, 34, 6, 5), GLN, 'f', False),
       L([(36, 30), (32, 35), (36, 35), (32, 39)], YLW := _c('#f0d020'), 'f', False, False, 1.4), L([(68, 30), (64, 35), (68, 35), (64, 39)], YLW, 'f', False, False, 1.4)],
  s + [band('side', BND, y=26, h=5), L(ell(80, 30, 6, 8), GLD, 'f'), L(ell(81, 30, 4, 5), GLN, 'f', False)],
  b + [band('back', BND, y=30, h=5, w=46)])

# Axel Lottle: gorra plana gris verdosa, pelo rosa en mechones de punta que asoman por los lados, gafas redondas de sol
# rojas y cara ancha pálida con la boca recta
CAPG = _c('#657a78')
C('axel-lottle', 'corpulento', P('#d07a8a', '#fdf0d8'),
  F(eyes='none', brows=False, mouth='line', mouth_y=96, hairline=False, face_front=face(w=4, chin=104, jaw=2)),
  [L(outline([(16, 60), (-2, 50, 1), (12, 46), (-4, 36, 1), (16, 36)])), L(outline([(84, 60), (102, 50, 1), (88, 46), (104, 36, 1), (84, 36)])),
   L(blob([(10, 50), (12, 26), (30, 16), (50, 14), (70, 16), (88, 26), (90, 50), (50, 44)], 6), CAPG, 'f'),
   L(blob([(8, 44), (50, 40), (92, 44), (94, 54), (50, 52), (6, 54)], 4), _c('#4e605e'), 'f')] +
  [L(ell(38, 76, 7, 6), _c('#d02a2a'), 'f'), L(ell(62, 76, 7, 6), _c('#d02a2a'), 'f'), L([(45, 76), (55, 76)], OUTC, 'f', False, False, 1.4)],
  [L(outline([(40, 70), (28, 62, 1), (38, 58), (26, 50, 1), (42, 50)])),
   L(blob([(8, 54), (10, 26), (34, 12), (60, 12), (82, 22), (90, 40), (104, 46), (104, 52), (60, 50), (30, 58)], 6), CAPG, 'f'),
   L(ell(86, 76, 4, 6), _c('#d02a2a'), 'f')],
  [L(outline([(16, 72), (0, 62, 1), (14, 56), (-2, 46, 1), (16, 46)])), L(outline([(84, 72), (100, 62, 1), (86, 56), (102, 46, 1), (84, 46)])),
   L(blob([(10, 60), (12, 26), (30, 16), (50, 14), (70, 16), (88, 26), (90, 60), (50, 64)], 6), CAPG, 'f')])

# Aya Shadowe: media melena gris violácea en casco con flequillo recto y las puntas abiertas a la altura de la barbilla;
# piel pálida, sombra morada en los ojos y sonrisa de lado
PURP = _c('#7e5a8a')
C('aya-shadowe', 'chica', P('#635664', '#f4f1df', iris='#7a5a6a'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=94, hairline=[(8, 62), (92, 62)], ears=False),
  bowl3('front', top=2, side=98, w=8, fringe=62) + [mark([(22, 70), (34, 66), (44, 72), (34, 74)], PURP), mark([(78, 70), (66, 66), (56, 72), (66, 74)], PURP)],
  bowl3('side', top=2, nape=98, w=6, fringe=60), bowl3('back', top=2, nape=98, w=8))

# Aymer Loozit: casquete de pelo castaño con dos cuernos de toro curvos hacia arriba y orejas grandes; piel rojiza, ojos
# fruncidos, colmillos y un rizo en la barbilla
HRB = _c('#8a6a40')
f = [L(outline([(16, 58), (12, 36), (24, 18), (50, 12), (76, 18), (88, 36), (84, 58), (74, 46), (50, 50), (26, 46)])),
     L(outline([(20, 28), (2, 18), (-6, 0, 1), (10, 8), (28, 18)]), 'mid', 'b'), L(outline([(80, 28), (98, 18), (106, 0, 1), (90, 8), (72, 18)]), 'mid', 'b'),
     L(outline([(44, 14), (48, 2, 1), (52, 14)]), 'mid', 'b'), L(outline([(58, 16), (64, 4, 1), (66, 18)]), 'mid', 'b')]
s = [L(outline([(54, 54), (60, 42), (82, 38), (86, 24), (66, 8), (36, 6), (12, 20), (4, 44), (8, 64), (24, 72), (44, 64)])),
     L(outline([(46, 14), (40, -6, 1), (58, 2), (56, 14)]), 'mid', 'b')]
b = [L(outline([(12, 76), (8, 38), (24, 16), (50, 10), (76, 16), (92, 38), (88, 76), (50, 82)])),
     L(outline([(20, 28), (2, 18), (-6, 0, 1), (10, 8), (28, 18)]), 'mid', 'b'), L(outline([(80, 28), (98, 18), (106, 0, 1), (90, 8), (72, 18)]), 'mid', 'b')]
C('aymer-loozit', 'corpulento', P('#674a2c', '#cb714f', iris='#4a5020'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=False, big_ears=3, ear_out=3, face_front=face(w=4, chin=104, jaw=3), nose=(50, 84, 4)),
  f + [L([(38, 94), (40, 89), (42, 94)], WHITE, 'f', False, True), L([(58, 94), (60, 89), (62, 94)], WHITE, 'f', False, True),
       strand([(48, 102), (52, 100), (54, 104), (50, 106)], OUTC, 'f', 1.0)], s, b)

# Azrael Andrews: melena gris hasta los hombros con un flequillo largo que tapa un ojo, una coleta baja a un lado y un
# cuerno negro enroscado en el pelo; pintura roja alrededor del ojo verde y ceño
f, s, b = D(top=-2, w=46, cy=46, n=6, amp=6, seed=5, sb=84, nape=94, long=100, flare=6, ends=3)
C('azrael-andrews', 'normal', P('#7b6f74', '#f4bf86', iris='#3a8a50'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, hairline=[(8, 66), (20, 50), (36, 46), (50, 48), (64, 46), (80, 50), (92, 66)]),
  [L(outline([(26, 18), (6, 6), (-6, 18), (-2, 34), (8, 24), (16, 30)]), _c('#3a3034'), 'b')] + f +
  [fr([(20, 46), (56, 36), (60, 50), (54, 96, 1), (42, 72), (30, 60)]), mark([(73, 70), (84, 66), (84, 80), (74, 80)], _c('#c83a2a')),
   L(outline([(14, 82), (4, 100), (10, 118, 1), (18, 100)]), 'mid', 'f')],
  s, b)

# Barbara "Bunny" Bitt: capucha blanca de conejo con dos orejas largas caídas y un panel rosa en la frente con un botón
# blanco; ojos rosas grandes y boca pequeña
WH2, PK2 = _c('#f4eeee'), _c('#f09090')
def _bunny(view):
    ears = [L(outline([(14, 16), (2, -6), (-18, 20), (-24, 70), (-16, 106, 1), (-4, 72), (4, 40)]), WH2, 'b'),
            L(outline([(86, 16), (98, -6), (118, 20), (124, 70), (116, 106, 1), (104, 72), (96, 40)]), WH2, 'b')]
    if view == 'front':
        return hood('front', WH2, top=-2, rim=_c('#d8c8c8'), face_hole=[(22, 104), (18, 76), (26, 60), (50, 54), (74, 60), (82, 76), (78, 104), (50, 110)]) + ears + \
            [L(outline([(36, 6), (64, 6), (60, 54), (50, 60), (40, 54)]), PK2, 'f', False), L(ell(50, 30, 6, 6), WHITE, 'f')]
    if view == 'side':
        return hood('side', WH2, rim=_c('#d8c8c8')) + [L(outline([(30, 6), (10, -6), (-14, 30), (-18, 80), (-12, 106, 1), (-2, 70), (14, 30)]), WH2, 'b')]
    return hood('back', WH2, rim=_c('#d8c8c8')) + ears


C('barbara-bunny-bitt', 'chica', P('#f4eeee', '#f1d5bc', iris='#e06a7a'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=96, hairline=False, ears=False), _bunny('front'), _bunny('side'), _bunny('back'))

# Barry Tone: tupé plano altísimo gris violáceo oscuro (flat-top) y una barba fina que le recorre la mandíbula; piel
# morena, cejas pobladas, nariz grande y ceño
BRD = '#3d3233'
f = [L([(16, 60), (12, 2), (20, -20), (80, -20), (88, 2), (84, 60), (78, 46), (22, 46)], 'mid', 'b', True, True),
     L([(60, -18), (78, -20), (86, 2), (84, 52), (76, 42)], 'shade', 'b', False)]
s = [L([(54, 56), (62, 44), (82, 40), (88, 4), (84, -20), (20, -20), (8, 10), (4, 50), (20, 64), (44, 60)], 'mid', 'b', True, True)]
b = [L([(14, 72), (12, 2), (20, -20), (80, -20), (88, 2), (86, 72), (50, 78)], 'mid', 'b', True, True)]
C('barry-tone', 'delgado', P('#4e4853', '#ce976a', iris='#3a3a50', beard=BRD),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=98, hairline=[(14, 60), (20, 48), (50, 46), (80, 48), (86, 60)], nose=(50, 88, 3.4),
    face_front=face(chin=108), face_side=face_side(chin=6)),
  f + [L(quad((19, 60), (18, 96), (50, 110)) + quad((50, 110), (82, 96), (81, 60))[1:] + quad((78, 62), (78, 94), (50, 104)) + quad((50, 104), (22, 94), (22, 62))[1:],
         'beard', 'f', False)],
  s + [L(outline([(48, 62), (58, 98), (74, 108), (64, 100), (54, 74)]), 'beard', 'f', False)], b)

# Baz "B-Boy" Boyes: casco de pelo turquesa con flequillo que le tapa los ojos y un rizo enroscado encima, cascos de
# música rojos con la diadema blanca; ojos apretados y una sonrisa enorme de dientes
RDH, WBD = _c('#d03a3a'), _c('#f0e8e0')
def _phones(view):
    if view == 'side':
        return [L(quad((44, 0), (60, -4), (74, 10)), WBD, 'f', False, True, 4.0), L(ell(46, 70, 11, 12), RDH, 'f')]
    return [L(quad((10, 50), (50, -16), (90, 50)), WBD, 'f', False, True, 4.4), L(ell(8, 72, 9, 13), RDH, 'f'), L(ell(92, 72, 9, 13), RDH, 'f')]
C('baz-b-boy-boyes', 'normal', P('#499ea4', '#f9e0c0'),
  F(eyes='none', brows=False, mouth='none', hairline=[(8, 74), (92, 74)], ears=False),
  bowl3('front', top=4, side=74, fringe=74) + [strand([(50, 4), (46, -12), (58, -18), (60, -6), (52, -6)], 'mid', 'f', 3.0)] + _phones('front') +
  [L([(36, 79), (42, 81), (36, 83)], OUTC, 'f', False, False, 1.4), L([(64, 79), (58, 81), (64, 83)], OUTC, 'f', False, False, 1.4)] + big_grin(92, 16, 10),
  bowl3('side', top=4, nape=90, fringe=72) + [strand([(46, 2), (42, -12), (54, -18), (56, -6)], 'mid', 'f', 3.0)] + _phones('side'),
  bowl3('back', top=4, nape=90) + _phones('back'))

# Bea "Bijou" Jou: melena naranja larga en dos grandes bucles a los lados con flequillo recto, una rosa morada con lazo
# negro a un lado; ojos de dos colores (azul y rosa)
ROS, RBN = _c('#8a5aa8'), _c('#3a2a2a')
f, s, b = D(top=-4, w=48, cy=46, n=0, sb=80, nape=96, long=112, flare=12, ends=3)
C('bea-bijou-jou', 'normal', P('#f7915d', '#f6efd8', iris='#4a90d0'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=95, hairline=[(8, 66), (16, 60), (84, 60), (92, 66)]),
  f + [fr([(14, 48), (86, 48), (84, 64), (74, 60), (62, 66, 1), (52, 60), (40, 66, 1), (28, 60), (16, 64)]),
       L(outline([(18, 30), (8, 50), (6, 90), (14, 100), (16, 60)]), RBN, 'f'), L(ell(20, 24, 8, 7), ROS, 'f'), L(ell(64, 79, 3.2, 4.2), _c('#e070a0'), 'f', False)],
  s + [L(ell(30, 22, 7, 7), ROS, 'f')], b + [L(ell(20, 24, 8, 7), ROS, 'f')])

# Beat Baxter: afro enorme castaño oscuro; piel morena, ojos caídos tristones, perilla fina y boca pequeña
f, s, b = D(top=-12, w=58, cy=40, n=12, amp=7, soft=True, seed=7, sb=70, nape=88, fr_=44)
C('beat-baxter', 'normal', P('#38281e', '#bd8d5c'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, hairline=hl(7, 64, 52, 58, jit=2, seed=2)),
  f + lid_eyes(77, 14) + [L(quad((26, 70), (34, 66), (42, 70)), OUTC, 'f', False, False, 1.6), L(quad((74, 70), (66, 66), (58, 70)), OUTC, 'f', False, False, 1.6),
                          L([(50, 102), (50, 108)], OUTC, 'f', False, False, 1.4)], s, b)

# Beatrix "Bee" Hunny: gorro de abeja a rayas morado y amarillo con unas gafas rojas de ojos de insecto; dos coletas
# rubias cortas que salen por debajo y sonrisa
BPR, BYL, BRD2 = _c('#6c5261'), _c('#fdfa0b'), _c('#f62924')
def _bee(view):
    if view == 'front':
        return [L(outline([(16, 84), (4, 96), (10, 104, 1), (20, 92)]), BYL, 'b'), L(outline([(84, 84), (96, 96), (90, 104, 1), (80, 92)]), BYL, 'b'),
                cap('front', BPR, top=0, rim=62, w=46, z='f'), L(quad((8, 30), (50, 6), (92, 30)) + quad((94, 38), (50, 14), (6, 38)), BYL, 'f', False),
                L(quad((4, 52), (50, 32), (96, 52)) + quad((96, 58), (50, 40), (4, 58)), BYL, 'f', False),
                L(blob([(12, 70), (50, 70), (88, 70), (84, 82), (50, 78), (16, 82)], 4), BLACK, 'f'),
                L(blob([(16, 64), (36, 58), (46, 70), (34, 84), (18, 80)], 4), BRD2, 'f'), L(blob([(84, 64), (64, 58), (54, 70), (66, 84), (82, 80)], 4), BRD2, 'f')]
    if view == 'side':
        return [L(outline([(36, 84), (26, 98), (32, 106, 1), (42, 92)]), BYL, 'b'), cap('side', BPR, top=0, rim=60, z='f'),
                L(quad((4, 40), (50, 4), (92, 30)) + quad((92, 38), (50, 12), (4, 48)), BYL, 'f', False),
                L(blob([(70, 62), (92, 62), (94, 82), (74, 80)], 4), BRD2, 'f')]
    return [L(outline([(16, 84), (4, 96), (10, 104, 1), (20, 92)]), BYL, 'b'), L(outline([(84, 84), (96, 96), (90, 104, 1), (80, 92)]), BYL, 'b'),
            cap('back', BPR, top=0, rim=66, z='f'), L(quad((6, 34), (50, 10), (94, 34)) + quad((94, 42), (50, 18), (6, 42)), BYL, 'f', False),
            L(quad((4, 58), (50, 40), (96, 58)) + quad((96, 64), (50, 48), (4, 64)), BYL, 'f', False)]
C('beatrix-bee-hunny', 'chica', P('#fdfa0b', '#ecdec8'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, hairline=False, ears=False), _bee('front'), _bee('side'), _bee('back'))

# Beau Gotcher (portero): pelo lila rosado en casco con un flequillo que le tapa un ojo; piel morena, un ojo enorme redondo
# blanco con la pupila negra y sonrisa
f, s, b = D(top=2, w=46, cy=46, sb=72, nape=88)
C('beau-gotcher', 'normal', P('#d3b5d3', '#b38b78'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=95, hairline=[(8, 66), (20, 50), (36, 46), (50, 46), (64, 46), (80, 50), (92, 66)]),
  f + [fr([(16, 46), (40, 40), (60, 42), (64, 60), (56, 92, 1), (46, 74), (28, 66)]), L(ell(68, 76, 8, 8), WHITE, 'f'), L(ell(68, 76, 4, 4), BLACK, 'f', False)],
  s + [L(ell(82, 76, 4, 7), WHITE, 'f'), L(ell(84, 76, 2.2, 3), BLACK, 'f', False)], b)

# Benji Near (portero): un turbante de tela a rayas azul y salmón muy calado sobre los ojos, mechones blancos esponjosos
# a los lados, nariz larga naranja y sonrisa
TBL, TSL = _c('#92c3cc'), _c('#ef8b6e')
def _turban(view):
    if view == 'front':
        return [L(blob([(10, 66), (8, 34), (24, 14), (50, 8), (76, 14), (92, 34), (90, 66), (50, 70)], 6), TBL, 'f'),
                L(outline([(36, 10), (64, 10), (66, 70), (34, 70)]), TSL, 'f', False),
                L(blob([(10, 64), (50, 60), (90, 64), (88, 72), (50, 70), (12, 72)], 4), _c('#6a9aa4'), 'f', False)]
    if view == 'side':
        return [L(blob([(6, 70), (4, 30), (30, 8), (66, 8), (88, 26), (94, 60), (60, 66)], 6), TBL, 'f'),
                L(outline([(30, 8), (50, 8), (40, 68), (22, 68)]), TSL, 'f', False)]
    return [L(blob([(10, 74), (8, 34), (24, 14), (50, 8), (76, 14), (92, 34), (90, 74), (50, 78)], 6), TBL, 'f'),
            L(outline([(36, 10), (64, 10), (66, 76), (34, 76)]), TSL, 'f', False)]
C('benji-near', 'normal', P('#f0ece4', '#f9cea1'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=96, hairline=False, ears=False, nose=(50, 84, 3)),
  [L(curls := blob([(10, 60), (2, 80), (8, 100), (22, 104), (24, 80)], 6)), L(blob([(90, 60), (98, 80), (92, 100), (78, 104), (76, 80)], 6))] + _turban('front') +
  [L(blob([(46, 72), (54, 72), (58, 88), (50, 92), (42, 88)], 4), TSL, 'f'), L([(34, 74), (42, 76)], OUTC, 'f', False, False, 1.6), L([(66, 74), (58, 76)], OUTC, 'f', False, False, 1.6)],
  [L(blob([(30, 60), (20, 80), (28, 100), (44, 98), (46, 76)], 6))] + _turban('side') + [L(blob([(84, 74), (98, 84), (88, 90)], 4), TSL, 'f')],
  [L(blob([(8, 64), (4, 100), (50, 106), (96, 100), (92, 64)], 6))] + _turban('back'))

# Beorn Kodiak (portero): pelo gris echado a un lado en mechones de punta sobre una capa más oscura, patillas y barba fina
# oscuras por la mandíbula; ojos negros afilados y una sonrisa de dientes
f, s, b = D(top=-8, w=46, cy=44, n=6, amp=14, sweep=-0.8, seed=6, sb=66, nape=86)
C('beorn-kodiak', 'normal', P('#a8adb1', '#f9bc7d', iris='#202020', beard='#4e5760'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=95, hairline=hl(6, 64, 48, 56, lean=-3, jit=2, seed=8)),
  [L(outline([(12, 66), (8, 40), (92, 40), (88, 66)]), 'beard', 'b')] + f +
  [L(quad((19, 60), (19, 94), (40, 104)) + quad((40, 100), (24, 90), (24, 62))[0:], 'beard', 'f', False),
   L(quad((81, 60), (81, 94), (60, 104)) + quad((60, 100), (76, 90), (76, 62))[0:], 'beard', 'f', False)],
  s + [L(outline([(48, 62), (58, 96), (70, 104), (60, 92), (54, 70)]), 'beard', 'f', False)], b)

# Bert Laydie (portero): casco de mariquita rojo con lunares negros y dos antenas cortas; trenzas negras que cuelgan por los
# lados; ojos cerrados tranquilos y sonrisa
LRD = _c('#ee4325')
def _lady(view):
    spots = [(30, 30), (62, 22), (50, 46), (18, 50), (84, 44)]
    if view == 'front':
        out = [L(outline([(20, 66), (14, 104, 1), (24, 70)]), 'mid', 'b'), L(outline([(80, 66), (86, 104, 1), (76, 70)]), 'mid', 'b'),
               cap('front', LRD, top=0, rim=62, w=48, z='f'), L(quad((8, 62), (50, 50), (92, 62)) + quad((92, 66), (50, 56), (8, 66)), _c('#3b2a27'), 'f', False),
               L([(36, 4), (30, -8)], BLACK, 'f', False, False, 2.4), L([(64, 4), (70, -8)], BLACK, 'f', False, False, 2.4)]
        return out + [L(ell(x, y, 6, 5), _c('#3b2a27'), 'f', False) for x, y in spots]
    if view == 'side':
        return [L(outline([(36, 66), (34, 104, 1), (44, 70)]), 'mid', 'b'), cap('side', LRD, top=0, rim=60, z='f'), L([(46, 2), (54, -10)], BLACK, 'f', False, False, 2.4)] + \
               [L(ell(x, y, 6, 5), _c('#3b2a27'), 'f', False) for x, y in ((26, 30), (56, 22), (40, 48))]
    return [L(outline([(20, 66), (14, 104, 1), (24, 70)]), 'mid', 'b'), L(outline([(80, 66), (86, 104, 1), (76, 70)]), 'mid', 'b'),
            cap('back', LRD, top=0, rim=66, z='f')] + [L(ell(x, y, 6, 5), _c('#3b2a27'), 'f', False) for x, y in spots]
C('bert-laydie', 'normal', P('#3b2a27', '#f5be93'),
  F(eyes='closed', brows=False, mouth='smile', mouth_y=94, hairline=False, ears=False), _lady('front'), _lady('side'), _lady('back'))

# Bertie Cees (portero): cresta verde muy oscura altísima y puntas a los lados de la cabeza; piel rojiza oscura, nariz
# roja, ojos fruncidos y una sonrisa ancha
f = [L(outline([(24, 40), (36, 4), (48, -26, 1), (56, 0), (68, 20), (76, 40), (50, 36)])),
     L(outline([(18, 66), (-4, 72, 1), (12, 58), (-2, 52, 1), (18, 48)])), L(outline([(82, 66), (104, 72, 1), (88, 58), (102, 52, 1), (82, 48)]))]
s = [L(outline([(20, 30), (34, 0), (40, -24, 1), (56, 0), (80, 22), (72, 34), (40, 34)])), L(outline([(40, 66), (20, 74, 1), (30, 58), (18, 52, 1), (40, 50)]))]
b = [L(outline([(36, 36), (44, 0), (48, -26, 1), (56, 0), (64, 36)])),
     L(outline([(18, 66), (-4, 72, 1), (12, 58), (-2, 52, 1), (18, 48)])), L(outline([(82, 66), (104, 72, 1), (88, 58), (102, 52, 1), (82, 48)]))]
C('bertie-cees', 'corpulento', P('#3d3c2c', '#c87252'),
  F(eyes='sharp', brows='angry', mouth='none', hairline=False, face_front=face(w=4, chin=104, jaw=2)),
  skull3('front') + f + [L(ell(50, 84, 5, 4), _c('#b03a2a'), 'f', False), L(quad((32, 92), (50, 100), (68, 92)), OUTC, 'f', False, False, 2.0)],
  skull3('side') + s, skull3('back') + b)

# Bianca Snough: pelo morado redondeado con flequillo recto, una diadema dorada y dos moños bajos a la altura de las orejas;
# ojos rojos grandes y sonrisa
GLB = _c('#d2aa69')
C('bianca-snough', 'chica', P('#634970', '#f4efdc', iris='#c02a3a'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=95, hairline=[(8, 62), (92, 62)], ears=False),
  bowl3('front', top=0, side=78, fringe=62) + [L(ell(12, 84, 10, 10), 'mid', 'b'), L(ell(88, 84, 10, 10), 'mid', 'b'), band('front', GLB, y=22, h=5, w=40, dip=10)],
  bowl3('side', top=0, nape=84, fringe=60) + [L(ell(40, 84, 10, 10), 'mid', 'f'), band('side', GLB, y=16, h=5)],
  bowl3('back', top=0, nape=84) + [L(ell(14, 88, 10, 10)), L(ell(86, 88, 10, 10)), band('back', GLB, y=20, h=5, w=40)])

# Bianco Snowden: melena blanca ondulada y abultada; piel morena clara, ojos amarillos con un trazo negro grueso alrededor
# y una sonrisa enorme de dientes
f, s, b = D(top=-6, w=52, cy=46, n=10, amp=7, soft=True, seed=9, sb=86, nape=96, long=None)
C('bianco-snowden', 'normal', P('#e9eada', '#fbb880', iris='#d0a020', shade='#c0bcaa'),
  F(eyes='sharp', brows=False, mouth='none', hairline=[(8, 66), (16, 52), (30, 44), (50, 48), (70, 44), (84, 52), (92, 66)], face_front=face(chin=104)),
  f + big_grin(92, 18, 10) + [L(quad((22, 70), (34, 66), (44, 72)), OUTC, 'f', False, False, 2.4), L(quad((78, 70), (66, 66), (56, 72)), OUTC, 'f', False, False, 2.4)],
  s, b)

# Bill Ingsgate: pinchos azul marino muy oscuros con una llama magenta en el centro, una cinta blanca gruesa y retorcida
# alrededor de la frente; ojos negros con raya gruesa, patillas oscuras y sonrisa de lado
MAG, ROPE = _c('#a82266'), _c('#ece4e0')
f, s, b = D(top=-12, w=46, cy=42, n=8, amp=16, seed=21, sb=66, nape=84)
C('bill-ingsgate', 'normal', P('#2b2a34', '#f4ba83', iris='#1a1a1a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=[(8, 66), (16, 58), (84, 58), (92, 66)]),
  f + [L(outline([(30, 44), (36, 20, 1), (44, 30), (50, 10, 1), (58, 28), (66, 18, 1), (70, 44)]), MAG, 'f', False),
       L(blob([(4, 50), (24, 40), (50, 38), (76, 40), (96, 50), (98, 60), (76, 54), (50, 52), (24, 54), (2, 60)], 4), ROPE, 'f'),
       strand([(20, 44), (26, 54)], _c('#c0b8b4'), 'f', 1.2), strand([(42, 40), (46, 52)], _c('#c0b8b4'), 'f', 1.2), strand([(62, 40), (66, 52)], _c('#c0b8b4'), 'f', 1.2),
       L([(19, 70), (20, 86)], OUTC, 'f', False, False, 2.4), L([(81, 70), (80, 86)], OUTC, 'f', False, False, 2.4)],
  s + [band('side', ROPE, y=44, h=8)], b + [band('back', ROPE, y=44, h=8)])

# Bill Sye: pelo morado oscuro despeinado que le cae en mechones por la frente y la nuca; ojos rojos con los párpados
# oscuros y boca recta
f, s, b = D(top=-2, w=48, cy=46, n=9, amp=8, sweep=0.2, seed=22, sb=82, nape=96, flare=6)
C('bill-sye', 'normal', P('#3d2b3f', '#f8f0d9', iris='#c03a3a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, hairline=hl(6, 66, 50, 62, jit=3, seed=9)),
  f + [mark([(22, 70), (34, 66), (44, 70), (34, 72)], _c('#4a3040')), mark([(78, 70), (66, 66), (56, 70), (66, 72)], _c('#4a3040'))], s, b)

# Bisher "B. White" Whitehurst: pelo blanco con una cresta alta y una cuña oscura en el centro, y los lados largos que se
# enroscan hacia fuera a la altura del cuello; ojos con manchas negras alrededor, perilla negra y ceño
f = [L(outline([(36, 40), (40, 6), (50, -16, 1), (60, 6), (64, 40)])), L(outline([(44, 34), (50, -4, 1), (56, 34)]), _c('#5e5c57'), 'f', False),
     L(outline([(18, 50), (12, 74), (14, 96), (4, 104), (-6, 98, 1), (6, 108), (22, 102), (22, 60)])),
     L(outline([(82, 50), (88, 74), (86, 96), (96, 104), (106, 98, 1), (94, 108), (78, 102), (78, 60)]))]
s = [L(outline([(30, 34), (40, 4), (50, -14, 1), (64, 6), (70, 36)])),
     L(outline([(52, 54), (40, 52), (20, 60), (10, 84), (8, 100), (-4, 100, 1), (8, 110), (24, 102), (34, 80), (46, 66)]))]
b = [L(outline([(36, 40), (40, 6), (50, -16, 1), (60, 6), (64, 40)])),
     L(outline([(16, 46), (10, 74), (12, 96), (2, 104), (-8, 98, 1), (4, 108), (50, 104), (96, 108), (108, 98, 1), (98, 104), (88, 96), (90, 74), (84, 46), (50, 40)]))]
C('bisher-b-white-whitehurst', 'delgado', P('#e8e2de', '#fdeab8', iris='#2a2a2a', shade='#bdb0aa'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=97, hairline=False, face_front=face(chin=108), face_side=face_side(chin=6), nose=(50, 86, 2.4)),
  skull3('front') + f + [mark([(22, 70), (36, 66), (46, 72), (40, 82), (26, 80)], _c('#3a3634')), mark([(78, 70), (64, 66), (54, 72), (60, 82), (74, 80)], _c('#3a3634')),
                         L(outline([(44, 102), (56, 102), (50, 112, 1)]), _c('#2a2624'), 'f')] + sharp_eyes(_c('#2a2a2a'), 75, 14),
  skull3('side') + s + [L(outline([(78, 102), (86, 102), (80, 112, 1)]), _c('#2a2624'), 'f')], skull3('back') + b)

# Bishopp "B. Black" Blackside: pelo negro en una cúpula enorme y ancha con un moño encima; piel morena, barba negra fina
# por la mandíbula, nariz larga con una raya oscura y ceño
f = [L(blob([(14, 60), (-2, 40), (2, 16), (26, 4), (50, 2), (74, 4), (98, 16), (102, 40), (86, 60), (70, 48), (50, 52), (30, 48)], 6)), L(ell(50, -6, 9, 7)),
     L(blob([(60, 4), (90, 12), (100, 38), (86, 56), (72, 34)], 6), 'shade', 'b', False)]
s = [L(blob([(52, 54), (62, 42), (84, 38), (92, 22), (70, 4), (36, 0), (6, 10), (-6, 36), (4, 60), (26, 66), (44, 60)], 6)), L(ell(44, -6, 8, 7))]
b = [L(blob([(10, 70), (-2, 40), (2, 16), (26, 4), (50, 2), (74, 4), (98, 16), (102, 40), (90, 70), (50, 76)], 6)), L(ell(50, -6, 9, 7))]
C('bishopp-b-black-blackside', 'delgado', P('#322f32', '#eca664', iris='#2a2a2a', beard='#2b2320'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=98, hairline=[(14, 60), (30, 50), (50, 54), (70, 50), (86, 60)],
    face_front=face(chin=108), face_side=face_side(chin=6)),
  f + [L(quad((19, 66), (18, 96), (50, 112)) + quad((50, 112), (82, 96), (81, 66))[1:] + quad((78, 68), (78, 94), (50, 106)) + quad((50, 106), (22, 94), (22, 68))[1:],
         'beard', 'f', False), L([(48, 70), (52, 70), (51, 90), (49, 90)], _c('#6a4a30'), 'f', False)],
  s + [L(outline([(48, 64), (58, 100), (74, 110), (64, 102), (54, 76)]), 'beard', 'f', False)], b)

# Bjorn Thiswey: tupé bajo blanco rosado y largas patillas lilas por los lados de una cara larguísima y pálida; ojos
# amarillos con un aro negro grueso, ceño y una perilla pequeña
f = [L(outline([(26, 44), (30, 20), (50, 6), (70, 20), (74, 44), (50, 40)]), _c('#e8dce0')), strand([(40, 16), (46, 38)], _c('#c0b0b8'), 'f', 1.0),
     strand([(56, 14), (54, 38)], _c('#c0b0b8'), 'f', 1.0),
     L(outline([(20, 48), (14, 70), (16, 102), (22, 100), (24, 60)])), L(outline([(80, 48), (86, 70), (84, 102), (78, 100), (76, 60)]))]
s = [L(outline([(24, 40), (30, 14), (54, 4), (76, 16), (80, 38), (50, 36)]), _c('#e8dce0')), L(outline([(48, 50), (40, 56), (40, 96), (46, 100), (50, 70)]))]
b = [L(outline([(26, 44), (30, 20), (50, 6), (70, 20), (74, 44), (50, 40)]), _c('#e8dce0')), L(outline([(16, 44), (10, 76), (14, 100), (86, 100), (90, 76), (84, 44), (50, 50)]))]
C('bjorn-thiswey', 'delgado', P('#8b7394', '#e3cbad', iris='#e0b030'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=100, hairline=False, face_front=face(chin=112), face_side=face_side(chin=9), nose=(50, 86, 2.4)),
  skull3('front') + f + round_glasses('front', OUTC, y=76, sep=14, r=6.4, w=2.6) + [L(ell(50, 108, 2.4, 2.4), OUTC, 'f', False)],
  skull3('side') + s, skull3('back') + b)

# Blakey Itchifoot: pelo corto verde agua con el nacimiento en pico muy bajo, cara larguísima y pálida con una franja negra
# en forma de antifaz sobre los ojos, nariz larga gris y boca recta
f, s, b = D(top=4, w=44, cy=44, sb=60, nape=82)
C('blakey-itchifoot', 'delgado', P('#759e8e', '#e2cbab', iris='#2a2a2a'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=102, hairline=[(10, 60), (22, 50), (40, 46), (50, 62), (60, 46), (78, 50), (90, 60)],
    face_front=face(chin=114, w=-1), face_side=face_side(chin=10)),
  f + [mark([(20, 70), (36, 74), (50, 66), (64, 74), (80, 70), (76, 80), (64, 78), (50, 72), (36, 78), (24, 80)], BLACK),
       L([(48, 74), (52, 74), (54, 96), (46, 96)], _c('#9a9a90'), 'f', False)], s, b)

# Bloomer "Bloo" Topp (portero): pelo rubio en pinchos hacia arriba y hacia los lados, máscara azul tribal alrededor de los
# ojos que baja por la nariz; boca con los dientes
MSK = _c('#318caf')
f, s, b = D(top=-14, w=50, cy=44, n=9, amp=16, seed=31, sb=80, nape=92)
C('bloomer-bloo-topp', 'normal', P('#f8ea9a', '#f8bd7c', iris='#c03030', shade='#d8b848'),
  F(eyes='round', brows=False, mouth='grin', mouth_y=97, hairline=hl(6, 62, 48, 58, jit=3, seed=12)),
  [L(outline([(16, 80), (-4, 92, 1), (10, 76), (-6, 70, 1), (14, 66)])), L(outline([(84, 80), (104, 92, 1), (90, 76), (106, 70, 1), (86, 66)]))] + f +
  [L(blob([(16, 66), (34, 60), (50, 66), (66, 60), (84, 66), (82, 84), (62, 84), (54, 94), (46, 94), (38, 84), (18, 84)], 4), MSK, 'f'),
   L(ell(36, 74, 7, 6), WHITE, 'f', False), L(ell(64, 74, 7, 6), WHITE, 'f', False), L(ell(36, 74, 3, 3), _c('#c03030'), 'f', False),
   L(ell(64, 74, 3, 3), _c('#c03030'), 'f', False)],
  s + [L(blob([(70, 64), (92, 64), (94, 90), (80, 86), (72, 82)], 4), MSK, 'f')], b)

# Bluster Tryadd: cara redonda muy pálida con orejas grandes, pelo celeste corto con dos mechones de punta hacia los lados
# como orejas de gato; ojos verdes caídos y boca en O
f = [L(blob([(14, 56), (16, 32), (34, 16), (50, 14), (66, 16), (84, 32), (86, 56), (70, 40), (50, 36), (30, 40)], 6)),
     L(outline([(20, 30), (-10, 22, 1), (4, 46), (18, 50)])), L(outline([(80, 30), (110, 22, 1), (96, 46), (82, 50)]))]
s = [L(blob([(30, 46), (24, 22), (50, 12), (76, 20), (86, 36), (60, 34)], 6)), L(outline([(40, 22), (14, 6, 1), (24, 34)]))]
b = [L(blob([(12, 60), (16, 30), (34, 16), (50, 14), (66, 16), (84, 30), (88, 60), (50, 54)], 6)),
     L(outline([(20, 30), (-10, 22, 1), (4, 46), (18, 50)])), L(outline([(80, 30), (110, 22, 1), (96, 46), (82, 50)]))]
C('bluster-tryadd', 'bajito', P('#5ebfd8', '#feeab8', iris='#3a8a6a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, big_ears=4, ear_out=4, face_front=face(w=5, chin=104, top=12)),
  skull3('front') + f + lid_eyes(76, 16) + [L(ell(50, 96, 3, 4), _c('#c05050'), 'f', False), L(ell(50, 86, 2, 1.5), _c('#e0a090'), 'f', False)],
  skull3('side') + s, skull3('back') + b)

# Bobbie Pompon: gorro de punto blanco calado hasta la nariz con un pompón verde oscuro encima y dos cuernos verdes curvos a
# los lados; piel morena y sonrisa
KNT, DGR = _c('#eeeae6'), _c('#404743')
def _knit(view):
    if view == 'front':
        return [L(outline([(16, 40), (-4, 36), (-6, 14, 1), (6, 26), (20, 28)]), DGR, 'b'), L(outline([(84, 40), (104, 36), (106, 14, 1), (94, 26), (80, 28)]), DGR, 'b'),
                L(blob([(10, 84), (8, 40), (26, 12), (50, 6), (74, 12), (92, 40), (90, 84), (50, 88)], 6), KNT, 'f')] + \
               [strand([(x, 14 + abs(x - 50) * 0.3), (x, 84)], _c('#c8c4c0'), 'f', 1.0) for x in (26, 38, 50, 62, 74)] + [L(ell(50, 6, 13, 12), DGR, 'f')]
    if view == 'side':
        return [L(outline([(40, 30), (24, 22), (20, 0, 1), (34, 12), (48, 20)]), DGR, 'b'),
                L(blob([(10, 84), (4, 40), (26, 10), (60, 6), (86, 22), (94, 50), (92, 86), (50, 90)], 6), KNT, 'f'), L(ell(52, 4, 12, 11), DGR, 'f')]
    return [L(outline([(16, 40), (-4, 36), (-6, 14, 1), (6, 26), (20, 28)]), DGR, 'b'), L(outline([(84, 40), (104, 36), (106, 14, 1), (94, 26), (80, 28)]), DGR, 'b'),
            L(blob([(10, 84), (8, 40), (26, 12), (50, 6), (74, 12), (92, 40), (90, 84), (50, 88)], 6), KNT, 'f'), L(ell(50, 6, 13, 12), DGR, 'f')]
C('bobbie-pompon', 'normal', P('#404743', '#a46d46'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=96, hairline=False, ears=False), _knit('front'), _knit('side'), _knit('back'))

# Boe Heemian: melena naranja enorme y ondulada que cae a un lado, una cinta azul marino con aros plateados en la frente
# y aros grandes en las orejas; piel morena, mirada pícara y sonrisa
SLR, NBD = _c('#c8c4c0'), _c('#3a4a6a')
f, s, b = D(top=-6, w=50, cy=46, n=7, amp=6, soft=True, seed=33, sb=84, nape=100, long=110, flare=12, ends=3)
C('boe-heemian', 'chica', P('#e36b44', '#eca663', iris='#2a2a2a'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=95, hairline=[(8, 66), (16, 56), (84, 56), (92, 66)]),
  f + [band('front', NBD, y=44, h=8, w=44, dip=4)] + [L(ell(x, 50, 3, 3) + [ell(x, 50, 3, 3)[0]], SLR, 'f', False, False, 1.4) for x in (26, 40, 54, 68)] +
  [L(ell(14, 90, 6, 7) + [ell(14, 90, 6, 7)[0]], SLR, 'f', False, False, 2.0), L(ell(86, 90, 6, 7) + [ell(86, 90, 6, 7)[0]], SLR, 'f', False, False, 2.0),
   fr([(60, 52), (88, 56), (96, 96), (90, 110, 1), (80, 86)])],
  s + [band('side', NBD, y=40, h=8)], b + [band('back', NBD, y=40, h=8, w=46)])

# Bolt Cagey: ninja con el pelo azul acero en mechones largos peinados hacia atrás, la cara tapada por una máscara negra y
# una cinta negra con una placa metálica en la frente, con las puntas al viento; ojos azules
NJ, PLT = _c('#2e2a2a'), _c('#c8bfb2')
def _ninja(view):
    if view == 'front':
        return [L(outline([(14, 58), (16, 10), (40, -10), (70, -18, 1), (64, 0), (96, -10, 1), (84, 18), (86, 58)]), 'mid', 'b'),
                L(blob([(14, 104), (12, 66), (20, 50), (80, 50), (88, 66), (86, 104), (50, 110)], 6), NJ, 'f'),
                L(blob([(16, 54), (84, 54), (84, 66), (16, 66)], 4), NJ, 'f'), L([(36, 46), (64, 46), (64, 62), (36, 62)], PLT, 'f', True, True),
                L(blob([(18, 70), (82, 70), (82, 82), (18, 82)], 4), 'skin', 'f', False),
                L(outline([(12, 60), (-14, 74, 1), (2, 72), (-10, 90, 1), (10, 74)]), NJ, 'f'), L(outline([(88, 60), (114, 74, 1), (98, 72), (110, 90, 1), (90, 74)]), NJ, 'f')]
    if view == 'side':
        return [L(outline([(92, 52), (84, 14), (50, 0), (20, -6), (-20, -8, 1), (0, 6), (-14, 20, 1), (8, 22), (6, 56)]), 'mid', 'b'),
                L(blob([(20, 104), (10, 70), (16, 48), (90, 50), (94, 70), (94, 104), (50, 110)], 6), NJ, 'f'),
                L(blob([(70, 70), (94, 70), (94, 82), (70, 82)], 4), 'skin', 'f', False), L([(80, 48), (94, 48), (94, 62), (80, 62)], PLT, 'f', True, True),
                L(outline([(10, 58), (-16, 70, 1), (0, 70), (-12, 86, 1), (12, 72)]), NJ, 'f')]
    return [L(outline([(14, 50), (14, 10), (40, -10), (70, -18, 1), (64, 0), (96, -10, 1), (86, 50)]), 'mid', 'b'),
            L(blob([(12, 104), (10, 60), (90, 60), (88, 104), (50, 110)], 6), NJ, 'f'),
            L(outline([(40, 60), (20, 80, 1), (36, 76), (24, 100, 1), (50, 70)]), NJ, 'f')]
C('bolt-cagey', 'normal', P('#688ea3', '#e0c8a8', iris='#3a7ac0'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False), _ninja('front') + sharp_eyes(_c('#3a7ac0'), 75, 14),
  _ninja('side') + sharp_eye_side(_c('#3a7ac0'), 74), _ninja('back'))

# Bonnie Sytree: pelo rubio con flequillo recto, dos moños abultados arriba a los lados y dos coletas largas en bolas que
# caen hasta el pecho; ojos morados grandes, rubor y sonrisa
def _bub(view):
    if view == 'side':
        return [L(ell(30, 12, 12, 12), 'mid', 'b')] + [L(ell(30, y, 8, 7), 'mid', 'b') for y in (64, 80, 96, 110)]
    out = [L(ell(12, 14, 14, 14), 'mid', 'b'), L(ell(88, 14, 14, 14), 'mid', 'b')]
    for x in (4, 96):
        out += [L(ell(x, y, 8, 7), 'mid', 'b') for y in (62, 78, 94, 108)]
    return out
C('bonnie-sytree', 'chica', P('#f2e77d', '#fdeab8', iris='#8a4ab0', shade='#d8c060'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=95, hairline=[(8, 62), (92, 62)], ears=False),
  _bub('front') + bowl3('front', top=2, side=80, fringe=62) + blush(86, 24, 4),
  _bub('side') + bowl3('side', top=2, nape=86, fringe=60), _bub('back') + bowl3('back', top=2, nape=86))

# Bonza Barnett: pelo negro corto en pico sobre la frente con dos mechones como cuernos a los lados, rayados en celeste;
# ojos azules redondos enormes, rubor y una sonrisa ancha
CYN = _c('#a0f3f4')
def _horns2(view):
    if view == 'side':
        return [L(outline([(40, 20), (18, -4, 1), (50, 6)]), 'mid', 'b'), L([(30, 8), (36, 4), (40, 10), (34, 14)], CYN, 'f', False)]
    return [L(outline([(24, 22), (-6, 4, 1), (18, 40)]), 'mid', 'b'), L(outline([(76, 22), (106, 4, 1), (82, 40)]), 'mid', 'b'),
            L([(6, 10), (12, 8), (16, 22), (8, 20)], CYN, 'f', False), L([(94, 10), (88, 8), (84, 22), (92, 20)], CYN, 'f', False)]
f, s, b = D(top=6, w=44, cy=44, sb=62, nape=82)
C('bonza-barnett', 'normal', P('#2b2f36', '#fce9b7', iris='#3a8ab0'),
  F(eyes='round', brows=True, mouth='smile', mouth_y=94, mouth_w=12, hairline=[(10, 62), (20, 50), (30, 56), (40, 46), (50, 56), (60, 46), (70, 56), (80, 50), (90, 62)]),
  _horns2('front') + f + blush(88, 26, 4), _horns2('side') + s, _horns2('back') + b)
