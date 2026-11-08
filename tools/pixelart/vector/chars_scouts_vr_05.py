"""Ojeadores de Victory Road (scouts-vr), tanda 05: dibujados a partir de su retrato; claves 'scouts-vr:<id>'.

Casi todos salen del retrato (frente) y el perfil y la espalda se deducen de cómo cae su peinado; los que tienen modelo
3D del mismo personaje (Howell Bloomhurst, Ibuto Shinohara, Jennifer Mystic Prittia, Josephine, Kendrick Townsend, Kota)
lo usan para el perfil y la espalda. Ayudas propias: bun() (moños y bolas), puffs() (nube de rizos), bangs() (flequillo
recto por delante), mir() (simetría con puntas) y specs()."""
import math
import random

from chars import CHARS, L, OUTC, blob, ell, longhair, outline, pal, rope, strand  # noqa: F401
from chars_scouts_ie1_03 import rect_specs, round_specs, stache, thick_brows  # noqa: F401
from chars_scouts_ie1_09 import dome, face, face_side, hl, mark  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401

K = 'scouts-vr:'
WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)


def _c(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5)) + (255,)


def F(**k):
    d = {'eyes': 'normal', 'mouth': 'line'}
    d.update(k)
    return d


def P(hair, skin, iris='#302232', **k):
    return pal(hair, skin, iris, **k)


def C(pid, body, palette, f, front, side, back):
    """El nacimiento del pelo baja por el borde de la cara hasta la barbilla (su raya no cruza el pelo de los lados)."""
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[K + pid] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def mir(pts):
    return [(100 - p[0],) + tuple(p[1:]) for p in pts]


def bun(x, y, rx, ry=None, c='mid', z='b', sil=True):
    return L(ell(x, y, rx, ry or rx), c, z, sil)


def puffs(cx, cy, rx, ry, n=9, amp=0.16, c='mid', z='b', seed=1, sil=True):
    """Nube de rizos: contorno de bultos redondos alrededor de (cx, cy)."""
    rnd = random.Random(seed)
    pts = []
    for i in range(n * 2):
        a = 2 * math.pi * i / (n * 2)
        k = 1.0 if i % 2 == 0 else 1 - amp * rnd.uniform(0.7, 1.2)
        pts.append((cx + rx * k * math.cos(a), cy + ry * k * math.sin(a)))
    return L(blob(pts, 6), c, z, sil)


def bangs(y=58, x0=14, x1=86, top=18, c='mid', n=0, amp=5):
    """Flequillo recto por delante de la frente hasta y (n > 0: acabado en n mechones de punta)."""
    pts = [(x0 - 2, y + 2), (x0, 36), (30, top + 6), (50, top), (70, top + 6), (x1, 36), (x1 + 2, y + 2)]
    if n:
        for i in range(n):
            x = x1 - (i + 0.5) * (x1 - x0) / n
            pts += [(x + (x1 - x0) / n / 2, y - amp), (x, y, 1)]
    return L(outline(pts), c, 'f')


def specs(view, c, y=76, kind='round', **k):
    return round_specs(view, c, y=y, **k) if kind == 'round' else rect_specs(view, c, y=y, **k)


def side_bangs(y=58, c='mid'):
    """Flequillo de perfil: un saliente por delante de la frente."""
    return L(outline([(56, 22), (82, 30), (90, y - 6), (86, y, 1), (76, y - 4), (64, 40)]), c, 'f')


# ------------------------------------------------------------------ jugadores

# Henrietta Kettingham: melena gris lisa con flequillo recto (corte hime) y mechones que caen por delante de las orejas
# hasta los hombros; ojos grandes morados y media sonrisa
C('henrietta-kettingham', 'chica', P('#a3a1b0', '#fbe8e0', iris='#7a4aa0'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=94, hairline=[(6, 62), (16, 58), (84, 58), (94, 62)]),
  longhair('front', length=104, flare=2, top=2) + [bangs(60, top=16),
                                                   L(outline([(16, 58), (24, 60), (24, 104), (14, 108, 1), (12, 80)]), 'mid', 'f'),
                                                   L(outline(mir([(16, 58), (24, 60), (24, 104), (14, 108, 1), (12, 80)])), 'mid', 'f')],
  longhair('side', length=104, flare=2, top=2) + [side_bangs(60), L(outline([(60, 56), (68, 58), (70, 104), (62, 108, 1), (58, 80)]), 'mid', 'f')],
  longhair('back', length=104, flare=2, top=2, ends=5))

# Hercule Gaillard: pelo corto morado oscuro de mechones de punta hacia arriba y a un lado; piel morena, ojos grises
# afilados y sonrisa enseñando los dientes
C('hercule-gaillard', 'normal', P('#564d71', '#b46d5b', iris='#8a8a94'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, hairline=hl(5, 64, 50, 58, lean=4, seed=2)),
  dome('front', top=-4, w=44, cy=44, n=7, amp=10, sweep=0.5, seed=5, sb=66),
  dome('side', top=-4, w=44, cy=44, n=7, amp=10, sweep=0.5, seed=5, nape=84, fr=50),
  dome('back', top=-4, w=44, cy=44, n=7, amp=10, sweep=0.5, seed=5, nape=84))

# Hernan Rippett: peluca crema abultada de rizos, con dos caracoles sobre las sienes; piel clara, ceño fruncido y boca
# torcida hacia abajo
C('hernan-rippett', 'normal', P('#e0cfba', '#fcbda1', iris='#a08a5a'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=94, nose=(50, 85, 2.4), hairline=[(6, 66), (20, 56), (34, 50), (50, 52), (66, 50), (80, 56), (94, 66)]),
  [puffs(50, 34, 48, 34, n=9, seed=3), puffs(10, 64, 13, 18, n=5, seed=4), puffs(90, 64, 13, 18, n=5, seed=6),
   L(blob([(64, 6), (92, 30), (96, 60), (80, 44)], 6), 'shade', 'b', False),
   strand(quad((20, 60), (14, 70), (22, 76)) + quad((22, 76), (28, 68), (20, 66))[1:], 'shade', 'f', 1.6),
   strand(quad((80, 60), (86, 70), (78, 76)) + quad((78, 76), (72, 68), (80, 66))[1:], 'shade', 'f', 1.6)],
  [puffs(44, 34, 48, 34, n=9, seed=3), puffs(30, 70, 22, 22, n=6, seed=8), L(blob([(6, 40), (20, 78), (40, 84), (24, 56)], 6), 'shade', 'b', False)],
  [puffs(50, 36, 50, 36, n=9, seed=3), puffs(50, 74, 38, 18, n=7, seed=9), L(blob([(62, 8), (94, 34), (92, 80), (70, 70)], 6), 'shade', 'b', False)])

# Heron Champs: pinchos cian hacia arriba y a los lados, con las puntas de las sienes amarillas; cejas cian gruesas, ojos
# azules y sonrisa de dientes
YEL = _c('#f0d860')
C('heron-champs', 'normal', P('#52ccca', '#f7bf8c', iris='#2a7ad0'),
  F(eyes='sharp', brows=False, mouth='grin', mouth_y=94, hairline=hl(5, 62, 48, 56, seed=4)),
  dome('front', top=-8, w=46, cy=42, n=8, amp=12, seed=11, sb=62) +
  [L(outline([(6, 56), (2, 70, 1), (14, 66), (18, 58)]), YEL, 'b'), L(outline(mir([(6, 56), (2, 70, 1), (14, 66), (18, 58)])), YEL, 'b')] +
  thick_brows(63, 'mid', h=4.6, tilt=0.6),
  dome('side', top=-8, w=46, cy=42, n=8, amp=12, seed=11, nape=82, fr=48) + [L(outline([(50, 60), (54, 74, 1), (60, 62)]), YEL, 'b')],
  dome('back', top=-8, w=46, cy=42, n=8, amp=12, seed=11, nape=82))

# Hexine Cantation: melena larga lila ondulada con flequillo recto; ojos azules muy abiertos, rubor y la boca abierta
C('hexine-cantation', 'chica', P('#b99bd8', '#fbe4d7', iris='#5a8ad0'),
  F(eyes='big', brows=False, mouth='buck', mouth_y=94, hairline=[(6, 62), (16, 58), (84, 58), (94, 62)]),
  longhair('front', length=114, flare=8, top=0) + [bangs(60, top=14, n=7, amp=3), mark([(24, 84), (32, 84), (32, 89), (24, 89)], _c('#f4a0a0')),
                                                   mark([(68, 84), (76, 84), (76, 89), (68, 89)], _c('#f4a0a0'))],
  longhair('side', length=114, flare=8, top=0) + [side_bangs(60)],
  longhair('back', length=114, flare=8, top=0, ends=6))


# Hiatt Heddon: gorro rojo abombado con el borde blanco que le tapa todo el pelo; piel morena, ojos amarillos afilados
# y ceño fruncido
def _hat_hiatt(view):
    R, W = _c('#d54142'), _c('#eef2f2')
    if view == 'front':
        return [L(puffs(50, 22, 50, 24, n=7, seed=2)['s'], R),
                L(outline([(6, 58), (8, 38), (50, 34), (92, 38), (94, 58), (50, 64)]), W),
                L(blob([(62, 4), (96, 18), (96, 34), (70, 30)], 6), _c('#a83034'), 'b', False)]
    if view == 'side':
        return [L(puffs(44, 22, 50, 24, n=7, seed=2)['s'], R), L(outline([(2, 64), (2, 40), (48, 34), (90, 40), (90, 58), (50, 62)]), W)]
    return [L(puffs(50, 22, 50, 24, n=7, seed=2)['s'], R), L(outline([(6, 64), (8, 40), (50, 36), (92, 40), (94, 64), (50, 70)]), W)]


C('hiatt-heddon', 'normal', P('#2a1c18', '#b26a59', iris='#c8901e'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=(66, 62)),
  _hat_hiatt('front'), _hat_hiatt('side'), _hat_hiatt('back') + [L(outline([(14, 66), (16, 84), (50, 90), (84, 84), (86, 66)]), 'mid')])

