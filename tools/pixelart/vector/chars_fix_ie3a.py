"""Correcciones de la revisión de diseños (grupo ie3a): redefine con claves '<equipo>:<jugador>' (o las de los
ojeadores 'scouts-<temporada>:<id>') los dibujos que no se parecían al personaje original. Se carga después de todos los
demás módulos (chars.py), así que lo que hay aquí manda."""
import copy  # noqa: F401
from chars import CHARS  # noqa: F401
from chars import L, OUTC, blob, outline, hexc, strand, messy  # noqa: E402,F401
from chars_alius import SIDE_SKULL, SKULL_B  # noqa: E402,F401


def _pal(c, **kw):
    """Cambia colores de la paleta (en hexadecimal)."""
    for k, v in kw.items():
        c['pal'][k] = hexc(v) if isinstance(v, str) else v
    return c


def _fix(tid, pid, base=None):
    """Copia del dibujo actual de un jugador para redefinirlo con la clave '<equipo>:<jugador>'."""
    c = copy.deepcopy(CHARS[base or pid])
    CHARS[f'{tid}:{pid}'] = c
    return c


# ------------------------------------------------------------------ Big Waves
BW = 'ie3-big-waves'
# Hank Tennyson: el pelo es gris marengo con las puntas y los brillos azul claro (no azul entero)
_pal(_fix(BW, 'hank-tennyson'), mid='#56607a', shade='#3c4254', deep='#2c3040', light='#8eb2e2')
# Joe Dawes: solo lleva el tupé ondulado de arriba; la nuca y la parte de atrás de la cabeza van rapadas (piel)
c = _fix(BW, 'joe-dawes')
c['side'] = [L(outline([(16, 36), (20, 6), (44, -6), (70, -6), (92, 6), (100, 22), (90, 30), (76, 36), (58, 38), (40, 38)])),
             L(outline([(18, 30), (34, 30), (40, 36), (20, 36)]), 'shade', 'b', False),
             L(outline([(54, 40), (62, 40), (74, 96), (80, 106), (70, 106), (56, 80)]), 'mid', 'f', ln=True),
             L(outline([(80, 74), (88, 72), (90, 78), (82, 80)]), OUTC, 'f', False)]
c['back'] = [L(blob(SKULL_B), 'skin'),
             L(outline([(14, 40), (12, 26), (20, 6), (50, -6), (80, 6), (88, 26), (86, 40), (66, 46), (50, 44), (34, 46)])),
             L(outline([(56, 0), (82, 12), (88, 38), (66, 44)]), 'shade', 'b', False)]
# Holly Summers: el flequillo le tapa el ojo izquierdo (a la derecha de la imagen)
c = _fix(BW, 'holly-summers')
c['front'][2] = L(outline([(14, 60), (16, 38), (30, 22), (52, 16), (74, 22), (88, 40), (90, 66), (86, 94, 1), (78, 84), (70, 92, 1), (62, 78), (54, 56),
                           (40, 46), (24, 52)]), 'mid', 'f', ln=True)
c['front'][3] = L(outline([(58, 22), (82, 34), (88, 60), (84, 86), (74, 66)]), 'shade', 'f', False)
# Barack Daniels: alto y delgado (no corpulento)
_fix(BW, 'barack-daniels')['body'] = 'delgado'

# ------------------------------------------------------------------ Desert Lion
DL = 'ie3-desert-lion'
# Bilal Kalil: un mechón ondulado le tapa el ojo derecho (a la izquierda de la imagen)
c = _fix(DL, 'bilal-kalil')
c['front'] += [L(outline([(16, 50), (34, 38), (50, 50), (48, 88, 1), (40, 78), (32, 94, 1), (26, 76), (14, 84, 1), (16, 64)]), 'mid', 'f', ln=True),
               L(outline([(36, 44), (46, 52), (44, 76), (38, 64)]), 'shade', 'f', False)]
# Sulayk Sulaiman: de espaldas el moño abultado es castaño; solo lo de arriba es amarillo verdoso
c = _fix(DL, 'sulayk-sulaiman')
_pal(c, bun='#7a6436', bun_d='#5c4a26')
for l in c['back']:
    if l['c'] == 'mid':
        l['c'] = 'bun'
    elif l['c'] == 'shade':
        l['c'] = 'bun_d'
