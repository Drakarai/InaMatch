"""Academia IA (vr-ai-gakuen, AI学園): personajes propios de Victory Road, con sus modelos 3D de 英雄たちのヴィクトリーロード
en la enciclopedia. Cada uno tiene una sola forma; van como 'vr:<id>'. Muchos llevan aparatos (cascos de música, visores,
gafas): se dibujan como capas de delante."""
from chars import CHARS, L, OUTC, blob, bumpy, ell, outline, pal, rope, strand  # noqa: F401
from chars_vr_toufuu_ikokukan import dots, fr, fre
from heads import quad  # noqa: F401

V = 'vr'
WHITE = (246, 246, 248, 255)
GREYW = (200, 200, 206, 255)
TEAL = (60, 200, 200, 255)
BLUSH = (236, 140, 120, 255)


def phones(band=WHITE, cup=WHITE, ring=TEAL, y=72, top=-4, r=(8, 11)):
    """Cascos de música de frente: diadema por encima de la cabeza y dos auriculares sobre las orejas."""
    return [L(quad((10, y - 6), (50, top - 22), (90, y - 6)), OUTC, 'f', False, False, 7.6), L(quad((10, y - 6), (50, top - 22), (90, y - 6)), band, 'f', False, False, 5.4),
            L(ell(10, y, *r), cup, 'f', ln=True), L(ell(90, y, *r), cup, 'f', ln=True),
            L(ell(10, y, r[0] * 0.45, r[1] * 0.7), ring, 'f', False), L(ell(90, y, r[0] * 0.45, r[1] * 0.7), ring, 'f', False)]


def phones_side(band=WHITE, cup=WHITE, ring=TEAL, y=70, r=(11, 12)):
    return [L(quad((46, y - 8), (52, 10), (56, -10)), OUTC, 'f', False, False, 7.6), L(quad((46, y - 8), (52, 10), (56, -10)), band, 'f', False, False, 5.4),
            L(ell(46, y, *r), cup, 'f', ln=True), L(ell(46, y, r[0] * 0.6, r[1] * 0.6), ring, 'f', False), L(ell(46, y, r[0] * 0.38, r[1] * 0.38), cup, 'f', False)]


def phones_back(band=WHITE, cup=WHITE, y=70, r=(8, 11)):
    return [L(quad((10, y - 6), (50, -26), (90, y - 6)), OUTC, 'f', False, False, 7.6), L(quad((10, y - 6), (50, -26), (90, y - 6)), band, 'f', False, False, 5.4),
            L(ell(8, y, *r), cup, 'f', ln=True), L(ell(92, y, *r), cup, 'f', ln=True)]


# Eugenio Provost (portero): cara redonda y mofletuda, pelo rosa chicle corto con flequillo recto de mechones; cascos de
# música blancos con aros turquesa; ojos verdes de enfado y boquita fruncida
CHARS[f'{V}:eugenio-provost'] = {
    'body': 'normal', 'pal': pal('#e47ad8', '#fde6dc', iris='#8ac83a', shade='#c45ab8', deep='#a04498'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False, 'ears': False,
             'face_front': blob([(14, 52), (50, 36), (86, 52), (92, 78), (86, 100), (66, 110), (50, 112), (34, 110), (14, 100), (8, 78)])},
    'front': [L(outline([(16, 80), (12, 56), (12, 30), (26, 8), (50, 0), (74, 8), (88, 30), (88, 56), (84, 80), (80, 60), (20, 60)])),
              L(outline([(60, 2), (82, 14), (90, 46), (84, 76), (76, 44)]), 'shade', 'b', False),
              fre([(14, 64), (14, 40), (28, 22), (50, 16), (72, 22), (86, 40), (86, 64), (78, 56), (72, 64, 1), (66, 56), (60, 64, 1), (54, 56), (46, 64, 1), (40, 56),
                   (34, 64, 1), (28, 56), (22, 66, 1)], 7)] + phones(),
    'side': [L(outline([(60, 64), (62, 52), (82, 48), (92, 34), (86, 12), (62, 0), (34, 2), (14, 14), (6, 40), (8, 64), (22, 76), (40, 72), (50, 64)])),
             L(outline([(6, 42), (30, 48), (40, 70), (20, 74)]), 'shade', 'b', False),
             fr([(74, 48), (92, 42), (94, 58), (82, 58)])] + phones_side(),
    'back': [L(outline([(16, 80), (12, 56), (12, 30), (26, 8), (50, 0), (74, 8), (88, 30), (88, 56), (84, 80), (50, 86)])),
             L(outline([(56, 2), (82, 14), (90, 50), (84, 78), (62, 84), (68, 40)]), 'shade', 'b', False),
             strand([(50, 2), (50, 80)], 'deep', 'b', 1.0), strand([(14, 50), (50, 56), (86, 50)], 'deep', 'b', 1.0)] + phones_back(),
}

