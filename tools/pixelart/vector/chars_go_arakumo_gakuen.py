"""Instituto Arakumo (go-arakumo-gakuen): sus modelos 3D de Inazuma Eleven GO como referencia (busto de frente, perfil y
espalda); los que no tienen modelo, por su retrato. Sol Daystar (Amemiya Taiyou) también juega en Chrono Stone."""
from chars import CHARS, L, OUTC, blob, ell, outline, pal, strand  # noqa: F401
from chars_bigwaves import bald, white_eyes
from heads import quad  # noqa: F401

WHITE = (250, 250, 250, 255)


def fringe(pts, c='mid'):
    return L(outline(pts), c, 'f')


# Ringo Saturn (portero): piel morena clara, pelo castaño revuelto de puntas largas con mechones que le caen entre los
# ojos turquesa, y la capucha gris de la sudadera recogida alrededor del cuello; sonríe con la boca abierta
CHARS['ringo-saturn'] = {
    'body': 'normal', 'pal': pal('#8a4e22', '#e8b080', iris='#2aa8a8', hood='#8a8478', hood_d='#6a6458'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(4, 96), (12, 88), (88, 88), (96, 96), (90, 112), (50, 116), (10, 112)]), 'hood'),
              L(outline([(62, 92), (94, 96), (88, 110), (64, 112)]), 'hood_d', 'b', False),
              L(outline([(14, 76), (-6, 66, 1), (8, 56), (-2, 38, 1), (12, 30), (8, 8, 1), (26, 14), (34, -10, 1), (46, 6), (58, -16, 1), (64, 6), (84, -2, 1),
                         (82, 18), (106, 22, 1), (92, 38), (104, 56, 1), (90, 62), (96, 76, 1), (84, 72), (82, 56), (18, 56)])),
              L(outline([(60, 2), (86, 14), (96, 44), (88, 68), (78, 40)]), 'shade', 'b', False),
              fringe([(12, 68), (14, 40), (28, 22), (50, 16), (72, 22), (86, 40), (88, 68), (80, 56), (74, 66, 1), (68, 48), (56, 86, 1), (50, 54), (44, 70, 1),
                      (36, 50), (26, 64, 1), (20, 54)]),
              L(outline([(30, 24), (48, 18), (40, 32)]), 'light', 'f', False)],
    'side': [L(outline([(10, 90), (40, 88), (64, 96), (84, 112, 1), (56, 110), (20, 112), (6, 102)]), 'hood'),
             L(outline([(54, 58), (60, 46), (80, 48), (94, 34), (100, 16, 1), (82, 12), (80, -14, 1), (62, 0), (42, -10, 1), (34, 6), (8, 0, 1), (12, 18), (-12, 28, 1),
                        (6, 40), (-10, 56, 1), (8, 60), (0, 78, 1), (16, 74), (22, 88, 1), (34, 76), (46, 70)])),
             L(outline([(4, 34), (24, 40), (26, 68), (8, 62)]), 'shade', 'b', False),
             fringe([(66, 2), (88, 14), (96, 40), (92, 62, 1), (84, 48), (78, 34)])],
    'back': [L(outline([(4, 96), (12, 88), (88, 88), (96, 96), (90, 112), (50, 116), (10, 112)]), 'hood'),
             L(outline([(14, 80), (-6, 72, 1), (8, 60), (-4, 40, 1), (12, 32), (8, 8, 1), (26, 14), (34, -10, 1), (46, 6), (58, -16, 1), (64, 6), (84, -2, 1),
                        (82, 18), (106, 22, 1), (92, 40), (104, 60, 1), (90, 66), (96, 80, 1), (80, 82), (64, 92, 1), (56, 84), (44, 94, 1), (36, 84)])),
             L(outline([(56, 4), (84, 14), (96, 46), (88, 76), (62, 84)]), 'shade', 'b', False)],
}