c['back'].insert(len(c['back']) - 2, L(outline([(12, 34), (26, 10), (50, 0), (74, 10), (88, 34), (70, 28), (50, 26), (30, 28)]), 'mid', 'f', ln=True))
# Adel Siddique: pelo gris pizarra con la parte de abajo casi negra (no verde azulado)
_pal(_fix(DL, 'adel-siddique'), mid='#5e7078', shade='#3a3e46', deep='#2a2e34', light='#8a9aa0')

# ------------------------------------------------------------------ Inazuma Japan
IJ = 'ie3-inazuma-japan'
# David Samford: el parche del ojo es gris claro y la parte de atrás del pelo, gris (no negro ni verde menta)
_pal(_fix(IJ, 'david-samford'), patch='#b4b2ac', shade='#aab0a8')

# ------------------------------------------------------------------ Rose Griffon
RG = 'ie3-rose-griffon'
# Kevin Pinot: piel morena más clara y apagada (no anaranjada)
_pal(_fix(RG, 'kevin-pinot'), skin='#b48c72', skin_d='#9a7460')
# Romuald Huysmans: el pelo es castaño malva (no granate)
_pal(_fix(RG, 'romuald-huysmans'), mid='#6e4858', shade='#523442', deep='#3e2632', light='#9a7684')
# Émile Lazare: melena platino revuelta que cae hasta la mandíbula con la cara bien a la vista, y el mechón azul sobre el ojo
# izquierdo (a la derecha de la imagen); antes la bola de pelo le comía la cara
c = _fix(RG, 'mile-lazare')
c['front'] = [L(outline([(-2, 104, 1), (2, 84), (-6, 70, 1), (2, 58), (-2, 40, 1), (8, 30), (6, 12, 1), (22, 14), (30, -4, 1), (42, 8), (54, -6, 1), (62, 8),
                         (76, -2, 1), (80, 14), (96, 10, 1), (94, 30), (104, 40, 1), (98, 58), (106, 70, 1), (98, 84), (102, 104, 1), (86, 96), (80, 70), (20, 70),
                         (14, 96)])),
              L(outline([(60, 4), (80, 6), (96, 34), (98, 80), (90, 96), (84, 60)]), 'shade', 'b', False),

    L(outline([(8, 98, 1), (10, 50), (24, 26), (50, 18), (76, 26), (90, 50), (92, 98, 1), (84, 78), (80, 62, 1), (72, 56), (66, 64, 1), (60, 52), (52, 62, 1),
               (46, 52), (38, 64, 1), (32, 54), (24, 64, 1), (18, 76)]), 'mid', 'f'),
    L(outline([(60, 24), (80, 34), (88, 56), (82, 70), (76, 48)]), 'shade', 'f', False),
    L(outline([(52, 22), (64, 22), (72, 40), (70, 62, 1), (62, 44)]), 'streak', 'f', ln=True)]
c['face']['mouth_y'] = 95
# André Pinson: piel morena grisácea, más clara (no anaranjada)
_pal(_fix(RG, 'andr-pinson'), skin='#a88672', skin_d='#8e6e5c')

# ------------------------------------------------------------------ Team K
TK = 'ie3-team-k'
# Giulio Acuto: lleva la capa roja del capitán por la espalda
_fix(TK, 'giulio-acuto')['cape'] = '#e2584e'
# Amaranto Rubino: rojo carmesí algo más oscuro
_pal(_fix(TK, 'amaranto-rubino'), mid='#b8222a', shade='#8e1820', deep='#6e1218', light='#d85a5e')

# ------------------------------------------------------------------ The Great Horn
GH = 'ie3-the-great-horn'
# Herschel de Villiers: las rastas de delante le caen sobre el ojo izquierdo (a la derecha de la imagen) y lo tapan
c = _fix(GH, 'herschel-de-villiers')
c['front'][2] = L(outline([(36, 22), (60, 14), (82, 22), (92, 40), (94, 66), (88, 96, 1), (80, 84), (72, 94, 1), (62, 84), (50, 94, 1), (46, 66), (36, 44)]),
                  'mid', 'f', ln=True)
c['front'][3:6] = [strand([(46 + k * 10, 18 + k), (56 + k * 9, 52), (60 + k * 12, 86)], 'shade', 'f', 1.4) for k in range(3)]

