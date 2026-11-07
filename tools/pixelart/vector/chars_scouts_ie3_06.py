"""Ojeadores de IE3 (scouts-ie3), tanda 06: dibujados a partir de su retrato de Victory Road; claves 'scouts-ie3:<id>'.

Ninguno tiene modelo 3D propio: el frente sale del retrato y el perfil y la espalda se deducen de cómo cae el pelo o el
gorro. Usa dome()/hl()/face() de la tanda 09 de IE1 y añade unos pocos ayudantes de gorros: cap() (casquete que tapa la
cabeza hasta rim), band() (cinta o borde alrededor de la cabeza) y arc()."""
import math

from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars_scouts_ie1_09 import F, P, _c, dome, face, face_side, hl, mark  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)


def C(pid, body, palette, f, front, side, back):
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        # el nacimiento del pelo baja por el borde de la cara: así su raya no cruza el pelo de los lados
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[f'scouts-ie3:{pid}'] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def arc(cx, cy, rx, ry, a0, a1, n=14):
    """Puntos de un arco de elipse de a0 a a1 grados (0 = derecha, 90 = arriba)."""
    return [(cx + rx * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy - ry * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]


def cap(view, c, top=0, rim=56, w=47, drop=12, z='b', ln=False):
    """Casquete (gorro, casco, capucha) que tapa la cabeza desde top hasta rim; drop: cuánto baja por detrás de perfil."""
    if view == 'front':
        pts = arc(50, rim, w, rim - top, 180, 0) + [(50 + w, rim + 3), (50, rim - 1), (50 - w, rim + 3)]
    elif view == 'side':
        pts = arc(47, rim, w, rim - top, 180, 0) + [(47 + w, rim - 2), (60, rim + 2), (30, rim + drop * 0.7), (47 - w, rim + drop)]
    else:
        pts = arc(50, rim + 4, w, rim + 4 - top, 180, 0) + [(50 + w, rim + drop), (50, rim + drop + 4), (50 - w, rim + drop)]
    return L(outline(pts), c, z, True, ln)


def band(view, c, y=52, h=8, w=48, z='f', ln=True, dip=4):
    """Cinta alrededor de la cabeza a la altura y (de frente baja un poco por los lados)."""
    if view == 'front':
        top = quad((50 - w, y + dip), (50, y - dip), (50 + w, y + dip))
        bot = quad((50 + w, y + dip + h), (50, y - dip + h), (50 - w, y + dip + h))
        return L(top + bot, c, z, True, ln)
    if view == 'side':
        return L([(2, y + 10), (94, y - 4), (94, y - 4 + h), (2, y + 10 + h)], c, z, True, ln)
    top = quad((50 - w, y + dip), (50, y + dip + 2), (50 + w, y + dip))
    bot = quad((50 + w, y + dip + h), (50, y + dip + h + 2), (50 - w, y + dip + h))
    return L(top + bot, c, z, True, ln)


def bush(view, c='mid', top=0, w=46, cy=46, n=10, amp=6, seed=1, sb=64, nape=86, fr=48, **k):
    """Pelo rizado o abultado en bultos redondos (dome con pinchos suaves)."""
    return dome(view, top=top, w=w, cy=cy, n=n, amp=amp, soft=True, seed=seed, sb=sb, nape=nape, fr=fr, c=c, **k)


def specs_dot(view, y, c=BLACK):
    """Dos puntitos (marcas bajo los ojos)."""
    if view == 'front':
        return [L(ell(x, y, 1.0, 1.0), c, 'f', False) for x in (32, 68)]
    return [L(ell(80, y, 1.0, 1.0), c, 'f', False)]


# ------------------------------------------------------------------ jugadores

# Snowy Bergman: pinchos rubios enormes echados hacia arriba y a un lado como llamas, unas gafas de nieve grises con una
# cruz roja en cada cristal sobre la frente; piel morena, ojos negros afilados con marcas amarillas debajo y ceño
GRY, RED = _c('#a8b0b0'), _c('#d8402a')
def _snow_goggles(view):
    if view == 'front':
        out = [band('front', _c('#7a4a2a'), 46, 6)]
        for cx in (32, 68):
            out += [L(ell(cx, 50, 11, 8), GRY, 'f', True, True), L(ell(cx, 50, 7, 5), _c('#c8602a'), 'f', False),
                    L([(cx - 4, 50), (cx + 4, 50)], RED, 'f', False, False, 2.4), L([(cx, 46.5), (cx, 53.5)], RED, 'f', False, False, 2.4)]
        return out
    if view == 'side':
        return [band('side', _c('#7a4a2a'), 44, 6), L(ell(84, 46, 8, 7), GRY, 'f', True, True), L(ell(85, 46, 4, 4), _c('#c8602a'), 'f', False)]
    return [band('back', _c('#7a4a2a'), 44, 6)]
C('snowy-bergman', 'normal', P('#f2d860', '#c88c4e', iris='#1e1a1a', shade='#d8b040', deep='#a88a2a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=hl(5, 66, 52, 60, lean=2, jit=2, seed=3)),
  dome('front', top=-14, w=44, cy=44, n=6, amp=24, sweep=0.5, seed=11, sb=66) + _snow_goggles('front') +
  [mark([(26, 84), (36, 86)], _c('#e8c040'), w=1.4), mark([(64, 86), (74, 84)], _c('#e8c040'), w=1.4)],
  dome('side', top=-14, w=44, cy=44, n=6, amp=24, sweep=0.5, seed=11, nape=84, fr=46) + _snow_goggles('side'),
  dome('back', top=-14, w=44, cy=44, n=6, amp=24, sweep=0.5, seed=11, nape=84) + _snow_goggles('back'))

# Sonny Monkey Wukong: rey mono: pelo castaño rojizo de punta hacia arriba, orejas de mono enormes y redondas, la diadema
# dorada con el remolino en la frente, mechones castaños en las mejillas y una perilla en punta; ojos de párpado caído
GOLD = _c('#e8c040')
def _circlet(view):
    if view == 'front':
        return [band('front', GOLD, 52, 5, dip=3), L(outline([(44, 54), (50, 50), (56, 54), (54, 60), (46, 60)]), GOLD, 'f', True, True)]
    if view == 'side':
        return [band('side', GOLD, 50, 5)]
    return [band('back', GOLD, 50, 5)]
C('sonny-monkey-wukong', 'normal', P('#8a3a10', '#f2bc72', iris='#1e1a1a', shade='#6a2a0c', deep='#4a1e08'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=95, big_ears=6, ear_out=4, nose=(50, 86, 3),
    hairline=[(6, 62), (20, 52), (34, 48), (50, 50), (66, 48), (80, 52), (94, 62)]),
  dome('front', top=-8, w=42, cy=44, n=7, amp=14, seed=12, sb=56) + _circlet('front') +
  [mark([(18, 88), (24, 84), (26, 94)], 'deep'), mark([(82, 88), (76, 84), (74, 94)], 'deep'),
   L(outline([(46, 102), (50, 98), (54, 102), (50, 112, 1)]), 'deep', 'f')],
  dome('side', top=-8, w=42, cy=44, n=7, amp=14, seed=12, nape=78, fr=48) + _circlet('side') + [mark([(76, 88), (82, 84), (82, 94)], 'deep')],
  dome('back', top=-8, w=42, cy=44, n=7, amp=14, seed=12, nape=78) + _circlet('back'))

# Springer Boreham: casco de aviador verde oliva con orejeras que le bajan hasta la barbilla, unas gafas de aviador
# marrones encima y la visera naranja; flequillo negro en puntas; ojos grandes y sonrisa
OLV, VIS, GOG = _c('#625a32'), _c('#d8703a'), _c('#5a3a1e')
def _aviator(view):
    if view == 'front':
        return [cap('front', OLV, top=-2, rim=58, w=48),
                L(outline([(4, 58), (16, 58), (18, 96), (8, 100), (2, 90)]), OLV, 'f', True, True),
                L(outline([(96, 58), (84, 58), (82, 96), (92, 100), (98, 90)]), OLV, 'f', True, True),
                L(outline([(14, 56), (50, 48), (86, 56), (82, 64), (50, 58), (18, 64)]), VIS, 'f', True, True),
                L(ell(33, 32, 11, 9), GOG, 'f', True, True), L(ell(67, 32, 11, 9), GOG, 'f', True, True),
                L(ell(33, 32, 7, 5.5), _c('#3a3a32'), 'f', False), L(ell(67, 32, 7, 5.5), _c('#3a3a32'), 'f', False),
                L(outline([(30, 44), (50, 40), (70, 44), (68, 48), (50, 46), (32, 48)]), _c('#f0e8d0'), 'f', False)]
    if view == 'side':
        return [cap('side', OLV, top=-2, rim=58, w=48, drop=26), L(outline([(36, 58), (58, 58), (60, 96), (48, 100), (36, 92)]), OLV, 'f', True, True),
                L(outline([(60, 56), (100, 50), (100, 58), (62, 64)]), VIS, 'f', True, True), L(ell(72, 30, 9, 9), GOG, 'f', True, True),
                L(ell(74, 30, 5, 5), _c('#3a3a32'), 'f', False)]
    return [cap('back', OLV, top=-2, rim=70, w=48, drop=14),
            L(outline([(2, 60), (16, 58), (18, 98), (6, 98)]), OLV, 'f', True, True), L(outline([(98, 60), (84, 58), (82, 98), (94, 98)]), OLV, 'f', True, True),
            band('back', GOG, 36, 5)]
C('springer-boreham', 'normal', P('#201c18', '#f4c08a', iris='#1e1a1a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=hl(6, 68, 58, 66, jit=2, seed=4), ears=False, eye_y=77),
  _aviator('front') + [L(outline([(20, 60), (26, 74, 1), (32, 62), (40, 72, 1), (46, 62), (54, 74, 1), (58, 62), (66, 72, 1), (70, 62), (78, 74, 1), (80, 60)]), 'mid', 'f')],
  dome('side', top=10, w=44, cy=50, nape=80, fr=60, shade=False) + _aviator('side'),
  _aviator('back'))

# Stackem Skyhigh: pelo naranja en pinchos que suben hasta una punta alta en el centro, una cinta blanca en la frente con
# un rombo rojo y un rayo amarillo; ojos grandes rojizos y sonrisa
OR1, WHB = _c('#c84018'), _c('#f0ece4')
def _stack_band(view):
    if view == 'front':
        return [band('front', WHB, 50, 8), L(outline([(50, 44), (60, 54), (50, 64), (40, 54)]), RED, 'f', True, True),
                L([(52, 48), (47, 55), (53, 55), (48, 61)], GOLD, 'f', False, False, 1.6)]
    if view == 'side':
        return [band('side', WHB, 48, 8), L(outline([(6, 60), (-4, 66, 1), (4, 72), (-2, 80, 1), (10, 70)]), WHB, 'f', True, True)]
    return [band('back', WHB, 48, 8), L(outline([(44, 58), (36, 76, 1), (48, 64), (56, 64), (62, 78, 1), (54, 58)]), WHB, 'f', True, True)]
C('stackem-skyhigh', 'normal', P('#e85818', '#f6c48e', iris='#b03a18', shade='#c03e12', deep='#8a2a10'),
  F(eyes='big', brows='angry', mouth='smile', mouth_y=93, hairline=hl(6, 72, 56, 66, jit=3, seed=5)),
  dome('front', top=-16, w=46, cy=46, n=7, amp=18, seed=14, sb=74, flare=10) + _stack_band('front'),
  dome('side', top=-16, w=46, cy=46, n=7, amp=18, seed=14, nape=88, fr=52) + _stack_band('side'),
  dome('back', top=-16, w=46, cy=46, n=7, amp=18, seed=14, nape=88) + _stack_band('back'))

# Stan Statto Tistischen: gorra negra con el frente crema y la visera hacia delante, unos cascos enormes negros con luz
# turquesa y un visor gris con una raya turquesa que le tapa los ojos; mechones salmón por debajo; sonrisa
BK2, CRM, CYN, VGR = _c('#1e2a2a'), _c('#f2ead4'), _c('#40d8e8'), _c('#7a7e78')
def _stan(view):
    if view == 'front':
        return [cap('front', BK2, top=-4, rim=52, w=48), L(outline([(26, 50), (24, 18), (40, 4), (60, 4), (76, 18), (74, 50)]), CRM, 'b', False),
                L(outline([(10, 54), (50, 46), (90, 54), (88, 62), (50, 56), (12, 62)]), BK2, 'f', True, True),
                L(outline([(2, 58), (14, 54), (16, 90), (2, 90)]), BK2, 'f', True, True), L(outline([(98, 58), (86, 54), (84, 90), (98, 90)]), BK2, 'f', True, True),
                L([(6, 64), (6, 84)], CYN, 'f', False, False, 1.8), L([(94, 64), (94, 84)], CYN, 'f', False, False, 1.8),
                L(outline([(16, 68), (50, 64), (84, 68), (84, 82), (50, 80), (16, 82)]), VGR, 'f', True, True),
                L([(22, 74), (78, 74)], CYN, 'f', False, False, 1.6)]
    if view == 'side':
        return [cap('side', BK2, top=-4, rim=52, w=48, drop=16), L(outline([(64, 50), (106, 52), (104, 60), (64, 58)]), BK2, 'f', True, True),
                L(ell(46, 72, 11, 13), BK2, 'f', True, True), L(ell(46, 72, 5, 7), CYN, 'f', False),
                L(outline([(56, 66), (92, 64), (92, 80), (56, 80)]), VGR, 'f', True, True), L([(60, 72), (90, 71)], CYN, 'f', False, False, 1.6)]
    return [cap('back', BK2, top=-4, rim=60, w=48, drop=10), L(outline([(2, 60), (14, 56), (16, 90), (2, 90)]), BK2, 'f', True, True),
            L(outline([(98, 60), (86, 56), (84, 90), (98, 90)]), BK2, 'f', True, True), band('back', VGR, 66, 6)]
C('stan-statto-tistischen', 'normal', P('#f08a6a', '#f2b27e', shade='#d06a50'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=92, hairline=False, ears=False),
  [L(outline([(30, 60), (40, 84, 1), (46, 64), (56, 90, 1), (60, 64), (72, 86, 1), (74, 60)]), 'mid', 'f')] + _stan('front'),
  [L(outline([(60, 56), (66, 84, 1), (76, 62), (84, 80, 1), (88, 58)]), 'mid', 'f')] + _stan('side'),
  [L(outline([(12, 70), (24, 92, 1), (40, 78), (50, 94, 1), (60, 78), (76, 92, 1), (88, 70)]), 'mid')] + _stan('back'))

# Stanza Verse: pelo castaño oscuro rizado en mechones de punta por los lados y arriba, con una cinta ancha crema que le
# tapa media cabeza; piel morena, ojos grandes, aros blancos en las orejas y sonrisa
CR2 = _c('#f8f0d0')
C('stanza-verse', 'chica', P('#3a1a0a', '#c8925e', iris='#2a1a12'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=[(6, 64), (18, 56), (32, 54), (50, 52), (68, 54), (82, 56), (94, 64)]),
  dome('front', top=0, w=48, cy=46, n=10, amp=8, seed=15, sb=74) + [band('front', CR2, 28, 22, w=44, dip=8)] +
  [L(ell(14, 92, 3, 4), CR2, 'f', True, True), L(ell(86, 92, 3, 4), CR2, 'f', True, True)],
  dome('side', top=0, w=48, cy=46, n=10, amp=8, seed=15, nape=86, fr=54) + [L(outline([(28, 20), (86, 30), (88, 50), (30, 36)]), CR2, 'f', True, True),
                                                                          L(ell(48, 86, 3, 4), CR2, 'f', True, True)],
  dome('back', top=0, w=48, cy=46, n=10, amp=8, seed=15, nape=86) + [band('back', CR2, 22, 18, w=44, dip=6)])

# Steven Nevets: melena gris beige ondulada con raya en medio que le cae hasta el cuello; piel clara, ojos grises
# entornados, un punto en la frente y media sonrisa
C('steven-nevets', 'normal', P('#b49c8a', '#fae2b8', iris='#7a8088', shade='#8a7064', deep='#6a5248'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=93, face_front=face(chin=104), face_side=face_side(chin=4),
    hairline=[(6, 70), (16, 52), (30, 42), (50, 38), (70, 42), (84, 52), (94, 70)], nose=(50, 86, 2.6)),
  dome('front', top=2, w=47, cy=46, long=104, flare=4) + [strand([(50, 4), (48, 26)], 'deep', 'b', 1.2), L(ell(50, 60, 1.2, 1.2), BLACK, 'f', False),
                                                          strand([(10, 70), (6, 86), (10, 100)], 'deep', 'b', 1.0), strand([(90, 70), (94, 86), (90, 100)], 'deep', 'b', 1.0)],
  dome('side', top=2, w=47, cy=46, long=102, flare=4, fr=46),
  dome('back', top=2, w=47, cy=46, long=102, flare=4, ends=5) + [strand([(50, 6), (50, 60)], 'deep', 'b', 1.2)])

# Strama Dakoto: media melena verde grisácea con un flequillo grande echado a un lado y una coleta alta envuelta en vendas
# blancas que sale disparada hacia arriba, con las tiras colgando; sombra gris en los ojos y sonrisa dulce
VND = _c('#ece6d8')
C('strama-dakoto', 'chica', P('#6a6a5c', '#f6c48e', iris='#4a4038', shade='#4e4e44'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=93, hairline=[(6, 70), (14, 60), (24, 66), (40, 58), (60, 50), (80, 46), (94, 60)]),
  [L(outline([(62, 14), (96, -14), (104, -6), (74, 26)]), VND, 'b', True, True), L(outline([(98, -10), (100, 40), (104, 40), (104, -6)]), VND, 'b', True, True),
   L([(96, -12), (92, 36)], VND, 'b', False, False, 2.4)] +
  dome('front', top=2, w=47, cy=46, sb=78) + [L(outline([(6, 76), (4, 56), (20, 36), (50, 30), (80, 36), (94, 50), (90, 56), (60, 50), (36, 58), (20, 66), (10, 84, 1)]), 'mid', 'f')] +
  [mark([(26, 70), (38, 70), (38, 73), (26, 73)], _c('#b8b0a0')), mark([(62, 70), (74, 70), (74, 73), (62, 73)], _c('#b8b0a0'))],
  dome('side', top=2, w=47, cy=46, nape=86, fr=60) + [L(outline([(14, 18), (-16, -12), (-22, -4), (2, 26)]), VND, 'f', True, True),
                                                      L(outline([(-18, -8), (-20, 40), (-14, 40), (-14, -4)]), VND, 'f', True, True)],
  dome('back', top=2, w=47, cy=46, nape=86) + [L(outline([(56, 10), (80, -16), (88, -8), (64, 20)]), VND, 'f', True, True),
                                               L(outline([(82, -12), (84, 36), (90, 36), (88, -8)]), VND, 'f', True, True)])

# Stu Stewpot Potter: cabeza casi rapada con una cinta ancha azul marino con un óvalo rojo a rayas en la frente; piel
# morena, una cicatriz en la frente, ojos blancos de ceño fruncido y labios gruesos naranjas
NAV = _c('#2c2840')
def _stu(view):
    if view == 'front':
        return [band('front', NAV, 36, 18, w=48, dip=6), L(ell(50, 44, 6, 5), _c('#c8302a'), 'f', True, True),
                L([(45, 44), (55, 44)], NAV, 'f', False, False, 1.2), L([(46, 41.5), (54, 41.5)], NAV, 'f', False, False, 1.0)]
    if view == 'side':
        return [band('side', NAV, 34, 18)]
    return [band('back', NAV, 32, 18, dip=6)]
C('stu-stewpot-potter', 'normal', P('#90603a', '#a8683a', iris='#1e1a1a'),
  F(eyes='round', brows='angry', mouth='lips', mouth_y=94, mouth_w=10, hairline=False, nose=(50, 86, 3)),
  [cap('front', 'mid', top=8, rim=46, w=44, z='b')] + _stu('front') + [mark([(56, 62), (60, 54)], _c('#6a3a1e'), w=1.2)],
  [cap('side', 'mid', top=8, rim=46, w=44, drop=10)] + _stu('side'),
  [cap('back', 'mid', top=8, rim=50, w=44, drop=6)] + _stu('back'))

# Sue Chirpy Accharin: sombrero de copa a cuadros rojos y blancos con una franja azul marino; melena rubia ondulada hasta
# los hombros con las puntas hacia fuera; ojos azules grandes, pecas y sonrisa
RDH, NV2 = _c('#b81818'), _c('#2e3a5e')
def _tophat(view):
    if view == 'front':
        return [L(outline([(10, 44), (12, -20), (88, -20), (90, 44)]), RDH, 'f', True, True),
                L([(30, -18), (28, 42)], WHITE, 'f', False, False, 5), L([(70, -18), (72, 42)], WHITE, 'f', False, False, 5),
                L([(50, -18), (50, 42)], WHITE, 'f', False, False, 5), L([(12, -8), (88, -8)], WHITE, 'f', False, False, 5),
                L([(12, 12), (88, 12)], WHITE, 'f', False, False, 5), L(outline([(10, 22), (90, 22), (90, 34), (10, 34)]), NV2, 'f', True, True),
                L(outline([(2, 44), (50, 38), (98, 44), (96, 54), (50, 48), (4, 54)]), RDH, 'f', True, True)]
    if view == 'side':
        return [L(outline([(6, 44), (10, -20), (84, -20), (88, 40)]), RDH, 'f', True, True), L([(46, -18), (46, 40)], WHITE, 'f', False, False, 5),
                L([(10, 2), (86, 2)], WHITE, 'f', False, False, 5), L(outline([(8, 22), (88, 20), (88, 32), (8, 34)]), NV2, 'f', True, True),
                L(outline([(-4, 48), (50, 40), (100, 40), (98, 50), (50, 50), (-2, 58)]), RDH, 'f', True, True)]
    return [L(outline([(10, 44), (12, -20), (88, -20), (90, 44)]), RDH, 'f', True, True), L([(50, -18), (50, 42)], WHITE, 'f', False, False, 5),
            L([(12, 2), (88, 2)], WHITE, 'f', False, False, 5), L(outline([(10, 22), (90, 22), (90, 34), (10, 34)]), NV2, 'f', True, True),
            L(outline([(2, 44), (50, 40), (98, 44), (96, 54), (50, 50), (4, 54)]), RDH, 'f', True, True)]
C('sue-chirpy-accharin', 'chica', P('#d8b068', '#f6dcb8', iris='#2a5ab0', shade='#b08a48'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=[(6, 70), (18, 58), (30, 56), (50, 60), (70, 56), (82, 58), (94, 70)]),
  bush('front', top=30, w=48, cy=58, n=6, amp=6, seed=21, long=104, flare=12) + _tophat('front') +
  [L(ell(x, y, 0.8, 0.8), _c('#b07848'), 'f', False) for x, y in ((26, 86), (30, 88), (33, 85), (74, 86), (70, 88), (67, 85))],
  bush('side', top=30, w=48, cy=58, n=6, amp=6, seed=21, long=102, flare=10, fr=62) + _tophat('side'),
  bush('back', top=30, w=48, cy=58, n=6, amp=6, seed=21, long=102, flare=12, ends=5) + _tophat('back'))

# Sunil Ra Rahman (portero): melena lisa negra verdosa que le cae hasta el pecho, con raya en medio, y una corona de
# laurel; piel morena, un punto en la frente, ojos naranjas de ceño fruncido y boca apretada
LAU = _c('#4a9a3a')
def _laurel(view):
    if view == 'front':
        return [L(ell(50 + t * 34, 22 + abs(t) * 12, 6, 3.6), LAU, 'f', True, True) for t in (-1, -0.66, -0.33, 0.33, 0.66, 1)]
    if view == 'side':
        return [L(ell(x, y, 5, 3.2), LAU, 'f', True, True) for x, y in ((80, 30), (66, 22), (52, 18), (38, 20), (24, 26))]
    return [L(ell(50 + t * 38, 24 + abs(t) * 8, 6, 3.6), LAU, 'f', True, True) for t in (-1, -0.66, -0.33, 0, 0.33, 0.66, 1)]
C('sunil-ra-rahman', 'normal', P('#3a4846', '#b8865a', iris='#d86a1e', shade='#2a3432', deep='#1e2624'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, face_front=face(chin=104), face_side=face_side(chin=4),
    hairline=[(6, 76), (18, 54), (32, 44), (50, 40), (68, 44), (82, 54), (94, 76)], nose=(50, 86, 2.6)),
  dome('front', top=2, w=48, cy=46, long=118, flare=6) + _laurel('front') + [strand([(50, 4), (50, 36)], 'deep', 'b', 1.2), L(ell(50, 58, 1.4, 1.4), BLACK, 'f', False)],
  dome('side', top=2, w=48, cy=46, long=116, flare=4, fr=50) + _laurel('side'),
  dome('back', top=2, w=48, cy=46, long=116, flare=6, ends=6) + _laurel('back') + [strand([(50, 6), (50, 110)], 'deep', 'b', 1.2)])

# Sunniffa Scentgood: pelo granate recogido en un moño alto con una flor rosa encima y un mechón grueso en forma de gota
# que le baja por la frente; orejas a la vista, ojos negros grandes de ceño fruncido y boca pequeña
FLW = _c('#e07888')
C('sunniffa-scentgood', 'chica', P('#7a2638', '#f8cc8c', iris='#1e1a1a', shade='#5a1c28'),
  F(eyes='big', brows='angry', mouth='frown', mouth_y=93, hairline=[(6, 58), (20, 48), (36, 44), (50, 46), (64, 44), (80, 48), (94, 58)]),
  [L(ell(50, -2, 13, 11)), L(outline([(32, -10), (50, -20), (68, -10), (72, -4), (50, -8), (28, -4)]), FLW, 'f', True, True)] +
  dome('front', top=6, w=45, cy=46, sb=58) + [L(outline([(46, 40), (50, 30), (58, 36), (54, 60, 1)]), 'mid', 'f'), L(outline([(48, 40), (51, 34), (54, 40), (52, 52)]), FLW, 'f', False)],
  [L(ell(42, -2, 13, 11)), L(outline([(26, -10), (42, -20), (58, -10), (60, -4), (42, -8), (22, -4)]), FLW, 'f', True, True)] +
  dome('side', top=6, w=45, cy=46, nape=80, fr=46),
  [L(ell(50, -2, 13, 11)), L(outline([(32, -10), (50, -20), (68, -10), (72, -4), (50, -8), (28, -4)]), FLW, 'f', True, True)] +
  dome('back', top=6, w=45, cy=46, nape=80) + [strand([(50, 4), (50, 70)], 'deep', 'b', 1.0)])

# Susan Taylor (portera): pelo castaño oliva con flequillo de mechones, una diadema turquesa con un botón grande y dos
# coletas bajas sujetas con botones; ojos verdes grandes y sonrisa abierta
TQ, BTN, BT2 = _c('#5ac0b0'), _c('#f2e8c8'), _c('#e07a2a')
def _pig(x, y):
    return [L(ell(x, y + 14, 10, 13)), L(ell(x, y, 5, 5), BT2, 'f', True, True)]
C('susan-taylor', 'chica', P('#6a5c30', '#f6c48e', iris='#3a9a7a', shade='#4e4226'),
  F(eyes='big', brows=True, mouth='grin', mouth_y=93, hairline=hl(5, 72, 54, 66, lean=-2, jit=3, seed=22)),
  dome('front', top=4, w=46, cy=46, sb=78) + [band('front', TQ, 34, 6, w=44), L(ell(70, 34, 7, 7), BTN, 'f', True, True)] + _pig(12, 88) + _pig(88, 88),
  dome('side', top=4, w=46, cy=46, nape=84, fr=56) + [band('side', TQ, 30, 6)] + _pig(26, 88),
  dome('back', top=4, w=46, cy=46, nape=84) + [band('back', TQ, 30, 6)] + _pig(14, 88) + _pig(86, 88))

# T T Mann: pelo rubio arena en cresta de pinchos peinada hacia arriba y atrás, con los lados cortos y dos rayas oscuras
# afeitadas; ojos marrones afilados de ceño fruncido y media sonrisa
C('t-t-mann', 'normal', P('#c09050', '#f6c48e', iris='#8a4a20', shade='#8a5c30', deep='#4c2c0a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=[(6, 64), (18, 54), (32, 48), (44, 58), (52, 46), (60, 56), (68, 48), (82, 54), (94, 64)]),
  [cap('front', 'shade', top=22, rim=56, w=39)] + dome('front', top=-14, w=26, cy=40, n=5, amp=16, seed=23, sb=50) +
  [strand([(14, 50), (22, 30)], 'deep', 'b', 1.6), strand([(18, 54), (26, 34)], 'deep', 'b', 1.6), strand([(86, 50), (78, 30)], 'deep', 'b', 1.6),
   strand([(82, 54), (74, 34)], 'deep', 'b', 1.6)],
  [cap('side', 'shade', top=20, rim=60, w=46, drop=20)] + dome('side', top=-14, w=36, cy=36, n=5, amp=16, sweep=-0.5, seed=23, nape=60, fr=44, shade=False) +
  [strand([(20, 52), (46, 30)], 'deep', 'b', 1.6), strand([(24, 58), (50, 36)], 'deep', 'b', 1.6)],
  [cap('back', 'shade', top=22, rim=62, w=42, drop=10)] + dome('back', top=-14, w=26, cy=40, n=5, amp=16, seed=23, nape=50, shade=False))

# Theron Shuriken Starr: ninja con un gorro negro, una cinta blanca con la placa de metal gris cuyas tiras ondean detrás,
# un antifaz negro en los ojos, perilla negra y una cicatriz en la mejilla; boca de enfado
NJ, PLT, BDG = _c('#2e2c2a'), _c('#6a6a68'), _c('#e8dcc4')
def _ninja(view):
    if view == 'front':
        return [cap('front', NJ, top=-6, rim=50, w=46, z='f', ln=True), band('front', BDG, 48, 9, w=50),
                L(outline([(30, 46), (70, 46), (68, 58), (32, 58)]), PLT, 'f', True, True),
                L(outline([(84, 54), (108, 46, 1), (100, 60), (110, 80, 1), (92, 62)]), BDG, 'f', True, True)]
    if view == 'side':
        return [cap('side', NJ, top=-6, rim=50, w=46, drop=12, z='f', ln=True), band('side', BDG, 46, 9),
                L(outline([(80, 44), (96, 42), (96, 54), (80, 56)]), PLT, 'f', True, True),
                L(outline([(4, 58), (-22, 54, 1), (-8, 66), (-24, 84, 1), (0, 70)]), BDG, 'f', True, True)]
    return [cap('back', NJ, top=-6, rim=58, w=46, drop=8, z='f', ln=True), band('back', BDG, 46, 9),
            L(outline([(44, 56), (30, 84, 1), (48, 66), (56, 66), (74, 86, 1), (58, 56)]), BDG, 'f', True, True)]
C('theron-shuriken-starr', 'normal', P('#1e1c1a', '#f2c8a0', iris='#1e1a1a'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=94, hairline=False, nose=(50, 86, 2.6)),
  _ninja('front') + [L(outline([(16, 70), (50, 66), (84, 70), (84, 80), (50, 76), (16, 80)]), BLACK, 'f', False),
                     L(ell(36, 74, 4.4, 3.6), WHITE, 'f', False), L(ell(64, 74, 4.4, 3.6), WHITE, 'f', False),
                     L(ell(36, 74, 2.2, 2.4), BLACK, 'f', False), L(ell(64, 74, 2.2, 2.4), BLACK, 'f', False),
                     L(outline([(40, 100), (50, 98), (60, 100), (54, 108), (46, 108)]), BLACK, 'f', False),
                     mark([(22, 86), (30, 92)], _c('#8a5a40'), w=1.2)],
  _ninja('side') + [L(outline([(66, 70), (92, 68), (92, 78), (66, 80)]), BLACK, 'f', False), L(outline([(76, 98), (86, 98), (82, 106)]), BLACK, 'f', False)],
  _ninja('back'))

# Thomas Tomahawk Oquendo: máscara tribal de madera clara con la nariz larga, los ojos cerrados y labios gruesos, un casco
# naranja a franjas y una melena de rastas castaño oscuro que cae a los lados
MSK, HLM, HL2 = _c('#f4e2b4'), _c('#b05a1e'), _c('#d88a3a')
def _tomahawk(view):
    if view == 'front':
        return [L(outline([(16, 60), (14, 30), (30, 12), (50, 8), (70, 12), (86, 30), (84, 60)]), HLM, 'f', True, True),
                L(outline([(24, 52), (26, 30), (40, 18), (60, 18), (74, 30), (76, 52), (50, 40)]), HL2, 'f', False),
                L(outline([(34, 48), (36, 34), (50, 26), (64, 34), (66, 48), (50, 40)]), HLM, 'f', False)]
    if view == 'side':
        return [L(outline([(10, 62), (8, 30), (26, 12), (52, 6), (76, 14), (90, 34), (92, 58)]), HLM, 'f', True, True),
                L(outline([(30, 50), (40, 22), (64, 18), (82, 34), (84, 52)]), HL2, 'f', False)]
    return [L(outline([(14, 62), (14, 30), (30, 12), (50, 8), (70, 12), (86, 30), (86, 62)]), HLM, 'f', True, True),
            L(outline([(26, 54), (30, 28), (50, 18), (70, 28), (74, 54)]), HL2, 'f', False)]
def _dreads(view):
    xs = (2, 10, 18, 82, 90, 98) if view == 'front' else ((0, 8, 16, 24, 32, 40) if view == 'side' else (4, 16, 28, 40, 52, 64, 76, 88, 96))
    return [L(outline([(x - 4, 30), (x + 4, 30), (x + 3, 104), (x - 3, 104)])) for x in xs]
C('thomas-tomahawk-oquendo', 'corpulento', P('#4a2c14', '#f4e2b4', iris='#1e1a1a', shade='#30200e'),
  F(eyes='closed', brows=False, mouth='lips', mouth_y=98, mouth_w=12, hairline=False, ears=False, nose=(50, 84, 5),
    face_front=face(w=2, chin=106, jaw=2)),
  _dreads('front') + [dome('front', top=-4, w=50, cy=44, n=9, amp=10, seed=24, sb=60)[0]] + _tomahawk('front') +
  [L(outline([(46, 64), (54, 64), (58, 88), (42, 88)]), _c('#e8cc96'), 'f', True, True)],
  _dreads('side') + [dome('side', top=-4, w=50, cy=44, n=9, amp=10, seed=24, nape=96, fr=60)[0]] + _tomahawk('side') +
  [L(outline([(84, 66), (96, 82), (86, 88)]), _c('#e8cc96'), 'f', True, True)],
  _dreads('back') + [dome('back', top=-4, w=50, cy=44, n=9, amp=10, seed=24, long=104, flare=4, ends=6)[0]] + _tomahawk('back'))

# Tia T Quoise Cruz: capucha de tela verde grisácea muy clara que le envuelve la cabeza, un pañuelo rojo de rombos encima
# y dos borlas rojas trenzadas que le caen por delante; ojos negros grandes, una tirita en la nariz y boca de enfado
HD, RD1, RD2 = _c('#cfdccb'), _c('#c8604a'), _c('#8a2412')
def _tia(view):
    if view == 'front':
        return [L(outline([(4, 100), (2, 50), (14, 18), (50, 2), (86, 18), (98, 50), (96, 100), (84, 96), (84, 60), (16, 60), (16, 96)]), HD, 'b'),
                L(outline([(14, 46), (16, 20), (50, 6), (84, 20), (86, 46), (50, 40)]), RD1, 'f', True, True),
                L([(30, 14), (50, 40), (70, 14)], RD2, 'f', False, False, 1.6), L([(16, 30), (34, 44)], RD2, 'f', False, False, 1.6),
                L([(84, 30), (66, 44)], RD2, 'f', False, False, 1.6),
                L(outline([(18, 86), (26, 86), (28, 116), (16, 116)]), RD1, 'f', True, True), L(outline([(74, 86), (82, 86), (84, 116), (72, 116)]), RD1, 'f', True, True)]
    if view == 'side':
        return [L(outline([(60, 100), (52, 62), (66, 56), (90, 50), (92, 26), (70, 6), (40, 2), (12, 16), (0, 50), (2, 96), (24, 104)]), HD, 'f', True, True),
                L(outline([(10, 40), (14, 18), (44, 4), (74, 10), (90, 30), (88, 46), (50, 40)]), RD1, 'f', True, True),
                L(outline([(70, 86), (78, 86), (80, 116), (68, 116)]), RD1, 'f', True, True)]
    return [L(outline([(4, 104), (2, 50), (14, 18), (50, 2), (86, 18), (98, 50), (96, 104), (50, 110)]), HD, 'f', True, True),
            L(outline([(14, 50), (16, 20), (50, 6), (84, 20), (86, 50), (50, 56)]), RD1, 'f', True, True),
            L([(30, 14), (50, 54), (70, 14)], RD2, 'f', False, False, 1.6)]
C('tia-t-quoise-cruz', 'chica', P('#cfdccb', '#f6c48e', iris='#1e1a1a'),
  F(eyes='big', brows='angry', mouth='frown', mouth_y=95, hairline=False, ears=False),
  _tia('front') + [L(outline([(42, 84), (58, 84), (58, 90), (42, 90)]), _c('#d88a6a'), 'f', True, True)],
  _tia('side'), _tia('back'))

# Tiger Bleriot (portero): gorra marrón rojiza con una llama dorada dibujada y el borde crema, pelo castaño oscuro en
# mechones de punta por debajo y abiertos a los lados; piel tostada, ojos afilados y media sonrisa
BRC, FLM = _c('#a04a1e'), _c('#e8b040')
def _tiger(view):
    if view == 'front':
        return [cap('front', BRC, top=-2, rim=52, w=46, z='f', ln=True), L(outline([(40, 20), (56, 8), (52, 22), (66, 18), (54, 34), (40, 36)]), FLM, 'f', False),
                L(outline([(10, 54), (50, 44), (90, 54), (88, 62), (50, 54), (12, 62)]), CRM, 'f', True, True)]
    if view == 'side':
        return [cap('side', BRC, top=-2, rim=52, w=46, drop=14, z='f', ln=True), L(outline([(56, 48), (100, 46), (98, 54), (58, 56)]), CRM, 'f', True, True)]
    return [cap('back', BRC, top=-2, rim=56, w=46, drop=8, z='f', ln=True)]
C('tiger-bleriot', 'normal', P('#4a2008', '#d8a05a', iris='#1e1a1a', shade='#30160a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=hl(6, 70, 54, 68, lean=2, jit=3, seed=31)),
  dome('front', top=10, w=48, cy=50, n=7, amp=10, seed=32, sb=84, flare=12, long=90) + _tiger('front'),
  dome('side', top=10, w=48, cy=50, n=7, amp=10, seed=32, nape=90, fr=60) + _tiger('side'),
  dome('back', top=10, w=48, cy=50, n=7, amp=10, seed=32, nape=90) + _tiger('back'))

# Tim Minstrel Roubadour: pelo rosa malva abultado y ondulado con raya en medio que le llega a la mandíbula, una bufanda
# crema anudada al cuello; ojos rojos afilados de ceño fruncido y boca apretada
SCF = _c('#f4ecd0')
C('tim-minstrel-roubadour', 'normal', P('#b48a80', '#fcd0a0', iris='#b01e1e', shade='#8a6058', deep='#68443e'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 76), (16, 54), (30, 44), (48, 40), (52, 40), (70, 44), (84, 54), (94, 76)]),
  bush('front', top=0, w=52, cy=46, n=8, amp=6, seed=33, long=96, flare=8) + [strand([(50, 4), (50, 36)], 'deep', 'b', 1.2),
   L(outline([(28, 104), (50, 98), (72, 104), (66, 116), (56, 112), (54, 126, 1), (46, 126, 1), (44, 112), (34, 116)]), SCF, 'f', True, True)],
  bush('side', top=0, w=52, cy=46, n=8, amp=6, seed=33, long=94, flare=6, fr=50) + [L(outline([(44, 98), (86, 102), (82, 116), (62, 120), (66, 132, 1), (56, 120), (46, 112)]), SCF, 'f', True, True)],
  bush('back', top=0, w=52, cy=46, n=8, amp=6, seed=33, long=94, flare=8, ends=5) + [L(outline([(28, 100), (72, 100), (70, 110), (30, 110)]), SCF, 'f', True, True)])

# Tiny Jetson: pelo rojo en pinchos grandes alborotados, gafas de sol negras anchas en punta; piel morena, cara ancha y
# dientes apretados
SUN = _c('#2a323a')
C('tiny-jetson', 'corpulento', P('#b80a1e', '#b07440', iris='#1e1a1a', shade='#8a0a18', deep='#5c1414'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=96, face_front=face(w=4, chin=104, jaw=4), face_side=face_side(chin=4, jaw=4),
    hairline=hl(6, 64, 50, 58, jit=3, seed=34), nose=(50, 88, 3)),
  dome('front', top=-12, w=52, cy=44, n=9, amp=14, seed=35, sb=70) +
  [L(outline([(12, 70), (30, 64), (46, 70), (54, 70), (70, 64), (88, 70), (84, 82), (60, 82), (50, 76), (40, 82), (16, 82)]), SUN, 'f', True, True)],
  dome('side', top=-12, w=52, cy=44, n=9, amp=14, seed=35, nape=86, fr=52) + [L(outline([(54, 68), (94, 66), (92, 80), (60, 80)]), SUN, 'f', True, True)],
  dome('back', top=-12, w=52, cy=44, n=9, amp=14, seed=35, nape=86) + [band('back', SUN, 68, 3)])

# Titania Wraps Khamun: momia: vendas crema que le envuelven la cabeza y media cara dejando un solo ojo rojo a la vista,
# y una melena verde de rizos grandes que sale por arriba y a los lados
VN2 = _c('#e0dacd')
def _wraps(view):
    if view == 'front':
        return [L(outline([(14, 96), (12, 46), (24, 22), (50, 14), (76, 22), (88, 46), (86, 70), (60, 70), (54, 84), (66, 96), (50, 104)]), VN2, 'f', True, True),
                L([(14, 40), (86, 52)], OUTC, 'f', False, False, 0.8), L([(14, 58), (60, 66)], OUTC, 'f', False, False, 0.8),
                L([(16, 78), (56, 88)], OUTC, 'f', False, False, 0.8), L([(22, 94), (60, 98)], OUTC, 'f', False, False, 0.8)]
    if view == 'side':
        return [L(outline([(20, 90), (12, 46), (30, 20), (60, 18), (86, 36), (90, 64), (86, 100), (60, 104)]), VN2, 'f', True, True),
                L([(14, 50), (88, 48)], OUTC, 'f', False, False, 0.8), L([(16, 74), (90, 80)], OUTC, 'f', False, False, 0.8)]
    return [L(outline([(14, 90), (12, 46), (24, 22), (50, 14), (76, 22), (88, 46), (86, 90), (50, 100)]), VN2, 'f', True, True),
            L([(14, 44), (86, 60)], OUTC, 'f', False, False, 0.8), L([(14, 70), (86, 80)], OUTC, 'f', False, False, 0.8)]
def _green_curls(view):
    if view == 'side':
        return bush('side', top=-6, w=52, cy=44, n=8, amp=10, seed=36, long=104, flare=8, fr=40) + [L(ell(x, y, 15, 14)) for x, y in ((10, 24), (34, 4), (4, 56), (12, 88))]
    base = bush(view, top=-6, w=54, cy=44, n=8, amp=10, seed=36, long=104, flare=10)
    return base + [L(ell(x, y, 16, 15)) for x, y in ((8, 34), (30, 8), (70, 8), (92, 34), (2, 66), (98, 66), (6, 96), (94, 96))]
C('titania-wraps-khamun', 'chica', P('#6aa024', '#f4cc9a', iris='#c83a1e', shade='#4e6a1e'),
  F(eyes='big', brows=False, mouth='none', hairline=False, ears=False),
  _green_curls('front') + _wraps('front') + [L(ell(36, 75, 5, 6), VN2, 'f', False)],
  _green_curls('side') + _wraps('side'),
  _green_curls('back') + _wraps('back'))

# Tom Bulldown: melena granate larga que le tapa media cara, recogida abajo en una coleta con una goma verde, un paño
# beige doblado sobre la cabeza; orejas de punta, un ojo afilado y media sonrisa
CLT = _c('#d8bc90')
C('tom-bulldown', 'normal', P('#8a2e1c', '#f6d4a4', iris='#3a2a20', shade='#6a2418', deep='#4c1e14'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=False),
  [L(outline([(4, 60), (0, 46, 1), (14, 54)]), 'skin', 'b', True, True), L(outline([(96, 60), (100, 46, 1), (86, 54)]), 'skin', 'b', True, True)] +
  dome('front', top=0, w=46, cy=46, long=104, flare=2) +
  [L(outline([(10, 60), (14, 30), (40, 14), (56, 14), (52, 50), (46, 84), (40, 104), (30, 110, 1), (24, 96), (12, 92)]), 'mid', 'f'),
   L(outline([(52, 12), (84, 18), (88, 46), (56, 44)]), CLT, 'f', True, True), L(ell(36, 100, 5, 3), _c('#7ab040'), 'f', True, True)],
  dome('side', top=0, w=46, cy=46, long=104, flare=2, fr=58) + [L(outline([(40, 6), (86, 16), (90, 44), (44, 40)]), CLT, 'f', True, True)],
  dome('back', top=0, w=46, cy=46, long=104, flare=2, ends=4) + [L(outline([(50, 10), (86, 18), (88, 44), (54, 42)]), CLT, 'f', True, True),
                                                                 L(ell(50, 96, 6, 3), _c('#7ab040'), 'f', True, True)])

# Tom Dark: pelo castaño peinado hacia atrás y pegado, con mechones largos que le caen detrás de las orejas hasta los
# hombros y una coleta atrás; piel tostada, cara larga de barbilla en punta, ojos de ceño fruncido con ojeras
C('tom-dark', 'delgado', P('#7a6250', '#d8985a', iris='#1e1a1a', shade='#5e4a3c', deep='#3e3028'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=97, face_front=face(chin=110, jaw=-2), face_side=face_side(chin=8),
    hairline=[(6, 62), (18, 46), (30, 38), (50, 36), (70, 38), (82, 46), (94, 62)], nose=(50, 88, 2.6)),
  dome('front', top=4, w=44, cy=44, long=112, flare=-4) + [strand([(x, 8), (x + (x - 50) * 0.3, 36)], 'deep', 'b', 1.0) for x in (36, 50, 64)] +
  [mark([(26, 80), (38, 82)], _c('#a86a3a'), w=1.2), mark([(62, 82), (74, 80)], _c('#a86a3a'), w=1.2)],
  dome('side', top=4, w=44, cy=44, long=110, flare=-2, fr=40) + [L(outline([(6, 24), (-24, 46, 1), (-14, 60), (-30, 84, 1), (-6, 58), (4, 40)]))],
  dome('back', top=4, w=44, cy=44, long=110, flare=-4, ends=4) + [L(outline([(42, 20), (58, 20), (60, 90), (50, 108, 1), (40, 90)]), 'shade', 'f', True, True)])

# Tommo Marrow: gorro verde oliva muy ajustado con dos picos como cuernos a los lados; cabeza grande, piel morena, una
# cicatriz en la frente, ojos blancos de ceño muy fruncido y boca torcida con un colmillo
OLV2 = _c('#6a5612')
def _tommo(view):
    if view == 'front':
        return [cap('front', OLV2, top=10, rim=58, w=44, z='f', ln=True), L(outline([(10, 52), (2, 34, 1), (18, 42)]), OLV2, 'f', True, True),
                L(outline([(90, 52), (98, 34, 1), (82, 42)]), OLV2, 'f', True, True)]
    if view == 'side':
        return [cap('side', OLV2, top=10, rim=56, w=44, drop=10, z='f', ln=True), L(outline([(40, 30), (30, 12, 1), (52, 24)]), OLV2, 'f', True, True)]
    return [cap('back', OLV2, top=10, rim=60, w=44, drop=6, z='f', ln=True), L(outline([(10, 52), (2, 34, 1), (18, 42)]), OLV2, 'f', True, True),
            L(outline([(90, 52), (98, 34, 1), (82, 42)]), OLV2, 'f', True, True)]
C('tommo-marrow', 'corpulento', P('#4a3010', '#b07440', iris='#1e1a1a'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=98, face_front=face(w=8, chin=106, jaw=6), face_side=face_side(chin=6, jaw=6),
    hairline=False, ear_out=6, nose=(50, 88, 3)),
  _tommo('front') + [mark([(32, 62), (36, 72), (34, 80)], _c('#6a3a1e'), w=1.2), L(outline([(56, 98), (60, 92), (62, 99)]), WHITE, 'f', True, True)],
  _tommo('side'), _tommo('back'))

# Ton Nino: pelo crema rosado en pinchos que suben a una punta en el centro y se abren hacia atrás por los lados; piel
# morena, cejas gruesas claras, ojos afilados y media sonrisa
C('ton-nino', 'normal', P('#f8dcb4', '#c88e4c', iris='#1e1a1a', shade='#d8b896', deep='#a8866a', brow='#f8dcb4'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=[(6, 62), (18, 52), (30, 46), (44, 50), (50, 40), (56, 50), (70, 46), (82, 52), (94, 62)]),
  dome('front', top=-12, w=46, cy=44, n=7, amp=14, seed=41, sb=66, flare=14) + [L(outline([(36, 20), (50, -16, 1), (64, 20)]))],
  dome('side', top=-12, w=46, cy=44, n=7, amp=14, sweep=-0.6, seed=41, nape=84, fr=46),
  dome('back', top=-12, w=46, cy=44, n=7, amp=14, seed=41, nape=84))

# Tony Tripitaka Sanzang (portera): corona dorada alta de puntas con gajos, un velo granate que le cae desde la corona a
# los lados de la cara hasta los hombros; piel clara, ojos cerrados con pestañas y boca pequeña de disgusto
CRW, CRW2, VEL = _c('#d8c02a'), _c('#9a7a14'), _c('#8a2e48')
def _crown(view):
    if view == 'front':
        pts = [(10, 40), (10, 6)] + [p for i in range(6) for p in ((16 + i * 14, -12, 1), (22 + i * 14, 4))][:-1] + [(90, 6), (90, 40)]
        return [L(outline(pts), CRW, 'f', True, True)] + [L([(x, 0), (x, 38)], CRW2, 'f', False, False, 1.2) for x in (26, 40, 54, 68, 80)]
    if view == 'side':
        pts = [(6, 44), (6, 6)] + [p for i in range(6) for p in ((12 + i * 14, -10, 1), (18 + i * 14, 4))][:-1] + [(90, 4), (90, 40)]
        return [L(outline(pts), CRW, 'f', True, True)] + [L([(x, 0), (x, 40)], CRW2, 'f', False, False, 1.2) for x in (24, 46, 68)]
    pts = [(10, 44), (10, 6)] + [p for i in range(6) for p in ((16 + i * 14, -12, 1), (22 + i * 14, 4))][:-1] + [(90, 6), (90, 44)]
    return [L(outline(pts), CRW, 'f', True, True)]
C('tony-tripitaka-sanzang', 'chica', P('#8a2e48', '#fae4b8', iris='#1e1a1a'),
  F(eyes='closed', brows='angry', mouth='frown', mouth_y=95, hairline=False, ears=False),
  [L(outline([(8, 40), (0, 80), (8, 104, 1), (20, 92), (18, 50)]), VEL), L(outline([(92, 40), (100, 80), (92, 104, 1), (80, 92), (82, 50)]), VEL)] +
  [cap('front', VEL, top=10, rim=48, w=42)] + _crown('front'),
  [L(outline([(10, 40), (2, 80), (14, 104, 1), (40, 96), (50, 60), (40, 44)]), VEL), cap('side', VEL, top=10, rim=48, w=42, drop=8)] + _crown('side'),
  [L(outline([(8, 40), (4, 100), (50, 106), (96, 100), (92, 40)]), VEL)] + _crown('back'))

# Tori Tourer Torrence: pelo rubio verdoso con un flequillo largo echado a un lado que le tapa un ojo y las puntas por la
# mandíbula; gafas de sol rosas con los cristales a rayas blancas; piel clara y sonrisa
PNK = _c('#e8a0c8')
def _tori_specs(view):
    if view == 'front':
        out = []
        for cx, s in ((34, -1), (66, 1)):
            out += [L(outline([(cx - 14 * s, 68), (cx + 12 * s, 70), (cx + 10 * s, 82), (cx - 8 * s, 82)]), PNK, 'f', True, True),
                    L(outline([(cx - 10 * s, 71), (cx + 9 * s, 72), (cx + 7 * s, 79), (cx - 6 * s, 79)]), BLACK, 'f', False)]
            out += [L([(cx - 6, 74), (cx + 4, 73)], WHITE, 'f', False, False, 1.0), L([(cx - 5, 77), (cx + 5, 76)], WHITE, 'f', False, False, 1.0)]
        return out
    return [L(outline([(70, 68), (96, 66), (94, 80), (72, 80)]), PNK, 'f', True, True), L(outline([(74, 71), (92, 70), (90, 77), (76, 77)]), BLACK, 'f', False)]
C('tori-tourer-torrence', 'chica', P('#d6cc60', '#fae4c8', iris='#1e1a1a', shade='#a88a44', deep='#7a5c30'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=93, hairline=False),
  dome('front', top=2, w=46, cy=46, long=96, flare=8) + [L(outline([(4, 60), (14, 22), (44, 6), (80, 14), (96, 40), (100, 52, 1), (78, 40), (66, 46), (60, 84, 1), (54, 50), (40, 54), (24, 70), (10, 84, 1)]), 'mid', 'f')] +
  _tori_specs('front'),
  dome('side', top=2, w=46, cy=46, long=94, flare=6, fr=52) + [L(outline([(60, 10), (96, 30), (106, 44, 1), (84, 42), (80, 60, 1), (70, 44)]), 'mid', 'f')] + _tori_specs('side'),
  dome('back', top=2, w=46, cy=46, long=94, flare=8, ends=4))

# Tracy Tracker (portera): pañuelo azul muy claro atado sobre la cabeza, pelo caoba con flequillo recto y dos trenzas
# largas por delante; ojos grandes verde oliva y sonrisa
SCV = _c('#d0dde0')
def _braid(x, y, n=5):
    return [L(ell(x, y + i * 7, 5.5, 4.6)) for i in range(n)]
C('tracy-tracker', 'chica', P('#a8543a', '#fad0a0', iris='#8a8a2a', shade='#7a3a28'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=[(6, 70), (14, 64), (24, 66), (50, 64), (76, 66), (86, 64), (94, 70)]),
  dome('front', top=4, w=46, cy=46, sb=82) + [L(outline([(2, 60), (6, 30), (24, 8), (50, 2), (76, 8), (94, 30), (98, 60), (96, 70, 1), (84, 48), (50, 40), (16, 48), (4, 70, 1)]), SCV, 'f', True, True)] +
  _braid(14, 84) + _braid(86, 84),
  dome('side', top=4, w=46, cy=46, nape=88, fr=60) + [L(outline([(-2, 70, 1), (2, 30), (24, 6), (50, 0), (78, 8), (94, 30), (90, 44), (50, 36), (20, 46)]), SCV, 'f', True, True)] +
  _braid(70, 86),
  dome('back', top=4, w=46, cy=46, nape=88) + [L(outline([(2, 60), (6, 30), (24, 8), (50, 2), (76, 8), (94, 30), (98, 60), (50, 76, 1)]), SCV, 'f', True, True)] +
  _braid(16, 84) + _braid(84, 84))

# Traylor Beadle: pelo granate oscuro con una cinta verde de zigzag y dos trenzas cortas que salen hacia los lados; piel
# tostada, ojos redondos enormes rojos y sonrisa
GRZ = _c('#5a9a10')
def _zigband(view):
    out = [band(view, GRZ, 34 if view != 'side' else 32, 10, w=48)]
    if view == 'front':
        out.append(L([(4 + i * 8, 40 if i % 2 else 32) for i in range(12)], _c('#a8d050'), 'f', False, False, 1.2))
    return out
C('traylor-beadle', 'chica', P('#6a0e04', '#d8a05a', iris='#c02a1a', shade='#4a0a04'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=[(6, 62), (20, 52), (34, 48), (50, 46), (66, 48), (80, 52), (94, 62)]),
  bush('front', top=2, w=48, cy=46, n=8, amp=5, seed=42, sb=70) + _zigband('front') +
  [L(outline([(10, 74), (-12, 68), (-16, 80, 1), (-4, 86), (12, 84)])), L(outline([(90, 74), (112, 68), (116, 80, 1), (104, 86), (88, 84)]))],
  bush('side', top=2, w=48, cy=46, n=8, amp=5, seed=42, nape=86, fr=52) + _zigband('side') + [L(outline([(24, 76), (6, 86), (4, 98, 1), (18, 94), (32, 84)]))],
  bush('back', top=2, w=48, cy=46, n=8, amp=5, seed=42, nape=86) + _zigband('back') +
  [L(outline([(10, 74), (-12, 68), (-16, 80, 1), (-4, 86), (12, 84)])), L(outline([(90, 74), (112, 68), (116, 80, 1), (104, 86), (88, 84)]))])

# Tribulus Galtrop: pelo castaño oliva en pinchos largos con flequillo que le cae entre los ojos y la melena por detrás
# hasta el cuello, una cinta con placa de metal gris de la que cuelgan dos tiras blancas hasta el pecho; ojos amarillos
# afilados y una perilla oscura
CLW = _c('#e8e0cc')
C('tribulus-galtrop', 'normal', P('#76640a', '#f2dcb8', iris='#d8a020', shade='#5a4c08', deep='#3a3006'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=[(6, 68), (18, 56), (30, 48), (44, 66), (50, 48), (56, 66), (70, 48), (82, 56), (94, 68)],
    face_front=face(chin=104), face_side=face_side(chin=4)),
  dome('front', top=-8, w=50, cy=44, n=8, amp=14, seed=43, long=92, flare=14) +
  [band('front', CLW, 46, 6), L(outline([(34, 42), (66, 42), (64, 54), (36, 54)]), PLT, 'f', True, True),
   L(outline([(18, 50), (24, 50), (24, 120), (18, 120)]), CLW, 'f', True, True), L(outline([(76, 50), (82, 50), (82, 120), (76, 120)]), CLW, 'f', True, True),
   L(outline([(36, 96), (50, 100), (64, 96), (58, 110), (50, 114, 1), (42, 110)]), _c('#3a3020'), 'f', False)],
  dome('side', top=-8, w=50, cy=44, n=8, amp=14, seed=43, long=92, flare=10, fr=56) +
  [band('side', CLW, 44, 6), L(outline([(80, 40), (96, 38), (96, 50), (80, 52)]), PLT, 'f', True, True), L(outline([(66, 52), (72, 52), (74, 120), (68, 120)]), CLW, 'f', True, True),
   L(outline([(78, 98), (90, 100), (84, 112, 1)]), _c('#3a3020'), 'f', False)],
  dome('back', top=-8, w=50, cy=44, n=8, amp=14, seed=43, long=92, flare=14, ends=5) + [band('back', CLW, 44, 6)])

# Ugg O Porc Lemugg: ogro de piel verde azulada, calvo, con dos cuernecillos en la cabeza, un antifaz negro de bandido con
# la cola al viento, nariz de cerdo y dos colmillos que le salen de la boca; cara ancha
GSK, HRN = _c('#86b4a4'), _c('#d8c0b0')
C('ugg-o-porc-lemugg', 'corpulento', P('#86b4a4', '#86b4a4', iris='#1e1a1a', shade='#6a948a'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=98, hairline=False, face_front=face(w=8, chin=106, jaw=8), face_side=face_side(chin=6, jaw=8),
    ear_out=6),
  [L(outline([(26, 40), (30, 22, 1), (36, 38)]), HRN, 'f', True, True), L(outline([(64, 38), (70, 22, 1), (74, 40)]), HRN, 'f', True, True),
   L(outline([(14, 66), (30, 58), (50, 64), (70, 58), (86, 66), (84, 82), (60, 80), (50, 74), (40, 80), (16, 82)]), BLACK, 'f', True, True),
   L(outline([(82, 60), (98, 46, 1), (96, 58), (104, 56, 1), (90, 70)]), BLACK, 'f', True, True),
   L(outline([(26, 72), (40, 68), (40, 76)]), WHITE, 'f', False), L(outline([(74, 72), (60, 68), (60, 76)]), WHITE, 'f', False),
   L(ell(50, 88, 7, 5), _c('#6a948a'), 'f', True, True), L(ell(47, 88, 1.2, 1.6), BLACK, 'f', False), L(ell(53, 88, 1.2, 1.6), BLACK, 'f', False),
   L(outline([(30, 98), (34, 90, 1), (38, 98)]), WHITE, 'f', True, True), L(outline([(62, 98), (66, 90, 1), (70, 98)]), WHITE, 'f', True, True)],
  [L(outline([(54, 30), (58, 12, 1), (64, 28)]), HRN, 'f', True, True), L(outline([(60, 66), (94, 64), (92, 78), (62, 80)]), BLACK, 'f', True, True),
   L(outline([(62, 66), (40, 54, 1), (48, 68), (36, 72, 1), (60, 76)]), BLACK, 'f', True, True), L(ell(92, 88, 5, 5), _c('#6a948a'), 'f', True, True),
   L(outline([(78, 98), (82, 90, 1), (86, 98)]), WHITE, 'f', True, True)],
  [L(outline([(26, 40), (30, 22, 1), (36, 38)]), HRN, 'f', True, True), L(outline([(64, 38), (70, 22, 1), (74, 40)]), HRN, 'f', True, True),
   band('back', BLACK, 64, 6), L(outline([(46, 66), (36, 86, 1), (50, 74), (62, 88, 1), (54, 66)]), BLACK, 'f', True, True)])

# Urbana Street: pelo rosa en media melena recta con un flequillo espeso que le tapa los ojos hasta las pestañas y dos
# moños redondos rosa claro arriba como orejas de oso; ojos entornados y boca pequeña
PK2 = _c('#e47898')
C('urbana-street', 'chica', P('#a8506a', '#faeccc', iris='#1e1a1a', shade='#843e52'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=93, hairline=[(6, 76), (14, 72), (50, 72), (86, 72), (94, 76)]),
  [L(ell(22, 8, 13, 13), PK2, 'b', True, True), L(ell(78, 8, 13, 13), PK2, 'b', True, True)] + dome('front', top=4, w=46, cy=46, long=98, flare=0) +
  [L(outline([(10, 40), (30, 20), (50, 16), (70, 20), (90, 40), (88, 72), (12, 72)]), 'mid', 'f')],
  [L(ell(36, 6, 13, 13), PK2, 'b', True, True)] + dome('side', top=4, w=46, cy=46, long=96, flare=0, fr=72),
  [L(ell(22, 8, 13, 13), PK2, 'b', True, True), L(ell(78, 8, 13, 13), PK2, 'b', True, True)] + dome('back', top=4, w=46, cy=46, long=96, flare=0, ends=3))

# Venus Demila (portera): rastas castañas que le caen hasta los hombros, con un mechón de rastas recogido en una coleta alta
# a un lado con una goma turquesa; piel morena, ojos castaños grandes con pestañas y labios sonrientes
TQ2 = _c('#3ab0a0')
def _dreadlocks(view, xs, top=30, bot=96):
    return [L(outline([(x - 4, top), (x + 4, top), (x + 3, bot), (x, bot + 4, 1), (x - 3, bot)])) for x in xs]
C('venus-demila', 'chica', P('#6a442a', '#c8925e', iris='#4a2a18', shade='#4e301e'),
  F(eyes='big', brows=True, mouth='lips', mouth_y=94, hairline=[(6, 64), (18, 52), (30, 46), (50, 44), (70, 46), (82, 52), (94, 64)]),
  _dreadlocks('front', (6, 14, 86, 94)) + dome('front', top=2, w=46, cy=46, sb=64) +
  [L(outline([(70, 16), (82, 2), (104, 30), (106, 58, 1), (96, 40), (86, 30)])), L(ell(80, 10, 4, 3), TQ2, 'f', True, True),
   strand([(30, 10), (24, 40)], 'deep', 'b', 1.0), strand([(50, 6), (50, 40)], 'deep', 'b', 1.0)],
  _dreadlocks('side', (8, 18, 28, 38)) + dome('side', top=2, w=46, cy=46, nape=80, fr=48) + [L(outline([(30, 6), (16, -8), (-12, 18), (-14, 46, 1), (-2, 28), (14, 20)]))],
  _dreadlocks('back', (8, 20, 32, 44, 56, 68, 80, 92)) + dome('back', top=2, w=46, cy=46, nape=80) +
  [L(outline([(30, 16), (18, 2), (-4, 30), (-6, 58, 1), (4, 40), (14, 30)])), L(ell(22, 10, 4, 3), TQ2, 'f', True, True)])

# Viking Beagle: pañuelo azul marino atado a la cabeza con un dibujo de llamas crema y unas gafas de esquí naranjas enormes
# que le tapan los ojos; piel morena grisácea, pendientes de perla y boca recta
BNV, BCR, SKI = _c('#2e3446'), _c('#e2dece'), _c('#f0a010')
def _viking(view):
    if view == 'front':
        return [cap('front', BNV, top=-2, rim=62, w=46, z='f', ln=True),
                L(outline([(14, 50), (20, 30), (30, 44), (36, 20), (44, 40), (50, 26), (56, 40), (64, 20), (70, 44), (80, 30), (86, 50), (50, 58)]), BCR, 'f', False),
                L(outline([(10, 62), (50, 58), (90, 62), (90, 80), (60, 82), (50, 78), (40, 82), (10, 80)]), _c('#8a3a0a'), 'f', True, True),
                L(outline([(14, 64), (50, 61), (86, 64), (86, 77), (60, 79), (50, 75), (40, 79), (14, 77)]), SKI, 'f', False),
                L(ell(19, 92, 2, 2), WHITE, 'f', True, True), L(ell(81, 92, 2, 2), WHITE, 'f', True, True)]
    if view == 'side':
        return [cap('side', BNV, top=-2, rim=60, w=46, drop=16, z='f', ln=True),
                L(outline([(20, 46), (30, 26), (40, 42), (52, 20), (60, 40), (72, 28), (80, 50), (50, 56)]), BCR, 'f', False),
                L(outline([(54, 62), (96, 60), (96, 78), (56, 80)]), SKI, 'f', True, True), band('side', _c('#8a3a0a'), 64, 4),
                L(ell(48, 92, 2, 2), WHITE, 'f', True, True)]
    return [cap('back', BNV, top=-2, rim=66, w=46, drop=8, z='f', ln=True),
            L(outline([(20, 52), (30, 30), (42, 48), (50, 22), (58, 48), (70, 30), (80, 52), (50, 60)]), BCR, 'f', False), band('back', _c('#8a3a0a'), 66, 4)]
C('viking-beagle', 'normal', P('#2e3446', '#a8866e', iris='#1e1a1a'),
  F(eyes='none', brows=False, mouth='line', mouth_y=96, hairline=False, face_front=face(chin=104), face_side=face_side(chin=4), nose=(50, 88, 3)),
  _viking('front'), _viking('side'), _viking('back'))

# Virgil Milliner: pelo gris muy corto, cascos enormes crema con la diadema morada, gafitas redondas pequeñas y boca torcida
# en zigzag; cara ancha de piel clara
HPC, HPB = _c('#e8dcc0'), _c('#4a3a5a')
def _phones(view):
    if view == 'front':
        return [L(quad((8, 60), (50, -10), (92, 60)), HPB, 'f', False, False, 3.4),
                L(outline([(2, 58), (16, 56), (18, 92), (4, 92)]), HPC, 'f', True, True), L(outline([(98, 58), (84, 56), (82, 92), (96, 92)]), HPC, 'f', True, True)]
    if view == 'side':
        return [L(quad((40, 64), (44, -8), (58, 64)), HPB, 'f', False, False, 3.4), L(ell(46, 74, 12, 15), HPC, 'f', True, True), L(ell(46, 74, 6, 9), _c('#c8bca0'), 'f', False)]
    return [L(quad((8, 60), (50, -6), (92, 60)), HPB, 'f', False, False, 3.4),
            L(outline([(2, 58), (16, 56), (18, 92), (4, 92)]), HPC, 'f', True, True), L(outline([(98, 58), (84, 56), (82, 92), (96, 92)]), HPC, 'f', True, True)]
C('virgil-milliner', 'normal', P('#94947e', '#f8be80', iris='#1e1a1a'),
  F(eyes='dot', brows='angry', mouth='none', hairline=[(6, 60), (18, 48), (34, 42), (50, 40), (66, 42), (82, 48), (94, 60)],
    face_front=face(w=6, chin=102, jaw=6), face_side=face_side(jaw=4), glasses=(220, 220, 210, 255), ears=False),
  dome('front', top=12, w=44, cy=48, sb=60, shade=False) + _phones('front') +
  [L([(42, 96), (46, 93), (50, 96), (54, 93), (58, 96)], OUTC, 'f', False, False, 1.6)],
  dome('side', top=12, w=44, cy=48, nape=80, fr=44, shade=False) + _phones('side') + [L([(80, 96), (84, 93), (88, 96)], OUTC, 'f', False, False, 1.6)],
  dome('back', top=12, w=44, cy=48, nape=80, shade=False) + _phones('back'))

# Virginia Virgo Goldstein: pelo carmesí con una trenza alrededor de la cabeza como corona y una melena ondulada hasta los
# hombros, con un mechón rosa claro en el flequillo; ojos verde azulado grandes y sonrisa
PK3 = _c('#e48aa4')
C('virginia-virgo-goldstein', 'chica', P('#a4425e', '#fad8b8', iris='#2a8a8a', shade='#80304a', deep='#5e2232'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=[(6, 70), (16, 56), (28, 52), (44, 58), (56, 46), (70, 50), (84, 56), (94, 70)]),
  bush('front', top=0, w=48, cy=46, n=8, amp=6, seed=51, long=104, flare=10) + [L(quad((10, 34), (50, 0), (90, 34)), 'deep', 'f', False, False, 2.2),
   L(outline([(40, 46), (48, 24), (64, 26), (60, 48), (52, 62, 1)]), PK3, 'f', True, True)],
  bush('side', top=0, w=48, cy=46, n=8, amp=6, seed=51, long=102, flare=8, fr=56) + [L(quad((14, 40), (44, 2), (90, 24)), 'deep', 'f', False, False, 2.2)],
  bush('back', top=0, w=48, cy=46, n=8, amp=6, seed=51, long=102, flare=10, ends=5) + [L(quad((10, 34), (50, 8), (90, 34)), 'deep', 'f', False, False, 2.2)])

# Walken Stickler Ruhlbuch (portero): pelo azul pizarra en tupé de rizos y una barba rizada que le rodea toda la mandíbula;
# cara ancha, ojillos redondos y media sonrisa pícara
C('walken-stickler-ruhlbuch', 'corpulento', P('#3e545e', '#f8c078', iris='#1e1a1a', shade='#2a3a42', deep='#1e2a30'),
  F(eyes='round', brows='angry', mouth='smile', mouth_y=92, face_front=face(w=4, chin=102, jaw=4), face_side=face_side(jaw=4),
    hairline=[(6, 64), (18, 52), (34, 46), (50, 44), (66, 46), (82, 52), (94, 64)]),
  bush('front', top=-4, w=48, cy=44, n=8, amp=6, seed=52, sb=78) + [L(ell(50, 14, 14, 10), 'shade', 'f', False), L(ell(50, 14, 7, 5), 'mid', 'f', False),
   L(outline([(14, 70), (20, 96), (34, 108), (50, 112), (66, 108), (80, 96), (86, 70), (82, 92), (66, 104), (50, 106), (34, 104), (18, 92)]), 'mid', 'f')],
  bush('side', top=-4, w=48, cy=44, n=8, amp=6, seed=52, nape=86, fr=56) + [L(outline([(52, 72), (60, 100), (76, 108), (88, 104), (78, 98), (64, 94), (60, 72)]), 'mid', 'f')],
  bush('back', top=-4, w=48, cy=44, n=8, amp=6, seed=52, nape=86))

# Walt Whittler (portero): melena ondulada verde oliva oscura y abultada, una pieza naranja en la frente atada a la cabeza
# y una pluma blanca de punta roja; pintura roja de guerra alrededor de los ojos; cara larga morena y boca recta
ORG, FTH = _c('#e8a010'), _c('#f4f0e4')
C('walt-whittler', 'delgado', P('#454032', '#b89a80', iris='#c83a1e', shade='#302a22'),
  F(eyes='round', brows=False, mouth='line', mouth_y=98, face_front=face(chin=108, jaw=-2), face_side=face_side(chin=6),
    hairline=[(6, 66), (16, 54), (30, 50), (50, 48), (70, 50), (84, 54), (94, 66)], nose=(50, 86, 3)),
  bush('front', top=0, w=52, cy=46, n=8, amp=8, seed=53, long=96, flare=10) +
  [band('front', ORG, 44, 6), L(outline([(38, 40), (62, 40), (60, 60), (40, 60)]), ORG, 'f', True, True),
   L(outline([(70, 30), (92, -2), (96, 2), (76, 34)]), FTH, 'f', True, True), L(outline([(90, 0), (96, -10), (98, 2)]), _c('#c83a1e'), 'f', False),
   L(outline([(22, 64), (46, 66), (46, 69), (22, 68)]), _c('#c03020'), 'f', False), L(outline([(78, 64), (54, 66), (54, 69), (78, 68)]), _c('#c03020'), 'f', False),
   L([(40, 80), (42, 94)], _c('#c03020'), 'f', False, False, 2.6), L([(60, 80), (58, 94)], _c('#c03020'), 'f', False, False, 2.6)],
  bush('side', top=0, w=52, cy=46, n=8, amp=8, seed=53, long=94, flare=8, fr=50) + [band('side', ORG, 42, 6),
   L(outline([(30, 30), (10, -2), (6, 2), (26, 34)]), FTH, 'f', True, True), L([(76, 82), (78, 94)], _c('#c03020'), 'f', False, False, 2.6)],
  bush('back', top=0, w=52, cy=46, n=8, amp=8, seed=53, long=94, flare=10, ends=5) + [band('back', ORG, 42, 6),
   L(outline([(70, 30), (92, -2), (96, 2), (76, 34)]), FTH, 'f', True, True)])

# Walter Rally Carr: casco integral amarillo de piloto con la parte de arriba gris, una rendija negra de visor con barrotes
# y la barbilla gris en punta
YH, GH = _c('#f6f010'), _c('#8e8c80')
def _helmet(view):
    if view == 'front':
        return [L(outline([(6, 90), (4, 40), (16, 12), (50, 0), (84, 12), (96, 40), (94, 90), (70, 110), (50, 116, 1), (30, 110)]), YH, 'f', True, True),
                L(outline([(36, 6), (50, 2), (64, 6), (60, 34), (40, 34)]), GH, 'f', False),
                L(outline([(14, 60), (86, 60), (84, 80), (16, 80)]), BLACK, 'f', True, True),
                L(outline([(40, 90), (60, 90), (58, 106), (50, 112, 1), (42, 106)]), GH, 'f', True, True)] + \
            [L([(x, 62), (x, 78)], WHITE, 'f', False, False, 2.2) for x in (28, 40, 52, 64, 76)]
    if view == 'side':
        return [L(outline([(2, 90), (0, 40), (16, 10), (50, 0), (82, 12), (98, 40), (100, 84), (84, 108), (60, 112), (24, 104)]), YH, 'f', True, True),
                L(outline([(30, 4), (60, 2), (74, 30), (40, 34)]), GH, 'f', False), L(outline([(66, 60), (100, 60), (100, 80), (68, 80)]), BLACK, 'f', True, True)]
    return [L(outline([(6, 96), (4, 40), (16, 12), (50, 0), (84, 12), (96, 40), (94, 96), (50, 104)]), YH, 'f', True, True),
            L(outline([(38, 6), (62, 6), (58, 60), (42, 60)]), GH, 'f', False)]
C('walter-rally-carr', 'normal', P('#2a2a1a', '#f6c48e', iris='#1e1a1a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _helmet('front'), _helmet('side'), _helmet('back'))

# Wanda Mage Spelling: sombrero de bruja morado de ala ancha con una cinta naranja y una estrella amarilla, dos trenzas rosa
# a los lados, orejas de punta, coloretes redondos y boca en o
WH, WB, STR, PKB = _c('#584658'), _c('#b8823a'), _c('#f0c840'), _c('#d898b0')
def _witch(view):
    if view == 'front':
        return [L(outline([(16, 46), (26, 10), (50, -16), (76, -30, 1), (70, -10), (82, 14), (84, 46)]), WH, 'f', True, True),
                L(outline([(18, 34), (82, 34), (84, 46), (16, 46)]), WB, 'f', True, True),
                L(outline([(70, 30), (73, 36), (80, 37), (75, 41), (77, 48), (70, 44), (63, 48), (65, 41), (60, 37), (67, 36)]), STR, 'f', True, True),
                L(outline([(-12, 54), (20, 42), (50, 40), (80, 42), (112, 54), (80, 56), (50, 52), (20, 56)]), WH, 'f', True, True)]
    if view == 'side':
        return [L(outline([(10, 46), (20, 10), (40, -14), (14, -26, 1), (40, -20), (66, 6), (80, 44)]), WH, 'f', True, True),
                L(outline([(10, 34), (80, 32), (82, 44), (10, 46)]), WB, 'f', True, True),
                L(outline([(-18, 58), (20, 44), (60, 40), (110, 46), (70, 54), (20, 56)]), WH, 'f', True, True)]
    return [L(outline([(16, 46), (26, 10), (50, -16), (24, -30, 1), (30, -10), (18, 14), (84, 46)]), WH, 'f', True, True),
            L(outline([(18, 34), (82, 34), (84, 46), (16, 46)]), WB, 'f', True, True),
            L(outline([(-12, 54), (20, 44), (50, 42), (80, 44), (112, 54), (80, 58), (50, 56), (20, 58)]), WH, 'f', True, True)]
def _pinkbraid(x, y, n=6):
    return [L(ell(x, y + i * 6, 4.6, 4), PKB, 'b', True, True) for i in range(n)]
C('wanda-mage-spelling', 'chica', P('#3e2e40', '#f4dcc0', iris='#1e1a1a'),
  F(eyes='dot', brows=False, mouth='none', hairline=hl(6, 70, 58, 66, jit=2, seed=54), ears=False),
  _pinkbraid(14, 82) + _pinkbraid(86, 82) + [L(outline([(16, 66), (0, 56, 1), (14, 80)]), 'skin', 'b', True, True), L(outline([(84, 66), (100, 56, 1), (86, 80)]), 'skin', 'b', True, True)] +
  dome('front', top=10, w=44, cy=50, sb=70, shade=False) + _witch('front') + [L(ell(28, 84, 4, 3.4), _c('#f4a0a0'), 'f', False), L(ell(72, 84, 4, 3.4), _c('#f4a0a0'), 'f', False),
   L(ell(50, 94, 2.4, 2.8), _c('#8a3a3a'), 'f', True, True)],
  _pinkbraid(30, 82) + [L(outline([(42, 66), (30, 52, 1), (52, 62), (50, 78)]), 'skin', 'f', True, True)] + dome('side', top=10, w=44, cy=50, nape=82, fr=60, shade=False) + _witch('side'),
  _pinkbraid(16, 82) + _pinkbraid(84, 82) + dome('back', top=10, w=44, cy=50, nape=82, shade=False) + _witch('back'))

# Wesley Pro Provolone (portero): melena amarilla de pinchos enormes alrededor de toda la cabeza como un sol, un antifaz
# rojo anaranjado con los cristales verdes; piel tostada y mueca de dientes
MSR, LNG = _c('#d84a10'), _c('#20b050')
C('wesley-pro-provolone', 'normal', P('#f0bc08', '#d8a868', iris='#1e1a1a', shade='#c89008', deep='#8a6008'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=96, hairline=[(6, 70), (14, 62), (30, 54), (50, 52), (70, 54), (86, 62), (94, 70)]),
  dome('front', top=-16, w=54, cy=48, n=12, amp=18, seed=61, sb=96, flare=16) +
  [L(outline([(10, 66), (50, 62), (90, 66), (88, 82), (60, 84), (50, 78), (40, 84), (12, 82)]), MSR, 'f', True, True),
   L(outline([(22, 70), (44, 72), (42, 80), (26, 78)]), LNG, 'f', False), L(outline([(78, 70), (56, 72), (58, 80), (74, 78)]), LNG, 'f', False)],
  dome('side', top=-16, w=54, cy=48, n=12, amp=18, seed=61, nape=96, fr=58) + [L(outline([(56, 66), (96, 64), (94, 82), (60, 82)]), MSR, 'f', True, True),
                                                                              L(outline([(74, 68), (92, 68), (90, 78), (76, 78)]), LNG, 'f', False)],
  dome('back', top=-16, w=54, cy=48, n=12, amp=18, seed=61, nape=96) + [band('back', MSR, 66, 5)])

# Will Wary: pelo gris azulado en casco de tazón con el flequillo recto por encima de los ojos; ojos cerrados felices y
# sonrisa; piel clara
C('will-wary', 'normal', P('#b8c6c8', '#fcecc8', iris='#1e1a1a', shade='#8e8888', deep='#706060'),
  F(eyes='closed', brows=False, mouth='smile', mouth_y=93, hairline=[(6, 76), (14, 66), (50, 64), (86, 66), (94, 76)]),
  dome('front', top=0, w=50, cy=48, long=84, flare=-2) + [strand([(x, 40), (x + (x - 50) * 0.1, 64)], 'deep', 'b', 1.0) for x in (34, 50, 66)] +
  [strand([(50, 2), (40, 14)], 'deep', 'b', 1.0), strand([(50, 2), (60, 14)], 'deep', 'b', 1.0)],
  dome('side', top=0, w=50, cy=48, long=82, flare=-2, fr=64),
  dome('back', top=0, w=50, cy=48, long=82, flare=-2, ends=3))

# Woody Ellement: media melena lavanda azulada redondeada con dos mechones finísimos larguísimos que le caen a los lados
# hasta el pecho, una espiral morada en la frente; ojos verdes afilados y boca pequeña
SPI = _c('#6a5a9a')
C('woody-ellement', 'normal', P('#8890ba', '#f8c078', iris='#5a8a3a', shade='#6a6280', deep='#4a4060'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=94, hairline=[(6, 74), (16, 60), (28, 54), (40, 64), (50, 50), (60, 64), (72, 54), (84, 60), (94, 74)]),
  [L(quad((20, 80), (-4, 100), (4, 124)), 'mid', 'b', False, False, 2.4), L(quad((80, 80), (104, 100), (96, 124)), 'mid', 'b', False, False, 2.4)] +
  dome('front', top=0, w=50, cy=46, long=86, flare=4) + [L(ell(50, 60, 5, 5), SPI, 'f', False), L(ell(50, 60, 3, 3), _c('#f8c078'), 'f', False),
                                                         L(ell(50, 60, 1.2, 1.2), SPI, 'f', False)],
  dome('side', top=0, w=50, cy=46, long=84, flare=2, fr=58) + [L(quad((50, 84), (60, 104), (56, 124)), 'mid', 'f', False, False, 2.4)],
  dome('back', top=0, w=50, cy=46, long=84, flare=4, ends=4) + [L(quad((14, 80), (-4, 100), (4, 124)), 'mid', 'b', False, False, 2.4),
                                                                 L(quad((86, 80), (104, 100), (96, 124)), 'mid', 'b', False, False, 2.4)])

# Woody Prince: melena verde agua muy clara, ondulada y abultada en mechones que se abren hacia los lados, con una cinta roja
# en la frente; ojos azules afilados y media sonrisa
C('woody-prince', 'normal', P('#88c6c4', '#f8c088', iris='#2a5a9a', shade='#6a8a88', deep='#4e6a68'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=hl(5, 70, 56, 66, lean=-2, jit=3, seed=62)),
  bush('front', top=-4, w=54, cy=46, n=9, amp=12, seed=63, long=92, flare=16) + [band('front', _c('#c82a2a'), 52, 4, w=46)],
  bush('side', top=-4, w=54, cy=46, n=9, amp=12, seed=63, long=90, flare=12, fr=56) + [band('side', _c('#c82a2a'), 50, 4)],
  bush('back', top=-4, w=54, cy=46, n=9, amp=12, seed=63, long=90, flare=16, ends=5) + [band('back', _c('#c82a2a'), 50, 4)])

# Wowzer Bigtop (portero): capucha azul de osito con orejas redondas y el borde de pelo crema, que le abriga hasta el cuello;
# flequillo rubio por dentro, ojos verdes y sonrisa
BHD, FUR = _c('#406a90'), _c('#efe0be')
def _bearhood(view):
    if view == 'front':
        return [L(ell(12, 8, 12, 12), BHD, 'f', True, True), L(ell(88, 8, 12, 12), BHD, 'f', True, True),
                L(outline([(0, 104), (-2, 50), (12, 14), (50, 0), (88, 14), (102, 50), (100, 104), (84, 110), (84, 70), (78, 50), (50, 44), (22, 50), (16, 70), (16, 110)]), BHD, 'f', True, True),
                L(outline([(10, 100), (10, 60), (18, 42), (50, 34), (82, 42), (90, 60), (90, 100), (82, 100), (80, 62), (74, 50), (50, 46), (26, 50), (20, 62), (18, 100)]), FUR, 'f', True, True),
                L(outline([(8, 104), (50, 112), (92, 104), (90, 118), (50, 124), (10, 118)]), BHD, 'f', True, True)]
    if view == 'side':
        return [L(ell(40, 2, 12, 12), BHD, 'f', True, True),
                L(outline([(70, 110), (64, 70), (82, 46), (96, 40), (90, 12), (60, -2), (28, 0), (4, 20), (-4, 60), (0, 100), (30, 116)]), BHD, 'f', True, True),
                L(outline([(70, 106), (62, 70), (80, 44), (96, 40), (96, 48), (86, 52), (74, 72), (78, 106)]), FUR, 'f', True, True)]
    return [L(ell(12, 8, 12, 12), BHD, 'f', True, True), L(ell(88, 8, 12, 12), BHD, 'f', True, True),
            L(outline([(0, 110), (-2, 50), (12, 14), (50, 0), (88, 14), (102, 50), (100, 110), (50, 118)]), BHD, 'f', True, True)]
C('wowzer-bigtop', 'normal', P('#d8b860', '#f6e0bc', iris='#3a9a7a', shade='#a88a40'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=92, hairline=False, ears=False),
  _bearhood('front') + [L(outline([(22, 70), (24, 50), (50, 44), (76, 50), (78, 70), (70, 60), (62, 70, 1), (56, 58), (48, 70, 1), (42, 58), (32, 70, 1)]), 'mid', 'f')],
  _bearhood('side'), _bearhood('back'))

# Wulf Blackbean: melena verde grisácea oscura y ondulada que le tapa media cara, un ojo grande y redondo con la ojera negra
# y labios gruesos; piel morena
C('wulf-blackbean', 'normal', P('#3e4c4c', '#c8a080', iris='#1e1a1a', shade='#2a3434', deep='#1e2626'),
  F(eyes='round', brows=False, mouth='lips', mouth_y=96, mouth_w=10, hairline=False, nose=(58, 86, 2.6)),
  bush('front', top=0, w=50, cy=46, n=6, amp=6, seed=64, long=96, flare=6) +
  [L(outline([(6, 90), (2, 50), (16, 20), (44, 6), (70, 10), (84, 26), (66, 36), (56, 60), (50, 90), (40, 108, 1), (28, 96), (14, 106, 1)]), 'mid', 'f'),
   L(ell(64, 75, 8, 9), BLACK, 'f', False), L(ell(64, 75, 5.6, 6.6), WHITE, 'f', False), L(ell(64, 75, 2.6, 3), BLACK, 'f', False)],
  bush('side', top=0, w=50, cy=46, n=6, amp=6, seed=64, long=94, flare=4, fr=52) + [L(ell(82, 75, 6, 8), BLACK, 'f', False), L(ell(84, 75, 3, 5), WHITE, 'f', False)],
  bush('back', top=0, w=50, cy=46, n=6, amp=6, seed=64, long=94, flare=6, ends=4))

# Xenophon Bicknishan Naudle: pelo castaño oliva oscuro en pinchos de punta por todos lados; ojos afilados de ceño muy
# fruncido y boca recta
C('xenophon-bicknishan-naudle', 'normal', P('#4e4414', '#f8c070', iris='#1e1a1a', shade='#3a3010', deep='#20180a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=hl(6, 66, 50, 62, jit=3, seed=65)),
  dome('front', top=-12, w=48, cy=46, n=10, amp=14, seed=66, sb=70, flare=14),
  dome('side', top=-12, w=48, cy=46, n=10, amp=14, sweep=-0.4, seed=66, nape=86, fr=50),
  dome('back', top=-12, w=48, cy=46, n=10, amp=14, seed=66, nape=86))

# Yasser Yesman Rightaway (portero): pelo verde azulado oscuro en pinchos largos revueltos con un mechón que le cae entre
# los ojos; ojos grandes, unas pecas y sonrisa
C('yasser-yesman-rightaway', 'normal', P('#1e787a', '#f8c078', iris='#1e1a1a', shade='#145050', deep='#0e3a3a'),
  F(eyes='big', brows='angry', mouth='smile', mouth_y=93, hairline=[(6, 66), (18, 56), (32, 50), (44, 70), (50, 52), (60, 60), (72, 50), (84, 56), (94, 66)]),
  dome('front', top=-12, w=50, cy=46, n=9, amp=16, seed=67, sb=72, flare=14) + specs_dot('front', 86, _c('#b87848')),
  dome('side', top=-12, w=50, cy=46, n=9, amp=16, sweep=-0.4, seed=67, nape=86, fr=52) + specs_dot('side', 86, _c('#b87848')),
  dome('back', top=-12, w=50, cy=46, n=9, amp=16, seed=67, nape=86))

# Yurina Kumai: melena castaña larga y lisa con raya en medio y dos trencitas finas a los lados de la cara; ojos negros y
# sonrisa; piel clara
C('yurina-kumai', 'chica', P('#6e501e', '#fae8c0', iris='#1e1a1a', shade='#563c18', deep='#3e2a10'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=[(6, 76), (16, 58), (30, 50), (48, 44), (52, 44), (70, 50), (84, 58), (94, 76)]),
  dome('front', top=2, w=47, cy=46, long=118, flare=2) + [strand([(50, 4), (50, 40)], 'deep', 'b', 1.2),
   L(rope([(16, 54), (14, 80), (16, 106)], 3.2), 'shade', 'f', True, True), L(rope([(84, 54), (86, 80), (84, 106)], 3.2), 'shade', 'f', True, True)] if False else
  dome('front', top=2, w=47, cy=46, long=118, flare=2) + [strand([(50, 4), (50, 40)], 'deep', 'b', 1.2),
   strand([(18, 56), (16, 80), (18, 104)], 'deep', 'f', 3.0), strand([(82, 56), (84, 80), (82, 104)], 'deep', 'f', 3.0)],
  dome('side', top=2, w=47, cy=46, long=116, flare=2, fr=56),
  dome('back', top=2, w=47, cy=46, long=116, flare=2, ends=5) + [strand([(50, 6), (50, 110)], 'deep', 'b', 1.2)])

# Yuta Kitajima: pelo castaño oscuro corto y ondulado, cejas gruesas, piel tostada clara y media sonrisa (retrato de la DS)
C('yuta-kitajima', 'normal', P('#4c3a38', '#ecbc92', iris='#1e1a1a', shade='#38282a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=hl(6, 64, 50, 56, jit=2, seed=71)),
  bush('front', top=2, w=47, cy=46, n=9, amp=5, seed=72, sb=66),
  bush('side', top=2, w=47, cy=46, n=9, amp=5, seed=72, nape=84, fr=50),
  bush('back', top=2, w=47, cy=46, n=9, amp=5, seed=72, nape=84))

# Zahida Afif Zahid: velo azul marino oscuro que le tapa toda la cabeza y la cara salvo una franja para los ojos, rojos y
# afilados, con una cinta más oscura a la altura del cuello
NIQ, NIQ2 = _c('#363a50'), _c('#22232e')
def _niqab(view):
    if view == 'front':
        return [L(outline([(4, 112), (2, 50), (14, 14), (50, 0), (86, 14), (98, 50), (96, 112), (50, 118)]), NIQ, 'f', True, True),
                L(outline([(18, 66), (50, 64), (82, 66), (80, 82), (50, 80), (20, 82)]), _c('#f0b880'), 'f', True, True),
                band('front', NIQ2, 100, 4, w=46)]
    if view == 'side':
        return [L(outline([(2, 108), (-2, 50), (14, 12), (48, 0), (80, 10), (98, 40), (100, 112), (40, 118)]), NIQ, 'f', True, True),
                L(outline([(72, 66), (100, 64), (100, 82), (74, 82)]), _c('#f0b880'), 'f', True, True), band('side', NIQ2, 96, 4)]
    return [L(outline([(4, 112), (2, 50), (14, 14), (50, 0), (86, 14), (98, 50), (96, 112), (50, 118)]), NIQ, 'f', True, True), band('back', NIQ2, 98, 4)]
C('zahida-afif-zahid', 'chica', P('#363a50', '#f0b880', iris='#c02020'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _niqab('front') + [L(outline([(26, 72), (42, 70), (40, 77), (28, 77)]), WHITE, 'f', False), L(outline([(74, 72), (58, 70), (60, 77), (72, 77)]), WHITE, 'f', False),
                     L(ell(35, 74, 2.6, 2.6), _c('#c02020'), 'f', False), L(ell(65, 74, 2.6, 2.6), _c('#c02020'), 'f', False),
                     L([(24, 70), (42, 68)], BLACK, 'f', False, False, 1.6), L([(76, 70), (58, 68)], BLACK, 'f', False, False, 1.6)],
  _niqab('side') + [L(outline([(84, 72), (96, 70), (96, 77), (86, 77)]), WHITE, 'f', False), L(ell(91, 74, 2.2, 2.4), _c('#c02020'), 'f', False)],
  _niqab('back'))

# Zip Windrush: pelo gris malva peinado de golpe hacia un lado en un ala enorme que le tapa medio rostro y sale en punta por
# el lado; piel tostada, un ojo verde, un pendiente rojo y media sonrisa
C('zip-windrush', 'normal', P('#a0889a', '#f6be82', iris='#2a9a3a', shade='#7a6070', deep='#5a4452', light='#c8bcc8'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=False),
  dome('front', top=2, w=46, cy=46, sb=70) + [L(outline([(10, 40), (24, 14), (60, 4), (96, 16), (112, 40, 1), (98, 50), (100, 76, 1), (86, 64), (66, 96, 1),
                                                          (56, 56), (40, 52), (24, 60)]), 'mid', 'f'),
                                              strand([(30, 20), (80, 30), (104, 40)], 'light', 'f', 2.4), strand([(40, 34), (78, 46)], 'light', 'f', 2.0),
                                              L(ell(17, 90, 2, 2), _c('#c8302a'), 'f', True, True)],
  dome('side', top=2, w=46, cy=46, nape=84, fr=46) + [L(outline([(10, 20), (50, 2), (94, 12), (114, 34, 1), (96, 44), (104, 66, 1), (80, 50), (60, 40), (20, 40)]), 'mid', 'f'),
                                                      strand([(20, 22), (90, 24), (108, 34)], 'light', 'f', 2.2), L(ell(48, 90, 2, 2), _c('#c8302a'), 'f', True, True)],
  dome('back', top=2, w=46, cy=46, nape=84) + [L(outline([(-12, 40, 1), (4, 20), (40, 4), (80, 10), (96, 30), (86, 50), (40, 46), (8, 52)]), 'mid', 'f')])

# Zipp Fastener: capucha verde con una cremallera grande que le cruza la cabeza en diagonal y baja hasta el cuello, donde
# asoma el forro amarillo; flequillo castaño oscuro en puntas, ojos castaños y sonrisa
GZP, ZPY, ZPG = _c('#5aaa10'), _c('#e8c020'), _c('#a8a898')
def _zip_hood(view):
    if view == 'front':
        return [L(outline([(2, 100), (0, 46), (12, 14), (50, 0), (88, 14), (100, 46), (98, 96), (84, 104), (84, 66), (70, 52), (30, 48), (16, 60), (16, 100)]), GZP, 'f', True, True),
                L([(10, 30), (40, 10), (78, 4)], ZPG, 'f', False, False, 3.0), L([(86, 50), (86, 100)], ZPG, 'f', False, False, 3.0),
                L(outline([(8, 100), (30, 96), (50, 112), (70, 98), (92, 98), (88, 118), (50, 124), (12, 118)]), GZP, 'f', True, True),
                L(outline([(28, 98), (50, 100), (46, 118), (36, 112)]), ZPY, 'f', True, True)]
    if view == 'side':
        return [L(outline([(70, 104), (64, 70), (80, 46), (96, 38), (90, 12), (60, -2), (28, 0), (4, 20), (-4, 60), (0, 100), (30, 112)]), GZP, 'f', True, True),
                L([(14, 16), (50, 2), (86, 10)], ZPG, 'f', False, False, 3.0), L(outline([(64, 98), (96, 100), (90, 118), (62, 118)]), GZP, 'f', True, True)]
    return [L(outline([(2, 108), (0, 46), (12, 14), (50, 0), (88, 14), (100, 46), (98, 108), (50, 116)]), GZP, 'f', True, True),
            L([(16, 22), (50, 6), (84, 22)], ZPG, 'f', False, False, 3.0)]
C('zipp-fastener', 'normal', P('#3a3022', '#fae8c8', iris='#7a3a1a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=False, ears=False),
  _zip_hood('front') + [L(outline([(16, 60), (26, 50), (60, 48), (78, 56), (84, 64), (72, 62), (64, 72, 1), (58, 60), (46, 70, 1), (40, 60), (28, 72, 1), (22, 62), (10, 70, 1)]), 'mid', 'f')],
  _zip_hood('side') + [L(outline([(70, 52), (96, 46), (100, 54, 1), (84, 56), (88, 66, 1), (72, 60)]), 'mid', 'f')],
  _zip_hood('back'))

# Zowie Trope: pelo azul marino grisáceo despeinado en mechones de punta con uno que le cae por la frente, piel morena,
# cejas gruesas, ojos de ceño fruncido y una perilla oscura
C('zowie-trope', 'normal', P('#42405a', '#d8a060', iris='#3a2a20', shade='#2e2c40', deep='#1e1c2a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 64), (18, 52), (32, 46), (44, 64), (50, 48), (66, 48), (80, 52), (94, 64)],
    face_front=face(chin=104), face_side=face_side(chin=4)),
  dome('front', top=-6, w=48, cy=46, n=8, amp=10, seed=73, sb=68) + [L(outline([(38, 98), (50, 102), (62, 98), (56, 112), (50, 116, 1), (44, 112)]), 'mid', 'f')],
  dome('side', top=-6, w=48, cy=46, n=8, amp=10, sweep=-0.4, seed=73, nape=84, fr=50) + [L(outline([(76, 100), (88, 102), (82, 114, 1)]), 'mid', 'f')],
  dome('back', top=-6, w=48, cy=46, n=8, amp=10, seed=73, nape=84))
