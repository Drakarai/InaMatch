"""Ojeadores de GX (scouts-gx), tanda 01: dibujados a partir de su retrato de Victory Road; claves 'scouts-gx:<id>'.

Muchos son alienígenas de Galaxy: pieles de colores, orejas de punta, cascos con cuernos, cabezas de animal o de pantalla.
Con modelo 3D del mismo personaje (para perfil y espalda): Adrastus Argos, Catora Peiji, Cedric Blossom, Chip Flashman,
Clark von Wunderbar (el oso) y Ducksquiggan Barboyle (los cinco Ducksquiggan comparten forma). Ayudas de esta tanda:
helm() (casco que tapa cabeza y mejillas con una ventana para los ojos), boxhead() (cabeza de pantalla), duck() (los
Ducksquiggan) y hornpair()."""
import math
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401
from chars_scouts_ie1_09 import dome, hl, face, face_side, mark, _c  # noqa: F401
from chars_scouts_ie2_03 import ears_pointy, teeth_grin
from chars_scouts_ie2_04 import sharp_eyes, sharp_eye_side, _mushroom

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
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[f'scouts-gx:{pid}'] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def fr(pts, c='mid'):
    """Mechones por delante de la cara."""
    return L(outline(pts), c, 'f')


def mir(pts):
    return [(100 - p[0],) + tuple(p[1:]) for p in pts]


def hornpair(pts, c, z='f'):
    """Un cuerno (de frente, lado izquierdo de la imagen) y su simétrico."""
    return [L(outline(pts), c, z), L(outline(mir(pts)), c, z)]


def helm(view, c, win=68, cheek=96, top=-2, w=0, z='f'):
    """Casco que tapa la cabeza y las mejillas y deja una ventana para los ojos y la boca (de win hacia abajo)."""
    if view == 'front':
        return L(outline([(12 - w, cheek, 1), (6 - w, 52), (12 - w, 24), (30, 4 + top), (50, top), (70, 4 + top), (88 + w, 24), (94 + w, 52), (88 + w, cheek, 1),
                          (76, cheek - 6), (74, win + 6), (62, win - 1), (50, win + 2), (38, win - 1), (26, win + 6), (24, cheek - 6)]), c, z)
    if view == 'side':
        return L(outline([(90, win + 2), (94, 42), (82, 12), (56, top - 2), (28, 4 + top), (8, 26), (2, 56), (8, 86), (28, cheek + 2), (50, cheek - 2), (58, win + 10),
                          (72, win + 4)]), c, z)
    return L(outline([(10, cheek), (4, 50), (12, 22), (30, 4 + top), (50, top), (70, 4 + top), (88, 22), (96, 50), (90, cheek), (50, cheek + 6)]), c, z)


def boxhead(view, c, screen, frame, knob, faces):
    """Cabeza de pantalla (robot): caja de color c con la pantalla y la cara de píxeles (faces: lista de capas de frente)."""
    if view == 'front':
        return ([L(blob([(-4, 46), (8, 46), (8, 56), (-4, 56)], 2), knob, 'f'), L(blob([(92, 46), (104, 46), (104, 56), (92, 56)], 2), knob, 'f'),
                 L(blob([(6, -6), (94, -6), (96, 98), (4, 98)], 3), c, 'f'), L(blob([(18, 10), (82, 10), (82, 86), (18, 86)], 2), frame, 'f', False),
                 L(blob([(22, 14), (78, 14), (78, 82), (22, 82)], 2), screen, 'f', False)] + faces)
    if view == 'side':
        return [L(blob([(10, -6), (92, -6), (94, 98), (8, 98)], 3), c, 'f'), L(blob([(40, 44), (56, 44), (56, 58), (40, 58)], 2), knob, 'f'),
                L(blob([(88, 12), (95, 12), (95, 84), (88, 84)], 2), frame, 'f', False)]
    return [L(blob([(-4, 46), (8, 46), (8, 56), (-4, 56)], 2), knob, 'f'), L(blob([(92, 46), (104, 46), (104, 56), (92, 56)], 2), knob, 'f'),
            L(blob([(6, -6), (94, -6), (96, 98), (4, 98)], 3), c, 'f'), L(blob([(14, 6), (86, 6), (86, 90), (14, 90)], 3), 'boxd', 'f', False)]


def px(cells, c, x0=26, y0=20, s=4):
    """Cara de píxeles: cells = lista de (columna, fila)."""
    return [L(blob([(x0 + i * s, y0 + j * s), (x0 + i * s + s - 0.6, y0 + j * s), (x0 + i * s + s - 0.6, y0 + j * s + s - 0.6), (x0 + i * s, y0 + j * s + s - 0.6)], 1),
              c, 'f', False) for i, j in cells]


def eyes_white(ey=74, sep=15, rx=7, ry=4.6, iris=BLACK, ang=True, pr=2.6):
    """Ojos blancos rasgados con pupila (sobre máscaras, cascos o cabezas de animal), de frente."""
    out = []
    for cx, s_ in ((50 - sep, 1), (50 + sep, -1)):
        e = [(cx - rx * s_, ey - (3 if ang else ry)), (cx + rx * s_, ey + (1 if ang else -ry)), (cx + rx * 0.7 * s_, ey + ry), (cx - rx * 0.8 * s_, ey + ry * 0.6)]
        out += [L(e, WHITE, 'f', True), L(ell(cx + 1.5 * s_, ey + 1.2, pr, pr + 0.6), iris, 'f', False)]
    return out


def eye_white_side(ey=74, iris=BLACK):
    return [L([(76, ey - 3), (88, ey), (87, ey + 4.6), (77, ey + 3.6)], WHITE, 'f', True), L(ell(84, ey + 1.2, 2.2, 2.8), iris, 'f', False)]


# ------------------------------------------------------------------ jugadores

# Adrastus Argos (adulto): melena larga ondulada gris oscuro hasta los hombros, peinada hacia atrás con un pico en la frente;
# ojos rojos afilados, arrugas y boca seria
AA = P('#5a4c54', '#f2d2ae', iris='#c01e1e', shade='#3e3238')
C('adrastus-argos', 'delgado', AA,
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, face_front=face(chin=106, jaw=-1), face_side=face_side(chin=6),
    hairline=[(12, 70), (18, 50), (32, 44), (44, 48), (50, 58), (56, 48), (68, 44), (82, 50), (88, 70)]),
  dome('front', top=0, w=48, cy=46, n=9, amp=6, soft=True, long=118, flare=10, seed=11) +
  [mark([(30, 84), (34, 88)], OUTC, w=0.9), mark([(70, 84), (66, 88)], OUTC, w=0.9), mark([(44, 66), (56, 66)], OUTC, w=0.8)],
  dome('side', top=0, w=48, cy=46, n=9, amp=6, soft=True, long=116, flare=10, fr=46, seed=11),
  dome('back', top=0, w=48, cy=46, n=9, amp=6, soft=True, long=118, flare=10, ends=5, seed=11))

# Akram Alvayra: cara de lagarto verde agua con marcas azul petróleo en la frente, morro más claro, ojos amarillos y dientes
# apretados; melena morada en greñas largas que se abren hacia los lados
AK = P('#8a4aa0', '#80b8a8', iris='#d8a020', mark='#3a6a70', muz='#c4dcd0')
C('akram-alvayra', 'normal', AK,
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, hairline=[(12, 70), (18, 52), (30, 44), (50, 40), (70, 44), (82, 52), (88, 70)]),
  dome('front', top=-12, w=52, cy=44, n=7, amp=18, sweep=0.3, seed=21, sb=86) +
  [mark([(44, 52), (50, 44), (56, 52), (50, 60)], 'mark'), mark([(32, 56), (38, 52), (40, 60)], 'mark'), mark([(68, 56), (62, 52), (60, 60)], 'mark'),
   mark([(36, 86), (50, 82), (64, 86), (60, 100), (50, 104), (40, 100)], 'muz', 'b')],
  dome('side', top=-12, w=52, cy=44, n=7, amp=18, sweep=0.3, seed=21, nape=96, fr=46) + [mark([(80, 50), (86, 46), (88, 56)], 'mark')],
  dome('back', top=-12, w=52, cy=44, n=7, amp=18, sweep=0.3, seed=21, long=100, flare=10))

# Alec Sarker: casco rosa malva con dos cuernos altos que le tapa la cabeza y las mejillas; deja ver unos ojos blancos de
# mirada torva y la cara gris, con una pieza turquesa en la barbilla; pelo negro largo por detrás
AS = P('#2a2228', '#a8a8b2', iris='#1e1a1e', helm='#c47e88', helmd='#9a5a66', chin='#3ad8c8')
C('alec-sarker', 'normal', AS, F(eyes='sharp', brows=False, mouth='line', mouth_y=90, hairline=False),
  dome('front', top=4, w=46, cy=46, long=112, flare=8, shade=False) + hornpair([(28, 22), (24, -16, 1), (36, 14)], 'helm') + [helm('front', 'helm', win=68)] +
  [mark([(50, 4), (60, 10), (62, 40), (50, 62)], 'helmd'), mark([(40, 98), (60, 98), (50, 110)], 'chin')],
  dome('side', top=4, w=46, cy=46, long=110, flare=8, fr=46, shade=False) + [L(outline([(30, 14), (20, -18, 1), (44, 6)]), 'helm', 'f'), helm('side', 'helm', win=68),
                                                                        mark([(84, 98), (92, 98), (86, 108)], 'chin')],
  dome('back', top=4, w=46, cy=46, long=112, flare=8, shade=False) + hornpair([(28, 22), (24, -16, 1), (36, 14)], 'helm') + [helm('back', 'helm')])

# Amon Boaker: casco plateado entero con dos antenas negras larguísimas en aspa; ojos redondos con aro naranja y cara gris
AB = P('#22222a', '#a8a8b0', iris='#e07020', helm='#d0d4dc', helmd='#9aa0ac', ant='#2a3048')
C('amon-boaker', 'normal', AB, F(eyes='round', brows=False, mouth='line', mouth_y=92, hairline=False),
  dome('front', top=4, w=46, cy=46, long=114, flare=8, shade=False) +
  hornpair([(36, 20), (6, -30, 1), (12, -24), (42, 16)], 'ant') + [helm('front', 'helm', win=66)] + [mark([(50, 2), (62, 24), (50, 64), (38, 24)], 'helmd')],
  dome('side', top=4, w=46, cy=46, long=110, flare=8, fr=46, shade=False) + [L(outline([(52, 10), (20, -34, 1), (26, -28), (58, 6)]), 'ant', 'f'), helm('side', 'helm', win=66)],
  dome('back', top=4, w=46, cy=46, long=114, flare=8, shade=False) + hornpair([(36, 20), (6, -30, 1), (12, -24), (42, 16)], 'ant') + [helm('back', 'helm')])