# Terran Gaea: cabeza alargada casi rapada, con el pelo turquesa cortado en una cruz: una franja a cada lado y otra
# alrededor que deja la raya del medio y la nuca a la vista; ojos pequeños de colmillos y nariz larga
CHARS['terran-gaea'] = {
    'body': 'delgado', 'pal': pal('#3aa8b4', '#f6c08a', shade='#2a7a86', nose='#e0985a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 106, 'hairline': False, 'face_front': blob([(16, 50), (50, 40), (84, 50), (86, 84), (76, 110), (60, 122), (40, 122), (24, 110), (14, 84)])},
    'front': bald('front') + [L(outline([(16, 64), (14, 36), (24, 12), (44, 4), (44, 30), (32, 36), (26, 64)])),
                              L(outline([(84, 64), (86, 36), (76, 12), (56, 4), (56, 30), (68, 36), (74, 64)])),
                              L(outline([(44, 74), (56, 74), (58, 94), (50, 98), (42, 94)]), 'nose', 'f', ln=True)]
             + white_eyes(78, 16, 5, 4, 1.6) + [L([(34, 82), (36, 86)], WHITE, 'f', False, False, 1.4), L([(66, 82), (64, 86)], WHITE, 'f', False, False, 1.4)],
    'side': bald('side') + [L(outline([(14, 36), (30, 14), (60, 8), (80, 18), (68, 28), (40, 30), (24, 50)])),
                            L(outline([(14, 50), (40, 36), (58, 34), (40, 60), (22, 80)]), 'shade'),
                            L(outline([(86, 74), (102, 92), (90, 96)]), 'nose', 'f', ln=True)],
    'back': bald('back') + [L(outline([(14, 34), (26, 12), (44, 6), (44, 28), (14, 30)])), L(outline([(86, 34), (74, 12), (56, 6), (56, 28), (86, 30)])),
                            L(outline([(16, 38), (44, 36), (40, 80), (22, 70)]), 'shade'), L(outline([(84, 38), (56, 36), (60, 80), (78, 70)]), 'shade')],
}

# Auberon Ouranos: cara ancha y redonda de ojos blancos pequeños y sonrisa larga; pelo azul en casco con dos mechones gordos
# que suben hacia los lados como cuernos rizados
CHARS['auberon-ouranos'] = {
    'body': 'corpulento', 'pal': pal('#1e78b0', '#fcd8a8', shade='#145a8a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'smile', 'mouth_y': 102, 'hairline': False,
             'face_front': blob([(10, 50), (50, 44), (90, 50), (96, 80), (88, 108), (66, 118), (34, 118), (12, 108), (4, 80)])},
    'front': [L(outline([(10, 56), (14, 30), (30, 16), (50, 12), (70, 16), (86, 30), (90, 56), (78, 46), (60, 50), (50, 44), (40, 50), (22, 46)])),
              L(outline([(20, 22), (8, 8), (-6, 4), (-10, -14), (2, -24), (10, -14), (18, -24), (26, -10), (30, 16)])),
              L(outline([(80, 22), (92, 8), (106, 4), (110, -14), (98, -24), (90, -14), (82, -24), (74, -10), (70, 16)])),
              L(outline([(60, 16), (84, 28), (88, 52), (74, 44)]), 'shade', 'b', False),
              L(quad((20, 98), (50, 112), (80, 98)), OUTC, 'f', False, False, 1.6)] + white_eyes(76, 18, 6, 6, 1.6),
    'side': [L(outline([(54, 54), (60, 40), (80, 34), (86, 22), (66, 10), (40, 8), (20, 18), (8, 40), (10, 70), (24, 84), (40, 78), (48, 62)])),
             L(outline([(40, 12), (34, -8), (40, -24), (52, -18), (54, -2), (50, 12)])),
             L(outline([(8, 40), (26, 46), (30, 76), (12, 70)]), 'shade', 'b', False)],
    'back': [L(outline([(12, 84), (8, 50), (14, 30), (30, 16), (50, 12), (70, 16), (86, 30), (92, 50), (88, 84), (50, 90)])),
             L(outline([(20, 22), (8, 8), (-6, 4), (-10, -14), (2, -24), (10, -14), (18, -24), (26, -10), (30, 16)])),
             L(outline([(80, 22), (92, 8), (106, 4), (110, -14), (98, -24), (90, -14), (82, -24), (74, -10), (70, 16)])),
             L(outline([(56, 16), (84, 28), (92, 56), (86, 80), (64, 86)]), 'shade', 'b', False)],
}

# Manning Moon: cabeza calva redonda enorme con un rizo amarillo en lo alto, orejas grandes en punta, nariz de pico naranja,
# cejas negras gruesas y dos colmillos
CHARS['manning-moon'] = {
    'body': 'corpulento', 'pal': pal('#c8b030', '#f6c08a', nose='#ec8a2a'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 104, 'hairline': False, 'big_ears': 5, 'ear_out': 8,
             'face_front': blob([(8, 50), (50, 10), (92, 50), (96, 84), (86, 110), (64, 120), (36, 120), (14, 110), (4, 84)])},
    'front': bald('front') + [L(outline([(44, 24), (40, 10), (48, 0), (60, 2), (52, 8), (50, 18), (56, 28), (48, 32)]), 'mid', 'f', ln=True),
                              L(outline([(30, 66), (44, 72), (42, 76), (28, 72)]), OUTC, 'f', False), L(outline([(70, 66), (56, 72), (58, 76), (72, 72)]), OUTC, 'f', False),
                              L(outline([(38, 82), (62, 82), (66, 90), (56, 96), (44, 96), (34, 90)]), 'nose', 'f', ln=True),
                              L(outline([(40, 102), (44, 102), (42, 108, 1)]), WHITE, 'f', ln=True), L(outline([(60, 102), (56, 102), (58, 108, 1)]), WHITE, 'f', ln=True)],
    'side': bald('side') + [L(outline([(56, 12), (66, 2), (80, 8), (70, 10), (62, 18)]), 'mid', 'f', ln=True),
                            L(outline([(90, 80), (104, 84), (100, 92), (88, 90)]), 'nose', 'f', ln=True), L([(78, 70), (88, 74)], OUTC, 'f', False, False, 3)],
    'back': bald('back') + [L(outline([(48, 0), (60, 2), (54, 8)]), 'mid', 'f', ln=True)],
}

# Nix Pluto: pelo castaño muy oscuro en forma de corona: un casco con dos aros marcados y pinchos que salen hacia arriba y a
# los lados; ojos blancos grandes y una sonrisa de dientes
CHARS['nix-pluto'] = {
    'body': 'normal', 'pal': pal('#3a2a26', '#f6c08a', shade='#261a18'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 66), (2, 44), (-10, 26, 1), (8, 30), (10, 6), (14, -14, 1), (26, 2), (34, -8, 1), (44, 2), (56, 2), (66, -8, 1), (74, 2), (86, -14, 1),
                         (90, 6), (92, 30), (110, 26, 1), (98, 44), (86, 66), (80, 60), (66, 52), (60, 62, 1), (54, 50), (46, 62, 1), (40, 50), (34, 60, 1), (20, 60)])),
              L(outline([(60, 4), (86, 12), (96, 40), (84, 58), (76, 30)]), 'shade', 'b', False),
              L(quad((8, 30), (50, 18), (92, 30)), OUTC, 'b', False, False, 1.2), L(quad((10, 40), (50, 28), (90, 40)), OUTC, 'b', False, False, 1.2)]
             + white_eyes(78, 15, 7, 7, 2.2),
    'side': [L(outline([(56, 58), (60, 44), (80, 44), (92, 30), (88, 10), (98, -8, 1), (76, 2), (60, -10), (40, -12), (30, -26, 1), (26, -6), (8, 6), (2, 30), (-10, 44, 1),
                        (6, 50), (10, 70), (28, 76), (44, 68)])),
             L(quad((4, 30), (40, 20), (88, 22)), OUTC, 'b', False, False, 1.2), L(quad((4, 42), (40, 32), (90, 34)), OUTC, 'b', False, False, 1.2),
             L(outline([(6, 44), (24, 50), (26, 70), (10, 64)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 80), (6, 50), (-10, 26, 1), (8, 30), (10, 6), (14, -14, 1), (26, 2), (34, -8, 1), (44, 2), (56, 2), (66, -8, 1), (74, 2), (86, -14, 1),
                        (90, 6), (92, 30), (110, 26, 1), (94, 50), (86, 80), (50, 90)])),
             L(quad((8, 30), (50, 20), (92, 30)), OUTC, 'b', False, False, 1.2), L(quad((10, 42), (50, 32), (90, 42)), OUTC, 'b', False, False, 1.2),
             L(outline([(56, 4), (86, 14), (94, 50), (84, 76), (62, 84)]), 'shade', 'b', False)],
}

