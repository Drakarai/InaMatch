"""Ojeadores de GO (scouts-go), tanda 02: dibujados a partir de su retrato de Victory Road; claves 'scouts-go:<id>'.

Ninguno tiene modelo 3D: el frente sale del retrato y el perfil y la espalda se deducen. Se reutilizan las ayudas de los
ojeadores de IE (dome/hl/face de ie1_09, bowl3/hood/ring/scarf de ie3_02, cap/band de ie3_06...) sin tocarlas; el sexo
para el cuerpo viene de la ficha de la wiki de cada uno."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401
from chars_scouts_ie1_09 import dome, hl, face, face_side, F, P, mark, _c  # noqa: F401
from chars_scouts_ie1_03 import thick_brows, side_brow, goggles, round_specs, big_grin, freckles  # noqa: F401
from chars_scouts_ie3_02 import ring, hood, skull3, bowl3, scarf, side_lock  # noqa: F401
from chars_scouts_ie3_06 import cap, band, arc  # noqa: F401
from chars_scouts_ie2_03 import round_glasses, curls  # noqa: F401
from chars_scouts_ie1_10 import nose_tri, squint  # noqa: F401

K = 'scouts-go:'
WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)
RED = _c('#c8302a')
PINK = _c('#f08a9a')


def C(pid, body, palette, f, front, side, back):
    """Como en la tanda 09 de IE1: el nacimiento del pelo baja por el borde de la cara para que su raya no cruce el pelo."""
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[K + pid] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def mir(pts):
    return [(100 - p[0],) + tuple(p[1:]) for p in pts][::-1]


def fl(pts, c='mid', z='f'):
    """Mechón por delante de la cara."""
    return L(outline(pts), c, z)


def blk(pts, c=BLACK, z='f', w=0):
    return L(pts, c, z, False, False, w) if w else L(blob(pts, 4), c, z, False)


def bow_knot(x, y, c, spot=None, s=1.0):
    """Lazo: dos alas y el nudo."""
    out = [L(outline([(x, y), (x - 16 * s, y - 10 * s, 1), (x - 20 * s, y + 4 * s), (x - 12 * s, y + 10 * s, 1)]), c, 'f'),
           L(outline([(x, y), (x + 16 * s, y - 10 * s, 1), (x + 20 * s, y + 4 * s), (x + 12 * s, y + 10 * s, 1)]), c, 'f'),
           L(ell(x, y, 5 * s, 5 * s), c, 'f')]
    if spot:
        out += [L(ell(x - 12 * s, y - 2 * s, 2.6 * s, 2.2 * s), spot, 'f', False), L(ell(x + 13 * s, y - 1 * s, 2.6 * s, 2.2 * s), spot, 'f', False)]
    return out


def lens_rect(view, frame, lens, y=74, sep=14, w=10, h=6):
    """Gafas de cristales rectangulares (montura gruesa de color)."""
    if view == 'front':
        out = []
        for cx in (50 - sep, 50 + sep):
            out.append(L(blob([(cx - w - 2, y - h - 2), (cx + w + 2, y - h - 2), (cx + w + 2, y + h + 2), (cx - w - 2, y + h + 2)], 3), frame, 'f', True))
            out.append(L(blob([(cx - w + 1, y - h + 1), (cx + w - 1, y - h + 1), (cx + w - 1, y + h - 1), (cx - w + 1, y + h - 1)], 3), lens, 'f', False))
        return out + [L([(50 - sep + w, y - 2), (50 + sep - w, y - 2)], frame, 'f', False, False, 3)]
    if view == 'side':
        return [L(blob([(72, y - h - 2), (90, y - h - 2), (90, y + h + 2), (73, y + h + 2)], 3), frame, 'f', True),
                L(blob([(75, y - h + 1), (88, y - h + 1), (88, y + h - 1), (76, y + h - 1)], 3), lens, 'f', False),
                L([(72, y - 2), (44, y - 6)], frame, 'f', False, False, 3)]
    return [L(quad((6, y - 4), (50, y), (94, y - 4)), frame, 'f', False, False, 3)]


def kabuki(c, ey=75, sep=14, iris=None):
    """Pintura de los ojos (kabuki): una llama alrededor de cada ojo que sube hacia la sien; con iris, el ojo encima."""
    out = []
    for cx, s in ((50 - sep, 1), (50 + sep, -1)):
        out.append(L(blob([(cx + 7 * s, ey + 6), (cx - 2 * s, ey + 8), (cx - 10 * s, ey + 2), (cx - 14 * s, ey - 10), (cx - 6 * s, ey - 4), (cx + 2 * s, ey - 6)], 4), c, 'f', False))
        if iris:
            out.append(L(blob([(cx - 6 * s, ey - 3), (cx + 6 * s, ey - 1), (cx + 5 * s, ey + 4), (cx - 5 * s, ey + 3)], 3), WHITE, 'f', False))
            out.append(L(ell(cx + s, ey + 1, 2.6, 3), iris, 'f', False))
    return out


# ------------------------------------------------------------------ jugadores

# Boo Fonte: melena castaña lisa con flequillo recto hasta los ojos, un sombrero redondo enorme marrón oscuro detrás y un
# pañuelo azul de lunares blancos anudado en lo alto; ojos grandes dorados y sonrisa
HAT, BLU = _c('#4a342e'), _c('#3c4a8e')
C('boo-fonte', 'chica', P('#6d564b', '#f4bb84', iris='#b08a20', shade='#533a33'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, hairline=False),
  [L(ell(50, 34, 58, 42), HAT, 'b'), L(blob([(22, 12), (50, 4), (78, 12), (82, 22), (50, 16), (18, 22)], 6), BLU, 'b')] +
  bowl3('front', top=6, side=104, fringe=66) + [L(blob([(8, 26), (50, 14), (92, 26), (92, 34), (50, 24), (8, 34)], 6), BLU, 'f')] +
  bow_knot(50, 8, BLU, WHITE, 1.1),
  [L(ell(44, 30, 54, 20), HAT, 'b')] + bowl3('side', top=6, nape=104, fringe=64) + [L(blob([(10, 28), (50, 14), (90, 20), (90, 28), (50, 22), (10, 36)], 6), BLU, 'f'),
                                                                                   L(ell(46, 10, 8, 6), BLU, 'f')],
  [L(ell(50, 34, 58, 42), HAT, 'b')] + bowl3('back', top=6, nape=106) + [L(blob([(6, 30), (50, 20), (94, 30), (94, 38), (50, 28), (6, 38)], 6), BLU, 'f')] +
  bow_knot(50, 12, BLU, WHITE, 1.0))

# Bowan Arras: pelo azul petróleo oscuro con una coleta alta larguísima atada con una goma morada, un mechón largo que le
# cae por el centro de la cara y una cinta blanca en la frente; ojos verdes serios
VIO = _c('#7a3a8a')
def _bowan_pony(view):
    if view == 'side':
        return [L(outline([(36, 8), (20, -6), (2, 0), (-10, 30), (-14, 70, 1), (0, 40), (8, 20), (28, 18)])), L(ell(30, 8, 6, 6), VIO, 'f')]
    if view == 'back':
        return [L(outline([(42, 4), (58, 4), (62, 40), (58, 90), (50, 112, 1), (42, 90), (38, 40)])), L(ell(50, 6, 7, 6), VIO, 'f')]
    return [L(outline([(74, 10), (92, 0), (104, 30), (98, 80, 1), (94, 40), (84, 24)]), 'mid', 'b'), L(ell(78, 10, 6, 5), VIO, 'f')]
C('bowan-arras', 'chica', P('#39556d', '#f5f0dd', iris='#3a6a5a', shade='#2f3743'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=93, hairline=hl(5, 64, 50, 60, jit=2, seed=21)),
  _bowan_pony('front') + dome('front', top=4, w=46, cy=46, n=5, amp=8, sweep=0.3, seed=21, sb=74) +
  [band('front', WHITE, 50, 7), fl([(44, 46), (54, 44), (56, 66), (50, 92, 1), (46, 66)])],
  _bowan_pony('side') + dome('side', top=4, w=46, cy=46, n=5, amp=8, sweep=0.3, seed=21, nape=82, fr=52) + [band('side', WHITE, 50, 7)],
  dome('back', top=4, w=46, cy=46, n=5, amp=8, sweep=0.3, seed=21, nape=82) + _bowan_pony('back') + [band('back', WHITE, 50, 7)])

# Boyle Egg-Egger: cabeza de huevo: la cáscara rota de color crema con manchas pastel le cubre lo alto, pelo verde a los
# lados hasta una perilla verde, cara morena enorme, orejas redondas, ojos de anillo verde, narizota y boca de pato abierta
SHL, GRN, GRD = _c('#ece2cc'), _c('#5a7a3e'), _c('#3e5a2a')
def _shell(view):
    zig = [(14, 34), (22, 28), (28, 36), (36, 26), (44, 34), (52, 24), (60, 34), (68, 26), (76, 36), (82, 28), (88, 34)]
    if view == 'front':
        return [L(outline([(16, 40), (14, 22), (28, 4), (50, -4), (72, 4), (86, 22), (84, 40)]) , SHL, 'f'),
                L(zig + [(88, 40), (12, 40)], SHL, 'f', False),
                L(ell(34, 14, 4, 3), _c('#f0b8c8'), 'f', False), L(ell(62, 8, 4, 3), _c('#a8d8f0'), 'f', False), L(ell(56, 22, 3, 2.4), _c('#f8e08a'), 'f', False)]
    if view == 'side':
        return [L(outline([(14, 40), (12, 18), (32, 0), (56, -4), (80, 6), (90, 24), (88, 40)]), SHL, 'f'), L(ell(50, 12, 4, 3), _c('#a8d8f0'), 'f', False)]
    return [L(outline([(14, 42), (12, 20), (28, 2), (50, -4), (72, 2), (88, 20), (86, 42)]), SHL, 'f'), L(ell(40, 14, 4, 3), _c('#f0b8c8'), 'f', False)]
C('boyle-egg-egger', 'corpulento', P('#5a7a3e', '#cd9569', iris='#2a2a1a', shade='#3e5a2a'),
  F(eyes='dot', brows=False, mouth='lips', mouth_y=96, mouth_w=8, face_front=face(w=4, chin=106, jaw=4, top=10), face_side=face_side(chin=6, jaw=4), nose=(50, 84, 5.5),
    big_ears=3, ear_out=6, hairline=False),
  [L(outline([(10, 40), (14, 96), (24, 100), (22, 44)]), GRN, 'f'), L(outline([(90, 40), (86, 96), (76, 100), (78, 44)]), GRN, 'f'),
   L(blob([(42, 104), (58, 104), (56, 112), (44, 112)], 4), GRN, 'f'),
   L(ell(36, 75, 7, 6) + [ell(36, 75, 7, 6)[0]], GRD, 'f', False, False, 2.4), L(ell(64, 75, 7, 6) + [ell(64, 75, 7, 6)[0]], GRD, 'f', False, False, 2.4)] + _shell('front'),
  [L(outline([(30, 40), (34, 100), (50, 104), (46, 44)]), GRN, 'f')] + _shell('side'),
  [L(outline([(10, 40), (12, 96), (50, 106), (88, 96), (90, 40)]), GRN, 'b')] + _shell('back'))

# Brane Friese: un gorro enorme de helado de crema en espiral, con rayas rosadas, que le tapa toda la cabeza; asoma un
# mechón castaño en la frente; ojos redondos enormes y sonrisa de oreja a oreja
CRM, CRP = _c('#fcf2dc'), _c('#e8c0b0')
def _ice(view):
    if view == 'side':
        tiers = [(48, 46, 48, 10), (46, 30, 40, 9), (44, 16, 30, 8), (42, 4, 18, 7)]
    else:
        tiers = [(50, 46, 50, 10), (50, 30, 42, 9), (50, 16, 32, 8), (52, 4, 20, 7)]
    out = []
    for cx, cy, rx, ry in tiers:
        out += [L(ell(cx, cy, rx, ry), CRM, 'f'), L(quad((cx - rx * 0.8, cy + 2), (cx, cy + ry * 0.9), (cx + rx * 0.8, cy + 2)), CRP, 'f', False, False, 1.6)]
    out.append(L(outline([(50 if view != 'side' else 40, -14), (58 if view != 'side' else 48, 2), (44 if view != 'side' else 34, 2)]), CRM, 'f'))
    return out
C('brane-friese', 'normal', P('#a87048', '#f4b87f', iris='#1a1414'),
  F(eyes='none', brows=False, mouth='none', mouth_y=92, hairline=False, eye_y=76),
  big_grin(92, 16, 8) + [L(ell(cx, 76, 7.4, 7.4), WHITE, 'f', True) for cx in (35, 65)] + [L(ell(cx, 76, 3.6, 3.8), BLACK, 'f', False) for cx in (35, 65)] + _ice('front') + [fl([(52, 52), (60, 54), (54, 64, 1)])],
  _ice('side'),
  _ice('back'))

# Breeze Flurry-Windward: pelo blanco crema largo y revuelto, echado por el viento hacia un lado con mechones de punta que
# le tapan media frente; ojos rojos afilados y sonrisa pícara
C('breeze-flurry-windward', 'normal', P('#e5e4d7', '#fbd08e', iris='#c8282a', shade='#c5bbad'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=92, hairline=[(6, 64), (16, 48), (28, 56), (36, 44), (50, 54), (62, 42), (78, 48), (94, 66)]),
  dome('front', top=0, w=48, cy=46, n=7, amp=16, sweep=-0.9, seed=31, sb=78) + [fl([(30, 40), (52, 36), (40, 60), (30, 72, 1), (32, 54)])],
  dome('side', top=0, w=48, cy=46, n=7, amp=16, sweep=-0.9, seed=31, nape=90, fr=50),
  dome('back', top=0, w=48, cy=46, n=7, amp=16, sweep=-0.9, seed=31, nape=90))

# Bruno Tanner: pelo corto gris plata con reflejos lilas, piel morena, dos marcas blancas pintadas en las mejillas, ojos
# grandes de pupila pequeña y sonrisa
C('bruno-tanner', 'normal', P('#c4d1d5', '#bc8c6a', iris='#1e1a1a', shade='#a59195'),
  F(eyes='round', brows='angry', mouth='smile', mouth_y=92, hairline=hl(5, 64, 48, 56, jit=2, seed=7)),
  dome('front', top=2, w=47, cy=46, n=6, amp=8, seed=41, sb=72) +
  [mark([(26, 82), (32, 80), (34, 88), (28, 90)], WHITE), mark([(74, 82), (68, 80), (66, 88), (72, 90)], WHITE)],
  dome('side', top=2, w=47, cy=46, n=6, amp=8, seed=41, nape=86, fr=48) + [mark([(76, 82), (82, 80), (82, 88), (76, 88)], WHITE)],
  dome('back', top=2, w=47, cy=46, n=6, amp=8, seed=41, nape=86))

# Brutus Pummel: pinchos rojo oscuro de punta hacia arriba, una cinta ancha verde oliva en la frente, gafas negras de
# montura gruesa con los cristales blancos, narizota, boca torcida y perilla granate
OLV = _c('#756523')
C('brutus-pummel', 'normal', P('#7a1e24', '#f5be93', iris='#1e1a1a'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, nose=(50, 86, 3.6), hairline=False),
  dome('front', top=-6, w=48, cy=46, n=7, amp=16, sweep=-0.3, seed=51, sb=64) +
  [band('front', OLV, 50, 13), L(blob([(42, 104), (58, 104), (54, 112), (46, 112)], 4), 'deep', 'f')] + lens_rect('front', BLACK, WHITE, 74, 15, 10, 5),
  dome('side', top=-6, w=48, cy=46, n=7, amp=16, sweep=-0.3, seed=51, nape=84, fr=46) + [band('side', OLV, 50, 13)] + lens_rect('side', BLACK, WHITE, 74),
  dome('back', top=-6, w=48, cy=46, n=7, amp=16, sweep=-0.3, seed=51, nape=84) + [band('back', OLV, 50, 13)])

# Buck Choy: pelo verde oliva en forma de col china: una masa ancha y plana arriba, más estrecha abajo, con una muesca en
# medio; cara enorme pálida, ojos entornados de mala uva, naricita verde y dientes apretados
C('buck-choy', 'corpulento', P('#a8a777', '#fdeab7', iris='#3a3a2a', nose='#9ab060'),
  F(eyes='sharp', brows=False, mouth='grin', mouth_y=98, face_front=face(w=8, chin=108, jaw=6), face_side=face_side(chin=8, jaw=6), nose=(50, 84, 3), ear_out=6,
    hairline=[(6, 58), (14, 50), (50, 52), (86, 50), (94, 58)]),
  [L(outline([(16, 62), (4, 18), (20, 6), (44, 8), (50, 16, 1), (56, 8), (80, 6), (96, 18), (84, 62), (50, 56)])),
   L(outline([(58, 10), (80, 8), (94, 20), (82, 58), (66, 40)]), 'shade', 'b', False)],
  [L(outline([(56, 60), (64, 50), (88, 50), (98, 18), (78, 4), (40, 4), (12, 14), (6, 40), (12, 70), (30, 76), (50, 62)])),
   L(outline([(8, 30), (30, 36), (40, 60), (28, 74), (12, 68)]), 'shade', 'b', False)],
  [L(outline([(16, 70), (4, 18), (20, 6), (50, 6), (80, 6), (96, 18), (84, 70), (50, 76)])),
   L(outline([(58, 10), (80, 8), (94, 20), (82, 68), (64, 60)]), 'shade', 'b', False)])

# Buddy "Muscles" Arnolds (portero): pelo engominado hacia atrás, castaño oscuro y largo hasta la mandíbula por un lado y
# amarillo a rayas por el otro; gafas de visera amarillas, piel morena y dientes apretados
YLW = _c('#e8b030')
C('buddy-muscles-arnolds', 'corpulento', P('#65534f', '#d49d56', iris='#1e1a1a', shade='#4a3e38'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=96, face_front=face(w=4, chin=104, jaw=3), nose=(50, 86, 3), hairline=[(6, 70), (14, 52), (30, 42), (50, 38), (70, 42), (86, 50), (94, 66)]),
  [L(outline([(8, 104), (4, 60), (12, 24), (30, 8), (50, 4), (52, 46), (24, 50), (20, 104)])),
   L(outline([(50, 4), (72, 8), (88, 22), (92, 50), (84, 52), (54, 46)]), YLW, 'b'),
   L([(56, 14), (84, 30)], _c('#c88a1a'), 'b', False, False, 1.6), L([(54, 26), (88, 40)], _c('#c88a1a'), 'b', False, False, 1.6),
   L(blob([(20, 70), (48, 68), (52, 72), (80, 68), (82, 74), (52, 78), (48, 78), (22, 76)], 4), YLW, 'f', True, True)],
  [L(outline([(56, 52), (70, 42), (84, 40), (88, 20), (70, 4), (40, 2), (14, 14), (4, 40), (8, 70), (24, 82), (44, 78), (52, 62)]), YLW),
   L(blob([(70, 70), (90, 68), (90, 74), (72, 76)], 4), YLW, 'f', True, True), L([(70, 72), (46, 70)], YLW, 'f', False, False, 2.4)],
  [L(outline([(8, 100), (4, 60), (12, 24), (30, 8), (50, 4), (50, 86), (14, 96)])),
   L(outline([(50, 4), (70, 8), (88, 22), (96, 60), (88, 84), (50, 86)]), YLW)])

# Burt Zerka: un tupé de pinchos rojo oscuro en lo alto y una melena roja enorme y erizada que le abulta a los lados de la
# cara, con las sienes azul marino; pintura negra de kabuki alrededor de los ojos y ceño muy fruncido
NAV = _c('#3e3a4c')
C('burt-zerka', 'normal', P('#8c1425', '#fcd08c', iris='#1e1a1a', shade='#6a171e'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, face_front=face(w=4, chin=104, jaw=2), nose=(50, 85, 2.4),
    hairline=[(6, 62), (16, 50), (30, 44), (50, 42), (70, 44), (84, 50), (94, 62)]),
  [L(outline([(16, 110), (-10, 100, 1), (2, 88), (-12, 74, 1), (4, 66), (12, 60), (88, 60), (96, 66), (112, 74, 1), (98, 88), (110, 100, 1), (84, 110), (82, 76), (18, 76)])),
   L(outline([(12, 56), (10, 30), (28, 14), (72, 14), (90, 30), (88, 56)]), NAV),
   L(outline([(24, 30), (26, 8), (34, -12, 1), (44, 2), (54, -16, 1), (60, 2), (74, -8, 1), (72, 12), (78, 30), (50, 26)])),
   L(outline([(54, -16), (60, 2), (74, -8), (72, 12), (78, 30), (62, 22)]), 'shade', 'b', False)] +
  kabuki(BLACK, iris=BLACK) + [L([(24, 60), (44, 68)], BLACK, 'f', False, False, 4.6), L([(76, 60), (56, 68)], BLACK, 'f', False, False, 4.6)],
  [L(outline([(52, 80), (40, 104), (14, 100, 1), (8, 82), (-10, 72, 1), (6, 56), (24, 50), (50, 56)])),
   L(outline([(52, 56), (60, 44), (82, 40), (88, 26), (70, 12), (40, 10), (16, 22), (8, 44), (26, 54)]), NAV),
   L(outline([(30, 24), (34, 2), (44, -14, 1), (54, 2), (66, -10, 1), (70, 8), (84, 4, 1), (82, 22), (56, 26)])),
   L(blob([(74, 74), (88, 70), (90, 78), (78, 84)], 4), BLACK, 'f', False), L([(72, 62), (88, 66)], BLACK, 'f', False, False, 4)],
  [L(outline([(10, 110), (-10, 96, 1), (2, 80), (-12, 64, 1), (4, 50), (12, 30), (30, 14), (70, 14), (88, 30), (96, 50), (112, 64, 1), (98, 80), (110, 96, 1), (90, 110),
              (50, 116)])),
   L(outline([(24, 30), (26, 8), (34, -12, 1), (44, 2), (54, -16, 1), (60, 2), (74, -8, 1), (72, 12), (78, 30), (50, 26)])),
   L(outline([(56, 20), (80, 30), (94, 60), (96, 100), (76, 108), (70, 60)]), 'shade', 'b', False)])

# Buzz "Beanie" Cutt (defensa): gorra azul grisácea de rayas blancas con orejeras, calada hasta un ojo, y un parche negro
# redondo en el otro; cara ancha y morena, boca apretada en mueca
CAP, CPW = _c('#57768f'), _c('#e8eef0')
def _beanie_cutt(view):
    if view == 'front':
        return [L(outline([(10, 64), (6, 20), (8, 8), (20, 12), (50, 4), (80, 12), (92, 8), (94, 20), (90, 64), (50, 70)]), CAP, 'f'),
                L(blob([(8, 30), (50, 22), (92, 30), (92, 38), (50, 30), (8, 38)], 6), CPW, 'f', False),
                L(blob([(9, 46), (50, 38), (91, 46), (91, 54), (50, 46), (9, 54)], 6), CPW, 'f', False),
                L(ell(64, 76, 8, 7), BLACK, 'f', True), L(ell(64, 76, 4, 3.4), (200, 200, 200, 255), 'f', False)]
    if view == 'side':
        return [L(outline([(10, 74), (2, 40), (16, 10), (50, 2), (80, 10), (94, 36), (96, 62), (60, 64), (30, 74)]), CAP, 'f'),
                L(blob([(4, 34), (50, 24), (94, 30), (94, 38), (50, 32), (4, 42)], 6), CPW, 'f', False),
                L(blob([(4, 52), (50, 42), (95, 48), (95, 56), (50, 50), (6, 60)], 6), CPW, 'f', False)]
    return [L(outline([(8, 76), (6, 20), (8, 8), (20, 12), (50, 4), (80, 12), (92, 8), (94, 20), (92, 76), (50, 82)]), CAP, 'f'),
            L(blob([(6, 32), (50, 24), (94, 32), (94, 40), (50, 32), (6, 40)], 6), CPW, 'f', False),
            L(blob([(6, 50), (50, 42), (94, 50), (94, 58), (50, 50), (6, 58)], 6), CPW, 'f', False)]
C('buzz-beanie-cutt', 'corpulento', P('#3c393a', '#bd8d6a', iris='#1e1a1a'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=98, face_front=face(w=6, chin=106, jaw=5), face_side=face_side(chin=6, jaw=5), nose=(50, 86, 3), hairline=False),
  [L(ell(36, 76, 3, 3.4), BLACK, 'f', False)] + _beanie_cutt('front'),
  _beanie_cutt('side'),
  _beanie_cutt('back'))

# Buzz O'Hare: melena negra lisa hasta el cuello que le tapa media cara, con un mechón gris en el otro lado; piel morena,
# un solo ojo a la vista, afilado, y boca torcida
GRY = _c('#8a8580')
C('buzz-o-hare', 'delgado', P('#3f414c', '#bd8e6c', iris='#e8e0c0', shade='#2a2527'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, face_front=face(chin=106), face_side=face_side(chin=6), hairline=[(6, 70), (20, 50), (40, 42), (62, 42), (80, 50), (94, 70)]),
  [L(outline([(6, 112), (2, 60), (10, 24), (30, 6), (52, 2), (74, 8), (90, 26), (96, 60), (92, 112), (84, 108), (82, 60), (18, 60), (16, 112)])),
   L(outline([(72, 10), (88, 24), (94, 56), (90, 96), (84, 90), (84, 52), (78, 28)]), GRY, 'b'),
   fl([(18, 40), (40, 30), (56, 34), (54, 70), (46, 96), (40, 112, 1), (32, 96), (24, 70)])],
  [L(outline([(58, 60), (64, 46), (82, 40), (86, 24), (66, 4), (36, 2), (12, 14), (2, 44), (4, 112), (20, 112), (32, 84), (46, 80), (54, 70)]))],
  [L(outline([(6, 112), (2, 60), (10, 24), (30, 6), (52, 2), (74, 8), (90, 26), (96, 60), (94, 112), (50, 116)])),
   L(outline([(70, 8), (90, 26), (96, 60), (94, 110), (76, 112), (80, 50)]), GRY, 'b')])

# Byrd Stryke (defensa): melena corta revuelta rosa salmón, con mechones de punta que le caen por la frente y se abren a
# los lados del cuello; ojos grandes lilas y sonrisa
C('byrd-stryke', 'normal', P('#d28071', '#fccfa1', iris='#7a5aa8', shade='#9d5f55'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 62), (18, 58), (26, 70), (34, 52), (44, 66), (52, 50), (62, 64), (72, 52), (82, 62), (94, 62)]),
  dome('front', top=2, w=48, cy=46, n=6, amp=6, seed=61, long=96, flare=8) ,
  dome('side', top=2, w=48, cy=46, n=6, amp=6, seed=61, long=96, flare=8, fr=56),
  dome('back', top=2, w=48, cy=46, n=6, amp=6, seed=61, long=96, flare=8, ends=4))

# Caetano Settler: pelo castaño casi negro corto, revuelto con pinchos arriba; piel morena, dos marcas rojas en una
# mejilla, ojos afilados y boca de enfado
C('caetano-settler', 'normal', P('#3e3a36', '#bc8e6d', iris='#1e1a1a', shade='#2a2622'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=hl(6, 64, 48, 58, jit=3, seed=9)),
  dome('front', top=-2, w=48, cy=46, n=8, amp=12, sweep=0.2, seed=71, sb=72) +
  [L([(22, 84), (30, 80)], _c('#b8382a'), 'f', False, False, 1.8), L([(22, 88), (30, 84)], _c('#b8382a'), 'f', False, False, 1.8)],
  dome('side', top=-2, w=48, cy=46, n=8, amp=12, sweep=0.2, seed=71, nape=86, fr=48),
  dome('back', top=-2, w=48, cy=46, n=8, amp=12, sweep=0.2, seed=71, nape=86))

# Cain Cavalier: chistera blanca con una cinta roja, melena corta roja en casco que le tapa la frente y un círculo morado
# pintado alrededor de un ojo; ojo rosa y sonrisa
def _tophat(view, x=50):
    if view == 'side':
        return [L(ell(46, 20, 54, 10), WHITE, 'f'), L(outline([(20, 18), (24, -30), (72, -30), (74, 16)]), WHITE, 'f', True, True),
                L(outline([(22, 6), (74, 6), (74, 16), (22, 18)]), RED, 'f', False)]
    return [L(ell(50, 20, 52, 12), WHITE, 'f'), L(outline([(20, 16), (22, -32), (78, -32), (80, 16)]), WHITE, 'f', True, True),
            L(outline([(21, 2), (79, 2), (80, 14), (20, 14)]), RED, 'f', False), L(ell(50, -32, 28, 5), _c('#dadada'), 'f', False)]
C('cain-cavalier', 'normal', P('#c8302a', '#f8d6b7', iris='#c86a9a', shade='#882927'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, hairline=[(6, 70), (18, 54), (40, 52), (60, 50), (82, 54), (94, 70)]),
  bowl3('front', top=10, side=98, fringe=56) + [L(ell(36, 76, 9, 9), _c('#9a5aa0'), 'f', False), L(ell(36, 76, 4.4, 5), WHITE, 'f', False),
                                               L(ell(36, 77, 2.6, 3), _c('#c86a9a'), 'f', False)] + _tophat('front'),
  bowl3('side', top=10, nape=98, fringe=56) + _tophat('side'),
  bowl3('back', top=10, nape=98) + _tophat('back'))

# Calla de Wild: pelo rojo anaranjado con mechones de punta en la frente y una trenza gruesa que le cae por un hombro,
# atada con un aro dorado; ojos verdes afilados, pecas y sonrisa
GLD = _c('#d8a830')
C('calla-de-wild', 'chica', P('#cb5941', '#f5dbbb', iris='#4a8a3a', shade='#a54834'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=92, hairline=[(6, 64), (16, 50), (30, 58), (40, 46), (54, 56), (66, 46), (80, 54), (94, 62)]),
  dome('front', top=2, w=47, cy=46, n=5, amp=10, sweep=0.4, seed=81, sb=72) +
  [L(outline([(80, 60), (94, 70), (92, 96), (84, 112), (74, 118, 1), (76, 100), (78, 80)])), L(ell(80, 104, 6, 4), GLD, 'f')] + freckles(84, 22),
  dome('side', top=2, w=47, cy=46, n=5, amp=10, sweep=0.4, seed=81, nape=86, fr=50),
  dome('back', top=2, w=47, cy=46, n=5, amp=10, sweep=0.4, seed=81, nape=86) +
  [L(outline([(14, 70), (24, 74), (22, 100), (14, 116, 1), (10, 100)])), L(ell(18, 104, 6, 4), GLD, 'f')])

# Callum "Croc" Rocke: gorro verde oscuro calado con un zigzag rojo, pelo blanco de punta que le sale por los lados en
# mechones afilados; piel tostada, ojos rojos afilados y boca de enfado
CGR = _c('#44623a')
def _croc_hat(view):
    zz = [(10, 34), (22, 24), (32, 34), (44, 22), (56, 34), (68, 22), (78, 34), (90, 26)]
    if view == 'front':
        return [cap('front', CGR, top=-2, rim=48, w=48, z='f', ln=True), L(zz, RED, 'f', False, False, 2.4)]
    if view == 'side':
        return [cap('side', CGR, top=-2, rim=48, w=48, z='f', ln=True), L([(4, 36), (20, 26), (36, 36), (52, 24), (68, 34), (90, 24)], RED, 'f', False, False, 2.4)]
    return [cap('back', CGR, top=-2, rim=48, w=48, z='f', ln=True), L(zz, RED, 'f', False, False, 2.4)]
C('callum-croc-rocke', 'normal', P('#e3ddd3', '#eba662', iris='#b8281e', shade='#c0b8ac'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 62), (18, 54), (28, 66), (36, 52), (46, 64), (54, 52), (64, 66), (72, 52), (82, 64), (94, 62)]),
  [L(outline([(16, 50), (2, 64, 1), (12, 70), (0, 84, 1), (14, 86), (8, 100, 1), (20, 92), (22, 60), (78, 60), (80, 92), (92, 100, 1), (86, 86), (100, 84, 1), (88, 70),
              (98, 64, 1), (84, 50)])), L(outline([(14, 46), (86, 46), (86, 60), (14, 60)]))] + _croc_hat('front'),
  [L(outline([(54, 60), (40, 70), (20, 66, 1), (28, 78), (10, 82, 1), (26, 88), (16, 100, 1), (34, 92), (46, 80), (8, 60), (4, 40), (90, 40), (90, 54), (64, 50)]))] +
  _croc_hat('side'),
  [L(outline([(8, 50), (0, 66, 1), (10, 70), (2, 86, 1), (16, 86), (14, 100, 1), (30, 92), (50, 96, 1), (70, 92), (86, 100, 1), (84, 86), (98, 86, 1), (90, 70),
              (100, 66, 1), (92, 50)]))] + _croc_hat('back'))

# Camille Aeon (defensa): un gorro verde en forma de hoja que baja en punta hasta la nariz y le tapa los ojos tras un
# antifaz verde claro; mechones azul oscuro de punta a los lados; boca grande de disgusto
LGR, DGR = _c('#5f9351'), _c('#d8e070')
def _leaf(view):
    if view == 'front':
        return [L(outline([(8, 60), (6, 30), (24, 6), (50, -2), (76, 6), (94, 30), (92, 60), (64, 70), (50, 92, 1), (36, 70)]), LGR, 'f', True, True),
                L(blob([(26, 72), (40, 70), (46, 78), (40, 84), (26, 82)], 4), DGR, 'f', True), L(blob([(74, 72), (60, 70), (54, 78), (60, 84), (74, 82)], 4), DGR, 'f', True),
                L([(50, -2), (50, 88)], _c('#3e6a34'), 'f', False, False, 1.2)]
    if view == 'side':
        return [L(outline([(10, 70), (2, 40), (20, 8), (50, -2), (80, 10), (94, 40), (98, 70), (92, 92, 1), (80, 72), (60, 64), (40, 70)]), LGR, 'f', True, True),
                L(blob([(78, 72), (90, 70), (92, 80), (80, 82)], 4), DGR, 'f', True)]
    return [L(outline([(8, 72), (6, 30), (24, 6), (50, -2), (76, 6), (94, 30), (92, 72), (50, 80)]), LGR, 'f', True, True), L([(50, -2), (50, 78)], _c('#3e6a34'), 'f', False, False, 1.2)]
C('camille-aeon', 'normal', P('#2e3a5a', '#eed6b2', iris='#1e1a1a'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, face_front=face(w=4, chin=104, jaw=3), hairline=False),
  [L(outline([(10, 60), (-6, 66, 1), (8, 74), (-4, 82, 1), (12, 80), (16, 64)])), L(outline([(90, 60), (106, 66, 1), (92, 74), (104, 82, 1), (88, 80), (84, 64)]))] +
  _leaf('front') + [L(quad((38, 96), (50, 92), (62, 96)), OUTC, 'f', False, False, 1.6)],
  [L(outline([(16, 64), (0, 74, 1), (14, 80), (2, 90, 1), (20, 88), (30, 70)]))] + _leaf('side'),
  _leaf('back') + [L(outline([(10, 66), (-6, 74, 1), (10, 80), (90, 80), (106, 74, 1), (90, 66)]))])

# Capro Lynes: pelo celeste claro altísimo que sube en dos picos como llamas y un mechón largo que le cae por el centro de
# la cara; piel morena, rayas blancas pintadas en las mejillas, ojos amarillos y dientes apretados
C('capro-lynes', 'normal', P('#d2f9fd', '#bb8d6c', iris='#c8a020', shade='#b8d1d2'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=96, face_front=face(chin=104), hairline=[(6, 62), (18, 46), (34, 52), (50, 44), (66, 52), (82, 46), (94, 62)]),
  [L(outline([(14, 62), (8, 30), (0, -30, 1), (26, 10), (50, 20), (74, 10), (100, -30, 1), (92, 30), (86, 62), (80, 50), (20, 50)])),
   L(outline([(60, 16), (74, 10), (100, -30), (92, 30), (86, 58), (78, 34)]), 'shade', 'b', False),
   fl([(42, 40), (58, 40), (56, 70), (50, 96, 1), (44, 70)]),
   L([(22, 82), (32, 86)], WHITE, 'f', False, False, 2), L([(22, 88), (32, 92)], WHITE, 'f', False, False, 2),
   L([(78, 82), (68, 86)], WHITE, 'f', False, False, 2), L([(78, 88), (68, 92)], WHITE, 'f', False, False, 2)],
  [L(outline([(56, 58), (64, 46), (84, 42), (96, 20), (94, -30, 1), (70, 0), (40, 4), (6, -24, 1), (10, 20), (4, 50), (18, 74), (40, 74), (50, 64)])),
   L([(76, 84), (86, 86)], WHITE, 'f', False, False, 2)],
  [L(outline([(14, 74), (8, 30), (0, -30, 1), (26, 10), (50, 20), (74, 10), (100, -30, 1), (92, 30), (86, 74), (50, 82)])),
   L(outline([(60, 16), (74, 10), (100, -30), (92, 30), (86, 72), (70, 60)]), 'shade', 'b', False)])

# Captain Jokar: casco negro que le tapa toda la cabeza, con una franja amarilla que baja en Y hasta la mandíbula y dos ojos
# rojos brillantes; una bufanda roja deshilachada alrededor del cuello que sube en dos puntas como cuernos
JK, JY, JR = _c('#343038'), _c('#ddc734'), _c('#a3392e')
def _jokar(view):
    if view == 'front':
        return [L(outline([(50, 110), (14, 96), (-6, 70), (2, 20, 1), (12, 60), (30, 90)]), JR, 'b'), L(outline([(50, 110), (86, 96), (106, 70), (98, 20, 1), (88, 60), (70, 90)]), JR, 'b'),
                L(outline([(12, 70), (10, 30), (26, 8), (50, 2), (74, 8), (90, 30), (88, 70), (76, 96), (50, 104), (24, 96)]), JK, 'f', True),
                L(outline([(56, 8), (70, 12), (60, 50), (78, 88), (66, 98), (50, 104), (34, 98), (24, 88), (50, 56)]), JY, 'f', False),
                L(blob([(24, 70), (40, 70), (44, 80), (30, 82)], 4), _c('#e8201a'), 'f', False), L(blob([(76, 70), (60, 70), (56, 80), (70, 82)], 4), _c('#e8201a'), 'f', False),
                L(blob([(10, 98), (50, 104), (90, 98), (94, 112), (50, 118), (6, 112)], 6), JR, 'f')]
    if view == 'side':
        return [L(outline([(30, 104), (8, 88), (-4, 40, 1), (14, 70), (40, 96)]), JR, 'b'),
                L(outline([(14, 80), (6, 40), (24, 8), (52, 2), (80, 12), (92, 40), (92, 80), (78, 100), (40, 100)]), JK, 'f', True),
                L(outline([(70, 12), (82, 20), (78, 56), (90, 90), (74, 100), (60, 60)]), JY, 'f', False),
                L(blob([(76, 70), (90, 70), (90, 80), (80, 82)], 4), _c('#e8201a'), 'f', False),
                L(blob([(20, 98), (60, 96), (90, 98), (92, 112), (50, 116), (16, 112)], 6), JR, 'f')]
    return [L(outline([(12, 70), (10, 30), (26, 8), (50, 2), (74, 8), (90, 30), (88, 70), (76, 96), (50, 104), (24, 96)]), JK, 'f', True),
            L(outline([(14, 96), (-4, 70), (2, 24, 1), (14, 64), (40, 98)]), JR, 'f'), L(outline([(86, 96), (104, 70), (98, 24, 1), (86, 64), (60, 98)]), JR, 'f'),
            L(blob([(8, 98), (50, 102), (92, 98), (94, 112), (50, 118), (6, 112)], 6), JR, 'f')]
C('captain-jokar', 'normal', P('#343038', '#cfa080', iris='#e8201a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _jokar('front'), _jokar('side'), _jokar('back'))

# Cara Mass (defensa): pelo azul recogido en un turbante de mechones enrollados que acaba a los lados en dos rizos enormes
# hacia arriba; ojos cerrados con pestañas largas y boquita con dos dientes
C('cara-mass', 'chica', P('#5d8daf', '#fcf2dd', iris='#1e1a1a', shade='#4c6e8a'),
  F(eyes='closed', brows=False, mouth='buck', mouth_y=94, hairline=[(6, 66), (20, 50), (50, 44), (80, 50), (94, 66)]),
  [L(outline([(16, 60), (12, 30), (28, 8), (50, 2), (72, 8), (88, 30), (84, 60), (50, 54)])),
   L(outline([(16, 52), (0, 54), (-8, 42, 1), (2, 64), (16, 66)])), L(outline([(84, 52), (100, 54), (108, 42, 1), (98, 64), (84, 66)])),
   strand([(20, 40), (50, 30), (82, 22)], 'shade', 'b', 1.4), strand([(18, 50), (50, 40), (84, 36)], 'shade', 'b', 1.4)] +
  [L([(28 + i * 3, 78), (24 + i * 4, 84)], OUTC, 'f', False, False, 1.2) for i in range(4)] + [L([(72 - i * 3, 78), (76 - i * 4, 84)], OUTC, 'f', False, False, 1.2) for i in range(4)],
  [L(outline([(56, 54), (66, 46), (86, 42), (88, 22), (68, 4), (40, 2), (14, 14), (4, 40), (12, 70), (30, 74), (48, 64)])),
   L(outline([(24, 56), (6, 58), (-4, 46, 1), (4, 68), (26, 70)])), strand([(10, 40), (50, 26), (86, 26)], 'shade', 'b', 1.4)],
  [L(outline([(16, 70), (12, 30), (28, 8), (50, 2), (72, 8), (88, 30), (84, 70), (50, 76)])),
   L(outline([(16, 56), (0, 58), (-8, 46, 1), (2, 68), (16, 70)])), L(outline([(84, 56), (100, 58), (108, 46, 1), (98, 68), (84, 70)])),
   strand([(20, 40), (50, 30), (82, 22)], 'shade', 'b', 1.4), strand([(18, 54), (50, 44), (84, 40)], 'shade', 'b', 1.4)])

# Carey Noakie: dos cuernos enormes de pelo enroscado hacia arriba, castaño oscuro uno y blanco el otro (el pelo, partido en
# dos colores); cara pálida y larga, ojos afilados, nariz larga y boca de enfado
CWH = _c('#f0ece1')
C('carey-noakie', 'delgado', P('#44302d', '#fef0d4', iris='#4a6a9a', shade='#312320'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=98, face_front=face(chin=110, top=20), face_side=face_side(chin=8), nose=(50, 88, 1.6),
    hairline=[(6, 58), (20, 44), (50, 38), (80, 44), (94, 58)]),
  [L(outline([(50, 40), (16, 46), (12, 30), (2, 20), (-6, 4), (6, -4), (24, 4), (30, 18), (50, 22)])),
   L(outline([(50, 40), (84, 46), (88, 30), (98, 20), (106, 4), (94, -4), (76, 4), (70, 18), (50, 22)]), CWH),
   L(ell(8, 6, 7, 6), 'deep', 'b'), L(ell(92, 6, 7, 6), _c('#d8d0c4'), 'b')],
  [L(outline([(54, 46), (60, 40), (80, 38), (84, 22), (98, 10), (100, -6), (84, -6), (70, 10), (40, 12), (16, 22), (8, 44), (20, 64), (40, 60)]), CWH)],
  [L(outline([(50, 70), (14, 64), (12, 30), (2, 20), (-6, 4), (6, -4), (24, 4), (30, 18), (50, 22)]), CWH),
   L(outline([(50, 70), (86, 64), (88, 30), (98, 20), (106, 4), (94, -4), (76, 4), (70, 18), (50, 22)]))])

# Carny Voris (defensa): cabeza calva morena, cejas castañas gruesas fruncidas, ojos pequeños en ojeras claras, nariz
# naranja y un hueso atravesado en la boca
BONE = _c('#f0e6d4')
def _bone(view):
    if view == 'front':
        return [L(outline([(14, 92), (20, 86), (80, 86), (86, 92), (86, 100), (80, 104), (20, 104), (14, 100)]), BONE, 'f'),
                L(ell(10, 90, 6, 6), BONE, 'f'), L(ell(10, 102, 6, 6), BONE, 'f'), L(ell(90, 90, 6, 6), BONE, 'f'), L(ell(90, 102, 6, 6), BONE, 'f')]
    return [L(outline([(64, 90), (98, 88), (100, 100), (66, 100)]), BONE, 'f'), L(ell(100, 90, 6, 5), BONE, 'f'), L(ell(100, 100, 6, 5), BONE, 'f')]
C('carny-voris', 'corpulento', P('#6d3a12', '#ae8861', iris='#1e1a1a', nose='#e07030'),
  F(eyes='dot', brows=False, mouth='none', face_front=face(w=6, chin=108, jaw=5, top=12), face_side=face_side(chin=6, jaw=4), nose=(50, 84, 5), big_ears=2, ear_out=4,
    hairline=False),
  skull3('front') + [L(blob([(24, 70), (44, 68), (46, 82), (26, 84)], 4), _c('#d0c8bc'), 'f', False), L(blob([(76, 70), (56, 68), (54, 82), (74, 84)], 4), _c('#d0c8bc'), 'f', False),
                     L(blob([(20, 64), (32, 58), (46, 64), (44, 70), (24, 70)], 4), 'mid', 'f'), L(blob([(80, 64), (68, 58), (54, 64), (56, 70), (76, 70)], 4), 'mid', 'f'),
                     L(ell(35, 76, 2.4, 2.8), BLACK, 'f', False), L(ell(65, 76, 2.4, 2.8), BLACK, 'f', False)] + _bone('front') +
  [L(quad((40, 108), (50, 104), (60, 108)), OUTC, 'f', False, False, 1.6)],
  skull3('side') + [L(blob([(70, 64), (88, 62), (88, 68), (72, 70)], 4), 'mid', 'f')] + _bone('side'),
  skull3('back'))

# Carter Spaid: casco rojo de luchador con un corazón naranja que le tapa los ojos y baja en punta por la nariz, franjas
# claras en las sienes y un pañuelo blanco atado que ondea detrás; sonrisa de dientes
CRR, CRO = _c('#b62b20'), _c('#dc5006')
def _spade(view):
    if view == 'front':
        return [L(outline([(10, 74), (8, 30), (26, 6), (50, 0), (74, 6), (92, 30), (90, 74), (70, 80), (50, 90, 1), (30, 80)]), CRR, 'f', True),
                L(outline([(50, 40), (38, 30), (24, 40), (26, 60), (50, 86, 1), (74, 60), (76, 40), (62, 30)]), CRO, 'f', False),
                L(outline([(14, 50), (22, 30), (34, 16), (28, 36), (22, 60)]), _c('#f0d8c8'), 'f', False), L(outline([(86, 50), (78, 30), (66, 16), (72, 36), (78, 60)]), _c('#f0d8c8'), 'f', False),
                L(outline([(4, 54), (-8, 30), (2, 26), (14, 46)]), _c('#f4ece4'), 'b')]
    if view == 'side':
        return [L(outline([(10, 80), (4, 40), (22, 8), (52, 0), (80, 10), (94, 40), (94, 70), (82, 82), (40, 82)]), CRR, 'f', True),
                L(outline([(70, 40), (90, 44), (92, 70), (84, 84, 1), (74, 66)]), CRO, 'f', False),
                L(outline([(14, 60), (-14, 40, 1), (-6, 60), (-18, 76, 1), (12, 70)]), _c('#f4ece4'), 'f')]
    return [L(outline([(10, 80), (8, 30), (26, 6), (50, 0), (74, 6), (92, 30), (90, 80), (50, 86)]), CRR, 'f', True),
            L(outline([(40, 60), (20, 70, 1), (30, 84), (50, 66), (70, 84), (80, 70, 1), (60, 60)]), _c('#f4ece4'), 'f')]
C('carter-spaid', 'normal', P('#392b28', '#ca936e', iris='#1e1a1a'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=96, hairline=False),
  _spade('front'), _spade('side'), _spade('back'))

# Casey "Bagworm" Moth (portero): la cabeza entera envuelta en vendas color crema, salvo un ojo rojo; mechones negros
# largos y de punta salen por todos lados entre las vendas, como patas
BND = _c('#ecdcc1')
def _wrap(view):
    if view == 'front':
        return [L(outline([(14, 90), (8, 40), (24, 10), (50, 2), (76, 10), (92, 40), (88, 84), (70, 90), (50, 86), (30, 92)]), BND, 'f', True),
                strand([(14, 40), (50, 30), (88, 46)], _c('#c8b090'), 'f', 1.2), strand([(10, 60), (40, 64), (90, 60)], _c('#c8b090'), 'f', 1.2),
                strand([(14, 82), (50, 78), (88, 80)], _c('#c8b090'), 'f', 1.2),
                L(blob([(54, 68), (72, 66), (74, 82), (56, 84)], 4), _c('#ca8a5a'), 'f', False), L(ell(64, 75, 5, 5), WHITE, 'f', False), L(ell(64, 75, 3.4, 3.4), _c('#c8201e'), 'f', False),
                L(ell(64, 75, 1.4, 1.4), BLACK, 'f', False)]
    if view == 'side':
        return [L(outline([(10, 96), (4, 40), (22, 8), (52, 0), (80, 10), (94, 40), (94, 82), (70, 86), (40, 100)]), BND, 'f', True),
                strand([(8, 40), (50, 28), (92, 40)], _c('#c8b090'), 'f', 1.2), strand([(6, 70), (50, 64), (94, 66)], _c('#c8b090'), 'f', 1.2)]
    return [L(outline([(12, 96), (8, 40), (24, 10), (50, 2), (76, 10), (92, 40), (88, 96), (50, 104)]), BND, 'f', True),
            strand([(12, 44), (50, 34), (88, 44)], _c('#c8b090'), 'f', 1.2), strand([(10, 72), (50, 66), (90, 72)], _c('#c8b090'), 'f', 1.2)]
def _legs(view):
    if view == 'side':
        return [L(outline([(20, 30), (-20, 20, 1), (14, 44)]), 'mid', 'b'), L(outline([(10, 60), (-24, 70, 1), (14, 76)]), 'mid', 'b'),
                L(outline([(40, 4), (30, -24, 1), (54, 6)]), 'mid', 'b'), L(outline([(30, 92), (14, 116, 1), (44, 98)]), 'mid', 'b')]
    return [L(outline([(16, 30), (-20, 20, 1), (14, 44)]), 'mid', 'b'), L(outline([(84, 30), (120, 20, 1), (86, 44)]), 'mid', 'b'),
            L(outline([(10, 60), (-24, 74, 1), (14, 76)]), 'mid', 'b'), L(outline([(90, 60), (124, 74, 1), (86, 76)]), 'mid', 'b'),
            L(outline([(30, 8), (20, -22, 1), (44, 4)]), 'mid', 'b'), L(outline([(70, 8), (80, -22, 1), (56, 4)]), 'mid', 'b'),
            L(outline([(16, 88), (6, 116, 1), (30, 96)]), 'mid', 'b'), L(outline([(84, 88), (94, 116, 1), (70, 96)]), 'mid', 'b')]
C('casey-bagworm-moth', 'normal', P('#2c2c31', '#cda37e', iris='#c8201e'),
  F(eyes='none', brows=False, mouth='line', mouth_y=95, hairline=False, ears=False),
  _legs('front') + _wrap('front'), _legs('side') + _wrap('side'), _legs('back') + _wrap('back'))

# Cash "Crash" Tempest: pelo blanco de pinchos hacia arriba y, a cada lado, un mechón amarillo anaranjado en forma de rayo;
# guiña un ojo, ceja levantada y boca de fastidio
YOR = _c('#e8a830')
C('cash-crash-tempest', 'normal', P('#efeae4', '#fdd08c', iris='#2a2020', shade='#beaca6'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, face_front=face(chin=104), hairline=[(6, 62), (18, 50), (30, 56), (50, 46), (70, 56), (82, 50), (94, 62)]),
  [L(outline([(6, 50), (-6, 30), (2, 0, 1), (8, 22), (16, -4, 1), (22, 40), (14, 64)]), YOR), L(outline([(94, 50), (106, 30), (98, 0, 1), (92, 22), (84, -4, 1), (78, 40), (86, 64)]), YOR)] +
  dome('front', top=-6, w=40, cy=44, n=7, amp=14, seed=91, sb=60) +
  [L([(26, 74), (44, 76)], OUTC, 'f', False, False, 2.6), L(ell(36, 77, 2.6, 2.6), BLACK, 'f', False), L([(26, 66), (42, 68)], OUTC, 'f', False, False, 2.4),
   L(quad((58, 76), (64, 72), (72, 76)), OUTC, 'f', False, False, 2.4), L([(56, 66), (72, 62)], OUTC, 'f', False, False, 2.4)],
  dome('side', top=-6, w=44, cy=44, n=7, amp=14, seed=91, nape=84, fr=48) + [L(outline([(30, 50), (14, 30), (24, 0, 1), (30, 24), (40, 6, 1), (44, 44), (36, 66)]), YOR, 'f')],
  [L(outline([(6, 50), (-6, 30), (2, 0, 1), (8, 22), (16, -4, 1), (22, 40), (14, 64)]), YOR), L(outline([(94, 50), (106, 30), (98, 0, 1), (92, 22), (84, -4, 1), (78, 40), (86, 64)]), YOR)] +
  dome('back', top=-6, w=42, cy=44, n=7, amp=14, seed=91, nape=84))

# Cato "Caterpillar" Pillar: casco verde de oruga que le tapa la cabeza y los ojos, con dos grandes manchas de ojo a los
# lados y un visor verde lima; asoma pelo oscuro en bultos por debajo; nariz naranja y boca pequeña
CAT, CTL = _c('#5d9144'), _c('#b8d322')
def _cater(view):
    if view == 'front':
        return [L(outline([(8, 74), (6, 34), (22, 8), (50, 0), (78, 8), (94, 34), (92, 74), (50, 70)]), CAT, 'f', True, True),
                L(ell(20, 44, 12, 15), _c('#384232'), 'f', False), L(ell(20, 44, 7, 9), CTL, 'f', False), L(ell(80, 44, 12, 15), _c('#384232'), 'f', False), L(ell(80, 44, 7, 9), CTL, 'f', False),
                L(blob([(32, 54), (68, 54), (66, 72), (34, 72)], 6), CTL, 'f', True),
                L(outline([(12, 72), (20, 82), (30, 76), (40, 84), (50, 78), (60, 84), (70, 76), (80, 82), (88, 72), (50, 70)]), _c('#2a2a22'), 'f', False)]
    if view == 'side':
        return [L(outline([(10, 82), (4, 40), (22, 8), (52, 0), (80, 10), (94, 40), (94, 72), (60, 74), (30, 84)]), CAT, 'f', True, True),
                L(ell(40, 46, 13, 16), _c('#384232'), 'f', False), L(ell(40, 46, 8, 10), CTL, 'f', False), L(blob([(70, 56), (94, 58), (94, 72), (72, 74)], 6), CTL, 'f', True)]
    return [L(outline([(8, 84), (6, 34), (22, 8), (50, 0), (78, 8), (94, 34), (92, 84), (50, 90)]), CAT, 'f', True, True),
            L(ell(26, 50, 10, 12), _c('#384232'), 'f', False), L(ell(74, 50, 10, 12), _c('#384232'), 'f', False)]
C('cato-caterpillar-pillar', 'normal', P('#2a2a22', '#eed9ab', iris='#1e1a1a', nose='#e8802a'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, nose=(50, 86, 3.4), face_front=face(w=4, chin=104, jaw=3), hairline=False),
  _cater('front'), _cater('side'), _cater('back'))

# Caul Erpa: una mata enorme de pelo azul marino casi negro en bultos cuadrados, como un engranaje; piel tostada, ojos
# blancos cuadrados con la pupila negra y una sonrisa enorme de dientes
C('caul-erpa', 'normal', P('#28283f', '#eda662', iris='#1e1a1a', shade='#1e1e30'),
  F(eyes='none', brows='angry', mouth='none', face_front=face(chin=106), hairline=[(6, 60), (16, 48), (30, 42), (50, 40), (70, 42), (84, 48), (94, 60)]),
  [L(outline([(14, 64), (2, 60, 1), (0, 44, 1), (-6, 40, 1), (-4, 22, 1), (6, 22, 1), (8, 6, 1), (20, 8, 1), (26, -6, 1), (40, -2, 1), (46, -12, 1), (58, -8, 1), (66, -14, 1),
              (74, -2, 1), (86, -2, 1), (90, 12, 1), (102, 16, 1), (100, 30, 1), (108, 36, 1), (100, 48, 1), (98, 62, 1), (86, 64), (80, 50), (20, 50)])),
   L(outline([(62, -4), (74, -2), (86, -2), (90, 12), (102, 16), (100, 30), (98, 60), (84, 44)]), 'shade', 'b', False)] +
  [L(blob([(cx - 7, 70), (cx + 7, 70), (cx + 7, 80), (cx - 7, 80)], 2), WHITE, 'f', True) for cx in (35, 65)] +
  [L(ell(cx, 76, 2.4, 3), BLACK, 'f', False) for cx in (37, 63)] + big_grin(92, 14, 8),
  [L(outline([(56, 52), (64, 44), (84, 40), (90, 26, 1), (86, 10, 1), (74, 0, 1), (60, -10, 1), (46, -6, 1), (32, -10, 1), (22, 0, 1), (8, 2, 1), (4, 18, 1), (-6, 26, 1),
              (-2, 42, 1), (-8, 54, 1), (2, 64, 1), (6, 78, 1), (20, 78, 1), (30, 86, 1), (40, 76, 1), (52, 66)]))],
  [L(outline([(10, 80), (2, 64, 1), (-6, 56, 1), (-4, 40, 1), (-6, 24, 1), (6, 20, 1), (8, 6, 1), (20, 8, 1), (26, -6, 1), (40, -2, 1), (46, -12, 1), (58, -8, 1), (66, -14, 1),
              (74, -2, 1), (86, -2, 1), (92, 6, 1), (94, 20, 1), (106, 24, 1), (104, 40, 1), (106, 56, 1), (98, 64, 1), (90, 80, 1), (70, 82, 1), (50, 88, 1), (30, 82, 1)])),
   L(outline([(62, -4), (74, -2), (86, -2), (94, 20), (104, 40), (98, 64), (88, 78), (70, 60)]), 'shade', 'b', False)])

# Celer Lightfoot: mata de pelo azul marino echada hacia un lado, con dos pinchos curvos hacia arriba, que le tapa un ojo;
# ojo naranja afilado y un pañuelo amarillo al cuello
YSC = _c('#e8b030')
C('celer-lightfoot', 'normal', P('#2b3860', '#f5ca93', iris='#d8641e', shade='#202a4a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=[(6, 66), (16, 54), (40, 52), (60, 60), (76, 56), (94, 64)]),
  [L(outline([(10, 70), (2, 40), (14, 14), (28, 4), (34, -18, 1), (40, 6), (60, 4), (82, -14, 1), (78, 10), (94, 24), (98, 50), (92, 72), (82, 64), (24, 60)])),
   L(outline([(60, 6), (82, -14), (78, 10), (94, 24), (98, 50), (92, 70), (80, 40)]), 'shade', 'b', False),
   fl([(16, 44), (40, 40), (62, 46), (60, 70), (50, 84, 1), (40, 70), (24, 64), (14, 66)])] + scarf('front', YSC, 102, 10),
  [L(outline([(58, 60), (64, 48), (84, 44), (98, 30), (96, 10), (82, -14, 1), (70, 2), (40, 0), (30, -18, 1), (16, 10), (4, 34), (6, 62), (20, 78), (40, 76), (52, 68)]))] +
  scarf('side', YSC, 102, 10),
  [L(outline([(8, 76), (2, 40), (14, 14), (28, 4), (34, -18, 1), (40, 6), (60, 4), (82, -14, 1), (78, 10), (94, 24), (98, 50), (92, 76), (50, 84)])),
   L(outline([(60, 6), (82, -14), (78, 10), (94, 24), (98, 50), (92, 74), (76, 60)]), 'shade', 'b', False)] + scarf('back', YSC, 102, 10))

# Cham Barra (defensa): melena granate echada a un lado, con un mechón oscuro, que le tapa un ojo y le cae en punta por los
# lados del cuello; cara larga y pálida, ojo afilado y una perilla en punta
C('cham-barra', 'delgado', P('#9b5354', '#f5eac2', iris='#1e1a1a', shade='#773c3b', deep='#554449'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=96, face_front=face(chin=108), face_side=face_side(chin=8), nose=(50, 86, 1.4),
    hairline=[(6, 64), (14, 48), (30, 42), (50, 46), (70, 52), (86, 56), (94, 66)]),
  [L(outline([(8, 90), (4, 50), (16, 18), (40, 4), (66, 6), (88, 20), (104, 40), (110, 70, 1), (96, 62), (100, 88, 1), (88, 74), (82, 60), (18, 60), (18, 92)])),
   L(outline([(14, 40), (8, 70), (12, 92), (20, 70), (22, 46)]), 'deep', 'b'),
   fl([(60, 30), (90, 36), (96, 60), (88, 76, 1), (80, 60), (66, 56), (56, 80, 1), (54, 56)]),
   L(blob([(46, 104), (54, 104), (50, 112)], 3), BLACK, 'f', False)],
  [L(outline([(56, 62), (64, 48), (88, 42), (98, 24), (82, 6), (50, 0), (20, 8), (4, 32), (-8, 70, 1), (8, 64), (0, 92, 1), (20, 80), (36, 76), (48, 72)]))],
  [L(outline([(8, 92), (4, 50), (16, 18), (40, 4), (66, 6), (88, 20), (104, 40), (110, 70, 1), (96, 62), (100, 92, 1), (80, 86), (50, 90)])),
   L(outline([(70, 10), (88, 22), (104, 42), (108, 68), (96, 60), (98, 88), (80, 80), (84, 50)]), 'shade', 'b', False)])

# Charity Verchu: pelo verde corto con un mechón de antena en lo alto y dos coletas bajas a los lados atadas con gomas
# blancas que acaban en puntas; ojos grandes azules y sonrisa
C('charity-verchu', 'chica', P('#6ca772', '#fad7af', iris='#3a6ad0', shade='#557f5a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 62), (16, 50), (28, 62), (38, 48), (50, 64), (62, 48), (72, 62), (84, 50), (94, 62)]),
  [L(outline([(10, 84), (0, 92), (-4, 108, 1), (6, 100), (10, 112, 1), (16, 98), (20, 86)])), L(outline([(90, 84), (100, 92), (104, 108, 1), (94, 100), (90, 112, 1), (84, 98), (80, 86)])),
   L(blob([(8, 80), (18, 78), (20, 88), (10, 90)], 4), WHITE, 'f'), L(blob([(92, 80), (82, 78), (80, 88), (90, 90)], 4), WHITE, 'f')] +
  dome('front', top=4, w=46, cy=46, n=5, amp=6, seed=101, sb=80) + [L(outline([(44, 6), (40, -14), (56, -24, 1), (50, -8), (54, 6)]))],
  dome('side', top=4, w=46, cy=46, n=5, amp=6, seed=101, nape=84, fr=56) + [L(outline([(42, 6), (38, -14), (54, -24, 1), (48, -8), (52, 6)])),
                                                                          L(outline([(28, 80), (18, 92), (16, 108, 1), (26, 98), (34, 90)])),
                                                                          L(blob([(24, 78), (34, 78), (34, 88), (24, 88)], 4), WHITE, 'f')],
  dome('back', top=4, w=46, cy=46, n=5, amp=6, seed=101, nape=84) + [L(outline([(44, 6), (40, -14), (56, -24, 1), (50, -8), (54, 6)])),
                                                                    L(outline([(10, 84), (0, 92), (-4, 108, 1), (6, 100), (10, 112, 1), (16, 98), (20, 86)])),
                                                                    L(outline([(90, 84), (100, 92), (104, 108, 1), (94, 100), (90, 112, 1), (84, 98), (80, 86)]))])

# Charr Lightning (portero): pelo blanco pegado como un casco y una cresta naranja en forma de rayo que sale de lo alto;
# piel morena, pintura negra de guerra alrededor de los ojos azules y una sonrisa enorme de dientes
ORG = _c('#fbb443')
C('charr-lightning', 'corpulento', P('#e8e4e0', '#b5733b', iris='#4a8ad0', shade='#b5a9a0'),
  F(eyes='none', brows=False, mouth='none', face_front=face(w=6, chin=106, jaw=4), face_side=face_side(chin=6, jaw=4), big_ears=2, ear_out=4,
    hairline=[(6, 70), (14, 54), (30, 46), (50, 44), (70, 46), (86, 54), (94, 70)]),
  [L(outline([(8, 96), (4, 50), (16, 18), (40, 6), (60, 6), (84, 18), (96, 50), (92, 96), (82, 90), (82, 60), (18, 60), (18, 92)])),
   L(outline([(40, 20), (34, -4), (52, 4), (48, -26, 1), (76, -8), (60, -2), (66, 22), (52, 30)]), ORG)] +
  kabuki(BLACK, iris=_c('#4a8ad0')) + big_grin(94, 15, 8),
  [L(outline([(56, 60), (64, 48), (86, 44), (90, 22), (70, 6), (40, 4), (14, 16), (4, 44), (6, 80), (24, 90), (44, 84), (52, 72)])),
   L(outline([(50, 14), (40, -6), (56, 0), (56, -28, 1), (80, -6), (64, -2), (66, 20)]), ORG)],
  [L(outline([(8, 96), (4, 50), (16, 18), (40, 6), (60, 6), (84, 18), (96, 50), (92, 96), (50, 102)])),
   L(outline([(40, 20), (34, -4), (52, 4), (48, -26, 1), (76, -8), (60, -2), (66, 22), (52, 30)]), ORG)])

# Chief "Kerchief" Kerr: melena gris pizarra en casco que le cae por la frente y le tapa un ojo; ojo afilado de enfado y una
# bufanda a rayas amarillas y verde oscuro
SCY, SCG = _c('#e8d070'), _c('#2a5a3a')
def _kerr_scarf(view):
    out = scarf(view, SCG, 100, 12)
    if view == 'front':
        out += [L(outline([(18, 104), (28, 104), (30, 128), (20, 128)]), SCY, 'f'), L([(19, 112), (29, 112)], SCG, 'f', False, False, 2.4), L([(20, 120), (30, 120)], SCG, 'f', False, False, 2.4)]
    return out
C('chief-kerchief-kerr', 'normal', P('#4a5c62', '#fbf1ba', iris='#1e1a1a', shade='#343739'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=[(6, 70), (16, 60), (40, 56), (60, 50), (80, 52), (94, 66)]),
  bowl3('front', top=0, side=88, fringe=60, w=4) + [fl([(20, 40), (46, 40), (58, 52), (52, 70), (44, 84, 1), (36, 70), (22, 66)])] + _kerr_scarf('front'),
  bowl3('side', top=0, nape=90, fringe=58, w=4) + _kerr_scarf('side'),
  bowl3('back', top=0, nape=90, w=4) + _kerr_scarf('back'))

# Chip Chisel (defensa): pelo castaño rojizo en tupé plano cortado a escuadra; cabeza cuadrada enorme, cejas negras
# gruesas fruncidas, nariz grande con una cicatriz y boca recta
C('chip-chisel', 'corpulento', P('#742104', '#cf9669', iris='#1e1a1a', shade='#5a1a04'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=98, face_front=blob([(10, 40), (90, 40), (92, 96), (82, 110), (18, 110), (8, 96)], 4),
    face_side=face_side(chin=10, jaw=8), nose=(50, 86, 4), hairline=[(8, 66), (20, 54), (50, 52), (80, 54), (92, 66)], ear_out=6),
  [L(outline([(10, 70), (8, 20), (14, 10), (86, 10), (92, 20), (90, 70), (80, 56), (20, 56)])),
   L(outline([(60, 12), (86, 12), (92, 22), (90, 66), (78, 50)]), 'shade', 'b', False)] + thick_brows(64, BLACK, 4.6, 15, 1.4, 14) +
  [L([(44, 70), (48, 90)], OUTC, 'f', False, False, 1.4)],
  [L(outline([(56, 56), (64, 48), (90, 46), (96, 12), (20, 8), (8, 20), (6, 66), (22, 74), (46, 66)]))] + side_brow(64, BLACK, 4.6, 1.2),
  [L(outline([(10, 78), (8, 20), (14, 10), (86, 10), (92, 20), (90, 78), (50, 84)])),
   L(outline([(60, 12), (86, 12), (92, 22), (90, 76), (74, 70)]), 'shade', 'b', False)])

# Chrissy Urchin: una corona de pinchos castaño oscuro en lo alto de una cabeza pálida, larga y calva, orejas de punta,
# gafas redondas moradas de cristal azul y una mueca torcida de dientes
PUR, LBL = _c('#8c5ac8'), _c('#4a8ae0')
C('chrissy-urchin', 'delgado', P('#55454a', '#e2ccad', iris='#1e1a1a', shade='#3a3034'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=100, face_front=face(chin=112, top=14), face_side=face_side(chin=10), hairline=False, big_ears=3, ear_out=4),
  skull3('front') + [L(outline([(26, 22), (16, 14, 1), (30, 14), (24, 0, 1), (38, 8), (40, -8, 1), (48, 6), (54, -10, 1), (58, 6), (68, -6, 1), (66, 8), (80, 2, 1), (74, 14),
                                  (86, 14, 1), (74, 22), (50, 18)])),
                     L(blob([(28, 56), (36, 52), (44, 58), (40, 62)], 4), _c('#5a3a4a'), 'f', False), L(blob([(72, 56), (64, 52), (56, 58), (60, 62)], 4), _c('#5a3a4a'), 'f', False)] +
  round_glasses('front', PUR, 74, 14, 8, LBL, 2.6) + [L(ell(cx, 74, 3, 3), _c('#1a3a8a'), 'f', False) for cx in (36, 64)] +
  [L(blob([(44, 86), (56, 86), (54, 90), (46, 90)], 3), _c('#a08070'), 'f', False)],
  skull3('side') + [L(outline([(30, 12), (24, -2, 1), (38, 4), (42, -10, 1), (50, 2), (60, -8, 1), (62, 6), (76, 2, 1), (72, 14), (50, 16)]))] +
  round_glasses('side', PUR, 74, 14, 8, LBL, 2.6),
  skull3('back') + [L(outline([(26, 22), (16, 14, 1), (30, 14), (24, 0, 1), (38, 8), (40, -8, 1), (48, 6), (54, -10, 1), (58, 6), (68, -6, 1), (66, 8), (80, 2, 1), (74, 14),
                                 (86, 14, 1), (74, 22), (50, 18)]))])

# Christian Ball (portero): melena lisa naranja rojiza hasta los hombros con flequillo recto, y pintura roja de kabuki
# alrededor de los ojos; ojos afilados y boca de disgusto
C('christian-ball', 'normal', P('#b43b0d', '#f2eed7', iris='#1e1a1a', shade='#8d2f13'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=95, hairline=False),
  bowl3('front', top=2, side=110, fringe=60, w=4) + kabuki(_c('#c8201e'), iris=BLACK) + [L([(26, 62), (42, 67)], OUTC, 'f', False, False, 2.6), L([(74, 62), (58, 67)], OUTC, 'f', False, False, 2.6)] +
  [L(outline([(6, 110), (0, 118, 1), (12, 112)])), L(outline([(94, 110), (100, 118, 1), (88, 112)]))],
  bowl3('side', top=2, nape=110, fringe=58, w=4) + [L(blob([(78, 70), (90, 68), (90, 76), (80, 80)], 4), _c('#c8201e'), 'f', False)],
  bowl3('back', top=2, nape=112, w=4))

# Ciaran Wale (defensa): gorro de lana rojo calado, cara alargada como una talla de madera, con una narizota que baja en
# columna, ojos entornados en párpados grandes y una raya por boca
RBN = _c('#b73c48')
C('ciaran-wale', 'delgado', P('#3a2a20', '#cd966b', iris='#1e1a1a'),
  F(eyes='none', brows=False, mouth='none', face_front=face(chin=114, top=24), face_side=face_side(chin=12, nose=4), hairline=False, ear_out=2),
  [cap('front', RBN, top=-2, rim=54, w=48, z='f', ln=True), L(blob([(4, 50), (50, 44), (96, 50), (96, 60), (50, 54), (4, 60)], 6), _c('#9a2e3a'), 'f', True)] +
  [L(ell(cx, 74, 8, 6), WHITE, 'f', True) for cx in (34, 66)] + [L(ell(cx, 76, 2.6, 2.6), BLACK, 'f', False) for cx in (34, 66)] +
  [L(quad((26, 70), (34, 64), (42, 70)), OUTC, 'f', False, False, 2), L(quad((58, 70), (66, 64), (74, 70)), OUTC, 'f', False, False, 2),
   L(outline([(44, 64), (56, 64), (56, 106), (50, 112), (44, 106)]), 'skin_d', 'f', False, True), L([(30, 98), (44, 98)], OUTC, 'f', False, False, 1.4),
   L([(56, 98), (70, 98)], OUTC, 'f', False, False, 1.4)],
  [cap('side', RBN, top=-2, rim=54, w=48, z='f', ln=True)],
  [cap('back', RBN, top=-2, rim=56, w=48, z='f', ln=True), L(blob([(4, 54), (50, 48), (96, 54), (96, 64), (50, 58), (4, 64)], 6), _c('#9a2e3a'), 'f', True)])

# Cindy Reller: melena rubia larga y ondulada con flequillo, y una tiara plateada en lo alto; ojos azules y sonrisa
SLV = _c('#e8e8f0')
C('cindy-reller', 'chica', P('#e2c274', '#fbe8b8', iris='#3a8ac8', shade='#ac8151'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 64), (16, 50), (30, 56), (40, 46), (50, 58), (60, 46), (70, 56), (84, 50), (94, 64)]),
  dome('front', top=4, w=48, cy=46, n=0, long=110, flare=12, sb=70) +
  [L(outline([(28, 10), (34, -6, 1), (42, 4), (50, -10, 1), (58, 4), (66, -6, 1), (72, 10), (50, 6)]), SLV, 'f', True, True)],
  dome('side', top=4, w=48, cy=46, n=0, long=110, flare=12, fr=56) + [L(outline([(30, 8), (36, -6, 1), (44, 2), (52, -8, 1), (58, 6)]), SLV, 'f', True, True)],
  dome('back', top=4, w=48, cy=46, n=0, long=112, flare=12, ends=5) + [L(outline([(30, 12), (50, 4), (70, 12), (68, 16), (50, 10), (32, 16)]), SLV, 'f')])

# Cinqua Lightning: pelo rubio corto en mechones de punta, con un mechón negro largo que le cae por un lado de la cara;
# ojos naranjas en espiral y boquita abierta en O
C('cinqua-lightning', 'chica', P('#fdee89', '#f8d7b6', iris='#e0701e', shade='#d8c060'),
  F(eyes='none', brows=False, mouth='none', hairline=[(6, 62), (16, 48), (26, 58), (36, 46), (48, 60), (58, 46), (70, 56), (80, 46), (94, 62)]),
  dome('front', top=4, w=46, cy=46, n=6, amp=8, seed=111, sb=72) +
  [L(outline([(70, 26), (86, 30), (88, 60), (80, 92), (70, 104, 1), (72, 80), (74, 50)]), _c('#4a4440'), 'f')] +
  [L(ell(cx, 76, 6, 6.4), WHITE, 'f', True) for cx in (36, 64)] + [L(ell(cx, 76, 4.2, 4.4) + [ell(cx, 76, 4.2, 4.4)[0]], _c('#e0701e'), 'f', False, False, 1.6) for cx in (36, 64)] +
  [L(ell(cx, 76, 1.8, 2), BLACK, 'f', False) for cx in (36, 64)] + [L(ell(50, 94, 2.4, 3), _c('#8a3a2a'), 'f', True)],
  dome('side', top=4, w=46, cy=46, n=6, amp=8, seed=111, nape=84, fr=54) + [L(ell(82, 76, 3, 5), WHITE, 'f', True), L(ell(83, 76, 1.6, 2.6), _c('#e0701e'), 'f', False)],
  dome('back', top=4, w=46, cy=46, n=6, amp=8, seed=111, nape=84) + [L(outline([(14, 30), (30, 26), (28, 60), (22, 92), (12, 104, 1), (14, 70)]), _c('#4a4440'), 'f')])

# Cinque "5" Black-Blackley: un gorro negro enorme como una bola de bolos con cinco círculos blancos; el pelo negro le tapa
# los ojos y asoma una sonrisa pequeña
BOL = _c('#2c2a2c')
def _bowling(view):
    if view == 'side':
        return [L(ell(46, 30, 52, 44), BOL, 'f'), L(ell(52, 62, 50, 8), BOL, 'f'), L(ell(56, 18, 8, 8), WHITE, 'f', False), L(ell(76, 30, 7, 7), WHITE, 'f', False)]
    out = [L(ell(50, 28, 52, 44), BOL, 'f'), L(ell(50, 62, 52, 9), BOL, 'f')]
    if view == 'front':
        out += [L(ell(x, y, 8, 8), WHITE, 'f', False) for x, y in ((50, 0), (30, 12), (70, 12), (38, 34), (62, 34))]
    return out
C('cinque-5-black-blackley', 'normal', P('#2a2627', '#edd6bc', iris='#1e1a1a'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, hairline=False),
  [L(outline([(14, 96), (10, 60), (90, 60), (86, 96), (80, 80), (66, 86), (50, 80), (34, 86), (20, 80)]), 'mid', 'f')] + _bowling('front'),
  [L(outline([(54, 62), (20, 60), (10, 92), (30, 96), (48, 84), (70, 82), (80, 70)]), 'mid', 'f')] + _bowling('side'),
  [L(outline([(10, 96), (10, 60), (90, 60), (90, 96), (50, 100)]), 'mid', 'f')] + _bowling('back'))

# Ciril "Citrine" Trine (defensa): casco amarillo tallado como una gema que le tapa la cabeza, con placas a juego en la
# mandíbula; gafas de sol negras, cara cuadrada morena y boca recta
GEM, GEMD = _c('#fce65f'), _c('#d8b030')
def _gem(view):
    if view == 'front':
        return [L(outline([(16, 60), (14, 20), (30, 4), (70, 4), (86, 20), (84, 60), (70, 52), (30, 52)]), GEM, 'f', True, True),
                L([(30, 4), (36, 52)], GEMD, 'f', False, False, 1.4), L([(70, 4), (64, 52)], GEMD, 'f', False, False, 1.4), L([(14, 28), (86, 28)], GEMD, 'f', False, False, 1.4),
                L(outline([(14, 90), (24, 94), (36, 108), (24, 108), (16, 100)]), GEM, 'f', True, True), L(outline([(86, 90), (76, 94), (64, 108), (76, 108), (84, 100)]), GEM, 'f', True, True)]
    if view == 'side':
        return [L(outline([(10, 66), (6, 26), (24, 4), (64, 0), (86, 16), (92, 50), (70, 52), (40, 60)]), GEM, 'f', True, True),
                L([(40, 2), (34, 58)], GEMD, 'f', False, False, 1.4), L(outline([(70, 92), (86, 96), (82, 108), (66, 104)]), GEM, 'f', True, True)]
    return [L(outline([(14, 74), (14, 20), (30, 4), (70, 4), (86, 20), (86, 74), (50, 80)]), GEM, 'f', True, True),
            L([(30, 4), (34, 76)], GEMD, 'f', False, False, 1.4), L([(70, 4), (66, 76)], GEMD, 'f', False, False, 1.4)]
C('ciril-citrine-trine', 'corpulento', P('#c89a30', '#eaa65f', iris='#1e1a1a'),
  F(eyes='none', brows=False, mouth='line', mouth_y=98, face_front=blob([(14, 44), (86, 44), (88, 96), (78, 108), (22, 108), (12, 96)], 4),
    face_side=face_side(chin=8, jaw=6), big_ears=2, ear_out=4, hairline=False),
  _gem('front') + [L(blob([(18, 68), (48, 68), (50, 72), (52, 68), (82, 68), (80, 80), (54, 80), (50, 76), (46, 80), (20, 80)], 3), BLACK, 'f', True)],
  _gem('side') + [L(blob([(70, 68), (92, 68), (92, 80), (72, 80)], 3), BLACK, 'f', True), L([(70, 72), (46, 70)], BLACK, 'f', False, False, 2.6)],
  _gem('back'))

# Clara Schott: pelo castaño corto con una diadema naranja y unas gafas blancas de cristal amarillo encima; ojos afilados,
# sonrisa y un pañuelo amarillo atado al cuello
ORB, GLY = _c('#e8902a'), _c('#f8e8a0')
C('clara-schott', 'chica', P('#59412a', '#f3ba7c', iris='#1e1a1a', shade='#473223'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 66), (14, 50), (26, 60), (34, 48), (46, 62), (54, 50), (66, 60), (78, 50), (94, 64)]),
  dome('front', top=2, w=46, cy=46, n=5, amp=6, seed=121, sb=86) +
  [band('front', ORB, 30, 5, w=44, dip=8)] + [L(blob([(cx - 9, 20), (cx + 9, 18), (cx + 9, 28), (cx - 9, 30)], 4), WHITE, 'f', True) for cx in (34, 60)] +
  [L(blob([(cx - 6, 21), (cx + 6, 20), (cx + 6, 26), (cx - 6, 27)], 3), GLY, 'f', False) for cx in (34, 60)] + scarf('front', _c('#fbe545'), 100, 12),
  dome('side', top=2, w=46, cy=46, n=5, amp=6, seed=121, nape=86, fr=56) + [band('side', ORB, 28, 5)] + scarf('side', _c('#fbe545'), 100, 12),
  dome('back', top=2, w=46, cy=46, n=5, amp=6, seed=121, nape=86) + [band('back', ORB, 30, 5)] + scarf('back', _c('#fbe545'), 100, 12))

# Claude Hammer: pelo morado liso peinado en un tupé redondo y alto; ojos ovalados blancos con la pupila pequeña y una
# sonrisa pequeña de dientes
C('claude-hammer', 'normal', P('#5b4865', '#e2ccae', iris='#1e1a1a', shade='#4e414f'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=94, hairline=[(8, 62), (18, 52), (34, 48), (50, 46), (66, 48), (82, 52), (92, 62)]),
  [L(outline([(16, 62), (12, 30), (16, 8), (32, -10), (50, -14), (68, -10), (84, 8), (88, 30), (84, 62), (78, 52), (22, 52)])),
   L(outline([(58, -10), (78, -4), (88, 20), (86, 58), (76, 30)]), 'shade', 'b', False), strand([(36, -6), (44, 30)], 'deep', 'b', 1.0), strand([(56, -8), (58, 30)], 'deep', 'b', 1.0)] +
  [L(ell(cx, 76, 8, 5.6), WHITE, 'f', True) for cx in (35, 65)] + [L(ell(cx, 76, 1.8, 2), BLACK, 'f', False) for cx in (37, 63)] +
  [L(quad((44, 60), (50, 56), (56, 60)), OUTC, 'f', False, False, 1.2)],
  [L(outline([(56, 56), (64, 48), (86, 44), (90, 18), (76, -6), (50, -14), (24, -6), (8, 16), (4, 46), (14, 72), (34, 74), (50, 64)]))] +
  [L(ell(82, 76, 3, 5), WHITE, 'f', True), L(ell(83, 76, 1.2, 1.8), BLACK, 'f', False)],
  [L(outline([(14, 74), (12, 30), (16, 8), (32, -10), (50, -14), (68, -10), (84, 8), (88, 30), (86, 74), (50, 80)])),
   L(outline([(58, -10), (78, -4), (88, 20), (86, 72), (70, 40)]), 'shade', 'b', False)])

# Cloudy Forbes (defensa): pelo gris claro peinado hacia arriba en una onda con punta, piel morena, una marca color melocotón
# en la frente, ojos afilados castaños y boca de enfado
C('cloudy-forbes', 'normal', P('#c3bfb7', '#ae8760', iris='#7a3a2a', shade='#87756f'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=[(6, 62), (14, 50), (30, 46), (44, 56), (56, 48), (70, 46), (86, 50), (94, 62)]),
  [L(outline([(12, 66), (6, 36), (16, 14), (40, 0), (66, -4), (90, -10, 1), (84, 10), (94, 36), (88, 66), (80, 52), (20, 52)])),
   L(outline([(60, 0), (90, -10), (84, 10), (94, 36), (88, 62), (76, 30)]), 'shade', 'b', False),
   L(outline([(44, 50), (50, 40), (56, 50), (50, 58)]), _c('#e8a880'), 'f', False)],
  [L(outline([(56, 58), (64, 46), (86, 42), (96, 20), (100, -8, 1), (76, 2), (40, 2), (14, 14), (4, 44), (14, 72), (34, 74), (50, 64)]))],
  [L(outline([(12, 74), (6, 36), (16, 14), (40, 0), (66, -4), (90, -10, 1), (84, 10), (94, 36), (88, 74), (50, 80)])),
   L(outline([(60, 0), (90, -10), (84, 10), (94, 36), (88, 72), (72, 50)]), 'shade', 'b', False)])

# Cobie Clubb (portero): máscara de luchador verde con un trébol en la frente, unas gafas de cristal verde y un pañuelo
# verde al cuello; bigote amarillo y boca de rabia
MSK, MSL = _c('#62a337'), _c('#87f174')
def _clubb(view):
    if view == 'front':
        return [L(outline([(10, 92), (6, 40), (22, 8), (50, 0), (78, 8), (94, 40), (90, 92), (74, 70), (26, 70)]), MSK, 'f', True, True),
                L(ell(42, 24, 8, 8), MSL, 'f', False), L(ell(58, 24, 8, 8), MSL, 'f', False), L(ell(50, 14, 8, 8), MSL, 'f', False), L([(50, 28), (50, 40)], MSL, 'f', False, False, 2.4),
                L(ell(34, 74, 12, 9), BLACK, 'f', True), L(ell(66, 74, 12, 9), BLACK, 'f', True), L(ell(34, 74, 9, 6.4), MSL, 'f', False), L(ell(66, 74, 9, 6.4), MSL, 'f', False),
                L(outline([(40, 84), (50, 80), (60, 84), (56, 90), (44, 90)]), _c('#e8c030'), 'f', True)] + scarf('front', MSK, 100, 12)
    if view == 'side':
        return [L(outline([(10, 96), (4, 40), (22, 8), (52, 0), (80, 10), (94, 40), (94, 66), (70, 70), (40, 90)]), MSK, 'f', True, True),
                L(ell(82, 74, 8, 9), BLACK, 'f', True), L(ell(83, 74, 5, 6.4), MSL, 'f', False)] + scarf('side', MSK, 100, 12)
    return [L(outline([(10, 96), (6, 40), (22, 8), (50, 0), (78, 8), (94, 40), (90, 96), (50, 100)]), MSK, 'f', True, True), L([(50, 0), (50, 96)], _c('#4a8a2a'), 'f', False, False, 1.4)] + \
        scarf('back', MSK, 100, 12)
C('cobie-clubb', 'normal', P('#2a2a22', '#f8d28d', iris='#1e1a1a'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=96, hairline=False),
  _clubb('front'), _clubb('side'), _clubb('back'))

# Cole Bludd (defensa): pelo rosa peinado en un tupé enrollado y dos rulos a los lados, castaño por debajo; ojos redondos
# negros, nariz rosa redonda y sonrisa
PNK = _c('#f9cdba')
C('cole-bludd', 'normal', P('#4a2e22', '#feeaba', iris='#1e1a1a', nose='#e8907a'),
  F(eyes='round', brows=False, mouth='smile', mouth_y=92, nose=(50, 85, 2.8), hairline=[(8, 60), (18, 50), (50, 46), (82, 50), (92, 60)]),
  [L(outline([(16, 62), (14, 34), (30, 22), (70, 22), (86, 34), (84, 62), (50, 54)])),
   L(outline([(28, 30), (24, 6), (40, -10), (60, -10), (72, 6), (70, 30), (50, 36)]), PNK, 'b', True, True), strand([(40, -4), (48, 24)], _c('#d8a090'), 'b', 1.2),
   L(ell(14, 46, 10, 8), PNK, 'b'), L(ell(86, 46, 10, 8), PNK, 'b'), L(ell(14, 78, 7, 6), PNK, 'f'), L(ell(86, 78, 7, 6), PNK, 'f'),
   L(blob([(28, 62), (40, 60), (38, 66)], 3), PNK, 'f', False), L(blob([(72, 62), (60, 60), (62, 66)], 3), PNK, 'f', False)],
  [L(outline([(54, 56), (64, 48), (82, 42), (84, 28), (60, 20), (30, 22), (12, 34), (8, 60), (24, 74), (44, 66)])),
   L(outline([(30, 30), (30, 4), (46, -10), (66, -8), (76, 8), (72, 30)]), PNK, 'b', True, True), L(ell(30, 46, 10, 8), PNK, 'b')],
  [L(outline([(14, 74), (14, 34), (30, 22), (70, 22), (86, 34), (86, 74), (50, 80)])),
   L(outline([(28, 30), (24, 6), (40, -10), (60, -10), (72, 6), (70, 30), (50, 36)]), PNK, 'b', True, True), L(ell(14, 46, 10, 8), PNK, 'b'), L(ell(86, 46, 10, 8), PNK, 'b')])

# Cole "Rhino" Optera: casco granate de escarabajo rinoceronte que le tapa la cabeza, con un cuerno bifurcado que sube de la
# frente; cara morena ancha con dos franjas granates, ojos de enfado y una nariz en pico
RHN = _c('#750d04')
def _rhino(view):
    if view == 'front':
        return [L(outline([(12, 64), (10, 24), (26, 6), (74, 6), (90, 24), (88, 64), (76, 56), (24, 56)]), RHN, 'f', True, True),
                L(outline([(44, 10), (40, -14), (24, -24), (30, -30, 1), (46, -20), (50, -36, 1), (54, -20), (70, -30, 1), (76, -24), (60, -14), (56, 10)]), RHN, 'f', True, True),
                L(blob([(12, 76), (20, 74), (22, 94), (14, 96)], 3), RHN, 'f', False), L(blob([(88, 76), (80, 74), (78, 94), (86, 96)], 3), RHN, 'f', False)]
    if view == 'side':
        return [L(outline([(8, 70), (4, 30), (22, 6), (70, 4), (90, 20), (92, 60), (60, 58), (30, 70)]), RHN, 'f', True, True),
                L(outline([(60, 6), (66, -16), (60, -34, 1), (74, -20), (90, -30, 1), (82, -10), (72, 8)]), RHN, 'f', True, True)]
    return [L(outline([(12, 74), (10, 24), (26, 6), (74, 6), (90, 24), (88, 74), (50, 80)]), RHN, 'f', True, True),
            L(outline([(44, 10), (40, -14), (24, -24), (30, -30, 1), (46, -20), (50, -36, 1), (54, -20), (70, -30, 1), (76, -24), (60, -14), (56, 10)]), RHN, 'f', True, True)]
C('cole-rhino-optera', 'normal', P('#501109', '#eca563', iris='#1e1a1a'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=96, face_front=face(w=4, chin=104, jaw=3), hairline=False, ear_out=4),
  _rhino('front') + [L(outline([(44, 80), (56, 80), (50, 92, 1)]), _c('#8a6a3a'), 'f', True)],
  _rhino('side'), _rhino('back'))

# Colin Urlane: melena blanca larga y alborotada en mechones de punta, con un moñito de pinchos en lo alto; ojos afilados y
# una sonrisa de dientes
C('colin-urlane', 'normal', P('#efe8e2', '#fabc7d', iris='#3a6a6a', shade='#c9ad9c'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=93, hairline=hl(6, 64, 48, 58, jit=3, seed=13)),
  dome('front', top=4, w=50, cy=46, n=10, amp=10, seed=131, long=104, flare=14) + [L(outline([(40, 8), (36, -10, 1), (46, -4), (50, -18, 1), (54, -4), (64, -10, 1), (60, 8)]))],
  dome('side', top=4, w=50, cy=46, n=10, amp=10, seed=131, long=104, flare=14, fr=54) + [L(outline([(38, 6), (34, -12, 1), (44, -4), (50, -18, 1), (56, 6)]))],
  dome('back', top=4, w=50, cy=46, n=10, amp=10, seed=131, long=106, flare=14, ends=5) + [L(outline([(40, 8), (36, -10, 1), (46, -4), (50, -18, 1), (54, -4), (64, -10, 1), (60, 8)]))])

# Cooper Kettle: una tapa de cazuela amarilla de sombrero con su asa, pelo blanco esponjoso que le sale a los lados; cara
# redonda y enorme anaranjada, ojitos de enfado y la boca abierta con la lengua
POT, POTD = _c('#e1bd49'), _c('#b8962a')
def _pot(view):
    if view == 'side':
        return [L(ell(46, 30, 50, 10), POT, 'f', True, True), L(outline([(20, 30), (24, 12), (70, 12), (74, 30)]), POT, 'f', True, True), L(ell(46, 8, 7, 5), POTD, 'f', True)]
    return [L(ell(50, 30, 52, 11), POT, 'f', True, True), L(outline([(20, 30), (24, 12), (76, 12), (80, 30)]), POT, 'f', True, True), L(ell(50, 8, 8, 5), POTD, 'f', True),
            L(quad((22, 30), (50, 36), (78, 30)), POTD, 'f', False, False, 1.4)]
C('cooper-kettle', 'corpulento', P('#efe6e2', '#eda561', iris='#1e1a1a', shade='#c3a9a3'),
  F(eyes='dot', brows='angry', mouth='none', face_front=face(w=8, chin=110, jaw=6, top=24), face_side=face_side(chin=8, jaw=6), hairline=False),
  [L(outline([(10, 40), (-6, 50, 1), (2, 60), (-8, 70, 1), (4, 76), (-2, 88, 1), (12, 84), (18, 50)])),
   L(outline([(90, 40), (106, 50, 1), (98, 60), (108, 70, 1), (96, 76), (102, 88, 1), (88, 84), (82, 50)]))] + _pot('front') +
  [L(ell(50, 96, 6, 8), _c('#a03a2a'), 'f', True), L(ell(50, 100, 4, 4), _c('#f07a7a'), 'f', False)],
  [L(outline([(30, 40), (10, 50, 1), (18, 62), (8, 74, 1), (22, 78), (16, 90, 1), (36, 84), (44, 50)]))] + _pot('side'),
  [L(outline([(8, 40), (-6, 56, 1), (4, 66), (-4, 80, 1), (10, 84), (50, 90), (90, 84), (104, 80, 1), (96, 66), (106, 56, 1), (92, 40)]))] + _pot('back'))

# Cornelius Roes: pelo amarillo en casco con franjas verticales más claras, como un balón; gafas redondas blancas de
# cristales rojos a rayas y una sonrisa pequeña
GLR = _c('#8b403e')
C('cornelius-roes', 'normal', P('#f5e56a', '#eba762', iris='#1e1a1a', shade='#d8c040'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, hairline=[(8, 58), (20, 48), (50, 44), (80, 48), (92, 58)], ear_out=2),
  [L(outline([(14, 62), (12, 30), (26, 10), (50, 4), (74, 10), (88, 30), (86, 62), (50, 52)]))] +
  [L([(x, 8 + abs(50 - x) * 0.2), (x * 0.9 + 5, 52)], 'shade', 'b', False, False, 3.0) for x in (30, 44, 56, 70)] +
  round_glasses('front', WHITE, 76, 14, 9, GLR, 3.0) + [L([(27, 76), (45, 76)], WHITE, 'f', False, False, 1.6), L([(55, 76), (73, 76)], WHITE, 'f', False, False, 1.6)],
  [L(outline([(56, 54), (66, 46), (86, 42), (88, 22), (68, 4), (40, 2), (14, 14), (4, 40), (10, 66), (30, 72), (48, 64)]))] +
  [L([(x, 4 + abs(46 - x) * 0.3), (x - 6, 66)], 'shade', 'b', False, False, 3.0) for x in (30, 50, 70)] + round_glasses('side', WHITE, 76, 14, 9, GLR, 3.0),
  [L(outline([(12, 74), (12, 30), (26, 10), (50, 4), (74, 10), (88, 30), (88, 74), (50, 80)]))] +
  [L([(x, 8 + abs(50 - x) * 0.2), (x, 78)], 'shade', 'b', False, False, 3.0) for x in (30, 44, 56, 70)])

# Corvus Cardson: melena granate larga y rizada que le cae por los hombros, con una trenza de cuentas, y un pañuelo azul
# marino con un rayo amarillo y dos picos; piel morena, ojos amarillos y sonrisa
BND2 = _c('#4f4f65')
C('corvus-cardson', 'normal', P('#8a3233', '#c9a967', iris='#e8c820', shade='#6c2527'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=93, hairline=[(6, 64), (16, 50), (30, 58), (42, 48), (54, 58), (66, 48), (80, 56), (94, 62)]),
  dome('front', top=6, w=50, cy=48, n=10, amp=6, soft=True, seed=141, long=108, flare=14) +
  [L(outline([(6, 40), (-4, 26, 1), (14, 26), (50, 18), (86, 26), (104, 26, 1), (94, 40), (50, 34)]), BND2, 'f', True, True),
   L(outline([(40, 22), (58, 20), (48, 28), (62, 28), (42, 38), (50, 30), (38, 30)]), _c('#f0d030'), 'f', False),
   L([(24, 66), (26, 100)], _c('#2a2a2a'), 'f', False, False, 3.4), L(ell(26, 102, 3, 3), _c('#3a9a6a'), 'f', False)],
  dome('side', top=6, w=50, cy=48, n=10, amp=6, soft=True, seed=141, long=108, flare=14, fr=56) +
  [L(outline([(2, 40), (-10, 28, 1), (8, 26), (50, 18), (92, 26), (94, 36), (50, 32)]), BND2, 'f', True, True)],
  dome('back', top=6, w=50, cy=48, n=10, amp=6, soft=True, seed=141, long=110, flare=14, ends=6) +
  [L(outline([(6, 40), (-4, 26, 1), (14, 26), (50, 20), (86, 26), (104, 26, 1), (94, 40), (50, 36)]), BND2, 'f', True, True)])

# Cory "Coral" Alberts: pelo rojo en forma de coral, un cilindro que sube por el centro con ramas cortas a los lados; piel
# rojiza, ojos cerrados tranquilos y la boca en ondas
CRL = _c('#a42629')
C('cory-coral-alberts', 'normal', P('#a42629', '#cb7150', iris='#1e1a1a', shade='#6a1f1d'),
  F(eyes='closed', brows=False, mouth='none', hairline=[(8, 58), (20, 50), (50, 46), (80, 50), (92, 58)]),
  [L(outline([(14, 62), (12, 34), (28, 18), (50, 14), (72, 18), (88, 34), (86, 62), (50, 54)])),
   L(outline([(42, 18), (40, -18), (50, -24), (60, -18), (58, 18)])), L(ell(50, -20, 8, 4), _c('#f0a0a0'), 'f', False),
   L(outline([(20, 30), (6, 20), (0, 8), (6, 6), (14, 16), (28, 22)])), L(outline([(80, 30), (94, 20), (100, 8), (94, 6), (86, 16), (72, 22)])),
   L(outline([(14, 46), (-2, 44), (-4, 36), (14, 38)])), L(outline([(86, 46), (102, 44), (104, 36), (86, 38)]))] +
  [L(quad((36, 94), (40, 98), (44, 94)) + quad((44, 94), (48, 90), (52, 94))[1:] + quad((52, 94), (56, 98), (60, 94))[1:] + quad((60, 94), (63, 91), (65, 94))[1:],
     OUTC, 'f', False, False, 1.4)],
  [L(outline([(56, 54), (66, 46), (86, 40), (88, 26), (70, 14), (40, 14), (16, 24), (6, 46), (14, 70), (34, 72), (48, 64)])),
   L(outline([(40, 18), (38, -18), (48, -24), (58, -18), (56, 18)])), L(outline([(24, 30), (8, 18), (4, 8), (12, 8), (20, 16), (34, 22)]))],
  [L(outline([(14, 74), (12, 34), (28, 18), (50, 14), (72, 18), (88, 34), (86, 74), (50, 80)])),
   L(outline([(42, 18), (40, -18), (50, -24), (60, -18), (58, 18)])),
   L(outline([(20, 30), (6, 20), (0, 8), (6, 6), (14, 16), (28, 22)])), L(outline([(80, 30), (94, 20), (100, 8), (94, 6), (86, 16), (72, 22)]))])

# Cumulo Nimbus (portero): una nube enorme de rizos azul petróleo que le tapa casi toda la cabeza y un ojo; cara ancha y
# pálida, nariz rosada, ojo de párpado caído y dos colmillos hacia arriba
C('cumulo-nimbus', 'corpulento', P('#365969', '#e5d5bd', iris='#1e1a1a', shade='#2b3841', nose='#d89a8a'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=98, face_front=face(w=8, chin=108, jaw=6), face_side=face_side(chin=8, jaw=6), nose=(56, 84, 4), hairline=False),
  [L(curls(50, 42, (60, 44), 11, 0.1), 'mid', 'b'), L(curls(36, 60, (34, 24), 7, 0.3), 'mid', 'f'),
   strand([(20, 30), (28, 22), (34, 30)], 'shade', 'f', 1.4), strand([(60, 20), (70, 14), (76, 22)], 'shade', 'b', 1.4),
   L(quad((60, 76), (66, 72), (74, 76)), OUTC, 'f', False, False, 2.4), L(ell(66, 78, 2.4, 2), BLACK, 'f', False),
   L(outline([(38, 100), (40, 92, 1), (43, 100)]), WHITE, 'f', True), L(outline([(57, 100), (60, 92, 1), (62, 100)]), WHITE, 'f', True)],
  [L(curls(44, 42, (54, 44), 10, 0.2), 'mid', 'b'), L(curls(60, 52, (30, 20), 6, 0.3), 'mid', 'f')],
  [L(curls(50, 46, (60, 48), 11, 0.1), 'mid', 'b'), strand([(30, 30), (40, 22), (46, 30)], 'shade', 'b', 1.4)])

# Cynthia "Synthpop" Electra: pelo verde agua por los hombros con mechones de punta, unos cascos blancos con corazones
# rosas y un aro de pelo en espiral flotando encima, como un halo; ojos azules y boquita en O
HRT = _c('#f070a8')
def _phones(view):
    if view == 'side':
        return [L(ell(46, 64, 12, 14), WHITE, 'f', True), L(outline([(46, 60), (38, 50), (46, 44), (54, 50)]), HRT, 'f', True)]
    out = []
    for x, s in ((8, -1), (92, 1)):
        out += [L(ell(x, 50, 12, 16), WHITE, 'f', True), L(outline([(x, 60), (x - 9, 50), (x - 4, 44), (x, 48), (x + 4, 44), (x + 9, 50)]), HRT, 'f', True)]
    return out
C('cynthia-synthpop-electra', 'chica', P('#7ed7c4', '#f5d4b8', iris='#3a9ad8', shade='#5aa898'),
  F(eyes='big', brows=True, mouth='none', hairline=[(6, 64), (16, 50), (28, 62), (38, 48), (50, 62), (62, 48), (72, 62), (84, 50), (94, 64)]),
  dome('front', top=6, w=48, cy=46, n=8, amp=6, seed=151, long=96, flare=16) + _phones('front') +
  [L(quad((8, 36), (50, 24), (92, 36)), WHITE, 'f', False, False, 3), L(ell(50, -8, 20, 4) + [ell(50, -8, 20, 4)[0]], 'mid', 'f', False, False, 2.6),
   L(ell(50, 94, 2, 2.6), _c('#8a3a2a'), 'f', True)],
  dome('side', top=6, w=48, cy=46, n=8, amp=6, seed=151, long=96, flare=16, fr=56) + _phones('side') +
  [L(ell(46, -8, 16, 3) + [ell(46, -8, 16, 3)[0]], 'mid', 'f', False, False, 2.6)],
  dome('back', top=6, w=48, cy=46, n=8, amp=6, seed=151, long=98, flare=16, ends=5) + _phones('front') +
  [L(ell(50, -8, 20, 4) + [ell(50, -8, 20, 4)[0]], 'mid', 'f', False, False, 2.6)])

# Dai Mondo (defensa): capucha blanca y azul en rombos con unas gafas de nieve en la frente, una máscara a juego que le tapa
# la cara salvo un ojo, mechones largos plateados que le caen por un lado y una bufanda azul marino
DMB, DMW, DMS = _c('#2587bf'), _c('#e8eef0'), _c('#3c4454')
def _dai(view):
    if view == 'front':
        return [L(outline([(6, 104), (2, 50), (16, 10), (50, -10), (84, 10), (98, 50), (94, 104), (50, 110)]), DMW, 'f', True, True),
                L(outline([(50, -10), (66, 30), (50, 60), (34, 30)]), DMB, 'f', False), L(outline([(16, 60), (34, 30), (50, 60), (34, 92)]), DMB, 'f', False),
                L(outline([(84, 60), (66, 30), (50, 60), (66, 92)]), DMB, 'f', False),
                L(outline([(70, 30), (96, 40), (106, 80), (100, 108), (86, 90), (80, 60)]), _c('#a7b2c1'), 'f'),
                L(blob([(24, 66), (46, 66), (46, 76), (24, 78)], 3), _c('#f4d8c0'), 'f', False), L(ell(36, 72, 3, 3), BLACK, 'f', False),
                L(quad((22, 62), (34, 58), (46, 64)), OUTC, 'f', False, False, 2)] + goggles('front', 28, DMS, _c('#c8e8f0')) + scarf('front', DMS, 102, 14)
    if view == 'side':
        return [L(outline([(10, 104), (2, 50), (20, 8), (50, -8), (80, 10), (96, 50), (96, 96), (70, 108), (40, 110)]), DMW, 'f', True, True),
                L(outline([(50, -8), (66, 30), (52, 60), (36, 30)]), DMB, 'f', False), L(outline([(70, 60), (88, 40), (96, 70), (84, 96)]), DMB, 'f', False),
                L(outline([(30, 20), (6, 40), (-8, 90), (8, 100), (20, 60)]), _c('#a7b2c1'), 'f')] + goggles('side', 28, DMS, _c('#c8e8f0')) + scarf('side', DMS, 102, 14)
    return [L(outline([(6, 104), (2, 50), (16, 10), (50, -10), (84, 10), (98, 50), (94, 104), (50, 110)]), DMW, 'f', True, True),
            L(outline([(50, -10), (66, 30), (50, 60), (34, 30)]), DMB, 'f', False),
            L(outline([(30, 30), (4, 40), (-6, 80), (4, 108), (18, 90), (24, 60)]), _c('#a7b2c1'), 'f')] + goggles('back', 28, DMS) + scarf('back', DMS, 102, 14)
C('dai-mondo', 'normal', P('#a7b2c1', '#f4d8c0', iris='#1e1a1a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _dai('front'), _dai('side'), _dai('back'))

# Daisy Young: pelo rubio con dos moños enormes y esponjosos arriba atados con gomas verdes, flequillo y media melena;
# ojos castaños, coloretes y sonrisa
C('daisy-young', 'chica', P('#ecdb81', '#f5dcbf', iris='#8a5a2a', shade='#b98f56'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 64), (16, 52), (30, 60), (40, 50), (50, 62), (60, 50), (70, 60), (84, 52), (94, 64)]),
  [L(curls(16, 12, (22, 20), 6, 0.2), 'mid', 'b'), L(curls(84, 12, (22, 20), 6, 0.5), 'mid', 'b')] +
  dome('front', top=6, w=46, cy=46, n=0, sb=90) + [L(ell(28, 26, 5, 4), _c('#7ad040'), 'f'), L(ell(72, 26, 5, 4), _c('#7ad040'), 'f'),
                                                  L(ell(28, 86, 5, 3.4), PINK, 'f', False), L(ell(72, 86, 5, 3.4), PINK, 'f', False)],
  [L(curls(40, 6, (24, 20), 6, 0.2), 'mid', 'b')] + dome('side', top=6, w=46, cy=46, n=0, nape=90, fr=56),
  [L(curls(16, 12, (22, 20), 6, 0.2), 'mid', 'b'), L(curls(84, 12, (22, 20), 6, 0.5), 'mid', 'b')] + dome('back', top=6, w=46, cy=46, n=0, nape=92) +
  [L(ell(28, 26, 5, 4), _c('#7ad040'), 'f'), L(ell(72, 26, 5, 4), _c('#7ad040'), 'f')])

# Damo "DJ" Jukes: rastas granate oscuro echadas hacia delante, que le caen en cortina por la cara; gafas de sol negras,
# piel morena y boca seria
C('damo-dj-jukes', 'delgado', P('#51112d', '#bc8f61', iris='#1e1a1a', shade='#401424'),
  F(eyes='none', brows=False, mouth='line', mouth_y=96, face_front=face(chin=108), face_side=face_side(chin=8), hairline=[(6, 60), (20, 46), (50, 40), (80, 46), (94, 60)]),
  [L(outline([(14, 60), (10, 24), (30, 2), (60, -6), (96, -8, 1), (84, 6), (92, 22), (86, 60), (70, 50), (30, 50)])),
   L(outline([(22, 30), (14, 70), (20, 110, 1), (30, 70), (34, 40)]), 'mid', 'f'), L(outline([(34, 26), (30, 64), (36, 96, 1), (42, 60), (44, 30)]), 'mid', 'f'),
   strand([(40, 4), (60, 0), (80, -4)], 'shade', 'b', 1.2), strand([(30, 14), (60, 10), (88, 8)], 'shade', 'b', 1.2),
   L(blob([(20, 70), (46, 70), (48, 80), (24, 80)], 3), BLACK, 'f', True), L(blob([(80, 70), (54, 70), (52, 80), (76, 80)], 3), BLACK, 'f', True)],
  [L(outline([(56, 54), (66, 46), (86, 42), (102, 26), (110, 0, 1), (80, 4), (50, -4), (20, 4), (4, 30), (6, 60), (20, 72), (40, 66)])),
   L(outline([(84, 30), (96, 50), (92, 90, 1), (86, 54)]), 'mid', 'f'), L(blob([(74, 70), (92, 70), (92, 80), (76, 80)], 3), BLACK, 'f', True)],
  [L(outline([(12, 76), (10, 24), (30, 2), (60, -6), (96, -8, 1), (84, 6), (92, 22), (88, 76), (50, 84)])),
   strand([(30, 10), (34, 74)], 'shade', 'b', 1.2), strand([(50, 4), (50, 80)], 'shade', 'b', 1.2), strand([(70, 6), (66, 76)], 'shade', 'b', 1.2)])

# Damon Valiant: pinchos rubio crema altísimos, unas gafas rojas de cristal redondo subidas a la frente y una mascarilla
# blanca sobre la boca; ojos afilados de color granate
RGL = _c('#d3180c')
C('damon-valiant', 'normal', P('#fdeab9', '#f9cea0', iris='#8a2a2a', shade='#d8c090'),
  F(eyes='sharp', brows='angry', mouth='none', hairline=hl(6, 64, 50, 58, jit=2, seed=17)),
  dome('front', top=-12, w=48, cy=44, n=7, amp=18, seed=161, sb=72) +
  [L(blob([(20, 50), (80, 50), (80, 58), (20, 58)], 4), WHITE, 'f', True), L(ell(36, 50, 10, 9), RGL, 'f', True), L(ell(64, 50, 10, 9), RGL, 'f', True),
   L(ell(33, 47, 3, 2.4), _c('#ff8a7a'), 'f', False), L(ell(61, 47, 3, 2.4), _c('#ff8a7a'), 'f', False),
   L(outline([(38, 90), (62, 90), (60, 104), (50, 108), (40, 104)]), WHITE, 'f', True, True), L([(24, 84), (38, 92)], BLACK, 'f', False, False, 1.2),
   L([(76, 84), (62, 92)], BLACK, 'f', False, False, 1.2)],
  dome('side', top=-12, w=48, cy=44, n=7, amp=18, seed=161, nape=86, fr=48) +
  [L(ell(80, 50, 8, 9), RGL, 'f', True), L(outline([(76, 90), (92, 90), (92, 104), (80, 106)]), WHITE, 'f', True, True), L([(76, 92), (50, 80)], BLACK, 'f', False, False, 1.2)],
  dome('back', top=-12, w=48, cy=44, n=7, amp=18, seed=161, nape=86) + [L(quad((6, 52), (50, 58), (94, 52)), WHITE, 'f', False, False, 3)])

# Dan "Banner" Bannerman (defensa): pelo gris rapado y una cinta blanca con un círculo rojo, atada con dos colas a los
# lados; cejas verdes, ojos redondos azul grisáceo, coloretes y sonrisa
C('dan-banner-bannerman', 'normal', P('#9a979c', '#fbd18c', iris='#5a7a9a', shade='#7f7672'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=93, hairline=[(8, 60), (18, 50), (50, 46), (82, 50), (92, 60)]),
  dome('front', top=6, w=44, cy=46, n=0, sb=62) +
  [band('front', WHITE, 34, 12, w=46), L(ell(50, 38, 7, 7), RED, 'f', False),
   L(outline([(8, 50), (2, 78), (10, 80), (16, 52)]), WHITE, 'f', True, True), L(outline([(92, 50), (98, 78), (90, 80), (84, 52)]), WHITE, 'f', True, True),
   L(quad((26, 64), (34, 58), (42, 64)), _c('#5a7a3a'), 'f', False, False, 2.6), L(quad((58, 64), (66, 58), (74, 64)), _c('#5a7a3a'), 'f', False, False, 2.6),
   L(ell(28, 86, 5, 3.4), _c('#e88a6a'), 'f', False), L(ell(72, 86, 5, 3.4), _c('#e88a6a'), 'f', False)],
  dome('side', top=6, w=44, cy=46, n=0, nape=84, fr=46) + [band('side', WHITE, 32, 12), L(outline([(8, 44), (-4, 72), (4, 76), (16, 48)]), WHITE, 'f', True, True)],
  dome('back', top=6, w=44, cy=46, n=0, nape=84) + [band('back', WHITE, 34, 12), L(outline([(44, 44), (34, 76), (44, 78), (50, 48), (56, 78), (66, 76), (56, 44)]), WHITE, 'f', True, True)])

# Dave Dreem (defensa): pinchos rubio crema, una cinta azul marino calada sobre la frente y un pañuelo a juego que le tapa
# la cara hasta los ojos, ninja; ojos rojos afilados y piel morena
NJ = _c('#36394d')
C('dave-dreem', 'normal', P('#fdfdd9', '#ad846e', iris='#c8281e', shade='#d8d8a8'),
  F(eyes='sharp', brows=False, mouth='none', hairline=False),
  dome('front', top=-4, w=48, cy=44, n=7, amp=14, sweep=0.4, seed=171, sb=60) +
  [band('front', NJ, 54, 12, w=48), L(outline([(10, 82), (50, 80), (90, 82), (94, 104), (80, 126), (50, 130), (20, 126), (6, 104)]), NJ, 'f', True, True),
   L(blob([(24, 70), (42, 72), (40, 78), (26, 76)], 3), _c('#c83a2a'), 'f', False), L(blob([(76, 70), (58, 72), (60, 78), (74, 76)], 3), _c('#c83a2a'), 'f', False)],
  dome('side', top=-4, w=48, cy=44, n=7, amp=14, sweep=0.4, seed=171, nape=84, fr=48) +
  [band('side', NJ, 54, 12), L(outline([(46, 82), (94, 80), (96, 104), (80, 124), (50, 126), (40, 104)]), NJ, 'f', True, True)],
  dome('back', top=-4, w=48, cy=44, n=7, amp=14, sweep=0.4, seed=171, nape=84) + [band('back', NJ, 54, 12), L(outline([(10, 90), (90, 90), (90, 112), (50, 118), (10, 112)]), NJ, 'f', True, True)])

# Debbie Dare: pelo gris verdoso recogido en dos moños redondos enormes a los lados de lo alto y un flequillo que baja en
# punta entre los ojos; ojos grandes con pestañas y el iris amarillento, sonrisa
C('debbie-dare', 'chica', P('#a2c0c1', '#f8bc7d', iris='#c8a040', shade='#82a0a1'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, hairline=[(6, 60), (18, 50), (34, 54), (46, 62), (50, 70), (54, 62), (66, 54), (82, 50), (94, 60)]),
  [L(ell(22, 14, 24, 20), 'mid', 'b'), L(ell(78, 14, 24, 20), 'mid', 'b')] + dome('front', top=10, w=44, cy=48, n=0, sb=70) +
  [L(ell(16, 8, 8, 5), 'light', 'b', False), L(ell(72, 8, 8, 5), 'light', 'b', False),
   L([(24, 72), (18, 68)], OUTC, 'f', False, False, 2), L([(76, 72), (82, 68)], OUTC, 'f', False, False, 2)],
  [L(ell(40, 8, 24, 20), 'mid', 'b')] + dome('side', top=10, w=44, cy=48, n=0, nape=86, fr=58),
  [L(ell(22, 14, 24, 20), 'mid', 'b'), L(ell(78, 14, 24, 20), 'mid', 'b')] + dome('back', top=10, w=44, cy=48, n=0, nape=86))
