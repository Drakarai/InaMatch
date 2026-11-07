"""Ojeadores de IE1 (scouts-ie1), tanda 09: dibujados a partir de su retrato de Victory Road; claves 'scouts-ie1:<id>'.

Casi ninguno tiene modelo 3D: el frente sale del retrato y el perfil y la espalda se deducen de cómo cae ese peinado.
Ayudas de esta tanda: dome() (masa de pelo en las tres vistas, lisa o de pinchos, corta o larga), hl() (nacimiento del
pelo en flecos de punta), face()/face_side() (caras más anchas, largas o de mandíbula grande) y unos pocos accesorios."""
import math
import random

from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)


def _c(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5)) + (255,)


def _ring(cx, cy, rx, ry, a0, a1, n, amp, sweep, rnd, k=1, soft=False):
    """Arco de a0 a a1 (grados, sentido horario de pantalla al bajar el ángulo) con n pinchos de largo amp (0: liso)."""
    pts = []
    if n <= 0:
        m = 14
        for i in range(m + 1):
            a = math.radians(a0 + (a1 - a0) * i / m)
            pts.append((cx + rx * math.cos(a), cy - ry * math.sin(a)))
        return pts
    for i in range(n):
        ta = math.radians(a0 + (a1 - a0) * i / n)
        tb = math.radians(a0 + (a1 - a0) * (i + 0.5 + rnd.uniform(-0.12, 0.12)) / n)
        pts.append((cx + rx * math.cos(ta), cy - ry * math.sin(ta)))
        wgt = min(1.0, max(0.25, (math.sin(tb) + 0.45) / 1.3))  # pinchos largos arriba y más cortos por los lados
        f = 1 + amp * wgt * rnd.uniform(0.55, 1.35) / max(rx, ry)
        tip = (cx + rx * f * math.cos(tb) + sweep * amp * k, cy - ry * f * math.sin(tb))
        pts.append(tip if soft else tip + (1,))
    a = math.radians(a1)
    pts.append((cx + rx * math.cos(a), cy - ry * math.sin(a)))
    return pts


def dome(view, top=6, w=46, cy=46, n=0, amp=10, sweep=0.0, seed=1, sb=62, nape=84, long=None, flare=6, fr=46, c='mid',
         shade=True, back_n=None, ends=4, side_burn=True, soft=False):
    """Masa de pelo: top = lo más alto, w = medio ancho, n pinchos de largo amp (n=0: liso), sb = hasta dónde bajan las
    patillas de frente, nape = nuca, long = largo de una melena (por los lados y detrás), fr = altura del flequillo de perfil."""
    rnd = random.Random(seed)
    ry = cy - top
    if view == 'front':
        pts = _ring(50, cy, w, ry, 200, -20, n, amp, sweep, rnd, soft=soft)
        if long:
            pts += [(50 + w + flare * 0.4, long - 18), (50 + w + flare, long, 1), (76, long - 14), (76, 56), (24, 56), (24, long - 14),
                    (50 - w - flare, long, 1), (50 - w - flare * 0.4, long - 18)]
        else:
            pts += [(50 + w * 0.95, sb, 1), (80, sb - 4), (80, 50), (20, 50), (20, sb - 4), (50 - w * 0.95, sb, 1)]
        out = [L(outline(pts), c)]
        if shade:
            out.append(L(blob([(60, top + 4), (50 + w * 0.9, cy - 6), (50 + w * 0.92, (long or sb) - 4), (72, (long or sb) - 10), (74, cy)], 6), 'shade', 'b', False))
        return out
    if view == 'side':
        pts = _ring(46, cy, w, ry, 25, 232, n, amp, -abs(sweep) * 0.5, rnd, soft=soft)
        if long:
            pts += [(6, long - 8), (4 - flare * 0.5, long, 1), (18, long - 6), (30, long, 1), (44, long - 12), (54, long - 26), (54, 72)]
        else:
            pts += [(26, nape), (42, nape + 1), (52, 80 if side_burn else 64), (53, 62)]
        pts += [(62, fr + 2), (78, fr + 3), (46 + w * 0.97, fr - 4, 1)]
        out = [L(outline(pts), c)]
        if shade:
            out.append(L(blob([(4, cy + 2), (16, cy + 16), (36, (long or nape) - 6), (24, (long or nape) - 1), (8, (long or nape) - 10)], 6), 'shade', 'b', False))
        return out
    nb = n if back_n is None else back_n
    pts = _ring(50, cy, w, ry, 195, -15, nb, amp, sweep, rnd, soft=soft)
    if long:
        R0, L0 = 50 + w + flare, 50 - w - flare
        pts += [(50 + w + flare * 0.4, long - 18), (R0, long, 1)]
        for i in range(ends):
            x = R0 - (i + 1) * (R0 - L0) / (ends + 1)
            pts += [(x + 6, long - 8), (x, long + 4, 1)]
        pts += [(L0, long, 1), (50 - w - flare * 0.4, long - 18)]
    else:
        pts += [(50 + w * 0.9, nape - 10), (68, nape - 1), (50, nape + 1), (32, nape - 1), (50 - w * 0.9, nape - 10)]
    out = [L(outline(pts), c)]
    if shade:
        out.append(L(blob([(58, top + 4), (50 + w * 0.92, cy), (50 + w * 0.85, (long or nape) - 6), (62, (long or nape) - 2), (66, cy)], 6), 'shade', 'b', False))
    return out


def hl(n=5, side=62, base=48, tip=58, x0=16, x1=84, lean=0.0, jit=0, seed=0):
    """Nacimiento del pelo de frente con n mechones de punta (tip) entre bases (base); side = altura en las sienes."""
    rnd = random.Random(seed)
    pts = [(x0 - 10, side)]
    for i in range(n):
        xb = x0 + (x1 - x0) * i / n
        xt = x0 + (x1 - x0) * (i + 0.5) / n + lean
        pts += [(xb, base + rnd.uniform(-jit, jit)), (xt, tip + rnd.uniform(-jit, jit))]
    pts += [(x1, base), (x1 + 10, side)]
    return pts


def face(w=0, chin=100, jaw=0, top=26):
    """Cara de frente: w la ensancha, chin baja la barbilla, jaw abre la mandíbula."""
    return quad((19 - w, 52), (17 - w - jaw, 92), (50, chin)) + quad((50, chin), (83 + w + jaw, 92), (81 + w, 52))[1:] + quad((81 + w, 52), (50, top), (19 - w, 52))[1:-1]


def face_side(chin=0, jaw=0, nose=0):
    return blob([(48, 20), (72, 24), (85, 40), (87, 62), (87 + nose, 70), (87 + jaw * 0.3, 82), (82 + jaw * 0.3, 96 + chin), (72, 102 + chin),
                 (58, 101 + chin), (42, 94 + chin * 0.6), (24, 80), (16, 58), (24, 32)])


def F(**k):
    """Datos de la cara con valores de partida."""
    d = {'eyes': 'normal', 'mouth': 'line'}
    d.update(k)
    return d


def P(hair, skin, iris='#302232', **k):
    return pal(hair, skin, iris, **k)


def C(pid, body, palette, f, front, side, back):
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        # el nacimiento del pelo baja por el borde de la cara hasta la barbilla: así su raya no cruza el pelo de los lados
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[f'scouts-ie1:{pid}'] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def mark(pts, c, z='f', w=0):
    """Mancha o pintura de la cara (forma rellena) o una raya (w > 0)."""
    return L(pts, c, z, False, False, w) if w else L(blob(pts, 4) if len(pts) > 2 else pts, c, z, False)


def side_x(x):
    """De frente a perfil: la mitad derecha de la cara (x de 50 a 90) queda delante, entre 62 y 90."""
    return 62 + (x - 50) * 0.7


# ------------------------------------------------------------------ jugadores

def horn(x, y, tx, ty, c):
    return L(outline([(x - 6, y + 4), (tx, ty, 1), (x + 6, y + 2)]), c, 'f')


# Pascal Richter: rizos castaño rojizo en bola y dos cuernos amarillos encima; cejas gruesas fruncidas y ojos redondos
YEL = _c('#f0c040')
C('pascal-richter', 'normal', P('#a8501e', '#f4c08a'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=92, hairline=hl(6, 64, 50, 56, jit=2, seed=3)),
  dome('front', top=0, w=50, cy=44, n=12, amp=6, soft=True, sb=70, seed=2) + [horn(26, 10, 14, -12, YEL), horn(74, 10, 88, -12, YEL)],
  dome('side', top=0, w=48, cy=44, n=12, amp=6, soft=True, nape=88, fr=50, seed=2) + [horn(50, 6, 50, -16, YEL)],
  dome('back', top=0, w=50, cy=44, n=12, amp=6, soft=True, nape=88, seed=2) + [horn(26, 10, 14, -12, YEL), horn(74, 10, 88, -12, YEL)])

# Pat Greene: afro rubio claro encima y castaño por los lados; dos parches azul grisáceo bajo los ojos y una tirita en la nariz
GB = _c('#4a6a84')
C('pat-greene', 'normal', P('#e8c878', '#f4caa0', light='#f4e2b0', low='#a8703a'),
  F(eyes='dot', brows=True, mouth='frown', mouth_y=93, hairline=[(6, 66), (20, 52), (34, 46), (50, 44), (66, 46), (80, 52), (94, 66)],
    nose=(50, 84, 3.4)),
  [L(outline([(6, 76), (4, 54), (16, 40), (84, 40), (96, 54), (94, 76), (82, 70), (18, 70)]), 'low')] +
  dome('front', top=-2, w=46, cy=38, n=11, amp=6, soft=True, sb=52, seed=4, shade=False) +
  [mark([(25, 80), (41, 80), (41, 88), (25, 88)], GB), mark([(59, 80), (75, 80), (75, 88), (59, 88)], GB),
   mark([(45, 82), (55, 82), (55, 87), (45, 87)], _c('#f8dcb8'))],
  [L(outline([(10, 50), (40, 52), (54, 62), (52, 84), (28, 90), (8, 78)]), 'low')] +
  dome('side', top=-2, w=46, cy=38, n=11, amp=6, soft=True, nape=60, fr=44, seed=4, shade=False) +
  [mark([(74, 80), (86, 80), (86, 88), (74, 88)], GB)],
  [L(outline([(6, 80), (4, 54), (96, 54), (94, 80), (70, 90), (30, 90)]), 'low')] +
  dome('back', top=-2, w=46, cy=38, n=11, amp=6, soft=True, nape=60, seed=4, shade=False))

# Pat MacLean: gorro de punto caqui con una franja de zigzag crema en medio y el borde crema; asoma pelo verde por los
# lados; nariz redonda naranja
KH, CR = _c('#a89858'), _c('#efe6c8')
def _beanie(view):
    if view == 'front':
        return [L(outline([(6, 62), (8, 30), (24, 8), (50, 0), (76, 8), (92, 30), (94, 62), (50, 58)]), KH),
                L(outline([(7, 58), (50, 52), (93, 58), (92, 67), (50, 62), (8, 67)]), CR, 'b', True, True),
                L(outline([(46, 2), (54, 2), (55, 54), (45, 54)]), CR, 'b', False),
                L(ell(50, -1, 5, 4), KH)]
    if view == 'side':
        return [L(outline([(8, 70), (2, 40), (20, 8), (48, 0), (76, 8), (92, 30), (94, 54), (60, 58), (30, 66)]), KH),
                L(outline([(6, 66), (40, 58), (93, 50), (93, 59), (40, 67), (9, 74)]), CR, 'b', True, True),
                L(outline([(44, 2), (52, 2), (34, 62), (26, 62)]), CR, 'b', False), L(ell(48, -1, 5, 4), KH)]
    return [L(outline([(6, 70), (6, 30), (24, 8), (50, 0), (76, 8), (94, 30), (94, 70), (50, 66)]), KH),
            L(outline([(7, 66), (50, 60), (93, 66), (92, 75), (50, 70), (8, 75)]), CR, 'b', True, True),
            L(outline([(46, 2), (54, 2), (55, 62), (45, 62)]), CR, 'b', False), L(ell(50, -1, 5, 4), KH)]
