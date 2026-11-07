"""Ojeadores de IE2 (scouts-ie2), tanda 01: dibujados a partir de su retrato de Victory Road; claves 'scouts-ie2:<id>'.

Casi ninguno tiene modelo 3D: el frente sale del retrato y el perfil y la espalda se deducen de cómo cae ese peinado.
Se apoya en las ayudas de los ojeadores de IE1 (dome/hl/face de la tanda 09, gafas y cejas de la 03, crop de Twinford)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars import messy  # noqa: F401
from chars_scouts_ie1_09 import dome, hl, face, face_side, F, P, mark, _c  # noqa: F401
from chars_scouts_ie1_03 import (skull, round_specs, goggles, thick_brows, side_brow, freckles, big_grin, stache, tri_nose,  # noqa: F401
                                 eyes_custom, side_eye_custom, blush, rect_specs, shades, lashes_out)
from chars_vr_nikogawa import crop  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)
GREY = (150, 150, 156, 255)
PINK = (238, 140, 140, 255)
BROWN = (150, 90, 50, 255)


def C(pid, body, palette, f, front, side, back):
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        # el nacimiento del pelo baja por el borde de la cara hasta la barbilla: así su raya no cruza el pelo de los lados
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[f'scouts-ie2:{pid}'] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def three(fn, **k):
    return [fn(v, **k) for v in ('front', 'side', 'back')]


def fr(pts, c='mid'):
    """Mechón por delante de la cara."""
    return L(outline(pts), c, 'f')


def sq_face(w=4, chin=108):
    """Cara cuadrada de mandíbula ancha."""
    return blob([(14 - w, 50), (50, 34), (86 + w, 50), (88 + w, 80), (84 + w, 100), (66, chin), (50, chin + 1), (34, chin), (16 - w, 100), (12 - w, 80)], 6)


def headband(view, y=44, h=9, c='band', knot=True):
    """Cinta en la frente; de frente con un nudo en medio."""
    if view == 'front':
        out = [L(outline([(10, y + 2), (50, y - 2), (90, y + 2), (90, y + h + 2), (50, y + h - 2), (10, y + h + 2)]), c, 'f')]
        if knot:
            out.append(L(outline([(42, y - 4), (58, y - 4), (54, y + h + 6), (50, y + h + 10, 1), (46, y + h + 6)]), c, 'f'))
        return out
    if view == 'side':
        return [L(outline([(10, y - 2), (88, y + 2), (88, y + h + 2), (10, y + h)]), c, 'f')]
    return [L(outline([(8, y + 2), (50, y - 1), (92, y + 2), (92, y + h + 2), (50, y + h - 1), (8, y + h + 2)]), c, 'f')]


# ------------------------------------------------------------------ jugadores

# Ace Slider (portero): pelo corto verde oliva con un pincho de punta en la coronilla; cejas gruesas fruncidas, ceño, nariz
# marcada y orejas grandes
C('ace-slider', 'normal', P('#5f511e', '#f8c072', iris='#1e1a16'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=94, big_ears=1, nose=(50, 86, 2.4),
    hairline=[(8, 62), (18, 54), (34, 52), (50, 54), (66, 52), (82, 54), (92, 62)]),
  crop('front', top=4, side=60, w=1) + [L(outline([(40, 10), (48, -6, 1), (54, 6), (62, -2, 1), (64, 12)]))] + thick_brows(64, _c('#3e3414'), 4.2, 15, 1.4, 14),
  crop('side', top=4, nape=80, w=1) + [L(outline([(40, 8), (50, -6, 1), (56, 6), (66, -2, 1), (68, 10)]))] + side_brow(64, _c('#3e3414'), 4.2, 1.4),
  crop('back', top=4, nape=80, w=1) + [L(outline([(40, 10), (48, -6, 1), (54, 6), (62, -2, 1), (64, 12)]))])

# Achilles Chinner (portero): grandullón de piel gris parda y cara cuadrada; pelo verde azulado oscuro corto y plano con dos
# cuernos de pelo a los lados; chapa de metal en la barbilla, dos colmillos y cicatrices en las mejillas
TEAL, METAL = _c('#3e6662'), _c('#a8a8ac')
def _horns(view):
    if view == 'front':
        return [L(outline([(10, 52), (12, 30), (30, 18), (50, 16), (70, 18), (88, 30), (90, 52), (80, 44), (20, 44)]), TEAL),
                L(outline([(14, 34), (2, 12, 1), (24, 24)]), TEAL), L(outline([(86, 34), (98, 12, 1), (76, 24)]), TEAL),
                L(outline([(46, 20), (50, 34, 1), (54, 20)]), TEAL, 'f')]
    if view == 'side':
        return [L(outline([(74, 44), (84, 30), (70, 16), (44, 14), (20, 20), (8, 36), (8, 56), (20, 62), (40, 56), (56, 50)]), TEAL),
                L(outline([(30, 24), (20, 2, 1), (44, 18)]), TEAL)]
    return [L(outline([(10, 62), (12, 30), (30, 18), (50, 16), (70, 18), (88, 30), (90, 62), (50, 66)]), TEAL),
            L(outline([(14, 34), (2, 12, 1), (24, 24)]), TEAL), L(outline([(86, 34), (98, 12, 1), (76, 24)]), TEAL)]
C('achilles-chinner', 'corpulento', P('#3e6662', '#ad8e77', iris='#1e1a16'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=96, hairline=False, face_front=sq_face(4, 112), face_side=face_side(chin=8, jaw=6)),
  _horns('front') + [L(blob([(36, 102), (64, 102), (64, 114), (36, 114)], 3), METAL, 'f', True),
                     L([(38, 108), (62, 108)], GREY, 'f', False, False, 0.8),
                     L([(37, 96), (40, 89), (43, 96)], WHITE, 'f', False), L([(57, 96), (60, 89), (63, 96)], WHITE, 'f', False),
                     L([(46, 88), (54, 88)], _c('#e07a2a'), 'f', False, False, 2.2),
                     L([(18, 80), (26, 84)], _c('#7a5e4c'), 'f', False, False, 1.0), L([(19, 85), (26, 89)], _c('#7a5e4c'), 'f', False, False, 1.0),
                     L([(82, 80), (74, 84)], _c('#7a5e4c'), 'f', False, False, 1.0)],
  _horns('side') + [L(blob([(70, 102), (88, 100), (88, 112), (70, 114)], 3), METAL, 'f', True), L([(84, 96), (86, 89), (88, 96)], WHITE, 'f', False)],
  _horns('back'))

# Adel Tactor: chica de melena corta castaño rojizo con flequillo recto y las puntas abiertas hacia fuera a la altura de la
# barbilla; ojos grandes con pestañas y sonrisa
C('adel-tactor', 'chica', P('#884b3f', '#fabd7c', iris='#2a1a16'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=[(8, 64), (16, 54), (30, 56), (50, 56), (70, 56), (84, 54), (92, 64)]),
  [L(outline([(16, 64), (10, 40), (22, 14), (50, 4), (78, 14), (90, 40), (84, 64), (90, 84), (98, 96, 1), (82, 92), (76, 70), (80, 52), (20, 52), (24, 70), (18, 92),
              (2, 96, 1), (10, 84)])),
   L(outline([(60, 8), (80, 18), (90, 42), (86, 64), (78, 46)]), 'shade', 'b', False),
   fr([(18, 56), (20, 34), (36, 22), (50, 20), (64, 22), (80, 34), (82, 56), (70, 58), (60, 56), (50, 58), (40, 56), (30, 58)])] + lashes_out(75, 14),
  [L(outline([(70, 50), (82, 40), (82, 20), (60, 4), (32, 6), (12, 20), (4, 46), (6, 74), (12, 88), (2, 98, 1), (20, 96), (36, 90), (44, 76), (52, 62), (60, 56)])),
   L(outline([(4, 48), (30, 54), (42, 76), (32, 90), (16, 94), (8, 76)]), 'shade', 'b', False),
   fr([(64, 10), (84, 22), (90, 44), (84, 56), (76, 50), (72, 34)])],
  [L(outline([(12, 70), (8, 40), (22, 14), (50, 4), (78, 14), (92, 40), (88, 70), (92, 86), (100, 98, 1), (78, 94), (50, 96), (22, 94), (0, 98, 1), (8, 86)])),
   L(outline([(60, 10), (82, 20), (92, 44), (88, 76), (94, 94), (74, 94), (70, 50)]), 'shade', 'b', False)])

# Adelpha Lovelace: chica morena con melena corta amarilla que le tapa las orejas, un rizo en espiral sobre la frente y dos
# coletitas tiesas hacia arriba con gomas verdes; ojos redondos grandes
YELL, YLIGHT, GTIE = _c('#f8c838'), _c('#fde24f'), _c('#5a9a30')
def _pig(cx, view='front'):
    s = 1 if cx > 50 else -1
    return [L(outline([(cx - 4 * s, 18), (cx + 2 * s, 0), (cx + 6 * s, -18), (cx + 12 * s, -22), (cx + 16 * s, -14), (cx + 10 * s, 4), (cx + 4 * s, 20)]), 'mid', 'b'),
            L(ell(cx + 1 * s, 14, 4.4, 3.6), GTIE, 'b', True)]
C('adelpha-lovelace', 'chica', P('#f8c838', '#c18847', iris='#1a2a3a', light='#fde24f'),
  F(eyes='round', brows=False, mouth='smile', mouth_y=94, hairline=[(8, 66), (16, 60), (30, 56), (50, 54), (70, 56), (84, 60), (92, 66)]),
  _pig(24) + _pig(76) +
  [L(outline([(14, 90), (6, 60), (10, 32), (28, 14), (50, 8), (72, 14), (90, 32), (94, 60), (86, 90), (76, 76), (80, 56), (20, 56), (24, 76)])),
   L(outline([(60, 12), (80, 22), (92, 46), (90, 78), (84, 86), (80, 56), (70, 34)]), 'shade', 'b', False),
   fr([(22, 58), (24, 36), (40, 24), (50, 22), (60, 24), (76, 36), (78, 58), (64, 56), (50, 60), (36, 56)]),
   L(ell(50, 46, 9, 9), 'light', 'f', True),
   strand([(50, 46), (54, 44), (52, 40), (46, 42), (45, 48), (50, 52), (57, 49), (58, 42)], 'shade', 'f', 1.4)],
  [L(outline([(28, 20), (24, -2), (30, -20), (38, -18), (36, 0), (38, 20)])), L(ell(32, 16, 4, 3.6), GTIE, 'b', True),
   L(outline([(72, 54), (84, 40), (84, 20), (62, 6), (34, 8), (14, 22), (6, 50), (8, 80), (16, 92), (36, 90), (44, 76), (52, 60), (60, 56)])),
   L(outline([(6, 52), (30, 56), (42, 76), (34, 90), (16, 90), (8, 76)]), 'shade', 'b', False),
   fr([(68, 12), (86, 24), (92, 46), (86, 58), (78, 52), (74, 36)])],
  _pig(24) + _pig(76) +
  [L(outline([(10, 88), (6, 60), (10, 32), (28, 14), (50, 8), (72, 14), (90, 32), (94, 60), (90, 88), (50, 94)])),
   L(outline([(60, 12), (80, 22), (92, 46), (92, 84), (70, 92), (68, 50)]), 'shade', 'b', False)])

# Adrian Heartly: pelo verde azulado peinado hacia atrás y recogido en un mechón tieso que sale hacia un lado de la coronilla,
# con otro mechón que le cae por detrás de la oreja; ojos redondos y boca pequeña de enfado
C('adrian-heartly', 'normal', P('#1f6c67', '#f9bc7c', iris='#1a1a1a', shade='#18514d'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=94, nose=(50, 86, 1.8), big_ears=1, hairline=[(10, 60), (20, 48), (36, 42), (50, 42), (64, 42), (80, 48), (90, 60)]),
  [L(outline([(16, 62), (10, 40), (18, 18), (36, 6), (60, 4), (80, 12), (90, 30), (88, 56), (80, 46), (20, 46)])),
   L(outline([(72, 14), (90, 0), (104, -4, 1), (98, 12), (104, 22, 1), (88, 26)])),
   L(outline([(14, 56), (8, 76), (12, 96, 1), (20, 82), (22, 62)])),
   strand([(30, 40), (34, 22), (44, 10)], 'shade', 'b', 1.0), strand([(50, 40), (54, 22), (64, 10)], 'shade', 'b', 1.0), strand([(68, 42), (74, 26), (82, 16)], 'shade', 'b', 1.0)],
  [L(outline([(70, 46), (82, 40), (84, 22), (68, 6), (40, 2), (18, 10), (4, 30), (2, 52), (8, 66), (20, 72), (34, 62), (44, 56), (56, 50)])),
   L(outline([(20, 12), (8, -6), (0, -12, 1), (4, 4), (-6, 10, 1), (8, 20)])),
   strand([(76, 38), (56, 14), (30, 8)], 'shade', 'b', 1.0), strand([(70, 46), (46, 26), (16, 22)], 'shade', 'b', 1.0)],
  [L(outline([(16, 76), (10, 44), (18, 18), (36, 6), (64, 6), (82, 18), (90, 44), (84, 76), (50, 82)])),
   L(outline([(60, 12), (78, 0), (96, -6, 1), (92, 10), (100, 20, 1), (84, 24)])),
   strand([(40, 10), (42, 40), (40, 70)], 'shade', 'b', 1.0), strand([(60, 10), (60, 40), (62, 70)], 'shade', 'b', 1.0)])

# Al Itchen: pelo gris pizarra oscuro de pinchos revueltos que le caen por la frente; ojos cerrados y caídos de pena, pecas
# y boca temblorosa
C('al-itchen', 'normal', P('#414d59', '#f9bc7d', iris='#1a1a1a', shade='#2e2c30'),
  F(eyes='none', brows=False, mouth='none', hairline=hl(7, 62, 50, 60, jit=3, seed=11)),
  messy('front', amp=8, n=12, seed=61, lo=66) +
  [L(quad((28, 78), (36, 82), (44, 78)), OUTC, 'f', False, False, 2.0), L(quad((56, 78), (64, 82), (72, 78)), OUTC, 'f', False, False, 2.0),
   L([(28, 68), (40, 72)], OUTC, 'f', False, False, 1.4), L([(72, 68), (60, 72)], OUTC, 'f', False, False, 1.4),
   L([(42, 97), (46, 95), (50, 97), (54, 95), (58, 97)], OUTC, 'f', False, False, 1.6)] + freckles(86, 22),
  messy('side', amp=8, n=12, seed=61, lo=66) + [L(quad((76, 78), (81, 81), (86, 78)), OUTC, 'f', False, False, 2.0)],
  messy('back', amp=8, n=12, seed=61, lo=66))

# Al Stringer: gorro de buzo azul claro con remaches que le tapa la cabeza hasta las orejas, gafas redondas verdes de
# cristal amarillo y nariz gorda; la parte de abajo de la cara oscura, como una barba de tres días, y boca de dientes
HAT, HAT_D, GOG, LENS = _c('#abcfd6'), _c('#7b9499'), _c('#41622a'), _c('#c8b830')
def _helmet(view):
    if view == 'front':
        return [L(outline([(6, 80), (8, 40), (18, 10), (50, 2), (82, 10), (92, 40), (94, 80), (84, 84), (82, 62), (18, 62), (16, 84)]), HAT),
                L(outline([(60, 6), (82, 12), (92, 42), (92, 78), (84, 82), (80, 60), (72, 30)]), HAT_D, 'b', False)] + \
               [L(ell(x, y, 3.2, 4.2), WHITE, 'b', True) for x, y in ((30, 20), (50, 14), (70, 20), (16, 48), (84, 48))]
    if view == 'side':
        return [L(outline([(86, 62), (90, 36), (76, 10), (48, 2), (20, 10), (4, 36), (2, 70), (14, 90), (40, 90), (48, 70), (60, 64)]), HAT),
                L(outline([(4, 40), (40, 46), (46, 70), (40, 88), (14, 88), (4, 70)]), HAT_D, 'b', False)] + \
               [L(ell(x, y, 3.2, 4.2), WHITE, 'b', True) for x, y in ((62, 16), (38, 12), (16, 34), (20, 64))]
    return [L(outline([(6, 86), (8, 40), (18, 10), (50, 2), (82, 10), (92, 40), (94, 86), (50, 92)]), HAT),
            L(outline([(60, 6), (82, 12), (92, 42), (92, 84), (66, 90), (68, 40)]), HAT_D, 'b', False)] + \
           [L(ell(x, y, 3.2, 4.2), WHITE, 'b', True) for x, y in ((30, 22), (50, 16), (70, 22), (24, 56), (50, 52), (76, 56))]
C('al-stringer', 'normal', P('#abcfd6', '#da9e63', iris='#1a1a1a'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=98, hairline=False),
  _helmet('front') + [L(blob([(20, 86), (50, 84), (80, 86), (76, 100), (60, 110), (50, 112), (40, 110), (24, 100)], 6), _c('#8a7458'), 'f', False),
                      L(ell(36, 74, 10, 9), GOG, 'f', True), L(ell(64, 74, 10, 9), GOG, 'f', True),
                      L(ell(36, 75, 6, 4.4), LENS, 'f', False), L(ell(64, 75, 6, 4.4), LENS, 'f', False),
                      L(ell(50, 86, 7, 5.6), _c('#a8683a'), 'f', True),
                      L(blob([(40, 96), (60, 96), (60, 102), (40, 102)], 3), WHITE, 'f', True), L([(40, 99), (60, 99)], OUTC, 'f', False, False, 0.8)],
  _helmet('side') + [L(blob([(60, 86), (88, 86), (86, 100), (72, 108), (60, 104)], 6), _c('#8a7458'), 'f', False),
                     L(ell(82, 74, 6, 8), GOG, 'f', True), L(ell(84, 75, 3, 4), LENS, 'f', False), L(ell(90, 86, 4, 5), _c('#c88a52'), 'f', True)],
  _helmet('back'))

# Alex Copple (portero): melena negra larga y ondulada que le cae hasta los hombros, cinta naranja en la frente con el nudo
# en medio, ojos azules afilados, tirita en la nariz y una cruz cicatrizada en la mejilla
C('alex-copple', 'normal', P('#2e2d33', '#d8a061', iris='#3a6ac8', shade='#202024', band='#e05a24'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=96, hairline=[(8, 64), (14, 50), (30, 46), (50, 48), (70, 46), (86, 50), (92, 64)]),
  dome('front', top=-2, w=50, cy=44, n=10, amp=8, soft=True, seed=21, long=112, flare=10) + headband('front', 42, 8) +
  [L(blob([(44, 84), (56, 84), (56, 89), (44, 89)], 2), _c('#f0d0a8'), 'f', True),
   L([(64, 92), (70, 98)], OUTC, 'f', False, False, 1.2), L([(70, 92), (64, 98)], OUTC, 'f', False, False, 1.2)],
  dome('side', top=-2, w=50, cy=44, n=10, amp=8, soft=True, seed=21, long=112, flare=10, fr=48) + headband('side', 42, 8),
  dome('back', top=-2, w=50, cy=44, n=10, amp=8, soft=True, seed=21, long=112, flare=10, ends=6) + headband('back', 42, 8, knot=False))

# Alexis Watchorn: chica rubia con dos tirabuzones gordos a los lados de la cara y una boina blanca con cinta gris azulada
# ladeada; ojos verde agua con pestañas y sonrisa
BERET, BAND = _c('#f4f2f0'), _c('#6a7e86')
def _beret(view):
    if view == 'front':
        return [L(blob([(8, 36), (20, 12), (50, 4), (84, 8), (100, 22), (96, 36), (60, 38), (24, 42)], 8), BERET, 'f'),
                L(outline([(10, 38), (50, 34), (94, 32), (94, 40), (50, 42), (12, 46)]), BAND, 'f', False)]
    if view == 'side':
        return [L(blob([(6, 30), (20, 6), (54, 0), (84, 8), (96, 26), (80, 34), (40, 36)], 8), BERET, 'f'),
                L(outline([(10, 32), (50, 34), (90, 30), (90, 38), (50, 42), (12, 40)]), BAND, 'f', False)]
    return [L(blob([(4, 34), (18, 8), (50, 2), (84, 8), (98, 30), (80, 40), (20, 40)], 8), BERET, 'f'),
            L(outline([(8, 36), (50, 40), (94, 36), (94, 44), (50, 48), (8, 44)]), BAND, 'f', False)]
def _ringlet(cx, cy, s):
    return [L(blob([(cx - 4 * s, cy - 12), (cx + 6 * s, cy - 10), (cx + 8 * s, cy + 2), (cx + 2 * s, cy + 10), (cx - 8 * s, cy + 8), (cx - 6 * s, cy)], 6)),
            strand([(cx - 4 * s, cy - 4), (cx + 2 * s, cy - 2), (cx + 1 * s, cy + 4)], 'shade', 'b', 1.0)]
C('alexis-watchorn', 'chica', P('#e8b83a', '#fdcf9f', iris='#2a9a94', shade='#b98131'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=[(8, 62), (16, 50), (30, 46), (50, 48), (70, 46), (84, 50), (92, 62)]),
  _ringlet(10, 86, -1) + _ringlet(90, 86, 1) +
  [L(outline([(14, 74), (10, 44), (24, 26), (50, 20), (76, 26), (90, 44), (86, 74), (80, 52), (20, 52)])),
   fr([(18, 56), (24, 40), (40, 34), (50, 40), (56, 34), (76, 40), (82, 56), (70, 50), (52, 44), (40, 50)])] + _beret('front') + lashes_out(75, 14),
  _ringlet(30, 88, -1) + [L(outline([(70, 48), (82, 40), (80, 24), (60, 16), (32, 18), (12, 30), (6, 54), (14, 76), (32, 78), (44, 62), (56, 52)]))] + _beret('side'),
  _ringlet(10, 86, -1) + _ringlet(90, 86, 1) + [L(outline([(12, 80), (8, 44), (24, 26), (50, 20), (76, 26), (92, 44), (88, 80), (50, 86)]))] + _beret('back'))

# Algy Kelp: pelo verde oscuro con un flequillo en punta que le baja por el centro hasta la nariz y mechones sueltos a los
# lados; orejas puntiagudas, piel pálida y ojos amarillos rasgados sin pupila
SLIT = _c('#f0c830')
def _slit(cx, s):
    return [L(blob([(cx - 8 * s, 80), (cx - 2 * s, 72), (cx + 6 * s, 68), (cx + 2 * s, 78)], 4), SLIT, 'f', True)]
C('algy-kelp', 'normal', P('#0a4a24', '#e5d2b6', iris='#1a1a1a', shade='#05321a'),
  F(eyes='none', brows=False, mouth='line', mouth_y=96, nose=(50, 88, 1.4), ears=False, hairline=False),
  [L(outline([(8, 64), (2, 70, 1), (6, 54), (2, 40, 1), (10, 32), (22, 12), (50, 2), (78, 12), (90, 32), (98, 40, 1), (94, 54), (98, 70, 1), (92, 64), (82, 54), (18, 54)])),
   L(outline([(12, 70), (-6, 60, 1), (10, 78), (20, 74)]), 'skin'), L(outline([(88, 70), (106, 60, 1), (90, 78), (80, 74)]), 'skin'),
   fr([(16, 58), (20, 40), (36, 30), (50, 28), (64, 30), (80, 40), (84, 58), (72, 48), (58, 60), (50, 84, 1), (42, 60), (28, 48)]),
   fr([(10, 60), (4, 86), (2, 104, 1), (12, 90), (18, 66)]), fr([(90, 60), (96, 86), (98, 104, 1), (88, 90), (82, 66)])] + _slit(34, 1) + _slit(66, -1),
  [L(outline([(70, 52), (84, 44), (84, 24), (62, 6), (34, 6), (14, 18), (2, 40), (-4, 56, 1), (6, 62), (4, 84, 1), (16, 78), (26, 86, 1), (36, 72), (52, 60)])),
   L(outline([(44, 64), (30, 50, 1), (40, 76)]), 'skin'),
   fr([(68, 8), (86, 24), (92, 46), (96, 60, 1), (84, 52), (76, 36)])] + [L(blob([(78, 76), (82, 70), (90, 68), (86, 78)], 4), SLIT, 'f', True)],
  [L(outline([(8, 64), (2, 70, 1), (6, 54), (2, 40, 1), (10, 32), (22, 12), (50, 2), (78, 12), (90, 32), (98, 40, 1), (94, 54), (98, 70, 1), (92, 84), (96, 100, 1), (80, 88),
              (66, 98, 1), (54, 86), (40, 98, 1), (28, 86), (6, 100, 1), (10, 82)]))])

# Alice Nutty: chica de melena castaña lisa y larga con una cinta azul en la frente; la cara tapada por una máscara de ópera
# china roja con espirales crema y la boca azul
MASK, CREAM, MBLUE = _c('#b8141a'), _c('#ece6d5'), _c('#616e95')
C('alice-nutty', 'chica', P('#564339', '#e8c8a0', iris='#1a1a1a', shade='#402f29', band='#616e95'),
  F(eyes='none', brows=False, mouth='none', hairline=[(8, 66), (14, 52), (30, 46), (50, 46), (70, 46), (86, 52), (92, 66)]),
  dome('front', top=0, w=46, cy=44, seed=31, long=114, flare=4) + headband('front', 42, 7, knot=False) +
  [L(blob([(22, 52), (50, 48), (78, 52), (80, 80), (70, 100), (50, 108), (30, 100), (20, 80)], 8), CREAM, 'f', True),
   L(blob([(24, 56), (50, 54), (76, 56), (76, 80), (66, 96), (56, 98), (56, 88), (44, 88), (44, 98), (34, 96), (24, 80)], 6), MASK, 'f', False),
   L(blob([(42, 54), (50, 50), (58, 54), (54, 60), (46, 60)], 4), CREAM, 'f', False),
   strand([(46, 70), (40, 66), (32, 70), (32, 80), (40, 82), (42, 76), (37, 75)], CREAM, 'f', 1.8),
   strand([(54, 70), (60, 66), (68, 70), (68, 80), (60, 82), (58, 76), (63, 75)], CREAM, 'f', 1.8),
   L(blob([(42, 90), (58, 90), (56, 100), (44, 100)], 4), MBLUE, 'f', True)],
  dome('side', top=0, w=46, cy=44, seed=31, long=114, flare=4, fr=46) + headband('side', 42, 7) +
  [L(blob([(70, 52), (88, 54), (90, 80), (84, 100), (70, 104)], 6), MASK, 'f', True), strand([(80, 68), (86, 72), (84, 80), (78, 78)], CREAM, 'f', 1.8)],
  dome('back', top=0, w=46, cy=44, seed=31, long=114, flare=4, ends=5) + headband('back', 42, 7, knot=False))

# Amy Pink-Peach: casco de superheroína rosa con franjas lila y amarillas y dos alas blancas hacia arriba, pañuelo rosa al
# cuello; le asoma por debajo la melena dorada y se le ve la boca sonriente
HPINK, HLIL, HYEL, WING = _c('#f898bc'), _c('#d6c8dc'), _c('#f6e070'), _c('#f4ecd8')
def _hero(view):
    if view == 'front':
        return [L(outline([(26, 30), (12, 10), (6, -18, 1), (22, 12), (30, 24)]), WING, 'f'), L(outline([(74, 30), (88, 10), (94, -18, 1), (78, 12), (70, 24)]), WING, 'f'),
                L(blob([(12, 70), (10, 40), (24, 14), (50, 6), (76, 14), (90, 40), (88, 70), (74, 82), (62, 78), (50, 80), (38, 78), (26, 82)], 8), HPINK, 'f'),
                L(blob([(30, 24), (50, 16), (70, 24), (64, 44), (50, 36), (36, 44)], 6), HLIL, 'f', False),
                L(blob([(38, 50), (46, 44), (50, 60), (44, 64)], 4), HYEL, 'f', False), L(blob([(62, 50), (54, 44), (50, 60), (56, 64)], 4), HYEL, 'f', False),
                L(blob([(30, 64), (44, 66), (44, 74), (32, 72)], 4), _c('#3a2a44'), 'f', False), L(blob([(70, 64), (56, 66), (56, 74), (68, 72)], 4), _c('#3a2a44'), 'f', False)]
    if view == 'side':
        return [L(outline([(54, 16), (60, -14, 1), (66, 14)]), WING, 'f'),
                L(blob([(8, 70), (4, 40), (20, 12), (50, 4), (76, 12), (90, 40), (90, 72), (78, 80), (60, 74), (40, 80)], 8), HPINK, 'f'),
                L(blob([(54, 20), (80, 26), (88, 46), (76, 50), (60, 36)], 6), HLIL, 'f', False),
                L(blob([(74, 64), (88, 64), (88, 72), (76, 72)], 4), _c('#3a2a44'), 'f', False)]
    return [L(outline([(26, 30), (12, 10), (6, -18, 1), (22, 12), (30, 24)]), WING, 'f'), L(outline([(74, 30), (88, 10), (94, -18, 1), (78, 12), (70, 24)]), WING, 'f'),
            L(blob([(10, 74), (8, 40), (24, 14), (50, 6), (76, 14), (92, 40), (90, 74), (50, 80)], 8), HPINK, 'f'),
            L(blob([(36, 20), (50, 14), (64, 20), (60, 70), (40, 70)], 6), HLIL, 'f', False)]
C('amy-pink-peach', 'chica', P('#b07a10', '#f4caa0', iris='#1a1a1a', shade='#7a4b0d', scarf='#f898bc'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, hairline=False),
  [L(outline([(6, 98), (4, 70), (14, 60), (86, 60), (96, 70), (94, 98), (84, 90), (16, 90)])),
   L(outline([(16, 104), (50, 110), (84, 104), (100, 92, 1), (90, 112), (50, 120), (10, 112), (0, 92, 1)]), 'scarf', 'f')] + _hero('front'),
  [L(outline([(4, 70), (30, 70), (52, 80), (44, 96), (24, 100), (6, 96)])), L(outline([(40, 106), (90, 108), (84, 116), (36, 116), (12, 104, 1)]), 'scarf', 'f')] + _hero('side'),
  [L(outline([(6, 100), (4, 70), (96, 70), (94, 100), (50, 104)])), L(outline([(40, 96), (60, 96), (76, 112, 1), (50, 104), (24, 112, 1)]), 'scarf', 'f')] + _hero('back'))

# Amy Stinger: chica de piel pálida con el pelo rojo frambuesa corto y un tupé que sale hacia delante como una visera
# ladeada; pendientes verdes, ojos entornados verde agua y labios morados
C('amy-stinger', 'chica', P('#a72c48', '#e2ccae', iris='#3a8a80', shade='#7a2331'),
  F(eyes='sharp', brows=True, mouth='lips', mouth_y=95, mouth_w=7, nose=(50, 86, 1.2),
    hairline=[(8, 62), (16, 52), (30, 50), (50, 52), (70, 50), (84, 52), (92, 62)]),
  [L(outline([(16, 64), (12, 40), (22, 18), (44, 6), (70, 8), (86, 18), (106, 22, 1), (88, 34), (88, 56), (82, 64), (80, 50), (20, 50)])),
   L(outline([(58, 10), (86, 20), (104, 24), (88, 34), (86, 54), (76, 40)]), 'shade', 'b', False),
   fr([(18, 54), (24, 36), (40, 26), (60, 24), (80, 30), (84, 52), (66, 44), (44, 46), (30, 50)]),
   L(ell(16, 82, 2.2, 2.2), _c('#6ac040'), 'f', True), L(ell(84, 82, 2.2, 2.2), _c('#6ac040'), 'f', True),
   L(blob([(44, 94), (56, 94), (54, 99), (46, 99)], 4), _c('#4a2a40'), 'f', False)],
  [L(outline([(70, 50), (86, 40), (106, 30, 1), (88, 24), (80, 10), (56, 2), (30, 6), (12, 18), (4, 42), (8, 66), (22, 78), (34, 70), (44, 58), (56, 52)])),
   L(outline([(4, 44), (30, 48), (40, 62), (30, 74), (16, 74), (6, 62)]), 'shade', 'b', False), L(ell(46, 80, 2.2, 2.2), _c('#6ac040'), 'f', True)],
  [L(outline([(16, 78), (10, 44), (22, 18), (44, 6), (70, 8), (88, 22), (92, 44), (86, 78), (50, 84)])),
   L(outline([(60, 12), (82, 22), (90, 46), (86, 76), (66, 82), (66, 40)]), 'shade', 'b', False)])

# Andrew Hooper: pelo azul marino oscuro con un pico que le baja por el centro de la frente hasta entre los ojos y dos
# mechones largos a los lados que acaban en punta hacia fuera; orejas grandes, piel tostada y ojos de enfado
C('andrew-hooper', 'normal', P('#243949', '#cd966a', iris='#1a1a1a', shade='#171c22'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, big_ears=2, ear_out=2,
    hairline=[(8, 62), (16, 46), (30, 46), (44, 58), (50, 70), (56, 58), (70, 46), (84, 46), (92, 62)]),
  [L(outline([(16, 60), (10, 36), (22, 12), (50, 2), (78, 12), (90, 36), (84, 60), (80, 46), (20, 46)])),
   L(outline([(60, 6), (80, 16), (90, 38), (84, 56), (76, 36)]), 'shade', 'b', False),
   fr([(18, 50), (16, 74), (20, 94), (12, 102, 1), (26, 92), (24, 66)]), fr([(82, 50), (84, 74), (80, 94), (88, 102, 1), (74, 92), (76, 66)])],
  [L(outline([(70, 48), (84, 40), (82, 18), (60, 4), (32, 6), (12, 18), (4, 42), (8, 70), (20, 78), (34, 70), (44, 60), (56, 52)])),
   L(outline([(4, 44), (30, 48), (40, 62), (30, 74), (16, 74), (6, 62)]), 'shade', 'b', False),
   fr([(72, 50), (78, 74), (74, 94), (82, 102, 1), (66, 92), (66, 66)])],
  [L(outline([(16, 80), (10, 40), (22, 12), (50, 2), (78, 12), (90, 40), (84, 80), (86, 98, 1), (70, 88), (50, 90), (30, 88), (14, 98, 1)])),
   L(outline([(60, 8), (80, 18), (90, 42), (84, 80), (68, 86), (66, 40)]), 'shade', 'b', False)])

# Andy Fudge: grandullón de cara ancha con papada, orejas grandes de mono, pelo azul petróleo en un tupé plano con
# patillas largas; ojos redondos pequeños con el ceño fruncido y dos colmillos que le salen hacia arriba de la boca
C('andy-fudge', 'corpulento', P('#2a5f6d', '#cd9569', iris='#1a1a1a', shade='#1e4650'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=98, big_ears=3, ear_out=12, nose=(50, 88, 2.6),
    face_front=blob([(12, 50), (50, 40), (88, 50), (96, 80), (90, 104), (68, 116), (50, 118), (32, 116), (10, 104), (4, 80)], 8),
    face_side=face_side(chin=10, jaw=8), hairline=[(10, 64), (16, 50), (30, 46), (50, 48), (70, 46), (84, 50), (90, 64)]),
  [L(outline([(14, 74), (10, 50), (16, 30), (34, 16), (52, 10), (74, 12), (90, 22), (94, 34), (88, 50), (86, 74), (80, 52), (20, 52)])),
   L(outline([(60, 12), (86, 18), (94, 34), (88, 50), (76, 36)]), 'shade', 'b', False),
   L([(36, 100), (39, 92), (42, 100)], WHITE, 'f', True), L([(58, 100), (61, 92), (64, 100)], WHITE, 'f', True),
   L(quad((30, 104), (50, 110), (70, 104)), _c('#a26a49'), 'f', False, False, 1.0)],
  [L(outline([(70, 46), (88, 36), (96, 22), (84, 12), (56, 6), (30, 10), (12, 22), (6, 44), (10, 70), (22, 80), (34, 72), (44, 58), (56, 50)])),
   L(outline([(6, 46), (30, 50), (40, 62), (30, 76), (16, 76), (8, 64)]), 'shade', 'b', False),
   L([(80, 100), (83, 92), (86, 100)], WHITE, 'f', True)],
  [L(outline([(14, 78), (10, 48), (16, 28), (34, 14), (52, 10), (74, 12), (90, 24), (92, 48), (86, 78), (50, 84)])),
   L(outline([(60, 12), (86, 20), (92, 46), (86, 76), (66, 82), (66, 40)]), 'shade', 'b', False)])

# Angus Hogg: gorro de hipopótamo pardo que le tapa toda la cabeza, con las fosas nasales y las orejitas encima; piel
# tostada, ojos entornados y sonrisa
HIPPO, HIPPO_D, NOSTRIL = _c('#8b715d'), _c('#6a5444'), _c('#4a3e30')
def _hippo(view):
    if view == 'front':
        return [L(blob([(8, 70), (6, 40), (18, 14), (50, 4), (82, 14), (94, 40), (92, 70), (80, 60), (20, 60)], 8), HIPPO),
                L(blob([(18, 46), (20, 24), (50, 14), (80, 24), (82, 46), (50, 52)], 8), _c('#a39f8f'), 'b', False),
                L(ell(34, 34, 10, 9), NOSTRIL, 'b', True), L(ell(66, 34, 10, 9), NOSTRIL, 'b', True),
                L(outline([(10, 22), (2, 8, 1), (18, 12)]), HIPPO), L(outline([(90, 22), (98, 8, 1), (82, 12)]), HIPPO),
                L(outline([(8, 62), (92, 62), (92, 70), (8, 70)]), HIPPO_D, 'b', True)]
    if view == 'side':
        return [L(blob([(6, 74), (2, 40), (18, 12), (50, 4), (84, 12), (96, 34), (92, 60), (60, 62), (34, 70)], 8), HIPPO),
                L(blob([(56, 12), (86, 16), (96, 34), (80, 44), (60, 36)], 8), _c('#a39f8f'), 'b', False),
                L(ell(80, 26, 7, 6), NOSTRIL, 'b', True), L(outline([(30, 12), (24, -2, 1), (40, 8)]), HIPPO)]
    return [L(blob([(8, 80), (6, 40), (18, 14), (50, 4), (82, 14), (94, 40), (92, 80), (50, 86)], 8), HIPPO),
            L(blob([(56, 10), (80, 18), (92, 42), (90, 78), (66, 84), (64, 40)], 8), HIPPO_D, 'b', False),
            L(outline([(10, 22), (2, 8, 1), (18, 12)]), HIPPO), L(outline([(90, 22), (98, 8, 1), (82, 12)]), HIPPO)]
C('angus-hogg', 'normal', P('#504332', '#ce9569', iris='#1a1a1a'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, hairline=False, nose=(50, 86, 1.6)),
  _hippo('front') + [L(quad((28, 78), (36, 74), (44, 78)), OUTC, 'f', False, False, 2.2), L(quad((56, 78), (64, 74), (72, 78)), OUTC, 'f', False, False, 2.2),
                     L(ell(36, 78, 2.4, 2), BLACK, 'f', False), L(ell(64, 78, 2.4, 2), BLACK, 'f', False),
                     L(outline([(12, 68), (10, 82), (16, 84), (18, 70)]), _c('#6a3a7a'), 'f', False), L(outline([(88, 68), (90, 82), (84, 84), (82, 70)]), _c('#6a3a7a'), 'f', False)],
  _hippo('side') + [L(quad((76, 78), (81, 74), (86, 78)), OUTC, 'f', False, False, 2.2)],
  _hippo('back'))

# Ann Taisie: chica de piel muy clara con el pelo dorado recogido arriba con un lazo azul claro y tirabuzones gordos en
# espiral que le caen a los lados hasta los hombros; ojos verde azulado con pestañas
BOW = _c('#77ced9')
def _drill(x, y0, y1, s):
    out = []
    n = 4
    for i in range(n):
        y = y0 + (y1 - y0) * i / n
        h = (y1 - y0) / n
        out.append(L(blob([(x - 9, y), (x + 9, y), (x + 8 + s, y + h * 0.6), (x, y + h + 2), (x - 8 + s, y + h * 0.6)], 5)))
        out.append(strand([(x - 7, y + h * 0.4), (x + 6, y + h * 0.7)], 'shade', 'b', 1.0))
    return out
C('ann-taisie', 'chica', P('#f0b020', '#fdeab9', iris='#3a8a98', shade='#c68918'),
  F(eyes='big', brows=True, mouth='frown', mouth_y=94, hairline=[(8, 62), (16, 48), (32, 42), (50, 46), (68, 42), (84, 48), (92, 62)]),
  _drill(10, 60, 112, -2) + _drill(90, 60, 112, 2) +
  [L(outline([(14, 70), (10, 40), (22, 16), (50, 6), (78, 16), (90, 40), (86, 70), (80, 50), (20, 50)])),
   strand([(30, 40), (34, 22), (46, 12)], 'shade', 'b', 1.0), strand([(70, 40), (66, 22), (54, 12)], 'shade', 'b', 1.0),
   L(blob([(50, 8), (62, -4), (72, 0), (66, 12), (50, 12)], 5), BOW, 'f', True), L(blob([(50, 8), (40, -2), (34, 4), (40, 12), (50, 12)], 5), BOW, 'f', True),
   L(ell(50, 9, 4, 3.4), BOW, 'f', True)] + lashes_out(75, 14),
  _drill(36, 60, 112, -2) + [L(outline([(70, 48), (84, 40), (82, 18), (60, 4), (32, 6), (12, 18), (4, 44), (10, 66), (28, 70), (44, 60), (56, 52)])),
                             L(blob([(48, 4), (60, -6), (66, 2), (58, 10)], 5), BOW, 'f', True)],
  _drill(14, 60, 112, -2) + _drill(50, 66, 116, 0) + _drill(86, 60, 112, 2) +
  [L(outline([(12, 76), (8, 40), (22, 16), (50, 6), (78, 16), (92, 40), (88, 76), (50, 80)])),
   L(blob([(50, 8), (62, -4), (72, 0), (66, 12), (50, 12)], 5), BOW, 'f', True), L(blob([(50, 8), (40, -2), (34, 4), (40, 12), (50, 12)], 5), BOW, 'f', True)])

# Anna Bugeisha: chica de pelo verde azulado oscuro en casco con flequillo que le tapa la frente hasta los ojos; una
# máscara de ninja morada le tapa nariz y boca; ojos afilados morados
NINJA = _c('#746477')
C('anna-bugeisha', 'chica', P('#406265', '#d8b498', iris='#6a3a7a', shade='#2c3a3c'),
  F(eyes='sharp', brows=False, mouth='none', eye_y=76, hairline=[(8, 66), (16, 62), (30, 66), (50, 70), (70, 66), (84, 62), (92, 66)]),
  [L(outline([(12, 84), (8, 50), (14, 22), (34, 6), (50, 2), (66, 6), (86, 22), (92, 50), (88, 84), (80, 70), (20, 70)])),
   L(outline([(60, 6), (82, 16), (92, 46), (88, 80), (80, 60)]), 'shade', 'b', False),
   L(blob([(18, 84), (40, 80), (50, 88), (60, 80), (82, 84), (80, 98), (66, 108), (50, 112), (34, 108), (20, 98)], 6), NINJA, 'f', True)],
  [L(outline([(72, 64), (86, 50), (86, 22), (64, 4), (34, 4), (12, 18), (4, 46), (6, 80), (16, 92), (36, 92), (46, 76), (56, 66)])),
   L(outline([(4, 48), (30, 54), (42, 76), (34, 90), (16, 90), (6, 78)]), 'shade', 'b', False),
   L(blob([(60, 84), (82, 80), (90, 88), (86, 100), (70, 106), (58, 98)], 6), NINJA, 'f', True)],
  [L(outline([(10, 88), (8, 50), (14, 22), (34, 6), (50, 2), (66, 6), (86, 22), (92, 50), (90, 88), (50, 94)])),
   L(outline([(60, 8), (84, 18), (92, 48), (90, 86), (68, 92), (66, 40)]), 'shade', 'b', False)])

# Anne Somnia: chica de pelo salmón recogido hacia arriba en un moño de lado, con un mechón que le cruza la frente; cejas de
# preocupación, ojos castaños grandes y boca triste
C('anne-somnia', 'chica', P('#dd996d', '#fdeab7', iris='#8a4a20', shade='#ab6a4b'),
  F(eyes='big', brows=True, mouth='frown', mouth_y=95, hairline=[(8, 62), (16, 50), (34, 40), (56, 36), (76, 42), (86, 50), (92, 62)]),
  [L(outline([(14, 70), (10, 40), (20, 16), (44, 4), (70, 6), (88, 18), (94, 40), (90, 64), (82, 50), (18, 50)])),
   L(blob([(66, 4), (86, 2), (98, 16), (94, 34), (80, 26)], 6)),
   L(outline([(62, 8), (88, 16), (94, 42), (88, 62), (78, 40)]), 'shade', 'b', False),
   strand([(24, 46), (40, 24), (66, 12)], 'shade', 'b', 1.0), strand([(40, 40), (56, 22), (76, 16)], 'shade', 'b', 1.0)] + lashes_out(75, 14),
  [L(outline([(70, 46), (84, 38), (82, 18), (60, 4), (32, 4), (12, 16), (4, 40), (8, 64), (22, 72), (36, 64), (46, 56), (58, 50)])),
   L(blob([(6, 14), (22, 2), (40, 6), (36, 24), (14, 28)], 6)), strand([(76, 36), (54, 16), (30, 10)], 'shade', 'b', 1.0)],
  [L(outline([(14, 76), (10, 40), (20, 16), (44, 4), (70, 6), (88, 18), (92, 40), (88, 76), (50, 82)])),
   L(blob([(56, 10), (84, 6), (96, 22), (88, 42), (64, 36)], 6), 'shade'), strand([(64, 16), (80, 26), (86, 22)], 'deep', 'b', 1.0)])

# Ant Anomy: pelo azul marino peinado hacia arriba en un tupé de pincho grande hacia su izquierda, con un mechón que le cae
# sobre un ojo y puntas sueltas en la nuca; ojos ámbar y boca seria
C('ant-anomy', 'normal', P('#224a70', '#f3c695', iris='#a07a20', shade='#1a2f42'),
  F(eyes='sharp', brows=True, mouth='line', mouth_y=95, hairline=[(8, 62), (16, 50), (30, 48), (44, 52), (58, 46), (72, 48), (86, 52), (92, 62)]),
  [L(outline([(14, 70), (2, 74, 1), (10, 52), (4, 36), (16, 20), (36, 14), (60, -2), (76, -16, 1), (74, 6), (90, 14), (96, 36), (92, 60), (100, 72, 1), (84, 66), (80, 50),
              (20, 50)])),
   L(outline([(60, 6), (76, -14), (74, 6), (90, 16), (94, 40), (88, 60), (78, 40)]), 'shade', 'b', False),
   fr([(30, 46), (40, 34), (54, 30), (64, 40), (56, 50), (54, 74, 1), (48, 56), (40, 50)])],
  [L(outline([(70, 48), (86, 40), (92, 20), (96, 0, 1), (74, 8), (56, -2), (30, 4), (10, 16), (2, 40), (-6, 62, 1), (8, 62), (14, 78), (30, 74), (44, 60), (56, 52)])),
   L(outline([(2, 42), (28, 48), (40, 62), (28, 72), (12, 72)]), 'shade', 'b', False)],
  [L(outline([(14, 80), (2, 84, 1), (10, 60), (8, 36), (18, 18), (40, 8), (60, 0), (72, -12, 1), (74, 8), (90, 18), (94, 40), (90, 70), (100, 82, 1), (80, 80), (50, 84)])),
   L(outline([(60, 6), (72, -10), (74, 8), (90, 20), (92, 46), (88, 76), (66, 80), (66, 40)]), 'shade', 'b', False)])

# Anton Donce: pelo azul con dos pinchos grandes de punta a los lados, como orejas de gato, y mechones finos por la frente;
# ojos blancos redondos de pupila pequeña y sonrisa
C('anton-donce', 'normal', P('#135c7d', '#f8bd7d', iris='#1a1a1a', shade='#103b4e'),
  F(eyes='round', brows=False, mouth='smile', mouth_y=94, nose=(50, 86, 1.4), hairline=hl(6, 60, 46, 54, jit=1, seed=4)),
  [L(outline([(16, 62), (12, 40), (4, 4), (-2, -24, 1), (24, 0), (36, 10), (50, 8), (64, 10), (76, 0), (102, -24, 1), (96, 4), (88, 40), (84, 62), (80, 48), (20, 48)])),
   L(outline([(62, 12), (76, 2), (100, -22), (94, 6), (88, 40), (84, 58), (76, 36)]), 'shade', 'b', False),
   strand([(40, 44), (42, 20)], 'shade', 'b', 1.0), strand([(56, 44), (58, 20)], 'shade', 'b', 1.0)],
  [L(outline([(70, 48), (84, 40), (84, 22), (70, 10), (60, 4), (54, -24, 1), (40, 4), (22, 8), (8, 22), (4, 46), (10, 66), (22, 72), (36, 64), (46, 56), (58, 50)])),
   L(outline([(4, 46), (30, 50), (40, 62), (28, 72), (12, 70)]), 'shade', 'b', False)],
  [L(outline([(16, 76), (12, 40), (4, 4), (-2, -24, 1), (24, 0), (36, 10), (50, 8), (64, 10), (76, 0), (102, -24, 1), (96, 4), (88, 40), (84, 76), (50, 82)])),
   L(outline([(62, 12), (76, 2), (100, -22), (94, 6), (88, 40), (84, 74), (66, 80), (66, 40)]), 'shade', 'b', False)])

# Archy Seago: capucha verde azulado con el borde de borreguillo crema alrededor de la cara; le asoma el pelo castaño en
# dos mechones que le rodean los ojos; ojos azules mirando arriba y boca de piñón rosa
HOOD, FUR = _c('#306c76'), _c('#fdf3dc')
def _hood(view):
    if view == 'front':
        return [L(outline([(4, 100), (2, 50), (14, 14), (50, 0), (86, 14), (98, 50), (96, 100), (84, 104), (16, 104)]), HOOD),
                L(outline([(60, 4), (86, 16), (96, 50), (94, 96), (86, 98), (84, 50)]), _c('#245a62'), 'b', False)]
    if view == 'side':
        return [L(outline([(84, 50), (86, 20), (64, 2), (34, 2), (10, 18), (0, 50), (4, 96), (40, 104), (60, 96), (70, 70)]), HOOD),
                L(outline([(2, 52), (34, 56), (44, 80), (36, 100), (8, 96)]), _c('#245a62'), 'b', False)]
    return [L(outline([(4, 104), (2, 50), (14, 14), (50, 0), (86, 14), (98, 50), (96, 104), (50, 110)]), HOOD),
            L(outline([(60, 4), (86, 16), (96, 50), (94, 100), (66, 106), (66, 40)]), _c('#245a62'), 'b', False)]
def _fur(cx, cy, rx, ry, n=12):
    import math
    pts = []
    for i in range(n * 2):
        a = math.pi * 2 * i / (n * 2)
        k = 1.0 if i % 2 == 0 else 0.88
        pts.append((cx + rx * k * math.cos(a), cy + ry * k * math.sin(a)))
    return blob(pts, 4)
C('archy-seago', 'normal', P('#572807', '#f0bf98', iris='#3a8ac8', shade='#3e1c04'),
  F(eyes='round', brows=False, mouth='none', eye_y=76, hairline=False),
  _hood('front') + [L(_fur(50, 74, 44, 44), FUR, 'f', True), L(blob([(16, 72), (24, 50), (50, 44), (76, 50), (84, 72), (82, 96), (64, 110), (50, 112), (36, 110), (18, 96)], 8), 'skin', 'f', False),
                    L(blob([(18, 74), (24, 56), (42, 52), (48, 64), (36, 70), (30, 84), (22, 92)], 6), 'mid', 'f', False),
                    L(blob([(82, 74), (76, 56), (58, 52), (52, 64), (64, 70), (70, 84), (78, 92)], 6), 'mid', 'f', False),
                    L(ell(36, 76, 6, 6), WHITE, 'f', True), L(ell(64, 76, 6, 6), WHITE, 'f', True),
                    L(ell(37, 73, 2.6, 2.8), _c('#3a8ac8'), 'f', False), L(ell(63, 73, 2.6, 2.8), _c('#3a8ac8'), 'f', False),
                    L(ell(50, 98, 4.4, 3.6), _c('#e88a8a'), 'f', True), L(ell(50, 98, 1.6, 1.4), _c('#7a2a2a'), 'f', False)],
  _hood('side') + [L(_fur(66, 72, 22, 40, 8), FUR, 'f', True), L(blob([(68, 50), (86, 52), (90, 80), (84, 100), (70, 106), (64, 80)], 6), 'skin', 'f', False),
                   L(ell(80, 76, 4, 5.4), WHITE, 'f', True), L(ell(81, 73, 2, 2.4), _c('#3a8ac8'), 'f', False), L(ell(88, 98, 3, 3), _c('#e88a8a'), 'f', True)],
  _hood('back'))

# Ardel Kernel: pelo amarillo oliva en una seta ancha y plana encima (flat top) sobre los lados castaños rapados; ojos
# afilados de pillo, nariz redonda y media sonrisa
C('ardel-kernel', 'normal', P('#a99d1f', '#fcc271', iris='#1a1a1a', shade='#81611d', low='#644516'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=95, nose=(50, 86, 2.6), big_ears=1, hairline=[(10, 62), (18, 48), (50, 46), (82, 48), (90, 62)]),
  [L(outline([(16, 64), (14, 40), (86, 40), (84, 64), (80, 48), (20, 48)]), 'low'),
   L(blob([(8, 30), (6, 10), (20, -6), (50, -10), (80, -6), (94, 10), (92, 30), (76, 40), (50, 42), (24, 40)], 8)),
   L(blob([(60, -6), (84, 0), (92, 22), (80, 36), (68, 24)], 6), 'shade', 'b', False)],
  [L(outline([(70, 46), (80, 40), (80, 30), (12, 30), (8, 54), (16, 72), (32, 72), (44, 56), (56, 50)]), 'low'),
   L(blob([(4, 28), (4, 6), (24, -8), (60, -10), (88, -4), (94, 14), (88, 32), (50, 38), (16, 38)], 8))],
  [L(outline([(16, 78), (12, 34), (88, 34), (84, 78), (50, 84)]), 'low'),
   L(blob([(8, 30), (6, 10), (20, -6), (50, -10), (80, -6), (94, 10), (92, 30), (76, 40), (50, 42), (24, 40)], 8)),
   L(blob([(60, -6), (84, 0), (92, 22), (80, 36), (68, 24)], 6), 'shade', 'b', False)])

# Argento Salvage: escafandra morada redonda que le tapa toda la cabeza, con una mirilla redonda de barrotes rojos, el marco
# de barras marrones con remaches y el cuello acolchado
HELM, HELM_D, BAR, PORT = _c('#674e7a'), _c('#503c5a'), _c('#5a4040'), _c('#c01a1a')
def _scaph(view):
    if view == 'front':
        out = [L(ell(50, 58, 50, 52), HELM, 'f'), L(blob([(58, 10), (86, 26), (98, 58), (88, 90), (70, 104), (80, 60)], 8), HELM_D, 'f', False),
               L(outline([(46, 4), (54, 4), (54, 112), (46, 112)]), BAR, 'f', True), L(outline([(2, 54), (98, 54), (98, 62), (2, 62)]), BAR, 'f', True),
               L(ell(50, 64, 22, 22), BAR, 'f', True), L(ell(50, 64, 17, 17), PORT, 'f', True)]
        for x in (40, 46, 52, 58):
            out.append(L(outline([(x, 50), (x + 3, 50), (x + 3, 78), (x, 78)]), _c('#4a2020'), 'f', False))
        out.append(L(blob([(18, 104), (50, 98), (82, 104), (80, 116), (50, 120), (20, 116)], 6), _c('#4a3a6a'), 'f', True))
        return out
    if view == 'side':
        return [L(ell(50, 58, 48, 52), HELM, 'f'), L(blob([(4, 50), (24, 80), (50, 104), (20, 96)], 6), HELM_D, 'f', False),
                L(outline([(2, 54), (98, 54), (98, 62), (2, 62)]), BAR, 'f', True), L(ell(88, 64, 10, 18), BAR, 'f', True), L(ell(90, 64, 6, 13), PORT, 'f', True),
                L(blob([(24, 104), (60, 100), (84, 106), (80, 116), (30, 118)], 6), _c('#4a3a6a'), 'f', True)]
    return [L(ell(50, 58, 50, 52), HELM, 'f'), L(blob([(58, 10), (86, 26), (98, 58), (88, 90), (70, 104), (80, 60)], 8), HELM_D, 'f', False),
            L(outline([(46, 4), (54, 4), (54, 112), (46, 112)]), BAR, 'f', True), L(outline([(2, 54), (98, 54), (98, 62), (2, 62)]), BAR, 'f', True),
            L(blob([(18, 104), (50, 98), (82, 104), (80, 116), (50, 120), (20, 116)], 6), _c('#4a3a6a'), 'f', True)]
C('argento-salvage', 'normal', P('#674e7a', '#e8c8a0', iris='#1a1a1a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _scaph('front'), _scaph('side'), _scaph('back'))

# Arnan Wheelie: tupé crema peinado hacia arriba y hacia su izquierda, con unas gafas de soldador verdes en la frente; ojos
# blancos en raya, triángulos rojos pintados en las mejillas y sonrisa en V
CREAMH, GOGW = _c('#ecdec4'), _c('#3e4a30')
C('arnan-wheelie', 'normal', P('#ecdec4', '#ce9669', iris='#1a1a1a', shade='#b29483'),
  F(eyes='none', brows=False, mouth='none', hairline=[(8, 62), (18, 54), (50, 52), (82, 54), (92, 62)], big_ears=1),
  [L(outline([(16, 60), (8, 40), (14, 20), (2, 4, 1), (26, 6), (40, -8), (62, -14), (92, -10, 1), (80, 0), (88, 20), (90, 40), (84, 60), (80, 50), (20, 50)])),
   strand([(30, 36), (40, 10), (60, -6)], 'shade', 'b', 1.4), strand([(50, 36), (60, 12), (80, -4)], 'shade', 'b', 1.4),
   L([(10, 46), (90, 46)], GREY, 'f', False, False, 3.0),
   L(ell(34, 44, 9, 8), GOGW, 'f', True), L(ell(66, 44, 9, 8), GOGW, 'f', True), L(ell(34, 44, 3.4, 3), _c('#1a2414'), 'f', False), L(ell(66, 44, 3.4, 3), _c('#1a2414'), 'f', False),
   L(blob([(26, 72), (44, 72), (44, 78), (26, 78)], 3), WHITE, 'f', True), L(blob([(56, 72), (74, 72), (74, 78), (56, 78)], 3), WHITE, 'f', True),
   L([(22, 82), (30, 84), (26, 92)], _c('#d04a2a'), 'f', False), L([(78, 82), (70, 84), (74, 92)], _c('#d04a2a'), 'f', False),
   L([(30, 90), (50, 102), (70, 90)], OUTC, 'f', False, False, 1.8)],
  [L(outline([(70, 50), (84, 42), (88, 22), (100, 2, 1), (76, 4), (50, -8), (26, -4), (10, 10), (4, 40), (10, 64), (22, 72), (36, 64), (46, 56), (58, 52)])),
   L([(10, 42), (84, 42)], GREY, 'f', False, False, 3.0), L(ell(80, 42, 7, 8), GOGW, 'f', True),
   L(blob([(78, 72), (88, 72), (88, 77), (78, 77)], 3), WHITE, 'f', True), L([(76, 82), (84, 84), (80, 92)], _c('#d04a2a'), 'f', False)],
  [L(outline([(16, 76), (8, 40), (14, 20), (2, 4, 1), (26, 6), (40, -8), (62, -14), (92, -10, 1), (80, 0), (88, 20), (92, 40), (84, 76), (50, 80)])),
   L([(8, 46), (92, 46)], GREY, 'f', False, False, 3.0)])

# Arthur Easley: pelo verde azulado abombado con ondas que acaban en rizos hacia fuera a la altura de las orejas; ojos rojos
# de enfado, coloretes naranjas y boca seria
C('arthur-easley', 'normal', P('#4a7671', '#f9bc7c', iris='#a02a3a', shade='#2e4a46'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, nose=(50, 86, 1.4), hairline=[(8, 62), (16, 50), (30, 44), (50, 46), (70, 44), (84, 50), (92, 62)]),
  [L(outline([(12, 80), (0, 90, 1), (4, 64), (-2, 50, 1), (8, 40), (14, 18), (50, 4), (86, 18), (92, 40), (102, 50, 1), (96, 64), (100, 90, 1), (88, 80), (82, 54), (18, 54)])),
   L(outline([(60, 8), (84, 18), (92, 42), (96, 62), (88, 78), (80, 50)]), 'shade', 'b', False),
   strand([(30, 46), (32, 22), (42, 12)], 'shade', 'b', 1.0), strand([(50, 46), (50, 12)], 'shade', 'b', 1.0), strand([(70, 46), (68, 22), (58, 12)], 'shade', 'b', 1.0),
   L(ell(28, 86, 5, 3.4), _c('#f0905a'), 'f', False), L(ell(72, 86, 5, 3.4), _c('#f0905a'), 'f', False)],
  [L(outline([(70, 50), (84, 42), (84, 22), (62, 4), (32, 4), (12, 18), (2, 44), (-6, 64, 1), (6, 70), (4, 90, 1), (22, 82), (36, 70), (46, 58), (58, 52)])),
   L(outline([(2, 46), (30, 52), (40, 66), (28, 80), (10, 80)]), 'shade', 'b', False)],
  [L(outline([(12, 84), (0, 92, 1), (4, 64), (-2, 50, 1), (8, 40), (14, 18), (50, 4), (86, 18), (92, 40), (102, 50, 1), (96, 64), (100, 92, 1), (88, 84), (50, 88)])),
   L(outline([(60, 8), (84, 18), (92, 42), (96, 62), (88, 82), (66, 86), (66, 40)]), 'shade', 'b', False)])

# Arvin Inkwell: chico de piel clara con el pelo castaño claro liso hasta los hombros y mechones que le cruzan la cara; ojos
# morados oscuros y boca pequeña
C('arvin-inkwell', 'normal', P('#d69e68', '#fce9b8', iris='#4a3a5a', shade='#a06f4d'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=94, hairline=[(8, 66), (16, 52), (28, 48), (40, 58), (50, 46), (62, 56), (74, 48), (86, 52), (92, 66)]),
  dome('front', top=0, w=46, cy=44, seed=41, long=100, flare=6) +
  [fr([(32, 42), (40, 34), (46, 40), (42, 60), (38, 74, 1), (36, 56)]), fr([(62, 40), (56, 34), (52, 40), (60, 60), (66, 76, 1), (64, 56)])],
  dome('side', top=0, w=46, cy=44, seed=41, long=100, flare=6, fr=46),
  dome('back', top=0, w=46, cy=44, seed=41, long=100, flare=6, ends=5))

# Audry Orange: chica con un gorro con forma de naranja (con su hoja verde encima) del que le asoma un flequillo castaño;
# ojos de punto, coloretes y sonrisa recta y ancha
ORANGE, ORANGE_D, LEAF = _c('#f79411'), _c('#c86a10'), _c('#4a9a3a')
def _orange(view):
    if view == 'front':
        return [L(blob([(6, 64), (6, 36), (20, 12), (50, 2), (80, 12), (94, 36), (94, 64), (78, 56), (50, 52), (22, 56)], 8), ORANGE),
                L(blob([(62, 6), (84, 16), (94, 40), (92, 60), (80, 50)], 6), ORANGE_D, 'b', False),
                L(outline([(52, 4), (60, -10), (76, -16, 1), (70, -4), (56, 6)]), LEAF)] + \
               [L(ell(x, y, 0.9, 0.9), ORANGE_D, 'b', False) for x, y in ((30, 20), (44, 14), (62, 18), (76, 28), (22, 36), (70, 40))]
    if view == 'side':
        return [L(blob([(4, 66), (2, 36), (18, 10), (50, 2), (80, 10), (94, 34), (90, 58), (60, 56), (30, 64)], 8), ORANGE),
                L(outline([(48, 4), (56, -10), (72, -16, 1), (66, -4), (52, 6)]), LEAF)]
    return [L(blob([(6, 74), (6, 36), (20, 12), (50, 2), (80, 12), (94, 36), (94, 74), (50, 80)], 8), ORANGE),
            L(blob([(62, 6), (84, 16), (94, 40), (92, 70), (70, 76), (72, 40)], 6), ORANGE_D, 'b', False),
            L(outline([(52, 4), (60, -10), (76, -16, 1), (70, -4), (56, 6)]), LEAF)]
C('audry-orange', 'chica', P('#9b551b', '#fdeab8', iris='#1a1a1a'),
  F(eyes='dot', brows=False, mouth='line', mouth_y=94, eye_y=76, hairline=False),
  _orange('front') + [fr([(22, 58), (36, 46), (50, 50), (58, 60), (54, 68, 1), (48, 58), (40, 60), (30, 66, 1)]), L(outline([(10, 62), (14, 80), (20, 66)])),
                      L(outline([(90, 62), (86, 80), (80, 66)])), L(ell(26, 84, 4.4, 3), PINK, 'f', False), L(ell(74, 84, 4.4, 3), PINK, 'f', False),
                      L([(24, 94), (76, 94)], OUTC, 'f', False, False, 1.6)],
  _orange('side'), _orange('back'))

# August Dyers: pelo azul violeta oscuro en pinchos: uno alto en el centro y dos alas abiertas a los lados, con picos que le
# bajan por la frente; orejas de punta, ojos verdes de borde rojo, sonrisa de dientes y cicatrices en las mejillas
C('august-dyers', 'normal', P('#51516b', '#cb966d', iris='#3a8a5a', shade='#36364a'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=96, ear_out=2, hairline=[(8, 60), (18, 50), (30, 58), (40, 46), (50, 60), (60, 46), (70, 58), (82, 50), (92, 60)]),
  [L(outline([(16, 60), (6, 36), (-6, 24, 1), (16, 22), (30, 10), (50, -26, 1), (70, 10), (84, 22), (106, 24, 1), (94, 36), (84, 60), (80, 46), (20, 46)])),
   L(outline([(54, -18), (70, 10), (86, 24), (104, 24), (92, 36), (84, 56), (74, 30)]), 'shade', 'b', False),
   L([(20, 86), (30, 90)], _c('#8a5a3a'), 'f', False, False, 1.0), L([(20, 90), (30, 94)], _c('#8a5a3a'), 'f', False, False, 1.0),
   L([(80, 86), (70, 90)], _c('#8a5a3a'), 'f', False, False, 1.0), L([(80, 90), (70, 94)], _c('#8a5a3a'), 'f', False, False, 1.0)],
  [L(outline([(70, 48), (86, 40), (96, 30), (106, 16, 1), (80, 18), (64, -24, 1), (48, 4), (26, 6), (10, 18), (-6, 30, 1), (6, 40), (8, 64), (22, 72), (36, 64), (46, 56), (58, 50)])),
   L(outline([(6, 42), (30, 50), (40, 62), (28, 72), (12, 70)]), 'shade', 'b', False)],
  [L(outline([(16, 76), (6, 36), (-6, 24, 1), (16, 22), (30, 10), (50, -26, 1), (70, 10), (84, 22), (106, 24, 1), (94, 36), (84, 76), (50, 82)])),
   L(outline([(54, -18), (70, 10), (86, 24), (104, 24), (92, 36), (84, 74), (66, 80), (66, 30)]), 'shade', 'b', False)])

# Aurie Garmer: chica de pelo verde azulado largo con flequillo recto y dos mechones a los lados recogidos con fundas
# amarillas; ojos castaños y sonrisa
TIEY = _c('#dcaa59')
C('aurie-garmer', 'chica', P('#048ea0', '#fbcfa0', iris='#8a4a1a', shade='#055963'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=[(8, 62), (16, 60), (30, 62), (50, 62), (70, 62), (84, 60), (92, 62)]),
  dome('front', top=0, w=48, cy=44, seed=51, long=110, flare=4) +
  [fr([(16, 64), (20, 36), (36, 26), (50, 24), (64, 26), (80, 36), (84, 64), (70, 62), (60, 64), (50, 62), (40, 64), (30, 62)]),
   L(blob([(4, 72), (20, 70), (20, 80), (4, 82)], 3), TIEY, 'f', True), L(blob([(96, 72), (80, 70), (80, 80), (96, 82)], 3), TIEY, 'f', True),
   fr([(6, 80), (18, 80), (16, 96), (8, 96)]), fr([(94, 80), (82, 80), (84, 96), (92, 96)])] + lashes_out(75, 14),
  dome('side', top=0, w=48, cy=44, seed=51, long=110, flare=4, fr=60) + [L(blob([(56, 72), (70, 70), (70, 80), (56, 82)], 3), TIEY, 'f', True)],
  dome('back', top=0, w=48, cy=44, seed=51, long=110, flare=4, ends=5))

# Aya Strand (portera): chica de pelo castaño rojizo oscuro peinado hacia atrás con un moño arriba, dos horquillas rosas a
# los lados y dos mechones finos y largos que le caen junto a la cara; ojos negros grandes, pecas y sonrisa
CLIP = _c('#f0a8b0')
C('aya-strand', 'chica', P('#751f04', '#f9bc7d', iris='#1a1a1a', shade='#551b09'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=94, hairline=[(8, 62), (18, 48), (36, 42), (50, 44), (64, 42), (82, 48), (92, 62)]),
  [L(ell(50, -4, 9, 8)), L(outline([(16, 62), (12, 40), (22, 16), (50, 6), (78, 16), (88, 40), (84, 62), (80, 48), (20, 48)])),
   strand([(50, 44), (50, 10)], 'shade', 'b', 1.0), strand([(30, 46), (40, 14)], 'shade', 'b', 1.0), strand([(70, 46), (60, 14)], 'shade', 'b', 1.0),
   fr([(18, 56), (16, 90), (12, 116, 1), (20, 92), (22, 60)]), fr([(82, 56), (84, 90), (88, 116, 1), (80, 92), (78, 60)]),
   L(outline([(20, 52), (24, 46), (26, 58)]), CLIP, 'f'), L(outline([(80, 52), (76, 46), (74, 58)]), CLIP, 'f')] + freckles(86, 22) + lashes_out(75, 14),
  [L(ell(46, -4, 9, 8)), L(outline([(70, 48), (84, 40), (82, 20), (62, 6), (34, 6), (14, 18), (6, 42), (10, 66), (24, 74), (36, 66), (46, 56), (58, 50)])),
   fr([(72, 52), (74, 90), (72, 116, 1), (66, 90), (66, 58)])],
  [L(ell(50, -4, 9, 8)), L(outline([(16, 76), (12, 40), (22, 16), (50, 6), (78, 16), (88, 40), (84, 76), (50, 82)])),
   strand([(50, 8), (50, 76)], 'shade', 'b', 1.0)])

# Bailey Sitter: chica morena con el pelo blanco grisáceo echado hacia un lado que le tapa la coronilla y las puntas rosadas
# en una melena corta; ojos negros de enfado, boca abierta y pecas
C('bailey-sitter', 'chica', P('#d6e3e5', '#ad8b76', iris='#1a1a1a', shade='#a8b4b8', low='#b8a0a8'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=[(8, 62), (16, 50), (30, 46), (50, 48), (70, 44), (84, 48), (92, 62)]),
  [L(outline([(12, 94), (6, 64), (94, 64), (88, 94), (82, 74), (18, 74)]), 'low'),
   L(outline([(14, 70), (10, 40), (22, 14), (50, 4), (80, 10), (94, 34), (92, 64), (84, 52), (18, 52)])),
   L(outline([(60, 6), (84, 14), (94, 36), (92, 60), (82, 44)]), 'shade', 'b', False),
   strand([(22, 50), (40, 22), (70, 10)], 'shade', 'b', 1.2), strand([(40, 50), (60, 26), (84, 18)], 'shade', 'b', 1.2),
   L(blob([(42, 94), (58, 94), (56, 100), (44, 100)], 4), _c('#3a2020'), 'f', False), L([(44, 95), (56, 95)], WHITE, 'f', False, False, 1.4)] + freckles(86, 22),
  [L(outline([(6, 96), (4, 66), (40, 66), (46, 86), (34, 98)]), 'low'),
   L(outline([(70, 48), (84, 40), (84, 20), (62, 4), (32, 4), (12, 18), (4, 44), (6, 70), (22, 76), (36, 66), (46, 56), (58, 50)]))],
  [L(outline([(10, 96), (6, 64), (94, 64), (90, 96), (50, 100)]), 'low'),
   L(outline([(12, 76), (8, 40), (22, 14), (50, 4), (80, 10), (94, 34), (92, 76), (50, 80)])),
   L(outline([(60, 6), (84, 14), (94, 36), (92, 72), (68, 78), (66, 40)]), 'shade', 'b', False)])

# Barbara Clector: chica de pelo gris verdoso peinado hacia atrás que se levanta en dos lazadas altas sobre la cabeza, con
# mechones largos que le caen a los lados hasta los hombros; ojos entornados y sonrisa
C('barbara-clector', 'chica', P('#96aba3', '#f9b87c', iris='#6a7a5a', shade='#6e807a'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=94, hairline=[(8, 62), (18, 46), (34, 38), (50, 36), (66, 38), (82, 46), (92, 62)]),
  [L(outline([(26, 20), (20, -14), (24, -30, 1), (38, -14), (40, 12)])), L(outline([(74, 20), (80, -14), (76, -30, 1), (62, -14), (60, 12)])),
   L(outline([(16, 62), (10, 38), (20, 16), (50, 8), (80, 16), (90, 38), (84, 62), (80, 44), (20, 44)])),
   strand([(32, 38), (30, 14), (26, -14)], 'shade', 'b', 1.0), strand([(42, 36), (42, 12)], 'shade', 'b', 1.0), strand([(58, 36), (58, 12)], 'shade', 'b', 1.0),
   strand([(68, 38), (70, 14), (74, -14)], 'shade', 'b', 1.0),
   fr([(14, 54), (8, 86), (10, 112, 1), (18, 88), (20, 60)]), fr([(86, 54), (92, 86), (90, 112, 1), (82, 88), (80, 60)])] + lashes_out(75, 14),
  [L(outline([(52, 14), (58, -18), (54, -32, 1), (40, -14), (40, 12)])),
   L(outline([(70, 44), (84, 38), (80, 18), (60, 6), (32, 6), (12, 18), (4, 44), (8, 72), (12, 104, 1), (24, 80), (36, 66), (46, 56), (58, 48)]))],
  [L(outline([(26, 20), (20, -14), (24, -30, 1), (38, -14), (40, 12)])), L(outline([(74, 20), (80, -14), (76, -30, 1), (62, -14), (60, 12)])),
   L(outline([(14, 78), (10, 38), (20, 16), (50, 8), (80, 16), (90, 38), (86, 78), (90, 110, 1), (70, 86), (50, 84), (30, 86), (10, 110, 1)])),
   strand([(50, 10), (50, 80)], 'shade', 'b', 1.0)])

# Bash Beaton: máscara tribal de madera marrón que le tapa la cara (ojos de anillos, sonrisa enorme de dientes cuadrados y
# una ceja en arco), con las orejas de mono y una cresta de pinchos verde menta encima
MINT = _c('#90b6a9')
C('bash-beaton', 'normal', P('#90b6a9', '#b6733a', iris='#1a1a1a', shade='#6e9488'),
  F(eyes='none', brows=False, mouth='none', hairline=False, big_ears=2, ear_out=2,
    face_front=blob([(18, 46), (50, 30), (82, 46), (86, 76), (78, 100), (62, 112), (50, 114), (38, 112), (22, 100), (14, 76)], 8)),
  [L(outline([(30, 34), (32, 14), (40, 22), (44, 4, 1), (52, 18), (58, 2, 1), (62, 18), (70, 10, 1), (70, 34)])),
   L(ell(34, 70, 8, 7.4), _c('#e0f0ea'), 'f', True), L(ell(34, 70, 4.4, 4), _c('#90b6a9'), 'f', True), L(ell(34, 70, 1.6, 1.6), BLACK, 'f', False),
   L(ell(66, 70, 8, 7.4), _c('#e0f0ea'), 'f', True), L(ell(66, 70, 4.4, 4), _c('#90b6a9'), 'f', True), L(ell(66, 70, 1.6, 1.6), BLACK, 'f', False),
   L(quad((40, 52), (50, 44), (60, 52)), OUTC, 'f', False, False, 1.6),
   L(ell(46, 84, 1.6, 1.2), OUTC, 'f', False), L(ell(54, 84, 1.6, 1.2), OUTC, 'f', False),
   L(blob([(22, 90), (50, 92), (78, 90), (72, 104), (50, 108), (28, 104)], 6), WHITE, 'f', True),
   L([(28, 96), (36, 96), (36, 100), (44, 100), (44, 96), (56, 96), (56, 100), (64, 100), (64, 96), (72, 96)], OUTC, 'f', False, False, 1.0)],
  [L(outline([(30, 30), (36, 6, 1), (44, 18), (54, 2, 1), (60, 16), (72, 8, 1), (74, 30)])),
   L(ell(80, 70, 5, 7), _c('#e0f0ea'), 'f', True), L(ell(82, 70, 2.4, 3.4), _c('#90b6a9'), 'f', True),
   L(blob([(66, 90), (90, 90), (86, 104), (70, 106)], 6), WHITE, 'f', True)],
  [L(outline([(30, 34), (32, 14), (40, 22), (44, 4, 1), (52, 18), (58, 2, 1), (62, 18), (70, 10, 1), (70, 34)]))])

# Beat Scatton: pelo azul claro de pinchos revueltos echados hacia su izquierda, con un mechón largo que le cae por el
# centro de la cara; ojos redondos y boca pequeña
C('beat-scatton', 'normal', P('#699caf', '#f7bc7e', iris='#1a1a1a', shade='#556670'),
  F(eyes='round', brows=True, mouth='frown', mouth_y=95, nose=(50, 86, 1.2), hairline=hl(5, 62, 48, 58, lean=-2, jit=2, seed=7)),
  dome('front', top=-2, w=46, cy=44, n=7, amp=12, sweep=0.5, seed=13, sb=66) + [fr([(36, 40), (46, 34), (52, 40), (48, 62), (44, 82, 1), (42, 60)])],
  dome('side', top=-2, w=46, cy=44, n=7, amp=12, sweep=0.5, seed=13, nape=86, fr=50),
  dome('back', top=-2, w=46, cy=44, n=7, amp=12, sweep=0.5, seed=13, nape=86))

# Beata Pummel: chica morena con melena rubia corta de puntas rizadas hacia fuera y una gorra marrón con manchas de vaca
# crema; ojos lila con pestañas y sonrisa abierta
CAPB, SPOT = _c('#604132'), _c('#efd3a3')
def _cowcap(view):
    if view == 'front':
        return [L(blob([(14, 44), (16, 18), (34, 2), (50, -2), (66, 2), (84, 18), (86, 44), (50, 40)], 8), CAPB, 'f'),
                L(outline([(8, 44), (50, 38), (92, 44), (94, 52), (50, 48), (6, 52)]), CAPB, 'f')] + \
               [L(blob([(x - 5, y - 3), (x + 4, y - 4), (x + 5, y + 3), (x - 3, y + 4)], 4), SPOT, 'f', False) for x, y in ((32, 14), (50, 8), (68, 16), (40, 28), (62, 30))]
    if view == 'side':
        return [L(blob([(12, 40), (16, 14), (40, 0), (66, 2), (84, 18), (88, 40), (50, 40)], 8), CAPB, 'f'),
                L(outline([(70, 40), (100, 44), (98, 50), (70, 48)]), CAPB, 'f')] + \
               [L(blob([(x - 5, y - 3), (x + 4, y - 4), (x + 5, y + 3), (x - 3, y + 4)], 4), SPOT, 'f', False) for x, y in ((40, 12), (60, 14), (30, 28))]
    return [L(blob([(12, 46), (16, 18), (34, 2), (50, -2), (66, 2), (84, 18), (88, 46), (50, 50)], 8), CAPB, 'f')] + \
           [L(blob([(x - 5, y - 3), (x + 4, y - 4), (x + 5, y + 3), (x - 3, y + 4)], 4), SPOT, 'f', False) for x, y in ((32, 16), (52, 10), (66, 26), (40, 34))]
C('beata-pummel', 'chica', P('#efd3a3', '#c7966d', iris='#8a6aa8', shade='#c8a878'),
  F(eyes='big', brows=True, mouth='grin', mouth_y=95, hairline=[(8, 62), (16, 50), (50, 48), (84, 50), (92, 62)]),
  [L(outline([(10, 94), (2, 70), (6, 44), (94, 44), (98, 70), (90, 94), (78, 98), (80, 60), (20, 60), (22, 98)])),
   L(ell(10, 94, 9, 7)), L(ell(90, 94, 9, 7)), L(ell(24, 100, 7, 5)), L(ell(76, 100, 7, 5))] + _cowcap('front') + lashes_out(75, 14),
  [L(outline([(70, 50), (80, 44), (10, 40), (2, 70), (8, 96), (30, 100), (44, 80), (56, 56)])), L(ell(12, 96, 9, 7)), L(ell(32, 100, 7, 5))] + _cowcap('side'),
  [L(outline([(8, 96), (2, 70), (6, 44), (94, 44), (98, 70), (92, 96), (50, 102)])), L(ell(10, 96, 9, 7)), L(ell(90, 96, 9, 7)), L(ell(30, 102, 8, 6)), L(ell(70, 102, 8, 6))] + _cowcap('back'))

# Beau Hammock: pañuelo verde de pirata atado a la cabeza con una calavera en la frente, del que asoma un poco de pelo
# castaño; ojos redondos grandes, orejas grandes y sonrisa
BANDANA, BAN_D = _c('#a2aa3c'), _c('#7e712d')
def _bandana(view):
    if view == 'front':
        return [L(blob([(10, 60), (10, 32), (24, 12), (50, 4), (76, 12), (90, 32), (90, 60), (50, 52)], 8), BANDANA),
                L(blob([(60, 8), (82, 18), (90, 40), (88, 58), (76, 44)], 6), BAN_D, 'b', False),
                L(ell(50, 22, 6, 5), _c('#efe6c8'), 'b', True), L(ell(48, 21, 1.2, 1.2), OUTC, 'b', False), L(ell(52, 21, 1.2, 1.2), OUTC, 'b', False),
                L(outline([(32, 54), (40, 50), (48, 56), (56, 50), (62, 56), (56, 60), (40, 60)]), _c('#583f13'), 'b')]
    if view == 'side':
        return [L(blob([(6, 62), (4, 34), (20, 10), (50, 4), (78, 12), (90, 34), (86, 54), (40, 56)], 8), BANDANA),
                L(outline([(8, 50), (-6, 62, 1), (2, 66), (-2, 78, 1), (14, 64)]), BANDANA)]
    return [L(blob([(10, 70), (10, 32), (24, 12), (50, 4), (76, 12), (90, 32), (90, 70), (50, 66)], 8), BANDANA),
            L(outline([(44, 64), (36, 80, 1), (50, 72), (64, 80, 1), (56, 64)]), BANDANA), L(ell(50, 66, 5, 4), BAN_D)]
C('beau-hammock', 'normal', P('#583f13', '#fac172', iris='#1a1a1a'),
  F(eyes='round', brows=False, mouth='smile', mouth_y=94, big_ears=2, ear_out=2, nose=(50, 86, 1.8), hairline=[(10, 62), (18, 56), (50, 58), (82, 56), (90, 62)]),
  _bandana('front'), _bandana('side'), _bandana('back'))

# Becca Pilgreen: chica con un sombrero cónico de paja con el ala roja, un lazo rojo encima y cinta roja atada bajo la
# barbilla; le cae el pelo azul marino oscuro por los lados; ojos grandes negros
STRAW, RED = _c('#ebcb88'), _c('#dc2a28')
def _conehat(view):
    if view == 'front':
        return [L(outline([(-4, 42), (50, 4), (104, 42), (98, 50), (50, 44), (2, 50)]), STRAW, 'f'),
                L(outline([(-4, 42), (50, 36), (104, 42), (100, 52), (50, 46), (0, 52)]), RED, 'f', False),
                L(blob([(38, 8), (44, -4), (50, 2), (56, -4), (62, 8), (50, 12)], 6), RED, 'f'),
                L([(16, 48), (30, 100), (46, 108)], RED, 'f', False, False, 1.8), L([(84, 48), (70, 100), (54, 108)], RED, 'f', False, False, 1.8),
                L(outline([(46, 106), (54, 106), (58, 120, 1), (50, 112), (42, 120, 1)]), RED, 'f')]
    if view == 'side':
        return [L(outline([(-6, 46), (48, 4), (102, 40), (96, 50), (50, 48), (0, 54)]), STRAW, 'f'),
                L(outline([(-6, 46), (50, 40), (102, 40), (98, 50), (50, 50), (-2, 56)]), RED, 'f', False),
                L(blob([(40, 6), (48, -6), (58, 6), (48, 12)], 6), RED, 'f'), L([(54, 50), (66, 102), (80, 108)], RED, 'f', False, False, 1.8)]
    return [L(outline([(-4, 46), (50, 6), (104, 46), (98, 54), (50, 50), (2, 54)]), STRAW, 'f'),
            L(outline([(-4, 46), (50, 42), (104, 46), (100, 56), (50, 52), (0, 56)]), RED, 'f', False),
            L(blob([(38, 10), (44, -2), (50, 4), (56, -2), (62, 10), (50, 14)], 6), RED, 'f')]
C('becca-pilgreen', 'chica', P('#3c2b32', '#fceec9', iris='#1a1a1a', shade='#2a1e24'),
  F(eyes='big', brows='angry', mouth='smile', mouth_y=93, hairline=[(8, 60), (18, 54), (50, 56), (82, 54), (92, 60)]),
  [L(outline([(12, 96), (6, 60), (94, 60), (88, 96), (80, 80), (20, 80)])), fr([(20, 54), (40, 52), (50, 60), (60, 52), (80, 54), (80, 60), (20, 60)])] + _conehat('front') + lashes_out(75, 14),
  [L(outline([(70, 52), (6, 52), (4, 90), (24, 96), (40, 80), (56, 60)]))] + _conehat('side'),
  [L(outline([(10, 96), (6, 52), (94, 52), (90, 96), (50, 100)]))] + _conehat('back'))

# Beck Hand: pelo verde azulado oscuro de pinchos revueltos arriba que se ondula hacia fuera a los lados y en la nuca;
# ojos afilados y sonrisa de dientes
C('beck-hand', 'normal', P('#4a6b75', '#efca9d', iris='#1a1a1a', shade='#3b4247'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=95, hairline=hl(6, 62, 48, 58, jit=3, seed=19)),
  dome('front', top=-4, w=48, cy=44, n=8, amp=12, seed=23, long=92, flare=10) + [fr([(40, 40), (50, 32), (56, 44), (52, 64, 1), (46, 48)])],
  dome('side', top=-4, w=48, cy=44, n=8, amp=12, seed=23, long=92, flare=10, fr=50),
  dome('back', top=-4, w=48, cy=44, n=8, amp=12, seed=23, long=92, flare=10, ends=5))

# Becky Shuffle: chica de pelo rubio largo con raya al lado que le tapa un ojo y cae hasta los hombros con las puntas
# abiertas hacia fuera; ojo azul y sonrisa
C('becky-shuffle', 'chica', P('#d6b93a', '#efc39d', iris='#4a5a8a', shade='#a3752e'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=94, hairline=[(8, 62), (16, 50), (30, 44), (44, 42), (60, 46), (76, 56), (92, 66)]),
  dome('front', top=0, w=48, cy=44, seed=29, long=112, flare=12) +
  [fr([(36, 40), (50, 30), (70, 34), (86, 46), (90, 70), (84, 96), (76, 82), (74, 64), (62, 54), (48, 48)])] + lashes_out(75, 14),
  dome('side', top=0, w=48, cy=44, seed=29, long=112, flare=12, fr=56),
  dome('back', top=0, w=48, cy=44, seed=29, long=112, flare=12, ends=4))

# Bella Shaded (portera): chica de pelo magenta largo y liso que le cae hasta el pecho, con unas gafas de sol redondas
# blancas de cristal oscuro; boca seria
SUNW, SUND = _c('#f4f2f0'), _c('#2a2422')
C('bella-shaded', 'chica', P('#972b48', '#f1d5b4', iris='#1a1a1a', shade='#732133'),
  F(eyes='none', brows=False, mouth='line', mouth_y=95, hairline=[(8, 64), (16, 50), (32, 42), (50, 40), (68, 42), (84, 50), (92, 64)]),
  dome('front', top=-2, w=48, cy=44, seed=33, long=122, flare=8) +
  [L(ell(34, 74, 12, 10), SUNW, 'f', True), L(ell(66, 74, 12, 10), SUNW, 'f', True), L(ell(34, 74, 8, 7), SUND, 'f', False), L(ell(66, 74, 8, 7), SUND, 'f', False),
   L([(46, 72), (54, 72)], SUNW, 'f', False, False, 3.0)],
  dome('side', top=-2, w=48, cy=44, seed=33, long=122, flare=8, fr=46) + [L(ell(82, 74, 7, 10), SUNW, 'f', True), L(ell(84, 74, 4, 7), SUND, 'f', False)],
  dome('back', top=-2, w=48, cy=44, seed=33, long=122, flare=8, ends=6))

# Belle Allure: chica de pelo malva recogido en una bola grande y abombada encima de la cabeza, con dos mechones gruesos
# que le cuelgan por delante a los lados de la cara; ojos negros afilados
C('belle-allure', 'chica', P('#95535c', '#f0c390', iris='#1a1a1a', shade='#7b4547'),
  F(eyes='sharp', brows=True, mouth='frown', mouth_y=95, hairline=[(8, 60), (16, 52), (30, 50), (44, 56), (56, 48), (70, 50), (84, 52), (92, 60)]),
  [L(blob([(10, 50), (6, 20), (20, -4), (50, -14), (80, -4), (94, 20), (90, 50), (70, 56), (50, 52), (30, 56)], 8)),
   L(blob([(56, -10), (82, -2), (94, 22), (88, 48), (72, 30)], 6), 'shade', 'b', False),
   fr([(14, 52), (12, 84), (16, 104), (24, 104), (26, 80), (24, 56)]), fr([(86, 52), (88, 84), (84, 104), (76, 104), (74, 80), (76, 56)]),
   fr([(24, 50), (40, 40), (56, 44), (52, 54), (40, 52)])],
  [L(blob([(4, 50), (2, 18), (24, -6), (54, -14), (82, -4), (92, 20), (86, 48), (60, 54), (30, 60)], 8)),
   fr([(70, 50), (74, 84), (70, 104), (62, 104), (62, 80), (62, 56)])],
  [L(blob([(10, 60), (6, 20), (20, -4), (50, -14), (80, -4), (94, 20), (90, 60), (70, 74), (50, 76), (30, 74)], 8)),
   L(blob([(56, -10), (82, -2), (94, 22), (90, 58), (70, 70), (66, 30)], 6), 'shade', 'b', False)])

# Ben Danna: grandullón de cara naranja con morro gris, nariz larga y orejas de mono; pelo verde oscuro que sube en una
# punta alta y curvada, con una cinta crema cosida en la frente y patillas largas; ojos de enfado y ceño fruncido
MUZZLE, ROPE = _c('#ad8c73'), _c('#efe6d0')
C('ben-danna', 'corpulento', P('#2d443b', '#e48405', iris='#1a1a1a', shade='#1d201c'),
  F(eyes='sharp', brows='angry', mouth='none', hairline=False, big_ears=2, ear_out=4, eye_y=72,
    face_front=blob([(16, 44), (50, 36), (84, 44), (90, 74), (86, 100), (66, 114), (50, 116), (34, 114), (14, 100), (10, 74)], 8), face_side=face_side(chin=10, jaw=8, nose=4)),
  [L(outline([(16, 44), (24, 22), (40, 12), (36, -6), (24, -18, 1), (52, -10), (66, 4), (80, 22), (84, 44)])),
   L(outline([(12, 44), (8, 80), (16, 88), (18, 50)])), L(outline([(88, 44), (92, 80), (84, 88), (82, 50)])),
   L(outline([(14, 38), (50, 30), (86, 38), (86, 46), (50, 40), (14, 46)]), ROPE, 'f'),
   L([(24, 38), (28, 42), (36, 36), (40, 40), (48, 34), (52, 38), (60, 34), (64, 40), (72, 36), (76, 42)], OUTC, 'f', False, False, 0.8),
   L(blob([(24, 86), (50, 82), (76, 86), (78, 102), (66, 114), (50, 116), (34, 114), (22, 102)], 8), MUZZLE, 'f', False),
   L(blob([(42, 62), (58, 62), (62, 84), (50, 90), (38, 84)], 6), _c('#c86e04'), 'f', True),
   L(quad((38, 104), (50, 96), (62, 104)), OUTC, 'f', False, False, 1.8)],
  [L(outline([(66, 40), (82, 28), (72, 14), (60, 2), (50, -14), (32, -20, 1), (36, -2), (20, 10), (8, 30), (6, 60), (18, 76), (34, 66), (44, 52), (56, 44)])),
   L(outline([(10, 34), (86, 34), (86, 42), (10, 42)]), ROPE, 'f'),
   L(blob([(66, 84), (90, 84), (88, 104), (72, 112)], 6), MUZZLE, 'f', False), L(blob([(80, 62), (94, 70), (92, 84), (82, 84)], 6), _c('#c86e04'), 'f', True)],
  [L(outline([(12, 76), (10, 40), (24, 22), (40, 12), (36, -6), (24, -18, 1), (52, -10), (66, 4), (80, 22), (90, 40), (88, 76), (50, 80)])),
   L(outline([(10, 38), (50, 34), (90, 38), (90, 46), (50, 42), (10, 46)]), ROPE, 'f')])

# Ben Whistler: pelo verde oliva oscuro de mechones blandos que caen hacia los lados, con un brote de pelo tieso encima;
# piel muy clara, ojos redondos grandes y boca triste
C('ben-whistler', 'normal', P('#585426', '#f5eac5', iris='#1a1a1a', shade='#453d21'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=95, nose=(50, 86, 1.2), hairline=hl(5, 64, 50, 60, jit=2, seed=37)),
  dome('front', top=0, w=50, cy=44, n=7, amp=8, soft=True, seed=41, sb=68) + [L(outline([(46, 4), (44, -16, 1), (52, -4), (60, -18, 1), (56, 6)]))],
  dome('side', top=0, w=50, cy=44, n=7, amp=8, soft=True, seed=41, nape=84, fr=52) + [L(outline([(46, 4), (44, -16, 1), (54, 4)]))],
  dome('back', top=0, w=50, cy=44, n=7, amp=8, soft=True, seed=41, nape=84) + [L(outline([(46, 4), (44, -16, 1), (52, -4), (60, -18, 1), (56, 6)]))])

# Benny Terra: gorro de lana beige del que le asoma un flequillo verde en mechones; coloretes naranjas, ojos redondos de
# enfado con cejas gruesas negras y ceño fruncido
BEANIE = _c('#e4dabf')
def _beanie(view):
    if view == 'front':
        return [L(blob([(8, 56), (10, 26), (26, 6), (50, 0), (74, 6), (90, 26), (92, 56), (50, 50)], 8), BEANIE, 'f'),
                L(outline([(8, 48), (50, 42), (92, 48), (92, 58), (50, 52), (8, 58)]), _c('#cfc4a4'), 'f', False)]
    if view == 'side':
        return [L(blob([(4, 60), (4, 26), (24, 4), (52, 0), (78, 8), (90, 30), (88, 52), (40, 56)], 8), BEANIE, 'f')]
    return [L(blob([(8, 66), (10, 26), (26, 6), (50, 0), (74, 6), (90, 26), (92, 66), (50, 62)], 8), BEANIE, 'f')]
C('benny-terra', 'normal', P('#6e8a4a', '#fbc06f', iris='#1a1a1a', shade='#4e6a34'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=95, nose=(50, 86, 1.4), hairline=False),
  [L(outline([(10, 56), (8, 92), (18, 100), (22, 60)])), L(outline([(90, 56), (92, 92), (82, 100), (78, 60)]))] + _beanie('front') +
  [fr([(26, 54), (40, 52), (48, 58), (56, 54), (62, 62), (54, 66), (44, 62), (34, 66)])] + thick_brows(66, BLACK, 4.2, 15, 1.6, 15) +
  [L(ell(26, 86, 5, 4.4), _c('#f0904a'), 'f', False), L(ell(74, 86, 5, 4.4), _c('#f0904a'), 'f', False)],
  _beanie('side') + [L(outline([(50, 56), (46, 84), (56, 88), (60, 60)]))] + side_brow(66, BLACK, 4.2, 1.6),
  _beanie('back') + [L(outline([(12, 64), (20, 80), (50, 82), (80, 80), (88, 64)]))])

# Bern MacMahon: pelo verde oscuro de pinchos revueltos que se abren en todas direcciones; piel tostada, ojos de enfado y
# ceño serio
C('bern-macmahon', 'normal', P('#56745b', '#dda358', iris='#1a1a1a', shade='#485240'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=hl(6, 62, 48, 58, jit=3, seed=43)),
  messy('front', amp=12, n=12, seed=71, lo=66), messy('side', amp=12, n=12, seed=71, lo=66), messy('back', amp=12, n=12, seed=71, lo=66))

# Bert Emmerson: pelo naranja abultado en ondas grandes que le cae por los lados, gafas rectangulares negras, ojos azules,
# pecas y sonrisa
C('bert-emmerson', 'normal', P('#e19909', '#fceec8', iris='#3a6ac8', shade='#ad620c'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=95, hairline=[(8, 64), (16, 50), (30, 46), (44, 56), (54, 44), (70, 46), (84, 50), (92, 64)]),
  dome('front', top=-6, w=52, cy=44, n=8, amp=8, soft=True, seed=47, long=96, flare=8) + rect_specs('front', BLACK, 76, 14) + freckles(86, 22),
  dome('side', top=-6, w=52, cy=44, n=8, amp=8, soft=True, seed=47, long=96, flare=8, fr=50) + rect_specs('side', BLACK, 76),
  dome('back', top=-6, w=52, cy=44, n=8, amp=8, soft=True, seed=47, long=96, flare=8, ends=5))

# Bert McClure: calvo de piel marrón y cara larga, con unos aros naranjas alrededor de los ojos, nariz naranja enorme,
# boca abierta en O y orejas grandes
ORG = _c('#f6af73')
C('bert-mcclure', 'delgado', P('#8c4d2a', '#b57337', iris='#1a1a1a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, big_ears=2, ear_out=2, face_front=face(chin=112, w=-2), face_side=face_side(chin=10)),
  [L(blob([(18, 56), (16, 30), (28, 10), (50, 4), (72, 10), (84, 30), (82, 56)], 8), 'skin'),
   L(ell(36, 64, 9, 8), ORG, 'f', True), L(ell(64, 64, 9, 8), ORG, 'f', True), L(ell(36, 64, 4.4, 4.2), BLACK, 'f', False), L(ell(64, 64, 4.4, 4.2), BLACK, 'f', False),
   L([(44, 62), (56, 62)], ORG, 'f', False, False, 2.4),
   L(blob([(44, 70), (56, 70), (60, 90), (50, 94), (40, 90)], 6), ORG, 'f', True),
   L(ell(50, 104, 6, 6), ORG, 'f', True), L(ell(50, 104, 3, 3.4), _c('#5a2010'), 'f', False)],
  [L(ell(82, 64, 6, 8), ORG, 'f', True), L(ell(83, 64, 2.6, 4), BLACK, 'f', False), L(blob([(84, 72), (96, 82), (92, 92), (84, 90)], 6), ORG, 'f', True),
   L(ell(88, 104, 4, 5), ORG, 'f', True)],
  [L(blob([(18, 60), (16, 30), (28, 10), (50, 4), (72, 10), (84, 30), (82, 60), (78, 86), (50, 96), (22, 86)], 8), 'skin')])

# Bertram Manning: pelo azul grisáceo abultado con un mechón que le baja por el centro de la frente y una cola gruesa
# recogida que le abulta por detrás a un lado; ojos verde azulado y boca seria
C('bertram-manning', 'normal', P('#537784', '#f8bc7d', iris='#2a6a70', shade='#434d54'),
  F(eyes='sharp', brows=True, mouth='frown', mouth_y=95, nose=(50, 86, 1.2), hairline=[(8, 64), (16, 52), (32, 48), (44, 54), (50, 66), (56, 54), (68, 48), (84, 52), (92, 64)]),
  [L(blob([(2, 70), (-4, 90), (6, 104), (18, 96), (16, 72)], 6)),
   L(outline([(14, 74), (8, 44), (18, 18), (40, 4), (64, 4), (84, 16), (94, 40), (90, 70), (82, 52), (18, 52)])),
   L(outline([(60, 6), (84, 16), (94, 42), (88, 66), (78, 44)]), 'shade', 'b', False),
   strand([(24, 48), (34, 22), (50, 10)], 'shade', 'b', 1.0), strand([(70, 48), (66, 22), (56, 10)], 'shade', 'b', 1.0)],
  [L(outline([(70, 48), (84, 40), (84, 20), (62, 4), (32, 4), (12, 18), (2, 44), (-2, 70), (4, 96), (20, 98), (28, 78), (36, 66), (46, 56), (58, 50)])),
   L(outline([(2, 46), (28, 50), (34, 68), (24, 94), (6, 94)]), 'shade', 'b', False)],
  [L(outline([(12, 80), (8, 44), (18, 18), (40, 4), (64, 4), (84, 16), (94, 40), (90, 80), (50, 86)])),
   L(blob([(10, 70), (2, 92), (12, 106), (28, 98), (26, 74)], 6), 'shade'),
   L(outline([(60, 6), (84, 18), (94, 44), (90, 78), (68, 84), (66, 40)]), 'shade', 'b', False)])

# Beth Doodle: chica con una boina verde oscura grande y el pelo lila rosado rizado por debajo, con las puntas abiertas
# hacia fuera a los lados; ojos castaños y sonrisa
BOINA = _c('#4f605a')
C('beth-doodle', 'chica', P('#c8a4b0', '#f9bc7d', iris='#6a4020', shade='#a88290'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=[(8, 62), (16, 52), (30, 48), (50, 50), (70, 48), (84, 52), (92, 62)]),
  [L(outline([(14, 80), (10, 50), (90, 50), (86, 80), (96, 92, 1), (80, 88), (78, 60), (22, 60), (20, 88), (4, 92, 1)])),
   L(blob([(14, 50), (26, 40), (50, 36), (74, 40), (86, 50), (80, 58), (50, 56), (20, 58)], 6), 'mid', 'f'),
   L(blob([(6, 36), (14, 12), (40, 0), (70, 2), (92, 16), (96, 34), (80, 44), (50, 46), (20, 44)], 8), BOINA, 'f'),
   L(ell(64, 2, 4, 3), BOINA, 'f')] + lashes_out(75, 14),
  [L(outline([(70, 50), (6, 46), (4, 80), (2, 92, 1), (20, 88), (36, 72), (56, 58)])),
   L(blob([(2, 34), (12, 8), (44, -2), (78, 4), (92, 22), (86, 40), (50, 46), (14, 46)], 8), BOINA, 'f')],
  [L(outline([(12, 84), (8, 50), (92, 50), (88, 84), (96, 94, 1), (50, 92), (4, 94, 1)])),
   L(blob([(6, 38), (14, 12), (40, 0), (70, 2), (92, 16), (96, 38), (80, 48), (50, 50), (20, 48)], 8), BOINA, 'f')])

# Betty Backer: chica con una capucha de animal naranja y crema con dos cuernos blandos hacia los lados, un antifaz crema
# alrededor de los ojos y el pelo morado oscuro largo y liso que le cae por detrás de la cara
HORANGE, HCREAM = _c('#f6a506'), _c('#fdfae0')
def _beast(view):
    if view == 'front':
        return [L(outline([(16, 36), (2, 22), (-6, 4), (6, 0), (22, 12), (36, 22)]), HORANGE, 'f'),
                L(outline([(84, 36), (98, 22), (106, 4), (94, 0), (78, 12), (64, 22)]), HORANGE, 'f'),
                L(blob([(14, 64), (12, 34), (26, 14), (50, 6), (74, 14), (88, 34), (86, 64), (50, 60)], 8), HORANGE, 'f'),
                L(blob([(40, 10), (50, 6), (60, 10), (60, 60), (40, 60)], 6), HCREAM, 'f', False),
                L(outline([(4, 6), (10, 2), (16, 12), (10, 14)]), HCREAM, 'f', False), L(outline([(96, 6), (90, 2), (84, 12), (90, 14)]), HCREAM, 'f', False),
                L(blob([(18, 62), (50, 58), (82, 62), (80, 86), (60, 84), (50, 90), (40, 84), (20, 86)], 6), HCREAM, 'f', True)]
    if view == 'side':
        return [L(outline([(40, 20), (32, 4), (44, -6), (58, 4), (60, 22)]), HORANGE, 'f'),
                L(blob([(6, 64), (4, 34), (22, 10), (50, 4), (76, 12), (88, 34), (86, 62), (60, 60), (30, 66)], 8), HORANGE, 'f'),
                L(blob([(66, 62), (90, 62), (90, 86), (70, 86)], 6), HCREAM, 'f', True)]
    return [L(outline([(16, 36), (2, 22), (-6, 4), (6, 0), (22, 12), (36, 22)]), HORANGE, 'f'),
            L(outline([(84, 36), (98, 22), (106, 4), (94, 0), (78, 12), (64, 22)]), HORANGE, 'f'),
            L(blob([(12, 72), (12, 34), (26, 14), (50, 6), (74, 14), (88, 34), (88, 72), (50, 76)], 8), HORANGE, 'f'),
            L(blob([(40, 10), (50, 6), (60, 10), (60, 72), (40, 72)], 6), HCREAM, 'f', False)]
C('betty-backer', 'chica', P('#5f4f5f', '#ebbd95', iris='#3a2a4a', shade='#3f2f33'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=96, hairline=False),
  [L(outline([(10, 116), (8, 60), (92, 60), (90, 116), (80, 100), (20, 100)]))] + _beast('front') +
  [L(ell(36, 75, 6, 6.4), WHITE, 'f', True), L(ell(64, 75, 6, 6.4), WHITE, 'f', True),
   L(ell(36, 76, 3.6, 4.4), _c('#3a2a4a'), 'f', False), L(ell(64, 76, 3.6, 4.4), _c('#3a2a4a'), 'f', False)],
  [L(outline([(4, 116), (4, 60), (50, 62), (40, 116)]))] + _beast('side') + [L(ell(82, 75, 3.4, 5), WHITE, 'f', True), L(ell(83, 76, 2, 3.4), _c('#3a2a4a'), 'f', False)],
  [L(outline([(8, 118), (8, 60), (92, 60), (92, 118), (50, 122)]))] + _beast('back'))

# Betty Evenson: chica de pelo gris verdoso recogido en un moño arriba con una colita, flequillo de mechones y un rizo
# suelto en la frente; ojos verde oliva, coloretes naranjas y sonrisa
C('betty-evenson', 'chica', P('#9abaab', '#f8bc7d', iris='#7a7a20', shade='#76746c'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=94, hairline=hl(5, 60, 46, 56, jit=2, seed=53)),
  [L(ell(50, -2, 12, 9)), L(outline([(50, -8), (62, -18), (72, -14, 1), (62, -6)])),
   L(outline([(16, 64), (12, 40), (22, 14), (50, 4), (78, 14), (88, 40), (84, 64), (80, 46), (20, 46)])),
   L(outline([(60, 6), (82, 16), (88, 42), (84, 60), (76, 40)]), 'shade', 'b', False),
   strand([(50, 50), (46, 58), (52, 62), (54, 56)], 'mid', 'f', 1.4),
   L(ell(26, 86, 4.4, 3), _c('#f0905a'), 'f', False), L(ell(74, 86, 4.4, 3), _c('#f0905a'), 'f', False)] + lashes_out(75, 14),
  [L(ell(46, -2, 11, 9)), L(outline([(40, -6), (30, -16), (22, -12, 1), (34, -2)])),
   L(outline([(70, 48), (84, 40), (82, 20), (62, 4), (32, 4), (12, 18), (4, 42), (8, 66), (22, 74), (36, 66), (46, 56), (58, 50)]))],
  [L(ell(50, -2, 12, 9)), L(outline([(16, 76), (12, 40), (22, 14), (50, 4), (78, 14), (88, 40), (84, 76), (50, 82)])),
   L(outline([(60, 6), (82, 16), (88, 42), (84, 74), (66, 80), (66, 40)]), 'shade', 'b', False)])

# Bigsby Pigford: gorro de cerdito rosado con las orejas, el morro marrón y los ojos encima, del que asoma el pelo morado
# por los lados; pecas, ojos castaños de enfado y boca seria
PIG, SNOUT = _c('#f4d0b8'), _c('#7c3924')
def _pighat(view):
    if view == 'front':
        return [L(outline([(12, 22), (2, 2, 1), (24, 12)]), _c('#b5755d')), L(outline([(88, 22), (98, 2, 1), (76, 12)]), _c('#b5755d')),
                L(blob([(6, 62), (6, 32), (20, 10), (50, 2), (80, 10), (94, 32), (94, 62), (50, 56)], 8), PIG),
                L(blob([(16, 50), (18, 30), (34, 20), (50, 22), (66, 20), (82, 30), (84, 50), (50, 52)], 6), SNOUT, 'b', True),
                L(blob([(22, 46), (24, 32), (44, 30), (44, 44)], 4), _c('#5a2010'), 'b', False), L(blob([(78, 46), (76, 32), (56, 30), (56, 44)], 4), _c('#5a2010'), 'b', False)]
    if view == 'side':
        return [L(outline([(30, 14), (22, -6, 1), (44, 6)]), _c('#b5755d')),
                L(blob([(4, 64), (2, 34), (18, 8), (50, 2), (82, 10), (96, 34), (92, 58), (60, 58), (30, 64)], 8), PIG),
                L(blob([(70, 20), (94, 28), (98, 46), (80, 50)], 6), SNOUT, 'b', True)]
    return [L(outline([(12, 22), (2, 2, 1), (24, 12)]), _c('#b5755d')), L(outline([(88, 22), (98, 2, 1), (76, 12)]), _c('#b5755d')),
            L(blob([(6, 74), (6, 32), (20, 10), (50, 2), (80, 10), (94, 32), (94, 74), (50, 78)], 8), PIG)]
C('bigsby-pigford', 'normal', P('#5a3a8a', '#efab7a', iris='#7a3a1a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=False),
  [L(outline([(14, 60), (12, 84), (20, 86), (22, 62)])), L(outline([(86, 60), (88, 84), (80, 86), (78, 62)]))] + _pighat('front') + freckles(86, 22),
  [L(outline([(50, 60), (44, 82), (56, 84), (58, 62)]))] + _pighat('side'),
  _pighat('back') + [L(outline([(14, 72), (20, 84), (50, 86), (80, 84), (86, 72)]))])

# Bill Clanger: hombre de piel beige pálida con cara larga y mandíbula ancha llena de arrugas; pelo azul petróleo plano
# que se abre en dos puntas a los lados como un yunque; ojos caídos medio cerrados y media sonrisa torcida con un colmillo
C('bill-clanger', 'corpulento', P('#284c5d', '#e6d2b5', iris='#1a1a1a', shade='#1e3846'),
  F(eyes='none', brows=False, mouth='none', hairline=False, face_front=sq_face(2, 112), face_side=face_side(chin=8, jaw=6, nose=3)),
  [L(outline([(16, 46), (10, 36), (-2, 40, 1), (12, 26), (30, 16), (50, 14), (70, 16), (88, 26), (102, 40, 1), (90, 36), (84, 46), (50, 40)])),
   L(quad((28, 76), (36, 72), (44, 76)), OUTC, 'f', False, False, 1.8), L(quad((56, 76), (64, 72), (72, 76)), OUTC, 'f', False, False, 1.8),
   L(quad((28, 78), (36, 80), (44, 78)), OUTC, 'f', False, False, 1.0), L(quad((56, 78), (64, 80), (72, 78)), OUTC, 'f', False, False, 1.0),
   L(blob([(46, 66), (54, 66), (56, 88), (50, 90), (44, 88)], 6), _c('#d8c0a0'), 'f', True),
   L([(34, 100), (46, 98), (60, 100), (68, 96)], OUTC, 'f', False, False, 1.8), L([(58, 99), (60, 104), (62, 99)], WHITE, 'f', False),
   L([(18, 84), (26, 92)], _c('#a18874'), 'f', False, False, 1.0), L([(82, 84), (74, 92)], _c('#a18874'), 'f', False, False, 1.0),
   L([(24, 98), (34, 108)], _c('#a18874'), 'f', False, False, 1.0), L([(76, 98), (66, 108)], _c('#a18874'), 'f', False, False, 1.0)],
  [L(outline([(70, 40), (84, 30), (78, 18), (50, 12), (24, 18), (2, 30, 1), (14, 34), (8, 52), (20, 60), (40, 52), (56, 44)])),
   L(quad((76, 76), (81, 72), (86, 76)), OUTC, 'f', False, False, 1.8), L([(76, 100), (86, 98)], OUTC, 'f', False, False, 1.8)],
  [L(outline([(16, 54), (10, 36), (-2, 40, 1), (12, 26), (30, 16), (50, 14), (70, 16), (88, 26), (102, 40, 1), (90, 36), (84, 54), (50, 60)]))])

# Bill Fierce: hombre de cara larga con un gorro de pájaro rosa (con su pico naranja y ojitos encima), gafas de buceo verdes
# redondas, nariz larga y sonrisa de dientes
BIRD, BEAK = _c('#f9bbaf'), _c('#f0a030')
def _birdhat(view):
    if view == 'front':
        return [L(blob([(4, 68), (12, 30), (30, 4), (50, -2), (70, 4), (88, 30), (96, 68), (50, 62)], 8), BIRD),
                L(ell(40, 22, 2, 2.4), BLACK, 'b', False), L(ell(60, 22, 2, 2.4), BLACK, 'b', False),
                L(outline([(44, 28), (56, 28), (50, 38, 1)]), BEAK, 'b')]
    if view == 'side':
        return [L(blob([(2, 70), (6, 30), (28, 4), (54, -2), (80, 8), (94, 34), (92, 62), (50, 62)], 8), BIRD),
                L(ell(78, 22, 2, 2.4), BLACK, 'b', False), L(outline([(88, 26), (100, 32, 1), (88, 36)]), BEAK, 'b')]
    return [L(blob([(4, 76), (12, 30), (30, 4), (50, -2), (70, 4), (88, 30), (96, 76), (50, 80)], 8), BIRD)]
C('bill-fierce', 'delgado', P('#3f4324', '#fcc270', iris='#1a1a1a'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=100, hairline=False, face_front=face(chin=114, w=-3), face_side=face_side(chin=12, nose=5)),
  _birdhat('front') + [L(ell(36, 66, 10, 9), _c('#2b3a16'), 'f', True), L(ell(64, 66, 10, 9), _c('#2b3a16'), 'f', True),
                       L(ell(36, 66, 5, 4.6), _c('#9aa040'), 'f', False), L(ell(64, 66, 5, 4.6), _c('#9aa040'), 'f', False),
                       L(blob([(46, 72), (54, 72), (56, 92), (50, 94), (44, 92)], 6), _c('#c78251'), 'f', True)],
  _birdhat('side') + [L(ell(82, 66, 6, 9), _c('#2b3a16'), 'f', True), L(ell(84, 66, 3, 4.6), _c('#9aa040'), 'f', False),
                      L(blob([(84, 72), (98, 86), (92, 92), (84, 88)], 6), _c('#c78251'), 'f', True)],
  _birdhat('back'))

# Bish Beaton: la misma máscara tribal de madera que su hermano (ojos de espiral morada y sonrisa enorme de dientes
# cuadrados), con las orejas de mono y un pincho de pelo verde lima alto en llama
LIME = _c('#cfdc75')
C('bish-beaton', 'normal', P('#cfdc75', '#b4743b', iris='#1a1a1a', shade='#a8b850'),
  F(eyes='none', brows=False, mouth='none', hairline=False, big_ears=2, ear_out=2,
    face_front=blob([(18, 46), (50, 30), (82, 46), (86, 76), (78, 100), (62, 112), (50, 114), (38, 112), (22, 100), (14, 76)], 8)),
  [L(outline([(36, 36), (40, 16), (52, -4), (62, -20, 1), (60, 6), (66, 20), (64, 36)])),
   L(ell(34, 70, 8, 7.4), _c('#efe6f0'), 'f', True), L(ell(34, 70, 5, 4.6), _c('#9a5aa8'), 'f', False), L(ell(34, 70, 2.6, 2.4), _c('#efe6f0'), 'f', False),
   L(ell(34, 70, 1.2, 1.2), BLACK, 'f', False),
   L(ell(66, 70, 8, 7.4), _c('#efe6f0'), 'f', True), L(ell(66, 70, 5, 4.6), _c('#9a5aa8'), 'f', False), L(ell(66, 70, 2.6, 2.4), _c('#efe6f0'), 'f', False),
   L(ell(66, 70, 1.2, 1.2), BLACK, 'f', False),
   L(ell(46, 84, 1.6, 1.2), OUTC, 'f', False), L(ell(54, 84, 1.6, 1.2), OUTC, 'f', False),
   L(blob([(22, 90), (50, 92), (78, 90), (72, 104), (50, 108), (28, 104)], 6), WHITE, 'f', True),
   L([(28, 96), (36, 96), (36, 100), (44, 100), (44, 96), (56, 96), (56, 100), (64, 100), (64, 96), (72, 96)], OUTC, 'f', False, False, 1.0)],
  [L(outline([(40, 32), (46, 12), (58, -6), (68, -20, 1), (64, 8), (70, 30)])),
   L(ell(80, 70, 5, 7), _c('#efe6f0'), 'f', True), L(ell(82, 70, 2.6, 3.6), _c('#9a5aa8'), 'f', False),
   L(blob([(66, 90), (90, 90), (86, 104), (70, 106)], 6), WHITE, 'f', True)],
  [L(outline([(36, 36), (40, 16), (52, -4), (62, -20, 1), (60, 6), (66, 20), (64, 36)]))])

# Blake Nailor (portero): grandullón con un pañuelo azul petróleo pequeño atado en lo alto de la cabeza, un parche negro en
# el ojo, patillas oscuras y boca de disgusto con los dientes
C('blake-nailor', 'corpulento', P('#362d24', '#f8bb80', iris='#1a1a1a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, big_ears=1, ear_out=4,
    face_front=blob([(14, 48), (50, 34), (86, 48), (92, 78), (86, 102), (66, 114), (50, 116), (34, 114), (14, 102), (8, 78)], 8), face_side=face_side(chin=10, jaw=6)),
  [L(blob([(20, 46), (24, 24), (40, 12), (60, 12), (76, 24), (80, 46), (50, 40)], 8), _c('#487784')),
   L(outline([(12, 52), (10, 80), (16, 84), (20, 56)])), L(outline([(88, 52), (90, 80), (84, 84), (80, 56)])),
   L(ell(36, 74, 6, 5), WHITE, 'f', True), L(ell(37, 75, 2.4, 2.6), BLACK, 'f', False), L([(28, 66), (44, 68)], OUTC, 'f', False, False, 2.0),
   L(ell(64, 74, 9, 8), BLACK, 'f', True), L([(56, 70), (16, 56)], BLACK, 'f', False, False, 1.8), L([(72, 70), (88, 60)], BLACK, 'f', False, False, 1.8),
   L(ell(50, 86, 3, 2.4), _c('#d8935a'), 'f', True),
   L(blob([(38, 96), (62, 96), (60, 104), (40, 104)], 4), WHITE, 'f', True), L([(38, 100), (62, 100)], OUTC, 'f', False, False, 0.8)],
  [L(blob([(30, 34), (36, 14), (56, 8), (74, 16), (76, 34), (50, 36)], 8), _c('#487784')),
   L(outline([(52, 54), (46, 80), (56, 84), (60, 58)])),
   L(ell(82, 74, 6, 7), BLACK, 'f', True), L([(76, 70), (40, 60)], BLACK, 'f', False, False, 1.8)],
  [L(blob([(20, 46), (24, 24), (40, 12), (60, 12), (76, 24), (80, 46), (50, 40)], 8), _c('#487784')), L([(14, 60), (86, 60)], BLACK, 'f', False, False, 1.8)])

# Bob Beelzy (portero): grandullón de piel roja rosada con el pelo gris pardo levantado en dos cuernos de punta a los lados;
# ojos de enfado con el borde negro grueso, nariz grande y boca abierta de dientes bajo el bigote
C('bob-beelzy', 'corpulento', P('#62594b', '#e79283', iris='#1a1a1a', shade='#43342d'),
  F(eyes='sharp', brows='angry', mouth='none', hairline=[(10, 60), (20, 48), (36, 44), (50, 46), (64, 44), (80, 48), (90, 60)], big_ears=1, ear_out=4,
    face_front=blob([(14, 48), (50, 36), (86, 48), (92, 78), (86, 102), (66, 114), (50, 116), (34, 114), (14, 102), (8, 78)], 8), face_side=face_side(chin=10, jaw=6, nose=4)),
  [L(outline([(16, 60), (10, 40), (-4, 0, 1), (20, 20), (36, 14), (50, 16), (64, 14), (80, 20), (104, 0, 1), (90, 40), (84, 60), (80, 48), (20, 48)])),
   L(outline([(60, 16), (80, 20), (102, 2), (90, 40), (84, 56), (74, 34)]), 'shade', 'b', False),
   L(quad((24, 70), (32, 80), (44, 78)), OUTC, 'f', False, False, 3.0), L(quad((76, 70), (68, 80), (56, 78)), OUTC, 'f', False, False, 3.0),
   L(blob([(44, 78), (56, 78), (60, 92), (50, 94), (40, 92)], 6), _c('#c87060'), 'f', True),
   L(blob([(38, 98), (62, 98), (60, 108), (40, 108)], 4), _c('#3a2020'), 'f', True), L([(40, 101), (60, 101)], WHITE, 'f', False, False, 2.0)],
  [L(outline([(70, 46), (84, 38), (80, 22), (60, 14), (40, -8, 1), (36, 14), (14, 20), (4, 42), (8, 64), (22, 72), (36, 64), (46, 56), (58, 50)])),
   L(blob([(84, 80), (98, 90), (92, 96), (84, 94)], 6), _c('#c87060'), 'f', True)],
  [L(outline([(16, 76), (10, 40), (-4, 0, 1), (20, 20), (36, 14), (50, 16), (64, 14), (80, 20), (104, 0, 1), (90, 40), (84, 76), (50, 82)])),
   L(outline([(60, 16), (80, 20), (102, 2), (90, 40), (84, 74), (66, 80), (66, 34)]), 'shade', 'b', False)])

# Bob Daruma: casco rojo redondo con dos espirales amarillas a los lados que le tapa hasta la mandíbula, con un flequillo
# rubio que le asoma; ojos redondos de enfado y boca pequeña abierta
HRED, HRED_D, SWIRL = _c('#c2292f'), _c('#7a2423'), _c('#f0c030')
def _daruma(view):
    if view == 'front':
        return [L(blob([(4, 96), (2, 50), (12, 18), (50, 2), (88, 18), (98, 50), (96, 96), (84, 98), (82, 56), (18, 56), (16, 98)], 8), HRED),
                L(blob([(60, 6), (86, 18), (96, 50), (94, 94), (86, 96), (84, 54)], 6), HRED_D, 'b', False),
                strand([(10, 44), (14, 36), (20, 40), (16, 48), (8, 46)], SWIRL, 'b', 2.0), strand([(90, 44), (86, 36), (80, 40), (84, 48), (92, 46)], SWIRL, 'b', 2.0)]
    if view == 'side':
        return [L(blob([(86, 54), (88, 22), (64, 2), (32, 2), (10, 16), (0, 50), (4, 96), (40, 100), (56, 86), (60, 62)], 8), HRED),
                strand([(24, 50), (32, 38), (42, 46), (34, 58), (22, 54)], SWIRL, 'b', 2.0)]
    return [L(blob([(4, 98), (2, 50), (12, 18), (50, 2), (88, 18), (98, 50), (96, 98), (50, 104)], 8), HRED),
            L(blob([(60, 6), (86, 18), (96, 50), (94, 96), (70, 100), (70, 40)], 6), HRED_D, 'b', False)]
C('bob-daruma', 'normal', P('#c99e5b', '#eed5bb', iris='#1a1a1a', shade='#a8804a'),
  F(eyes='round', brows='angry', mouth='none', hairline=False),
  _daruma('front') + [fr([(20, 56), (34, 52), (50, 54), (62, 60), (58, 74, 1), (50, 62), (40, 66, 1), (30, 62), (22, 68, 1)]),
                      L(ell(50, 96, 3.4, 3.4), _c('#5a2020'), 'f', True), L(ell(50, 94.6, 2.4, 1.2), WHITE, 'f', False)],
  _daruma('side') + [fr([(70, 56), (84, 54), (88, 70, 1), (80, 62)])],
  _daruma('back'))

# Bob Jammen (portero): cabeza afeitada con un casquete crema y tres rastas marrones gruesas de pie encima; gafas de visor
# verde oscuro que le tapan los ojos y boca seria
CAP3, DREAD = _c('#d8d5c5'), _c('#72521e')
C('bob-jammen', 'normal', P('#72521e', '#dca257', iris='#1a1a1a', shade='#46331f'),
  F(eyes='none', brows=False, mouth='line', mouth_y=96, hairline=False, face_front=face(chin=108, w=-1)),
  [L(blob([(16, 52), (16, 28), (30, 10), (50, 4), (70, 10), (84, 28), (84, 52), (50, 48)], 8), CAP3),
   L(outline([(28, 22), (18, -10), (24, -14), (36, 18)]), DREAD), L(outline([(46, 14), (46, -18), (54, -18), (54, 14)]), DREAD),
   L(outline([(72, 22), (82, -10), (76, -14), (64, 18)]), DREAD),
   strand([(26, 12), (22, 2)], 'shade', 'b', 1.0), strand([(50, 6), (50, -10)], 'shade', 'b', 1.0), strand([(74, 12), (78, 2)], 'shade', 'b', 1.0),
   L(outline([(10, 70), (30, 66), (50, 74), (70, 66), (90, 70), (84, 80), (60, 80), (50, 84), (40, 80), (16, 80)]), _c('#0a4a1c'), 'f')],
  [L(blob([(30, 16), (50, 4), (76, 10), (86, 30), (80, 48), (30, 52), (10, 40)], 8), CAP3),
   L(outline([(44, 12), (40, -18), (48, -20), (52, 10)]), DREAD), L(outline([(64, 16), (70, -14), (76, -10), (70, 18)]), DREAD),
   L(outline([(60, 68), (90, 66), (92, 78), (64, 80)]), _c('#0a4a1c'), 'f')],
  [L(blob([(16, 60), (16, 28), (30, 10), (50, 4), (70, 10), (84, 28), (84, 60), (50, 64)], 8), CAP3),
   L(outline([(28, 22), (18, -10), (24, -14), (36, 18)]), DREAD), L(outline([(46, 14), (46, -18), (54, -18), (54, 14)]), DREAD),
   L(outline([(72, 22), (82, -10), (76, -14), (64, 18)]), DREAD), L([(10, 72), (90, 72)], _c('#0a4a1c'), 'f', False, False, 2.4)])

# Bobbie Tomey: chica de piel clara con el pelo rojo peinado hacia atrás muy liso que acaba en una melena corta a los
# lados; gafas ovaladas doradas, ojos lila y boca seria
C('bobbie-tomey', 'chica', P('#b0413f', '#fdeab8', iris='#7a6aa8', shade='#87332e'),
  F(eyes='normal', brows=True, mouth='frown', mouth_y=95, glasses=_c('#a8803a'), hairline=[(8, 66), (14, 50), (30, 40), (50, 36), (70, 40), (86, 50), (92, 66)]),
  dome('front', top=0, w=46, cy=44, seed=59, long=96, flare=2) +
  [strand([(30, 40), (34, 20), (46, 8)], 'shade', 'b', 1.0), strand([(70, 40), (66, 20), (54, 8)], 'shade', 'b', 1.0)] + lashes_out(75, 14),
  dome('side', top=0, w=46, cy=44, seed=59, long=96, flare=2, fr=40),
  dome('back', top=0, w=46, cy=44, seed=59, long=96, flare=2, ends=3))

# Bobby Green (del dúo): máscara de héroe blanca con dos ojos verdes de insecto de pupila amarilla, pañuelo blanco atado
# con las puntas al aire y pinchos rubios claros encima; se le ve la sonrisa
MASKW, BUGG, BUGY = _c('#f4f0ea'), _c('#8ad030'), _c('#f0e040')
C('bobby-green-s-duo', 'normal', P('#faf2b4', '#e8c8a8', iris='#1a1a1a', shade='#d8cc80'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=96, hairline=False),
  messy('front', amp=12, n=10, seed=81, lo=50, cy=36, ry=36) +
  [L(blob([(14, 80), (12, 46), (24, 30), (50, 26), (76, 30), (88, 46), (86, 80), (70, 88), (50, 86), (30, 88)], 8), MASKW, 'f'),
   L(outline([(12, 70), (-4, 76, 1), (2, 84), (-6, 94, 1), (14, 84)]), MASKW, 'f'),
   L(blob([(24, 52), (40, 50), (46, 64), (42, 84), (34, 86), (28, 70)], 6), BUGG, 'f', True),
   L(blob([(76, 52), (60, 50), (54, 64), (58, 84), (66, 86), (72, 70)], 6), BUGG, 'f', True),
   L(ell(34, 60, 4, 4.4), BUGY, 'f', False), L(ell(66, 60, 4, 4.4), BUGY, 'f', False)],
  messy('side', amp=12, n=10, seed=81, lo=50, cy=36, ry=36) +
  [L(blob([(60, 40), (84, 36), (90, 60), (88, 84), (66, 86), (56, 64)], 8), MASKW, 'f'), L(blob([(76, 52), (88, 54), (88, 80), (78, 82)], 6), BUGG, 'f', True),
   L(outline([(36, 50), (8, 52, 1), (20, 60), (2, 70, 1), (36, 62)]), MASKW, 'f')],
  messy('back', amp=12, n=10, seed=81, lo=50, cy=36, ry=36) +
  [L(outline([(10, 52), (90, 52), (90, 62), (10, 62)]), MASKW, 'f'), L(outline([(46, 58), (30, 80, 1), (50, 66), (70, 80, 1), (54, 58)]), MASKW, 'f')])