# Hildy Tattleswell: melena larga morada ondulada con la raya a un lado y un mechón suelto en la frente; ojos morados
# redondos con ojeras y sonrisa de dientes
C('hildy-tattleswell', 'chica', P('#875192', '#fdeae1', iris='#5a3a7a'),
  F(eyes='round', brows=True, mouth='buck', mouth_y=93, hairline=[(6, 64), (14, 52), (30, 44), (44, 46), (56, 42), (72, 46), (86, 54), (94, 64)]),
  longhair('front', length=114, flare=10, top=0) + [strand(quad((44, 34), (40, 52), (46, 62)), 'mid', 'f', 3.2),
                                                    mark([(26, 82), (40, 82)], _c('#c8a0b0'), w=1.2), mark([(60, 82), (74, 82)], _c('#c8a0b0'), w=1.2)],
  longhair('side', length=114, flare=10, top=0),
  longhair('back', length=114, flare=10, top=0, ends=5, part=True))

# Hop Sadler: una nube gris azulada de pelo esponjoso arriba y mechones negros rizados que le caen por la frente y los
# lados; piel morena y ojos morados adormilados
DK = _c('#2e2a36')
C('hop-sadler', 'normal', P('#8486a0', '#c08666', iris='#7a5aa0'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=94, hairline=[(6, 64), (20, 50), (36, 46), (50, 48), (66, 46), (80, 50), (94, 64)]),
  [puffs(50, 24, 48, 24, n=8, seed=5), L(outline([(14, 62), (12, 44), (30, 40), (70, 40), (88, 44), (86, 62), (78, 48), (22, 48)]), DK),
   L(rope((40, 40), (28, 54), (36, 70), 4), DK, 'f'), L(rope((58, 40), (68, 56), (62, 70), 3.6), DK, 'f'),
   L(rope((18, 46), (10, 66), (18, 86), 4), DK, 'b'), L(rope((82, 46), (90, 66), (82, 86), 4), DK, 'b')],
  [puffs(44, 24, 48, 24, n=8, seed=5), L(outline([(6, 60), (4, 42), (30, 38), (72, 40), (88, 48), (72, 50), (56, 56), (48, 74), (26, 72)]), DK),
   L(rope((10, 56), (2, 76), (14, 92), 4.4), DK, 'b'), L(rope((28, 62), (24, 82), (34, 92), 4.4), DK, 'b'), L(rope((82, 46), (92, 60), (86, 72), 3.6), DK, 'f')],
  [puffs(50, 24, 48, 24, n=8, seed=5), L(outline([(8, 64), (6, 44), (50, 38), (94, 44), (92, 64), (50, 70)]), DK)] +
  [L(rope((x, 60), (x - 6, 76), (x + 2, 90), 4.4), DK, 'b') for x in (16, 32, 50, 68, 84)])


# Hope Astor: pelo celeste con dos moños altos en lo alto de la cabeza y dos tirabuzones enormes a los lados que acaban
# en rosa, con mechones grises; ojos rosas y la boca abierta de alegría
def _hope(view):
    PK, GR = _c('#f4a8c0'), _c('#8d9b9e')
    if view == 'front':
        return [bun(30, -4, 12), bun(70, -4, 12),
                L(blob([(16, 30), (2, 56), (-6, 82), (2, 96), (18, 92), (22, 60)], 6), 'mid'),
                L(blob(mir([(16, 30), (2, 56), (-6, 82), (2, 96), (18, 92), (22, 60)]), 6), 'mid'),
                L(blob([(-6, 80), (2, 96), (18, 92), (16, 78)], 6), PK, 'b', False), L(blob(mir([(-6, 80), (2, 96), (18, 92), (16, 78)]), 6), PK, 'b', False),
                strand(quad((14, 40), (6, 60), (8, 78)), GR, 'b', 2.4), strand(quad((86, 40), (94, 60), (92, 78)), GR, 'b', 2.4)] + \
            dome('front', top=4, w=44, cy=44, sb=64, seed=1)
    if view == 'side':
        return [bun(42, -2, 12), L(blob([(24, 30), (6, 56), (-2, 84), (8, 96), (24, 90), (30, 60)], 6), 'mid'),
                L(blob([(-2, 82), (8, 96), (24, 90), (22, 78)], 6), PK, 'b', False)] + dome('side', top=4, w=44, cy=44, nape=80, fr=52)
    return [bun(30, -4, 12), bun(70, -4, 12)] + dome('back', top=4, w=44, cy=44, nape=80) + \
        [L(blob([(16, 30), (2, 56), (-6, 82), (2, 96), (18, 92), (22, 60)], 6), 'mid', 'f'),
         L(blob(mir([(16, 30), (2, 56), (-6, 82), (2, 96), (18, 92), (22, 60)]), 6), 'mid', 'f'),
         L(blob([(-6, 80), (2, 96), (18, 92), (16, 78)], 6), PK, 'f', False), L(blob(mir([(-6, 80), (2, 96), (18, 92), (16, 78)]), 6), PK, 'f', False)]


C('hope-astor', 'chica', P('#abe5ea', '#f9e1db', iris='#e07aa0'),
  F(eyes='big', brows=False, mouth='lips', mouth_y=94, mouth_w=6, hairline=hl(5, 62, 50, 58, seed=6)),
  _hope('front'), _hope('side'), _hope('back'))

# Hovard Schulder: grandullón de cara ancha; casco de pelo gris oscuro con picos a los lados; dos manchas grises
# alrededor de los ojos (rojos) y una sonrisa enorme de dientes
GREY = _c('#7a7e86')
C('hovard-schulder', 'corpulento', P('#5a616a', '#f8c7a8', iris='#c02a4a'),
  F(eyes='sharp', brows=False, mouth='grin', mouth_y=96, face_front=face(w=6, chin=104, jaw=3), hairline=[(6, 62), (16, 54), (50, 50), (84, 54), (94, 62)]),
  dome('front', top=2, w=50, cy=46, n=6, amp=8, seed=7, sb=64) +
  [L(outline([(22, 70), (40, 66), (44, 76), (40, 84), (24, 82)]), GREY, 'f'), L(outline(mir([(22, 70), (40, 66), (44, 76), (40, 84), (24, 82)])), GREY, 'f'),
   L(ell(37, 76, 2.6, 2.2), _c('#d02a5a'), 'f', False), L(ell(63, 76, 2.6, 2.2), _c('#d02a5a'), 'f', False)],
  dome('side', top=2, w=50, cy=46, n=6, amp=8, seed=7, nape=84, fr=50) + [L(outline([(72, 68), (86, 66), (88, 80), (74, 82)]), GREY, 'f')],
  dome('back', top=2, w=50, cy=46, n=6, amp=8, seed=7, nape=84))

# Howell Bloomhurst (con modelo 3D): adulto de cara larga y piel morena; pelo castaño muy oscuro peinado hacia atrás con
# dos franjas grises en las sienes y mechones que caen por la nuca; cejas fruncidas, boca seria
SILVER = _c('#b8b4b8')
C('howell-bloomhurst', 'delgado', P('#2e2026', '#ad7b6c', iris='#4a6a9a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=98, face_front=face(chin=106, jaw=1), face_side=face_side(chin=6),
    hairline=[(6, 62), (18, 48), (34, 40), (50, 44), (66, 40), (82, 48), (94, 62)]),
  dome('front', top=6, w=44, cy=44, sb=74, seed=2) +
  [L(outline([(14, 54), (24, 40), (40, 34), (30, 44), (20, 60)]), SILVER, 'b'), L(outline(mir([(14, 54), (24, 40), (40, 34), (30, 44), (20, 60)])), SILVER, 'b'),
   L(outline([(8, 60), (2, 82, 1), (14, 76), (16, 64)]), 'mid'), L(outline(mir([(8, 60), (2, 82, 1), (14, 76), (16, 64)])), 'mid')],
  dome('side', top=6, w=44, cy=44, nape=92, fr=44, seed=2) + [L(outline([(54, 40), (72, 30), (60, 46)]), SILVER, 'f'),
                                                               L(outline([(4, 70), (-2, 94, 1), (14, 88), (20, 96, 1), (26, 84)]), 'mid')],
  dome('back', top=6, w=44, cy=44, nape=92, seed=2) + [L(outline([(10, 80), (16, 100, 1), (30, 90), (50, 102, 1), (70, 90), (84, 100, 1), (90, 80)]), 'mid')])

# Huxley Tagg: pelo verde oliva en una mata enorme como un brócoli; piel clara, ojos afilados, pecas y los dos dientes
# de delante
C('huxley-tagg', 'normal', P('#6c791f', '#fae6d7', iris='#202020'),
  F(eyes='sharp', brows='angry', mouth='buck', mouth_y=95, hairline=(60, 54)),
  [puffs(50, 18, 52, 32, n=10, amp=0.12, seed=12), L(blob([(62, -8), (98, 12), (96, 36), (70, 28)], 6), 'shade', 'b', False),
   mark([(30, 86), (31, 87)], _c('#8a5a40'), w=1.6), mark([(34, 88), (35, 89)], _c('#8a5a40'), w=1.6),
   mark([(66, 86), (67, 87)], _c('#8a5a40'), w=1.6), mark([(70, 88), (71, 89)], _c('#8a5a40'), w=1.6)],
  [puffs(44, 18, 52, 32, n=10, amp=0.12, seed=12), L(outline([(16, 46), (40, 44), (52, 60), (48, 74), (26, 72), (14, 60)]), 'mid')],
  [puffs(50, 18, 52, 32, n=10, amp=0.12, seed=12), L(outline([(16, 44), (84, 44), (82, 70), (50, 76), (18, 70)]), 'mid')])

