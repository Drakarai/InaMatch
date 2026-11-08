"""Ojeadores de GX (scouts-gx), tanda 04: dibujados a partir de su retrato de Victory Road; claves 'scouts-gx:<id>'.

Casi todos salen del retrato (perfil y espalda deducidos); los pocos con modelo 3D propio (Roleia, Saber, Schemer, Seraph,
Skie, Skip, Sonny, Tetsu) se han mirado en él para el perfil y la espalda. El sexo (para el cuerpo) es el de la ficha de la
wiki. Muchos son alienígenas o van con la cabeza tapada por un disfraz: esos llevan no_head y la cabeza entera dibujada en
capas (head() abajo). Ayudas: las de las tandas anteriores (dome/hl/face de ie1_09, hood/ring de ie3_02, cap/band de ie3_06,
ears_pointy de ie2_03, crop/brows/ring_glasses de chars_vr_nikogawa, dots_eyes/eye_side_n de go_09)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401
from chars_scouts_ie1_09 import BLACK, WHITE, F, P, _c, dome, face, face_side, hl, mark  # noqa: F401
from chars_scouts_ie3_06 import arc, band, bush, cap  # noqa: F401
from chars_scouts_ie3_02 import hood, ring, scarf, skull3  # noqa: F401
from chars_scouts_ie2_03 import ears_pointy  # noqa: F401
from chars_scouts_go_09 import dots_eyes, eye_side_n, tuft  # noqa: F401
from chars_vr_nikogawa import brow_side, brows, crop, ring_glasses  # noqa: F401

_DOT = blob([(48, 90), (52, 90), (52, 94), (48, 94)], 2)
# cabezas tapadas: sin cara ni orejas (con face_front/face_side propios para que no se pinte la sombra de la cara)
NOFACE = dict(eyes='none', brows=False, mouth='none', hairline=False, no_head=True, ears=False, face_front=_DOT, face_side=_DOT)


def C(pid, body, palette, f, front, side, back):
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        # el nacimiento del pelo baja por el borde de la cara: así su raya no cruza el pelo de los lados
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[f'scouts-gx:{pid}'] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def M(pts, c='mid', z='b', sil=True, ln=False):
    return L(outline(pts), c, z, sil, ln)


def head(view, c, top=0, w=46, low=100, shade=None, snout=0):
    """Cabeza entera (máscaras y cabezas de bicho, con no_head): de frente y de espaldas un óvalo de top a low; de perfil,
    con el morro adelantado snout unidades."""
    if view == 'side':
        pts = [(18, low - 6), (6, 70), (4, 40), (16, top + 14), (44, top), (72, top + 8), (88 + snout * 0.4, 34), (92 + snout, 64), (88 + snout * 0.6, 86),
               (72, low), (44, low + 4)]
    else:
        pts = [(50 - w * 0.8, low - 6), (50 - w, 66), (50 - w, 40), (50 - w * 0.62, top + 12), (50, top), (50 + w * 0.62, top + 12), (50 + w, 40), (50 + w, 66),
               (50 + w * 0.8, low - 6), (50, low + 4)]
    out = [M(pts, c)]
    if shade:
        if view == 'side':
            out.append(L(blob([(6, 44), (24, 50), (34, low - 4), (16, low - 8), (6, 72)], 6), shade, 'b', False))
        else:
            out.append(L(blob([(58, top + 4), (50 + w * 0.85, 30), (50 + w, 64), (50 + w * 0.75, low - 6), (66, low - 2), (70, 40)], 6), shade, 'b', False))
    return out


def eyes2(ey=75, sep=14, rx=6, ry=7, iris=BLACK, ring_c=None, white=True):
    """Ojos redondos grandes dibujados como capas (para cabezas de bicho)."""
    out = []
    for cx in (50 - sep, 50 + sep):
        if ring_c:
            out.append(L(ell(cx, ey, rx + 2.4, ry + 2.4), ring_c, 'f', False))
        out.append(L(ell(cx, ey, rx, ry), WHITE if white else iris, 'f', True))
        if white:
            out.append(L(ell(cx, ey + 0.6, rx * 0.62, ry * 0.66), iris, 'f', False))
        out.append(L(ell(cx - rx * 0.28, ey - ry * 0.32, rx * 0.22, ry * 0.2), WHITE, 'f', False))
    return out


def eye2_side(ey=75, rx=4.6, ry=7, iris=BLACK, x=82, white=True):
    out = [L(ell(x, ey, rx, ry), WHITE if white else iris, 'f', True)]
    if white:
        out.append(L(ell(x + 1, ey + 0.6, rx * 0.62, ry * 0.66), iris, 'f', False))
    return out


def smile_l(y=92, w=8, c=OUTC, d=3, lw=1.6):
    return L(quad((50 - w, y - 1), (50, y + d), (50 + w, y - 1)), c, 'f', False, False, lw)


def frown_l(y=93, w=6, c=OUTC, lw=1.6):
    return L(quad((50 - w, y + 1.5), (50, y - 2), (50 + w, y + 1.5)), c, 'f', False, False, lw)


def tentacle(x, y, tx, ty, c, wd=5, z='b', tip=None):
    """Mechón grueso o tentáculo que cae de (x, y) a (tx, ty), con la punta redonda de otro color si tip."""
    mx, my = (x + tx) / 2, (y + ty) / 2
    out = [L(blob([(x - wd, y), (x + wd, y), (mx + wd * 0.9, my), (tx + wd * 0.6, ty), (tx, ty + wd * 0.6), (tx - wd * 0.6, ty), (mx - wd * 0.9, my)], 5), c, z)]
    if tip:
        out.append(L(ell(tx, ty, wd * 1.1, wd * 1.4), tip, z))
    return out


# ------------------------------------------------------------------ jugadores (hoja 0)

# Roleia Orbes: melena morada lisa y larguísima hasta el pecho, con raya en medio; una corona morada de cuernos hacia
# arriba con un rombo en la frente y una gema verde; orejas de elfo, ojos verde agua grandes con sombra morada
PU, PUD, GEM = _c('#7a50b8'), _c('#4c2e80'), _c('#3aa89a')
def _crown(view):
    if view == 'front':
        return [M([(12, 46), (6, -10, 1), (26, 12), (40, 4), (50, -8, 1), (60, 4), (74, 12), (94, -10, 1), (88, 46), (70, 40), (50, 56, 1), (30, 40)], PU, 'f'),
                M([(44, 16), (50, 4, 1), (56, 16), (50, 44, 1)], PUD, 'f', False), L(ell(50, 60, 1.8, 2.2), GEM, 'f', False)]
    if view == 'side':
        return [M([(30, 44), (24, 14), (36, 4), (40, -10, 1), (56, 6), (76, 14), (88, 26), (92, 44), (80, 48), (60, 40)], PU, 'f'),
                M([(84, 30), (92, 40), (88, 50)], PUD, 'f', False)]
    return [M([(12, 46), (6, -10, 1), (26, 12), (50, 4), (74, 12), (94, -10, 1), (88, 46), (50, 40)], PU, 'f')]
C('roleia-orbes', 'chica', P('#6a46a8', '#fbe0c4', iris='#2ea8a0'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=93, ears=False, hairline=[(8, 66), (20, 50), (50, 44), (80, 50), (92, 66)]),
  dome('front', top=6, w=46, cy=48, long=124, flare=6) + ears_pointy('front', h=14) + _crown('front') +
  [mark([(30, 70), (42, 68), (44, 72), (30, 74)], PUD), mark([(70, 70), (58, 68), (56, 72), (70, 74)], PUD)],
  dome('side', top=6, w=46, cy=48, long=124, flare=6) + ears_pointy('side', h=14) + _crown('side'),
  dome('back', top=6, w=46, cy=48, long=124, flare=6, ends=5) + _crown('back'))

HAT, HATD = _c('#3a3a3e'), _c('#1e1e22')


def _fedora(view, hat=HAT, bnd=HATD):
    """Sombrero de ala (el de Freddie Aster-Stayre de go_04, con colores propios)."""
    if view == 'front':
        return [M([(24, 38), (26, 8), (50, 0), (74, 8), (76, 38)], hat, 'f'), M([(26, 30), (74, 30), (75, 38), (25, 38)], bnd, 'f', False),
                L(ell(50, 40, 48, 9), hat, 'f', True, True), L(blob([(10, 42), (50, 46), (90, 42), (92, 46), (50, 50), (8, 46)], 4), bnd, 'f', False)]
    if view == 'side':
        return [M([(20, 36), (24, 6), (50, -2), (76, 6), (80, 36)], hat, 'f'), M([(22, 28), (78, 28), (79, 36), (21, 36)], bnd, 'f', False),
                L(ell(52, 38, 50, 7), hat, 'f', True, True)]
    return [M([(24, 40), (26, 10), (50, 2), (74, 10), (76, 40)], hat, 'f'), M([(26, 32), (74, 32), (75, 40), (25, 40)], bnd, 'f', False),
            L(ell(50, 42, 48, 9), hat, 'f', True, True)]


# Saber Sabel: sombrero de gánster negro con la cinta oscura; melena roja oscura por los lados hasta el cuello, en
# mechones; ojos azules, sonrisa de lado y algo de barba
RED = _c('#9a1e2a')
C('saber-sabel', 'normal', P('#9a1e2a', '#f2b884', iris='#3a6aa8'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=[(8, 62), (18, 48), (50, 44), (82, 48), (92, 62)]),
  [M([(10, 104, 1), (6, 70), (10, 40), (90, 40), (94, 70), (90, 104, 1), (84, 92), (82, 56), (18, 56), (16, 92)])] + _fedora('front') +
  [strand([(14, 60), (12, 90)], 'deep', 'b', 1.0), strand([(86, 60), (88, 90)], 'deep', 'b', 1.0)],
  [M([(60, 52), (70, 42), (40, 38), (8, 42), (2, 70), (6, 100, 1), (22, 90), (30, 104, 1), (40, 84), (46, 66)])] + _fedora('side'),
  [M([(8, 104, 1), (4, 70), (8, 40), (92, 40), (96, 70), (92, 104, 1), (76, 96), (66, 106, 1), (50, 96), (34, 106, 1), (24, 96)])] + _fedora('back'))

# Sad Sajord: pelo morado largo peinado a su derecha que le tapa media cara (la mitad derecha de la imagen queda al
# aire, con frente alta); piel muy clara, un ojo azul a la vista, sonrisa
C('sad-sajord', 'delgado', P('#9a70c0', '#f8e4c8', iris='#4a8ac0'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=94, eye_sep=14, hairline=False, face_front=face(chin=104, top=20)),
  [M([(6, 100), (2, 60), (12, 20), (40, 4), (66, 8), (80, 20), (70, 30), (60, 56), (56, 84), (50, 100, 1), (40, 104), (22, 108, 1)]),
   M([(46, 8), (66, 10), (78, 22), (64, 30), (54, 60), (50, 90), (44, 60)], 'shade', 'f', False),
   M([(6, 100), (2, 60), (12, 22), (36, 8), (52, 14), (56, 40), (52, 70), (50, 100, 1), (40, 104), (22, 108, 1)], 'mid', 'f')],
  [M([(60, 34), (76, 20), (66, 6), (40, 2), (14, 14), (2, 46), (4, 90), (16, 108, 1), (30, 92), (40, 74), (48, 56)])],
  [M([(6, 100), (2, 60), (12, 20), (40, 4), (66, 8), (88, 22), (96, 56), (90, 92), (70, 104, 1), (50, 96), (22, 108, 1)])])

# Salicy Lic: pelo morado con dos rulos enormes arriba que forman un lazo, y ondas que caen por los lados hasta el cuello;
# orejas de elfo, cejas fruncidas, ojos negros grandes y boquita enfadada
SL = _c('#8a68a8')
def _loops(view):
    if view == 'side':
        return [L(ell(44, 6, 22, 14), SL), L(ell(44, 6, 10, 6), 'shade', 'b', False)]
    return [L(ell(26, 8, 22, 14), SL), L(ell(74, 8, 22, 14), SL), L(ell(26, 8, 10, 6), 'shade', 'b', False), L(ell(74, 8, 10, 6), 'shade', 'b', False)]
C('salicy-lic', 'chica', P('#8a68a8', '#fbe0c8', iris='#2a2a30'),
  F(eyes='big', brows='angry', mouth='frown', mouth_y=94, ears=False, hairline=[(8, 62), (20, 46), (34, 40), (50, 48), (66, 40), (80, 46), (92, 62)]),
  _loops('front') + dome('front', top=8, w=44, cy=48, sb=72) + ears_pointy('front', h=10) +
  tentacle(14, 60, 14, 98, SL, 7) + tentacle(86, 60, 86, 98, SL, 7),
  _loops('side') + dome('side', top=8, w=44, cy=48, nape=96) + ears_pointy('side', h=10),
  _loops('back') + dome('back', top=8, w=44, cy=48, long=100, flare=4))

# Sambas Soya: melena negra en casco con flequillo recto y dos puntas como orejas de gato arriba; las puntas de abajo
# grises; piel azul clara, ojos verdes afilados y boca seria
SB = _c('#1e2426')
def _cat_tips(view):
    if view == 'side':
        return [M([(30, 14), (36, -10, 1), (52, 10)], SB)]
    return [M([(14, 30), (16, -8, 1), (36, 12)], SB), M([(86, 30), (84, -8, 1), (64, 12)], SB)]
C('sambas-soya', 'normal', P('#1e2426', '#a8dcec', iris='#2a8a4a', light='#9a9aa0'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=93, hairline=[(8, 60), (16, 62), (84, 62), (92, 60)]),
  _cat_tips('front') + [M([(12, 104), (6, 64), (10, 30), (30, 10), (50, 4), (70, 10), (90, 30), (94, 64), (88, 104), (82, 62), (18, 62)]),
                        M([(8, 90), (14, 88), (16, 106), (8, 106)], 'light', 'b', False), M([(92, 90), (86, 88), (84, 106), (92, 106)], 'light', 'b', False)],
  _cat_tips('side') + [M([(80, 62), (88, 40), (80, 14), (54, 2), (26, 8), (8, 26), (2, 60), (6, 100), (30, 104), (46, 86), (56, 66)]),
                       M([(4, 90), (30, 94), (30, 104), (6, 102)], 'light', 'b', False)],
  _cat_tips('back') + [M([(8, 104), (4, 64), (10, 30), (30, 10), (50, 4), (70, 10), (90, 30), (96, 64), (92, 104), (50, 108)]),
                       M([(6, 92), (94, 92), (92, 106), (50, 110), (8, 106)], 'light', 'b', False)])

# Schemer Guile: señor mayor con una mata enorme de pelo gris que sale en pinchos hacia los lados; barba gris tupida
# alrededor de toda la cara; gafas naranjas en visera, ceño fruncido y un auricular en la oreja
GR, OR = _c('#9a96a8'), _c('#f08a1e')
C('schemer-guile', 'corpulento', P('#9a96a8', '#c4864e', iris='#2a1e1a'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=96, face_front=face(w=2, chin=104),
    hairline=[(8, 60), (24, 48), (40, 56), (50, 46), (60, 56), (76, 48), (92, 60)]),
  dome('front', top=-6, w=52, cy=42, n=11, amp=14, sb=74, seed=3) +
  [M([(16, 70), (6, 80, 1), (16, 96), (30, 110), (50, 116, 1), (70, 110), (84, 96), (94, 80, 1), (84, 70), (78, 90), (64, 98), (50, 96), (36, 98), (22, 90)], GR, 'f'),
   M([(22, 70), (30, 66), (46, 70), (50, 74), (54, 70), (70, 66), (78, 70), (74, 80), (56, 80), (50, 77), (44, 80), (26, 80)], OR, 'f'),
   L([(24, 72), (76, 72)], OUTC, 'f', False, False, 1.4), L(blob([(8, 78), (14, 74), (26, 88), (22, 92)], 4), _c('#d8e0f0'), 'f')],
  dome('side', top=-6, w=50, cy=42, n=11, amp=14, nape=90, seed=3) +
  [M([(56, 72), (70, 84), (84, 92), (86, 104), (72, 110), (54, 100), (46, 84)], GR, 'f'), M([(70, 68), (92, 68), (90, 80), (72, 80)], OR, 'f')],
  dome('back', top=-6, w=52, cy=42, n=11, amp=14, nape=92, seed=3))

# Sena Arata: pelo naranja de pinchos revueltos, ojos azul oscuro grandes y la boca abierta de alegría (sprite de la DS)
C('sena-arata', 'normal', P('#e8661e', '#f6d0a4', iris='#3a3a8a'),
  F(eyes='big', brows=True, mouth='grin', mouth_y=94, hairline=hl(5, 62, 48, 58, jit=3, seed=2)),
  dome('front', top=2, w=48, cy=44, n=11, amp=10, sb=66, seed=5),
  dome('side', top=2, w=46, cy=44, n=11, amp=10, nape=86, seed=5),
  dome('back', top=2, w=48, cy=44, n=11, amp=10, nape=86, seed=5))

# Senna Regan (portera): cabeza de bicho rosa salmón con la cara blanca, dos ojazos marrones redondos, mofletes rosas y
# labios; dos orejas largas como de conejo caídas hasta los hombros con la punta oscura
SAL, SALD, TIPD = _c('#f0a090'), _c('#d07c70'), _c('#5a5040')
def _senna(view):
    if view == 'front':
        return (head('front', SAL, top=-2, w=44, low=104) + tentacle(10, 50, 4, 118, SAL, 9, tip=TIPD) + tentacle(90, 50, 96, 118, SAL, 9, tip=TIPD) +
                [L(blob([(14, 92), (20, 50), (50, 40), (80, 50), (86, 92), (66, 104), (34, 104)], 6), _c('#faf4ee'), 'f')] +
                eyes2(66, 18, 9, 10, _c('#6a2a1e')) + [L(ell(26, 84, 5, 4), _c('#f4a0a0'), 'f', False), L(ell(74, 84, 5, 4), _c('#f4a0a0'), 'f', False),
                                                        L(blob([(42, 92), (50, 90), (58, 92), (50, 96)], 4), _c('#e09080'), 'f')])
    if view == 'side':
        return (head('side', SAL, top=-2, low=104, snout=2) + tentacle(30, 50, 24, 118, SAL, 9, tip=TIPD) +
                [L(blob([(60, 50), (88, 46), (94, 70), (88, 96), (66, 102)], 6), _c('#faf4ee'), 'f')] + eye2_side(66, 5, 9, _c('#6a2a1e'), x=84))
    return head('back', SAL, top=-2, w=44, low=104, shade=SALD) + tentacle(10, 50, 4, 118, SAL, 9, tip=TIPD) + tentacle(90, 50, 96, 118, SAL, 9, tip=TIPD)
C('senna-regan', 'chica', P('#f0a090', '#faf4ee'), F(**NOFACE), _senna('front'), _senna('side'), _senna('back'))

# ------------------------------------------------------------------ hoja 1

# Seraph Sharpe: pelo castaño corto y peinado con raya a un lado, gafas redondas de montura dorada, piel tostada, sonrisa
C('seraph-sharpe', 'normal', P('#7a4a26', '#e8a466', iris='#3a5a3a'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=93, hairline=[(8, 62), (16, 52), (30, 42), (60, 44), (84, 52), (92, 62)]),
  crop('front', top=0, side=64) + ring_glasses('front', c=_c('#a07838'), w=2.2),
  crop('side', top=0) + ring_glasses('side', c=_c('#a07838'), w=2.2),
  crop('back', top=0))

# Seth Yinkley: alienígena de piel azul clara con orejas grandes grises; gorro azul con una franja blanca y una banda
# amarilla de gafas, y un moño azul oscuro encima; ojos grandes verde azulado y una sonrisa ancha
BL, BLD, YL = _c('#2a5aa8'), _c('#1e2e5a'), _c('#f0d040')
def _seth_cap(view):
    if view == 'side':
        return [cap('side', BL, top=4, rim=52, w=46), M([(40, 4), (52, 4), (52, 50), (40, 52)], WHITE, 'b', False),
                M([(56, 44), (94, 40), (94, 52), (58, 56)], YL, 'f'), L(blob([(30, 2), (44, -14), (56, -6), (52, 6)], 5), BLD)]
    out = [cap(view, BL, top=4, rim=52, w=46), M([(42, 6), (58, 6), (58, 50), (42, 50)], WHITE, 'b', False)]
    if view == 'front':
        out.append(M([(18, 50), (50, 42), (82, 50), (80, 60), (50, 54), (20, 60)], YL, 'f'))
    out.append(L(blob([(38, 4), (42, -12), (50, -18), (60, -10), (62, 4)], 5), BLD))
    return out
C('seth-yinkley', 'normal', P('#2a5aa8', '#a8d8ec', iris='#1e6a6a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, big_ears=4, ear_out=4),
  _seth_cap('front') + eyes2(76, 15, 7.5, 8, _c('#1e6a6a')) + [L(quad((30, 90), (50, 100), (70, 90)), OUTC, 'f', False, False, 1.6)],
  _seth_cap('side') + eye2_side(76, 5, 8, _c('#1e6a6a')) + [L([(78, 94), (88, 92)], OUTC, 'f', False, False, 1.6)],
  _seth_cap('back'))

# Seyon Shore (portero): casco de seta gris oscuro con lunares azules que le tapa hasta los ojos; piel gris, ojos azules
# afilados y boca recta
MG, MB = _c('#4a4a52'), _c('#2a8ad0')
def _mush(view):
    if view == 'side':
        pts = arc(48, 62, 52, 66, 180, 0) + [(100, 66), (50, 70), (-4, 66)]
        return [M(pts, MG, 'f'), L(ell(30, 30, 10, 8), MB, 'f', False), L(ell(66, 24, 10, 8), MB, 'f', False), L(ell(86, 52, 6, 6), MB, 'f', False)]
    pts = arc(50, 62, 54, 66, 180, 0) + [(104, 66), (50, 72), (-4, 66)]
    out = [M(pts, MG, 'f')]
    for x, y, r in ((16, 46, 9), (38, 20, 10), (62, 20, 10), (84, 46, 9), (50, 50, 8)) if view == 'front' else ((20, 30, 10), (50, 14, 10), (80, 30, 10), (50, 48, 9)):
        out.append(L(ell(x, y, r, r * 0.8), MB, 'f', False))
    return out
C('seyon-shore', 'normal', P('#4a4a52', '#a4a4ac', iris='#2a8ad0'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=94, hairline=False),
  _mush('front'), _mush('side'), _mush('back'))

# Shaurashaula Toxbarb: melena roja salmón en mechones gruesos como tentáculos que le enmarcan la cara hasta los hombros;
# piel morena con marcas blancas (una en la frente y puntos en las mejillas); ojos granates grandes
TX = _c('#d05048')
C('shaurashaula-toxbarb', 'chica', P('#d05048', '#b07858', iris='#8a2a40'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=94, hairline=[(8, 60), (20, 44), (36, 50), (50, 40), (64, 50), (80, 44), (92, 60)]),
  dome('front', top=2, w=48, cy=46, long=108, flare=8) + tentacle(12, 62, 10, 104, TX, 7) + tentacle(88, 62, 90, 104, TX, 7) +
  [mark([(46, 54), (54, 54), (52, 62), (48, 62)], WHITE), mark([(22, 84), (28, 82), (28, 88)], WHITE), mark([(78, 84), (72, 82), (72, 88)], WHITE)],
  dome('side', top=2, w=46, cy=46, long=108, flare=8) + [mark([(82, 84), (88, 82), (88, 88)], WHITE)],
  dome('back', top=2, w=48, cy=46, long=108, flare=8, ends=5))

# Shawby Ehan: cara enorme amarillo pálido de tortuga triste dentro de una capucha blanca de orejas largas caídas; gorra
# morada con un ojo dorado bordado; pañuelo morado al cuello; ojos caídos tristes y boca recta
TW, TWD, PV = _c('#f4f0ec'), _c('#c8bcbc'), _c('#7a4ab0')
def _shawby(view):
    if view == 'front':
        return [M([(4, 112), (0, 70), (6, 34), (30, 18), (70, 18), (94, 34), (100, 70), (96, 112), (82, 108), (84, 70), (16, 70), (18, 108)], TW),
                M([(10, 110), (8, 70), (12, 44), (16, 40), (18, 106)], TWD, 'b', False), M([(90, 110), (92, 70), (88, 44), (84, 40), (82, 106)], TWD, 'b', False),
                L(blob([(14, 96), (12, 54), (30, 32), (70, 32), (88, 54), (86, 96), (64, 108), (36, 108)], 6), _c('#f4ecb8'), 'f'),
                M([(18, 30), (16, 10), (50, 2), (84, 10), (82, 30), (90, 34), (10, 34)], PV, 'f'), L(ell(50, 18, 6, 4), YL, 'f', False),
                L(quad((26, 70), (34, 66), (42, 72)), OUTC, 'f', False, False, 2.0), L(quad((58, 72), (66, 66), (74, 70)), OUTC, 'f', False, False, 2.0),
                L(quad((30, 76), (34, 78), (38, 76)), OUTC, 'f', False, False, 1.4), L(quad((62, 76), (66, 78), (70, 76)), OUTC, 'f', False, False, 1.4),
                L([(42, 94), (58, 94)], OUTC, 'f', False, False, 1.6)] + scarf('front', PV, y=104, h=10)
    if view == 'side':
        return [M([(10, 112), (2, 70), (8, 30), (36, 14), (70, 16), (84, 30), (76, 60), (60, 70), (40, 110)], TW),
                L(blob([(56, 34), (86, 30), (96, 60), (92, 96), (70, 104), (56, 80)], 6), _c('#f4ecb8'), 'f'),
                M([(30, 28), (34, 6), (62, 2), (84, 12), (90, 30)], PV, 'f'),
                L(quad((76, 68), (82, 66), (88, 70)), OUTC, 'f', False, False, 2.0)] + scarf('side', PV, y=104, h=10)
    return [M([(4, 112), (0, 70), (6, 34), (30, 18), (70, 18), (94, 34), (100, 70), (96, 112), (50, 116)], TW),
            M([(18, 30), (16, 10), (50, 2), (84, 10), (82, 30)], PV, 'f')] + scarf('back', PV, y=104, h=10)
C('shawby-ehan', 'normal', P('#f4f0ec', '#f4ecb8'), F(**NOFACE), _shawby('front'), _shawby('side'), _shawby('back'))

# Shiro Hatch: piel azul clara; pelo naranja rizado que se abre en dos nubes a los lados a la altura del cuello; una
# diadema roja con tres gemas sobre la frente; cejas naranjas y ojos granates
RJ, RJD = _c('#c8202a'), _c('#7a1018')
def _gems(view):
    if view == 'side':
        return [M([(44, 10), (84, 18), (90, 30), (50, 26)], RJ, 'f'), L(ell(88, 30, 4.4, 5), RJD, 'f')]
    return [M([(20, 34), (30, 16), (50, 6), (70, 16), (80, 34), (66, 26), (50, 22), (34, 26)], RJ, 'f'),
            L(ell(50, 16, 7, 8), RJD, 'f'), L(ell(28, 30, 5, 5.5), RJD, 'f'), L(ell(72, 30, 5, 5.5), RJD, 'f')]
C('shiro-hatch', 'chica', P('#f0884a', '#a8d8f0', iris='#8a2a2a'),
  F(eyes='sharp', brows=True, mouth='frown', mouth_y=94, hairline=[(8, 58), (20, 40), (50, 34), (80, 40), (92, 58)]),
  dome('front', top=4, w=44, cy=44, sb=70) +
  [L(blob([(-8, 94), (0, 80), (14, 76), (20, 94), (12, 104), (0, 102)], 5), 'mid'), L(blob([(108, 94), (100, 80), (86, 76), (80, 94), (88, 104), (100, 102)], 5), 'mid')] + _gems('front'),
  dome('side', top=4, w=44, cy=44, nape=86) + [L(blob([(8, 80), (24, 74), (34, 94), (20, 106), (2, 98)], 5), 'mid')] + _gems('side'),
  dome('back', top=4, w=44, cy=44, nape=86) + [L(blob([(-8, 94), (10, 76), (50, 84), (90, 76), (108, 94), (90, 106), (50, 100), (10, 106)], 5), 'mid')] + _gems('back'))

# Shuse Keylor (portero): cabeza de máquina: una caja azul con una pantalla que muestra los ojos en X y la boca de puntos
BX, BXD, SCR = _c('#4a70c0'), _c('#2a4a8a'), _c('#dce8f0')
def _box(view):
    if view == 'side':
        return [M([(2, 100, 1), (4, 6, 1), (90, 4, 1), (92, 100, 1)], BX), M([(70, 6), (90, 4), (92, 100), (70, 100)], BXD, 'f', False),
                M([(36, 4), (48, 4), (48, -6), (36, -6)], BXD)]
    out = [M([(2, 102, 1), (4, 4, 1), (96, 4, 1), (98, 102, 1)], BX), M([(42, 4), (58, 4), (58, -6), (42, -6)], BXD)]
    if view == 'front':
        out += [M([(14, 90, 1), (14, 22, 1), (86, 22, 1), (86, 90, 1)], SCR, 'f'),
                L([(24, 38), (40, 54)], BLACK, 'f', False, False, 3.6), L([(40, 38), (24, 54)], BLACK, 'f', False, False, 3.6),
                L([(60, 38), (76, 54)], BLACK, 'f', False, False, 3.6), L([(76, 38), (60, 54)], BLACK, 'f', False, False, 3.6),
                L([(24, 76), (76, 76)], BLACK, 'f', False, False, 3.0)]
    return out
C('shuse-keylor', 'normal', P('#4a70c0', '#4a70c0'), F(**NOFACE), _box('front'), _box('side'), _box('back'))

# Sierra Mone (portera): pelo gris oscuro pegado en casquete, del que salen tentáculos largos con la punta blanca en bola;
# piel verde muy clara, ojos granates afilados y ceño
SG, SW = _c('#5a5860'), _c('#ece8f0')
C('sierra-mone', 'chica', P('#5a5860', '#c8ecdc', iris='#8a2040'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(8, 62), (18, 46), (50, 38), (82, 46), (92, 62)]),
  crop('front', top=0, side=74) + tentacle(14, 70, 2, 104, SG, 5, tip=SW) + tentacle(86, 70, 104, 92, SG, 5, tip=SW) + tentacle(84, 76, 92, 112, SG, 4, tip=SW),
  crop('side', top=0) + tentacle(24, 70, 10, 108, SG, 5, tip=SW),
  crop('back', top=0) + tentacle(16, 74, 0, 106, SG, 5, tip=SW) + tentacle(84, 74, 100, 106, SG, 5, tip=SW))

# ------------------------------------------------------------------ hoja 2

# Silas Kaye: máscara de pájaro crema con dos orejas planas hacia arriba con agujero, pico grande y ojos marcados en
# granate (uno guiñado); pañuelo granate y verde azulado al cuello
CRM, CRMD, BEAK, MR = _c('#f6eed4'), _c('#d8ccaa'), _c('#c8a88a'), _c('#9a4a3a')
def _silas(view):
    if view == 'front':
        return (head('front', CRM, top=4, w=44, low=104) +
                [M([(20, 30), (2, 2), (8, -10, 1), (32, 16)], CRM), M([(80, 30), (98, 2), (92, -10, 1), (68, 16)], CRM),
                 L(ell(10, 0, 3, 3), CRMD, 'b', False), L(ell(90, 0, 3, 3), CRMD, 'b', False),
                 mark([(20, 66), (40, 62), (40, 90), (30, 96), (22, 84)], MR), mark([(80, 66), (60, 62), (60, 90), (70, 96), (78, 84)], MR)] +
                eyes2(74, 16, 5.5, 6, BLACK) + [M([(40, 70), (60, 70), (50, 102, 1)], BEAK, 'f')] + scarf('front', MR, y=104, h=12))
    if view == 'side':
        return (head('side', CRM, top=4, low=104) + [M([(30, 24), (20, -8, 1), (48, 16)], CRM), mark([(70, 64), (88, 62), (86, 88)], MR)] +
                eye2_side(74, 4.4, 6) + [M([(84, 70), (106, 92, 1), (82, 90)], BEAK, 'f')] + scarf('side', MR, y=104, h=12))
    return head('back', CRM, top=4, w=44, low=104, shade=CRMD) + [M([(20, 30), (4, -8, 1), (32, 16)], CRM), M([(80, 30), (96, -8, 1), (68, 16)], CRM)] + \
        scarf('back', MR, y=104, h=12)
C('silas-kaye', 'normal', P('#f6eed4', '#f6eed4'), F(**NOFACE), _silas('front'), _silas('side'), _silas('back'))

# Silica Gel: melena verde azulada larga y ondulada con raya en medio, recogida a los lados en dos rodetes oscuros a la
# altura de las orejas; orejas de elfo, ojos oscuros grandes y sonrisa
TEAL, TEALD = _c('#5aa0a8'), _c('#2e5a60')
C('silica-gel', 'chica', P('#5aa0a8', '#fbe0c4', iris='#2a1e1e'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, ears=False, hairline=[(8, 66), (22, 48), (46, 40), (50, 46), (54, 40), (78, 48), (92, 66)]),
  [L(ell(8, 74, 12, 12), TEALD), L(ell(92, 74, 12, 12), TEALD)] + dome('front', top=4, w=44, cy=48, long=110, flare=4) + ears_pointy('front', h=12) +
  tentacle(16, 70, 18, 108, TEAL, 6, z='f') + tentacle(84, 70, 82, 108, TEAL, 6, z='f'),
  [L(ell(30, 76, 12, 12), TEALD)] + dome('side', top=4, w=44, cy=48, long=110, flare=4) + ears_pointy('side', h=12),
  [L(ell(8, 74, 12, 12), TEALD), L(ell(92, 74, 12, 12), TEALD)] + dome('back', top=4, w=44, cy=48, long=110, flare=4, ends=5))

# Silt Deigan: cabeza de rana naranja con manchas claras, ojos negros redondos y una boca enorme blanca; encima dos moños
# castaños de afro con gomas rojas
FRG, FRGD, AFR = _c('#f0943a'), _c('#c86a24'), _c('#7a5a2a')
def _frog(view):
    if view == 'front':
        return ([L(ell(22, 6, 16, 15), AFR), L(ell(78, 6, 16, 15), AFR), M([(28, 18), (32, 14), (36, 30), (32, 32)], RJ), M([(72, 18), (68, 14), (64, 30), (68, 32)], RJ)] +
                head('front', FRG, top=20, w=46, low=104) + [L(ell(50, 32, 6, 4), _c('#f8d098'), 'f', False), L(ell(14, 70, 6, 8), _c('#f8d098'), 'f', False),
                                                             L(ell(86, 70, 6, 8), _c('#f8d098'), 'f', False)] +
                eyes2(60, 16, 6, 7) + [L(blob([(18, 74), (50, 72), (82, 74), (74, 92), (50, 98), (26, 92)], 6), WHITE, 'f'),
                                       L(quad((18, 74), (50, 84), (82, 74)), OUTC, 'f', False, False, 1.4)])
    if view == 'side':
        return ([L(ell(44, 8, 16, 15), AFR), M([(48, 20), (52, 18), (54, 32), (48, 32)], RJ)] + head('side', FRG, top=20, low=104, snout=6) +
                eye2_side(60, 4.4, 7) + [L(blob([(70, 76), (98, 72), (92, 92), (72, 92)], 5), WHITE, 'f')])
    return [L(ell(22, 6, 16, 15), AFR), L(ell(78, 6, 16, 15), AFR)] + head('back', FRG, top=20, w=46, low=104, shade=FRGD)
C('silt-deigan', 'normal', P('#f0943a', '#f0943a'), F(**NOFACE), _frog('front'), _frog('side'), _frog('back'))

# Skie Blue: melena azul marino muy oscura en media melena, con flequillo recto y las puntas hacia fuera bajo la
# mandíbula; ojos azules grandes, sonrisa
C('skie-blue', 'chica', P('#24384a', '#fbe0c8', iris='#3a7ac0'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=[(8, 60), (18, 60), (82, 60), (92, 60)]),
  [M([(6, 100, 1), (8, 70), (8, 36), (28, 10), (50, 4), (72, 10), (92, 36), (92, 70), (94, 100, 1), (84, 94), (82, 60), (18, 60), (16, 94)])],
  [M([(80, 60), (88, 40), (80, 14), (54, 2), (26, 8), (6, 30), (2, 70), (6, 100, 1), (24, 96), (40, 100, 1), (50, 80), (60, 62)])],
  [M([(6, 100, 1), (6, 66), (8, 34), (28, 10), (50, 4), (72, 10), (92, 34), (94, 66), (94, 100, 1), (72, 96), (50, 100), (28, 96)])])

# Skip Flashman: gorro de lana crema calado; asoma el pelo castaño en flequillo de mechones y por los lados; piel
# tostada, ojos negros y boca seria
BEA, BEAD = _c('#f2e8cc'), _c('#d4c8a4')
def _beanie(view):
    out = [cap(view, BEA, top=-4, rim=50, w=48, drop=10)]
    if view == 'front':
        out.append(M([(4, 46), (50, 40), (96, 46), (96, 56), (50, 50), (4, 56)], BEAD, 'f'))
    elif view == 'side':
        out.append(M([(0, 54), (94, 40), (95, 50), (2, 64)], BEAD, 'f'))
    return out
C('skip-flashman', 'normal', P('#4a3022', '#e8a868', iris='#1e1414'),
  F(eyes='normal', brows='angry', mouth='frown', mouth_y=94, hairline=[(8, 62), (16, 58), (28, 66), (40, 56), (52, 66), (64, 56), (76, 64), (84, 58), (92, 62)]),
  [M([(10, 74, 1), (8, 50), (92, 50), (92, 74, 1), (84, 66), (80, 56), (20, 56), (16, 66)])] + _beanie('front'),
  [M([(66, 56), (88, 46), (20, 46), (4, 56), (8, 80), (24, 84), (40, 66)])] + _beanie('side'),
  [M([(8, 78), (8, 50), (92, 50), (92, 78), (50, 86)])] + _beanie('back'))

# Skoll Pion: casco de escorpión rojo de placas, con dos cuernos arriba y dos pinzas que bajan por los lados; puntas
# moradas; cara rosada pálida, ojos naranjas redondos con aro, mechones rosas a los lados y sonrisa
SC, SCD, SCP = _c('#b02a2a'), _c('#7a1a1a'), _c('#6a4aa0')
def _scorp(view):
    if view == 'front':
        return [M([(10, 70), (4, 36), (16, 14), (22, -12, 1), (34, 8), (50, 4), (66, 8), (78, -12, 1), (84, 14), (96, 36), (90, 70), (80, 58), (20, 58)], SC),
                L([(20, 40), (80, 40)], SCD, 'b', False, False, 1.6), L([(16, 28), (84, 28)], SCD, 'b', False, False, 1.6),
                M([(4, 40), (-4, 30, 1), (-6, 52)], SCP), M([(96, 40), (104, 30, 1), (106, 52)], SCP)] + \
            tentacle(10, 66, 4, 104, SC, 6, tip=SC) + tentacle(90, 66, 96, 104, SC, 6, tip=SC) + \
            [M([(20, 62), (26, 60), (28, 100), (20, 98)], _c('#f0a0a8'), 'f'), M([(80, 62), (74, 60), (72, 100), (80, 98)], _c('#f0a0a8'), 'f')]
    if view == 'side':
        return [M([(70, 58), (86, 40), (80, 14), (66, -12, 1), (54, 6), (24, 8), (6, 30), (2, 64), (10, 90), (30, 84), (44, 62)], SC),
                M([(14, 40), (4, 26, 1), (0, 52)], SCP)] + tentacle(30, 70, 22, 106, SC, 6, tip=SC)
    return [M([(10, 74), (4, 36), (16, 14), (22, -12, 1), (34, 8), (50, 4), (66, 8), (78, -12, 1), (84, 14), (96, 36), (90, 74), (50, 86)], SC),
            L([(14, 40), (86, 40)], SCD, 'b', False, False, 1.6), L([(10, 58), (90, 58)], SCD, 'b', False, False, 1.6)] + \
        tentacle(10, 70, 4, 104, SC, 6, tip=SC) + tentacle(90, 70, 96, 104, SC, 6, tip=SC)
C('skoll-pion', 'chica', P('#b02a2a', '#f8e4ec', iris='#e0901e'),
  F(eyes='round', brows=False, mouth='smile', mouth_y=94, hairline=[(8, 60), (16, 62), (84, 62), (92, 60)]),
  _scorp('front') + [L(ell(36, 75, 7, 7), _c('#e0901e'), 'b', False), L(ell(64, 75, 7, 7), _c('#e0901e'), 'b', False)],
  _scorp('side'), _scorp('back'))

# Smeba Myko: capucha blanca con dos orejas largas de punta con manchas lilas, que baja por los lados de la cara; cara
# blanca con sombras lilas sobre los ojos verde agua, sonrisa
SM, SML = _c('#f4f0f6'), _c('#b8a0d8')
def _smeba(view):
    spikes = [M([(18, 20), (8, -22, 1), (34, 6)], SM), M([(82, 20), (92, -22, 1), (66, 6)], SM),
              L(ell(14, -6, 3.6, 8), SML, 'b', False), L(ell(86, -6, 3.6, 8), SML, 'b', False)]
    if view == 'front':
        return spikes + hood('front', SM, top=0, low=112, rim=_c('#ddd4e6'),
                             face_hole=[(22, 104), (18, 72), (22, 50), (50, 42), (78, 50), (82, 72), (78, 104), (50, 108)]) + \
            [L(ell(8, 104, 4, 8), SML, 'f', False), L(ell(92, 104, 4, 8), SML, 'f', False)]
    if view == 'side':
        return [M([(40, 20), (30, -22, 1), (54, 6)], SM), L(ell(36, -6, 3.6, 8), SML, 'b', False)] + hood('side', SM, top=0, rim=_c('#ddd4e6'))
    return spikes + hood('back', SM, top=0, low=112, rim=_c('#ddd4e6'))
C('smeba-myko', 'chica', P('#f4f0f6', '#fbf6fa', iris='#3ab8a8'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, ears=False, hairline=[(8, 50), (20, 44), (80, 44), (92, 50)]),
  _smeba('front') + [mark([(26, 64), (42, 62), (44, 66), (28, 70)], SML), mark([(74, 64), (58, 62), (56, 66), (72, 70)], SML)],
  _smeba('side'), _smeba('back'))

# Sofu Tokrim: la cabeza es un helado de nata en espiral blanco rosado, con la lengua azul fuera
ICE, ICED, TNG = _c('#f6eae6'), _c('#d8b0aa'), _c('#4aa8e0')
def _ice(view):
    xs = 0 if view != 'side' else -4
    out = [M([(4 + xs, 108), (0 + xs, 80), (8 + xs, 56), (14 + xs, 34), (30 + xs, 12), (52 + xs, 0), (66 + xs, -14), (70 + xs, -6), (62 + xs, 8), (84 + xs, 22),
              (92 + xs, 46), (100 + xs, 72), (98 + xs, 108)], ICE)]
    for y, a in ((28, 30), (52, 40), (76, 48), (98, 50)):
        out.append(L(quad((50 - a + xs, y + 6), (50 + xs, y - 4), (50 + a + xs, y + 6)), ICED, 'b', False, False, 2.0))
    if view == 'front':
        out += [L(blob([(44, 64), (58, 62), (60, 82), (52, 90), (44, 84)], 5), TNG, 'f'), L([(52, 66), (52, 80)], _c('#2a78b0'), 'f', False, False, 1.0)]
    elif view == 'side':
        out.append(L(blob([(86, 64), (100, 66), (98, 84), (88, 80)], 5), TNG, 'f'))
    return out
C('sofu-tokrim', 'chica', P('#f6eae6', '#f6eae6'), F(**NOFACE), _ice('front'), _ice('side'), _ice('back'))

# ------------------------------------------------------------------ hoja 3

# Solton Benvan: sombrero enorme de seta, ala ancha azul marino oscuro por encima y marrón por debajo, con la copa roja;
# pelo rubio platino corto que asoma a los lados; ojos verde agua grandes y boca abierta sonriente
NAV, BRN, RDT = _c('#24223a'), _c('#9a7060'), _c('#a02a2a')
def _shroom(view):
    if view == 'side':
        return [L(ell(50, 40, 56, 10), BRN, 'f'), M([(0, 38), (20, 20), (50, 12), (80, 20), (104, 38), (50, 44)], NAV, 'f'),
                M([(34, 14), (40, 0), (60, 0), (66, 14)], RDT, 'f')]
    return [L(ell(50, 44, 58, 12), BRN, 'f'), M([(-8, 40), (18, 22), (50, 12), (82, 22), (108, 40), (50, 46)], NAV, 'f'),
            M([(32, 16), (38, 0), (50, -4), (62, 0), (68, 16)], RDT, 'f')]
C('solton-benvan', 'chica', P('#e4dcc8', '#fbe0c4', iris='#2a9a9a'),
  F(eyes='big', brows='angry', mouth='grin', mouth_y=94, hairline=[(8, 60), (20, 54), (80, 54), (92, 60)]),
  [M([(12, 92, 1), (8, 60), (14, 44), (86, 44), (92, 60), (88, 92, 1), (82, 70), (78, 56), (22, 56), (18, 70)])] + _shroom('front'),
  [M([(60, 54), (70, 46), (20, 46), (6, 60), (8, 90, 1), (26, 86), (40, 66)])] + _shroom('side'),
  [M([(10, 92, 1), (8, 56), (92, 56), (90, 92, 1), (50, 90)])] + _shroom('back'))

# Sonny Raimon: adulto de cara larga con el pelo verde oscuro muy corto en cepillo plano y una coletita atrás; gafas de
# montura gris, perilla fina y bigote en ancla; piel tostada
DG = _c('#3e4a32')
C('sonny-raimon', 'delgado', P('#3e4a32', '#d89a5e', iris='#2a2a2a'),
  F(eyes='dot', brows=True, mouth='line', mouth_y=94, face_front=face(chin=106, top=22),
    hairline=[(8, 58), (16, 46), (30, 40), (70, 40), (84, 46), (92, 58)]),
  crop('front', top=-2, side=60, flat=10) + ring_glasses('front', c=_c('#9a9aa8'), w=2.0, rx=9, ry=6) +
  [L([(42, 90), (50, 88), (58, 90)], DG, 'f', False, False, 1.6), L([(50, 94), (50, 106)], DG, 'f', False, False, 2.0)],
  crop('side', top=-2, flat=10) + ring_glasses('side', c=_c('#9a9aa8'), w=2.0) + [L(blob([(6, 54), (-6, 50), (-10, 60), (0, 64)], 4), DG),
                                                                               L([(84, 96), (82, 106)], DG, 'f', False, False, 2.0)],
  crop('back', top=-2, flat=10) + [L(blob([(44, 60), (56, 60), (58, 74), (50, 80), (42, 74)], 4), DG, 'f')])

# Sugaken: pelo castaño corto de pinchos de punta, piel tostada y ojos negros (sprite de la DS)
C('sugaken', 'normal', P('#6a4026', '#e0a86a', iris='#1e1414'),
  F(eyes='dot', brows=True, mouth='line', mouth_y=93, hairline=hl(5, 62, 50, 58, jit=2, seed=4)),
  dome('front', top=4, w=46, cy=44, n=13, amp=7, sb=64, seed=8),
  dome('side', top=4, w=44, cy=44, n=13, amp=7, nape=84, seed=8),
  dome('back', top=4, w=46, cy=44, n=13, amp=7, nape=84, seed=8))

# Sylvany Igan: media melena hinchada a rayas rojas y naranjas que tapa la frente; un antifaz negro grueso sobre los
# ojos y ceño fruncido
SR, SO = _c('#c8302a'), _c('#e07a4a')
def _stripes(view):
    out = []
    for y in (14, 38, 62, 86):
        if view == 'side':
            out.append(L([(4, y + 6), (86, y - 4)], SO, 'b', False, False, 7))
        else:
            out.append(L(quad((2, y + 10), (50, y - 2), (98, y + 10)), SO, 'b', False, False, 7))
    return out
C('sylvany-igan', 'chica', P('#c8302a', '#f8dcc4', iris='#2a2a2a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=[(8, 66), (20, 62), (80, 62), (92, 66)]),
  [M([(0, 92), (-4, 64), (6, 26), (30, 6), (50, 2), (70, 6), (94, 26), (104, 64), (100, 92), (84, 98), (80, 62), (20, 62), (16, 98)])] + _stripes('front') +
  [L(blob([(18, 70), (50, 74), (82, 70), (80, 84), (60, 82), (50, 78), (40, 82), (20, 84)], 6), BLACK, 'f')],
  [M([(80, 60), (90, 40), (80, 12), (50, 2), (20, 8), (2, 36), (-4, 70), (6, 96), (34, 98), (48, 76), (60, 64)])] + _stripes('side') +
  [L(blob([(66, 70), (92, 70), (92, 82), (68, 82)], 4), BLACK, 'f')],
  [M([(0, 92), (-4, 64), (6, 26), (30, 6), (50, 2), (70, 6), (94, 26), (104, 64), (100, 92), (50, 100)])] + _stripes('back'))

# Tage Hamley: máscara de cabra azul y blanca con los cuernos abiertos hacia los lados y orejas caídas marrones; ojos
# rojizos afilados, sonrisa
GW, GB, GBR = _c('#f0f0f4'), _c('#3a5a98'), _c('#7a5a4a')
def _goat(view):
    if view == 'front':
        return (head('front', GW, top=6, w=44, low=104) +
                [M([(26, 30), (-6, 12, 1), (10, 40), (30, 44)], GW), M([(74, 30), (106, 12, 1), (90, 40), (70, 44)], GW),
                 M([(8, 66), (-10, 84, 1), (18, 80)], GBR), M([(92, 66), (110, 84, 1), (82, 80)], GBR),
                 M([(38, 6), (62, 6), (58, 40), (50, 60, 1), (42, 40)], GB, 'f'), M([(14, 46), (36, 52), (30, 64), (14, 60)], GB, 'f'),
                 M([(86, 46), (64, 52), (70, 64), (86, 60)], GB, 'f'),
                 L(blob([(24, 74), (40, 70), (44, 78), (28, 80)], 4), BLACK, 'f'), L(blob([(76, 74), (60, 70), (56, 78), (72, 80)], 4), BLACK, 'f'),
                 L(ell(34, 76, 2.6, 2.6), _c('#c84a2a'), 'f', False), L(ell(66, 76, 2.6, 2.6), _c('#c84a2a'), 'f', False), smile_l(94, 10)])
    if view == 'side':
        return (head('side', GW, top=6, low=104, snout=4) + [M([(40, 24), (10, 4, 1), (26, 36)], GW), M([(30, 66), (10, 86, 1), (40, 78)], GBR),
                                                              M([(60, 6), (86, 20), (90, 40), (70, 30)], GB, 'f')] + eye2_side(76, 4, 4, white=False))
    return head('back', GW, top=6, w=44, low=104, shade=_c('#c8c8d0')) + [M([(26, 30), (-6, 12, 1), (10, 40)], GW), M([(74, 30), (106, 12, 1), (90, 40)], GW),
                                                                          M([(40, 4), (60, 4), (56, 60), (44, 60)], GB, 'f')]
C('tage-hamley', 'normal', P('#3a5a98', '#f0f0f4'), F(**NOFACE), _goat('front'), _goat('side'), _goat('back'))

# Tanky Hanson: casco blanco en forma de huevo que le tapa la cabeza y la cara, con líneas rosadas y dos cuernecillos
# naranjas a los lados; ojos verdes afilados y una sonrisa de dientes
EG, EGL = _c('#f4f2f0'), _c('#d4a0a8')
def _egg(view):
    if view == 'front':
        return (head('front', EG, top=-8, w=42, low=104) + [M([(10, 56), (-2, 52, 1), (10, 64)], OR), M([(90, 56), (102, 52, 1), (90, 64)], OR),
                L(quad((18, 40), (50, -2), (82, 40)), EGL, 'f', False, False, 1.6), L([(50, -4), (50, 50)], EGL, 'f', False, False, 1.4),
                L(blob([(22, 72), (42, 66), (44, 80), (24, 80)], 4), BLACK, 'f'), L(blob([(78, 72), (58, 66), (56, 80), (76, 80)], 4), BLACK, 'f'),
                L(ell(34, 75, 3.6, 3.6), _c('#3ab060'), 'f', False), L(ell(66, 75, 3.6, 3.6), _c('#3ab060'), 'f', False),
                M([(34, 88), (66, 88), (62, 98), (38, 98)], WHITE, 'f'), L([(34, 88), (66, 88), (62, 98), (38, 98), (34, 88)], OUTC, 'f', False, False, 1.2)])
    if view == 'side':
        return head('side', EG, top=-8, low=104) + [M([(44, 56), (32, 50, 1), (44, 64)], OR), L(quad((20, 30), (50, -6), (80, 20)), EGL, 'f', False, False, 1.6)] + \
            [L(blob([(70, 70), (88, 68), (88, 80), (72, 80)], 4), BLACK, 'f'), L(ell(83, 75, 2.6, 3.4), _c('#3ab060'), 'f', False)]
    return head('back', EG, top=-8, w=42, low=104, shade=_c('#d0ccd0')) + [M([(10, 56), (-2, 52, 1), (10, 64)], OR), M([(90, 56), (102, 52, 1), (90, 64)], OR)]
C('tanky-hanson', 'normal', P('#f4f2f0', '#f4f2f0'), F(**NOFACE), _egg('front'), _egg('side'), _egg('back'))

# Tau Rin: pelo azul celeste peinado hacia arriba en un tupé alto que se curva a su derecha, con mechones por los lados;
# orejas de elfo, ojos verdes y sonrisa
TB = _c('#88c8f0')
C('tau-rin', 'chica', P('#88c8f0', '#fcecc8', iris='#3a9a3a'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, ears=False, hairline=[(8, 62), (22, 50), (34, 58), (50, 46), (66, 56), (78, 48), (92, 62)]),
  [M([(14, 74), (10, 44), (20, 20), (24, -10), (40, -24), (64, -26), (84, -14, 1), (66, -12), (74, 10), (90, 30), (90, 74), (82, 56), (18, 56)]),
   M([(40, -22), (64, -24), (80, -14), (64, -12), (72, 12), (86, 34), (88, 70), (78, 40), (56, 8)], 'shade', 'b', False)] + ears_pointy('front', h=14),
  [M([(66, 54), (84, 46), (88, 24), (80, -4), (96, -16, 1), (66, -26), (40, -20), (20, 0), (6, 30), (4, 62), (16, 80), (36, 74), (48, 58)])] + ears_pointy('side', h=14),
  [M([(14, 78), (10, 44), (20, 20), (30, -10), (50, -24), (72, -22), (84, -12, 1), (78, 10), (90, 30), (90, 78), (50, 86)])])

# Tech Nobit: careta de soldador gris con una visera alargada de borde naranja y rejillas a los lados; cascos negros y
# naranjas sobre la cabeza
WG, WGD = _c('#9a9aa0'), _c('#5a5a62')
def _weld(view):
    if view == 'front':
        return (head('front', WG, top=6, w=42, low=104) +
                [M([(20, 54), (80, 54), (82, 66), (18, 66)], OR, 'f'), M([(24, 56), (76, 56), (76, 64), (24, 64)], _c('#f4f4f8'), 'f', False),
                 M([(18, 74), (32, 74), (32, 80), (18, 80)], WGD, 'f', False), M([(82, 74), (68, 74), (68, 80), (82, 80)], WGD, 'f', False),
                 M([(42, 66), (58, 66), (60, 92), (40, 92)], WGD, 'f', False),
                 L(quad((6, 66), (50, -18), (94, 66)), BLACK, 'f', False, False, 4.0), L(ell(6, 70, 6, 10), BLACK, 'f'), L(ell(94, 70, 6, 10), BLACK, 'f'),
                 L(ell(6, 70, 3, 6), OR, 'f', False), L(ell(94, 70, 3, 6), OR, 'f', False)])
    if view == 'side':
        return head('side', WG, top=6, low=104, snout=4) + [M([(70, 54), (96, 54), (96, 66), (72, 66)], OR, 'f'),
                                                             L(quad((30, 66), (44, -16), (62, 66)), BLACK, 'f', False, False, 4.0), L(ell(44, 70, 8, 11), BLACK, 'f'),
                                                             L(ell(44, 70, 4, 6), OR, 'f', False)]
    return head('back', WG, top=6, w=42, low=104, shade=WGD) + [L(quad((6, 66), (50, -18), (94, 66)), BLACK, 'f', False, False, 4.0),
                                                                 L(ell(6, 70, 6, 10), BLACK, 'f'), L(ell(94, 70, 6, 10), BLACK, 'f')]
C('tech-nobit', 'normal', P('#9a9aa0', '#9a9aa0'), F(**NOFACE), _weld('front'), _weld('side'), _weld('back'))

# ------------------------------------------------------------------ hoja 4

# Tem Akirrol (portero): pelo azul con dos puntas de orejas de gato y aletas azules que salen por debajo a los lados;
# cinta rosa y blanca en la frente; piel azul clara, ojos magenta y sonrisa
TMB = _c('#4a70a8')
C('tem-akirrol', 'normal', P('#4a70a8', '#a8d4ec', iris='#b0206a'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=94, hairline=[(8, 60), (20, 56), (80, 56), (92, 60)]),
  [M([(18, 34), (14, -6, 1), (36, 10)]), M([(82, 34), (86, -6, 1), (64, 10)])] + crop('front', top=4, side=74) +
  [M([(14, 70), (-8, 76, 1), (12, 86)], TMB), M([(86, 70), (108, 76, 1), (88, 86)], TMB), band('front', _c('#f0d4d8'), y=44, h=8)],
  [M([(40, 30), (40, -6, 1), (58, 10)])] + crop('side', top=4) + [M([(24, 70), (4, 80, 1), (28, 86)], TMB), band('side', _c('#f0d4d8'), y=40, h=8)],
  [M([(18, 34), (14, -6, 1), (36, 10)]), M([(82, 34), (86, -6, 1), (64, 10)])] + crop('back', top=4) + [band('back', _c('#f0d4d8'), y=44, h=8)])

# Teodorus Toxsin: melena rubia en casco con flequillo recto, las puntas blancas y dos puntas de orejas arriba; piel azul
# clara con mofletes azules redondos, ojos magenta grandes y sonrisa
BLD2 = _c('#f4d468')
C('teodorus-toxsin', 'normal', P('#f4d468', '#a8d8ec', iris='#b02a8a', light='#f8f4ec'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=[(8, 60), (16, 60), (84, 60), (92, 60)]),
  [M([(18, 30), (16, -12, 1), (38, 8)]), M([(82, 30), (84, -12, 1), (62, 8)]),
   M([(10, 102), (6, 64), (10, 30), (30, 8), (50, 4), (70, 8), (90, 30), (94, 64), (90, 102), (82, 60), (18, 60)]),
   M([(6, 88), (16, 88), (16, 104), (8, 104)], 'light', 'b', False), M([(94, 88), (84, 88), (84, 104), (92, 104)], 'light', 'b', False),
   L(ell(28, 86, 4.6, 3.6), _c('#5a8ad0'), 'f', False), L(ell(72, 86, 4.6, 3.6), _c('#5a8ad0'), 'f', False)],
  [M([(40, 28), (40, -12, 1), (58, 8)]), M([(80, 60), (88, 40), (80, 14), (54, 2), (26, 8), (8, 26), (2, 60), (6, 100), (30, 104), (46, 86), (56, 66)]),
   M([(4, 88), (30, 92), (30, 104), (6, 102)], 'light', 'b', False)],
  [M([(18, 30), (16, -12, 1), (38, 8)]), M([(82, 30), (84, -12, 1), (62, 8)]),
   M([(8, 104), (4, 64), (10, 30), (30, 8), (50, 4), (70, 8), (90, 30), (96, 64), (92, 104), (50, 108)]),
   M([(6, 90), (94, 90), (92, 106), (50, 110), (8, 106)], 'light', 'b', False)])

# Terryl Terrid: pelo rosa con flequillo, dos moños altos sujetos con pinzas verde agua y mechones ondulados por los lados
# hasta la mandíbula; orejas de elfo, cejas fruncidas y boquita enfadada
PK, CL = _c('#e888a0'), _c('#5ac8c0')
def _buns(view):
    if view == 'side':
        return [L(ell(40, 6, 14, 12), PK), M([(40, 12), (50, 12), (50, 20), (40, 20)], CL, 'b', False)]
    return [L(ell(24, 6, 14, 12), PK), L(ell(76, 6, 14, 12), PK), M([(26, 14), (36, 14), (36, 22), (26, 22)], CL, 'b', False),
            M([(74, 14), (64, 14), (64, 22), (74, 22)], CL, 'b', False)]
C('terryl-terrid', 'chica', P('#e888a0', '#fce4cc', iris='#2a2a30'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, ears=False, hairline=[(8, 62), (20, 52), (30, 58), (40, 50), (50, 58), (60, 50), (70, 58), (80, 52), (92, 62)]),
  _buns('front') + dome('front', top=6, w=44, cy=46, sb=70) + ears_pointy('front', h=12) +
  [L(ell(10, 94, 8, 8), PK), L(ell(90, 94, 8, 8), PK)] + tentacle(12, 64, 10, 92, PK, 6) + tentacle(88, 64, 90, 92, PK, 6),
  _buns('side') + dome('side', top=6, w=44, cy=46, nape=92) + ears_pointy('side', h=12),
  _buns('back') + dome('back', top=6, w=44, cy=46, long=96, flare=4))

# Tetchan: pelo castaño oscuro revuelto con una cinta roja en la frente; cara redonda y cansada, un ojo más abierto que el
# otro mirando hacia arriba; boca hacia abajo
C('tetchan-scout-character', 'corpulento', P('#3a2a1e', '#e0a874', iris='#2a1e14'),
  F(eyes='round', brows=True, mouth='frown', mouth_y=96, face_front=face(w=4, jaw=2, chin=104), hairline=[(8, 62), (16, 56), (84, 56), (92, 62)]),
  dome('front', top=0, w=52, cy=46, n=10, amp=8, sb=70, seed=11) + [band('front', _c('#b02a2a'), y=48, h=9)],
  dome('side', top=0, w=50, cy=46, n=10, amp=8, nape=88, seed=11) + [band('side', _c('#b02a2a'), y=44, h=9)],
  dome('back', top=0, w=52, cy=46, n=10, amp=8, nape=88, seed=11) + [band('back', _c('#b02a2a'), y=48, h=9)])

# Tetrae Charlong: melena azul marino oscura larguísima con dos puntas enormes como orejas y un mechón que le tapa el ojo
# derecho; piel azul pálida y un ojo rojo
TC = _c('#262448')
C('tetrae-charlong', 'chica', P('#262448', '#a8c8e0', iris='#c82a3a'),
  F(eyes='normal', brows=False, mouth='line', mouth_y=94, hairline=[(8, 62), (20, 46), (50, 40), (80, 46), (92, 62)]),
  [M([(14, 40), (4, -18, 1), (34, 14)], TC), M([(86, 40), (96, -18, 1), (66, 14)], TC)] + dome('front', top=6, w=46, cy=48, long=126, flare=8) +
  [M([(10, 50), (30, 40), (52, 46), (54, 70), (48, 90, 1), (40, 76), (30, 92, 1), (22, 74), (12, 80)], TC, 'f')],
  [M([(40, 40), (30, -18, 1), (56, 12)], TC)] + dome('side', top=6, w=46, cy=48, long=126, flare=8),
  [M([(14, 40), (4, -18, 1), (34, 14)], TC), M([(86, 40), (96, -18, 1), (66, 14)], TC)] + dome('back', top=6, w=46, cy=48, long=126, flare=8, ends=5))

# Tetsu Foreman: pelo castaño en pinchos de punta hacia arriba con una mecha blanca; piel morena, orejas grandes, ojos
# afilados y una sonrisa de dientes
C('tetsu-foreman', 'corpulento', P('#6a5446', '#d08a4a', iris='#2a1e14', light='#f0e4e4'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=95, big_ears=3, ear_out=3, face_front=face(w=4, jaw=4, chin=104),
    hairline=[(8, 58), (18, 52), (32, 46), (50, 54), (68, 46), (82, 52), (92, 58)]),
  [M([(14, 60), (10, 36), (14, 4, 1), (30, 14), (36, -10, 1), (50, 8), (60, -8, 1), (70, 12), (86, 2, 1), (90, 36), (86, 60), (78, 46), (22, 46)]),
   M([(56, 4), (64, -6), (66, 30), (58, 40)], 'light', 'b', False)],
  [M([(68, 46), (84, 40), (90, 20), (82, 2, 1), (66, 6), (56, -10, 1), (40, 4), (14, 6, 1), (16, 22), (4, 40), (8, 66), (28, 72), (48, 56)])],
  [M([(14, 68), (10, 36), (14, 4, 1), (30, 14), (40, -8, 1), (50, 8), (62, -8, 1), (70, 12), (86, 2, 1), (90, 36), (86, 68), (50, 74)])])

# Thor Nado (portero): tornado morado en espiral que le envuelve la cabeza entera; solo se le ven los ojos rosas por un hueco
TN, TND = _c('#6a6ac8'), _c('#4040a0')
def _tornado(view):
    out = [M([(4, 110), (-4, 90), (8, 70), (2, 52), (16, 36), (14, 18), (32, 6), (50, -6), (64, -20), (66, -10), (58, 2), (76, 14), (86, 34), (94, 54),
              (98, 78), (104, 100), (96, 112)], TN)]
    for y, a in ((20, 26), (44, 40), (66, 48), (90, 52)):
        out.append(L(quad((50 - a, y + 8), (50, y - 4), (50 + a, y + 8)), TND, 'b', False, False, 2.6))
    if view == 'front':
        out += [M([(24, 74), (76, 74), (72, 84), (28, 84)], _c('#2a2050'), 'f'), L(ell(36, 79, 6, 3), _c('#f08ad8'), 'f', False),
                L(ell(64, 79, 6, 3), _c('#f08ad8'), 'f', False), L(ell(36, 79, 2, 2.4), BLACK, 'f', False), L(ell(64, 79, 2, 2.4), BLACK, 'f', False)]
    elif view == 'side':
        out += [M([(66, 74), (96, 74), (94, 84), (68, 84)], _c('#2a2050'), 'f'), L(ell(84, 79, 5, 3), _c('#f08ad8'), 'f', False)]
    return out
C('thor-nado', 'normal', P('#6a6ac8', '#6a6ac8'), F(**NOFACE), _tornado('front'), _tornado('side'), _tornado('back'))

# Thorin Kards (portera): capucha de ninja azul marino con un protector metálico en la frente y el nudo detrás; piel
# clara, ojos verdes, mofletes rosas y sonrisa
NJ, MTL = _c('#24305a'), _c('#a8b0b8')
C('thorin-kards', 'chica', P('#24305a', '#fbe8cc', iris='#3a8a3a'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=93, hairline=False, ears=False),
  hood('front', NJ, top=-2, rim=_c('#1a2040'), face_hole=[(20, 100), (16, 70), (20, 50), (50, 44), (80, 50), (84, 70), (80, 100), (50, 108)]) +
  [M([(18, 44), (50, 36), (82, 44), (82, 56), (50, 50), (18, 56)], MTL, 'f'), L(ell(50, 47, 5, 4), _c('#6a7480'), 'f', False),
   L(ell(28, 86, 5, 4), _c('#f4a0a0'), 'f', False), L(ell(72, 86, 5, 4), _c('#f4a0a0'), 'f', False)],
  hood('side', NJ, top=-2, rim=_c('#1a2040')) + [M([(70, 40), (94, 36), (94, 48), (72, 52)], MTL, 'f'), M([(4, 60), (-14, 74, 1), (2, 80)], NJ)],
  hood('back', NJ, top=-2, rim=_c('#1a2040')) + [M([(50, 56), (36, 74, 1), (50, 66), (64, 74, 1)], NJ, 'f')])

# ------------------------------------------------------------------ hoja 5

# Tippi Tappa: melena rosa clara hinchada con flequillo y las puntas hacia fuera; encima un bicho rosa con dos aletas
# enormes a los lados y una carita; ojos verde agua y boquita seria
PKL, PKD = _c('#f4c4cc'), _c('#c89aa0')
def _tippi(view):
    if view == 'side':
        return [M([(20, 10), (24, -14), (60, -16), (70, 6), (44, 14)], PKL, 'f'), M([(30, -6), (8, -18, 1), (22, 6)], PKL, 'f')]
    return [M([(30, 10), (32, -10), (50, -18), (68, -10), (70, 10)], PKL, 'f'), M([(32, -4), (-4, -16, 1), (2, 6), (26, 10)], PKL, 'f'),
            M([(68, -4), (104, -16, 1), (98, 6), (74, 10)], PKL, 'f'), L(ell(10, -6, 4, 3), PKD, 'f', False), L(ell(90, -6, 4, 3), PKD, 'f', False)] + \
        ([L(ell(45, -6, 1.4, 1.4), BLACK, 'f', False), L(ell(55, -6, 1.4, 1.4), BLACK, 'f', False)] if view == 'front' else [])
C('tippi-tappa-tippitappa', 'chica', P('#f4c4cc', '#fcecd4', iris='#2ab0b0'),
  F(eyes='big', brows='angry', mouth='frown', mouth_y=94, hairline=[(8, 62), (20, 54), (32, 60), (44, 52), (56, 60), (68, 52), (80, 56), (92, 62)]),
  dome('front', top=8, w=46, cy=50, sb=74) + [L(ell(8, 86, 10, 10), PKL), L(ell(92, 86, 10, 10), PKL)] + _tippi('front'),
  dome('side', top=8, w=46, cy=50, nape=94) + [L(ell(24, 90, 10, 10), PKL)] + _tippi('side'),
  dome('back', top=8, w=46, cy=50, long=96, flare=6) + _tippi('back'))

# Tobiah Bragg (portero): cabeza de pájaro marrón con un pico amarillo ancho y dos cuernos beis largos abiertos a los lados;
# ojos grises afilados
TBR, TBD, HRN = _c('#7a3a2a'), _c('#5a2a1e'), _c('#d8c8a8')
def _tobiah(view):
    if view == 'front':
        return (head('front', TBR, top=6, w=42, low=110) + [M([(30, 20), (-12, 26, 1), (20, 36)], HRN), M([(70, 20), (112, 26, 1), (80, 36)], HRN),
                M([(26, 22), (50, 4), (74, 22), (50, 30)], HRN)] +
                [L(blob([(24, 62), (40, 58), (44, 66), (28, 70)], 4), WHITE, 'f'), L(blob([(76, 62), (60, 58), (56, 66), (72, 70)], 4), WHITE, 'f'),
                 L(ell(36, 64, 3, 3.4), _c('#5a5a7a'), 'f', False), L(ell(64, 64, 3, 3.4), _c('#5a5a7a'), 'f', False),
                 L([(24, 56), (40, 60)], OUTC, 'f', False, False, 2.0), L([(76, 56), (60, 60)], OUTC, 'f', False, False, 2.0),
                 L(blob([(28, 78), (50, 72), (72, 78), (64, 90), (50, 94), (36, 90)], 5), _c('#f0d040'), 'f')])
    if view == 'side':
        return head('side', TBR, top=6, low=110) + [M([(50, 20), (10, 14, 1), (40, 32)], HRN), M([(80, 76), (106, 84, 1), (82, 92)], _c('#f0d040'), 'f')] + \
            eye2_side(64, 3.6, 4)
    return head('back', TBR, top=6, w=42, low=110, shade=TBD) + [M([(30, 20), (-12, 26, 1), (20, 36)], HRN), M([(70, 20), (112, 26, 1), (80, 36)], HRN)]
C('tobiah-bragg', 'normal', P('#7a3a2a', '#7a3a2a'), F(**NOFACE), _tobiah('front'), _tobiah('side'), _tobiah('back'))

# Tog Romack: una serpiente morada con manchas verdes enroscada sobre la cabeza, con su cabeza de ojos rojos tapándole la cara
SN, SND, SNG = _c('#8a6ab8'), _c('#5a4088'), _c('#9ad040')
def _snake(view):
    out = [M([(2, 104), (-4, 70), (4, 30), (24, 6), (50, -2), (76, 6), (96, 30), (104, 70), (98, 104), (50, 112)], SN)]
    for y in (22, 46, 70, 94):
        out.append(L(quad((4, y + 6), (50, y - 6), (96, y + 6)), SND, 'b', False, False, 2.0))
    for x, y in ((20, 14), (60, 8), (84, 40), (12, 58), (90, 84), (14, 94)):
        out.append(L(ell(x, y, 5, 4), SNG, 'b', False))
    if view == 'front':
        out += [L(blob([(26, 56), (50, 46), (74, 56), (72, 80), (50, 90), (28, 80)], 6), SN, 'f'), L(ell(50, 58, 4, 3.5), SNG, 'f', False),
                L(blob([(30, 66), (42, 62), (44, 74), (32, 74)], 4), _c('#d01e1e'), 'f'), L(blob([(70, 66), (58, 62), (56, 74), (68, 74)], 4), _c('#d01e1e'), 'f'),
                L(ell(38, 69, 1.4, 3), BLACK, 'f', False), L(ell(62, 69, 1.4, 3), BLACK, 'f', False)]
    elif view == 'side':
        out += [L(blob([(70, 56), (100, 60), (102, 80), (74, 84)], 5), SN, 'f'), L(blob([(84, 64), (94, 64), (94, 74), (86, 74)], 4), _c('#d01e1e'), 'f')]
    return out
C('tog-romack', 'normal', P('#8a6ab8', '#8a6ab8'), F(**NOFACE), _snake('front'), _snake('side'), _snake('back'))

# Tri-Trot: un gorro enorme de bicho rojo coral con dos aletas a los lados y una carita encima; cara redonda clara, ojos
# de raya y mofletes rosas, sonrisa
CO, COD = _c('#d84a5a'), _c('#a8303e')
def _trot(view):
    if view == 'side':
        return [L(ell(50, 34, 52, 26), CO, 'f'), L(blob([(4, 40), (50, 52), (100, 40), (96, 54), (50, 62), (8, 54)], 5), COD, 'f'),
                M([(36, 10), (40, -10), (64, -10), (68, 10)], CO, 'f')]
    return [L(ell(50, 34, 56, 26), CO, 'f'), L(blob([(-4, 40), (50, 52), (104, 40), (100, 56), (50, 62), (0, 56)], 5), COD, 'f'),
            M([(36, 10), (40, -10), (60, -10), (64, 10)], CO, 'f'), M([(38, 0), (8, -12, 1), (14, 8)], CO, 'f'), M([(62, 0), (92, -12, 1), (86, 8)], CO, 'f')] + \
        ([L(ell(46, -2, 1.4, 1.4), BLACK, 'f', False), L(ell(54, -2, 1.4, 1.4), BLACK, 'f', False)] if view == 'front' else [])
C('tri-trot-tritrot', 'chica', P('#d84a5a', '#fce8c0', iris='#2a2a2a'),
  F(eyes='closed', brows=True, mouth='smile', mouth_y=92, hairline=False, face_front=face(w=4, chin=102)),
  _trot('front') + [L(ell(26, 84, 5, 4), _c('#f4a0a0'), 'f', False), L(ell(74, 84, 5, 4), _c('#f4a0a0'), 'f', False)],
  _trot('side'), _trot('back'))

# Tsum Jicker: cabeza de llama azul clara en espirales, con una punta enroscada arriba; cara azul con ojos ovalados negros,
# boca de gato y mofletes blancos
FL, FLD = _c('#a8d8f0'), _c('#80aed0')
def _flame(view):
    out = [M([(6, 104), (0, 70), (8, 40), (24, 20), (40, 8), (56, -6), (66, -24, 1), (70, -6), (62, 8), (80, 18), (94, 40), (100, 70), (94, 104), (50, 112)], FL)]
    out += [L(arc(36, 30, 12, 10, 0, 300), FLD, 'b', False, False, 2.0), L(arc(14, 66, 8, 8, 60, 340), FLD, 'b', False, False, 2.0),
            L(arc(86, 66, 8, 8, 200, -80), FLD, 'b', False, False, 2.0)]
    if view == 'front':
        out += [L(ell(36, 72, 3.4, 5), BLACK, 'f', False), L(ell(64, 72, 3.4, 5), BLACK, 'f', False), L(ell(26, 84, 5, 3.4), WHITE, 'f', False),
                L(ell(74, 84, 5, 3.4), WHITE, 'f', False),
                L(quad((40, 88), (45, 92), (50, 88)) + quad((50, 88), (55, 92), (60, 88))[1:], OUTC, 'f', False, False, 1.6)]
    elif view == 'side':
        out += [L(ell(82, 72, 2.6, 5), BLACK, 'f', False), L(ell(82, 84, 4, 3), WHITE, 'f', False)]
    return out
C('tsum-jicker', 'chica', P('#a8d8f0', '#a8d8f0'), F(**NOFACE), _flame('front'), _flame('side'), _flame('back'))

# Ugwis Ann: cabeza de pájaro verde menta con una cresta blanca curvada arriba, ojos redondos negros con pestañas, pico
# marrón y una bufanda granate
MNT, MNTD = _c('#b4ecd0'), _c('#8cc8ac')
def _parrot(view):
    if view == 'front':
        return (head('front', MNT, top=4, w=40, low=106) + [M([(54, 6), (66, -24, 1), (70, 0), (60, 14)], WHITE)] +
                eyes2(66, 15, 6, 6.5) + [L(ell(26, 78, 4, 3), _c('#a8e0f0'), 'f', False), L(ell(74, 78, 4, 3), _c('#a8e0f0'), 'f', False),
                                        M([(42, 74), (58, 74), (56, 92), (50, 98, 1), (44, 92)], _c('#6a5a40'), 'f')] + scarf('front', _c('#9a1e2a'), y=100, h=16))
    if view == 'side':
        return head('side', MNT, top=4, low=106, snout=4) + [M([(50, 4), (60, -24, 1), (66, 2)], WHITE)] + eye2_side(66, 4.4, 6.5) + \
            [M([(86, 74), (100, 84, 1), (86, 92)], _c('#6a5a40'), 'f')] + scarf('side', _c('#9a1e2a'), y=100, h=16)
    return head('back', MNT, top=4, w=40, low=106, shade=MNTD) + [M([(54, 6), (66, -24, 1), (70, 0), (60, 14)], WHITE)] + scarf('back', _c('#9a1e2a'), y=100, h=16)
C('ugwis-ann', 'chica', P('#b4ecd0', '#b4ecd0'), F(**NOFACE), _parrot('front'), _parrot('side'), _parrot('back'))

# Umral Seaslug: melena morada con dos puntas anchas como orejas y un pico en la frente, que cae hasta los hombros con las
# puntas blanquecinas; piel azul clara, ojos oscuros afilados y sonrisa de lado
UM = _c('#7a5ab0')
C('umral-seaslug', 'normal', P('#7a5ab0', '#a8d0e8', iris='#1e1e2a', light='#e8dcec'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=94, hairline=[(8, 62), (20, 48), (36, 52), (50, 66), (64, 52), (80, 48), (92, 62)]),
  [M([(14, 30), (-10, 4, 1), (24, 12)], UM), M([(86, 30), (110, 4, 1), (76, 12)], UM)] + dome('front', top=4, w=46, cy=46, long=112, flare=4) +
  [M([(4, 96), (16, 96), (16, 112), (6, 112)], 'light', 'b', False), M([(96, 96), (84, 96), (84, 112), (94, 112)], 'light', 'b', False)],
  [M([(40, 26), (20, 0, 1), (56, 10)], UM)] + dome('side', top=4, w=46, cy=46, long=112, flare=4),
  [M([(14, 30), (-10, 4, 1), (24, 12)], UM), M([(86, 30), (110, 4, 1), (76, 12)], UM)] + dome('back', top=4, w=46, cy=46, long=112, flare=4, ends=5))

# Unahr Giil: melena rosa pálido lisa y larga que le cae por los lados de la cara; piel verde clara, ojos cerrados en
# rendija con las cejas finas y boca seria
UP = _c('#f0c8c8')
C('unahr-giil', 'delgado', P('#f0c8c8', '#c4ecd8', iris='#1e1e1e'),
  F(eyes='closed', brows=True, mouth='frown', mouth_y=95, face_front=face(chin=104), hairline=[(8, 62), (16, 46), (40, 40), (60, 42), (84, 46), (92, 62)]),
  dome('front', top=4, w=46, cy=48, long=122, flare=2) + tentacle(14, 56, 16, 116, UP, 6, z='f') + tentacle(86, 56, 84, 116, UP, 6, z='f'),
  dome('side', top=4, w=46, cy=48, long=122, flare=2),
  dome('back', top=4, w=46, cy=48, long=122, flare=2, ends=5))

# ------------------------------------------------------------------ hoja 6

# Uni-Sync: cabeza calva morena con un moño azul marino arriba, una máscara marino que le cruza los ojos (amarillos) y
# baja en tiras por los lados, una marca roja en la nariz y perilla marino
UN, UNY = _c('#2a2850'), _c('#f0d040')
C('uni-sync-unisync', 'corpulento', P('#2a2850', '#a8744a', iris='#2a1e14'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=92, hairline=False, face_front=face(w=4, jaw=4, chin=104)),
  skull3('front') + [L(ell(50, 8, 14, 9), UN), L(blob([(12, 66), (30, 54), (50, 60), (70, 54), (88, 66), (84, 80), (60, 76), (50, 70), (40, 76), (16, 80)], 6), UN, 'f'),
                     L(ell(34, 68, 4.4, 3.4), UNY, 'f', False), L(ell(66, 68, 4.4, 3.4), UNY, 'f', False), L(ell(34, 68, 1.6, 2.4), BLACK, 'f', False),
                     L(ell(66, 68, 1.6, 2.4), BLACK, 'f', False), M([(46, 74), (54, 74), (50, 86, 1)], _c('#9a2a1e'), 'f'),
                     M([(42, 98), (58, 98), (50, 112, 1)], UN, 'f'), L([(10, 70), (6, 110)], UN, 'f', False, False, 4.0), L([(90, 70), (94, 110)], UN, 'f', False, False, 4.0)],
  skull3('side') + [L(ell(44, 6, 12, 8), UN), M([(50, 60), (94, 58), (94, 72), (54, 72)], UN, 'f'), L(ell(84, 66, 3, 2.6), UNY, 'f', False),
                    M([(84, 96), (92, 98), (86, 110, 1)], UN, 'f')],
  skull3('back') + [L(ell(50, 8, 14, 9), UN), L([(14, 66), (86, 66)], UN, 'f', False, False, 5.0)])

# Uzma Kyallak: pelo en casco azul marino con rayas celestes y blancas, en media melena con las puntas enrolladas hacia
# dentro y un rulo a cada lado arriba; piel verde grisácea, ojos negros y boca seria
UZ, UZC = _c('#1e2a6a'), _c('#4ac8e8')
def _uz_stripes(view):
    out = []
    for y, c in ((16, WHITE), (26, UZC), (60, WHITE), (70, UZC), (84, UZC)):
        if view == 'side':
            out.append(L([(4, y + 4), (84 if y < 50 else 50, y - 4 if y < 50 else y)], c, 'b', False, False, 3.6))
        else:
            out.append(L(quad((6, y + 6), (50, y - 4), (94, y + 6)), c, 'b', False, False, 3.6))
    return out
C('uzma-kyallak', 'normal', P('#1e2a6a', '#88aaa4', iris='#1e1e1e'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=94, hairline=[(8, 64), (18, 66), (82, 66), (92, 64)]),
  [L(ell(10, 20, 9, 9), UZC), L(ell(90, 20, 9, 9), UZC), M([(10, 104), (6, 64), (10, 30), (30, 8), (50, 4), (70, 8), (90, 30), (94, 64), (90, 104), (82, 66), (18, 66)], UZ)] +
  _uz_stripes('front') + [L(ell(14, 102, 7, 5), UZC), L(ell(86, 102, 7, 5), UZC)],
  [L(ell(30, 18, 9, 9), UZC), M([(80, 64), (88, 40), (80, 14), (54, 2), (26, 8), (8, 26), (2, 60), (6, 100), (30, 104), (46, 86), (56, 68)], UZ)] + _uz_stripes('side'),
  [L(ell(10, 20, 9, 9), UZC), L(ell(90, 20, 9, 9), UZC), M([(8, 104), (4, 64), (10, 30), (30, 8), (50, 4), (70, 8), (90, 30), (96, 64), (92, 104), (50, 108)], UZ)] +
  _uz_stripes('back'))

# Victarion: pelo castaño claro en pinchos revueltos hacia arriba y a los lados, ceño fruncido (sprite de la DS)
C('victor-arion-victarion', 'normal', P('#a89070', '#fadcb8', iris='#2a2a3a'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=93, hairline=hl(5, 62, 48, 58, jit=3, seed=9)),
  dome('front', top=-4, w=48, cy=44, n=10, amp=14, sb=66, seed=13),
  dome('side', top=-4, w=46, cy=44, n=10, amp=14, nape=86, seed=13),
  dome('back', top=-4, w=48, cy=44, n=10, amp=14, nape=86, seed=13))

# Wacke Koshra: casco de escarabajo naranja rojizo con dos cuernos curvados hacia arriba a los lados y manchas crema; la
# cara es una máscara naranja con dos ojos blancos de aro y una boca recta
BT, BTD, BTC = _c('#d06a3a'), _c('#a04a24'), _c('#f6dcb8')
def _beetle(view):
    if view == 'front':
        return (head('front', BT, top=8, w=40, low=104) + [M([(18, 40), (2, -10, 1), (14, 4), (30, 30)], BT), M([(82, 40), (98, -10, 1), (86, 4), (70, 30)], BT),
                M([(42, 12), (50, 6), (58, 12), (54, 44), (46, 44)], BTC, 'f', False), M([(28, 20), (38, 16), (36, 36)], BTC, 'f', False),
                M([(72, 20), (62, 16), (64, 36)], BTC, 'f', False)] + eyes2(68, 14, 5, 5, WHITE, ring_c=_c('#f4f4f4'), white=True) +
                [L(blob([(30, 84), (50, 80), (70, 84), (66, 104), (34, 104)], 5), BTC, 'f', False), L([(40, 90), (60, 90)], OUTC, 'f', False, False, 1.6)])
    if view == 'side':
        return head('side', BT, top=8, low=104, snout=4) + [M([(40, 34), (30, -10, 1), (50, 24)], BT)] + eye2_side(68, 4, 5)
    return head('back', BT, top=8, w=40, low=104, shade=BTD) + [M([(18, 40), (2, -10, 1), (14, 4), (30, 30)], BT), M([(82, 40), (98, -10, 1), (86, 4), (70, 30)], BT)]
C('wacke-koshra', 'normal', P('#d06a3a', '#d06a3a'), F(**NOFACE), _beetle('front'), _beetle('side'), _beetle('back'))

# Warim Kalkawa: máscara marrón de animal con manchas crema arriba, ojos blancos en aro y un hocico crema con la boca;
# encima un moño negro enroscado
WB, WBD, WBC = _c('#9a7a5a'), _c('#6a5038'), _c('#f2e2b8')
def _warim(view):
    if view == 'front':
        return ([L(blob([(42, 8), (40, -8), (52, -20), (66, -14), (60, -6), (50, -10), (54, 8)], 5), _c('#2a2a32'))] + head('front', WB, top=6, w=40, low=104) +
                [M([(44, 16), (56, 16), (52, 28), (48, 28)], WBC, 'f', False)] + eyes2(64, 15, 5, 5.5, BLACK, ring_c=WHITE) +
                [L(blob([(24, 78), (50, 74), (76, 78), (70, 100), (50, 104), (30, 100)], 5), WBC, 'f'), L(blob([(38, 88), (62, 88), (56, 96), (44, 96)], 4), _c('#8a4a3a'), 'f')])
    if view == 'side':
        return [L(blob([(40, 8), (36, -10), (52, -20), (60, -6), (50, 8)], 5), _c('#2a2a32'))] + head('side', WB, top=6, low=104, snout=6) + eye2_side(64, 4, 5.5) + \
            [L(blob([(66, 78), (98, 78), (94, 100), (70, 100)], 5), WBC, 'f')]
    return [L(blob([(42, 8), (40, -8), (52, -20), (66, -14), (54, 8)], 5), _c('#2a2a32'))] + head('back', WB, top=6, w=40, low=104, shade=WBD)
C('warim-kalkawa', 'normal', P('#9a7a5a', '#9a7a5a'), F(**NOFACE), _warim('front'), _warim('side'), _warim('back'))

# Worren Mooram: cabeza de oso verde agua con orejas redondas de dentro marrón, antifaz marrón alrededor de unos ojos
# negros grandes y un pico amarillo
BRG, BRGD, PAT = _c('#88b8a8'), _c('#5a8a7a'), _c('#5a4a3a')
def _bear(view):
    if view == 'front':
        return (head('front', BRG, top=6, w=46, low=104) + [L(ell(12, 16, 13, 13), BRG), L(ell(88, 16, 13, 13), BRG), L(ell(12, 16, 7, 7), PAT, 'b', False),
                L(ell(88, 16, 7, 7), PAT, 'b', False), L(ell(36, 32, 3, 3), PAT, 'f', False), L(ell(64, 32, 3, 3), PAT, 'f', False),
                L(ell(32, 66, 12, 11), PAT, 'f', False), L(ell(68, 66, 12, 11), PAT, 'f', False)] + eyes2(66, 18, 7, 7.5) +
                [L(blob([(36, 72), (50, 68), (64, 72), (62, 88), (50, 92), (38, 88)], 5), _c('#f0c840'), 'f')])
    if view == 'side':
        return head('side', BRG, top=6, low=104, snout=4) + [L(ell(40, 14, 12, 12), BRG), L(ell(80, 66, 9, 10), PAT, 'f', False)] + eye2_side(66, 5, 7) + \
            [M([(84, 72), (104, 80, 1), (86, 90)], _c('#f0c840'), 'f')]
    return head('back', BRG, top=6, w=46, low=104, shade=BRGD) + [L(ell(12, 16, 13, 13), BRG), L(ell(88, 16, 13, 13), BRG)]
C('worren-mooram', 'normal', P('#88b8a8', '#88b8a8'), F(**NOFACE), _bear('front'), _bear('side'), _bear('back'))

# Yolanda Umick: medusa: una campana azul con una línea celeste que le tapa la cabeza, tentáculos celestes que se enroscan
# por los lados; cara azul clara con ojitos azules y un chupete azul en la boca
JB, JC = _c('#4a7ac8'), _c('#5ad0d0')
def _jelly(view):
    tents = [L(quad((14, 56), (-8, 66), (0, 92)), JC, 'b', False, False, 5.0), L(quad((10, 50), (-14, 40), (-6, 20)), JC, 'b', False, False, 5.0),
             L(quad((86, 56), (108, 66), (100, 92)), JC, 'b', False, False, 5.0), L(quad((90, 50), (114, 40), (106, 20)), JC, 'b', False, False, 5.0)]
    if view == 'side':
        return [L(quad((20, 56), (0, 70), (6, 96)), JC, 'b', False, False, 5.0), L(quad((16, 50), (-6, 36), (2, 18)), JC, 'b', False, False, 5.0),
                cap('side', JB, top=4, rim=60, w=46, z='f'), L(quad((6, 46), (50, 30), (90, 40)), JC, 'f', False, False, 2.6)]
    out = tents + [cap(view, JB, top=4, rim=60, w=46, z='f'), L(quad((8, 52), (50, 34), (92, 52)), JC, 'f', False, False, 2.6)]
    if view == 'front':
        out += [L(ell(50, 96, 6, 4.6), _c('#2a5ab0'), 'f'), L(ell(50, 96, 2.6, 2), _c('#4a8ae0'), 'f', False)]
    return out
C('yolanda-umick', 'chica', P('#4a7ac8', '#b0dcf0', iris='#2a6ac8'),
  F(eyes='round', brows=False, mouth='none', mouth_y=94, hairline=False, eye_y=76),
  _jelly('front'), _jelly('side'), _jelly('back'))
