"""Ojeadores de GO (scouts-go), tanda 03: dibujados a partir de su retrato de Victory Road; claves 'scouts-go:<id>'.

Ninguno tiene modelo 3D propio: el frente sale del retrato y el perfil y la espalda se deducen de cómo cae ese peinado.
Se reutilizan las ayudas de las tandas de IE (dome/hl/face de ie1_09, bowl/rect_specs/round_specs/blush/thick_brows de
ie1_03, hood/ring/skull3/bowl3 de ie3_02)."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, rope, strand  # noqa: F401
from heads import FACE_FRONT, quad  # noqa: F401
from chars_scouts_ie1_09 import dome, hl, face, face_side, F, P, mark, _c  # noqa: F401
from chars_scouts_ie1_03 import big_grin, bowl, rect_specs, round_specs, blush, thick_brows, side_brow, freckles, eyes_custom, side_eye_custom  # noqa: F401
from chars_scouts_ie3_02 import hood, ring, skull3, bowl3, scarf  # noqa: F401

WHITE = (248, 248, 248, 255)
BLACK = (30, 26, 30, 255)


def C(pid, body, palette, f, front, side, back):
    hl_ = f.get('hairline')
    if isinstance(hl_, list) and len(hl_) > 2:
        # el nacimiento del pelo baja por el borde de la cara: así su raya no cruza el pelo de los lados
        xs = [p[0] for p in f.get('face_front', FACE_FRONT) if 56 <= p[1] <= 96]
        f['hairline'] = [(min(xs) + 0.6, 104)] + hl_[1:-1] + [(max(xs) - 0.6, 104)]
    CHARS[f'scouts-go:{pid}'] = {'body': body, 'pal': palette, 'face': f, 'front': front, 'side': side, 'back': back}


def loop(pts, c, w=2.4, z='f'):
    """Raya cerrada (aros, cintas)."""
    return L(pts + [pts[0]], c, z, False, False, w)


def mirx(pts):
    return [(100 - p[0], p[1]) + tuple(p[2:]) for p in pts]


# ------------------------------------------------------------------ jugadores

# Deece Lightning: pañuelo naranja que le tapa la cabeza, con una venda blanca cruzada por la derecha y el nudo colgando a
# la izquierda; flequillo rubio por debajo, ojos grandes verde agua y sonrisa
WH = _c('#f4f2ea')
def _deece(view):
    if view == 'front':
        return [L(outline([(10, 62), (8, 40), (18, 18), (36, 6), (56, 4), (76, 10), (90, 28), (92, 50), (88, 62), (70, 52), (40, 50), (20, 56)])),
                L(outline([(48, 8), (62, 4), (88, 30), (92, 52), (86, 60), (80, 56), (76, 36)]), WH, 'b', False),
                L(outline([(14, 48), (6, 60), (-4, 80, 1), (8, 70), (10, 86, 1), (18, 62)]), 'mid', 'f'),
                L(outline([(18, 54), (30, 50), (44, 52), (42, 64, 1), (36, 56), (28, 68, 1), (24, 56)]), 'light', 'f')]
    if view == 'side':
        return [L(outline([(54, 58), (60, 48), (80, 46), (94, 34), (90, 14), (70, 2), (40, 0), (16, 10), (4, 30), (2, 52), (10, 66), (28, 64), (44, 58)])),
                L(outline([(58, 4), (70, 4), (92, 32), (92, 42), (82, 44)]), WH, 'b', False),
                L(outline([(8, 46), (-6, 58), (-14, 80, 1), (-2, 66), (-4, 88, 1), (10, 60)]), 'mid', 'f')]
    return [L(outline([(10, 72), (6, 40), (18, 14), (50, 2), (82, 14), (94, 40), (90, 72), (50, 76)])),
            L(outline([(60, 6), (74, 10), (94, 40), (92, 60), (84, 44)]), WH, 'b', False),
            L(outline([(40, 62), (30, 70), (22, 94, 1), (36, 78), (40, 98, 1), (46, 70)]), 'mid', 'f')]
C('deece-lightning', 'chica', P('#efb441', '#fbcfa1', iris='#3a9a96', light='#f4d670', shade='#c88a2a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(8, 66), (16, 56), (30, 52), (50, 50), (70, 52), (84, 56), (92, 66)]),
  _deece('front'), _deece('side'), _deece('back'))

# Del Aket: dos bolas enormes de pelo negro a los lados y un moño de sumo con un aro crema y dos palos encima; piel morena,
# nariz roja, cejas furiosas y dientes apretados
CR = _c('#e8dcae')
def _delaket(view):
    sticks = [L(outline([(30, 8), (44, 6), (44, 12), (30, 14)]), CR), L(outline([(70, 8), (56, 6), (56, 12), (70, 14)]), CR), loop(ell(50, 2, 6, 6), CR, 3.0)]
    if view == 'front':
        return [L(ell(6, 66, 20, 22)), L(ell(94, 66, 20, 22)),
                L(outline([(14, 60), (16, 36), (30, 18), (50, 12), (70, 18), (84, 36), (86, 60), (70, 50), (30, 50)]))] + sticks
    if view == 'side':
        return [L(ell(30, 66, 24, 25)),
                L(outline([(54, 58), (58, 46), (80, 42), (90, 28), (80, 12), (56, 4), (30, 8), (12, 24), (8, 46), (20, 60), (40, 60)])),
                L(outline([(40, 6), (60, 4), (60, 10), (42, 12)]), CR), loop(ell(48, 0, 6, 6), CR, 3.0)]
    return [L(ell(6, 68, 20, 22)), L(ell(94, 68, 20, 22)),
            L(outline([(12, 74), (10, 40), (24, 18), (50, 10), (76, 18), (90, 40), (88, 74), (50, 80)]))] + sticks
C('del-aket', 'corpulento', P('#2e2a2e', '#ae8a64', iris='#1a1414', nose='#d24a34'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=95, nose=(50, 85, 3.6), face_front=face(w=4, jaw=3), hairline=[(8, 62), (20, 52), (50, 50), (80, 52), (92, 62)]),
  _delaket('front'), _delaket('side'), _delaket('back'))

# Delia "Psyche" Sykes: pelo rojo con mechones blancos a la izquierda y un pico de flequillo en medio; dos coletas bajas
# muy abultadas, rojas y blancas; ojos verde azulado y sonrisa
def _psyche(view):
    tails = lambda xs: sum(([L(ell(x, 86, 11, 12)), L(blob([(x - 8, 80), (x + 2, 76), (x + 6, 86), (x - 4, 92)], 4), WHITE, 'b', False)] for x in xs), [])
    if view == 'front':
        return tails((8, 92)) + [L(outline([(16, 64), (12, 40), (20, 18), (36, 6), (50, 4), (64, 6), (80, 18), (88, 40), (84, 64), (76, 50), (24, 50)])),
                                 L(outline([(14, 44), (22, 16), (36, 6), (42, 8), (28, 30), (20, 54)]), WHITE, 'b', False)]
    if view == 'side':
        return tails((30,)) + [L(outline([(56, 56), (62, 46), (82, 44), (94, 30), (88, 12), (64, 0), (36, 2), (14, 14), (4, 36), (6, 56), (22, 66), (40, 62)])),
                               L(outline([(40, 4), (56, 2), (40, 30), (24, 42), (18, 30)]), WHITE, 'b', False)]
    return tails((8, 92)) + [L(outline([(12, 70), (8, 40), (20, 16), (50, 4), (80, 16), (92, 40), (88, 70), (50, 74)])),
                             L(outline([(70, 8), (84, 18), (92, 44), (84, 58), (76, 30)]), WHITE, 'b', False)]
C('delia-psyche-sykes', 'chica', P('#c41e10', '#f9bb7c', iris='#2a8aa8', shade='#901810'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=92, hairline=[(8, 66), (20, 52), (34, 48), (50, 60), (66, 48), (80, 52), (92, 66)]),
  _psyche('front'), _psyche('side'), _psyche('back'))

# Deliah "Dazzle" Azel: melena lisa castaño oscuro hasta los hombros con flequillo recto y una diadema dorada; piel muy
# clara y ojos grandes rojos
GOLD = _c('#c8a050')
C('deliah-dazzle-azel', 'chica', P('#401808', '#f5ecc7', iris='#c01818'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, hairline=[(8, 70), (16, 62), (50, 62), (84, 62), (92, 70)]),
  dome('front', top=2, w=46, cy=46, long=118, flare=4) + [L(quad((8, 32), (50, 14), (92, 32)), GOLD, 'f', False, False, 2.6)],
  dome('side', top=2, w=46, cy=46, long=118, flare=4, fr=60) + [L(quad((70, 6), (40, 2), (12, 26)), GOLD, 'f', False, False, 2.6)],
  dome('back', top=2, w=46, cy=46, long=118, flare=4, ends=4) + [L(quad((8, 32), (50, 14), (92, 32)), GOLD, 'f', False, False, 2.6)])

# Dennis Tistry: señor de cabeza redonda con un gorro de quirófano verde menta, una barba enorme del mismo color que le
# tapa la boca, gafitas redondas negras, nariz gorda y orejotas
MINT, MINT_D = _c('#b8dccc'), _c('#8aa898')
C('dennis-tistry', 'corpulento', P('#b8dccc', '#fbce89', iris='#1a1414', shade='#8aa898'),
  F(eyes='none', brows=False, mouth='none', mouth_y=96, hairline=False, nose=(50, 84, 4.2), big_ears=3, ear_out=6, face_front=face(w=4, chin=106, jaw=2)),
  [L(outline([(18, 46), (22, 26), (36, 16), (50, 14), (64, 16), (78, 26), (82, 46), (50, 42)])),
   L(outline([(15, 74), (30, 82), (50, 86), (70, 82), (85, 74), (84, 96), (68, 110), (50, 114), (32, 110), (16, 96)]), MINT, 'f'),
   L(outline([(20, 96), (34, 108), (50, 112), (66, 108), (80, 96), (68, 104), (50, 108), (32, 104)]), MINT_D, 'f', False),
   L(ell(42, 74, 4.6, 4.6), BLACK, 'f', False), L(ell(58, 74, 4.6, 4.6), BLACK, 'f', False), L([(46, 73), (54, 73)], BLACK, 'f', False, False, 1.4),
   L(ell(41, 72.6, 1.2, 1.2), WHITE, 'f', False), L(ell(57, 72.6, 1.2, 1.2), WHITE, 'f', False)],
  [L(outline([(26, 32), (44, 16), (68, 16), (86, 30), (86, 42), (40, 46)])),
   L(outline([(56, 76), (88, 78), (90, 94), (80, 108), (62, 110), (50, 98)]), MINT, 'f'),
   L(ell(82, 74, 4.2, 4.6), BLACK, 'f', False)],
  [L(outline([(14, 46), (22, 24), (50, 14), (78, 24), (86, 46), (50, 48)]))])

# Des Eving: pelo crema plateado peinado hacia atrás con un mechón en antena muy alto; gafas rojas, ojos ámbar y pecas
RED = _c('#c82a32')
C('des-eving', 'normal', P('#dcd8c8', '#fdf0d5', iris='#c8901e', shade='#b8b4a2', deep='#8a8676'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=92, hairline=[(8, 64), (18, 50), (34, 42), (50, 40), (66, 42), (82, 50), (92, 64)]),
  dome('front', top=4, w=44, cy=46, sb=64) + [L(outline([(46, 8), (42, -12), (56, -28, 1), (50, -10), (54, 8)])),
                                             strand([(30, 14), (36, 38)], 'deep', 'f'), strand([(70, 14), (64, 38)], 'deep', 'f')] +
  rect_specs('front', RED) + freckles(86, 24),
  dome('side', top=4, w=44, cy=46, nape=86, fr=44) + [L(outline([(52, 6), (46, -12), (60, -28, 1), (56, -10), (60, 6)]))] + rect_specs('side', RED),
  dome('back', top=4, w=44, cy=46, nape=86) + [L(outline([(46, 8), (42, -12), (56, -28, 1), (50, -10), (54, 8)]))])

# Devin Hornes: melena negra lisa con raya en medio que le cae hasta el pecho; cara larga muy pálida, ojos de mirada fija
# con el iris rojo oscuro y boca seria
C('devin-hornes', 'delgado', P('#2e2a26', '#e2ccad', iris='#7a1a26', shade='#1e1a18', deep='#141210'),
  F(eyes='normal', brows='angry', mouth='frown', mouth_y=97, face_front=face(chin=108, w=-2), face_side=face_side(chin=6),
    hairline=[(6, 70), (14, 56), (30, 44), (50, 32), (70, 44), (86, 56), (94, 70)]),
  dome('front', top=0, w=44, cy=46, long=122, flare=2) + [strand([(50, 0), (50, 30)], 'deep', 'f')],
  dome('side', top=0, w=44, cy=46, long=122, flare=2, fr=56),
  dome('back', top=0, w=44, cy=46, long=122, flare=2, ends=3) + [strand([(50, 2), (50, 40)], 'deep', 'f')])

# Dexter Poine: cara redonda y gorda con mofletes rosas; pelo castaño en casco con raya a un lado; gafas azules
# rectangulares sobre unos ojos cerrados y boca enfurruñada
BLUE = _c('#4a5aa0')
C('dexter-poine', 'corpulento', P('#5a4a36', '#fbd18c', iris='#1a1414', shade='#3e3224'),
  F(eyes='closed', brows=True, mouth='frown', mouth_y=94, face_front=face(w=4, jaw=2),
    hairline=[(8, 66), (16, 56), (30, 50), (44, 52), (60, 56), (74, 54), (84, 56), (92, 66)]),
  dome('front', top=10, w=44, cy=48, sb=70) + [strand([(34, 14), (40, 36)], 'deep', 'f')] + rect_specs('front', BLUE) + blush(88, 24, 5),
  dome('side', top=10, w=44, cy=48, nape=86, fr=50) + rect_specs('side', BLUE),
  dome('back', top=10, w=44, cy=48, nape=86))

# Dias "Diamond" Mondragon (portero): pelo gris plateado en casco con flequillo recto que le tapa las cejas; ojos verde
# agua con un destello de diamante
C('dias-diamond-mondragon', 'normal', P('#cfd4d9', '#fdf3dd', iris='#7ab8b0', shade='#a8aeb4', deep='#8a9096'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, hairline=[(8, 68), (16, 64), (50, 64), (84, 64), (92, 68)]),
  dome('front', top=2, w=46, cy=46, sb=76) + [L([(33, 75), (39, 75)], WHITE, 'f', False, False, 1.2), L([(36, 72), (36, 78)], WHITE, 'f', False, False, 1.2),
                                             L([(61, 75), (67, 75)], WHITE, 'f', False, False, 1.2), L([(64, 72), (64, 78)], WHITE, 'f', False, False, 1.2)],
  dome('side', top=2, w=46, cy=46, nape=88, fr=62),
  dome('back', top=2, w=46, cy=46, nape=88))

# Dilly Honeywell: capucha blanca de gato con orejas (una naranja) y dos parches redondos naranjas; asoma pelo rojo
# coral con rizos hacia fuera y flequillo rubio; piel morena, ojos rojos y un cascabel dorado al cuello
CRM, CRM_D, ORG, YEL2 = _c('#f4f0e2'), _c('#d8d2c0'), _c('#e8742c'), _c('#f8f088')
def _dilly(view):
    if view == 'front':
        return [L(outline([(18, 50), (82, 50), (88, 98), (78, 94), (22, 94), (12, 98)]), 'mid', 'b'),
                L(outline([(34, 44), (66, 44), (64, 62), (50, 64), (36, 62)]), YEL2, 'b'),
                L(outline([(10, 66), (-2, 58), (-6, 66), (0, 72), (6, 70)]), 'mid', 'f'), L(outline(mirx([(10, 66), (-2, 58), (-6, 66), (0, 72), (6, 70)])), 'mid', 'f')] + \
               hood('front', CRM, top=0, rim=CRM_D, face_hole=[(20, 100), (16, 72), (22, 48), (50, 40), (78, 48), (84, 72), (80, 100), (50, 106)]) + \
               [L(outline([(16, 20), (12, -16, 1), (40, 8)]), ORG), L(outline([(84, 20), (88, -16, 1), (60, 8)]), CRM),
                L(ell(26, 32, 7, 7), ORG, 'f'), L(ell(74, 32, 7, 7), ORG, 'f'), L(ell(50, 110, 4.4, 4.4), GOLD, 'f')]
    if view == 'side':
        return hood('side', CRM, top=0, rim=CRM_D) + [L(outline([(40, 8), (36, -18, 1), (60, 4)]), ORG), L(ell(30, 34, 7, 7), ORG, 'f'),
                                                     L(outline([(70, 60), (84, 58), (82, 96), (72, 92)]), 'mid', 'f')]
    return hood('back', CRM, top=0, rim=CRM_D) + [L(outline([(16, 20), (12, -16, 1), (40, 8)]), ORG), L(outline([(84, 20), (88, -16, 1), (60, 8)]), CRM),
                                                 L(ell(30, 40, 7, 7), ORG, 'f')]
C('dilly-honeywell', 'chica', P('#e26550', '#bc9475', iris='#b8301e', shade='#a84a3a'),
  F(eyes='normal', brows=True, mouth='smile', mouth_y=92, hairline=[(8, 66), (20, 58), (36, 62), (50, 64), (64, 62), (80, 58), (92, 66)]),
  _dilly('front'), _dilly('side'), _dilly('back'))

# Dirk Eisberg: pelo blanco plateado en pinchos que suben en una cresta altísima con una raya azul en medio; ojos azules
# afilados con sombra morada y sonrisa pícara
BLU = _c('#2a64c8')
C('dirk-eisberg', 'normal', P('#dce2e7', '#fdf0d5', iris='#2a5ab8', shade='#b4bcc4', deep='#8a929a'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=92, hairline=[(8, 64), (18, 52), (34, 48), (50, 58), (66, 48), (82, 52), (92, 64)]),
  [L(outline([(14, 62), (10, 42), (2, 30, 1), (16, 26), (10, 8, 1), (26, 14), (40, -4), (58, -32, 1), (54, -6), (66, 8), (80, 2, 1), (76, 18), (92, 22, 1),
              (86, 36), (86, 62), (78, 48), (22, 48)])),
   L(outline([(58, -6), (66, 8), (80, 2), (76, 18), (92, 22), (86, 36), (86, 60), (76, 34)]), 'shade', 'b', False),
   L(outline([(44, 48), (48, 20), (56, -26), (58, -32), (54, -4), (54, 20), (52, 48)]), BLU, 'b', False)],
  [L(outline([(56, 56), (60, 44), (80, 40), (96, 24, 1), (84, 22), (86, 6), (70, -6), (66, -32, 1), (54, -6), (40, 2), (20, 8), (6, 24), (4, 46), (14, 60), (34, 62), (46, 56)])),
   L(outline([(48, 40), (58, 10), (66, -30), (62, -6), (56, 14), (52, 40)]), BLU, 'b', False)],
  [L(outline([(14, 72), (10, 40), (22, 14), (44, 0), (58, -30, 1), (60, -2), (78, 12), (90, 40), (86, 72), (50, 78)])),
   L(outline([(47, 72), (51, 20), (58, -26), (57, 4), (55, 40), (54, 72)]), BLU, 'b', False)])

# Dirk Point: pelo verde oliva oscuro largo hasta la barbilla, en mechones que le caen por la cara y tapan medio ojo;
# mascarilla azul clara y un solo ojo gris a la vista
MASK = _c('#d4e8f0')
def _dpoint(view):
    if view == 'front':
        return dome('front', top=2, w=46, cy=46, long=100, flare=2) + [
            L(outline([(18, 84), (50, 80), (82, 84), (78, 100), (50, 110), (22, 100)]), MASK, 'f'),
            L(outline([(26, 48), (42, 50), (40, 90, 1), (32, 70), (24, 92, 1)]), 'mid', 'f'),
            L(outline([(60, 48), (70, 50), (72, 94, 1), (64, 70)]), 'mid', 'f'),
            strand([(30, 20), (34, 60)], 'deep', 'f'), strand([(66, 20), (66, 70)], 'deep', 'f')]
    if view == 'side':
        return dome('side', top=2, w=46, cy=46, long=100, flare=2, fr=64) + [L(outline([(56, 84), (88, 82), (88, 96), (78, 106), (60, 104)]), MASK, 'f'),
                                                                             L([(56, 84), (46, 72)], BLACK, 'f', False, False, 1.0)]
    return dome('back', top=2, w=46, cy=46, long=100, flare=2, ends=4)
C('dirk-point', 'normal', P('#4f5623', '#e8d8c8', iris='#8a96a0', shade='#3a4018', deep='#262a10'),
  F(eyes='sharp', brows=False, mouth='none', mouth_y=96, hairline=[(8, 70), (18, 54), (34, 48), (50, 50), (66, 48), (82, 54), (92, 70)]),
  _dpoint('front'), _dpoint('side'), _dpoint('back'))

# Don Capo: melena salvaje granate oscuro con mechones rojos por debajo y dos picos como cuernos arriba; ojos redondos
# furiosos
RED2 = _c('#b0383a')
C('don-capo', 'normal', P('#3d272b', '#f3c391', iris='#5a1a1a', shade='#2a1a1e', deep='#1e1214'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=92, hairline=hl(6, 66, 48, 62, jit=3, seed=4)),
  dome('front', top=0, w=48, cy=46, n=8, amp=8, long=112, flare=8, seed=3) +
  [L(outline([(18, 24), (10, -14, 1), (34, 10)])), L(outline([(82, 24), (90, -14, 1), (66, 10)])),
   L(outline([(8, 60), (20, 56), (16, 100, 1)]), RED2, 'b', False), L(outline([(92, 60), (80, 56), (84, 100, 1)]), RED2, 'b', False),
   L(outline([(26, 50), (38, 48), (30, 66, 1)]), RED2, 'b', False), L(outline([(74, 50), (62, 48), (70, 66, 1)]), RED2, 'b', False)],
  dome('side', top=0, w=48, cy=46, n=8, amp=8, long=112, flare=8, seed=3, fr=56) + [L(outline([(40, 10), (40, -18, 1), (58, 6)])),
                                                                                  L(outline([(10, 66), (26, 64), (14, 104, 1)]), RED2, 'f')],
  dome('back', top=0, w=48, cy=46, n=8, amp=8, long=112, flare=8, seed=3, ends=5) +
  [L(outline([(18, 24), (10, -14, 1), (34, 10)])), L(outline([(82, 24), (90, -14, 1), (66, 10)])),
   L(outline([(30, 70), (40, 66), (36, 108, 1)]), RED2, 'f'), L(outline([(70, 70), (60, 66), (64, 108, 1)]), RED2, 'f')])

# Don Prima: peinado de kabuki con un moño negro arriba y rulos gordos a los lados; cara blanca con maquillaje rojo (una
# uve en la frente y rayas en los ojos), ojos cerrados y labios rojos apretados
KR = _c('#c8303a')
def _rolls(xs):
    return [L(ell(x, y, 10, 9)) for x in xs for y in (46, 64, 82)]
C('don-prima', 'corpulento', P('#343b46', '#fdefd5', iris='#1a1414', shade='#262c34'),
  F(eyes='closed', brows=False, mouth='lips', mouth_w=11, mouth_y=95, hairline=[(8, 58), (20, 50), (50, 48), (80, 50), (92, 58)], face_front=face(w=4, jaw=3)),
  _rolls((8, 92)) + [L(ell(50, 4, 14, 12)), L(outline([(16, 56), (18, 30), (32, 14), (50, 10), (68, 14), (82, 30), (84, 56), (50, 48)])),
                     L([(38, 52), (50, 66), (62, 52)], KR, 'f', False, False, 2.4),
                     L(quad((22, 72), (34, 62), (46, 70)), KR, 'f', False, False, 2.2), L(quad((78, 72), (66, 62), (54, 70)), KR, 'f', False, False, 2.2),
                     L(quad((26, 82), (36, 86), (44, 82)), KR, 'f', False, False, 1.6), L(quad((74, 82), (64, 86), (56, 82)), KR, 'f', False, False, 1.6)],
  [L(ell(30, 46, 10, 9)), L(ell(26, 64, 10, 9)), L(ell(30, 82, 10, 9)), L(ell(46, 0, 13, 11)),
   L(outline([(54, 54), (60, 40), (82, 36), (86, 22), (66, 8), (36, 8), (16, 22), (12, 46), (30, 56)])),
   L(quad((72, 70), (80, 62), (88, 68)), KR, 'f', False, False, 2.2)],
  _rolls((10, 90)) + [L(ell(50, 4, 14, 12)), L(outline([(14, 74), (14, 30), (32, 12), (50, 8), (68, 12), (86, 30), (86, 74), (50, 84)]))] +
  [L(ell(50, 78, 10, 8))])

# Donald "Don" Hooan: melena en casco azul verdoso con flequillo recto y mechas negras a los lados, hasta la mandíbula;
# guiña un ojo
def _wink():
    return [L(ell(36, 75, 7.5, 8), 'skin', 'f', False), L(quad((29, 77), (36, 72), (43, 77)), OUTC, 'f', False, False, 2.2)]
C('donald-don-hooan', 'normal', P('#4a8aa4', '#fbf2dc', iris='#8a7a3a', shade='#2e6a84', deep='#121c22'),
  F(eyes='sharp', brows=False, mouth='line', mouth_y=93, hairline=[(8, 70), (16, 62), (50, 62), (84, 62), (92, 70)]),
  dome('front', top=2, w=46, cy=46, long=98, flare=0) + [L(outline([(10, 40), (16, 38), (14, 96), (8, 96)]), 'deep', 'b', False), L(outline([(90, 40), (84, 38), (86, 96), (92, 96)]), 'deep', 'b', False)] + _wink(),
  dome('side', top=2, w=46, cy=46, long=98, flare=0, fr=62) + [L(outline([(28, 24), (34, 26), (22, 94), (16, 92)]), 'deep', 'b', False)],
  dome('back', top=2, w=46, cy=46, long=98, flare=0, ends=4))

# Donna Hooan: media melena rubia con flequillo recto y dos trenzas finas que bajan por los lados de la cara; ojos grandes
# azules y sonrisa
def _braids(x0, y0=50, y1=94):
    return [L(ell(x0, y, 4.2, 4.2), 'shade', 'f') for y in range(y0, y1, 7)]
C('donna-hooan', 'chica', P('#f9e58b', '#facf9e', iris='#2a90c8', shade='#d4b25e', deep='#a8864a'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=[(8, 70), (16, 62), (50, 62), (84, 62), (92, 70)]),
  dome('front', top=2, w=46, cy=46, long=98, flare=4) + _braids(16) + _braids(84),
  dome('side', top=2, w=46, cy=46, long=98, flare=4, fr=62) + _braids(54, 56, 96),
  dome('back', top=2, w=46, cy=46, long=98, flare=4, ends=4))

# Dos Lightning: pinchos blancos de punta arriba y pinchos negros que salen a los lados, patillas blancas; piel morena,
# ojos rojos afilados con cejas negras gruesas y boca seria
C('dos-lightning', 'normal', P('#efeae4', '#cc946a', iris='#b81e1e', shade='#c8c0b8', deep='#8a827a'),
  F(eyes='sharp', brows=False, mouth='frown', mouth_y=93, hairline=[(8, 62), (18, 50), (34, 46), (50, 52), (66, 46), (82, 50), (92, 62)]),
  [L(outline([(14, 58), (0, 40, 1), (12, 40), (2, 24, 1), (18, 30), (22, 52)]), BLACK), L(outline(mirx([(14, 58), (0, 40, 1), (12, 40), (2, 24, 1), (18, 30), (22, 52)])), BLACK),
   L(outline([(16, 50), (12, 30), (18, 6, 1), (28, 20), (32, -8, 1), (42, 12), (54, -16, 1), (56, 8), (70, -8, 1), (68, 16), (86, 6, 1), (82, 30), (84, 50), (70, 44), (30, 44)])),
   L(outline([(60, 2), (70, -8), (68, 16), (86, 6), (82, 30), (84, 48), (74, 30)]), 'shade', 'b', False),
   L(outline([(17, 62), (23, 62), (23, 84), (17, 80)]), 'mid', 'f'), L(outline([(83, 62), (77, 62), (77, 84), (83, 80)]), 'mid', 'f')] +
  thick_brows(63, BLACK, 4.0, 14, 1.2, 13),
  [L(outline([(12, 50), (-6, 40, 1), (6, 36), (-4, 20, 1), (14, 26), (24, 46)]), BLACK),
   L(outline([(56, 50), (60, 40), (80, 38), (96, 20, 1), (84, 18), (90, -2, 1), (72, 4), (70, -16, 1), (56, 0), (42, -10, 1), (36, 6), (20, 8), (10, 24), (8, 44), (22, 54), (40, 54)])),
   L(outline([(56, 62), (62, 62), (60, 84), (54, 80)]), 'mid', 'f')] + side_brow(63, BLACK, 4.0, 1.2),
  [L(outline([(14, 58), (0, 40, 1), (12, 40), (2, 24, 1), (18, 30), (22, 52)]), BLACK), L(outline(mirx([(14, 58), (0, 40, 1), (12, 40), (2, 24, 1), (18, 30), (22, 52)])), BLACK),
   L(outline([(14, 76), (12, 30), (18, 6, 1), (28, 20), (32, -8, 1), (42, 12), (54, -16, 1), (56, 8), (70, -8, 1), (68, 16), (86, 6, 1), (82, 30), (86, 76), (50, 82)]))])

# Doug Spoddy: capucha negra que le tapa toda la cabeza, con dos ojos redondos blancos y una sonrisa dibujados, y encima un
# sombrero negro de ala ancha y plana; asoman las orejas
HD, BR = _c('#474a4d'), _c('#36383b')
def _spoddy(view):
    if view == 'front':
        return [L(outline([(10, 22), (90, 22), (90, 96), (80, 112), (20, 112), (10, 96)]), HD, 'f'),
                L(outline([(-6, 20), (4, 6), (50, 2), (96, 6), (106, 20), (50, 26)]), BR, 'f'),
                L(ell(36, 66, 7.5, 7.5), WHITE, 'f'), L(ell(36, 66, 4.2, 4.2), BLACK, 'f', False), L(ell(64, 66, 7.5, 7.5), WHITE, 'f'), L(ell(64, 66, 4.2, 4.2), BLACK, 'f', False),
                L(quad((38, 84), (50, 96), (62, 84)), BLACK, 'f', False, False, 2.0)]
    if view == 'side':
        return [L(outline([(18, 22), (86, 22), (92, 96), (82, 112), (30, 112), (14, 92)]), HD, 'f'),
                L(outline([(-8, 14), (10, 4), (60, 0), (106, 8), (98, 20), (50, 22)]), BR, 'f'),
                L(ell(82, 66, 5.5, 7), WHITE, 'f'), L(ell(84, 66, 3, 4), BLACK, 'f', False), L(quad((76, 90), (84, 94), (90, 88)), BLACK, 'f', False, False, 1.8)]
    return [L(outline([(10, 22), (90, 22), (92, 100), (50, 112), (8, 100)]), HD, 'f'), L(outline([(-6, 20), (4, 6), (50, 2), (96, 6), (106, 20), (50, 26)]), BR, 'f')]
C('doug-spoddy', 'normal', P('#474a4d', '#f1c79b', iris='#1a1414'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears_front=True, ear_out=3), _spoddy('front'), _spoddy('side'), _spoddy('back'))

# Dougal Axe: grandullón de piel morena con una mata de pelo castaño oscuro rizado y dos hojas de hacha grises que le salen
# a los lados de la cabeza; nariz grande, ojos pequeños enfadados y morros
AXE, AXE_D, NOSE = _c('#b8b4ae'), _c('#8a8680'), _c('#765b50')
def _axes(view):
    a = [(16, 24), (2, 30), (-8, 50), (-4, 72), (4, 90), (12, 74), (6, 56), (10, 40), (22, 34)]
    if view == 'side':
        return [L(outline([(30, 20), (16, 26), (6, 46), (10, 70), (20, 86), (26, 68), (20, 50), (24, 36), (36, 30)]), AXE)]
    return [L(outline(a), AXE), L(outline(mirx(a)), AXE), L(outline([(2, 34), (-4, 50), (-2, 70), (2, 80), (2, 56), (8, 38)]), AXE_D, 'b', False)]
C('dougal-axe', 'corpulento', P('#3b3834', '#bc8c69', iris='#1a1414', shade='#2a2826'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=96, face_front=face(w=5, jaw=3), hairline=hl(6, 60, 48, 54, jit=2, seed=9)),
  _axes('front') + dome('front', top=6, w=44, cy=44, n=10, amp=5, soft=True, sb=60, seed=5) + [L(blob([(43, 78), (57, 78), (59, 89), (41, 89)], 4), NOSE, 'f')],
  _axes('side') + dome('side', top=6, w=44, cy=44, n=10, amp=5, soft=True, nape=84, fr=48, seed=5),
  _axes('back') + dome('back', top=6, w=44, cy=44, n=10, amp=5, soft=True, nape=84, seed=5))

# Douglas "Dogfish" Fische: pelo azul petróleo peinado hacia atrás hasta la nuca, con puntas como aletas a los lados;
# antifaz negro en punta sobre unos ojos rosas, una cicatriz naranja en la mejilla y dientes apretados
PK, SC = _c('#e88aa8'), _c('#e8902a')
def _fins(view):
    f = [(10, 76), (-6, 82, 1), (8, 86), (-4, 96, 1), (14, 94)]
    return [L(outline(f)), L(outline(mirx(f)))] if view != 'side' else [L(outline([(16, 80), (0, 88, 1), (14, 92), (2, 102, 1), (20, 98)]))]
C('douglas-dogfish-fische', 'normal', P('#2d4e61', '#bd8e6c', iris='#1a1414', shade='#1e3a4a', deep='#14262e'),
  F(eyes='none', brows=False, mouth='grin', mouth_y=95, hairline=[(8, 62), (18, 46), (34, 38), (50, 36), (66, 38), (82, 46), (92, 62)]),
  _fins('front') + dome('front', top=4, w=46, cy=46, long=96, flare=2) +
  [L(outline([(18, 66), (50, 72), (82, 66), (80, 82), (56, 84), (50, 92, 1), (44, 84), (20, 82)]), BLACK, 'f'),
   L(ell(36, 76, 4.4, 3.6), PK, 'f', False), L(ell(64, 76, 4.4, 3.6), PK, 'f', False), L(ell(36, 76, 1.6, 1.6), BLACK, 'f', False), L(ell(64, 76, 1.6, 1.6), BLACK, 'f', False),
   L([(66, 82), (71, 98)], SC, 'f', False, False, 1.8)],
  _fins('side') + dome('side', top=4, w=46, cy=46, long=96, flare=2, fr=44) +
  [L(outline([(56, 66), (90, 66), (92, 80), (60, 80)]), BLACK, 'f'), L(ell(84, 73, 3.4, 3.2), PK, 'f', False)],
  _fins('back') + dome('back', top=4, w=46, cy=46, long=96, flare=2, ends=3) + [L(outline([(6, 70), (94, 70), (94, 76), (6, 76)]), BLACK, 'f')])

# Downtworth "Worthy" Beyan: cabeza casi rapada con el pelo gris azulado en franjas oscuras que suben hacia la coronilla;
# piel cobriza, perilla oscura, ojos afilados y media sonrisa
GOAT = _c('#2e3640')
def _stripes(view):
    if view == 'side':
        return [L(outline([(40, 8), (48, 6), (40, 40), (34, 38)]), 'shade', 'b', False), L(outline([(60, 8), (66, 10), (70, 36), (64, 38)]), 'shade', 'b', False)]
    return [L(outline([(46, 12), (54, 12), (54, 40), (46, 40)]), 'shade', 'b', False),
            L(outline([(28, 20), (34, 16), (30, 44), (24, 42)]), 'shade', 'b', False), L(outline(mirx([(28, 20), (34, 16), (30, 44), (24, 42)])), 'shade', 'b', False)]
C('downtworth-worthy-beyan', 'normal', P('#6f7d90', '#ca7150', iris='#1a1414', shade='#3c424b'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=92, hairline=[(8, 58), (20, 48), (50, 42), (80, 48), (92, 58)]),
  [L(outline([(18, 54), (18, 30), (34, 14), (50, 10), (66, 14), (82, 30), (82, 54), (70, 42), (50, 38), (30, 42)]))] + _stripes('front') +
  [L(outline([(45, 100), (55, 100), (53, 109), (47, 109)]), GOAT, 'f')],
  [L(outline([(46, 44), (30, 46), (14, 40), (10, 24), (26, 8), (52, 4), (74, 10), (86, 28), (84, 40), (70, 36), (56, 38)]))] + _stripes('side') +
  [L(outline([(78, 100), (86, 98), (84, 106), (78, 106)]), GOAT, 'f')],
  [L(outline([(14, 58), (12, 32), (26, 12), (50, 6), (74, 12), (88, 32), (86, 58), (50, 54)]))] + _stripes('back'))

# Drakaina Eastwick: melena larga azul oscuro con flequillo y dos mechones rubios que le enmarcan la cara y acaban en punta
# en la barbilla; la melena se abre por abajo; ojos verde grisáceo con pestañas
YEL3 = _c('#ebc16c')
C('drakaina-eastwick', 'chica', P('#4d6096', '#fcf2db', iris='#5a8a8a', shade='#3a4874', deep='#2a3456'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=92, hairline=[(8, 70), (16, 62), (30, 58), (50, 62), (70, 58), (84, 62), (92, 70)]),
  dome('front', top=0, w=46, cy=46, long=120, flare=10) +
  [L(outline([(16, 48), (26, 48), (28, 80), (22, 104, 1), (15, 80)]), YEL3, 'f'), L(outline(mirx([(16, 48), (26, 48), (28, 80), (22, 104, 1), (15, 80)])), YEL3, 'f')],
  dome('side', top=0, w=46, cy=46, long=120, flare=10, fr=60) + [L(outline([(70, 46), (80, 48), (84, 80), (78, 102, 1), (72, 80)]), YEL3, 'f')],
  dome('back', top=0, w=46, cy=46, long=120, flare=10, ends=4))

# Dreama Paris (portera): cofia de doncella blanca con volantes sobre una melena larga azul marino con flequillo recto;
# ojos grandes rojos
def _frill(view):
    if view == 'side':
        return [L(outline([(28, 8), (50, 2), (72, 6), (82, 16), (70, 18), (50, 14), (32, 16)]), WHITE, 'f')] + \
               [L(ell(x, y, 6, 6), WHITE, 'f') for x, y in ((34, 6), (48, 0), (62, 2), (74, 8))]
    return [L(outline([(12, 32), (14, 18), (30, 8), (50, 4), (70, 8), (86, 18), (88, 32), (70, 26), (50, 24), (30, 26)]), WHITE, 'f')] + \
           [L(ell(x, y, 6.5, 6.5), WHITE, 'f') for x, y in ((16, 22), (28, 10), (42, 4), (58, 4), (72, 10), (84, 22))]
C('dreama-paris', 'chica', P('#39385a', '#f5d7bb', iris='#c02040', shade='#2a2a44', deep='#1e1e30'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, hairline=[(8, 70), (16, 64), (50, 64), (84, 64), (92, 70)]),
  dome('front', top=4, w=46, cy=46, long=114, flare=4) + _frill('front'),
  dome('side', top=4, w=46, cy=46, long=114, flare=4, fr=62) + _frill('side'),
  dome('back', top=4, w=46, cy=46, long=114, flare=4, ends=4) + _frill('back'))

# Drei "3" White-Whitely: casco blanco redondo como una bola de billar con un 3 negro enorme, que le tapa la cabeza y media
# cara; un solo ojo grande verde azulado a la vista, una tirita en la mejilla y morros
BALL, BALL_D, N3, PL = _c('#f4f2ee'), _c('#d8c4c4'), _c('#3a3a3a'), _c('#f0dcc0')
DIGITS = {3: [[(48, 14), (62, 12), (64, 22), (56, 28), (66, 32), (66, 44), (52, 46)]], 1: [[(48, 18), (57, 11), (57, 46)], [(49, 46), (65, 46)]],
          5: [[(64, 12), (50, 12), (49, 26), (62, 26), (66, 36), (62, 46), (48, 46)]]}
def _three(dx=0, s=1.0, d=3):
    return [L([(50 + (x - 50) * s + dx, 10 + (y - 10) * s) for x, y in p], N3, 'f', False, False, 5 * s) for p in DIGITS[d]]
def _ballhead(view, d):
    eye = _c('#3a9aa8')
    if view == 'front':
        return [L(outline([(8, 74), (4, 44), (14, 18), (34, 4), (60, 0), (84, 8), (96, 30), (98, 62), (92, 88), (80, 98), (74, 84), (70, 62), (50, 58), (28, 62), (16, 76)]), BALL, 'f'),
                L(outline([(84, 40), (96, 50), (94, 80), (82, 94), (78, 70)]), BALL_D, 'f', False)] + _three(d=d) + \
               [L(ell(36, 74, 7.5, 8.5), WHITE, 'f'), L(ell(37, 75, 5, 6), eye, 'f', False), L(ell(37, 75, 2.4, 2.8), BLACK, 'f', False),
                L(outline([(60, 86), (70, 84), (72, 92), (62, 94)]), PL, 'f')]
    if view == 'side':
        return [L(outline([(20, 82), (6, 50), (12, 20), (36, 4), (64, 2), (86, 14), (96, 36), (94, 60), (86, 62), (70, 54), (50, 58), (36, 78)]), BALL, 'f')] + _three(-14, 0.7, d) + \
               [L(ell(82, 74, 5, 7), WHITE, 'f'), L(ell(84, 75, 3, 4.5), eye, 'f', False)]
    return [L(outline([(8, 88), (4, 44), (16, 14), (50, 0), (84, 14), (96, 44), (92, 88), (50, 96)]), BALL, 'f')] + _three(0, 1.2, d)
C('drei-3-white-whitely', 'normal', P('#f4f2ee', '#fbefd5', iris='#3a9aa8'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=95, hairline=False), _ballhead('front', 3), _ballhead('side', 3), _ballhead('back', 3))

# Drew "Circle" Serkell: pelo corto amarillo oliva con un racimo de bolas amarillas y blancas encima, a la izquierda; gafas
# blancas de lentes verdes y una sonrisa enorme de dientes; piel tostada
YB, GRN = _c('#f8d040'), _c('#4a7a3a')
def _balls(view):
    if view == 'side':
        return [L(ell(36, 6, 12, 12), YB), L(ell(24, -2, 10, 10), YB), L(ell(46, 18, 9, 9), WHITE)]
    return [L(ell(20, 24, 10, 10), WHITE), L(ell(34, 24, 9, 9), WHITE), L(ell(30, 6, 12, 12), YB), L(ell(46, -4, 10, 10), YB), L(ell(16, 8, 8, 8), WHITE)]
def _wgog(view):
    if view == 'side':
        return [L(ell(82, 75, 6, 7), WHITE, 'f'), L(ell(83, 75, 4, 5), GRN, 'f', False), L([(76, 74), (50, 70)], WHITE, 'f', False, False, 2.2)]
    return [L(ell(36, 76, 10, 8), WHITE, 'f'), L(ell(36, 76, 6.5, 5), GRN, 'f', False), L(ell(64, 76, 10, 8), WHITE, 'f'), L(ell(64, 76, 6.5, 5), GRN, 'f', False)]
C('drew-circle-serkell', 'normal', P('#b0a038', '#cd9668', iris='#1a1414', shade='#8a7e28'),
  F(eyes='none', brows=False, mouth='none', mouth_y=94, hairline=[(8, 62), (18, 52), (50, 48), (82, 52), (92, 62)]),
  dome('front', top=10, w=44, cy=48, sb=62) + _balls('front') + _wgog('front') + big_grin(94, 13, 9),
  dome('side', top=10, w=44, cy=48, nape=84, fr=50) + _balls('side') + _wgog('side'),
  dome('back', top=10, w=44, cy=48, nape=84) + _balls('back'))

# Drew Pii: pelo verde oscuro en pinchos con un flequillo largo que le tapa media cara; el ojo que se ve, redondo y negro;
# mofletes naranjas y boca enfurruñada
C('drew-pii', 'normal', P('#26442b', '#f8ba7b', iris='#1a1414', shade='#1a3020', deep='#0e1a10'),
  F(eyes='round', brows=False, mouth='frown', mouth_y=93, hairline=hl(5, 64, 48, 58, jit=2, seed=11)),
  dome('front', top=0, w=48, cy=46, n=9, amp=10, seed=12, sb=72) + [L(outline([(16, 46), (54, 46), (50, 92, 1), (42, 72), (30, 86, 1), (22, 62)]), 'mid', 'f')] +
  blush(88, 22, 4.4),
  dome('side', top=0, w=48, cy=46, n=9, amp=10, seed=12, nape=88, fr=50),
  dome('back', top=0, w=48, cy=46, n=9, amp=10, seed=12, nape=88))

# Dri Lightning: pañuelo blanco grisáceo enrollado en la cabeza, echado hacia atrás y con la cola colgando a la izquierda;
# un mechón naranja le tapa media cara; cara larga pálida, un ojo rojo afilado y boca seria
WH2, WH2D = _c('#dae5e3'), _c('#a8b4b2')
def _dri(view):
    if view == 'front':
        return [L(outline([(12, 54), (10, 30), (22, 10), (50, 2), (80, 6), (98, -2, 1), (86, 20), (70, 30), (40, 44), (18, 60)]), WH2),
                L(outline([(14, 50), (6, 70), (2, 98, 1), (12, 76), (20, 58)]), WH2),
                L(outline([(48, 40), (70, 22), (90, 30), (92, 60), (84, 98, 1), (72, 80), (60, 56)]), 'mid', 'f'),
                L(outline([(70, 30), (88, 34), (90, 58), (84, 90), (78, 60)]), 'shade', 'f', False)]
    if view == 'side':
        return [L(outline([(44, 52), (20, 48), (6, 30), (20, 8), (50, 0), (80, 6), (100, 0, 1), (88, 22), (70, 32), (56, 42)]), WH2),
                L(outline([(10, 46), (-4, 64), (-8, 94, 1), (4, 72), (16, 54)]), WH2),
                L(outline([(62, 30), (84, 30), (94, 52), (90, 84), (82, 98, 1), (76, 66)]), 'mid', 'f')]
    return [L(outline([(10, 76), (8, 30), (22, 10), (50, 2), (80, 6), (94, 30), (92, 76), (50, 82)]), WH2),
            L(outline([(60, 8), (80, 10), (94, 36), (90, 70), (76, 40)]), WH2D, 'b', False),
            L(outline([(80, 50), (92, 64), (98, 96, 1), (86, 74)]), WH2)]
C('dri-lightning', 'delgado', P('#f9b70f', '#fce9b6', iris='#b01818', shade='#d08a08'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=97, face_front=face(chin=106, w=-2), face_side=face_side(chin=5),
    hairline=[(8, 66), (20, 56), (40, 48), (60, 42), (80, 50), (92, 66)]),
  _dri('front'), _dri('side'), _dri('back'))

# Drummond Bays: pelo azul en pinchos largos que salen hacia arriba y a los lados, con una cinta verde ancha en la frente
# y una bufanda verde al cuello; ojos verde agua y sonrisa
GRN2 = _c('#688052')
def _band(view):
    if view == 'side':
        return [L(outline([(10, 34), (50, 26), (90, 34), (92, 48), (50, 42), (10, 50)]), GRN2, 'f')]
    return [L(outline([(6, 40), (50, 32), (94, 40), (96, 54), (50, 48), (4, 54)]), GRN2, 'f')]
C('drummond-bays', 'normal', P('#7093b1', '#ca976c', iris='#2aa8a0', shade='#5a7898', deep='#3e5470'),
  F(eyes='sharp', brows=True, mouth='smile', mouth_y=92, hairline=hl(5, 66, 50, 62, jit=2, seed=13)),
  dome('front', top=-2, w=48, cy=46, n=9, amp=16, sweep=0.3, seed=14, sb=72) + _band('front') + scarf('front', GRN2, 100, 14),
  dome('side', top=-2, w=48, cy=46, n=9, amp=16, sweep=0.3, seed=14, nape=88, fr=50) + _band('side') + scarf('side', GRN2, 100, 14),
  dome('back', top=-2, w=48, cy=46, n=9, amp=16, sweep=0.3, seed=14, nape=88) + _band('back') + scarf('back', GRN2, 100, 14))

# Duane Jerus: media melena ondulada rosa lila con reflejos azul claro, hasta la mandíbula; piel morena, ojos azules
# afilados y la lengua fuera
LB, TONG = _c('#bfd3ee'), _c('#e0707a')
C('duane-jerus', 'normal', P('#e8d4ec', '#be8c69', iris='#4a8ad8', shade='#c4b0c8', deep='#a08ca4'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=[(8, 66), (18, 52), (34, 46), (50, 50), (64, 44), (82, 50), (92, 66)]),
  dome('front', top=2, w=48, cy=46, n=6, amp=6, soft=True, long=96, flare=6, seed=15) +
  [L(outline([(52, 20), (64, 14), (62, 44), (56, 50)]), LB, 'b', False), L(outline([(20, 50), (26, 54), (22, 90), (16, 86)]), LB, 'f', False),
   L(blob([(47, 95), (53, 95), (54, 101), (46, 101)], 4), TONG, 'f')],
  dome('side', top=2, w=48, cy=46, n=6, amp=6, soft=True, long=96, flare=6, seed=15, fr=56) + [L(outline([(40, 14), (56, 10), (48, 40), (40, 44)]), LB, 'b', False)],
  dome('back', top=2, w=48, cy=46, n=6, amp=6, soft=True, long=96, flare=6, seed=15, ends=4))

# Due "2" Black-Blackley: bola negra enorme sobre la cabeza con dos círculos blancos como ojos y un ala de sombrero
# debajo; flequillo negro que le tapa los ojos; nariz pequeña y media sonrisa
BK2 = _c('#2a272a')
def _due(view):
    if view == 'front':
        return [L(ell(50, 10, 48, 44), BLACK, 'f'), L(ell(36, 2, 9, 9), WHITE, 'f'), L(ell(62, -2, 9, 9), WHITE, 'f'),
                L(outline([(14, 58), (86, 58), (86, 80), (72, 74), (62, 88, 1), (52, 72), (40, 80), (26, 74), (16, 86)]), 'mid', 'f'),
                L(outline([(4, 58), (10, 48), (50, 44), (90, 48), (96, 58), (50, 62)]), BK2, 'f')]
    if view == 'side':
        return [L(ell(46, 8, 46, 42), BLACK, 'f'), L(ell(76, -2, 8, 8), WHITE, 'f'),
                L(outline([(58, 58), (90, 58), (88, 82), (76, 76), (68, 62)]), 'mid', 'f'),
                L(outline([(-4, 54), (10, 46), (50, 42), (100, 48), (96, 58), (50, 60)]), BK2, 'f')]
    return [L(outline([(12, 58), (88, 58), (86, 86), (50, 92), (14, 86)])), L(ell(50, 10, 48, 44), BLACK, 'f'),
            L(outline([(4, 58), (10, 48), (50, 44), (90, 48), (96, 58), (50, 62)]), BK2, 'f')]
C('due-2-black-blackley', 'normal', P('#322f32', '#e8c8b8', iris='#1a1414'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=95, hairline=False, nose=(50, 86, 2.4)), _due('front'), _due('side'), _due('back'))

# Dusty Weeza: casco gris verdoso con pinchitos y una máscara de gas marrón oscura con dos lentes naranjas y el filtro
# redondo; asoman las orejas
HELM, GM, LENS, FIL = _c('#9ca899'), _c('#4e4038'), _c('#f19249'), _c('#2a221e')
def _gas(view):
    if view == 'front':
        sp = [L(outline([(x - 5, y + 4), (x, y - 8, 1), (x + 5, y + 4)]), HELM) for x, y in ((24, 14), (40, 6), (60, 6), (76, 14))]
        return sp + [L(outline([(12, 54), (10, 30), (24, 12), (50, 6), (76, 12), (90, 30), (88, 54), (50, 48)]), HELM),
                     L(outline([(14, 50), (86, 50), (88, 80), (76, 96), (60, 106), (40, 106), (24, 96), (12, 80)]), GM, 'f'),
                     L(blob([(24, 60), (44, 58), (46, 80), (28, 82)], 4), LENS, 'f'), L(blob(mirx([(24, 60), (44, 58), (46, 80), (28, 82)]), 4), LENS, 'f'),
                     L(ell(50, 96, 8, 7), FIL, 'f')] + [L(ell(50 + dx, 96 + dy, 1.2, 1.2), GM, 'f', False) for dx, dy in ((-3, -2), (3, -2), (0, 2))]
    if view == 'side':
        return [L(outline([(x - 5, y + 4), (x, y - 8, 1), (x + 5, y + 4)]), HELM) for x, y in ((30, 8), (50, 2), (70, 6))] + \
               [L(outline([(40, 54), (14, 50), (6, 30), (24, 8), (52, 2), (76, 8), (90, 26), (90, 46), (60, 50)]), HELM),
                L(outline([(56, 50), (90, 50), (96, 80), (88, 100), (66, 106), (54, 92)]), GM, 'f'), L(ell(84, 68, 6, 8), LENS, 'f'), L(ell(92, 96, 6, 7), FIL, 'f')]
    return [L(outline([(x - 5, y + 4), (x, y - 8, 1), (x + 5, y + 4)]), HELM) for x, y in ((24, 14), (40, 6), (60, 6), (76, 14))] + \
           [L(outline([(10, 80), (8, 30), (24, 10), (50, 4), (76, 10), (92, 30), (90, 80), (50, 86)]), HELM), L([(10, 72), (90, 72)], FIL, 'f', False, False, 3.0)]
C('dusty-weeza', 'normal', P('#9ca899', '#e8c0a0', iris='#1a1414'),
  F(eyes='none', brows=False, mouth='none', hairline=False, ears_front=True, ear_out=3), _gas('front'), _gas('side'), _gas('back'))

# Dylan Quint: melena castaña lisa con raya en medio hasta los hombros y mechones rubios que le enmarcan la cara; ojos
# afilados con ojeras moradas, ceño fruncido y dientes de sierra
YS, BAG = _c('#e7c844'), _c('#7a5a8a')
C('dylan-quint', 'normal', P('#624f31', '#f9d8b5', iris='#1a1414', shade='#4a3a22', deep='#2e2414'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=95, hairline=[(8, 70), (16, 56), (32, 46), (50, 40), (68, 46), (84, 56), (92, 70)]),
  dome('front', top=2, w=46, cy=46, long=106, flare=2) +
  [L(outline([(22, 46), (30, 44), (26, 100), (18, 100)]), YS, 'f'), L(outline([(78, 46), (70, 44), (74, 100), (82, 100)]), YS, 'f'),
   L(quad((28, 83), (36, 87), (44, 83)), BAG, 'f', False, False, 2.0), L(quad((56, 83), (64, 87), (72, 83)), BAG, 'f', False, False, 2.0),
   strand([(50, 4), (50, 34)], 'deep', 'f')],
  dome('side', top=2, w=46, cy=46, long=106, flare=2, fr=54) + [L(outline([(66, 44), (74, 44), (76, 100), (68, 98)]), YS, 'f')],
  dome('back', top=2, w=46, cy=46, long=106, flare=2, ends=3))

# Eartha Toughlove (portera): grandullona de cara ancha y morena con el pelo morado corto en pinchos que se rizan a los
# lados; maquillaje de payaso: nariz roja, sombra morada en los ojos y la boca pintada de lila con una sonrisa de dientes
PURP, LAV, CNOSE = _c('#6a2a6a'), _c('#9896c8'), _c('#e04a5a')
C('eartha-toughlove', 'corpulento', P('#6a2a6a', '#b08264', iris='#2a8a8a', shade='#4a1a4a'),
  F(eyes='normal', brows=False, mouth='none', mouth_y=94, face_front=face(w=6, jaw=4), hairline=[(8, 56), (20, 46), (50, 42), (80, 46), (92, 56)]),
  [L(outline([(16, 50), (10, 32), (0, 22, 1), (18, 24), (22, 10), (14, -6, 1), (32, 8), (50, 6), (68, 8), (86, -6, 1), (78, 10), (82, 24), (100, 22, 1), (90, 32),
              (84, 50), (70, 40), (30, 40)])),
   L(quad((26, 66), (36, 60), (46, 66)), PURP, 'f', False, False, 2.6), L(quad((54, 66), (64, 60), (74, 66)), PURP, 'f', False, False, 2.6),
   L(blob([(24, 86), (50, 82), (76, 86), (78, 100), (60, 110), (40, 110), (22, 100)], 6), LAV, 'f', False)] + big_grin(92, 15, 10) + [L(ell(50, 84, 6, 5), CNOSE, 'f')],
  [L(outline([(54, 46), (60, 36), (80, 34), (90, 22, 1), (76, 18), (70, 4, 1), (54, 8), (36, 4), (18, 14), (6, 28), (-4, 26, 1), (6, 40), (20, 50), (40, 50)])),
   L(blob([(66, 86), (90, 84), (92, 100), (80, 108), (66, 104)], 6), LAV, 'f', False), L(ell(90, 84, 4.6, 4.2), CNOSE, 'f')],
  [L(outline([(12, 66), (8, 36), (-2, 24, 1), (16, 26), (20, 10), (14, -6, 1), (32, 8), (50, 6), (68, 8), (86, -6, 1), (80, 10), (84, 26), (102, 24, 1), (92, 36),
              (88, 66), (50, 72)]))])

# Ed Jogge: pelo gris plateado de erizo, con pinchos larguísimos en todas direcciones y algunos por la frente; ojos verde
# agua afilados y boca pequeña
C('ed-jogge', 'normal', P('#a8adb3', '#f8dabc', iris='#4aa8a0', shade='#7f8288', deep='#5a5c60'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=93, hairline=hl(6, 68, 48, 66, jit=4, seed=16)),
  dome('front', top=0, w=48, cy=46, n=13, amp=24, seed=17, sb=76),
  dome('side', top=0, w=48, cy=46, n=13, amp=24, seed=17, nape=90, fr=52),
  dome('back', top=0, w=48, cy=46, n=13, amp=24, seed=17, nape=90))

# Egor Coxcomb (portero): grandullón moreno con una cresta roja de gallo y rayas rojas en los lados rapados; ojos amarillos
# con la raya negra gruesa, cejas furiosas, nariz gorda, sonrisa de dientes y un pañuelo rojo anudado al cuello
CRS = _c('#c42a26')
C('egor-coxcomb', 'corpulento', P('#c42a26', '#bf844d', iris='#e0b020', shade='#88221b', nose='#955834'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=96, nose=(50, 86, 3.8), face_front=face(w=6, jaw=4), hairline=False),
  skull3('front') + [L(outline([(40, 32), (34, 8), (40, -14, 1), (48, 0), (52, -22, 1), (58, -2), (66, -12, 1), (66, 10), (60, 32)])),
   L([(22, 44), (30, 32)], 'shade', 'f', False, False, 2.6), L([(26, 50), (34, 38)], 'shade', 'f', False, False, 2.6),
   L([(78, 44), (70, 32)], 'shade', 'f', False, False, 2.6), L([(74, 50), (66, 38)], 'shade', 'f', False, False, 2.6),
   L(outline([(80, 96), (96, 90), (94, 100), (82, 102)]), CRS, 'f')] + thick_brows(64, BLACK, 4.2, 14, 1.4, 14),
  skull3('side') + [L(outline([(26, 22), (34, -4, 1), (46, 4), (58, -16, 1), (66, 2), (80, -6, 1), (80, 16), (62, 22), (40, 24)])),
   L([(30, 40), (40, 30)], 'shade', 'f', False, False, 2.6), L([(36, 46), (46, 36)], 'shade', 'f', False, False, 2.6)] + side_brow(64, BLACK, 4.2, 1.4),
  skull3('back') + [L(outline([(44, 44), (42, 4), (50, -14, 1), (58, 4), (56, 44)]))])

# Eins "1" White-Whitely (portero): casco blanco de bola de billar con un 1 negro que le tapa la cabeza y media cara; un
# solo ojo verde azulado, tirita en la mejilla y morros
C('eins-1-white-whitely', 'normal', P('#f4f2ee', '#f8ecd6', iris='#3a9aa8'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=95, hairline=False), _ballhead('front', 1), _ballhead('side', 1), _ballhead('back', 1))

# Eira Dynamic (portera): gorro rojo de pelo enorme y cuadrado que le baja hasta las cejas, y una melena rubia lisa hasta
# los hombros; ojos grandes azules con pestañas y boquita seria
HAT, HAT_D = _c('#c04234'), _c('#8a2e24')
def _eira(view):
    fz = lambda pts: [L(outline([(x - 4, y), (x, y - 6, 1), (x + 4, y)]), HAT, 'f') for x, y in pts]
    if view == 'side':
        return [L(outline([(8, 66), (2, 30), (6, -6), (50, -12), (92, -6), (98, 30), (94, 60), (50, 62)]), HAT, 'f'),
                L(outline([(70, -8), (92, -4), (98, 30), (94, 58), (80, 30)]), HAT_D, 'f', False)] + fz([(20, -8), (50, -12), (80, -8)])
    return [L(outline([(10, 64), (4, 40), (2, 8), (8, -8), (30, -12), (50, -10), (70, -12), (92, -8), (98, 8), (96, 40), (90, 64), (50, 68)]), HAT, 'f'),
            L(outline([(70, -10), (92, -6), (98, 10), (96, 40), (90, 62), (80, 30)]), HAT_D, 'f', False)] + \
           fz([(14, -8), (34, -12), (56, -10), (78, -12)]) + [L(outline([(0, 30), (-6, 34, 1), (2, 40)]), HAT, 'f'), L(outline([(100, 30), (106, 34, 1), (98, 40)]), HAT, 'f')]
C('eira-dynamic', 'chica', P('#e0b878', '#f2d8b8', iris='#4a90d0', shade='#b88e54'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=93, hairline=False),
  dome('front', top=10, w=46, cy=50, long=108, flare=6) + _eira('front'),
  dome('side', top=10, w=46, cy=50, long=108, flare=6, fr=62) + _eira('side'),
  dome('back', top=10, w=46, cy=50, long=108, flare=6, ends=4) + _eira('back'))

# Elf Lightning (portero): pelo gris oscuro corto en pinchitos, con dos mechones amarillos en forma de rayo a los lados que
# suben como cuernos; ojos en espiral rojos, orejas grandes y boca seria
YB2, SPR = _c('#fce871'), _c('#c8283a')
def _spiral():
    out = []
    for cx in (36, 64):
        out += [L(ell(cx, 76, 7, 7.5), WHITE, 'f'), loop(ell(cx, 76, 4.6, 5), SPR, 1.5), L(ell(cx, 76, 1.8, 1.8), SPR, 'f', False)]
    return out
bolt = [(16, 60), (20, 42), (8, 16), (2, -6, 1), (16, 8), (22, 26), (28, 34), (26, 52)]
C('elf-lightning', 'normal', P('#6b6359', '#f6bc7b', iris='#c8283a', shade='#4a443c'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=93, big_ears=2,
    hairline=[(8, 60), (20, 48), (34, 56), (42, 46), (50, 54), (58, 46), (66, 56), (80, 48), (92, 60)]),
  dome('front', top=6, w=44, cy=46, n=3, amp=10, seed=18, sb=60) + [L(outline(bolt), YB2, 'f'), L(outline(mirx(bolt)), YB2, 'f')] + _spiral(),
  dome('side', top=6, w=44, cy=46, n=3, amp=10, seed=18, nape=84, fr=50) + [L(outline([(70, 60), (74, 40), (64, 16), (60, -4, 1), (72, 8), (78, 28), (82, 50)]), YB2, 'f'),
                                                                          L(ell(82, 76, 5, 7), WHITE, 'f'), L(ell(83, 76, 2, 2.4), SPR, 'f', False)],
  dome('back', top=6, w=44, cy=46, n=3, amp=10, seed=18, nape=84) + [L(outline(bolt), YB2), L(outline(mirx(bolt)), YB2)])

# Emett "Emerald" Raldo: pelo verde en un tupé plano y cuadrado como una maceta, más ancho arriba, con patillas que le bajan
# por las mejillas; cejas verdes, tirita en la nariz, ojos entornados y sonrisa de dientes
EG, EG_L, PLAST = _c('#5b9b56'), _c('#7ab874'), _c('#f0e0c8')
C('emett-emerald-raldo', 'normal', P('#5b9b56', '#f8bc7c', iris='#1a1414', shade='#486139', light='#7ab874'),
  F(eyes='sharp', brows=False, mouth='grin', mouth_y=95, hairline=[(8, 82), (20, 82), (22, 58), (40, 54), (60, 54), (78, 58), (80, 82), (92, 82)]),
  [L(outline([(14, 82), (14, 52), (10, 18), (6, 10), (94, 10), (90, 18), (86, 52), (86, 82), (79, 82), (78, 56), (22, 56), (21, 82)])),
   L(outline([(6, 10), (94, 10), (92, 18), (8, 18)]), 'light', 'f'),
   L(outline([(64, 18), (90, 18), (86, 52), (80, 56), (76, 30)]), 'shade', 'b', False),
   L(outline([(44, 80), (56, 80), (56, 86), (44, 86)]), PLAST, 'f')] + thick_brows(64, _c('#3a7a36'), 3.4, 14, 1.0, 13),
  [L(outline([(54, 82), (56, 56), (84, 52), (92, 18), (96, 10), (4, 10), (8, 18), (6, 56), (20, 78), (40, 80)])),
   L(outline([(4, 10), (96, 10), (94, 18), (8, 18)]), 'light', 'f')] + side_brow(64, _c('#3a7a36'), 3.4, 1.0),
  [L(outline([(12, 86), (12, 50), (10, 18), (6, 10), (94, 10), (90, 18), (88, 50), (88, 86), (50, 90)])), L(outline([(6, 10), (94, 10), (92, 18), (8, 18)]), 'light', 'f')])

# Emilia Odde (portera): lolita gótica de melena larga gris plateada con mechones a los lados que se rizan al final; tocado
# negro de volantes con una cinta verde azulada y dos horquillas de trébol; ojos grandes gris violeta y labios morados
TEAL = _c('#2a8a8a')
def _goth(view):
    if view == 'side':
        return [L(outline([(30, 6), (50, -2), (72, 4), (82, 16), (70, 18), (50, 14), (34, 16)]), BLACK, 'f')] + \
               [L(ell(x, y, 6, 6), BLACK, 'f') for x, y in ((34, 4), (48, -4), (62, 0), (74, 8))] + [L(quad((28, 18), (50, 14), (80, 20)), TEAL, 'f', False, False, 2.4)]
    return [L(outline([(14, 32), (18, 14), (30, 2), (50, -4), (70, 2), (82, 14), (86, 32), (70, 26), (50, 24), (30, 26)]), BLACK, 'f')] + \
           [L(ell(x, y, 7, 7), BLACK, 'f') for x, y in ((18, 18), (30, 6), (44, 0), (56, 0), (70, 6), (82, 18))] + \
           [L(quad((12, 34), (50, 24), (88, 34)), TEAL, 'f', False, False, 2.6)]
C('emilia-odde', 'chica', P('#dae3e7', '#fef0d5', iris='#5a5a8a', shade='#b4bcc0', deep='#9a9ea2'),
  F(eyes='big', brows=False, mouth='line', mouth_y=93, hairline=[(8, 70), (16, 58), (30, 50), (50, 56), (70, 50), (84, 58), (92, 70)]),
  dome('front', top=4, w=46, cy=46, long=116, flare=6) + _goth('front') +
  [L(ell(20, 60, 4, 4), TEAL, 'f'), L(ell(80, 60, 4, 4), TEAL, 'f'),
   L(outline([(12, 104), (4, 112), (8, 120, 1), (14, 112)]), 'mid', 'f'), L(outline([(88, 104), (96, 112), (92, 120, 1), (86, 112)]), 'mid', 'f')] + blush(88, 22, 4),
  dome('side', top=4, w=46, cy=46, long=116, flare=6, fr=60) + _goth('side') + [L(ell(66, 60, 4, 4), TEAL, 'f')],
  dome('back', top=4, w=46, cy=46, long=116, flare=6, ends=4) + _goth('back'))

# Eolia Amhart: gorro de aviador caqui con las orejeras larguísimas colgando hasta los hombros y unas gafas de piloto de
# cristales verdes en la frente; ojos marrones, pinturas gris verdoso en las mejillas y sonrisa de dientes
KH2, KH2D, STRAP, GL = _c('#8a7a68'), _c('#6a5a4a'), _c('#a8501e'), _c('#a8d0c4')
def _aviator(view):
    if view == 'front':
        return [L(outline([(10, 104), (6, 60), (8, 30), (22, 10), (50, 2), (78, 10), (92, 30), (94, 60), (90, 104), (80, 106), (80, 70), (78, 54), (22, 54), (20, 70), (20, 106)]), KH2, 'f'),
                L(outline([(70, 8), (90, 28), (94, 60), (90, 102), (82, 100), (84, 58), (80, 30)]), KH2D, 'f', False),
                L(outline([(6, 42), (94, 42), (94, 52), (6, 52)]), STRAP, 'f'),
                L(blob([(20, 34), (46, 34), (46, 54), (22, 56)], 4), GL, 'f'), L(blob(mirx([(20, 34), (46, 34), (46, 54), (22, 56)]), 4), GL, 'f'),
                L(blob([(16, 82), (30, 80), (32, 90), (18, 92)], 4), _c('#90a89a'), 'f', False), L(blob(mirx([(16, 82), (30, 80), (32, 90), (18, 92)]), 4), _c('#90a89a'), 'f', False)]
    if view == 'side':
        return [L(outline([(66, 54), (82, 50), (90, 30), (78, 10), (50, 2), (22, 10), (6, 34), (4, 70), (16, 110), (36, 110), (46, 80), (56, 60)]), KH2, 'f'),
                L(outline([(4, 40), (90, 34), (92, 44), (6, 50)]), STRAP, 'f'), L(blob([(76, 30), (94, 32), (94, 50), (78, 50)], 4), GL, 'f')]
    return [L(outline([(8, 106), (6, 60), (8, 30), (22, 10), (50, 2), (78, 10), (92, 30), (94, 60), (92, 106), (50, 100)]), KH2, 'f'),
            L(outline([(6, 42), (94, 42), (94, 52), (6, 52)]), STRAP, 'f')]
C('eolia-amhart', 'chica', P('#736354', '#f9bc7c', iris='#a8501e'),
  F(eyes='normal', brows=False, mouth='grin', mouth_y=93, hairline=False), _aviator('front'), _aviator('side'), _aviator('back'))

# Eric Byrne: máscara de calavera de toro color hueso con los cuernos curvados, que le tapa la cara hasta el hocico; se ven
# unos ojos naranjas por los agujeros y mechones castaño rojizo por los lados
BONE, BONE_D, EYO = _c('#dacaad'), _c('#b4a488'), _c('#e0702a')
horn = [(20, 30), (2, 24), (-10, 6), (-8, -10, 1), (4, 10), (22, 18)]
def _bull(view):
    if view == 'front':
        return [L(outline(horn), BONE), L(outline(mirx(horn)), BONE),
                L(outline([(16, 70), (6, 84, 1), (20, 80), (14, 94, 1), (28, 82)]), 'mid', 'f'), L(outline(mirx([(16, 70), (6, 84, 1), (20, 80), (14, 94, 1), (28, 82)])), 'mid', 'f'),
                L(outline([(14, 40), (18, 14), (34, 4), (50, 2), (66, 4), (82, 14), (86, 40), (80, 66), (64, 76), (58, 104), (50, 114, 1), (42, 104), (36, 76), (20, 66)]), BONE, 'f'),
                L(outline([(64, 6), (82, 16), (86, 40), (80, 64), (66, 74), (70, 40)]), BONE_D, 'f', False),
                L(blob([(26, 60), (44, 66), (42, 74), (28, 70)], 4), EYO, 'f'), L(blob(mirx([(26, 60), (44, 66), (42, 74), (28, 70)]), 4), EYO, 'f'),
                L(ell(37, 68, 1.6, 2.4), BLACK, 'f', False), L(ell(63, 68, 1.6, 2.4), BLACK, 'f', False),
                L([(50, 80), (50, 108)], BLACK, 'f', False, False, 1.6), L([(50, 6), (46, 20), (52, 30)], BONE_D, 'f', False, False, 1.2)]
    if view == 'side':
        return [L(outline([(40, 20), (26, 4), (26, -14, 1), (40, 4), (56, 14)]), BONE),
                L(outline([(28, 72), (16, 82, 1), (30, 82), (26, 94, 1), (40, 84)]), 'mid', 'f'),
                L(outline([(20, 40), (26, 10), (50, 2), (74, 10), (88, 30), (94, 56), (100, 80), (96, 106, 1), (84, 92), (70, 76), (50, 74), (30, 66)]), BONE, 'f'),
                L(blob([(76, 60), (88, 62), (88, 70), (78, 70)], 4), EYO, 'f')]
    return [L(outline(horn), BONE), L(outline(mirx(horn)), BONE),
            L(outline([(16, 68), (12, 30), (26, 8), (50, 2), (74, 8), (88, 30), (84, 68), (50, 74)]), BONE, 'f'),
            L(outline([(18, 64), (82, 64), (84, 86), (70, 80), (60, 92, 1), (50, 82), (40, 92, 1), (30, 80), (16, 86)]), 'mid', 'f')]
C('eric-byrne', 'normal', P('#a84a2a', '#a8816f', iris='#1a1414'),
  F(eyes='none', brows=False, mouth='none', hairline=False), _bull('front'), _bull('side'), _bull('back'))

# Ernest Etson (portero): sombrero vaquero blanco grisáceo enorme cuya ala le tapa la frente; mechones rubios a los lados,
# ojos redondos blancos, barba de pocos días y media sonrisa
HW, HWD = _c('#d0d1d3'), _c('#a8a8ac')
def _cowboy(view):
    if view == 'side':
        return [L(outline([(28, 28), (30, 0), (50, -8), (72, 0), (74, 28)]), HW),
                L(outline([(-6, 34), (20, 26), (50, 30), (90, 24), (104, 34), (90, 50), (50, 52), (10, 46)]), HW, 'f'),
                L(outline([(30, 24), (74, 24), (74, 32), (30, 32)]), HWD, 'f', False)]
    return [L(outline([(24, 32), (22, 6), (34, -8), (50, -4), (66, -8), (78, 6), (76, 32)]), HW),
            L(outline([(-2, 40), (4, 20), (18, 30), (50, 38), (82, 30), (96, 20), (102, 40), (80, 56), (50, 60), (20, 56)]), HW, 'f'),
            L(outline([(60, 40), (84, 32), (96, 22), (100, 40), (80, 54), (66, 56)]), HWD, 'f', False)]
wisp = [(14, 58), (4, 76, 1), (16, 72), (12, 88, 1), (24, 74)]
C('ernest-etson', 'normal', P('#e8c870', '#eaad68', iris='#1a1414'),
  F(eyes='round', brows=False, mouth='smile', mouth_y=94, hairline=False),
  [L(outline(wisp), 'mid', 'f'), L(outline(mirx(wisp)), 'mid', 'f')] + _cowboy('front') +
  [L(ell(50 + dx, 102 + dy, 0.8, 0.8), _c('#a87a40'), 'f', False) for dx, dy in ((-4, 0), (0, 2), (4, 0), (-2, -2), (2, -2))],
  [L(outline([(52, 60), (44, 78, 1), (56, 74), (52, 90, 1), (62, 76)]), 'mid', 'f')] + _cowboy('side'),
  _cowboy('back') + [L(outline([(14, 56), (86, 56), (84, 78), (50, 84), (16, 78)]))])

# Erwin Goel: pelo verde muy oscuro en bultos redondos enormes como nubes; gafas rojas de montura gruesa, ojos amarillos y
# boca seria
C('erwin-goel', 'normal', P('#30514f', '#f4d7a4', iris='#d8c030', shade='#223a38'),
  F(eyes='normal', brows=False, mouth='frown', mouth_y=93, hairline=[(8, 64), (20, 52), (36, 56), (50, 52), (64, 56), (80, 52), (92, 64)]),
  [L(ell(14, 48, 14, 14)), L(ell(86, 48, 14, 14)), L(ell(26, 24, 20, 18)), L(ell(74, 24, 20, 18)), L(ell(50, 12, 20, 18)),
   L(outline([(16, 62), (14, 40), (86, 40), (84, 62), (50, 52)])), L(ell(78, 26, 12, 10), 'shade', 'b', False)] + rect_specs('front', RED, 76, 14, 3.0),
  [L(ell(22, 46, 16, 16)), L(ell(40, 18, 22, 20)), L(ell(66, 22, 18, 16)), L(outline([(54, 56), (60, 42), (82, 38), (84, 30), (10, 30), (6, 56), (20, 66), (40, 62)]))] +
  rect_specs('side', RED, 76, 14, 3.0),
  [L(ell(14, 50, 14, 14)), L(ell(86, 50, 14, 14)), L(ell(26, 26, 20, 18)), L(ell(74, 26, 20, 18)), L(ell(50, 14, 20, 18)),
   L(outline([(14, 74), (12, 40), (88, 40), (86, 74), (50, 80)]))])

# Esau Tariq: melena color crema con flequillo recto, dos picos como orejas arriba y dos coletas bajas larguísimas atadas
# con bolas rojas que se abren a los lados; piel clara, ojos rojos afilados y sonrisa pícara
tail = [(14, 88), (0, 98), (-16, 116, 1), (2, 108), (18, 98)]
C('esau-tariq', 'normal', P('#f2e2c4', '#fdedd2', iris='#c01818', shade='#d4c0a0', deep='#b4a080'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=92, hairline=[(8, 68), (16, 62), (50, 62), (84, 62), (92, 68)]),
  [L(outline(tail)), L(outline(mirx(tail)))] + dome('front', top=4, w=46, cy=46, long=96, flare=2) +
  [L(outline([(12, 26), (8, 2, 1), (28, 12)])), L(outline([(88, 26), (92, 2, 1), (72, 12)])), L(ell(16, 92, 4.2, 4.2), RED, 'f'), L(ell(84, 92, 4.2, 4.2), RED, 'f')],
  dome('side', top=4, w=46, cy=46, long=96, flare=2, fr=62) + [L(outline([(36, 92), (24, 104), (10, 120, 1), (28, 110), (40, 100)])), L(ell(38, 94, 4, 4), RED, 'f')],
  [L(outline(tail)), L(outline(mirx(tail)))] + dome('back', top=4, w=46, cy=46, long=96, flare=2, ends=4) +
  [L(outline([(12, 26), (8, 2, 1), (28, 12)])), L(outline([(88, 26), (92, 2, 1), (72, 12)])), L(ell(16, 92, 4.2, 4.2), RED, 'f'), L(ell(84, 92, 4.2, 4.2), RED, 'f')])

# Eska Layte: pelo rosa en picos como pétalos con dos rizos amarillos en espiral encima y una raya amarilla en forma de
# corazón; ojos grandes verde agua, naricita redonda y boca pequeña
YS2 = _c('#f8d878')
def _eska(view):
    if view == 'side':
        return [L(outline([(56, 52), (62, 42), (82, 40), (94, 24), (98, 10, 1), (84, 14), (70, 2), (48, 0), (24, 6), (8, 22), (4, 44), (16, 58), (36, 60), (48, 54)])),
                loop(ell(56, 18, 7, 7), YS2, 2.6), L(quad((60, 30), (76, 26), (88, 36)), YS2, 'f', False, False, 2.4)]
    pts = [(16, 62), (6, 30), (2, 10, 1), (20, 22), (30, 6), (50, 10), (70, 6), (80, 22), (98, 10, 1), (94, 30), (84, 62), (70, 50), (30, 50)]
    if view == 'front':
        return [L(outline(pts)), loop(ell(38, 22, 7.5, 7.5), YS2, 2.8), loop(ell(62, 22, 7.5, 7.5), YS2, 2.8),
                L(quad((20, 42), (50, 28), (80, 42)), YS2, 'f', False, False, 2.4), L(quad((30, 34), (50, 52), (70, 34)), YS2, 'f', False, False, 2.0)]
    return [L(outline([(14, 72), (6, 30), (2, 10, 1), (20, 22), (30, 6), (50, 10), (70, 6), (80, 22), (98, 10, 1), (94, 30), (86, 72), (50, 78)])),
            loop(ell(38, 22, 7.5, 7.5), YS2, 2.8), loop(ell(62, 22, 7.5, 7.5), YS2, 2.8)]
C('eska-layte', 'chica', P('#f98d91', '#fcd69f', iris='#40b0a0', shade='#d86a70', nose='#f08a80'),
  F(eyes='big', brows=False, mouth='line', mouth_y=94, nose=(50, 86, 2.6), hairline=[(8, 64), (20, 52), (36, 48), (50, 58), (64, 48), (80, 52), (92, 64)]),
  _eska('front'), _eska('side'), _eska('back'))

# Esme Hexe: sombrero de bruja granate enorme y caído con un adorno naranja; media melena verde oliva con un mechón que le
# tapa un ojo; el otro, naranja, y sonrisa
HATR, HATRD = _c('#700e26'), _c('#511620')
def _witch(view):
    if view == 'side':
        return [L(outline([(16, 30), (20, 4), (40, -10), (64, -16), (86, -10), (100, -2, 1), (82, 2), (76, 28)]), HATR),
                L(outline([(-8, 42), (6, 28), (50, 22), (100, 28), (106, 40), (80, 46), (50, 44), (10, 48)]), HATR, 'f'), L(ell(96, 0, 5, 5), ORG, 'f')]
    return [L(outline([(14, 32), (20, 6), (40, -8), (64, -14), (86, -4), (98, 8, 1), (80, 8), (76, 32)]), HATR),
            L(outline([(-6, 46), (4, 30), (50, 22), (96, 30), (106, 46), (80, 52), (50, 50), (20, 52)]), HATR, 'f'),
            L(outline([(60, 26), (96, 32), (104, 46), (80, 50)]), HATRD, 'f', False), L(ell(92, 8, 5, 5), ORG, 'f')]
C('esme-hexe', 'chica', P('#a3a868', '#e2cfb1', iris='#d06020', shade='#7a8048', deep='#5a5e34'),
  F(eyes='normal', brows=False, mouth='smile', mouth_y=93, hairline=[(8, 66), (18, 54), (50, 52), (82, 54), (92, 66)]),
  dome('front', top=10, w=46, cy=50, long=98, flare=2) + _witch('front') + [L(outline([(14, 50), (52, 50), (48, 88, 1), (36, 72), (22, 94, 1)]), 'mid', 'f')],
  dome('side', top=10, w=46, cy=50, long=98, flare=2, fr=60) + _witch('side'),
  dome('back', top=10, w=46, cy=50, long=98, flare=2, ends=4) + _witch('back'))

# Esteban Range (portero): melena revuelta azul marino casi negra con mechones verde amarillento que se curvan hacia fuera
# como cuernos y uno que le tapa un ojo; piel morena, un ojo verde, dientes apretados y perilla
YG = _c('#d6db9d')
C('esteban-range', 'normal', P('#3f3c48', '#c09b72', iris='#6a9a4a', shade='#2c2830', deep='#1e1a20'),
  F(eyes='sharp', brows='angry', mouth='grin', mouth_y=95, hairline=hl(6, 66, 48, 60, jit=3, seed=19)),
  dome('front', top=0, w=48, cy=46, n=7, amp=8, long=100, flare=6, seed=20) +
  [L(outline([(26, 22), (40, 16), (30, 40), (6, 48), (-6, 40, 1), (12, 38)]), YG, 'f'), L(outline([(70, 18), (84, 30), (98, 34), (106, 28, 1), (100, 42), (82, 40)]), YG, 'f'),
   L(outline([(30, 40), (52, 30), (50, 84, 1), (42, 62), (30, 78, 1)]), YG, 'f'), L(outline([(46, 100), (54, 100), (52, 108), (48, 108)]), BLACK, 'f')],
  dome('side', top=0, w=48, cy=46, n=7, amp=8, long=100, flare=6, seed=20, fr=56) + [L(outline([(60, 16), (80, 26), (98, 30), (104, 24, 1), (100, 38), (78, 36)]), YG, 'f')],
  dome('back', top=0, w=48, cy=46, n=7, amp=8, long=100, flare=6, seed=20, ends=4) +
  [L(outline([(26, 22), (40, 16), (30, 40), (6, 48), (-6, 40, 1), (12, 38)]), YG), L(outline([(74, 22), (60, 16), (70, 40), (94, 48), (106, 40, 1), (88, 38)]), YG)])

# Everard Valiant: pelo azul marino en pinchos altos y un antifaz marrón de héroe en punta sobre los ojos grises; una
# bufanda turquesa que ondea a un lado y sonrisa
MASKBR, TURQ = _c('#a87a50'), _c('#20c8d8')
C('everard-valiant', 'normal', P('#0a1a6a', '#e9d4b5', iris='#8a8a8a', shade='#061048', deep='#040a30'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=93, hairline=hl(5, 64, 48, 58, jit=2, seed=21)),
  dome('front', top=-4, w=48, cy=46, n=9, amp=16, sweep=0.3, seed=22, sb=70) +
  [L(outline([(18, 64), (46, 66), (50, 56, 1), (54, 66), (82, 64), (82, 82), (60, 86), (50, 80), (40, 86), (18, 82)]), MASKBR, 'f'),
   L(blob([(28, 72), (44, 72), (44, 80), (28, 80)], 4), WHITE, 'f', False), L(blob(mirx([(28, 72), (44, 72), (44, 80), (28, 80)]), 4), WHITE, 'f', False),
   L(ell(37, 76, 3, 3.4), _c('#8a8a8a'), 'f', False), L(ell(63, 76, 3, 3.4), _c('#8a8a8a'), 'f', False),
   L(outline([(80, 100), (100, 88), (110, 74, 1), (106, 96), (90, 108)]), TURQ, 'f')] + scarf('front', TURQ, 100, 10),
  dome('side', top=-4, w=48, cy=46, n=9, amp=16, sweep=0.3, seed=22, nape=88, fr=50) +
  [L(outline([(60, 64), (92, 62), (92, 82), (62, 82)]), MASKBR, 'f'), L(ell(82, 74, 3, 3.6), WHITE, 'f', False), L(outline([(20, 98), (0, 90), (-12, 76, 1), (-6, 98), (16, 108)]), TURQ, 'f')] + scarf('side', TURQ, 100, 10),
  dome('back', top=-4, w=48, cy=46, n=9, amp=16, sweep=0.3, seed=22, nape=88) + scarf('back', TURQ, 100, 10))

# Evita "Goe" Gowell (portera): media melena castaña con una coletita alta a un lado sujeta con bolitas blancas; ojos
# marrones y sonrisa
C('evita-goe-gowell', 'chica', P('#8f6651', '#fbcea1', iris='#7a4a3a', shade='#6d4336', deep='#4a2e22'),
  F(eyes='big', brows=True, mouth='smile', mouth_y=92, hairline=hl(6, 66, 52, 62, jit=2, seed=23)),
  dome('front', top=4, w=46, cy=46, long=100, flare=6, n=0) +
  [L(outline([(70, 10), (86, 0), (98, 16), (92, 36, 1), (84, 18)])), L(ell(72, 6, 4, 4), WHITE, 'f'), L(ell(78, 2, 4, 4), WHITE, 'f')],
  dome('side', top=4, w=46, cy=46, long=100, flare=6, fr=60) + [L(outline([(40, 4), (24, -6), (12, 10), (18, 32, 1), (30, 14)])), L(ell(38, 2, 4, 4), WHITE, 'f')],
  dome('back', top=4, w=46, cy=46, long=100, flare=6, ends=4) + [L(outline([(30, 10), (14, 0), (2, 16), (8, 36, 1), (16, 18)])), L(ell(28, 6, 4, 4), WHITE, 'f')])

# F-nf "5" White-Whitely: casco blanco de bola de billar con un 5 negro; un solo ojo verde azulado, tirita y morros
C('f-nf-5-white-whitely', 'normal', P('#f4f2ee', '#faedd5', iris='#3a9aa8'),
  F(eyes='none', brows=False, mouth='frown', mouth_y=95, hairline=False), _ballhead('front', 5), _ballhead('side', 5), _ballhead('back', 5))

# Falco Peregrine: melena castaña larga echada a un lado que le tapa un ojo, con mechones blancos rosados como plumas a los
# lados; el otro ojo con un monóculo dorado; cara larga y boca seria
FEATH = _c('#f0d8d8')
C('falco-peregrine', 'delgado', P('#684825', '#dcc1ac', iris='#1a1414', shade='#4c311d', deep='#2e1e12'),
  F(eyes='sharp', brows='angry', mouth='frown', mouth_y=97, face_front=face(chin=108, w=-2), face_side=face_side(chin=6),
    hairline=[(8, 66), (20, 48), (40, 40), (60, 44), (80, 54), (92, 66)]),
  dome('front', top=0, w=46, cy=46, long=104, flare=4) +
  [L(outline([(14, 44), (4, 60), (2, 84, 1), (10, 70), (14, 92, 1), (20, 60)]), FEATH, 'f'),
   L(outline([(86, 50), (100, 62), (108, 90, 1), (96, 76), (98, 104, 1), (86, 76)]), FEATH, 'f'),
   L(outline([(20, 44), (52, 40), (48, 96, 1), (40, 70), (28, 88, 1), (24, 60)]), 'mid', 'f'),
   loop(ell(64, 75, 8, 8), GOLD, 2.4)],
  dome('side', top=0, w=46, cy=46, long=104, flare=4, fr=54) + [L(outline([(14, 50), (-2, 66), (-6, 96, 1), (6, 78), (6, 104, 1), (20, 70)]), FEATH, 'f')],
  dome('back', top=0, w=46, cy=46, long=104, flare=4, ends=4) +
  [L(outline([(12, 50), (0, 66), (-4, 94, 1), (8, 76), (10, 100, 1), (18, 66)]), FEATH), L(outline([(88, 50), (100, 66), (104, 94, 1), (92, 76), (90, 100, 1), (82, 66)]), FEATH)])

# Faulk Dansa: melena gris plateada revuelta con picos arriba; cara blanca con maquillaje de kabuki rojo alrededor de los
# ojos, ojos furiosos y boca hacia abajo
C('faulk-dansa', 'normal', P('#d9d9d6', '#fcf2e0', iris='#1a1414', shade='#b0aeaa', deep='#8a8884'),
  F(eyes='round', brows='angry', mouth='frown', mouth_y=95, hairline=[(8, 64), (18, 54), (34, 58), (50, 54), (66, 58), (82, 54), (92, 64)]),
  dome('front', top=4, w=48, cy=46, n=8, amp=8, long=104, flare=8, seed=24) +
  [L(quad((22, 74), (36, 62), (48, 72)), KR, 'f', False, False, 2.4), L(quad((78, 74), (64, 62), (52, 72)), KR, 'f', False, False, 2.4),
   L(quad((24, 84), (34, 90), (44, 84)), KR, 'f', False, False, 1.8), L(quad((76, 84), (66, 90), (56, 84)), KR, 'f', False, False, 1.8)],
  dome('side', top=4, w=48, cy=46, n=8, amp=8, long=104, flare=8, seed=24, fr=56) + [L(quad((72, 74), (80, 64), (90, 70)), KR, 'f', False, False, 2.4)],
  dome('back', top=4, w=48, cy=46, n=8, amp=8, long=104, flare=8, seed=24, ends=5))

# Faye Ted: pelo corto amarillo crema muy claro con un mechón de antena arriba, mechones por la frente; piel morena, ojos
# grandes azules y boca abierta sonriente
C('faye-ted', 'chica', P('#fdf9d3', '#cc9d7b', iris='#2a9ad8', shade='#e0d8a8', deep='#c0b888'),
  F(eyes='big', brows=True, mouth='grin', mouth_y=93, hairline=hl(5, 66, 50, 62, jit=2, seed=25)),
  dome('front', top=6, w=46, cy=48, n=6, amp=6, soft=True, long=92, flare=4, seed=26) + [L(outline([(48, 10), (46, -6), (54, -16, 1), (52, -4), (56, 10)]))],
  dome('side', top=6, w=46, cy=48, n=6, amp=6, soft=True, long=92, flare=4, seed=26, fr=58) + [L(outline([(48, 8), (46, -8), (56, -18, 1), (54, -6), (58, 8)]))],
  dome('back', top=6, w=46, cy=48, n=6, amp=6, soft=True, long=92, flare=4, seed=26, ends=4) + [L(outline([(48, 10), (46, -6), (54, -16, 1), (52, -4), (56, 10)]))])

# Finn Boyle: melena enorme de león color paja en mechones de punta, con dos tornillos gris verdoso clavados arriba; piel
# morena, ojos afilados verde grisáceo y media sonrisa
BOLT2 = _c('#4a6a5a')
C('finn-boyle', 'normal', P('#c6b565', '#b7864d', iris='#5a7a7a', shade='#9a8a48', deep='#7a6a30'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=hl(6, 68, 50, 64, jit=3, seed=27)),
  dome('front', top=0, w=50, cy=46, n=10, amp=10, long=112, flare=12, seed=28) + [L(ell(28, 24, 6, 4), BOLT2, 'f'), L(ell(72, 24, 6, 4), BOLT2, 'f')],
  dome('side', top=0, w=50, cy=46, n=10, amp=10, long=112, flare=12, seed=28, fr=54) + [L(ell(56, 14, 6, 4), BOLT2, 'f')],
  dome('back', top=0, w=50, cy=46, n=10, amp=10, long=112, flare=12, seed=28, ends=5) + [L(ell(28, 24, 6, 4), BOLT2, 'f'), L(ell(72, 24, 6, 4), BOLT2, 'f')])

# Fishel Bucket: gorro de cubo verde con rayas blancas; patillas negras largas hasta la mandíbula, orejas puntiagudas,
# perilla y sonrisa de dientes
BG, BGD = _c('#487d67'), _c('#34403a')
def _bucket(view):
    st = lambda y0, y1, x0=8, x1=92: L(outline([(x0, y0), (x1, y0), (x1, y1), (x0, y1)]), WHITE, 'f', False)
    if view == 'side':
        return [L(outline([(10, 52), (16, 4), (84, 4), (92, 52)]), BG, 'f'), st(18, 24, 14, 86), st(32, 38, 13, 88), L(outline([(4, 52), (98, 52), (96, 60), (6, 60)]), BGD, 'f')]
    return [L(outline([(10, 54), (14, 4), (86, 4), (90, 54)]), BG, 'f'), st(18, 24, 12, 88), st(32, 38, 11, 89), L(outline([(4, 52), (96, 52), (94, 60), (6, 60)]), BGD, 'f')]
C('fishel-bucket', 'normal', P('#232521', '#f9bb7c', iris='#1a1414'),
  F(eyes='closed', brows=False, mouth='grin', mouth_y=94, hairline=False, ears_front=True),
  _bucket('front') + [L(outline([(16, 60), (24, 60), (24, 92), (18, 88)])), L(outline([(84, 60), (76, 60), (76, 92), (82, 88)])),
                      L(outline([(46, 102), (54, 102), (52, 110), (48, 110)]), BLACK, 'f')],
  _bucket('side') + [L(outline([(48, 58), (58, 58), (58, 88), (50, 84)]))],
  _bucket('back') + [L(outline([(12, 58), (88, 58), (86, 82), (50, 88), (14, 82)]))])

# Fletch Blitzen: pelo naranja peinado hacia un lado en un mechón grande que le tapa un ojo y acaba en punta hacia arriba;
# bufanda azul al cuello; el ojo que se ve, azul y afilado
BLU2 = _c('#1e3a98')
C('fletch-blitzen', 'normal', P('#ed8a2c', '#fbe9b9', iris='#2a3a78', shade='#b46026', deep='#8a4618'),
  F(eyes='sharp', brows='angry', mouth='smile', mouth_y=93, hairline=[(8, 64), (16, 50), (34, 44), (54, 46), (74, 50), (92, 64)]),
  dome('front', top=4, w=46, cy=46, sb=70) + [L(outline([(60, 14), (80, -16, 1), (76, 10), (90, 26), (88, 50)])),
                                             L(outline([(12, 44), (54, 40), (52, 92, 1), (40, 70), (24, 86, 1), (18, 60)]), 'mid', 'f')] + scarf('front', BLU2, 100, 12),
  dome('side', top=4, w=46, cy=46, nape=86, fr=50) + [L(outline([(44, 8), (64, -20, 1), (62, 6), (80, 20)]))] + scarf('side', BLU2, 100, 12),
  dome('back', top=4, w=46, cy=46, nape=86) + [L(outline([(60, 14), (80, -16, 1), (76, 10), (90, 26), (88, 50)]))] + scarf('back', BLU2, 100, 12))

# Florence Orderly: cofia de enfermera rosa pálida sobre una media melena verde con flequillo recto; ojos grandes ámbar
NURSE, NURSED = _c('#f0d8d8'), _c('#c8a8a8')
def _nurse(view):
    if view == 'side':
        return [L(outline([(10, 26), (20, 4), (50, -4), (82, 2), (94, 18), (90, 30), (50, 22)]), NURSE, 'f')]
    return [L(outline([(6, 32), (10, 10), (30, -2), (50, -4), (70, -2), (90, 10), (94, 32), (70, 24), (50, 22), (30, 24)]), NURSE, 'f'),
            L(outline([(70, 0), (90, 10), (94, 30), (76, 24)]), NURSED, 'f', False)]
C('florence-orderly', 'chica', P('#95af53', '#f9d8b7', iris='#d8901e', shade='#7b7446', deep='#5a5334'),
  F(eyes='big', brows=False, mouth='smile', mouth_y=92, hairline=[(8, 68), (16, 62), (50, 62), (84, 62), (92, 68)]),
  dome('front', top=8, w=46, cy=48, long=96, flare=0) + _nurse('front'),
  dome('side', top=8, w=46, cy=48, long=96, flare=0, fr=62) + _nurse('side'),
  dome('back', top=8, w=46, cy=48, long=96, flare=0, ends=3) + _nurse('back'))

# Folda Steel: pelo granate peinado hacia atrás con mechones sueltos que le caen por los lados y una coleta baja; una venda
# blanca que le tapa los ojos y una sonrisa tranquila
BAND = _c('#f0ead8')
C('folda-steel', 'chica', P('#842b44', '#fccfa0', iris='#1a1414', shade='#682233', deep='#4e1823'),
  F(eyes='none', brows=False, mouth='smile', mouth_y=93, hairline=[(8, 62), (20, 46), (40, 38), (60, 38), (80, 46), (92, 62)]),
  dome('front', top=2, w=46, cy=46, sb=68) +
  [L(outline([(16, 64), (84, 64), (86, 82), (14, 82)]), BAND, 'f'),
   L(outline([(14, 50), (6, 80), (2, 110, 1), (12, 86), (20, 60)]), 'mid', 'f'), L(outline([(86, 50), (96, 80), (104, 112, 1), (90, 86), (82, 60)]), 'mid', 'f')],
  dome('side', top=2, w=46, cy=46, nape=86, fr=44) + [L(outline([(56, 66), (90, 64), (92, 82), (56, 82)]), BAND, 'f'),
                                                      L(outline([(12, 80), (-4, 96), (-6, 116, 1), (6, 102), (20, 90)]), 'mid', 'f')],
  dome('back', top=2, w=46, cy=46, nape=86) + [L(outline([(10, 66), (90, 66), (90, 78), (10, 78)]), BAND, 'f'),
                                               L(outline([(42, 82), (58, 82), (62, 110, 1), (50, 100), (38, 110, 1)]), 'mid', 'f')])

# Foley Edge: melena verde en forma de seta que se abre a los lados; cara larguísima con nariz alargada, cejas gruesas
# verdes en uve, ojos de párpado caído y labios gruesos rosas
C('foley-edge', 'delgado', P('#5a7d0a', '#f7b77d', iris='#1a1414', shade='#3f5a08', deep='#2a3c06'),
  F(eyes='closed', brows=False, mouth='lips', mouth_w=8, mouth_y=100, face_front=face(chin=112, w=-4), face_side=face_side(chin=10, nose=4),
    hairline=[(8, 58), (20, 46), (50, 40), (80, 46), (92, 58)]),
  [L(outline([(2, 70), (-6, 56), (4, 30), (22, 8), (50, 0), (78, 8), (96, 30), (106, 56), (98, 70), (82, 60), (50, 54), (18, 60)])),
   L(outline([(60, 4), (86, 16), (104, 50), (96, 66), (82, 50)]), 'shade', 'b', False),
   L([(46, 70), (48, 92)], _c('#c88050'), 'f', False, False, 1.4)] + thick_brows(64, 'shade', 4.4, 14, 1.6, 14),
  [L(outline([(56, 52), (60, 40), (80, 36), (92, 20), (70, 4), (40, 0), (14, 10), (-4, 40), (0, 66), (20, 66), (40, 58)]))] + side_brow(64, 'shade', 4.4, 1.6),
  [L(outline([(2, 74), (-6, 56), (4, 30), (22, 8), (50, 0), (78, 8), (96, 30), (106, 56), (98, 74), (50, 80)]))])

# Francie Holly: pelo morado recogido hacia atrás con un mechón sobre la frente y una coleta que le cae por delante del
# hombro; orejas grandes, ojos verdes, mofletes rosas y boca abierta sonriente
C('francie-holly', 'chica', P('#714880', '#fcce9e', iris='#4a8a4a', shade='#5a3955', deep='#423040'),
  F(eyes='big', brows=True, mouth='grin', mouth_y=93, big_ears=2, hairline=[(8, 60), (20, 46), (36, 42), (52, 56), (60, 42), (80, 46), (92, 60)]),
  dome('front', top=4, w=46, cy=46, sb=62) + [L(outline([(70, 84), (80, 84), (78, 112), (66, 124, 1), (70, 104)]), 'mid', 'f')] + blush(88, 22, 4.6),
  dome('side', top=4, w=46, cy=46, nape=86, fr=44) + [L(outline([(30, 80), (40, 78), (44, 110), (36, 122, 1), (32, 100)]), 'mid', 'f')],
  dome('back', top=4, w=46, cy=46, nape=86) + [L(outline([(44, 80), (56, 80), (58, 110), (50, 120, 1), (44, 106)]), 'mid', 'f')])