# Anky Mo: piel verde agua, media melena rosa que se abre hacia fuera en las puntas y dos mechones de punta arriba como
# orejas; ojos amarillos entornados y sonrisa pequeña
AM = P('#e88a96', '#7ab0a0', iris='#e0c840', shade='#c86a76')
C('anky-mo', 'normal', AM, F(eyes='sharp', brows=False, mouth='smile', mouth_y=92, hairline=[(12, 66), (18, 50), (36, 42), (56, 46), (72, 42), (84, 50), (88, 66)]),
  hornpair([(18, 24), (14, -10, 1), (34, 12)], 'mid', 'b') + dome('front', top=2, w=46, cy=46, long=92, flare=18, seed=31) +
  [fr([(14, 56), (20, 34), (44, 26), (62, 30), (40, 40), (24, 54)])],
  [L(outline([(40, 14), (40, -12, 1), (58, 8)]), 'mid', 'b')] + dome('side', top=2, w=46, cy=46, long=90, flare=18, fr=46, seed=31),
  hornpair([(18, 24), (14, -10, 1), (34, 12)], 'mid', 'b') + dome('back', top=2, w=46, cy=46, long=92, flare=18, seed=31))

# Anthocia Arnin (portera): pelo rojo con un mechón de punta en la frente y dos coletas bajas abultadas atadas con gomas
# blancas; orejas de punta, ojos grandes verde grisáceo y un halo turquesa y blanco sobre la cabeza
AN = P('#c83a22', '#f8dcc0', iris='#4a8a8a', halo='#40c8c0', tie=(240, 240, 240, 255))


def _halo(view):
    if view == 'side':
        return [L(ell(48, -14, 30, 5) + [ell(48, -14, 30, 5)[0]], 'halo', 'f', False, False, 2.4)]
    return [L(ell(50, -12, 40, 9) + [ell(50, -12, 40, 9)[0]], 'halo', 'f', False, False, 2.6),
            L(ell(50, -6, 34, 7) + [ell(50, -6, 34, 7)[0]], WHITE, 'f', False, False, 2.0)]


C('anthocia-arnin', 'chica', AN,
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=[(14, 64), (20, 48), (36, 42), (46, 52), (50, 62), (54, 52), (64, 42), (80, 48), (86, 64)]),
  ears_pointy('front') + [L(blob([(2, 96), (14, 92), (22, 104), (16, 118), (2, 116)], 6)), L(blob([(98, 96), (86, 92), (78, 104), (84, 118), (98, 116)], 6)),
                          L(ell(14, 92, 5, 3), 'tie', 'f'), L(ell(86, 92, 5, 3), 'tie', 'f')] +
  dome('front', top=0, w=46, cy=46, sb=78, seed=41) + _halo('front'),
  ears_pointy('side') + dome('side', top=0, w=46, cy=46, nape=88, fr=48, seed=41) + [L(blob([(20, 88), (34, 86), (36, 104), (24, 112), (14, 102)], 6)),
                                                                                       L(ell(30, 86, 4, 3), 'tie', 'f')] + _halo('side'),
  ears_pointy('back') + dome('back', top=0, w=46, cy=46, nape=88, seed=41) + [L(blob([(2, 96), (14, 90), (22, 104), (16, 118), (2, 116)], 6)),
                                                                                 L(blob([(98, 96), (86, 90), (78, 104), (84, 118), (98, 116)], 6))] + _halo('back'))

# Arenite Serka: máscara de bestia color arena con cuernos cortos a los lados y marcas crema en la frente, un moño castaño
# arriba, ojos con raya azul marino y sonrisa de dientes con el morro claro
AR = P('#8a5a3a', '#bc8e62', iris='#2a2a5a', cream='#f0dcc0', muz='#e6cca8')
C('arenite-serka', 'normal', AR, F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, hairline=False),
  [L(ell(50, 32, 10, 9))] + hornpair([(18, 46), (0, 30, 1), (14, 30)], 'skin') +
  [mark([(42, 40), (50, 32), (58, 40), (50, 56)], 'cream'), mark([(30, 48), (38, 44), (40, 56)], 'cream'), mark([(70, 48), (62, 44), (60, 56)], 'cream'),
   mark([(38, 86), (50, 82), (62, 86), (58, 102), (42, 102)], 'muz', 'b')],
  [L(ell(40, 18, 9, 9)), L(outline([(40, 46), (28, 28, 1), (46, 36)]), 'skin', 'f'), mark([(78, 40), (86, 36), (86, 54)], 'cream')],
  [L(ell(50, 30, 10, 9))] + hornpair([(18, 46), (0, 30, 1), (14, 30)], 'skin', 'b'))

# Ares Zumish: casco azul marino con cuernos curvos hacia fuera y una cresta turquesa; la visera le deja los ojos en sombra
# negra y solo se le ve la cara lila pálido de la nariz abajo
AZ = P('#24304a', '#ecdcf0', iris='#1e1a1e', helm='#2e4064', crest='#4ad0e0', shadow=(20, 18, 26, 255))
C('ares-zumish', 'chica', AZ, F(eyes='none', brows=False, mouth='line', mouth_y=92, hairline=False),
  hornpair([(14, 40), (-12, 8, 1), (-4, 4), (20, 26)], 'helm') + [helm('front', 'helm', win=74, cheek=102, w=4)] +
  [mark([(46, 0), (54, 0), (52, 20), (48, 20)], 'crest'), mark([(26, 74), (74, 74), (72, 82), (28, 82)], 'shadow')],
  [L(outline([(20, 30), (-6, 6, 1), (0, 0), (30, 18)]), 'helm', 'f'), helm('side', 'helm', win=74, cheek=102), mark([(72, 76), (90, 74), (90, 82), (74, 82)], 'shadow')],
  hornpair([(14, 40), (-12, 8, 1), (-4, 4), (20, 26)], 'helm') + [helm('back', 'helm', cheek=104, w=4)])

# Arion Mark Markion (fusión de Arion y Mark): pelo castaño en pinchos con la cinta naranja de Mark, ojos grises redondos
# y sonrisa
AX = P('#7a4a22', '#f4c48e', iris='#5a6070', band='#e0702a')
C('arion-mark-markion', 'normal', AX, F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=hl(5, 62, 56, 62, jit=2, seed=51)),
  dome('front', top=-2, w=48, cy=46, n=9, amp=10, seed=51, sb=72) + [mark([(10, 52), (50, 46), (90, 52), (90, 60), (50, 56), (10, 60)], 'band')],
  dome('side', top=-2, w=48, cy=46, n=9, amp=10, seed=51, nape=86, fr=52) + [mark([(6, 46), (90, 46), (90, 56), (6, 58)], 'band'),
                                                                                 L(outline([(4, 50), (-10, 62, 1), (6, 58)]), 'band', 'f')],
  dome('back', top=-2, w=48, cy=46, n=9, amp=10, seed=51, nape=86) + [mark([(8, 50), (92, 50), (92, 58), (8, 58)], 'band'),
                                                                        L(outline([(46, 56), (40, 74, 1), (50, 60), (60, 74, 1), (54, 56)]), 'band', 'f')])

# Aurora Sorker: máscara blanca con un casco turquesa de tres cuernos (una cresta alta) y unas piezas blancas en forma de
# ala a los lados; melena turquesa lisa hasta el pecho, ojos turquesa y labios azules
AU = P('#7ac4d0', '#f2f2f6', iris='#2ab0b0', helm='#8ad0dc', wing=(250, 250, 250, 255), lip='#3a5ac0')
C('aurora-sorker', 'chica', AU, F(eyes='sharp', brows=False, mouth='none', hairline=False),
  dome('front', top=6, w=44, cy=46, long=118, flare=6, seed=61) +
  [L(outline([(16, 64), (-8, 52, 1), (10, 78)]), 'wing', 'f'), L(outline([(84, 64), (108, 52, 1), (90, 78)]), 'wing', 'f'),
   L(outline([(16, 66), (14, 40), (6, 6, 1), (28, 26), (44, 30), (50, -22, 1), (56, 30), (72, 26), (94, 6, 1), (86, 40), (84, 66), (66, 60), (50, 70, 1), (34, 60)]), 'helm', 'f'),
   mark([(46, 52), (50, 46), (54, 52), (50, 58)], WHITE), mark([(46, 96), (54, 96)], 'lip', w=1.8)],
  dome('side', top=6, w=44, cy=46, long=116, flare=6, fr=46, seed=61) +
  [L(outline([(40, 64), (16, 52, 1), (34, 80)]), 'wing', 'f'), L(outline([(88, 62), (90, 30), (70, 18), (60, -20, 1), (52, 20), (30, 20), (14, 36), (30, 58), (60, 52)]), 'helm', 'f')],
  dome('back', top=6, w=44, cy=46, long=118, flare=6, ends=5, seed=61) +
  [L(outline([(16, 40), (6, 6, 1), (28, 22), (50, -22, 1), (72, 22), (94, 6, 1), (84, 40), (50, 50)]), 'helm', 'f')])

# Axel Shawn Shaxel (fusión de Axel y Shawn): pelo lila claro de pinchos hacia arriba y hacia atrás, con dos mechones que le
# caen por la frente; ojos oscuros afilados y boca seria
AXS = P('#bab2dc', '#f4d6b0', iris='#4a4040', shade='#9890c4')
C('axel-shawn-shaxel', 'normal', AXS, F(eyes='sharp', brows='angry', mouth='line', mouth_y=92, hairline=hl(5, 62, 50, 60, lean=1, jit=3, seed=71)),
  dome('front', top=-14, w=50, cy=44, n=9, amp=16, sweep=-0.2, seed=71, sb=74) + [fr([(40, 42), (46, 40), (48, 66, 1), (42, 52)]), fr([(56, 40), (62, 42), (60, 54), (56, 64, 1)])],
  dome('side', top=-14, w=50, cy=44, n=9, amp=18, sweep=-0.6, seed=71, nape=88, fr=50),
  dome('back', top=-14, w=50, cy=44, n=9, amp=16, seed=71, nape=88))

# Bailong Tezcat Tezlong (fusión): pelo azul hielo en pinchos echados a un lado con dos cuentas redondas turquesa; piel
# morena, ojos oscuros y unas marcas rosas junto a las orejas
BT = P('#b6dcea', '#c88a5a', iris='#3a2a2a', bead='#4ab0c0', pink='#e88aa8')
C('bailong-tezcat-tezlong', 'normal', BT, F(eyes='sharp', brows=True, mouth='frown', mouth_y=92, hairline=hl(6, 62, 50, 60, lean=2, jit=3, seed=81)),
  dome('front', top=-6, w=50, cy=44, n=8, amp=14, sweep=0.5, seed=81, sb=72) +
  [L(ell(30, 18, 4, 4), 'bead', 'f'), L(ell(70, 18, 4, 4), 'bead', 'f'), mark([(18, 72), (24, 72)], 'pink', w=1.6), mark([(82, 72), (76, 72)], 'pink', w=1.6)],
  dome('side', top=-6, w=50, cy=44, n=8, amp=14, sweep=0.5, seed=81, nape=86, fr=50) + [L(ell(50, 16, 4, 4), 'bead', 'f')],
  dome('back', top=-6, w=50, cy=44, n=8, amp=14, sweep=0.5, seed=81, nape=86) + [L(ell(30, 20, 4, 4), 'bead', 'f'), L(ell(70, 20, 4, 4), 'bead', 'f')])