C('pat-maclean', 'normal', P('#7ab040', '#f4c08a'),
  F(eyes='dot', brows=True, mouth='frown', mouth_y=93, hairline=False, nose=(50, 84, 3.6), eye_y=77),
  [L(outline([(6, 60), (2, 72), (12, 78), (16, 66)])), L(outline([(94, 60), (98, 72), (88, 78), (84, 66)]))] + _beanie('front'),
  [L(outline([(52, 62), (44, 74), (56, 78), (60, 64)]))] + _beanie('side'),
  _beanie('back') + [L(outline([(10, 72), (20, 84), (40, 80), (60, 80), (80, 84), (90, 72)]))])

# Pat Shinko: pelo naranja en mechones de punta echados a un lado, cara larga morena, labios gruesos sonrientes
C('pat-shinko', 'delgado', P('#e07428', '#c88a50', iris='#3a2a20'),
  F(eyes='sharp', brows='angry', mouth='lips', mouth_y=97, mouth_w=10, face_front=face(chin=108, jaw=1), face_side=face_side(chin=7),
    hairline=[(6, 64), (18, 46), (30, 40), (44, 46), (58, 38), (72, 44), (86, 50), (94, 64)], nose=(50, 86, 3)),
  dome('front', top=-4, w=46, cy=44, n=6, amp=16, sweep=0.6, seed=7, sb=70),
  dome('side', top=-4, w=46, cy=44, n=6, amp=16, sweep=0.6, seed=7, nape=86, fr=46),
  dome('back', top=-4, w=46, cy=44, n=6, amp=16, sweep=0.6, seed=7, nape=86))

# Patch Borgnine: pinchos naranjas altísimos hacia arriba, un mechón verde que le cae por el centro de la cara y un
# antifaz rojo con los agujeros blancos
GR, RD = _c('#4a9a50'), _c('#c83a2a')
def _mask(view):
    if view == 'front':
        return [L(outline([(14, 66), (16, 74), (30, 84), (44, 80), (50, 74), (56, 80), (70, 84), (84, 74), (86, 66), (70, 68), (50, 70), (30, 68)]), RD, 'f'),
                L(outline([(24, 72), (40, 74), (44, 78), (30, 79)]), WHITE, 'f', False), L(outline([(76, 72), (60, 74), (56, 78), (70, 79)]), WHITE, 'f', False)]
    return [L(outline([(54, 66), (90, 64), (92, 74), (82, 82), (56, 76)]), RD, 'f'), L(outline([(76, 70), (88, 70), (86, 76), (78, 76)]), WHITE, 'f', False)]
C('patch-borgnine', 'normal', P('#d8862e', '#f4c08a', shade='#b8661e'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=92, hairline=[(6, 70), (18, 50), (50, 46), (82, 50), (94, 70)]),
  [L(outline([(10, 70), (6, 40), (4, -6, 1), (18, 20), (24, -26, 1), (34, 10), (42, -34, 1), (50, 6), (60, -34, 1), (66, 10), (78, -26, 1), (82, 20), (96, -6, 1),
              (94, 40), (90, 70), (80, 56), (20, 56)])),
   L(outline([(56, -10), (60, -34), (66, 10), (78, -26), (82, 20), (96, -6), (94, 40), (90, 66), (78, 40)]), 'shade', 'b', False)] + _mask('front') +
  [L(outline([(44, 40), (52, 30), (58, 44), (56, 66), (50, 80, 1), (46, 62)]), GR, 'f')],
  [L(outline([(54, 70), (60, 54), (84, 50), (96, 30), (92, 10, 1), (76, 14), (78, -24, 1), (60, 6), (50, -32, 1), (40, 6), (24, -24, 1), (20, 12), (2, 4, 1),
              (8, 34), (6, 60), (22, 80), (40, 80), (50, 74)]))] + _mask('side') +
  [L(outline([(80, 40), (92, 36), (94, 60), (90, 74, 1), (86, 56)]), GR, 'f')],
  [L(outline([(10, 80), (6, 40), (4, -6, 1), (18, 20), (24, -26, 1), (34, 10), (42, -34, 1), (50, 6), (60, -34, 1), (66, 10), (78, -26, 1), (82, 20), (96, -6, 1),
              (94, 40), (90, 80), (50, 86)])),
   L(outline([(56, -10), (60, -34), (66, 10), (78, -26), (82, 20), (96, -6), (94, 40), (90, 78), (70, 60)]), 'shade', 'b', False),
   L(outline([(14, 66), (86, 66), (86, 72), (14, 72)]), RD, 'f')])

# Patch Upright: pelo verde oscuro alborotado en pinchos, con un mechón que baja por la frente; cejas gruesas y sonrisa ladeada
C('patch-upright', 'normal', P('#2a6a40', '#f4c08a', iris='#2a2020'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=92, hairline=hl(5, 64, 46, 58, lean=1, jit=3, seed=5)),
  dome('front', top=0, w=48, cy=44, n=8, amp=11, seed=8, sb=68) + [L(outline([(44, 36), (52, 32), (54, 50), (50, 62, 1), (46, 50)]), 'mid', 'f')],
  dome('side', top=0, w=48, cy=44, n=8, amp=11, seed=8, nape=88, fr=50),
  dome('back', top=0, w=48, cy=44, n=8, amp=11, seed=8, nape=88))

# Patrick Edie: pelo crema claro echado a un lado y un mechón naranja que le cae por la frente; ojos redondos negros
OR = _c('#e08a3a')
C('patrick-edie', 'normal', P('#efe6b0', '#f4c08a', iris='#1e1a1a', brow='#c86a2a'),
  F(eyes='round', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 64), (18, 48), (36, 44), (58, 42), (78, 46), (94, 62)]),
  dome('front', top=0, w=47, cy=44, n=6, amp=8, sweep=0.8, seed=11, sb=64) +
  [L(outline([(38, 28), (58, 26), (60, 46), (52, 66, 1), (46, 48), (40, 42)]), OR, 'f')],
  dome('side', top=0, w=47, cy=44, n=6, amp=8, sweep=0.8, seed=11, nape=84, fr=46) + [L(outline([(78, 30), (92, 34), (92, 52), (88, 60, 1), (84, 44)]), OR, 'f')],
  dome('back', top=0, w=47, cy=44, n=6, amp=8, sweep=0.8, seed=11, nape=84))

# Patsy Cornish: una mata enorme de pelo castaño anaranjado en pinchos anchos que tapan la frente; cara ancha, ojos de
# gato entornados, nariz naranja y boca de gato con un colmillo
C('patsy-cornish', 'corpulento', P('#c8641e', '#f4c08a', iris='#1e1a1a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, face_front=face(w=6, chin=102, jaw=3), nose=(50, 85, 2.6), ear_out=6,
    hairline=[(6, 66), (10, 58), (22, 66), (28, 54), (40, 64), (48, 52), (60, 62), (68, 52), (80, 64), (88, 56), (94, 66)]),
  dome('front', top=0, w=56, cy=46, n=7, amp=14, seed=12, sb=66) +
  [L(quad((50, 94), (51, 99), (53, 94)) + [(53, 94)], WHITE, 'f', False), L([(49, 94), (52, 99), (54, 94)], OUTC, 'f', False, False, 1.0)],
  dome('side', top=0, w=52, cy=46, n=7, amp=14, seed=12, nape=88, fr=56),
  dome('back', top=0, w=56, cy=46, n=7, amp=14, seed=12, nape=88))

# Paul Chucker (portero): casco de pelo verde oliva corto y redondo, cara enorme de mandíbula ancha, orejas grandes, cejas
# negras gruesas, nariz grande, boca abierta en O y dos rayos verdes pintados en las mejillas
LG = _c('#3a8a4a')
C('paul-chucker', 'corpulento', P('#6a5a28', '#e0a464'),
  F(eyes='round', brows=True, mouth='none', face_front=face(w=8, chin=106, jaw=6), face_side=face_side(chin=6, jaw=6), big_ears=2, ear_out=6,
    hairline=[(6, 62), (14, 50), (30, 46), (50, 44), (70, 46), (86, 50), (94, 62)], nose=(50, 84, 5)),
  dome('front', top=2, w=50, cy=46, sb=58) +
  [L([(28, 62), (36, 58), (44, 62)], OUTC, 'f', False, False, 3.6), L([(56, 62), (64, 58), (72, 62)], OUTC, 'f', False, False, 3.6),
   L(ell(50, 96, 6, 6.5), _c('#8a4a24'), 'f', True), L(ell(50, 96, 2, 2.2), _c('#3a2016'), 'f', False),
   L(outline([(14, 82), (26, 80), (20, 86), (30, 88)]), LG, 'f', False, False, 2.2), L(outline([(86, 82), (74, 80), (80, 86), (70, 88)]), LG, 'f', False, False, 2.2)],
  dome('side', top=2, w=48, cy=46, nape=80, fr=44) + [L([(70, 80), (80, 78), (74, 84), (82, 86)], LG, 'f', False, False, 2.2)],
  dome('back', top=2, w=50, cy=46, nape=80))

# Paul Downs: melena granate oscuro hasta el cuello, con un mechón rosa que le tapa un ojo; labios lila y pendiente en la nariz
PK = _c('#d87a80')
C('paul-downs', 'delgado', P('#6a2a3a', '#f8dcc0', iris='#2a2028'),
  F(eyes='sharp', brows='angry', mouth='none', eye_sep=13, hairline=[(6, 70), (18, 48), (34, 42), (56, 44), (74, 46), (86, 56), (94, 70)]),
  dome('front', top=0, w=46, cy=44, n=5, amp=10, sweep=0.6, seed=21, long=96, flare=4) +
  [L(outline([(40, 30), (66, 30), (72, 56), (68, 84), (62, 96, 1), (56, 80), (52, 60)]), PK, 'f'),
   L(ell(55, 87, 1.4, 1.4), (200, 200, 210, 255), 'f', False), L(ell(50, 93, 5, 2.4), _c('#b8a0c8'), 'f', True)],
  dome('side', top=0, w=46, cy=44, n=5, amp=10, sweep=0.6, seed=21, long=96, flare=4, fr=50) +
  [L(outline([(70, 30), (92, 36), (94, 60), (88, 82, 1), (82, 60)]), PK, 'f')],
  dome('back', top=0, w=46, cy=44, n=5, amp=10, sweep=0.6, seed=21, long=96, flare=4))

# Paul Pitcher: rapado crema con entradas en pico, orejas grandes, cara larga; cejas fruncidas y la boca muy abierta
C('paul-pitcher', 'normal', P('#f0e6c0', '#f4c08a'),
  F(eyes='sharp', brows='angry', mouth='none', face_front=face(w=2, chin=108, jaw=2), face_side=face_side(chin=8), big_ears=2, ear_out=3,
    hairline=[(16, 58), (24, 40), (38, 34), (50, 44), (62, 34), (76, 40), (84, 58)]),
  dome('front', top=10, w=40, cy=46, sb=58, shade=False) +
  [L(ell(50, 96, 9, 6), _c('#b06a50'), 'f', True), L([(43, 96), (57, 96)], OUTC, 'f', False, False, 1.2)],
  dome('side', top=10, w=40, cy=46, nape=78, fr=40, shade=False, side_burn=False),
  dome('back', top=10, w=40, cy=46, nape=78, shade=False))

