"""Ojeadores de GO (scouts-go), tanda 05: dibujados a partir de su retrato de Victory Road; claves 'scouts-go:<id>'.

Ninguno tiene modelo 3D propio que sirva (el de Jade Greene es otro personaje): el frente sale del retrato y el perfil y
la espalda se deducen del peinado o del gorro. Usa dome()/hl()/face() de la tanda 09 de IE1, cap()/band() de la 06 de
IE3, bowl3()/hood()/ring() de la 02 de IE3 y mir() de la 02 de IE1, y añade unos pocos ayudantes propios."""
import math

from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars_scouts_ie1_02 import mir  # noqa: F401
from chars_scouts_ie1_09 import F, P, _c, dome, face, face_side, hl, mark  # noqa: F401
from chars_scouts_ie3_02 import bowl3, hood, ring, scarf  # noqa: F401
from chars_scouts_ie3_06 import arc, band, cap  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)
RED = (200, 40, 40, 255)


def C(pid, body, palette, f, front, side, back):
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        # el nacimiento del pelo baja por el borde de la cara: así su raya no cruza el pelo de los lados
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + [tuple(p[:2]) for p in hl_[1:-1]] + [(max(xs) - 0.6, 104)]
    CHARS[f'scouts-go:{pid}'] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def R(p0, c, p1, col='mid', w=6, z='f'):
    """Mechón grueso redondeado (trenzas, cuerdas) de p0 a p1 pasando por c."""
    return L(rope(p0, c, p1, w), col, z)


def bandl(*a, **k):
    return [band(*a, **k)]


def lock(pts, c='mid', z='f'):
    """Mechón o forma de pelo por delante de la cara."""
    return L(outline(pts), c, z)


def shade(pts, c='shade', z='b'):
    return L(blob(pts, 6), c, z, False)


def sidelocks(y=100, x=(18, 82), w=8, c='mid', z='f'):
    """Dos mechones que bajan junto a la cara de frente hasta y."""
    return [lock([(x[0] - w * 0.6, 54), (x[0] + w * 0.5, 56), (x[0] + w * 0.2, y - 8), (x[0] - w * 0.1, y, 1), (x[0] - w * 0.6, y - 10)], c, z),
            lock([(x[1] + w * 0.6, 54), (x[1] - w * 0.5, 56), (x[1] - w * 0.2, y - 8), (x[1] + w * 0.1, y, 1), (x[1] + w * 0.6, y - 10)], c, z)]


def side_lock_s(y=100, c='mid', z='f'):
    """El mechón de delante de la oreja, de perfil."""
    return lock([(56, 56), (64, 56), (62, y - 8), (58, y, 1), (54, y - 10)], c, z)


def long_back(y=120, w=48, c='mid', n=4):
    """Melena larga por detrás (espalda) hasta y."""
    pts = [(50 - w, 50), (50 - w - 2, y - 14)]
    for i in range(n + 1):
        x = 50 - w + i * (2 * w) / n
        pts += [(x, y + (4 if i % 2 == 0 else 0), 1)] if 0 < i < n else [(x, y, 1)]
    pts += [(50 + w + 2, y - 14), (50 + w, 50)]
    return L(outline(pts), c)


def long_side(y=120, c='mid'):
    """Melena larga por detrás de la cabeza (perfil)."""
    return L(outline([(40, 40), (6, 46), (0, 80), (2, y - 10), (10, y, 1), (24, y - 6), (34, y + 2, 1), (46, y - 14), (54, 80), (56, 50)]), c)


def spiral_eyes(ey=75, sep=14, c=WHITE, r=6.5):
    """Ojos en espiral o de anillo (blancos con dos anillos negros)."""
    out = []
    for cx in (50 - sep, 50 + sep):
        out += [L(ell(cx, ey, r + 1.6, r + 1.2), BLACK, 'f', False), L(ell(cx, ey, r, r * 0.8), c, 'f', False),
                L(ell(cx, ey, r * 0.55, r * 0.45) + [ell(cx, ey, r * 0.55, r * 0.45)[0]], BLACK, 'f', False, False, 1.2), L(ell(cx, ey, 1.6, 1.4), BLACK, 'f', False)]
    return out


def ring_eye_side(ey=75, r=6, c=WHITE):
    return [L(ell(81, ey, r * 0.75, r + 1), BLACK, 'f', False), L(ell(81.5, ey, r * 0.55, r * 0.8), c, 'f', False), L(ell(82, ey, 1.4, 1.6), BLACK, 'f', False)]


def teeth(y=92, w=10, h=6):
    """Dientes apretados (boca ancha con la fila de dientes)."""
    pts = [(50 - w, y - h / 2), (50 + w, y - h / 2), (50 + w * 0.85, y + h / 2), (50 - w * 0.85, y + h / 2)]
    return [L(pts, WHITE, 'f', False, True), L([(50 - w * 0.9, y), (50 + w * 0.9, y)], OUTC, 'f', False, False, 0.9)]


def teeth_side(y=92):
    return [L([(79, y - 3), (87, y - 3), (86, y + 3), (79, y + 3)], WHITE, 'f', False, True)]


def blush(y=86, dx=22, r=4.6, c=(240, 140, 130, 255)):
    return [L(ell(50 - dx, y, r, r * 0.7), c, 'f', False), L(ell(50 + dx, y, r, r * 0.7), c, 'f', False)]


def eyepatch(view, x=64, y=75, c=BLACK, strap=True):
    if view == 'front':
        out = [L(blob([(x - 9, y - 7), (x + 9, y - 7), (x + 9, y + 5), (x, y + 9), (x - 9, y + 5)], 4), c, 'f')]
        if strap:
            out.append(L([(x - 6, y - 6), (20, 52)], c, 'f', False, False, 1.6))
            out.append(L([(x + 6, y - 6), (86, 60)], c, 'f', False, False, 1.6))
        return out
    if view == 'side':
        return [L(blob([(76, y - 7), (88, y - 6), (88, y + 6), (78, y + 7)], 4), c, 'f'), L([(76, y - 4), (20, y - 14)], c, 'f', False, False, 1.6)]
    return [L(quad((8, y - 18), (50, y - 22), (92, y - 18)), c, 'f', False, False, 1.6)]


def face_paint(pts, c):
    return L(blob(pts, 4), c, 'f', False)


def ear_ring(x=86, y=82, c=(200, 200, 210, 255)):
    return L(ell(x, y, 2.4, 2.4) + [ell(x, y, 2.4, 2.4)[0]], c, 'f', False, False, 1.4)


# ------------------------------------------------------------------------------------------------------------ 01-08

# Jack Alltrade: pelo azul petróleo liso con un mechón grande que se levanta en punta hacia su izquierda y dos mechones
# largos que le caen junto a la cara hasta la barbilla; ojos rosas afilados, cejas fruncidas, boca seria
C('jack-alltrade', 'normal', P('#587c90', '#fcebbc', '#c070b0'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=[(8, 66), (18, 52), (30, 44), (42, 54, 1), (50, 44), (62, 40), (76, 46), (86, 58), (92, 66)]),
  dome('front', top=8, w=44, cy=46, sb=66, seed=3) + [lock([(56, 14), (74, 4), (100, -10, 1), (90, 8), (98, 22, 1), (80, 22), (62, 24)]),
                                                     lock([(36, 20), (54, 18), (44, 34), (40, 56, 1), (34, 36)])] + sidelocks(104, (16, 84), 10),
  dome('side', top=8, w=44, cy=46, nape=86, fr=50, seed=3) + [lock([(46, 10), (70, 2), (96, -12, 1), (86, 8), (90, 22, 1), (70, 20)]), side_lock_s(104)],
  dome('back', top=8, w=44, cy=46, nape=88, seed=3) + [lock([(56, 12), (76, 2), (100, -12, 1), (88, 10)])])

# Jack O'Nonne: cabeza rapada con una franja morada de pelo en medio (cresta corta) rematada por un moño de cuerda blanca;
# una trenza blanca le baja por el lado izquierdo hasta una bola morada; ojos afilados y media sonrisa
PU, ROPE = _c('#6e5885'), _c('#efe6dc')
C('jack-o-nonne', 'normal', P('#6e5885', '#fdd28b', '#302232', rope='#efe6dc', ball='#59175a'),
  F(eyes='sharp', mouth='smile', mouth_y=93, hairline=False),
  [L(blob([(18, 58), (16, 34), (28, 14), (50, 6), (72, 14), (84, 34), (82, 58)], 8), 'skin'),
   lock([(38, 54), (34, 30), (40, 10), (50, 4), (60, 10), (66, 30), (62, 54), (56, 40), (44, 40)]),
   L(ell(50, 2, 9, 7), 'rope'), strand([(44, 0), (50, -4), (56, 2)], 'deep', 'f', 1.0),
   R((26, 26), (4, 60), (16, 100), 'rope', 11), L(ell(18, 104, 9, 8), 'ball', 'f'), strand([(10, 102), (26, 106)], 'mid', 'f', 2.0)],
  [L(blob([(44, 60), (30, 62), (10, 50), (6, 30), (20, 10), (46, 2), (72, 8), (86, 26), (88, 44), (70, 40), (54, 42)], 8), 'skin'),
   lock([(56, 40), (60, 12), (48, 0), (26, 4), (14, 20), (26, 26), (44, 22)]), L(ell(44, -2, 9, 7), 'rope')],
  [L(blob([(16, 76), (12, 42), (22, 16), (50, 6), (78, 16), (88, 42), (84, 76), (50, 84)], 8), 'skin'),
   lock([(40, 70), (38, 30), (44, 8), (56, 8), (62, 30), (60, 70), (50, 76)]), L(ell(50, 2, 9, 7), 'rope'),
   R((74, 26), (96, 60), (84, 100), 'rope', 11), L(ell(82, 104, 9, 8), 'ball', 'f')])

# Jack Skipper (portero): sombrero pirata negro azulado con calavera y tibias, pañuelo rojo debajo, mechones rubios que
# asoman por los lados, un parche en su ojo izquierdo y un monóculo en el derecho; piel tostada y boca seria
HAT, SKULLC, BAND = _c('#26454e'), _c('#d8d0bc'), _c('#8a2e34')
C('jack-skipper', 'normal', P('#e8b850', '#c7956a', '#302232', hat='#26454e', band='#8a2e34'),
  F(eyes='normal', mouth='frown', mouth_y=94, hairline=(58, 56)),
  [lock([(14, 70), (10, 52), (24, 54), (22, 66)], 'mid', 'b'), lock([(86, 70), (90, 52), (76, 54), (78, 66)], 'mid', 'b'),
   lock([(10, 92), (6, 70), (16, 56), (22, 72), (20, 88, 1)]), lock([(90, 92), (94, 70), (84, 56), (78, 72), (80, 88, 1)]),
   L(blob([(14, 58), (30, 50), (50, 48), (70, 50), (86, 58), (86, 66), (50, 60), (14, 66)], 4), 'band', 'f'),
   L(outline([(-14, 50), (8, 28), (28, 8), (50, 2), (72, 8), (92, 28), (114, 50), (84, 46), (50, 40), (16, 46)]), 'hat', 'f'),
   L(ell(50, 26, 8, 7), SKULLC, 'f', False), L([(38, 18), (62, 36)], SKULLC, 'f', False, False, 3.0), L([(62, 18), (38, 36)], SKULLC, 'f', False, False, 3.0),
   L(ell(47, 25, 1.6, 1.6), BLACK, 'f', False), L(ell(53, 25, 1.6, 1.6), BLACK, 'f', False)] +
  eyepatch('front', 64, 74, HAT) + [L(ell(36, 75, 8, 8) + [ell(36, 75, 8, 8)[0]], (190, 180, 150, 255), 'f', False, False, 1.6)],
  [lock([(56, 60), (62, 84), (54, 92, 1), (48, 70)]), lock([(10, 56), (4, 80, 1), (16, 74), (24, 58)]),
   L(blob([(4, 54), (40, 50), (86, 50), (86, 58), (40, 58), (4, 62)], 4), 'band', 'f'),
   L(outline([(-16, 54), (4, 30), (30, 6), (56, 2), (80, 14), (104, 46), (80, 42), (40, 40)]), 'hat', 'f'), L(ell(46, 26, 6, 6), SKULLC, 'f', False)] +
  eyepatch('side', 0, 74, HAT),
  [lock([(10, 92), (6, 70), (20, 56), (80, 56), (94, 70), (90, 92), (70, 84), (50, 88), (30, 84)]),
   L(blob([(10, 60), (50, 52), (90, 60), (90, 68), (50, 62), (10, 68)], 4), 'band', 'f'),
   R((50, 62), (60, 76), (66, 88), 'band', 5),
   L(outline([(-14, 54), (8, 30), (28, 8), (50, 2), (72, 8), (92, 30), (114, 54), (84, 48), (50, 44), (16, 48)]), 'hat', 'f')])

# Jade Greene: melena larga rojo anaranjado con dos mechones gruesos que le caen por delante envueltos en cintas azul
# verdoso y celeste, y un lazo azul verdoso arriba; ojos verde azulado afilados, cejas fruncidas y boca seria
TEAL, SKY = _c('#3a6e7e'), _c('#7ccbd8')
def _bands(x, y0, n=3):
    return [L(blob([(x - 6, y0 + i * 9), (x + 6, y0 + i * 9 - 1), (x + 6, y0 + i * 9 + 4), (x - 6, y0 + i * 9 + 5)], 3), TEAL if i % 2 == 0 else SKY, 'f', False)
            for i in range(n)]


C('jade-greene', 'chica', P('#dc5f4b', '#e7c0a6', '#3a7a78'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(8, 66), (18, 50), (32, 44), (44, 56, 1), (50, 44), (58, 56, 1), (68, 44), (82, 50), (92, 66)]),
  dome('front', top=6, w=46, cy=46, long=100, seed=4) + [R((20, 56), (14, 84), (20, 116), 'mid', 10), R((80, 56), (86, 84), (80, 116), 'mid', 10)] +
  _bands(17, 80) + _bands(83, 80) +
  [L(outline([(30, 2), (14, -10, 1), (26, 4), (44, 4), (50, 10), (56, 4), (74, 4), (86, -10, 1), (70, 2), (56, 12), (44, 12)]), TEAL, 'f')],
  dome('side', top=6, w=46, cy=46, long=104, fr=50, seed=4) + [R((60, 56), (66, 84), (62, 116), 'mid', 10)] + _bands(63, 82) +
  [L(outline([(40, 2), (54, -10, 1), (52, 6), (66, 4), (56, 12)]), TEAL, 'f')],
  dome('back', top=6, w=46, cy=46, long=104, seed=4) + [L(outline([(30, 2), (14, -10, 1), (26, 4), (50, 8), (74, 4), (86, -10, 1), (70, 2), (50, 14)]), TEAL, 'f')])