# Bailong Victor Baivic (fusión): pelo azul verdoso ondulado y revuelto, con un mechón blanco en lo alto y un rizo largo que
# sale hacia un lado; ojos entornados
BV = P('#5aa0b0', '#f4dcc0', iris='#5a4a2a', white=(248, 248, 240, 255))
C('bailong-victor-baivic', 'normal', BV, F(eyes='sharp', brows=False, mouth='line', mouth_y=92, hairline=hl(6, 64, 50, 62, jit=3, seed=91)),
  dome('front', top=0, w=48, cy=46, n=9, amp=8, soft=True, seed=91, sb=80) + [L(ell(46, 2, 12, 9), 'white', 'f'),
                                                                            L(outline([(80, 30), (98, 24), (110, 10, 1), (102, 26), (86, 38)]), 'mid', 'f')],
  dome('side', top=0, w=48, cy=46, n=9, amp=8, soft=True, seed=91, nape=88, fr=50) + [L(ell(46, 0, 12, 9), 'white', 'f')],
  dome('back', top=0, w=48, cy=46, n=9, amp=8, soft=True, seed=91, nape=88) + [L(ell(52, 2, 12, 9), 'white', 'f'),
                                                                              L(outline([(20, 30), (2, 24), (-10, 10, 1), (-2, 26), (14, 38)]), 'mid', 'f')])

# Barton Combo: pelo morado oscuro en mechones revueltos de punta, una tirita en la nariz y unos cascos amarillos colgados
# del cuello; ojos afilados y sonrisa de pillo
BC = P('#4a3448', '#f4c48a', iris='#6a2a1a', phone='#f0b030', phoned='#8a8a8a')
C('barton-combo', 'normal', BC, F(eyes='sharp', brows='angry', mouth='smile', mouth_y=92, hairline=hl(5, 60, 48, 60, lean=1, jit=3, seed=101)),
  dome('front', top=-6, w=52, cy=44, n=8, amp=14, seed=101, sb=72) +
  [mark([(44, 82), (56, 80), (57, 85), (45, 87)], _c('#f6e2c4')),
   L(blob([(22, 104), (36, 104), (36, 116), (22, 116)], 4), 'phone', 'f'), L(blob([(64, 104), (78, 104), (78, 116), (64, 116)], 4), 'phone', 'f'),
   L(quad((30, 104), (50, 112), (70, 104)), 'phoned', 'f', False, False, 2.4)],
  dome('side', top=-6, w=52, cy=44, n=8, amp=14, seed=101, nape=86, fr=50) + [L(blob([(60, 104), (76, 104), (76, 116), (60, 116)], 4), 'phone', 'f')],
  dome('back', top=-6, w=52, cy=44, n=8, amp=14, seed=101, nape=86))

# Bennet Goodacre: sombrero de seta roja con lunares blancos, media melena verde por debajo, piel verde menta pálido, ojos en
# espiral y sonrisa
BG = P('#58a840', '#cfe8dc', iris='#2a3a2a', cap='#e02a2a', dot=(250, 250, 250, 255))
C('bennet-goodacre', 'chica', BG, F(eyes='dot', brows=False, mouth='smile', mouth_y=93, hairline=[(14, 62), (20, 52), (50, 50), (80, 52), (86, 62)]),
  dome('front', top=30, w=44, cy=56, long=96, flare=4, shade=False) + _mushroom('front') +
  [L(ell(36, 75, 6, 6) + [ell(36, 75, 6, 6)[0]], OUTC, 'f', False, False, 1.0), L(ell(64, 75, 6, 6) + [ell(64, 75, 6, 6)[0]], OUTC, 'f', False, False, 1.0)],
  dome('side', top=30, w=44, cy=56, long=94, flare=4, fr=56, shade=False) + _mushroom('side'),
  dome('back', top=30, w=44, cy=56, long=96, flare=4, shade=False) + _mushroom('back'))

# Bettas Renden: melena azul larga con dos aletas que salen hacia los lados y un mechón rojo; piel azul claro, ojos negros
BR = P('#3a8ad0', '#a8d6f0', iris='#141014', red='#d0302a', shade='#2a6ab0')
C('bettas-renden', 'chica', BR, F(eyes='sharp', brows=False, mouth='smile', mouth_y=92, hairline=[(14, 66), (20, 50), (36, 44), (60, 40), (80, 48), (86, 66)]),
  [L(outline([(16, 40), (-14, 30, 1), (-4, 48), (16, 56)])), L(outline([(84, 40), (114, 30, 1), (104, 48), (84, 56)]))] +
  dome('front', top=2, w=46, cy=46, long=116, flare=6, seed=111) + [fr([(14, 60), (20, 36), (46, 22), (70, 26), (44, 36), (26, 56)]),
                                                                   mark([(30, 40), (40, 30), (34, 54)], 'red')],
  [L(outline([(40, 36), (12, 22, 1), (20, 44), (40, 50)]))] + dome('side', top=2, w=46, cy=46, long=114, flare=6, fr=46, seed=111),
  [L(outline([(16, 40), (-14, 30, 1), (-4, 48), (16, 56)])), L(outline([(84, 40), (114, 30, 1), (104, 48), (84, 56)]))] +
  dome('back', top=2, w=46, cy=46, long=116, flare=6, seed=111))

# Biffy Sausse: pelo rojo en pinchos con dos puntas como orejas de gato, una visera amarilla con montura plateada en la
# frente, orejas de punta, dos coletas bajas; ojos ámbar grandes y sonrisa de dientes
BS = P('#c82a1e', '#f4c896', iris='#a87020', visor='#f0d020', frame='#b8c0d0')
C('biffy-sausse', 'chica', BS, F(eyes='big', brows=True, mouth='grin', mouth_y=93, hairline=hl(6, 62, 52, 62, jit=2, seed=121)),
  ears_pointy('front') + [L(blob([(4, 92), (16, 88), (24, 102), (16, 118), (4, 114)], 6)), L(blob([(96, 92), (84, 88), (76, 102), (84, 118), (96, 114)], 6))] +
  hornpair([(14, 30), (16, -12, 1), (34, 14)], 'mid', 'b') + dome('front', top=0, w=48, cy=46, n=8, amp=10, seed=121, sb=74) +
  [L(blob([(26, 34), (46, 24), (70, 28), (66, 40), (40, 42)], 6), 'visor', 'f'), L(quad((22, 36), (48, 22), (78, 30)), 'frame', 'f', False, False, 2.2)],
  ears_pointy('side') + [L(outline([(40, 14), (36, -14, 1), (56, 8)]), 'mid', 'b')] + dome('side', top=0, w=48, cy=46, n=8, amp=10, seed=121, nape=88, fr=50) +
  [L(blob([(70, 28), (88, 30), (90, 40), (72, 40)], 6), 'visor', 'f'), L(blob([(22, 88), (34, 86), (36, 104), (24, 112), (16, 100)], 6))],
  ears_pointy('back') + hornpair([(14, 30), (16, -12, 1), (34, 14)], 'mid', 'b') + dome('back', top=0, w=48, cy=46, n=8, amp=10, seed=121, nape=88) +
  [L(blob([(4, 92), (16, 88), (24, 102), (16, 118), (4, 114)], 6)), L(blob([(96, 92), (84, 88), (76, 102), (84, 118), (96, 114)], 6))])

# Bo Lourdash: alienígena crema y calvo con unas orejas larguísimas en punta hacia los lados, cejas de hueso abultadas y un
# morro en pico oliva; ojos blancos de mirada fiera y una gorguera de pelo blanco al cuello
BL = P('#f0e0a8', '#f0e0a8', iris='#1e1a1e', ear='#e0b088', beak='#8a7a4a', ruff=(244, 240, 240, 255))
C('bo-lourdash', 'normal', BL, F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  [L(outline([(20, 64), (-26, 50, 1), (14, 82)]), 'skin', 'b'), L(outline([(80, 64), (126, 50, 1), (86, 82)]), 'skin', 'b'),
   L(outline([(16, 66), (-14, 56, 1), (14, 76)]), 'ear', 'b', False), L(outline([(84, 66), (114, 56, 1), (86, 76)]), 'ear', 'b', False)] +
  eyes_white(72, 15, 7, 4) + [mark([(22, 64), (50, 60), (78, 64), (76, 68), (50, 64), (24, 68)], 'skin_d'),
                              L(outline([(40, 86), (60, 86), (52, 112, 1), (48, 112, 1)]), 'beak', 'f'),
                              L(blob([(14, 100), (30, 96), (50, 104), (70, 96), (86, 100), (80, 112), (20, 112)], 6), 'ruff', 'f')],
  [L(outline([(48, 64), (4, 46, 1), (40, 80)]), 'skin', 'f')] + eye_white_side(72) + [L(outline([(80, 86), (92, 88), (86, 112, 1)]), 'beak', 'f'),
                                                                                     L(blob([(30, 100), (60, 98), (80, 104), (70, 112), (36, 112)], 6), 'ruff', 'f')],
  [L(outline([(20, 64), (-26, 50, 1), (14, 82)]), 'skin', 'b'), L(outline([(80, 64), (126, 50, 1), (86, 82)]), 'skin', 'b'),
   L(blob([(14, 100), (50, 96), (86, 100), (80, 112), (20, 112)], 6), 'ruff', 'f')])

# Brom Hexine: pelo granate oscuro en rizos que caen hasta el cuello, dos cuernos rosados curvos hacia arriba, orejas de
# punta, ojos oliva afilados, ceño fruncido y boca torcida
BH = P('#5a2430', '#e8c49a', iris='#6a6a2a', horn='#e0a0a0')
C('brom-hexine', 'normal', BH, F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=hl(6, 62, 50, 58, jit=3, seed=131)),
  ears_pointy('front') + dome('front', top=2, w=48, cy=46, n=10, amp=6, soft=True, long=96, flare=6, seed=131) +
  hornpair([(22, 34), (6, 20), (14, -6, 1), (18, 14), (32, 26)], 'horn'),
  ears_pointy('side') + dome('side', top=2, w=48, cy=46, n=10, amp=6, soft=True, long=94, flare=6, fr=48, seed=131) +
  [L(outline([(60, 22), (54, 8), (64, -14, 1), (64, 6), (70, 18)]), 'horn', 'f')],
  ears_pointy('back') + dome('back', top=2, w=48, cy=46, n=10, amp=6, soft=True, long=96, flare=6, seed=131) +
  hornpair([(22, 34), (6, 20), (14, -6, 1), (18, 14), (32, 26)], 'horn'))