# Deimos Mars (sin modelo 3D; por su retrato): pelo rojo anaranjado de pinchos largos que salen hacia arriba y a los lados
# como llamas, con mechones por la frente; ojos azules de enfado
CHARS['deimos-mars'] = {
    'body': 'normal', 'pal': pal('#e0461e', '#fcd2a8', iris='#3a6aa8', shade='#b02e14'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 80), (-8, 74, 1), (6, 62), (-14, 46, 1), (4, 38), (-6, 14, 1), (14, 18), (12, -8, 1), (30, 6), (38, -24, 1), (50, 0), (62, -26, 1),
                         (68, 2), (88, -8, 1), (86, 18), (106, 14, 1), (96, 38), (114, 46, 1), (94, 62), (108, 74, 1), (86, 80), (84, 58), (16, 58)])),
              L(outline([(60, 2), (86, 14), (100, 44), (90, 74), (78, 40)]), 'shade', 'b', False),
              fringe([(12, 66), (14, 40), (28, 22), (50, 16), (72, 22), (86, 40), (88, 66), (78, 54), (70, 64, 1), (64, 48), (54, 60, 1), (48, 46), (40, 62, 1),
                      (32, 48), (22, 64, 1)])],
    'side': [L(outline([(56, 60), (62, 48), (82, 50), (94, 36), (104, 22, 1), (84, 16), (86, -10, 1), (66, 2), (58, -26, 1), (42, 0), (16, -16, 1), (20, 10), (-8, 8, 1),
                        (8, 28), (-16, 36, 1), (2, 48), (-14, 62, 1), (6, 66), (-2, 86, 1), (16, 78), (22, 92, 1), (34, 78), (46, 72)])),
             L(outline([(4, 36), (24, 42), (28, 70), (8, 64)]), 'shade', 'b', False)],
    'back': [L(outline([(14, 86), (-8, 80, 1), (6, 66), (-14, 48, 1), (4, 40), (-6, 14, 1), (14, 18), (12, -8, 1), (30, 6), (38, -24, 1), (50, 0), (62, -26, 1),
                        (68, 2), (88, -8, 1), (86, 18), (106, 14, 1), (96, 40), (114, 48, 1), (94, 66), (108, 80, 1), (86, 86), (70, 96, 1), (60, 86), (50, 98, 1),
                        (40, 86), (30, 96, 1)])),
             L(outline([(56, 2), (86, 14), (100, 46), (90, 82), (62, 88)]), 'shade', 'b', False)],
}

