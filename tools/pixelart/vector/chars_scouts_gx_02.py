"""Ojeadores de GX (scouts-gx), tanda 02: dibujados a partir de su retrato de Victory Road; claves 'scouts-gx:<id>'.

En Galaxy muchos ojeadores son alienígenas o llevan máscara: la piel ('skin') es el color de la máscara o de la cabeza
del bicho, la cara tiene la forma de esa cabeza (face_front/face_side) y los ojos, picos y bocas van como capas de
delante. Los que tienen modelo 3D del mismo personaje (Fuyukai, Mizukawa, Minel Ava, Senguuji, Haniwaa, Tiger T,
Manabe, Kanda) usan su perfil y su espalda."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal  # noqa: F401
from chars_scouts_ie1_09 import dome, face, face_side, hl  # noqa: F401
from chars_scouts_ie2_03 import ears_pointy, round_glasses  # noqa: F401
from heads import quad  # noqa: F401

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
    CHARS[f'scouts-gx:{pid}'] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def M(pts, c='mid', z='b', sil=True, ln=False):
    return L(outline(pts), c, z, sil, ln)


def B(pts, c, z='f', k=6):
    """Mancha rellena suave (sin contorno propio)."""
    return L(blob(pts, k), c, z, False)


def ln(pts, c=OUTC, w=1.4):
    return L(pts, c, 'f', False, False, w)


def mx(pts):
    return [(100 - p[0],) + tuple(p[1:]) for p in pts]


def both(pts, c='mid', z='b', sil=True):
    return [M(pts, c, z, sil), M(mx(pts), c, z, sil)]


def eye(cx, cy, rx, ry, white=WHITE, iris=None, ir=0.6, out=True):
    """Ojo de bicho: óvalo blanco (o del color white) con contorno y pupila."""
    o = [L(ell(cx, cy, rx + 1.2, ry + 1.2), OUTC, 'f', False)] if out else []
    o.append(L(ell(cx, cy, rx, ry), white, 'f', False))
    if iris:
        o.append(L(ell(cx, cy, rx * ir, ry * ir), iris, 'f', False))
    return o


def eyes2(ey=75, sep=14, rx=5, ry=6, white=WHITE, iris=None, ir=0.6, out=True):
    return eye(50 - sep, ey, rx, ry, white, iris, ir, out) + eye(50 + sep, ey, rx, ry, white, iris, ir, out)


def holes(ey=76, sep=15, c=BLACK, iris=WHITE, w=10, h=7, tilt=3):
    """Agujeros de máscara en almendra enfadada con el ojo blanco dentro."""
    o = []
    for cx, s in ((50 - sep, 1), (50 + sep, -1)):
        pts = [(cx - w * s, ey - h + tilt * 0 - 1), (cx + w * 0.8 * s, ey - h * 0.2 + tilt), (cx + w * 0.6 * s, ey + h * 0.8), (cx - w * 0.7 * s, ey + h * 0.6)]
        o += [L(blob(pts, 5), c, 'f', False), L(ell(cx + s * 1.5, ey + 1.5, w * 0.38, h * 0.42), iris, 'f', False)]
    return o


def hole_side(ey=76, c=BLACK, iris=WHITE):
    return [L(blob([(72, ey - 6), (88, ey - 2), (87, ey + 5), (74, ey + 4)], 5), c, 'f', False), L(ell(82, ey + 1, 3, 3.2), iris, 'f', False)]


def mouth(y=94, kind='frown', w=6, c=OUTC):
    if kind == 'frown':
        return [ln(quad((50 - w, y + 2), (50, y - 2), (50 + w, y + 2)), c)]
    if kind == 'smile':
        return [ln(quad((50 - w, y - 1), (50, y + 3), (50 + w, y - 1)), c)]
    if kind == 'grin':
        pts = [(50 - w, y - 2), (50 + w, y - 2), (50 + w * 0.8, y + 4), (50 - w * 0.8, y + 4)]
        return [L(pts, WHITE, 'f', False, True), ln([(50 - w, y + 1), (50 + w, y + 1)], OUTC, 0.8)]
    if kind == 'o':
        return [L(ell(50, y, w * 0.5, w * 0.6), OUTC, 'f', False)]
    return [ln([(50 - w, y), (50 + w, y)], c)]


def beak(y=82, w=6, h=12, c=None, tip=None):
    """Pico de frente: triángulo hacia abajo."""
    c = c or _c('#e8c040')
    return [L(outline([(50 - w, y), (50 + w, y), (50, y + h, 1)]), c, 'f', False, True)]


def beak_side(y=82, l=10, h=8, c=None):
    c = c or _c('#e8c040')
    return [L(outline([(84, y - h / 2), (86 + l, y + 1, 1), (84, y + h / 2)]), c, 'f', False, True)]


def horn(x, y, tx, ty, c, w=6):
    return M([(x - w, y + 4), (tx, ty, 1), (x + w, y + 2)], c, 'f')


def glasses_rect(view, c=BLACK, y=76, sep=14, w=9, h=6):
    if view == 'front':
        o = []
        for cx in (50 - sep, 50 + sep):
            o.append(ln([(cx - w, y - h), (cx + w, y - h), (cx + w - 1, y + h), (cx - w + 1, y + h), (cx - w, y - h)], c, 1.8))
        return o + [ln([(50 - sep + w, y - 2), (50 + sep - w, y - 2)], c, 1.4)]
    return [ln([(76, y - h), (88, y - h), (88, y + h), (77, y + h), (76, y - h)], c, 1.8), ln([(76, y - 2), (50, y - 6)], c, 1.4)]


ROUND = [(14, 64), (16, 34), (30, 14), (50, 8), (70, 14), (84, 34), (86, 64), (84, 90), (68, 104), (50, 106), (32, 104), (16, 90)]
ROUND_S = [(46, 14), (70, 16), (86, 34), (90, 60), (88, 86), (76, 102), (56, 104), (40, 98), (22, 84), (12, 58), (18, 30)]


def head_round(front=ROUND, side=ROUND_S):
    return {'face_front': blob(front, 6), 'face_side': blob(side, 6)}


# ------------------------------------------------------------------ jugadores

# Feriando Hidery: casco-máscara naranja rojizo que le tapa toda la cabeza, con dos cuernos cortos en punta arriba, un
# mechón morado en el centro, manchas claras en la frente y el hocico blanco con la boca de dientes apretados; ojos
# blancos en agujeros negros enfadados
OR1, OR1D, PU1 = _c('#c97251'), _c('#9b4d3a'), _c('#7a6a84')
def _helmet(view, horns=True):
    if view == 'front':
        o = [M([(12, 100), (10, 60), (14, 30), (30, 10), (50, 4), (70, 10), (86, 30), (90, 60), (88, 100), (70, 108), (50, 110), (30, 108)], 'skin')]
        if horns:
            o += [horn(24, 14, 18, -14, 'skin'), horn(76, 14, 82, -14, 'skin')]
        return o
    if view == 'side':
        o = [M([(8, 96), (4, 60), (10, 30), (30, 10), (56, 6), (78, 16), (90, 36), (94, 62), (92, 90), (80, 106), (50, 108), (24, 104)], 'skin')]
        if horns:
            o += [horn(50, 10, 46, -16, 'skin')]
        return o
    o = [M([(12, 100), (10, 60), (14, 30), (30, 10), (50, 4), (70, 10), (86, 30), (90, 60), (88, 100), (50, 106)], 'skin')]
    if horns:
        o += [horn(24, 14, 18, -14, 'skin'), horn(76, 14, 82, -14, 'skin')]
    return o
C('feriando-hidery', 'normal', P('#7a6a84', '#c97251', skin_d='#a85a40'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True),
  _helmet('front') + [B([(30, 30), (40, 24), (44, 44), (34, 48)], _c('#e8a888')), B([(70, 30), (60, 24), (56, 44), (66, 48)], _c('#e8a888')),
                      M([(44, 34), (46, 10), (54, 0), (58, 12), (56, 34)], PU1, 'f'),
                      B([(34, 82), (50, 70), (66, 82), (64, 102), (50, 108), (36, 102)], WHITE)] + holes(74, 16) + mouth(94, 'grin', 7),
  _helmet('side') + [M([(48, 30), (52, 6), (62, -2), (64, 12), (60, 32)], PU1, 'f'),
                     B([(74, 80), (90, 74), (94, 92), (84, 104), (72, 100)], WHITE)] + hole_side(74) + [ln([(80, 94), (90, 93)], OUTC, 1.4)],
  _helmet('back') + [M([(44, 30), (46, 8), (54, -2), (58, 10), (56, 30)], PU1, 'f'), B([(58, 8), (84, 30), (88, 96), (66, 100)], 'skin_d', 'f')])

# Flint Heutch: cabeza de bicho redonda y lisa, marrón, con un rombo crema en la frente y el hocico crema ancho con una
# sonrisa de dientes torcida; ojos afilados enfadados
BR2, CR2 = _c('#ae8860'), _c('#eae1d0')
C('flint-heutch', 'normal', P('#ae8860', '#ae8860', iris='#302020', skin_d='#8a6a48'),
  F(eyes='sharp', brows='angry', mouth='none', hairline=False, ears=False, eye_y=72,
    face_front=blob([(14, 66), (14, 36), (28, 16), (50, 8), (72, 16), (86, 36), (86, 66), (84, 92), (66, 106), (50, 108), (34, 106), (16, 92)], 6),
    face_side=blob([(40, 10), (66, 12), (84, 30), (92, 56), (94, 84), (82, 102), (60, 106), (40, 98), (20, 82), (12, 56), (18, 26)], 6)),
  [B([(44, 30), (50, 16), (56, 30), (50, 44)], CR2), B([(22, 86), (36, 82), (50, 86), (64, 82), (78, 86), (74, 102), (50, 110), (26, 102)], CR2),
   L([(36, 92), (64, 90), (60, 96), (40, 97)], WHITE, 'f', False, True), ln([(38, 94), (62, 93)], OUTC, 0.8)],
  [B([(70, 84), (90, 80), (94, 94), (84, 104), (68, 100)], CR2), ln([(80, 94), (92, 92)], OUTC, 1.4)],
  [M([(14, 90), (12, 50), (24, 20), (50, 8), (76, 20), (88, 50), (86, 90), (50, 100)], 'skin'), B([(60, 14), (82, 30), (86, 86), (64, 96)], 'skin_d', 'f')])

# Foggara Kanart: el mismo casco-máscara naranja de su tribu, con un rombo crema en la frente y un penacho gris verdoso
# largo que sale de arriba y le cae por el lado derecho hasta el hombro; ojos azulados en agujeros negros, hocico crema
TEAL3 = _c('#a0bab5')
def _plume(view):
    if view == 'front':
        return [M([(58, 10), (66, -16), (78, -10), (84, 20), (90, 60), (94, 96), (86, 104), (82, 70), (74, 30)], TEAL3, 'f'),
                ln([(72, -6), (82, 40), (88, 90)], _c('#787672'), 1.2)]
    if view == 'side':
        return [M([(30, 8), (36, -18), (50, -12), (40, 10), (24, 40), (10, 80), (6, 104), (0, 96), (6, 60), (16, 26)], TEAL3, 'f')]
    return [M([(42, 8), (34, -16), (22, -10), (16, 20), (10, 60), (6, 96), (14, 104), (18, 70), (26, 30)], TEAL3, 'f')]
C('foggara-kanart', 'normal', P('#a0bab5', '#cb7250', skin_d='#a85a40'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True),
  _helmet('front', False) + _plume('front') + [B([(40, 30), (50, 18), (60, 30), (50, 44)], CR2), B([(26, 26), (36, 20), (40, 34), (30, 38)], _c('#e8a888')),
                                              B([(36, 84), (50, 74), (64, 84), (62, 102), (50, 108), (38, 102)], CR2)] +
  holes(74, 16, iris=_c('#c0c8e8')) + mouth(96, 'line', 4),
  _helmet('side', False) + _plume('side') + [B([(74, 82), (90, 76), (94, 92), (84, 104), (72, 100)], CR2)] + hole_side(74, iris=_c('#c0c8e8')),
  _helmet('back', False) + _plume('back') + [B([(58, 8), (84, 30), (88, 96), (66, 100)], 'skin_d', 'f')])

# Frank Wintersea (Fuyukai Suguru, profesor): pelo castaño claro entrecano peinado hacia arriba con un rizo alto a la
# derecha, entradas, gafas de pasta oscuras rectangulares, ojos caídos, perilla de barba de tres días; cara larga
C('frank-wintersea', 'delgado', P('#ab9679', '#f8bc7f', iris='#3a2a20', shade='#82624b'),
  F(eyes='closed', brows=True, mouth='smile', mouth_y=97, face_front=face(chin=106), face_side=face_side(chin=6, nose=3), nose=(50, 88, 2.6),
    hairline=[(8, 62), (16, 48), (24, 40), (40, 42), (50, 44), (62, 40), (78, 38), (86, 46), (92, 62)]),
  [M([(14, 62), (12, 34), (24, 12), (44, 6), (60, 4), (70, -10), (84, -14, 1), (82, 2), (90, 20), (88, 62), (80, 46), (20, 46)]),
   M([(62, 2), (72, -10), (84, -14), (82, 2), (90, 22), (86, 46), (74, 24)], 'shade', 'b', False)] + glasses_rect('front', _c('#2a2420')) +
  [ln([(40, 102), (44, 104)], _c('#82624b'), 1), ln([(56, 104), (60, 102)], _c('#82624b'), 1)],
  [M([(54, 56), (60, 42), (80, 36), (86, 20), (80, 6), (66, -4), (74, -14, 1), (56, -6), (36, -2), (16, 10), (6, 32), (8, 58), (22, 70), (40, 66)]),
   M([(8, 36), (30, 40), (44, 56), (36, 66), (20, 66)], 'shade', 'b', False)] + glasses_rect('side', _c('#2a2420')),
  [M([(14, 72), (10, 34), (24, 10), (50, 2), (66, -2), (78, -12, 1), (78, 6), (90, 30), (86, 72), (50, 80)]),
   M([(60, 4), (80, 14), (90, 36), (86, 70), (66, 72)], 'shade', 'b', False)])

# Gabriel Aitor Aitriel (Kiriya): melena lila revuelta de mechones finos que le cae por los lados hasta el cuello y un
# flequillo de mechones por la frente; piel morena clara, ojos verde azulado grandes
C('gabriel-aitor-aitriel', 'normal', P('#ad9ab0', '#e9b786', iris='#2a9aa0', shade='#836a73'),
  F(eyes='big', brows=False, mouth='line', mouth_y=93, hairline=hl(6, 70, 50, 62, jit=3, seed=21)),
  dome('front', top=2, w=48, cy=46, n=12, amp=6, seed=21, long=98, flare=6),
  dome('side', top=2, w=48, cy=46, n=12, amp=6, seed=21, long=98, fr=52),
  dome('back', top=2, w=48, cy=46, n=12, amp=6, seed=21, long=100, ends=5))

# Galiaf Satonga: piel verde menta pálida, pelo amarillo en pinchos enormes hacia arriba y patillas amarillas que le
# bajan por las mejillas hasta la barbilla como una barba; cejas amarillas gruesas enfadadas, ojos rojos y boca seria
YE6, YE6D = _c('#edea6c'), _c('#bb984d')
C('galiaf-satonga', 'normal', P('#edea6c', '#cde7e0', iris='#c02838', shade='#bb984d'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=95, face_front=face(chin=104, jaw=2), ears=False,
    hairline=[(8, 64), (18, 52), (30, 54), (40, 46), (50, 50), (60, 46), (72, 54), (82, 52), (92, 64)]),
  [M([(14, 70), (8, 40), (0, 12, 1), (20, 22), (18, -10, 1), (34, 8), (44, -34, 1), (54, 4), (64, -14, 1), (70, 10), (86, -6, 1), (84, 24), (100, 14, 1), (92, 40),
      (86, 70), (80, 52), (20, 52)]),
   M([(56, 0), (64, -14), (70, 10), (86, -6), (84, 24), (98, 16), (90, 44), (86, 66), (74, 30)], 'shade', 'b', False),
   M([(17, 60), (24, 60), (28, 88), (40, 102), (30, 104), (18, 92)], YE6, 'f'), M([(83, 60), (76, 60), (72, 88), (60, 102), (70, 104), (82, 92)], YE6, 'f'),
   M([(24, 66), (46, 70), (44, 74), (24, 72)], YE6, 'f'), M([(76, 66), (54, 70), (56, 74), (76, 72)], YE6, 'f')],
  [M([(54, 60), (60, 44), (80, 40), (96, 24, 1), (82, 18), (90, -8, 1), (70, 4), (60, -30, 1), (46, -2), (26, -14, 1), (24, 10), (4, 6, 1), (8, 34), (6, 60), (22, 72),
      (40, 70)]),
   M([(60, 62), (66, 62), (72, 90), (82, 102), (70, 104), (62, 86)], YE6, 'f'), M([(68, 66), (86, 70), (86, 74), (68, 72)], YE6, 'f')],
  [M([(14, 76), (8, 40), (0, 12, 1), (20, 22), (18, -10, 1), (34, 8), (44, -34, 1), (54, 4), (64, -14, 1), (70, 10), (86, -6, 1), (84, 24), (100, 14, 1), (92, 40),
      (86, 76), (50, 82)]),
   M([(56, 0), (64, -14), (70, 10), (86, -6), (84, 24), (98, 16), (90, 44), (86, 74), (66, 60)], 'shade', 'b', False)])

# Gengo Rowe (portero): melena lisa gris azulado oscura hasta los hombros con el flequillo recto y el pelo de arriba más
# claro, mechones granates por debajo a los lados; piel verde menta pálida, ojos azules enfadados
GY7, MR7 = _c('#a4b1b5'), _c('#a83a4a')
C('gengo-rowe', 'normal', P('#636f7f', '#cbe8e3', iris='#2a7ac8', shade='#4e5a6a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(8, 66), (16, 58), (30, 58), (50, 58), (70, 58), (84, 58), (92, 66)]),
  [M([(16, 106), (6, 70), (8, 34), (24, 10), (50, 2), (76, 10), (92, 34), (94, 70), (84, 106), (80, 60), (20, 60)]),
   M([(18, 30), (30, 14), (50, 8), (70, 14), (82, 30), (70, 26), (50, 24), (30, 26)], GY7, 'b', False),
   M([(12, 76), (16, 74), (22, 104), (14, 112, 1)], MR7, 'f'), M([(88, 76), (84, 74), (78, 104), (86, 112, 1)], MR7, 'f')],
  [M([(56, 58), (64, 46), (82, 44), (88, 26), (70, 6), (44, 0), (20, 10), (6, 34), (4, 70), (10, 100), (24, 108), (36, 100), (44, 84), (50, 68)]),
   M([(24, 14), (46, 6), (70, 10), (80, 22), (60, 22), (36, 24)], GY7, 'b', False), M([(30, 80), (36, 80), (34, 104), (28, 108, 1)], MR7, 'f')],
  [M([(10, 106), (6, 70), (8, 34), (24, 10), (50, 2), (76, 10), (92, 34), (94, 70), (90, 106), (50, 110)]),
   M([(18, 30), (30, 14), (50, 8), (70, 14), (82, 30), (70, 26), (50, 24), (30, 26)], GY7, 'f', False),
   M([(14, 84), (20, 84), (20, 106), (12, 108, 1)], MR7, 'f'), M([(86, 84), (80, 84), (80, 106), (88, 108, 1)], MR7, 'f')])

# Geoff Nory: cabeza de casco negro con una cresta en punta y una franja gris en diagonal; la cara es una placa gris con
# los ojos amarillos de pupila negra; un pañuelo rosa crema enrollado al cuello que sube por detrás en dos tiras curvas
# como cuernos
BK8, GY8, PK8 = _c('#232926'), _c('#aaa6a6'), _c('#e6d6c8')
def _wrap(view):
    if view == 'front':
        return [M([(10, 70), (2, 30), (8, -6), (16, -14, 1), (16, 10), (18, 40), (24, 70)], PK8, 'b'), M([(90, 70), (98, 30), (92, -6), (84, -14, 1), (84, 10), (82, 40), (76, 70)], PK8, 'b'),
                M([(8, 96), (30, 92), (50, 98), (70, 92), (92, 96), (94, 108), (50, 112), (6, 108)], PK8, 'f')]
    if view == 'side':
        return [M([(20, 70), (6, 36), (4, -4), (10, -12, 1), (16, 20), (30, 60)], PK8, 'b'), M([(20, 96), (60, 92), (84, 98), (84, 110), (40, 112), (16, 108)], PK8, 'f')]
    return [M([(10, 70), (2, 30), (8, -6), (16, -14, 1), (16, 10), (18, 40), (24, 70)], PK8, 'f'), M([(90, 70), (98, 30), (92, -6), (84, -14, 1), (84, 10), (82, 40), (76, 70)], PK8, 'f'),
            M([(8, 96), (30, 92), (50, 98), (70, 92), (92, 96), (94, 108), (50, 112), (6, 108)], PK8, 'f')]
C('geoff-nory', 'normal', P('#232926', '#aaa6a6', skin_d='#88847f'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False,
    face_front=blob([(22, 66), (50, 58), (78, 66), (76, 90), (62, 104), (50, 106), (38, 104), (24, 90)], 6)),
  _wrap('front') + [M([(14, 86), (12, 50), (18, 24), (36, 6), (50, -16, 1), (64, 6), (82, 24), (88, 50), (86, 86), (78, 66), (50, 58), (22, 66)], BK8, 'f'),
                    M([(56, 6), (66, 10), (40, 60), (30, 56)], _c('#6a6866'), 'f', False)] +
  [L(blob([(26, 70), (44, 74), (42, 82), (28, 80)], 4), _c('#e8b830'), 'f', False, True), L(blob([(74, 70), (56, 74), (58, 82), (72, 80)], 4), _c('#e8b830'), 'f', False, True),
   L(ell(36, 77, 2, 2.6), OUTC, 'f', False), L(ell(64, 77, 2, 2.6), OUTC, 'f', False)] + mouth(96, 'line', 4),
  _wrap('side') + [M([(8, 70), (6, 40), (20, 14), (46, 0), (52, -18, 1), (70, 8), (86, 28), (90, 56), (80, 62), (62, 60), (50, 86), (30, 94), (12, 86)], BK8, 'f'),
                   M([(56, 4), (66, 10), (44, 58), (36, 54)], _c('#6a6866'), 'f', False),
                   L(blob([(74, 70), (88, 70), (88, 80), (76, 80)], 4), _c('#e8b830'), 'f', False, True), L(ell(83, 75, 1.8, 2.6), OUTC, 'f', False)],
  [M([(12, 96), (10, 50), (18, 24), (36, 6), (50, -16, 1), (64, 6), (82, 24), (90, 50), (88, 96), (50, 102)], BK8, 'b'),
   M([(56, 6), (66, 10), (40, 70), (30, 66)], _c('#6a6866'), 'b', False)] + _wrap('back'))

# Gieve Tik Gievetik: pelo azul como una medusa, en una masa redonda que le cae hasta la barbilla y le tapa el ojo
# derecho, con manchas moradas y flecos rosados por debajo, y un ojillo negro en lo alto; ojo verde amarillento
BL9, PU9, PK9 = _c('#74a4c3'), _c('#5e5e8a'), _c('#e8a8b8')
C('gieve-tik-gievetik', 'normal', P('#74a4c3', '#fad8b1', iris='#9ab830', shade='#5a86a8'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=94, hairline=[(8, 74), (14, 60), (30, 50), (50, 50), (64, 54), (80, 58), (92, 70)]),
  [M([(10, 96), (4, 60), (8, 28), (26, 8), (50, 2), (76, 8), (92, 28), (96, 60), (92, 92), (80, 90), (82, 60), (66, 56), (56, 66), (50, 90), (40, 96)]),
   M([(56, 4), (78, 10), (94, 30), (96, 60), (90, 88), (82, 84), (82, 58), (72, 28)], 'shade', 'b', False),
   B([(16, 70), (26, 66), (28, 80), (18, 82)], PU9), B([(84, 64), (92, 66), (90, 78), (84, 76)], PU9), B([(60, 20), (70, 18), (72, 30), (62, 30)], PU9),
   M([(10, 96), (4, 60), (8, 34), (26, 40), (44, 46), (54, 54), (54, 76), (50, 90), (40, 96), (26, 100)], 'mid', 'f'),
   B([(18, 70), (28, 66), (30, 80), (20, 82)], PU9),
   B([(16, 96), (30, 98), (40, 94), (36, 102), (22, 104)], PK9), L(ell(66, 10, 3, 2.4), OUTC, 'f', False)],
  [M([(54, 66), (64, 56), (82, 52), (88, 30), (72, 8), (46, 2), (22, 10), (6, 32), (4, 64), (12, 92), (30, 100), (44, 92), (50, 78)]),
   M([(8, 36), (30, 40), (46, 60), (40, 90), (26, 96), (10, 86)], 'shade', 'b', False), B([(20, 60), (32, 58), (34, 72), (22, 72)], PU9),
   B([(14, 94), (30, 98), (40, 92), (34, 102)], PK9), L(ell(50, 6, 3, 2.4), OUTC, 'f', False)],
  [M([(8, 100), (4, 60), (8, 28), (26, 8), (50, 2), (76, 8), (92, 28), (96, 60), (92, 100), (50, 104)]),
   M([(58, 6), (80, 14), (94, 36), (94, 96), (70, 100)], 'shade', 'b', False), B([(20, 50), (32, 48), (34, 62), (22, 62)], PU9),
   B([(70, 70), (82, 68), (84, 80), (72, 82)], PU9), B([(14, 100), (40, 104), (60, 104), (86, 100), (80, 108), (20, 108)], PK9)])

# Glacia Vessal (Mizukawa Minori): melena lisa verde azulado oscuro muy larga, con la raya a un lado y el flequillo
# echado; piel clara y ojos turquesa serios
C('glacia-vessal', 'chica', P('#1b4f57', '#fcf0d6', iris='#2a9aa0', shade='#173c43'),
  F(eyes='sharp', brows=True, mouth='line', mouth_y=93, hairline=[(8, 74), (16, 56), (28, 46), (40, 50), (52, 42), (66, 46), (80, 54), (92, 72)]),
  [M([(16, 118), (6, 80), (6, 40), (20, 14), (40, 4), (62, 4), (82, 14), (94, 40), (94, 80), (86, 118), (80, 70), (20, 70)]),
   M([(58, 6), (80, 16), (92, 40), (92, 80), (86, 114), (82, 70), (76, 34)], 'shade', 'b', False)] + [L([(30, 70), (24, 92)], 'shade', 'f', False, False, 1)],
  [M([(56, 56), (62, 44), (82, 42), (88, 24), (70, 4), (44, -2), (20, 8), (4, 32), (2, 70), (6, 110), (20, 120), (36, 112), (44, 90), (50, 70)]),
   M([(6, 36), (26, 40), (42, 64), (34, 110), (16, 114), (6, 90)], 'shade', 'b', False)],
  [M([(8, 120), (4, 80), (6, 40), (20, 12), (50, 2), (80, 12), (94, 40), (96, 80), (92, 120), (50, 124)]),
   M([(58, 6), (80, 14), (94, 40), (94, 116), (70, 120)], 'shade', 'b', False)])

# Globulus Ava (Minel Ava): piel morena, pelo verde grisáceo peinado hacia atrás con un pico en la frente, orejas de
# punta enormes hacia arriba y hacia fuera, dos mechones a los lados enroscados hacia arriba como tentáculos y una coleta
# larga por detrás; ojos de párpado caído
GR11, GR11D = _c('#698875'), _c('#4e6a5a')
C('globulus-ava', 'normal', P('#698875', '#ad8861', iris='#3a6a3a', shade='#4e6a5a', skin_d='#845a41'),
  F(eyes='closed', brows='angry', mouth='frown', mouth_y=95, face_front=face(chin=104, jaw=1), ears=False,
    hairline=[(8, 62), (18, 52), (30, 48), (42, 40), (50, 54), (58, 40), (70, 48), (82, 52), (92, 62)]),
  [M([(16, 70), (8, 82), (-6, 74, 1), (4, 64), (14, 60)]), M([(84, 70), (92, 82), (106, 74, 1), (96, 64), (86, 60)]),
   M([(18, 62), (4, 40), (-8, 22, 1), (12, 34), (22, 52)], 'skin', 'b'), M([(82, 62), (96, 40), (108, 22, 1), (88, 34), (78, 52)], 'skin', 'b'),
   M([(18, 60), (14, 30), (28, 10), (50, 4), (72, 10), (86, 30), (82, 60), (70, 46), (30, 46)]),
   M([(44, 8), (50, -4, 1), (56, 8), (52, 46), (48, 46)], GR11D, 'b', False)],
  [M([(54, 60), (62, 46), (80, 40), (86, 24), (70, 6), (44, 0), (20, 8), (6, 30), (6, 60), (14, 86), (10, 110), (20, 114), (24, 88), (30, 70), (44, 66)]),
   M([(44, 62), (34, 34), (30, 16, 1), (46, 36), (54, 58)], 'skin', 'f'), M([(26, 74), (12, 80), (2, 70, 1), (14, 66)])],
  [M([(16, 70), (10, 30), (26, 8), (50, 2), (74, 8), (90, 30), (84, 70), (58, 76), (56, 110), (50, 116), (44, 110), (42, 76)]),
   M([(18, 62), (4, 40), (-8, 22, 1), (12, 34), (22, 52)], 'skin', 'b'), M([(82, 62), (96, 40), (108, 22, 1), (88, 34), (78, 52)], 'skin', 'b'),
   M([(16, 74), (8, 84), (-6, 76, 1), (6, 66)]), M([(84, 74), (92, 84), (106, 76, 1), (94, 66)])])

# Golgi Tai: melena blanca crema enorme y salvaje de mechones largos que le caen por los lados; piel naranja, orejas de
# punta, pintura roja alrededor de los ojos con rayas blancas por encima; ojos turquesa enfadados
CR12, RD12 = _c('#fefdd6'), _c('#c82a2a')
C('golgi-tai', 'normal', P('#fefdd6', '#fabc7e', iris='#2a9a9a', shade='#d8d6bc'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=95, hairline=hl(5, 64, 42, 50, jit=3, seed=31)),
  ears_pointy('front', h=14) +
  [M([(14, 104), (0, 70), (-6, 30, 1), (8, 34), (6, 6, 1), (24, 14), (30, -10, 1), (44, 4), (56, -14, 1), (64, 6), (82, -6, 1), (80, 16), (98, 8, 1), (94, 36),
      (106, 64, 1), (96, 70), (90, 104), (82, 66), (18, 66)]),
   M([(62, 4), (82, -6), (80, 16), (98, 8), (94, 36), (104, 62), (92, 100), (80, 50)], 'shade', 'b', False),
   B([(24, 70), (44, 72), (44, 84), (26, 84)], RD12), B([(76, 70), (56, 72), (56, 84), (74, 84)], RD12),
   ln([(28, 66), (40, 58)], WHITE, 1.6), ln([(72, 66), (60, 58)], WHITE, 1.6)] +
  [L([(28, 74), (44, 76), (42, 81), (30, 80)], WHITE, 'f', False), L(ell(37, 78, 2.6, 3), _c('#2a9a9a'), 'f', False), ln([(26, 72), (44, 76)], OUTC, 2.6),
   L([(72, 74), (56, 76), (58, 81), (70, 80)], WHITE, 'f', False), L(ell(63, 78, 2.6, 3), _c('#2a9a9a'), 'f', False), ln([(74, 72), (56, 76)], OUTC, 2.6)],
  [M([(54, 60), (62, 46), (82, 40), (98, 30, 1), (84, 20), (92, -2, 1), (70, 6), (62, -16, 1), (46, 0), (26, -10, 1), (22, 10), (2, 6, 1), (8, 34), (-4, 60, 1), (6, 70),
      (0, 100, 1), (16, 96), (22, 110, 1), (32, 92), (44, 70)])] + ears_pointy('side', h=14) +
  [B([(70, 70), (88, 70), (88, 84), (72, 84)], RD12), L([(74, 74), (86, 75), (85, 81), (76, 80)], WHITE, 'f', False), L(ell(82, 78, 2.4, 3), _c('#2a9a9a'), 'f', False),
   ln([(72, 72), (86, 75)], OUTC, 2.6)],
  [M([(10, 106), (0, 70), (-6, 30, 1), (8, 34), (6, 6, 1), (24, 14), (30, -10, 1), (44, 4), (56, -14, 1), (64, 6), (82, -6, 1), (80, 16), (98, 8, 1), (94, 36), (106, 64, 1),
      (96, 70), (92, 106), (70, 100, 1), (60, 110), (50, 100, 1), (40, 110), (30, 100, 1)]),
   M([(62, 4), (82, -6), (80, 16), (98, 8), (94, 36), (104, 62), (92, 104), (70, 98)], 'shade', 'b', False)])

# Gomara Raccamere: cabeza de casco negro con dos cuernos dorados curvos, los ojos amarillos grandes y una placa gris en
# la boca; le cuelgan dos brazos verdes de mantis con pinchos por delante del pecho
BK13, GO13, GN13 = _c('#2a2b2b'), _c('#d8a83a'), _c('#5a8a2a')
def _gomara(view):
    if view == 'front':
        return [M([(26, 80), (20, 112), (28, 118), (34, 90)], GN13, 'f'), M([(74, 80), (80, 112), (72, 118), (66, 90)], GN13, 'f'),
                M([(12, 90), (10, 50), (16, 22), (34, 8), (50, 4), (66, 8), (84, 22), (90, 50), (88, 90), (66, 104), (50, 108), (34, 104)], BK13, 'f'),
                M([(18, 20), (4, 6), (0, -14, 1), (14, 0), (26, 12)], GO13, 'f'), M([(82, 20), (96, 6), (100, -14, 1), (86, 0), (74, 12)], GO13, 'f'),
                M([(30, 84), (50, 78), (70, 84), (64, 100), (50, 104), (36, 100)], _c('#9a9a9a'), 'f'),
                L(blob([(24, 64), (44, 70), (42, 80), (28, 78)], 4), _c('#f0e070'), 'f', False, True), L(blob([(76, 64), (56, 70), (58, 80), (72, 78)], 4), _c('#f0e070'), 'f', False, True)]
    if view == 'side':
        return [M([(70, 84), (78, 112), (70, 118), (64, 90)], GN13, 'f'),
                M([(8, 90), (6, 50), (16, 22), (40, 6), (66, 10), (84, 26), (92, 54), (92, 86), (76, 104), (44, 106), (20, 100)], BK13, 'f'),
                M([(40, 14), (36, -4), (44, -18, 1), (52, 6)], GO13, 'f'), M([(74, 84), (92, 80), (92, 98), (76, 102)], _c('#9a9a9a'), 'f'),
                L(blob([(74, 64), (90, 66), (90, 78), (76, 78)], 4), _c('#f0e070'), 'f', False, True)]
    return [M([(12, 96), (10, 50), (16, 22), (34, 8), (50, 4), (66, 8), (84, 22), (90, 50), (88, 96), (50, 104)], BK13, 'f'),
            M([(18, 20), (4, 6), (0, -14, 1), (14, 0), (26, 12)], GO13, 'f'), M([(82, 20), (96, 6), (100, -14, 1), (86, 0), (74, 12)], GO13, 'f')]
C('gomara-raccamere', 'normal', P('#2a2b2b', '#9a9a9a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True), _gomara('front'), _gomara('side'), _gomara('back'))

# Gupas Melaka: piel azul celeste, pelo rosa recogido en un gran rulo encima de la frente con dos lazadas arriba, y a
# los lados dos rulos blancos rosados en espiral como cuernos de carnero; ojos morados con pestañas, mejillas azules y
# boca de gatito
PK14, WH14 = _c('#f0b5a8'), _c('#f8ece8')
def _spiral(cx, cy, r, view_z='b'):
    return [L(ell(cx, cy, r, r), WH14, view_z, True, True), L(ell(cx, cy, r * 0.55, r * 0.55) + [ell(cx, cy, r * 0.55, r * 0.55)[0]], _c('#d8a8a0'), view_z, False, False, 1.4)]
C('gupas-melaka', 'chica', P('#f0b5a8', '#bbe4ec', iris='#7a4aa8', shade='#d0948a'),
  F(eyes='big', brows=False, mouth='none', hairline=[(10, 64), (18, 54), (30, 50), (50, 50), (70, 50), (82, 54), (90, 64)]),
  _spiral(10, 70, 13) + _spiral(90, 70, 13) +
  [M([(12, 64), (12, 34), (20, 20), (14, 4), (26, -4, 1), (36, 10), (50, 6), (64, 10), (74, -4, 1), (86, 4), (80, 20), (88, 34), (88, 64), (80, 52), (20, 52)]),
   L(ell(50, 40, 30, 11), 'mid', 'b', True, True), L(quad((26, 40), (50, 30), (74, 40)), 'shade', 'b', False, False, 1.4),
   B([(24, 86), (32, 86), (32, 90), (24, 90)], _c('#7aaad0')), B([(68, 86), (76, 86), (76, 90), (68, 90)], _c('#7aaad0')),
   ln([(43, 92), (46, 95), (50, 92), (54, 95), (57, 92)], OUTC, 1.3), ln([(26, 70), (22, 67)], OUTC, 1.6), ln([(74, 70), (78, 67)], OUTC, 1.6)],
  [M([(54, 58), (60, 46), (80, 40), (86, 26), (74, 10), (78, -4, 1), (60, 4), (40, 0), (20, 10), (6, 32), (8, 58), (22, 68), (40, 64)])] + _spiral(36, 70, 14, 'f') +
  [B([(78, 86), (86, 86), (86, 90), (78, 90)], _c('#7aaad0'))],
  _spiral(10, 72, 13) + _spiral(90, 72, 13) +
  [M([(14, 74), (12, 34), (20, 20), (14, 4), (26, -4, 1), (36, 10), (50, 6), (64, 10), (74, -4, 1), (86, 4), (80, 20), (88, 34), (86, 74), (50, 80)]),
   M([(58, 8), (80, 18), (86, 40), (84, 70), (64, 76)], 'shade', 'b', False)])

# Guramki Abantis: pelo celeste turquesa en mechones grandes de punta que salen hacia arriba y hacia los lados, con un
# mechón que le cae entre los ojos y una mata de pelusa blanca por detrás; piel verde menta pálida, ojos morados
TQ15 = _c('#6dc6ca')
C('guramki-abantis', 'normal', P('#6dc6ca', '#d3e7e3', iris='#8a4ac8', shade='#4a9aa0'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=94, hairline=hl(5, 66, 46, 60, lean=2, jit=3, seed=41)),
  [M([(84, 50), (98, 40), (104, 60), (96, 80), (88, 78)], WHITE, 'b')] +
  [M([(14, 74), (6, 46), (-4, 20, 1), (14, 26), (12, 0, 1), (28, 14), (36, -18, 1), (50, 6), (66, -12, 1), (68, 8), (90, -10, 1), (86, 20), (102, 30, 1), (92, 44),
      (90, 74), (82, 56), (18, 56)]),
   M([(56, 4), (66, -12), (68, 8), (90, -10), (86, 20), (100, 30), (92, 44), (88, 70), (76, 30)], 'shade', 'b', False),
   M([(44, 40), (52, 36), (54, 62), (50, 74, 1), (46, 60)], 'mid', 'f')],
  [M([(10, 54), (-4, 46), (-8, 70), (6, 84), (14, 76)], WHITE, 'b'),
   M([(54, 64), (62, 50), (84, 44), (100, 34, 1), (84, 26), (92, 4, 1), (70, 8), (64, -18, 1), (48, 0), (24, -12, 1), (22, 12), (2, 10, 1), (8, 36), (6, 64), (22, 76),
      (40, 72)]),
   M([(80, 44), (94, 46), (92, 68), (86, 74, 1), (84, 56)], 'mid', 'f')],
  [M([(14, 80), (6, 46), (-4, 20, 1), (14, 26), (12, 0, 1), (28, 14), (36, -18, 1), (50, 6), (66, -12, 1), (68, 8), (90, -10, 1), (86, 20), (102, 30, 1), (92, 44),
      (90, 80), (50, 86)]),
   M([(56, 4), (66, -12), (68, 8), (90, -10), (86, 20), (100, 30), (92, 44), (88, 78), (70, 50)], 'shade', 'b', False),
   M([(70, 50), (92, 44), (100, 64), (90, 84), (72, 76)], WHITE, 'f')])

# Gyan Cinquedea (Senguuji Daigo, adulto): pelo rosa peinado hacia atrás en crestas que se abren detrás en un abanico
# de puntas hacia los lados; piel morena, ojos grises afilados y cara larga
C('gyan-cinquedea', 'delgado', P('#f9b8b5', '#c1856c', iris='#5a6a70', shade='#d8908a', skin_d='#99594c'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=97, face_front=face(chin=106), face_side=face_side(chin=6, nose=3), nose=(50, 88, 2.6),
    hairline=[(8, 60), (18, 46), (30, 38), (50, 34), (70, 38), (82, 46), (92, 60)]),
  [M([(16, 64), (0, 70, 1), (8, 56), (-4, 50, 1), (12, 44), (14, 24), (30, 8), (50, 2), (70, 8), (86, 24), (88, 44), (104, 50, 1), (92, 56), (100, 70, 1), (84, 64),
      (80, 46), (20, 46)]),
   M([(60, 4), (80, 14), (88, 36), (100, 50), (90, 58), (82, 44)], 'shade', 'b', False)] +
  [ln([(36, 8), (40, 34)], 'shade', 1.2), ln([(50, 4), (50, 32)], 'shade', 1.2), ln([(64, 8), (60, 34)], 'shade', 1.2)],
  [M([(54, 56), (60, 42), (80, 34), (86, 18), (70, 2), (44, -2), (20, 8), (6, 30), (-8, 46, 1), (4, 52), (-10, 68, 1), (8, 66), (0, 84, 1), (20, 74), (40, 66)]),
   M([(8, 36), (30, 40), (40, 60), (20, 70), (2, 60)], 'shade', 'b', False), ln([(70, 8), (20, 30)], 'shade', 1.2), ln([(76, 22), (16, 48)], 'shade', 1.2)],
  [M([(16, 66), (-2, 74, 1), (8, 58), (-6, 50, 1), (12, 44), (14, 24), (30, 8), (50, 2), (70, 8), (86, 24), (88, 44), (106, 50, 1), (92, 58), (102, 74, 1), (84, 66),
      (70, 80, 1), (50, 72), (30, 80, 1)]),
   M([(60, 4), (80, 14), (88, 36), (104, 50), (92, 60), (84, 66), (70, 50)], 'shade', 'b', False)])

# Hanam Gurry: pelo rubio arena en forma de cebolla que termina en punta arriba, con dos cuernos oscuros enormes que le
# salen de los lados curvándose hacia arriba y un rombo rojo en la frente; piel lila muy pálida y ojos verde grisáceo
HORN17, RD17 = _c('#3a3532'), _c('#d8402a')
def _horns17(view):
    if view == 'side':
        return [M([(40, 50), (24, 40), (6, 20), (-4, 0, 1), (14, 18), (30, 34), (48, 44)], HORN17, 'f')]
    return [M([(22, 66), (8, 50), (-2, 30), (-6, 12, 1), (8, 30), (20, 48), (34, 60)], HORN17, 'f'),
            M([(78, 66), (92, 50), (102, 30), (106, 12, 1), (92, 30), (80, 48), (66, 60)], HORN17, 'f')]
C('hanam-gurry', 'chica', P('#bea476', '#f4e4f2', iris='#5a8a7a', shade='#92715a'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=94, hairline=[(10, 70), (18, 54), (32, 50), (50, 52), (68, 50), (82, 54), (90, 70)]),
  [M([(14, 82), (8, 50), (16, 26), (34, 8), (50, -12, 1), (66, 8), (84, 26), (92, 50), (86, 82), (80, 56), (20, 56)]),
   M([(54, -4), (66, 8), (84, 26), (90, 52), (84, 78), (74, 40)], 'shade', 'b', False)] + _horns17('front') +
  [M([(46, 52), (54, 52), (50, 66, 1)], RD17, 'f')],
  [M([(54, 62), (62, 50), (82, 46), (86, 26), (66, 6), (54, -12, 1), (40, 4), (18, 12), (6, 34), (6, 62), (20, 80), (40, 76)])] + _horns17('side'),
  [M([(12, 84), (8, 50), (16, 26), (34, 8), (50, -12, 1), (66, 8), (84, 26), (92, 50), (88, 84), (50, 90)]),
   M([(54, -4), (66, 8), (84, 26), (90, 52), (86, 82), (66, 86)], 'shade', 'b', False)] + _horns17('back'))

# Haniwa Pawlo (Haniwaa Paulo): cabeza de haniwa de barro marrón, un cilindro alto y redondeado arriba con dos agujeros
# negros redondos por ojos, una nariz en relieve y la boca en o
CL18, CL18D = _c('#ae885f'), _c('#876851')
def _haniwa(view):
    if view == 'front':
        return [M([(14, 104), (14, 20), (28, 0), (50, -6), (72, 0), (86, 20), (86, 104), (50, 110)], CL18, 'f'),
                B([(64, 0), (84, 20), (84, 102), (70, 106)], CL18D), ln([(46, 30), (46, 72), (54, 72), (54, 30)], CL18D, 1.4),
                L(ell(32, 60, 7, 8), OUTC, 'f', False), L(ell(68, 60, 7, 8), OUTC, 'f', False), L(ell(50, 88, 6, 7), OUTC, 'f', False)]
    if view == 'side':
        return [M([(10, 104), (10, 24), (24, 2), (50, -6), (74, 2), (88, 24), (90, 104), (50, 110)], CL18, 'f'), B([(10, 30), (40, 30), (40, 104), (12, 104)], CL18D),
                L(ell(84, 60, 3.4, 8), OUTC, 'f', False), M([(86, 34), (92, 40), (92, 70), (86, 72)], CL18, 'f'), L(ell(86, 88, 3, 6), OUTC, 'f', False)]
    return [M([(14, 104), (14, 20), (28, 0), (50, -6), (72, 0), (86, 20), (86, 104), (50, 110)], CL18, 'f'), B([(60, 0), (84, 20), (84, 102), (64, 106)], CL18D)]
C('haniwa-pawlo', 'normal', P('#ae885f', '#ae885f'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True), _haniwa('front'), _haniwa('side'), _haniwa('back'))

# Hannah Jarrow: piel blanca lila, melena corta blanca crema que le enmarca la cara y una trenza larga a un lado que acaba
# en un lazo rosa; un lazo rojo grande en lo alto con dos antenas negras de punta amarilla; ojos azules grandes
CR19, RD19, PK19 = _c('#f4ecdc'), _c('#c84050'), _c('#e8b0a8')
def _bow19(view):
    if view == 'side':
        return [M([(50, 4), (40, -10), (58, -8)], RD19, 'f'), M([(50, 4), (62, -14), (68, 2)], RD19, 'f'),
                ln([(46, -6), (30, -20), (24, -12)], OUTC, 1.4), L(ell(24, -12, 2.4, 2.4), _c('#e8d870'), 'f', False, True)]
    return [M([(64, 8), (54, -6), (64, -12), (70, 0)], RD19, 'f'), M([(70, 2), (82, -10), (90, 0), (80, 10)], RD19, 'f'),
            ln([(64, -6), (40, -22), (32, -14)], OUTC, 1.4), ln([(82, 0), (96, 14)], OUTC, 1.4),
            L(ell(32, -14, 2.4, 2.4), _c('#e8d870'), 'f', False, True), L(ell(96, 14, 2.4, 2.4), _c('#e8d870'), 'f', False, True)]
C('hannah-jarrow', 'chica', P('#f4ecdc', '#f8eef6', iris='#2a5a8a', shade='#d8ccbc'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=[(10, 72), (16, 56), (30, 48), (50, 52), (70, 48), (84, 56), (90, 72)]),
  [M([(14, 96), (8, 60), (12, 30), (28, 10), (50, 4), (72, 10), (88, 30), (92, 60), (86, 96), (80, 60), (20, 60)]),
   M([(12, 80), (2, 100), (4, 116), (14, 112), (20, 96)]), M([(4, 112), (-2, 118), (6, 124), (16, 120), (12, 112)], PK19, 'f')] + _bow19('front'),
  [M([(54, 60), (62, 48), (82, 44), (86, 24), (68, 6), (44, 2), (20, 10), (6, 34), (6, 70), (14, 96), (30, 100), (44, 88), (50, 72)])] + _bow19('side'),
  [M([(12, 98), (8, 60), (12, 30), (28, 10), (50, 4), (72, 10), (88, 30), (92, 60), (88, 98), (50, 102)]),
   M([(86, 80), (96, 100), (94, 116), (84, 112), (80, 96)]), M([(94, 112), (100, 118), (92, 124), (82, 120), (86, 112)], PK19, 'f')] + _bow19('front'))

# Hashi Bilocco (portero): cabeza de picozapato, una capucha gris verdosa con la parte de arriba plana y muy ancha, ojos
# con el borde rojo y un pico enorme marrón que baja por el centro hasta la punta roja
GT20, BK20, RD20 = _c('#9fb6b4'), _c('#90815c'), _c('#a8282e')
def _shoebill(view):
    if view == 'front':
        return [M([(8, 104), (12, 40), (2, 16), (-6, 4, 1), (20, 8), (50, 4), (80, 8), (106, 4, 1), (98, 16), (88, 40), (92, 104), (50, 110)], GT20, 'f'),
                B([(10, 70), (30, 70), (40, 104), (12, 104)], _c('#817978')), B([(90, 70), (70, 70), (60, 104), (88, 104)], _c('#817978')),
                M([(40, 50), (60, 50), (58, 92), (50, 106, 1), (42, 92)], BK20, 'f'), M([(44, 92), (56, 92), (50, 108, 1)], RD20, 'f')] + \
               [L(blob([(22, 46), (38, 50), (36, 58), (24, 56)], 4), RD20, 'f', False), L(ell(30, 52, 3, 3), WHITE, 'f', False, True),
                L(blob([(78, 46), (62, 50), (64, 58), (76, 56)], 4), RD20, 'f', False), L(ell(70, 52, 3, 3), WHITE, 'f', False, True)]
    if view == 'side':
        return [M([(6, 104), (4, 40), (-6, 16, 1), (20, 8), (60, 6), (90, 14), (88, 40), (84, 104), (40, 108)], GT20, 'f'),
                M([(70, 44), (98, 50), (104, 70), (98, 82, 1), (90, 74), (72, 70)], BK20, 'f'), M([(92, 74), (100, 76), (98, 86, 1)], RD20, 'f'),
                L(blob([(66, 40), (80, 42), (80, 50), (68, 50)], 4), RD20, 'f', False), L(ell(74, 45, 2.6, 2.6), WHITE, 'f', False, True)]
    return [M([(8, 104), (12, 40), (2, 16), (-6, 4, 1), (20, 8), (50, 4), (80, 8), (106, 4, 1), (98, 16), (88, 40), (92, 104), (50, 110)], GT20, 'f'),
            B([(60, 10), (90, 20), (90, 100), (64, 104)], _c('#7e9694'))]
C('hashi-bilocco', 'normal', P('#9fb6b4', '#9fb6b4'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True), _shoebill('front'), _shoebill('side'), _shoebill('back'))

# Hatara Tehaze: piel celeste, melena blanca lisa larga con el flequillo recto, dos mechones blancos que salen hacia
# arriba y hacia fuera como cuernos, y un mechón rojo fino que le cruza la cara; sombra de ojos morada, ojos verdes
# enfadados y puntitos azules en las mejillas
RD21 = _c('#d82a20')
C('hatara-tehaze', 'chica', P('#f6eef0', '#9ad8ec', iris='#2a7a3a', shade='#d8c8d0'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=94, hairline=[(10, 70), (16, 62), (30, 62), (50, 62), (70, 62), (84, 62), (90, 70)]),
  [M([(14, 114), (6, 80), (6, 44), (-6, 28), (-14, 14, 1), (4, 18), (14, 22), (30, 8), (50, 4), (70, 8), (86, 22), (96, 18), (114, 14, 1), (106, 28), (94, 44),
      (94, 80), (86, 114), (82, 64), (18, 64)]),
   M([(58, 6), (80, 16), (92, 44), (92, 80), (84, 110), (80, 64), (74, 30)], 'shade', 'b', False),
   B([(24, 70), (44, 72), (42, 78), (26, 78)], _c('#8a7ad8')), B([(76, 70), (56, 72), (58, 78), (74, 78)], _c('#8a7ad8')),
   ln([(60, 10), (54, 50), (42, 80), (34, 100)], RD21, 1.6),
   L(ell(28, 88, 1.2, 1.2), _c('#4a6ad0'), 'f', False), L(ell(72, 88, 1.2, 1.2), _c('#4a6ad0'), 'f', False)],
  [M([(56, 62), (64, 50), (84, 46), (90, 26), (98, 16), (110, 6, 1), (94, 4), (80, 6), (60, 0), (36, 2), (16, 12), (4, 36), (2, 80), (8, 112), (24, 118), (36, 108),
      (44, 86), (50, 70)]),
   ln([(64, 6), (40, 40), (24, 100)], RD21, 1.6), B([(72, 70), (86, 72), (86, 78), (74, 78)], _c('#8a7ad8'))],
  [M([(10, 116), (6, 80), (6, 44), (-6, 28), (-14, 14, 1), (4, 18), (14, 22), (30, 8), (50, 4), (70, 8), (86, 22), (96, 18), (114, 14, 1), (106, 28), (94, 44),
      (94, 80), (90, 116), (50, 120)]),
   M([(58, 6), (80, 16), (92, 44), (92, 80), (88, 114), (66, 118)], 'shade', 'b', False), ln([(40, 8), (36, 60), (30, 116)], RD21, 1.6)])

# Hattar Meppo: cabeza de pajarito en forma de campana color melocotón, con un rizo de nata en lo alto, ojitos negros de
# pestañas, un pico rosa en punta hacia abajo y una mancha blanca en la papada
PE22, WH22 = _c('#f0b8a0'), _c('#fcf4ec')
def _bell(view):
    if view == 'front':
        return [M([(2, 110), (8, 80), (20, 50), (30, 20), (40, 6), (50, 2), (60, 6), (70, 20), (80, 50), (92, 80), (98, 110), (70, 104), (50, 112), (30, 104)], PE22, 'f'),
                M([(38, 8), (40, -8), (52, -14), (62, -6), (56, 4), (48, 2), (46, 10)], WH22, 'f'),
                B([(26, 88), (40, 84), (50, 90), (60, 84), (74, 88), (70, 104), (50, 108), (30, 104)], WH22)] + eyes2(62, 12, 3.2, 4.2, OUTC, out=False) + [L(ell(37, 60.5, 1.1, 1.3), WHITE, 'f', False), L(ell(61, 60.5, 1.1, 1.3), WHITE, 'f', False)] + \
               [ln([(34, 58), (30, 55)], OUTC, 1.2), ln([(66, 58), (70, 55)], OUTC, 1.2),
                M([(44, 70), (56, 70), (50, 90, 1)], _c('#e06868'), 'f')]
    if view == 'side':
        return [M([(4, 110), (10, 80), (20, 50), (30, 20), (44, 4), (58, 4), (70, 20), (80, 50), (92, 80), (96, 110), (50, 112)], PE22, 'f'),
                M([(42, 6), (44, -10), (56, -14), (64, -6), (56, 4)], WH22, 'f'), B([(64, 88), (88, 86), (94, 106), (70, 108)], WH22),
                L(ell(72, 62, 2, 3), OUTC, 'f', False), M([(76, 70), (96, 76), (78, 84)], _c('#e06868'), 'f')]
    return [M([(2, 110), (8, 80), (20, 50), (30, 20), (40, 6), (50, 2), (60, 6), (70, 20), (80, 50), (92, 80), (98, 110), (50, 114)], PE22, 'f'),
            M([(38, 8), (40, -8), (52, -14), (62, -6), (56, 4), (48, 2), (46, 10)], WH22, 'f'), B([(56, 10), (80, 50), (94, 106), (66, 110)], _c('#d8a088'))]
C('hattar-meppo', 'corpulento', P('#f0b8a0', '#f0b8a0'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True), _bell('front'), _bell('side'), _bell('back'))

# Hawky Turbay: alienígena de piel rosa muy pálida con dos orejas grandes caídas hacia los lados, un gorro alto amarillo
# en forma de corona, marcas moradas en la frente y pelo morado oscuro por debajo de las orejas; ojos azules grandes con
# una raya debajo
YE23, PU23 = _c('#f0c040'), _c('#5a2a6a')
C('hawky-turbay', 'chica', P('#5a2a6a', '#f8e4ee', iris='#3a5aa8'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=False, ears=False),
  [M([(10, 84), (0, 92), (6, 100), (24, 96)]), M([(90, 84), (100, 92), (94, 100), (76, 96)]),
   M([(20, 64), (2, 58), (-8, 70), (2, 82), (20, 80)], 'skin', 'b'), M([(80, 64), (98, 58), (108, 70), (98, 82), (80, 80)], 'skin', 'b'),
   B([(4, 64), (16, 66), (16, 76), (4, 76)], _c('#f0b8c8')), B([(96, 64), (84, 66), (84, 76), (96, 76)], _c('#f0b8c8')),
   M([(22, 44), (20, 6), (30, -20), (50, -26), (70, -20), (80, 6), (78, 44), (50, 50)], YE23, 'f'),
   M([(36, 40), (36, 0), (50, -18), (64, 0), (64, 40)], _c('#e8a030'), 'f', False),
   B([(30, 54), (50, 48), (70, 54), (60, 58), (40, 58)], PU23), ln([(36, 62), (34, 70)], PU23, 1.6), ln([(64, 62), (66, 70)], PU23, 1.6),
   ln([(36, 82), (36, 88)], OUTC, 1), ln([(64, 82), (64, 88)], OUTC, 1)],
  [M([(14, 82), (6, 92), (20, 96)]), M([(40, 64), (26, 56), (16, 66), (24, 80), (42, 78)], 'skin', 'f'),
   M([(34, 44), (34, 6), (46, -20), (66, -24), (80, -14), (84, 10), (80, 44), (60, 50)], YE23, 'f')],
  [M([(10, 88), (4, 96), (14, 102), (50, 96), (86, 102), (96, 96), (90, 88)]),
   M([(20, 64), (2, 58), (-8, 70), (2, 82), (20, 80)], 'skin', 'b'), M([(80, 64), (98, 58), (108, 70), (98, 82), (80, 80)], 'skin', 'b'),
   M([(22, 44), (20, 6), (30, -20), (50, -26), (70, -20), (80, 6), (78, 44), (50, 50)], YE23, 'f')])

# Hector See: cabeza de pájaro blanca rosada (como un águila calva), con una franja de sombra azul oscuro sobre los ojos,
# un pico amarillo ancho y una pajarita roja al cuello
WP24, NV24 = _c('#f6e8ee'), _c('#2a2a6a')
def _eagle(view):
    if view == 'front':
        return [M([(10, 106), (8, 50), (16, 18), (34, 2), (50, -2), (66, 2), (84, 18), (92, 50), (90, 106), (50, 112)], WP24, 'f'),
                B([(18, 60), (36, 56), (50, 64), (64, 56), (82, 60), (78, 72), (64, 70), (50, 74), (36, 70), (22, 72)], NV24)] + \
               eyes2(66, 14, 4.6, 3.4, WHITE, OUTC, 0.6, True) + \
               [L(blob([(30, 76), (50, 72), (70, 76), (64, 84), (50, 92), (36, 84)], 4), _c('#f0e060'), 'f', False, True),
                M([(36, 104), (50, 108), (64, 104), (62, 112), (50, 110), (38, 112)], _c('#c83030'), 'f')]
    if view == 'side':
        return [M([(6, 106), (4, 50), (14, 18), (40, 0), (66, 4), (84, 20), (92, 50), (90, 106), (40, 110)], WP24, 'f'),
                B([(66, 58), (88, 60), (88, 70), (68, 70)], NV24), L(ell(80, 64, 2.4, 2), OUTC, 'f', False),
                L(blob([(80, 72), (100, 78), (90, 88), (80, 86)], 4), _c('#f0e060'), 'f', False, True)]
    return [M([(10, 106), (8, 50), (16, 18), (34, 2), (50, -2), (66, 2), (84, 18), (92, 50), (90, 106), (50, 112)], WP24, 'f'), B([(60, 6), (86, 22), (88, 100), (66, 106)], _c('#e8d0da'))]
C('hector-see', 'chica', P('#f6e8ee', '#f6e8ee'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True), _eagle('front'), _eagle('side'), _eagle('back'))

# Hemo Globin (portero): pelo verde en una mata enorme de pinchos revueltos que le tapa el ojo derecho y media cara, con
# una marca verde en la frente; oreja de punta, ojo rojo con ojera oscura y sonrisa tranquila
C('hemo-globin', 'normal', P('#5b8558', '#f3d6b2', iris='#c02020', shade='#47533b'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=93, hairline=hl(4, 64, 48, 56, lean=3, jit=3, seed=51)),
  ears_pointy('front', h=8)[1:] +
  [M([(10, 90), (0, 56), (-8, 34, 1), (6, 30), (2, 6, 1), (20, 14), (24, -12, 1), (40, 2), (54, -16, 1), (62, 4), (82, -6, 1), (80, 16), (100, 18, 1), (92, 36),
      (102, 50, 1), (88, 58), (82, 56), (60, 50), (54, 66), (48, 82), (34, 90), (20, 96)]),
   M([(60, 2), (82, -6), (80, 16), (98, 20), (92, 36), (100, 50), (88, 56), (72, 30)], 'shade', 'b', False),
   M([(6, 40), (24, 46), (46, 50), (56, 58), (50, 80), (36, 90), (18, 94), (6, 80)], 'mid', 'f'),
   B([(60, 48), (70, 46), (72, 52), (62, 54)], _c('#3a7a3a'))] + eye(64, 74, 4.6, 5.4, WHITE, _c('#c02020'), 0.62) +
  [L(ell(64, 74, 7, 7.4) + [ell(64, 74, 7, 7.4)[0]], _c('#6a4a4a'), 'f', False, False, 1.2), ln([(56, 66), (72, 64)], OUTC, 2)],
  [M([(54, 60), (62, 48), (82, 44), (98, 34, 1), (86, 24), (92, 2, 1), (70, 6), (62, -18, 1), (46, 0), (24, -12, 1), (22, 12), (2, 8, 1), (8, 34), (-4, 56, 1), (8, 64),
      (6, 86, 1), (22, 78), (40, 72)])] + ears_pointy('side', h=8) + [L(ell(81, 75, 3, 4.6), WHITE, 'f', False, True), L(ell(83, 75, 2, 3.2), _c('#c02020'), 'f', False)],
  [M([(10, 86), (0, 56), (-8, 34, 1), (6, 30), (2, 6, 1), (20, 14), (24, -12, 1), (40, 2), (54, -16, 1), (62, 4), (82, -6, 1), (80, 16), (100, 18, 1), (92, 36),
      (102, 50, 1), (92, 60), (90, 86), (70, 80, 1), (50, 88), (30, 80, 1)]),
   M([(60, 2), (82, -6), (80, 16), (98, 20), (92, 36), (100, 50), (90, 84), (70, 78)], 'shade', 'b', False)])

# Herak Lestril: casco de insecto amarillo verdoso con una cresta en punta en el centro y dos cuernos verde oscuro
# curvos, con pelo largo amarillo que cae por los lados; la cara de abajo es gris con una sonrisa de dientes de sierra y
# los ojos azulados en agujeros negros
YG26, GN26, GY26 = _c('#e2ec92'), _c('#6b702b'), _c('#a2a2a6')
def _beetle(view):
    if view == 'front':
        return [M([(12, 108), (8, 60), (14, 40), (86, 40), (92, 60), (88, 108), (76, 106), (74, 60), (26, 60), (24, 106)], _c('#d8c070'), 'f'),
                M([(22, 70), (30, 102), (50, 108), (70, 102), (78, 70)], GY26, 'f'),
                M([(14, 70), (14, 40), (26, 18), (40, 8), (50, -18, 1), (60, 8), (74, 18), (86, 40), (86, 70), (64, 62), (50, 84, 1), (36, 62)], YG26, 'f'),
                M([(24, 36), (14, 14), (18, -8, 1), (26, 14), (32, 32)], GN26, 'f'), M([(76, 36), (86, 14), (82, -8, 1), (74, 14), (68, 32)], GN26, 'f'),
                L(ell(40, 34, 1.6, 3), _c('#a8487a'), 'f', False), L(ell(60, 34, 1.6, 3), _c('#a8487a'), 'f', False)] + holes(72, 14, iris=_c('#c0d8f0'), w=8, h=5) + \
               [L([(32, 88), (68, 88), (66, 96), (34, 96)], WHITE, 'f', False, True), ln([(34, 92), (38, 88), (42, 96), (46, 88), (50, 96), (54, 88), (58, 96), (62, 88), (66, 92)], OUTC, 0.8)]
    if view == 'side':
        return [M([(10, 108), (6, 60), (20, 44), (30, 60), (34, 106)], _c('#d8c070'), 'f'), M([(56, 72), (66, 104), (88, 100), (92, 76)], GY26, 'f'),
                M([(14, 70), (12, 40), (30, 14), (50, -14, 1), (66, 10), (86, 32), (94, 60), (90, 76), (70, 66), (40, 70)], YG26, 'f'),
                M([(56, 30), (60, 8), (54, -10, 1), (48, 10), (48, 28)], GN26, 'f')] + hole_side(72, iris=_c('#c0d8f0')) + \
               [L([(78, 88), (92, 86), (90, 94), (78, 95)], WHITE, 'f', False, True)]
    return [M([(12, 110), (8, 60), (14, 40), (86, 40), (92, 60), (88, 110), (50, 112)], _c('#d8c070'), 'f'),
            M([(14, 70), (14, 40), (26, 18), (40, 8), (50, -18, 1), (60, 8), (74, 18), (86, 40), (86, 70), (50, 76)], YG26, 'f'),
            M([(24, 36), (14, 14), (18, -8, 1), (26, 14), (32, 32)], GN26, 'f'), M([(76, 36), (86, 14), (82, -8, 1), (74, 14), (68, 32)], GN26, 'f')]
C('herak-lestril', 'normal', P('#d8c070', '#a2a2a6'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True), _beetle('front'), _beetle('side'), _beetle('back'))

# Hick Idris: máscara de médico de la peste blanca, con dos gafas redondas grises y un pico largo que baja; alrededor,
# una capucha granate en pinchos con una cresta roja en el centro
MR27, RD27, WH27 = _c('#754645'), _c('#cf5352'), _c('#ece6e0')
def _plague(view):
    if view == 'front':
        return [M([(6, 110), (2, 60), (-8, 20, 1), (14, 30), (14, 0, 1), (30, 18), (40, -10), (50, -24, 1), (60, -10), (70, 18), (86, 0, 1), (86, 30), (108, 20, 1), (98, 60),
                   (94, 110), (50, 116)], MR27, 'f'),
                M([(44, 0), (50, -26, 1), (56, 0), (54, 20), (46, 20)], RD27, 'f'),
                M([(22, 96), (18, 50), (28, 24), (50, 16), (72, 24), (82, 50), (78, 96), (60, 92), (50, 112, 1), (40, 92)], WH27, 'f'),
                ln([(50, 18), (50, 108)], _c('#b8b0a8'), 1.2)] + \
               [L(ell(34, 60, 9, 9), _c('#4a4442'), 'f', False, True), L(ell(34, 60, 6, 6), _c('#9a9898'), 'f', False),
                L(ell(66, 60, 9, 9), _c('#4a4442'), 'f', False, True), L(ell(66, 60, 6, 6), _c('#9a9898'), 'f', False)]
    if view == 'side':
        return [M([(4, 110), (0, 60), (-8, 24, 1), (12, 26), (16, 0, 1), (34, 12), (50, -24, 1), (64, 6), (80, 22), (84, 60), (80, 110), (40, 114)], MR27, 'f'),
                M([(44, 4), (50, -26, 1), (58, 4)], RD27, 'f'),
                M([(56, 30), (78, 30), (88, 56), (100, 96, 1), (80, 90), (60, 70)], WH27, 'f'), L(ell(78, 54, 4, 8), _c('#4a4442'), 'f', False, True)]
    return [M([(6, 110), (2, 60), (-8, 20, 1), (14, 30), (14, 0, 1), (30, 18), (40, -10), (50, -24, 1), (60, -10), (70, 18), (86, 0, 1), (86, 30), (108, 20, 1), (98, 60),
               (94, 110), (50, 116)], MR27, 'f'), M([(44, 0), (50, -26, 1), (56, 0), (54, 20), (46, 20)], RD27, 'f')]
C('hick-idris', 'normal', P('#754645', '#ece6e0'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True), _plague('front'), _plague('side'), _plague('back'))

# Hika Rabeer: máscara de animal marrón claro con manchas crema, dos orejas de punta arriba y un mechón gris atado en lo
# alto; los ojos son rendijas negras con un brillo rojo y la boca, unos labios gruesos; piel oscura
BR28, CR28 = _c('#ae875f'), _c('#e6e2cb')
def _mask28(view):
    if view == 'front':
        return [M([(10, 20), (6, -10, 1), (26, 6)], BR28, 'f'), M([(90, 20), (94, -10, 1), (74, 6)], BR28, 'f'),
                M([(44, 4), (40, -12), (50, -18), (60, -12), (56, 4)], _c('#9a9898'), 'f'),
                M([(12, 90), (8, 40), (18, 14), (50, 2), (82, 14), (92, 40), (88, 90), (70, 104), (50, 108), (30, 104)], BR28, 'f'),
                B([(32, 20), (40, 18), (40, 28), (32, 28)], CR28), B([(60, 20), (68, 18), (68, 28), (60, 28)], CR28), B([(46, 14), (54, 14), (54, 24), (46, 24)], CR28),
                B([(20, 40), (28, 38), (28, 48), (20, 48)], CR28), B([(80, 40), (72, 38), (72, 48), (80, 48)], CR28),
                B([(28, 80), (50, 74), (72, 80), (66, 100), (50, 106), (34, 100)], CR28)] + \
               [L(blob([(22, 60), (44, 66), (42, 72), (26, 70)], 4), OUTC, 'f', False), L(blob([(78, 60), (56, 66), (58, 72), (74, 70)], 4), OUTC, 'f', False),
                L(ell(36, 68, 2, 1.4), _c('#d03030'), 'f', False), L(ell(64, 68, 2, 1.4), _c('#d03030'), 'f', False),
                L(blob([(38, 90), (50, 86), (62, 90), (50, 96)], 4), _c('#d87a5a'), 'f', False, True), ln([(38, 91), (62, 91)], OUTC, 1)]
    if view == 'side':
        return [M([(40, 14), (36, -16, 1), (56, 4)], BR28, 'f'), M([(40, 4), (36, -10), (48, -14), (52, 4)], _c('#9a9898'), 'f'),
                M([(10, 90), (6, 40), (20, 12), (50, 2), (78, 12), (92, 40), (94, 80), (84, 104), (50, 108), (24, 102)], BR28, 'f'),
                B([(30, 30), (40, 28), (40, 38), (30, 38)], CR28), B([(66, 80), (90, 76), (94, 96), (78, 104)], CR28),
                L(blob([(74, 62), (90, 64), (88, 72), (76, 70)], 4), OUTC, 'f', False), L(blob([(84, 86), (96, 86), (96, 94), (86, 94)], 4), _c('#d87a5a'), 'f', False, True)]
    return [M([(10, 20), (6, -10, 1), (26, 6)], BR28, 'f'), M([(90, 20), (94, -10, 1), (74, 6)], BR28, 'f'),
            M([(12, 92), (8, 40), (18, 14), (50, 2), (82, 14), (92, 40), (88, 92), (50, 100)], BR28, 'f'), B([(60, 8), (86, 30), (86, 88), (64, 96)], _c('#8d7158')),
            M([(44, 4), (40, -12), (50, -18), (60, -12), (56, 4)], _c('#9a9898'), 'f')]
C('hika-rabeer', 'normal', P('#ae875f', '#5a3a2a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True), _mask28('front'), _mask28('side'), _mask28('back'))

# Holly Mirae: cabeza redonda enorme de pelusa marrón rojiza, como una bola de lana, con la cara en medio: ojos de párpado
# caído, una nariz grande color carne y una boca ondulada; dos bolitas de pelusa más pequeñas a la altura de los hombros
BR29, BR29D = _c('#8e412a'), _c('#592b23')
def _fuzz(cx, cy, r, n, seed, c=BR29):
    import math, random
    rnd = random.Random(seed)
    pts = []
    for i in range(n * 2):
        a = math.pi * 2 * i / (n * 2)
        k = 1.0 if i % 2 == 0 else 0.9 + rnd.uniform(-0.03, 0.03)
        pts.append((cx + r * k * math.cos(a), cy + r * k * math.sin(a)))
    return M(pts, c, 'f')
def _holly(view):
    if view == 'front':
        return [_fuzz(8, 104, 12, 8, 1), _fuzz(92, 104, 12, 8, 2), _fuzz(50, 54, 50, 22, 3)] + \
               [L(ell(36, 56, 5, 5), WHITE, 'f', False, True), L(ell(64, 56, 5, 5), WHITE, 'f', False, True), L(ell(36, 57, 2.2, 3), OUTC, 'f', False),
                L(ell(64, 57, 2.2, 3), OUTC, 'f', False), ln([(30, 52), (42, 52)], OUTC, 2.2), ln([(58, 52), (70, 52)], OUTC, 2.2),
                M([(46, 58), (54, 58), (62, 76), (50, 80), (38, 76)], _c('#f3c8a0'), 'f'),
                ln([(30, 82), (36, 88), (42, 84), (50, 90), (58, 84), (64, 88), (70, 82)], OUTC, 1.4), ln([(50, 30), (50, 40)], BR29D, 1.2)]
    if view == 'side':
        return [_fuzz(30, 104, 12, 8, 1), _fuzz(46, 54, 50, 22, 3), M([(88, 54), (100, 70), (86, 76)], _c('#f3c8a0'), 'f'),
                L(ell(84, 56, 3, 5), WHITE, 'f', False, True), L(ell(86, 57, 1.8, 3), OUTC, 'f', False)]
    return [_fuzz(8, 104, 12, 8, 1), _fuzz(92, 104, 12, 8, 2), _fuzz(50, 54, 50, 22, 3), B([(60, 14), (90, 40), (90, 80), (64, 96)], BR29D)]
C('holly-mirae', 'corpulento', P('#8e412a', '#f3d1ab'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True), _holly('front'), _holly('side'), _holly('back'))

# Holsten Leebrook: piel celeste, pelo blanco en una gran onda que le tapa la cabeza y el ojo derecho, con un mechón gris
# azulado como un ala que sale hacia la izquierda y otro que le cae por el lado derecho hasta el cuello; ojo morado
GB30 = _c('#849aae')
C('holsten-leebrook', 'normal', P('#f2eef0', '#bce6ed', iris='#7a4ab0', shade='#c3b2b7'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=94, hairline=[(8, 66), (16, 54), (30, 50), (50, 50), (64, 52), (80, 56), (92, 66)]),
  [M([(14, 74), (8, 40), (20, 14), (44, 2), (70, 4), (88, 20), (94, 50), (92, 80), (86, 92), (80, 60), (60, 54), (52, 70), (40, 64), (20, 62)]),
   M([(58, 6), (80, 12), (92, 40), (92, 80), (84, 88), (80, 56)], 'shade', 'b', False),
   M([(20, 48), (4, 52), (-10, 62, 1), (6, 66), (24, 60)], GB30, 'f'),
   M([(10, 50), (30, 46), (50, 50), (60, 56), (54, 70), (42, 80), (30, 78), (24, 66), (12, 62)], 'mid', 'f'),
   M([(84, 70), (92, 74), (90, 104), (84, 110, 1), (80, 96)], GB30, 'f')] + eye(66, 76, 4.4, 5.4, WHITE, _c('#7a4ab0'), 0.62) + [ln([(60, 68), (72, 70)], OUTC, 1.6)],
  [M([(54, 62), (62, 50), (84, 46), (90, 26), (72, 6), (44, 0), (20, 8), (6, 32), (6, 62), (20, 72), (40, 70)]),
   M([(80, 46), (94, 50), (96, 66), (88, 62)], 'mid', 'f'), M([(18, 60), (4, 70), (6, 100), (12, 106, 1), (20, 82)], GB30, 'f'),
   L(ell(81, 76, 3, 4.4), WHITE, 'f', False, True), L(ell(83, 76, 2, 3), _c('#7a4ab0'), 'f', False)],
  [M([(12, 80), (8, 40), (20, 14), (44, 2), (70, 4), (88, 20), (94, 50), (90, 80), (50, 86)]),
   M([(58, 6), (80, 12), (92, 40), (90, 78), (66, 82)], 'shade', 'b', False), M([(80, 48), (96, 52), (110, 62, 1), (94, 66), (76, 60)], GB30, 'f'),
   M([(16, 70), (8, 74), (10, 104), (16, 110, 1), (20, 96)], GB30, 'f')])

# Honena Sisson: pelo rojo en tentáculos gruesos como un coral, con lunares melocotón, y uno que se enrosca sobre la
# frente; piel melocotón claro, orejas de punta, ojos grandes redondos y una naricilla de cerdito
RD31, PE31 = _c('#bd2b13'), _c('#f9bd90')
def _tent(x, y, tx, ty, w=6):
    return [M([(x - w, y), (tx - w * 0.6, ty), (tx, ty - w * 0.8), (tx + w * 0.6, ty), (x + w, y)], RD31, 'b'), B([(tx - 2, ty + 2), (tx + 2, ty + 2), (tx + 2, ty + 6), (tx - 2, ty + 6)], PE31, 'b')]
C('honena-sisson', 'chica', P('#bd2b13', '#fdf0d6', iris='#2a2020', shade='#932212'),
  F(eyes='round', brows=False, mouth='none', hairline=[(10, 64), (18, 52), (32, 46), (50, 46), (68, 46), (82, 52), (90, 64)]),
  ears_pointy('front', h=6) + _tent(20, 40, 0, 20) + _tent(30, 30, 14, -2) + _tent(44, 24, 38, -10) + _tent(58, 24, 64, -10) + _tent(70, 30, 86, -2) + _tent(80, 40, 100, 20) +
  [M([(14, 60), (12, 36), (26, 20), (50, 14), (74, 20), (88, 36), (86, 60), (78, 50), (22, 50)]),
   B([(30, 30), (36, 30), (36, 36), (30, 36)], PE31, 'b'), B([(62, 26), (68, 26), (68, 32), (62, 32)], PE31, 'b'),
   M([(36, 46), (30, 56), (38, 66), (46, 62), (42, 56)], RD31, 'f'),
   L(ell(50, 90, 5, 3.4), _c('#f0a8a0'), 'f', False, True), L(ell(48, 90, 0.8, 1), OUTC, 'f', False), L(ell(52, 90, 0.8, 1), OUTC, 'f', False)],
  ears_pointy('side', h=6) + _tent(40, 20, 30, -12) + _tent(26, 30, 6, 10) + _tent(56, 22, 70, -10) + _tent(20, 50, -2, 52) +
  [M([(54, 58), (62, 46), (82, 42), (86, 24), (70, 10), (44, 6), (20, 14), (8, 34), (8, 60), (22, 70), (40, 66)]), L(ell(88, 90, 3, 3), _c('#f0a8a0'), 'f', False, True)],
  _tent(20, 44, 0, 24) + _tent(30, 30, 14, -2) + _tent(44, 24, 38, -10) + _tent(58, 24, 64, -10) + _tent(70, 30, 86, -2) + _tent(80, 44, 100, 24) +
  [M([(14, 74), (12, 36), (26, 20), (50, 14), (74, 20), (88, 36), (86, 74), (50, 80)]), B([(30, 40), (36, 40), (36, 46), (30, 46)], PE31, 'f'),
   B([(62, 50), (68, 50), (68, 56), (62, 56)], PE31, 'f')])

# Horton Giess: cabeza de pájaro blanca con una franja gris verdosa por el centro que acaba en una cresta en punta, dos
# cejas-cuernos verdes enroscados, ojos con la pupila negra, un piquito amarillo y un cuello de plumas verdes
WH32, GN32 = _c('#ecece0'), _c('#7d8b4f')
def _bird32(view):
    if view == 'front':
        return [M([(4, 112), (14, 92), (30, 100), (50, 92), (70, 100), (86, 92), (96, 112)], GN32, 'f'),
                M([(14, 96), (12, 50), (20, 20), (38, 2), (50, -18, 1), (62, 2), (80, 20), (88, 50), (86, 96), (50, 104)], WH32, 'f'),
                M([(40, 10), (50, -14), (60, 10), (60, 80), (50, 92), (40, 80)], _c('#c5c8b2'), 'f', False),
                M([(40, 50), (24, 44), (8, 46), (4, 30, 1), (14, 38), (28, 38), (44, 46)], GN32, 'f'), M([(60, 50), (76, 44), (92, 46), (96, 30, 1), (86, 38), (72, 38), (56, 46)], GN32, 'f')] + \
               eyes2(60, 16, 5, 4, WHITE, OUTC, 0.55) + beak(66, 4, 10)
    if view == 'side':
        return [M([(20, 112), (30, 92), (60, 96), (86, 94), (94, 112)], GN32, 'f'),
                M([(8, 96), (6, 50), (18, 20), (40, 2), (52, -18, 1), (64, 4), (82, 22), (90, 50), (88, 96), (40, 104)], WH32, 'f'),
                M([(70, 50), (86, 44), (100, 46), (104, 30, 1), (94, 38), (80, 40), (66, 46)], GN32, 'f'),
                L(ell(80, 60, 3.2, 4), WHITE, 'f', False, True), L(ell(82, 60, 1.8, 2.4), OUTC, 'f', False)] + beak_side(68, 8, 6)
    return [M([(4, 112), (14, 92), (30, 100), (50, 92), (70, 100), (86, 92), (96, 112)], GN32, 'f'),
            M([(14, 96), (12, 50), (20, 20), (38, 2), (50, -18, 1), (62, 2), (80, 20), (88, 50), (86, 96), (50, 104)], WH32, 'f'),
            M([(40, 10), (50, -14), (60, 10), (60, 90), (40, 90)], _c('#c5c8b2'), 'f', False)]
C('horton-giess', 'normal', P('#7d8b4f', '#ecece0'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True), _bird32('front'), _bird32('side'), _bird32('back'))

# Hubert Iger (Tiger T): capucha de cabeza de tigre amarilla con rayas negras, orejas de dentro rosas y el hocico blanco
# con la nariz rosa sobre la frente; por debajo asoma el flequillo negro; ojos marrón rojizo y una sonrisa con colmillo
YE33, ST33 = _c('#f0b030'), _c('#2a2020')
def _tiger(view):
    if view == 'front':
        return [M([(14, 22), (10, 0), (20, -8), (30, 4)], YE33, 'f'), M([(86, 22), (90, 0), (80, -8), (70, 4)], YE33, 'f'),
                B([(16, 6), (22, 0), (26, 8), (20, 14)], _c('#f0a0b0')), B([(84, 6), (78, 0), (74, 8), (80, 14)], _c('#f0a0b0')),
                M([(6, 104), (2, 60), (6, 30), (20, 8), (50, 0), (80, 8), (94, 30), (98, 60), (94, 104), (84, 104), (84, 64), (80, 50), (20, 50), (16, 64), (16, 104)], YE33, 'f'),
                M([(18, 34), (50, 26), (82, 34), (84, 48), (50, 44), (16, 48)], WHITE, 'f'), L(ell(50, 34, 5, 3.4), _c('#f08098'), 'f', False, True),
                M([(20, 48), (30, 46), (40, 60), (50, 48), (60, 60), (70, 46), (80, 48), (78, 58), (22, 58)], ST33, 'f')] + \
               [ln([(44, 12), (40, 20)], ST33, 1.8), ln([(56, 12), (60, 20)], ST33, 1.8), ln([(50, 8), (50, 18)], ST33, 1.8),
                ln([(6, 50), (14, 54)], ST33, 1.6), ln([(4, 70), (14, 72)], ST33, 1.6), ln([(94, 50), (86, 54)], ST33, 1.6), ln([(96, 70), (86, 72)], ST33, 1.6),
                L([(55, 94), (57, 94), (56, 97)], WHITE, 'f', False, True)]
    if view == 'side':
        return [M([(36, 10), (30, -10), (44, -10)], YE33, 'f'),
                M([(4, 100), (0, 60), (6, 30), (24, 8), (54, 2), (78, 10), (90, 26), (96, 44), (82, 50), (62, 52), (56, 70), (60, 104), (30, 108)], YE33, 'f'),
                M([(70, 30), (92, 30), (100, 40), (92, 50), (72, 46)], WHITE, 'f'), L(ell(98, 40, 3, 3), _c('#f08098'), 'f', False, True),
                M([(70, 46), (90, 50), (86, 60), (76, 58)], ST33, 'f'), ln([(20, 30), (30, 40)], ST33, 1.8), ln([(10, 60), (22, 64)], ST33, 1.8)]
    return [M([(14, 22), (10, 0), (20, -8), (30, 4)], YE33, 'f'), M([(86, 22), (90, 0), (80, -8), (70, 4)], YE33, 'f'),
            M([(6, 104), (2, 60), (6, 30), (20, 8), (50, 0), (80, 8), (94, 30), (98, 60), (94, 104), (50, 108)], YE33, 'f'), B([(60, 8), (92, 30), (94, 100), (66, 104)], _c('#d8901e')),
            ln([(30, 30), (36, 44)], ST33, 1.8), ln([(70, 30), (64, 44)], ST33, 1.8), ln([(50, 20), (50, 36)], ST33, 1.8)]
C('hubert-iger', 'normal', P('#2a2020', '#f8c890', iris='#a03a2a'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=92, hairline=False, ears=False), _tiger('front'), _tiger('side'), _tiger('back'))

# Hugaro Tarlow: cara de máscara blanca ovalada con dos ojazos negros de pestañas y dos cuernos blancos curvos que se
# abren hacia arriba; tres puntitos grises en la frente y pelo gris liso por detrás hasta los hombros
WH34, GY34 = _c('#f6f4f2'), _c('#8e8a80')
C('hugaro-tarlow', 'chica', P('#8e8a80', '#f6f4f2', shade='#6e6a62'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False,
    face_front=blob([(22, 60), (32, 40), (50, 34), (68, 40), (78, 60), (72, 88), (58, 102), (50, 104), (42, 102), (28, 88)], 6)),
  [M([(12, 104), (6, 60), (12, 26), (30, 6), (50, 0), (70, 6), (88, 26), (94, 60), (88, 104), (76, 70), (24, 70)]),
   M([(34, 50), (20, 24), (22, -8, 1), (30, 22), (44, 44)], WH34, 'f'), M([(66, 50), (80, 24), (78, -8, 1), (70, 22), (56, 44)], WH34, 'f')] +
  [L(blob([(30, 70), (42, 66), (44, 76), (34, 80)], 4), OUTC, 'f', False), L(blob([(70, 70), (58, 66), (56, 76), (66, 80)], 4), OUTC, 'f', False),
   L(ell(38, 70, 1.2, 1.4), WHITE, 'f', False), L(ell(62, 70, 1.2, 1.4), WHITE, 'f', False),
   L(ell(50, 44, 1.6, 1.6), _c('#9a90a8'), 'f', False), L(ell(50, 52, 1.6, 1.6), _c('#9a90a8'), 'f', False), ln([(48, 96), (52, 96)], OUTC, 1)],
  [M([(52, 50), (60, 36), (80, 34), (86, 20), (70, 4), (44, 0), (20, 8), (6, 32), (4, 70), (10, 104), (30, 108), (44, 90), (48, 70)]),
   M([(66, 44), (60, 16), (64, -10, 1), (74, 16), (78, 40)], WH34, 'f'), L(blob([(78, 68), (90, 66), (90, 76), (80, 78)], 4), OUTC, 'f', False)],
  [M([(10, 106), (6, 60), (12, 26), (30, 6), (50, 0), (70, 6), (88, 26), (94, 60), (90, 106), (50, 110)]),
   M([(34, 40), (20, 20), (22, -8, 1), (30, 18), (44, 34)], WH34, 'b'), M([(66, 40), (80, 20), (78, -8, 1), (70, 18), (56, 34)], WH34, 'b'),
   M([(58, 6), (80, 16), (92, 50), (90, 104), (66, 106)], 'shade', 'b', False)])

# Hugh Semburn (portero): cabeza de nube rosa, en bultos redondos de algodón de azúcar (uno encima y dos a los lados);
# la cara rosa pálido con ojillos negros, el ceño fruncido, una nariz redonda rosa y la boca seria
PK35, PK35L = _c('#e8b0c8'), _c('#f6dce8')
def _cloud35(view):
    if view == 'front':
        return [L(ell(14, 56, 16, 18), PK35, 'f', True, True), L(ell(86, 56, 16, 18), PK35, 'f', True, True),
                M([(22, 96), (18, 56), (24, 30), (38, 10), (50, 4), (62, 10), (76, 30), (82, 56), (78, 96), (50, 104)], PK35L, 'f'),
                M([(22, 46), (26, 14), (40, -2), (60, -2), (74, 14), (78, 46), (62, 30), (50, 40), (38, 30)], PK35, 'f')] + \
               [L(ell(38, 64, 2, 2.6), OUTC, 'f', False), L(ell(62, 64, 2, 2.6), OUTC, 'f', False), ln([(32, 56), (42, 60)], OUTC, 1.8), ln([(68, 56), (58, 60)], OUTC, 1.8),
                L(ell(50, 74, 7, 6), PK35, 'f', False, True)] + mouth(90, 'frown', 6)
    if view == 'side':
        return [L(ell(30, 56, 18, 20), PK35, 'f', True, True), M([(30, 96), (34, 56), (40, 30), (54, 8), (70, 12), (84, 34), (90, 60), (86, 96), (60, 104)], PK35L, 'f'),
                M([(30, 40), (40, 10), (60, 0), (80, 12), (86, 36), (66, 30), (50, 40)], PK35, 'f'), L(ell(92, 74, 5, 5), PK35, 'f', False, True),
                L(ell(80, 64, 1.6, 2.6), OUTC, 'f', False), ln([(74, 56), (84, 59)], OUTC, 1.8)]
    return [L(ell(14, 56, 16, 18), PK35, 'f', True, True), L(ell(86, 56, 16, 18), PK35, 'f', True, True),
            M([(20, 98), (16, 50), (24, 14), (40, -2), (60, -2), (76, 14), (84, 50), (80, 98), (50, 104)], PK35, 'f')]
C('hugh-semburn', 'normal', P('#e8b0c8', '#f6dce8'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True), _cloud35('front'), _cloud35('side'), _cloud35('back'))

# Ilka Rugar: cabeza de pingüino gris verdoso oscuro, con un gorro de aviador marrón con una lámpara redonda dorada en la
# frente y las orejeras largas que bajan hasta los hombros; ojos de párpado caído, pico amarillo y una media luna azul en
# el pecho
DG36, BR36, CR36 = _c('#4a5450'), _c('#8a5a3a'), _c('#d8c8a8')
def _penguin(view):
    if view == 'front':
        return [M([(4, 112), (2, 60), (8, 26), (24, 8), (50, 2), (76, 8), (92, 26), (98, 60), (96, 112), (80, 112), (80, 60), (20, 60), (20, 112)], BR36, 'f'),
                M([(18, 112), (16, 60), (22, 46), (50, 40), (78, 46), (84, 60), (82, 112), (50, 116)], DG36, 'f'),
                M([(8, 30), (50, 20), (92, 30), (92, 42), (50, 34), (8, 42)], _c('#3a2a20'), 'f'), M([(26, 18), (50, 10), (74, 18), (70, 24), (30, 24)], CR36, 'f', False),
                L(ell(50, 34, 10, 10), _c('#d8a830'), 'f', False, True), L(ell(50, 34, 6.4, 6.4), CR36, 'f', False)] + \
               [L(ell(36, 60, 5, 4), WHITE, 'f', False, True), L(ell(64, 60, 5, 4), WHITE, 'f', False, True), L(ell(36, 61, 2, 2.6), OUTC, 'f', False),
                L(ell(64, 61, 2, 2.6), OUTC, 'f', False), ln([(30, 57), (42, 57)], OUTC, 2), ln([(58, 57), (70, 57)], OUTC, 2),
                L(blob([(38, 70), (50, 66), (62, 70), (50, 80)], 4), _c('#e8c860'), 'f', False, True),
                L(quad((40, 92), (50, 100), (60, 92)) + quad((60, 92), (50, 96), (40, 92))[1:], _c('#3aa8e0'), 'f', False)]
    if view == 'side':
        return [M([(4, 112), (2, 60), (8, 26), (30, 6), (60, 4), (82, 16), (90, 40), (70, 46), (60, 70), (64, 112)], BR36, 'f'),
                M([(56, 110), (58, 60), (70, 46), (88, 46), (94, 70), (92, 110)], DG36, 'f'), M([(12, 30), (60, 20), (88, 30), (88, 40), (60, 32), (10, 42)], _c('#3a2a20'), 'f'),
                L(ell(84, 34, 4, 9), _c('#d8a830'), 'f', False, True), L(ell(84, 60, 3, 3.6), WHITE, 'f', False, True), L(ell(85, 61, 1.6, 2.4), OUTC, 'f', False)] + beak_side(70, 10, 8)
    return [M([(4, 112), (2, 60), (8, 26), (24, 8), (50, 2), (76, 8), (92, 26), (98, 60), (96, 112), (50, 116)], BR36, 'f'),
            M([(8, 30), (50, 20), (92, 30), (92, 42), (50, 34), (8, 42)], _c('#3a2a20'), 'f'), B([(60, 10), (92, 30), (94, 108), (66, 112)], _c('#6a4428'))]
C('ilka-rugar', 'normal', P('#8a5a3a', '#4a5450'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True), _penguin('front'), _penguin('side'), _penguin('back'))

# Iriho: pelo negro en pinchos de punta hacia arriba, piel muy blanca, unas gafas grandes de cristal celeste y unos
# cascos morados con un micrófono delante de la boca
PU37 = _c('#7a6aa8')
C('iriho', 'normal', P('#1e2030', '#ecebf2', iris='#3a4a6a', shade='#141620'),
  F(eyes='closed', brows=False, mouth='line', mouth_y=94, ears=False, hairline=hl(5, 64, 48, 56, jit=2, seed=61)),
  dome('front', top=-8, w=44, cy=44, n=7, amp=14, seed=61, sb=62) +
  [M([(4, 62), (8, 56), (18, 58), (18, 84), (8, 86), (4, 80)], PU37, 'f'), M([(96, 62), (92, 56), (82, 58), (82, 84), (92, 86), (96, 80)], PU37, 'f')] +
  round_glasses('front', _c('#9aa8b8'), y=75, sep=14, r=9, lens=_c('#b0d8e0'), w=2.2) +
  [M([(40, 92), (60, 92), (58, 100), (42, 100)], PU37, 'f'), ln([(10, 84), (20, 96), (40, 96)], OUTC, 1.2)],
  dome('side', top=-8, w=44, cy=44, n=7, amp=14, seed=61, nape=84, fr=48) +
  [L(ell(46, 70, 9, 12), PU37, 'f', True, True), L(ell(82, 75, 5, 8), _c('#b0d8e0'), 'f', False, True), M([(80, 92), (94, 92), (94, 100), (80, 100)], PU37, 'f')],
  dome('back', top=-8, w=44, cy=44, n=7, amp=14, seed=61, nape=84) + [L(ell(8, 70, 7, 12), PU37, 'f', True, True), L(ell(92, 70, 7, 12), PU37, 'f', True, True)])

# Isor Eshen: pelo verde oliva en pinchos altos hacia arriba y una coleta larga que le cae por un lado; piel tostada,
# orejas de punta enormes con pendientes de aro turquesa, una cinta roja con unas gafas naranjas sobre los ojos y una
# sonrisa de dientes
OL38, RD38, TQ38 = _c('#8a9a3a'), _c('#d03a2a'), _c('#5ad0d0')
C('isor-eshen', 'normal', P('#8a9a3a', '#f6c080', iris='#2a2020', shade='#6a7a28'),
  F(eyes='closed', brows=False, mouth='grin', mouth_y=94, ears=False, hairline=hl(5, 60, 44, 54, jit=3, seed=71)),
  [M([(18, 66), (-6, 50, 1), (14, 80)], 'skin'), M([(82, 66), (106, 50, 1), (86, 80)], 'skin'),
   L(ell(10, 80, 3, 3) + [ell(10, 80, 3, 3)[0]], TQ38, 'f', False, False, 1.6), L(ell(90, 80, 3, 3) + [ell(90, 80, 3, 3)[0]], TQ38, 'f', False, False, 1.6)] +
  dome('front', top=-12, w=42, cy=44, n=7, amp=16, seed=71, sb=60) +
  [M([(70, 70), (78, 80), (74, 104), (66, 112, 1), (68, 90)], 'mid', 'f'),
   M([(16, 62), (50, 58), (84, 62), (84, 68), (50, 64), (16, 68)], RD38, 'f'),
   L(blob([(24, 68), (46, 70), (46, 82), (26, 82)], 4), _c('#e88a2a'), 'f', False, True), L(blob([(76, 68), (54, 70), (54, 82), (74, 82)], 4), _c('#e88a2a'), 'f', False, True),
   L(ell(36, 76, 4, 3), _c('#f6c080'), 'f', False), L(ell(64, 76, 4, 3), _c('#f6c080'), 'f', False),
   L(ell(36, 76, 1.6, 2), OUTC, 'f', False), L(ell(64, 76, 1.6, 2), OUTC, 'f', False)],
  dome('side', top=-12, w=42, cy=44, n=7, amp=16, seed=71, nape=84, fr=46) +
  [M([(44, 64), (28, 44, 1), (54, 60), (52, 80)], 'skin', 'f'), L(ell(44, 82, 3, 3) + [ell(44, 82, 3, 3)[0]], TQ38, 'f', False, False, 1.6),
   M([(20, 70), (30, 70), (26, 104), (18, 112, 1)], 'mid', 'f'), M([(40, 62), (90, 62), (90, 68), (40, 68)], RD38, 'f'),
   L(blob([(74, 68), (90, 70), (90, 82), (76, 82)], 4), _c('#e88a2a'), 'f', False, True)],
  [M([(18, 66), (-6, 50, 1), (14, 80)], 'skin'), M([(82, 66), (106, 50, 1), (86, 80)], 'skin')] +
  dome('back', top=-12, w=42, cy=44, n=7, amp=16, seed=71, nape=84) +
  [M([(44, 76), (56, 76), (58, 108), (50, 116, 1), (42, 108)], 'mid', 'f'), M([(14, 62), (86, 62), (86, 68), (14, 68)], RD38, 'f')])

# Iwan Gahana (portero): un gorro blanco en forma de fresa o seta, con manchas melocotón y un rabito verde arriba, que le
# llega a la cara; la cara blanca con ojos azules y la boca seria
WH39, PE39, GN39 = _c('#f6eef0'), _c('#e8a080'), _c('#5a8a3a')
def _straw(view):
    if view == 'front':
        return [M([(4, 84), (4, 50), (14, 22), (34, 6), (50, 2), (66, 6), (86, 22), (96, 50), (96, 84), (86, 92), (80, 66), (60, 56), (50, 64), (40, 56), (20, 66), (14, 92)], WH39, 'f'),
                B([(14, 40), (24, 36), (26, 48), (16, 50)], PE39), B([(62, 16), (74, 14), (76, 26), (64, 26)], PE39), B([(80, 50), (90, 48), (90, 60), (82, 60)], PE39),
                B([(36, 24), (44, 22), (44, 30), (36, 30)], PE39),
                M([(48, 4), (46, -6), (40, -12), (50, -10), (58, -16), (56, -6), (52, 4)], GN39, 'f')]
    if view == 'side':
        return [M([(4, 90), (2, 50), (14, 20), (40, 4), (66, 6), (86, 22), (94, 50), (90, 62), (66, 60), (54, 72), (40, 92), (20, 96)], WH39, 'f'),
                B([(14, 50), (26, 46), (28, 60), (16, 62)], PE39), B([(60, 16), (72, 14), (74, 26), (62, 26)], PE39), M([(42, 6), (40, -6), (34, -12), (46, -10), (50, 4)], GN39, 'f')]
    return [M([(4, 90), (4, 50), (14, 22), (34, 6), (50, 2), (66, 6), (86, 22), (96, 50), (96, 90), (50, 96)], WH39, 'f'),
            B([(20, 50), (32, 46), (34, 60), (22, 62)], PE39), B([(62, 26), (74, 24), (76, 36), (64, 36)], PE39), B([(70, 70), (82, 68), (84, 80), (72, 80)], PE39),
            M([(48, 4), (46, -6), (40, -12), (50, -10), (58, -16), (56, -6), (52, 4)], GN39, 'f')]
C('iwan-gahana', 'normal', P('#f6eef0', '#f8f4f6', iris='#2a7ac8'),
  F(eyes='normal', brows=False, mouth='frown', mouth_y=94, hairline=False, ears=False, face_front=face(chin=102)), _straw('front'), _straw('side'), _straw('back'))

# Iwers Mogan: casco de zorro azul marino oscuro con dos orejas en punta muy altas, que deja la cara azul celeste en
# punta hacia abajo; orejas de duende verde menta pálido hacia los lados, ojos rojos enfadados y una perilla oscura
NV40, MT40 = _c('#2a3a6a'), _c('#c0ecdc')
C('iwers-mogan', 'normal', P('#2a3a6a', '#a8d8d8', iris='#c02020', shade='#1e2a50'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=94, ears=False, hairline=[(8, 66), (20, 56), (36, 50), (50, 58), (64, 50), (80, 56), (92, 66)]),
  [M([(20, 66), (-6, 50, 1), (10, 82)], MT40), M([(80, 66), (106, 50, 1), (90, 82)], MT40),
   M([(14, 104), (8, 60), (10, 30), (14, -2), (20, -20, 1), (34, 6), (50, 2), (66, 6), (80, -20, 1), (86, -2), (90, 30), (92, 60), (86, 104), (80, 60), (20, 60)]),
   M([(40, 10), (50, 2), (60, 10), (56, 30), (50, 40), (44, 30)], _c('#4a6aa8'), 'b', False), M([(22, 0), (30, 18), (24, 20)], _c('#4a6aa8'), 'b', False),
   M([(78, 0), (70, 18), (76, 20)], _c('#4a6aa8'), 'b', False), M([(46, 98), (54, 98), (50, 106, 1)], NV40, 'f')],
  [M([(46, 66), (26, 52, 1), (52, 62), (50, 80)], MT40, 'f'),
   M([(54, 60), (62, 48), (82, 44), (88, 24), (78, 8), (82, -16, 1), (64, 2), (44, -2), (20, 8), (6, 32), (4, 70), (10, 104), (30, 108), (44, 88), (50, 72)])],
  [M([(20, 66), (-6, 50, 1), (10, 82)], MT40), M([(80, 66), (106, 50, 1), (90, 82)], MT40),
   M([(12, 106), (8, 60), (10, 30), (14, -2), (20, -20, 1), (34, 6), (50, 2), (66, 6), (80, -20, 1), (86, -2), (90, 30), (92, 60), (88, 106), (50, 110)]),
   M([(58, 6), (80, 16), (90, 50), (88, 104), (66, 106)], 'shade', 'b', False)])

# Iyer Zuck: cabeza de búho blanca con dos penachos rosados larguísimos que salen hacia los lados, los ojos en anillos
# finos como gafas, el pico marrón hacia abajo y el pecho azul marino oscuro en pico
WH41, PK41, NV41 = _c('#f6f4f2'), _c('#e8c8d0'), _c('#3a3a52')
def _owl(view):
    if view == 'front':
        return [M([(10, 112), (14, 92), (30, 96), (50, 110), (70, 96), (86, 92), (90, 112)], NV41, 'f'),
                M([(14, 96), (10, 50), (16, 24), (34, 10), (50, 6), (66, 10), (84, 24), (90, 50), (86, 96), (64, 98), (50, 110, 1), (36, 98)], WH41, 'f'),
                M([(24, 34), (6, 20), (-12, 6, 1), (8, 12), (30, 24)], PK41, 'f'), M([(76, 34), (94, 20), (112, 6, 1), (92, 12), (70, 24)], PK41, 'f')] + \
               [L(ell(36, 56, 7, 5) + [ell(36, 56, 7, 5)[0]], OUTC, 'f', False, False, 1.4), L(ell(64, 56, 7, 5) + [ell(64, 56, 7, 5)[0]], OUTC, 'f', False, False, 1.4),
                L(ell(38, 56, 1.4, 1.6), OUTC, 'f', False), L(ell(62, 56, 1.4, 1.6), OUTC, 'f', False), ln([(28, 50), (44, 46)], _c('#b8a8b0'), 1.6),
                ln([(72, 50), (56, 46)], _c('#b8a8b0'), 1.6)] + beak(60, 5, 22, _c('#9a7a5a'))
    if view == 'side':
        return [M([(30, 112), (40, 92), (70, 96), (90, 112)], NV41, 'f'),
                M([(8, 96), (6, 50), (16, 22), (40, 8), (66, 10), (84, 24), (90, 50), (88, 96), (40, 104)], WH41, 'f'),
                M([(30, 30), (10, 14), (-8, 2, 1), (12, 8), (36, 20)], PK41, 'f'), L(ell(80, 56, 4, 5) + [ell(80, 56, 4, 5)[0]], OUTC, 'f', False, False, 1.4)] + \
               beak_side(64, 8, 10, _c('#9a7a5a'))
    return [M([(14, 100), (10, 50), (16, 24), (34, 10), (50, 6), (66, 10), (84, 24), (90, 50), (86, 100), (50, 106)], WH41, 'f'),
            M([(24, 34), (6, 20), (-12, 6, 1), (8, 12), (30, 24)], PK41, 'f'), M([(76, 34), (94, 20), (112, 6, 1), (92, 12), (70, 24)], PK41, 'f')]
C('iyer-zuck', 'normal', P('#f6f4f2', '#f6f4f2'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True), _owl('front'), _owl('side'), _owl('back'))

# Jabhat Graffias (portero): cabeza de sapo amarilla con lunares oscuros, ojos saltones de pupila pequeña, una boca
# enorme de labio rojizo y un bonsái verde que le crece encima
YE42, SP42, GN42 = _c('#e8c040'), _c('#8a7a30'), _c('#4a9a3a')
def _toad(view):
    if view == 'front':
        return [M([(46, 10), (46, -4), (54, -4), (54, 10)], _c('#c8b080'), 'f'), L(ell(50, -14, 12, 10), GN42, 'f', True, True),
                M([(4, 90), (2, 60), (8, 30), (24, 12), (50, 6), (76, 12), (92, 30), (98, 60), (96, 90), (76, 102), (50, 106), (24, 102)], YE42, 'f'),
                B([(18, 30), (26, 28), (26, 36), (18, 36)], SP42), B([(74, 28), (82, 30), (82, 36), (74, 36)], SP42), B([(10, 58), (16, 56), (16, 64), (10, 64)], SP42),
                B([(84, 56), (90, 58), (90, 64), (84, 64)], SP42), B([(44, 92), (56, 92), (56, 100), (44, 100)], SP42)] + \
               eyes2(44, 18, 9, 9, WHITE, OUTC, 0.32) + \
               [L(quad((16, 66), (50, 58), (84, 66)) + quad((84, 66), (50, 86), (16, 66))[1:], _c('#c84a3a'), 'f', False, True),
                L(quad((22, 68), (50, 62), (78, 68)) + quad((78, 68), (50, 76), (22, 68))[1:], WHITE, 'f', False)]
    if view == 'side':
        return [M([(36, 10), (36, -4), (44, -4), (44, 10)], _c('#c8b080'), 'f'), L(ell(40, -14, 12, 10), GN42, 'f', True, True),
                M([(6, 90), (4, 50), (14, 22), (40, 6), (70, 10), (90, 30), (98, 60), (96, 86), (70, 102), (30, 104)], YE42, 'f'),
                B([(24, 40), (32, 38), (32, 46), (24, 46)], SP42), L(ell(78, 40, 7, 9), WHITE, 'f', True, True), L(ell(82, 40, 2.4, 3), OUTC, 'f', False),
                L(quad((60, 70), (90, 64), (98, 68)) + [(80, 78)], _c('#c84a3a'), 'f', False, True)]
    return [M([(46, 10), (46, -4), (54, -4), (54, 10)], _c('#c8b080'), 'f'), L(ell(50, -14, 12, 10), GN42, 'f', True, True),
            M([(4, 92), (2, 60), (8, 30), (24, 12), (50, 6), (76, 12), (92, 30), (98, 60), (96, 92), (50, 104)], YE42, 'f'),
            B([(30, 40), (38, 38), (38, 46), (30, 46)], SP42), B([(60, 60), (68, 58), (68, 66), (60, 66)], SP42), B([(70, 24), (78, 22), (78, 30), (70, 30)], SP42)]
C('jabhat-graffias', 'corpulento', P('#e8c040', '#e8c040'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True), _toad('front'), _toad('side'), _toad('back'))

# Jan Suparo: cabeza de fantasma pollito crema que le cae hasta los hombros en goterones, con un piquito amarillo y
# mejillas rosas; encima, un gorro de aviador verde oliva con unas gafas grises y un cuerno marrón en punta
CR43, OL43, BR43 = _c('#f4f0dc'), _c('#5a5a3a'), _c('#8a6a4a')
def _ghost(view):
    if view == 'front':
        return [M([(6, 108), (8, 70), (12, 40), (88, 40), (92, 70), (94, 108), (82, 112), (78, 104), (66, 112), (56, 104), (44, 112), (34, 104), (22, 112)], CR43, 'f'),
                M([(14, 46), (14, 22), (30, 8), (50, 4), (70, 8), (86, 22), (86, 46), (50, 40)], OL43, 'f'),
                M([(42, 8), (50, -26, 1), (58, 8)], BR43, 'f')] + \
               [L(ell(32, 26, 9, 7), _c('#9a9898'), 'f', False, True), L(ell(68, 26, 9, 7), _c('#9a9898'), 'f', False, True),
                L(ell(32, 26, 5, 4), _c('#d8d8d8'), 'f', False), L(ell(68, 26, 5, 4), _c('#d8d8d8'), 'f', False),
                L(ell(38, 60, 1.6, 2), OUTC, 'f', False), L(ell(62, 60, 1.6, 2), OUTC, 'f', False),
                B([(24, 70), (34, 68), (36, 78), (26, 80)], _c('#f0b0b0')), B([(76, 70), (66, 68), (64, 78), (74, 80)], _c('#f0b0b0'))] + beak(62, 5, 7)
    if view == 'side':
        return [M([(10, 108), (6, 70), (10, 40), (86, 40), (92, 70), (94, 108), (70, 112), (54, 104), (40, 112), (24, 104)], CR43, 'f'),
                M([(8, 46), (10, 20), (36, 4), (64, 6), (84, 22), (88, 46), (50, 40)], OL43, 'f'), M([(40, 6), (44, -26, 1), (54, 6)], BR43, 'f'),
                L(ell(78, 26, 6, 7), _c('#9a9898'), 'f', False, True), L(ell(82, 60, 1.6, 2), OUTC, 'f', False)] + beak_side(66, 6, 6)
    return [M([(6, 108), (8, 70), (12, 40), (88, 40), (92, 70), (94, 108), (50, 112)], CR43, 'f'),
            M([(14, 50), (14, 22), (30, 8), (50, 4), (70, 8), (86, 22), (86, 50), (50, 54)], OL43, 'f'), M([(42, 8), (50, -26, 1), (58, 8)], BR43, 'f'),
            ln([(14, 30), (86, 30)], _c('#9a9898'), 2.4)]
C('jan-suparo', 'normal', P('#5a5a3a', '#f4f0dc'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True), _ghost('front'), _ghost('side'), _ghost('back'))

# Jari Baras: máscara redonda de pájaro naranja tostado con manchas claras, los ojos en dos grandes manchas negras con
# un brillo blanco, la parte de abajo blanca con una boquita, y encima una espiga de anea marrón oscuro sobre un palito
OR44, WH44 = _c('#e8a060'), _c('#f8f0e8')
def _jari(view):
    if view == 'front':
        return [M([(48, 14), (48, 0), (52, 0), (52, 14)], _c('#d8c890'), 'f'), L(ell(50, -14, 7, 14), _c('#4a3020'), 'f', True, True),
                M([(14, 80), (12, 50), (20, 26), (36, 12), (50, 8), (64, 12), (80, 26), (88, 50), (86, 80), (74, 100), (50, 106), (26, 100)], OR44, 'f'),
                B([(36, 20), (48, 14), (50, 28), (40, 34)], _c('#f8d0a8')), B([(64, 20), (52, 14), (50, 28), (60, 34)], _c('#f8d0a8')),
                B([(28, 72), (50, 62), (72, 72), (70, 92), (50, 104), (30, 92)], WH44),
                L(blob([(18, 50), (42, 58), (40, 72), (24, 70)], 4), OUTC, 'f', False), L(blob([(82, 50), (58, 58), (60, 72), (76, 70)], 4), OUTC, 'f', False),
                L(ell(30, 60, 2.6, 2.6), WHITE, 'f', False), L(ell(70, 60, 2.6, 2.6), WHITE, 'f', False), L(ell(50, 84, 2.2, 3), OUTC, 'f', False)]
    if view == 'side':
        return [M([(44, 14), (44, 0), (48, 0), (48, 14)], _c('#d8c890'), 'f'), L(ell(46, -14, 6, 14), _c('#4a3020'), 'f', True, True),
                M([(8, 80), (8, 50), (18, 24), (42, 10), (66, 14), (84, 30), (92, 54), (90, 82), (76, 100), (44, 104), (20, 96)], OR44, 'f'),
                B([(66, 72), (88, 66), (92, 86), (76, 100)], WH44), L(blob([(70, 52), (90, 58), (88, 70), (74, 68)], 4), OUTC, 'f', False)]
    return [M([(48, 14), (48, 0), (52, 0), (52, 14)], _c('#d8c890'), 'f'), L(ell(50, -14, 7, 14), _c('#4a3020'), 'f', True, True),
            M([(14, 84), (12, 50), (20, 26), (36, 12), (50, 8), (64, 12), (80, 26), (88, 50), (86, 84), (50, 96)], OR44, 'f'), B([(58, 14), (82, 30), (84, 82), (64, 92)], _c('#d08848'))]
C('jari-baras', 'normal', P('#4a3020', '#f8e0c0'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True), _jari('front'), _jari('side'), _jari('back'))

# Jasper Lerner (Manabe Jinsuke, adulto): pelo gris corto peinado con raya y hacia atrás, gafas redondas finas, piel
# tostada, ojos grises afilados y cara larga seria
C('jasper-lerner', 'delgado', P('#8a8088', '#e8b080', iris='#5a5a6a', shade='#6a6068'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=97, face_front=face(chin=106), face_side=face_side(chin=6, nose=3), nose=(50, 88, 2.6),
    hairline=[(8, 60), (16, 48), (30, 42), (44, 40), (56, 38), (72, 40), (84, 46), (92, 60)]),
  [M([(14, 62), (12, 30), (26, 10), (50, 4), (74, 10), (88, 30), (86, 62), (80, 48), (20, 48)]),
   M([(54, 6), (74, 10), (88, 30), (86, 58), (76, 40)], 'shade', 'b', False), ln([(38, 8), (34, 40)], 'shade', 1.2)] +
  round_glasses('front', _c('#4a4040'), y=76, sep=14, r=7.5, w=1.4),
  [M([(54, 56), (62, 44), (82, 40), (86, 22), (70, 6), (44, 2), (20, 10), (8, 30), (8, 56), (20, 66), (40, 62)]),
   M([(8, 34), (28, 38), (40, 56), (24, 64), (10, 56)], 'shade', 'b', False)] + round_glasses('side', _c('#4a4040'), y=76, r=7.5, w=1.4),
  [M([(14, 70), (12, 30), (26, 10), (50, 4), (74, 10), (88, 30), (86, 70), (50, 78)]), M([(58, 8), (80, 18), (88, 40), (84, 68), (64, 72)], 'shade', 'b', False)])

# Jigo Jetok (portero): casco de robot gris que le tapa la cabeza hasta la nariz, con una franja de luz celeste arriba y
# un visor celeste; debajo, la cara pálida con la boca apretada y una barba negra redonda en la mandíbula
GY46, CY46 = _c('#9a9ea4'), _c('#5ae0e8')
def _robo(view):
    if view == 'front':
        return [M([(10, 74), (8, 40), (18, 14), (50, 4), (82, 14), (92, 40), (90, 74), (50, 78)], GY46, 'f'),
                M([(14, 32), (50, 24), (86, 32), (86, 40), (50, 34), (14, 40)], CY46, 'f'), M([(26, 60), (74, 60), (72, 68), (28, 68)], CY46, 'f'),
                M([(18, 78), (24, 96), (40, 108), (60, 108), (76, 96), (82, 78), (70, 80), (66, 98), (50, 102), (34, 98), (30, 80)], BLACK, 'f'),
                ln([(40, 88), (50, 86), (60, 88)], OUTC, 1.4)]
    if view == 'side':
        return [M([(6, 78), (4, 40), (16, 12), (44, 2), (74, 8), (90, 30), (92, 74), (60, 78)], GY46, 'f'), M([(10, 34), (50, 24), (90, 30), (90, 38), (50, 32), (10, 42)], CY46, 'f'),
                M([(70, 60), (92, 60), (92, 68), (70, 68)], CY46, 'f'), M([(50, 78), (60, 100), (80, 104), (88, 90), (86, 78), (74, 80), (70, 92), (62, 80)], BLACK, 'f')]
    return [M([(10, 78), (8, 40), (18, 14), (50, 4), (82, 14), (92, 40), (90, 78), (50, 84)], GY46, 'f'), M([(14, 32), (50, 24), (86, 32), (86, 40), (50, 34), (14, 40)], CY46, 'f'),
            B([(60, 10), (88, 30), (88, 74), (64, 80)], _c('#7a7e84'))]
C('jigo-jetok', 'normal', P('#1e1a1a', '#f4e4d8'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False), _robo('front'), _robo('side'), _robo('back'))

# Jomon Dorg: cabeza de dogū de barro dorado, redonda, con dos ojos almendrados verde claro enormes, una boca en o,
# pendientes de aro y una corona de cuernos curvos de hueso sobre la cabeza
GO47, GO47D = _c('#e8c040'), _c('#b88a20')
def _dogu(view):
    if view == 'front':
        return [M([(10, 20), (-4, 4), (-10, -10, 1), (6, 0), (30, 8), (70, 8), (94, 0), (110, -10, 1), (104, 4), (90, 20), (50, 16)], _c('#ece0c0'), 'f'),
                M([(30, 18), (34, 4), (50, 0), (66, 4), (70, 18)], GO47, 'f'),
                M([(10, 80), (8, 50), (16, 28), (34, 16), (50, 14), (66, 16), (84, 28), (92, 50), (90, 80), (76, 100), (50, 106), (24, 100)], GO47, 'f'),
                M([(46, 26), (54, 26), (52, 46), (48, 46)], GO47D, 'f', False)] + \
               [L(blob([(20, 56), (44, 62), (42, 72), (26, 70)], 4), _c('#e8f0a8'), 'f', False, True), L(blob([(80, 56), (56, 62), (58, 72), (74, 70)], 4), _c('#e8f0a8'), 'f', False, True),
                L(ell(50, 86, 4, 4), _c('#c89020'), 'f', False, True), L(ell(50, 86, 1.6, 1.6), OUTC, 'f', False),
                L(ell(8, 80, 4, 4) + [ell(8, 80, 4, 4)[0]], GO47D, 'f', False, False, 1.6), L(ell(92, 80, 4, 4) + [ell(92, 80, 4, 4)[0]], GO47D, 'f', False, False, 1.6)]
    if view == 'side':
        return [M([(30, 16), (10, 4), (2, -10, 1), (20, 0), (60, 6), (80, 14)], _c('#ece0c0'), 'f'),
                M([(8, 80), (6, 50), (16, 26), (40, 14), (66, 18), (84, 32), (92, 56), (90, 82), (76, 100), (44, 104), (20, 96)], GO47, 'f'),
                L(blob([(72, 56), (90, 60), (88, 72), (76, 70)], 4), _c('#e8f0a8'), 'f', False, True), L(ell(40, 80, 4, 4) + [ell(40, 80, 4, 4)[0]], GO47D, 'f', False, False, 1.6)]
    return [M([(10, 20), (-4, 4), (-10, -10, 1), (6, 0), (30, 8), (70, 8), (94, 0), (110, -10, 1), (104, 4), (90, 20), (50, 16)], _c('#ece0c0'), 'f'),
            M([(10, 84), (8, 50), (16, 28), (34, 16), (50, 14), (66, 16), (84, 28), (92, 50), (90, 84), (50, 96)], GO47, 'f'), B([(58, 18), (84, 32), (88, 82), (64, 92)], GO47D)]
C('jomon-dorg', 'normal', P('#e8c040', '#e8c040'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True), _dogu('front'), _dogu('side'), _dogu('back'))

# Josina Mary: melena corta naranja rojiza en mechones de punta con dos orejas grandes y caídas, color tostado, que le
# salen hacia los lados; piel morena clara, ojos morados grandes y una sonrisa
C('josina-mary', 'chica', P('#e05a2a', '#e8b080', iris='#5a3a7a', shade='#b8401a', skin_d='#c88a60'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, ears=False, hairline=hl(6, 68, 50, 60, jit=3, seed=81)),
  dome('front', top=4, w=46, cy=46, n=10, amp=6, seed=81, long=96, flare=4) +
  [M([(16, 40), (0, 30), (-16, 30, 1), (-6, 48), (6, 60), (18, 56)], 'skin', 'f'), M([(84, 40), (100, 30), (116, 30, 1), (106, 48), (94, 60), (82, 56)], 'skin', 'f'),
   B([(0, 36), (12, 40), (12, 52), (4, 50)], 'skin_d'), B([(100, 36), (88, 40), (88, 52), (96, 50)], 'skin_d')],
  [M([(40, 52), (24, 36), (16, 28, 1), (30, 34), (46, 46)], 'skin', 'b')] + dome('side', top=4, w=46, cy=46, n=10, amp=6, seed=81, long=96, fr=52),
  [M([(20, 52), (2, 40), (-12, 36, 1), (-2, 52), (8, 64), (20, 66)], 'skin'), M([(80, 52), (98, 40), (112, 36, 1), (102, 52), (92, 64), (80, 66)], 'skin')] +
  dome('back', top=4, w=46, cy=46, n=10, amp=6, seed=81, long=98, ends=5))

# Jude Caleb Juleb (Doudou): pelo verde azulado oscuro en pinchos revueltos hacia arriba y hacia atrás, con un mechón
# verde amarillento; unas gafas de nadador redondas de cristal verde sobre los ojos; piel tostada
TL49 = _c('#2a6a6a')
C('jude-caleb-juleb', 'normal', P('#2a6a6a', '#e0a070', iris='#2a2020', shade='#1e4a4a'),
  F(eyes='none', brows=False, mouth='line', mouth_y=94, hairline=hl(5, 62, 46, 56, lean=2, jit=3, seed=91)),
  dome('front', top=-8, w=46, cy=44, n=8, amp=14, sweep=0.5, seed=91, sb=66) +
  [M([(40, 30), (50, 12), (62, 0), (58, 24), (50, 44)], _c('#b8c070'), 'f')] + round_glasses('front', _c('#d8e0e0'), y=76, sep=14, r=8, lens=_c('#5a8a5a'), w=2.6),
  dome('side', top=-8, w=46, cy=44, n=8, amp=14, sweep=0.5, seed=91, nape=86, fr=48) + [M([(50, 20), (66, 4), (70, 20), (58, 32)], _c('#b8c070'), 'f')] +
  round_glasses('side', _c('#d8e0e0'), y=76, r=8, lens=_c('#5a8a5a'), w=2.6),
  dome('back', top=-8, w=46, cy=44, n=8, amp=14, sweep=0.5, seed=91, nape=86) + [ln([(10, 76), (90, 76)], _c('#d8e0e0'), 2.4)])

# Judie (Kanda Satoko): melena castaña rojiza en mechones hasta la barbilla, más larga por un lado, con una horquilla
# rosa a la derecha y una coleta baja larga por detrás; piel clara, ojos negros grandes y sonrisa
C('judie', 'chica', P('#a85a5a', '#fcecc8', iris='#1e1414', shade='#7a3e3e'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=[(10, 70), (16, 56), (30, 46), (44, 50), (58, 44), (72, 50), (84, 56), (90, 70)]),
  [M([(14, 96), (6, 60), (10, 28), (28, 8), (50, 2), (72, 8), (90, 28), (94, 60), (88, 100), (80, 64), (20, 64)]),
   M([(58, 4), (80, 14), (92, 40), (92, 64), (88, 96), (82, 62), (74, 30)], 'shade', 'b', False),
   ln([(70, 50), (80, 46)], _c('#f0a8c0'), 2.4), L(ell(80, 46, 2, 2), _c('#e85878'), 'f', False)],
  [M([(54, 60), (62, 48), (82, 44), (88, 24), (70, 6), (44, 0), (20, 8), (6, 32), (4, 64), (8, 90), (2, 112), (10, 116), (20, 92), (30, 80), (40, 70)]),
   M([(6, 36), (26, 40), (36, 64), (20, 90), (8, 80)], 'shade', 'b', False)],
  [M([(10, 98), (6, 60), (10, 28), (28, 8), (50, 2), (72, 8), (90, 28), (94, 60), (90, 98), (60, 96), (56, 116), (48, 120, 1), (42, 112), (40, 96)]),
   M([(58, 6), (80, 16), (92, 40), (92, 96), (66, 96)], 'shade', 'b', False)])

# Julia Blaze (Gouenji Yuuka): pelo castaño con un remolino alto en punta encima, flequillo de mechones y dos trenzas
# bajas enroscadas que salen hacia los lados; piel clara, ojos negros grandes y una sonrisa
BR51 = _c('#8a6a50')
def _braid(x, d):
    return [L(ell(x, 82, 6, 6), 'mid', 'b', True, True), L(ell(x + d * 8, 90, 6, 5.4), 'mid', 'b', True, True), L(ell(x + d * 14, 98, 5, 4.6), 'mid', 'b', True, True),
            M([(x + d * 16, 100), (x + d * 24, 104), (x + d * 20, 110, 1)], 'mid', 'b')]
C('julia-blaze', 'chica', P('#8a6a50', '#fde4c4', iris='#1e1414', shade='#6a4e38'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=hl(6, 66, 50, 60, jit=2, seed=101)),
  _braid(14, -1) + _braid(86, 1) + dome('front', top=4, w=46, cy=46, n=0, sb=74, seed=101) + [M([(46, 8), (40, -12), (30, -20, 1), (48, -14), (56, 6)], 'mid', 'f')],
  [L(ell(30, 84, 7, 7), 'mid', 'b', True, True), L(ell(22, 94, 6, 5.4), 'mid', 'b', True, True), L(ell(14, 102, 5, 4.6), 'mid', 'b', True, True)] +
  dome('side', top=4, w=46, cy=46, n=0, nape=86, fr=52, seed=101) + [M([(42, 6), (36, -12), (26, -20, 1), (44, -14), (52, 4)], 'mid', 'f')],
  _braid(14, -1) + _braid(86, 1) + dome('back', top=4, w=46, cy=46, n=0, nape=88, seed=101) + [M([(46, 8), (40, -12), (30, -20, 1), (48, -14), (56, 6)], 'mid', 'f')])

# Kagraro Ephemera: una capucha-melena granate morada que le cae hasta los hombros y acaba arriba en una punta curva; la
# cara verde menta claro con el pelo en flequillo cosido con puntadas negras que le tapa los ojos, y una sonrisa
PU52, MT52 = _c('#8a2a5a'), _c('#bfe8e0')
C('kagraro-ephemera', 'normal', P('#8a2a5a', '#bfe8e0', shade='#6a1e44'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, hairline=[(10, 80), (16, 76), (30, 76), (50, 76), (70, 76), (84, 76), (90, 80)]),
  [M([(6, 116), (0, 70), (6, 30), (20, 10), (44, 0), (54, -20), (66, -30, 1), (64, -12), (72, 6), (90, 26), (98, 70), (94, 116), (84, 116), (82, 80), (18, 80), (16, 116)]),
   M([(60, -10), (72, 6), (90, 26), (96, 70), (90, 112), (84, 78), (74, 30)], 'shade', 'b', False)] +
  [ln([(x, 66), (x, 80)], OUTC, 1.4) for x in (30, 42, 58, 70)],
  [M([(56, 78), (64, 60), (84, 56), (90, 30), (72, 8), (60, -4), (64, -28, 1), (48, -12), (30, -2), (10, 14), (0, 50), (2, 100), (14, 116), (36, 116), (46, 96)]),
   ln([(78, 66), (78, 80)], OUTC, 1.4)],
  [M([(6, 116), (0, 70), (6, 30), (20, 10), (44, 0), (54, -20), (66, -30, 1), (64, -12), (72, 6), (90, 26), (98, 70), (94, 116), (50, 120)]),
   M([(60, -10), (72, 6), (90, 26), (96, 70), (92, 114), (70, 116)], 'shade', 'b', False)])

# Kanzan Focho (portera): bicho rechoncho morado claro, como un pájaro de cuerpo gordo, con una franja blanca en la
# frente, ojos morados grandes, un pico amarillo y dos antenas negras largas con la punta lila
LV53, PU53 = _c('#c8a8e0'), _c('#7a4ab0')
def _focho(view):
    if view == 'front':
        return [ln([(30, 14), (10, -4), (0, -24)], OUTC, 1.6), ln([(70, 14), (90, -4), (100, -24)], OUTC, 1.6),
                L(ell(0, -26, 2.6, 4), _c('#d8b8e8'), 'f', False, True), L(ell(100, -26, 2.6, 4), _c('#d8b8e8'), 'f', False, True),
                M([(2, 112), (6, 70), (12, 36), (28, 14), (50, 8), (72, 14), (88, 36), (94, 70), (98, 112), (50, 116)], LV53, 'f'),
                M([(44, 14), (56, 14), (54, 40), (50, 48), (46, 40)], WHITE, 'f', False)] + \
               eyes2(56, 18, 6, 6, WHITE, PU53, 0.62) + [ln([(10, 52), (24, 48)], OUTC, 1.6), ln([(90, 52), (76, 48)], OUTC, 1.6)] + beak(60, 7, 12, _c('#e8d050')) + \
               [ln(quad((28, 92), (50, 100), (72, 92)), _c('#9a78b8'), 1.6)]
    if view == 'side':
        return [ln([(40, 14), (30, -6), (24, -26)], OUTC, 1.6), L(ell(24, -28, 2.6, 4), _c('#d8b8e8'), 'f', False, True),
                M([(4, 112), (6, 70), (14, 36), (36, 12), (62, 12), (82, 30), (92, 60), (96, 112), (50, 116)], LV53, 'f'),
                L(ell(80, 56, 4, 6), WHITE, 'f', False, True), L(ell(82, 56, 2.4, 3.6), PU53, 'f', False)] + beak_side(64, 10, 10, _c('#e8d050'))
    return [ln([(30, 14), (10, -4), (0, -24)], OUTC, 1.6), ln([(70, 14), (90, -4), (100, -24)], OUTC, 1.6),
            M([(2, 112), (6, 70), (12, 36), (28, 14), (50, 8), (72, 14), (88, 36), (94, 70), (98, 112), (50, 116)], LV53, 'f'), B([(60, 14), (88, 40), (94, 108), (66, 112)], _c('#a888c8'))]
C('kanzan-focho', 'corpulento', P('#c8a8e0', '#c8a8e0'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True), _focho('front'), _focho('side'), _focho('back'))

# Karka Poe: cabeza de pájaro verde alargada hacia arriba que acaba en un rizo, con los ojos cerrados contentos y un pico
# naranja grande
GN54 = _c('#6a9a4a')
def _karka(view):
    if view == 'front':
        return [M([(10, 112), (10, 60), (16, 30), (30, 12), (44, 4), (40, -10), (46, -22), (60, -18), (54, -12), (56, 4), (70, 12), (84, 30), (90, 60), (90, 112), (50, 116)], GN54, 'f'),
                ln(quad((28, 56), (36, 50), (44, 56)), OUTC, 2), ln(quad((56, 56), (64, 50), (72, 56)), OUTC, 2),
                L(outline([(34, 64), (66, 64), (60, 80), (50, 90, 1), (40, 80)]), _c('#e89060'), 'f', False, True), ln([(38, 72), (62, 72)], _c('#c06a40'), 1)]
    if view == 'side':
        return [M([(10, 112), (8, 60), (16, 28), (36, 10), (40, -8), (50, -20), (62, -14), (54, -8), (54, 8), (76, 18), (88, 40), (90, 112), (50, 116)], GN54, 'f'),
                ln(quad((72, 56), (78, 50), (84, 56)), OUTC, 2), L(outline([(82, 62), (104, 74, 1), (82, 84)]), _c('#e89060'), 'f', False, True)]
    return [M([(10, 112), (10, 60), (16, 30), (30, 12), (44, 4), (40, -10), (46, -22), (60, -18), (54, -12), (56, 4), (70, 12), (84, 30), (90, 60), (90, 112), (50, 116)], GN54, 'f'),
            B([(60, 14), (86, 34), (88, 108), (64, 112)], _c('#4e7a38'))]
C('karka-poe', 'chica', P('#6a9a4a', '#6a9a4a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True), _karka('front'), _karka('side'), _karka('back'))

# Katie Forester (Kodama Fumika): pelo castaño con flequillo, recogido atrás en una coleta con un lazo rosa grande en lo
# alto; piel clara, ojos castaños grandes y sonrisa
PK55 = _c('#f080b8')
C('katie-forester', 'chica', P('#8a5038', '#fde0c4', iris='#5a3a2a', shade='#6a3a28'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=[(10, 70), (16, 56), (30, 50), (50, 54), (70, 50), (84, 56), (90, 70)]),
  [M([(14, 80), (8, 50), (14, 24), (30, 10), (50, 6), (70, 10), (86, 24), (92, 50), (86, 80), (80, 60), (20, 60)]),
   M([(58, 8), (80, 16), (90, 40), (88, 74), (78, 40)], 'shade', 'b', False),
   M([(50, 6), (36, -8), (32, 4), (40, 10)], PK55, 'f'), M([(50, 6), (64, -8), (68, 4), (60, 10)], PK55, 'f'), L(ell(50, 6, 3, 3), PK55, 'f', False, True)],
  [M([(54, 58), (62, 46), (82, 42), (88, 24), (70, 8), (44, 4), (20, 12), (6, 34), (6, 60), (20, 70), (40, 66)]),
   M([(14, 40), (2, 60), (4, 90), (12, 94), (20, 70)]), M([(40, 8), (30, -6), (28, 6)], PK55, 'f')],
  [M([(12, 82), (8, 50), (14, 24), (30, 10), (50, 6), (70, 10), (86, 24), (92, 50), (88, 82), (50, 86)]),
   M([(42, 40), (58, 40), (60, 90), (50, 100, 1), (40, 90)], 'shade', 'f'),
   M([(50, 6), (36, -8), (32, 4), (40, 10)], PK55, 'f'), M([(50, 6), (64, -8), (68, 4), (60, 10)], PK55, 'f')])

# Kaven Mirae (portera): piel amarilla, pelo verde con flequillo en punta y dos trenzas largas atadas con gomas naranjas;
# dos orejas amarillas enormes en punta hacia arriba y hacia fuera, como de murciélago; ojos verdes serios
YE56, OR56 = _c('#e0c840'), _c('#e87a2a')
C('kaven-mirae', 'chica', P('#4ab060', '#e8d850', iris='#3a8a2a', shade='#2a8a40'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=93, ears=False, hairline=[(10, 66), (18, 56), (32, 50), (44, 58), (56, 50), (70, 56), (84, 56), (90, 66)]),
  [M([(18, 46), (6, 20), (-2, -16, 1), (16, 8), (28, 30)], 'skin', 'b'), M([(82, 46), (94, 20), (102, -16, 1), (84, 8), (72, 30)], 'skin', 'b'),
   M([(14, 70), (10, 40), (22, 18), (50, 10), (78, 18), (90, 40), (86, 70), (80, 56), (20, 56)]),
   M([(14, 66), (20, 66), (24, 104), (16, 108)]), M([(86, 66), (80, 66), (76, 104), (84, 108)]),
   M([(14, 98), (24, 98), (24, 104), (14, 104)], OR56, 'f'), M([(86, 98), (76, 98), (76, 104), (86, 104)], OR56, 'f')],
  [M([(50, 40), (40, 14), (40, -18, 1), (54, 10), (60, 34)], 'skin', 'b'),
   M([(54, 58), (62, 46), (82, 42), (86, 26), (70, 12), (44, 8), (20, 16), (8, 36), (8, 60), (22, 70), (40, 66)]),
   M([(20, 64), (28, 64), (28, 104), (20, 108)]), M([(20, 98), (28, 98), (28, 104), (20, 104)], OR56, 'f')],
  [M([(18, 46), (6, 20), (-2, -16, 1), (16, 8), (28, 30)], 'skin', 'b'), M([(82, 46), (94, 20), (102, -16, 1), (84, 8), (72, 30)], 'skin', 'b'),
   M([(12, 76), (10, 40), (22, 18), (50, 10), (78, 18), (90, 40), (88, 76), (50, 82)]),
   M([(18, 70), (26, 70), (28, 106), (20, 110)]), M([(82, 70), (74, 70), (72, 106), (80, 110)]),
   M([(20, 100), (28, 100), (28, 106), (20, 106)], OR56, 'f'), M([(80, 100), (72, 100), (72, 106), (80, 106)], OR56, 'f')])