# Bunash Magee: cabeza alargada como un tubo color crema, con un gorro verde oscuro de tachuelas arriba y una franja de
# cristal; sin ojos, una nariz en uve y una sonrisa enorme de dientes
BM = P('#3a4030', '#f4e2c8', iris='#1e1a1e', stud='#8a6a4a', glass='#c8a898')
TUBE = blob([(28, 30), (72, 30), (74, 104), (26, 104)], 3)
C('bunash-magee', 'normal', BM,
  F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, face_front=TUBE, face_side=blob([(30, 30), (76, 30), (78, 104), (28, 104)], 3)),
  [L(blob([(22, -18), (78, -18), (80, 30), (20, 30)], 3), 'mid', 'f'), L(ell(30, -6, 4, 4), 'stud', 'f'), L(ell(50, -8, 4, 4), 'stud', 'f'),
   L(ell(70, -6, 4, 4), 'stud', 'f'), L(blob([(26, 34), (74, 34), (74, 48), (26, 48)], 2), 'glass', 'f', False),
   mark([(46, 66), (50, 70), (54, 66)], OUTC, w=1.0)] + teeth_grin(90, 11, 8),
  [L(blob([(26, -18), (80, -18), (82, 30), (24, 30)], 3), 'mid', 'f'), L(blob([(30, 34), (78, 34), (78, 48), (30, 48)], 2), 'glass', 'f', False)],
  [L(blob([(22, -18), (78, -18), (80, 30), (20, 30)], 3), 'mid', 'f'), L(blob([(26, 30), (74, 30), (74, 104), (26, 104)], 3), 'skin', 'f')])

# Cameron Agura: lana lila grisácea que le envuelve toda la cabeza y le cae como una barba enorme bajo la barbilla, un pico
# rosa y dos ojos azules redondos
CA = P('#a8a2b6', '#b4aec0', iris='#3a5aa0', beak='#e0706a', shade='#8a849c', light='#d0cad8')
C('cameron-agura', 'chica', CA, F(eyes='round', brows=False, mouth='none', hairline=False, ears=False),
  [L(blob([(2, 70), (6, 20), (30, -4), (50, -8), (70, -4), (94, 20), (98, 70), (86, 112), (50, 122), (14, 112)], 8), 'mid', 'b'),
   L(blob([(14, 66), (24, 54), (50, 58), (76, 54), (86, 66), (82, 70), (18, 70)], 6), 'light', 'f'),
   L(blob([(14, 86), (36, 82), (50, 92), (64, 82), (86, 86), (84, 116), (50, 124), (16, 116)], 8), 'light', 'f'),
   L(quad((30, 100), (50, 112), (70, 100)), 'shade', 'f', False, False, 1.4),
   L(blob([(30, 82), (50, 78), (70, 82), (56, 96), (50, 100), (44, 96)], 4), 'beak', 'f')],
  [L(blob([(2, 70), (8, 16), (40, -8), (76, 0), (94, 30), (94, 80), (80, 116), (40, 120), (10, 104)], 8), 'mid', 'f'),
   L(blob([(68, 64), (92, 62), (94, 86), (72, 84)], 4), 'skin_d', 'f', False), L(ell(84, 72, 3.6, 4), WHITE, 'f'), L(ell(85, 72, 2, 2.4), 'iris', 'f', False),
   L(blob([(84, 80), (100, 84), (90, 96)], 4), 'beak', 'f')],
  [L(blob([(2, 70), (6, 20), (30, -4), (50, -8), (70, -4), (94, 20), (98, 70), (86, 112), (50, 122), (14, 112)], 8), 'mid', 'f'),
   L(blob([(56, 4), (86, 26), (90, 80), (70, 110), (62, 50)], 6), 'shade', 'f', False)])

# Carabcalkrab Antares: cara de bestia morena con un cuerno corto en la frente y marcas crema, melena azul de greñas que
# barre hacia atrás, ojos blancos con pupila azul y una sonrisa enorme de dientes
CK = P('#3a6aa8', '#c4926a', iris='#3a5aa0', cream='#f0d8b0')
C('carabcalkrab-antares', 'corpulento', CK, F(eyes='none', brows=False, mouth='none', hairline=[(12, 68), (16, 46), (36, 40), (50, 38), (64, 40), (84, 46), (88, 68)]),
  dome('front', top=-8, w=54, cy=44, n=7, amp=16, sweep=-0.4, seed=141, sb=84) +
  [L(outline([(42, 46), (50, 30, 1), (58, 46), (50, 52)]), 'cream', 'f'), mark([(26, 60), (38, 64), (30, 70)], 'cream'), mark([(74, 60), (62, 64), (70, 70)], 'cream')] +
  eyes_white(74, 15, 8, 5, _c('#3a5aa0')) + [mark([(22, 68), (44, 70)], OUTC, w=2.6), mark([(78, 68), (56, 70)], OUTC, w=2.6)] + teeth_grin(92, 15, 9),
  dome('side', top=-8, w=54, cy=44, n=7, amp=16, sweep=-0.6, seed=141, nape=92, fr=46) + [L(outline([(82, 44), (92, 30, 1), (90, 50)]), 'cream', 'f')] +
  eye_white_side(74, _c('#3a5aa0')) + [L(blob([(70, 92), (88, 90), (86, 100), (72, 100)], 2), WHITE, 'f')],
  dome('back', top=-8, w=54, cy=44, n=7, amp=16, seed=141, nape=92))

# Catora Peiji (con su modelo 3D): pelo lila en melena corta con una diadema blanca de cadenitas y una gema en la frente,
# dos coletas bajas largas; orejas de punta y ojos rosas
CP = P('#d4b8e8', '#f6dcc4', iris='#d07aa0', tiara=(246, 246, 250, 255), gem='#e0a8c8')
C('catora-peiji', 'chica', CP, F(eyes='big', brows=True, mouth='line', mouth_y=93, hairline=[(14, 64), (20, 48), (36, 44), (50, 50), (64, 44), (80, 48), (86, 64)]),
  ears_pointy('front') + [L(blob([(6, 84), (16, 80), (20, 112), (10, 122), (4, 112)], 6)), L(blob([(94, 84), (84, 80), (80, 112), (90, 122), (96, 112)], 6))] +
  dome('front', top=2, w=46, cy=46, sb=78, seed=151) +
  [L(quad((18, 50), (50, 40), (82, 50)), 'tiara', 'f', False, False, 1.8), L(ell(50, 54, 2.6, 3.4), 'gem', 'f')],
  ears_pointy('side') + dome('side', top=2, w=46, cy=46, nape=84, fr=48, seed=151) +
  [L(quad((22, 46), (56, 34), (86, 44)), 'tiara', 'f', False, False, 1.8), L(blob([(40, 82), (52, 82), (50, 112), (40, 120), (34, 104)], 6))],
  ears_pointy('back') + dome('back', top=2, w=46, cy=46, nape=84, seed=151) + [L(quad((12, 44), (50, 34), (88, 44)), 'tiara', 'f', False, False, 1.8),
                                                                               L(blob([(18, 84), (28, 82), (30, 112), (20, 122), (14, 108)], 6)),
                                                                               L(blob([(82, 84), (72, 82), (70, 112), (80, 122), (86, 108)], 6))])

# Catro Corydoras: pelo rubio en mechones de punta que se abren arriba como alas y le tapa un ojo; piel azul claro, ojo azul
# oscuro, sonrisa y bufanda naranja
CC = P('#f4d860', '#a8d4ec', iris='#2a3a8a', scarf='#e8a030', shade='#d8b040')
C('catro-corydoras', 'normal', CC, F(eyes='sharp', brows=False, mouth='smile', mouth_y=93, hairline=[(14, 64), (20, 46), (40, 42), (60, 40), (80, 46), (86, 64)]),
  hornpair([(16, 30), (-6, 4, 1), (30, 16)], 'mid', 'b') + dome('front', top=-2, w=50, cy=46, n=8, amp=12, seed=161, long=104, flare=8) +
  [fr([(14, 60), (16, 36), (40, 26), (54, 34), (50, 60), (40, 86, 1), (30, 68), (22, 80, 1)]),
   L(blob([(20, 102), (50, 106), (84, 98), (96, 110), (60, 118), (18, 114)], 6), 'scarf', 'f')],
  [L(outline([(40, 20), (20, -6, 1), (54, 10)]), 'mid', 'b')] + dome('side', top=-2, w=50, cy=46, n=8, amp=12, seed=161, long=100, flare=8, fr=46) +
  [L(blob([(40, 100), (88, 98), (90, 112), (44, 114)], 6), 'scarf', 'f')],
  hornpair([(16, 30), (-6, 4, 1), (30, 16)], 'mid', 'b') + dome('back', top=-2, w=50, cy=46, n=8, amp=12, seed=161, long=104, flare=8) +
  [L(blob([(14, 104), (86, 104), (88, 114), (12, 114)], 6), 'scarf', 'f')])

# Cedric Blossom (adulto, con su modelo 3D): pelo rosa viejo en casco corto con el flequillo recto, gafas rectangulares
# negras, ojos azules y boca seria
CB = P('#c08098', '#f6cc98', iris='#3a7ac0', shade='#a06078')
C('cedric-blossom', 'delgado', CB, F(eyes='normal', brows=True, mouth='frown', mouth_y=93, glasses=(30, 26, 30, 255), glasses_rect=True,
                                    hairline=[(14, 70), (18, 52), (30, 56), (44, 52), (56, 56), (70, 52), (82, 54), (86, 70)]),
  dome('front', top=4, w=46, cy=48, n=7, amp=4, soft=True, sb=80, seed=171),
  dome('side', top=4, w=46, cy=48, n=7, amp=4, soft=True, nape=92, fr=54, seed=171),
  dome('back', top=4, w=46, cy=48, n=7, amp=4, soft=True, nape=94, seed=171))

# Cherrie Menjikko: melena larga rosa salmón con dos orejas de zorro arriba, piel azul claro, ojos turquesa y boca en o
CM = P('#e8987e', '#a8d4ee', iris='#2a8a9a', shade='#c87a62', ear=(250, 236, 230, 255))
C('cherrie-menjikko', 'chica', CM, F(eyes='big', brows=False, mouth='none', hairline=[(14, 64), (20, 46), (36, 40), (54, 48), (70, 42), (84, 48), (86, 64)]),
  hornpair([(18, 26), (18, -14, 1), (36, 10)], 'mid', 'b') + dome('front', top=2, w=46, cy=46, long=114, flare=8, seed=181) +
  [fr([(46, 34), (62, 30), (64, 56), (58, 76, 1), (52, 54)]), L(ell(50, 96, 2.6, 3.2), (120, 40, 50, 255), 'f')],
  [L(outline([(42, 14), (40, -16, 1), (58, 6)]), 'mid', 'b')] + dome('side', top=2, w=46, cy=46, long=112, flare=8, fr=46, seed=181),
  hornpair([(18, 26), (18, -14, 1), (36, 10)], 'mid', 'b') + dome('back', top=2, w=46, cy=46, long=114, flare=8, seed=181))

# Chip Flashman (con su modelo 3D): una mata enorme de pinchos negros, piel morena, ojos grandes castaños, una marca de
# bigotes en la mejilla y media sonrisa
CF = P('#1e1a1a', '#e0a46a', iris='#4a2a1a')
C('chip-flashman', 'normal', CF, F(eyes='big', brows='angry', mouth='smile', mouth_y=92, hairline=hl(6, 64, 50, 62, jit=3, seed=191)),
  dome('front', top=-16, w=60, cy=44, n=13, amp=16, seed=191, sb=82, shade=False) + [mark([(74, 86), (82, 84)], OUTC, w=0.9), mark([(74, 89), (82, 89)], OUTC, w=0.9)],
  dome('side', top=-16, w=60, cy=44, n=12, amp=16, sweep=-0.4, seed=191, nape=96, fr=50, shade=False),
  dome('back', top=-16, w=60, cy=44, n=13, amp=16, seed=191, nape=96, shade=False))