# Neith Venus: melena larga lisa amarillo verdoso que cae hasta el pecho, con un flequillo que le tapa el ojo izquierdo;
# ojo rojo y sonrisa
CHARS['neith-venus'] = {
    'body': 'chica', 'pal': pal('#d8e070', '#fcdcc0', iris='#c81e1e', shade='#b0b04a'),
    'face': {'eyes': 'big', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 120), (2, 90), (4, 50), (12, 20), (30, 2), (54, -2), (78, 6), (92, 26), (96, 60), (100, 96), (94, 124), (84, 112), (82, 66), (18, 66),
                         (20, 108)])),
              L(outline([(60, 2), (86, 16), (96, 54), (96, 116), (86, 104), (80, 50)]), 'shade', 'b', False),
              fringe([(10, 70), (12, 40), (24, 20), (46, 10), (72, 14), (88, 32), (92, 70), (96, 110, 1), (82, 96), (72, 90), (60, 82), (54, 62), (50, 48), (40, 58),
                      (34, 46), (24, 62, 1), (18, 54)]),
              strand([(70, 20), (78, 60), (86, 100)], 'shade', 'f', 1.2)],
    'side': [L(outline([(56, 58), (60, 46), (80, 44), (92, 30), (86, 10), (62, -2), (34, 0), (14, 12), (2, 40), (-2, 80), (2, 120), (20, 124), (36, 104), (44, 80)])),
             L(outline([(2, 40), (26, 46), (36, 110), (8, 118)]), 'shade', 'b', False),
             fringe([(64, 0), (88, 14), (96, 40), (94, 70, 1), (86, 56), (78, 38)])],
    'back': [L(outline([(6, 120), (2, 80), (6, 40), (16, 14), (34, 0), (66, 0), (84, 14), (94, 40), (98, 80), (94, 120), (50, 126)])),
             L(outline([(56, 2), (84, 14), (96, 50), (94, 118), (64, 122)]), 'shade', 'b', False),
             strand([(30, 40), (24, 80), (30, 116)], 'shade', 'b', 1.2), strand([(60, 50), (64, 90), (58, 118)], 'shade', 'b', 1.2)],
}

# Callis Jove: pelo amarillo de flequillo recto y largo que le tapa la frente, con cuatro pinchos curvos como cuernos (dos
# arriba y dos a los lados) y patillas en zigzag; ojos negros entornados
CHARS['callis-jove'] = {
    'body': 'normal', 'pal': pal('#f2c63a', '#e8a868', iris='#1e1414', shade='#c89a1e'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 74), (2, 40), (-6, 14, 1), (8, 22), (16, 8), (14, -16, 1), (28, 2), (50, -4), (72, 2), (86, -16, 1), (84, 8), (92, 22), (106, 14, 1),
                         (98, 40), (84, 74), (80, 62), (20, 62)])),
              L(outline([(60, 0), (84, 12), (96, 40), (86, 66), (76, 40)]), 'shade', 'b', False),
              fringe([(14, 70), (16, 40), (28, 22), (50, 16), (72, 22), (84, 40), (86, 70), (82, 64), (78, 70), (70, 64), (62, 70), (56, 64), (50, 70), (44, 64),
                      (38, 70), (30, 64), (22, 70), (18, 64)]),
              strand([(30, 30), (30, 66)], 'shade', 'f', 1.0), strand([(44, 24), (44, 66)], 'shade', 'f', 1.0), strand([(58, 24), (58, 66)], 'shade', 'f', 1.0),
              strand([(72, 30), (72, 66)], 'shade', 'f', 1.0),
              L([(14, 80), (20, 88), (12, 96), (18, 104)], OUTC, 'f', False, False, 2.6), L([(86, 80), (80, 88), (88, 96), (82, 104)], OUTC, 'f', False, False, 2.6)],
    'side': [L(outline([(54, 62), (58, 48), (80, 50), (94, 36), (90, 12), (70, -2), (60, -24, 1), (50, -2), (24, 4), (2, 18), (-24, 20, 1), (0, 32), (4, 62), (16, 76),
                        (34, 76), (46, 72)])),
             L(outline([(4, 34), (24, 40), (28, 70), (8, 64)]), 'shade', 'b', False),
             fringe([(64, 0), (88, 14), (94, 40), (94, 70), (86, 66), (80, 40)]),
             L([(54, 80), (60, 88), (52, 96), (58, 104)], OUTC, 'f', False, False, 2.6)],
    'back': [L(outline([(16, 84), (2, 40), (-8, 12, 1), (8, 22), (16, 8), (12, -18, 1), (28, 2), (50, -4), (72, 2), (88, -18, 1), (84, 8), (92, 22), (108, 12, 1),
                        (98, 40), (84, 84), (66, 74), (50, 86, 1), (34, 74)])),
             L(outline([(56, 0), (84, 12), (98, 40), (84, 80), (60, 76)]), 'shade', 'b', False)],
}