# Ibuto Shinohara (con modelo 3D): anciano de piel morena; pelo morado grisáceo peinado hacia atrás pegado a la cabeza;
# cejas negras pobladas, bigote negro muy largo con las puntas caídas y perilla gris larga
BEARD = _c('#9a9098')
C('ibuto-shinohara', 'delgado', P('#6a4a58', '#bf8e7c', iris='#2a2028', deep='#2a1c22'),
  F(eyes='sharp', brows=False, mouth='none', mouth_y=98, face_front=face(chin=106, jaw=1), face_side=face_side(chin=6),
    hairline=[(6, 62), (18, 46), (34, 38), (50, 40), (66, 38), (82, 46), (94, 62)]),
  dome('front', top=4, w=44, cy=44, sb=70, seed=3) + thick_brows(64, 'deep', h=5, tilt=0.4, w=16) +
  [L(blob([(44, 112), (50, 96), (56, 112), (50, 128)], 6), BEARD, 'f'),
   L(blob([(50, 92), (60, 90), (74, 96), (80, 108), (70, 100), (50, 98), (30, 100), (20, 108), (26, 96), (40, 90)], 6), 'deep', 'f')],
  dome('side', top=4, w=44, cy=44, nape=84, fr=42, seed=3) +
  [L(blob([(70, 64), (82, 60), (88, 66), (76, 68)], 4), 'deep', 'f'), L(blob([(78, 92), (90, 90), (88, 100), (80, 112), (76, 100)], 6), 'deep', 'f'),
   L(blob([(80, 100), (88, 104), (84, 124), (78, 110)], 6), BEARD, 'f')],
  dome('back', top=4, w=44, cy=44, nape=84, seed=3))

