"""Correcciones de la revisión de diseños (grupo ie2b): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda."""
import copy  # noqa: F401
from chars import CHARS  # noqa: F401
from chars import L, messy, outline, spk  # noqa: E402


def _fix(team, pid, base=None):
    """Copia del dibujo actual de un jugador para corregirlo con la clave de su equipo."""
    c = copy.deepcopy(CHARS[base or pid])
    CHARS[f'{team}:{pid}'] = c
    return c


# ------------------------------------------------------------------ Yokato
# Mick Mishap: la mata de pinchos rubios era tan enorme que se tragaba la cara; en el modelo los pinchos salen hacia
# arriba y a los lados por encima de las sienes, la cara se ve entera y de espaldas asoma la nuca
c = _fix('ie2-yokato', 'mick-mishap')
c['front'] = messy('front', 15, 11, seed=202, rx=50, ry=42, lo=64) + [
    L(outline([(12, 66, 1), (16, 40), (30, 26), (50, 22), (70, 26), (84, 40), (88, 66, 1), (82, 54), (76, 62, 1), (66, 48), (58, 58, 1), (50, 46),
               (42, 58, 1), (34, 48), (24, 62, 1), (18, 54)]), 'mid', 'f'),
    L(outline([(56, 28), (78, 36), (86, 52), (78, 52), (70, 40)]), 'shade', 'f', False)]
c['side'] = messy('side', 16, 9, seed=202, rx=48, ry=42, nape=84, sweep=-0.3) + [spk((58, 30), (88, 40), (92, 64), 5, z='f', light_left=False)]
c['back'] = messy('back', 15, 11, seed=202, rx=50, ry=42, nape=80)
# Louis Leave: de espaldas el tupé plano solo cubre lo alto de la cabeza; la nuca va rapada (piel)
c = _fix('ie2-yokato', 'louis-leave')
c['back'] = [L(outline([(12, 62), (10, 6), (24, -6), (76, -6), (90, 6), (88, 62), (50, 66)])),
             L(outline([(58, -4), (80, -4), (90, 10), (88, 58), (66, 62)]), 'shade', 'b', False)]
# Wiley Cracker: pelo corto de cepillo; de espaldas se le ve la nuca
c = _fix('ie2-yokato', 'wiley-cracker')
c['back'] = [L(outline([(16, 64), (12, 30), (26, 6), (50, 0), (74, 6), (88, 30), (84, 64), (50, 68)])),
             L(outline([(56, 4), (82, 18), (88, 50), (84, 62), (64, 64)]), 'shade', 'b', False)]
CHARS['ie2-yokato:louis-leave']['side'] = [
    L(outline([(50, 60), (34, 64), (12, 58), (10, 4), (24, -6), (80, -6), (94, 6), (88, 36), (76, 44), (64, 46), (56, 52)])),
    L(outline([(12, 30), (40, 40), (42, 58), (14, 56)]), 'shade', 'b', False)]

# ------------------------------------------------------------------ Mar de Árboles (Jukai)
from chars import blob, ell, strand  # noqa: E402
from heads import quad  # noqa: E402
# Cam Mando: bajo la capucha oscura con orejas de gato rosas lleva una careta de calavera crema con dos ojos enormes
# verde azulado rasgados (antes era todo oscuro con ojitos); por detrás la capucha va atada con cintas rosas en cruz
c = _fix('ie2-jukai-team', 'cam-mando')
c['pal']['lens'] = (30, 74, 82, 255)
c['pal']['mask_d'] = (30, 42, 46, 255)
PLATE = blob([(18, 40), (50, 32), (82, 40), (88, 74), (70, 104), (50, 112), (30, 104), (12, 74)])
c['front'] = c['front'] + [L(PLATE, 'filt', 'f', ln=True), L(blob([(60, 40), (82, 42), (86, 74), (70, 100), (66, 70)], 6), (206, 194, 160, 255), 'f', False)]
for cx, s in ((34, 1), (66, -1)):
    c['front'] += [L(blob([(cx - 17 * s, 50), (cx + 12 * s, 56), (cx + 9 * s, 74), (cx - 14 * s, 70)]), 'mask', 'f', ln=True),
                   L(blob([(cx - 14 * s, 53), (cx + 9 * s, 58), (cx + 7 * s, 71), (cx - 11 * s, 67)]), 'lens', 'f', False),
                   L(ell(cx - 4 * s, 61, 2.2, 1.6), (150, 196, 200, 255), 'f', False)]