# Claria Leone: melena rosa larga que le tapa un ojo, con dos mechones gruesos en punta que salen hacia los lados como
# cuernos; piel azul claro, ojo negro y sonrisa
CL = P('#e070a0', '#a8d6f0', iris='#141014', shade='#c0507e')
C('claria-leone', 'chica', CL, F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=[(14, 64), (20, 46), (36, 40), (60, 40), (80, 46), (86, 64)]),
  [L(outline([(18, 34), (-16, 10, 1), (-4, 30), (18, 50)])), L(outline([(82, 34), (116, 10, 1), (104, 30), (82, 50)]))] +
  dome('front', top=-2, w=48, cy=46, long=112, flare=6, seed=201) + [fr([(46, 30), (74, 32), (86, 50), (84, 74), (74, 90, 1), (66, 70), (54, 50)])],
  [L(outline([(40, 30), (6, 8, 1), (18, 32), (40, 46)]))] + dome('side', top=-2, w=48, cy=46, long=110, flare=6, fr=46, seed=201) +
  [fr([(70, 40), (90, 40), (94, 70), (88, 86, 1), (80, 60)])],
  [L(outline([(18, 34), (-16, 10, 1), (-4, 30), (18, 50)])), L(outline([(82, 34), (116, 10, 1), (104, 30), (82, 50)]))] +
  dome('back', top=-2, w=48, cy=46, long=112, flare=6, seed=201))

# Clark von Wunderbar (con su modelo 3D): cabeza de osito de peluche azul cielo, orejas redondas, hocico crema con una nariz
# negra grande y ojos de botón negros
CW = P('#40b4d8', '#46b8dc', iris='#141014', muz='#f0e2c8', earin='#2a90b8')
C('clark-von-wunderbar', 'corpulento', CW,
  F(eyes='dot', brows=False, mouth='none', hairline=False, ears=False, eye_y=66, eye_sep=20,
    face_front=blob([(8, 60), (16, 26), (50, 14), (84, 26), (92, 60), (86, 94), (50, 108), (14, 94)], 8)),
  [L(ell(12, 22, 13, 13), 'skin', 'b'), L(ell(88, 22, 13, 13), 'skin', 'b'), L(ell(12, 22, 7, 7), 'earin', 'b', False), L(ell(88, 22, 7, 7), 'earin', 'b', False),
   L(blob([(30, 70), (50, 64), (70, 70), (72, 96), (50, 104), (28, 96)], 8), 'muz', 'f'), L(blob([(40, 70), (60, 70), (58, 80), (42, 80)], 4), BLACK, 'f'),
   mark([(50, 80), (50, 90)], OUTC, w=1.2), L(quad((38, 92), (44, 96), (50, 90)) + quad((50, 90), (56, 96), (62, 92))[1:], OUTC, 'f', False, False, 1.2)],
  [L(ell(36, 16, 12, 12), 'skin', 'f'), L(blob([(70, 70), (96, 70), (96, 96), (74, 98)], 6), 'muz', 'f'), L(blob([(90, 70), (100, 72), (100, 80), (90, 80)], 3), BLACK, 'f'),
   L(ell(74, 62, 2.6, 3), BLACK, 'f')],
  [L(ell(12, 22, 13, 13), 'skin', 'b'), L(ell(88, 22, 13, 13), 'skin', 'b'),
   L(blob([(8, 60), (16, 24), (50, 12), (84, 24), (92, 60), (86, 94), (50, 108), (14, 94)], 8), 'skin', 'f')])

# Coby Redstone: rastas gruesas azules con lunares claros que salen en todas direcciones y una que le cae por la cara; piel
# morena, ojos entornados, orejas con marcas y labios rosas
CR = P('#3a6aa8', '#c48a5a', iris='#2a1a1a', dot='#7ab0d8', lip='#e898a0')


def _dreads(view, cx=50):
    out = []
    for i, (a, l) in enumerate(((-150, 26), (-125, 30), (-100, 32), (-80, 32), (-55, 30), (-30, 26), (-170, 22), (-10, 22))):

        r = math.radians(a)
        bx, by = cx + 30 * math.cos(r), 40 + 28 * math.sin(r)
        tx, ty = cx + (30 + l) * math.cos(r), 40 + (28 + l) * math.sin(r)
        out.append(L(rope((bx, by), ((bx + tx) / 2, (by + ty) / 2 - 2), (tx, ty), 7), 'mid', 'b'))
        out.append(L(ell((bx + tx) / 2, (by + ty) / 2, 2.4, 2.4), 'dot', 'b', False))
    return out


C('coby-redstone', 'normal', CR, F(eyes='sharp', brows=False, mouth='lips', mouth_y=94, mouth_w=7, hairline=[(14, 60), (20, 50), (50, 46), (80, 50), (86, 60)]),
  _dreads('front') + dome('front', top=10, w=40, cy=46, sb=62, shade=False) + [L(rope((50, 40), (44, 56), (52, 70), 6), 'mid', 'f')],
  _dreads('side', 44) + dome('side', top=10, w=40, cy=46, nape=78, fr=50, shade=False),
  _dreads('back') + dome('back', top=10, w=40, cy=46, nape=78, shade=False))

# Concord Rigan: sombrero de fieltro negro calado hasta los ojos, que le deja la cara en sombra, dos mechones negros
# larguísimos que le caen como orejas de perro, perilla negra y media sonrisa
CN = P('#1e1c20', '#f0c48e', iris='#141014', hat='#2a2a2e', hatd='#4a4a50')
C('concord-rigan', 'normal', CN, F(eyes='none', brows=False, mouth='smile', mouth_y=92, hairline=False),
  [L(blob([(8, 50), (20, 50), (24, 110), (10, 124), (2, 112)], 6)), L(blob([(92, 50), (80, 50), (76, 110), (90, 124), (98, 112)], 6)),
   L(blob([(-6, 50), (50, 40), (106, 50), (104, 60), (50, 56), (-4, 60)], 6), 'hat', 'f'),
   L(blob([(16, 50), (20, 8), (50, 0), (80, 8), (84, 50)], 8), 'hat', 'f'), L(blob([(18, 40), (82, 40), (82, 48), (18, 48)], 3), 'hatd', 'f', False),
   mark([(20, 60), (50, 58), (80, 60), (80, 80), (50, 84), (20, 80)], 'skin_d'), mark([(40, 100), (50, 98), (60, 100), (50, 108)], BLACK)],
  [L(blob([(28, 50), (42, 50), (44, 110), (32, 122), (24, 108)], 6)), L(blob([(-8, 52), (50, 42), (108, 50), (106, 60), (50, 58), (-6, 62)], 6), 'hat', 'f'),
   L(blob([(14, 50), (20, 8), (50, 0), (80, 8), (86, 50)], 8), 'hat', 'f'), mark([(80, 98), (90, 98), (86, 106)], BLACK)],
  [L(blob([(8, 50), (20, 50), (24, 110), (10, 124), (2, 112)], 6)), L(blob([(92, 50), (80, 50), (76, 110), (90, 124), (98, 112)], 6)),
   L(blob([(-6, 50), (50, 40), (106, 50), (104, 60), (50, 56), (-4, 60)], 6), 'hat', 'f'), L(blob([(16, 50), (20, 8), (50, 0), (80, 8), (84, 50)], 8), 'hat', 'f')])

# Cord Ratozol: piel naranja, pelo rubio peinado hacia arriba en una coleta de punta, una marca oscura en la frente y unas
# gafas de soldador de cristales negros redondos con montura oliva; sonríe con la boca abierta
CZ = P('#f0c850', '#d87048', iris='#141014', lens=(26, 24, 28, 255), frame='#8a8a4a', mark='#8a3a2a')
C('cord-ratozol', 'normal', CZ, F(eyes='none', brows=False, mouth='grin', mouth_y=94, hairline=[(14, 60), (20, 40), (50, 34), (80, 40), (86, 60)]),
  dome('front', top=0, w=44, cy=44, n=6, amp=12, sweep=0.6, sb=56, seed=211, shade=False) + [L(outline([(50, 10), (70, -10), (96, -6, 1), (80, 4), (66, 20)]), 'mid', 'f'),
   mark([(46, 48), (54, 48), (52, 56), (48, 56)], 'mark'), L(quad((14, 74), (50, 66), (86, 74)), 'frame', 'f', False, False, 3.0),
   L(ell(35, 76, 9, 8), 'frame', 'f'), L(ell(65, 76, 9, 8), 'frame', 'f'), L(ell(35, 76, 7, 6), 'lens', 'f', False), L(ell(65, 76, 7, 6), 'lens', 'f', False)],
  dome('side', top=0, w=44, cy=44, n=6, amp=12, sweep=0.6, nape=74, fr=44, seed=211, shade=False) + [L(outline([(30, 10), (6, -6, 1), (20, 8), (40, 20)]), 'mid', 'f'),
   L([(46, 72), (86, 70)], 'frame', 'f', False, False, 3.0), L(ell(84, 74, 6, 7), 'frame', 'f'), L(ell(85, 74, 4, 5), 'lens', 'f', False)],
  dome('back', top=0, w=44, cy=44, n=6, amp=12, sweep=0.6, nape=74, seed=211, shade=False) + [L(outline([(44, 20), (50, -10, 1), (56, 20)]), 'mid', 'f'),
                                                                                            L(quad((10, 72), (50, 76), (90, 72)), 'frame', 'f', False, False, 3.0)])

# Craig Chart: cabeza de dinosaurio naranja con marcas crema en la frente, cuernecillos atrás, ojos amarillos de mirada fiera
# y una sonrisa enorme de dientes en punta con la mandíbula crema
CH = P('#d87448', '#d87448', iris='#d8a020', cream='#f0dcc0')
C('craig-chart', 'normal', CH, F(eyes='none', brows=False, mouth='none', hairline=False, ears=False,
                                face_front=blob([(12, 60), (18, 26), (50, 12), (82, 26), (88, 60), (84, 96), (50, 108), (16, 96)], 8)),
  hornpair([(22, 22), (14, 4, 1), (30, 16)], 'skin', 'b') +
  [mark([(42, 30), (50, 22), (58, 30), (54, 54), (46, 54)], 'cream'), mark([(28, 36), (36, 32), (36, 48)], 'cream'), mark([(72, 36), (64, 32), (64, 48)], 'cream'),
   L(blob([(16, 84), (50, 92), (84, 84), (80, 100), (50, 110), (20, 100)], 6), 'cream', 'f')] +
  eyes_white(68, 16, 8, 5, _c('#d8a020')) + [mark([(20, 58), (44, 62)], OUTC, w=2.6), mark([(80, 58), (56, 62)], OUTC, w=2.6)] + teeth_grin(88, 24, 8),
  [L(outline([(30, 18), (18, 2, 1), (40, 12)]), 'skin', 'f'), L(blob([(64, 84), (96, 84), (92, 100), (66, 104)], 6), 'cream', 'f')] + eye_white_side(68, _c('#d8a020')),
  hornpair([(22, 22), (14, 4, 1), (30, 16)], 'skin', 'b'))

