"""Instituto Brain (ares-mikage-sennou-ares, Mikage Sennou en Ares): sus modelos 3D de Inazuma Eleven Ares como referencia.

Los de IE1 (Harry, Terry, Philip, Noel, Francis, Victor, Neil) tienen en Ares el mismo peinado, pero ya no llevan los
cascos con cable y auriculares del proyecto Brain: van en 'ares:<id>' sin ellos. Jonathan Seller sí cambia (melena ondulada
peinada atrás con coleta). Los nuevos: Oma Nao (portera), Segawa Den, Enami Michiru, Wagano Kakumei (el entrenador con gorra
militar) y Kikai Yattarou (cabeza de caja de cartón de robot)."""
import copy

from chars import CHARS, L, OUTC, ell, outline, pal, rope, strand
from chars_alius import WIDE_FACE

WHITE = (250, 250, 250, 255)
CABLE = (24, 22, 26, 255)
EARBUD = (236, 226, 206, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


def no_headset(pid):
    """El dibujo de IE1 sin el casco del proyecto Brain (cable negro y auriculares)."""
    ch = copy.deepcopy(CHARS[pid])
    for v in ('front', 'side', 'back'):
        flat = [l for it in ch[v] for l in (it if isinstance(it, list) else [it])]
        ch[v] = [l for l in flat if not (l['c'] == CABLE and l['w'] == 2.0) and l['c'] != EARBUD]
    return ch


for _pid in ('harry-leading', 'terry-stronger', 'philip-marvel', 'noel-good', 'francis-tell', 'victor-kind', 'neil-turner'):
    CHARS[f'ares:{_pid}'] = no_headset(_pid)

# ------------------------------------------------------------------ Jonathan Seller (Yamagishi Seri) en Ares
# Melena rosa pálido grisácea ondulada, peinada hacia atrás y hacia un lado (le abulta a la derecha de la imagen), con una
# coleta baja ondulada en la nuca; ojos afilados con raya
CHARS['ares:jonathan-seller'] = {
    'body': 'normal', 'pal': pal('#c8aaa6', '#fcd0a8', iris='#1e2a3a', shade='#9a7c7a', light='#ece0dc'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 72), (10, 36), (20, 10), (42, -2), (64, 0), (84, 8), (100, 22), (104, 44), (98, 66), (92, 82, 1), (86, 64), (84, 52), (20, 52)])),
              L(outline([(60, 2), (86, 10), (102, 36), (96, 70), (86, 56)]), 'shade', 'b', False),
              fringe([(14, 58), (16, 30), (28, 12), (46, 6), (52, 18), (60, 8), (80, 14), (94, 30), (98, 52), (88, 46), (78, 30), (62, 26), (50, 36), (40, 26), (28, 30),
                      (20, 46)]),
              strand([(28, 18), (40, 30)], 'shade', 'f', 1.1), strand([(56, 12), (76, 24)], 'shade', 'f', 1.1), strand([(80, 30), (96, 48)], 'shade', 'f', 1.1),
              L(outline([(30, 8), (46, 4), (40, 14)]), 'light', 'f', False)],
    'side': [L(outline([(16, 54), (2, 64), (-10, 84), (-6, 102, 1), (2, 88), (8, 100, 1), (12, 82), (22, 68)])),
             L(outline([(54, 54), (62, 44), (82, 44), (94, 30), (92, 6), (74, -6), (46, -8), (20, 2), (6, 26), (4, 50), (14, 66), (30, 66), (44, 60)])),
             L(outline([(6, 30), (26, 36), (28, 60), (10, 58)]), 'shade', 'b', False),
             strand([(30, 4), (60, 6), (86, 18)], 'shade', 'f', 1.1), strand([(20, 20), (50, 18), (80, 30)], 'shade', 'f', 1.1),
             L(ell(18, 60, 4, 4), 'shade', 'f', ln=True)],
    'back': [L(outline([(14, 74), (10, 36), (22, 8), (50, -4), (78, 4), (96, 20), (100, 46), (92, 72), (64, 82), (36, 82)])),
             L(outline([(56, -2), (84, 8), (98, 40), (90, 70), (64, 80)]), 'shade', 'b', False),
             L(outline([(40, 76), (60, 76), (64, 96), (58, 114, 1), (50, 100), (42, 114, 1), (36, 96)]), 'mid', 'f', ln=True),
             L(ell(50, 78, 6, 4), 'shade', 'f', ln=True), strand([(30, 10), (24, 50)], 'shade', 'b', 1.0), strand([(70, 10), (78, 50)], 'shade', 'b', 1.0)],
}