c['front'] += [L([(50, 40), (54, 46), (50, 52), (46, 46)], 'mask', 'f', False), L([(46, 78), (54, 78), (50, 90)], (206, 194, 160, 255), 'f', ln=True),
               L(quad((36, 98), (50, 104), (64, 98)), 'mask', 'f', False, False, 1.4)]
c['side'] = c['side'] + [L(blob([(62, 34), (90, 40), (100, 68), (96, 100), (74, 110), (62, 76)]), 'filt', 'f', ln=True),
                         L(blob([(78, 56), (96, 60), (96, 72), (80, 70)]), 'mask', 'f', ln=True), L(blob([(81, 59), (94, 62), (94, 69), (83, 68)]), 'lens', 'f', False),
                         L([(12, 40), (62, 44)], 'ear', 'f', False, False, 3), L([(10, 72), (62, 76)], 'ear', 'f', False, False, 3)]
c['back'] = c['back'] + [L(quad((10, 44), (50, 50), (90, 44)), 'ear', 'f', False, False, 3), L(quad((10, 74), (50, 80), (90, 74)), 'ear', 'f', False, False, 3),
                         L([(50, 2), (50, 110)], 'ear', 'f', False, False, 3)]
# Chase Faithfull: no lleva la máscara entera; un casco de piedra con musgo le tapa la cabeza hasta la nariz, con dos
# lentes distintas (una grande gris y una roja), y debajo se le ve la cara morena con la boca abierta enseñando los
# dientes; el pelo morado asoma por los lados y la nuca
from chars import bumpy  # noqa: E402
c = _fix('ie2-jukai-team', 'chase-faithfull')
c['pal'].update({'purple': (112, 84, 150, 255), 'grey': (184, 188, 190, 255)})
c['face'] = {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 94, 'ears': False, 'hairline': False}
HELM_F = blob([(4, 74), (2, 40), (16, 12), (50, 0), (84, 12), (98, 40), (96, 74), (70, 80), (50, 82), (30, 80)])
c['front'] = [L(blob([(-4, 62), (50, 52), (104, 62), (104, 100), (86, 98), (84, 76), (16, 76), (14, 98), (-4, 100)]), 'purple', 'b'),
              L(HELM_F, 'mask', 'f', ln=True), L(blob([(64, 8), (94, 40), (92, 72), (72, 74)], 6), 'mask_d', 'f', False),
              L(bumpy(40, 12, 26, 9, 7, 0.18), 'moss', 'f', False), L(bumpy(82, 34, 9, 10, 6, 0.15), 'moss', 'f', False),
              L(ell(34, 58, 15, 14), 'mask_d', 'f', ln=True), L(ell(34, 58, 12, 11), 'grey', 'f', False), L(ell(34, 58, 5, 5), (40, 44, 48, 255), 'f', False),
              L(ell(68, 60, 10, 9.5), 'mask_d', 'f', ln=True), L(ell(68, 60, 7.4, 7), 'lens', 'f', False), L(ell(66, 58, 2.2, 2), (255, 200, 200, 255), 'f', False),
              L(ell(84, 58, 4, 4), (40, 44, 48, 255), 'f', ln=True)]
c['side'] = [L(blob([(2, 62), (44, 60), (46, 98), (20, 106), (0, 94)]), 'purple', 'f', ln=True),
             L(blob([(8, 78), (6, 40), (20, 12), (50, 0), (80, 8), (96, 34), (100, 64), (84, 72), (50, 76)]), 'mask', 'f', ln=True),
             L(bumpy(44, 10, 26, 8, 7, 0.18), 'moss', 'f', False),
             L(ell(92, 60, 6, 10), 'mask_d', 'f', ln=True), L(ell(93, 60, 4, 7.6), 'grey', 'f', False)]
