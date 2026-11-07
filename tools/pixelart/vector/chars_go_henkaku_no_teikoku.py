"""Royal Academy de GO (go-henkaku-no-teikoku): sus modelos 3D de Inazuma Eleven GO como referencia (busto de frente, perfil
y espalda). Peinados de villano: cuernos, crestas, picos en la frente, cicatrices y una máscara."""
from chars import CHARS, L, OUTC, blob, ell, messy, outline, pal, strand  # noqa: F401
from chars_alius import LONG_FACE, WIDE_FACE
from chars_bigwaves import side_eye, white_eyes
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


def scar(x0, y0, x1, y1):
    return [L([(x0, y0), (x1, y1)], (150, 70, 60, 255), 'f', False, False, 1.6), L([(x0 + 3, y0 - 1), (x1 + 3, y1 - 1)], (150, 70, 60, 255), 'f', False, False, 1.2)]


# Preston Princeton (portero): pelo lavanda grisáceo de pinchos largos que se abren a los lados y dos cuernos arriba, con un
# mechón que le cruza la cara en diagonal; ojos redondos de pupila pequeña y boca seria
CHARS['preston-princeton'] = {
    'body': 'normal', 'pal': pal('#8a8ab8', '#fce4c0', iris='#2a2a2a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 92), (-6, 92, 1), (8, 74), (-14, 64, 1), (6, 54), (-10, 36, 1), (8, 30), (14, -12, 1), (30, 8), (50, 0), (70, 8), (86, -12, 1), (92, 30),
                         (110, 36, 1), (94, 54), (114, 64, 1), (92, 74), (106, 92, 1), (84, 92), (82, 62), (18, 62)])),
              L(outline([(60, 4), (84, 14), (94, 44), (90, 84), (80, 50)]), 'shade', 'b', False),
              fringe([(12, 62), (16, 38), (30, 22), (50, 16), (70, 22), (84, 38), (88, 62), (78, 50), (70, 44), (60, 46), (54, 64), (48, 100, 1), (44, 70), (36, 50),
                      (26, 50), (20, 60)]),
              L(outline([(24, 26), (40, 18), (34, 30)]), 'light', 'f', False)] + white_eyes(77, 15, 6, 5, 2.2),
    'side': [L(outline([(54, 62), (58, 50), (80, 48), (92, 34), (88, 12), (70, -2), (80, -20, 1), (52, -4), (34, -14, 1), (22, 6), (-8, 6, 1), (8, 24), (-14, 40, 1),
                        (4, 50), (-6, 70, 1), (10, 72), (4, 92, 1), (22, 82), (30, 96, 1), (40, 80), (46, 72)])),
             L(outline([(6, 34), (26, 40), (28, 74), (10, 68)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 42), (92, 62), (86, 92, 1), (82, 56), (74, 36)])] + side_eye(77),
    'back': [L(outline([(18, 96), (-10, 100, 1), (8, 78), (-16, 64, 1), (6, 52), (-12, 30, 1), (10, 28), (12, -14, 1), (30, 6), (50, -2), (70, 6), (88, -14, 1), (90, 28),
                        (112, 30, 1), (94, 52), (116, 64, 1), (92, 78), (110, 100, 1), (82, 96), (50, 102)])),
             L(outline([(56, 4), (84, 14), (94, 50), (90, 92), (62, 98)]), 'shade', 'b', False)],
}

# Dracon Yale: piel morena; melena enorme blanco crema, de pinchos arriba, que le cae por delante tapándole un ojo hasta el
# pecho, con mechones que se retuercen hacia fuera a los lados como llamas; ojo violeta y dientes apretados
CHARS['dracon-yale'] = {
    'body': 'normal', 'pal': pal('#e8e4c4', '#c08a5a', iris='#8a5ab0', shade='#c8bea0', deep='#a89c80'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 120), (-2, 90), (-30, 76, 1), (-6, 70), (-20, 52, 1), (2, 50), (8, 20), (14, -10, 1), (30, 4), (46, -20, 1), (58, 2), (76, -8, 1), (90, 20),
                         (98, 50), (120, 52, 1), (104, 70), (130, 76, 1), (102, 90), (90, 120), (82, 90), (80, 62), (20, 62), (20, 100)])),
              L(outline([(60, 2), (86, 14), (96, 46), (96, 100), (84, 104), (80, 50)]), 'shade', 'b', False),
              fringe([(12, 70), (14, 40), (28, 18), (52, 10), (74, 18), (88, 38), (90, 70), (80, 56), (72, 50), (64, 60), (58, 54), (56, 80), (50, 120, 1), (42, 92),
                      (36, 70), (28, 64), (22, 80, 1), (18, 66)]),
              strand([(30, 20), (40, 50), (46, 100)], 'deep', 'f', 1.0), strand([(70, 20), (66, 50)], 'deep', 'f', 1.0),
              L(ell(68, 77, 4.6, 4), WHITE, 'f', ln=True), L(ell(68.5, 77.4, 2, 2.4), 'iris', 'f', False)],
    'side': [L(outline([(56, 62), (60, 50), (82, 46), (92, 30), (86, 10), (90, -10, 1), (66, 0), (54, -22, 1), (40, -2), (14, 4), (2, 34), (-22, 40, 1), (0, 52), (-2, 90),
                        (-26, 104, 1), (6, 102), (20, 124, 1), (30, 96), (42, 80), (48, 70)])),
             L(outline([(2, 40), (28, 46), (30, 96), (8, 98)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 44), (94, 70), (88, 100, 1), (82, 60), (74, 38)])],
    'back': [L(outline([(10, 120), (-2, 90), (-30, 76, 1), (-6, 70), (-20, 52, 1), (2, 50), (8, 20), (14, -10, 1), (30, 4), (46, -20, 1), (58, 2), (76, -8, 1), (90, 20),
                        (98, 50), (120, 52, 1), (104, 70), (130, 76, 1), (102, 90), (90, 120), (50, 128)])),
             L(outline([(56, 2), (86, 14), (98, 50), (94, 116), (64, 122)]), 'shade', 'b', False)],
}