# Pradip Lurning: moreno, pelo azul marino muy oscuro: arriba abultado como una nube con el borde del nacimiento recto, y
# detrás una coleta baja de rizos gruesos; ojos entornados de aburrimiento y media sonrisa
CHARS[f'{V}:pradip-lurning'] = {
    'body': 'normal', 'pal': pal('#2a3448', '#a46a46', iris='#1e1a1a', shade='#1e2636', deep='#141a26'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': [(14, 64), (20, 56), (34, 54), (50, 52), (66, 54), (80, 56), (86, 64)]},
    'front': [L(bumpy(50, 24, 46, 34, n=12, amp=0.06)), L(outline([(14, 70), (12, 44), (88, 44), (86, 70), (50, 60)])),
              L(outline([(58, -6), (88, 10), (96, 40), (86, 60), (74, 30)]), 'shade', 'b', False),
              L(quad((16, 58), (50, 48), (84, 58)), 'deep', 'f', False, False, 1.4)],
    'side': [L(bumpy(52, 20, 40, 28, n=12, amp=0.06)), L(bumpy(70, -6, 14, 12, n=8, amp=0.1)),
             L(outline([(58, 60), (62, 50), (82, 46), (88, 30), (60, 20), (24, 26), (8, 50), (14, 70), (36, 70), (48, 62)])),
             [L(bumpy(10 - 4 * k, 66 + 12 * k, 10 - k, 8, n=7, amp=0.12)) for k in range(4)],
             L(outline([(8, 46), (30, 50), (40, 68), (16, 70)]), 'shade', 'b', False)],
    'back': [L(bumpy(50, 22, 48, 34, n=12, amp=0.06)), L(outline([(14, 74), (12, 44), (88, 44), (86, 74), (50, 80)])),
             [L(bumpy(50, 74 + 12 * k, 14 - k, 9, n=7, amp=0.12)) for k in range(4)],
             L(outline([(56, -6), (90, 10), (98, 40), (84, 70), (70, 40)]), 'shade', 'b', False),
             L(quad((20, 30), (50, 46), (80, 30)), 'deep', 'b', False, False, 1.2)],
}

# Talim Muskel: grandullón de nariz grande; pelo verde azulado rapado muy corto, con las patillas y el borde en un verde
# más claro; cascos de música grises enormes; ojos azules y gesto serio
CHARS[f'{V}:talim-muskel'] = {
    'body': 'corpulento', 'pal': pal('#2a9a80', '#e8a878', iris='#2a4aa0', shade='#1e7a64', deep='#145a48', light='#5ad4c0', nose='#d08a5a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 100, 'nose': (50, 86, 4.4), 'ears': False,
             'hairline': [(14, 70), (20, 54), (30, 50), (36, 44), (50, 42), (64, 44), (70, 50), (80, 54), (86, 70)],
             'face_front': blob([(14, 52), (50, 34), (86, 52), (92, 78), (86, 102), (66, 112), (50, 114), (34, 112), (14, 102), (8, 78)])},
    'front': [L(outline([(14, 80), (10, 50), (14, 26), (30, 8), (50, 4), (70, 8), (86, 26), (90, 50), (86, 80), (50, 70)])),
              L(outline([(12, 62), (16, 50), (26, 50), (24, 72)]), 'light', 'f', False), L(outline([(88, 62), (84, 50), (74, 50), (76, 72)]), 'light', 'f', False),
              L(outline([(60, 6), (82, 20), (90, 46), (80, 50), (74, 30)]), 'shade', 'b', False)] + phones(GREYW, GREYW, (40, 60, 70, 255), 74, 2, (10, 13)),
    'side': [L(outline([(58, 56), (62, 46), (76, 40), (84, 26), (70, 8), (46, 4), (22, 12), (8, 34), (8, 62), (22, 80), (40, 76), (50, 60)])),
             L(outline([(64, 46), (76, 40), (72, 56), (62, 60)]), 'light', 'f', False),
             L(outline([(26, 56), (56, 56), (66, 64), (66, 82), (56, 88), (26, 88), (16, 80), (16, 64)]), GREYW, 'f', ln=True),
             L(outline([(28, 64), (40, 60), (48, 66), (48, 80), (40, 86), (28, 82)]), (226, 226, 230, 255), 'f', ln=True)],
    'back': [L(outline([(16, 84), (12, 50), (16, 26), (32, 8), (50, 4), (68, 8), (84, 26), (88, 50), (84, 84), (50, 90)])),
             L(outline([(56, 6), (82, 20), (88, 52), (70, 56), (66, 30)]), 'shade', 'b', False),
             L(outline([(4, 54), (96, 54), (98, 64), (96, 82), (50, 86), (4, 82), (2, 64)]), GREYW, 'f', ln=True),
             L(ell(4, 70, 6, 10), (226, 226, 230, 255), 'f', ln=True), L(ell(96, 70, 6, 10), (226, 226, 230, 255), 'f', ln=True)],
}

# Synthian Volkel: pelo rubio casi blanco a media melena, peinado de lado, con dos mechones negros gruesos que le cruzan la
# cabeza y le caen sobre la frente y el ojo; ojos turquesa afilados y sonrisa de dientes
CHARS[f'{V}:synthian-volkel'] = {
    'body': 'normal', 'pal': pal('#f2eecc', '#fde2cc', iris='#3ab0b0', shade='#d0c8a0', deep='#aaa078', blk='#1e2432', blk_l='#3a4458'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 100), (4, 80), (8, 60), (6, 34), (20, 8), (46, -4), (76, 4), (94, 24), (98, 50), (94, 78), (86, 96), (80, 66), (20, 66)])),
              L(outline([(60, 0), (86, 12), (98, 44), (90, 90), (80, 56)]), 'shade', 'b', False),
              fre([(10, 76), (12, 44), (26, 20), (50, 10), (74, 18), (90, 40), (90, 72), (84, 56), (74, 48), (64, 52), (56, 60, 1), (50, 50), (40, 52), (28, 60), (20, 76)], 7),
              L(outline([(26, 8), (50, -2), (80, 8), (98, 26), (100, 44, 1), (90, 30), (76, 22), (60, 26), (50, 40), (44, 60), (40, 84, 1), (36, 60), (34, 36), (22, 24)]), 'blk', 'f', ln=True),
              L(outline([(64, 16), (86, 20), (104, 32), (110, 50, 1), (94, 38), (78, 32)]), 'blk', 'f', ln=True)],
    'side': [L(outline([(60, 70), (62, 54), (82, 48), (96, 34), (94, 12), (72, -4), (44, -6), (18, 4), (4, 24), (-2, 50), (2, 80), (-6, 100, 1), (12, 90), (20, 104, 1),
                        (28, 86), (40, 78), (50, 70)])),
             L(outline([(0, 50), (26, 54), (36, 78), (14, 92)]), 'shade', 'b', False),
             L(outline([(14, 10), (44, -4), (80, 0), (98, 16), (104, 40, 1), (88, 26), (64, 18), (40, 22), (14, 40), (-4, 70, 1), (2, 40)]), 'blk', 'f', ln=True),
             fr([(72, 50), (92, 42), (96, 62), (84, 84, 1), (78, 64)])],
    'back': [L(outline([(10, 96), (4, 76), (6, 50), (8, 28), (24, 8), (50, -2), (76, 8), (92, 28), (94, 50), (96, 76), (90, 96), (70, 102), (50, 98), (30, 102)])),
             L(outline([(56, 0), (84, 14), (94, 60), (88, 96), (64, 98), (70, 50)]), 'shade', 'b', False),
             L(outline([(-6, 26), (20, 8), (50, 4), (80, 14), (106, 40, 1), (80, 30), (50, 26), (20, 36), (-10, 54, 1)]), 'blk', 'f', ln=True),
             L(outline([(-4, 60), (30, 50), (70, 56), (104, 80, 1), (70, 70), (30, 66), (0, 76, 1)]), 'blk', 'f', ln=True)],
}