# ------------------------------------------------------------------ Unicorn
UN = 'ie3-unicorn'
# Billy Dash: alto y delgado
_fix(UN, 'billy-dash')['body'] = 'delgado'
# Petie Pooma: piel morena más clara
c = _pal(_fix(UN, 'petie-pooma'), skin='#a27258', skin_d='#88604a')
c['body'] = 'normal'  # de estatura normal, no bajito
# Bob Bobbins: el pelo es castaño (no verde oliva)
_pal(_fix(UN, 'bob-bobbins'), mid='#6e5634', shade='#4e3c22', deep='#3a2c18', light='#9a825a')

# ------------------------------------------------------------------ Ogre
OG = 'ie3-ogre'
# Lars Luceafăr: de espaldas solo hay la cresta rubia de arriba; la nuca va rapada (piel), cruzada por la correa del parche
c = _fix(OG, 'lars-luceaf-r')
c['back'] = [L(blob(SKULL_B), 'skin'),
             L(outline([(20, 40), (18, 22), (24, 6), (16, -16, 1), (34, -2), (40, -24, 1), (50, -6), (60, -18, 1), (64, 2), (78, 8), (82, 24), (80, 40), (50, 46)])),
             L(outline([(56, 2), (78, 10), (82, 36), (64, 42)]), 'shade', 'b', False),
             L(outline([(10, 30), (86, 70), (82, 80), (8, 40)]), 'band', 'f', ln=True)]
# Mystral Callous: es una chica
_fix(OG, 'mystral-callous')['body'] = 'chica'

# ------------------------------------------------------------------ Little Gigant
# Drago Hill: alto y espigado
_fix('ie3-little-gigant', 'drago-hill')['body'] = 'delgado'


# ------------------------------------------------------------------ pelos de pinchos rehechos con su forma real (antes, el
# patrón genérico de bola de pinchos de messy)
def _mirror_pts(pts):
    return [((100 - q[0], q[1]) + tuple(q[2:])) for q in pts]


# Destra: melenón castaño rojizo de mechones en punta que se abre hacia fuera y baja por los hombros hasta el pecho; la
# cara a la vista, con un mechón en V que baja entre los ojos y dos mechones que la enmarcan; de espaldas, un triángulo
# enorme de puntas hasta media espalda
c = _fix('ie3-dark-angel', 'destra')
DESTRA_SIDE_LOCK = [(12, 62), (20, 66), (19, 96), (12, 120, 1), (8, 94)]
c['front'] = [
    L(outline([(2, 146, 1), (4, 122), (-14, 116, 1), (-2, 100), (-18, 86, 1), (-2, 74), (-14, 56, 1), (4, 48), (-4, 28, 1), (14, 24), (10, 2, 1), (28, 8),
               (30, -14, 1), (42, 0), (50, -20, 1), (58, 0), (70, -14, 1), (72, 8), (90, 2, 1), (86, 24), (104, 28, 1), (96, 48), (114, 56, 1), (102, 74),
               (118, 86, 1), (102, 100), (114, 116, 1), (96, 122), (98, 146, 1), (84, 128), (82, 64), (18, 64), (16, 128)])),
    L(outline([(60, 4), (86, 24), (102, 60), (100, 118), (90, 126), (84, 60)]), 'shade', 'b', False),
    strand([(10, 70), (2, 96), (6, 124)], 'shade', 'b', 1.4), strand([(90, 70), (98, 96), (94, 124)], 'shade', 'b', 1.4),
    L(outline([(16, 80, 1), (16, 50), (30, 30), (50, 24), (70, 30), (84, 50), (84, 80, 1), (76, 62), (66, 58), (56, 62), (50, 84, 1), (44, 62), (34, 58),
               (24, 62)]), 'mid', 'f'),
    L(outline([(58, 28), (76, 34), (84, 54), (78, 64), (68, 46)]), 'shade', 'f', False),
    L(outline(DESTRA_SIDE_LOCK), 'mid', 'f', ln=True), L(outline(_mirror_pts(DESTRA_SIDE_LOCK)), 'mid', 'f', ln=True)]