# Duke Dartmouth: gordo; pelo castaño como un casco que le tapa la frente en pico hasta entre los ojos, con dos puntas de
# cuerno arriba a los lados y una cola larga por detrás; máscara gris con rendijas sobre la boca
CHARS['duke-dartmouth'] = {
    'body': 'corpulento', 'pal': pal('#5a3a34', '#d8a070', iris='#2a2a2a', mask='#8a8e90', mask_d='#6a6e70'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'none', 'hairline': False, 'face_front': WIDE_FACE},
    'front': [L(outline([(10, 92), (6, 40), (8, -6, 1), (20, 8), (50, 0), (80, 8), (92, -6, 1), (94, 40), (90, 92), (84, 70), (16, 70)])),
              L(outline([(60, 2), (84, 10), (92, 40), (88, 84), (78, 50)]), 'shade', 'b', False),
              fringe([(14, 64), (14, 36), (28, 22), (50, 20), (72, 22), (86, 36), (86, 64), (76, 58), (62, 64), (50, 76, 1), (38, 64), (24, 58)]),
              L(outline([(18, 86), (50, 82), (82, 86), (82, 110), (50, 114), (18, 110)]), 'mask', 'f', ln=True),
              L(outline([(56, 84), (82, 86), (82, 110), (58, 112)]), 'mask_d', 'f', False)]
             + [L([(40, y), (60, y)], OUTC, 'f', False, False, 2.2) for y in (92, 98, 104)]
             + white_eyes(78, 15, 5.6, 3.6, 1.6),
    'side': [L(outline([(60, 66), (70, 46), (90, 40), (110, 30), (116, 16), (100, 4), (66, -2), (60, -16, 1), (44, 0), (20, 4), (6, 30), (0, 70), (-6, 88, 1), (16, 82),
                        (40, 76)])),
             L(outline([(6, 30), (30, 36), (30, 76), (8, 76)]), 'shade', 'b', False),
             L(outline([(70, 84), (98, 84), (100, 110), (72, 110)]), 'mask', 'f', ln=True)] + side_eye(78),
    'back': [L(outline([(12, 92), (6, 40), (8, -6, 1), (20, 8), (50, 0), (80, 8), (92, -6, 1), (94, 40), (88, 92), (60, 96), (50, 104, 1), (40, 96)])),
             L(outline([(56, 2), (84, 10), (94, 44), (88, 90), (62, 94)]), 'shade', 'b', False)],
}

