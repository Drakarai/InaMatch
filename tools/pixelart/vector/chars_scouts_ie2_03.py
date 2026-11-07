"""Ojeadores de IE2 (scouts-ie2), tanda 03: dibujados a partir de su retrato de Victory Road (casi ninguno tiene modelo 3D);
claves 'scouts-ie2:<id>'. El perfil y la espalda se deducen del peinado del retrato. Reutiliza ayudas de las tandas de
IE1 (dome/hl/face de la 09, fr/bowl/cejas gruesas de la 03, narices y ojos de la 10)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars import messy  # noqa: F401
from chars_scouts_ie1_03 import blush, bowl, eyes_custom, fr, side_brow, side_eye_custom, thick_brows  # noqa: F401
from chars_scouts_ie1_09 import _c, dome, face, face_side, hl, mark  # noqa: F401
from chars_scouts_ie1_10 import nose_line, nose_tri, squint  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401

K = 'scouts-ie2:'
WHITE = (250, 250, 250, 255)
BLACK = (24, 18, 20, 255)
LIP = (214, 120, 120, 255)
RED = (200, 60, 50, 255)


def F(**k):
    d = {'eyes': 'normal', 'mouth': 'line'}
    d.update(k)
    return d


def C(pid, body, palette, f, front, side, back):
    """Como en la tanda 09 de IE1: el nacimiento del pelo baja por el borde de la cara para que su raya no cruce el pelo."""
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[K + pid] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def skull(view='front', c='skin'):
    """Calva: la bóveda del cráneo en piel."""
    if view == 'front':
        return [L(outline([(17, 66), (13, 42), (22, 18), (50, 6), (78, 18), (87, 42), (83, 66), (50, 72)]), c)]
    if view == 'side':
        return [L(outline([(80, 56), (88, 38), (80, 16), (56, 4), (30, 6), (12, 20), (4, 44), (6, 70), (20, 84), (40, 84), (52, 70)]), c)]
    return [L(outline([(16, 76), (12, 44), (22, 18), (50, 6), (78, 18), (88, 44), (84, 76), (50, 84)]), c)]


def ears_pointy(view, c='skin', h=12):
    """Orejas de punta (duendes, dragones)."""
    if view == 'front':
        return [L(outline([(16, 64), (2, 58 - h, 1), (14, 80)]), c, 'b'), L(outline([(84, 64), (98, 58 - h, 1), (86, 80)]), c, 'b')]
    if view == 'back':
        return [L(outline([(16, 64), (0, 56 - h, 1), (14, 80)]), c, 'b'), L(outline([(84, 64), (100, 56 - h, 1), (86, 80)]), c, 'b')]
    return [L(outline([(40, 66), (30, 52 - h, 1), (52, 62), (50, 78)]), c, 'f')]


def teeth_grin(y=94, w=13, h=7):
    """Sonrisa ancha de dientes en punta."""
    pts = [(50 - w, y - 2), (50 + w, y - 2), (50 + w * 0.6, y + h), (50 - w * 0.6, y + h)]
    out = [L(pts, WHITE, 'f', False, True)]
    for i in range(5):
        x = 50 - w * 0.8 + i * w * 0.4
        out.append(L([(x - 2, y - 2), (x, y + 2), (x + 2, y - 2)], OUTC, 'f', False, False, 0.8))
    return out


# ---------------------------------------------------------------------------------------------------------------- 1-8

# Dotty Hickman: melena rubia lisa con la raya a un lado que le tapa el ojo izquierdo y cae por detrás hasta los hombros
C('dotty-hickman', 'chica', pal('#e2b22a', '#f6cca4', '#3a2a24', shade='#b8861c'),
  F(eyes='normal', mouth='frown', mouth_y=94, hairline=False, eye_sep=13),
  dome('front', top=4, w=46, cy=46, long=106, flare=4) +
  [fr([(40, 10), (70, 8), (90, 30), (92, 62), (88, 96, 1), (74, 88), (60, 92), (52, 96, 1), (50, 70), (44, 44), (30, 52), (22, 66, 1), (20, 44), (28, 22)])],
  dome('side', top=4, w=46, cy=46, long=104, flare=4, fr=60) + [fr([(62, 10), (84, 24), (92, 46), (88, 62, 1), (78, 50), (66, 56)])],
  dome('back', top=4, w=46, cy=46, long=106, flare=4, ends=4))

# Doug Lapp: grandullón de cara cuadrada; pelo verde azulado muy oscuro corto en pinchos, cejas gruesas en una sola raya
# fruncida, ojos cerrados, boca torcida y una cicatriz en la barbilla
C('doug-lapp', 'corpulento', pal('#2c4a4e', '#f4c088', shade='#1e3438'),
  F(eyes='closed', brows=False, mouth='frown', mouth_y=98, eye_y=76, hairline=hl(6, 60, 40, 46, jit=2, seed=5),
    face_front=face(w=4, chin=108, jaw=4)),
  dome('front', top=12, w=42, cy=46, n=10, amp=6, sb=62, seed=6) + thick_brows(64, BLACK, 4.0, tilt=0.6, w=16) +
  nose_tri(88, 5, 9) + [mark([(54, 104), (62, 98)], (224, 170, 120, 255), w=1.4)],
  dome('side', top=12, w=42, cy=46, n=10, amp=6, nape=76, fr=48, seed=6) + side_brow(64, BLACK, 4.0, 0.6),
  dome('back', top=12, w=42, cy=46, n=10, amp=6, nape=76, seed=6))

# Doyle Palmer: portero gordo de piel verde grisácea, calvo, con un rizo amarillo de punta en lo alto; ojitos redondos,
# hocico y boquita rosa en "o"
GS = '#8eb8a6'
C('doyle-palmer', 'corpulento', pal('#d8a830', GS, '#1e1e1e', skin_d='#6e9a88', shade='#b08418'),
  F(eyes='round', brows=False, mouth='none', eye_y=72, eye_sep=11, hairline=False, big_ears=2, face_front=face(w=6, chin=110, jaw=8)),
  skull('front', 'skin') + [L(outline([(46, 10), (40, -10), (50, -24), (62, -16, 1), (54, -12), (54, 10)]), 'mid', 'f'),
                            L(ell(50, 82, 4, 2.6), (90, 120, 108, 255), 'f', False), L(ell(50, 96, 5, 3.2), LIP, 'f', True)],
  skull('side', 'skin') + [L(outline([(50, 6), (46, -12), (56, -24), (66, -16, 1), (58, -10), (60, 6)]), 'mid', 'f'),
                           L(ell(86, 96, 3, 3), LIP, 'f', True)],
  skull('back', 'skin') + [L(outline([(46, 10), (40, -10), (50, -24), (62, -16, 1), (54, -12), (54, 10)]), 'mid', 'f')])

# Drack Dragon-Gorn: piel verde agua, orejas de punta, pelo verde azulado oscuro en pinchos altísimos hacia arriba, ojos
# blancos brillantes y una sonrisa enorme de colmillos
C('drack-dragon-gorn', 'normal', pal('#2e5a68', '#7cae9c', '#f4f4f4', skin_d='#5a8a7a', shade='#1e3e4a'),
  F(eyes='sharp', brows='angry', mouth='none', hairline=hl(5, 60, 44, 52, seed=8)),
  ears_pointy('front') +
  [L(outline([(16, 60), (10, 36), (-4, 0, 1), (18, 20), (16, -20, 1), (32, 12), (36, -30, 1), (46, 8), (56, -32, 1), (62, 8), (78, -22, 1), (74, 14),
              (102, 0, 1), (90, 36), (84, 60), (80, 44), (20, 44)])),
   L(outline([(56, -28), (62, 8), (78, -18), (74, 14), (98, 4), (88, 36), (84, 56), (74, 30)]), 'shade', 'b', False)] + teeth_grin(94, 14, 8),
  ears_pointy('side') + [L(outline([(70, 48), (82, 40), (96, 10, 1), (78, 22), (80, -20, 1), (62, 8), (56, -30, 1), (44, 4), (30, -26, 1), (26, 8), (2, -6, 1),
                                    (8, 24), (4, 50), (20, 64), (40, 60), (56, 50)])),
                         L(quad((78, 94), (84, 98), (88, 92)), OUTC, 'f', False, False, 1.4)],
  ears_pointy('back') + [L(outline([(14, 70), (8, 36), (-4, 0, 1), (18, 20), (16, -20, 1), (32, 12), (36, -30, 1), (46, 8), (56, -32, 1), (62, 8), (78, -22, 1),
                                    (74, 14), (104, 0, 1), (92, 36), (86, 70), (50, 78)]))])

# Draco Scallon: cabeza de rana de piel verde agua, orejas de punta, una boca enorme de labios rosas de lado a lado,
# párpados caídos con mirada de malo y un moñito castaño en forma de hojas encima
C('draco-scallon', 'normal', pal('#7a4a24', '#80b0a0', '#1e1e1e', skin_d='#5e8c7c', shade='#5a3418'),
  F(eyes='sharp', brows='angry', mouth='none', eye_y=72, hairline=False, face_front=face(w=8, chin=104, jaw=8)),
  ears_pointy('front', h=6) + skull('front') +
  [L(outline([(36, 10), (30, -6, 1), (42, 2), (44, -14, 1), (52, 0), (60, -14, 1), (60, 2), (72, -6, 1), (64, 10)]), 'mid'),
   L(ell(50, 10, 8, 3), (230, 196, 90, 255), 'f', True),
   L(blob([(8, 88), (30, 84), (50, 86), (70, 84), (92, 88), (80, 98), (50, 100), (20, 98)], 6), LIP, 'f', True)],
  ears_pointy('side', h=6) + skull('side') +
  [L(outline([(44, 6), (38, -10, 1), (50, -2), (54, -16, 1), (60, -2), (70, -10, 1), (64, 8)]), 'mid'),
   L(blob([(60, 88), (90, 84), (94, 92), (86, 98), (64, 96)], 6), LIP, 'f', True)],
  ears_pointy('back', h=6) + skull('back') +
  [L(outline([(36, 10), (30, -6, 1), (42, 2), (44, -14, 1), (52, 0), (60, -14, 1), (60, 2), (72, -6, 1), (64, 10)]), 'mid')])

# Dreama Bartle: pelo castaño anaranjado corto en mechones de punta echados a un lado, un flequillo largo que le cae entre
# los ojos y dos puntas por detrás de las orejas; ojos verde azulado y sonrisa
C('dreama-bartle', 'chica', pal('#c8702a', '#f6cca4', '#2e6a72', shade='#9a4e18', deep='#7a3a10'),
  F(eyes='normal', mouth='smile', mouth_y=94, hairline=False),
  dome('front', top=2, w=46, cy=46, n=7, amp=7, sweep=0.3, sb=74, seed=11) +
  [fr([(20, 30), (40, 14), (70, 12), (88, 30), (86, 52), (78, 42), (62, 46), (52, 82, 1), (48, 48), (36, 50), (24, 60, 1), (20, 46)]),
   L(outline([(12, 66), (4, 84, 1), (18, 74)]), 'mid', 'b'), L(outline([(88, 66), (96, 84, 1), (82, 74)]), 'mid', 'b')],
  dome('side', top=2, w=46, cy=46, n=7, amp=7, sweep=0.3, nape=86, fr=56, seed=11) + [fr([(66, 12), (88, 26), (94, 46), (90, 62, 1), (80, 50), (70, 54)])],
  dome('back', top=2, w=46, cy=46, n=7, amp=7, sweep=0.3, nape=90, seed=11))

# Duke Scrubine: portero de piel morena con pelo castaño oscuro corto en pinchos revueltos; cejas fruncidas, ojos redondos
# y boca apretada
C('duke-scrubine', 'normal', pal('#4a3228', '#b47a52', '#1e1e1e', shade='#2e1e18'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=94, hairline=hl(6, 60, 44, 52, jit=3, seed=13)),
  dome('front', top=6, w=46, cy=44, n=11, amp=7, sb=62, seed=14) + nose_line(86),
  dome('side', top=6, w=46, cy=44, n=11, amp=7, nape=82, fr=50, seed=14),
  dome('back', top=6, w=46, cy=44, n=11, amp=7, nape=82, seed=14))

# Ebirina: melena castaña rosada larga que le enmarca la cara como una capucha y le cae hasta el pecho; flequillo de
# mechones, ojos verde oliva con dos marcas moradas debajo y ceño
PURP = _c('#7a4ab0')
C('ebirina', 'chica', pal('#9a6a5e', '#f2c8a0', '#7a7a3a', shade='#764e44'),
  F(eyes='normal', brows='angry', mouth='frown', mouth_y=94, hairline=hl(7, 64, 46, 58, seed=15)),
  dome('front', top=2, w=48, cy=48, long=112, flare=6) +
  [mark([(30, 84), (36, 84), (33, 90)], PURP), mark([(64, 84), (70, 84), (67, 90)], PURP)],
  dome('side', top=2, w=48, cy=48, long=110, flare=6, fr=58) + [mark([(78, 84), (84, 84), (81, 90)], PURP)],
  dome('back', top=2, w=48, cy=48, long=112, flare=6, ends=5))


# --------------------------------------------------------------------------------------------------------------- 9-16

def round_glasses(view, c, y=76, sep=14, r=7.5, lens=None, w=2.0):
    """Gafas redondas de montura gruesa (lens: cristal de color)."""
    out = []
    if view == 'front':
        for cx in (50 - sep, 50 + sep):
            if lens:
                out.append(L(ell(cx, y, r, r), lens, 'f', False))
            out.append(L(ell(cx, y, r, r) + [ell(cx, y, r, r)[0]], c, 'f', False, False, w))
        out.append(L([(50 - sep + r, y), (50 + sep - r, y)], c, 'f', False, False, w * 0.8))
    elif view == 'side':
        if lens:
            out.append(L(ell(82, y, r * 0.6, r), lens, 'f', False))
        out += [L(ell(82, y, r * 0.6, r) + [ell(82, y, r * 0.6, r)[0]], c, 'f', False, False, w), L([(78, y - 1), (50, y - 4)], c, 'f', False, False, w * 0.8)]
    return out


# Ed Hartsell: pelo verde peinado hacia atrás con dos mechones largos que le caen por delante de las orejas hasta la
# mandíbula; piel morena, cara larga, ojos afilados de párpado caído y boca seria
C('ed-hartsell', 'delgado', pal('#4e7e2c', '#c48c5c', '#1e1e1e', shade='#36601c'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=98, hairline=[(14, 60), (20, 40), (36, 32), (50, 30), (64, 32), (80, 40), (86, 60)],
    face_front=face(chin=108)),
  dome('front', top=0, w=44, cy=42, n=5, amp=6, sweep=0.5, sb=60, seed=21, soft=True) +
  [fr([(16, 52), (12, 70), (16, 94, 1), (22, 74), (22, 52)]), fr([(84, 52), (88, 70), (84, 94, 1), (78, 74), (78, 52)])] + nose_line(88),
  dome('side', top=0, w=44, cy=42, n=5, amp=6, sweep=0.5, nape=84, fr=40, seed=21, soft=True) + [fr([(56, 56), (62, 76), (58, 96, 1), (52, 76)])],
  dome('back', top=0, w=44, cy=42, n=5, amp=6, sweep=0.5, nape=86, seed=21, soft=True))

# Eddy "Yellow" Pentaris: portero con una máscara blanca de héroe que le tapa media cara, con dos ojos naranjas y amarillos
# en llama; un mechón rubio de punta asoma por arriba y el pañuelo blanco se ata por detrás
MW, MO, MY = _c('#f4f2ee'), _c('#ec9a2a'), _c('#f6e070')
C('eddy-yellow-s-pentaris', 'normal', pal('#f2dc84', '#f6d6b0', '#1e1e1e', shade='#d8b85a'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=96, hairline=False, face_front=face(w=4, chin=104)),
  [L(outline([(30, 12), (52, -6), (74, 0, 1), (60, 8), (70, 14)]), 'mid'),
   L(outline([(14, 70), (12, 40), (24, 18), (50, 10), (76, 18), (88, 40), (86, 70), (70, 86), (50, 84), (30, 86)]), MW, 'f'),
   L(blob([(24, 62), (34, 56), (46, 70), (40, 84), (28, 80)], 5), MO, 'f', False), L(blob([(76, 62), (66, 56), (54, 70), (60, 84), (72, 80)], 5), MO, 'f', False),
   L(blob([(29, 68), (36, 64), (42, 72), (36, 80)], 5), MY, 'f', False), L(blob([(71, 68), (64, 64), (58, 72), (64, 80)], 5), MY, 'f', False)],
  [L(outline([(40, 8), (60, -6), (78, 0, 1), (64, 10)]), 'mid'),
   L(outline([(86, 72), (90, 40), (78, 16), (50, 8), (24, 14), (8, 34), (6, 60), (22, 72), (50, 80), (72, 84)]), MW, 'f'),
   L(blob([(74, 62), (84, 58), (90, 70), (82, 82)], 5), MO, 'f', False),
   L(outline([(12, 60), (-4, 72, 1), (0, 56), (-6, 50, 1), (8, 50)]), MW, 'f')],
  [L(outline([(30, 12), (52, -6), (74, 0, 1), (60, 8), (70, 14)]), 'mid'),
   L(outline([(12, 74), (10, 40), (24, 16), (50, 8), (76, 16), (90, 40), (88, 74), (50, 82)]), MW, 'f'),
   L(outline([(44, 62), (34, 84, 1), (48, 70), (52, 70), (66, 84, 1), (56, 62)]), MW, 'f')])

# Edward Baron: adulto con una melena castaño dorada ondulada hasta los hombros y una coronita roja y dorada encima;
# ojos caídos de sueño, nariz naranja enorme y un bigote negro rizado
CRR, CRG = _c('#c8282a'), _c('#f0c040')
C('edward-baron', 'delgado', pal('#c8962e', '#f4c290', '#2a1e1e', shade='#9a6e1e'),
  F(eyes='closed', brows=True, mouth='smile', mouth_y=100, eye_y=76, hairline=[(14, 64), (24, 42), (40, 34), (50, 40), (60, 34), (76, 42), (86, 64)],
    face_front=face(chin=110), nose=(50, 88, 4)),
  dome('front', top=6, w=46, cy=48, long=104, flare=8, soft=True) +
  [L(outline([(36, 10), (36, -2), (64, -2), (64, 10)]), CRR, 'f'), L(outline([(34, 10), (66, 10), (66, 14), (34, 14)]), CRG, 'f'),
   L(ell(50, -6, 4, 4), CRG, 'f'),
   L([(30, 74), (42, 74)], OUTC, 'f', False, False, 2.0), L([(58, 74), (70, 74)], OUTC, 'f', False, False, 2.0),
   L(ell(50, 88, 6, 5), _c('#ee8a4a'), 'f'),
   L(blob([(50, 94), (60, 92), (70, 96), (74, 90, 1), (68, 100), (50, 98), (32, 100), (26, 90, 1), (30, 96), (40, 92)], 4), BLACK, 'f', False)],
  dome('side', top=6, w=46, cy=48, long=102, flare=8, fr=52, soft=True) +
  [L(outline([(44, 6), (44, -6), (70, -6), (70, 6)]), CRR, 'f'), L(outline([(42, 6), (72, 6), (72, 10), (42, 10)]), CRG, 'f'),
   L(ell(90, 88, 5, 5), _c('#ee8a4a'), 'f'), L(blob([(82, 96), (92, 94), (94, 100), (84, 100)], 4), BLACK, 'f', False)],
  dome('back', top=6, w=46, cy=48, long=104, flare=8, ends=4, soft=True) +
  [L(outline([(36, 10), (36, -2), (64, -2), (64, 10)]), CRR, 'f'), L(outline([(34, 10), (66, 10), (66, 14), (34, 14)]), CRG, 'f')])

# Egon Omercer: portero con un casco azul que le tapa toda la cabeza, con unos cordones blancos en cruz por encima y
# dos gafas redondas blancas de cristal oscuro; solo se le ve la barbilla
HB = _c('#2e78c8')
C('egon-omercer', 'normal', pal('#2e78c8', '#f2b886', '#1e1e1e', shade='#1e5aa0'),
  F(eyes='none', brows=False, mouth='none', hairline=False),
  [L(outline([(12, 80), (8, 44), (20, 16), (50, 4), (80, 16), (92, 44), (88, 80), (76, 84), (70, 96), (62, 84), (38, 84), (30, 96), (24, 84)]), HB),
   L(outline([(60, 8), (80, 18), (92, 44), (88, 78), (80, 56)]), 'shade', 'b', False)] +
  [L([(46, 12 + i * 10), (54, 18 + i * 10)], WHITE, 'f', False, False, 1.6) for i in range(3)] +
  [L([(54, 12 + i * 10), (46, 18 + i * 10)], WHITE, 'f', False, False, 1.6) for i in range(3)] +
  round_glasses('front', WHITE, 74, 13, 7, _c('#3a1e1e'), 3.0) + [L(quad((40, 96), (50, 100), (60, 96)), OUTC, 'f', False, False, 1.2)],
  [L(outline([(80, 84), (90, 50), (82, 18), (56, 4), (28, 8), (10, 26), (4, 54), (8, 80), (28, 90), (52, 86), (66, 92)]), HB),
   L(outline([(6, 50), (40, 56), (50, 84), (26, 88), (8, 78)]), 'shade', 'b', False)] + round_glasses('side', WHITE, 74, r=7, lens=_c('#3a1e1e'), w=3.0),
  [L(outline([(12, 84), (8, 44), (20, 16), (50, 4), (80, 16), (92, 44), (88, 84), (50, 90)]), HB)] +
  [L([(46, 12 + i * 10), (54, 18 + i * 10)], WHITE, 'f', False, False, 1.6) for i in range(3)] +
  [L([(54, 12 + i * 10), (46, 18 + i * 10)], WHITE, 'f', False, False, 1.6) for i in range(3)])

# Egon Timing: pelo verde abierto hacia los lados en dos alas planas, con dos mechones largos por delante de las orejas;
# ojos redondos enormes de susto y los dos dientes de delante fuera
C('egon-timing', 'normal', pal('#4e7a2e', '#f2c894', '#1e1e1e', shade='#34581c'),
  F(eyes='round', brows=False, mouth='buck', mouth_y=96, eye_sep=15, hairline=[(14, 58), (22, 46), (34, 52), (44, 44), (54, 52), (66, 44), (78, 52), (86, 58)],
    face_front=face(chin=106)),
  [L(outline([(16, 58), (-8, 46, 1), (12, 34), (24, 14), (50, 8), (76, 14), (88, 34), (108, 46, 1), (84, 58), (80, 48), (20, 48)])),
   L(outline([(58, 10), (78, 16), (88, 36), (104, 46), (84, 56), (76, 34)]), 'shade', 'b', False),
   fr([(14, 54), (12, 76), (16, 94, 1), (22, 74), (22, 54)]), fr([(86, 54), (88, 76), (84, 94, 1), (78, 74), (78, 54)])],
  [L(outline([(72, 50), (84, 44), (88, 30), (74, 12), (50, 6), (24, 12), (8, 28), (-8, 46, 1), (10, 52), (26, 62), (44, 62), (56, 52)])),
   fr([(58, 54), (62, 76), (58, 96, 1), (52, 76)])],
  [L(outline([(14, 66), (-8, 50, 1), (10, 36), (24, 14), (50, 8), (76, 14), (90, 36), (108, 50, 1), (86, 66), (50, 74)]))])

# Elata Mighty: chica con una mata roja salmón enorme en forma de corazón por arriba y dos rulos gordos a los lados de la
# barbilla; ojos verde agua afilados y sonrisa de lista
C('elata-mighty', 'chica', pal('#de6a52', '#f4c898', '#2e8a80', shade='#b24a38', deep='#8a3426'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=[(14, 62), (22, 50), (36, 46), (50, 54), (64, 46), (78, 50), (86, 62)]),
  [L(outline([(16, 76), (6, 52), (2, 20), (20, -4), (40, -6), (50, 8), (60, -6), (80, -4), (98, 20), (94, 52), (84, 76), (80, 54), (20, 54)])),
   L(outline([(54, 4), (62, -4), (80, -2), (96, 22), (92, 50), (84, 70), (78, 40)]), 'shade', 'b', False),
   strand([(50, 10), (50, 40)], 'deep', 'b', 1.2),
   L(ell(14, 92, 8, 8), 'mid', 'f'), L(ell(86, 92, 8, 8), 'mid', 'f'),
   fr([(12, 60), (10, 84), (18, 88), (20, 64)]), fr([(88, 60), (90, 84), (82, 88), (80, 64)])],
  [L(outline([(70, 50), (86, 44), (98, 24), (84, -2), (60, -8), (34, -2), (10, 14), (2, 40), (6, 62), (20, 72), (40, 68), (56, 56)])),
   L(ell(50, 92, 8, 8), 'mid', 'f'), fr([(46, 60), (44, 84), (54, 86), (54, 62)])],
  [L(outline([(14, 78), (4, 52), (2, 20), (20, -4), (40, -6), (50, 8), (60, -6), (80, -4), (98, 20), (96, 52), (86, 78), (50, 84)])),
   L(ell(14, 92, 8, 8), 'mid', 'f'), L(ell(86, 92, 8, 8), 'mid', 'f')])

# Elegance Stuckon: chica de pelo beis con dos moños redondos arriba y dos coletas largas lisas que le caen hasta el
# pecho; ojos grandes morados y sonrisa
C('elegance-stuckon', 'chica', pal('#bca48c', '#f6cca4', '#7a3a6a', shade='#9a8270', deep='#7e6654'),
  F(eyes='big', mouth='smile', mouth_y=94, hairline=[(14, 60), (22, 44), (36, 36), (50, 34), (64, 36), (78, 44), (86, 60)]),
  dome('front', top=6, w=44, cy=46, sb=62, shade=False) +
  [L(ell(18, 12, 10, 10), 'mid'), L(ell(82, 12, 10, 10), 'mid'), L(ell(18, 12, 5, 5), 'shade', 'b', False), L(ell(82, 12, 5, 5), 'shade', 'b', False),
   L(outline([(10, 50), (4, 80), (8, 116), (16, 120, 1), (20, 84), (18, 56)]), 'mid', 'f'),
   L(outline([(90, 50), (96, 80), (92, 116), (84, 120, 1), (80, 84), (82, 56)]), 'mid', 'f')] +
  [strand([(50, 8), (50, 34)], 'deep', 'b', 1.0), strand([(36, 12), (30, 36)], 'deep', 'b', 0.8), strand([(64, 12), (70, 36)], 'deep', 'b', 0.8)],
  dome('side', top=6, w=44, cy=46, nape=82, fr=42, shade=False) +
  [L(ell(40, 6, 10, 10), 'mid'), L(outline([(26, 52), (20, 84), (24, 116), (32, 118, 1), (34, 84), (34, 56)]), 'mid', 'f')],
  dome('back', top=6, w=44, cy=46, nape=84, shade=False) +
  [L(ell(18, 12, 10, 10), 'mid'), L(ell(82, 12, 10, 10), 'mid'),
   L(outline([(12, 50), (6, 80), (10, 116), (18, 120, 1), (22, 84), (20, 56)]), 'mid', 'f'),
   L(outline([(88, 50), (94, 80), (90, 116), (82, 120, 1), (78, 84), (80, 56)]), 'mid', 'f')])

# Elias Lens: pelo morado en un tupé alto echado hacia un lado; gafas redondas amarillas, sonrisa enorme de dientes,
# nariz chata y barbilla larga
C('elias-lens', 'delgado', pal('#7a4ab4', '#f6caa4', '#1e1e1e', shade='#563494'),
  F(eyes='dot', brows=False, mouth='none', hairline=[(16, 62), (22, 48), (40, 44), (60, 44), (78, 48), (84, 62)], face_front=face(chin=112),
    nose=(50, 88, 2.6)),
  [L(outline([(16, 60), (12, 34), (22, 10), (46, 0), (78, 2), (104, 16, 1), (84, 24), (88, 40), (84, 62), (80, 54), (20, 54)])),
   L(outline([(56, 2), (78, 4), (100, 16), (84, 22), (86, 40), (80, 30), (64, 16)]), 'shade', 'b', False)] +
  round_glasses('front', _c('#c8b820'), 76, 14, 8, _c('#e8e080'), 2.4) + teeth_grin(98, 14, 6),
  [L(outline([(72, 46), (84, 40), (88, 26), (104, 14, 1), (78, 2), (50, -2), (24, 4), (8, 22), (4, 50), (20, 62), (44, 60), (58, 48)]))] +
  round_glasses('side', _c('#c8b820'), 76, r=8, lens=_c('#e8e080'), w=2.4),
  [L(outline([(14, 70), (10, 34), (22, 10), (46, 0), (78, 2), (100, 16, 1), (86, 26), (90, 40), (86, 70), (50, 78)]))])


# -------------------------------------------------------------------------------------------------------------- 17-24

def ball(cx, cy, r=10):
    """Balón de fútbol blanco con los pentágonos negros."""
    out = [L(ell(cx, cy, r, r), WHITE, 'f')]
    out.append(L(ell(cx, cy, r * 0.32, r * 0.32), BLACK, 'f', False))
    for dx, dy in ((-0.7, -0.45), (0.7, -0.45), (0, 0.8), (-0.75, 0.6), (0.75, 0.6)):
        out.append(L(ell(cx + dx * r * 0.85, cy + dy * r * 0.85, r * 0.2, r * 0.2), BLACK, 'f', False))
    return out


# Elinor Maven: pelo verde oliva con dos coletas cortas rizadas hacia fuera a los lados y una cinta naranja; ojos azules
# afilados y boca seria
OR = _c('#eea02a')
C('elinor-maven', 'chica', pal('#6e6a1e', '#ecac72', '#3e7aa0', shade='#4e4a12'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(14, 64), (22, 46), (34, 40), (44, 52), (50, 38), (60, 50), (70, 40), (80, 46), (86, 64)]),
  dome('front', top=6, w=44, cy=46, sb=66, soft=True) +
  [L(outline([(10, 34), (-6, 44), (-8, 66), (4, 76, 1), (6, 60), (14, 54)]), 'mid'), L(outline([(90, 34), (106, 44), (108, 66), (96, 76, 1), (94, 60), (86, 54)]), 'mid'),
   L(quad((16, 30), (50, 4), (84, 30)), OR, 'f', False, False, 4.0)],
  dome('side', top=6, w=44, cy=46, nape=84, fr=48, soft=True) + [L(outline([(14, 34), (-4, 48), (-4, 70), (8, 78, 1), (10, 60), (18, 54)]), 'mid'),
                                                                L(quad((80, 26), (54, 0), (22, 10)), OR, 'f', False, False, 4.0)],
  dome('back', top=6, w=44, cy=46, nape=86, soft=True) +
  [L(outline([(10, 34), (-6, 44), (-8, 66), (4, 76, 1), (6, 60), (14, 54)]), 'mid'), L(outline([(90, 34), (106, 44), (108, 66), (96, 76, 1), (94, 60), (86, 54)]), 'mid')])

# Elsa Roamer: gorro de lana azul con la borla crema y una visera ancha crema con orejeras que caen a los lados; pelo
# rosa grisáceo corto por debajo, ojos verde azulado y cejas de pena
BE, CRM = _c('#4c6c9c'), _c('#f2e4c8')
C('elsa-roamer', 'chica', pal('#c8a8ae', '#f2bc8c', '#2e7a80', shade='#a08890'),
  F(eyes='normal', brows=True, mouth='frown', mouth_y=94, hairline=hl(6, 62, 48, 58, seed=24)),
  dome('front', top=10, w=44, cy=50, sb=72, shade=False) +
  [L(blob([(10, 40), (20, 6), (50, -6), (80, 6), (92, 40), (50, 30)], 6), BE, 'f'), L(ell(66, -8, 9, 8), CRM, 'f'),
   L(blob([(6, 44), (50, 26), (94, 44), (90, 56), (50, 44), (10, 56)], 6), CRM, 'f'),
   L(outline([(82, 48), (94, 52), (96, 84), (86, 88), (82, 60)]), CRM, 'f')],
  dome('side', top=10, w=44, cy=50, nape=84, fr=54, shade=False) +
  [L(blob([(8, 40), (20, 6), (50, -6), (78, 4), (92, 34), (50, 30)], 6), BE, 'f'), L(ell(56, -10, 9, 8), CRM, 'f'),
   L(blob([(2, 44), (50, 26), (96, 36), (92, 48), (50, 42), (8, 56)], 6), CRM, 'f'),
   L(outline([(36, 50), (52, 50), (54, 84), (40, 86)]), CRM, 'f')],
  dome('back', top=10, w=44, cy=50, nape=86, shade=False) +
  [L(blob([(10, 40), (20, 6), (50, -6), (80, 6), (92, 40), (50, 30)], 6), BE, 'f'), L(ell(34, -8, 9, 8), CRM, 'f'),
   L(blob([(6, 44), (50, 32), (94, 44), (90, 56), (50, 48), (10, 56)], 6), CRM, 'f'),
   L(outline([(18, 48), (6, 52), (4, 84), (14, 88), (18, 60)]), CRM, 'f')])

# Emma Barres: melena azul marino muy oscura, lisa y recta hasta los hombros, con flequillo recto; ojos entornados y
# cara de aburrida
C('emma-barres', 'chica', pal('#24384e', '#f8dcb4', '#2a2a30', shade='#162434'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=94, eye_y=76, hairline=[(14, 66), (16, 58), (30, 60), (50, 60), (70, 60), (84, 58), (86, 66)]),
  dome('front', top=2, w=46, cy=46, long=104, flare=4) + [fr([(16, 36), (30, 18), (50, 14), (70, 18), (84, 36), (84, 60), (16, 60)])],
  dome('side', top=2, w=46, cy=46, long=102, flare=4, fr=60),
  dome('back', top=2, w=46, cy=46, long=104, flare=4, ends=3))

# Erhardt Knead: casco de pelo gris lila liso y recto, con el flequillo tapándole los ojos y unas gafitas redondas
# blancas encima; cara larga y pálida, barbilla grande
C('erhardt-knead', 'delgado', pal('#b2b2c6', '#f8e4ba', '#1e1e1e', shade='#8a8aa2'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=96, hairline=False, face_front=face(chin=112)),
  bowl('front', 0, 94) + [fr([(14, 40), (24, 14), (50, 4), (76, 14), (86, 40), (86, 70), (14, 70)])] +
  [L(ell(38, 66, 5, 3.6), WHITE, 'f', True), L(ell(62, 66, 5, 3.6), WHITE, 'f', True), L([(43, 66), (57, 66)], OUTC, 'f', False, False, 1.0),
   L([(40, 104), (60, 104)], OUTC, 'f', False, False, 1.0)],
  bowl('side', 0, 96) + [fr([(62, 16), (84, 30), (90, 70), (76, 72), (70, 52)]), L(ell(86, 66, 3, 3.6), WHITE, 'f', True)],
  bowl('back', 0, 96))

# Eric Motter: portero gordo y calvo de piel tostada con un brote verde de brócoli en lo alto; ojitos enfadados, boca de
# pato naranja y coloretes
C('eric-motter', 'corpulento', pal('#4e7a2a', '#dca262', '#1e1e1e', skin_d='#b8824a', shade='#34581c'),
  F(eyes='dot', brows='angry', mouth='none', eye_y=74, eye_sep=11, hairline=False, face_front=face(w=8, chin=112, jaw=10)),
  skull('front') + [L(blob([(40, 10), (38, -2), (46, -8), (54, -6), (62, -2), (60, 10)], 5), 'mid', 'f'),
                    L(blob([(42, 86), (50, 82), (58, 86), (56, 92), (44, 92)], 4), _c('#e89a3a'), 'f'),
                    L(ell(28, 86, 5, 3.6), _c('#ec8a7a'), 'f', False), L(ell(72, 86, 5, 3.6), _c('#ec8a7a'), 'f', False)],
  skull('side') + [L(blob([(42, 6), (40, -6), (48, -12), (58, -10), (64, -4), (62, 6)], 5), 'mid', 'f'),
                   L(blob([(84, 86), (94, 84), (96, 90), (86, 92)], 4), _c('#e89a3a'), 'f')],
  skull('back') + [L(blob([(40, 10), (38, -2), (46, -8), (54, -6), (62, -2), (60, 10)], 5), 'mid', 'f')])

# Erica Hogland: capucha rosa de cerdito con dos orejas y el morro marrón sobre la frente; pelo morado corto que sale
# rizado hacia fuera por debajo, ojos marrones grandes, pecas y sonrisa
PK, SN = _c('#f2c0b4'), _c('#8a3e26')
C('erica-hogland', 'chica', pal('#5a3a7e', '#f4c290', '#8a4a26', shade='#3e2660'),
  F(eyes='big', mouth='smile', mouth_y=94, hairline=False),
  [L(outline([(16, 76), (2, 92, 1), (14, 70)]), 'mid', 'b'), L(outline([(84, 76), (98, 92, 1), (86, 70)]), 'mid', 'b'),
   L(outline([(12, 74), (8, 40), (20, 14), (50, 4), (80, 14), (92, 40), (88, 74), (80, 58), (20, 58)]), PK, 'f'),
   L(outline([(16, 22), (-2, 4, 1), (24, 12)]), PK, 'f'), L(outline([(84, 22), (102, 4, 1), (76, 12)]), PK, 'f'),
   L(blob([(24, 34), (50, 26), (76, 34), (74, 52), (50, 56), (26, 52)], 6), _c('#e8a090'), 'f'),
   L(ell(38, 42, 7, 8), SN, 'f'), L(ell(62, 42, 7, 8), SN, 'f')] +
  [L(ell(36 + dx, 88, 0.9, 0.9), _c('#c87a4a'), 'f', False) for dx in (-6, 0, 6)] + [L(ell(64 + dx, 88, 0.9, 0.9), _c('#c87a4a'), 'f', False) for dx in (-6, 0, 6)],
  [L(outline([(36, 76), (30, 92, 1), (46, 74)]), 'mid', 'b'),
   L(outline([(84, 60), (92, 34), (80, 12), (52, 2), (24, 8), (6, 30), (4, 62), (18, 78), (40, 78), (56, 62), (70, 54)]), PK, 'f'),
   L(outline([(38, 12), (26, -6, 1), (50, 6)]), PK, 'f'), L(blob([(78, 30), (96, 30), (98, 52), (80, 52)], 5), SN, 'f')],
  [L(outline([(16, 80), (2, 92, 1), (14, 70)]), 'mid', 'b'), L(outline([(84, 80), (98, 92, 1), (86, 70)]), 'mid', 'b'),
   L(outline([(12, 80), (8, 40), (20, 14), (50, 4), (80, 14), (92, 40), (88, 80), (50, 86)]), PK, 'f'),
   L(outline([(16, 22), (-2, 4, 1), (24, 12)]), PK, 'f'), L(outline([(84, 22), (102, 4, 1), (76, 12)]), PK, 'f')])

# Esther Egerer: pelo naranja con las puntas onduladas hacia fuera a los lados y dos trenzas bajas atadas con cinta azul;
# ojos verdes redondos y boca abierta de sorpresa
BW = _c('#8ab8d8')
C('esther-egerer', 'chica', pal('#ea782a', '#f6d0aa', '#2a8a4a', shade='#c0561a'),
  F(eyes='big', mouth='none', mouth_y=96, hairline=hl(5, 62, 44, 54, lean=3, seed=28)),
  dome('front', top=2, w=44, cy=44, n=4, amp=5, sweep=0.4, sb=64, soft=True, seed=27) +
  [L(outline([(10, 50), (-8, 66, 1), (8, 64), (12, 76)]), 'mid'), L(outline([(90, 50), (108, 62, 1), (92, 64), (88, 76)]), 'mid'),
   L(outline([(20, 80), (16, 100), (22, 122, 1), (30, 100), (28, 80)]), 'mid', 'f'), L(outline([(80, 80), (84, 100), (78, 122, 1), (70, 100), (72, 80)]), 'mid', 'f'),
   L(blob([(16, 84), (30, 84), (30, 96), (16, 96)], 3), BW, 'f'), L(blob([(70, 84), (84, 84), (84, 96), (70, 96)], 3), BW, 'f'),
   L(ell(50, 96, 3.4, 4), (120, 40, 40, 255), 'f', True)],
  dome('side', top=2, w=44, cy=44, n=4, amp=5, sweep=0.4, nape=80, fr=46, soft=True, seed=27) +
  [L(outline([(36, 78), (34, 100), (40, 122, 1), (48, 100), (46, 78)]), 'mid', 'f'), L(blob([(34, 84), (48, 84), (48, 96), (34, 96)], 3), BW, 'f')],
  dome('back', top=2, w=44, cy=44, n=4, amp=5, sweep=0.4, nape=82, soft=True, seed=27) +
  [L(outline([(26, 78), (20, 100), (26, 122, 1), (34, 100), (34, 78)]), 'mid', 'f'), L(outline([(74, 78), (80, 100), (74, 122, 1), (66, 100), (66, 78)]), 'mid', 'f'),
   L(blob([(20, 86), (34, 86), (34, 96), (20, 96)], 3), BW, 'f'), L(blob([(66, 86), (80, 86), (80, 96), (66, 96)], 3), BW, 'f')])

# Ethan Swallow: pelo amarillo en dos rizos enormes de cuernos de carnero a los lados, con un balón encima de la
# cabeza; ojos con dos manchas negras alrededor, espirales en las mejillas, nariz de triángulo y boca ondulada
YH, SPI = _c('#d8c03e'), _c('#c89a4e')
C('ethan-swallow', 'normal', pal('#d8c03e', '#f4c290', '#1e1e1e', shade='#a89020'),
  F(eyes='none', brows=True, mouth='none', hairline=[(14, 58), (20, 44), (36, 40), (50, 44), (64, 40), (80, 44), (86, 58)]),
  dome('front', top=10, w=42, cy=48, sb=58, shade=False) +
  [L(ell(12, 38, 18, 16), YH, 'f'), L(ell(88, 38, 18, 16), YH, 'f'),
   L(ell(12, 38, 10, 8) + [ell(12, 38, 10, 8)[0]], SPI, 'f', False, False, 1.4), L(ell(88, 38, 10, 8) + [ell(88, 38, 10, 8)[0]], SPI, 'f', False, False, 1.4)] +
  ball(50, 0, 12) +
  [L(ell(36, 76, 7, 6.5), BLACK, 'f', False), L(ell(64, 76, 7, 6.5), BLACK, 'f', False), L(ell(36, 76, 3.6, 3.6), WHITE, 'f', False), L(ell(64, 76, 3.6, 3.6), WHITE, 'f', False),
   L(ell(36, 76, 1.8, 1.8), BLACK, 'f', False), L(ell(64, 76, 1.8, 1.8), BLACK, 'f', False),
   L([(50, 82), (54, 88), (46, 88)], _c('#e08a5a'), 'f', False, True),
   L(ell(31, 89, 4, 4) + [ell(31, 89, 4, 4)[0]], SPI, 'f', False, False, 1.2), L(ell(69, 89, 4, 4) + [ell(69, 89, 4, 4)[0]], SPI, 'f', False, False, 1.2),
   L([(42, 96), (46, 94), (50, 96), (54, 94), (58, 96)], OUTC, 'f', False, False, 1.4)],
  dome('side', top=10, w=42, cy=48, nape=80, fr=46, shade=False) +
  [L(ell(46, 30, 16, 14), YH, 'f'), L(ell(46, 30, 9, 7) + [ell(46, 30, 9, 7)[0]], SPI, 'f', False, False, 1.4)] + ball(54, -2, 12) +
  [L(ell(80, 76, 5, 6.5), BLACK, 'f', False), L(ell(81, 76, 2.4, 3), WHITE, 'f', False)],
  dome('back', top=10, w=42, cy=48, nape=82, shade=False) + [L(ell(14, 34, 16, 14), YH, 'f'), L(ell(86, 34, 16, 14), YH, 'f')] + ball(50, 0, 12))


# -------------------------------------------------------------------------------------------------------------- 25-32

# Farrah Fairway: pelo castaño oliva en pinchos alborotados hacia arriba, con mechones largos que le caen por los lados de
# la cara; ojos lilas afilados y sonrisa pícara
C('farrah-fairway', 'chica', pal('#8a7a2c', '#f6c898', '#7a6aa0', shade='#625618'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=hl(6, 60, 44, 54, jit=3, seed=31)),
  dome('front', top=0, w=44, cy=44, n=9, amp=11, sb=62, seed=32) +
  [fr([(14, 52), (8, 74), (12, 96, 1), (20, 74), (22, 54)]), fr([(86, 52), (92, 74), (88, 96, 1), (80, 74), (78, 54)])],
  dome('side', top=0, w=44, cy=44, n=9, amp=11, nape=84, fr=48, seed=32) + [fr([(56, 54), (60, 76), (56, 96, 1), (50, 76)])],
  dome('back', top=0, w=44, cy=44, n=9, amp=11, nape=86, seed=32))

# Farris Stickman: piel morena y pelo gris morado en un cono de punta con rayas oscuras; orejas grandes, gafas redondas
# enormes de cristal verde con montura beis, nariz de pico y dientes apretados
CONE, CONE_D = _c('#6c6a7e'), _c('#4a4858')
C('farris-stickman', 'normal', pal('#6c6a7e', '#a8784c', '#1e1e1e', skin_d='#86593a', shade='#4a4858'),
  F(eyes='none', brows=False, mouth='none', hairline=False, big_ears=3),
  [L(outline([(18, 56), (24, 28), (50, -10, 1), (76, 28), (82, 56), (50, 48)]), CONE)] +
  [L(quad((26 + i * 3, 42 - i * 12), (50, 34 - i * 12), (74 - i * 3, 42 - i * 12)), CONE_D, 'f', False, False, 2.4) for i in range(3)] +
  round_glasses('front', _c('#d8c8a0'), 74, 13, 8, _c('#4a8a2a'), 3.4) +
  [L([(50, 80), (55, 88), (50, 91), (45, 88)], 'skin_d', 'f', False, True),
   L([(40, 93), (60, 93), (60, 98), (40, 98)], WHITE, 'f', False, True), L([(40, 95.5), (60, 95.5)], OUTC, 'f', False, False, 0.8)],
  [L(outline([(80, 54), (82, 30), (56, -10, 1), (24, 20), (10, 44), (14, 64), (34, 66), (56, 58)]), CONE)] +
  [L(quad((24 + i * 6, 40 - i * 12), (50, 30 - i * 12), (80 - i * 4, 36 - i * 12)), CONE_D, 'f', False, False, 2.4) for i in range(3)] +
  round_glasses('side', _c('#d8c8a0'), 74, r=8, lens=_c('#4a8a2a'), w=3.4) + [L([(86, 80), (96, 90), (86, 92)], 'skin_d', 'f', False, True)],
  [L(outline([(14, 70), (18, 34), (50, -10, 1), (82, 34), (86, 70), (50, 76)]), CONE)] +
  [L(quad((24 + i * 3, 44 - i * 12), (50, 36 - i * 12), (76 - i * 3, 44 - i * 12)), CONE_D, 'f', False, False, 2.4) for i in range(3)])

# Fawn Blossom: media melena lisa verde lima con un moño arriba y dos horquillas naranjas en cruz; ojos azules y sonrisa
C('fawn-blossom', 'chica', pal('#c8d840', '#f8d0a8', '#3a5a9a', shade='#a0b028'),
  F(eyes='big', mouth='smile', mouth_y=94, hairline=[(14, 64), (18, 46), (32, 34), (50, 30), (68, 34), (82, 46), (86, 64)]),
  dome('front', top=6, w=44, cy=46, long=96, flare=2) + [L(ell(50, 6, 11, 9), 'mid'), L(ell(50, 6, 5, 4), 'shade', 'b', False),
                                                          L([(76, 46), (82, 54)], OR, 'f', False, False, 1.8), L([(82, 46), (76, 54)], OR, 'f', False, False, 1.8)],
  dome('side', top=6, w=44, cy=46, long=94, flare=2, fr=40) + [L(ell(46, 2, 11, 9), 'mid')],
  dome('back', top=6, w=44, cy=46, long=96, flare=2, ends=3) + [L(ell(50, 6, 11, 9), 'mid')])

# Fen Skates: melena roja enorme echada a un lado que le cae por detrás en una ola larga; ojos negros grandes de punta y
# boca pequeña seria
C('fen-skates', 'chica', pal('#d8604c', '#f6cca4', '#1e1e1e', shade='#ae4232', deep='#8a3022'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=94, hairline=[(14, 62), (18, 44), (30, 36), (46, 44), (60, 34), (78, 40), (86, 62)]),
  [L(outline([(16, 66), (6, 40), (14, 12), (40, -4), (70, -2), (94, 14), (100, 44), (108, 84), (110, 104, 1), (92, 92), (88, 66), (82, 50), (20, 50)])),
   L(outline([(62, 0), (90, 14), (100, 48), (106, 92), (90, 84), (86, 54), (76, 28)]), 'shade', 'b', False),
   strand([(30, 10), (24, 40)], 'deep', 'b', 1.0), strand([(50, 4), (60, 30)], 'deep', 'b', 1.0)],
  [L(outline([(70, 52), (86, 44), (90, 22), (70, 2), (40, -6), (14, 6), (2, 36), (-4, 70), (-6, 104, 1), (12, 88), (26, 82), (40, 70), (54, 58)]))],
  [L(outline([(14, 80), (4, 44), (14, 12), (40, -4), (70, -2), (94, 14), (102, 46), (108, 84), (110, 106, 1), (90, 94), (70, 92), (50, 86), (30, 84)])),
   L(outline([(62, 0), (92, 14), (102, 50), (106, 96), (86, 90), (72, 40)]), 'shade', 'b', False)])

# Fern Mycota: un gorro o pelo rojo oscuro en forma de seta, a rayas, que le cubre hasta las cejas; piel pálida, ojos
# amarillos afilados con sombra morada y sonrisa de lado
MUSH = _c('#a42a2a')
C('fern-mycota', 'chica', pal('#a42a2a', '#f8e2b4', '#d8b020', shade='#7a1c1c'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=94, hairline=False),
  [L(blob([(-4, 50), (6, 20), (30, 4), (60, 2), (88, 14), (104, 40), (100, 54), (50, 50)], 7), MUSH),
   L(blob([(58, 6), (88, 16), (104, 40), (98, 52), (80, 46)], 6), 'shade', 'b', False)] +
  [L(quad((14 + i * 14, 50), (16 + i * 14, 24), (24 + i * 13, 8)), 'shade', 'f', False, False, 1.4) for i in range(6)] +
  [L(blob([(26, 66), (42, 64), (44, 70), (28, 72)], 4), _c('#b48ad8'), 'f', False), L(blob([(74, 66), (58, 64), (56, 70), (72, 72)], 4), _c('#b48ad8'), 'f', False)],
  [L(blob([(-2, 54), (4, 22), (30, 2), (64, 0), (92, 16), (106, 44), (96, 54), (50, 50)], 7), MUSH),
   L(blob([(72, 66), (84, 64), (86, 70), (74, 72)], 4), _c('#b48ad8'), 'f', False)],
  [L(blob([(-4, 50), (6, 20), (30, 4), (60, 2), (88, 14), (104, 40), (100, 54), (50, 58)], 7), MUSH)] +
  [L(quad((14 + i * 14, 54), (16 + i * 14, 24), (24 + i * 13, 8)), 'shade', 'f', False, False, 1.4) for i in range(6)])

# Finn Gold-Geld: un casco dorado de buzo que le tapa toda la cabeza, con una corona encima y una ventana redonda oscura
# cruzada por una cruz de oro con una gema verde en medio
GOLD, GOLD_D, WIN = _c('#eaa422'), _c('#c07a14'), _c('#2a1e3a')
C('finn-gold-geld', 'normal', pal('#eaa422', '#f2c498', '#1e1e1e', shade='#c07a14'),
  F(eyes='none', brows=False, mouth='none', hairline=False, no_head=True),
  [L(ell(50, 58, 44, 46), GOLD), L(blob([(60, 18), (88, 40), (92, 72), (76, 96), (70, 60)], 6), GOLD_D, 'f', False),
   L(outline([(0, 50), (8, 44), (8, 74), (0, 70)]), GOLD, 'f'), L(outline([(100, 50), (92, 44), (92, 74), (100, 70)]), GOLD, 'f'),
   L(outline([(30, 14), (26, -6, 1), (38, 4), (50, -10, 1), (62, 4), (74, -6, 1), (70, 14)]), _c('#f2d050'), 'f'),
   L(ell(50, 62, 20, 20), _c('#f2d050'), 'f'), L(ell(50, 62, 16, 16), WIN, 'f', False),
   L([(50, 46), (50, 78)], _c('#f2d050'), 'f', False, False, 3.0), L([(34, 62), (66, 62)], _c('#f2d050'), 'f', False, False, 3.0),
   L(ell(50, 62, 3.6, 3.6), _c('#30b080'), 'f'), L(outline([(32, 100), (68, 100), (64, 108), (36, 108)]), GOLD, 'f')],
  [L(ell(48, 58, 44, 46), GOLD), L(outline([(30, 14), (28, -6, 1), (44, 4), (56, -10, 1), (66, 6)]), _c('#f2d050'), 'f'),
   L(ell(84, 62, 10, 18), _c('#f2d050'), 'f'), L(ell(86, 62, 6, 14), WIN, 'f', False), L(outline([(30, 100), (66, 100), (62, 108), (34, 108)]), GOLD, 'f')],
  [L(ell(50, 58, 44, 46), GOLD), L(blob([(60, 18), (88, 40), (92, 72), (76, 96), (70, 60)], 6), GOLD_D, 'f', False),
   L(outline([(30, 14), (26, -6, 1), (38, 4), (50, -10, 1), (62, 4), (74, -6, 1), (70, 14)]), _c('#f2d050'), 'f'),
   L(outline([(32, 100), (68, 100), (64, 108), (36, 108)]), GOLD, 'f')])

# Flip Sliden: pelo celeste pálido en pinchos largos echados hacia arriba y a un lado, con una cinta a rombos rojos y
# azules en la frente; ojos amarillos afilados, rayas azules pintadas en las mejillas y boca seria
HR, HBL = _c('#c8303a'), _c('#2a4a9a')
C('flip-sliden', 'normal', pal('#a8d8d2', '#ecb682', '#e0b020', shade='#7ab0aa'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, hairline=False),
  [L(outline([(14, 70), (10, 44), (6, 16, 1), (22, 22), (24, -10, 1), (38, 12), (52, -20, 1), (58, 6), (84, -12, 1), (78, 12), (106, 6, 1), (90, 28), (104, 40, 1),
              (88, 44), (88, 70), (82, 56), (18, 56)])),
   L(outline([(56, 4), (80, -6), (78, 14), (100, 10), (88, 28), (98, 40), (86, 44), (80, 30)]), 'shade', 'b', False),
   L(outline([(14, 60), (16, 44), (50, 40), (84, 44), (86, 60), (50, 58)]), HBL, 'f')] +
  [L([(20 + i * 12, 58 - (2 if i in (2, 3) else 0)), (26 + i * 12, 44), (32 + i * 12, 58 - (2 if i in (1, 2) else 0))], HR, 'f', False, True) for i in range(6)] +
  [mark([(22, 84), (32, 82)], HBL, w=2.0), mark([(24, 88), (34, 86)], HBL, w=2.0), mark([(78, 84), (68, 82)], HBL, w=2.0), mark([(76, 88), (66, 86)], HBL, w=2.0)],
  [L(outline([(70, 48), (86, 40), (104, 30, 1), (88, 20), (100, -4, 1), (74, 6), (70, -18, 1), (54, 4), (34, -12, 1), (30, 10), (6, 8, 1), (10, 30), (4, 54),
              (18, 66), (40, 62), (56, 52)])),
   L(outline([(4, 46), (50, 40), (88, 42), (88, 56), (50, 56), (6, 60)]), HBL, 'f'), mark([(78, 86), (88, 84)], HBL, w=2.0)],
  [L(outline([(14, 74), (10, 44), (6, 16, 1), (22, 22), (24, -10, 1), (38, 12), (52, -20, 1), (58, 6), (84, -12, 1), (78, 12), (106, 6, 1), (90, 28), (104, 40, 1),
              (90, 44), (88, 74), (50, 80)])),
   L(outline([(10, 60), (12, 44), (50, 40), (88, 44), (90, 60), (50, 58)]), HBL, 'f')] +
  [L([(16 + i * 12, 58), (22 + i * 12, 44), (28 + i * 12, 58)], HR, 'f', False, True) for i in range(6)])

# Flo Nighting: boina celeste y pelo verde oscuro con dos trenzas que le caen por delante de los hombros; ojos marrones
# redondos enormes, coloretes y sonrisa
BER = _c('#a6c4d6')
C('flo-nighting', 'chica', pal('#2a6a3a', '#f2c08e', '#6a3a1e', shade='#1c4a28'),
  F(eyes='big', mouth='smile', mouth_y=94, hairline=hl(7, 60, 50, 58, seed=35)),
  dome('front', top=10, w=44, cy=50, sb=72, shade=False) +
  [L(blob([(4, 50), (8, 24), (30, 6), (60, 4), (88, 16), (98, 40), (92, 52), (50, 44)], 7), BER, 'f'), L(ell(52, 6, 3, 3), BER, 'f'),
   L(outline([(18, 74), (12, 92), (16, 112), (24, 116, 1), (26, 94), (24, 76)]), 'mid', 'f'),
   L(outline([(82, 74), (88, 92), (84, 112), (76, 116, 1), (74, 94), (76, 76)]), 'mid', 'f')] + blush(88, 24),
  dome('side', top=10, w=44, cy=50, nape=82, fr=52, shade=False) +
  [L(blob([(2, 54), (6, 24), (30, 4), (64, 2), (92, 18), (100, 40), (92, 52), (50, 44)], 7), BER, 'f'),
   L(outline([(52, 74), (48, 94), (52, 114), (60, 116, 1), (60, 94), (58, 76)]), 'mid', 'f')],
  dome('back', top=10, w=44, cy=50, nape=84, shade=False) +
  [L(blob([(4, 50), (8, 24), (30, 6), (60, 4), (88, 16), (98, 40), (92, 56), (50, 50)], 7), BER, 'f')])


# -------------------------------------------------------------------------------------------------------------- 33-40

def curls(cx, cy, r, n=8, a0=0.0):
    """Contorno de nube de rizos (bultos redondos alrededor de un centro)."""
    import math
    pts = []
    for i in range(n * 2):
        a = a0 + math.pi * 2 * i / (n * 2)
        k = 1.0 if i % 2 == 0 else 0.84
        pts.append((cx + r[0] * k * math.cos(a), cy + r[1] * k * math.sin(a)))
    return blob(pts, 6)


# Flora Summars: media melena rosa de rizos gordos y abultados; piel muy clara, ojos marrones grandes y sonrisa
C('flora-summars', 'chica', pal('#e86c86', '#fae6c4', '#7a3e1e', shade='#c04e68'),
  F(eyes='big', mouth='smile', mouth_y=94, hairline=[(14, 60), (22, 42), (36, 34), (50, 40), (64, 32), (80, 42), (86, 60)]),
  [L(curls(14, 64, (16, 22), 5, 0.3)), L(curls(86, 64, (16, 22), 5, 0.6)), L(curls(50, 30, (50, 34), 10)),
   L(curls(66, 22, (20, 14), 5, 0.4), 'shade', 'b', False)],
  [L(curls(26, 62, (24, 26), 6)), L(curls(46, 30, (46, 34), 9)), L(curls(70, 24, (18, 12), 5), 'mid', 'f')],
  [L(curls(16, 70, (18, 22), 5)), L(curls(84, 70, (18, 22), 5)), L(curls(50, 36, (50, 40), 10))])

# Florian Fauna: pelo verde muy oscuro en pinchos de punta hacia arriba y un pañuelo amarillo con manchas de leopardo que
# le tapa media cara y se anuda a un lado; ojos marrones fruncidos
LEO, SPOT = _c('#eed64a'), _c('#3a2a10')
C('florian-fauna', 'normal', pal('#28463a', '#c88a5a', '#7a3a10', shade='#162e24'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, hairline=False),
  [L(outline([(16, 62), (10, 40), (-2, 22, 1), (16, 20), (14, -6, 1), (32, 10), (40, -20, 1), (52, 6), (66, -12, 1), (68, 12), (92, 4, 1), (84, 28), (98, 40, 1),
              (86, 46), (84, 62), (80, 48), (20, 48)])),
   L(outline([(14, 50), (50, 40), (86, 50), (88, 86), (50, 90), (12, 86)]), LEO, 'f'),
   L(outline([(86, 72), (104, 66, 1), (96, 80), (106, 88, 1), (88, 84)]), LEO, 'f')] +
  [L(ell(x, y, 2.4, 2), SPOT, 'f', False) for x, y in ((24, 56), (42, 52), (60, 54), (78, 58), (20, 70), (50, 64), (80, 72), (30, 84), (70, 84), (56, 84))] +
  [L([(28, 72), (44, 75), (42, 81), (30, 79)], WHITE, 'f', False, True), L([(72, 72), (56, 75), (58, 81), (70, 79)], WHITE, 'f', False, True),
   L(ell(38, 77, 3, 3.4), _c('#7a3a10'), 'f', False), L(ell(62, 77, 3, 3.4), _c('#7a3a10'), 'f', False),
   L([(26, 68), (44, 73)], OUTC, 'f', False, False, 2.6), L([(74, 68), (56, 73)], OUTC, 'f', False, False, 2.6)],
  [L(outline([(70, 50), (84, 42), (98, 28, 1), (84, 22), (92, -2, 1), (70, 8), (64, -18, 1), (50, 4), (30, -14, 1), (26, 10), (4, 6, 1), (10, 30), (4, 54),
              (20, 64), (40, 60), (56, 52)])),
   L(outline([(50, 48), (88, 48), (90, 86), (60, 88), (50, 70)]), LEO, 'f'), L(outline([(52, 70), (36, 66, 1), (42, 78), (34, 88, 1), (52, 80)]), LEO, 'f')] +
  [L(ell(x, y, 2.4, 2), SPOT, 'f', False) for x, y in ((62, 56), (78, 60), (66, 74), (82, 80))],
  [L(outline([(14, 70), (8, 40), (-2, 22, 1), (16, 20), (14, -6, 1), (32, 10), (40, -20, 1), (52, 6), (66, -12, 1), (68, 12), (92, 4, 1), (84, 28), (100, 40, 1),
              (88, 46), (86, 70), (50, 78)])),
   L(outline([(12, 56), (50, 52), (88, 56), (88, 70), (50, 70), (12, 70)]), LEO, 'f'),
   L(outline([(16, 64), (0, 60, 1), (8, 72), (0, 82, 1), (18, 72)]), LEO, 'f')])

# Floyd Spades: pelo castaño revuelto en mechones de punta, uno muy alto echado hacia atrás; ojos de sueño con el párpado
# naranja, boca seria
C('floyd-spades', 'normal', pal('#8a6a4c', '#f2ba84', '#1e1e1e', shade='#664c34'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=94, hairline=hl(6, 60, 46, 56, lean=2, jit=3, seed=41)),
  dome('front', top=4, w=46, cy=44, n=8, amp=9, sweep=0.3, sb=62, seed=42) + [L(outline([(30, 12), (20, -12, 1), (44, 6)]), 'mid'),
                                                                               L([(28, 72), (42, 72)], _c('#e89a5a'), 'f', False, False, 2.4),
                                                                               L([(58, 72), (72, 72)], _c('#e89a5a'), 'f', False, False, 2.4)],
  dome('side', top=4, w=46, cy=44, n=8, amp=9, sweep=0.3, nape=84, fr=48, seed=42) + [L(outline([(30, 10), (14, -10, 1), (44, 4)]), 'mid')],
  dome('back', top=4, w=46, cy=44, n=8, amp=9, sweep=0.3, nape=86, seed=42) + [L(outline([(70, 12), (80, -12, 1), (56, 6)]), 'mid')])

# Fonda Katz: pelo rojo con una coleta de lado atravesada por dos palillos; ojos lilas, cejas de apuro, coloretes y
# sonrisa tímida
C('fonda-katz', 'chica', pal('#c8303a', '#f6c8a0', '#6a5a8a', shade='#9a2028'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=94, hairline=hl(6, 62, 46, 56, lean=-2, seed=43)),
  dome('front', top=4, w=44, cy=46, sb=72, soft=True) +
  [L(outline([(80, 20), (92, 14), (100, 30), (98, 66), (92, 84, 1), (88, 60), (84, 34)]), 'mid'),
   L([(82, 24), (102, 8)], _c('#3a2a20'), 'f', False, False, 1.8), L([(84, 28), (104, 14)], _c('#3a2a20'), 'f', False, False, 1.8)] + blush(88, 24),
  dome('side', top=4, w=44, cy=46, nape=84, fr=52, soft=True) + [L(outline([(36, 14), (24, 10), (14, 30), (16, 66), (22, 84, 1), (26, 60), (32, 34)]), 'mid')],
  dome('back', top=4, w=44, cy=46, nape=86, soft=True) +
  [L(outline([(20, 20), (8, 14), (0, 30), (2, 66), (8, 84, 1), (12, 60), (16, 34)]), 'mid'), L([(18, 24), (-2, 8)], _c('#3a2a20'), 'f', False, False, 1.8)])

# Frank Homey: grandullón de cara enorme tostada con un cepillo de pelo azul marino muy corto encima; cejas gruesas
# fruncidas, aro en la nariz y una boca grande con dos dientes que asoman
C('frank-homey', 'corpulento', pal('#262a50', '#d8a262', '#1e1e1e', skin_d='#b2804a', shade='#161a36'),
  F(eyes='dot', brows=False, mouth='none', eye_y=72, hairline=False, big_ears=3, face_front=face(w=8, chin=112, jaw=10)),
  skull('front') + [L(outline([(34, 14), (34, 0), (66, 0), (66, 14), (50, 16)]), 'mid')] + thick_brows(64, BLACK, 4.4, tilt=0.9, w=16) +
  [L(ell(50, 82, 5, 4), 'skin_d', 'f'), L(ell(50, 88, 3, 3) + [ell(50, 88, 3, 3)[0]], _c('#c8c8d0'), 'f', False, False, 1.4),
   L(blob([(32, 94), (68, 94), (66, 108), (34, 108)], 5), _c('#a86a4a'), 'f'),
   L([(38, 94), (44, 94), (44, 100), (38, 100)], WHITE, 'f', False, True), L([(56, 94), (62, 94), (62, 100), (56, 100)], WHITE, 'f', False, True)],
  skull('side') + [L(outline([(40, 8), (42, -4), (72, -2), (70, 10)]), 'mid')] + side_brow(64, BLACK, 4.4, 0.9) +
  [L(ell(90, 82, 4, 4), 'skin_d', 'f'), L(blob([(78, 94), (92, 94), (92, 106), (80, 106)], 4), _c('#a86a4a'), 'f')],
  skull('back') + [L(outline([(34, 14), (34, 0), (66, 0), (66, 14), (50, 16)]), 'mid')])

# Fred Punch: cara larga, calvo por los lados con un mechón castaño de punta en lo alto; cejas gruesas en arco de malo,
# ojos grandes, nariz roja y una sonrisa enorme de dientes
C('fred-punch', 'normal', pal('#6c3c1c', '#f4c294', '#3a6a7a', shade='#4a2810'),
  F(eyes='normal', brows=False, mouth='none', hairline=False, face_front=face(chin=112), nose=(50, 88, 3)),
  skull('front') + [L(outline([(30, 14), (22, 2, 1), (38, 4), (44, -10, 1), (52, 2), (64, -8, 1), (66, 4), (80, 0, 1), (70, 14), (50, 18)]), 'mid')] +
  thick_brows(64, _c('#5a3018'), 4.0, tilt=1.2, w=16) + [L(ell(50, 88, 3.4, 3.4), _c('#e86a4a'), 'f')] + teeth_grin(98, 15, 7),
  skull('side') + [L(outline([(36, 8), (28, -4, 1), (44, -2), (54, -14, 1), (60, -2), (76, -6, 1), (72, 8)]), 'mid')] + side_brow(64, _c('#5a3018'), 4.0, 1.2),
  skull('back') + [L(outline([(30, 14), (22, 2, 1), (38, 4), (44, -10, 1), (52, 2), (64, -8, 1), (66, 4), (80, 0, 1), (70, 14), (50, 18)]), 'mid')])

# Garry Planer: portero grandullón de pelo castaño rojizo en pinchos hacia arriba, con una cinta azul marino de dibujo
# blanco en la frente; ojitos pequeños, nariz larga, rombos rojos pintados en las mejillas y boca seria
HDB = _c('#2a3460')
C('garry-planer', 'corpulento', pal('#7a3a22', '#f2c088', '#1e1e1e', shade='#562814'),
  F(eyes='dot', brows=False, mouth='frown', mouth_y=100, eye_y=74, hairline=False, face_front=face(w=6, chin=110, jaw=6)),
  [L(outline([(16, 60), (12, 34), (16, 10, 1), (30, 16), (34, -6, 1), (46, 10), (56, -12, 1), (62, 8), (78, -4, 1), (78, 16), (92, 14, 1), (86, 34), (86, 60), (50, 56)])),
   L(outline([(10, 62), (12, 42), (50, 38), (88, 42), (90, 62), (50, 58)]), HDB, 'f'),
   L(blob([(34, 46), (50, 42), (66, 46), (66, 54), (50, 56), (34, 54)], 5) + [blob([(34, 46), (50, 42), (66, 46), (66, 54), (50, 56), (34, 54)], 5)[0]],
     _c('#e2dcc8'), 'f', False, False, 2.0),
   L(nose_tri(90, 4, 12)[0]['s'], 'skin_d', 'f', False, True),
   L([(26, 86), (30, 82), (34, 86), (30, 90)], RED, 'f', False, True), L([(66, 86), (70, 82), (74, 86), (70, 90)], RED, 'f', False, True)],
  [L(outline([(80, 50), (84, 30), (80, 8, 1), (64, 10), (60, -12, 1), (46, 6), (30, -6, 1), (24, 14), (6, 14, 1), (6, 40), (8, 62), (26, 72), (46, 66), (62, 56)])),
   L(outline([(4, 54), (8, 40), (50, 38), (88, 40), (88, 56), (50, 56)]), HDB, 'f'), L([(88, 84), (92, 80), (96, 84), (92, 88)], RED, 'f', False, True)],
  [L(outline([(14, 74), (10, 34), (14, 10, 1), (30, 16), (34, -6, 1), (46, 10), (56, -12, 1), (62, 8), (78, -4, 1), (78, 16), (92, 14, 1), (90, 34), (88, 74), (50, 80)])),
   L(outline([(8, 62), (10, 44), (50, 40), (90, 44), (92, 62), (50, 60)]), HDB, 'f')])

# Gary Burdine: máscara de calavera crema que le cubre toda la cabeza, con un rayo naranja que la cruza, dos cuencas
# negras enormes y una sonrisa roja pintada de payaso
SKC, BOLT = _c('#f4ead0'), _c('#f0a020')
C('gary-burdine', 'normal', pal('#f4ead0', '#f4ead0', '#1e1e1e', shade='#d8ccb0', skin_d='#d8ccb0'),
  F(eyes='none', brows=False, mouth='none', hairline=False),
  skull('front', SKC) +
  [L([(42, 6), (54, 30), (40, 30), (70, 60), (82, 54)], BOLT, 'f', False, False, 4.0),
   L(ell(36, 76, 9, 9), BLACK, 'f', False), L(ell(64, 76, 9, 9), BLACK, 'f', False),
   L([(50, 82), (53, 88), (47, 88)], BLACK, 'f', False, True),
   L(quad((26, 90), (50, 104), (74, 90)), RED, 'f', False, False, 3.0), L(blob([(44, 100), (56, 100), (54, 106), (46, 106)], 3), RED, 'f', False)],
  skull('side', SKC) + [L([(40, 4), (64, 26), (52, 30), (80, 54)], BOLT, 'f', False, False, 4.0),
                        L(ell(80, 76, 6, 9), BLACK, 'f', False), L(quad((70, 92), (84, 100), (92, 92)), RED, 'f', False, False, 3.0)],
  skull('back', SKC) + [L([(50, 6), (40, 30), (56, 34), (30, 66)], BOLT, 'f', False, False, 4.0)])


# -------------------------------------------------------------------------------------------------------------- 41-48

def hero_mask(view, hair_front, hair_side, hair_back, eye_out, eye_in, mw=None, tie=None):
    """Máscara blanca de héroe que tapa media cara, con los ojos en llama, el pañuelo atado detrás y el pelo encima."""
    MW = mw or _c('#f4f2ee')
    TIE = tie or MW
    if view == 'front':
        return hair_front + [
            L(outline([(14, 70), (12, 40), (24, 18), (50, 10), (76, 18), (88, 40), (86, 70), (70, 86), (50, 92, 1), (30, 86)]), MW, 'f'),
            L(blob([(24, 62), (36, 54), (48, 72), (40, 84), (28, 80)], 5), eye_out, 'f', False), L(blob([(76, 62), (64, 54), (52, 72), (60, 84), (72, 80)], 5), eye_out, 'f', False),
            L(blob([(29, 68), (37, 62), (44, 73), (37, 80)], 5), eye_in, 'f', False), L(blob([(71, 68), (63, 62), (56, 73), (63, 80)], 5), eye_in, 'f', False)]
    if view == 'side':
        return hair_side + [
            L(outline([(86, 72), (90, 40), (78, 16), (50, 8), (24, 14), (8, 34), (6, 60), (22, 72), (50, 80), (72, 84)]), MW, 'f'),
            L(blob([(74, 62), (84, 56), (90, 70), (82, 82)], 5), eye_out, 'f', False),
            L(outline([(12, 60), (-6, 74, 1), (0, 56), (-8, 48, 1), (8, 50)]), TIE, 'f')]
    return hair_back + [
        L(outline([(12, 74), (10, 40), (24, 16), (50, 8), (76, 16), (90, 40), (88, 74), (50, 82)]), MW, 'f'),
        L(outline([(44, 62), (30, 86, 1), (48, 70), (52, 70), (70, 86, 1), (56, 62)]), TIE, 'f')]


# Gary "Red" Primo: como el Yellow pero en rojo: máscara blanca de héroe con los ojos en llama roja y amarilla y el pelo
# rubio de pinchos altos asomando por arriba
SPK = [(26, 20), (22, -10, 1), (36, 8), (44, -22, 1), (54, 6), (66, -16, 1), (68, 10), (82, -2, 1), (78, 20)]
C('gary-red-s-primo', 'normal', pal('#f6e07c', '#f6d6b0', '#1e1e1e', shade='#d8b85a'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=98, hairline=False, face_front=face(w=2, chin=106)),
  hero_mask('front', [L(outline(SPK), 'mid')], [L(outline([(30, 16), (28, -12, 1), (44, 6), (56, -20, 1), (62, 6), (80, -6, 1), (74, 14)]), 'mid')],
            [L(outline(SPK), 'mid')], _c('#e2402a'), _c('#f6d050')),
  hero_mask('side', [], [L(outline([(30, 16), (28, -12, 1), (44, 6), (56, -20, 1), (62, 6), (80, -6, 1), (74, 14)]), 'mid')], [], _c('#e2402a'), _c('#f6d050')),
  hero_mask('back', [], [], [L(outline(SPK), 'mid')], _c('#e2402a'), _c('#f6d050')))

# Gem Shorn: portero de pelo naranja en mechones gordos de llama echados hacia arriba; ojos redondos grandes y sonrisa
C('gem-shorn', 'normal', pal('#d8762c', '#f6c898', '#1e1e1e', shade='#a8521a', deep='#8a3e10'),
  F(eyes='round', brows=True, mouth='smile', mouth_y=94, eye_sep=15, hairline=hl(5, 60, 44, 52, lean=3, seed=51)),
  [L(outline([(16, 62), (8, 40), (2, 16, 1), (20, 22), (20, -2, 1), (36, 10), (44, -16, 1), (56, 6), (72, -14, 1), (72, 10), (96, 2, 1), (88, 26), (94, 40, 1),
              (86, 48), (84, 62), (80, 48), (20, 48)])),
   L(outline([(56, 4), (72, -10), (72, 12), (94, 6), (86, 28), (90, 40), (84, 52), (76, 30)]), 'shade', 'b', False),
   strand([(30, 14), (28, 34)], 'deep', 'b', 1.0), strand([(50, 4), (52, 30)], 'deep', 'b', 1.0)],
  [L(outline([(70, 50), (84, 42), (92, 26, 1), (82, 20), (90, -4, 1), (66, 6), (64, -16, 1), (48, 4), (28, -10, 1), (26, 10), (4, 10, 1), (10, 30), (4, 54),
              (20, 64), (40, 60), (56, 52)]))],
  [L(outline([(14, 70), (8, 40), (2, 16, 1), (20, 22), (20, -2, 1), (36, 10), (44, -16, 1), (56, 6), (72, -14, 1), (72, 10), (96, 2, 1), (90, 26), (96, 40, 1),
              (88, 48), (86, 70), (50, 78)]))])

# George Barros: media melena verde oliva con las puntas hacia fuera y flequillo; ojos redondos enormes y boca pequeña
C('george-barros', 'normal', pal('#6e8a34', '#f6c8a0', '#1e1e1e', shade='#4e6a20'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=96, eye_sep=15, hairline=hl(7, 60, 46, 56, seed=53)),
  dome('front', top=4, w=46, cy=46, long=88, flare=10, soft=True) + [L(outline([(48, 6), (52, -6, 1), (58, 6)]), 'mid')],
  dome('side', top=4, w=46, cy=46, long=86, flare=10, fr=52, soft=True),
  dome('back', top=4, w=46, cy=46, long=88, flare=10, ends=4, soft=True))

# Georgio Plumber: pelo azul en pinchos grandes que salen hacia todos lados, con mechones de punta por la frente; ojos
# afilados de enfado y boca seria
C('georgio-plumber', 'normal', pal('#2c5c9c', '#f2c08a', '#1e1e1e', shade='#1c3e72'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, hairline=hl(6, 62, 44, 58, jit=3, seed=55)),
  dome('front', top=0, w=48, cy=44, n=11, amp=13, sb=66, seed=56),
  dome('side', top=0, w=48, cy=44, n=11, amp=13, nape=84, fr=52, seed=56),
  dome('back', top=0, w=48, cy=44, n=11, amp=13, nape=86, seed=56))

# Gerald Pourer: piel morena con una mata rojo oscuro abultada por arriba y rizos largos a los lados; ojos de enfado,
# arrugas en las mejillas y boca torcida
C('gerald-pourer', 'normal', pal('#a82222', '#b47a52', '#1e1e1e', skin_d='#8e5a3a', shade='#7a1414'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=96, hairline=[(14, 64), (18, 50), (30, 46), (50, 44), (70, 46), (82, 50), (86, 64)],
    face_front=face(w=4, chin=106)),
  [L(curls(50, 24, (52, 22), 9)), L(curls(10, 74, (10, 22), 4, 0.4), 'mid', 'f'), L(curls(90, 74, (10, 22), 4, 0.8), 'mid', 'f'),
   L(curls(60, 18, (24, 10), 5), 'shade', 'b', False)] +
  [L([(24, 90), (30, 94)], OUTC, 'f', False, False, 0.9), L([(76, 90), (70, 94)], OUTC, 'f', False, False, 0.9)],
  [L(curls(46, 24, (48, 22), 9)), L(curls(28, 66, (22, 26), 5))],
  [L(curls(50, 26, (52, 24), 9)), L(curls(50, 70, (40, 26), 7))])

# Gertrude Choker: portera de cara ancha y redonda con el pelo gris morado ondulado hasta la mandíbula y un rizo sobre la
# frente; ojos afilados con pestañas, coloretes naranjas y labios pintados
C('gertrude-choker', 'corpulento', pal('#7a5c8e', '#f6c482', '#4a4a1e', shade='#5a4070'),
  F(eyes='sharp', brows=True, mouth='lips', mouth_y=98, mouth_w=6, hairline=[(14, 64), (18, 46), (34, 38), (50, 36), (66, 38), (82, 46), (86, 64)],
    face_front=face(w=8, chin=110, jaw=8)),
  dome('front', top=10, w=48, cy=50, long=96, flare=8, soft=True) +
  [fr([(48, 34), (44, 46), (50, 56, 1), (54, 46), (56, 34)]),
   L(ell(28, 90, 5, 4.6), _c('#f09a50'), 'f', False), L(ell(72, 90, 5, 4.6), _c('#f09a50'), 'f', False)],
  dome('side', top=10, w=48, cy=50, long=94, flare=8, fr=50, soft=True),
  dome('back', top=10, w=48, cy=50, long=96, flare=8, ends=4, soft=True))

# Gil Holden: pelo azul en un tupé alto de punta hacia arriba; piel clara, cara larga, ojos entornados y sonrisa enorme
# de dientes
C('gil-holden', 'delgado', pal('#3a92d2', '#ecd2aa', '#1e1e1e', shade='#2068a8'),
  F(eyes='closed', brows=False, mouth='none', hairline=[(18, 54), (24, 40), (40, 36), (60, 36), (76, 40), (82, 54)], face_front=face(chin=112), big_ears=2),
  [L(outline([(18, 54), (14, 30), (26, -8), (40, -24, 1), (50, -6), (62, -26, 1), (68, -6), (80, 10), (86, 30), (82, 54), (78, 44), (22, 44)])),
   L(outline([(60, -20), (68, -4), (82, 12), (86, 32), (80, 50), (72, 20)]), 'shade', 'b', False),
   strand([(40, -14), (44, 30)], 'shade', 'b', 1.2)] + teeth_grin(98, 15, 6),
  [L(outline([(70, 44), (82, 36), (84, 14), (70, -8), (50, -26, 1), (36, -6), (18, 4), (6, 26), (8, 50), (24, 60), (44, 56), (58, 48)]))],
  [L(outline([(16, 64), (12, 30), (26, -8), (40, -24, 1), (50, -6), (62, -26, 1), (68, -6), (80, 10), (88, 30), (84, 64), (50, 70)]))])

# Ginny White: capucha blanca de vaca con cuernos, manchas marrones y el morro con dos agujeros sobre la frente; pelo
# morado oscuro asomando a los lados, ojos amarillos afilados y boca en "o"
CW, CB = _c('#f6f2ea'), _c('#7a4a2e')
C('ginny-white', 'chica', pal('#3e2a5a', '#f8e4c4', '#d8a020', shade='#2a1c40'),
  F(eyes='sharp', brows=False, mouth='none', hairline=False),
  [L(outline([(16, 74), (8, 92, 1), (20, 70)]), 'mid', 'b'), L(outline([(84, 74), (92, 92, 1), (80, 70)]), 'mid', 'b'),
   L(outline([(12, 74), (8, 40), (20, 14), (50, 4), (80, 14), (92, 40), (88, 74), (80, 60), (20, 60)]), CW, 'f'),
   L(outline([(20, 16), (6, 6), (4, 14), (18, 24)]), _c('#e0c8a8'), 'f'), L(outline([(80, 16), (94, 6), (96, 14), (82, 24)]), _c('#e0c8a8'), 'f'),
   L(ell(30, 10, 3, 2.4), CB, 'f', False), L(ell(70, 10, 3, 2.4), CB, 'f', False),
   L(blob([(22, 34), (50, 28), (78, 34), (76, 54), (50, 58), (24, 54)], 6), _c('#e6c4b4'), 'f'),
   L(ell(38, 44, 8, 7), CB, 'f'), L(ell(62, 44, 8, 7), CB, 'f'), L(ell(50, 96, 2.6, 3.2), (120, 40, 40, 255), 'f', True)],
  [L(outline([(36, 76), (30, 92, 1), (46, 74)]), 'mid', 'b'),
   L(outline([(84, 60), (92, 34), (80, 12), (52, 2), (24, 8), (6, 30), (4, 62), (18, 78), (40, 78), (56, 62), (70, 54)]), CW, 'f'),
   L(outline([(40, 12), (30, 0), (28, 8), (40, 18)]), _c('#e0c8a8'), 'f'), L(blob([(78, 32), (98, 32), (100, 54), (80, 54)], 5), _c('#e6c4b4'), 'f'),
   L(ell(30, 40, 4, 3), CB, 'f', False)],
  [L(outline([(16, 80), (8, 92, 1), (20, 70)]), 'mid', 'b'), L(outline([(84, 80), (92, 92, 1), (80, 70)]), 'mid', 'b'),
   L(outline([(12, 80), (8, 40), (20, 14), (50, 4), (80, 14), (92, 40), (88, 80), (50, 86)]), CW, 'f'),
   L(outline([(20, 16), (6, 6), (4, 14), (18, 24)]), _c('#e0c8a8'), 'f'), L(outline([(80, 16), (94, 6), (96, 14), (82, 24)]), _c('#e0c8a8'), 'f'),
   L(ell(36, 40, 5, 4), CB, 'f', False), L(ell(64, 60, 6, 4), CB, 'f', False)])


# -------------------------------------------------------------------------------------------------------------- 49-56

# Glenn Broth: grandullón de cara larga con el pelo verde rapado muy corto arriba; ojeras, nariz grande, orejas grandes
# y una boca de labios gruesos enfurruñada
C('glenn-broth', 'corpulento', pal('#2e6a50', '#f0b47a', '#1e1e1e', skin_d='#c88a56', shade='#1e4a36'),
  F(eyes='round', brows='angry', mouth='none', eye_y=74, hairline=[(16, 50), (22, 30), (36, 20), (50, 18), (64, 20), (78, 30), (84, 50)],
    face_front=face(w=4, chin=114, jaw=4), big_ears=3),
  dome('front', top=8, w=38, cy=40, sb=44, shade=False) +
  [L(ell(36, 76, 8, 6) + [ell(36, 76, 8, 6)[0]], _c('#8a5a3a'), 'f', False, False, 1.6), L(ell(64, 76, 8, 6) + [ell(64, 76, 8, 6)[0]], _c('#8a5a3a'), 'f', False, False, 1.6),
   L(blob([(44, 78), (56, 78), (58, 92), (50, 94), (42, 92)], 5), 'skin_d', 'f'),
   L(blob([(38, 100), (50, 96), (62, 100), (60, 106), (50, 104), (40, 106)], 4), _c('#9a6a4e'), 'f')],
  dome('side', top=8, w=38, cy=40, nape=56, fr=30, shade=False) + [L(blob([(86, 80), (96, 88), (88, 94)], 4), 'skin_d', 'f')],
  dome('back', top=8, w=38, cy=40, nape=56, shade=False))

# Grant "Red" Stodgell: la máscara de héroe en negro y gris con los ojos en llama roja, el pelo rojo oscuro en pinchos
# altos y el pañuelo negro atado detrás
SPK2 = [(24, 22), (24, -8, 1), (36, 6), (48, -26, 1), (58, 4), (70, -14, 1), (70, 10), (84, 0, 1), (78, 22)]
MK = _c('#3a3a40')
C('grant-red-d-stodgell', 'normal', pal('#7c1c22', '#f2b67e', '#1e1e1e', shade='#561016'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=98, hairline=False, face_front=face(w=2, chin=106)),
  hero_mask('front', [L(outline(SPK2), 'mid')], [], [], _c('#e8e8ec'), _c('#d82a2a'), MK, _c('#2a2a2e')),
  hero_mask('side', [], [L(outline([(30, 18), (26, -12, 1), (44, 4), (56, -22, 1), (62, 4), (82, -8, 1), (74, 16)]), 'mid')], [], _c('#e8e8ec'), _c('#d82a2a'), MK,
            _c('#2a2a2e')),
  hero_mask('back', [], [], [L(outline(SPK2), 'mid')], _c('#e8e8ec'), _c('#d82a2a'), MK, _c('#2a2a2e')))

# Gregg Deremer: portero gordo de cara redonda con una melena en casco magenta que le tapa las orejas; ojitos de punto,
# una marca en la frente y una sonrisa enorme de dientes, papada
C('gregg-deremer', 'corpulento', pal('#aa2c4c', '#f6c48a', '#1e1e1e', skin_d='#d8a06a', shade='#801c36'),
  F(eyes='dot', brows=False, mouth='none', eye_y=76, eye_sep=12, hairline=[(12, 70), (14, 56), (30, 48), (50, 46), (70, 48), (86, 56), (88, 70)],
    face_front=face(w=8, chin=114, jaw=10)),
  bowl('front', 2, 78, w=6) + [L([(46, 60), (50, 56), (54, 60)], _c('#c8705a'), 'f', False, False, 1.4)] + teeth_grin(94, 15, 7) +
  [L(quad((40, 110), (50, 114), (60, 110)), 'skin_d', 'f', False, False, 1.2)],
  bowl('side', 2, 80, w=6),
  bowl('back', 2, 82, w=6))

# Griff Hardcasel: pelo castaño rojizo en pinchos altos de punta y mechones largos que le caen por los lados hasta los
# hombros; piel clara, ojos verdes afilados y media sonrisa
C('griff-hardcasel', 'normal', pal('#8a4a2a', '#f4dcbc', '#4a8a2a', shade='#62321a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=96, hairline=hl(6, 62, 46, 58, jit=3, seed=61)),
  dome('front', top=0, w=46, cy=44, n=10, amp=12, sb=64, seed=62) +
  [fr([(14, 54), (8, 84), (12, 110, 1), (22, 84), (22, 56)]), fr([(86, 54), (92, 84), (88, 110, 1), (78, 84), (78, 56)])],
  dome('side', top=0, w=46, cy=44, n=10, amp=12, nape=88, fr=50, seed=62) + [fr([(54, 56), (58, 86), (54, 110, 1), (48, 86)])],
  dome('back', top=0, w=46, cy=44, n=10, amp=12, long=106, flare=4, ends=4, seed=62))

# Guy Kogan: pelo plateado en pinchos enormes que salen hacia todos lados; piel clara con un rombo blanco pintado en la
# frente y otros alrededor de los ojos verde azulado, ceño y boca seria
DIA = _c('#f6f4ee')
C('guy-kogan', 'normal', pal('#b8c0ca', '#f6dcb8', '#2e8a8a', shade='#8a929e'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, hairline=hl(6, 60, 44, 56, jit=3, seed=63)),
  dome('front', top=-2, w=50, cy=44, n=11, amp=15, sb=64, seed=64) +
  [L([(50, 46), (58, 56), (50, 66), (42, 56)], DIA, 'f', False, True),
   L([(36, 66), (48, 76), (36, 86), (24, 76)], DIA, 'b', False, True), L([(64, 66), (76, 76), (64, 86), (52, 76)], DIA, 'b', False, True)],
  dome('side', top=-2, w=50, cy=44, n=11, amp=15, nape=84, fr=50, seed=64),
  dome('back', top=-2, w=50, cy=44, n=11, amp=15, nape=86, seed=64))

# Guy Pinnay: pelo morado corto con pico en la frente; cara larga, ojos redondos grandes de enfado, una nariz grande
# marrón y sonrisa ancha
C('guy-pinnay', 'normal', pal('#6a5a92', '#f6c896', '#1e1e1e', skin_d='#c88a5a', shade='#4a3e6e'),
  F(eyes='round', brows='angry', mouth='smile', mouth_y=100, eye_sep=15, hairline=[(16, 54), (20, 40), (34, 32), (50, 50), (66, 32), (80, 40), (84, 54)],
    face_front=face(chin=112)),
  dome('front', top=4, w=42, cy=42, sb=52, n=3, amp=6, seed=65) + [L(blob([(46, 78), (54, 78), (58, 92), (50, 96), (42, 92)], 5), _c('#a86a42'), 'f'),
                                                                   L(quad((36, 98), (50, 106), (64, 98)), OUTC, 'f', False, False, 1.6)],
  dome('side', top=4, w=42, cy=42, nape=66, fr=40, n=3, amp=6, seed=65) + [L(blob([(86, 80), (98, 90), (88, 96)], 4), _c('#a86a42'), 'f')],
  dome('back', top=4, w=42, cy=42, nape=66, n=3, amp=6, seed=65))

# Gyll Netters: pelo azul grisáceo corto de pinchos y una cinta de cuerda crema retorcida atada a un lado; cara redonda,
# coloretes naranjas, nariz naranja, ceño y sonrisa con los dos dientes fuera
ROPE = _c('#ece0c0')
C('gyll-netters', 'normal', pal('#3a4a62', '#f4c084', '#1e1e1e', shade='#262f42'),
  F(eyes='round', brows='angry', mouth='buck', mouth_y=96, hairline=False, face_front=face(w=4, chin=106)),
  dome('front', top=4, w=46, cy=44, n=9, amp=8, sb=60, seed=67) +
  [L(blob([(10, 50), (50, 38), (90, 50), (90, 58), (50, 48), (10, 58)], 6), ROPE, 'f'),
   L([(80, 44), (88, 30), (96, 38)], ROPE, 'f', False, False, 3.4), L([(84, 46), (96, 46)], ROPE, 'f', False, False, 3.0),
   L(ell(28, 88, 5, 4.4), _c('#f09a50'), 'f', False), L(ell(72, 88, 5, 4.4), _c('#f09a50'), 'f', False), L(ell(50, 86, 4, 3), _c('#f09a50'), 'f')],
  dome('side', top=4, w=46, cy=44, n=9, amp=8, nape=80, fr=46, seed=67) + [L(blob([(4, 50), (50, 38), (92, 44), (92, 52), (50, 48), (6, 60)], 6), ROPE, 'f')],
  dome('back', top=4, w=46, cy=44, n=9, amp=8, nape=82, seed=67) + [L(blob([(8, 54), (50, 46), (92, 54), (92, 62), (50, 54), (8, 62)], 6), ROPE, 'f'),
                                                                     L([(20, 50), (10, 36), (4, 44)], ROPE, 'f', False, False, 3.4)])

# Haden Safe: pelo verde azulado echado hacia atrás en dos alas grandes de punta y mechones largos por los lados de la
# cara; ojos verde oliva afilados y media sonrisa
C('haden-safe', 'normal', pal('#2e7a70', '#f6cca0', '#7a7a2a', shade='#1e5850'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=96, hairline=hl(4, 62, 44, 60, seed=69)),
  [L(outline([(16, 62), (10, 44), (-8, 10, 1), (20, 20), (36, 4), (50, 0), (64, 4), (80, 20), (108, 10, 1), (90, 44), (84, 62), (80, 48), (20, 48)])),
   L(outline([(56, 2), (80, 18), (104, 12), (88, 44), (84, 58), (76, 30)]), 'shade', 'b', False),
   fr([(14, 54), (10, 84), (16, 104, 1), (22, 82), (22, 56)]), fr([(86, 54), (90, 84), (84, 104, 1), (78, 82), (78, 56)]),
   fr([(44, 46), (50, 72, 1), (56, 46)])],
  [L(outline([(70, 48), (86, 40), (88, 24), (72, 6), (50, 0), (24, 4), (-12, 0, 1), (6, 30), (4, 54), (20, 66), (40, 62), (56, 52)])),
   fr([(56, 56), (60, 84), (56, 104, 1), (50, 84)])],
  [L(outline([(14, 72), (10, 44), (-8, 10, 1), (20, 20), (36, 4), (50, 0), (64, 4), (80, 20), (108, 10, 1), (90, 44), (86, 72), (50, 78)]))])


# -------------------------------------------------------------------------------------------------------------- 57-62

# Hank Cranker: payaso: pelo morado peinado hacia atrás con dos moños bajos a los lados, la cara pintada de blanco con
# manchas negras alrededor de los ojos, nariz roja de triángulo, sonrisa enorme de dientes y aros dorados en la oreja
C('hank-cranker', 'normal', pal('#7a3ca2', '#f8eedc', '#c8a020', skin_d='#dcd0bc', shade='#562a78'),
  F(eyes='none', brows=False, mouth='none', hairline=[(16, 56), (22, 36), (36, 26), (50, 24), (64, 26), (78, 36), (84, 56)], face_front=face(chin=110)),
  dome('front', top=4, w=42, cy=42, sb=52) +
  [L(ell(14, 84, 8, 8), 'mid'), L(ell(86, 84, 8, 8), 'mid'),
   L(blob([(24, 66), (34, 62), (46, 72), (42, 84), (30, 84), (24, 76)], 5), BLACK, 'f', False),
   L(blob([(76, 66), (66, 62), (54, 72), (58, 84), (70, 84), (76, 76)], 5), BLACK, 'f', False),
   L(ell(36, 75, 3.6, 3.6), _c('#e8d870'), 'f', False), L(ell(64, 75, 3.6, 3.6), _c('#e8d870'), 'f', False),
   L(ell(36, 75, 1.4, 1.4), BLACK, 'f', False), L(ell(64, 75, 1.4, 1.4), BLACK, 'f', False),
   L([(44, 78), (56, 78), (50, 96)], RED, 'f', False, True),
   L(ell(84, 80, 2, 2) + [ell(84, 80, 2, 2)[0]], _c('#f0c040'), 'f', False, False, 1.2)] + teeth_grin(100, 16, 7),
  dome('side', top=4, w=42, cy=42, nape=72, fr=36) + [L(ell(30, 82, 9, 9), 'mid'), L(blob([(76, 66), (86, 64), (88, 82), (78, 84)], 5), BLACK, 'f', False),
                                                      L([(86, 80), (100, 88), (88, 92)], RED, 'f', False, True)],
  dome('back', top=4, w=42, cy=42, nape=74) + [L(ell(18, 82, 9, 9), 'mid'), L(ell(82, 82, 9, 9), 'mid')])

# Hank Ershef: pelo gris con el flequillo de mechones largos por la frente; gafas finas redondeadas doradas, ojos verdes y
# boca seria
C('hank-ershef', 'normal', pal('#a8a8ae', '#f2c08a', '#3e7a4a', shade='#82828a', deep='#6a6a72'),
  F(eyes='normal', brows=False, mouth='frown', mouth_y=96, hairline=hl(6, 62, 46, 64, lean=-2, seed=71)),
  dome('front', top=4, w=44, cy=44, sb=66, n=6, amp=4, soft=True, seed=72) +
  [L(ell(x, 77, 9.5, 7) + [ell(x, 77, 9.5, 7)[0]], _c('#d8a040'), 'f', False, False, 1.4) for x in (36, 64)] +
  [L([(45.5, 77), (54.5, 77)], _c('#d8a040'), 'f', False, False, 1.2), strand([(40, 10), (34, 40)], 'deep', 'b', 1.0), strand([(62, 10), (66, 40)], 'deep', 'b', 1.0)],
  dome('side', top=4, w=44, cy=44, nape=84, fr=56, n=6, amp=4, soft=True, seed=72) + round_glasses('side', _c('#d8a040'), 77, r=7, w=1.4),
  dome('back', top=4, w=44, cy=44, nape=86, n=6, amp=4, soft=True, seed=72))

# Hanna "Pink" Slack: la máscara de héroe negra y gris con los ojos en llama rosa, la melena granate larga por detrás y el
# pañuelo negro atado
C('hanna-pink-d-slack', 'chica', pal('#7a2a3c', '#b47a4e', '#1e1e1e', shade='#561c28'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=98, hairline=False, face_front=face(chin=104)),
  hero_mask('front', dome('front', top=2, w=48, cy=46, long=100, flare=6), [], [], _c('#f0b0cc'), _c('#e8508a'), MK, _c('#2a2a2e')),
  hero_mask('side', [], dome('side', top=2, w=48, cy=46, long=98, flare=6, fr=50), [], _c('#f0b0cc'), _c('#e8508a'), MK, _c('#2a2a2e')),
  hero_mask('back', [], [], dome('back', top=2, w=48, cy=46, long=100, flare=6, ends=4), _c('#f0b0cc'), _c('#e8508a'), MK, _c('#2a2a2e')))

# Hannah Breer: media melena gris verdosa con flequillo recto y una capucha o diadema ancha rosa encima; ojos negros
# grandes y sonrisa
HPK = _c('#f08a96')
C('hannah-breer', 'chica', pal('#9cb2b2', '#f6c898', '#1e1e1e', shade='#7a9090'),
  F(eyes='big', mouth='smile', mouth_y=94, hairline=[(14, 66), (16, 58), (30, 60), (50, 60), (70, 60), (84, 58), (86, 66)]),
  bowl('front', 2, 86) + [fr([(16, 40), (30, 24), (50, 20), (70, 24), (84, 40), (84, 60), (16, 60)]),
                          L(blob([(14, 40), (20, 14), (50, 6), (80, 14), (86, 40), (50, 34)], 6), HPK, 'f')],
  bowl('side', 2, 88) + [L(blob([(10, 40), (18, 12), (50, 4), (80, 12), (88, 34), (50, 32)], 6), HPK, 'f')],
  bowl('back', 2, 90) + [L(blob([(12, 44), (20, 14), (50, 6), (80, 14), (88, 44), (50, 38)], 6), HPK, 'f')])

# Hannibal Whipp: zombi: piel beis grisácea con costras marrones en las mejillas, pelo castaño abierto hacia los lados en
# puntas, ojos redondos amarillentos de mirada perdida y barbilla larga
SCAB = _c('#a88a62')
C('hannibal-whipp', 'normal', pal('#8a4a20', '#e4d2aa', '#4a4a2a', skin_d='#c4b088', shade='#623212'),
  F(eyes='round', brows=False, mouth='none', eye_sep=15, hairline=hl(5, 60, 40, 54, seed=73), face_front=face(chin=112)),
  [L(outline([(16, 64), (10, 46), (-12, 66, 1), (4, 38), (14, 16), (50, 2), (86, 16), (96, 38), (112, 66, 1), (90, 46), (84, 64), (80, 46), (20, 46)])),
   L(outline([(58, 4), (86, 18), (98, 40), (108, 62), (88, 48), (78, 28)]), 'shade', 'b', False),
   L(ell(36, 76, 7, 7) + [ell(36, 76, 7, 7)[0]], _c('#c8b860'), 'f', False, False, 1.6), L(ell(64, 76, 7, 7) + [ell(64, 76, 7, 7)[0]], _c('#c8b860'), 'f', False, False, 1.6)] +
  [L(blob([(x - 3, y - 2), (x + 3, y - 2), (x + 2, y + 2), (x - 2, y + 2)], 3), SCAB, 'f', False) for x, y in ((26, 88), (30, 94), (24, 96), (72, 88), (76, 94))],
  [L(outline([(70, 46), (86, 40), (90, 22), (70, 4), (40, 2), (14, 14), (4, 36), (-14, 62, 1), (8, 56), (20, 66), (40, 62), (56, 50)])),
   L(blob([(80, 88), (86, 88), (85, 93), (79, 93)], 3), SCAB, 'f', False)],
  [L(outline([(14, 72), (8, 46), (-12, 66, 1), (4, 38), (14, 16), (50, 2), (86, 16), (96, 38), (112, 66, 1), (92, 46), (86, 72), (50, 78)]))])

# Hans Freesing: melena morada lisa con la raya a un lado que le tapa un ojo y una coleta baja que cae por un lado;
# piel clara, ojo entornado y boca seria
C('hans-freesing', 'normal', pal('#5c4c9c', '#f8e0c0', '#3a6a8a', shade='#3e3274'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=96, hairline=False),
  dome('front', top=2, w=46, cy=46, sb=70, soft=True) +
  [fr([(56, 8), (24, 14), (14, 34), (14, 62), (20, 92, 1), (30, 72), (44, 70), (50, 94, 1), (54, 60), (60, 36), (70, 20)]),
   L(outline([(78, 76), (88, 96), (84, 118, 1), (76, 100), (72, 80)]), 'mid', 'f')],
  dome('side', top=2, w=46, cy=46, nape=84, fr=56, soft=True) + [L(outline([(30, 78), (24, 100), (30, 118, 1), (36, 98), (40, 80)]), 'mid', 'f')],
  dome('back', top=2, w=46, cy=46, nape=86, soft=True) + [L(outline([(26, 78), (16, 98), (20, 118, 1), (28, 100), (34, 80)]), 'mid', 'f')])