c['back'] = [L(blob([(-4, 66), (50, 60), (104, 66), (100, 98), (50, 104), (0, 98)]), 'purple', 'b'),
             L(blob([(4, 76), (2, 40), (16, 12), (50, 0), (84, 12), (98, 40), (96, 76), (50, 82)]), 'mask', 'f', ln=True),
             L(blob([(60, 6), (94, 40), (92, 74), (64, 80)], 6), 'mask_d', 'f', False),
             L(bumpy(50, 18, 30, 12, 7, 0.18), 'moss', 'f', False)]
# Roy Daring: de espaldas lo que se ve es su capucha de musgo verde oliva con las dos puntas a los lados
c = _fix('ie2-jukai-team', 'roy-daring')
c['back'] = c['back'] + [L(blob([(-6, 16), (16, 4), (50, 0), (84, 4), (106, 16), (92, 30), (90, 70), (50, 80), (10, 70), (8, 30)]), 'moss', 'f', ln=True),
                         L(blob([(60, 6), (90, 26), (88, 66), (66, 74)], 6), (110, 120, 40, 255), 'f', False)]

# ------------------------------------------------------------------ Manyuuji (Claustro Sagrado)
from chars_yokato import bald  # noqa: E402
from heads import mirror  # noqa: E402
# Max Fortune: los lóbulos de las orejas le cuelgan larguísimos (orejas de Buda) hasta la mandíbula
c = _fix('ie2-manyuuji', 'max-fortune')
LOBE = blob([(4, 62), (16, 62), (19, 84), (16, 108), (9, 112), (3, 100), (2, 80)])
c['front'] = c['front'] + [L(LOBE, 'skin', 'f', ln=True), L(blob([(8, 70), (13, 70), (13, 96), (9, 100)], 4), 'skin_d', 'f', False),
                           L(mirror(LOBE), 'skin', 'f', ln=True), L(mirror(blob([(8, 70), (13, 70), (13, 96), (9, 100)], 4)), 'skin_d', 'f', False)]
c['back'] = c['back'] + [L(LOBE, 'skin', 'f', ln=True), L(mirror(LOBE), 'skin', 'f', ln=True)]
c['side'] = c['side'] + [L(blob([(39, 62), (53, 62), (54, 92), (48, 110), (40, 100)]), 'skin', 'f', ln=True),
                         L(blob([(43, 68), (49, 68), (49, 94), (45, 100)], 4), 'skin_d', 'f', False)]
# Earnest Bookworm: el pelo castaño es un casquete corto en lo alto; de perfil y de espaldas se le ve la cabeza rapada
c = _fix('ie2-manyuuji', 'earnest-bookworm')
c['side'] = bald('side') + [L(outline([(14, 52), (14, 28), (30, 10), (52, 4), (72, 8), (84, 22), (86, 34), (70, 30), (52, 32), (36, 44)]), 'mid', 'f', ln=True),
                            L(outline([(16, 48), (18, 30), (30, 18), (34, 40)]), 'shade', 'f', False)]
c['back'] = bald('back') + [L(outline([(14, 46), (18, 22), (34, 8), (50, 4), (66, 8), (82, 22), (86, 46), (50, 52)]), 'mid', 'f', ln=True),
                            L(outline([(58, 8), (80, 22), (84, 44), (64, 48)]), 'shade', 'f', False)]
# Roman Kandel: no es calvo; un casquete de pelo crema desflecado le cubre lo alto de la cabeza (y la nuca), con el moño
# en espiral encima, y tiene las orejas de punta
c = _fix('ie2-manyuuji', 'roman-kandel')
EAR = [(14, 62), (-6, 52), (6, 72), (14, 80)]
c['front'] = c['front'] + [
    L(outline([(14, 54), (14, 30), (28, 12), (50, 6), (72, 12), (86, 30), (86, 54), (78, 46, 1), (72, 52), (64, 44, 1), (56, 50), (48, 42, 1), (40, 50), (32, 42, 1), (24, 50)]), 'mid', 'f', ln=True),
    L(outline([(60, 10), (80, 22), (86, 48), (76, 42), (70, 24)]), 'shade', 'f', False),
    L(blob(EAR, 4), 'skin', 'f', ln=True), L(mirror(blob(EAR, 4)), 'skin', 'f', ln=True)]