# Randon Datta: pelo gris lavanda claro peinado hacia arriba en una punta, con las sienes despejadas; cejas finas, ojos
# verdes serios y gesto adusto
CHARS[f'{V}:randon-datta'] = {
    'body': 'normal', 'pal': pal('#d6daee', '#fcdcc4', iris='#3ab05a', shade='#a8a4c0', deep='#8a86a4'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'frown', 'mouth_y': 98,
             'hairline': [(16, 68), (18, 54), (24, 46), (34, 42), (50, 40), (66, 42), (76, 46), (82, 54), (84, 68)]},
    'front': [L(outline([(16, 74), (12, 50), (16, 26), (30, 4), (48, -16, 1), (66, 2), (82, 22), (88, 50), (84, 74), (78, 56), (22, 56)])),
              L(outline([(56, -6), (76, 12), (88, 40), (84, 66), (74, 30)]), 'shade', 'b', False),
              strand([(36, 40), (42, 4)], 'deep', 'b', 1.0), strand([(52, 38), (50, 0)], 'deep', 'b', 1.0), strand([(66, 40), (60, 6)], 'deep', 'b', 1.0)],
    'side': [L(outline([(60, 54), (64, 46), (82, 40), (90, 26), (82, 4), (66, -14, 1), (40, -6), (18, 8), (6, 32), (8, 60), (20, 78), (36, 76), (46, 64), (54, 60)])),
             L(outline([(8, 36), (40, 30), (60, 50), (40, 74), (16, 72)]), 'shade', 'b', False),
             strand([(30, 4), (66, -10)], 'deep', 'b', 1.0)],
    'back': [L(outline([(18, 80), (14, 50), (16, 26), (30, 6), (50, -12, 1), (70, 6), (84, 26), (86, 50), (82, 80), (50, 86)])),
             L(outline([(14, 46), (50, 60), (86, 46), (82, 80), (50, 86), (18, 80)]), 'shade', 'b', False),
             strand([(40, 20), (44, 70)], 'deep', 'b', 1.0), strand([(60, 20), (56, 70)], 'deep', 'b', 1.0)],
}

# Chayce Golana: pelo azul marino con un casquete azul claro en el centro, y dos moños en punta como cuernos envueltos en
# vendas grises; pendientes turquesa, ojos grandes con ojeras negras, rubor y sonrisa
CHARS[f'{V}:chayce-golana'] = {
    'body': 'normal', 'pal': pal('#1e3a7a', '#fde2cc', iris='#4a3a5a', shade='#162c5e', deep='#0e1e44', cap='#5aa0d8', wrap='#a8988a'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 88), (10, 60), (12, 34), (24, 12), (50, 4), (76, 12), (88, 34), (90, 60), (84, 88), (80, 66), (20, 66)])),
              L(outline([(16, 30), (-8, 8, 1), (24, 16)])), L(outline([(84, 30), (108, 8, 1), (76, 16)])),
              L(outline([(14, 26), (2, 14), (8, 10), (22, 20)]), 'wrap', 'f', ln=True), L(outline([(86, 26), (98, 14), (92, 10), (78, 20)]), 'wrap', 'f', ln=True),
              L(outline([(32, 60), (30, 30), (40, 14), (60, 14), (70, 30), (68, 60), (50, 56)]), 'cap', 'f', ln=True),
              L(outline([(16, 62), (14, 44), (30, 32), (32, 60)]), 'mid', 'f'), L(outline([(84, 62), (86, 44), (70, 32), (68, 60)]), 'mid', 'f'),
              L(ell(12, 84, 2.4, 3.4), TEAL, 'f', ln=True), L(ell(88, 84, 2.4, 3.4), TEAL, 'f', ln=True),
              L(quad((26, 84), (36, 88), (44, 84)), OUTC, 'f', False, False, 2.6), L(quad((56, 84), (64, 88), (74, 84)), OUTC, 'f', False, False, 2.6)]
             + dots([(26, 90), (74, 90)], BLUSH, 2.4),
    'side': [L(outline([(58, 66), (62, 52), (80, 48), (90, 34), (82, 12), (60, 2), (34, 4), (14, 16), (4, 40), (6, 68), (0, 84, 1), (14, 80), (22, 90, 1), (30, 78), (44, 70)])),
             L(outline([(40, 20), (34, -20, 1), (54, 10)])), L(outline([(38, 12), (46, 6), (52, 14), (42, 20)]), 'wrap', 'f', ln=True),
             L(outline([(70, 46), (64, 20), (78, 10), (90, 30), (88, 46)]), 'cap', 'f', ln=True),
             L(outline([(4, 40), (28, 46), (38, 70), (14, 78)]), 'shade', 'b', False),
             L(ell(50, 80, 2.4, 3.4), TEAL, 'f', ln=True)],
    'back': [L(outline([(14, 86), (10, 60), (12, 34), (24, 12), (50, 4), (76, 12), (88, 34), (90, 60), (86, 86), (74, 92, 1), (66, 84), (56, 94, 1), (50, 84), (42, 94, 1),
                        (34, 84), (24, 92, 1)])),
             L(outline([(16, 30), (-8, 8, 1), (24, 16)])), L(outline([(84, 30), (108, 8, 1), (76, 16)])),
             L(outline([(14, 26), (2, 14), (8, 10), (22, 20)]), 'wrap', 'f', ln=True), L(outline([(86, 26), (98, 14), (92, 10), (78, 20)]), 'wrap', 'f', ln=True),
             L(outline([(56, 6), (84, 18), (90, 60), (84, 84), (62, 86), (70, 40)]), 'shade', 'b', False),
             strand([(50, 6), (50, 40)], 'deep', 'b', 1.0)],
}

