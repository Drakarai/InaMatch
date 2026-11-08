"""Ojeadores de CS (scouts-cs), tanda 03: dibujados a partir de su retrato de Victory Road; claves 'scouts-cs:<id>'.

El frente sale del retrato; el perfil y la espalda, de los modelos 3D cuando son del mismo personaje (Nakaoka Shintarou,
Kinoshita Toukichirou, Maeda Toshiie, Yamano Van) y, si no, se deducen de cómo cae el peinado. Ayudas propias: eyes_f()
(ojos dibujados encima de máscaras y pinturas), beard() (barbas de frente y de perfil), topknot() (moño de samurái)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401
from chars_scouts_ie1_09 import dome, hl, face, face_side, _c  # noqa: F401
from chars_scouts_ie3_02 import hood, bowl3, ring, scarf, side_lock  # noqa: F401
from chars_scouts_ie1_03 import round_specs, thick_brows, side_brow, blush, freckles  # noqa: F401
from chars_scouts_ie2_03 import ears_pointy, curls  # noqa: F401

K = 'scouts-cs:'
WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)


def F(**k):
    d = {'eyes': 'normal', 'mouth': 'line'}
    d.update(k)
    return d


def P(hair, skin, iris='#302232', **k):
    return pal(hair, skin, iris, **k)


def C(pid, body, palette, f, front, side, back):
    """El nacimiento del pelo baja por el borde de la cara hasta la barbilla: así su raya no cruza el pelo de los lados."""
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[K + pid] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def eyes_f(iris, ey=75, sep=14, kind='sharp', brows=None):
    """Ojos como capas de delante (encima de máscaras o pinturas): devuelve (frente, perfil)."""
    fr, sd = [], []
    for cx, s in ((50 - sep, 1), (50 + sep, -1)):
        if kind == 'sharp':
            e = [(cx - 8 * s, ey - 4), (cx + 7 * s, ey - 1.5), (cx + 5.5 * s, ey + 5), (cx - 6 * s, ey + 3.5)]
            fr += [L(blob(e, 3), WHITE, 'f', False), L(ell(cx + s, ey + 1, 3.4, 4.2), iris, 'f', False),
                   L(ell(cx + s * 2, ey - 0.6, 1.1, 1.1), WHITE, 'f', False), L([e[0], e[1]], OUTC, 'f', False, False, 2.8)]
        else:
            fr += [L(ell(cx, ey, 5.2, 6.2), WHITE, 'f', False), L(ell(cx, ey + 1, 4, 5), iris, 'f', False),
                   L(ell(cx, ey + 1.6, 2, 2.6), BLACK, 'f', False), L(ell(cx - s * 1.4 + 1, ey - 2, 1.3, 1.3), WHITE, 'f', False),
                   L(quad((cx - 6, ey - 2), (cx, ey - 8), (cx + 6, ey - 2)), OUTC, 'f', False, False, 2.4)]
        if brows:
            fr.append(L([(cx - 8 * s, ey - 13), (cx + 7 * s, ey - 9)], brows, 'f', False, False, 2.8))
    sd += [L(blob([(74, ey - 3.5), (85, ey - 2), (84.5, ey + 5), (75, ey + 4)], 3), WHITE, 'f', False), L(ell(81.5, ey + 1, 3, 4), iris, 'f', False),
           L([(74, ey - 3.5), (85, ey - 2)], OUTC, 'f', False, False, 2.8)]
    if brows:
        sd.append(L([(71, ey - 12), (84, ey - 9)], brows, 'f', False, False, 2.8))
    return fr, sd


def beard(view, c='mid', top=84, low=112, w=0, mouth=True):
    """Barba que rodea la boca y la barbilla."""
    if view == 'front':
        out = [L(outline([(16 - w, 70), (22, top), (36, top + 4), (44, 92), (56, 92), (64, top + 4), (78, top), (84 + w, 70), (88 + w, 92), (72, low - 4), (50, low + 2, 1),
                          (28, low - 4), (12 - w, 92)]), c, 'f')]
        if mouth:
            out.append(L([(44, 96), (56, 96)], OUTC, 'f', False, False, 1.6))
        return out
    if view == 'side':
        return [L(outline([(54, 70), (66, top), (80, top + 4), (88, 92), (90, low - 8), (76, low + 2, 1), (58, low - 6), (48, 90)]), c, 'f')]
    return [L(outline([(14 - w, 80), (24, 100), (50, low), (76, 100), (86 + w, 80), (80, 96), (50, 104), (20, 96)]), c, 'f', True)]


def topknot(view, c='mid', x=50, y=-4, h=14):
    """Moño de samurái arriba: de frente y de espaldas un pincho, de perfil tumbado hacia delante."""
    if view == 'side':
        return [L(outline([(30, 8), (34, -2), (60, y - 6), (80, y - 14, 1), (66, y), (46, 12)]), c), L(ell(36, 4, 5, 6), (200, 160, 170, 255), 'f', False)]
    return [L(outline([(x - 7, y + 12), (x - 5, y - h), (x - 1, y - h + 6), (x + 2, y - h - 4, 1), (x + 5, y - h + 4), (x + 7, y + 12)]), c, 'b')]


def side_eye_ring(c, ey=75):
    return L(blob([(70, ey - 8), (88, ey - 8), (90, ey + 8), (70, ey + 8)], 4), c, 'f', False)


# ------------------------------------------------------------------ jugadores

# Pyon Pyon (portera): gorro de punto gris oscuro con canalé, media melena negra lisa de flequillo recto que asoma por debajo;
# piel morena clara, ojos azules grandes, coloretes y la boca en "o"
BEAN = _c('#3a3d42')
def _beanie(view):
    if view == 'front':
        return [L(outline([(8, 52), (10, 26), (24, 4), (50, -4), (76, 4), (90, 26), (92, 52), (50, 48)]), BEAN),
                L(outline([(8, 50), (50, 44), (92, 50), (92, 58), (50, 54), (8, 58)]), _c('#2c2e33'), 'b', True)] + \
               [L([(x, 4 + abs(x - 50) * 0.3), (x * 0.96 + 2, 46)], _c('#26282c'), 'b', False, False, 1.0) for x in (26, 38, 50, 62, 74)]
    if view == 'side':
        return [L(outline([(6, 60), (2, 30), (20, 4), (48, -4), (76, 4), (92, 26), (94, 48), (60, 48), (30, 58)]), BEAN),
                L(outline([(4, 56), (40, 50), (94, 44), (94, 52), (40, 58), (6, 64)]), _c('#2c2e33'), 'b', True)]
    return [L(outline([(6, 62), (8, 26), (24, 4), (50, -4), (76, 4), (92, 26), (94, 62), (50, 58)]), BEAN),
            L(outline([(6, 58), (50, 52), (94, 58), (94, 66), (50, 62), (6, 66)]), _c('#2c2e33'), 'b', True)]
C('pyon-pyon', 'chica', P('#1e1e22', '#d29c6e', iris='#3a8ab0'),
  F(eyes='normal', brows=True, mouth='none', mouth_y=94, hairline=[(8, 62), (20, 62), (50, 62), (80, 62), (92, 62)]),
  bowl3('front', top=10, side=96, fringe=62, w=2) + _beanie('front') + blush(86, 22, 4.4) + [L(ell(50, 95, 2.4, 3), (120, 40, 40, 255), 'f', True)],
  bowl3('side', top=10, nape=96, fringe=62, w=2) + _beanie('side'),
  bowl3('back', top=10, nape=98, w=2) + _beanie('back'))

# Redd Hazzard: melena carmesí larga y erizada en mechones de punta; máscara roja de luchador con lunares blancos en la
# frente que le tapa la cara hasta la nariz; ojos rosas
MSK = _c('#d4204a')
_rf, _rs = eyes_f(_c('#e070b0'), kind='sharp')
C('redd-hazzard', 'normal', P('#ac224a', '#e8c8a8', shade='#851d36', deep='#611a27'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=95, hairline=[(6, 70), (18, 50), (34, 42), (50, 40), (66, 42), (82, 50), (94, 70)]),
  dome('front', top=-6, w=52, cy=44, n=11, amp=14, seed=11, long=100, flare=8, ends=5) +
  [L(outline([(15, 52), (24, 40), (50, 36), (76, 40), (85, 52), (84, 80), (64, 86), (56, 82), (50, 90, 1), (44, 82), (36, 86), (16, 80)]), MSK, 'f'),
   L(ell(40, 44, 3, 2.4), WHITE, 'f', False), L(ell(58, 42, 4, 3), WHITE, 'f', False), L(ell(66, 50, 2.4, 2), WHITE, 'f', False)] + _rf +
  [L(outline([(44, 34), (56, 30), (60, 42), (52, 52, 1), (48, 42)]), 'mid', 'f')],
  dome('side', top=-6, w=52, cy=44, n=11, amp=14, seed=11, long=100, flare=8, fr=48) +
  [L(outline([(62, 50), (86, 44), (90, 62), (88, 80), (66, 84), (58, 70)]), MSK, 'f'), L(ell(74, 48, 2.6, 2.2), WHITE, 'f', False)] + _rs,
  dome('back', top=-6, w=52, cy=44, n=11, amp=14, seed=11, long=100, flare=8, ends=5))

# Rei Nurtur (portera): pelo largo castaño grisáceo con raya a un lado, que le tapa media frente y cae por un hombro en una
# cortina que se enrosca; ojos dorados y sonrisa tranquila
C('rei-nurtur', 'chica', P('#94826e', '#fcebc1', iris='#b08a3a', shade='#7c6b5a', deep='#6a5243'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=93, hairline=[(6, 66), (20, 50), (40, 42), (60, 40), (80, 48), (94, 66)]),
  dome('front', top=2, w=47, cy=44, soft=True, long=104, flare=4) +
  [L(outline([(16, 52), (36, 32), (66, 30), (82, 44), (72, 52), (56, 50), (44, 58)]), 'mid', 'f'),
   L(outline([(70, 48), (86, 50), (92, 80), (86, 112), (70, 126, 1), (74, 104), (76, 80)]), 'mid', 'f'),
   strand([(78, 56), (84, 86), (76, 116)], 'deep', 'f', 1.0)],
  dome('side', top=2, w=47, cy=44, soft=True, long=104, flare=4, fr=50) + [L(outline([(70, 40), (90, 44), (92, 60), (82, 52)]), 'mid', 'f')],
  dome('back', top=2, w=47, cy=44, soft=True, long=104, flare=4) + [L(outline([(20, 60), (6, 100), (14, 124, 1), (24, 96)]), 'shade', 'f')])

# Rick Warwick: oni grandullón: pelo negro corto con dos cuernos grises curvados hacia arriba, antifaz rojo alrededor de los
# ojos, nariz naranja, colmillos y una barba negra cerrada que le rodea la cara
HRN = _c('#7a7684')
_kf, _ks = eyes_f(_c('#c83a2a'), kind='sharp', brows=BLACK)
C('rick-warwick', 'corpulento', P('#16121b', '#e3c8a3'),
  F(eyes='none', brows=False, mouth='none', hairline=[(6, 62), (20, 52), (50, 48), (80, 52), (94, 62)], face_front=face(w=4, chin=106, jaw=3), nose=(50, 88, 4)),
  dome('front', top=6, w=48, cy=44, sb=60) +
  [L(outline([(18, 32), (2, 22), (-4, 2, 1), (6, 14), (14, 22), (24, 26)]), HRN, 'b'), L(outline([(82, 32), (98, 22), (104, 2, 1), (94, 14), (86, 22), (76, 26)]), HRN, 'b'),
   L(outline([(16, 66), (26, 64), (50, 70), (74, 64), (84, 66), (82, 84), (64, 82), (50, 78), (36, 82), (18, 84)]), _c('#c82a2a'), 'f')] + _kf +
  [L(ell(50, 87, 5, 4), _c('#e07a3a'), 'f')] + beard('front', BLACK, 88, 116, 4, mouth=False) +
  [L(outline([(36, 92), (40, 102, 1), (44, 94)]), WHITE, 'f'), L(outline([(56, 94), (60, 102, 1), (64, 92)]), WHITE, 'f')],
  dome('side', top=6, w=48, cy=44, nape=84, fr=48) + [L(outline([(44, 20), (36, 4), (40, -14, 1), (48, 4), (54, 16)]), HRN, 'b'),
   L(outline([(66, 64), (90, 66), (90, 84), (68, 82)]), _c('#c82a2a'), 'f')] + _ks + [L(ell(90, 87, 3, 4), _c('#e07a3a'), 'f')] + beard('side', BLACK, 88, 116),
  dome('back', top=6, w=48, cy=44, nape=84) + [L(outline([(18, 32), (2, 22), (-4, 2, 1), (6, 14), (14, 22), (24, 26)]), HRN),
   L(outline([(82, 32), (98, 22), (104, 2, 1), (94, 14), (86, 22), (76, 26)]), HRN)] + beard('back', BLACK, 88, 112, 4))

# Roost Dubois: cara de mono: pelo castaño oscuro peinado hacia atrás con pico en la frente, orejas grandes, ojos verdes
# afilados con mucha raya, nariz ancha y la boca torcida hacia abajo
C('roost-dubois', 'normal', P('#5a524d', '#f6d0ae', iris='#3a8a5a', shade='#463f3b'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=97, big_ears=3, ear_out=4, nose=(50, 86, 4.4),
    hairline=[(8, 62), (20, 46), (34, 40), (50, 54), (66, 40), (80, 46), (92, 62)], face_front=face(chin=106, jaw=2)),
  dome('front', top=2, w=46, cy=44, sb=62),
  dome('side', top=2, w=46, cy=44, nape=86, fr=48),
  dome('back', top=2, w=46, cy=44, nape=86))

# Ruff LeGrand (portero): vikingo grandote: melena rubia hacia atrás con trencitas atadas con cintas azules a los lados,
# pintura azul en las mejillas, tirita en la nariz, ceño fruncido y barba rubia con una trenza
BLU = _c('#3a7ac0')
C('ruff-legrand', 'corpulento', P('#f0c870', '#e0a070', iris='#3a6ab0', shade='#c8a050'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=97, hairline=[(8, 62), (22, 48), (40, 44), (50, 50), (60, 44), (78, 48), (92, 62)], face_front=face(w=3, chin=106, jaw=2)),
  dome('front', top=-4, w=48, cy=42, n=7, amp=10, seed=21, sb=74) +
  [L(blob([(22, 80), (34, 76), (42, 84), (30, 88)], 4), BLU, 'f', False), L(blob([(78, 80), (66, 76), (58, 84), (70, 88)], 4), BLU, 'f', False),
   L(outline([(42, 78), (58, 78), (58, 84), (42, 84)]), _c('#f4e2c8'), 'f')] + beard('front', 'mid', 92, 112, 2) +
  [L(outline([(46, 110), (54, 110), (52, 128), (50, 132, 1), (48, 128)]), 'mid', 'f'), L(outline([(6, 74), (14, 74), (12, 96), (8, 96)]), 'mid', 'f'),
   L(outline([(86, 74), (94, 74), (92, 96), (88, 96)]), 'mid', 'f'), L([(7, 90), (13, 90)], BLU, 'f', False, False, 2.4), L([(87, 90), (93, 90)], BLU, 'f', False, False, 2.4)],
  dome('side', top=-4, w=48, cy=42, n=7, amp=10, seed=21, nape=92, fr=46) + beard('side', 'mid', 92, 112) +
  [L(outline([(36, 70), (44, 70), (42, 100), (38, 100)]), 'mid', 'f'), L([(37, 92), (43, 92)], BLU, 'f', False, False, 2.4)],
  dome('back', top=-4, w=48, cy=42, n=7, amp=10, seed=21, nape=94) + beard('back', 'mid', 92, 110, 2))

# Ryo Terada (portera): pelo azul blanquecino largo recogido en una coleta alta con goma lila, con mechones largos por delante
# de las orejas; ojos azules
C('ryo-terada', 'chica', P('#dcf4f6', '#fcefd5', iris='#4a8ab0', shade='#a8c8d0', deep='#87979b'),
  F(eyes='normal', brows=True, mouth='line', mouth_y=93, hairline=[(8, 64), (20, 48), (36, 42), (50, 50), (64, 42), (80, 48), (92, 64)]),
  dome('front', top=2, w=46, cy=44, soft=True, sb=70) +
  [side_lock(14, 54, 104, wd=12), side_lock(86, 54, 104, wd=12), L(outline([(44, 4), (56, 4), (54, -6), (46, -6)]), _c('#9a6ac8'), 'b')],
  dome('side', top=2, w=46, cy=44, soft=True, nape=84, fr=50) +
  [L(outline([(26, 4), (6, 10), (-6, 50), (-4, 92, 1), (10, 54), (20, 22)]), 'mid', 'b'), L(ell(26, 4, 4, 4), _c('#9a6ac8'), 'f'),
   L(outline([(62, 56), (70, 56), (68, 100), (64, 104, 1)]), 'mid', 'f')],
  dome('back', top=2, w=46, cy=44, soft=True, nape=84) +
  [L(outline([(42, 4), (58, 4), (60, 50), (54, 100), (50, 108, 1), (46, 100), (40, 50)]), 'mid', 'f'), L(ell(50, 6, 6, 4), _c('#9a6ac8'), 'f')])

# Ryuun Cho: pelo plateado largo hacia atrás en una coleta alta atada con una cinta roja, mechones que le caen por la frente
# y los lados; cejas plateadas fruncidas, ojos azul grisáceo
C('ryuun-cho', 'normal', P('#d5dbe2', '#fce7b6', iris='#5a6a8a', shade='#a8aeb8', deep='#7a6869'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(8, 66), (18, 50), (34, 48), (50, 56), (66, 48), (82, 50), (92, 66)]),
  dome('front', top=0, w=46, cy=44, n=5, amp=8, seed=4, sb=82) +
  [L(outline([(48, 2), (58, -14), (70, -18, 1), (62, 2)]), 'mid', 'b'), L([(48, 4), (62, 2)], _c('#c82a2a'), 'f', False, False, 3),
   side_lock(14, 56, 100, wd=10), side_lock(86, 56, 100, wd=10)],
  dome('side', top=0, w=46, cy=44, n=5, amp=8, seed=4, nape=86, fr=50) +
  [L(outline([(30, 4), (8, -6), (-8, 30), (-6, 80, 1), (6, 40), (24, 14)]), 'mid', 'b'), L(ell(28, 6, 4, 5), _c('#c82a2a'), 'f')],
  dome('back', top=0, w=46, cy=44, n=5, amp=8, seed=4, nape=86) +
  [L(outline([(42, 4), (58, 4), (62, 50), (52, 96, 1), (40, 50)]), 'mid', 'f'), L(ell(50, 6, 7, 4), _c('#c82a2a'), 'f')])

# Samey Kondo: rizos azul marino abultados con dos moños de rizos a los lados atados con cintas blancas que cuelgan; cejas
# gruesas, ojos azules grandes y la boca abierta y contenta
C('samey-kondo', 'normal', P('#384974', '#eecca9', iris='#3a7ac0', shade='#2e3347'),
  F(eyes='normal', brows='angry', mouth='grin', mouth_y=94, hairline=[(8, 62), (22, 54), (36, 56), (50, 52), (64, 56), (78, 54), (92, 62)]),
  [L(curls(10, 0, (14, 12), 6)), L(curls(90, 0, (14, 12), 6))] +
  dome('front', top=2, w=48, cy=44, n=10, amp=6, soft=True, seed=5, sb=64) + [L(ell(17, 11, 4, 3), WHITE, 'f'), L(ell(83, 11, 4, 3), WHITE, 'f')] +
  [L(outline([(14, 70), (20, 72), (18, 90), (12, 86)]), WHITE, 'f'), L(outline([(86, 70), (80, 72), (82, 90), (88, 86)]), WHITE, 'f')],
  [L(curls(46, 6, (14, 12), 6))] + dome('side', top=2, w=48, cy=44, n=10, amp=6, soft=True, seed=5, nape=84, fr=50),
  [L(curls(10, 0, (14, 12), 6)), L(curls(90, 0, (14, 12), 6))] + dome('back', top=2, w=48, cy=44, n=10, amp=6, soft=True, seed=5, nape=84))

# Sandi Bay: melena corta de nube crema claro, abultada, con mechones que le caen por la frente; piel morena, ojos azules
# afilados con pestañas
C('sandi-bay', 'chica', P('#e0e0bc', '#c87050', iris='#4a8ac8', shade='#b8b498', deep='#8f7c6a'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=93, hairline=[(6, 66), (18, 50), (30, 58), (42, 50), (54, 58), (66, 50), (80, 58), (94, 66)]),
  dome('front', top=-4, w=52, cy=42, n=12, amp=8, soft=True, seed=6, sb=72) +
  [L([(22, 70), (18, 66)], OUTC, 'f', False, False, 1.6), L([(78, 70), (82, 66)], OUTC, 'f', False, False, 1.6)],
  dome('side', top=-4, w=52, cy=42, n=12, amp=8, soft=True, seed=6, nape=88, fr=54),
  dome('back', top=-4, w=52, cy=42, n=12, amp=8, soft=True, seed=6, nape=90))

# Saul Première: media melena castaña lisa con flequillo de mechones en pico y las puntas abiertas por los lados; ojos lilas
# afilados y sonrisa pícara
C('saul-premi-re', 'normal', P('#7b6653', '#fad0a1', iris='#7a6ab0', shade='#5e463b', deep='#4a352d'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=hl(5, 64, 46, 60, lean=2, jit=2, seed=3)),
  dome('front', top=2, w=48, cy=44, soft=True, long=94, flare=10, n=4, amp=4, seed=7),
  dome('side', top=2, w=48, cy=44, soft=True, long=94, flare=10, n=4, amp=4, seed=7, fr=54),
  dome('back', top=2, w=48, cy=44, soft=True, long=94, flare=10, n=4, amp=4, seed=7))

# Sayo Nakamise: pelo morado muy oscuro con dos moños redondos y un lazo rosa entre ellos, flequillo recto y dos mechones
# finos larguísimos que le caen junto a la cara; ojos verdes y sonrisa
PNK = _c('#f09aa8')
C('sayo-nakamise', 'chica', P('#2f1e37', '#fccea0', iris='#3a9a8a', shade='#241628'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=93, hairline=[(8, 60), (20, 54), (50, 52), (80, 54), (92, 60)]),
  [L(ell(26, 2, 13, 12)), L(ell(74, 2, 13, 12))] + bowl3('front', top=6, side=70, fringe=56) +
  [L(outline([(36, 2), (50, 6), (64, 2), (62, 12), (50, 10), (38, 12)]), PNK, 'f'), L(ell(50, 8, 3.4, 3.4), PNK, 'f'),
   L(outline([(13, 60), (17, 60), (16, 112), (14, 118, 1)]), 'mid', 'f'), L(outline([(83, 60), (87, 60), (86, 118, 1), (84, 112)]), 'mid', 'f')],
  [L(ell(46, 0, 12, 12))] + bowl3('side', top=6, nape=88, fringe=56) + [L(outline([(60, 60), (64, 60), (62, 116, 1)]), 'mid', 'f')],
  [L(ell(26, 2, 13, 12)), L(ell(74, 2, 13, 12))] + bowl3('back', top=6, nape=88) + [L(outline([(36, 2), (50, 6), (64, 2), (62, 12), (50, 10), (38, 12)]), PNK, 'f')])

# Scott Chegwin: mono: la cabeza cubierta de pelo marrón como una capucha con pico sobre la frente y patillas, orejas de mono
# redondas y naranjas; cara naranja, ojos redondos y sonrisa
OEAR = _c('#e89a58')
C('scott-chegwin', 'normal', P('#614e3d', '#eca662', iris='#1e1a1a', shade='#453831'),
  F(eyes='round', brows=False, mouth='smile', mouth_y=93, ears=False, hairline=[(10, 80), (18, 54), (34, 48), (50, 60), (66, 48), (82, 54), (90, 80)]),
  [L(ell(8, 70, 10, 12), OEAR), L(ell(92, 70, 10, 12), OEAR), L(ell(8, 70, 5, 7), _c('#c87a40'), 'b', False), L(ell(92, 70, 5, 7), _c('#c87a40'), 'b', False)] +
  dome('front', top=-6, w=48, cy=44, sb=96, n=0),
  dome('side', top=-6, w=48, cy=44, nape=96, fr=52) + [L(ell(44, 70, 9, 11), OEAR, 'f'), L(ell(44, 70, 5, 7), _c('#c87a40'), 'f', False)],
  dome('back', top=-6, w=48, cy=44, nape=98) + [L(ell(6, 70, 10, 12), OEAR), L(ell(94, 70, 10, 12), OEAR)])

# Senjiro Kohama: grandullón de piel morena y cara cuadrada; tupé de rizos castaño oscuro alto y lados rapados, cejas gruesas
# muy fruncidas, tirita en la nariz, barba de tres días y los dientes apretados
C('senjiro-kohama', 'corpulento', P('#41342b', '#ae8860', iris='#1e1a1a', shade='#31251e'),
  F(eyes='sharp', brows=False, mouth='grin', mouth_y=97, hairline=[(8, 50), (22, 38), (50, 34), (78, 38), (92, 50)], face_front=face(w=4, chin=108, jaw=4), nose=(50, 88, 3)),
  dome('front', top=18, w=40, cy=46, sb=50, c='shade', shade=False) + [L(curls(50, 16, (32, 15), 9))] + thick_brows(64, BLACK, 5, 15, 1.6, 15) +
  [L(outline([(42, 82), (58, 82), (58, 88), (42, 88)]), _c('#d8b088'), 'f'), L(blob([(34, 104), (50, 108), (66, 104), (60, 107), (50, 110), (40, 107)], 4), _c('#8a6a48'), 'f', False)],
  dome('side', top=18, w=40, cy=46, nape=70, fr=38, c='shade', shade=False) + [L(curls(52, 14, (28, 15), 8))] + side_brow(64, BLACK, 5, 1.6),
  dome('back', top=18, w=40, cy=46, nape=70, c='shade', shade=False) + [L(curls(50, 16, (30, 15), 9))])

# Senkuro Hajime: pelo gris pardo largo peinado hacia un lado que le cae en mechones hasta el cuello; venda blanca en la
# frente con una placa marrón, parche negro en el ojo derecho
C('senkuro-hajime', 'normal', P('#b3a896', '#fadcba', iris='#3a3430', shade='#866b60', deep='#674e46'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=94, hairline=[(6, 66), (16, 50), (34, 42), (60, 40), (80, 46), (94, 60)]),
  dome('front', top=-2, w=47, cy=44, soft=True, long=104, flare=6, n=5, amp=6, seed=12) +
  [L(outline([(16, 54), (14, 70), (8, 100), (14, 120, 1), (24, 92), (30, 62)]), 'mid', 'f'),
   L(outline([(20, 48), (82, 44), (84, 56), (24, 60)]), _c('#f2ece4'), 'f'), L(outline([(30, 49), (56, 47), (56, 55), (30, 57)]), _c('#8a4a2a'), 'f', False),
   L(ell(36, 76, 8, 7), BLACK, 'f'), L([(20, 66), (46, 72)], BLACK, 'f', False, False, 1.6)],
  dome('side', top=-2, w=47, cy=44, soft=True, long=104, flare=6, n=5, amp=6, seed=12, fr=46) +
  [L(outline([(30, 48), (86, 44), (88, 56), (32, 60)]), _c('#f2ece4'), 'f')],
  dome('back', top=-2, w=47, cy=44, soft=True, long=104, flare=6, n=5, amp=6, seed=12) + [L(outline([(10, 46), (90, 46), (90, 56), (10, 56)]), _c('#f2ece4'), 'f')])

# Senzo Takamori: pelo azul petróleo enorme en mechones gruesos de punta abiertos hacia los lados; cara alargada pálida, ojos
# entornados y perilla
C('senzo-takamori', 'delgado', P('#1d4662', '#e8d6b8', iris='#3a5a7a', shade='#182d3b'),
  F(eyes='sharp', brows=True, mouth='frown', mouth_y=96, face_front=face(chin=106), hairline=hl(4, 64, 50, 60, jit=2, seed=9)),
  dome('front', top=-12, w=54, cy=42, n=8, amp=18, seed=13, sb=80) + [L(outline([(46, 100), (54, 100), (52, 110, 1), (48, 108)]), 'mid', 'f')],
  dome('side', top=-12, w=54, cy=42, n=8, amp=18, seed=13, nape=90, fr=52) + [L(outline([(82, 100), (88, 98), (88, 110, 1)]), 'mid', 'f')],
  dome('back', top=-12, w=54, cy=42, n=8, amp=18, seed=13, nape=90))

# Shinken Gaku: pelo azul marino peinado hacia atrás en un mechón grueso con los lados rapados gris azulado, coleta baja con un
# cascabel; ojos lilas con raya, perilla gris y pendiente
GRB = _c('#a8b6c0')
C('shinken-gaku', 'normal', P('#294963', '#fbf0d6', iris='#7a4a9a', shade='#243441'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(8, 66), (16, 52), (30, 46), (50, 60), (70, 46), (84, 52), (92, 66)]),
  [L(outline([(10, 70), (10, 30), (90, 30), (90, 70), (50, 66)]), GRB)] +
  [L(outline([(26, 50), (24, 14), (40, -6), (60, -14), (80, -8), (92, 4, 1), (76, 6), (70, 20), (64, 44), (50, 62, 1), (36, 44)])),
   L(blob([(30, 98), (50, 106), (70, 98), (62, 108), (50, 112), (38, 108)], 4), GRB, 'f', False), L(ell(86, 82, 2, 2), _c('#e0c050'), 'f')],
  [L(outline([(54, 60), (30, 66), (8, 50), (8, 24), (40, 10), (60, 20)]), GRB),
   L(outline([(84, 40), (74, 6), (50, -10), (20, -6), (4, 12, 1), (20, 14), (36, 30), (30, 60), (40, 96), (36, 110, 1), (50, 92), (56, 50), (70, 38)])),
   L(ell(42, 104, 4, 4), _c('#e0c050'), 'f')],
  [L(outline([(12, 76), (10, 30), (90, 30), (88, 76), (50, 82)]), GRB),
   L(outline([(30, 10), (50, -10), (70, 10), (62, 60), (56, 100), (50, 110, 1), (44, 100), (38, 60)])), L(ell(50, 104, 4, 4), _c('#e0c050'), 'f')])

# Shintaro Nakaoka (modelo 3D): pelo verde grisáceo peinado tirante hacia atrás hasta un moño de samurái en punta; cejas
# gruesas fruncidas, una cicatriz en la frente y perilla
C('shintaro-nakaoka', 'normal', P('#686d53', '#fbd18b', iris='#1e1a1a', shade='#504933'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(10, 62), (18, 44), (34, 34), (50, 32), (66, 34), (82, 44), (90, 62)]),
  dome('front', top=6, w=44, cy=44, sb=64) + topknot('front') + [strand([(36, 14), (40, 36)], 'shade', 'b', 1.0), strand([(64, 14), (60, 36)], 'shade', 'b', 1.0),
   L([(56, 50), (62, 58)], _c('#c8905a'), 'f', False, False, 1.2), L(outline([(46, 100), (54, 100), (50, 108, 1)]), 'mid', 'f')],
  dome('side', top=6, w=44, cy=44, nape=84, fr=44) + topknot('side') + [L(outline([(84, 100), (89, 99), (88, 108, 1)]), 'mid', 'f')],
  dome('back', top=6, w=44, cy=44, nape=84) + topknot('front'))

# Silvain Hache: pelo blanco con sombras rosas en mechones de punta; le cae un mechón grande sobre un ojo y lleva una visera
# lila transparente sobre media cara
VIS = (196, 186, 230, 200)
C('silvain-hache', 'normal', P('#f2eef0', '#f0c8a8', iris='#7a8aa8', shade='#d8b8c0', deep='#977d7e'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=94, hairline=[(6, 66), (18, 50), (34, 44), (54, 44), (72, 46), (94, 64)]),
  dome('front', top=-10, w=50, cy=42, n=8, amp=14, sweep=0.4, seed=14, sb=74) +
  [L(outline([(16, 52), (30, 40), (52, 36), (56, 60), (46, 92, 1), (40, 70), (24, 62)]), 'mid', 'f'),
   L(outline([(16, 58), (52, 56), (54, 84), (40, 92), (18, 84)]), VIS, 'f', True), L(outline([(56, 46), (76, 46), (74, 52), (58, 52)]), _c('#3a2a3a'), 'f')],
  dome('side', top=-10, w=50, cy=42, n=8, amp=14, sweep=0.4, seed=14, nape=86, fr=50) + [L(outline([(66, 58), (90, 58), (90, 84), (70, 86)]), VIS, 'f', True)],
  dome('back', top=-10, w=50, cy=42, n=8, amp=14, sweep=0.4, seed=14, nape=86))

# Sloan Henge-Hinge: pelo gris pardo alborotado que le tapa un ojo; en el otro, un monóculo de espiral azul con una cadenita
# y un pendiente azul colgando
MON = _c('#4a8ac8')
C('sloan-henge-hinge', 'normal', P('#9a9480', '#f8ddbe', iris='#3a3430', shade='#7d7569', deep='#675549'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=95, hairline=[(6, 66), (18, 48), (40, 44), (62, 46), (80, 50), (94, 64)]),
  dome('front', top=-8, w=52, cy=42, n=12, amp=10, seed=15, sb=76) +
  [L(outline([(14, 52), (30, 40), (54, 40), (50, 66), (40, 86, 1), (32, 70), (18, 66)]), 'mid', 'f'),
   L(ell(64, 76, 9, 9), WHITE, 'f'), L(ell(64, 76, 6, 6), MON, 'f', False), L(ell(64, 76, 3, 3), WHITE, 'f', False), L(ell(64, 76, 1.4, 1.4), BLACK, 'f', False),
   L([(72, 80), (76, 96)], _c('#c8c8c8'), 'f', False, False, 1.0), L(outline([(76, 96), (79, 100), (76, 108, 1), (73, 100)]), MON, 'f')],
  dome('side', top=-8, w=52, cy=42, n=12, amp=10, seed=15, nape=88, fr=52) + [L(ell(82, 76, 5, 8), WHITE, 'f'), L(ell(82, 76, 3, 5), MON, 'f', False)],
  dome('back', top=-8, w=52, cy=42, n=12, amp=10, seed=15, nape=90))

# Souta Hayari: pinchos azul marino hacia atrás y un flequillo naranja en llamas que le cae por la frente; una cuerda con una
# bola negra colgando a un lado; ojos afilados
ORF = _c('#c84a10')
C('souta-hayari', 'normal', P('#141a30', '#e4bb8f', iris='#1e1a1a', shade='#0c0c14'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=hl(4, 64, 48, 62, jit=2, seed=6)),
  dome('front', top=-10, w=50, cy=42, n=8, amp=16, seed=16, sb=72) +
  [L(outline([(22, 56), (24, 32), (40, 14), (50, 2, 1), (56, 20), (70, 30), (78, 56), (66, 52), (58, 64, 1), (50, 50), (42, 64, 1), (34, 52)]), ORF, 'f'),
   L(quad((18, 82), (10, 96), (16, 104)), _c('#e8e0d0'), 'f', False, False, 2.4), L(ell(16, 106, 5, 5), BLACK, 'f')],
  dome('side', top=-10, w=50, cy=42, n=8, amp=16, seed=16, nape=86, fr=50) + [L(outline([(70, 30), (86, 34), (92, 56), (84, 62, 1), (76, 50)]), ORF, 'f')],
  dome('back', top=-10, w=50, cy=42, n=8, amp=16, seed=16, nape=86))

# Stan Proud: grandullón moreno de cara cuadrada; pelo rojo en pinchos de punta hacia arriba y barba roja enorme que le rodea la
# cara; cejas negras gruesas fruncidas y ojos turquesa
C('stan-proud', 'corpulento', P('#b02015', '#bd834f', iris='#3aa8b0', shade='#7b2016'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=96, hairline=[(8, 60), (22, 46), (40, 42), (50, 48), (60, 42), (78, 46), (92, 60)], face_front=face(w=4, chin=106, jaw=3)),
  dome('front', top=-10, w=50, cy=40, n=6, amp=16, seed=17, sb=70) + thick_brows(64, BLACK, 5, 15, 1.4, 15) + beard('front', 'mid', 88, 118, 6),
  dome('side', top=-10, w=50, cy=40, n=6, amp=16, seed=17, nape=86, fr=48) + side_brow(64, BLACK, 5, 1.4) + beard('side', 'mid', 88, 118),
  dome('back', top=-10, w=50, cy=40, n=6, amp=16, seed=17, nape=86) + beard('back', 'mid', 88, 114, 6))

# Sting Xiang: pelo azul grisáceo largo y liso con flequillo, diadema azul con rombos blancos; mascarilla azul con un rombo
# que le tapa boca y nariz; ojos turquesa grandes
HBL = _c('#5a98d8')
C('sting-xiang', 'chica', P('#668898', '#eee1cd', iris='#3ab0c8', shade='#4c6470'),
  F(eyes='normal', brows=True, mouth='none', hairline=hl(5, 66, 50, 62, jit=2, seed=8)),
  dome('front', top=0, w=48, cy=44, soft=True, long=118, flare=6, ends=5) +
  [L(quad((10, 40), (50, 2), (90, 40)), HBL, 'f', False, False, 4.5), L(outline([(46, 10), (50, 4), (54, 10), (50, 16)]), WHITE, 'f', False),
   L(outline([(20, 82), (50, 80), (80, 82), (78, 98), (50, 106), (22, 98)]), HBL, 'f'), L(outline([(60, 88), (64, 84), (68, 88), (64, 92)]), WHITE, 'f', False)],
  dome('side', top=0, w=48, cy=44, soft=True, long=118, flare=6, fr=56) +
  [L(quad((40, 0), (60, 4), (80, 26)), HBL, 'f', False, False, 4.5), L(outline([(58, 82), (88, 82), (88, 98), (66, 104)]), HBL, 'f')],
  dome('back', top=0, w=48, cy=44, soft=True, long=118, flare=6, ends=5) + [L(quad((8, 44), (50, 32), (92, 44)), HBL, 'f', False, False, 3)])

# Susuru Hanawa: pelo verde oliva con dos hojas de brote arriba y los lados en mechones lisos; gafas redondas enormes, dos
# dientes de delante, coloretes y una sonrisa abierta
from chars_scouts_ie2_03 import round_glasses  # noqa: E402
C('susuru-hanawa', 'bajito', P('#7e8237', '#f9cf8d', iris='#3a4a30', shade='#575a25'),
  F(eyes='dot', brows=False, mouth='buck', mouth_y=95, hairline=[(8, 60), (22, 50), (50, 48), (78, 50), (92, 60)]),
  [L(outline([(50, 4), (36, -14), (30, -2, 1), (44, 6)]), 'shade'), L(outline([(50, 4), (64, -14), (70, -2, 1), (56, 6)]), 'shade')] +
  bowl3('front', top=4, side=94, fringe=52, w=2) + round_glasses('front', BLACK, 76, 15, 10, None, 2.4) + blush(88, 24, 4.4),
  [L(outline([(48, 2), (60, -14), (66, -2, 1), (54, 6)]), 'shade')] + bowl3('side', top=4, nape=94, fringe=52, w=2) + round_glasses('side', BLACK),
  [L(outline([(50, 4), (36, -14), (30, -2, 1), (44, 6)]), 'shade'), L(outline([(50, 4), (64, -14), (70, -2, 1), (56, 6)]), 'shade')] + bowl3('back', top=4, nape=96, w=2))

# Suzy Stamp: pelo rojo con flequillo y dos coletas enormes abombadas a los lados con lazos amarillos; ojos rojos, coloretes y
# boca abierta sonriente
YB = _c('#f4c840')
def _puff(cx, s):
    return [L(curls(cx, 18, (18, 20), 5, 0.3)), L(outline([(cx - 6 * s, 10), (cx + 2 * s, -4, 1), (cx + 8 * s, 18), (cx - 2 * s, 26)]), YB, 'f')]
C('suzy-stamp', 'chica', P('#a62203', '#f6e9c3', iris='#c82a2a', shade='#81220c'),
  F(eyes='normal', brows=True, mouth='grin', mouth_y=93, hairline=hl(5, 62, 50, 58, jit=1, seed=2)),
  _puff(-4, 1) + _puff(104, -1) + dome('front', top=4, w=46, cy=44, soft=True, sb=66) + blush(87, 22, 4.2),
  [L(curls(30, 18, (16, 20), 5, 0.3)), L(outline([(26, 10), (32, -4, 1), (40, 18)]), YB, 'f')] + dome('side', top=4, w=46, cy=44, soft=True, nape=84, fr=50),
  _puff(-4, 1) + _puff(104, -1) + dome('back', top=4, w=46, cy=44, soft=True, nape=86))

# Sylvain Elph (portero): elfo de melena rubia larga y lisa con raya en medio, orejas de punta con anillas azules; ojos verdes
# afilados con raya y sonrisa fina
C('sylvain-elph', 'delgado', P('#e2d596', '#f9dcb4', iris='#3a9a5a', shade='#bfb18f'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=94, ears=False, hairline=[(6, 70), (18, 54), (36, 42), (50, 56), (64, 42), (82, 54), (94, 70)], face_front=face(chin=104)),
  dome('front', top=0, w=48, cy=44, soft=True, long=118, flare=2, ends=6) +
  [L(outline([(16, 64), (-2, 50, 1), (12, 80)]), 'skin', 'f'), L(outline([(84, 64), (102, 50, 1), (88, 80)]), 'skin', 'f'),
   L([(8, 66), (12, 74)], BLU, 'f', False, False, 2.6), L([(92, 66), (88, 74)], BLU, 'f', False, False, 2.6)],
  dome('side', top=0, w=48, cy=44, soft=True, long=118, flare=2, fr=52) + ears_pointy('side', h=18),
  ears_pointy('back', h=18) + dome('back', top=0, w=48, cy=44, soft=True, long=118, flare=2, ends=6))

# Synch Rogram: pelo azul en mechones de punta abiertos hacia los lados, con dos mechones finos que le caen por la frente;
# ojos verdes grandes y sonrisa
C('synch-rogram', 'normal', P('#345378', '#fceeca', iris='#3a9a5a', shade='#2d3e51'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=93, hairline=hl(5, 64, 48, 60, jit=2, seed=11)),
  dome('front', top=-2, w=50, cy=44, n=9, amp=12, sweep=0.2, seed=18, sb=76),
  dome('side', top=-2, w=50, cy=44, n=9, amp=12, sweep=0.2, seed=18, nape=88, fr=50),
  dome('back', top=-2, w=50, cy=44, n=9, amp=12, sweep=0.2, seed=18, nape=88))

# Taiji Kinetsuki (portero): pelo negro recogido en una coleta alta y dos cortinas lisas a los lados de la cara; cinta blanca
# con una placa negra en la frente, pintura roja alrededor de los ojos y nariz larga; cara alargada morena
RP = _c('#c83a2a')
_tf, _ts = eyes_f(_c('#4a4a5a'), kind='sharp', brows=BLACK)
C('taiji-kinetsuki', 'delgado', P('#2a2628', '#eba764', iris='#4a4a5a', shade='#1c1817'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=98, face_front=face(chin=108, jaw=-1), hairline=[(10, 58), (20, 48), (50, 46), (80, 48), (90, 58)], nose=(50, 88, 3)),
  dome('front', top=4, w=44, cy=42, sb=60) + [L(outline([(44, 6), (48, -14), (56, -18, 1), (56, 6)]), 'mid', 'b'),
   L(outline([(8, 50), (16, 50), (16, 104), (6, 108)]), 'mid', 'f'), L(outline([(84, 50), (92, 50), (94, 108), (84, 104)]), 'mid', 'f'),
   L(outline([(14, 46), (86, 46), (86, 56), (14, 56)]), WHITE, 'f'), L(outline([(40, 47), (60, 47), (60, 55), (40, 55)]), BLACK, 'f', False),
   L(blob([(20, 62), (44, 62), (50, 70), (56, 62), (80, 62), (80, 86), (56, 82), (50, 90), (44, 82), (20, 86)], 4), RP, 'f', False),
   L(outline([(46, 64), (54, 64), (54, 92), (46, 92)]), _c('#d8904a'), 'f', False)] + _tf,
  dome('side', top=4, w=44, cy=42, nape=84, fr=44) + [L(outline([(36, 6), (20, -10), (10, -6, 1), (26, 10)]), 'mid', 'b'),
   L(outline([(30, 46), (88, 44), (88, 54), (30, 56)]), WHITE, 'f'), L(blob([(66, 62), (88, 62), (88, 86), (66, 86)], 4), RP, 'f', False)] + _ts,
  dome('back', top=4, w=44, cy=42, nape=84) + [L(outline([(10, 48), (90, 48), (90, 56), (10, 56)]), WHITE, 'f'),
   L(outline([(44, 6), (56, 6), (58, 30), (50, 40, 1), (42, 30)]), 'mid', 'f')])

# Tey Liadika: melena castaño muy oscuro enorme y ondulada, recogida arriba en un remolino y echada hacia un lado, que le tapa
# un ojo y cae en ondas hasta el hombro; piel morena, ojo azul
C('tey-liadika', 'chica', P('#2e221c', '#c29568', iris='#3a6aa8', shade='#1f1917'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=93, hairline=[(6, 66), (18, 48), (40, 40), (64, 42), (84, 50), (94, 64)]),
  dome('front', top=-6, w=48, cy=42, soft=True, long=104, flare=10) +
  [L(outline([(30, 4), (44, -22), (62, -8), (56, 6)]), 'mid', 'b'),
   L(outline([(12, 52), (30, 36), (56, 38), (54, 62), (44, 84), (30, 96), (12, 120, 1), (16, 96), (14, 72)]), 'mid', 'f')],
  dome('side', top=-6, w=48, cy=42, soft=True, long=104, flare=10, fr=54) + [L(outline([(30, 4), (36, -22), (56, -10), (50, 6)]), 'mid')],
  dome('back', top=-6, w=48, cy=42, soft=True, long=104, flare=10) + [L(outline([(30, 4), (44, -22), (62, -8), (56, 6)]), 'mid')])

# Tezcat's Sister: pelo gris azulado oscuro corto con flequillo de mechones; pendientes largos de bolitas rojas y blancas,
# pecas, ojos grandes y sonrisa
C('tezcat-s-sister', 'chica', P('#515266', '#f6bc84', iris='#3a3a5a', shade='#3e3741'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=93, hairline=hl(5, 62, 48, 58, jit=2, seed=12)),
  dome('front', top=2, w=46, cy=44, soft=True, sb=70) + freckles(84, 24) +
  [L(ell(14, 90, 2.4, 2.4), WHITE, 'f'), L(ell(14, 96, 3, 3), _c('#c83a2a'), 'f'), L(ell(86, 90, 2.4, 2.4), WHITE, 'f'), L(ell(86, 96, 3, 3), _c('#c83a2a'), 'f')],
  dome('side', top=2, w=46, cy=44, soft=True, nape=82, fr=50) + [L(ell(46, 90, 2.4, 2.4), WHITE, 'f'), L(ell(46, 96, 3, 3), _c('#c83a2a'), 'f')],
  dome('back', top=2, w=46, cy=44, soft=True, nape=84))

# Tokichiro Kinoshita (modelo 3D): pelo castaño alborotado con mechones por la cara, un mechón largo en arco por encima de la
# cabeza y una coleta baja atada con una cinta roja; cicatriz en la mejilla y sonrisa
C('tokichiro-kinoshita', 'normal', P('#58442b', '#eca966', iris='#1e1a1a', shade='#463220', deep='#372415'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=hl(5, 64, 46, 62, lean=1, jit=3, seed=13)),
  dome('front', top=-2, w=48, cy=44, n=7, amp=10, seed=19, long=98, flare=10, ends=3) +
  [L(quad((30, 8), (50, -26), (72, 4)), 'mid', 'b', False, False, 4), L([(60, 86), (68, 82)], _c('#b0603a'), 'f', False, False, 1.4)],
  dome('side', top=-2, w=48, cy=44, n=7, amp=10, seed=19, nape=86, fr=50) +
  [L(quad((70, 8), (44, -26), (20, 4)), 'mid', 'b', False, False, 4), L(outline([(14, 74), (24, 76), (18, 116), (8, 124, 1), (8, 100)]), 'mid'),
   L(ell(18, 78, 4, 3), _c('#c82a2a'), 'f')],
  dome('back', top=-2, w=48, cy=44, n=7, amp=10, seed=19, nape=86) +
  [L(outline([(44, 78), (56, 78), (54, 112), (50, 122, 1), (46, 112)]), 'mid', 'f'), L(ell(50, 80, 5, 3), _c('#c82a2a'), 'f')])

# Toshihito Ishida: pelo azul marino oscuro en pinchos peinados hacia atrás y hacia arriba, con las sienes en punta; cejas
# gruesas fruncidas y boca apretada
C('toshihito-ishida', 'normal', P('#1d242d', '#f9bc7e', iris='#1e1a1a', shade='#141414'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(8, 62), (18, 46), (30, 40), (50, 36), (70, 40), (82, 46), (92, 62)]),
  dome('front', top=-8, w=50, cy=42, n=8, amp=14, sweep=0.0, seed=20, sb=80),
  dome('side', top=-8, w=50, cy=42, n=8, amp=14, sweep=-0.6, seed=20, nape=90, fr=46),
  dome('back', top=-8, w=50, cy=42, n=8, amp=14, seed=20, nape=92))

# Toshiie Maeda (modelo 3D): pelo granate liso con un moño pequeño arriba, flequillo de mechones y los lados cayendo hasta la
# mandíbula; ojos grises grandes con raya y sonrisa
C('toshiie-maeda', 'normal', P('#582b31', '#f4c18c', iris='#7a7a80', shade='#462226', deep='#381819'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=hl(5, 64, 48, 58, jit=2, seed=14)),
  dome('front', top=2, w=48, cy=44, n=4, amp=6, seed=21, long=100, flare=6, ends=4) + [L(ell(50, -6, 7, 6), 'mid', 'b')],
  dome('side', top=2, w=48, cy=44, n=4, amp=6, seed=21, long=100, flare=6, fr=52) + [L(ell(40, -4, 7, 6), 'mid'), L([(34, 0), (44, 2)], _c('#c8c8c8'), 'f', False, False, 1.6)],
  dome('back', top=2, w=48, cy=44, n=4, amp=6, seed=21, long=100, flare=6, ends=4) + [L(ell(50, -6, 7, 6), 'mid')])

# Trigo Teah (portero): cara alargada morena; pelo azul marino peinado hacia atrás con un mechón enroscado en gancho, dos
# mechones largos junto a las orejas y la barba trenzada en punta; ojos de cejas arqueadas
C('trigo-teah', 'delgado', P('#314253', '#be854e', iris='#1e1a1a', shade='#2a313a'),
  F(eyes='round', brows='angry', mouth='smile', mouth_y=96, face_front=face(chin=108), hairline=[(10, 60), (20, 44), (36, 36), (50, 42), (64, 36), (80, 44), (90, 60)]),
  dome('front', top=2, w=46, cy=44, sb=66) +
  [L(outline([(56, 6), (72, -14), (90, -12), (84, -2), (74, -6), (66, 10)]), 'mid', 'b'),
   side_lock(14, 56, 100, wd=8), side_lock(86, 56, 100, wd=8),
   L(outline([(30, 96), (50, 104), (70, 96), (60, 110), (54, 112), (52, 124, 1), (48, 112), (40, 110)]), 'mid', 'f')],
  dome('side', top=2, w=46, cy=44, nape=86, fr=44) + [L(outline([(40, 6), (24, -16), (6, -14), (12, -4), (22, -8), (32, 10)]), 'mid'),
   L(outline([(70, 98), (88, 96), (88, 108), (84, 122, 1), (76, 108)]), 'mid', 'f')],
  dome('back', top=2, w=46, cy=44, nape=86) + [L(outline([(56, 6), (72, -14), (90, -12), (84, -2), (74, -6), (66, 10)]), 'mid')])

# Utamaro Kusuri: pelo rojo anaranjado en pinchos revueltos sobre una cinta azul marino en la frente; patillas que bajan hasta
# una barba de mentón, cicatriz en la frente y ceño fruncido
NAV = _c('#262236')
C('utamaro-kusuri', 'normal', P('#ac4824', '#eca663', iris='#1e1a1a', shade='#86391e'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=94, hairline=[(8, 66), (18, 58), (50, 58), (82, 58), (92, 66)]),
  dome('front', top=-10, w=50, cy=40, n=10, amp=12, seed=22, sb=90) +
  [L(outline([(10, 44), (50, 40), (90, 44), (90, 54), (50, 50), (10, 54)]), NAV, 'f'),
   L(blob([(18, 80), (26, 96), (40, 106), (50, 108), (60, 106), (74, 96), (82, 80), (78, 96), (60, 102), (50, 104), (40, 102), (22, 96)], 4), 'mid', 'f', False),
   L([(54, 52), (58, 66)], _c('#c06838'), 'f', False, False, 1.2)],
  dome('side', top=-10, w=50, cy=40, n=10, amp=12, seed=22, nape=86, fr=48) + [L(outline([(20, 40), (90, 38), (90, 48), (20, 50)]), NAV, 'f')],
  dome('back', top=-10, w=50, cy=40, n=10, amp=12, seed=22, nape=86) + [L(outline([(6, 46), (94, 46), (94, 56), (6, 56)]), NAV, 'f')])

# Van Yamano (modelo 3D): pelo castaño en mechones de punta revueltos con dos pinchos que salen arriba y las puntas de los
# lados hacia fuera; ojos grandes y sonrisa
C('van-yamano', 'normal', P('#47351a', '#f8e1ca', iris='#3a3a4a', shade='#362518'),
  F(eyes='normal', brows='angry', mouth='smile', mouth_y=93, hairline=hl(5, 64, 50, 62, lean=1, jit=3, seed=15)),
  dome('front', top=-4, w=52, cy=44, n=10, amp=10, sweep=0.3, seed=23, sb=82) + [L(outline([(42, 2), (46, -22, 1), (52, 0)]), 'mid', 'b')],
  dome('side', top=-4, w=52, cy=44, n=10, amp=10, sweep=0.3, seed=23, nape=92, fr=50) + [L(outline([(30, 4), (24, -20, 1), (40, 2)]), 'mid')],
  dome('back', top=-4, w=52, cy=44, n=10, amp=10, sweep=0.3, seed=23, nape=94, back_n=12))

# Vic Longboat: grandullón tapado por una capucha de pelo naranja rojizo que le rodea la cara y una barba enorme con dos
# trenzas atadas; ojos cansados de párpado caído
from chars_scouts_ie1_10 import nose_tri  # noqa: E402,F401
C('vic-longboat', 'corpulento', P('#aa2d06', '#efb782', iris='#1e1a1a', shade='#84270d'),
  F(eyes='closed', brows=False, mouth='none', ears=False, hairline=False, face_front=face(w=2, chin=104), nose=(50, 86, 4)),
  hood('front', 'mid', top=-6, w=4, low=104, face_hole=[(26, 96), (22, 74), (28, 58), (50, 54), (72, 58), (78, 74), (74, 96), (50, 100)]) +
  [L([(30, 70), (44, 72)], OUTC, 'f', False, False, 2.4), L([(56, 72), (70, 70)], OUTC, 'f', False, False, 2.4),
   L(outline([(12, 84), (30, 84), (40, 90), (50, 88), (60, 90), (70, 84), (88, 84), (94, 104), (80, 124), (50, 130), (20, 124), (6, 104)]), 'mid', 'f'),
   L(outline([(2, 116), (10, 116), (8, 132), (0, 136, 1)]), 'mid', 'f'), L(outline([(98, 116), (90, 116), (92, 132), (100, 136, 1)]), 'mid', 'f'),
   L([(3, 124), (9, 124)], _c('#3a4a8a'), 'f', False, False, 2.4), L([(91, 124), (97, 124)], _c('#3a4a8a'), 'f', False, False, 2.4)],
  hood('side', 'mid', top=-6, w=4) + [L(outline([(60, 84), (90, 84), (94, 104), (84, 124), (60, 120), (52, 100)]), 'mid', 'f')],
  hood('back', 'mid', top=-6, w=4, low=104))

# Wade Posey: pelo amarillo en mechones de punta revueltos con un pincho arriba; gafas de visera azul marino en zigzag que le
# tapan los ojos; piel morena y sonrisa de dientes
VIZ = _c('#1e2a6a')
C('wade-posey', 'normal', P('#fdcc5c', '#cc955e', iris='#1e1a1a', shade='#e0a840'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=94, hairline=hl(5, 64, 48, 62, jit=3, seed=16)),
  dome('front', top=-6, w=52, cy=44, n=11, amp=12, seed=24, sb=78) + [L(outline([(48, 2), (54, -24, 1), (60, 2)]), 'mid', 'b'),
   L(outline([(12, 66), (32, 64), (50, 70), (68, 62), (90, 64), (84, 82), (64, 80), (50, 76), (36, 82), (16, 80)]), VIZ, 'f'),
   L(outline([(24, 68), (40, 68), (34, 72)]), _c('#6a8ad8'), 'f', False)],
  dome('side', top=-6, w=52, cy=44, n=11, amp=12, seed=24, nape=88, fr=52) + [L(outline([(62, 66), (92, 62), (90, 80), (66, 80)]), VIZ, 'f')],
  dome('back', top=-6, w=52, cy=44, n=11, amp=12, seed=24, nape=88) + [L(quad((6, 70), (50, 76), (94, 70)), VIZ, 'f', False, False, 3)])

# Will Reynard: melena larga ondulada rubio crema que le cae por los hombros, con un mechón por la frente; ojos verdosos
# afilados y gesto serio
C('will-reynard', 'delgado', P('#fcf2cc', '#f4d0b0', iris='#6a9a8a', shade='#cec8ae', deep='#a18370'),
  F(eyes='sharp', brows=True, mouth='line', mouth_y=94, hairline=[(6, 66), (18, 48), (36, 42), (52, 54), (66, 42), (84, 50), (94, 66)]),
  dome('front', top=-4, w=50, cy=44, soft=True, long=120, flare=12, ends=4, n=5, amp=5, seed=25) +
  [L(outline([(42, 34), (54, 30), (56, 56), (48, 72, 1), (46, 50)]), 'mid', 'f')] +
  [L(curls(x, 104, (8, 10), 4), 'mid', 'f') for x in (8, 92)],
  dome('side', top=-4, w=50, cy=44, soft=True, long=120, flare=12, fr=52, n=5, amp=5, seed=25),
  dome('back', top=-4, w=50, cy=44, soft=True, long=120, flare=12, ends=4, n=5, amp=5, seed=25))

# Winnie Hull: melena morada muy oscura enorme en ondas gruesas que se abren a los lados como alas; pintura roja en espiral en
# las mejillas y la frente, ojos rojos y una sonrisa con colmillo
WP = _c('#c8303a')
C('winnie-hull', 'chica', P('#372e43', '#e1d2bc', iris='#c82a3a', shade='#251e24'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=93, hairline=[(6, 64), (18, 48), (36, 42), (52, 46), (68, 42), (84, 48), (94, 64)]),
  dome('front', top=-8, w=50, cy=42, soft=True, long=104, flare=18, n=6, amp=10, seed=26, ends=4) +
  [L(outline([(10, 40), (-10, 20), (-14, 46, 1), (2, 60)]), 'mid', 'b'), L(outline([(90, 40), (110, 20), (114, 46, 1), (98, 60)]), 'mid', 'b'),
   L(quad((22, 84), (28, 78), (34, 86)), WP, 'f', False, False, 1.6), L(quad((78, 84), (72, 78), (66, 86)), WP, 'f', False, False, 1.6),
   L(quad((44, 56), (50, 52), (56, 56)), WP, 'f', False, False, 1.4), L(outline([(54, 94), (57, 94), (55.5, 98, 1)]), WHITE, 'f')],
  dome('side', top=-8, w=50, cy=42, soft=True, long=104, flare=18, fr=52, n=6, amp=10, seed=26),
  dome('back', top=-8, w=50, cy=42, soft=True, long=104, flare=18, n=6, amp=10, seed=26, ends=4) +
  [L(outline([(10, 40), (-10, 20), (-14, 46, 1), (2, 60)]), 'mid'), L(outline([(90, 40), (110, 20), (114, 46, 1), (98, 60)]), 'mid')])

# Wowah Zumu: pelo azul marino que se abre a los lados en dos alas en punta; adornos largos a rayas amarillas y rojas que le
# cuelgan junto a las mejillas; piel morena, ojos grandes y sonrisa de dientes
YEL, RDD = _c('#e8c030'), _c('#c83a2a')
def _orn(x):
    return [L(outline([(x - 3, 70), (x + 3, 70), (x + 3, 104), (x - 3, 104)]), YEL, 'f')] + [L([(x - 3, y), (x + 3, y)], RDD, 'f', False, False, 2.4) for y in (76, 84, 92, 100)]
C('wowah-zumu', 'chica', P('#141a62', '#b08c5f', iris='#3a3a3a', shade='#121945'),
  F(eyes='normal', brows=False, mouth='grin', mouth_y=93, hairline=[(8, 62), (20, 50), (50, 46), (80, 50), (92, 62)]),
  dome('front', top=0, w=46, cy=44, soft=True, sb=66) +
  [L(outline([(14, 34), (-6, 22), (-12, 14, 1), (-2, 44), (12, 58)]), 'mid', 'b'), L(outline([(86, 34), (106, 22), (112, 14, 1), (102, 44), (88, 58)]), 'mid', 'b')] +
  _orn(14) + _orn(86),
  dome('side', top=0, w=46, cy=44, soft=True, nape=84, fr=50) + [L(outline([(30, 30), (6, 16), (0, 8, 1), (6, 40), (24, 52)]), 'mid')] +
  [L(outline([(43, 70), (49, 70), (49, 104), (43, 104)]), YEL, 'f')],
  dome('back', top=0, w=46, cy=44, soft=True, nape=86) +
  [L(outline([(14, 34), (-6, 22), (-12, 14, 1), (-2, 44), (12, 58)]), 'mid'), L(outline([(86, 34), (106, 22), (112, 14, 1), (102, 44), (88, 58)]), 'mid')])

# Xander Ice: pelo amarillo en pinchos altísimos echados a un lado; gafas enormes redondas de cristal verde con montura blanca
# y una sonrisa de dientes
GLE = _c('#3a8a4a')
C('xander-ice', 'bajito', P('#fcd565', '#eee4c6', iris='#1e1a1a', shade='#d8a840'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=94, big_ears=1, hairline=hl(4, 62, 50, 58, lean=2, jit=2, seed=17)),
  dome('front', top=-18, w=50, cy=38, n=7, amp=22, sweep=0.7, seed=27, sb=66) + round_glasses('front', _c('#f0ece0'), 76, 14, 8.5, GLE, 3.0),
  dome('side', top=-18, w=50, cy=38, n=7, amp=22, sweep=0.7, seed=27, nape=86, fr=50) + round_glasses('side', _c('#f0ece0'), lens=GLE, w=3.0),
  dome('back', top=-18, w=50, cy=38, n=7, amp=22, sweep=0.7, seed=27, nape=86) + [L(quad((6, 72), (50, 78), (94, 72)), _c('#f0ece0'), 'f', False, False, 2.4)])

# Yoshinobu Tokugawa: cara alargada; pelo negro recogido bajo un sombrero de corte negro alto (eboshi) con el ala estrecha,
# atado con una cinta blanca bajo la barbilla; ojos afilados y media sonrisa
EB = _c('#1e1e22')
def _eboshi(view):
    if view == 'side':
        return [L(outline([(36, 6), (40, -36), (62, -36), (62, 6)]), EB), L(outline([(20, 2), (82, -2), (82, 4), (20, 8)]), EB)]
    return [L(outline([(38, 6), (40, -36), (60, -36), (62, 6)]), EB), L(outline([(12, 0), (88, 0), (88, 6), (12, 6)]), EB)]
C('yoshinobu-tokugawa', 'delgado', P('#141818', '#fbd28e', iris='#3a2a20', shade='#0c0e0e'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=96, face_front=face(chin=106), hairline=[(10, 60), (18, 44), (34, 36), (50, 34), (66, 36), (82, 44), (90, 60)]),
  dome('front', top=10, w=44, cy=44, sb=64) + _eboshi('front') +
  [L([(16, 44), (20, 86), (40, 104)], WHITE, 'f', False, False, 1.2), L([(84, 44), (80, 86), (60, 104)], WHITE, 'f', False, False, 1.2)],
  dome('side', top=10, w=44, cy=44, nape=84, fr=44) + _eboshi('side') + [L([(52, 40), (60, 82), (70, 102)], WHITE, 'f', False, False, 1.2)],
  dome('back', top=10, w=44, cy=44, nape=84) + _eboshi('back'))

# Yuki Oolong: pelo azul petróleo oscuro recogido arriba en un moño con una peineta rosa, flequillo partido y dos mechones
# lisos que bajan hasta la mandíbula; ojos lilas afilados con pestañas y sonrisa
COMB = _c('#f09aa8')
C('yuki-oolong', 'chica', P('#375368', '#f9bc7e', iris='#8a7ab8', shade='#2e3945'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=93, hairline=[(8, 64), (18, 48), (36, 40), (50, 48), (64, 40), (82, 48), (92, 64)]),
  dome('front', top=2, w=46, cy=44, soft=True, sb=92) + [L(ell(50, -4, 14, 9), 'mid', 'b'), L(quad((38, -4), (50, -14), (62, -4)), COMB, 'f', False, False, 3)],
  dome('side', top=2, w=46, cy=44, soft=True, nape=84, fr=50) + [L(ell(40, -2, 12, 9), 'mid'), L(quad((30, -4), (40, -12), (52, -4)), COMB, 'f', False, False, 3)],
  dome('back', top=2, w=46, cy=44, soft=True, nape=86) + [L(ell(50, -4, 14, 9), 'mid'), L(quad((38, -4), (50, -14), (62, -4)), COMB, 'f', False, False, 3)])

# Zato Memmor: pelo gris verdoso oscuro con un tupé enrollado hacia atrás arriba, un mechón como un cuerno a un lado y el
# flequillo revuelto sobre los ojos; ojos verdes afilados y boca seria
C('zato-memmor', 'normal', P('#5a6963', '#f7bc80', iris='#4a9a5a', shade='#444440'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=94, hairline=hl(6, 64, 50, 66, lean=1, jit=3, seed=18)),
  dome('front', top=-2, w=48, cy=44, n=6, amp=6, soft=True, seed=28, sb=80) +
  [L(outline([(30, 12), (40, -8), (66, -10), (72, 6), (58, 2), (44, 14)]), 'shade', 'b'), L(outline([(84, 16), (96, 2), (100, -6, 1), (92, 22)]), _c('#9ac0a0'), 'b')],
  dome('side', top=-2, w=48, cy=44, n=6, amp=6, soft=True, seed=28, nape=88, fr=56) + [L(outline([(30, 6), (50, -10), (74, -4), (60, 10)]), 'shade')],
  dome('back', top=-2, w=48, cy=44, n=6, amp=6, soft=True, seed=28, nape=88) + [L(outline([(30, 12), (40, -8), (66, -10), (72, 6), (58, 2), (44, 14)]), 'shade')])