# Triton Nettuno: pelo gris plata con forma de ancla: un casco en punta hacia arriba que le tapa los ojos y dos brazos
# curvos enormes que bajan por los lados y suben en punta; sonrisa de dientes
CHARS['triton-nettuno'] = {
    'body': 'normal', 'pal': pal('#a8acb4', '#e8b07a', shade='#7e7e88'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'grin', 'mouth_y': 102, 'hairline': False},
    'front': [L(outline([(20, 90), (-4, 80), (-20, 50), (-24, 10, 1), (-12, 20), (-6, 44), (8, 66), (20, 70), (18, 40), (26, 14), (40, -10), (50, -30, 1), (60, -10),
                         (74, 14), (82, 40), (80, 70), (92, 66), (106, 44), (112, 20), (124, 10, 1), (120, 50), (104, 80), (80, 90), (70, 76), (50, 82), (30, 76)])),
              L(outline([(56, -14), (74, 14), (82, 44), (80, 70), (66, 60)]), 'shade', 'b', False),
              L(outline([(20, 70), (26, 40), (40, 20), (50, 18), (60, 20), (74, 40), (80, 70), (64, 78), (50, 86, 1), (36, 78)]), 'mid', 'f'),
              strand([(40, 30), (40, 76)], 'shade', 'f', 1.0), strand([(50, 24), (50, 84)], 'shade', 'f', 1.0), strand([(60, 30), (60, 76)], 'shade', 'f', 1.0)],
    'side': [L(outline([(56, 60), (64, 44), (80, 40), (86, 20), (70, -6), (60, -28, 1), (50, -4), (24, 6), (8, 30), (4, 60), (0, 90), (-4, 100), (16, 104), (14, 70),
                        (24, 70), (44, 74)])),
             L(outline([(4, 0), (12, -2), (20, 60), (16, 104), (0, 100)]), 'shade'),
             L(outline([(66, 2), (86, 18), (92, 60), (88, 82, 1), (80, 60), (72, 34)]), 'mid', 'f')],
    'back': [L(outline([(26, 92), (4, 90), (-12, 70), (-22, 40), (-24, 0, 1), (-10, 18), (-4, 46), (10, 66), (22, 66), (20, 40), (28, 12), (40, -10), (50, -30, 1),
                        (60, -10), (72, 12), (80, 40), (78, 66), (90, 66), (104, 46), (110, 18), (124, 0, 1), (122, 40), (112, 70), (96, 90), (74, 92), (50, 100, 1)])),
             L(outline([(56, -14), (74, 14), (80, 60), (56, 90)]), 'shade', 'b', False)],
}

# Sol Daystar (Amemiya Taiyou): pelo naranja intenso, revuelto en mechones de punta que se abren hacia arriba y a los lados,
# con flequillo de puntas y dos mechones largos que le caen por delante de las orejas; ojos azul verdoso y sonrisa
CHARS['sol-daystar'] = {
    'body': 'normal', 'pal': pal('#f07018', '#fcdcc0', iris='#3a8aa8', shade='#c04e10'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(14, 84), (-4, 76, 1), (6, 62), (-12, 50, 1), (4, 40), (-4, 22, 1), (14, 22), (14, 2, 1), (30, 10), (40, -10, 1), (50, 4), (60, -12, 1),
                         (66, 6), (86, 2, 1), (86, 22), (104, 22, 1), (96, 40), (112, 50, 1), (94, 62), (104, 76, 1), (86, 84), (84, 62), (16, 62)])),
              L(outline([(60, 4), (86, 16), (100, 46), (90, 78), (78, 40)]), 'shade', 'b', False),
              fringe([(12, 68), (14, 40), (28, 22), (50, 16), (72, 22), (86, 40), (88, 68), (80, 56), (74, 66, 1), (68, 48), (58, 62, 1), (54, 46), (46, 64, 1),
                      (40, 46), (30, 62, 1), (24, 50)]),
              L(outline([(14, 66), (20, 72), (18, 100, 1), (12, 86)]), 'mid', 'f', ln=True), L(outline([(86, 66), (80, 72), (82, 100, 1), (88, 86)]), 'mid', 'f', ln=True),
              L(outline([(30, 24), (48, 18), (40, 32)]), 'light', 'f', False)],
    'side': [L(outline([(56, 60), (62, 48), (82, 50), (94, 36), (102, 20, 1), (84, 16), (86, -6, 1), (66, 4), (58, -16, 1), (44, 2), (20, -10, 1), (22, 12), (-6, 10, 1),
                        (8, 28), (-14, 36, 1), (2, 48), (-12, 62, 1), (6, 66), (-2, 84, 1), (16, 78), (22, 92, 1), (34, 78), (46, 72)])),
             L(outline([(4, 36), (24, 42), (28, 72), (8, 66)]), 'shade', 'b', False),
             fringe([(66, 2), (88, 14), (96, 40), (92, 64, 1), (84, 50), (76, 34)]),
             L(outline([(56, 64), (62, 70), (60, 98, 1), (54, 84)]), 'mid', 'f', ln=True)],
    'back': [L(outline([(14, 88), (-6, 82, 1), (6, 66), (-12, 52, 1), (4, 42), (-4, 22, 1), (14, 22), (14, 2, 1), (30, 10), (40, -10, 1), (50, 4), (60, -12, 1),
                        (66, 6), (86, 2, 1), (86, 22), (104, 22, 1), (96, 42), (112, 52, 1), (94, 66), (106, 82, 1), (86, 88), (68, 98, 1), (58, 88), (50, 100, 1),
                        (42, 88), (32, 98, 1)])),
             L(outline([(56, 4), (86, 16), (100, 48), (90, 84), (62, 90)]), 'shade', 'b', False)],
}