# Annalisa Cubon: chica morena con una melena roja en forma de seta, más clara (rosada) por abajo, con un flequillo
# enorme que le tapa un ojo y dos mechones finos que le cuelgan en gancho; un auricular negro con luces turquesa; ojo azul
# y labios amarillos
CHARS[f'{V}:annalisa-cubon'] = {
    'body': 'chica', 'pal': pal('#e04e4e', '#8a5a40', iris='#3a4ab0', shade='#b83838', deep='#902626', low='#f08a80', dev='#2a2a30'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 80), (-4, 74), (-10, 56), (-4, 30), (14, 8), (40, -4), (60, -4), (86, 8), (104, 30), (110, 56), (104, 74), (84, 80), (80, 64), (20, 64)])),
              L(outline([(-8, 56), (108, 56), (104, 74), (84, 80), (20, 80), (-4, 74)]), 'low', 'b', False),
              L(outline([(60, -2), (88, 10), (106, 40), (100, 56), (82, 30)]), 'shade', 'b', False),
              fr([(14, 64), (16, 40), (30, 22), (50, 16), (70, 20), (86, 36), (92, 56), (86, 74), (76, 82, 1), (74, 70), (64, 64), (56, 66), (50, 78, 1), (46, 64), (42, 56),
                  (34, 50), (24, 54)]),
              L(outline([(56, 66), (64, 64), (74, 70), (76, 82), (66, 76)]), 'low', 'f', False),
              L(rope((14, 76), (6, 92), (16, 98), 2.4), 'mid', 'f'), L(rope((86, 76), (94, 92), (84, 98), 2.4), 'mid', 'f'),
              L(outline([(80, 30), (88, 26), (92, 56), (86, 60)]), 'dev', 'f', ln=True), L(outline([(82, 48), (90, 46), (91, 54), (84, 56)]), TEAL, 'f', False),
              L(ell(50, 98, 2.6, 1.6), (230, 200, 60, 255), 'f', False)],
    'side': [L(outline([(62, 62), (64, 52), (84, 46), (100, 30), (92, 8), (64, -6), (34, -4), (10, 10), (-6, 36), (-8, 60), (6, 72), (28, 76), (44, 72), (54, 64)])),
             L(outline([(-8, 54), (60, 56), (54, 66), (28, 76), (6, 72)]), 'low', 'b', False),
             L(outline([(42, 30), (36, 10, 1), (50, 28), (52, 76), (44, 80)]), 'dev', 'f', ln=True), L(outline([(43, 60), (52, 60), (52, 66), (43, 66)]), TEAL, 'f', False),
             L(rope((60, 72), (66, 90), (58, 96), 2.4), 'mid', 'f')],
    'back': [L(outline([(16, 80), (-4, 74), (-10, 56), (-4, 30), (14, 8), (50, -4), (86, 8), (104, 30), (110, 56), (104, 74), (84, 80), (50, 84)])),
             L(outline([(-8, 54), (108, 54), (104, 74), (84, 80), (50, 84), (16, 80), (-4, 74)]), 'low', 'b', False),
             L(rope((22, 80), (14, 92), (24, 98), 2.4), 'mid', 'f'), L(rope((78, 80), (86, 92), (76, 98), 2.4), 'mid', 'f')],
}

# Cleo Balbot: chica de pelo amarillo verdoso con flequillo recto y dos coletas altas que suben en lazo como cuernos, de
# las que salen tirabuzones con anillas blancas; marcas amarillas bajo los ojos y sonrisa
RING = (232, 226, 230, 255)
CHARS[f'{V}:cleo-balbot'] = {
    'body': 'chica', 'pal': pal('#c8c830', '#fde6d8', iris='#2a2a3a', shade='#a4a41e', deep='#7e7e14'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 80), (12, 56), (12, 32), (26, 10), (50, 2), (74, 10), (88, 32), (88, 56), (84, 80), (80, 62), (20, 62)])),
              L(outline([(26, 18), (2, 4), (-10, -16), (-6, -34), (12, -40), (28, -28), (34, 10)])), L(outline([(74, 18), (98, 4), (110, -16), (106, -34), (88, -40), (72, -28), (66, 10)])), L(ell(8, -18, 5, 7), 'deep', 'b', False), L(ell(92, -18, 5, 7), 'deep', 'b', False),
              L(ell(22, 18, 6, 3), RING, 'f', ln=True), L(ell(78, 18, 6, 3), RING, 'f', ln=True),
              [L(ell(4 - 0.6 * k, 50 + 9 * k, 6 - 0.6 * k, 5)) for k in range(5)], [L(ell(96 + 0.6 * k, 50 + 9 * k, 6 - 0.6 * k, 5)) for k in range(5)],
              L(ell(4, 54, 6, 2.6), RING, 'f', ln=True), L(ell(96, 54, 6, 2.6), RING, 'f', ln=True),
              L(ell(2, 72, 5, 2.4), RING, 'f', ln=True), L(ell(98, 72, 5, 2.4), RING, 'f', ln=True),
              L(outline([(60, 4), (82, 16), (88, 46), (84, 76), (76, 44)]), 'shade', 'b', False),
              fre([(14, 66), (14, 40), (28, 22), (50, 16), (72, 22), (86, 40), (86, 66), (80, 62), (72, 64), (60, 62), (50, 64), (40, 62), (28, 64), (20, 62)], 7),
              L([(30, 84), (36, 86)], (230, 200, 40, 255), 'f', False, False, 1.4), L([(70, 84), (64, 86)], (230, 200, 40, 255), 'f', False, False, 1.4)],
    'side': [L(outline([(60, 62), (62, 50), (80, 44), (90, 30), (80, 10), (56, 2), (30, 6), (12, 20), (6, 44), (10, 66), (24, 76), (42, 70), (52, 62)])),
             L(outline([(42, 16), (24, -2), (18, -26), (30, -42), (50, -36), (54, 12)])), L(ell(44, 14, 6, 3), RING, 'f', ln=True),
             [L(ell(24 - 2 * k, 30 + 9 * k, 6 - 0.6 * k, 5)) for k in range(6)], L(ell(22, 40, 6, 2.6), RING, 'f', ln=True), L(ell(18, 58, 5, 2.4), RING, 'f', ln=True),
             L(outline([(6, 44), (28, 48), (38, 70), (20, 74)]), 'shade', 'b', False),
             fr([(72, 46), (92, 40), (92, 56), (80, 56)])],
    'back': [L(outline([(16, 80), (12, 56), (12, 32), (26, 10), (50, 2), (74, 10), (88, 32), (88, 56), (84, 80), (50, 86)])),
             L(outline([(26, 18), (2, 4), (-10, -16), (-6, -34), (12, -40), (28, -28), (34, 10)])), L(outline([(74, 18), (98, 4), (110, -16), (106, -34), (88, -40), (72, -28), (66, 10)])), L(ell(8, -18, 5, 7), 'deep', 'b', False), L(ell(92, -18, 5, 7), 'deep', 'b', False),
             L(ell(22, 18, 6, 3), RING, 'f', ln=True), L(ell(78, 18, 6, 3), RING, 'f', ln=True),
             [L(ell(4 - 0.6 * k, 50 + 9 * k, 6 - 0.6 * k, 5)) for k in range(5)], [L(ell(96 + 0.6 * k, 50 + 9 * k, 6 - 0.6 * k, 5)) for k in range(5)],
             L(ell(4, 54, 6, 2.6), RING, 'f', ln=True), L(ell(96, 54, 6, 2.6), RING, 'f', ln=True),
             L(outline([(56, 4), (82, 16), (88, 50), (84, 78), (62, 84), (68, 40)]), 'shade', 'b', False),
             strand([(50, 4), (50, 84)], 'deep', 'b', 1.0)],
}