# Cameron Cambridge: una cresta altísima de pelo crema en forma de cono en lo alto y los lados cortos de pinchos; orejas
# grandes, ojos castaños y cara seria
CHARS['cameron-cambridge'] = {
    'body': 'normal', 'pal': pal('#e0dca0', '#fcd4a8', iris='#6a3a22', side='#b89a6a', side_d='#9a7e52'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': (58, 44), 'big_ears': 3, 'ear_out': 3},
    'front': [L(outline([(16, 64), (14, 36), (26, 14), (74, 14), (86, 36), (84, 64), (80, 52), (20, 52)]), 'side'),
              L(outline([(30, 48), (34, 10), (44, -20), (52, -40, 1), (60, -20), (68, 10), (70, 48), (50, 44)])),
              L(outline([(54, -30), (62, -10), (68, 20), (68, 44), (58, 40)]), 'shade', 'b', False)],
    'side': [L(outline([(54, 50), (58, 30), (40, 20), (16, 16), (-6, 24, 1), (8, 34), (-10, 46, 1), (8, 52), (-4, 70, 1), (14, 72), (20, 88), (36, 80), (46, 64)]), 'side'),
             L(outline([(18, 18), (30, -2), (50, -24), (80, -34, 1), (70, -10), (80, 14, 1), (64, 16), (60, 30), (36, 26)])),
             L(outline([(4, 34), (24, 40), (26, 66), (10, 60)]), 'side_d', 'b', False)],
    'back': [L(outline([(16, 70), (14, 36), (26, 14), (74, 14), (86, 36), (84, 70), (66, 86), (34, 86)]), 'side'),
             L(outline([(36, 70), (32, 30), (40, 0), (52, -40, 1), (62, 0), (68, 30), (64, 70), (50, 78)])),
             strand([(38, 30), (50, 36), (62, 30)], 'shade', 'b', 1.0), strand([(36, 54), (50, 60), (64, 54)], 'shade', 'b', 1.0)],
}

# Baron Oxford: pelo morado oscuro en casco con un pico que baja hasta entre los ojos y dos cuernos de toro que se curvan
# hacia arriba a los lados; nariz larga en punta, ojos rojos y sonrisa de dientes afilados
CHARS['baron-oxford'] = {
    'body': 'normal', 'pal': pal('#4a3450', '#fce4b8', iris='#a82020', nose='#f0c890'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 100, 'hairline': False, 'big_ears': 3, 'ear_out': 4},
    'front': [L(outline([(18, 96), (12, 40), (-4, 34), (-22, 22), (-24, -10, 1), (-8, 12), (20, 8), (50, 0), (80, 8), (108, 12), (124, -10, 1), (122, 22), (104, 34), (88, 40), (82, 96), (78, 60),
                         (22, 60)])),
              L(outline([(60, 4), (90, 10), (118, -4), (116, 20), (100, 32), (84, 40), (82, 86), (76, 50)]), 'shade', 'b', False),
              fringe([(16, 70), (16, 40), (30, 26), (50, 22), (70, 26), (84, 40), (84, 70), (76, 54), (62, 48), (50, 72, 1), (38, 48), (24, 54)]),
              L(outline([(48, 74), (52, 74), (60, 94, 1), (50, 92)]), 'nose', 'f', ln=True)],
    'side': [L(outline([(60, 70), (64, 50), (84, 46), (92, 30), (88, 10), (96, -10, 1), (74, 0), (52, -2), (24, 4), (8, 24), (4, 60), (12, 82), (30, 86), (46, 80),
                        (56, 96), (62, 96)])),
             L(outline([(6, 30), (28, 36), (30, 80), (10, 76)]), 'shade', 'b', False),
             fringe([(70, 4), (92, 18), (94, 40), (88, 64, 1), (80, 44)]),
             L(outline([(88, 80), (104, 92, 1), (88, 94)]), 'nose', 'f', ln=True)],
    'back': [L(outline([(16, 90), (14, 40), (-4, 34), (-22, 22), (-24, -10, 1), (-8, 12), (20, 8), (50, 0), (80, 8), (108, 12), (124, -10, 1), (122, 22), (104, 34), (86, 40), (84, 90), (50, 96)])),
             L(outline([(56, 4), (90, 10), (118, -4), (116, 20), (100, 32), (86, 44), (84, 88), (62, 94)]), 'shade', 'b', False)],
}

# Earl Eton: piel morena oscura; pelo castaño oscuro levantado en una torre de dos pinchos enormes hacia arriba con una
# muesca en medio y pinchos más pequeños a los lados; ojos blancos serios y boca de labios gruesos
CHARS['earl-eton'] = {
    'body': 'normal', 'pal': pal('#4a3a34', '#7a5034', iris='#2a2a2a', mouth='#a86a5a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'lips', 'mouth_y': 98, 'mouth_w': 8, 'hairline': (56, 44)},
    'front': [L(outline([(16, 62), (12, 40), (-10, 6, 1), (16, 14), (30, -40, 1), (46, -6), (50, -20), (54, -6), (70, -40, 1), (84, 14), (110, 6, 1), (88, 40), (84, 62),
                         (80, 52), (20, 52)])),
              L(outline([(56, -6), (70, -34), (82, 14), (100, 10), (86, 40), (76, 30)]), 'shade', 'b', False),
              L(outline([(30, -30), (40, -6), (34, 20)]), 'light', 'b', False)],
    'side': [L(outline([(56, 52), (64, 40), (82, 38), (92, 24), (88, 4), (110, -14, 1), (70, -6), (50, -50, 1), (40, -10), (6, -24, 1), (20, 8), (6, 30), (8, 58), (20, 76),
                        (36, 74), (46, 62)])),
             L(outline([(8, 30), (26, 38), (28, 66), (12, 60)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 76), (12, 40), (-12, 4, 1), (16, 14), (34, -40, 1), (46, -6), (50, -26), (54, -6), (66, -40, 1), (84, 14), (112, 4, 1), (88, 40), (84, 76),
                        (50, 84)])),
             L(outline([(56, -6), (66, -34), (82, 14), (102, 8), (86, 44), (82, 74), (62, 80)]), 'shade', 'b', False)],
}

# Caesar Cornell: pelo morado en forma de casco puntiagudo, con un pico alto en lo alto, aletas a los lados y dos mechones
# finos que bajan hasta la mandíbula; por detrás, la nuca rapada castaña; ojos de sueño
CHARS['caesar-cornell'] = {
    'body': 'normal', 'pal': pal('#7a4a9a', '#fce4c0', iris='#2a2a2a', buzz='#6a5050'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 62), (12, 30), (30, 0), (50, -28, 1), (70, 0), (88, 30), (84, 62), (78, 50), (22, 50)])),
              L(outline([(60, -8), (84, 26), (84, 56), (76, 44)]), 'shade', 'b', False),
              L(outline([(10, 52), (6, 6, 1), (16, 30), (18, 54)]), 'mid', 'f', ln=True), L(outline([(90, 52), (94, 6, 1), (84, 30), (82, 54)]), 'mid', 'f', ln=True),
              L(outline([(12, 54), (20, 54), (18, 104, 1), (12, 80)]), 'mid', 'f', ln=True), L(outline([(88, 54), (80, 54), (82, 104, 1), (88, 80)]), 'mid', 'f', ln=True),
              fringe([(16, 50), (24, 34), (40, 28), (50, 30), (60, 28), (76, 34), (84, 50), (70, 44), (50, 50), (30, 44)])]
             + white_eyes(77, 15, 6, 4.6, 1.8, lid=1.5),
    'side': [L(outline([(56, 58), (58, 46), (36, 36), (12, 40), (4, 60), (12, 84), (30, 90), (46, 78)]), 'buzz'),
             L(outline([(58, 54), (60, 40), (80, 40), (90, 26), (88, 4), (96, -20, 1), (78, -4), (50, -6), (20, -18), (-20, -40, 1), (8, 0), (12, 34), (36, 30), (54, 40)])),
             L(outline([(62, 50), (70, 50), (70, 100, 1), (62, 78)]), 'mid', 'f', ln=True)] + side_eye(77, lid=1),
    'back': [L(outline([(16, 74), (14, 40), (86, 40), (84, 74), (66, 88), (34, 88)]), 'buzz'),
             L(outline([(12, 50), (12, 30), (30, 0), (50, -28, 1), (70, 0), (88, 30), (88, 50), (50, 44)])),
             L(outline([(12, 50), (18, 54), (18, 100, 1), (12, 80)]), 'mid', 'f', ln=True), L(outline([(88, 50), (82, 54), (82, 100, 1), (88, 80)]), 'mid', 'f', ln=True)],
}