c['side'] = [
    L(outline([(58, 62), (52, 88), (54, 118), (46, 142, 1), (36, 126), (22, 144, 1), (16, 122), (-2, 128, 1), (2, 106), (-16, 98, 1), (-2, 84), (-18, 66, 1),
               (0, 58), (-12, 36, 1), (8, 32), (4, 8, 1), (22, 12), (26, -12, 1), (40, 2), (52, -18, 1), (58, 2), (76, -8, 1), (76, 12), (98, 16, 1), (90, 32),
               (102, 48, 1), (86, 46), (74, 44), (64, 50)])),
    L(outline([(4, 40), (34, 40), (48, 80), (44, 128), (16, 120), (2, 90)]), 'shade', 'b', False),
    strand([(30, 50), (20, 90), (26, 130)], 'deep', 'b', 1.2)]
c['back'] = [
    L(outline([(-6, 146, 1), (-2, 126), (-20, 118, 1), (-4, 104), (-18, 88, 1), (-2, 76), (-12, 58, 1), (4, 50), (-2, 30, 1), (16, 26), (12, 4, 1), (30, 10),
               (34, -14, 1), (46, 2), (54, -20, 1), (62, 0), (74, -14, 1), (76, 8), (92, 2, 1), (88, 26), (104, 30, 1), (96, 50), (112, 58, 1), (102, 76),
               (118, 88, 1), (104, 104), (120, 118, 1), (102, 126), (106, 146, 1), (86, 136), (70, 148, 1), (56, 136), (40, 148, 1), (26, 136), (12, 148, 1)])),
    L(outline([(56, 10), (90, 30), (104, 80), (104, 136), (70, 142), (64, 60)]), 'shade', 'b', False),
    strand([(50, 40), (50, 80), (44, 120)], 'deep', 'b', 1.2), strand([(26, 50), (12, 100), (16, 136)], 'deep', 'b', 1.2),
    strand([(74, 50), (90, 100), (86, 136)], 'deep', 'b', 1.2)]

# Escavan Malice: pelo azul marino de pinchos que salen hacia arriba y hacia la derecha de la imagen, con un flequillo de
# mechones largos en punta que le baja hasta las mejillas; de perfil, los pinchos barren hacia atrás; de espaldas acaba en
# la nuca
c = _fix('ie3-ogre', 'escavan-malice')
paint = [l for l in c['front'] if l['c'] == OUTC]
c['front'] = [
    L(outline([(8, 90, 1), (10, 66), (-6, 56, 1), (6, 44), (-4, 24, 1), (16, 22), (10, -6, 1), (30, 8), (34, -22, 1), (48, 2), (62, -20, 1), (66, 0),
               (90, -14, 1), (84, 12), (108, 8, 1), (94, 28), (108, 40, 1), (94, 48), (98, 70), (94, 90, 1), (84, 74), (80, 62), (20, 62), (16, 76)])),
    L(outline([(62, 0), (86, 10), (100, 34), (94, 70), (86, 72), (82, 40)]), 'shade', 'b', False)] + paint + [
    # los ojos blancos asoman dentro de la pintura negra
    L([(29, 72), (43, 74.5), (41, 79), (31, 78)], (250, 250, 250, 255), 'f', False), L(blob([(36, 74), (39, 74), (39, 78.5), (36, 78.5)], 4), (40, 30, 30, 255), 'f', False),
    L([(71, 72), (57, 74.5), (59, 79), (69, 78)], (250, 250, 250, 255), 'f', False), L(blob([(61, 74), (64, 74), (64, 78.5), (61, 78.5)], 4), (40, 30, 30, 255), 'f', False),
    L(outline([(10, 88, 1), (14, 48), (28, 30), (50, 24), (72, 30), (86, 46), (92, 88, 1), (84, 68), (80, 84, 1), (72, 60), (56, 72, 1), (52, 58), (46, 74, 1),
               (30, 60), (20, 84, 1), (18, 66)]), 'mid', 'f'),
    L(outline([(58, 28), (78, 36), (88, 56), (80, 64), (70, 44)]), 'shade', 'f', False)]
