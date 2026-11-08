"""Ojeadores de GO (scouts-go), tanda 07: dibujados a partir de su retrato de Victory Road; claves 'scouts-go:<id>'.

Casi ninguno tiene modelo 3D: el frente sale del retrato y el perfil y la espalda se deducen. Muchos van disfrazados
(capuchas, cascos, máscaras): esas piezas van como capas delante de la cara. Ayudas de las tandas de IE (sin editarlas)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401
from chars_scouts_ie1_09 import dome, hl, face, face_side, mark, _c  # noqa: F401
from chars_scouts_ie3_02 import ring, hood, skull3, bowl3, scarf, side_lock  # noqa: F401
from chars_scouts_ie3_06 import arc, cap, band, bush  # noqa: F401
from chars_scouts_ie1_03 import round_specs, goggles, shades, thick_brows, side_brow, blush  # noqa: F401
from chars_scouts_ie2_03 import round_glasses, ears_pointy, curls  # noqa: F401

K = 'scouts-go:'
WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)


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


def fr(pts, c='mid'):
    """Mechón o flequillo delante de la cara."""
    return L(outline(pts), c, 'f')


def eye_pair(ey=75, sep=14, rx=6, ry=6.5, c=BLACK, inner=None, ri=2.4):
    """Dos ojos dibujados a mano encima de una máscara (rellenos de c, con pupila inner)."""
    out = []
    for cx in (50 - sep, 50 + sep):
        out.append(L(ell(cx, ey, rx, ry), c, 'f', False))
        if inner:
            out.append(L(ell(cx, ey, ri, ri), inner, 'f', False))
    return out


# ------------------------------------------------------------------ jugadores

# Pyro Piranha Nyah: pelo morado muy oscuro en pinchos que se levantan hacia un lado, con mechones que caen entre los ojos
# rojos; un pañuelo negro le tapa nariz y boca con una fila de dientes blancos de piraña pintados en el borde
NAVY = _c('#24202e')
def _piranha(view):
    if view == 'front':
        out = [L(blob([(14, 82), (50, 78), (86, 82), (84, 104), (64, 116), (50, 118), (36, 116), (16, 104)], 6), NAVY, 'f')]
        teeth = []
        for i in range(7):
            x = 20 + i * 10
            teeth += [(x, 82 + (0 if i else 1)), (x + 5, 91)]
        out.append(L([(16, 83)] + teeth + [(86, 83), (84, 80), (16, 80)], WHITE, 'f', False))
        return out
    return [L(blob([(54, 84), (88, 80), (92, 96), (82, 112), (60, 116), (50, 100)], 6), NAVY, 'f'),
            L([(64, 82), (68, 90), (72, 82), (76, 90), (80, 82), (84, 90), (88, 81), (88, 79), (64, 80)], WHITE, 'f', False)]
C('pyro-piranha-nyah', 'normal', pal('#3e3a5c', '#efc49a', '#d8241e', shade='#2c2944'),
  F(eyes='sharp', brows='angry', mouth='none', hairline=[(10, 66), (20, 50), (34, 54), (42, 46), (50, 66), (56, 46), (66, 52), (80, 48), (90, 66)]),
  dome('front', top=-6, w=46, cy=44, n=5, amp=18, sweep=0.8, seed=71, sb=74) + _piranha('front') +
  [fr([(44, 40), (54, 38), (52, 62), (48, 74, 1), (44, 58)])],
  dome('side', top=-6, w=46, cy=44, n=5, amp=18, sweep=0.8, seed=71, nape=88, fr=56) + _piranha('side'),
  dome('back', top=-6, w=46, cy=44, n=5, amp=18, sweep=0.8, seed=71, nape=90))

# Quattro "4" Black Blackley: un sombrero enorme negro como una bola de bolos, con cuatro círculos blancos y ala; debajo,
# pelo negro que le tapa los ojos y las mejillas; nariz pequeña marrón y boca pequeña
def _ball_hat(view):
    if view == 'front':
        out = [L(ell(50, 6, 48, 40), BLACK), L(blob([(2, 40), (50, 32), (98, 40), (96, 50), (50, 44), (4, 50)], 6), BLACK)]
        for cx, cy in ((36, 0), (54, -16), (64, 6), (44, 18)):
            out.append(L(ell(cx, cy, 8, 8), WHITE, 'b', False, True))
        return out
    if view == 'side':
        return [L(ell(46, 6, 46, 40), BLACK), L(blob([(-4, 46), (46, 34), (100, 38), (98, 48), (46, 44), (-2, 56)], 6), BLACK),
                L(ell(60, -6, 7, 8), WHITE, 'b', False, True), L(ell(72, 10, 6, 7), WHITE, 'b', False, True)]
    return [L(ell(50, 6, 48, 40), BLACK), L(blob([(2, 42), (50, 36), (98, 42), (96, 52), (50, 48), (4, 52)], 6), BLACK)]
C('quattro-4-black-blackley', 'normal', pal('#1e1c22', '#c8986a', shade='#121014'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=96, hairline=False, nose=(50, 88, 2.4)),
  [L(outline([(10, 92), (6, 60), (14, 44), (86, 44), (94, 60), (92, 88), (80, 74), (74, 84), (60, 72), (50, 80), (40, 70), (26, 84), (20, 74)]), 'mid', 'f')] + _ball_hat('front'),
  [L(outline([(54, 80), (66, 62), (86, 70), (90, 50), (60, 44), (20, 46), (4, 60), (6, 86), (22, 98), (42, 92)]), 'mid')] + _ball_hat('side'),
  [L(outline([(10, 92), (6, 50), (94, 50), (92, 92), (50, 98)]), 'mid')] + _ball_hat('back'))

# Queenie Blackcrown: capucha gris de gato con las orejas negras y un antifaz granate que le tapa los ojos; melena gris lisa
# que le cae a los lados hasta el cuello
GRY, BLK2, MAR = _c('#6a6a72'), _c('#28262c'), _c('#5a1e2a')
C('queenie-blackcrown', 'chica', pal('#7a7a80', '#efc49a', shade='#5a5a62'),
  F(eyes='none', brows=False, mouth='none', hairline=False),
  [L(outline([(14, 112), (8, 70), (16, 46), (84, 46), (92, 70), (86, 112), (78, 106), (80, 74), (20, 74), (22, 106)]), 'mid')] +
  [L(outline([(10, 60), (6, 30), (-8, 14, 1), (22, 10), (50, 0), (78, 10), (108, 14, 1), (94, 30), (90, 60), (76, 52), (50, 50), (24, 52)]), GRY, 'f'),
   L(outline([(-8, 14), (22, 10), (12, 26)]), BLK2, 'f', False), L(outline([(108, 14), (78, 10), (88, 26)]), BLK2, 'f', False),
   L(blob([(20, 56), (50, 52), (80, 56), (82, 76), (60, 82), (50, 76), (40, 82), (18, 76)], 6), MAR, 'f')],
  [L(outline([(40, 70), (30, 112), (8, 110), (2, 70), (10, 44), (60, 44)]), 'mid'),
   L(outline([(56, 66), (90, 62), (92, 30), (76, 6), (40, 0), (12, 14), (0, 40), (6, 70), (30, 64)]), GRY),
   L(outline([(50, 6), (54, -10, 1), (66, 4)]), BLK2), L(blob([(70, 58), (92, 56), (92, 76), (74, 80)], 6), MAR, 'f')],
  [L(outline([(10, 112), (6, 60), (94, 60), (90, 112), (50, 116)]), 'mid'),
   L(outline([(8, 70), (4, 30), (-8, 14, 1), (22, 10), (50, 0), (78, 10), (108, 14, 1), (96, 30), (92, 70), (50, 76)]), GRY),
   L(outline([(-8, 14), (22, 10), (12, 26)]), BLK2, 'b', False), L(outline([(108, 14), (78, 10), (88, 26)]), BLK2, 'b', False)])

# Quinn "Q" White Whitebridge: capucha blanca de orejas enormes en punta con una mancha rosa encima; bandas grises a los
# lados de la cara; ojos grises redondos y boca pequeña seria
PNK, GR2 = _c('#d8a0a4'), _c('#8a8a92')
def _q_hood(view):
    if view == 'front':
        return [ring([(4, 112), (2, 60), (6, 30), (-8, -4, 1), (24, 10), (50, 4), (76, 10), (108, -4, 1), (94, 30), (98, 60), (96, 112), (50, 116)],
                     [(22, 104), (20, 68), (26, 52), (50, 48), (74, 52), (80, 68), (78, 104), (50, 110)], WHITE),
                L(blob([(40, 18), (60, 18), (64, 32), (50, 38), (36, 32)], 6), PNK, 'f', False),
                L(blob([(20, 66), (28, 64), (30, 94), (22, 96)], 4), GR2, 'f', False), L(blob([(80, 66), (72, 64), (70, 94), (78, 96)], 4), GR2, 'f', False)]
    if view == 'side':
        return [L(outline([(70, 112), (74, 84), (76, 54), (84, 34), (96, 22), (90, 4), (70, 0), (60, -18, 1), (40, 4), (14, 14), (0, 50), (2, 100), (24, 116)]), WHITE),
                L(blob([(50, 10), (64, 12), (60, 24), (48, 22)], 6), PNK, 'f', False)]
    return [L(outline([(4, 112), (2, 60), (6, 30), (-8, -4, 1), (24, 10), (50, 4), (76, 10), (108, -4, 1), (94, 30), (98, 60), (96, 112), (50, 116)]), WHITE),
            L(blob([(40, 18), (60, 18), (64, 32), (50, 38), (36, 32)], 6), PNK, 'f', False)]
C('quinn-q-white-whitebridge', 'chica', pal('#f0f0f0', '#f6dcc0', '#3a3a44'),
  F(eyes='round', brows=True, mouth='line', mouth_y=94, hairline=False),
  _q_hood('front'), _q_hood('side'), _q_hood('back'))

# Radius Pye: casco gris redondo que le tapa toda la cabeza, como una olla, con un círculo azul verdoso delante y dos ojos de
# anillo negro; tornillos a los lados
STEEL, TEAL = _c('#6e8a8e'), _c('#8ab4b4')
def _pot(view):
    if view == 'front':
        return [L(ell(50, 58, 48, 56), STEEL, 'f'), L(ell(50, 74, 28, 26), TEAL, 'f', False),
                L(ell(4, 62, 5, 10), STEEL, 'f'), L(ell(96, 62, 5, 10), STEEL, 'f'),
                L(ell(36, 76, 6, 6), BLACK, 'f', False), L(ell(36, 76, 3, 3), WHITE, 'f', False), L(ell(36, 76, 1.4, 1.4), BLACK, 'f', False),
                L(ell(64, 76, 6, 6), BLACK, 'f', False), L(ell(64, 76, 3, 3), WHITE, 'f', False), L(ell(64, 76, 1.4, 1.4), BLACK, 'f', False),
                L(blob([(70, 14), (88, 34), (94, 62), (84, 92), (78, 60)], 6), _c('#5a7276'), 'f', False)]
    if view == 'side':
        return [L(ell(48, 58, 46, 56), STEEL, 'f'), L(blob([(78, 52), (94, 58), (96, 90), (80, 98)], 6), TEAL, 'f', False),
                L(ell(88, 74, 3, 4), BLACK, 'f', False), L(ell(44, 62, 6, 10), _c('#5a7276'), 'f')]
    return [L(ell(50, 58, 48, 56), STEEL, 'f'), L(ell(4, 62, 5, 10), STEEL, 'f'), L(ell(96, 62, 5, 10), STEEL, 'f'),
            L(blob([(60, 8), (88, 34), (94, 62), (84, 94), (64, 106), (70, 60)], 6), _c('#5a7276'), 'f', False)]
C('radius-pye', 'normal', pal('#3a2a1a', '#efc49a'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _pot('front'), _pot('side'), _pot('back'))

# Raider Takkel: pelo verde oliva casi negro, largo y revuelto en mechones ondulados que se abren a los lados; un mechón le
# tapa un ojo; ojo ámbar enfadado, piel morena clara y boca seria
C('raider-takkel', 'normal', pal('#2e3226', '#eab07c', '#b8701e', shade='#202418'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, hairline=[(10, 64), (20, 48), (36, 42), (50, 46), (60, 40), (76, 48), (90, 64)]),
  dome('front', top=-4, w=48, cy=46, n=7, amp=12, sweep=0.3, seed=72, long=96, flare=10) +
  [fr([(48, 40), (64, 36), (76, 50), (74, 76), (66, 92, 1), (62, 70), (54, 56)])],
  dome('side', top=-4, w=48, cy=46, n=7, amp=12, seed=72, long=96, flare=10, fr=56),
  dome('back', top=-4, w=48, cy=46, n=7, amp=12, seed=72, long=98, flare=10, ends=5))

# Rain Bowe: nube de pelo blanco esponjoso con un arcoíris a un lado; ojos azules grandes, coloretes naranjas redondos y boca
# abierta; una aleta azul clara le sale por detrás de una oreja
RAIN = [_c('#e03a2a'), _c('#f0a030'), _c('#f8e050'), _c('#7ad8e8')]
def _cloud(view):
    if view == 'front':
        out = [L(curls(56, 30, (44, 32), 9, 0.3), 'mid'), L(curls(18, 64, (16, 18), 5, 0.2), 'mid'), L(curls(84, 62, (14, 16), 5, 0.6), 'mid')]
        for i, c in enumerate(RAIN):
            r = 30 - i * 6
            out.append(L(arc(30, 40, r, r * 0.9, 170, 70) + arc(30, 40, r - 6, (r - 6) * 0.9, 70, 170), c, 'f', i == 0))
        out.append(L(outline([(86, 70), (108, 62), (96, 78)]), _c('#9ae0e8'), 'b'))
        return out
    if view == 'side':
        return [L(curls(44, 30, (46, 32), 9, 0.3), 'mid'), L(curls(26, 70, (22, 20), 6, 0.2), 'mid'), L(outline([(40, 72), (16, 66), (28, 82)]), _c('#9ae0e8'), 'f')]
    return [L(curls(50, 30, (46, 32), 9, 0.3), 'mid'), L(curls(18, 66, (16, 18), 5), 'mid'), L(curls(82, 66, (16, 18), 5, 0.5), 'mid'),
            L(curls(50, 76, (24, 14), 6), 'mid')]
C('rain-bowe', 'chica', pal('#f6f0f0', '#fdf0e2', '#3a8ae0', shade='#e0d4d8'),
  F(eyes='big', brows=False, mouth='grin', mouth_y=94, hairline=[(10, 60), (24, 50), (50, 48), (76, 50), (90, 60)]),
  _cloud('front') + [L(ell(28, 88, 5, 4.5), _c('#f4a060'), 'f', False), L(ell(72, 88, 5, 4.5), _c('#f4a060'), 'f', False)],
  _cloud('side') + [L(ell(78, 88, 4, 4), _c('#f4a060'), 'f', False)],
  _cloud('back'))

# Ramona "Rumble" Tempest: melena azul marino que se abre en puntas a los lados, y un rayo naranja enorme que le cruza la
# cara tapándole un ojo; ojo azul y sonrisa
ORG = _c('#f0a030')
C('ramona-rumble-tempest', 'chica', pal('#28305a', '#f4d0b0', '#3a50b0', shade='#1c2242'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=94, hairline=[(12, 64), (22, 44), (40, 36), (60, 38), (78, 46), (88, 64)]),
  dome('front', top=0, w=48, cy=46, long=100, flare=14, seed=73) +
  [L(outline([(-6, 64), (12, 60), (14, 90), (-8, 104, 1), (4, 84)]), 'mid', 'b'), L(outline([(106, 64), (88, 60), (86, 90), (108, 104, 1), (96, 84)]), 'mid', 'b'),
   L(outline([(30, 30), (58, 24), (48, 52), (62, 54), (24, 108, 1), (36, 66), (22, 64)]), ORG, 'f')],
  dome('side', top=0, w=48, cy=46, long=100, flare=14, seed=73, fr=52) + [L(outline([(70, 30), (88, 28), (84, 50), (92, 52), (78, 80, 1), (80, 56), (72, 56)]), ORG, 'f')],
  dome('back', top=0, w=48, cy=46, long=102, flare=14, seed=73, ends=3) +
  [L(outline([(-6, 64), (12, 60), (14, 90), (-8, 104, 1), (4, 84)]), 'mid', 'b'), L(outline([(106, 64), (88, 60), (86, 90), (108, 104, 1), (96, 84)]), 'mid', 'b')])

# Raphael Allegro (portero): pelo castaño claro recogido en un remolino arriba con un aro amarillo de ángel alrededor y
# mechones largos que le caen a los lados de la cara; ojos amarillos con marcas finas y sonrisa
HALO = _c('#f6e06a')
def _halo(view):
    if view == 'side':
        return [L(ell(48, 8, 34, 9) + ell(48, 8, 26, 5)[::-1], HALO, 'f', True)]
    return [L(ell(50, 8, 44, 12) + ell(50, 8, 34, 7)[::-1], HALO, 'f', True)]
C('raphael-allegro', 'normal', pal('#b8946a', '#f8e0c8', '#d8b030', shade='#94744e'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=94, hairline=[(10, 64), (24, 46), (40, 44), (52, 52), (64, 42), (80, 46), (90, 64)]),
  dome('front', top=0, w=48, cy=46, n=6, amp=8, sweep=0.4, seed=74, long=92, flare=8) + [L(curls(50, 10, (20, 12), 6), 'mid')] + _halo('front') +
  [fr([(22, 46), (30, 44), (26, 76), (18, 90, 1), (18, 66)]), fr([(78, 46), (70, 44), (76, 76), (84, 92, 1), (84, 66)])],
  dome('side', top=0, w=48, cy=46, n=6, amp=8, seed=74, long=92, flare=8, fr=54) + [L(curls(46, 10, (18, 12), 6), 'mid')] + _halo('side'),
  dome('back', top=0, w=48, cy=46, n=6, amp=8, seed=74, long=94, flare=8) + [L(curls(50, 10, (20, 12), 6), 'mid')] + _halo('back'))

# Rayne Shawa: capucha azul en forma de gota terminada en punta, con una franja azul clara; ojos negros enormes de
# extraterrestre y boca pequeña sonriente
BLU, BLU2 = _c('#2e6aa0'), _c('#7ab8e0')
def _drop(view):
    if view == 'front':
        return [ring([(6, 108), (14, 96), (6, 74), (8, 44), (30, 14), (50, -18, 1), (70, 14), (92, 44), (94, 74), (86, 96), (94, 108), (50, 104)],
                     [(22, 92), (20, 70), (28, 56), (50, 52), (72, 56), (80, 70), (78, 92), (50, 100)], BLU),
                L(quad((10, 46), (50, 30), (90, 46)) + quad((92, 54), (50, 38), (8, 54)), BLU2, 'f', False)]
    if view == 'side':
        return [L(outline([(66, 104), (72, 80), (76, 54), (82, 40), (68, 14), (50, -18, 1), (30, 12), (8, 36), (2, 70), (10, 100), (40, 110)]), BLU),
                L([(8, 54), (76, 38), (78, 46), (8, 62)], BLU2, 'f', False)]
    return [L(outline([(6, 108), (14, 96), (6, 74), (8, 44), (30, 14), (50, -18, 1), (70, 14), (92, 44), (94, 74), (86, 96), (94, 108), (50, 112)]), BLU),
            L(quad((10, 46), (50, 30), (90, 46)) + quad((92, 54), (50, 38), (8, 54)), BLU2, 'f', False)]
def _alien_eyes(view):
    if view == 'front':
        return [L(blob([(26, 72), (42, 68), (44, 80), (34, 86)], 6), BLACK, 'f', False), L(blob([(74, 72), (58, 68), (56, 80), (66, 86)], 6), BLACK, 'f', False),
                L(ell(36, 73, 1.6, 1.6), WHITE, 'f', False), L(ell(64, 73, 1.6, 1.6), WHITE, 'f', False)]
    return [L(blob([(76, 70), (86, 70), (86, 82), (78, 84)], 6), BLACK, 'f', False)]
C('rayne-shawa', 'chica', pal('#2e6aa0', '#f6dcc0'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=95, hairline=False),
  _drop('front') + _alien_eyes('front'), _drop('side') + _alien_eyes('side'), _drop('back'))

# Reilly Italot: gorra verde con la visera hacia atrás y pelo negro asomando; mandíbula enorme y ancha que le ocupa media
# cara, ojos pequeños, orejas grandes y boca en mueca
GRN = _c('#8aa04a')
C('reilly-italot', 'corpulento', pal('#1e1a1a', '#f4c890', '#2a2020'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=98, eye_y=70, hairline=[(14, 60), (30, 54), (50, 56), (70, 54), (86, 60)], big_ears=3,
    face_front=blob([(20, 50), (50, 40), (80, 50), (84, 70), (96, 86), (94, 106), (70, 116), (50, 118), (30, 116), (6, 106), (4, 86), (16, 70)], 6),
    face_side=face_side(chin=12, jaw=10)),
  [L(outline([(14, 66), (12, 50), (30, 46), (70, 46), (88, 50), (86, 66), (70, 58), (30, 58)]), 'mid'), cap('front', GRN, top=8, rim=50, w=40)],
  [L(outline([(40, 70), (30, 66), (14, 56), (30, 46), (60, 46), (80, 52)]), 'mid'), cap('side', GRN, top=8, rim=48, w=40), L([(10, 50), (-6, 54), (-4, 58), (12, 56)], GRN, 'f')],
  [L(outline([(16, 72), (12, 54), (88, 54), (84, 72), (50, 78)]), 'mid'), cap('back', GRN, top=8, rim=48, w=40), L(ell(50, 58, 12, 6), GRN, 'f')])

# Renardo Foxe (portero): máscara de zorro blanca con orejas altas en punta y mechones blancos en pico a los lados; marcas
# rojas alrededor de los ojos y una raya roja que baja por la nariz; boca sonriente
RED = _c('#b8282a')
def _fox(view):
    if view == 'front':
        return [L(outline([(16, 90), (-8, 76, 1), (10, 70), (-4, 54, 1), (14, 52), (12, 30), (22, -10, 1), (36, 22), (50, 16), (64, 22), (78, -10, 1), (88, 30), (86, 52),
                           (104, 54, 1), (90, 70), (108, 76, 1), (84, 90), (80, 64), (20, 64)]), WHITE, 'f'),
                L(blob([(22, 60), (50, 54), (78, 60), (76, 88), (50, 92), (24, 88)], 6), _c('#e8e0e0'), 'f', False),
                L(blob([(24, 66), (40, 64), (44, 72), (38, 84), (28, 82)], 6), RED, 'f', False), L(blob([(76, 66), (60, 64), (56, 72), (62, 84), (72, 82)], 6), RED, 'f', False),
                L(outline([(46, 70), (54, 70), (52, 92), (50, 98, 1), (48, 92)]), RED, 'f', False),
                L(ell(36, 74, 3.5, 3.5), _c('#f0d8a0'), 'f', False), L(ell(64, 74, 3.5, 3.5), _c('#f0d8a0'), 'f', False),
                L(ell(36, 74, 1.4, 1.6), BLACK, 'f', False), L(ell(64, 74, 1.4, 1.6), BLACK, 'f', False)]
    if view == 'side':
        return [L(outline([(54, 84), (40, 92), (10, 80, 1), (20, 70), (0, 56, 1), (14, 46), (16, 20), (40, -10, 1), (54, 18), (76, 18), (92, 40), (94, 90), (80, 92), (70, 70)]), WHITE),
                L(blob([(74, 66), (90, 64), (90, 82), (78, 84)], 6), RED, 'f', False), L(ell(84, 74, 1.4, 1.6), BLACK, 'f', False)]
    return [L(outline([(16, 90), (-8, 76, 1), (10, 70), (-4, 54, 1), (14, 52), (12, 30), (22, -10, 1), (36, 22), (50, 16), (64, 22), (78, -10, 1), (88, 30), (86, 52),
                       (104, 54, 1), (90, 70), (108, 76, 1), (84, 90), (50, 96)]), WHITE),
            L(blob([(60, 22), (84, 34), (88, 80), (66, 90)], 6), _c('#d8d0d0'), 'b', False)]
C('renardo-foxe', 'normal', pal('#f0f0f0', '#d8b48a'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=97, hairline=False, ears=False),
  _fox('front'), _fox('side'), _fox('back'))

# Rex Ex-Less: pelo castaño claro en mechones de punta abiertos arriba y los lados rapados en crema; una cicatriz en X
# sobre un ojo; ojos rojizos, piel morena y boca seria
CRM = _c('#f0e2b8')
C('rex-ex-less', 'normal', pal('#b89464', '#c8885a', '#a83a3a', shade='#94744a'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=94, hairline=[(14, 60), (20, 48), (50, 46), (80, 48), (86, 60)]),
  [L(outline([(16, 66), (14, 40), (24, 20), (76, 20), (86, 40), (84, 66), (78, 50), (22, 50)]), CRM),
   L(outline([(28, 50), (24, 30), (2, 24, 1), (22, 14), (14, -2, 1), (36, 6), (50, -12, 1), (62, 6), (86, -2, 1), (78, 14), (98, 24, 1), (76, 30), (72, 50), (50, 44)]), 'mid'),
   L([(30, 66), (46, 82)], _c('#8a3a2a'), 'f', False, False, 2.2), L([(46, 66), (30, 82)], _c('#8a3a2a'), 'f', False, False, 2.2)],
  [L(outline([(52, 60), (60, 46), (80, 44), (88, 30), (60, 20), (30, 22), (14, 34), (8, 56), (20, 72), (40, 70)]), CRM),
   L(outline([(84, 40), (96, 24, 1), (78, 18), (82, 2, 1), (60, 8), (50, -12, 1), (36, 8), (14, 4, 1), (24, 20), (40, 38), (70, 40)]), 'mid')],
  [L(outline([(16, 76), (12, 40), (24, 20), (76, 20), (88, 40), (84, 76), (50, 84)]), CRM),
   L(outline([(28, 46), (24, 30), (2, 24, 1), (22, 14), (14, -2, 1), (36, 6), (50, -12, 1), (62, 6), (86, -2, 1), (78, 14), (98, 24, 1), (76, 30), (72, 46), (50, 50)]), 'mid')])

# Rhiannon Hoode: caperuza roja con un lazo rojo al cuello y media melena castaña oscura con flequillo; ojos azul verdoso
# grandes y sonrisa
RRED = _c('#c02a22')
def _redhood(view):
    if view == 'front':
        return [ring([(4, 108), (0, 64), (8, 26), (30, 4), (50, 0), (70, 4), (92, 26), (100, 64), (96, 108), (50, 112)],
                     [(19, 94), (16, 66), (22, 44), (50, 34), (78, 44), (84, 66), (81, 94), (50, 101)], RRED),
                L(blob([(64, 6), (90, 26), (98, 62), (94, 104), (86, 100), (86, 60), (80, 34)], 6), _c('#9a1e1a'), 'f', False),
                L([(38, 106), (50, 102), (62, 106), (66, 116), (50, 110), (34, 116)], RRED, 'f', True)]
    if view == 'side':
        return [L(outline([(70, 106), (72, 80), (76, 50), (86, 30), (74, 8), (46, 0), (18, 10), (0, 44), (0, 90), (20, 110), (50, 112)]), RRED),
                L(blob([(60, 104), (76, 100), (80, 112), (62, 114)], 6), RRED, 'f')]
    return [L(outline([(4, 108), (0, 64), (8, 26), (30, 4), (50, 0), (70, 4), (92, 26), (100, 64), (96, 108), (50, 116)]), RRED),
            L(blob([(60, 8), (90, 30), (98, 66), (92, 106), (66, 112)], 6), _c('#9a1e1a'), 'f', False)]
C('rhiannon-hoode', 'chica', pal('#3a2a22', '#f8e0c8', '#2a9a9a', shade='#2a1e18'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=94, hairline=False),
  [L(outline([(18, 96), (16, 60), (26, 42), (50, 36), (74, 42), (84, 60), (82, 96), (76, 80), (74, 60), (60, 58), (52, 64, 1), (46, 56), (34, 60), (26, 80)]), 'mid', 'f')] + _redhood('front'),
  [L(outline([(60, 60), (76, 50), (84, 64), (70, 76)]), 'mid', 'f')] + _redhood('side'),
  _redhood('back'))

# Rhonda House: pelo castaño oscuro rizado y abultado con una cinta crema ancha; piel morena, ojos castaños enfadados, una
# tirita en la nariz y la boca pequeña abierta
CRB = _c('#e8dcc0')
C('rhonda-house', 'chica', pal('#3a261e', '#a8704a', '#5a3018', shade='#2a1a14'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, hairline=[(12, 62), (24, 52), (50, 50), (76, 52), (88, 62)]),
  bush('front', top=0, w=50, cy=46, n=10, amp=8, seed=75, sb=72) + [band('front', CRB, y=38, h=12, w=46, z='b', dip=6),
                                                                     L(blob([(44, 84), (56, 84), (56, 89), (44, 89)], 4), _c('#e8c8a0'), 'f', False)],
  bush('side', top=0, w=50, cy=46, n=10, amp=8, seed=75, nape=88, fr=52) + [band('side', CRB, y=34, h=12, z='b')],
  bush('back', top=0, w=50, cy=46, n=10, amp=8, seed=75, nape=90) + [band('back', CRB, y=38, h=12, w=46, z='b')])

# Rhys Eller: pinchos azul marino altísimos hacia arriba con un mechón blanco en medio; cara ancha de mandíbula grande y
# nariz marcada, ojos de enfado y boca recta
C('rhys-eller', 'normal', pal('#243a7a', '#eaa868', '#1e1a1a', shade='#1a2a5a'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=98, hairline=[(8, 66), (16, 46), (30, 54), (40, 40), (50, 56), (60, 40), (70, 54), (84, 46), (92, 66)],
    face_front=face(w=4, chin=106, jaw=4), face_side=face_side(chin=6, jaw=6, nose=3)),
  [L(outline([(10, 74), (2, 50), (4, 24, 1), (18, 30), (20, -10, 1), (34, 14), (40, -30, 1), (50, 6), (60, -30, 1), (66, 14), (80, -10, 1), (82, 30), (96, 24, 1),
              (98, 50), (90, 74), (84, 54), (16, 54)])),
   L(outline([(44, 4), (52, -40, 1), (60, 0), (54, 20)]), WHITE, 'f', True),
   L([(48, 66), (46, 84), (52, 86)], _c('#b06a3a'), 'f', False, False, 1.4)],
  [L(outline([(56, 62), (66, 46), (84, 44), (96, 26), (86, 22), (90, 0, 1), (70, 8), (64, -30, 1), (48, 4), (30, -26, 1), (26, 8), (6, 6, 1), (12, 28), (2, 50), (18, 74),
              (40, 74)])),
   L(outline([(54, 2), (60, -36, 1), (68, 4)]), WHITE, 'f', True)],
  [L(outline([(10, 84), (2, 50), (4, 24, 1), (18, 30), (20, -10, 1), (34, 14), (40, -30, 1), (50, 6), (60, -30, 1), (66, 14), (80, -10, 1), (82, 30), (96, 24, 1),
              (98, 50), (90, 84), (50, 90)])),
   L(outline([(44, 4), (52, -40, 1), (60, 0), (54, 20)]), WHITE, 'b', True)])

# Rhys "Lil' Rhys" Semanrime: rastas gruesas gris oscuro que caen desde arriba y le tapan un ojo, con una cinta roja en la
# frente; piel morena clara, ojo castaño y boca seria
RDB = _c('#c0281e')
def _dreads(view, seed=0):
    if view == 'front':
        out = [L(outline([(10, 60), (6, 30), (24, 6), (50, 0), (76, 6), (94, 30), (96, 60), (84, 54), (16, 54)]))]
        for i, (x, y1) in enumerate(((10, 66), (22, 70), (36, 66), (54, 80), (68, 76), (82, 72), (94, 64))):
            out.append(L(outline([(x - 6, 20), (x + 6, 20), (x + 5, y1 - 4), (x, y1), (x - 5, y1 - 4)]), 'mid', 'f'))
            out.append(L([(x + 2, 26), (x + 2, y1 - 8)], 'shade', 'f', False, False, 1.4))
        return out
    if view == 'side':
        out = [L(outline([(56, 60), (60, 44), (84, 40), (90, 22), (70, 4), (40, 0), (14, 12), (2, 40), (6, 66), (30, 70)]))]
        for x, y1 in ((8, 74), (20, 80), (34, 76), (84, 60), (92, 54)):
            out.append(L(outline([(x - 6, 24), (x + 6, 24), (x + 5, y1 - 4), (x, y1), (x - 5, y1 - 4)]), 'mid', 'f' if x > 60 else 'b'))
        return out
    out = [L(outline([(10, 74), (6, 30), (24, 6), (50, 0), (76, 6), (94, 30), (90, 74), (50, 80)]))]
    for x in (12, 26, 40, 54, 68, 82, 94):
        out.append(L(outline([(x - 6, 30), (x + 6, 30), (x + 5, 84), (x, 90), (x - 5, 84)]), 'mid', 'b'))
    return out
C('rhys-lil-rhys-semanrime', 'normal', pal('#4a4644', '#e8a870', '#7a3a1e', shade='#32302e'),
  F(eyes='normal', brows=False, mouth='line', mouth_y=94, hairline=[(10, 62), (20, 56), (50, 56), (80, 56), (90, 62)]),
  _dreads('front') + [band('front', RDB, y=54, h=8, w=44, z='b')],
  _dreads('side') + [band('side', RDB, y=50, h=8, z='b')],
  _dreads('back'))

# Richard Roake (portero): melena larga gris oscuro, lisa, con mechones de punta que le caen por la cara y se abren a un
# lado; pintura naranja bajo los ojos y ceño fruncido
C('richard-roake', 'delgado', pal('#3e3a3a', '#efd0b0', '#c8501e', shade='#2a2626'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=97, hairline=[(12, 62), (22, 44), (36, 40), (48, 74), (56, 40), (72, 42), (88, 62)],
    face_front=face(chin=106), face_side=face_side(chin=6)),
  dome('front', top=-6, w=46, cy=46, long=104, flare=6, seed=76) +
  [L(outline([(80, 40), (112, 70, 1), (92, 62), (106, 94, 1), (86, 76)]), 'mid', 'b'),
   fr([(44, 36), (56, 34), (54, 64), (48, 86, 1), (44, 60)]),
   L([(26, 80), (40, 84)], _c('#e07a2a'), 'f', False, False, 2.4), L([(60, 84), (74, 80)], _c('#e07a2a'), 'f', False, False, 2.4)],
  dome('side', top=-6, w=46, cy=46, long=104, flare=6, seed=76, fr=56) + [L(outline([(12, 40), (-16, 74, 1), (4, 66), (-8, 96, 1), (14, 80)]), 'mid', 'b')],
  dome('back', top=-6, w=46, cy=46, long=106, flare=6, seed=76, ends=5) + [L(outline([(80, 40), (112, 70, 1), (92, 62), (106, 94, 1), (86, 76)]), 'mid', 'b')])

# Rick "R" White Whitehurst: pelo blanco peinado hacia arriba en un bloque con picos a los lados; cara ancha de viejo
# cascarrabias con ojos cerrados en uve, nariz grande, mejillas con marcas rosadas y boca en mueca
C('rick-r-white-whitehurst', 'normal', pal('#f2f0f0', '#efd2b0', shade='#c8c4c8'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, hairline=[(14, 60), (24, 44), (40, 40), (50, 64), (60, 40), (76, 44), (86, 60)],
    face_front=face(w=4, chin=104, jaw=3)),
  [L(outline([(16, 62), (12, 30), (14, 2, 1), (26, 12), (34, -8), (50, -2), (66, -8), (74, 12), (86, 2, 1), (88, 30), (84, 62), (74, 46), (26, 46)])),
   fr([(42, 34), (58, 34), (56, 56), (50, 66, 1), (44, 56)]),
   L([(26, 72), (40, 78)], OUTC, 'f', False, False, 2.4), L([(40, 78), (28, 82)], OUTC, 'f', False, False, 2.0),
   L([(74, 72), (60, 78)], OUTC, 'f', False, False, 2.4), L([(60, 78), (72, 82)], OUTC, 'f', False, False, 2.0),
   L(outline([(46, 74), (54, 74), (58, 88), (50, 92), (42, 88)]), _c('#e4bf9a'), 'f', False, True),
   L(blob([(16, 82), (24, 80), (24, 92), (16, 94)], 4), _c('#e8b8c8'), 'f', False), L(blob([(84, 82), (76, 80), (76, 92), (84, 94)], 4), _c('#e8b8c8'), 'f', False)],
  [L(outline([(56, 56), (64, 44), (84, 40), (92, 20), (82, 2, 1), (60, -6), (36, -4), (14, 6, 1), (8, 34), (10, 60), (28, 66), (44, 62)])),
   L([(74, 72), (86, 76)], OUTC, 'f', False, False, 2.4)],
  [L(outline([(16, 74), (12, 30), (14, 2, 1), (26, 12), (34, -8), (50, -2), (66, -8), (74, 12), (86, 2, 1), (88, 30), (84, 74), (50, 80)]))])

# Rick Tangle: cabeza tallada como un tótem cuadrado de madera, con la parte de arriba azul grisácea en escalones, ojos
# amarillos de ranura y la barba cuadrada azul; nariz recta y boca de raya
WOOD, TBL = _c('#c08a58'), _c('#6a9ab0')
def _totem(view):
    if view == 'front':
        return [L([(16, 4), (84, 4), (84, 104), (16, 104)], WOOD, 'f', True), L([(18, 2), (82, 2), (82, 40), (66, 40), (66, 48), (34, 48), (34, 40), (18, 40)], TBL, 'f', True),
                L([(6, 44), (16, 44), (16, 84), (6, 84)], WOOD, 'f', True), L([(94, 44), (84, 44), (84, 84), (94, 84)], WOOD, 'f', True),
                L([(26, 62), (42, 62), (42, 68), (26, 68)], BLACK, 'f', False), L([(58, 62), (74, 62), (74, 68), (58, 68)], BLACK, 'f', False),
                L([(30, 63), (40, 63), (40, 67), (30, 67)], _c('#f0a030'), 'f', False), L([(60, 63), (70, 63), (70, 67), (60, 67)], _c('#f0a030'), 'f', False),
                L([(46, 66), (54, 66), (54, 88), (46, 88)], _c('#a87444'), 'f', False), L([(40, 96), (60, 96)], OUTC, 'f', False, False, 1.6),
                L([(36, 100), (64, 100), (64, 104), (36, 104)], TBL, 'f', False)]
    if view == 'side':
        return [L([(12, 4), (84, 4), (88, 104), (16, 104)], WOOD, 'f', True), L([(12, 2), (84, 2), (86, 40), (12, 40)], TBL, 'f', True),
                L([(36, 44), (52, 44), (52, 84), (36, 84)], _c('#a87444'), 'f', True), L([(78, 62), (88, 62), (88, 68), (78, 68)], BLACK, 'f', False),
                L([(86, 66), (94, 70), (94, 88), (86, 88)], WOOD, 'f', True)]
    return [L([(16, 4), (84, 4), (84, 104), (16, 104)], WOOD, 'f', True), L([(18, 2), (82, 2), (82, 40), (18, 40)], TBL, 'f', True),
            L([(6, 44), (16, 44), (16, 84), (6, 84)], WOOD, 'f', True), L([(94, 44), (84, 44), (84, 84), (94, 84)], WOOD, 'f', True)]
C('rick-tangle', 'normal', pal('#6a9ab0', '#c08a58'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  _totem('front'), _totem('side'), _totem('back'))

# Rick Whited: pelo gris verdoso muy claro, de mechones en punta que se levantan arriba y una coleta larga que le cae por
# un lado; ojos azules dulces y sonrisa
C('rick-whited', 'normal', pal('#d4e4e0', '#f8e0c8', '#3a7ab0', shade='#a8bcb8'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=94, hairline=[(12, 62), (22, 46), (36, 50), (50, 44), (64, 50), (78, 46), (88, 62)]),
  dome('front', top=-4, w=46, cy=46, n=5, amp=14, seed=77, sb=72) +
  [L(outline([(80, 60), (90, 58), (92, 90), (86, 116, 1), (82, 90)]), 'mid', 'f')],
  dome('side', top=-4, w=46, cy=46, n=5, amp=14, seed=77, nape=84, fr=52) + [L(outline([(16, 70), (26, 72), (20, 104), (12, 118, 1), (10, 96)]), 'mid', 'b')],
  dome('back', top=-4, w=46, cy=46, n=5, amp=14, seed=77, nape=86) + [L(outline([(14, 70), (26, 72), (22, 104), (14, 118, 1), (10, 96)]), 'mid', 'b')])

# Ricky Shee: casquete de pelo verde muy oscuro con la raya en uve sobre la frente; cara redonda grande, ojos pequeños de
# enfado con cejas gruesas, nariz ancha y labios gruesos
C('ricky-shee', 'corpulento', pal('#22382a', '#efc898', '#1e1a1a'),
  F(eyes='dot', brows=False, mouth='lips', mouth_y=98, mouth_w=10, hairline=[(14, 58), (30, 50), (50, 62), (70, 50), (86, 58)], nose=(50, 88, 3.6),
    face_front=face(w=6, chin=106, jaw=4)),
  [L(outline([(12, 62), (10, 34), (24, 10), (50, 2), (76, 10), (90, 34), (88, 62), (70, 50), (30, 50)]))] + thick_brows(66, BLACK, 4.4, 15, 1.4, 14),
  [L(outline([(58, 50), (80, 44), (88, 26), (70, 6), (40, 2), (16, 14), (6, 40), (10, 66), (30, 72), (46, 60)]))] + side_brow(66, BLACK, 4.4, 1.4),
  [L(outline([(12, 70), (8, 34), (24, 10), (50, 2), (76, 10), (92, 34), (88, 70), (50, 76)]))])

# Riff Ormd: rastas gris azulado gruesas y retorcidas que se levantan como cuernos, con un mechón celeste en medio; gafas
# de sol negras puntiagudas, piel morena y boca seria
C('riff-ormd', 'normal', pal('#4e6070', '#b07a50', shade='#3a4a58'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, hairline=[(12, 62), (24, 50), (50, 46), (76, 50), (88, 62)], face_front=face(chin=104)),
  [L(outline([(8, 90), (2, 60), (6, 30), (24, 10), (50, 4), (76, 10), (94, 30), (98, 60), (92, 90), (82, 64), (18, 64)])),
   L(outline([(20, 18), (10, -10, 1), (26, -2), (30, 14)]), 'mid'), L(outline([(80, 18), (90, -10, 1), (74, -2), (70, 14)]), 'mid'),
   L(outline([(6, 40), (-10, 30, 1), (4, 52)]), 'mid'), L(outline([(94, 40), (110, 30, 1), (96, 52)]), 'mid'),
   fr([(48, 20), (58, 22), (60, 50), (54, 72, 1), (50, 50)], _c('#a8c8d8')),
   L(blob([(20, 70), (46, 74), (50, 80), (54, 74), (80, 70), (76, 84), (56, 84), (50, 80), (44, 84), (24, 84)], 4), BLACK, 'f', True)],
  [L(outline([(54, 66), (60, 48), (84, 44), (92, 24), (70, 4), (40, 0), (14, 12), (0, 40), (2, 80), (20, 96), (40, 90), (48, 74)])),
   L(outline([(30, 12), (24, -14, 1), (42, 4)]), 'mid'), L(blob([(72, 70), (92, 70), (90, 82), (74, 82)], 4), BLACK, 'f', True)],
  [L(outline([(8, 96), (2, 60), (6, 30), (24, 10), (50, 4), (76, 10), (94, 30), (98, 60), (92, 96), (50, 100)])),
   L(outline([(20, 18), (10, -10, 1), (26, -2), (30, 14)]), 'mid'), L(outline([(80, 18), (90, -10, 1), (74, -2), (70, 14)]), 'mid')])

# Rihanna Lin: pelo verde lima con mechas blancas, una coleta alta ladeada atada con goma roja y mechones que le caen por
# la frente; ojos verdes afilados, piel tostada y sonrisa pícara
C('rihanna-lin', 'chica', pal('#8ac83a', '#f0c088', '#6a8a1e', shade='#6aa020'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=94, hairline=[(12, 62), (20, 46), (34, 52), (44, 42), (56, 54), (66, 44), (80, 48), (88, 62)]),
  dome('front', top=2, w=46, cy=46, n=4, amp=8, seed=78, sb=78) +
  [L(outline([(26, 14), (8, -18, 1), (14, 4), (-8, -6, 1), (16, 22)]), 'mid', 'b'), L(ell(24, 14, 4, 4), _c('#c83a2a'), 'f'),
   fr([(54, 30), (72, 34), (80, 56), (74, 66, 1), (64, 48)], WHITE)],
  dome('side', top=2, w=46, cy=46, n=4, amp=8, seed=78, nape=86, fr=54) + [L(outline([(36, 10), (14, -18, 1), (22, 6), (2, 0, 1), (26, 22)]), 'mid'), L(ell(34, 12, 4, 4), _c('#c83a2a'), 'f')],
  dome('back', top=2, w=46, cy=46, n=4, amp=8, seed=78, nape=86) + [L(outline([(28, 14), (8, -18, 1), (14, 4), (-8, -6, 1), (18, 22)]), 'mid'), L(ell(26, 14, 4, 4), _c('#c83a2a'), 'f')])

# Rio "Samba" Sands: melena morada en rizos gruesos de tirabuzón que se abren a los lados, con una diadema amarilla; piel
# morena, ojos grandes con sombra verde y labios verdes sonrientes
YEL = _c('#f2c43a')
C('rio-samba-sands', 'chica', pal('#8a5aa8', '#b8805a', '#3a2220', shade='#6a3e88'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=94, hairline=[(12, 62), (22, 46), (50, 40), (78, 46), (88, 62)]),
  [L(curls(50, 26, (46, 28), 8, 0.2)), L(curls(10, 70, (14, 20), 5, 0.3)), L(curls(90, 70, (14, 20), 5, 0.6)),
   L(curls(4, 92, (10, 10), 4)), L(curls(96, 92, (10, 10), 4)), band('front', YEL, y=36, h=8, w=42, z='f', dip=8),
   L([(28, 68), (42, 66)], _c('#4ac0a0'), 'f', False, False, 2.4), L([(58, 66), (72, 68)], _c('#4ac0a0'), 'f', False, False, 2.4)],
  [L(curls(44, 26, (46, 28), 8, 0.2)), L(curls(20, 70, (20, 24), 6, 0.3)), L(curls(10, 96, (12, 12), 4)), band('side', YEL, y=30, h=8, z='f')],
  [L(curls(50, 26, (46, 28), 8, 0.2)), L(curls(14, 70, (16, 22), 5, 0.3)), L(curls(86, 70, (16, 22), 5, 0.6)), L(curls(50, 80, (30, 18), 7)),
   L(curls(8, 96, (10, 10), 4)), L(curls(92, 96, (10, 10), 4))])

# Rita Bloggs: pelo azul en dos coletas abultadas atadas con gomas rosas y unas gafas rosas en la cabeza; un flequillo
# espeso le tapa los ojos; boca pequeña seria
PINK = _c('#f080a8')
C('rita-bloggs', 'chica', pal('#4a5aa0', '#f6dcc0', shade='#36447e'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, hairline=False),
  [L(curls(12, 22, (16, 16), 5)), L(curls(88, 22, (16, 16), 5)), L(curls(4, 70, (12, 16), 4, 0.3)), L(curls(96, 70, (12, 16), 4, 0.6)),
   L(outline([(14, 84), (10, 50), (18, 24), (50, 14), (82, 24), (90, 50), (86, 84), (76, 80), (74, 86), (60, 80), (50, 84), (40, 80), (26, 86), (24, 80)]), 'mid', 'f'),
   L(ell(36, 20, 9, 7), PINK, 'f'), L(ell(64, 20, 9, 7), PINK, 'f'), L([(44, 20), (56, 20)], _c('#8a6a4a'), 'f', False, False, 2)],
  [L(curls(30, 20, (16, 16), 5)), L(curls(12, 70, (14, 18), 4, 0.3)),
   L(outline([(56, 82), (64, 56), (86, 60), (90, 40), (70, 14), (40, 10), (14, 22), (4, 50), (8, 84), (30, 92)])), L(ell(70, 20, 8, 7), PINK, 'f')],
  [L(curls(12, 22, (16, 16), 5)), L(curls(88, 22, (16, 16), 5)), L(curls(8, 70, (14, 18), 4, 0.3)), L(curls(92, 70, (14, 18), 4, 0.6)),
   L(outline([(12, 86), (8, 40), (24, 16), (50, 10), (76, 16), (92, 40), (88, 86), (50, 92)])), L(ell(36, 20, 9, 7), PINK, 'f'), L(ell(64, 20, 9, 7), PINK, 'f')])

# Rith McCal (portero): pelo azul en casco con la raya alta y las puntas hacia fuera; gafas puntiagudas rosas de cristal
# turquesa, cara larga con nariz marcada y una raya en la barbilla
C('rith-mccal', 'delgado', pal('#3a6aa8', '#f0cca0', shade='#2a5084'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=98, hairline=[(12, 62), (20, 42), (36, 36), (50, 44), (64, 36), (80, 42), (88, 62)],
    face_front=face(chin=110), face_side=face_side(chin=8, nose=3)),
  bowl3('front', top=0, side=86, fringe=50, w=4) +
  [L(blob([(14, 66), (44, 70), (46, 82), (22, 84)], 4), _c('#e04a78'), 'f', True), L(blob([(86, 66), (56, 70), (54, 82), (78, 84)], 4), _c('#e04a78'), 'f', True),
   L(blob([(20, 70), (42, 72), (42, 80), (24, 80)], 4), _c('#5ae0d0'), 'f', False), L(blob([(80, 70), (58, 72), (58, 80), (76, 80)], 4), _c('#5ae0d0'), 'f', False),
   L([(50, 104), (50, 110)], OUTC, 'f', False, False, 1.2), L([(46, 76), (48, 92), (54, 92)], _c('#c08a60'), 'f', False, False, 1.4)],
  bowl3('side', top=0, nape=94, fringe=50, w=4) + [L(blob([(72, 68), (92, 68), (92, 80), (74, 80)], 4), _c('#e04a78'), 'f', True)],
  bowl3('back', top=0, nape=96, w=4))

# Ro St Nutts (portero): un tupé verde oscuro en pico arriba; cara redonda grande muy morena, ojos pequeños de enfado,
# nariz chata y una cruz marrón en la boca, como una nuez
C('ro-st-nutts', 'corpulento', pal('#2a5a2a', '#b8603a', '#1e1a1a', shade='#1e441e'),
  F(eyes='dot', brows='angry', mouth='none', hairline=[(14, 56), (30, 46), (50, 40), (70, 46), (86, 56)], nose=(50, 84, 3), face_front=face(w=8, chin=106, jaw=6)),
  [L(outline([(20, 50), (26, 26), (40, 8), (52, -6, 1), (62, 10), (76, 28), (80, 50), (50, 44)])),
   L(outline([(36, 90), (50, 94), (64, 90), (60, 100), (66, 110), (50, 104), (34, 110), (40, 100)]), _c('#6a3a1e'), 'f', False)],
  [L(outline([(60, 46), (80, 40), (78, 20), (60, 4), (54, -8, 1), (40, 6), (24, 20), (20, 44), (40, 50)])),
   L(blob([(82, 92), (92, 96), (90, 106), (80, 104)], 4), _c('#6a3a1e'), 'f', False)],
  [L(outline([(20, 54), (26, 26), (40, 8), (52, -6, 1), (62, 10), (76, 28), (80, 54), (50, 60)]))])

# Rob-O-Meca (portero): casco blanco con dos cuernos rojos enormes en uve que le bajan por la cara; piel morena, ojos verdes
# afilados y una sonrisa de dientes
def _robo(view):
    if view == 'front':
        return [cap('front', WHITE, top=4, rim=58, w=40, z='f'),
                L(outline([(4, -6, 1), (30, 30), (46, 66), (40, 70), (22, 44)]), _c('#d84a2a'), 'f'),
                L(outline([(96, -6, 1), (70, 30), (54, 66), (60, 70), (78, 44)]), _c('#d84a2a'), 'f')]
    if view == 'side':
        return [cap('side', WHITE, top=4, rim=56, w=40, z='f'), L(outline([(60, -8, 1), (80, 30), (84, 64), (76, 64), (66, 30)]), _c('#d84a2a'), 'f')]
    return [cap('back', WHITE, top=4, rim=56, w=40, z='f'), L(outline([(4, -6, 1), (30, 30), (30, 50), (20, 40)]), _c('#d84a2a'), 'f'),
            L(outline([(96, -6, 1), (70, 30), (70, 50), (80, 40)]), _c('#d84a2a'), 'f')]
C('rob-o-meca', 'normal', pal('#f0f0f0', '#a8704a', '#2a8a4a'),
  F(eyes='sharp', brows=False, mouth='grin', mouth_y=94, hairline=False, face_front=face(w=2, chin=104, jaw=2)),
  _robo('front'), _robo('side'), _robo('back'))

# Robbie Tout (portero): gorro a rayas azules, blancas y negras que le tapa hasta los ojos, con dos rendijas para ver;
# mandíbula grande y boca de raya
def _stripe_cap(view):
    BL, NV = _c('#2a4aa0'), _c('#1e1e22')
    if view == 'front':
        out = [L([(14, 74), (14, 20), (24, 6), (76, 6), (86, 20), (86, 74)], BL, 'f', True)]
        for x0, c in ((26, WHITE), (40, NV), (54, NV), (62, WHITE)):
            out.append(L([(x0, 8), (x0 + 10, 8), (x0 + 10, 74), (x0, 74)], c, 'f', False))
        out += [L([(26, 64), (44, 64), (44, 70), (26, 70)], WHITE, 'f', False), L([(56, 64), (74, 64), (74, 70), (56, 70)], WHITE, 'f', False),
                L([(30, 66), (40, 66)], BLACK, 'f', False, False, 1.6), L([(60, 66), (70, 66)], BLACK, 'f', False, False, 1.6)]
        return out
    if view == 'side':
        return [L([(10, 76), (10, 20), (20, 6), (80, 6), (88, 20), (88, 74)], BL, 'f', True), L([(40, 8), (50, 8), (50, 76), (40, 76)], WHITE, 'f', False),
                L([(76, 64), (88, 64), (88, 70), (76, 70)], WHITE, 'f', False)]
    out = [L([(14, 80), (14, 20), (24, 6), (76, 6), (86, 20), (86, 80)], BL, 'f', True)]
    for x0, c in ((26, WHITE), (40, NV), (54, NV), (62, WHITE)):
        out.append(L([(x0, 8), (x0 + 10, 8), (x0 + 10, 80), (x0, 80)], c, 'f', False))
    return out
C('robbie-tout', 'corpulento', pal('#2a4aa0', '#f4cc98'),
  F(eyes='none', brows=False, mouth='line', mouth_y=96, hairline=False, ears=False, face_front=face(w=4, chin=108, jaw=6)),
  _stripe_cap('front'), _stripe_cap('side'), _stripe_cap('back'))

# Robin O'Cruise: cabeza de calavera crema muy alargada, con las cuencas negras y redondas, nariz pequeña y la boca de
# dientes cosidos; orejas grandes
BONE = _c('#f2e6c4')
def _skull_head(view):
    if view == 'front':
        return [L(blob([(14, 20), (50, -12), (86, 20), (84, 70), (64, 80), (64, 118), (36, 118), (36, 80), (16, 70)], 8), BONE, 'f'),
                L(ell(34, 50, 10, 10), BLACK, 'f', False), L(ell(66, 50, 10, 10), BLACK, 'f', False),
                L(ell(34, 50, 2.4, 2.4), WHITE, 'f', False), L(ell(66, 50, 2.4, 2.4), WHITE, 'f', False),
                L(blob([(46, 72), (54, 72), (52, 80), (48, 80)], 4), _c('#e8a090'), 'f', False),
                L([(38, 92), (62, 92), (62, 106), (38, 106)], BLACK, 'f', False),
                L([(40, 96), (60, 96), (60, 102), (40, 102)], BONE, 'f', False), L([(50, 92), (50, 106)], BLACK, 'f', False, False, 1.4)]
    if view == 'side':
        return [L(blob([(12, 24), (44, -12), (84, 16), (90, 60), (80, 78), (70, 118), (44, 118), (40, 80), (16, 66)], 8), BONE, 'f'),
                L(ell(78, 50, 7, 10), BLACK, 'f', False), L([(68, 92), (84, 92), (84, 106), (68, 106)], BLACK, 'f', False)]
    return [L(blob([(14, 20), (50, -12), (86, 20), (84, 70), (64, 80), (64, 118), (36, 118), (36, 80), (16, 70)], 8), BONE, 'f'),
            L(blob([(60, 0), (84, 22), (82, 66), (62, 80)], 6), _c('#d8cca8'), 'f', False)]
C('robin-o-cruise', 'delgado', pal('#f2e6c4', '#f2e6c4'),
  F(eyes='none', brows=False, mouth='none', hairline=False),
  _skull_head('front'), _skull_head('side'), _skull_head('back'))

# Rocky McCanns: pelo azul marino muy oscuro con picos a los lados como orejas de gato, una diadema gris y un mechón rubio
# que le cruza la cara; cascos amarillos en las orejas, ojos grandes de enfado y boca pequeña
C('rocky-mccanns', 'normal', pal('#2a2e46', '#f6dcc0', '#1e1a1a', shade='#1c1e30'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=95, hairline=[(12, 62), (22, 46), (40, 40), (60, 40), (78, 46), (88, 62)], ears=False),
  dome('front', top=4, w=46, cy=46, sb=78) +
  [L(outline([(12, 40), (-6, 14, 1), (22, 22)]), 'mid'), L(outline([(88, 40), (106, 14, 1), (78, 22)]), 'mid'), L(outline([(40, 8), (50, -8, 1), (60, 8)]), 'mid'),
   band('front', _c('#a8a8b0'), y=24, h=5, w=44, z='f', dip=10),
   fr([(52, 30), (62, 32), (50, 70), (40, 88, 1), (44, 64)], _c('#f0e090')),
   L(ell(10, 76, 6, 9), _c('#e8c040'), 'f'), L(ell(90, 76, 6, 9), _c('#e8c040'), 'f')],
  dome('side', top=4, w=46, cy=46, nape=86, fr=52) + [L(outline([(12, 36), (-4, 12, 1), (24, 20)]), 'mid'), L(ell(46, 72, 8, 10), _c('#e8c040'), 'f')],
  dome('back', top=4, w=46, cy=46, nape=86) + [L(outline([(12, 40), (-6, 14, 1), (22, 22)]), 'mid'), L(outline([(88, 40), (106, 14, 1), (78, 22)]), 'mid'),
                                               L(ell(8, 76, 6, 9), _c('#e8c040'), 'f'), L(ell(92, 76, 6, 9), _c('#e8c040'), 'f')])

# Rocky Zine: pelo azul petróleo muy oscuro, liso, en casco con un flequillo largo de puntas que le tapa los ojos; una
# perilla corta y la boca torcida enseñando los dientes
C('rocky-zine', 'normal', pal('#2a3a42', '#c8986a', shade='#1e2a30'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=94, hairline=[(10, 62), (20, 52), (50, 50), (80, 52), (90, 62)]),
  bowl3('front', top=0, side=84, fringe=50, w=2) +
  [fr([(14, 50), (86, 50), (84, 70), (74, 84, 1), (66, 68), (58, 86, 1), (50, 70), (42, 86, 1), (34, 68), (26, 84, 1), (16, 70)]),
   L(blob([(46, 101), (54, 101), (52, 106), (48, 106)], 4), _c('#2a2020'), 'f', False)],
  bowl3('side', top=0, nape=92, fringe=60, w=2) + [fr([(66, 46), (88, 44), (92, 66), (86, 84, 1), (80, 64)])],
  bowl3('back', top=0, nape=94, w=2))

# Roland Netland: pelo gris claro con una mecha rosada, en melena corta echada a un lado que le tapa un ojo; piel morena,
# ojo gris de párpado caído, perilla rala y media sonrisa
C('roland-netland', 'normal', pal('#cfc8c8', '#b07a52', '#7a7a80', shade='#a8a0a4'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=95, hairline=[(12, 62), (22, 44), (40, 38), (60, 40), (78, 46), (88, 62)]),
  dome('front', top=2, w=48, cy=46, sb=80, seed=79) +
  [fr([(26, 36), (60, 32), (72, 50), (68, 80), (60, 92, 1), (54, 66), (40, 52)]), fr([(40, 30), (52, 26), (60, 50), (54, 62)], _c('#e0b4b4')),
   L([(44, 100), (50, 104), (56, 100)], _c('#5a3a2a'), 'f', False, False, 1.2)],
  dome('side', top=2, w=48, cy=46, nape=86, fr=56, seed=79),
  dome('back', top=2, w=48, cy=46, nape=88, seed=79))

# Roland "Rodent" Dent: cara de hámster redonda y mofletuda, con orejas redondas grandes y un pico de pelo castaño oscuro
# arriba; ojos de párpado caído, nariz de roedor y dos dientes de conejo
C('roland-rodent-dent', 'corpulento', pal('#4a3428', '#f4b878', '#4a2a1a'),
  F(eyes='sharp', brows=False, mouth='buck', mouth_y=96, hairline=[(20, 40), (36, 30), (50, 28), (64, 30), (80, 40)], nose=(50, 86, 3.4), big_ears=6, ear_out=6,
    face_front=blob([(16, 48), (50, 26), (84, 48), (98, 76), (90, 104), (64, 116), (50, 118), (36, 116), (10, 104), (2, 76)], 6),
    face_side=face_side(chin=10, jaw=12)),
  [L(outline([(26, 40), (34, 22), (46, 14), (50, -8, 1), (54, 14), (66, 22), (74, 40), (50, 32)]))],
  [L(outline([(60, 30), (66, 20), (48, 12), (46, -8, 1), (36, 12), (20, 22), (14, 40), (36, 34)]))],
  [L(outline([(24, 44), (32, 22), (46, 14), (50, -8, 1), (54, 14), (68, 22), (76, 44), (50, 36)]))])

# Rolanda "Roll" Tempest: media melena naranja con flequillo y dos coletas amarillas de punta tiesas en los lados de arriba,
# y otras dos puntas amarillas bajo las orejas; ojos morados grandes y sonrisa
YL2 = _c('#f2cc4a')
C('rolanda-roll-tempest', 'chica', pal('#e0902a', '#f8dcc0', '#7a4aa0', shade='#c0741e'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=94, hairline=[(12, 62), (20, 46), (36, 52), (50, 44), (64, 52), (80, 46), (88, 62)]),
  dome('front', top=4, w=46, cy=46, sb=84, seed=80) +
  [L(outline([(16, 24), (2, -12, 1), (14, 4), (4, 8), (24, 34)]), YL2, 'b'), L(outline([(84, 24), (98, -12, 1), (86, 4), (96, 8), (76, 34)]), YL2, 'b'),
   L(outline([(16, 84), (-2, 96, 1), (14, 92), (8, 100, 1), (20, 88)]), YL2, 'f'), L(outline([(84, 84), (102, 96, 1), (86, 92), (92, 100, 1), (80, 88)]), YL2, 'f')],
  dome('side', top=4, w=46, cy=46, nape=88, fr=52, seed=80) + [L(outline([(30, 24), (16, -12, 1), (40, 18)]), YL2, 'b'), L(outline([(40, 82), (24, 98, 1), (46, 88)]), YL2, 'f')],
  dome('back', top=4, w=46, cy=46, nape=88, seed=80) +
  [L(outline([(16, 24), (2, -12, 1), (14, 4), (4, 8), (24, 34)]), YL2, 'b'), L(outline([(84, 24), (98, -12, 1), (86, 4), (96, 8), (76, 34)]), YL2, 'b')])

# Rollo "Bunches" Twain: pelo morado oscuro recogido en dos moños enormes a los lados de la cabeza, como cuernos de carnero,
# y un mechón rizado en la frente; cara larga, ojos rojos con ojeras y ceño fruncido
C('rollo-bunches-twain', 'delgado', pal('#3e2654', '#efd2b0', '#c0402a', shade='#2c1a3e'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=100, hairline=[(14, 56), (24, 44), (40, 42), (50, 50), (60, 42), (76, 44), (86, 56)],
    face_front=face(chin=110), face_side=face_side(chin=8, nose=3)),
  [L(outline([(16, 58), (14, 30), (30, 14), (50, 10), (70, 14), (86, 30), (84, 58), (70, 44), (30, 44)])),
   L(blob([(-6, 6), (20, 0), (34, 14), (26, 34), (0, 30), (-14, 18)], 8)), L(blob([(106, 6), (80, 0), (66, 14), (74, 34), (100, 30), (114, 18)], 8)),
   fr([(44, 38), (54, 36), (52, 54), (44, 58, 1), (48, 50)]),
   L(ell(36, 75, 7.6, 7.6) + ell(36, 75, 5.6, 5.6)[::-1], _c('#d08a7a'), 'f', False), L(ell(64, 75, 7.6, 7.6) + ell(64, 75, 5.6, 5.6)[::-1], _c('#d08a7a'), 'f', False)],
  [L(outline([(56, 54), (66, 42), (84, 40), (90, 24), (70, 10), (40, 8), (16, 20), (6, 44), (14, 66), (34, 66)])),
   L(blob([(20, 0), (48, -6), (60, 10), (50, 30), (24, 26)], 8))],
  [L(outline([(14, 74), (12, 30), (30, 14), (50, 10), (70, 14), (88, 30), (86, 74), (50, 80)])),
   L(blob([(-6, 6), (20, 0), (34, 14), (26, 34), (0, 30), (-14, 18)], 8)), L(blob([(106, 6), (80, 0), (66, 14), (74, 34), (100, 30), (114, 18)], 8))])

# Romeo Wheedler: pelo granate oscuro ondulado hacia atrás con mechones sueltos que le caen por la cara y la nuca, y una
# cinta azul marino; piel morena, ojos castaños con raya negra y media sonrisa
C('romeo-wheedler', 'normal', pal('#4a2230', '#a8724e', '#7a4a2a', shade='#341822'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=95, hairline=[(12, 62), (22, 50), (50, 48), (78, 50), (88, 62)]),
  dome('front', top=0, w=48, cy=46, n=7, amp=8, seed=81, sb=80) +
  [band('front', _c('#2a2e5a'), y=46, h=8, w=44, z='b'), fr([(30, 52), (36, 54), (30, 76), (22, 84, 1), (26, 66)]), fr([(66, 52), (72, 54), (76, 76), (80, 88, 1), (70, 66)]),
   L(outline([(6, 76), (-4, 94, 1), (10, 86)]), 'mid'), L(outline([(94, 76), (104, 94, 1), (90, 86)]), 'mid')],
  dome('side', top=0, w=48, cy=46, n=7, amp=8, seed=81, nape=96, fr=54) + [band('side', _c('#2a2e5a'), y=42, h=8, z='b')],
  dome('back', top=0, w=48, cy=46, n=7, amp=8, seed=81, nape=96) + [band('back', _c('#2a2e5a'), y=46, h=8, w=44, z='b')])

# Romulus Fulmen: pelo rubio oscuro peinado hacia atrás que cae en mechones en zigzag a los lados, como rayos; orejas de punta,
# cara muy alargada, ojos rojos pequeños de enfado y boca en mueca
C('romulus-fulmen', 'delgado', pal('#c8962e', '#f2dcb8', '#c02a2a', shade='#a0741e'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=104, eye_y=72, hairline=[(14, 56), (24, 40), (40, 32), (50, 30), (60, 32), (76, 40), (86, 56)],
    face_front=face(chin=116), face_side=face_side(chin=14, nose=4)),
  [L(outline([(16, 58), (12, 30), (28, 10), (50, 4), (72, 10), (88, 30), (84, 58), (76, 40), (24, 40)])),
   L(outline([(16, 58), (4, 76), (14, 78), (-2, 102, 1), (20, 84), (14, 70), (22, 62)]), 'mid'),
   L(outline([(84, 58), (96, 76), (86, 78), (102, 102, 1), (80, 84), (86, 70), (78, 62)]), 'mid')] + ears_pointy('front', h=14),
  [L(outline([(56, 50), (64, 34), (82, 28), (70, 10), (40, 4), (16, 14), (4, 40), (8, 66), (-4, 92, 1), (20, 76), (30, 60), (44, 56)]))] + ears_pointy('side', h=14),
  [L(outline([(14, 70), (10, 30), (28, 10), (50, 4), (72, 10), (90, 30), (86, 70), (98, 100, 1), (70, 80), (50, 84), (30, 80), (2, 100, 1)]))] + ears_pointy('back', h=14))

# Ron Flappibal: pelo verde grisáceo claro que se abre en dos grandes alas curvas a los lados de la cabeza, con una raya al
# medio; cejas verdes, ojos cerrados tranquilos y sonrisa
C('ron-flappibal', 'normal', pal('#9ac0a0', '#f4d8b8', shade='#7a9e80'),
  F(eyes='closed', brows=False, mouth='smile', mouth_y=94, hairline=[(14, 56), (24, 44), (42, 40), (50, 46), (58, 40), (76, 44), (86, 56)]),
  [L(outline([(18, 56), (16, 34), (30, 18), (50, 12), (70, 18), (84, 34), (82, 56), (70, 44), (30, 44)])),
   L(outline([(30, 24), (6, 24), (-8, 40), (-4, 62, 1), (6, 46), (24, 40)])), L(outline([(70, 24), (94, 24), (108, 40), (104, 62, 1), (94, 46), (76, 40)])),
   L([(24, 66), (40, 62)], _c('#7ab08a'), 'f', False, False, 2.4), L([(60, 62), (76, 66)], _c('#7ab08a'), 'f', False, False, 2.4)],
  [L(outline([(56, 50), (64, 40), (84, 36), (78, 18), (54, 10), (30, 12), (12, 26), (8, 50), (14, 68), (30, 66)])),
   L(outline([(30, 18), (8, 22), (-6, 40), (-2, 62, 1), (8, 46), (24, 36)]))],
  [L(outline([(16, 72), (14, 34), (30, 16), (50, 12), (70, 16), (86, 34), (84, 72), (50, 78)])),
   L(outline([(30, 24), (6, 24), (-8, 40), (-4, 62, 1), (6, 46), (24, 40)])), L(outline([(70, 24), (94, 24), (108, 40), (104, 62, 1), (94, 46), (76, 40)]))])

# Rook "R" Black Blackside: un sombrero negro con forma de torre de ajedrez (almenas arriba) y pelo negro que asoma en puntas
# por los lados; un antifaz morado alrededor de los ojos y una sonrisa de dientes apretados
PUR = _c('#5a4a7a')
def _rook(view):
    if view == 'front':
        return [L([(10, 50), (10, 8), (22, 8), (22, -2), (36, -2), (36, 8), (64, 8), (64, -2), (78, -2), (78, 8), (90, 8), (90, 50), (50, 46)], BLACK, 'f', True),
                L(blob([(4, 50), (50, 44), (96, 50), (96, 58), (50, 54), (4, 58)], 4), BLACK, 'f', True)]
    if view == 'side':
        return [L([(6, 52), (6, 8), (18, 8), (18, -2), (34, -2), (34, 8), (70, 8), (70, -2), (86, -2), (86, 8), (90, 50)], BLACK, 'f', True),
                L(blob([(0, 54), (50, 46), (98, 50), (98, 58), (50, 56), (0, 62)], 4), BLACK, 'f', True)]
    return [L([(10, 52), (10, 8), (22, 8), (22, -2), (36, -2), (36, 8), (64, 8), (64, -2), (78, -2), (78, 8), (90, 8), (90, 52), (50, 50)], BLACK, 'f', True),
            L(blob([(4, 52), (50, 48), (96, 52), (96, 60), (50, 58), (4, 60)], 4), BLACK, 'f', True)]
C('rook-r-black-blackside', 'normal', pal('#1e1c22', '#efd0a8', '#2a2020'),
  F(eyes='round', brows=False, mouth='grin', mouth_y=95, hairline=False, face_front=face(w=2, chin=104, jaw=3)),
  [L(outline([(16, 58), (12, 80), (-4, 92, 1), (16, 88), (20, 70)])), L(outline([(84, 58), (88, 80), (104, 92, 1), (84, 88), (80, 70)])),
   L(blob([(20, 68), (46, 70), (46, 82), (22, 82)], 4), PUR, 'f', False), L(blob([(80, 68), (54, 70), (54, 82), (78, 82)], 4), PUR, 'f', False)] + _rook('front'),
  [L(outline([(36, 58), (20, 90, 1), (44, 76)])), L(blob([(70, 68), (90, 68), (90, 82), (72, 82)], 4), PUR, 'f', False)] + _rook('side'),
  [L(outline([(14, 56), (8, 84), (50, 90), (92, 84), (86, 56)]))] + _rook('back'))

# Rory "Stripes" Tigre: melena rubia de león con mechones de punta y orejas negras de tigre, rayas negras en el pelo y en
# la cara; ojos naranjas de enfado y boca seria
def _stripes(view):
    out = []
    if view == 'front':
        for x0, y0, x1, y1 in ((6, 40, 18, 46), (8, 60, 18, 62), (94, 40, 82, 46), (92, 60, 82, 62), (40, 6, 44, 18), (60, 6, 56, 18)):
            out.append(L([(x0, y0), (x1, y1)], BLACK, 'f', False, False, 2.6))
        for y in (78, 84, 90):
            out += [L([(16, y), (28, y + 2)], BLACK, 'f', False, False, 1.6), L([(84, y), (72, y + 2)], BLACK, 'f', False, False, 1.6)]
    return out
C('rory-stripes-tigre', 'normal', pal('#e8b84a', '#e8a868', '#e05a1e', shade='#c8962e'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, hairline=[(10, 64), (20, 46), (32, 54), (40, 40), (50, 56), (60, 40), (68, 54), (80, 46), (90, 64)]),
  dome('front', top=0, w=50, cy=46, n=9, amp=10, seed=82, long=96, flare=8) +
  [L(outline([(12, 22), (6, -4, 1), (28, 8)]), BLACK), L(outline([(88, 22), (94, -4, 1), (72, 8)]), BLACK)] + _stripes('front'),
  dome('side', top=0, w=50, cy=46, n=9, amp=10, seed=82, long=96, flare=8, fr=54) + [L(outline([(36, 12), (36, -10, 1), (54, 6)]), BLACK)],
  dome('back', top=0, w=50, cy=46, n=9, amp=10, seed=82, long=98, flare=8, ends=5) +
  [L(outline([(12, 22), (6, -4, 1), (28, 8)]), BLACK), L(outline([(88, 22), (94, -4, 1), (72, 8)]), BLACK),
   L([(30, 30), (40, 40)], BLACK, 'f', False, False, 2.6), L([(70, 30), (60, 40)], BLACK, 'f', False, False, 2.6)])

# Rosa Welle: casco de platillo volante rojo con el borde gris y una cúpula turquesa delante que le tapa los ojos; asoma
# pelo gris oscuro a los lados; sonrisa
UFO, UFG, UFC = _c('#c8282a'), _c('#7a7a88'), _c('#5ad0c8')
def _ufo(view):
    if view == 'front':
        return [L(blob([(26, 30), (34, 4), (50, -4), (66, 4), (74, 30)], 8), UFO, 'f'),
                L(blob([(-4, 40), (20, 26), (50, 22), (80, 26), (104, 40), (90, 48), (50, 50), (10, 48)], 6), UFG, 'f'),
                L(ell(50, 64, 20, 12), UFC, 'f'), L(ell(42, -2, 4, 3), UFC, 'f', False), L(ell(58, -2, 4, 3), UFC, 'f', False)]
    if view == 'side':
        return [L(blob([(26, 30), (34, 4), (50, -4), (66, 4), (74, 30)], 8), UFO, 'f'), L(blob([(-4, 40), (20, 26), (50, 22), (80, 26), (104, 40), (90, 48), (50, 50), (10, 48)], 6), UFG, 'f'),
                L(ell(84, 62, 10, 12), UFC, 'f')]
    return [L(blob([(26, 30), (34, 4), (50, -4), (66, 4), (74, 30)], 8), UFO, 'f'), L(blob([(-4, 40), (20, 26), (50, 22), (80, 26), (104, 40), (90, 48), (50, 50), (10, 48)], 6), UFG, 'f')]
C('rosa-welle', 'chica', pal('#5a5a66', '#f2d0a8'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=92, hairline=False),
  [L(outline([(12, 86), (8, 54), (20, 44), (80, 44), (92, 54), (88, 86), (78, 76), (22, 76)]), 'mid', 'f')] + _ufo('front'),
  [L(outline([(54, 66), (60, 50), (40, 44), (10, 48), (4, 70), (14, 88), (40, 84)]))] + _ufo('side'),
  [L(outline([(10, 88), (8, 50), (92, 50), (90, 88), (50, 92)]))] + _ufo('back'))

# Rosie Redd (con su modelo 3D): melena castaña rosada abombada a los lados, con la raya a un lado y dos trenzas que le caen
# por delante de los hombros; ojos lilas, coloretes y sonrisa
C('rosie-redd', 'chica', pal('#a4807a', '#f8e2cc', '#7a6aa8', shade='#866460'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=94, hairline=[(12, 64), (22, 46), (40, 38), (56, 40), (64, 50), (74, 44), (88, 64)]),
  [L(curls(50, 46, (50, 44), 6, 0.2)), L(ell(20, 98, 6, 8), 'mid', 'f'), L(ell(20, 111, 5, 7), 'mid', 'f'), L(ell(80, 98, 6, 8), 'mid', 'f'), L(ell(80, 111, 5, 7), 'mid', 'f')] + blush(86, 22, 4),
  [L(curls(44, 46, (46, 44), 6, 0.2)), L(ell(56, 102, 5, 7), 'mid', 'f'), L(ell(58, 114, 4, 6), 'mid', 'f')],
  [L(curls(50, 46, (50, 44), 6, 0.2)), L(ell(30, 98, 6, 7)), L(ell(70, 98, 6, 7))])

# Ross Seption: un sombrero de antena parabólica blanca con su soporte; pelo castaño en puntas a los lados; cara alargada,
# ojos redondos asustados y boca temblorosa
DISH = _c('#e8e0dc')
def _dish(view):
    if view == 'side':
        return [L(blob([(-10, 34), (30, 24), (70, 22), (106, 30), (100, 40), (50, 40), (-6, 44)], 6), DISH, 'f'),
                L([(46, 26), (50, -10), (54, 26)], _c('#c8b8b4'), 'f', False, False, 2), L(ell(50, -10, 3, 3), DISH, 'f')]
    return [L(blob([(-14, 36), (20, 24), (50, 20), (80, 24), (114, 36), (100, 44), (50, 42), (0, 44)], 6), DISH, 'f'),
            L([(30, 26), (50, -12)], _c('#c8b8b4'), 'f', False, False, 2), L([(70, 26), (50, -12)], _c('#c8b8b4'), 'f', False, False, 2), L(ell(50, -12, 3, 3), DISH, 'f')]
C('ross-seption', 'delgado', pal('#6a4a40', '#efd0a8', '#1e1a1a'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=100, hairline=False, face_front=face(chin=112), face_side=face_side(chin=10, nose=4)),
  [L(outline([(16, 52), (4, 66, 1), (16, 64), (6, 78, 1), (20, 70)])), L(outline([(84, 52), (100, 64, 1), (86, 64), (96, 78, 1), (80, 70)]))] + _dish('front'),
  [L(outline([(54, 52), (40, 42), (10, 44), (-4, 60, 1), (8, 62), (-2, 76, 1), (20, 74), (40, 70)]))] + _dish('side'),
  [L(outline([(10, 74), (8, 40), (92, 40), (90, 74), (50, 80)]))] + _dish('back'))

# Ruben Lamp: cabeza rapada castaña con una cresta de bolas turquesa que baja por un lado y acaba en una coleta castaña;
# piel morena, cejas gruesas, ojos rojizos de enfado y boca en mueca
TQ = _c('#4ac0b0')
C('ruben-lamp', 'normal', pal('#3a2a22', '#b06a42', '#8a1e1e'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=98, hairline=[(14, 56), (26, 44), (50, 40), (74, 44), (86, 56)], face_front=face(w=3, chin=106, jaw=3)),
  [L(outline([(16, 60), (14, 34), (28, 14), (50, 8), (72, 14), (86, 34), (84, 60), (70, 44), (30, 44)]))] +
  [L(ell(x, y, 9, 8), TQ) for x, y in ((36, 4), (22, 14), (12, 30), (8, 48), (8, 66))] +
  [L(outline([(6, 74), (14, 76), (16, 94), (24, 110, 1), (6, 96)])), L(ell(10, 74, 3.4, 3), _c('#a01e3a'))] + thick_brows(64, BLACK, 4.2, 15, 1.2, 14),
  [L(outline([(56, 50), (66, 40), (84, 36), (76, 16), (50, 6), (24, 12), (8, 36), (10, 62), (24, 72), (44, 64)]))] +
  [L(ell(x, y, 9, 8), TQ) for x, y in ((44, 2), (28, 8), (14, 22))] + side_brow(64, BLACK, 4.2, 1.2),
  [L(outline([(16, 72), (12, 34), (28, 14), (50, 8), (72, 14), (88, 34), (84, 72), (50, 78)]))] +
  [L(ell(x, y, 9, 8), TQ) for x, y in ((64, 4), (78, 14), (88, 30), (92, 48), (92, 66))] + [L(outline([(94, 74), (86, 76), (84, 94), (76, 110, 1), (94, 96)]))])

# Ruby Catbear: capucha naranja de panda rojo con orejas redondas y dos espirales a los lados, y la cara de panda pintada:
# manchas negras alrededor de los ojos naranjas y una naricita
ORA = _c('#e05a1e')
def _redpanda(view):
    if view == 'front':
        return [ring([(2, 104), (-2, 60), (8, 22), (30, 4), (50, 0), (70, 4), (92, 22), (102, 60), (98, 104), (50, 108)],
                     [(22, 93), (20, 70), (28, 58), (50, 54), (72, 58), (80, 70), (78, 93), (50, 101)], ORA),
                L(ell(16, 6, 10, 9), BLACK, 'f'), L(ell(84, 6, 10, 9), BLACK, 'f'),
                L(curls(10, 74, (10, 12), 4), _c('#c84a16'), 'f', False, True), L(curls(90, 74, (10, 12), 4, 0.5), _c('#c84a16'), 'f', False, True),
                L(blob([(24, 66), (44, 68), (44, 82), (26, 82)], 4), BLACK, 'f', False), L(blob([(76, 66), (56, 68), (56, 82), (74, 82)], 4), BLACK, 'f', False),
                L(ell(36, 75, 4.5, 4.5), WHITE, 'f', False), L(ell(64, 75, 4.5, 4.5), WHITE, 'f', False),
                L(ell(36, 75, 3, 3), _c('#e07a1e'), 'f', False), L(ell(64, 75, 3, 3), _c('#e07a1e'), 'f', False),
                L(ell(36, 75, 1.3, 1.3), BLACK, 'f', False), L(ell(64, 75, 1.3, 1.3), BLACK, 'f', False),
                L(blob([(47, 86), (53, 86), (50, 90)], 3), BLACK, 'f', False),
                L(quad((18, 40), (50, 28), (82, 40)) + quad((82, 50), (50, 38), (18, 50)), BLACK, 'f', False)]
    if view == 'side':
        return [L(outline([(70, 104), (72, 80), (76, 54), (84, 36), (74, 10), (46, 0), (18, 10), (0, 44), (0, 90), (20, 106), (50, 110)]), ORA),
                L(ell(40, 2, 9, 8), BLACK, 'f'), L(curls(30, 70, (14, 16), 5), _c('#c84a16'), 'f', False, True),
                L(blob([(74, 66), (90, 68), (90, 82), (76, 82)], 4), BLACK, 'f', False), L(ell(84, 75, 2.6, 2.6), _c('#e07a1e'), 'f', False)]
    return [L(outline([(2, 104), (-2, 60), (8, 22), (30, 4), (50, 0), (70, 4), (92, 22), (102, 60), (98, 104), (50, 110)]), ORA),
            L(ell(16, 6, 10, 9), BLACK, 'f'), L(ell(84, 6, 10, 9), BLACK, 'f'), L(curls(50, 50, (22, 22), 6), _c('#c84a16'), 'f', False, True)]
C('ruby-catbear', 'chica', pal('#e05a1e', '#f8dcc0'),
  F(eyes='none', brows=False, mouth='none', hairline=False),
  _redpanda('front'), _redpanda('side'), _redpanda('back'))

# Rudy Blush (portero): capucha verde oscuro en punta, con una cinta caqui sobre la frente, y una máscara gris de pico que le
# tapa nariz y boca; ojos grises entornados
GRD, KHK, MSK = _c('#2e4a34'), _c('#8a8a4a'), _c('#a8acb0')
def _ninja(view):
    if view == 'front':
        return [ring([(2, 110), (-2, 64), (10, 28), (30, 6), (50, -10, 1), (70, 6), (90, 28), (102, 64), (98, 110), (50, 114)],
                     [(22, 93), (20, 70), (26, 58), (50, 54), (74, 58), (80, 70), (78, 93), (50, 101)], GRD),
                L(quad((14, 56), (50, 50), (86, 56)) + quad((86, 66), (50, 60), (14, 66)), KHK, 'f', True),
                L(outline([(20, 78), (50, 76), (80, 78), (74, 96), (50, 116, 1), (26, 96)]), MSK, 'f')]
    if view == 'side':
        return [L(outline([(72, 108), (74, 80), (76, 54), (86, 36), (74, 6), (50, -10, 1), (18, 8), (0, 44), (0, 92), (20, 110), (50, 114)]), GRD),
                L([(8, 60), (92, 50), (92, 60), (8, 70)], KHK, 'f', True), L(outline([(60, 78), (92, 76), (98, 96), (70, 112, 1), (60, 96)]), MSK, 'f')]
    return [L(outline([(2, 110), (-2, 64), (10, 28), (30, 6), (50, -10, 1), (70, 6), (90, 28), (102, 64), (98, 110), (50, 116)]), GRD),
            L(quad((4, 58), (50, 52), (96, 58)) + quad((96, 68), (50, 62), (4, 68)), KHK, 'f', True)]
C('rudy-blush', 'normal', pal('#2e4a34', '#efd0a8', '#6a6a72'),
  F(eyes='sharp', brows=False, mouth='none', hairline=False, eye_y=72),
  _ninja('front'), _ninja('side'), _ninja('back'))

# Ruff Weedon: pelo rosa con flequillo recto de mechones y dos picos curvos a los lados; piel morena con unas marcas rosas en
# espiral en las mejillas y una marca blanca en la frente; ojos entornados y labios gruesos
PNK2 = _c('#f2a0b0')
C('ruff-weedon', 'normal', pal('#f096a8', '#a8724e', '#2a2020', shade='#d07888'),
  F(eyes='sharp', brows=False, mouth='lips', mouth_y=98, mouth_w=9, hairline=[(14, 56), (20, 48), (50, 46), (80, 48), (86, 56)], face_front=face(chin=106)),
  [L(outline([(16, 58), (14, 30), (28, 12), (50, 6), (72, 12), (86, 30), (84, 58), (78, 46), (22, 46)])),
   L(outline([(16, 30), (-2, 18, 1), (6, 40), (16, 50)])), L(outline([(84, 30), (102, 18, 1), (94, 40), (84, 50)])),
   fr([(18, 40), (82, 40), (82, 52), (72, 56), (64, 50), (56, 56), (50, 50), (44, 56), (36, 50), (28, 56), (18, 52)]),
   L(outline([(46, 60), (54, 60), (52, 68), (54, 76), (46, 76), (48, 68)]), WHITE, 'f', False),
   L(quad((32, 82), (24, 90), (32, 96)), PNK2, 'f', False, False, 2.2), L(quad((68, 82), (76, 90), (68, 96)), PNK2, 'f', False, False, 2.2)],
  [L(outline([(56, 52), (66, 44), (84, 40), (82, 20), (60, 6), (34, 6), (14, 18), (6, 44), (10, 66), (28, 70), (44, 62)])),
   L(outline([(30, 20), (16, 6, 1), (18, 32)]))],
  [L(outline([(14, 72), (12, 30), (28, 12), (50, 6), (72, 12), (88, 30), (86, 72), (50, 78)])),
   L(outline([(16, 30), (-2, 18, 1), (6, 40), (16, 50)])), L(outline([(84, 30), (102, 18, 1), (94, 40), (84, 50)]))])

# Rufus Brunt (portero): pelo rubio claro en una cresta de pinchos con los lados rapados; cara cuadrada grande, ojos
# pequeños de enfado, nariz ancha y boca de mueca
C('rufus-brunt', 'corpulento', pal('#f2dc8a', '#f6c890', '#2a2020', shade='#d8bc68'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=100, hairline=[(16, 52), (30, 42), (50, 40), (70, 42), (84, 52)], nose=(50, 88, 3.4),
    face_front=blob([(18, 46), (50, 30), (82, 46), (88, 70), (86, 100), (70, 112), (50, 114), (30, 112), (14, 100), (12, 70)], 6), big_ears=2),
  [L(outline([(30, 44), (26, 20), (34, 4, 1), (40, 12), (44, -6, 1), (50, 8), (56, -8, 1), (62, 10), (68, 0, 1), (74, 22), (70, 44), (50, 40)]))],
  [L(outline([(60, 40), (70, 30), (74, 10, 1), (60, 12), (54, -8, 1), (44, 8), (34, -4, 1), (30, 12), (20, 6, 1), (22, 26), (30, 44)]))],
  [L(outline([(30, 46), (26, 20), (34, 4, 1), (40, 12), (44, -6, 1), (50, 8), (56, -8, 1), (62, 10), (68, 0, 1), (74, 22), (70, 46), (50, 50)]))])

# Rumer Reveale: máscara roja ovalada como de portero de hockey que le tapa toda la cara, con agujeros para los ojos
# amarillos de párpado caído; pelo morado en mechones curvos que se levantan por detrás
MSKR = _c('#c03a1e')
C('rumer-reveale', 'normal', pal('#9a4a8a', '#a8724e', '#d8c020', shade='#783a6a'),
  F(eyes='none', brows=False, mouth='none', hairline=False),
  [L(outline([(14, 70), (6, 40), (-8, 30, 1), (12, 24), (16, -6, 1), (32, 10), (46, -18, 1), (56, 6), (74, -12, 1), (78, 14), (100, 4, 1), (92, 30), (108, 44, 1), (94, 56), (86, 70)])),
   L(ell(50, 74, 32, 40), MSKR, 'f'),
   L(blob([(30, 72), (44, 70), (44, 78), (30, 78)], 4), _c('#2a1a14'), 'f', False), L(blob([(70, 72), (56, 70), (56, 78), (70, 78)], 4), _c('#2a1a14'), 'f', False),
   L(ell(37, 75, 4, 2.6), _c('#e8d040'), 'f', False), L(ell(63, 75, 4, 2.6), _c('#e8d040'), 'f', False),
   L([(48, 44), (48, 54), (52, 54), (52, 44), (48, 44)], _c('#7a2010'), 'f', False, False, 1.2)] +
  [L(ell(x, y, 1.6, 1.6), _c('#7a2010'), 'f', False) for x, y in ((34, 90), (66, 90), (44, 100), (56, 100))],
  [L(outline([(52, 60), (60, 40), (80, 30), (92, 10, 1), (66, 12), (60, -10, 1), (44, 6), (22, -10, 1), (24, 14), (0, 10, 1), (8, 34), (-6, 50, 1), (8, 60), (14, 80), (30, 84)])),
   L(blob([(64, 40), (84, 38), (96, 70), (90, 104), (70, 112)], 6), MSKR, 'f')],
  [L(outline([(14, 80), (6, 40), (-8, 30, 1), (12, 24), (16, -6, 1), (32, 10), (46, -18, 1), (56, 6), (74, -12, 1), (78, 14), (100, 4, 1), (92, 30), (108, 44, 1), (94, 56),
              (86, 80), (50, 86)]))])

# Rundeep Stillwater: melena lisa morada muy larga hasta el pecho, con un mechón amarillo a cada lado de la cara y la raya en
# punta sobre la frente; cara alargada, ojos cerrados en uve y media sonrisa
C('rundeep-stillwater', 'delgado', pal('#5a3a8a', '#f2dcc0', shade='#42286a'),
  F(eyes='closed', brows=True, mouth='smile', mouth_y=98, hairline=[(14, 60), (22, 40), (36, 34), (50, 52), (64, 34), (78, 40), (86, 60)],
    face_front=face(chin=110), face_side=face_side(chin=8, nose=3)),
  dome('front', top=0, w=46, cy=44, long=130, flare=4, seed=83) +
  [L(outline([(16, 36), (24, 32), (22, 90), (16, 132, 1), (12, 90)]), _c('#f0c040'), 'f'), L(outline([(84, 36), (76, 32), (78, 90), (84, 132, 1), (88, 90)]), _c('#f0c040'), 'f')],
  dome('side', top=0, w=46, cy=44, long=130, flare=4, seed=83, fr=52) + [L(outline([(70, 36), (78, 34), (76, 90), (72, 128, 1), (68, 90)]), _c('#f0c040'), 'f')],
  dome('back', top=0, w=46, cy=44, long=132, flare=4, seed=83, ends=3))

# Ruth "Ruby" Byron: media melena roja rosada en casco con las puntas abiertas a los lados y un flequillo largo que le tapa
# un ojo; ojo rojo con pestañas y sonrisa pícara
C('ruth-ruby-byron', 'chica', pal('#d8284e', '#f8dcc0', '#c0202e', shade='#a81e3a'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=94, hairline=[(12, 62), (22, 44), (40, 38), (60, 40), (78, 46), (88, 62)]),
  dome('front', top=0, w=48, cy=46, sb=80, seed=84) +
  [L(outline([(10, 70), (-8, 84, 1), (14, 86)]), 'mid'), L(outline([(90, 70), (108, 84, 1), (86, 86)]), 'mid'),
   fr([(36, 34), (66, 32), (74, 50), (66, 86), (56, 102, 1), (54, 72), (44, 52)])],
  dome('side', top=0, w=48, cy=46, nape=88, fr=56, seed=84) + [L(outline([(16, 74), (-4, 88, 1), (20, 90)]), 'mid')],
  dome('back', top=0, w=48, cy=46, nape=90, seed=84) + [L(outline([(10, 74), (-8, 88, 1), (14, 90)]), 'mid'), L(outline([(90, 74), (108, 88, 1), (86, 90)]), 'mid')])

# Ryan Tamer: pelo morado abultado en un bloque con dos picos arriba como orejas y el borde ondulado sobre la frente; ojos
# amarillos grandes con rayas negras debajo, como de payaso, y sonrisa; gorguera blanca y negra al cuello
C('ryan-tamer', 'normal', pal('#5a2a7a', '#f2c08a', '#e0b020', shade='#421e5a'),
  F(eyes='round', brows=False, mouth='smile', mouth_y=94, hairline=[(12, 60), (20, 56), (30, 60), (40, 54), (50, 60), (60, 54), (70, 60), (80, 56), (88, 60)]),
  bush('front', top=-14, w=46, cy=30, n=10, amp=4, seed=85, sb=64) +
  [L(outline([(10, 10), (4, -24, 1), (30, -4)]), 'mid'), L(outline([(90, 10), (96, -24, 1), (70, -4)]), 'mid'),
   L([(30, 82), (32, 92)], BLACK, 'f', False, False, 1.6), L([(70, 82), (68, 92)], BLACK, 'f', False, False, 1.6),
   L(blob([(14, 104), (30, 100), (50, 106), (70, 100), (86, 104), (90, 114), (50, 118), (10, 114)], 6), WHITE, 'f')],
  bush('side', top=-14, w=46, cy=30, n=10, amp=4, seed=85, nape=80, fr=56) + [L(outline([(20, 6), (12, -26, 1), (40, -6)]), 'mid')],
  bush('back', top=-14, w=46, cy=30, n=10, amp=4, seed=85, nape=80) +
  [L(outline([(10, 10), (4, -24, 1), (30, -4)]), 'mid'), L(outline([(90, 10), (96, -24, 1), (70, -4)]), 'mid')])

# Ryota Tsutsui: pelo castaño rojizo despeinado en pinchos cortos con unas gafas de aviador sobre la frente; cara redonda,
# ojos pequeños y sonrisa
C('ryota-tsutsui', 'normal', pal('#8a3a22', '#f0c090', '#2a2020', shade='#6a2a18'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=hl(5, 62, 48, 58, jit=2, seed=7)),
  dome('front', top=0, w=48, cy=44, n=9, amp=10, seed=86, sb=72) + goggles('front', y=46, frame=(60, 110, 70, 255), lens=(240, 220, 150, 255)),
  dome('side', top=0, w=48, cy=44, n=9, amp=10, seed=86, nape=88, fr=56) + goggles('side', y=42, frame=(60, 110, 70, 255), lens=(240, 220, 150, 255)),
  dome('back', top=0, w=48, cy=44, n=9, amp=10, seed=86, nape=88) + goggles('back', y=46, frame=(60, 110, 70, 255)))

# Sal Armando: piel verde azulada de pez con la cabeza alargada y una gorra blanca de marinero, con mechones azul marino
# en picos a los lados; ojos amarillos entornados y boca grande seria
FISH = _c('#7aa8a0')
C('sal-armando', 'corpulento', pal('#2a3a5a', '#7aa8a0', '#e0c030', shade='#1e2a42'),
  F(eyes='sharp', brows='angry', mouth='line', mouth_y=100, hairline=False, face_front=face(w=4, chin=110, jaw=6), face_side=face_side(chin=8, jaw=6, nose=4), ears=False),
  [L(outline([(16, 60), (-4, 44, 1), (10, 52), (-2, 62, 1), (14, 66), (22, 54)])), L(outline([(84, 60), (104, 44, 1), (90, 52), (102, 62, 1), (86, 66), (78, 54)])),
   cap('front', _c('#eef0e0'), top=16, rim=56, w=36, z='f'), L(blob([(14, 52), (50, 46), (86, 52), (84, 60), (50, 56), (16, 60)], 6), _c('#eef0e0'), 'f'),
   L([(46, 72), (44, 92), (56, 92)], _c('#5a8880'), 'f', False, False, 1.6)],
  [L(outline([(40, 60), (20, 46, 1), (28, 60), (16, 70, 1), (40, 70)])), cap('side', _c('#eef0e0'), top=16, rim=54, w=36, z='f')],
  [L(outline([(16, 62), (-4, 46, 1), (10, 54), (-2, 64, 1), (14, 68)])), L(outline([(84, 62), (104, 46, 1), (90, 54), (102, 64, 1), (86, 68)])),
   cap('back', _c('#eef0e0'), top=16, rim=54, w=36, z='f')])

# Sal Hughes: pelo rojo intenso con un flequillo enorme echado a un lado que le tapa un ojo y media cara; piel morena, ojo
# ámbar con raya negra, un pendiente de aro y boca seria
C('sal-hughes', 'normal', pal('#d0281e', '#b07a50', '#d8a020', shade='#a81e16'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=95, hairline=[(12, 62), (22, 44), (40, 38), (60, 40), (78, 46), (88, 62)]),
  dome('front', top=-2, w=48, cy=46, sb=82, seed=87) +
  [fr([(10, 40), (50, 28), (70, 40), (64, 70), (50, 86, 1), (40, 70), (24, 74, 1), (18, 58)]), L(ell(86, 88, 2, 2.4), WHITE, 'f')],
  dome('side', top=-2, w=48, cy=46, nape=90, fr=60, seed=87),
  dome('back', top=-2, w=48, cy=46, nape=90, seed=87))

# Sally Honeywell: capucha negra de gato con una oreja rosa y unos ojos de botón cosidos encima, y un cascabel dorado al
# cuello; pelo verde menta con un remolino rosa en la frente y dos mechones rizados a los lados; ojos rosas grandes
MINT = _c('#8ae0c0')
def _cat_hood(view):
    if view == 'front':
        return [ring([(2, 108), (-4, 60), (8, 22), (4, -18, 1), (30, 4), (50, 0), (70, 4), (100, -18, 1), (92, 22), (104, 60), (98, 108), (50, 112)],
                     [(18, 98), (14, 66), (22, 44), (50, 36), (78, 44), (86, 66), (82, 98), (50, 104)], BLACK),
                L(outline([(80, 8), (98, -14, 1), (90, 18)]), _c('#d86070'), 'f', False),
                L(ell(34, 18, 7, 7), _c('#d84a6a'), 'f', False, True), L(ell(34, 18, 2.4, 2.4), BLACK, 'f', False), L(ell(64, 20, 3, 3), _c('#d84a6a'), 'f', False),
                L(ell(50, 110, 4, 4), _c('#e8c040'), 'f')]
    if view == 'side':
        return [L(outline([(72, 106), (74, 80), (78, 52), (86, 34), (76, 8), (60, -16, 1), (46, 2), (18, 10), (0, 44), (0, 92), (20, 110), (50, 112)]), BLACK)]
    return [L(outline([(2, 108), (-4, 60), (8, 22), (4, -18, 1), (30, 4), (50, 0), (70, 4), (100, -18, 1), (92, 22), (104, 60), (98, 108), (50, 114)]), BLACK)]
C('sally-honeywell', 'chica', pal('#8ae0c0', '#f8e0cc', '#d8486a', shade='#6ac0a0'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=95, hairline=False),
  [L(outline([(18, 90), (16, 60), (26, 44), (50, 38), (74, 44), (84, 60), (82, 90), (76, 70), (66, 58), (34, 58), (24, 70)]), 'mid', 'f'),
   L(curls(50, 52, (8, 7), 4), _c('#f0a0b0'), 'f'),
   L(quad((14, 70), (2, 86), (14, 96)), MINT, 'f', False, False, 5), L(quad((86, 70), (98, 86), (86, 96)), MINT, 'f', False, False, 5)] + _cat_hood('front'),
  [L(outline([(60, 60), (76, 50), (84, 64), (70, 76)]), 'mid', 'f')] + _cat_hood('side'),
  _cat_hood('back'))

# Sam "Brave" Arritan: pelo rojo carmesí en pinchos altos de punta y una diadema dorada con una gema verde en la frente;
# ojos verdes de enfado y sonrisa
GLD = _c('#e8b83a')
C('sam-brave-arritan', 'normal', pal('#c0204a', '#f6cc98', '#2a9a7a', shade='#981838'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=94, hairline=[(12, 62), (20, 54), (50, 52), (80, 54), (88, 62)]),
  dome('front', top=-10, w=48, cy=44, n=7, amp=18, seed=88, sb=72) +
  [L(quad((18, 54), (50, 44), (82, 54)) + quad((80, 62), (50, 52), (20, 62)), GLD, 'f', True), L(ell(50, 52, 5, 4), _c('#3ab08a'), 'f', True)],
  dome('side', top=-10, w=48, cy=44, n=7, amp=18, seed=88, nape=88, fr=54) + [L([(54, 52), (90, 46), (90, 54), (54, 60)], GLD, 'f', True)],
  dome('back', top=-10, w=48, cy=44, n=7, amp=18, seed=88, nape=88))

# Sammy Salter (portero): melena pelirroja larga echada a un lado que le tapa un ojo, recogida en una trenza gorda que le
# cae por el hombro con un lazo verde oscuro; ojo negro, una lágrima pintada y sonrisa
C('sammy-salter', 'normal', pal('#c84a1e', '#f8dcc0', '#1e1a1a', shade='#a03a16'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=94, hairline=[(12, 62), (22, 44), (40, 38), (60, 40), (78, 46), (88, 62)]),
  dome('front', top=0, w=48, cy=46, sb=84, seed=89) +
  [fr([(14, 40), (50, 30), (54, 50), (44, 80), (34, 96, 1), (30, 70), (18, 66)]),
   L(ell(84, 98, 7, 8), 'mid', 'f'), L(ell(84, 112, 6, 7), 'mid', 'f'), L(outline([(76, 118), (92, 118), (90, 128), (78, 128)]), _c('#2a4a2a'), 'f'),
   L(blob([(66, 82), (70, 82), (69, 90), (67, 90)], 3), BLACK, 'f', False)],
  dome('side', top=0, w=48, cy=46, nape=90, fr=56, seed=89) + [L(ell(40, 98, 6, 8), 'mid', 'f')],
  dome('back', top=0, w=48, cy=46, nape=90, seed=89) + [L(ell(18, 98, 7, 8), 'mid'), L(ell(16, 112, 6, 7), 'mid')])

# Samson "Biggles" Bigglesworth (portero): pelo granate en pinchos gruesos enormes con una cinta negra en la frente; ojos
# grandes de sorpresa y la boca muy abierta
C('samson-biggles-bigglesworth', 'normal', pal('#8a1e2a', '#f6cc98', '#2a2020', shade='#6a141e'),
  F(eyes='round', brows=False, mouth='none', hairline=[(12, 62), (20, 56), (50, 54), (80, 56), (88, 62)]),
  dome('front', top=-14, w=52, cy=44, n=6, amp=20, seed=90, sb=72) + [band('front', BLACK, y=50, h=10, w=46, z='b'),
                                                                     L(ell(50, 96, 7, 6), _c('#8a2a2a'), 'f', False, True), L(blob([(44, 92), (56, 92), (55, 95), (45, 95)], 3), WHITE, 'f', False),
                                                                     L(ell(50, 99, 4, 2), _c('#e07a6a'), 'f', False)],
  dome('side', top=-14, w=52, cy=44, n=6, amp=20, seed=90, nape=88, fr=56) + [band('side', BLACK, y=46, h=10, z='b')],
  dome('back', top=-14, w=52, cy=44, n=6, amp=20, seed=90, nape=88) + [band('back', BLACK, y=50, h=10, w=46, z='b')])