# ------------------------------------------------------------------ Gideon Poe (Oma Nao, portera)
# Melena castaño oscuro larga y lisa con raya a un lado: un mechón largo le tapa el ojo izquierdo de la imagen y cae por
# delante del hombro; ojos granates afilados con pestañas
CHARS['gideon-poe'] = {
    'body': 'chica', 'pal': pal('#4a3a30', '#fce0c4', iris='#8a2a2e', shade='#33281f'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'frown', 'mouth_y': 98, 'eye_sep': 15, 'hairline': False},
    'front': [L(outline([(12, 112), (6, 60), (8, 20), (24, -4), (50, -10), (76, -4), (92, 20), (96, 60), (92, 112), (82, 112), (80, 60), (20, 60), (20, 108)])),
              L(outline([(58, -6), (84, 4), (96, 40), (92, 108), (82, 108), (80, 50)]), 'shade', 'b', False),
              fringe([(14, 60), (14, 28), (26, 6), (46, -2), (66, 2), (82, 16), (90, 40), (92, 110), (80, 110), (78, 70), (66, 60), (56, 52), (50, 40), (44, 24), (32, 22),
                      (20, 40)]),
              strand([(54, 4), (66, 50), (80, 104)], 'shade', 'f', 1.1), strand([(72, 8), (84, 60)], 'shade', 'f', 1.1)],
    'side': [L(outline([(54, 62), (60, 50), (82, 50), (94, 34), (92, 8), (72, -8), (40, -10), (14, 4), (2, 40), (0, 80), (4, 112), (34, 116), (42, 96), (46, 74)])),
             L(outline([(2, 40), (26, 46), (34, 110), (8, 110)]), 'shade', 'b', False), strand([(12, 50), (18, 106)], 'deep', 'b', 1.0),
             fringe([(64, 0), (88, 14), (96, 40), (94, 60, 1), (86, 50), (80, 40)])],
    'back': [L(outline([(10, 108), (4, 60), (8, 20), (24, -4), (50, -10), (76, -4), (92, 20), (96, 60), (92, 108), (50, 114)])),
             L(outline([(56, -6), (84, 4), (96, 44), (92, 106), (60, 112), (64, 40)]), 'shade', 'b', False), strand([(36, 4), (32, 106)], 'deep', 'b', 1.0)],
}