# Hampton Harvard: pelo castaño con una cresta redondeada en medio, puntas que se abren hacia fuera arriba a los lados y
# otras largas que se curvan en la mandíbula; ojos de sueño, dientes apretados y un palillo en la boca
CHARS['hampton-harvard'] = {
    'body': 'delgado', 'pal': pal('#6a5038', '#fce4b0', iris='#2a2a2a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 84), (-6, 108, 1), (6, 76), (8, 40), (-14, 20, 1), (16, 18), (30, 2), (50, -4), (70, 2), (84, 18), (114, 20, 1), (92, 40), (94, 76),
                         (106, 108, 1), (86, 84), (82, 62), (18, 62)])),
              L(outline([(60, 2), (84, 16), (92, 44), (90, 76), (80, 46)]), 'shade', 'b', False),
              fringe([(14, 64), (16, 40), (30, 24), (40, 20), (40, 4), (60, 4), (60, 20), (70, 24), (84, 40), (86, 64), (76, 52), (62, 44), (50, 54, 1), (38, 44),
                      (24, 52)]),
              L(outline([(42, 6), (58, 6), (56, 20), (44, 20)]), 'shade', 'f', False),
              L([(30, 102), (14, 116)], (200, 170, 120, 255), 'f', False, False, 1.4)] + white_eyes(78, 15, 6.4, 4.6, 1.8, lid=1.2),
    'side': [L(outline([(54, 62), (58, 50), (80, 48), (92, 34), (88, 12), (66, -2), (40, -2), (20, 4), (-20, -8, 1), (8, 20), (4, 52), (10, 76), (-10, 90, 1), (24, 84),
                        (40, 80)])),
             L(outline([(6, 30), (26, 40), (28, 76), (10, 72)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 42), (92, 62, 1), (84, 46), (74, 32)]),
             L([(84, 98), (100, 118)], (200, 170, 120, 255), 'f', False, False, 1.4)] + side_eye(78, lid=1),
    'back': [L(outline([(14, 84), (-8, 110, 1), (6, 76), (8, 40), (-14, 18, 1), (16, 16), (30, 2), (50, -4), (70, 2), (84, 16), (114, 18, 1), (92, 40), (94, 76),
                        (108, 110, 1), (86, 84), (50, 92)])),
             L(outline([(56, 2), (84, 16), (92, 50), (90, 80), (62, 88)]), 'shade', 'b', False)],
}