# Ignacio Gerhardt: grandullón; pelo rojo en cepillo alto sobre la frente y patillas y barba castaño oscuro que le rodean
# la cara; piel morena, ceño fruncido y boca apretada
BRD = _c('#3d342e')
C('ignacio-gerhardt', 'corpulento', P('#d95055', '#c18567', iris='#3a5a8a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, face_front=face(w=4, chin=104, jaw=3), hairline=(58, 54), nose=(50, 85, 3)),
  [L(outline([(12, 58), (10, 24), (16, 12, 1), (28, 10), (36, 2, 1), (50, 8), (64, 2, 1), (72, 10), (84, 12, 1), (90, 24), (88, 58), (80, 46), (20, 46)])), L(blob([(62, 6), (90, 18), (88, 46), (72, 40)], 6), 'shade', 'b', False),
   L(outline([(12, 56), (19, 52), (19, 82), (34, 101), (50, 105), (66, 101), (81, 82), (81, 52), (88, 56), (88, 90), (70, 110), (50, 114), (30, 110), (12, 90)]), BRD, 'f')],
  [L(outline([(10, 56), (6, 22), (20, 6), (50, 2), (80, 6), (92, 20), (90, 46), (60, 48), (40, 56)])),
   L(outline([(48, 54), (58, 52), (60, 80), (74, 100), (84, 104), (78, 110), (58, 108), (48, 94)]), BRD, 'f')],
  [L(outline([(10, 60), (8, 20), (20, 6), (50, 2), (80, 6), (92, 20), (90, 60), (50, 64)])), L(outline([(12, 60), (88, 60), (84, 84), (50, 90), (16, 84)]), BRD)])

# Inga Calmari: pelo celeste en un casco abombado con dos coletas cortas que se levantan a los lados (gomas rojas);
# cejas celestes gruesas, sombra celeste en los ojos y la boca pequeña
REDT = _c('#d03a3a')
C('inga-calmari', 'chica', P('#76bfc7', '#fae4d5', iris='#3a9ab0'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=94, hairline=[(6, 62), (18, 52), (34, 48), (50, 50), (66, 48), (82, 52), (94, 62)]),
  dome('front', top=4, w=46, cy=44, sb=66, seed=2) +
  [L(outline([(10, 22), (-4, 6), (-10, 12, 1), (2, 2), (-12, -4, 1), (6, 8), (16, 18)])), L(outline(mir([(10, 22), (-4, 6), (-10, 12, 1), (2, 2), (-12, -4, 1), (6, 8), (16, 18)]))),
   bun(10, 20, 3, c=REDT, z='f'), bun(90, 20, 3, c=REDT, z='f')] + thick_brows(64, 'mid', h=4, w=14),
  dome('side', top=4, w=46, cy=44, nape=82, fr=52, seed=2) + [L(outline([(36, 8), (24, -10), (16, -8, 1), (30, 4)])), bun(36, 8, 3, c=REDT, z='f')],
  dome('back', top=4, w=46, cy=44, nape=82, seed=2) + [L(outline([(10, 22), (-4, 6), (-10, 12, 1), (2, 2), (-12, -4, 1), (6, 8), (16, 18)]), 'mid', 'f'),
                                                       L(outline(mir([(10, 22), (-4, 6), (-10, 12, 1), (2, 2), (-12, -4, 1), (6, 8), (16, 18)])), 'mid', 'f')])

# Iro Armussel: pinchos azul marino muy oscuros abiertos hacia arriba y los lados; marcas azules bajo los ojos afilados,
# media sonrisa
BLU = _c('#2a5ab0')
C('iro-armussel', 'normal', P('#1f3a50', '#ddb4a5', iris='#4a7ac0'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=95, hairline=hl(5, 62, 50, 58, seed=8)),
  dome('front', top=-6, w=48, cy=42, n=9, amp=13, seed=21, sb=64) +
  [mark([(26, 80), (36, 86)], BLU, w=1.6), mark([(74, 80), (64, 86)], BLU, w=1.6)],
  dome('side', top=-6, w=48, cy=42, n=9, amp=13, seed=21, nape=82, fr=50) + [mark([(78, 81), (84, 86)], BLU, w=1.6)],
  dome('back', top=-6, w=48, cy=42, n=9, amp=13, seed=21, nape=82))

# Isanna Countenford: pelo castaño recogido en un casco liso con dos coletitas bajas detrás de las orejas; cara redonda,
# ojos morados caídos, rubor y la boca triste
C('isanna-countenford', 'chica', P('#684f3e', '#fac5a5', iris='#7a5aa0'),
  F(eyes='normal', brows=False, mouth='frown', mouth_y=95, face_front=face(w=3, chin=102), hairline=[(6, 60), (18, 48), (34, 44), (50, 46), (66, 44), (82, 48), (94, 60)]),
  dome('front', top=6, w=44, cy=44, sb=60, seed=1) + [puffs(10, 92, 6, 8, n=4, seed=2), puffs(90, 92, 6, 8, n=4, seed=3),
                                                      mark([(24, 84), (32, 84), (32, 88), (24, 88)], _c('#f4a090')), mark([(68, 84), (76, 84), (76, 88), (68, 88)], _c('#f4a090'))],
  dome('side', top=6, w=44, cy=44, nape=80, fr=50, seed=1) + [puffs(30, 92, 7, 9, n=4, seed=2)],
  dome('back', top=6, w=44, cy=44, nape=80, seed=1) + [puffs(20, 90, 7, 9, n=4, seed=2, z='f'), puffs(80, 90, 7, 9, n=4, seed=3, z='f')])

# Isolde Bourgeon: melena roja oscura enmarañada y llena de picos, con dos trenzas que caen por delante; ojos rojos de
# enfado, rubor en la nariz y la boca torcida
C('isolde-bourgeon', 'chica', P('#822723', '#f0b385', iris='#c02a2a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, nose=(50, 85, 2.6), hairline=hl(6, 64, 50, 60, jit=3, seed=9)),
  dome('front', top=-6, w=52, cy=44, n=12, amp=10, seed=31, sb=78) +
  [L(rope((20, 80), (16, 100), (22, 118), 6), 'mid', 'f'), L(rope((80, 80), (84, 100), (78, 118), 6), 'mid', 'f'),
   bun(22, 112, 2.6, c=_c('#e0b030'), z='f'), bun(78, 112, 2.6, c=_c('#e0b030'), z='f')],
  dome('side', top=-6, w=52, cy=44, n=12, amp=10, seed=31, nape=92, fr=52) + [L(rope((60, 82), (64, 100), (60, 118), 6), 'mid', 'f')],
  dome('back', top=-6, w=52, cy=44, n=12, amp=10, seed=31, nape=94) + [L(rope((24, 80), (20, 100), (26, 118), 6), 'mid', 'b'), L(rope((76, 80), (80, 100), (74, 118), 6), 'mid', 'b')])

# Ivo Woodward: melena verde salvia ondulada hasta los hombros, con mechones que se rizan hacia fuera; piel muy clara, ojos
# morados afilados y ceño fruncido
C('ivo-woodward', 'delgado', P('#5d7e6c', '#fce4d5', iris='#6a4a9a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=97, face_front=face(chin=104), face_side=face_side(chin=4),
    hairline=[(6, 62), (16, 50), (30, 42), (44, 50), (54, 40), (70, 44), (84, 52), (94, 62)]),
  longhair('front', length=100, flare=12, top=2) + [L(outline([(6, 80), (-8, 74, 1), (2, 70)])), L(outline(mir([(6, 80), (-8, 74, 1), (2, 70)]))),
                                                     strand(quad((48, 28), (40, 46), (44, 60)), 'mid', 'f', 3)],
  longhair('side', length=100, flare=12, top=2),
  longhair('back', length=100, flare=12, top=2, ends=4))

# Iza Improvelli: melena castaña en forma de campana, abombada y con las puntas hacia fuera; flequillo recto; ojos grises
# redondos y la boca seria
C('iza-improvelli', 'chica', P('#8c5643', '#fad5c3', iris='#6a6a70'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=95, hairline=[(6, 62), (16, 56), (84, 56), (94, 62)]),
  [L(outline([(-4, 92, 1), (2, 70), (2, 34), (20, 10), (50, 2), (80, 10), (98, 34), (98, 70), (104, 92, 1), (84, 86), (82, 60), (18, 60), (16, 86)])),
   L(blob([(62, 6), (94, 30), (100, 86), (84, 80), (80, 40)], 6), 'shade', 'b', False), bangs(58, top=12, n=6, amp=2)],
  [L(outline([(54, 70), (56, 86), (40, 92), (10, 96, 1), (0, 70), (2, 34), (20, 8), (50, 0), (78, 8), (92, 28), (92, 50), (70, 48), (60, 56)])), side_bangs(58)],
  [L(outline([(-4, 92, 1), (2, 70), (2, 34), (20, 10), (50, 2), (80, 10), (98, 34), (98, 70), (104, 92, 1), (50, 96)])),
   L(blob([(60, 8), (94, 32), (100, 88), (64, 94)], 6), 'shade', 'b', False)])

# Izekiel Truth: casco de pelo verde claro en forma de seta, más oscuro por arriba, que le baja hasta las mejillas; ojos
# redondos muy abiertos y grises, boca triste
C('izekiel-truth', 'normal', P('#a5b782', '#f8e4d5', iris='#9a9a9a', top='#4b563d'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=95, hairline=[(6, 70), (16, 64), (84, 64), (94, 70)]),
  [L(outline([(-6, 88), (-6, 50), (6, 22), (50, 10), (94, 22), (106, 50), (106, 88), (86, 84), (84, 66), (16, 66), (14, 84)])),
   L(outline([(4, 30), (14, 14), (50, 6), (86, 14), (96, 30), (80, 36), (64, 30), (50, 36), (36, 30), (20, 36)]), 'top'),
   bangs(66, x0=12, x1=88, top=14, n=5, amp=3)],
  [L(outline([(60, 80), (56, 92), (30, 94), (-4, 88), (-6, 50), (6, 22), (50, 8), (84, 16), (96, 34), (96, 64), (80, 66), (66, 66)])),
   L(outline([(0, 34), (14, 14), (50, 4), (84, 14), (96, 32), (70, 36), (40, 32)]), 'top')],
  [L(outline([(-6, 90), (-6, 50), (6, 22), (50, 10), (94, 22), (106, 50), (106, 90), (50, 96)])),
   L(outline([(4, 30), (14, 14), (50, 6), (86, 14), (96, 30), (70, 36), (50, 32), (30, 36)]), 'top')])

# Jackson Bover: pelo morado corto y peinado, más claro en el centro de la frente; ojos morados entornados y sonrisa
C('jackson-bover', 'normal', P('#6d5673', '#f7d0b5', iris='#7a4a8a', light='#a795a8'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=94, hairline=[(6, 62), (18, 52), (34, 48), (50, 56), (66, 48), (82, 52), (94, 62)]),
  dome('front', top=4, w=46, cy=46, sb=62, seed=1) + [strand(quad((46, 20), (44, 36), (48, 52)), 'light', 'b', 3), strand(quad((54, 20), (56, 36), (52, 52)), 'light', 'b', 3)],
  dome('side', top=4, w=46, cy=46, nape=82, fr=52, seed=1),
  dome('back', top=4, w=46, cy=46, nape=82, seed=1))

# Jakell Wardly: grandullón de piel morena y cara ancha; pelo verde muy oscuro con un moño alto y dos bolas de rizos
# a los lados de la cabeza; cejas gruesas y boca torcida
C('jakell-wardly', 'corpulento', P('#1e2e22', '#9f5843', iris='#3a4a6a'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=97, face_front=face(w=7, chin=106, jaw=4), hairline=[(4, 62), (18, 54), (34, 50), (50, 52), (66, 50), (82, 54), (96, 62)]),
  dome('front', top=10, w=48, cy=48, sb=60, seed=1, shade=False) + [bun(50, 2, 9), puffs(0, 64, 13, 16, n=6, seed=3), puffs(100, 64, 13, 16, n=6, seed=4)] +
  thick_brows(63, 'mid', h=5, w=16),
  dome('side', top=10, w=48, cy=48, nape=80, fr=52, seed=1, shade=False) + [bun(42, 4, 9), puffs(28, 66, 16, 18, n=6, seed=3)],
  dome('back', top=10, w=48, cy=48, nape=82, seed=1, shade=False) + [bun(50, 4, 9), puffs(2, 64, 13, 16, n=6, seed=3), puffs(98, 64, 13, 16, n=6, seed=4)])

# Janet Hollilocks: pelo gris oliva con flequillo de mechones rectos y dos mechones largos y finos que caen por delante
# hasta el pecho; ojos verde azulado grandes, cejas firmes y media sonrisa
C('janet-hollilocks', 'chica', P('#79735c', '#fce5d2', iris='#2a9a8a'),
  F(eyes='big', brows='angry', mouth='smile', mouth_y=94, hairline=[(6, 62), (16, 56), (84, 56), (94, 62)]),
  dome('front', top=2, w=46, cy=46, sb=70, seed=3) + [bangs(58, top=14, n=6, amp=4), L(rope((16, 66), (10, 96), (18, 124), 4), 'mid', 'f'),
                                                      L(rope((84, 66), (90, 96), (82, 124), 4), 'mid', 'f')],
  dome('side', top=2, w=46, cy=46, nape=84, fr=52, seed=3) + [side_bangs(58), L(rope((60, 66), (64, 96), (58, 124), 4), 'mid', 'f')],
  dome('back', top=2, w=46, cy=46, nape=84, seed=3) + [L(rope((16, 66), (12, 96), (18, 122), 4), 'mid'), L(rope((84, 66), (88, 96), (82, 122), 4), 'mid')])

# Jaslyn Warbleton: pelo crema corto con una onda enorme echada hacia un lado sobre la cabeza; ojos dorados grandes y
# sonrisa
C('jaslyn-warbleton', 'chica', P('#dbcdbf', '#fbe8df', iris='#c08a2a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=94, hairline=[(6, 62), (18, 50), (30, 44), (46, 48), (60, 40), (76, 46), (88, 54), (94, 62)]),
  dome('front', top=6, w=44, cy=46, sb=64, seed=1) + [L(outline([(10, 34), (14, 10), (40, -6), (78, -10), (106, -2), (96, 8), (70, 4), (50, 14), (30, 30)])),
                                                      L(outline([(60, -6), (100, -4), (90, 4), (68, 2)]), 'shade', 'b', False)],
  dome('side', top=6, w=44, cy=46, nape=80, fr=50, seed=1) + [L(outline([(10, 30), (20, 6), (50, -6), (92, -4), (82, 6), (56, 6), (30, 24)]))],
  dome('back', top=6, w=44, cy=46, nape=80, seed=1) + [L(outline([(10, 34), (14, 10), (40, -6), (78, -10), (106, -2), (96, 8), (70, 4), (50, 14), (30, 30)]))])

# Jasper Chatterly: afro castaño oscuro enorme; gafas rectangulares de montura celeste, ojos entornados y sonrisa
C('jasper-chatterly', 'normal', P('#46383a', '#f6e8da', iris='#5a5a9a'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=95, hairline=[(6, 62), (18, 52), (34, 48), (50, 52), (66, 48), (82, 52), (94, 62)]),
  [puffs(50, 26, 56, 38, n=11, amp=0.1, seed=7), L(blob([(64, -6), (100, 20), (104, 54), (82, 40)], 6), 'shade', 'b', False)] + specs('front', _c('#8acad8'), kind='rect'),
  [puffs(44, 28, 54, 38, n=11, amp=0.1, seed=7)] + specs('side', _c('#8acad8'), kind='rect'),
  [puffs(50, 30, 56, 42, n=11, amp=0.1, seed=7)])

# Javor Bonnaire: pelo azul con raya a un lado, peinado en una onda que cae sobre la frente, con mechas claras; ojos
# azules y sonrisa tranquila
C('javor-bonnaire', 'delgado', P('#1d3c84', '#fbe9df', iris='#3a5aa0', light='#5a8ad8'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=96, face_front=face(chin=104), face_side=face_side(chin=4),
    hairline=[(6, 62), (18, 46), (34, 40), (50, 44), (62, 54), (74, 52), (86, 56), (94, 62)]),
  dome('front', top=2, w=44, cy=44, sb=64, seed=2) + [L(outline([(38, 10), (70, 20), (86, 40), (80, 58, 1), (66, 40), (46, 26)]), 'mid', 'f'),
                                                      strand(quad((44, 14), (70, 26), (78, 50)), 'light', 'f', 2), strand(quad((30, 14), (20, 30), (18, 50)), 'light', 'b', 2)],
  dome('side', top=2, w=44, cy=44, nape=80, fr=48, seed=2) + [strand(quad((40, 8), (70, 18), (84, 40)), 'light', 'f', 2)],
  dome('back', top=2, w=44, cy=44, nape=80, seed=2) + [strand(quad((30, 14), (24, 40), (30, 70)), 'light', 'f', 2)])

# Jayce Chorden: pinchos verde oscuro altísimos hacia arriba; piel morena, ojos verdes afilados con una cicatriz en la
# nariz y media sonrisa
C('jayce-chorden', 'normal', P('#356454', '#b57458', iris='#3aa06a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=95, hairline=hl(5, 62, 50, 58, seed=10)),
  dome('front', top=-20, w=40, cy=40, n=7, amp=18, seed=41, sb=64) + [mark([(44, 78), (56, 82)], _c('#8a4a3a'), w=1.4)],
  dome('side', top=-20, w=40, cy=40, n=7, amp=18, seed=41, nape=82, fr=50),
  dome('back', top=-20, w=40, cy=40, n=7, amp=18, seed=41, nape=82))

# Jayden Durance: pelo negro corto de puntas pequeñas; piel morena, cejas gruesas, ojos oscuros normales y sonrisa
C('jayden-durance', 'normal', P('#2e2d36', '#c68c78', iris='#2a2a2a'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=95, hairline=hl(6, 62, 48, 54, seed=11)),
  dome('front', top=10, w=44, cy=48, n=12, amp=3, seed=51, sb=62) + thick_brows(63, 'mid', h=4.2, w=14),
  dome('side', top=10, w=44, cy=48, n=12, amp=3, seed=51, nape=80, fr=50),
  dome('back', top=10, w=44, cy=48, n=12, amp=3, seed=51, nape=80))

# Jella Fisker: melena azul en media melena con las puntas moradas que se rizan, y unos tirabuzones que le caen por
# delante; ojos morados entornados y la boca pequeña
PUR = _c('#8a6ac8')
C('jella-fisker', 'chica', P('#4d83c0', '#f8e2d4', iris='#8a6ac0'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=95, hairline=[(6, 62), (18, 54), (30, 58), (40, 50), (50, 58), (60, 50), (70, 58), (82, 54), (94, 62)]),
  longhair('front', length=96, flare=6, top=2) + [L(blob([(-4, 84), (6, 98), (16, 94), (16, 80)], 6), PUR, 'b', False), L(blob(mir([(-4, 84), (6, 98), (16, 94), (16, 80)]), 6), PUR, 'b', False),
                                                  L(rope((16, 76), (8, 98), (16, 116), 6), 'mid', 'f'), L(rope((84, 76), (92, 98), (84, 116), 6), 'mid', 'f'),
                                                  L(blob([(6, 104), (16, 118), (24, 106)], 6), PUR, 'f', False), L(blob(mir([(6, 104), (16, 118), (24, 106)]), 6), PUR, 'f', False),
                                                  strand(quad((40, 30), (34, 46), (40, 54)), PUR, 'f', 2.2), strand(quad((58, 30), (64, 46), (58, 54)), PUR, 'f', 2.2)],
  longhair('side', length=96, flare=6, top=2) + [L(rope((60, 76), (66, 98), (58, 116), 6), 'mid', 'f')],
  longhair('back', length=96, flare=6, top=2, ends=4) + [L(blob([(-4, 84), (6, 100), (94, 100), (104, 84), (50, 92)], 6), PUR, 'f', False)])


# Jennifer Mystic Prittia (con modelo 3D): lleva una cabeza de osito amarillo con un lazo rosa encima: orejas redondas,
# el hocico crema con la nariz negra y la boca abierta, y los ojos negros redondos
def _bear(view):
    Y, CR, BR, PK = _c('#fedb1a'), _c('#f2e5d0'), _c('#c8901a'), _c('#f490a0')
    if view == 'front':
        return [bun(10, 24, 16, c=Y), bun(90, 24, 16, c=Y), bun(10, 24, 8, c=BR, z='f', sil=False), bun(90, 24, 8, c=BR, z='f', sil=False),
                L(blob([(6, 70), (8, 34), (26, 10), (50, 4), (74, 10), (92, 34), (94, 70), (84, 102), (50, 114), (16, 102)], 6), Y, 'f'),
                L(blob([(30, 76), (50, 64), (70, 76), (68, 100), (50, 108), (32, 100)], 6), CR, 'f', False),
                L(ell(50, 76, 8, 6), BLACK, 'f', False), L(blob([(40, 92), (50, 88), (60, 92), (56, 102), (44, 102)], 6), _c('#d06a6a'), 'f', False),
                L(ell(28, 66, 4.6, 4.6), BLACK, 'f', False), L(ell(72, 66, 4.6, 4.6), BLACK, 'f', False),
                L(ell(27, 64.6, 1.4, 1.4), WHITE, 'f', False), L(ell(71, 64.6, 1.4, 1.4), WHITE, 'f', False),
                L(blob([(30, 2), (50, 8), (70, 2), (64, 14), (50, 12), (36, 14)], 6), PK, 'f'), L(blob([(28, 80), (36, 82), (28, 86)], 4), _c('#f8b060'), 'f', False)]
    if view == 'side':
        return [bun(36, 14, 15, c=Y), L(blob([(8, 64), (10, 28), (34, 6), (64, 6), (88, 26), (96, 56), (110, 76), (104, 94), (80, 108), (40, 110), (14, 94)], 6), Y, 'f'),
                L(blob([(84, 66), (106, 72), (108, 92), (90, 100), (80, 84)], 6), CR, 'f', False), L(ell(104, 76, 4, 4), BLACK, 'f', False),
                L(ell(74, 58, 3.6, 4.6), BLACK, 'f', False), L(blob([(40, 4), (60, 6), (56, 14), (44, 14)], 6), PK, 'f')]
    return [bun(10, 24, 16, c=Y), bun(90, 24, 16, c=Y),
            L(blob([(6, 70), (8, 34), (26, 10), (50, 4), (74, 10), (92, 34), (94, 70), (84, 102), (50, 112), (16, 102)], 6), Y, 'f'),
            L(blob([(60, 12), (90, 36), (92, 74), (80, 100), (64, 104)], 6), _c('#e0b810'), 'f', False),
            L(blob([(30, 2), (50, 8), (70, 2), (64, 14), (50, 12), (36, 14)], 6), PK, 'f')]


C('jennifer-mystic-prittia', 'chica', P('#fedb1a', '#f8d8b8'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True), _bear('front'), _bear('side'), _bear('back'))

# Jensen Nariopoulos: pelo naranja rojizo largo y abultado que le cae como una capucha hasta el cuello, con mechones
# rizados sobre la frente; ojos azules tristes y la boca seria
C('jensen-nariopoulos', 'normal', P('#c35124', '#fce5d4', iris='#4a8ab0', deep='#702b1d'),
  F(eyes='normal', brows=False, mouth='line', mouth_y=95, hairline=[(6, 62), (18, 54), (30, 58), (40, 52), (50, 58), (60, 52), (70, 58), (82, 54), (94, 62)]),
  longhair('front', length=104, flare=4, top=-4) + [strand(quad((30, 48), (24, 56), (32, 62)), 'deep', 'f', 2), strand(quad((50, 46), (44, 56), (50, 62)), 'deep', 'f', 2),
                                                    strand(quad((70, 48), (76, 56), (68, 62)), 'deep', 'f', 2), L(blob([(4, 40), (0, 80), (8, 104), (16, 84)], 6), 'deep', 'b', False)],
  longhair('side', length=104, flare=4, top=-4),
  longhair('back', length=104, flare=4, top=-4, ends=3))

# Jeremy Yung: pelo gris corto en mechones de punta peinados hacia abajo; piel morena, ojos verde azulado con pestañas
# marcadas, cejas grises fruncidas y la boca apretada
C('jeremy-yung', 'normal', P('#a19e9f', '#c68b77', iris='#2aa0a8'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=hl(6, 62, 48, 58, seed=12)),
  dome('front', top=6, w=45, cy=46, n=9, amp=4, seed=61, sb=64),
  dome('side', top=6, w=45, cy=46, n=9, amp=4, seed=61, nape=82, fr=50),
  dome('back', top=6, w=45, cy=46, n=9, amp=4, seed=61, nape=82))

# Jerome Knight: melena granate lisa y larga hasta la barbilla, con un mechón cruzándole la cara y una horquilla negra;
# parche negro en el ojo derecho; piel tostada
C('jerome-knight', 'delgado', P('#7a0c1a', '#ddb3a5', iris='#a08a3a'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=97, face_front=face(chin=104), face_side=face_side(chin=4),
    hairline=[(6, 62), (18, 50), (34, 42), (50, 46), (66, 42), (82, 50), (94, 62)]),
  longhair('front', length=102, flare=4, top=0) + [L(blob([(24, 70), (44, 66), (44, 82), (26, 84)], 6), BLACK, 'f', False),
                                                   strand([(20, 66), (46, 60), (80, 44)], BLACK, 'f', 1.4),
                                                   strand(quad((40, 30), (30, 60), (36, 90)), 'mid', 'f', 3.2), L([(70, 38), (82, 34)], BLACK, 'f', False, False, 2.4)],
  longhair('side', length=102, flare=4, top=0) + [L([(70, 38), (82, 34)], BLACK, 'f', False, False, 2.4)],
  longhair('back', length=102, flare=4, top=0, ends=5) + [strand([(10, 60), (90, 60)], BLACK, 'f', 1.4)])

# Jester Biggs: pelo rojo rosado corto con un remolino en la frente; gafas redondas de montura negra gruesa y sonrisa
C('jester-biggs', 'normal', P('#a04f58', '#f9d7c8', iris='#5a4a3a'),
  F(eyes='dot', brows=False, mouth='smile', mouth_y=95, hairline=[(6, 62), (18, 52), (34, 48), (46, 54), (54, 46), (66, 50), (82, 52), (94, 62)]),
  dome('front', top=6, w=44, cy=46, sb=62, seed=1) + specs('front', BLACK, w=2.6, rx=9, ry=7.5),
  dome('side', top=6, w=44, cy=46, nape=80, fr=52, seed=1) + specs('side', BLACK, w=2.6),
  dome('back', top=6, w=44, cy=46, nape=80, seed=1))

# Jett Allegri: pelo castaño rojizo peinado hacia arriba en un tupé de mechones y corto a los lados; piel morena, ojos
# amarillos y cejas fruncidas
C('jett-allegri', 'normal', P('#84402c', '#c18667', iris='#d0b030'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=[(6, 62), (16, 48), (30, 42), (50, 46), (70, 42), (84, 48), (94, 62)]),
  dome('front', top=6, w=44, cy=46, sb=62, seed=1, shade=False) + [L(outline([(16, 30), (12, 10), (24, -6, 1), (34, 6), (44, -12, 1), (56, 2), (72, -6, 1), (76, 10), (90, 20), (84, 36)])),
                                                                   L(blob([(56, 0), (76, -2), (88, 22), (80, 32)], 6), 'shade', 'b', False)],
  dome('side', top=6, w=44, cy=46, nape=80, fr=48, seed=1, shade=False) + [L(outline([(30, 24), (34, 0), (50, -14, 1), (60, 0), (80, -4, 1), (90, 14), (88, 34), (60, 30)]))],
  dome('back', top=6, w=44, cy=46, nape=80, seed=1, shade=False) + [L(outline([(16, 30), (12, 10), (24, -6, 1), (34, 6), (44, -12, 1), (56, 2), (72, -6, 1), (76, 10), (90, 20), (84, 36)]))])

# Jewelyn Plunkett: melena larga caqui con dos mechones de antena levantados en la coronilla; marcas negras en las
# mejillas, ojos claros enfadados y la boca abierta
C('jewelyn-plunkett', 'chica', P('#a0987a', '#fcdcd0', iris='#8a8a6a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=[(6, 62), (18, 48), (30, 42), (40, 50), (50, 44), (60, 50), (70, 42), (82, 48), (94, 62)]),
  longhair('front', length=112, flare=10, top=2) + [L(outline([(40, 8), (30, -18, 1), (46, 4)])), L(outline([(50, 6), (48, -22, 1), (56, 6)])),
                                                    mark([(22, 82), (32, 86)], BLACK, w=1.6), mark([(78, 82), (68, 86)], BLACK, w=1.6)],
  longhair('side', length=112, flare=10, top=2) + [L(outline([(44, 4), (36, -20, 1), (52, 2)]))],
  longhair('back', length=112, flare=10, top=2, ends=5) + [L(outline([(40, 8), (30, -18, 1), (46, 4)])), L(outline([(50, 6), (48, -22, 1), (56, 6)]))])


# Josephine (con modelo 3D): lleva una capucha de gato siamés: cara negra con sombra morada en los ojos azules, el borde
# blanco alrededor y dos orejas negras altísimas de punta
def _cat(view):
    DK2, WH, PU, IN = _c('#3a3234'), _c('#f2eef0'), _c('#b48aa8'), _c('#6a4a5a')
    if view == 'front':
        return [L(outline([(16, 30), (8, -30, 1), (40, 16)]), DK2), L(outline(mir([(16, 30), (8, -30, 1), (40, 16)])), DK2),
                L(outline([(18, 24), (14, -18, 1), (32, 14)]), IN, 'b', False), L(outline(mir([(18, 24), (14, -18, 1), (32, 14)])), IN, 'b', False),
                L(blob([(4, 70), (8, 34), (28, 12), (50, 8), (72, 12), (92, 34), (96, 70), (84, 100), (50, 112), (16, 100)], 6), WH, 'f'),
                L(blob([(16, 66), (22, 38), (50, 26), (78, 38), (84, 66), (72, 94), (50, 104), (28, 94)], 6), DK2, 'f', False),
                L(blob([(22, 70), (32, 62), (44, 68), (40, 76), (26, 78)], 6), PU, 'f', False), L(blob(mir([(22, 70), (32, 62), (44, 68), (40, 76), (26, 78)]), 6), PU, 'f', False),
                L(ell(34, 74, 6.4, 4.8), _c('#6a9ae0'), 'f', False), L(ell(66, 74, 6.4, 4.8), _c('#6a9ae0'), 'f', False),
                L(ell(34, 74, 1.8, 3.6), BLACK, 'f', False), L(ell(66, 74, 1.8, 3.6), BLACK, 'f', False),
                L([(46, 90), (50, 93), (54, 90)], WH, 'f', False, False, 1.2)]
    if view == 'side':
        return [L(outline([(30, 30), (18, -28, 1), (50, 14)]), DK2),
                L(blob([(6, 66), (10, 32), (34, 10), (64, 8), (88, 26), (96, 60), (90, 96), (60, 112), (24, 104)], 6), WH, 'f'),
                L(blob([(60, 30), (86, 34), (96, 62), (90, 92), (70, 102), (62, 70)], 6), DK2, 'f', False),
                L(ell(84, 74, 3.6, 4), _c('#6a9ae0'), 'f', False)]
    return [L(outline([(16, 30), (8, -30, 1), (40, 16)]), DK2), L(outline(mir([(16, 30), (8, -30, 1), (40, 16)])), DK2),
            L(blob([(4, 70), (8, 34), (28, 12), (50, 8), (72, 12), (92, 34), (96, 70), (84, 100), (50, 112), (16, 100)], 6), WH, 'f'),
            L(blob([(60, 14), (90, 36), (94, 72), (82, 100), (62, 104)], 6), _c('#d8d0d6'), 'f', False)]


C('josephine', 'chica', P('#3a3234', '#c8a08a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True), _cat('front'), _cat('side'), _cat('back'))

# Joyce Deckard: pelo naranja revuelto en mechones con un pelo de antena; gafas redondas negras y ojos adormilados
C('joyce-deckard', 'chica', P('#f1901e', '#f9e1d2', iris='#4a4a5a'),
  F(eyes='closed', brows=False, mouth='frown', mouth_y=95, hairline=hl(6, 64, 48, 62, jit=3, seed=13)),
  dome('front', top=2, w=48, cy=44, n=8, amp=6, seed=71, sb=74, soft=True) + [L(outline([(50, 6), (54, -16, 1), (60, 6)]))] + specs('front', BLACK, w=2.2),
  dome('side', top=2, w=48, cy=44, n=8, amp=6, seed=71, nape=84, fr=56, soft=True) + [L(outline([(46, 4), (52, -16, 1), (56, 6)]))] + specs('side', BLACK),
  dome('back', top=2, w=48, cy=44, n=8, amp=6, seed=71, nape=84, soft=True) + [L(outline([(50, 6), (54, -16, 1), (60, 6)]))])

# Jubilee Meriday: melena amarillo muy pálido ondulada hasta el cuello, con la raya en medio; ojos verdes y sonrisa abierta
C('jubilee-meriday', 'chica', P('#f6f2c8', '#fadeb2', iris='#2aa07a'),
  F(eyes='big', brows=True, mouth='buck', mouth_y=94, hairline=[(6, 62), (16, 50), (30, 42), (46, 40), (50, 46), (54, 40), (70, 42), (84, 50), (94, 62)]),
  longhair('front', length=94, flare=12, top=0, part=True),
  longhair('side', length=94, flare=12, top=0),
  longhair('back', length=94, flare=12, top=0, ends=4, part=True))

# Judeau Garb: adulto de piel clara y cara larga; pelo castaño ceniza corto y peinado; ceño fruncido con arrugas y la boca
# torcida
C('judeau-garb', 'delgado', P('#9f9789', '#fdeadf', iris='#4a5a8a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=98, face_front=face(chin=106, jaw=1), face_side=face_side(chin=6),
    hairline=[(6, 62), (18, 48), (32, 42), (44, 46), (58, 40), (74, 44), (86, 50), (94, 62)]),
  dome('front', top=6, w=44, cy=46, sb=62, seed=1) + [mark([(44, 80), (48, 70)], _c('#c8a090'), w=1.2), mark([(56, 80), (52, 70)], _c('#c8a090'), w=1.2)],
  dome('side', top=6, w=44, cy=46, nape=80, fr=48, seed=1),
  dome('back', top=6, w=44, cy=46, nape=80, seed=1))

# Judis Nitcher: pelo azul marino oscurísimo en pinchos revueltos; ojos oscuros normales y la boca pequeña
C('judis-nitcher', 'normal', P('#22313f', '#f4c3a7', iris='#2a2020'),
  F(eyes='normal', brows=True, mouth='line', mouth_y=95, hairline=hl(6, 62, 48, 58, jit=2, seed=14)),
  dome('front', top=-4, w=48, cy=44, n=11, amp=8, seed=81, sb=64),
  dome('side', top=-4, w=48, cy=44, n=11, amp=8, seed=81, nape=82, fr=50),
  dome('back', top=-4, w=48, cy=44, n=11, amp=8, seed=81, nape=82))

# Juniper Cushionne: media melena castaño dorado con la raya a un lado y las puntas hacia dentro; cara redonda, ojos negros
# grandes, rubor y la boca triste
C('juniper-cushionne', 'chica', P('#a17533', '#f8d4bb', iris='#1a1a1a'),
  F(eyes='round', brows=True, mouth='frown', mouth_y=95, face_front=face(w=3, chin=102), hairline=[(6, 62), (16, 50), (30, 40), (44, 38), (58, 42), (74, 46), (86, 52), (94, 62)]),
  [L(outline([(10, 96), (4, 60), (8, 30), (26, 8), (50, 2), (74, 8), (92, 30), (96, 60), (90, 96), (82, 94), (82, 60), (18, 60), (18, 94)])),
   L(blob([(60, 4), (92, 30), (94, 92), (84, 88), (82, 40)], 6), 'shade', 'b', False),
   mark([(24, 86), (32, 86), (32, 91), (24, 91)], _c('#f4a090')), mark([(68, 86), (76, 86), (76, 91), (68, 91)], _c('#f4a090'))],
  [L(outline([(54, 72), (56, 94), (30, 98), (6, 90), (2, 56), (8, 26), (30, 4), (60, 2), (84, 12), (94, 32), (90, 48), (70, 44), (60, 54)]))],
  [L(outline([(10, 96), (4, 60), (8, 30), (26, 8), (50, 2), (74, 8), (92, 30), (96, 60), (90, 96), (50, 100)])),
   L(blob([(58, 6), (92, 32), (94, 94), (62, 98)], 6), 'shade', 'b', False)])


# Justine Gardenet: media melena gris plateada con dos moños bajos a los lados y un mechón azul en forma de media luna
# sobre la frente; ojos azul oscuro redondos
def _moon(view):
    B = _c('#3a5ad8')
    if view == 'front':
        return [L(outline([(54, 6), (40, 18), (40, 40), (52, 52), (40, 50), (30, 36), (34, 16)]), B, 'f')]
    if view == 'side':
        return [L(outline([(70, 10), (82, 24), (84, 44), (76, 52), (78, 36), (72, 20)]), B, 'f')]
    return []


C('justine-gardenet', 'chica', P('#b4b7c3', '#fbe9df', iris='#2a3a8a'),
  F(eyes='round', brows=False, mouth='line', mouth_y=95, hairline=[(6, 62), (16, 54), (40, 52), (60, 52), (84, 54), (94, 62)]),
  dome('front', top=2, w=48, cy=46, sb=80, seed=1) + [puffs(4, 86, 11, 10, n=5, seed=2), puffs(96, 86, 11, 10, n=5, seed=3)] + _moon('front'),
  dome('side', top=2, w=48, cy=46, nape=86, fr=56, seed=1) + [puffs(30, 88, 12, 10, n=5, seed=2)] + _moon('side'),
  dome('back', top=2, w=48, cy=46, nape=86, seed=1) + [puffs(6, 86, 11, 10, n=5, seed=2, z='f'), puffs(94, 86, 11, 10, n=5, seed=3, z='f')])

# Kairo Reaser: pelo verde azulado liso echado hacia un lado que le tapa parte de la frente; ojos morados afilados y la
# boca seria
C('kairo-reaser', 'delgado', P('#33677b', '#fbe5d6', iris='#5a3a8a'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=97, face_front=face(chin=104), face_side=face_side(chin=4),
    hairline=[(6, 62), (18, 56), (30, 62), (46, 58), (60, 50), (74, 46), (86, 52), (94, 62)]),
  dome('front', top=4, w=46, cy=46, sb=64, seed=1) + [L(outline([(72, 14), (36, 22), (22, 40), (20, 68, 1), (34, 54), (50, 46), (66, 40)]), 'mid', 'f')],
  dome('side', top=4, w=46, cy=46, nape=82, fr=54, seed=1) + [side_bangs(60)],
  dome('back', top=4, w=46, cy=46, nape=82, seed=1))

# Kali Seaborn: pelo castaño rosado con una mancha roja en la coronilla, mechones largos y lisos que le caen por la cara
# y las puntas que se curvan hacia fuera a la altura del cuello; ojos rojos afilados
REDS = _c('#b04a44')
C('kali-seaborn', 'chica', P('#9d706b', '#fbe6d6', iris='#c02a20'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=95, hairline=[(6, 62), (18, 56), (30, 62), (40, 52), (50, 60), (60, 52), (70, 62), (82, 56), (94, 62)]),
  longhair('front', length=100, flare=14, top=2) + [L(blob([(36, 4), (56, 2), (64, 12), (44, 16)], 6), REDS, 'b', False),
                                                    strand(quad((50, 20), (46, 50), (50, 66)), 'mid', 'f', 3)],
  longhair('side', length=100, flare=14, top=2) + [L(blob([(36, 2), (60, 0), (64, 10), (40, 12)], 6), REDS, 'b', False)],
  longhair('back', length=100, flare=14, top=2, ends=4) + [L(blob([(36, 4), (60, 2), (64, 14), (40, 16)], 6), REDS, 'b', False)])

# Kara Okenridge: melena aguamarina hasta los hombros con una mancha morada oscura en lo alto de la cabeza; piel tostada,
# ojos morados adormilados con dos estrellas amarillas debajo
STAR = _c('#f0d040')
C('kara-okenridge', 'chica', P('#6eece6', '#d5aa99', iris='#7a5aa0', top='#4a3a4a'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=95, hairline=[(6, 62), (18, 52), (34, 48), (50, 54), (66, 48), (82, 52), (94, 62)]),
  longhair('front', length=96, flare=8, top=2) + [L(blob([(30, 10), (54, 2), (66, 14), (54, 30), (40, 36), (34, 24)], 6), 'top', 'b', False),
                                                  L(outline([(30, 84), (32, 80, 1), (34, 84), (38, 85, 1), (34, 87), (35, 91, 1), (32, 88), (29, 91, 1), (30, 87), (26, 85, 1)]), STAR, 'f', False),
                                                  L(outline(mir([(30, 84), (32, 80, 1), (34, 84), (38, 85, 1), (34, 87), (35, 91, 1), (32, 88), (29, 91, 1), (30, 87), (26, 85, 1)])), STAR, 'f', False)],
  longhair('side', length=96, flare=8, top=2) + [L(blob([(30, 2), (60, 0), (64, 16), (40, 22)], 6), 'top', 'b', False)],
  longhair('back', length=96, flare=8, top=2, ends=4) + [L(blob([(30, 6), (56, 2), (66, 16), (50, 30), (34, 24)], 6), 'top', 'b', False)])

# Karina Rosenqueen: pelo castaño grisáceo con la raya en medio, recogido en un moño bajo a un lado de la nuca; cejas
# marcadas, ojos morados grandes y sonrisa
C('karina-rosenqueen', 'chica', P('#937d7e', '#fce8de', iris='#7a5ab0'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=94, hairline=[(6, 62), (16, 50), (30, 40), (46, 38), (50, 44), (54, 38), (70, 40), (84, 50), (94, 62)]),
  dome('front', top=4, w=45, cy=46, sb=80, seed=1) + [puffs(6, 90, 10, 10, n=5, seed=4), strand([(50, 6), (50, 38)], 'deep', 'b', 1.2)],
  dome('side', top=4, w=45, cy=46, nape=84, fr=46, seed=1) + [puffs(24, 86, 12, 11, n=5, seed=4)],
  dome('back', top=4, w=45, cy=46, nape=84, seed=1) + [puffs(26, 84, 12, 11, n=5, seed=4, z='f'), strand([(50, 6), (50, 70)], 'deep', 'f', 1.2)])

# Kellan Beatley: pelo rubio dorado largo con un mechón que le tapa un ojo y una trenza fina a un lado; piel tostada y
# ojo verde
C('kellan-beatley', 'normal', P('#e0ac72', '#c68e73', iris='#6a8a3a'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=96, hairline=[(6, 62), (16, 50), (30, 44), (46, 46), (60, 40), (76, 46), (88, 54), (94, 62)]),
  dome('front', top=2, w=46, cy=46, sb=76, seed=1) + [L(outline([(70, 10), (40, 20), (22, 40), (18, 66), (28, 86, 1), (36, 74), (50, 50), (64, 34)]), 'mid', 'f'),
                                                      L(rope((84, 64), (90, 80), (84, 98), 5), 'mid', 'f'), strand([(82, 70), (88, 74), (84, 80), (90, 86), (85, 92)], 'shade', 'f', 1)],
  dome('side', top=2, w=46, cy=46, nape=84, fr=54, seed=1) + [side_bangs(64)],
  dome('back', top=2, w=46, cy=46, nape=84, seed=1) + [L(rope((16, 64), (10, 80), (16, 98), 5), 'mid', 'f')])

# Kendrick Townsend (con modelo 3D): pelo castaño rojizo con un pelo de antena, mechones sueltos que le caen por la
# frente y cubren las orejas; ojos negros grandes y sonrisa
C('kendrick-townsend', 'normal', P('#9a4636', '#fcd1af', iris='#1a1414'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=94, hairline=[(6, 62), (18, 54), (30, 60), (42, 50), (54, 62), (64, 52), (76, 58), (88, 54), (94, 62)]),
  dome('front', top=2, w=48, cy=46, sb=74, seed=1) + [L(outline([(50, 4), (44, -14), (58, -16, 1), (52, -8), (56, 4)])),
                                                      strand(quad((56, 30), (62, 50), (56, 66)), 'mid', 'f', 3), strand(quad((40, 32), (34, 50), (38, 62)), 'mid', 'f', 2.6)],
  dome('side', top=2, w=48, cy=46, nape=84, fr=56, seed=1) + [L(outline([(44, 2), (40, -14), (54, -16, 1), (48, -8), (50, 2)]))],
  dome('back', top=2, w=48, cy=46, nape=84, seed=1) + [L(outline([(50, 4), (44, -14), (58, -16, 1), (52, -8), (56, 4)]))])

# Kenneth Frostner: rizos rosa fucsia arriba y rizos verde azulado oscuro por los lados y detrás; cejas rosas, piel
# morena y una sonrisa enorme de dientes
TEAL = _c('#385559')
C('kenneth-frostner', 'normal', P('#dc3b6b', '#c38976', iris='#5a5a8a'),
  F(eyes='big', brows=False, mouth='grin', mouth_y=95, hairline=[(6, 62), (18, 52), (34, 46), (50, 50), (66, 46), (82, 52), (94, 62)]),
  dome('front', top=10, w=46, cy=48, sb=70, c=TEAL, shade=False) +
  [puffs(8, 70, 14, 26, n=7, c=TEAL, seed=3), puffs(92, 70, 14, 26, n=7, c=TEAL, seed=4), puffs(50, 22, 46, 26, n=10, amp=0.12, seed=5)] + thick_brows(62, 'mid', h=3.6, w=14),
  dome('side', top=10, w=46, cy=48, nape=84, fr=50, c=TEAL, shade=False) + [puffs(28, 66, 26, 30, n=8, c=TEAL, seed=3), puffs(46, 22, 46, 26, n=10, amp=0.12, seed=5)],
  dome('back', top=10, w=46, cy=48, nape=84, c=TEAL, shade=False) + [puffs(50, 70, 46, 28, n=9, c=TEAL, seed=3), puffs(50, 24, 48, 28, n=10, amp=0.12, seed=5)])

# Keyston Typewright: rizos verdes abultados; gafas rojas de montura gruesa en ángulo, cejas verdes y media sonrisa
C('keyston-typewright', 'bajito', P('#49b67f', '#f8e7d9', iris='#2a8ab0'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=95, hairline=[(6, 62), (18, 52), (34, 46), (50, 50), (66, 46), (82, 52), (94, 62)]),
  dome('front', top=10, w=46, cy=48, sb=66, shade=False) + [puffs(50, 28, 52, 32, n=11, amp=0.12, seed=9)] + thick_brows(64, 'shade', h=3.6, tilt=0.6) +
  specs('front', _c('#e04848'), kind='rect', w=2.8),
  dome('side', top=10, w=46, cy=48, nape=84, fr=52, shade=False) + [puffs(44, 30, 50, 32, n=11, amp=0.12, seed=9)] + specs('side', _c('#e04848'), kind='rect', w=2.8),
  dome('back', top=10, w=46, cy=48, nape=84, shade=False) + [puffs(50, 32, 52, 36, n=11, amp=0.12, seed=9)])

# Kipp Sycamore: rizos rojo oscuro muy abultados que le suben por encima de la cabeza y le caen a los lados hasta el
# cuello; ojos redondos muy abiertos y la boca seria
C('kipp-sycamore', 'normal', P('#8b1c22', '#f9d3ba', iris='#3a3a6a'),
  F(eyes='round', brows=True, mouth='frown', mouth_y=96, hairline=[(6, 62), (18, 50), (34, 44), (50, 48), (66, 44), (82, 50), (94, 62)]),
  dome('front', top=10, w=46, cy=48, sb=80, shade=False) + [puffs(4, 82, 13, 24, n=6, seed=3), puffs(96, 82, 13, 24, n=6, seed=4), puffs(50, 20, 50, 34, n=10, amp=0.12, seed=6)],
  dome('side', top=10, w=46, cy=48, nape=90, fr=50, shade=False) + [puffs(26, 76, 22, 30, n=7, seed=3), puffs(44, 20, 50, 34, n=10, amp=0.12, seed=6)],
  dome('back', top=10, w=46, cy=48, nape=90, shade=False) + [puffs(50, 76, 48, 30, n=9, seed=3), puffs(50, 22, 50, 34, n=10, amp=0.12, seed=6)])

# Kipper Marino: pelo azul marino corto con dos mechones celestes que se abren como alas a los lados de la cabeza; piel
# tostada, ojos grises y media sonrisa
WING = _c('#a8d8e0')
C('kipper-marino', 'normal', P('#3f4456', '#d4aa9c', iris='#6a7a8a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=95, hairline=hl(5, 62, 50, 58, seed=15)),
  dome('front', top=2, w=44, cy=46, n=6, amp=6, seed=91, sb=64) +
  [L(outline([(10, 66), (-2, 40), (2, 12, 1), (12, 34), (18, 56)]), WING), L(outline(mir([(10, 66), (-2, 40), (2, 12, 1), (12, 34), (18, 56)])), WING)],
  dome('side', top=2, w=44, cy=46, n=6, amp=6, seed=91, nape=82, fr=50) + [L(outline([(40, 60), (26, 34), (28, 8, 1), (40, 30), (50, 52)]), WING, 'f')],
  dome('back', top=2, w=44, cy=46, n=6, amp=6, seed=91, nape=82) +
  [L(outline([(10, 66), (-2, 40), (2, 12, 1), (12, 34), (18, 56)]), WING, 'f'), L(outline(mir([(10, 66), (-2, 40), (2, 12, 1), (12, 34), (18, 56)])), WING, 'f')])

# Kohara Staley: melena castaña larga y ondulada con la raya en medio y ondas grandes por delante de los hombros; ojos
# morados enormes y sonrisa
C('kohara-staley', 'chica', P('#74614b', '#fcd3c0', iris='#8a3a8a'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=94, hairline=[(6, 62), (16, 50), (30, 40), (46, 38), (50, 44), (54, 38), (70, 40), (84, 50), (94, 62)]),
  longhair('front', length=116, flare=12, top=0, part=True) + [puffs(14, 104, 11, 14, n=5, seed=2, z='f'), puffs(86, 104, 11, 14, n=5, seed=3, z='f')],
  longhair('side', length=116, flare=12, top=0) + [puffs(60, 104, 10, 14, n=5, seed=2, z='f')],
  longhair('back', length=116, flare=12, top=0, ends=5, part=True))


# Kota (con modelo 3D): sombrero negro de ala ancha muy redondeado encima de un flequillo castaño; ojos castaños y sonrisa
def _kota_hat(view):
    H = _c('#2b2121')
    if view == 'front':
        return [L(blob([(-8, 44), (-6, 22), (10, 4), (50, -6), (90, 4), (106, 22), (108, 44), (90, 38), (50, 34), (10, 38)], 6), H, 'f'),
                L(blob([(62, -2), (94, 8), (104, 30), (86, 32), (78, 14)], 6), _c('#3e3232'), 'f', False)]
    if view == 'side':
        return [L(blob([(-10, 44), (-4, 20), (20, 2), (54, -4), (86, 6), (108, 30), (108, 42), (80, 38), (40, 36), (10, 40)], 6), H, 'f')]
    return [L(blob([(-8, 44), (-6, 22), (10, 4), (50, -6), (90, 4), (106, 22), (108, 44), (90, 40), (50, 38), (10, 40)], 6), H, 'f')]


C('kota', 'normal', P('#553c33', '#fbd2bd', iris='#6a4a3a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=94, hairline=[(6, 64), (18, 56), (30, 62), (40, 54), (50, 62), (60, 54), (70, 62), (82, 56), (94, 64)]),
  dome('front', top=10, w=45, cy=48, sb=66, seed=1) + _kota_hat('front'),
  dome('side', top=10, w=45, cy=48, nape=84, fr=56, seed=1) + _kota_hat('side'),
  dome('back', top=10, w=45, cy=48, nape=84, seed=1) + _kota_hat('back'))

# Krome Tallic: grandullón con una melena enorme verde azulado oscuro y ondulada, con la raya en medio, que le cae hasta los
# hombros; gafas de sol verdes oscuras, marcas negras en las sienes y la boca torcida
SUN = _c('#3a5a4a')
C('krome-tallic', 'corpulento', P('#31464a', '#dab0a0', iris='#2a2a2a'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=97, face_front=face(w=5, chin=104, jaw=3), hairline=[(6, 62), (18, 48), (34, 42), (46, 40), (50, 46), (54, 40), (66, 42), (82, 48), (94, 62)]),
  longhair('front', length=110, flare=18, top=0, part=True) +
  [L(blob([(20, 72), (46, 70), (46, 82), (24, 84)], 6), SUN, 'f'), L(blob(mir([(20, 72), (46, 70), (46, 82), (24, 84)]), 6), SUN, 'f'),
   L([(46, 74), (54, 74)], BLACK, 'f', False, False, 2), mark([(22, 64), (32, 60), (28, 66)], BLACK, w=2), mark([(78, 64), (68, 60), (72, 66)], BLACK, w=2)],
  longhair('side', length=110, flare=18, top=0) + [L(blob([(72, 72), (88, 72), (88, 82), (74, 82)], 6), SUN, 'f'), L([(72, 74), (50, 70)], BLACK, 'f', False, False, 2)],
  longhair('back', length=110, flare=18, top=0, ends=5, part=True))

# Kujira Torikawa: pelo verde azulado peinado hacia atrás con un rizo sobre la frente; cejas verdes gruesas, gafas
# cuadradas de montura negra, nariz grande y sonrisa
C('kujira-torikawa', 'normal', P('#355e5d', '#fad2be', iris='#1a1a1a'),
  F(eyes='round', brows=False, mouth='smile', mouth_y=96, nose=(50, 86, 3.6), hairline=[(6, 62), (18, 48), (34, 42), (46, 50), (54, 50), (66, 42), (82, 48), (94, 62)]),
  dome('front', top=2, w=46, cy=46, sb=64, seed=1) + [L(blob([(44, 40), (50, 34), (58, 40), (54, 52), (48, 48)], 6), 'mid', 'f')] +
  thick_brows(63, 'mid', h=4.4, tilt=0.6, w=14) + specs('front', BLACK, kind='rect', w=2.8),
  dome('side', top=2, w=46, cy=46, nape=82, fr=50, seed=1) + specs('side', BLACK, kind='rect', w=2.8),
  dome('back', top=2, w=46, cy=46, nape=82, seed=1))

# Kurtis Loafinn: pelo azul violeta revuelto en mechones que le caen sobre la frente y un ojo; ojos azules adormilados
# y la boca triste
C('kurtis-loafinn', 'normal', P('#44497f', '#f7c3a8', iris='#3a5aa0'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=95, hairline=hl(6, 64, 50, 64, lean=-3, jit=3, seed=16)),
  dome('front', top=-2, w=48, cy=44, n=8, amp=7, seed=101, sb=70, soft=True) + [L(outline([(20, 40), (16, 70, 1), (28, 58), (40, 44)]), 'mid', 'f')],
  dome('side', top=-2, w=48, cy=44, n=8, amp=7, seed=101, nape=84, fr=58, soft=True),
  dome('back', top=-2, w=48, cy=44, n=8, amp=7, seed=101, nape=84, soft=True))

# Kurtz Armishaw: cabeza rapada gris a los lados con una cresta amarilla enorme que se enrosca hacia atrás; ojos
# afilados y sonrisa de dientes
YM = _c('#f2cf49')
C('kurtz-armishaw', 'normal', P('#7f8383', '#facbac', iris='#2a2a2a'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=95, hairline=[(6, 62), (18, 46), (34, 40), (50, 42), (66, 40), (82, 46), (94, 62)]),
  dome('front', top=10, w=44, cy=48, sb=60, seed=1, shade=False) + [L(outline([(36, 30), (30, 6), (40, -14), (58, -22, 1), (64, -8), (70, 6, 1), (62, 10), (64, 30)]), YM),
                                                                    L(blob([(50, -12), (60, -14), (62, 8), (54, 20)], 6), _c('#c8a030'), 'b', False)],
  dome('side', top=10, w=44, cy=48, nape=80, fr=46, seed=1, shade=False) + [L(outline([(30, 30), (24, 6), (36, -14), (60, -20, 1), (72, -4), (84, 12, 1), (70, 16), (66, 30)]), YM)],
  dome('back', top=10, w=44, cy=48, nape=80, seed=1, shade=False) + [L(outline([(38, 40), (34, 6), (50, -16, 1), (64, 6), (62, 40)]), YM)])

# Kye Sendon: pelo castaño esponjoso y despeinado con un mechón que le cae sobre la frente; piel morena, ojos castaños
# grandes y sonrisa
C('kye-sendon', 'normal', P('#705c4a', '#c58c79', iris='#7a5a3a'),
  F(eyes='big', brows='angry', mouth='smile', mouth_y=95, hairline=[(6, 62), (18, 52), (34, 48), (50, 52), (66, 48), (82, 52), (94, 62)]),
  dome('front', top=-2, w=50, cy=44, n=7, amp=6, seed=111, sb=66, soft=True) + [strand(quad((52, 36), (44, 50), (50, 62)), 'mid', 'f', 3.4)],
  dome('side', top=-2, w=50, cy=44, n=7, amp=6, seed=111, nape=82, fr=52, soft=True),
  dome('back', top=-2, w=50, cy=44, n=7, amp=6, seed=111, nape=82, soft=True))
