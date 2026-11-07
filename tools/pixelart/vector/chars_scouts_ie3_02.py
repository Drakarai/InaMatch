"""Ojeadores de IE3 (scouts-ie3), tanda 02: dibujados a partir de su retrato de Victory Road; claves 'scouts-ie3:<id>'.

Ninguno de la tanda tiene modelo 3D: el frente sale del retrato y el perfil y la espalda se deducen. Muchos llevan
capucha, casco, sombrero o máscara: van como capas de delante (ring() hace un aro con hueco para la cara)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401
from chars_scouts_ie1_09 import dome, hl, face, face_side, mark, _c  # noqa: F401
from chars_scouts_ie1_03 import round_specs, goggles, thick_brows, side_brow, big_grin, tri_nose  # noqa: F401
from chars_scouts_ie1_10 import skull, nose_tri, nose_line, squint  # noqa: F401
from chars_scouts_ie2_04 import band, strands_down, lashes, lash_side, sharp_eyes, sharp_eye_side  # noqa: F401
from chars_scouts_ie2_03 import ears_pointy, teeth_grin  # noqa: F401
from chars_vr_nikogawa import crop, brows, blush  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)
K = 'scouts-ie3:'


def F(**k):
    d = {'eyes': 'normal', 'mouth': 'line'}
    d.update(k)
    return d


def P(hair, skin, iris='#302232', **k):
    return pal(hair, skin, iris, **k)


def C(pid, body, palette, f, front, side, back):
    """Como en la tanda 09 de IE1: el nacimiento del pelo baja por el borde de la cara para que su raya no cruce el pelo."""
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[K + pid] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def ring(outer, inner, c, z='f', sil=True):
    """Aro: contorno de fuera y hueco de dentro (capuchas y cascos con la cara al aire)."""
    o = outline(outer)
    i = outline(inner)[::-1]
    return L(o + [o[0]] + i + [i[0]], c, z, sil)


def skull3(view, c='skin'):
    """Calva en las tres vistas (de frente, la de la tanda 10 de IE1)."""
    if view == 'front':
        return skull('front')
    if view == 'side':
        return [L(outline([(44, 60), (30, 62), (10, 50), (6, 30), (20, 10), (46, 2), (72, 8), (86, 26), (88, 44), (70, 40), (54, 42)]), c)]
    return [L(outline([(16, 76), (12, 42), (22, 16), (50, 6), (78, 16), (88, 42), (84, 76), (50, 84)]), c),
            L(outline([(60, 10), (80, 20), (88, 44), (84, 74), (70, 60)]), 'skin_d', 'b', False)]


def hood(view, c, top=-4, w=0, low=104, rim='shade', face_hole=None):
    """Capucha que tapa la cabeza (la cara queda en el hueco). face_hole: contorno del hueco de frente."""
    if view == 'front':
        hole = face_hole or [(20, 100), (16, 70), (22, 46), (50, 38), (78, 46), (84, 70), (80, 100), (50, 108)]
        outer = [(2 - w, low), (-2 - w, 60), (8 - w, 22), (30, top + 6), (50, top), (70, top + 6), (92 + w, 22), (102 + w, 60), (98 + w, low), (50, low + 8)]
        hx = max(p[0] for p in hole)
        return [ring(outer, hole, c), L(blob([(64, top + 5), (88 + w, 20), (99 + w, 58), (96 + w, low - 6), (hx + 8, low - 2), (hx + 8, 60), (hx + 4, 34), (78, 18)], 6), rim, 'f', False)]
    if view == 'side':
        return [L(outline([(70, 104), (74, 80), (78, 52), (84, 34), (92, 24), (86, 6), (60, top - 2), (30, top + 4), (6, 22), (-4 - w, 56), (0 - w, 92), (20, 108),
                           (50, 110)]), c),
                L(outline([(-2 - w, 50), (30, 50), (56, 74), (60, 100), (30, 106), (2 - w, 90)]), rim, 'b', False)]
    return [L(outline([(2 - w, low), (-2 - w, 60), (8 - w, 22), (30, top + 6), (50, top), (70, top + 6), (92 + w, 22), (102 + w, 60), (98 + w, low), (50, low + 8)]), c),
            L(blob([(58, top + 8), (88 + w, 26), (98 + w, 62), (94 + w, low - 4), (66, low + 4), (64, 40)], 6), rim, 'f', False)]


def bowl3(view, top=4, side=90, nape=96, w=0, c='mid', fringe=58):
    """Melena en casco que tapa las orejas, con el flequillo recto a la altura fringe."""
    if view == 'front':
        return [L(outline([(14 - w * 0.5, side), (7 - w, 62), (10 - w, 32), (28, 10 + top), (50, top), (72, 10 + top), (90 + w, 32), (93 + w, 62), (86 + w * 0.5, side),
                           (82, fringe), (18, fringe)]), c),
                L(outline([(60, top + 4), (80, 14 + top), (91 + w, 36), (92 + w, 62), (86, side - 4), (82, 50)]), 'shade', 'b', False)]
    if view == 'side':
        return [L(outline([(80, fringe - 2), (88, 40), (82, 16), (60, top - 2), (32, top + 2), (12, 16), (2 - w, 42), (2 - w, 70), (8, nape - 4), (28, nape), (44, nape - 4),
                           (56, 84), (62, 62), (72, fringe)]), c),
                L(outline([(4 - w, 44), (34, 48), (52, 66), (50, 84), (30, nape - 2), (8, nape - 6)]), 'shade', 'b', False)]
    return [L(outline([(10 - w * 0.5, nape - 2), (5 - w, 62), (8 - w, 32), (26, 10 + top), (50, top + 2), (74, 10 + top), (92 + w, 32), (95 + w, 62), (90 + w * 0.5, nape - 2),
                       (70, nape + 2), (50, nape + 3), (30, nape + 2)]), c),
            L(outline([(58, top + 6), (80, 16 + top), (93 + w, 40), (93 + w, 64), (88, nape - 2), (66, nape + 2), (62, 50)]), 'shade', 'b', False)]


def scarf(view, c, y=100, h=14):
    """Bufanda o pañuelo alrededor del cuello."""
    if view == 'front':
        return [L(blob([(10, y), (30, y - 4), (50, y - 2), (70, y - 4), (90, y), (94, y + h), (70, y + h + 4), (50, y + h + 6), (30, y + h + 4), (6, y + h)], 6), c, 'f')]
    if view == 'side':
        return [L(blob([(30, y - 2), (60, y - 6), (86, y - 2), (88, y + h), (60, y + h + 4), (28, y + h + 2)], 6), c, 'f')]
    return [L(blob([(8, y), (50, y - 4), (92, y), (94, y + h), (50, y + h + 6), (6, y + h)], 6), c, 'f')]


def side_lock(x, y0, y1, c='mid', wd=8, z='f'):
    """Mechón ancho que cae junto a la cara (de frente)."""
    return L(outline([(x - wd / 2, y0), (x + wd / 2, y0), (x + wd / 3, y1 - 6), (x, y1, 1), (x - wd / 3, y1 - 6)]), c, z)


# ------------------------------------------------------------------ jugadores

# Chucky Discard (Cardaway): melena granate oscuro hasta los hombros, lacia, con un flequillo largo que le tapa un ojo;
# ojo verde afilado y ceño fruncido
C('chucky-discard-cardaway', 'normal', P('#741422', '#f6cea3', iris='#3a8a4a', shade='#560e18'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=[(6, 70), (18, 48), (36, 38), (58, 40), (78, 46), (94, 66)]),
  dome('front', top=0, w=47, cy=44, n=5, amp=6, sweep=0.5, seed=31, long=104, flare=4, soft=True) +
  [L(outline([(16, 46), (34, 28), (60, 30), (60, 52), (50, 72), (42, 92, 1), (36, 76), (24, 70), (16, 64)]), 'mid', 'f'),
   strand([(40, 36), (46, 60), (42, 84)], 'deep', 'f', 1.0)],
  dome('side', top=0, w=47, cy=44, n=5, amp=6, sweep=0.5, seed=31, long=104, flare=4, fr=56, soft=True) +
  [L(outline([(70, 30), (90, 36), (92, 58), (86, 74, 1), (80, 58)]), 'mid', 'f')],
  dome('back', top=0, w=47, cy=44, n=5, amp=6, sweep=0.5, seed=31, long=104, flare=4, soft=True))

# Clark Fax (Phylen): media melena gris verdoso oscuro con la raya en medio y mechones que le caen hasta el cuello; mascarilla
# antigás caqui con un filtro redondo y correas negras; ojos tristes de iris rojizo
GAS, GASD = _c('#a29a78'), _c('#6c6650')
def _gas(view):
    if view == 'front':
        return [L([(16, 82), (32, 86)], BLACK, 'f', False, False, 3.0), L([(84, 82), (68, 86)], BLACK, 'f', False, False, 3.0),
                L(blob([(32, 84), (50, 78), (68, 84), (70, 98), (60, 108), (40, 108), (30, 98)], 6), GAS, 'f'),
                L(ell(50, 96, 8, 7), GASD, 'f'), L(ell(50, 96, 4, 3.4), _c('#c8a088'), 'f', False),
                L(ell(48, 96, 1, 1), BLACK, 'f', False), L(ell(52, 96, 1, 1), BLACK, 'f', False)]
    if view == 'side':
        return [L([(50, 78), (78, 84)], BLACK, 'f', False, False, 3.0),
                L(blob([(76, 82), (90, 84), (98, 94), (94, 106), (80, 106), (72, 96)], 6), GAS, 'f'), L(ell(92, 96, 4, 6), GASD, 'f')]
    return [L(quad((14, 82), (50, 88), (86, 82)), BLACK, 'f', False, False, 3.0)]
C('clark-fax-phylen', 'delgado', P('#4a5859', '#fbeec8', iris='#8a4a3a', shade='#3a4545'),
  F(eyes='normal', brows=True, mouth='none', hairline=[(6, 70), (18, 48), (36, 40), (50, 46), (64, 40), (82, 48), (94, 70)]),
  dome('front', top=2, w=46, cy=46, long=102, flare=6, ends=5) + [side_lock(20, 56, 104, 'mid', 9), side_lock(80, 56, 104, 'mid', 9)] + _gas('front'),
  dome('side', top=2, w=46, cy=46, long=102, flare=6, fr=50) + _gas('side'),
  dome('back', top=2, w=46, cy=46, long=102, flare=6, ends=5) + _gas('back'))

# Clay Ellement: pelo gris violáceo liso con flequillo recto, mechones hasta la mandíbula y una coleta alta atada con una
# goma roja; dos rectángulos rojos pintados en las mejillas
RED = _c('#c83a2a')
def _pony(view, x=50, y=-2):
    if view == 'side':
        return [L(outline([(x - 6, y + 10), (x - 18, y - 6), (x - 30, y + 4), (x - 40, y + 30, 1), (x - 26, y + 14), (x - 10, y + 18)])),
                L(ell(x - 8, y + 6, 6, 5), RED, 'b')]
    return [L(outline([(x - 10, y + 10), (x - 8, y - 14), (x, y - 20, 1), (x + 8, y - 14), (x + 10, y + 10)])), L(ell(x, y + 4, 8, 4), RED, 'b')]
C('clay-ellement', 'normal', P('#77697b', '#f9bc7c', iris='#3a3048', shade='#5f5263'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=91, hairline=[(6, 70), (16, 50), (30, 58), (50, 56), (70, 58), (84, 50), (94, 70)]),
  _pony('front') + dome('front', top=4, w=46, cy=46, long=96, flare=2, ends=4) +
  [mark([(18, 80), (25, 80), (25, 86), (18, 86)], RED), mark([(75, 80), (82, 80), (82, 86), (75, 86)], RED)],
  _pony('side', 46) + dome('side', top=4, w=46, cy=46, long=96, flare=2, fr=58) + [mark([(80, 80), (86, 80), (86, 86), (80, 86)], RED)],
  _pony('back') + dome('back', top=4, w=46, cy=46, long=96, flare=2, ends=4))

# Climie Hills (portero): pinchos verde grisáceo oscuro de punta hacia arriba, una cinta blanca sucia atada en la frente con
# las puntas colgando a un lado; cara larga de mandíbula grande, nariz enorme, ojos afilados y media sonrisa
HB = _c('#e1e2d7')
C('climie-hills', 'normal', P('#52574f', '#fbc171', iris='#1e1a1a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=96, face_front=face(w=2, chin=108, jaw=4), face_side=face_side(chin=8, jaw=4, nose=4), ear_out=4,
    hairline=False, nose=(50, 86, 3.4)),
  dome('front', top=-8, w=46, cy=40, n=6, amp=12, sweep=0.4, seed=4, sb=56, shade=True) +
  [L(blob([(10, 52), (30, 44), (50, 42), (70, 44), (90, 52), (90, 62), (70, 54), (50, 52), (30, 54), (10, 62)], 6), HB, 'f'),
   L(outline([(12, 50), (-6, 44, 1), (0, 56), (-8, 64, 1), (12, 60)]), HB, 'f')] + nose_tri(88, 5, 12),
  dome('side', top=-8, w=46, cy=40, n=6, amp=12, sweep=0.4, seed=4, nape=74, fr=42) +
  [L(blob([(4, 50), (40, 42), (88, 42), (90, 52), (40, 52), (4, 60)], 6), HB, 'f'), L(outline([(8, 52), (-10, 50, 1), (-4, 60), (-10, 70, 1), (8, 62)]), HB, 'f')],
  dome('back', top=-8, w=46, cy=40, n=6, amp=12, sweep=0.4, seed=4, nape=74) +
  [L(blob([(8, 54), (50, 48), (92, 54), (92, 64), (50, 58), (8, 64)], 6), HB, 'f'), L(outline([(10, 56), (-4, 52, 1), (2, 62), (-6, 72, 1), (12, 64)]), HB, 'f')])

# Cole (Koala Bear): capucha de koala gris con dos orejas grandes redondas, un mechón castaño que asoma por la frente; ojos
# redondos negros enormes, naricilla y una sonrisa pequeña
KOA, KOAD, KOAI = _c('#929285'), _c('#6d615a'), _c('#57443d')
def _koala(view):
    if view == 'front':
        return [L(ell(10, 22, 18, 17), KOA, 'b'), L(ell(90, 22, 18, 17), KOA, 'b'), L(ell(12, 24, 10, 10), KOAI, 'b', False), L(ell(88, 24, 10, 10), KOAI, 'b', False)] + \
            hood('front', KOA, top=4, w=0, low=96, face_hole=[(20, 96), (14, 66), (22, 44), (50, 36), (78, 44), (86, 66), (80, 96), (50, 106)]) + \
            [L(outline([(44, 46), (50, 30, 1), (52, 40), (62, 32, 1), (56, 50)]), _c('#8a4a2a'), 'f')]
    if view == 'side':
        return [L(ell(30, 10, 17, 17), KOA, 'b')] + hood('side', KOA, top=4) + [L(ell(30, 10, 9, 9), KOAI, 'f', False)]
    return [L(ell(10, 22, 18, 17), KOA, 'b'), L(ell(90, 22, 18, 17), KOA, 'b')] + hood('back', KOA, top=4, low=96)
C('cole-koala-bear', 'bajito', P('#929285', '#f7bf94', iris='#141414', shade='#6d615a'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, hairline=False, ears=False),
  _koala('front') + [L(ell(36, 76, 7, 7), WHITE, 'f'), L(ell(64, 76, 7, 7), WHITE, 'f'), L(ell(36, 76, 5, 5), BLACK, 'f', False), L(ell(64, 76, 5, 5), BLACK, 'f', False),
                     L(ell(50, 88, 3, 2), BLACK, 'f', False)],
  _koala('side') + [L(ell(82, 76, 4, 6), WHITE, 'f'), L(ell(83, 76, 3, 4.4), BLACK, 'f', False)],
  _koala('back'))

# Cole Tivator: piel morena, pelo verde azulado oscuro rapado muy corto, orejas enormes, cejas gruesas arqueadas, ojos que
# miran hacia arriba y la boca torcida en ola
C('cole-tivator', 'normal', P('#3b5652', '#b6723a', iris='#141414'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=95, big_ears=4, ear_out=3, nose=(50, 86, 3),
    hairline=[(10, 60), (20, 46), (36, 40), (50, 40), (64, 40), (80, 46), (90, 60)]),
  crop('front', top=4, side=58) + brows(62, _c('#2a3a36'), 3.6, 15, -1.0, 13),
  crop('side', top=4, nape=78) + side_brow(62, _c('#2a3a36'), 3.4, -0.8),
  crop('back', top=4, nape=78))

# Colin (Commando) Mando: pelo azul marino alborotado como llamas, una cinta ancha de camuflaje verde en la frente, rayas de
# camuflaje verde pintadas en las mejillas y una sonrisa enorme de dientes
CAMO, CAMOD = _c('#5a8a2a'), _c('#2e5214')
def _camo(view):
    if view == 'front':
        return [L(blob([(10, 50), (30, 44), (50, 42), (70, 44), (90, 50), (90, 66), (70, 62), (50, 60), (30, 62), (10, 66)], 6), CAMO, 'f'),
                mark([(24, 50), (34, 48), (36, 54), (26, 56)], CAMOD), mark([(52, 46), (62, 48), (60, 54), (50, 54)], CAMOD), mark([(72, 52), (84, 54), (80, 60), (70, 58)], CAMOD)]
    if view == 'side':
        return [L(blob([(4, 52), (40, 44), (88, 46), (90, 62), (40, 60), (4, 66)], 6), CAMO, 'f'), mark([(50, 48), (62, 48), (60, 56), (48, 56)], CAMOD)]
    return [L(blob([(8, 54), (50, 48), (92, 54), (92, 68), (50, 62), (8, 68)], 6), CAMO, 'f'), mark([(30, 54), (44, 54), (40, 60), (28, 60)], CAMOD)]
C('colin-commando-mando', 'normal', P('#1e345c', '#eac4a4', iris='#5a2a2a'),
  F(eyes='sharp', brows='angry', mouth='none', hairline=False),
  dome('front', top=-12, w=48, cy=40, n=7, amp=14, sweep=0.3, seed=9, sb=56) + _camo('front') +
  [mark([(18, 84), (30, 82), (32, 88), (20, 90)], CAMO), mark([(70, 82), (82, 84), (80, 90), (68, 88)], CAMO)] + big_grin(92, 14, 8),
  dome('side', top=-12, w=48, cy=40, n=7, amp=14, sweep=0.3, seed=9, nape=74, fr=42) + _camo('side') + [mark([(74, 82), (86, 82), (86, 88), (74, 90)], CAMO)],
  dome('back', top=-12, w=48, cy=40, n=7, amp=14, sweep=0.3, seed=9, nape=76) + _camo('back'))

# Concordia Choral: pelo cobrizo recogido en una corona de trenzas, con la raya en medio y dos mechones finos junto a las
# orejas; sombra rosa en los párpados, ojos castaños grandes y sonrisa
COP = '#c47e55'
def _braids(view):
    out = []
    if view == 'front':
        out = [L(blob([(10, 54), (14, 26), (30, 8), (50, 4), (70, 8), (86, 26), (90, 54), (80, 42), (64, 24), (50, 22), (36, 24), (20, 42)], 6), 'shade', 'f')]
        for i in range(7):
            t = i / 6
            import math
            a = math.pi * (1 - t)
            out.append(L(ell(50 + 38 * math.cos(a), 32 - 24 * math.sin(a), 6, 5), 'mid', 'f', False))
        return out
    if view == 'side':
        for i in range(6):
            out.append(L(ell(16 + i * 12, 14 - (i in (2, 3)) * 4 + (i == 5) * 6, 6, 5), 'mid', 'f', False))
        return out
    for i in range(7):
        out.append(L(ell(14 + i * 12, 22 - min(i, 6 - i) * 3, 6, 5), 'mid', 'f', False))
    return out
C('concordia-choral', 'chica', P(COP, '#fde9b8', iris='#8a3a1e', shade='#924f32'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=91, hairline=[(6, 66), (18, 46), (34, 40), (50, 44), (66, 40), (82, 46), (94, 66)]),
  dome('front', top=6, w=44, cy=46, sb=66) + _braids('front') + [strands_down(18, 56, 92, 'mid', 2.0, 1), strands_down(82, 56, 92, 'mid', 2.0, -1)] +
  [L(blob([(28, 70), (36, 66), (44, 70), (36, 72)], 4), _c('#e89aa0'), 'f', False), L(blob([(56, 70), (64, 66), (72, 70), (64, 72)], 4), _c('#e89aa0'), 'f', False)] + lashes(),
  dome('side', top=6, w=44, cy=46, nape=84, fr=46) + _braids('side') + lash_side(),
  dome('back', top=6, w=44, cy=46, nape=86) + _braids('back') + [L(ell(50, 74, 12, 10), 'mid', 'f')])

# Connie (Confucia) Fuchsia: pelo gris casi negro recogido en un moño alto con un lazo rojo y dos bucles enrollados a la
# altura del cuello; ojos cerrados con unas rayas finas pintadas y la boca pequeña
BOW = _c('#c82a2a')
def _connie(view):
    if view == 'front':
        return [L(ell(50, -2, 13, 11)), L(outline([(50, -8), (34, -18, 1), (36, -2)]), BOW, 'f'), L(outline([(50, -8), (66, -18, 1), (64, -2)]), BOW, 'f'),
                L(ell(14, 98, 12, 9)), L(ell(86, 98, 12, 9)), strand([(6, 96), (14, 92), (22, 98)], 'deep', 'f', 1.0), strand([(78, 98), (86, 92), (94, 96)], 'deep', 'f', 1.0)]
    if view == 'side':
        return [L(ell(40, -2, 13, 11)), L(outline([(40, -8), (30, -20, 1), (28, -2)]), BOW, 'f'), L(ell(26, 96, 13, 10))]
    return [L(ell(50, -2, 13, 11)), L(outline([(50, -8), (34, -18, 1), (36, -2)]), BOW, 'f'), L(outline([(50, -8), (66, -18, 1), (64, -2)]), BOW, 'f'),
            L(ell(16, 96, 12, 9)), L(ell(84, 96, 12, 9))]
C('connie-confucia-fuchsia', 'chica', P('#3b4448', '#f9bc7d', iris='#1e1a1a', shade='#2c3336'),
  F(eyes='closed', brows=False, mouth='frown', mouth_y=92, hairline=[(6, 64), (18, 46), (36, 40), (50, 42), (64, 40), (82, 46), (94, 64)]),
  _connie('front') + dome('front', top=4, w=44, cy=46, sb=66) +
  [L(quad((24, 70), (20, 64), (26, 58)), OUTC, 'f', False, False, 1.0), L(quad((76, 70), (80, 64), (74, 58)), OUTC, 'f', False, False, 1.0)],
  _connie('side') + dome('side', top=4, w=44, cy=46, nape=88, fr=46),
  _connie('back') + dome('back', top=4, w=44, cy=46, nape=88))

# Cuba Libra: calvo de cabeza alargada en huevo, con tres puntos rojos en la frente, ojos cerrados en raya, nariz larga,
# orejas grandes con pendientes dorados en forma de balanza y una sonrisa tranquila
GOLD = _c('#e0b030')
def _scales(x):
    return [L([(x, 80), (x, 90)], GOLD, 'f', False, False, 1.6), L([(x - 7, 92), (x + 7, 92)], GOLD, 'f', False, False, 1.6),
            L(quad((x - 10, 94), (x - 7, 101), (x - 4, 94)) + [(x - 4, 94)], GOLD, 'f', True), L(quad((x + 4, 94), (x + 7, 101), (x + 10, 94)) + [(x + 10, 94)], GOLD, 'f', True)]
C('cuba-libra', 'delgado', P('#e4ccac', '#e4ccac', iris='#1e1a1a'),
  F(eyes='closed', brows=False, mouth='smile', mouth_y=94, big_ears=4, ear_out=4, hairline=False, face_front=face(chin=106), face_side=face_side(chin=6, nose=5)),
  [L(outline([(17, 66), (14, 30), (24, -6), (50, -18), (76, -6), (86, 30), (83, 66), (50, 72)]), 'skin'),
   L(outline([(62, -12), (78, -2), (86, 30), (83, 62), (74, 30)]), 'skin_d', 'b', False),
   L(ell(50, 34, 3.4, 3.4), RED, 'f'), L(ell(42, 44, 3.4, 3.4), RED, 'f'), L(ell(58, 44, 3.4, 3.4), RED, 'f')] + nose_line(88) + _scales(12) + _scales(88),
  [L(outline([(44, 60), (30, 62), (10, 44), (8, 10), (26, -14), (50, -18), (72, -6), (86, 24), (88, 44), (70, 40), (54, 42)]), 'skin'),
   L(ell(86, 40, 3, 3.4), RED, 'f')] + [L([(46, 80), (46, 90)], GOLD, 'f', False, False, 1.6), L([(40, 92), (52, 92)], GOLD, 'f', False, False, 1.6)],
  [L(outline([(16, 76), (12, 30), (24, -6), (50, -18), (76, -6), (88, 30), (84, 76), (50, 84)]), 'skin'),
   L(outline([(60, -12), (80, 0), (88, 34), (84, 74), (70, 50)]), 'skin_d', 'b', False)] + _scales(12) + _scales(88))

# Curtis (Curses) Carson: capucha de tela crema con un gorro naranja de orejas de gato remendado encima, una máscara marrón
# que le tapa los ojos (con dos ojazos rojos), el pañuelo crema atado al cuello y la boca enfurruñada
CRM, ORG, MSK = _c('#efdfc2'), _c('#c46817'), _c('#6e5542')
def _curtis(view):
    if view == 'front':
        return [L(outline([(10, 20), (6, -10, 1), (26, 6)]), ORG, 'b'), L(outline([(90, 20), (94, -10, 1), (74, 6)]), ORG, 'b')] + \
            hood('front', CRM, top=0, low=104, face_hole=[(22, 100), (18, 72), (24, 52), (50, 46), (76, 52), (82, 72), (78, 100), (50, 108)]) + \
            [L(blob([(14, 50), (16, 24), (34, 6), (50, 2), (66, 6), (84, 24), (86, 50), (70, 40), (50, 38), (30, 40)], 6), ORG, 'f'),
             strand([(30, 20), (36, 30)], _c('#8a4010'), 'f', 1.2), strand([(68, 18), (62, 28)], _c('#8a4010'), 'f', 1.2),
             L(blob([(18, 60), (34, 52), (50, 58), (66, 52), (82, 60), (80, 82), (64, 88), (50, 86), (36, 88), (20, 82)], 6), MSK, 'f')] + \
            [L(ell(36, 74, 7, 6), WHITE, 'f'), L(ell(64, 74, 7, 6), WHITE, 'f'), L(ell(36, 74, 4.4, 4.4), RED, 'f', False), L(ell(64, 74, 4.4, 4.4), RED, 'f', False),
             L(ell(36, 74, 2, 2), BLACK, 'f', False), L(ell(64, 74, 2, 2), BLACK, 'f', False)] + scarf('front', CRM, 102, 12)
    if view == 'side':
        return [L(outline([(34, 10), (36, -18, 1), (52, 4)]), ORG, 'b')] + hood('side', CRM, top=0) + \
            [L(blob([(10, 40), (20, 10), (50, 2), (80, 10), (90, 30), (60, 34), (30, 44)], 6), ORG, 'f'),
             L(blob([(64, 60), (90, 58), (92, 82), (70, 86)], 6), MSK, 'f'), L(ell(84, 72, 4, 5), WHITE, 'f'), L(ell(85, 72, 2.6, 3), RED, 'f', False)] + scarf('side', CRM, 102, 12)
    return [L(outline([(10, 20), (6, -10, 1), (26, 6)]), ORG, 'b'), L(outline([(90, 20), (94, -10, 1), (74, 6)]), ORG, 'b')] + hood('back', CRM, top=0) + \
        [L(blob([(10, 50), (14, 22), (34, 4), (50, 0), (66, 4), (86, 22), (90, 50), (50, 44)], 6), ORG, 'f'), L(outline([(40, 96), (50, 112, 1), (60, 96)]), CRM, 'f')]
C('curtis-curses-carson', 'normal', P('#efdfc2', '#bb9682', iris='#c82a1e'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, hairline=False, ears=False),
  _curtis('front'), _curtis('side'), _curtis('back'))

# Cutter Shorten: pañuelo azul grisáceo que le tapa la cabeza, atado bajo la barbilla; cara ancha morena de mandíbula grande,
# cejas arqueadas, ojos afilados, nariz gorda rosada y una sonrisa de dientes
KER = _c('#709cb0')
C('cutter-shorten', 'normal', P('#709cb0', '#ce9568', iris='#1e1a1a', shade='#5a7e8e'),
  F(eyes='sharp', brows='angry', mouth='none', face_front=face(w=4, chin=106, jaw=3), face_side=face_side(chin=6, jaw=3, nose=3), hairline=False, ears=False),
  hood('front', KER, top=0, low=100, face_hole=[(18, 100), (14, 70), (20, 48), (50, 42), (80, 48), (86, 70), (82, 100), (50, 110)]) +
  [L(outline([(40, 102), (50, 98), (60, 102), (66, 116, 1), (50, 108), (34, 116, 1)]), KER, 'f'), L(ell(50, 86, 5, 3.4), _c('#e08a7a'), 'f')] + teeth_grin(94, 12, 5),
  hood('side', KER, top=0) + [L(ell(91, 86, 3, 3), _c('#e08a7a'), 'f')],
  hood('back', KER, top=0, low=100) + [L(outline([(42, 100), (50, 96), (58, 100), (54, 112, 1), (46, 112, 1)]), KER, 'f')])

# Damon Sumner: capucha negra con dos cuernos curvos y una costura cosida en medio; máscara roja de pájaro con un pico largo
# que le tapa la cara y deja ver los ojos verdes
HD, HDD, BIRD = _c('#443e3d'), _c('#2d2423'), _c('#9a2e2c')
def _damon(view):
    if view == 'front':
        return [L(outline([(12, 30), (2, 0), (8, -26, 1), (16, 6), (24, 20)]), HDD, 'b'), L(outline([(88, 30), (98, 0), (92, -26, 1), (84, 6), (76, 20)]), HDD, 'b')] + \
            hood('front', HD, top=-6, low=106, face_hole=[(22, 104), (20, 80), (26, 62), (50, 56), (74, 62), (80, 80), (78, 104), (50, 112)], rim=HDD) + \
            [L([(50, -4), (50, 56)], BLACK, 'f', False, False, 1.4)] + [L([(46, k), (54, k + 6)], BLACK, 'f', False, False, 1.2) for k in (4, 18, 32, 46)] + \
            [L(blob([(20, 66), (36, 62), (50, 70), (64, 62), (80, 66), (74, 80), (58, 84), (50, 112), (42, 84), (26, 80)], 6), BIRD, 'f'),
             L(blob([(28, 70), (38, 68), (42, 74), (32, 76)], 4), _c('#4ab090'), 'f', False), L(blob([(72, 70), (62, 68), (58, 74), (68, 76)], 4), _c('#4ab090'), 'f', False)]
    if view == 'side':
        return [L(outline([(30, 14), (26, -20, 1), (44, 6)]), HDD, 'b')] + hood('side', HD, top=-6, rim=HDD) + \
            [L(blob([(66, 62), (88, 62), (106, 96, 1), (84, 84), (68, 82)], 6), BIRD, 'f'), L(ell(82, 70, 3, 2.4), _c('#4ab090'), 'f', False)]
    return [L(outline([(12, 30), (2, 0), (8, -26, 1), (16, 6), (24, 20)]), HDD, 'b'), L(outline([(88, 30), (98, 0), (92, -26, 1), (84, 6), (76, 20)]), HDD, 'b')] + \
        hood('back', HD, top=-6, rim=HDD) + [L([(50, -4), (50, 100)], BLACK, 'f', False, False, 1.4)]
C('damon-sumner', 'normal', P('#443e3d', '#c08a6a', iris='#4ab090'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _damon('front'), _damon('side'), _damon('back'))

# Dan Fei: gorro redondo rojo con un botón dorado y un moño azul encima; patillas azul grisáceo que se abren en punta, cejas
# enormes azules en pico, nariz gorda, ojos cerrados y boca enfurruñada; cara ancha
CAPR = _c('#d03b04')
C('dan-fei', 'corpulento', P('#334553', '#dca459', iris='#1e1a1a', shade='#2a3a46'),
  F(eyes='closed', brows=False, mouth='frown', mouth_y=97, face_front=face(w=6, chin=106, jaw=4), face_side=face_side(chin=6, jaw=4, nose=4), ear_out=5, hairline=False),
  [L(outline([(16, 62), (2, 88, 1), (14, 82), (8, 100, 1), (22, 84), (22, 64)])), L(outline([(84, 62), (98, 88, 1), (86, 82), (92, 100, 1), (78, 84), (78, 64)])),
   L(ell(50, 6, 6, 6)), L([(50, 10), (50, 20)], 'mid', 'b', False, False, 4), L(blob([(10, 54), (12, 28), (30, 16), (50, 14), (70, 16), (88, 28), (90, 54), (50, 50)], 6), CAPR, 'f'),
   L(ell(50, 22, 3.4, 3.4), GOLD, 'f')] +
  [L(outline([(24, 64), (32, 58), (44, 64), (42, 70, 1), (34, 66), (26, 70, 1)]), 'mid', 'f'), L(outline([(76, 64), (68, 58), (56, 64), (58, 70, 1), (66, 66), (74, 70, 1)]), 'mid', 'f'),
   L(ell(50, 86, 7, 5.4), 'skin_d', 'f')],
  [L(outline([(52, 62), (44, 92, 1), (56, 82), (60, 64)])), L(ell(44, 6, 6, 6)), L(blob([(6, 56), (10, 26), (40, 14), (80, 18), (92, 36), (90, 54), (50, 52)], 6), CAPR, 'f'),
   L(outline([(74, 62), (84, 58), (88, 66), (82, 68)]), 'mid', 'f'), L(ell(90, 86, 4, 5), 'skin_d', 'f')],
  [L(outline([(16, 62), (8, 92, 1), (22, 84), (84, 84), (92, 92, 1), (84, 62)])), L(ell(50, 6, 6, 6)),
   L(blob([(8, 56), (12, 28), (30, 16), (50, 14), (70, 16), (88, 28), (92, 56), (50, 52)], 6), CAPR, 'f')])

# Debra (Brolly) Lee: melena castaño rojizo larga y ondulada con la raya en medio; gafas grandes de montura blanca con los
# cristales verdes sobre los ojos y una sonrisa
LENS = _c('#9ad0a0')
def _goggles_w(view):
    if view == 'front':
        out = []
        for cx in (35, 65):
            out += [L(blob([(cx - 13, 70), (cx, 66), (cx + 13, 70), (cx + 12, 82), (cx, 84), (cx - 12, 82)], 6), _c('#efefe4'), 'f'),
                    L(blob([(cx - 9, 72), (cx, 70), (cx + 9, 72), (cx + 8, 80), (cx, 81), (cx - 8, 80)], 6), LENS, 'f', False)]
        return out
    return [L(blob([(72, 68), (90, 68), (92, 82), (74, 84)], 6), _c('#efefe4'), 'f'), L(blob([(76, 71), (88, 71), (89, 80), (77, 81)], 6), LENS, 'f', False),
            L([(72, 74), (44, 70)], _c('#efefe4'), 'f', False, False, 3)]
C('debra-brolly-lee', 'chica', P('#823b0e', '#f6be94', iris='#3a2a20', shade='#632c10'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=92, hairline=[(6, 66), (18, 46), (36, 40), (50, 44), (64, 40), (82, 46), (94, 66)]),
  dome('front', top=2, w=46, cy=46, n=6, amp=6, soft=True, seed=15, long=112, flare=8, ends=5) + _goggles_w('front'),
  dome('side', top=2, w=46, cy=46, n=6, amp=6, soft=True, seed=15, long=112, flare=8, fr=50) + _goggles_w('side'),
  dome('back', top=2, w=46, cy=46, n=6, amp=6, soft=True, seed=15, long=112, flare=8, ends=6))

# Decker (Deck) Pile (portero): pelo corto verde oliva oscuro alborotado, con mechones de punta por la frente; ojos negros
# afilados y una sonrisa pícara
C('decker-deck-pile', 'normal', P('#454531', '#fbc273', iris='#141414'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=92, hairline=hl(5, 62, 46, 58, lean=1, jit=3, seed=21)),
  dome('front', top=0, w=46, cy=44, n=8, amp=8, seed=21, sb=64),
  dome('side', top=0, w=46, cy=44, n=8, amp=8, seed=21, nape=84, fr=50),
  dome('back', top=0, w=46, cy=44, n=8, amp=8, seed=21, nape=84))

# Dee (Powers) Tarrant (portero): pañoleta atada con la mitad azul con una estrella amarilla y la mitad roja; gafas de sol
# negras; cara enorme muy pálida y ancha, la boca en un mohín y el pelo oscuro por los lados
BLUE, STAR = _c('#2c4989'), _c('#f0c030')
def _star(cx, cy, r, c=STAR):
    import math
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)) + ((1,) if i % 2 == 0 else ()))
    return L(outline(pts, 2), c, 'f', False)
C('dee-powers-tarrant', 'corpulento', P('#4a413c', '#feefd3', iris='#141414'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, face_front=face(w=8, chin=106, jaw=6), face_side=face_side(chin=6, jaw=6), ear_out=6, hairline=False),
  [L(outline([(12, 62), (8, 90), (16, 92), (18, 64)])), L(outline([(88, 62), (92, 90), (84, 92), (82, 64)])),
   L(blob([(6, 62), (8, 32), (26, 12), (50, 6), (74, 12), (92, 32), (94, 62), (50, 56)], 6), BLUE, 'f'),
   L(blob([(50, 6), (74, 12), (92, 32), (94, 62), (50, 56)], 6), RED, 'f', False), _star(34, 32, 9), _star(14, 50, 5),
   L(blob([(20, 70), (40, 68), (48, 72), (52, 72), (60, 68), (80, 70), (76, 80), (60, 80), (52, 76), (48, 76), (40, 80), (24, 80)], 6), BLACK, 'f'),
   L(ell(50, 84, 5, 3.4), 'skin_d', 'f')],
  [L(outline([(52, 62), (48, 92), (56, 92), (60, 64)])), L(blob([(4, 64), (6, 30), (40, 8), (80, 16), (94, 40), (92, 60), (50, 58)], 6), RED, 'f'),
   L(blob([(66, 70), (92, 70), (90, 80), (68, 80)], 6), BLACK, 'f'), L([(66, 74), (44, 70)], BLACK, 'f', False, False, 2.4)],
  [L(outline([(12, 62), (10, 92), (90, 92), (88, 62)])), L(blob([(6, 66), (8, 32), (26, 12), (50, 6), (74, 12), (92, 32), (94, 66), (50, 62)], 6), BLUE, 'f'),
   L(blob([(50, 6), (74, 12), (92, 32), (94, 66), (50, 62)], 6), RED, 'f', False), L(outline([(40, 64), (34, 82, 1), (50, 68), (66, 82, 1), (60, 64)]), RED, 'f')])

# Demerara Kane: cabeza redonda morena anaranjada, pelo verde oliva rapado con una mata amarilla rizada encima; ojillos,
# coloretes y una sonrisa enorme de dientes
YEL = _c('#f0d040')
C('demerara-kane', 'corpulento', P('#6a6a30', '#dda256', iris='#2a3a5a'),
  F(eyes='dot', brows=False, mouth='none', face_front=face(w=8, chin=104, jaw=6), face_side=face_side(chin=4, jaw=6), ear_out=6,
    hairline=[(8, 60), (20, 46), (36, 40), (50, 42), (64, 40), (80, 46), (92, 60)]),
  crop('front', top=6, side=56, w=4) + [L(blob([(36, 10), (40, -2), (50, -8), (60, -2), (64, 10), (56, 18), (44, 18)], 8), YEL, 'f')] + big_grin(92, 16, 8) +
  blush(86, _c('#e08a6a'), 26),
  crop('side', top=6, nape=76, w=4) + [L(blob([(36, 6), (44, -6), (56, -6), (62, 6), (52, 14)], 8), YEL, 'f')],
  crop('back', top=6, nape=76, w=4) + [L(blob([(36, 10), (40, -2), (50, -8), (60, -2), (64, 10), (56, 18), (44, 18)], 8), YEL, 'f')])

# Derry Farmer: gorro de aviador verde oliva con una franja crema en medio, orejeras largas y unas gafas grandes de montura
# gris; nariz roja y una sonrisa de dientes
AV, AVL = _c('#676726'), _c('#e4e1cd')
def _aviator(view):
    if view == 'front':
        return [L(blob([(10, 66), (8, 32), (24, 8), (50, 0), (76, 8), (92, 32), (90, 66), (80, 56), (50, 52), (20, 56)], 6), AV, 'f'),
                L(outline([(46, 2), (54, 2), (55, 52), (45, 52)]), AVL, 'f', False), L(outline([(76, 6), (92, -4, 1), (86, 14)]), AV, 'f'),
                L(outline([(10, 60), (22, 60), (20, 104), (12, 108)]), AV, 'f'), L(outline([(90, 60), (78, 60), (80, 104), (88, 108)]), AV, 'f'),
                L([(16, 64), (16, 104)], AVL, 'f', False, False, 1.6), L([(84, 64), (84, 104)], AVL, 'f', False, False, 1.6)] + \
            [x for cx in (35, 65) for x in (L(blob([(cx - 13, 68), (cx + 13, 68), (cx + 13, 84), (cx - 13, 84)], 4), _c('#909090'), 'f'),
                                            L(blob([(cx - 9, 71), (cx + 9, 71), (cx + 9, 81), (cx - 9, 81)], 4), _c('#e8e0d0'), 'f', False))]
    if view == 'side':
        return [L(blob([(4, 70), (4, 30), (30, 4), (60, 0), (86, 16), (92, 50), (70, 56), (50, 60), (30, 70)], 6), AV, 'f'),
                L(outline([(30, 4), (36, 2), (20, 66), (14, 66)]), AVL, 'f', False), L(outline([(40, 60), (54, 60), (52, 106), (42, 108)]), AV, 'f'),
                L(blob([(72, 68), (92, 68), (92, 84), (74, 84)], 4), _c('#909090'), 'f'), L(blob([(76, 71), (90, 71), (90, 81), (77, 81)], 4), _c('#e8e0d0'), 'f', False),
                L([(72, 74), (54, 72)], _c('#909090'), 'f', False, False, 3)]
    return [L(blob([(8, 76), (8, 32), (24, 8), (50, 0), (76, 8), (92, 32), (92, 76), (50, 84)], 6), AV, 'f'),
            L(outline([(46, 2), (54, 2), (55, 82), (45, 82)]), AVL, 'f', False), L(quad((8, 72), (50, 78), (92, 72)), _c('#909090'), 'f', False, False, 3)]
C('derry-farmer', 'normal', P('#676726', '#f8c174', iris='#1e1a1a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _aviator('front') + [L(ell(50, 86, 4, 3.4), _c('#d84a2a'), 'f')] + big_grin(92, 12, 7),
  _aviator('side') + [L(ell(90, 86, 3, 3), _c('#d84a2a'), 'f')],
  _aviator('back'))

# Des Einer: pelo rubio dorado enorme en mechones abultados echados a un lado, que le tapa la mitad de la cara y un ojo; ojo
# azul y la boca seria
C('des-einer', 'normal', P('#dbb257', '#f5e2ca', iris='#3a6aa0', shade='#a9763e'),
  F(eyes='normal', brows=True, mouth='line', mouth_y=92, hairline=[(6, 64), (18, 46), (36, 40), (56, 44), (76, 48), (94, 66)]),
  dome('front', top=-6, w=50, cy=42, n=8, amp=12, sweep=0.6, soft=True, seed=33, sb=74) +
  [L(outline([(40, 26), (70, 26), (88, 46), (88, 70), (78, 88, 1), (72, 72), (60, 62), (52, 44)]), 'mid', 'f'),
   strand([(58, 34), (72, 54), (76, 76)], 'shade', 'f', 1.2)],
  dome('side', top=-6, w=50, cy=42, n=8, amp=12, sweep=0.6, soft=True, seed=33, nape=86, fr=52) +
  [L(outline([(70, 30), (94, 38), (98, 62), (90, 80, 1), (82, 62)]), 'mid', 'f')],
  dome('back', top=-6, w=50, cy=42, n=8, amp=12, sweep=0.6, soft=True, seed=33, nape=86))

# Devlin (Grrrar) Ogor (portero): ogro de piel rosa, calvo, con unas cejas negras tatuadas en uve que le enmarcan los ojos
# blancos, dos colmillos grandes que salen por los lados de la boca, orejas grandes y la boca enfurruñada
TUSK = _c('#efe4c8')
C('devlin-grrrar-ogor', 'corpulento', P('#ea9284', '#ea9284', iris='#141414'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=98, face_front=face(w=8, chin=108, jaw=8), face_side=face_side(chin=8, jaw=8), big_ears=3, ear_out=7, hairline=False),
  skull3('front') + [L(blob([(22, 68), (32, 58), (44, 64), (50, 72), (56, 64), (68, 58), (78, 68), (70, 82), (56, 78), (50, 84), (44, 78), (30, 82)], 6), BLACK, 'f', False),
                     L(blob([(28, 70), (36, 66), (44, 72), (36, 76)], 4), WHITE, 'f', False), L(blob([(72, 70), (64, 66), (56, 72), (64, 76)], 4), WHITE, 'f', False),
                     L(quad((22, 46), (40, 30), (46, 54)), BLACK, 'f', False, False, 2.2), L(quad((78, 46), (60, 30), (54, 54)), BLACK, 'f', False, False, 2.2),
                     L(outline([(18, 98), (12, 84, 1), (26, 92)]), TUSK, 'f'), L(outline([(82, 98), (88, 84, 1), (74, 92)]), TUSK, 'f')],
  skull3('side') + [L(blob([(72, 66), (88, 64), (88, 80), (74, 78)], 4), BLACK, 'f', False), L(ell(83, 72, 3, 2.4), WHITE, 'f', False),
                    L(outline([(72, 98), (70, 82, 1), (80, 92)]), TUSK, 'f')],
  skull3('back'))

# Dextra Gleeson: media melena verde claro hasta la barbilla, con flequillo de mechones, un moño crema arriba sujeto con una
# cinta oscura; ojos azules grandes y boca pequeña
DXB = _c('#ece0c4')
C('dextra-gleeson', 'chica', P('#a2c27d', '#fae8b8', iris='#3a8ab8', shade='#818661'),
  F(eyes='big', brows=True, mouth='line', mouth_y=92, hairline=hl(5, 66, 46, 60, jit=3, seed=41)),
  [L(ell(50, -6, 12, 10), DXB, 'b'), L(blob([(36, 2), (50, -2), (64, 2), (64, 8), (50, 6), (36, 8)], 4), _c('#2a4a40'), 'b')] +
  dome('front', top=4, w=45, cy=46, long=98, flare=2, ends=3) + lashes(),
  [L(ell(40, -6, 12, 10), DXB, 'b')] + dome('side', top=4, w=45, cy=46, long=98, flare=2, fr=58) + lash_side(),
  [L(ell(50, -6, 12, 10), DXB, 'b')] + dome('back', top=4, w=45, cy=46, long=98, flare=2, ends=4))

# Dino Zolletta: melena rubia caqui enorme en mechones anchos de punta, echada hacia un lado y que le cubre media frente;
# ojos azules afilados y sonrisa pícara
C('dino-zolletta', 'normal', P('#af9862', '#f7e1c8', iris='#3a5a8a', shade='#876b4c'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=92, hairline=[(6, 64), (18, 46), (34, 40), (52, 46), (66, 52), (80, 54), (94, 66)]),
  dome('front', top=-8, w=50, cy=42, n=6, amp=16, sweep=-0.6, seed=43, long=100, flare=10, ends=3) +
  [L(outline([(26, 24), (56, 22), (62, 44), (58, 62, 1), (48, 48), (36, 42)]), 'mid', 'f')],
  dome('side', top=-8, w=50, cy=42, n=6, amp=16, sweep=-0.6, seed=43, long=100, flare=10, fr=50),
  dome('back', top=-8, w=50, cy=42, n=6, amp=16, sweep=-0.6, seed=43, long=100, flare=10, ends=3))

# Direm Ederi: pañuelo verde oliva enrollado en la cabeza sobre otro crema, con una cola larga que le cae por un lado; asoma
# un flequillo negro en punta; bufanda crema al cuello, ojos castaños y gesto serio
TUR, TURC = _c('#706932'), _c('#ded0bf')
def _turban(view):
    if view == 'front':
        return [L(blob([(8, 60), (8, 30), (24, 6), (50, 0), (76, 6), (92, 30), (92, 60), (50, 52)], 6), TURC, 'f'),
                L(blob([(6, 50), (10, 30), (50, 22), (90, 30), (94, 50), (50, 46)], 6), TUR, 'f'),
                L(outline([(84, 40), (96, 44), (98, 100), (92, 112, 1), (88, 96)]), TUR, 'f'),
                L(outline([(34, 50), (50, 44), (66, 50), (58, 58, 1), (52, 52), (44, 60, 1), (38, 52)]), 'mid', 'f')]
    if view == 'side':
        return [L(blob([(4, 70), (4, 30), (30, 4), (60, 0), (86, 16), (92, 50), (60, 56), (30, 70)], 6), TURC, 'f'),
                L(blob([(2, 50), (30, 26), (88, 30), (92, 46), (30, 50), (4, 64)], 6), TUR, 'f'), L(outline([(10, 44), (2, 50), (0, 104), (8, 110, 1), (14, 70)]), TUR, 'f')]
    return [L(blob([(8, 76), (8, 30), (24, 6), (50, 0), (76, 6), (92, 30), (92, 76), (50, 84)], 6), TURC, 'f'),
            L(blob([(6, 54), (10, 30), (50, 22), (90, 30), (94, 54), (50, 50)], 6), TUR, 'f'), L(outline([(10, 44), (2, 48), (4, 104), (10, 112, 1), (16, 70)]), TUR, 'f')]
C('direm-ederi', 'normal', P('#2a2620', '#daa35b', iris='#5a3a20'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=92, hairline=False),
  _turban('front') + scarf('front', TURC, 104, 10), _turban('side') + scarf('side', TURC, 104, 10), _turban('back') + scarf('back', TURC, 104, 10))

# Dirk (Motocr) Byker: casco integral de motocross azul con la visera negra, dos ojos amarillos pintados en ella y unas
# rejillas negras en la barbilla: no se le ve la cara
HEL, HELD = _c('#0d67ad'), _c('#06426d')
def _moto(view):
    if view == 'front':
        return [L(blob([(4, 70), (4, 30), (20, 6), (50, -4), (80, 6), (96, 30), (96, 70), (84, 100), (50, 110), (16, 100)], 8), HEL, 'f'),
                L(blob([(62, 0), (84, 10), (96, 40), (94, 74), (82, 98), (76, 60)], 6), HELD, 'f', False),
                L(blob([(14, 56), (30, 44), (50, 42), (70, 44), (86, 56), (82, 72), (50, 70), (18, 72)], 6), _c('#9ab0c0'), 'f'),
                L(blob([(18, 60), (32, 52), (50, 50), (68, 52), (82, 60), (78, 74), (50, 72), (22, 74)], 6), BLACK, 'f', False),
                L(blob([(24, 62), (40, 60), (44, 68), (28, 68)], 4), _c('#f0e020'), 'f', False), L(blob([(76, 62), (60, 60), (56, 68), (72, 68)], 4), _c('#f0e020'), 'f', False)] + \
            [L([(30 + 6 * k, 86 + abs(k - 2) * -1), (34 + 6 * k, 92)], BLACK, 'f', False, False, 2.2) for k in (0, 1)] + \
            [L([(70 - 6 * k, 86), (66 - 6 * k, 92)], BLACK, 'f', False, False, 2.2) for k in (0, 1)]
    if view == 'side':
        return [L(blob([(2, 70), (4, 30), (30, 2), (60, -4), (88, 12), (100, 46), (100, 80), (88, 104), (50, 110), (14, 98)], 8), HEL, 'f'),
                L(blob([(64, 48), (98, 50), (98, 74), (66, 72)], 6), BLACK, 'f'), L(blob([(84, 58), (96, 58), (96, 66), (86, 66)], 4), _c('#f0e020'), 'f', False),
                L(blob([(4, 50), (40, 50), (60, 80), (50, 104), (16, 96)], 6), HELD, 'f', False)]
    return [L(blob([(4, 72), (4, 30), (20, 6), (50, -4), (80, 6), (96, 30), (96, 72), (84, 100), (50, 108), (16, 100)], 8), HEL, 'f'),
            L(blob([(62, 0), (84, 10), (96, 40), (94, 74), (82, 98), (70, 60)], 6), HELD, 'f', False), L([(50, -2), (50, 106)], _c('#9ab0c0'), 'f', False, False, 2.4)]
C('dirk-motocr-byker', 'normal', P('#0d67ad', '#f1c79b', iris='#141414'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _moto('front'), _moto('side'), _moto('back'))

# Dorian (Luchador) Lucenzo: pelo castaño oscuro echado atrás en una coleta alta y larguísima atada con un aro, que se curva
# hacia un lado; pintura de guerra naranja alrededor de los ojos que baja por las mejillas; ojos verdes, perilla y ceño
WAR = _c('#d86a1e')
C('dorian-luchador-lucenzo', 'normal', P('#612503', '#daaa69', iris='#3a9a4a', shade='#431d0c'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=92, hairline=[(8, 62), (18, 44), (34, 36), (50, 34), (66, 36), (82, 44), (92, 62)]),
  [L(outline([(44, 10), (40, -8), (30, -20), (20, -16), (8, 10), (2, 60), (-6, 104, 1), (8, 76), (16, 30), (26, -4), (36, 4)])),
   L(ell(44, 2, 6, 5), _c('#a0662a'), 'b')] + crop('front', top=4, side=62) +
  [L(blob([(24, 70), (42, 70), (48, 64), (46, 80), (38, 96, 1), (34, 80), (22, 76)], 4), WAR, 'f', False),
   L(blob([(76, 70), (58, 70), (52, 64), (54, 80), (62, 96, 1), (66, 80), (78, 76)], 4), WAR, 'f', False)] + sharp_eyes(_c('#3a9a4a')) +
  [L([(46, 100), (50, 104), (54, 100)], _c('#431d0c'), 'f', False, False, 1.4)],
  [L(outline([(36, 4), (20, -12), (4, -8), (-6, 20), (-10, 70), (-14, 104, 1), (0, 70), (6, 20), (20, 4)])), L(ell(36, 2, 6, 5), _c('#a0662a'), 'b')] +
  crop('side', top=4, nape=80) + [L(blob([(70, 70), (88, 68), (86, 80), (80, 94, 1), (74, 80)], 4), WAR, 'f', False)] + sharp_eye_side(_c('#3a9a4a')),
  crop('back', top=4, nape=80) + [L(outline([(40, 10), (36, -8), (24, -18), (12, -10), (8, 30), (6, 104, 1), (16, 60), (22, 6), (32, 0)])), L(ell(44, 4, 6, 5), _c('#a0662a'), 'f')])

# Doug Boateng: pelo verde menta muy claro en pinchos revueltos, con un pañuelo rojo encima de la frente; dos tiras de cuentas
# amarillas cuelgan junto a la cara; rayas rojas pintadas en las mejillas y ojos amarillos
RB = _c('#ba0202')
def _beads(x):
    return [L([(x, 66), (x, 104)], _c('#f4b650'), 'f', False, False, 4.0)] + [L([(x - 2.4, y), (x + 2.4, y)], _c('#b07020'), 'f', False, False, 1.0) for y in range(72, 104, 6)]
C('doug-boateng', 'normal', P('#c1d2ab', '#f4b650', iris='#e0c020', shade='#938972'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=93, hairline=False),
  dome('front', top=-8, w=52, cy=42, n=11, amp=13, seed=45, long=104, flare=12, ends=4) +
  [L(blob([(14, 62), (16, 42), (34, 32), (50, 30), (66, 32), (84, 42), (86, 62), (50, 58)], 6), RB, 'f')] + _beads(20) + _beads(80) +
  [mark([(22, 84), (40, 84), (40, 88), (22, 88)], RB), mark([(60, 84), (78, 84), (78, 88), (60, 88)], RB)],
  dome('side', top=-8, w=52, cy=42, n=11, amp=13, seed=45, long=104, flare=12, fr=50) +
  [L(blob([(10, 54), (30, 34), (70, 30), (90, 40), (90, 58), (50, 60)], 6), RB, 'f'), L([(56, 66), (56, 104)], _c('#f4b650'), 'f', False, False, 4.0),
   mark([(76, 84), (88, 84), (88, 88), (76, 88)], RB)],
  dome('back', top=-8, w=52, cy=42, n=11, amp=13, seed=45, long=104, flare=12, ends=5) + [L(blob([(14, 50), (16, 28), (34, 12), (50, 8), (66, 12), (84, 28), (86, 50), (50, 46)], 6), RB, 'f')])

# Drysden Waller: pinchos verde hierba de punta hacia arriba; piel muy pálida, cara alargada, pintura negra en lágrimas bajo
# los ojos y unas rayas cosidas en la boca
C('drysden-waller', 'delgado', P('#5b7825', '#e2d0b4', iris='#141414', shade='#46501e'),
  F(eyes='sharp', brows='angry', mouth='none', face_front=face(chin=108), face_side=face_side(chin=8), ear_out=2, hairline=[(10, 60), (20, 44), (36, 40), (50, 42), (64, 40), (80, 44), (90, 60)]),
  dome('front', top=-16, w=44, cy=36, n=7, amp=16, seed=47, sb=56) +
  [L(outline([(28, 76), (34, 92, 1), (40, 76)]), BLACK, 'f', False), L(outline([(60, 76), (66, 92, 1), (72, 76)]), BLACK, 'f', False)] +
  [L([(34, 98 + k * 3), (66, 98 + k * 3)], _c('#8a5a3a'), 'f', False, False, 1.2) for k in range(3)],
  dome('side', top=-16, w=44, cy=36, n=7, amp=16, seed=47, nape=72, fr=42) + [L(outline([(78, 78), (82, 92, 1), (86, 78)]), BLACK, 'f', False)],
  dome('back', top=-16, w=44, cy=36, n=7, amp=16, seed=47, nape=72))

# Earl E. Bird (portero): melena castaña desgreñada hasta los hombros en mechones de punta; ojos afilados con una raya roja,
# colmillos y la boca abierta enfadada
C('earl-ee-bird', 'normal', P('#745b2b', '#f4edca', iris='#3a3048', shade='#5a4123'),
  F(eyes='sharp', brows='angry', mouth='none', hairline=hl(5, 64, 44, 56, jit=4, seed=49)),
  dome('front', top=-2, w=48, cy=44, n=8, amp=12, seed=49, long=98, flare=12, ends=3) +
  [L([(22, 70), (28, 66)], RED, 'f', False, False, 1.6), L([(78, 70), (72, 66)], RED, 'f', False, False, 1.6),
   L(blob([(40, 92), (50, 90), (60, 92), (56, 98), (44, 98)], 4), _c('#6a2a2a'), 'f'),
   L(outline([(42, 92), (44, 97, 1), (46, 92)]), WHITE, 'f', False), L(outline([(54, 92), (56, 97, 1), (58, 92)]), WHITE, 'f', False)],
  dome('side', top=-2, w=48, cy=44, n=8, amp=12, seed=49, long=98, flare=12, fr=52),
  dome('back', top=-2, w=48, cy=44, n=8, amp=12, seed=49, long=98, flare=12, ends=4))

# Earle Humble: pelo negro con un mechón largo blanco rosado que le cruza la frente y cae por un lado; orejas de punta, ojos
# morados afilados y la boca enfurruñada
PKW = _c('#e8d0dc')
C('earle-humble', 'normal', P('#2b2b2e', '#f8dcc2', iris='#8a3ab0'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, ears=False, hairline=[(6, 64), (18, 46), (36, 40), (54, 44), (72, 46), (94, 64)]),
  ears_pointy('front', h=14) + dome('front', top=0, w=46, cy=44, n=6, amp=8, sweep=-0.5, seed=51, sb=70) +
  [L(outline([(40, 6), (56, -8, 1), (62, 10), (58, 40), (48, 70), (40, 86, 1), (42, 60), (46, 32)]), PKW, 'f')],
  ears_pointy('side', h=14) + dome('side', top=0, w=46, cy=44, n=6, amp=8, sweep=-0.5, seed=51, nape=86, fr=52) +
  [L(outline([(60, -4), (72, -10, 1), (80, 14), (88, 50), (84, 70, 1), (78, 40)]), PKW, 'f')],
  ears_pointy('back', h=14) + dome('back', top=0, w=46, cy=44, n=6, amp=8, sweep=-0.5, seed=51, nape=86) +
  [L(outline([(44, 0), (56, -8, 1), (60, 10), (56, 40), (50, 50)]), PKW, 'f')])

# Edison Ford: pelo granate oscuro en casco abultado con una franja crema que lo cruza de delante atrás, como una cresta;
# dos tapones crema en las orejas, ojos negros afilados y sonrisa
CRM2 = _c('#f4f0cc')
C('edison-ford', 'normal', P('#700102', '#f6bc80', iris='#141414', shade='#560906'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=92, ears=False, hairline=[(6, 66), (14, 50), (30, 56), (50, 60), (70, 56), (86, 50), (94, 66)]),
  bowl3('front', top=-4, side=86, w=4, fringe=58) + [L(outline([(42, -2), (58, -2), (58, 60), (50, 66, 1), (42, 60)]), CRM2, 'f'),
                                                    L(ell(14, 82, 5, 6), CRM2, 'f'), L(ell(86, 82, 5, 6), CRM2, 'f')],
  bowl3('side', top=-4, nape=92, w=4) + [L(outline([(30, -4), (60, -6), (88, 26), (82, 34), (56, 4), (30, 4)]), CRM2, 'f'), L(ell(52, 82, 5, 6), CRM2, 'f')],
  bowl3('back', top=-4, nape=92, w=4) + [L(outline([(42, -2), (58, -2), (58, 92), (42, 92)]), CRM2, 'f')])

# Eldritch Priest (portero): capucha de cuero marrón con dos cuernos y remiendos crema; la cara queda en sombra, con dos ojos
# amarillos que brillan y la parte de abajo de la cara naranja
LEA, LEAC = _c('#89604a'), _c('#e8dcc2')
def _eldritch(view):
    if view == 'front':
        return [L(outline([(10, 40), (-6, 14), (-10, -16, 1), (8, 6), (22, 24)]), LEAC, 'b'), L(outline([(90, 40), (106, 14), (110, -16, 1), (92, 6), (78, 24)]), LEAC, 'b')] + \
            hood('front', LEA, top=-4, low=108, face_hole=[(22, 104), (18, 76), (24, 56), (50, 50), (76, 56), (82, 76), (78, 104), (50, 112)], rim=_c('#6b4737')) + \
            [L(blob([(60, 4), (80, 14), (88, 34), (70, 30)], 6), LEAC, 'f', False), L(blob([(4, 70), (14, 60), (18, 90), (8, 98)], 6), LEAC, 'f', False),
             L(blob([(22, 60), (50, 54), (78, 60), (80, 82), (50, 84), (20, 82)], 6), _c('#2a2220'), 'f', False),
             L(ell(36, 72, 6, 6), _c('#d8d040'), 'f', False), L(ell(64, 72, 6, 6), _c('#d8d040'), 'f', False),
             L(ell(36, 72, 2.4, 2.4), BLACK, 'f', False), L(ell(64, 72, 2.4, 2.4), BLACK, 'f', False),
             L(blob([(36, 82), (50, 80), (50, 92), (44, 96)], 4), _c('#8a7060'), 'f', False)]
    if view == 'side':
        return [L(outline([(30, 20), (24, -16, 1), (46, 10)]), LEAC, 'b')] + hood('side', LEA, top=-4, rim=_c('#6b4737')) + \
            [L(blob([(70, 58), (88, 58), (90, 82), (72, 82)], 6), _c('#2a2220'), 'f', False), L(ell(82, 70, 4, 4), _c('#d8d040'), 'f', False),
             L(blob([(20, 30), (40, 20), (44, 44), (26, 46)], 6), LEAC, 'f', False)]
    return [L(outline([(10, 40), (-6, 14), (-10, -16, 1), (8, 6), (22, 24)]), LEAC, 'b'), L(outline([(90, 40), (106, 14), (110, -16, 1), (92, 6), (78, 24)]), LEAC, 'b')] + \
        hood('back', LEA, top=-4, rim=_c('#6b4737')) + [L(blob([(30, 30), (48, 24), (50, 50), (32, 54)], 6), LEAC, 'f', False)]
C('eldritch-priest', 'normal', P('#89604a', '#f0a050', iris='#d8d040'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _eldritch('front'), _eldritch('side'), _eldritch('back'))

# Elvis (Cobblers) Schumacher: gorro de pescador a rayas azules y crema; nariz larguísima que cae en punta, ojos redondos con
# la pupila negra y piel morena anaranjada
BH, BHC = _c('#046ba8'), _c('#e7e3cf')
def _bucket(view):
    if view == 'front':
        out = [L(blob([(-2, 58), (6, 48), (50, 44), (94, 48), (102, 58), (90, 64), (50, 60), (10, 64)], 6), BH, 'f'),
               L(blob([(14, 50), (16, 20), (30, 2), (50, -4), (70, 2), (84, 20), (86, 50), (50, 46)], 6), BH, 'f')]
        for y0 in (6, 26):
            out.append(L(blob([(16, y0 + 2), (50, y0 - 4), (84, y0 + 2), (85, y0 + 10), (50, y0 + 5), (15, y0 + 10)], 4), BHC, 'f', False))
        return out
    if view == 'side':
        return [L(blob([(-6, 58), (4, 48), (50, 44), (96, 48), (104, 58), (90, 64), (50, 60), (6, 64)], 6), BH, 'f'),
                L(blob([(10, 50), (14, 18), (34, 0), (60, -4), (80, 6), (88, 30), (88, 50), (50, 46)], 6), BH, 'f'),
                L(blob([(12, 10), (50, 2), (86, 10), (87, 18), (50, 12), (12, 20)], 4), BHC, 'f', False), L(blob([(10, 30), (50, 24), (88, 30), (88, 38), (50, 32), (10, 40)], 4), BHC, 'f', False)]
    return _bucket('front')
C('elvis-cobblers-schumacher', 'normal', P('#5a3a20', '#dca259', iris='#141414'),
  F(eyes='round', brows=False, mouth='none', hairline=False, face_side=face_side(nose=4)),
  _bucket('front') + [L(outline([(46, 76), (54, 76), (54, 96), (50, 112, 1), (46, 96)]), 'skin_d', 'f')],
  _bucket('side') + [L(outline([(84, 76), (104, 96), (106, 106, 1), (88, 94)]), 'skin_d', 'f')],
  _bucket('back'))

# Erik Strongarm (portero): casco vikingo de metal oscuro con dos cuernos cortos crema; melena morada lisa hasta la barbilla
# que le tapa un ojo; ojo amarillo y la boca seria
VK, HORN = _c('#4c4237'), _c('#e8dcc0')
def _viking(view):
    if view == 'front':
        return [L(outline([(10, 26), (-4, 14), (-6, 4), (6, 4), (16, 16)]), HORN, 'f'), L(outline([(90, 26), (104, 14), (106, 4), (94, 4), (84, 16)]), HORN, 'f'),
                L(outline([(8, 50), (10, 24), (30, 4), (50, -10, 1), (70, 4), (90, 24), (92, 50), (70, 56), (50, 46, 1), (30, 56)]), VK, 'f'),
                L(blob([(58, -2), (80, 12), (90, 34), (90, 48), (74, 52), (70, 20)], 6), _c('#3d322f'), 'f', False)]
    if view == 'side':
        return [L(outline([(40, 20), (30, 4), (30, -6), (40, -4), (48, 10)]), HORN, 'f'),
                L(outline([(4, 56), (6, 26), (30, 2), (60, -10, 1), (80, 6), (92, 30), (92, 52), (60, 52), (30, 58)]), VK, 'f')]
    return [L(outline([(10, 26), (-4, 14), (-6, 4), (6, 4), (16, 16)]), HORN, 'f'), L(outline([(90, 26), (104, 14), (106, 4), (94, 4), (84, 16)]), HORN, 'f'),
            L(outline([(8, 56), (10, 24), (30, 4), (50, -10, 1), (70, 4), (90, 24), (92, 56), (50, 60)]), VK, 'f')]
C('erik-strongarm', 'normal', P('#614e69', '#f0e4bf', iris='#d8c030', shade='#4a3a52'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=93, hairline=[(6, 66), (18, 50), (40, 52), (60, 56), (80, 54), (94, 66)]),
  dome('front', top=10, w=45, cy=48, long=96, flare=2, ends=3) + _viking('front') +
  [L(outline([(16, 50), (40, 46), (56, 56), (54, 80), (44, 96, 1), (36, 80), (22, 74)]), 'mid', 'f')],
  dome('side', top=10, w=45, cy=48, long=96, flare=2, fr=60) + _viking('side'),
  dome('back', top=10, w=45, cy=48, long=96, flare=2, ends=4) + _viking('back'))

# Ernest (Warrior) Goodman: pelo azul marino oscuro en pinchos anchos, con dos que se levantan como orejas de gato; una diadema
# dorada con una gema azul en la frente, ojos verde agua, sonrisa y una bufanda azul enrollada al cuello
GEM = _c('#3a8ad0')
C('ernest-warrior-goodman', 'normal', P('#293f4f', '#f8c082', iris='#3a9a9a', shade='#202a32'),
  F(eyes='big', brows='angry', mouth='smile', mouth_y=91, hairline=hl(5, 66, 46, 58, jit=2, seed=53)),
  dome('front', top=-4, w=50, cy=44, n=7, amp=14, seed=53, sb=70) +
  [L(outline([(14, 30), (2, -14, 1), (28, 10)]), 'mid', 'b'), L(outline([(86, 30), (98, -14, 1), (72, 10)]), 'mid', 'b'),
   L(blob([(34, 44), (50, 36), (66, 44), (64, 50), (50, 44), (36, 50)], 4), GOLD, 'f'), L(outline([(42, 40), (50, 16, 1), (58, 40)]), GOLD, 'f'),
   L(ell(50, 34, 5, 5), GEM, 'f')] + scarf('front', _c('#2a5a7a'), 104, 12),
  dome('side', top=-4, w=50, cy=44, n=7, amp=14, seed=53, nape=86, fr=52) + [L(blob([(70, 40), (88, 36), (90, 46), (72, 48)], 4), GOLD, 'f')] +
  scarf('side', _c('#2a5a7a'), 104, 12),
  dome('back', top=-4, w=50, cy=44, n=7, amp=14, seed=53, nape=86) + scarf('back', _c('#2a5a7a'), 104, 12))

# Eva Chatton: una mata enorme de pelo amarillo pálido en forma de seta que le cae por toda la cabeza y la frente; ojeras
# negras alrededor de los ojos redondos y una boquita
C('eva-chatton', 'chica', P('#fef0bd', '#dbad89', iris='#141414', shade='#e8d098'),
  F(eyes='round', brows=False, mouth='none', hairline=False),
  [L(blob([(-14, 96), (-12, 50), (0, 14), (30, -8), (60, -10), (88, 2), (108, 36), (114, 80), (104, 104), (84, 90), (80, 64), (60, 60), (44, 70), (26, 66), (18, 90), (0, 108)], 8)),
   L(blob([(70, 6), (100, 30), (110, 74), (100, 100), (86, 80), (84, 50)], 6), 'shade', 'f', False),
   L(ell(36, 76, 9, 8), _c('#3a342e'), 'f', False), L(ell(64, 76, 9, 8), _c('#3a342e'), 'f', False),
   L(ell(36, 76, 5.4, 5), WHITE, 'f', False), L(ell(64, 76, 5.4, 5), WHITE, 'f', False), L(ell(36, 76, 2.6, 2.6), BLACK, 'f', False), L(ell(64, 76, 2.6, 2.6), BLACK, 'f', False),
   L(ell(50, 92, 1.6, 1.8), _c('#6a3a2a'), 'f', False)],
  [L(blob([(-14, 100), (-10, 40), (10, 6), (50, -10), (86, 0), (100, 30), (98, 58), (78, 56), (64, 66), (44, 90), (20, 110)], 8)),
   L(ell(82, 76, 6, 7), _c('#3a342e'), 'f', False), L(ell(83, 76, 3, 3.4), WHITE, 'f', False)],
  [L(blob([(-14, 100), (-12, 50), (0, 14), (30, -8), (60, -10), (88, 2), (108, 36), (114, 80), (104, 106), (50, 116)], 8)),
   L(blob([(64, 4), (100, 30), (110, 74), (100, 104), (74, 110), (70, 50)], 6), 'shade', 'f', False)])

# Eveline (Vicked) Veitch: sombrero de bruja negro de ala ancha con una cinta naranja; melena morada larga y ondulada que cae
# por un lado; ojo entornado y media sonrisa
WH, WHO = _c('#2e2826'), _c('#c85f07')
def _witch(view):
    if view == 'front':
        return [L(blob([(-14, 48), (0, 38), (50, 34), (100, 38), (114, 48), (100, 56), (50, 52), (0, 56)], 6), WH, 'f'),
                L(outline([(20, 44), (30, 14), (46, -20), (64, -38, 1), (62, -18), (74, 14), (80, 44), (50, 40)]), WH, 'f'),
                L(blob([(24, 30), (50, 26), (76, 30), (78, 40), (50, 36), (22, 40)], 4), WHO, 'f', False)]
    if view == 'side':
        return [L(blob([(-20, 48), (0, 38), (50, 34), (104, 38), (118, 48), (100, 56), (50, 52), (-4, 56)], 6), WH, 'f'),
                L(outline([(14, 44), (24, 14), (36, -16), (20, -36, 1), (50, -12), (70, 14), (80, 44), (50, 40)]), WH, 'f'),
                L(blob([(18, 30), (50, 26), (76, 30), (78, 40), (50, 36), (16, 40)], 4), WHO, 'f', False)]
    return _witch('front')
C('eveline-vicked-veitch', 'chica', P('#822396', '#f1d6bc', iris='#3a2a40', shade='#612258'),
  F(eyes='closed', brows=False, mouth='smile', mouth_y=92, hairline=[(6, 70), (18, 54), (40, 56), (60, 58), (80, 56), (94, 70)]),
  dome('front', top=10, w=46, cy=48, n=8, amp=6, soft=True, seed=55, long=112, flare=12, ends=4) + _witch('front') + lashes(),
  dome('side', top=10, w=46, cy=48, n=8, amp=6, soft=True, seed=55, long=112, flare=12, fr=58) + _witch('side'),
  dome('back', top=10, w=46, cy=48, n=8, amp=6, soft=True, seed=55, long=112, flare=12, ends=5) + _witch('back'))

# Ewan (People) Envoi: cabeza rapada morena con una cresta corta roja de punta arriba; una estrella amarilla grande y otra
# naranja pequeña pintadas en la frente; ojos azules afilados, orejas grandes y una sonrisa apretada de dientes
C('ewan-people-envoi', 'normal', P('#a20806', '#ae8c73', iris='#3a6aa0'),
  F(eyes='sharp', brows='angry', mouth='none', big_ears=3, ear_out=3, hairline=False),
  skull3('front') + [L(outline([(46, 12), (46, -16), (54, -16), (54, 12)])), _star(30, 38, 12, _c('#f1bd33')), _star(60, 42, 6, _c('#e07020'))] + big_grin(94, 12, 7),
  skull3('side') + [L(outline([(40, 6), (36, -18), (48, -20), (50, 4)]))],
  skull3('back') + [L(outline([(46, 12), (46, -16), (54, -16), (54, 30), (46, 30)]))])

# Ezio (Chopper) Ryder: cresta gris azulada de pinchos que sigue hasta la nuca y asoma por los lados; gafas de sol redondas
# negras, cara muy alargada y pálida, y la boca en un mohín
C('ezio-chopper-ryder', 'delgado', P('#8894a3', '#fdefd3', iris='#141414', shade='#6b6c70'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=104, face_front=face(w=-2, chin=118), face_side=face_side(chin=16, nose=3), hairline=False),
  skull3('front') + [L(outline([(36, 30), (30, -10, 1), (42, 6), (48, -26, 1), (54, 6), (66, -14, 1), (64, 30)])),
                     L(outline([(14, 50), (-6, 40, 1), (8, 60), (-8, 72, 1), (12, 76)])), L(outline([(86, 50), (106, 40, 1), (92, 60), (108, 72, 1), (88, 76)]))] +
  [L(ell(36, 74, 10, 9), BLACK, 'f'), L(ell(64, 74, 10, 9), BLACK, 'f'), L([(46, 72), (54, 72)], BLACK, 'f', False, False, 2.0),
   L([(30, 70), (34, 72)], WHITE, 'f', False, False, 1.4), L([(58, 70), (62, 72)], WHITE, 'f', False, False, 1.4)],
  skull3('side') + [L(outline([(80, 10), (82, -14, 1), (66, 0), (56, -26, 1), (44, -2), (24, -16, 1), (20, 8), (-6, 10, 1), (8, 30), (-10, 50, 1), (8, 56), (-4, 80, 1), (22, 66),
                               (40, 40)])),
                    L(ell(84, 74, 6, 8), BLACK, 'f'), L([(78, 72), (50, 66)], BLACK, 'f', False, False, 2.0)],
  skull3('back') + [L(outline([(40, 2), (36, -24, 1), (50, -8), (64, -24, 1), (60, 2), (66, 40), (60, 90), (40, 90), (34, 40)])),
                    L(outline([(14, 50), (-6, 40, 1), (8, 60), (-8, 72, 1), (12, 76)])), L(outline([(86, 50), (106, 40, 1), (92, 60), (108, 72, 1), (88, 76)]))])

# Fabrice Pesci: piel morena, pelo rojo rapado corto como un casquete, ojos afilados y una media sonrisa de labios gruesos
C('fabrice-pesci', 'normal', P('#a3190d', '#b7723a', iris='#141414'),
  F(eyes='sharp', brows='angry', mouth='lips', mouth_y=94, mouth_w=10, big_ears=2, ear_out=2, face_front=face(chin=104, jaw=2), nose=(50, 86, 3.6),
    hairline=[(10, 58), (20, 42), (36, 36), (50, 36), (64, 36), (80, 42), (90, 58)]),
  crop('front', top=4, side=56), crop('side', top=4, nape=76), crop('back', top=4, nape=76))

# Fabrice Soffner: mata enorme de pelo rizado verde oliva que oscurece a castaño por abajo; gafas de sol negras en forma de
# antifaz, cara alargada y la boca torcida
C('fabrice-soffner', 'delgado', P('#7e774b', '#fcc271', iris='#141414', low='#52402e'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=98, face_front=face(chin=110), face_side=face_side(chin=10), hairline=[(6, 70), (18, 40), (40, 34), (50, 40), (60, 34), (82, 40), (94, 70)]),
  [L(blob([(-6, 100), (-10, 70), (110, 70), (106, 100), (84, 104), (16, 104)], 8), 'low')] +
  dome('front', top=-4, w=54, cy=44, n=12, amp=7, soft=True, seed=57, sb=80) +
  [L(blob([(14, 70), (32, 64), (48, 70), (52, 70), (68, 64), (86, 70), (76, 82), (56, 78), (44, 78), (24, 82)], 6), BLACK, 'f')],
  [L(blob([(-6, 70), (40, 64), (50, 100), (20, 106), (-4, 96)], 8), 'low')] + dome('side', top=-4, w=54, cy=44, n=12, amp=7, soft=True, seed=57, nape=96, fr=50) +
  [L(blob([(70, 68), (92, 68), (88, 80), (72, 80)], 6), BLACK, 'f')],
  [L(blob([(-6, 100), (-10, 66), (110, 66), (106, 100), (50, 110)], 8), 'low')] + dome('back', top=-4, w=54, cy=44, n=12, amp=7, soft=True, seed=57, nape=80))

# Fada Prendi: melena rubia ondulada hasta los hombros con flequillo recto, y dos lazos con los colores de Italia (verde,
# blanco y rojo) arriba; ojos azules grandes y sonrisa
def _ribbon(x, view='front'):
    """Lazo con los colores de Italia: dos lazadas (verde y roja) y el nudo blanco, con las puntas colgando."""
    return [L(outline([(x, 10), (x - 12, 0), (x - 12, 16)]), _c('#2a8a3a'), 'f'), L(outline([(x, 10), (x + 12, 0), (x + 12, 16)]), _c('#c82a2a'), 'f'),
            L(outline([(x - 2, 12), (x - 6, 28, 1), (x, 18), (x + 6, 28, 1), (x + 2, 12)]), WHITE, 'f'), L(ell(x, 10, 3.4, 3.4), WHITE, 'f')]
C('fada-prendi', 'chica', P('#eacb8d', '#facea3', iris='#3a7ab8', shade='#c6a681'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=91, hairline=[(6, 64), (16, 52), (30, 58), (50, 58), (70, 58), (84, 52), (94, 64)]),
  dome('front', top=2, w=46, cy=46, n=8, amp=6, soft=True, seed=59, long=106, flare=12, ends=4) + _ribbon(20) + _ribbon(76) + lashes(),
  dome('side', top=2, w=46, cy=46, n=8, amp=6, soft=True, seed=59, long=106, flare=12, fr=58) + _ribbon(40) + lash_side(),
  dome('back', top=2, w=46, cy=46, n=8, amp=6, soft=True, seed=59, long=106, flare=12, ends=5) + _ribbon(20) + _ribbon(76))

# Fala Polaris: capucha de tela beige con un ala que le cae sobre los ojos y una cinta gris; la parte de arriba de la cara queda
# en sombra negra y abajo asoma una sonrisa de dientes; bufanda del mismo color
BEI = _c('#cfbaa0')
def _fala(view):
    if view == 'front':
        return hood('front', BEI, top=-6, low=104, face_hole=[(22, 100), (18, 78), (24, 60), (50, 54), (76, 60), (82, 78), (78, 100), (50, 108)], rim=_c('#a89478')) + \
            [L(blob([(4, 56), (14, 44), (50, 40), (86, 44), (96, 56), (80, 66), (50, 62), (20, 66)], 6), BEI, 'f'),
             L(blob([(10, 44), (50, 36), (90, 44), (90, 50), (50, 44), (10, 50)], 4), _c('#6d6f6c'), 'f', False),
             L(blob([(20, 64), (50, 60), (80, 64), (80, 82), (50, 80), (20, 82)], 6), BLACK, 'f', False)] + scarf('front', BEI, 100, 14)
    if view == 'side':
        return hood('side', BEI, top=-6, rim=_c('#a89478')) + [L(blob([(30, 46), (90, 42), (100, 54), (80, 62), (40, 58)], 6), BEI, 'f'),
                                                               L(blob([(68, 62), (90, 62), (90, 82), (70, 80)], 6), BLACK, 'f', False)] + scarf('side', BEI, 100, 14)
    return hood('back', BEI, top=-6, rim=_c('#a89478')) + [L(blob([(6, 44), (50, 36), (94, 44), (94, 50), (50, 44), (6, 50)], 4), _c('#6d6f6c'), 'f', False)] + \
        scarf('back', BEI, 100, 14)
C('fala-polaris', 'normal', P('#cfbaa0', '#ce9668', iris='#141414'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _fala('front') + teeth_grin(92, 12, 5), _fala('side'), _fala('back'))

# Falah Hazbin: mata de pelo verde oliva oscuro en pinchos gruesos y cortos, piel morena, cara alargada, ojos blancos de
# enfado con cejas en pico y los dientes apretados
C('falah-hazbin', 'normal', P('#4c4a02', '#d0a580', iris='#141414', shade='#3d310c'),
  F(eyes='none', brows=False, mouth='none', face_front=face(chin=106), face_side=face_side(chin=6), hairline=[(10, 64), (20, 44), (36, 38), (50, 40), (64, 38), (80, 44), (90, 64)]),
  dome('front', top=-8, w=52, cy=42, n=11, amp=9, seed=61, sb=70) +
  [L(blob([(26, 72), (40, 68), (44, 76), (30, 78)], 4), WHITE, 'f'), L(blob([(74, 72), (60, 68), (56, 76), (70, 78)], 4), WHITE, 'f'),
   L([(24, 66), (42, 70)], BLACK, 'f', False, False, 2.4), L([(76, 66), (58, 70)], BLACK, 'f', False, False, 2.4)] + teeth_grin(94, 10, 4),
  dome('side', top=-8, w=52, cy=42, n=11, amp=9, seed=61, nape=86, fr=48) + [L(blob([(76, 72), (88, 70), (88, 78), (78, 78)], 4), WHITE, 'f')],
  dome('back', top=-8, w=52, cy=42, n=11, amp=9, seed=61, nape=86))

# Fanella Waftgood: media melena negra morada con un flequillo recto espeso que le tapa los ojos, y dos moños redondos a los
# lados rodeados de cuentas amarillas; pecas, pendientes dorados y una sonrisa de dientes
def _fanella(view):
    beads = lambda cx, cy: [L(ell(cx + 13 * __import__('math').cos(a / 3), cy + 13 * __import__('math').sin(a / 3), 3, 3), GOLD, 'f') for a in range(-6, 7, 2)]
    if view == 'front':
        return [L(ell(8, 22, 16, 16)), L(ell(92, 22, 16, 16))] + beads(12, 26)[:4] + beads(88, 26)[3:]
    if view == 'side':
        return [L(ell(30, 14, 16, 16))]
    return [L(ell(8, 22, 16, 16)), L(ell(92, 22, 16, 16))]
C('fanella-waftgood', 'chica', P('#302833', '#f0d6b5', iris='#141414', shade='#201a1a'),
  F(eyes='none', brows=False, mouth='none', hairline=[(6, 80), (20, 77), (50, 79), (80, 77), (94, 80)]),
  _fanella('front') + bowl3('front', top=2, side=92, w=2, fringe=80) + big_grin(94, 12, 6) +
  [L(ell(x, 86, 0.9, 0.9), _c('#b07050'), 'f', False) for x in (24, 28, 32, 68, 72, 76)] + [L(ell(14, 84, 2, 2), GOLD, 'f'), L(ell(86, 84, 2, 2), GOLD, 'f')],
  _fanella('side') + bowl3('side', top=2, nape=94, w=2, fringe=70),
  _fanella('back') + bowl3('back', top=2, nape=94, w=2))

# Fanny (Deadeye) Oakley: sombrero vaquero crema con una cinta granate y una piedra verde; melena naranja rizada y abultada a
# los lados; ojos castaños, sonrisa y un pañuelo verde al cuello
HAT, HATB = _c('#e9d9bb'), _c('#8a2a1e')
def _cowboy(view):
    if view == 'front':
        return [L(blob([(-12, 40), (-6, 30), (14, 34), (50, 30), (86, 34), (106, 30), (112, 40), (90, 48), (50, 44), (10, 48)], 6), HAT, 'f'),
                L(blob([(18, 38), (20, 12), (36, -2), (50, 4), (64, -2), (80, 12), (82, 38), (50, 34)], 6), HAT, 'f'),
                L(blob([(18, 30), (50, 26), (82, 30), (82, 36), (50, 32), (18, 36)], 4), HATB, 'f', False), L(ell(50, 32, 5, 5), _c('#3a9a3a'), 'f')]
    if view == 'side':
        return [L(blob([(-16, 40), (-8, 30), (50, 30), (104, 30), (112, 40), (90, 48), (10, 48)], 6), HAT, 'f'),
                L(blob([(14, 38), (18, 10), (50, -2), (80, 10), (84, 38), (50, 34)], 6), HAT, 'f'), L(blob([(14, 30), (84, 30), (84, 36), (14, 36)], 4), HATB, 'f', False)]
    return _cowboy('front')[:3]
C('fanny-deadeye-oakley', 'chica', P('#d06006', '#fdebbc', iris='#7a3a1e', shade='#9e4210'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=91, hairline=[(6, 66), (18, 50), (36, 46), (50, 50), (64, 46), (82, 50), (94, 66)]),
  [L(blob([(-10, 70), (0, 50), (14, 52), (20, 90), (8, 104), (-8, 96)], 8)), L(blob([(110, 70), (100, 50), (86, 52), (80, 90), (92, 104), (108, 96)], 8))] +
  dome('front', top=10, w=44, cy=48, sb=70) + _cowboy('front') + scarf('front', _c('#3a6a2a'), 104, 10) + lashes(),
  [L(blob([(-10, 60), (10, 46), (40, 56), (44, 96), (20, 106), (-6, 96)], 8))] + dome('side', top=10, w=44, cy=48, nape=90, fr=52) + _cowboy('side') +
  scarf('side', _c('#3a6a2a'), 104, 10),
  [L(blob([(-10, 70), (0, 46), (100, 46), (110, 70), (104, 100), (50, 108), (-4, 100)], 8))] + _cowboy('back'))

# Fez Monkton: un fez rojo con la borla oscura; cara de mono ancha morena anaranjada, con la boca saliente, los ojos
# entornados y orejas grandes
FEZ = _c('#a32f30')
def _fez(view):
    if view == 'side':
        return skull3('side') + [L(blob([(20, 42), (24, 6), (76, 2), (82, 40), (50, 46)], 4), FEZ, 'f'), L(outline([(26, 8), (16, 12), (10, 40), (16, 42), (24, 18)]), _c('#3a3a5a'), 'f')]
    return skull3('front') + [L(blob([(20, 44), (22, 8), (78, 8), (80, 44), (50, 48)], 4), FEZ, 'f'), L(outline([(26, 10), (18, 14), (14, 44), (20, 46), (28, 20)]), _c('#3a3a5a'), 'f')]
C('fez-monkton', 'corpulento', P('#342f2e', '#dca257', iris='#141414'),
  F(eyes='closed', brows=False, mouth='line', mouth_y=100, face_front=face(w=8, chin=110, jaw=6), face_side=face_side(chin=8, jaw=6, nose=6), big_ears=3, ear_out=6,
    hairline=False),
  _fez('front') + [L(blob([(20, 60), (50, 56), (80, 60), (82, 66), (50, 62), (18, 66)], 4), 'skin_d', 'f', False),
                   L(blob([(30, 84), (50, 80), (70, 84), (72, 102), (50, 108), (28, 102)], 6), _c('#c08a48'), 'f', False)],
  _fez('side') + [L(blob([(76, 82), (94, 80), (96, 100), (78, 104)], 6), _c('#c08a48'), 'f', False)],
  skull3('back') + _fez('front')[2:])

# Flick Screening: media melena castaño rojizo con la raya en medio y las puntas metidas, dos coletas bajas atadas con lazos
# rosas; ojos negros enormes y una sonrisa
PB = _c('#f0a0a0')
C('flick-screening', 'chica', P('#872804', '#f6dcc4', iris='#141414', shade='#6a2309'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=91, hairline=[(6, 64), (18, 46), (36, 40), (50, 44), (64, 40), (82, 46), (94, 64)]),
  dome('front', top=4, w=46, cy=46, long=94, flare=0, ends=3) + [L(ell(12, 96, 8, 7), PB, 'f'), L(ell(88, 96, 8, 7), PB, 'f'),
                                                                 L(outline([(6, 90), (-2, 84, 1), (4, 98)]), PB, 'f'), L(outline([(94, 90), (102, 84, 1), (96, 98)]), PB, 'f')] + lashes(),
  dome('side', top=4, w=46, cy=46, long=94, flare=0, fr=50) + [L(ell(30, 96, 8, 7), PB, 'f')] + lash_side(),
  dome('back', top=4, w=46, cy=46, long=94, flare=0, ends=3) + [L(ell(14, 96, 8, 7), PB, 'f'), L(ell(86, 96, 8, 7), PB, 'f')])

# Florence Tripps: pelo naranja claro rizado en bucles a los lados con una boina granate encima; gafas redondas enormes verdes
# y ojos tristes
C('florence-tripps', 'normal', P('#de9f60', '#fbecc1', iris='#7a4a20', shade='#aa6a41'),
  F(eyes='normal', brows=True, mouth='frown', mouth_y=93, hairline=[(6, 64), (18, 46), (36, 42), (50, 46), (64, 42), (82, 46), (94, 64)]),
  dome('front', top=6, w=50, cy=48, n=8, amp=6, soft=True, seed=63, long=96, flare=8, ends=3) +
  [L(blob([(14, 30), (30, 8), (54, 2), (78, 8), (90, 24), (80, 30), (50, 24)], 6), _c('#7e0526'), 'f'), L(outline([(48, 4), (52, -6, 1), (56, 4)]), _c('#7e0526'), 'f')] +
  round_specs('front', _c('#5aa030'), 76, 15, 11, 9, 2.6),
  dome('side', top=6, w=50, cy=48, n=8, amp=6, soft=True, seed=63, long=96, flare=8, fr=52) +
  [L(blob([(10, 26), (30, 4), (60, 0), (86, 14), (80, 24), (50, 18)], 6), _c('#7e0526'), 'f')] + round_specs('side', _c('#5aa030'), 76, 15, 11, 9, 2.6),
  dome('back', top=6, w=50, cy=48, n=8, amp=6, soft=True, seed=63, long=96, flare=8, ends=4) +
  [L(blob([(14, 30), (30, 8), (54, 2), (78, 8), (90, 24), (80, 30), (50, 24)], 6), _c('#7e0526'), 'f')])

# Fox Wiley: pelo magenta despeinado echado hacia atrás con mechones que le caen por la frente y hasta el cuello; ojos rojos
# afilados y una sonrisa enorme y abierta de dientes
C('fox-wiley', 'delgado', P('#9e2054', '#fdf3e1', iris='#a02a1e', shade='#842039'),
  F(eyes='sharp', brows='angry', mouth='none', face_front=face(chin=106), face_side=face_side(chin=6), hairline=[(6, 66), (18, 46), (34, 38), (50, 42), (66, 38), (82, 46), (94, 66)]),
  dome('front', top=-2, w=46, cy=44, n=6, amp=12, sweep=0.5, seed=65, long=100, flare=8, ends=3) +
  [L(outline([(34, 30), (44, 26), (48, 50), (42, 70, 1), (38, 50)]), 'mid', 'f'),
   L(blob([(32, 88), (50, 90), (68, 88), (62, 100), (50, 104), (38, 100)], 6), _c('#c83a2a'), 'f'), L(blob([(36, 89), (64, 89), (62, 93), (38, 93)], 4), WHITE, 'f', False)],
  dome('side', top=-2, w=46, cy=44, n=6, amp=12, sweep=0.5, seed=65, long=100, flare=8, fr=52),
  dome('back', top=-2, w=46, cy=44, n=6, amp=12, sweep=0.5, seed=65, long=100, flare=8, ends=4))

# Gail Ellement: pelo verde musgo alborotado y corto, con un rizo en espiral en la frente y mechones que tapan las orejas; ojos
# grandes violeta y boca pequeña
C('gail-ellement', 'bajito', P('#647a43', '#ece2c7', iris='#5a4a8a', shade='#464a2c'),
  F(eyes='big', brows=False, mouth='line', mouth_y=92, hairline=hl(6, 70, 48, 60, jit=3, seed=67)),
  dome('front', top=0, w=50, cy=44, n=9, amp=8, seed=67, long=90, flare=6, ends=3) +
  [L(ell(50, 50, 8, 8), 'mid', 'f'), strand([(50, 50), (54, 48), (52, 44), (46, 46), (46, 54), (54, 56), (58, 50)], 'deep', 'f', 1.2)],
  dome('side', top=0, w=50, cy=44, n=9, amp=8, seed=67, long=90, flare=6, fr=54),
  dome('back', top=0, w=50, cy=44, n=9, amp=8, seed=67, long=90, flare=6, ends=4))

# Galahad Chevalier: yelmo de caballero gris con la visera de rejilla y un penacho rojo; la cara redonda y mofletuda asoma por
# debajo, con la boca pequeña; gorjal de metal al cuello
MET, METD = _c('#a7a49a'), _c('#6e6a64')
def _helm(view):
    if view == 'front':
        return [L(blob([(10, 66), (10, 30), (26, 8), (50, 0), (74, 8), (90, 30), (90, 66), (70, 60), (50, 58), (30, 60)], 6), MET, 'f'),
                L(blob([(60, 4), (80, 14), (90, 36), (88, 62), (76, 52)], 6), METD, 'f', False),
                L(blob([(26, 40), (50, 34), (74, 40), (72, 56), (50, 52), (28, 56)], 6), _c('#3a3634'), 'f', False)] + \
            [L([(30 + 8 * k, 38), (30 + 8 * k, 54)], MET, 'f', False, False, 2.2) for k in range(6)] + \
            [L(blob([(44, 0), (48, -14), (58, -16), (62, -8), (56, 2)], 6), _c('#c8202a'), 'f')]
    if view == 'side':
        return [L(blob([(4, 70), (6, 30), (30, 4), (60, 0), (86, 16), (92, 56), (60, 60), (30, 70)], 6), MET, 'f'),
                L(blob([(70, 36), (92, 36), (92, 54), (72, 54)], 4), _c('#3a3634'), 'f', False), L(blob([(40, 0), (40, -16), (54, -16), (56, -4)], 6), _c('#c8202a'), 'f')]
    return [L(blob([(10, 80), (10, 30), (26, 8), (50, 0), (74, 8), (90, 30), (90, 80), (50, 86)], 6), MET, 'f'),
            L(blob([(60, 4), (80, 14), (90, 36), (88, 78), (70, 60)], 6), METD, 'f', False), L(blob([(44, 0), (48, -14), (58, -16), (62, -8), (56, 2)], 6), _c('#c8202a'), 'f')]
def _gorget(view):
    if view == 'side':
        return [L(blob([(20, 100), (60, 96), (96, 102), (98, 112), (60, 112), (16, 110)], 6), MET, 'f')]
    return [L(blob([(-4, 104), (20, 98), (50, 102), (80, 98), (104, 104), (100, 116), (50, 118), (0, 116)], 6), MET, 'f')] + \
        [L(ell(x, 110, 1.4, 1.4), METD, 'f', False) for x in (10, 30, 70, 90)]
C('galahad-chevalier', 'corpulento', P('#85685b', '#ce9466', iris='#141414'),
  F(eyes='none', brows=False, mouth='line', mouth_y=88, face_front=face(w=10, chin=104, jaw=8), face_side=face_side(chin=4, jaw=8), ear_out=8, hairline=False),
  _helm('front') + _gorget('front'), _helm('side') + _gorget('side'), _helm('back') + _gorget('back'))

# Gary Baldi: calvo moreno con un tatuaje negro de aro y llamas en un lado de la cabeza; ojos rojos afilados de enfado, un
# aro de plata en la oreja y la boca seria
C('gary-baldi', 'normal', P('#ce9568', '#ce9568', iris='#c02a1e'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, face_front=face(chin=104), hairline=False, nose=(50, 86, 2.6)),
  skull3('front') + [L(blob([(54, 8), (72, 12), (84, 30), (78, 40), (70, 26), (60, 20)], 6), BLACK, 'f', False),
                     L(ell(66, 30, 9, 6) + [ell(66, 30, 9, 6)[0]], _c('#8a6a4a'), 'f', False, False, 1.6),
                     L(ell(14, 80, 2.4, 3), _c('#c0c8d0'), 'f')],
  skull3('side') + [L(blob([(40, 6), (60, 4), (74, 14), (66, 22), (48, 16)], 6), BLACK, 'f', False)],
  skull3('back') + [L(blob([(30, 10), (50, 6), (58, 20), (40, 30)], 6), BLACK, 'f', False)])

# Gene Bulge: pelo azul verdoso muy claro, esponjoso y alborotado, con mechones que le caen por la frente; ojos negros
# redondos grandes y una sonrisa
C('gene-bulge', 'normal', P('#b3d2cb', '#f8bc7f', iris='#141414', shade='#8d928f'),
  F(eyes='round', brows=False, mouth='smile', mouth_y=92, hairline=hl(5, 68, 50, 64, lean=2, jit=3, seed=69)),
  dome('front', top=-4, w=50, cy=44, n=9, amp=10, soft=True, sweep=0.3, seed=69, sb=76) + [strand([(30, 30), (40, 44)], 'shade', 'f', 1.0), strand([(60, 26), (66, 42)], 'shade', 'f', 1.0)],
  dome('side', top=-4, w=50, cy=44, n=9, amp=10, soft=True, sweep=0.3, seed=69, nape=88, fr=56),
  dome('back', top=-4, w=50, cy=44, n=9, amp=10, soft=True, sweep=0.3, seed=69, nape=88))

# Genghis Cohen: piel morena oscura, pelo verde oliva oscuro corto y plano arriba con los lados rapados grises; cejas gruesas
# fruncidas, ojos verdes y unos labios gruesos con la boca abierta
C('genghis-cohen', 'normal', P('#423e25', '#b77238', iris='#3a9a3a', side='#8a8a8a'),
  F(eyes='normal', brows=False, mouth='none', big_ears=2, ear_out=2, face_front=face(w=2, chin=106, jaw=3), nose=(50, 86, 4),
    hairline=[(10, 58), (18, 42), (34, 34), (50, 34), (66, 34), (82, 42), (90, 58)]),
  crop('front', top=4, side=56, c='side', shade=False) + [L(blob([(22, 30), (24, 10), (50, 4), (76, 10), (78, 30), (50, 26)], 6), 'mid', 'f')] +
  brows(64, _c('#2a2a1a'), 4.4, 15, 1.6, 14) + [L(ell(50, 98, 7, 6), _c('#6a3a1e'), 'f'), L(ell(50, 98, 3.4, 3), _c('#3a1e14'), 'f', False)],
  crop('side', top=4, nape=76, c='side', shade=False) + [L(blob([(16, 20), (40, 4), (80, 6), (88, 22), (50, 22)], 6), 'mid', 'f')] + side_brow(64, _c('#2a2a1a'), 4.2, 1.6),
  crop('back', top=4, nape=76, c='side', shade=False) + [L(blob([(22, 30), (24, 10), (50, 4), (76, 10), (78, 30), (50, 26)], 6), 'mid', 'f')])

# Gerald Gerund (portero): melena gris azulado oscuro en casco que le tapa las orejas, con un mechón en punta que sale hacia
# un lado; ojos azul claro entornados y la boca pequeña
C('gerald-gerund', 'normal', P('#4a5a62', '#fac274', iris='#5aa0b0', shade='#373231'),
  F(eyes='normal', brows='angry', mouth='frown', mouth_y=93, ears=False, hairline=[(6, 66), (18, 48), (36, 44), (52, 50), (72, 46), (94, 66)]),
  bowl3('front', top=2, side=94, w=4, fringe=58) + [L(outline([(86, 72), (104, 64, 1), (94, 84)]), 'mid', 'f'),
                                                   L(outline([(30, 30), (54, 34), (60, 52), (54, 64, 1), (46, 48)]), 'mid', 'f')],
  bowl3('side', top=2, nape=96, w=4) + [L(outline([(10, 70), (-6, 80, 1), (8, 86)]), 'mid', 'f')],
  bowl3('back', top=2, nape=96, w=4) + [L(outline([(90, 72), (108, 66, 1), (96, 86)]), 'mid', 'f')])

# Ghoulian Haunter: disfrazado de fantasma con una sábana azul muy pálida remendada que le tapa toda la cabeza, dos ojos negros
# alargados y una sonrisa; un sombrerito de copa negro con cinta naranja y una calavera
GH, GHD = _c('#e0f1f8'), _c('#b8c8d0')
def _ghost(view):
    if view == 'front':
        out = [L(blob([(2, 110), (4, 60), (14, 22), (50, 4), (86, 22), (96, 60), (98, 110), (50, 116)], 8), GH, 'f'),
               L(blob([(64, 10), (88, 26), (96, 70), (94, 108), (80, 100), (80, 50)], 6), GHD, 'f', False),
               L(blob([(30, 62), (38, 62), (38, 78), (30, 78)], 4), BLACK, 'f', False), L(blob([(62, 62), (70, 62), (70, 78), (62, 78)], 4), BLACK, 'f', False),
               L(quad((34, 88), (50, 102), (66, 88)) + [(66, 88)], BLACK, 'f', False)]
        hat = [L(blob([(-6, 12), (2, 6), (30, 8), (36, 14), (28, 18), (-2, 18)], 4), BLACK, 'f'), L(blob([(4, 10), (6, -10), (28, -12), (30, 10)], 4), BLACK, 'f'),
               L(blob([(4, 2), (30, 0), (30, 6), (4, 8)], 4), _c('#e07020'), 'f', False), L(ell(8, 6, 4, 4), _c('#f0e8d8'), 'f')]
        return out + hat + [L([(50, 26), (76, 40)], _c('#8a7a3a'), 'f', False, False, 1.2)]
    if view == 'side':
        return [L(blob([(0, 110), (2, 60), (14, 20), (50, 4), (84, 20), (98, 60), (100, 110), (50, 116)], 8), GH, 'f'),
                L(blob([(84, 62), (90, 62), (90, 78), (84, 78)], 4), BLACK, 'f', False),
                L(blob([(6, 12), (14, 6), (44, 8), (50, 14), (40, 18), (10, 18)], 4), BLACK, 'f'), L(blob([(16, 10), (18, -10), (40, -12), (42, 10)], 4), BLACK, 'f')]
    return [L(blob([(2, 110), (4, 60), (14, 22), (50, 4), (86, 22), (96, 60), (98, 110), (50, 116)], 8), GH, 'f'),
            L(blob([(60, 10), (88, 26), (96, 70), (94, 108), (70, 110), (70, 50)], 6), GHD, 'f', False),
            L(blob([(64, 12), (72, 6), (100, 8), (106, 14), (96, 18), (68, 18)], 4), BLACK, 'f'), L(blob([(74, 10), (76, -10), (98, -12), (100, 10)], 4), BLACK, 'f')]
C('ghoulian-haunter', 'normal', P('#e0f1f8', '#e0f1f8', iris='#141414'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _ghost('front'), _ghost('side'), _ghost('back'))

# Gladius Swinger: melena azul petróleo hasta los hombros echada atrás, con una cinta fina en la frente; piel morena, ojos
# afilados de enfado y la boca seria
C('gladius-swinger', 'normal', P('#37596a', '#cc966a', iris='#141414', shade='#2e3a41'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, face_front=face(chin=104, jaw=2), hairline=[(8, 62), (18, 46), (34, 42), (50, 42), (66, 42), (82, 46), (92, 62)]),
  dome('front', top=0, w=46, cy=44, n=5, amp=6, soft=True, seed=71, long=100, flare=10, ends=4) + [band('front', 42, 2.4, BLACK)],
  dome('side', top=0, w=46, cy=44, n=5, amp=6, soft=True, seed=71, long=100, flare=10, fr=46) + [band('side', 42, 2.4, BLACK)],
  dome('back', top=0, w=46, cy=44, n=5, amp=6, soft=True, seed=71, long=100, flare=10, ends=5) + [band('back', 42, 2.4, BLACK)])

# Goodie Touchouse: pelo castaño oscuro rizado y abultado, piel morena; gafas de broma azules con una nariz postiza naranja y
# cejas gruesas, y una sonrisa
NOSE = _c('#c0703a')
C('goodie-touchouse', 'normal', P('#413119', '#b2957c', iris='#5a4a3a', shade='#2d241e'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, hairline=[(8, 62), (18, 44), (36, 38), (50, 40), (64, 38), (82, 44), (92, 62)]),
  dome('front', top=-4, w=48, cy=44, n=12, amp=6, soft=True, seed=73, sb=64) + thick_brows(64, _c('#2d241e'), 4.4, 15, 0, 13) +
  [x for cx in (35, 65) for x in (L(blob([(cx - 12, 70), (cx + 12, 70), (cx + 12, 82), (cx - 12, 82)], 4), _c('#4a7ac0'), 'f'),
                                  L(blob([(cx - 9, 72), (cx + 9, 72), (cx + 9, 80), (cx - 9, 80)], 4), _c('#d8d0b8'), 'f', False))] +
  [L(ell(50, 86, 7, 6), NOSE, 'f')],
  dome('side', top=-4, w=48, cy=44, n=12, amp=6, soft=True, seed=73, nape=84, fr=50) + side_brow(64, _c('#2d241e'), 4.2) +
  [L(blob([(72, 70), (90, 70), (90, 82), (74, 82)], 4), _c('#4a7ac0'), 'f'), L(ell(92, 86, 5, 5), NOSE, 'f'), L([(72, 74), (48, 70)], _c('#4a7ac0'), 'f', False, False, 2.4)],
  dome('back', top=-4, w=48, cy=44, n=12, amp=6, soft=True, seed=73, nape=84))