# Colby Columbia: pelo granate de llamas en punta hacia arriba y mechones largos a los lados hasta la mandíbula; una
# cicatriz en la mejilla y media sonrisa de chulo
CHARS['colby-columbia'] = {
    'body': 'normal', 'pal': pal('#8a1a30', '#fcd8b0', iris='#2a2a2a'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 92), (8, 70), (-6, 54, 1), (8, 44), (0, 18, 1), (18, 16), (20, -14, 1), (36, 2), (48, -34, 1), (58, -2), (76, -24, 1), (78, 6), (100, 0, 1),
                         (90, 24), (106, 40, 1), (92, 50), (92, 70), (86, 92), (82, 62), (18, 62)])),
              L(outline([(58, -2), (76, -18), (80, 8), (96, 4), (88, 30), (90, 70), (80, 50)]), 'shade', 'b', False),
              fringe([(14, 64), (18, 40), (30, 26), (50, 20), (70, 26), (82, 40), (86, 64), (74, 48), (66, 58, 1), (60, 44), (50, 60, 1), (42, 44), (34, 56, 1), (26, 48)])]
             + scar(22, 80, 36, 92),
    'side': [L(outline([(54, 62), (60, 50), (82, 48), (92, 34), (88, 12), (104, -8, 1), (70, 2), (60, -30, 1), (44, -2), (10, -24, 1), (20, 10), (-6, 20, 1), (6, 36),
                        (-10, 54, 1), (6, 60), (8, 90), (30, 96), (42, 80)])),
             L(outline([(6, 34), (26, 40), (28, 80), (10, 80)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 40), (92, 60, 1), (84, 46), (76, 34)])],
    'back': [L(outline([(14, 90), (8, 70), (-8, 54, 1), (8, 44), (-2, 18, 1), (18, 16), (22, -14, 1), (36, 2), (50, -34, 1), (60, -2), (78, -24, 1), (80, 6), (102, 0, 1),
                        (90, 24), (108, 40, 1), (92, 50), (92, 70), (86, 90), (50, 96)])),
             L(outline([(58, -2), (78, -18), (82, 8), (98, 4), (90, 30), (90, 86), (62, 94)]), 'shade', 'b', False)],
}

# Rex Remington: pelo gris de pinchos de punta hacia arriba, una cicatriz que le cruza la mejilla y arrugas de mal genio
CHARS['rex-remington'] = {
    'body': 'normal', 'pal': pal('#a8b0b0', '#fcd8b0', iris='#2a2a2a', shade='#888c8c', deep='#6a6e6e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': (60, 44)},
    'front': [L(outline([(16, 62), (12, 40), (6, 10, 1), (20, 16), (24, -14, 1), (36, 6), (48, -22, 1), (56, 4), (70, -16, 1), (76, 8), (94, 6, 1), (88, 40), (84, 62),
                         (80, 50), (20, 50)])),
              L(outline([(56, 4), (70, -10), (76, 8), (90, 8), (86, 40), (76, 30)]), 'shade', 'b', False),
              L([(40, 56), (44, 70)], OUTC, 'f', False, False, 1.0), L([(60, 56), (56, 70)], OUTC, 'f', False, False, 1.0)] + scar(24, 86, 34, 96),
    'side': [L(outline([(56, 54), (62, 44), (80, 42), (90, 28), (84, 10), (96, -4, 1), (70, 4), (60, -18, 1), (44, 2), (14, -8, 1), (20, 10), (-8, 20, 1), (8, 30),
                        (4, 58), (14, 74), (32, 76), (46, 64)])),
             L(outline([(6, 30), (26, 40), (28, 66), (10, 62)]), 'shade', 'b', False)] + scar(78, 92, 94, 98),
    'back': [L(outline([(16, 76), (12, 40), (4, 8, 1), (20, 16), (24, -14, 1), (36, 6), (50, -20, 1), (58, 4), (72, -14, 1), (78, 8), (96, 6, 1), (88, 40), (84, 76),
                        (50, 84)])),
             L(outline([(56, 4), (80, 12), (88, 46), (84, 74), (62, 82)]), 'shade', 'b', False)],
}