# Janice Queen: melena larguísima celeste pálido que le tapa el ojo derecho con un flequillo largo; el otro ojo rojo con
# ojeras grises, labios grisáceos
GR = _c('#9aa0a8')
C('janice-queen', 'chica', P('#b4dce1', '#fcf1da', '#c02828'),
  F(eyes='round', brows=False, mouth='line', mouth_y=94, hairline=[(8, 64), (20, 48), (36, 44), (50, 46), (64, 48), (80, 50), (92, 64)]),
  dome('front', top=4, w=48, cy=46, long=128, flare=4, seed=5) +
  [lock([(8, 56), (16, 36), (40, 28), (62, 34), (60, 60), (57, 92), (52, 104, 1), (38, 104), (24, 100), (12, 88)]),
   L(ell(64, 78, 7, 5), GR, 'b', False), shade([(66, 10), (92, 40), (94, 120), (80, 110), (78, 60)])],
  dome('side', top=4, w=48, cy=46, long=130, fr=56, seed=5) + [lock([(60, 40), (88, 38), (90, 60), (80, 70), (70, 56)])],
  dome('back', top=4, w=48, cy=46, long=130, ends=5, seed=5))

# Jemima "Jelly" Ellison: gorro de medusa lila muy pálido con aros magenta alrededor y mechones magenta que asoman a los
# lados; ojos redondos azules y una sonrisa enorme de dientes
JEL, MAG = _c('#ece2ee'), _c('#b84f7a')
def _jelly(view):
    if view == 'front':
        pts = [(-4, 70), (0, 40), (16, 14), (50, 4), (84, 14), (100, 40), (104, 70), (84, 62), (66, 60), (50, 62), (34, 60), (16, 62)]
        rings = [(8, 50), (30, 34), (50, 28), (70, 34), (92, 50)]
    elif view == 'side':
        pts = [(-6, 74), (-2, 40), (16, 12), (50, 2), (80, 12), (98, 40), (98, 66), (80, 60), (50, 60), (20, 66)]
        rings = [(4, 50), (26, 30), (52, 26), (78, 34)]
    else:
        pts = [(-4, 72), (0, 40), (16, 14), (50, 4), (84, 14), (100, 40), (104, 72), (50, 70)]
        rings = [(10, 54), (30, 36), (50, 30), (70, 36), (90, 54)]
    out = [L(outline(pts), JEL, 'f')]
    for x, y in rings:
        out += [L(ell(x, y, 6, 7), MAG, 'f', False), L(ell(x, y, 3, 3.6), JEL, 'f', False)]
    return out


C('jemima-jelly-ellison', 'chica', P('#c05888', '#f3d4ba', '#4a7ac0'),
  F(eyes='round', brows=False, mouth='none', hairline=False),
  [L(blob([(4, 96), (6, 66), (22, 60), (26, 90)], 6)), L(blob([(96, 96), (94, 66), (78, 60), (74, 90)], 6))] + _jelly('front') + teeth(91, 14, 6),
  [L(blob([(14, 92), (6, 66), (40, 62), (44, 88)], 6))] + _jelly('side') + teeth_side(91),
  [L(blob([(6, 96), (4, 66), (96, 66), (94, 96), (50, 100)], 6))] + _jelly('back'))

# Jenral Gaim: pinchos azules hacia arriba con un mechón amarillo anaranjado enorme que sube curvado en punta; marcas
# azules en las mejillas, ojos naranjas afilados y sonrisa con colmillo
YO = _c('#f0aa38')
C('jenral-gaim', 'normal', P('#5b789e', '#f7bd7d', '#d07a10'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=93, hairline=hl(6, 64, 50, 58, jit=2, seed=7)),
  dome('front', top=10, w=46, cy=46, n=9, amp=10, sweep=0.2, sb=68, seed=7) +
  [lock([(44, 40), (40, 20), (50, 4), (66, -14), (72, -28, 1), (70, -10), (60, 8), (54, 30), (52, 46)], YO),
   face_paint([(26, 84), (34, 82), (34, 88), (28, 90)], _c('#4a6a9a')), face_paint([(74, 84), (66, 82), (66, 88), (72, 90)], _c('#4a6a9a'))],
  dome('side', top=10, w=46, cy=46, n=9, amp=10, sweep=0.2, nape=86, fr=52, seed=7) + [lock([(40, 20), (52, 2), (66, -14), (72, -26, 1), (66, -6), (56, 18)], YO)],
  dome('back', top=10, w=46, cy=46, n=9, amp=10, nape=88, seed=7) + [lock([(46, 20), (54, 2), (66, -14), (72, -26, 1), (64, 0), (56, 24)], YO)])

# Joe Leggit: pelo granate oscuro alborotado con dos pinchos como cuernos a los lados de la cabeza; piel tostada, ojos
# verdes afilados, cejas fruncidas, boca seria y un pendiente de aro en la oreja izquierda
C('joe-leggit', 'normal', P('#63202f', '#bb8c6c', '#7aa040'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=hl(6, 62, 50, 60, jit=2, seed=8)),
  dome('front', top=10, w=48, cy=48, n=10, amp=7, sb=70, seed=8) +
  [lock([(12, 30), (2, 8), (6, -6, 1), (16, 8), (24, 20)]), lock([(88, 30), (98, 8), (94, -6, 1), (84, 8), (76, 20)]), ear_ring(84, 80)],
  dome('side', top=10, w=48, cy=48, n=10, amp=7, nape=88, fr=54, seed=8) + [lock([(56, 20), (66, 2), (64, -10, 1), (52, 6), (44, 16)])],
  dome('back', top=10, w=48, cy=48, n=10, amp=7, nape=88, seed=8) +
  [lock([(12, 30), (2, 8), (6, -6, 1), (16, 8), (24, 20)]), lock([(88, 30), (98, 8), (94, -6, 1), (84, 8), (76, 20)])])

# ------------------------------------------------------------------------------------------------------------ 09-16

# Joe "Meister X" Bloggs: pelo celeste muy pálido en mechones de punta echados hacia atrás, con un mechón largo que le cae
# por la izquierda; parche gris en el ojo izquierdo, ojo morado y sonrisa
C('joe-meister-x-bloggs', 'normal', P('#b4d4ee', '#fbcf9f', '#6a50a0'),
  F(eyes='normal', mouth='smile', mouth_y=93, hairline=[(8, 66), (18, 48), (30, 40), (44, 46), (56, 38), (72, 44), (86, 56), (92, 66)]),
  dome('front', top=8, w=46, cy=46, n=7, amp=12, sweep=-0.6, sb=66, seed=9) +
  [lock([(30, -2), (4, -12, 1), (20, 6), (16, 20)]), lock([(70, 4), (92, -8, 1), (84, 12)]),
   lock([(12, 54), (20, 44), (26, 60), (18, 96), (12, 112, 1), (10, 80)])] + eyepatch('front', 64, 75, _c('#4a4a52')),
  dome('side', top=8, w=46, cy=46, n=7, amp=12, sweep=0.4, nape=86, fr=50, seed=9) + [lock([(30, 4), (2, -6, 1), (18, 14)])] +
  eyepatch('side', 0, 75, _c('#4a4a52')),
  dome('back', top=8, w=46, cy=46, n=7, amp=12, nape=88, seed=9) + [lock([(70, 4), (96, -8, 1), (84, 12)]), lock([(30, -2), (6, -12, 1), (20, 8)])] +
  eyepatch('back', 0, 75, _c('#4a4a52')))

# Johann Storm (portero): una mata enorme de pelo verde con un mechón grueso que le cruza la cara y le tapa los ojos, y
# unas gafas de mariposa de montura blanca con cristales verde lima encima; media sonrisa
LIME = _c('#c7f343')
def _bfly(view):
    if view == 'front':
        out = []
        for s in (-1, 1):
            out += [L(outline([(50 + s * 4, 40), (50 + s * 34, 28), (50 + s * 40, 30, 1), (50 + s * 32, 52), (50 + s * 8, 56)]), WHITE, 'f'),
                    L(blob([(50 + s * 10, 42), (50 + s * 30, 34), (50 + s * 28, 48), (50 + s * 12, 52)], 4), LIME, 'f', False)]
        return out
    return [L(outline([(74, 38), (96, 30), (100, 32, 1), (94, 52), (76, 54)]), WHITE, 'f'), L(blob([(80, 42), (94, 36), (92, 48), (80, 50)], 4), LIME, 'f', False)]


C('johann-storm', 'normal', P('#66a95b', '#f6dcc0', '#302232'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, hairline=(66, 60)),
  dome('front', top=-6, w=50, cy=44, n=11, amp=10, sweep=0.4, sb=76, seed=10) +
  [lock([(16, 50), (40, 46), (64, 56), (80, 70), (84, 86, 1), (68, 80), (50, 74), (30, 72), (18, 66)]), strand([(30, 56), (56, 64), (76, 80)], 'deep', 'f', 1.2)] +
  _bfly('front'),
  dome('side', top=-6, w=50, cy=44, n=11, amp=10, sweep=0.4, nape=90, fr=60, seed=10) +
  [lock([(56, 48), (84, 58), (96, 78, 1), (80, 76), (60, 70)])] + _bfly('side'),
  dome('back', top=-6, w=50, cy=44, n=11, amp=10, nape=92, seed=10))

# Jon Gleur: payaso con la cara pintada de blanco, nariz roja octogonal, círculos verde azulado en las mejillas y
# los ojos rodeados de negro; gorro cónico crema y dos mechones azul marino a los lados
CRM = _c('#f2e2a8')
C('jon-gleur', 'normal', P('#3d3c51', '#fcf4d0', '#302232'),
  F(eyes='dot', brows=False, mouth='none', hairline=False, face_front=face(w=4, chin=104)),
  [lock([(14, 60), (2, 50), (6, 34, 1), (18, 40), (28, 46)]), lock([(86, 60), (98, 50), (94, 34, 1), (82, 40), (72, 46)]),
   L(blob([(20, 54), (30, 40), (50, 36), (70, 40), (80, 54)], 6), 'skin'),
   L(outline([(30, 44), (36, 20), (46, 4), (54, -10, 1), (62, 10), (70, 44), (50, 48)]), CRM, 'f'), strand([(34, 36), (66, 36)], 'shade', 'f', 1.0),
   L(ell(36, 75, 6, 6), BLACK, 'f', False), L(ell(64, 75, 6, 6), BLACK, 'f', False), L(ell(36, 75, 3.6, 3.6), WHITE, 'f', False), L(ell(64, 75, 3.6, 3.6), WHITE, 'f', False),
   L(ell(36, 75, 1.6, 1.6), BLACK, 'f', False), L(ell(64, 75, 1.6, 1.6), BLACK, 'f', False),
   L(ell(50, 86, 7, 6.5, 8), RED, 'f', False, True), L(ell(26, 88, 4.6, 4.6), _c('#2aa8a0'), 'f', False), L(ell(74, 88, 4.6, 4.6), _c('#2aa8a0'), 'f', False),
   L(quad((42, 96), (50, 99), (58, 96)), OUTC, 'f', False, False, 1.4)],
  [lock([(52, 60), (46, 46), (54, 30, 1), (62, 44), (64, 58)]), L(blob([(20, 52), (24, 30), (50, 22), (76, 30), (84, 50)], 6), 'skin'),
   L(outline([(36, 42), (42, 18), (52, 2), (60, -10, 1), (66, 12), (74, 40), (56, 46)]), CRM, 'f'),
   L(ell(81, 75, 4, 5), BLACK, 'f', False), L(ell(82, 75, 2, 3), WHITE, 'f', False), L(ell(90, 86, 4, 5, 8), RED, 'f', False, True), L(ell(76, 88, 3.4, 3.4), _c('#2aa8a0'), 'f', False)],
  [lock([(14, 62), (2, 52), (6, 36, 1), (18, 42), (28, 48)]), lock([(86, 62), (98, 52), (94, 36, 1), (82, 42), (72, 48)]),
   L(outline([(30, 44), (36, 20), (46, 4), (54, -10, 1), (62, 10), (70, 44), (50, 48)]), CRM, 'f')])

# Jon Himmel: pelo celeste salvaje en mechones rizados de punta, con unas gafas azules de cristales blancos sobre los ojos
# y un mechón que le baja por el medio de la cara; sonrisa afilada de dientes
BLU = _c('#325cd9')
C('jon-himmel', 'normal', P('#80cff6', '#f0d4bc', '#2a4aa0'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, hairline=hl(6, 64, 52, 60, jit=3, seed=11)),
  dome('front', top=4, w=50, cy=46, n=10, amp=12, sb=70, seed=11, soft=True) +
  [L(blob([(22, 50), (50, 44), (78, 50), (80, 66), (66, 70), (50, 62), (34, 70), (20, 66)], 4), BLU, 'f'),
   L(ell(36, 58, 8, 7), WHITE, 'f', False), L(ell(64, 58, 8, 7), WHITE, 'f', False),
   lock([(46, 50), (54, 50), (52, 70), (50, 84, 1), (46, 66)])],
  dome('side', top=4, w=50, cy=46, n=10, amp=12, nape=88, fr=52, seed=11, soft=True) +
  [L(blob([(70, 50), (92, 48), (94, 66), (72, 66)], 4), BLU, 'f'), L(ell(84, 57, 6, 6), WHITE, 'f', False), L([(70, 56), (10, 50)], BLU, 'f', False, False, 2.0)],
  dome('back', top=4, w=50, cy=46, n=10, amp=12, nape=90, seed=11, soft=True) + [L(quad((6, 56), (50, 50), (94, 56)), BLU, 'f', False, False, 2.4)])