c['side'] = c['side'] + [
    L(outline([(10, 70), (8, 36), (22, 12), (48, 4), (72, 10), (86, 26), (80, 34, 1), (72, 30), (62, 40, 1), (54, 34), (44, 50, 1), (36, 46), (30, 64, 1), (22, 60), (16, 76, 1)]), 'mid', 'f', ln=True),
    L(outline([(12, 60), (14, 34), (26, 20), (30, 44)]), 'shade', 'f', False),
    L(blob([(40, 62), (30, 44), (52, 60), (50, 76)], 4), 'skin', 'f', ln=True)]
c['back'] = c['back'] + [
    L(outline([(10, 84), (8, 36), (22, 12), (50, 4), (78, 12), (92, 36), (90, 84), (82, 74, 1), (74, 84), (66, 74, 1), (58, 86), (50, 76, 1), (42, 86), (34, 74, 1), (26, 84), (18, 74, 1)]), 'mid', 'f', ln=True),
    L(outline([(58, 8), (84, 26), (90, 70), (74, 76), (70, 40)]), 'shade', 'f', False),
    L(blob(EAR, 4), 'skin', 'f', ln=True), L(mirror(blob(EAR, 4)), 'skin', 'f', ln=True)]
# el moño en espiral va encima del casquete (si no, su contorno lo cruza)
for v, cone in (('front', [(36, 12), (41, -4), (50, -22), (59, -4), (64, 12)]), ('side', [(30, 12), (36, -4), (48, -22), (60, -4), (62, 12)]),
                ('back', [(36, 12), (41, -4), (50, -22), (59, -4), (64, 12)])):
    c[v][0]['ln'] = False
    c[v].append(L(blob(cone), 'mid', 'f', ln=True))
    c[v].append(L(quad((40, 4), (50, -1), (60, 4)) if v != 'side' else quad((36, 4), (48, -1), (58, 4)), 'shade', 'f', False, False, 1.2))
c['back'] = [l for l in c['back'] if not (l['z'] == 'f' and l['s'] in (blob(EAR, 4), mirror(blob(EAR, 4))))]
c['back'] = [L(blob(EAR, 4), 'skin', 'b', ln=True), L(mirror(blob(EAR, 4)), 'skin', 'b', ln=True)] + c['back']

# ------------------------------------------------------------------ Osaka Gals CCC
from chars import bumpy as _bumpy  # noqa: E402
# Daisy Fields: el moño de rizos es una mata grande y abultada arriba y hacia atrás, no un pompón pequeño
c = _fix('ie2-osaka-gals-ccc', 'daisy-fields')
c['front'][0] = L(_bumpy(60, -8, 30, 22, 11, 0.12))
c['front'].insert(1, L(_bumpy(70, -6, 16, 14, 7, 0.12), 'shade', 'b', False))
c['side'][0] = L(_bumpy(26, -4, 30, 24, 11, 0.12))
c['side'].insert(1, L(_bumpy(20, 2, 16, 14, 7, 0.12), 'shade', 'b', False))
c['back'][0] = L(_bumpy(56, -6, 32, 24, 11, 0.12))
# Janine Brook: sus dos moños son enormes y se abren a los lados (el peinado es más ancho que la cara); sonríe con picardía
c = _fix('ie2-osaka-gals-ccc', 'janine-brook')
c['face'].update({'brows': True, 'mouth': 'smile'})
c['front'][0] = L(_bumpy(12, 24, 24, 22, 9, 0.1))
c['front'][1] = L(_bumpy(88, 24, 24, 22, 9, 0.1))
c['side'][0] = L(_bumpy(30, 6, 32, 24, 10, 0.1))
c['back'][0] = L(_bumpy(12, 26, 24, 22, 9, 0.1))
c['back'][1] = L(_bumpy(88, 26, 24, 22, 9, 0.1))

# ------------------------------------------------------------------ Prominence / Caos
# Nigel August, Ben Blowton y Jim Flareson no llevan gafas de sol: la franja negra es una marca de alienígena pintada
# alrededor de los ojos, y dentro se les ven los ojos (azules, turquesa y amarillos)
WHITE = (250, 250, 250, 255)
PUPIL = (20, 14, 18, 255)