# Paul Rush: pelo morado oscuro muy alborotado en pinchos, con mechones que le caen por los lados hasta el cuello
C('paul-rush', 'normal', P('#4a2a5a', '#f4c08a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=92, hairline=hl(5, 66, 48, 58, jit=3, seed=9)),
  dome('front', top=-2, w=48, cy=44, n=9, amp=13, seed=22, long=90, flare=8),
  dome('side', top=-2, w=48, cy=44, n=9, amp=13, seed=22, long=90, flare=8, fr=52),
  dome('back', top=-2, w=48, cy=44, n=9, amp=13, seed=22, long=90, flare=8, ends=5))

# Paul Sapp: pelo crema liso peinado de lado, que le cae sobre la frente; dos uves azules pintadas bajo los ojos, ojos entornados
BLU = _c('#2a4a8a')
C('paul-sapp', 'normal', P('#efe2c4', '#f4c08a'),
  F(eyes='closed', brows=True, mouth='smile', mouth_y=92, face_front=face(w=3, chin=100, jaw=2),
    hairline=[(6, 66), (18, 54), (30, 48), (50, 52), (70, 58), (84, 60), (94, 68)]),
  dome('front', top=8, w=46, cy=48, sb=64) + [L(outline([(16, 44), (40, 30), (70, 34), (92, 56, 1), (70, 52), (40, 48)]), 'mid', 'f')] +
  [L([(24, 82), (30, 90), (36, 82)], BLU, 'f', False, False, 2.6), L([(64, 82), (70, 90), (76, 82)], BLU, 'f', False, False, 2.6)],
  dome('side', top=8, w=46, cy=48, nape=84, fr=52) + [L([(74, 82), (78, 90), (84, 82)], BLU, 'f', False, False, 2.6)],
  dome('back', top=8, w=46, cy=48, nape=84))

# Pauly Ontology: pelo rosa en pinchos revueltos, ojos verdes grandes y sonrisa
C('pauly-ontology', 'normal', P('#d07070', '#f4c08a', iris='#4a9a3a'),
  F(eyes='big', brows='angry', mouth='smile', mouth_y=93, hairline=hl(5, 66, 48, 60, lean=-1, jit=3, seed=13)),
  dome('front', top=-2, w=48, cy=44, n=8, amp=14, sweep=0.4, seed=23, sb=74),
  dome('side', top=-2, w=48, cy=44, n=8, amp=14, sweep=0.4, seed=23, nape=90, fr=54),
  dome('back', top=-2, w=48, cy=44, n=8, amp=14, sweep=0.4, seed=23, nape=90))

# Pay Chance (portero): pelo verde en pinchos que se abren a los lados como una palmera, con un mechón naranja que le cae
# por el centro; mandíbula ancha, ceño fruncido y los dientes apretados
C('pay-chance', 'corpulento', P('#6aa040', '#f6cfa0'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=97, face_front=face(w=6, chin=106, jaw=6), face_side=face_side(chin=6, jaw=4), ear_out=4,
    hairline=[(6, 60), (16, 46), (32, 40), (50, 36), (68, 40), (84, 46), (94, 60)]),
  dome('front', top=-4, w=56, cy=44, n=10, amp=14, seed=24, sb=60) + [L(outline([(44, -2), (54, -6), (56, 30), (54, 62, 1), (48, 34)]), _c('#e07020'), 'f')],
  dome('side', top=-4, w=52, cy=44, n=10, amp=14, seed=24, nape=82, fr=40) + [L(outline([(60, -4), (72, -6), (84, 24), (88, 48, 1), (76, 26)]), _c('#e07020'), 'f')],
  dome('back', top=-4, w=56, cy=44, n=10, amp=14, seed=24, nape=82))

# Penfold Pulper: pelo verde agua recogido en un moño alto atado con una cinta amarilla, flequillo de mechones y dos mechones
# largos que le caen junto a la cara; ojos grandes azul claro
TEAL = '#5aa0a0'
def _topknot(x, y):
    return [L(outline([(x - 12, y + 10), (x - 18, y - 10, 1), (x - 6, y - 2), (x, y - 16, 1), (x + 6, y - 2), (x + 18, y - 10, 1), (x + 12, y + 10)])),
            L(outline([(x - 8, y + 6), (x + 8, y + 6), (x + 8, y + 14), (x - 8, y + 14)]), _c('#e8d27a'))]
C('penfold-pulper', 'normal', P(TEAL, '#f6cfa0', iris='#7ac8d8'),
  F(eyes='big', brows='angry', mouth='line', mouth_y=93, hairline=hl(5, 70, 46, 60, jit=3, seed=14)),
  _topknot(50, -4) + dome('front', top=6, w=46, cy=46, sb=64) +
  [L(outline([(10, 50), (18, 60), (22, 96, 1), (14, 80)])), L(outline([(90, 50), (82, 60), (78, 96, 1), (86, 80)]))],
  _topknot(40, -2) + dome('side', top=6, w=46, cy=46, nape=84, fr=56) + [L(outline([(54, 58), (62, 62), (60, 96, 1), (52, 80)]))],
  _topknot(50, -4) + dome('back', top=6, w=46, cy=46, nape=84))

# Per Hockside: melena hasta el cuello granate oscuro, de puntas abiertas, con el flequillo verde oliva partido en dos
# cortinas; ojos azul claro y sonrisa
OLV = _c('#a8a840')
C('per-hockside', 'delgado', P('#6a3a4a', '#f4c08a', iris='#7ac0d0'),
  F(eyes='normal', brows='angry', mouth='smile', mouth_y=93, face_front=face(chin=104), face_side=face_side(chin=4),
    hairline=[(6, 70), (18, 54), (30, 44), (46, 40), (50, 46), (54, 40), (70, 44), (82, 54), (94, 70)]),
  dome('front', top=0, w=47, cy=44, n=6, amp=8, seed=31, long=90, flare=10) +
  [L(outline([(20, 46), (34, 32), (50, 34), (44, 46), (30, 62, 1), (26, 52)]), OLV, 'f'), L(outline([(80, 46), (66, 32), (50, 34), (56, 46), (70, 62, 1), (74, 52)]), OLV, 'f')],
  dome('side', top=0, w=47, cy=44, n=6, amp=8, seed=31, long=88, flare=10, fr=50) + [L(outline([(70, 30), (90, 36), (92, 50), (84, 62, 1), (80, 46)]), OLV, 'f')],
  dome('back', top=0, w=47, cy=44, n=6, amp=8, seed=31, long=88, flare=10, ends=5))

# Percy Coldstair: casco de pelo azul brillante cortado en media melena, con el flequillo en puntas que le tapa la frente;
# sombra azul en los párpados
C('percy-coldstair', 'normal', P('#1e6a98', '#f4c08a', iris='#6a3a20', light='#5aa8d8'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=93, hairline=[(6, 76), (18, 56), (30, 66), (36, 52), (44, 70), (50, 54), (58, 72), (64, 54), (72, 66), (80, 56), (94, 76)]),
  dome('front', top=0, w=48, cy=46, long=88, flare=0) + [L(outline([(30, 14), (46, 8), (40, 22)]), 'light', 'b', False),
  L([(24, 70), (40, 72)], _c('#5a9ad0'), 'f', False, False, 2.0), L([(76, 70), (60, 72)], _c('#5a9ad0'), 'f', False, False, 2.0)],
  dome('side', top=0, w=48, cy=46, long=86, flare=0, fr=62) + [L(outline([(36, 10), (56, 6), (46, 18)]), 'light', 'b', False)],
  dome('back', top=0, w=48, cy=46, long=86, flare=0, ends=0))

# Percy Stent (portero): cara redonda y mofletuda, pelo castaño oscuro corto con dos picos como cuernecillos y un rizo en
# la frente; nariz naranja y ceño fruncido
C('percy-stent', 'corpulento', P('#4a3020', '#f2b878'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=95, face_front=face(w=6, chin=102, jaw=5), nose=(50, 86, 3.6), ear_out=5,
    hairline=[(6, 62), (16, 50), (30, 46), (44, 50), (52, 60), (60, 50), (74, 46), (86, 50), (94, 62)]),
  dome('front', top=10, w=48, cy=48, sb=60) + [horn(24, 16, 16, -2, 'mid'), horn(76, 16, 86, -2, 'mid'),
  L(outline([(46, 40), (58, 34), (62, 46), (54, 52), (52, 44)]), 'mid', 'f')],
  dome('side', top=10, w=46, cy=48, nape=80, fr=50) + [horn(56, 12, 60, -4, 'mid')],
  dome('back', top=10, w=48, cy=48, nape=80) + [horn(24, 16, 16, -2, 'mid'), horn(76, 16, 86, -2, 'mid')])

# Percy Verence: tupé gris verdoso peinado hacia arriba, orejas grandes, gafas redondas grandes de montura negra y la boca
# abierta en una sonrisa
C('percy-verence', 'normal', P('#6a9aa0', '#f8d4b0', iris='#2a2028'),
  F(eyes='dot', brows='angry', mouth='none', glasses=BLACK, big_ears=3, ear_out=4,
    hairline=[(6, 60), (22, 44), (40, 38), (60, 38), (78, 44), (94, 60)]),
  [L(outline([(14, 60), (12, 30), (24, 6), (40, -6), (60, -10, 1), (66, 0), (82, 10), (90, 30), (86, 60), (78, 48), (22, 48)])),
   L(outline([(56, -6), (82, 10), (90, 32), (86, 56), (74, 30)]), 'shade', 'b', False), strand([(30, 30), (44, 6), (58, -6)], 'deep', 'b', 1.0)] +
  [L(ell(50, 93, 5, 4), _c('#c04a40'), 'f', True), L(outline([(46, 90), (54, 90), (53, 92), (47, 92)]), WHITE, 'f', False)],
  [L(outline([(52, 62), (52, 80), (40, 84), (24, 82), (8, 66), (4, 40), (14, 14), (36, 0), (64, -8, 1), (70, 4), (86, 16), (92, 34), (78, 40), (62, 46)])),
   L(outline([(6, 44), (20, 50), (36, 76), (22, 80), (8, 64)]), 'shade', 'b', False)],
  dome('back', top=-4, w=44, cy=42, nape=80))

# Percy Wrench: piel oscura, cara anchísima, pelo azul marino en pinchos arriba y a los lados; ojos redondos, nariz grande
# y una sonrisa recta y ancha
C('percy-wrench', 'corpulento', P('#2a3a5a', '#8a6448'),
  F(eyes='round', brows='angry', mouth='line', mouth_y=97, face_front=face(w=10, chin=104, jaw=8), face_side=face_side(chin=4, jaw=6), ear_out=8,
    nose=(50, 86, 4.4), hairline=[(6, 62), (10, 50), (30, 44), (50, 42), (70, 44), (90, 50), (94, 62)]),
  dome('front', top=-2, w=56, cy=44, n=9, amp=16, seed=33, sb=72) +
  [L([(38, 97), (62, 97)], OUTC, 'f', False, False, 1.6)],
  dome('side', top=-2, w=52, cy=44, n=9, amp=16, seed=33, nape=86, fr=44),
  dome('back', top=-2, w=56, cy=44, n=9, amp=16, seed=33, nape=86))

# Perry Pincher: pelo verde azulado con dos picos arriba como orejas de gato y la frente en uve; ojos negros grandes
C('perry-pincher', 'normal', P('#5a9a90', '#f4c08a', iris='#1e1a1a'),
  F(eyes='big', brows='angry', mouth='smile', mouth_y=93, hairline=[(6, 66), (18, 46), (34, 44), (50, 62), (66, 44), (82, 46), (94, 66)]),
  [L(outline([(12, 66), (8, 30), (4, -8, 1), (30, 12), (50, 8), (70, 12), (96, -8, 1), (92, 30), (88, 66), (78, 52), (22, 52)])),
   L(outline([(60, 10), (96, -8), (92, 30), (88, 62), (74, 30)]), 'shade', 'b', False),
   strand([(30, 18), (36, 40)], 'deep', 'b', 1.0), strand([(50, 12), (50, 36)], 'deep', 'b', 1.0), strand([(70, 18), (64, 40)], 'deep', 'b', 1.0)],
  [L(outline([(54, 66), (60, 52), (80, 46), (92, 30), (88, 12), (70, 4), (40, -10, 1), (34, 6), (16, 12), (4, 34), (6, 62), (22, 80), (40, 82), (52, 78)])),
   L(outline([(6, 40), (24, 48), (40, 76), (24, 80), (8, 62)]), 'shade', 'b', False)],
  [horn(18, 22, 6, -8, 'mid'), horn(82, 22, 94, -8, 'mid')] + dome('back', top=6, w=46, cy=46, nape=84))

# Pete Grimes (portero): piel morena, cara larga, pelo verde azulado echado sobre un lado de la frente y con las puntas
# abiertas sobre las orejas; los dientes apretados
C('pete-grimes', 'delgado', P('#4a9a90', '#8a6040', iris='#c8a040'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=98, face_front=face(chin=108, jaw=1), face_side=face_side(chin=8), nose=(50, 86, 3),
    hairline=[(6, 64), (18, 46), (40, 40), (70, 50), (86, 60), (94, 66)]),
  dome('front', top=2, w=46, cy=46, sb=66) + [L(outline([(6, 60), (-2, 70, 1), (12, 68)])), L(outline([(94, 60), (102, 70, 1), (88, 68)])),
  L(outline([(18, 44), (46, 30), (76, 42), (92, 64, 1), (70, 58), (44, 50), (26, 54)]), 'mid', 'f')],
  dome('side', top=2, w=46, cy=46, nape=84, fr=52) + [L(outline([(50, 66), (40, 74, 1), (52, 76)]))],
  dome('back', top=2, w=46, cy=46, nape=84) + [L(outline([(8, 66), (-2, 74, 1), (12, 76)])), L(outline([(92, 66), (102, 74, 1), (88, 76)]))])

# Pete Legume: media melena azul marino con un mechón que le cae sobre un ojo y otro largo hasta el cuello por un lado;
# ojos verde agua
C('pete-legume', 'normal', P('#2a3a5a', '#f4c08a', iris='#5ab0b0'),
  F(eyes='normal', brows='angry', mouth='smile', mouth_y=93, hairline=[(6, 70), (18, 52), (30, 64), (40, 50), (52, 66), (62, 50), (76, 58), (94, 70)]),
  dome('front', top=0, w=47, cy=46, sb=70) + [L(outline([(8, 60), (16, 64), (12, 100, 1), (4, 80)])),
  L(outline([(36, 40), (56, 36), (58, 56), (50, 74, 1), (44, 54)]), 'mid', 'f')],
  dome('side', top=0, w=47, cy=46, nape=86, fr=58),
  dome('back', top=0, w=47, cy=46, nape=86) + [L(outline([(92, 60), (84, 64), (88, 100, 1), (96, 80)]))])

# Pete Nokeyo: pelo verde oliva corto peinado hacia atrás con tres mechones de punta arriba y patillas largas; párpados
# caídos sobre ojos verde agua
C('pete-nokeyo', 'normal', P('#6a8a3a', '#f4c08a', iris='#5a9a90'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=[(6, 76), (16, 56), (26, 44), (50, 40), (74, 44), (84, 56), (94, 76)]),
  dome('front', top=12, w=44, cy=50, sb=82) + [horn(36, 14, 30, -6, 'mid'), horn(50, 12, 52, -10, 'mid'), horn(64, 14, 72, -6, 'mid')],
  dome('side', top=12, w=44, cy=50, nape=84, fr=42) + [horn(46, 12, 40, -8, 'mid'), horn(60, 14, 64, -6, 'mid')],
  dome('back', top=12, w=44, cy=50, nape=84) + [horn(36, 14, 30, -6, 'mid'), horn(50, 12, 52, -10, 'mid'), horn(64, 14, 72, -6, 'mid')])

# Pete Pang (portero): casco de pelo rubio claro con la parte de abajo más oscura, que le tapa la frente; ojos cerrados,
# pecas, nariz redonda naranja y cara redonda
C('pete-pang', 'corpulento', P('#e8e0a0', '#f2b878', low='#a89870'),
  F(eyes='closed', brows=False, mouth='smile', mouth_y=95, face_front=face(w=6, chin=102, jaw=4), nose=(50, 86, 4.4), ear_out=5,
    hairline=[(6, 74), (12, 62), (30, 64), (50, 60), (70, 66), (88, 62), (94, 74)]),
  [L(outline([(4, 76), (2, 50), (98, 50), (96, 76), (84, 70), (16, 70)]), 'low')] + dome('front', top=0, w=50, cy=46, sb=60, shade=False) +
  [L(outline([(8, 46), (30, 40), (50, 46), (72, 40), (92, 46), (92, 62), (70, 64), (50, 58), (30, 64), (8, 62)]), 'mid', 'b', False)] +
  [L(ell(x, y, 0.9, 0.9), _c('#c87a4a'), 'f', False) for x, y in ((26, 84), (30, 88), (24, 89), (74, 84), (70, 88), (76, 89))],
  [L(outline([(6, 56), (40, 58), (54, 64), (52, 84), (26, 86), (6, 76)]), 'low')] + dome('side', top=0, w=48, cy=46, nape=64, fr=62, shade=False),
  [L(outline([(4, 80), (2, 54), (98, 54), (96, 80), (50, 88)]), 'low')] + dome('back', top=0, w=50, cy=46, nape=66, shade=False))

# Pete Sadow: piel pálida grisácea, cresta azul acero peinada hacia un lado que le cae larga junto a la mejilla, con el
# resto rapado; ojos redondos con el borde rojo
C('pete-sadow', 'delgado', P('#5a8aa8', '#e6dac6', iris='#1e1a1a', buzz='#cfc4b0'),
  F(eyes='round', brows='angry', mouth='smile', mouth_y=94, face_front=face(chin=104), face_side=face_side(chin=4), hairline=False),
  [L(outline([(16, 60), (14, 36), (30, 16), (50, 10), (70, 16), (86, 36), (84, 60), (80, 50), (20, 50)]), 'buzz', 'b', False),
   L(outline([(36, 18), (52, -4), (76, 6), (92, 30), (92, 64), (86, 90, 1), (80, 60), (70, 30), (56, 20)])),
   L(outline([(66, 6), (84, 18), (90, 50), (86, 80), (80, 44)]), 'shade', 'b', False)] +
  [L(ell(36, 75, 5.4, 5.4), _c('#c03a3a'), 'b', False), L(ell(64, 75, 5.4, 5.4), _c('#c03a3a'), 'b', False)],
  [L(outline([(52, 62), (40, 78), (14, 70), (6, 40), (24, 14), (50, 8), (76, 14), (90, 32), (82, 40), (60, 44)]), 'buzz', 'b', False),
   L(outline([(20, 30), (40, 0), (70, 0), (92, 18), (98, 40, 1), (80, 30), (60, 24), (40, 34)]))],
  [L(outline([(16, 76), (12, 40), (30, 16), (50, 10), (70, 16), (88, 40), (84, 76), (50, 82)]), 'buzz', 'b', False),
   L(outline([(40, 6), (54, -4), (66, 6), (64, 60), (50, 80, 1), (40, 60)]))])

# Peter Malus: piel tostada, cabeza redonda rapada con el pelo verde oliva muy corto, orejas grandes; ojos entornados
C('peter-malus', 'corpulento', P('#8a8a50', '#c8925a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=95, face_front=face(w=6, chin=102, jaw=4), big_ears=2, ear_out=6, nose=(50, 86, 3.6),
    hairline=[(6, 66), (16, 50), (30, 42), (50, 40), (70, 42), (84, 50), (94, 66)]),
  dome('front', top=10, w=46, cy=48, sb=66, shade=False),
  dome('side', top=10, w=44, cy=48, nape=82, fr=42, shade=False, side_burn=False),
  dome('back', top=10, w=46, cy=48, nape=82, shade=False))

# Peyton Pope (portero): gorra naranja con una estrella de cuatro puntas gris morada delante; cejas verdes y ojos de punto
CAP, STAR = _c('#d8742a'), _c('#8a7a9a')
def _cap(view):
    if view == 'front':
        return [L(outline([(10, 56), (10, 26), (26, 6), (50, 0), (74, 6), (90, 26), (90, 56)]), CAP),
                L(outline([(4, 58), (50, 52), (96, 58), (94, 66), (50, 62), (6, 66)]), CAP, 'f', True, True),
                L(outline([(50, 14), (56, 26), (68, 32), (56, 36), (50, 48), (44, 36), (32, 32), (44, 26)]), STAR, 'f', False, True),
                L(ell(50, 32, 3, 3), CAP, 'f', False)]
    if view == 'side':
        return [L(outline([(6, 60), (4, 30), (22, 6), (50, 0), (76, 8), (90, 30), (92, 52), (50, 58)]), CAP),
                L(outline([(70, 48), (112, 54), (110, 60), (70, 58)]), CAP, 'f', True, True)]
    return [L(outline([(8, 62), (8, 26), (26, 6), (50, 0), (74, 6), (92, 26), (92, 62), (50, 58)]), CAP),
            L(outline([(36, 54), (64, 54), (60, 62), (40, 62)]), STAR, 'f', False, True)]
C('peyton-pope', 'normal', P('#6a5a2a', '#f4c08a', brow='#7a8a3a'),
  F(eyes='dot', brows=True, mouth='smile', mouth_y=92, hairline=False, eye_y=77),
  _cap('front'), [L(outline([(52, 60), (44, 74), (56, 76), (60, 62)]))] + _cap('side'),
  dome('back', top=10, w=46, cy=48, nape=82) + _cap('back'))

# Phil Anthropic: monje de cabeza rapada (pelo verde oliva muy corto), orejas de lóbulo largo, un punto rojo en la frente,
# ojos cerrados y cara anchísima
C('phil-anthropic', 'corpulento', P('#9a9a6a', '#f2b878'),
  F(eyes='closed', brows='angry', mouth='frown', mouth_y=96, face_front=face(w=10, chin=104, jaw=8), face_side=face_side(chin=4, jaw=6), ears=False,
    hairline=[(6, 60), (16, 48), (30, 42), (50, 40), (70, 42), (84, 48), (94, 60)], nose=(50, 86, 3)),
  [L(outline([(10, 62), (2, 66), (0, 92), (8, 100), (14, 90)]), 'skin', 'b', True, True), L(outline([(90, 62), (98, 66), (100, 92), (92, 100), (86, 90)]), 'skin', 'b', True, True)] +
  dome('front', top=12, w=44, cy=48, sb=58, shade=False) + [L(ell(50, 58, 2, 2), _c('#c03a2a'), 'f', False)],
  dome('side', top=12, w=42, cy=48, nape=80, fr=42, shade=False, side_burn=False) +
  [L(outline([(40, 64), (52, 64), (54, 94), (46, 100), (40, 90)]), 'skin', 'f', True, True)],
  [L(outline([(10, 62), (2, 66), (0, 92), (8, 100), (14, 90)]), 'skin', 'b', True, True), L(outline([(90, 62), (98, 66), (100, 92), (92, 100), (86, 90)]), 'skin', 'b', True, True)] +
  dome('back', top=12, w=44, cy=48, nape=80, shade=False))

# Phil Biblist-o-biblist: tupé granate alto y plano que sube en diagonal, con una coletilla en la nuca; gafas redondas negras
C('phil-biblist-o-biblist', 'normal', P('#6a3a4a', '#f4c08a', iris='#1e1a1a'),
  F(eyes='big', brows='angry', mouth='smile', mouth_y=93, glasses=BLACK,
    hairline=[(6, 66), (18, 50), (30, 58), (36, 46), (46, 60), (52, 46), (62, 58), (70, 46), (82, 54), (94, 66)]),
  [L(outline([(12, 66), (8, 30), (4, -2, 1), (40, 0), (96, -12, 1), (94, 14), (90, 40), (88, 66), (78, 52), (22, 52)])),
   L(outline([(60, -4), (96, -12), (94, 14), (88, 60), (74, 30)]), 'shade', 'b', False),
   strand([(30, 6), (38, 30)], 'deep', 'b', 1.0), strand([(60, 0), (60, 30)], 'deep', 'b', 1.0)],
  [L(outline([(52, 62), (52, 80), (36, 84), (30, 90), (18, 86), (20, 80), (6, 64), (4, 30), (2, 0, 1), (40, -4), (94, -12, 1), (92, 14), (92, 36), (78, 42), (62, 46)])),
   L(outline([(4, 40), (24, 44), (40, 78), (22, 82), (8, 62)]), 'shade', 'b', False)],
  [L(outline([(10, 80), (6, 30), (4, -2, 1), (40, 0), (96, -12, 1), (94, 14), (90, 80), (60, 86), (56, 96), (44, 96), (40, 86)])),
   L(outline([(60, -4), (96, -12), (94, 14), (90, 78), (70, 60)]), 'shade', 'b', False)])

# Phil Dippedes: pelo gris morado peinado hacia atrás en una onda alta, con un mechón largo que le cae por un lado de la
# cara; piel tostada y cara larga
C('phil-dippedes', 'delgado', P('#8a7a9a', '#d8a26a', iris='#2a2020'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=95, face_front=face(chin=106), face_side=face_side(chin=6), nose=(50, 86, 3),
    hairline=[(6, 62), (20, 44), (40, 38), (60, 38), (78, 42), (86, 58)]),
  dome('front', top=4, w=44, cy=48, sb=60) + [L(outline([(24, 30), (40, -6, 1), (60, 0), (84, 14), (98, 4, 1), (92, 26), (80, 30)])),
  L(outline([(66, 34), (82, 40), (82, 70), (78, 92, 1), (72, 66)]), 'mid', 'f')],
  dome('side', top=4, w=44, cy=48, nape=82, fr=40) + [L(outline([(30, 20), (50, -8, 1), (76, 2), (92, 24), (76, 26)]))],
  dome('back', top=4, w=44, cy=48, nape=82) + [L(outline([(24, 30), (40, -6, 1), (60, 0), (84, 14), (98, 4, 1), (92, 26), (80, 30)]))])

# Phil Fog (portero): piel oscura, melena morada lisa hasta los hombros con la raya en medio en pico; ojos rasgados negros,
# ceño fruncido y arrugas
C('phil-fog', 'normal', P('#5a4a7a', '#8a6a50', iris='#1e1a1a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, face_front=face(chin=106, jaw=2), face_side=face_side(chin=6), nose=(50, 86, 2.6),
    hairline=[(6, 70), (18, 50), (34, 42), (50, 50), (66, 42), (82, 50), (94, 70)]),
  dome('front', top=2, w=46, cy=46, long=100, flare=2) + [strand([(50, 8), (50, 48)], 'deep', 'b', 1.2),
  L([(40, 100), (44, 102)], OUTC, 'f', False, False, 1.0), L([(60, 100), (56, 102)], OUTC, 'f', False, False, 1.0)],
  dome('side', top=2, w=46, cy=46, long=98, flare=2, fr=46),
  dome('back', top=2, w=46, cy=46, long=98, flare=2, ends=5) + [strand([(50, 8), (50, 90)], 'deep', 'b', 1.0)])

# Phil Occifer: pelo granate en pinchos revueltos que le caen por la frente; ojos rosados grandes y sonrisa
C('phil-occifer', 'normal', P('#7a3a40', '#f4c08a', iris='#c08a8a'),
  F(eyes='big', brows='angry', mouth='smile', mouth_y=93, hairline=hl(6, 66, 50, 62, jit=4, seed=41)),
  dome('front', top=-2, w=48, cy=44, n=9, amp=14, seed=42, sb=72),
  dome('side', top=-2, w=48, cy=44, n=9, amp=14, seed=42, nape=88, fr=56),
  dome('back', top=-2, w=48, cy=44, n=9, amp=14, seed=42, nape=88))

# Phil Rosey: cabeza redonda morena con un casquete de pelo negro verdoso pequeño arriba, acabado en pico, y dos mechones
# de punta junto a las orejas; ojos redondos y boca recta
C('phil-rosey', 'corpulento', P('#3a3a20', '#c08a50'),
  F(eyes='round', brows='angry', mouth='line', mouth_y=96, face_front=face(w=8, chin=102, jaw=6), ear_out=6,
    hairline=[(16, 50), (26, 34), (42, 26), (58, 26), (74, 34), (84, 50)]),
  [L(outline([(18, 50), (22, 26), (40, 14), (50, 2, 1), (60, 14), (78, 26), (82, 50), (50, 40)])),
   L(outline([(6, 76), (-6, 84, 1), (8, 86)])), L(outline([(94, 76), (106, 84, 1), (92, 86)]))],
  [L(outline([(16, 40), (30, 18), (50, 2, 1), (70, 14), (84, 30), (60, 30), (40, 40)])), L(outline([(48, 78), (36, 88, 1), (50, 86)]))],
  [L(outline([(16, 50), (20, 26), (40, 14), (50, 2, 1), (60, 14), (80, 26), (84, 50), (50, 56)])),
   L(outline([(8, 76), (-4, 84, 1), (10, 86)])), L(outline([(92, 76), (104, 84, 1), (90, 86)]))])

# Philip Flagg: pelo blanco crema con un mechón rosa, largo y revuelto, que le tapa la frente y cae por los lados; piel
# morena, cara redonda, ojos apretados y sonrisa ondulada
C('philip-flagg', 'corpulento', P('#f0e8d8', '#c88850', pinkh='#e0a8a8'),
  F(eyes='closed', brows='angry', mouth='smile', mouth_y=95, face_front=face(w=8, chin=102, jaw=6), ear_out=6,
    hairline=hl(6, 74, 56, 66, x0=10, x1=90, jit=3, seed=43)),
  dome('front', top=-2, w=54, cy=46, n=8, amp=10, sweep=0.4, seed=44, sb=80) +
  [L(outline([(30, 6), (46, 0), (44, 30), (34, 62, 1), (30, 34)]), 'pinkh', 'b', False)],
  dome('side', top=-2, w=50, cy=46, n=8, amp=10, sweep=0.4, seed=44, nape=90, fr=62),
  dome('back', top=-2, w=54, cy=46, n=8, amp=10, sweep=0.4, seed=44, nape=90))

# Philip Prince (portero): media melena verde oscuro con flequillo en puntas y un mechón tieso arriba; a cada lado le sale
# un mechón curvado hacia abajo como un gancho; ojos oliva
def _hook(x, s):
    return L(outline([(x, 46), (x - s * 20, 42), (x - s * 26, 56), (x - s * 22, 74, 1), (x - s * 18, 58), (x - s * 8, 56)]), 'mid', 'b')
C('philip-prince', 'normal', P('#2a7a50', '#f4c08a', iris='#8a8a3a'),
  F(eyes='big', brows='angry', mouth='line', mouth_y=93, hairline=hl(6, 70, 50, 64, jit=3, seed=45)),
  [_hook(14, 1), _hook(86, -1)] + dome('front', top=4, w=47, cy=46, sb=72) + [L(outline([(48, 8), (52, -8, 1), (56, 8)]))],
  dome('side', top=4, w=47, cy=46, nape=86, fr=58) + [L(outline([(14, 50), (-6, 52), (-10, 68), (-4, 82, 1), (-2, 66), (10, 62)])), L(outline([(44, 8), (50, -8, 1), (54, 8)]))],
  [_hook(14, 1), _hook(86, -1)] + dome('back', top=4, w=47, cy=46, nape=86) + [L(outline([(48, 8), (52, -8, 1), (56, 8)]))])

# Pica Vellosum: pelo verde oliva con dos moños abultados a los lados y flequillo de puntas; gafas grandes redondas naranjas
# de cristal claro, nariz larga y sonrisa de dientes
ORG = _c('#d84a2a')
def _puffs():
    return [L(ell(12, 26, 16, 14)), L(ell(88, 26, 16, 14))]
C('pica-vellosum', 'normal', P('#8a9a40', '#d8a070', iris='#2a2020'),
  F(eyes='dot', brows=False, mouth='grin', mouth_y=97, face_front=face(chin=104), face_side=face_side(chin=4, nose=3), nose=(50, 88, 3.4),
    hairline=hl(5, 66, 46, 60, jit=2, seed=46)),
  _puffs() + dome('front', top=4, w=46, cy=46, sb=66) +
  [L(ell(36, 76, 9.5, 9.5), _c('#f8e4c8'), 'f', False), L(ell(64, 76, 9.5, 9.5), _c('#f8e4c8'), 'f', False),
   L(ell(36, 76, 9.5, 9.5) + [ell(36, 76, 9.5, 9.5)[0]], ORG, 'f', False, False, 2.4), L(ell(64, 76, 9.5, 9.5) + [ell(64, 76, 9.5, 9.5)[0]], ORG, 'f', False, False, 2.4),
   L(ell(36, 76, 1.8, 2.2), OUTC, 'f', False), L(ell(64, 76, 1.8, 2.2), OUTC, 'f', False)],
  [L(ell(30, 22, 18, 16))] + dome('side', top=4, w=46, cy=46, nape=84, fr=56) +
  [L(ell(82, 76, 6, 9) + [ell(82, 76, 6, 9)[0]], ORG, 'f', False, False, 2.4), L([(76, 74), (50, 70)], ORG, 'f', False, False, 1.8)],
  _puffs() + dome('back', top=4, w=46, cy=46, nape=84))

# Pike Tucker: pelo marrón rosado con raya a un lado, peinado sobre la frente; nariz redonda, ceño fruncido
C('pike-tucker', 'normal', P('#b88078', '#e8a868', iris='#1e1a1a'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=94, nose=(50, 85, 3.4),
    hairline=[(6, 68), (18, 54), (30, 48), (50, 54), (66, 52), (78, 60), (94, 68)]),
  dome('front', top=4, w=47, cy=46, sb=68) + [strand([(36, 6), (34, 30)], 'deep', 'b', 1.2), L(outline([(16, 44), (36, 28), (62, 32), (80, 52), (82, 64, 1), (64, 50), (40, 46)]), 'mid', 'f')],
  dome('side', top=4, w=47, cy=46, nape=84, fr=54),
  dome('back', top=4, w=47, cy=46, nape=84))

# Pip Aminty: pelo amarillo peinado hacia atrás muy liso, con las rayas del peine; ojos afilados y media sonrisa
C('pip-aminty', 'normal', P('#e0b830', '#e8a868', iris='#1e1a1a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=[(6, 62), (20, 46), (34, 38), (50, 36), (66, 38), (80, 46), (94, 62)]),
  dome('front', top=4, w=45, cy=46, sb=64) + [strand([(x, 10), (x + (x - 50) * 0.3, 40)], 'deep', 'b', 1.0) for x in (34, 44, 56, 66)],
  dome('side', top=4, w=45, cy=46, nape=84, fr=38) + [strand([(80, 30), (50, 10), (20, 30)], 'deep', 'b', 1.0), strand([(84, 40), (50, 22), (14, 50)], 'deep', 'b', 1.0)],
  dome('back', top=4, w=45, cy=46, nape=84) + [strand([(x, 10), (x + (x - 50) * 0.2, 76)], 'deep', 'b', 1.0) for x in (36, 50, 64)])

# Pip Goodweather (portero): pelo verde que sube en una cresta de punta, con mechones de punta a los lados; piel morena y
# tres rayas blancas pintadas en cada mejilla
C('pip-goodweather', 'normal', P('#6a9a3a', '#b07848', iris='#1e1a1a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, face_front=face(chin=104), face_side=face_side(chin=4),
    hairline=[(6, 64), (20, 48), (34, 40), (50, 36), (66, 40), (80, 48), (94, 64)]),
  [L(outline([(12, 66), (2, 52, 1), (12, 46), (8, 30, 1), (20, 24), (30, 4), (50, -18, 1), (70, 4), (80, 24), (92, 30, 1), (88, 46), (98, 52, 1), (88, 66), (78, 52), (22, 52)])),
   L(outline([(52, -14), (70, 4), (80, 24), (90, 32), (86, 60), (72, 30)]), 'shade', 'b', False), strand([(50, -10), (50, 30)], 'deep', 'b', 1.2)] +
  [L([(x, 84), (x + 1, 89)], WHITE, 'f', False, False, 1.6) for x in (24, 28, 32, 68, 72, 76)],
  [L(outline([(52, 62), (52, 80), (40, 86), (24, 84), (10, 70), (-2, 60, 1), (8, 52), (2, 34, 1), (14, 28), (24, 6), (46, -16, 1), (70, 0), (86, 18), (94, 34), (80, 40), (62, 46)])),
   L(outline([(4, 44), (24, 50), (40, 80), (22, 82), (8, 64)]), 'shade', 'b', False)] +
  [L([(x, 84), (x + 1, 89)], WHITE, 'f', False, False, 1.6) for x in (74, 78)],
  [L(outline([(12, 80), (2, 58, 1), (12, 50), (8, 30, 1), (20, 24), (30, 4), (50, -18, 1), (70, 4), (80, 24), (92, 30, 1), (88, 50), (98, 58, 1), (88, 80), (50, 86)])),
   L(outline([(52, -14), (70, 4), (80, 24), (90, 32), (88, 78), (66, 60)]), 'shade', 'b', False)])

# Pip Skinner (portero): cabeza enorme, redonda y calva con un único rizo rubio crema encima; ojos entornados y sonrisa ancha
C('pip-skinner', 'corpulento', P('#efe2b0', '#f2b878', iris='#1e1a1a'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=96, face_front=blob([(8, 60), (14, 26), (50, 4), (86, 26), (92, 60), (86, 92), (66, 104), (50, 106), (34, 104), (14, 92)]),
    face_side=blob([(30, 10), (64, 6), (86, 30), (90, 62), (86, 92), (70, 104), (50, 102), (24, 90), (10, 62), (12, 30)]), ear_out=8, hairline=False, nose=(50, 86, 3)),
  [L(outline([(42, 30), (44, 12), (58, 8), (64, 18), (54, 20), (50, 34, 1)]), 'mid', 'f', True, True), L([(36, 96), (44, 99), (56, 99), (64, 96)], OUTC, 'f', False, False, 1.4)],
  [L(outline([(52, 24), (54, 8), (66, 6), (70, 16), (60, 18), (56, 30, 1)]), 'mid', 'f', True, True)],
  [L(blob([(10, 60), (16, 26), (50, 4), (84, 26), (90, 60), (84, 92), (50, 104), (16, 92)], 8), 'skin', 'b', True), L(outline([(44, 8), (56, 6), (58, 14), (50, 16)]), 'mid', 'f', True, True)])

# Pippin Flowers: pelo naranja revuelto en pinchos largos, cara larga con una nariz enorme; ojos redondos y sonrisa
C('pippin-flowers', 'delgado', P('#e07028', '#f4c08a', iris='#1e1a1a'),
  F(eyes='round', brows='angry', mouth='smile', mouth_y=100, face_front=face(chin=110, jaw=2), face_side=face_side(chin=10, nose=6), nose=(50, 88, 5.4),
    hairline=hl(5, 66, 48, 60, lean=2, jit=3, seed=51)),
  dome('front', top=-4, w=48, cy=44, n=8, amp=16, sweep=0.5, seed=52, sb=72),
  dome('side', top=-4, w=48, cy=44, n=8, amp=16, sweep=0.5, seed=52, nape=90, fr=54),
  dome('back', top=-4, w=48, cy=44, n=8, amp=16, sweep=0.5, seed=52, nape=90))

# Powers Flawless (portero): gorro de lana a rayas azul marino y crema, del que asoman puntas de pelo amarillo por la frente;
# piel tostada, cara larga y párpados caídos
NV, CRM = _c('#2a3a5a'), _c('#efe2c4')
def _wool(view):
    if view == 'side':
        base = [(8, 64), (4, 34), (20, 8), (48, 0), (76, 8), (92, 28), (92, 50), (60, 54), (30, 60)]
    else:
        base = [(10, 58), (10, 26), (26, 6), (50, 0), (74, 6), (90, 26), (90, 58)] if view == 'front' else [(8, 66), (8, 26), (26, 6), (50, 0), (74, 6), (92, 26), (92, 66), (50, 62)]
    out = [L(outline(base), NV)]
    for y0 in (12, 30):
        out.append(L(outline([(10, y0 + 2), (50, y0 - 4), (90, y0 + 2), (92, y0 + 10), (50, y0 + 4), (8, y0 + 10)]), CRM, 'b', False))
    out.append(L(outline([(8, 50), (50, 44), (92, 50), (92, 60), (50, 54), (8, 60)]), NV, 'b', True, True))
    return out
C('powers-flawless', 'delgado', P('#e8c030', '#c08a50', iris='#1e1a1a'),
  F(eyes='closed', brows=True, mouth='smile', mouth_y=98, face_front=face(chin=108, jaw=1), face_side=face_side(chin=8), nose=(50, 88, 3),
    hairline=False, eye_y=77),
  [L(outline([(14, 60), (20, 56), (26, 66, 1), (32, 56), (38, 66, 1), (44, 56), (50, 66, 1), (56, 56), (62, 66, 1), (68, 56), (74, 66, 1), (80, 56), (86, 60)]), 'mid', 'f')] + _wool('front'),
  [L(outline([(70, 52), (78, 62, 1), (84, 54), (90, 62, 1), (92, 52)]), 'mid', 'f')] + _wool('side'),
  _wool('back'))

# Powers Squatts (portero): pelo rojo peinado de lado que le tapa la frente en mechones de punta; cejas rojas gruesas
C('powers-squatts', 'normal', P('#b8341e', '#f4c08a', iris='#1e1a1a', brow='#b8341e'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=[(6, 70), (18, 54), (28, 62), (36, 50), (48, 60), (58, 48), (70, 58), (80, 52), (94, 70)]),
  dome('front', top=2, w=48, cy=46, n=6, amp=7, sweep=-0.6, seed=53, sb=72),
  dome('side', top=2, w=48, cy=46, n=6, amp=7, sweep=-0.6, seed=53, nape=86, fr=56),
  dome('back', top=2, w=48, cy=46, n=6, amp=7, sweep=-0.6, seed=53, nape=86))

# Pres Cripton: media melena marrón oliva lisa con flequillo recto en puntas y dos mechones largos hasta la mandíbula;
# ojos grandes redondos
C('pres-cripton', 'normal', P('#9a8048', '#f4c08a', iris='#1e1a1a'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=94, eye_sep=15, hairline=hl(5, 74, 56, 64, jit=2, seed=54)),
  dome('front', top=2, w=47, cy=46, long=96, flare=-2),
  dome('side', top=2, w=47, cy=46, long=92, flare=-2, fr=62),
  dome('back', top=2, w=47, cy=46, long=92, flare=-2, ends=4))

# Preston Gumbs: pelo azul marino liso peinado de lado sobre la frente; ojos grises y media sonrisa
C('preston-gumbs', 'normal', P('#2a4a6a', '#f6d2b0', iris='#7a7a7a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=[(6, 66), (18, 52), (32, 46), (50, 50), (70, 56), (84, 58), (94, 66)]),
  dome('front', top=4, w=47, cy=46, sb=66) + [L(outline([(16, 40), (40, 26), (70, 30), (88, 50), (86, 60, 1), (66, 50), (40, 44)]), 'mid', 'f')],
  dome('side', top=4, w=47, cy=46, nape=84, fr=52),
  dome('back', top=4, w=47, cy=46, nape=84))

# Quentin Quartz: pelo verde oscuro de puntas con un rizo en espiral sobre la frente; cejas gruesas y ojos verde claro
C('quentin-quartz', 'normal', P('#2a6a4a', '#f4c08a', iris='#9ac860'),
  F(eyes='normal', brows='angry', mouth='frown', mouth_y=94, hairline=hl(5, 66, 46, 56, jit=3, seed=55)),
  dome('front', top=0, w=48, cy=44, n=8, amp=9, seed=56, sb=70) +
  [L(outline([(48, 44), (58, 34), (68, 40), (66, 52), (58, 54), (56, 46), (62, 44)]), 'mid', 'f', True, True)],
  dome('side', top=0, w=48, cy=44, n=8, amp=9, seed=56, nape=86, fr=50),
  dome('back', top=0, w=48, cy=44, n=8, amp=9, seed=56, nape=86))

# Rab Acus: media melena verde oliva oscuro con las puntas abiertas y una cinta verde agua en la cabeza; gafas hexagonales
# de cristal claro
TEA = _c('#4a9a8a')
C('rab-acus', 'normal', P('#4a4a2a', '#f4c08a', iris='#2a2020'),
  F(eyes='dot', brows=True, mouth='smile', mouth_y=93, hairline=[(6, 66), (18, 46), (34, 38), (50, 36), (66, 38), (82, 46), (94, 66)]),
  dome('front', top=2, w=47, cy=46, n=6, amp=8, seed=61, long=88, flare=10) +
  [L(outline([(12, 44), (24, 22), (50, 14), (76, 22), (88, 44), (82, 48), (72, 30), (50, 24), (28, 30), (18, 48)]), TEA, 'f', True, True),
   L(outline([(25, 70), (47, 70), (48, 78), (44, 84), (28, 84), (24, 78)]), _c('#f6ecd0'), 'f', False),
   L(outline([(75, 70), (53, 70), (52, 78), (56, 84), (72, 84), (76, 78)]), _c('#f6ecd0'), 'f', False),
   L([(25, 70), (47, 70), (48, 78), (44, 84), (28, 84), (24, 78), (25, 70)], _c('#8a8a70'), 'f', False, False, 1.8),
   L([(75, 70), (53, 70), (52, 78), (56, 84), (72, 84), (76, 78), (75, 70)], _c('#8a8a70'), 'f', False, False, 1.8)],
  dome('side', top=2, w=47, cy=46, n=6, amp=8, seed=61, long=86, flare=10, fr=46) +
  [L(outline([(80, 30), (60, 12), (36, 10), (34, 18), (58, 22), (82, 38)]), TEA, 'f', True, True), L([(76, 72), (88, 72), (88, 82), (78, 82), (76, 72)], _c('#8a8a70'), 'f', False, False, 1.8)],
  dome('back', top=2, w=47, cy=46, n=6, amp=8, seed=61, long=86, flare=10, ends=5) +
  [L(outline([(10, 40), (50, 30), (90, 40), (90, 48), (50, 38), (10, 48)]), TEA, 'f', True, True)])

# Rainier Welkin (portero): un demonio de piel marrón oscura, sin pelo, con dos cuernos grandes curvados y orejas de punta;
# ojos pequeños blancos, nariz ancha y un colmillo
HORN = _c('#4a3a3a')
def _bighorn(s):
    return L(outline([(50 - s * 26, 34), (50 - s * 40, 24), (50 - s * 50, 4), (50 - s * 46, -16, 1), (50 - s * 54, 6), (50 - s * 46, 34), (50 - s * 32, 44)]), HORN, 'b')
C('rainier-welkin', 'corpulento', P('#4a3a3a', '#6a4a3a', iris='#f0f0f0'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=96, face_front=face(w=8, chin=104, jaw=6), face_side=face_side(chin=4, jaw=4, nose=3), hairline=False,
    ears=False, nose=(50, 85, 5)),
  [_bighorn(1), _bighorn(-1), L(outline([(14, 66), (-4, 56, 1), (10, 82)]), 'skin', 'b', True, True), L(outline([(86, 66), (104, 56, 1), (90, 82)]), 'skin', 'b', True, True),
   L(outline([(56, 96), (60, 104, 1), (62, 96)]), WHITE, 'f', True)],
  [L(outline([(40, 30), (30, 14), (36, -10, 1), (44, 12), (52, 26)]), HORN, 'b'), L(outline([(44, 64), (26, 52, 1), (40, 80)]), 'skin', 'f', True, True)],
  [_bighorn(1), _bighorn(-1), L(outline([(14, 66), (-4, 56, 1), (10, 82)]), 'skin', 'b', True, True), L(outline([(86, 66), (104, 56, 1), (90, 82)]), 'skin', 'b', True, True)])

# Ramsey Faroe (portero): tocado de faraón azul marino con franjas doradas y una joya roja en la frente; labios rosados
GOLD, GEM = _c('#d8b860'), _c('#e0606a')
def _nemes(view):
    if view == 'front':
        return [L(outline([(16, 62), (12, 30), (26, 8), (50, 2), (74, 8), (88, 30), (84, 62), (98, 92, 1), (82, 94), (80, 60), (20, 60), (18, 94), (2, 92, 1)]), NV),
                L(outline([(34, 6), (42, 4), (38, 54), (30, 56)]), GOLD, 'b', False), L(outline([(66, 6), (58, 4), (62, 54), (70, 56)]), GOLD, 'b', False),
                L(outline([(14, 52), (50, 46), (86, 52), (86, 58), (50, 52), (14, 58)]), GOLD, 'b', True, True),
                L(outline([(50, 22), (60, 32), (50, 44), (40, 32)]), GOLD, 'f', True), L(outline([(50, 26), (56, 32), (50, 40), (44, 32)]), GEM, 'f', False)]
    if view == 'side':
        return [L(outline([(4, 94, 1), (6, 40), (22, 8), (50, 2), (76, 10), (90, 30), (90, 54), (60, 60), (56, 96), (30, 100)]), NV),
                L(outline([(30, 6), (38, 4), (30, 90), (22, 92)]), GOLD, 'b', False), L(outline([(56, 56), (90, 50), (90, 56), (58, 62)]), GOLD, 'b', True, True)]
    return [L(outline([(16, 62), (8, 30), (26, 8), (50, 2), (74, 8), (92, 30), (84, 62), (98, 96, 1), (50, 102), (2, 96, 1)]), NV),
            L(outline([(34, 6), (42, 4), (40, 96), (32, 96)]), GOLD, 'b', False), L(outline([(66, 6), (58, 4), (60, 96), (68, 96)]), GOLD, 'b', False)]
C('ramsey-faroe', 'normal', P('#2a3a5a', '#e8a868', iris='#1e1a1a'),
  F(eyes='normal', brows=True, mouth='none', hairline=False, eye_y=77),
  _nemes('front') + [L(ell(50, 94, 5, 2.6), _c('#e890a0'), 'f', True)], _nemes('side'), _nemes('back'))

# Randolf Finn (portero): pelo castaño oliva peinado de lado con un mechón que cae por la sien; cara larga y ceño fruncido
C('randolf-finn', 'delgado', P('#9a8050', '#f6d0a8', iris='#1e1a1a'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=97, face_front=face(chin=106, jaw=2), face_side=face_side(chin=6),
    hairline=[(6, 60), (18, 46), (34, 42), (50, 44), (70, 40), (84, 46), (94, 60)]),
  dome('front', top=2, w=46, cy=46, sb=62) + [L(outline([(12, 40), (34, 26), (60, 26), (74, 34), (50, 40), (26, 52), (18, 66, 1)]), 'mid', 'f')],
  dome('side', top=2, w=46, cy=46, nape=82, fr=42),
  dome('back', top=2, w=46, cy=46, nape=82))

# Raven Crowe: pelo naranja greñudo en mechones de punta, con un manojo verde atado arriba; cejas gruesas gris verdoso
C('raven-crowe', 'normal', P('#e07a2a', '#f6d0a8', iris='#1e1a1a', brow='#6a8a6a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=[(6, 66), (18, 48), (32, 40), (50, 36), (68, 40), (82, 48), (94, 66)], nose=(50, 85, 2.6)),
  dome('front', top=4, w=48, cy=46, n=8, amp=12, seed=63, sb=76) + _topknot(50, -6)[:0] +
  [L(outline([(38, 8), (36, -12, 1), (46, -4), (50, -18, 1), (54, -4), (64, -12, 1), (62, 8)]), _c('#4a8a6a')), L(ell(50, 8, 7, 3.4), _c('#d8c890'))],
  dome('side', top=4, w=48, cy=46, n=8, amp=12, seed=63, nape=88, fr=42) +
  [L(outline([(34, 10), (28, -10, 1), (38, -2), (42, -16, 1), (46, -2), (54, -10, 1), (52, 10)]), _c('#4a8a6a')), L(ell(42, 10, 7, 3.4), _c('#d8c890'))],
  dome('back', top=4, w=48, cy=46, n=8, amp=12, seed=63, nape=88) +
  [L(outline([(38, 8), (36, -12, 1), (46, -4), (50, -18, 1), (54, -4), (64, -12, 1), (62, 8)]), _c('#4a8a6a')), L(ell(50, 8, 7, 3.4), _c('#d8c890'))])

# Ray Deo (portero): una mata de pinchos azul marino casi negro, grandes y en todas direcciones; sonrisa de dientes
C('ray-deo', 'normal', P('#2a2a4a', '#f4c08a', iris='#1e1a1a'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, hairline=hl(5, 66, 48, 60, jit=4, seed=64)),
  dome('front', top=-4, w=50, cy=44, n=8, amp=20, seed=65, sb=74),
  dome('side', top=-4, w=50, cy=44, n=8, amp=20, seed=65, nape=88, fr=54),
  dome('back', top=-4, w=50, cy=44, n=8, amp=20, seed=65, nape=88))

# Ray Dioset: media melena naranja con raya en medio que le llega a la barbilla; ojos azul claro redondos
C('ray-dioset', 'normal', P('#e07830', '#f6d0a8', iris='#8ac0e0'),
  F(eyes='big', brows='angry', mouth='smile', mouth_y=94, hairline=[(6, 74), (18, 52), (32, 44), (50, 42), (68, 44), (82, 52), (94, 74)]),
  dome('front', top=2, w=47, cy=46, long=96, flare=2) + [strand([(50, 4), (50, 40)], 'deep', 'b', 1.2)],
  dome('side', top=2, w=47, cy=46, long=94, flare=2, fr=46),
  dome('back', top=2, w=47, cy=46, long=94, flare=2, ends=0) + [strand([(50, 4), (50, 60)], 'deep', 'b', 1.0)])

# Ray Menn: pelo verde corto en pinchos de punta hacia arriba; piel tostada, ojos afilados y sonrisa de dientes
C('ray-menn', 'normal', P('#6a9a40', '#c08a60', iris='#1e1a1a'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=96, face_front=face(chin=104, jaw=2), face_side=face_side(chin=4),
    hairline=[(6, 62), (20, 46), (36, 40), (50, 38), (64, 40), (80, 46), (94, 62)]),
  dome('front', top=4, w=46, cy=46, n=9, amp=14, seed=66, sb=66),
  dome('side', top=4, w=46, cy=46, n=9, amp=14, seed=66, nape=84, fr=40),
  dome('back', top=4, w=46, cy=46, n=9, amp=14, seed=66, nape=84))

# Ray Whitehead: piel oscura, cara redonda, pelo crema en pinchos con una mancha castaña en medio y rayas afeitadas a los
# lados; ojos redondos y boca torcida
C('ray-whitehead', 'corpulento', P('#e8dcc0', '#9a7058', iris='#1e1a1a', patch='#b89070'),
  F(eyes='round', brows=True, mouth='frown', mouth_y=96, face_front=face(w=6, chin=102, jaw=4), ear_out=5, nose=(50, 86, 2.4),
    hairline=hl(5, 60, 46, 54, jit=3, seed=71)),
  dome('front', top=0, w=46, cy=46, n=8, amp=14, seed=72, sb=58) + [L(outline([(40, 10), (50, 2), (60, 10), (56, 30), (44, 30)]), 'patch', 'b', False),
  L([(16, 50), (14, 58)], 'patch', 'b', False, False, 1.4), L([(84, 50), (86, 58)], 'patch', 'b', False, False, 1.4)],
  dome('side', top=0, w=46, cy=46, n=8, amp=14, seed=72, nape=82, fr=44) + [L([(30, 56), (40, 52)], 'patch', 'b', False, False, 1.4), L([(28, 64), (40, 60)], 'patch', 'b', False, False, 1.4)],
  dome('back', top=0, w=46, cy=46, n=8, amp=14, seed=72, nape=82) + [L(outline([(40, 10), (50, 2), (60, 10), (56, 34), (44, 34)]), 'patch', 'b', False)])

# Rayburn Lightly: pelo rosa grisáceo en pinchos, gafas de sol redondas verdes de montura dorada, cejas de preocupación
# y cara larga
GLS = _c('#7a8a3a')
C('rayburn-lightly', 'delgado', P('#c8a0a8', '#f4c08a', iris='#1e1a1a'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=98, face_front=face(chin=106), face_side=face_side(chin=6), nose=(50, 86, 2.6),
    hairline=[(6, 62), (18, 46), (34, 40), (50, 38), (66, 40), (82, 46), (94, 62)]),
  dome('front', top=-2, w=48, cy=44, n=9, amp=14, seed=73, sb=66) +
  [L(ell(36, 76, 8, 7.5), GLS, 'f', False), L(ell(64, 76, 8, 7.5), GLS, 'f', False),
   L(ell(36, 76, 8, 7.5) + [ell(36, 76, 8, 7.5)[0]], GOLD, 'f', False, False, 1.6), L(ell(64, 76, 8, 7.5) + [ell(64, 76, 8, 7.5)[0]], GOLD, 'f', False, False, 1.6),
   L([(44, 75), (56, 75)], GOLD, 'f', False, False, 1.4), L([(28, 64), (40, 60)], OUTC, 'f', False, False, 1.8), L([(72, 64), (60, 60)], OUTC, 'f', False, False, 1.8)],
  dome('side', top=-2, w=48, cy=44, n=9, amp=14, seed=73, nape=84, fr=44) +
  [L(ell(82, 76, 5, 7), GLS, 'f', False), L([(76, 74), (50, 70)], GOLD, 'f', False, False, 1.4)],
  dome('back', top=-2, w=48, cy=44, n=9, amp=14, seed=73, nape=84))

# Reagan Boneman: pelo gris morado ondulado peinado hacia atrás, que cae en ondas largas por los lados hasta una coleta;
# cara larga, ojos redondos y ceño serio
C('reagan-boneman', 'delgado', P('#6a6a9a', '#f4c08a', iris='#1e1a1a'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=98, face_front=face(chin=108), face_side=face_side(chin=8), nose=(50, 86, 3.4),
    hairline=[(6, 66), (20, 48), (36, 40), (50, 44), (64, 40), (80, 48), (94, 66)]),
  dome('front', top=4, w=44, cy=46, sb=70) + [L(outline([(86, 50), (96, 62), (88, 74), (96, 86), (88, 96, 1), (84, 80), (88, 70), (82, 60)])),
                                           L(outline([(14, 50), (6, 62), (14, 74), (8, 84, 1), (18, 74), (12, 62)]))],
  dome('side', top=4, w=44, cy=46, nape=80, fr=42) + [L(outline([(10, 60), (2, 74), (10, 86), (4, 100, 1), (16, 88), (12, 74), (20, 64)]))],
  dome('back', top=4, w=44, cy=46, nape=80) + [L(outline([(42, 74), (58, 74), (62, 88), (54, 100, 1), (48, 90), (40, 100, 1), (38, 88)]))])

# Reese Ickle: melena verde rizada hasta los hombros con raya en medio; cara larga tostada y sonrisa tranquila
C('reese-ickle', 'delgado', P('#5a8a3a', '#d8a070', iris='#1e1a1a'),
  F(eyes='round', brows='angry', mouth='smile', mouth_y=97, face_front=face(chin=106), face_side=face_side(chin=6), nose=(50, 86, 3),
    hairline=[(6, 70), (18, 50), (34, 42), (50, 46), (66, 42), (82, 50), (94, 70)]),
  dome('front', top=2, w=48, cy=46, n=10, amp=6, soft=True, seed=74, long=92, flare=10),
  dome('side', top=2, w=48, cy=46, n=10, amp=6, soft=True, seed=74, long=90, flare=10, fr=46),
  dome('back', top=2, w=48, cy=46, n=10, amp=6, soft=True, seed=74, long=90, flare=10, ends=5))

# Reg Thrift: media melena castaño oliva lisa con raya en medio hasta la mandíbula; ojos afilados y sonrisa torcida
C('reg-thrift', 'normal', P('#8a7030', '#f4c08a', iris='#1e1a1a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, nose=(50, 86, 3.4), hairline=[(6, 72), (18, 52), (34, 44), (50, 48), (66, 44), (82, 52), (94, 72)]),
  dome('front', top=2, w=47, cy=46, long=94, flare=4) + [strand([(50, 4), (50, 44)], 'deep', 'b', 1.2)],
  dome('side', top=2, w=47, cy=46, long=92, flare=4, fr=48),
  dome('back', top=2, w=47, cy=46, long=92, flare=4, ends=0) + [strand([(50, 4), (50, 60)], 'deep', 'b', 1.0)])

# Reid Scarlet: piel morena, cara larga y cuadrada con los lados pintados de naranja como una máscara; flequillo rosa crema
# revuelto; ojos redondos, nariz grande y boca recta
ORP = _c('#d8702a')
C('reid-scarlet', 'normal', P('#f0c0a8', '#a8784a', iris='#1e1a1a'),
  F(eyes='round', brows=False, mouth='line', mouth_y=100, face_front=face(w=4, chin=110, jaw=4), face_side=face_side(chin=10), nose=(50, 86, 4.4),
    hairline=hl(5, 62, 48, 58, jit=3, seed=75)),
  dome('front', top=0, w=46, cy=44, n=7, amp=10, seed=76, sb=62) +
  [L(outline([(16, 60), (30, 58), (30, 104), (22, 96), (14, 80)]), ORP, 'f', False), L(outline([(84, 60), (70, 58), (70, 104), (78, 96), (86, 80)]), ORP, 'f', False),
   L([(30, 58), (30, 104)], OUTC, 'f', False, False, 1.2), L([(70, 58), (70, 104)], OUTC, 'f', False, False, 1.2),
   L([(36, 100), (64, 100)], OUTC, 'f', False, False, 1.6)],
  dome('side', top=0, w=46, cy=44, n=7, amp=10, seed=76, nape=82, fr=50) + [L(outline([(56, 60), (68, 60), (66, 104), (58, 100)]), ORP, 'f', False)],
  dome('back', top=0, w=46, cy=44, n=7, amp=10, seed=76, nape=82))

# Rex George (portero): media melena gris plata con mechones que le caen por la cara y una corona de laurel verde; ojos ámbar
LAU = _c('#3a7a4a')
def _laurel(cy, w):
    out = []
    for i in range(7):
        t = -1 + i / 3
        x, y = 50 + t * w, cy + abs(t) * 10
        out.append(L(ell(x, y, 6.5, 4), LAU, 'f', True))
    return out
C('rex-george', 'normal', P('#d0d0c8', '#f6d2b0', iris='#b08a30'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=94, hairline=hl(5, 76, 52, 66, lean=-2, jit=3, seed=77)),
  dome('front', top=2, w=47, cy=46, long=90, flare=0) + _laurel(28, 34),
  dome('side', top=2, w=47, cy=46, long=88, flare=0, fr=60) + [L(ell(x, y, 5, 3.2), LAU, 'f', True) for x, y in ((80, 34), (68, 26), (54, 22), (40, 22), (26, 28))],
  dome('back', top=2, w=47, cy=46, long=88, flare=0, ends=4) + _laurel(30, 38))

# Rex Plorer: pelo rosa en rizos grandes de espiral; ojos azul claro y sonrisa
C('rex-plorer', 'normal', P('#d06a70', '#f6d0a8', iris='#8ac0d0'),
  F(eyes='big', brows='angry', mouth='smile', mouth_y=94, hairline=hl(6, 66, 50, 58, jit=2, seed=78)),
  dome('front', top=-4, w=52, cy=44, n=11, amp=8, soft=True, seed=79, sb=72),
  dome('side', top=-4, w=50, cy=44, n=11, amp=8, soft=True, seed=79, nape=88, fr=54),
  dome('back', top=-4, w=52, cy=44, n=11, amp=8, soft=True, seed=79, nape=88))

# Rhys Masher: pelo rubio dorado peinado hacia atrás con las rayas del peine y un mechón más oscuro a un lado; piel
# tostada, cara redonda y media sonrisa
C('rhys-masher', 'corpulento', P('#e0b838', '#c89260', iris='#5a4a3a'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=95, face_front=face(w=4, chin=102, jaw=3), ear_out=4, nose=(50, 86, 3.4),
    hairline=[(6, 64), (18, 48), (34, 40), (50, 38), (66, 40), (82, 48), (94, 64)]),
  dome('front', top=4, w=47, cy=46, sb=64) + [strand([(x, 8), (x + (x - 50) * 0.35, 40)], 'deep', 'b', 1.0) for x in (32, 42, 50, 58, 68)] +
  [L(outline([(10, 40), (20, 20), (30, 30), (24, 60, 1), (16, 56)]), 'shade', 'b', False)],
  dome('side', top=4, w=47, cy=46, nape=84, fr=40) + [strand([(84, 36), (50, 14), (16, 34)], 'deep', 'b', 1.0), strand([(84, 44), (50, 26), (10, 52)], 'deep', 'b', 1.0)],
  dome('back', top=4, w=47, cy=46, nape=84) + [strand([(x, 10), (x + (x - 50) * 0.2, 78)], 'deep', 'b', 1.0) for x in (36, 50, 64)])

# Rich Cave (portero): gorro de aviador amarillo con orejeras naranjas y un rombo naranja dibujado delante; pecas
YLW, ORN = _c('#e0b828'), _c('#d8702a')
def _aviator(view):
    if view == 'front':
        return [L(outline([(8, 60), (8, 24), (24, 6), (50, 0), (76, 6), (92, 24), (92, 60), (50, 56)]), YLW),
                L(outline([(4, 54), (16, 52), (24, 60), (22, 90), (14, 96), (2, 88)]), ORN, 'f', True, True),
                L(outline([(96, 54), (84, 52), (76, 60), (78, 90), (86, 96), (98, 88)]), ORN, 'f', True, True),
                L(outline([(14, 54), (50, 48), (86, 54), (84, 62), (50, 56), (16, 62)]), ORN, 'f', True, True),
                L(outline([(50, 10), (64, 26), (50, 42), (36, 26)]), ORN, 'f', False, True), L(outline([(50, 18), (56, 26), (50, 34), (44, 26)]), YLW, 'f', False, True),
                L(outline([(26, 30), (34, 34), (32, 40), (24, 38)]), ORN, 'f', False), L(outline([(74, 30), (66, 34), (68, 40), (76, 38)]), ORN, 'f', False)]
    if view == 'side':
        return [L(outline([(6, 70), (4, 30), (22, 6), (50, 0), (76, 8), (92, 28), (92, 54), (60, 58), (36, 60)]), YLW),
                L(outline([(34, 56), (58, 56), (60, 92), (50, 98), (36, 92)]), ORN, 'f', True, True),
                L(outline([(36, 56), (92, 48), (92, 56), (60, 62), (36, 64)]), ORN, 'f', True, True)]
    return [L(outline([(6, 76), (6, 24), (24, 6), (50, 0), (76, 6), (94, 24), (94, 76), (50, 82)]), YLW),
            L(outline([(2, 58), (14, 56), (18, 92), (8, 96), (0, 86)]), ORN, 'f', True, True), L(outline([(98, 58), (86, 56), (82, 92), (92, 96), (100, 86)]), ORN, 'f', True, True)]
C('rich-cave', 'normal', P('#6a5a2a', '#f6d0a8', iris='#1e1a1a', brow='#9a8a50'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=94, hairline=False, eye_y=77, ears=False),
  _aviator('front') + [L(ell(x, y, 0.9, 0.9), _c('#b8704a'), 'f', False) for x, y in ((24, 86), (28, 89), (31, 85), (76, 86), (72, 89), (69, 85))],
  _aviator('side'), _aviator('back'))

# Rich Eden (portero): pelo verde oliva oscuro con flequillo en puntas, las puntas abiertas por los lados y dos pelillos
# tiesos arriba; ojos grises entornados y media sonrisa
C('rich-eden', 'normal', P('#4a5a2a', '#f6d0a8', iris='#8a8a8a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=hl(5, 72, 50, 62, jit=3, seed=81)),
  dome('front', top=4, w=46, cy=46, n=6, amp=8, seed=82, long=86, flare=14) + [L([(48, 6), (44, -6), (40, -8)], 'mid', 'b', False, False, 2.2),
                                                                            L([(52, 6), (56, -6), (62, -8)], 'mid', 'b', False, False, 2.2)],
  dome('side', top=4, w=46, cy=46, n=6, amp=8, seed=82, long=84, flare=12, fr=56) + [L([(50, 6), (48, -6), (42, -8)], 'mid', 'b', False, False, 2.2)],
  dome('back', top=4, w=46, cy=46, n=6, amp=8, seed=82, long=84, flare=12, ends=5) + [L([(48, 6), (44, -6), (40, -8)], 'mid', 'b', False, False, 2.2)])