# Juan Avis: melena en casco azul oscuro con flequillo recto y puntas sobre las orejas; ojos amarillos afilados, cejas
# fruncidas y boca seria
C('juan-avis', 'normal', P('#49538e', '#f4d7b3', '#d8c020'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=False),
  bowl3('front', top=4, side=82, fringe=63),
  bowl3('side', top=4, nape=90, fringe=62),
  bowl3('back', top=4, nape=90))

# Keigo Tsunoda (su retrato es de la DS): pelo corto verde muy oscuro en pinchos revueltos; piel tostada, ojos de mirada
# de lado y media sonrisa de suficiencia
C('keigo-tsunoda', 'normal', P('#3f4d3a', '#f6bf7c', '#302232'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=hl(6, 62, 50, 58, jit=3, seed=12)),
  dome('front', top=10, w=46, cy=46, n=10, amp=8, sb=66, seed=12),
  dome('side', top=10, w=46, cy=46, n=10, amp=8, nape=86, fr=52, seed=12),
  dome('back', top=10, w=46, cy=46, n=10, amp=8, nape=86, seed=12))

# Keir Mudgeon: adulto de cara larga y pálida; pelo verde oliva muy oscuro en melena recta hasta la mandíbula con un
# mechón que le cae por la frente; ojos rojos entornados, nariz larga y boca seria
C('keir-mudgeon', 'delgado', P('#3e4734', '#e0d2b9', '#b02828'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=96, hairline=False, face_front=face(chin=106)),
  bowl3('front', top=6, side=96, fringe=58) + [lock([(42, 54), (52, 52), (54, 70), (50, 84, 1), (44, 68)]),
                                              L(quad((52, 70), (56, 84), (50, 88)), OUTC, 'f', False, False, 1.2),
                                              L(blob([(40, 92), (50, 90), (60, 92), (60, 95), (50, 93), (40, 95)], 3), 'deep', 'f', False),
                                              L(blob([(44, 101), (56, 101), (54, 107), (46, 107)], 3), 'deep', 'f', False)],
  bowl3('side', top=6, nape=96, fringe=60),
  bowl3('back', top=6, nape=98))

# Ken Dough: sombrero cónico de paja enorme que le tapa los ojos; asoma pelo castaño oscuro por debajo, pecas y boca
# pequeña
STRAW = _c('#c9a878')
def _straw(view):
    if view == 'front':
        return [L(outline([(-18, 66), (20, 30), (50, -2, 1), (80, 30), (118, 66), (50, 70)]), STRAW, 'f'),
                L(blob([(52, 2), (80, 32), (114, 64), (70, 66)], 4), 'hat_d', 'f', False)] + \
               [strand([(50, 2), (50 + k * 10, 66)], 'hat_d', 'f', 0.9) for k in (-5, -3, -1, 1, 3, 5)]
    if view == 'side':
        return [L(outline([(-24, 64), (16, 30), (48, -2, 1), (78, 30), (116, 62), (46, 68)]), STRAW, 'f')]
    return [L(outline([(-18, 66), (20, 30), (50, -2, 1), (80, 30), (118, 66), (50, 72)]), STRAW, 'f')] + \
        [strand([(50, 2), (50 + k * 10, 68)], 'hat_d', 'f', 0.9) for k in (-5, -3, -1, 1, 3, 5)]


C('ken-dough', 'normal', P('#322925', '#f2dcc6', '#302232', hat_d='#a1825e'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, hairline=False),
  [lock([(6, 84), (10, 60), (90, 60), (94, 84), (84, 76), (74, 84, 1), (64, 72), (36, 72), (26, 84, 1), (16, 76)], 'mid', 'f')] + _straw('front') +
  [L(ell(30, 82, 1, 1), _c('#a06040'), 'f', False), L(ell(34, 85, 1, 1), _c('#a06040'), 'f', False), L(ell(66, 82, 1, 1), _c('#a06040'), 'f', False),
   L(ell(70, 85, 1, 1), _c('#a06040'), 'f', False)],
  [lock([(4, 90), (6, 60), (56, 60), (52, 80), (40, 88), (24, 92)])] + _straw('side'),
  [lock([(6, 92), (8, 60), (92, 60), (94, 92), (70, 86), (50, 92), (30, 86)])] + _straw('back'))

# ------------------------------------------------------------------------------------------------------------ 17-24

# Ken Haddow: pinchos crema muy claros de punta hacia arriba, con un pañuelo azul grisáceo atado en la frente y las puntas
# al viento; ojos de anillo (blancos rodeados de negro), un arañazo en la mejilla y sonrisa
BAN = _c('#5e7c8c')
C('ken-haddow', 'normal', P('#ebe7d3', '#f8bc7f', '#302232'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=93, hairline=(62, 58)),
  dome('front', top=-4, w=44, cy=44, n=9, amp=16, sb=64, seed=17) + bandl('front', BAN, y=50, h=12) +
  [L(outline([(84, 58), (100, 54), (110, 62, 1), (98, 64), (106, 72, 1), (90, 68)]), BAN, 'f')] + spiral_eyes(75, 14, WHITE, 6) +
  [L([(74, 86), (78, 92)], _c('#a06040'), 'f', False, False, 1.0), L([(77, 85), (81, 91)], _c('#a06040'), 'f', False, False, 1.0)],
  dome('side', top=-4, w=44, cy=44, n=9, amp=16, nape=86, fr=52, seed=17) + bandl('side', BAN, y=50, h=12) +
  [L(outline([(6, 60), (-10, 62), (-18, 74, 1), (-6, 72), (-12, 84, 1), (4, 70)]), BAN, 'f')] + ring_eye_side(75, 6),
  dome('back', top=-4, w=44, cy=44, n=9, amp=16, nape=86, seed=17) + bandl('back', BAN, y=50, h=12) +
  [L(outline([(46, 60), (40, 76), (34, 90, 1), (48, 76), (56, 92, 1), (56, 66)]), BAN, 'f')])

# Kik O'Round: tupé rojo altísimo y plano por arriba, con mechones largos que le caen por los lados hasta los hombros;
# ojos amarillos afilados, sonrisa enorme de dientes y barbilla partida
C('kik-o-round', 'delgado', P('#9b0302', '#fdcf9d', '#e0c020'),
  F(eyes='sharp', brows='angry', mouth='none', hairline=[(8, 64), (20, 48), (36, 46), (50, 52), (64, 46), (80, 48), (92, 64)], face_front=face(chin=104, jaw=2)),
  [L(outline([(20, 56), (18, 20), (22, -14), (78, -14), (82, 20), (80, 56), (50, 50)])), shade([(60, -10), (78, -12), (80, 30), (70, 50)]),
   lock([(12, 58), (22, 54), (24, 80), (20, 108), (12, 122, 1), (8, 96)]), lock([(88, 58), (78, 54), (76, 80), (80, 108), (88, 122, 1), (92, 96)])] +
  teeth(93, 14, 7) + [L([(50, 100), (50, 104)], OUTC, 'f', False, False, 1.0)],
  [L(outline([(80, 50), (86, 20), (84, -14), (30, -14), (14, 10), (8, 40), (14, 76), (24, 96), (34, 108, 1), (44, 84), (54, 60), (66, 48)])),
   shade([(10, 30), (30, 40), (40, 80), (30, 100)])] + teeth_side(93),
  [L(outline([(16, 108), (10, 70), (14, 30), (20, -14), (80, -14), (86, 30), (90, 70), (84, 108), (70, 92), (50, 90), (30, 92)])),
   shade([(60, -10), (80, -12), (88, 70), (84, 104), (70, 90)])])

# Kingley "K. Black" Blackcrown (portero): pelo negro con dos puntas curvadas hacia arriba como cuernos, un pico que le
# baja por la frente hasta la nariz y una barba negra cerrada que le rodea la cara; piel tostada y ojos rosas
C('kingley-k-black-blackcrown', 'corpulento', P('#322f32', '#cc966c', '#c06080'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(8, 64), (20, 52), (36, 54), (46, 66), (50, 84, 1), (54, 66), (64, 54), (80, 52), (92, 64)],
    face_front=face(w=4, chin=104, jaw=3)),
  dome('front', top=10, w=48, cy=48, sb=66, seed=19) +
  [lock([(10, 36), (0, 14), (6, -6, 1), (14, 14), (24, 26)]), lock([(90, 36), (100, 14), (94, -6, 1), (86, 14), (76, 26)]),
   L(outline([(10, 70), (18, 78), (26, 98), (40, 104), (50, 98), (60, 104), (74, 98), (82, 78), (90, 70), (92, 96), (76, 116), (50, 122), (24, 116), (8, 96)]), 'mid', 'f'),
   L(blob([(38, 92), (50, 88), (62, 92), (60, 96), (50, 94), (40, 96)], 3), 'mid', 'f', False)],
  dome('side', top=10, w=48, cy=48, nape=86, fr=56, seed=19) + [lock([(52, 22), (58, 0), (54, -10, 1), (44, 6), (40, 18)]),
                                                              L(outline([(52, 70), (60, 86), (76, 98), (90, 94), (88, 108), (70, 120), (50, 114), (44, 92)]), 'mid', 'f')],
  dome('back', top=10, w=48, cy=48, nape=88, seed=19) +
  [lock([(10, 36), (0, 14), (6, -6, 1), (14, 14), (24, 26)]), lock([(90, 36), (100, 14), (94, -6, 1), (86, 14), (76, 26)])])

# Kingston "K. White" Whitebridge (portero): pelo blanco peinado en cúpula con un rizo gris en forma de C en medio, barba
# y patillas blancas que le rodean la cara; ojos azules, cejas fruncidas y boca torcida
WH = _c('#f0eee8')
C('kingston-k-white-whitebridge', 'corpulento', P('#eceae2', '#f7bb7f', '#7aa0c0'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(8, 66), (20, 54), (36, 50), (50, 54), (64, 50), (80, 54), (92, 66)], face_front=face(w=4, chin=104, jaw=2)),
  dome('front', top=2, w=48, cy=48, sb=70, seed=20) +
  [L(outline([(54, 10), (40, 12), (34, 26), (42, 38), (52, 38), (52, 32), (44, 30), (42, 22), (50, 18)]), _c('#6a6a66'), 'f'),
   L(outline([(10, 70), (16, 82), (24, 98), (40, 104), (50, 100), (60, 104), (76, 98), (84, 82), (90, 70), (94, 96), (76, 114), (50, 120), (24, 114), (6, 96)]), 'mid', 'f'),
   L(blob([(38, 91), (50, 87), (62, 91), (60, 95), (50, 92), (40, 95)], 3), 'mid', 'f', False)],
  dome('side', top=2, w=48, cy=48, nape=88, fr=56, seed=20) + [L(outline([(52, 70), (60, 86), (76, 98), (90, 94), (88, 108), (70, 118), (50, 112), (44, 90)]), 'mid', 'f')],
  dome('back', top=2, w=48, cy=48, nape=90, seed=20))

# Kit Cymbal: pelo naranja con dos coletas cortas en lo alto como pompones y flequillo en puntas; ojos verdes grandes y
# sonrisa
C('kit-cymbal', 'chica', P('#dd8053', '#fccfa0', '#5aa040'),
  F(eyes='big', mouth='smile', mouth_y=93, hairline=hl(5, 62, 50, 58, seed=21)),
  dome('front', top=10, w=46, cy=48, sb=70, seed=21) +
  [lock([(24, 20), (6, 2), (-4, 8, 1), (2, 22), (-2, 32, 1), (14, 30)]), lock([(76, 20), (94, 2), (104, 8, 1), (98, 22), (102, 32, 1), (86, 30)])],
  dome('side', top=10, w=46, cy=48, nape=88, fr=52, seed=21) + [lock([(40, 16), (30, -4), (20, -6, 1), (22, 8), (14, 18, 1), (28, 22)])],
  dome('back', top=10, w=46, cy=48, nape=88, seed=21) +
  [lock([(24, 20), (6, 2), (-4, 8, 1), (2, 22), (-2, 32, 1), (14, 30)]), lock([(76, 20), (94, 2), (104, 8, 1), (98, 22), (102, 32, 1), (86, 30)])])

# Kitty Spinster: media melena naranja con una diadema de orejas de gato azul grisácea; cara blanca con bigotes de gato
# pintados, ojos ámbar y azul y sonrisa
CAT = _c('#6c919c')
C('kitty-spinster', 'chica', P('#ea9b4a', '#fcf9de', '#d08030'),
  F(eyes='big', mouth='smile', mouth_y=94, hairline=[(8, 66), (18, 54), (34, 50), (50, 56), (66, 50), (82, 54), (92, 66)]),
  bowl3('front', top=8, side=96, fringe=56) + bandl('front', CAT, y=24, h=8, w=44) +
  [L(outline([(16, 30), (12, 6, 1), (32, 22)]), CAT, 'f'), L(outline([(84, 30), (88, 6, 1), (68, 22)]), CAT, 'f')] +
  [L([(22 + 4 * k, 86 + 2 * k), (32, 88)], _c('#4a6a7a'), 'f', False, False, 0.8) for k in (0, 1)] +
  [L([(78 - 4 * k, 86 + 2 * k), (68, 88)], _c('#4a6a7a'), 'f', False, False, 0.8) for k in (0, 1)],
  bowl3('side', top=8, nape=96, fringe=58) + bandl('side', CAT, y=22, h=8) + [L(outline([(44, 24), (50, 0, 1), (60, 22)]), CAT, 'f')],
  bowl3('back', top=8, nape=98) + bandl('back', CAT, y=24, h=8, w=44) +
  [L(outline([(16, 30), (12, 6, 1), (32, 22)]), CAT, 'f'), L(outline([(84, 30), (88, 6, 1), (68, 22)]), CAT, 'f')])

