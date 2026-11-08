"""Ojeadores de Victory Road (scouts-vr), tanda 06: dibujados a partir de su retrato; claves 'scouts-vr:<id>'.

Casi ninguno tiene modelo 3D (Lumina sí): el frente sale del retrato y el perfil y la espalda se deducen del peinado.
Usa dome()/hl()/face()/face_side()/F()/P()/mark()/horn() de chars_scouts_ie1_09; aquí, unas ayudas para coletas,
trenzas, moños y cintas."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401
from chars_scouts_ie1_09 import F, P, _c, dome, face, face_side, hl, horn, mark  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)


def C(pid, body, palette, f, front, side, back):
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        # el nacimiento del pelo baja por el borde de la cara: así su raya no cruza el pelo de los lados
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[f'scouts-vr:{pid}'] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def tail(x, y, dx, ln, w=12, c='mid', z='b'):
    """Coleta que sale de (x, y) y cae hacia dx (lado) con largo ln."""
    s = 1 if dx >= 0 else -1
    return L(outline([(x - s * 2, y - w * 0.5), (x + dx * 0.6 + s * w, y + ln * 0.25), (x + dx + s * w * 0.4, y + ln * 0.7),
                      (x + dx, y + ln, 1), (x + dx * 0.5 - s * w * 0.3, y + ln * 0.6), (x - s * 2, y + w * 0.6)]), c, z)


def braid(pts, c='mid', z='b', r=5):
    """Trenza: bolitas a lo largo de la línea."""
    out = []
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        for t in (0.0, 0.5):
            out.append(L(ell(x0 + (x1 - x0) * t, y0 + (y1 - y0) * t, r, r * 0.85), c, z))
    out.append(L(ell(*pts[-1], r, r * 0.85), c, z))
    return out


def bun(x, y, r, c='mid', z='b'):
    return L(ell(x, y, r, r), c, z)


def band(y0, y1, c, view='front'):
    """Cinta del pelo: de frente cruza la cabeza; de perfil y de espaldas, una franja."""
    if view == 'front':
        return L(outline([(6, y1 + 6), (10, y0 + 2), (50, y0 - 6), (90, y0 + 2), (94, y1 + 6), (88, y1 + 2), (50, y1 - 6), (12, y1 + 2)]), c, 'f', False)
    if view == 'side':
        return L(outline([(8, y1 + 4), (6, y0 + 6), (50, y0 - 4), (92, y0 + 6), (90, y1 + 2), (50, y1 - 4)]), c, 'f', False)
    return L(outline([(6, y1 + 6), (8, y0 + 4), (50, y0 - 4), (92, y0 + 4), (94, y1 + 6), (50, y1 - 2)]), c, 'f', False)


def blush(c='#f0a0a0'):
    return [mark([(24, 82), (34, 80), (34, 86), (24, 87)], _c(c)), mark([(76, 82), (66, 80), (66, 86), (76, 87)], _c(c))]


def shadow_eyes(c):
    """Sombra de ojos (pintura sobre los párpados)."""
    return [L([(26, 70), (40, 68)], _c(c), 'f', False, False, 2.2), L([(74, 70), (60, 68)], _c(c), 'f', False, False, 2.2)]


# Kyle Flaggard: piel oscura, pelo cortito rojo anaranjado con la parte de arriba verde en llamas; ojos verdes y ceño
GRN = _c('#5a7a3a')
C('kyle-flaggard', 'normal', P('#d0603a', '#8a5a3a', iris='#6a8a5a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=hl(6, 64, 44, 52, jit=2, seed=3)),
  dome('front', top=6, w=44, cy=46, sb=64) + [L(outline([(16, 40), (22, 22), (30, 30), (38, 14, 1), (46, 26), (54, 12, 1), (60, 26), (68, 16, 1),
                                                         (72, 30), (80, 22, 1), (84, 40), (70, 34), (50, 38), (30, 34)]), GRN, 'f')],
  dome('side', top=6, w=44, cy=46, nape=82, fr=50) + [L(outline([(30, 20), (44, 4, 1), (52, 16), (66, 6, 1), (70, 20), (84, 16, 1), (86, 34), (60, 30), (34, 30)]), GRN, 'f')],
  dome('back', top=6, w=44, cy=46, nape=82) + [L(outline([(20, 30), (34, 12, 1), (44, 22), (56, 10, 1), (62, 22), (76, 12, 1), (82, 30), (50, 34)]), GRN, 'f')])

# Lace Tangler: pelo gris lavanda con flequillo recto y dos coletas altas abultadas a los lados; ojos morados grandes
C('lace-tangler', 'chica', P('#9a9ab8', '#f6dcd0', iris='#8a4a8a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 70), (16, 52), (30, 50), (50, 50), (70, 50), (84, 52), (94, 70)]),
  [tail(12, 14, -16, 64, 16), tail(88, 14, 16, 64, 16)] + dome('front', top=4, w=46, cy=46, sb=70) +
  [L(outline([(20, 40), (36, 32), (64, 32), (80, 40), (82, 56), (18, 56)]), 'mid', 'f'), L([(40, 56), (40, 48)], 'deep', 'f', False, False, 1.0),
   L([(60, 56), (60, 48)], 'deep', 'f', False, False, 1.0)] + blush(),
  [tail(30, 12, -26, 64, 16)] + dome('side', top=4, w=46, cy=46, nape=84, fr=56),
  [tail(14, 14, -16, 64, 16), tail(86, 14, 16, 64, 16)] + dome('back', top=4, w=46, cy=46, nape=84))

# Lacie Pawford: media melena gris oscuro en campana, abierta hacia fuera abajo; horquilla turquesa, mofletes rosas, ceño
C('lacie-pawford', 'chica', P('#555550', '#f6d8c8', iris='#4a4a40'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=94, face_front=face(w=2), hairline=[(6, 66), (18, 48), (34, 42), (52, 50), (70, 42), (84, 48), (94, 66)]),
  dome('front', top=4, w=46, cy=46, long=84, flare=16) + blush() + [L(outline([(26, 44), (32, 42), (34, 48), (28, 50)]), _c('#3ac8c0'), 'f', False)],
  dome('side', top=4, w=46, cy=46, long=82, flare=16, fr=56),
  dome('back', top=4, w=46, cy=46, long=82, flare=16, ends=0))

# Landon Crosser: pelo rojo en casco con un mechón en gancho arriba y un rizo rojo vivo; marcas naranjas en las mejillas
RED = _c('#e83a3a')
C('landon-crosser', 'normal', P('#a82a2a', '#f0b880', iris='#6a4a3a'),
  F(eyes='big', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 66), (16, 50), (30, 46), (46, 54), (60, 44), (76, 46), (86, 52), (94, 66)]),
  dome('front', top=4, w=46, cy=46, sb=66) + [L(outline([(44, 6), (40, -10), (52, -18, 1), (48, -6), (52, 4)])),
  L(outline([(54, 20), (72, 22), (76, 40), (66, 52, 1), (70, 38), (60, 30)]), RED, 'f')] + blush('#f0a050'),
  dome('side', top=4, w=46, cy=46, nape=84, fr=54) + [L(outline([(44, 6), (42, -10), (54, -18, 1), (50, -6), (54, 4)]))],
  dome('back', top=4, w=46, cy=46, nape=84) + [L(outline([(44, 6), (40, -10), (52, -18, 1), (48, -6), (52, 4)]))])

# Landric Delphin: piel oscura, pelo gris lavanda peinado hacia atrás con mechones que le caen a los lados hasta el
# cuello; ojos amarillos afilados y media sonrisa
C('landric-delphin', 'delgado', P('#9aa0c0', '#8a5038', iris='#c8b040'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=95, face_front=face(chin=104), face_side=face_side(chin=4), hairline=[(6, 60), (20, 46), (50, 40), (80, 46), (94, 60)]),
  dome('front', top=4, w=44, cy=44, sb=60) + [L(outline([(10, 50), (4, 70), (12, 96, 1), (18, 74), (20, 58)])), L(outline([(90, 50), (96, 70), (88, 96, 1), (82, 74), (80, 58)])),
  strand([(30, 40), (40, 14)], 'deep', 'b', 1.0), strand([(70, 40), (60, 14)], 'deep', 'b', 1.0)],
  dome('side', top=4, w=44, cy=44, long=96, flare=4, fr=44),
  dome('back', top=4, w=44, cy=44, long=94, flare=4, ends=4))

# Laurence Stumbleton: media melena verde azulado hasta la barbilla, cinta naranja ancha; cejas gruesas en pico y boca ondulada
C('laurence-stumbleton', 'normal', P('#2a8a8a', '#f6d0a0', iris='#2a2a40'),
  F(eyes='round', brows='angry', mouth='line', mouth_y=95, face_front=face(w=4, chin=104), hairline=[(6, 60), (22, 44), (44, 40), (50, 46), (56, 40), (78, 44), (94, 60)]),
  dome('front', top=6, w=48, cy=46, long=88, flare=8) + [band(22, 32, _c('#d8703a'))],
  dome('side', top=6, w=48, cy=46, long=86, flare=8, fr=48) + [band(22, 32, _c('#d8703a'), 'side')],
  dome('back', top=6, w=48, cy=46, long=86, flare=8, ends=3) + [band(22, 32, _c('#d8703a'), 'back')])

# Lawton Dappermann: pelo castaño grisáceo rizado en forma de seta, que tapa las orejas; ojos redondos y gesto serio
C('lawton-dappermann', 'normal', P('#6a625a', '#f6d0a8', iris='#3a3060'),
  F(eyes='round', brows=True, mouth='frown', mouth_y=94, ears=False, hairline=[(6, 70), (16, 54), (32, 50), (50, 52), (68, 50), (84, 54), (94, 70)]),
  dome('front', top=2, w=54, cy=44, n=12, amp=5, seed=7, soft=True, sb=78),
  dome('side', top=2, w=52, cy=44, n=12, amp=5, seed=7, soft=True, nape=86, fr=54),
  dome('back', top=2, w=54, cy=44, n=12, amp=5, seed=7, soft=True, nape=86))

# Lazaro Coveton: piel muy clara, pelo lavanda que sube en llama hacia arriba; ojos cerrados apretados, cejas lilas y orejas grandes
C('lazaro-coveton', 'normal', P('#a080c0', '#f6dcd8', iris='#3a3040'),
  F(eyes='closed', brows='angry', mouth='frown', mouth_y=94, big_ears=2, face_front=face(chin=104), hairline=[(6, 56), (24, 44), (50, 38), (76, 44), (94, 56)]),
  [L(outline([(18, 50), (14, 30), (24, 8), (34, 0), (42, -14, 1), (48, -2), (56, -16, 1), (62, 0), (74, 6), (86, 28), (82, 50), (50, 44)])),
   L(outline([(56, -8), (74, 6), (86, 28), (82, 48), (70, 22)]), 'shade', 'b', False), L(outline([(40, 0), (48, -12), (52, 10), (46, 22)]), 'light', 'b', False)],
  [L(outline([(54, 54), (62, 44), (82, 38), (88, 20), (72, 0), (60, -16, 1), (52, 0), (34, -6, 1), (30, 8), (12, 18), (6, 40), (12, 60), (28, 66), (46, 62)]))],
  [L(outline([(18, 70), (14, 30), (24, 8), (42, -14, 1), (56, -16, 1), (76, 6), (86, 30), (82, 70), (50, 76)]))])

# Leander Courtman: pelo castaño corto, cinta roja ancha en la frente; cejas gruesas, ojos castaños y una sonrisa enorme
C('leander-courtman', 'normal', P('#8a5a2a', '#f6c8a0', iris='#6a4020'),
  F(eyes='round', brows='angry', mouth='grin', mouth_y=95, face_front=face(w=4), hairline=[(6, 58), (18, 46), (50, 44), (82, 46), (94, 58)]),
  dome('front', top=6, w=46, cy=46, n=9, amp=4, seed=5, sb=60) + [band(26, 40, _c('#c83030'))] + blush(),
  dome('side', top=6, w=46, cy=46, n=9, amp=4, seed=5, nape=80, fr=46) + [band(26, 40, _c('#c83030'), 'side')],
  dome('back', top=6, w=46, cy=46, n=9, amp=4, seed=5, nape=80) + [band(26, 40, _c('#c83030'), 'back')])

# Leero Pard: pelo verde menta muy claro en pinchos alborotados con mechas gris verdoso; ojos morados afilados y sonrisa pícara
C('leero-pard', 'normal', P('#b8d8c8', '#f6d0b0', iris='#6a4aa0', shade='#6a8a8a'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=95, face_front=face(chin=104), hairline=hl(5, 64, 44, 60, lean=2, jit=4, seed=11)),
  dome('front', top=-6, w=50, cy=42, n=11, amp=16, seed=13, sb=70) + [strand([(30, 30), (24, 10)], 'shade', 'b', 1.6), strand([(70, 30), (78, 8)], 'shade', 'b', 1.6)],
  dome('side', top=-6, w=50, cy=42, n=11, amp=16, seed=13, nape=86, fr=50),
  dome('back', top=-6, w=50, cy=42, n=11, amp=16, seed=13, nape=86))

# Lester Bawlund: casco de pelo castaño oscuro con la parte de arriba roja intensa; ojos redondos amarillentos y gesto serio
C('lester-bawlund', 'normal', P('#3a2020', '#f6d0b0', iris='#b0a060'),
  F(eyes='round', brows=True, mouth='frown', mouth_y=94, hairline=[(6, 70), (16, 52), (28, 44), (40, 54), (52, 44), (64, 54), (76, 44), (86, 52), (94, 70)]),
  dome('front', top=0, w=50, cy=44, sb=72) + [L(blob([(8, 36), (20, 6), (50, -2), (80, 6), (92, 36), (70, 28), (50, 26), (30, 28)], 8), _c('#b02030'), 'b', False)],
  dome('side', top=0, w=50, cy=44, nape=86, fr=54) + [L(blob([(2, 36), (14, 6), (46, -2), (84, 8), (94, 36), (60, 26), (30, 26)], 8), _c('#b02030'), 'b', False)],
  dome('back', top=0, w=50, cy=44, nape=86) + [L(blob([(6, 40), (20, 6), (50, -2), (80, 6), (94, 40), (50, 30)], 8), _c('#b02030'), 'b', False)])

# Leston Thoreau (portero): grandullón de cabeza ancha con el pelo gris rapado al cero, orejas grandes, cejas gruesas y ceño
C('leston-thoreau', 'corpulento', P('#b8c0c0', '#f6dcd0', iris='#3a3a50'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, big_ears=3, ear_out=6, face_front=face(w=8, chin=102, jaw=4),
    hairline=[(6, 58), (16, 46), (50, 38), (84, 46), (94, 58)]),
  dome('front', top=12, w=46, cy=48, sb=66, shade=False) + [L(outline([(16, 60), (22, 72), (16, 78)])), L(outline([(84, 60), (78, 72), (84, 78)]))],
  dome('side', top=12, w=44, cy=48, nape=80, fr=40, shade=False),
  dome('back', top=12, w=46, cy=48, nape=80, shade=False))

# Levy Vales (portero): melena castaña en seta enorme que le tapa los ojos casi del todo, ojos en espiral y boca ondulada
C('levy-vales', 'corpulento', P('#6a4a30', '#f6d8c0', iris='#3a3a3a'),
  F(eyes='round', brows=False, mouth='line', mouth_y=96, eye_y=80, ears=False, face_front=face(w=8, chin=102, jaw=6), hairline=[(6, 72), (50, 72), (94, 72)]),
  [L(outline([(-6, 76), (-4, 50), (10, 20), (50, 6), (90, 20), (104, 50), (106, 76), (80, 70), (52, 74), (50, 60, 1), (48, 74), (20, 70)])),
   L(outline([(60, 10), (90, 20), (104, 50), (104, 72), (82, 46)]), 'shade', 'b', False),
   L(ell(36, 80, 4, 4), WHITE, 'f', True), L(ell(64, 80, 4, 4), WHITE, 'f', True)],
  [L(outline([(70, 70), (96, 66), (100, 44), (84, 16), (50, 6), (16, 16), (0, 44), (4, 74), (30, 80), (50, 76)]))],
  [L(outline([(-6, 76), (-4, 50), (10, 20), (50, 6), (90, 20), (104, 50), (106, 76), (50, 82)]))])

# Liam Tossarawn: piel tostada anaranjada, pelo rosa fuerte en mechones alborotados hacia arriba; ojos amarillos, marcas rojas y sonrisa
C('liam-tossarawn', 'normal', P('#e04a60', '#f0a868', iris='#d8b030'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=hl(5, 64, 46, 56, lean=-3, jit=3, seed=17)),
  dome('front', top=-8, w=48, cy=44, n=8, amp=12, sweep=0.3, seed=19, sb=66) + [mark([(20, 80), (30, 78)], _c('#d83a3a'), w=1.6), mark([(80, 80), (70, 78)], _c('#d83a3a'), w=1.6)],
  dome('side', top=-8, w=48, cy=44, n=8, amp=12, sweep=0.3, seed=19, nape=84, fr=50),
  dome('back', top=-8, w=48, cy=44, n=8, amp=12, sweep=0.3, seed=19, nape=84))

# Link Whitstone: pelo azul marino con una mecha más clara, flequillo largo hasta los ojos y un pelito de punta arriba; ojos azules afilados
C('link-whitstone', 'normal', P('#3a4a90', '#f6d0b0', iris='#4a8ad0', light='#6a7ad0'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=hl(6, 68, 52, 70, jit=3, seed=23)),
  dome('front', top=0, w=48, cy=46, n=7, amp=6, seed=29, sb=70) + [L(outline([(48, 8), (56, -8, 1), (54, 6)])),
  L(outline([(40, 12), (56, 10), (54, 50), (46, 64, 1), (44, 40)]), 'light', 'f', False)],
  dome('side', top=0, w=48, cy=46, n=7, amp=6, seed=29, nape=86, fr=60) + [L(outline([(44, 8), (50, -8, 1), (52, 6)]))],
  dome('back', top=0, w=48, cy=46, n=7, amp=6, seed=29, nape=86))

# Linton Judson: grandullón de cara ancha con el pelo negro muy corto en pico sobre la frente; ojillos y ceño fruncido
C('linton-judson', 'corpulento', P('#1e1e22', '#f6d0b0', iris='#2a2a2a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, face_front=face(w=10, chin=104, jaw=8), face_side=face_side(chin=4, jaw=6),
    hairline=[(6, 56), (18, 46), (40, 44), (50, 50), (60, 44), (82, 46), (94, 56)]),
  dome('front', top=8, w=44, cy=48, sb=60),
  dome('side', top=8, w=44, cy=48, nape=80, fr=44),
  dome('back', top=8, w=44, cy=48, nape=80))

# Lior Morrissey: piel oscura, melena rubia dorada desgreñada que le tapa medio ojo; ojos rojos afilados y ceño
C('lior-morrissey', 'normal', P('#e8b020', '#8a5038', iris='#c03030'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 70), (16, 56), (28, 66), (34, 50), (50, 76), (58, 52), (70, 62), (82, 52), (94, 70)]),
  dome('front', top=2, w=50, cy=46, n=8, amp=8, seed=41, long=84, flare=8) + [L(outline([(30, 30), (54, 34), (60, 60), (52, 80, 1), (40, 56)]), 'mid', 'f')],
  dome('side', top=2, w=50, cy=46, n=8, amp=8, seed=41, long=82, flare=8, fr=60),
  dome('back', top=2, w=50, cy=46, n=8, amp=8, seed=41, long=82, flare=8, ends=4))

# Liron Suesskind: pelo gris de mechones largos con una mecha negra a un lado y el flequillo entre los ojos; ojos verdosos
C('liron-suesskind', 'normal', P('#9a9a9a', '#f6d0b0', iris='#8a9a6a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 70), (18, 50), (34, 46), (46, 74), (54, 50), (68, 48), (82, 52), (94, 70)]),
  dome('front', top=0, w=50, cy=46, n=9, amp=8, seed=43, long=82, flare=8) + [L(outline([(12, 50), (6, 66), (14, 86, 1), (22, 70), (22, 56)]), BLACK, 'f'),
  L(outline([(42, 30), (54, 34), (50, 74, 1), (44, 52)]), 'mid', 'f')],
  dome('side', top=0, w=50, cy=46, n=9, amp=8, seed=43, long=80, flare=8, fr=58),
  dome('back', top=0, w=50, cy=46, n=9, amp=8, seed=43, long=80, flare=8, ends=4) + [L(outline([(80, 50), (92, 64), (86, 82, 1), (78, 66)]), BLACK, 'b')])

# Lisa Lovetluke: pelo rosa coral corto y ondulado, con un rizo sobre la frente; ojos turquesa grandes y redondos
C('lisa-lovetluke', 'chica', P('#f07070', '#f6d0b0', iris='#3ab0c8'),
  F(eyes='big', brows=True, mouth='none', hairline=[(6, 64), (16, 48), (30, 40), (44, 40), (52, 50), (62, 42), (80, 46), (94, 64)]),
  dome('front', top=2, w=48, cy=46, n=6, amp=6, seed=47, soft=True, sb=70) + [L(outline([(36, 40), (46, 34), (50, 46), (44, 50)]), 'shade', 'f', False),
  L(ell(50, 92, 1.4, 1.4), OUTC, 'f', False)],
  dome('side', top=2, w=48, cy=46, n=6, amp=6, seed=47, soft=True, nape=84, fr=52),
  dome('back', top=2, w=48, cy=46, n=6, amp=6, seed=47, soft=True, nape=84))

# Liselotte Heartsway: pelo naranja rojizo con flequillo y dos coletas bajas que se abren en bucles; ojos turquesa y sonrisa
C('liselotte-heartsway', 'chica', P('#f05030', '#f6d8c0', iris='#3a9aa8'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 66), (16, 50), (30, 46), (44, 52), (56, 44), (72, 48), (84, 52), (94, 66)]),
  [tail(14, 66, -12, 30, 16), tail(86, 66, 12, 30, 16)] + dome('front', top=2, w=48, cy=46, sb=70),
  [tail(26, 66, -16, 30, 16)] + dome('side', top=2, w=48, cy=46, nape=84, fr=54),
  [tail(14, 66, -12, 30, 16), tail(86, 66, 12, 30, 16)] + dome('back', top=2, w=48, cy=46, nape=84))

# Lita Vault: media melena roja con una mecha blanca que cae ondulada por delante de la cara; ojos verdes y sonrisa
C('lita-vault', 'chica', P('#c04030', '#f6d0b8', iris='#3a9a6a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 66), (14, 50), (30, 46), (50, 50), (70, 46), (86, 50), (94, 66)]),
  dome('front', top=4, w=46, cy=46, long=80, flare=4) + [L(outline([(26, 20), (32, 18), (30, 50), (20, 70), (28, 84, 1), (16, 70), (22, 48)]), WHITE, 'f')],
  dome('side', top=4, w=46, cy=46, long=78, flare=4, fr=54) + [L(outline([(70, 20), (76, 22), (80, 56), (74, 74, 1), (72, 50)]), WHITE, 'f')],
  dome('back', top=4, w=46, cy=46, long=78, flare=4, ends=0))

# Livia Marsquall (portera): pelo malva con flequillo y una trenza que le cae por un lado; ojos rosas y boca abierta sonriente
C('livia-marsquall', 'chica', P('#b07890', '#f8dcd0', iris='#d04a70'),
  F(eyes='big', brows=True, mouth='grin', mouth_y=93, hairline=[(6, 66), (16, 50), (30, 46), (50, 48), (70, 46), (84, 50), (94, 66)]),
  dome('front', top=4, w=46, cy=46, sb=70) + braid([(84, 60), (86, 74), (84, 88), (80, 100)], r=6) + blush(),
  dome('side', top=4, w=46, cy=46, nape=84, fr=54) + braid([(38, 70), (36, 84), (34, 98)], r=6),
  dome('back', top=4, w=46, cy=46, nape=84) + braid([(18, 60), (16, 74), (18, 88), (20, 100)], r=6))

# Lockin Somnal: piel tostada, un afro negro enorme con la parte de arriba azul claro; ojos verdes y gesto serio
C('lockin-somnal', 'normal', P('#1e1a1e', '#c8906a', iris='#3a9a6a', top='#8aa0d8'),
  F(eyes='round', brows='angry', mouth='line', mouth_y=95, ears=False, face_front=face(w=4), hairline=[(6, 62), (24, 50), (50, 48), (76, 50), (94, 62)]),
  dome('front', top=-8, w=60, cy=40, n=14, amp=8, seed=53, soft=True, sb=80) + [L(blob([(14, 34), (24, 10), (50, 4), (76, 10), (86, 34), (70, 48), (50, 44), (30, 48)], 8), 'top', 'f', False)],
  dome('side', top=-8, w=58, cy=40, n=14, amp=8, seed=53, soft=True, nape=88, fr=50) + [L(blob([(24, 30), (40, 6), (70, 6), (90, 30), (80, 44), (50, 40)], 8), 'top', 'f', False)],
  dome('back', top=-8, w=60, cy=40, n=14, amp=8, seed=53, soft=True, nape=88))

# Lorenzo Dellart: melena negra larga y lisa con un moño alto, un mechón sobre un ojo; sombra morada y sonrisa torcida
C('lorenzo-dellart', 'delgado', P('#1e1a24', '#f6dcd0', iris='#6a5aa8'),
  F(eyes='sharp', brows=False, mouth='grin', mouth_y=95, face_front=face(chin=104), face_side=face_side(chin=4), hairline=[(6, 62), (20, 46), (40, 40), (60, 50), (76, 62), (94, 70)]),
  [bun(48, -4, 10)] + dome('front', top=2, w=46, cy=44, long=104, flare=4) + [L(outline([(52, 30), (76, 40), (82, 60), (74, 82, 1), (66, 56)]), 'mid', 'f')] + shadow_eyes('#8a5ac8'),
  [bun(40, -4, 10)] + dome('side', top=2, w=46, cy=44, long=104, flare=4, fr=48),
  [bun(50, -4, 10)] + dome('back', top=2, w=46, cy=44, long=104, flare=4, ends=3))

# Louise Basson (portera): pelo naranja intenso recogido con un gran rizo en espiral sobre un lado y dos moñitos
C('louise-basson', 'chica', P('#e87020', '#f6d8c0', iris='#3aa8a0'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=[(6, 62), (18, 46), (40, 40), (60, 44), (80, 50), (94, 66)]),
  [bun(94, 14, 7), bun(98, 30, 6)] + dome('front', top=2, w=46, cy=44, sb=60) + [L(outline([(14, 40), (20, 18), (44, 10), (58, 22), (48, 36), (36, 28), (30, 40)]), 'light', 'f'),
  L(outline([(78, 48), (84, 64), (80, 86, 1), (74, 64)]))] + blush(),
  [bun(20, 12, 7)] + dome('side', top=2, w=46, cy=44, nape=80, fr=46) + [L(outline([(54, 20), (70, 10), (84, 24), (72, 32), (62, 26)]), 'light', 'f')],
  [bun(8, 14, 7), bun(4, 30, 6)] + dome('back', top=2, w=46, cy=44, nape=80))

# Luceus Cloudstrider: pelo gris plateado en ondas de nube, piel clara; ojos grises y labios en sonrisa
C('luceus-cloudstrider', 'normal', P('#a8a8b0', '#f6dcc8', iris='#8a8a98'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=94, face_front=face(chin=104), hairline=[(6, 62), (18, 48), (34, 44), (50, 50), (66, 44), (82, 48), (94, 62)]),
  dome('front', top=0, w=48, cy=44, n=10, amp=5, seed=59, soft=True, sb=64) + [strand([(30, 24), (40, 36)], 'shade', 'b', 1.2), strand([(70, 24), (60, 36)], 'shade', 'b', 1.2)],
  dome('side', top=0, w=48, cy=44, n=10, amp=5, seed=59, soft=True, nape=82, fr=48),
  dome('back', top=0, w=48, cy=44, n=10, amp=5, seed=59, soft=True, nape=82))

# Lumina (portera, con modelo 3D): media melena rubia clara en campana, abierta hacia fuera; ojos verdes y sonrisa
C('lumina', 'chica', P('#f0e070', '#f8dcc8', iris='#3aa84a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 66), (16, 50), (30, 44), (46, 50), (54, 42), (72, 46), (86, 50), (94, 66)]),
  dome('front', top=2, w=48, cy=46, long=84, flare=12) + [strand([(46, 10), (40, 40)], 'shade', 'b', 1.2)],
  dome('side', top=2, w=48, cy=46, long=82, flare=12, fr=54) + [L(blob([(-6, 70), (20, 66), (44, 74), (40, 86), (0, 86)], 6), _c('#a07a40'), 'b', False)],
  dome('back', top=2, w=48, cy=46, long=82, flare=12, ends=3) + [L(blob([(2, 64), (98, 64), (102, 84), (50, 90), (-2, 84)], 6), _c('#a07a40'), 'b', False)])

# Lyla Loveland: pelo azul claro desfilado con un mechón que le cae sobre un ojo; ojos azules afilados y sonrisa
C('lyla-loveland', 'chica', P('#6a9ae0', '#f6d8c8', iris='#3a6ab0'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 66), (18, 50), (30, 56), (40, 46), (60, 74), (68, 50), (82, 52), (94, 66)]),
  dome('front', top=2, w=48, cy=46, n=8, amp=8, seed=61, long=80, flare=10) + [L(outline([(44, 30), (66, 36), (72, 60), (64, 78, 1), (56, 52)]), 'mid', 'f')],
  dome('side', top=2, w=48, cy=46, n=8, amp=8, seed=61, long=78, flare=10, fr=58),
  dome('back', top=2, w=48, cy=46, n=8, amp=8, seed=61, long=78, flare=10, ends=4))

# Lyra Nazar: piel morena, pelo castaño oscuro peinado hacia atrás con una trenza larga que cae por un lado y se riza;
# ojos afilados con sombra rosa y sonrisa
C('lyra-nazar', 'chica', P('#3a3020', '#c09070', iris='#8a7a50'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=[(6, 58), (22, 44), (50, 40), (78, 44), (94, 58)]),
  dome('front', top=6, w=44, cy=46, sb=60) + braid([(12, 26), (6, 44), (6, 62), (8, 80), (14, 96)], r=5) + shadow_eyes('#d07090'),
  dome('side', top=6, w=44, cy=46, nape=82, fr=44),
  dome('back', top=6, w=44, cy=46, nape=82) + braid([(88, 26), (94, 44), (94, 62), (92, 80), (86, 96)], r=5))

# Lysander Trimore: tupé rubio crema por delante con la parte de atrás castaña echada hacia arriba en pico; ojos naranjas
C('lysander-trimore', 'normal', P('#b08060', '#f6d0b0', iris='#d08030', front='#f0e0b0'),
  F(eyes='round', brows='angry', mouth='smile', mouth_y=94, hairline=[(6, 60), (18, 46), (40, 40), (60, 44), (82, 48), (94, 60)]),
  dome('front', top=4, w=46, cy=46, sb=62) + [L(outline([(70, 10), (96, -6, 1), (90, 20), (84, 36)])),
  L(outline([(10, 44), (14, 16), (34, 4), (56, 12), (62, 30), (44, 42), (24, 46)]), 'front', 'f')],
  dome('side', top=4, w=46, cy=46, nape=82, fr=50) + [L(outline([(20, 14), (0, -4, 1), (14, 24)])), L(outline([(54, 14), (76, 8), (90, 22), (86, 40), (64, 40)]), 'front', 'f')],
  dome('back', top=4, w=46, cy=46, nape=82) + [L(outline([(30, 10), (4, -6, 1), (10, 20), (16, 36)]))])

# Machaela Thevert: melena ondulada verde oliva hasta los hombros, sombra verde en los párpados; gesto serio
C('machaela-thevert', 'chica', P('#6a6a50', '#f6d8c0', iris='#4a4a3a'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=93, hairline=[(6, 66), (16, 50), (30, 46), (50, 50), (70, 46), (84, 50), (94, 66)]),
  dome('front', top=2, w=48, cy=46, n=8, amp=5, seed=67, soft=True, long=90, flare=10) + shadow_eyes('#4ab06a'),
  dome('side', top=2, w=48, cy=46, n=8, amp=5, seed=67, soft=True, long=88, flare=10, fr=54),
  dome('back', top=2, w=48, cy=46, n=8, amp=5, seed=67, soft=True, long=88, flare=10, ends=5))

# Macy Drapeley: pelo rojo cobrizo con un moño alto redondo, flequillo y dos coletitas a los lados; ojos cerrados contentos
C('macy-drapeley', 'chica', P('#b03020', '#f6d8c0', iris='#3a2a2a'),
  F(eyes='closed', brows=False, mouth='smile', mouth_y=92, face_front=face(w=3), hairline=[(6, 64), (16, 48), (30, 44), (50, 50), (70, 44), (84, 48), (94, 64)]),
  [bun(50, -6, 12), tail(10, 52, -8, 18, 8), tail(90, 52, 8, 18, 8)] + dome('front', top=6, w=46, cy=46, sb=66) + blush(),
  [bun(40, -6, 12), tail(30, 52, -10, 18, 8)] + dome('side', top=6, w=46, cy=46, nape=82, fr=52),
  [bun(50, -6, 12), tail(10, 52, -8, 18, 8), tail(90, 52, 8, 18, 8)] + dome('back', top=6, w=46, cy=46, nape=82))

# Madeline Milke: pañuelo blanco atado bajo la barbilla que deja ver solo el pelo castaño de la frente; piel morena y ojos azul claro
CLOTH = _c('#f4ecec')
C('madeline-milke', 'chica', P('#4a3020', '#c09070', iris='#7ac8d8'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, ears=False, hairline=[(6, 56), (24, 44), (50, 40), (76, 44), (94, 56)]),
  [L(outline([(4, 90), (0, 50), (14, 14), (50, 0), (86, 14), (100, 50), (96, 90), (84, 96), (82, 60), (70, 40), (50, 36), (30, 40), (18, 60), (16, 96)]), CLOTH, 'f'),
   L(outline([(40, 100), (50, 96), (64, 104), (56, 110), (46, 108)]), CLOTH, 'f')] + dome('front', top=24, w=34, cy=50, sb=56, shade=False),
  [L(outline([(70, 52), (86, 34), (80, 10), (50, 0), (20, 6), (4, 30), (2, 70), (14, 88), (34, 96), (56, 98), (66, 86), (62, 64)]), CLOTH)],
  [L(outline([(4, 90), (0, 50), (14, 14), (50, 0), (86, 14), (100, 50), (96, 90), (50, 98)]), CLOTH)])

# Maeve Smith (con modelo 3D): melena castaña ondulada hasta los hombros, con raya al lado que le tapa un ojo y las puntas
# turquesa por debajo; ojos verde agua
TEAL = _c('#2ab0b0')
C('maeve-smith', 'chica', P('#7a5a3a', '#f6d0b0', iris='#2a9a98'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=93, hairline=[(6, 70), (14, 50), (24, 40), (40, 44), (48, 80), (56, 44), (70, 42), (84, 50), (94, 70)]),
  [L(blob([(10, 70), (26, 86), (40, 92), (22, 96), (6, 88)], 6), TEAL)] + dome('front', top=0, w=48, cy=44, n=6, amp=6, seed=71, soft=True, long=92, flare=14) +
  [L(outline([(26, 30), (48, 26), (52, 60), (44, 86, 1), (34, 58)]), 'mid', 'f')],
  [L(blob([(0, 80), (30, 84), (40, 94), (4, 96)], 6), TEAL)] + dome('side', top=0, w=48, cy=44, n=6, amp=6, seed=71, soft=True, long=90, flare=14, fr=52),
  [L(blob([(0, 80), (100, 80), (102, 96), (-2, 96)], 6), TEAL)] + dome('back', top=0, w=48, cy=44, n=6, amp=6, seed=71, soft=True, long=90, flare=14, ends=4))

# Mako Carcher: melena negra azulada ondulada hasta el cuello con una mecha celeste; ojos azul claro afilados y sonrisa
SKY = _c('#6ac8f0')
C('mako-carcher', 'chica', P('#1e2030', '#f8e0d8', iris='#6ac0e0'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=92, hairline=[(6, 64), (16, 48), (34, 44), (50, 54), (66, 42), (84, 48), (94, 64)]),
  dome('front', top=2, w=48, cy=46, n=6, amp=6, seed=73, soft=True, long=86, flare=10) + [L(outline([(56, 8), (62, 8), (64, 44), (58, 50)]), SKY, 'f', False)],
  dome('side', top=2, w=48, cy=46, n=6, amp=6, seed=73, soft=True, long=84, flare=10, fr=54) + [L(outline([(64, 8), (70, 10), (78, 40), (70, 42)]), SKY, 'f', False)],
  dome('back', top=2, w=48, cy=46, n=6, amp=6, seed=73, soft=True, long=84, flare=10, ends=4))

# Manni Lamasque: piel oscura, afro castaño redondo, cejas gruesas y un punto en la frente; mirada aburrida
C('manni-lamasque', 'normal', P('#4a2a1a', '#8a5a3a', iris='#3a2a3a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, ears=True, hairline=[(6, 60), (22, 48), (50, 46), (78, 48), (94, 60)]),
  dome('front', top=-6, w=56, cy=40, n=14, amp=5, seed=79, soft=True, sb=64) + [L(ell(50, 64, 1.6, 1.6), _c('#5a3020'), 'f', False)],
  dome('side', top=-6, w=54, cy=40, n=14, amp=5, seed=79, soft=True, nape=82, fr=46),
  dome('back', top=-6, w=56, cy=40, n=14, amp=5, seed=79, soft=True, nape=82))

# Manon Matopia: pelo naranja en rizos muy abultados a los lados con coletas atadas con gomas rojas; ojos verdes y sonrisa de dientes
C('manon-matopia', 'chica', P('#e8962a', '#f6d8c0', iris='#5aa83a'),
  F(eyes='big', brows=True, mouth='grin', mouth_y=93, hairline=[(6, 64), (16, 48), (30, 44), (44, 52), (56, 44), (70, 46), (84, 50), (94, 64)]),
  [L(blob([(-14, 40), (6, 26), (20, 50), (16, 84), (-4, 96), (-16, 72)], 6)), L(blob([(114, 40), (94, 26), (80, 50), (84, 84), (104, 96), (116, 72)], 6)),
   L(ell(6, 92, 4, 3), _c('#c83030'), 'b'), L(ell(94, 92, 4, 3), _c('#c83030'), 'b')] + dome('front', top=0, w=48, cy=44, n=10, amp=5, seed=83, soft=True, sb=66) +
  [L(outline([(46, 4), (50, -8), (56, 2)]))] + blush(),
  [L(blob([(-6, 40), (20, 30), (34, 60), (24, 90), (4, 96), (-10, 70)], 6))] + dome('side', top=0, w=48, cy=44, n=10, amp=5, seed=83, soft=True, nape=84, fr=52),
  [L(blob([(-14, 40), (6, 26), (20, 50), (16, 84), (-4, 96), (-16, 72)], 6)), L(blob([(114, 40), (94, 26), (80, 50), (84, 84), (104, 96), (116, 72)], 6))] +
  dome('back', top=0, w=48, cy=44, n=10, amp=5, seed=83, soft=True, nape=84))

# Marcel Leapman: pelo castaño en casco redondo con dos bultos a los lados como orejas de mono; mejillas rosas, nariz y sonrisa
C('marcel-leapman', 'normal', P('#8a6a30', '#f6c8a0', iris='#4a6a5a'),
  F(eyes='big', brows='angry', mouth='grin', mouth_y=96, nose=(50, 86, 3), ears=False, face_front=face(w=4, chin=104), hairline=[(6, 60), (24, 46), (50, 40), (76, 46), (94, 60)]),
  [L(blob([(-10, 50), (2, 34), (18, 50), (14, 76), (0, 78)], 6)), L(blob([(110, 50), (98, 34), (82, 50), (86, 76), (100, 78)], 6))] + dome('front', top=0, w=48, cy=44, sb=60) + blush('#f0a070'),
  [L(blob([(14, 48), (34, 44), (40, 70), (24, 80)], 6))] + dome('side', top=0, w=48, cy=44, nape=82, fr=46),
  [L(blob([(-10, 50), (2, 34), (18, 50), (14, 76), (0, 78)], 6)), L(blob([(110, 50), (98, 34), (82, 50), (86, 76), (100, 78)], 6))] + dome('back', top=0, w=48, cy=44, nape=82))

# Marcol Leapstone: piel oscura, pelo verde azulado oscuro peinado hacia arriba y atrás; ceño muy fruncido, gafitas y boca torcida
C('marcol-leapstone', 'normal', P('#1e5a5a', '#8a5a3a', iris='#2a2a2a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, glasses=_c('#c8a070'), face_front=face(w=4, chin=104), hairline=[(6, 58), (20, 44), (50, 38), (80, 44), (94, 58)]),
  dome('front', top=-4, w=44, cy=42, sb=60) + [L(outline([(30, 10), (46, -12, 1), (56, 4), (70, -6, 1), (72, 14)])), strand([(36, 30), (44, 4)], 'deep', 'b', 1.2)],
  dome('side', top=-4, w=44, cy=42, nape=80, fr=40) + [L(outline([(30, 6), (10, -10, 1), (26, 18)]))],
  dome('back', top=-4, w=44, cy=42, nape=80))

# Margo Versier: pelo rosa fucsia con flequillo de mechones y dos coletas bajas abultadas; ojos grises y media sonrisa
C('margo-versier', 'chica', P('#d84a6a', '#f6d0b8', iris='#8a90a8'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 62), (16, 48), (26, 54), (34, 44), (44, 56), (56, 44), (66, 56), (76, 44), (86, 50), (94, 62)]),
  [tail(10, 50, -10, 36, 16), tail(90, 50, 10, 36, 16)] + dome('front', top=2, w=48, cy=46, sb=70),
  [tail(26, 50, -14, 36, 16)] + dome('side', top=2, w=48, cy=46, nape=84, fr=52),
  [tail(10, 50, -10, 36, 16), tail(90, 50, 10, 36, 16)] + dome('back', top=2, w=48, cy=46, nape=84))

# Margot Napier: pelo rubio en casco abultado con un rizo crema arriba; mofletes rosas en espiral y ojos amarillos
C('margot-napier', 'chica', P('#e8c050', '#f8dcd0', iris='#c8a030', light='#f8f0d0'),
  F(eyes='round', brows=True, mouth='smile', mouth_y=93, face_front=face(w=4, chin=102), hairline=[(6, 64), (16, 48), (34, 42), (50, 48), (66, 42), (84, 48), (94, 64)]),
  dome('front', top=0, w=50, cy=44, n=8, amp=5, seed=89, soft=True, long=78, flare=4) + [L(outline([(26, 16), (50, 4), (66, 14), (58, 22), (46, 16), (36, 26)]), 'light', 'f')] + blush('#f09080'),
  dome('side', top=0, w=50, cy=44, n=8, amp=5, seed=89, soft=True, long=76, flare=4, fr=50),
  dome('back', top=0, w=50, cy=44, n=8, amp=5, seed=89, soft=True, long=76, flare=4, ends=3))

# Marius Harlow (portero): piel oscura, pelo verde oscuro desfilado hasta el cuello con dos mechas granates; ojos grandes y sonrisa
MAR = _c('#7a1e2a')
C('marius-harlow', 'normal', P('#1e5a4a', '#8a5a40', iris='#2a2a2a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=94, hairline=hl(6, 70, 48, 62, jit=3, seed=91)),
  dome('front', top=-2, w=48, cy=44, n=8, amp=8, seed=93, long=88, flare=10) + [L(outline([(26, 6), (32, 6), (24, 48), (20, 46)]), MAR, 'f', False), L(outline([(70, 6), (76, 8), (80, 46), (76, 46)]), MAR, 'f', False)],
  dome('side', top=-2, w=48, cy=44, n=8, amp=8, seed=93, long=86, flare=10, fr=58) + [L(outline([(60, 4), (66, 6), (74, 40), (70, 40)]), MAR, 'f', False)],
  dome('back', top=-2, w=48, cy=44, n=8, amp=8, seed=93, long=86, flare=10, ends=4))

# Marjorette Pompom: pelo verde claro con raya al medio y dos coletas largas con lazos amarillos; ojos de estrella y sonrisa de dientes
YEL = _c('#f0c030')
C('marjorette-pompom', 'chica', P('#c8d898', '#f8dcd0', iris='#c8a030'),
  F(eyes='big', brows=True, mouth='grin', mouth_y=93, hairline=[(6, 62), (20, 46), (40, 40), (50, 46), (60, 40), (80, 46), (94, 62)]),
  [tail(10, 60, -10, 52, 14), tail(90, 60, 10, 52, 14), L(ell(10, 62, 6, 5), YEL, 'b'), L(ell(90, 62, 6, 5), YEL, 'b')] + dome('front', top=2, w=46, cy=44, sb=66) + blush(),
  [tail(28, 60, -14, 52, 14), L(ell(28, 62, 6, 5), YEL, 'b')] + dome('side', top=2, w=46, cy=44, nape=82, fr=48),
  [tail(10, 60, -10, 52, 14), tail(90, 60, 10, 52, 14), L(ell(10, 62, 6, 5), YEL), L(ell(90, 62, 6, 5), YEL)] + dome('back', top=2, w=46, cy=44, nape=82))

# Marjorie Piperplume: pelo castaño claro rosado con flequillo partido y los lados abultados en alas; ojos morados
C('marjorie-piperplume', 'chica', P('#d8a890', '#f6d8c8', iris='#6a5a90', shade='#a07060'),
  F(eyes='big', brows=True, mouth='none', hairline=[(6, 62), (18, 46), (34, 44), (46, 56), (54, 44), (70, 46), (84, 50), (94, 62)]),
  [L(blob([(-14, 44), (6, 28), (20, 50), (14, 76), (-6, 70)], 6)), L(blob([(114, 44), (94, 28), (80, 50), (86, 76), (106, 70)], 6))] +
  dome('front', top=4, w=46, cy=44, n=8, amp=5, seed=97, soft=True, sb=66) + [L(ell(50, 92, 1.4, 1.4), OUTC, 'f', False)],
  [L(blob([(0, 44), (24, 36), (34, 60), (20, 76), (2, 70)], 6))] + dome('side', top=4, w=46, cy=44, n=8, amp=5, seed=97, soft=True, nape=82, fr=50),
  [L(blob([(-14, 44), (6, 28), (20, 50), (14, 76), (-6, 70)], 6)), L(blob([(114, 44), (94, 28), (80, 50), (86, 76), (106, 70)], 6))] +
  dome('back', top=4, w=46, cy=44, n=8, amp=5, seed=97, soft=True, nape=82))

# Masala Mettler: pelo rosa fucsia con dos picos arriba como orejas de gato y las puntas abiertas; ojos rojos y ceño
C('masala-mettler', 'chica', P('#d84a6a', '#f8dcd0', iris='#a01e2a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=[(6, 66), (18, 50), (34, 46), (44, 70), (54, 48), (68, 46), (84, 50), (94, 66)]),
  [horn(20, 22, 8, -6, 'mid'), horn(80, 22, 92, -6, 'mid')] + dome('front', top=4, w=46, cy=46, sb=66) + [L(outline([(-2, 70), (10, 56), (14, 74)])), L(outline([(102, 70), (90, 56), (86, 74)]))],
  [horn(50, 10, 54, -10, 'mid')] + dome('side', top=4, w=46, cy=46, nape=84, fr=56),
  [horn(20, 22, 8, -6, 'mid'), horn(80, 22, 92, -6, 'mid')] + dome('back', top=4, w=46, cy=46, nape=84))

# Matilde Pendlebury: pelo granate oscuro corto con flequillo a un lado; ojos castaños y sonrisa tranquila
C('matilde-pendlebury', 'chica', P('#4a2030', '#f8dcd0', iris='#7a6a40'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 62), (16, 48), (30, 52), (40, 44), (60, 46), (84, 50), (94, 62)]),
  dome('front', top=2, w=46, cy=46, n=7, amp=5, seed=101, sb=70) + [L(outline([(30, 24), (60, 22), (46, 40), (34, 50, 1), (32, 36)]), 'mid', 'f')],
  dome('side', top=2, w=46, cy=46, n=7, amp=5, seed=101, nape=82, fr=52),
  dome('back', top=2, w=46, cy=46, n=7, amp=5, seed=101, nape=82))

# Maximus Cordray (portero, con modelo 3D): adulto de piel morena, pelo gris oscuro con dos picos arriba y melena abierta
# hasta los hombros; mirada seria y media sonrisa
C('maximus-cordray', 'delgado', P('#3a3a3c', '#a07050', iris='#7a8090'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=96, face_front=face(chin=106, jaw=2), face_side=face_side(chin=6), hairline=[(6, 58), (22, 44), (50, 40), (78, 44), (94, 58)]),
  [horn(18, 22, 2, -6, 'mid'), horn(82, 22, 98, -6, 'mid')] + dome('front', top=6, w=46, cy=46, n=0, seed=103, long=92, flare=16),
  [horn(50, 10, 54, -10, 'mid')] + dome('side', top=6, w=46, cy=46, n=0, seed=103, long=90, flare=16, fr=46),
  [horn(18, 22, 2, -6, 'mid'), horn(82, 22, 98, -6, 'mid')] + dome('back', top=6, w=46, cy=46, n=0, seed=103, long=90, flare=16, ends=4))

# Medwin Silvers (portero): señor mayor con el pelo gris a los lados y una cresta verde azulada hacia atrás; cejas pobladas
# verde azulado, nariz roja y boca de enfado
C('medwin-silvers', 'corpulento', P('#7a8a98', '#f6d0b8', iris='#2a2a3a', crest='#3a9aa0'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=97, nose=(50, 86, 3.4), face_front=face(w=4, chin=104), hairline=[(6, 58), (20, 44), (50, 42), (80, 44), (94, 58)]),
  dome('front', top=10, w=46, cy=48, n=6, amp=6, seed=107, sb=64) + [L(outline([(40, 20), (44, -18), (60, -24, 1), (56, -6), (60, 20)]), 'crest'),
  L(outline([(22, 70), (32, 62), (44, 68), (40, 72), (30, 68)]), 'crest', 'f'), L(outline([(78, 70), (68, 62), (56, 68), (60, 72), (70, 68)]), 'crest', 'f'),
  L(ell(50, 84, 4, 3), _c('#d86060'), 'f', False)],
  dome('side', top=10, w=46, cy=48, n=6, amp=6, seed=107, nape=82, fr=48) + [L(outline([(70, 18), (50, -16), (20, -20, 1), (36, 0), (30, 20)]), 'crest')],
  dome('back', top=10, w=46, cy=48, n=6, amp=6, seed=107, nape=82) + [L(outline([(42, 30), (44, -16), (58, -20, 1), (58, 30)]), 'crest')])

# Megal O'Donn: pelo naranja en mechones de punta con una mecha verde menta grande sobre un lado; ojos azules
MINT = _c('#7ac8a8')
C('megal-o-donn', 'normal', P('#e8703a', '#f6d0b0', iris='#5a8ac8'),
  F(eyes='big', brows=True, mouth='frown', mouth_y=93, hairline=hl(5, 66, 48, 62, lean=3, jit=3, seed=109)),
  dome('front', top=-4, w=48, cy=44, n=8, amp=10, sweep=0.3, seed=111, sb=68) + [L(outline([(36, 6), (60, 2), (66, 20), (50, 50), (44, 62, 1), (40, 34)]), MINT, 'f')],
  dome('side', top=-4, w=48, cy=44, n=8, amp=10, sweep=0.3, seed=111, nape=84, fr=54) + [L(outline([(52, 4), (76, 10), (78, 30), (68, 44, 1), (60, 22)]), MINT, 'f')],
  dome('back', top=-4, w=48, cy=44, n=8, amp=10, sweep=0.3, seed=111, nape=84) + [L(outline([(40, 6), (60, 4), (56, 30), (44, 30)]), MINT, 'b')])

# Megpie O'Neering: media melena rosa palo lisa con flequillo; ojos morados y boca en "o"
C('megpie-o-neering', 'chica', P('#c08080', '#f8dcd0', iris='#8a5a90'),
  F(eyes='big', brows=True, mouth='none', hairline=[(6, 66), (16, 50), (30, 46), (46, 56), (56, 46), (72, 46), (84, 50), (94, 66)]),
  dome('front', top=0, w=48, cy=46, long=82, flare=2) + [L(ell(50, 93, 2.2, 2.6), _c('#c04a40'), 'f', False)],
  dome('side', top=0, w=48, cy=46, long=80, flare=2, fr=54),
  dome('back', top=0, w=48, cy=46, long=80, flare=2, ends=0))

# Memo Rize: pelo verde con flequillo en tejadillo y unas hojitas de punta arriba; cejas verdes gruesas, ojos saltones y sonrisa
C('memo-rize', 'bajito', P('#4ab040', '#f6c8a0', iris='#c03030'),
  F(eyes='round', brows='angry', mouth='line', mouth_y=95, big_ears=2, ear_out=4, face_front=face(w=4, chin=104), hairline=[(6, 56), (16, 48), (50, 50), (84, 48), (94, 56)]),
  dome('front', top=4, w=46, cy=44, sb=56) + [L(outline([(44, 6), (40, -10, 1), (50, 2), (58, -12, 1), (60, 6)])),
  L(outline([(12, 44), (50, 40), (88, 44), (90, 54), (50, 52), (10, 54)]), 'mid', 'f')],
  dome('side', top=4, w=46, cy=44, nape=78, fr=48) + [L(outline([(40, 4), (38, -12, 1), (48, 2), (56, -12, 1), (58, 6)])), L(outline([(60, 40), (96, 44), (94, 54), (62, 52)]), 'mid', 'f')],
  dome('back', top=4, w=46, cy=44, nape=78) + [L(outline([(44, 6), (40, -10, 1), (50, 2), (58, -12, 1), (60, 6)]))])

# Micco Chantelle: pelo negro liso con raya al medio, recogido en dos coletas bajas con gomas blancas; ojos afilados y sonrisa
C('micco-chantelle', 'normal', P('#1e1e22', '#f6dcd0', iris='#3a3030'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=93, face_front=face(chin=104), hairline=[(6, 62), (20, 46), (40, 40), (50, 44), (60, 40), (80, 46), (94, 62)]),
  [tail(12, 64, -4, 36, 14), tail(88, 64, 4, 36, 14), L(ell(12, 64, 6, 3), WHITE, 'b'), L(ell(88, 64, 6, 3), WHITE, 'b')] + dome('front', top=2, w=46, cy=44, sb=66),
  [tail(26, 64, -8, 36, 14), L(ell(26, 64, 6, 3), WHITE, 'b')] + dome('side', top=2, w=46, cy=44, nape=80, fr=48),
  [tail(12, 64, -4, 36, 14), tail(88, 64, 4, 36, 14), L(ell(12, 64, 6, 3), WHITE), L(ell(88, 64, 6, 3), WHITE)] + dome('back', top=2, w=46, cy=44, nape=80))

# Mika Upton: melena rosa chicle larga con un gran rizo sobre la frente; sombra amarilla en los ojos y boca en "o"
C('mika-upton', 'chica', P('#e8609a', '#f6c8a0', iris='#a0a030'),
  F(eyes='sharp', brows='angry', mouth='none', hairline=[(6, 60), (20, 44), (40, 36), (60, 34), (80, 42), (94, 60)]),
  dome('front', top=0, w=48, cy=44, long=100, flare=6) + [L(outline([(24, 20), (40, 6), (66, 8), (74, 24), (60, 34), (42, 30)]), 'light', 'f'),
  L(ell(50, 93, 2.2, 2.6), _c('#c04a40'), 'f', False)] + shadow_eyes('#e0c040'),
  dome('side', top=0, w=48, cy=44, long=98, flare=6, fr=42) + [L(outline([(60, 10), (82, 14), (88, 30), (72, 34)]), 'light', 'f')],
  dome('back', top=0, w=48, cy=44, long=98, flare=6, ends=0))

# Millicent "Milli" Vociere: pelo verde menta en casco liso con raya al lado; ojos verdes y boca ondulada
C('millicent-milli-vociere', 'chica', P('#5aa07a', '#f8e0d8', iris='#8ac840'),
  F(eyes='sharp', brows=True, mouth='line', mouth_y=93, hairline=[(6, 66), (16, 50), (30, 44), (44, 50), (60, 40), (80, 46), (94, 66)]),
  dome('front', top=4, w=46, cy=46, sb=72) + [strand([(40, 10), (48, 40)], 'deep', 'b', 1.2)],
  dome('side', top=4, w=46, cy=46, nape=84, fr=54),
  dome('back', top=4, w=46, cy=46, nape=84))

# Mina Veyance: pelo negro azulado corto con mechones de punta que salen a los lados; ojos morados con sombra y sonrisa
C('mina-veyance', 'chica', P('#1a2232', '#f8dcd0', iris='#6a5ab0'),
  F(eyes='big', brows='angry', mouth='smile', mouth_y=93, hairline=[(6, 62), (18, 48), (34, 40), (50, 48), (66, 40), (82, 48), (94, 62)]),
  dome('front', top=2, w=46, cy=46, sb=64) + [L(outline([(10, 40), (-10, 30, 1), (4, 50), (-8, 62, 1), (12, 60)])), L(outline([(90, 40), (110, 30, 1), (96, 50), (108, 62, 1), (88, 60)]))] + shadow_eyes('#6a6a90'),
  dome('side', top=2, w=46, cy=46, nape=82, fr=50) + [L(outline([(10, 40), (-12, 30, 1), (2, 52), (-8, 64, 1), (14, 62)]))],
  dome('back', top=2, w=46, cy=46, nape=82) + [L(outline([(10, 40), (-10, 30, 1), (4, 50), (-8, 62, 1), (12, 60)])), L(outline([(90, 40), (110, 30, 1), (96, 50), (108, 62, 1), (88, 60)]))])

# Minerva Elderbright: melena azul acero larga y lisa con flequillo recto; ojos castaños rojizos y sonrisa
C('minerva-elderbright', 'chica', P('#3a6a8a', '#f8dcd0', iris='#a05030'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 66), (14, 52), (30, 54), (50, 54), (70, 54), (86, 52), (94, 66)]),
  dome('front', top=2, w=46, cy=46, long=104, flare=4) + [strand([(30, 30), (30, 52)], 'deep', 'f', 1.0), strand([(50, 30), (50, 52)], 'deep', 'f', 1.0), strand([(70, 30), (70, 52)], 'deep', 'f', 1.0)],
  dome('side', top=2, w=46, cy=46, long=102, flare=4, fr=56),
  dome('back', top=2, w=46, cy=46, long=102, flare=4, ends=0))

# Minna Smallwood: pelo lila con mechas rosas, flequillo largo y una coleta alta a un lado con lazo rosa; ojos amarillos y ceño
PNK = _c('#f0a0d0')
C('minna-smallwood', 'chica', P('#a878d8', '#f8dcd0', iris='#d8c030'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=[(6, 70), (16, 52), (30, 56), (40, 50), (50, 58), (60, 50), (70, 56), (84, 52), (94, 70)]),
  [tail(14, 18, -18, 40, 16), L(ell(16, 14, 6, 4), PNK, 'b')] + dome('front', top=2, w=46, cy=46, long=86, flare=4) +
  [strand([(30, 20), (30, 50)], PNK, 'f', 2.0), strand([(64, 20), (66, 50)], PNK, 'f', 2.0), strand([(84, 50), (86, 84)], PNK, 'b', 2.0)],
  [tail(30, 12, -24, 40, 16), L(ell(30, 10, 6, 4), PNK, 'b')] + dome('side', top=2, w=46, cy=46, long=84, flare=4, fr=56),
  [tail(86, 18, 18, 40, 16), L(ell(84, 14, 6, 4), PNK)] + dome('back', top=2, w=46, cy=46, long=84, flare=4, ends=0))

# Minty Shuttlebrook: melena índigo hasta los hombros con raya al lado y las puntas hacia dentro; ojos turquesa y mofletes rosas
C('minty-shuttlebrook', 'chica', P('#4a4a90', '#f8dcd0', iris='#3ab0b8'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 66), (16, 50), (26, 40), (40, 36), (52, 46), (66, 40), (82, 48), (94, 66)]),
  dome('front', top=0, w=50, cy=46, long=96, flare=-2) + blush(),
  dome('side', top=0, w=50, cy=46, long=94, flare=-2, fr=50),
  dome('back', top=0, w=50, cy=46, long=94, flare=-2, ends=0))

# Mira Fiendish: pelo castaño con raya al medio y diadema blanca, dos coletas bajas grises en bucle con gomas naranjas; ojos naranjas
C('mira-fiendish', 'chica', P('#5a3a28', '#f8dcd0', iris='#c87020'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 62), (20, 46), (40, 40), (50, 46), (60, 40), (80, 46), (94, 62)]),
  [tail(12, 62, -10, 30, 12, c=_c('#c0b8b0')), tail(88, 62, 10, 30, 12, c=_c('#c0b8b0')), L(ell(12, 60, 4, 5), _c('#f0a030'), 'b'), L(ell(88, 60, 4, 5), _c('#f0a030'), 'b')] +
  dome('front', top=4, w=46, cy=44, sb=64) + [band(16, 22, _c('#ece4dc'))],
  [tail(26, 62, -14, 30, 12, c=_c('#c0b8b0')), L(ell(26, 60, 4, 5), _c('#f0a030'), 'b')] + dome('side', top=4, w=46, cy=44, nape=80, fr=48) + [band(16, 22, _c('#ece4dc'), 'side')],
  [tail(12, 62, -10, 30, 12, c=_c('#c0b8b0')), tail(88, 62, 10, 30, 12, c=_c('#c0b8b0'))] + dome('back', top=4, w=46, cy=44, nape=80) + [band(16, 22, _c('#ece4dc'), 'back')])

# Mireille Modelle (portera): turbante azul que le envuelve la cabeza con el pelo rubio asomando arriba y una coleta
# rubia larga que le cae por un lado; ojos azules y sombra rosa
BLU = _c('#3a5aa8')
C('mireille-modelle', 'chica', P('#e8c870', '#f8e0d8', iris='#3a5aa8'),
  F(eyes='sharp', brows=True, mouth='line', mouth_y=93, face_front=face(chin=104), hairline=[(6, 56), (22, 44), (50, 42), (78, 44), (94, 56)]),
  [L(blob([(22, 14), (34, -4), (60, -6), (76, 10), (60, 14)], 6)), L(outline([(16, 54), (10, 80), (14, 100, 1), (22, 76), (24, 58)]))] +
  [L(outline([(10, 54), (8, 30), (20, 8), (50, 2), (80, 8), (92, 30), (90, 54), (70, 44), (50, 42), (30, 44)]), BLU, 'f'), strand([(14, 34), (88, 22)], _c('#2a4a90'), 'f', 1.4)] + shadow_eyes('#e090a0'),
  [L(blob([(26, 10), (40, -6), (66, -4), (76, 12)], 6)), L(outline([(50, 60), (44, 84), (48, 100, 1), (56, 80)])),
   L(outline([(54, 56), (66, 44), (86, 40), (90, 22), (72, 4), (40, 2), (14, 14), (6, 40), (14, 60), (34, 64)]), BLU)],
  [L(blob([(24, 12), (36, -6), (64, -6), (78, 12)], 6)), L(outline([(76, 54), (82, 80), (78, 100, 1), (70, 76)])),
   L(outline([(10, 62), (8, 30), (20, 8), (50, 2), (80, 8), (92, 30), (90, 62), (50, 68)]), BLU)])

# Miriam Masheene (portera): piel morena, pelo negro en mechones de punta con mechas rojas y un mechón entre los ojos; ojos rojos
RD = _c('#c02a2a')
C('miriam-masheene', 'chica', P('#1e1a1e', '#b88a6a', iris='#d02a2a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=[(6, 70), (16, 52), (30, 48), (44, 66), (50, 76), (56, 66), (70, 48), (84, 52), (94, 70)]),
  dome('front', top=2, w=48, cy=46, n=8, amp=8, seed=113, long=86, flare=10) + [L(outline([(20, 30), (36, 4), (40, 8), (26, 40), (18, 60, 1), (16, 44)]), RD, 'f'),
  L(outline([(46, 6), (40, -10, 1), (54, 2)])), L(outline([(26, -2), (44, -8), (30, 4)]), RD, 'b')],
  dome('side', top=2, w=48, cy=46, n=8, amp=8, seed=113, long=84, flare=10, fr=60) + [L(outline([(60, 10), (80, 16), (74, 22), (58, 18)]), RD, 'f')],
  dome('back', top=2, w=48, cy=46, n=8, amp=8, seed=113, long=84, flare=10, ends=4) + [L(outline([(70, 20), (84, 30), (90, 60), (82, 60)]), RD, 'b')])