# Wenceslas Wales: pelo azul marino con dos alas de cuerno enormes que salen a los lados, un pico hasta la nariz y mechones
# hasta la mandíbula; ojos rojos y sonrisa abierta
CHARS['wenceslas-wales'] = {
    'body': 'normal', 'pal': pal('#3a4a8a', '#fcd4a8', iris='#c02020'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 96), (8, 66), (-20, 70, 1), (-12, 56), (-26, 20, 1), (8, 40), (14, 14), (16, -4, 1), (30, 6), (50, -8, 1), (70, 6), (84, -4, 1), (86, 14),
                         (92, 40), (126, 20, 1), (112, 56), (120, 70, 1), (92, 66), (86, 96), (82, 62), (18, 62)])),
              L(outline([(60, 4), (84, 6), (92, 40), (120, 26), (110, 56), (88, 70), (80, 50)]), 'shade', 'b', False),
              fringe([(14, 70), (16, 40), (30, 24), (50, 18), (70, 24), (84, 40), (86, 70), (76, 54), (62, 52), (50, 84, 1), (38, 52), (24, 54)])],
    'side': [L(outline([(54, 62), (60, 50), (82, 48), (92, 34), (88, 12), (96, -8, 1), (68, 2), (40, -2), (20, 4), (-26, -18, 1), (6, 24), (-16, 46, 1), (4, 52), (2, 80),
                        (16, 98), (36, 92), (44, 76)])),
             L(outline([(6, 30), (26, 40), (28, 86), (10, 84)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (96, 42), (92, 66), (86, 92, 1), (82, 56), (74, 36)])],
    'back': [L(outline([(16, 84), (10, 66), (-30, 70, 1), (-14, 54), (-30, 14, 1), (8, 40), (14, 14), (16, -4, 1), (30, 6), (50, -8, 1), (70, 6), (84, -4, 1), (86, 14),
                        (92, 40), (130, 14, 1), (114, 54), (130, 70, 1), (90, 66), (84, 84), (50, 90)])),
             L(outline([(56, 4), (84, 6), (92, 40), (124, 20), (112, 56), (86, 80), (62, 86)]), 'shade', 'b', False)],
}