# Kyu Lightning: un tupé naranja tostado enorme enrollado hacia delante que le tapa un ojo, con un rayo castaño oscuro
# en el mechón; boca seria
C('kyu-lightning', 'normal', P('#be7203', '#e1d0b6', '#302232'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=(64, 52)),
  dome('front', top=-2, w=48, cy=44, sb=66, seed=23) +
  [lock([(14, 46), (30, 30), (56, 30), (80, 44), (86, 62), (78, 82, 1), (72, 66), (58, 60), (40, 52)]),
   L(outline([(56, 40), (70, 52), (64, 56), (88, 68, 1), (68, 64), (72, 76, 1), (60, 62), (64, 58), (52, 48)]), _c('#4a3020'), 'f')],
  dome('side', top=-2, w=48, cy=44, nape=86, fr=54, seed=23) +
  [lock([(50, 30), (80, 30), (98, 46), (100, 64, 1), (90, 56), (80, 52), (62, 48)]),
   L(outline([(80, 40), (92, 50), (86, 52), (98, 60, 1), (84, 56)]), _c('#4a3020'), 'f')],
  dome('back', top=-2, w=48, cy=44, nape=88, seed=23))

# Larga Thanlyfe: anciano calvo con melena blanca a los lados, orejas de punta, nariz grande, gafas redondas pequeñas
# de cristal oscuro y una sonrisa enorme de dientes en punta
C('larga-thanlyfe', 'normal', P('#dbdacf', '#fdf0d5', '#302232'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, face_front=face(w=4, chin=102, jaw=3)),
  [L(blob([(18, 58), (16, 34), (28, 14), (50, 6), (72, 14), (84, 34), (82, 58)], 8), 'skin'),
   lock([(14, 46), (4, 62), (2, 100), (10, 112, 1), (20, 96), (22, 66)], 'mid', 'b'), lock([(86, 46), (96, 62), (98, 100), (90, 112, 1), (80, 96), (78, 66)], 'mid', 'b'),
   L(outline([(14, 62), (-6, 52, 1), (12, 76)]), 'skin', 'f'), L(outline([(86, 62), (106, 52, 1), (88, 76)]), 'skin', 'f'),
   L([(30, 60), (40, 62)], OUTC, 'f', False, False, 1.2), L([(70, 60), (60, 62)], OUTC, 'f', False, False, 1.2),
   L(ell(38, 68, 4, 4), _c('#3a2a40'), 'f', False, True), L(ell(62, 68, 4, 4), _c('#3a2a40'), 'f', False, True),
   L(outline([(46, 64), (54, 64), (58, 84), (50, 88), (42, 84)]), 'skin_d', 'f', False, True)] + teeth(95, 16, 8) +
  [L([(50 - 12 + 4 * k, 91), (50 - 10 + 4 * k, 95), (50 - 8 + 4 * k, 91)], OUTC, 'f', False, False, 0.8) for k in range(6)],
  [L(blob([(44, 60), (30, 62), (10, 50), (6, 30), (20, 10), (46, 2), (72, 8), (86, 26), (88, 44), (70, 40), (54, 42)], 8), 'skin'),
   lock([(10, 40), (2, 70), (6, 104), (18, 108, 1), (30, 90), (40, 64), (30, 46)]), L(outline([(40, 64), (22, 54, 1), (44, 78)]), 'skin', 'f'),
   L(ell(82, 68, 3.4, 4), _c('#3a2a40'), 'f', False, True), L(outline([(84, 66), (96, 82), (86, 86)]), 'skin_d', 'f', False, True)] + teeth_side(95),
  [L(blob([(16, 76), (12, 42), (22, 16), (50, 6), (78, 16), (88, 42), (84, 76), (50, 84)], 8), 'skin'),
   lock([(10, 44), (2, 70), (6, 108), (30, 112), (50, 104), (70, 112), (94, 108), (98, 70), (90, 44), (70, 60), (50, 64), (30, 60)])])

# ------------------------------------------------------------------------------------------------------------ 25-32

# Larveo Antlion: gorro morado con dos cuernos curvos, faldones grises que le cuelgan por los lados de la cara y una
# máscara morada que le tapa la boca y la nariz; ojos blancos redondos y cejas de mal humor
PU2, GRY = _c('#705977'), _c('#a29a90')
C('larveo-antlion', 'normal', P('#a29a90', '#dee1d5', '#302232'),
  F(eyes='round', brows='angry', mouth='none', hairline=False),
  [L(outline([(4, 104), (2, 60), (14, 44), (86, 44), (98, 60), (96, 104), (82, 98), (80, 62), (20, 62), (18, 98)]), GRY, 'f'),
   L(blob([(22, 82), (50, 78), (78, 82), (76, 98), (62, 108), (50, 110), (38, 108), (24, 98)], 4), PU2, 'f'),
   L(outline([(6, 52), (-6, 30), (-4, 6, 1), (12, 26), (30, 16), (50, 14), (70, 16), (88, 26), (104, 6, 1), (106, 30), (94, 52), (50, 46)]), PU2, 'f'),
   L(blob([(52, 18), (86, 28), (96, 46), (70, 44)], 4), _c('#5a4860'), 'f', False)],
  [L(outline([(4, 100), (0, 60), (10, 44), (60, 44), (62, 70), (58, 104), (30, 108)]), GRY, 'f'),
   L(blob([(72, 82), (90, 80), (92, 96), (80, 108), (66, 104)], 4), PU2, 'f'),
   L(outline([(-4, 52), (-8, 28), (-14, 8, 1), (6, 22), (40, 14), (70, 18), (92, 30), (100, 10, 1), (104, 34), (96, 50), (50, 46)]), PU2, 'f')],
  [L(outline([(4, 104), (2, 60), (14, 40), (86, 40), (98, 60), (96, 104), (50, 110)]), GRY, 'f'),
   L(outline([(6, 52), (-6, 30), (-4, 6, 1), (12, 26), (30, 16), (50, 14), (70, 16), (88, 26), (104, 6, 1), (106, 30), (94, 52), (50, 46)]), PU2, 'f')])

# Lawrence Leepson (portero): gorro alto azul con cuadrícula blanca y el borde blanco, y debajo una melena azul marino muy
# oscura en mechones de punta que le llega a los hombros; ojos rojos afilados y media sonrisa
CAPB = _c('#3e9bdc')
def _grid_cap(view):
    if view == 'front':
        out = [L(outline([(14, 44), (16, 10), (30, -4), (70, -4), (84, 10), (86, 44), (50, 40)]), CAPB, 'f')]
        out += [strand([(14 + 12 * k, 2 + abs(k - 3) * 1.5), (16 + 11.4 * k, 42)], WHITE, 'f', 1.0) for k in range(1, 6)]
        out += [strand([(15, 22), (50, 18), (85, 22)], WHITE, 'f', 1.0)]
        out += [L(blob([(12, 40), (50, 34), (88, 40), (88, 50), (50, 44), (12, 50)], 4), WHITE, 'f')]
        return out
    if view == 'side':
        return [L(outline([(8, 46), (10, 8), (30, -6), (70, -4), (86, 10), (88, 42), (50, 40)]), CAPB, 'f'),
                strand([(10, 22), (50, 18), (87, 24)], WHITE, 'f', 1.0), L(blob([(6, 44), (50, 36), (90, 40), (90, 50), (50, 46), (6, 54)], 4), WHITE, 'f')]
    return [L(outline([(14, 46), (16, 10), (30, -4), (70, -4), (84, 10), (86, 46), (50, 42)]), CAPB, 'f'),
            strand([(15, 22), (50, 18), (85, 22)], WHITE, 'f', 1.0), L(blob([(12, 42), (50, 38), (88, 42), (88, 52), (50, 48), (12, 52)], 4), WHITE, 'f')]


C('lawrence-leepson', 'normal', P('#253950', '#fbe9ba', '#c02828'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=hl(6, 64, 50, 62, jit=2, seed=26)),
  dome('front', top=10, w=48, cy=48, n=10, amp=10, long=108, flare=8, seed=26) + _grid_cap('front'),
  dome('side', top=10, w=48, cy=48, n=10, amp=10, long=108, fr=56, seed=26) + _grid_cap('side'),
  dome('back', top=10, w=48, cy=48, n=10, amp=10, long=108, ends=4, seed=26) + _grid_cap('back'))

# Leafy Tryadd (portero): cabeza casi calva con tres brotes de pelo verde como hojas (uno arriba y uno a cada lado);
# orejas grandes, ojos castaños redondos grandes y sonrisa
C('leafy-tryadd', 'bajito', P('#7bb158', '#fdd18c', '#8a4a20'),
  F(eyes='big', mouth='smile', mouth_y=94, hairline=False, big_ears=2, ear_out=3),
  [L(blob([(18, 58), (16, 34), (28, 14), (50, 6), (72, 14), (84, 34), (82, 58)], 8), 'skin'),
   lock([(42, 18), (40, 2), (50, -14, 1), (60, 2), (58, 18), (50, 26)]), lock([(22, 30), (8, 14), (-6, 12, 1), (6, 26), (20, 38)]),
   lock([(78, 30), (92, 14), (106, 12, 1), (94, 26), (80, 38)]), strand([(50, -8), (50, 20)], 'deep', 'f', 1.0),
   lock([(40, 24), (50, 18), (58, 26), (52, 40, 1), (46, 30)])],
  [L(blob([(44, 60), (30, 62), (10, 50), (6, 30), (20, 10), (46, 2), (72, 8), (86, 26), (88, 44), (70, 40), (54, 42)], 8), 'skin'),
   lock([(40, 14), (42, -4), (52, -16, 1), (58, 0), (56, 16)]), lock([(20, 26), (4, 12), (-10, 12, 1), (4, 26), (18, 32)])],
  [L(blob([(16, 76), (12, 42), (22, 16), (50, 6), (78, 16), (88, 42), (84, 76), (50, 84)], 8), 'skin'),
   lock([(42, 18), (40, 2), (50, -14, 1), (60, 2), (58, 18), (50, 26)]), lock([(22, 30), (8, 14), (-6, 12, 1), (6, 26), (20, 38)]),
   lock([(78, 30), (92, 14), (106, 12, 1), (94, 26), (80, 38)])])

# Len Grayves: sombrero ancho azul petróleo oscuro de ala levantada, mechones celestes finos que le caen junto a la cara,
# gafas redondas de sol naranjas y una sonrisa grande de dientes; adulto de cara larga
HAT2 = _c('#45545c')
C('len-grayves', 'delgado', P('#6598a6', '#f9cea0', '#302232'),
  F(eyes='none', brows=False, mouth='none', hairline=False, face_front=face(chin=106)),
  [lock([(14, 50), (22, 50), (20, 90), (16, 106, 1), (10, 84)]), lock([(86, 50), (78, 50), (80, 90), (84, 106, 1), (90, 84)]),
   L(outline([(-14, 30), (-4, 22), (20, 30), (34, 10), (66, 10), (80, 30), (104, 22), (114, 30), (100, 46), (60, 54), (40, 54), (0, 46)]), HAT2, 'f'),
   L(blob([(56, 14), (80, 32), (108, 28), (98, 44), (62, 50)], 4), _c('#38464e'), 'f', False),
   L(ell(36, 72, 8, 7), _c('#f0a080'), 'f', False, True), L(ell(64, 72, 8, 7), _c('#f0a080'), 'f', False, True), L([(44, 71), (56, 71)], OUTC, 'f', False, False, 1.4)] +
  teeth(94, 14, 7),
  [lock([(56, 50), (62, 50), (62, 90), (58, 104, 1), (54, 84)]),
   L(outline([(-18, 34), (-8, 24), (14, 32), (28, 10), (66, 10), (84, 30), (106, 26), (112, 34), (96, 48), (50, 54), (0, 48)]), HAT2, 'f'),
   L(ell(84, 72, 6, 6.5), _c('#f0a080'), 'f', False, True), L([(78, 70), (40, 66)], OUTC, 'f', False, False, 1.2)] + teeth_side(94),
  [lock([(12, 50), (88, 50), (90, 90), (84, 104, 1), (70, 90), (50, 96), (30, 90), (16, 104, 1), (10, 90)]),
   L(outline([(-14, 30), (-4, 22), (20, 30), (34, 10), (66, 10), (80, 30), (104, 22), (114, 30), (100, 46), (60, 54), (40, 54), (0, 46)]), HAT2, 'f')])

# Leon Griffin: melena de león amarilla enorme en mechones de punta que le rodea toda la cara; piel naranja tostada,
# marcas castañas en la frente, ojos afilados y una tirita en la nariz
C('leon-griffin', 'normal', P('#f5df68', '#e8aa5f', '#6a5020'),
  F(eyes='sharp', brows=False, mouth='grin', mouth_y=94, hairline=hl(7, 60, 46, 58, jit=2, seed=29)),
  dome('front', top=0, w=52, cy=46, n=12, amp=12, long=116, flare=10, seed=29) +
  [L(blob([(36, 64), (42, 62), (42, 66), (36, 67)], 3), _c('#8a5a20'), 'f', False), L(blob([(64, 64), (58, 62), (58, 66), (64, 67)], 3), _c('#8a5a20'), 'f', False),
   L(blob([(42, 84), (58, 84), (58, 89), (42, 89)], 3), _c('#f4e8e0'), 'f', False, True)],
  dome('side', top=0, w=52, cy=46, n=12, amp=12, long=116, fr=54, seed=29),
  dome('back', top=0, w=52, cy=46, n=12, amp=12, long=116, ends=5, seed=29))

# Leon Proudler: melena enorme melocotón claro en mechones de punta que le cae por los lados; piel morena, ojos morados
# afilados y sonrisa de dientes; corpulento
C('leon-proudler', 'corpulento', P('#fed4ac', '#ce9369', '#6a40a0'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, hairline=[(8, 64), (20, 50), (36, 46), (50, 58, 1), (64, 46), (80, 50), (92, 64)]),
  dome('front', top=-4, w=52, cy=44, n=11, amp=14, long=118, flare=12, seed=30) +
  [lock([(36, 20), (50, 10), (64, 20), (56, 40), (50, 56, 1), (44, 40)]), lock([(8, 70), (18, 72), (12, 110), (4, 118, 1), (2, 90)]),
   lock([(92, 70), (82, 72), (88, 110), (96, 118, 1), (98, 90)])],
  dome('side', top=-4, w=52, cy=44, n=11, amp=14, long=118, fr=54, seed=30),
  dome('back', top=-4, w=52, cy=44, n=11, amp=14, long=118, ends=5, seed=30))