def _alien_eyes(c, ey, iris, sep=13, side_x=85, pupil=True):
    c['pal']['iris'] = iris
    for cx, s in ((50 - sep, 1), (50 + sep, -1)):
        eye = blob([(cx - 6.5 * s, ey - 1.6), (cx + 1 * s, ey - 3.4), (cx + 6 * s, ey + 0.4), (cx - 1 * s, ey + 3.2)], 6)
        c['front'] += [L(eye, WHITE, 'f', False), L(ell(cx + 1 * s, ey, 2.6, 3.0), 'iris', 'f', False)]
        if pupil:
            c['front'].append(L(ell(cx + 1 * s, ey + 0.4, 1.2, 1.5), PUPIL, 'f', False))
    c['side'] += [L(blob([(side_x - 4, ey - 1.6), (side_x + 3, ey - 3), (side_x + 6, ey + 0.4), (side_x, ey + 3)], 6), WHITE, 'f', False),
                  L(ell(side_x + 2.4, ey, 2.2, 3.0), 'iris', 'f', False)]


for team in ('ie2-prominence', 'ie2-chaos'):
    _alien_eyes(_fix(team, 'nigel-august'), 77.5, (70, 140, 210, 255), 12.5, 81)
    _alien_eyes(_fix(team, 'ben-blowton'), 76.5, (50, 170, 170, 255), 15, 80)
c = _fix('ie2-prominence', 'jim-flareson')
c['pal']['iris'] = (232, 184, 32, 255)
for cx, s in ((36, 1), (64, -1)):
    c['front'].append(L(blob([(cx - 8 * s, 71), (cx + 6 * s, 75.5), (cx + 4 * s, 79), (cx - 6 * s, 76.5)], 6), 'iris', 'f', False))
c['side'].append(L(blob([(80, 72), (90, 75), (89, 78.5), (81, 77)], 6), 'iris', 'f', False))

# ------------------------------------------------------------------ Shin Teikoku
# Maston Color: el sombrero de bruja lo lleva calado hasta los ojos; bajo el ala solo se le ven dos rendijas oscuras
c = _fix('ie2-shin-teikoku-gakuen', 'maston-color')
c['face'].update({'eyes': 'none', 'brows': False, 'ears': False})
c['body'] = 'corpulento'  # en su modelo es rechoncho y barrigón
HAT_F = blob([(-4, 76), (12, 66), (14, 30), (28, 8), (48, -14), (60, -8), (74, 10), (86, 32), (88, 66), (104, 76), (50, 82)])
c['front'] = bald('front') + [L(HAT_F, 'hat', 'f', ln=True), L(blob([(52, -8), (72, 12), (84, 36), (86, 66), (100, 74), (62, 76)], 5), 'hat_d', 'f', False),
                              L(quad((4, 74), (50, 84), (96, 74)), 'hat_d', 'f', False, False, 1.4)]
for cx in (36, 64):
    c['front'].append(L(blob([(cx - 7, 85), (cx, 83.5), (cx + 7, 85), (cx, 88)], 6), (40, 30, 44, 255), 'f', False))
c['side'] = bald('side') + [L(blob([(-12, 74), (8, 64), (10, 30), (28, 6), (54, -14), (68, -6), (80, 12), (88, 40), (90, 64), (112, 76), (50, 82)]), 'hat', 'f', ln=True),
                            L(blob([(8, 60), (12, 32), (26, 12), (28, 50)], 5), 'hat_d', 'f', False),
                            L(blob([(80, 85), (86, 83.5), (90, 85), (86, 88)], 6), (40, 30, 44, 255), 'f', False)]
c['back'] = bald('back') + [L(HAT_F, 'hat', 'f', ln=True), L(blob([(52, -8), (72, 12), (84, 36), (86, 66), (100, 74), (62, 76)], 5), 'hat_d', 'f', False)]

# ------------------------------------------------------------------ Emperadores Oscuros
# Shadow Cimmerian: en su modelo tiene la piel clara (melocotón), no morena
c = _fix('ie2-dark-emperors', 'shadow-cimmerian')
c['pal'].update({'skin': (252, 204, 164, 255), 'skin_d': (226, 172, 136, 255)})