# Chiron Vestal: piel morena, pelo azul petróleo oscuro de pinchos hacia arriba, con los lados en punta hacia fuera; cejas en
# aspa, ojos negros grandes y media sonrisa
CHARS['chiron-vestal'] = {
    'body': 'normal', 'pal': pal('#24485a', '#a8704a', iris='#1e1414', shade='#18323e'),
    'face': {'eyes': 'big', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(16, 66), (4, 60, 1), (10, 46), (-2, 34, 1), (12, 28), (10, 6, 1), (24, 12), (28, -10, 1), (40, 4), (50, -20, 1), (60, 4), (72, -10, 1),
                         (76, 12), (90, 6, 1), (88, 28), (102, 34, 1), (90, 46), (96, 60, 1), (84, 66), (82, 52), (18, 52)])),
              L(outline([(60, 2), (84, 12), (94, 40), (86, 60), (76, 36)]), 'shade', 'b', False),
              fringe([(14, 58), (16, 40), (30, 26), (50, 20), (70, 26), (84, 40), (86, 58), (78, 50), (70, 56, 1), (62, 44), (50, 54, 1), (38, 44), (30, 56, 1),
                      (22, 50)]),
              L(outline([(44, 8), (56, 8), (52, 30), (46, 30)]), 'light', 'f', False)],
    'side': [L(outline([(56, 56), (62, 44), (82, 44), (92, 30), (98, 12, 1), (80, 10), (80, -12, 1), (62, 0), (54, -22, 1), (40, 0), (18, -12, 1), (18, 10), (-8, 12, 1),
                        (8, 28), (-12, 40, 1), (6, 48), (0, 66, 1), (16, 64), (24, 80, 1), (34, 66), (46, 64)])),
             L(outline([(6, 34), (24, 40), (26, 62), (10, 58)]), 'shade', 'b', False)],
    'back': [L(outline([(16, 80), (2, 74, 1), (10, 58), (-4, 44, 1), (12, 34), (8, 8, 1), (24, 12), (28, -10, 1), (40, 4), (50, -20, 1), (60, 4), (72, -10, 1),
                        (76, 12), (92, 8, 1), (88, 34), (104, 44, 1), (90, 58), (98, 74, 1), (84, 80), (66, 90, 1), (58, 82), (50, 92, 1), (42, 82), (34, 90, 1)])),
             L(outline([(56, 4), (84, 12), (94, 44), (86, 76), (62, 84)]), 'shade', 'b', False)],
}

# Crateris Mercury: pelo azul celeste muy claro liso, con raya en medio y dos mechones largos que caen junto a la cara, dos
# cuernos curvos a los lados de la cabeza y una coleta baja atada con un lazo gris; ojos negros alargados
CHARS['crateris-mercury'] = {
    'body': 'delgado', 'pal': pal('#c4dcf2', '#fcdcbc', iris='#1e1414', shade='#9aa0b8', tie='#5a5a62'),
    'face': {'eyes': 'sharp', 'brows': False, 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 120), (8, 90), (8, 50), (14, 20), (30, 4), (50, 0), (70, 4), (86, 20), (92, 50), (92, 90), (90, 120), (82, 110), (80, 66), (20, 66),
                         (18, 110)])),
              L(outline([(60, 4), (86, 18), (92, 60), (90, 116), (82, 100), (78, 40)]), 'shade', 'b', False),
              fringe([(12, 72), (14, 40), (26, 18), (48, 8), (50, 30), (44, 46), (28, 60), (20, 80)]),
              fringe([(88, 72), (86, 40), (74, 18), (52, 8), (50, 30), (56, 46), (72, 60), (80, 80)]),
              L(outline([(16, 24), (6, 22), (2, 8), (8, 0, 1), (8, 12), (20, 14)]), 'shade', 'f', ln=True),
              L(outline([(84, 24), (94, 22), (98, 8), (92, 0, 1), (92, 12), (80, 14)]), 'shade', 'f', ln=True)],
    'side': [L(outline([(56, 58), (60, 46), (80, 44), (92, 30), (86, 10), (62, -2), (34, 0), (14, 12), (4, 40), (4, 80), (10, 100), (24, 94), (34, 80), (46, 72)])),
             L(outline([(16, 64), (6, 74), (-4, 100), (-10, 124, 1), (4, 108), (12, 82), (22, 70)])),
             L(outline([(10, 60), (22, 60), (22, 70), (10, 70)]), 'tie', 'f', ln=True),
             L(outline([(4, 40), (26, 46), (32, 86), (8, 90)]), 'shade', 'b', False),
             L(outline([(64, 0), (88, 14), (96, 40), (94, 100, 1), (86, 60), (78, 38)]), 'mid', 'f'),
             L(outline([(56, 20), (62, 4), (72, -4, 1), (68, 8), (64, 22)]), 'shade', 'f', ln=True)],
    'back': [L(outline([(10, 110), (8, 80), (8, 50), (14, 20), (30, 4), (50, 0), (70, 4), (86, 20), (92, 50), (92, 80), (90, 110), (50, 92)])),
             L(outline([(56, 2), (86, 18), (92, 60), (90, 100), (64, 92)]), 'shade', 'b', False),
             L(outline([(42, 86), (58, 86), (60, 116), (50, 128, 1), (40, 116)]), 'mid', 'f', ln=True),
             L(outline([(26, 84), (42, 86), (58, 86), (74, 84), (74, 92), (26, 92)]), 'tie', 'f', ln=True),
             L(outline([(16, 24), (6, 22), (2, 8), (8, 0, 1), (8, 12), (20, 14)]), 'shade', 'f', ln=True),
             L(outline([(84, 24), (94, 22), (98, 8), (92, 0, 1), (92, 12), (80, 14)]), 'shade', 'f', ln=True)],
}