# Leroy Kingsley (portero): peluca de rulos grises a los lados con una corona dorada en lo alto; cara ancha y pálida,
# ojos pequeños de enfado y boca torcida; corpulento
GOLD = _c('#e0b040')
def _crown(y=4, w=18):
    return [L(outline([(50 - w, y + 12), (50 - w - 2, y - 4, 1), (50 - w / 2, y + 4), (50, y - 10, 1), (50 + w / 2, y + 4), (50 + w + 2, y - 4, 1), (50 + w, y + 12)]),
              GOLD, 'f'), L(blob([(50 - w, y + 8), (50 + w, y + 8), (50 + w, y + 13), (50 - w, y + 13)], 3), _c('#b08020'), 'f', False)]


C('leroy-kingsley', 'corpulento', P('#bcaea0', '#fde9b7', '#302232'),
  F(eyes='dot', brows='angry', mouth='frown', mouth_y=96, hairline=[(8, 62), (22, 46), (40, 40), (50, 40), (60, 40), (78, 46), (92, 62)], face_front=face(w=6, chin=104, jaw=3)),
  dome('front', top=10, w=46, cy=48, sb=64, seed=31, shade=False) +
  [L(ell(x, y, 9, 8), 'mid', 'f') for x, y in ((12, 60), (8, 76), (88, 60), (92, 76), (16, 44), (84, 44))] +
  [strand([(x - 4, y - 2), (x, y - 4), (x + 4, y), (x, y + 3)], 'deep', 'f', 1.0) for x, y in ((12, 60), (8, 76), (88, 60), (92, 76))] + _crown(4),
  dome('side', top=10, w=46, cy=48, nape=86, fr=50, seed=31, shade=False) +
  [L(ell(x, y, 9, 8), 'mid', 'f') for x, y in ((20, 60), (14, 76), (34, 70))] + [L(outline([(36, 16), (34, 0, 1), (46, 8), (56, -6, 1), (62, 8), (70, 0, 1), (70, 16)]), GOLD, 'f')],
  dome('back', top=10, w=46, cy=48, nape=88, seed=31, shade=False) +
  [L(ell(x, y, 9, 8), 'mid', 'f') for x, y in ((12, 60), (8, 76), (88, 60), (92, 76), (30, 80), (50, 82), (70, 80))] + _crown(4))

# Logan Armstrong: cara de gorila de pelaje castaño con una cresta amarilla en pinchos, marcas amarillas en las mejillas,
# mandíbula enorme y una mancha amarilla en forma de corona en la barbilla; corpulento
YEL = _c('#fcdf4c')
C('logan-armstrong', 'corpulento', P('#fcdf4c', '#be854c', '#302232'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=92, hairline=False, face_front=face(w=6, chin=108, jaw=6)),
  [L(blob([(14, 60), (12, 34), (26, 16), (50, 10), (74, 16), (88, 34), (86, 60)], 8), 'skin'),
   lock([(24, 34), (18, 10), (30, 14), (34, -6, 1), (44, 8), (52, -12, 1), (58, 6), (70, -4, 1), (70, 12), (82, 10), (78, 34), (50, 28)]),
   L(blob([(14, 62), (6, 66), (8, 84), (16, 84)], 4), 'skin_d', 'b'), L(blob([(86, 62), (94, 66), (92, 84), (84, 84)], 4), 'skin_d', 'b'),
   L(blob([(24, 80), (32, 82), (30, 96), (24, 92)], 3), YEL, 'f', False), L(blob([(76, 80), (68, 82), (70, 96), (76, 92)], 3), YEL, 'f', False),
   L(blob([(24, 88), (50, 84), (76, 88), (74, 106), (50, 112), (26, 106)], 6), 'skin_d', 'f', False, True),
   L(outline([(40, 104), (42, 96, 1), (46, 100), (50, 94, 1), (54, 100), (58, 96, 1), (60, 104)]), YEL, 'f', False)],
  [L(blob([(44, 60), (30, 62), (10, 50), (6, 30), (20, 10), (46, 2), (72, 8), (86, 26), (88, 44), (70, 40), (54, 42)], 8), 'skin'),
   lock([(30, 30), (28, 8), (40, 4), (46, -10, 1), (56, 4), (66, -4, 1), (70, 10), (80, 20), (60, 30)]),
   L(blob([(66, 86), (90, 84), (96, 100), (78, 112), (62, 106)], 6), 'skin_d', 'f', False, True)],
  [L(blob([(16, 76), (12, 42), (22, 16), (50, 6), (78, 16), (88, 42), (84, 76), (50, 84)], 8), 'skin'),
   lock([(24, 34), (18, 10), (30, 14), (34, -6, 1), (44, 8), (52, -12, 1), (58, 6), (70, -4, 1), (70, 12), (82, 10), (78, 34), (50, 28)])])

# ------------------------------------------------------------------------------------------------------------ 33-40

# Lora Fayre: dos coletas larguísimas que se rizan hacia fuera, azules por fuera y crema por dentro; un flequillo crema le
# tapa el ojo derecho y lleva un pasador de pulpo morado con ojos verdes; pecas, ojo morado y boca en o
LBL, LCR = _c('#1c5092'), _c('#ece6d6')
C('lora-fayre', 'chica', P('#1c5092', '#f0c8a0', '#7a5aa8', cream='#ece6d6', octo='#a888c8'),
  F(eyes='normal', brows=False, mouth='none', hairline=[(8, 64), (18, 50), (34, 44), (50, 46), (64, 48), (80, 50), (92, 64)]),
  dome('front', top=6, w=46, cy=46, sb=66, seed=33) +
  [L(outline([(16, 30), (-6, 20), (-14, 50), (-8, 90), (6, 110, 1), (2, 80), (4, 52), (14, 44)])), L(outline([(10, 40), (-4, 56), (-2, 90), (6, 104), (8, 70)]), 'cream', 'f'),
   L(outline([(84, 30), (106, 20), (114, 50), (108, 90), (94, 110, 1), (98, 80), (96, 52), (86, 44)])), L(outline([(90, 40), (104, 56), (102, 90), (94, 104), (92, 70)]), 'cream', 'f'),
   lock([(16, 52), (24, 36), (44, 30), (56, 40), (50, 60), (46, 86), (40, 98, 1), (30, 84), (22, 70)], 'cream'),
   L(ell(32, 18, 12, 9), 'octo', 'f'), L(ell(27, 18, 3, 3), _c('#4aa040'), 'f', False), L(ell(37, 18, 3, 3), _c('#4aa040'), 'f', False),
   L(ell(50, 94, 2.4, 3), OUTC, 'f', False)] + [L(ell(x, 86, 0.9, 0.9), _c('#a86040'), 'f', False) for x in (60, 63, 66)],
  dome('side', top=6, w=46, cy=46, nape=86, fr=50, seed=33) +
  [L(outline([(30, 30), (6, 24), (-6, 56), (-2, 96), (10, 114, 1), (8, 80), (12, 52), (28, 44)])), L(ell(36, 14, 10, 8), 'octo', 'f')],
  dome('back', top=6, w=46, cy=46, nape=88, seed=33) +
  [L(outline([(16, 30), (-6, 20), (-14, 50), (-8, 90), (6, 110, 1), (2, 80), (4, 52), (14, 44)])),
   L(outline([(84, 30), (106, 20), (114, 50), (108, 90), (94, 110, 1), (98, 80), (96, 52), (86, 44)])), L(ell(68, 18, 12, 9), 'octo', 'f')])

# Louisa Borde (portera): melena azul marino muy oscura que le envuelve la cabeza como una capucha y baja hasta enrollarse
# en el cuello; un mechón le tapa un ojo y el otro es enorme y redondo con iris rojo; sonrisa de dientes
C('louisa-borde', 'chica', P('#434762', '#e4d2b9', '#b02838'),
  F(eyes='none', brows=False, mouth='none', hairline=False),
  hood('front', 'mid', top=-2, w=2, low=110, face_hole=[(22, 100), (18, 70), (24, 50), (50, 44), (76, 50), (82, 70), (78, 100), (50, 106)]) +
  [lock([(26, 44), (60, 40), (82, 52), (84, 80), (78, 100), (70, 84), (64, 66), (40, 56)]),
   L(ell(36, 76, 9, 9), WHITE, 'f', False, True), L(ell(36, 76, 5, 5), _c('#b02838'), 'f', False), L(ell(36, 76, 2, 2), BLACK, 'f', False)] + teeth(95, 14, 6) +
  scarf('front', 'mid', 104, 14),
  hood('side', 'mid', top=-2, w=2) + [L(ell(82, 76, 5, 6), WHITE, 'f', False, True), L(ell(83, 76, 2.4, 3), _c('#b02838'), 'f', False)] + teeth_side(95) +
  scarf('side', 'mid', 104, 14),
  hood('back', 'mid', top=-2, w=2) + scarf('back', 'mid', 104, 14))

# Luca "Stag" Cervus: pelo gris azulado con dos mechones enormes curvados hacia arriba como cuernos de ciervo y cejas
# grises gruesas que le tapan la frente; ojos amarillos, nariz triangular y boca apretada; cara ancha morena, corpulento
C('luca-stag-cervus', 'corpulento', P('#acb3c0', '#ce986a', '#e0c020'),
  F(eyes='sharp', brows=False, mouth='none', hairline=False, face_front=face(w=8, chin=104, jaw=4)),
  [L(blob([(12, 60), (10, 34), (26, 16), (50, 10), (74, 16), (90, 34), (88, 60)], 8)),
   lock([(30, 24), (8, 14), (2, -10), (14, -22, 1), (12, -6), (22, 6), (40, 12)]), lock([(70, 24), (92, 14), (98, -10), (86, -22, 1), (88, -6), (78, 6), (60, 12)]),
   L(blob([(14, 62), (30, 54), (46, 64), (40, 70), (24, 68)], 4), 'mid', 'f'), L(blob([(86, 62), (70, 54), (54, 64), (60, 70), (76, 68)], 4), 'mid', 'f'),
   L([(44, 76), (56, 76), (50, 84)], 'skin_d', 'f', False, True)] + teeth(94, 12, 5),
  [L(blob([(44, 60), (30, 62), (10, 50), (6, 30), (20, 10), (46, 2), (72, 8), (86, 26), (88, 44), (70, 40), (54, 42)], 8)),
   lock([(50, 14), (60, -8), (50, -22, 1), (52, -6), (40, 8)]), L(blob([(66, 60), (88, 58), (88, 66), (70, 68)], 4), 'mid', 'f')] + teeth_side(94),
  [L(blob([(14, 76), (10, 40), (22, 16), (50, 8), (78, 16), (90, 40), (86, 76), (50, 86)], 8)),
   lock([(30, 24), (8, 14), (2, -10), (14, -22, 1), (12, -6), (22, 6), (40, 12)]), lock([(70, 24), (92, 14), (98, -10), (86, -22, 1), (88, -6), (78, 6), (60, 12)])])

# Lucan Thorpe: pelo pardo en pinchos altos como una corona, con un pico que le baja hasta la nariz; cara pálida, orejas
# grandes, ojos blancos redondos, dos colmillos y perilla; delgado
C('lucan-thorpe', 'delgado', P('#786b5a', '#e1d0b7', '#302232'),
  F(eyes='round', brows='angry', mouth='none', big_ears=2, hairline=[(8, 62), (18, 46), (32, 50), (44, 64), (50, 80, 1), (56, 64), (68, 50), (82, 46), (92, 62)],
    face_front=face(chin=106)),
  [L(outline([(16, 58), (6, 30), (-4, 0, 1), (18, 16), (28, -12, 1), (38, 6), (50, -22, 1), (62, 6), (72, -12, 1), (82, 16), (104, 0, 1), (94, 30), (84, 58), (50, 54)])),
   shade([(56, -10), (80, 14), (92, 36), (80, 56), (66, 40)]),
   L([(46, 94), (54, 94)], (130, 70, 50, 255), 'f', False, False, 1.4), L([(44, 94), (45, 98), (47, 94)], WHITE, 'f', False, True), L([(53, 94), (55, 98), (56, 94)], WHITE, 'f', False, True),
   L(outline([(46, 102), (54, 102), (50, 110, 1)]), 'mid', 'f')],
  [L(outline([(70, 46), (76, 34), (88, 22, 1), (70, 24), (66, -4, 1), (52, 10), (38, -18, 1), (32, 8), (12, -2, 1), (16, 22), (4, 40), (10, 62), (30, 62), (52, 50)])),
   L(outline([(84, 100), (90, 104), (86, 110, 1)]), 'mid', 'f')],
  [L(outline([(16, 62), (6, 30), (-4, 0, 1), (18, 16), (28, -12, 1), (38, 6), (50, -22, 1), (62, 6), (72, -12, 1), (82, 16), (104, 0, 1), (94, 30), (84, 62), (50, 70)])),
   shade([(56, -10), (80, 14), (92, 36), (80, 60), (66, 40)])])

# Lucian Sunfish: cabeza muy alargada con una cresta estrecha verde oliva en punta y franjas oliva hacia los lados; gafas
# amarillas enormes en forma de antifaz, boca pequeña en o y una perilla verde; delgado
OLV, YG = _c('#9eab74'), _c('#e2a508')
C('lucian-sunfish', 'delgado', P('#9eab74', '#cf986c', '#302232'),
  F(eyes='none', brows=False, mouth='none', hairline=False, face_front=face(w=-4, chin=110, top=14)),
  [L(blob([(22, 60), (22, 24), (36, 4), (50, -2), (64, 4), (78, 24), (78, 60)], 8), 'skin'),
   lock([(42, 30), (46, -6), (50, -24, 1), (54, -6), (58, 30), (50, 40)]), lock([(26, 40), (34, 14), (40, 18), (32, 52)]), lock([(74, 40), (66, 14), (60, 18), (68, 52)]),
   L(outline([(22, 66), (36, 58), (48, 64), (50, 70), (52, 64), (64, 58), (78, 66), (74, 80), (58, 82), (50, 76), (42, 82), (26, 80)]), YG, 'f'),
   L(ell(50, 92, 2.6, 3), OUTC, 'f', False), L(ell(50, 92, 1.2, 1.6), 'skin', 'f', False), L(outline([(46, 100), (54, 100), (50, 112, 1)]), 'mid', 'f')],
  [L(blob([(44, 60), (30, 62), (14, 50), (12, 26), (26, 4), (50, -2), (72, 6), (84, 26), (86, 44), (70, 40), (54, 42)], 8), 'skin'),
   lock([(42, 30), (42, 0), (50, -24, 1), (56, -2), (58, 30)]), L(outline([(70, 64), (90, 62), (92, 78), (74, 80)]), YG, 'f'),
   L(outline([(84, 100), (90, 104), (86, 112, 1)]), 'mid', 'f')],
  [L(blob([(22, 76), (20, 40), (30, 10), (50, -2), (70, 10), (80, 40), (78, 76), (50, 86)], 8), 'skin'),
   lock([(42, 40), (46, -6), (50, -24, 1), (54, -6), (58, 40), (50, 50)])])