# ------------------------------------------------------------------ Épsilon y Épsilon Plus
# Los alienígenas de Épsilon tienen las orejas de punta (Craven, Kayson, Metron/Mads, Kiburn/Carrie, Zel/Zeke)
EAR_P = blob([(17, 64), (6, 56), (-8, 44), (-2, 60), (6, 78), (16, 84)], 4)
EAR_PI = blob([(14, 66), (6, 60), (0, 54), (4, 64), (8, 74), (14, 78)], 4)
EAR_S = blob([(42, 62), (34, 48), (30, 38), (52, 58), (54, 76), (44, 80)], 4)


def _pointy(c):
    c['face'] = dict(c['face'], ears=False)
    c['front'] = [L(EAR_P, 'skin', 'b', ln=True), L(EAR_PI, 'skin_d', 'b', False),
                  L(mirror(EAR_P), 'skin', 'b', ln=True), L(mirror(EAR_PI), 'skin_d', 'b', False)] + c['front']
    c['back'] = [L(EAR_P, 'skin', 'b', ln=True), L(mirror(EAR_P), 'skin', 'b', ln=True)] + c['back']
    c['side'] = c['side'] + [L(EAR_S, 'skin', 'f', ln=True), L(blob([(44, 64), (38, 52), (48, 62), (49, 74)], 4), 'skin_d', 'f', False)]


SHELL = blob([(-16, 2), (-2, -16), (18, -8), (24, 16), (14, 40), (-6, 36), (-16, 18)])
SHELL_IN = blob([(-8, 6), (2, -6), (14, 0), (16, 18), (8, 32), (-4, 28)])
for team in ('ie2-epsilon', 'ie2-epsilon-kai'):
    for pid in ('craven-kenville', 'kayson-wattever', 'mads-hatter', 'carrie-mccuring', 'zeke-valanche'):
        c = copy.deepcopy(CHARS[f'{team}:{pid}'])
        CHARS[f'{team}:{pid}'] = c
        for v in ('front', 'side', 'back'):  # capas en una lista plana (spk devuelve listas)
            c[v] = [l for it in c[v] for l in (it if isinstance(it, list) else [it])]
        _pointy(c)
        if pid == 'mads-hatter':  # piel tostada grisácea, no marrón oscuro
            c['pal'].update({'skin': (176, 140, 112, 255), 'skin_d': (150, 116, 92, 255)})
        if pid == 'carrie-mccuring':  # los moños van dentro de dos conchas metálicas grandes, no en dos aros pequeños
            for v in ('front', 'back'):
                c[v] = [l for l in c[v] if l['c'] not in ('metal', 'light2') and not (l['c'] == 'mid' and l['z'] == 'f' and len(l['s']) == 36)]
                c[v] = [L(SHELL, 'metal', 'b', ln=True), L(SHELL_IN, 'mid', 'b', ln=True), L(ell(16, 2, 2.6, 2.6), 'light2', 'b', False),
                        L(mirror(SHELL), 'metal', 'b', ln=True), L(mirror(SHELL_IN), 'mid', 'b', ln=True), L(ell(84, 2, 2.6, 2.6), 'light2', 'b', False)] + c[v]
            c['side'] = [l for l in c['side'] if l['c'] not in ('metal', 'light2') and not (l['c'] == 'mid' and l['z'] == 'f' and len(l['s']) == 36)]
            c['side'] = [L([(x + 40, y) for x, y in SHELL], 'metal', 'b', ln=True), L([(x + 40, y) for x, y in SHELL_IN], 'mid', 'b', ln=True)] + c['side']

# Bonnie Sparks: el lazo turquesa de lo alto es enorme (casi tan ancho como la cabeza)
for team in ('ie2-prominence', 'ie2-chaos'):
    c = _fix(team, 'bonnie-sparks')
    for v in ('front', 'side', 'back'):
        for l in (l for it in c[v] for l in (it if isinstance(it, list) else [it])):
            if l['c'] in ('bow', 'bow_d'):
                cx = 50 if v != 'side' else 36
                l['s'] = [(cx + (x - cx) * 1.6, -2 + (y + 2) * 1.6) for x, y in l['s']]