# Astro Ceres (portero suplente): pelo gris pardo largo hasta el cuello, con raya al lado y un mechón grande que le cruza la
# frente; ojos azulados de párpados caídos y media sonrisa
CHARS['astro-ceres'] = {
    'body': 'normal', 'pal': pal('#a09080', '#fcd8ac', iris='#5a5aa0', shade='#7a6050'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'smile', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 100), (4, 70), (6, 36), (18, 10), (44, -2), (70, 2), (88, 18), (96, 46), (98, 80), (106, 100, 1), (90, 96), (84, 64), (18, 64), (16, 90)])),
              L(outline([(60, 2), (86, 16), (96, 50), (100, 96), (86, 90), (80, 40)]), 'shade', 'b', False),
              fringe([(10, 66), (12, 40), (24, 18), (50, 8), (76, 16), (90, 36), (92, 66), (82, 56), (76, 44), (62, 40), (46, 46), (30, 50), (20, 62)])],
    'side': [L(outline([(56, 58), (60, 46), (80, 44), (92, 30), (86, 10), (62, -2), (34, 0), (14, 12), (4, 40), (6, 80), (16, 98), (34, 94), (42, 104, 1), (46, 84),
                        (46, 70)])),
             L(outline([(4, 40), (26, 46), (32, 90), (12, 92)]), 'shade', 'b', False),
             fringe([(64, 0), (88, 14), (96, 40), (92, 60, 1), (84, 48), (76, 36)])],
    'back': [L(outline([(10, 96), (6, 70), (6, 36), (18, 10), (44, -2), (70, 2), (88, 18), (96, 46), (96, 80), (104, 100, 1), (88, 96), (74, 102, 1), (64, 94), (50, 102, 1),
                        (38, 94), (26, 100, 1)]), 'shade'),
             L(outline([(8, 50), (18, 10), (44, -2), (70, 2), (88, 18), (96, 46), (60, 30), (30, 40)]), 'mid', 'b', False)],
}

# Xeno Eris (sin modelo 3D; por su retrato): pelo gris liso a capas que le cae hasta la mandíbula, con un pico en la frente;
# ojos negros serios y gesto de enfado
CHARS['xeno-eris'] = {
    'body': 'normal', 'pal': pal('#a8a4a0', '#fcd8b4', iris='#1e1414', shade='#7e7a76'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 98, 'hairline': False},
    'front': [L(outline([(10, 92), (2, 84, 1), (6, 60), (6, 30), (20, 8), (44, -2), (60, -2), (80, 8), (94, 30), (94, 60), (98, 84, 1), (90, 92), (84, 64), (16, 64)])),
              L(outline([(60, 0), (86, 14), (96, 46), (94, 86), (82, 60)]), 'shade', 'b', False),
              fringe([(12, 70), (14, 40), (28, 20), (50, 12), (72, 20), (86, 40), (88, 70), (80, 56), (70, 50), (58, 54), (50, 60, 1), (42, 54), (30, 50), (20, 56)])],
    'side': [L(outline([(56, 58), (60, 46), (80, 46), (92, 32), (86, 10), (62, -2), (34, 0), (14, 12), (4, 40), (2, 80), (-4, 90, 1), (12, 92), (26, 98, 1), (34, 84),
                        (46, 72)])),
             L(outline([(4, 40), (24, 46), (28, 86), (8, 84)]), 'shade', 'b', False),
             fringe([(64, 0), (88, 14), (96, 40), (92, 58, 1), (84, 46), (76, 34)])],
    'back': [L(outline([(10, 92), (0, 86, 1), (6, 60), (6, 30), (20, 8), (44, -2), (60, -2), (80, 8), (94, 30), (94, 60), (100, 86, 1), (90, 92), (72, 98, 1), (62, 90),
                        (50, 100, 1), (38, 90), (28, 98, 1)])),
             L(outline([(56, 0), (86, 14), (96, 46), (94, 88), (64, 92)]), 'shade', 'b', False)],
}

