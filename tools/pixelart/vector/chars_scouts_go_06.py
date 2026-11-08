"""Ojeadores de GO (scouts-go), tanda 06: dibujados a partir de su retrato de Victory Road; claves 'scouts-go:<id>'.

Ninguno de la tanda tiene modelo 3D: el frente sale del retrato y el perfil y la espalda se deducen de cómo cae ese
peinado. Usa las ayudas de la tanda 09 de IE1 (dome, hl, face...) sin tocarlas."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from chars_scouts_ie1_09 import BLACK, WHITE, F, P, _c, dome, face, face_side, hl, horn, mark  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401


def C(pid, body, palette, f, front, side, back):
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        # el nacimiento del pelo baja por el borde de la cara hasta la barbilla: así su raya no cruza el pelo de los lados
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[f'scouts-go:{pid}'] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def band(view, c, y=52, h=8, w=48, z='f', dip=4):
    """Cinta alrededor de la cabeza a la altura y."""
    if view == 'front':
        top = quad((50 - w, y + dip), (50, y - dip), (50 + w, y + dip))
        bot = quad((50 + w, y + dip + h), (50, y - dip + h), (50 - w, y + dip + h))
        return L(top + bot, c, z, True, True)
    if view == 'side':
        return L([(2, y + 10), (94, y - 4), (94, y - 4 + h), (2, y + 10 + h)], c, z, True, True)
    top = quad((50 - w, y + dip), (50, y + dip + 2), (50 + w, y + dip))
    bot = quad((50 + w, y + dip + h), (50, y + dip + h + 2), (50 - w, y + dip + h))
    return L(top + bot, c, z, True, True)


def blush(c=_c('#f09a8a')):
    return [L(ell(30, 86, 5, 3), c, 'f', False), L(ell(70, 86, 5, 3), c, 'f', False)]


def mole(x, y):
    return L(ell(x, y, 1.4, 1.4), OUTC, 'f', False)


def lock(pts, c='mid', z='f'):
    return L(outline(pts), c, z)


RED = _c('#c83a2a')
DARK = _c('#2a2228')

# Moe Tivation: pelo verde con el flequillo echado a un lado en mechones de punta, un pelo suelto que se riza hacia
# arriba y los lados más claros; ojos verdes y cara de preocupación
C('moe-tivation', 'normal', P('#647e4a', '#f9bc7d', iris='#6a9a5a', light='#8aa868'),
  F(eyes='normal', brows=True, mouth='frown', mouth_y=93, hairline=[(6, 66), (18, 48), (34, 46), (50, 52), (66, 56), (82, 56), (94, 66)]),
  dome('front', top=4, w=46, cy=46, sb=64) +
  [L(outline([(8, 50), (24, 56), (20, 70, 1), (10, 64)]), 'light'), L(outline([(92, 50), (76, 56), (80, 70, 1), (90, 64)]), 'light'),
   lock([(10, 44), (30, 24), (60, 16), (88, 30), (92, 50), (80, 44), (66, 58, 1), (60, 44), (46, 52, 1), (40, 40), (24, 54, 1)]),
   L(quad((64, 8), (72, -6), (60, -10)), 'mid', 'f', False, False, 2.2)],
  dome('side', top=4, w=46, cy=46, nape=82, fr=50) + [L(quad((52, 6), (60, -8), (48, -12)), 'mid', 'f', False, False, 2.2)],
  dome('back', top=4, w=46, cy=46, nape=82) + [L(quad((60, 8), (68, -6), (56, -10)), 'mid', 'b', False, False, 2.2)])

# Mollie Cular: melena granate lisa y larga con raya en medio, piel muy clara, gafas redondas finas de montura dorada en la
# punta de la nariz, un lunar sobre la ceja y sonrisa
C('mollie-cular', 'chica', P('#653145', '#fdeab8', iris='#8a6a3a'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=94, glasses=_c('#b89a5a'),
    hairline=[(6, 76), (16, 56), (30, 44), (48, 40), (52, 44), (68, 42), (84, 56), (94, 76)]),
  dome('front', top=2, w=46, cy=46, long=104, flare=4) + [mole(64, 62), L([(46, 40), (40, 20)], 'shade', 'f', False, False, 1.0)],
  dome('side', top=2, w=46, cy=46, long=104, flare=4, fr=56),
  dome('back', top=2, w=46, cy=46, long=104, flare=4, ends=4))

# Molly Gunn: pelo morado oscuro recogido en un tupé alto con una coleta gruesa que le cae por un lado hasta el pecho y el
# otro lado rapado; piel morena, ojos rojos afilados y la boca abierta de enfado
PLR = _c('#7a5a80')
C('molly-gunn', 'chica', P('#4f2f54', '#eca663', iris='#c8304a', light='#6a4a70'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 62), (16, 46), (30, 38), (50, 36), (70, 40), (84, 48), (94, 62)]),
  [L(outline([(80, 50), (90, 46), (92, 70), (84, 72)]), PLR)] +
  dome('front', top=-4, w=44, cy=40, sb=56) +
  [L(outline([(8, 46), (2, 70), (-2, 100), (8, 118, 1), (14, 96), (20, 74), (24, 52)])),
   L(outline([(30, 6), (50, -8), (72, 2), (60, 14), (40, 14)]), 'light', 'b', False),
   L([(70, 60), (74, 76)], 'deep', 'f', False, False, 1.4)],
  dome('side', top=-4, w=44, cy=40, nape=70, fr=44) + [L(outline([(14, 50), (4, 80), (6, 112, 1), (20, 92), (26, 62)]))],
  dome('back', top=-4, w=44, cy=40, nape=72) + [L(outline([(88, 46), (98, 74), (94, 112, 1), (84, 90), (78, 58)]))])

# Montana Fleetfoot: media melena azul marino con dos moños bajos a los lados de la barbilla y una horquilla crema; cejas
# gruesas, pecas y coloretes
CRM = _c('#e8d8a8')
C('montana-fleetfoot', 'chica', P('#3a475a', '#f9d0a1', iris='#3a4a7a'),
  F(eyes='normal', brows=True, mouth='frown', mouth_y=94, hairline=[(6, 70), (18, 50), (34, 44), (50, 48), (66, 44), (82, 50), (94, 70)]),
  dome('front', top=2, w=46, cy=46, long=86, flare=2) +
  [L(ell(14, 90, 8, 7)), L(ell(86, 90, 8, 7)), L(outline([(66, 26), (82, 18), (84, 24), (68, 32)]), CRM, 'f')] + blush() +
  [L(ell(34, 84, 0.8, 0.8), _c('#b06a4a'), 'f', False), L(ell(66, 84, 0.8, 0.8), _c('#b06a4a'), 'f', False)],
  dome('side', top=2, w=46, cy=46, long=84, flare=2, fr=54) + [L(ell(36, 90, 8, 7))],
  dome('back', top=2, w=46, cy=46, long=84, flare=2, ends=0) + [L(ell(14, 90, 8, 7)), L(ell(86, 90, 8, 7))])

# Monty Montague (portero): casco morado con dos cuernos curvos a los lados que le baja en pico hasta la nariz; piel oscura,
# dos rayas granates bajando de los ojos y ojos pequeños redondos
HMP, MAR = _c('#6f5b80'), _c('#7a1e2c')
def _horned(view):
    if view == 'front':
        return [L(outline([(6, 46), (-12, 58), (-8, 86, 1), (2, 70), (16, 62)]), HMP), L(outline([(94, 46), (112, 58), (108, 86, 1), (98, 70), (84, 62)]), HMP),
                L(outline([(6, 64), (4, 30), (22, 8), (50, 0), (78, 8), (96, 30), (94, 64), (70, 62), (50, 84, 1), (30, 62)]), HMP),
                L(outline([(14, 50), (16, 64), (30, 67), (44, 69), (50, 84, 1), (56, 69), (70, 67), (84, 64), (86, 50)]), HMP, 'f'),
                L(outline([(50, 4), (52, 4), (51, 80), (49, 80)]), _c('#5a4868'), 'f', False)]
    if view == 'side':
        return [L(outline([(6, 74), (2, 40), (20, 8), (50, 0), (80, 12), (94, 36), (96, 62), (88, 64), (70, 58), (54, 62), (40, 76)]), HMP),
                L(outline([(30, 50), (14, 70), (22, 92, 1), (34, 64)]), HMP)]
    return [L(outline([(-4, 56), (0, 84, 1), (14, 70)]), HMP), L(outline([(104, 56), (100, 84, 1), (86, 70)]), HMP),
            L(outline([(6, 80), (4, 30), (22, 8), (50, 0), (78, 8), (96, 30), (94, 80), (50, 88)]), HMP)]
C('monty-montague', 'corpulento', P('#3a2a2a', '#be8b68'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=95, hairline=False, face_front=face(w=4, chin=102, jaw=4)),
  _horned('front') + [L(outline([(24, 78), (30, 78), (34, 100), (28, 100)]), MAR, 'f', False), L(outline([(70, 78), (76, 78), (72, 100), (66, 100)]), MAR, 'f', False)],
  _horned('side') + [L(outline([(78, 78), (84, 78), (82, 98), (76, 98)]), MAR, 'f', False)],
  _horned('back'))

# Moonir Stone: casco blanco redondo como una luna, con una espiral color arena encima, que le tapa la cabeza hasta las
# mejillas; cara plana muy clara, ojos de párpado caído y una sonrisa recta
WH, SND = _c('#ecece6'), _c('#cbb28e')
def _moon(view):
    if view == 'front':
        return [L(outline([(4, 80), (0, 44), (12, 14), (50, -4), (88, 14), (100, 44), (96, 80), (82, 74), (80, 58), (20, 58), (18, 74)]), WH),
                L(blob([(30, 22), (50, 8), (74, 16), (76, 34), (60, 40), (40, 38), (40, 26), (56, 22), (64, 28), (52, 32)], 6), SND, 'f', False)]
    if view == 'side':
        return [L(outline([(4, 84), (0, 44), (14, 12), (50, -4), (86, 14), (98, 44), (94, 60), (60, 58), (52, 84)]), WH),
                L(blob([(30, 18), (50, 8), (70, 18), (66, 34), (44, 36)], 6), SND, 'f', False)]
    return [L(outline([(4, 84), (0, 44), (12, 14), (50, -4), (88, 14), (100, 44), (96, 84), (50, 92)]), WH),
            L(blob([(34, 26), (50, 14), (70, 22), (66, 40), (44, 42)], 6), SND, 'b', False)]
C('moonir-moonsy-stone', 'normal', P('#988776', '#fde9b6', iris='#5a4a30'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=94, mouth_w=12, hairline=False, big_ears=2, ear_out=4),
  _moon('front') + [L([(38, 95), (62, 95)], OUTC, 'f', False, False, 1.4), L([(48, 76), (48, 86), (52, 86)], _c('#c8a87a'), 'f', False, False, 1.2)],
  _moon('side'), _moon('back'))

# Moos Akka: gorro de berenjena morado con el rabito de hojas azul encima que le baja hasta las cejas; cara redonda, ojos
# cerrados felices, boca pequeña en o y pecas
EGG, LEAF = _c('#855b98'), _c('#2a4a8a')
def _eggplant(view):
    k = 0 if view != 'side' else -4
    body = {'front': [(4, 70), (2, 44), (14, 18), (34, 6), (50, 4), (66, 6), (86, 18), (98, 44), (96, 70), (80, 60), (20, 60)],
            'side': [(4, 76), (2, 44), (16, 16), (40, 4), (60, 4), (82, 16), (96, 40), (94, 60), (60, 58), (50, 80)],
            'back': [(4, 80), (2, 44), (14, 18), (34, 6), (50, 4), (66, 6), (86, 18), (98, 44), (96, 80), (50, 88)]}[view]
    return [L(outline(body), EGG), L(outline([(36 + k, 6), (40 + k, -6, 1), (48 + k, 0), (52 + k, -8, 1), (58 + k, 0), (66 + k, -4, 1), (64 + k, 8)]), LEAF),
            L([(50 + k, -2), (50 + k, -14)], LEAF, 'b', False, False, 2.6)]
C('moos-akka', 'bajito', P('#5a3a6a', '#fdd18c'),
  F(eyes='closed', brows=False, mouth='none', hairline=False, face_front=face(w=4, chin=100, jaw=3), nose=(50, 84, 2.4)),
  _eggplant('front') + [L(ell(50, 93, 2.4, 2.6), _c('#7a3a3a'), 'f', True), L(ell(34, 66, 1.2, 1.2), _c('#c08050'), 'f', False), L(ell(66, 66, 1.2, 1.2), _c('#c08050'), 'f', False)],
  _eggplant('side'), _eggplant('back'))

# Ms Q-T: máscara redonda en blanco y negro con una diana y una Q que le tapa toda la cara, dos coletas larguísimas a rayas
# blancas y negras con lazos morados y un pañuelo morado al cuello
PUR, BW, BB = _c('#7a4aa0'), _c('#ececec'), _c('#2a282a')
def _qt(view):
    out = []
    if view in ('front', 'back'):
        for s in (-1, 1):
            out += [L(outline([(50 + s * 30, 10), (50 + s * 52, 0), (50 + s * 58, 40), (50 + s * 54, 96, 1), (50 + s * 44, 50), (50 + s * 36, 22)]), BW),
                    L(outline([(50 + s * 44, 6), (50 + s * 52, 2), (50 + s * 56, 46), (50 + s * 50, 70), (50 + s * 50, 40)]), BB, 'b', False),
                    L(ell(50 + s * 34, 12, 6, 5), PUR)]
    else:
        out += [L(outline([(40, 8), (20, 0), (8, 40), (14, 96, 1), (26, 50), (36, 24)]), BW), L(outline([(26, 4), (14, 6), (10, 50), (18, 70), (18, 40)]), BB, 'b', False),
                L(ell(38, 10, 6, 5), PUR)]
    if view == 'front':
        out += [L(ell(50, 60, 40, 42), BW, 'f'), L(blob([(50, 18), (90, 60), (50, 102), (50, 60)], 2), BB, 'f', False),
                L(ell(50, 58, 22, 24), BB, 'f', False), L(ell(50, 58, 15, 17), BW, 'f', False), L(ell(50, 58, 8, 10), BB, 'f', False),
                L([(56, 70), (66, 88)], BB, 'f', False, False, 4.0)]
    elif view == 'side':
        out += [L(blob([(30, 22), (74, 18), (90, 50), (84, 92), (60, 102), (40, 94), (26, 60)], 6), BW, 'f')]
    else:
        out += [L(ell(50, 58, 40, 42), BB, 'b')]
    return out
C('ms-qt', 'chica', P('#2a282a', '#f0d0b0'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _qt('front') + [L(outline([(20, 100), (50, 112), (80, 100), (70, 124, 1), (50, 116), (30, 124, 1)]), PUR, 'f')],
  _qt('side'), _qt('back'))

# Mudhi Uppindown: melena castaño morado oscuro hasta el cuello, con las puntas abiertas en mechones hacia fuera y una cinta
# verde oliva en la cabeza; piel morena y ojos amarillos afilados
OLIVE = _c('#a8a040')
C('mudhi-uppindown', 'normal', P('#5c4250', '#ba8f56', iris='#c8b030'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=[(6, 66), (18, 50), (34, 42), (50, 46), (66, 42), (82, 50), (94, 66)]),
  dome('front', top=0, w=46, cy=44, n=7, amp=8, seed=61, long=80, flare=14) + [band('front', OLIVE, y=24, h=6, w=40, dip=10)],
  dome('side', top=0, w=46, cy=44, n=7, amp=8, seed=61, long=80, flare=14, fr=52) + [band('side', OLIVE, y=20, h=6)],
  dome('back', top=0, w=46, cy=44, n=7, amp=8, seed=61, long=80, flare=14, ends=4) + [band('back', OLIVE, y=24, h=6, w=40, dip=6)])

# Nai Swanson: pelo azul peinado hacia arriba en una cresta de pinchos alta con los lados cortos; cara larga y pálida, ojos
# azul claro afilados y el ceño fruncido
C('nai-swanson', 'delgado', P('#3d619d', '#f9d8b6', iris='#7ab0c8'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=97, face_front=face(chin=108, jaw=1), face_side=face_side(chin=7), nose=(50, 86, 2.4),
    hairline=[(6, 62), (18, 50), (30, 42), (50, 40), (70, 42), (82, 50), (94, 62)]),
  [L(outline([(16, 66), (12, 40), (20, 22), (30, 8), (36, -8, 1), (42, 4), (50, -24, 1), (58, 4), (64, -8, 1), (70, 8), (80, 22), (88, 40), (84, 66), (78, 50), (22, 50)])),
   L(outline([(56, -4), (70, 8), (84, 30), (84, 60), (72, 36)]), 'shade', 'b', False)],
  [L(outline([(54, 62), (60, 48), (82, 42), (88, 26), (78, 14), (66, -16, 1), (56, 4), (40, -4, 1), (36, 8), (16, 14), (6, 36), (8, 60), (22, 74), (40, 74), (50, 70)]))],
  [L(outline([(16, 76), (12, 40), (24, 16), (36, -6, 1), (44, 6), (50, -22, 1), (58, 6), (66, -6, 1), (76, 16), (88, 40), (84, 76), (50, 82)]))])

# Nan Desuka (portero): pelo crema muy claro, esponjoso y alborotado con un pelo suelto arriba, que le tapa un ojo; piel
# morena y ojos verde agua
C('nan-desuka', 'normal', P('#f4f0cc', '#cc9d7b', iris='#5ab0a0', shade='#d8d0a8'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 66), (18, 52), (28, 66), (36, 50), (50, 58), (60, 46), (74, 56), (86, 50), (94, 66)]),
  dome('front', top=0, w=48, cy=46, n=9, amp=8, soft=True, seed=62, long=86, flare=10) +
  [L(outline([(48, 30), (66, 36), (76, 50), (78, 76, 1), (66, 62), (56, 50)]), 'mid', 'f'), L(quad((52, 2), (60, -18), (44, -16)), 'mid', 'b', False, False, 2.4)],
  dome('side', top=0, w=48, cy=46, n=9, amp=8, soft=True, seed=62, long=84, flare=10, fr=56),
  dome('back', top=0, w=48, cy=46, n=9, amp=8, soft=True, seed=62, long=84, flare=10, ends=4))

# Narcisse Rotondo: melena negra ondulada hasta los hombros, con mechones sueltos sobre la frente; piel pálida y ojos rojos
# afilados
C('narcisse-rotondo', 'normal', P('#3a3845', '#dfd6c2', iris='#c8202a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 68), (16, 50), (28, 56), (36, 44), (48, 54), (58, 42), (70, 52), (84, 48), (94, 68)]),
  dome('front', top=0, w=48, cy=46, n=8, amp=6, soft=True, seed=63, long=100, flare=12),
  dome('side', top=0, w=48, cy=46, n=8, amp=6, soft=True, seed=63, long=98, flare=12, fr=56),
  dome('back', top=0, w=48, cy=46, n=8, amp=6, soft=True, seed=63, long=98, flare=12, ends=5))

# Nash Room: pelo rosa en forma de seta que le baja hasta las cejas, gafas de sol de montura roja con los cristales blancos
# y una sonrisa
PNKR = _c('#c02a50')
C('nash-shroom-room', 'normal', P('#caa5ae', '#e3c9b4'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, hairline=[(6, 70), (16, 66), (50, 64), (84, 66), (94, 70)]),
  dome('front', top=0, w=52, cy=48, sb=66) + [L([(14, 66), (86, 66)], 'shade', 'f', False, False, 1.2),
  L(outline([(24, 70), (44, 72), (46, 80), (40, 84), (26, 80), (22, 74)]), WHITE, 'f', True, True),
  L(outline([(76, 70), (56, 72), (54, 80), (60, 84), (74, 80), (78, 74)]), WHITE, 'f', True, True),
  L([(22, 72), (46, 72), (54, 72), (78, 72)], PNKR, 'f', False, False, 3.0)],
  dome('side', top=0, w=50, cy=48, nape=72, fr=64) + [L([(70, 74), (90, 74)], PNKR, 'f', False, False, 2.6)],
  dome('back', top=0, w=52, cy=48, nape=74))

# Nate Blackside: pelo negro peinado hacia atrás con un mechón largo que le cae por un lado hasta el pecho, una diadema gris
# en arco como dos cuernos; piel oscura, cara larga, ojos afilados
GRY = _c('#8e868b')
C('nate-n-black-blackside', 'delgado', P('#322f31', '#bd8c69', iris='#2a2a30'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=97, face_front=face(chin=108, jaw=0), face_side=face_side(chin=7), nose=(50, 86, 2.4),
    hairline=[(6, 60), (20, 44), (40, 34), (56, 34), (74, 40), (88, 50), (94, 62)]),
  dome('front', top=2, w=44, cy=44, sb=56) +
  [L(outline([(62, 38), (80, 50), (78, 90), (74, 120, 1), (70, 92), (68, 60)]), 'mid', 'f'),
   L(quad((14, 70), (2, 10), (40, -6)), GRY, 'f', False, False, 3.4), L(quad((86, 70), (98, 10), (60, -6)), GRY, 'f', False, False, 3.4)],
  dome('side', top=2, w=44, cy=44, nape=80, fr=40) + [L(quad((40, 76), (20, 10), (60, -4)), GRY, 'f', False, False, 3.0),
  L(outline([(74, 40), (86, 50), (88, 100), (82, 118, 1), (78, 80)]), 'mid', 'f')],
  dome('back', top=2, w=44, cy=44, nape=80) + [L(quad((14, 70), (2, 10), (40, -6)), GRY, 'f', False, False, 3.4), L(quad((86, 70), (98, 10), (60, -6)), GRY, 'f', False, False, 3.4)])

# Neil Yetty: melena verde en pinchos que le rodea toda la cara y le baja en barba; párpados verdes enormes, nariz grande y
# una sonrisa de dientes
C('neil-yeti-yetty', 'corpulento', P('#457256', '#ca986d', iris='#2a2a20', light='#5a8a6a'),
  F(eyes='closed', brows=False, mouth='grin', mouth_y=96, face_front=face(w=4, chin=100, jaw=4), nose=(50, 84, 4.4), ear_out=8,
    hairline=[(6, 62), (18, 52), (34, 48), (50, 52), (66, 48), (82, 52), (94, 62)]),
  [L(outline([(-4, 70), (6, 88, 1), (8, 108), (24, 120, 1), (40, 108), (50, 124, 1), (60, 108), (76, 120, 1), (92, 108), (94, 88, 1), (104, 70), (86, 80), (50, 108), (14, 80)]))] +
  dome('front', top=-6, w=50, cy=44, n=10, amp=12, seed=64, sb=72) +
  [L(blob([(22, 70), (44, 66), (46, 78), (24, 80)], 6), 'light', 'f', True), L(blob([(78, 70), (56, 66), (54, 78), (76, 80)], 6), 'light', 'f', True)],
  dome('side', top=-6, w=50, cy=44, n=10, amp=12, seed=64, nape=90, fr=48) + [L(outline([(54, 84), (66, 104), (80, 114, 1), (86, 102), (70, 100), (60, 80)]))],
  dome('back', top=-6, w=50, cy=44, n=10, amp=12, seed=64, nape=96, back_n=12))

# Neva Kevinne: melena azul celeste hasta los hombros con dos cuernos grises a los lados y un mechón naranja en el flequillo;
# ojos grandes rosas y piel clara
HRN, ORG = _c('#8a8c8e'), _c('#f0a040')
C('neva-kevinne', 'chica', P('#addee5', '#fcf1d9', iris='#d03a80', shade='#90c0c8'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=94, hairline=[(6, 72), (18, 56), (30, 62), (40, 48), (50, 58), (58, 46), (70, 56), (84, 54), (94, 72)]),
  [horn(10, 46, -6, 30, HRN), horn(90, 46, 106, 30, HRN)] +
  dome('front', top=0, w=46, cy=46, long=96, flare=8) + [L(outline([(58, 30), (68, 34), (66, 62, 1), (60, 44)]), ORG, 'f')],
  [horn(36, 46, 24, 30, HRN)] + dome('side', top=0, w=46, cy=46, long=94, flare=8, fr=56),
  [horn(10, 46, -6, 30, HRN), horn(90, 46, 106, 30, HRN)] + dome('back', top=0, w=46, cy=46, long=94, flare=8, ends=0))

# Newt Lease: pinchos rojos alborotados, orejas grandes y el ceño muy fruncido
C('newt-lease', 'normal', P('#c02c3a', '#fabb7c', iris='#2a1a1a'),
  F(eyes='normal', brows='angry', mouth='frown', mouth_y=94, big_ears=3, ear_out=4,
    hairline=[(6, 62), (18, 48), (30, 54), (40, 44), (52, 52), (62, 42), (74, 50), (84, 46), (94, 62)]),
  dome('front', top=-2, w=48, cy=44, n=8, amp=16, sweep=0.2, seed=65, sb=60),
  dome('side', top=-2, w=48, cy=44, n=8, amp=16, sweep=0.2, seed=65, nape=80, fr=48),
  dome('back', top=-2, w=48, cy=44, n=8, amp=16, sweep=0.2, seed=65, nape=80))

# Newt Tangels (portero): media melena castaño claro ondulada con dos mechones negros en el flequillo; piel muy clara, cara
# larga, ojos de párpado caído y nariz grande
C('newt-tangels', 'delgado', P('#c59c63', '#f8ebc5', iris='#2a2018'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=98, face_front=face(chin=108), face_side=face_side(chin=7, nose=3), nose=(50, 86, 3.6),
    hairline=[(6, 70), (18, 52), (30, 58), (40, 44), (50, 50), (60, 44), (72, 56), (84, 52), (94, 70)]),
  dome('front', top=0, w=46, cy=46, n=7, amp=6, soft=True, seed=66, long=88, flare=12) +
  [L(outline([(36, 22), (42, 20), (36, 70, 1), (32, 46)]), DARK, 'f'), L(outline([(60, 22), (66, 22), (68, 66, 1), (62, 46)]), DARK, 'f')],
  dome('side', top=0, w=46, cy=46, n=7, amp=6, soft=True, seed=66, long=86, flare=12, fr=58),
  dome('back', top=0, w=46, cy=46, n=7, amp=6, soft=True, seed=66, long=86, flare=12, ends=4))

# Nick Yergrub (portero): melena granate ondulada y abultada, cara cuadrada de mandíbula grande con una cicatriz cosida en
# la frente y la mejilla; ojos hundidos y una boca enfadada hacia abajo
C('nick-yergrub', 'corpulento', P('#5f2c36', '#e2ccad', iris='#3a4a6a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=98, mouth_w=12, face_front=face(w=6, chin=106, jaw=8), face_side=face_side(chin=6, jaw=6), nose=(50, 86, 3.4),
    hairline=[(6, 62), (18, 50), (34, 46), (50, 50), (66, 46), (82, 50), (94, 62)]),
  dome('front', top=-2, w=54, cy=46, n=8, amp=8, soft=True, seed=67, long=94, flare=14) +
  [L([(38, 52), (34, 62), (30, 76), (26, 94)], OUTC, 'f', False, False, 1.0)] +
  [L([(c - 2, y), (c + 2, y)], OUTC, 'f', False, False, 0.9) for c, y in ((36, 56), (33, 66), (30, 76), (28, 86))] +
  [L(quad((40, 100), (50, 94), (60, 100)), OUTC, 'f', False, False, 1.6)],
  dome('side', top=-2, w=52, cy=46, n=8, amp=8, soft=True, seed=67, long=92, flare=14, fr=54),
  dome('back', top=-2, w=54, cy=46, n=8, amp=8, soft=True, seed=67, long=92, flare=14, ends=5))

# Nieve Alba: media melena gris azulado como una medusa, con lunares blancos arriba; ojos grandes rojos, dos puntitos bajo
# cada ojo y una bufanda azul grisácea
SCF = _c('#6a8a98')
C('nieve-alba', 'chica', P('#b7c5c7', '#fbefd6', iris='#c02a3a', light='#e8eeee', shade='#909ea0'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=94, hairline=[(6, 70), (18, 56), (50, 52), (82, 56), (94, 70)]),
  dome('front', top=2, w=50, cy=48, long=88, flare=6) +
  [L(ell(36, 16, 5, 3), 'light', 'f', False), L(ell(56, 10, 6, 3), 'light', 'f', False), L(ell(72, 20, 4, 3), 'light', 'f', False),
   L(ell(24, 88, 1.3, 1.3), OUTC, 'f', False), L(ell(28, 90, 1.3, 1.3), OUTC, 'f', False), L(ell(76, 88, 1.3, 1.3), OUTC, 'f', False), L(ell(72, 90, 1.3, 1.3), OUTC, 'f', False),
   L(outline([(20, 100), (50, 108), (80, 100), (84, 112), (50, 120), (16, 112)]), SCF, 'f')],
  dome('side', top=2, w=50, cy=48, long=86, flare=6, fr=54) + [L(ell(40, 14, 5, 3), 'light', 'f', False)],
  dome('back', top=2, w=50, cy=48, long=86, flare=6, ends=0) + [L(ell(40, 20, 5, 3), 'light', 'f', False), L(ell(60, 16, 6, 3), 'light', 'f', False)])

# Nitely Whitehurst: pelo blanco plateado con un mechón grande que se curva sobre la frente y los lados largos hasta la
# mandíbula; ojos afilados grises y ceño fruncido
C('nitely-n-white-whitehurst', 'normal', P('#d6d8db', '#fdf0d5', iris='#5a5a60', shade='#a8aaae'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 66), (18, 48), (34, 40), (50, 44), (66, 40), (82, 48), (94, 66)]),
  dome('front', top=2, w=46, cy=46, long=94, flare=0) +
  [L(outline([(30, 30), (54, 4), (84, 10), (64, 16), (52, 36), (46, 64, 1), (40, 40)]), 'mid', 'f')],
  dome('side', top=2, w=46, cy=46, long=92, flare=0, fr=56) + [L(outline([(50, 16), (80, 4), (98, 14), (76, 20), (70, 36)]), 'mid', 'f')],
  dome('back', top=2, w=46, cy=46, long=92, flare=0, ends=0))

# Nitey Niht: pelo castaño con raya en medio peinado a los lados y un pelo suelto arriba; cara larguísima y pálida, ojos
# cerrados, una pompa de moco en la nariz y la boca abierta babeando
C('nitey-niht', 'delgado', P('#8c6114', '#fceab8'),
  F(eyes='closed', brows='angry', mouth='none', face_front=face(chin=112, jaw=-1), face_side=face_side(chin=10, nose=4), nose=(50, 86, 3.4),
    hairline=[(6, 60), (20, 44), (38, 38), (50, 44), (62, 38), (80, 44), (94, 60)]),
  dome('front', top=4, w=44, cy=44, sb=56) + [L(quad((50, 6), (56, -12), (46, -14)), 'mid', 'b', False, False, 2.4),
  L(ell(44, 92, 5, 5), _c('#cae8f0'), 'f', True, True), L(ell(50, 102, 4, 3), _c('#a0302a'), 'f', True)],
  dome('side', top=4, w=44, cy=44, nape=80, fr=44) + [L(ell(94, 92, 4, 4), _c('#cae8f0'), 'f', True, True)],
  dome('back', top=4, w=44, cy=44, nape=80) + [L(quad((50, 6), (56, -12), (46, -14)), 'mid', 'b', False, False, 2.4)])

# Noah Anon-Nymous: pelo gris azulado corto en forma de tabla plana arriba, con la frente en pico; ojos azul grisáceo y
# sonrisa
C('noah-anon-nymous', 'normal', P('#516a74', '#fabc7e', iris='#4a6a7a'),
  F(eyes='normal', brows='angry', mouth='smile', mouth_y=93, hairline=[(6, 60), (18, 46), (34, 42), (50, 50), (66, 42), (82, 46), (94, 60)]),
  [L(outline([(16, 62), (12, 30), (6, 8), (50, 4), (94, 8), (88, 30), (84, 62), (78, 46), (22, 46)])),
   L(outline([(60, 6), (94, 8), (88, 30), (84, 58), (74, 30)]), 'shade', 'b', False)],
  [L(outline([(54, 62), (60, 48), (80, 44), (92, 30), (94, 8), (60, 4), (10, 8), (4, 30), (8, 62), (22, 78), (40, 78), (50, 72)]))],
  [L(outline([(16, 80), (12, 30), (6, 8), (50, 4), (94, 8), (88, 30), (84, 80), (50, 86)]))])

# Noah Yu: pelo a rayas verde azulado y azul que se enrosca en una espiral grande sobre la frente y cae en una coleta gruesa
# por un lado hasta el pecho; piel morena, ojos afilados y sonrisa
TL, BL = _c('#245d67'), _c('#5e7096')
C('noah-yu', 'normal', P('#5e7096', '#ad8762', iris='#3a2a2a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=95, hairline=[(6, 62), (20, 46), (40, 40), (58, 46), (74, 44), (88, 52), (94, 62)]),
  dome('front', top=-2, w=44, cy=42, sb=56, shade=False) +
  [L(blob([(30, 42), (24, 10), (48, -6), (70, 6), (66, 30), (50, 26), (44, 40)], 6), TL, 'f'), L([(38, 6), (60, 30)], BL, 'f', False, False, 3.0),
   L(outline([(70, 40), (86, 54), (86, 90), (76, 120, 1), (70, 92), (64, 60)]), TL, 'f'), L([(78, 60), (80, 100)], BL, 'f', False, False, 2.4)],
  dome('side', top=-2, w=44, cy=42, nape=78, fr=44, shade=False) + [L(blob([(40, 20), (50, -6), (78, 4), (86, 30), (66, 34)], 6), TL, 'f'),
  L(outline([(30, 50), (44, 60), (40, 100), (32, 120, 1), (26, 90)]), TL, 'f')],
  dome('back', top=-2, w=44, cy=42, nape=78, shade=False) + [L(outline([(80, 40), (94, 60), (92, 100), (82, 120, 1), (76, 80)]), TL, 'f'), L([(40, 10), (60, 30)], TL, 'b', False, False, 3.0)])

# Nuno Vertigo (portero): pinchos azul marino con una cinta blanca retorcida en la frente y dos borlas blancas a los lados
TWW = _c('#ecece8')
C('nuno-vertigo', 'normal', P('#464c78', '#f9bc7d', iris='#2a1a1a'),
  F(eyes='normal', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 66), (16, 60), (50, 58), (84, 60), (94, 66)]),
  dome('front', top=-6, w=46, cy=44, n=8, amp=14, seed=68, sb=60) + [band('front', TWW, y=50, h=12, w=46, dip=2),
  L(ell(4, 30, 7, 6), TWW, 'f'), L(ell(96, 30, 7, 6), TWW, 'f')] +
  [L([(x, 52), (x + 6, 62)], _c('#b8b8b0'), 'f', False, False, 1.0) for x in range(10, 90, 10)],
  dome('side', top=-6, w=46, cy=44, n=8, amp=14, seed=68, nape=80, fr=48) + [band('side', TWW, y=46, h=12), L(ell(40, 28, 7, 6), TWW, 'f')],
  dome('back', top=-6, w=46, cy=44, n=8, amp=14, seed=68, nape=80) + [band('back', TWW, y=50, h=12, w=46, dip=2), L(ell(4, 30, 7, 6), TWW, 'f'), L(ell(96, 30, 7, 6), TWW, 'f')])

# Ocho Lightning: pelo blanco liso echado a un lado que le tapa un ojo, con un rayo naranja en el flequillo; ojos grises en
# espiral y ceño fruncido
OR2 = _c('#dd6f19')
C('ocho-lightning', 'normal', P('#e8e4e0', '#fbd08d', iris='#6a6060', shade='#b8aca6'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 68), (18, 50), (30, 44), (50, 50), (66, 60), (82, 66), (94, 68)]),
  dome('front', top=0, w=46, cy=46, n=6, amp=10, sweep=0.6, seed=69, sb=74) +
  [L(outline([(16, 44), (50, 26), (84, 40), (96, 54, 1), (76, 52), (66, 76, 1), (54, 54), (40, 50)]), 'mid', 'f'),
   L(outline([(30, 28), (42, 22), (40, 36), (52, 34), (60, 66, 1), (48, 44), (40, 46)]), OR2, 'f')],
  dome('side', top=0, w=46, cy=46, n=6, amp=10, sweep=0.6, seed=69, nape=84, fr=56) + [L(outline([(54, 24), (64, 20), (70, 44, 1), (62, 34)]), OR2, 'f')],
  dome('back', top=0, w=46, cy=46, n=6, amp=10, sweep=0.6, seed=69, nape=84))

# Ollie Impix (portero): pelo rubio peinado en casco con raya y la frente tapada, antifaz negro, cara anchísima y una boca
# recta y larga
C('ollie-impix', 'corpulento', P('#e6c169', '#fdcf9e', iris='#3a3a3a'),
  F(eyes='sharp', brows=False, mouth='none', face_front=face(w=8, chin=106, jaw=8), face_side=face_side(chin=6, jaw=6), ear_out=8,
    hairline=[(6, 64), (14, 60), (50, 58), (86, 60), (94, 64)]),
  dome('front', top=0, w=50, cy=46, sb=60) + [L([(50, 6), (48, 56)], 'shade', 'f', False, False, 1.2),
  L(outline([(14, 64), (50, 70), (86, 64), (84, 82), (60, 84), (50, 78), (40, 84), (16, 82)]), BLACK, 'f', True),
  L(ell(34, 75, 6, 4), WHITE, 'f', False), L(ell(66, 75, 6, 4), WHITE, 'f', False), L(ell(34, 76, 2.6, 2.6), BLACK, 'f', False), L(ell(66, 76, 2.6, 2.6), BLACK, 'f', False),
  L([(30, 98), (70, 98)], OUTC, 'f', False, False, 1.6)],
  dome('side', top=0, w=48, cy=46, nape=80, fr=58) + [L(outline([(66, 66), (92, 64), (92, 82), (68, 84)]), BLACK, 'f', True)],
  dome('back', top=0, w=50, cy=46, nape=80) + [L([(8, 74), (92, 74)], BLACK, 'f', False, False, 2.4)])

# Olympe Haymes (portera): melena roja lisa hasta la mandíbula con dos horquillas plateadas en punta, ojos grises afilados y
# la lengua fuera
SIL = _c('#c8d0dc')
C('olympe-haymes', 'chica', P('#c6302c', '#fccfa0', iris='#6a7a8a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=[(6, 72), (18, 50), (30, 58), (42, 44), (50, 54), (58, 44), (70, 58), (82, 50), (94, 72)]),
  dome('front', top=0, w=46, cy=46, long=94, flare=4) +
  [L(outline([(16, 40), (32, 30), (30, 36)]), SIL, 'f'), L(outline([(84, 40), (68, 30), (70, 36)]), SIL, 'f'),
   L(ell(54, 97, 2.6, 2.4), _c('#e06a70'), 'f', True)],
  dome('side', top=0, w=46, cy=46, long=92, flare=4, fr=56) + [L(outline([(64, 36), (80, 26), (78, 32)]), SIL, 'f')],
  dome('back', top=0, w=46, cy=46, long=92, flare=4, ends=0))

# Ophelio Albans: pelo verde menta muy corto arriba y los lados rapados con dibujos azules; piel morena, ojos verde agua
# afilados y la boca apretada
BLU2 = _c('#5050c0')
C('ophelio-opal-albans', 'normal', P('#69c4a2', '#cd9569', iris='#3ac0a0'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 56), (18, 46), (30, 40), (50, 38), (70, 40), (82, 46), (94, 56)]),
  [L(outline([(14, 66), (12, 40), (22, 18), (78, 18), (88, 40), (86, 66), (80, 46), (20, 46)]), BLU2),
   L(outline([(22, 34), (26, 14), (50, 6), (74, 14), (78, 34), (60, 24), (50, 36), (40, 24)]))],
  [L(outline([(54, 60), (58, 46), (80, 40), (86, 24), (70, 8), (40, 4), (16, 12), (6, 34), (8, 58), (22, 70), (40, 70), (50, 66)]), BLU2),
   L(outline([(40, 4), (70, 8), (86, 24), (60, 26), (40, 20)]))],
  [L(outline([(16, 76), (12, 40), (22, 16), (50, 8), (78, 16), (88, 40), (84, 76), (50, 82)]), BLU2), L(outline([(30, 20), (50, 8), (70, 20), (50, 28)]))])

# Ord Ayshus: pelo verde azulado oscuro en casco redondo con el flequillo en picos cortos sobre la frente; piel morena,
# ojos redondos con párpados y la boca entreabierta
C('ord-ayshus', 'normal', P('#314e52', '#cd976a', iris='#3a5a4a'),
  F(eyes='normal', brows=False, mouth='line', mouth_y=95, hairline=[(6, 66), (18, 56), (28, 62), (36, 54), (46, 60), (56, 54), (66, 60), (76, 54), (86, 58), (94, 66)]),
  dome('front', top=2, w=48, cy=46, sb=68),
  dome('side', top=2, w=48, cy=46, nape=82, fr=58),
  dome('back', top=2, w=48, cy=46, nape=82))

# Orel Knighter: pelo azul verdoso muy corto con muescas cuadradas como almenas, cara cuadrada pálida, ojos pequeñísimos y
# una boca enorme abierta llena de dientes afilados; perilla
C('orel-knighter', 'corpulento', P('#345966', '#e3ccad', iris='#1e1e1e'),
  F(eyes='dot', brows=False, mouth='none', face_front=face(w=6, chin=106, jaw=6), face_side=face_side(chin=6, jaw=6), nose=(50, 80, 3),
    hairline=[(6, 56), (16, 50), (24, 40), (30, 40), (32, 54), (40, 54), (42, 40), (58, 40), (60, 54), (68, 54), (70, 40), (76, 40), (84, 50), (94, 56)]),
  dome('front', top=10, w=46, cy=46, sb=56) +
  [L(ell(50, 94, 16, 14), _c('#7a3a5a'), 'f', True), L(ell(50, 99, 10, 8), _c('#c8a0d0'), 'f', False)] +
  [L(outline([(x - 3.5, 81), (x, 89, 1), (x + 3.5, 81)]), WHITE, 'f', False) for x in (38, 46, 54, 62)] +
  [L(outline([(x - 3.5, 107), (x, 99, 1), (x + 3.5, 107)]), WHITE, 'f', False) for x in (40, 50, 60)] +
  [L(outline([(44, 110), (56, 110), (50, 116)]), 'mid', 'f')],
  dome('side', top=10, w=46, cy=46, nape=80, fr=44) + [L(ell(84, 94, 6, 9), _c('#7a3a5a'), 'f', True)],
  dome('back', top=10, w=46, cy=46, nape=80))

# Orson Riffe: melena verde alborotada en mechones gruesos que le tapa medio rostro, con una pluma negra al otro lado; piel
# muy clara, ojo amarillo y labios oscuros
FTH = _c('#2a2a2e')
C('orson-riffe', 'normal', P('#4c836e', '#f5efda', iris='#d8c040', shade='#36514a', deep='#2f3b35'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=95, hairline=[(6, 66), (14, 40), (40, 30), (60, 34), (80, 44), (94, 66)]),
  dome('front', top=-2, w=48, cy=44, n=6, amp=14, soft=True, sweep=-0.4, seed=70, sb=72, shade=True) +
  [L(outline([(14, 40), (40, 22), (60, 30), (56, 60), (48, 84, 1), (40, 70), (30, 92, 1), (24, 70), (10, 80, 1), (8, 56)]), 'mid', 'f'),
   L(outline([(80, 40), (96, 16, 1), (100, 30), (88, 46)]), FTH, 'f'), L(outline([(82, 50), (104, 34, 1), (100, 46)]), FTH, 'f')],
  dome('side', top=-2, w=48, cy=44, n=6, amp=14, soft=True, sweep=-0.4, seed=70, nape=86, fr=50) + [L(outline([(36, 30), (24, 6, 1), (16, 20), (28, 36)]), FTH, 'f')],
  dome('back', top=-2, w=48, cy=44, n=6, amp=14, soft=True, sweep=-0.4, seed=70, nape=86) + [L(outline([(16, 40), (2, 16, 1), (0, 30), (12, 46)]), FTH, 'f')])

# Oswald Bones: pelo blanco plateado liso que le tapa un ojo, una máscara blanca de calavera en la boca con rayas negras; un
# ojo de pestañas abierto y el otro guiñado
SKM = _c('#f4f2ee')
C('oswald-bones', 'normal', P('#d5d6d9', '#dcc8ad', iris='#1e1e1e', shade='#a8a8ae'),
  F(eyes='sharp', brows=False, mouth='none', hairline=[(6, 66), (18, 48), (34, 40), (50, 46), (66, 54), (82, 62), (94, 66)]),
  dome('front', top=2, w=46, cy=46, sb=70) +
  [L(outline([(20, 44), (50, 28), (80, 40), (74, 60), (64, 82, 1), (56, 58), (44, 52)]), 'mid', 'f'),
   L(outline([(22, 86), (50, 84), (78, 86), (74, 100), (50, 108), (26, 100)]), SKM, 'f', True, True)] +
  [L([(x, 86), (x, 100)], OUTC, 'f', False, False, 1.2) for x in (38, 50, 62)] + [L(ell(x, 100, 1.6, 1.6), OUTC, 'f', False) for x in (38, 50, 62)],
  dome('side', top=2, w=46, cy=46, nape=84, fr=56) + [L(outline([(64, 84), (90, 82), (88, 98), (66, 102)]), SKM, 'f', True, True)],
  dome('back', top=2, w=46, cy=46, nape=84))

# Othello Go: gorra blanca de capitán con visera, pelo azul marino que asoma a los lados y una coleta rizada atrás; gafas
# negras de natación, nariz larga en punta y una sonrisa enorme de dientes (con su modelo 3D)
CAPW, CAPS = _c('#f2eeee'), _c('#c8c0c0')
def _captain(view):
    if view == 'front':
        return [L(outline([(10, 44), (14, 16), (50, 2), (86, 16), (90, 44), (50, 40)]), CAPW),
                L(outline([(14, 40), (50, 36), (86, 40), (84, 50), (50, 46), (16, 50)]), CAPS, 'f', True, True),
                L(outline([(24, 50), (50, 46), (76, 50), (70, 58), (30, 58)]), _c('#2a2a2e'), 'f', True)]
    if view == 'side':
        return [L(outline([(6, 44), (16, 12), (50, 2), (80, 14), (88, 40), (50, 44)]), CAPW),
                L(outline([(60, 40), (102, 42), (100, 50), (62, 50)]), _c('#2a2a2e'), 'f', True), L(outline([(8, 40), (88, 38), (88, 46), (8, 48)]), CAPS, 'f', True, True)]
    return [L(outline([(10, 44), (14, 16), (50, 2), (86, 16), (90, 44), (50, 40)]), CAPW), L(outline([(12, 40), (88, 40), (88, 48), (12, 48)]), CAPS, 'f', True, True)]
C('othello-go', 'delgado', P('#36324a', '#fab87d', iris='#2a2a30'),
  F(eyes='none', brows=False, mouth='none', face_front=face(chin=110, jaw=-2), face_side=face_side(chin=8, nose=10), hairline=False),
  [L(outline([(14, 50), (8, 70), (12, 82, 1), (20, 70)])), L(outline([(86, 50), (92, 70), (88, 82, 1), (80, 70)]))] + _captain('front') +
  [L(outline([(20, 68), (46, 68), (54, 68), (80, 68), (80, 80), (54, 78), (46, 78), (20, 80)]), _c('#1e1e22'), 'f', True),
   L(ell(32, 73, 7, 4), _c('#4a4a52'), 'f', False), L(ell(68, 73, 7, 4), _c('#4a4a52'), 'f', False),
   L(outline([(30, 94), (70, 94), (62, 106), (38, 106)]), WHITE, 'f', True, True), L([(32, 98), (68, 98)], _c('#b0a8a8'), 'f', False, False, 0.8)],
  [L(outline([(8, 44), (2, 70), (20, 76), (40, 64), (50, 50)])), L(outline([(14, 54), (-6, 70), (2, 92, 1), (10, 74), (-4, 96, 1), (16, 84)]))] + _captain('side') +
  [L(outline([(68, 68), (92, 68), (92, 80), (70, 80)]), _c('#1e1e22'), 'f', True)],
  [L(outline([(12, 44), (12, 80), (50, 90), (88, 80), (88, 44)])), L(outline([(44, 60), (40, 96, 1), (50, 84), (60, 96, 1), (56, 60)]))] + _captain('back'))

# Otto Legge (portero): pelo rojo de tentáculos de pulpo en filas alrededor de la cabeza, con ventosas; piel tostada, cara
# redonda, ojos pequeños redondos y la boca en o
TEN, SUC = _c('#a01322'), _c('#e07a6a')
def _octo(view):
    out = []
    if view == 'front':
        out += [L(outline([(4, 66), (6, 40), (20, 22), (50, 16), (80, 22), (94, 40), (96, 66), (84, 56), (16, 56)]), TEN)]
        for s in (-1, 1):
            out += [L(outline([(50 + s * 40, 50), (50 + s * 52, 74), (50 + s * 50, 100), (50 + s * 40, 108, 1), (50 + s * 42, 90), (50 + s * 36, 70)]), TEN)]
            out += [L(ell(50 + s * 46, y, 1.6, 1.6), SUC, 'f', False) for y in (70, 84, 96)]
        out += [L(quad((x, 20), (x + 4, 36), (x, 50)), _c('#701618'), 'b', False, False, 1.2) for x in (30, 44, 58, 72)]
    elif view == 'side':
        out += [L(outline([(6, 80), (4, 44), (20, 22), (50, 16), (80, 24), (90, 40), (70, 54), (52, 56), (44, 76), (30, 100), (18, 110, 1), (20, 90)]), TEN)]
        out += [L(ell(x, y, 1.6, 1.6), SUC, 'f', False) for x, y in ((20, 70), (24, 86))]
    else:
        out += [L(outline([(4, 80), (6, 40), (20, 22), (50, 16), (80, 22), (94, 40), (96, 80), (90, 104), (80, 110, 1), (76, 92), (50, 96), (24, 92), (20, 110, 1), (10, 104)]), TEN)]
    return out
C('otto-tentacle-legge', 'corpulento', P('#a01322', '#cf9569', iris='#1e1e1e'),
  F(eyes='round', brows='angry', mouth='none', face_front=face(w=6, chin=104, jaw=6), face_side=face_side(chin=4, jaw=4), hairline=[(6, 60), (16, 56), (50, 54), (84, 56), (94, 60)],
    nose=(50, 86, 2.6), ear_out=6),
  _octo('front') + [L(ell(50, 94, 2.6, 3), _c('#5a2a2a'), 'f', True)], _octo('side'), _octo('back'))

# Oz Rater: melena de pinchos rojo oscuro arriba que se vuelve naranja por los lados y le cae larga hasta los hombros; ojos
# afilados, sonrisa de dientes y un pendiente
ORA = _c('#d86020')
C('oz-rater', 'normal', P('#a63834', '#fbcf8d', iris='#5a3a1a', shade='#7b2c1e'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=96, hairline=[(6, 66), (18, 50), (28, 58), (36, 44), (48, 54), (58, 42), (70, 54), (82, 50), (94, 66)]),
  [L(outline([(10, 44), (-6, 76, 1), (6, 70), (0, 104, 1), (14, 84), (16, 110, 1), (24, 80), (24, 56)]), ORA),
   L(outline([(90, 44), (106, 76, 1), (94, 70), (100, 104, 1), (86, 84), (84, 110, 1), (76, 80), (76, 56)]), ORA)] +
  dome('front', top=-8, w=46, cy=42, n=8, amp=16, seed=71, sb=60) + [L(ell(86, 82, 1.6, 2.4), _c('#e8c040'), 'f', True)],
  [L(outline([(14, 50), (2, 90, 1), (14, 80), (14, 112, 1), (28, 84), (40, 104, 1), (44, 70)]), ORA)] +
  dome('side', top=-8, w=46, cy=42, n=8, amp=16, seed=71, nape=78, fr=50),
  [L(outline([(6, 50), (-4, 90, 1), (10, 84), (10, 112, 1), (30, 88), (50, 114, 1), (70, 88), (90, 112, 1), (90, 84), (104, 90, 1), (94, 50)]), ORA)] +
  dome('back', top=-8, w=46, cy=42, n=8, amp=16, seed=71, nape=78))

# Paco Dermott (portero): máscara de elefante gris con dos colmillos blancos a los lados y la trompa bajándole por el centro
# de la cara; ojos naranjas y piel oscura
ELE, TUSK = _c('#6c6764'), _c('#e8ecea')
def _elephant(view):
    if view == 'front':
        return [L(outline([(-4, 70), (2, 40), (14, 16), (50, 4), (86, 16), (98, 40), (104, 70), (88, 80), (80, 62), (20, 62), (12, 80)]), ELE),
                L(outline([(10, 70), (2, 52), (8, 40), (16, 58), (20, 76)]), TUSK, 'f'), L(outline([(90, 70), (98, 52), (92, 40), (84, 58), (80, 76)]), TUSK, 'f'),
                L(outline([(18, 60), (82, 60), (82, 70), (60, 72), (58, 110), (50, 116), (42, 110), (40, 72), (18, 70)]), ELE, 'f'),
                L(ell(32, 76, 6, 5), WHITE, 'f', True), L(ell(68, 76, 6, 5), WHITE, 'f', True),
                L(ell(32, 76, 3.4, 3.4), _c('#f0801e'), 'f', False), L(ell(68, 76, 3.4, 3.4), _c('#f0801e'), 'f', False)]
    if view == 'side':
        return [L(outline([(2, 80), (2, 40), (16, 14), (50, 4), (84, 16), (96, 44), (98, 70), (104, 110), (94, 114), (86, 80), (60, 70), (40, 86)]), ELE),
                L(outline([(70, 76), (82, 64), (90, 72), (76, 86)]), TUSK, 'f')]
    return [L(outline([(-4, 70), (2, 40), (14, 16), (50, 4), (86, 16), (98, 40), (104, 70), (88, 86), (50, 92), (12, 86)]), ELE)]
C('paco-dermott', 'corpulento', P('#594d4a', '#c08e69'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=100, hairline=False, ears=False, face_front=face(w=4, chin=106, jaw=4)),
  _elephant('front'), _elephant('side'), _elephant('back'))

# Paris Mosquito-Sight: melena gris verdosa lisa en mechones planos que le cuelgan como plumas, gafas de aviador de cristal
# marrón y una nariz naranja larguísima en pico de mosquito; piel morena
BEAK, GOG = _c('#e07a20'), _c('#6a4a40')
C('paris-mosquito-sight', 'normal', P('#99a19c', '#bd8d69', iris='#3a2a2a', shade='#7d837e'),
  F(eyes='none', brows=False, mouth='none', hairline=[(6, 70), (20, 56), (40, 48), (50, 54), (60, 48), (80, 56), (94, 70)]),
  dome('front', top=0, w=46, cy=44, long=104, flare=16, n=0) +
  [L(outline([(46, 6), (50, 24), (54, 6)]), 'shade', 'f', False),
   L(ell(34, 74, 10, 8), _c('#c0c0b8'), 'f', True), L(ell(66, 74, 10, 8), _c('#c0c0b8'), 'f', True),
   L(ell(34, 74, 7.4, 5.6), GOG, 'f', False), L(ell(66, 74, 7.4, 5.6), GOG, 'f', False),
   L(outline([(44, 78), (56, 78), (50, 122, 1)]), BEAK, 'f')],
  dome('side', top=0, w=46, cy=44, long=102, flare=16, fr=56) + [L(ell(78, 74, 6, 7), GOG, 'f', True), L(outline([(82, 80), (88, 84), (110, 112, 1)]), BEAK, 'f')],
  dome('back', top=0, w=46, cy=44, long=102, flare=16, ends=5))

# Pat Ryarke (portero): pelo gris verdoso corto, gafas redondas grandes de cristales blancos opacos, cejas gruesas, nariz
# redonda y la boca enfadada hacia abajo; piel muy clara
C('pat-ryarke', 'normal', P('#717d75', '#fbe9b8', iris='#1e1e1e'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, nose=(50, 88, 3.4), ear_out=4, big_ears=1,
    hairline=[(6, 60), (16, 48), (30, 42), (50, 44), (70, 42), (84, 48), (94, 60)]),
  dome('front', top=6, w=44, cy=44, sb=56) +
  [L([(26, 64), (40, 64)], OUTC, 'f', False, False, 3.0), L([(60, 64), (74, 64)], OUTC, 'f', False, False, 3.0),
   L(ell(34, 75, 10, 9), WHITE, 'f', True, True), L(ell(66, 75, 10, 9), WHITE, 'f', True, True), L([(43, 76), (57, 76)], _c('#a8a0a0'), 'f', False, False, 1.4)],
  dome('side', top=6, w=44, cy=44, nape=80, fr=46) + [L(ell(82, 76, 5, 7), WHITE, 'f', True)],
  dome('back', top=6, w=44, cy=44, nape=80))

# Patrick Childs: gorro verde de punta caída que le tapa un ojo, pelo rubio debajo; ojo azul y sonrisa
HAT, HATD = _c('#66974b'), _c('#4a6a37')
C('patrick-childs', 'normal', P('#e8b858', '#f1c492', iris='#5a7aa8'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=94, hairline=[(6, 70), (16, 66), (50, 70), (84, 66), (94, 70)]),
  [L(outline([(10, 60), (8, 90), (20, 96), (24, 70)])), L(outline([(90, 60), (92, 90), (80, 96), (76, 70)]))] +
  [L(outline([(-2, 62), (4, 30), (24, 10), (56, 4), (80, 8), (94, -2, 1), (96, 20), (104, 50), (100, 70), (70, 66), (50, 76), (30, 82), (6, 74)]), HAT),
   L(outline([(-2, 62), (30, 72), (60, 64), (100, 62), (100, 72), (60, 76), (32, 86), (2, 76)]), HATD, 'f', True)],
  [L(outline([(48, 60), (44, 90), (56, 92), (60, 70)]))] +
  [L(outline([(2, 70), (6, 30), (30, 8), (60, 4), (88, 16), (98, 40), (96, 66), (60, 66), (20, 80)]), HAT), L(outline([(28, 6), (10, -6, 1), (18, 12)]), HAT)],
  [L(outline([(-2, 66), (4, 30), (24, 10), (56, 4), (80, 8), (94, -2, 1), (96, 20), (104, 50), (102, 72), (50, 82)]), HAT)])

# Patton Fairway: pelo negro peinado hacia arriba en una punta, con patillas largas hasta la mandíbula y una perilla; nariz
# larga, ceño fruncido y boca enfadada
C('patton-fairway', 'normal', P('#302e2d', '#f9bc7d', iris='#1e1e1e'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=97, face_front=face(chin=106, jaw=2), face_side=face_side(chin=6, nose=5), nose=(50, 86, 3.2),
    hairline=[(6, 60), (18, 46), (32, 40), (50, 42), (68, 40), (82, 46), (94, 60)]),
  [L(outline([(16, 66), (14, 36), (30, 12), (50, -12, 1), (70, 12), (86, 36), (84, 66), (78, 46), (22, 46)])),
   L(outline([(54, -6), (70, 12), (84, 34), (82, 60), (70, 30)]), 'shade', 'b', False),
   L(outline([(18, 56), (24, 56), (26, 96), (20, 92)]), 'mid', 'f'), L(outline([(82, 56), (76, 56), (74, 96), (80, 92)]), 'mid', 'f'),
   L(outline([(42, 104), (58, 104), (50, 110)]), 'mid', 'f')],
  [L(outline([(54, 62), (58, 48), (80, 42), (86, 28), (66, 6), (54, -12, 1), (40, 4), (16, 12), (6, 34), (8, 60), (22, 76), (40, 76), (50, 70)])),
   L(outline([(50, 60), (56, 60), (56, 92), (50, 90)]), 'mid', 'f')],
  [L(outline([(16, 76), (14, 36), (30, 12), (50, -12, 1), (70, 12), (86, 36), (84, 76), (50, 82)]))])

# Patty Sierra (portera): media melena castaña con las puntas y el interior rosa, una diadema verde con dos cerezas encima y
# una flor rosa en el pelo; ojos grandes rosas, coloretes y boquita en o
CHR, LEAFG = _c('#b0303a'), _c('#5aa040')
C('patty-sierra', 'chica', P('#7a584e', '#fdecc1', iris='#c04a6a', light='#e1a187'),
  F(eyes='big', brows=False, mouth='none', hairline=[(6, 72), (18, 52), (30, 46), (50, 50), (70, 46), (82, 52), (94, 72)]),
  dome('front', top=4, w=46, cy=46, long=94, flare=4) +
  [L(outline([(6, 64), (14, 64), (16, 94), (8, 94)]), 'light'), L(outline([(94, 64), (86, 64), (84, 94), (92, 94)]), 'light'),
   L(quad((14, 30), (50, 0), (86, 30)), LEAFG, 'f', False, False, 3.0), L(ell(40, 2, 8, 7), CHR, 'f'), L(ell(60, 2, 8, 7), CHR, 'f'),
   L(ell(64, 38, 3, 3), _c('#f0a0a8'), 'f', True), L(ell(50, 94, 1.8, 2.2), _c('#7a3a3a'), 'f', False)] + blush(),
  dome('side', top=4, w=46, cy=46, long=92, flare=4, fr=56) + [L(quad((30, 30), (50, 4), (80, 22)), LEAFG, 'f', False, False, 3.0), L(ell(50, 2, 8, 7), CHR, 'f')],
  dome('back', top=4, w=46, cy=46, long=92, flare=4, ends=0) + [L(ell(40, 2, 8, 7), CHR, 'f'), L(ell(60, 2, 8, 7), CHR, 'f')])

# Penn Manship: pelo azul marino violáceo en pinchos alborotados con dos puntas a los lados; piel clara, ojos ámbar
# afilados y ceño fruncido
C('penn-manship', 'normal', P('#463f58', '#fcefd4', iris='#c88a40'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 64), (18, 50), (30, 56), (38, 44), (50, 52), (60, 42), (72, 52), (84, 48), (94, 64)]),
  dome('front', top=0, w=46, cy=44, n=7, amp=12, seed=72, sb=70) + [L(outline([(10, 52), (-6, 50, 1), (8, 62)])), L(outline([(90, 52), (106, 50, 1), (92, 62)]))],
  dome('side', top=0, w=46, cy=44, n=7, amp=12, seed=72, nape=82, fr=50),
  dome('back', top=0, w=46, cy=44, n=7, amp=12, seed=72, nape=82))

# Pepe Bell: gorro de pimiento verde con el rabito encima que le baja hasta las cejas; cejas gruesas y sonrisa de dientes
PEP, PEPD = _c('#397f49'), _c('#2a5a34')
def _pepper(view):
    if view == 'front':
        return [L(blob([(2, 64), (-2, 30), (18, 10), (36, 18), (50, 6), (64, 18), (82, 10), (102, 30), (98, 64), (80, 58), (50, 64), (20, 58)], 6), PEP),
                L([(36, 18), (40, 58)], PEPD, 'b', False, False, 1.6), L([(64, 18), (60, 58)], PEPD, 'b', False, False, 1.6),
                L(quad((50, 8), (52, -8), (62, -14)), _c('#6a8a3a'), 'b', False, False, 3.0)]
    if view == 'side':
        return [L(blob([(2, 72), (0, 30), (20, 8), (50, 6), (80, 12), (98, 36), (96, 60), (60, 60), (44, 76)], 6), PEP),
                L(quad((50, 8), (50, -8), (60, -14)), _c('#6a8a3a'), 'b', False, False, 3.0)]
    return [L(blob([(2, 74), (-2, 30), (18, 10), (36, 18), (50, 6), (64, 18), (82, 10), (102, 30), (98, 74), (50, 84)], 6), PEP),
            L(quad((50, 8), (52, -8), (62, -14)), _c('#6a8a3a'), 'b', False, False, 3.0)]
C('pepe-bell', 'normal', P('#283021', '#f1c695', iris='#2a2a2a'),
  F(eyes='normal', brows='angry', mouth='grin', mouth_y=95, hairline=False, ears=False),
  _pepper('front') + [L([(24, 62), (40, 66)], _c('#8a6a2a'), 'f', False, False, 3.4), L([(76, 62), (60, 66)], _c('#8a6a2a'), 'f', False, False, 3.4)],
  _pepper('side'), _pepper('back'))

# Perla Sizzors: pelo rosa con dos lazadas grandes encima y dos abajo a los lados, como las asas de unas tijeras; piel
# clara, ojos grandes rojizos y una sonrisa abierta
C('perla-sizzors', 'chica', P('#cfa1b4', '#fdf1bf', iris='#c03a5a', shade='#9a6a76'),
  F(eyes='big', brows=False, mouth='grin', mouth_y=94, hairline=[(6, 68), (18, 50), (34, 40), (50, 42), (66, 40), (82, 50), (94, 68)]),
  [L(blob([(14, 20), (4, -6), (24, -16), (40, 0), (34, 14)], 6)), L(blob([(86, 20), (96, -6), (76, -16), (60, 0), (66, 14)], 6)),
   L(ell(20, -2, 6, 6), _c('#fdf8f0'), 'b', False), L(ell(80, -2, 6, 6), _c('#fdf8f0'), 'b', False),
   L(blob([(14, 76), (-4, 84), (0, 104), (14, 108), (20, 92)], 6)), L(blob([(86, 76), (104, 84), (100, 104), (86, 108), (80, 92)], 6))] +
  dome('front', top=4, w=46, cy=46, sb=76),
  [L(blob([(40, 14), (36, -10), (56, -16), (64, 4)], 6)), L(blob([(30, 76), (14, 88), (18, 106), (34, 104)], 6))] + dome('side', top=4, w=46, cy=46, nape=84, fr=50),
  [L(blob([(14, 20), (4, -6), (24, -16), (40, 0), (34, 14)], 6)), L(blob([(86, 20), (96, -6), (76, -16), (60, 0), (66, 14)], 6)),
   L(blob([(14, 76), (-4, 84), (0, 104), (14, 108), (20, 92)], 6)), L(blob([(86, 76), (104, 84), (100, 104), (86, 108), (80, 92)], 6))] +
  dome('back', top=4, w=46, cy=46, nape=84))

# Pero Tractor: pelo amarillo pajizo en un abanico plano como una escoba encima de la cabeza; piel morena, cara ancha, nariz
# roja, párpados caídos y una boca enfadada grande
C('pero-tractor', 'corpulento', P('#e1d87c', '#bc864e', iris='#1e1e1e', shade='#b8ae5a'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=98, mouth_w=12, face_front=face(w=8, chin=104, jaw=8), face_side=face_side(chin=4, jaw=6), nose=(50, 84, 4.4),
    hairline=[(6, 58), (14, 52), (50, 50), (86, 52), (94, 58)], ear_out=8),
  [L(outline([(-10, 52), (-6, 30, 1), (4, 20), (8, 4, 1), (22, 6), (30, -8, 1), (42, 0), (50, -12, 1), (58, 0), (70, -8, 1), (78, 6), (92, 4, 1), (96, 20), (106, 30, 1), (110, 52), (50, 58)])),
   L(outline([(-10, 52), (50, 44), (110, 52), (106, 58), (50, 54), (-6, 58)]), 'shade', 'f', False),
   L(ell(50, 84, 4.4, 4), _c('#c83a30'), 'f', True), L(quad((38, 98), (50, 92), (62, 98)), OUTC, 'f', False, False, 1.8)] +
  [L([(50, 4), (50 + k * 14, 46)], 'shade', 'b', False, False, 0.8) for k in (-3, -2, -1, 1, 2, 3)],
  [L(outline([(-6, 54), (0, 20, 1), (20, 10), (40, -10, 1), (60, 0), (84, -6, 1), (90, 20), (104, 40, 1), (100, 56), (60, 54)])), L(ell(92, 84, 4, 4), _c('#c83a30'), 'f', True)],
  [L(outline([(-10, 52), (-6, 30, 1), (4, 20), (8, 4, 1), (22, 6), (30, -8, 1), (42, 0), (50, -12, 1), (58, 0), (70, -8, 1), (78, 6), (92, 4, 1), (96, 20), (106, 30, 1), (110, 52), (50, 60)]))])

# Perpetua Naim: melena morada larga que le enmarca la cara como una capucha, con un rizo en el centro de la frente; ojos
# grandes con pestañas y la boca seria
C('perpetua-petname-naim', 'chica', P('#62476d', '#fbcfa0', iris='#6a3a2a'),
  F(eyes='normal', brows=False, mouth='frown', mouth_y=95, hairline=[(6, 76), (16, 56), (28, 48), (42, 56), (50, 64), (58, 56), (72, 48), (84, 56), (94, 76)]),
  dome('front', top=0, w=48, cy=46, long=108, flare=6) + [L(ell(50, 58, 4, 4), 'mid', 'f'), L(ell(50, 58, 1.6, 1.6), 'shade', 'f', False)],
  dome('side', top=0, w=48, cy=46, long=106, flare=6, fr=58),
  dome('back', top=0, w=48, cy=46, long=106, flare=6, ends=3))

# Philip Stic (portero): turbante alto rojo como un cilindro con una cinta dorada; cara larguísima morena, ojos afilados
# con pestañas, nariz larga y la boca ondulada
TUR, GLD = _c('#cf4156'), _c('#d8a848')
def _turban(view):
    if view == 'front':
        return [L(outline([(16, 46), (14, -4), (30, -24), (60, -28), (82, -20), (86, 0), (84, 46)]), TUR),
                L(outline([(14, 40), (86, 40), (86, 48), (14, 48)]), GLD, 'f', True, True),
                L(quad((18, 10), (50, -2), (84, 20)), _c('#a83040'), 'b', False, False, 1.6), L(quad((18, -6), (50, -20), (82, -2)), _c('#a83040'), 'b', False, False, 1.6)]
    if view == 'side':
        return [L(outline([(10, 50), (8, -4), (28, -26), (62, -28), (86, -16), (90, 44)]), TUR), L(outline([(8, 44), (90, 40), (90, 48), (8, 52)]), GLD, 'f', True, True)]
    return [L(outline([(14, 52), (14, -4), (30, -24), (60, -28), (82, -20), (86, 0), (86, 52)]), TUR), L(outline([(14, 46), (86, 46), (86, 54), (14, 54)]), GLD, 'f', True, True)]
C('philip-stic', 'delgado', P('#2a2020', '#eca663', iris='#1e1e1e'),
  F(eyes='sharp', brows=False, mouth='none', hairline=False, face_front=face(chin=114, jaw=-2), face_side=face_side(chin=12, nose=6), nose=(50, 90, 3), big_ears=2, ear_out=4),
  _turban('front') + [L([(42, 102), (46, 100), (50, 102), (54, 100), (58, 102)], OUTC, 'f', False, False, 1.4)],
  _turban('side'), _turban('back'))

# Philippa Belle: melena castaño granate ondulada hasta el pecho con dos horquillas amarillas; un ojo amarillo abierto y el
# otro guiñado, y una sonrisa
YCL = _c('#e8c840')
C('philippa-pippa-belle', 'chica', P('#6b4652', '#eedfc0', iris='#c8b030'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=94, hairline=[(6, 70), (16, 52), (30, 46), (44, 52), (58, 46), (74, 50), (86, 54), (94, 70)]),
  dome('front', top=0, w=48, cy=46, n=6, amp=6, soft=True, seed=73, long=104, flare=12) +
  [L(outline([(60, 22), (74, 18), (74, 24), (60, 28)]), YCL, 'f', True, True), L(outline([(62, 32), (76, 28), (76, 34), (62, 38)]), YCL, 'f', True, True),
   L(ell(36, 75, 7, 7), 'skin', 'f', False), L(quad((30, 75), (36, 70), (42, 75)), OUTC, 'f', False, False, 2.0)],
  dome('side', top=0, w=48, cy=46, n=6, amp=6, soft=True, seed=73, long=102, flare=12, fr=56) + [L(outline([(66, 24), (80, 20), (80, 26), (66, 30)]), YCL, 'f', True, True)],
  dome('back', top=0, w=48, cy=46, n=6, amp=6, soft=True, seed=73, long=102, flare=12, ends=4))

# Phoenix Southers: pelo rojo en llamas hacia arriba con dos llamas doradas a los lados de la cara, pintura roja y amarilla
# alrededor de los ojos, ojos verdes afilados y sonrisa de dientes
GLDF, RDP = _c('#f0b030'), _c('#d83020')
C('phoenix-firebird-southers', 'normal', P('#e0352f', '#eeae62', iris='#3a8a4a', shade='#b02a20'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=96, face_front=face(chin=104), hairline=[(6, 60), (18, 48), (30, 54), (40, 44), (52, 52), (62, 42), (74, 50), (84, 46), (94, 60)]),
  [L(outline([(16, 56), (2, 30, 1), (10, 44), (6, 20, 1), (20, 40), (22, 70)]), GLDF), L(outline([(84, 56), (98, 30, 1), (90, 44), (94, 20, 1), (80, 40), (78, 70)]), GLDF)] +
  dome('front', top=-12, w=40, cy=40, n=6, amp=16, sweep=0.3, seed=74, sb=56) +
  [L(outline([(20, 64), (44, 68), (44, 71), (22, 69)]), RDP, 'f', False), L(outline([(80, 64), (56, 68), (56, 71), (78, 69)]), RDP, 'f', False),
   L(outline([(20, 78), (30, 84), (26, 96, 1)]), GLDF, 'f', False), L(outline([(80, 78), (70, 84), (74, 96, 1)]), GLDF, 'f', False)],
  [L(outline([(40, 56), (30, 30, 1), (36, 44), (40, 20, 1), (50, 42), (54, 70)]), GLDF)] + dome('side', top=-12, w=40, cy=40, n=6, amp=16, sweep=0.3, seed=74, nape=78, fr=46),
  [L(outline([(16, 56), (2, 30, 1), (10, 44), (6, 20, 1), (20, 40), (22, 70)]), GLDF), L(outline([(84, 56), (98, 30, 1), (90, 44), (94, 20, 1), (80, 40), (78, 70)]), GLDF)] +
  dome('back', top=-12, w=40, cy=40, n=6, amp=16, sweep=0.3, seed=74, nape=78))

# Piero Mantisse: cabeza de mantis, un casco de pelo verde en capas con dos grandes ojos rojos encima a los lados; piel
# clara, ojos rojos, unas lágrimas negras pintadas y la boca seria
MAN, MANR = _c('#94a96b'), _c('#ba333a')
C('piero-mantisse', 'normal', P('#94a96b', '#e6d4b9', iris='#c0302a', shade='#707249'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=94, hairline=[(6, 70), (16, 58), (28, 64), (38, 52), (50, 58), (62, 52), (72, 64), (84, 58), (94, 70)]),
  dome('front', top=4, w=50, cy=48, n=6, amp=6, soft=True, seed=75, long=90, flare=8) +
  [L(blob([(6, 14), (-2, -14), (20, -24), (40, -8), (32, 14)], 6), MANR, 'f'), L(blob([(94, 14), (102, -14), (80, -24), (60, -8), (68, 14)], 6), MANR, 'f'),
   L(ell(20, 0, 5, 6), BLACK, 'f', False), L(ell(80, 0, 5, 6), BLACK, 'f', False),
   L([(30, 82), (30, 92)], OUTC, 'f', False, False, 1.2), L([(70, 82), (70, 92)], OUTC, 'f', False, False, 1.2)],
  dome('side', top=4, w=50, cy=48, n=6, amp=6, soft=True, seed=75, long=88, flare=8, fr=56) + [L(blob([(46, 14), (40, -14), (62, -24), (80, -8), (70, 14)], 6), MANR, 'f')],
  dome('back', top=4, w=50, cy=48, n=6, amp=6, soft=True, seed=75, long=88, flare=8, ends=4) +
  [L(blob([(6, 14), (-2, -14), (20, -24), (40, -8), (32, 14)], 6), MANR, 'f'), L(blob([(94, 14), (102, -14), (80, -24), (60, -8), (68, 14)], 6), MANR, 'f')])

# Pinkie Harte: casco rosa con unas gafas de corazón encima, el pelo blanco a los lados, un flequillo verde menta y una
# bufanda rosa; un corazón pintado en la mejilla, ojos verde agua y sonrisa
PNK, PNKD, MNT = _c('#e8a0b0'), _c('#d28593'), _c('#9cd59e')
def _heart(cx, cy, r, c):
    return L(blob([(cx, cy + r), (cx - r, cy - r * 0.1), (cx - r * 0.6, cy - r * 0.9), (cx, cy - r * 0.4), (cx + r * 0.6, cy - r * 0.9), (cx + r, cy - r * 0.1)], 4), c, 'f', True, True)
C('pinkie-harte', 'chica', P('#f0ecec', '#f6cabb', iris='#4aa8a8'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=94, hairline=[(6, 70), (18, 58), (40, 52), (50, 60), (60, 52), (82, 58), (94, 70)]),
  [L(outline([(10, 50), (6, 90), (20, 90), (22, 60)])), L(outline([(90, 50), (94, 90), (80, 90), (78, 60)]))] +
  [L(outline([(6, 56), (8, 26), (26, 8), (50, 2), (74, 8), (92, 26), (94, 56), (50, 50)]), PNK),
   L(blob([(40, 40), (50, 36), (60, 40), (58, 56), (50, 62), (42, 56)], 6), MNT, 'f'),
   _heart(32, 20, 11, _c('#f06a8a')), _heart(68, 20, 11, _c('#f06a8a')), _heart(32, 20, 6, MNT), _heart(68, 20, 6, MNT),
   _heart(72, 88, 4, _c('#e86a8a')),
   L(outline([(16, 98), (50, 106), (84, 98), (96, 80), (104, 70, 1), (96, 100), (84, 110), (50, 116), (16, 108)]), PNKD, 'f')],
  [L(outline([(4, 64), (6, 26), (26, 6), (60, 2), (86, 14), (96, 40), (90, 56), (60, 56), (40, 70)]), PNK), _heart(60, 16, 9, _c('#f06a8a')),
   L(outline([(30, 50), (40, 96), (26, 100), (20, 60)]))],
  [L(outline([(6, 70), (8, 26), (26, 8), (50, 2), (74, 8), (92, 26), (94, 70), (50, 76)]), PNK), L(outline([(16, 70), (84, 70), (80, 94), (20, 94)])),
   L(outline([(70, 90), (96, 70), (104, 110, 1), (86, 96)]), PNKD, 'f')])

# Plato Mail: kabuto rojo de samurái con una media luna dorada encima y una máscara oscura que le tapa la cara por debajo de
# los ojos; solo se le ven los ojos, blancos y enfadados
KAB, MEN, GLD2 = _c('#b63343'), _c('#4f4553'), _c('#c8a048')
def _samurai(view):
    if view == 'front':
        return [L(quad((10, -16), (50, 36), (90, -16)), GLD2, 'f', False, False, 6.0),
                L(outline([(4, 80), (-2, 60), (10, 50), (12, 26), (30, 12), (50, 8), (70, 12), (88, 26), (90, 50), (102, 60), (96, 80), (84, 70), (16, 70)]), KAB),
                L(outline([(10, 50), (24, 56), (24, 74), (10, 78)]), MEN, 'f', True), L(outline([(90, 50), (76, 56), (76, 74), (90, 78)]), MEN, 'f', True),
                L(outline([(16, 80), (36, 82), (50, 78), (64, 82), (84, 80), (82, 100), (60, 112), (50, 116), (40, 112), (18, 100)]), MEN, 'f', True)]
    if view == 'side':
        return [L(quad((40, 6), (60, 30), (80, 0)), GLD2, 'b', False, False, 5.0),
                L(outline([(2, 86), (4, 50), (14, 24), (40, 8), (70, 12), (88, 28), (92, 50), (60, 60), (40, 80)]), KAB),
                L(outline([(64, 80), (92, 80), (94, 100), (72, 108)]), MEN, 'f', True)]
    return [L(quad((10, 6), (50, 44), (90, 6)), GLD2, 'b', False, False, 6.0),
            L(outline([(4, 86), (-2, 60), (10, 50), (12, 26), (30, 12), (50, 8), (70, 12), (88, 26), (90, 50), (102, 60), (96, 86), (50, 92)]), KAB)]
C('plato-mail', 'normal', P('#3b3238', '#c2a057', iris='#1e1e1e'),
  F(eyes='sharp', brows='angry', mouth='none', hairline=False, ears=False),
  _samurai('front'), _samurai('side'), _samurai('back'))

# Pontius Blank: gorro de aviador marrón con orejeras que le tapan los lados de la cara; cara ancha naranja, cejas gruesas
# fruncidas, ojos cerrados y la boca enfadada
TRP, TRPD = _c('#957957'), _c('#5a4733')
def _trapper(view):
    if view == 'front':
        return [L(outline([(6, 50), (8, 26), (24, 8), (50, 2), (76, 8), (92, 26), (94, 50), (50, 46)]), TRP),
                L(outline([(4, 40), (50, 36), (96, 40), (96, 50), (50, 46), (4, 50)]), TRPD, 'f', True, True),
                L(outline([(4, 50), (18, 52), (20, 96), (8, 104), (2, 80)]), TRP, 'f', True), L(outline([(96, 50), (82, 52), (80, 96), (92, 104), (98, 80)]), TRP, 'f', True)]
    if view == 'side':
        return [L(outline([(4, 60), (8, 26), (26, 6), (60, 2), (86, 14), (96, 40), (92, 50), (50, 50)]), TRP),
                L(outline([(4, 42), (94, 38), (94, 48), (4, 52)]), TRPD, 'f', True, True), L(outline([(30, 50), (54, 50), (56, 100), (34, 104)]), TRP, 'f', True)]
    return [L(outline([(4, 100), (6, 26), (24, 8), (50, 2), (76, 8), (94, 26), (96, 100), (50, 96)]), TRP), L(outline([(4, 44), (96, 44), (96, 54), (4, 54)]), TRPD, 'f', True, True)]
C('pontius-blank', 'corpulento', P('#363029', '#fcc271', iris='#1e1e1e'),
  F(eyes='closed', brows=False, mouth='none', hairline=False, ears=False, face_front=face(w=4, chin=108, jaw=4), face_side=face_side(chin=6, jaw=4), nose=(50, 84, 3)),
  _trapper('front') + [L([(28, 64), (44, 70)], OUTC, 'f', False, False, 4.0), L([(72, 64), (56, 70)], OUTC, 'f', False, False, 4.0),
  L(quad((36, 100), (50, 92), (64, 100)), OUTC, 'f', False, False, 2.0)],
  _trapper('side'), _trapper('back'))

# Posy Striker: pelo azul peinado hacia atrás con un mechón largo que le cae por un lado y se riza hasta el pecho; unas gafas
# rojas de visera sobre los ojos y la boca seria
VIS = _c('#d8303a')
C('posy-striker', 'chica', P('#485c8a', '#fdf0d8', iris='#1e1e1e', shade='#3f4f75'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=95, hairline=[(6, 62), (18, 48), (34, 40), (50, 40), (66, 40), (82, 48), (94, 62)]),
  dome('front', top=0, w=46, cy=44, sb=62) +
  [L(outline([(62, 6), (80, 24), (82, 70), (80, 104), (70, 116, 1), (74, 96), (72, 60), (64, 30)]), 'mid', 'f'),
   L(outline([(16, 66), (50, 70), (84, 66), (80, 80), (60, 78), (50, 82), (40, 78), (20, 80)]), VIS, 'f', True)],
  dome('side', top=0, w=46, cy=44, nape=82, fr=44) + [L(outline([(66, 68), (94, 66), (92, 80), (68, 80)]), VIS, 'f', True)],
  dome('back', top=0, w=46, cy=44, nape=82) + [L(outline([(26, 40), (20, 80), (24, 112, 1), (32, 80), (34, 50)]))])

# Precious Cryan: media melena granate con flequillo recto y la parte de arriba rosa con forma de corazón; ojos castaños y
# sonrisa
PKT = _c('#d88d8f')
C('precious-cryan', 'chica', P('#6f3c4a', '#f9dcc4', iris='#8a4a3a'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=94, hairline=[(6, 74), (18, 60), (50, 60), (82, 60), (94, 74)]),
  dome('front', top=2, w=46, cy=46, long=100, flare=2) + [L(blob([(30, 16), (50, 24), (70, 16), (74, 8), (50, 0), (26, 8)], 4), PKT, 'b', False),
  L(outline([(40, 22), (50, 30), (60, 22)]), PKT, 'b', False)],
  dome('side', top=2, w=46, cy=46, long=98, flare=2, fr=60) + [L(blob([(30, 10), (60, 6), (74, 20), (50, 22)], 4), PKT, 'b', False)],
  dome('back', top=2, w=46, cy=46, long=98, flare=2, ends=0) + [L(blob([(30, 16), (50, 24), (70, 16), (74, 8), (50, 0), (26, 8)], 4), PKT, 'b', False)])

# Preston Digitate (portero): afro castaño enorme con un sombrerito de copa azul marino con una banda roja y blanca; una cara
# extraña de nariz larga en punta, dos círculos naranjas por ojos y una sonrisa
NAVY, RDB = _c('#2a2a50'), _c('#c8303a')
C('preston-digitate', 'normal', P('#723f26', '#f7d7af', shade='#5e2618'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=96, mouth_w=12, hairline=[(6, 62), (16, 56), (34, 54), (50, 58), (66, 54), (84, 56), (94, 62)]),
  dome('front', top=4, w=56, cy=46, n=10, amp=6, soft=True, seed=76, sb=80) +
  [L(outline([(28, 10), (30, -14), (70, -14), (72, 10)]), NAVY, 'f'), L(outline([(29, 0), (71, 0), (71, 6), (29, 6)]), RDB, 'f', False),
   L(outline([(16, 12), (84, 12), (80, 18), (20, 18)]), NAVY, 'f'),
   L(ell(32, 74, 6, 6), _c('#e8602a'), 'f', True), L(ell(68, 74, 6, 6), _c('#e8602a'), 'f', True),
   L(outline([(46, 60), (54, 60), (50, 90)]), _c('#e8b890'), 'f', True, True),
   L(quad((38, 96), (50, 100), (62, 96)), OUTC, 'f', False, False, 1.4)],
  dome('side', top=4, w=54, cy=46, n=10, amp=6, soft=True, seed=76, nape=88, fr=56) + [L(outline([(40, 8), (42, -14), (76, -14), (78, 8)]), NAVY, 'f'), L(outline([(24, 10), (90, 10), (88, 16), (26, 16)]), NAVY, 'f')],
  dome('back', top=4, w=56, cy=46, n=10, amp=6, soft=True, seed=76, nape=88) + [L(outline([(28, 10), (30, -14), (70, -14), (72, 10)]), NAVY, 'f'), L(outline([(16, 12), (84, 12), (80, 18), (20, 18)]), NAVY, 'f')])

# Price Shaids (portero): pelo blanco crema peinado hacia arriba en un tupé alto con los lados abombados; piel morena, cara
# de mandíbula grande, gafas de sol azul oscuro de montura amarilla y una sonrisa de dientes
SHD, YFR = _c('#2f4351'), _c('#e0c040')
C('price-shaids', 'corpulento', P('#e2ded4', '#cd9568', iris='#1e1e1e', shade='#b8b0a4'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=98, mouth_w=12, face_front=face(w=6, chin=108, jaw=8), face_side=face_side(chin=6, jaw=6), nose=(50, 86, 3.4),
    hairline=[(6, 60), (18, 46), (34, 40), (50, 42), (66, 40), (82, 46), (94, 60)]),
  [L(outline([(8, 60), (2, 80), (10, 96), (22, 84), (22, 62)])), L(outline([(92, 60), (98, 80), (90, 96), (78, 84), (78, 62)]))] +
  [L(outline([(16, 62), (14, 34), (24, 10), (40, -2), (56, -8, 1), (64, 2), (80, 10), (88, 34), (84, 62), (78, 46), (22, 46)])),
   L(outline([(60, -6), (80, 10), (88, 34), (84, 58), (74, 30)]), 'shade', 'b', False),
   L(outline([(18, 68), (46, 66), (54, 66), (82, 68), (78, 80), (56, 78), (44, 78), (22, 80)]), SHD, 'f', True),
   L([(18, 68), (82, 68)], YFR, 'f', False, False, 2.0)],
  [L(outline([(54, 62), (58, 48), (80, 42), (88, 26), (70, 6), (56, -6, 1), (40, 0), (16, 10), (6, 34), (8, 60), (14, 84), (26, 92), (40, 78), (50, 72)])),
   L(outline([(68, 68), (92, 68), (92, 80), (70, 80)]), SHD, 'f', True)],
  [L(outline([(10, 92), (12, 34), (24, 10), (40, -2), (56, -8, 1), (64, 2), (80, 10), (88, 34), (90, 92), (50, 86)]))])

# Primrose Proppa: pelo verde salvia con flequillo recto y un mechón largo por un lado hasta el cuello; piel clara, ojos
# rojizos con pestañas y ojeras, y la boca seria
C('primrose-proppa', 'chica', P('#7e8b6e', '#f2dfc7', iris='#a84a4a', shade='#5a6650'),
  F(eyes='normal', brows=False, mouth='frown', mouth_y=95, hairline=[(6, 72), (18, 62), (50, 62), (82, 62), (94, 72)]),
  dome('front', top=2, w=46, cy=46, sb=72) + [L(outline([(80, 54), (92, 60), (90, 96), (80, 112, 1), (82, 90)]), 'mid', 'f'),
  L(quad((26, 84), (34, 88), (42, 84)), _c('#b89a90'), 'f', False, False, 1.0), L(quad((58, 84), (66, 88), (74, 84)), _c('#b89a90'), 'f', False, False, 1.0)],
  dome('side', top=2, w=46, cy=46, nape=84, fr=62) + [L(outline([(70, 56), (82, 60), (80, 100), (72, 112, 1), (70, 84)]), 'mid', 'f')],
  dome('back', top=2, w=46, cy=46, nape=84) + [L(outline([(16, 60), (8, 96), (14, 112, 1), (24, 90), (26, 66)]))])

# Prosper Cooka: pelo gris oscuro de luchador de sumo, con un moñito encima y los lados abiertos en alas; piel morena, ojos
# entornados, labios gruesos apretados y una gola blanca al cuello
RUFF = _c('#f0ece4')
C('prosper-cooka', 'corpulento', P('#4a433e', '#cd966b', iris='#1e1e1e'),
  F(eyes='closed', brows='angry', mouth='lips', mouth_y=94, mouth_w=10, face_front=face(w=8, chin=104, jaw=6), face_side=face_side(chin=4, jaw=6), nose=(50, 84, 3.4), ear_out=8,
    hairline=[(6, 56), (16, 50), (34, 46), (50, 48), (66, 46), (84, 50), (94, 56)]),
  [L(outline([(10, 64), (-10, 40, 1), (16, 30), (30, 18), (50, 14), (70, 18), (84, 30), (110, 40, 1), (90, 64), (80, 50), (20, 50)])),
   L(ell(50, 6, 8, 7)), L(outline([(44, 12), (56, 12), (54, 18), (46, 18)]), 'deep', 'f', False),
   L(outline([(14, 100), (24, 108), (34, 102), (44, 110), (56, 110), (66, 102), (76, 108), (86, 100), (88, 112), (50, 122), (12, 112)]), RUFF, 'f', True, True)],
  [L(outline([(54, 58), (58, 46), (80, 40), (88, 28), (70, 16), (40, 14), (16, 22), (4, 40), (-6, 60, 1), (14, 64), (30, 70), (50, 66)])), L(ell(46, 6, 8, 7))],
  [L(outline([(10, 70), (-10, 44, 1), (16, 30), (30, 18), (50, 14), (70, 18), (84, 30), (110, 44, 1), (90, 70), (50, 76)])), L(ell(50, 6, 8, 7))])

# Prue Scription: cofia rosa de enfermera grande, pelo castaño oliva echado a un lado con dos mechones que caen junto a las
# mejillas; gafas rojas rectangulares, ojos verdes afilados, boquita en o y un lunar
NUR, NURD = _c('#e8909a'), _c('#c87078')
C('prue-scription', 'chica', P('#9b762e', '#fbc3ab', iris='#4a8a3a'),
  F(eyes='sharp', brows='angry', mouth='none', glasses=_c('#d03030'), glasses_rect=True,
    hairline=[(6, 66), (18, 52), (30, 44), (44, 40), (60, 50), (76, 58), (86, 60), (94, 66)]),
  [L(outline([(-2, 46), (4, 14), (24, -4), (50, -8), (76, -4), (96, 14), (102, 46), (80, 30), (50, 26), (20, 30)]), NUR)] +
  dome('front', top=10, w=44, cy=46, sb=62) +
  [L(outline([(14, 60), (22, 62), (20, 96), (14, 104, 1), (12, 80)]), 'mid', 'f'), L(outline([(86, 60), (78, 62), (80, 96), (86, 104, 1), (88, 80)]), 'mid', 'f'),
   L(outline([(20, 40), (40, 24), (64, 30), (56, 46), (40, 50)]), 'mid', 'f'),
   L(ell(50, 96, 1.8, 2.2), _c('#a03a3a'), 'f', False), mole(56, 102)],
  [L(outline([(-2, 54), (4, 16), (30, -4), (60, -6), (88, 4), (100, 28), (76, 30), (40, 34), (10, 50)]), NUR)] + dome('side', top=10, w=44, cy=46, nape=82, fr=48),
  [L(outline([(-2, 46), (4, 14), (24, -4), (50, -8), (76, -4), (96, 14), (102, 46), (50, 40)]), NUR)] + dome('back', top=10, w=44, cy=46, nape=82))