# Sterling Stanford: cara larga y pálida; pelo morado con dos antenas altísimas en lo alto, un pico hasta la frente y la
# melena lisa que cae a los lados hasta los hombros; cara seria
CHARS['sterling-stanford'] = {
    'body': 'delgado', 'pal': pal('#5a4a7a', '#f0e0a4', iris='#5a7a8a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 104, 'hairline': False, 'face_front': LONG_FACE},
    'front': [L(outline([(8, 120), (2, 60), (-8, 30, 1), (8, 34), (14, 10), (24, -40, 1), (32, 0), (50, -10), (68, 0), (76, -40, 1), (86, 10), (92, 34), (108, 30, 1),
                         (98, 60), (92, 120), (82, 116), (80, 60), (20, 60), (18, 116)])),
              L(outline([(60, 0), (84, 12), (94, 50), (90, 112), (82, 108), (80, 50)]), 'shade', 'b', False),
              fringe([(16, 60), (20, 36), (34, 26), (50, 22), (66, 26), (80, 36), (84, 60), (70, 46), (58, 44), (50, 62, 1), (42, 44), (30, 46)])],
    'side': [L(outline([(56, 62), (60, 50), (82, 48), (92, 34), (88, 12), (70, 0), (68, -40, 1), (54, -4), (30, -2), (12, 12), (2, 40), (0, 116), (30, 118), (40, 90),
                        (46, 74)])),
             L(outline([(4, 40), (26, 44), (30, 110), (6, 110)]), 'shade', 'b', False),
             fringe([(66, 2), (90, 16), (94, 40), (90, 56, 1), (82, 42)])],
    'back': [L(outline([(8, 118), (2, 60), (-8, 30, 1), (8, 34), (14, 10), (24, -40, 1), (32, 0), (50, -10), (68, 0), (76, -40, 1), (86, 10), (92, 34), (108, 30, 1),
                        (98, 60), (92, 118), (50, 122)])),
             L(outline([(56, 0), (84, 12), (96, 50), (92, 116), (62, 120)]), 'shade', 'b', False)],
}

# Fred Featherstonhaugh (portero suplente): pelo azul verdoso en casco, con un pico en la frente y los lados largos que se
# curvan hacia dentro en la mandíbula y caen hasta el cuello; cara arrugada de ojos rojizos
CHARS['fred-featherstonhaugh'] = {
    'body': 'normal', 'pal': pal('#3a6a8a', '#fce4c4', iris='#8a2a2a'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': False},
    'front': [L(outline([(10, 104), (6, 40), (14, 10), (50, -4), (86, 10), (94, 40), (90, 104), (82, 104), (80, 62), (20, 62), (18, 104)])),
              L(outline([(60, 2), (86, 14), (94, 50), (90, 100), (80, 50)]), 'shade', 'b', False),
              fringe([(14, 70), (16, 38), (30, 22), (50, 18), (70, 22), (84, 38), (86, 70), (76, 54), (62, 50), (50, 64, 1), (38, 50), (24, 54)]),
              L(outline([(10, 84), (20, 100), (24, 112), (8, 108)]), 'mid', 'f', ln=True), L(outline([(90, 84), (80, 100), (76, 112), (92, 108)]), 'mid', 'f', ln=True),
              L([(36, 60), (44, 72)], OUTC, 'f', False, False, 1.0), L([(64, 60), (56, 72)], OUTC, 'f', False, False, 1.0)],
    'side': [L(outline([(56, 62), (60, 50), (82, 48), (92, 34), (88, 12), (66, -4), (36, -4), (12, 10), (2, 40), (2, 80), (-8, 102, 1), (18, 98), (34, 110), (40, 86),
                        (46, 74)])),
             L(outline([(4, 40), (26, 44), (30, 96), (8, 94)]), 'shade', 'b', False),
             fringe([(64, 2), (90, 16), (94, 40), (92, 60, 1), (82, 46), (74, 34)])],
    'back': [L(outline([(8, 96), (6, 40), (14, 10), (50, -4), (86, 10), (94, 40), (92, 96), (70, 102), (60, 94), (50, 106, 1), (40, 94), (30, 102)])),
             L(outline([(56, 2), (86, 14), (94, 50), (90, 94), (62, 100)]), 'shade', 'b', False)],
}

# Arthur Ascot: piel morena clara; pelo blanco crema de pinchos, con dos mechones largos arqueados como orejas de conejo en
# medio de la frente y una coleta baja atada atrás; ojos azules y sonrisa de pillo
CHARS['arthur-ascot'] = {
    'body': 'normal', 'pal': pal('#f2ead2', '#b88050', iris='#3a8ab8', shade='#d0b8a8', deep='#b09888', tie='#1e1e1e'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 96), (4, 72), (-12, 62, 1), (6, 50), (-6, 30, 1), (12, 26), (12, -2, 1), (28, 6), (50, -8, 1), (72, 6), (88, -2, 1), (88, 26), (106, 30, 1),
                         (94, 50), (112, 62, 1), (96, 72), (86, 96), (82, 64), (18, 64)])),
              L(outline([(60, 2), (84, 4), (92, 40), (90, 80), (80, 50)]), 'shade', 'b', False),
              fringe([(12, 66), (16, 40), (30, 26), (50, 22), (70, 26), (84, 40), (88, 66), (78, 50), (70, 60, 1), (64, 44), (56, 52, 1), (50, 40), (44, 52, 1),
                      (36, 44), (30, 58, 1), (22, 50)]),
              L(outline([(44, 40), (34, 10), (40, -20, 1), (48, 10), (50, 40)]), 'mid', 'f', ln=True),
              L(outline([(56, 40), (66, 10), (60, -20, 1), (52, 10), (50, 40)]), 'mid', 'f', ln=True)],
    'side': [L(outline([(54, 62), (60, 50), (82, 48), (92, 34), (88, 12), (70, -2), (78, -24, 1), (50, -4), (24, -10, 1), (24, 8), (-8, 10, 1), (8, 26), (-10, 40, 1),
                        (6, 50), (2, 74), (14, 86), (34, 84), (44, 74)])),
             L(outline([(14, 66), (4, 84), (-10, 112, 1), (8, 98), (20, 76)]), 'shade', 'b'), L(ell(14, 68, 4, 4), 'tie', 'f', ln=True),
             L(outline([(70, 6), (84, -16), (98, 0, 1), (88, 0), (80, 16)]), 'mid', 'f', ln=True),
             fringe([(64, 2), (90, 16), (96, 42), (92, 62, 1), (84, 46), (74, 32)])],
    'back': [L(outline([(16, 88), (4, 72), (-14, 60, 1), (6, 48), (-8, 26, 1), (12, 24), (12, -4, 1), (28, 6), (50, -10, 1), (72, 6), (88, -4, 1), (88, 24), (108, 26, 1),
                        (94, 48), (114, 60, 1), (96, 72), (84, 88), (50, 94)]), 'shade'),
             L(outline([(12, 24), (12, -4, 1), (28, 6), (50, -10, 1), (72, 6), (88, -4, 1), (88, 24), (70, 30), (50, 20), (30, 30)]), 'mid', 'b', False),
             L(outline([(44, 70), (40, 94), (52, 120, 1), (60, 96), (56, 70)]), 'shade', 'f', ln=True), L(ell(50, 72, 5, 4), 'tie', 'f', ln=True)],
}