c['side'] = [
    L(outline([(56, 62), (50, 86), (40, 100, 1), (30, 88), (14, 98, 1), (12, 80), (-12, 74, 1), (4, 62), (-18, 44, 1), (4, 36), (-10, 14, 1), (16, 14),
               (10, -10, 1), (32, 4), (42, -20, 1), (56, 2), (76, -8, 1), (76, 12), (98, 14, 1), (90, 30), (104, 54, 1), (86, 46), (72, 46), (62, 50)])),
    L(outline([(6, 40), (30, 40), (44, 80), (32, 92), (12, 84)]), 'shade', 'b', False)]
c['back'] = [
    L(outline([(16, 98, 1), (8, 80), (-10, 78, 1), (4, 62), (-16, 48, 1), (2, 38), (-6, 14, 1), (18, 16), (14, -10, 1), (34, 4), (42, -20, 1), (56, 2),
               (72, -14, 1), (72, 6), (94, 0, 1), (88, 20), (112, 28, 1), (96, 40), (114, 58, 1), (96, 64), (110, 82, 1), (92, 84), (86, 100, 1), (70, 92),
               (56, 104, 1), (44, 92), (30, 104, 1)])),
    L(outline([(58, 6), (90, 24), (100, 60), (88, 90), (64, 92)]), 'shade', 'b', False),
    strand([(40, 20), (30, 60), (34, 96)], 'deep', 'b', 1.2), strand([(64, 20), (74, 60), (70, 94)], 'deep', 'b', 1.2)]

# Bash Lancer: pelo blanco grisáceo de pinchos enormes que se abren hacia arriba y a los lados, con dos mechones largos y
# lisos que le caen por delante de las orejas hasta el pecho y un flequillo de mechones con uno en punta entre los ojos
c = _fix('ie3-ogre', 'bash-lancer')
mark = [l for l in c['front'] if l['c'] == OUTC]
BASH_LOCK = [(12, 56), (26, 62), (24, 96), (20, 132, 1), (12, 100)]
c['front'] = [
    L(outline([(12, 134, 1), (8, 104), (4, 76), (-16, 62, 1), (4, 50), (-8, 26, 1), (14, 24), (14, 2, 1), (30, 10), (38, -16, 1), (50, 4), (64, -14, 1),
               (68, 6), (88, -4, 1), (84, 18), (110, 22, 1), (94, 36), (114, 56, 1), (96, 58), (96, 80), (92, 106), (88, 134, 1), (80, 110), (80, 66), (20, 66),
               (20, 110)])),
    L(outline([(62, 4), (86, 16), (98, 50), (94, 100), (86, 110), (82, 50)]), 'shade', 'b', False)] + mark + [
    L(outline([(14, 76, 1), (16, 46), (30, 30), (50, 24), (70, 30), (86, 46), (88, 78, 1), (78, 58), (68, 64, 1), (60, 50), (50, 76, 1), (44, 52), (32, 64, 1),
               (24, 52)]), 'mid', 'f'),
    L(outline([(58, 28), (78, 36), (86, 54), (78, 58), (68, 44)]), 'shade', 'f', False),
    L(outline(BASH_LOCK), 'mid', 'f', ln=True), L(outline(_mirror_pts(BASH_LOCK)), 'mid', 'f', ln=True)]
c['side'] = [
    L(outline([(56, 64), (50, 90), (44, 128, 1), (32, 104), (20, 130, 1), (14, 100), (2, 92, 1), (8, 74), (-14, 60, 1), (6, 50), (-6, 24, 1), (16, 20),
               (14, -4, 1), (32, 8), (44, -18, 1), (54, 4), (72, -8, 1), (74, 12), (96, 14, 1), (90, 30), (100, 48, 1), (84, 46), (74, 44), (62, 50)])),
    L(outline([(6, 40), (32, 40), (46, 80), (40, 120), (18, 104), (6, 80)]), 'shade', 'b', False),
    L(outline([(60, 60), (70, 62), (68, 100), (62, 130, 1), (56, 100)]), 'mid', 'f', ln=True)]
