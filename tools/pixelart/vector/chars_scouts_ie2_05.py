"""Ojeadores de IE2 (scouts-ie2), tanda 05: dibujados a partir de su retrato de Victory Road; claves 'scouts-ie2:<id>'.

Ninguno de esta tanda tiene modelo 3D: el frente sale del retrato y el perfil y la espalda se deducen de cómo cae ese
peinado. Reutiliza las ayudas de los ojeadores de IE1 (dome/hl/face de la tanda 09, bowl/round_specs de la 03...)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars import longhair, messy  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401
from chars_scouts_ie1_09 import dome, hl, face, face_side, F, P, mark, _c  # noqa: F401
from chars_scouts_ie1_03 import bowl, round_specs, eyes_custom, side_eye_custom, thick_brows, side_brow  # noqa: F401
from chars_scouts_ie1_10 import skull, squint, nose_tri  # noqa: F401
from chars_scouts_ie1_02 import mir  # noqa: F401
from chars_vr_nikogawa import crop, brows, brow_side, blush  # noqa: F401

K = 'scouts-ie2:'
WHITE = (248, 248, 248, 255)
BLACK = (28, 22, 26, 255)
ORANGE_CHEEK = (240, 150, 90, 255)


def C(pid, body, palette, f, front, side, back):
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        # el nacimiento del pelo baja por el borde de la cara: así su raya no cruza el pelo de los lados
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[K + pid] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def fr(pts, c='mid'):
    """Mechón o flequillo por delante de la cara."""
    return L(outline(pts), c, 'f')


# ---------------------------------------------------------------------------------------------------------------- 1-8

# Leon Hotair: casco de pelo verde azulado liso y abultado, con el flequillo echado hacia la derecha de la imagen y un remolino
# en la coronilla; ojos castaños grandes, cejas fruncidas y sonrisa
C('leon-hotair', 'normal', P('#5d8a80', '#f9bc7d', iris='#6a3a1a'),
  F(eyes='normal', brows='angry', mouth='smile', mouth_y=93,
    hairline=[(8, 70), (14, 58), (24, 52), (40, 50), (54, 48), (66, 54), (76, 60), (84, 64), (92, 70)]),
  dome('front', top=0, w=48, cy=46, sb=72) + [strand([(46, 6), (58, 18), (70, 22)], 'deep', 'b', 1.2), strand([(30, 20), (40, 36)], 'deep', 'b', 1.0)],
  dome('side', top=0, w=48, cy=46, nape=88, fr=52) + [strand([(40, 6), (60, 16), (80, 30)], 'deep', 'b', 1.2)],
  dome('back', top=0, w=48, cy=46, nape=88) + [strand([(50, 4), (56, 20), (48, 36)], 'deep', 'b', 1.2)])

# Leon Morcey: pelo azul marino casi negro con raya en medio, recogido en dos moños bajos a los lados de la cara sujetos con
# anillas doradas; diadema dorada con una pieza en la frente; ojos castaños grandes, colorete y boca fruncida
GOLD = _c('#e0b030')
def _morcey_buns(view):
    if view == 'front':
        out = []
        for s in (-1, 1):
            cx = 50 + s * 42
            out += [L(blob([(cx - 9, 64), (cx + 9, 62), (cx + 10, 80), (cx, 90), (cx - 10, 80)], 6), 'mid', 'f'),
                    L(blob([(cx - 7, 56), (cx + 7, 56), (cx + 7, 63), (cx - 7, 63)], 4), GOLD, 'f')]
        return out
    if view == 'side':
        return [L(blob([(26, 64), (42, 62), (44, 80), (34, 90), (24, 80)], 6), 'mid', 'f'), L(blob([(28, 56), (42, 56), (42, 63), (28, 63)], 4), GOLD, 'f')]
    out = []
    for s in (-1, 1):
        cx = 50 + s * 42
        out += [L(blob([(cx - 9, 64), (cx + 9, 62), (cx + 10, 80), (cx, 90), (cx - 10, 80)], 6), 'mid'),
                L(blob([(cx - 7, 56), (cx + 7, 56), (cx + 7, 63), (cx - 7, 63)], 4), GOLD, 'f')]
    return out
C('leon-morcey', 'normal', P('#14283a', '#fbc271', iris='#6a3a1a'),
  F(eyes='big', brows='angry', mouth='frown', mouth_y=93, hairline=[(8, 66), (18, 54), (32, 48), (50, 44), (68, 48), (82, 54), (92, 66)]),
  dome('front', top=2, w=44, cy=46, sb=64) + [strand([(50, 4), (50, 44)], 'deep', 'b', 1.2)] + _morcey_buns('front') +
  [L(quad((26, 52), (50, 46), (74, 52)), GOLD, 'f', False, False, 2.2), L(blob([(45, 46), (55, 46), (55, 52), (45, 52)], 4), GOLD, 'f')] + blush(87),
  dome('side', top=2, w=44, cy=46, nape=72, fr=50) + _morcey_buns('side') + [L([(84, 52), (60, 48)], GOLD, 'f', False, False, 2.2)],
  dome('back', top=2, w=44, cy=46, nape=72) + [strand([(50, 4), (50, 66)], 'deep', 'b', 1.0)] + _morcey_buns('back'))

# Lewis Brownie: sombrero de paja marrón grisáceo de punta caída y ala ancha y blanda, con remiendos cosidos; asoma pelo verde
# por debajo; orejas puntiagudas de duende, ojos de punto bajo el ala, mofletes naranjas y sonrisa pequeña
HAT = _c('#b59c85')
def _brownie_hat(view):
    if view == 'front':
        return [L(outline([(6, 60), (14, 40), (30, 16), (46, -2), (60, -8, 1), (66, 6), (74, 24), (84, 42), (96, 62), (78, 66), (50, 62), (22, 66)]), HAT, 'f'),
                L(outline([(66, 6), (80, 30), (92, 54), (84, 60), (74, 34)]), tuple(int(v * 0.8) for v in HAT[:3]) + (255,), 'f', False),
                L([(36, 30), (42, 40)], OUTC, 'f', False, False, 1.0), L([(34, 36), (40, 32)], OUTC, 'f', False, False, 1.0),
                L([(24, 52), (34, 46), (42, 52)], OUTC, 'f', False, False, 1.0)]
    if view == 'side':
        return [L(outline([(-6, 62), (8, 42), (22, 18), (40, 0), (54, -10, 1), (64, 4), (78, 24), (92, 44), (104, 58), (80, 62), (40, 64), (10, 70)]), HAT, 'f'),
                L([(30, 30), (36, 40)], OUTC, 'f', False, False, 1.0)]
    return [L(outline([(4, 64), (14, 40), (30, 16), (46, -2), (40, -8, 1), (58, 4), (72, 22), (86, 42), (96, 64), (70, 70), (50, 68), (30, 70)]), HAT, 'f'),
            L(outline([(56, 4), (76, 28), (92, 56), (70, 66), (64, 34)]), tuple(int(v * 0.8) for v in HAT[:3]) + (255,), 'f', False),
            L([(34, 40), (44, 52)], OUTC, 'f', False, False, 1.0)]
C('lewis-brownie', 'bajito', P('#3a6a40', '#f8bb7c'),
  F(eyes='dot', brows=False, mouth='smile', mouth_y=92, hairline=False, ears=False, eye_y=76),
  [L(outline([(16, 72), (0, 64, 1), (14, 82)]), 'skin', 'f', True, True), L(outline([(84, 72), (100, 64, 1), (86, 82)]), 'skin', 'f', True, True),
   L(outline([(14, 64), (24, 72), (36, 66), (50, 70), (64, 66), (76, 72), (86, 64), (80, 58), (20, 58)]), 'mid', 'f')] + _brownie_hat('front') +
  [L(ell(24, 86, 4.6, 3.6), ORANGE_CHEEK, 'f', False), L(ell(76, 86, 4.6, 3.6), ORANGE_CHEEK, 'f', False)],
  [L(outline([(40, 70), (30, 60, 1), (46, 62)]), 'skin', 'f'), L(outline([(10, 70), (30, 80), (48, 72), (60, 66), (40, 60)]), 'mid')] + _brownie_hat('side') +
  [L(ell(78, 86, 3.6, 3), ORANGE_CHEEK, 'f', False)],
  [L(outline([(12, 66), (20, 80), (50, 84), (80, 80), (88, 66)]), 'mid')] + _brownie_hat('back'))

# Lillie Pink S Quattro: casco de superhéroe crema que le tapa toda la cara salvo la barbilla, con el visor blanco rodeado de
# franjas rosa y amarilla y dos antenas largas en punta; asoma melena rubia por los lados y un pañuelo blanco al cuello
CREAM, VPINK, VYEL = _c('#fdf3d0'), _c('#e8a0b8'), _c('#f4d860')
def _quattro(view):
    if view == 'front':
        return [L(outline([(10, 60), (-6, 74, 1), (12, 72), (8, 96, 1), (20, 84), (26, 98, 1), (30, 80)]), 'mid'),
                L(outline([(90, 60), (106, 74, 1), (88, 72), (92, 96, 1), (80, 84), (74, 98, 1), (70, 80)]), 'mid'),
                L(outline([(14, 84), (10, 50), (16, 22), (34, 6), (50, 2), (66, 6), (84, 22), (90, 50), (86, 84), (66, 90), (60, 82), (40, 82), (34, 90)]), CREAM, 'f'),
                L(outline([(24, 70), (22, 44), (34, 22), (50, 16), (66, 22), (78, 44), (76, 70), (56, 82), (44, 82)]), VPINK, 'f', False),
                L(outline([(30, 66), (30, 44), (40, 28), (50, 24), (60, 28), (70, 44), (70, 66), (56, 76), (44, 76)]), VYEL, 'f', False),
                L(outline([(34, 62), (34, 44), (42, 32), (50, 30), (58, 32), (66, 44), (66, 62), (54, 72), (46, 72)]), WHITE, 'f', False),
                L(outline([(18, 30), (4, -14, 1), (24, 22)]), CREAM, 'f'), L(outline([(82, 30), (96, -14, 1), (76, 22)]), CREAM, 'f'),
                L(quad((44, 94), (50, 97), (56, 94)), OUTC, 'f', False, False, 1.2)]
    if view == 'side':
        return [L(outline([(10, 56), (-4, 80, 1), (12, 76), (8, 100, 1), (22, 86), (34, 96, 1), (40, 76)]), 'mid'),
                L(outline([(30, 84), (8, 66), (8, 34), (26, 10), (50, 2), (74, 8), (90, 26), (94, 50), (92, 82), (82, 90), (72, 82), (50, 86)]), CREAM, 'f'),
                L(outline([(70, 70), (66, 44), (74, 24), (90, 30), (93, 50), (92, 76)]), VPINK, 'f', False),
                L(outline([(76, 64), (74, 44), (80, 32), (91, 36), (92, 66)]), WHITE, 'f', False),
                L(outline([(40, 22), (32, -18, 1), (50, 16)]), CREAM, 'f')]
    return [L(outline([(10, 60), (-6, 80, 1), (12, 76), (10, 100, 1), (30, 86), (50, 102, 1), (70, 86), (90, 100, 1), (88, 76), (106, 80, 1), (90, 60)]), 'mid'),
            L(outline([(10, 74), (8, 40), (20, 16), (50, 2), (80, 16), (92, 40), (90, 74), (50, 80)]), CREAM, 'f'),
            L(outline([(18, 30), (4, -14, 1), (24, 22)]), CREAM, 'f'), L(outline([(82, 30), (96, -14, 1), (76, 22)]), CREAM, 'f')]
C('lillie-pink-s-quattro', 'chica', P('#f4dc90', '#d9a8a0'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _quattro('front'), _quattro('side'), _quattro('back'))

# Lionel Silent (portero): pinchos naranjas de punta por arriba, una cinta blanca ancha en la frente y los lados de la cabeza
# cubiertos por un casco azul marino; ojos blancos redondos de pupila pequeña, cejas fruncidas y boca torcida
NAVY = _c('#3e3a52')
def _silent(view):
    if view == 'front':
        return [L(outline([(10, 44), (2, 26, 1), (18, 30), (16, 6, 1), (32, 20), (40, -10, 1), (50, 14), (62, -6, 1), (68, 18), (86, 4, 1), (84, 28), (98, 26, 1),
                           (90, 44)]), 'mid'),
                L(outline([(10, 90), (8, 60), (12, 44), (88, 44), (92, 60), (90, 90), (80, 88), (80, 60), (20, 60), (20, 88)]), NAVY, 'f'),
                L(blob([(12, 42), (50, 40), (88, 42), (88, 58), (50, 56), (12, 58)], 4), WHITE, 'f'),
                L(blob([(36, 42), (64, 42), (64, 56), (36, 56)], 4), (230, 230, 236, 255), 'f', False)]
    if view == 'side':
        return [L(outline([(18, 48), (4, 34, 1), (20, 32), (10, 10, 1), (30, 18), (34, -8, 1), (48, 12), (64, -6, 1), (66, 16), (88, 8, 1), (80, 28), (94, 36, 1),
                           (80, 44)]), 'mid'),
                L(outline([(8, 50), (84, 46), (86, 58), (60, 60), (58, 92), (14, 90), (4, 70)]), NAVY, 'f'),
                L(blob([(6, 44), (86, 42), (88, 56), (8, 60)], 4), WHITE, 'f')]
    return [L(outline([(10, 48), (2, 28, 1), (18, 30), (16, 6, 1), (32, 20), (40, -8, 1), (50, 14), (62, -6, 1), (68, 18), (86, 4, 1), (84, 28), (98, 28, 1),
                       (90, 48)]), 'mid'),
            L(outline([(10, 92), (6, 60), (12, 46), (88, 46), (94, 60), (90, 92), (50, 96)]), NAVY, 'f'),
            L(blob([(10, 44), (50, 42), (90, 44), (90, 58), (50, 56), (10, 58)], 4), WHITE, 'f')]
C('lionel-silent', 'normal', P('#e98009', '#fbe6d0'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=94, hairline=False, ears=False, eye_y=76),
  _silent('front') + [L([(28, 63), (42, 68)], OUTC, 'f', False, False, 3.0), L([(72, 63), (58, 68)], OUTC, 'f', False, False, 3.0)],
  _silent('side'), _silent('back'))

# Lisle Plotter: pelo verde azulado oscuro en mechones largos y lacios que le caen por los lados hasta el cuello, un flequillo
# en pico que le tapa media frente y un mechón tieso hacia fuera a la derecha; ojos afilados de iris verdoso y boca recta
C('lisle-plotter', 'normal', P('#256572', '#fcc271', iris='#8a9a40'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=94, hairline=False),
  longhair('front', length=100, flare=2, top=2, ends=3) +
  [fr([(14, 74, 1), (16, 40), (30, 22), (52, 18), (70, 26), (78, 40), (66, 46), (58, 70, 1), (52, 46), (40, 56), (30, 50), (24, 60)]),
   L(outline([(86, 70), (108, 64, 1), (88, 78)]), 'mid'), L([(72, 64), (58, 68)], OUTC, 'f', False, False, 3.0)],
  longhair('side', length=100, flare=2, top=2) + [L(outline([(70, 6), (92, 24), (94, 50), (88, 64, 1), (82, 46), (74, 36)]), 'mid', 'f')],
  longhair('back', length=100, flare=2, top=2, ends=3) + [L(outline([(14, 70), (-8, 64, 1), (12, 78)]), 'mid')])

# Lou Daguerre: pelo rosa malva corto con dos rizos que se levantan a los lados como cuernos; orejas grandes, ojos redondos
# con los párpados medio caídos, nariz naranja de botón, mofletes naranjas y boca fruncida
C('lou-daguerre', 'normal', P('#d39e91', '#fbbc7b', iris='#2a1a14'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=95, big_ears=2, ear_out=2, nose=(50, 85, 3.4),
    hairline=[(8, 62), (16, 50), (30, 46), (42, 50), (54, 44), (68, 48), (84, 50), (92, 62)]),
  crop('front', top=6, side=62, w=2) +
  [L(outline([(14, 34), (4, 24), (2, 8, 1), (12, 18), (22, 26)]), 'mid'), L(outline([(86, 34), (96, 24), (98, 8, 1), (88, 18), (78, 26)]), 'mid'),
   *[l for cx in (36, 64) for l in (L(ell(cx, 76, 8, 8.4), WHITE, 'f', True, True), L(ell(cx, 79, 3, 3.2), BLACK, 'f', False),
                                    L(blob([(cx - 8.6, 74), (cx - 6, 68), (cx, 66.5), (cx + 6, 68), (cx + 8.6, 74)], 4), 'skin', 'f', False),
                                    L([(cx - 8.6, 74), (cx + 8.6, 74)], OUTC, 'f', False, False, 2.2))],
   L(ell(22, 90, 5, 4.4), ORANGE_CHEEK, 'f', False), L(ell(78, 90, 5, 4.4), ORANGE_CHEEK, 'f', False),
   L(ell(50, 85, 3.2, 2.8), (230, 120, 70, 255), 'f', True)],
  crop('side', top=6, nape=84, w=2) + [L(outline([(30, 20), (20, 8), (18, -6, 1), (30, 6), (40, 16)]), 'mid'),
                                      L([(74, 70), (86, 70)], OUTC, 'f', False, False, 2.6), L(ell(76, 90, 4, 3.6), ORANGE_CHEEK, 'f', False)],
  crop('back', top=6, nape=84, w=2) + [L(outline([(14, 34), (4, 24), (2, 8, 1), (12, 18), (22, 26)]), 'mid'),
                                      L(outline([(86, 34), (96, 24), (98, 8, 1), (88, 18), (78, 26)]), 'mid')])

# Lou Fauntleroy: cara larguísima y pálida con un mentón enorme, frente alta y despejada y una peluca de rizos dorados en
# rollos a los lados de la cabeza; ojos entornados de aburrimiento y boca recta
GOLDH = _c('#e9a83c')
LONGFACE = blob([(18, 48), (50, 30), (82, 48), (86, 76), (84, 100), (72, 116), (50, 122), (28, 116), (16, 100), (14, 76)])
def _curls(view):
    out = []
    xs = (-1, 1) if view != 'side' else (-1,)
    for s in xs:
        cx = 50 + s * 42 if view != 'side' else 34
        for cy in (40, 58, 76):
            out.append(L(ell(cx, cy, 11, 9.5), 'mid', 'b'))
            out.append(strand(quad((cx - 6, cy), (cx, cy - 6), (cx + 5, cy + 1)), 'deep', 'b', 1.2))
    return out
C('lou-fauntleroy', 'normal', P('#e9a83c', '#fdeab7', iris='#3a2a20'),
  F(eyes='dot', brows=True, mouth='line', mouth_y=100, hairline=False, ears=False, face_front=LONGFACE, face_side=face_side(chin=14, jaw=4), eye_y=74),
  [L(blob([(18, 50), (20, 26), (34, 12), (50, 8), (66, 12), (80, 26), (82, 50)], 8), 'skin', 'b')] + _curls('front') +
  [L([(28, 71), (42, 71)], OUTC, 'f', False, False, 2.2), L([(58, 71), (72, 71)], OUTC, 'f', False, False, 2.2), L([(40, 100), (60, 100)], OUTC, 'f', False, False, 1.4)],
  [L(blob([(30, 14), (54, 6), (78, 14), (86, 36), (60, 40), (30, 40)], 8), 'skin')] + _curls('side') +
  [L(ell(22, 46, 11, 9.5), 'mid'), L(ell(20, 64, 11, 9.5), 'mid')],
  [L(blob([(18, 70), (16, 30), (30, 12), (50, 6), (70, 12), (84, 30), (82, 70), (50, 76)], 8), 'mid')] + _curls('back') +
  [strand(quad((30, 20), (50, 14), (70, 20)), 'deep', 'b', 1.2), strand(quad((26, 36), (50, 30), (74, 36)), 'deep', 'b', 1.2)])


# --------------------------------------------------------------------------------------------------------------- 9-16

# Lucia Ander: pelo magenta peinado hacia arriba y atrás en un tupé alto, con los lados de la cabeza rapados; cara larga y
# pálida, orejas grandes con un pendiente de perla, ojos verdes afilados con raya y labios rosa oscuro
LIP = _c('#c0507a')
C('lucia-ander', 'chica', P('#a12774', '#e3ccad', iris='#2a9a40'),
  F(eyes='sharp', brows='angry', mouth='none', big_ears=2, ear_out=2, hairline=False, face_front=face(chin=106), face_side=face_side(chin=6)),
  [L(blob([(18, 56), (16, 34), (28, 16), (50, 10), (72, 16), (84, 34), (82, 56)], 8), 'skin')] +
  [L(outline([(22, 40), (18, 14), (30, -4), (50, -10), (70, -4), (80, 12), (76, 40), (64, 30), (36, 30)]), 'mid'),
   L(outline([(56, -8), (72, -2), (80, 14), (76, 38), (66, 26)]), 'shade', 'b', False),
   strand([(40, -4), (42, 26)], 'deep', 'b', 1.2), strand([(56, -6), (58, 26)], 'deep', 'b', 1.2),
   L(ell(14, 84, 2.4, 2.4), WHITE, 'f', True), L(blob([(43, 95), (50, 93), (57, 95), (50, 99)], 4), LIP, 'f')],
  [L(outline([(70, 32), (76, 16), (66, 0), (46, -10), (24, -6), (8, 10), (4, 34), (20, 40), (40, 36)]), 'mid'),
   L(outline([(6, 30), (26, 38), (40, 34), (30, 22)]), 'shade', 'b', False), L(ell(46, 84, 2.2, 2.2), WHITE, 'f', True)],
  [L(outline([(24, 44), (18, 14), (30, -4), (50, -10), (70, -4), (82, 14), (76, 44), (50, 50)]), 'mid'),
   L(outline([(56, -8), (74, 0), (82, 16), (76, 44), (64, 46)]), 'shade', 'b', False),
   strand([(40, -4), (42, 40)], 'deep', 'b', 1.0), strand([(58, -4), (58, 40)], 'deep', 'b', 1.0)])

# Lucille Strummon: media melena castaño rojiza con las puntas hacia fuera y una diadema azul celeste; flequillo echado a un
# lado; ojos entornados de pestañas, pecas y boca recta
SKY = _c('#70c0d0')
C('lucille-strummon', 'chica', P('#83423e', '#fabc7c', iris='#2a1a14'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=94, hairline=[(8, 70), (16, 56), (28, 48), (44, 52), (60, 44), (76, 48), (86, 58), (92, 70)]),
  longhair('front', length=96, flare=8, top=4, ends=3) +
  [L(quad((14, 44), (50, 8), (86, 44)), SKY, 'b', False, False, 3.4),
   L(ell(32, 88, 0.9, 0.9), (190, 100, 70, 255), 'f', False), L(ell(28, 86, 0.9, 0.9), (190, 100, 70, 255), 'f', False),
   L(ell(68, 88, 0.9, 0.9), (190, 100, 70, 255), 'f', False), L(ell(72, 86, 0.9, 0.9), (190, 100, 70, 255), 'f', False)],
  longhair('side', length=96, flare=8, top=4) + [L(quad((34, 4), (60, 4), (84, 26)), SKY, 'b', False, False, 3.4)],
  longhair('back', length=96, flare=8, top=4, ends=3) + [L(quad((14, 40), (50, 2), (86, 40)), SKY, 'b', False, False, 3.4)])

# Luis Springs (portero): tupé enorme castaño rojizo, plano por arriba y en pico hacia la frente, con los lados rapados;
# gafas rojas de cristales morados caídas sobre la nariz, ojos blancos de enfado y boca recta
RED, PURP = _c('#c03030'), _c('#9a7ab8')
def _springs(view):
    if view == 'front':
        return [L(blob([(18, 56), (16, 34), (28, 16), (50, 10), (72, 16), (84, 34), (82, 56)], 8), 'skin_d'),
                L(outline([(6, 22), (10, 2), (30, -6), (50, -2), (70, -8), (92, -2), (96, 20), (80, 36), (60, 44), (50, 50), (40, 44), (20, 36)]), 'mid'),
                fr([(36, 44), (50, 40), (64, 44), (56, 56), (50, 70, 1), (44, 56)]),
                L(outline([(56, -6), (90, -2), (94, 18), (78, 34), (58, 40)]), 'shade', 'b', False),
                strand([(20, 6), (48, 14)], 'deep', 'b', 1.0), strand([(54, 12), (84, 4)], 'deep', 'b', 1.0)]
    if view == 'side':
        return [L(blob([(30, 66), (14, 52), (16, 24), (40, 14), (64, 22), (60, 50)], 8), 'skin_d'),
                L(outline([(10, 26), (14, 4), (40, -6), (70, -6), (96, 4), (100, 22), (86, 36), (70, 42), (50, 36), (24, 36)]), 'mid'),
                L(outline([(10, 26), (14, 6), (30, 0), (40, 30), (24, 34)]), 'shade', 'b', False)]
    return [L(blob([(18, 60), (16, 34), (28, 16), (50, 10), (72, 16), (84, 34), (82, 60), (50, 70)], 8), 'skin_d'),
            L(outline([(6, 24), (10, 2), (30, -6), (50, -2), (70, -8), (92, -2), (96, 22), (80, 34), (50, 38), (20, 34)]), 'mid'),
            L(outline([(56, -4), (90, 0), (94, 20), (80, 32), (58, 34)]), 'shade', 'b', False)]
C('luis-springs', 'normal', P('#902402', '#f9bc7e', iris='#2a1a14'),
  F(eyes='round', brows='angry', mouth='line', mouth_y=95, hairline=False, big_ears=1, eye_y=74),
  _springs('front') + [L(blob([(22, 78), (46, 78), (45, 85), (24, 85)], 4), PURP, 'f', True), L(blob([(54, 78), (78, 78), (76, 85), (55, 85)], 4), PURP, 'f', True),
                       L([(20, 78), (80, 78)], RED, 'f', False, False, 2.2)],
  _springs('side') + [L(blob([(74, 78), (88, 78), (88, 85), (75, 85)], 4), PURP, 'f', True), L([(74, 78), (48, 72)], RED, 'f', False, False, 2.0)],
  _springs('back'))

# Luke Severin: pelo verde menta muy claro en pinchos que se abren hacia los lados como orejas; una pieza roja con una gema
# hexagonal dorada en la frente; piel morena, ojos amarillos afilados y media sonrisa
GEM = _c('#e8b830')
C('luke-severin', 'normal', P('#cbe3be', '#c38533', iris='#e0b020'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=[(8, 66), (14, 54), (26, 62), (34, 50), (44, 56), (56, 56), (66, 50), (74, 62), (86, 54), (92, 66)]),
  messy('front', amp=9, n=9, seed=21, lo=70, rx=44, ry=38, sweep=0.0) +
  [L(outline([(16, 40), (-6, 20, 1), (14, 26)]), 'mid'), L(outline([(84, 40), (106, 20, 1), (86, 26)]), 'mid'),
   L(outline([(14, 70), (2, 84, 1), (16, 80)]), 'mid'), L(outline([(86, 70), (98, 84, 1), (84, 80)]), 'mid'),
   L(blob([(40, 30), (60, 30), (62, 56), (38, 56)], 4), RED, 'f'), L(outline([(44, 40), (56, 40), (60, 48), (50, 56), (40, 48)]), GEM, 'f', True)],
  messy('side', amp=9, n=9, seed=21, rx=44, ry=38) + [L(outline([(30, 30), (10, 10, 1), (34, 20)]), 'mid'), L(blob([(80, 34), (90, 36), (92, 54), (82, 54)], 4), RED, 'f')],
  messy('back', amp=9, n=9, seed=21, rx=44, ry=38) + [L(outline([(16, 40), (-6, 20, 1), (14, 26)]), 'mid'), L(outline([(84, 40), (106, 20, 1), (86, 26)]), 'mid')])

# Lynne Mandel: pelo lila en media melena con flequillo recto, dos coletas planas y anchas que salen hacia arriba a los lados
# y dos mechones que le caen por las mejillas; ojos verde azulado grandes, colorete y sonrisa
def _mandel_tails(view):
    if view == 'side':
        return [L(outline([(30, 30), (6, 10), (-2, 22), (2, 40), (20, 44)]), 'mid')]
    return [L(outline([(20, 30), (-6, 12), (-12, 26), (-8, 44), (14, 46)]), 'mid'), L(outline([(80, 30), (106, 12), (112, 26), (108, 44), (86, 46)]), 'mid'),
            L(outline([(-6, 14), (-12, 26), (-8, 44), (-2, 40), (-4, 24)]), 'shade', 'b', False)]
C('lynne-mandel', 'chica', P('#a388a6', '#fcebc2', iris='#2a8a90'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=[(8, 66), (14, 54), (20, 60), (24, 56), (76, 56), (80, 60), (86, 54), (92, 66)]),
  _mandel_tails('front') + bowl('front', top=2, side=80) +
  [L(outline([(10, 70), (2, 86), (8, 104, 1), (18, 92), (20, 74)]), 'mid'), L(outline([(90, 70), (98, 86), (92, 104, 1), (82, 92), (80, 74)]), 'mid')] + blush(86, (240, 160, 170, 255), 22, 4.6),
  _mandel_tails('side') + bowl('side', top=2, nape=88),
  _mandel_tails('back') + bowl('back', top=2, nape=90))

# Mac Gabbon: pelo granate en una cúpula lisa que se abre a los lados en dos alas de punta, con un flequillo enorme en pico que
# le tapa el ojo izquierdo de la imagen; piel pálida, el otro ojo amarillo de gato y boca recta
C('mac-gabbon', 'normal', P('#822942', '#e2cbad', iris='#e0b020'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=95, hairline=False),
  [L(outline([(18, 64), (8, 40), (-10, 24, 1), (14, 22), (30, 4), (50, -4), (70, 4), (86, 22), (110, 24, 1), (92, 40), (82, 64), (80, 50), (20, 50)]), 'mid'),
   L(outline([(60, -2), (84, 20), (106, 26), (88, 40), (82, 60), (74, 30)]), 'shade', 'b', False),
   fr([(14, 64), (16, 40), (30, 20), (50, 12), (62, 20), (60, 44), (56, 66), (50, 96, 1), (40, 88), (26, 86), (16, 78)])],
  [L(outline([(70, 42), (82, 30), (78, 10), (56, -4), (30, -2), (12, 12), (-10, 20, 1), (6, 32), (4, 52), (12, 74), (30, 82), (44, 72), (56, 54)]), 'mid'),
   L(outline([(6, 34), (30, 40), (44, 60), (30, 80), (12, 72)]), 'shade', 'b', False), fr([(70, 22), (90, 34), (92, 60), (86, 80, 1), (80, 54), (74, 40)])],
  [L(outline([(18, 72), (8, 40), (-10, 24, 1), (14, 22), (30, 4), (50, -4), (70, 4), (86, 22), (110, 24, 1), (92, 40), (82, 72), (50, 80)]), 'mid'),
   L(outline([(58, 0), (84, 20), (106, 26), (88, 40), (82, 70), (62, 74)]), 'shade', 'b', False)])

# Mac Robat: pelo castaño casi negro en casco con flequillo recto, bajo una gorra redonda naranja con gajos amarillos; ojos
# rojizos de enfado y boca de puchero
CAP, CAPY = _c('#e06a18'), _c('#f4c020')
def _robat_cap(view):
    if view == 'front':
        return [L(outline([(14, 34), (20, 12), (36, 0), (50, -2), (64, 0), (80, 12), (86, 34), (50, 30)]), CAP),
                L(outline([(40, 2), (50, -1), (60, 2), (58, 30), (42, 30)]), CAPY, 'b', False),
                L(outline([(24, 10), (32, 4), (34, 32), (20, 34)]), CAPY, 'b', False), L(outline([(76, 10), (68, 4), (66, 32), (80, 34)]), CAPY, 'b', False)]
    if view == 'side':
        return [L(outline([(16, 38), (14, 16), (32, 2), (54, -2), (74, 6), (86, 24), (84, 36), (50, 34)]), CAP),
                L(outline([(46, 0), (58, 0), (62, 34), (46, 34)]), CAPY, 'b', False)]
    return [L(outline([(14, 36), (20, 12), (36, 0), (50, -2), (64, 0), (80, 12), (86, 36), (50, 32)]), CAP),
            L(outline([(40, 2), (50, -1), (60, 2), (58, 32), (42, 32)]), CAPY, 'b', False)]
C('mac-robat', 'normal', P('#332013', '#fbc272', iris='#c03a1a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, hairline=[(8, 64), (14, 58), (86, 58), (92, 64)]),
  bowl('front', top=10, side=84) + _robat_cap('front') + [fr([(16, 56), (18, 38), (50, 34), (82, 38), (84, 56), (70, 60), (50, 60), (30, 60)])],
  bowl('side', top=10, nape=92) + _robat_cap('side'),
  bowl('back', top=10, nape=94) + _robat_cap('back'))

# Mal Maroon: pelo rubio muy claro en pinchos revueltos con mechones que le caen por la frente y le tapan el ojo izquierdo de
# la imagen; ojos negros afilados y boca recta
C('mal-maroon', 'normal', P('#f2dc9a', '#fcc273', iris='#20181a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=[(8, 66), (14, 56), (24, 66), (30, 52), (42, 62), (52, 50), (62, 58), (72, 50), (82, 58), (92, 66)]),
  messy('front', amp=14, n=11, seed=33, lo=70, sweep=0.2) + [fr([(20, 50), (40, 44), (44, 62), (36, 82, 1), (32, 66), (24, 72, 1), (22, 60)])],
  messy('side', amp=14, n=11, seed=33, sweep=0.2),
  messy('back', amp=14, n=11, seed=33, sweep=0.2))


# -------------------------------------------------------------------------------------------------------------- 17-24

# Malcolm Blue D Shirker: casco negro de visor con franjas azules y grises que le tapa la cara hasta la boca en pico, rodeado
# de una melena azul marino desgreñada; solo se le ven la barbilla pálida y la boca con los dientes
HELM, HGREY, HBLUE = _c('#2a2a30'), _c('#9a9aa2'), _c('#3a7ad8')
def _shirker(view):
    if view == 'front':
        return [L(outline([(14, 80), (-4, 66, 1), (8, 56), (-6, 40, 1), (10, 30), (4, 10, 1), (24, 10), (36, -6, 1), (50, 2), (66, -6, 1), (76, 10), (96, 8, 1),
                           (90, 30), (106, 44, 1), (92, 56), (104, 70, 1), (86, 80)]), 'mid'),
                L(outline([(16, 84), (12, 50), (18, 24), (34, 8), (50, 4), (66, 8), (82, 24), (88, 50), (84, 84), (64, 82), (50, 96, 1), (36, 82)]), HELM, 'f'),
                L(outline([(24, 70), (22, 44), (32, 22), (44, 14), (40, 40), (42, 70)]), HGREY, 'f', False),
                L(outline([(76, 70), (78, 44), (68, 22), (56, 14), (60, 40), (58, 70)]), HGREY, 'f', False),
                L(outline([(28, 66), (28, 46), (36, 28), (40, 46), (38, 66)]), HBLUE, 'f', False),
                L(outline([(72, 66), (72, 46), (64, 28), (60, 46), (62, 66)]), HBLUE, 'f', False),
                L([(42, 98), (58, 98)], WHITE, 'f', False, False, 2.4), L([(40, 98), (60, 98)], OUTC, 'f', False, False, 0.8)]
    if view == 'side':
        return [L(outline([(16, 84), (-4, 74, 1), (6, 60), (-8, 44, 1), (8, 34), (2, 14, 1), (22, 14), (32, -4, 1), (48, 6), (40, 60)]), 'mid'),
                L(outline([(24, 70), (10, 46), (18, 18), (44, 4), (72, 8), (88, 28), (92, 54), (90, 86), (78, 84), (70, 66), (50, 70)]), HELM, 'f'),
                L(outline([(70, 60), (66, 36), (76, 18), (88, 32), (90, 60)]), HGREY, 'f', False),
                L(outline([(74, 56), (72, 38), (78, 26), (86, 40), (86, 56)]), HBLUE, 'f', False)]
    return [L(outline([(14, 84), (-4, 70, 1), (8, 58), (-6, 42, 1), (10, 30), (4, 10, 1), (24, 10), (36, -6, 1), (50, 2), (66, -6, 1), (76, 10), (96, 8, 1),
                       (90, 30), (106, 44, 1), (92, 58), (104, 72, 1), (86, 84), (70, 96, 1), (60, 86), (50, 98, 1), (40, 86), (30, 96, 1)]), 'mid'),
            L(outline([(56, 4), (84, 16), (96, 44), (90, 76), (70, 86)]), 'shade', 'b', False)]
C('malcolm-blue-d-shirker', 'normal', P('#19395a', '#f4e8c8'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _shirker('front'), _shirker('side'), _shirker('back'))

# Manuel Kinart: pelo azul grisáceo estirado hacia atrás y atado arriba con un pañuelo anudado; parche de madera con forma de
# guitarra sobre el ojo izquierdo de la imagen, sujeto con una cinta naranja en diagonal; el otro ojo afilado y una sonrisa
# enorme
WOOD, STRAP = _c('#a08060'), _c('#e07a2a')
C('manuel-kinart', 'normal', P('#506f79', '#f3bf94', iris='#20181a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=[(8, 62), (16, 50), (30, 44), (50, 42), (70, 44), (84, 50), (92, 62)]),
  crop('front', top=2, side=64, w=2) +
  [L(outline([(66, 10), (88, -6, 1), (80, 10), (98, 2, 1), (84, 20)]), 'mid'),
   L(quad((14, 62), (50, 54), (86, 22)), STRAP, 'f', False, False, 3.4),
   L(blob([(22, 66), (40, 62), (48, 72), (44, 86), (30, 90), (20, 82)], 6), WOOD, 'f', True),
   L(ell(34, 76, 3, 3), (60, 40, 30, 255), 'f', False),
   L(quad((32, 92), (50, 104), (70, 92)), OUTC, 'f', False, False, 1.6)],
  crop('side', top=2, nape=82, w=2) + [L(outline([(40, 4), (30, -12, 1), (46, 0), (56, -8, 1), (52, 8)]), 'mid')],
  crop('back', top=2, nape=82, w=2) + [L(outline([(66, 10), (88, -6, 1), (80, 10), (98, 2, 1), (84, 20)]), 'mid'),
                                      L(quad((12, 66), (50, 70), (88, 22)), STRAP, 'f', False, False, 3.0)])

# Marcy Laise: pelo naranja con raya en medio, recogido en dos coletas enormes y esponjosas a los lados como nubes; ojos verdes
# entornados, pecas y una sonrisa tranquila
def _puffs(view):
    if view == 'side':
        return [L(blob([(30, 20), (6, 10), (-12, 30), (-10, 66), (4, 90), (24, 86), (34, 60)], 8), 'mid')]
    out = []
    for s in (-1, 1):
        pts = [(50 + s * 30, 16), (50 + s * 46, 4), (50 + s * 62, 22), (50 + s * 64, 50), (50 + s * 60, 80), (50 + s * 44, 94), (50 + s * 32, 80), (50 + s * 34, 40)]
        out.append(L(blob(pts, 8), 'mid'))
        out.append(L(blob([(50 + s * 52, 14), (50 + s * 62, 30), (50 + s * 62, 70), (50 + s * 50, 88), (50 + s * 50, 50)], 6), 'shade', 'b', False))
    return out
C('marcy-laise', 'chica', P('#e8783e', '#fcd18a', iris='#3a8a50'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=94, hairline=[(8, 60), (18, 48), (34, 42), (50, 40), (66, 42), (82, 48), (92, 60)]),
  _puffs('front') + crop('front', top=4, side=60, shade=False) + [strand([(50, 4), (50, 40)], 'deep', 'b', 1.2),
                                                                 *[L(ell(x, y, 0.9, 0.9), (190, 100, 60, 255), 'f', False) for x, y in ((28, 86), (32, 88), (30, 90), (72, 86), (68, 88), (70, 90))]],
  _puffs('side') + crop('side', top=4, nape=80, shade=False),
  _puffs('back') + crop('back', top=4, nape=82, shade=False) + [strand([(50, 6), (50, 70)], 'deep', 'b', 1.0)])

# Marg Shuttle: media melena gris oscuro con un flequillo largo echado a un lado, una venda beige en la frente; ojos negros
# grandes de enfado, boca fruncida y manchitas de suciedad en la cara
BAND = _c('#e8d8c0')
C('marg-shuttle', 'chica', P('#6c6762', '#f9e7b8', iris='#1a1414'),
  F(eyes='normal', brows='angry', mouth='frown', mouth_y=94, hairline=[(8, 70), (14, 54), (24, 48), (40, 58), (56, 50), (72, 42), (86, 48), (92, 70)]),
  longhair('front', length=96, flare=4, top=2, ends=3) +
  [L(blob([(16, 56), (50, 52), (84, 56), (84, 64), (50, 62), (16, 64)], 4), BAND, 'b', True, True),
   fr([(12, 72, 1), (12, 44), (24, 22), (46, 14), (64, 20), (56, 30), (42, 46), (32, 64, 1), (28, 50), (20, 56)]),
   L(ell(26, 90, 1.4, 1.0), (170, 140, 110, 255), 'f', False), L(ell(66, 96, 1.2, 1.2), (80, 60, 50, 255), 'f', False)],
  longhair('side', length=96, flare=4, top=2) + [L(blob([(54, 54), (90, 52), (90, 60), (54, 62)], 4), BAND, 'b', True, True)],
  longhair('back', length=96, flare=4, top=2, ends=3) + [L(blob([(12, 52), (50, 56), (88, 52), (88, 60), (50, 64), (12, 60)], 4), BAND, 'b', True, True)])

# Marilyn Henshaw (portera): grandota de cara redonda y mofletuda; pañuelo naranja en la cabeza y rizos verde azulado que le
# abultan a los lados; ojos afilados con pestañas y labios naranjas gruesos
SCARF = _c('#db6e1d')
def _henshaw(view):
    if view == 'front':
        return [L(blob([(20, 54), (2, 58), (-6, 76), (0, 94), (16, 98), (24, 80)], 8), 'mid'), L(blob([(80, 54), (98, 58), (106, 76), (100, 94), (84, 98), (76, 80)], 8), 'mid'),
                L(outline([(10, 56), (12, 30), (28, 14), (50, 10), (72, 14), (88, 30), (90, 56), (70, 50), (30, 50)]), SCARF),
                L(outline([(62, 14), (84, 26), (90, 54), (74, 46), (70, 26)]), tuple(int(v * 0.82) for v in SCARF[:3]) + (255,), 'b', False)]
    if view == 'side':
        return [L(blob([(40, 50), (14, 54), (0, 74), (6, 96), (30, 100), (46, 80)], 8), 'mid'),
                L(outline([(6, 60), (8, 30), (30, 12), (60, 10), (82, 24), (88, 46), (60, 48), (30, 56)]), SCARF)]
    return [L(blob([(6, 56), (-6, 76), (0, 96), (30, 104), (50, 100), (70, 104), (100, 96), (106, 76), (94, 56)], 8), 'mid'),
            L(outline([(8, 62), (10, 30), (28, 14), (50, 10), (72, 14), (90, 30), (92, 62), (50, 66)]), SCARF)]
C('marilyn-henshaw', 'corpulento', P('#26616f', '#fcc271', iris='#20181a'),
  F(eyes='sharp', brows=True, mouth='none', hairline=False, face_front=blob([(14, 52), (50, 36), (86, 52), (94, 76), (86, 98), (66, 110), (50, 112), (34, 110), (14, 98), (6, 76)])),
  _henshaw('front') + [L(blob([(38, 94), (50, 90), (62, 94), (58, 102), (50, 104), (42, 102)], 6), _c('#f4902a'), 'f', True, True),
                       L([(40, 96), (60, 96)], OUTC, 'f', False, False, 1.0)],
  _henshaw('side') + [L(blob([(82, 92), (90, 92), (90, 100), (82, 100)], 4), _c('#f4902a'), 'f', True)],
  _henshaw('back'))

# Mark Izushy (portero): cabeza grande calva y pálida con un mechón castaño oscuro corto en lo alto y los lados castaños;
# ojitos tristes, cejas caídas y una nariz roja enorme y redonda
C('mark-izushy', 'corpulento', P('#473726', '#e4ccac', iris='#20181a'),
  F(eyes='dot', brows=False, mouth='none', hairline=False, face_front=blob([(14, 50), (50, 30), (86, 50), (92, 76), (84, 98), (64, 108), (50, 110), (36, 108), (16, 98), (8, 76)])),
  skull() + [L(blob([(36, 16), (50, 4), (64, 16), (60, 24), (40, 24)], 6), 'mid'),
             L(outline([(10, 72), (8, 56), (16, 50), (18, 72)]), 'mid'), L(outline([(90, 72), (92, 56), (84, 50), (82, 72)]), 'mid'),
             L([(30, 70), (40, 66)], OUTC, 'f', False, False, 1.6), L([(70, 70), (60, 66)], OUTC, 'f', False, False, 1.6),
             L(ell(50, 92, 8, 7.4), _c('#9a4a30'), 'f', True)],
  [L(blob([(30, 18), (50, 4), (68, 12), (60, 24)], 6), 'mid'), L(outline([(10, 60), (30, 56), (34, 76), (14, 80)]), 'mid'),
   L(ell(86, 92, 5, 6), _c('#9a4a30'), 'f', True)],
  [L(blob([(36, 16), (50, 4), (64, 16), (60, 24), (40, 24)], 6), 'mid'), L(outline([(10, 52), (50, 56), (90, 52), (88, 80), (50, 88), (12, 80)]), 'mid')])

# Mark Smudge (portero): adulto de cara larga; tupé verde oscuro ondulado, cejas gruesas, gafas rectangulares rojas, nariz
# larga y boca ancha
GLRED = _c('#c03030')
C('mark-smudge', 'delgado', P('#2d5d52', '#fbc273', iris='#20181a'),
  F(eyes='dot', brows=False, mouth='line', mouth_y=100, hairline=[(8, 62), (14, 50), (30, 46), (50, 50), (70, 46), (86, 50), (92, 62)],
    face_front=face(chin=110, jaw=2), face_side=face_side(chin=8, nose=3), mouth_w=14),
  [L(blob([(10, 58), (6, 30), (18, 8), (40, -6), (62, -2), (80, 6), (94, 24), (92, 58), (80, 48), (20, 48)], 8), 'mid'),
   L(blob([(60, -2), (82, 8), (94, 28), (90, 52), (76, 36)], 6), 'shade', 'b', False),
   strand([(24, 20), (40, 10), (56, 14)], 'deep', 'b', 1.2)] + thick_brows(64, 'mid', 4.0, 15, 0.3, 13) +
  [L(blob([(24, 70), (46, 70), (46, 82), (24, 82)], 3) + [(24, 70)], GLRED, 'f', False, False, 2.2),
   L(blob([(54, 70), (76, 70), (76, 82), (54, 82)], 3) + [(54, 70)], GLRED, 'f', False, False, 2.2), L([(46, 74), (54, 74)], GLRED, 'f', False, False, 2.0),
   L(quad((48, 76), (46, 88), (52, 90)), OUTC, 'f', False, False, 1.2), L([(38, 100), (62, 100)], OUTC, 'f', False, False, 1.4)],
  [L(blob([(70, 46), (82, 30), (84, 6), (60, -6), (30, -4), (8, 14), (4, 44), (14, 70), (30, 74), (44, 62)], 8), 'mid')] + side_brow(64, 'mid', 4.0) +
  [L(blob([(74, 70), (88, 70), (88, 82), (74, 82)], 3) + [(74, 70)], GLRED, 'f', False, False, 2.2), L([(74, 74), (48, 70)], GLRED, 'f', False, False, 2.0)],
  [L(blob([(10, 70), (6, 30), (18, 8), (40, -6), (62, -2), (80, 6), (94, 24), (92, 70), (50, 78)], 8), 'mid'),
   L(blob([(58, 0), (82, 8), (94, 28), (90, 66), (66, 74)], 6), 'shade', 'b', False)])

# Marvin Reading (portero): pinchos gris verdoso echados hacia arriba y a la derecha, una cinta roja con una franja amarilla en
# la frente; ojos redondos de enfado y boca recta
HBR, HBY = _c('#c81a10'), _c('#e8a030')
C('marvin-reading', 'normal', P('#5c766a', '#f6ba7d', iris='#20181a'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=95, hairline=[(8, 62), (16, 58), (84, 58), (92, 62)]),
  [L(outline([(12, 56), (8, 36), (2, 18, 1), (18, 24), (20, 4, 1), (34, 18), (44, -4, 1), (54, 16), (68, -6, 1), (70, 14), (94, 2, 1), (86, 26), (104, 30, 1), (88, 40),
              (88, 56)]), 'mid'),
   L(outline([(60, 4), (68, -4), (70, 14), (92, 4), (86, 28), (100, 30), (88, 40), (86, 54), (74, 30)]), 'shade', 'b', False),
   L(blob([(10, 46), (50, 42), (90, 46), (90, 60), (50, 56), (10, 60)], 4), HBR, 'f'),
   L(blob([(10, 50), (50, 46), (90, 50), (90, 55), (50, 51), (10, 55)], 4), HBY, 'f', False)],
  [L(outline([(16, 52), (6, 30), (0, 10, 1), (18, 18), (24, -2, 1), (38, 14), (52, -8, 1), (60, 12), (84, 0, 1), (80, 22), (98, 28, 1), (82, 40), (60, 44), (40, 48)]), 'mid'),
   L(blob([(6, 46), (86, 40), (88, 54), (8, 60)], 4), HBR, 'f'), L(blob([(6, 50), (86, 44), (87, 49), (7, 55)], 4), HBY, 'f', False)],
  [L(outline([(12, 70), (8, 36), (2, 18, 1), (18, 24), (20, 4, 1), (34, 18), (44, -4, 1), (54, 16), (68, -6, 1), (70, 14), (94, 2, 1), (86, 26), (104, 30, 1), (88, 40),
              (88, 70), (50, 76)]), 'mid'),
   L(blob([(10, 46), (50, 50), (90, 46), (90, 60), (50, 64), (10, 60)], 4), HBR, 'f'),
   L(blob([(10, 50), (50, 54), (90, 50), (90, 55), (50, 59), (10, 55)], 4), HBY, 'f', False)])


# -------------------------------------------------------------------------------------------------------------- 25-32

# Mary Antoine: pelo naranja con raya en medio que cae en dos tirabuzones gruesos a los lados, coronado con una corona dorada;
# ojos cerrados de risa con pestañas y sonrisa
CROWN = _c('#f0d040')
def _drills(view):
    out = []
    xs = (-1, 1) if view != 'side' else (-1,)
    for s in xs:
        cx = 50 + s * 38 if view != 'side' else 30
        for i, cy in enumerate((66, 80, 94)):
            r = 9 - i * 1.2
            out.append(L(ell(cx + s * 2 * i, cy, r + 1, 7.5), 'mid'))
            out.append(strand(quad((cx - r, cy), (cx, cy + 4), (cx + r, cy)), 'deep', 'b', 1.0))
    return out
def _crown(y=10, x0=34, x1=66):
    n = 4
    pts = [(x0, y + 6)]
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        pts += [(x, y - 6, 1)] + ([(x + (x1 - x0) / n / 2, y)] if i < n else [])
    pts += [(x1, y + 6)]
    return L(outline(pts), CROWN, 'f')
C('mary-antoine', 'chica', P('#f78f3c', '#fdeab8'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=93, hairline=[(8, 62), (18, 50), (34, 40), (50, 36), (66, 40), (82, 50), (92, 62)]),
  _drills('front') + crop('front', top=4, side=66) + [strand([(50, 6), (50, 36)], 'deep', 'b', 1.2), _crown()] + squint(76, 14, 6.5, True),
  _drills('side') + crop('side', top=4, nape=80) + [L(outline([(40, 12), (36, -2, 1), (46, 6), (52, -4, 1), (56, 8)]), CROWN, 'f')],
  _drills('back') + crop('back', top=4, nape=82) + [_crown(8)])

# Mary Cramer: media melena morada en casco con un flequillo espeso que le tapa los ojos, dos coletitas con bolas rojas arriba;
# cara ancha con mofletes naranjas, nariz pequeña y boca de pena
REDB = _c('#d04050')
C('mary-cramer', 'chica', P('#84708c', '#fabb7a'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=97, hairline=False, face_front=face(w=4, chin=104, jaw=2), nose=(50, 86, 2.4)),
  bowl('front', top=6, side=92, w=4) +
  [fr([(12, 64), (14, 40), (30, 18), (50, 12), (70, 18), (86, 40), (88, 64), (80, 80), (50, 82), (20, 80)]),
   strand([(30, 30), (28, 76)], 'deep', 'f', 1.0), strand([(50, 20), (50, 78)], 'deep', 'f', 1.0), strand([(70, 30), (72, 76)], 'deep', 'f', 1.0),
   L(ell(24, 14, 4.4, 4.4), REDB, 'f'), L(ell(76, 14, 4.4, 4.4), REDB, 'f'),
   L(ell(26, 88, 6, 4), ORANGE_CHEEK, 'f', False), L(ell(74, 88, 6, 4), ORANGE_CHEEK, 'f', False)],
  bowl('side', top=6, nape=96, w=4) + [fr([(66, 14), (92, 36), (94, 82), (82, 82), (76, 50)]), L(ell(44, 8, 4.4, 4.4), REDB, 'f')],
  bowl('back', top=6, nape=96, w=4) + [L(ell(24, 14, 4.4, 4.4), REDB, 'f'), L(ell(76, 14, 4.4, 4.4), REDB, 'f')])

# Mary Hugland (portera): pelo verde oliva oscuro con raya en medio, estirado hacia atrás en una coleta baja; cara ancha, cejas
# finas arqueadas de enfado con pestañas, ojos pequeños y la boca abierta gritando
C('mary-hugland', 'corpulento', P('#605926', '#fdeab7', iris='#3a3020'),
  F(eyes='dot', brows='angry', mouth='none', hairline=[(8, 58), (20, 44), (36, 38), (50, 34), (64, 38), (80, 44), (92, 58)],
    face_front=blob([(14, 50), (50, 32), (86, 50), (92, 76), (84, 98), (64, 108), (50, 110), (36, 108), (16, 98), (8, 76)]), nose=(50, 85, 2.4)),
  crop('front', top=2, side=60) + [strand([(50, 4), (50, 34)], 'deep', 'b', 1.2),
                                   L(blob([(42, 92), (50, 88), (58, 92), (56, 104), (44, 104)], 6), (190, 60, 50, 255), 'f', True, True),
                                   L(blob([(44, 92), (56, 92), (54, 96), (46, 96)], 4), WHITE, 'f', False)],
  crop('side', top=2, nape=80) + [L(blob([(14, 76), (24, 74), (26, 96), (18, 104), (10, 94)], 6), 'mid')],
  crop('back', top=2, nape=80) + [L(blob([(42, 78), (58, 78), (56, 100), (50, 108), (44, 100)], 6), 'mid'), strand([(50, 6), (50, 76)], 'deep', 'b', 1.0)])

# Mason Tirell: casco amarillo alto en punta con una uve naranja y pinchos hacia los lados arriba y abajo; gafas de sol
# redondas negras, nariz larga, cara alargada y sonrisa ancha
HY, HO = _c('#f1d909'), _c('#e2863d')
def _tirell(view):
    if view == 'front':
        return [L(outline([(18, 76), (16, 50), (0, 46, 1), (16, 40), (18, 12), (-14, 6, 1), (20, 0), (34, -10), (50, -14), (66, -10), (80, 0), (114, 6, 1), (82, 12),
                           (84, 40), (100, 46, 1), (84, 50), (82, 76), (70, 66), (30, 66)]), HY, 'f'),
                L(outline([(36, -10), (50, 40, 1), (64, -10), (56, -12), (50, 16), (44, -12)]), HO, 'f', False),
                L(outline([(66, -8), (82, 2), (84, 46), (80, 68), (74, 40)]), tuple(int(v * 0.86) for v in HY[:3]) + (255,), 'f', False)]
    if view == 'side':
        return [L(outline([(24, 78), (14, 50), (0, 44, 1), (16, 40), (10, 12), (-14, 10, 1), (18, 0), (40, -12), (66, -10), (84, 2), (110, 6, 1), (88, 14), (92, 40),
                           (104, 46, 1), (90, 52), (90, 66), (70, 60), (50, 66)]), HY, 'f'),
                L(outline([(70, -8), (84, 4), (88, 40), (80, 30)]), HO, 'f', False)]
    return [L(outline([(16, 84), (14, 50), (0, 46, 1), (16, 40), (18, 12), (-14, 6, 1), (20, 0), (34, -10), (50, -14), (66, -10), (80, 0), (114, 6, 1), (82, 12),
                       (84, 40), (100, 46, 1), (84, 50), (84, 84), (50, 90)]), HY, 'f'),
            L(outline([(56, -12), (80, 0), (84, 50), (82, 84), (64, 88)]), tuple(int(v * 0.86) for v in HY[:3]) + (255,), 'f', False)]
SHADE_G = _c('#2a3a2a')
C('mason-tirell', 'delgado', P('#f1d909', '#fcc270'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, face_front=face(chin=112, jaw=-2), face_side=face_side(chin=10, nose=4)),
  _tirell('front') + [L(ell(36, 74, 7.4, 7), SHADE_G, 'f', True), L(ell(64, 74, 7.4, 7), SHADE_G, 'f', True), L([(42, 73), (58, 73)], OUTC, 'f', False, False, 2.0),
                      L(quad((50, 74), (44, 92), (52, 94)), OUTC, 'f', False, False, 1.4), L(quad((36, 100), (50, 104), (64, 100)), OUTC, 'f', False, False, 1.6)],
  _tirell('side') + [L(ell(84, 74, 5, 6.6), SHADE_G, 'f', True), L([(80, 72), (56, 66)], OUTC, 'f', False, False, 1.8)],
  _tirell('back'))

# Mat Halled: pelo blanco plateado en pinchos largos recogidos en una coleta alta que sale disparada hacia la derecha, con un
# pañuelo azul marino atado en la frente hasta las cejas; piel morena, ojos rojos afilados y boca recta
NAVYB = _c('#2a496e')
C('mat-halled', 'normal', P('#d2d6d0', '#cd976a', iris='#a01818'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=95, hairline=False),
  [L(outline([(12, 76), (6, 54), (10, 30), (26, 14), (40, 6), (54, 4), (62, -6), (100, -10, 1), (80, 4), (106, 14, 1), (84, 18), (100, 36, 1), (88, 44), (92, 70),
              (84, 84, 1), (82, 60), (18, 60), (16, 80, 1)]), 'mid'),
   L(outline([(62, 0), (96, -8), (80, 6), (102, 16), (84, 22), (96, 36), (86, 40), (74, 20)]), 'shade', 'b', False),
   L(ell(58, 2, 3.4, 3.4), _c('#c03020'), 'b'),
   L(blob([(12, 46), (30, 32), (50, 30), (70, 32), (88, 46), (88, 66), (50, 62), (12, 66)], 6), NAVYB, 'f')],
  [L(outline([(60, 54), (16, 66), (4, 44), (10, 20), (30, 6), (44, -4), (80, -10, 1), (62, 6), (90, 10, 1), (66, 20), (80, 44), (70, 50)]), 'mid'),
   L(blob([(14, 44), (40, 30), (70, 34), (90, 46), (90, 66), (60, 64), (16, 62)], 6), NAVYB, 'f')],
  [L(outline([(12, 80), (6, 54), (10, 30), (26, 14), (40, 6), (54, 4), (62, -6), (100, -10, 1), (80, 4), (106, 14, 1), (84, 18), (100, 36, 1), (88, 44), (92, 76),
              (78, 90, 1), (64, 80), (50, 92, 1), (36, 80), (22, 90, 1)]), 'mid'),
   L(blob([(10, 46), (50, 40), (90, 46), (90, 64), (50, 60), (10, 64)], 6), NAVYB, 'f'), L(ell(58, 2, 3.4, 3.4), _c('#c03020'), 'b')])

# Max Motto: casco verde con una cresta dorada en el centro y orejeras de rayas blancas, y unas gafas redondas amarillas por
# las que se le ven los ojos entornados; boca con labios
HGRN, HGLD, EARW = _c('#358e71'), _c('#d7a51d'), _c('#e8dcd0')
def _motto(view):
    if view == 'front':
        return [L(ell(8, 74, 8, 12), EARW, 'f'), L(ell(92, 74, 8, 12), EARW, 'f'),
                L(outline([(14, 86), (10, 50), (16, 22), (32, 6), (50, 2), (68, 6), (84, 22), (90, 50), (86, 86), (70, 80), (60, 84), (40, 84), (30, 80)]), HGRN, 'f'),
                L(outline([(40, 4), (50, -6), (60, 4), (58, 40), (50, 50, 1), (42, 40)]), HGLD, 'f'),
                L(outline([(66, 6), (84, 24), (90, 52), (86, 82), (74, 40)]), tuple(int(v * 0.8) for v in HGRN[:3]) + (255,), 'f', False),
                L(ell(34, 74, 10, 10), HGLD, 'f'), L(ell(66, 74, 10, 10), HGLD, 'f'),
                L(ell(34, 74, 7.6, 7.6), _c('#f4e030'), 'f', False), L(ell(66, 74, 7.6, 7.6), _c('#f4e030'), 'f', False),
                L([(28, 72), (40, 72)], OUTC, 'f', False, False, 2.0), L([(60, 72), (72, 72)], OUTC, 'f', False, False, 2.0),
                L(ell(34, 75, 1.8, 1.8), BLACK, 'f', False), L(ell(66, 75, 1.8, 1.8), BLACK, 'f', False)]
    if view == 'side':
        return [L(outline([(24, 84), (8, 56), (10, 26), (32, 6), (58, 0), (80, 10), (92, 32), (94, 60), (90, 84), (76, 80), (60, 66), (44, 80)]), HGRN, 'f'),
                L(outline([(30, 6), (50, -6), (74, 4), (70, 14), (50, 6)]), HGLD, 'f'), L(ell(44, 72, 8, 11), EARW, 'f'),
                L(ell(84, 74, 6, 9), HGLD, 'f'), L(ell(85, 74, 4, 6.6), _c('#f4e030'), 'f', False), L([(82, 72), (88, 72)], OUTC, 'f', False, False, 1.8)]
    return [L(ell(8, 74, 8, 12), EARW, 'f'), L(ell(92, 74, 8, 12), EARW, 'f'),
            L(outline([(12, 90), (8, 50), (16, 22), (32, 6), (50, 2), (68, 6), (84, 22), (92, 50), (88, 90), (50, 96)]), HGRN, 'f'),
            L(outline([(42, 4), (50, -6), (58, 4), (56, 60), (44, 60)]), HGLD, 'f')]
C('max-motto', 'normal', P('#358e71', '#efbf95'),
  F(eyes='none', brows=False, mouth='lips', mouth_y=95, mouth_w=8, hairline=False, ears=False),
  _motto('front'), _motto('side'), _motto('back'))

# May Apple: sombrero verde con forma de manzana y su rabito encima; pelo rubio muy claro en mechones que caen por los lados,
# orejas puntiagudas, ojos castaños grandes, mofletes naranjas y sonrisa
APPLE = _c('#a9c044')
def _apple(view):
    if view == 'side':
        return [L(blob([(12, 50), (4, 24), (24, 2), (54, -2), (82, 6), (94, 30), (90, 50), (50, 46)], 8), APPLE, 'f'),
                L(quad((50, 0), (52, -10), (60, -14)), _c('#8a7a40'), 'f', False, False, 3.0)]
    return [L(blob([(8, 54), (4, 26), (22, 4), (42, 0), (50, 6), (58, 0), (78, 4), (96, 26), (92, 54), (50, 50)], 8), APPLE, 'f'),
            L(blob([(64, 4), (86, 14), (94, 40), (84, 52), (78, 26)], 6), tuple(int(v * 0.82) for v in APPLE[:3]) + (255,), 'f', False),
            L(quad((50, 4), (50, -8), (58, -14)), _c('#8a7a40'), 'f', False, False, 3.0)]
C('may-apple', 'chica', P('#f0e8b0', '#f3c194', iris='#8a6030'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=False, ears=False),
  [L(outline([(14, 70), (-4, 62, 1), (12, 80)]), 'skin', 'f', True, True), L(outline([(86, 70), (104, 62, 1), (88, 80)]), 'skin', 'f', True, True),
   L(outline([(10, 52), (12, 84), (20, 92, 1), (22, 66), (78, 66), (80, 92, 1), (88, 84), (90, 52)]), 'mid')] + _apple('front') +
  [fr([(16, 52), (30, 50), (40, 64), (36, 70, 1), (30, 60), (22, 70, 1)]), fr([(84, 52), (70, 50), (60, 64), (64, 70, 1), (70, 60), (78, 70, 1)]),
   L(ell(26, 88, 5, 4.4), ORANGE_CHEEK, 'f', False), L(ell(74, 88, 5, 4.4), ORANGE_CHEEK, 'f', False)],
  [L(outline([(10, 50), (6, 80), (20, 88), (40, 82), (54, 60), (40, 50)]), 'mid')] + _apple('side') + [L(outline([(46, 70), (32, 60, 1), (50, 76)]), 'skin', 'f', True, True)],
  [L(outline([(10, 50), (12, 86), (30, 92, 1), (50, 84), (70, 92, 1), (88, 86), (90, 50)]), 'mid')] + _apple('back'))

# Mia Pitchford: pelo morado ciruela en media melena desgreñada que se abre en puntas a los lados a la altura de la barbilla,
# flequillo de mechones; ojos verdes afilados, colorete y boca fruncida
C('mia-pitchford', 'chica', P('#6e3060', '#fac173', iris='#3a9a60'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=hl(5, 66, 50, 60, x0=16, x1=84, lean=-2, jit=2, seed=5)),
  dome('front', top=0, w=48, cy=46, n=9, amp=6, seed=9, long=96, flare=10, soft=False) + blush(86, (240, 140, 120, 255), 22, 4.0),
  dome('side', top=0, w=48, cy=46, n=9, amp=6, seed=9, long=96, flare=10, fr=50),
  dome('back', top=0, w=48, cy=46, n=9, amp=6, seed=9, long=96, flare=10, ends=4))


# -------------------------------------------------------------------------------------------------------------- 33-40

# Michael Gibe: pelo castaño dorado peinado hacia atrás en surcos, con dos coletitas finas y tiesas que salen de la nuca hacia
# abajo; orejas grandes en punta, piel tostada, ojos entornados de pillo y boca ancha recta
C('michael-gibe', 'normal', P('#a88141', '#ce9669', iris='#20181a'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=95, mouth_w=12, big_ears=3, ear_out=3, hairline=[(8, 56), (18, 46), (34, 40), (50, 38), (66, 40), (82, 46), (92, 56)]),
  crop('front', top=-2, side=56, w=4) + [strand([(30, 4), (32, 40)], 'deep', 'b', 1.4), strand([(44, -1), (44, 38)], 'deep', 'b', 1.4),
                                         strand([(58, -1), (58, 38)], 'deep', 'b', 1.4), strand([(72, 6), (70, 40)], 'deep', 'b', 1.4),
                                         L([(18, 92), (10, 108)], 'deep', 'b', False, False, 3.4), L([(82, 92), (90, 108)], 'deep', 'b', False, False, 3.4),
                                         L([(38, 95), (62, 95)], OUTC, 'f', False, False, 1.4)],
  crop('side', top=-2, nape=80, w=4) + [strand([(30, 4), (10, 40)], 'deep', 'b', 1.4), strand([(54, 0), (28, 50)], 'deep', 'b', 1.4),
                                        L([(24, 80), (16, 104)], 'deep', 'b', False, False, 3.4)],
  crop('back', top=-2, nape=80, w=4) + [strand([(34, 6), (36, 76)], 'deep', 'b', 1.4), strand([(50, 4), (50, 78)], 'deep', 'b', 1.4),
                                        strand([(66, 6), (64, 76)], 'deep', 'b', 1.4), L([(40, 80), (34, 104)], 'deep', 'b', False, False, 3.4),
                                        L([(60, 80), (66, 104)], 'deep', 'b', False, False, 3.4)])

# Milly Vacey: melena castaña ondulada hasta los hombros con un flequillo largo que le tapa el ojo derecho de la imagen y un
# hibisco rojo prendido arriba; piel morena, ojo azul verdoso, pendiente y sonrisa de dientes
HIB = _c('#e02830')
def _hibiscus(x, y):
    pts = []
    import math
    for i in range(10):
        a = math.pi * 2 * i / 10
        r = 11 if i % 2 == 0 else 6
        pts.append((x + r * math.cos(a), y + r * math.sin(a)))
    return [L(blob(pts, 4), HIB, 'f'), L(ell(x, y, 2, 2), _c('#f4d040'), 'f', False)]
C('milly-vacey', 'chica', P('#816654', '#cc9c6d', iris='#30a0a0'),
  F(eyes='big', brows='angry', mouth='grin', mouth_y=95, hairline=False),
  dome('front', top=2, w=48, cy=46, long=96, flare=10, n=0) +
  [fr([(46, 18), (64, 12), (82, 22), (90, 46), (88, 70), (84, 92, 1), (76, 76), (60, 70), (54, 50), (44, 40)]),
   L(ell(16, 84, 1.6, 1.6), WHITE, 'f', True)] + _hibiscus(20, 18),
  dome('side', top=2, w=48, cy=46, long=96, flare=10, fr=52) + [fr([(66, 16), (90, 30), (94, 56), (90, 80, 1), (82, 60), (74, 44)])],
  dome('back', top=2, w=48, cy=46, long=96, flare=10, ends=5) + _hibiscus(80, 18))

# Minnie Stratio (portera): pelo azul petróleo con flequillo de mechones largos a los lados de la cara y dos trenzas que le
# caen por delante hasta el pecho; gafas redondas rojas, ojos verdes grandes y boca recta
GLR = _c('#d02828')
C('minnie-stratio', 'chica', P('#34647d', '#fcd9b6', iris='#5a9a30'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=94, hairline=[(8, 66), (16, 50), (30, 46), (40, 56), (50, 44), (62, 54), (72, 46), (84, 50), (92, 66)]),
  dome('front', top=2, w=48, cy=46, sb=80) +
  [fr([(14, 60), (12, 92, 1), (20, 70)]), fr([(86, 60), (88, 92, 1), (80, 70)]),
   L(rope((18, 86), (14, 104), (18, 120), 6), 'mid', 'f'), L(rope((82, 86), (86, 104), (82, 120), 6), 'mid', 'f')] + round_specs('front', GLR, 77, 14, 9.5, 8, 2.2),
  dome('side', top=2, w=48, cy=46, nape=88, fr=52) + [L(rope((60, 84), (68, 104), (70, 120), 6), 'mid', 'f')] + round_specs('side', GLR, 77),
  dome('back', top=2, w=48, cy=46, nape=88))

# Mitch Blackston: pelo gris oscuro en pinchos como una corona; cara pálida de muñeco con una cicatriz cosida en diagonal,
# marcas rojas alrededor de los ojos, ojos negros enormes y redondos, un triángulo morado en la frente y sonrisa de dientes;
# orejas puntiagudas
SCAR, TRI = _c('#a02020'), _c('#7a5a9a')
C('mitch-blackston', 'normal', P('#464653', '#e2ccae'),
  F(eyes='none', brows=False, mouth='none', hairline=[(8, 50), (20, 44), (50, 42), (80, 44), (92, 50)], ears=False),
  [L(outline([(12, 70), (-4, 60, 1), (14, 62)]), 'skin', 'f', True, True), L(outline([(88, 70), (104, 60, 1), (86, 62)]), 'skin', 'f', True, True),
   L(outline([(14, 54), (12, 30), (10, 8, 1), (24, 20), (34, -6, 1), (44, 14), (56, -6, 1), (64, 14), (78, -4, 1), (80, 18), (92, 6, 1), (88, 32), (86, 54), (50, 46)]), 'mid'),
   L(quad((18, 70), (30, 62), (30, 86)), SCAR, 'f', False, False, 3.0), L(quad((82, 70), (70, 62), (70, 86)), SCAR, 'f', False, False, 3.0),
   L(ell(36, 74, 7.6, 8.4), WHITE, 'f', True, True), L(ell(36, 74, 5.4, 6.2), BLACK, 'f', False),
   L(ell(64, 74, 7.6, 8.4), WHITE, 'f', True, True), L(ell(64, 74, 5.4, 6.2), BLACK, 'f', False),
   L([(50, 52), (55, 60), (45, 60)], TRI, 'f', False, True),
   L([(24, 96), (40, 88), (56, 82), (72, 76)], OUTC, 'f', False, False, 1.2),
   *[L([(x, y - 3), (x + 2, y + 3)], OUTC, 'f', False, False, 1.0) for x, y in ((32, 92), (44, 86), (56, 81), (66, 78))],
   L(blob([(38, 96), (62, 96), (58, 101), (42, 101)], 4), WHITE, 'f', True, True)],
  [L(outline([(18, 54), (8, 30), (6, 8, 1), (22, 14), (32, -6, 1), (44, 10), (58, -6, 1), (64, 12), (82, 0, 1), (80, 20), (90, 30), (80, 40), (50, 42)]), 'mid'),
   L(outline([(52, 70), (38, 60, 1), (54, 76)]), 'skin', 'f', True, True), L(ell(82, 74, 5, 8), WHITE, 'f', True, True), L(ell(83, 74, 3.4, 6), BLACK, 'f', False)],
  [L(outline([(14, 64), (12, 30), (10, 8, 1), (24, 20), (34, -6, 1), (44, 14), (56, -6, 1), (64, 14), (78, -4, 1), (80, 18), (92, 6, 1), (88, 32), (86, 64), (50, 70)]), 'mid'),
   L(outline([(12, 70), (-4, 60, 1), (14, 62)]), 'skin', 'f', True, True), L(outline([(88, 70), (104, 60, 1), (86, 62)]), 'skin', 'f', True, True)])

# Nancy Pickney: señora mayor de pelo gris azulado estirado hacia arriba en un moño alto; orejas grandes, ojos entornados con
# sombra rosa en los párpados, nariz pequeña y boca de disgusto
EYESH = _c('#e0a0b0')
C('nancy-pickney', 'chica', P('#96a7b6', '#fabc7c', iris='#3a3020'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=95, big_ears=3, ear_out=2, nose=(50, 85, 2.2),
    hairline=[(8, 58), (20, 46), (36, 40), (50, 38), (64, 40), (80, 46), (92, 58)]),
  crop('front', top=4, side=56) + [L(ell(50, 0, 13, 12), 'mid'), strand(quad((40, -2), (50, -8), (60, -2)), 'deep', 'b', 1.2),
                                   strand([(36, 14), (44, 36)], 'deep', 'b', 1.0), strand([(64, 14), (56, 36)], 'deep', 'b', 1.0),
                                   L(blob([(26, 69), (44, 70), (44, 72), (26, 72)], 3), EYESH, 'f', False), L(blob([(56, 70), (74, 69), (74, 72), (56, 72)], 3), EYESH, 'f', False)],
  crop('side', top=4, nape=80) + [L(ell(40, 0, 12, 12), 'mid')],
  crop('back', top=4, nape=80) + [L(ell(50, 0, 13, 12), 'mid'), strand([(50, 12), (50, 76)], 'deep', 'b', 1.0)])

# Nancy Polearm: pelo azul marino en casco redondeado con un flequillo de puntas que le cae sobre la cara y dos lazos negros a
# los lados de la nuca; ojos afilados con sombra morada y los dientes apretados
BOW = _c('#1e1c22')
C('nancy-polearm', 'chica', P('#3d4163', '#fac274', iris='#2a2028'),
  F(eyes='sharp', brows=False, mouth='grin', mouth_y=96, hairline=False),
  bowl('front', top=0, side=84) +
  [fr([(14, 66), (14, 40), (28, 20), (50, 14), (72, 20), (86, 40), (86, 66), (78, 54), (70, 72, 1), (64, 54), (54, 80, 1), (48, 56), (36, 74, 1), (32, 54), (24, 70, 1), (20, 54)]),
   L(blob([(4, 88), (16, 82), (20, 92), (10, 100)], 4), BOW, 'f'), L(blob([(96, 88), (84, 82), (80, 92), (90, 100)], 4), BOW, 'f'),
   L(blob([(26, 68), (44, 71), (44, 73), (26, 71)], 3), _c('#a080c0'), 'f', False), L(blob([(56, 71), (74, 68), (74, 71), (56, 73)], 3), _c('#a080c0'), 'f', False)],
  bowl('side', top=0, nape=92) + [fr([(66, 16), (90, 34), (92, 60), (86, 74, 1), (80, 54), (72, 40)]), L(blob([(20, 92), (34, 86), (36, 98), (24, 104)], 4), BOW, 'f')],
  bowl('back', top=0, nape=94) + [L(blob([(30, 92), (50, 88), (70, 92), (60, 100), (40, 100)], 4), BOW, 'f')])

# Nate Checker: pelo gris verdoso en pinchos largos echados hacia la izquierda de la imagen, con patillas largas que bajan por
# delante de las orejas; ojos azul grisáceo, rayitas en las mejillas y sonrisa
C('nate-checker', 'normal', P('#5b7174', '#f7bc7e', iris='#6070a0'),
  F(eyes='normal', brows='angry', mouth='smile', mouth_y=94, hairline=hl(5, 64, 48, 58, x0=16, x1=84, lean=-4, jit=2, seed=12)),
  dome('front', top=0, w=46, cy=44, n=6, amp=18, sweep=-0.9, seed=13, sb=86) + [fr([(14, 60), (14, 92, 1), (20, 66)]), fr([(86, 60), (86, 92, 1), (80, 66)]),
                                                                                *[L([(x, 88), (x + 3, 85)], (200, 110, 90, 255), 'f', False, False, 1.0) for x in (24, 28, 70, 74)]],
  dome('side', top=0, w=46, cy=44, n=6, amp=18, sweep=-0.9, seed=13, nape=86, fr=50),
  dome('back', top=0, w=46, cy=44, n=6, amp=18, sweep=-0.9, seed=13, nape=86))

# Neil Seating: corte de tazón rojo intenso, ancho y abombado como una seta, con un mechón levantado en la coronilla; piel
# tostada, ojos blancos redondos, rayitas en las mejillas y boca recta
C('neil-seating', 'normal', P('#9d0a0a', '#dda258', iris='#20181a'),
  F(eyes='round', brows=False, mouth='line', mouth_y=95, hairline=[(4, 64), (30, 63), (70, 63), (96, 64)]),
  [L(outline([(2, 64), (4, 40), (16, 16), (36, 4), (56, 6), (64, -6, 1), (70, 6), (84, 14), (96, 36), (98, 64), (80, 66), (50, 64), (20, 66)]), 'mid'),
   L(outline([(62, 6), (86, 16), (96, 40), (96, 62), (80, 60), (78, 34)]), 'shade', 'b', False),
   fr([(4, 64), (8, 56), (92, 56), (96, 64), (80, 66), (50, 64), (20, 66)]),
   *[L([(x, 88), (x + 3, 85)], (170, 90, 50, 255), 'f', False, False, 1.0) for x in (24, 28, 70, 74)]],
  [L(outline([(84, 60), (94, 44), (90, 16), (68, 2), (58, -8, 1), (52, 4), (28, 6), (8, 24), (0, 50), (4, 70), (40, 70), (70, 66)]), 'mid'),
   L(outline([(2, 50), (30, 56), (40, 68), (6, 68)]), 'shade', 'b', False)],
  [L(outline([(2, 70), (4, 40), (16, 16), (36, 4), (56, 6), (64, -6, 1), (70, 6), (84, 14), (96, 36), (98, 70), (50, 76)]), 'mid'),
   L(outline([(60, 6), (86, 16), (96, 40), (96, 68), (70, 74)]), 'shade', 'b', False)])


# -------------------------------------------------------------------------------------------------------------- 41-48

# Nelson Levene: gorro de pelo castaño a franjas onduladas más claras, calado hasta las cejas, del que caen mechones lisos y
# rectos por los lados hasta la mandíbula; cara alargada y pálida, nariz larga marcada, ojos entornados y boca de disgusto
STRIPE = _c('#a88030')
C('nelson-levene', 'delgado', P('#70501f', '#e6d2b7', iris='#3a3020'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=100, hairline=[(8, 64), (20, 62), (50, 62), (80, 62), (92, 64)],
    face_front=face(chin=112, jaw=-1), face_side=face_side(chin=10, nose=3)),
  [L(outline([(12, 60), (10, 36), (20, 12), (50, 0), (80, 12), (90, 36), (88, 60), (50, 64)]), 'mid'),
   L(quad((14, 30), (50, 18), (86, 30)), STRIPE, 'b', False, False, 4.0), L(quad((12, 46), (50, 36), (88, 46)), STRIPE, 'b', False, False, 4.0),
   L(outline([(12, 60), (10, 100), (16, 104, 1), (18, 66)]), 'mid', 'f'), L(outline([(88, 60), (90, 100), (84, 104, 1), (82, 66)]), 'mid', 'f'),
   L(quad((48, 68), (46, 84), (50, 90)), OUTC, 'f', False, False, 1.2), L(quad((52, 68), (54, 84), (50, 90)), OUTC, 'f', False, False, 1.0)],
  [L(outline([(70, 60), (88, 56), (86, 30), (66, 6), (40, 0), (16, 12), (6, 36), (8, 64), (20, 98), (32, 102), (34, 66), (50, 62)]), 'mid'),
   L(quad((10, 30), (40, 14), (82, 24)), STRIPE, 'b', False, False, 4.0), L(quad((8, 46), (40, 32), (86, 42)), STRIPE, 'b', False, False, 4.0)],
  [L(outline([(10, 64), (10, 36), (20, 12), (50, 0), (80, 12), (90, 36), (90, 64), (88, 100), (70, 102), (50, 104), (30, 102), (12, 100)]), 'mid'),
   L(quad((14, 30), (50, 18), (86, 30)), STRIPE, 'b', False, False, 4.0), L(quad((12, 46), (50, 36), (88, 46)), STRIPE, 'b', False, False, 4.0)])

# Nev Puffer: pelo azul petróleo con un mechón enorme en arco que se enrosca por encima de la cabeza, flequillo largo de puntas
# que le cae sobre la cara y mechones laterales hasta la barbilla; ojos morados afilados y boca recta
C('nev-puffer', 'normal', P('#2a5f70', '#f8bc7f', iris='#7a5aa0'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=False),
  dome('front', top=4, w=46, cy=46, sb=94, n=0) +
  [L(quad((50, 8), (10, -30), (-14, 10)), 'mid', 'b', True, False, 5.0),
   fr([(14, 76, 1), (14, 44), (30, 22), (50, 16), (70, 22), (86, 44), (86, 76, 1), (78, 56), (66, 76, 1), (60, 54), (50, 84, 1), (44, 56), (34, 72, 1), (28, 54), (22, 66)])],
  dome('side', top=4, w=46, cy=46, nape=90, fr=56) + [L(quad((50, 6), (20, -30), (-6, 8)), 'mid', 'b', True, False, 5.0),
                                                     fr([(66, 16), (90, 32), (94, 62), (88, 80, 1), (82, 58), (74, 40)])],
  dome('back', top=4, w=46, cy=46, nape=90) + [L(quad((50, 8), (90, -30), (114, 10)), 'mid', 'b', True, False, 5.0)])

# Nick Uman: grandullón de cara ancha y mandíbula enorme, piel morena; pelo castaño oscuro en pinchos que suben en pico hacia
# la coronilla y salen por los lados; orejas puntiagudas, ojos apretados de esfuerzo y una mueca de dientes
C('nick-uman', 'corpulento', P('#512105', '#ce9568'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=97, hairline=[(8, 50), (20, 46), (50, 44), (80, 46), (92, 50)], ears=False,
    face_front=blob([(14, 48), (50, 34), (86, 48), (94, 76), (90, 100), (70, 114), (50, 116), (30, 114), (10, 100), (6, 76)]), face_side=face_side(chin=10, jaw=6)),
  [L(outline([(10, 74), (-6, 66, 1), (12, 62)]), 'skin', 'f', True, True), L(outline([(90, 74), (106, 66, 1), (88, 62)]), 'skin', 'f', True, True),
   L(outline([(12, 60), (2, 52, 1), (12, 44), (4, 30, 1), (18, 28), (26, 10), (40, 0), (50, -16, 1), (60, 0), (74, 10), (82, 28), (96, 30, 1), (88, 44), (98, 52, 1),
              (88, 60), (80, 50), (20, 50)]), 'mid'),
   L(outline([(10, 72), (0, 84, 1), (8, 90), (2, 100, 1), (14, 96)]), 'mid', 'f'), L(outline([(90, 72), (100, 84, 1), (92, 90), (98, 100, 1), (86, 96)]), 'mid', 'f'),
   L([(26, 70), (40, 76), (28, 80)], OUTC, 'f', False, False, 2.2), L([(74, 70), (60, 76), (72, 80)], OUTC, 'f', False, False, 2.2),
   L([(24, 66), (42, 70)], OUTC, 'f', False, False, 2.6), L([(76, 66), (58, 70)], OUTC, 'f', False, False, 2.6),
   L(quad((46, 74), (44, 86), (52, 88)), OUTC, 'f', False, False, 1.0)],
  [L(outline([(16, 60), (4, 48, 1), (14, 40), (8, 24, 1), (24, 22), (38, 4), (50, -12, 1), (60, 2), (76, 12), (88, 30), (74, 46), (50, 50), (40, 76), (24, 74)]), 'mid'),
   L(outline([(52, 74), (40, 64, 1), (54, 64)]), 'skin', 'f', True, True), L([(74, 74), (84, 76)], OUTC, 'f', False, False, 2.2)],
  [L(outline([(10, 80), (2, 52, 1), (12, 44), (4, 30, 1), (18, 28), (26, 10), (40, 0), (50, -16, 1), (60, 0), (74, 10), (82, 28), (96, 30, 1), (88, 44), (98, 52, 1),
              (90, 80), (50, 86)]), 'mid'),
   L(outline([(10, 74), (-6, 66, 1), (12, 62)]), 'skin', 'f', True, True), L(outline([(90, 74), (106, 66, 1), (88, 62)]), 'skin', 'f', True, True)])

# Niki Colbeck: boina roja grande ladeada sobre una mata de pelo gris claro esponjoso que abulta a los lados; piel pálida,
# ojos azul verdoso afilados y la boca en O
BERET = _c('#a7232e')
def _niki(view):
    if view == 'front':
        return [L(blob([(14, 40), (-4, 50), (-8, 72), (8, 84), (22, 74)], 8), 'mid'), L(blob([(86, 40), (104, 50), (108, 72), (92, 84), (78, 74)], 8), 'mid'),
                L(blob([(2, 44), (10, 18), (40, 4), (70, 4), (88, 10), (96, 30), (90, 46), (50, 44), (12, 50)], 8), BERET),
                L(blob([(64, 6), (88, 12), (96, 30), (88, 44), (74, 30)], 6), tuple(int(v * 0.8) for v in BERET[:3]) + (255,), 'b', False),
                L(ell(80, 2, 4, 3.4), BERET)]
    if view == 'side':
        return [L(blob([(40, 40), (12, 44), (0, 66), (12, 84), (34, 76)], 8), 'mid'),
                L(blob([(4, 46), (8, 18), (36, 2), (70, 2), (92, 16), (96, 34), (60, 40)], 8), BERET)]
    return [L(blob([(6, 44), (-8, 66), (6, 86), (50, 90), (94, 86), (108, 66), (94, 44)], 8), 'mid'),
            L(blob([(4, 48), (10, 18), (40, 4), (70, 4), (90, 14), (96, 34), (92, 50), (50, 52)], 8), BERET)]
C('niki-colbeck', 'chica', P('#d8d4dc', '#ece7cf', iris='#3a8a9a'),
  F(eyes='sharp', brows=False, mouth='none', hairline=False),
  _niki('front') + [L(ell(50, 96, 3, 3.6), (120, 50, 40, 255), 'f', True, True)],
  _niki('side'), _niki('back'))

# Nina Trowel: corte de tazón lila muy espeso con el flequillo hasta la nariz, que le tapa los ojos del todo; labios gruesos
# pintados de azul oscuro
C('nina-trowel', 'chica', P('#cbb0c7', '#e4ceae'),
  F(eyes='none', brows=False, mouth='none', hairline=False),
  bowl('front', top=0, side=90, w=4) +
  [fr([(8, 70), (10, 40), (26, 14), (50, 4), (74, 14), (90, 40), (92, 70), (80, 86), (50, 88), (20, 86)]),
   *[strand([(x, 50), (x, 84)], 'shade', 'f', 1.0) for x in (24, 38, 52, 66, 80)],
   L(blob([(42, 98), (50, 96), (58, 98), (54, 104), (46, 104)], 6), _c('#2a3a50'), 'f', True, True)],
  bowl('side', top=0, nape=96, w=4) + [fr([(62, 10), (92, 34), (96, 86), (84, 88), (74, 50)])],
  bowl('back', top=0, nape=96, w=4))

# Nolene Ider: pelo naranja con flequillo de puntas y dos coletas cortas y erizadas a los lados, sujetas con gomas moradas;
# ojos turquesa grandes y boca pequeña
PURPLE = _c('#4a3a80')
def _nolene_tails(view):
    if view == 'side':
        return [L(outline([(26, 46), (8, 40), (-10, 30, 1), (0, 50), (-12, 62, 1), (4, 64), (-4, 80, 1), (14, 72), (24, 66)]), 'mid'), L(ell(26, 54, 3, 6), PURPLE, 'f')]
    out = []
    for s in (-1, 1):
        out.append(L(outline([(50 + s * 38, 44), (50 + s * 52, 36), (50 + s * 66, 30, 1), (50 + s * 58, 48), (50 + s * 70, 60, 1), (50 + s * 56, 62), (50 + s * 64, 80, 1),
                              (50 + s * 48, 70), (50 + s * 40, 64)]), 'mid'))
        out.append(L(ell(50 + s * 40, 52, 3, 7), PURPLE, 'f'))
    return out
C('nolene-ider', 'chica', P('#e26b05', '#fcecc1', iris='#30b0b0'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=94, hairline=hl(6, 64, 50, 60, x0=16, x1=84, jit=2, seed=17)),
  _nolene_tails('front') + crop('front', top=2, side=64, w=2) + [L(outline([(46, 4), (48, -10, 1), (54, 4)]), 'mid')],
  _nolene_tails('side') + crop('side', top=2, nape=80, w=2),
  _nolene_tails('back') + crop('back', top=2, nape=80, w=2))

# Odessa Ryder: gafas de aviador de cristales azules subidas en la frente sobre un pelo gris verdoso oscuro que se abre a los
# lados en dos alas de punta, con mechones finos por delante; ojos grandes redondos, una peca y sonrisa
C('odessa-ryder', 'chica', P('#526360', '#fac373', iris='#20181a'),
  F(eyes='round', brows=False, mouth='smile', mouth_y=94, hairline=[(8, 62), (16, 52), (30, 54), (40, 48), (50, 56), (60, 48), (70, 54), (84, 52), (92, 62)]),
  [L(outline([(18, 50), (-12, 36, 1), (2, 60), (14, 62)]), 'mid'), L(outline([(82, 50), (112, 36, 1), (98, 60), (86, 62)]), 'mid')] +
  crop('front', top=4, side=64, w=2) +
  [fr([(14, 60), (12, 90, 1), (20, 70)]), fr([(86, 60), (88, 90, 1), (80, 70)])] +
  [L(quad((6, 34), (50, 20), (94, 34)), _c('#3a3a40'), 'f', False, False, 4.0)] +
  [L(ell(36, 30, 10, 8), _c('#5a6a8a'), 'f'), L(ell(64, 30, 10, 8), _c('#5a6a8a'), 'f'),
   L(ell(36, 30, 7.4, 5.6), _c('#c8e0f0'), 'f', False), L(ell(64, 30, 7.4, 5.6), _c('#c8e0f0'), 'f', False),
   L(ell(70, 92, 1.2, 1.2), (160, 90, 60, 255), 'f', False)],
  [L(outline([(30, 50), (-2, 38, 1), (10, 60), (24, 64)]), 'mid')] + crop('side', top=4, nape=80, w=2) +
  [L(quad((8, 38), (40, 24), (86, 30)), _c('#3a3a40'), 'f', False, False, 4.0), L(ell(76, 30, 7, 7.6), _c('#5a6a8a'), 'f'), L(ell(78, 30, 4.4, 5), _c('#c8e0f0'), 'f', False)],
  [L(outline([(18, 50), (-12, 36, 1), (2, 60), (14, 62)]), 'mid'), L(outline([(82, 50), (112, 36, 1), (98, 60), (86, 62)]), 'mid')] + crop('back', top=4, nape=80, w=2) +
  [L(quad((6, 36), (50, 46), (94, 36)), _c('#3a3a40'), 'f', False, False, 4.0)])

# Odette Musetta (portera): melena larga morada grisácea, desgreñada y de puntas, con dos mechones que se enroscan hacia fuera
# arriba como cuernos y un flequillo que le tapa media cara; ojos entornados de iris morado, cejas tristes y boca de pena
C('odette-musetta', 'chica', P('#554c56', '#e5d4ba', iris='#8a5a9a'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=96, hairline=False, face_front=face(chin=106), face_side=face_side(chin=6)),
  [L(outline([(10, 106, 1), (4, 80), (8, 56), (4, 30), (-12, 20), (-6, 12, 1), (10, 18), (24, 4), (50, -4), (76, 4), (90, 18), (106, 12, 1), (112, 20), (96, 30), (92, 56),
              (96, 80), (90, 106, 1), (80, 90), (82, 64), (18, 64), (20, 90)]), 'mid'),
   L(outline([(60, 0), (86, 14), (94, 50), (92, 100), (84, 80), (78, 40)]), 'shade', 'b', False),
   fr([(14, 70), (16, 40), (30, 20), (50, 12), (66, 16), (60, 36), (52, 54), (46, 84, 1), (40, 60), (30, 66, 1), (24, 54)]),
   L([(58, 66), (70, 63)], OUTC, 'f', False, False, 1.6)],
  [L(outline([(70, 40), (84, 30), (80, 10), (58, -4), (30, -2), (10, 14), (-8, 8, 1), (2, 30), (2, 60), (-2, 90), (6, 108, 1), (20, 96), (30, 110, 1), (40, 92), (52, 70)]), 'mid'),
   fr([(66, 14), (90, 30), (92, 60), (86, 84, 1), (80, 58), (72, 40)])],
  [L(outline([(10, 108, 1), (4, 80), (8, 56), (4, 30), (-12, 20), (-6, 12, 1), (10, 18), (24, 4), (50, -4), (76, 4), (90, 18), (106, 12, 1), (112, 20), (96, 30), (92, 56),
              (96, 80), (90, 108, 1), (74, 96), (62, 110, 1), (50, 96), (38, 110, 1), (26, 96)]), 'mid'),
   L(outline([(56, -2), (86, 14), (94, 50), (92, 100), (64, 100)]), 'shade', 'b', False)])


# -------------------------------------------------------------------------------------------------------------- 49-56

# Ol Factory (portero): capucha verde de perro con orejas caídas y una máscara de cara de perro naranja con el hocico crema,
# la nariz rosa y los ojos de enfado; solo se le ven el cuello y la barbilla
HOOD, DOGM, MUZ, DNOSE = _c('#5d7756'), _c('#d8a060'), _c('#eeebd5'), _c('#c07878')
def _dog(view):
    if view == 'front':
        return [L(outline([(8, 76), (2, 54), (10, 30), (28, 10), (50, 6), (72, 10), (90, 30), (98, 54), (92, 76), (82, 58), (18, 58)]), HOOD, 'f'),
                L(outline([(10, 40), (-2, 70), (8, 86, 1), (18, 60)]), _c('#a2b69a'), 'f'), L(outline([(90, 40), (102, 70), (92, 86, 1), (82, 60)]), _c('#a2b69a'), 'f'),
                L(blob([(20, 50), (34, 34), (50, 30), (66, 34), (80, 50), (82, 80), (66, 96), (34, 96), (18, 80)], 8), DOGM, 'f'),
                L(blob([(24, 72), (50, 66), (76, 72), (74, 96), (50, 100), (26, 96)], 6), MUZ, 'f', False),
                L(ell(50, 74, 7, 4.4), DNOSE, 'f', True), L([(50, 78), (50, 86), (40, 92)], OUTC, 'f', False, False, 1.2), L([(50, 86), (60, 92)], OUTC, 'f', False, False, 1.2),
                L([(30, 52), (42, 58)], OUTC, 'f', False, False, 2.6), L([(70, 52), (58, 58)], OUTC, 'f', False, False, 2.6),
                L(ell(37, 60, 2.2, 2.2), BLACK, 'f', False), L(ell(63, 60, 2.2, 2.2), BLACK, 'f', False)]
    if view == 'side':
        return [L(outline([(20, 86), (4, 60), (8, 30), (30, 8), (58, 4), (80, 12), (92, 32), (96, 60), (90, 80), (60, 80), (40, 70)]), HOOD, 'f'),
                L(outline([(36, 40), (24, 70), (34, 88, 1), (44, 60)]), _c('#a2b69a'), 'f'),
                L(blob([(70, 36), (90, 40), (104, 64), (102, 86), (86, 96), (72, 90), (66, 60)], 8), DOGM, 'f'),
                L(blob([(84, 66), (104, 64), (104, 90), (88, 94)], 6), MUZ, 'f', False), L(ell(102, 70, 4, 4), DNOSE, 'f', True),
                L([(78, 52), (90, 56)], OUTC, 'f', False, False, 2.4)]
    return [L(outline([(8, 86), (4, 54), (10, 30), (28, 10), (50, 6), (72, 10), (90, 30), (96, 54), (92, 86), (50, 92)]), HOOD, 'f'),
            L(outline([(10, 40), (-2, 70), (8, 86, 1), (18, 60)]), _c('#a2b69a'), 'f'), L(outline([(90, 40), (102, 70), (92, 86, 1), (82, 60)]), _c('#a2b69a'), 'f')]
C('ol-factory', 'normal', P('#5d7756', '#d8a159'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _dog('front'), _dog('side'), _dog('back'))

# Olivia Baker: pelo verde azulado con dos coletas largas a los lados de la cabeza y un flequillo de mechones; ojos azules
# grandes y sonrisa abierta
def _twintails(view, y=24, length=110):
    if view == 'side':
        return [L(outline([(24, y), (8, y + 6), (2, y + 40), (6, length - 10), (14, length, 1), (18, y + 50), (28, y + 20)]), 'mid')]
    out = []
    for s in (-1, 1):
        out.append(L(outline([(50 + s * 36, y), (50 + s * 50, y - 2), (50 + s * 56, y + 20), (50 + s * 54, y + 50), (50 + s * 50, length, 1), (50 + s * 44, y + 56),
                              (50 + s * 42, y + 26)]), 'mid'))
        out.append(L(outline([(50 + s * 50, y + 4), (50 + s * 55, y + 24), (50 + s * 52, y + 56), (50 + s * 48, y + 30)]), 'shade', 'b', False))
    return out
C('olivia-baker', 'chica', P('#5f928f', '#f8bb7e', iris='#3080b0'),
  F(eyes='big', brows=False, mouth='grin', mouth_y=94, hairline=[(8, 66), (16, 52), (28, 58), (38, 48), (50, 56), (62, 48), (72, 58), (84, 52), (92, 66)]),
  _twintails('front') + dome('front', top=2, w=46, cy=46, sb=80) + [fr([(14, 62), (12, 90, 1), (20, 70)]), fr([(86, 62), (88, 90, 1), (80, 70)])],
  _twintails('side') + dome('side', top=2, w=46, cy=46, nape=86, fr=52),
  _twintails('back') + dome('back', top=2, w=46, cy=46, nape=86))

# Olivia Twist: pelo verde menta con raya en medio, media melena lisa y dos moños grandes en espiral arriba a los lados,
# atravesados por palillos marrones; ojos naranjas grandes y sonrisa suave
STICK = _c('#8a5a30')
def _buns(view):
    if view == 'side':
        return [L(ell(34, 12, 16, 15), 'mid', 'f', True, True), strand(quad((24, 14), (34, 2), (44, 14)), 'deep', 'f', 1.4), L([(14, 26), (52, 2)], STICK, 'f', False, False, 2.6)]
    out = []
    for s in (-1, 1):
        cx = 50 + s * 34
        out += [L(ell(cx + s * 4, 16, 16, 15), 'mid', 'f', True, True), strand(quad((cx + s * 4 - 10, 18), (cx + s * 4, 5), (cx + s * 4 + 10, 18)), 'deep', 'f', 1.4),
                L(ell(cx + s * 4, 16, 6.4, 5.8), 'shade', 'f', False), L([(cx - s * 2, 18), (cx + s * 26, 8)], STICK, 'f', False, False, 2.6)]
    return out
C('olivia-twist', 'chica', P('#85c9bb', '#fceab8', iris='#e07a20'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=[(8, 62), (18, 50), (34, 46), (50, 40), (66, 46), (82, 50), (92, 62)]),
  longhair('front', length=92, flare=4, top=6, ends=3) + [strand([(50, 8), (50, 40)], 'deep', 'b', 1.2)] + _buns('front'),
  longhair('side', length=92, flare=4, top=6) + _buns('side'),
  longhair('back', length=92, flare=4, top=6, ends=3) + _buns('back'))

# Ollie Tuckney: cabeza rapada con un mechón castaño malva echado a un lado en la coronilla, tiritas grises en la cabeza;
# orejas grandes, ojos entornados con raya morada, marcas moradas en las mejillas y sonrisa torcida
MAUVE, TAPE, PMARK = _c('#9a7064'), _c('#a09890'), _c('#6a4a9a')
C('ollie-tuckney', 'normal', P('#9a7064', '#fcc272', iris='#20181a'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=95, big_ears=3, ear_out=2, hairline=False),
  skull() + [L(outline([(52, 8), (60, 0), (78, 6), (88, 22), (90, 44), (82, 58), (74, 40), (66, 20)]), 'mid'),
             strand([(62, 6), (78, 30), (80, 50)], 'deep', 'b', 1.2), L(blob([(24, 20), (34, 14), (44, 34), (34, 40)], 4), TAPE, 'b', False),
             L(blob([(22, 66), (44, 68), (44, 72), (22, 70)], 3), PMARK, 'f', False), L(blob([(56, 68), (78, 66), (78, 70), (56, 72)], 3), PMARK, 'f', False),
             L(blob([(20, 84), (28, 82), (28, 90), (20, 90)], 3), PMARK, 'f', False), L(blob([(72, 82), (80, 84), (80, 90), (72, 90)], 3), PMARK, 'f', False)],
  [L(blob([(26, 30), (40, 10), (70, 4), (88, 18), (90, 40), (80, 40), (60, 20)], 6), 'mid'), L(blob([(30, 30), (40, 24), (46, 40)], 4), TAPE, 'b', False)],
  [L(blob([(50, 6), (70, 8), (84, 24), (80, 40), (60, 30)], 6), 'mid'), L(blob([(24, 20), (34, 14), (44, 34), (34, 40)], 4), TAPE, 'b', False)])

# Orpah Talkington: media melena castaña lisa con flequillo echado a un lado; ojos negros grandes, colorete y boca fruncida
C('orpah-talkington', 'chica', P('#a86920', '#fcc272', iris='#20181a'),
  F(eyes='big', brows='angry', mouth='frown', mouth_y=94, hairline=[(8, 66), (16, 52), (28, 46), (44, 50), (60, 54), (74, 60), (84, 64), (92, 70)]),
  longhair('front', length=96, flare=2, top=2, ends=3) + [fr([(14, 64), (16, 40), (30, 22), (50, 16), (70, 22), (84, 40), (88, 66, 1), (74, 54), (54, 48), (36, 52), (22, 64)])] +
  blush(86, (240, 140, 120, 255), 22, 3.6),
  longhair('side', length=96, flare=2, top=2),
  longhair('back', length=96, flare=2, top=2, ends=3))

# Osier Twining: capucha caqui con forma de calavera (agujeros de ojos y nariz), raída en los bordes, gafas redondas verdes
# de cristal oscuro, nariz pequeña, sonrisa y perilla castaña
SKH, GOG = _c('#b5b487'), _c('#3a4a20')
def _osier(view):
    if view == 'front':
        return [L(outline([(6, 90), (4, 70), (12, 40), (24, 14), (50, 2), (76, 14), (88, 40), (96, 70), (94, 90), (82, 84), (80, 70), (20, 70), (18, 84)]), SKH, 'f'),
                L(blob([(30, 26), (40, 24), (40, 34), (32, 36)], 4), BLACK, 'f', False), L(blob([(70, 26), (60, 24), (60, 34), (68, 36)], 4), BLACK, 'f', False),
                L([(46, 40), (50, 36), (54, 40)], BLACK, 'f', False, True),
                L(blob([(36, 56), (44, 52), (46, 62), (40, 64)], 4), BLACK, 'f', False), L(blob([(64, 56), (56, 52), (54, 62), (60, 64)], 4), BLACK, 'f', False)]
    if view == 'side':
        return [L(outline([(20, 96), (4, 70), (6, 36), (26, 10), (54, 2), (78, 12), (92, 36), (96, 70), (82, 70), (60, 76), (40, 90)]), SKH, 'f'),
                L(blob([(76, 26), (86, 26), (86, 34), (78, 36)], 4), BLACK, 'f', False)]
    return [L(outline([(6, 94), (4, 70), (12, 40), (24, 14), (50, 2), (76, 14), (88, 40), (96, 70), (94, 94), (78, 86), (64, 96), (50, 88), (36, 96), (22, 86)]), SKH, 'f')]
C('osier-twining', 'normal', P('#5a4a30', '#fcc372'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, hairline=False, ears=False, nose=(50, 86, 2.6)),
  _osier('front') + [L(ell(36, 76, 8.6, 8.6), GOG, 'f', True), L(ell(64, 76, 8.6, 8.6), GOG, 'f', True),
                     L(ell(36, 76, 5, 5), _c('#8a9a40'), 'f', False), L(ell(64, 76, 5, 5), _c('#8a9a40'), 'f', False),
                     L(blob([(40, 102), (50, 98), (60, 102), (50, 110)], 4), 'mid', 'f')],
  _osier('side') + [L(ell(84, 76, 5.4, 8), GOG, 'f', True), L(blob([(76, 102), (86, 100), (84, 108)], 4), 'mid', 'f')],
  _osier('back'))

# Ovie Whisker: cabeza calva y pálida con cuatro pelos de punta como granitos, orejas grandes con pendientes, un ojo cerrado y
# el otro entornado, papada, y una mueca torcida con un colmillo
C('ovie-whisker', 'corpulento', P('#4a4a5a', '#f6be91'),
  F(eyes='none', brows=False, mouth='none', hairline=False, big_ears=3, ear_out=3, face_front=face(chin=112, jaw=2), face_side=face_side(chin=10, jaw=4)),
  skull() + [*[L(ell(x, y, 1.6, 1.2), 'mid', 'b', False) for x, y in ((34, 12), (44, 8), (56, 8), (66, 12), (28, 20), (72, 20))],
             L(ell(12, 84, 2, 2), _c('#e0c030'), 'f', True), L(ell(88, 84, 2, 2), _c('#20b0b0'), 'f', True),
             L(quad((28, 74), (36, 70), (44, 74)), OUTC, 'f', False, False, 2.0), L(quad((56, 74), (64, 78), (72, 74)), OUTC, 'f', False, False, 2.0),
             L(quad((38, 98), (50, 92), (62, 100)), OUTC, 'f', False, False, 1.6), L([(58, 96), (60, 101), (62, 97)], WHITE, 'f', False, True),
             L(quad((42, 108), (50, 106), (58, 108)), OUTC, 'f', False, False, 1.0)],
  [*[L(ell(x, y, 1.6, 1.2), 'mid', 'f', False) for x, y in ((42, 24), (54, 22), (66, 26))], L([(76, 74), (84, 74)], OUTC, 'f', False, False, 2.0)],
  [*[L(ell(x, y, 1.6, 1.2), 'mid', 'f', False) for x, y in ((34, 30), (44, 25), (56, 25), (66, 30))]])

# Owen Rage: pelo naranja amarillento abombado como una nube; cara alargada y pálida con una nariz larga marcada, ojos blancos
# de rabia y una barba castaña enorme en bloque que le tapa la boca y la mandíbula
BEARD = _c('#87552a')
C('owen-rage', 'normal', P('#fdba45', '#e3cbae'),
  F(eyes='round', brows='angry', mouth='none', hairline=[(8, 56), (20, 52), (50, 50), (80, 52), (92, 56)], face_front=face(chin=108), face_side=face_side(chin=8, nose=3)),
  [L(blob([(4, 52), (0, 30), (14, 12), (32, 2), (50, 6), (68, 0), (86, 10), (100, 30), (96, 52), (80, 58), (60, 54), (40, 56), (20, 58)], 8), 'mid'),
   L(blob([(64, 4), (86, 12), (98, 32), (92, 50), (76, 40)], 6), 'shade', 'b', False),
   L(blob([(44, 70), (56, 70), (56, 86), (44, 86)], 3), 'skin_d', 'f', True, True),
   L(blob([(14, 92), (50, 88), (86, 92), (88, 108), (70, 116), (50, 118), (30, 116), (12, 108)], 6), BEARD, 'f'),
   L([(36, 102), (64, 102)], OUTC, 'f', False, False, 1.6)],
  [L(blob([(70, 50), (80, 30), (72, 8), (48, 0), (22, 6), (4, 26), (2, 50), (16, 66), (30, 60), (50, 56)], 8), 'mid'),
   L(blob([(56, 90), (90, 88), (94, 106), (80, 116), (60, 112)], 6), BEARD, 'f')],
  [L(blob([(4, 60), (0, 30), (14, 12), (32, 2), (50, 6), (68, 0), (86, 10), (100, 30), (96, 60), (70, 68), (50, 66), (30, 68)], 8), 'mid'),
   L(blob([(64, 4), (86, 12), (98, 32), (94, 58), (74, 62)], 6), 'shade', 'b', False)])


# -------------------------------------------------------------------------------------------------------------- 57-62

# Pace Keeping: pelo gris oliva desgreñado de media melena con mechones largos sobre la frente; gafas rectangulares finas de
# montura oscura, ojos azul claro y dientes apretados
C('pace-keeping', 'normal', P('#6b654d', '#fbc274', iris='#70a8c8'),
  F(eyes='normal', brows=False, mouth='grin', mouth_y=96, hairline=hl(5, 66, 50, 62, x0=16, x1=84, lean=-3, jit=3, seed=23)),
  dome('front', top=0, w=48, cy=46, n=10, amp=5, seed=24, sb=88) + [fr([(14, 60), (12, 90, 1), (20, 68)]), fr([(86, 60), (88, 90, 1), (80, 68)])] +
  [L(blob([(23, 70), (47, 70), (47, 82), (23, 82)], 3) + [(23, 70)], (40, 34, 30, 255), 'f', False, False, 1.8),
   L(blob([(53, 70), (77, 70), (77, 82), (53, 82)], 3) + [(53, 70)], (40, 34, 30, 255), 'f', False, False, 1.8), L([(47, 74), (53, 74)], (40, 34, 30, 255), 'f', False, False, 1.6)],
  dome('side', top=0, w=48, cy=46, n=10, amp=5, seed=24, nape=90, fr=54) +
  [L(blob([(74, 70), (88, 70), (88, 82), (74, 82)], 3) + [(74, 70)], (40, 34, 30, 255), 'f', False, False, 1.8), L([(74, 74), (50, 70)], (40, 34, 30, 255), 'f', False, False, 1.6)],
  dome('back', top=0, w=48, cy=46, n=10, amp=5, seed=24, nape=90))

# Pace Maker: pinchos castaño oscuro altísimos que salen hacia arriba y a los lados; gafas redondas verdes subidas sobre las
# cejas, ojos entornados con sombra morada, piel muy pálida, barbilla larga y sonrisa torcida
GGREEN = _c('#838755')
C('pace-maker', 'delgado', P('#563426', '#f9eabc', iris='#20181a'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=98, hairline=[(8, 60), (18, 54), (30, 58), (44, 52), (56, 58), (70, 52), (82, 56), (92, 60)],
    face_front=face(chin=108, jaw=-2), face_side=face_side(chin=8)),
  [L(outline([(14, 58), (-4, 30, 1), (14, 34), (8, -10, 1), (28, 18), (34, -22, 1), (46, 10), (56, -26, 1), (62, 8), (78, -18, 1), (78, 16), (102, -4, 1), (86, 30), (104, 32, 1),
              (86, 44), (86, 58), (80, 50), (20, 50)]), 'mid'),
   L(outline([(56, -20), (62, 8), (78, -12), (78, 16), (98, 0), (86, 30), (100, 32), (86, 42), (84, 56), (70, 30)]), 'shade', 'b', False),
   L(ell(36, 62, 8.4, 7.4), GGREEN, 'f'), L(ell(64, 62, 8.4, 7.4), GGREEN, 'f'),
   L(ell(36, 62, 4.6, 4.2), (40, 50, 30, 255), 'f', False), L(ell(64, 62, 4.6, 4.2), (40, 50, 30, 255), 'f', False),
   L([(8, 62), (28, 62)], GGREEN, 'f', False, False, 2.6), L([(72, 62), (92, 62)], GGREEN, 'f', False, False, 2.6), L([(44, 62), (56, 62)], GGREEN, 'f', False, False, 2.6),
   L(blob([(26, 74), (44, 76), (44, 78), (26, 77)], 3), _c('#a080c0'), 'f', False), L(blob([(56, 76), (74, 74), (74, 77), (56, 78)], 3), _c('#a080c0'), 'f', False)],
  [L(outline([(18, 54), (0, 30, 1), (14, 28), (6, 2, 1), (26, 14), (28, -18, 1), (44, 6), (56, -24, 1), (62, 4), (82, -12, 1), (78, 18), (100, 14, 1), (84, 34), (70, 46), (50, 50),
              (36, 64)]), 'mid'),
   L(ell(82, 62, 5.4, 7), GGREEN, 'f'), L(ell(84, 62, 3, 4.2), (40, 50, 30, 255), 'f', False), L([(76, 62), (40, 58)], GGREEN, 'f', False, False, 2.4)],
  [L(outline([(14, 66), (-4, 30, 1), (14, 34), (8, -10, 1), (28, 18), (34, -22, 1), (46, 10), (56, -26, 1), (62, 8), (78, -18, 1), (78, 16), (102, -4, 1), (86, 30), (104, 32, 1),
              (86, 44), (86, 66), (50, 72)]), 'mid'),
   L([(10, 62), (90, 62)], GGREEN, 'f', False, False, 2.6)])

# Pam Vision: media melena color salmón con flequillo recto y las puntas hacia fuera; ojos ámbar afilados, pecas y boca recta
C('pam-vision', 'chica', P('#ee8e67', '#fdc271', iris='#b07a20'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=[(8, 62), (16, 56), (24, 58), (76, 58), (84, 56), (92, 62)]),
  dome('front', top=2, w=46, cy=46, long=90, flare=10, n=0) +
  [fr([(16, 58), (18, 38), (34, 22), (50, 18), (66, 22), (82, 38), (84, 58), (70, 60), (50, 60), (30, 60)]),
   *[L(ell(x, y, 0.9, 0.9), (190, 100, 60, 255), 'f', False) for x, y in ((28, 86), (32, 88), (68, 88), (72, 86))]],
  dome('side', top=2, w=46, cy=46, long=90, flare=10, fr=56),
  dome('back', top=2, w=46, cy=46, long=90, flare=10, ends=4))

# Pat Lubow: afro de rizos mostaza abombado como una nube; cara alargada y pálida, ojos blancos de pupila pequeña, cejas
# de puntitos y boca recta
C('pat-lubow', 'normal', P('#bc9f10', '#f5be93', iris='#20181a'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=98, hairline=[(8, 58), (20, 52), (50, 54), (80, 52), (92, 58)], face_front=face(chin=108), face_side=face_side(chin=8)),
  dome('front', top=-4, w=50, cy=40, n=14, amp=6, soft=True, sb=62, seed=31) +
  [*[L(ell(x, 64, 0.9, 0.9), OUTC, 'f', False) for x in (30, 34, 38, 62, 66, 70)], L(quad((48, 80), (47, 88), (52, 89)), OUTC, 'f', False, False, 1.0)],
  dome('side', top=-4, w=50, cy=40, n=14, amp=6, soft=True, nape=82, fr=50, seed=31),
  dome('back', top=-4, w=50, cy=40, n=14, amp=6, soft=True, nape=84, seed=31))

# Patt Howell: capucha de animal amarillo ocre con orejas de punta y el borde claro; cara tostada con rayas oscuras como un
# antifaz, ojos entornados, una mascarilla crema con la nariz rosa sobre la boca y mechones oscuros por los lados
OCH, OCHL, MASK = _c('#b79c34'), _c('#f0e080'), _c('#ece4c8')
def _howell(view):
    if view == 'front':
        return [L(outline([(8, 104), (4, 70), (8, 40), (14, 16), (10, -8, 1), (26, 6), (50, 0), (74, 6), (90, -8, 1), (86, 16), (92, 40), (96, 70), (92, 104), (80, 100),
                           (82, 60), (18, 60), (20, 100)]), OCH, 'f'),
                L(quad((14, 60), (50, 48), (86, 60)), OCHL, 'f', False, False, 5.0),
                L(outline([(16, 64), (14, 100, 1), (22, 70)]), 'mid', 'f'), L(outline([(84, 64), (86, 100, 1), (78, 70)]), 'mid', 'f')]
    if view == 'side':
        return [L(outline([(20, 106), (4, 74), (6, 36), (20, 12), (24, -10, 1), (40, 4), (64, 2), (84, 14), (94, 38), (96, 62), (80, 58), (60, 60), (44, 70), (40, 100)]), OCH, 'f'),
                L(quad((94, 40), (82, 56), (60, 60)), OCHL, 'f', False, False, 4.0)]
    return [L(outline([(8, 106), (4, 70), (8, 40), (14, 16), (10, -8, 1), (26, 6), (50, 0), (74, 6), (90, -8, 1), (86, 16), (92, 40), (96, 70), (92, 106), (50, 112)]), OCH, 'f')]
C('patt-howell', 'normal', P('#3f3224', '#d9a45b', iris='#20181a'),
  F(eyes='sharp', brows=False, mouth='none', hairline=False, ears=False),
  _howell('front') +
  [L(blob([(22, 66), (40, 70), (44, 64), (30, 60)], 4), (90, 60, 30, 255), 'f', False), L(blob([(78, 66), (60, 70), (56, 64), (70, 60)], 4), (90, 60, 30, 255), 'f', False),
   L(blob([(24, 86), (50, 82), (76, 86), (74, 100), (50, 106), (26, 100)], 6), MASK, 'f', True, True),
   L([(46, 86), (54, 86), (50, 91)], (210, 130, 130, 255), 'f', False, True)],
  _howell('side') + [L(blob([(70, 86), (92, 84), (92, 100), (74, 102)], 6), MASK, 'f', True, True)],
  _howell('back'))

# Paul Steed: grandullón de cara ancha y mofletuda; pelo verde petróleo corto en lo alto con dos mechones a rayas grises que
# salen como orejas; ojos blancos de enfado, nariz marrón grande y chata y boca de disgusto
STRP = _c('#7a7a80')
C('paul-steed', 'corpulento', P('#3d6d5d', '#fec16e', iris='#20181a'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=100, hairline=[(8, 50), (24, 40), (50, 36), (76, 40), (92, 50)], big_ears=3, ear_out=4,
    face_front=blob([(12, 46), (50, 30), (88, 46), (96, 76), (90, 100), (70, 112), (50, 114), (30, 112), (10, 100), (4, 76)])),
  crop('front', top=4, side=46, w=0) +
  [L(blob([(14, 24), (8, 8), (26, 6), (30, 22)], 6), STRP), L(blob([(86, 24), (92, 8), (74, 6), (70, 22)], 6), STRP),
   strand([(12, 14), (26, 12)], 'deep', 'b', 1.4), strand([(74, 12), (88, 14)], 'deep', 'b', 1.4),
   L(blob([(42, 82), (58, 82), (60, 90), (50, 94), (40, 90)], 6), _c('#b07850'), 'f', True, True)],
  crop('side', top=4, nape=70, w=0) + [L(blob([(30, 22), (24, 6), (42, 4), (46, 20)], 6), STRP), L(blob([(84, 82), (94, 84), (92, 92), (84, 92)], 4), _c('#b07850'), 'f', True)],
  crop('back', top=4, nape=72, w=0) + [L(blob([(14, 24), (8, 8), (26, 6), (30, 22)], 6), STRP), L(blob([(86, 24), (92, 8), (74, 6), (70, 22)], 6), STRP)])