# Stuart St. John: un tupé caqui enorme que se levanta en ola desde un lado y se curva hacia el otro, los lados cortos
# castaños; un punto en la frente, ojos naranjas de sueño y sonrisa
CHARS['stuart-st-john'] = {
    'body': 'normal', 'pal': pal('#c0b070', '#fcdcb8', iris='#d8701e', shade='#9a8a50', side='#9a7e52', side_d='#7a623e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': (56, 44)},
    'front': [L(outline([(16, 62), (14, 36), (26, 14), (74, 14), (86, 36), (84, 62), (80, 52), (20, 52)]), 'side'),
              L(outline([(14, 50), (16, 20), (30, 4), (20, -24), (60, -18, 1), (82, -4), (90, 20), (110, 36, 1), (86, 36), (66, 30), (40, 40), (24, 50)])),
              L(outline([(60, -14), (82, -2), (88, 22), (104, 34), (80, 32), (70, 10)]), 'shade', 'b', False),
              strand([(26, 0), (40, 20), (50, 36)], 'shade', 'b', 1.0), strand([(42, -10), (58, 10), (66, 28)], 'shade', 'b', 1.0),
              L(ell(50, 58, 1.6, 1.6), OUTC, 'f', False)] + white_eyes(78, 15, 6, 4.4, 2, lid=1.5),
    'side': [L(outline([(54, 54), (60, 40), (40, 26), (14, 24), (4, 50), (14, 80), (32, 84), (46, 70)]), 'side'),
             L(outline([(10, 34), (14, 10), (36, -2), (40, -20), (70, -30), (100, -28, 1), (76, -16), (66, 0), (80, 20), (90, 36), (66, 30), (40, 28)])),
             L(outline([(14, 30), (30, 10), (40, 26)]), 'shade', 'b', False)] + side_eye(78, lid=1),
    'back': [L(outline([(16, 72), (14, 36), (26, 14), (74, 14), (86, 36), (84, 72), (66, 88), (34, 88)]), 'side'),
             L(outline([(12, 44), (14, 16), (30, 0), (10, -16), (40, -26), (62, -14), (76, 4), (88, 20), (88, 44), (60, 40)])),
             L(outline([(2, -10), (14, 2), (10, -18)]), 'mid', 'b', False),
             L(outline([(56, -6), (80, 8), (88, 40), (66, 38)]), 'shade', 'b', False)],
}

# Yorick York: melena granate lisa con raya y un mechón largo que le tapa un ojo y le baja hasta la barbilla, el resto
# cae hasta el cuello; orejas grandes en punta, ojeras y una sonrisa torcida de dientes
CHARS['yorick-york'] = {
    'body': 'delgado', 'pal': pal('#5a2a2a', '#fce4c0', iris='#2a2a2a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 100, 'hairline': False, 'big_ears': 4, 'ear_out': 6, 'face_front': LONG_FACE},
    'front': [L(outline([(16, 90), (12, 40), (24, 6), (50, -10), (76, 6), (88, 40), (84, 90), (80, 60), (20, 60)])),
              L(outline([(60, -4), (84, 10), (90, 44), (84, 84), (78, 46)]), 'shade', 'b', False),
              fringe([(14, 62), (18, 34), (34, 12), (50, 4), (66, 12), (82, 34), (86, 62), (78, 46), (62, 34), (54, 50), (50, 76), (44, 112, 1), (36, 84), (30, 60),
                      (24, 52)]),
              L(ell(64, 76, 6.4, 4.4), OUTC, 'f', False), L(ell(64, 76, 5, 3), WHITE, 'f', False), L(ell(65, 76, 1.8, 2), OUTC, 'f', False)],
    'side': [L(outline([(56, 62), (60, 50), (82, 48), (92, 30), (84, 8), (64, -8), (36, -6), (14, 8), (4, 40), (4, 80), (20, 116, 1), (30, 96), (40, 80), (48, 70)])),
             L(outline([(6, 36), (26, 44), (30, 92), (10, 86)]), 'shade', 'b', False),
             fringe([(64, 0), (88, 14), (94, 40), (90, 70), (86, 104, 1), (82, 60), (74, 36)])],
    'back': [L(outline([(16, 92), (12, 40), (24, 6), (50, -10), (76, 6), (88, 40), (84, 92), (60, 100), (52, 118, 1), (44, 100)])),
             L(outline([(56, -4), (84, 10), (90, 50), (84, 90), (62, 96)]), 'shade', 'b', False),
             strand([(50, -10), (50, 40)], 'deep', 'b', 1.2)],
}
