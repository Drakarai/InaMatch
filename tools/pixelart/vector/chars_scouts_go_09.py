"""Ojeadores de GO (scouts-go), tanda 09: dibujados a partir de su retrato de Victory Road; claves 'scouts-go:<id>'.

Ninguno de la tanda tiene modelo 3D propio: el frente sale del retrato y el perfil y la espalda se deducen de cómo cae ese
peinado. El sexo (para el cuerpo) es el de la ficha de la wiki. Ayudas: las de las tandas de IE (dome/hl/face de ie1_09,
cap/band de ie3_06, hood/ring/skull3 de ie3_02, crop/brows de chars_vr_nikogawa...) y unas pocas propias abajo."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401
from chars_scouts_ie1_09 import BLACK, WHITE, F, P, _c, dome, face, face_side, hl, mark  # noqa: F401
from chars_scouts_ie3_06 import arc, band, bush, cap  # noqa: F401
from chars_scouts_ie3_02 import hood, ring, skull3  # noqa: F401
from chars_scouts_ie2_04 import sharp_eye_side, sharp_eyes  # noqa: F401
from chars_scouts_ie1_10 import nose_tri  # noqa: F401
from chars_vr_nikogawa import brow_side, brows, crop, ring_glasses  # noqa: F401


def C(pid, body, palette, f, front, side, back):
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        # el nacimiento del pelo baja por el borde de la cara: así su raya no cruza el pelo de los lados
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[f'scouts-go:{pid}'] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def tuft(x, y, tx, ty, c='mid', w=7, z='f'):
    """Mechón o cuerno en punta de (x, y) a (tx, ty)."""
    return L(outline([(x - w, y + 3), (tx, ty, 1), (x + w, y)]), c, z)


def dots_eyes(view, ey=75, sep=14, r=4.6, c=BLACK):
    """Ojos en círculo negro con brillo (capas de delante, para encima de máscaras)."""
    if view == 'front':
        out = []
        for cx in (50 - sep, 50 + sep):
            out += [L(ell(cx, ey, r, r * 1.1), c, 'f', False), L(ell(cx - 1.2, ey - 1.4, r * 0.32, r * 0.32), WHITE, 'f', False)]
        return out
    return [L(ell(82, ey, r * 0.8, r * 1.1), c, 'f', False)]


def eye_side_n(iris='iris', ey=75):
    """Ojo de perfil redondo (para los que llevan los ojos de frente dibujados a mano)."""
    return [L(ell(81.5, ey, 4.4, 6.2), WHITE, 'f', False), L(ell(83.2, ey + 1, 3.2, 4.8), iris, 'f', False),
            L(quad((76, ey - 3), (81, ey - 7.5), (86.6, ey - 4)), OUTC, 'f', False, False, 2.4)]


def tongue(y=96, c=(220, 90, 110, 255)):
    return L(blob([(46, y - 1), (54, y - 1), (55, y + 5), (50, y + 8), (45, y + 5)], 4), c, 'f', True)


# ------------------------------------------------------------------ jugadores (sheet 0)

# Tawny Screech: capucha de búho morada con dos penachos de plumas; antifaz morado en uve sobre los ojos, que son dos aros
# verdes con el centro blanco; plumas moradas a los lados y una mancha morada en la barbilla; piel tostada
OWL, GRN = _c('#793465'), _c('#9ad070')
def _owl(view):
    if view == 'front':
        return [L(outline([(10, 92), (2, 66), (4, 40), (12, 20), (8, -12, 1), (30, 10), (50, 6), (70, 10), (92, -12, 1), (88, 20), (96, 40), (98, 66), (90, 92),
                           (82, 66), (82, 50), (18, 50), (18, 66)]), OWL),
                L(outline([(18, 56), (50, 52), (82, 56), (84, 68), (72, 82), (56, 82), (50, 90, 1), (44, 82), (28, 82), (16, 68)]), OWL, 'f'),
                L(ell(36, 72, 7.5, 7), GRN, 'f', True), L(ell(64, 72, 7.5, 7), GRN, 'f', True),
                L(ell(36, 72, 4.6, 4.2), WHITE, 'f', False), L(ell(64, 72, 4.6, 4.2), WHITE, 'f', False),
                L(outline([(36, 98), (42, 94), (50, 97), (58, 94), (64, 98), (56, 104), (44, 104)]), OWL, 'f')]
    if view == 'side':
        return [L(outline([(70, 62), (78, 52), (88, 46), (86, 24), (72, 8), (66, -14, 1), (52, 4), (30, 4), (10, 18), (2, 46), (4, 80), (14, 96, 1), (28, 84),
                           (44, 66), (58, 58)]), OWL),
                L(outline([(66, 60), (90, 56), (92, 72), (84, 84), (68, 80)]), OWL, 'f'), L(ell(82, 70, 4.6, 6), GRN, 'f', True),
                L(ell(83, 70, 2.6, 3.6), WHITE, 'f', False), L(outline([(76, 98), (88, 96), (86, 104), (78, 104)]), OWL, 'f')]
    return [L(outline([(10, 96, 1), (4, 66), (6, 40), (14, 20), (10, -12, 1), (32, 10), (50, 6), (68, 10), (90, -12, 1), (86, 20), (94, 40), (96, 66), (90, 96, 1),
                       (70, 86), (50, 92), (30, 86)]), OWL),
            L(blob([(58, 10), (86, 24), (94, 60), (88, 90), (66, 82), (66, 40)], 6), 'shade', 'f', False)]
C('tawny-screech', 'normal', P('#793465', '#c9976a'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=92, hairline=False),
  _owl('front'), _owl('side'), _owl('back'))

# Ted HB Ledd: pelo verde en bloque muy alto y plano por arriba (como un lápiz), con los lados cortos; perilla negra en
# punta; ojos redondos y cejas negras gruesas fruncidas
C('ted-hb-ledd', 'normal', P('#5b8b5e', '#fbd08d'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=90, hairline=[(8, 62), (18, 56), (24, 44), (40, 52), (50, 46), (60, 52), (76, 44), (82, 56), (92, 62)]),
  [L(outline([(17, 66), (14, 40), (20, -16), (34, -22), (66, -22), (80, -16), (86, 40), (83, 66), (80, 50), (20, 50)])),
   L(outline([(60, -20), (78, -16), (86, 40), (84, 62), (72, 30)]), 'shade', 'b', False),
   L(outline([(42, 93), (50, 91), (58, 93), (54, 99), (50, 106, 1), (46, 99)]), BLACK, 'f', False)],
  [L(outline([(68, 50), (84, 40), (86, -14), (74, -22), (34, -22), (16, -14), (6, 20), (4, 54), (16, 80), (32, 82), (40, 62), (54, 52)])),
   L(outline([(5, 40), (30, 44), (38, 62), (32, 80), (16, 80)]), 'shade', 'b', False),
   L(outline([(80, 94), (88, 92), (86, 100), (80, 106, 1)]), BLACK, 'f', False)],
  [L(outline([(17, 76), (14, 40), (20, -16), (34, -22), (66, -22), (80, -16), (86, 40), (83, 76), (66, 84), (50, 86), (34, 84)])),
   L(outline([(58, -20), (80, -14), (86, 40), (83, 74), (66, 82), (64, 30)]), 'shade', 'b', False)])

# Teo Chaspet: melena castaña oscura en casco, con el flequillo echado a su izquierda en mechones de punta y las patillas
# largas y afiladas hasta la mandíbula; ojos castaños afilados
C('teo-chaspet', 'normal', P('#615549', '#f6d6aa', iris='#5a3e2a'),
  F(eyes='sharp', brows=True, mouth='line', mouth_y=92, hairline=[(8, 66), (18, 50), (28, 62), (34, 46), (46, 58), (52, 44), (64, 54), (72, 42), (86, 52), (92, 66)]),
  dome('front', top=0, w=48, cy=46, sb=94, sweep=0.6) +
  [L(outline([(84, 46), (100, 40, 1), (92, 56)]), 'mid', 'b')],
  dome('side', top=0, w=48, cy=46, nape=90, fr=50),
  dome('back', top=0, w=48, cy=46, nape=90))

# Tex Tuber: un gorro verde menta en forma de matraz (bulbo redondo con un cuello largo arriba); orejas grandes y en punta,
# gafas redondas amarillas, nariz gorda y boca pequeña con los dientes
MINT, YEL = _c('#8ac49f'), _c('#f0c830')
def _flask(view):
    x = 50 if view != 'side' else 46
    return [L(outline([(x - 44, 58), (x - 42, 36), (x - 26, 20), (x - 8, 14), (x - 8, -10), (x - 12, -22), (x, -26), (x + 12, -22), (x + 8, -10), (x + 8, 14),
                       (x + 26, 20), (x + 42, 36), (x + 44, 58), (x, 54)]), MINT),
            L(outline([(x + 4, -22), (x + 12, -22), (x + 8, -10), (x + 8, 14), (x + 30, 22), (x + 42, 40), (x + 42, 56), (x + 20, 40), (x + 6, 20)]), _c('#6aa482'), 'b', False)]
C('tex-tuber', 'bajito', P('#8ac49f', '#fad197', nose='#ca9568'),
  F(eyes='round', brows=False, mouth='grin', mouth_y=92, hairline=False, big_ears=3, ear_out=4, nose=(50, 84, 4.6)),
  _flask('front') +
  [L(ell(35, 75, 9, 8) + [ell(35, 75, 9, 8)[0]], YEL, 'f', False, False, 2.6), L(ell(65, 75, 9, 8) + [ell(65, 75, 9, 8)[0]], YEL, 'f', False, False, 2.6),
   L([(44, 74), (56, 74)], YEL, 'f', False, False, 2.0)] +
  [L(outline([(10, 60), (-6, 54, 1), (12, 74)]), 'skin', 'b'), L(outline([(90, 60), (106, 54, 1), (88, 74)]), 'skin', 'b')],
  _flask('side') + [L(ell(82, 75, 5, 8) + [ell(82, 75, 5, 8)[0]], YEL, 'f', False, False, 2.6), L([(77, 74), (52, 70)], YEL, 'f', False, False, 2.0)],
  _flask('back') + [L(outline([(10, 60), (-6, 54, 1), (12, 74)]), 'skin', 'f'), L(outline([(90, 60), (106, 54, 1), (88, 74)]), 'skin', 'f')])

# Tez Beyan: pelo rubio ceniza corto en pinchos de punta hacia arriba; una tirita grande en la nariz, ojos afilados y
# ceño muy fruncido, boca apretada; mandíbula ancha
BAND = _c('#c8a882')
C('tez-beyan', 'corpulento', P('#c7a978', '#fdcf9f', iris='#4a6a8a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=94, face_front=face(w=4, chin=102, jaw=3), face_side=face_side(chin=2, jaw=4),
    hairline=[(8, 62), (18, 50), (34, 44), (50, 42), (66, 44), (82, 50), (92, 62)]),
  dome('front', top=-2, w=46, cy=44, n=7, amp=12, seed=21, sb=62) +
  [L(outline([(36, 82), (64, 82), (64, 90), (36, 90)]), BAND, 'f', True)],
  dome('side', top=-2, w=46, cy=44, n=7, amp=12, seed=21, nape=82, fr=46) + [L(outline([(80, 82), (90, 82), (90, 90), (80, 90)]), BAND, 'f', True)],
  dome('back', top=-2, w=46, cy=44, n=7, amp=12, seed=21, nape=82))

# Theo Therr: pelo azul pizarra a media melena, con las puntas de los lados abiertas hacia fuera a la altura de las orejas
# y mechones de punta que le caen entre los ojos; ojos en espiral rosa oscuro
C('theo-therr', 'normal', P('#5a6d8e', '#f6d7b8', iris='#a04a7a'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=92, hairline=[(8, 70), (16, 52), (28, 66), (36, 50), (46, 70), (52, 50), (60, 64), (70, 50), (84, 60), (92, 70)]),
  dome('front', top=0, w=48, cy=46, long=88, flare=12) +
  [L(outline([(6, 76), (-8, 96, 1), (14, 90)]), 'mid', 'b'), L(outline([(94, 76), (108, 96, 1), (86, 90)]), 'mid', 'b'),
   L([(32, 75), (36, 72), (40, 75), (36, 78)], OUTC, 'f', False, False, 0.9), L([(60, 75), (64, 72), (68, 75), (64, 78)], OUTC, 'f', False, False, 0.9)],
  dome('side', top=0, w=48, cy=46, long=88, flare=10, fr=56),
  dome('back', top=0, w=48, cy=46, long=88, flare=12, ends=5))

# Tia Towell: pañuelo blanco atado sobre la cabeza que le tapa el pelo; asoma el flequillo rojo granate redondeado; ojos
# verdes en espiral con pestañas y boquita
TOW = _c('#f2eeea')
def _towel(view):
    if view == 'front':
        return [L(outline([(4, 70), (6, 40), (20, 14), (50, 4), (80, 14), (94, 40), (96, 70), (84, 60), (80, 44), (50, 38), (20, 44), (16, 60)]), TOW),
                L(outline([(70, 10), (90, 28), (96, 60), (88, 50), (82, 34)]), _c('#d4ccc8'), 'b', False)]
    if view == 'side':
        return [L(outline([(80, 50), (88, 38), (80, 16), (56, 4), (28, 6), (8, 22), (0, 50), (6, 76), (20, 80), (30, 60), (50, 50)]), TOW),
                L(outline([(4, 60), (-6, 72, 1), (10, 74)]), TOW)]
    return [L(outline([(4, 76), (6, 40), (20, 14), (50, 4), (80, 14), (94, 40), (96, 76), (70, 84), (50, 86), (30, 84)]), TOW),
            L(outline([(42, 80), (36, 96, 1), (50, 88), (64, 96, 1), (58, 80)]), TOW)]
C('tia-towell', 'chica', P('#8c233b', '#fabb7c', iris='#4a9a5a'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=[(8, 64), (18, 54), (32, 48), (50, 46), (68, 48), (82, 54), (92, 64)]),
  [L(outline([(16, 66), (18, 50), (30, 42), (50, 40), (70, 42), (82, 50), (84, 66), (76, 58), (24, 58)]))] + _towel('front'),
  [L(outline([(70, 50), (84, 44), (82, 60), (66, 56)]))] + _towel('side'),
  _towel('back'))

# Tish Badum (portera): una melena enorme verde azulado en ondas gruesas que le llega a los hombros, con un flequillo en
# pico; cejas pintadas azules gruesas, ojos afilados, sonrisa enorme con todos los dientes; cara ancha
TEAL = _c('#0c454e')
C('tish-badum', 'chica', P('#09687b', '#eaa765', iris='#1e1a1a'),
  F(eyes='sharp', brows=False, mouth='grin', mouth_y=94, face_front=face(w=4, chin=102, jaw=2),
    hairline=[(8, 64), (18, 52), (32, 46), (44, 50), (50, 60), (56, 50), (68, 46), (82, 52), (92, 64)]),
  bush('front', top=-4, w=52, cy=46, n=10, amp=8, seed=31, long=104, flare=14) +
  [L(outline([(24, 64), (42, 62), (40, 66), (26, 69)]), TEAL, 'f', False), L(outline([(76, 64), (58, 62), (60, 66), (74, 69)]), TEAL, 'f', False),
   L(outline([(40, 94), (60, 94), (58, 100), (42, 100)]), WHITE, 'f', True)],
  bush('side', top=-4, w=50, cy=46, n=10, amp=8, seed=31, long=104, flare=12, fr=52) + [L(outline([(72, 64), (86, 63), (84, 67), (72, 68)]), TEAL, 'f', False)],
  bush('back', top=-4, w=52, cy=46, n=10, amp=8, seed=31, long=106, flare=14, ends=6))

# ------------------------------------------------------------------ (sheet 1)

# Toadie Fawner Fauna: pelo azul marino peinado hacia atrás y pegado, con un rizo largo que sale de la coronilla; dos
# espirales azules pintadas en la frente; orejas de punta, cara larga, ojos entornados y sonrisa enorme
NAVY = _c('#435481')
C('toadie-fawner-fauna', 'delgado', P('#435481', '#fbcfa0', iris='#6a3a2a'),
  F(eyes='closed', brows=False, mouth='smile', mouth_y=94, mouth_w=12, face_front=face(chin=108, top=2), face_side=face_side(chin=7),
    hairline=[(8, 54), (18, 40), (34, 32), (50, 30), (66, 32), (82, 40), (92, 54)]),
  crop('front', top=0, side=50) + [L(quad((52, 4), (40, -22), (20, -24)), 'mid', 'f', False, False, 3.4)] +
  [L(quad((42, 50), (36, 42), (44, 40)) + quad((44, 40), (48, 46), (42, 48))[1:], NAVY, 'f', False, False, 1.8),
   L(quad((58, 50), (64, 42), (56, 40)) + quad((56, 40), (52, 46), (58, 48))[1:], NAVY, 'f', False, False, 1.8),
   L(quad((38, 74), (36, 71), (44, 71)), OUTC, 'f', False, False, 2.2), L(quad((56, 71), (64, 71), (62, 74)), OUTC, 'f', False, False, 2.2),
   L(quad((36, 92), (50, 104), (64, 92)) + [(50, 96)], WHITE, 'f', True)] +
  [L(outline([(16, 64), (2, 52, 1), (14, 78)]), 'skin', 'b'), L(outline([(84, 64), (98, 52, 1), (86, 78)]), 'skin', 'b')],
  crop('side', top=0) + [L(quad((40, 4), (30, -20), (10, -24)), 'mid', 'f', False, False, 3.4)],
  crop('back', top=0) + [L(quad((48, 4), (40, -22), (20, -24)), 'mid', 'f', False, False, 3.4),
                         L(outline([(16, 64), (2, 52, 1), (14, 78)]), 'skin', 'f'), L(outline([(84, 64), (98, 52, 1), (86, 78)]), 'skin', 'f')])

# Toasty Tryadd: cabeza casi calva con un solo mechón naranja en llama en lo alto; orejas enormes, ojos redondos muy
# abiertos, ceño y una sonrisa de dientes apretados con baba
C('toasty-tryadd', 'bajito', P('#c5411f', '#fabb7b'),
  F(eyes='round', brows='angry', mouth='grin', mouth_y=93, hairline=False, big_ears=4, ear_out=3),
  [L(outline([(36, 34), (40, 14), (50, -6), (56, -20, 1), (58, -2), (64, 14), (62, 34), (50, 30)])),
   L(outline([(52, -4), (60, 8), (62, 30), (54, 22)]), 'shade', 'b', False),
   L(outline([(54, 96), (58, 96), (57, 102), (55, 102)]), WHITE, 'f', True)],
  [L(outline([(40, 26), (48, 6), (58, -10), (66, -22, 1), (64, -4), (68, 12), (64, 30)]))],
  [L(outline([(36, 34), (40, 14), (50, -6), (56, -20, 1), (58, -2), (64, 14), (62, 34), (50, 30)]))])

# Tom-Tom Thrasher: pelo carmesí en mechones largos de punta revueltos hacia todos lados, que bajan por los lados de la
# cara; piel pálida amarillenta, sombra morada en los ojos, labios morados y la lengua fuera
PUR = _c('#7a5aa0')
C('tom-tom-thrasher', 'normal', P('#a31740', '#f7f1cc', iris='#4a2a4a', lip='#6a3a6a'),
  F(eyes='sharp', brows=False, mouth='none', hairline=[(8, 66), (16, 50), (26, 62), (34, 44), (44, 56), (52, 40), (62, 54), (70, 42), (84, 56), (92, 66)]),
  dome('front', top=-6, w=50, cy=44, n=9, amp=16, seed=41, long=96, flare=10) +
  [L(blob([(26, 70), (44, 70), (44, 80), (28, 80)], 4), PUR, 'b', False), L(blob([(56, 70), (74, 70), (72, 80), (56, 80)], 4), PUR, 'b', False),
   L(quad((40, 92), (50, 100), (60, 92)) + quad((60, 92), (50, 90), (40, 92))[1:], 'lip', 'f', True), tongue(96)],
  dome('side', top=-6, w=50, cy=44, n=9, amp=16, seed=41, long=94, flare=8, fr=52) + [L(ell(84, 94, 3.6, 2.6), 'lip', 'f', True)],
  dome('back', top=-6, w=50, cy=44, n=9, amp=16, seed=41, long=98, flare=10, ends=5))

# Tommie Loveapple: gorro de tomate rojo, redondo y grande, con las hojas verdes encima; flequillo rubio recto; ojos
# grandes castaños y boca en o
TOM, LEAF = _c('#d75034'), _c('#3a8a3a')
def _tomato(view):
    x = 50 if view != 'side' else 46
    out = [L(outline([(x - 46, 64), (x - 50, 36), (x - 36, 12), (x - 14, 2), (x, 4), (x + 14, 2), (x + 36, 12), (x + 50, 36), (x + 46, 64), (x + 30, 56),
                      (x, 54), (x - 30, 56)]), TOM),
           L(outline([(x + 10, 6), (x + 36, 14), (x + 48, 38), (x + 44, 60), (x + 30, 30)]), _c('#b03a24'), 'b', False)]
    out += [L(outline([(x - 2, 4), (x - 22, -4, 1), (x - 6, -2), (x - 12, -14, 1), (x, -6), (x + 10, -16, 1), (x + 6, -2), (x + 22, -6, 1), (x + 4, 6)]), LEAF, 'f')]
    return out
C('tommie-loveapple', 'chica', P('#f4ee74', '#f5eecd', iris='#7a4a1e'),
  F(eyes='big', brows=False, mouth='none', hairline=[(8, 62), (18, 60), (50, 60), (82, 60), (92, 62)]),
  [L(outline([(14, 70), (16, 52), (84, 52), (86, 70), (50, 66)]))] + _tomato('front') + [L(ell(50, 93, 2.2, 2.6), (120, 50, 40, 255), 'f', True)],
  _tomato('side'),
  _tomato('back'))

# Tommy Wobbal (portero): lados rapados grises y arriba unas rastas castaño oscuro retorcidas que salen disparadas hacia
# arriba y a los lados; piel morena, ojos afilados y boca seria
DRD = _c('#352b24')
def _dreads(view):
    tips = [(18, -14), (34, -26), (52, -28), (68, -20), (90, -6), (100, 10)] if view != 'side' else [(20, -20), (40, -28), (60, -24), (84, -10)]
    base = (50, 22) if view != 'side' else (46, 20)
    out = []
    for i, (tx, ty) in enumerate(tips):
        bx = base[0] - 18 + 36 * i / max(1, len(tips) - 1)
        mx, my = (bx + tx) / 2 + (3 if i % 2 else -3), (base[1] + ty) / 2
        out.append(L(outline([(bx - 3.4, base[1]), (mx - 3, my), (tx, ty, 1), (mx + 3, my), (bx + 3.4, base[1])]), DRD, 'f'))
    return out
C('tommy-wobbal', 'normal', P('#5a5450', '#bd8d6a', iris='#2a2020'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=[(8, 62), (18, 50), (34, 44), (50, 42), (66, 44), (82, 50), (92, 62)]),
  crop('front', top=4, side=60) + [L(outline([(28, 28), (36, 12), (50, 8), (64, 12), (72, 28), (50, 26)]), DRD, 'f')] + _dreads('front'),
  crop('side', top=4) + [L(outline([(24, 24), (36, 8), (56, 6), (70, 16), (60, 26)]), DRD, 'f')] + _dreads('side'),
  crop('back', top=4) + [L(outline([(28, 28), (36, 12), (50, 8), (64, 12), (72, 28), (50, 32)]), DRD, 'f')] + _dreads('back'))

# Tortus Northe: una melena gris oscuro que le enmarca la cara y baja hasta la barbilla (como un caparazón), con un
# flequillo rubio en mechones gordos de punta por encima; piel tostada, ojos rojos con el blanco verdoso y ceño
GRAY = _c('#585352')
C('tortus-northe', 'normal', P('#f4c858', '#be8e62', iris='#c8302a', shade='#d8a838'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=[(8, 64), (16, 56), (26, 70), (32, 52), (44, 64), (50, 50), (58, 62), (68, 50), (76, 68), (84, 54), (92, 64)]),
  [L(outline([(16, 104), (4, 80), (2, 46), (14, 14), (50, 0), (86, 14), (98, 46), (96, 80), (84, 104), (80, 70), (20, 70)]), GRAY)] +
  dome('front', top=4, w=48, cy=44, n=6, amp=12, sweep=0.4, seed=51, sb=72) +
  [L(outline([(10, 54), (-6, 46, 1), (16, 46)]), 'mid', 'f'), L(outline([(90, 54), (106, 44, 1), (84, 46)]), 'mid', 'f')],
  [L(outline([(70, 52), (80, 40), (84, 20), (66, 4), (36, 2), (12, 14), (0, 46), (2, 84), (14, 104), (34, 104), (44, 78), (56, 60)]), GRAY)] +
  dome('side', top=4, w=46, cy=44, n=6, amp=12, sweep=0.4, seed=51, nape=60, fr=50, shade=False),
  [L(outline([(10, 100), (2, 46), (14, 14), (50, 0), (86, 14), (98, 46), (90, 100), (50, 106)]), GRAY)] +
  dome('back', top=4, w=48, cy=44, n=6, amp=12, sweep=0.4, seed=51, nape=52))

# Tostig Muffler (portero): pelo blanco con reflejos rosados en un casco redondo; una máscara negra le tapa de la nariz para
# abajo y lleva una bufanda blanca alrededor del cuello; ojos negros cuadrados
MASK = _c('#453f3b')
C('tostig-muffler', 'normal', P('#e0d7ce', '#ddc7ad', shade='#c8b0b0'),
  F(eyes='none', brows=False, mouth='none', hairline=[(8, 64), (18, 56), (34, 54), (50, 54), (66, 54), (82, 56), (92, 64)]),
  dome('front', top=0, w=48, cy=46, sb=70) +
  [L(outline([(28, 70), (42, 70), (42, 80), (28, 80)]), BLACK, 'f', False), L(outline([(58, 70), (72, 70), (72, 80), (58, 80)]), BLACK, 'f', False),
   L(outline([(30, 71), (34, 71), (34, 75), (30, 75)]), WHITE, 'f', False), L(outline([(60, 71), (64, 71), (64, 75), (60, 75)]), WHITE, 'f', False),
   L(outline([(17, 82), (50, 84), (83, 82), (82, 96), (66, 106), (50, 108), (34, 106), (18, 96)]), MASK, 'f'),
   L(outline([(20, 104), (50, 110), (80, 104), (82, 114), (50, 120), (18, 114)]), WHITE, 'f')],
  dome('side', top=0, w=48, cy=46, nape=84, fr=54) +
  [L(outline([(76, 70), (86, 70), (86, 80), (76, 80)]), BLACK, 'f', False), L(outline([(52, 84), (88, 82), (86, 98), (70, 106), (54, 100)]), MASK, 'f'),
   L(outline([(48, 102), (84, 104), (84, 114), (48, 114)]), WHITE, 'f')],
  dome('back', top=0, w=48, cy=46, nape=84) + [L(outline([(18, 102), (50, 106), (82, 102), (82, 114), (50, 118), (18, 114)]), WHITE, 'f')])

# Trajan Leet: pelo blanco rosado esponjoso y revuelto, con un flequillo largo que le tapa el ojo derecho y un pelo de punta
# arriba; ojo amarillo con ojera, piruleta roja en la boca
LOLLY = _c('#c8303a')
C('trajan-leet', 'normal', P('#e2d4d0', '#f6e8dc', iris='#c8a828', shade='#b49b9a'),
  F(eyes='none', brows=False, mouth='none', hairline=[(8, 66), (16, 52), (28, 62), (36, 50), (50, 58), (60, 46), (74, 56), (84, 52), (92, 66)]),
  bush('front', top=-2, w=50, cy=46, n=9, amp=7, seed=61, sb=86) +
  [L(outline([(48, 44), (70, 42), (84, 56), (82, 84), (74, 92, 1), (66, 78), (56, 66), (50, 56)]), 'mid', 'f'),
   L(quad((50, 2), (46, -12), (54, -16)), 'mid', 'f', False, False, 2.0),
   L(ell(36, 75, 5.4, 6.6), WHITE, 'f', False), L(ell(36, 76, 4.2, 5.2), 'iris', 'f', False), L(ell(36, 76.5, 2.0, 2.8), BLACK, 'f', False),
   L(quad((30, 72), (36, 67), (42, 72)), OUTC, 'f', False, False, 2.4), L(quad((30, 83), (36, 86), (42, 83)), (150, 120, 130, 255), 'f', False, False, 1.2),
   L([(44, 92), (40, 100)], WHITE, 'f', False, False, 1.4), L(ell(38, 102, 4.4, 4.4), LOLLY, 'f', True)],
  bush('side', top=-2, w=48, cy=46, n=9, amp=7, seed=61, nape=86, fr=52) + sharp_eye_side(_c('#c8a828')) + [L(ell(88, 100, 3.6, 3.6), LOLLY, 'f', True)],
  bush('back', top=-2, w=50, cy=46, n=9, amp=7, seed=61, nape=86))

# ------------------------------------------------------------------ (sheet 2)

# Trappy Zeum (portero): cabezón cuadrado de piel morena con el pelo gris morado cortísimo y plano por arriba; ojos azules
# entornados, nariz roja y una sonrisa enorme de dientes apretados
C('trappy-zeum', 'corpulento', P('#685b68', '#be8d69', iris='#7ab0c8', nose='#a8504a'),
  F(eyes='sharp', brows='angry', mouth='none', face_front=face(w=8, chin=106, jaw=6, top=14), face_side=face_side(chin=6, jaw=6), ear_out=7,
    hairline=[(8, 50), (14, 40), (30, 38), (50, 38), (70, 38), (86, 40), (92, 50)], nose=(50, 82, 3.4)),
  crop('front', top=14, side=48, w=6, flat=10) +
  [L(outline([(34, 88), (66, 88), (64, 100), (36, 100)]), WHITE, 'f', True), L([(36, 94), (64, 94)], OUTC, 'f', False, False, 1.0)] +
  [L([(x, 88), (x, 100)], OUTC, 'f', False, False, 0.8) for x in (42, 50, 58)],
  crop('side', top=14, w=4, flat=10) + [L(outline([(78, 88), (90, 88), (88, 100), (80, 100)]), WHITE, 'f', True)],
  crop('back', top=14, w=6, flat=10))

# Tre 3 Black Blackley: una bola de bolos negra enorme por sombrero, con tres agujeros blancos y un ala alrededor; el pelo
# negro le cae por la cara y le tapa los ojos; solo se le ve la nariz
BALL = _c('#312f32')
def _bowling(view):
    x = 50 if view != 'side' else 46
    out = [L(ell(x, 6, 52, 46), BALL), L(outline([(x - 54, 56), (x - 40, 44), (x, 40), (x + 40, 44), (x + 54, 56), (x + 40, 62), (x, 58), (x - 40, 62)]), _c('#201d1d'))]
    if view == 'front':
        out += [L(ell(32, -4, 9, 8), WHITE, 'f', False), L(ell(58, -16, 9, 8), WHITE, 'f', False), L(ell(62, 8, 9, 8), WHITE, 'f', False)]
    elif view == 'side':
        out += [L(ell(70, -8, 7, 8), WHITE, 'f', False), L(ell(74, 14, 6, 7), WHITE, 'f', False)]
    return out
C('tre-3-black-blackley', 'normal', P('#292526', '#f1d2bb', nose='#8a6a5a'),
  F(eyes='none', brows=False, mouth='line', mouth_y=94, hairline=False, nose=(50, 86, 2.4)),
  [L(outline([(10, 92), (14, 60), (86, 60), (92, 92, 1), (78, 84), (74, 70), (60, 82, 1), (50, 70), (40, 82, 1), (28, 70), (22, 86)]), 'mid', 'f')] + _bowling('front'),
  [L(outline([(72, 60), (90, 62), (86, 84, 1), (76, 74), (60, 70), (40, 90), (14, 94, 1), (4, 62)]), 'mid', 'f')] + _bowling('side'),
  [L(outline([(8, 96), (6, 60), (94, 60), (92, 96), (70, 90), (50, 96), (30, 90)]))] + _bowling('back'))

# Trent Tarantula Ulah (portero): sombrero de tarántula granate peluda con las patas que le caen por los lados; antifaz
# naranja en pico con los ojos rojos; boca de enfado
SPID, MASKO = _c('#622240'), _c('#f0a030')
def _spider(view):
    if view == 'side':
        body = [L(outline([(70, 52), (86, 40), (80, 14), (56, 2), (28, 4), (8, 20), (4, 46), (20, 56), (44, 52)]), SPID)]
        legs = [L(quad((20, 30), (-10, 30), (-8, 70)), SPID, 'f', False, False, 4.6), L(quad((30, 46), (8, 64), (16, 104)), SPID, 'f', False, False, 4.6),
                L(quad((70, 20), (90, 0), (96, -16)), SPID, 'f', False, False, 4.6)]
        return body + legs
    body = [L(outline([(14, 56), (10, 30), (26, 8), (50, 0), (74, 8), (90, 30), (86, 56), (50, 52)]), SPID),
            L(blob([(60, 6), (84, 24), (88, 52), (70, 40)], 6), _c('#551e34'), 'b', False)]
    legs = []
    for s in (-1, 1):
        legs += [L(quad((50 + s * 28, 14), (50 + s * 44, -4), (50 + s * 46, -22)), SPID, 'f', False, False, 4.6),
                 L(quad((50 + s * 36, 30), (50 + s * 60, 34), (50 + s * 56, 66)), SPID, 'f', False, False, 4.6),
                 L(quad((50 + s * 34, 46), (50 + s * 50, 70), (50 + s * 42, 106)), SPID, 'f', False, False, 4.6)]
    return body + legs
C('trent-tarantula-ulah', 'normal', P('#622240', '#c28e5c'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=94, hairline=False),
  _spider('front') +
  [L(outline([(18, 64), (40, 66), (50, 72), (60, 66), (82, 64), (80, 76), (62, 82), (50, 88, 1), (38, 82), (20, 76)]), MASKO, 'f'),
   L(ell(36, 74, 4, 3.6), _c('#d82a1a'), 'f', True), L(ell(64, 74, 4, 3.6), _c('#d82a1a'), 'f', True),
   L([(28, 66), (42, 72)], OUTC, 'f', False, False, 2.4), L([(72, 66), (58, 72)], OUTC, 'f', False, False, 2.4)],
  _spider('side') + [L(outline([(66, 64), (90, 64), (92, 76), (84, 84, 1), (68, 78)]), MASKO, 'f'), L(ell(84, 73, 2.6, 3), _c('#d82a1a'), 'f', True)],
  _spider('back'))

# Trev Eeya: tupé naranja rojizo alto en mechones de punta echados hacia atrás, sobre los lados cortos; cara cuadrada,
# gafas rectangulares verde azulado, nariz grande cuadrada naranja y cejas naranjas en pico
TEAL2, NOSEO = _c('#2a8a9a'), _c('#e99458')
C('trev-eeya', 'normal', P('#ca684b', '#f7bb7d', iris='#2a2020', brow='#c8502a'),
  F(eyes='round', brows=False, mouth='smile', mouth_y=96, face_front=face(w=4, chin=104, jaw=5, top=14),
    hairline=[(8, 54), (16, 44), (30, 42), (50, 42), (70, 42), (84, 44), (92, 54)]),
  crop('front', top=14, side=54, w=2) +
  [L(outline([(24, 30), (26, 6), (36, -16, 1), (44, 4), (56, -22, 1), (62, 2), (80, -12, 1), (78, 12), (84, 30), (50, 26)])),
   L(outline([(58, -14), (80, -12), (78, 12), (84, 30), (64, 22)]), 'shade', 'b', False),
   L(outline([(24, 64), (42, 60), (40, 65), (26, 68)]), 'brow', 'f', False), L(outline([(76, 64), (58, 60), (60, 65), (74, 68)]), 'brow', 'f', False),
   L(outline([(22, 70), (46, 70), (46, 82), (22, 82)]) + [(22, 70)], TEAL2, 'f', False, False, 2.6),
   L(outline([(54, 70), (78, 70), (78, 82), (54, 82)]) + [(54, 70)], TEAL2, 'f', False, False, 2.6),
   L(outline([(42, 78), (58, 78), (60, 90), (40, 90)]), NOSEO, 'f', True)],
  crop('side', top=14) + [L(outline([(30, 24), (34, 0), (46, -20, 1), (52, 2), (66, -14, 1), (68, 10), (84, 4, 1), (82, 24), (60, 30)])),
                          L(outline([(74, 70), (88, 70), (88, 82), (74, 82)]) + [(74, 70)], TEAL2, 'f', False, False, 2.4),
                          L(outline([(84, 78), (96, 80), (94, 90), (84, 90)]), NOSEO, 'f', True)],
  crop('back', top=14) + [L(outline([(24, 30), (26, 6), (36, -16, 1), (44, 4), (56, -22, 1), (62, 2), (80, -12, 1), (78, 12), (84, 30), (50, 34)]))])

# Trey Faste: cara larga muy pálida, pelo verde agua grisáceo peinado hacia atrás y liso que le cae por detrás hasta los
# hombros; ojos afilados con mucho negro alrededor, sonrisa fina y alargada
C('trey-faste', 'delgado', P('#719c8f', '#fcefd3', iris='#2a2a2a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=98, mouth_w=12, face_front=face(chin=112, top=6), face_side=face_side(chin=10),
    hairline=[(8, 60), (16, 40), (30, 30), (50, 28), (70, 30), (84, 40), (92, 60)]),
  [L(outline([(16, 64), (12, 30), (24, 8), (50, 2), (76, 8), (88, 30), (84, 64), (96, 112, 1), (74, 104), (82, 60), (18, 60), (26, 104), (4, 112, 1)])),
   L(outline([(60, 4), (80, 14), (88, 34), (88, 104), (78, 64)]), 'shade', 'b', False),
   L(quad((26, 70), (36, 66), (46, 72)), OUTC, 'f', False, False, 2.2), L(quad((74, 70), (64, 66), (54, 72)), OUTC, 'f', False, False, 2.2)],
  [L(outline([(70, 40), (80, 30), (74, 10), (50, 2), (24, 6), (8, 22), (2, 50), (4, 90), (14, 116, 1), (30, 100), (40, 70), (50, 48)])),
   L(outline([(4, 48), (28, 52), (36, 76), (28, 100), (12, 112)]), 'shade', 'b', False)],
  [L(outline([(14, 70), (12, 30), (24, 8), (50, 2), (76, 8), (88, 30), (86, 70), (90, 112, 1), (70, 104), (50, 110, 1), (30, 104), (10, 112, 1)])),
   L(outline([(58, 6), (80, 16), (88, 36), (86, 104), (66, 60)]), 'shade', 'b', False)])

# Trey Prongs: casco gris como de escarabajo, con tres franjas negras y una pala que le baja por la nariz; cara larga y
# pálida, orejas enormes en punta, marcas negras alrededor de los ojos y dientes apretados
HELM = _c('#9c9a98')
C('trey-prongs', 'delgado', P('#9c9a98', '#fdf1da', iris='#1e1a1a'),
  F(eyes='sharp', brows=False, mouth='grin', mouth_y=98, face_front=face(chin=112), face_side=face_side(chin=10), hairline=False),
  [L(outline([(14, 60), (12, 30), (26, 6), (50, -4), (74, 6), (88, 30), (86, 60), (62, 56), (56, 66), (54, 92, 1), (48, 92), (44, 66), (38, 56)]), HELM),
   L(outline([(30, 52), (32, 20), (40, 8), (42, 52)]), BLACK, 'f', False), L(outline([(70, 52), (68, 20), (60, 8), (58, 52)]), BLACK, 'f', False),
   L(outline([(46, 50), (48, 0), (52, 0), (54, 50)]), _c('#6a6866'), 'f', False),
   L(outline([(24, 68), (34, 64), (42, 72), (30, 82, 1)]), BLACK, 'b', False), L(outline([(76, 68), (66, 64), (58, 72), (70, 82, 1)]), BLACK, 'b', False),
   L(outline([(16, 62), (-2, 44, 1), (14, 80)]), 'skin', 'b'), L(outline([(84, 62), (102, 44, 1), (86, 80)]), 'skin', 'b')],
  [L(outline([(72, 56), (84, 46), (90, 30), (78, 6), (50, -4), (22, 4), (6, 24), (4, 54), (24, 64), (50, 56)]), HELM),
   L(outline([(40, 4), (50, 2), (34, 56), (24, 56)]), BLACK, 'f', False), L(outline([(84, 50), (92, 56), (90, 92, 1), (84, 70)]), HELM, 'f')],
  [L(outline([(12, 70), (12, 30), (26, 6), (50, -4), (74, 6), (88, 30), (88, 70), (50, 76)]), HELM),
   L(outline([(30, 66), (32, 20), (40, 8), (42, 70)]), BLACK, 'f', False), L(outline([(70, 66), (68, 20), (60, 8), (58, 70)]), BLACK, 'f', False),
   L(outline([(16, 62), (-2, 44, 1), (14, 80)]), 'skin', 'f'), L(outline([(84, 62), (102, 44, 1), (86, 80)]), 'skin', 'f')])

# Trixie Playfair: media melena carmesí en mechones de punta abiertos hacia los lados, con un flequillo de picos; ojos
# amarillos afilados con pestañas y una media sonrisa
C('trixie-playfair', 'chica', P('#962231', '#f8bc7e', iris='#d8a820'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=[(8, 66), (16, 52), (26, 64), (32, 48), (42, 60), (50, 46), (58, 60), (68, 48), (74, 64), (84, 52), (92, 66)]),
  dome('front', top=-2, w=50, cy=46, n=9, amp=9, seed=71, long=94, flare=16) +
  [L(outline([(6, 80), (-10, 92, 1), (12, 92)]), 'mid', 'b'), L(outline([(94, 80), (110, 92, 1), (88, 92)]), 'mid', 'b')],
  dome('side', top=-2, w=48, cy=46, n=9, amp=9, seed=71, long=94, flare=12, fr=52),
  dome('back', top=-2, w=50, cy=46, n=9, amp=9, seed=71, long=96, flare=16, ends=5))

# Troi Dryer: pelo rojo peinado hacia atrás en una ola que baja por los lados hasta el cuello; cara pálida, sombras grises
# redondas alrededor de los ojos, ceño, nariz grande marcada y boca recta
C('troi-dryer', 'normal', P('#bd2e39', '#fdf4db', iris='#3a3040'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, face_front=face(chin=106, top=8), face_side=face_side(chin=5, nose=4),
    hairline=[(8, 60), (16, 42), (30, 34), (50, 32), (70, 34), (84, 42), (92, 60)]),
  [L(outline([(16, 66), (12, 30), (26, 6), (50, 0), (74, 6), (88, 30), (84, 66), (98, 98, 1), (80, 92), (82, 62), (18, 62), (20, 92), (2, 98, 1)])),
   L(outline([(56, 2), (80, 14), (88, 34), (90, 92), (78, 56)]), 'shade', 'b', False),
   L(blob([(24, 68), (44, 68), (46, 82), (26, 82)], 4), _c('#b8b0c0'), 'f', False), L(blob([(56, 68), (76, 68), (74, 82), (54, 82)], 4), _c('#b8b0c0'), 'f', False),
  ] + sharp_eyes(_c('#3a3040')) + [L([(24, 63), (42, 68)], OUTC, 'f', False, False, 3.0), L([(76, 63), (58, 68)], OUTC, 'f', False, False, 3.0),
   L(quad((50, 70), (46, 82), (52, 88)), OUTC, 'f', False, False, 1.4)],
  [L(outline([(70, 40), (80, 30), (74, 10), (50, 0), (24, 6), (8, 22), (2, 50), (6, 86), (16, 104, 1), (32, 90), (40, 66), (50, 46)])),
   L(outline([(4, 50), (28, 54), (36, 76), (24, 96)]), 'shade', 'b', False)] + sharp_eye_side(_c('#3a3040')) + [L([(70, 63), (84, 67)], OUTC, 'f', False, False, 3.0)],
  [L(outline([(14, 74), (12, 30), (26, 6), (50, 0), (74, 6), (88, 30), (86, 74), (96, 100, 1), (70, 94), (50, 98), (30, 94), (4, 100, 1)])),
   L(outline([(58, 4), (80, 16), (88, 36), (88, 94), (66, 60)]), 'shade', 'b', False)])

# ------------------------------------------------------------------ (sheet 3)

# Trump Dealer: pelo azul pizarra liso con un mechón larguísimo que le tapa media cara (su lado derecho) hasta el pecho;
# un solo ojo verde rodeado de negro, cicatrices cosidas en la frente y la mejilla; piel pálida
C('trump-dealer', 'delgado', P('#636f8e', '#f3ecc9', iris='#4aa04a'),
  F(eyes='none', brows=False, mouth='none', face_front=face(chin=106), hairline=[(8, 60), (16, 42), (34, 32), (50, 30), (66, 32), (84, 42), (92, 60)]),
  [L(outline([(16, 62), (12, 30), (26, 6), (52, 0), (76, 8), (90, 24), (102, 30, 1), (88, 40), (84, 62), (80, 46), (60, 36), (52, 40)])),
   L(outline([(54, 2), (30, 10), (14, 30), (12, 70), (24, 104), (40, 128, 1), (44, 100), (46, 60), (50, 36)]), 'mid', 'f'),
   L(outline([(30, 14), (20, 40), (22, 80), (36, 120)]), 'shade', 'f', False, False, 1.6),
   L(outline([(56, 70), (74, 68), (78, 76), (60, 80)]), BLACK, 'f', False), L(ell(66, 74, 4, 3.2), 'iris', 'f', False), L(ell(66, 74, 1.6, 1.6), BLACK, 'f', False),
   L([(62, 44), (70, 60)], OUTC, 'f', False, False, 1.0), L([(60, 50), (66, 48)], OUTC, 'f', False, False, 1.0), L([(64, 56), (70, 54)], OUTC, 'f', False, False, 1.0),
   L([(52, 92), (62, 96)], OUTC, 'f', False, False, 1.0), L([(54, 90), (56, 96)], OUTC, 'f', False, False, 1.0), L([(58, 92), (60, 97)], OUTC, 'f', False, False, 1.0)],
  [L(outline([(70, 44), (80, 34), (76, 10), (52, 0), (26, 6), (8, 22), (2, 50), (6, 80), (16, 92), (30, 80), (40, 60), (54, 48)])),
   L(outline([(-4, 30, 1), (10, 26), (8, 40)])), L(outline([(78, 64), (88, 64), (88, 72), (78, 72)]), BLACK, 'f', False), L(ell(83, 68, 2.4, 2.4), 'iris', 'f', False)],
  [L(outline([(14, 76), (12, 30), (26, 6), (50, 0), (76, 8), (90, 24), (102, 30, 1), (88, 40), (86, 76), (50, 84)])),
   L(outline([(-2, 30, 1), (14, 22), (12, 40)])), L(outline([(60, 6), (80, 16), (88, 40), (86, 74), (66, 60)]), 'shade', 'b', False)])

# Tsun Derrey: media melena naranja en forma de campana, abierta hacia fuera a la altura de la mandíbula, con un flequillo
# recto partido en mechones; ojos verdes con pestañas y boquita enfurruñada
C('tsun-derrey', 'chica', P('#f77e36', '#fdecc4', iris='#3a9a4a'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=93, hairline=[(8, 62), (16, 56), (28, 62), (32, 52), (44, 62), (50, 52), (56, 62), (68, 52), (72, 62), (84, 56), (92, 62)]),
  [L(outline([(18, 70), (12, 36), (24, 12), (50, 2), (76, 12), (88, 36), (82, 70), (104, 84, 1), (82, 92), (80, 60), (20, 60), (18, 92), (-4, 84, 1)])),
   L(outline([(58, 4), (80, 16), (88, 40), (84, 76), (100, 84), (84, 90), (78, 50)]), 'shade', 'b', False)],
  [L(outline([(70, 52), (82, 44), (82, 20), (60, 2), (30, 4), (10, 20), (2, 52), (-2, 84, 1), (20, 90), (36, 82), (44, 62), (56, 54)])),
   L(outline([(4, 52), (28, 56), (34, 80), (16, 88)]), 'shade', 'b', False)],
  [L(outline([(16, 76), (12, 36), (24, 12), (50, 2), (76, 12), (88, 36), (84, 76), (104, 86, 1), (50, 96), (-4, 86, 1)])),
   L(outline([(58, 6), (80, 18), (88, 40), (86, 76), (100, 86), (66, 90)]), 'shade', 'b', False)])

# Tuff Weedon: pelo verde menta en un casco cuadrado, con flequillo recto de mechones y rizos enroscados junto a las
# patillas; piel morena, marca II en la frente, espirales verdes alrededor de los ojos y labios gruesos
MINT2 = _c('#6ac888')
C('tuff-weedon', 'normal', P('#a0e4af', '#ce986a', iris='#2a2020', shade='#7ac08a'),
  F(eyes='sharp', brows=False, mouth='lips', mouth_y=97, mouth_w=8, face_front=face(chin=106), hairline=[(8, 58), (16, 50), (24, 58), (30, 48), (70, 48), (76, 58), (84, 50), (92, 58)]),
  [L(outline([(16, 76), (12, 36), (22, 10), (50, 2), (78, 10), (88, 36), (84, 76), (82, 54), (18, 54)])),
   L(outline([(58, 4), (80, 14), (88, 38), (84, 72), (78, 44)]), 'shade', 'b', False),
   L(quad((16, 74), (8, 82), (16, 88)), 'mid', 'f', False, False, 3.0), L(quad((84, 74), (92, 82), (84, 88)), 'mid', 'f', False, False, 3.0),
   L(quad((30, 64), (22, 76), (34, 84)), MINT2, 'f', False, False, 1.8), L(quad((70, 64), (78, 76), (66, 84)), MINT2, 'f', False, False, 1.8),
   L([(47, 52), (47, 60)], OUTC, 'f', False, False, 1.4), L([(53, 52), (53, 60)], OUTC, 'f', False, False, 1.4),
   L([(45, 52), (55, 52)], OUTC, 'f', False, False, 1.0), L([(45, 60), (55, 60)], OUTC, 'f', False, False, 1.0)],
  [L(outline([(68, 48), (82, 44), (84, 20), (64, 2), (34, 2), (12, 16), (4, 46), (6, 80), (22, 88), (40, 76), (50, 56)])),
   L(outline([(5, 44), (30, 48), (38, 72), (22, 86)]), 'shade', 'b', False), L(quad((72, 64), (64, 76), (76, 84)), MINT2, 'f', False, False, 1.8)],
  [L(outline([(14, 82), (12, 36), (22, 10), (50, 2), (78, 10), (88, 36), (86, 82), (50, 88)])),
   L(outline([(58, 6), (80, 16), (88, 40), (86, 80), (66, 60)]), 'shade', 'b', False)])

# Turco Turquoise Quoisey: gorro de seta turquesa grande y redondo con manchas negras; gafas redondas blancas con los
# cristales oscuros; cara regordeta y pálida, sonrisa abierta
SHROOM = _c('#37c6c8')
def _shroom(view):
    x = 50 if view != 'side' else 46
    out = [L(outline([(x - 54, 62), (x - 52, 34), (x - 34, 8), (x, -2), (x + 34, 8), (x + 52, 34), (x + 54, 62), (x + 40, 56), (x, 52), (x - 40, 56)]), SHROOM),
           L(blob([(x + 14, 4), (x + 40, 18), (x + 52, 50), (x + 30, 40)], 6), _c('#2aa0a4'), 'b', False)]
    spots = [(x - 30, 22, 8), (x + 2, 8, 7), (x + 26, 26, 9), (x - 8, 36, 6)] if view == 'front' else [(x - 20, 14, 8), (x + 16, 10, 7), (x + 30, 34, 8), (x - 34, 40, 6)]
    out += [L(ell(sx, sy, r, r * 0.8), _c('#292d37'), 'f', False) for sx, sy, r in spots]
    return out
C('turco-turquoise-quoisey', 'corpulento', P('#37c6c8', '#fbefd3', iris='#1e1a1a'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, face_front=face(w=6, chin=104, jaw=4), hairline=False),
  _shroom('front') +
  [L(ell(35, 74, 9, 8), WHITE, 'f', True), L(ell(65, 74, 9, 8), WHITE, 'f', True), L(ell(35, 74, 5.6, 5), _c('#3f4a4c'), 'f', False),
   L(ell(65, 74, 5.6, 5), _c('#3f4a4c'), 'f', False), L(quad((44, 92), (50, 100), (56, 92)) + [(50, 93)], _c('#c84a5a'), 'f', True)],
  _shroom('side') + [L(ell(83, 74, 5, 8), WHITE, 'f', True), L(ell(84, 74, 3, 5), _c('#3f4a4c'), 'f', False)],
  _shroom('back'))

# Turner Newleaf: tupé gris verdoso altísimo y muy abierto por arriba (como un trapecio), con los lados cortos; un antifaz
# oscuro sobre los ojos, piel morena y una cicatriz en la mejilla
MASKD = _c('#3e3833')
C('turner-newleaf', 'normal', P('#6a7f77', '#cc976b', iris='#1e1a1a'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=95, face_front=face(chin=106), hairline=[(8, 60), (18, 56), (34, 58), (50, 58), (66, 58), (82, 56), (92, 60)]),
  [L(outline([(17, 74), (14, 54), (2, -24), (98, -24), (86, 54), (83, 74), (80, 60), (20, 60)])),
   L(outline([(62, -22), (96, -22), (86, 50), (84, 70), (74, 20)]), 'shade', 'b', False),
   L(outline([(17, 62), (50, 64), (83, 62), (82, 80), (50, 80), (18, 80)]), MASKD, 'f'),
   L(outline([(26, 68), (42, 70), (40, 76), (28, 75)]), WHITE, 'f', False), L(outline([(74, 68), (58, 70), (60, 76), (72, 75)]), WHITE, 'f', False),
   L(ell(35, 72.5, 2.4, 2.4), BLACK, 'f', False), L(ell(65, 72.5, 2.4, 2.4), BLACK, 'f', False),
   L([(26, 66), (42, 70)], OUTC, 'f', False, False, 2.0), L([(74, 66), (58, 70)], OUTC, 'f', False, False, 2.0),
   L([(62, 92), (66, 98)], _c('#8a4a34'), 'f', False, False, 1.4)],
  [L(outline([(66, 58), (86, 54), (102, -20), (40, -26), (4, -20), (2, 40), (8, 76), (24, 84), (40, 70), (52, 58)])),
   L(outline([(52, 64), (88, 62), (88, 80), (56, 80)]), MASKD, 'f'), L(outline([(76, 68), (86, 69), (85, 75), (77, 74)]), WHITE, 'f', False)],
  [L(outline([(14, 80), (14, 54), (2, -24), (98, -24), (86, 54), (86, 80), (50, 86)])),
   L(outline([(62, -22), (96, -22), (86, 54), (86, 78), (70, 40)]), 'shade', 'b', False),
   L(outline([(14, 66), (86, 66), (86, 74), (14, 74)]), MASKD, 'f')])

# Turner Tabel: melena larga castaño malva con raya en medio, que le cae lisa por los lados hasta el pecho; gafas de sol
# rosas en forma de mariposa, cara larga, ceño y dientes apretados
PINKG = _c('#e8a8d8')
C('turner-tabel', 'delgado', P('#a37a70', '#fabb7b', iris='#3a2a2a'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=98, face_front=face(chin=110, top=6), face_side=face_side(chin=8),
    hairline=[(8, 66), (18, 46), (34, 34), (50, 30), (66, 34), (82, 46), (92, 66)]),
  dome('front', top=0, w=48, cy=46, long=126, flare=8, shade=True) +
  [L(outline([(48, 4), (50, 30), (52, 4)]), 'shade', 'f', False),
   L(outline([(22, 70), (36, 64), (48, 72), (44, 84), (30, 84)]), PINKG, 'f', True), L(outline([(78, 70), (64, 64), (52, 72), (56, 84), (70, 84)]), PINKG, 'f', True),
   L([(30, 72), (42, 80)], _c('#a0508a'), 'f', False, False, 2.4), L([(70, 72), (58, 80)], _c('#a0508a'), 'f', False, False, 2.4)],
  dome('side', top=0, w=48, cy=46, long=126, flare=8, fr=40) + [L(outline([(70, 68), (88, 66), (86, 82), (72, 80)]), PINKG, 'f', True)],
  dome('back', top=0, w=48, cy=46, long=128, flare=8, ends=6))

# Ty Titan Tanner: cabezón calvo de piel gris verdosa (como un zombi), cara enorme de mandíbula ancha, ojos amarillos
# caídos, nariz morada con una lágrima y boca de enfado
C('ty-titan-tanner', 'corpulento', P('#7a9088', '#89b8a8', iris='#e8d040', nose='#8a6a8a'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=96, face_front=face(w=8, chin=108, jaw=8, top=12), face_side=face_side(chin=8, jaw=8), ear_out=7,
    hairline=False, nose=(50, 84, 4)),
  skull3('front') +
  [L(outline([(26, 72), (44, 74), (42, 80), (28, 78)]), _c('#e8d040'), 'f', True), L(outline([(74, 72), (56, 74), (58, 80), (72, 78)]), _c('#e8d040'), 'f', True),
   L([(24, 70), (44, 74)], OUTC, 'f', False, False, 2.4), L([(76, 70), (56, 74)], OUTC, 'f', False, False, 2.4),
   L(ell(56, 92, 1.4, 2), _c('#2a3a3a'), 'f', False)],
  skull3('side') + [L(outline([(74, 72), (86, 74), (84, 80), (76, 78)]), _c('#e8d040'), 'f', True)],
  skull3('back'))

# Tye Foon: pelo verde oscuro recogido en un moño arriba con un lazo rojo y dos rizos enormes enroscados a los lados como
# cuernos de carnero; piel morena, ojos amarillos afilados y ceño muy fruncido
GRN2 = _c('#546745')
def _ramcurl(x, y, s):
    return [L(outline([(x, y - 22), (x + s * 18, y - 16), (x + s * 22, y + 4), (x + s * 14, y + 24), (x, y + 26), (x - s * 4, y + 6)]), GRN2),
            L(quad((x + s * 4, y - 12), (x + s * 18, y), (x + s * 6, y + 14)) + quad((x + s * 6, y + 14), (x, y + 2), (x + s * 8, y - 4))[1:],
              _c('#353628'), 'f', False, False, 1.8)]
C('tye-foon', 'normal', P('#546745', '#bd8d69', iris='#e8d040'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=95, face_front=face(w=3, chin=104, jaw=3), hairline=[(8, 56), (18, 46), (34, 42), (50, 42), (66, 42), (82, 46), (92, 56)]),
  crop('front', top=4, side=56) + _ramcurl(10, 60, -1) + _ramcurl(90, 60, 1) +
  [L(ell(50, -4, 12, 9), 'mid', 'f'), L(ell(50, 6, 6, 3), _c('#c83a3a'), 'f', True)],
  crop('side', top=4) + _ramcurl(40, 60, -1) + [L(ell(46, -4, 11, 9), 'mid', 'f'), L(ell(50, 6, 5, 3), _c('#c83a3a'), 'f', True)],
  crop('back', top=4) + _ramcurl(10, 60, -1) + _ramcurl(90, 60, 1) + [L(ell(50, -4, 12, 9), 'mid', 'f'), L(ell(50, 6, 6, 3), _c('#c83a3a'), 'f', True)])

# ------------------------------------------------------------------ (sheet 4)

# Tyko Wondo (portero): pelo rubio en un tupé de mechones echados hacia arriba y hacia su izquierda; piel tostada, cejas
# pintadas amarillas en pico, perilla amarilla dibujada en la barbilla, ojos azules y sonrisa
YEL2 = _c('#f2c23a')
C('tyko-wondo', 'normal', P('#fad37a', '#ce9766', iris='#5aa8c8', shade='#d8a848'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=92, face_front=face(chin=106, top=8), face_side=face_side(chin=5),
    hairline=[(8, 54), (16, 40), (30, 34), (50, 32), (70, 34), (84, 40), (92, 54)]),
  crop('front', top=8, side=54) +
  [L(outline([(20, 30), (18, 10), (30, -10), (44, -20, 1), (52, -4), (70, -18, 1), (74, -2), (96, -4, 1), (84, 14), (82, 30), (50, 26)])),
   L(outline([(60, -14), (74, -2), (96, -4), (84, 14), (82, 30), (66, 20)]), 'shade', 'b', False),
   L(outline([(24, 66), (34, 58), (44, 64), (40, 68), (32, 64), (26, 70)]), YEL2, 'f', False),
   L(outline([(76, 66), (66, 58), (56, 64), (60, 68), (68, 64), (74, 70)]), YEL2, 'f', False),
   L(outline([(40, 98), (46, 96), (50, 99), (54, 96), (60, 98), (56, 106), (50, 102), (44, 106)]), YEL2, 'f', False)],
  crop('side', top=8) + [L(outline([(28, 22), (32, 2), (48, -16, 1), (56, 0), (72, -10, 1), (74, 6), (94, 2, 1), (84, 24), (58, 28)])),
                         L(outline([(80, 98), (88, 96), (86, 106)]), YEL2, 'f', False)],
  crop('back', top=8) + [L(outline([(20, 30), (18, 10), (30, -10), (44, -20, 1), (52, -4), (70, -18, 1), (74, -2), (96, -4, 1), (84, 14), (82, 30), (50, 34)]))])

# Una Lightning (portera): melena hasta el pecho partida en dos colores, naranja por su derecha y gris oscuro por su
# izquierda, con el flequillo naranja echado a un lado; piel muy clara, ojos grandes y sonrisa
GRY2 = _c('#5e5956')
C('una-lightning', 'chica', P('#fdb744', '#f7f0d9', iris='#4a5a6a', shade='#d8902a'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=[(8, 66), (16, 50), (30, 44), (44, 46), (56, 40), (70, 44), (84, 50), (92, 66)]),
  dome('front', top=-2, w=50, cy=46, long=112, flare=8) +
  [L(outline([(54, -1), (76, 4), (94, 22), (100, 46), (100, 80), (106, 116, 1), (88, 108), (84, 64), (76, 50), (60, 44)]), GRY2),
   L(outline([(30, 4), (50, 0), (56, 40), (40, 52), (24, 70), (14, 96, 1), (16, 60)]), 'mid', 'f')],
  dome('side', top=-2, w=48, cy=46, long=112, flare=8, fr=50, c=GRY2),
  [L(outline([(0, 70), (2, 40), (14, 14), (50, 0), (50, 116, 1), (30, 108), (-2, 114, 1)])),
   L(outline([(50, 0), (86, 14), (98, 40), (100, 70), (102, 114, 1), (70, 108), (50, 116)]), GRY2)])

# Uno 1 Black Blackley (portero): como su hermano Tre, una bola de bolos negra por sombrero con un ala, pero con un solo
# agujero blanco enorme; el pelo negro le tapa los ojos
def _bowling1(view):
    out = _bowling(view)[:2]
    if view == 'front':
        out.append(L(ell(54, -2, 15, 15), WHITE, 'f', False))
    elif view == 'side':
        out.append(L(ell(72, 0, 9, 13), WHITE, 'f', False))
    return out
C('uno-1-black-blackley', 'normal', P('#272324', '#c8a088', nose='#8a5a4a'),
  F(eyes='none', brows=False, mouth='line', mouth_y=94, hairline=False, nose=(52, 86, 2.6)),
  [L(outline([(10, 92), (14, 60), (86, 60), (94, 90, 1), (80, 84), (74, 70), (62, 84, 1), (52, 70), (42, 84, 1), (30, 70), (22, 88)]), 'mid', 'f')] + _bowling1('front'),
  [L(outline([(72, 60), (90, 62), (86, 84, 1), (76, 74), (60, 70), (40, 90), (14, 94, 1), (4, 62)]), 'mid', 'f')] + _bowling1('side'),
  [L(outline([(8, 96), (6, 60), (94, 60), (92, 96), (70, 90), (50, 96), (30, 90)]))] + _bowling1('back'))

# Uzi Slugge: capucha lila de hipopótamo con orejas redondas y el hocico encima de los ojos (con dos bultos de nariz y una
# nariz marrón); solo se le ve la boca, sonriendo con los dientes
HIPPO = _c('#a498b4')
def _hippo(view):
    if view == 'side':
        return [L(outline([(70, 104), (66, 86), (74, 80), (98, 80), (100, 58), (88, 46), (74, 10), (50, 0), (24, 6), (4, 30), (0, 70), (10, 100), (40, 108)]), HIPPO),
                L(ell(40, -2, 9, 10), HIPPO), L(ell(97, 64, 3.4, 3.4), _c('#9b807d'), 'f', True)]
    out = [L(outline([(10, 108), (2, 70), (4, 30), (20, 6), (50, 0), (80, 6), (96, 30), (98, 70), (90, 108), (78, 96), (80, 70), (20, 70), (22, 96)]), HIPPO),
           L(ell(18, -2, 11, 10), HIPPO), L(ell(82, -2, 11, 10), HIPPO), L(ell(18, -2, 5, 4.6), _c('#7b6371'), 'f', False), L(ell(82, -2, 5, 4.6), _c('#7b6371'), 'f', False)]
    if view == 'front':
        out += [L(outline([(16, 58), (30, 50), (50, 48), (70, 50), (84, 58), (82, 82), (50, 86), (18, 82)]), HIPPO, 'f'),
                L(ell(38, 62, 5, 4), _c('#b8acc8'), 'f', True), L(ell(62, 62, 5, 4), _c('#b8acc8'), 'f', True),
                L(ell(50, 76, 6, 4.4), _c('#9b807d'), 'f', True)]
    return out
C('uzi-slugge', 'normal', P('#a498b4', '#e9d6bc'),
  F(eyes='none', brows=False, mouth='none', hairline=False),
  _hippo('front') + [L(quad((36, 92), (50, 98), (64, 92)) + quad((64, 92), (50, 102), (36, 92))[1:], WHITE, 'f', True)],
  _hippo('side'), _hippo('back'))

# Val Cano: media melena celeste muy clara con las puntas abiertas como aletas y la parte de abajo morada oscura; unas
# gafas de esquí rosas con el cristal negro sobre la frente; piel morena, ojos rosas y boca seria
PINK2, DARKV = _c('#d8406a'), _c('#403846')
C('val-cano', 'chica', P('#d8eaf4', '#bd8b6b', iris='#c84a6a', shade='#b0c8d8'),
  F(eyes='big', brows=False, mouth='frown', mouth_y=93, hairline=[(8, 62), (18, 54), (34, 52), (50, 52), (66, 52), (82, 54), (92, 62)]),
  [L(outline([(12, 96), (-2, 84, 1), (4, 66), (16, 70)]), DARKV, 'b'), L(outline([(88, 96), (102, 84, 1), (96, 66), (84, 70)]), DARKV, 'b')] +
  dome('front', top=0, w=48, cy=46, long=88, flare=12) +
  [L(outline([(14, 44), (30, 38), (50, 42), (70, 38), (86, 44), (84, 58), (70, 54), (58, 60), (50, 56), (42, 60), (30, 54), (16, 58)]), PINK2, 'f'),
   L(outline([(22, 46), (46, 46), (46, 54), (34, 54), (22, 52)]), BLACK, 'f', False), L(outline([(78, 46), (54, 46), (54, 54), (66, 54), (78, 52)]), BLACK, 'f', False)],
  dome('side', top=0, w=48, cy=46, long=88, flare=10, fr=46) + [L(outline([(54, 42), (88, 40), (90, 54), (60, 56)]), PINK2, 'f'),
                                                                L(outline([(70, 44), (88, 43), (88, 52), (72, 52)]), BLACK, 'f', False)],
  dome('back', top=0, w=48, cy=46, long=90, flare=12) + [L(outline([(6, 46), (94, 46), (94, 52), (6, 52)]), PINK2, 'f')])

# Venoma Sting (portera): pelo morado con un moño de punta enroscado arriba, flequillo recto y dos coletas gruesas que le
# caen por los lados y se curvan hacia dentro a la altura de la barbilla; ojos amarillos con mucho negro y sonrisa pícara
C('venoma-sting', 'chica', P('#90568a', '#e2d2b9', iris='#e0d040'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, hairline=[(8, 62), (18, 60), (34, 64), (50, 64), (66, 64), (82, 60), (92, 62)]),
  dome('front', top=4, w=48, cy=48, sb=70) +
  [L(outline([(10, 56), (2, 80), (8, 106), (26, 112, 1), (22, 100), (14, 84), (20, 64)])), L(outline([(90, 56), (98, 80), (92, 106), (74, 112, 1), (78, 100), (86, 84), (80, 64)])),
   L(outline([(40, 8), (36, -8), (48, -20), (66, -16, 1), (54, -12), (58, 4)]), 'mid', 'f'),
   L(blob([(24, 68), (44, 70), (44, 80), (26, 80)], 4), _c('#2a1e2a'), 'f', False), L(blob([(76, 68), (56, 70), (56, 80), (74, 80)], 4), _c('#2a1e2a'), 'f', False)] + sharp_eyes(_c('#e0d040')),
  dome('side', top=4, w=48, cy=48, nape=88, fr=60) + sharp_eye_side(_c('#e0d040')) + [L(outline([(36, 60), (30, 84), (36, 106), (52, 112, 1), (46, 98), (42, 82), (46, 66)])),
                                                       L(outline([(34, 8), (30, -8), (42, -20), (60, -16, 1), (48, -12), (52, 4)]), 'mid', 'f')],
  dome('back', top=4, w=48, cy=48, nape=88) +
  [L(outline([(10, 56), (2, 80), (8, 106), (26, 112, 1), (22, 100), (14, 84), (20, 64)]), 'mid', 'f'),
   L(outline([(90, 56), (98, 80), (92, 106), (74, 112, 1), (78, 100), (86, 84), (80, 64)]), 'mid', 'f'),
   L(outline([(40, 8), (36, -8), (48, -20), (66, -16, 1), (54, -12), (58, 4)]), 'mid', 'f')])

# Verity Quick: pelo rojo con una cinta amarilla en arco y un flequillo largo que le tapa el ojo izquierdo; mechones de
# punta que salen hacia atrás y una coleta suelta; un ojo azul verdoso y boca seria
C('verity-quick', 'chica', P('#d44759', '#f6eed8', iris='#4aa0a8'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=93, hairline=[(8, 64), (16, 54), (30, 50), (44, 52), (56, 46), (70, 48), (84, 54), (92, 64)]),
  dome('front', top=0, w=48, cy=46, sb=78) +
  [L(outline([(4, 30), (-12, 14, 1), (8, 22)]), 'mid', 'b'), L(outline([(94, 28), (110, 18, 1), (94, 40)]), 'mid', 'b'),
   L(quad((12, 46), (48, 4), (88, 40)), YEL2, 'f', False, False, 3.6),
   L(outline([(48, 30), (66, 34), (82, 52), (84, 80), (72, 92, 1), (66, 74), (56, 62), (50, 46)]), 'mid', 'f'),
   L(outline([(84, 76), (100, 96, 1), (88, 100)]), 'mid', 'f'),
   L(ell(36, 75, 5.4, 6.6), WHITE, 'f', False), L(ell(36, 76, 4.2, 5.2), 'iris', 'f', False), L(ell(36, 76.5, 2.0, 2.8), BLACK, 'f', False),
   L(quad((30, 71), (36, 67), (42, 71)), OUTC, 'f', False, False, 2.4)],
  dome('side', top=0, w=48, cy=46, nape=86, fr=50) + eye_side_n() + [L(quad((40, 2), (70, 10), (90, 36)), YEL2, 'f', False, False, 3.6),
                                                       L(outline([(4, 30), (-14, 18, 1), (10, 20)]), 'mid', 'b')],
  dome('back', top=0, w=48, cy=46, nape=86) + [L(outline([(70, 70), (92, 104, 1), (74, 96)]), 'mid', 'f'),
                                               L(outline([(4, 30), (-12, 14, 1), (8, 22)]), 'mid', 'b'), L(outline([(94, 28), (110, 18, 1), (94, 40)]), 'mid', 'b')])

# Vier 4 White Whitely: un casco blanco redondo como una bola con un 4 negro enorme, calado hasta el ojo derecho; asoma pelo
# blanco rosado; un ojo azul, una tirita en la mejilla y boca de enfado
BALLW = _c('#f2eeea')
def _four(x, y, s=1.0):
    return [L([(x + 4 * s, y - 14 * s), (x - 8 * s, y + 4 * s), (x + 10 * s, y + 4 * s)], BLACK, 'f', False, False, 4.4 * s),
            L([(x + 4 * s, y - 14 * s), (x + 4 * s, y + 14 * s)], BLACK, 'f', False, False, 4.4 * s)]
def _two(x, y, s=1.0):
    return [L(quad((x - 8 * s, y - 8 * s), (x, y - 20 * s), (x + 8 * s, y - 6 * s)) + [(x - 8 * s, y + 12 * s), (x + 10 * s, y + 12 * s)], BLACK, 'f', False, False, 4.4 * s)]
def _numball(view, glyph):
    x = 50 if view != 'side' else 46
    if view == 'front':
        out = [L(outline([(4, 76), (0, 30), (20, 2), (54, -8), (88, 4), (102, 34), (100, 70), (78, 62), (62, 76), (50, 70), (20, 80)]), BALLW),
               L(blob([(70, 4), (94, 22), (100, 60), (80, 56)], 6), _c('#d8d0cc'), 'b', False)]
        return out + glyph(58, 24)
    if view == 'side':
        return [L(outline([(70, 70), (96, 60), (100, 30), (80, 2), (46, -8), (14, 4), (-2, 34), (4, 76), (30, 86), (52, 76)]), BALLW)] + glyph(44, 26, 0.8)
    return [L(outline([(2, 80), (0, 30), (20, 2), (50, -8), (80, 2), (100, 30), (98, 80), (50, 90)]), BALLW),
            L(blob([(62, 0), (90, 20), (98, 70), (74, 70)], 6), _c('#d8d0cc'), 'b', False)]
for _pid, _g, _sk in (('vier-4-white-whitely', _four, '#faedd6'), ('zwei-2-white-whitely', _two, '#faedd6')):
    C(_pid, 'normal', P('#e0c8c4', _sk, iris='#4ab0c8'),
      F(eyes='none', brows=False, mouth='frown', mouth_y=94, hairline=False),
      _numball('front', _g) +
      [L(outline([(14, 74), (8, 90, 1), (22, 84)]), 'mid', 'f'), L(outline([(76, 72), (90, 92, 1), (80, 88)]), 'mid', 'f'),
       L(ell(36, 78, 5.4, 6.4), WHITE, 'f', False), L(ell(36, 79, 4.2, 5), 'iris', 'f', False), L(ell(36, 79.5, 2, 2.6), BLACK, 'f', False),
       L(quad((30, 74), (36, 70), (42, 74)), OUTC, 'f', False, False, 2.2),
       L(outline([(58, 86), (70, 84), (72, 92), (60, 94)]), _c('#f2e2d0'), 'f', True)],
      _numball('side', _g) + [L(ell(83, 79, 3, 5), 'iris', 'f', False)],
      _numball('back', _g))

# ------------------------------------------------------------------ (sheet 5)

# Violet Eamow: pelo morado liso en un casco redondo con una franja blanca cruzada en diagonal, y un mechón que le tapa el
# ojo izquierdo; un ojo rojo grande con pestañas, orejas pequeñas y boca seria
C('violet-eamow', 'chica', P('#654a69', '#f7d7b7', iris='#c83a3a'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=93, hairline=[(8, 60), (18, 48), (34, 42), (50, 40), (66, 42), (82, 48), (92, 60)]),
  crop('front', top=0, side=62) +
  [L(outline([(48, 28), (70, 30), (84, 46), (82, 76), (70, 90, 1), (64, 70), (56, 56), (50, 44)]), 'mid', 'f'),
   L(outline([(30, 18), (84, 40), (80, 52), (26, 30)]), WHITE, 'f', False), L(outline([(60, 66), (80, 76), (76, 84), (60, 76)]), WHITE, 'f', False),
   L(ell(36, 75, 5.4, 6.6), WHITE, 'f', False), L(ell(36, 76, 4.2, 5.2), 'iris', 'f', False), L(ell(36, 76.5, 2.0, 2.8), BLACK, 'f', False),
   L(quad((29, 71), (36, 66), (43, 71)), OUTC, 'f', False, False, 2.6), L([(28, 70), (25, 68)], OUTC, 'f', False, False, 1.6)],
  crop('side', top=0) + eye_side_n() + [L(outline([(20, 20), (60, 8), (66, 18), (26, 32)]), WHITE, 'f', False)],
  crop('back', top=0) + [L(outline([(16, 30), (84, 14), (86, 26), (18, 42)]), WHITE, 'f', False)])

# Virgil Ante: capucha y bufanda de tela crema que le envuelven la cabeza y el cuello, con un pañuelo enrollado en la
# frente; un parche negro en el ojo derecho, el otro ojo afilado y una sonrisa ladeada
CLOTH = _c('#dcd9c9')
C('virgil-ante', 'normal', P('#dcd9c9', '#fcd18d', iris='#2a2020', shade='#aa8b81'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=93, hairline=False, face_front=face(chin=104)),
  hood('front', CLOTH, top=-4, low=112) +
  [L(outline([(18, 50), (50, 44), (82, 50), (80, 58), (50, 54), (20, 58)]), _c('#c8c2b0'), 'f'),
   L(ell(36, 74, 8, 7.4), _c('#27282f'), 'f', True), L([(28, 66), (14, 52)], _c('#27282f'), 'f', False, False, 1.6),
   L(outline([(56, 70), (74, 68), (72, 76), (58, 77)]), WHITE, 'f', False), L(ell(66, 73, 2.6, 3), BLACK, 'f', False),
   L([(56, 69), (75, 67)], OUTC, 'f', False, False, 2.6),
   L(outline([(10, 100), (50, 108), (90, 100), (94, 116), (60, 122), (20, 120)]), CLOTH, 'f'),
   L(outline([(70, 104), (96, 108), (90, 138, 1), (78, 118)]), CLOTH, 'f')],
  hood('side', CLOTH, top=-4) + [L(outline([(70, 100), (92, 102), (92, 116), (66, 116)]), CLOTH, 'f'),
                                  L(outline([(76, 69), (86, 68), (85, 75), (77, 76)]), WHITE, 'f', False)],
  hood('back', CLOTH, top=-4, low=112) + [L(outline([(10, 100), (90, 100), (94, 116), (50, 122), (6, 116)]), CLOTH, 'f')])

# Walden Squire: gorro negro azulado de marinero con una raya naranja cruzada; cara larga y cuadrada como la de un
# monstruo, con costuras a los lados y una placa en la nariz; ojos amarillos en una franja negra y boca seria
CAPN, ORL = _c('#393e47'), _c('#e07a3a')
C('walden-squire', 'delgado', P('#393e47', '#fbe8b7', iris='#e8d040'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=98, face_front=face(w=2, chin=110, jaw=4, top=10), face_side=face_side(chin=8, jaw=4), hairline=False),
  [L(outline([(16, 56), (14, 24), (26, 4), (50, -2), (74, 4), (86, 24), (84, 56), (50, 52)]), CAPN),
   L(outline([(16, 46), (50, 32), (84, 22), (84, 30), (50, 40), (16, 54)]), ORL, 'f', False),
   L(outline([(22, 66), (78, 66), (78, 74), (22, 74)]), BLACK, 'f', False),
   L(outline([(28, 68), (42, 68), (42, 72), (28, 72)]), _c('#e8d040'), 'f', False), L(outline([(58, 68), (72, 68), (72, 72), (58, 72)]), _c('#e8d040'), 'f', False),
   L(outline([(44, 74), (56, 74), (56, 92), (44, 92)]), _c('#e8d8a8'), 'f', True),
   L([(20, 60), (22, 100)], _c('#8b7466'), 'f', False, False, 1.4), L([(80, 60), (78, 100)], _c('#8b7466'), 'f', False, False, 1.4)],
  [L(outline([(70, 52), (84, 46), (88, 26), (70, 4), (44, -2), (20, 4), (6, 22), (4, 52), (30, 58), (50, 54)]), CAPN),
   L(outline([(6, 40), (88, 30), (88, 38), (6, 48)]), ORL, 'f', False), L(outline([(66, 66), (88, 66), (88, 74), (66, 74)]), BLACK, 'f', False),
   L(outline([(78, 68), (86, 68), (86, 72), (78, 72)]), _c('#e8d040'), 'f', False)],
  [L(outline([(14, 66), (14, 24), (26, 4), (50, -2), (74, 4), (86, 24), (86, 66), (50, 70)]), CAPN),
   L(outline([(14, 50), (86, 38), (86, 46), (14, 58)]), ORL, 'f', False)])

# Wally Ramm: lana crema rizada de oveja en la cabeza, con dos cuernos de carnero enroscados a los lados; cara pálida,
# orejas grandes, ojos amarillos caídos y boca pequeña
WOOL, HORN = _c('#d5ccb5'), _c('#a08878')
def _ram(x, y, s):
    return [L(outline([(x - s * 4, y - 16), (x + s * 14, y - 18), (x + s * 22, y - 2), (x + s * 16, y + 14), (x, y + 12), (x - s * 4, y)]), HORN),
            L(quad((x + s * 2, y - 8), (x + s * 16, y - 4), (x + s * 6, y + 6)), _c('#7f6a5e'), 'f', False, False, 1.8)]
C('wally-ramm', 'normal', P('#d5ccb5', '#fdf1da', iris='#c8a030'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=94, hairline=[(8, 60), (16, 54), (24, 60), (32, 54), (40, 60), (50, 54), (60, 60), (68, 54), (76, 60), (84, 54), (92, 60)],
    big_ears=2, ear_out=4),
  bush('front', top=2, w=44, cy=44, n=11, amp=5, seed=81, sb=62) + _ram(12, 34, -1) + _ram(88, 34, 1) +
  [L(outline([(26, 70), (44, 70), (44, 82), (26, 80)]), WHITE, 'f', True), L(outline([(74, 70), (56, 70), (56, 82), (74, 80)]), WHITE, 'f', True),
   L(ell(36, 77, 4, 4), 'iris', 'f', False), L(ell(64, 77, 4, 4), 'iris', 'f', False),
   L([(25, 71), (45, 71)], OUTC, 'f', False, False, 2.6), L([(55, 71), (75, 71)], OUTC, 'f', False, False, 2.6)],
  bush('side', top=2, w=44, cy=44, n=11, amp=5, seed=81, nape=80, fr=52) + _ram(40, 36, -1) +
  [L(outline([(74, 70), (86, 70), (86, 82), (76, 80)]), WHITE, 'f', True), L(ell(82, 77, 2.6, 4), 'iris', 'f', False), L([(73, 71), (87, 71)], OUTC, 'f', False, False, 2.6)],
  bush('back', top=2, w=44, cy=44, n=11, amp=5, seed=81, nape=80) + _ram(12, 34, -1) + _ram(88, 34, 1))

# Walter Skimmer (portero): capucha de calamar crema en forma de rombo, con la punta arriba y alas a los lados, y una
# máscara de tela que le tapa la boca y la nariz, atada por detrás; ojos azules con rayas
SQUID = _c('#e8eedc')
C('walter-skimmer', 'normal', P('#cbcec1', '#faeed6', iris='#4a6ac8'),
  F(eyes='none', brows=False, mouth='none', hairline=False),
  [L(outline([(16, 100), (8, 70), (-8, 50, 1), (14, 30), (50, -14, 1), (86, 30), (108, 50, 1), (92, 70), (84, 100), (80, 64), (20, 64)]), SQUID),
   L(outline([(58, -4), (86, 30), (106, 50), (90, 64), (80, 40)]), _c('#cbd2bc'), 'b', False),
   L(outline([(18, 80), (50, 84), (82, 80), (80, 100), (50, 108), (20, 100)]), SQUID, 'f'),
   L(outline([(84, 86), (100, 80, 1), (96, 92)]), SQUID, 'f'),
   L(quad((26, 74), (36, 70), (46, 74)), _c('#4a6ac8'), 'f', False, False, 2.2), L(quad((54, 74), (64, 70), (74, 74)), _c('#4a6ac8'), 'f', False, False, 2.2),
   L(quad((28, 70), (36, 66), (44, 70)), OUTC, 'f', False, False, 2.0), L(quad((56, 70), (64, 66), (72, 70)), OUTC, 'f', False, False, 2.0)],
  [L(outline([(72, 64), (88, 50), (78, 26), (50, -14, 1), (20, 20), (-4, 44, 1), (4, 80), (20, 100), (40, 96), (56, 70)]), SQUID),
   L(outline([(54, 82), (90, 80), (88, 98), (60, 102)]), SQUID, 'f'), L(outline([(40, 86), (18, 82, 1), (26, 94)]), SQUID, 'f'),
   L(quad((74, 72), (80, 69), (86, 72)), _c('#4a6ac8'), 'f', False, False, 2.2)],
  [L(outline([(16, 100), (8, 70), (-8, 50, 1), (14, 30), (50, -14, 1), (86, 30), (108, 50, 1), (92, 70), (84, 100), (50, 106)]), SQUID),
   L(outline([(44, 86), (30, 98, 1), (50, 92), (70, 98, 1), (56, 86)]), SQUID, 'f')])

# Watson Itfamie: pelo morado en mechones largos de punta echados hacia arriba y hacia un lado, con mechones azul marino
# por debajo, y un flequillo que le tapa el ojo izquierdo; piel pálida, un ojo rojo entornado y media sonrisa
NAVY2 = _c('#3e2f5e')
C('watson-itfamie', 'delgado', P('#a97bae', '#fcf0d8', iris='#c8304a'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=94, face_front=face(chin=106), hairline=[(8, 62), (16, 46), (32, 40), (50, 40), (66, 42), (82, 48), (92, 62)]),
  [L(outline([(10, 84), (2, 50), (-6, 24, 1), (14, 30), (16, 50)]), NAVY2, 'b'), L(outline([(90, 84), (98, 50), (106, 30, 1), (86, 36), (84, 56)]), NAVY2, 'b')] +
  dome('front', top=-2, w=48, cy=46, n=5, amp=20, sweep=1.0, seed=91, sb=72) +
  [L(outline([(46, 30), (68, 34), (82, 52), (82, 82), (70, 94, 1), (64, 74), (54, 60), (48, 44)]), 'mid', 'f'),
   L(outline([(26, 72), (44, 70), (42, 78), (28, 78)]), WHITE, 'f', False), L(ell(36, 75, 3, 3), 'iris', 'f', False),
   L([(25, 72), (45, 70)], OUTC, 'f', False, False, 2.6)],
  dome('side', top=-2, w=48, cy=46, n=5, amp=20, sweep=1.0, seed=91, nape=88, fr=50) + eye_side_n() + [L(outline([(4, 60), (-6, 86, 1), (16, 80)]), NAVY2, 'b')],
  dome('back', top=-2, w=48, cy=46, n=5, amp=20, sweep=1.0, seed=91, nape=88) + [L(outline([(10, 70), (4, 94, 1), (30, 84)]), NAVY2, 'f'),
                                                                               L(outline([(90, 70), (96, 94, 1), (70, 84)]), NAVY2, 'f')])

# Watta Kicker: pelo verde azulado oscuro abultado arriba, con un flequillo de mechones y dos coletas bajas abiertas a los
# lados; guiña un ojo, tirita en la mejilla y boca apretada
C('watta-kicker', 'chica', P('#546f65', '#fcd6af', iris='#c8a030'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=94, hairline=[(8, 64), (16, 52), (28, 60), (36, 50), (50, 58), (62, 50), (72, 60), (84, 52), (92, 64)]),
  bush('front', top=0, w=48, cy=46, n=8, amp=6, seed=95, sb=72) +
  [L(outline([(10, 70), (-6, 82), (-8, 100, 1), (8, 92), (16, 82)]), 'mid', 'b'), L(outline([(90, 70), (106, 82), (108, 100, 1), (92, 92), (84, 82)]), 'mid', 'b'),
   L(outline([(28, 72), (44, 72), (42, 80), (30, 80)]), WHITE, 'f', False), L(ell(37, 76, 3.4, 3.8), 'iris', 'f', False), L(ell(37, 76.5, 1.6, 2), BLACK, 'f', False),
   L([(27, 71), (45, 72)], OUTC, 'f', False, False, 2.6), L(quad((56, 76), (64, 80), (72, 74)), OUTC, 'f', False, False, 2.4),
   L(outline([(58, 84), (72, 82), (74, 90), (60, 92)]), _c('#f2e2d0'), 'f', True)],
  bush('side', top=0, w=48, cy=46, n=8, amp=6, seed=95, nape=84, fr=52) + eye_side_n() + [L(outline([(26, 76), (8, 90), (6, 106, 1), (22, 98), (32, 86)]), 'mid', 'f')],
  bush('back', top=0, w=48, cy=46, n=8, amp=6, seed=95, nape=84) +
  [L(outline([(16, 72), (-6, 82), (-8, 100, 1), (8, 92), (22, 84)]), 'mid', 'f'), L(outline([(84, 72), (106, 82), (108, 100, 1), (92, 92), (78, 84)]), 'mid', 'f')])

# Wick Bowler: una mata enorme de pelo naranja que le tapa los ojos del todo y se abre hasta los hombros; nariz redonda
# grande, pecas y una sonrisa de dientes
C('wick-bowler', 'corpulento', P('#e8661e', '#fdecc1', nose='#e09070'),
  F(eyes='none', brows=False, mouth='none', face_front=face(w=4, chin=104, jaw=3), hairline=[(8, 80), (20, 82), (34, 84), (50, 84), (66, 84), (80, 82), (92, 80)],
    nose=(50, 88, 5)),
  [L(outline([(4, 118, 1), (-6, 80), (-2, 40), (14, 10), (50, -2), (86, 10), (102, 40), (106, 80), (96, 118, 1), (84, 104), (84, 84), (16, 84), (16, 104)])),
   L(outline([(60, 0), (86, 12), (100, 40), (102, 80), (94, 112), (86, 60), (74, 20)]), 'shade', 'b', False),
   L(outline([(16, 74), (34, 82), (50, 80), (66, 82), (84, 74), (84, 86), (50, 88), (16, 86)]), 'mid', 'f'),
   L(outline([(34, 96), (66, 96), (64, 104), (36, 104)]), WHITE, 'f', True)] +
  [L(ell(x, y, 0.9, 0.9), _c('#b4491c'), 'f', False) for x, y in ((28, 92), (32, 95), (25, 96), (72, 92), (68, 95), (75, 96))],
  [L(outline([(70, 86), (84, 82), (94, 62), (96, 30), (80, 6), (50, -2), (20, 6), (2, 30), (-6, 80), (0, 118, 1), (24, 110), (40, 96), (54, 88)])),
   L(outline([(-2, 70), (26, 74), (36, 96), (12, 112)]), 'shade', 'b', False)],
  [L(outline([(4, 118, 1), (-6, 80), (-2, 40), (14, 10), (50, -2), (86, 10), (102, 40), (106, 80), (96, 118, 1), (70, 112), (50, 118), (30, 112)])),
   L(outline([(58, 2), (86, 14), (100, 40), (102, 80), (94, 114), (70, 100)]), 'shade', 'b', False)])

# ------------------------------------------------------------------ (sheet 6)

# Wilfred Cog Coggle: pelo azul pizarra en pinchos cortos alrededor de la cabeza y un pico que le baja por la frente; una
# mascarilla gris azulada le tapa nariz y boca; ojos rojos grandes con el blanco alrededor
MASKG = _c('#8a9ab0')
C('wilfred-cog-coggle', 'normal', P('#515e6e', '#e5d0b4', iris='#c8302a'),
  F(eyes='normal', brows=False, mouth='none', hairline=[(8, 60), (16, 46), (30, 40), (42, 44), (50, 58), (58, 44), (70, 40), (84, 46), (92, 60)]),
  dome('front', top=0, w=48, cy=46, n=10, amp=9, seed=101, sb=66) +
  [L(outline([(22, 82), (50, 80), (78, 82), (76, 96), (60, 104), (40, 104), (24, 96)]), MASKG, 'f'),
   L([(22, 84), (16, 76)], MASKG, 'f', False, False, 1.4), L([(78, 84), (84, 76)], MASKG, 'f', False, False, 1.4)],
  dome('side', top=0, w=48, cy=46, n=10, amp=9, seed=101, nape=86, fr=50) + [L(outline([(60, 82), (90, 80), (90, 96), (70, 104), (60, 98)]), MASKG, 'f'),
                                                                             L([(60, 84), (46, 72)], MASKG, 'f', False, False, 1.4)],
  dome('back', top=0, w=48, cy=46, n=10, amp=9, seed=101, nape=86) + [L([(16, 76), (84, 76)], MASKG, 'f', False, False, 1.4)])

# Will Golightly: casco rojo con dos cuernos y una uve blanca, que le tapa la cabeza hasta la nariz (con un pico en
# medio); se le ven los ojos azules por los huecos y una boca de enfado
HRED = _c('#a81c0e')
C('will-golightly', 'normal', P('#961702', '#f8efd4', iris='#4a7aa8'),
  F(eyes='normal', brows=False, mouth='frown', mouth_y=94, hairline=False),
  [L(outline([(12, 84), (8, 50), (14, 22), (22, 0), (22, -24, 1), (34, 2), (50, -2), (66, 2), (78, -24, 1), (78, 0), (86, 22), (92, 50), (88, 84),
              (80, 66), (66, 66), (56, 74), (50, 90, 1), (44, 74), (34, 66), (20, 66)]), HRED),
   L(outline([(60, 2), (86, 24), (90, 60), (80, 50)]), _c('#751a09'), 'b', False),
   L([(14, 34), (34, 30), (50, 44), (66, 30), (86, 34)], WHITE, 'f', False, False, 3.0)],
  [L(outline([(70, 66), (88, 62), (92, 40), (80, 6), (72, -20, 1), (62, 0), (36, -4), (12, 10), (2, 40), (4, 80), (30, 92), (52, 82)]), HRED),
   L([(6, 34), (40, 28), (88, 40)], WHITE, 'f', False, False, 3.0)],
  [L(outline([(10, 86), (8, 50), (14, 22), (22, 0), (22, -24, 1), (34, 2), (50, -2), (66, 2), (78, -24, 1), (78, 0), (86, 22), (92, 50), (90, 86), (50, 92)]), HRED),
   L(outline([(58, 4), (86, 24), (90, 80), (70, 70)]), _c('#751a09'), 'b', False)])

# Will Lusion: media melena granate liso con la raya a un lado y un flequillo largo que le tapa el ojo izquierdo; un ojo
# grande muy abierto y cara pálida
C('will-lusion', 'normal', P('#7d4255', '#f4ece0', iris='#4a4a4a'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=92, hairline=[(8, 62), (16, 48), (30, 42), (44, 40), (60, 36), (76, 42), (86, 50), (92, 62)]),
  dome('front', top=0, w=48, cy=46, long=92, flare=4) +
  [L(outline([(40, 4), (62, 8), (80, 30), (86, 60), (80, 90, 1), (70, 76), (60, 56), (52, 36)]), 'mid', 'f'),
   L(ell(34, 75, 6.4, 7), WHITE, 'f', True), L(ell(34, 75, 2.6, 2.8), BLACK, 'f', False)],
  dome('side', top=0, w=48, cy=46, long=92, flare=4, fr=46) + [L(ell(83, 75, 3.6, 6), WHITE, 'f', True), L(ell(84, 75, 1.6, 2.4), BLACK, 'f', False)],
  dome('back', top=0, w=48, cy=46, long=92, flare=4, ends=4))

# Wyther Longfeys: cara redondísima y enorme, con un pañuelo verde atado en la frente y pinchos azul marino que asoman por
# encima; ojos de punto y una sonrisa tranquila
GBAND = _c('#a8b850')
C('wyther-longfeys', 'corpulento', P('#4a5a8a', '#fed08b'),
  F(eyes='dot', brows=True, mouth='smile', mouth_y=96, face_front=face(w=10, chin=112, jaw=8, top=20), face_side=face_side(chin=10, jaw=8), ear_out=8,
    hairline=[(6, 56), (16, 50), (34, 48), (50, 48), (66, 48), (84, 50), (94, 56)]),
  [L(outline([(20, 34), (24, 8), (34, -8, 1), (44, 6), (56, -12, 1), (62, 6), (78, -4, 1), (76, 14), (82, 34), (50, 30)]))] +
  [L(outline([(8, 58), (12, 34), (30, 26), (50, 24), (70, 26), (88, 34), (92, 58), (50, 52)]), GBAND, 'b', True),
   L(outline([(30, 30), (50, 28), (70, 30), (88, 40), (86, 52), (64, 40), (40, 42), (14, 50), (14, 40)]), _c('#8a9a38'), 'b', False)],
  [L(outline([(30, 30), (34, 6), (48, -10, 1), (54, 6), (68, -6, 1), (70, 14), (86, 8, 1), (80, 30)])),
   L(outline([(0, 56), (4, 30), (40, 20), (80, 24), (92, 36), (90, 52), (40, 50)]), GBAND, 'b', True), L(outline([(4, 40), (-10, 52, 1), (6, 54)]), GBAND, 'b', True)],
  [L(outline([(20, 34), (24, 8), (34, -8, 1), (44, 6), (56, -12, 1), (62, 6), (78, -4, 1), (76, 14), (82, 34), (50, 30)])),
   L(outline([(6, 60), (10, 34), (50, 24), (90, 34), (94, 60), (50, 56)]), GBAND, 'b', True),
   L(outline([(44, 56), (36, 70, 1), (50, 62), (64, 70, 1), (56, 56)]), GBAND, 'f', True)])

# Xander Noddle: sombrero gris oscuro ancho y plano, con una cinta de tela en la frente y una placa metálica en medio;
# melena oscura por detrás hasta el cuello; cara larga, nariz larga, ojos afilados y ceño
HAT = _c('#4d4b47')
C('xander-noddle', 'delgado', P('#3e322a', '#fabb7e', iris='#1e1a1a'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=98, face_front=face(chin=110), face_side=face_side(chin=8, nose=4), hairline=False),
  [L(outline([(-6, 30), (6, 4), (50, -4), (94, 4), (106, 30), (90, 34), (50, 30), (10, 34)]), HAT),
   L(outline([(16, 40), (50, 34), (84, 40), (84, 56), (50, 50), (16, 56)]), _c('#d9c8a8'), 'b', True),
   L(outline([(38, 34), (62, 34), (64, 50), (50, 56), (36, 50)]), _c('#c8cccc'), 'b', True),
   L(ell(44, 42, 1.2, 1.2), _c('#8a8a8a'), 'b', False), L(ell(56, 42, 1.2, 1.2), _c('#8a8a8a'), 'b', False),
   L(quad((50, 70), (46, 86), (52, 90)), OUTC, 'f', False, False, 1.4)],
  [L(outline([(-4, 30), (6, 4), (46, -4), (92, 4), (104, 28), (90, 34), (46, 30), (6, 36)]), HAT),
   L(outline([(6, 40), (86, 36), (86, 52), (6, 58)]), _c('#d9c8a8'), 'b', True), L(outline([(4, 52), (2, 96), (22, 106), (40, 74), (30, 56)]))],
  [L(outline([(10, 100), (8, 50), (92, 50), (90, 100), (50, 106)])),
   L(outline([(-6, 30), (6, 4), (50, -4), (94, 4), (106, 30), (90, 34), (50, 30), (10, 34)]), HAT),
   L(outline([(12, 40), (88, 40), (88, 54), (12, 54)]), _c('#d9c8a8'), 'b', True)])

# Xanthe Crosse: pelo negro recogido, con dos moños como orejas encima de la cabeza y dos bolitas abajo a los lados; ojos
# castaños grandes y enfadados, pecas en las mejillas y boca seria
C('xanthe-crosse', 'chica', P('#362f29', '#fbcfa0', iris='#a86a1e'),
  F(eyes='big', brows='angry', mouth='frown', mouth_y=94, hairline=[(8, 60), (18, 50), (34, 46), (46, 50), (50, 56), (54, 50), (66, 46), (82, 50), (92, 60)]),
  crop('front', top=4, side=66) +
  [L(ell(22, -2, 13, 14), 'mid', 'b'), L(ell(78, -2, 13, 14), 'mid', 'b'),
   L(ell(10, 92, 8, 7), 'mid', 'b'), L(ell(90, 92, 8, 7), 'mid', 'b')] +
  [L(ell(x, y, 0.9, 0.9), _c('#c8784a'), 'f', False) for x, y in ((30, 86), (34, 88), (66, 86), (70, 88))],
  crop('side', top=4) + [L(ell(36, -2, 12, 14), 'mid', 'b'), L(ell(30, 92, 8, 7), 'mid', 'b')],
  crop('back', top=4) + [L(ell(22, -2, 13, 14), 'mid', 'b'), L(ell(78, -2, 13, 14), 'mid', 'b'), L(ell(14, 92, 8, 7), 'mid', 'f'), L(ell(86, 92, 8, 7), 'mid', 'f')])