# Crow Icarus: cabeza de cuervo azul marino de plumas que caen por los hombros, pico amarillo y ojos blancos rasgados
CI = P('#283458', '#2e3c64', iris='#141014', beak='#f0d870', shade='#1e2844')
C('crow-icarus', 'normal', CI, F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  [L(outline([(6, 120), (2, 60), (-10, 34, 1), (14, 30), (30, 8), (50, 2), (70, 8), (86, 30), (110, 34, 1), (98, 60), (94, 120, 1), (80, 108), (66, 120, 1), (50, 108),
              (34, 120, 1), (20, 108)]), 'skin', 'b')] + eyes_white(66, 16, 10, 5.4, pr=3) +
  [L(outline([(30, 74), (50, 70), (70, 74), (54, 100, 1), (46, 100, 1)]), 'beak', 'f')],
  [L(outline([(10, 116), (4, 60), (12, 24), (40, 4), (72, 10), (90, 36), (92, 70), (80, 116, 1), (60, 104), (40, 118, 1), (24, 104)]), 'skin', 'f')] +
  eye_white_side(66) + [L(outline([(80, 72), (106, 82, 1), (82, 88)]), 'beak', 'f')],
  [L(outline([(6, 120), (2, 60), (-10, 34, 1), (14, 30), (30, 8), (50, 2), (70, 8), (86, 30), (110, 34, 1), (98, 60), (94, 120, 1), (80, 108), (66, 120, 1), (50, 108),
              (34, 120, 1), (20, 108)]), 'skin', 'f'), L(blob([(56, 10), (86, 34), (90, 100), (64, 104)], 6), 'shade', 'f', False)])

# Croy Roy: yelmo de caballero verde oscuro con una cresta de punta, dos cuernos laterales, una gema morada en la frente y la
# rendija negra de la cara; un pañuelo morado al cuello
CY = P('#3a4038', '#3a4038', iris='#141014', helm='#3e4a40', trim='#9aa0a0', gem='#8a5ad0', slot=(16, 14, 18, 255), scarf='#6a2a8a')
C('croy-roy', 'normal', CY, F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True),
  hornpair([(18, 40), (2, 4, 1), (30, 22)], 'helm') +
  [L(outline([(16, 104), (10, 50), (20, 16), (44, 4), (50, -24, 1), (56, 4), (80, 16), (90, 50), (84, 104), (50, 112)]), 'helm', 'f'),
   L(blob([(24, 62), (76, 62), (72, 96), (50, 104), (28, 96)], 4), 'slot', 'f', False), L(quad((30, 30), (50, 20), (70, 30)), 'trim', 'f', False, False, 1.6),
   L([(50, 36), (50, 104)], 'helm', 'f', False, False, 3.0), L(ell(50, 44, 6, 7), 'gem', 'f'),
   L(blob([(10, 104), (50, 98), (90, 104), (96, 118), (50, 124), (4, 118)], 6), 'scarf', 'f')],
  [L(outline([(14, 104), (8, 50), (20, 14), (50, 2), (56, -24, 1), (62, 4), (84, 18), (92, 50), (88, 104), (50, 110)]), 'helm', 'f'),
   L(blob([(74, 62), (92, 62), (90, 96), (76, 98)], 4), 'slot', 'f', False), L(outline([(30, 30), (12, 0, 1), (44, 20)]), 'helm', 'f'),
   L(blob([(14, 104), (90, 100), (96, 118), (12, 120)], 6), 'scarf', 'f')],
  hornpair([(18, 40), (2, 4, 1), (30, 22)], 'helm') +
  [L(outline([(16, 104), (10, 50), (20, 16), (44, 4), (50, -24, 1), (56, 4), (80, 16), (90, 50), (84, 104), (50, 112)]), 'helm', 'f'),
   L(blob([(10, 104), (50, 98), (90, 104), (96, 118), (50, 124), (4, 118)], 6), 'scarf', 'f')])

# Derika Cachil (portero): pelo rojo de pinchos altos con aletas a los lados, piel verde menta pálido, ojos rosas afilados
# con ceño fruncido y boca seria
DC = P('#c83a4a', '#c4e4dc', iris='#c060c0', fin='#e0a090', shade='#a0283a')
C('derika-cachil', 'normal', DC, F(eyes='sharp', brows='angry', mouth='frown', mouth_y=92, ears=False, hairline=hl(5, 62, 48, 60, jit=3, seed=221)),
  [L(outline([(16, 62), (0, 50, 1), (2, 70), (14, 84)]), 'fin', 'b'), L(outline([(84, 62), (100, 50, 1), (98, 70), (86, 84)]), 'fin', 'b')] +
  dome('front', top=-16, w=50, cy=44, n=6, amp=18, seed=221, sb=80),
  [L(outline([(44, 62), (30, 52, 1), (32, 74), (48, 82)]), 'fin', 'f')] + dome('side', top=-16, w=50, cy=44, n=6, amp=18, sweep=-0.4, seed=221, nape=90, fr=48),
  [L(outline([(16, 62), (0, 50, 1), (2, 70), (14, 84)]), 'fin', 'b'), L(outline([(84, 62), (100, 50, 1), (98, 70), (86, 84)]), 'fin', 'b')] +
  dome('back', top=-16, w=50, cy=44, n=6, amp=18, seed=221, nape=90))

# Dervan Yorhal: máscara de ave naranja con marcas crema que le tapa la cabeza, un antifaz negro alrededor de los ojos
# turquesa y la cara crema de pico abajo con los dientes apretados
DY = P('#d87040', '#f0dca8', iris='#3a9a9a', helm='#d87040', cream='#f4dcc0', band=(26, 22, 26, 255))
C('dervan-yorhal', 'normal', DY, F(eyes='none', brows=False, mouth='none', hairline=False, ears=False),
  hornpair([(14, 40), (2, 10, 1), (26, 22)], 'helm') + [helm('front', 'helm', win=68, cheek=92, w=2)] +
  [mark([(42, 22), (50, 12), (58, 22), (50, 46)], 'cream'), mark([(28, 30), (36, 26), (38, 42)], 'cream'), mark([(72, 30), (64, 26), (62, 42)], 'cream'),
   L(blob([(14, 66), (50, 70), (86, 66), (82, 84), (50, 90), (18, 84)], 6), 'band', 'f')] + sharp_eyes(_c('#3a9a9a'), 76, 15) + teeth_grin(96, 10, 5),
  [L(outline([(24, 30), (10, 4, 1), (36, 20)]), 'helm', 'f'), helm('side', 'helm', win=68, cheek=92), L(blob([(64, 66), (94, 66), (92, 84), (66, 84)], 6), 'band', 'f')] +
  sharp_eye_side(_c('#3a9a9a'), 76),
  hornpair([(14, 40), (2, 10, 1), (26, 22)], 'helm') + [helm('back', 'helm', cheek=94, w=2)])

# Diazo Cabot (portero): pelo verde petróleo muy oscuro de mechones de punta hacia arriba y a los lados, orejas de punta, una
# cicatriz que cruza un ojo cerrado, piel morena clara y boca seria
DZ = P('#1e3a3e', '#f0b880', iris='#1e2a2a')
C('diazo-cabot', 'normal', DZ, F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=hl(5, 62, 48, 58, lean=1, jit=2, seed=231)),
  ears_pointy('front') + dome('front', top=-6, w=54, cy=44, n=7, amp=16, sweep=0.2, seed=231, sb=82) +
  [mark([(66, 62), (60, 84)], OUTC, w=1.4), mark([(58, 76), (70, 76)], 'skin', w=4.0), mark([(58, 77), (70, 76)], OUTC, w=1.4)],
  ears_pointy('side') + dome('side', top=-6, w=54, cy=44, n=7, amp=16, sweep=-0.3, seed=231, nape=92, fr=48),
  ears_pointy('back') + dome('back', top=-6, w=54, cy=44, n=7, amp=16, seed=231, nape=92))

# Dioxily Bocca: piel morena, una mata de pelo crema en mechones de punta con dos cuernos crema, una cinta blanca, orejas de
# punta, una gema en la frente y ojos rojos fieros
DB = P('#f0e4c8', '#a8784a', iris='#c02a2a', band=(250, 250, 250, 255), gem='#6a6a7a', shade='#d0c0a0')
C('dioxily-bocca', 'normal', DB, F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=[(14, 62), (20, 48), (36, 46), (50, 42), (64, 46), (80, 48), (86, 62)]),
  ears_pointy('front') + dome('front', top=-2, w=46, cy=44, n=9, amp=8, soft=True, seed=241, sb=66) +
  hornpair([(34, 34), (28, -16, 1), (44, 28)], 'shade') + [L(quad((24, 16), (50, 6), (76, 16)), 'band', 'f', False, False, 3.0), L(ell(50, 52, 2.4, 3), 'gem', 'f')],
  ears_pointy('side') + dome('side', top=-2, w=46, cy=44, n=9, amp=8, soft=True, seed=241, nape=88, fr=48) + [L(outline([(60, 28), (62, -16, 1), (72, 24)]), 'shade', 'f')],
  ears_pointy('back') + dome('back', top=-2, w=46, cy=44, n=9, amp=8, soft=True, seed=241, nape=88) + hornpair([(34, 34), (28, -16, 1), (44, 28)], 'shade'))

# Doctor Cross Word Cryptix (adulto): pelo rubio crema alborotado, un bigote enorme y barba, y un monóculo tecnológico blanco
# con visor negro sobre un ojo
DX = P('#f0dca0', '#f4d4b0', iris='#2a2a2a', mono=(244, 244, 248, 255), visor=(30, 28, 34, 255), bar='#5ad0e0', shade='#d0b878')
C('doctor-cross-word-cryptix', 'delgado', DX,
  F(eyes='dot', brows=True, mouth='none', hairline=hl(6, 64, 48, 56, jit=3, seed=251), face_front=face(chin=106), face_side=face_side(chin=6)),
  dome('front', top=-6, w=52, cy=44, n=11, amp=10, soft=True, seed=251, sb=86) +
  [L(blob([(22, 86), (50, 82), (78, 86), (94, 94), (74, 96), (50, 92), (26, 96), (6, 94)], 6), 'mid', 'f'),
   L(blob([(30, 96), (50, 94), (70, 96), (64, 112), (50, 116), (36, 112)], 6), 'mid', 'f'),
   L(blob([(54, 64), (80, 64), (82, 84), (56, 84)], 4), 'mono', 'f'), L(blob([(58, 70), (78, 70), (74, 78), (60, 78)], 3), 'visor', 'f', False),
   mark([(62, 74), (72, 74)], 'bar', w=1.4)],
  dome('side', top=-6, w=52, cy=44, n=11, amp=10, soft=True, seed=251, nape=92, fr=48) +
  [L(blob([(66, 86), (98, 90), (90, 98), (70, 96)], 6), 'mid', 'f'), L(blob([(60, 96), (84, 96), (78, 114), (62, 112)], 6), 'mid', 'f'),
   L(blob([(72, 64), (92, 64), (92, 84), (74, 84)], 4), 'mono', 'f'), L(blob([(80, 70), (92, 70), (92, 78), (82, 78)], 3), 'visor', 'f', False)],
  dome('back', top=-6, w=52, cy=44, n=11, amp=10, soft=True, seed=251, nape=92))

