"""Ojeadores de GO (scouts-go), tanda 08: dibujados a partir de su retrato de Victory Road; claves 'scouts-go:<id>'.

Ninguno tiene modelo 3D propio: el frente sale del retrato y el perfil y la espalda se deducen de cómo cae ese peinado.
Usa las ayudas de los ojeadores de IE (dome/hl/face de ie1_09, gafas de ie1_03 e ie2_03, capucha de ie3_02...)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401
from chars_scouts_ie1_09 import dome, hl, face, face_side, mark, _c  # noqa: F401
from chars_scouts_ie1_03 import goggles, round_specs, thick_brows, side_brow, blush, big_grin  # noqa: F401
from chars_scouts_ie2_03 import ears_pointy, teeth_grin, round_glasses  # noqa: F401
from chars_scouts_ie3_02 import hood, skull3, bowl3, scarf  # noqa: F401

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
    CHARS[f'scouts-go:{pid}'] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def fr(pts, c='mid', z='f'):
    """Mechón o flequillo por delante de la cara."""
    return L(outline(pts), c, z)


def lock(x, y0, y1, c='mid', wd=8, z='f', tip=True):
    """Mechón que cae recto junto a la cara."""
    return L(outline([(x - wd / 2, y0), (x + wd / 2, y0), (x + wd / 2 - 1, y1 - 6), (x, y1, 1) if tip else (x, y1), (x - wd / 2 + 1, y1 - 6)]), c, z)


def lashes(ey=75, sep=14, c=OUTC):
    """Pestañas hacia fuera (chicas)."""
    return [L([(50 - sep - 7, ey - 4), (50 - sep - 11, ey - 7)], c, 'f', False, False, 1.4),
            L([(50 + sep + 7, ey - 4), (50 + sep + 11, ey - 7)], c, 'f', False, False, 1.4)]


def lash_side(ey=75, c=OUTC):
    return [L([(86, ey - 4), (90, ey - 7)], c, 'f', False, False, 1.4)]


def nose_line(y=86, c=None):
    return L([(50, y - 5), (52, y), (49, y + 1)], c or (150, 90, 60, 255), 'f', False, False, 1.0)


# ------------------------------------------------------------------ jugadores

# Sapp Hirell: media melena azul lisa que le tapa el ojo izquierdo con un mechón largo; una mancha azul oscuro en lo alto;
# ojo azul con pestañas y media sonrisa
DB = _c('#24429b')
C('sapp-sapphire-hirell', 'normal', P('#3282d3', '#f6dcb6', iris='#2a6ab0', shade='#2a66b0', deep='#1d3a63'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=93, hairline=[(6, 66), (20, 50), (36, 46), (50, 44), (66, 48), (80, 52), (94, 66)]),
  dome('front', top=0, w=47, cy=46, sb=86) +
  [L(blob([(54, 2), (72, 6), (84, 20), (70, 24), (66, 34), (56, 22)], 6), DB, 'b', False),
   fr([(40, 30), (62, 28), (80, 40), (84, 66), (76, 100), (66, 106, 1), (66, 84), (58, 70), (48, 52)])] + lashes(),
  dome('side', top=0, w=47, cy=46, nape=90, fr=50) + [L(blob([(48, 4), (70, 8), (72, 22), (54, 20)], 6), DB, 'b', False),
                                                    fr([(70, 30), (88, 38), (92, 64), (86, 92), (80, 100, 1), (80, 70)])],
  dome('back', top=0, w=47, cy=46, nape=92) + [L(blob([(30, 4), (48, 2), (52, 18), (36, 22)], 6), DB, 'b', False)])

# Saskia Fresh: media melena verde oliva con las puntas vueltas hacia fuera; ojos rojos afilados con pestañas y un globo
# de chicle morado en la boca
PU = _c('#a070c0')
def _flicks(view):
    if view == 'front':
        return [L(outline([(4, 64), (2, 86), (-6, 98, 1), (10, 94), (18, 84), (20, 60)])),
                L(outline([(96, 64), (98, 86), (106, 98, 1), (90, 94), (82, 84), (80, 60)]))]
    if view == 'side':
        return [L(outline([(4, 60), (0, 90), (-8, 102, 1), (12, 96), (30, 84), (40, 66)]))]
    return [L(outline([(4, 60), (-6, 98, 1), (20, 92), (50, 96), (80, 92), (106, 98, 1), (96, 60)]))]
C('saskia-bubbles-fresh', 'chica', P('#918a21', '#f6e6c8', iris='#c02a20', shade='#6f6a18'),
  F(eyes='sharp', brows=True, mouth='none', mouth_y=94, hairline=[(6, 66), (16, 46), (30, 42), (50, 46), (70, 42), (84, 46), (94, 66)]),
  _flicks('front') + dome('front', top=0, w=48, cy=46, sb=80) + lashes() + [L(ell(50, 98, 7, 7), PU, 'f'), L(ell(48, 96, 2, 2), (210, 180, 230, 255), 'f', False)],
  _flicks('side') + dome('side', top=0, w=48, cy=46, nape=88, fr=48) + lash_side() + [L(ell(92, 96, 6, 6), PU, 'f')],
  _flicks('back') + dome('back', top=0, w=48, cy=46, nape=90))

# Saul Durban: turbante gris azulado enrollado que le tapa la frente y el ojo derecho; mascarilla blanca y piel morena;
# un solo ojo grande y redondo
TG, TD, MK = _c('#718b9b'), _c('#596974'), _c('#dde1e0')
def _turban(view):
    if view == 'front':
        return [L(outline([(10, 66), (4, 40), (16, 12), (50, 0), (84, 12), (96, 40), (92, 64), (80, 72), (66, 80), (54, 66), (40, 64), (20, 70)]), TG),
                L(quad((10, 50), (40, 40), (90, 22)), TD, 'f', False, False, 2), L(quad((14, 30), (50, 16), (80, 12)), TD, 'f', False, False, 2),
                L(quad((54, 66), (72, 58), (92, 46)), TD, 'f', False, False, 2)]
    if view == 'side':
        return [L(outline([(8, 76), (2, 40), (20, 8), (50, 0), (80, 10), (96, 34), (96, 62), (78, 66), (50, 62), (30, 70)]), TG),
                L(quad((6, 50), (40, 36), (94, 40)), TD, 'f', False, False, 2), L(quad((14, 26), (50, 12), (86, 20)), TD, 'f', False, False, 2)]
    return [L(outline([(8, 76), (4, 40), (16, 12), (50, 0), (84, 12), (96, 40), (92, 76), (50, 82)]), TG),
            L(quad((8, 56), (50, 40), (92, 30)), TD, 'f', False, False, 2), L(quad((10, 32), (50, 18), (88, 14)), TD, 'f', False, False, 2)]
C('saul-durban', 'normal', P('#2a2020', '#8d5d4c', iris='#141010'),
  F(eyes='none', brows=False, mouth='none', hairline=False),
  _turban('front') + [L(ell(36, 76, 8, 8), WHITE, 'f'), L(ell(38, 76, 4, 4.4), BLACK, 'f', False),
                      L(outline([(16, 84), (50, 80), (84, 84), (80, 98), (50, 106), (20, 98)]), MK, 'f')],
  _turban('side') + [L(ell(82, 74, 5, 7), WHITE, 'f'), L(ell(84, 74, 2.6, 4), BLACK, 'f', False),
                     L(outline([(60, 84), (88, 82), (90, 96), (74, 104), (60, 98)]), MK, 'f'), L([(60, 88), (44, 76)], MK, 'f', False, False, 1.4)],
  _turban('back') + [L([(14, 84), (86, 84)], MK, 'f', False, False, 1.4)])

# Saul Hermit: melena negra verdosa lisa con raya en medio hasta los hombros; orejas grandes en punta, gafas redondas
# oscuras con montura blanca, nariz larga y los dos dientes de delante
C('saul-hermit', 'delgado', P('#3f3f34', '#f7bb7d', iris='#141010', shade='#2c2c24'),
  F(eyes='none', brows=False, mouth='buck', mouth_y=100, face_front=face(chin=108), face_side=face_side(chin=6, nose=5),
    hairline=[(6, 66), (20, 46), (40, 36), (50, 34), (60, 36), (80, 46), (94, 66)], nose=(50, 88, 3)),
  ears_pointy('front', h=16) +
  [L(outline([(8, 104), (6, 50), (14, 18), (50, 0), (86, 18), (94, 50), (92, 104), (82, 100), (82, 50), (54, 30), (50, 40), (46, 30), (18, 50), (18, 100)]))] +
  [L(ell(36, 76, 9, 7), (40, 30, 50, 255), 'f'), L(ell(64, 76, 9, 7), (40, 30, 50, 255), 'f'),
   L(ell(36, 76, 9, 7) + [ell(36, 76, 9, 7)[0]], WHITE, 'f', False, False, 1.6), L(ell(64, 76, 9, 7) + [ell(64, 76, 9, 7)[0]], WHITE, 'f', False, False, 1.6),
   L([(45, 75), (55, 75)], WHITE, 'f', False, False, 1.6), L([(50, 78), (53, 90), (48, 92)], (190, 120, 80, 255), 'f', False, False, 1.2)],
  [L(outline([(48, 60), (56, 40), (80, 32), (88, 20), (70, 4), (40, 2), (16, 14), (4, 40), (2, 100), (14, 110), (30, 106), (40, 70)]))] +
  ears_pointy('side', h=16) + [L(ell(82, 76, 6, 7), (40, 30, 50, 255), 'f'), L([(76, 76), (50, 70)], WHITE, 'f', False, False, 1.6)],
  [L(outline([(6, 106), (4, 50), (14, 16), (50, 0), (86, 16), (96, 50), (94, 106), (50, 110)])),
   L([(50, 4), (50, 106)], 'shade', 'f', False, False, 1.2)])

# Scally Wagg: piel verde grisácea; pinchos azul oscuro disparados hacia arriba y a los lados con un mechón lila curvado;
# dos rayas amarillas en uve sobre la cara, ojos amarillos y una sonrisa enorme de dientes
YL, LV = _c('#f0d020'), _c('#829bc1')
C('scally-wagg', 'normal', P('#3c5d84', '#8db7a9', iris='#d8b020', shade='#2c4464', deep='#22344c', skin_d='#6f9488'),
  F(eyes='sharp', brows=False, mouth='none', hairline=[(6, 62), (18, 48), (32, 50), (44, 42), (58, 50), (70, 42), (84, 48), (94, 62)], ears_front=False),
  [L(outline([(10, 60), (8, 40), (-8, 30, 1), (8, 24), (0, 4, 1), (22, 12), (24, -16, 1), (40, 6), (52, -24, 1), (60, 4), (80, -14, 1), (78, 12), (100, 6, 1),
              (90, 26), (108, 34, 1), (92, 44), (90, 62), (80, 50), (20, 50)])),
   L(outline([(44, 8), (60, -2), (80, 10), (70, 40), (64, 60, 1), (62, 30), (52, 20)]), LV, 'f'),
   L([(30, 64), (50, 86), (70, 64)], YL, 'f', False, False, 2.4), L([(46, 86), (50, 80), (54, 86)], YL, 'f', False, False, 2.0)] + teeth_grin(y=94, w=16, h=8),
  [L(outline([(54, 60), (60, 46), (84, 42), (100, 30, 1), (88, 22), (100, 4, 1), (78, 10), (74, -16, 1), (58, 4), (44, -20, 1), (36, 6), (14, -8, 1), (14, 16),
              (-6, 24, 1), (8, 36), (0, 54, 1), (16, 60), (30, 76), (46, 70)])),
   L(outline([(60, 4), (80, 0), (92, 22), (86, 50, 1), (80, 26)]), LV, 'f'),
   L([(76, 62), (88, 84)], YL, 'f', False, False, 2.4), L(quad((72, 92), (82, 98), (90, 92)), WHITE, 'f', True, False, 0)],
  [L(outline([(10, 74), (8, 40), (-8, 30, 1), (8, 24), (0, 4, 1), (22, 12), (24, -16, 1), (40, 6), (52, -24, 1), (60, 4), (80, -14, 1), (78, 12), (100, 6, 1),
              (90, 26), (108, 34, 1), (92, 44), (90, 74), (50, 80)])),
   L(outline([(30, 8), (46, 0), (54, 14), (42, 40, 1), (38, 20)]), LV, 'f')])

# Scaris Cowler: melena negra azulada larga y desordenada hasta el pecho con un mechón blanco, un parche de vendas
# negras en diagonal sobre el ojo derecho y un ojo rojo; cara seria
WS = _c('#e8e8de')
C('scaris-cowler', 'normal', P('#283740', '#f4e2c8', iris='#c02020', shade='#1c252c', deep='#121618'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=94, hairline=[(6, 66), (16, 48), (30, 40), (46, 44), (60, 38), (76, 44), (94, 66)]),
  dome('front', top=-2, w=48, cy=44, n=7, amp=8, seed=21, long=120, flare=10) +
  [L(outline([(54, -2), (70, 4), (80, 30), (84, 70), (90, 116, 1), (76, 80), (66, 40), (60, 20)]), WS, 'f'),
   L(outline([(30, 58), (84, 82), (82, 90), (28, 66)]), BLACK, 'f'), L([(50, 70), (58, 78)], (110, 110, 110, 255), 'f', False, False, 1.2),
   fr([(18, 46), (34, 40), (40, 70), (36, 96, 1), (28, 70)])],
  dome('side', top=-2, w=48, cy=44, n=7, amp=8, seed=21, long=118, flare=10, fr=48) +
  [L(outline([(40, 4), (56, 4), (40, 60), (30, 112, 1), (28, 60)]), WS, 'f'), L([(56, 64), (92, 70)], BLACK, 'f', False, False, 3)],
  dome('back', top=-2, w=48, cy=44, n=7, amp=8, seed=21, long=120, flare=10, ends=5) +
  [L(outline([(30, 4), (44, 2), (40, 60), (34, 118, 1), (26, 60)]), WS, 'f'), L([(8, 66), (92, 76)], BLACK, 'f', False, False, 3)])

# Scarlett Strands: pelo azul marino con un mechón magenta en el flequillo y dos coletas bajas que caen por delante de los
# hombros; ojos grandes grises y sonrisa
MG = _c('#bc4377')
C('scarlett-strands', 'chica', P('#175081', '#fccfa0', iris='#6a7480', shade='#103a60'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 66), (16, 48), (30, 44), (40, 54), (50, 44), (66, 46), (84, 50), (94, 66)]),
  dome('front', top=0, w=47, cy=46, sb=74) +
  [L(outline([(28, 22), (44, 18), (40, 46), (34, 62, 1), (30, 44)]), MG, 'f'),
   L(outline([(8, 70), (2, 96), (-2, 118, 1), (12, 104), (16, 80)])), L(outline([(92, 70), (98, 96), (102, 118, 1), (88, 104), (84, 80)]))] + lashes(),
  dome('side', top=0, w=47, cy=46, nape=84, fr=48) + [L(outline([(36, 70), (28, 96), (26, 120, 1), (40, 104), (44, 78)]))] + lash_side(),
  dome('back', top=0, w=47, cy=46, nape=86) + [L(outline([(8, 72), (2, 100), (-2, 120, 1), (14, 104), (18, 80)])),
                                                L(outline([(92, 72), (98, 100), (102, 120, 1), (86, 104), (82, 80)]))])

# Seb Rosa: pelo castaño con un pincho alto en punta y alas naranjas a los lados; gafas de carreras rojas sobre la frente;
# rayas negras bajo los ojos, cejas enfadadas y los dientes apretados
OR, RG = _c('#e8a020'), _c('#d83a20')
C('seb-rosa', 'normal', P('#b1743e', '#fccf8d', iris='#c03a1e', shade='#8c5a2e'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, hairline=[(6, 62), (18, 52), (50, 48), (82, 52), (94, 62)]),
  [L(outline([(16, 46), (-8, 64, 1), (4, 44), (2, 36)]), OR), L(outline([(84, 46), (108, 64, 1), (96, 44), (98, 36)]), OR),
   L(outline([(12, 60), (6, 36), (20, 18), (40, 12), (50, -24, 1), (60, 12), (80, 18), (94, 36), (88, 60), (80, 50), (20, 50)])),
   L(outline([(52, -18), (60, 12), (80, 18), (92, 36), (86, 56), (70, 30)]), 'shade', 'b', False)] + goggles('front', y=40, frame=_c('#7a2a1a'), lens=RG) +
  [L([(26, 82), (34, 86)], BLACK, 'f', False, False, 1.6), L([(74, 82), (66, 86)], BLACK, 'f', False, False, 1.6)],
  [L(outline([(30, 42), (4, 30, 1), (16, 50)]), OR),
   L(outline([(54, 60), (60, 46), (84, 44), (92, 30), (76, 12), (56, 8), (50, -22, 1), (40, 8), (18, 14), (4, 34), (6, 60), (22, 70), (40, 68)]))] +
  goggles('side', y=36, frame=_c('#7a2a1a'), lens=RG) + [L([(82, 84), (88, 88)], BLACK, 'f', False, False, 1.6)],
  [L(outline([(16, 46), (-8, 64, 1), (4, 44), (2, 36)]), OR), L(outline([(84, 46), (108, 64, 1), (96, 44), (98, 36)]), OR),
   L(outline([(12, 72), (6, 36), (20, 18), (40, 12), (50, -24, 1), (60, 12), (80, 18), (94, 36), (88, 72), (50, 78)]))] + goggles('back', y=38, frame=_c('#7a2a1a')))

# Sei Lightning: media melena rubia lisa y corta, con un mechón negro que le cae por la sien derecha; ojos azules grandes y
# sonrisa
C('sei-lightning', 'chica', P('#f2d870', '#fadcb4', iris='#3a90c0', shade='#d8b850'),
  F(eyes='big', brows='angry', mouth='smile', mouth_y=92, hairline=[(6, 64), (20, 46), (40, 40), (60, 42), (80, 50), (94, 64)]),
  dome('front', top=0, w=47, cy=46, sb=82) + [L(outline([(14, 40), (24, 30), (24, 70), (22, 100, 1), (12, 70)]), BLACK, 'f')] + lashes(),
  dome('side', top=0, w=47, cy=46, nape=88, fr=48) + lash_side(),
  dome('back', top=0, w=47, cy=46, nape=90) + [L(outline([(84, 40), (92, 46), (90, 86), (84, 90)]), BLACK, 'f', False)])

# Seiji Sato (portero): pelo azul marino de pinchos revueltos y cortos; cara normal y media sonrisa
C('seiji-sato', 'normal', P('#2c2c6a', '#f6c89a', iris='#1e1a1a'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=92, hairline=hl(6, 64, 48, 58, jit=2, seed=31)),
  dome('front', top=-2, w=47, cy=44, n=9, amp=10, seed=31, sb=66),
  dome('side', top=-2, w=47, cy=44, n=9, amp=10, seed=31, nape=86, fr=48),
  dome('back', top=-2, w=47, cy=44, n=9, amp=10, seed=31, nape=86))

# Selwyn Crawler: un pañuelo verde de ladrón con espirales blancas le envuelve la cabeza y se anuda bajo la nariz; antifaz
# negro con los ojos blancos
GN, GD = _c('#4a7a4a'), _c('#365a36')
def _furoshiki(view):
    if view == 'front':
        out = [L(outline([(8, 70), (4, 40), (16, 12), (50, 0), (84, 12), (96, 40), (92, 70), (80, 66), (20, 66)]), GN)]
        out += [L(ell(x, y, 7, 6) + [ell(x, y, 7, 6)[0]], WHITE, 'f', False, False, 1.4) for x, y in ((30, 26), (62, 18), (78, 46), (40, 50))]
        out += [L(outline([(16, 64), (50, 60), (84, 64), (82, 82), (50, 84), (18, 82)]), BLACK, 'f'),
                L(ell(36, 74, 7, 4), WHITE, 'f', False), L(ell(64, 74, 7, 4), WHITE, 'f', False), L(ell(38, 75, 2.4, 2.4), BLACK, 'f', False),
                L(ell(62, 75, 2.4, 2.4), BLACK, 'f', False),
                L(outline([(30, 86), (50, 84), (70, 86), (62, 96), (50, 90), (38, 96)]), GN, 'f')]
        return out
    if view == 'side':
        return [L(outline([(6, 82), (2, 40), (20, 8), (50, 0), (80, 10), (96, 36), (96, 64), (60, 66), (30, 76)]), GN),
                L(ell(40, 30, 8, 7) + [ell(40, 30, 8, 7)[0]], WHITE, 'f', False, False, 1.4),
                L(outline([(56, 64), (94, 62), (94, 82), (58, 80)]), BLACK, 'f'), L(ell(84, 72, 5, 4), WHITE, 'f', False),
                L(outline([(80, 84), (96, 86), (92, 96), (82, 92)]), GN, 'f')]
    return [L(outline([(6, 80), (4, 40), (16, 12), (50, 0), (84, 12), (96, 40), (94, 80), (50, 86)]), GN),
            L(ell(36, 30, 8, 7) + [ell(36, 30, 8, 7)[0]], WHITE, 'f', False, False, 1.4), L(ell(66, 50, 8, 7) + [ell(66, 50, 8, 7)[0]], WHITE, 'f', False, False, 1.4),
            L(outline([(6, 70), (94, 70), (94, 80), (6, 80)]), BLACK, 'f')]
C('selwyn-crawler', 'normal', P('#2a2020', '#c0805a', iris='#141010'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=100, hairline=False),
  _furoshiki('front'), _furoshiki('side'), _furoshiki('back'))

# Seneca Herrmann: melena morada lisa echada a un lado que le tapa el ojo izquierdo y cae larga por ese lado hasta el
# pecho; piel morena, ojo morado con pestañas y sonrisa
C('seneca-herrmann', 'chica', P('#6a3a8a', '#b5835a', iris='#7a4ab0', shade='#502a6a'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=93, hairline=[(6, 64), (16, 48), (30, 44), (50, 40), (70, 44), (84, 52), (94, 64)]),
  dome('front', top=0, w=47, cy=46, sb=80) +
  [fr([(34, 26), (60, 24), (82, 40), (90, 70), (92, 110), (84, 122, 1), (78, 100), (64, 90), (50, 78), (40, 56)])] + lashes(),
  dome('side', top=0, w=47, cy=46, nape=96, fr=48) + [fr([(66, 28), (90, 40), (94, 72), (90, 112), (84, 122, 1), (82, 80)])],
  dome('back', top=0, w=47, cy=46, nape=92) + [L(outline([(10, 60), (6, 100), (12, 122, 1), (22, 96), (24, 70)]))])

# Sepia Bartletti: melena azul larga con mechones que le cruzan la cara y dos rizos rojos enroscados a los lados, como
# tentáculos; ojos grandes enfadados con pestañas
RC = _c('#d83a1a')
def _tent(x, s):
    return L(outline([(x, 82), (x - 14 * s, 86), (x - 22 * s, 98), (x - 18 * s, 110), (x - 8 * s, 108), (x - 12 * s, 100), (x - 8 * s, 94), (x + 2 * s, 94)]), RC, 'f')
C('sepia-bartletti', 'chica', P('#3a60c0', '#f6d8b0', iris='#4a5a8a', shade='#2a4a9a'),
  F(eyes='big', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 64), (18, 44), (30, 40), (50, 36), (70, 40), (82, 44), (94, 64)]),
  dome('front', top=-2, w=48, cy=44, long=104, flare=6) +
  [fr([(40, 30), (52, 28), (58, 56), (54, 90, 1), (50, 60), (44, 50)]), fr([(30, 34), (40, 34), (38, 66, 1), (32, 50)]), _tent(10, 1), _tent(90, -1)] + lashes(),
  dome('side', top=-2, w=48, cy=44, long=104, flare=6, fr=48) + [_tent(36, 1)] + lash_side(),
  dome('back', top=-2, w=48, cy=44, long=104, flare=6) + [_tent(10, 1), _tent(90, -1)])

# Serena Halcyon: melena negra en corte recto (flequillo recto sobre las cejas y los lados rectos hasta el cuello); ojos
# cerrados y una sonrisa fina
C('serena-halcyon', 'chica', P('#2a2a28', '#faddb0', iris='#1e1a1a', shade='#1e1e1c'),
  F(eyes='closed', brows=False, mouth='line', mouth_y=92, hairline=[(6, 66), (14, 62), (30, 62), (50, 62), (70, 62), (86, 62), (94, 66)]),
  [L(outline([(8, 104), (4, 50), (14, 14), (50, 0), (86, 14), (96, 50), (92, 104), (80, 104), (80, 62), (20, 62), (20, 104)])),
   L(blob([(56, 4), (84, 16), (92, 50), (90, 100), (82, 100), (80, 58), (70, 30)], 6), 'shade', 'b', False), L(ell(46, 14, 8, 5), 'light', 'b', False)],
  [L(outline([(80, 62), (88, 44), (82, 14), (50, 0), (18, 10), (4, 40), (4, 104), (52, 104), (54, 66)]))],
  [L(outline([(8, 104), (4, 50), (14, 14), (50, 0), (86, 14), (96, 50), (92, 104), (50, 106)])),
   L(blob([(56, 4), (84, 16), (92, 50), (90, 100), (70, 100), (70, 30)], 6), 'shade', 'b', False)])

# Sett Lightning: pelo amarillo pegado como un casco, con un rayo negro encima y dos puntas a los lados; piel tostada,
# ojos rojos y enfadados, dientes apretados
C('sett-lightning', 'normal', P('#f0d040', '#e8a868', iris='#c02020', shade='#d0b030'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=96, hairline=[(6, 64), (18, 56), (30, 60), (40, 50), (50, 56), (60, 50), (70, 60), (82, 56), (94, 64)]),
  [L(outline([(12, 60), (6, 40), (-14, 36, 1), (10, 30), (24, 12), (50, 4), (76, 12), (90, 30), (114, 36, 1), (94, 40), (88, 60), (80, 52), (20, 52)])),
   L(outline([(40, 8), (62, 8), (54, 22), (66, 22), (44, 48, 1), (50, 30), (38, 30)]), BLACK, 'f')],
  [L(outline([(54, 60), (60, 48), (84, 44), (92, 28), (76, 10), (50, 4), (24, 10), (8, 26), (-10, 40, 1), (6, 46), (8, 62), (24, 70), (40, 66)])),
   L(outline([(54, 8), (72, 12), (64, 24), (74, 26), (52, 46, 1), (58, 30), (48, 28)]), BLACK, 'f')],
  [L(outline([(12, 72), (6, 40), (-14, 36, 1), (10, 30), (24, 12), (50, 4), (76, 12), (90, 30), (114, 36, 1), (94, 40), (88, 72), (50, 78)])),
   L(outline([(40, 8), (62, 8), (54, 22), (66, 22), (44, 48, 1), (50, 30), (38, 30)]), BLACK, 'f')])

# Shah Lott (portero): toda la cabeza es una cebolla blanca con la punta arriba y dos rayas verdes en los mofletes; ojos
# redondos, nariz naranja y boca torcida
ON, OS, OG = _c('#f2ead8'), _c('#d8ccb0'), _c('#a0b040')
C('shah-shallot-lott', 'corpulento', P('#f2ead8', '#f8d0a0', iris='#141010'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=98, hairline=False, nose=(50, 86, 4.4), face_front=face(w=8, chin=108, jaw=4), eye_y=78),
  [L(outline([(2, 80), (4, 46), (24, 18), (44, 8), (50, -10, 1), (56, 8), (76, 18), (96, 46), (98, 80), (90, 66), (70, 58), (50, 56), (30, 58), (10, 66)]), ON),
   L(quad((30, 20), (24, 40), (26, 60)), OS, 'f', False, False, 1.2), L(quad((70, 20), (76, 40), (74, 60)), OS, 'f', False, False, 1.2),
   L(quad((14, 82), (16, 92), (24, 96)), OG, 'f', False, False, 3), L(quad((86, 82), (84, 92), (76, 96)), OG, 'f', False, False, 3),
   L(quad((30, 66), (36, 62), (42, 66)), OG, 'f', False, False, 2.4), L(quad((58, 66), (64, 62), (70, 66)), OG, 'f', False, False, 2.4)],
  [L(outline([(54, 62), (70, 54), (90, 50), (96, 36), (74, 16), (54, 8), (48, -10, 1), (40, 8), (16, 20), (2, 46), (6, 80), (24, 86), (44, 76)]), ON),
   L(quad((36, 16), (24, 40), (28, 70)), OS, 'f', False, False, 1.2), L(quad((82, 82), (84, 92), (78, 96)), OG, 'f', False, False, 3)],
  [L(outline([(2, 80), (4, 46), (24, 18), (44, 8), (50, -10, 1), (56, 8), (76, 18), (96, 46), (98, 80), (70, 92), (30, 92)]), ON),
   L(quad((36, 16), (30, 50), (34, 88)), OS, 'f', False, False, 1.2), L(quad((64, 16), (70, 50), (66, 88)), OS, 'f', False, False, 1.2)])

# Shai Klopps: calvo, con una banda blanca sobre los ojos y en medio un ojo enorme de diana roja y negra; boca seria
RD = _c('#d02a20')
C('shai-klopps', 'normal', P('#d8b890', '#e2c49c', iris='#141010'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, hairline=False),
  skull3('front') + [L(outline([(20, 70, 1), (50, 66), (80, 70, 1), (80, 82, 1), (50, 85), (20, 82, 1)]), _c('#dcdcdc'), 'f'),
                     L(ell(50, 76, 12, 11), BLACK, 'f'), L(ell(50, 76, 9, 8), RD, 'f', False), L(ell(50, 76, 6, 5.4), BLACK, 'f', False)],
  skull3('side') + [L(outline([(48, 66), (92, 64), (94, 82), (50, 84)]), _c('#dcdcdc'), 'f'), L(ell(90, 74, 5, 9), BLACK, 'f'), L(ell(91, 74, 3, 6), RD, 'f', False)],
  skull3('back') + [L(outline([(16, 70, 1), (84, 70, 1), (84, 80, 1), (16, 80, 1)]), _c('#dcdcdc'), 'f')])

# Shaun Asparr: maquillaje de kabuki: un moño negro enorme y redondo encima de la cabeza y dos mechones largos y rectos
# que caen a los lados hasta el pecho; rayas rojas alrededor de los ojos, cara blanca, boca en arco hacia abajo
KR = _c('#c8281e')
C('shaun-asparr', 'delgado', P('#2c2a48', '#faecd8', iris='#3a2a20', shade='#1e1c34'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=98, face_front=face(chin=108), face_side=face_side(chin=6), hairline=[(6, 62), (20, 50), (50, 46), (80, 50), (94, 62)]),
  [L(blob([(2, 30), (10, -12), (50, -24), (90, -12), (98, 30), (80, 50), (20, 50)], 8)),
   L(outline([(6, 50), (20, 46), (22, 80), (20, 116), (12, 120, 1), (8, 90)])), L(outline([(94, 50), (80, 46), (78, 80), (80, 116), (88, 120, 1), (92, 90)])),
   L(blob([(56, -20), (90, -8), (96, 30), (78, 44), (70, 10)], 6), 'shade', 'b', False),
   L(quad((26, 70), (36, 64), (46, 72)), KR, 'f', False, False, 2.2), L(quad((74, 70), (64, 64), (54, 72)), KR, 'f', False, False, 2.2),
   L([(28, 80), (40, 84)], KR, 'f', False, False, 1.6), L([(72, 80), (60, 84)], KR, 'f', False, False, 1.6),
   L(outline([(46, 100), (50, 108, 1), (54, 100)]), KR, 'f', False)],
  [L(blob([(4, 30), (14, -12), (50, -24), (88, -10), (96, 26), (70, 48), (24, 52)], 8)),
   L(outline([(26, 50), (40, 48), (40, 80), (38, 116), (30, 120, 1), (26, 90)])),
   L(quad((72, 70), (80, 64), (88, 72)), KR, 'f', False, False, 2.2)],
  [L(blob([(2, 30), (10, -12), (50, -24), (90, -12), (98, 30), (80, 54), (20, 54)], 8)),
   L(outline([(6, 50), (94, 50), (92, 80), (88, 120, 1), (80, 84), (20, 84), (12, 120, 1), (8, 80)])),
   L(blob([(56, -20), (90, -8), (96, 30), (78, 44), (70, 10)], 6), 'shade', 'b', False)])

# Sheldon Bugg: luchador de sumo: pelo negro peinado en cresta con el moño atrás y una cinta naranja; cara ancha y
# anaranjada, ojos cerrados con fuerza, nariz naranja redonda, perilla negra y boca apretada
OB = _c('#e8902a')
C('sheldon-bugg', 'corpulento', P('#2a2424', '#f6b260', iris='#141010'),
  F(eyes='closed', brows='angry', mouth='frown', mouth_y=96, face_front=face(w=8, chin=106, jaw=4), nose=(50, 84, 5), ear_out=6, eye_y=78,
    hairline=[(6, 60), (20, 56), (36, 50), (50, 40), (64, 50), (80, 56), (94, 60)]),
  [L(outline([(10, 60), (8, 40), (26, 16), (50, -4, 1), (74, 16), (92, 40), (90, 60), (70, 50), (50, 44), (30, 50)])),
   L(outline([(10, 54), (50, 46), (90, 54), (90, 60), (50, 52), (10, 60)]), OB, 'f'),
   L(quad((26, 84), (32, 82), (38, 84)), _c('#e86a3a'), 'f', False, False, 4), L(quad((62, 84), (68, 82), (74, 84)), _c('#e86a3a'), 'f', False, False, 4),
   L(quad((28, 104), (50, 114), (72, 104)), BLACK, 'f', False, False, 3.4)],
  [L(outline([(52, 58), (66, 50), (86, 44), (74, 18), (50, -4, 1), (30, 12), (10, 30), (6, 54), (20, 68), (40, 64)])),
   L(ell(10, 46, 9, 8), 'mid'), L(outline([(10, 54), (90, 46), (90, 52), (10, 60)]), OB, 'f'),
   L(quad((64, 104), (78, 112), (86, 100)), BLACK, 'f', False, False, 3.4)],
  [L(outline([(10, 70), (8, 40), (26, 16), (50, -4, 1), (74, 16), (92, 40), (90, 70), (50, 76)])), L(ell(50, 54, 10, 9), 'mid'),
   L(outline([(10, 56), (90, 56), (90, 62), (10, 62)]), OB, 'f')])

# Sheldon Myrtle (portero): pelo verde peinado hacia atrás con raya; cara larga y pálida, ojos redondos muy abiertos y una
# sonrisa ancha de labios gruesos
C('sheldon-trot-myrtle', 'delgado', P('#2a7a4a', '#ecd8b8', iris='#141010', shade='#1e5a36'),
  F(eyes='round', brows=True, mouth='lips', mouth_y=98, mouth_w=12, face_front=face(chin=110), face_side=face_side(chin=8),
    hairline=[(6, 62), (18, 50), (36, 44), (44, 52), (54, 42), (74, 44), (86, 50), (94, 62)], nose=(50, 88, 3)),
  dome('front', top=0, w=46, cy=44, sb=66) + [L(quad((44, 10), (40, 30), (44, 52)), 'shade', 'f', False, False, 1.4)],
  dome('side', top=0, w=46, cy=44, nape=82, fr=46),
  dome('back', top=0, w=46, cy=44, nape=82))

# Shilo Placidus: pelo azul grisáceo en casco con flequillo de mechones rectos; gafas rojas y ojos morados; boca seria
C('shilo-placidus', 'normal', P('#9aa8c0', '#f6c89a', iris='#9a3a8a', shade='#7a88a0'),
  F(eyes='normal', brows=True, mouth='frown', mouth_y=94, hairline=[(6, 64), (14, 58), (24, 66), (32, 58), (42, 66), (50, 58), (60, 66), (70, 58), (80, 66), (90, 60), (94, 64)]),
  dome('front', top=0, w=47, cy=46, sb=72) + round_specs('front', _c('#d83a2a'), y=77, rx=10, ry=7, w=2.4),
  dome('side', top=0, w=47, cy=46, nape=86, fr=58) + round_specs('side', _c('#d83a2a'), y=77, w=2.4),
  dome('back', top=0, w=47, cy=46, nape=88))

# Shiv Allrie: melena ondulada castaño verdoso, alborotada y abierta en rizos por los lados hasta el cuello; ojos castaños,
# un lunar bajo el ojo y sonrisa
C('shiv-allrie', 'normal', P('#a89a68', '#f8d4a8', iris='#7a4a2a', shade='#86784e'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 66), (14, 50), (26, 56), (34, 44), (46, 60, 1), (52, 44), (64, 52), (78, 46), (88, 56), (94, 66)]),
  dome('front', top=-2, w=48, cy=44, n=9, amp=6, soft=True, seed=41, long=98, flare=12) + [L(ell(42, 84, 1, 1), BLACK, 'f', False)],
  dome('side', top=-2, w=48, cy=44, n=9, amp=6, soft=True, seed=41, long=98, flare=12, fr=52),
  dome('back', top=-2, w=48, cy=44, n=9, amp=6, soft=True, seed=41, long=98, flare=12, ends=5))

# Shortcake Holmes: lleva por sombrero una tarta de nata con fresas encima y ala blanca; pelo negro corto debajo, mofletes
# sonrosados, ojos risueños, gran sonrisa y pajarita roja
CK, CY, ST = _c('#fafaf2'), _c('#f2d27a'), _c('#e02a3a')
def _cake(view):
    if view == 'front':
        return [L(outline([(-2, 54), (102, 54), (100, 62), (0, 62)]), CK),
                L(outline([(14, 54), (14, 14), (86, 14), (86, 54)]), CK), L(outline([(14, 30), (86, 30), (86, 38), (14, 38)]), CY, 'f', False),
                L(blob([(14, 16), (24, 2), (34, 12), (46, 0), (56, 12), (68, 2), (78, 12), (86, 4), (86, 18), (14, 18)], 4), CK),
                L(ell(54, -2, 6, 6), ST)]
    if view == 'side':
        return [L(outline([(-4, 56), (104, 50), (104, 58), (-4, 64)]), CK), L(outline([(10, 56), (12, 14), (88, 12), (88, 52)]), CK),
                L(outline([(12, 30), (88, 28), (88, 36), (12, 38)]), CY, 'f', False), L(ell(50, -2, 6, 6), ST)]
    return [L(outline([(-2, 54), (102, 54), (100, 62), (0, 62)]), CK), L(outline([(14, 54), (14, 14), (86, 14), (86, 54)]), CK),
            L(outline([(14, 30), (86, 30), (86, 38), (14, 38)]), CY, 'f', False), L(ell(46, -2, 6, 6), ST)]
C('shortcake-holmes', 'normal', P('#2a2424', '#f8c890', iris='#2a1e1a'),
  F(eyes='closed', brows=True, mouth='grin', mouth_y=94, hairline=[(6, 64), (20, 62), (50, 62), (80, 62), (94, 64)]),
  [L(outline([(12, 74), (10, 58), (90, 58), (88, 74), (80, 64), (20, 64)]))] + _cake('front') + blush(y=86, dx=24) +
  [L(outline([(38, 106), (50, 110), (62, 106), (62, 116), (50, 112), (38, 116)]), ST, 'f')],
  [L(outline([(10, 74), (8, 58), (60, 58), (52, 72), (30, 76)]))] + _cake('side'),
  [L(outline([(10, 80), (10, 58), (90, 58), (90, 80), (50, 84)]))] + _cake('back'))

# Siarti Tivi: la cabeza es una tele negra con una gorra naranja encima y cascos amarillos; en la pantalla, dos puntos
# blancos y una boca en uve doble
TV, CP, PH = _c('#22222a'), _c('#d86a1e'), _c('#e8b020')
def _tv(view):
    if view == 'front':
        return [L(outline([(10, 104), (10, 46), (90, 46), (90, 104)]), TV, 'f'), L(outline([(2, 64), (12, 60), (12, 90), (2, 86)]), PH, 'f'),
                L(outline([(98, 64), (88, 60), (88, 90), (98, 86)]), PH, 'f'),
                L(blob([(6, 50), (10, 14), (50, -2), (90, 14), (94, 50)], 8), CP, 'f'), L(outline([(4, 46), (96, 46), (102, 54), (0, 54)]), _c('#a84a14'), 'f'),
                L(ell(34, 74, 3, 3), WHITE, 'f', False), L(ell(66, 74, 3, 3), WHITE, 'f', False),
                L([(36, 86), (42, 94), (50, 86), (58, 94), (64, 86)], WHITE, 'f', False, False, 2.6)]
    if view == 'side':
        return [L(outline([(16, 104), (16, 46), (92, 46), (92, 104)]), TV, 'f'), L(outline([(40, 60), (60, 60), (60, 90), (40, 90)]), PH, 'f'),
                L(blob([(8, 50), (14, 14), (50, -2), (86, 14), (92, 50)], 8), CP, 'f'), L(outline([(60, 46), (110, 48), (104, 56), (60, 54)]), _c('#a84a14'), 'f'),
                L(ell(86, 74, 2, 3), WHITE, 'f', False)]
    return [L(outline([(10, 104), (10, 46), (90, 46), (90, 104)]), TV, 'f'), L(outline([(2, 64), (12, 60), (12, 90), (2, 86)]), PH, 'f'),
            L(outline([(98, 64), (88, 60), (88, 90), (98, 86)]), PH, 'f'), L(blob([(6, 50), (10, 14), (50, -2), (90, 14), (94, 50)], 8), CP, 'f')]
C('siarti-tivi', 'normal', P('#2a2424', '#c09060', iris='#141010'),
  F(eyes='none', brows=False, mouth='none', hairline=False, no_head=True, ears=False),
  _tv('front'), _tv('side'), _tv('back'))

# Sid Steppe: pelo negro cortado en plano por arriba, con los lados grises y un rizo gris en la sien; patillas largas en
# punta, cejas negras gruesas y enfadadas, nariz larga y boca seria
GY = _c('#8a8680')
C('sid-steppe', 'delgado', P('#3a322c', '#f6c08c', iris='#141010', shade='#2a2420'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=98, face_front=face(chin=108), face_side=face_side(chin=6, nose=4), nose=(50, 88, 3),
    hairline=[(6, 60), (16, 46), (30, 44), (50, 44), (70, 44), (84, 46), (94, 60)]),
  [L(outline([(12, 60), (10, 30), (6, 8, 1), (50, 0), (94, 8, 1), (90, 30), (88, 60), (80, 48), (20, 48)]), GY),
   L(outline([(8, 8), (50, -2), (92, 8), (90, 30), (78, 46), (22, 46), (10, 30)])),
   L(outline([(18, 50), (22, 50), (24, 90), (20, 96, 1), (16, 70)]), BLACK, 'f'), L(outline([(82, 50), (78, 50), (76, 90), (80, 96, 1), (84, 70)]), BLACK, 'f'),
   L(ell(28, 32, 6, 6) + [ell(28, 32, 6, 6)[0]], GY, 'f', False, False, 2.4)] + thick_brows(y=66, c=BLACK, h=4, tilt=0.35),
  [L(outline([(52, 58), (60, 48), (84, 42), (90, 26), (88, 8, 1), (50, 0), (12, 8, 1), (6, 30), (8, 54), (20, 64), (40, 62)]), GY),
   L(outline([(12, 8), (50, -2), (88, 8), (88, 24), (50, 20), (12, 26)])), L(outline([(56, 54), (62, 54), (64, 90), (60, 96, 1)]), BLACK, 'f')] + side_brow(y=66, c=BLACK, h=4, tilt=0.35),
  [L(outline([(12, 74), (10, 30), (6, 8, 1), (50, 0), (94, 8, 1), (90, 30), (88, 74), (50, 80)]), GY),
   L(outline([(8, 8), (50, -2), (92, 8), (90, 26), (50, 22), (10, 26)]))])

# Sidney Cal: melena larga verde azulado lacia y despeinada que le tapa media cara, con las puntas atadas en cintas rojas;
# ojeras oscuras, nariz larga y boca triste
RB = _c('#c84a40')
def _ends(xs, y):
    return [L(outline([(x - 5, y), (x + 5, y), (x + 5, y + 8), (x - 5, y + 8)]), RB, 'f') for x in xs]
C('sidney-cal', 'delgado', P('#1e5a6a', '#e8c8a0', iris='#141010', shade='#164450'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=98, face_front=face(chin=108), face_side=face_side(chin=6, nose=4), nose=(50, 88, 3),
    hairline=[(6, 62), (18, 44), (36, 38), (50, 36), (64, 40), (82, 44), (94, 62)]),
  dome('front', top=-2, w=48, cy=44, long=108, flare=4) +
  [fr([(44, 30), (60, 26), (64, 60), (60, 100), (54, 104, 1), (56, 70), (50, 50)]), L(ell(64, 78, 6, 5), _c('#6a5a4a'), 'f', False)] + _ends((14, 28, 72, 86), 100),
  dome('side', top=-2, w=48, cy=44, long=108, flare=4, fr=46) + _ends((16, 36), 100),
  dome('back', top=-2, w=48, cy=44, long=108, flare=4, ends=5) + _ends((14, 32, 50, 68, 86), 104))

# Silas Andice (portero): pelo gris oscuro echado a un lado que le tapa el ojo izquierdo, con un mechón blanco, y un moño
# arriba atado con un lazo blanco; ojo rojo y boca seria
C('silas-andice', 'normal', P('#3a3a48', '#f4dcc0', iris='#c02020', shade='#2a2a36'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=94, hairline=[(6, 64), (16, 48), (30, 42), (50, 40), (70, 42), (84, 50), (94, 64)]),
  dome('front', top=0, w=47, cy=46, sb=76) +
  [L(ell(50, -2, 9, 8)), L(outline([(30, -6), (70, -6), (72, 4), (28, 4)]), WHITE, 'f'),
   fr([(14, 40), (40, 26), (70, 30), (80, 52), (60, 70), (36, 92), (20, 110, 1), (28, 84), (20, 60)]),
   L(quad((40, 30), (52, 50), (30, 96)), WHITE, 'f', False, False, 2.4)],
  dome('side', top=0, w=47, cy=46, nape=86, fr=48) + [L(ell(46, -2, 9, 8)), L(outline([(26, -6), (66, -6), (68, 4), (24, 4)]), WHITE, 'f')],
  dome('back', top=0, w=47, cy=46, nape=88) + [L(ell(50, -2, 9, 8)), L(outline([(30, -6), (70, -6), (72, 4), (28, 4)]), WHITE, 'f')])

# Silke Coombe: melena verde oscuro en corte recto con flequillo y un gorro rojo alto de rayas negras encima; ojos
# amarillos y sonrisa
FZ = _c('#b81e1e')
C('silke-coombe', 'chica', P('#1e3a2a', '#f8dcb4', iris='#c8a020', shade='#142a1e'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=[(6, 64), (14, 60), (30, 60), (50, 60), (70, 60), (86, 60), (94, 64)]),
  [L(outline([(6, 100), (4, 50), (14, 16), (50, 6), (86, 16), (96, 50), (94, 100), (82, 100), (82, 60), (18, 60), (18, 100)])),
   L(outline([(20, 18), (18, -12), (82, -12), (80, 18)]), FZ)] + [L([(x, -8), (x, 12)], BLACK, 'f', False, False, 1.4) for x in (30, 40, 50, 60, 70)] + lashes(),
  [L(outline([(78, 60), (86, 44), (80, 16), (50, 6), (18, 12), (4, 40), (4, 100), (50, 102), (52, 66)])), L(outline([(20, 18), (18, -12), (78, -12), (76, 16)]), FZ)] + lash_side(),
  [L(outline([(6, 100), (4, 50), (14, 16), (50, 6), (86, 16), (96, 50), (94, 100), (50, 104)])), L(outline([(20, 18), (18, -12), (82, -12), (80, 18)]), FZ)])

# Silvio Di Fence: pelo granate con un moño alto atado y un mechón largo que le cae por el lado derecho hasta el pecho;
# ojos grandes y cejas enfadadas
C('silvio-di-fence', 'normal', P('#8a2424', '#f8c890', iris='#2a2a3a', shade='#6a1a1a'),
  F(eyes='big', brows='angry', mouth='frown', mouth_y=94, hairline=[(6, 62), (18, 48), (40, 38), (62, 42), (84, 50), (94, 62)]),
  dome('front', top=4, w=47, cy=46, sb=66, sweep=0.5, n=0) +
  [L(ell(50, -2, 10, 9)), L(ell(50, 8, 7, 3), _c('#f2e2d0'), 'f', False),
   fr([(10, 40), (30, 30), (36, 50), (24, 76), (22, 118), (14, 112, 1), (12, 80)])],
  dome('side', top=4, w=47, cy=46, nape=86, fr=48) + [L(ell(44, -2, 10, 9))],
  dome('back', top=4, w=47, cy=46, nape=86) + [L(ell(50, -2, 10, 9)), L(outline([(80, 50), (90, 56), (88, 118), (82, 112, 1), (80, 80)]))])

# Simon Cleric (portero): un gorro alto blanco y beis de obispo con una gema verde; pelo azul claro rizado a los lados y
# un bigote enorme en rizos; la visera le tapa los ojos; boca seria
HT, HB, GM = _c('#fafaf2'), _c('#c8b890'), _c('#2a9a5a')
C('simon-cleric', 'normal', P('#8ab8d8', '#fae2c8', iris='#141010', shade='#6a98b8'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=98, hairline=False),
  [L(outline([(8, 90), (4, 60), (16, 54), (24, 80), (22, 92)])), L(outline([(92, 90), (96, 60), (84, 54), (76, 80), (78, 92)])),
   L(outline([(14, 62), (12, 20), (24, -18), (50, -24), (76, -18), (88, 20), (86, 62)]), HT, 'f'),
   L(outline([(10, 58), (90, 58), (90, 68), (10, 68)]), HB, 'f'), L(outline([(46, -22), (54, -22), (54, 56), (46, 56)]), HB, 'f', False),
   L(outline([(16, 20), (84, 20), (84, 26), (16, 26)]), HB, 'f', False), L(ell(50, 48, 6, 6), GM, 'f'),
   L(outline([(12, 68), (88, 68), (86, 76), (14, 76)]), BLACK, 'f'),
   L(outline([(50, 86), (36, 84), (24, 90), (20, 98), (30, 96), (40, 92), (50, 92), (60, 92), (70, 96), (80, 98), (76, 90), (64, 84)]), 'mid', 'f')],
  [L(outline([(30, 92), (26, 60), (40, 56), (46, 84)])), L(outline([(10, 60), (8, 20), (24, -18), (50, -24), (76, -16), (90, 20), (90, 60)]), HT),
   L(outline([(6, 58), (94, 56), (94, 66), (6, 68)]), HB, 'f'), L(outline([(60, 68), (94, 66), (94, 76), (60, 76)]), BLACK, 'f'),
   L(outline([(86, 86), (96, 88), (100, 98), (88, 94)]), 'mid', 'f')],
  [L(outline([(8, 90), (4, 60), (96, 60), (92, 90), (50, 94)])), L(outline([(14, 60), (12, 20), (24, -18), (50, -24), (76, -18), (88, 20), (86, 60)]), HT),
   L(outline([(10, 58), (90, 58), (90, 68), (10, 68)]), HB, 'f')])

# Singer Long (portero): un tupé naranja altísimo en ola; cejas fruncidas, ojos entornados y los dientes apretados en una
# sonrisa forzada
C('singer-long', 'normal', P('#e88a2a', '#f8c890', iris='#3a2a1a', shade='#c06a1a'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=95, hairline=[(6, 62), (18, 52), (34, 50), (50, 52), (66, 50), (82, 52), (94, 62)]),
  [L(outline([(12, 64), (6, 40), (14, 18), (26, 4), (24, -20), (40, -38), (64, -36), (74, -20), (66, -6), (80, 10), (92, 30), (90, 64), (80, 54), (20, 54)])),
   L(outline([(44, -32), (64, -34), (72, -20), (62, -8), (56, -20)]), 'light', 'b', False),
   L(outline([(60, 0), (82, 12), (92, 34), (88, 60), (76, 30)]), 'shade', 'b', False)],
  [L(outline([(54, 60), (62, 48), (86, 40), (96, 20), (100, -16), (86, -36), (60, -36), (54, -16), (36, -4), (14, 10), (4, 34), (6, 58), (22, 70), (40, 66)])),
   L(outline([(70, -32), (90, -30), (96, -12), (84, -6), (76, -20)]), 'light', 'b', False)],
  [L(outline([(12, 76), (6, 40), (14, 18), (26, 4), (24, -20), (40, -38), (64, -36), (74, -20), (66, -6), (80, 10), (92, 30), (90, 76), (50, 82)]))])

# Sirius Buff: cara ancha y redonda, tostada; pelo rubio anaranjado en pinchos arriba y dos mechones como hojas a los lados;
# gafas redondas pequeñas, ojos cerrados y labios en morro
C('sirius-buff', 'corpulento', P('#f0b02a', '#e8a860', iris='#141010', shade='#c8901e'),
  F(eyes='closed', brows='angry', mouth='lips', mouth_y=98, mouth_w=8, face_front=face(w=8, chin=106, jaw=5), ear_out=8, eye_y=78,
    hairline=[(6, 56), (20, 50), (50, 46), (80, 50), (94, 56)]),
  [L(outline([(16, 52), (14, 36), (22, 18), (20, -2, 1), (34, 10), (46, -12, 1), (54, 8), (68, -4, 1), (72, 14), (86, 22), (84, 52), (50, 46)])),
   L(outline([(6, 84), (-8, 92, 1), (0, 76), (-6, 66, 1), (8, 68), (12, 80)])), L(outline([(94, 84), (108, 92, 1), (100, 76), (106, 66, 1), (92, 68), (88, 80)]))] +
  round_specs('front', _c('#f0e0c0'), y=78, rx=7.5, ry=6, w=1.6),
  [L(outline([(52, 54), (66, 46), (82, 30), (74, 10), (66, -6, 1), (54, 6), (42, -10, 1), (34, 6), (18, 10), (8, 30), (12, 52), (30, 60)])),
   L(outline([(30, 82), (14, 92, 1), (22, 76), (16, 66, 1), (32, 70)]))] + round_specs('side', _c('#f0e0c0'), y=78, w=1.6),
  [L(outline([(14, 60), (14, 36), (22, 18), (20, -2, 1), (34, 10), (46, -12, 1), (54, 8), (68, -4, 1), (72, 14), (86, 22), (86, 60), (50, 64)])),
   L(outline([(6, 84), (-8, 92, 1), (0, 76), (-6, 66, 1), (8, 68), (12, 80)])), L(outline([(94, 84), (108, 92, 1), (100, 76), (106, 66, 1), (92, 68), (88, 80)]))])

# Sita Square: un sombrero azul grisáceo de ala ancha con dos picos como orejas de gato; ojos amarillos afilados y boca
# triste
HG, HE = _c('#5a6a98'), _c('#e8eaf0')
def _cathat(view):
    if view == 'front':
        return [L(outline([(-6, 66), (6, 40), (4, -8, 1), (26, 14), (50, 6), (74, 14), (96, -8, 1), (94, 40), (106, 66), (80, 58), (50, 54), (20, 58)]), HG, 'f'),
                L(outline([(10, 4), (12, 30), (22, 16)]), HE, 'f', False), L(outline([(90, 4), (88, 30), (78, 16)]), HE, 'f', False),
                L(quad((50, 8), (44, 30), (54, 54)), _c('#46547a'), 'f', False, False, 1.2)]
    if view == 'side':
        return [L(outline([(-6, 66), (8, 36), (20, -8, 1), (44, 10), (70, 12), (92, 30), (108, 62), (70, 56), (30, 64)]), HG, 'f'),
                L(outline([(24, 2), (28, 24), (36, 12)]), HE, 'f', False)]
    return [L(outline([(-6, 66), (6, 40), (4, -8, 1), (26, 14), (50, 6), (74, 14), (96, -8, 1), (94, 40), (106, 66), (50, 74)]), HG, 'f')]
C('sita-square', 'chica', P('#5a6a98', '#f8d2a8', iris='#d8b020'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, hairline=False),
  _cathat('front') + lashes(), _cathat('side') + lash_side(), _cathat('back'))

# Slim Pointer: cabeza muy alargada con un gorro azul claro alto, orejas grandes, unas gafas diminutas redondas en la
# frente y una sonrisa enorme de dientes cuadrados; la barbilla, tapada con una mascarilla bajada azul clara
LB = _c('#a8d0e8')
C('slim-pointer', 'delgado', P('#a8d0e8', '#dcbc94', iris='#141010'),
  F(eyes='none', brows=False, mouth='none', hairline=False, face_front=blob([(24, 30), (50, 22), (76, 30), (78, 70), (74, 100), (62, 114), (50, 116), (38, 114), (26, 100), (22, 70)]),
    face_side=face_side(chin=12), big_ears=3),
  [L(outline([(22, 36, 1), (22, -26), (78, -26), (78, 36, 1)]), LB, 'f'), L([(24, -10), (76, -10)], _c('#88b0c8'), 'f', False, False, 1.2),
   L(ell(43, 52, 4.4, 4.4) + [ell(43, 52, 4.4, 4.4)[0]], BLACK, 'f', False, False, 1.4), L(ell(57, 52, 4.4, 4.4) + [ell(57, 52, 4.4, 4.4)[0]], BLACK, 'f', False, False, 1.4),
   L(ell(43, 52, 1.4, 1.4), BLACK, 'f', False), L(ell(57, 52, 1.4, 1.4), BLACK, 'f', False), L([(50, 64), (52, 76), (48, 78)], _c('#a88a68'), 'f', False, False, 1.2),
   L(outline([(30, 82), (70, 82), (66, 98), (50, 102), (34, 98)]), WHITE, 'f')] +
  [L([(x, 82), (x, 100)], BLACK, 'f', False, False, 0.8) for x in (38, 44, 50, 56, 62)] + [L([(32, 90), (68, 90)], BLACK, 'f', False, False, 0.8),
   L(outline([(28, 102), (72, 102), (64, 116), (36, 116)]), LB, 'f')],
  [L(outline([(26, 36, 1), (24, -26), (84, -26), (86, 36, 1)]), LB, 'f'), L(ell(84, 52, 3.4, 4.4) + [ell(84, 52, 3.4, 4.4)[0]], BLACK, 'f', False, False, 1.4),
   L(outline([(74, 82), (92, 84), (90, 98), (74, 100)]), WHITE, 'f'), L(outline([(64, 102), (90, 104), (84, 116), (66, 114)]), LB, 'f')],
  [L(outline([(22, 36, 1), (22, -26), (78, -26), (78, 36, 1)]), LB, 'f'), L(outline([(30, 104), (70, 104), (68, 112), (32, 112)]), LB, 'f')])

# Sloan Steddy: pelo negro corto y rizado, cara redonda morena con los mofletes llenos, ojos pequeños, sonrisa y una
# tirita en la barbilla
C('sloan-steddy', 'corpulento', P('#2a2420', '#d88a4a', iris='#141010'),
  F(eyes='dot', brows='angry', mouth='smile', mouth_y=92, face_front=face(w=8, chin=104, jaw=5), ear_out=7, eye_y=76,
    hairline=[(6, 58), (20, 50), (50, 46), (80, 50), (94, 58)]),
  dome('front', top=6, w=44, cy=46, n=12, amp=4, soft=True, seed=51, sb=56) +
  [L(outline([(42, 100), (58, 100), (58, 106), (42, 106)]), _c('#e8c070'), 'f')],
  dome('side', top=6, w=44, cy=46, n=12, amp=4, soft=True, seed=51, nape=78, fr=50),
  dome('back', top=6, w=44, cy=46, n=12, amp=4, soft=True, seed=51, nape=78))

# Sly Sundice: melena lacia crema hasta los hombros con un mechón verde que le cae sobre el ojo izquierdo; piel morena,
# ojos rojos perfilados de negro, nariz larga y media sonrisa
GL = _c('#2a8a5a')
C('sly-sundice', 'delgado', P('#ece6cc', '#b5835a', iris='#c02020', shade='#cac2a4'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=98, face_front=face(chin=108), face_side=face_side(chin=6, nose=4), nose=(50, 88, 3),
    hairline=[(6, 62), (18, 44), (36, 36), (50, 34), (64, 36), (82, 44), (94, 62)]),
  dome('front', top=-2, w=48, cy=44, long=106, flare=6) +
  [fr([(46, 26), (66, 24), (70, 50), (62, 76), (54, 84, 1), (54, 60), (44, 46)], GL),
   L(quad((24, 72), (34, 68), (44, 74)), BLACK, 'f', False, False, 2.4), L(quad((76, 72), (66, 68), (56, 74)), BLACK, 'f', False, False, 2.4)],
  dome('side', top=-2, w=48, cy=44, long=106, flare=6, fr=46) + [fr([(74, 28), (90, 36), (92, 60), (86, 80, 1), (82, 52)], GL)],
  dome('back', top=-2, w=48, cy=44, long=106, flare=6, ends=5))

# Snap Breakwater: gorro de punto marrón con dos picos como orejas; por debajo le salen mechones naranjas abiertos a los
# lados; ojos grises y sonrisa
BW, BD = _c('#5a3a2c'), _c('#46281e')
C('snap-shutter-breakwater', 'normal', P('#d8783a', '#f8c890', iris='#7a8088', shade='#b85e2a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=93, hairline=[(6, 64), (16, 58), (28, 64), (40, 58), (50, 64), (60, 58), (72, 64), (84, 58), (94, 64)]),
  [L(outline([(10, 66), (-10, 74, 1), (2, 58), (-12, 50, 1), (4, 44), (20, 50)])), L(outline([(90, 66), (110, 74, 1), (98, 58), (112, 50, 1), (96, 44), (80, 50)])),
   L(outline([(8, 60), (6, 30), (0, 6, 1), (20, 16), (50, 10), (80, 16), (100, 6, 1), (94, 30), (92, 60), (50, 56)]), BW, 'f'),
   L(outline([(8, 48), (92, 48), (92, 60), (50, 58), (8, 60)]), BD, 'f')] + [L([(x, 20), (x, 46)], BD, 'f', False, False, 1.2) for x in (24, 38, 50, 62, 76)],
  [L(outline([(30, 66), (14, 78, 1), (24, 60), (10, 52, 1), (30, 48)])),
   L(outline([(6, 62), (4, 30), (14, 6, 1), (40, 12), (70, 14), (92, 30), (94, 56), (50, 58)]), BW, 'f'), L(outline([(6, 50), (94, 46), (94, 58), (6, 62)]), BD, 'f')],
  [L(outline([(10, 66), (-10, 74, 1), (2, 58), (-12, 50, 1), (4, 44), (96, 44), (112, 50, 1), (98, 58), (110, 74, 1), (90, 66), (70, 74), (30, 74)])),
   L(outline([(8, 60), (6, 30), (0, 6, 1), (20, 16), (50, 10), (80, 16), (100, 6, 1), (94, 30), (92, 60), (50, 62)]), BW, 'f'),
   L(outline([(8, 48), (92, 48), (92, 60), (50, 62), (8, 60)]), BD, 'f')])

# Snapper Krabbie (portero): pelo rosa en pinchos hacia arriba y a los lados con un rizo grande que le cae por la frente;
# ojos afilados y cejas enfadadas
C('snapper-krabbie', 'normal', P('#f07a80', '#fadcb4', iris='#141010', shade='#d05a60'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=hl(5, 64, 50, 58, jit=2, seed=61)),
  dome('front', top=-4, w=48, cy=44, n=8, amp=14, seed=61, sb=70) +
  [fr([(40, 20), (62, 16), (70, 34), (60, 50), (52, 66, 1), (52, 46), (60, 36), (48, 30)])],
  dome('side', top=-4, w=48, cy=44, n=8, amp=14, seed=61, nape=86, fr=50) + [fr([(72, 24), (90, 30), (88, 50), (82, 62, 1), (80, 40)])],
  dome('back', top=-4, w=48, cy=44, n=8, amp=14, seed=61, nape=86))

# Snorri Sloth: cara de perezoso: cara redonda clara con una franja gris sobre los ojos, ojos cerrados y boquita pequeña;
# pelo castaño corto como un casquete con un mechón atado con cuentas naranjas encima
SG, SO = _c('#6a6a60'), _c('#e8902a')
C('snorri-sloth', 'corpulento', P('#8a6a4e', '#f2dcc0', iris='#141010', shade='#6a5038'),
  F(eyes='closed', brows=False, mouth='frown', mouth_y=92, face_front=face(w=8, chin=104, jaw=4), ear_out=7, eye_y=78,
    hairline=[(6, 58), (20, 50), (50, 46), (80, 50), (94, 58)]),
  dome('front', top=6, w=46, cy=48, sb=58, shade=False) +
  [L(ell(50, -2, 4, 6)), L(ell(46, 6, 3, 3), SO), L(ell(54, 6, 3, 3), SO),
   L(outline([(12, 74), (30, 68), (50, 74), (70, 68), (88, 74), (86, 86), (70, 82), (50, 86), (30, 82), (14, 86)]), SG, 'f')],
  dome('side', top=6, w=46, cy=48, nape=80, fr=52, shade=False) + [L(ell(46, -2, 4, 6)), L(outline([(56, 72), (92, 70), (92, 82), (58, 84)]), SG, 'f')],
  dome('back', top=6, w=46, cy=48, nape=80, shade=False) + [L(ell(50, -2, 4, 6)), L(ell(46, 6, 3, 3), SO), L(ell(54, 6, 3, 3), SO)])

# Sophie Spencer: melena negra larga y lisa, gris en lo alto de la cabeza, echada a un lado sobre el ojo izquierdo; ojos
# morados y cara seria
GH = _c('#8a8580')
C('sophie-spencer', 'chica', P('#2a2a2c', '#f8dcc4', iris='#8a3aa0', shade='#1e1e20'),
  F(eyes='normal', brows=False, mouth='line', mouth_y=94, hairline=[(6, 64), (16, 46), (30, 40), (50, 38), (70, 42), (84, 50), (94, 64)]),
  dome('front', top=0, w=47, cy=46, long=112, flare=4) +
  [L(blob([(12, 34), (24, 10), (50, 2), (76, 10), (86, 28), (50, 22)], 6), GH, 'b', False),
   fr([(24, 30), (60, 26), (82, 44), (78, 70), (66, 78, 1), (60, 62), (44, 50)])] + lashes(),
  dome('side', top=0, w=47, cy=46, long=112, flare=4, fr=48) + [L(blob([(10, 30), (24, 8), (50, 2), (80, 10), (88, 26), (40, 20)], 6), GH, 'b', False)],
  dome('back', top=0, w=47, cy=46, long=112, flare=4) + [L(blob([(12, 34), (24, 10), (50, 2), (76, 10), (88, 34), (50, 26)], 6), GH, 'b', False)])

# Soren Uphigh: un sombrero ancho granate como un platillo, con una máscara negra abombada que le tapa los ojos y la nariz
# y dos cuernos naranjas a los lados; piel morena y boca seria
SR, SM, SH = _c('#8a2a24'), _c('#3a2a24'), _c('#e88a2a')
def _saucer(view):
    if view == 'front':
        return [L(outline([(-14, 50, 1), (0, 52), (100, 52), (114, 50, 1), (100, 58), (0, 58)]), SH, 'f'),
                L(blob([(-2, 30), (14, 6), (50, -4), (86, 6), (102, 30), (86, 46), (50, 50), (14, 46)], 8), SR, 'f'),
                L(blob([(30, 44), (36, 20), (50, 14), (64, 20), (70, 44), (64, 80), (50, 86), (36, 80)], 8), SM, 'f'),
                L(blob([(40, 78), (60, 78), (58, 88), (42, 88)], 4), _c('#8a8080'), 'f', False)]
    if view == 'side':
        return [L(blob([(-4, 30), (14, 6), (50, -4), (90, 6), (106, 30), (90, 46), (50, 50), (10, 46)], 8), SR, 'f'),
                L(blob([(60, 40), (80, 30), (96, 50), (94, 82), (76, 88), (64, 70)], 8), SM, 'f'), L(outline([(40, 50), (64, 52), (40, 58)]), SH, 'f')]
    return [L(outline([(-14, 50, 1), (0, 52), (100, 52), (114, 50, 1), (100, 58), (0, 58)]), SH, 'f'),
            L(blob([(-2, 30), (14, 6), (50, -4), (86, 6), (102, 30), (86, 46), (50, 50), (14, 46)], 8), SR, 'f')]
C('soren-uphigh', 'normal', P('#2a2020', '#a8704a', iris='#141010'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, hairline=False),
  _saucer('front'), _saucer('side'), _saucer('back') + [L(outline([(10, 70), (12, 54), (88, 54), (90, 70), (50, 76)]))])

# Spacey Flipper (portero): pelo azul grisáceo con dos picos como orejas de gato arriba y las puntas vueltas hacia fuera a
# los lados; cara ancha y pálida, nariz grande, ojos de párpado caído y una mueca de dientes apretados
C('spacey-flipper', 'corpulento', P('#4a6a8a', '#f8deb0', iris='#141010', shade='#3a5470'),
  F(eyes='sharp', brows=True, mouth='grin', mouth_y=98, face_front=face(w=8, chin=108, jaw=5), ear_out=7, nose=(50, 88, 4.4),
    hairline=[(6, 58), (20, 50), (50, 48), (80, 50), (94, 58)]),
  [L(outline([(14, 54), (12, 30), (20, 6, 1), (30, 18), (50, 14), (70, 18), (80, 6, 1), (88, 30), (86, 54), (50, 50)])),
   L(outline([(14, 54), (6, 80), (-8, 90, 1), (6, 92), (18, 84), (22, 60)])), L(outline([(86, 54), (94, 80), (108, 90, 1), (94, 92), (82, 84), (78, 60)]))],
  [L(outline([(52, 54), (66, 46), (84, 40), (86, 20), (74, 4, 1), (60, 16), (40, 12), (16, 18), (6, 40), (6, 70), (-8, 86, 1), (12, 88), (24, 76), (36, 60)]))],
  [L(outline([(14, 66), (12, 30), (20, 6, 1), (30, 18), (50, 14), (70, 18), (80, 6, 1), (88, 30), (86, 66), (50, 70)])),
   L(outline([(14, 60), (6, 84), (-8, 92, 1), (6, 94), (50, 80), (94, 94), (108, 92, 1), (94, 84), (86, 60)]))])

# Spark Volt: pelo amarillo pegado con el borde en zigzag de rayo; cejas negras en espiral, cara ancha tostada, ojos
# claros, boca seria y un tatuaje de omega en la barbilla
C('spark-volt', 'corpulento', P('#f0d830', '#c8885a', iris='#6a90a0', shade='#d8b820'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=90, face_front=face(w=8, chin=108, jaw=6), ear_out=8, eye_y=76,
    hairline=[(6, 60), (16, 52), (22, 60), (30, 52), (50, 56), (70, 52), (78, 60), (84, 52), (94, 60)]),
  [L(outline([(12, 62), (10, 30), (16, 4, 1), (28, 16), (50, 12), (72, 16), (84, 4, 1), (90, 30), (88, 62), (80, 54), (20, 54)])),
   L([(26, 70), (34, 64), (42, 70), (38, 72)], BLACK, 'f', False, False, 3), L([(74, 70), (66, 64), (58, 70), (62, 72)], BLACK, 'f', False, False, 3),
   L([(38, 106), (39, 99), (50, 96), (61, 99), (62, 106)], BLACK, 'f', False, False, 3.0)],
  [L(outline([(54, 58), (64, 48), (86, 44), (90, 24), (80, 6, 1), (66, 16), (40, 12), (16, 18), (6, 40), (8, 62), (22, 72), (40, 66)])),
   L([(76, 70), (84, 64), (90, 70)], BLACK, 'f', False, False, 3)],
  [L(outline([(12, 74), (10, 30), (16, 4, 1), (28, 16), (50, 12), (72, 16), (84, 4, 1), (90, 30), (88, 74), (50, 80)]))])

# Spike Echidna: pelo blanco en pinchos largos y despeinados hacia todos lados; una máscara roja de zorro le tapa la cara
# hasta la nariz, con espirales negras como cejas
FX, FS = _c('#c82a24'), _c('#f2e6e6')
C('spike-echidna', 'normal', P('#f2e6e6', '#d89a6a', iris='#7a8a9a', shade='#d0c0c4'),
  F(eyes='sharp', brows=False, mouth='none', hairline=False),
  dome('front', top=-6, w=50, cy=44, n=11, amp=16, seed=71, long=104, flare=12) +
  [L(outline([(16, 50), (28, 36), (50, 30), (72, 36), (84, 50), (80, 82), (62, 96), (50, 110, 1), (38, 96), (20, 82)]), FX, 'f'),
   L(ell(36, 76, 6, 4), WHITE, 'f', False), L(ell(64, 76, 6, 4), WHITE, 'f', False), L(ell(37, 76, 2.4, 2.8), _c('#4a5a6a'), 'f', False),
   L(ell(63, 76, 2.4, 2.8), _c('#4a5a6a'), 'f', False),
   L([(28, 60), (34, 52), (42, 56), (38, 62)], BLACK, 'f', False, False, 2.4), L([(72, 60), (66, 52), (58, 56), (62, 62)], BLACK, 'f', False, False, 2.4)],
  dome('side', top=-6, w=50, cy=44, n=11, amp=16, seed=71, long=104, flare=12, fr=46) +
  [L(outline([(60, 44), (84, 40), (94, 60), (100, 96, 1), (80, 92), (62, 80)]), FX, 'f'), L(ell(84, 74, 4, 4), WHITE, 'f', False)],
  dome('back', top=-6, w=50, cy=44, n=11, amp=16, seed=71, long=104, flare=12, ends=5))

# Spookie Otherside (portero): melena morada larga con raya en medio que acaba en dos trenzas gruesas; cara larga y
# morena, sombra morada en los párpados y boca torcida
C('spookie-otherside', 'delgado', P('#6a3a7a', '#e0a066', iris='#141010', shade='#502a5c'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=100, face_front=face(chin=110), face_side=face_side(chin=8, nose=3), nose=(50, 88, 3),
    hairline=[(6, 64), (18, 46), (36, 34), (50, 30), (64, 34), (82, 46), (94, 64)]),
  [L(outline([(6, 100), (4, 50), (14, 16), (50, 0), (86, 16), (96, 50), (94, 100), (84, 100), (82, 50), (54, 28), (50, 34), (46, 28), (18, 50), (16, 100)])),
   L(quad((26, 68), (36, 62), (46, 68)), _c('#8a4aa0'), 'f', False, False, 2.6), L(quad((74, 68), (64, 62), (54, 68)), _c('#8a4aa0'), 'f', False, False, 2.6)] +
  [L(ell(x, y, 6, 5), 'mid', 'f') for x in (10, 90) for y in (100, 110, 120)],
  [L(outline([(50, 60), (56, 40), (80, 30), (88, 16), (70, 2), (40, 2), (14, 14), (2, 40), (2, 96), (14, 104), (30, 100), (40, 66)]))] +
  [L(ell(22, y, 6, 5), 'mid', 'f') for y in (104, 114, 124)],
  [L(outline([(6, 100), (4, 50), (14, 16), (50, 0), (86, 16), (96, 50), (94, 100), (50, 104)])), L([(50, 4), (50, 100)], 'shade', 'f', False, False, 1.2)] +
  [L(ell(x, y, 6, 5), 'mid', 'f') for x in (16, 84) for y in (104, 114, 124)])

# Spot Barkley: lleva un gorro de perro crema con las orejas marrones caídas, un parche marrón en un ojo y un mechón
# arriba; asoma pelo negro por debajo; ojos grandes y sonrisa
DC, DB2 = _c('#f2ead0'), _c('#6a4a30')
def _doghat(view):
    if view == 'front':
        return [L(outline([(10, 62), (8, 30), (24, 8), (50, 2), (76, 8), (92, 30), (90, 62), (50, 56)]), DC, 'f'),
                L(outline([(10, 26), (-8, 50), (-6, 62), (8, 60), (18, 40)]), DB2, 'f'), L(outline([(90, 26), (108, 50), (106, 62), (92, 60), (82, 40)]), DB2, 'f'),
                L(ell(64, 32, 9, 7), DB2, 'f', False), L(ell(50, 0, 6, 5), DB2, 'f'), L(ell(50, 44, 4, 3), BLACK, 'f', False),
                L(quad((28, 32), (34, 28), (40, 32)), BLACK, 'f', False, False, 1.2)]
    if view == 'side':
        return [L(outline([(6, 66), (4, 32), (20, 8), (50, 2), (78, 8), (94, 28), (96, 56), (60, 56), (30, 62)]), DC, 'f'),
                L(outline([(40, 20), (28, 50), (32, 64), (44, 60), (50, 34)]), DB2, 'f'), L(ell(50, 0, 6, 5), DB2, 'f'), L(ell(96, 42, 3, 3), BLACK, 'f', False)]
    return [L(outline([(10, 70), (8, 30), (24, 8), (50, 2), (76, 8), (92, 30), (90, 70), (50, 74)]), DC, 'f'),
            L(outline([(10, 26), (-8, 50), (-6, 62), (8, 60), (18, 40)]), DB2, 'f'), L(outline([(90, 26), (108, 50), (106, 62), (92, 60), (82, 40)]), DB2, 'f'),
            L(ell(50, 0, 6, 5), DB2, 'f')]
C('spot-barkley', 'normal', P('#2a2424', '#f2b880', iris='#2a2a3a'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=[(6, 64), (16, 60), (26, 66), (36, 60), (50, 66), (64, 60), (74, 66), (84, 60), (94, 64)]),
  [L(outline([(12, 72), (10, 56), (90, 56), (88, 72), (80, 66), (20, 66)]))] + _doghat('front'),
  [L(outline([(10, 74), (8, 56), (60, 56), (52, 70), (30, 76)]))] + _doghat('side'),
  _doghat('back'))

# Spotter: la cabeza entera es la de un perro blanco con las orejas largas verde oscuro caídas, un parche oscuro en el ojo
# izquierdo, nariz negra y un tupé verde oscuro encima (como su modelo 3D)
DW, DG = _c('#e6e2d6'), _c('#1e3a36')
def _dog(view):
    if view == 'front':
        return [L(blob([(10, 50), (18, 14), (50, 4), (82, 14), (90, 50), (84, 92), (66, 112), (50, 114), (34, 112), (16, 92)], 8), DW, 'f'),
                L(outline([(12, 30), (2, 60), (4, 100), (16, 104), (20, 60), (22, 34)]), DG, 'f'), L(outline([(88, 30), (98, 60), (96, 100), (84, 104), (80, 60), (78, 34)]), DG, 'f'),
                L(outline([(36, 10), (44, -14, 1), (52, 2), (62, -10, 1), (62, 10), (50, 16)]), DG, 'f'),
                L(ell(66, 64, 9, 8), DG, 'f', False), L(ell(34, 66, 5, 4), WHITE, 'f', False), L(ell(66, 66, 5, 4), WHITE, 'f', False),
                L(ell(35, 66, 2, 2.4), BLACK, 'f', False), L(ell(65, 66, 2, 2.4), BLACK, 'f', False),
                L(blob([(42, 84), (58, 84), (54, 94), (46, 94)], 4), BLACK, 'f'), L(quad((36, 102), (50, 98), (64, 102)), BLACK, 'f', False, False, 1.2)]
    if view == 'side':
        return [L(blob([(10, 50), (22, 14), (52, 4), (78, 18), (84, 50), (106, 70), (104, 84), (80, 100), (54, 104), (30, 96), (14, 80)], 8), DW, 'f'),
                L(outline([(40, 40), (52, 36), (56, 70), (52, 100), (40, 104), (36, 70)]), DG, 'f'),
                L(outline([(30, 10), (50, -14, 1), (54, 0), (70, -6, 1), (70, 12), (46, 18)]), DG, 'f'),
                L(ell(78, 62, 3, 4), BLACK, 'f', False), L(ell(104, 76, 4, 4), BLACK, 'f')]
    return [L(blob([(10, 50), (18, 14), (50, 4), (82, 14), (90, 50), (86, 90), (50, 100), (14, 90)], 8), DW, 'f'),
            L(outline([(12, 30), (2, 60), (4, 100), (16, 104), (20, 60), (22, 34)]), DG, 'f'), L(outline([(88, 30), (98, 60), (96, 100), (84, 104), (80, 60), (78, 34)]), DG, 'f'),
            L(outline([(36, 10), (44, -14, 1), (52, 2), (62, -10, 1), (62, 10), (50, 16)]), DG, 'f')]
C('spotter', 'normal', P('#1e3a36', '#d8b090', iris='#141010'),
  F(eyes='none', brows=False, mouth='none', hairline=False, no_head=True, ears=False),
  _dog('front'), _dog('side'), _dog('back'))

# Stace Strikes: pelo verde claro corto en mechones de punta revueltos; ojos turquesa grandes y sonrisa
C('stace-strikes', 'chica', P('#a8d890', '#fadcb4', iris='#2a9ab0', shade='#88b870'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=hl(6, 64, 48, 58, jit=2, seed=81)),
  dome('front', top=0, w=47, cy=46, n=10, amp=7, seed=81, sb=70) + lashes(),
  dome('side', top=0, w=47, cy=46, n=10, amp=7, seed=81, nape=84, fr=50) + lash_side(),
  dome('back', top=0, w=47, cy=46, n=10, amp=7, seed=81, nape=84))

# Stanley Switch: pelo gris en una hoja alta inclinada hacia arriba; gafas negras con los ojos rojos, orejas en punta,
# nariz larga, cara alargada morena y una sonrisa enorme de dientes
C('stanley-switch', 'delgado', P('#9a9a98', '#d8a878', iris='#c02020', shade='#7a7a78'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=98, face_front=face(chin=112), face_side=face_side(chin=8, nose=5), nose=(50, 88, 3),
    hairline=[(6, 64), (16, 50), (34, 50), (50, 56), (66, 50), (84, 50), (94, 64)]),
  ears_pointy('front', h=12) +
  [L(outline([(16, 62), (12, 30), (26, -6), (40, -44, 1), (60, -30), (84, 10), (88, 62), (80, 50), (20, 50)])),
   L(outline([(44, -38), (60, -30), (84, 10), (86, 50), (66, 20)]), 'shade', 'b', False),
   L(outline([(20, 68), (46, 70), (50, 74), (54, 70), (80, 68), (78, 82), (56, 82), (50, 78), (44, 82), (22, 82)]), BLACK, 'f'),
   L(ell(35, 76, 5, 3), _c('#c02020'), 'f', False), L(ell(65, 76, 5, 3), _c('#c02020'), 'f', False)],
  [L(outline([(54, 62), (62, 50), (84, 46), (90, 20), (66, -36, 1), (46, -24), (20, -2), (6, 30), (8, 60), (22, 70), (40, 66)]))] + ears_pointy('side', h=12) +
  [L(outline([(70, 68), (92, 68), (92, 82), (72, 82)]), BLACK, 'f'), L([(70, 72), (50, 66)], BLACK, 'f', False, False, 1.6)],
  [L(outline([(16, 74), (12, 30), (26, -6), (40, -44, 1), (60, -30), (84, 10), (88, 74), (50, 80)])), L([(16, 74), (84, 74)], BLACK, 'f', False, False, 1.6)])

# Stella Thee: una capucha roja entera, como un daruma, le tapa la cabeza y la boca; solo se ven sus ojos grandes y redondos
HR, HRD = _c('#c81e1e'), _c('#a01616')
C('stella-thee', 'chica', P('#c81e1e', '#f8dcb4', iris='#3a3a30'),
  F(eyes='big', brows=False, mouth='none', hairline=False, eye_y=75),
  hood('front', HR, top=-6, low=110, rim='shade', face_hole=[(16, 60), (50, 54), (84, 60), (84, 92), (50, 94), (16, 92)]) +
  [L(outline([(14, 90), (50, 88), (86, 90), (84, 108), (50, 112), (16, 108)]), HR, 'f'), L(ell(36, 26, 8, 6), _c('#e04a4a'), 'f', False)],
  hood('side', HR, top=-6, low=110, rim='shade') + [L(outline([(60, 84), (94, 84), (94, 106), (62, 108)]), HR, 'f')],
  hood('back', HR, top=-6, low=110, rim='shade'))

# Steph Scorer: pelo negro en mechones de punta por la frente y los lados, recogido arriba con un lazo rojo grande; ojos
# castaños grandes con pestañas y sonrisa abierta
RL = _c('#d02a2a')
C('steph-scorer', 'chica', P('#2a2424', '#f8d0a4', iris='#6a4a3a'),
  F(eyes='big', brows=True, mouth='grin', mouth_y=93, hairline=hl(6, 64, 46, 60, jit=2, seed=91)),
  dome('front', top=0, w=48, cy=46, n=8, amp=10, seed=91, long=96, flare=12) +
  [L(ell(50, -2, 7, 6)), L(outline([(50, 2), (24, -8), (18, 4), (30, 10)]), RL, 'f'), L(outline([(50, 2), (76, -8), (82, 4), (70, 10)]), RL, 'f')] + lashes(),
  dome('side', top=0, w=48, cy=46, n=8, amp=10, seed=91, long=96, flare=12, fr=50) + [L(ell(46, -2, 7, 6)), L(outline([(46, 2), (24, -10), (22, 6)]), RL, 'f')] + lash_side(),
  dome('back', top=0, w=48, cy=46, n=8, amp=10, seed=91, long=96, flare=12) +
  [L(ell(50, -2, 7, 6)), L(outline([(50, 2), (24, -8), (18, 4), (30, 10)]), RL, 'f'), L(outline([(50, 2), (76, -8), (82, 4), (70, 10)]), RL, 'f')])

# Strata Pudden: media melena a rayas verde menta y crema con las puntas abiertas hacia fuera; ojos verdes, mofletes
# sonrosados y sonrisa
MN, CRM = _c('#7acca8'), _c('#f0f4e0')
C('strata-pudden', 'chica', P('#7acca8', '#f8c890', iris='#2a9a5a', shade='#5aa888'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, hairline=[(6, 64), (18, 48), (36, 42), (50, 46), (64, 42), (82, 48), (94, 64)]),
  [L(outline([(6, 60), (-4, 84), (4, 92), (20, 86), (22, 62)])), L(outline([(94, 60), (104, 84), (96, 92), (80, 86), (78, 62)]))] +
  dome('front', top=0, w=48, cy=46, sb=74) +
  [L(blob([(10, 30), (30, 14), (70, 14), (90, 30), (86, 38), (50, 26), (14, 38)], 6), CRM, 'f', False),
   L(blob([(4, 60), (20, 58), (16, 70), (2, 72)], 4), CRM, 'f', False), L(blob([(96, 60), (80, 58), (84, 70), (98, 72)], 4), CRM, 'f', False)] + lashes() + blush(y=86, dx=24),
  dome('side', top=0, w=48, cy=46, nape=88, fr=48) + [L(blob([(8, 30), (30, 12), (76, 14), (90, 30), (50, 26)], 6), CRM, 'f', False)] + lash_side(),
  dome('back', top=0, w=48, cy=46, nape=88) + [L(blob([(10, 30), (30, 14), (70, 14), (90, 30), (86, 38), (50, 26), (14, 38)], 6), CRM, 'f', False),
                                                L(blob([(8, 60), (92, 60), (90, 70), (10, 70)], 4), CRM, 'f', False)])

# Stuart Potty: lleva una olla de metal gris del revés en la cabeza, con el asa a un lado, que le tapa los ojos; le asoman
# mechones verdes por los lados; una gran sonrisa
PT, PTD = _c('#aaa8a4'), _c('#7a7874')
C('stuart-potty', 'normal', P('#6a8a3a', '#f8c070', iris='#141010'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=94, hairline=False),
  [L(outline([(10, 70), (-6, 74, 1), (4, 62), (-8, 56, 1), (8, 54)])), L(outline([(90, 70), (106, 74, 1), (96, 62), (108, 56, 1), (92, 54)])),
   L(outline([(4, 76), (6, 40), (10, 14), (50, 6), (90, 14), (94, 40), (96, 76), (50, 82)]), PT, 'f'),
   L(blob([(16, 16), (50, 10), (84, 16), (70, 24), (30, 24)], 6), PTD, 'f', False),
   L(quad((84, 64), (100, 70), (90, 84)), PTD, 'f', False, False, 3)],
  [L(outline([(10, 82), (2, 40), (10, 14), (50, 6), (88, 14), (96, 40), (96, 76), (50, 80)]), PT, 'f'), L(quad((30, 64), (16, 76), (30, 86)), PTD, 'f', False, False, 3)],
  [L(outline([(4, 76), (6, 40), (10, 14), (50, 6), (90, 14), (94, 40), (96, 76), (50, 82)]), PT, 'f'),
   L(outline([(10, 80), (90, 80), (86, 90), (14, 90)]))])

# Summer Salt: pelo verde agua recogido en dos moños de pinchos arriba, con mechones que caen por la cara y una cinta
# amarilla; guiña un ojo, ojo amarillo, mofletes sonrosados y sonrisa
YB = _c('#e8c030')
C('summer-salt', 'chica', P('#4ab4a0', '#f8d0a4', iris='#c8a020', shade='#3a9482'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 64), (18, 50), (34, 48), (50, 52), (66, 48), (82, 50), (94, 64)]),
  dome('front', top=4, w=47, cy=46, sb=80) +
  [L(outline([(12, 22), (2, 2, 1), (14, 6), (14, -14, 1), (26, -2), (34, -12, 1), (36, 8), (24, 24)])),
   L(outline([(88, 22), (98, 2, 1), (86, 6), (86, -14, 1), (74, -2), (66, -12, 1), (64, 8), (76, 24)])),
   L(quad((16, 50), (50, 40), (84, 50)), YB, 'f', False, False, 3), lock(14, 50, 98), lock(86, 50, 98)] + blush(y=86, dx=24),
  dome('side', top=4, w=47, cy=46, nape=86, fr=50) + [L(outline([(44, 16), (36, -6, 1), (48, 0), (54, -14, 1), (62, 4), (56, 20)]))],
  dome('back', top=4, w=47, cy=46, nape=86) + [L(outline([(12, 22), (2, 2, 1), (14, 6), (14, -14, 1), (26, -2), (34, -12, 1), (36, 8), (24, 24)])),
                                               L(outline([(88, 22), (98, 2, 1), (86, 6), (86, -14, 1), (74, -2), (66, -12, 1), (64, 8), (76, 24)]))])

# Sunny Fairweather: pelo naranja como llamas echado hacia atrás, con dos mechones rizados que bajan por los lados hasta la
# barbilla; piel morena, ojos rojos afilados y una sonrisa de dientes
C('sunny-fairweather', 'normal', P('#e8601e', '#b5835a', iris='#c03a1e', shade='#c04a16'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=95, hairline=[(6, 62), (18, 50), (34, 46), (50, 50), (66, 46), (82, 50), (94, 62)]),
  [L(outline([(12, 60), (8, 36), (-8, 22, 1), (12, 18), (16, -4, 1), (32, 10), (46, -14, 1), (54, 6), (70, -8, 1), (72, 12), (90, 6, 1), (88, 24), (106, 26, 1),
              (92, 38), (88, 60), (80, 50), (20, 50)])),
   L(outline([(14, 54), (8, 80), (12, 104), (2, 110, 1), (18, 108), (22, 80), (24, 58)]), 'mid', 'f'),
   L(outline([(86, 54), (92, 80), (88, 104), (98, 110, 1), (82, 108), (78, 80), (76, 58)]), 'mid', 'f')],
  [L(outline([(54, 58), (62, 46), (84, 40), (100, 30, 1), (88, 20), (98, 2, 1), (76, 8), (64, -14, 1), (50, 4), (28, -10, 1), (26, 10), (2, 14, 1), (8, 34), (6, 58), (22, 68), (40, 64)])),
   L(outline([(58, 56), (56, 84), (60, 104), (52, 110, 1), (66, 104), (66, 80), (64, 58)]), 'mid', 'f')],
  [L(outline([(12, 74), (8, 36), (-8, 22, 1), (12, 18), (16, -4, 1), (32, 10), (46, -14, 1), (54, 6), (70, -8, 1), (72, 12), (90, 6, 1), (88, 24), (106, 26, 1),
              (92, 38), (88, 74), (50, 80)])),
   L(outline([(10, 60), (4, 84), (8, 104), (-2, 110, 1), (14, 108), (18, 82)])), L(outline([(90, 60), (96, 84), (92, 104), (102, 110, 1), (86, 108), (82, 82)]))])

# Sylvester Tung (portero): rastas gruesas morado oscuro que le caen por toda la cabeza, le tapan un ojo y llegan al pecho
# por un lado; una cinta verde agua en la frente, un ojo grande y redondo y una gran sonrisa
DP, DPD, MB = _c('#2a2450'), _c('#1e1a3a'), _c('#9ad8c8')
def _dreads(view):
    if view == 'front':
        out = [L(blob([(2, 50), (8, 14), (50, -2), (92, 14), (98, 50), (90, 60), (10, 60)], 8), DP)]
        out += [L(outline([(x - 5, 30), (x + 5, 30), (x + 5, 96 + d), (x, 104 + d, 1), (x - 5, 96 + d)]), DP, 'f') for x, d in ((8, 0), (92, 16), (80, 20), (66, 4))]
        out += [L(quad((16, 52), (40, 46), (60, 50)), MB, 'f', False, False, 3)]
        return out
    if view == 'side':
        return [L(blob([(2, 50), (14, 12), (52, -2), (86, 14), (94, 40), (70, 54), (20, 66)], 8), DP),
                L(outline([(10, 40), (30, 40), (32, 110), (24, 118, 1), (14, 110)]), DP, 'f'), L(outline([(36, 40), (52, 44), (50, 104), (42, 112, 1), (36, 100)]), DP, 'f')]
    return [L(blob([(2, 50), (8, 14), (50, -2), (92, 14), (98, 50), (94, 110), (6, 110)], 8), DP)] + \
        [L([(x, 30), (x, 108)], DPD, 'f', False, False, 1.4) for x in (20, 34, 50, 66, 80)]
C('sylvester-tung', 'normal', P('#2a2450', '#f8d0a4', iris='#3a2a20'),
  F(eyes='round', brows=False, mouth='grin', mouth_y=94, hairline=False),
  _dreads('front'), _dreads('side'), _dreads('back'))

# Sylvia Lagus: pelo lila con flequillo y dos coletas bajas enroscadas en bucle, atadas con gomas turquesa; ojos amarillos
# grandes y sonrisa
TQ = _c('#3ac8b0')
C('sylvia-doe-lagus', 'chica', P('#c8b0c8', '#fadcb8', iris='#c8a020', shade='#a890a8'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(6, 64), (18, 48), (32, 50), (44, 44), (56, 50), (70, 44), (82, 48), (94, 64)]),
  dome('front', top=0, w=47, cy=46, sb=76) +
  [L(ell(4, 78, 9, 12)), L(ell(96, 78, 9, 12)), L(ell(8, 96, 7, 9)), L(ell(92, 96, 7, 9)), L(ell(8, 88, 4, 3), TQ, 'f'), L(ell(92, 88, 4, 3), TQ, 'f')] + lashes(),
  dome('side', top=0, w=47, cy=46, nape=84, fr=48) + [L(ell(28, 80, 9, 12)), L(ell(30, 98, 7, 9)), L(ell(30, 90, 4, 3), TQ, 'f')] + lash_side(),
  dome('back', top=0, w=47, cy=46, nape=86) + [L(ell(8, 78, 9, 12)), L(ell(92, 78, 9, 12)), L(ell(10, 96, 7, 9)), L(ell(90, 96, 7, 9)),
                                                L(ell(10, 88, 4, 3), TQ, 'f'), L(ell(90, 88, 4, 3), TQ, 'f')])

# Taiga West (portera): pelo blanco plateado largo con flequillo de mechones y dos cuernos de carnero amarillos enroscados;
# rayas de tigre negras en los mofletes, ojos amarillos rojizos y una sonrisa con colmillo
HN = _c('#e8b030')
def _horn(cx, s):
    return L(outline([(cx, 30), (cx + 10 * s, 6), (cx + 24 * s, 4), (cx + 30 * s, 16), (cx + 26 * s, 30), (cx + 18 * s, 32), (cx + 20 * s, 18), (cx + 12 * s, 16), (cx + 6 * s, 34)]), HN, 'f')
C('taiga-west', 'chica', P('#e2e6ee', '#fadca8', iris='#d0602a', shade='#c0c6d0'),
  F(eyes='sharp', brows=False, mouth='smile', mouth_y=93, hairline=hl(5, 64, 46, 62, jit=3, seed=101)),
  dome('front', top=0, w=48, cy=46, n=6, amp=6, seed=101, long=106, flare=4) + [_horn(18, -1), _horn(82, 1)] +
  [L([(x0, y), (x1, y + 2)], BLACK, 'f', False, False, 2) for x0, x1, y in ((18, 28, 84), (18, 28, 90), (82, 72, 84), (82, 72, 90))] + lashes(),
  dome('side', top=0, w=48, cy=46, n=6, amp=6, seed=101, long=106, flare=4, fr=52) + [_horn(54, -1)] + [L([(86, 86), (78, 88)], BLACK, 'f', False, False, 2)],
  dome('back', top=0, w=48, cy=46, n=6, amp=6, seed=101, long=106, flare=4) + [_horn(18, -1), _horn(82, 1)])

# Taranis Virga: pelo celeste abultado como una nube, con una cinta azul en la frente y dos mechones azules caídos a los
# lados como orejas; ojos con una cruz y boca seria
CB, BB = _c('#7ad8e8'), _c('#2a60c0')
C('taranis-virga', 'normal', P('#2a60c0', '#f8d4a8', iris='#141010'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=94, hairline=[(6, 62), (20, 58), (50, 58), (80, 58), (94, 62)]),
  [L(outline([(10, 60), (4, 80), (6, 100), (18, 100), (22, 76), (24, 58)])), L(outline([(90, 60), (96, 80), (94, 100), (82, 100), (78, 76), (76, 58)])),
   L(blob([(0, 40), (2, 12), (30, -8), (64, -10), (96, 4), (108, 20), (100, 40), (50, 48)], 8), CB),
   L(blob([(40, -4), (70, -6), (80, 10), (54, 14)], 6), _c('#a8eaf2'), 'b', False),
   L(outline([(8, 44), (50, 40), (92, 44), (92, 58), (50, 56), (8, 58)]), BB, 'f'),
   L([(32, 76), (40, 76)], WHITE, 'f', False, False, 1.4), L([(36, 72), (36, 80)], WHITE, 'f', False, False, 1.4),
   L([(60, 76), (68, 76)], WHITE, 'f', False, False, 1.4), L([(64, 72), (64, 80)], WHITE, 'f', False, False, 1.4)],
  [L(outline([(36, 58), (28, 80), (30, 102), (42, 100), (46, 76), (48, 58)])), L(blob([(-4, 40), (4, 10), (40, -8), (80, -6), (104, 16), (100, 40), (50, 48)], 8), CB),
   L(outline([(4, 44), (94, 42), (94, 56), (6, 58)]), BB, 'f')],
  [L(outline([(10, 60), (4, 80), (6, 100), (18, 100), (22, 76), (78, 76), (82, 100), (94, 100), (96, 80), (90, 60)])),
   L(blob([(0, 40), (2, 12), (30, -8), (64, -10), (96, 4), (108, 20), (100, 40), (50, 48)], 8), CB), L(outline([(8, 44), (92, 44), (92, 58), (8, 58)]), BB, 'f')])

# Tarquin Chatstone (portero): melena larga salmón con mechas granates, peinada hacia atrás y suelta hasta el pecho; piel
# morena, ojos rojos y una sonrisa de dientes
C('tarquin-chatty-chatstone', 'normal', P('#e8907a', '#b5835a', iris='#c02a20', shade='#a83a30', deep='#8a2a24'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=94, hairline=[(6, 62), (18, 46), (32, 40), (50, 44), (68, 40), (82, 46), (94, 62)]),
  dome('front', top=-4, w=48, cy=44, long=116, flare=8) +
  [L(quad((30, 0), (24, 30), (18, 60)), 'deep', 'f', False, False, 3), L(quad((70, 0), (76, 30), (82, 60)), 'deep', 'f', False, False, 3),
   L(quad((50, -2), (46, 20), (42, 40)), 'deep', 'f', False, False, 2.4), lock(12, 60, 116, 'deep', 6), lock(88, 60, 116, 'deep', 6)],
  dome('side', top=-4, w=48, cy=44, long=116, flare=8, fr=44) + [L(quad((70, 4), (40, 20), (10, 60)), 'deep', 'f', False, False, 3)],
  dome('back', top=-4, w=48, cy=44, long=116, flare=8, ends=5) +
  [L(quad((30, 0), (26, 50), (24, 110)), 'deep', 'f', False, False, 3), L(quad((70, 0), (74, 50), (76, 110)), 'deep', 'f', False, False, 3)])

# Tatsuya Okumura: pelo negro revuelto en pinchos con un mechón levantado; piel tostada, cejas marcadas, media sonrisa y un
# pañuelo rojo al cuello
C('tatsuya-okumura', 'normal', P('#2c2a2a', '#d8a070', iris='#141010'),
  F(eyes='normal', brows='angry', mouth='smile', mouth_y=92, hairline=hl(6, 64, 48, 58, jit=2, seed=111)),
  dome('front', top=-4, w=48, cy=44, n=9, amp=11, seed=111, sb=68) + scarf('front', _c('#c8281e')),
  dome('side', top=-4, w=48, cy=44, n=9, amp=11, seed=111, nape=86, fr=50) + scarf('side', _c('#c8281e')),
  dome('back', top=-4, w=48, cy=44, n=9, amp=11, seed=111, nape=86) + scarf('back', _c('#c8281e')))