# ------------------------------------------------------------------ Electra Faraday (Segawa Den)
# Pelo azul marino muy oscuro peinado hacia atrás tirante y recogido en una coleta altísima que sube en arco y cae hacia un
# lado hasta el hombro; un mechón largo junto a la cara; ojos verdes afilados con raya marcada
CHARS['electra-faraday'] = {
    'body': 'normal', 'pal': pal('#34405a', '#fcd8b4', iris='#3a8a6a', shade='#242c40'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': [(14, 60), (16, 40), (30, 28), (50, 24), (70, 28), (84, 40), (86, 60)]},
    'front': [L(outline([(54, 6), (50, -14), (58, -30), (72, -24), (84, -6), (90, 24), (92, 60), (88, 88, 1), (84, 60), (78, 20), (66, -10), (62, 4)])),
              L(outline([(16, 64), (12, 36), (24, 14), (50, 4), (76, 14), (88, 36), (86, 64), (80, 54), (20, 54)])),
              L(outline([(58, 10), (80, 18), (88, 44), (84, 60), (76, 36)]), 'shade', 'b', False),
              L(ell(54, -2, 6, 4), 'shade', 'f', ln=True), L(outline([(80, 54), (88, 66), (84, 84, 1), (80, 70)]), 'mid', 'f'),
              strand([(30, 20), (40, 8)], 'shade', 'f', 1.0), strand([(50, 16), (52, 4)], 'shade', 'f', 1.0), strand([(70, 20), (60, 8)], 'shade', 'f', 1.0)],
    'side': [L(outline([(40, 8), (30, -20), (20, -34), (0, -30), (-14, -6), (-18, 30), (-12, 70), (-6, 92, 1), (-4, 70), (-6, 30), (2, -10), (16, -20), (30, -8), (46, 12)])),
             L(outline([(54, 58), (60, 46), (80, 46), (92, 32), (86, 12), (64, 2), (40, 4), (18, 14), (8, 36), (10, 60), (22, 74), (38, 72), (46, 64)])),
             L(ell(36, 4, 6, 6), 'shade', 'f', ln=True), strand([(70, 8), (40, 6), (20, 18)], 'shade', 'f', 1.0)],
    'back': [L(outline([(16, 76), (12, 36), (24, 12), (50, 2), (76, 12), (88, 36), (84, 76), (50, 84)])),
             L(outline([(50, 4), (44, -16), (50, -32), (60, -32), (56, -10), (60, 4)]), 'mid', 'f', ln=True),
             L(outline([(46, 2), (22, 20), (6, 50), (2, 80), (8, 98, 1), (12, 76), (20, 46), (40, 20), (54, 6)]), 'mid', 'f', ln=True),
             L(ell(52, 0, 7, 5), 'shade', 'f', ln=True), strand([(30, 20), (40, 70)], 'shade', 'b', 1.0), strand([(70, 20), (60, 70)], 'shade', 'b', 1.0)],
}

# ------------------------------------------------------------------ Darren Gouger (Enami Michiru)
# Piel morena y rastas blancas con sombra rosada, gruesas, que se abren desde lo alto hacia los lados y por detrás hasta la
# nuca; ojos azul claro afilados y media sonrisa
def _dread(p0, c, p1, col='mid', w=9.5):
    return L(rope(p0, c, p1, w), col)


# una masa de rastas detrás (para que no se vean huecos) y rastas gruesas encima, abiertas hacia los lados hasta la mandíbula
_dg_mass_f = L(outline([(6, 90), (-10, 60), (-6, 30), (14, 4), (50, -6), (86, 4), (106, 30), (110, 60), (94, 90), (84, 70), (16, 70)]), 'shade', 'b')
_dg_dreads_f = [_dread((44, 6), (14, 6), (-8, 30)), _dread((56, 6), (86, 6), (108, 30)), _dread((34, 14), (4, 30), (-6, 66), 'shade'),
                _dread((66, 14), (96, 30), (106, 66), 'shade'), _dread((26, 30), (4, 56), (4, 92)), _dread((74, 30), (96, 56), (96, 92)),
                _dread((40, 2), (26, -4), (6, 10)), _dread((60, 2), (74, -4), (94, 10))]
CHARS['darren-gouger'] = {
    'body': 'normal', 'pal': pal('#f2e8e8', '#a8704a', iris='#5a9ac8', shade='#c4a0a4', deep='#9a7478'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': [(14, 56), (22, 46), (32, 50), (40, 42), (50, 48), (60, 42), (68, 50),
                                                                                              (78, 46), (86, 56)]},
    'front': [_dg_mass_f] + _dg_dreads_f + [L(outline([(14, 50), (12, 26), (26, 6), (50, -4), (74, 6), (88, 26), (86, 50), (70, 44), (50, 48), (30, 44)])),
                                            strand([(30, 10), (24, 40)], 'shade', 'b', 1.2), strand([(50, 0), (50, 42)], 'shade', 'b', 1.2),
                                            strand([(70, 10), (76, 40)], 'shade', 'b', 1.2)],
    'side': [L(outline([(34, 4), (8, 4), (-20, 20), (-30, 50), (-20, 80), (0, 98), (30, 100), (40, 70), (50, 50), (70, 36)]), 'shade', 'b'),
             _dread((44, 2), (12, -2), (-22, 22)), _dread((40, 14), (6, 20), (-24, 54)), _dread((34, 28), (4, 48), (-12, 84), 'shade'),
             _dread((30, 40), (12, 70), (8, 100)), _dread((40, 46), (30, 76), (32, 102), 'shade'),
             L(outline([(70, 36), (60, 20), (80, 16), (92, 30), (86, 4), (62, -8), (30, -6), (12, 12), (8, 36), (30, 40)])),
             strand([(80, 10), (40, 6), (14, 22)], 'shade', 'b', 1.2), strand([(84, 26), (50, 22), (16, 38)], 'shade', 'b', 1.2)],
    'back': [L(outline([(-6, 96), (-10, 50), (6, 12), (30, -2), (50, -6), (70, -2), (94, 12), (110, 50), (106, 96), (50, 104)]), 'shade', 'b')]
            + [_dread((x0, 8), (x0 + (x0 - 50) * 0.5, 50), (x0 + (x0 - 50) * 0.7, 98 + (6 if i % 2 else 0)), 'mid' if i % 2 else 'deep')
               for i, x0 in enumerate((14, 24, 34, 44, 56, 66, 76, 86))],
}

