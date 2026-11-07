"""Instituto Kirkwood (Ares) (ares-kidokawa-seishuu-ares): sus modelos 3D de Inazuma Eleven Ares como referencia (busto de
frente, perfil y espalda).

Los de Kirkwood de IE1 (Nishigaki, los hermanos Mukata, Megawa...) y Gouenji tienen en Ares el mismo diseño y usan su
dibujo de siempre. Nuevos de Ares: el portero Oogosho, el entrenador Nikaidou, Tanba Suzu, Mito y Hoshino."""
from chars import CHARS, L, OUTC, ell, outline, pal, strand  # noqa: F401
from heads import blob, quad  # noqa: F401

WHITE = (248, 246, 244, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


def star(cx, cy, r, c='star', z='f'):
    """Estrella de cinco puntas (las de la boina de Hoshino)."""
    import math
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return L(pts, c, z, False)


# Oogosho Yakata (portero): cabeza enorme y redonda de piel parda, como un muñeco, con tres conos dorados a rayas en lo alto
# (el grande en medio), ojos redondos azules, nariz rojiza y una sonrisa enorme de dientes
_OOG_FACE = [(4, 60), (14, 40), (50, 28), (86, 40), (96, 60), (100, 84), (92, 106), (72, 120), (50, 122), (28, 120), (8, 106), (0, 84)]
_OOG_HORNS_F = [L(outline([(12, 48), (14, 20, 1), (32, 40)]), 'horn', 'f', ln=True), L(outline([(88, 48), (86, 20, 1), (68, 40)]), 'horn', 'f', ln=True),
                L(outline([(34, 38), (50, -2, 1), (66, 38)]), 'horn', 'f', ln=True),
                L(outline([(30, 36), (70, 36), (68, 44), (32, 44)]), 'horn_d', 'f', ln=True),
                L([(40, 22), (60, 22)], 'horn_d', 'f', False, False, 1.4), L([(44, 12), (56, 12)], 'horn_d', 'f', False, False, 1.4),
                L([(15, 34), (24, 38)], 'horn_d', 'f', False, False, 1.2), L([(85, 34), (76, 38)], 'horn_d', 'f', False, False, 1.2)]
CHARS['trice-topper'] = {
    'body': 'corpulento', 'pal': pal('#9a6434', '#b0763e', iris='#2a5ab0', skin_d='#8e5a2c', horn='#e6c872', horn_d='#b4924a', nose='#c8603a'),
    'face': {'eyes': 'round', 'brows': 'angry', 'mouth': 'none', 'hairline': False, 'face_front': blob(_OOG_FACE), 'big_ears': 2, 'ear_out': 8,
             'nose': (50, 82, 3.6), 'eye_sep': 13},
    'front': _OOG_HORNS_F + [L(outline([(28, 90), (72, 90), (70, 98), (50, 102), (30, 98)]), WHITE, 'f', ln=True),
                             L(quad((30, 94), (50, 98), (70, 94)), OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(36, 40), (40, 8, 1), (56, 34)]), 'horn', 'f', ln=True), L(outline([(54, 30), (64, -6, 1), (80, 30)]), 'horn', 'f', ln=True),
             L(outline([(12, 50), (10, 24, 1), (28, 40)]), 'horn', 'f', ln=True),
             L(outline([(34, 36), (82, 28), (82, 34), (36, 42)]), 'horn_d', 'f', ln=True),
             L(blob([(46, 118), (16, 108), (2, 80), (4, 50), (22, 30), (54, 24), (80, 32), (96, 54), (100, 80), (96, 102), (80, 116)]), 'skin', 'b'),
             L(outline([(84, 92), (98, 90), (96, 100), (86, 100)]), WHITE, 'f', ln=True)],
    'back': [L(blob([(4, 70), (12, 42), (50, 28), (88, 42), (96, 70), (90, 100), (70, 116), (30, 116), (10, 100)]), 'skin'),
             L(outline([(56, 32), (88, 44), (94, 74), (86, 100), (64, 112)]), 'skin_d', 'b', False)] + _OOG_HORNS_F,
}
CHARS['trice-topper']['face']['face_side'] = blob([(46, 118), (16, 108), (2, 80), (4, 50), (22, 30), (54, 24), (80, 32), (96, 54), (100, 80), (96, 102),
                                                   (80, 116)])