c['back'] = [
    L(outline([(10, 134, 1), (8, 104), (-12, 90, 1), (4, 74), (-18, 56, 1), (2, 46), (-8, 22, 1), (16, 20), (16, -4, 1), (34, 8), (44, -18, 1), (56, 4),
               (70, -12, 1), (72, 8), (92, 0, 1), (88, 20), (112, 30, 1), (96, 42), (116, 62, 1), (96, 72), (108, 92, 1), (92, 100), (90, 134, 1), (70, 116),
               (50, 124, 1), (30, 116)])),
    L(outline([(58, 6), (90, 24), (104, 64), (92, 110), (66, 116)]), 'shade', 'b', False),
    strand([(40, 30), (34, 80), (36, 116)], 'deep', 'b', 1.0), strand([(62, 30), (68, 80), (66, 116)], 'deep', 'b', 1.0)]

# Wenel: pelo rubio de rizos ondulados como llamas que suben hacia arriba (no una bola de pinchos); el flequillo ondulado
# le llega a las cejas y por detrás acaba en la nuca
c = _fix('ie3-dark-angel', 'wenel')
c['front'] = [
    L(outline([(16, 76), (8, 58), (10, 40), (2, 30, 1), (14, 24), (12, 8), (20, -6, 1), (30, 4), (34, -14), (44, -24, 1), (48, -8), (58, -16), (64, -30, 1),
               (68, -14), (76, -4), (88, -10, 1), (86, 4), (94, 16), (100, 28, 1), (92, 36), (96, 54), (86, 76), (82, 62), (18, 62)])),
    L(outline([(66, -10), (86, 4), (96, 30), (92, 58), (84, 66), (80, 30)]), 'shade', 'b', False),
    strand([(30, 10), (38, -4), (44, -18)], 'shade', 'b', 1.4), strand([(54, 6), (60, -10), (64, -24)], 'shade', 'b', 1.4),
    strand([(18, 40), (10, 32)], 'shade', 'b', 1.4),
    L(outline([(14, 70), (14, 50), (26, 32), (50, 26), (74, 32), (86, 50), (86, 70, 1), (78, 58), (70, 64, 1), (62, 52), (52, 62, 1), (44, 52), (34, 62, 1),
               (26, 54), (20, 66, 1)]), 'mid', 'f'),
    L(outline([(58, 30), (78, 38), (84, 56), (76, 58), (68, 44)]), 'shade', 'f', False)]
c['side'] = [
    L(outline([(56, 64), (50, 84), (40, 86), (26, 82), (16, 84, 1), (12, 66), (0, 58, 1), (8, 46), (-2, 30, 1), (12, 24), (10, 4), (22, -8, 1), (30, 2),
               (38, -16), (50, -28, 1), (54, -10), (66, -6), (78, -14, 1), (80, 4), (94, 14, 1), (92, 30), (100, 44, 1), (86, 46), (74, 44), (62, 50)])),
    L(outline([(8, 40), (32, 40), (46, 76), (30, 84), (14, 76)]), 'shade', 'b', False),
    strand([(24, 30), (34, 10), (44, -10)], 'shade', 'b', 1.4)]
c['back'] = [
    L(outline([(16, 84), (8, 64), (2, 44, 1), (12, 34), (8, 14), (18, -2, 1), (30, 4), (36, -14), (46, -24, 1), (50, -8), (60, -18), (66, -32, 1), (70, -14),
               (80, -6), (92, -8, 1), (90, 8), (96, 22), (104, 32, 1), (94, 42), (94, 64), (86, 84), (70, 92), (50, 86), (32, 92)])),
    L(outline([(20, 50), (50, 44), (82, 52), (86, 80), (70, 90), (50, 84), (30, 90), (16, 78)]), 'shade', 'b', False),
    strand([(40, 10), (46, -6), (48, -18)], 'shade', 'b', 1.4), strand([(66, 8), (70, -8)], 'shade', 'b', 1.4)]


def _squash(c, views, y0, ky, kx=1.0):
    """Acorta lo que cuelga por debajo de y0 (melenas demasiado largas) y lo estrecha hacia el centro."""
    for v in views:
        for l in c[v]:
            l['s'] = [((50 + (x - 50) * kx, y0 + (y - y0) * ky) if y > y0 else (x, y)) for x, y in l['s']]


# la melena de Destra le llega a los hombros y algo más (no hasta la cintura), y la de Bash Lancer por detrás, a los hombros
_squash(CHARS['ie3-dark-angel:destra'], ('front', 'side', 'back'), 60, 0.62, 0.9)
_squash(CHARS['ie3-ogre:bash-lancer'], ('back',), 70, 0.55)