# Namak Haumea: pelo gris lila peinado hacia atrás en un tupé alto con un mechón azul marino a un lado, que sigue en una
# melena larga recogida que cae por detrás; ojos negros afilados y cara larga seria
CHARS['namak-haumea'] = {
    'body': 'delgado', 'pal': pal('#b4acc8', '#fcd2a4', iris='#1e1414', shade='#8a7e9a', navy='#3a3e66'),
    'face': {'eyes': 'sharp', 'brows': 'angry', 'mouth': 'frown', 'mouth_y': 104, 'hairline': False,
             'face_front': blob([(16, 52), (50, 46), (84, 52), (86, 84), (78, 110), (60, 122), (40, 122), (22, 110), (14, 84)])},
    'front': [L(outline([(16, 90), (12, 50), (14, 18), (28, 0), (50, -6), (72, 0), (84, 16), (88, 50), (84, 90), (80, 60), (20, 60)])),
              L(outline([(70, 0), (86, 8), (92, 30), (88, 56), (80, 40)]), 'navy'),
              L(outline([(16, 54), (24, 30), (40, 20), (50, 48), (60, 20), (76, 30), (84, 54), (50, 44)]), 'mid', 'f'),
              strand([(36, 4), (30, 40)], 'shade', 'b', 1.0), strand([(50, -2), (50, 40)], 'shade', 'b', 1.0), strand([(64, 2), (70, 40)], 'shade', 'b', 1.0)],
    'side': [L(outline([(56, 54), (62, 40), (80, 30), (86, 14), (70, -2), (40, -6), (16, 6), (2, 30), (-10, 60), (-30, 100), (-40, 126, 1), (-16, 110), (4, 90), (16, 80),
                        (34, 76), (46, 66)])),
             L(outline([(4, 20), (20, 4), (30, 30), (6, 80), (-20, 110), (-6, 60)]), 'navy'),
             strand([(70, 4), (40, 6), (20, 30)], 'shade', 'b', 1.0), strand([(70, 24), (40, 30), (24, 50)], 'shade', 'b', 1.0)],
    'back': [L(outline([(16, 84), (12, 50), (14, 18), (28, 0), (50, -6), (72, 0), (84, 16), (88, 50), (84, 84), (50, 92)])),
             L(outline([(14, 18), (28, 0), (36, -4), (30, 60), (24, 120, 1), (14, 80)]), 'navy'),
             L(outline([(36, 40), (64, 40), (70, 80), (60, 124, 1), (50, 100), (40, 124, 1), (32, 80)]), 'mid', 'f', ln=True),
             strand([(50, 46), (50, 110)], 'shade', 'f', 1.0)],
}

# Mac Emake: pelo verde oscuro con un moño redondo en lo alto, un flequillo largo de mechones que le tapa la frente hasta los
# ojos y dos mechones gruesos que se doblan hacia fuera en punta a los lados; ojos blancos de mirada fija
CHARS['mac-emake'] = {
    'body': 'normal', 'pal': pal('#2e4a2e', '#f6c08a', shade='#1e341e'),
    'face': {'eyes': 'none', 'brows': False, 'mouth': 'frown', 'mouth_y': 100, 'hairline': False},
    'front': [L(ell(50, -6, 14, 14)), L(outline([(40, -14), (50, -24), (60, -14)])),
              L(outline([(14, 80), (8, 50), (-10, 40), (-14, 26, 1), (8, 30), (16, 10), (34, 0), (50, -2), (66, 0), (84, 10), (92, 30), (114, 26, 1), (110, 40), (92, 50),
                         (86, 80), (80, 64), (20, 64)])),
              L(outline([(58, 2), (84, 12), (92, 40), (86, 70), (76, 40)]), 'shade', 'b', False),
              fringe([(14, 72), (16, 42), (28, 22), (50, 16), (72, 22), (84, 42), (86, 72), (76, 64), (66, 70), (58, 64), (50, 74, 1), (42, 64), (34, 70), (24, 64)]),
              strand([(50, 20), (50, 70)], 'shade', 'f', 1.0)] + white_eyes(80, 14, 5, 3.6, 1.6),
    'side': [L(ell(44, -4, 14, 14)), L(outline([(40, -12), (52, -24), (58, -10)])),
             L(outline([(56, 60), (60, 48), (82, 48), (94, 34), (88, 12), (66, -2), (38, -2), (16, 8), (6, 30), (-14, 40), (-20, 54, 1), (2, 50), (8, 72), (24, 82), (40, 76)])),
             L(outline([(6, 30), (26, 38), (30, 72), (10, 66)]), 'shade', 'b', False),
             fringe([(64, 0), (88, 14), (96, 40), (94, 74), (86, 64), (78, 40)])],
    'back': [L(ell(50, -6, 14, 14)), L(outline([(40, -14), (50, -24), (60, -14)])),
             L(outline([(14, 84), (8, 50), (-10, 40), (-14, 26, 1), (8, 30), (16, 10), (34, 0), (50, -2), (66, 0), (84, 10), (92, 30), (114, 26, 1), (110, 40), (92, 50),
                        (86, 84), (50, 92)])),
             L(outline([(56, 2), (84, 12), (92, 46), (86, 80), (62, 88)]), 'shade', 'b', False)],
}