# Nikaidou Shuugo (entrenador de Kirkwood): adulto de piel morena, pelo azul marino abundante peinado con raya y un
# flequillo en diagonal, barba de pocos días y mirada seria
CHARS['seth-nichols'] = {
    'body': 'delgado', 'pal': pal('#2c3052', '#c48c5c', iris='#3a2418', shade='#1e2240', stub='#b6845a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'line', 'mouth_y': 98, 'hairline': False, 'nose': (50, 86, 2)},
    'front': [L(outline([(10, 78), (2, 40), (8, 14), (30, -2), (56, -6), (80, 2), (96, 22), (98, 52), (90, 78), (84, 60), (18, 60)])),
              L(outline([(60, -2), (84, 8), (96, 36), (92, 66), (82, 46)]), 'shade', 'b', False),
              fringe([(8, 64), (10, 36), (24, 16), (50, 8), (74, 14), (90, 30), (92, 64), (84, 52), (80, 62, 1), (72, 44), (58, 38), (46, 50), (36, 66, 1),
                      (32, 48), (22, 54), (16, 66, 1)]),
              L(outline([(38, 104), (50, 108), (62, 104), (60, 112), (50, 116), (40, 112)]), 'stub', 'f', False)],
    'side': [L(outline([(52, 62), (56, 50), (80, 48), (94, 34), (98, 14), (80, -4), (54, -8), (28, -4), (8, 10), (0, 36), (2, 64), (14, 84), (30, 86), (44, 72)])),
             L(outline([(2, 36), (24, 42), (28, 80), (8, 76)]), 'shade', 'b', False),
             fringe([(70, 2), (94, 18), (100, 40), (92, 58, 1), (84, 44), (76, 34)]),
             L(outline([(78, 102), (90, 104), (86, 112), (78, 110)]), 'stub', 'f', False)],
    'back': [L(outline([(10, 82), (2, 40), (8, 14), (30, -2), (56, -6), (80, 2), (96, 22), (100, 52), (92, 82), (70, 90), (30, 90)])),
             L(outline([(56, -2), (84, 8), (98, 40), (92, 80), (64, 88)]), 'shade', 'b', False)],
}

# Tanba Suzu: rubia clarísima con dos coletas largas sujetas con bolas grises a la altura de las orejas, flequillo recto
# y una sonrisa de boca abierta; ojos grandes castaños
_SUZU_TAILS = [L(outline([(10, 44), (0, 70), (4, 108), (12, 120, 1), (18, 96), (18, 54)])), L(outline([(90, 44), (100, 70), (96, 108), (88, 120, 1), (82, 96), (82, 54)]))]
CHARS['lynn-tambelle'] = {
    'body': 'chica', 'pal': pal('#ecdcc0', '#fce6d4', iris='#7a4a22', shade='#c8b494', deep='#a89474', band='#8a8e98'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': _SUZU_TAILS + [L(outline([(14, 64), (10, 36), (20, 12), (50, 2), (80, 12), (90, 36), (86, 64), (80, 54), (20, 54)])),
                            L(outline([(60, 4), (82, 14), (90, 40), (86, 60), (78, 40)]), 'shade', 'b', False),
                            fringe([(12, 58), (14, 36), (28, 20), (50, 14), (72, 20), (86, 36), (88, 58), (80, 56), (72, 60), (64, 56), (56, 60), (48, 56),
                                    (40, 60), (32, 56), (24, 60), (18, 56)]),
                            L(ell(10, 46, 5, 5), 'band', 'f', ln=True), L(ell(90, 46, 5, 5), 'band', 'f', ln=True)],
    'side': [L(outline([(24, 44), (8, 56), (-4, 90), (0, 122, 1), (12, 98), (20, 66), (30, 50)])),
             L(outline([(52, 60), (56, 50), (80, 48), (92, 34), (86, 12), (64, 0), (36, 0), (14, 12), (6, 36), (8, 56), (20, 62), (38, 62)])),
             L(outline([(8, 30), (28, 34), (30, 56), (12, 54)]), 'shade', 'b', False),
             fringe([(62, 4), (88, 16), (94, 40), (92, 52, 1), (84, 46), (76, 38)]),
             L(ell(22, 46, 5, 5), 'band', 'f', ln=True)],
    'back': _SUZU_TAILS + [L(outline([(12, 62), (8, 30), (20, 8), (50, -2), (80, 8), (92, 30), (88, 62), (50, 68)])),
                           L(outline([(56, 2), (82, 12), (92, 40), (86, 60), (62, 66)]), 'shade', 'b', False),
                           strand([(50, 0), (50, 64)], 'deep', 'b', 1.0),
                           L(ell(12, 46, 5, 5), 'band', 'f', ln=True), L(ell(88, 46, 5, 5), 'band', 'f', ln=True)],
}

# Mito Atomi: pelo negro alborotado en pinchos irregulares hacia arriba y hacia los lados, con mechones sobre la frente;
# ojos grandes y una sonrisa tranquila
CHARS['hilary-prentice'] = {
    'body': 'normal', 'pal': pal('#1e1e24', '#fcdcc0', iris='#1e1e30', shade='#3a3a44', deep='#4e4e5a'),
    'face': {'eyes': 'big', 'brows': True, 'mouth': 'smile', 'mouth_y': 96, 'hairline': False},
    'front': [L(outline([(14, 84), (4, 76, 1), (10, 64), (0, 50, 1), (8, 40), (2, 20, 1), (14, 14), (8, -6, 1), (26, 4), (36, -8, 1), (46, 0), (54, -14, 1),
                         (60, 0), (74, -6, 1), (78, 8), (96, 6, 1), (90, 24), (100, 38, 1), (92, 48), (98, 66, 1), (88, 70), (88, 84), (84, 62), (16, 62)])),
              L(outline([(58, 2), (80, 8), (94, 40), (88, 76), (80, 50)]), 'shade', 'b', False),
              fringe([(12, 70), (14, 40), (26, 22), (50, 14), (74, 22), (86, 40), (88, 70), (80, 58), (76, 68, 1), (70, 48), (60, 60, 1), (56, 44), (48, 58, 1),
                      (42, 42), (32, 60, 1), (26, 48), (18, 66, 1)]),
              strand([(30, 24), (36, 44)], 'shade', 'f', 1.0), strand([(64, 22), (60, 42)], 'shade', 'f', 1.0)],
    'side': [L(outline([(54, 64), (58, 50), (80, 50), (92, 38), (96, 18), (108, 10, 1), (88, 6), (84, -12, 1), (66, 0), (56, -16, 1), (44, 0), (22, -4),
                        (26, 8), (2, 10, 1), (10, 26), (-10, 40, 1), (4, 50), (-4, 66, 1), (10, 70), (10, 86, 1), (24, 80), (40, 82), (46, 72)])),
             L(outline([(2, 38), (22, 44), (26, 78), (8, 74)]), 'shade', 'b', False),
             fringe([(66, 4), (90, 18), (98, 40), (92, 66, 1), (86, 50), (80, 60, 1), (76, 42), (66, 30)])],
    'back': [L(outline([(14, 84), (2, 80, 1), (8, 64), (-4, 50, 1), (6, 40), (0, 20, 1), (14, 14), (8, -6, 1), (26, 4), (36, -8, 1), (46, 0), (54, -14, 1),
                        (60, 0), (74, -6, 1), (78, 8), (98, 4, 1), (90, 24), (104, 38, 1), (94, 50), (100, 70, 1), (88, 84), (74, 92, 1), (62, 84), (50, 94, 1),
                        (38, 84), (26, 92, 1)])),
             L(outline([(56, 2), (82, 10), (96, 44), (88, 82), (64, 88)]), 'shade', 'b', False),
             strand([(30, 30), (38, 60), (32, 84)], 'deep', 'b', 1.0), strand([(70, 30), (62, 60), (68, 84)], 'deep', 'b', 1.0)],
}

# Hoshino Madoka: boina roja enorme con estrellas blancas y visera negra, el pelo castaño asomando por debajo en mechones
# hasta la nuca, ojos grandes y unos pendientes largos de cuentas de colores
_MADOKA_EAR = [L([(30, 96), (30, 110)], 'bead_d', 'f', False, False, 1.0), L(ell(30, 98, 2, 2), 'bead1', 'f', ln=True),
               L(ell(30, 104, 2, 2), 'bead2', 'f', ln=True), L(outline([(28, 106), (32, 106), (30, 114, 1)]), 'bead_d', 'f', False),
               L([(70, 96), (70, 110)], 'bead_d', 'f', False, False, 1.0), L(ell(70, 98, 2, 2), 'bead1', 'f', ln=True),
               L(ell(70, 104, 2, 2), 'bead2', 'f', ln=True), L(outline([(68, 106), (72, 106), (70, 114, 1)]), 'bead_d', 'f', False)]
CHARS['jodi-green'] = {
    'body': 'normal', 'pal': pal('#6a3a24', '#f6cca4', iris='#22222e', shade='#4a2818', cap='#c41e24', cap_d='#961418', brim='#1e1e22', star='#f4ecdc',
                             bead1='#5ab86a', bead2='#4a5ab0', bead_d='#8a8e98'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(12, 98), (12, 62), (88, 62), (88, 98), (80, 82), (20, 82)])),
              fringe([(16, 72), (18, 60), (84, 60), (84, 72), (76, 64), (68, 76, 1), (60, 64), (52, 74, 1), (44, 64), (36, 76, 1), (28, 64), (22, 74, 1)]),
              L(outline([(-4, 52), (0, 30), (18, 12), (50, 6), (82, 12), (100, 30), (104, 52), (82, 62), (18, 62)]), 'cap', 'f', ln=True),
              L(outline([(60, 8), (84, 14), (100, 32), (102, 52), (84, 60), (80, 36)]), 'cap_d', 'f', False),
              L(outline([(8, 58), (50, 54), (92, 58), (92, 68), (50, 64), (8, 68)]), 'brim', 'f', ln=True),
              star(30, 22, 8), star(84, 34, 8), star(4, 44, 6)] + _MADOKA_EAR,
    'side': [L(outline([(10, 58), (54, 58), (54, 74), (40, 82), (26, 94, 1), (20, 82), (12, 90, 1), (10, 76)])),
             L(outline([(-14, 46), (-10, 20), (12, 4), (50, -2), (84, 4), (98, 22), (96, 42), (80, 52), (30, 58), (-2, 58)]), 'cap', 'f', ln=True),
             L(outline([(-14, 46), (-10, 24), (10, 30), (12, 52), (-2, 56)]), 'cap_d', 'f', False),
             L(outline([(64, 46), (104, 52), (98, 62), (64, 56)]), 'brim', 'f', ln=True), star(54, 24, 9), star(10, 14, 6),
             L([(84, 94), (84, 108)], 'bead_d', 'f', False, False, 1.0), L(ell(84, 96, 2, 2), 'bead1', 'f', ln=True), L(ell(84, 102, 2, 2), 'bead2', 'f', ln=True)],
    'back': [L(outline([(12, 96), (10, 60), (90, 60), (90, 96), (78, 88), (70, 100, 1), (60, 88), (50, 98, 1), (40, 88), (30, 100, 1), (22, 88)])),
             L(outline([(-4, 52), (0, 30), (18, 12), (50, 6), (82, 12), (100, 30), (104, 52), (82, 66), (18, 66)]), 'cap', 'f', ln=True),
             L(outline([(56, 8), (84, 14), (100, 32), (102, 52), (84, 64), (70, 40)]), 'cap_d', 'f', False),
             star(30, 40, 8), star(72, 30, 8)] + _MADOKA_EAR,
}