# Reubel Kauntless: melena larga y ondulada partida en dos colores (media cabeza negra y media lavanda) que le cae por
# detrás hasta la espalda; visor turquesa sobre los ojos y una sonrisa enorme con la boca abierta
VISOR = (60, 220, 200, 255)
VISOR_F = (30, 40, 70, 255)
CHARS[f'{V}:reubel-kauntless'] = {
    'body': 'normal', 'pal': pal('#a8a8d8', '#fde2cc', iris='#2a2a3a', shade='#8484b8', deep='#64649a', blk='#1e1e2a', blk_s='#141420'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(10, 110), (-6, 96), (0, 80), (-8, 60), (0, 36), (14, 10), (50, -6), (50, 70), (20, 70)])),
              L(outline([(50, -6), (86, 10), (100, 36), (108, 60), (100, 80), (106, 96), (90, 110), (80, 70), (50, 70)]), 'blk', 'b'),
              fr([(12, 66), (14, 40), (28, 18), (50, 10), (50, 50), (36, 52), (24, 60), (18, 70)]),
              fr([(50, 10), (72, 18), (86, 40), (88, 66), (82, 70), (76, 60), (64, 52), (50, 50)], 'blk'),
              L(outline([(20, 68), (80, 68), (82, 78), (64, 84), (50, 80), (36, 84), (18, 78)]), VISOR_F, 'f', ln=True),
              L(outline([(24, 70), (46, 70), (46, 80), (26, 80)]), VISOR, 'f', False), L(outline([(76, 70), (54, 70), (54, 80), (74, 80)]), VISOR, 'f', False)],
    'side': [L(outline([(62, 66), (64, 52), (84, 46), (98, 30), (92, 8), (66, -6), (36, -4), (12, 10), (-6, 34), (-14, 60), (-20, 84), (-10, 98), (10, 100), (30, 96),
                        (44, 86), (54, 70)])),
             L(outline([(80, 0), (94, 10), (98, 30), (86, 44), (82, 20)]), 'blk', 'b'),
             L(outline([(-12, 60), (20, 60), (40, 84), (10, 100), (-14, 92)]), 'shade', 'b', False),
             L(outline([(64, 68), (90, 66), (92, 80), (66, 82)]), VISOR_F, 'f', ln=True), L(outline([(76, 69), (90, 68), (90, 78), (78, 79)]), VISOR, 'f', False)],
    'back': [L(outline([(50, -6), (14, 10), (0, 36), (-8, 60), (0, 80), (-10, 100), (10, 112), (30, 104), (50, 112)]), 'blk', 'b'),
             L(outline([(50, -6), (86, 10), (100, 36), (108, 60), (100, 80), (110, 100), (90, 112), (70, 104), (50, 112)])),
             L(outline([(52, 30), (100, 44), (106, 70), (60, 60)]), 'shade', 'b', False)],
}

# Obert Deance: casco blanco abombado con un visor rojo que le tapa los ojos y dos antenas a los lados; por detrás le
# asoma una coleta larga de pelo azul marino
HELM = (238, 238, 242, 255)
HELM_D = (196, 190, 198, 255)
RED = (222, 40, 60, 255)
CHARS[f'{V}:obert-deance'] = {
    'body': 'normal', 'pal': pal('#1e2a5a', '#fde2cc', iris='#2a2a3a', shade='#141e44', deep='#0e1430'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'line', 'mouth_y': 98, 'hairline': False, 'ears': False},
    'front': [L(outline([(4, 92), (0, 50), (6, 20), (24, 2), (50, -4), (76, 2), (94, 20), (100, 50), (96, 92), (86, 92), (84, 84), (16, 84), (14, 92)]), HELM, 'f'),
              L(outline([(14, 66), (86, 66), (84, 86), (16, 86)]), RED, 'f', ln=True),
              strand([(50, -2), (50, 10), (54, 12), (54, 60)], OUTC, 'f', 1.0),
              L(outline([(16, 40), (16, 14), (34, 4), (40, 30), (34, 44)]), (250, 250, 252, 255), 'f', False),
              L(outline([(84, 40), (84, 14), (66, 4), (60, 30), (66, 44)]), (250, 250, 252, 255), 'f', False),
              L([(0, 70), (-4, 40)], OUTC, 'f', False, False, 3.0), L([(0, 70), (-4, 40)], GREYW, 'f', False, False, 1.8),
              L([(100, 70), (104, 40)], OUTC, 'f', False, False, 3.0), L([(100, 70), (104, 40)], GREYW, 'f', False, False, 1.8),
              L(ell(-4, 38, 1.8, 3), RED, 'f', False), L(ell(104, 38, 1.8, 3), RED, 'f', False)],
    'side': [L(rope((20, 60), (-10, 76), (-34, 76), 10)), L(rope((20, 64), (-6, 84), (-30, 90), 6)),
             L(outline([(14, 84), (6, 50), (12, 18), (36, 0), (64, -4), (88, 10), (96, 40), (96, 64), (90, 84), (60, 90), (36, 92)]), HELM, 'f'),
             L(outline([(70, 62), (98, 60), (98, 80), (72, 82)]), RED, 'f', ln=True),
             L(ell(44, 66, 14, 15), HELM_D, 'f', ln=True), L(ell(44, 66, 8, 9), HELM, 'f', ln=True),
             L([(30, 66), (26, 30)], OUTC, 'f', False, False, 3.0), L([(30, 66), (26, 30)], GREYW, 'f', False, False, 1.8), L(ell(26, 28, 1.8, 3), RED, 'f', False)],
    'back': [L(rope((40, 84), (30, 100), (14, 112), 8)), L(rope((56, 84), (66, 100), (84, 112), 8)), L(rope((50, 84), (50, 100), (48, 116), 8)),
             L(outline([(4, 94), (0, 50), (6, 20), (24, 2), (50, -4), (76, 2), (94, 20), (100, 50), (96, 94), (50, 98)]), HELM, 'f'),
             L(outline([(56, 2), (90, 20), (98, 60), (94, 92), (60, 96), (66, 40)]), HELM_D, 'f', False),
             strand([(50, -2), (50, 14), (46, 16), (46, 96)], OUTC, 'f', 1.0),
             L([(0, 70), (-4, 40)], OUTC, 'f', False, False, 3.0), L([(0, 70), (-4, 40)], GREYW, 'f', False, False, 1.8),
             L([(100, 70), (104, 40)], OUTC, 'f', False, False, 3.0), L([(100, 70), (104, 40)], GREYW, 'f', False, False, 1.8),
             L(ell(-4, 38, 1.8, 3), RED, 'f', False), L(ell(104, 38, 1.8, 3), RED, 'f', False)],
}