# ------------------------------------------------------------------ Des Pott (Wagano Kakumei)
# Grandullón de piel morena con una gorra militar verde oliva de visera, pelo negro rapado debajo, gafas de sol oscuras
# grandes, perilla y bigote de pocos días y cejas fruncidas
CHARS['des-pott'] = {
    'body': 'corpulento', 'pal': pal('#1e2422', '#b07a50', cap='#7a8a3e', cap_d='#5a6a2a', lens='#1e2a4a', lens_l='#4a6aa8', beard='#3a2a20'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'face_front': WIDE_FACE, 'hairline': False, 'big_ears': 1},
    'front': [L(outline([(16, 60), (14, 30), (86, 30), (84, 60), (70, 48), (30, 48)])),
              L(outline([(10, 22), (20, -2), (50, -28), (80, -2), (90, 22), (50, 24)]), 'cap', 'f', ln=True),
              L(outline([(50, -28), (80, -2), (90, 22), (60, 24)]), 'cap_d', 'f', False),
              L(outline([(10, 22), (50, 16), (90, 22), (92, 32), (50, 28), (8, 32)]), 'cap_d', 'f', ln=True),
              L(outline([(20, 58), (46, 58), (48, 66), (44, 78), (24, 78), (18, 66)]), 'lens', 'f', ln=True),
              L(outline([(80, 58), (54, 58), (52, 66), (56, 78), (76, 78), (82, 66)]), 'lens', 'f', ln=True),
              L(outline([(24, 62), (34, 62), (28, 72)]), 'lens_l', 'f', False), L(outline([(58, 62), (68, 62), (62, 72)]), 'lens_l', 'f', False),
              L([(44, 60), (56, 60)], OUTC, 'f', False, False, 2.0),
              L([(28, 48), (42, 54)], OUTC, 'f', False, False, 3.0), L([(72, 48), (58, 54)], OUTC, 'f', False, False, 3.0),
              L(outline([(38, 92), (50, 90), (62, 92), (62, 108), (50, 112), (38, 108)]) + [(38, 92)], 'beard', 'f', False, False, 1.4)],
    'side': [L(outline([(54, 50), (60, 40), (80, 36), (86, 26), (40, 22), (10, 26), (6, 50), (14, 66), (34, 64), (46, 58)])),
             L(outline([(4, 26), (14, 2), (46, -24), (80, -14), (96, 4), (100, 18), (114, 24, 1), (88, 24), (50, 22), (10, 32)]), 'cap', 'f', ln=True),
             L(outline([(4, 26), (14, 6), (40, 2), (60, 18), (10, 32)]), 'cap_d', 'f', False),
             L(outline([(76, 58), (96, 56), (96, 72), (80, 74)]), 'lens', 'f', ln=True), L([(76, 60), (40, 50)], OUTC, 'f', False, False, 2.0),
             L(outline([(80, 92), (96, 92), (94, 108), (82, 110)]) + [(80, 92)], 'beard', 'f', False, False, 1.4)],
    'back': [L(outline([(14, 70), (12, 30), (88, 30), (86, 70), (50, 76)])),
             L(outline([(10, 26), (20, 0), (50, -28), (80, 0), (90, 26), (50, 30)]), 'cap', 'f', ln=True),
             L(outline([(50, -28), (80, 0), (90, 26), (60, 30)]), 'cap_d', 'f', False)],
}

