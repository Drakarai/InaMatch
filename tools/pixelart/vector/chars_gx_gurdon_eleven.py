"""Los Magmavís (gx-gurdon-eleven, Gurdon Eleven): los aviares del planeta Gurdon, con la cabeza entera de pájaro (búho,
águila, secretario, picozapato...) y un manto de plumas que les cae por el cuello hasta los hombros. Sus modelos 3D de
Galaxy como referencia (busto de frente, perfil y espalda). Las cabezas no son humanas: todo lo dibujan sus capas."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from heads import quad  # noqa: F401

NOFACE = {'eyes': 'none', 'brows': False, 'mouth': 'none', 'ears': False, 'hairline': False, 'no_head': True}
WHITE = (250, 250, 250, 255)
BLACK = (24, 20, 24, 255)


def eye(cx, cy, rx, ry, iris, pupil=0.45, ring=None, sclera=WHITE, look=0.0):
    """Ojo de pájaro redondo: el blanco (o un anillo de color), el iris y la pupila."""
    out = []
    if ring:
        out.append(L(ell(cx, cy, rx + 2.2, ry + 2.2), ring, 'f', ln=True))
    out += [L(ell(cx, cy, rx, ry), sclera, 'f', ln=True), L(ell(cx + look, cy, rx * 0.72, ry * 0.72), iris, 'f', False),
            L(ell(cx + look, cy, rx * pupil, ry * pupil), BLACK, 'f', False), L(ell(cx + look - rx * 0.25, cy - ry * 0.3, rx * 0.18, ry * 0.18), WHITE, 'f', False)]
    return out


def side_eye(cx, cy, r, iris, ring=None):
    out = [L(ell(cx, cy, r + 2, r + 2.4), ring, 'f', ln=True)] if ring else []
    return out + [L(ell(cx, cy, r * 0.7, r), WHITE, 'f', ln=True), L(ell(cx + r * 0.15, cy, r * 0.45, r * 0.7), iris, 'f', False),
                  L(ell(cx + r * 0.2, cy, r * 0.22, r * 0.36), BLACK, 'f', False)]


def mean_brow(x0, y0, x1, y1, w=2.6):
    return L([(x0, y0), (x1, y1)], OUTC, 'f', False, False, w)


# ------------------------------------------------------------------ Aoba Gyr (portero): grifo de plumas pardo oliva con dos
# penachos enormes en punta abiertos hacia arriba, un monóculo de piloto de metal en el ojo izquierdo de la imagen sujeto
# con una correa marrón, el ojo derecho marrón, pico crema sonriente y el manto de plumas cayendo largo hasta el pecho
CHARS['aoba-gyr'] = {
    'body': 'corpulento', 'pal': pal('#8a7a5c', '#8a7a5c', shade='#6c5e44', deep='#54482f', beak='#eedcae', beak_d='#c8b07a', strap='#4a2e1e',
                                     rim='#c8c8cc', lens='#f6f6f6', iris='#8a3a1e'),
    'face': NOFACE,
    'front': [L(outline([(-6, 130), (-10, 90), (0, 60), (4, 30), (-14, -24, 1), (20, 6), (50, -2), (80, 6), (114, -24, 1), (96, 30), (100, 60), (110, 90),
                         (106, 130), (80, 120), (66, 132, 1), (56, 118), (44, 118), (34, 132, 1), (20, 120)])),
              L(outline([(60, 0), (84, 8), (110, -18), (96, 32), (104, 80), (104, 124), (82, 116), (84, 60)]), 'shade', 'b', False),
              L(outline([(-6, -12), (16, 10), (8, 22)]), 'shade', 'b', False),
              strand([(30, 96), (24, 112), (32, 124)], 'deep', 'f', 1.2), strand([(70, 96), (76, 112), (68, 124)], 'deep', 'f', 1.2),
              strand([(16, 70), (10, 100)], 'deep', 'f', 1.0), strand([(84, 70), (90, 100)], 'deep', 'f', 1.0),
              L([(0, 50), (30, 44), (50, 48), (70, 40), (100, 46)], 'strap', 'f', False, False, 3.2),
              L(outline([(26, 68), (50, 62), (74, 68), (70, 86), (58, 96), (50, 104, 1), (42, 96), (30, 86)]), 'beak', 'f', ln=True),
              L(outline([(50, 74), (68, 72), (62, 88), (50, 102)]), 'beak_d', 'f', False),
              L(quad((32, 84), (50, 92), (68, 84)), OUTC, 'f', False, False, 1.4), L(ell(46, 74, 1.2, 1.2), OUTC, 'f', False), L(ell(54, 74, 1.2, 1.2), OUTC, 'f', False),
              L(ell(32, 54, 10, 10), 'rim', 'f', ln=True), L(ell(32, 54, 6.6, 6.6), 'lens', 'f', False),
              L(outline([(56, 52), (74, 46), (78, 56), (64, 62)]), WHITE, 'f', ln=True), L(ell(68, 54, 3.4, 3.8), 'iris', 'f', False),
              L(ell(68, 54, 1.6, 2), BLACK, 'f', False), mean_brow(56, 46, 78, 42)],
    'side': [L(outline([(30, 132), (-8, 120), (-12, 80), (0, 40), (6, 20), (-6, -14, 1), (22, 8), (44, 0), (40, -26, 1), (60, 2), (80, 10), (92, 32), (92, 54),
                        (86, 64), (64, 70), (50, 90), (54, 126)])),
             L(outline([(-8, 60), (22, 70), (40, 120), (6, 124)]), 'shade', 'b', False),
             L(outline([(70, 60), (100, 64), (112, 74), (104, 84), (92, 86), (74, 82)]), 'beak', 'f', ln=True),
             L(quad((80, 78), (96, 82), (106, 80)), OUTC, 'f', False, False, 1.2),
             L([(2, 46), (40, 46), (78, 50)], 'strap', 'f', False, False, 3.2),
             L(ell(80, 52, 5.4, 7.4), 'rim', 'f', ln=True), L(ell(81, 52, 3.4, 5), 'lens', 'f', False)],
    'back': [L(outline([(-6, 130), (-10, 90), (0, 60), (4, 30), (-14, -24, 1), (20, 6), (50, -2), (80, 6), (114, -24, 1), (96, 30), (100, 60), (110, 90),
                        (106, 130), (50, 136)])),
             L(outline([(56, 0), (84, 8), (110, -18), (96, 32), (106, 90), (104, 128), (64, 132)]), 'shade', 'b', False),
             L([(0, 52), (30, 58), (50, 60), (70, 58), (100, 52)], 'strap', 'f', False, False, 3.2),
             L(outline([(40, 30), (60, 30), (66, 42), (50, 46), (36, 42)]), 'deep', 'b', False)],
}

# Mayon: pájaro azul marino de cabeza redonda con un penacho larguísimo que sale de lo alto y se enrosca hacia la derecha,
# dos manchas negras encima de los ojos amarillos, pico amarillo corto y el plumaje cayendo en mechones como tentáculos
CHARS['mayon'] = {
    'body': 'normal', 'pal': pal('#3c5a8e', '#3c5a8e', shade='#2c4470', deep='#1e3058', beak='#f2d860', beak_d='#c8a830', iris='#c8c020'),
    'face': NOFACE,
    'front': [L(outline([(44, 4), (40, -20), (48, -40), (66, -48), (76, -42), (66, -40), (56, -32), (54, -16), (58, 4)])),
              L(outline([(66, -48), (84, -50), (90, -60, 1), (92, -46), (78, -40)]), 'mid', 'b', ln=True),
              L(outline([(10, 120), (2, 100), (6, 70), (6, 40), (16, 14), (50, 2), (84, 14), (94, 40), (94, 70), (98, 100), (90, 120), (78, 108), (70, 124, 1),
                         (60, 106), (50, 124, 1), (40, 106), (30, 124, 1), (22, 108)])),
              L(outline([(60, 6), (86, 16), (94, 50), (94, 110), (78, 104), (82, 60)]), 'shade', 'b', False),
              strand([(26, 86), (20, 116)], 'deep', 'f', 1.2), strand([(74, 86), (80, 116)], 'deep', 'f', 1.2), strand([(50, 100), (50, 120)], 'deep', 'f', 1.2),
              L(ell(34, 54, 9, 7), BLACK, 'f', False), L(ell(66, 54, 9, 7), BLACK, 'f', False),
              L(ell(34, 38, 2, 2.4), BLACK, 'f', False), L(ell(66, 38, 2, 2.4), BLACK, 'f', False),
              L(ell(34, 56, 5, 4.4), 'iris', 'f', False), L(ell(66, 56, 5, 4.4), 'iris', 'f', False),
              L(ell(34, 57, 2.2, 2.8), BLACK, 'f', False), L(ell(66, 57, 2.2, 2.8), BLACK, 'f', False),
              L(outline([(32, 70), (50, 64), (68, 70), (60, 80), (50, 86, 1), (40, 80)]), 'beak', 'f', ln=True),
              L(outline([(50, 66), (66, 70), (58, 80), (50, 84)]), 'beak_d', 'f', False)],
    'side': [L(outline([(42, 4), (34, -20), (40, -42), (58, -52), (68, -46), (56, -40), (48, -24), (54, 4)])),
             L(outline([(36, 120), (6, 112), (-6, 80), (0, 40), (16, 10), (48, 0), (76, 12), (88, 36), (88, 56), (80, 66), (56, 70), (52, 100), (58, 122)])),
             L(outline([(-4, 50), (22, 60), (40, 116), (8, 112)]), 'shade', 'b', False),
             L(outline([(74, 56), (104, 62), (118, 70), (104, 76), (78, 72)]), 'beak', 'f', ln=True),
             L(ell(76, 46, 6, 5), BLACK, 'f', False), L(ell(78, 47, 3, 3.4), 'iris', 'f', False), L(ell(79, 47, 1.4, 2), BLACK, 'f', False)],
    'back': [L(outline([(44, 6), (40, -20), (48, -40), (66, -48), (76, -42), (66, -40), (56, -32), (54, -16), (58, 6)])),
             L(outline([(8, 118), (2, 90), (6, 40), (16, 14), (50, 2), (84, 14), (94, 40), (98, 90), (92, 118), (50, 124)])),
             L(outline([(56, 6), (86, 16), (96, 60), (94, 116), (60, 120)]), 'shade', 'b', False),
             L(outline([(4, 76), (96, 76), (96, 118), (50, 124), (6, 118)]), 'deep', 'b', False)],
}

# Merapil Sekretair: pájaro secretario de cabeza blanca, con la parte de abajo malva rosada, un antifaz naranja alrededor de
# los ojos grises, pico pálido largo y tres plumas negras largas a cada lado que salen de la nuca en abanico
_quills_f = [L(quad((22, 34), (4, 14), (-22, 6)), 'quill', 'b', False, False, 3.4), L(quad((14, 48), (-8, 40), (-28, 42)), 'quill', 'b', False, False, 3.4),
             L(quad((14, 62), (-6, 66), (-24, 74)), 'quill', 'b', False, False, 3.4),
             L(quad((78, 34), (96, 14), (122, 6)), 'quill', 'b', False, False, 3.4), L(quad((86, 48), (108, 40), (128, 42)), 'quill', 'b', False, False, 3.4),
             L(quad((86, 62), (106, 66), (124, 74)), 'quill', 'b', False, False, 3.4)]
CHARS['merapil-sekretair'] = {
    'body': 'normal', 'pal': pal('#f2f4f8', '#f2f4f8', shade='#d8dce6', pink='#c8a0a8', pink_d='#a8808a', quill='#2a2e44', mask='#f0a030',
                                 beak='#f0e6d0', beak_d='#cfc0a0', iris='#8a9a8a'),
    'face': NOFACE,
    'front': _quills_f + [L(outline([(10, 120), (6, 80), (8, 40), (20, 14), (50, 2), (80, 14), (92, 40), (94, 80), (90, 120), (50, 126)])),
                          L(outline([(6, 90), (24, 86), (30, 104), (20, 122), (8, 120)]), 'pink', 'f', False),
                          L(outline([(94, 90), (76, 86), (70, 104), (80, 122), (92, 120)]), 'pink', 'f', False),
                          L(outline([(70, 10), (88, 26), (92, 60), (84, 60)]), 'shade', 'f', False),
                          L(outline([(18, 46), (36, 40), (50, 48), (64, 40), (82, 46), (80, 62), (64, 66), (50, 60), (36, 66), (20, 62)]), 'mask', 'f', ln=True)]
             + eye(32, 53, 5.2, 5, 'iris') + eye(68, 53, 5.2, 5, 'iris')
             + [mean_brow(22, 44, 40, 48, 2.2), mean_brow(78, 44, 60, 48, 2.2),
                L(outline([(40, 60), (50, 56), (60, 60), (56, 82), (50, 100, 1), (44, 82)]), 'beak', 'f', ln=True),
                L(outline([(50, 58), (60, 60), (55, 84), (50, 98)]), 'beak_d', 'f', False)],
    'side': [L(quad((24, 30), (0, 0), (-24, -30)), 'quill', 'b', False, False, 3.4), L(quad((20, 40), (-6, 30), (-30, 22)), 'quill', 'b', False, False, 3.4),
             L(quad((20, 52), (-4, 52), (-26, 58)), 'quill', 'b', False, False, 3.4),
             L(outline([(40, 122), (10, 116), (2, 80), (6, 40), (20, 12), (50, 2), (76, 12), (88, 36), (88, 60), (80, 70), (58, 76), (54, 100), (58, 124)])),
             L(outline([(4, 60), (40, 70), (54, 100), (58, 124), (40, 122), (10, 116)]), 'pink', 'f', False),
             L(outline([(70, 40), (92, 40), (94, 60), (74, 62)]), 'mask', 'f', ln=True),
             L(outline([(80, 60), (104, 70), (116, 84, 1), (96, 80), (78, 72)]), 'beak', 'f', ln=True)]
            + side_eye(84, 50, 4.4, 'iris'),
    'back': _quills_f + [L(outline([(10, 120), (6, 80), (8, 40), (20, 14), (50, 2), (80, 14), (92, 40), (94, 80), (90, 120), (50, 126)]), 'pink'),
                         L(outline([(20, 30), (36, 10), (50, 6), (64, 10), (80, 30), (60, 34), (50, 40), (40, 34)]), 'mid', 'b', False)],
}

# Mistis: búho morado de cara redonda color crema con dos ojos amarillos enormes y un pico gris; el manto de plumas se abre
# en dos puntas a los lados como alas por encima de los hombros
CHARS['mistis'] = {
    'body': 'normal', 'pal': pal('#6e5470', '#6e5470', shade='#56405a', deep='#432f48', disk='#f4ecdc', disk_d='#d8ccb8', beak='#9a9a96', iris='#f2d020'),
    'face': NOFACE,
    'front': [L(outline([(8, 100), (-28, 104), (-34, 96, 1), (-10, 88), (4, 70), (6, 34), (20, 10), (50, 2), (80, 10), (94, 34), (96, 70), (110, 88), (134, 96, 1),
                         (128, 104), (92, 100), (80, 124), (50, 132, 1), (20, 124)])),
              L(outline([(60, 6), (86, 18), (96, 70), (112, 92), (90, 100), (80, 60)]), 'shade', 'b', False),
              L(outline([(14, 70), (14, 40), (30, 26), (50, 32), (70, 26), (86, 40), (86, 70), (70, 82), (50, 78), (30, 82)]), 'disk', 'f', ln=True),
              L(outline([(50, 32), (70, 26), (86, 40), (86, 70), (70, 82), (60, 80)]), 'disk_d', 'f', False),
              L(outline([(30, 96), (50, 90), (70, 96), (60, 116), (50, 124, 1), (40, 116)]), 'deep', 'f', ln=True)]
             + eye(34, 54, 9, 9, 'iris', 0.4) + eye(66, 54, 9, 9, 'iris', 0.4)
             + [L(outline([(44, 62), (56, 62), (54, 80), (50, 88, 1), (46, 80)]), 'beak', 'f', ln=True)],
    'side': [L(outline([(40, 122), (-2, 108), (-14, 100, 1), (2, 84), (4, 40), (16, 12), (48, 2), (76, 12), (90, 36), (92, 66), (82, 82), (60, 90), (56, 124)])),
             L(outline([(-2, 60), (24, 66), (40, 116), (4, 108)]), 'shade', 'b', False),
             L(outline([(72, 24), (92, 30), (96, 66), (84, 82), (70, 70)]), 'disk', 'f', ln=True),
             L(outline([(88, 56), (104, 64), (98, 80), (88, 72)]), 'beak', 'f', ln=True)]
            + side_eye(86, 46, 6, 'iris'),
    'back': [L(outline([(8, 100), (-28, 104), (-34, 96, 1), (-10, 88), (4, 70), (6, 34), (20, 10), (50, 2), (80, 10), (94, 34), (96, 70), (110, 88), (134, 96, 1),
                        (128, 104), (92, 100), (80, 124), (50, 132), (20, 124)])),
             L(outline([(56, 6), (86, 18), (96, 70), (112, 92), (88, 104), (78, 124), (60, 128)]), 'shade', 'b', False),
             L([(2, 80), (50, 90), (98, 80)], 'deep', 'b', False, False, 3)],
}

# Nevado: cabeza rosa rojiza de murciélago, con dos orejas enormes en punta terminadas en una bolita, ojos malvados, sonrisa
# y un pico pálido pequeño; una gola de plumas negras azuladas desgreñadas alrededor del cuello
CHARS['nevado'] = {
    'body': 'normal', 'pal': pal('#e06a7a', '#e06a7a', shade='#b84e60', deep='#963c4e', ruff='#22304c', ruff_d='#16203a', beak='#f2dcc4'),
    'face': NOFACE,
    'front': [L(outline([(-18, 120), (-6, 108), (-22, 96, 1), (0, 92), (-14, 76, 1), (14, 80), (30, 92), (50, 96), (70, 92), (86, 80), (114, 76, 1), (100, 92),
                         (122, 96, 1), (106, 108), (118, 120, 1), (90, 120), (76, 132, 1), (62, 120), (50, 134, 1), (38, 120), (24, 132, 1), (10, 120)]), 'ruff'),
              L(outline([(60, 96), (96, 90), (110, 110), (80, 120)]), 'ruff_d', 'b', False),
              L(outline([(20, 30), (-6, 6), (-14, -26, 1), (14, 0), (30, 18)])), L(outline([(80, 30), (106, 6), (114, -26, 1), (86, 0), (70, 18)])),
              L(ell(-14, -28, 4, 4), 'mid', 'b', ln=True), L(ell(114, -28, 4, 4), 'mid', 'b', ln=True),
              L(outline([(-6, 6), (8, 4), (14, 20), (2, 14)]), 'deep', 'b', False), L(outline([(106, 6), (92, 4), (86, 20), (98, 14)]), 'deep', 'b', False),
              L(outline([(18, 92), (14, 60), (18, 30), (32, 14), (50, 10), (68, 14), (82, 30), (86, 60), (82, 92), (50, 102)]), 'mid', 'f', ln=True),
              L(outline([(26, 34), (50, 24), (74, 34), (70, 42), (50, 36), (30, 42)]), 'shade', 'f', False),
              L(outline([(60, 14), (80, 28), (86, 60), (80, 86), (70, 60)]), 'shade', 'f', False),
              L(outline([(28, 54), (42, 58), (40, 64), (30, 62)]), WHITE, 'f', ln=True), L(outline([(72, 54), (58, 58), (60, 64), (70, 62)]), WHITE, 'f', ln=True),
              L(ell(37, 60, 1.6, 1.8), BLACK, 'f', False), L(ell(63, 60, 1.6, 1.8), BLACK, 'f', False),
              mean_brow(26, 48, 44, 56, 3), mean_brow(74, 48, 56, 56, 3),
              L(quad((32, 72), (50, 82), (68, 72)), OUTC, 'f', False, False, 1.6),
              L(outline([(44, 76), (56, 76), (52, 92), (50, 98, 1), (48, 92)]), 'beak', 'f', ln=True)],
    'side': [L(outline([(-14, 118), (-4, 106), (-20, 94, 1), (2, 92), (-8, 76, 1), (22, 82), (40, 92), (60, 96), (70, 112), (66, 130, 1), (50, 120), (36, 132, 1),
                        (20, 120), (6, 132, 1)]), 'ruff'),
             L(outline([(26, 26), (40, -6), (46, -34, 1), (56, -4), (52, 22)])),
             L(outline([(40, 96), (14, 88), (8, 60), (14, 30), (34, 14), (60, 12), (80, 26), (90, 50), (88, 70), (78, 82), (60, 88)]), 'mid', 'f', ln=True),
             L(outline([(70, 60), (90, 64), (104, 72, 1), (88, 76), (72, 70)]), 'beak', 'f', ln=True),
             L(outline([(70, 46), (82, 48), (80, 54), (70, 52)]), WHITE, 'f', ln=True), L(ell(78, 50, 1.4, 1.8), BLACK, 'f', False),
             mean_brow(66, 40, 84, 46, 2.6)],
    'back': [L(outline([(20, 30), (-6, 6), (-14, -26, 1), (14, 0), (30, 18)])), L(outline([(80, 30), (106, 6), (114, -26, 1), (86, 0), (70, 18)])),
             L(ell(-14, -28, 4, 4), 'mid', 'b', ln=True), L(ell(114, -28, 4, 4), 'mid', 'b', ln=True),
             L(outline([(18, 90), (14, 60), (18, 30), (32, 14), (50, 10), (68, 14), (82, 30), (86, 60), (82, 90), (50, 96)]), 'mid', 'b', ln=True),
             L(outline([(56, 12), (80, 28), (86, 60), (80, 88), (62, 92)]), 'shade', 'b', False),
             L(outline([(-18, 120), (-6, 106), (-22, 92, 1), (0, 86), (-14, 70, 1), (14, 72), (30, 62), (50, 70), (70, 62), (86, 72), (114, 70, 1), (100, 86),
                        (122, 92, 1), (106, 106), (118, 120, 1), (90, 120), (76, 132, 1), (62, 120), (50, 134, 1), (38, 120), (24, 132, 1), (10, 120)]), 'ruff', 'f', ln=True)],
}

# Etna: águila de cabeza blanca crema con goterones malva rosados por abajo, un antifaz rojo alrededor de los ojos grises,
# pico amarillo ganchudo y una sonrisa
CHARS['etna'] = {
    'body': 'normal', 'pal': pal('#f4ecd4', '#f4ecd4', shade='#ddd2b4', drip='#c8a090', drip_d='#a8806e', mask='#c8301e', beak='#f0d040', beak_d='#c8a420',
                                 iris='#8a9a9a'),
    'face': NOFACE,
    'front': [L(outline([(6, 118), (2, 80), (6, 40), (16, 12), (50, 0), (84, 12), (94, 40), (98, 80), (94, 118), (50, 126)])),
              L(outline([(4, 90), (14, 100), (20, 120, 1), (28, 102), (40, 112, 1), (46, 98), (50, 104), (54, 98), (60, 112, 1), (72, 102), (80, 120, 1), (86, 100),
                         (96, 90), (96, 120), (50, 128), (4, 120)]), 'drip', 'f', False),
              L(outline([(70, 10), (90, 24), (96, 70), (88, 72)]), 'shade', 'f', False),
              L(outline([(44, 8), (50, 20), (56, 10), (52, 30)]), 'shade', 'f', False),
              L(outline([(14, 50), (30, 44), (50, 56), (70, 44), (86, 50), (84, 64), (66, 70), (50, 66), (34, 70), (16, 64)]), 'mask', 'f', ln=True)]
             + eye(32, 57, 5.4, 5.4, 'iris') + eye(68, 57, 5.4, 5.4, 'iris')
             + [L(outline([(28, 70), (50, 62), (72, 70), (64, 86), (50, 96, 1), (36, 86)]), 'beak', 'f', ln=True),
                L(outline([(50, 64), (70, 70), (62, 86), (50, 94)]), 'beak_d', 'f', False),
                L(quad((34, 80), (50, 88), (66, 80)), OUTC, 'f', False, False, 1.4)],
    'side': [L(outline([(40, 122), (6, 116), (-2, 80), (4, 40), (18, 10), (48, 0), (76, 10), (90, 36), (92, 62), (84, 74), (62, 80), (56, 100), (60, 124)])),
             L(outline([(-2, 60), (30, 70), (50, 90), (60, 124), (40, 122), (6, 116)]), 'drip', 'f', False),
             L(outline([(68, 40), (92, 40), (94, 56), (70, 60)]), 'mask', 'f', ln=True),
             L(outline([(78, 58), (102, 62), (112, 78, 1), (96, 78), (78, 72)]), 'beak', 'f', ln=True)]
            + side_eye(84, 48, 4.4, 'iris'),
    'back': [L(outline([(6, 118), (2, 80), (6, 40), (16, 12), (50, 0), (84, 12), (94, 40), (98, 80), (94, 118), (50, 126)])),
             L(outline([(2, 60), (20, 54), (30, 70), (50, 60), (70, 70), (80, 54), (98, 60), (98, 118), (50, 126), (2, 118)]), 'drip', 'f', False)],
}

# Proman: picozapato malva de cabeza aplastada con el borde de arriba en picos, un pico enorme gris pálido que le baja
# hasta el pecho y ojillos blancos malvados
CHARS['proman'] = {
    'body': 'normal', 'pal': pal('#a8848c', '#a8848c', shade='#8a6a72', deep='#6e5258', beak='#d2ccbe', beak_d='#b2ab9a'),
    'face': NOFACE,
    'front': [L(outline([(0, 116), (-4, 70), (-10, 40), (-24, 16, 1), (-8, 20), (-12, 30, 1), (4, 30), (20, 26), (50, 22), (80, 26), (96, 30), (112, 30, 1),
                         (108, 20), (124, 16, 1), (110, 40), (104, 70), (100, 116), (50, 124)])),
              L(outline([(60, 24), (96, 30), (104, 70), (100, 112), (80, 110)]), 'shade', 'b', False),
              L(outline([(20, 44), (36, 50), (40, 60), (30, 56)]), 'deep', 'f', False), L(outline([(80, 44), (64, 50), (60, 60), (70, 56)]), 'deep', 'f', False),
              L(outline([(28, 52), (40, 56), (36, 60)]), WHITE, 'f', ln=True), L(outline([(72, 52), (60, 56), (64, 60)]), WHITE, 'f', ln=True),
              L(outline([(36, 56), (64, 56), (70, 80), (66, 108), (50, 120), (34, 108), (30, 80)]), 'beak', 'f', ln=True),
              L(outline([(50, 58), (64, 56), (70, 80), (66, 106), (54, 116)]), 'beak_d', 'f', False),
              mean_brow(24, 46, 40, 54, 2.6), mean_brow(76, 46, 60, 54, 2.6)],
    'side': [L(outline([(36, 124), (-4, 116), (-10, 70), (-2, 30), (14, 4), (24, -12, 1), (30, 4), (50, 2), (72, 10), (84, 30), (84, 50), (64, 70), (56, 124)])),
             L(outline([(-6, 60), (24, 66), (42, 118), (4, 116)]), 'shade', 'b', False),
             L(outline([(70, 40), (96, 50), (114, 70), (120, 96, 1), (98, 90), (74, 74), (62, 60)]), 'beak', 'f', ln=True),
             L(quad((70, 66), (96, 76), (118, 94)), OUTC, 'f', False, False, 1.2),
             L(outline([(70, 38), (82, 40), (78, 44)]), WHITE, 'f', ln=True), mean_brow(66, 34, 84, 40, 2.4)],
    'back': [L(outline([(0, 116), (-4, 70), (-10, 40), (-24, 16, 1), (-8, 20), (-12, 30, 1), (4, 30), (20, 26), (50, 22), (80, 26), (96, 30), (112, 30, 1),
                        (108, 20), (124, 16, 1), (110, 40), (104, 70), (100, 116), (50, 124)])),
             L(outline([(20, 40), (80, 40), (90, 112), (50, 120), (10, 112)]), 'deep', 'b', False)],
}

# Cotopax: cabeza ovalada alta color crema amarillento, terminada arriba en un tubo con la punta azul turquesa, ojos negros
# enfadados, un pico corto pálido y una bufanda azul anudada al cuello con las puntas al viento
CHARS['cotopax'] = {
    'body': 'normal', 'pal': pal('#f0eab8', '#f0eab8', shade='#d8d098', tube='#5ab8c8', tube_d='#3a8ea0', back='#c09878', scarf='#2a6ab0', scarf_d='#1e4e88',
                                 beak='#f6f0e0'),
    'face': NOFACE,
    'front': [L(outline([(56, -20), (60, -40), (72, -42), (70, -20)]), 'tube', 'b', ln=True), L(ell(66, -41, 6, 2.4), 'tube_d', 'b', False),
              L(outline([(14, 100), (8, 60), (16, 20), (34, 0), (56, -16), (72, -12), (86, 10), (94, 50), (90, 100), (50, 108)])),
              L(outline([(70, -8), (86, 10), (94, 50), (90, 96), (80, 70)]), 'shade', 'b', False),
              L(outline([(28, 50), (40, 48), (42, 60), (30, 62)]), BLACK, 'f', False), L(outline([(72, 50), (60, 48), (58, 60), (70, 62)]), BLACK, 'f', False),
              L(ell(34, 53, 1.4, 1.4), WHITE, 'f', False), L(ell(66, 53, 1.4, 1.4), WHITE, 'f', False),
              mean_brow(24, 42, 42, 48, 2.8), mean_brow(76, 42, 58, 48, 2.8),
              L(outline([(42, 62), (58, 62), (56, 76), (50, 80, 1), (44, 76)]), 'beak', 'f', ln=True),
              L(outline([(4, 96), (30, 88), (50, 92), (70, 88), (96, 96), (100, 112), (80, 118), (50, 114), (20, 118), (2, 112)]), 'scarf', 'f', ln=True),
              L(outline([(80, 102), (110, 96), (124, 110, 1), (108, 112), (118, 124, 1), (92, 116)]), 'scarf', 'f', ln=True),
              L(outline([(60, 104), (96, 100), (98, 110), (64, 112)]), 'scarf_d', 'f', False)],
    'side': [L(outline([(36, -16), (40, -40), (52, -42), (52, -14)]), 'tube', 'b', ln=True),
             L(outline([(40, 102), (6, 96), (2, 60), (10, 24), (30, 0), (48, -16), (66, -6), (80, 20), (88, 50), (84, 80), (66, 92), (56, 104)])),
             L(outline([(4, 50), (24, 20), (40, 60), (40, 100), (10, 96)]), 'back', 'b', False),
             L(outline([(80, 54), (94, 58), (88, 68), (80, 66)]), 'beak', 'f', ln=True),
             L(outline([(72, 46), (80, 44), (82, 54), (74, 54)]), BLACK, 'f', False), mean_brow(68, 38, 84, 42, 2.6),
             L(outline([(0, 92), (40, 88), (70, 92), (72, 110), (40, 112), (-4, 108)]), 'scarf', 'f', ln=True),
             L(outline([(4, 96), (-24, 92), (-36, 104, 1), (-18, 106), (-28, 118, 1), (0, 110)]), 'scarf', 'f', ln=True)],
    'back': [L(outline([(28, -20), (30, -40), (42, -42), (44, -20)]), 'tube', 'b', ln=True),
             L(outline([(14, 100), (8, 60), (16, 20), (30, 0), (40, -16), (56, -12), (80, 10), (92, 50), (90, 100), (50, 108)])),
             L(outline([(40, 0), (80, 14), (92, 60), (88, 100), (50, 106)]), 'back', 'b', False),
             L(outline([(4, 94), (50, 90), (96, 94), (98, 112), (50, 116), (2, 112)]), 'scarf', 'f', ln=True),
             L(outline([(40, 100), (30, 124, 1), (46, 112), (56, 126, 1), (60, 100)]), 'scarf_d', 'f', ln=True)],
}

# Vesuvian: búho gris de cara blanca con unas líneas oscuras onduladas a los lados, ojos amarillos y pico pardo; dos
# penachos largos abiertos hacia arriba que se ramifican en puntas rosadas, y el manto cayendo en flecos hasta el pecho
CHARS['vesuvian'] = {
    'body': 'normal', 'pal': pal('#9a9a8e', '#9a9a8e', shade='#7e7e72', deep='#5e5e54', tuft='#a88a86', disk='#f2f0e6', line='#4a4a44', beak='#7a5a4a',
                                 iris='#d8d020'),
    'face': NOFACE,
    'front': [L(outline([(26, 22), (4, 6), (-18, -10), (-22, -16, 1), (-6, -6), (-10, -18, 1), (2, -6), (14, 6), (34, 14)])),
              L(outline([(74, 22), (96, 6), (118, -10), (122, -16, 1), (106, -6), (110, -18, 1), (98, -6), (86, 6), (66, 14)])),
              L(ell(-20, -14, 3, 3), 'tuft', 'b', False), L(ell(-8, -16, 3, 3), 'tuft', 'b', False),
              L(ell(120, -14, 3, 3), 'tuft', 'b', False), L(ell(108, -16, 3, 3), 'tuft', 'b', False),
              L(outline([(4, 124), (0, 80), (6, 40), (18, 14), (50, 6), (82, 14), (94, 40), (100, 80), (96, 124), (82, 112), (74, 126, 1), (64, 112), (56, 126, 1),
                         (50, 112), (44, 126, 1), (36, 112), (26, 126, 1), (18, 112)])),
              L(outline([(60, 8), (84, 18), (96, 60), (96, 120), (82, 108), (82, 60)]), 'shade', 'b', False),
              L(outline([(20, 76), (18, 48), (28, 36), (50, 42), (72, 36), (82, 48), (80, 76), (66, 84), (50, 92), (34, 84)]), 'disk', 'f', ln=True),
              L([(22, 46), (18, 58), (24, 68), (18, 80)], 'line', 'f', False, False, 2.4), L([(78, 46), (82, 58), (76, 68), (82, 80)], 'line', 'f', False, False, 2.4)]
             + eye(36, 56, 6.4, 6, 'iris', 0.38, ring=OUTC) + eye(64, 56, 6.4, 6, 'iris', 0.38, ring=OUTC)
             + [mean_brow(26, 44, 44, 50, 2.6), mean_brow(74, 44, 56, 50, 2.6),
                L(outline([(44, 62), (56, 62), (54, 80), (50, 88, 1), (46, 80)]), 'beak', 'f', ln=True)],
    'side': [L(outline([(36, 18), (30, -10), (24, -24, 1), (34, -12), (38, -24, 1), (42, -8), (48, 16)])),
             L(outline([(40, 124), (-4, 116), (-8, 80), (2, 40), (16, 12), (48, 4), (76, 14), (90, 38), (92, 66), (84, 80), (62, 88), (56, 124)])),
             L(outline([(-6, 60), (24, 66), (44, 120), (4, 114)]), 'shade', 'b', False),
             L(outline([(74, 30), (92, 34), (94, 66), (84, 80), (72, 70)]), 'disk', 'f', ln=True),
             L([(74, 36), (70, 50), (76, 62), (70, 74)], 'line', 'f', False, False, 2.2),
             L(outline([(88, 58), (100, 64), (96, 78), (88, 72)]), 'beak', 'f', ln=True)]
            + side_eye(86, 48, 5, 'iris', ring=OUTC),
    'back': [L(outline([(26, 22), (4, 6), (-18, -10), (-22, -16, 1), (-6, -6), (-10, -18, 1), (2, -6), (14, 6), (34, 14)])),
             L(outline([(74, 22), (96, 6), (118, -10), (122, -16, 1), (106, -6), (110, -18, 1), (98, -6), (86, 6), (66, 14)])),
             L(outline([(4, 124), (0, 80), (6, 40), (18, 14), (50, 6), (82, 14), (94, 40), (100, 80), (96, 124), (50, 130)])),
             L(outline([(56, 8), (84, 18), (98, 70), (96, 122), (60, 128), (66, 60)]), 'deep', 'b', False)],
}

# Tair: cabeza rosa redonda con dos asas en anillo a los lados, ojos blancos redondos de pupila pequeña con una raya negra
# alrededor, pico amarillo y una gola de plumas magenta en el cuello
CHARS['tair'] = {
    'body': 'normal', 'pal': pal('#f4b8c8', '#f4b8c8', shade='#e098ae', ruff='#a83a80', ruff_d='#7e2a62', beak='#f0d040', beak_d='#c8a420', blush='#f08aa8'),
    'face': NOFACE,
    'front': [L(outline([(2, 112), (12, 92), (30, 88), (50, 92), (70, 88), (88, 92), (98, 112), (80, 118), (70, 128, 1), (60, 118), (50, 128, 1), (40, 118),
                         (30, 128, 1), (20, 118)]), 'ruff', 'b', ln=True),
              L(outline([(60, 92), (88, 92), (98, 112), (70, 116)]), 'ruff_d', 'b', False),
              L(outline([(10, 40), (-8, 30), (-14, 44), (-6, 58), (10, 56)])), L(outline([(90, 40), (108, 30), (114, 44), (106, 58), (90, 56)])),
              L(ell(-2, 44, 3.6, 4.4), WHITE, 'f', ln=True), L(ell(102, 44, 3.6, 4.4), WHITE, 'f', ln=True),
              L(outline([(14, 96), (6, 60), (12, 26), (30, 6), (50, 2), (70, 6), (88, 26), (94, 60), (86, 96), (50, 104)]), 'mid', 'f', ln=True),
              L(outline([(60, 6), (86, 22), (94, 60), (86, 92), (74, 60)]), 'shade', 'f', False),
              L(quad((28, 30), (34, 26), (40, 30)), OUTC, 'f', False, False, 1.6), L(quad((72, 30), (66, 26), (60, 30)), OUTC, 'f', False, False, 1.6),
              L(ell(32, 50, 8, 7), OUTC, 'f', False), L(ell(68, 50, 8, 7), OUTC, 'f', False),
              L(ell(32, 50, 6.4, 5.6), WHITE, 'f', False), L(ell(68, 50, 6.4, 5.6), WHITE, 'f', False),
              L(ell(33, 50, 1.8, 2.4), BLACK, 'f', False), L(ell(67, 50, 1.8, 2.4), BLACK, 'f', False),
              L(ell(22, 66, 4, 2.4), 'blush', 'f', False), L(ell(78, 66, 4, 2.4), 'blush', 'f', False),
              L(outline([(38, 58), (62, 58), (56, 74), (50, 88, 1), (44, 74)]), 'beak', 'f', ln=True),
              L(outline([(50, 60), (62, 58), (56, 74), (50, 86)]), 'beak_d', 'f', False)],
    'side': [L(outline([(10, 112), (20, 92), (40, 88), (60, 96), (62, 116), (50, 126, 1), (40, 116), (28, 128, 1), (16, 118)]), 'ruff', 'b', ln=True),
             L(outline([(20, 40), (2, 34), (-4, 48), (4, 60), (20, 58)])), L(ell(8, 48, 3.4, 4.2), WHITE, 'f', ln=True),
             L(outline([(40, 98), (12, 90), (6, 56), (14, 24), (36, 6), (62, 6), (82, 22), (92, 48), (90, 70), (76, 86), (56, 94)]), 'mid', 'f', ln=True),
             L(outline([(80, 52), (98, 58), (104, 70, 1), (92, 72), (80, 66)]), 'beak', 'f', ln=True),
             L(ell(80, 44, 4.6, 6), OUTC, 'f', False), L(ell(80, 44, 3.4, 4.8), WHITE, 'f', False), L(ell(81, 44, 1.4, 2), BLACK, 'f', False)],
    'back': [L(outline([(10, 40), (-8, 30), (-14, 44), (-6, 58), (10, 56)])), L(outline([(90, 40), (108, 30), (114, 44), (106, 58), (90, 56)])),
             L(ell(-2, 44, 3.6, 4.4), WHITE, 'b', ln=True), L(ell(102, 44, 3.6, 4.4), WHITE, 'b', ln=True),
             L(outline([(14, 96), (6, 60), (12, 26), (30, 6), (50, 2), (70, 6), (88, 26), (94, 60), (86, 96), (50, 104)]), 'mid', 'b', ln=True),
             L(outline([(56, 4), (86, 22), (94, 60), (86, 94), (60, 100)]), 'shade', 'b', False),
             L(outline([(2, 112), (10, 88), (30, 80), (50, 84), (70, 80), (90, 88), (98, 112), (80, 118), (70, 128, 1), (60, 118), (50, 128, 1), (40, 118),
                        (30, 128, 1), (20, 118)]), 'ruff', 'f', ln=True)],
}

# Nyira: capucha de plumas marrón oscuro muy alta en punta, con una cresta a rayas rosa, azul y roja; la cara roja con el
# contorno azul marino, ojos blancos con la pupila pequeña, pico crema y unas gafas de piloto grises en la frente
CHARS['nyira'] = {
    'body': 'normal', 'pal': pal('#4a2a1e', '#4a2a1e', shade='#341c14', red='#d8401e', navy='#2a3a7a', crest='#e8a8b0', beak='#eedcae',
                                 gog='#7a7a80', lens='#3a3a42'),
    'face': NOFACE,
    'front': [L(outline([(40, 4), (42, -26), (50, -44, 1), (58, -26), (60, 4)]), 'navy', 'b', ln=True),
              L(outline([(44, 0), (46, -22), (50, -36, 1), (54, -22), (56, 0)]), 'crest', 'b', False),
              L(outline([(-6, 124), (-4, 90), (6, 50), (18, 18), (50, 2), (82, 18), (94, 50), (104, 90), (106, 124), (80, 116), (66, 132, 1), (50, 118), (34, 132, 1),
                         (20, 116)])),
              L(outline([(60, 6), (84, 20), (100, 90), (104, 120), (82, 112), (80, 60)]), 'shade', 'b', False),
              L(outline([(14, 110), (16, 70), (26, 44), (50, 36), (74, 44), (84, 70), (86, 110), (66, 116), (50, 126, 1), (34, 116)]), 'navy', 'f', ln=True),
              L(outline([(22, 80), (28, 54), (50, 46), (72, 54), (78, 80), (66, 100), (50, 108), (34, 100)]), 'red', 'f', ln=True),
              L(ell(34, 34, 11, 7), 'gog', 'f', ln=True), L(ell(66, 34, 11, 7), 'gog', 'f', ln=True),
              L(ell(34, 34, 7, 4.4), 'lens', 'f', False), L(ell(66, 34, 7, 4.4), 'lens', 'f', False),
              L(outline([(28, 58), (42, 62), (40, 70), (30, 68)]), WHITE, 'f', ln=True), L(outline([(72, 58), (58, 62), (60, 70), (70, 68)]), WHITE, 'f', ln=True),
              L(ell(36, 65, 1.6, 2), BLACK, 'f', False), L(ell(64, 65, 1.6, 2), BLACK, 'f', False),
              L(outline([(40, 70), (60, 70), (56, 90), (50, 100, 1), (44, 90)]), 'beak', 'f', ln=True)],
    'side': [L(outline([(26, 6), (16, -26), (14, -48, 1), (30, -28), (40, 2)]), 'navy', 'b', ln=True),
             L(outline([(24, 0), (20, -26), (20, -40, 1), (30, -24), (34, 0)]), 'crest', 'b', False),
             L(outline([(40, 128), (-6, 120), (-8, 80), (2, 40), (16, 10), (48, 2), (74, 12), (88, 36), (92, 70), (86, 96), (64, 110), (58, 128)])),
             L(outline([(-6, 60), (24, 66), (42, 124), (4, 120)]), 'shade', 'b', False),
             L(outline([(70, 44), (90, 46), (94, 80), (80, 100), (66, 84)]), 'navy', 'f', ln=True),
             L(outline([(76, 54), (92, 56), (94, 78), (80, 86)]), 'red', 'f', ln=True),
             L(ell(76, 34, 8, 6), 'gog', 'f', ln=True), L(ell(78, 34, 5, 3.6), 'lens', 'f', False),
             L(outline([(86, 70), (104, 76), (94, 90), (86, 84)]), 'beak', 'f', ln=True),
             L(outline([(82, 60), (90, 62), (88, 68), (82, 66)]), WHITE, 'f', ln=True)],
    'back': [L(outline([(40, 6), (42, -24), (50, -44, 1), (58, -24), (60, 6)]), 'navy', 'b', ln=True),
             L(outline([(46, 2), (50, -36, 1), (54, 2)]), 'crest', 'b', False),
             L(outline([(-6, 124), (-4, 90), (6, 50), (18, 18), (50, 2), (82, 18), (94, 50), (104, 90), (106, 124), (50, 132)])),
             L(outline([(56, 6), (84, 20), (100, 90), (104, 122), (60, 128)]), 'shade', 'b', False)],
}

# Caldera Dorne (Rodan): pájaro lila de cabeza alta, con dos astas ramificadas en lo alto, unos mechones largos que le
# salen a los lados del cuello y se curvan hacia arriba, cejas fruncidas, ojos negros con el borde blanco y pico amarillento
CHARS['caldera-dorne'] = {
    'body': 'normal', 'pal': pal('#a68ac4', '#a68ac4', shade='#8a70a8', deep='#6e5690', beak='#d8d07a', beak_d='#b0a858'),
    'face': NOFACE,
    'front': [L(outline([(30, 14), (22, -6), (12, -16), (8, -30, 1), (18, -18), (20, -30, 1), (26, -14), (40, 6)])),
              L(outline([(70, 14), (78, -6), (88, -16), (92, -30, 1), (82, -18), (80, -30, 1), (74, -14), (60, 6)])),
              L(outline([(6, 96), (-14, 98), (-30, 84), (-34, 72, 1), (-20, 82), (2, 80)])), L(outline([(94, 96), (114, 98), (130, 84), (134, 72, 1), (120, 82), (98, 80)])),
              L(outline([(8, 120), (2, 80), (6, 40), (18, 12), (50, 2), (82, 12), (94, 40), (98, 80), (92, 120), (78, 108), (66, 124, 1), (56, 110), (50, 126, 1),
                         (44, 110), (34, 124, 1), (22, 108)])),
              L(outline([(60, 6), (84, 16), (96, 60), (94, 114), (80, 106), (82, 60)]), 'shade', 'b', False),
              strand([(30, 90), (24, 116)], 'deep', 'f', 1.2), strand([(70, 90), (76, 116)], 'deep', 'f', 1.2),
              L(ell(32, 54, 8, 6.4), WHITE, 'f', ln=True), L(ell(68, 54, 8, 6.4), WHITE, 'f', ln=True),
              L(ell(32, 54, 6.8, 5.4), BLACK, 'f', False), L(ell(68, 54, 6.8, 5.4), BLACK, 'f', False),
              L(ell(31, 53, 1.4, 1.4), WHITE, 'f', False), L(ell(65, 53, 1.4, 1.4), WHITE, 'f', False),
              mean_brow(22, 40, 44, 48, 3), mean_brow(78, 40, 56, 48, 3),
              strand([(44, 36), (50, 30), (56, 36)], 'deep', 'f', 1.2),
              L(outline([(36, 64), (64, 64), (58, 80), (50, 92, 1), (42, 80)]), 'beak', 'f', ln=True),
              L(outline([(50, 66), (64, 64), (58, 80), (50, 90)]), 'beak_d', 'f', False)],
    'side': [L(outline([(36, 12), (28, -10), (24, -28, 1), (34, -14), (40, -26, 1), (42, -8), (50, 10)])),
             L(outline([(20, 96), (0, 100), (-18, 88), (-24, 76, 1), (-8, 84), (14, 82)])),
             L(outline([(40, 122), (6, 116), (-2, 80), (4, 40), (18, 10), (48, 2), (76, 12), (90, 36), (92, 62), (84, 74), (62, 80), (56, 100), (60, 124)])),
             L(outline([(-2, 60), (24, 66), (44, 118), (8, 114)]), 'shade', 'b', False),
             L(outline([(76, 56), (104, 64), (120, 80, 1), (98, 78), (76, 70)]), 'beak', 'f', ln=True),
             L(ell(82, 46, 5, 5.6), WHITE, 'f', ln=True), L(ell(83, 46, 3.4, 4), BLACK, 'f', False), mean_brow(70, 36, 90, 42, 2.8)],
    'back': [L(outline([(30, 14), (22, -6), (12, -16), (8, -30, 1), (18, -18), (20, -30, 1), (26, -14), (40, 6)])),
             L(outline([(70, 14), (78, -6), (88, -16), (92, -30, 1), (82, -18), (80, -30, 1), (74, -14), (60, 6)])),
             L(outline([(6, 96), (-14, 98), (-30, 84), (-34, 72, 1), (-20, 82), (2, 80)])), L(outline([(94, 96), (114, 98), (130, 84), (134, 72, 1), (120, 82), (98, 80)])),
             L(outline([(8, 120), (2, 80), (6, 40), (18, 12), (50, 2), (82, 12), (94, 40), (98, 80), (92, 120), (50, 126)])),
             L(outline([(56, 6), (84, 16), (96, 60), (94, 118), (60, 124)]), 'shade', 'b', False)],
}


def _shrink(spec, k=0.86, cy=112):
    """Encoge la cabeza (todas sus capas) hacia el cuello: con el manto de plumas, a tamaño natural quedaban más grandes
    que en el modelo."""
    for v in ('front', 'side', 'back'):
        spec[v] = [dict(l, s=[(50 + (x - 50) * k, cy + (y - cy) * k) for x, y in l['s']], w=l['w'] * k if l['w'] else 0)
                   for item in spec[v] for l in (item if isinstance(item, list) else [item])]


for _cid in ('aoba-gyr', 'mayon', 'merapil-sekretair', 'mistis', 'nevado', 'etna', 'proman', 'cotopax', 'vesuvian', 'tair', 'nyira', 'caldera-dorne'):
    _shrink(CHARS[_cid])