# Zuzu Intel: piel morena, pelo blanco crema en forma de medusa (una campana ancha que le cae por los lados) con el borde de
# abajo azul y turquesa; cinta blanca en la frente; ojos azules enormes y sonrisa abierta
CHARS[f'{V}:zuzu-intel'] = {
    'body': 'normal', 'pal': pal('#f2eedc', '#7a4a32', iris='#3a8ad8', shade='#d6ccb4', deep='#b4a890', blue='#2a5ab0', teal='#6ac8c0'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'grin', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(-12, 76), (-8, 60), (4, 38), (16, 14), (36, 0), (50, -2), (64, 0), (84, 14), (96, 38), (108, 60), (112, 76), (98, 74), (86, 64), (80, 50),
                         (20, 50), (14, 64), (2, 74)])),
              L(outline([(-12, 76), (-8, 66), (4, 70), (14, 60), (18, 70), (14, 76), (2, 80)]), 'blue', 'f', ln=True),
              L(outline([(112, 76), (108, 66), (96, 70), (86, 60), (82, 70), (86, 76), (98, 80)]), 'blue', 'f', ln=True),
              L(outline([(60, 0), (84, 14), (100, 44), (108, 64), (90, 60), (80, 36)]), 'shade', 'b', False),
              L(outline([(20, 52), (24, 38), (40, 28), (60, 28), (76, 38), (80, 52), (66, 44), (34, 44)]), 'blue', 'f', ln=True),
              L(quad((22, 50), (50, 34), (78, 50)), WHITE, 'f', False, False, 4.0),
              strand([(48, 0), (50, 16), (52, 0)], 'deep', 'f', 1.0), strand([(30, 10), (12, 60)], 'shade', 'f', 1.0), strand([(70, 10), (88, 60)], 'shade', 'f', 1.0)]
             + dots([(28, 86), (31, 88), (72, 86), (69, 88)], OUTC, 0.8),
    'side': [L(outline([(-24, 78), (-16, 60), (-2, 36), (14, 14), (40, 0), (66, 0), (86, 12), (98, 30), (92, 40), (100, 58), (90, 64), (78, 56), (60, 50), (40, 56),
                        (20, 68), (0, 76)])),
             L(outline([(-24, 78), (-18, 68), (0, 72), (20, 64), (40, 52), (60, 48), (78, 54), (90, 62), (96, 66), (84, 70), (60, 60), (40, 64), (20, 74), (0, 82)]), 'blue', 'f', ln=True),
             L(outline([(-14, 60), (20, 40), (60, 40), (90, 50), (60, 30), (20, 26)]), 'shade', 'b', False)],
    'back': [L(outline([(-10, 82), (-6, 60), (6, 36), (18, 12), (36, 0), (50, -2), (64, 0), (82, 12), (94, 36), (106, 60), (110, 82), (90, 84), (70, 82), (50, 86), (30, 82),
                        (10, 84)])),
             L(outline([(-10, 82), (-6, 74), (10, 78), (30, 74), (50, 78), (70, 74), (90, 78), (106, 74), (110, 82), (90, 88), (70, 86), (50, 90), (30, 86), (10, 88)]), 'blue', 'f', ln=True),
             L(outline([(4, 40), (50, 30), (96, 40), (106, 72), (50, 76), (-6, 72)]), 'shade', 'b', False),
             strand([(30, 30), (24, 76)], 'deep', 'b', 1.0), strand([(50, 20), (50, 80)], 'deep', 'b', 1.0), strand([(70, 30), (76, 76)], 'deep', 'b', 1.0)],
}