# ------------------------------------------------------------------ Jethro Mackin (Kikai Yattarou)
# Lleva la cabeza metida en una caja de cartón de robot: una pantalla azul con una cara sonriente pixelada, orejeras de
# cartón a los lados, una solapa por abajo y una antena con un rayo amarillo arriba (por detrás, un disco de cartón)
CHARS['jethro-mackin'] = {
    'body': 'normal', 'pal': pal('#a8784a', '#f6c8a0', box='#b08048', box_d='#8a5e34', box_l='#d0a060', screen='#6ac4f6', pix='#2a6aa8', bolt='#f0d830'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'ears': False, 'no_head': True, 'hairline': False},
    'front': [L(outline([(36, -22, 1), (44, -40, 1), (58, -40, 1), (52, -30, 1), (62, -30, 1), (48, -10, 1), (50, -22, 1)]), 'bolt', 'b', ln=True),
              L(ell(50, -10, 9, 4), 'box_d', 'b', ln=True),
              L(outline([(0, 30, 1), (8, 22, 1), (8, 70, 1), (0, 66, 1)]), 'box_d', 'b', ln=True), L(outline([(100, 30, 1), (92, 22, 1), (92, 70, 1), (100, 66, 1)]), 'box_d', 'b', ln=True),
              L(outline([(4, -8, 1), (96, -8, 1), (96, 88, 1), (4, 88, 1)]), 'box', 'b', ln=True),
              L(outline([(-12, 92, 1), (4, 82, 1), (96, 82, 1), (112, 92, 1), (96, 100, 1), (4, 100, 1)]), 'box_l', 'b', ln=True),
              L(outline([(14, 4, 1), (86, 4, 1), (86, 66, 1), (14, 66, 1)]), 'screen', 'f', ln=True),
              L(outline([(26, 16, 1), (34, 16, 1), (34, 36, 1), (26, 36, 1)]), 'pix', 'f', False), L(outline([(66, 16, 1), (74, 16, 1), (74, 36, 1), (66, 36, 1)]), 'pix', 'f', False),
              L([(30, 44), (34, 48), (40, 52), (50, 54), (60, 52), (66, 48), (70, 44)], 'pix', 'f', False, False, 3.0)],
    'side': [L(outline([(44, -12, 1), (46, -34, 1), (50, -34, 1), (50, -12, 1)]), 'box_d', 'b', ln=True),
             L(outline([(6, -8, 1), (96, -8, 1), (96, 88, 1), (6, 88, 1)]), 'box', 'b', ln=True),
             L(outline([(6, 44, 1), (96, 44, 1), (96, 88, 1), (6, 88, 1)]), 'box_d', 'b', False),
             L(outline([(-10, 92, 1), (6, 82, 1), (96, 82, 1), (110, 92, 1), (96, 100, 1), (6, 100, 1)]), 'box_l', 'b', ln=True),
             L(ell(50, 34, 16, 16), 'box_l', 'f', ln=True), L(ell(50, 34, 11, 11), 'bolt', 'f', False)],
    'back': [L(outline([(38, -22, 1), (46, -40, 1), (58, -40, 1), (52, -30, 1), (62, -30, 1), (50, -10, 1), (50, -22, 1)]), 'box_l', 'b', ln=True),
             L(outline([(0, 30, 1), (8, 22, 1), (8, 70, 1), (0, 66, 1)]), 'box_d', 'b', ln=True), L(outline([(100, 30, 1), (92, 22, 1), (92, 70, 1), (100, 66, 1)]), 'box_d', 'b', ln=True),
             L(outline([(4, -8, 1), (96, -8, 1), (96, 88, 1), (4, 88, 1)]), 'box', 'b', ln=True),
             L(outline([(4, 44, 1), (96, 44, 1), (96, 88, 1), (4, 88, 1)]), 'box_d', 'b', False),
             L(outline([(-12, 92, 1), (4, 82, 1), (96, 82, 1), (112, 92, 1), (96, 100, 1), (4, 100, 1)]), 'box_l', 'b', ln=True)],
}