# Lucius Lox (portero): mata de pelo verde oscuro con franjas blancas que se enrosca hacia un lado en un mechón enorme
# curvado, y un pico verde y blanco en la frente; piel morena, ojos rojizos y boca seria
WSTR = _c('#ece4dc')
C('lucius-lox', 'normal', P('#254d2b', '#a9846a', '#a04020'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(8, 64), (18, 50), (34, 50), (44, 60), (50, 72, 1), (56, 60), (66, 50), (82, 50), (92, 64)]),
  dome('front', top=4, w=46, cy=46, sb=68, seed=38) +
  [L(outline([(20, 30), (0, 22), (-12, 40), (-10, 70), (-2, 90, 1), (2, 66), (10, 50), (18, 44)])), L(outline([(-6, 44), (2, 34), (14, 36), (4, 52), (-2, 70)]), WSTR, 'f'),
   lock([(78, 50), (92, 60), (96, 88), (90, 110, 1), (86, 82), (80, 64)]), L(outline([(90, 66), (94, 82), (90, 96), (88, 76)]), WSTR, 'f'),
   L(outline([(40, 22), (50, 30), (60, 22), (58, 44), (50, 60, 1), (42, 44)]), WSTR, 'f'), strand([(30, 10), (50, 4), (70, 12)], WSTR, 'b', 3.0)],
  dome('side', top=4, w=46, cy=46, nape=88, fr=54, seed=38) + [strand([(20, 12), (50, 4), (84, 26)], WSTR, 'b', 3.0), L(outline([(66, 50), (78, 58), (76, 90), (70, 108, 1), (68, 80)]), 'mid', 'f')],
  dome('back', top=4, w=46, cy=46, nape=90, seed=38) + [strand([(30, 10), (50, 4), (70, 12)], WSTR, 'b', 3.0), strand([(20, 40), (50, 34), (80, 40)], WSTR, 'b', 3.0)])

# Luke Dwight (portero): cara redonda y mofletuda, pelo corto oscuro con rayas rapadas y un moñito arriba; ojos apretados
# de esfuerzo y dientes apretados; corpulento
C('luke-dwight', 'corpulento', P('#3b312a', '#be8c67', '#302232'),
  F(eyes='none', brows=False, mouth='none', hairline=(50, 44), face_front=face(w=8, chin=104, jaw=8)),
  dome('front', top=14, w=42, cy=48, sb=56, seed=39, shade=False) +
  [strand([(16, 46 - 4 * k), (50, 40 - 8 * k), (84, 46 - 4 * k)], 'skin_d', 'b', 1.4) for k in range(3)] +
  [L(ell(50, 12, 8, 7), 'mid'), L([(28, 72), (40, 76), (28, 80)], OUTC, 'f', False, False, 2.4), L([(72, 72), (60, 76), (72, 80)], OUTC, 'f', False, False, 2.4),
   L([(28, 64), (40, 68)], OUTC, 'f', False, False, 2.4), L([(72, 64), (60, 68)], OUTC, 'f', False, False, 2.4)] + teeth(93, 12, 7),
  dome('side', top=14, w=42, cy=48, nape=80, fr=46, seed=39, shade=False) + [L(ell(46, 12, 8, 7), 'mid'), L([(76, 72), (86, 76)], OUTC, 'f', False, False, 2.4)] + teeth_side(93),
  dome('back', top=14, w=42, cy=48, nape=82, seed=39, shade=False) + [strand([(14, 50 - 6 * k), (50, 46 - 8 * k), (86, 50 - 6 * k)], 'skin_d', 'b', 1.4) for k in range(3)] +
  [L(ell(50, 12, 8, 7), 'mid')])

# Luna Reid: melena larga y lisa azul marino con un rizo blanco en lo alto; ojos rojos, mejillas coloradas redondas y
# sonrisa
C('luna-reid', 'chica', P('#333065', '#fabc7c', '#c02828'),
  F(eyes='normal', mouth='smile', mouth_y=93, hairline=[(8, 64), (18, 48), (32, 42), (50, 50), (68, 42), (82, 48), (92, 64)]),
  dome('front', top=8, w=46, cy=48, long=114, flare=2, seed=40) +
  [L(outline([(44, 26), (36, 8), (50, -2), (66, 4), (68, 18), (58, 22), (52, 12), (46, 16), (52, 30)]), _c('#e4dcea'), 'f')] + blush(86, 22, 5, _c('#e04848')),
  dome('side', top=8, w=46, cy=48, long=116, fr=52, seed=40) + [L(outline([(52, 20), (52, 2), (66, -2), (74, 8), (64, 14)]), _c('#e4dcea'), 'f')],
  dome('back', top=8, w=46, cy=48, long=116, ends=4, seed=40) + [L(outline([(44, 20), (40, 4), (54, -2), (62, 8)]), _c('#e4dcea'), 'f')])

# ------------------------------------------------------------------------------------------------------------ 41-48