# Bren Techner (portero): pelo naranja peinado hacia arriba en un tupé de mechones, con patillas cortas; gafas de buceo
# azul marino redondas sobre los ojos verdes; pendientes dorados y sonrisa
GOG = (30, 46, 80, 255)
CHARS[f'{V}:bren-techner'] = {
    'body': 'normal', 'pal': pal('#f09030', '#fde2cc', iris='#3a9a4a', shade='#d07018', deep='#a8540e'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 98,
             'hairline': [(16, 68), (20, 56), (28, 58), (32, 48), (42, 52), (50, 44), (58, 52), (68, 48), (72, 58), (80, 56), (84, 68)]},
    'front': [L(outline([(16, 76), (12, 54), (8, 34), (2, 16, 1), (18, 20), (22, 2), (36, -12), (50, -18), (64, -12), (78, 2), (82, 20), (98, 16, 1), (92, 34), (88, 54),
                         (84, 76), (78, 58), (22, 58)])),
              L(outline([(58, -14), (78, 2), (90, 30), (86, 70), (76, 40)]), 'shade', 'b', False),
              strand([(34, 44), (40, 0)], 'deep', 'b', 1.0), strand([(50, 40), (50, -12)], 'deep', 'b', 1.0), strand([(66, 44), (60, 0)], 'deep', 'b', 1.0),
              L(ell(36, 76, 10, 9), GOG, 'f'), L(ell(64, 76, 10, 9), GOG, 'f'), L(outline([(44, 72), (56, 72), (56, 78), (44, 78)]), GOG, 'f', False),
              L(ell(36, 76, 6.6, 6), (170, 214, 200, 255), 'f', False), L(ell(64, 76, 6.6, 6), (170, 214, 200, 255), 'f', False),
              L(ell(36, 77, 2.6, 3), (40, 120, 60, 255), 'f', False), L(ell(64, 77, 2.6, 3), (40, 120, 60, 255), 'f', False),
              L([(14, 76), (26, 76)], GOG, 'f', False, False, 3.0), L([(86, 76), (74, 76)], GOG, 'f', False, False, 3.0),
              L(ell(14, 86, 2.2, 3.4), (220, 190, 80, 255), 'f', ln=True), L(ell(86, 86, 2.2, 3.4), (220, 190, 80, 255), 'f', ln=True)],
    'side': [L(outline([(58, 60), (62, 48), (80, 44), (92, 30), (102, 8, 1), (84, 6), (90, -14, 1), (66, -8), (40, -6), (20, -2), (2, 10, 1), (10, 24), (4, 46), (12, 70),
                        (28, 78), (40, 70), (50, 62)])),
             L(outline([(4, 30), (30, 36), (40, 68), (14, 70)]), 'shade', 'b', False),
             L(outline([(72, 68), (88, 66), (92, 76), (88, 86), (72, 86)]), GOG, 'f'), L([(46, 72), (72, 74)], GOG, 'f', False, False, 3.0),
             L(ell(46, 84, 2.2, 3.4), (220, 190, 80, 255), 'f', ln=True)],
    'back': [L(outline([(16, 80), (12, 54), (6, 32), (-4, 14, 1), (16, 18), (22, 2), (36, -10), (50, -16, 1), (64, -10), (78, 2), (84, 18), (104, 14, 1), (94, 32), (88, 54),
                        (84, 80), (50, 86)])),
             L(outline([(14, 50), (50, 60), (86, 50), (84, 80), (50, 86), (16, 80)]), 'shade', 'b', False),
             L(quad((10, 74), (50, 66), (90, 74)), GOG, 'f', False, False, 3.0)],
}

# Cognus Sention: moreno claro con pelo aguamarina en forma de casco liso (raya en medio y la nuca más gris), con el
# flequillo en punta que le baja entre los ojos; ojos azules con raya negra y gesto amargo
CHARS[f'{V}:cognus-sention'] = {
    'body': 'normal', 'pal': pal('#a8eeee', '#d8a07a', iris='#3a6ab0', shade='#7ab8bc', deep='#8a9294', grey='#8e9696'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 94), (4, 60), (8, 30), (22, 6), (50, -2), (78, 6), (92, 30), (96, 60), (90, 94), (82, 66), (18, 66)])),
              L(outline([(60, 0), (84, 12), (96, 50), (90, 90), (80, 56)]), 'shade', 'b', False),
              fre([(10, 84), (12, 46), (24, 22), (50, 12), (76, 22), (88, 46), (90, 84), (82, 68), (70, 62), (58, 66), (50, 84, 1), (42, 66), (30, 62), (18, 68)], 7),
              strand([(50, 12), (50, 60)], 'deep', 'f', 1.0)],
    'side': [L(outline([(62, 70), (64, 54), (84, 48), (96, 32), (90, 10), (66, -4), (36, -2), (12, 12), (2, 36), (2, 70), (14, 92), (30, 92), (40, 80), (52, 70)])),
             L(outline([(2, 40), (40, 30), (60, 52), (40, 80), (30, 92), (14, 92), (2, 70)]), 'grey', 'b', False),
             fr([(72, 50), (92, 42), (94, 62), (88, 82, 1), (80, 64)])],
    'back': [L(outline([(10, 94), (4, 60), (8, 30), (22, 6), (50, -2), (78, 6), (92, 30), (96, 60), (90, 94), (74, 80), (50, 76), (26, 80)])),
             L(outline([(4, 50), (40, 40), (60, 30), (96, 40), (96, 60), (90, 94), (74, 80), (50, 76), (26, 80), (10, 94)]), 'grey', 'b', False),
             strand([(50, 0), (50, 30)], 'deep', 'b', 1.0)],
}

# Manila Brickit: chica de pelo lila con un rizo de antena arriba, dos moños redondos a los lados de la cabeza y mechones
# largos que le caen delante de las orejas; flequillo en mechón central; ojos lilas grandes y la lengua fuera
CHARS[f'{V}:manila-brickit'] = {
    'body': 'chica', 'pal': pal('#b08ad4', '#fde6d4', iris='#6a5ab0', shade='#9070b4', deep='#6e5296'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(16, 80), (12, 56), (12, 32), (26, 10), (50, 2), (74, 10), (88, 32), (88, 56), (84, 80), (80, 60), (20, 60)])),
              L(ell(6, 32, 12, 13)), L(ell(94, 32, 12, 13)),
              L(rope((50, 4), (40, -20), (58, -26), 3.0)),
              L(outline([(60, 4), (82, 16), (88, 46), (84, 76), (76, 44)]), 'shade', 'b', False),
              fre([(14, 58), (16, 36), (30, 20), (50, 14), (70, 20), (84, 36), (86, 58), (76, 54), (64, 50), (60, 58), (54, 66, 1), (46, 66, 1), (40, 58), (36, 50), (24, 54)], 7),
              L(outline([(16, 54), (24, 56), (24, 100), (20, 106, 1), (14, 90)]), 'mid', 'f'), L(outline([(84, 54), (76, 56), (76, 100), (80, 106, 1), (86, 90)]), 'mid', 'f'),
              L(ell(51, 99, 2.4, 2.4), (220, 90, 110, 255), 'f', False)],
    'side': [L(outline([(60, 62), (62, 50), (80, 44), (90, 30), (80, 10), (56, 2), (30, 6), (12, 20), (6, 44), (10, 66), (24, 76), (42, 70), (52, 62)])),
             L(ell(36, 26, 16, 16)), L(ell(36, 26, 9, 9), 'shade', 'f', ln=True),
             L(rope((56, 4), (50, -20), (68, -24), 3.0)),
             L(outline([(58, 50), (64, 52), (66, 96), (62, 104, 1), (56, 86)]), 'mid', 'f'),
             L(outline([(6, 44), (28, 48), (38, 70), (20, 74)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 80), (12, 56), (12, 32), (26, 10), (50, 2), (74, 10), (88, 32), (88, 56), (84, 80), (50, 86)])),
             L(ell(8, 34, 13, 14)), L(ell(92, 34, 13, 14)), L(rope((50, 4), (40, -20), (58, -26), 3.0)),
             L(outline([(16, 70), (20, 100), (14, 106, 1), (10, 80)])), L(outline([(84, 70), (80, 100), (86, 106, 1), (90, 80)])),
             L(outline([(56, 4), (82, 16), (88, 50), (84, 78), (62, 84), (68, 40)]), 'shade', 'b', False),
             strand([(50, 4), (50, 84)], 'deep', 'b', 1.0)],
}