# Doro Might: cabeza de animal marrón (como un topo) con marcas crema en la frente y un moño de tela verde petróleo arriba,
# ojos tristes caídos y un hocico crema con nariz de cerdito
DM = P('#2a4a4a', '#b87a3e', iris='#2a2020', cream='#f4e8cc', nose='#f0c0b0')
C('doro-might', 'normal', DM, F(eyes='round', brows=False, mouth='none', hairline=False, ears=False, eye_y=72,
                               face_front=blob([(14, 60), (20, 20), (50, 10), (80, 20), (86, 60), (82, 96), (50, 108), (18, 96)], 8)),
  [L(blob([(26, 8), (50, -10), (74, 8), (60, 14), (40, 14)], 6), 'mid', 'f'), L(ell(50, 12, 6, 4), (120, 180, 110, 255), 'f'),
   mark([(40, 24), (50, 20), (48, 44)], 'cream'), mark([(60, 24), (50, 20), (52, 44)], 'cream'),
   mark([(24, 66), (34, 64)], OUTC, w=1.6), mark([(76, 66), (66, 64)], OUTC, w=1.6),
   L(blob([(22, 84), (50, 78), (78, 84), (74, 104), (50, 110), (26, 104)], 8), 'cream', 'f'), L(blob([(40, 92), (60, 92), (58, 100), (42, 100)], 4), 'nose', 'f'),
   L(ell(46, 96, 1.2, 1.4), OUTC, 'f', False), L(ell(54, 96, 1.2, 1.4), OUTC, 'f', False)],
  [L(blob([(26, 18), (50, 2), (74, 18), (60, 26), (40, 26)], 6), 'mid', 'f'), L(blob([(64, 84), (96, 84), (94, 102), (68, 104)], 8), 'cream', 'f'),
   L(blob([(88, 90), (100, 92), (98, 100), (88, 100)], 3), 'nose', 'f')],
  [L(blob([(26, 8), (50, -10), (74, 8), (60, 14), (40, 14)], 6), 'mid', 'f'),
   L(blob([(14, 60), (20, 20), (50, 10), (80, 20), (86, 60), (82, 96), (50, 106), (18, 96)], 8), 'skin', 'f')])


# Dotmar Tricks: cabeza de pantalla roja con una franja granate, botones laterales azul marino y una cara de píxeles enfadada
DT = P('#e02a2a', '#e8c49a', iris='#141014', box='#e02a2a', boxd='#c01e1e', scr='#f0b840', frm='#2a3a4a', knob='#2a3a4a')
_angry = px([(1, 2), (2, 3), (3, 4), (9, 2), (8, 3), (7, 4), (2, 5), (3, 5), (7, 5), (8, 5), (2, 10), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 10)], BLACK)
C('dotmar-tricks', 'normal', DT, F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True),
  boxhead('front', 'box', 'scr', 'frm', 'knob', _angry), boxhead('side', 'box', 'scr', 'frm', 'knob', []), boxhead('back', 'box', 'scr', 'frm', 'knob', []))

# Doyle Coco: cabeza de pollito amarillo con la cara crema, un pico naranja, ojos entornados y una antena verde en espiral
DO = P('#f0c850', '#f4e8c4', iris='#141014', beak='#e8a030', ant='#5aa830', shade='#d8a838')
C('doyle-coco', 'normal', DO, F(eyes='sharp', brows=False, mouth='none', hairline=False, ears=False, eye_y=72,
                               face_front=blob([(14, 70), (22, 40), (50, 34), (78, 40), (86, 70), (78, 100), (50, 108), (22, 100)], 8)),
  [L(blob([(2, 60), (8, 18), (40, 0), (80, 4), (98, 30), (100, 80), (84, 108), (50, 116), (16, 108)], 8), 'mid', 'b'),
   L(blob([(14, 34), (40, 22), (70, 26), (96, 40), (70, 42), (40, 40)], 6), 'shade', 'b'),
   L(quad((30, 8), (10, -20), (34, -26)), 'ant', 'f', False, False, 6.0), L(quad((34, -26), (46, -16), (38, -10)), 'ant', 'f', False, False, 6.0),
   L(blob([(40, 82), (60, 82), (50, 94)], 3), 'beak', 'f')],
  [L(blob([(2, 60), (10, 16), (44, 0), (80, 8), (98, 36), (98, 80), (84, 108), (40, 114), (10, 100)], 8), 'mid', 'f'),
   L(blob([(66, 50), (94, 50), (94, 96), (70, 96)], 6), 'skin', 'f', False), L(ell(84, 72, 2.4, 3), OUTC, 'f', False),
   L(blob([(90, 80), (104, 86), (90, 92)], 3), 'beak', 'f'), L(quad((40, 4), (24, -22), (46, -26)), 'ant', 'f', False, False, 6.0)],
  [L(blob([(2, 60), (8, 18), (40, 0), (80, 4), (98, 30), (100, 80), (84, 108), (50, 116), (16, 108)], 8), 'mid', 'f'),
   L(quad((30, 8), (10, -20), (34, -26)), 'ant', 'f', False, False, 6.0)])

# Dry Karwack (portero): cara ancha color carne clara con marcas crema en la frente, ojos gris azulado de raya negra y una
# sonrisa enorme
DK = P('#e8cca8', '#e8cca8', iris='#6a7a9a', cream='#f6ecdc')
C('dry-karwack', 'corpulento', DK, F(eyes='none', brows=False, mouth='none', hairline=False, ears=False,
                                    face_front=blob([(6, 66), (14, 30), (50, 18), (86, 30), (94, 66), (88, 98), (50, 110), (12, 98)], 8)),
  [mark([(40, 30), (50, 22), (60, 30), (56, 50), (44, 50)], 'cream'), mark([(14, 68), (28, 62), (46, 70), (30, 84)], 'cream'),
   mark([(86, 68), (72, 62), (54, 70), (70, 84)], 'cream')] + eyes_white(74, 16, 7, 4.6, _c('#6a7a9a'), ang=False) +
  [L(quad((16, 86), (50, 96), (84, 86)) + quad((84, 86), (50, 110), (16, 86))[1:], WHITE, 'f', True, True), L([(24, 92), (76, 92)], OUTC, 'f', False, False, 0.8)],
  [L(blob([(66, 88), (92, 86), (88, 98)], 3), WHITE, 'f', True, True)],
  [L(blob([(6, 66), (14, 30), (50, 18), (86, 30), (94, 66), (88, 98), (50, 108), (12, 98)], 8), 'skin', 'f')])


def duck(view, helm_, star, patch):
    """Los Ducksquiggan (con el modelo 3D de Barboyle): casco de pulpo de color con un símbolo de estrella, ojos de mirada
    torva pintados en el casco, una gorguera blanca y debajo la cara gris de alienígena con dos ojos amarillos sobre manchas."""
    if view == 'front':
        return ([L(blob([(6, 30), (12, 0), (50, -10), (88, 0), (94, 30), (96, 62), (50, 70), (4, 62)], 8), helm_, 'f'),
                L(ell(4, 40, 4, 4), helm_, 'f'), L(ell(96, 40, 4, 4), helm_, 'f'),
                L([(50, 4), (50, 26)], star, 'f', False, False, 2.4), L([(40, 10), (60, 20)], star, 'f', False, False, 2.4), L([(60, 10), (40, 20)], star, 'f', False, False, 2.4),
                L(ell(50, 15, 3.4, 3.4), star, 'f', False)] + eyes_white(48, 15, 9, 4) +
               [L([(22, 40), (46, 46)], OUTC, 'f', False, False, 3.0), L([(78, 40), (54, 46)], OUTC, 'f', False, False, 3.0),
                L(blob([(8, 66), (50, 60), (92, 66), (86, 78), (50, 74), (14, 78)], 6), WHITE, 'f'),
                L(blob([(20, 80), (42, 78), (42, 94), (22, 94)], 6), patch, 'f', False), L(blob([(80, 80), (58, 78), (58, 94), (78, 94)], 6), patch, 'f', False),
                L(ell(32, 86, 4, 4), (240, 230, 90, 255), 'f'), L(ell(68, 86, 4, 4), (240, 230, 90, 255), 'f'),
                L(ell(32, 86, 1.6, 1.6), BLACK, 'f', False), L(ell(68, 86, 1.6, 1.6), BLACK, 'f', False)])
    if view == 'side':
        return [L(blob([(4, 30), (14, 0), (52, -10), (88, 0), (96, 30), (98, 62), (50, 68), (2, 60)], 8), helm_, 'f'),
                L(ell(60, 40, 4, 4), helm_, 'f')] + eye_white_side(48) + \
               [L(blob([(10, 64), (60, 60), (98, 64), (94, 76), (50, 74), (14, 78)], 6), WHITE, 'f'),
                L(blob([(76, 80), (92, 80), (92, 94), (78, 94)], 6), patch, 'f', False), L(ell(86, 86, 3.4, 4), (240, 230, 90, 255), 'f')]
    return [L(blob([(6, 30), (12, 0), (50, -10), (88, 0), (94, 30), (96, 62), (50, 70), (4, 62)], 8), helm_, 'f'),
            L(blob([(14, 40), (86, 40), (86, 54), (14, 54)], 4), 'helmd', 'f', False),
            L(blob([(8, 66), (50, 60), (92, 66), (86, 80), (50, 76), (14, 80)], 6), WHITE, 'f')]


for _pid, _h, _s, _p in (('ducksquiggan-barboyle', '#4a9a8a', '#c0e050', '#e0607a'), ('ducksquiggan-carboyle', '#e02a5a', '#f4f4f4', '#1e1a1e'),
                         ('ducksquiggan-garboyle', '#2aa040', '#f4f4f4', '#7a4ab0'), ('ducksquiggan-tarboyle', '#f0e040', '#f4f4f4', '#2a6ae0'),
                         ('ducksquiggan-zarboyle', '#8a4ab0', '#f4f4f4', '#f08a20')):
    _pp = P(_h, '#a8a8b2', iris='#141014', helm=_h, helmd=tuple(int(int(_h[i:i + 2], 16) * 0.8) for i in (1, 3, 5)) + (255,), star=_s, patch=_p)
    C(_pid, 'normal', _pp, F(eyes='none', brows=False, mouth='frown', mouth_y=100, hairline=False, ears=False),
      duck('front', 'helm', 'star', 'patch'), duck('side', 'helm', 'star', 'patch'), duck('back', 'helm', 'star', 'patch'))