# Lykan Moss (portero): una mata de musgo verde que le tapa toda la cabeza menos un recuadro de cara castaña con una
# franja amarilla por ceja, ojos blancos redondos y la boca pequeña
MOSS = _c('#5a7215')
C('lykan-moss', 'normal', P('#5a7215', '#c18e3c', '#302232'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  [L(outline([(-6, 70), (-8, 40), (4, 12), (26, -2), (50, -6), (74, -2), (96, 12), (108, 40), (106, 70), (100, 96), (80, 112), (50, 116), (20, 112), (0, 96)]), MOSS),
   shade([(60, -2), (96, 16), (104, 60), (96, 100), (74, 108), (80, 60)])] +
  [L(ell(x, y, 7, 6), 'shade', 'f', False) for x, y in ((14, 30), (30, 16), (80, 40), (10, 70), (88, 84), (20, 100))] +
  [L(blob([(32, 56), (68, 56), (68, 96), (32, 96)], 3), 'skin', 'f', False, True), L(blob([(30, 54), (70, 54), (70, 60), (30, 60)], 2), _c('#f0d040'), 'f', False, True),
   L(ell(40, 68, 5, 5), WHITE, 'f', False, True), L(ell(60, 68, 5, 5), WHITE, 'f', False, True), L(ell(40, 68, 2, 2), BLACK, 'f', False), L(ell(60, 68, 2, 2), BLACK, 'f', False),
   L(blob([(36, 78), (64, 78), (64, 96), (36, 96)], 3), _c('#c07030'), 'f', False), L([(46, 88), (54, 88)], OUTC, 'f', False, False, 1.2)],
  [L(outline([(-6, 70), (-8, 40), (4, 12), (26, -2), (50, -6), (74, -2), (96, 12), (106, 40), (104, 70), (98, 96), (80, 112), (50, 116), (20, 112), (0, 96)]), MOSS),
   L(blob([(80, 56), (100, 56), (100, 96), (80, 96)], 3), 'skin', 'f', False, True), L(ell(92, 68, 3.4, 4.6), WHITE, 'f', False, True)],
  [L(outline([(-6, 70), (-8, 40), (4, 12), (26, -2), (50, -6), (74, -2), (96, 12), (108, 40), (106, 70), (100, 96), (80, 112), (50, 116), (20, 112), (0, 96)]), MOSS)] +
  [L(ell(x, y, 7, 6), 'shade', 'f', False) for x, y in ((14, 30), (40, 20), (70, 50), (30, 80), (80, 90))])

# Lynne Wildcat: pelo gris azulado con dos puntas de oreja de gato arriba y mechones que se curvan hacia fuera junto a la
# cara; cara muy blanca con marcas verde oscuro alrededor de los ojos y de la boca, ojos afilados y media sonrisa
MRK = _c('#2e5048')
C('lynne-wildcat', 'chica', P('#95aaac', '#fdf7e0', '#302232'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=94, hairline=[(8, 64), (20, 50), (34, 44), (50, 54, 1), (66, 44), (80, 50), (92, 64)]),
  dome('front', top=10, w=44, cy=48, sb=68, seed=41) +
  [lock([(24, 22), (14, -2, 1), (34, 12)]), lock([(76, 22), (86, -2, 1), (66, 12)]),
   lock([(14, 56), (20, 60), (16, 88), (2, 104, 1), (6, 84)]), lock([(86, 56), (80, 60), (84, 88), (98, 104, 1), (94, 84)]),
   face_paint([(22, 70), (28, 66), (26, 76), (30, 84), (24, 80)], MRK), face_paint([(78, 70), (72, 66), (74, 76), (70, 84), (76, 80)], MRK),
   face_paint([(36, 96), (42, 94), (40, 100)], MRK), face_paint([(64, 96), (58, 94), (60, 100)], MRK)],
  dome('side', top=10, w=44, cy=48, nape=88, fr=54, seed=41) + [lock([(48, 20), (56, -4, 1), (64, 16)]), lock([(58, 58), (62, 62), (58, 90), (46, 104, 1), (50, 84)])],
  dome('back', top=10, w=44, cy=48, nape=90, seed=41) +
  [lock([(24, 22), (14, -2, 1), (34, 12)]), lock([(76, 22), (86, -2, 1), (66, 12)]),
   lock([(14, 56), (20, 60), (16, 88), (2, 104, 1), (6, 84)]), lock([(86, 56), (80, 60), (84, 88), (98, 104, 1), (94, 84)])])

# Magnus "Baboon" Aype: pelo castaño como pelaje con dos bultos redondos arriba y patillas espesas; cara morena ancha,
# cicatriz en la mejilla, ojos pequeños de enfado y boca torcida; corpulento
C('magnus-baboon-aype', 'corpulento', P('#6c5510', '#b88d6d', '#302232'),
  F(eyes='dot', brows='angry', mouth='frown', mouth_y=96, hairline=[(8, 66), (20, 52), (36, 50), (50, 54), (64, 50), (80, 52), (92, 66)], face_front=face(w=6, chin=106, jaw=4)),
  dome('front', top=10, w=48, cy=48, sb=86, seed=42) + [L(ell(22, 14, 10, 9)), L(ell(78, 14, 10, 9)),
                                                       L(blob([(44, 70), (56, 70), (60, 86), (50, 90), (40, 86)], 4), 'skin_d', 'f', False, True),
                                                       L([(66, 78), (72, 92)], _c('#8a5a40'), 'f', False, False, 1.2)],
  dome('side', top=10, w=48, cy=48, nape=90, fr=56, seed=42) + [L(ell(40, 10, 10, 9))],
  dome('back', top=10, w=48, cy=48, nape=90, seed=42) + [L(ell(22, 14, 10, 9)), L(ell(78, 14, 10, 9))])

# Manny Saboy: tupé coral abultado que le cae por los lados de la cara; piel anaranjada, ojos de espiral y dientes
# apretados
C('manny-saboy', 'normal', P('#d96a52', '#eca763', '#302232'),
  F(eyes='none', brows='angry', mouth='none', hairline=(60, 48)),
  dome('front', top=-2, w=48, cy=44, sb=96, seed=43) + spiral_eyes(76, 14, _c('#f0f0d0'), 6.5) + teeth(94, 10, 6),
  dome('side', top=-2, w=48, cy=44, nape=92, fr=52, seed=43) + ring_eye_side(76, 6, _c('#f0f0d0')) + teeth_side(94),
  dome('back', top=-2, w=48, cy=44, nape=94, seed=43))

# Marcus Maan: pelo negro verdoso revuelto con mechones rizados como cuernos; parche rojo con forma de corazón en el ojo
# izquierdo, el otro ojo azul redondo; orejas de punta, cara larga y pálida, bigote rizado y dientes apretados; delgado
C('marcus-maan', 'delgado', P('#2b2e1c', '#e5d1b7', '#5a8ac0'),
  F(eyes='none', brows=False, mouth='none', hairline=hl(6, 58, 44, 52, jit=3, seed=44), ears=False, face_front=face(chin=108)),
  dome('front', top=12, w=42, cy=46, n=8, amp=8, sb=60, seed=44) +
  [lock([(18, 30), (6, 12), (12, -2, 1), (16, 14), (26, 22)]), lock([(82, 30), (94, 12), (88, -2, 1), (84, 14), (74, 22)]),
   L(outline([(16, 62), (-4, 54, 1), (14, 78)]), 'skin', 'f'), L(outline([(84, 62), (104, 54, 1), (86, 78)]), 'skin', 'f'),
   L(ell(36, 74, 6, 6), WHITE, 'f', False, True), L(ell(36, 74, 3, 3), _c('#5a8ac0'), 'f', False), L(ell(36, 74, 1.4, 1.4), BLACK, 'f', False),
   L(blob([(56, 66), (64, 64), (72, 66), (74, 76), (64, 86), (56, 76)], 4), _c('#b81c28'), 'f', False, True), L([(56, 66), (30, 52)], BLACK, 'f', False, False, 1.4),
   L(quad((32, 92), (42, 86), (50, 90)) + quad((50, 90), (58, 86), (68, 92))[1:], 'mid', 'f', False, False, 2.0)] + teeth(96, 9, 5),
  dome('side', top=12, w=42, cy=46, n=8, amp=8, nape=84, fr=50, seed=44) +
  [lock([(48, 16), (56, -2), (50, -8, 1), (42, 6)]), L(outline([(44, 62), (26, 54, 1), (44, 76)]), 'skin', 'f'),
   L(ell(81, 74, 4, 5), _c('#b81c28'), 'f', False, True), L([(78, 70), (20, 58)], BLACK, 'f', False, False, 1.4)] + teeth_side(96),
  dome('back', top=12, w=42, cy=46, n=8, amp=8, nape=86, seed=44) +
  [lock([(18, 30), (6, 12), (12, -2, 1), (16, 14), (26, 22)]), lock([(82, 30), (94, 12), (88, -2, 1), (84, 14), (74, 22)]), L(quad((8, 56), (50, 50), (92, 56)), BLACK, 'f', False, False, 1.4)])

# Mariposa Papillon: pelo crema muy claro, liso y por los hombros, con un lazo enorme de alas de mariposa en lo alto,
# crema con franjas amarillas, y una diadema amarilla; ojos entornados de sueño, cejas en dos puntos y boca pequeña
YSTR = _c('#e3c84d')
def _bow(view):
    if view == 'front':
        return [L(outline([(48, 10), (24, -14), (8, -10, 1), (14, 14), (36, 22)]), _c('#f8f0d0'), 'f'), L(outline([(52, 10), (76, -14), (92, -10, 1), (86, 14), (64, 22)]), _c('#f8f0d0'), 'f'),
                strand([(14, -6), (32, 14)], YSTR, 'f', 3.0), strand([(86, -6), (68, 14)], YSTR, 'f', 3.0), L(ell(50, 12, 6, 6), _c('#f8f0d0'), 'f')]
    if view == 'side':
        return [L(outline([(44, 12), (30, -12), (20, -8, 1), (24, 14)]), _c('#f8f0d0'), 'f'), strand([(24, -4), (34, 10)], YSTR, 'f', 3.0)]
    return _bow('front')


C('mariposa-papillon', 'chica', P('#f6eecc', '#fbe0c0', '#302232'),
  F(eyes='closed', brows=False, mouth='line', mouth_y=95, hairline=[(8, 64), (20, 52), (34, 46), (50, 50), (66, 46), (80, 52), (92, 64)]),
  dome('front', top=8, w=46, cy=48, long=104, flare=4, seed=46) + bandl('front', YSTR, y=34, h=5, w=44) + _bow('front') +
  [L(ell(36, 72, 6, 3.4), WHITE, 'f', False), L(ell(64, 72, 6, 3.4), WHITE, 'f', False), L(ell(36, 72, 2.6, 3), BLACK, 'f', False), L(ell(64, 72, 2.6, 3), BLACK, 'f', False),
   L([(29, 70), (43, 70)], OUTC, 'f', False, False, 2.2), L([(57, 70), (71, 70)], OUTC, 'f', False, False, 2.2),
   L(ell(42, 60, 1.6, 1.6), _c('#c0a060'), 'f', False), L(ell(58, 60, 1.6, 1.6), _c('#c0a060'), 'f', False)],
  dome('side', top=8, w=46, cy=48, long=106, fr=54, seed=46) + bandl('side', YSTR, y=32, h=5) + _bow('side'),
  dome('back', top=8, w=46, cy=48, long=106, ends=4, seed=46) + _bow('back'))

# Martin Fleet (portero): pelo gris peinado hacia un lado con una onda arriba y mechones largos junto a la cara; ojos
# azules afilados, cejas fruncidas y boca seria
C('martin-fleet', 'normal', P('#b3aba7', '#fde4cc', '#5a8ac0'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=94, hairline=[(8, 64), (18, 48), (30, 42), (46, 50), (62, 40), (78, 46), (92, 64)]),
  dome('front', top=6, w=44, cy=46, sb=66, seed=47) + [lock([(60, 10), (84, 10), (98, 22, 1), (84, 22), (70, 30)]), lock([(30, 16), (54, 22), (40, 40), (34, 56, 1), (28, 34)])] +
  sidelocks(104, (17, 83), 7),
  dome('side', top=6, w=44, cy=46, nape=86, fr=50, seed=47) + [lock([(56, 8), (84, 10), (96, 22, 1), (80, 22)]), side_lock_s(104)],
  dome('back', top=6, w=44, cy=46, nape=88, seed=47) + [lock([(40, 10), (16, 10), (2, 22, 1), (16, 22)])])

# Maude Erne: melena verde oscura que baja por los lados y se recoge en dos rodetes junto a las mejillas; piel tostada,
# un punto negro en la frente, ojos morados con pestañas y media sonrisa
C('maude-erne', 'chica', P('#306352', '#eda762', '#8a5aa0'),
  F(eyes='sharp', mouth='smile', mouth_y=94, hairline=[(8, 64), (20, 46), (38, 40), (50, 44), (62, 40), (80, 46), (92, 64)]),
  dome('front', top=6, w=46, cy=46, long=112, flare=0, seed=48) +
  [L(ell(10, 84, 11, 13)), L(ell(90, 84, 11, 13)), strand([(4, 80), (14, 78), (16, 90)], 'deep', 'f', 1.0), strand([(96, 80), (86, 78), (84, 90)], 'deep', 'f', 1.0),
   L(ell(50, 60, 1.8, 1.8), BLACK, 'f', False)],
  dome('side', top=6, w=46, cy=46, long=112, fr=52, seed=48) + [L(ell(42, 86, 12, 14))],
  dome('back', top=6, w=46, cy=46, long=112, ends=4, seed=48) + [L(ell(10, 84, 11, 13)), L(ell(90, 84, 11, 13))])

# ------------------------------------------------------------------------------------------------------------ 49-56

# Maya O'Pier: melena larga rosa muy pálido con una diadema oscura y un antifaz rojo de cristales grises que le tapa los
# ojos; boca seria
VIS = _c('#c82830')
C('maya-o-pier', 'chica', P('#f2dcdc', '#fdefd4', '#302232'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=95, hairline=[(8, 64), (20, 50), (36, 46), (50, 48), (64, 46), (80, 50), (92, 64)]),
  dome('front', top=6, w=46, cy=46, long=118, flare=2, seed=49) + bandl('front', _c('#4a3f3a'), y=18, h=5, w=44) +
  [L(outline([(22, 66), (40, 62), (50, 70), (60, 62), (78, 66), (74, 82), (58, 84), (50, 78), (42, 84), (26, 82)]), VIS, 'f'),
   L(blob([(28, 68), (42, 66), (46, 74), (40, 80), (28, 78)], 4), _c('#5a5a60'), 'f', False), L(blob([(72, 68), (58, 66), (54, 74), (60, 80), (72, 78)], 4), _c('#5a5a60'), 'f', False),
   L([(42, 60), (48, 64)], OUTC, 'f', False, False, 1.0), L([(58, 60), (52, 64)], OUTC, 'f', False, False, 1.0)],
  dome('side', top=6, w=46, cy=46, long=120, fr=54, seed=49) + bandl('side', _c('#4a3f3a'), y=16, h=5) +
  [L(outline([(70, 64), (92, 62), (94, 80), (72, 82)]), VIS, 'f'), L(blob([(78, 66), (90, 66), (90, 78), (78, 78)], 4), _c('#5a5a60'), 'f', False)],
  dome('back', top=6, w=46, cy=46, long=120, ends=4, seed=49) + bandl('back', _c('#4a3f3a'), y=18, h=5, w=44) + [L(quad((6, 70), (50, 66), (94, 70)), VIS, 'f', False, False, 2.0)])

# Mel O'Drahma: pelo negro en media melena con flequillo recto y un moño en lo alto atado con una cinta amarilla; piel
# tostada, ojos amarillos grandes y una sonrisa pequeña
C('mel-o-drahma', 'chica', P('#2c3433', '#e8b47a', '#e0b020'),
  F(eyes='big', mouth='smile', mouth_y=94, hairline=False),
  bowl3('front', top=8, side=94, fringe=62) + [L(ell(50, 4, 11, 9)), L(blob([(44, 12), (56, 12), (56, 15), (44, 15)], 2), _c('#e0c040'), 'f', False)],
  bowl3('side', top=8, nape=94, fringe=62) + [L(ell(46, 2, 10, 9))],
  bowl3('back', top=8, nape=96) + [L(ell(50, 4, 11, 9))])

# Melody Fayre: pelo rubio con dos rodetes en lo alto adornados con peces rojos, flequillo recto y mechones largos que
# bajan por los lados y se vuelven rojos en las puntas como llamas; ojos verde azulado y labios rojos sonrientes
FISH, FLM = _c('#d02828'), _c('#c0402a')
def _fish(x, y, s=1):
    return [L(outline([(x - 8 * s, y + 4), (x, y - 6), (x + 6 * s, y - 14, 1), (x + 4 * s, y - 2), (x + 10 * s, y + 4, 1), (x + 2 * s, y + 6)]), FISH, 'f'),
            L(ell(x + 1 * s, y, 2, 2), WHITE, 'f', False)]


C('melody-fayre', 'chica', P('#e7d66f', '#fad09d', '#3aa0a0'),
  F(eyes='big', mouth='smile', mouth_y=94, hairline=False),
  bowl3('front', top=10, side=74, fringe=60) +
  [L(ell(22, 14, 13, 12)), L(ell(78, 14, 13, 12)), lock([(14, 56), (24, 56), (24, 84), (18, 112), (10, 120, 1), (10, 86)]), lock([(86, 56), (76, 56), (76, 84), (82, 112), (90, 120, 1), (90, 86)]),
   L(outline([(12, 96), (22, 92), (18, 112), (10, 120, 1)]), FLM, 'f'), L(outline([(88, 96), (78, 92), (82, 112), (90, 120, 1)]), FLM, 'f')] +
  _fish(20, 8, 1) + _fish(80, 8, -1) + [L(quad((45, 93), (50, 96), (55, 93)), _c('#c03030'), 'f', False, False, 2.0)],
  bowl3('side', top=10, nape=92, fringe=60) + [L(ell(40, 10, 12, 11)), lock([(56, 56), (64, 58), (62, 90), (58, 116, 1), (52, 90)]), L(outline([(54, 96), (62, 94), (58, 116, 1)]), FLM, 'f')] +
  _fish(40, 4, 1),
  bowl3('back', top=10, nape=96) + [L(ell(22, 14, 13, 12)), L(ell(78, 14, 13, 12)), L(outline([(10, 92), (20, 88), (16, 110), (8, 118, 1)]), FLM, 'f'),
                                     L(outline([(90, 92), (80, 88), (84, 110), (92, 118, 1)]), FLM, 'f')] + _fish(20, 8, 1) + _fish(80, 8, -1))

# Mia Tior (portera): pelo verde menta recogido en un turbante de mechones con dos rizos a los lados y dos mechones largos
# que bajan por la cara; ojos negros grandes y sonrisa
C('mia-tior', 'chica', P('#88d184', '#f4dec2', '#2a2a3a'),
  F(eyes='big', mouth='smile', mouth_y=94, hairline=[(8, 64), (20, 54), (34, 52), (50, 54), (66, 52), (80, 54), (92, 64)]),
  dome('front', top=-2, w=50, cy=44, sb=70, seed=52) + [L(ell(10, 26, 10, 10)), L(ell(90, 26, 10, 10)), strand([(20, 20), (50, 12), (80, 20)], 'shade', 'f', 1.4),
                                                       strand([(16, 34), (50, 28), (84, 34)], 'shade', 'f', 1.4)] + sidelocks(108, (16, 84), 9),
  dome('side', top=-2, w=50, cy=44, nape=88, fr=54, seed=52) + [L(ell(30, 22, 10, 10)), side_lock_s(108)],
  dome('back', top=-2, w=50, cy=44, nape=90, seed=52) + [L(ell(10, 26, 10, 10)), L(ell(90, 26, 10, 10))])

# Mick Sologee: pelo crema muy claro con las puntas rosadas, revuelto y por debajo de las orejas; piel morena, cejas
# blancas, ojos verdes y sonrisa
C('mick-sologee', 'normal', P('#f2ece0', '#b6896e', '#2aa070', tip='#e0a8b0'),
  F(eyes='normal', mouth='smile', mouth_y=93, hairline=[(8, 64), (18, 52), (30, 50), (40, 60, 1), (48, 50), (58, 60, 1), (66, 50), (82, 52), (92, 64)]),
  dome('front', top=6, w=48, cy=46, sb=84, seed=53) + [lock([(10, 62), (18, 62), (16, 88), (10, 96, 1), (6, 80)], 'tip'), lock([(90, 62), (82, 62), (84, 88), (90, 96, 1), (94, 80)], 'tip'),
                                                     L([(28, 64), (40, 64)], WHITE, 'f', False, False, 2.4), L([(60, 64), (72, 64)], WHITE, 'f', False, False, 2.4)],
  dome('side', top=6, w=48, cy=46, nape=90, fr=52, seed=53) + [lock([(52, 70), (58, 70), (56, 92), (50, 98, 1), (48, 80)], 'tip')],
  dome('back', top=6, w=48, cy=46, nape=92, seed=53) + [L(blob([(10, 80), (90, 80), (88, 92), (50, 96), (12, 92)], 4), 'tip', 'f', False)])

# Mickey Schmitt: casco-máscara blanco con una franja roja y dos puntas rojas como cuernos, que le tapa la cabeza y la cara
# hasta la nariz; ojos azules en los huecos con rayas negras, y la boca con media sonrisa
HEL = _c('#f4f0ea')
C('mickey-schmitt', 'normal', P('#f4f0ea', '#fbe8b9', '#4a7ac0'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=95, hairline=False),
  [L(outline([(12, 76), (10, 40), (22, 12), (40, 2), (60, 2), (78, 12), (90, 40), (88, 76), (72, 72), (60, 80), (50, 92, 1), (40, 80), (28, 72)]), HEL, 'f'),
   L(outline([(30, 6), (26, -16, 1), (36, 2)]), RED, 'f'), L(outline([(70, 6), (74, -16, 1), (64, 2)]), RED, 'f'),
   strand([(14, 40), (30, 30), (50, 26), (70, 30), (86, 40)], RED, 'f', 3.0),
   L(blob([(24, 70), (42, 70), (40, 80), (26, 80)], 3), 'skin', 'f', False), L(blob([(76, 70), (58, 70), (60, 80), (74, 80)], 3), 'skin', 'f', False),
   L(ell(34, 75, 3.4, 4), _c('#4a7ac0'), 'f', False), L(ell(66, 75, 3.4, 4), _c('#4a7ac0'), 'f', False),
   L([(26, 82), (30, 88)], BLACK, 'f', False, False, 1.6), L([(74, 82), (70, 88)], BLACK, 'f', False, False, 1.6)],
  [L(outline([(54, 78), (60, 92, 1), (72, 80), (92, 82), (96, 60), (90, 34), (72, 10), (46, 2), (22, 10), (6, 32), (4, 64), (16, 84), (36, 92)]), HEL, 'f'),
   L(outline([(52, 6), (56, -16, 1), (60, 4)]), RED, 'f'), strand([(6, 40), (40, 26), (88, 34)], RED, 'f', 3.0),
   L(blob([(74, 70), (88, 70), (88, 80), (76, 80)], 3), 'skin', 'f', False), L(ell(82, 75, 2.6, 3.6), _c('#4a7ac0'), 'f', False)],
  [L(outline([(10, 80), (8, 40), (20, 12), (40, 2), (60, 2), (80, 12), (92, 40), (90, 80), (50, 88)]), HEL, 'f'),
   L(outline([(30, 6), (26, -16, 1), (36, 2)]), RED, 'f'), L(outline([(70, 6), (74, -16, 1), (64, 2)]), RED, 'f'), strand([(12, 40), (50, 30), (88, 40)], RED, 'f', 3.0)])

# Miles Panzer: gorra militar verde oliva, pelo granate en pinchos que asoma por los lados, gafas de visor naranjas, unos
# auriculares con micrófono y una sonrisa grande de dientes; piel tostada
OLIVE, VISO = _c('#535337'), _c('#e07020')
C('miles-panzer', 'normal', P('#7a2040', '#c8936b', '#302232'),
  F(eyes='none', brows=False, mouth='none', hairline=False),
  [lock([(14, 66), (0, 52), (-6, 40, 1), (8, 42), (2, 30, 1), (18, 36)]), lock([(86, 66), (100, 52), (106, 40, 1), (92, 42), (98, 30, 1), (82, 36)]),
   L(outline([(12, 44), (12, 22), (26, 6), (50, 0), (76, 4), (90, 18), (90, 44), (50, 40)]), OLIVE, 'f'),
   L(blob([(8, 42), (50, 36), (94, 42), (96, 50), (50, 46), (6, 50)], 4), _c('#3c372a'), 'f'),
   L(outline([(18, 66), (40, 60), (50, 64), (60, 60), (82, 66), (78, 78), (58, 78), (50, 74), (42, 78), (22, 78)]), VISO, 'f'),
   L(ell(14, 72, 6, 7), _c('#d0dcdc'), 'f', False, True), L(ell(86, 72, 6, 7), _c('#d0dcdc'), 'f', False, True),
   L(quad((86, 78), (88, 96), (74, 100)), _c('#d0dcdc'), 'f', False, False, 1.6), L(ell(72, 100, 3, 2.4), _c('#d0dcdc'), 'f', False, True)] + teeth(93, 13, 6),
  [lock([(30, 64), (10, 56), (4, 44, 1), (18, 46), (14, 34, 1), (30, 40)]),
   L(outline([(6, 46), (6, 22), (24, 4), (50, 0), (76, 6), (88, 22), (88, 44), (50, 40)]), OLIVE, 'f'), L(blob([(4, 42), (60, 38), (104, 46), (100, 52), (56, 46), (4, 50)], 4), _c('#3c372a'), 'f'),
   L(outline([(72, 64), (94, 62), (96, 78), (74, 78)]), VISO, 'f'), L(ell(46, 72, 7, 8), _c('#d0dcdc'), 'f', False, True),
   L(quad((50, 78), (66, 98), (84, 98)), _c('#d0dcdc'), 'f', False, False, 1.6)] + teeth_side(93),
  [lock([(10, 70), (4, 48), (96, 48), (90, 70), (70, 66), (50, 72), (30, 66)]),
   L(outline([(12, 46), (12, 22), (26, 6), (50, 0), (76, 4), (90, 18), (90, 46), (50, 42)]), OLIVE, 'f'),
   L(ell(10, 72, 6, 7), _c('#d0dcdc'), 'f', False, True), L(ell(90, 72, 6, 7), _c('#d0dcdc'), 'f', False, True)])

# Millie Cheer: media melena verde menta de rizos abultados por los lados; ojos verdes, mejillas sonrosadas y sonrisa
C('millie-cheer', 'chica', P('#64ca82', '#f9dcbe', '#5aa040'),
  F(eyes='big', mouth='smile', mouth_y=94, hairline=[(8, 64), (20, 50), (36, 46), (50, 52), (64, 46), (80, 50), (92, 64)]),
  dome('front', top=8, w=48, cy=46, sb=80, seed=56) + [L(ell(10, 78, 12, 13)), L(ell(90, 78, 12, 13)), L(ell(14, 96, 9, 9)), L(ell(86, 96, 9, 9)),
                                                     strand([(4, 74), (14, 70), (16, 82)], 'deep', 'f', 1.0), strand([(96, 74), (86, 70), (84, 82)], 'deep', 'f', 1.0)] + blush(87, 22, 4.6),
  dome('side', top=8, w=48, cy=46, nape=92, fr=52, seed=56) + [L(ell(28, 82, 13, 14)), L(ell(36, 100, 9, 9))],
  dome('back', top=8, w=48, cy=46, nape=94, seed=56) + [L(ell(10, 78, 12, 13)), L(ell(90, 78, 12, 13)), L(ell(30, 92, 11, 10)), L(ell(70, 92, 11, 10))])

# ------------------------------------------------------------------------------------------------------------ 57-61

# Millie Terry: gorra de plato gris oscura con cinta amarilla, pelo negro que le tapa un ojo y un rizo a un lado; el otro
# ojo naranja en espiral, pecas y cara muy pálida
CAPG = _c('#706d6d')
C('millie-terry', 'chica', P('#2d2926', '#f0f0df', '#e08020'),
  F(eyes='none', brows=False, mouth='line', mouth_y=95, hairline=False),
  [lock([(12, 90), (8, 60), (20, 50), (40, 50), (72, 56), (80, 72), (74, 92), (66, 74), (54, 62), (40, 60), (26, 66), (20, 88)]), L(ell(86, 84, 6, 6)),
   L(outline([(-2, 36), (6, 14), (30, 0), (64, -2), (92, 8), (104, 26), (96, 40), (60, 50), (24, 52)]), CAPG, 'f'),
   L(blob([(14, 42), (60, 38), (98, 30), (100, 36), (60, 46), (14, 50)], 4), _c('#e0b040'), 'f', False),
   L(blob([(10, 48), (40, 46), (64, 52), (40, 58), (10, 58)], 4), _c('#3a3838'), 'f'),
   L(ell(36, 76, 6, 6), WHITE, 'f', False, True), L(ell(36, 76, 4, 4) + [ell(36, 76, 4, 4)[0]], _c('#e08020'), 'f', False, False, 1.4), L(ell(36, 76, 1.4, 1.4), _c('#e08020'), 'f', False)] +
  [L(ell(x, 86, 0.9, 0.9), _c('#c08060'), 'f', False) for x in (28, 31, 34)],
  [lock([(56, 52), (66, 60), (62, 84), (54, 92, 1), (50, 70)]), L(outline([(-6, 40), (4, 14), (30, -2), (64, -2), (92, 8), (106, 28), (98, 42), (60, 48), (20, 52)]), CAPG, 'f'),
   L(blob([(4, 42), (60, 38), (100, 32), (100, 38), (60, 46), (4, 50)], 4), _c('#e0b040'), 'f', False), L(ell(82, 76, 4, 5), WHITE, 'f', False, True)],
  [lock([(10, 92), (6, 60), (94, 60), (90, 92), (70, 86), (50, 90), (30, 86)]), L(ell(14, 84, 6, 6)),
   L(outline([(-2, 38), (6, 14), (30, 0), (64, -2), (92, 8), (104, 26), (96, 42), (60, 50), (24, 52)]), CAPG, 'f'),
   L(blob([(4, 44), (50, 40), (100, 30), (100, 36), (50, 48), (4, 52)], 4), _c('#e0b040'), 'f', False)])

# Mint Royle: gorro de lana amarillo con el borde verde azulado vuelto hacia arriba y una borla del mismo color, pelo rubio
# que asoma por debajo; ojeras rojas alrededor de los ojos y boca enfurruñada
KNIT, TEAL2 = _c('#f6ca4e'), _c('#2e6268')
C('mint-royle', 'bajito', P('#e8b048', '#f7d3ab', '#302232'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=94, hairline=(60, 58)),
  dome('front', top=24, w=44, cy=50, sb=66, seed=58, shade=False) +
  [L(outline([(16, 44), (16, 20), (30, 4), (50, 0), (70, 4), (84, 20), (84, 44), (50, 40)]), KNIT, 'f'), strand([(40, 4), (50, 14), (60, 4)], _c('#d0a030'), 'f', 2.0),
   L(outline([(4, 34), (20, 44), (50, 48), (80, 44), (96, 34), (94, 46), (80, 56), (50, 58), (20, 56), (6, 46)]), TEAL2, 'f'), L(ell(50, -6, 8, 8), TEAL2, 'f'),
   L(ell(36, 75, 7, 6), _c('#c02828'), 'b', False), L(ell(64, 75, 7, 6), _c('#c02828'), 'b', False)],
  dome('side', top=24, w=44, cy=50, nape=86, fr=56, seed=58, shade=False) +
  [L(outline([(10, 44), (12, 20), (28, 4), (50, 0), (72, 6), (84, 22), (84, 44), (50, 40)]), KNIT, 'f'),
   L(outline([(2, 40), (40, 48), (88, 42), (100, 32), (96, 46), (84, 56), (40, 58), (4, 52)]), TEAL2, 'f'), L(ell(48, -6, 8, 8), TEAL2, 'f')],
  dome('back', top=24, w=44, cy=50, nape=86, seed=58, shade=False) +
  [L(outline([(16, 44), (16, 20), (30, 4), (50, 0), (70, 4), (84, 20), (84, 44), (50, 40)]), KNIT, 'f'),
   L(outline([(4, 36), (20, 46), (50, 50), (80, 46), (96, 36), (94, 48), (80, 58), (50, 60), (20, 58), (6, 48)]), TEAL2, 'f'), L(ell(50, -6, 8, 8), TEAL2, 'f')])

# Mirabel "Bella" Tussel: pelo rojo con dos puntas como cuernos curvados en lo alto y dos coletas bajas a los lados; ojos
# de dos colores (rojo y verde azulado), cejas fruncidas y boca seria
C('mirabel-bella-tussel', 'chica', P('#b83542', '#fadcbf', '#c03030'),
  F(eyes='big', brows='angry', mouth='frown', mouth_y=94, hairline=hl(5, 62, 50, 58, seed=59)),
  dome('front', top=10, w=46, cy=48, sb=68, seed=59) +
  [lock([(14, 34), (2, 14), (8, -6, 1), (14, 12), (26, 22)]), lock([(86, 34), (98, 14), (92, -6, 1), (86, 12), (74, 22)]),
   lock([(14, 70), (2, 76), (-6, 100, 1), (8, 96), (16, 82)]), lock([(86, 70), (98, 76), (106, 100, 1), (92, 96), (84, 82)]),
   L(ell(64, 76, 3.6, 4.6), _c('#2aa0a0'), 'f', False), L(ell(64, 76, 1.8, 2.4), BLACK, 'f', False)],
  dome('side', top=10, w=48, cy=48, nape=88, fr=54, seed=59) + [lock([(50, 20), (58, 0), (52, -8, 1), (42, 8)]), lock([(34, 72), (20, 80), (14, 102, 1), (28, 96), (36, 82)])],
  dome('back', top=10, w=46, cy=48, nape=88, seed=59) +
  [lock([(14, 34), (2, 14), (8, -6, 1), (14, 12), (26, 22)]), lock([(86, 34), (98, 14), (92, -6, 1), (86, 12), (74, 22)]),
   lock([(14, 70), (2, 76), (-6, 100, 1), (8, 96), (16, 82)]), lock([(86, 70), (98, 76), (106, 100, 1), (92, 96), (84, 82)])])

# Mitzi "Mittens" Holly: pelo rosa con raya al lado y dos coletas bajas junto a las mejillas; ojos verdes afilados,
# mejillas coloradas y sonrisa pícara
C('mitzi-mittens-holly', 'chica', P('#cc7973', '#fdd0a0', '#5a8a40'),
  F(eyes='sharp', mouth='smile', mouth_y=93, hairline=[(8, 64), (18, 50), (30, 42), (44, 48), (58, 40), (74, 44), (86, 54), (92, 64)]),
  dome('front', top=8, w=46, cy=46, sb=70, seed=60) +
  [lock([(14, 70), (4, 82), (-2, 104, 1), (12, 100), (20, 82)]), lock([(86, 70), (96, 82), (102, 104, 1), (88, 100), (80, 82)])] + blush(86, 22, 5),
  dome('side', top=8, w=46, cy=46, nape=88, fr=52, seed=60) + [lock([(36, 70), (26, 82), (20, 104, 1), (34, 100), (40, 82)])],
  dome('back', top=8, w=46, cy=46, nape=88, seed=60) +
  [lock([(14, 70), (4, 82), (-2, 104, 1), (12, 100), (20, 82)]), lock([(86, 70), (96, 82), (102, 104, 1), (88, 100), (80, 82)])])

# Mo Zake: pelo castaño rojizo corto en pinchos, con mechones que se abren hacia fuera junto a las mejillas; ojos
# entornados de cansancio con ojeras y dientes apretados
C('mo-zake', 'chica', P('#994d4c', '#e3d0b6', '#6a6a8a'),
  F(eyes='sharp', brows='angry', mouth='none', hairline=hl(6, 62, 50, 58, jit=2, seed=61)),
  dome('front', top=8, w=46, cy=46, n=8, amp=12, sweep=0.3, sb=68, seed=61) +
  [lock([(14, 66), (4, 76), (-4, 88, 1), (8, 86), (18, 78)]), lock([(86, 66), (96, 76), (104, 88, 1), (92, 86), (82, 78)])] + teeth(94, 8, 5),
  dome('side', top=8, w=46, cy=46, n=8, amp=12, sweep=0.3, nape=86, fr=52, seed=61) + teeth_side(94),
  dome('back', top=8, w=46, cy=46, n=8, amp=12, nape=88, seed=61) +
  [lock([(14, 66), (4, 76), (-4, 88, 1), (8, 86), (18, 78)]), lock([(86, 66), (96, 76), (104, 88, 1), (92, 86), (82, 78)])])
