"""Ojeadores de IE2 (scouts-ie2), tanda 02: dibujados a partir de su retrato de Victory Road (casi ninguno tiene modelo 3D);
claves 'scouts-ie2:<id>'. El perfil y la espalda se deducen de cómo cae cada peinado.

Reutiliza las ayudas de los ojeadores de IE1 (dome/hl/face de la tanda 09, bowl/skull/gafas de la 03, crop de Nikogawa)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars import longhair, messy  # noqa: F401
from chars_scouts_ie1_03 import blush, bowl, eyes_custom, freckles, goggles, round_specs, shades, side_brow, side_eye_custom, skull, thick_brows  # noqa: F401
from chars_scouts_ie1_09 import dome, face, face_side, hl, mark  # noqa: F401
from chars_scouts_ie1_02 import mir  # noqa: F401
from chars_vr_nikogawa import crop  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401

K = 'scouts-ie2:'
WHITE = (250, 250, 250, 255)
BLACK = (24, 18, 20, 255)
MOUTH = (130, 70, 50, 255)


def c_(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5)) + (255,)


def C(pid, body, palette, f, front, side, back):
    """Guarda el personaje; el nacimiento del pelo en lista baja por el borde de la cara (si no, su raya cruza los lados)."""
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[K + pid] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def F(**k):
    d = {'eyes': 'normal', 'mouth': 'line'}
    d.update(k)
    return d


def fr(pts, c='mid'):
    """Mechón por delante de la cara."""
    return L(outline(pts), c, 'f')


def specs(view, c, y=76, rx=9, ry=7, w=1.8):
    return round_specs(view, c, y, 14, rx, ry, w)


def o_mouth(y=94, r=3.0, c=(110, 50, 44, 255)):
    return [L(ell(50, y, r, r * 1.1), c, 'f', True)]


def teeth(y=93, w=12, h=6):
    """Sonrisa ancha enseñando los dientes."""
    return [L(blob([(50 - w, y - 2), (50 + w, y - 2), (50 + w * 0.7, y + h), (50 - w * 0.7, y + h)], 4), WHITE, 'f', True),
            L([(50 - w * 0.85, y + 1.5), (50 + w * 0.85, y + 1.5)], OUTC, 'f', False, False, 0.9)]


def nose(y=86, w=3.0, c=None):
    return [L([(50, y - 5), (50 - w, y + 1), (50, y + 1.5)], c or OUTC, 'f', False, False, 1.2)]


# ---------------------------------------------------------------------------------------------------------- jugadores

# Bomber Pikes (portero): cabezón de cara enorme y redonda con papada; casquete de pelo gris pardo con unas gafas de
# soldador verdes de cristales naranjas subidas a la frente y dos mechones castaños de punta junto a las sienes; sin ojos a
# la vista, morro de nariz grande y boquita redonda
GOG, ORA = c_('#5e7a5e'), c_('#e8862a')
C('bomber-pikes', 'corpulento', pal('#6a655c', '#dda255', shade='#55514a', deep='#3a3632', tuft='#3a2c26'),
  F(eyes='none', brows=False, mouth='none', hairline=False, face_front=face(w=7, chin=108, jaw=5), ear_out=6),
  [skull(), L(blob([(24, 40), (28, 20), (50, 12), (72, 20), (76, 40), (50, 36)], 8), 'mid'),
   L(blob([(56, 16), (72, 20), (76, 38), (64, 36)], 6), 'shade', 'b', False)] +
  [L(outline([(16, 52), (4, 42, 1), (14, 40), (8, 32, 1), (22, 38)]), 'tuft'), L(outline([(84, 52), (96, 42, 1), (86, 40), (92, 32, 1), (78, 38)]), 'tuft'),
   L(ell(38, 44, 9, 8), GOG, 'f', True), L(ell(62, 44, 9, 8), GOG, 'f', True), L(ell(38, 44, 4.5, 4), ORA, 'f', True), L(ell(62, 44, 4.5, 4), ORA, 'f', True),
   L(blob([(42, 82), (58, 82), (60, 92), (50, 95), (40, 92)], 5), c_('#c88a46'), 'f', True), L(ell(46, 89, 1.4, 1.2), OUTC, 'f', False), L(ell(54, 89, 1.4, 1.2), OUTC, 'f', False)]
  + o_mouth(101, 2.4),
  [L(blob([(30, 14), (56, 10), (76, 22), (74, 36), (40, 40), (24, 34)], 8), 'mid')] + [L(outline([(52, 54), (60, 40, 1), (64, 50)]), 'tuft'), L(ell(76, 42, 7, 7), GOG, 'f', True), L(ell(78, 42, 3.6, 3.4), ORA, 'f', True),
                                  L([(70, 44), (30, 40)], GOG, 'f', False, False, 3), L(blob([(84, 80), (95, 84), (94, 94), (84, 94)], 4), c_('#c88a46'), 'f', True)],
  [L(blob([(24, 44), (26, 24), (50, 14), (74, 24), (76, 44), (50, 50)], 8), 'mid')] + [L(quad((8, 44), (50, 50), (92, 44)), GOG, 'f', False, False, 3.2),
                                  L(outline([(16, 54), (4, 44, 1), (18, 42)]), 'tuft'), L(outline([(84, 54), (96, 44, 1), (82, 42)]), 'tuft')])

# Boomer Smolen (portero): pelo castaño oscuro revuelto con un pincho de punta arriba y un mechón largo que le cae por
# encima del ojo derecho; ojos grises azulados y media sonrisa
C('boomer-smolen', 'normal', pal('#6d413b', '#fbc273', iris='#6a7a90', shade='#542d25', deep='#3a1e18'),
  F(eyes='normal', brows=True, mouth='smile', hairline=hl(5, 64, 52, 62, jit=2, seed=4)),
  dome('front', top=6, w=46, cy=46, n=8, amp=9, sweep=0.3, sb=68, seed=12) + [fr([(40, 40), (60, 44), (54, 70, 1), (46, 52)]), fr([(52, 6), (70, -12, 1), (62, 10)])],
  dome('side', top=6, w=46, cy=46, n=8, amp=9, sweep=0.3, nape=84, fr=50, seed=12) + [fr([(66, 40), (88, 50), (80, 66, 1), (74, 52)])],
  dome('back', top=6, w=46, cy=46, n=8, amp=9, sweep=0.3, nape=84, seed=12))

# Brenda Brandish: chica de pelo naranja intenso, media melena hasta las orejas con flequillo de mechones; ojos castaños
# grandes, piel muy clara y sonrisa
C('brenda-brandish', 'chica', pal('#f28505', '#fdefc9', iris='#8a3a14', shade='#b55c11', deep='#76350a'),
  F(eyes='big', brows=True, mouth='smile', hairline=hl(6, 70, 52, 64, lean=-2, jit=2, seed=7)),
  dome('front', top=2, w=48, cy=46, n=7, amp=7, soft=True, sb=76, seed=8) + [fr([(30, 42), (52, 40), (40, 66, 1)])],
  dome('side', top=2, w=48, cy=46, n=7, amp=7, soft=True, nape=86, fr=54, seed=8),
  dome('back', top=2, w=48, cy=46, n=7, amp=7, soft=True, nape=86, seed=8))

# Bryan Klamm: pelo morado grisáceo oscuro de pinchos revueltos que le cae en mechones por la frente; gafas redondas
# doradas finas y ojos verdes
C('bryan-klamm', 'normal', pal('#635566', '#f5bb80', iris='#2a9a7a', shade='#4b3c44', deep='#352a30'),
  F(eyes='normal', brows=True, mouth='line', hairline=hl(6, 64, 50, 62, jit=3, seed=9)),
  dome('front', top=4, w=47, cy=46, n=10, amp=8, sweep=0.2, sb=68, seed=21) + specs('front', c_('#c89a3a')),
  dome('side', top=4, w=47, cy=46, n=10, amp=8, sweep=0.2, nape=84, fr=50, seed=21) + specs('side', c_('#c89a3a')),
  dome('back', top=4, w=47, cy=46, n=10, amp=8, sweep=0.2, nape=84, seed=21))

# Cale Sticklin: casco amarillo anaranjado con una franja verde oscuro en medio y dos picos que salen a los lados como
# orejas; unas gafas blancas redondas enormes, nariz naranja grande en pico y la boca recta
HEL, STR, NOS = c_('#dd9a04'), c_('#3c480c'), c_('#e8804a')


def _sticklin(view):
    if view == 'front':
        return [L(outline([(16, 70), (12, 40), (-4, 22, 1), (20, 28), (34, 10), (50, 6), (66, 10), (80, 28), (104, 22, 1), (88, 40), (84, 70), (50, 66)]), HEL),
                L(outline([(44, 7), (56, 7), (54, 46), (50, 52, 1), (46, 46)]), STR, 'b', False),
                L(ell(38, 74, 8, 8), c_('#f4ecd8'), 'f', True), L(ell(62, 74, 8, 8), c_('#f4ecd8'), 'f', True),
                L(blob([(44, 80), (56, 80), (58, 96), (50, 100), (42, 96)], 6), NOS, 'f', True)]
    if view == 'side':
        return [L(outline([(80, 70), (88, 46), (82, 22), (60, 6), (36, 6), (14, 18), (4, 44), (8, 72), (30, 80), (50, 74)]), HEL),
                L(outline([(40, 6), (54, 4), (70, 12), (60, 16), (48, 10)]), STR, 'b', False),
                L(outline([(30, 18), (12, 2, 1), (40, 14)]), HEL),
                L(ell(82, 74, 6, 8), c_('#f4ecd8'), 'f', True), L(blob([(86, 80), (98, 88), (96, 98), (86, 96)], 6), NOS, 'f', True)]
    return [L(outline([(12, 76), (8, 40), (-6, 22, 1), (18, 28), (32, 10), (50, 6), (68, 10), (82, 28), (106, 22, 1), (92, 40), (88, 76), (50, 82)]), HEL),
            L(outline([(44, 7), (56, 7), (56, 80), (44, 80)]), STR, 'b', False)]


C('cale-sticklin', 'normal', pal('#dd9a04', '#f9bb7b', shade='#b07a04'),
  F(eyes='none', brows=False, mouth='line', mouth_y=104, hairline=False, face_front=face(chin=108)),
  _sticklin('front'), _sticklin('side'), _sticklin('back'))

# Callie Graffy: chica de pelo rosa fucsia corto en casquete con mechones finos que le caen por delante de las orejas, dos
# horquillas amarillas en aspa a los lados, flequillo de mechones; ojos grandes y boca pequeña seria
YX = c_('#f2d23a')


def _x(cx, cy):
    return [L([(cx - 3, cy - 3), (cx + 3, cy + 3)], YX, 'f', False, False, 1.8), L([(cx - 3, cy + 3), (cx + 3, cy - 3)], YX, 'f', False, False, 1.8)]


C('callie-graffy', 'chica', pal('#d3627b', '#f5bf93', iris='#2a1a1a', shade='#a24e53', deep='#7a3440'),
  F(eyes='big', brows=True, mouth='frown', hairline=hl(5, 66, 50, 64, lean=2, jit=2, seed=3)),
  dome('front', top=2, w=47, cy=46, sb=74, seed=2) + [fr([(14, 62), (22, 60), (20, 98, 1), (12, 80)]), fr([(86, 62), (78, 60), (80, 98, 1), (88, 80)]),
                                                     fr([(42, 40), (60, 44), (52, 66, 1)])] + _x(24, 62) + _x(76, 62),
  dome('side', top=2, w=47, cy=46, nape=80, fr=52, seed=2) + [fr([(66, 56), (74, 56), (72, 92, 1), (64, 74)])] + _x(58, 60),
  dome('back', top=2, w=47, cy=46, nape=80, seed=2) + _x(16, 62) + _x(84, 62))

# Callum Biddy: piel morena, pelo gris verdoso muy claro alborotado en mechones que se abren a los lados, con un mechón en
# zigzag que le baja por la frente; ojos blancos entornados con cejas gruesas y una sonrisa enorme de dientes
C('callum-biddy', 'normal', pal('#afcbc6', '#ae8b72', shade='#879e9a', deep='#5e706c'),
  F(eyes='sharp', brows=False, mouth='none', hairline=[(10, 66), (24, 52), (40, 56), (50, 50), (60, 56), (76, 52), (90, 66)]),
  messy('front', amp=13, n=10, seed=33, lo=62, sweep=0.2) +
  [L([(50, 50), (46, 58), (54, 64), (48, 72), (52, 78)], 'mid', 'f', False, False, 3.2), L([(50, 50), (46, 58), (54, 64), (48, 72), (52, 78)], 'shade', 'f', False, False, 1.2)]
  + thick_brows(64, BLACK, 3.4, 14, 1.0, 12) + teeth(93, 13, 6),
  messy('side', amp=13, n=10, seed=33, lo=62) + side_brow(64, BLACK, 3.4, 1.0) +
  [L(blob([(78, 90), (90, 89), (89, 97), (80, 97)], 4), WHITE, 'f', True)],
  messy('back', amp=13, n=10, seed=33, lo=62, nape=88))

# Camilla Textor: chica de pelo lila con raya en medio, liso y largo hasta los hombros que le enmarca la cara; piel clara,
# orejas de punta, ojos rasgados de pícara y sonrisa
C('camilla-textor', 'chica', pal('#a395b4', '#fceab8', iris='#7a3a4a', shade='#746277', deep='#584953'),
  F(eyes='sharp', brows=False, mouth='smile', ear_out=3, hairline=[(12, 70), (22, 46), (38, 34), (50, 32), (62, 34), (78, 46), (88, 70)]),
  longhair('front', length=110, flare=6, part=True, ends=3),
  longhair('side', length=110, flare=6, ends=3),
  longhair('back', length=110, flare=6, ends=4))

# Candice Mell: pelo verde hierba de pinchos alborotados que cae en mechones por los lados de la cara; lleva una máscara gris
# blanquecina que le tapa la cara entera, con dos agujeros ovalados rasgados para los ojos
MASK = c_('#dbe3de')


def _mell_mask(view):
    if view == 'front':
        out = [L(blob([(20, 54), (50, 46), (80, 54), (82, 80), (66, 100), (50, 104), (34, 100), (18, 80)], 8), MASK, 'f', True)]
        for cx, s in ((37, 1), (63, -1)):
            out.append(L(blob([(cx - 8 * s, 68), (cx + 6 * s, 74), (cx + 4 * s, 82), (cx - 7 * s, 78)], 6), c_('#3a4044'), 'f', True))
            out.append(L(blob([(cx - 6 * s, 70), (cx + 4 * s, 75), (cx + 2 * s, 80), (cx - 5 * s, 77)], 6), WHITE, 'f', False))
        return out
    return [L(blob([(70, 50), (86, 56), (90, 80), (84, 100), (70, 104), (66, 76)], 8), MASK, 'f', True),
            L(blob([(76, 70), (88, 72), (87, 80), (77, 79)], 6), c_('#3a4044'), 'f', True)]


C('candice-mell', 'chica', pal('#7ca042', '#f6e6c8', shade='#63693d', deep='#4b4b2f'),
  F(eyes='none', brows=False, mouth='none', hairline=hl(6, 66, 50, 60, jit=3, seed=5)),
  messy('front', amp=14, n=11, seed=41, lo=74) + [fr([(14, 60), (24, 58), (20, 100, 1), (10, 82)]), fr([(86, 60), (76, 58), (80, 100, 1), (90, 82)])] + _mell_mask('front'),
  messy('side', amp=14, n=11, seed=41, lo=74) + _mell_mask('side'),
  messy('back', amp=14, n=11, seed=41, lo=74, nape=92))

# Carey Filling: cabeza redonda y rapada con un tupé rosa palo encima, abultado como un cojín; cicatriz cosida en la frente;
# ojos de párpado caído aburridos y boca torcida
C('carey-filling', 'normal', pal('#cd857d', '#fbbc7a', shade='#a86660', deep='#804a46'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=95, hairline=False, ear_out=4, face_front=face(w=4, chin=104, jaw=3)),
  [skull(), L(blob([(28, 26), (30, 10), (50, 4), (72, 10), (74, 26), (50, 30)], 8), 'mid'), strand([(46, 10), (50, 18), (54, 10)], 'deep', 'b', 1.0),
   L([(24, 66), (40, 64)], OUTC, 'f', False, False, 3.0), L([(60, 64), (76, 66)], OUTC, 'f', False, False, 3.0),
   L([(26, 54), (38, 60)], OUTC, 'f', False, False, 1.2), L([(28, 60), (32, 54)], OUTC, 'f', False, False, 1.0), L([(33, 62), (37, 56)], OUTC, 'f', False, False, 1.0)],
  [L(blob([(36, 12), (60, 6), (80, 14), (78, 26), (40, 28)], 8), 'mid'), L([(74, 66), (86, 66)], OUTC, 'f', False, False, 3.0)],
  [L(blob([(26, 28), (30, 10), (50, 4), (70, 10), (74, 28), (50, 32)], 8), 'mid')])

# Carl Belcher (portero): pelo verde azulado oscuro en pinchos de punta que se disparan hacia arriba y a los lados; ojos
# afilados de enfado, cejas finas y boca recta
C('carl-belcher', 'normal', pal('#20716f', '#fac273', iris='#3a3a6a', shade='#1b4b48', deep='#123432'),
  F(eyes='sharp', brows='angry', mouth='frown', hairline=hl(5, 66, 52, 60, jit=3, seed=6)),
  messy('front', amp=16, n=11, seed=52, lo=72, sweep=0.1),
  messy('side', amp=16, n=11, seed=52, lo=72),
  messy('back', amp=16, n=11, seed=52, lo=72, nape=90))

# Carl Rhodes: pelo azul marino en forma de seta, una cúpula enorme más ancha que la cabeza y de borde recto por encima de
# los ojos; gafas redondas grandes de cristal rosado con remolinos y boca triste
LENS = c_('#c89a90')


def _swirl(cx, y):
    return [L(ell(cx, y, 11.5, 10), LENS, 'f', True, True), L(ell(cx, y, 6.5, 5.5) + [ell(cx, y, 6.5, 5.5)[0]], c_('#f0dcd0'), 'f', False, False, 1.4),
            L(ell(cx, y, 2.8, 2.4) + [ell(cx, y, 2.8, 2.4)[0]], c_('#f0dcd0'), 'f', False, False, 1.4)]


C('carl-rhodes', 'normal', pal('#2e4c65', '#efcfa7', shade='#24384c', deep='#182634'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, hairline=(60, 60)),
  [L(blob([(-6, 60), (-2, 36), (18, 8), (50, -2), (82, 8), (102, 36), (106, 60), (50, 64)], 10), 'mid'),
   L(blob([(60, 2), (86, 12), (102, 38), (104, 58), (76, 60)], 8), 'shade', 'b', False)] + _swirl(37, 76) + _swirl(63, 76),
  [L(blob([(-10, 60), (-4, 30), (20, 4), (54, -4), (84, 8), (100, 30), (104, 56), (50, 62)], 10), 'mid'),
   L(ell(84, 76, 7, 10), LENS, 'f', True, True), L([(76, 74), (54, 64)], OUTC, 'f', False, False, 1.4)],
  [L(blob([(-6, 62), (-2, 36), (18, 8), (50, -2), (82, 8), (102, 36), (106, 62), (50, 68)], 10), 'mid'),
   L(blob([(60, 2), (86, 12), (102, 38), (104, 60), (76, 64)], 8), 'shade', 'b', False)])

# Carol Chanter: chica de pelo rojo coral con raya en medio, recogido detrás de las orejas, y cuatro cuernos de pelo
# finos y largos: dos arriba que salen hacia los lados y dos que bajan junto a la mandíbula; ojos afilados verde oliva,
# cejas enfadadas y labios gruesos
def _horn(x0, y0, x1, y1, w=4):
    return L(outline([(x0, y0 - w), (x1, y1, 1), (x0, y0 + w)]), 'mid')


C('carol-chanter', 'chica', pal('#d85951', '#fdecc3', iris='#8a8a2a', shade='#9c3e31', deep='#7a2e24'),
  F(eyes='sharp', brows='angry', mouth='lips', mouth_w=6, mouth_y=95, hairline=[(14, 70), (20, 50), (34, 38), (50, 36), (66, 38), (80, 50), (86, 70)]),
  dome('front', top=4, w=42, cy=46, sb=76, seed=3) + [_horn(28, 18, -10, 0), _horn(72, 18, 110, 0), _horn(22, 84, -2, 110), _horn(78, 84, 102, 110),
                                                     strand([(50, 8), (50, 36)], 'deep', 'b', 1.0)],
  dome('side', top=4, w=42, cy=46, nape=84, fr=46, seed=3) + [_horn(40, 14, 20, -6), _horn(42, 82, 30, 112)],
  dome('back', top=4, w=42, cy=46, nape=84, seed=3) + [_horn(28, 18, -10, 0), _horn(72, 18, 110, 0), _horn(22, 84, -2, 110), _horn(78, 84, 102, 110)])

# Carrie O'Kea: chica de melena castaño rojiza ondulada hasta los hombros con flequillo echado a un lado y una horquilla;
# pecas, ojos grandes de enfado y boca pequeña fruncida
C('carrie-o-kea', 'chica', pal('#9d350d', '#f5be93', iris='#2a1a14', shade='#6f2713', deep='#4e1a0c'),
  F(eyes='normal', brows='angry', mouth='frown', mouth_y=94, hairline=[(14, 72), (18, 52), (30, 44), (48, 48), (66, 44), (82, 52), (86, 72)]),
  longhair('front', length=112, flare=12, ends=4) + [fr([(18, 46), (40, 36), (66, 40), (40, 56), (24, 66, 1)]), L([(30, 46), (38, 54)], c_('#e8b23a'), 'f', False, False, 2.0)]
  + freckles(86, 22),
  longhair('side', length=112, flare=12, ends=4),
  longhair('back', length=112, flare=12, ends=5))

# Cary Fearless: pelo rojo oscuro peinado hacia arriba en una llamarada con dos picos que salen a los lados como cuernos;
# ojos afilados de enfado y boca recta
C('cary-fearless', 'normal', pal('#9b0b0b', '#fcc171', iris='#2a1210', shade='#641511', deep='#460e0c'),
  F(eyes='sharp', brows='angry', mouth='frown', hairline=[(14, 64), (24, 50), (38, 56), (50, 48), (62, 56), (76, 50), (86, 64)]),
  [L(outline([(16, 64), (10, 44), (-2, 16, 1), (18, 26), (24, 6), (36, 18), (44, -6, 1), (52, 14), (58, -6, 1), (64, 18), (76, 6), (82, 26), (102, 16, 1),
              (90, 44), (84, 64), (80, 50), (20, 50)])),
   L(outline([(58, 0), (66, 18), (78, 8), (84, 28), (98, 20), (88, 44), (84, 60), (76, 36)]), 'shade', 'b', False)],
  [L(outline([(70, 52), (80, 44), (90, 22, 1), (76, 26), (72, 2, 1), (60, 16), (50, -4, 1), (40, 12), (20, 10, 1), (22, 26), (6, 40), (8, 66), (22, 78),
              (38, 72), (46, 58), (58, 54)])),
   L(outline([(8, 40), (30, 44), (44, 58), (36, 70), (20, 76), (8, 64)]), 'shade', 'b', False)],
  [L(outline([(16, 74), (10, 44), (-2, 16, 1), (18, 26), (24, 6), (36, 18), (44, -6, 1), (52, 14), (58, -6, 1), (64, 18), (76, 6), (82, 26), (102, 16, 1),
              (90, 44), (84, 74), (50, 80)])),
   L(outline([(58, 0), (66, 18), (78, 8), (84, 28), (98, 20), (88, 44), (84, 70), (64, 76)]), 'shade', 'b', False)])

# Carys Chaparon: chica de media melena magenta hasta la mandíbula, abombada y con las puntas hacia fuera, flequillo de
# mechones y un pelo de antena; ojos ámbar afilados y sonrisa decidida
C('carys-chaparon', 'chica', pal('#b8537b', '#f5bf94', iris='#b0701a', shade='#8d3a51', deep='#6e2e3a'),
  F(eyes='sharp', brows='angry', mouth='smile', hairline=hl(6, 70, 50, 62, jit=2, seed=11)),
  dome('front', top=4, w=46, cy=48, n=6, amp=6, soft=True, long=98, flare=10, seed=13) + [L(quad((52, 6), (60, -10), (48, -12)), 'mid', 'b', False, False, 2.4)],
  dome('side', top=4, w=46, cy=48, n=6, amp=6, soft=True, long=98, flare=10, fr=52, seed=13) + [L(quad((50, 4), (58, -12), (44, -12)), 'mid', 'b', False, False, 2.4)],
  dome('back', top=4, w=46, cy=48, n=6, amp=6, soft=True, long=98, flare=10, seed=13))

# Casey Leather: pelo de pinchos partido en dos colores, negro a su derecha (izquierda de la imagen) y plateado a su
# izquierda; ojos negros grandes y sonrisa
BLK = c_('#313033')


def _leather(view):
    if view == 'front':
        return [L(outline([(16, 66), (10, 44), (-4, 30, 1), (14, 26), (8, 8, 1), (28, 12), (36, -6, 1), (48, 8), (50, 40), (40, 50), (20, 50)]), BLK),
                L(outline([(84, 66), (90, 44), (106, 34, 1), (90, 26), (100, 8, 1), (76, 10), (78, -10, 1), (60, 4), (50, -4, 1), (46, 10), (50, 40), (60, 50), (80, 50)]), 'mid'),
                L(outline([(64, 8), (88, 26), (90, 50), (78, 40)]), 'shade', 'b', False)]
    if view == 'side':
        return [L(outline([(70, 52), (84, 44), (98, 30, 1), (84, 26), (94, 6, 1), (70, 10), (66, -10, 1), (52, 4), (40, -4, 1), (36, 10), (14, 12, 1), (18, 26), (2, 40, 1),
                           (8, 58), (22, 76), (38, 72), (46, 58), (58, 54)]), 'mid'),
                L(outline([(14, 12), (36, 10), (40, 30), (20, 50), (2, 40), (18, 26)]), BLK, 'b', False)]
    return [L(outline([(84, 74), (90, 44), (104, 30, 1), (90, 26), (96, 8, 1), (72, 12), (64, -6, 1), (52, 8), (50, 80), (70, 80)]), BLK),
            L(outline([(16, 74), (10, 44), (-6, 34, 1), (10, 26), (0, 8, 1), (24, 10), (22, -10, 1), (40, 4), (50, -4, 1), (52, 8), (50, 80), (30, 80)]), 'mid')]


C('casey-leather', 'normal', pal('#d7dedf', '#f8bc7f', iris='#1a1414', shade='#a8b0b4', deep='#7c8488'),
  F(eyes='big', brows=True, mouth='smile', hairline=hl(5, 66, 52, 62, jit=2, seed=14)),
  _leather('front'), _leather('side'), _leather('back'))

# Cash Winfall: piel morena, una llamarada de pelo amarillo anaranjado que sube de punta desde la frente (los lados, rapados);
# ojos afilados de enfado y boca seria
C('cash-winfall', 'normal', pal('#f8b946', '#cd9669', iris='#1a1210', shade='#d08a2a', deep='#a86a1a'),
  F(eyes='sharp', brows='angry', mouth='frown', hairline=False, face_front=face(chin=104)),
  [skull(), L(outline([(26, 50), (24, 30), (30, 12), (26, -12, 1), (42, 4), (46, -24, 1), (56, 0), (68, -18, 1), (68, 8), (76, 24), (76, 50), (62, 40), (40, 40)])),
   L(outline([(56, 0), (68, -18), (68, 8), (76, 24), (74, 46), (62, 30)]), 'shade', 'b', False)],
  [L(outline([(64, 46), (78, 34), (86, 10, 1), (72, 14), (70, -16, 1), (56, 4), (46, -20, 1), (40, 8), (28, 20), (36, 34), (50, 42)]))],
  [L(outline([(30, 44), (26, 24), (30, 8), (28, -14, 1), (42, 4), (50, -24, 1), (58, 2), (70, -14, 1), (70, 10), (72, 26), (70, 44), (50, 50)]))])

# Cat Selima: chica de piel morena con el pelo rosa palo peinado hacia atrás en ondas y dos moños abombados a los lados
# atados con gomas moradas; maquillaje de corazones granates alrededor de los ojos y la boca abierta gritando
HEART, BAND = c_('#5a1010'), c_('#5a3a8a')


def _hearts():
    out = []
    for cx in (37, 63):
        out.append(L(blob([(cx, 82), (cx - 10, 74), (cx - 8, 66), (cx - 3, 66), (cx, 70), (cx + 3, 66), (cx + 8, 66), (cx + 10, 74)], 4), HEART, 'f', False))
        out.append(L(ell(cx, 74, 4, 3.2), WHITE, 'f', False))
        out.append(L(ell(cx, 74, 1.8, 2.2), BLACK, 'f', False))
    return out


C('cat-selima', 'chica', pal('#f2a59a', '#b6713c', shade='#d08478', deep='#a8645a'),
  F(eyes='none', brows=False, mouth='none', hairline=[(14, 60), (22, 42), (36, 34), (50, 32), (64, 34), (78, 42), (86, 60)]),
  crop('front', top=0, side=60, w=1) + [L(ell(6, 54, 10, 8), 'mid'), L(ell(94, 54, 10, 8), 'mid'), L(ell(15, 56, 3, 4), BAND, 'f', True), L(ell(85, 56, 3, 4), BAND, 'f', True),
                                        L(blob([(42, 16), (50, 10), (58, 16), (50, 26)], 6), 'light', 'b', False)] + _hearts()
  + [L(blob([(44, 92), (56, 92), (57, 99), (43, 99)], 4), c_('#4c0c05'), 'f', True)],
  crop('side', top=0, nape=82) + [L(ell(40, 54, 10, 9), 'mid'), L(ell(46, 58, 3, 4), BAND, 'f', True),
                                  L(blob([(76, 80), (86, 66), (90, 74), (82, 84)], 4), HEART, 'f', False), L(blob([(80, 92), (88, 92), (88, 98), (80, 98)], 4), c_('#4c0c05'), 'f', True)],
  crop('back', top=0, nape=82) + [L(ell(6, 54, 10, 8), 'mid'), L(ell(94, 54, 10, 8), 'mid'), L(ell(15, 56, 3, 4), BAND, 'f', True), L(ell(85, 56, 3, 4), BAND, 'f', True)])

# Cerise Phoenix-Crane: chica de pelo rojo fuego con mechas naranjas, una melena que le tapa medio rostro (el ojo derecho) y
# adornos como plumas de llama naranja que asoman a los lados y arriba; piel muy clara, ojo verde agua y boca seria
FLM = c_('#fcb650')


def _flame(x, y, dx, dy):
    return L(outline([(x - 4, y), (x + dx, y + dy, 1), (x + dx * 0.4, y + dy * 0.5), (x + 4, y)]), FLM)


C('cerise-phoenix-crane', 'chica', pal('#cb2f03', '#f4ecc8', iris='#2a8a8a', shade='#89260a', deep='#6a1c08'),
  F(eyes='sharp', brows=False, mouth='frown', hairline=[(12, 70), (20, 48), (40, 40), (60, 42), (80, 50), (88, 70)]),
  dome('front', top=4, w=48, cy=48, sb=84, seed=5) +
  [fr([(14, 50), (40, 36), (66, 44), (56, 64), (46, 92), (30, 98, 1), (18, 80)]), L(outline([(26, 48), (44, 40), (40, 52), (30, 64)]), FLM, 'f', False),
   _flame(12, 52, -14, -10), _flame(10, 80, -12, 8), _flame(60, 10, 8, -20)],
  dome('side', top=4, w=48, cy=48, nape=90, fr=50, seed=5) + [_flame(30, 30, -18, -6), _flame(56, 8, 10, -18)],
  dome('back', top=4, w=48, cy=48, nape=90, seed=5) + [_flame(12, 52, -14, -10), _flame(88, 52, 14, -10), _flame(50, 8, 4, -20)])

# Chad Jowell (portero): grandullón de piel muy clara con papada, cabeza rapada con una cinta verde y un moño de pelo
# castaño anaranjado de punta encima; gafas de sol verdes y boca enfurruñada
GRN = c_('#065a1a')
C('chad-jowell', 'corpulento', pal('#c06a2a', '#f9f2dd', shade='#8a4a1a', deep='#6a3412'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, hairline=False, face_front=face(w=8, chin=110, jaw=6), ear_out=7),
  [skull(), L(quad((22, 46), (50, 38), (78, 46)), GRN, 'f', False, False, 5),
   L(outline([(42, 30), (40, 14), (48, -8, 1), (56, -2), (62, -14, 1), (60, 10), (58, 30)])), L(outline([(54, 0), (62, -14), (60, 10), (58, 26)]), 'shade', 'b', False)]
  + shades('front', 70, GRN),
  [L(quad((24, 40), (50, 36), (80, 44)), GRN, 'f', False, False, 5), L(outline([(48, 30), (44, 12), (34, -8, 1), (54, 2), (60, 30)]))] + shades('side', 70, GRN),
  [L(quad((20, 46), (50, 38), (80, 46)), GRN, 'f', False, False, 5), L(outline([(42, 30), (42, 10), (50, -10, 1), (58, 10), (58, 30)]))])

# Chance Blue-Cerulean: máscara de luchador azul con dos llamas amarillas sobre los ojos y el borde plateado, con las cintas
# sueltas a un lado; asoma pelo azul muy oscuro, abultado, por los lados; solo se le ve la boca seria
MBL, MYE, MSI = c_('#3577b3'), c_('#e8d24a'), c_('#d8d4d0')


def _luchador(view):
    if view == 'front':
        return [L(blob([(18, 74), (16, 44), (30, 16), (50, 8), (70, 16), (84, 44), (82, 74), (66, 92), (50, 98), (34, 92)], 8), MBL, 'f', True),
                L(outline([(26, 46), (38, 74), (46, 78), (40, 56)]), MYE, 'f', False), L(outline([(74, 46), (62, 74), (54, 78), (60, 56)]), MYE, 'f', False),
                L(quad((18, 74), (16, 30), (50, 8)), MSI, 'f', False, False, 2.6), L(quad((82, 74), (84, 30), (50, 8)), MSI, 'f', False, False, 2.6),
                L(ell(36, 72, 3, 2.4), BLACK, 'f', False), L(ell(64, 72, 3, 2.4), BLACK, 'f', False)]
    if view == 'side':
        return [L(blob([(48, 30), (66, 12), (84, 26), (90, 56), (86, 80), (72, 94), (56, 86), (50, 60)], 8), MBL, 'f', True),
                L(outline([(80, 42), (86, 70), (78, 72), (76, 52)]), MYE, 'f', False),
                L(outline([(48, 58), (30, 70, 1), (40, 58), (24, 56, 1), (48, 50)]), MBL, 'f', True)]
    return [L(blob([(20, 76), (16, 44), (30, 16), (50, 8), (70, 16), (84, 44), (80, 76), (50, 82)], 8), MBL, 'f', True),
            L([(50, 20), (50, 80)], MSI, 'f', False, False, 2.4), L(outline([(56, 70), (78, 94, 1), (64, 74), (70, 100, 1), (52, 74)]), MBL, 'f', True)]


C('chance-blue-cerulean', 'normal', pal('#2a3a4a', '#e3c26a', shade='#1e2a36', deep='#141c24'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=94, hairline=False),
  [L(blob([(-2, 80), (0, 50), (14, 22), (50, 6), (86, 22), (100, 50), (102, 80), (88, 90), (12, 90)], 10), 'mid')] + _luchador('front'),
  [L(blob([(4, 84), (2, 50), (20, 16), (60, 8), (86, 30), (60, 90), (20, 96)], 10), 'mid')] + _luchador('side'),
  [L(blob([(-2, 86), (0, 50), (14, 22), (50, 6), (86, 22), (100, 50), (102, 86), (50, 96)], 10), 'mid')] + _luchador('back'))

# Chase Spoor: pelo azul marino oscuro peinado hacia atrás y recogido detrás, con un par de mechones sueltos por las sienes;
# un antifaz gris de murciélago con los ojos blancos y una cara de murciélago en la frente; boca seria
BAT = c_('#919ea1')


def _bat(view):
    if view == 'front':
        return [L(outline([(10, 66), (22, 62), (30, 58), (44, 64), (50, 54), (56, 64), (70, 58), (78, 62), (90, 66), (80, 76), (84, 86, 1), (70, 82), (56, 86), (50, 80),
                           (44, 86), (30, 82), (16, 86, 1), (20, 76)]), BAT, 'f', True),
                L(blob([(28, 72), (42, 68), (44, 76), (30, 78)], 4), WHITE, 'f', True), L(blob([(72, 72), (58, 68), (56, 76), (70, 78)], 4), WHITE, 'f', True)]
    return [L(outline([(66, 62), (80, 60), (90, 66), (88, 82), (78, 84), (70, 80), (60, 84, 1), (62, 72)]), BAT, 'f', True),
            L(blob([(78, 70), (88, 70), (87, 77), (79, 77)], 4), WHITE, 'f', True)]


C('chase-spoor', 'normal', pal('#434255', '#f6bb7f', shade='#393540', deep='#26232c'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=95, hairline=[(14, 60), (22, 44), (36, 36), (50, 34), (64, 36), (78, 44), (86, 60)]),
  crop('front', top=2, side=62) + [strand([(22, 60), (18, 76), (22, 92)], 'mid', 'f', 2.0), strand([(78, 60), (82, 76), (78, 92)], 'mid', 'f', 2.0)] + _bat('front'),
  crop('side', top=2, nape=84) + [L(outline([(8, 60), (0, 80), (4, 100, 1), (12, 82), (16, 66)]))] + _bat('side'),
  crop('back', top=2, nape=84) + [L(outline([(42, 74), (40, 100, 1), (50, 92), (60, 100, 1), (58, 74)]))])

# Chester Takes: cara alargada; pelo gris verdoso oscuro corto, con un tupé que sube y se echa a un lado; gafas de sol finas
# rectangulares de cristal verde claro, cejas fruncidas por encima y boca pequeña seria
C('chester-takes', 'delgado', pal('#4e5e5d', '#fabc7b', shade='#3e4a49', deep='#2a3232'),
  F(eyes='none', brows=False, mouth='line', mouth_y=98, hairline=[(14, 62), (22, 44), (40, 42), (60, 38), (78, 40), (86, 62)],
    face_front=face(w=-1, chin=110, jaw=-2)),
  crop('front', top=4, side=62) + [L(outline([(30, 20), (50, 4), (78, 0), (96, -10, 1), (88, 10), (80, 24)]), 'mid')]
  + shades('front', 76, c_('#c8ccaa')) + [L([(26, 64), (40, 68)], OUTC, 'f', False, False, 2.4), L([(74, 64), (60, 68)], OUTC, 'f', False, False, 2.4)],
  crop('side', top=4, nape=82) + [L(outline([(60, 8), (84, 2), (100, -8, 1), (94, 12), (84, 20)]), 'mid')] + shades('side', 76, c_('#c8ccaa')),
  crop('back', top=4, nape=82))

# Chip Spacek (portero): señor de cabeza alargada en huevo, calva salvo una franja de pelo pardo arriba; visera plateada
# sobre los ojos con una ranura oscura, barba gris que le rodea la mandíbula y boca grande enfadada
VIS, BEARD = c_('#d2ceca'), c_('#b8b2ae')
C('chip-spacek', 'normal', pal('#826a60', '#fdc271', shade='#5e4c44', deep='#4c3e36'),
  F(eyes='none', brows=False, mouth='none', hairline=False, face_front=face(w=-2, chin=112, top=6)),
  [L(blob([(22, 56), (24, 26), (36, 4), (50, -4), (64, 4), (76, 26), (78, 56)], 10), 'skin'), L(blob([(40, 2), (50, -4), (60, 2), (50, 10)], 6), 'mid'),
   L(blob([(12, 68), (16, 60), (84, 60), (88, 68), (84, 80), (16, 80)], 6), VIS, 'f', True), L(blob([(24, 68), (76, 68), (76, 72), (24, 72)], 4), c_('#3a3030'), 'f', False),
   L(blob([(18, 76), (26, 96), (40, 108), (50, 114), (60, 108), (74, 96), (82, 76), (84, 100), (66, 118), (50, 122), (34, 118), (16, 100)], 6), BEARD, 'f', True),
   L(blob([(34, 92), (50, 86), (66, 92), (62, 98), (50, 94), (38, 98)], 5), c_('#8a4a2a'), 'f', True)],
  [L(blob([(20, 50), (26, 22), (44, 2), (60, 0), (76, 14), (84, 40), (70, 56)], 10), 'skin'), L(blob([(40, 6), (54, -2), (64, 2), (58, 10), (44, 12)], 8), 'mid'),
   L(blob([(60, 62), (90, 62), (92, 78), (60, 78)], 6), VIS, 'f', True),
   L(blob([(50, 80), (70, 96), (90, 92), (86, 110), (66, 120), (48, 108)], 6), BEARD, 'f', True)],
  [L(blob([(20, 60), (22, 26), (36, 4), (50, -4), (64, 4), (78, 26), (80, 60)], 10), 'skin'), L(blob([(56, 4), (76, 26), (78, 56), (64, 50)], 8), 'skin_d', 'b', False),
   L(blob([(40, 4), (50, -4), (60, 4), (50, 10)], 6), 'mid'), L(quad((10, 70), (50, 76), (90, 70)), VIS, 'f', False, False, 4)])

# Chip Stocks: piel tostada, pelo gris verdoso de pinchos revueltos con un flequillo largo de mechones que le cae sobre los
# ojos; cicatriz en aspa en la mejilla, ojos azul grisáceo afilados y boca enfadada
C('chip-stocks', 'normal', pal('#a5b18e', '#daa25a', iris='#5a6a8a', shade='#89896f', deep='#5e5649'),
  F(eyes='sharp', brows='angry', mouth='frown', hairline=hl(6, 70, 50, 68, jit=3, seed=17)),
  dome('front', top=4, w=48, cy=46, n=9, amp=10, sweep=0.3, sb=74, seed=61) + [fr([(30, 44), (46, 44), (40, 72, 1)]), fr([(54, 44), (68, 46), (60, 70, 1)]), L([(30, 84), (38, 90)], c_('#7a4a2a'), 'f', False, False, 1.2), L([(30, 90), (38, 84)], c_('#7a4a2a'), 'f', False, False, 1.2)],
  dome('side', top=4, w=48, cy=46, n=9, amp=10, sweep=0.3, nape=86, fr=54, seed=61),
  dome('back', top=4, w=48, cy=46, n=9, amp=10, sweep=0.3, nape=86, seed=61))

# Chloe Glazier: chica de pelo rosa salmón recogido detrás en una coleta baja, con flequillo echado a un lado y dos mechones
# largos que le caen por delante de las orejas hasta el pecho; ojos verde grisáceo serios
C('chloe-glazier', 'chica', pal('#cc8078', '#fcce9f', iris='#5a6a4a', shade='#a05d56', deep='#84473e'),
  F(eyes='sharp', brows='angry', mouth='frown', hairline=[(14, 70), (18, 48), (30, 40), (54, 44), (70, 40), (82, 48), (86, 70)]),
  crop('front', top=2, side=66) + [fr([(20, 42), (50, 34), (72, 44), (46, 52), (30, 66, 1)]), fr([(16, 62), (24, 62), (24, 110, 1), (14, 92)]), fr([(84, 62), (76, 62), (76, 110, 1), (86, 92)])],
  crop('side', top=2, nape=82) + [L(outline([(16, 60), (4, 90), (8, 118, 1), (20, 92), (26, 66)])), fr([(64, 60), (72, 60), (72, 108, 1), (64, 90)])],
  crop('back', top=2, nape=82) + [L(outline([(42, 70), (38, 104), (50, 120, 1), (62, 104), (58, 70)]))])

# Chris Country: pelo azul celeste que cae en cortinas lisas a los lados de la cara, con flequillo de mechones y dos cuernos
# de carnero enroscados junto a las orejas; piel clara, ojos oscuros y boca seria
HORN = c_('#a08a74')


def _ram(cx, s):
    return [L(ell(cx, 74, 7, 9), HORN, 'f', True), L(ell(cx, 74, 3.4, 4.4) + [ell(cx, 74, 3.4, 4.4)[0]], c_('#6a5a4a'), 'f', False, False, 1.2)]


C('chris-country', 'normal', pal('#78adc1', '#fceab8', iris='#5a1a1a', shade='#6a909d', deep='#4a6a74'),
  F(eyes='normal', brows='angry', mouth='frown', hairline=hl(5, 70, 46, 60, jit=2, seed=19)),
  dome('front', top=2, w=48, cy=48, long=98, flare=6, seed=19) + _ram(12, 1) + _ram(88, -1),
  dome('side', top=2, w=48, cy=48, long=98, flare=6, fr=48, seed=19) + [L(ell(48, 74, 7, 9), HORN, 'f', True)],
  dome('back', top=2, w=48, cy=48, long=98, flare=6, seed=19) + _ram(10, 1) + _ram(90, -1))

# Claire Hostess: chica de piel tostada con media melena rosa en casco y flequillo recto de mechones; ojos verdes grandes,
# coloretes y sonrisa
C('claire-hostess', 'chica', pal('#faa59d', '#dda259', iris='#2a5a4a', shade='#ca6e68', deep='#a0504a'),
  F(eyes='big', brows=True, mouth='smile', hairline=hl(7, 72, 58, 66, jit=1, seed=21)),
  bowl('front', top=2, side=92) + blush(88, 22),
  bowl('side', top=2, nape=92),
  bowl('back', top=2, nape=92))

# Claire Taker: chica de pelo gris lavanda con flequillo recto y dos mechones largos lisos a los lados hasta el cuello, y un
# lazo rojo encima; piel clara, ojos redondos grandes y sonrisa
BOW = c_('#b81e1e')


def _bow(x, y, view='front'):
    if view == 'side':
        return [L(blob([(x - 8, y - 6), (x + 8, y - 6), (x + 6, y + 4), (x - 6, y + 4)], 4), BOW, 'f', True)]
    return [L(blob([(x - 16, y - 6), (x - 2, y), (x - 16, y + 6)], 4), BOW, 'f', True), L(blob([(x + 16, y - 6), (x + 2, y), (x + 16, y + 6)], 4), BOW, 'f', True),
            L(ell(x, y, 3, 3), BOW, 'f', True)]


C('claire-taker', 'chica', pal('#89738c', '#f5edca', iris='#1a1414', shade='#684f5d', deep='#4d3c45'),
  F(eyes='round', brows=False, mouth='smile', hairline=hl(7, 72, 60, 64, jit=1, seed=23)),
  dome('front', top=6, w=46, cy=48, sb=70, seed=23) + [fr([(12, 60), (24, 60), (24, 104), (14, 106)]), fr([(88, 60), (76, 60), (76, 104), (86, 106)])] + _bow(50, 4),
  dome('side', top=6, w=46, cy=48, nape=84, fr=52, seed=23) + [fr([(56, 60), (66, 60), (66, 104), (56, 106)])] + _bow(44, 4, 'side'),
  dome('back', top=6, w=46, cy=48, nape=84, seed=23) + [L(outline([(8, 60), (24, 60), (24, 106), (10, 106)])), L(outline([(92, 60), (76, 60), (76, 106), (90, 106)]))] + _bow(50, 4))

# Claire Voyant: chica de piel tostada con melena morada oscura lisa y raya en medio que le cae por los lados hasta los
# hombros; una joya en la frente (cadena dorada, piedra turquesa y gotas rojas); ojos naranja afilados y labios oscuros
GOLD, TURQ, RUBY = c_('#c8a040'), c_('#3ab8b8'), c_('#c02020')
C('claire-voyant', 'chica', pal('#43103d', '#dda359', iris='#c0501a', shade='#331922', deep='#200c18'),
  F(eyes='sharp', brows='angry', mouth='frown', hairline=[(12, 70), (20, 44), (36, 34), (50, 32), (64, 34), (80, 44), (88, 70)]),
  longhair('front', length=112, flare=6, part=True, ends=3) +
  [L([(50, 4), (50, 52)], GOLD, 'f', False, False, 1.4), L(ell(50, 58, 4, 4.4), TURQ, 'f', True), L(ell(50, 66, 1.6, 2), RUBY, 'f', False)],
  longhair('side', length=112, flare=6, ends=3) + [L(ell(84, 58, 2.6, 3.4), TURQ, 'f', True)],
  longhair('back', length=112, flare=6, ends=4))

# Clara Tompkins: chica de pelo rojo liso peinado hacia atrás con raya en medio, largo por detrás; gafas grandes verdes
# rectangulares, ojos de enfado y dientes apretados
C('clara-tompkins', 'chica', pal('#a9301a', '#fbcf9f', iris='#2a1a14', shade='#752515', deep='#561a0e'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, hairline=[(14, 70), (22, 44), (36, 34), (50, 30), (64, 34), (78, 44), (86, 70)],
    glasses=c_('#2a8a2a'), glasses_rect=True),
  longhair('front', length=110, flare=4, part=True, ends=3),
  longhair('side', length=110, flare=4, ends=3),
  longhair('back', length=110, flare=4, ends=4))

# Clark Tappen (portero): pelo pardo oliva de pinchos que se abren en alas hacia los lados y uno hacia arriba; unas gafas
# enormes de cristal verde lima tapándole los ojos y media sonrisa
LIME, LFR = c_('#a3dd59'), c_('#4e5a3a')
C('clark-tappen', 'normal', pal('#868063', '#f3cb8d', shade='#695d3c', deep='#4e4134'),
  F(eyes='none', brows=False, mouth='smile', hairline=hl(5, 64, 52, 60, jit=2, seed=25)),
  [L(outline([(16, 64), (10, 50), (-14, 40, 1), (12, 34), (2, 20, 1), (24, 22), (26, 0, 1), (40, 12), (54, -14, 1), (60, 10), (78, 4, 1), (78, 22), (104, 22, 1),
              (88, 36), (112, 46, 1), (90, 50), (84, 64), (80, 50), (20, 50)])),
   L(outline([(60, 10), (78, 4), (78, 22), (104, 22), (88, 36), (110, 46), (88, 52), (76, 34)]), 'shade', 'b', False)] +
  [L(blob([(22, 66), (44, 64), (48, 76), (36, 86), (22, 80)], 6), LIME, 'f', True), L(blob([(78, 66), (56, 64), (52, 76), (64, 86), (78, 80)], 6), LIME, 'f', True),
   L([(46, 70), (54, 70)], LFR, 'f', False, False, 2.4), L([(14, 70), (22, 70)], LFR, 'f', False, False, 2.4), L([(78, 70), (86, 70)], LFR, 'f', False, False, 2.4)],
  [L(outline([(70, 52), (86, 44), (104, 30, 1), (86, 26), (94, 6, 1), (72, 12), (64, -14, 1), (54, 6), (36, 0, 1), (34, 18), (8, 18, 1), (16, 32), (-10, 44, 1),
              (8, 58), (22, 76), (38, 72), (46, 58), (58, 54)])),
   L(blob([(72, 64), (90, 64), (92, 80), (76, 84)], 6), LIME, 'f', True), L([(72, 70), (44, 64)], LFR, 'f', False, False, 2.4)],
  [L(outline([(16, 74), (10, 50), (-14, 40, 1), (12, 34), (2, 20, 1), (24, 22), (26, 0, 1), (40, 12), (54, -14, 1), (60, 10), (78, 4, 1), (78, 22), (104, 22, 1),
              (88, 36), (112, 46, 1), (90, 50), (84, 74), (50, 80)])), L(quad((10, 70), (50, 74), (90, 70)), LFR, 'f', False, False, 2.4)])

# Clay Turnor (portero): melena amarilla dorada alborotada de pinchos, con mechones largos de punta que le bajan por los
# lados hasta la barbilla; ojos verde azulado afilados de enfado y boca apretada
C('clay-turnor', 'normal', pal('#d3aa05', '#f1ca9b', iris='#1a7a6a', shade='#a88004', deep='#8e5c10'),
  F(eyes='sharp', brows='angry', mouth='frown', hairline=hl(6, 70, 50, 66, jit=3, seed=27)),
  dome('front', top=0, w=50, cy=46, n=9, amp=11, sweep=0.4, long=104, flare=14, seed=27),
  dome('side', top=0, w=50, cy=46, n=9, amp=11, sweep=0.4, long=104, flare=14, fr=54, seed=27),
  dome('back', top=0, w=50, cy=46, n=9, amp=11, sweep=0.4, long=104, flare=14, seed=27))

# Clef Bassett: piel morena y cara alargada; melena castaña peinada hacia atrás que cae ondulada hasta los hombros; una
# cicatriz en aspa clara en la frente, gafas de sol oscuras y una sonrisa enorme de dientes
SUNG = c_('#3a4a40')
C('clef-bassett', 'delgado', pal('#7a4e3f', '#daa35c', shade='#60372a', deep='#422d26'),
  F(eyes='none', brows=False, mouth='none', hairline=[(14, 66), (22, 40), (36, 30), (50, 28), (64, 30), (78, 40), (86, 66)],
    face_front=face(w=-1, chin=110)),
  longhair('front', length=112, flare=8, ends=4) + shades('front', 74, SUNG) + teeth(94, 14, 7) +
  [L([(42, 48), (58, 58)], c_('#f4e2b0'), 'f', False, False, 2.2), L([(42, 58), (58, 48)], c_('#f4e2b0'), 'f', False, False, 2.2)],
  longhair('side', length=112, flare=8, ends=4) + shades('side', 74, SUNG) + [L(blob([(76, 90), (90, 89), (89, 98), (78, 98)], 4), WHITE, 'f', True)],
  longhair('back', length=112, flare=8, ends=5))

# Clint Peacock: piel tostada, pelo castaño rojizo oscuro en casco con un flequillo largo que le tapa el ojo derecho; ojo
# entornado de desgana y boca seria
C('clint-peacock', 'normal', pal('#714844', '#d9b37c', iris='#1a1210', shade='#512e29', deep='#3a201c'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=94, hairline=[(14, 72), (16, 52), (30, 46), (50, 50), (70, 46), (84, 52), (86, 72)]),
  bowl('front', top=2, side=88) + [fr([(18, 46), (50, 40), (70, 46), (48, 62), (40, 86, 1), (30, 70)])],
  bowl('side', top=2, nape=90),
  bowl('back', top=2, nape=90))

# Cody Fink: pelo gris verdoso con flequillo de mechones y media melena hasta la mandíbula; gafas finas negras, ojos
# morados y unos cascos oscuros con borde de pelo colgados al cuello
PHN, FUR = c_('#2a2e3a'), c_('#8a6a4a')
C('cody-fink', 'normal', pal('#858c6f', '#f9d28e', iris='#6a3a6a', shade='#615646', deep='#4a3f39'),
  F(eyes='sharp', brows=False, mouth='line', hairline=hl(6, 70, 52, 66, jit=2, seed=29), glasses=BLACK, glasses_rect=True),
  dome('front', top=2, w=47, cy=48, long=96, flare=6, seed=29) +
  [L(blob([(10, 98), (26, 94), (30, 110), (14, 114)], 6), FUR, 'f', True), L(blob([(90, 98), (74, 94), (70, 110), (86, 114)], 6), FUR, 'f', True),
   L(ell(16, 104, 7, 8), PHN, 'f', True), L(ell(84, 104, 7, 8), PHN, 'f', True)],
  dome('side', top=2, w=47, cy=48, long=96, flare=6, fr=52, seed=29) + [L(ell(56, 104, 9, 9), PHN, 'f', True)],
  dome('back', top=2, w=47, cy=48, long=96, flare=6, seed=29) + [L(quad((14, 104), (50, 112), (86, 104)), PHN, 'f', False, False, 3)])

# Coe Dachy (portero): grandullón calvo con la cabeza y la mandíbula sombreadas de barba verdosa, un moñito negro diminuto
# encima; gafas cuadradas negras, morro marrón grande y la boca abierta enseñando los dientes
STUB, SNOUT = c_('#9eaf82'), c_('#8a6048')
C('coe-dachy', 'corpulento', pal('#9eaf82', '#f7bc7d', shade='#7e8e66'),
  F(eyes='dot', brows=False, mouth='none', hairline=False, glasses=BLACK, glasses_rect=True, face_front=face(w=8, chin=110, jaw=6), ear_out=7),
  [skull(), L(blob([(34, 14), (50, 6), (66, 14), (60, 28), (40, 28)], 6), STUB, 'b', False), L(ell(50, 2, 4, 4), BLACK, 'f', True),
   L(blob([(14, 80), (20, 98), (36, 110), (50, 114), (64, 110), (80, 98), (86, 80), (84, 102), (64, 118), (36, 118), (16, 102)], 6), STUB, 'f', False),
   L(blob([(36, 84), (50, 80), (64, 84), (66, 98), (50, 104), (34, 98)], 6), SNOUT, 'f', True), L(blob([(42, 92), (58, 92), (56, 98), (44, 98)], 4), WHITE, 'f', True)],
  [L(blob([(16, 50), (24, 22), (46, 8), (70, 12), (84, 34), (70, 50)], 10), 'skin'), L(blob([(30, 20), (48, 10), (62, 12), (58, 24), (36, 28)], 6), STUB, 'b', False),
   L(ell(50, 6, 4, 4), BLACK, 'f', True),
   L(blob([(80, 82), (98, 86), (96, 100), (80, 102)], 6), SNOUT, 'f', True), L(blob([(60, 90), (78, 108), (60, 116), (50, 100)], 6), STUB, 'f', False)],
  [L(blob([(18, 60), (20, 28), (50, 10), (80, 28), (82, 60)], 10), 'skin'), L(blob([(30, 22), (50, 14), (70, 22), (70, 44), (30, 44)], 6), STUB, 'b', False),
   L(ell(50, 8, 4, 4), BLACK, 'f', True)])

# Cole Stoaker (portero): piel tostada, pelo verde muy oscuro de pinchos tiesos en todas direcciones; ojos afilados de
# enfado, arrugas marcadas en las mejillas y boca seria
C('cole-stoaker', 'normal', pal('#36463e', '#eca663', iris='#1a1210', shade='#2a3630', deep='#1e2622'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=hl(6, 64, 50, 58, jit=3, seed=31)),
  messy('front', amp=16, n=12, seed=71, lo=68) + [L([(24, 86), (30, 92)], OUTC, 'f', False, False, 1.0), L([(76, 86), (70, 92)], OUTC, 'f', False, False, 1.0)],
  messy('side', amp=16, n=12, seed=71, lo=68),
  messy('back', amp=16, n=12, seed=71, lo=68, nape=90))

# Colet First: piel muy pálida, un mechón de pelo verde oliva de pinchos sobre la coronilla y los lados rapados; ojos
# cerrados, orejas de punta, nariz fina y boca ancha apretada
C('colet-first', 'normal', pal('#8a9224', '#e8d4b9', shade='#6a701c', deep='#5a4e1b'),
  F(eyes='closed', brows=False, mouth='frown', mouth_y=96, hairline=False, ear_out=4, face_front=face(chin=108)),
  [skull(), L(outline([(22, 40), (14, 30, 1), (24, 22), (20, 6, 1), (36, 10), (42, -6, 1), (52, 8), (64, -4, 1), (66, 12), (82, 8, 1), (78, 24), (88, 32, 1), (76, 40),
                       (60, 34), (50, 52, 1), (40, 34)])),
   L(outline([(52, 8), (64, -4), (66, 12), (80, 10), (78, 24), (86, 32), (74, 38), (60, 30)]), 'shade', 'b', False)] + nose(86),
  [L(outline([(36, 30), (30, 14, 1), (44, 12), (50, -4, 1), (60, 8), (74, 2, 1), (74, 16), (88, 20, 1), (80, 32), (60, 36)]))],
  [L(outline([(22, 40), (14, 30, 1), (24, 22), (20, 6, 1), (36, 10), (42, -6, 1), (52, 8), (64, -4, 1), (66, 12), (82, 8, 1), (78, 24), (88, 32, 1), (76, 40), (50, 44)]))])

# Colin Binder: piel tostada, pelo blanco lila en casco con flequillo recto hasta los ojos y dos mechones finos y largos que
# le caen por delante hasta el pecho; un ojo naranja y otro amarillo y boca seria
C('colin-binder', 'normal', pal('#e4d9d6', '#ca9444', iris='#d0601a', shade='#ae9793', deep='#8a7672', eye2='#e0b020'),
  F(eyes='sharp', brows=False, mouth='frown', hairline=hl(7, 70, 64, 68, jit=1, seed=33)),
  bowl('front', top=2, side=84) + [fr([(20, 64), (26, 64), (28, 116, 1), (18, 96)]), fr([(80, 64), (74, 64), (72, 116, 1), (82, 96)]),
                                   L(ell(65, 77, 2.4, 3.4), c_('#e0b020'), 'f', False)],
  bowl('side', top=2, nape=88) + [fr([(66, 64), (72, 64), (72, 114, 1), (64, 96)])],
  bowl('back', top=2, nape=88))

# Colin Glower: cabeza calva con tres rayas azul marino pintadas encima; orejas grandes, ojos pequeños de enfado con cejas
# marcadas, nariz grande, boca ancha apretada y perilla azul marino
NAVY = c_('#3a3e7a')
C('colin-glower', 'delgado', pal('#3a3e7a', '#fdc271', shade='#2a2e5a'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, hairline=False, big_ears=2, ear_out=4, face_front=face(chin=110, jaw=2), nose=(50, 86, 3.4)),
  [skull(), L(blob([(36, 10), (40, 8), (42, 40), (38, 40)], 4), NAVY, 'b', False), L(blob([(48, 6), (52, 6), (52, 40), (48, 40)], 4), NAVY, 'b', False),
   L(blob([(60, 8), (64, 10), (62, 40), (58, 40)], 4), NAVY, 'b', False), L(blob([(46, 102), (54, 102), (52, 112), (48, 112)], 4), NAVY, 'f', True)],
  [L(blob([(16, 50), (24, 22), (46, 8), (70, 12), (84, 34), (70, 50)], 10), 'skin'), L(quad((40, 10), (62, 12), (80, 30)), NAVY, 'f', False, False, 3),
   L(blob([(80, 104), (88, 104), (86, 112), (82, 112)], 4), NAVY, 'f', True)],
  [L(blob([(18, 60), (20, 28), (50, 10), (80, 28), (82, 60)], 10), 'skin'), L([(38, 14), (40, 50)], NAVY, 'f', False, False, 3),
   L([(50, 12), (50, 52)], NAVY, 'f', False, False, 3), L([(62, 14), (60, 50)], NAVY, 'f', False, False, 3)])

# Colt Youngstein: pelo azul marino muy oscuro bien peinado con flequillo de mechones y patillas; gafas redondas finas
# doradas, ojos castaños y sonrisa abierta
C('colt-youngstein', 'normal', pal('#433b4b', '#fbc273', iris='#8a5a1a', shade='#2a2123', deep='#1e181a'),
  F(eyes='normal', brows=True, mouth='smile', hairline=hl(6, 70, 52, 64, jit=2, seed=35)),
  dome('front', top=4, w=46, cy=46, n=7, amp=6, sb=78, seed=35) + specs('front', c_('#b88a3a')),
  dome('side', top=4, w=46, cy=46, n=7, amp=6, nape=86, fr=52, seed=35) + specs('side', c_('#b88a3a')),
  dome('back', top=4, w=46, cy=46, n=7, amp=6, nape=86, seed=35))

# Conn Fuchus (portero): pelo verde agua de pinchos revueltos con mechones largos que le bajan por los lados de la cara;
# ojos azules entornados, marcas de arañazos en las mejillas y boca seria
C('conn-fuchus', 'normal', pal('#57ab98', '#fac272', iris='#2a6a9a', shade='#4a7f72', deep='#365c52'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=hl(6, 66, 50, 62, jit=3, seed=37)),
  messy('front', amp=13, n=11, seed=81, lo=70, sweep=0.2) + [fr([(14, 60), (22, 60), (22, 102, 1), (12, 84)]), fr([(86, 60), (78, 60), (78, 102, 1), (88, 84)]),
                                                         L([(26, 86), (34, 90)], c_('#c87a3a'), 'f', False, False, 1.2), L([(66, 90), (74, 86)], c_('#c87a3a'), 'f', False, False, 1.2)],
  messy('side', amp=13, n=11, seed=81, lo=70) + [fr([(62, 60), (70, 60), (70, 100, 1), (62, 82)])],
  messy('back', amp=13, n=11, seed=81, lo=70, nape=92))

# Connor Seuer: pelo verde azulado oscuro con flequillo largo que le sombrea los ojos y mechones laterales más claros hasta
# los hombros; unos cascos grises de diadema con auriculares redondos en las sienes; sonrisa de pillo
HEAD, DISC = c_('#9aa0aa'), c_('#7a7290')
C('connor-seuer', 'normal', pal('#355d6b', '#fbc272', iris='#1a1414', shade='#2b383d', deep='#1e282c', low='#76959a'),
  F(eyes='sharp', brows=False, mouth='smile', hairline=hl(7, 72, 66, 70, jit=1, seed=39)),
  [fr([(12, 62), (24, 60), (26, 110, 1), (12, 100)], 'low'), fr([(88, 62), (76, 60), (74, 110, 1), (88, 100)], 'low')] +
  dome('front', top=2, w=48, cy=48, sb=70, seed=39)[:1] + [L(quad((14, 46), (50, 4), (86, 46)), HEAD, 'f', False, False, 3),
                                                       L(ell(14, 50, 7, 8), DISC, 'f', True), L(ell(86, 50, 7, 8), DISC, 'f', True)] + blush(88, 22, 3.4),
  dome('side', top=2, w=48, cy=48, long=100, flare=4, fr=56, seed=39) + [L(quad((30, 50), (40, 6), (60, 2)), HEAD, 'f', False, False, 3), L(ell(40, 50, 8, 9), DISC, 'f', True)],
  dome('back', top=2, w=48, cy=48, long=100, flare=4, seed=39) + [L(quad((14, 46), (50, 2), (86, 46)), HEAD, 'f', False, False, 3),
                                                                 L(ell(12, 50, 7, 8), DISC, 'f', True), L(ell(88, 50, 7, 8), DISC, 'f', True)])

# Conrad Jacket: gorro de punto verde en punta con dibujos de almohadilla blancos; asoman mechones negros por los lados;
# piel clara, gafas de sol redondas pequeñas, coloretes, nariz picuda y una sonrisa enorme
BEAN, WHL = c_('#48943b'), c_('#d8f0d0')
C('conrad-jacket', 'normal', pal('#2a2622', '#fdeab7', shade='#1a1814'),
  F(eyes='none', brows=False, mouth='none', hairline=False, face_front=face(w=4, chin=110, jaw=3)),
  [L(outline([(16, 64), (6, 70, 1), (14, 54), (20, 50)])), L(outline([(84, 64), (94, 70, 1), (86, 54), (80, 50)])),
   L(outline([(16, 56), (18, 30), (36, 6), (50, -10, 1), (64, 6), (82, 30), (84, 56), (50, 52)]), BEAN, 'f', True),
   L([(30, 24), (42, 18)], WHL, 'f', False, False, 1.6), L([(30, 32), (42, 26)], WHL, 'f', False, False, 1.6), L([(34, 16), (36, 34)], WHL, 'f', False, False, 1.6),
   L([(40, 14), (42, 32)], WHL, 'f', False, False, 1.6), L([(66, 22), (74, 26)], WHL, 'f', False, False, 1.6), L([(68, 18), (70, 30)], WHL, 'f', False, False, 1.6),
   L(ell(38, 72, 5, 5), BLACK, 'f', True), L(ell(62, 72, 5, 5), BLACK, 'f', True), L([(43, 72), (57, 72)], BLACK, 'f', False, False, 1.2),
   L(outline([(48, 74), (50, 86, 1), (53, 80)]), c_('#f0d098'), 'f', True), L(quad((30, 92), (50, 106), (70, 92)), MOUTH, 'f', False, False, 1.8)] + blush(84, 22, 4),
  [L(outline([(52, 56), (44, 68, 1), (48, 50)])), L(outline([(46, 56), (40, 28), (52, 6), (76, -6, 1), (82, 18), (90, 40), (82, 52)]), BEAN, 'f', True),
   L(ell(84, 72, 4, 5), BLACK, 'f', True), L(outline([(88, 76), (98, 84, 1), (88, 84)]), c_('#f0d098'), 'f', True)],
  [L(outline([(16, 70), (8, 76, 1), (18, 54)])), L(outline([(84, 70), (92, 76, 1), (82, 54)])),
   L(outline([(14, 60), (16, 30), (36, 6), (50, -10, 1), (64, 6), (84, 30), (86, 60), (50, 66)]), BEAN, 'f', True)])

# Craig Placid: grandullón de piel morena y mandíbula cuadrada enorme; pelo negro en cepillo alto y plano; cejas negras
# gruesas en uve de enfado, ojos entornados y una sonrisa de colmillos
C('craig-placid', 'corpulento', pal('#221e1b', '#dda255', shade='#19130f', deep='#0d0806'),
  F(eyes='none', brows=False, mouth='none', hairline=(56, 56),
    face_front=blob([(18, 50), (50, 44), (82, 50), (88, 80), (86, 110), (50, 116), (14, 110), (12, 80)], 6), ear_out=6),
  [L(outline([(16, 64), (14, 24), (18, 6), (50, 2), (82, 6), (86, 24), (84, 64), (80, 52), (20, 52)])),
   L(outline([(60, 4), (82, 6), (86, 26), (84, 56), (76, 40)]), 'shade', 'b', False)] +
  [L(blob([(22, 62), (44, 72), (44, 76), (22, 68)], 4), BLACK, 'f', False), L(blob([(78, 62), (56, 72), (56, 76), (78, 68)], 4), BLACK, 'f', False),
   L([(30, 78), (42, 80)], BLACK, 'f', False, False, 2.2), L([(70, 78), (58, 80)], BLACK, 'f', False, False, 2.2),
   L(quad((30, 98), (50, 106), (70, 98)), OUTC, 'f', False, False, 1.8), L(outline([(32, 98), (36, 106, 1), (38, 100)]), WHITE, 'f', True),
   L(outline([(68, 98), (64, 106, 1), (62, 100)]), WHITE, 'f', True)],
  crop('side', top=2, nape=78, flat=8) + [L([(72, 64), (86, 72)], BLACK, 'f', False, False, 3), L([(76, 78), (86, 80)], BLACK, 'f', False, False, 2)],
  crop('back', top=2, nape=78, flat=8))

# Crystal Clears: chica de media melena malva en forma de seta, abombada y con las puntas metidas hacia dentro a la altura
# de la barbilla, y flequillo recto; ojos rojos redondos, pecas y sonrisa
C('crystal-clears', 'chica', pal('#865868', '#efd1b6', iris='#c0201a', shade='#614449', deep='#4a3236'),
  F(eyes='big', brows=False, mouth='smile', hairline=hl(7, 70, 60, 64, jit=1, seed=41)),
  bowl('front', top=6, side=96, w=8) + freckles(86, 22),
  bowl('side', top=6, nape=96, w=8),
  bowl('back', top=6, nape=96, w=8))

# Curtis Croon: cara alargada con los lados de la cabeza rapados y un tupé rosa palo altísimo que se echa hacia su
# izquierda y acaba en rizo; ojos afilados de enfado, nariz larga y boca seria
C('curtis-croon', 'delgado', pal('#cd7f79', '#fbbc7b', iris='#1a1210', shade='#a8605a', deep='#81433a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=98, hairline=False, face_front=face(w=-2, chin=112, top=20)),
  [skull(), L(outline([(24, 40), (20, 20), (30, 0), (50, -12), (74, -12), (94, -4), (100, 8), (92, 20), (90, 12), (84, 10), (80, 24), (78, 40), (50, 36)])),
   L(outline([(60, -10), (88, -8), (98, 6), (88, 14), (80, 22), (70, 6)]), 'shade', 'b', False), strand([(36, 4), (56, -6), (78, -4)], 'deep', 'b', 1.0)] + nose(88, 3.6),
  [L(outline([(40, 30), (30, 10), (46, -10), (70, -14), (92, -8), (100, 6), (88, 14), (80, 6), (76, 18), (70, 30), (54, 34)])),
   L(blob([(16, 50), (24, 26), (40, 22), (40, 46)], 8), 'skin')],
  [L(outline([(26, 40), (22, 20), (32, 0), (50, -12), (70, -12), (82, 0), (80, 20), (74, 40), (50, 36)]))])

# Curtis Rebell: señor de pelo castaño oscuro repeinado hacia atrás con las patillas abiertas en punta a los lados, como
# alas; cejas negras gruesas y retorcidas de enfado, nariz larga arrugada y boca torcida
C('curtis-rebell', 'corpulento', pal('#625342', '#f8bc7c', iris='#1a1210', shade='#48392e', deep='#302620'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=100, hairline=[(14, 66), (20, 42), (36, 30), (50, 28), (64, 30), (80, 42), (86, 66)],
    face_front=face(w=2, chin=110, jaw=2)),
  crop('front', top=4, side=66) + [L(outline([(16, 62), (-6, 76, 1), (12, 76), (18, 72)])), L(outline([(84, 62), (106, 76, 1), (88, 76), (82, 72)]))]
  + thick_brows(64, BLACK, 4.6, 15, 1.6, 15) + nose(90, 3.4),
  crop('side', top=4, nape=82) + [L(outline([(46, 60), (28, 76, 1), (40, 76), (52, 70)]))] + side_brow(64, BLACK, 4.6, 1.6),
  crop('back', top=4, nape=82) + [L(outline([(16, 62), (-6, 76, 1), (12, 78), (20, 74)])), L(outline([(84, 62), (106, 76, 1), (88, 78), (80, 74)]))])

# Dale Riverhead (portero): mole de piel morena con la cabeza metida en el cuello; un moñito de sumo azul marino diminuto
# encima de la cabeza rapada; ojos blancos pequeños de enfado y una boca torcida con dos colmillos
C('dale-riverhead', 'corpulento', pal('#302b40', '#ce9466', shade='#201c2c'),
  F(eyes='none', brows=False, mouth='none', hairline=False, face_front=face(w=10, chin=114, jaw=10), ear_out=8),
  [skull(), L(blob([(30, 22), (40, 8), (60, 8), (70, 22), (50, 26)], 6), 'mid'), L(blob([(44, 2), (50, -4), (56, 2), (50, 8)], 4), 'mid'),
   L(ell(36, 72, 5, 4), WHITE, 'f', True), L(ell(64, 72, 5, 4), WHITE, 'f', True), L([(28, 64), (42, 68)], OUTC, 'f', False, False, 2.2), L([(72, 64), (58, 68)], OUTC, 'f', False, False, 2.2),
   L(quad((34, 100), (50, 92), (66, 100)), OUTC, 'f', False, False, 1.8), L(outline([(36, 98), (38, 92, 1), (41, 97)]), WHITE, 'f', True),
   L(outline([(64, 98), (62, 92, 1), (59, 97)]), WHITE, 'f', True)],
  [L(blob([(16, 50), (24, 22), (46, 8), (70, 12), (84, 34), (70, 50)], 10), 'skin'), L(blob([(36, 16), (52, 8), (64, 14), (50, 22)], 6), 'mid'),
   L(blob([(46, 6), (52, 0), (58, 6), (52, 12)], 4), 'mid'), L(ell(80, 72, 3.6, 3.6), WHITE, 'f', True)],
  [L(blob([(18, 60), (20, 28), (50, 10), (80, 28), (82, 60)], 10), 'skin'), L(blob([(32, 26), (42, 12), (58, 12), (68, 26), (50, 30)], 6), 'mid'),
   L(blob([(44, 6), (50, 0), (56, 6), (50, 12)], 4), 'mid')])

# Dan Cawarry: grandullón de cabeza cuadrada y mandíbula ancha; pelo pardo oliva corto, peinado de punta hacia un lado arriba
# y plano por los lados; ojos pequeños de enfado y labios gruesos apretados
C('dan-cawarry', 'corpulento', pal('#6d654d', '#fdc270', iris='#1a1210', shade='#55503c', deep='#3a3628'),
  F(eyes='dot', brows='angry', mouth='lips', mouth_w=8, mouth_y=98, hairline=(54, 50),
    face_front=blob([(16, 50), (50, 40), (84, 50), (88, 80), (84, 106), (50, 114), (16, 106), (12, 80)], 6), ear_out=6),
  crop('front', top=12, side=56, flat=8) + [L(outline([(30, 18), (50, 8), (74, 4), (86, -6, 1), (82, 12), (74, 20)]))],
  crop('side', top=12, nape=76, flat=8) + [L(outline([(52, 12), (76, 4), (90, -6, 1), (84, 14)]))],
  crop('back', top=12, nape=76, flat=8))

# Darren Catt: capucha azul grisácea con orejas de gato puntiagudas; asoma pelo verde negruzco de pinchos por la frente; ojos
# rojos de enfado y una mascarilla crema con dientes en zigzag y nariz rosa de gato
HOOD, HOODD, MSK = c_('#a8cad4'), c_('#527a87'), c_('#efead6')


def _catt(view):
    if view == 'front':
        return [L(outline([(4, 110), (2, 60), (8, 30), (2, -6, 1), (24, 16), (50, 8), (76, 16), (98, -6, 1), (92, 30), (98, 60), (96, 110), (84, 96), (84, 50), (16, 50),
                           (16, 96)]), HOOD, 'b'),
                L(outline([(14, 60), (14, 40), (30, 24), (50, 20), (70, 24), (86, 40), (86, 60), (70, 40), (30, 40)]), HOODD, 'b', False),
                L(blob([(20, 82), (50, 80), (80, 82), (78, 98), (50, 106), (22, 98)], 6), MSK, 'f', True),
                L([(26, 92), (32, 88), (38, 94), (44, 88), (50, 94), (56, 88), (62, 94), (68, 88), (74, 92)], OUTC, 'f', False, False, 1.2),
                L(blob([(46, 82), (54, 82), (50, 87)], 3), c_('#e88a8a'), 'f', True)]
    if view == 'side':
        return [L(outline([(70, 46), (82, 28), (70, 16), (60, -6, 1), (48, 12), (24, 14), (6, 40), (4, 80), (14, 110), (40, 108), (50, 70), (62, 56)]), HOOD),
                L(blob([(70, 82), (90, 80), (92, 98), (74, 104)], 6), MSK, 'f', True)]
    return [L(outline([(6, 110), (2, 60), (8, 30), (2, -6, 1), (24, 16), (50, 8), (76, 16), (98, -6, 1), (92, 30), (98, 60), (94, 110), (50, 116)]), HOOD)]


C('darren-catt', 'normal', pal('#2b2823', '#efd0a8', iris='#c0201e', shade='#1e1c18', deep='#141210'),
  F(eyes='sharp', brows='angry', mouth='none', hairline=hl(6, 70, 52, 68, jit=3, seed=43)),
  _catt('front') + dome('front', top=22, w=36, cy=48, n=7, amp=6, sb=66, seed=43, shade=False),
  _catt('side'), _catt('back'))

# Daryl Floor: pelo rosa muy claro corto y de pinchos, con mechones de punta junto a las orejas; ojos azules grandes de
# pestaña marcada y boca pequeña seria
C('daryl-floor', 'normal', pal('#f4d6df', '#fabb7d', iris='#2a7ac8', shade='#c8a6b0', deep='#8e6966'),
  F(eyes='big', brows='angry', mouth='frown', hairline=hl(5, 64, 50, 58, jit=2, seed=45)),
  dome('front', top=6, w=46, cy=46, n=9, amp=9, sweep=0.1, sb=70, seed=45) + [fr([(14, 60), (20, 58), (12, 84, 1)]), fr([(86, 60), (80, 58), (88, 84, 1)])],
  dome('side', top=6, w=46, cy=46, n=9, amp=9, sweep=0.1, nape=84, fr=50, seed=45),
  dome('back', top=6, w=46, cy=46, n=9, amp=9, sweep=0.1, nape=84, seed=45))

# Dave Lung (portero): escafandra de buzo azul redonda que le tapa la cabeza entera, con una ventanilla oscura de marco
# dorado con cruz y remaches, y el cuello de goma azul
DIVE, BRASS, PORT = c_('#3e74aa'), c_('#efc764'), c_('#281e2d')


def _dive(view):
    if view == 'front':
        return [L(ell(50, 50, 48, 50), DIVE, 'f', True), L(blob([(4, 50), (96, 50), (96, 62), (4, 62)], 4), BRASS, 'f', True),
                L(ell(50, 56, 20, 20), BRASS, 'f', True), L(ell(50, 56, 15, 15), PORT, 'f', False),
                L([(50, 41), (50, 71)], BRASS, 'f', False, False, 2.6), L([(35, 56), (65, 56)], BRASS, 'f', False, False, 2.6),
                L(blob([(20, 96), (80, 96), (84, 106), (16, 106)], 4), c_('#2a5a8a'), 'f', True)]
    if view == 'side':
        return [L(ell(50, 50, 48, 50), DIVE, 'f', True), L(blob([(70, 50), (98, 50), (98, 62), (70, 62)], 4), BRASS, 'f', True),
                L(ell(90, 56, 8, 18), BRASS, 'f', True), L(blob([(22, 96), (78, 96), (80, 106), (20, 106)], 4), c_('#2a5a8a'), 'f', True)]
    return [L(ell(50, 50, 48, 50), DIVE, 'f', True), L(blob([(4, 50), (96, 50), (96, 62), (4, 62)], 4), BRASS, 'f', True),
            L(blob([(20, 96), (80, 96), (84, 106), (16, 106)], 4), c_('#2a5a8a'), 'f', True)]


C('dave-lung', 'normal', pal('#3e74aa', '#f1c79b', shade='#2a5a8a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _dive('front'), _dive('side'), _dive('back'))

# Del Brighton: pelo granate oscuro abundante y ondulado en mechones que le caen por la frente y abultan por los lados;
# piel clara, ojos afilados y media sonrisa
C('del-brighton', 'normal', pal('#622434', '#f4ecc9', iris='#2a1414', shade='#4f1d28', deep='#3c191e'),
  F(eyes='sharp', brows='angry', mouth='smile', hairline=hl(6, 68, 50, 66, lean=3, jit=3, seed=47)),
  dome('front', top=2, w=50, cy=46, n=8, amp=8, soft=True, sweep=0.3, sb=78, seed=47) + [fr([(42, 40), (62, 42), (52, 70, 1)])],
  dome('side', top=2, w=50, cy=46, n=8, amp=8, soft=True, sweep=0.3, nape=86, fr=54, seed=47),
  dome('back', top=2, w=50, cy=46, n=8, amp=8, soft=True, sweep=0.3, nape=86, seed=47))

# Des Igner: piel tostada, pelo azul marino de pinchos altos de punta, con las patillas largas hasta la mandíbula; un
# antifaz de tela crema con dos círculos verde oscuro le tapa los ojos; boca triste
SLEEP, DOT = c_('#e5e0cb'), c_('#3a5a3a')
C('des-igner', 'normal', pal('#3a4b5c', '#dba25a', shade='#2e3c4a', deep='#202a34'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, hairline=hl(5, 64, 52, 58, jit=2, seed=49)),
  dome('front', top=0, w=44, cy=48, n=8, amp=12, sweep=0.5, sb=92, seed=49) +
  [L(blob([(10, 66), (50, 60), (90, 66), (88, 82), (50, 84), (12, 82)], 6), SLEEP, 'f', True), L(ell(36, 73, 7, 5), DOT, 'f', True), L(ell(64, 73, 7, 5), DOT, 'f', True)],
  dome('side', top=0, w=44, cy=48, n=8, amp=12, sweep=0.5, nape=86, fr=56, seed=49) + [L(blob([(60, 64), (92, 64), (92, 82), (60, 82)], 6), SLEEP, 'f', True),
                                                                                     L(ell(84, 73, 5, 5), DOT, 'f', True)],
  dome('back', top=0, w=44, cy=48, n=8, amp=12, sweep=0.5, nape=86, seed=49) + [L(quad((8, 72), (50, 78), (92, 72)), SLEEP, 'f', False, False, 4)])

# Dexter Caise: pelo morado pizarra oscuro en melena lisa con flequillo recto y largo, cortado a la altura del cuello; ojos
# blancos redondos enormes con la pupila diminuta y una sonrisa ancha
C('dexter-caise', 'normal', pal('#555065', '#f7bc7e', shade='#413843', deep='#302a2f'),
  F(eyes='none', brows=False, mouth='smile', mouth_w=12, hairline=hl(8, 72, 62, 64, jit=0.5, seed=51)),
  [L(outline([(10, 108), (8, 60), (14, 26), (32, 6), (50, 0), (68, 6), (86, 26), (92, 60), (90, 108), (80, 108), (80, 60), (20, 60), (20, 108)])),
   L(outline([(62, 4), (84, 20), (92, 60), (90, 106), (82, 104), (80, 50)]), 'shade', 'b', False),
   L(ell(36, 76, 7, 6), WHITE, 'f', True), L(ell(64, 76, 7, 6), WHITE, 'f', True), L(ell(36, 76, 1.6, 1.6), BLACK, 'f', False), L(ell(64, 76, 1.6, 1.6), BLACK, 'f', False),
   L(quad((36, 90), (50, 100), (64, 90)), MOUTH, 'f', False, False, 1.6)],
  [L(outline([(80, 60), (88, 40), (78, 12), (54, 0), (28, 4), (10, 24), (4, 60), (6, 106), (40, 108), (48, 64), (62, 62)])),
   L(ell(84, 76, 4.6, 5.6), WHITE, 'f', True), L(ell(85, 76, 1.4, 1.4), BLACK, 'f', False)],
  [L(outline([(8, 108), (6, 60), (12, 26), (30, 6), (50, 0), (70, 6), (88, 26), (94, 60), (92, 108), (50, 112)])),
   L(outline([(60, 4), (84, 20), (92, 60), (90, 106), (62, 110)]), 'shade', 'b', False)])

# Dom Edarry: cara alargada morena, pañuelo blanco grisáceo sobre la cabeza que cae por los lados hasta el cuello, sujeto con
# un cordón trenzado rojo y blanco; ojos de párpado caído, nariz larga y boca triste
SCARF, SCARFD, AGAL = c_('#ced6c7'), c_('#9f9f96'), c_('#c02020')


def _keffiyeh(view):
    if view == 'front':
        out = [L(outline([(8, 112), (6, 60), (12, 26), (30, 6), (50, 0), (70, 6), (88, 26), (94, 60), (92, 112), (80, 112), (80, 62), (20, 62), (20, 112)]), SCARF),
               L(outline([(64, 6), (86, 24), (94, 60), (92, 110), (82, 110), (82, 54)]), SCARFD, 'b', False),
               L(blob([(6, 54), (50, 48), (94, 54), (94, 64), (50, 58), (6, 64)], 4), WHITE, 'f', True)]
        for x in range(10, 92, 10):
            out.append(L([(x, 54 + abs(50 - x) * 0.06), (x + 6, 62 + abs(50 - x) * 0.06)], AGAL, 'f', False, False, 3.0))
        return out
    if view == 'side':
        return [L(outline([(78, 62), (84, 30), (66, 4), (36, 2), (12, 20), (2, 60), (0, 112), (40, 114), (52, 66)]), SCARF),
                L(blob([(10, 50), (82, 54), (84, 64), (10, 60)], 4), WHITE, 'f', True), L([(20, 52), (78, 58)], AGAL, 'f', False, False, 2.6)]
    return [L(outline([(6, 114), (6, 60), (12, 26), (30, 6), (50, 0), (70, 6), (88, 26), (94, 60), (94, 114), (50, 118)]), SCARF),
            L(outline([(60, 6), (86, 24), (94, 60), (94, 112), (64, 116)]), SCARFD, 'b', False),
            L(blob([(6, 54), (50, 48), (94, 54), (94, 64), (50, 58), (6, 64)], 4), WHITE, 'f', True), L(quad((6, 58), (50, 52), (94, 58)), AGAL, 'f', False, False, 2.6)]


C('dom-edarry', 'delgado', pal('#ced6c7', '#ce9568', iris='#1a1210', shade='#9f9f96'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=100, hairline=False, face_front=face(w=-2, chin=112)),
  _keffiyeh('front') + nose(88, 3.4) + [L([(26, 70), (42, 72)], OUTC, 'f', False, False, 2.2), L([(74, 70), (58, 72)], OUTC, 'f', False, False, 2.2)],
  _keffiyeh('side'), _keffiyeh('back'))

# Dom Round: cabeza pequeña y muy redonda de orejas grandes, casi calva, con un remolino de pelo gris morado que se echa a un
# lado encima; ojos de párpado caído y boca enfurruñada
C('dom-round', 'bajito', pal('#867c88', '#fdc271', iris='#1a1210', shade='#62565c', deep='#4a4048'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=94, hairline=False, big_ears=2, ear_out=3,
    face_front=blob([(18, 50), (50, 30), (82, 50), (86, 76), (76, 98), (50, 106), (24, 98), (14, 76)], 6)),
  [skull(), L(outline([(30, 30), (40, 14), (60, 10), (78, 22), (82, 40), (72, 30), (58, 24), (44, 28)])),
   L([(26, 70), (42, 72)], OUTC, 'f', False, False, 2.4), L([(74, 70), (58, 72)], OUTC, 'f', False, False, 2.4)],
  [L(blob([(16, 50), (24, 22), (46, 8), (70, 12), (84, 34), (70, 50)], 10), 'skin'), L(outline([(40, 14), (60, 8), (82, 24), (84, 40), (70, 28), (50, 22)]))],
  [L(blob([(18, 60), (20, 28), (50, 10), (80, 28), (82, 60)], 10), 'skin'), L(outline([(26, 34), (40, 14), (62, 10), (76, 22), (64, 26), (44, 30)]))])

# Dom Yellow D. Poppy (portero): máscara negra con dos llamas amarillas en los ojos y orejeras plateadas, un mechón castaño
# rojizo de punta asomando arriba y la parte de abajo envuelta en tela negra; dientes apretados
MASKB, MYEL, MSIL = c_('#2a2a2c'), c_('#f3dd27'), c_('#8a8a90')


def _poppy(view):
    if view == 'front':
        return [L(outline([(36, 10), (50, -6), (74, -10, 1), (62, 6)]), c_('#6a2a10'), 'b'),
                L(blob([(14, 74), (16, 40), (30, 14), (50, 8), (70, 14), (84, 40), (86, 74), (50, 80)], 8), MASKB, 'f', True),
                L(outline([(24, 62), (42, 72), (46, 66), (32, 50)]), MYEL, 'f', False), L(outline([(76, 62), (58, 72), (54, 66), (68, 50)]), MYEL, 'f', False),
                L(blob([(6, 50), (18, 48), (20, 76), (8, 78)], 6), MSIL, 'f', True), L(blob([(94, 50), (82, 48), (80, 76), (92, 78)], 6), MSIL, 'f', True),
                L(blob([(16, 90), (34, 98), (50, 100), (66, 98), (84, 90), (84, 108), (50, 116), (16, 108)], 6), MASKB, 'f', True),
                L(blob([(38, 88), (62, 88), (60, 95), (40, 95)], 4), WHITE, 'f', True), L([(40, 91.5), (60, 91.5)], OUTC, 'f', False, False, 0.8)]
    if view == 'side':
        return [L(outline([(40, 10), (54, -4), (76, -6, 1), (62, 8)]), c_('#6a2a10'), 'b'),
                L(blob([(30, 70), (28, 30), (50, 10), (76, 18), (90, 46), (90, 74), (60, 80)], 8), MASKB, 'f', True),
                L(outline([(76, 60), (90, 68), (90, 60), (82, 52)]), MYEL, 'f', False), L(blob([(40, 50), (54, 50), (54, 76), (40, 76)], 6), MSIL, 'f', True),
                L(blob([(56, 90), (90, 92), (88, 108), (60, 114)], 6), MASKB, 'f', True)]
    return [L(outline([(36, 10), (50, -6), (74, -10, 1), (62, 6)]), c_('#6a2a10'), 'b'),
            L(blob([(14, 80), (16, 40), (30, 14), (50, 8), (70, 14), (84, 40), (86, 80), (50, 86)], 8), MASKB, 'f', True),
            L(blob([(6, 50), (18, 48), (20, 76), (8, 78)], 6), MSIL, 'f', True), L(blob([(94, 50), (82, 48), (80, 76), (92, 78)], 6), MSIL, 'f', True),
            L(outline([(40, 76), (34, 104, 1), (50, 90), (64, 106, 1), (60, 76)]), MASKB, 'f', True)]


C('dom-yellow-d-poppy', 'normal', pal('#6a2a10', '#aa7a5a', shade='#4a1e0a'),
  F(eyes='none', brows=False, mouth='none', hairline=False),
  _poppy('front'), _poppy('side'), _poppy('back'))

# Dory O'Bonn: chica de cara afilada y piel clara con el pelo rojo granate liso peinado hacia atrás, largo por detrás, y un
# mechón suelto que le cae sobre el ojo derecho; ojos entornados de mala uva y boca pequeña apretada
C('dory-o-bonn', 'chica', pal('#a24948', '#f5bd93', iris='#5a3a1a', shade='#7e3532', deep='#5e2927'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, hairline=[(14, 70), (22, 44), (36, 32), (50, 28), (64, 32), (78, 44), (86, 70)],
    face_front=face(w=-3, chin=110, jaw=-2)),
  longhair('front', length=114, flare=2, ends=3) + [fr([(34, 30), (42, 30), (40, 84, 1), (32, 60)])] + nose(88, 2.4),
  longhair('side', length=114, flare=2, ends=3),
  longhair('back', length=114, flare=2, ends=4))
