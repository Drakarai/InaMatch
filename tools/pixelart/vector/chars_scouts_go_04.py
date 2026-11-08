"""Ojeadores de GO (scouts-go), tanda 04: dibujados a partir de su retrato de Victory Road; claves 'scouts-go:<id>'.

Ninguno tiene modelo 3D propio (el de Gazza Irons es el suyo y cuadra): frente desde el retrato y perfil y espalda deducidos.
Usa las ayudas de las tandas de IE (dome/hl/face de ie1_09, round_specs/goggles/shades de ie1_03, ring/hood/bowl3 de
ie3_02...)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401
from chars_scouts_ie1_09 import dome, hl, face, face_side, F, P, mark, _c  # noqa: F401
from chars_scouts_ie1_03 import round_specs, goggles, shades, thick_brows, side_brow, blush, stache, freckles, skull  # noqa: F401
from chars_scouts_ie3_02 import ring, hood, bowl3, scarf, skull3  # noqa: F401,E402

WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)


def C(pid, body, palette, f, front, side, back):
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        # el nacimiento del pelo baja por el borde de la cara: así su raya no cruza el pelo de los lados
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[f'scouts-go:{pid}'] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def M(pts, c='mid', z='b', sil=True, ln=False):
    return L(outline(pts), c, z, sil, ln)


def mx(pts):
    """Refleja puntos de frente (x -> 100 - x), con las puntas (x, y, 1)."""
    return [(100 - p[0],) + tuple(p[1:]) for p in pts]


def grid(x0, y0, x1, y1, n=4, c=OUTC, w=0.9):
    """Rejilla fina (parches, máscaras de malla)."""
    out = []
    for i in range(1, n):
        x = x0 + (x1 - x0) * i / n
        y = y0 + (y1 - y0) * i / n
        out += [L([(x, y0), (x, y1)], c, 'f', False, False, w), L([(x0, y), (x1, y)], c, 'f', False, False, w)]
    return out


def eye_mask(c=BLACK, ey=75, sep=14):
    """Antifaz pintado: aros gruesos alrededor de los ojos, el puente y las alas hacia las sienes (los ojos quedan encima)."""
    out = []
    for cx in (50 - sep, 50 + sep):
        e = ell(cx, ey, 9.5, 7)
        out.append(L(e + [e[0]], c, 'f', False, False, 3.2))
    out += [L([(44, ey - 2), (56, ey - 2)], c, 'f', False, False, 4.5), L([(14, ey - 6), (27, ey - 1)], c, 'f', False, False, 4.5),
            L([(86, ey - 6), (73, ey - 1)], c, 'f', False, False, 4.5)]
    return out


# ------------------------------------------------------------------ jugadores

# Francis Shoe: cabezón de cara ancha y pálida; una cresta gris corta con piquitos encima y un pico en la frente, los lados
# casi pelados; orejas grandes, cejas grises gruesas de enfado, ojos pequeños azulados y boca torcida hacia abajo
C('francis-shoe', 'corpulento', P('#9c978d', '#fbe8cc', iris='#5a6e8a'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=95, face_front=face(w=6, chin=104, jaw=3), big_ears=3, ear_out=5, nose=(50, 86, 3),
    hairline=[(10, 60), (22, 50), (36, 48), (50, 56), (64, 48), (78, 50), (90, 60)]),
  [M([(24, 58), (22, 38), (30, 20), (40, 10), (45, 4, 1), (51, 10), (57, 3, 1), (62, 12), (70, 20), (78, 38), (76, 58), (66, 50), (34, 50)]),
   M([(56, 4), (68, 16), (76, 36), (74, 54), (64, 30)], 'shade', 'b', False)] + thick_brows(63, 'shade', 4.2, 15, 1.4, 13),
  [M([(32, 46), (34, 22), (48, 8), (54, -2, 1), (62, 6), (76, 14), (86, 30), (80, 46), (60, 40)]), M([(36, 40), (50, 14), (70, 16), (60, 38)], 'shade', 'b', False)] +
  side_brow(63, 'shade', 4.2, 1.4),
  [M([(22, 50), (24, 26), (36, 12), (45, 2, 1), (53, 8), (60, 0, 1), (68, 12), (78, 26), (80, 50), (64, 42), (36, 42)]),
   M([(58, 6), (76, 22), (80, 46), (66, 40)], 'shade', 'b', False)])

# Frank Reddy Redmond: pelo castaño rojizo despeinado en mechones de punta, flequillo hasta las cejas y los lados que le
# tapan media oreja; ojos negros grandes y sonrisa
C('frank-reddy-redmond', 'normal', P('#7a3436', '#f6ba7c', iris='#1e1414'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=92, hairline=hl(6, 70, 50, 62, jit=2, seed=4)),
  dome('front', top=2, w=48, cy=46, n=7, amp=7, sweep=-0.3, sb=82, seed=5),
  dome('side', top=2, w=48, cy=46, n=7, amp=7, sweep=-0.3, nape=90, fr=56, seed=5),
  dome('back', top=2, w=48, cy=46, n=7, amp=7, sweep=-0.3, nape=92, seed=5))

# Frankie Boulder: un Frankenstein de piel verde agua con una franja gris que le baja por media cara, pelo azul marino plano
# encima, dos tornillos en las sienes, ojos entornados y boca recta con los dientes asomando
GREY, BOLT = _c('#7a7878'), _c('#5a5658')
def _bolts(view):
    if view == 'front':
        return [M([(2, 40), (12, 40), (12, 54), (2, 54)], BOLT), M([(-4, 36), (2, 36), (2, 58), (-4, 58)], BOLT),
                M([(88, 40), (98, 40), (98, 54), (88, 54)], BOLT), M([(98, 36), (104, 36), (104, 58), (98, 58)], BOLT)]
    if view == 'side':
        return [L(ell(46, 48, 7, 7), BOLT, 'f'), L(ell(46, 48, 3, 3), GREY, 'f', False)]
    return [M([(2, 44), (12, 44), (12, 58), (2, 58)], BOLT), M([(88, 44), (98, 44), (98, 58), (88, 58)], BOLT)]
C('frankie-boulder', 'normal', P('#33465a', '#8ab8a8', iris='#5a6a6a'),
  F(eyes='sharp', brows='angry', mouth='buck', mouth_y=94, face_front=face(chin=106), face_side=face_side(chin=5),
    hairline=[(10, 56), (18, 42), (50, 38), (82, 42), (90, 56)]),
  _bolts('front') + [M([(16, 50), (16, 24), (30, 10), (50, 6), (70, 10), (84, 24), (84, 50), (70, 40), (30, 40)]),
                     mark([(43, 40), (57, 40), (55, 66), (60, 102), (40, 102), (45, 66)], GREY),
                     L([(28, 92), (34, 96)], OUTC, 'f', False, False, 1.0), L([(66, 92), (72, 88)], OUTC, 'f', False, False, 1.0)],
  [M([(36, 44), (40, 18), (56, 6), (78, 10), (88, 26), (86, 40), (60, 36)]), mark([(80, 50), (88, 50), (88, 104), (78, 104)], GREY)] + _bolts('side'),
  [M([(14, 54), (14, 26), (30, 10), (50, 6), (70, 10), (86, 26), (86, 54), (50, 46)])] + _bolts('back'))

# Fred Manners Sidemanners (portero): tupé naranja rojizo que se levanta en una ola hacia su izquierda, una cinta gris con el
# espejo redondo de médico en la frente; cara cuadrada, cejas gruesas y sonrisa de dientes
SIL = _c('#dfe6e6')
C('fred-manners-sidemanners', 'normal', P('#b2400a', '#f8bb7c', iris='#2a1a12'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, face_front=face(w=3, jaw=3, chin=102),
    hairline=[(10, 62), (16, 52), (50, 50), (84, 52), (90, 62)]),
  [M([(14, 60), (10, 36), (18, 16), (34, 4), (54, 0), (72, -8), (92, -12, 1), (84, 4), (98, 12, 1), (88, 24), (92, 44), (86, 60), (70, 50), (30, 50)]),
   M([(60, 0), (84, 2), (90, 26), (88, 50), (76, 30)], 'shade', 'b', False),
   M([(12, 52), (88, 52), (88, 59), (12, 59)], _c('#8a8686'), 'f'),
   L(ell(55, 50, 12, 12), SIL, 'f', True, True), L(ell(55, 50, 3, 3), _c('#9aa0a0'), 'f', False)],
  [M([(60, 50), (66, 36), (82, 30), (98, 20), (100, 6, 1), (84, 6), (90, -10, 1), (66, 0), (40, 0), (16, 10), (4, 34), (10, 60), (28, 74), (44, 70), (52, 58)]),
   M([(52, 52), (90, 46), (90, 53), (52, 59)], _c('#8a8686'), 'f'), L(ell(88, 48, 4, 10), SIL, 'f', True, True)],
  [M([(12, 64), (10, 36), (18, 16), (34, 4), (54, 0), (74, -6), (94, -10, 1), (86, 6), (96, 16, 1), (88, 28), (90, 64), (50, 70)]),
   M([(10, 54), (90, 54), (90, 61), (10, 61)], _c('#8a8686'), 'f')])

# Fred Wheels Wheeler: cara larga; tupé verde azulado en cuña altísima inclinada hacia su izquierda, con un mechón blanco en
# rayo que le cae por la cara; gafas de visera naranja y media sonrisa
TEALW, ORV = _c('#f2f2ee'), _c('#e8902a')
C('fred-wheels-wheeler', 'delgado', P('#22797c', '#f8cca0', iris='#2a2a2a'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=96, face_front=face(chin=108, jaw=-1), face_side=face_side(chin=7),
    hairline=hl(7, 62, 46, 56, jit=2, seed=9)),
  [M([(14, 64), (12, 40), (20, 22), (40, 8), (70, -6), (100, -20, 1), (84, 2), (88, 22), (86, 64), (76, 48), (24, 48)]),
   M([(60, -2), (90, -12), (84, 6), (86, 40), (76, 22)], 'shade', 'b', False),
   M([(42, 22), (56, 12), (50, 40), (58, 38), (44, 100, 1), (42, 56), (34, 60)], TEALW, 'f'),
   M([(18, 68), (82, 68), (78, 80), (58, 82), (50, 76), (42, 82), (22, 80)], ORV, 'f')],
  [M([(56, 52), (62, 40), (80, 36), (92, 24), (100, -8, 1), (76, -2), (56, -12, 1), (30, 2), (10, 16), (4, 40), (10, 62), (28, 76), (44, 72), (52, 60)]),
   M([(66, 68), (90, 66), (90, 78), (70, 80)], ORV, 'f'), M([(84, 30), (92, 26), (92, 60), (88, 90, 1), (84, 56)], TEALW, 'f')],
  [M([(12, 66), (10, 40), (18, 22), (40, 8), (70, -4), (98, -16, 1), (84, 4), (90, 24), (90, 66), (50, 74)]),
   M([(60, 0), (90, -8), (86, 10), (88, 60), (70, 40)], 'shade', 'b', False)])

# Freddie Aster Stayre: sombrero de fieltro blanco rosado de ala ancha; debajo, pelo negro con un mechón grande que le tapa
# el ojo derecho; piel morena y un ojo azul grisáceo
HAT, HATD = _c('#e4e2e4'), _c('#c8a8b0')
def _fedora(view):
    if view == 'front':
        return [M([(24, 38), (26, 8), (50, 0), (74, 8), (76, 38)], HAT, 'f'), M([(26, 30), (74, 30), (75, 38), (25, 38)], HATD, 'f', False),
                L(ell(50, 40, 48, 9), HAT, 'f', True, True), L(blob([(10, 42), (50, 46), (90, 42), (92, 46), (50, 50), (8, 46)], 4), HATD, 'f', False)]
    if view == 'side':
        return [M([(20, 36), (24, 6), (50, -2), (76, 6), (80, 36)], HAT, 'f'), M([(22, 28), (78, 28), (79, 36), (21, 36)], HATD, 'f', False),
                L(ell(52, 38, 50, 7), HAT, 'f', True, True)]
    return [M([(24, 40), (26, 10), (50, 2), (74, 10), (76, 40)], HAT, 'f'), M([(26, 32), (74, 32), (75, 40), (25, 40)], HATD, 'f', False),
            L(ell(50, 42, 48, 9), HAT, 'f', True, True)]
C('freddie-aster-stayre', 'normal', P('#14181a', '#b88c78', iris='#6a8a96'),
  F(eyes='normal', brows=True, mouth='line', mouth_y=93, hairline=[(10, 64), (16, 50), (50, 46), (84, 50), (90, 64)]),
  [M([(12, 72), (10, 50), (18, 40), (82, 40), (90, 50), (88, 68), (78, 56), (22, 56)]),
   M([(16, 46), (52, 42), (58, 54), (50, 64), (44, 86, 1), (36, 68), (22, 78, 1), (18, 62)], 'mid', 'f')] + _fedora('front'),
  [M([(56, 54), (62, 44), (84, 44), (88, 58), (80, 60), (66, 58), (60, 70), (40, 74), (16, 72), (8, 50), (20, 40)])] + _fedora('side'),
  [M([(12, 72), (10, 48), (90, 48), (88, 72), (50, 80)])] + _fedora('back'))

# Freyer Monk: pelo negro en dos alas de pinchos enormes que salen hacia arriba y a los lados, con pico en la frente y
# entradas; piel tostada, ceño muy fruncido, dientes apretados y una cicatriz en la mejilla
C('freyer-monk', 'corpulento', P('#302c2c', '#cc976e', iris='#1e1414'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=95, face_front=face(w=4, jaw=4, chin=104),
    hairline=[(10, 64), (16, 50), (28, 58), (36, 48), (50, 62), (64, 48), (72, 58), (84, 50), (90, 64)]),
  [M([(12, 62), (8, 38), (-8, -8, 1), (20, 8), (40, 14), (50, 22), (60, 14), (80, 8), (108, -8, 1), (92, 38), (88, 62), (76, 46), (24, 46)]),
   M([(60, 14), (84, 10), (100, -2), (90, 36), (86, 58), (76, 32)], 'shade', 'b', False),
   L([(62, 90), (72, 100)], _c('#8a5a3a'), 'f', False, False, 1.4)],
  [M([(56, 56), (64, 44), (84, 42), (96, 30), (88, 18), (70, 12), (40, 4), (-2, -14, 1), (8, 20), (4, 46), (12, 66), (30, 78), (46, 70)])],
  [M([(12, 70), (8, 38), (-8, -6, 1), (20, 10), (50, 18), (80, 10), (108, -6, 1), (92, 38), (88, 70), (50, 78)]),
   M([(56, 16), (82, 12), (100, 0), (90, 36), (86, 66), (64, 50)], 'shade', 'b', False)])

# Fritzy Flaps: gorro de aviador granate con rayas grises y orejeras largas, calado hasta la nariz (no se le ven los ojos);
# perilla fina y boca torcida hacia abajo
MAR, STR = _c('#8b3446'), _c('#56494a')
def _flaps(view):
    if view == 'front':
        out = [M([(10, 98), (8, 60), (10, 30), (24, 8), (50, 0), (76, 8), (90, 30), (92, 60), (90, 98), (80, 100), (78, 74), (50, 76), (22, 74), (20, 100)], MAR, 'f'),
               M([(60, 4), (84, 18), (92, 50), (90, 96), (80, 98), (80, 70)], 'shade', 'f', False)]
        for y in (18, 34, 50):
            out.append(L(quad((12 if y > 20 else 22, y + 2), (50, y - 4), (88 if y > 20 else 78, y + 2)), STR, 'f', False, False, 4))
        return out
    if view == 'side':
        out = [M([(60, 76), (84, 74), (92, 54), (88, 26), (66, 6), (36, 2), (12, 16), (2, 44), (6, 76), (30, 82), (36, 102), (52, 104), (54, 80)], MAR)]
        for y in (18, 34, 50):
            out.append(L(quad((6, y + 6), (46, y - 4), (90, y + 2)), STR, 'b', False, False, 4))
        return out
    out = [M([(8, 96), (8, 60), (10, 30), (24, 8), (50, 0), (76, 8), (90, 30), (92, 60), (92, 96), (80, 98), (70, 84), (30, 84), (20, 98)], MAR)]
    for y in (18, 34, 50, 66):
        out.append(L(quad((10, y + 2), (50, y - 4), (90, y + 2)), STR, 'b', False, False, 4))
    return out
C('fritzy-flaps', 'normal', P('#4a3434', '#f0ecdc'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=92, hairline=False),
  _flaps('front') + [mark([(46, 99), (54, 99), (52, 104), (48, 104)], _c('#3a2828'))],
  _flaps('side'), _flaps('back'))

# Frosty Patissier: pelo lila rosado alborotado con dos picos como orejas de gato arriba, flequillo de mechones; cejas lilas
# finas, ojos verdes de gato y sonrisa
C('frosty-patissier', 'normal', P('#d4a0bc', '#fad8b6', iris='#3a9a44', brow='#b07a96'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=92, hairline=hl(6, 66, 48, 60, jit=2, seed=12)),
  dome('front', top=6, w=48, cy=46, n=8, amp=6, sweep=0.2, sb=70, seed=13) +
  [M([(16, 24), (4, -6, 1), (30, 10)]), M([(84, 24), (96, -6, 1), (70, 10)]),
   L([(24, 63), (42, 66)], 'brow', 'f', False, False, 2.0), L([(76, 63), (58, 66)], 'brow', 'f', False, False, 2.0)],
  dome('side', top=6, w=48, cy=46, n=8, amp=6, sweep=0.2, nape=88, fr=52, seed=13) + [M([(52, 12), (60, -8, 1), (70, 12)])],
  dome('back', top=6, w=48, cy=46, n=8, amp=6, sweep=0.2, nape=88, seed=13) + [M([(16, 24), (4, -6, 1), (30, 10)]), M([(84, 24), (96, -6, 1), (70, 10)])])

# Gabe Roundy Roundhouse (portero): pelo rojo en pinchos encima de un pañuelo verde grisáceo calado hasta las cejas, dos
# mechones rojos que le caen por los lados de la cara; ojos amarillos y rayas rojas bajo los ojos
BAND = _c('#5a8482')
C('gabe-roundy-roundhouse', 'normal', P('#cc463e', '#e6b88a', iris='#e0a020'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=93, hairline=[(10, 66), (16, 60), (50, 60), (84, 60), (90, 66)]),
  [M([(14, 50), (8, 30), (-6, 14, 1), (14, 12), (12, -8, 1), (30, 6), (40, -14, 1), (52, 2), (66, -10, 1), (70, 6), (90, -2, 1), (86, 18), (100, 26, 1), (88, 34), (86, 50)]),
   M([(10, 64), (12, 42), (50, 36), (88, 42), (90, 64), (50, 60)], BAND, 'f'),
   M([(56, 36), (66, 34), (70, 50), (62, 56)], 'mid', 'f'),
   M([(12, 58), (22, 58), (26, 92, 1), (14, 80)], 'mid', 'f'), M([(88, 58), (78, 58), (74, 92, 1), (86, 80)], 'mid', 'f'),
   L([(24, 84), (32, 86)], _c('#c83a2a'), 'f', False, False, 1.6), L([(76, 84), (68, 86)], _c('#c83a2a'), 'f', False, False, 1.6)],
  [M([(50, 40), (40, 10), (60, -12, 1), (62, 6), (84, -4, 1), (82, 14), (98, 20, 1), (88, 36), (60, 46)]),
   M([(4, 44), (10, 26), (30, 12), (54, 8), (80, 14), (92, 30), (92, 56), (52, 58), (20, 66), (6, 60)], BAND),
   M([(56, 56), (66, 56), (66, 90, 1), (58, 74)], 'mid', 'f')],
  [M([(14, 56), (8, 30), (-6, 14, 1), (14, 12), (12, -8, 1), (30, 6), (40, -14, 1), (52, 2), (66, -10, 1), (70, 6), (90, -2, 1), (86, 18), (100, 26, 1), (88, 34), (86, 56)]),
   M([(8, 66), (10, 42), (50, 36), (90, 42), (92, 66), (50, 70)], BAND), M([(44, 66), (56, 66), (62, 90, 1), (50, 80), (40, 92, 1)], BAND)])

# Gale Mistral: pelo azul celeste con dos mechones enormes que se curvan hacia arriba en arco, como cuernos, y mechones a
# los lados de la cara; ojos rosas con ojeras y sonrisa
C('gale-mistral', 'chica', P('#68aad0', '#fcf0d6', iris='#c0507a', shade='#4a7aa0'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=92, hairline=[(10, 64), (18, 46), (34, 40), (50, 46), (66, 40), (82, 46), (90, 64)]),
  [M([(12, 84), (10, 50), (20, 26), (50, 16), (80, 26), (90, 50), (88, 84), (80, 66), (20, 66)]),
   M([(44, 22), (32, -2), (16, -18), (0, -10, 1), (10, -2), (22, 6), (34, 16), (52, 26)], 'mid', 'f'),
   M([(52, 24), (64, 0), (82, -14), (100, -4, 1), (90, 2), (78, 8), (68, 16), (60, 28)], 'mid', 'f'),
   M([(12, 60), (22, 56), (26, 94, 1), (12, 82)], 'mid', 'f'), M([(88, 60), (78, 56), (74, 94, 1), (88, 82)], 'mid', 'f'),
   L([(28, 80), (30, 84)], _c('#a86078'), 'f', False, False, 1.2), L([(72, 80), (70, 84)], _c('#a86078'), 'f', False, False, 1.2)],
  [M([(54, 52), (62, 40), (82, 34), (86, 22), (64, 12), (36, 12), (14, 24), (6, 50), (8, 84), (24, 92), (40, 84), (50, 66)]),
   M([(50, 16), (52, -8), (40, -18), (28, -10, 1), (40, -8), (44, 4), (56, 20)], 'mid', 'f'),
   M([(56, 54), (64, 56), (64, 90, 1), (58, 76)], 'mid', 'f')],
  [M([(10, 88), (8, 50), (18, 24), (50, 14), (82, 24), (92, 50), (90, 88), (70, 96), (50, 92), (30, 96)]),
   M([(44, 20), (30, -4), (14, -18), (2, -8, 1), (20, -10), (32, 2), (50, 24)]), M([(56, 20), (70, -4), (86, -18), (98, -8, 1), (80, -10), (68, 2), (50, 24)])])

# Gale Sweep: melena larga gris azulada barrida por el viento hacia su derecha en mechones largos, que le tapan un ojo; ojo
# morado y boca de disgusto
C('gale-sweep', 'normal', P('#9cbecc', '#fcecc6', iris='#4a3a6a', shade='#7a7c84', deep='#5e585e'),
  F(eyes='normal', brows=True, mouth='frown', mouth_y=93, hairline=[(10, 66), (20, 46), (40, 40), (60, 40), (80, 46), (90, 66)]),
  [M([(90, 70), (92, 40), (80, 12), (56, 2), (30, 6), (4, 18), (-26, 38, 1), (-4, 40), (-24, 60, 1), (2, 58), (-14, 80, 1), (10, 72), (2, 96, 1), (22, 82), (34, 72), (60, 50)]),
   M([(-20, 40), (6, 26), (40, 18), (20, 36)], 'light', 'b', False),
   M([(12, 44), (64, 32), (60, 50), (54, 70), (46, 100, 1), (30, 84), (12, 94, 1), (12, 62)], 'mid', 'f'),
   M([(84, 50), (92, 54), (90, 82, 1), (84, 70)], 'mid', 'f')],
  [M([(56, 54), (64, 42), (84, 38), (90, 22), (70, 6), (40, 4), (14, 14), (-10, 30, 1), (4, 40), (-16, 58, 1), (6, 62), (-10, 84, 1), (14, 80), (6, 102, 1), (28, 90), (44, 76),
      (52, 64)])],
  [M([(8, 70), (8, 40), (20, 14), (50, 4), (80, 12), (104, 24, 1), (94, 40), (110, 56, 1), (94, 62), (106, 82, 1), (88, 82), (94, 100, 1), (74, 90), (50, 86), (20, 80)])])

# Garreth Garnet Nett: pelo granate oscuro con un tupé naranja enrollado encima, flequillo en punta que baja entre los ojos y
# los lados hasta la mandíbula; ojos naranjas de enfado
ORR = _c('#c04626')
C('garreth-garnet-nett', 'normal', P('#8a0a10', '#f8d2aa', iris='#e06020', shade='#5c1012'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93,
    hairline=[(10, 90), (16, 56), (28, 50), (38, 62), (46, 52), (50, 72), (54, 52), (62, 62), (72, 50), (84, 56), (90, 90)]),
  dome('front', top=8, w=48, cy=48, n=8, amp=5, sb=94, seed=21) + [M([(28, 8), (48, -6), (72, -4), (74, 6), (52, 12), (30, 14)], ORR, 'f')],
  dome('side', top=8, w=48, cy=48, n=8, amp=5, nape=92, fr=58, seed=21) + [M([(30, 6), (50, -6), (74, 0), (72, 8), (50, 10)], ORR, 'f')],
  dome('back', top=8, w=48, cy=48, n=8, amp=5, nape=94, seed=21) + [M([(28, 8), (48, -4), (72, -2), (72, 8), (50, 12), (30, 14)], ORR, 'f')])

# Gazza Irons (portero): gorro de lana gris con una franja oscura, flequillo negro en dientes de sierra, un parche de
# rejilla en el ojo izquierdo y una mascarilla de rejilla en la boca sujeta con correas
CAP, CAPD, MESH = _c('#8a8786'), _c('#54504e'), _c('#e8e4e0')
def _beanie(view):
    if view == 'front':
        return [M([(12, 52), (12, 26), (26, 8), (50, 2), (74, 8), (88, 26), (88, 52)], CAP, 'f'), M([(12, 40), (88, 40), (88, 48), (12, 48)], CAPD, 'f', False),
                M([(14, 52), (20, 62, 1), (26, 52), (32, 62, 1), (38, 52), (44, 62, 1), (50, 52), (56, 62, 1), (62, 52), (68, 62, 1), (74, 52), (80, 62, 1), (86, 52)], BLACK, 'f')]
    if view == 'side':
        return [M([(6, 58), (4, 30), (20, 8), (50, 0), (76, 8), (90, 28), (90, 52), (60, 54)], CAP, 'f'), M([(5, 46), (60, 42), (90, 40), (90, 48), (60, 50), (5, 54)], CAPD, 'f', False),
                M([(60, 52), (66, 60, 1), (72, 52), (78, 60, 1), (86, 52)], BLACK, 'f')]
    return [M([(10, 64), (10, 28), (26, 8), (50, 2), (74, 8), (90, 28), (90, 64), (50, 66)], CAP, 'f'), M([(10, 46), (90, 46), (90, 54), (10, 54)], CAPD, 'f', False)]
C('gazza-irons', 'normal', P('#1e1a1a', '#fcefd4', iris='#1e1414'),
  F(eyes='round', brows=False, mouth='none', hairline=False, eye_sep=15),
  _beanie('front') + [M([(54, 66), (74, 64), (76, 84), (56, 86)], MESH, 'f')] + grid(54, 66, 75, 85, 4) +
  [M([(28, 86), (72, 86), (70, 100), (30, 100)], MESH, 'f')] + grid(28, 86, 72, 100, 6) +
  [L([(16, 82), (28, 90)], CAPD, 'f', False, False, 1.4), L([(84, 82), (72, 90)], CAPD, 'f', False, False, 1.4), L([(30, 60), (60, 92)], CAPD, 'f', False, False, 1.2)],
  _beanie('side') + [M([(70, 86), (90, 86), (90, 100), (74, 100)], MESH, 'f'), L([(46, 76), (72, 90)], CAPD, 'f', False, False, 1.4)],
  _beanie('back') + [L(quad((14, 84), (50, 92), (86, 84)), CAPD, 'f', False, False, 1.4)])

# Gee Geek Kasoid: rizos castaño granate en nube, gafas de cristal rosa con montura marrón y cinta azul por encima de los ojos
# caídos; nariz roja grande y labios gruesos
C('gee-geek-kasoid', 'normal', P('#642c2c', '#f0ccba', iris='#2a1a1a', nose='#d47868'),
  F(eyes='dot', brows=False, mouth='lips', mouth_w=8, mouth_y=96, eye_y=80, nose=(50, 88, 6), hairline=hl(7, 64, 46, 54, jit=3, seed=7)),
  dome('front', top=2, w=52, cy=44, n=13, amp=6, soft=True, sb=66, seed=31) +
  goggles('front', y=66, frame=_c('#9a6a4a'), lens=_c('#f0a8b8')) + [L([(46, 63), (54, 63)], _c('#3a5ab0'), 'f', False, False, 3)],
  dome('side', top=2, w=50, cy=44, n=13, amp=6, soft=True, nape=86, fr=50, seed=31) + goggles('side', y=66, frame=_c('#9a6a4a'), lens=_c('#f0a8b8')),
  dome('back', top=2, w=52, cy=44, n=13, amp=6, soft=True, nape=88, seed=31) + goggles('back', y=66, frame=_c('#9a6a4a')))

# Gen Tallgiant: grandullón moreno con un afro negro enorme y patillas que le bajan hasta la mandíbula; gafas redondas de
# montura blanca y labios gruesos naranjas
C('gen-tallgiant', 'corpulento', P('#28292d', '#ba8650', iris='#1e1414'),
  F(eyes='dot', brows=False, mouth='lips', mouth_w=9, mouth_y=95, face_front=face(w=5, chin=104, jaw=2), hairline=[(10, 66), (18, 54), (50, 50), (82, 54), (90, 66)],
    glasses=_c('#f0e8d0')),
  dome('front', top=-6, w=54, cy=44, n=0, sb=98, seed=1) + [M([(10, 60), (20, 58), (24, 98, 1), (12, 90)], 'mid', 'f'), M([(90, 60), (80, 58), (76, 98, 1), (88, 90)], 'mid', 'f')],
  dome('side', top=-6, w=52, cy=44, n=0, nape=92, fr=56, seed=1) + [M([(56, 58), (66, 58), (68, 96, 1), (58, 86)], 'mid', 'f')],
  dome('back', top=-6, w=54, cy=44, n=0, nape=94, seed=1))

# Gen Tillmann: gorra de béisbol azul y crema con un rayo amarillo y la visera morada hacia su derecha; asoman dos rollos de
# pelo granate rizado a los lados; piel morena, ojos cansados con ojeras y boca de preocupación
CBL, CCR, CPU, YEL = _c('#2c74b2'), _c('#efe6c8'), _c('#4a4f8a'), _c('#f0c834')
def _cap(view):
    if view == 'front':
        return [M([(16, 48), (18, 22), (34, 8), (56, 4), (78, 12), (88, 32), (86, 48)], CBL, 'f'),
                M([(60, 4), (78, 12), (88, 32), (86, 48), (68, 46), (64, 20)], CCR, 'f', False),
                M([(2, 54), (12, 42), (36, 40), (56, 44), (54, 52), (24, 56)], CPU, 'f'),
                M([(36, 12), (50, 10), (42, 22), (52, 22), (34, 40, 1), (40, 26), (30, 26)], YEL, 'f', False)]
    if view == 'side':
        return [M([(6, 50), (8, 22), (28, 6), (56, 2), (80, 10), (90, 30), (90, 46), (50, 50)], CBL, 'f'), M([(6, 50), (8, 22), (28, 6), (40, 4), (30, 48)], CCR, 'f', False),
                M([(82, 44), (104, 42), (108, 48), (86, 52)], CPU, 'f')]
    return [M([(12, 52), (14, 22), (30, 8), (50, 4), (70, 8), (86, 22), (88, 52)], CCR, 'f'), M([(12, 52), (14, 22), (30, 8), (44, 5), (40, 52)], CBL, 'f', False),
            L(ell(50, 50, 8, 3), CPU, 'f')]
C('gen-tillmann', 'normal', P('#965654', '#ac8a64', iris='#5a4040'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=95, face_front=face(w=4, chin=104, jaw=2), hairline=False),
  [L(ell(14, 66, 12, 14), 'mid'), L(ell(86, 66, 12, 14), 'mid'), L(ell(14, 66, 5, 6), 'shade', 'b', False), L(ell(86, 66, 5, 6), 'shade', 'b', False)] + _cap('front') +
  [L([(26, 84), (40, 82)], _c('#7a5a40'), 'f', False, False, 1.2), L([(74, 84), (60, 82)], _c('#7a5a40'), 'f', False, False, 1.2)],
  [L(ell(44, 64, 13, 15), 'mid'), L(ell(44, 64, 5, 6), 'shade', 'b', False)] + _cap('side'),
  [L(ell(14, 66, 12, 14), 'mid'), L(ell(86, 66, 12, 14), 'mid'), M([(14, 60), (86, 60), (84, 80), (50, 86), (16, 80)])] + _cap('back'))

# Gerda Dogge: pelo azul marino oscuro con dos coletas hacia arriba y afuera como orejas de perro, flequillo en pinchos y los
# lados hasta la mandíbula; ojos naranjas grandes
C('gerda-dogge', 'chica', P('#26404f', '#f2c89a', iris='#d86a20'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=hl(6, 70, 48, 60, jit=3, seed=41)),
  dome('front', top=4, w=48, cy=46, n=8, amp=6, sb=86, seed=42) +
  [M([(14, 22), (-6, 20), (-10, 50, 1), (8, 38), (18, 40)]), M([(86, 22), (106, 20), (110, 50, 1), (92, 38), (82, 40)])],
  dome('side', top=4, w=48, cy=46, n=8, amp=6, nape=88, fr=54, seed=42) + [M([(40, 10), (26, -6), (4, 4, 1), (22, 6), (30, 22)])],
  dome('back', top=4, w=48, cy=46, n=8, amp=6, nape=90, seed=42) +
  [M([(14, 22), (-6, 20), (-10, 50, 1), (8, 38), (18, 40)]), M([(86, 22), (106, 20), (110, 50, 1), (92, 38), (82, 40)])])

# Ginger Carret (portero): disfrazado de zanahoria: un cono naranja que le envuelve la cabeza hasta la barbilla, con el tallo
# verde arriba; asoma un rizo rubio en la frente; ojos azules entornados y sonrisa de dientes
CAR, CARD, STEM = _c('#ef914c'), _c('#c8702e'), _c('#5a9a3a')
C('ginger-carret', 'normal', P('#f0d050', '#fbcd9c', iris='#4a7ab0'),
  F(eyes='sharp', brows=True, mouth='grin', mouth_y=94, face_front=face(chin=104), hairline=False),
  [M([(2, 6), (98, 6), (88, 50), (70, 96), (50, 116, 1), (30, 96), (12, 50)], CAR), M([(62, 8), (98, 6), (86, 52), (66, 96), (72, 50)], CARD, 'b', False),
   M([(46, 8), (44, -14), (50, -22, 1), (56, -14), (54, 8)], STEM, 'f'),
   M([(38, 50), (40, 36), (54, 30), (64, 38), (58, 46), (52, 40), (46, 44), (46, 58, 1)], 'mid', 'f')],
  [M([(10, 4), (92, 4), (88, 26), (64, 40), (58, 80), (48, 112, 1), (30, 96), (14, 70), (4, 36)], CAR), M([(46, 4), (44, -16), (50, -24, 1), (56, -16), (54, 4)], STEM, 'f'),
   M([(84, 36), (92, 34), (92, 50), (86, 56, 1)], 'mid', 'f')],
  [M([(2, 6), (98, 6), (88, 50), (70, 96), (50, 116, 1), (30, 96), (12, 50)], CAR), M([(46, 8), (44, -14), (50, -22, 1), (56, -14), (54, 8)], STEM, 'f')])

# Goldie G Lo Locke: melena rubia dorada larga con ondas grandes que le llega a los hombros, raya al lado y mechones que
# enmarcan la cara; ojos ámbar grandes y sonrisa
C('goldie-g-lo-locke', 'chica', P('#cc9a34', '#fdcf9e', iris='#b07a1e', light='#e8c260', shade='#9e6c2e'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(10, 70), (18, 50), (32, 40), (44, 44), (56, 36), (72, 42), (84, 52), (90, 70)]),
  dome('front', top=2, w=48, cy=46, n=0, long=106, flare=10, ends=5, seed=1) +
  [M([(8, 66), (2, 82), (10, 92), (4, 104, 1), (16, 98), (22, 80)], 'light', 'f', False), M([(92, 66), (98, 82), (90, 92), (96, 104, 1), (84, 98), (78, 80)], 'light', 'f', False)],
  dome('side', top=2, w=48, cy=46, n=0, long=104, flare=10, fr=46, seed=1),
  dome('back', top=2, w=48, cy=46, n=0, long=106, flare=10, ends=5, seed=1))

# Gonzalo Karter (portero): casquete de pelo verde agua con dos cuchillas lilas blanquecinas que salen hacia arriba por los
# lados, como alas; patillas en punta; ojos rojos muy enfadados y boca recta
BLADE = _c('#d8d4ec')
C('gonzalo-karter', 'normal', P('#48baa2', '#e2ccae', iris='#8a2a2a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=[(10, 66), (18, 54), (30, 50), (44, 58), (56, 50), (70, 56), (82, 52), (90, 66)]),
  [M([(14, 64), (12, 36), (22, 16), (50, 6), (78, 16), (88, 36), (86, 64), (76, 52), (24, 52)]),
   M([(18, 62), (8, 96, 1), (22, 74)], 'mid', 'f'), M([(82, 62), (92, 96, 1), (78, 74)], 'mid', 'f'),
   M([(20, 64), (2, 10, 1), (32, 34)], BLADE, 'f'), M([(80, 64), (98, 10, 1), (68, 34)], BLADE, 'f')],
  [M([(56, 54), (64, 42), (82, 38), (88, 24), (66, 8), (38, 6), (14, 18), (4, 42), (10, 66), (28, 72), (46, 66)]), M([(46, 60), (40, 4, 1), (60, 30)], BLADE, 'f'),
   M([(60, 58), (60, 92, 1), (68, 70)], 'mid', 'f')],
  [M([(12, 70), (10, 36), (20, 16), (50, 6), (80, 16), (90, 36), (88, 70), (50, 76)]), M([(18, 60), (0, 8, 1), (30, 32)], BLADE, 'f'), M([(82, 60), (100, 8, 1), (70, 32)], BLADE, 'f')])

# Gord Squash (portero): pelo celeste en seta enorme con el borde gris, calado hasta los ojos (no se le ven); perilla
# celeste en la barbilla y media sonrisa
MUSH = _c('#6e6866')
C('gord-squash', 'normal', P('#a6e2e4', '#eaa870'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=92, hairline=False),
  [M([(0, 66), (2, 30), (20, 6), (50, -2), (80, 6), (98, 30), (100, 66), (80, 76), (50, 78), (20, 76)], 'mid', 'f'),
   M([(0, 60), (50, 66), (100, 60), (98, 72), (80, 80), (50, 82), (20, 80), (2, 72)], MUSH, 'f'),
   L(quad((30, 6), (26, 40), (30, 64)), 'shade', 'f', False, False, 1.4), L(quad((70, 6), (74, 40), (70, 64)), 'shade', 'f', False, False, 1.4),
   L([(50, 0), (50, 64)], 'shade', 'f', False, False, 1.4), mark([(44, 100), (56, 100), (54, 106), (46, 106)], 'mid')],
  [M([(-2, 66), (2, 28), (22, 4), (52, -4), (82, 4), (100, 28), (100, 66), (80, 76), (40, 78), (10, 76)], 'mid', 'f'),
   M([(-2, 60), (50, 66), (100, 60), (98, 72), (80, 80), (40, 82), (4, 76)], MUSH, 'f'), mark([(82, 100), (90, 98), (90, 106), (84, 106)], 'mid')],
  [M([(0, 66), (2, 30), (20, 6), (50, -2), (80, 6), (98, 30), (100, 66), (80, 76), (50, 78), (20, 76)], 'mid', 'f'),
   M([(0, 60), (50, 66), (100, 60), (98, 72), (80, 80), (50, 82), (20, 80), (2, 72)], MUSH, 'f')])

# Gordon Bolt: pelo castaño peinado hacia atrás y un mechón rubio en forma de rayo que le cae por la mitad derecha de la cara
# hasta la barbilla; ojos ámbar de enfado
BOLTY = _c('#e8d670')
C('gordon-bolt', 'normal', P('#7a623f', '#fde8b6', iris='#a0601e'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=93, hairline=[(10, 62), (18, 46), (40, 40), (60, 38), (80, 44), (90, 62)]),
  dome('front', top=6, w=46, cy=46, n=0, sb=62, seed=1) + [M([(16, 34), (54, 6), (62, 10), (34, 40), (50, 42), (26, 102, 1), (28, 56), (12, 60)], BOLTY, 'f')],
  dome('side', top=6, w=46, cy=46, n=0, nape=84, fr=44, seed=1),
  dome('back', top=6, w=46, cy=46, n=0, nape=84, seed=1) + [M([(84, 34), (46, 6), (38, 10), (66, 40), (50, 42), (74, 80, 1), (72, 56), (88, 60)], BOLTY, 'f')])

# Gordon Hoe: grandullón con un gorro ceñido marrón oscuro y una placa de metal en la frente, como un ninja; ojitos redondos
# y boca de disgusto; bufanda marrón al cuello
NIN, PLATE, SCARF = _c('#4e4232'), _c('#c8cccc'), _c('#5a4b3a')
C('gordon-hoe', 'corpulento', P('#201c19', '#ce9768', iris='#1e1414'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=95, face_front=face(w=6, chin=104, jaw=3), hairline=False),
  [M([(10, 64), (10, 32), (24, 12), (50, 4), (76, 12), (90, 32), (90, 64), (50, 60)], NIN, 'f'), M([(10, 56), (90, 56), (90, 64), (10, 64)], BLACK, 'f', False),
   M([(40, 50), (60, 50), (60, 62), (40, 62)], PLATE, 'f', True, True)] + scarf('front', SCARF, y=98, h=16),
  [M([(6, 60), (4, 30), (22, 8), (50, 2), (78, 10), (90, 30), (90, 62), (50, 60)], NIN, 'f'), M([(5, 54), (90, 54), (90, 62), (5, 62)], BLACK, 'f', False),
   M([(84, 50), (92, 50), (92, 62), (84, 62)], PLATE, 'f')] + scarf('side', SCARF, y=98, h=16),
  [M([(8, 70), (8, 32), (24, 10), (50, 4), (76, 10), (92, 32), (92, 70), (50, 74)], NIN, 'f'), M([(8, 56), (92, 56), (92, 64), (8, 64)], BLACK, 'f', False)] +
  scarf('back', SCARF, y=98, h=16))

# Graham Bock: gordo de cara redonda; pelo gris oscuro repeinado con pico en la frente y dos rollos en la nuca, a los lados;
# antifaz pintado rojo y negro alrededor de los ojos, nariz redonda pálida y boca de pato
RED = _c('#c8202a')
C('graham-bock', 'corpulento', P('#4a4848', '#f8d6b2', iris='#1e1414', nose='#c8d8dc'),
  F(eyes='sharp', brows='angry', mouth='buck', mouth_y=96, face_front=face(w=6, chin=104, jaw=4), nose=(50, 87, 4.4),
    hairline=[(12, 58), (26, 46), (50, 56), (74, 46), (88, 58)]),
  [L(ell(8, 96, 9, 8), 'mid'), L(ell(92, 96, 9, 8), 'mid'),
   M([(18, 56), (18, 30), (32, 12), (50, 8), (68, 12), (82, 30), (82, 56), (70, 48), (30, 48)]),
   L(ell(36, 76, 10, 6.5) + [ell(36, 76, 10, 6.5)[0]], RED, 'f', False, False, 2.8), L(ell(64, 76, 10, 6.5) + [ell(64, 76, 10, 6.5)[0]], RED, 'f', False, False, 2.8),
   L(quad((30, 100), (50, 106), (70, 100)), RED, 'f', False, False, 1.6)],
  [M([(34, 46), (38, 18), (56, 6), (78, 10), (88, 28), (82, 44), (60, 40)]), L(ell(36, 96, 10, 9), 'mid'),
   L(ell(80, 76, 7, 6.5) + [ell(80, 76, 7, 6.5)[0]], RED, 'f', False, False, 2.8)],
  [M([(16, 70), (16, 30), (32, 12), (50, 8), (68, 12), (84, 30), (84, 70), (50, 76)]), L(ell(10, 94, 10, 9), 'mid'), L(ell(90, 94, 10, 9), 'mid')])

# Grandpa Danger: abuelo calvo con cuatro pelos de punta encima y dos matas negras a los lados; un bigotazo negro enorme,
# ojos redondos con los párpados caídos, nariz larga y coloretes
C('grandpa-danger', 'bajito', P('#17110d', '#fbcf8c', iris='#1e1414'),
  F(eyes='round', brows='angry', mouth='none', hairline=False, eye_sep=15, nose=(50, 84, 3)),
  skull3('front') + [L(ell(12, 62, 9, 12), 'mid'), L(ell(88, 62, 9, 12), 'mid'),
                     L(quad((40, 10), (36, 0), (30, -4)), 'mid', 'f', False, False, 1.2), L(quad((46, 8), (46, -2), (42, -6)), 'mid', 'f', False, False, 1.2),
                     L(quad((54, 8), (56, -2), (60, -6)), 'mid', 'f', False, False, 1.2), L(quad((60, 10), (66, 2), (70, 0)), 'mid', 'f', False, False, 1.2),
                     stache(90, 26, 'mid'), L(ell(24, 86, 3, 2), _c('#e86a6a'), 'f', False), L(ell(76, 86, 3, 2), _c('#e86a6a'), 'f', False)],
  skull3('side') + [L(ell(40, 62, 9, 11), 'mid'), M([(66, 86), (90, 84), (96, 94), (90, 102), (80, 94), (68, 94)], 'mid', 'f'),
                    L(quad((50, 6), (50, -4), (46, -8)), 'mid', 'f', False, False, 1.2)],
  skull3('back') + [L(ell(14, 64, 9, 12), 'mid'), L(ell(86, 64, 9, 12), 'mid'), M([(20, 64), (80, 64), (76, 78), (50, 82), (24, 78)])])

# Grant Hoppa: cara larga tostada; un pañuelo marrón ceñido con dos puntas tiesas que salen hacia arriba como orejas;
# gafas de visera amarillas y patillas grises en cuerno por las mejillas; boca torcida
BAND2, VIS, HORN = _c('#653722'), _c('#b8a020'), _c('#b89088')
C('grant-hoppa', 'delgado', P('#653722', '#eaa462', iris='#1e1414'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=97, face_front=face(chin=110, jaw=-2), face_side=face_side(chin=8), hairline=False),
  [M([(18, 48), (20, 26), (36, 14), (64, 14), (80, 26), (82, 48), (50, 44)], BAND2, 'f'),
   M([(42, 20), (14, -8), (-12, -16, 1), (0, 0), (30, 26)], BAND2, 'f'), M([(58, 20), (86, -8), (112, -16, 1), (100, 0), (70, 26)], BAND2, 'f'),
   M([(24, 72), (76, 72), (72, 80), (28, 80)], VIS, 'f'),
   M([(18, 86), (28, 84), (36, 98), (28, 102, 1)], HORN, 'f'), M([(82, 86), (72, 84), (64, 98), (72, 102, 1)], HORN, 'f')],
  [M([(14, 50), (14, 26), (34, 12), (64, 10), (84, 22), (88, 44), (50, 44)], BAND2, 'f'), M([(40, 16), (24, -10), (2, -18, 1), (20, -2), (32, 22)], BAND2, 'f'),
   M([(70, 70), (90, 70), (90, 80), (72, 80)], VIS, 'f'), M([(60, 86), (72, 84), (78, 98), (70, 102, 1)], HORN, 'f')],
  [M([(16, 52), (18, 26), (36, 12), (64, 12), (82, 26), (84, 52), (50, 50)], BAND2, 'f'),
   M([(40, 18), (10, -12), (-12, -14, 1), (8, -2), (34, 22)], BAND2, 'f'), M([(60, 18), (90, -12), (112, -14, 1), (92, -2), (66, 22)], BAND2, 'f')])

# Greena Grasse (portera): una nube enorme de rizos crema muy claros, castaña por debajo; ojos azules grandes, coloretes y
# boca pequeña de disgusto
C('greena-grasse', 'chica', P('#fefbd6', '#fccb9c', iris='#6aa0c0', shade='#c8a890', deep='#ac7c68'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=93, hairline=hl(8, 62, 50, 58, jit=3, seed=51)),
  [M([(4, 72), (2, 56), (12, 54), (14, 82), (6, 86)], 'deep'), M([(96, 72), (98, 56), (88, 54), (86, 82), (94, 86)], 'deep')] +
  dome('front', top=-8, w=56, cy=40, n=15, amp=6, soft=True, sb=66, seed=52) + blush(86),
  [M([(26, 74), (50, 70), (56, 86), (34, 90)], 'deep')] + dome('side', top=-8, w=54, cy=40, n=15, amp=6, soft=True, nape=80, fr=50, seed=52),
  [M([(8, 82), (6, 60), (94, 60), (92, 82), (50, 88)], 'deep')] + dome('back', top=-8, w=56, cy=40, n=15, amp=6, soft=True, nape=72, seed=52))

# Griz Munkie: melena morada echada hacia atrás con volumen arriba y mechones largos que le caen hasta los hombros; piel
# morena, cejas moradas de enfado y ojos grises
C('griz-munkie', 'normal', P('#6a5076', '#bd8450', iris='#8a8a92', brow='#533a4f'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=93, hairline=[(10, 66), (18, 48), (36, 40), (50, 44), (64, 40), (82, 48), (90, 66)]),
  dome('front', top=0, w=50, cy=44, n=0, long=106, flare=8, ends=4, seed=1) + thick_brows(64, 'brow', 3.6, 15, 1.4, 12),
  dome('side', top=0, w=50, cy=44, n=0, long=104, flare=8, fr=44, seed=1),
  dome('back', top=0, w=50, cy=44, n=0, long=106, flare=8, ends=4, seed=1))

# Gus Bagge: cara larga muy pálida; pelo gris azulado en flequillo plano peinado hacia atrás con los lados cortos; ojos
# ámbar sombríos y una sonrisa enorme de dientes
C('gus-bagge', 'delgado', P('#bed8d8', '#fdeed2', iris='#c06a1e'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=97, face_front=face(chin=110, jaw=1), face_side=face_side(chin=8),
    hairline=[(12, 62), (18, 44), (34, 40), (50, 42), (66, 40), (82, 44), (88, 62)]),
  [M([(16, 62), (14, 22), (24, 8), (50, 4), (76, 8), (86, 22), (84, 62), (78, 44), (22, 44)]), M([(60, 6), (78, 10), (86, 30), (84, 58), (74, 30)], 'shade', 'b', False)],
  [M([(56, 52), (60, 40), (80, 36), (86, 18), (66, 4), (36, 4), (14, 14), (8, 40), (14, 62), (34, 66), (48, 60)])],
  [M([(14, 66), (12, 22), (24, 8), (50, 4), (76, 8), (88, 22), (86, 66), (50, 72)]), M([(60, 8), (78, 12), (88, 30), (86, 62), (66, 50)], 'shade', 'b', False)])

# Gus Duneaton (portero): media melena castaña clara en casco con flequillo; cara redonda con pecas, ojos redondos
# preocupados y boca pequeña
C('gus-duneaton', 'normal', P('#b29c7a', '#fcce9e', iris='#3a2a1a'),
  F(eyes='round', brows=True, mouth='frown', mouth_y=94, face_front=face(w=3, chin=104, jaw=2), hairline=False),
  bowl3('front', top=4, side=80, fringe=56) + freckles(86, 22),
  bowl3('side', top=4, nape=88, fringe=56),
  bowl3('back', top=4, nape=88))

# Gus Tronom: pelo azul marino en un penacho de pinchos arriba, gafas de piloto con cristales rojos sobre una cinta negra en
# la frente; sonrisa de dientes con malicia
C('gus-tronom', 'normal', P('#525e8a', '#f6ba7e', iris='#1e1414'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, hairline=[(12, 62), (18, 48), (50, 44), (82, 48), (88, 62)]),
  [M([(14, 60), (12, 36), (22, 18), (36, 10), (40, -10, 1), (48, 4), (56, -14, 1), (60, 4), (74, -6, 1), (72, 12), (84, 24), (88, 40), (86, 60), (74, 48), (26, 48)])] +
  goggles('front', y=52, frame=_c('#e8e0c8'), lens=_c('#a03040')) + [M([(8, 50), (92, 50), (92, 55), (8, 55)], BLACK, 'b', False)],
  [M([(56, 52), (62, 40), (84, 36), (88, 20), (70, 6), (60, -14, 1), (50, 4), (32, 6), (14, 16), (6, 40), (12, 62), (30, 70), (46, 64)])] +
  goggles('side', y=50, frame=_c('#e8e0c8'), lens=_c('#a03040')),
  [M([(14, 66), (12, 36), (22, 18), (36, 10), (40, -10, 1), (48, 4), (56, -14, 1), (60, 4), (74, -6, 1), (72, 12), (84, 24), (88, 40), (86, 66), (50, 72)])] +
  goggles('back', y=52, frame=_c('#202020')))

# Gwen Slinga: sombrero vaquero caqui con una pluma blanca en la cinta y una estrella dorada; melena granate que le sale
# por debajo a los lados en mechones; ojos amarillos grandes y boca de disgusto
KHA, KHAD, FEA, STAR = _c('#b2a379'), _c('#8e8058'), _c('#ece8da'), _c('#f0c040')
def _cowboy(view):
    if view == 'front':
        return [M([(22, 40), (24, 14), (40, 4), (50, 10), (60, 4), (76, 14), (78, 40)], KHA, 'f'),
                M([(2, 40), (20, 30), (50, 36), (80, 30), (100, 32), (94, 46), (70, 52), (50, 50), (30, 52), (6, 50)], KHA, 'f'),
                M([(30, 34), (60, 26), (76, 28), (52, 38), (36, 44)], FEA, 'f', False),
                M([(80, 32), (82, 26, 1), (84, 32), (90, 32, 1), (85, 35), (87, 41, 1), (82, 37), (77, 41, 1), (79, 35), (74, 32, 1)], STAR, 'f', False)]
    if view == 'side':
        return [M([(20, 38), (24, 10), (50, 2), (76, 10), (80, 38)], KHA, 'f'), M([(-6, 40), (20, 32), (60, 32), (104, 30), (100, 42), (60, 46), (6, 48)], KHA, 'f'),
                M([(24, 32), (76, 32), (78, 38), (22, 38)], FEA, 'f', False)]
    return [M([(22, 40), (24, 14), (40, 4), (50, 10), (60, 4), (76, 14), (78, 40)], KHA, 'f'),
            M([(2, 42), (20, 34), (50, 38), (80, 34), (98, 42), (94, 50), (50, 54), (6, 50)], KHA, 'f')]
C('gwen-slinga', 'chica', P('#a2303c', '#eba866', iris='#e0c020'),
  F(eyes='big', brows=True, mouth='frown', mouth_y=93, hairline=[(10, 66), (16, 54), (50, 50), (84, 54), (90, 66)]),
  [M([(14, 54), (6, 64), (-4, 74, 1), (8, 76), (2, 88, 1), (16, 84), (22, 64)]), M([(86, 54), (94, 64), (104, 74, 1), (92, 76), (98, 88, 1), (84, 84), (78, 64)]),
   M([(14, 60), (16, 46), (84, 46), (86, 60), (50, 54)])] + _cowboy('front'),
  [M([(56, 52), (60, 44), (84, 44), (88, 52), (64, 56), (52, 74), (30, 86, 1), (36, 74), (12, 78, 1), (20, 66), (6, 60), (14, 44)])] + _cowboy('side'),
  [M([(10, 82), (8, 50), (92, 50), (90, 82), (70, 76), (60, 90, 1), (50, 78), (40, 90, 1), (30, 76)])] + _cowboy('back'))

# Hal Istic: pelo azul con flequillo barrido hacia su izquierda que le tapa la frente y cae largo por ese lado; gafas de
# montura amarilla con sombra morada, ojos verdes y una mascarilla blanca
MASK, YFR = _c('#f4f4f2'), _c('#e0c838')
C('hal-istic', 'normal', P('#548faa', '#faf0d8', iris='#3a8a50'),
  F(eyes='sharp', brows='angry', mouth='none', hairline=[(10, 62), (16, 46), (30, 42), (50, 46), (70, 40), (86, 50), (90, 70)]),
  [M([(12, 64), (10, 36), (22, 14), (46, 4), (72, 8), (88, 24), (92, 50), (92, 86), (84, 92, 1), (80, 60), (60, 50), (40, 46), (22, 54)]),
   M([(30, 30), (60, 14), (84, 30), (88, 60), (84, 86, 1), (78, 54), (64, 46), (46, 54), (52, 40)], 'mid', 'f'),
   L(blob([(24, 70), (46, 70), (46, 74), (24, 74)], 4), _c('#9a6ab0'), 'f', False), L(blob([(54, 70), (76, 70), (76, 74), (54, 74)], 4), _c('#9a6ab0'), 'f', False)] +
  round_specs('front', YFR, y=77, sep=14, rx=10, ry=6.5, w=2.0) +
  [M([(28, 84), (50, 80), (72, 84), (70, 100), (50, 106), (30, 100)], MASK, 'f'), L([(30, 92), (70, 92)], _c('#c8c8c8'), 'f', False, False, 0.8)],
  [M([(56, 52), (64, 40), (86, 36), (92, 22), (70, 4), (40, 2), (16, 14), (6, 40), (12, 66), (30, 74), (46, 66)])] + round_specs('side', YFR, y=77) +
  [M([(70, 84), (90, 82), (92, 100), (76, 104)], MASK, 'f'), L([(70, 86), (48, 74)], MASK, 'f', False, False, 1.2)],
  [M([(12, 70), (10, 36), (22, 14), (50, 4), (78, 14), (90, 36), (88, 70), (50, 76)]), L(quad((12, 80), (50, 84), (88, 80)), MASK, 'f', False, False, 1.2)])

# Hamish Voracio: cabeza redonda morena y calva con un penacho rubio con dos cuernitos encima; nariz roja de payaso, una
# estrella azul tatuada alrededor del ojo izquierdo y gesto de enfado
YELH = _c('#f0c030')
C('hamish-voracio', 'corpulento', P('#856552', '#be8c68', iris='#1e1414', nose='#e05a3a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, face_front=face(w=7, chin=106, jaw=3, top=14), nose=(50, 84, 4.6), big_ears=2, ear_out=6, hairline=False),
  [L(blob([(14, 56), (16, 30), (30, 12), (50, 6), (70, 12), (84, 30), (86, 56)], 8), 'skin'),
   M([(38, 12), (34, 0), (24, -6, 1), (38, -6), (50, 2), (62, -6), (76, -6, 1), (66, 0), (62, 12), (50, 18)], YELH, 'f'),
   L([(56, 68), (62, 64), (64, 56), (68, 64), (78, 62), (74, 70), (80, 80), (72, 80), (70, 88), (64, 82), (56, 86), (58, 76), (56, 68)], _c('#3a5a8a'), 'f', False, False, 1.8)],
  skull3('side') + [M([(40, 6), (36, -4), (28, -10, 1), (44, -6), (56, 4)], YELH, 'f')],
  skull3('back') + [M([(38, 12), (34, 0), (24, -6, 1), (38, -6), (50, 2), (62, -6), (76, -6, 1), (66, 0), (62, 12), (50, 18)], YELH, 'f')])

# Hank Saw: pelo gris plateado en una bóveda alta como un huevo, con un flequillo blanco de dientes de sierra; ojos amarillos
# afilados y boca en zigzag
C('hank-saw', 'normal', P('#c4bab1', '#fceed4', iris='#c8a020'),
  F(eyes='sharp', brows=False, mouth='none', hairline=hl(7, 64, 46, 56, seed=61)),
  [M([(14, 62), (10, 30), (20, 2), (50, -14), (80, 2), (90, 30), (86, 62), (76, 48), (24, 48)]),
   M([(14, 52), (16, 36), (24, 30), (30, 40), (38, 24), (44, 38), (50, 22), (56, 38), (62, 24), (70, 40), (76, 30), (84, 36), (86, 52), (50, 48)], WHITE, 'f'),
   M([(36, -2), (40, -14, 1), (46, -4), (50, -16, 1), (54, -4), (60, -14, 1), (64, -2), (50, 2)], WHITE, 'f'),
   L([(40, 93), (43, 90), (46, 94), (50, 90), (54, 94), (57, 90), (60, 93)], OUTC, 'f', False, False, 1.3)],
  [M([(56, 52), (64, 40), (84, 36), (90, 16), (70, -6), (44, -14), (18, 0), (6, 30), (10, 62), (30, 72), (46, 64)]),
   M([(60, 44), (64, 34), (72, 40), (78, 30), (88, 36), (88, 24), (64, 24)], WHITE, 'f')],
  [M([(12, 68), (10, 30), (20, 2), (50, -14), (80, 2), (90, 30), (88, 68), (50, 74)])])

# Hardy Scrapper: pelo crema peinado hacia arriba en una cresta enorme que se curva hacia su izquierda, con una franja negra;
# los lados rapados con rayas; piel tostada, ojos azules y sonrisa de dientes
C('hardy-scrapper', 'normal', P('#dcd2a8', '#cc9469', iris='#3a8ac8', low='#8a7a5a'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, hairline=[(12, 64), (20, 50), (36, 46), (50, 52), (64, 46), (80, 50), (88, 64)]),
  [M([(16, 70), (14, 48), (84, 48), (86, 70), (78, 56), (22, 56)], 'low'),
   M([(24, 52), (22, 30), (30, 10), (44, -8), (60, -18), (80, -14, 1), (68, -6), (76, 10), (74, 32), (76, 52), (60, 46), (40, 46)]),
   M([(46, -8), (60, -18), (66, -12), (52, 4), (48, 40), (40, 40)], BLACK, 'f'),
   L([(16, 60), (22, 56)], OUTC, 'f', False, False, 0.8), L([(84, 60), (78, 56)], OUTC, 'f', False, False, 0.8)],
  [M([(14, 64), (16, 44), (54, 46), (52, 64), (30, 74)], 'low'),
   M([(50, 48), (40, 20), (50, 0), (70, -16), (92, -14, 1), (80, -4), (90, 16), (86, 34), (70, 44)]), M([(56, -4), (72, -14), (74, -8), (62, 8), (60, 40), (54, 40)], BLACK, 'f')],
  [M([(14, 76), (12, 48), (88, 48), (86, 76), (50, 82)], 'low'),
   M([(26, 54), (24, 30), (32, 10), (46, -8), (62, -18), (82, -14, 1), (70, -6), (76, 10), (74, 54)]), M([(46, -8), (60, -18), (66, -12), (52, 10), (50, 54), (44, 54)], BLACK, 'f')])

# Harold Oldings (portero): grandullón de cara ancha y anaranjada; pelo gris oscuro corto en cepillo; ceño marcado con
# arrugas, ojos entornados, nariz ancha y boca recta
C('harold-oldings', 'corpulento', P('#4e585c', '#f8ba7c', iris='#1e1414'),
  F(eyes='closed', brows='angry', mouth='line', mouth_y=96, face_front=face(w=8, chin=106, jaw=5), nose=(50, 86, 4.4), hairline=[(8, 64), (14, 48), (50, 42), (86, 48), (92, 64)]),
  [M([(8, 66), (6, 36), (18, 14), (50, 4), (82, 14), (94, 36), (92, 66), (84, 48), (16, 48)]),
   L(quad((30, 66), (50, 62), (70, 66)), OUTC, 'f', False, False, 1.0), L(quad((34, 70), (50, 67), (66, 70)), OUTC, 'f', False, False, 0.8)],
  [M([(56, 52), (62, 40), (84, 36), (90, 20), (70, 4), (40, 2), (14, 14), (4, 40), (10, 66), (30, 74), (46, 66)])],
  [M([(6, 72), (6, 36), (18, 14), (50, 4), (82, 14), (94, 36), (94, 72), (50, 78)])])

# Harriet Bunne: media melena rubio oliva en seta, con un moño arriba y una flor morada; mechones largos que le caen junto a
# la cara; ojos entornados y sonrisa pícara
FLOW, FLOWC = _c('#7a5ab8'), _c('#f0c840')
C('harriet-bunne', 'chica', P('#bda96e', '#f8d8b4', iris='#2a2020', shade='#917048'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=92, hairline=[(10, 70), (16, 54), (30, 50), (40, 58), (50, 50), (60, 58), (70, 50), (84, 54), (90, 70)]),
  bowl3('front', top=8, side=76, w=6, fringe=56) +
  [L(ell(44, 2, 13, 10), 'mid'), L(ell(66, 0, 9, 9), FLOW, 'f'), L(ell(66, 0, 3, 3), FLOWC, 'f', False),
   M([(22, 60), (28, 60), (30, 100, 1), (22, 84)], 'mid', 'f'), M([(78, 60), (72, 60), (70, 100, 1), (78, 84)], 'mid', 'f')],
  bowl3('side', top=8, nape=82, w=6, fringe=56) + [L(ell(44, 0, 12, 10), 'mid'), L(ell(56, -2, 8, 8), FLOW, 'f')],
  bowl3('back', top=8, nape=82, w=6) + [L(ell(50, 2, 13, 10), 'mid'), L(ell(66, 0, 9, 9), FLOW, 'f')])

# Harriet Pynn (portera): melena índigo en campana enorme abierta por abajo, con un moño alto atravesado por un alfiler con
# bola roja; cejas de punto, ojos verde agua con rabillo rojo y sonrisa
PIN, PINB = _c('#e8e0d8'), _c('#e04a2a')
C('harriet-pynn', 'chica', P('#433576', '#f6eac6', iris='#3aa098'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, hairline=[(10, 64), (18, 50), (50, 44), (82, 50), (90, 64)]),
  [M([(-4, 74), (2, 54), (14, 32), (30, 18), (50, 14), (70, 18), (86, 32), (98, 54), (104, 74), (86, 76), (80, 60), (20, 60), (14, 76)]),
   L(ell(50, 6, 13, 12), 'mid'), L(ell(50, 6, 13, 12), 'shade', 'b', False), L([(28, 2), (72, -2)], PIN, 'f', False, False, 1.4), L(ell(26, 2, 4, 4), PINB, 'f'),
   L(ell(38, 64, 1.6, 1.6), 'shade', 'f', False), L(ell(62, 64, 1.6, 1.6), 'shade', 'f', False),
   L([(24, 78), (30, 76)], _c('#d04a3a'), 'f', False, False, 1.2), L([(76, 78), (70, 76)], _c('#d04a3a'), 'f', False, False, 1.2)],
  [M([(56, 52), (64, 40), (84, 36), (90, 26), (70, 16), (40, 14), (14, 26), (0, 52), (-6, 76), (14, 78), (30, 66), (46, 62)]), L(ell(44, 4, 12, 12), 'mid')],
  [M([(-4, 78), (2, 54), (14, 32), (30, 18), (50, 14), (70, 18), (86, 32), (98, 54), (104, 78), (50, 84)]), L(ell(50, 6, 13, 12), 'mid'),
   L([(28, 2), (72, -2)], PIN, 'f', False, False, 1.4), L(ell(74, -2, 4, 4), PINB, 'f')])

# Hart O Gold: pelo dorado corto peinado hacia atrás con mechas en llama y dos puntas que salen hacia fuera a la altura de la
# mandíbula; piel morena, ojos verdes con raya negra gruesa de enfado y labios gruesos
GOLD = _c('#b78014')
C('hart-o-gold', 'corpulento', P('#c08a1e', '#ae8660', iris='#8ab040', light='#e8c040'),
  F(eyes='sharp', brows='angry', mouth='lips', mouth_w=9, mouth_y=96, face_front=face(w=6, chin=104, jaw=4), hairline=[(12, 56), (22, 44), (50, 40), (78, 44), (88, 56)]),
  [M([(18, 50), (18, 24), (32, 10), (50, 6), (68, 10), (82, 24), (82, 50), (70, 42), (30, 42)]),
   M([(30, 20), (40, 14), (38, 30), (46, 26), (42, 40)], 'light', 'b', False), M([(56, 14), (64, 18), (60, 34), (68, 30), (64, 40)], 'light', 'b', False),
   M([(16, 86), (2, 90, 1), (14, 80), (4, 76, 1), (18, 78)], GOLD, 'b'), M([(84, 86), (98, 90, 1), (86, 80), (96, 76, 1), (82, 78)], GOLD, 'b')],
  [M([(40, 44), (40, 18), (56, 6), (78, 10), (88, 26), (84, 42), (62, 38)]), M([(40, 86), (26, 92, 1), (38, 80), (28, 74, 1), (44, 78)], GOLD, 'b')],
  [M([(16, 60), (16, 26), (32, 10), (50, 6), (68, 10), (84, 26), (84, 60), (50, 64)])])

# Hartwin Throbb: media melena rubio pálido alborotada con un flequillo de mechones que le tapa media frente y puntas hacia
# fuera; piel tostada y ojos verde azulado
C('hartwin-throbb', 'chica', P('#fcf0a2', '#eca562', iris='#3a8a9a', shade='#ccaa76'),
  F(eyes='big', brows=True, mouth='frown', mouth_y=93, hairline=[(10, 74), (16, 52), (30, 46), (40, 62), (48, 46), (60, 58), (70, 46), (84, 54), (90, 72)]),
  dome('front', top=4, w=48, cy=46, n=8, amp=6, sweep=0.4, sb=84, seed=71) + [M([(84, 56), (96, 62), (104, 58, 1), (98, 70), (88, 74)])],
  dome('side', top=4, w=48, cy=46, n=8, amp=6, sweep=0.4, nape=88, fr=58, seed=71),
  dome('back', top=4, w=48, cy=46, n=8, amp=6, sweep=0.4, nape=88, seed=71))

# Heezbie Heindyu (portero): pañuelo verde oliva enrollado en la cabeza, anudado a un lado con una cola que cuelga; un
# antifaz negro pintado alrededor de los ojos y perilla negra en picos; piel tostada
OLV, OLVD = _c('#8e864a'), _c('#64522a')
C('heezbie-heindyu', 'normal', P('#1e1a1a', '#bc8a52', iris='#1e1414'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=93, hairline=False),
  [M([(12, 56), (12, 28), (26, 10), (50, 4), (74, 10), (88, 28), (88, 56), (50, 52)], OLV, 'f'),
   L(quad((14, 30), (50, 20), (86, 30)), OLVD, 'f', False, False, 1.6), L(quad((12, 44), (50, 36), (88, 44)), OLVD, 'f', False, False, 1.6),
   M([(86, 50), (102, 60), (104, 82, 1), (94, 70), (88, 62)], OLV, 'f'),
  ] + eye_mask() + [
   M([(42, 100), (44, 108, 1), (48, 102), (50, 110, 1), (52, 102), (56, 108, 1), (58, 100)], BLACK, 'f', False)],
  [M([(6, 58), (4, 30), (22, 8), (50, 2), (78, 10), (90, 30), (90, 54), (50, 54)], OLV, 'f'), M([(14, 50), (2, 64), (4, 84, 1), (12, 66), (24, 56)], OLV, 'f'),
   M([(70, 70), (90, 68), (90, 80), (72, 80)], BLACK, 'f', False)],
  [M([(10, 64), (10, 28), (26, 10), (50, 4), (74, 10), (90, 28), (90, 64), (50, 66)], OLV, 'f'), M([(14, 50), (-2, 60), (-4, 82, 1), (6, 70), (12, 62)], OLV, 'f')])

# Hilda Brunner: yelmo de caballero de cuero marrón con la visera de barrotes que le tapa los ojos y dos cuernos curvos
# hacia arriba a los lados; la parte de arriba azul pizarra; asoman mechones blancos por los lados; boca de disgusto
LEA, SLATE = _c('#b68660'), _c('#565870')
def _helm(view):
    if view == 'front':
        out = [M([(14, 52), (16, 22), (32, 6), (50, 2), (68, 6), (84, 22), (86, 52)], SLATE, 'f'),
               M([(12, 58), (20, 44), (50, 40), (80, 44), (88, 58), (80, 84), (50, 86), (20, 84)], LEA, 'f'),
               M([(16, 54), (2, 14), (-2, -6, 1), (10, 10), (24, 46)], LEA, 'f'), M([(84, 54), (98, 14), (102, -6, 1), (90, 10), (76, 46)], LEA, 'f')]
        for x in (38, 46, 54, 62):
            out.append(M([(x - 2, 56), (x + 2, 56), (x + 2, 80), (x - 2, 80)], BLACK, 'f', False))
        return out
    if view == 'side':
        return [M([(6, 56), (4, 24), (24, 4), (52, 0), (80, 8), (92, 28), (90, 48), (50, 50)], SLATE, 'f'),
                M([(40, 48), (60, 44), (92, 48), (92, 84), (70, 88), (50, 80)], LEA, 'f'), M([(46, 52), (40, 8), (34, -10, 1), (54, 6), (58, 46)], LEA, 'f')]
    return [M([(10, 60), (12, 24), (30, 6), (50, 2), (70, 6), (88, 24), (90, 60), (50, 64)], SLATE, 'f'),
            M([(14, 54), (0, 14), (-4, -6, 1), (8, 10), (22, 46)], LEA, 'f'), M([(86, 54), (100, 14), (104, -6, 1), (92, 10), (78, 46)], LEA, 'f')]
C('hilda-brunner', 'chica', P('#f2eef0', '#fbf0e0', iris='#1e1414'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=94, hairline=False),
  [M([(14, 60), (20, 60), (24, 104, 1), (14, 94), (6, 100, 1), (10, 80)]), M([(86, 60), (80, 60), (76, 104, 1), (86, 94), (94, 100, 1), (90, 80)])] + _helm('front'),
  [M([(40, 56), (50, 56), (52, 100, 1), (40, 92), (32, 98, 1), (34, 76)])] + _helm('side'),
  [M([(14, 60), (86, 60), (90, 100, 1), (76, 92), (64, 104, 1), (50, 94), (36, 104, 1), (24, 92), (10, 100, 1)])] + _helm('back'))

# Hippolytus Hippo Horseriver (portero): cara de hipopótamo: cabeza ancha y redonda morena con orejitas redondas arriba y un
# casquete de pelo gris azulado; ojitos diminutos, dos orificios nasales enormes y boca de disgusto
C('hippolytus-hippo-horseriver', 'corpulento', P('#5a6a8a', '#be834c', iris='#e8e8e8'),
  F(eyes='dot', brows=False, mouth='frown', mouth_y=97, face_front=face(w=9, chin=104, jaw=4, top=20), eye_y=68, eye_sep=17, hairline=False),
  [L(ell(14, 36, 10, 9), 'skin'), L(ell(86, 36, 10, 9), 'skin'), L(ell(14, 36, 5, 4.5), 'skin_d', 'b', False), L(ell(86, 36, 5, 4.5), 'skin_d', 'b', False),
   L(blob([(14, 56), (16, 32), (30, 18), (50, 14), (70, 18), (84, 32), (86, 56)], 8), 'skin'), M([(32, 24), (40, 14), (50, 12), (60, 14), (68, 24), (50, 26)]),
   L(ell(41, 82, 5, 5), BLACK, 'f', False), L(ell(59, 82, 5, 5), BLACK, 'f', False)],
  skull3('side') + [L(ell(46, 30, 9, 9), 'skin'), M([(56, 18), (66, 14), (76, 22), (64, 26)]), L(ell(88, 82, 3, 4), BLACK, 'f', False)],
  skull3('back') + [L(ell(14, 36, 10, 9), 'skin'), L(ell(86, 36, 10, 9), 'skin'), M([(32, 24), (40, 14), (50, 12), (60, 14), (68, 24), (50, 28)])])

# Holly Butterfly Blue: melena blanca plateada peinada hacia atrás, larga y ondulada hasta los hombros; antifaz negro alrededor
# de los ojos rojos, labios morados y piel tostada
C('holly-butterfly-blue', 'chica', P('#dceaea', '#eba664', iris='#c02a2a', shade='#a8b8b8'),
  F(eyes='sharp', brows=True, mouth='lips', mouth_w=7, mouth_y=95, hairline=[(10, 66), (18, 46), (34, 38), (50, 40), (66, 38), (82, 46), (90, 66)]),
  dome('front', top=0, w=48, cy=44, n=0, long=110, flare=10, ends=4, seed=1) +
  eye_mask(),
  dome('side', top=0, w=48, cy=44, n=0, long=108, flare=10, fr=42, seed=1) + [M([(70, 68), (90, 66), (90, 80), (72, 80)], BLACK, 'f', False)],
  dome('back', top=0, w=48, cy=44, n=0, long=110, flare=10, ends=4, seed=1))

# Homer Cooken: gordito calvo con un ricito castaño arriba; cara redonda, ojos cerrados de risa, nariz rosada enorme y una
# carcajada con la boca abierta y un diente mellado
C('homer-cooken', 'corpulento', P('#7f6a60', '#fdcd9c', iris='#1e1414', nose='#d88462'),
  F(eyes='closed', brows=True, mouth='none', face_front=face(w=7, chin=104, jaw=4, top=16), nose=(50, 82, 6), big_ears=1, ear_out=4, hairline=False),
  [L(blob([(14, 56), (16, 30), (30, 14), (50, 8), (70, 14), (84, 30), (86, 56)], 8), 'skin'),
   M([(44, 14), (40, 2), (48, -8, 1), (54, 0), (52, 14)]),
   M([(36, 90), (64, 90), (60, 102), (50, 106), (40, 102)], _c('#7a2a2a'), 'f'), M([(38, 90), (62, 90), (60, 94), (40, 94)], WHITE, 'f', False),
   M([(48, 90), (52, 90), (52, 94), (48, 94)], _c('#7a2a2a'), 'f', False)],
  skull3('side') + [M([(48, 6), (44, -6), (52, -12, 1), (58, -2), (56, 8)]), M([(80, 90), (92, 90), (90, 102), (82, 100)], _c('#7a2a2a'), 'f')],
  skull3('back') + [M([(44, 14), (40, 2), (48, -8, 1), (54, 0), (52, 14)])])

# Howard Robin: sombrero de mosquetero gris oscuro de ala ancha caída hacia su derecha, con dos plumas blancas rosadas y un
# broche dorado con una gema roja; pelo rubio corto debajo; ojos rosas y sonrisa
HAT2, FEA2, BRO, GEM = _c('#57514c'), _c('#f2e6e8'), _c('#e0a020'), _c('#a02a3a')
def _musket(view):
    if view == 'front':
        return [M([(18, 46), (22, 18), (40, 6), (62, 6), (80, 18), (84, 40)], HAT2, 'f'),
                M([(-4, 64), (6, 44), (30, 34), (60, 32), (86, 36), (100, 46), (88, 54), (60, 48), (30, 52), (10, 62)], HAT2, 'f'),
                M([(40, 34), (70, 4), (96, -18, 1), (82, 10), (56, 40)], FEA2, 'f'), M([(54, 30), (80, 2), (104, -8, 1), (86, 16), (64, 40)], FEA2, 'f'),
                L(ell(60, 42, 7, 6), BRO, 'f'), L(ell(60, 42, 3, 3), GEM, 'f', False)]
    if view == 'side':
        return [M([(18, 40), (22, 12), (46, 2), (74, 8), (84, 34)], HAT2, 'f'), M([(-6, 50), (20, 36), (60, 34), (102, 40), (96, 50), (60, 46), (4, 56)], HAT2, 'f'),
                M([(30, 32), (20, 4), (6, -14, 1), (24, 0), (40, 30)], FEA2, 'f')]
    return [M([(18, 48), (22, 18), (40, 6), (62, 6), (80, 18), (84, 46)], HAT2, 'f'),
            M([(0, 52), (20, 40), (50, 38), (80, 40), (102, 60), (90, 62), (60, 52), (20, 54)], HAT2, 'f'),
            M([(60, 34), (30, 4), (4, -18, 1), (18, 10), (44, 40)], FEA2, 'f')]
C('howard-robin', 'normal', P('#e8d47a', '#f0c89a', iris='#c04a7a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(10, 62), (16, 54), (50, 52), (84, 54), (90, 62)]),
  [M([(14, 66), (12, 48), (88, 48), (90, 66), (80, 58), (20, 58)])] + _musket('front'),
  [M([(56, 56), (62, 48), (86, 48), (88, 56), (64, 58), (52, 70), (30, 76), (10, 70), (8, 50)])] + _musket('side'),
  [M([(12, 76), (10, 50), (90, 50), (88, 76), (50, 82)])] + _musket('back'))

# Hugh Handy: gorro de punto rosa con franjas verde agua y dos picos como orejas de gato, calado hasta los ojos con la visera
# verde agua; asoma pelo castaño oscuro a los lados; coloretes y sonrisa
PNK, TEA = _c('#f8aeaa'), _c('#7ac8c0')
def _cathat(view):
    if view == 'front':
        return [M([(10, 60), (10, 24), (6, -6, 1), (30, 6), (50, 4), (70, 6), (94, -6, 1), (90, 24), (90, 60)], PNK, 'f'),
                M([(10, 22), (50, 18), (90, 22), (90, 38), (50, 34), (10, 38)], TEA, 'f', False),
                M([(8, 52), (30, 50), (50, 52), (70, 50), (92, 52), (92, 66), (70, 76), (50, 78), (30, 76), (8, 66)], TEA, 'f')]
    if view == 'side':
        return [M([(6, 62), (4, 26), (14, -4, 1), (34, 6), (60, 4), (84, 14), (92, 34), (92, 54), (50, 56)], PNK, 'f'),
                M([(4, 26), (50, 20), (92, 30), (92, 44), (50, 36), (4, 42)], TEA, 'f', False), M([(50, 50), (92, 50), (104, 62), (94, 72), (56, 64)], TEA, 'f')]
    return [M([(8, 66), (10, 24), (6, -6, 1), (30, 6), (50, 4), (70, 6), (94, -6, 1), (90, 24), (92, 66), (50, 70)], PNK, 'f'),
            M([(10, 22), (50, 18), (90, 22), (90, 38), (50, 34), (10, 38)], TEA, 'f', False), M([(8, 54), (92, 54), (92, 66), (50, 72), (8, 66)], TEA, 'f', False)]
C('hugh-handy', 'normal', P('#3a2620', '#fdd5ae'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=92, hairline=False),
  [M([(10, 62), (8, 80), (16, 84), (20, 66)]), M([(90, 62), (92, 80), (84, 84), (80, 66)])] + _cathat('front') + blush(86),
  [M([(48, 60), (44, 78), (56, 80), (60, 62)])] + _cathat('side'),
  [M([(10, 66), (12, 82), (50, 86), (88, 82), (90, 66)])] + _cathat('back'))

# Hulk Flounder (portero): gordo de cabeza redonda anaranjada; un tupé rubio rizado en lo alto y los lados rapados con rayas
# rubias; ojos redondos de párpados caídos con ojeras negras y la boca entreabierta babeando
C('hulk-flounder', 'corpulento', P('#ead38c', '#eca560', iris='#1e1414'),
  F(eyes='round', brows=False, mouth='buck', mouth_y=96, face_front=face(w=8, chin=106, jaw=5, top=16), eye_sep=15, hairline=False),
  [L(blob([(12, 56), (14, 30), (30, 14), (50, 8), (70, 14), (86, 30), (88, 56)], 8), 'skin'),
   M([(30, 18), (26, 0), (38, -14), (58, -18), (72, -8), (64, 2), (70, 14), (52, 22)]), M([(44, -8), (56, -10), (58, 4), (48, 8)], 'shade', 'b', False),
   L(quad((18, 44), (24, 24), (38, 14)), 'mid', 'f', False, False, 2.4), L(quad((82, 44), (76, 24), (62, 14)), 'mid', 'f', False, False, 2.4),
   L(quad((26, 70), (36, 66), (46, 70)), BLACK, 'f', False, False, 2.4), L(quad((74, 70), (64, 66), (54, 70)), BLACK, 'f', False, False, 2.4),
   L([(54, 99), (55, 106)], _c('#8ab0d8'), 'f', False, False, 1.6)],
  skull3('side') + [M([(52, 10), (52, -6), (64, -10), (74, 0), (66, 14)]), L(quad((20, 44), (34, 20), (52, 12)), 'mid', 'f', False, False, 2.4)],
  skull3('back') + [M([(36, 16), (34, 2), (44, -10), (56, -12), (66, -4), (64, 12), (50, 18)]),
                    L(quad((18, 44), (24, 24), (38, 14)), 'mid', 'f', False, False, 2.4), L(quad((82, 44), (76, 24), (62, 14)), 'mid', 'f', False, False, 2.4)])

# Humphrey Dictable: piel morena; cresta alta lila grisácea con un pompón blanco en la punta y los lados rapados; ojos
# morados entornados con pestañas, boca pequeña en "o" y orejas en aleta
FIN, POM = _c('#e8c8c4'), _c('#f6f8fa')
C('humphrey-dictable', 'normal', P('#937676', '#ae8860', iris='#6a4a9a'),
  F(eyes='sharp', brows=False, mouth='none', hairline=False, ears=False),
  skull('front') if False else [L(blob([(18, 56), (16, 34), (28, 14), (50, 6), (72, 14), (84, 34), (82, 56)], 8), 'skin'),
                                M([(40, 50), (38, 20), (42, -10), (50, -14), (58, -10), (62, 20), (60, 50), (50, 56)]),
                                L(ell(50, -18, 12, 11), POM, 'f'), M([(18, 72), (2, 80), (-4, 74, 1), (4, 68)], FIN), M([(82, 72), (98, 80), (104, 74, 1), (96, 68)], FIN),
                                L(ell(50, 94, 2.6, 3), _c('#5a3428'), 'f', False)],
  skull3('side') + [M([(70, 12), (56, -8), (40, -14), (20, -4), (10, 14), (30, 10), (50, 6)]), L(ell(44, -16, 12, 11), POM, 'f'),
                    M([(50, 72), (34, 82), (30, 72, 1), (40, 66)], FIN)],
  skull3('back') + [M([(40, 70), (38, 20), (42, -10), (50, -14), (58, -10), (62, 20), (60, 70), (50, 74)]), L(ell(50, -18, 12, 11), POM, 'f'),
                    M([(18, 72), (2, 80), (-4, 74, 1), (4, 68)], FIN), M([(82, 72), (98, 80), (104, 74, 1), (96, 68)], FIN)])

# Humphrey Hedrass: gordo moreno con el pelo verde muy oscuro repeinado, un rizo sobre la frente y una melenita de rizos
# por detrás a los lados; gafas de sol de visera oscura y boca pequeña de pucheros
VIS2 = _c('#3a3048')
C('humphrey-hedrass', 'corpulento', P('#3b4b41', '#ce9468', iris='#1e1414'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=97, face_front=face(w=8, chin=106, jaw=5), hairline=[(14, 56), (22, 44), (50, 38), (78, 44), (86, 56)]),
  [L(ell(4, 92, 10, 10), 'mid'), L(ell(96, 92, 10, 10), 'mid'), L(ell(10, 82, 9, 9), 'mid'), L(ell(90, 82, 9, 9), 'mid'),
   M([(20, 52), (20, 24), (34, 10), (50, 6), (66, 10), (80, 24), (80, 52), (70, 42), (30, 42)]),
   M([(40, 40), (44, 30), (52, 34), (48, 46), (54, 52, 1), (44, 48)], 'mid', 'f'),
   M([(16, 70), (50, 66), (84, 70), (80, 80), (56, 80), (50, 76), (44, 80), (20, 80)], VIS2, 'f')],
  [L(ell(30, 90, 11, 10), 'mid'), L(ell(22, 78, 10, 10), 'mid'), M([(40, 44), (40, 18), (56, 6), (78, 10), (88, 26), (84, 42), (62, 38)]),
   M([(68, 70), (92, 68), (92, 80), (70, 80)], VIS2, 'f')],
  [L(ell(12, 90, 11, 10), 'mid'), L(ell(30, 96, 11, 10), 'mid'), L(ell(50, 98, 11, 10), 'mid'), L(ell(70, 96, 11, 10), 'mid'), L(ell(88, 90, 11, 10), 'mid'),
   M([(16, 84), (16, 26), (32, 10), (50, 6), (68, 10), (84, 26), (84, 84), (50, 90)])])

# Hunter Wanabi (portero): gorra militar gris de plato con la cinta negra y una estrella dorada; flequillo negro que le tapa
# el ojo izquierdo; ojo gris y boca recta
MIL, MILB = _c('#c0c3bf'), _c('#3a3634')
def _milcap(view):
    if view == 'front':
        return [M([(2, 34), (12, 14), (50, 2), (88, 14), (98, 34), (86, 42), (50, 40), (14, 42)], MIL, 'f'),
                M([(14, 40), (86, 40), (84, 52), (16, 52)], MILB, 'f'),
                M([(50, 42), (52, 46, 1), (57, 46), (53, 49), (55, 54, 1), (50, 51), (45, 54, 1), (47, 49), (43, 46), (48, 46, 1)], STAR, 'f', False),
                M([(14, 52), (86, 52), (80, 60), (20, 60)], _c('#2a2a2a'), 'f')]
    if view == 'side':
        return [M([(-4, 34), (10, 14), (50, 2), (90, 14), (100, 32), (88, 40), (40, 40)], MIL, 'f'), M([(10, 38), (88, 38), (88, 50), (10, 50)], MILB, 'f'),
                M([(70, 50), (100, 50), (92, 58), (70, 56)], _c('#2a2a2a'), 'f')]
    return [M([(2, 36), (12, 16), (50, 4), (88, 16), (98, 36), (86, 44), (50, 42), (14, 44)], MIL, 'f'), M([(14, 42), (86, 42), (84, 54), (16, 54)], MILB, 'f')]
C('hunter-wanabi', 'normal', P('#2a2424', '#f8c274', iris='#8a8a8a'),
  F(eyes='normal', brows=False, mouth='line', mouth_y=93, hairline=[(10, 66), (16, 56), (50, 56), (84, 56), (90, 66)]),
  [M([(14, 70), (14, 56), (86, 56), (86, 70), (76, 62)]), M([(48, 56), (88, 56), (86, 66), (70, 82, 1), (66, 70), (54, 74, 1), (52, 64)], 'mid', 'f')] + _milcap('front'),
  [M([(56, 56), (88, 54), (90, 64), (78, 68), (64, 64), (54, 74), (30, 78), (12, 70), (10, 52)])] + _milcap('side'),
  [M([(12, 76), (12, 54), (88, 54), (88, 76), (50, 82)])] + _milcap('back'))

# Ian Spike (portero): cara larga morena; pelo gris oscuro en un cepillo alto y plano; gafas de sol redondas marrones y una
# sonrisa enorme de dientes cuadrados
C('ian-spike', 'delgado', P('#5b5653', '#bd8c68', iris='#1e1414'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=98, face_front=face(chin=112, jaw=-1), face_side=face_side(chin=9), hairline=[(14, 50), (20, 40), (50, 36), (80, 40), (86, 50)]),
  [M([(18, 48), (16, 6), (16, -22), (84, -22), (84, 6), (82, 48), (70, 40), (30, 40)]), M([(60, -22), (84, -22), (84, 6), (82, 44), (68, 20)], 'shade', 'b', False),
   L(ell(36, 74, 10, 6), _c('#6a2a1a'), 'f'), L(ell(64, 74, 10, 6), _c('#6a2a1a'), 'f'), L([(46, 73), (54, 73)], BLACK, 'f', False, False, 1.6),
   M([(38, 94), (62, 94), (60, 102), (40, 102)], WHITE, 'f'), L([(44, 94), (44, 102)], OUTC, 'f', False, False, 0.6), L([(50, 94), (50, 102)], OUTC, 'f', False, False, 0.6),
   L([(56, 94), (56, 102)], OUTC, 'f', False, False, 0.6)],
  [M([(56, 48), (60, 38), (82, 36), (84, 4), (84, -22), (20, -22), (14, 6), (8, 36), (12, 58), (30, 64), (46, 58)]), L(ell(84, 74, 6, 6), _c('#6a2a1a'), 'f')],
  [M([(16, 56), (14, 6), (14, -22), (86, -22), (86, 6), (84, 56), (50, 62)])])

# Icarus Damselfly: pelo verde azulado en melenita con dos moños tiesos a los lados de la cabeza, cinta amarilla con una
# pieza dorada en la frente y dos bolas oscuras en las sienes; piel tostada y ojos verde amarillento afilados
YB, DK = _c('#e8c030'), _c('#2c2c28')
C('icarus-damselfly', 'normal', P('#408678', '#f6c076', iris='#a0a040'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=93, hairline=[(10, 72), (16, 60), (50, 56), (84, 60), (90, 72)]),
  bowl3('front', top=6, side=80, fringe=56) +
  [M([(18, 22), (2, 6), (-6, 22, 1), (8, 30)]), M([(82, 22), (98, 6), (106, 22, 1), (92, 30)]),
   L(quad((14, 20), (50, 6), (86, 20)), YB, 'f', False, False, 3), L(ell(26, 48, 11, 10), DK, 'f'), L(ell(74, 48, 11, 10), DK, 'f'),
   M([(42, 44), (50, 36), (58, 44), (54, 54), (50, 60, 1), (46, 54)], YB, 'f')],
  bowl3('side', top=6, nape=86, fringe=56) + [L(ell(66, 46, 9, 10), DK, 'f'), M([(40, 14), (30, -2), (18, 6, 1), (28, 16)])],
  bowl3('back', top=6, nape=86) + [M([(18, 22), (2, 6), (-6, 22, 1), (8, 30)]), M([(82, 22), (98, 6), (106, 22, 1), (92, 30)]),
                                    L(quad((14, 20), (50, 6), (86, 20)), YB, 'f', False, False, 3)])

# Iggy Heade: grandullón con una cabeza calva enorme y alta como un huevo, con un brillo; ojos negros de enfado, nariz
# naranja y labios gruesos de pucheros
C('iggy-heade', 'corpulento', P('#f8c286', '#f8ba78', iris='#1e1414', nose='#d8804a'),
  F(eyes='round', brows='angry', mouth='lips', mouth_w=7, mouth_y=97, face_front=face(w=6, chin=106, jaw=3, top=0), nose=(50, 86, 3.6), big_ears=1, ear_out=4, hairline=False),
  [L(blob([(14, 56), (14, 20), (26, -8), (50, -18), (74, -8), (86, 20), (86, 56)], 8), 'skin'), M([(52, -12), (66, -6), (60, 10), (48, 4)], 'mid', 'b', False)],
  [L(blob([(44, 60), (26, 62), (8, 46), (6, 14), (24, -10), (50, -18), (74, -10), (86, 14), (88, 44), (70, 40), (54, 42)], 8), 'skin')],
  [L(blob([(16, 76), (12, 30), (24, -6), (50, -18), (76, -6), (88, 30), (84, 76), (50, 84)], 8), 'skin'),
   M([(60, -8), (80, 10), (86, 44), (82, 72), (70, 50)], 'skin_d', 'b', False)])

# Incus Squid Quid: pelo celeste con forma de calamar: una punta alta en el centro, aletas a los lados de la cabeza y
# tentáculos largos que le caen por delante de los hombros; un mechón más claro en la frente; ojos castaños y sonrisa
C('incus-squid-quid', 'normal', P('#b4d4ec', '#fbeed4', iris='#8a4a1e', light='#d6f0fb', shade='#8aa4c0'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, hairline=[(10, 66), (18, 50), (34, 42), (50, 54), (66, 42), (82, 50), (90, 66)]),
  [M([(14, 70), (10, 40), (22, 18), (36, 4), (50, -18, 1), (64, 4), (78, 18), (90, 40), (86, 70), (76, 54), (24, 54)]),
   M([(14, 40), (-6, 48), (-12, 62, 1), (12, 60)]), M([(86, 40), (106, 48), (112, 62, 1), (88, 60)]),
   M([(14, 60), (24, 60), (26, 108), (18, 116, 1), (12, 104)], 'mid', 'f'), M([(86, 60), (76, 60), (74, 108), (82, 116, 1), (88, 104)], 'mid', 'f'),
   M([(46, 10), (54, 10), (56, 40), (50, 70, 1), (44, 40)], 'light', 'f')],
  [M([(56, 54), (64, 40), (84, 36), (88, 20), (68, 4), (54, -16, 1), (40, 2), (16, 14), (6, 40), (10, 70), (30, 80), (46, 70)]),
   M([(30, 30), (6, 30), (-4, 44, 1), (20, 46)]), M([(56, 60), (66, 60), (68, 108), (60, 116, 1), (54, 100)], 'mid', 'f')],
  [M([(12, 80), (10, 40), (22, 18), (36, 4), (50, -18, 1), (64, 4), (78, 18), (90, 40), (88, 80), (50, 86)]),
   M([(14, 40), (-6, 48), (-12, 62, 1), (12, 60)]), M([(86, 40), (106, 48), (112, 62, 1), (88, 60)])])

# Indy Iffrent (portero): cara larga pálida y orejas en punta; pelo granate repeinado hacia atrás con una antena enroscada
# arriba y mechones ondulados que le caen a los lados hasta la barbilla; cejas granates arqueadas, ojos cerrados y morritos
C('indy-iffrent', 'delgado', P('#b44b52', '#fdeed4', iris='#1e1414'),
  F(eyes='closed', brows=False, mouth='frown', mouth_y=96, face_front=face(chin=110, jaw=-2), face_side=face_side(chin=8), ears=True, big_ears=2,
    hairline=[(12, 60), (18, 42), (40, 34), (60, 34), (82, 42), (88, 60)]),
  [M([(16, 60), (14, 30), (26, 12), (50, 6), (74, 12), (86, 30), (84, 60), (74, 40), (26, 40)]),
   L(quad((48, 8), (40, -14), (56, -18)), 'mid', 'f', False, False, 2.6),
   M([(14, 52), (6, 72), (12, 88), (8, 104, 1), (18, 92), (22, 68)], 'mid', 'f'), M([(86, 52), (94, 72), (88, 88), (92, 104, 1), (82, 92), (78, 68)], 'mid', 'f'),
   L(quad((26, 62), (34, 52), (44, 60)), 'mid', 'f', False, False, 3.0), L(quad((74, 62), (66, 52), (56, 60)), 'mid', 'f', False, False, 3.0)],
  [M([(56, 52), (62, 40), (84, 34), (86, 20), (66, 6), (40, 4), (16, 14), (6, 40), (10, 64), (20, 92), (14, 104, 1), (30, 92), (40, 70), (50, 62)]),
   L(quad((52, 6), (46, -14), (62, -18)), 'mid', 'f', False, False, 2.6)],
  [M([(12, 76), (10, 30), (24, 10), (50, 6), (76, 10), (90, 30), (88, 76), (90, 100, 1), (76, 90), (50, 84), (24, 90), (10, 100, 1)]),
   L(quad((48, 8), (40, -14), (56, -18)), 'mid', 'f', False, False, 2.6)])

# Indy Rockrolle (portera): pelo amarillo chillón en pinchos de punta revueltos, con dos mechones largos blancos que le caen
# por delante; maquillaje de estrellas negras alrededor de los ojos rojos y labios rojos
PALE = _c('#f6f0c8')
C('indy-rockrolle', 'chica', P('#f2e844', '#f8eac8', iris='#c02a2a', shade='#c0a032'),
  F(eyes='sharp', brows=False, mouth='lips', mouth_w=6, mouth_y=95, hairline=hl(6, 66, 46, 58, jit=3, seed=81)),
  dome('front', top=0, w=50, cy=44, n=9, amp=12, sweep=0.3, sb=72, seed=82) +
  [M([(18, 56), (26, 56), (28, 110, 1), (20, 100)], PALE, 'f'), M([(82, 56), (74, 56), (72, 110, 1), (80, 100)], PALE, 'f'),
   M([(36, 62), (38, 70, 1), (46, 66), (42, 73, 1), (48, 80), (40, 78, 1), (36, 88), (34, 78, 1), (26, 82), (30, 74, 1), (22, 68), (32, 70, 1)], BLACK, 'b', False),
   L([(26, 66), (32, 71)], BLACK, 'f', False, False, 2.2), L([(46, 66), (41, 71)], BLACK, 'f', False, False, 2.2), L([(36, 84), (36, 88)], BLACK, 'f', False, False, 2.2),
   L([(74, 66), (68, 71)], BLACK, 'f', False, False, 2.2), L([(54, 66), (59, 71)], BLACK, 'f', False, False, 2.2), L([(64, 84), (64, 88)], BLACK, 'f', False, False, 2.2)],
  dome('side', top=0, w=50, cy=44, n=9, amp=12, sweep=0.3, nape=90, fr=56, seed=82) + [M([(60, 56), (68, 56), (68, 110, 1), (60, 100)], PALE, 'f')],
  dome('back', top=0, w=50, cy=44, n=9, amp=12, sweep=0.3, nape=92, seed=82))

# Isaac Celise: pelo rojo en una forma enorme de cono invertido, muy ancho arriba y estrecho en las sienes; sombra roja en
# los párpados, ojos gris azulado y boca de disgusto
C('isaac-celise', 'normal', P('#db3c3a', '#fdce8c', iris='#6a8a96', shade='#a83028'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=93, hairline=[(14, 58), (20, 50), (50, 52), (80, 50), (86, 58)]),
  [M([(18, 58), (6, 30), (-14, -14, 1), (20, -10), (50, -6), (80, -10), (114, -14, 1), (94, 30), (82, 58), (70, 50), (30, 50)]),
   L(quad((30, 50), (20, 20), (4, -10)), 'shade', 'b', False, False, 1.4), L(quad((50, 50), (50, 20), (50, -6)), 'shade', 'b', False, False, 1.4),
   L(quad((70, 50), (80, 20), (96, -10)), 'shade', 'b', False, False, 1.4),
   L(quad((24, 70), (34, 64), (46, 70)), _c('#c82a2a'), 'f', False, False, 2.6), L(quad((76, 70), (66, 64), (54, 70)), _c('#c82a2a'), 'f', False, False, 2.6)],
  [M([(58, 54), (68, 40), (90, 14), (100, -12, 1), (60, -6), (20, -10), (-6, -14, 1), (10, 20), (14, 54), (32, 62), (48, 60)])],
  [M([(18, 62), (6, 30), (-14, -14, 1), (20, -10), (50, -6), (80, -10), (114, -14, 1), (94, 30), (82, 62), (50, 66)])])

# Ivor Colonel Kernel: gorra de plato negra con un botón dorado delante; pelo verde azulado muy oscuro en pinchos que asoma
# por los lados y un flequillo que le tapa el ojo izquierdo; un ojo redondo con aro blanco y boca de disgusto
CAPK, BTN = _c('#121212'), _c('#b8902a')
def _offcap(view):
    if view == 'front':
        return [M([(0, 30), (14, 8), (50, -2), (86, 8), (100, 30), (88, 40), (50, 38), (12, 40)], CAPK, 'f'), M([(16, 38), (84, 38), (82, 50), (18, 50)], CAPK, 'f'),
                L(ell(50, 40, 6, 5), BTN, 'f'), M([(16, 48), (84, 48), (78, 58), (22, 58)], _c('#2a2a2a'), 'f')]
    if view == 'side':
        return [M([(-6, 30), (10, 8), (50, -2), (90, 8), (100, 28), (88, 38), (40, 38)], CAPK, 'f'), M([(12, 36), (88, 36), (88, 48), (12, 48)], CAPK, 'f'),
                M([(70, 48), (102, 48), (94, 56), (70, 54)], _c('#2a2a2a'), 'f')]
    return [M([(0, 32), (14, 10), (50, 0), (86, 10), (100, 32), (88, 42), (50, 40), (12, 42)], CAPK, 'f'), M([(16, 40), (84, 40), (82, 52), (18, 52)], CAPK, 'f')]
C('ivor-colonel-kernel', 'normal', P('#1e3436', '#eec494', iris='#1e1414'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=93, hairline=[(10, 66), (16, 56), (50, 56), (84, 56), (90, 66)]),
  [M([(10, 74), (0, 66, 1), (12, 58), (10, 50), (90, 50), (88, 58), (100, 66, 1), (90, 74), (80, 60), (20, 60)]),
   M([(18, 54), (54, 54), (50, 68), (40, 84, 1), (36, 70), (22, 80, 1), (24, 66)], 'mid', 'f')] + _offcap('front'),
  [M([(56, 54), (86, 52), (90, 62), (78, 66), (66, 62), (54, 76), (40, 72), (26, 84, 1), (24, 70), (6, 72, 1), (10, 50)])] + _offcap('side'),
  [M([(10, 78), (0, 70, 1), (10, 52), (90, 52), (100, 70, 1), (90, 78), (70, 84, 1), (50, 78), (30, 84, 1)])] + _offcap('back'))
