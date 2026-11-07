"""Ojeadores de IE3 (scouts-ie3), tanda 04: dibujados a partir de su retrato de Victory Road; claves 'scouts-ie3:<id>'.

Ninguno tiene modelo 3D propio (el de maxtor-lunde es de otro personaje): el frente sale del retrato y el perfil y la
espalda se deducen. Usa dome()/hl()/face()/face_side() de la tanda 09 de IE1 (masas de pelo y caras) y unas pocas ayudas
propias (gorros, cascos, máscaras)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401
from chars_scouts_ie1_09 import _c, dome, face, face_side, hl, mark  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)
RED = _c('#c8302a')
GOLD = _c('#efc640')


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
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[f'scouts-ie3:{pid}'] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def cap(view, c, top=2, rim=54, w=47, ln=True):
    """Gorro o casco redondo que tapa la cabeza hasta rim (de frente), sin pelo encima."""
    if view == 'front':
        return [L(outline([(50 - w - 1, rim + 2), (50 - w, 30), (30, top + 6), (50, top), (70, top + 6), (50 + w, 30), (50 + w + 1, rim + 2), (50, rim - 2)]), c, 'f', True, ln)]
    if view == 'side':
        return [L(outline([(2, rim + 10), (2, 30), (22, top + 6), (48, top), (74, top + 6), (92, 30), (94, rim - 4), (60, rim - 2), (30, rim + 4)]), c, 'f', True, ln)]
    return [L(outline([(50 - w - 1, rim + 12), (50 - w, 30), (30, top + 6), (50, top), (70, top + 6), (50 + w, 30), (50 + w + 1, rim + 12), (50, rim + 8)]), c, 'f', True, ln)]


def goggles(y, c, frame=(170, 170, 176, 255), sep=15, rx=10, ry=6.5, z='f'):
    """Gafas de piloto (dos lentes con montura) a la altura y."""
    return [L(outline([(50 - sep - rx - 2, y - 1), (50 + sep + rx + 2, y - 1), (50 + sep + rx + 2, y + 2), (50 - sep - rx - 2, y + 2)]), BLACK, z, False),
            L(ell(50 - sep, y, rx + 1.6, ry + 1.6), frame, z, False), L(ell(50 + sep, y, rx + 1.6, ry + 1.6), frame, z, False),
            L(ell(50 - sep, y, rx, ry), c, z, False), L(ell(50 + sep, y, rx, ry), c, z, False),
            L(ell(50 - sep - 3, y - 2, 3, 1.8), WHITE, z, False), L(ell(50 + sep - 3, y - 2, 3, 1.8), WHITE, z, False)]


def teeth(y, w=8, h=4):
    """Boca abierta enseñando los dientes apretados."""
    return [L(outline([(50 - w, y - h / 2), (50 + w, y - h / 2), (50 + w - 1, y + h / 2), (50 - w + 1, y + h / 2)]), WHITE, 'f', True),
            L([(50 - w + 1, y), (50 + w - 1, y)], OUTC, 'f', False, False, 0.9)]


# ------------------------------------------------------------------ jugadores

# Levi Atherton: gorro de punto azul marino con unas gafas de buceo naranjas encima; pelo castaño corto por los lados,
# piel tostada, ojos azules adormilados y media sonrisa
NAVY, ORG = _c('#38364e'), _c('#f09a28')
def _levi(view):
    out = cap(view, NAVY, top=0, rim=52)
    for x in (34, 44, 56, 66):
        if view != 'side':
            out.append(L([(x, 8), (x + (x - 50) * 0.08, 50)], _c('#2a2840'), 'f', False, False, 1.0))
    if view == 'front':
        out += goggles(46, ORG, frame=BLACK, rx=9, ry=5.5)
    elif view == 'side':
        out += [L(ell(82, 44, 6, 5.5), BLACK, 'f', False), L(ell(82, 44, 4.6, 4.2), ORG, 'f', False), L([(76, 44), (4, 52)], BLACK, 'f', False, False, 1.6)]
    else:
        out.append(L([(4, 50), (96, 50)], BLACK, 'f', False, False, 1.8))
    return out
C('levi-leviath-atherton', 'normal', P('#7a4a2a', '#f4b46c', iris='#5a8ab0'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 70), (16, 56), (30, 54), (50, 54), (70, 54), (84, 56), (94, 70)]),
  [L(outline([(12, 76), (10, 56), (20, 50), (80, 50), (90, 56), (88, 76), (82, 64), (18, 64)]))] + _levi('front'),
  [L(outline([(52, 64), (44, 80), (30, 86), (8, 76), (4, 52), (60, 50)]))] + _levi('side'),
  [L(outline([(12, 80), (8, 56), (92, 56), (88, 80), (64, 88), (36, 88)]))] + _levi('back'))

# Liddy Gan (chica): moño enorme granate en dos bolas a los lados con un adorno dorado en media luna encima que baja en
# punta a la frente; piel muy clara, ojos rojos afilados, dos lunares rojos en la frente y pendientes dorados en gota
MAR = _c('#68213b')
def _liddy(view):
    if view == 'front':
        return [L(ell(24, 30, 22, 22), MAR, 'b'), L(ell(76, 30, 22, 22), MAR, 'b'), L(ell(50, 22, 26, 22), MAR, 'b'),
                L(outline([(30, 20), (36, 4), (50, -6, 1), (64, 4), (70, 20), (60, 28), (54, 40), (50, 54, 1), (46, 40), (40, 28)]), GOLD, 'f'),
                L(outline([(42, 18), (50, 4), (58, 18), (50, 30)]), MAR, 'f', False),
                L(ell(42, 63, 1.8, 1.8), RED, 'f', False), L(ell(58, 63, 1.8, 1.8), RED, 'f', False),
                L(outline([(14, 80), (18, 80), (19, 90), (16, 96, 1), (13, 90)]), GOLD, 'f'), L(outline([(82, 80), (86, 80), (87, 90), (84, 96, 1), (81, 90)]), GOLD, 'f')]
    if view == 'side':
        return [L(ell(30, 30, 30, 26), MAR, 'b'), L(ell(56, 18, 24, 18), MAR, 'b'),
                L(outline([(50, 10), (62, -4, 1), (76, 8), (84, 30), (80, 48, 1), (72, 30), (60, 20)]), GOLD, 'f'),
                L(outline([(43, 78), (47, 78), (48, 88), (45, 94, 1), (42, 88)]), GOLD, 'f')]
    return [L(ell(24, 32, 24, 24), MAR, 'b'), L(ell(76, 32, 24, 24), MAR, 'b'), L(ell(50, 26, 28, 24), MAR, 'b'),
            L(outline([(16, 40), (84, 40), (86, 62), (74, 80), (50, 84), (26, 80), (14, 62)]), MAR, 'b'),
            L(outline([(36, 6), (50, -6, 1), (64, 6), (56, 12), (44, 12)]), GOLD, 'f')]
C('liddy-gan', 'chica', P('#68213b', '#fcedc4', iris='#c8201e'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=92, hairline=[(6, 66), (14, 48), (30, 42), (50, 46), (70, 42), (86, 48), (94, 66)]),
  [L(outline([(10, 60), (14, 40), (86, 40), (90, 60), (84, 52), (16, 52)]), MAR)] + _liddy('front'),
  [L(outline([(10, 74), (4, 46), (40, 36), (62, 40), (52, 56), (40, 70)]), MAR)] + _liddy('side'),
  _liddy('back'))

# Lovell Lyons: cara de calavera color hueso con las cuencas negras y ojos rojos, sonrisa de dientes y una X cosida en la
# barbilla; pelo azul marino en mechones de punta que caen por los lados, con una mecha clara
BONE, NVY = _c('#e1d2ba'), _c('#1b204c')
C('lovell-lyons', 'delgado', P('#1b204c', '#e1d2ba', iris='#c8201e', light='#6a72b0'),
  F(eyes='none', brows=False, mouth='none', hairline=[(6, 64), (16, 46), (34, 40), (50, 44), (66, 40), (84, 46), (94, 64)],
    face_front=face(w=-2, chin=106, jaw=-2), face_side=face_side(chin=6)),
  [L(outline([(12, 60), (-6, 84, 1), (10, 70), (-4, 100, 1), (18, 82), (16, 54), (10, 30), (18, 4), (24, -18, 1), (34, 8), (42, -24, 1), (50, 6), (60, -26, 1),
              (66, 8), (80, -12, 1), (82, 20), (96, 18, 1), (90, 40), (86, 56), (82, 82), (104, 100, 1), (90, 70), (106, 84, 1), (88, 58)])),
   strand([(56, -14), (62, 10), (66, 30)], 'light', 'b', 1.6),
   L(ell(36, 76, 8, 7), BLACK, 'f', False), L(ell(64, 76, 8, 7), BLACK, 'f', False),
   L(ell(37, 76, 3, 3.2), RED, 'f', False), L(ell(63, 76, 3, 3.2), RED, 'f', False),
   L(outline([(46, 84), (50, 82), (54, 84), (50, 88)]), BLACK, 'f', False)] + teeth(95, 10, 6) +
  [L([(46, 101), (54, 107)], OUTC, 'f', False, False, 1.2), L([(54, 101), (46, 107)], OUTC, 'f', False, False, 1.2)],
  [L(outline([(54, 56), (62, 42), (82, 38), (96, 20, 1), (80, 16), (86, -10, 1), (66, 4), (60, -26, 1), (46, 2), (28, -18, 1), (24, 8), (4, 6, 1), (8, 30), (-4, 60, 1),
              (8, 58), (2, 92, 1), (20, 76), (26, 98, 1), (34, 74), (44, 64)])),
   strand([(60, -16), (60, 10), (70, 30)], 'light', 'b', 1.6),
   L(ell(80, 76, 6, 6.5), BLACK, 'f', False), L(ell(82, 76, 2.6, 3), RED, 'f', False),
   L(outline([(80, 92), (89, 92), (88, 98), (80, 98)]), WHITE, 'f', True)],
  [L(outline([(12, 80), (-6, 96, 1), (8, 74), (-6, 50, 1), (10, 40), (12, 12), (24, -18, 1), (36, 6), (46, -24, 1), (54, 4), (64, -24, 1), (70, 8), (84, -12, 1),
              (86, 18), (100, 40, 1), (90, 60), (106, 96, 1), (88, 82), (70, 98, 1), (60, 84), (50, 100, 1), (40, 84), (28, 100, 1)])),
   strand([(60, -16), (58, 20), (60, 50)], 'light', 'b', 1.6)])

# Lovell Ribner: turbante de vendas verde agua con una tira suelta que le cruza la cara por un ojo y baja por el cuello;
# arriba, un tapón de bote; pelo castaño corto, piel tostada, cara de pena
TEAL, TEALD, JAR = _c('#39b6a8'), _c('#24756c'), _c('#d8c8a0')
C('lovell-ribbons-ribner', 'delgado', P('#7a5a3a', '#f9c274', iris='#3a2a20'),
  F(eyes='normal', brows=True, mouth='frown', mouth_y=94, hairline=[(6, 70), (16, 58), (50, 56), (84, 58), (94, 70)], face_front=face(chin=106), face_side=face_side(chin=6)),
  [L(outline([(12, 76), (12, 58), (88, 58), (88, 76), (82, 66), (18, 66)]))] + cap('front', TEAL, top=6, rim=58) +
  [L([(10, 46), (90, 34)], TEALD, 'f', False, False, 1.4), L([(10, 32), (88, 50)], TEALD, 'f', False, False, 1.4),
   L(outline([(38, 0), (62, 0), (62, 8), (38, 8)]), TEAL, 'f'), L(outline([(40, -10), (60, -10), (62, 0), (38, 0)]), JAR, 'f'), L(ell(50, -10, 10, 2.4), _c('#a89870'), 'f'),
   L(outline([(16, 56), (30, 60), (70, 82), (86, 90), (84, 98), (66, 92), (26, 72), (12, 66)]), TEAL, 'f'),
   L(outline([(16, 64), (10, 80), (12, 104), (16, 118), (19, 104), (16, 82), (20, 68)]), TEAL, 'f')],
  [L(outline([(52, 66), (44, 80), (30, 84), (10, 74), (8, 56), (60, 54)]))] + cap('side', TEAL, top=6, rim=58) +
  [L(outline([(36, 0), (58, 0), (58, 8), (36, 8)]), TEAL, 'f'), L(outline([(38, -10), (56, -10), (58, 0), (36, 0)]), JAR, 'f'),
   L(outline([(70, 70), (90, 78), (88, 86), (68, 80)]), TEAL, 'f'), L(outline([(44, 64), (38, 84), (40, 110), (44, 112), (44, 86), (48, 66)]), TEAL, 'f')],
  [L(outline([(12, 80), (10, 60), (90, 60), (88, 80), (64, 90), (36, 90)]))] + cap('back', TEAL, top=6, rim=58) +
  [L(outline([(38, 0), (62, 0), (62, 8), (38, 8)]), TEAL, 'f'), L(outline([(40, -10), (60, -10), (62, 0), (38, 0)]), JAR, 'f'),
   L(outline([(80, 64), (84, 80), (86, 110), (82, 112), (78, 84), (76, 66)]), TEAL, 'f')])

# Lucien Brightside (portero): tupé rubio dorado peinado hacia atrás en ondas, con un mechón que cae a un lado; cejas
# doradas gruesas, ojos azules grandes, piel clara, sonrisa amable
C('lucien-brightside', 'normal', P('#dfa331', '#fdeab8', iris='#5a90c0', brow='#c88a28'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=[(6, 66), (14, 52), (26, 42), (44, 40), (60, 38), (76, 42), (86, 52), (94, 66)]),
  [L(outline([(10, 70), (8, 44), (12, 22), (20, 6), (34, -6), (50, -10), (64, -6), (78, 2), (88, 14), (92, 34), (92, 54), (90, 70), (84, 56), (16, 56)])),
   L(outline([(56, -6), (80, 4), (90, 26), (90, 56), (80, 40), (72, 18)]), 'shade', 'b', False),
   strand([(24, 20), (40, 4), (60, 0)], 'shade', 'b', 1.4), strand([(28, 34), (46, 16), (70, 12)], 'shade', 'b', 1.4),
   L(outline([(58, 38), (74, 30), (86, 40), (88, 60), (82, 54), (74, 44)]), 'mid', 'f')],
  [L(outline([(56, 62), (64, 46), (82, 44), (94, 30), (96, 12), (84, 0), (60, -8), (34, -6), (14, 6), (4, 26), (4, 54), (16, 78), (34, 78), (46, 64)])),
   strand([(40, 0), (64, 6), (88, 18)], 'shade', 'b', 1.4), strand([(20, 20), (48, 18), (82, 32)], 'shade', 'b', 1.4)],
  [L(outline([(12, 76), (8, 44), (12, 20), (26, 2), (50, -8), (74, 2), (88, 20), (92, 44), (88, 76), (68, 86), (50, 88), (32, 86)])),
   L(outline([(56, -4), (80, 6), (90, 30), (88, 74), (64, 84), (70, 40)]), 'shade', 'b', False),
   strand([(30, 10), (40, 50), (36, 80)], 'shade', 'b', 1.2), strand([(64, 8), (60, 50), (64, 82)], 'shade', 'b', 1.2)])

# Lucien Thrope (portero): hombre lobo; pelo castaño en greñas de punta con dos orejas de lobo encima y patillas enormes,
# cara clara alargada, ojos rojos furiosos, nariz de hocico, rayas verdes en las mejillas y los dientes apretados
GRN = _c('#5a9a4a')
C('lucien-howler-thrope', 'normal', P('#6c3c19', '#fcdec0', iris='#c8201e'),
  F(eyes='sharp', brows='angry', mouth='none', hairline=[(6, 70), (20, 52), (32, 58), (40, 44), (50, 54), (60, 44), (68, 58), (80, 52), (94, 70)],
    face_front=face(w=-2, chin=106), nose=(50, 86, 3.6)),
  [L(outline([(16, 90), (-4, 100, 1), (6, 80), (-10, 70, 1), (6, 62), (-4, 44, 1), (10, 38), (14, 4, 1), (30, 22), (40, 6), (50, 16), (60, 6), (70, 22), (86, 4, 1),
              (90, 38), (104, 44, 1), (94, 62), (110, 70, 1), (94, 80), (104, 100, 1), (84, 90), (82, 64), (18, 64)])),
   L(outline([(16, 22), (14, 4), (28, 18)]), 'deep', 'b', False), L(outline([(84, 22), (86, 4), (72, 18)]), 'deep', 'b', False),
   L(outline([(58, 8), (86, 6), (92, 40), (88, 84), (80, 60)]), 'shade', 'b', False),
   L([(22, 90), (30, 86)], GRN, 'f', False, False, 1.6), L([(22, 94), (30, 90)], GRN, 'f', False, False, 1.6),
   L([(78, 90), (70, 86)], GRN, 'f', False, False, 1.6), L([(78, 94), (70, 90)], GRN, 'f', False, False, 1.6)] + teeth(97, 10, 7),
  [L(outline([(56, 60), (64, 46), (82, 44), (96, 30, 1), (84, 22), (88, 4, 1), (70, 14), (60, 2, 1), (46, 14), (26, 0, 1), (22, 18), (2, 22, 1), (10, 38), (-8, 56, 1),
              (8, 60), (-4, 84, 1), (14, 80), (14, 100, 1), (28, 86), (40, 92, 1), (44, 74)])),
   L(outline([(54, 12), (60, -6), (68, 12)]), 'deep', 'b', False),
   L([(68, 90), (76, 86)], GRN, 'f', False, False, 1.6), L(outline([(80, 94), (89, 93), (88, 99), (80, 99)]), WHITE, 'f', True)],
  [L(outline([(14, 90), (-4, 100, 1), (6, 80), (-10, 64, 1), (8, 56), (-2, 38, 1), (12, 32), (14, 4, 1), (30, 20), (50, 12), (70, 20), (86, 4, 1), (88, 32), (102, 38, 1),
              (92, 56), (110, 64, 1), (94, 80), (104, 100, 1), (86, 90), (70, 102, 1), (60, 90), (50, 104, 1), (40, 90), (30, 102, 1)])),
   L(outline([(16, 22), (14, 4), (28, 18)]), 'deep', 'b', False), L(outline([(84, 22), (86, 4), (72, 18)]), 'deep', 'b', False),
   L(outline([(56, 14), (86, 10), (92, 50), (86, 88), (64, 96)]), 'shade', 'b', False)])

# Lucien Rarey: melena rosa salmón con tirabuzones gordos a los lados, una diadema de rayas con dos antenas de bolita y
# estrellas amarillas; ojos grandes con un rayo amarillo de pupila y sonrisa
YEL, NAVY2 = _c('#f8d040'), _c('#3a4a8a')
def _antenna(x, y, tx, ty):
    return [L([(x, y), (tx, ty)], NAVY2, 'f', False, False, 1.8), L(ell(tx, ty, 3.2, 3.2), YEL, 'f')]
C('lucien-shiny-rarey', 'normal', P('#c57466', '#efdcb6', iris='#2a1a1a', shade='#9a524b'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, hairline=[(6, 66), (14, 50), (24, 58), (32, 46), (44, 56), (54, 44), (64, 56), (74, 46), (84, 52), (94, 66)]),
  [L(outline([(12, 66), (8, 40), (18, 18), (50, 8), (82, 18), (92, 40), (88, 66), (82, 56), (18, 56)])),
   L(ell(10, 74, 9, 12)), L(ell(12, 94, 8, 11)), L(ell(90, 74, 9, 12)), L(ell(88, 94, 8, 11)),
   strand([(4, 70), (16, 76)], 'shade', 'f', 1.2), strand([(6, 92), (18, 96)], 'shade', 'f', 1.2), strand([(96, 70), (84, 76)], 'shade', 'f', 1.2), strand([(94, 92), (82, 96)], 'shade', 'f', 1.2),
   L(quad((12, 30), (50, 8), (88, 30)), NAVY2, 'f', False, False, 3.2), L(quad((14, 33), (50, 12), (86, 33)), WHITE, 'f', False, False, 1.2)] +
  _antenna(22, 22, 16, 0) + _antenna(78, 22, 84, 0) +
  [L(outline([(14, 34), (18, 28), (20, 34), (26, 36), (20, 38), (18, 44), (16, 38), (10, 36)]), YEL, 'f'),
   L(outline([(86, 34), (82, 28), (80, 34), (74, 36), (80, 38), (82, 44), (84, 38), (90, 36)]), YEL, 'f'),
   L([(37, 71), (34, 76), (38, 76), (35, 81)], YEL, 'f', False, False, 1.4), L([(65, 71), (62, 76), (66, 76), (63, 81)], YEL, 'f', False, False, 1.4)],
  [L(outline([(54, 58), (62, 46), (84, 42), (94, 26), (84, 8), (58, 2), (30, 6), (10, 20), (4, 44), (10, 64), (26, 74), (44, 70)])),
   L(ell(30, 82, 9, 12)), L(ell(32, 102, 8, 10)), strand([(24, 80), (36, 84)], 'shade', 'f', 1.2),
   L(quad((30, 8), (60, 2), (88, 18)), NAVY2, 'f', False, False, 3.2)] + _antenna(62, 4, 66, -16) +
  [L(outline([(70, 18), (74, 12), (76, 18), (82, 20), (76, 22), (74, 28), (72, 22), (66, 20)]), YEL, 'f')],
  [L(outline([(12, 70), (8, 40), (18, 16), (50, 6), (82, 16), (92, 40), (88, 70), (70, 82), (50, 84), (30, 82)])),
   L(ell(12, 80, 9, 12)), L(ell(14, 100, 8, 11)), L(ell(88, 80, 9, 12)), L(ell(86, 100, 8, 11)),
   L(outline([(56, 10), (82, 18), (90, 44), (86, 70), (66, 80)]), 'shade', 'b', False)] +
  _antenna(22, 20, 16, -2) + _antenna(78, 20, 84, -2))

# Luke Nohans: casco de rayas verde oscuro y crema con visera amarilla y una banda negra de antifaz con los ojos blancos
# (uno redondo y otro entornado); sonrisa pícara
HG, HC, VIS = _c('#435245'), _c('#e0e7db'), _c('#fccd05')
def _helmet(view):
    if view == 'front':
        return [L(outline([(6, 76), (4, 40), (16, 14), (50, 2), (84, 14), (96, 40), (94, 76), (84, 76), (84, 60), (16, 60), (16, 76)]), HG, 'f'),
                L(outline([(38, 4), (50, 2), (62, 4), (62, 50), (38, 50)]), HC, 'f', False), L(outline([(20, 12), (28, 8), (30, 50), (20, 50)]), HC, 'f', False),
                L(outline([(80, 12), (72, 8), (70, 50), (80, 50)]), HC, 'f', False),
                L(outline([(10, 52), (16, 38), (50, 34), (84, 38), (90, 52), (50, 56)]), VIS, 'f')]
    if view == 'side':
        return [L(outline([(4, 80), (2, 40), (20, 12), (50, 2), (80, 12), (94, 34), (92, 56), (60, 58), (40, 70), (26, 84)]), HG, 'f'),
                L(outline([(36, 4), (50, 2), (60, 6), (40, 60), (28, 60)]), HC, 'f', False),
                L(outline([(70, 46), (90, 36), (106, 50), (90, 56)]), VIS, 'f')]
    return [L(outline([(6, 86), (4, 40), (16, 14), (50, 2), (84, 14), (96, 40), (94, 86), (50, 92)]), HG, 'f'),
            L(outline([(38, 4), (50, 2), (62, 4), (62, 90), (38, 90)]), HC, 'f', False), L(outline([(20, 12), (28, 8), (30, 88), (20, 86)]), HC, 'f', False),
            L(outline([(80, 12), (72, 8), (70, 88), (80, 86)]), HC, 'f', False)]
C('luke-nohans', 'normal', P('#435245', '#f7bc7c'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=93, hairline=False),
  _helmet('front') + [L(outline([(14, 68), (16, 62), (50, 64), (84, 62), (86, 68), (84, 82), (50, 84), (16, 82)]), BLACK, 'f'),
                      L(ell(36, 73, 4, 5.4), WHITE, 'f', False), L(ell(36, 73, 1.6, 2.6), BLACK, 'f', False),
                      L(outline([(58, 74), (64, 71), (70, 74), (64, 76)]), WHITE, 'f', False)],
  _helmet('side') + [L(outline([(60, 64), (92, 62), (92, 82), (60, 82)]), BLACK, 'f'), L(ell(82, 73, 3, 4.6), WHITE, 'f', False)],
  _helmet('back') + [L(outline([(4, 66), (96, 66), (96, 74), (4, 74)]), BLACK, 'f')])

# Lyle Covet: cabezón calvo de piel naranja con una diadema de metal gris de estrías y dos cuernos amarillos a rayas a
# los lados; gafas de piloto azules, ceño enorme y dos colmillos blancos que salen del labio de abajo
ORS, MET, BLU = _c('#dda15c'), _c('#b9b5b1'), _c('#6a90c8')
def _horn(s):
    x = 50 + s * 40
    return [L(outline([(x, 30), (x + s * 26, 22, 1), (x + s * 4, 42)]), YEL, 'f'),
            L([(x + s * 8, 28), (x + s * 9, 37)], _c('#b88a20'), 'f', False, False, 1.2), L([(x + s * 15, 26), (x + s * 15, 33)], _c('#b88a20'), 'f', False, False, 1.2)]
def _fang(x):
    return L(outline([(x - 3, 98), (x + 3, 98), (x + 1, 88, 1)]), WHITE, 'f')
C('lyle-covet', 'corpulento', P('#dda15c', '#dda15c', iris='#2a2020'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=97, hairline=False, face_front=face(w=8, chin=108, jaw=6, top=8), face_side=face_side(chin=8, jaw=6),
    big_ears=2, ear_out=6),
  [L(outline([(10, 40), (14, 24), (50, 16), (86, 24), (90, 40), (86, 46), (50, 38), (14, 46)]), MET, 'f'),
   L([(30, 22), (30, 42)], _c('#8a8682'), 'f', False, False, 1.2), L([(70, 22), (70, 42)], _c('#8a8682'), 'f', False, False, 1.2)] + _horn(-1) + _horn(1) +
  goggles(68, BLU, frame=MET, sep=16, rx=12, ry=7) + [_fang(36), _fang(64), L([(32, 56), (44, 58)], OUTC, 'f', False, False, 3.0), L([(68, 56), (56, 58)], OUTC, 'f', False, False, 3.0)],
  [L(outline([(6, 44), (16, 22), (48, 14), (80, 22), (94, 40), (90, 48), (50, 38), (12, 50)]), MET, 'f'),
   L(outline([(40, 28), (30, 8, 1), (52, 26)]), YEL, 'f'),
   L(ell(82, 68, 7, 7), MET, 'f', False), L(ell(82, 68, 5.4, 5.4), BLU, 'f', False), L([(76, 66), (40, 62)], BLACK, 'f', False, False, 2.0),
   L(outline([(80, 96), (86, 96), (84, 87, 1)]), WHITE, 'f')],
  [L(outline([(10, 44), (14, 26), (50, 18), (86, 26), (90, 44), (86, 50), (50, 44), (14, 50)]), MET, 'f')] + _horn(-1) + _horn(1) +
  [L(outline([(10, 64), (90, 64), (90, 70), (10, 70)]), BLACK, 'f')])

# Maasa Sudou (chica): melena larga lisa castaño oscuro con raya en medio que cae hasta el pecho; piel clara, ojos
# grandes y redondos, sonrisa
C('maasa-maa-sudou', 'chica', P('#433c30', '#f1eac1', iris='#1e1a16'),
  F(eyes='round', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 64), (18, 46), (36, 38), (50, 34), (64, 38), (82, 46), (94, 64)]),
  dome('front', top=0, w=46, cy=44, long=120, flare=8) + [strand([(50, 6), (50, 32)], 'deep', 'b', 1.2),
   L(outline([(50, 30), (34, 40), (20, 54), (14, 80), (12, 58), (24, 34)]), 'mid', 'f'), L(outline([(50, 30), (66, 40), (80, 54), (86, 80), (88, 58), (76, 34)]), 'mid', 'f')],
  dome('side', top=0, w=46, cy=44, long=122, flare=8, fr=40),
  dome('back', top=0, w=46, cy=44, long=122, flare=8, ends=4))

# Malachi Way (portero): afro castaño enorme y redondo, piel morena, cara alargada, ojos entornados con ojeras y labios
# gruesos naranjas
LIPS = _c('#d8803a')
C('malachi-way', 'delgado', P('#64341a', '#af8c72', iris='#2a1a10', light='#8a5a2a'),
  F(eyes='sharp', brows=True, mouth='none', hairline=[(6, 64), (14, 50), (30, 44), (50, 42), (70, 44), (86, 50), (94, 64)], face_front=face(chin=108), face_side=face_side(chin=8)),
  dome('front', top=-12, w=54, cy=36, n=14, amp=5, soft=True, sb=66, seed=3) +
  [L(quad((37, 96), (50, 86), (63, 96)) + quad((63, 96), (50, 110), (37, 96))[1:], LIPS, 'f'), L([(39, 97), (61, 97)], OUTC, 'f', False, False, 1.0),
   L([(28, 82), (42, 82)], _c('#7a5a44'), 'f', False, False, 1.0), L([(58, 82), (72, 82)], _c('#7a5a44'), 'f', False, False, 1.0)],
  dome('side', top=-12, w=54, cy=36, n=14, amp=5, soft=True, nape=86, fr=44, seed=3) + [L(ell(85, 97, 4, 3.4), LIPS, 'f')],
  dome('back', top=-12, w=54, cy=36, n=14, amp=5, soft=True, nape=86, seed=3))

# Manny Pickles: cara de oso redonda de piel naranja, orejas redondas de oso arriba, un mechón castaño de pinchos en la
# coronilla, ojos furiosos, un lunar y una bocaza roja enseñando los dientes
MOUTH = _c('#da7252')
C('manny-pickles', 'corpulento', P('#573f2f', '#dda357', iris='#1e1a16'),
  F(eyes='sharp', brows='angry', mouth='none', hairline=False, face_front=face(w=8, chin=104, jaw=6, top=14), face_side=face_side(chin=4, jaw=6), ears=False),
  [L(ell(14, 48, 11, 11), 'skin', 'b'), L(ell(86, 48, 11, 11), 'skin', 'b'), L(ell(14, 48, 5, 5), _c('#b87a3a'), 'b', False), L(ell(86, 48, 5, 5), _c('#b87a3a'), 'b', False),
   L(outline([(36, 32), (30, 20, 1), (42, 26), (44, 12, 1), (52, 24), (60, 10, 1), (62, 26), (74, 20, 1), (66, 34), (50, 36)]), 'mid', 'f'),
   L(ell(50, 95, 17, 10), MOUTH, 'f'), L(outline([(40, 90), (60, 90), (58, 97), (42, 97)]), WHITE, 'f', False), L([(41, 93.5), (59, 93.5)], OUTC, 'f', False, False, 0.8),
   L(ell(70, 84, 1.6, 1.6), BLACK, 'f', False), L(ell(50, 84, 3, 2.4), _c('#b8603a'), 'f')],
  [L(ell(44, 34, 11, 11), 'skin', 'b'), L(ell(44, 34, 5, 5), _c('#b87a3a'), 'b', False),
   L(outline([(40, 26), (40, 12, 1), (50, 18), (58, 4, 1), (62, 20), (72, 16, 1), (66, 28), (52, 30)]), 'mid', 'f'),
   L(ell(84, 94, 7, 8), MOUTH, 'f'), L(outline([(80, 90), (90, 90), (90, 97), (80, 97)]), WHITE, 'f', False)],
  [L(ell(14, 36, 11, 11), 'skin', 'b'), L(ell(86, 36, 11, 11), 'skin', 'b'),
   L(outline([(36, 26), (30, 14, 1), (42, 20), (44, 6, 1), (52, 18), (60, 4, 1), (62, 20), (74, 14, 1), (66, 28), (50, 30)]), 'mid', 'f')])

# Mariah Knowles (chica): melena larguísima lisa color crema que le llega por debajo de los hombros, flequillo recto
# hasta los ojos; piel morena, ojos verdes y boca seria
C('mariah-knowles', 'chica', P('#fef6da', '#af8c75', iris='#3a8a3a', shade='#d8c8a8'),
  F(eyes='normal', brows=False, mouth='frown', mouth_y=93, hairline=[(6, 70), (12, 66), (88, 66), (94, 70)]),
  dome('front', top=0, w=48, cy=44, long=124, flare=6) +
  [L(outline([(12, 66), (12, 40), (26, 26), (50, 22), (74, 26), (88, 40), (88, 66), (78, 66), (70, 60), (62, 67), (54, 60), (46, 67), (38, 60), (30, 67), (22, 60)]), 'mid', 'f')],
  dome('side', top=0, w=48, cy=44, long=126, flare=6, fr=60),
  dome('back', top=0, w=48, cy=44, long=126, flare=6, ends=5))

# Marina Coaster (chica): melena corta ondulada verde oliva hasta la barbilla con una cinta de rayas rojas y blancas
# atada en lazo; ojos verdes, coloretes y boca seria
RW = _c('#c8402a')
def _band(view):
    if view == 'front':
        return [L(quad((10, 40), (50, 18), (90, 40)), WHITE, 'f', False, False, 6.0), L(quad((10, 38), (50, 16), (90, 38)), RW, 'f', False, False, 1.6),
                L(quad((11, 43), (50, 21), (89, 43)), RW, 'f', False, False, 1.6),
                L(outline([(62, 24), (74, 14), (78, 26), (70, 30)]), WHITE, 'f'), L(outline([(70, 30), (84, 30), (78, 40)]), WHITE, 'f')]
    if view == 'side':
        return [L(quad((10, 28), (50, 8), (92, 30)), WHITE, 'f', False, False, 6.0), L(quad((10, 26), (50, 6), (92, 28)), RW, 'f', False, False, 1.6),
                L(outline([(62, 12), (72, 2), (78, 16), (70, 20)]), WHITE, 'f')]
    return [L(quad((8, 36), (50, 14), (92, 36)), WHITE, 'f', False, False, 6.0), L(quad((8, 34), (50, 12), (92, 34)), RW, 'f', False, False, 1.6)]
C('marina-coaster', 'chica', P('#b7b483', '#f8d7b6', iris='#2a9a7a', shade='#8e795b'),
  F(eyes='sharp', brows=True, mouth='frown', mouth_y=93, hairline=[(6, 66), (16, 50), (30, 46), (44, 50), (56, 44), (72, 48), (86, 52), (94, 66)]),
  dome('front', top=4, w=48, cy=46, n=7, amp=5, soft=True, long=100, flare=8, seed=4) +
  [L(ell(30, 86, 5, 3), _c('#f0a090'), 'f', False), L(ell(70, 86, 5, 3), _c('#f0a090'), 'f', False)] + _band('front'),
  dome('side', top=4, w=48, cy=46, n=7, amp=5, soft=True, long=100, flare=8, fr=48, seed=4) + _band('side'),
  dome('back', top=4, w=48, cy=46, n=7, amp=5, soft=True, long=100, flare=8, ends=4, seed=4) + _band('back'))

# Mark Brand: pelo morado peinado hacia atrás en una cresta estrecha, frente pintada de rayas negras tribales, gafas de
# sol verdes de visera, cara larguísima y pálida, orejas largas
PUR, VIS2 = _c('#a9858c'), _c('#2d4d37')
C('mark-brand', 'delgado', P('#8a6a8a', '#e1cbae', iris='#1e1a16'),
  F(eyes='none', brows=False, mouth='line', mouth_y=100, hairline=False, face_front=face(w=-6, chin=114, jaw=-4, top=14), face_side=face_side(chin=12),
    big_ears=2, ear_out=2),
  [L(outline([(24, 100), (18, 76), (22, 40), (34, 10), (50, 2), (66, 10), (78, 40), (82, 76), (76, 100), (74, 66), (26, 66)])),
   L(outline([(34, 18), (50, 8), (66, 18), (68, 54), (32, 54)]), 'skin', 'f', False),
   L(outline([(36, 22), (44, 18), (46, 50), (40, 56)]), BLACK, 'f', False), L(outline([(64, 22), (56, 18), (54, 50), (60, 56)]), BLACK, 'f', False),
   L(outline([(47, 30), (53, 30), (52, 50), (48, 50)]), BLACK, 'f', False),
   L(outline([(20, 64), (50, 60), (80, 64), (78, 76), (50, 72), (22, 76)]), VIS2, 'f'), L([(48, 84), (50, 92)], OUTC, 'f', False, False, 1.0)],
  [L(outline([(56, 52), (60, 30), (50, 8), (30, 2), (10, 14), (2, 40), (6, 80), (20, 104), (34, 98), (40, 70), (50, 60)])),
   L(outline([(62, 60), (92, 60), (92, 72), (62, 72)]), VIS2, 'f')],
  [L(outline([(22, 104), (16, 76), (20, 40), (34, 10), (50, 2), (66, 10), (80, 40), (84, 76), (78, 104), (50, 108)])),
   L(outline([(56, 6), (70, 14), (82, 44), (80, 100), (62, 104)]), 'shade', 'b', False)])

# Mark Osman (portero): pelo gris oscuro peinado hacia atrás con un rizo que cae a un lado, parche negro en un ojo con su
# cinta, el otro ojo rojo, orejas grandes y media sonrisa; piel tostada
C('mark-marksman-osman', 'normal', P('#6c7176', '#f8bc7e', iris='#c83a2a'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=92, big_ears=3, ear_out=2, hairline=[(6, 64), (18, 46), (34, 42), (50, 42), (66, 42), (82, 46), (94, 64)]),
  dome('front', top=2, w=46, cy=44, sb=62) + [strand([(30, 10), (34, 40)], 'deep', 'b', 1.2), strand([(46, 6), (48, 40)], 'deep', 'b', 1.2), strand([(64, 8), (62, 40)], 'deep', 'b', 1.2),
   L(outline([(66, 40), (74, 36), (76, 48), (72, 56, 1), (70, 46)]), 'mid', 'f'),
   L([(14, 54), (86, 90)], BLACK, 'f', False, False, 2.2), L(ell(64, 75, 9, 8), BLACK, 'f')],
  dome('side', top=2, w=46, cy=44, nape=84, fr=44) + [L([(52, 60), (82, 64)], BLACK, 'f', False, False, 2.2)],
  dome('back', top=2, w=46, cy=44, nape=84) + [L([(4, 58), (96, 58)], BLACK, 'f', False, False, 2.2)])

# Marshall Artison: pelo negro con un tupé enroscado hacia arriba y dos mechones en punta a los lados, cinta roja en la
# frente; cara ancha tostada, nariz grande, ojos furiosos y los dientes apretados
RBAND = _c('#b8382a')
C('marshall-artison', 'corpulento', P('#302b2b', '#f3bd93', iris='#1e1a16'),
  F(eyes='round', brows='angry', mouth='none', hairline=False, face_front=face(w=6, chin=104, jaw=4, top=20), face_side=face_side(chin=4, jaw=4), nose=(50, 86, 5)),
  [L(outline([(10, 64), (-6, 74, 1), (8, 56), (10, 36), (24, 22), (44, 18), (40, 4), (52, -14), (72, -18, 1), (58, -8), (56, 10), (60, 18), (78, 24), (90, 36), (92, 56),
              (106, 74, 1), (90, 64), (84, 50), (16, 50)])),
   L(outline([(12, 34), (50, 30), (88, 34), (90, 50), (50, 46), (10, 50)]), RBAND, 'f')] + teeth(97, 10, 6),
  [L(outline([(54, 54), (62, 44), (80, 40), (90, 28), (82, 14), (62, 8), (58, -8), (70, -20, 1), (50, -12), (42, 8), (22, 12), (6, 28), (4, 54), (-8, 70, 1), (14, 66),
              (34, 66), (46, 60)])),
   L(outline([(4, 34), (50, 24), (92, 28), (92, 42), (50, 40), (4, 48)]), RBAND, 'f'), L(outline([(82, 92), (89, 92), (88, 98), (82, 98)]), WHITE, 'f', True)],
  [L(outline([(10, 74), (-6, 80, 1), (8, 62), (10, 34), (26, 18), (44, 14), (44, 0), (56, -14), (72, -18, 1), (60, -6), (60, 12), (76, 20), (90, 34), (92, 62), (106, 80, 1),
              (90, 74), (70, 86), (50, 88), (30, 86)])),
   L(outline([(10, 36), (50, 30), (90, 36), (90, 50), (50, 46), (10, 50)]), RBAND, 'f'),
   L(outline([(44, 44), (40, 60), (34, 74, 1), (48, 60), (50, 46)]), RBAND, 'f'), L(outline([(56, 44), (60, 62), (68, 74, 1), (54, 60), (52, 46)]), RBAND, 'f')])

# Martha Hubbard (chica): pelo castaño anaranjado recogido en un moño alto enroscado y un mechón largo suelto que le cae
# por un lado de la cara hasta la barbilla; ojos verde oliva y boca seria
C('martha-hubbard', 'chica', P('#b15105', '#f5bf93', iris='#8a8a3a', shade='#873a09'),
  F(eyes='normal', brows=True, mouth='frown', mouth_y=93, hairline=[(6, 64), (18, 44), (36, 36), (56, 34), (76, 40), (88, 50), (94, 64)]),
  dome('front', top=4, w=46, cy=44, sb=60) +
  [L(outline([(46, 12), (48, -12), (62, -26), (80, -22), (86, -6), (78, 10), (64, 16)])), strand([(56, -20), (78, -14)], 'shade', 'b', 1.2), strand([(52, -6), (80, -2)], 'shade', 'b', 1.2),
   L(outline([(26, 26), (40, 22), (30, 44), (22, 70), (18, 100), (14, 104, 1), (12, 76), (16, 48)]), 'mid', 'f')],
  dome('side', top=4, w=46, cy=44, nape=80, fr=42) + [L(outline([(30, 10), (34, -14), (50, -24), (64, -14), (60, 6), (44, 14)])), strand([(38, -14), (58, -12)], 'shade', 'b', 1.2)],
  dome('back', top=4, w=46, cy=44, nape=80) + [L(outline([(38, 12), (40, -12), (54, -26), (72, -22), (76, -6), (66, 10), (52, 16)])),
   strand([(46, -18), (70, -12)], 'shade', 'b', 1.2), L(outline([(14, 60), (10, 90), (12, 102, 1), (18, 86), (20, 62)]))])

# Marthin Bannister: pelo verde oliva en pinchos revueltos, una cinta clara cruzando la frente; ojos blancos de pupila
# pequeña con mirada de mala uva, orejas grandes y boca torcida
C('marthin-bannister', 'normal', P('#9c9134', '#f9bc7c', iris='#1e1a16', shade='#795d28'),
  F(eyes='dot', brows='angry', mouth='frown', mouth_y=93, big_ears=2, hairline=hl(6, 66, 48, 58, jit=3, seed=21)),
  dome('front', top=-2, w=48, cy=44, n=10, amp=12, seed=21, sb=66) +
  [L(quad((14, 52), (50, 46), (86, 52)), _c('#e8d8b8'), 'f', False, False, 3.2),
   L(ell(36, 76, 6, 5), WHITE, 'f', True), L(ell(64, 76, 6, 5), WHITE, 'f', True), L(ell(37, 76, 1.8, 2.2), BLACK, 'f', False), L(ell(63, 76, 1.8, 2.2), BLACK, 'f', False)],
  dome('side', top=-2, w=48, cy=44, n=10, amp=12, seed=21, nape=86, fr=50),
  dome('back', top=-2, w=48, cy=44, n=10, amp=12, seed=21, nape=86))

# Marty Oshker (chica): pañuelo rojo de abuela que le tapa la cabeza y se ata bajo la barbilla con un lazo; asoma el pelo
# castaño con raya en medio; ojos verde agua, coloretes y sonrisa
SCARF, SCARFD = _c('#bb4242'), _c('#832e2b')
C('marty-m-oshka-oshker', 'chica', P('#705e50', '#f6c299', iris='#4a8a8a'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 70), (20, 52), (36, 46), (50, 48), (64, 46), (80, 52), (94, 70)]),
  [L(outline([(16, 66), (16, 44), (50, 40), (84, 44), (84, 66), (74, 56), (50, 48), (26, 56)])), strand([(50, 40), (50, 52)], 'deep', 'b', 1.2),
   L(outline([(4, 100), (2, 50), (12, 18), (34, 2), (50, -2), (66, 2), (88, 18), (98, 50), (96, 100), (86, 104), (86, 60), (80, 42), (50, 32), (20, 42), (14, 60), (14, 104)]), SCARF, 'f'),
   L(outline([(30, 102), (50, 106), (70, 102), (80, 112), (64, 116), (50, 110), (36, 116), (20, 112)]), SCARF, 'f'),
   L(ell(50, 108, 5, 4), SCARFD, 'f'), L(ell(30, 86, 5, 3.4), _c('#f0a090'), 'f', False), L(ell(70, 86, 5, 3.4), _c('#f0a090'), 'f', False)],
  [L(outline([(60, 54), (2, 104), (0, 50), (12, 16), (40, 0), (66, 4), (86, 18), (94, 38), (80, 42), (60, 46), (56, 70), (60, 100), (50, 106), (30, 108)]), SCARF, 'f'),
   L(outline([(54, 100), (66, 104), (60, 112), (48, 108)]), SCARF, 'f')],
  [L(outline([(4, 104), (2, 50), (12, 18), (34, 2), (50, -2), (66, 2), (88, 18), (98, 50), (96, 104), (70, 112, 1), (50, 116, 1), (30, 112, 1)]), SCARF, 'f'),
   L(outline([(30, 30), (50, 10), (70, 30), (50, 60)]), SCARFD, 'f', False)])

# Mary Curey (portera, chica): gorro alto de fez granate con un adorno dorado de alas y una gema verde agua; melena larga
# azul marino con dos trenzas doradas a los lados que acaban en borlas azules; ojos azul oscuro y sonrisa
FEZ, GEM, NVB = _c('#99395e'), _c('#2aa8a8'), _c('#2a3a6a')
def _fez(view):
    if view == 'front':
        return [L(outline([(16, 52), (18, -6), (50, -10), (82, -6), (84, 52), (50, 48)]), FEZ, 'f'),
                L(outline([(14, 44), (50, 40), (86, 44), (86, 54), (50, 50), (14, 54)]), GOLD, 'f'),
                L(outline([(40, 40), (30, 22), (16, 14, 1), (30, 30), (44, 36)]), GOLD, 'f'), L(outline([(60, 40), (70, 22), (84, 14, 1), (70, 30), (56, 36)]), GOLD, 'f'),
                L(outline([(47, 40), (48, 14), (52, 14), (53, 40)]), GOLD, 'f'), L(ell(50, 42, 5, 5), GEM, 'f')]
    if view == 'side':
        return [L(outline([(10, 52), (14, -6), (50, -10), (84, -4), (88, 44), (50, 46)]), FEZ, 'f'),
                L(outline([(8, 46), (50, 38), (90, 40), (90, 50), (50, 48), (8, 56)]), GOLD, 'f'), L(outline([(80, 38), (86, 18, 1), (88, 38)]), GOLD, 'f')]
    return [L(outline([(16, 54), (18, -6), (50, -10), (82, -6), (84, 54), (50, 50)]), FEZ, 'f'),
            L(outline([(14, 46), (50, 42), (86, 46), (86, 56), (50, 52), (14, 56)]), GOLD, 'f')]
def _braid(x, y0, y1):
    out = [L(outline([(x - 3, y0), (x + 3, y0), (x + 3, y1), (x - 3, y1)]), GOLD, 'f')]
    for y in range(y0 + 4, y1, 6):
        out.append(L([(x - 3, y), (x + 3, y + 2)], _c('#b8902a'), 'f', False, False, 1.0))
    return out + [L(outline([(x - 4, y1), (x + 4, y1), (x + 5, y1 + 10, 1), (x - 5, y1 + 10, 1)]), NVB, 'f')]
C('mary-priest-curey', 'chica', P('#2a3a6a', '#f4ebc1', iris='#2a2a4a'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 66), (14, 56), (30, 54), (50, 58), (70, 54), (86, 56), (94, 66)]),
  [L(outline([(10, 120), (6, 80), (10, 52), (90, 52), (94, 80), (90, 120), (76, 104), (76, 60), (24, 60), (24, 104)])),
   L(outline([(16, 56), (50, 52), (84, 56), (84, 62), (70, 58), (58, 64), (50, 58), (42, 64), (30, 58), (16, 62)]))] + _fez('front') + _braid(13, 60, 104) + _braid(87, 60, 104),
  [L(outline([(54, 60), (40, 70), (34, 118), (10, 120), (4, 80), (6, 50), (60, 48)]))] + _fez('side') + _braid(46, 62, 104),
  [L(outline([(8, 122), (6, 52), (94, 52), (92, 122), (70, 128, 1), (50, 124), (30, 128, 1)]))] + _fez('back') + _braid(12, 62, 108) + _braid(88, 62, 108))

# Matt Skerade (portero): pelo azul marino peinado hacia atrás en mechones; una máscara blanca de hueso que le tapa la
# frente y los ojos, con agujeros negros en punta y ojos amarillos; boca seria
MASK = _c('#eadcbe')
C('matt-masque-skerade', 'normal', P('#36516b', '#eabb95', iris='#e8b820'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=95, hairline=False),
  dome('front', top=0, w=46, cy=44, sb=62) + [strand([(30, 8), (36, 40)], 'deep', 'b', 1.2), strand([(46, 4), (48, 40)], 'deep', 'b', 1.2), strand([(64, 6), (62, 40)], 'deep', 'b', 1.2),
   L(outline([(16, 44), (50, 34), (84, 44), (86, 70), (76, 86), (60, 88), (50, 82), (40, 88), (24, 86), (14, 70)]), MASK, 'f'),
   L(outline([(24, 70), (40, 66), (44, 78), (32, 80)]), BLACK, 'f', False), L(outline([(76, 70), (60, 66), (56, 78), (68, 80)]), BLACK, 'f', False),
   L(ell(36, 74, 2.6, 3), YEL, 'f', False), L(ell(64, 74, 2.6, 3), YEL, 'f', False), L([(50, 52), (50, 80)], _c('#c8b898'), 'f', False, False, 1.0)],
  dome('side', top=0, w=46, cy=44, nape=84, fr=40) +
  [L(outline([(62, 40), (88, 40), (94, 66), (90, 84), (76, 88), (64, 80)]), MASK, 'f'), L(outline([(76, 70), (88, 68), (86, 78), (78, 78)]), BLACK, 'f', False), L(ell(82, 73, 2.2, 2.8), YEL, 'f', False)],
  dome('back', top=0, w=46, cy=44, nape=84) + [strand([(36, 10), (40, 80)], 'deep', 'b', 1.2), strand([(64, 10), (60, 80)], 'deep', 'b', 1.2), L([(8, 62), (92, 62)], _c('#c8b898'), 'f', False, False, 1.4)])

# Maxtor Lunde (con su modelo 3D): pelo corto naranja peinado hacia atrás en surcos con un moño bajo detrás, cascos de
# radio azul marino con micrófono, gafas rectangulares rojas, cara grande con barba de tres días y sonrisa
HS, HSL = _c('#212330'), _c('#4a5a8a')
C('maxtor-lunde', 'corpulento', P('#ca7c24', '#f8be94', iris='#1e1a16', shade='#a14c25'),
  F(eyes='dot', brows=True, mouth='smile', mouth_y=94, face_front=face(w=6, chin=106, jaw=4), face_side=face_side(chin=6, jaw=4), glasses=_c('#d83a2a'), glasses_rect=True,
    nose=(50, 84, 3), hairline=[(6, 62), (16, 50), (30, 42), (50, 40), (70, 42), (84, 50), (94, 62)]),
  dome('front', top=4, w=48, cy=44, sb=58) + [strand([(30, 12), (32, 40)], 'shade', 'b', 1.2), strand([(42, 8), (44, 40)], 'shade', 'b', 1.2),
   strand([(58, 8), (56, 40)], 'shade', 'b', 1.2), strand([(70, 12), (68, 40)], 'shade', 'b', 1.2),
   L(quad((8, 66), (50, -10), (92, 66)), HS, 'f', False, False, 3.0), L(outline([(2, 60), (14, 58), (14, 82), (2, 80)]), HS, 'f'), L(outline([(98, 60), (86, 58), (86, 82), (98, 80)]), HS, 'f'),
   L([(90, 82), (86, 100), (66, 106)], _c('#9a9a8a'), 'f', False, False, 1.4), L(ell(64, 106, 5, 4), BLACK, 'f'),
   L([(30, 100), (32, 104)], _c('#c8906a'), 'f', False, False, 1.0), L([(40, 104), (40, 107)], _c('#c8906a'), 'f', False, False, 1.0),
   L([(60, 104), (60, 107)], _c('#c8906a'), 'f', False, False, 1.0), L([(70, 100), (68, 104)], _c('#c8906a'), 'f', False, False, 1.0)],
  dome('side', top=4, w=48, cy=44, nape=80, fr=42) + [L(ell(4, 56, 12, 10)), strand([(-4, 52), (10, 58)], 'shade', 'b', 1.2),
   L(outline([(40, 2), (50, 2), (52, 56), (42, 56)]), HSL, 'f'), L(ell(46, 70, 10, 11), HS, 'f'), L(ell(46, 70, 5, 6), _c('#4a4048'), 'f', False),
   L([(54, 76), (70, 100), (80, 104)], _c('#9a9a8a'), 'f', False, False, 1.4), L(ell(82, 104, 4.4, 3.6), BLACK, 'f'),
   L(outline([(74, 72), (92, 72), (92, 76), (74, 76)]), _c('#d83a2a'), 'f', False)],
  dome('back', top=4, w=48, cy=44, nape=80) + [L(ell(50, 72, 18, 12)), strand([(36, 70), (64, 70)], 'shade', 'b', 1.2),
   L(quad((8, 66), (50, -10), (92, 66)), HS, 'f', False, False, 3.0), L(outline([(2, 60), (14, 58), (14, 82), (2, 80)]), HS, 'f'), L(outline([(98, 60), (86, 58), (86, 82), (98, 80)]), HS, 'f')])

# May Jarrett (chica): melena rubia anaranjada lisa con un flequillo largo que le tapa un ojo; sobre ese lado, un mechón
# grueso teñido a rayas rojas y granates; el otro ojo entornado y boca pequeña
STR1, STR2 = _c('#dd7039'), _c('#924b24')
C('may-jarrett', 'chica', P('#fdb94c', '#f8dfc4', iris='#3a2a20', shade='#d8902a'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=93, hairline=[(6, 66), (14, 54), (30, 44), (46, 48), (56, 60), (64, 76), (72, 90), (90, 92), (94, 66)]),
  dome('front', top=0, w=48, cy=44, long=100, flare=6) +
  [L(outline([(30, 30), (60, 26), (78, 40), (86, 62), (84, 96), (70, 98), (62, 74), (52, 56), (40, 44)]), 'mid', 'f'),
   L(outline([(60, 40), (80, 44), (88, 64), (86, 80), (70, 76), (62, 56)]), STR1, 'f'), L(outline([(66, 52), (84, 56), (86, 66), (70, 64)]), STR2, 'f', False)],
  dome('side', top=0, w=48, cy=44, long=100, flare=6, fr=60) + [L(outline([(74, 40), (90, 44), (94, 64), (86, 76), (76, 62)]), STR1, 'f')],
  dome('back', top=0, w=48, cy=44, long=100, flare=6, ends=4) + [L(outline([(10, 44), (22, 40), (24, 70), (12, 74)]), STR1, 'f')])

# Melody Toontune (chica): la cabeza envuelta en una tela morada que le tapa la frente, la coronilla vendada color crema,
# melena morada lisa por los lados y una venda crema que le tapa la nariz y la boca; solo se le ven los ojos, grandes
CLOTH, BAND2 = _c('#61356e'), _c('#e8d8b0')
C('melody-toontune', 'chica', P('#61356e', '#fdf4d7', iris='#1e1a1a', shade='#402335'),
  F(eyes='big', brows=False, mouth='none', hairline=False, eye_y=76),
  [L(outline([(8, 120), (6, 70), (12, 50), (88, 50), (94, 70), (92, 120), (78, 106), (78, 66), (22, 66), (22, 106)])),
   L(outline([(10, 40), (20, 14), (50, 4), (80, 14), (90, 40)]), BAND2, 'f'),
   L(outline([(8, 64), (8, 40), (30, 30), (50, 26), (70, 30), (92, 40), (92, 64), (70, 58), (50, 62), (30, 58)]), CLOTH, 'f'),
   L([(12, 46), (86, 54)], _c('#402335'), 'f', False, False, 1.2), L([(14, 58), (88, 42)], _c('#402335'), 'f', False, False, 1.2),
   L(outline([(16, 82), (50, 80), (84, 82), (82, 100), (66, 106), (50, 108), (34, 106), (18, 100)]), BAND2, 'f'),
   L([(20, 90), (80, 98)], _c('#c8b890'), 'f', False, False, 1.0)],
  [L(outline([(54, 66), (40, 70), (36, 118), (10, 120), (4, 80), (6, 50), (60, 50)])),
   L(outline([(8, 40), (20, 12), (48, 2), (76, 10), (90, 34)]), BAND2, 'f'),
   L(outline([(4, 66), (4, 40), (40, 26), (92, 34), (94, 60), (60, 58), (40, 64)]), CLOTH, 'f'),
   L(outline([(60, 82), (90, 80), (92, 100), (80, 106), (62, 104)]), BAND2, 'f')],
  [L(outline([(8, 122), (6, 60), (94, 60), (92, 122), (70, 126, 1), (50, 122), (30, 126, 1)])),
   L(outline([(10, 40), (20, 14), (50, 4), (80, 14), (90, 40)]), BAND2, 'f'),
   L(outline([(6, 70), (6, 40), (50, 26), (94, 40), (94, 70), (50, 64)]), CLOTH, 'f'), L(outline([(44, 60), (56, 60), (60, 84), (50, 80), (40, 84)]), CLOTH, 'f')])

# Meowlinda Purrsival (chica): capucha roja de gata con orejas cosidas y un gran lazo rojo bajo la barbilla; dentro, la
# cara tapada por arriba con una máscara de gato color crema de ojos azules rasgados
HOOD, HOODD, CATM = _c('#a22201'), _c('#78210c'), _c('#ece0c4')
def _stitch(x, y):
    return [L([(x - 3, y - 3), (x + 3, y + 3)], CATM, 'f', False, False, 1.0), L([(x + 3, y - 3), (x - 3, y + 3)], CATM, 'f', False, False, 1.0)]
C('meowlinda-puss-purrsival', 'chica', P('#a22201', '#f0c8a0', iris='#3a8ac8'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, hairline=False),
  [L(outline([(2, 108), (0, 60), (6, 30), (4, -6, 1), (26, 12), (50, 6), (74, 12), (96, -6, 1), (94, 30), (100, 60), (98, 108), (86, 108), (88, 70), (80, 50), (50, 44),
              (20, 50), (12, 70), (14, 108)]), HOOD, 'f'),
   L(outline([(14, 108), (12, 70), (20, 50), (24, 104)]), HOODD, 'f', False), L(outline([(86, 108), (88, 70), (80, 50), (76, 104)]), HOODD, 'f', False),
   L(outline([(20, 56), (50, 48), (80, 56), (84, 72), (70, 84), (56, 86), (50, 94, 1), (44, 86), (30, 84), (16, 72)]), CATM, 'f'),
   L(outline([(24, 70), (40, 66), (44, 74), (30, 76)]), _c('#3a8ac8'), 'f'), L(outline([(76, 70), (60, 66), (56, 74), (70, 76)]), _c('#3a8ac8'), 'f'),
   L(ell(36, 72, 1.4, 2.4), BLACK, 'f', False), L(ell(64, 72, 1.4, 2.4), BLACK, 'f', False),
   L(outline([(24, 104), (50, 110), (76, 104), (90, 116), (70, 122), (50, 114), (30, 122), (10, 116)]), HOOD, 'f'), L(ell(50, 112, 6, 5), HOODD, 'f')] +
  _stitch(22, 16) + _stitch(78, 16) + _stitch(50, 24),
  [L(outline([(60, 52), (2, 108), (0, 50), (10, 16), (24, -6, 1), (36, 8), (60, 4), (80, 14), (94, 40), (78, 46), (62, 60), (60, 100), (50, 110), (30, 110)]), HOOD, 'f'),
   L(outline([(70, 56), (92, 54), (94, 72), (86, 84), (70, 82)]), CATM, 'f'), L(outline([(78, 68), (90, 66), (88, 74), (80, 74)]), _c('#3a8ac8'), 'f'),
   L(outline([(54, 104), (70, 108), (64, 118), (48, 112)]), HOOD, 'f')] + _stitch(30, 14),
  [L(outline([(2, 112), (0, 60), (6, 30), (4, -6, 1), (26, 12), (50, 6), (74, 12), (96, -6, 1), (94, 30), (100, 60), (98, 112), (70, 118, 1), (50, 114), (30, 118, 1)]), HOOD, 'f'),
   L(outline([(30, 30), (50, 14), (70, 30), (50, 70)]), HOODD, 'f', False)] + _stitch(22, 16) + _stitch(78, 16) + _stitch(50, 40))

# Merry Piper: un tocado de plumas crema con las puntas rojas alrededor de un casco dorado, y un velo rojo que le tapa la
# cara entera
FEA, FEAT, HELM, VEIL = _c('#ece0c8'), _c('#c8302a'), _c('#b89a2a'), _c('#a80a0a')
def _feathers(cx, cy, r, a0, a1, n):
    import math
    out = []
    for i in range(n):
        a = math.radians(a0 + (a1 - a0) * i / (n - 1))
        x, y = cx + r * math.cos(a), cy - r * math.sin(a)
        tx, ty = cx + (r + 22) * math.cos(a), cy - (r + 22) * math.sin(a)
        px, py = -math.sin(a) * 6, -math.cos(a) * 6
        out.append(L(outline([(x - px, y - py), (tx, ty, 1), (x + px, y + py)]), FEA, 'b'))
        out.append(L([(cx + (r + 14) * math.cos(a), cy - (r + 14) * math.sin(a)), (tx, ty)], FEAT, 'b', False, False, 2.0))
    return out
C('merry-piper', 'normal', P('#a78921', '#e6d9c2'),
  F(eyes='none', brows=False, mouth='none', hairline=False),
  _feathers(50, 50, 40, -30, 210, 13) +
  [L(outline([(10, 70), (10, 40), (20, 14), (50, 2), (80, 14), (90, 40), (90, 70), (74, 58), (50, 50), (26, 58)]), HELM, 'f'),
   L(outline([(26, 20), (50, 6), (74, 20), (62, 40), (50, 46), (38, 40)]), _c('#d8b84a'), 'f', False),
   L(outline([(16, 58), (50, 48), (84, 58), (86, 90), (70, 106), (50, 112, 1), (30, 106), (14, 90)]), VEIL, 'f'),
   L([(30, 64), (32, 100)], _c('#801010'), 'f', False, False, 1.0), L([(70, 64), (68, 100)], _c('#801010'), 'f', False, False, 1.0)],
  _feathers(46, 50, 40, 60, 260, 10) +
  [L(outline([(4, 74), (4, 40), (18, 12), (48, 2), (78, 12), (92, 36), (94, 60), (60, 54), (30, 64)]), HELM, 'f'),
   L(outline([(60, 52), (94, 58), (96, 90), (84, 104), (64, 108), (58, 80)]), VEIL, 'f')],
  _feathers(50, 50, 40, -40, 220, 14) +
  [L(outline([(8, 84), (8, 40), (20, 14), (50, 2), (80, 14), (92, 40), (92, 84), (50, 90)]), HELM, 'f')])

# Michael Shako (portero): un chacó alto negro con galones dorados y un botón rojo arriba; melena lila lisa por los lados,
# ojos cansados entornados, piel tostada y boca seria
SHAKO, SG = _c('#342d2b'), _c('#cbb748')
def _shako(view):
    if view == 'front':
        return [L(outline([(16, 48), (14, -14), (50, -18), (86, -14), (84, 48), (50, 44)]), SHAKO, 'f'),
                L(outline([(12, 40), (50, 36), (88, 40), (88, 50), (50, 46), (12, 50)]), SG, 'f'),
                L([(20, 34), (50, -12), (80, 34)], SG, 'f', False, False, 2.4), L(ell(50, -14, 4, 4), _c('#c8302a'), 'f'),
                L(outline([(12, 50), (50, 44), (88, 50), (86, 60), (50, 56), (14, 60)]), BLACK, 'f')]
    if view == 'side':
        return [L(outline([(10, 48), (12, -14), (50, -18), (84, -12), (86, 44), (50, 44)]), SHAKO, 'f'),
                L(outline([(6, 40), (50, 36), (90, 38), (90, 48), (50, 46), (6, 50)]), SG, 'f'), L([(20, 34), (50, -12)], SG, 'f', False, False, 2.4),
                L(outline([(60, 46), (96, 44), (102, 56), (64, 54)]), BLACK, 'f')]
    return [L(outline([(16, 52), (14, -14), (50, -18), (86, -14), (84, 52), (50, 48)]), SHAKO, 'f'),
            L(outline([(12, 44), (50, 40), (88, 44), (88, 54), (50, 50), (12, 54)]), SG, 'f'), L([(20, 38), (50, -12), (80, 38)], SG, 'f', False, False, 2.4)]
C('michael-wacko-shako', 'normal', P('#7a6b9a', '#f3c799', iris='#2a1a1a'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=93, hairline=[(6, 66), (14, 58), (50, 60), (86, 58), (94, 66)]),
  [L(outline([(12, 104), (8, 70), (12, 54), (88, 54), (92, 70), (88, 104), (80, 90), (78, 62), (22, 62), (20, 90)]))] + _shako('front') +
  [L([(26, 72), (44, 74)], OUTC, 'f', False, False, 1.4), L([(74, 72), (56, 74)], OUTC, 'f', False, False, 1.4)],
  [L(outline([(54, 60), (44, 74), (40, 102), (14, 100), (4, 70), (6, 52), (60, 50)]))] + _shako('side'),
  [L(outline([(10, 106), (6, 60), (94, 60), (90, 106), (70, 102, 1), (50, 106), (30, 102, 1)]))] + _shako('back'))

# Mike Roscopy: pinchos altos partidos por la mitad, rubios a un lado y rojos al otro; tirita en la nariz, cicatrices en las
# mejillas, ojos verdes afilados y media sonrisa
YH, RH = _c('#d9c723'), _c('#a22f0b')
C('mike-roscopy', 'normal', P('#d9c723', '#f0c5a0', iris='#5a8a2a', shade='#a07824', red=RH, redd=_c('#7a200a')),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=hl(6, 64, 46, 58, jit=3, seed=31)),
  dome('front', top=-6, w=48, cy=44, n=10, amp=16, seed=31, sb=66, shade=False) +
  [L(outline([(50, -30), (60, -14), (74, -22, 1), (74, -2), (92, -6, 1), (88, 14), (104, 22, 1), (94, 38), (100, 56, 1), (90, 64), (80, 58), (60, 50), (50, 48)]), 'red', 'b'),
   L(outline([(52, 62), (60, 48), (66, 56), (76, 46), (82, 58), (86, 66), (70, 66)]), 'red', 'f', False),
   L(outline([(42, 82), (58, 82), (58, 87), (42, 87)]), _c('#e8c8b0'), 'f'), L([(20, 80), (26, 88)], _c('#a0705a'), 'f', False, False, 1.0),
   L([(80, 80), (74, 88)], _c('#a0705a'), 'f', False, False, 1.0)],
  dome('side', top=-6, w=48, cy=44, n=10, amp=16, seed=31, nape=86, fr=50, shade=False) +
  [L(outline([(76, 82), (88, 82), (88, 87), (76, 87)]), _c('#e8c8b0'), 'f')],
  dome('back', top=-6, w=48, cy=44, n=10, amp=16, seed=31, nape=86, c='red', shade=False) +
  [L(outline([(50, -30), (56, -14), (74, -22, 1), (74, -2), (92, -6, 1), (88, 14), (104, 22, 1), (94, 38), (100, 56, 1), (92, 84), (50, 88)]), 'mid', 'b')])

# Miyabi Natsuyaki (chica): media melena castaño dorado con flequillo recto, recogida por una diadema de rayas azul marino
# y blancas; ojos marrones grandes y sonrisa
STRB = _c('#2a2a4a')
C('miyabi-miiya-natsuyaki', 'chica', P('#d19530', '#f3e8d6', iris='#7a3a1e', shade='#a26928'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=[(6, 70), (12, 64), (88, 64), (94, 70)]),
  dome('front', top=0, w=48, cy=46, long=104, flare=4) +
  [L(outline([(12, 64), (14, 42), (30, 30), (50, 28), (70, 30), (86, 42), (88, 64), (74, 62), (62, 66), (50, 62), (38, 66), (26, 62)]), 'mid', 'f'),
   L(quad((12, 34), (50, 6), (88, 34)), STRB, 'f', False, False, 4.0), L(quad((12, 34), (50, 6), (88, 34)), WHITE, 'f', False, False, 1.2)],
  dome('side', top=0, w=48, cy=46, long=104, flare=4, fr=60) + [L(quad((10, 26), (50, 2), (90, 30)), STRB, 'f', False, False, 4.0)],
  dome('back', top=0, w=48, cy=46, long=104, flare=4, ends=4) + [L(quad((8, 32), (50, 6), (92, 32)), STRB, 'f', False, False, 4.0)])

# Momoko Tsugunaga (chica; retrato de DS): melena negra azulada lisa con flequillo y una diadema blanca; ojos oscuros y
# sonrisa
C('momoko-peaches-tsugunaga', 'chica', P('#323947', '#f5e3c0', iris='#202533'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=93, hairline=[(6, 66), (14, 54), (24, 64), (34, 52), (46, 64), (56, 52), (66, 64), (76, 52), (86, 60), (94, 66)]),
  dome('front', top=0, w=48, cy=46, long=104, flare=6) + [L(quad((12, 34), (50, 8), (88, 34)), WHITE, 'f', False, False, 3.6)],
  dome('side', top=0, w=48, cy=46, long=104, flare=6, fr=56) + [L(quad((10, 26), (50, 2), (90, 30)), WHITE, 'f', False, False, 3.6)],
  dome('back', top=0, w=48, cy=46, long=104, flare=6, ends=4) + [L(quad((8, 32), (50, 6), (92, 32)), WHITE, 'f', False, False, 3.6)])

# Monarch Rome: pelo verde agua grisáceo revuelto en greñas de punta que le enmarcan la cara y caen por los lados; ojos
# cerrados y sonrisa tranquila
C('monarch-rome', 'normal', P('#a2b6aa', '#fdefca', iris='#2a2a2a', shade='#7c8a84'),
  F(eyes='closed', brows='angry', mouth='smile', mouth_y=93, hairline=[(6, 70), (16, 54), (26, 58), (30, 44), (44, 50), (54, 40), (66, 50), (74, 44), (82, 56), (94, 70)]),
  dome('front', top=-4, w=52, cy=46, n=12, amp=10, seed=41, long=100, flare=10, soft=False),
  dome('side', top=-4, w=52, cy=46, n=12, amp=10, seed=41, long=100, flare=10, fr=48),
  dome('back', top=-4, w=52, cy=46, n=12, amp=10, seed=41, long=100, flare=10, ends=5))

# Montaine Skalin: rastas gruesas a rayas naranjas y amarillas que salen en abanico de la coronilla, como cuernos;
# piel tostada, un ojo naranja y el otro verde agua, un pendiente de aro de metal y boca seria
DR1, DR2 = _c('#e0a020'), _c('#cd5b06')
def _dread(x, y, tx, ty, w=6):
    import math
    dx, dy = tx - x, ty - y
    n = math.hypot(dx, dy)
    px, py = -dy / n * w, dx / n * w
    out = [L(outline([(x - px, y - py), (x + dx * 0.6 - px * 0.9, y + dy * 0.6 - py * 0.9), (tx, ty, 1), (x + dx * 0.6 + px * 0.9, y + dy * 0.6 + py * 0.9), (x + px, y + py)]), DR1, 'b')]
    for t in (0.3, 0.55, 0.78):
        cx, cy = x + dx * t, y + dy * t
        out.append(L([(cx - px * 0.9, cy - py * 0.9), (cx + px * 0.9, cy + py * 0.9)], DR2, 'b', False, False, 2.4))
    return out
def _skalin(view):
    if view == 'front':
        spots = [(50, 20, 50, -24), (40, 22, 28, -18), (60, 22, 72, -18), (32, 26, 10, -6), (68, 26, 90, -6), (24, 34, -2, 14), (76, 34, 102, 14)]
    elif view == 'side':
        spots = [(46, 20, 50, -24), (36, 22, 20, -16), (56, 22, 74, -14), (26, 28, 2, 2), (66, 30, 94, 10), (18, 40, -8, 30)]
    else:
        spots = [(50, 22, 50, -22), (40, 24, 26, -16), (60, 24, 74, -16), (30, 30, 6, -2), (70, 30, 94, -2), (22, 40, -4, 26), (78, 40, 104, 26), (50, 40, 50, 40)]
    out = []
    for s in spots:
        if s[1] != s[3]:
            out += _dread(*s)
    return out
C('montaine-skalin', 'delgado', P('#bb7608', '#be844c', iris='#c87a20', shade='#833f08'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, face_front=face(chin=106), face_side=face_side(chin=6),
    hairline=[(6, 60), (16, 46), (30, 40), (42, 50), (50, 62), (58, 50), (70, 40), (84, 46), (94, 60)]),
  _skalin('front') + [L(outline([(14, 54), (16, 34), (30, 22), (50, 18), (70, 22), (84, 34), (86, 54), (66, 44), (50, 60, 1), (34, 44)]), 'mid', 'b'),
                      L(ell(64, 76, 3.2, 4), _c('#3aa8a0'), 'f', False), L(ell(14, 80, 3, 3), _c('#a8a8b0'), 'f', False)],
  _skalin('side') + [L(outline([(56, 50), (62, 38), (80, 34), (70, 22), (46, 16), (20, 22), (8, 40), (14, 60), (30, 60), (44, 52)]), 'mid', 'b')],
  _skalin('back') + [L(outline([(14, 70), (12, 40), (26, 22), (50, 16), (74, 22), (88, 40), (86, 70), (50, 78)]), 'mid', 'b')])

# Monty Tasker: pelo morado corto en pinchos hacia arriba, piel morena, ojos redondos con el ceño fruncido, pecas y una
# bocaza abierta riéndose
C('monty-tasker', 'normal', P('#6e5179', '#cc966b', iris='#1e1a16', shade='#513b4b'),
  F(eyes='round', brows='angry', mouth='none', hairline=[(6, 62), (18, 46), (34, 42), (50, 44), (66, 42), (82, 46), (94, 62)]),
  dome('front', top=-6, w=46, cy=44, n=9, amp=10, seed=33, sb=62) +
  [L(quad((36, 92), (50, 88), (64, 92)) + quad((64, 92), (50, 110), (36, 92))[1:], _c('#5a3a2a'), 'f'),
   L(ell(28, 86, 0.9, 0.9), _c('#7a4a30'), 'f', False), L(ell(32, 88, 0.9, 0.9), _c('#7a4a30'), 'f', False), L(ell(68, 86, 0.9, 0.9), _c('#7a4a30'), 'f', False),
   L(ell(72, 88, 0.9, 0.9), _c('#7a4a30'), 'f', False)],
  dome('side', top=-6, w=46, cy=44, n=9, amp=10, seed=33, nape=84, fr=46) + [L(outline([(80, 90), (90, 90), (88, 102), (80, 98)]), _c('#5a3a2a'), 'f')],
  dome('back', top=-6, w=46, cy=44, n=9, amp=10, seed=33, nape=84))

# Morty Portland: una mata de rizos gris verdoso que le tapa media cara en zigzag, por encima de un ojo; asoma la lengua
# por un lado de la sonrisa
C('morty-portland', 'normal', P('#868d72', '#cd986f', iris='#2a2a2a', shade='#5d5544'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=94, hairline=False, eye_sep=14),
  dome('front', top=-2, w=50, cy=44, n=12, amp=7, soft=True, seed=35, sb=70) +
  [L(outline([(10, 70), (14, 52), (30, 50), (50, 48), (64, 52), (70, 62), (62, 66), (58, 76), (50, 74), (46, 84), (36, 82), (32, 92), (22, 86), (14, 82)]), 'mid', 'f'),
   L(outline([(56, 94), (62, 96), (64, 100), (58, 100)]), _c('#e06a6a'), 'f')],
  dome('side', top=-2, w=50, cy=44, n=12, amp=7, soft=True, seed=35, nape=86, fr=52),
  dome('back', top=-2, w=50, cy=44, n=12, amp=7, soft=True, seed=35, nape=86))

# Mykerinos Menkh: cabezón calvo de piel castaña, una cicatriz clara cruzando un ojo, ojos furiosos, nariz ancha y una
# boca enfadada con dos colmillos
C('mykerinos-menkaure-menkh', 'corpulento', P('#884a28', '#b77339', iris='#1e1a16'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, hairline=False, face_front=face(w=8, chin=106, jaw=8, top=6), face_side=face_side(chin=6, jaw=8),
    nose=(50, 86, 4), ear_out=6),
  [L(outline([(64, 46), (70, 44), (66, 86), (60, 88)]), _c('#e0b090'), 'f', False),
   L(outline([(38, 96), (42, 96), (40, 91, 1)]), WHITE, 'f'), L(outline([(58, 96), (62, 96), (60, 91, 1)]), WHITE, 'f')],
  [L(outline([(86, 94), (89, 94), (87, 89, 1)]), WHITE, 'f')], [])

# Narcissa Plane (chica): pelo rojo con una coleta lateral enorme que baja por un lado en un rizo gordo; piel clara, ojos
# verde agua afilados y labios rosas en morrito
C('narcissa-hotstuff-plane', 'chica', P('#952219', '#fdeab9', iris='#3a9aa8', shade='#631d17'),
  F(eyes='sharp', brows='angry', mouth='lips', mouth_w=5, mouth_y=95, hairline=[(6, 64), (16, 46), (30, 38), (50, 34), (66, 40), (82, 48), (94, 64)]),
  dome('front', top=0, w=46, cy=44, sb=62) +
  [L(outline([(70, 30), (90, 44), (96, 70), (90, 96), (76, 110), (80, 122), (96, 118), (90, 128), (70, 126), (66, 110), (80, 92), (86, 70), (80, 48)])),
   L(outline([(14, 50), (20, 34), (30, 28), (22, 50), (16, 74), (8, 72)]), 'mid', 'f')],
  dome('side', top=0, w=46, cy=44, nape=82, fr=40) + [L(outline([(14, 50), (2, 70), (6, 100), (-6, 118), (10, 124), (16, 102), (12, 74), (24, 58)]))],
  dome('back', top=0, w=46, cy=44, nape=82) + [L(outline([(26, 40), (8, 50), (2, 80), (10, 100), (-2, 118), (16, 124), (20, 100), (14, 74), (34, 54)]))])

# Nat Meg: pelo gris recogido en un moño alto metido en una funda amarilla de corona con un pasador; dos mechones lisos le
# enmarcan la cara; piel tostada, ojos rojizos afilados y media sonrisa
CROWN = _c('#ead317')
C('nat-nutmeg-meg', 'normal', P('#828c92', '#fbca84', iris='#8a3a20', shade='#626a70'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=[(6, 64), (14, 52), (26, 40), (40, 34), (50, 36), (60, 34), (74, 40), (86, 52), (94, 64)]),
  dome('front', top=8, w=44, cy=46, sb=58) + [strand([(30, 16), (40, 38)], 'shade', 'b', 1.2), strand([(70, 16), (60, 38)], 'shade', 'b', 1.2),
   L(outline([(14, 50), (22, 36), (20, 70), (18, 100), (12, 102, 1), (10, 70)]), 'mid', 'f'), L(outline([(86, 50), (78, 36), (80, 70), (82, 100), (88, 102, 1), (90, 70)]), 'mid', 'f'),
   L(outline([(36, 10), (36, -6), (44, -16), (56, -16), (64, -6), (64, 10)]), CROWN, 'f'), L([(44, -14), (44, 8)], _c('#b8a010'), 'f', False, False, 1.2),
   L([(56, -14), (56, 8)], _c('#b8a010'), 'f', False, False, 1.2), L([(26, -4), (74, -4)], _c('#b84a2a'), 'f', False, False, 2.2)],
  dome('side', top=8, w=44, cy=46, nape=82, fr=40) + [L(outline([(30, 10), (30, -6), (38, -16), (50, -16), (56, -6), (56, 10)]), CROWN, 'f'),
   L([(20, -4), (66, -4)], _c('#b84a2a'), 'f', False, False, 2.2)],
  dome('back', top=8, w=44, cy=46, nape=82) + [L(outline([(36, 10), (36, -6), (44, -16), (56, -16), (64, -6), (64, 10)]), CROWN, 'f'),
   L([(26, -4), (74, -4)], _c('#b84a2a'), 'f', False, False, 2.2)])

# Natsuki Yoshida (portero; retrato de DS): pelo negro corto liso con flequillo, piel tostada, ojos marrones y sonrisa
C('natsuki-catchan-yoshida', 'normal', P('#484643', '#f3b27a', iris='#5a3a20'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=92, hairline=hl(5, 64, 50, 60, jit=2, seed=39)),
  dome('front', top=2, w=48, cy=44, n=9, amp=5, seed=39, sb=68),
  dome('side', top=2, w=48, cy=44, n=9, amp=5, seed=39, nape=86, fr=50),
  dome('back', top=2, w=48, cy=44, n=9, amp=5, seed=39, nape=86))

# Neville Boyle: rizos verdes cortos, cejas verdes gruesas fruncidas, cara enorme y redonda de piel gris parda, nariz naranja
# y boca seria
C('neville-boyle', 'corpulento', P('#33aa5d', '#ae8b71', iris='#1e1a16', brow='#2a8a4a'),
  F(eyes='dot', brows='angry', mouth='frown', mouth_y=95, face_front=face(w=10, chin=106, jaw=8, top=20), face_side=face_side(chin=6, jaw=8),
    nose=(50, 84, 3.4), ear_out=8, hairline=hl(6, 60, 46, 54, jit=2, seed=40)),
  dome('front', top=10, w=50, cy=46, n=12, amp=6, soft=True, seed=40, sb=60) +
  [L([(28, 68), (42, 72)], _c('#2a8a4a'), 'f', False, False, 3.6), L([(72, 68), (58, 72)], _c('#2a8a4a'), 'f', False, False, 3.6)],
  dome('side', top=10, w=48, cy=46, n=12, amp=6, soft=True, seed=40, nape=80, fr=46),
  dome('back', top=10, w=50, cy=46, n=12, amp=6, soft=True, seed=40, nape=80))

# Neville Goodenough: pelo azul marino corto y rizado, gafas rectangulares negras de cristal claro, piel tostada y una
# sonrisa enorme de dientes apretados
C('neville-goodenough', 'normal', P('#3b535e', '#fbc273', iris='#1e1a16', shade='#2a3a42'),
  F(eyes='sharp', brows='angry', mouth='none', glasses=BLACK, glasses_rect=True, hairline=hl(6, 62, 46, 52, jit=2, seed=41)),
  dome('front', top=0, w=46, cy=44, n=12, amp=5, soft=True, seed=41, sb=62) +
  [L(outline([(27, 70), (45, 70), (44, 81), (28, 81)]), _c('#d8e8f0'), 'f', False), L(outline([(55, 70), (73, 70), (72, 81), (56, 81)]), _c('#d8e8f0'), 'f', False)] +
  teeth(94, 12, 6),
  dome('side', top=0, w=46, cy=44, n=12, amp=5, soft=True, seed=41, nape=84, fr=46) + [L(outline([(80, 90), (89, 90), (88, 97), (80, 97)]), WHITE, 'f', True)],
  dome('back', top=0, w=46, cy=44, n=12, amp=5, soft=True, seed=41, nape=84))

# Newt Perfect: una máscara tiki que le tapa la cabeza entera: arriba naranja con un galón crema y dos cuernos curvos
# blancos y naranjas, la cara marrón con dos ojos redondos negros y una boca de dientes en zigzag
TKO, TKB, TKC = _c('#d95306'), _c('#664722'), _c('#e8e1cd')
def _thorn(s):
    x = 50 + s * 40
    return [L(outline([(x, 28), (x + s * 14, 14), (x + s * 10, -10, 1), (x + s * 2, 12), (x - s * 4, 22)]), TKC, 'b'),
            L([(x + s * 6, 18), (x + s * 14, 10)], TKO, 'b', False, False, 3.0)]
C('newt-tiki-perfect', 'normal', P('#664722', '#664722'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _thorn(-1) + _thorn(1) +
  [L(outline([(8, 104), (6, 50), (12, 20), (30, 4), (50, 0), (70, 4), (88, 20), (94, 50), (92, 104), (50, 112)]), TKB, 'f'),
   L(outline([(8, 50), (12, 20), (30, 4), (50, 0), (70, 4), (88, 20), (92, 50), (50, 44)]), TKO, 'f'),
   L(outline([(26, 26), (50, 10), (74, 26), (68, 30), (50, 18), (32, 30)]), TKC, 'f', False), L(outline([(44, 30), (56, 30), (54, 44), (46, 44)]), TKC, 'f', False),
   L(ell(32, 66, 9, 9), TKC, 'f', False), L(ell(68, 66, 9, 9), TKC, 'f', False), L(ell(32, 66, 7, 7), BLACK, 'f', False), L(ell(68, 66, 7, 7), BLACK, 'f', False),
   L(outline([(20, 82), (80, 82), (78, 100), (22, 100)]), _c('#7a2a10'), 'f', False),
   L(outline([(20, 82), (26, 90, 1), (32, 82), (38, 90, 1), (44, 82), (50, 90, 1), (56, 82), (62, 90, 1), (68, 82), (74, 90, 1), (80, 82)]), TKC, 'f', False),
   L(outline([(22, 100), (28, 92, 1), (34, 100), (40, 92, 1), (46, 100), (52, 92, 1), (58, 100), (64, 92, 1), (70, 100), (76, 92, 1), (78, 100)]), TKC, 'f', False)],
  [L(outline([(36, 22), (44, 6), (40, -12, 1), (30, 8), (26, 20)]), TKC, 'b'),
   L(outline([(4, 100), (2, 50), (10, 18), (40, 0), (70, 4), (90, 22), (98, 50), (96, 106), (60, 112)]), TKB, 'f'),
   L(outline([(4, 50), (10, 18), (40, 0), (70, 4), (90, 22), (96, 50), (60, 44)]), TKO, 'f'),
   L(ell(84, 66, 6, 8), BLACK, 'f', False), L(outline([(74, 82), (98, 82), (98, 100), (74, 100)]), _c('#7a2a10'), 'f', False),
   L(outline([(74, 82), (80, 90, 1), (86, 82), (92, 90, 1), (98, 82)]), TKC, 'f', False)],
  _thorn(-1) + _thorn(1) + [L(outline([(8, 106), (6, 50), (12, 20), (30, 4), (50, 0), (70, 4), (88, 20), (94, 50), (92, 106), (50, 112)]), TKO, 'f'),
   L(outline([(26, 26), (50, 10), (74, 26), (68, 30), (50, 18), (32, 30)]), TKC, 'f', False), L([(8, 60), (92, 60)], TKB, 'f', False, False, 3.0)])

# Niall Kuhn: gorro ninja negro con una placa de metal gris en la frente sobre una cinta crema; asoman pinchos rubios por
# los lados y dos mechones negros largos que le caen junto a la cara; tirita en la nariz, ojos verde grisáceo y boca seria
NJ, PLATE, NBAND = _c('#393837'), _c('#7f8a84'), _c('#e8dcc0')
C('niall-kunai-kuhn', 'normal', P('#d8b050', '#e9caa3', iris='#5a7a6a'),
  F(eyes='normal', brows=False, mouth='frown', mouth_y=94, hairline=False),
  [L(outline([(14, 70), (-4, 62, 1), (8, 56), (-2, 46, 1), (14, 46)])), L(outline([(86, 70), (104, 62, 1), (92, 56), (102, 46, 1), (86, 46)])),
   L(outline([(8, 58), (8, 26), (24, 6), (50, -2), (76, 6), (92, 26), (92, 58), (50, 54)]), NJ, 'f'),
   L(outline([(8, 48), (50, 42), (92, 48), (92, 60), (50, 56), (8, 60)]), NBAND, 'f'),
   L(outline([(20, 46), (50, 40), (80, 46), (80, 64), (50, 60), (20, 64)]), PLATE, 'f'),
   L(ell(26, 54, 1.2, 1.2), _c('#4a5450'), 'f', False), L(ell(74, 54, 1.2, 1.2), _c('#4a5450'), 'f', False),
   L(outline([(18, 62), (24, 62), (22, 100), (18, 112, 1), (14, 100)]), NJ, 'f'), L(outline([(82, 62), (76, 62), (78, 100), (82, 112, 1), (86, 100)]), NJ, 'f'),
   L(outline([(42, 82), (58, 82), (58, 87), (42, 87)]), _c('#e8c8b0'), 'f')],
  [L(outline([(54, 64), (40, 58), (26, 70, 1), (30, 56), (14, 60, 1), (22, 48), (54, 50)])),
   L(outline([(4, 64), (4, 26), (24, 4), (52, -2), (78, 6), (92, 28), (92, 48), (54, 52), (30, 62)]), NJ, 'f'),
   L(outline([(4, 54), (50, 42), (94, 46), (94, 58), (50, 56), (4, 66)]), NBAND, 'f'), L(outline([(62, 44), (94, 42), (94, 60), (62, 60)]), PLATE, 'f'),
   L(outline([(50, 58), (56, 58), (54, 100), (50, 110, 1), (46, 98)]), NJ, 'f')],
  [L(outline([(14, 74), (-4, 66, 1), (8, 60), (-2, 50, 1), (14, 50)])), L(outline([(86, 74), (104, 66, 1), (92, 60), (102, 50, 1), (86, 50)])),
   L(outline([(8, 80), (8, 26), (24, 6), (50, -2), (76, 6), (92, 26), (92, 80), (50, 86)]), NJ, 'f'),
   L(outline([(8, 50), (50, 44), (92, 50), (92, 62), (50, 58), (8, 62)]), NBAND, 'f'), L(outline([(44, 56), (56, 56), (60, 76), (50, 72), (40, 76)]), NBAND, 'f')])

# Nick Pincher: pañuelo pardo atado a la cabeza con el nudo a un lado y una luna dorada; melena verde agua lisa por los
# lados con una trenza; un pañuelo negro le tapa la nariz y la boca; ojos morados
BAND3, MOON, TEALH = _c('#453f35'), _c('#e8d870'), _c('#3aa89a')
C('nick-thief-pincher', 'normal', P('#3aa89a', '#f0c8a0', iris='#8a4a9a'),
  F(eyes='normal', brows=False, mouth='none', hairline=False),
  [L(outline([(10, 110), (8, 70), (14, 56), (86, 56), (92, 70), (90, 110), (80, 96), (78, 64), (22, 64), (20, 96)])),
   L(outline([(90, 90), (96, 104), (98, 118), (104, 124, 1), (94, 122), (90, 106)])),
   L(outline([(8, 66), (6, 30), (20, 8), (50, 0), (80, 8), (94, 30), (94, 66), (50, 62)]), BAND3, 'f'),
   L(outline([(8, 46), (-12, 30), (-16, 52, 1), (-2, 52), (-14, 70, 1), (8, 58)]), BAND3, 'f'),
   L(outline([(72, 40), (80, 48), (82, 60), (76, 70), (84, 66), (88, 54), (84, 42)]), MOON, 'f'),
   L([(10, 30), (90, 50)], _c('#2a2620'), 'f', False, False, 1.2),
   L(outline([(14, 84), (50, 80), (86, 84), (84, 102), (66, 110), (50, 112), (34, 110), (16, 102)]), BLACK, 'f')],
  [L(outline([(54, 64), (40, 72), (36, 112), (12, 112), (4, 80), (6, 56), (60, 56)])),
   L(outline([(2, 70), (2, 30), (18, 6), (50, 0), (80, 8), (94, 30), (94, 60), (60, 62), (30, 70)]), BAND3, 'f'),
   L(outline([(62, 82), (94, 80), (94, 102), (80, 110), (62, 106)]), BLACK, 'f')],
  [L(outline([(8, 112), (6, 60), (94, 60), (92, 112), (70, 118, 1), (50, 114), (30, 118, 1)])),
   L(outline([(74, 104), (80, 118), (86, 126, 1), (76, 124), (70, 110)])),
   L(outline([(6, 70), (6, 30), (20, 8), (50, 0), (80, 8), (94, 30), (94, 70), (50, 66)]), BAND3, 'f'),
   L(outline([(90, 44), (110, 30), (114, 52, 1), (100, 52), (112, 70, 1), (90, 58)]), BAND3, 'f')])

# Nifty Throttler: casco de motocross verde y crema con la visera levantada a rayas negras y blancas, ojos amarillos
# afilados y una mentonera crema que le tapa la boca
MOTO, MOTOC = _c('#2aa878'), _c('#ece4c4')
def _moto(view):
    if view == 'front':
        return [L(outline([(4, 100), (2, 50), (10, 20), (30, 4), (50, 0), (70, 4), (90, 20), (98, 50), (96, 100), (82, 100), (82, 64), (18, 64), (18, 100)]), MOTO, 'f'),
                L(outline([(40, 2), (60, 2), (60, 30), (40, 30)]), MOTOC, 'f', False), L(outline([(16, 22), (26, 12), (30, 30), (18, 34)]), MOTOC, 'f', False),
                L(outline([(84, 22), (74, 12), (70, 30), (82, 34)]), MOTOC, 'f', False),
                L(outline([(4, 54), (12, 34), (50, 28), (88, 34), (96, 54), (88, 62), (50, 58), (12, 62)]), BLACK, 'f'),
                L(outline([(24, 34), (32, 33), (32, 59), (24, 60)]), WHITE, 'f', False), L(outline([(44, 31), (52, 31), (52, 58), (44, 58)]), WHITE, 'f', False),
                L(outline([(64, 33), (72, 34), (72, 60), (64, 59)]), WHITE, 'f', False),
                L(outline([(20, 86), (50, 82), (80, 86), (82, 104), (66, 114), (50, 116), (34, 114), (18, 104)]), MOTOC, 'f')]
    if view == 'side':
        return [L(outline([(2, 104), (0, 50), (10, 18), (40, 0), (70, 4), (90, 20), (98, 46), (96, 60), (60, 62), (56, 104), (30, 110)]), MOTO, 'f'),
                L(outline([(36, 2), (54, 4), (40, 60), (26, 58)]), MOTOC, 'f', False),
                L(outline([(60, 46), (96, 30), (108, 46), (96, 60)]), BLACK, 'f'), L(outline([(76, 40), (82, 37), (84, 54), (78, 56)]), WHITE, 'f', False),
                L(outline([(60, 84), (96, 82), (98, 102), (84, 114), (60, 108)]), MOTOC, 'f')]
    return [L(outline([(4, 104), (2, 50), (10, 20), (30, 4), (50, 0), (70, 4), (90, 20), (98, 50), (96, 104), (50, 112)]), MOTO, 'f'),
            L(outline([(40, 2), (60, 2), (60, 110), (40, 110)]), MOTOC, 'f', False)]
C('nifty-trials-throttler', 'normal', P('#2aa878', '#f0c8a0', iris='#d8c020'),
  F(eyes='sharp', brows='angry', mouth='none', hairline=False, ears=False), _moto('front'), _moto('side'), _moto('back'))

# Noel Taurius: hombre toro; pelo castaño oscuro en greñas con dos cuernos naranjas curvos y una coleta detrás; cara enorme
# de piel gris parda, ojos rojos furiosos y los dientes apretados
HRN = _c('#d8603a')
def _bull(s, y=26):
    x = 50 + s * 34
    return [L(outline([(x, y + 8), (x + s * 20, y), (x + s * 22, y - 22, 1), (x + s * 10, y - 6), (x - s * 4, y)]), HRN, 'b')]
C('noel-taurius', 'corpulento', P('#3a2a1e', '#9a8070', iris='#d82020'),
  F(eyes='sharp', brows='angry', mouth='none', face_front=face(w=8, chin=108, jaw=8, top=22), face_side=face_side(chin=8, jaw=8), nose=(50, 84, 3),
    hairline=[(6, 62), (16, 50), (28, 56), (36, 46), (46, 54), (54, 44), (64, 54), (74, 46), (84, 52), (94, 62)]),
  _bull(-1) + _bull(1) + dome('front', top=10, w=48, cy=46, n=7, amp=8, seed=46, sb=60) + teeth(97, 14, 7),
  dome('side', top=10, w=46, cy=46, n=7, amp=8, seed=46, nape=80, fr=46) + [L(outline([(52, 26), (66, 16), (70, -4, 1), (60, 12), (46, 18)]), HRN, 'b'),
   L(outline([(10, 56), (-6, 70), (-8, 90, 1), (2, 74), (14, 66)])), L(outline([(80, 92), (90, 92), (89, 100), (80, 100)]), WHITE, 'f', True)],
  _bull(-1) + _bull(1) + dome('back', top=10, w=48, cy=46, n=7, amp=8, seed=46, nape=80) + [L(outline([(44, 74), (56, 74), (60, 96), (52, 108, 1), (40, 96)]))])

# Norman Zeus: cabeza de cerdo; calvo, con un cuerno blanco y negro en la frente y patillas naranjas en mechones; ojos
# blancos brillantes, hocico rosado y dos colmillos
PIG, PIGN, SIDEB = _c('#c89a82'), _c('#e8a898'), _c('#c8801a')
C('norman-nauseous-zeus', 'corpulento', P('#c8801a', '#c89a82', iris='#ffffff'),
  F(eyes='none', brows='angry', mouth='frown', mouth_y=100, hairline=False, face_front=face(w=8, chin=108, jaw=6, top=10), face_side=face_side(chin=8, jaw=6), big_ears=3, ear_out=6),
  [L(outline([(10, 60), (6, 76), (8, 96), (16, 104), (20, 80), (18, 62)]), SIDEB, 'f'), L(outline([(90, 60), (94, 76), (92, 96), (84, 104), (80, 80), (82, 62)]), SIDEB, 'f'),
   L(outline([(46, 50), (50, 32, 1), (54, 50)]), WHITE, 'f'), L(outline([(50, 34), (54, 50), (50, 50)]), BLACK, 'f', False),
   L(ell(36, 70, 6, 4.4), WHITE, 'f', True), L(ell(64, 70, 6, 4.4), WHITE, 'f', True),
   L([(28, 62), (42, 66)], OUTC, 'f', False, False, 2.4), L([(72, 62), (58, 66)], OUTC, 'f', False, False, 2.4),
   L(ell(50, 86, 11, 7), PIGN, 'f'), L(ell(46, 86, 1.6, 2.4), _c('#5a3a30'), 'f', False), L(ell(54, 86, 1.6, 2.4), _c('#5a3a30'), 'f', False),
   L(outline([(34, 102), (38, 102), (36, 96, 1)]), WHITE, 'f'), L(outline([(62, 102), (66, 102), (64, 96, 1)]), WHITE, 'f')],
  [L(outline([(48, 62), (44, 80), (46, 98), (54, 100), (54, 80), (52, 62)]), SIDEB, 'f'),
   L(outline([(70, 44), (78, 30, 1), (78, 46)]), WHITE, 'f'), L(ell(80, 70, 4.6, 4), WHITE, 'f', True),
   L(ell(90, 86, 6, 6), PIGN, 'f'), L(outline([(84, 102), (88, 102), (86, 96, 1)]), WHITE, 'f')],
  [L(outline([(10, 62), (6, 78), (8, 96), (16, 104), (20, 80), (18, 64)]), SIDEB, 'f'), L(outline([(90, 62), (94, 78), (92, 96), (84, 104), (80, 80), (82, 64)]), SIDEB, 'f')])

# Norton Waters: sombrero de pescador color crema y melena azul ondulada que le cae por los lados hasta el pecho; los ojos
# en sombra bajo el ala, piel morena y boca seria
BUCK, BUCKD = _c('#e8dca0'), _c('#c8b878')
C('norton-aquarius-waters', 'delgado', P('#6a8ac8', '#b8906a', iris='#1e1a16', light='#a8c0e8'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=96, hairline=[(6, 66), (14, 58), (50, 60), (86, 58), (94, 66)], face_front=face(chin=106), face_side=face_side(chin=6)),
  [L(outline([(12, 118), (6, 90), (12, 70), (8, 56), (92, 56), (88, 70), (94, 90), (88, 118), (80, 96), (78, 64), (22, 64), (20, 96)])),
   strand([(10, 70), (16, 90), (10, 110)], 'light', 'b', 1.2), strand([(90, 70), (84, 90), (90, 110)], 'light', 'b', 1.2),
   L(outline([(14, 50), (18, 22), (34, 6), (50, 2), (66, 6), (82, 22), (86, 50)]), BUCK, 'f'),
   L(outline([(0, 62), (10, 48), (50, 44), (90, 48), (100, 62), (50, 58)]), BUCKD, 'f'),
   L(outline([(16, 64), (50, 60), (84, 64), (84, 72), (50, 70), (16, 72)]), _c('#6a5040'), 'f', False)],
  [L(outline([(54, 60), (40, 70), (30, 116), (8, 112), (2, 80), (6, 54), (60, 52)])), strand([(10, 70), (16, 90), (10, 108)], 'light', 'b', 1.2),
   L(outline([(10, 50), (14, 20), (34, 4), (56, 2), (76, 10), (86, 30), (88, 50)]), BUCK, 'f'),
   L(outline([(-6, 60), (6, 46), (50, 42), (96, 46), (106, 58), (50, 56)]), BUCKD, 'f')],
  [L(outline([(8, 118), (6, 58), (94, 58), (92, 118), (72, 122, 1), (50, 118), (28, 122, 1)])), strand([(30, 70), (36, 110)], 'light', 'b', 1.2), strand([(70, 70), (64, 110)], 'light', 'b', 1.2),
   L(outline([(14, 50), (18, 22), (34, 6), (50, 2), (66, 6), (82, 22), (86, 50)]), BUCK, 'f'),
   L(outline([(0, 62), (10, 48), (50, 44), (90, 48), (100, 62), (50, 58)]), BUCKD, 'f')])

# Noyss Kensler: casco partido en gris y negro con unos cascos de música encima, gafas amarillas de lentes negras y una
# máscara blanca; nariz redonda naranja y una sonrisa enorme de dientes
GRY, GYL = _c('#9c8f86'), _c('#dbb22e')
def _noyss(view):
    if view == 'front':
        return [L(outline([(10, 56), (10, 30), (24, 10), (50, 4), (76, 10), (90, 30), (90, 56), (50, 52)]), GRY, 'f'),
                L(outline([(50, 4), (76, 10), (90, 30), (90, 56), (50, 52)]), _c('#2b2928'), 'f', False),
                L(quad((8, 60), (50, -16), (92, 60)), BLACK, 'f', False, False, 3.0),
                L(outline([(2, 56), (14, 52), (16, 80), (4, 80)]), GYL, 'f'), L(outline([(98, 56), (86, 52), (84, 80), (96, 80)]), GYL, 'f'),
                L(outline([(14, 60), (50, 54), (86, 60), (84, 82), (50, 86), (16, 82)]), WHITE, 'f')] + goggles(66, BLACK, frame=GYL, sep=17, rx=9, ry=7) + \
               [L(ell(50, 86, 4.4, 4), _c('#f08030'), 'f')]
    if view == 'side':
        return [L(outline([(4, 64), (4, 30), (20, 8), (50, 2), (78, 10), (92, 30), (94, 54), (60, 56), (30, 64)]), GRY, 'f'),
                L(outline([(38, 2), (50, 2), (50, 58), (38, 60)]), _c('#2b2928'), 'f', False),
                L(ell(46, 68, 10, 12), GYL, 'f'), L(outline([(60, 56), (94, 54), (94, 84), (64, 84)]), WHITE, 'f'),
                L(ell(82, 66, 7, 7), GYL, 'f', False), L(ell(82, 66, 5, 5), BLACK, 'f', False), L(ell(92, 86, 4, 4), _c('#f08030'), 'f')]
    return [L(outline([(10, 80), (10, 30), (24, 10), (50, 4), (76, 10), (90, 30), (90, 80), (50, 86)]), GRY, 'f'),
            L(outline([(10, 30), (24, 10), (50, 4), (50, 86), (10, 80)]), _c('#2b2928'), 'f', False),
            L(quad((8, 60), (50, -16), (92, 60)), BLACK, 'f', False, False, 3.0),
            L(outline([(2, 56), (14, 52), (16, 80), (4, 80)]), GYL, 'f'), L(outline([(98, 56), (86, 52), (84, 80), (96, 80)]), GYL, 'f')]
C('noyss-cancell-kensler', 'normal', P('#2b2928', '#e2c8a8', iris='#1e1a16'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _noyss('front') + teeth(96, 13, 7), _noyss('side') + [L(outline([(82, 93), (90, 93), (89, 100), (82, 100)]), WHITE, 'f', True)], _noyss('back'))

# Odo Riffeck: pelo azul turquesa en pinchos largos echados hacia arriba y a un lado, con mechones que le caen a los lados
# de la cara; piel clara, ojos azules afilados y boca seria
C('odo-riffeck', 'delgado', P('#37afcb', '#fbecc2', iris='#2f6a8a', shade='#2f8aa0'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, face_front=face(chin=104), face_side=face_side(chin=4),
    hairline=[(6, 64), (14, 50), (26, 56), (34, 44), (48, 52), (58, 42), (70, 50), (80, 44), (88, 54), (94, 64)]),
  dome('front', top=-6, w=46, cy=42, n=8, amp=18, sweep=0.7, seed=50, sb=68) +
  [L(outline([(14, 50), (20, 40), (18, 70), (14, 88, 1), (10, 70)]), 'mid', 'f'), L(outline([(86, 50), (80, 40), (82, 70), (88, 90, 1), (90, 70)]), 'mid', 'f')],
  dome('side', top=-6, w=46, cy=42, n=8, amp=18, sweep=0.7, seed=50, nape=86, fr=48),
  dome('back', top=-6, w=46, cy=42, n=8, amp=18, sweep=0.7, seed=50, nape=86))

# Olaf Nobeard: casco vikingo pardo con tiras de metal gris remachadas, protector de nariz y dos cuernos blancos; melena
# castaña lisa hasta la barbilla, gafas cuadradas negras, coloretes y boca seria
VH, VM, VHORN = _c('#7f644b'), _c('#bec1bf'), _c('#f4ead8')
def _viking(view):
    if view == 'front':
        return [L(outline([(16, 40), (6, 26), (2, 4, 1), (12, 20), (22, 30)]), VHORN, 'b'), L(outline([(84, 40), (94, 26), (98, 4, 1), (88, 20), (78, 30)]), VHORN, 'b'),
                L(outline([(12, 56), (12, 30), (26, 10), (50, 2), (74, 10), (88, 30), (88, 56), (50, 52)]), VH, 'f'),
                L(outline([(44, 4), (56, 4), (56, 50), (44, 50)]), VM, 'f', False),
                L(outline([(10, 48), (50, 44), (90, 48), (90, 60), (50, 56), (10, 60)]), VM, 'f'),
                L(outline([(46, 56), (54, 56), (53, 80), (47, 80)]), VM, 'f'),
                L(ell(50, 14, 1.4, 1.4), _c('#8a8a8a'), 'f', False), L(ell(50, 32, 1.4, 1.4), _c('#8a8a8a'), 'f', False)]
    if view == 'side':
        return [L(outline([(40, 26), (50, 12), (54, -10, 1), (58, 16), (52, 30)]), VHORN, 'b'),
                L(outline([(6, 60), (6, 30), (20, 8), (50, 2), (78, 10), (92, 30), (94, 52), (60, 54), (30, 62)]), VH, 'f'),
                L(outline([(4, 52), (50, 44), (94, 44), (94, 56), (50, 56), (4, 64)]), VM, 'f'), L(outline([(88, 54), (94, 54), (95, 76), (90, 76)]), VM, 'f')]
    return [L(outline([(16, 40), (6, 26), (2, 4, 1), (12, 20), (22, 30)]), VHORN, 'b'), L(outline([(84, 40), (94, 26), (98, 4, 1), (88, 20), (78, 30)]), VHORN, 'b'),
            L(outline([(12, 58), (12, 30), (26, 10), (50, 2), (74, 10), (88, 30), (88, 58), (50, 54)]), VH, 'f'),
            L(outline([(44, 4), (56, 4), (56, 52), (44, 52)]), VM, 'f', False), L(outline([(10, 50), (50, 46), (90, 50), (90, 62), (50, 58), (10, 62)]), VM, 'f')]
C('olaf-nobeard', 'normal', P('#7f644b', '#fbc172', iris='#1e1a16'),
  F(eyes='dot', brows=False, mouth='line', mouth_y=94, glasses=BLACK, glasses_rect=True, hairline=False),
  [L(outline([(14, 104), (10, 70), (14, 56), (86, 56), (90, 70), (86, 104), (78, 92), (78, 64), (22, 64), (22, 92)]))] + _viking('front') +
  [L(ell(26, 86, 5, 3), _c('#f0a090'), 'f', False), L(ell(74, 86, 5, 3), _c('#f0a090'), 'f', False)],
  [L(outline([(54, 62), (42, 72), (38, 102), (14, 100), (4, 74), (6, 56), (60, 54)]))] + _viking('side'),
  [L(outline([(10, 104), (6, 60), (94, 60), (90, 104), (50, 108)]))] + _viking('back'))

# Olivia Palme (chica): un afro enorme castaño oscuro de rizos con una cinta amarilla atada en lazo encima; piel morena,
# ojos rosados y labios gruesos
YB = _c('#e9c157')
C('olivia-palme', 'chica', P('#3e2d28', '#b97632', iris='#c87090', shade='#2a1e1a'),
  F(eyes='sharp', brows='angry', mouth='lips', mouth_w=5, mouth_y=95, hairline=[(6, 62), (14, 50), (30, 44), (50, 42), (70, 44), (86, 50), (94, 62)]),
  dome('front', top=-8, w=58, cy=46, n=14, amp=7, soft=True, seed=52, long=96, flare=10) +
  [L(quad((14, 44), (50, 16), (86, 44)), YB, 'f', False, False, 6.0),
   L(outline([(54, 20), (66, 4), (78, 4), (70, 18)]), YB, 'f'), L(outline([(54, 22), (74, 22), (86, 14), (80, 30), (64, 28)]), YB, 'f')],
  dome('side', top=-8, w=56, cy=46, n=14, amp=7, soft=True, seed=52, long=96, flare=10, fr=46) + [L(quad((12, 36), (50, 8), (90, 40)), YB, 'f', False, False, 6.0)],
  dome('back', top=-8, w=58, cy=46, n=14, amp=7, soft=True, seed=52, long=96, flare=10, ends=5) + [L(quad((10, 40), (50, 14), (90, 40)), YB, 'f', False, False, 6.0)])

# Onslow Mastick: pelo rosa en nube con dos picos como orejas de gato y un copete abultado en medio, con brillos claros;
# cejas rosas fruncidas, nariz redonda naranja y boca seria
C('onslow-mastick', 'normal', P('#c64574', '#fabb7c', iris='#1e1a16', light='#e888a8', brow='#c64574'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=95, nose=(50, 86, 3.4), hairline=[(6, 62), (14, 52), (28, 56), (40, 48), (50, 58), (60, 48), (72, 56), (86, 52), (94, 62)]),
  [L(outline([(6, 66), (2, 30), (0, -4, 1), (20, 6), (40, 2), (50, 6), (60, 2), (80, 6), (100, -4, 1), (98, 30), (94, 66), (80, 56), (20, 56)])),
   L(ell(50, 30, 16, 16)), L(ell(44, 24, 4, 3), 'light', 'f', False), L(ell(18, 20, 4, 3), 'light', 'b', False), L(ell(80, 24, 4, 3), 'light', 'b', False),
   L(outline([(58, 4), (80, 6), (100, -4), (98, 30), (94, 62), (80, 40)]), 'shade', 'b', False)],
  [L(outline([(54, 60), (62, 46), (84, 42), (96, 24), (90, 0, 1), (70, 6), (48, 2), (30, 6), (8, -4, 1), (4, 30), (6, 60), (22, 74), (40, 72), (48, 64)])),
   L(ell(60, 22, 14, 14)), L(ell(56, 18, 4, 3), 'light', 'f', False)],
  [L(outline([(6, 76), (2, 30), (0, -4, 1), (20, 6), (50, 2), (80, 6), (100, -4, 1), (98, 30), (94, 76), (50, 84)])),
   L(outline([(58, 4), (80, 6), (100, -4), (98, 30), (94, 74), (70, 80)]), 'shade', 'b', False)])

# Orion Tearing: capucha amarilla que le tapa la cabeza y cae por los hombros, con dos orejeras redondas a los lados; un
# antifaz negro con los ojos blancos le tapa la parte de arriba de la cara; sonrisa enorme de dientes
HOODY, HOODYD, EARM = _c('#fdd903'), _c('#c18c0d'), _c('#e8dcc8')
C('orion-bearings-tearing', 'normal', P('#fdd903', '#f9c172', iris='#1e1a16'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  [L(ell(8, 72, 9, 12), EARM, 'b'), L(ell(92, 72, 9, 12), EARM, 'b'),
   L(outline([(4, 120), (6, 60), (14, 26), (32, 6), (50, 0), (68, 6), (86, 26), (94, 60), (96, 120), (78, 112), (82, 80), (76, 60), (64, 48), (50, 44), (36, 48), (24, 60),
              (18, 80), (22, 112)]), HOODY, 'f'),
   L(outline([(22, 112), (18, 80), (24, 60), (30, 104), (50, 116, 1), (70, 104), (76, 60), (82, 80), (78, 112), (50, 124, 1)]), HOODY, 'f'),
   L(outline([(24, 62), (36, 50), (50, 46), (64, 50), (76, 62), (78, 78), (50, 82), (22, 78)]), BLACK, 'f'),
   L(outline([(28, 66), (40, 64), (44, 72), (32, 74)]), WHITE, 'f', False), L(outline([(72, 66), (60, 64), (56, 72), (68, 74)]), WHITE, 'f', False)] + teeth(95, 14, 8),
  [L(ell(42, 70, 9, 12), EARM, 'f'),
   L(outline([(60, 50), (40, 60), (30, 120), (4, 118), (0, 60), (10, 22), (34, 2), (64, 4), (86, 20), (94, 40), (80, 46)]), HOODY, 'f'),
   L(outline([(66, 54), (90, 52), (94, 78), (70, 80)]), BLACK, 'f'), L(outline([(78, 64), (90, 62), (90, 72), (80, 72)]), WHITE, 'f', False),
   L(outline([(80, 92), (92, 92), (90, 100), (80, 100)]), WHITE, 'f', True)],
  [L(ell(8, 72, 9, 12), EARM, 'f'), L(ell(92, 72, 9, 12), EARM, 'f'),
   L(outline([(4, 122), (6, 60), (14, 26), (32, 6), (50, 0), (68, 6), (86, 26), (94, 60), (96, 122), (50, 130, 1)]), HOODY, 'f'),
   L(outline([(40, 20), (50, 10), (60, 20), (56, 90), (44, 90)]), HOODYD, 'f', False)])

# Oz Tier: afro castaño oscuro de rizos, ojos rojos furiosos, piel tostada y boca seria
C('oz-tier', 'normal', P('#4a3924', '#eca764', iris='#c82020', shade='#35261d'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=hl(6, 64, 48, 56, jit=2, seed=55)),
  dome('front', top=-6, w=52, cy=44, n=14, amp=6, soft=True, seed=55, sb=72),
  dome('side', top=-6, w=50, cy=44, n=14, amp=6, soft=True, seed=55, nape=88, fr=52),
  dome('back', top=-6, w=52, cy=44, n=14, amp=6, soft=True, seed=55, nape=88))

# Pacey Mack (portera, chica): pelo turquesa con un flequillo largo echado a un lado y una diadema con dos tornillos grises
# a modo de antenas; ojos azules, coloretes redondos y sonrisa ondulada
BOLT = _c('#8e8e7a')
C('pacey-tinker-mack', 'chica', P('#6ac5bf', '#fbe5b3', iris='#3a7ab0', shade='#4d7976'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=93, hairline=[(6, 66), (16, 52), (30, 44), (46, 44), (62, 52), (74, 62), (84, 70), (94, 66)]),
  dome('front', top=2, w=48, cy=46, long=96, flare=4) +
  [L(outline([(20, 40), (46, 30), (72, 40), (90, 60), (94, 86), (86, 92), (80, 74), (68, 58), (50, 50), (34, 50), (22, 54)]), 'mid', 'f'),
   L(quad((10, 34), (50, 6), (90, 34)), BOLT, 'f', False, False, 3.4),
   L(outline([(14, 26), (18, 10), (26, 10), (26, 26)]), BOLT, 'f'), L(outline([(86, 26), (82, 10), (74, 10), (74, 26)]), BOLT, 'f'),
   L(ell(28, 86, 5, 5), _c('#f0a8a0'), 'f', False), L(ell(72, 86, 5, 5), _c('#f0a8a0'), 'f', False)],
  dome('side', top=2, w=48, cy=46, long=96, flare=4, fr=56) + [L(quad((10, 26), (50, 2), (90, 30)), BOLT, 'f', False, False, 3.4), L(outline([(46, 4), (50, -10), (58, -10), (58, 4)]), BOLT, 'f')],
  dome('back', top=2, w=48, cy=46, long=96, flare=4, ends=4) + [L(quad((8, 32), (50, 6), (92, 32)), BOLT, 'f', False, False, 3.4),
   L(outline([(14, 26), (18, 10), (26, 10), (26, 26)]), BOLT, 'f'), L(outline([(86, 26), (82, 10), (74, 10), (74, 26)]), BOLT, 'f')])

# Paddy Filler: pelo castaño con los lados rapados y un tupé alto echado hacia un lado; cara larga y pálida, ojos
# redondos de susto con ojeras y boca torcida
C('paddy-filler', 'delgado', P('#766d5f', '#fdf0d6', iris='#1e1a16', shade='#594a40'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=97, face_front=face(w=-2, chin=110), face_side=face_side(chin=10),
    hairline=[(6, 60), (14, 44), (30, 40), (50, 42), (70, 40), (86, 44), (94, 60)]),
  [L(outline([(14, 56), (14, 34), (86, 34), (86, 56), (80, 44), (20, 44)]), 'shade'),
   L(outline([(24, 40), (20, 18), (8, -6, 1), (32, 4), (40, -16, 1), (52, 2), (66, -10, 1), (68, 10), (78, 20), (76, 40)])),
   L(quad((29, 82), (36, 87), (43, 82)), _c('#a89880'), 'f', False, False, 1.4), L(quad((57, 82), (64, 87), (71, 82)), _c('#a89880'), 'f', False, False, 1.4)],
  [L(outline([(54, 54), (60, 40), (80, 36), (90, 24), (70, 16), (60, -12, 1), (46, 4), (24, -6, 1), (24, 14), (8, 28), (6, 54), (24, 64), (44, 60)]), 'shade'),
   L(outline([(30, 30), (24, 12), (24, -6, 1), (46, 4), (60, -12, 1), (68, 14), (84, 24), (70, 34)]))],
  [L(outline([(14, 70), (12, 34), (88, 34), (86, 70), (50, 76)]), 'shade'),
   L(outline([(28, 36), (24, 18), (14, -4, 1), (34, 4), (44, -14, 1), (54, 2), (66, -10, 1), (70, 10), (76, 22), (72, 36)]))])

# Pann Kidd: melena gris lisa hasta el cuello con flequillo y dos cuernecillos de cabra; una perilla gris larga en punta,
# párpados caídos, cejas grises enormes y boca pequeña; cara alargada
GOAT = _c('#cec4ba')
C('pann-capric-n-kidd', 'delgado', P('#cec4ba', '#fdeab8', iris='#3a2a20', shade='#978178', brow='#a89a8a'),
  F(eyes='sharp', brows=True, mouth='frown', mouth_y=94, face_front=face(chin=106), face_side=face_side(chin=6), big_ears=2, ear_out=2,
    hairline=[(6, 66), (12, 60), (88, 60), (94, 66)]),
  dome('front', top=2, w=46, cy=44, long=100, flare=4) +
  [L(outline([(12, 60), (14, 36), (30, 24), (50, 22), (70, 24), (86, 36), (88, 60), (76, 58), (64, 62), (50, 58), (36, 62), (24, 58)]), 'mid', 'f'),
   L(outline([(22, 16), (14, 4), (16, -6, 1), (24, 6), (28, 14)]), _c('#6a4a30'), 'b'), L(outline([(78, 16), (86, 4), (84, -6, 1), (76, 6), (72, 14)]), _c('#6a4a30'), 'b'),
   L(outline([(36, 98), (50, 100), (64, 98), (58, 108), (50, 120, 1), (42, 108)]), GOAT, 'f'),
   L(outline([(26, 70), (34, 66), (44, 70), (36, 72)]), _c('#c8bca8'), 'f', False), L(outline([(74, 70), (66, 66), (56, 70), (64, 72)]), _c('#c8bca8'), 'f', False)],
  dome('side', top=2, w=46, cy=44, long=100, flare=4, fr=58) + [L(outline([(58, 16), (66, 2), (64, -8, 1), (56, 6), (52, 14)]), _c('#6a4a30'), 'b'),
   L(outline([(76, 98), (88, 98), (86, 110), (82, 120, 1), (76, 108)]), GOAT, 'f')],
  dome('back', top=2, w=46, cy=44, long=100, flare=4, ends=4) +
  [L(outline([(22, 16), (14, 4), (16, -6, 1), (24, 6), (28, 14)]), _c('#6a4a30'), 'b'), L(outline([(78, 16), (86, 4), (84, -6, 1), (76, 6), (72, 14)]), _c('#6a4a30'), 'b')])

# Pasha Lomo: melena negra lisa en casco con flequillo, que por los lados se abre en mechones finos y ondulados; ojos con
# raya negra gruesa y una sonrisa enorme de dientes; cara alargada y pálida
C('pasha-lomo', 'delgado', P('#2b1f2f', '#f0e5d2', iris='#1e1a16', shade='#1e161f'),
  F(eyes='sharp', brows=False, mouth='none', face_front=face(chin=108), face_side=face_side(chin=8),
    hairline=[(6, 66), (12, 64), (88, 64), (94, 66)]),
  dome('front', top=0, w=44, cy=44, sb=66) +
  [L(outline([(12, 64), (14, 36), (30, 24), (50, 22), (70, 24), (86, 36), (88, 64), (70, 62), (50, 60), (30, 62)]), 'mid', 'f'),
   L(outline([(10, 66), (2, 84), (6, 98), (-2, 116, 1), (10, 100), (8, 86), (16, 72)]), 'mid', 'f'),
   L(outline([(90, 66), (98, 84), (94, 98), (102, 116, 1), (90, 100), (92, 86), (84, 72)]), 'mid', 'f'),
   L([(24, 70), (46, 72)], OUTC, 'f', False, False, 3.0), L([(76, 70), (54, 72)], OUTC, 'f', False, False, 3.0)] + teeth(95, 14, 8),
  dome('side', top=0, w=44, cy=44, nape=84, fr=62) + [L(outline([(44, 66), (36, 84), (40, 98), (32, 116, 1), (44, 100), (42, 86), (50, 72)]), 'mid', 'f'),
   L(outline([(80, 92), (92, 92), (90, 100), (80, 100)]), WHITE, 'f', True)],
  dome('back', top=0, w=44, cy=44, nape=84) + [L(outline([(10, 66), (2, 84), (6, 98), (-2, 116, 1), (10, 100), (8, 86), (16, 72)]), 'mid', 'f'),
   L(outline([(90, 66), (98, 84), (94, 98), (102, 116, 1), (90, 100), (92, 86), (84, 72)]), 'mid', 'f')])
