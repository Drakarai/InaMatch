"""Ojeadores de GX (scouts-gx), tanda 03: dibujados a partir de su retrato de Victory Road; claves 'scouts-gx:<id>'.

El frente sale del retrato y el perfil y la espalda se deducen (con el modelo 3D cuando es del mismo personaje: Lucia,
Mabel Lerner, Marigold Blossom, Miriam Sharpe, Mr. Shipwood, Mr. Veteran, Ptumri Emnator). Muchos son alienígenas o van
disfrazados (cabezas de pájaro, pingüino o gallo): esos se dibujan enteros como capas (no_head).
Usa las ayudas de los ojeadores de IE (dome/hl/face de ie1_09, gafas de ie1_03 e ie2_03, capucha de ie3_02...)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401
from chars_scouts_ie1_09 import dome, hl, face, face_side, mark, _c  # noqa: F401
from chars_scouts_ie1_03 import goggles, round_specs, thick_brows, side_brow, blush, big_grin, eyes_custom, side_eye_custom  # noqa: F401
from chars_scouts_ie2_03 import ears_pointy, teeth_grin, round_glasses, skull  # noqa: F401
from chars_scouts_ie2_04 import sharp_eyes, sharp_eye_side  # noqa: F401
from chars_scouts_ie3_02 import hood, skull3, bowl3, scarf, ring  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)


def F(**k):
    d = {'eyes': 'normal', 'mouth': 'line'}
    d.update(k)
    return d


def P(hair, skin, iris='#302232', **k):
    return pal(hair, skin, iris, **k)


def C(pid, body, palette, f, front, side, back):
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        # el nacimiento del pelo baja por el borde de la cara: así su raya no cruza el pelo de los lados
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + [p[:2] for p in hl_[1:-1]] + [(max(xs) - 0.6, 104)]
    CHARS[f'scouts-gx:{pid}'] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


NOHEAD = dict(eyes='none', brows=False, mouth='none', hairline=False, no_head=True, ears=False)


def fr(pts, c='mid', z='f'):
    return L(outline(pts), c, z)


def eye(cx, ey, iris, r=4.2, white=True, shine=True, rx=None):
    """Ojo redondo dibujado como capa (para cabezas de disfraz)."""
    rx = rx or r * 0.85
    out = []
    if white:
        out.append(L(ell(cx, ey, rx + 1.6, r + 1.6), WHITE, 'f', False))
    out.append(L(ell(cx, ey, rx, r), iris, 'f', False))
    if shine:
        out.append(L(ell(cx - rx * 0.35, ey - r * 0.4, rx * 0.3, r * 0.3), WHITE, 'f', False))
    return out


def eyes2(iris, ey=75, sep=14, r=4.2, white=True):
    return eye(50 - sep, ey, iris, r, white) + eye(50 + sep, ey, iris, r, white)


def cut(pts, c, z='f'):
    """Mancha plana sin contorno."""
    return L(blob(pts, 5), c, z, False)


# ------------------------------------------------------------------ jugadores

# Kazar Kibane (portero): disfraz de pájaro verde entero, una cresta de pinchos arriba, manchas azul claro alrededor de los
# ojos, pico naranja pequeño y un babero azul y rojo en el pecho
GR, GRD, LB, OR, RD = _c('#4aa838'), _c('#2f7a28'), _c('#7ad0e8'), _c('#f0a030'), _c('#d02a2a')
def _bird(view):
    if view == 'front':
        return [L(outline([(6, 110), (4, 70), (14, 30), (34, 10), (46, -12, 1), (52, 6), (58, -8, 1), (62, 8), (80, 22), (94, 58), (98, 110), (50, 116)]), GR, 'f'),
                cut([(62, 8), (82, 24), (94, 60), (96, 108), (76, 100), (78, 50)], GRD),
                cut([(24, 66), (38, 62), (46, 72), (40, 86), (26, 84), (20, 74)], LB), cut([(76, 66), (62, 62), (54, 72), (60, 86), (74, 84), (80, 74)], LB),
                L(blob([(30, 96), (50, 90), (70, 96), (66, 112), (50, 118), (34, 112)], 5), LB, 'f', False),
                L(blob([(36, 102), (50, 98), (64, 102), (58, 114), (50, 118), (42, 114)], 5), RD, 'f', False),
                L(outline([(42, 82), (58, 82), (50, 90)]), OR, 'f')] + eye(36, 75, BLACK, 3.6, False) + eye(64, 75, BLACK, 3.6, False)
    if view == 'side':
        return [L(outline([(10, 112), (2, 70), (10, 30), (30, 10), (40, -12, 1), (48, 6), (58, -4, 1), (62, 10), (82, 26), (92, 60), (94, 112), (50, 116)]), GR, 'f'),
                cut([(10, 40), (30, 30), (36, 70), (24, 100), (8, 90)], GRD),
                cut([(70, 64), (86, 62), (92, 74), (88, 86), (74, 84)], LB), L(outline([(88, 80), (100, 84), (88, 88)]), OR, 'f'),
                L(blob([(70, 96), (92, 94), (94, 112), (74, 116)], 5), RD, 'f', False)] + eye(82, 75, BLACK, 3.4, False)
    return [L(outline([(6, 112), (4, 70), (14, 30), (34, 10), (46, -12, 1), (52, 6), (58, -8, 1), (62, 8), (80, 22), (94, 58), (98, 112), (50, 116)]), GR, 'f'),
            cut([(60, 10), (82, 24), (94, 60), (96, 108), (70, 110), (72, 50)], GRD)]
C('kazar-kibane', 'normal', P('#4aa838', '#f0c8a0'), F(**NOHEAD), _bird('front'), _bird('side'), _bird('back'))

# Ken Park: alienígena de piel amarilla, calvo, con orejas largas de punta; una gema morada en la frente y sombra morada
# alrededor de los ojos rasgados
YL, YLD, PU = _c('#e8c440'), _c('#c8a028'), _c('#8a2a9a')
C('ken-park', 'normal', P('#e8c440', '#e8c440', iris='#f0e0f0', skin_d='#c8a028'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=94, hairline=False, ears=False),
  skull('front', 'skin') + ears_pointy('front', 'skin', 18) +
  [L(blob([(50, 30), (56, 42), (50, 54), (44, 42)], 4), PU, 'f'), cut([(48, 36), (51, 34), (50, 44)], _c('#c070d0')),
   cut([(22, 70), (44, 74), (42, 84), (30, 82)], PU), cut([(78, 70), (56, 74), (58, 84), (70, 82)], PU)] + sharp_eyes(_c('#f0d8f0')),
  skull3('side', 'skin') + ears_pointy('side', 'skin', 18) + [L(blob([(82, 34), (88, 42), (84, 52)], 4), PU, 'f'), cut([(74, 70), (90, 72), (88, 84)], PU)] +
  sharp_eye_side(_c('#f0d8f0')),
  skull3('back', 'skin') + ears_pointy('back', 'skin', 18))

# Kierry Reese: casco verde oscuro de cuernos con capucha blanca y rosa por los lados; la máscara verde baja hasta la nariz
# con dos marcas blancas; ojos morados y cara gris
DG, DGD, PK = _c('#2e5a4a'), _c('#1e3e34'), _c('#e8c8d0')
def _kierry(view):
    if view == 'front':
        return [L(outline([(4, 104), (2, 60), (8, 30), (-6, 0, 1), (22, 20), (50, 10), (78, 20), (106, 0, 1), (92, 30), (98, 60), (96, 104), (80, 102), (82, 50),
                           (50, 40), (18, 50), (20, 102)]), WHITE, 'f'),
                cut([(8, 60), (16, 52), (20, 100), (8, 100)], PK), cut([(92, 60), (84, 52), (80, 100), (92, 100)], PK),
                L(outline([(10, 34), (-4, 2, 1), (24, 16), (50, 4), (76, 16), (104, 2, 1), (90, 34), (82, 54), (76, 70), (62, 80), (50, 90, 1), (38, 80), (24, 70),
                           (18, 54)]), DG, 'f'),
                cut([(30, 24), (50, 10), (70, 24), (50, 18)], DGD),
                L(outline([(44, 50), (50, 44), (48, 58)]), WHITE, 'f', False), L(outline([(56, 50), (50, 44), (52, 58)]), WHITE, 'f', False)] + sharp_eyes(_c('#9a3ab0'), ey=74)
    if view == 'side':
        return [L(outline([(10, 104), (2, 60), (8, 30), (30, 14), (60, 8), (70, -8, 1), (76, 14), (90, 30), (94, 60), (90, 90), (70, 88), (60, 104)]), WHITE, 'f'),
                L(outline([(30, 20), (60, 8), (70, -8, 1), (78, 14), (92, 34), (94, 60), (84, 80), (76, 64), (60, 44), (40, 30)]), DG, 'f')] + sharp_eye_side(_c('#9a3ab0'), 74)
    return [L(outline([(4, 106), (2, 60), (8, 30), (-6, 0, 1), (22, 20), (50, 10), (78, 20), (106, 0, 1), (92, 30), (98, 60), (96, 106), (50, 110)]), WHITE, 'f'),
            cut([(4, 70), (20, 60), (30, 104), (6, 104)], PK), cut([(96, 70), (80, 60), (70, 104), (94, 104)], PK),
            L(outline([(10, 34), (-4, 2, 1), (24, 16), (50, 4), (76, 16), (104, 2, 1), (90, 34), (84, 54), (50, 60), (16, 54)]), DG, 'f')]
C('kierry-reese', 'normal', P('#2e5a4a', '#a8a8b0', iris='#9a3ab0', skin_d='#888890'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, hairline=False, ears=False), _kierry('front'), _kierry('side'), _kierry('back'))

# Kiroh Beira: capucha amarilla con dos orejas altas y un disco negro a cada lado; cara verde pálido con unas líneas
# claras en la frente y las mejillas, ojos enormes redondos y boca pequeña
YE, YED, PG = _c('#f0b820'), _c('#c88a10'), _c('#c8e8d8')
def _kiroh(view):
    if view == 'front':
        return [L(outline([(8, 100), (4, 60), (10, 30), (6, -14, 1), (26, 12), (50, 6), (74, 12), (94, -14, 1), (90, 30), (96, 60), (92, 100), (80, 98), (82, 50),
                           (50, 38), (18, 50), (20, 98)]), YE, 'f'),
                cut([(76, 14), (92, -10), (90, 40), (96, 70), (90, 96), (82, 92), (84, 50)], YED),
                L(ell(10, 74, 5, 9), BLACK, 'f'), L(ell(90, 74, 5, 9), BLACK, 'f'),
                L([(34, 52), (42, 48), (50, 52), (58, 48), (66, 52)], _c('#eef8c8'), 'f', False, False, 2), L([(38, 58), (50, 54), (62, 58)], _c('#eef8c8'), 'f', False, False, 2)]
    if view == 'side':
        return [L(outline([(10, 100), (4, 60), (12, 30), (20, -12, 1), (40, 10), (56, 4), (66, -14, 1), (76, 16), (86, 34), (88, 50), (70, 46), (56, 60), (54, 100)]), YE, 'f'),
                L(ell(50, 74, 6, 9), BLACK, 'f')]
    return [L(outline([(8, 104), (4, 60), (10, 30), (6, -14, 1), (26, 12), (50, 6), (74, 12), (94, -14, 1), (90, 30), (96, 60), (92, 104), (50, 108)]), YE, 'f'),
            cut([(70, 12), (92, -10), (90, 40), (96, 70), (90, 100), (70, 104)], YED), L(ell(6, 74, 4, 9), BLACK, 'f'), L(ell(94, 74, 4, 9), BLACK, 'f')]
C('kiroh-beira', 'normal', P('#f0b820', '#c8e8d8', iris='#141010', skin_d='#a8c8b8'),
  F(eyes='round', brows=False, mouth='smile', mouth_y=93, hairline=False, ears=False), _kiroh('front'), _kiroh('side'), _kiroh('back'))

# Kohen Moak: alienígena azul claro, calvo, con dos antenas pintadas en la frente y orejas de punta; antifaz marrón oscuro
# con dos lentes rojas de rayas y una sonrisa enorme con la boca roja
AB, AD, BR = _c('#a8d8ec'), _c('#80b0c8'), _c('#4a2a22')
def _goggle_k(view):
    if view == 'front':
        out = [L(blob([(16, 70), (30, 64), (50, 70), (70, 64), (84, 70), (82, 82), (66, 86), (50, 80), (34, 86), (18, 82)], 5), BR, 'f')]
        for cx in (34, 66):
            out += [L(ell(cx, 75, 7, 7), _c('#d02a2a'), 'f', False), L([(cx - 5, 74), (cx + 5, 74)], BLACK, 'f', False, False, 1.4), L([(cx - 5, 77), (cx + 5, 77)], BLACK, 'f', False, False, 1.4)]
        return out
    return [L(blob([(56, 70), (88, 66), (90, 82), (60, 84)], 5), BR, 'f'), L(ell(82, 75, 5, 6.5), _c('#d02a2a'), 'f', False)]
C('kohen-moak', 'normal', P('#a8d8ec', '#a8d8ec', iris='#d02a2a', skin_d='#80b0c8'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=92, hairline=False, ears=False),
  skull('front') + ears_pointy('front', 'skin', 10) + [L([(38, 54), (36, 24)], BLACK, 'f', False, False, 1.6), L([(62, 54), (64, 24)], BLACK, 'f', False, False, 1.6),
                                                     L(ell(36, 22, 3, 3), BLACK, 'f', False), L(ell(64, 22, 3, 3), BLACK, 'f', False), cut([(40, 92), (60, 92), (54, 100), (46, 100)], _c('#d83a3a'))] + _goggle_k('front'),
  skull3('side') + ears_pointy('side', 'skin', 10) + [L([(76, 50), (70, 20)], BLACK, 'f', False, False, 1.6), L(ell(70, 18, 3, 3), BLACK, 'f', False)] + _goggle_k('side'),
  skull3('back') + ears_pointy('back', 'skin', 10) + [L([(16, 72), (84, 72)], BR, 'f', False, False, 4)])

# Korum Jintal: disfraz de pingüino: capucha verde azulado oscuro con una X blanca encima, el pecho crema por delante de la
# cara, pico amarillo largo, manchas naranjas en las mejillas y ojos verdes aburridos
PT, PTD, CRM = _c('#1e4a50'), _c('#14343a'), _c('#f4ecd8')
def _penguin(view):
    if view == 'front':
        return [L(outline([(4, 112), (2, 60), (10, 24), (30, 6), (50, 2), (70, 6), (90, 24), (98, 60), (96, 112), (50, 116)]), PT, 'f'),
                L([(28, 10), (72, 46)], WHITE, 'f', False, False, 2.6), L([(72, 10), (28, 46)], WHITE, 'f', False, False, 2.6),
                L(blob([(16, 82), (30, 76), (50, 80), (70, 76), (84, 82), (86, 106), (70, 118), (50, 120), (30, 118), (14, 106)], 6), CRM, 'f'),
                cut([(18, 70), (28, 68), (28, 80), (18, 80)], OR), cut([(82, 70), (72, 68), (72, 80), (82, 80)], OR),
                L(outline([(42, 74), (58, 74), (50, 112, 1)]), YE, 'f')] + \
            [L(ell(36, 72, 5, 3), WHITE, 'f', False), L(ell(36, 72, 2.4, 2.4), _c('#2a8a6a'), 'f', False), L([(30, 70), (42, 70)], BLACK, 'f', False, False, 1.6),
             L(ell(64, 72, 5, 3), WHITE, 'f', False), L(ell(64, 72, 2.4, 2.4), _c('#2a8a6a'), 'f', False), L([(58, 70), (70, 70)], BLACK, 'f', False, False, 1.6)]
    if view == 'side':
        return [L(outline([(10, 114), (2, 60), (10, 24), (34, 4), (62, 6), (84, 22), (94, 54), (96, 114), (50, 118)]), PT, 'f'),
                L(blob([(64, 80), (92, 76), (96, 112), (70, 118)], 6), CRM, 'f'), cut([(82, 66), (92, 66), (92, 78), (84, 78)], OR),
                L(outline([(86, 74), (112, 96, 1), (88, 88)]), YE, 'f'), L(ell(82, 70, 3, 2.4), WHITE, 'f', False)]
    return [L(outline([(4, 114), (2, 60), (10, 24), (30, 6), (50, 2), (70, 6), (90, 24), (98, 60), (96, 114), (50, 118)]), PT, 'f'),
            L([(28, 10), (72, 46)], WHITE, 'f', False, False, 2.6), L([(72, 10), (28, 46)], WHITE, 'f', False, False, 2.6), cut([(64, 10), (92, 30), (96, 110), (70, 112)], PTD)]
C('korum-jintal', 'normal', P('#1e4a50', '#f0c8a0'), F(**NOHEAD), _penguin('front'), _penguin('side'), _penguin('back'))

# Kreaton Coco: disfraz de gallo: cabeza blanca con una cresta roja alta, antifaz rojo de picos alrededor de los ojos,
# pico amarillo y la barbilla roja colgando
def _rooster(view):
    if view == 'front':
        return [L(outline([(8, 112), (4, 60), (14, 22), (36, 8), (50, 6), (64, 8), (86, 22), (96, 60), (92, 112), (50, 116)]), WHITE, 'f'),
                L(outline([(44, 10), (40, -10), (46, -26), (54, -26), (60, -10), (56, 10)]), RD, 'f'),
                L(outline([(14, 68), (24, 60), (40, 66), (50, 72), (60, 66), (76, 60), (86, 68), (80, 80), (66, 84), (50, 80), (34, 84), (20, 80)]), RD, 'f'),
                L(outline([(40, 80), (60, 80), (50, 94)]), YE, 'f'), L(outline([(44, 92), (56, 92), (58, 112), (50, 118), (42, 112)]), RD, 'f')] + \
            sharp_eyes(BLACK, ey=73, sep=15)
    if view == 'side':
        return [L(outline([(10, 112), (2, 60), (12, 22), (36, 6), (62, 6), (84, 22), (94, 56), (94, 112), (50, 116)]), WHITE, 'f'),
                L(outline([(44, 8), (46, -14), (60, -26), (70, -16), (66, 10)]), RD, 'f'),
                L(outline([(66, 64), (90, 62), (92, 80), (70, 82)]), RD, 'f'), L(outline([(88, 78), (104, 86, 1), (88, 90)]), YE, 'f'),
                L(outline([(84, 90), (92, 92), (92, 112), (84, 114)]), RD, 'f')] + sharp_eye_side(BLACK, 72)
    return [L(outline([(8, 114), (4, 60), (14, 22), (36, 8), (50, 6), (64, 8), (86, 22), (96, 60), (92, 114), (50, 118)]), WHITE, 'f'),
            L(outline([(44, 10), (40, -10), (46, -26), (54, -26), (60, -10), (56, 10)]), RD, 'f'), cut([(64, 12), (88, 26), (94, 108), (72, 112)], _c('#dedede'))]
C('kreaton-coco', 'normal', P('#f4f4f4', '#f0c8a0'), F(**NOHEAD), _rooster('front'), _rooster('side'), _rooster('back'))

# Kudon Kanran: alienígena bajito de piel marrón, calvo y con orejas de punta anchas; un mechón verde oscuro alborotado en
# lo alto, marcas crema en la frente y las mejillas, ojos amarillos enfadados y dientes apretados
BRN, GRN = _c('#b8845e'), _c('#2e5a34')
C('kudon-kanran', 'bajito', P('#2e5a34', '#b8845e', iris='#c89a20', skin_d='#966644'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, hairline=False, ears=False, face_front=face(w=4, jaw=3)),
  skull('front') + ears_pointy('front', 'skin', 6) +
  [cut([(30, 50), (50, 44), (70, 50), (60, 56), (40, 56)], _c('#f0dcb0')), cut([(22, 84), (34, 82), (30, 90)], _c('#f0dcb0')), cut([(78, 84), (66, 82), (70, 90)], _c('#f0dcb0')),
   fr([(36, 30), (30, 14), (40, 18), (44, 2), (52, 16), (62, 4), (64, 20), (74, 16), (66, 32), (56, 28), (52, 40, 1), (46, 28)])],
  skull3('side') + ears_pointy('side', 'skin', 6) + [fr([(40, 16), (46, 0), (56, 12), (66, 2), (70, 16), (80, 18), (72, 28), (54, 26)]), cut([(74, 82), (86, 82), (82, 90)], _c('#f0dcb0'))],
  skull3('back') + ears_pointy('back', 'skin', 6) + [fr([(36, 24), (40, 6), (50, 16), (60, 4), (64, 24), (50, 30)], z='b')])

# Kusaken: niño de pelo negro en casco recto, mofletes colorados y ojos cerrados sonriendo
C('kusaken', 'bajito', P('#2a2a22', '#f6c8a0', iris='#141010'),
  F(eyes='closed', brows=True, mouth='smile', mouth_y=92, hairline=[(8, 58), (50, 58), (92, 58)]),
  bowl3('front', top=6, side=72, fringe=58) + blush(y=84, dx=22, r=5.4),
  bowl3('side', top=6, nape=88, fringe=58),
  bowl3('back', top=6, nape=88))

# Lesath Tine: pelo azul marino en mechones de punta echados hacia arriba y atrás con una goma roja; marcas verde agua (un
# rombo en la frente y líneas bajo los ojos), ojos verde agua afilados y sonrisa de dientes
NV, TQ = _c('#28364a'), _c('#5ab0b0')
C('lesath-tine', 'normal', P('#28364a', '#f0d0a8', iris='#3a9a9a', shade='#1a2434'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, hairline=[(14, 60), (18, 40), (32, 30), (50, 26), (68, 30), (82, 40), (86, 60)]),
  [L(outline([(14, 60), (12, 34), (20, 14), (6, 2, 1), (30, 4), (40, -16, 1), (52, 0), (70, -14, 1), (66, 6), (90, 0, 1), (84, 20), (88, 34), (86, 60), (80, 40), (20, 40)])),
   L(ell(52, 2, 5, 3), _c('#c03030'), 'f'),
   L(blob([(50, 32), (56, 40), (50, 48), (44, 40)], 4), TQ, 'f', False),
   L([(24, 84), (34, 86)], TQ, 'f', False, False, 2), L([(76, 84), (66, 86)], TQ, 'f', False, False, 2), L([(44, 98), (50, 104), (56, 98)], TQ, 'f', False, False, 2)],
  [L(outline([(54, 56), (60, 40), (80, 30), (84, 14), (70, 4), (50, -14, 1), (40, 2), (14, -10, 1), (20, 10), (2, 14, 1), (10, 30), (6, 50), (18, 62), (40, 60)])),
   L(ell(42, 4, 4, 4), _c('#c03030'), 'f'), L([(76, 84), (86, 86)], TQ, 'f', False, False, 2)],
  [L(outline([(16, 70), (12, 34), (20, 14), (6, 2, 1), (30, 4), (40, -16, 1), (52, 0), (70, -14, 1), (66, 6), (90, 0, 1), (84, 20), (88, 34), (84, 70), (50, 74)])),
   L(ell(50, 2, 5, 4), _c('#c03030'), 'f')])

# Lucia: media melena rubia clara en casco con flequillo de puntas, ojos verdes grandes y sonrisa (con su modelo 3D)
C('lucia', 'chica', P('#f4ec9a', '#fadcb4', iris='#3a9a4a', shade='#d8cc70'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(8, 60), (20, 58), (28, 50), (36, 60), (44, 50), (52, 60), (62, 50), (70, 60), (80, 52), (92, 60)]),
  bowl3('front', top=2, side=92, fringe=52) + [fr([(20, 50), (28, 64, 1), (34, 50), (44, 64, 1), (50, 50), (60, 64, 1), (66, 50), (76, 64, 1), (82, 50)])],
  bowl3('side', top=2, nape=94, fringe=54),
  bowl3('back', top=2, nape=96))

# Luka Aril: piel naranja, pelo azul claro corto en mechones con dos cuernos naranjas largos; orejas de punta muy largas,
# una marca morada en la frente, ojos marrones y un cuello de piel blanca esponjosa
BL, BLD, ORS = _c('#3aa0d0'), _c('#2a78a8'), _c('#f0a868')
C('luka-aril', 'normal', P('#3aa0d0', '#f0a868', iris='#5a3020', shade='#2a78a8', skin_d='#d08848'),
  F(eyes='normal', brows='angry', mouth='frown', mouth_y=94, hairline=[(14, 60), (18, 44), (30, 38), (44, 46), (56, 36), (70, 44), (82, 44), (86, 60)]),
  ears_pointy('front', 'skin', 22) + dome('front', top=4, w=42, cy=46, n=6, amp=6, soft=True, sb=62, seed=5) +
  [L(outline([(36, 14), (32, -22, 1), (42, 10)]), ORS, 'f'), L(outline([(60, 12), (66, -22, 1), (68, 14)]), ORS, 'f'),
   L(blob([(48, 54), (52, 54), (50, 60)], 3), PU, 'f', False),
   L(blob([(20, 100), (36, 96), (50, 100), (64, 96), (80, 100), (84, 112), (50, 118), (16, 112)], 6), WHITE, 'f')],
  ears_pointy('side', 'skin', 22) + dome('side', top=4, w=42, cy=46, n=6, amp=6, soft=True, nape=80, fr=46, seed=5) +
  [L(outline([(56, 10), (62, -22, 1), (66, 14)]), ORS, 'f'), L(blob([(40, 98), (86, 96), (88, 112), (40, 114)], 6), WHITE, 'f')],
  ears_pointy('back', 'skin', 22) + dome('back', top=4, w=42, cy=46, n=6, amp=6, soft=True, nape=80, seed=5) +
  [L(outline([(36, 14), (32, -22, 1), (42, 10)]), ORS, 'f'), L(outline([(60, 12), (66, -22, 1), (68, 14)]), ORS, 'f'),
   L(blob([(14, 100), (50, 96), (86, 100), (88, 112), (12, 112)], 6), WHITE, 'f')])

# Luvy Duvy (portera): gorro de medusa azul turquesa que se abre en dos alas anchas con lunares rosas, con dos tiras largas
# que caen a los lados de la cara; flequillo turquesa en ondas y ojos rojos grandes
TU, TUD = _c('#3ab8c8'), _c('#2a909e')
def _jelly(view):
    if view == 'front':
        return [L(outline([(16, 104), (12, 70), (-20, 56), (-26, 44), (-10, 36), (14, 34), (24, 14), (50, 4), (76, 14), (86, 34), (110, 36), (126, 44), (120, 56),
                           (88, 70), (84, 104), (76, 106), (76, 64), (24, 64), (24, 106)]), TU),
                L(ell(-14, 46, 4, 3), _c('#f0b0b0'), 'f', False), L(ell(114, 46, 4, 3), _c('#f0b0b0'), 'f', False),
                L([(36, 30), (42, 34), (50, 30), (58, 34), (64, 30)], TUD, 'f', False, False, 2)]
    if view == 'side':
        return [L(outline([(30, 104), (24, 70), (-6, 60), (-12, 46), (10, 38), (20, 14), (50, 4), (78, 16), (88, 40), (84, 54), (60, 60), (50, 104)]), TU),
                L(ell(0, 50, 4, 3), _c('#f0b0b0'), 'f', False)]
    return [L(outline([(16, 106), (12, 70), (-20, 56), (-26, 44), (-10, 36), (14, 34), (24, 14), (50, 4), (76, 14), (86, 34), (110, 36), (126, 44), (120, 56),
                       (88, 70), (84, 106), (50, 100)]), TU), cut([(60, 10), (84, 30), (84, 100), (66, 96)], TUD)]
C('luvy-duvy-luvyduvy', 'chica', P('#3ab8c8', '#fadcb4', iris='#b02030', shade='#2a909e'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=93, hairline=[(8, 62), (22, 58), (34, 64), (46, 58), (54, 64), (66, 58), (78, 64), (92, 62)]),
  _jelly('front'), _jelly('side'), _jelly('back'))

# Mabel Lerner: melena castaña larga y lisa con raya en medio, gafas de montura fina y pañuelo rosa al cuello; ojos
# morados serios (con su modelo 3D)
C('mabel-lerner', 'chica', P('#9a7a62', '#f6d8b4', iris='#6a5a8a', shade='#7a5e48'),
  F(eyes='sharp', brows=True, mouth='line', mouth_y=94, hairline=[(14, 70), (20, 44), (34, 34), (50, 30), (66, 34), (80, 44), (86, 70)]),
  dome('front', top=2, w=44, cy=46, long=104, flare=4, seed=2) + [fr([(50, 30), (40, 40), (30, 60), (28, 72), (24, 56)]), fr([(50, 30), (60, 40), (70, 60), (72, 72), (76, 56)])] +
  round_glasses('front', _c('#5a3a3a'), y=76, r=7, w=1.4) + scarf('front', _c('#f0a8a8'), y=102, h=10),
  dome('side', top=2, w=44, cy=46, long=104, seed=2, fr=40) + round_glasses('side', _c('#5a3a3a'), y=76, r=7, w=1.4) + scarf('side', _c('#f0a8a8'), y=102, h=10),
  dome('back', top=2, w=44, cy=46, long=96, seed=2, ends=3) +
  [L(outline([(42, 62), (58, 62), (60, 104), (50, 112, 1), (40, 104)]), 'mid', 'f'), L(outline([(41, 64), (59, 64), (59, 72), (41, 72)]), _c('#4a2a4a'), 'f')])

# Mag Nessium: piel morena, pelo castaño oscuro alborotado con dos mechones gruesos que se curvan como cuernos a los lados;
# orejas de punta y ojos morados
DBR = _c('#4a3426')
C('mag-nessium', 'normal', P('#4a3426', '#b8845e', iris='#8a4ac0', shade='#33241a'),
  F(eyes='big', brows=True, mouth='line', mouth_y=94, hairline=[(14, 60), (20, 46), (34, 42), (44, 50), (54, 42), (68, 46), (82, 46), (86, 60)]),
  ears_pointy('front', 'skin', 10) + dome('front', top=6, w=42, cy=46, n=8, amp=6, soft=True, sb=62, seed=8) +
  [L(outline([(14, 40), (-4, 34), (-8, 50), (-2, 62, 1), (4, 46), (16, 50)])), L(outline([(86, 40), (104, 34), (108, 50), (102, 62, 1), (96, 46), (84, 50)]))],
  ears_pointy('side', 'skin', 10) + dome('side', top=6, w=42, cy=46, n=8, amp=6, soft=True, nape=82, fr=46, seed=8) +
  [L(outline([(40, 36), (26, 24), (18, 38), (24, 52, 1), (28, 40), (40, 46)]))],
  ears_pointy('back', 'skin', 10) + dome('back', top=6, w=42, cy=46, n=8, amp=6, soft=True, nape=82, seed=8) +
  [L(outline([(14, 40), (-4, 34), (-8, 50), (-2, 62, 1), (4, 46), (16, 50)])), L(outline([(86, 40), (104, 34), (108, 50), (102, 62, 1), (96, 46), (84, 50)]))])

# Manny Armal: pelo amarillo en pinchos alrededor de la cabeza; la cara la tapa una máscara marrón con seis lentes naranjas
# redondas como ojos de insecto; asoma la boca con dientes
def _bug(view):
    if view == 'front':
        out = [L(blob([(26, 50), (50, 44), (74, 50), (78, 72), (72, 90), (50, 94), (28, 90), (22, 72)], 6), _c('#5a3a2a'), 'f')]
        for cx, cy, r in ((36, 58, 6), (64, 58, 6), (32, 72, 7), (68, 72, 7), (36, 86, 5.5), (64, 86, 5.5)):
            out += [L(ell(cx, cy, r, r), _c('#e8641e'), 'f'), L(ell(cx - r * 0.3, cy - r * 0.3, r * 0.3, r * 0.3), _c('#f8b878'), 'f', False)]
        return out
    return [L(blob([(60, 50), (88, 50), (92, 72), (88, 92), (62, 92)], 6), _c('#5a3a2a'), 'f'), L(ell(84, 60, 4, 5), _c('#e8641e'), 'f'), L(ell(86, 74, 4.5, 6), _c('#e8641e'), 'f'),
            L(ell(84, 87, 3.5, 4.5), _c('#e8641e'), 'f')]
C('manny-armal', 'normal', P('#f0c020', '#f6d0a8', shade='#d0a010'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=97, hairline=False),
  [L(outline([(8, 90), (-4, 70, 1), (6, 50), (-6, 30, 1), (12, 20), (14, -2, 1), (32, 8), (50, -16, 1), (68, 8), (86, -2, 1), (88, 20), (106, 30, 1), (94, 50),
              (104, 70, 1), (92, 90), (78, 76), (22, 76)]))] + _bug('front'),
  [L(outline([(56, 60), (60, 44), (80, 40), (90, 22), (80, 0, 1), (60, 10), (46, -14, 1), (34, 8), (10, 4, 1), (14, 24), (-4, 36, 1), (8, 52), (0, 74, 1), (16, 82),
              (40, 82), (52, 74)]))] + _bug('side'),
  [L(outline([(8, 92), (-4, 70, 1), (6, 50), (-6, 30, 1), (12, 20), (14, -2, 1), (32, 8), (50, -16, 1), (68, 8), (86, -2, 1), (88, 20), (106, 30, 1), (94, 50),
              (104, 70, 1), (92, 92), (50, 96)]))])

# Mantiska Markiry (portera): casco de mantis verde azulado con dos antenas grises largas, ojos amarillos de insecto a los
# lados y tres puntos negros en la frente; la cara verde pálido con una sonrisa y patas grises que salen por los lados
MT, MTD, MAG = _c('#2a7070'), _c('#1e5050'), _c('#a0a8b0')
def _mantis(view):
    if view == 'front':
        return [L([(36, 10), (10, -34)], MAG, 'f', False, False, 3), L([(64, 10), (90, -34)], MAG, 'f', False, False, 3),
                L([(16, 80), (0, 90), (-6, 108)], MAG, 'f', False, False, 3), L([(84, 80), (100, 90), (106, 108)], MAG, 'f', False, False, 3),
                L(outline([(14, 82), (2, 50), (10, 24), (30, 6), (50, 2), (70, 6), (90, 24), (98, 50), (86, 82), (70, 78), (56, 86), (50, 90, 1), (44, 86), (30, 78)]), MT, 'f'),
                cut([(4, 40), (14, 30), (20, 44), (10, 56)], _c('#c8c840')), cut([(96, 40), (86, 30), (80, 44), (90, 56)], _c('#c8c840')),
                L(outline([(18, 70), (34, 62), (42, 70), (30, 82)]), BLACK, 'f'), L(outline([(82, 70), (66, 62), (58, 70), (70, 82)]), BLACK, 'f'),
                L(ell(32, 72, 3.4, 4.4), _c('#f0b020'), 'f', False), L(ell(68, 72, 3.4, 4.4), _c('#f0b020'), 'f', False),
                L(ell(42, 26, 1.8, 1.8), BLACK, 'f', False), L(ell(58, 26, 1.8, 1.8), BLACK, 'f', False), L(ell(50, 34, 1.8, 1.8), BLACK, 'f', False)]
    if view == 'side':
        return [L([(60, 10), (40, -34)], MAG, 'f', False, False, 3), L([(50, 80), (30, 92), (20, 110)], MAG, 'f', False, False, 3),
                L(outline([(30, 84), (8, 60), (8, 30), (30, 6), (60, 2), (84, 18), (96, 46), (92, 66), (82, 86), (60, 84)]), MT, 'f'),
                cut([(56, 40), (70, 34), (72, 52), (60, 54)], _c('#c8c840')), L(outline([(72, 66), (90, 62), (92, 76), (78, 80)]), BLACK, 'f'),
                L(ell(84, 70, 3, 4), _c('#f0b020'), 'f', False)]
    return [L([(36, 10), (10, -34)], MAG, 'f', False, False, 3), L([(64, 10), (90, -34)], MAG, 'f', False, False, 3),
            L(outline([(12, 90), (2, 50), (10, 24), (30, 6), (50, 2), (70, 6), (90, 24), (98, 50), (88, 90), (50, 96)]), MT, 'f'),
            cut([(4, 40), (14, 30), (20, 44), (10, 56)], _c('#c8c840')), cut([(96, 40), (86, 30), (80, 44), (90, 56)], _c('#c8c840')), cut([(60, 8), (90, 26), (94, 80), (70, 88)], MTD)]
C('mantiska-markiry', 'chica', P('#2a7070', '#b8e0d0', iris='#141010', skin_d='#98c0b0'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, hairline=False, ears=False), _mantis('front'), _mantis('side'), _mantis('back'))

# Marigold Blossom: señora de pelo castaño claro recogido en un moño alto con un mechón ondulado que le cae por la derecha;
# ojos azules con pestañas y cara preocupada (con su modelo 3D)
C('marigold-blossom', 'chica', P('#9a7a62', '#f6d4b0', iris='#4a6ab0', shade='#7a5e48'),
  F(eyes='big', brows='sad', mouth='frown', mouth_y=94, hairline=[(14, 62), (20, 44), (34, 36), (50, 34), (66, 36), (80, 44), (86, 62)], nose=(50, 85, 2.4)),
  dome('front', top=6, w=42, cy=46, sb=58, seed=2) + [L(ell(54, -2, 12, 11)), fr([(80, 46), (90, 60), (86, 76), (92, 92), (86, 104, 1), (80, 86), (82, 66)])] +
  [L([(28, 70), (24, 66)], OUTC, 'f', False, False, 1.4), L([(72, 70), (76, 66)], OUTC, 'f', False, False, 1.4)],
  dome('side', top=6, w=42, cy=46, nape=72, fr=40, seed=2) + [L(ell(44, -2, 12, 11))],
  dome('back', top=6, w=42, cy=46, nape=72, seed=2) + [L(ell(50, -2, 12, 11)), fr([(70, 56), (84, 64), (84, 90), (78, 104, 1), (74, 80)])])

# Men Pukk: disfraz de búho: cabeza azul marino con la cara blanca en forma de corazón, ojos negros, pico rosa; el cuerpo
# marrón por debajo y una pluma roja y crema en lo alto
NB, OWB = _c('#2a4a6a'), _c('#7a3a2a')
def _owl(view):
    if view == 'front':
        return [L(outline([(2, 116), (4, 80), (14, 92), (50, 112), (86, 92), (96, 80), (98, 116), (50, 120)]), OWB, 'f'),
                L(outline([(12, 96), (6, 60), (12, 24), (32, 8), (50, 4), (68, 8), (88, 24), (94, 60), (88, 96), (50, 112)]), NB, 'f'),
                L(blob([(18, 64), (34, 52), (50, 62), (66, 52), (82, 64), (78, 84), (62, 96), (50, 102), (38, 96), (22, 84)], 6), WHITE, 'f', False),
                L(outline([(44, 4), (50, -24, 1), (56, 4)]), _c('#a8382a'), 'f'), L(ell(50, -8, 2.6, 5), _c('#f4e8d0'), 'f', False),
                L(ell(36, 70, 4.6, 5.4), BLACK, 'f', False), L(ell(64, 70, 4.6, 5.4), BLACK, 'f', False),
                L(outline([(46, 80), (54, 80), (50, 92, 1)]), _c('#f0b8b0'), 'f')]
    if view == 'side':
        return [L(outline([(10, 116), (8, 80), (40, 104), (90, 100), (94, 116), (50, 120)]), OWB, 'f'),
                L(outline([(14, 96), (6, 56), (16, 20), (40, 4), (66, 6), (86, 22), (94, 56), (90, 90), (60, 104)]), NB, 'f'),
                L(blob([(70, 60), (88, 56), (92, 80), (78, 96), (68, 84)], 5), WHITE, 'f', False), L(ell(82, 70, 3.4, 5), BLACK, 'f', False),
                L(outline([(88, 80), (96, 86, 1), (88, 90)]), _c('#f0b8b0'), 'f'), L(outline([(46, 4), (52, -24, 1), (58, 4)]), _c('#a8382a'), 'f')]
    return [L(outline([(2, 116), (4, 80), (50, 104), (96, 80), (98, 116), (50, 120)]), OWB, 'f'),
            L(outline([(10, 100), (6, 60), (12, 24), (32, 8), (50, 4), (68, 8), (88, 24), (94, 60), (90, 100), (50, 108)]), NB, 'f'),
            L(outline([(44, 4), (50, -24, 1), (56, 4)]), _c('#a8382a'), 'f')]
C('men-pukk', 'chica', P('#2a4a6a', '#f0c8a0'), F(**NOHEAD), _owl('front'), _owl('side'), _owl('back'))

# Mendry Charbeau: disfraz de pájaro naranja rojizo con dos cuernos rojos curvos, la cara blanca con ojos cerrados y un
# pico amarillo grande
OB, OBD = _c('#c8603a'), _c('#a04a2a')
def _hawk(view):
    if view == 'front':
        return [L(outline([(22, 10), (8, -24, 1), (30, 4)]), _c('#c02a2a'), 'f'), L(outline([(78, 10), (92, -24, 1), (70, 4)]), _c('#c02a2a'), 'f'),
                L(outline([(4, 116), (4, 60), (14, 24), (34, 8), (50, 4), (66, 8), (86, 24), (96, 60), (96, 116), (50, 120)]), OB, 'f'),
                L(blob([(16, 64), (34, 58), (50, 64), (66, 58), (84, 64), (80, 86), (62, 100), (50, 106), (38, 100), (20, 86)], 6), WHITE, 'f', False),
                L(quad((28, 72), (34, 68), (42, 72)), BLACK, 'f', False, False, 2.2), L(quad((58, 72), (66, 68), (72, 72)), BLACK, 'f', False, False, 2.2),
                L(outline([(38, 80), (62, 80), (56, 92), (50, 104, 1), (44, 92)]), YE, 'f')]
    if view == 'side':
        return [L(outline([(50, 10), (44, -24, 1), (60, 4)]), _c('#c02a2a'), 'f'),
                L(outline([(10, 116), (4, 60), (16, 20), (40, 4), (66, 6), (86, 22), (94, 56), (94, 116), (50, 120)]), OB, 'f'),
                L(blob([(70, 62), (90, 58), (94, 90), (78, 100)], 5), WHITE, 'f', False), L(quad((78, 72), (84, 68), (90, 72)), BLACK, 'f', False, False, 2.2),
                L(outline([(86, 78), (110, 90, 1), (88, 96)]), YE, 'f')]
    return [L(outline([(22, 10), (8, -24, 1), (30, 4)]), _c('#c02a2a'), 'f'), L(outline([(78, 10), (92, -24, 1), (70, 4)]), _c('#c02a2a'), 'f'),
            L(outline([(4, 116), (4, 60), (14, 24), (34, 8), (50, 4), (66, 8), (86, 24), (96, 60), (96, 116), (50, 120)]), OB, 'f'), cut([(62, 10), (88, 28), (94, 112), (70, 114)], OBD)]
C('mendry-charbeau', 'chica', P('#c8603a', '#f0c8a0'), F(**NOHEAD), _hawk('front'), _hawk('side'), _hawk('back'))

# Menoh Seaweed: piel azul claro, melena verde claro como un alga, abultada en grandes ondas a los lados; ojos rojos
C('menoh-seaweed', 'chica', P('#8ad870', '#a8d0e8', iris='#c02020', shade='#5aa848', skin_d='#88b0c8'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=[(14, 64), (24, 58), (34, 66), (44, 56), (54, 66), (66, 56), (78, 64), (86, 64)]),
  [L(outline([(16, 104), (-6, 92), (-2, 76), (-10, 62), (2, 44), (6, 22), (26, 4), (50, -2), (74, 4), (94, 22), (98, 44), (110, 62), (102, 76), (106, 92), (84, 104),
              (78, 60), (22, 60)])),
   cut([(70, 6), (94, 24), (98, 46), (108, 62), (100, 76), (104, 90), (84, 100), (82, 56)], 'shade'),
   fr([(18, 58), (24, 70, 1), (32, 56), (44, 68, 1), (50, 56), (58, 68, 1), (66, 56), (76, 70, 1), (82, 58)])],
  [L(outline([(60, 56), (66, 40), (86, 30), (82, 10), (56, -2), (30, 2), (6, 22), (-6, 44), (-10, 66), (-4, 90), (16, 104), (40, 100), (56, 84)]))],
  [L(outline([(10, 104), (-6, 92), (-2, 76), (-10, 62), (2, 44), (6, 22), (26, 4), (50, -2), (74, 4), (94, 22), (98, 44), (110, 62), (102, 76), (106, 92), (90, 104),
              (50, 108)])), cut([(66, 6), (94, 24), (98, 46), (108, 62), (100, 80), (90, 102), (70, 104)], 'shade')])

# Mesa Bute (portera): piel morena, pelo verde recogido en dos grandes moños de bultos con gomas rojas, dos coletas largas
# que caen por delante, una marca de corazón crema en la frente y ojos verde azulado
GRN2, GRN2D = _c('#2e9a6a'), _c('#1e7050')
def _flower(cx, cy, r=14):
    pts = []
    import math
    for i in range(10):
        a = math.pi * 2 * i / 10
        k = 1.0 if i % 2 == 0 else 0.72
        pts.append((cx + r * k * math.cos(a), cy + r * k * math.sin(a)))
    return blob(pts, 6)
C('mesa-bute', 'chica', P('#2e9a6a', '#b8845e', iris='#2a8a8a', shade='#1e7050'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=[(14, 62), (20, 46), (34, 38), (50, 40), (66, 38), (80, 46), (86, 62)]),
  [L(_flower(-4, 18, 23)), L(_flower(104, 18, 23)), L(ell(16, 32, 4, 7), _c('#c84a3a'), 'f'), L(ell(84, 32, 4, 7), _c('#c84a3a'), 'f')] +
  dome('front', top=10, w=40, cy=46, sb=60, seed=3) +
  [fr([(18, 60), (24, 60), (24, 106), (20, 112, 1), (16, 106)]), fr([(82, 60), (76, 60), (76, 106), (80, 112, 1), (84, 106)]),
   L(blob([(44, 44), (50, 48), (56, 44), (56, 50), (50, 56), (44, 50)], 3), _c('#f0dcb0'), 'f', False)],
  [L(_flower(40, 14, 23))] + dome('side', top=10, w=40, cy=46, nape=72, fr=44, seed=3) + [fr([(56, 64), (62, 64), (60, 108), (56, 112, 1)])],
  [L(_flower(-4, 18, 23)), L(_flower(104, 18, 23))] + dome('back', top=10, w=40, cy=46, nape=72, seed=3))

# Metha Nol: pelo rosa salmón en una llama alta de mechones de punta, piel amarilla con una franja gris azulada que le
# cruza la cara en diagonal, orejas de punta con un pendiente azul y sonrisa de dientes
C('metha-nol', 'normal', P('#f0a0a0', '#f0c878', iris='#3a6ab0', shade='#d07878', skin_d='#d0a858'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, hairline=[(14, 60), (20, 44), (30, 50), (40, 38), (50, 48), (60, 38), (70, 48), (82, 44), (86, 60)]),
  ears_pointy('front', 'skin', 8) +
  [L(outline([(14, 60), (10, 36), (20, 22), (24, 0, 1), (36, 14), (44, -28, 1), (52, 6), (60, -10, 1), (64, 12), (78, 4, 1), (78, 22), (90, 36), (86, 60), (76, 46),
              (24, 46)])),
   cut([(52, 0), (60, -10), (64, 12), (78, 4), (80, 26), (88, 44), (78, 44), (66, 20)], 'shade'),
   cut([(30, 46), (40, 46), (50, 74), (48, 100), (40, 100), (40, 74)], _c('#8a96a8')),
   L(ell(86, 84, 2, 2), _c('#2a6ab0'), 'f')],
  ears_pointy('side', 'skin', 8) +
  [L(outline([(54, 56), (62, 40), (80, 34), (88, 18), (72, 6, 1), (60, 10), (56, -24, 1), (44, 4), (22, -6, 1), (24, 14), (6, 24), (8, 52), (22, 64), (42, 60)])),
   L(ell(42, 82, 2, 2), _c('#2a6ab0'), 'f')],
  ears_pointy('back', 'skin', 8) +
  [L(outline([(16, 72), (10, 36), (20, 22), (24, 0, 1), (36, 14), (44, -28, 1), (52, 6), (60, -10, 1), (64, 12), (78, 4, 1), (78, 22), (90, 36), (84, 72), (50, 76)]))])

# Mikala Datasby: piel azul claro, pelo granate en pinchos grandes despeinados, orejas de punta muy anchas, pintura verde
# en las mejillas, ojos verdes de párpado caído y media sonrisa
C('mikala-datasby', 'normal', P('#a83040', '#a8d0e0', iris='#2a8a5a', shade='#7a2030', skin_d='#88b0c0'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=[(14, 60), (20, 44), (32, 50), (42, 40), (54, 50), (64, 40), (76, 48), (86, 60)]),
  [L(outline([(16, 64), (-14, 52, 1), (14, 80)]), 'skin', 'b'), L(outline([(84, 64), (114, 52, 1), (86, 80)]), 'skin', 'b')] +
  [L(outline([(14, 60), (2, 46, 1), (14, 36), (4, 14, 1), (26, 16), (30, -12, 1), (44, 8), (58, -18, 1), (62, 6), (84, -6, 1), (78, 16), (98, 22, 1), (88, 36),
              (98, 48, 1), (86, 60), (76, 44), (24, 44)])),
   cut([(58, 0), (84, -6), (78, 16), (96, 22), (88, 38), (84, 54), (72, 30)], 'shade'),
   L([(32, 82), (30, 92)], _c('#2a9a6a'), 'f', False, False, 3), L([(68, 82), (70, 92)], _c('#2a9a6a'), 'f', False, False, 3)],
  [L(outline([(40, 66), (20, 48, 1), (52, 62), (50, 78)]), 'skin', 'f'),
   L(outline([(54, 56), (62, 40), (84, 34), (94, 16, 1), (74, 12), (78, -12, 1), (58, 4), (44, -18, 1), (36, 6), (12, -2, 1), (16, 18), (-2, 30, 1), (8, 44), (4, 60, 1),
              (22, 64), (42, 60)]))],
  [L(outline([(16, 64), (-14, 52, 1), (14, 80)]), 'skin', 'b'), L(outline([(84, 64), (114, 52, 1), (86, 80)]), 'skin', 'b'),
   L(outline([(16, 72), (2, 46, 1), (14, 36), (4, 14, 1), (26, 16), (30, -12, 1), (44, 8), (58, -18, 1), (62, 6), (84, -6, 1), (78, 16), (98, 22, 1), (88, 36),
              (98, 48, 1), (84, 72), (50, 76)]))])

# Milo Agrias: capucha morada oscura en punta con una cinta rosa y dos cuernos blancos curvos hacia fuera; el pelo morado le
# cae a los lados y un mechón le tapa medio ojo; piel muy blanca y ojos verde lima
PUR, PURD = _c('#3a3260'), _c('#2a2448')
def _milo(view):
    if view == 'front':
        return [L(outline([(6, 96), (-14, 70), (2, 60), (6, 30), (30, 4), (50, -14, 1), (70, 4), (94, 30), (98, 60), (114, 70), (94, 96), (80, 94), (82, 52), (18, 52),
                           (20, 94)]), PUR),
                L(outline([(24, 20), (50, 14), (76, 20), (74, 28), (50, 22), (26, 28)]), _c('#d07898'), 'f'),
                L(outline([(14, 50), (-8, 36), (-4, 30), (18, 40)]), WHITE, 'f'), L(outline([(86, 50), (108, 36), (104, 30), (82, 40)]), WHITE, 'f'),
                fr([(50, 26), (60, 50), (58, 82, 1), (48, 60), (40, 50)], PUR)]
    if view == 'side':
        return [L(outline([(54, 60), (62, 44), (84, 34), (76, 10), (50, -14, 1), (26, 6), (6, 30), (-8, 62), (4, 94), (30, 98), (50, 80)]), PUR),
                L(outline([(30, 14), (60, 6), (64, 14), (34, 22)]), _c('#d07898'), 'f'), L(outline([(40, 44), (14, 30), (16, 24), (44, 36)]), WHITE, 'f')]
    return [L(outline([(6, 98), (-14, 70), (2, 60), (6, 30), (30, 4), (50, -14, 1), (70, 4), (94, 30), (98, 60), (114, 70), (94, 98), (50, 102)]), PUR),
            L(outline([(24, 20), (50, 14), (76, 20), (74, 28), (50, 22), (26, 28)]), _c('#d07898'), 'f'),
            L(outline([(14, 50), (-8, 36), (-4, 30), (18, 40)]), WHITE, 'f'), L(outline([(86, 50), (108, 36), (104, 30), (82, 40)]), WHITE, 'f')]
C('milo-agrias', 'chica', P('#3a3260', '#f6f0f0', iris='#8ac020', shade='#2a2448'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=94, hairline=[(14, 60), (50, 52), (86, 60)]), _milo('front'), _milo('side'), _milo('back'))

# Minack Sargo (portero): piel verde azulado pálido, pelo verde oliva alborotado en mechones largos con una punta alta que
# se dobla, flequillo que le cae sobre la cara; ojos castaños y sonrisa
C('minack-sargo', 'normal', P('#a09a48', '#a8d0c0', iris='#9a4a2a', shade='#7a7430', skin_d='#88b0a0'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=93, hairline=[(14, 64), (20, 50), (30, 62), (40, 48), (50, 64), (60, 50), (72, 62), (80, 50), (86, 64)]),
  dome('front', top=0, w=48, cy=46, n=9, amp=10, sweep=0.4, seed=11, sb=74) + [L(outline([(48, 4), (60, -26, 1), (66, 6)])),
                                                                           fr([(24, 46), (32, 66, 1), (40, 48), (50, 70, 1), (58, 48), (66, 66, 1), (74, 46)])],
  dome('side', top=0, w=48, cy=46, n=9, amp=10, sweep=0.4, seed=11, nape=88, fr=52) + [L(outline([(44, 4), (60, -26, 1), (60, 8)]))],
  dome('back', top=0, w=48, cy=46, n=9, amp=10, sweep=0.4, seed=11, nape=90) + [L(outline([(48, 4), (60, -26, 1), (66, 6)]))])

# Miriam Sharpe: pelo naranja vivo en media melena de mechones de punta, un flequillo largo que le cruza la cara; ojos
# morados grandes y sonrisa (con su modelo 3D)
C('miriam-sharpe', 'chica', P('#f07a20', '#fadcb4', iris='#7a6ab0', shade='#c85a10'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(10, 64), (20, 54), (30, 62), (40, 48), (52, 62), (62, 50), (74, 60), (84, 52), (90, 64)]),
  dome('front', top=2, w=46, cy=46, n=7, amp=8, soft=False, seed=13, long=86, flare=8) + [fr([(30, 40), (46, 44), (58, 50), (50, 70, 1), (42, 54), (34, 64, 1)])],
  dome('side', top=2, w=46, cy=46, n=7, amp=8, seed=13, long=86, fr=50),
  dome('back', top=2, w=46, cy=46, n=7, amp=8, seed=13, long=88, ends=4))

# Mitchi Osha: casco gris de escarabajo con un cuerno negro grande curvo a cada lado y una cresta en medio; la cara muy
# blanca, ojos morados con pestañas y sonrisa
SG, SGD, HK = _c('#9a9aa8'), _c('#72727e'), _c('#2a2a38')
def _beetle(view):
    if view == 'front':
        return [L(outline([(10, 100), (4, 60), (10, 30), (28, 12), (50, 6), (72, 12), (90, 30), (96, 60), (90, 100), (80, 98), (82, 62), (50, 52), (18, 62), (20, 98)]), SG, 'f'),
                L(outline([(34, 58), (16, 30), (22, -10), (30, -24, 1), (32, -6), (28, 22), (46, 50)]), HK, 'f'),
                L(outline([(66, 58), (84, 30), (78, -10), (70, -24, 1), (68, -6), (72, 22), (54, 50)]), HK, 'f'),
                L(outline([(40, 54), (50, 2), (60, 54), (50, 60)]), SGD, 'f'), cut([(6, 70), (14, 66), (18, 100), (8, 100)], _c('#c03a2a'))]
    if view == 'side':
        return [L(outline([(10, 100), (4, 60), (12, 26), (34, 8), (62, 6), (84, 22), (92, 46), (70, 52), (56, 66), (56, 100)]), SG, 'f'),
                L(outline([(70, 52), (88, 20), (82, -14), (76, -24, 1), (74, -6), (76, 20), (60, 46)]), HK, 'f')]
    return [L(outline([(8, 104), (4, 60), (10, 30), (28, 12), (50, 6), (72, 12), (90, 30), (96, 60), (92, 104), (50, 108)]), SG, 'f'),
            L(outline([(30, 30), (18, 0), (28, -22, 1), (30, 0), (40, 24)]), HK, 'f'), L(outline([(70, 30), (82, 0), (72, -22, 1), (70, 0), (60, 24)]), HK, 'f'),
            cut([(60, 10), (90, 30), (94, 100), (70, 104)], SGD)]
C('mitchi-osha', 'chica', P('#9a9aa8', '#f8f0f4', iris='#8a4ab0', skin_d='#e0d0dc'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=False, ears=False), _beetle('front'), _beetle('side'), _beetle('back'))

# Moka Rimmer: grandullón de cara verde, con una melena naranja rojiza enorme que le tapa los ojos y una barba naranja que
# le rodea la boca; un pendiente azul en una oreja
C('moka-rimmer', 'corpulento', P('#d0602a', '#80b8a0', iris='#141010', shade='#a8481e', skin_d='#609880'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=96, hairline=False, face_front=face(w=4, jaw=3)),
  [L(outline([(2, 104), (-4, 70), (2, 40), (12, 16), (34, 0), (50, -2), (66, 0), (88, 16), (98, 40), (104, 70), (98, 104), (84, 100), (80, 80), (20, 80), (16, 100)])),
   fr([(16, 40), (30, 30), (50, 28), (70, 30), (84, 40), (84, 78), (76, 82, 1), (70, 70), (62, 84, 1), (56, 72), (50, 86, 1), (44, 72), (38, 84, 1), (30, 70), (22, 82, 1)]),
   fr([(18, 86), (30, 92), (40, 104), (60, 104), (70, 92), (82, 86), (84, 104), (70, 120), (50, 124), (30, 120), (16, 104)]),
   L(ell(14, 90, 2.4, 3), _c('#3a8ad0'), 'f'), L(ell(44, 84, 2, 1.6), _c('#4a8870'), 'f', False), L(ell(56, 84, 2, 1.6), _c('#4a8870'), 'f', False)],
  [L(outline([(60, 70), (66, 40), (86, 30), (80, 8), (54, -4), (26, 2), (4, 22), (-6, 56), (0, 96), (30, 106), (52, 96)])),
   fr([(70, 40), (92, 46), (94, 82, 1), (84, 72), (78, 86, 1), (70, 76)]), fr([(66, 88), (90, 92), (92, 114), (70, 122), (60, 108)])],
  [L(outline([(2, 108), (-4, 70), (2, 40), (12, 16), (34, 0), (50, -2), (66, 0), (88, 16), (98, 40), (104, 70), (98, 108), (50, 114)])),
   cut([(62, 6), (90, 22), (100, 70), (94, 104), (70, 110)], 'shade')])

# Mony Tarling: la cabeza es una tele gris con la cara pintada (ojos de punto y una boca en w), una antena amarilla encima y
# dos altavoces redondos grises a los lados
TVG, TVD, SCR = _c('#4a4e58'), _c('#30343c'), _c('#c8d0dc')
def _tvh(view):
    if view == 'front':
        return [L(ell(4, 70, 8, 14), _c('#8a8e98'), 'f'), L(ell(96, 70, 8, 14), _c('#8a8e98'), 'f'),
                L(blob([(30, 32), (50, 22), (70, 32)], 6) + [(70, 34), (30, 34)], _c('#e8c030'), 'f'), L([(50, 24), (50, 4)], _c('#c8a020'), 'f', False, False, 2.4),
                L(ell(50, 2, 3.4, 3.4), _c('#e8c030'), 'f'),
                L(blob([(4, 40), (96, 40), (96, 102), (4, 102)], 8), TVG, 'f'), L(blob([(12, 48), (88, 48), (88, 94), (12, 94)], 6), SCR, 'f', False),
                L(blob([(22, 62), (28, 60), (30, 66), (24, 68)], 3), BLACK, 'f', False), L(blob([(78, 62), (72, 60), (70, 66), (76, 68)], 3), BLACK, 'f', False),
                L([(32, 76), (40, 88), (50, 78), (60, 88), (68, 76)], BLACK, 'f', False, False, 4.6)]
    if view == 'side':
        return [L(blob([(30, 32), (50, 22), (66, 32)], 6) + [(66, 34), (30, 34)], _c('#e8c030'), 'f'), L([(48, 24), (48, 4)], _c('#c8a020'), 'f', False, False, 2.4),
                L(ell(48, 2, 3.4, 3.4), _c('#e8c030'), 'f'), L(blob([(10, 40), (90, 40), (90, 102), (10, 102)], 8), TVG, 'f'),
                L(ell(48, 70, 9, 14), _c('#8a8e98'), 'f'), L(outline([(86, 46), (94, 46), (94, 96), (86, 96)]), SCR, 'f')]
    return [L(ell(4, 70, 8, 14), _c('#8a8e98'), 'f'), L(ell(96, 70, 8, 14), _c('#8a8e98'), 'f'),
            L(blob([(30, 32), (50, 22), (70, 32)], 6) + [(70, 34), (30, 34)], _c('#e8c030'), 'f'), L([(50, 24), (50, 4)], _c('#c8a020'), 'f', False, False, 2.4),
            L(ell(50, 2, 3.4, 3.4), _c('#e8c030'), 'f'), L(blob([(4, 40), (96, 40), (96, 102), (4, 102)], 8), TVG, 'f'),
            cut([(14, 50), (86, 50), (86, 92), (14, 92)], TVD)]
C('mony-tarling', 'normal', P('#4a4e58', '#c8906a'), F(**NOHEAD), _tvh('front'), _tvh('side'), _tvh('back'))

# Morr Fauche: melena verde agua enorme que se abre en dos alas a los lados con manchas azules, dos plumas naranjas que le
# salen de la frente hacia fuera, flequillo en mechones, piel muy blanca y ojos azules serios
MW, MWD = _c('#9adcc0'), _c('#6ab8a0')
C('morr-fauche', 'chica', P('#9adcc0', '#f6f2f2', iris='#3a6ab0', shade='#6ab8a0'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=94, hairline=[(14, 62), (22, 56), (32, 64), (42, 54), (50, 64), (58, 54), (68, 64), (78, 56), (86, 62)]),
  [L(outline([(18, 104), (-16, 92), (-26, 64), (-4, 50), (4, 22), (28, 2), (50, -4), (72, 2), (96, 22), (104, 50), (126, 64), (116, 92), (82, 104), (78, 60),
              (22, 60)])),
   L(ell(-8, 70, 3, 5), _c('#2a5ab0'), 'f', False), L(ell(2, 82, 3, 5), _c('#2a5ab0'), 'f', False),
   L(ell(108, 70, 3, 5), _c('#2a5ab0'), 'f', False), L(ell(98, 82, 3, 5), _c('#2a5ab0'), 'f', False),
   L(outline([(46, 40), (14, 10), (8, 16), (38, 46)]), _c('#f0a060'), 'f'), L(outline([(54, 40), (86, 10), (92, 16), (62, 46)]), _c('#f0a060'), 'f'),
   fr([(20, 56), (26, 68, 1), (34, 54), (44, 70, 1), (50, 54), (56, 70, 1), (66, 54), (74, 68, 1), (80, 56)])],
  [L(outline([(58, 56), (66, 40), (86, 30), (82, 8), (56, -4), (28, 2), (6, 22), (-10, 48), (-30, 70), (-14, 96), (20, 104), (50, 90)])),
   L(ell(-14, 76, 3, 5), _c('#2a5ab0'), 'f', False), L(outline([(76, 32), (96, 4), (100, 10), (82, 38)]), _c('#f0a060'), 'f')],
  [L(outline([(14, 106), (-16, 92), (-26, 64), (-4, 50), (4, 22), (28, 2), (50, -4), (72, 2), (96, 22), (104, 50), (126, 64), (116, 92), (86, 106), (50, 110)])),
   L(ell(-8, 70, 3, 5), _c('#2a5ab0'), 'f', False), L(ell(108, 70, 3, 5), _c('#2a5ab0'), 'f', False)])

# Mozun Yarne: disfraz de pájaro verde grisáceo con capucha azul marino de borde blanco, ojos con pestañas y un pico rosa
# pálido largo; el cuello blanco con dos círculos azules
MZ, NVB = _c('#5a8a7a'), _c('#2a3460')
def _mozun(view):
    if view == 'front':
        return [L(outline([(-2, 116), (2, 60), (10, 22), (32, 4), (50, 0), (68, 4), (90, 22), (98, 60), (102, 116), (50, 122)]), NVB, 'f'),
                L(outline([(6, 116), (10, 70), (30, 92), (50, 104), (70, 92), (90, 70), (94, 116), (50, 120)]), WHITE, 'f'),
                L(ell(14, 104, 5, 5) + [ell(14, 104, 5, 5)[0]], NVB, 'f', False, False, 2.6), L(ell(86, 104, 5, 5) + [ell(86, 104, 5, 5)[0]], NVB, 'f', False, False, 2.6),
                L(outline([(16, 90), (12, 50), (20, 22), (50, 10), (80, 22), (88, 50), (84, 90), (50, 112)]), MZ, 'f'),
                L(outline([(42, 74), (58, 74), (56, 92), (50, 98, 1), (44, 92)]), _c('#f0c8b8'), 'f')] + sharp_eyes(_c('#b04a6a'), ey=70, sep=15)
    if view == 'side':
        return [L(outline([(4, 116), (2, 60), (12, 22), (36, 4), (62, 4), (84, 20), (94, 54), (96, 116), (50, 122)]), NVB, 'f'),
                L(outline([(46, 110), (60, 90), (88, 70), (96, 116)]), WHITE, 'f'),
                L(outline([(46, 92), (44, 50), (54, 20), (80, 16), (92, 40), (92, 74), (80, 96), (60, 104)]), MZ, 'f'),
                L(outline([(88, 70), (104, 84, 1), (88, 90)]), _c('#f0c8b8'), 'f')] + sharp_eye_side(_c('#b04a6a'), 66)
    return [L(outline([(-2, 116), (2, 60), (10, 22), (32, 4), (50, 0), (68, 4), (90, 22), (98, 60), (102, 116), (50, 122)]), NVB, 'f'),
            cut([(62, 8), (90, 26), (98, 110), (70, 114)], _c('#1e2648'))]
C('mozun-yarne', 'normal', P('#2a3460', '#f0c8a0'), F(**NOHEAD), _mozun('front'), _mozun('side'), _mozun('back'))

# Mr. Shipwood (portero): señor de pelo castaño grisáceo con raya al lado y patillas largas, gafas rectangulares azules y
# boca torcida (con su modelo 3D)
from chars_scouts_ie1_03 import rect_specs  # noqa: E402
C('mr-shipwood', 'delgado', P('#8a7a62', '#f8dcb0', iris='#3a2a20', shade='#6a5c48'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, face_front=face(chin=106), face_side=face_side(chin=5),
    hairline=[(14, 62), (18, 44), (30, 36), (44, 34), (56, 40), (70, 38), (82, 44), (86, 62)], nose=(50, 86, 2.4)),
  dome('front', top=4, w=42, cy=46, sb=78, seed=3) + [fr([(44, 28), (60, 30), (78, 40), (82, 52), (64, 40)])] + rect_specs('front', _c('#3a7ab0'), y=77),
  dome('side', top=4, w=42, cy=46, nape=80, fr=40, seed=3) + rect_specs('side', _c('#3a7ab0'), y=77),
  dome('back', top=4, w=42, cy=46, nape=80, seed=3))

# Mr. Veteran (portero): abuelo de cara naranja con un gorro de lana rojo, nariz enorme marrón, bigotazo blanco y patillas
# blancas, cejas blancas pobladas y ojos pequeños (con su modelo 3D)
RDH = _c('#c82828')
C('mr-veteran', 'corpulento', P('#e8e8e8', '#e8a060', iris='#141010', skin_d='#c88048'),
  F(eyes='dot', brows=False, mouth='none', hairline=False, face_front=face(w=4, chin=106, jaw=3)),
  [L(blob([(14, 50), (16, 22), (34, 4), (50, 0), (66, 4), (84, 22), (86, 50), (50, 46)], 6), RDH),
   L(outline([(12, 44), (50, 40), (88, 44), (88, 54), (50, 50), (12, 54)]), _c('#a81e1e'), 'f'),
   fr([(14, 56), (22, 58), (24, 84), (14, 90)], WHITE), fr([(86, 56), (78, 58), (76, 84), (86, 90)], WHITE),
   L(blob([(28, 66), (40, 62), (44, 68), (30, 70)], 4), WHITE, 'f'), L(blob([(72, 66), (60, 62), (56, 68), (70, 70)], 4), WHITE, 'f'),
   L(blob([(14, 92), (30, 84), (50, 92), (70, 84), (86, 92), (76, 102), (60, 98), (50, 102), (40, 98), (24, 102)], 5), WHITE, 'f'),
   L(blob([(40, 70), (60, 70), (64, 86), (50, 94), (36, 86)], 6), _c('#a86a3a'), 'f')],
  [L(blob([(12, 52), (16, 20), (40, 2), (66, 4), (86, 22), (90, 50), (50, 50)], 6), RDH), L(outline([(10, 46), (90, 44), (90, 54), (10, 56)]), _c('#a81e1e'), 'f'),
   fr([(46, 58), (56, 58), (56, 84), (48, 88)], WHITE), L(blob([(76, 64), (88, 62), (88, 68), (78, 70)], 4), WHITE, 'f'),
   L(blob([(80, 72), (98, 76), (98, 90), (84, 92)], 6), _c('#a86a3a'), 'f'), L(blob([(70, 92), (96, 92), (90, 102), (72, 100)], 5), WHITE, 'f')],
  [L(blob([(14, 52), (16, 22), (34, 4), (50, 0), (66, 4), (84, 22), (86, 52), (50, 50)], 6), RDH), L(outline([(12, 46), (88, 46), (88, 56), (12, 56)]), _c('#a81e1e'), 'f'),
   L(outline([(16, 58), (84, 58), (84, 80), (50, 86), (16, 80)]), WHITE)])

# Nactena Naksey: alienígena de piel azul claro con una cresta de joyas azules redondas por la cabeza y melena lila
# esponjosa abultada a los lados; ojos negros rasgados con pestañas y boquita pequeña
C('nactena-naksey', 'chica', P('#d8c8f0', '#a8d0e8', iris='#141010', shade='#b0a0d8', skin_d='#88b0c8'),
  F(eyes='sharp', brows=False, mouth='none', hairline=False),
  [L(outline([(16, 110), (-6, 100), (2, 88), (-8, 74), (4, 62), (-2, 48), (10, 36), (90, 36), (102, 48), (96, 62), (108, 74), (98, 88), (106, 100), (84, 110),
              (80, 70), (20, 70)])),
   skull('front')[0], L(blob([(42, 8), (50, 0), (58, 8), (56, 20), (44, 20)], 4), _c('#2a4ab0'), 'f'),
   L(ell(26, 24, 5, 6), _c('#2a4ab0'), 'f'), L(ell(74, 24, 5, 6), _c('#2a4ab0'), 'f'), L(ell(16, 48, 4, 8), _c('#2a4ab0'), 'f'), L(ell(84, 48, 4, 8), _c('#2a4ab0'), 'f'),
   L([(28, 66), (40, 62)], BLACK, 'f', False, False, 1.4), L([(72, 66), (60, 62)], BLACK, 'f', False, False, 1.4),
   L(ell(50, 92, 2, 2.4), _c('#6a8aa8'), 'f', False)],
  [L(outline([(50, 110), (20, 106), (0, 94), (-6, 70), (4, 50), (30, 46), (50, 70)])), skull3('side')[0],
   L(blob([(56, 4), (66, 2), (70, 12), (60, 16)], 4), _c('#2a4ab0'), 'f'), L(ell(30, 20, 5, 6), _c('#2a4ab0'), 'f')],
  [L(outline([(10, 112), (-6, 100), (2, 88), (-8, 74), (4, 62), (-2, 48), (10, 30), (30, 10), (50, 4), (70, 10), (90, 30), (102, 48), (96, 62), (108, 74), (98, 88),
              (106, 100), (90, 112), (50, 116)])),
   L(blob([(42, 8), (50, 0), (58, 8), (56, 20), (44, 20)], 4), _c('#2a4ab0'), 'f'), L(ell(26, 24, 5, 6), _c('#2a4ab0'), 'f'), L(ell(74, 24, 5, 6), _c('#2a4ab0'), 'f')])

# Nathan "Nate" Adams: pelo castaño en pinchos de punta hacia arriba, ojos castaños grandes y sonrisa
C('nathan-nate-adams', 'normal', P('#7a4a2a', '#fadcb4', iris='#5a3a2a', shade='#5a341e'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(14, 62), (20, 48), (30, 56), (40, 44), (50, 56), (60, 44), (70, 56), (80, 48), (86, 62)]),
  dome('front', top=4, w=44, cy=46, n=7, amp=7, seed=21, sb=66) + [L(outline([(40, 8), (46, -24, 1), (54, 4), (62, -16, 1), (64, 10)]))],
  dome('side', top=4, w=44, cy=46, n=7, amp=7, seed=21, nape=84, fr=48) + [L(outline([(40, 6), (50, -24, 1), (56, 4)]))],
  dome('back', top=4, w=44, cy=46, n=7, amp=7, seed=21, nape=84) + [L(outline([(40, 8), (46, -24, 1), (54, 4), (62, -16, 1), (64, 10)]))])

# Nathanos Hoshten (portera): capucha roja de mariquita con lunares oscuros y una pieza marrón en la frente, dos cuernos
# crema largos, mechones rubios a los lados; cara lila clara con los ojos cerrados de felicidad
LDR, LDD = _c('#b83a2a'), _c('#5a2a20')
def _lady(view):
    if view == 'front':
        out = [L(outline([(30, 30), (16, -10, 1), (36, 22)]), _c('#f0e0c0'), 'f'), L(outline([(70, 30), (84, -10, 1), (64, 22)]), _c('#f0e0c0'), 'f'),
               L(outline([(10, 100), (-4, 84), (2, 60), (8, 30), (30, 10), (50, 6), (70, 10), (92, 30), (98, 60), (104, 84), (90, 100), (78, 96), (80, 54), (50, 44),
                          (20, 54), (22, 96)]), LDR, 'f'),
               L(outline([(30, 24), (50, 16), (70, 24), (64, 44), (50, 50), (36, 44)]), LDD, 'f'),
               fr([(22, 54), (36, 50), (30, 66), (24, 72)], _c('#e8d088')), fr([(78, 54), (64, 50), (70, 66), (76, 72)], _c('#e8d088'))]
        for x, y in ((6, 64), (12, 84), (94, 64), (88, 84), (20, 36), (80, 36)):
            out.append(L(ell(x, y, 4, 4.6), LDD, 'f', False))
        return out
    if view == 'side':
        return [L(outline([(54, 30), (60, -10, 1), (64, 24)]), _c('#f0e0c0'), 'f'),
                L(outline([(10, 100), (-2, 80), (4, 40), (24, 14), (50, 6), (76, 14), (88, 34), (80, 50), (62, 48), (56, 72), (54, 100)]), LDR, 'f'),
                L(ell(14, 64, 4, 4.6), LDD, 'f', False), L(ell(28, 84, 4, 4.6), LDD, 'f', False), L(ell(30, 34, 4, 4.6), LDD, 'f', False)]
    out = [L(outline([(30, 30), (16, -10, 1), (36, 22)]), _c('#f0e0c0'), 'f'), L(outline([(70, 30), (84, -10, 1), (64, 22)]), _c('#f0e0c0'), 'f'),
           L(outline([(10, 104), (-4, 84), (2, 60), (8, 30), (30, 10), (50, 6), (70, 10), (92, 30), (98, 60), (104, 84), (90, 104), (50, 108)]), LDR, 'f')]
    for x, y in ((14, 70), (30, 90), (70, 90), (86, 70), (34, 40), (66, 40), (50, 64)):
        out.append(L(ell(x, y, 5, 5.6), LDD, 'f', False))
    return out
C('nathanos-hoshten', 'chica', P('#e8d088', '#f0d8f0', iris='#141010', skin_d='#d8bcd8'),
  F(eyes='closed', brows=False, mouth='smile', mouth_y=93, hairline=False, ears=False), _lady('front'), _lady('side'), _lady('back'))

# Ned Jovan (portero): la cabeza es un casco de hierro gris con remaches, dos tornillos marrones a los lados, ojos redondos
# amarillos y una boca cuadrada negra de dientes
IRN, IRD, RIV = _c('#9a9aa0'), _c('#8a7a70'), _c('#4a3a30')
def _iron(view):
    if view == 'front':
        out = [L(outline([(-2, 60), (14, 56), (14, 76), (-2, 72)]), _c('#9a7a68'), 'f'), L(outline([(102, 60), (86, 56), (86, 76), (102, 72)]), _c('#9a7a68'), 'f'),
               L(blob([(12, 108), (10, 30), (24, 6), (50, 0), (76, 6), (90, 30), (88, 108)], 8), IRD, 'f'),
               L(blob([(22, 104), (20, 34), (30, 14), (50, 8), (70, 14), (80, 34), (78, 104)], 8), IRN, 'f', False),
               L(ell(34, 70, 6, 6), _c('#2a3a4a'), 'f', False), L(ell(66, 70, 6, 6), _c('#2a3a4a'), 'f', False),
               L(ell(34, 70, 4, 4), _c('#f0e070'), 'f', False), L(ell(66, 70, 4, 4), _c('#f0e070'), 'f', False),
               L([(36, 86), (64, 86), (64, 100), (60, 96), (56, 100), (52, 96), (48, 100), (44, 96), (40, 100), (36, 96)], BLACK, 'f', False)]
        for i in range(8):
            out.append(L(ell(16, 30 + i * 10, 1.2, 1.2), RIV, 'f', False))
            out.append(L(ell(84, 30 + i * 10, 1.2, 1.2), RIV, 'f', False))
        return out
    if view == 'side':
        return [L(blob([(12, 108), (8, 30), (26, 6), (56, 0), (80, 10), (92, 34), (90, 108)], 8), IRD, 'f'),
                L(outline([(40, 60), (56, 56), (56, 80), (40, 76)]), _c('#9a7a68'), 'f'), L(blob([(70, 20), (88, 34), (88, 104), (76, 104)], 6), IRN, 'f', False),
                L(ell(84, 70, 3, 5), _c('#f0e070'), 'f', False)]
    out = [L(outline([(-2, 60), (14, 56), (14, 76), (-2, 72)]), _c('#9a7a68'), 'f'), L(outline([(102, 60), (86, 56), (86, 76), (102, 72)]), _c('#9a7a68'), 'f'),
           L(blob([(12, 108), (10, 30), (24, 6), (50, 0), (76, 6), (90, 30), (88, 108)], 8), IRD, 'f')]
    for i in range(8):
        out.append(L(ell(50, 14 + i * 12, 1.2, 1.2), RIV, 'f', False))
    return out
C('ned-jovan', 'normal', P('#8a7a70', '#c8906a'), F(**NOHEAD), _iron('front'), _iron('side'), _iron('back'))

# Nemy Minimiz: alienígena azul claro, calvo, con dos orejas larguísimas de conejo (moradas por dentro) y una antena
# acabada en una bola verde agua; ojos grandes de espiral azul y boca pequeña seria
NBL = _c('#a8d8ec')
C('nemy-minimiz', 'normal', P('#a8d8ec', '#a8d8ec', iris='#3a5aa8', skin_d='#88b8d0'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=94, hairline=False, ears=False),
  [L(outline([(26, 40), (2, -16), (8, -24), (40, 30)]), 'skin', 'b'), L(outline([(74, 40), (98, -16), (92, -24), (60, 30)]), 'skin', 'b'),
   L(outline([(24, 34), (8, -12), (12, -16), (34, 28)]), _c('#8a7ac0'), 'b', False), L(outline([(76, 34), (92, -12), (88, -16), (66, 28)]), _c('#8a7ac0'), 'b', False)] +
  skull('front') + [L(quad((50, 10), (56, -6), (60, -18)), OUTC, 'f', False, False, 1.6), L(ell(60, -20, 4.6, 4.6), _c('#6ad0c0'), 'f')],
  [L(outline([(46, 30), (20, -20), (28, -26), (56, 24)]), 'skin', 'f'), L(outline([(46, 24), (28, -16), (32, -20), (52, 20)]), _c('#8a7ac0'), 'f', False)] +
  skull3('side') + [L(quad((56, 4), (66, -8), (70, -18)), OUTC, 'f', False, False, 1.6), L(ell(70, -20, 4.6, 4.6), _c('#6ad0c0'), 'f')],
  [L(outline([(26, 40), (2, -16), (8, -24), (40, 30)]), 'skin', 'b'), L(outline([(74, 40), (98, -16), (92, -24), (60, 30)]), 'skin', 'b')] + skull3('back') +
  [L(quad((50, 10), (56, -6), (60, -18)), OUTC, 'f', False, False, 1.6), L(ell(60, -20, 4.6, 4.6), _c('#6ad0c0'), 'f')])

# Nenban Slate (portero): cabeza de dinosaurio naranja con un rombo crema en la frente, ojos negros de párpado caído, una
# coleta crema y rosa enorme que sale de lo alto hacia atrás y una boca alargada
NOR = _c('#d0785a')
def _dino(view):
    if view == 'front':
        return [L(outline([(48, 10), (30, -14), (6, -14), (-6, -4), (14, -6), (30, 2), (40, 14)]), _c('#e8c8c0'), 'b'),
                L(outline([(20, 100), (14, 60), (18, 24), (34, 6), (50, 2), (66, 6), (82, 24), (86, 60), (80, 100), (64, 112), (50, 114), (36, 112)]), NOR, 'f'),
                L(outline([(50, 14), (56, 28), (50, 44), (44, 28)]), _c('#f0dcc0'), 'f', False), L(outline([(38, 36), (44, 44), (38, 54), (32, 44)]), _c('#f0dcc0'), 'f', False),
                L(outline([(62, 36), (68, 44), (62, 54), (56, 44)]), _c('#f0dcc0'), 'f', False), L(outline([(50, 48), (54, 54), (50, 60), (46, 54)]), _c('#f0dcc0'), 'f', False),
                L(blob([(24, 70), (34, 64), (40, 72), (32, 78)], 4), WHITE, 'f', False), L(blob([(76, 70), (66, 64), (60, 72), (68, 78)], 4), WHITE, 'f', False),
                L(ell(32, 72, 3, 3), BLACK, 'f', False), L(ell(68, 72, 3, 3), BLACK, 'f', False),
                L([(24, 68), (38, 64)], BLACK, 'f', False, False, 2.4), L([(76, 68), (62, 64)], BLACK, 'f', False, False, 2.4),
                L(quad((40, 100), (50, 104), (60, 100)), BLACK, 'f', False, False, 1.6)]
    if view == 'side':
        return [L(outline([(40, 10), (20, -10), (-10, -10), (-20, 0), (0, 0), (20, 8), (30, 18)]), _c('#e8c8c0'), 'f'),
                L(outline([(30, 104), (20, 60), (26, 22), (48, 4), (70, 8), (86, 26), (94, 60), (100, 92), (92, 108), (60, 112)]), NOR, 'f'),
                L(blob([(78, 66), (90, 64), (90, 76), (80, 76)], 4), WHITE, 'f', False), L(ell(86, 70, 2.6, 3), BLACK, 'f', False)]
    return [L(outline([(48, 10), (30, -14), (6, -14), (-6, -4), (14, -6), (30, 2), (40, 14)]), _c('#e8c8c0'), 'f'),
            L(outline([(20, 102), (14, 60), (18, 24), (34, 6), (50, 2), (66, 6), (82, 24), (86, 60), (80, 102), (50, 110)]), NOR, 'f')]
C('nenban-slate', 'normal', P('#d0785a', '#f0c8a0'), F(**NOHEAD), _dino('front'), _dino('side'), _dino('back'))

# Niall Rugan: gorro azul de bulto con dos ojos pintados y una bola amarilla encima, que le tapa los lados de la cara;
# cara azul claro con la boca en zigzag
NRB = _c('#2a8ab0')
def _niall(view):
    if view == 'front':
        return [L(outline([(10, 106), (2, 70), (6, 30), (26, 8), (50, 2), (74, 8), (94, 30), (98, 70), (90, 106), (78, 100), (80, 70), (50, 60), (20, 70), (22, 100)]), NRB, 'f'),
                L(ell(38, 38, 5, 5) + [ell(38, 38, 5, 5)[0]], BLACK, 'f', False, False, 2), L(ell(62, 38, 5, 5) + [ell(62, 38, 5, 5)[0]], BLACK, 'f', False, False, 2),
                L(ell(38, 38, 1.6, 1.6), BLACK, 'f', False), L(ell(62, 38, 1.6, 1.6), BLACK, 'f', False), L(ell(26, 14, 8, 7), _c('#f0c820'), 'f'),
                L([(36, 88), (42, 80), (50, 88), (58, 80), (64, 88)], BLACK, 'f', False, False, 2)]
    if view == 'side':
        return [L(outline([(10, 106), (2, 70), (8, 30), (30, 6), (60, 2), (82, 16), (92, 40), (78, 60), (60, 70), (56, 104)]), NRB, 'f'),
                L(ell(80, 34, 4, 5) + [ell(80, 34, 4, 5)[0]], BLACK, 'f', False, False, 2), L(ell(40, 6, 8, 7), _c('#f0c820'), 'f')]
    return [L(outline([(10, 108), (2, 70), (6, 30), (26, 8), (50, 2), (74, 8), (94, 30), (98, 70), (90, 108), (50, 112)]), NRB, 'f'), L(ell(74, 14, 8, 7), _c('#f0c820'), 'f')]
C('niall-rugan', 'normal', P('#2a8ab0', '#a8d8ec', skin_d='#88b8d0'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False), _niall('front'), _niall('side'), _niall('back'))

# Nico Burz: capucha blanca de conejo con las orejas caídas largas a los lados (oscuras por dentro); cara crema con cejas
# negras gruesas, ojos de pupila pequeña y marcas negras en la frente, boca seria
def _nico(view):
    if view == 'front':
        return [L(outline([(4, 116), (-4, 70), (2, 30), (24, 6), (50, 0), (76, 6), (98, 30), (104, 70), (96, 116), (82, 114), (80, 54), (50, 46), (20, 54), (18, 114)]), WHITE, 'f'),
                cut([(4, 80), (14, 70), (16, 112), (6, 112)], _c('#5a4a4a')), cut([(96, 80), (86, 70), (84, 112), (94, 112)], _c('#5a4a4a')),
                L([(24, 64), (42, 68)], BLACK, 'f', False, False, 4), L([(76, 64), (58, 68)], BLACK, 'f', False, False, 4),
                L([(44, 54), (48, 64)], BLACK, 'f', False, False, 1.4), L([(56, 54), (52, 64)], BLACK, 'f', False, False, 1.4)]
    if view == 'side':
        return [L(outline([(10, 116), (-2, 70), (6, 28), (32, 4), (62, 4), (84, 20), (90, 44), (70, 52), (56, 70), (52, 116)]), WHITE, 'f'),
                cut([(20, 70), (40, 64), (44, 110), (24, 110)], _c('#e0d8d8')), L([(76, 64), (88, 66)], BLACK, 'f', False, False, 4)]
    return [L(outline([(4, 116), (-4, 70), (2, 30), (24, 6), (50, 0), (76, 6), (98, 30), (104, 70), (96, 116), (50, 120)]), WHITE, 'f'),
            cut([(60, 8), (94, 30), (98, 110), (72, 114)], _c('#e4dede'))]
C('nico-burz', 'normal', P('#f4f4f4', '#f6ecc0', iris='#141010', skin_d='#dccca0'),
  F(eyes='dot', brows=False, mouth='frown', mouth_y=95, hairline=False, ears=False), _nico('front'), _nico('side'), _nico('back'))

# Nio Rentall: pelo azul marino en mechones de punta echados a un lado con un mechón amarillo, orejas largas de punta
# blancas; piel blanca con sombra morada en los ojos amarillos
C('nio-rentall', 'normal', P('#2a3a7a', '#f4f4f8', iris='#e0b020', shade='#1e2a5a', skin_d='#d8d8e0'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=94, hairline=[(14, 60), (20, 44), (32, 52), (42, 40), (54, 54), (62, 44), (74, 54), (82, 46), (86, 60)]),
  ears_pointy('front', 'skin', 30) +
  [L(outline([(14, 60), (10, 34), (22, 14), (36, 6), (46, -12, 1), (52, 6), (72, 6), (88, 22), (90, 40), (86, 60), (74, 44), (60, 52), (54, 74, 1), (46, 52), (24, 46)])),
   L(outline([(70, 6), (82, 12), (86, 30), (80, 40), (76, 22)]), _c('#f0c030'), 'f'),
   cut([(24, 70), (40, 72), (42, 80), (26, 78)], _c('#8a6ab0')), cut([(76, 70), (60, 72), (58, 80), (74, 78)], _c('#8a6ab0'))] + sharp_eyes(_c('#e0b020')),
  ears_pointy('side', 'skin', 30) +
  [L(outline([(54, 56), (62, 40), (82, 30), (90, 14, 1), (70, 8), (52, -12, 1), (36, 2), (14, 10), (4, 30), (6, 54), (20, 64), (42, 60)]))] + sharp_eye_side(_c('#e0b020')),
  ears_pointy('back', 'skin', 30) +
  [L(outline([(16, 70), (10, 34), (22, 14), (36, 6), (46, -12, 1), (52, 6), (72, 6), (88, 22), (90, 40), (84, 70), (50, 74)])),
   L(outline([(28, 8), (18, 14), (14, 32), (20, 40), (24, 22)]), _c('#f0c030'), 'f')])

# Nomare Lusha: melena larga azul grisácea en mechones gruesos que le enmarcan la cara; piel crema con marcas verde agua
# (gotas en la frente, rayas en las mejillas), ojos verde agua con pestañas y labios verdes
C('nomare-lusha', 'chica', P('#5a7a98', '#f0d4b0', iris='#4a9aa8', shade='#3e5a74'),
  F(eyes='sharp', brows=False, mouth='none', hairline=[(14, 64), (22, 46), (34, 40), (50, 44), (66, 40), (78, 46), (86, 64)]),
  dome('front', top=2, w=46, cy=46, long=102, flare=6, seed=4) +
  [L(blob([(50, 36), (54, 44), (50, 52), (46, 44)], 3), _c('#5ab0a8'), 'f', False), L(ell(42, 52, 2.4, 3), _c('#5ab0a8'), 'f', False), L(ell(58, 52, 2.4, 3), _c('#5ab0a8'), 'f', False),
   L([(26, 84), (34, 88)], _c('#5ab0a8'), 'f', False, False, 2.6), L([(74, 84), (66, 88)], _c('#5ab0a8'), 'f', False, False, 2.6),
   L(ell(50, 96, 4, 2), _c('#5aa898'), 'f', False), L([(26, 70), (22, 66)], OUTC, 'f', False, False, 1.4), L([(74, 70), (78, 66)], OUTC, 'f', False, False, 1.4)],
  dome('side', top=2, w=46, cy=46, long=102, seed=4, fr=44) + [L([(76, 84), (84, 88)], _c('#5ab0a8'), 'f', False, False, 2.6)],
  dome('back', top=2, w=46, cy=46, long=104, seed=4, ends=5))

# Norlan Rikwatta (portero): grandullón de cara verde con un casco azul marino de dos cuernos crema y una estrella blanca
# en la frente; el casco le baja hasta la nariz en pico, ojos naranjas afilados y boca seria
NVY = _c('#2e3460')
def _norlan(view):
    if view == 'front':
        return [L(outline([(16, 34), (-4, 20), (2, -16, 1), (8, 12), (24, 26)]), _c('#d8cca0'), 'f'), L(outline([(84, 34), (104, 20), (98, -16, 1), (92, 12), (76, 26)]), _c('#d8cca0'), 'f'),
                L(outline([(6, 84), (-4, 60), (8, 50), (8, 24), (30, 10), (50, 6), (70, 10), (92, 24), (92, 50), (104, 60), (94, 84), (82, 70), (66, 70), (56, 80), (50, 92, 1),
                           (44, 80), (34, 70), (18, 70)]), NVY, 'f'),
                L(outline([(50, 14), (56, 30), (72, 34), (56, 40), (50, 56), (44, 40), (28, 34), (44, 30)]), _c('#d8d8e8'), 'f', False)] + sharp_eyes(_c('#e08a20'), ey=74)
    if view == 'side':
        return [L(outline([(50, 30), (62, 4), (58, -16, 1), (70, 8), (64, 30)]), _c('#d8cca0'), 'f'),
                L(outline([(10, 92), (0, 60), (6, 26), (30, 8), (62, 6), (84, 20), (94, 50), (92, 70), (78, 70), (64, 64), (56, 80), (40, 92)]), NVY, 'f')] + sharp_eye_side(_c('#e08a20'), 74)
    return [L(outline([(16, 34), (-4, 20), (2, -16, 1), (8, 12), (24, 26)]), _c('#d8cca0'), 'f'), L(outline([(84, 34), (104, 20), (98, -16, 1), (92, 12), (76, 26)]), _c('#d8cca0'), 'f'),
            L(outline([(6, 92), (-4, 60), (8, 50), (8, 24), (30, 10), (50, 6), (70, 10), (92, 24), (92, 50), (104, 60), (94, 92), (50, 98)]), NVY, 'f')]
C('norlan-rikwatta', 'corpulento', P('#2e3460', '#78a890', iris='#e08a20', skin_d='#5a8a70'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, hairline=False, ears=False, face_front=face(w=4, jaw=3)), _norlan('front'), _norlan('side'), _norlan('back'))

# Norritz Ranhatch (portero): casco naranja de insecto con dos ojos morados enormes, dos antenas blancas en ángulo y una
# raya roja; asoma la cara morena por debajo con una sonrisa
ORH = _c('#e8a030')


def _ant(pts):
    """Antena blanca con contorno oscuro."""
    return [L(pts, OUTC, 'f', False, False, 6), L(pts, WHITE, 'f', False, False, 3.6)]


def _norritz(view):
    if view == 'front':
        return _ant([(36, 14), (28, -4), (34, -26)]) + _ant([(64, 14), (72, -4), (66, -26)]) + [
                L(outline([(16, 84), (10, 50), (16, 20), (34, 6), (50, 2), (66, 6), (84, 20), (90, 50), (84, 84), (66, 80), (50, 84), (34, 80)]), ORH, 'f'),
                L(outline([(18, 50), (30, 36), (46, 52), (40, 70), (26, 72)]), _c('#8a3a90'), 'f'), L(outline([(82, 50), (70, 36), (54, 52), (60, 70), (74, 72)]), _c('#8a3a90'), 'f'),
                L([(30, 30), (50, 40), (70, 30)], _c('#c03020'), 'f', False, False, 1.8), L(ell(50, 64, 3, 3), _c('#8a3a90'), 'f')]
    if view == 'side':
        return _ant([(60, 12), (68, -6), (62, -28)]) + [
                L(outline([(14, 88), (4, 50), (14, 20), (40, 4), (66, 6), (86, 22), (94, 50), (90, 82), (60, 86)]), ORH, 'f'),
                L(outline([(70, 40), (90, 44), (90, 68), (74, 70)]), _c('#8a3a90'), 'f')]
    return _ant([(36, 14), (28, -4), (34, -26)]) + _ant([(64, 14), (72, -4), (66, -26)]) + [
            L(outline([(14, 90), (10, 50), (16, 20), (34, 6), (50, 2), (66, 6), (84, 20), (90, 50), (86, 90), (50, 94)]), ORH, 'f')]
C('norritz-ranhatch', 'normal', P('#e8a030', '#b8845e', skin_d='#966644'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, hairline=False, ears=False), _norritz('front'), _norritz('side'), _norritz('back'))

# Oggris Roya (portera): melena verde agua muy larga y lisa con dos mechones que se levantan como orejas puntiagudas; piel
# verde pálido, ojos grises y sonrisa
C('oggris-roya', 'chica', P('#3ac8a0', '#c8e8dc', iris='#6a6a70', shade='#28a080', skin_d='#a8c8bc'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=[(14, 64), (24, 50), (36, 46), (50, 52), (64, 46), (76, 50), (86, 64)]),
  dome('front', top=6, w=42, cy=46, long=112, flare=10, seed=5) +
  [L(outline([(18, 30), (14, -8, 1), (36, 16)])), L(outline([(82, 30), (86, -8, 1), (64, 16)])), fr([(38, 38), (52, 42), (48, 56, 1), (42, 46)])],
  dome('side', top=6, w=42, cy=46, long=112, seed=5, fr=48) + [L(outline([(40, 14), (40, -10, 1), (56, 10)]))],
  dome('back', top=6, w=42, cy=46, long=114, seed=5, ends=5) + [L(outline([(18, 30), (14, -8, 1), (36, 16)])), L(outline([(82, 30), (86, -8, 1), (64, 16)]))])

# Okai Cosmer: capucha crema de calamar con dos cuernos marrones curvos de carnero a los lados y tentáculos que le caen a los
# lados de la cara con las puntas verde agua; cara muy blanca y ojos azules enfadados
CRE, HRN = _c('#f0e4cc'), _c('#9a7050')
def _okai(view):
    if view == 'front':
        return [L(outline([(16, 40), (-14, 30), (-22, 44), (-14, 50), (-6, 42), (10, 50)]), HRN, 'f'), L(outline([(84, 40), (114, 30), (122, 44), (114, 50), (106, 42), (90, 50)]), HRN, 'f'),
                L(outline([(14, 110), (6, 70), (4, 34), (22, 10), (50, 4), (78, 10), (96, 34), (94, 70), (86, 110), (78, 106), (80, 62), (50, 50), (20, 62), (22, 106)]), CRE, 'f'),
                L(ell(14, 108, 4, 3), _c('#7ad0c0'), 'f', False), L(ell(86, 108, 4, 3), _c('#7ad0c0'), 'f', False),
                L([(30, 40), (36, 52)], _c('#c8b898'), 'f', False, False, 1.6), L([(70, 40), (64, 52)], _c('#c8b898'), 'f', False, False, 1.6)] + sharp_eyes(_c('#2a6a98'))
    if view == 'side':
        return [L(outline([(50, 40), (30, 30), (24, 48), (34, 52), (36, 44), (52, 50)]), HRN, 'f'),
                L(outline([(30, 110), (10, 70), (8, 30), (34, 6), (64, 6), (86, 24), (90, 46), (70, 56), (58, 76), (56, 110)]), CRE, 'f'),
                L(ell(56, 108, 4, 3), _c('#7ad0c0'), 'f', False)] + sharp_eye_side(_c('#2a6a98'))
    return [L(outline([(16, 40), (-14, 30), (-22, 44), (-14, 50), (-6, 42), (10, 50)]), HRN, 'f'), L(outline([(84, 40), (114, 30), (122, 44), (114, 50), (106, 42), (90, 50)]), HRN, 'f'),
            L(outline([(12, 112), (6, 70), (4, 34), (22, 10), (50, 4), (78, 10), (96, 34), (94, 70), (88, 112), (50, 116)]), CRE, 'f')]
C('okai-cosmer', 'chica', P('#f0e4cc', '#f8f6f6', iris='#2a6a98', skin_d='#e0dcdc'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=94, hairline=False, ears=False), _okai('front'), _okai('side'), _okai('back'))

# Otto Sheveme: yelmo rosado de punta alta con una cresta en medio y lunares negros en las mejillas, que le baja hasta la
# nariz; melena amarilla a los lados y la cara gris por debajo
PKH = _c('#b07a70')
def _otto(view):
    if view == 'front':
        return [L(outline([(8, 100), (2, 74), (10, 50), (90, 50), (98, 74), (92, 100), (80, 96), (80, 60), (20, 60), (20, 96)]), _c('#d8b030'), 'f'),
                L(outline([(14, 70), (10, 40), (24, 14), (44, -4), (50, -28, 1), (56, -4), (76, 14), (90, 40), (86, 70), (70, 72), (60, 84), (50, 88, 1), (40, 84), (30, 72)]), PKH, 'f'),
                L([(50, -20), (50, 60)], _c('#e8c8c0'), 'f', False, False, 2)] + \
            [L(ell(x, y, 1.6, 1.6), BLACK, 'f', False) for x, y in ((24, 66), (30, 70), (28, 62), (76, 66), (70, 70), (72, 62))] + sharp_eyes(BLACK, ey=76)
    if view == 'side':
        return [L(outline([(10, 100), (4, 70), (14, 56), (50, 60), (52, 100)]), _c('#d8b030'), 'f'),
                L(outline([(10, 74), (6, 40), (24, 12), (50, -4), (58, -28, 1), (64, -2), (82, 14), (92, 40), (90, 66), (74, 72), (60, 84), (40, 80)]), PKH, 'f')]
    return [L(outline([(8, 104), (2, 74), (10, 50), (90, 50), (98, 74), (92, 104), (50, 108)]), _c('#d8b030'), 'f'),
            L(outline([(14, 74), (10, 40), (24, 14), (44, -4), (50, -28, 1), (56, -4), (76, 14), (90, 40), (86, 74), (50, 80)]), PKH, 'f')]
C('otto-sheveme', 'normal', P('#d8b030', '#9a9aa0', iris='#141010', skin_d='#80808a'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=95, hairline=False, ears=False), _otto('front'), _otto('side'), _otto('back'))

# Perrick Ambin (portero): disfraz de pelícano blanco con la bolsa del pico amarilla enorme que le tapa media cara; ojos
# rojizos de párpado caído
def _pelican(view):
    if view == 'front':
        return [L(outline([(4, 116), (2, 60), (14, 24), (34, 8), (44, -4), (56, -4), (66, 8), (86, 24), (98, 60), (96, 116), (50, 120)]), WHITE, 'f'),
                L(blob([(16, 82), (34, 76), (50, 78), (66, 76), (84, 82), (80, 106), (62, 118), (50, 120), (38, 118), (20, 106)], 6), _c('#e8d48a'), 'f'),
                L(outline([(40, 76), (60, 76), (54, 86), (46, 86)]), _c('#d8b860'), 'f', False),
                L(blob([(24, 64), (40, 60), (44, 70), (28, 72)], 4), _c('#8a6060'), 'f', False), L(blob([(76, 64), (60, 60), (56, 70), (72, 72)], 4), _c('#8a6060'), 'f', False),
                L(ell(34, 67, 2.6, 2.6), BLACK, 'f', False), L(ell(66, 67, 2.6, 2.6), BLACK, 'f', False),
                L([(24, 62), (42, 60)], BLACK, 'f', False, False, 2), L([(76, 62), (58, 60)], BLACK, 'f', False, False, 2)]
    if view == 'side':
        return [L(outline([(10, 116), (2, 60), (14, 24), (40, 4), (66, 6), (86, 22), (92, 56), (94, 116), (50, 120)]), WHITE, 'f'),
                L(blob([(60, 78), (112, 80), (100, 110), (70, 118)], 6), _c('#e8d48a'), 'f'), L(ell(80, 66, 2.6, 2.6), BLACK, 'f', False)]
    return [L(outline([(4, 116), (2, 60), (14, 24), (34, 8), (44, -4), (56, -4), (66, 8), (86, 24), (98, 60), (96, 116), (50, 120)]), WHITE, 'f'),
            cut([(62, 10), (90, 30), (96, 110), (72, 114)], _c('#e0dcdc'))]
C('perrick-ambin', 'normal', P('#f4f4f4', '#b8845e'), F(**NOHEAD), _pelican('front'), _pelican('side'), _pelican('back'))

# Piranu Rajelly: pelo verde agua claro despeinado que le tapa los ojos, con las puntas rosas, y dos mechones larguísimos
# que se levantan como orejas de conejo; piel verde pálido
C('piranu-rajelly', 'normal', P('#a0dcc0', '#b8dcc8', iris='#141010', shade='#78b89c', skin_d='#98bca8'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=95, hairline=False),
  [L(outline([(30, 20), (10, -30), (18, -34), (40, 14)])), L(outline([(70, 20), (90, -30), (82, -34), (60, 14)])),
   L(outline([(12, 92), (4, 50), (12, 20), (34, 6), (50, 2), (66, 6), (88, 20), (96, 50), (88, 92), (80, 80), (74, 92, 1), (66, 80), (58, 90, 1), (50, 80), (42, 90, 1),
              (34, 80), (26, 92, 1), (20, 80)])),
   cut([(14, 80), (20, 78), (26, 90), (16, 90)], _c('#e8a8b8')), cut([(86, 80), (80, 78), (74, 90), (84, 90)], _c('#e8a8b8')),
   cut([(44, 82), (56, 82), (50, 90)], _c('#e8a8b8'))],
  [L(outline([(50, 16), (40, -30), (48, -34), (60, 12)])),
   L(outline([(60, 84), (66, 50), (86, 40), (82, 12), (56, 2), (28, 6), (6, 24), (-2, 56), (6, 90), (30, 96), (50, 92)]))],
  [L(outline([(30, 20), (10, -30), (18, -34), (40, 14)])), L(outline([(70, 20), (90, -30), (82, -34), (60, 14)])),
   L(outline([(12, 96), (4, 50), (12, 20), (34, 6), (50, 2), (66, 6), (88, 20), (96, 50), (88, 96), (50, 100)])),
   cut([(14, 86), (86, 86), (88, 96), (12, 96)], _c('#e8a8b8'))])

# Ptumri Emnator: pelo negro con mechones rizados de punta encima, unas gafas de buceo blancas y azules sobre la frente, un
# flequillo que le tapa un ojo y dos coletas de bolas a los lados; orejas largas de punta (con su modelo 3D)
C('ptumri-emnator', 'normal', P('#2a2a2a', '#f8dcb4', iris='#3a3a6a', shade='#1a1a1a'),
  F(eyes='sharp', brows=True, mouth='line', mouth_y=94, hairline=[(14, 62), (20, 46), (34, 44), (50, 40), (66, 44), (80, 46), (86, 62)]),
  ears_pointy('front', 'skin', 18) + dome('front', top=6, w=42, cy=46, sb=70, seed=6) +
  [L(quad((26, 12), (16, -6), (26, -14)), 'mid', 'f', False, False, 3), L(quad((60, 6), (66, -12), (78, -10)), 'mid', 'f', False, False, 3),
   L(ell(10, 96, 7, 7)), L(ell(90, 96, 7, 7)), L(ell(12, 108, 6, 6)), L(ell(88, 108, 6, 6)),
   L(blob([(14, 28), (50, 20), (86, 28), (86, 40), (50, 34), (14, 40)], 5), WHITE, 'f'), L(ell(32, 32, 7, 5), _c('#4a8ac0'), 'f'), L(ell(68, 32, 7, 5), _c('#4a8ac0'), 'f'),
   fr([(46, 40), (64, 46), (70, 70), (62, 82, 1), (56, 62), (46, 52)])],
  ears_pointy('side', 'skin', 18) + dome('side', top=6, w=42, cy=46, nape=84, fr=44, seed=6) +
  [L(ell(46, 98, 7, 7)), L(blob([(40, 24), (88, 26), (90, 38), (40, 36)], 5), WHITE, 'f'), L(ell(80, 32, 6, 5), _c('#4a8ac0'), 'f')],
  ears_pointy('back', 'skin', 18) + dome('back', top=6, w=42, cy=46, nape=84, seed=6) +
  [L(ell(10, 96, 7, 7)), L(ell(90, 96, 7, 7)), L(ell(12, 108, 6, 6)), L(ell(88, 108, 6, 6)), L(outline([(10, 34), (90, 34), (90, 40), (10, 40)]), _c('#4a8ac0'), 'f')])

# Res Ord (portero): casco amarillo de cara entera con dos rombos blancos en la frente, una melena roja oscura en pétalos
# alrededor como un león, ojos blancos de pupila pequeña enfadados y un hocico crema
RDB, YH = _c('#a8341e'), _c('#e8c040')
def _lion(cx, cy, r):
    import math
    pts = []
    for i in range(24):
        a = math.pi * 2 * i / 24
        k = 1.0 if i % 2 == 0 else 0.78
        pts.append((cx + r * k * math.cos(a), cy + r * 0.95 * k * math.sin(a)) + ((1,) if i % 2 == 0 else ()))
    return pts
def _resord(view):
    if view == 'front':
        return [L(outline(_lion(50, 66, 54)), RDB, 'f'), L(outline([(36, 10), (44, -16, 1), (50, 6), (58, -14, 1), (62, 10)]), RDB, 'f'),
                L(outline([(22, 100), (16, 60), (20, 30), (36, 12), (50, 8), (64, 12), (80, 30), (84, 60), (78, 100), (50, 108)]), YH, 'f'),
                L(outline([(50, 18), (58, 28), (50, 38), (42, 28)]), WHITE, 'f', False), L(outline([(50, 34), (58, 44), (50, 54), (42, 44)]), WHITE, 'f', False),
                L(blob([(36, 86), (50, 82), (64, 86), (60, 100), (40, 100)], 5), _c('#f4ecd8'), 'f', False)] + sharp_eyes(BLACK, ey=72) + \
               [L(quad((44, 96), (50, 92), (56, 96)), BLACK, 'f', False, False, 1.6)]
    if view == 'side':
        return [L(outline(_lion(40, 66, 50)), RDB, 'f'),
                L(outline([(50, 100), (46, 60), (52, 26), (68, 12), (82, 24), (90, 50), (94, 84), (86, 104)]), YH, 'f')] + sharp_eye_side(BLACK, 72)
    return [L(outline(_lion(50, 66, 54)), RDB, 'f'), L(outline([(36, 10), (44, -16, 1), (50, 6), (58, -14, 1), (62, 10)]), RDB, 'f')]
C('res-ord', 'normal', P('#a8341e', '#f0c8a0'), F(**NOHEAD), _resord('front'), _resord('side'), _resord('back'))

# Ribo Som: gorro morado en punta curvada hacia atrás que le cubre la cabeza hasta las cejas; orejas largas de punta, ojos
# verde lima afilados y boca entreabierta
C('ribo-som', 'normal', P('#5a4aa8', '#f6d4b0', iris='#9ac020', shade='#3e3480'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=[(14, 62), (30, 58), (44, 64), (50, 60), (56, 64), (70, 58), (86, 62)]),
  ears_pointy('front', 'skin', 14) +
  [L(outline([(2, 76), (6, 40), (22, 14), (46, 2), (62, -18), (72, -28, 1), (70, -6), (80, 12), (94, 40), (98, 76), (80, 60), (60, 60), (50, 66, 1), (40, 60), (20, 60)])),
   cut([(60, 2), (70, -6), (80, 12), (94, 42), (96, 70), (80, 58), (76, 30)], 'shade')],
  ears_pointy('side', 'skin', 14) +
  [L(outline([(88, 62), (92, 40), (76, 12), (50, 2), (24, -10), (10, -26, 1), (14, -4), (4, 30), (2, 64), (20, 70), (40, 64), (60, 60)]))],
  ears_pointy('back', 'skin', 14) +
  [L(outline([(2, 80), (6, 40), (22, 14), (46, 2), (62, -18), (72, -28, 1), (70, -6), (80, 12), (94, 40), (98, 80), (50, 84)]))])

# Riccardo Gabriel Gabardo: pelo castaño rojizo largo y ondulado hasta los hombros, recogido abajo en dos coletas; ojos
# verdes y cara seria
C('riccardo-gabriel-gabardo', 'normal', P('#8a5a48', '#f6d4b0', iris='#3a8a6a', shade='#6a4234'),
  F(eyes='sharp', brows=True, mouth='frown', mouth_y=94, hairline=[(14, 62), (22, 48), (36, 42), (50, 46), (64, 42), (78, 48), (86, 62)]),
  dome('front', top=4, w=44, cy=46, long=96, flare=4, seed=8, n=8, amp=4, soft=True) + [L(ell(12, 100, 7, 8)), L(ell(88, 100, 7, 8)), L(ell(14, 112, 5, 5)), L(ell(86, 112, 5, 5))],
  dome('side', top=4, w=44, cy=46, long=96, seed=8, n=8, amp=4, soft=True, fr=46) + [L(ell(40, 102, 7, 8))],
  dome('back', top=4, w=44, cy=46, long=96, seed=8, n=8, amp=4, soft=True, ends=3) + [L(ell(12, 100, 7, 8)), L(ell(88, 100, 7, 8))])

# Ricky Regomen (portero): capucha verde agua de rana con las orejas largas caídas a los lados (oscuras en las puntas);
# cara amarilla pálida con ojos enormes blancos de pupila pequeña, mofletes rosas y una sonrisa enorme de dientes
FRG = _c('#6aa898')
def _frog(view):
    if view == 'front':
        return [L(outline([(4, 116), (-4, 60), (6, 24), (28, 4), (50, 0), (72, 4), (94, 24), (104, 60), (96, 116), (84, 116), (84, 60), (50, 40), (16, 60), (16, 116)]), FRG, 'f'),
                cut([(-2, 96), (14, 92), (16, 116), (2, 116)], _c('#4a5a40')), cut([(102, 96), (86, 92), (84, 116), (98, 116)], _c('#4a5a40')),
                L([(30, 10), (34, 4)], BLACK, 'f', False, False, 1.4), L([(70, 10), (66, 4)], BLACK, 'f', False, False, 1.4),
                L(ell(34, 70, 9, 10), WHITE, 'f'), L(ell(66, 70, 9, 10), WHITE, 'f'), L(ell(34, 72, 2.6, 3), BLACK, 'f', False), L(ell(66, 72, 2.6, 3), BLACK, 'f', False),
                L(ell(22, 88, 5, 3.4), _c('#f0a8a0'), 'f', False), L(ell(78, 88, 5, 3.4), _c('#f0a8a0'), 'f', False)] + big_grin(y=94, w=18, h=9)
    if view == 'side':
        return [L(outline([(10, 116), (0, 60), (10, 24), (36, 4), (64, 4), (84, 18), (90, 40), (70, 50), (56, 70), (54, 116)]), FRG, 'f'),
                cut([(14, 96), (40, 92), (44, 116), (18, 116)], _c('#4a5a40')), L(ell(82, 70, 6, 9), WHITE, 'f'), L(ell(84, 72, 2.4, 3), BLACK, 'f', False)]
    return [L(outline([(4, 116), (-4, 60), (6, 24), (28, 4), (50, 0), (72, 4), (94, 24), (104, 60), (96, 116), (50, 120)]), FRG, 'f'),
            cut([(-2, 96), (20, 92), (22, 116), (2, 116)], _c('#4a5a40')), cut([(102, 96), (80, 92), (78, 116), (98, 116)], _c('#4a5a40'))]
C('ricky-regomen', 'normal', P('#6aa898', '#f4ecc0', iris='#141010', skin_d='#dcd4a8'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, face_front=face(w=6, chin=104)), _frog('front'), _frog('side'), _frog('back'))