# Nettie Neuralyn: chica de pelo melocotón claro en forma de seta muy ancha, con un mechón partido sobre la frente;
# gafas amarillas redondeadas, ojos verdes, un lunar bajo el ojo y sonrisa suave
CHARS[f'{V}:nettie-neuralyn'] = {
    'body': 'chica', 'pal': pal('#f8c88a', '#fde6dc', iris='#3a8a6a', shade='#e0aa66', deep='#c08a48'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False, 'glasses': (230, 210, 40, 255)},
    'front': [L(outline([(16, 84), (0, 80), (-12, 66), (-12, 46), (2, 22), (22, 4), (50, -4), (78, 4), (98, 22), (112, 46), (112, 66), (100, 80), (84, 84), (80, 66),
                         (20, 66)])),
              L(outline([(60, -2), (86, 10), (108, 40), (108, 66), (92, 60), (80, 30)]), 'shade', 'b', False),
              fre([(14, 66), (14, 40), (28, 20), (50, 12), (72, 20), (86, 40), (86, 66), (80, 60), (72, 56), (60, 56), (54, 50), (46, 64, 1), (40, 52), (28, 58), (20, 68)], 7),
              strand([(4, 50), (0, 70)], 'deep', 'f', 1.0), strand([(96, 50), (100, 70)], 'deep', 'f', 1.0),
              L(ell(25, 82, 0.9, 0.9), OUTC, 'f', False)],
    'side': [L(outline([(60, 66), (64, 52), (84, 46), (98, 32), (92, 10), (66, -4), (36, -4), (10, 10), (-8, 34), (-12, 56), (-4, 72), (14, 80), (34, 82), (48, 72)])),
             L(outline([(-10, 50), (30, 50), (50, 66), (34, 82), (14, 80), (-4, 72)]), 'shade', 'b', False),
             fr([(72, 48), (90, 44), (92, 62), (84, 70), (78, 60)])],
    'back': [L(outline([(16, 86), (0, 80), (-12, 66), (-12, 46), (2, 22), (22, 4), (50, -4), (78, 4), (98, 22), (112, 46), (112, 66), (100, 80), (84, 86), (50, 90)])),
             L(outline([(-12, 54), (50, 50), (112, 54), (112, 66), (100, 80), (84, 86), (50, 90), (16, 86), (0, 80), (-12, 66)]), 'shade', 'b', False),
             strand([(30, 64), (26, 86)], 'deep', 'b', 1.0), strand([(70, 64), (74, 86)], 'deep', 'b', 1.0), strand([(50, 66), (50, 90)], 'deep', 'b', 1.0)],
}

# Deacon Pewter: piel morena, pelo blanco erizado en pinchos cortos por todos lados con un mechón levantado arriba; cejas
# blancas, sombra turquesa bajo los ojos castaños y gesto serio
CHARS[f'{V}:deacon-pewter'] = {
    'body': 'normal', 'pal': pal('#f4f2f0', '#9a6a4a', iris='#5a3a1e', shade='#d4ccd0', deep='#b0a4aa'),
    'face': {'eyes': 'sharp', 'brows': True, 'mouth': 'line', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 86), (2, 82, 1), (10, 70), (-4, 60, 1), (8, 50), (-2, 34, 1), (12, 26), (8, 8, 1), (26, 8), (34, -4), (40, -18, 1), (48, -4), (56, -20, 1),
                         (62, -4), (74, 6), (92, 6, 1), (88, 24), (104, 32, 1), (92, 48), (104, 60, 1), (90, 70), (98, 82, 1), (86, 86), (82, 64), (18, 64)])),
              L(outline([(60, -4), (86, 8), (98, 40), (92, 80), (80, 50)]), 'shade', 'b', False),
              fre([(14, 70), (14, 44), (26, 24), (50, 16), (74, 24), (86, 44), (86, 70), (80, 58), (74, 66, 1), (68, 52), (58, 58, 1), (52, 48), (44, 58, 1), (38, 50),
                   (28, 60, 1), (24, 52), (20, 70, 1)], 7),
              L(quad((28, 82), (36, 84), (44, 82)), (60, 180, 170, 255), 'f', False, False, 2.0), L(quad((56, 82), (64, 84), (72, 82)), (60, 180, 170, 255), 'f', False, False, 2.0)],
    'side': [L(outline([(58, 62), (62, 50), (82, 46), (94, 32), (104, 22, 1), (90, 16), (98, 0, 1), (76, 2), (78, -16, 1), (60, -6), (48, -20, 1), (38, 0), (16, 0, 1),
                        (16, 18), (-2, 26, 1), (8, 40), (-6, 54, 1), (8, 60), (2, 76, 1), (18, 72), (24, 88, 1), (32, 74), (46, 64)])),
             L(outline([(4, 40), (28, 46), (36, 74), (12, 72)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 88), (0, 84, 1), (8, 72), (-6, 62, 1), (6, 50), (-4, 34, 1), (10, 26), (6, 8, 1), (26, 8), (34, -4), (40, -18, 1), (48, -4), (56, -20, 1), (62, -4),
                        (74, 6), (94, 6, 1), (88, 26), (106, 34, 1), (94, 50), (106, 62, 1), (92, 72), (100, 84, 1), (86, 88), (72, 96, 1), (62, 88), (50, 98, 1), (40, 88),
                        (28, 96, 1)])),
             L(outline([(56, -4), (86, 10), (98, 44), (92, 84), (64, 90), (70, 40)]), 'shade', 'b', False),
             strand([(40, 50), (50, 40), (60, 50)], 'deep', 'b', 1.0)],
}