# Durmali Altos (portero): media melena azul marino con dos mechones amarillos largos que caen por delante, un gorro de
# rayas blancas y azul marino con un rabito, piel azul claro, ojos grandes oscuros y sonrisa
DA = P('#2a2a8a', '#a8d4ec', iris='#1e1a2a', hat='#2a2a8a', hatw=(246, 246, 250, 255), yel='#e8e050')
C('durmali-altos', 'normal', DA, F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=[(14, 64), (20, 50), (50, 54), (80, 50), (86, 64)]),
  dome('front', top=10, w=46, cy=50, long=92, flare=6, shade=False) +
  [L(rope((22, 60), (20, 90), (24, 116), 3.4), 'yel', 'f'), L(rope((78, 60), (80, 90), (76, 116), 3.4), 'yel', 'f'),
   L(blob([(6, 50), (12, 14), (50, 0), (88, 14), (94, 50), (50, 44)], 8), 'hatw', 'f'), L(blob([(10, 30), (50, 18), (90, 30), (90, 40), (50, 30), (10, 40)], 4), 'hat', 'f', False),
   L(blob([(8, 44), (50, 38), (92, 44), (92, 52), (50, 48), (8, 52)], 4), 'hat', 'f', False), L(quad((50, 0), (56, -14), (62, -20)), 'hatw', 'f', False, False, 2.4)],
  dome('side', top=10, w=46, cy=50, long=90, flare=6, fr=54, shade=False) +
  [L(blob([(4, 50), (12, 12), (50, 0), (88, 12), (96, 46), (50, 44)], 8), 'hatw', 'f'), L(blob([(6, 30), (92, 26), (94, 36), (8, 40)], 4), 'hat', 'f', False),
   L(rope((76, 60), (78, 90), (74, 116), 3.4), 'yel', 'f')],
  dome('back', top=10, w=46, cy=50, long=92, flare=6, shade=False) +
  [L(blob([(6, 50), (12, 14), (50, 0), (88, 14), (94, 50), (50, 50)], 8), 'hatw', 'f'), L(blob([(10, 30), (50, 18), (90, 30), (90, 40), (50, 30), (10, 40)], 4), 'hat', 'f', False)])

# Eas Tarmo: una máscara de madera marrón que le tapa toda la cara, con dos surcos verticales y una rendija negra como gafas
# de sol
ET = P('#a87040', '#8a5030', iris='#141014', wood='#b07a44', woodd='#8a5a30', slot=(24, 20, 24, 255))
C('eas-tarmo', 'corpulento', ET, F(eyes='none', brows=False, mouth='none', hairline=False, ear_out=4),
  [L(blob([(10, 60), (16, 16), (50, 4), (84, 16), (90, 60), (84, 100), (50, 108), (16, 100)], 8), 'wood', 'f'),
   L([(36, 12), (34, 100)], 'woodd', 'f', False, False, 2.0), L([(64, 12), (66, 100)], 'woodd', 'f', False, False, 2.0),
   L(blob([(18, 62), (82, 62), (80, 72), (20, 72)], 3), 'slot', 'f', False), L(blob([(44, 72), (56, 72), (56, 84), (44, 84)], 3), 'woodd', 'f', False),
   L([(28, 92), (72, 92)], 'woodd', 'f', False, False, 2.0)],
  [L(blob([(14, 60), (20, 14), (54, 2), (86, 16), (94, 60), (88, 100), (54, 108), (20, 100)], 8), 'wood', 'f'),
   L(blob([(80, 62), (96, 62), (96, 72), (82, 72)], 3), 'slot', 'f', False)],
  [L(blob([(10, 60), (16, 16), (50, 4), (84, 16), (90, 60), (84, 100), (50, 108), (16, 100)], 8), 'wood', 'f'),
   L([(36, 12), (34, 100)], 'woodd', 'f', False, False, 2.0), L([(64, 12), (66, 100)], 'woodd', 'f', False, False, 2.0)])

# Edana Naves: casco de ave azul y blanco con cuernos, piel verde grisáceo, plumas blancas de punta negra a los lados de la
# cara, ojos oscuros afilados y sonrisa
ED = P('#2e5ab0', '#7aa892', iris='#1e1a1e', helm='#3a6ac0', white=(246, 246, 250, 255), tip='#2a2a4a')
C('edana-naves', 'normal', ED, F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=False),
  [L(outline([(14, 70), (-6, 96), (-14, 112, 1), (8, 104), (22, 84)]), 'white', 'b'), L(outline([(86, 70), (106, 96), (114, 112, 1), (92, 104), (78, 84)]), 'white', 'b'),
   L(outline([(-6, 96), (-14, 112, 1), (2, 104)]), 'tip', 'b', False), L(outline([(106, 96), (114, 112, 1), (98, 104)]), 'tip', 'b', False)] +
  hornpair([(22, 30), (14, -14, 1), (34, 14)], 'helm') +
  [L(outline([(14, 70), (12, 34), (30, 10), (50, 4), (70, 10), (88, 34), (86, 70), (64, 62), (50, 72, 1), (36, 62)]), 'helm', 'f'),
   mark([(42, 14), (50, 6), (58, 14), (54, 40), (50, 60), (46, 40)], 'white')],
  [L(outline([(40, 70), (24, 96), (18, 112, 1), (34, 104), (46, 84)]), 'white', 'f'), L(outline([(40, 20), (28, -16, 1), (52, 10)]), 'helm', 'f'),
   L(outline([(90, 64), (92, 30), (70, 10), (40, 6), (14, 30), (12, 64), (50, 62)]), 'helm', 'f')],
  [L(outline([(14, 70), (-6, 96), (-14, 112, 1), (8, 104), (22, 84)]), 'white', 'b'), L(outline([(86, 70), (106, 96), (114, 112, 1), (92, 104), (78, 84)]), 'white', 'b')] +
  hornpair([(22, 30), (14, -14, 1), (34, 14)], 'helm') + [L(outline([(14, 74), (12, 34), (30, 10), (50, 4), (70, 10), (88, 34), (86, 74), (50, 80)]), 'helm', 'f')])

# Eli Mantary: melena larga verde petróleo oscuro con dos aletas que salen hacia los lados, como una manta raya; le tapa un
# ojo; piel azul claro, ojo rojo y labios pequeños
EM = P('#1e5a62', '#a8d6ec', iris='#d02a2a', shade='#164448')
C('eli-mantary', 'chica', EM, F(eyes='big', brows=False, mouth='line', mouth_y=94, hairline=[(14, 64), (20, 46), (36, 40), (60, 40), (80, 46), (86, 64)]),
  [L(outline([(18, 34), (-18, 30), (-12, 40, 1), (18, 50)])), L(outline([(82, 34), (118, 30), (112, 40, 1), (82, 50)]))] +
  dome('front', top=-2, w=48, cy=46, long=118, flare=6, seed=261) + [fr([(14, 58), (16, 36), (40, 26), (54, 34), (52, 60), (44, 92, 1), (34, 70), (24, 84, 1)])],
  [L(outline([(40, 30), (4, 26), (10, 36, 1), (40, 46)]))] + dome('side', top=-2, w=48, cy=46, long=116, flare=6, fr=46, seed=261),
  [L(outline([(18, 34), (-18, 30), (-12, 40, 1), (18, 50)])), L(outline([(82, 34), (118, 30), (112, 40, 1), (82, 50)]))] +
  dome('back', top=-2, w=48, cy=46, long=118, flare=6, ends=5, seed=261))

# Elreid Orbes (portero): pelo azul grisáceo largo con dos picos arriba y mechones lacios por los lados, orejas larguísimas
# en punta, ojos turquesa afilados, ceño fruncido
EO = P('#5a7a9a', '#f4d8b8', iris='#2a9a9a', shade='#3e5a78')
C('elreid-orbes', 'delgado', EO, F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=hl(4, 62, 46, 60, jit=2, seed=271)),
  ears_pointy('front', h=22) + hornpair([(36, 20), (34, -18, 1), (46, 12)], 'mid', 'b') + dome('front', top=0, w=46, cy=46, n=7, amp=8, long=112, flare=4, seed=271),
  ears_pointy('side', h=22) + [L(outline([(50, 14), (50, -18, 1), (62, 8)]), 'mid', 'b')] + dome('side', top=0, w=46, cy=46, n=7, amp=8, long=110, flare=4, fr=48, seed=271),
  ears_pointy('back', h=22) + hornpair([(36, 20), (34, -18, 1), (46, 12)], 'mid', 'b') + dome('back', top=0, w=46, cy=46, n=7, amp=8, long=112, flare=4, ends=5, seed=271))

# Elu Suay: cabeza de pantalla blanca con pantalla rosa de cara de píxeles sonriente, marco amarillo y botones amarillos
EU = P('#f0f0f4', '#e8c49a', iris='#141014', box='#f4f4f8', boxd='#d0d4e0', scr='#f08890', frm='#f0e070', knob='#f0d040')
_happy = px([(1, 2), (2, 2), (3, 2), (1, 3), (3, 3), (1, 4), (2, 4), (3, 4), (7, 2), (8, 2), (9, 2), (7, 3), (9, 3), (7, 4), (8, 4), (9, 4),
             (1, 9), (2, 10), (3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 9)], BLACK)
C('elu-suay', 'normal', EU, F(eyes='none', brows=False, mouth='none', hairline=False, ears=False, no_head=True),
  boxhead('front', 'box', 'scr', 'frm', 'knob', _happy), boxhead('side', 'box', 'scr', 'frm', 'knob', []), boxhead('back', 'box', 'scr', 'frm', 'knob', []))

# Ewano Bee: cabeza de pingüino negro azulado con dos cuernos amarillos curvos, pico naranja, ojos blancos de pupila azul
# con cejas amarillas y marcas rojas en las mejillas
EB = P('#2e3036', '#33363e', iris='#3a7ac0', horn='#f0c830', beak='#f0a030', red='#d83a3a', white=(246, 246, 250, 255))
C('ewano-bee', 'normal', EB, F(eyes='none', brows=False, mouth='none', hairline=False, ears=False,
                               face_front=blob([(6, 70), (12, 30), (50, 12), (88, 30), (94, 70), (88, 108), (50, 116), (12, 108)], 8)),
  hornpair([(22, 30), (8, 10), (0, -24, 1), (16, 4), (32, 20)], 'horn', 'b') + eyes_white(70, 15, 7, 4, _c('#3a7ac0')) +
  [L([(22, 62), (42, 68)], 'horn', 'f', False, False, 2.6), L([(78, 62), (58, 68)], 'horn', 'f', False, False, 2.6),
   mark([(18, 78), (26, 78)], 'red', w=2.2), mark([(82, 78), (74, 78)], 'red', w=2.2),
   L(outline([(38, 74), (62, 74), (52, 96, 1), (48, 96, 1)]), 'beak', 'f'), L(blob([(24, 96), (50, 108), (76, 96), (80, 112), (20, 112)], 6), 'white', 'f')],
  [L(outline([(40, 20), (28, 0), (24, -26, 1), (36, -2), (50, 14)]), 'horn', 'f')] + eye_white_side(70, _c('#3a7ac0')) +
  [L(outline([(82, 74), (102, 84, 1), (84, 88)]), 'beak', 'f')],
  hornpair([(22, 30), (8, 10), (0, -24, 1), (16, 4), (32, 20)], 'horn', 'b'))
